"""The Forecasting Company t0 family (t0-alpha/beta/gamma), via ``tfc-t0``.

    pip install "tfc-t0[torch]"
    model = T0Forecaster.from_pretrained("theforecastingcompany/t0-gamma")
    out   = model.predict(context, horizon=64, quantile_levels=[...])   # .quantiles, .median

The public package documents inference; there is no public training forward, so
fine-tuning is reported as ``n/a`` with that reason rather than approximated.
"""
from __future__ import annotations

import numpy as np

from ..base import to_numpy, Pred, TSFMModel, to_levels


class T0(TSFMModel):
    key, family = "t0-gamma", "t0"
    caps = frozenset({"forecast", "quantiles", "covariates"})
    loss_kind = None
    max_context = 4096
    max_horizon = 1024
    levels = [0.01, 0.05] + [round(0.05 * i, 2) for i in range(2, 19)] + [0.95, 0.99]

    def __init__(self, checkpoint: str = "theforecastingcompany/t0-gamma", **kw):
        super().__init__(**kw)
        from t0 import T0Forecaster
        self.checkpoint = checkpoint
        self.f = T0Forecaster.from_pretrained(checkpoint)
        try:
            self.f = self.f.to(self.device)
        except Exception:                                          # noqa: BLE001
            pass
        self.supports["finetune"] = hasattr(self.f, "fit")

    def predict(self, contexts, horizon, *, panels=None, future=None) -> Pred:
        import torch
        cs = self.trim(contexts)
        x = torch.tensor(np.stack(cs), dtype=torch.float32, device=self.device)
        kw = {}
        if future is not None:
            kw["future_covariates"] = torch.tensor(np.stack(future), dtype=torch.float32,
                                                   device=self.device)
        out = self.f.predict(x, horizon=int(horizon), quantile_levels=self.levels, **kw)
        q = to_numpy(getattr(out, "quantiles", None))
        med = to_numpy(getattr(out, "median", getattr(out, "point", None)))
        if q.ndim == 2:
            q = q[:, :, None]
        q = q[:, :horizon, :]
        lv = self.levels[: q.shape[-1]]
        return Pred(point=(med[:, :horizon] if med is not None else q[:, :, q.shape[-1] // 2]),
                    quantiles=to_levels(q, lv), meta={"levels_emitted": len(lv)})

    def trainable(self):
        if not self.supports.get("finetune"):
            return None
        return getattr(self.f, "model", None)

    def training_step(self, contexts, truth, horizon):
        from ...errors import CapabilityError
        raise CapabilityError(self.key, "finetune",
                              "tfc-t0 ships inference only (no public training forward as of the "
                              "installed version); ask for the vendor recipe before claiming a "
                              "t0 fine-tune")
