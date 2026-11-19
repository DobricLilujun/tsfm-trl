# Compatibility matrix

Generated 2026-11-20 00:21:11 on ubadmin-Precision-3591 (x86_64), python 3.11.15.

✅ ok · ❌ failed (see the JSON report for the captured reason) · — not offered by the model · ◐ partial · · not checked

A ✅ *fine-tune* cell means a differentiable objective ran, gradients were feasible and loss logging worked at smoke size. The `(a→b)` in that cell is the loss across the **two** smoke steps: it is a capability check, not a claim that fine-tuning improves out-of-sample error (`docs/03_fine_tune.md`). `classify n/m` counts the probe / head+LoRA / native routes that ran.

Machines: gpu7/aarch64, ubadmin-Precision-3591/x86_64. One row per (model, environment); when two machines disagree the row that ran is kept and the other is recorded under *other machine* in the reasons.

| model | tier | weights | load | forecast | quantiles | embed | fine-tune | classify | anomaly | reward | s | machine |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| arima | A | ✅ | ✅ | ✅ | ✅ | ✅ | · | ✅ 2/2 | ✅ | — | 5.9 | gpu7/aarch64 |
| moving_average | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 0.7 | gpu7/aarch64 |
| naive | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 0.6 | gpu7/aarch64 |
| seasonal_naive | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 0.6 | gpu7/aarch64 |
| theta | A | ✅ | ✅ | ✅ | — | ✅ | · | ✅ 2/2 | ✅ | — | 0.8 | gpu7/aarch64 |
| chronos-2 | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 2/2 | ✅ | ✅ | 14.3 | gpu7/aarch64 |
| chronos-bolt-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.530→3.526) | ✅ 2/2 | ✅ | ✅ | 2.4 | gpu7/aarch64 |
| chronos-t5-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (1.774→1.814) | ✅ 2/2 | ✅ | ✅ | 10.3 | gpu7/aarch64 |
| flowstate-r1 | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (7.098→7.722) | ✅ 2/2 | ✅ | ✅ | 2.0 | gpu7/aarch64 |
| hirondel-7m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.061→0.104) | ✅ 2/2 | ✅ | ✅ | 13.5 | ubadmin-Precision-3591/x86_64 |
| kairos-10m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.458→0.110) | ✅ 2/2 | ✅ | ✅ | 8.8 | ubadmin-Precision-3591/x86_64 |
| kronos-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.344→2.453) | ✅ 2/2 | ✅ | ✅ | 63.5 | gpu7/aarch64 |
| moirai-1.1-R-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.562→2.413) | ✅ 2/2 | ✅ | ✅ | 14.0 | gpu7/aarch64 |
| moirai-2.0-R-small | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.650→3.201) | ✅ 2/2 | ✅ | ✅ | 1.6 | gpu7/aarch64 |
| moment-1-large | A | ✅ | ✅ | ✅ | — | ✅ | ✅ (219.576→97.814) | ✅ 3/3 | ✅ | ✅ | 30.4 | gpu7/aarch64 |
| sundial-base-128m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.436→3.505) | ✅ 2/2 | ✅ | ✅ | 20.4 | gpu7/aarch64 |
| t0-gamma | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.052→3.046) | ✅ 2/2 | ✅ | ✅ | 8.8 | ubadmin-Precision-3591/x86_64 |
| timemoe-50m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.025→0.043) | ✅ 2/2 | ✅ | ✅ | 148.6 | gpu7/aarch64 |
| timesfm-2.0-500m | A | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 85.0 | gpu7/aarch64 |
| timesfm-2.5-200m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.347→0.450) | ✅ 2/2 | ✅ | ✅ | 5.9 | gpu7/aarch64 |
| timestral-28m | A | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 14.8 | ubadmin-Precision-3591/x86_64 |
| tirex | A | ✅ | ✅ | ✅ | ✅ | ✅ | · | ✅ 2/2 | ✅ | — | 17.1 | gpu7/aarch64 |
| toto-2-22m | A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.710→0.714) | ✅ 2/2 | ✅ | ✅ | 26.1 | gpu7/aarch64 |
| ttm-r2 | A | ✅ | ✅ | ✅ | — | ✅ | ✅ (219.444→315.138) | ✅ 2/2 | ✅ | ✅ | 0.8 | gpu7/aarch64 |
| ttm-r3 | A | ✅ | ✅ | ✅ | — | ✅ | ✅ (134.459→118.437) | ✅ 2/2 | ✅ | ✅ | 1.4 | gpu7/aarch64 |
| aurora | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 37.1 | ubadmin-Precision-3591/x86_64 |
| chronos-bolt-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.606→3.812) | ✅ 2/2 | ✅ | ✅ | 7.3 | gpu7/aarch64 |
| chronos-t5-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (1.702→1.733) | ✅ 2/2 | ✅ | ✅ | 29.3 | gpu7/aarch64 |
| kairos-50m | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.099→0.114) | ✅ 2/2 | ✅ | ✅ | 4.7 | ubadmin-Precision-3591/x86_64 |
| kronos-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.559→2.605) | ✅ 2/2 | ✅ | ✅ | 203.8 | gpu7/aarch64 |
| kronos-mini | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (9.066→9.096) | ✅ 2/2 | ✅ | ✅ | 26.1 | gpu7/aarch64 |
| moirai-1.1-R-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.576→2.852) | ✅ 2/2 | ✅ | ✅ | 6.0 | gpu7/aarch64 |
| moirai-moe-1.0-R-base | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.496→3.328) | ✅ 2/2 | ✅ | ✅ | 52.9 | gpu7/aarch64 |
| moment-1-small | B | ✅ | ✅ | ✅ | — | ✅ | ✅ (244.804→108.576) | ✅ 3/3 | ✅ | ✅ | 5.3 | gpu7/aarch64 |
| t0-alpha | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (4.039→3.726) | ✅ 2/2 | ✅ | ✅ | 4.7 | ubadmin-Precision-3591/x86_64 |
| t0-beta | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (2.990→3.380) | ✅ 2/2 | ✅ | ✅ | 6.0 | ubadmin-Precision-3591/x86_64 |
| timesfm-3.0 | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 12.7 | gpu7/aarch64 |
| timestral-123m | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 19.8 | ubadmin-Precision-3591/x86_64 |
| timestral-5m | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 11.0 | ubadmin-Precision-3591/x86_64 |
| tirex-2 | B | ✅ | ✅ | ❌ | · | ❌ | · | ❌ 0/2 | — | — | 8.6 | gpu7/aarch64 |
| toto-open-1.0 | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (3.067→2.643) | ✅ 2/2 | ✅ | ✅ | 235.2 | gpu7/aarch64 |
| toto-2-313m | B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (0.703→0.712) | ✅ 2/2 | ✅ | ✅ | 93.0 | gpu7/aarch64 |
| yug | B | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 9.3 | ubadmin-Precision-3591/x86_64 |
| patchtst-fm-r2 | C | ✅ | ✅ | ✅ | — | ✅ | — | ✅ 2/2 | ✅ | ✅ | 21.6 | gpu7/aarch64 |
| timestral-209m | C | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ 2/2 | ✅ | — | 23.7 | ubadmin-Precision-3591/x86_64 |
| visiontspp-base | C | ❌ | ❌ | · | · | · | · | · | · | · | 1.2 | gpu7/aarch64 |

## Summary

| task | ok | declined by the model | failed | not checked |
|---|---|---|---|---|
| load | 45 | 0 | 1 | 0 |
| predict | 44 | 0 | 1 | 1 |
| quantiles | 35 | 9 | 0 | 2 |
| embed | 44 | 0 | 1 | 1 |
| finetune | 29 | 9 | 0 | 8 |
| classify | 44 | 0 | 1 | 1 |
| anomaly | 44 | 1 | 0 | 1 |
| reward | 30 | 15 | 0 | 1 |

'declined' means the model or its vendor package offers no path for that task in this environment (a `—` in the table): Moirai 1.1 `forward` draws samples instead of returning differentiable quantiles, TimesFM's public build ships inference only, Aurora's flow-matching head has no public training step. 'failed' means something was attempted and broke, with the reason captured below. A declined row is a statement about the model package; a failed row is a statement about this environment or our adapter.


## Captured failures

- **arima** (baseline, python 3.11.14): reward: arima: no 'finetune' support (adapter exposes no trainable module)
- **moving_average** (baseline, python 3.11.14): reward: moving_average: no 'finetune' support (adapter exposes no trainable module)
- **naive** (baseline, python 3.11.14): reward: naive: no 'finetune' support (adapter exposes no trainable module)
- **seasonal_naive** (baseline, python 3.11.14): reward: seasonal_naive: no 'finetune' support (adapter exposes no trainable module)
- **theta** (baseline, python 3.11.14): reward: theta: no 'finetune' support (adapter exposes no trainable module)
- **hirondel-7m** (hirondel, python 3.12.13): finetune: loss did not fall: 0.061029 -> 0.103562
- **kairos-10m** (kairos, python 3.12.13): other machine: ubadmin-Precision-3591/x86_64: finetune=fail, reward=fail
- **moment-1-large** (moment, python 3.11.14): other machine: ubadmin-Precision-3591/x86_64: reward=fail
- **timemoe-50m** (timemoe, python 3.11.14): finetune: loss did not fall: 0.024578 -> 0.042918
- **timesfm-2.0-500m** (timesfm20, python 3.11.14): finetune: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module); reward: timesfm-2.0-500m: no 'finetune' support (adapter exposes no trainable module)
- **timestral-28m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **tirex** (tirex, python 3.11.14): reward: tirex: no 'finetune' support (adapter exposes no trainable module)
- **aurora** (aurora, python 3.12.13): finetune: aurora: no 'finetune' support (adapter exposes no trainable module); reward: aurora: no 'finetune' support (adapter exposes no trainable module)
- **chronos-t5-base** (chronos_t5, python 3.11.14): other machine: ubadmin-Precision-3591/x86_64: predict=fail, reward=fail
- **kairos-50m** (kairos, python 3.12.13): other machine: ubadmin-Precision-3591/x86_64: finetune=fail, reward=fail
- **timesfm-3.0** (timesfm30, python 3.11.14): finetune: timesfm-3.0: no 'finetune' support (the public timesfm package ships TimesFM 3.0 inference only (no documented training forward); contributing a head-only loop is tracked in docs/03_fine_tune.md); reward: timesfm-3.0: no 'finetune' support (adapter exposes no trainable module)
- **timestral-123m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **timestral-5m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **tirex-2** (tirex2, python 3.12.14): predict: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial states
        matC_k_val = tl.load(matCinitial_ptr, boundary_check=(0, 1)).to(tl.float32)
        vecN; embed: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial sta; other machine: ubadmin-Precision-3591/x86_64: load=fail; anomaly: CompilationError: at 85:21:
        # each thread block loads the scaMinter_initial
        scaMinterinitial_ptr = scaMinter_initial + idx_b_BNH * str_scaMinterinitial_B_NH

        # load initial sta; reward: tirex-2: no 'finetune' support (adapter exposes no trainable module)
- **toto-open-1.0** (toto1, python 3.12.14): other machine: gpu7/aarch64: load=fail
- **yug** (yug, python 3.12.13): finetune: yug: no 'finetune' support (adapter exposes no trainable module); reward: yug: no 'finetune' support (adapter exposes no trainable module)
- **patchtst-fm-r2** (patchtst, python 3.11.14): finetune: patchtst-fm-r2: no 'finetune' support (forward(['output_hidden_states', 'pad_mask', 'past_observed_mask', 'past_values', 'prediction_length', 'quantile_levels', 'return_dict', 'return_loss']) declares no target argument in transformers 5.22.1); other machine: gpu7/aarch64: finetune=fail
- **timestral-209m** (timestral, python 3.12.13): finetune: timestral: no 'finetune' support (the released timestral package exposes the inference forecaster only; wire the vendor training forward (mistralai/timestral) before claiming a Timestral fine-tune); reward: timestral: no 'finetune' support (adapter exposes no trainable module)
- **visiontspp-base** (visionts, python 3.11.14): load: UnavailableError: visiontspp-base: UnavailableError: visiontspp-base: VisionTS++ needs the upstream package (the Hub repo ships .ckpt weights only): No module named 'visiontspp'  [install: git clone the VisionTS/VisionTS++ upstream, then weights=/path/to/visiontspp_base.ckpt. clone it and point the ; other machine: ubadmin-Precision-3591/x86_64: load=fail
