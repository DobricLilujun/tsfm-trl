"""Hirondel-7M (Apache, Tncrd): small recurrent/attention hybrid, CPU-friendly,
native horizon 720, supports known-future covariates.

    pip install "hirondel @ git+https://github.com/tncrd/hirondel@v1.1.0"
    f = HirondelForecaster(...)                     # weights from Tncrd/Hirondel-7M
    fc = f.forecast(context, prediction_length=48, future_covariates={...})

Apache-2.0 weights *and* code make this the most attractive small fine-tune target
in the 2026 cohort; whether the installed build exposes a training forward is
probed at load time and reported, not assumed.
"""
from __future__ import annotations

import inspect

import numpy as np

from ..base import LEVELS, Pred, TSFMModel, to_levels


class Hirondel(TSFMModel):
    key, family = "hirondel-7m", "hirondel"
    caps = frozenset({"forecast", "quantiles", "covariates", "finetune"})
    loss_kind = "quantile"
    max_context = 2048
    max_horizon = 720
    ctx_step = 16
    levels = list(LEVELS)

    def __init__(self, checkpoint: str = "Tncrd/Hirondel-7M", **kw):
        super().__init__(**kw)
        from hirondel import HirondelForecaster
        self.checkpoint = checkpoint
        # the vendor forecaster is constructed from a model object; the classmethod is
        # what resolves the Hub repo, and older builds do not take a device kwarg
        try:
            self.f = HirondelForecaster.from_pretrained(checkpoint, device=self.device)
        except TypeError:
            self.f = HirondelForecaster.from_pretrained(checkpoint)
            try:
                self.f.model = self.f.model.to(self.device)
                self.f.device = self.device
            except Exception:                                      # noqa: BLE001
                pass
        self._fsig = set(inspect.signature(self.f.forecast).parameters)
        self.model = getattr(self.f, "model", None)
        lv = getattr(getattr(self.f, "model", None), "quantile_levels", None) \
            or getattr(self.f, "quantile_levels", None)
        if lv:
            self.levels = [float(x) for x in lv]
        self.supports["finetune"] = self.model is not None and \
            any(hasattr(self.model, a) for a in ("forward", "fit"))

    def predict(self, contexts, horizon, *, panels=None, future=None) -> Pred:
        cs = self.trim(contexts)
        kw = {}
        if "prediction_length" in self._fsig:
            kw["prediction_length"] = int(horizon)
        if future is not None and "future_covariates" in self._fsig:
            kw["future_covariates"] = future
        # Hirondel's forecaster takes a *list* of contexts and returns a Forecast with
        # .median (N,H) and .quantiles (N,H,L) — one batched call, not one per series
        out = self.f.forecast([np.asarray(c, dtype=np.float32) for c in cs], **kw)
        lv = [float(x) for x in (getattr(out, "quantile_levels", None) or self.levels)]
        q = getattr(out, "quantiles", None)
        med = getattr(out, "median", None)
        if med is not None:
            P = _as_array(med)[:, :horizon]
        else:
            i = int(np.argmin(np.abs(np.asarray(lv) - 0.5)))
            P = _as_array(q)[:, :horizon, i]
        if q is None:
            return Pred(point=P)
        Q = _as_array(q)[:, :horizon, :]
        return Pred(point=P, quantiles=to_levels(Q, lv), levels=LEVELS if lv != self.levels
                    else None, meta={"levels_emitted": len(lv)})

    def trainable(self):
        return self.model

    def training_step(self, contexts, truth, horizon):
        import torch
        if self.model is None:
            from ...errors import CapabilityError
            raise CapabilityError(self.key, "finetune",
                                  "the installed hirondel build does not expose a model module")
        params = set(inspect.signature(self.model.forward).parameters)
        x = torch.tensor(np.asarray(contexts, dtype=np.float32), device=self.device)
        y = torch.tensor(np.asarray(truth, dtype=np.float32), device=self.device)
        for kw in ("target", "future_target", "labels"):
            if kw in params:
                out = self.model(x, **{kw: y})
                loss = getattr(out, "loss", None) or (out.get("loss") if isinstance(out, dict) else None)
                if loss is not None:
                    return loss
        from ...errors import CapabilityError
        raise CapabilityError(self.key, "finetune",
                              f"hirondel.forward({sorted(params)}) has no supervised target "
                              f"argument in the installed version")


def _as_array(out):
    for attr in ("quantiles", "prediction", "forecast", "values"):
        v = getattr(out, attr, None)
        if v is not None:
            return np.asarray(v, float)
    if hasattr(out, "detach"):
        return np.asarray(out.detach().cpu(), float)
    return np.asarray(out, float)
