# Compatibility matrix

Generated 2026-11-17 23:58:45 on ubadmin-Precision-3591 (x86_64), python 3.11.15.

✅ ok · ❌ failed (see `reports/compat_matrix.json` for the captured reason) · — not offered by the model · ◐ partial · · not checked

| model | tier | weights | load | forecast | quantiles | embed | fine-tune | classify | anomaly | reward | s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| timesfm-2.0-500m | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ | ✅ | — | 428.5 |
| arima | A | ✅ | ✅ | ✅ | ✅ | · | · | ✅ | ✅ | — | 12.4 |
| moving_average | A | ✅ | ✅ | ✅ | — | · | · | ✅ | ✅ | — | 0.0 |
| naive | A | ✅ | ✅ | ✅ | — | · | · | ✅ | ✅ | — | 0.0 |
| seasonal_naive | A | ✅ | ✅ | ✅ | — | · | · | ✅ | ✅ | — | 0.0 |
| theta | A | ✅ | ✅ | ✅ | — | · | · | ✅ | ✅ | — | 1.4 |
| chronos-2 | A | ✅ | ✅ | ✅ | ✅ | · | ✅ | ✅ | ✅ | ✅ | 12.4 |
| chronos-bolt-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (3.530→3.526) | ✅ | ✅ | ✅ | 4.2 |
| chronos-t5-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (1.724→1.809) | ✅ | ✅ | ✅ | 39.6 |
| flowstate-r1 | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (9.862→5.678) | ✅ | ✅ | ✅ | 242.6 |
| timesfm-2.5-200m | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (0.347→0.450) | ✅ | ✅ | ✅ | 23.5 |
| ttm-r2 | A | ✅ | ✅ | ✅ | — | · | ✅ (243.899→312.505) | ✅ | ✅ | ✅ | 1.3 |
| ttm-r3 | A | ✅ | ✅ | ✅ | — | · | ✅ (135.088→117.542) | ✅ | ✅ | ✅ | 2.4 |
| chronos-bolt-base | B | ✅ | ✅ | ✅ | ✅ | · | ✅ (6.979→4.617) | ✅ | ✅ | ❌ | 27.6 |
| chronos-t5-base | B | ✅ | ❌ | · | · | · | · | · | · | · | 0.0766444206237793 |
| timesfm-3.0 | B | ✅ | ❌ | · | · | · | · | · | · | · | 1.595839500427246 |
| moirai-1.1-R-small | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ | ✅ | — | 9.3 |
| moirai-2.0-R-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (2.650→3.201) | ✅ | ✅ | ✅ | 2.9 |
| moirai-1.1-R-base | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ | ✅ | — | 7.3 |
| moirai-moe-1.0-R-base | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ | ✅ | — | 27.9 |
| moment-1-large | A | ✅ | ✅ | ✅ | — | · | ✅ (84.047→5.093) | ✅ | ✅ | ✅ | 80.2 |
| moment-1-small | B | ✅ | ✅ | ✅ | — | · | ✅ (221.181→98.460) | ✅ | ✅ | ✅ | 4.3 |
| toto-2-22m | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (0.710→0.714) | ✅ | ✅ | ✅ | 11.5 |
| toto-open-1.0 | B | ✅ | ❌ | · | · | · | · | · | · | · | 0.016299724578857422 |
| toto-2-313m | B | ✅ | ✅ | ✅ | ✅ | · | ❌ | ✅ | ✅ | ✅ | 20.4 |
| tirex | A | ✅ | ✅ | ✅ | ✅ | · | · | ✅ | ✅ | — | 62.4 |
| tirex-2 | B | ✅ | ❌ | · | · | · | · | · | · | · | 1.375934362411499 |
| timemoe-50m | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (0.025→0.043) | ✅ | ✅ | ✅ | 370.5 |
| kronos-small | A | ✅ | ✅ | ❌ | — | · | ❌ | — | — | — | 20.7 |
| kronos-base | B | ❌ | ✅ | ❌ | — | · | ❌ | — | — | — | 59.2 |
| kronos-mini | B | ❌ | ✅ | ❌ | — | · | ❌ | — | — | — | 4.9 |
| kairos-10m | A | ✅ | ❌ | · | · | · | · | · | · | · | 2.3649699687957764 |
| aurora | B | ✅ | ❌ | · | · | · | · | · | · | · | 3.5619890689849854 |
| kairos-50m | B | ✅ | ❌ | · | · | · | · | · | · | · | 0.13340187072753906 |

## Captured failures

- **timesfm-2.0-500m** (timesfm20, python 3.11.15): finetune: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module); reward: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module)
- **arima** (baseline, python 3.11.15): reward: arima: no 'finetune' support (adapter exposes no trainable module)
- **moving_average** (baseline, python 3.11.15): reward: moving_average: no 'finetune' support (adapter exposes no trainable module)
- **naive** (baseline, python 3.11.15): reward: naive: no 'finetune' support (adapter exposes no trainable module)
- **seasonal_naive** (baseline, python 3.11.15): reward: seasonal_naive: no 'finetune' support (adapter exposes no trainable module)
- **theta** (baseline, python 3.11.15): reward: theta: no 'finetune' support (adapter exposes no trainable module)
- **chronos-bolt-base** (chronos_bolt, python 3.11.15): reward: reward training failed even on the last profile (CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 5.64 GiB of which 22.44 MiB is free. Process 915373 has 163.04 MiB memory in use. Including non-PyTorch memory, this process has 5.42 GiB memory in use. Of the allocated memory 4.81 GiB is allocated by PyTorch, and 480.13 MiB is reserved by PyTorch but unallocated. If res
- **chronos-t5-base** (chronos_t5, python 3.11.15): load: UnavailableError: chronos-t5-base: OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 5.64 GiB of which 22.44 MiB is free. Process 915373 has 163.04 MiB memory in use. Including non-PyTorch memory, this process has 5.42 GiB memory in use. Of the allocate
- **timesfm-3.0** (timesfm30, python 3.11.15): load: UnavailableError: timesfm-3.0: OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 5.64 GiB of which 22.44 MiB is free. Process 915373 has 163.04 MiB memory in use. Including non-PyTorch memory, this process has 5.42 GiB memory in use. Of the allocated me
- **moirai-1.1-R-small** (moirai, python 3.11.15): finetune: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moirai-1.1-R-base** (moirai, python 3.11.15): finetune: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moirai-moe-1.0-R-base** (moirai_moe, python 3.11.15): finetune: moirai-moe: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-moe: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **toto-open-1.0** (toto1, python 3.12.13): load: UnavailableError: toto-open-1.0: missing package: No module named 'transformers'
- **toto-2-313m** (toto2, python 3.12.13): finetune: RuntimeError: non-finite loss at step 1: nan
- **tirex** (tirex, python 3.11.15): reward: tirex: no 'finetune' support (adapter exposes no trainable module)
- **tirex-2** (tirex2, python 3.12.13): load: UnavailableError: tirex-2: UnavailableError: tirex-2: needs either the Triton kernels (GPU sm8.9 below sm10.0) or a CUDA toolchain for the native fallback (nvcc not found)  [install: run it on a Blackwell-class GPU (sm >= 10.0) with CUDA 13 + Triton >= 3.4, or install the full CUDA toolkit (nvcc) fo
- **timemoe-50m** (timemoe, python 3.11.15): finetune: loss did not fall: 0.024578 -> 0.042918
- **kronos-small** (kronos, python 3.11.15): finetune: vendor fine-tune prepared but not run (pass extra={'run_training': True}); CSV at reports/ft_smoke/kronos-small__kronos/train.csv; classify: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...])); anomaly: CapabilityError: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...])); reward: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...]))
- **kronos-base** (kronos, python 3.11.15): finetune: vendor fine-tune prepared but not run (pass extra={'run_training': True}); CSV at reports/ft_smoke/kronos-small__kronos/train.csv; classify: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...])); anomaly: CapabilityError: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...])); reward: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...]))
- **kronos-mini** (kronos, python 3.11.15): finetune: vendor fine-tune prepared but not run (pass extra={'run_training': True}); CSV at reports/ft_smoke/kronos-small__kronos/train.csv; classify: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...])); anomaly: CapabilityError: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...])); reward: kronos-small: no 'panel_in' support (Kronos needs OHLCV panels (pass panels=[DataFrame, ...]))
- **kairos-10m** (kairos, python 3.11.15): load: UnavailableError: kairos-10m: UnavailableError: kairos: transformers does not know model_type 'kairos' and the authors' package is not importable (The checkpoint you are trying to load has model type `kairos` but Transformers does not recognize this architecture. This could be because of an issue wi
- **aurora** (aurora, python 3.11.15): load: UnavailableError: aurora: ValueError: Unrecognized configuration class <class 'transformers_modules.DecisionIntelligence.Aurora.c495b02c1b151be52a3c174237ed240aa66e6384.configuration_aurora.AuroraConfig'> for this kind of AutoModel: AutoModel.
Model type should be one of GPT2Config, AfmoeConfig, Aim
- **kairos-50m** (kairos, python 3.11.15): load: UnavailableError: kairos-50m: UnavailableError: kairos: transformers does not know model_type 'kairos' and the authors' package is not importable (The checkpoint you are trying to load has model type `kairos` but Transformers does not recognize this architecture. This could be because of an issue wi
