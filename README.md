# tsfm-trl

**TRL for Time-Series Foundation Models.** One API over every open time-series
foundation model (TSFM): zero-shot forecasting, fine-tuning (forecast *and*
classification), embedding probes, anomaly scoring, and reward post-training —
with a machine-checked compatibility matrix that says, per model and per task,
what actually works in *your* environment.

Nothing here is a wrapper around a paper's README. Every row of the matrix was
produced by running the code, and every `—` in it is a claim the code refuses to
fake. If a family's `forward()` only draws samples, the fine-tune column says
`— (needs the vendor's training stack)` instead of quietly optimising a
non-differentiable quantity.

```bash
pip install -e .                      # core env; other families get their own venv
tsfm-trl list --tier A                # 46 registered models, 11 environments
tsfm-trl forecast --model chronos-2 --series my.csv --horizon 21
```

```python
from tsfm_trl import ModelHub, ForecastTrainer, TrainingConfig
from tsfm_trl.data.fixtures import tiny_finance

m = ModelHub.load("moirai-2.0-R-small", device="cuda")
pred = m.predict([tiny_finance().values[:256]], horizon=16)
pred.point, pred.quantiles          # (1,16) and (1,16,9) on the canonical LEVELS grid

r = ForecastTrainer(m, TrainingConfig(budget="fs16", peft="lora")).fit(tiny_finance())
r.status, r.loss_first, r.loss_last # 'smoke', 3.027, 3.111
```

## What it gives you

| | |
|---|---|
| **Models** | Chronos (2 / Bolt / T5), TimesFM (2.0 / 2.5 / 3.0), Moirai (1.1 / 2 / MoE), MOMENT-1, TTM-r2/r3, Toto, FlowState/Granite, TiRex & TiRex-2, Time-MoE, Sundial, Kronos, Kairos, Timestral, Hirondel, t0-α/β/γ, Yug, Aurora, VisionTS++, plus statistical baselines (naive, seasonal naive, theta, ARIMA, moving average) as sanity checks |
| **Tasks** | zero-shot forecast (point + quantiles + sample paths), forecast fine-tuning (heads / LoRA / full), classification (native head, LoRA head, frozen-embedding probe), anomaly scoring, reward/GRPO post-training |
| **Honesty** | one canonical quantile grid (`LEVELS`), coverage measured only on bands the model actually emits, per-model `Pred.meta` recording *how* an interval was produced |
| **Proof** | `tsfm-trl doctor` → `COMPATIBILITY.md`, one subprocess per family environment, reason strings captured for every non-✅ |

## Quick tour

```bash
tsfm-trl info chronos-2                       # registry entry, caps, env, license
tsfm-trl forecast --model tirex --series px.csv --horizon 21 --md
tsfm-trl fit --model moirai-2.0-R-small --series px.csv --peft lora --budget fs16
tsfm-trl classify --model moment-1-large --task dir5 --levels probe,head,lora
tsfm-trl reward --model chronos-2 --task dir5 --steps 6      # GRPO / reward-descent / RFT
tsfm-trl evaluate --model timesfm-2.5-200m --series px.csv --horizons 21,63
tsfm-trl ckpt reports/ft_smoke/…              # inspect a checkpoint's provenance
tsfm-trl doctor --all-envs --md COMPATIBILITY.md
```

## Documentation

| doc | |
|---|---|
| [`docs/01_install.md`](docs/01_install.md) | the eleven environments, why one interpreter cannot hold them, third-party checkouts |
| [`docs/02_forecast.md`](docs/02_forecast.md) | forecasting, the quantile contract, evaluation and metrics |
| [`docs/03_fine_tune.md`](docs/03_fine_tune.md) | training levels, LoRA, checkpoints and provenance |
| [`docs/04_classify_probing.md`](docs/04_classify_probing.md) | the three classification levels, embedding probes, statistical probes |
| [`docs/05_reward_rl.md`](docs/05_reward_rl.md) | `RewardTrainer`: GRPO, reward-descent, rejection sampling |
| [`docs/06_matrix.md`](docs/06_matrix.md) | reproducing `COMPATIBILITY.md`, how to read every symbol |
| [`docs/07_finance_tasks.md`](docs/07_finance_tasks.md) | price panels, `dir5`/`extreme` labels, anchor-relative metrics |
| [`docs/08_known_issues.md`](docs/08_known_issues.md) | the version archaeology: which pin breaks which family, and why |

## Status

The machine-readable evidence lives in `reports/` (JSON, one row per model) and the
rendered table in [`COMPATIBILITY.md`](COMPATIBILITY.md). Tier A = must work;
Tier B = best effort; Tier C = documented-as-limited.

## Ground rules

* **No weights, not supported.** A model with no public checkpoint is out of scope
  (the registry keeps the row with `weights: null` and says so in the notes).
* **Small data.** Everything here is smoke-sized (≤ a few hundred windows) on
  purpose: this library proves *compatibility*, it is not a training benchmark.
* **Self-contained.** Adapters were ported from the TSFM4Finance benchmark, not
  imported from it.
* **Internal use.** Packaged as an installable distribution so publishing later is
  one command, but nothing is published now.

Apache-2.0 for this code; the model weights carry their own licenses (see the
registry and `docs/01_install.md`).
