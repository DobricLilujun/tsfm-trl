# Compatibility matrix

Generated 2026-11-18 02:22:38 on ubadmin-Precision-3591 (x86_64), python 3.11.15.

✅ ok · ❌ failed (see the JSON report for the captured reason) · — not offered by the model · ◐ partial · · not checked

Machines: ubadmin-Precision-3591/x86_64. One row per (model, environment); when two machines disagree the row that ran is kept and the other is recorded under *other machine* in the reasons.

| model | tier | weights | load | forecast | quantiles | embed | fine-tune | classify | anomaly | reward | s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| timesfm-2.0-500m | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 42.9 |
| arima | A | ✅ | ✅ | ✅ | ✅ | · | · | ✅ 2/2 | ✅ | · | 9.9 |
| moving_average | A | ✅ | ✅ | ✅ | — | · | · | ✅ 2/2 | ✅ | · | 1.5 |
| naive | A | ✅ | ✅ | ✅ | — | · | · | ✅ 2/2 | ✅ | · | 1.4 |
| seasonal_naive | A | ✅ | ✅ | ✅ | — | · | · | ✅ 2/2 | ✅ | · | 1.5 |
| theta | A | ✅ | ✅ | ✅ | — | · | · | ✅ 2/2 | ✅ | · | 2.3 |
| chronos-2 | A | ✅ | ✅ | ✅ | ✅ | · | ✅ | ✅ 2/2 | ✅ | ✅ | 9.4 |
| chronos-bolt-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (3.530→3.526) | ✅ 2/2 | ✅ | ✅ | 6.1 |
| chronos-t5-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (1.724→1.809) | ✅ 2/2 | ✅ | ✅ | 22.4 |
| flowstate-r1 | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (9.862→5.641) | ✅ 2/2 | ✅ | ✅ | 14.0 |
| timesfm-2.5-200m | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (0.347→0.450) | ✅ 2/2 | ✅ | ✅ | 11.2 |
| ttm-r2 | A | ✅ | ✅ | ✅ | — | · | ✅ (260.703→310.215) | ✅ 2/2 | ✅ | ✅ | 3.8 |
| ttm-r3 | A | ✅ | ✅ | ✅ | — | · | ✅ (134.923→118.313) | ✅ 2/2 | ✅ | ✅ | 2.6 |
| aurora | B | ✅ | ❌ | · | · | · | · | · | · | · | 2.2028162479400635 |
| chronos-bolt-base | B | ✅ | ✅ | ✅ | ✅ | · | ✅ (3.395→4.013) | ✅ 2/2 | ✅ | ✅ | 5.9 |
| chronos-t5-base | B | ✅ | ✅ | ✅ | ✅ | · | ✅ (1.615→1.723) | ✅ 1/2 | ✅ | ✅ | 34.2 |
| timesfm-3.0 | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 22.4 |
| patchtst-fm-r2 | C | ✅ | ✅ | ✅ | — | · | ❌ | ✅ 2/2 | ✅ | ❌ | 7.9 |
| moirai-1.1-R-small | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 8.4 |
| moirai-2.0-R-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (2.650→3.201) | ✅ 2/2 | ✅ | ✅ | 3.1 |
| moirai-1.1-R-base | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 5.0 |
| moirai-moe-1.0-R-base | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 17.2 |
| moment-1-large | A | ✅ | ✅ | ✅ | — | · | ✅ (84.251→4.319) | ✅ 2/3 | ✅ | ✅ | 63.1 |
| moment-1-small | B | ✅ | ✅ | ✅ | — | · | ✅ (215.365→96.405) | ✅ 2/3 | ✅ | ✅ | 7.8 |
| tirex | A | ✅ | ✅ | ✅ | ✅ | · | · | ✅ 2/2 | ✅ | · | 38.9 |
| tirex-2 | B | ✅ | ❌ | · | · | · | · | · | · | · | 1.7579233646392822 |
| timemoe-50m | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (0.025→0.043) | ✅ 1/2 | ✅ | ✅ | 111.7 |
| kronos-small | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (2.344→2.428) | ✅ 2/2 | ✅ | ✅ | 186.8 |
| kronos-base | B | ✅ | ✅ | ✅ | ✅ | · | ✅ (2.571→2.593) | ✅ 2/2 | ✅ | ✅ | 623.6 |
| kronos-mini | B | ✅ | ✅ | ✅ | ✅ | · | ✅ (9.000→9.137) | ✅ 2/2 | ✅ | ✅ | 49.3 |
| visiontspp-base | C | ❌ | ❌ | · | · | · | · | · | · | · | 1.2339987754821777 |
| hirondel-7m | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | — | ❌ | 12.1 |
| kairos-10m | A | ✅ | ✅ | ❌ | ❌ | · | ❌ | ✅ 2/2 | — | ❌ | 14.1 |
| t0-gamma | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 6.3 |
| timestral-28m | A | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 13.4 |
| kairos-50m | B | ✅ | ✅ | ❌ | ❌ | · | ❌ | ✅ 2/2 | — | ❌ | 13.1 |
| t0-alpha | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 5.7 |
| t0-beta | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 6.7 |
| timestral-123m | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 17.0 |
| timestral-5m | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 36.6 |
| yug | B | ✅ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 8.1 |
| timestral-209m | C | ❌ | ✅ | ✅ | ✅ | · | — | ✅ 2/2 | ✅ | · | 29.7 |
| toto-2-22m | A | ✅ | ✅ | ✅ | ✅ | · | ✅ (0.710→0.714) | ✅ 2/2 | ✅ | ✅ | 11.0 |
| toto-open-1.0 | B | ✅ | ❌ | · | · | · | · | · | · | · | 0.2056112289428711 |
| toto-2-313m | B | ✅ | ✅ | ✅ | ✅ | · | ✅ (1.211→1.157) | ✅ 2/2 | ✅ | ✅ | 24.9 |

## Captured failures

- **timesfm-2.0-500m** (timesfm20, python 3.11.15): finetune: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module); reward: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module)
- **arima** (baseline, python 3.11.15): reward: arima: no 'finetune' support (adapter exposes no trainable module)
- **moving_average** (baseline, python 3.11.15): reward: moving_average: no 'finetune' support (adapter exposes no trainable module)
- **naive** (baseline, python 3.11.15): reward: naive: no 'finetune' support (adapter exposes no trainable module)
- **seasonal_naive** (baseline, python 3.11.15): reward: seasonal_naive: no 'finetune' support (adapter exposes no trainable module)
- **theta** (baseline, python 3.11.15): reward: theta: no 'finetune' support (adapter exposes no trainable module)
- **aurora** (aurora, python 3.11.15): load: UnavailableError: aurora: ValueError: Unrecognized configuration class <class 'transformers_modules.DecisionIntelligence.Aurora.c495b02c1b151be52a3c174237ed240aa66e6384.configuration_aurora.AuroraConfig'> for this kind of AutoModel: AutoModel.
Model type should be one of GPT2Config, AfmoeConfig, Aim
- **chronos-t5-base** (chronos_t5, python 3.11.15): classify:probe: OutOfMemoryError: CUDA out of memory. Tried to allocate 182.00 MiB. GPU 0 has a total capacity of 5.64 GiB of which 69.31 MiB is free. Process 915373 has 163.04 MiB memory in use. Including non-PyTorc
- **timesfm-3.0** (timesfm30, python 3.11.15): finetune: timesfm-3.0: no 'finetune' support (the public timesfm package ships TimesFM 3.0 inference only (no documented training forward); contributing a head-only loop is tracked in docs/03_fine_tune.md); reward: timesfm-3.0: no 'finetune' support (adapter exposes no trainable module)
- **patchtst-fm-r2** (patchtst, python 3.11.15): finetune: TypeError: PatchTSTFMForPrediction.forward() got an unexpected keyword argument 'future_values'; reward: ValueError: peft='heads_only' matched no parameters; head_prefixes=('head', 'decoder'); declare them on the adapter (head_prefixes=...)
- **moirai-1.1-R-small** (moirai, python 3.11.15): finetune: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moirai-1.1-R-base** (moirai, python 3.11.15): finetune: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-1.1: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moirai-moe-1.0-R-base** (moirai_moe, python 3.11.15): finetune: moirai-moe: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune); reward: moirai-moe: no 'finetune' support (this uni2ts release exposes Moirai 1.1/MoE inference only through sample paths (``forward`` draws from the predicted distribution), and its ``_get_distr`` returns a distribution over the whole padded window, not the prediction slice. A differentiable step therefore needs uni2ts' own training stack (MoiraiForecast + PackedMaskedGlueTabDataset, see docs/03_fine_tune.md) — optimising quantiles of samples would be a no-op dressed as a fine-tune)
- **moment-1-large** (moment, python 3.11.15): classify:native: ValueError: num_class must be specified for classification.
- **moment-1-small** (moment, python 3.11.15): classify:native: ValueError: num_class must be specified for classification.
- **tirex** (tirex, python 3.11.15): reward: tirex: no 'finetune' support (adapter exposes no trainable module)
- **tirex-2** (tirex2, python 3.12.13): load: UnavailableError: tirex-2: UnavailableError: tirex-2: needs either the Triton kernels (GPU sm8.9 below sm10.0) or a CUDA toolchain for the native fallback (nvcc not found)  [install: run it on a Blackwell-class GPU (sm >= 10.0) with CUDA 13 + Triton >= 3.4, or install the full CUDA toolkit (nvcc) fo
- **timemoe-50m** (timemoe, python 3.11.15): finetune: loss did not fall: 0.024578 -> 0.042918; classify:probe: OutOfMemoryError: CUDA out of memory. Tried to allocate 92.00 MiB. GPU 0 has a total capacity of 5.64 GiB of which 8.44 MiB is free. Process 915373 has 163.04 MiB memory in use. Including non-PyTorch 
- **visiontspp-base** (visionts, python 3.11.15): load: UnavailableError: visiontspp-base: UnavailableError: visiontspp-base: VisionTS++ needs the upstream package (the Hub repo ships .ckpt weights only): No module named 'visiontspp'  [install: git clone the VisionTS/VisionTS++ upstream, then weights=/path/to/visiontspp_base.ckpt. clone it and point the 
- **hirondel-7m** (hirondel, python 3.12.13): finetune: hirondel-7m: no 'finetune' support (hirondel.forward(['coarse', 'horizon', 'observed', 'x']) has no supervised target argument in the installed version); anomaly: TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'; reward: ValueError: fp and xp are not of the same length.
- **kairos-10m** (kairos, python 3.12.13): finetune: RuntimeError: Boolean value of Tensor with more than one value is ambiguous; anomaly: ValueError: operands could not be broadcast together with shapes (4,16) (4,128) ; reward: ValueError: operands could not be broadcast together with shapes (2,4,128) (2,1,16) 
- **t0-gamma** (t0, python 3.12.13): finetune: t0-gamma: no 'finetune' support (adapter exposes no trainable module); reward: t0-gamma: no 'finetune' support (adapter exposes no trainable module)
- **timestral-28m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **kairos-50m** (kairos, python 3.12.13): finetune: RuntimeError: Boolean value of Tensor with more than one value is ambiguous; anomaly: ValueError: operands could not be broadcast together with shapes (4,16) (4,128) ; reward: ValueError: operands could not be broadcast together with shapes (2,4,128) (2,1,16) 
- **t0-alpha** (t0, python 3.12.13): finetune: t0-gamma: no 'finetune' support (adapter exposes no trainable module); reward: t0-gamma: no 'finetune' support (adapter exposes no trainable module)
- **t0-beta** (t0, python 3.12.13): finetune: t0-gamma: no 'finetune' support (adapter exposes no trainable module); reward: t0-gamma: no 'finetune' support (adapter exposes no trainable module)
- **timestral-123m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **timestral-5m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **yug** (yug, python 3.12.13): finetune: yug: no 'finetune' support (adapter exposes no trainable module); reward: yug: no 'finetune' support (adapter exposes no trainable module)
- **timestral-209m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **toto-open-1.0** (toto1, python 3.12.13): load: UnavailableError: toto-open-1.0: ValueError: Unrecognized model in Datadog/Toto-Open-Base-1.0. Should have a `model_type` key in its config.json, or contain one of the following strings in its name: albert, align, altclip, aria, aria_text, audio-spectrogram-transformer, autoformer, aya_vision, bamba
