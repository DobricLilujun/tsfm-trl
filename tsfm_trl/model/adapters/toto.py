"""Datadog Toto: Toto-Open-1.0 and Toto-2.0 (Apache).

Toto scales with a **causal** scaler, so the fine-tune target for the future block
is ``asinh((y-loc)/scale)`` from context statistics only — the same transform the
decoder inverts at inference. Anything else would optimise a different objective
than the one the model is scored on, so the training step works in the model's own
scaled space and the pinball grid is the model's own.

``toto-2`` needs python ≥ 3.12 → its own environment (``envs/toto``).
"""
from __future__ import annotations

import math

import numpy as np

from ..base import Pred, TSFMModel, levels_from_count, to_levels


class Toto2(TSFMModel):
    key, family = "toto-2-22m", "toto2"
    caps = frozenset({"forecast", "quantiles", "multivariate", "finetune"})
    loss_kind = "quantile"
    max_context = 4096
    ctx_step = 32
    head_prefixes = ("output_head", "head", "quantile")

    def __init__(self, checkpoint: str = "Datadog/Toto-2.0-22m", **kw):
        super().__init__(**kw)
        from toto2.model import Toto2Model
        self.checkpoint = checkpoint
        self.model = Toto2Model.from_pretrained(checkpoint).to(self.device)
        self.model.eval()
        cfg = self.model.config
        self.patch = int(cfg.patch_size)
        self.ctx_step = self.patch
        self.n_out_patches = int(getattr(cfg, "num_output_patches", 16))
        self.max_horizon = self.patch * self.n_out_patches
        self.levels = [float(x) for x in (getattr(cfg, "quantiles", None)
                                          or getattr(cfg, "quantile_levels", None)
                                          or np.linspace(0.1, 0.9, 9))]

    def _batch(self, contexts, extra_future=None):
        import torch
        cs = self.trim(contexts)
        ctx = torch.tensor(np.stack(cs)[:, None, :], dtype=torch.float32, device=self.device)
        ids = torch.zeros(len(cs), 1, dtype=torch.long, device=self.device)
        b = {"target": ctx, "target_mask": torch.ones_like(ctx, dtype=torch.bool),
             "series_ids": ids}
        return b

    def predict(self, contexts, horizon, *, panels=None, future=None) -> Pred:
        import torch
        b = self._batch(contexts)
        with torch.no_grad():
            q = self.model.forecast(b, horizon=int(horizon), decode_block_size=0,
                                    has_missing_values=False)
        q = np.asarray(q.detach().float().cpu())            # (nq,N,n_var,H) or (nq,N,H)
        nq = q.shape[0]
        if q.ndim == 4:
            q = np.transpose(q, (1, 3, 0, 2))[:, :horizon, :, 0] if q.shape[2] == 1 else \
                np.transpose(q.reshape(nq, q.shape[1], -1, q.shape[-1]), (1, 3, 0, 2))[:, :horizon, :, 0]
        else:
            q = np.transpose(q, (1, 2, 0))
        q = q[:, :horizon, :]
        lv = self.levels if len(self.levels) == nq else levels_from_count(nq)
        med = int(np.argmin(np.abs(np.asarray(lv) - 0.5)))
        return Pred(point=q[:, :, med], quantiles=to_levels(q, lv))

    def training_step(self, contexts, truth, horizon):
        """Pinball in the model's asinh-scaled space (see module docstring)."""
        import torch
        from ...training.losses import pinball_loss
        y = np.asarray(truth, dtype=np.float32)
        H = y.shape[1]
        pad = int(math.ceil(H / self.patch) * self.patch)
        rows, tm_rows, y_rows = [], [], []
        for c, yy in zip(np.asarray(contexts, dtype=np.float32), y):
            rows.append(np.concatenate([c, np.zeros(pad)]))
            tm_rows.append(np.r_[np.ones(len(c), dtype=bool), np.zeros(pad, dtype=bool)])
            y_rows.append(np.r_[c, yy, np.zeros(pad - H)])
        t = torch.tensor(np.stack(rows)[:, None, :], dtype=torch.float32, device=self.device)
        tm = torch.tensor(np.stack(tm_rows)[:, None, :], device=self.device)
        yfull = torch.tensor(np.stack(y_rows)[:, None, :], dtype=torch.float32, device=self.device)
        ids = torch.zeros(t.shape[0], 1, dtype=torch.long, device=self.device)
        out = self.model(target=t, target_mask=tm, cpm_mask=torch.ones_like(tm),
                         series_ids=ids, num_return_steps=None)
        q = out.quantiles.float()                              # (nq,B,1,P,patch)
        nq = q.shape[0]
        q = q.reshape(nq, t.shape[0], -1).permute(1, 2, 0)     # (B,P*patch,nq)
        with torch.no_grad():
            _scaled, loc, scale = self.model.scaler(t, tm & torch.ones_like(tm))
            loc = loc[:, 0, :] if loc.ndim == 3 else loc
            scale = scale[:, 0, :] if scale.ndim == 3 else scale
        T = q.shape[1]
        loc = loc[:, -T:]
        scale = scale[:, -T:].clamp_min(1e-6)
        tgt = torch.asinh((yfull[:, 0, -T:] - loc) / scale)
        loss = pinball_loss(q[:, -T:, :], tgt[:, -T:], self.levels[:nq])
        return loss

    def trainable(self):
        return self.model


class Toto1(TSFMModel):
    """Toto-Open-Base-1.0. Best effort through ``transformers``; if the installed
    transformers has no Toto time-series class, the doctor records it as
    ``unavailable(reason)`` instead of pretending the row exists."""

    key, family = "toto-open-1.0", "toto1"
    caps = frozenset({"forecast", "quantiles", "multivariate"})
    loss_kind = None
    max_context = 4096
    ctx_step = 32

    def __init__(self, checkpoint: str = "Datadog/Toto-Open-Base-1.0", **kw):
        super().__init__(**kw)
        from transformers import AutoModelForCausalLM
        self.checkpoint = checkpoint
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True,
                                                          device_map=self.device)
        self.model.eval()

    def predict(self, contexts, horizon, *, panels=None, future=None) -> Pred:
        import torch
        cs = self.trim(contexts)
        try:
            x = torch.tensor(np.stack(cs)[:, None, :], dtype=torch.float32, device=self.device)
            with torch.no_grad():
                out = self.model.forecast(x, prediction_length=int(horizon)) \
                    if hasattr(self.model, "forecast") else self.model(x).prediction_outputs
        except Exception as e:                                     # noqa: BLE001
            from ...errors import UnavailableError
            raise UnavailableError(self.key, f"Toto-1.0 inference path unavailable: {e}") from e
        arr = np.asarray(out.detach().float().cpu() if hasattr(out, "detach") else out, float)
        return Pred(point=arr.reshape(arr.shape[0], -1)[:, :horizon])
