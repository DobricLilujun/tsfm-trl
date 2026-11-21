# 09 · Running this as a benchmark

The compatibility matrix answers **"does this architecture work here at all"**. A
benchmark answers a different question: **"how well does it forecast, and how do the
architectures compare"**. Both run through the same API, and conflating them is the most
common way to over-claim from this repo, so the two are kept formally separate here.

## The two claims, in one table

| | question | command | what a ✅ / a number means |
|---|---|---|---|
| **compatibility** | can the architecture be loaded, forecast, be scored, and be reached by a training/RL path in *this* environment | `tsfm-trl doctor` → `COMPATIBILITY.md` | the code ran end-to-end at smoke size; nothing about accuracy |
| **effectiveness** | how accurate is it, and how does it compare across families, horizons, domains | `tsfm-trl evaluate` (`forecast_eval`) | numbers on held-out windows with a defined metric, split and seed |

`COMPATIBILITY.md` deliberately contains **no accuracy numbers**. Its fine-tune column
carries a two-step loss for one reason only: to prove the objective is differentiable and
the logging works. Reading it as "fine-tuning helped" is a category error
(`docs/03_fine_tune.md`).

## Metrics that exist (all hand-written, all NaN-safe)

`tsfm_trl/eval/metrics.py`, on the canonical `LEVELS` grid unless stated otherwise:

| family | function | note |
|---|---|---|
| point | `rmse`, `mae`, `mape`, `smape`, `nd` | scale-free ones (`nd`, `smape`) for cross-series comparison |
| scale-free skill | `mase`, `relative_skill` | both need the training span and a `season` (1 for the finance panels) |
| direction | `directional_accuracy` | anchor-relative: the last observed value by default, which is the version that matters for the finance labels (`docs/07_finance_tasks.md`) |
| ranking | `rank_corr` | per-window Spearman, useful for signal-style tasks |
| probabilistic | `pinball`, `crps_from_quantiles`, `wql`, `quantile_coverage` | quantile-based; **coverage only counts bands the model actually emits** — a model that ships 9 levels is not scored on 21 |
| classification | `classification_report` | PR-AUC (multiclass OVR), ROC-AUC, macro-F1, F2-beta, precision/recall, base rate; hard labels give `nan` for PR/ROC rather than a fabricated score |

`forecast_report(y, pred, train)` bundles the point + probabilistic set into one dict;
`forecast_eval(...)` produces one row per (span, horizon).

## Protocol

The library fixes the parts of a protocol that would otherwise differ per family:

* **one quantile grid** (`LEVELS`, 21 levels) — adapters that emit fewer levels are
  mapped onto their own subset and `Pred.meta["levels_emitted"]` records it;
* **one normalisation of the question** — anchor-relative targets for the finance labels,
  and the model's own scaler is never re-implemented outside the adapter;
* **context handling** — `ctx_step`/`max_context` per adapter, left-padding with the
  model's own pad mask instead of zeros (Moirai, FlowState) — a silent zero-pad changes
  the score for patch models;
* **split discipline** — `SeriesDataset.splits`, and any checkpoint carries
  `split_end` so `load_finetuned` can refuse an evaluation window that overlaps training.

Budget names in `TrainingConfig` are also evaluation sizes:

```python
BUDGETS = {"fs16": 16 windows / 40 steps / lr 1e-5,
           "fs64": 64 windows / 120 steps / lr 1e-5,
           "full": all windows / 3 epochs / lr 5e-6}
```

## Running an effectiveness pass

One model, several horizons, JSON rows out (stdout is a data channel — progress lines go
to stderr):

```bash
tsfm-trl evaluate --model chronos-2 --series px.csv --horizons 21,63,126 --ctx 512
tsfm-trl evaluate --model chronos-2 --adaptation reports/ft/chronos-2__…/model.pt \
                  --series px.csv --horizons 21,63
```

The second form is the zero-shot-vs-adapted comparison: the checkpoint's provenance
(base id, peft level, trained parameter names, `split_end`) is validated on load, so the
comparison cannot silently swap a TimesFM head onto a Moirai trunk or evaluate on
windows the run trained on.

Through the API, which is what a sweep should use:

```python
from tsfm_trl import ModelHub
from tsfm_trl.eval.evaluate import forecast_eval

m = ModelHub.load("moirai-1.1-R-small", device="cuda", ctx_cap=512, batch=16)
rows = forecast_eval(m, "panels/px.csv", horizons=(21, 63, 126),
                     spans=("test",), ctx=512, max_windows=64, seed=0, season=1)
```

Across environments, use the same subprocess dispatch the matrix uses — one interpreter
per family (`envs/local.json`), because the family pins are mutually contradictory
(`docs/01_install.md`):

```bash
tsfm-trl doctor --all-envs --tasks load,predict,quantiles \
                --json reports/matrix_bench_core.json
```

`predict` is the benchmark's inference half: every row that is ✅ there can be dropped
into `forecast_eval` without further adaptation work.

## Reporting rules (what goes in a table, what does not)

1. **Report the metric family the model can serve.** A point-only head (TTM r2/r3) has no
   CRPS; write `—`, do not integrate a degenerate distribution. Same reason TiRex's
   NPP and Chronos-Bolt's samples both get empirical quantiles first: different routes to
   the same grid, then the same metric.
2. **Report coverage per emitted band** and say which bands (`Pred.meta`).
3. **One row per (model, environment)**; a model that is ✅ on one machine and OOM on
   another is a fact about the machine, and the matrix keeps both under *other machine*.
4. **State the parameter budget for adapted rows** — `peft="lora"` now means a frozen
   trunk, and `TrainResult.trainable_parameters` is the number to print
   (`docs/08_known_issues.md` explains why that sentence exists).
5. **Multiple seeds and windows.** A single 16-window pass is a smoke test; the harness
   defaults are deliberately smoke-sized (`fs16`/`fs64`) so an accidental 10-hour run is
   impossible by default.
6. **Baselines in the same table.** `naive`, `seasonal_naive`, `theta`, `arima`,
   `moving_average` are registered models with their own rows, so every effectiveness
   table can carry skill relative to them (`relative_skill`, MASE) rather than raw loss.

## What is *not* done yet (so nobody reads it in)

* No repo-wide effectiveness sweep has been run: the checked-in evidence is the
  compatibility matrix, not a CRPS/MASE table for 46 models. The machinery
  (`forecast_eval`, `evaluate`, per-env dispatch) is there; the hours are not spent.
* No multi-seed confidence intervals, no Diebolt–Mariano / MZ statistics, no horizon-grid
  plots.
* The finance label set (`dir5`, `extreme`) and a tiny public UEA/UCR subset are wired for
  classification; external-validity classification numbers across all 46 models are not
  in the repo either.
* Fine-tune effectiveness (does adaptation improve out-of-sample skill, per family, at a
  stated parameter budget) is a separate experiment that the checkpoint provenance format
  is designed to make auditable, and has not been run at benchmark scale.

If a paper table is the goal, the honest structure is: **compatibility matrix** (this
repo, complete), **effectiveness table** (to run: `evaluate` across families × horizons ×
budgets, with baselines), **adaptation table** (zero-shot vs LoRA at a stated budget, for
the 29 families where the training path exists).
