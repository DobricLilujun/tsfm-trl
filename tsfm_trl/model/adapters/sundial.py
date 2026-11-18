"""THUML Sundial (Apache, ICML-2025 oral): a causal next-token model over
*time-series tokens*. Zero-shot inference goes through the model's own
``prepare_input_ids`` + token generation; the token vocabulary means fine-tuning
needs the vendor tokenizer ids, so without them the row is reported as
``finetune: n/a(reason)`` rather than trained with a made-up objective.
"""
from __future__ import annotations

import numpy as np

from ...errors import CapabilityError
from ..base import Pred, TSFMModel, quantiles_from_samples, to_numpy


class Sundial(TSFMModel):
    """Sundial base-128m (THUML, ICML-2025 oral): continuous-value patch tokens + a
    TimeFlow (flow-matching) head.

    What the *current* repository revision actually exposes, verified on the matrix
    machine:

    * **no tokenizer files in the Hub repo and none needed** — ``generate`` takes the
      raw values: ``model.generate(torch.randn(B, lookback), max_new_tokens=H,
      num_samples=k)`` → ``(B, k, H)`` de-normalised samples (the mixin applies revin
      itself). ``prepare_input_ids``/``mode=``/``tokenizer=`` belong to an *older*
      revision that the model card's prose still mentions; the adapter supports both,
      preferring whichever the loaded code offers.
    * the Auto* path needs ``transformers==4.40.1`` (the version in the model card's own
      Quickstart; 4.42.x mis-builds the causal mask for patched inputs), and
      ``device_map=`` must not be used with this remote code (accelerate re-dispatches
      through the Auto mapping, which does not know ``model_type: sundial``).
    * **no harness-runnable supervised step**: ``forward(labels=...)`` reaches the
      vendor's TimeFlow loss, whose packing (``output_token_lens``,
      ``diffusion_batch_mul``, ``mask_y``) is set by their training scripts, not by the
      checkpoint config — calling it with the checkpoint's config fails on shape
      (`addmm: (8x17664) @ (768x768)`). Fine-tuning therefore reports ``—`` with that
      reason instead of optimising an invented objective. Their GitHub training script
      is the supported route.
    """

    key, family = "sundial-base-128m", "sundial"
    caps = frozenset({"forecast", "paths"})
    loss_kind = None
    max_context = 2880                       # the model card's Quickstart lookback
    max_horizon = 720                        # one TimeFlow token block
    head_prefixes = ("flow_loss", "embed_layer", "norm")

    def __init__(self, checkpoint: str = "thuml/sundial-base-128m", n_paths: int = 8, **kw):
        super().__init__(**kw)
        from transformers import AutoModelForCausalLM
        self.checkpoint = checkpoint
        self.n_paths = int(n_paths)
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True)
        self.model = self.model.to(self.device)
        self.model.eval()

    def predict(self, contexts, horizon, *, panels=None, future=None) -> Pred:
        import torch
        horizon = int(horizon)
        x = torch.tensor(np.asarray(self.trim(contexts), dtype=np.float32),
                         device=self.device)
        kwargs = dict(max_new_tokens=max(horizon, 1), num_samples=max(1, self.n_paths))
        if hasattr(self.model, "prepare_input_ids"):        # older repo revision
            outs = []
            for c in self.trim(contexts):
                inputs, _ = self.model.prepare_input_ids(
                    X=np.asarray(c, dtype=np.float64)[:, None], normalize=True,
                    system="forecast", horizon=horizon)
                with torch.no_grad():
                    o = self.model.generate(inputs, mode="short_term_forecast",
                                            max_new_tokens=horizon, num_samples=self.n_paths)
                outs.append(np.asarray(o, dtype=float).reshape(self.n_paths, -1)[:, :horizon])
            S = np.stack(outs)
        else:
            with torch.no_grad():
                out = self.model.generate(x, **kwargs)      # (B, k, gen_len)
            S = to_numpy(out)[:, :, :horizon]
            if S.shape[-1] < horizon:
                # the head emits one block; extend it flat rather than pretending the
                # model predicted further ahead than it did
                S = np.concatenate([S, np.repeat(S[:, :, -1:], horizon - S.shape[-1],
                                                 axis=2)], axis=2)
        P = S.mean(axis=1)
        return Pred(point=P, quantiles=quantiles_from_samples(S), samples=S,
                    meta={"n_paths": S.shape[1], "how": "TimeFlow samples (revin-normalised)",
                          "api": "generate(values)"})

    def training_step(self, contexts, truth, horizon):
        raise CapabilityError(
            self.key, "finetune",
            "the TimeFlow supervised loss (forward(labels=...)) needs the vendor's "
            "training-script packing of output_token_lens/diffusion_batch_mul/mask_y; "
            "with the checkpoint's own config it fails on shape, so no objective is "
            "invented here — fine-tune via thuml/Sundial's scripts/ instead")

    def trainable(self):
        return self.model
