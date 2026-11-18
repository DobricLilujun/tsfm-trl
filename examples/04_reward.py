#!/usr/bin/env python3
"""Reward post-training, both demonstrator cases.
    python examples/04_reward.py

* token model     -> Chronos-T5   : GRPO (sample K candidates, group-relative
  advantages, -A*logp with a KL anchor to the frozen reference weights)
* quantile model  -> Chronos-Bolt : reward descent (direct gradient through the
  differentiable quantile head)

The custom reward is a P&L-shaped one: `anchor` (last observed price) is part of the
signature precisely so a trading reward cannot be written to reward "predict the
context mean". This is a capability demo: a handful of steps on a few dozen windows.
"""
import numpy as np

from tsfm_trl import ModelHub, RewardSpec, RewardTrainer, TrainingConfig
from tsfm_trl.data.fixtures import tiny_finance


def pnl_reward(candidates, truth, anchor, cost=2e-4):
    """candidates (B,K,H), truth (B,H), anchor (B,1) -> (B,K), higher is better."""
    c = np.asarray(candidates, float)
    t = np.asarray(truth, float)
    a = np.asarray(anchor, float)
    pos = np.sign(np.median(c, axis=2) - a)                       # (B,K)
    realised = np.sign(t[:, -1:] - a)                             # (B,1) -> (B,K)
    return pos * realised - cost * (pos != 0)


ds = tiny_finance(600)
cfg = TrainingConfig(ctx=256, horizon=16, budget="fs16", steps=4, bs=2,
                     peft="heads_only", seed=0, out_dir="reports/ft_examples",
                     tag="reward_example")

for key, expect in (("chronos-t5-small", "grpo"), ("chronos-bolt-small", "reward_descent")):
    m = ModelHub.load(key, device="auto", ctx_cap=512, batch=2)
    tr = RewardTrainer(m, cfg, spec=RewardSpec(w_pinball=1.0, w_dir=0.5, w_cross=0.2),
                       reward=pnl_reward, n_candidates=6, kl=1e-3)
    res = tr.fit(ds)
    print(f"{key:20s} wanted {expect:14s} got {str(res.extra.get('mode')):16s} "
          f"status={res.status:6s} steps={res.steps} "
          f"reward {res.first_loss:.3f} -> {res.final_loss:.3f}  {res.reason}")
