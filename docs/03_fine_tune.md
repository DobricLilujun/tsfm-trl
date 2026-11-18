# 3 · Fine-tuning

```python
from tsfm_trl import ForecastTrainer, ModelHub, TrainingConfig
from tsfm_trl.data.fixtures import tiny_finance

m   = ModelHub.load("moirai-2.0-R-small", device="cuda")
cfg = TrainingConfig(budget="fs16", peft="lora", ctx=256, horizon=16, seed=0)
res = ForecastTrainer(m, cfg).fit(tiny_finance())

res.status, res.steps, res.loss_first, res.loss_last   # 'smoke', 8, 3.027, 3.111
res.checkpoint                                          # written path
```

CLI equivalent:

```bash
tsfm-trl fit --model moirai-2.0-R-small --series px.csv --peft lora --budget fs16 \
             --ctx 256 --horizon 16 --ckpt reports/ft/px
```

## Data

`fit` accepts any of:

* a `SeriesDataset` (or a CSV/Parquet path, or a DataFrame) — windows are built for you
  with a train/val/test split,
* `{"windows": [(ctx, y), ...], "info": {...}}` — pre-cut windows, what the matrix uses,
* `{"dataset": ds}` — explicit.

Windows come from `data.series.windows(values, horizon, ctx, stride=…)`; the split
index is stored in the checkpoint so an evaluation can never accidentally train on the
test span.

## How much to train: budgets, not step counts

`TrainingConfig(budget=...)` picks a size, and the trainer keeps the *shape* of the run
stable across families:

| budget | windows | steps | lr |
|---|---|---|---|
| `fs16` (default for the matrix) | 16 | 40 (≤ that) | 1e-5 |
| `fs64` | 64 | 120 | 1e-5 |
| `full` | all | 3 epochs | 5e-6 |

`smoke=True` caps steps to 3 — that is what `doctor` uses, because the matrix checks
that a fine-tune **runs**, not that it converges. Losses are still reported
(`✅ (0.587→0.612)`), so a diverging run is visible rather than hidden.

## Three levels of invasiveness

```python
TrainingConfig(peft="heads_only")   # only the forecast head(s) train
TrainingConfig(peft="lora", lora_r=8, lora_targets=["q", "v"])
TrainingConfig(peft="full")         # everything (fine on ≤300 M at smoke size)
```

* `heads_only` uses the adapter's `head_prefixes` (e.g. `("decoder", "projection",
  "head", "p21")` for Kairos) — the names come from the vendor modules, and the list
  that actually became trainable is stored in the checkpoint.
* `lora` goes through `training.peft.apply_lora`; `merge_lora` is available for export.
* `full` is refused for families where the backbone cannot take a gradient (see below).

Loss follows the model: `loss_kind = "quantile"` families are trained with pinball on
their own head, `"token"` families (Chronos-T5, Time-MoE, Sundial, Kronos) with
cross-entropy on their discrete tokens, and vendor-loop families (Kronos) delegate to
the vendor's own trainer via `vendor_fit`.

## What "not fine-tunable" means, honestly

Some families cannot be fine-tuned through an HF-style `forward` at all. They report
`— (skipped)` with the reason, and it is a statement about the model:

* **Moirai 1.1 / Moirai-MoE** — `forward()` *draws samples*; `_get_distr` covers the
  whole padded window. A real fine-tune needs uni2ts' Lightning stack
  (`MoiraiForecast` + packed masked dataset). Optimising "quantiles of a sample" would
  be a no-op dressed as a fine-tune.
* **TimesFM 2.0/2.5/3.0, TiRex, FlowState inference builds** — no public training code;
  `trainable()` returns `None`, so the fine-tune column is `—`.
* **Kronos** — the vendor loop only *prepares* the CSV unless
  `extra={"run_training": True}`; the matrix records `prepared`, not `ok`.
* **MOMENT** — trainable, but its gradient checkpointing is non-deterministic, so the
  adapter disables it (otherwise torch aborts with *"different number of tensors was
  saved"*).

## Memory ladder

`ForecastTrainer.fit` (and `RewardTrainer.fit`) retry on OOM with progressively
cheaper profiles, and record which one was used:

```
(bs, amp, peft) = (given) → (1, bf16, given) → (1, bf16, heads_only)
                          → (1, bf16, lora)  → (1, fp32, heads_only)
```

CUDA *toolchain* failures (nvrtc, arch mismatch) are treated the same way — a CPU retry
is an environment fallback, not a silent downgrade; the checkpoint meta says
`fallbacks: [...]`.

## Checkpoints and provenance

```python
from tsfm_trl import load_finetuned
from tsfm_trl.training.checkpoints import describe

describe("reports/ft/moirai-2.0-R-small__tiny_fin.pt")
m2 = ModelHub.load("moirai-2.0-R-small")
load_finetuned(m2, "reports/ft/moirai-2.0-R-small__tiny_fin.pt")
```

A checkpoint is a state dict plus the provenance needed to refuse a wrong pairing:
base registry id, `trainable` parameter list, config, split index, loss curve, budget,
smoke flag, and any fallbacks. `load_finetuned` raises if the target model's base id
differs — a Chronos head loaded onto a Moirai is a silent nonsense machine otherwise.
`tsfm-trl ckpt <path>` prints the same record.
