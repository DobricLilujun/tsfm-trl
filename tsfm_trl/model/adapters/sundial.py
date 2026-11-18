"""THUML Sundial (Apache, ICML-2025 oral): a causal next-token model over
*time-series tokens*. Zero-shot inference goes through the model's own
``prepare_input_ids`` + token generation; the token vocabulary means fine-tuning
needs the vendor tokenizer ids, so without them the row is reported as
``finetune: n/a(reason)`` rather than trained with a made-up objective.
"""
from __future__ import annotations

import numpy as np

from ...errors import CapabilityError
from ..base import Pred, TSFMModel, quantiles_from_samples


class Sundial(TSFMModel):
    key, family = "sundial-base-128m", "sundial"
    caps = frozenset({"forecast", "paths", "finetune"})
    loss_kind = "token"
    max_context = 512
    max_horizon = 192

    def __init__(self, checkpoint: str = "thuml/sundial-base-128m", n_paths: int = 8, **kw):
        super().__init__(**kw)
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.checkpoint = checkpoint
        self.n_paths = int(n_paths)
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True,
                                                          device_map=self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True)
        self.model.eval()

    def predict(self, contexts, horizon, *, panels=None, future=None) -> Pred:
        import torch
        horizon = int(horizon)
        pts, paths = [], []
        for c in self.trim(contexts):
            hist = np.asarray(c, dtype=np.float64)[:, None]
            try:
                inputs, _prompt = self.model.prepare_input_ids(
                    X=hist, max_context_length=self.max_context, patch_size=32,
                    normalize=True, system="forecast", horizon=horizon)
            except TypeError:                                    # older/newer signature
                inputs, _prompt = self.model.prepare_input_ids(X=hist, normalize=True,
                                                               system="forecast")
            outs = []
            for k in range(self.n_paths):
                with torch.no_grad():
                    o = self.model.generate(inputs, mode="short_term_forecast",
                                            tokenizer=self.tokenizer, max_new_tokens=horizon,
                                            temperature=(0.0 if k == 0 else 0.2),
                                            top_p=0.95, top_k=6, horizon=horizon,
                                            do_sample=(k > 0))
                arr = np.asarray(o, dtype=float).reshape(-1)[:horizon]
                outs.append(arr)
            pts.append(outs[0])
            paths.append(np.stack(outs))
        P = np.stack(pts)[:, :horizon]
        S = np.stack(paths)[:, :, :horizon]
        return Pred(point=P, quantiles=quantiles_from_samples(S), samples=S,
                    meta={"n_paths": self.n_paths, "tokenized": True,
                          "normalisation": "model-side (prepare_input_ids normalize=True)"})

    def training_step(self, contexts, truth, horizon):
        raise CapabilityError(
            self.key, "finetune",
            "Sundial's head is a discrete token vocabulary: a fine-tune must build token ids "
            "with the vendor tokenizer (thuml/Sundial finetune pipeline). Wire that in this "
            "adapter before claiming a Sundial fine-tune.")

    def trainable(self):
        return self.model
