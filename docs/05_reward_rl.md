# 5 · Reward post-training (`RewardTrainer`)

One trainer, three mechanisms, chosen by what the model actually exposes:

| mode | what it optimises | which families can do it |
|---|---|---|
| `grpo` | group-relative policy gradient on **token log-probabilities** | token models: Chronos-T5, Time-MoE, Sundial (anything with `loss_kind="token"` + `path_logprob`) |
| `reward_descent` | direct gradient through a **differentiable quantile head** | Chronos-2/Bolt, Moirai 2, Toto, TiRex-2, FlowState |
| `reward_descent_point` | same, on a **mean-only head** (interval terms switched off) | MOMENT, small TTM releases |
| `rft` | rejection sampling / best-of-N: keep the best candidates, then supervise | any family with a `training_step` |

```python
from tsfm_trl import RewardSpec, RewardTrainer, ModelHub, TrainingConfig

m = ModelHub.load("chronos-2", device="cuda")
r = RewardTrainer(m, TrainingConfig(budget="fs16", steps=6, peft="heads_only"),
                  spec=RewardSpec(w_pinball=1.0, w_dir=0.5, w_cross=0.2),
                  n_candidates=8, kl=1e-3).fit(dataset)
r.extra["mode"]        # 'reward_descent'
```

CLI:

```bash
tsfm-trl reward --model chronos-t5 --steps 6 --candidates 8 --kl 1e-3 \
                --mode auto --budget fs16 --horizon 21 --ctx 256
```

## The default reward

`RewardSpec` is accuracy plus direction minus the pathologies that make a
probabilistic forecast useless in a portfolio:

```
reward = −w_pinball · pinball(quantiles, truth)
         + w_dir     · directional_accuracy(median vs truth)
         − w_cross   · quantile-crossing penalty
reward clipped to ±spec.clip          # outlier windows must not dominate a batch
```

## Bring your own reward

Any callable with this signature replaces it — the trading case is the reason the
signature has an `anchor`:

```python
def pnl(candidates, truth, anchor, *, cost=2e-4):
    """candidates (B,K,H), truth (B,H), anchor (B,1) -> reward (B,K)

    anchor is the last observed price: P&L is relative, so a reward that ignores it
    silently rewards forecasts that are simply close to the mean of the context.
    """
    pos = np.sign(np.median(candidates, axis=2) - anchor)          # (B,K)
    ret = np.log(truth[:, -1:] / anchor) - np.log(truth[:, -1:] - 0 * anchor)
    return pos * np.sign(ret) - cost * (pos != 0)

RewardTrainer(m, cfg, reward=pnl).fit(ds)
```

## GRPO, concretely

Per step: draw `K` candidate continuations, score them, convert rewards to
group-relative advantages `A = (r − mean)/std` across the group, then

```
loss = −Σ A · logp(candidates)  +  kl · KL(π ‖ π_ref)
```

with `π_ref` a frozen clone of the trainable parameters taken at the start of the run.
That is the ordinary GRPO update, at smoke scale (`reward_steps`, `n_candidates`),
which is what makes the matrix column meaningful: it proves the log-prob path, the
candidate sampler and the KL anchor all *run* on that family.

## Honest limits

* This is **reward post-training, not an RL benchmark**. Six steps on 16 windows is a
  capability check; `mean_reward` in the output is the mean reward of the *final* step,
  not a policy's expected return.
* `reward_descent` is not policy gradient — for a deterministic quantile head the reward
  is differentiable, and pretending otherwise would add variance for no bias-free
  benefit. The mode is recorded in the checkpoint and in `TrainResult.extra["mode"]`.
* Families with no gradient path at all (TimesFM inference builds, TiRex) report
  `— (no reward path)` rather than being run through a surrogate.
* Moirai 1.1 / Moirai-MoE are `—`: their head draws samples, so a "reward gradient"
  would be noise with a learning rate attached.

## Memory

The same ladder as fine-tuning (`bs/amp/peft` stepped down on OOM), and the same rule
that CUDA *toolchain* failures are environment problems: the run retries cheaper and
writes `fallbacks: [...]` into the checkpoint, so a table never hides the fact that a
row ran at `bs=1 bf16 heads_only`.

Runnable shape of the call: `examples/04_reward.py` (core env, one GPU, ~1 minute).

## Demonstrators (what was actually run)

Two models, small data (16 windows, `fs64` budget), LoRA, one GPU. Both are recorded
with the *quartile-mean* comparison described above rather than first-step-vs-last-step.

| model | family | mode | steps | reward early → late | verdict |
|---|---|---|---|---|---|
| `chronos-t5-small` | token (encoder-decoder) | `grpo` (8 sampled continuations, group-relative advantage) | 96 | **1.721 → 1.827** | improved |
| `toto-2-22m` | quantile head, inference path only | `rft` (rejection-sampling filtered fine-tune) | 48 | **−2.232 → −1.914** | improved |
| `flowstate-r1` | differentiable quantile head | `reward_descent` | 96 | −1.296 → −1.387 | **not improved** |

The FlowState row is kept as a negative result (re-run with quartile reporting: early
mean −1.296, late mean −1.387). What it shows: the run fell to the ladder profile
`bs=1, amp=bf16, peft=heads_only` under memory pressure, and gradient descent on the
pinball-plus-direction reward at that profile drifts the reward down instead of up. A reward *path* is demonstrated (the mode runs, the curve is logged);
a reward *gain* on a differentiable head is not demonstrated at this budget. Anyone
concluding "reward post-training helps TSForecasters" from this repo would be
over-reading it.

Reproduce:

```bash
tsfm-trl reward --model chronos-t5-small --steps 96 --bs 8 --lr 2e-5 \
                --budget fs64 --peft lora --device cuda
tsfm-trl reward --model toto-2-22m      --steps 48 --budget fs64 --peft lora --device cuda
```
