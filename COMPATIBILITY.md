# Compatibility matrix

Generated 2026-11-18 18:48:35 on ubadmin-Precision-3591 (x86_64), python 3.11.15.

✅ ok · ❌ failed (see the JSON report for the captured reason) · — not offered by the model · ◐ partial · · not checked

Machines: gpu7/aarch64, ubadmin-Precision-3591/x86_64. One row per (model, environment); when two machines disagree the row that ran is kept and the other is recorded under *other machine* in the reasons.

| model | tier | weights | load | forecast | quantiles | embed | fine-tune | classify | anomaly | reward | s | machine |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| arima | A | ✅ | ✅ | ✅ | ✅ | ✅ | · | ✅ 2/2 | ✅ | — | 8.4 | ubadmin-Precision-3591/x86_64 |
| moving_average | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 1.2 | ubadmin-Precision-3591/x86_64 |
| naive | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 1.4 | ubadmin-Precision-3591/x86_64 |
| seasonal_naive | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 1.5 | ubadmin-Precision-3591/x86_64 |
| theta | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 2.2 | ubadmin-Precision-3591/x86_64 |
| chronos-2 | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 2/2 | ✅ | ✅ | 9.2 | ubadmin-Precision-3591/x86_64 |
| chronos-bolt-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.530→3.526) | ✅ 2/2 | ✅ | ✅ | 3.0 | ubadmin-Precision-3591/x86_64 |
| chronos-t5-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (1.724→1.809) | ✅ 2/2 | ✅ | ✅ | 20.2 | ubadmin-Precision-3591/x86_64 |
| flowstate-r1 | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (9.862→5.641) | ✅ 2/2 | ✅ | ✅ | 18.6 | ubadmin-Precision-3591/x86_64 |
| hirondel-7m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.061→0.104) | ✅ 2/2 | ✅ | ✅ | 13.5 | ubadmin-Precision-3591/x86_64 |
| kairos-10m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ 2/2 | ✅ | ❌ | 6.2 | ubadmin-Precision-3591/x86_64 |
| kronos-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.356→2.423) | ✅ 2/2 | ✅ | ✅ | 186.6 | ubadmin-Precision-3591/x86_64 |
| moirai-1.1-R-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 9.2 | ubadmin-Precision-3591/x86_64 |
| moirai-2.0-R-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.650→3.201) | ✅ 2/2 | ✅ | ✅ | 3.7 | ubadmin-Precision-3591/x86_64 |
| moment-1-large | A | ✅ | ✅ | ✅ | — | ✅ | ✅ (83.293→4.007) | ✅ 3/3 | ✅ | ✅ | 68.4 | ubadmin-Precision-3591/x86_64 |
| sundial-base-128m | A | ✅ | ✅ | ✅ | ✅ | ✅ | · | ✅ 2/2 | ✅ | — | 12.8 | gpu7/aarch64 |
| t0-gamma | A | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 7.1 | ubadmin-Precision-3591/x86_64 |
| timemoe-50m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.025→0.043) | ✅ 2/2 | ✅ | ✅ | 78.4 | gpu7/aarch64 |
| timesfm-2.0-500m | A | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 36.7 | ubadmin-Precision-3591/x86_64 |
| timesfm-2.5-200m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.347→0.450) | ✅ 2/2 | ✅ | ✅ | 10.2 | ubadmin-Precision-3591/x86_64 |
| timestral-28m | A | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 14.8 | ubadmin-Precision-3591/x86_64 |
| tirex | A | ✅ | ✅ | ✅ | ✅ | ✅ | · | ✅ 2/2 | ✅ | — | 41.1 | ubadmin-Precision-3591/x86_64 |
| toto-2-22m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.710→0.714) | ✅ 2/2 | ✅ | ✅ | 9.5 | ubadmin-Precision-3591/x86_64 |
| ttm-r2 | A | ✅ | ✅ | ✅ | — | ✅ | ✅ (260.703→310.215) | ✅ 2/2 | ✅ | ✅ | 2.1 | ubadmin-Precision-3591/x86_64 |
| ttm-r3 | A | ✅ | ✅ | ✅ | — | ✅ | ✅ (134.923→118.313) | ✅ 2/2 | ✅ | ✅ | 2.5 | ubadmin-Precision-3591/x86_64 |
| aurora | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 37.1 | ubadmin-Precision-3591/x86_64 |
| chronos-bolt-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (6.194→4.667) | ✅ 2/2 | ✅ | ✅ | 12.5 | ubadmin-Precision-3591/x86_64 |
| chronos-t5-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (1.702→1.733) | ✅ 2/2 | ✅ | ✅ | 29.3 | gpu7/aarch64 |
| kairos-50m | B | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ 2/2 | ✅ | ❌ | 5.7 | ubadmin-Precision-3591/x86_64 |
| kronos-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.575→2.595) | ✅ 2/2 | ✅ | ✅ | 621.3 | ubadmin-Precision-3591/x86_64 |
| kronos-mini | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (9.017→9.076) | ✅ 2/2 | ✅ | ✅ | 51.9 | ubadmin-Precision-3591/x86_64 |
| moirai-1.1-R-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 5.2 | ubadmin-Precision-3591/x86_64 |
| moirai-moe-1.0-R-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 17.3 | ubadmin-Precision-3591/x86_64 |
| moment-1-small | B | ✅ | ✅ | ✅ | — | ✅ | ✅ (223.330→96.402) | ✅ 3/3 | ✅ | ✅ | 8.0 | ubadmin-Precision-3591/x86_64 |
| t0-alpha | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 5.5 | ubadmin-Precision-3591/x86_64 |
| t0-beta | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 6.6 | ubadmin-Precision-3591/x86_64 |
| timesfm-3.0 | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 29.4 | ubadmin-Precision-3591/x86_64 |
| timestral-123m | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 19.8 | ubadmin-Precision-3591/x86_64 |
| timestral-5m | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 11.0 | ubadmin-Precision-3591/x86_64 |
| tirex-2 | B | ✅ | ✅ | ❌ | · | ❌ | · | ❌ 0/2 | — | — | 10.0 | gpu7/aarch64 |
| toto-open-1.0 | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.988→2.586) | ✅ 2/2 | ✅ | ✅ | 23.5 | ubadmin-Precision-3591/x86_64 |
| toto-2-313m | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (1.211→1.157) | ✅ 2/2 | ✅ | ✅ | 31.2 | ubadmin-Precision-3591/x86_64 |
| yug | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 9.3 | ubadmin-Precision-3591/x86_64 |
| patchtst-fm-r2 | C | ✅ | ✅ | ✅ | — | ✅ | ❌ | ✅ 2/2 | ✅ | ✅ | 13.1 | gpu7/aarch64 |
| timestral-209m | C | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 23.7 | ubadmin-Precision-3591/x86_64 |
| visiontspp-base | C | ❌ | ❌ | · | · | · | · | · | · | · | 1.3 | ubadmin-Precision-3591/x86_64 |

## Summary

| task | ok | declined by the model | failed | not checked |
|---|---|---|---|---|
| load | 45 | 0 | 1 | 0 |
| predict | 44 | 0 | 1 | 1 |
| quantiles | 35 | 9 | 0 | 2 |
| embed | 44 | 0 | 1 | 1 |
| finetune | 20 | 14 | 3 | 9 |
| classify | 44 | 0 | 1 | 1 |
| anomaly | 44 | 1 | 0 | 1 |
| reward | 21 | 22 | 2 | 1 |

'declined' means the model or its vendor package offers no path for that task in this environment (a `—` in the table): Moirai 1.1 `forward` draws samples instead of returning differentiable quantiles, TimesFM's public build ships inference only, Aurora's flow-matching head has no public training step. 'failed' means something was attempted and broke, with the reason captured below. A declined row is a statement about the model package; a failed row is a statement about this environment or our adapter.


## Captured failures

- **arima** (baseline, python 3.11.15): reward: arima: no 'finetune' support (adapter exposes no trainable module)
- **moving_average** (baseline, python 3.11.15): reward: moving_average: no 'finetune' support (adapter exposes no trainable module)
- **naive** (baseline, python 3.11.15): reward: naive: no 'finetune' support (adapter exposes no trainable module)
- **seasonal_naive** (baseline, python 3.11.15): reward: seasonal_naive: no 'finetune' support (adapter exposes no trainable module)
- **theta** (baseline, python 3.11.15): reward: theta: no 'finetune' support (adapter exposes no trainable module)
- **hirondel-7m** (hirondel, python 3.12.13): finetune: loss did not fall: 0.061029 -> 0.103562
- **kairos-10m** (kairos, python 3.12.13): finetune: RuntimeError: Boolean value of Tensor with more than one value is ambiguous; reward: RuntimeError: grad can be implicitly created only for scalar outputs
- **kronos-small** (kronos, python 3.11.15): other machine: ubadmin-Precision-3591/x86_64: load=fail
- **moirai-1.1-R-small** (moirai, python 3.11.15): finetune: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moment-1-large** (moment, python 3.11.15): other machine: ubadmin-Precision-3591/x86_64: reward=fail
- **sundial-base-128m** (sundial, python 3.11.14): reward: sundial-base-128m: no 'finetune' support (adapter exposes no trainable module); other machine: gpu7/aarch64: load=fail
- **t0-gamma** (t0, python 3.12.13): finetune: t0-gamma: no 'finetune' support (adapter exposes no trainable module); reward: t0-gamma: no 'finetune' support (adapter exposes no trainable module)
- **timemoe-50m** (timemoe, python 3.11.14): finetune: loss did not fall: 0.024578 -> 0.042918
- **timesfm-2.0-500m** (timesfm20, python 3.11.15): finetune: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module); reward: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module)
- **timestral-28m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **tirex** (tirex, python 3.11.15): reward: tirex: no 'finetune' support (adapter exposes no trainable module)
- **aurora** (aurora, python 3.12.13): finetune: aurora: no 'finetune' support (adapter exposes no trainable module); reward: aurora: no 'finetune' support (adapter exposes no trainable module)
- **chronos-t5-base** (chronos_t5, python 3.11.14): other machine: ubadmin-Precision-3591/x86_64: predict=fail, reward=fail
- **kairos-50m** (kairos, python 3.12.13): finetune: RuntimeError: Boolean value of Tensor with more than one value is ambiguous; reward: RuntimeError: grad can be implicitly created only for scalar outputs
- **kronos-base** (kronos, python 3.11.15): other machine: ubadmin-Precision-3591/x86_64: load=fail
- **kronos-mini** (kronos, python 3.11.15): other machine: ubadmin-Precision-3591/x86_64: load=fail
- **moirai-1.1-R-base** (moirai, python 3.11.15): finetune: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moirai-moe-1.0-R-base** (moirai_moe, python 3.11.15): finetune: moirai-moe: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-moe: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **t0-alpha** (t0, python 3.12.13): finetune: t0-gamma: no 'finetune' support (adapter exposes no trainable module); reward: t0-gamma: no 'finetune' support (adapter exposes no trainable module)
- **t0-beta** (t0, python 3.12.13): finetune: t0-gamma: no 'finetune' support (adapter exposes no trainable module); reward: t0-gamma: no 'finetune' support (adapter exposes no trainable module)
- **timesfm-3.0** (timesfm30, python 3.11.15): finetune: timesfm-3.0: no 'finetune' support (the public timesfm package ships TimesFM 3.0 inference only (no documented training forward); contributing a head-only loop is tracked in docs/03_fine_tune.md); reward: timesfm-3.0: no 'finetune' support (adapter exposes no trainable module); device: cpu (retried after a GPU out-of-memory on auto: UnavailableError: timesfm-3.0: OutOfMemoryError: CUDA out of memory. Tried to allocate 20.)
- **timestral-123m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **timestral-5m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **tirex-2** (tirex2, python 3.12.14): predict: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial states
        matC_k_val = tl.load(matCinitial_ptr, boundary_check=(0, 1)).to(tl.float32)
        vecN; classify:probe: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial sta; classify:head: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial sta; anomaly: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial sta; reward: tirex-2: no 'finetune' support (adapter exposes no trainable module); other machine: ubadmin-Precision-3591/x86_64: load=fail; embed: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial sta
- **toto-open-1.0** (toto1, python 3.12.13): other machine: gpu7/aarch64: load=fail
- **yug** (yug, python 3.12.13): finetune: yug: no 'finetune' support (adapter exposes no trainable module); reward: yug: no 'finetune' support (adapter exposes no trainable module)
- **patchtst-fm-r2** (patchtst, python 3.11.14): finetune: TypeError: PatchTSTFMForPrediction.forward() got an unexpected keyword argument 'future_values'; other machine: ubadmin-Precision-3591/x86_64: finetune=fail, reward=fail
- **timestral-209m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **visiontspp-base** (visionts, python 3.11.15): load: UnavailableError: visiontspp-base: UnavailableError: visiontspp-base: VisionTS++ needs the upstream package (the Hub repo ships .ckpt weights only): No module named 'visiontspp'  [install: git clone the VisionTS/VisionTS++ upstream, then weights=/path/to/visiontspp_base.ckpt. clone it and point the ; other machine: gpu7/aarch64: load=fail
