#!/usr/bin/env python3
"""Benchmark sweep: the same forecast protocol over every registered model.

This is the *effectiveness* half of the library (docs/09_benchmark.md) — the
compatibility matrix answers "does it run", this answers "how well does it forecast",
on the same series, the same test span, the same horizon grid, the same window count.

Dispatch is per family environment through the same interpreter resolver the matrix
uses, and every model runs in its own subprocess: an OOM or segfault in one family is
one failed row, not a lost sweep. Rows are appended to JSONL as they land, so an
interrupted sweep keeps what it measured, and `--report` can be re-run over partial
data.

    scripts/sweep_evaluate.py --series ~/data/raw/btc.csv --series ~/data/raw/gbpusd.csv \\
        --horizons 21,63,126 --max-windows 16 --out reports/effectiveness.jsonl
    scripts/sweep_evaluate.py --report reports/effectiveness.jsonl --md EFFECTIVENESS.md
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tsfm_trl.doctor import env_interpreters                      # noqa: E402
from tsfm_trl.model.registry import default_registry              # noqa: E402

BENCH_COLS = ("rmse", "mae", "mase", "dir_acc", "rank_corr", "relative_skill")
PROB_COLS = ("crps", "wql", "pinball")


def _models(reg, spec: str, tier: str) -> list[str]:
    keys = list(reg.keys())
    if spec and spec != "all":
        want = [m.strip() for m in spec.split(",") if m.strip()]
        unknown = [m for m in want if m not in set(keys)]
        if unknown:
            raise SystemExit(f"unknown model(s): {unknown}")
        return want
    if tier:
        return [k for k in keys if reg.get(k).tier == tier]
    return keys


def sweep(args) -> int:
    reg = default_registry()
    interp = env_interpreters(args.envs)
    keys = _models(reg, args.models, args.tier)
    done = set()
    out = Path(args.out)
    if out.exists() and not args.fresh:
        for line in out.read_text().splitlines():
            try:
                done.add(json.loads(line).get("model", ""))
            except json.JSONDecodeError:
                continue
    fh = out.open("a" if not args.fresh else "w")
    series = [os.path.expanduser(s) for s in args.series]
    n_ok = n_bad = 0
    for k in keys:
        if k in done:
            continue
        spec = reg.get(k)
        py = interp.get(spec.env) or interp.get("core") or sys.executable
        print(f"== {k} (env {spec.env}, {py})", flush=True)
        tmp = Path(f"/tmp/eval_{k}_{os.getpid()}.json")
        rows = []
        err = ""
        # one subprocess per (model, series): SeriesDataset is single-series, and a
        # per-series pass keeps a partial sweep readable instead of all-or-nothing
        for s in series:
            nm = os.path.splitext(os.path.basename(s))[0]
            cmd = [py, "-m", "tsfm_trl.cli", "evaluate", "--model", k, "--series", s,
                   "--horizons", args.horizons, "--spans", args.spans,
                   "--max-windows", str(args.max_windows),
                   "--device", args.device, "--out", str(tmp)]
            env = dict(os.environ)
            env.setdefault("TSFMTRL_QUIET", "1")
            t0 = time.time()
            try:
                p = subprocess.run(cmd, capture_output=True, text=True,
                                   timeout=args.timeout, env=env)
                if tmp.exists() and tmp.stat().st_size:
                    rows.extend(json.loads(tmp.read_text()))
                    tmp.unlink()
                elif p.returncode != 0:
                    tail = (p.stderr or p.stdout or "").strip().splitlines()
                    err = (tail[-1] if tail else f"rc={p.returncode}")[:300]
            except subprocess.TimeoutExpired:
                err = f"timeout after {args.timeout}s"
            except Exception as e:                                          # noqa: BLE001
                err = f"{type(e).__name__}: {e}"[:300]
            got = len([r for r in rows if r.get("series") == nm])
            print(f"  {k:20s} {nm:14s} "
                  f"{('ok ' + str(got)) if not err else 'FAIL'}"
                  f"  {time.time() - t0:6.1f}s {err[:100]}", flush=True)
        rec = {"model": k, "env": spec.env, "tier": spec.tier, "family": spec.family,
               "rows": rows, "error": err}
        fh.write(json.dumps(rec, default=float) + "\n")
        fh.flush()
        n_ok += bool(rows)
        n_bad += bool(err and not rows)
    fh.close()
    print(f"swept {n_ok} ok / {n_bad} failed -> {out}")
    return 0


def report(args) -> int:
    src = Path(args.report)
    recs = [json.loads(l) for l in src.read_text().splitlines() if l.strip()]
    rows = [r for rec in recs for r in rec["rows"]]
    failed = {rec["model"]: rec["error"] for rec in recs if rec["error"] and not rec["rows"]}
    notrun = [rec["model"] for rec in recs if not rec["rows"] and not rec["error"]]
    series = sorted({r["series"] for r in rows})
    hz = sorted({int(r["horizon"]) for r in rows})
    out = ["# Effectiveness benchmark", "",
           f"Generated {time.strftime('%Y-%m-%d %H:%M:%S')} from `{src}` — "
           f"{len(rows)} evaluation rows over {len(series)} series, horizons "
           f"{', '.join(map(str, hz))}. Protocol: `docs/09_benchmark.md`.", "",
           "Rows are **zero-shot** (no adaptation) and slide windows over the span(s) "
           "named above — for zero-shot rows the whole series is legitimate because the "
           "model saw no training data; an *adapted* checkpoint must be scored with "
           "`--spans test`, or the comparison leaks. Same horizon grid, same window "
           "count, same seed for every model. `ctx` is the "
           "context actually used (an oversized one is clamped to the span, which is "
           "recorded, not hidden). **CRPS/WQL/pinball appear only for models that emit "
           "quantiles**; a point-only model gets point metrics and is marked `pt` — a "
           "probabilistic column with a dash is not a zero. `skill` is MASE-ratio vs "
           "seasonal naive (<1 is better than the baseline).", ""]
    spans = sorted({r.get("span", "test") for r in rows})

    def cell(v):
        return "—" if v is None or (isinstance(v, float) and v != v) else f"{v:.3g}"

    for srs in series:
        for sp in spans:
            for h in hz:
                sel = [r for r in rows if r["series"] == srs
                       and r.get("span", "test") == sp and int(r["horizon"]) == h]
                if not sel:
                    continue
                sel.sort(key=lambda r: (r.get("mase") is None, r.get("mase") or 9e9))
                out += [f"## {srs} · {sp} · horizon {h}", "",
                        "| model | ctx | win | MASE ↓ | RMSE | MAE | dir-acc | rank ρ | "
                        "skill | CRPS ↓ | WQL | pinball |",
                        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
                for r in sel:
                    pt = "" if "crps" in r else " · pt"
                    out.append(f"| {r['model']} | {r['ctx']} | {r['n_windows']} | "
                               f"{cell(r.get('mase'))} | {cell(r.get('rmse'))} | "
                               f"{cell(r.get('mae'))} | {cell(r.get('dir_acc'))} | "
                               f"{cell(r.get('rank_corr'))} | "
                               f"{cell(r.get('relative_skill'))} | "
                               f"{cell(r.get('crps'))}{pt} | {cell(r.get('wql'))} | "
                               f"{cell(r.get('pinball'))} |")
                out.append("")

    if failed:
        out += ["## Failed or incomplete rows", ""]
        for m, why in sorted(failed.items()):
            out.append(f"- **{m}**: {why}")
        out.append("")
    if notrun:
        out += [f"## No rows (attempted, nothing scored): {', '.join(notrun)}", ""]
    text = "\n".join(out) + "\n"
    if args.md:
        Path(args.md).write_text(text)
        print(f"wrote {args.md}")
    if args.stdout:
        sys.stdout.write(text)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--series", action="append", default=[],
                    help="CSV with timestamp,close (repeatable)")
    ap.add_argument("--horizons", default="21,63,126")
    ap.add_argument("--max-windows", type=int, default=16)
    ap.add_argument("--spans", default="all",
                    help="zero-shot rows slide over 'all'; use 'test' when scoring "
                         "adapted checkpoints, or the comparison leaks")
    ap.add_argument("--models", default="all")
    ap.add_argument("--tier", default="", choices=["", "A", "B", "C"])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--envs", default="envs")
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--out", default="reports/effectiveness.jsonl")
    ap.add_argument("--fresh", action="store_true", help="truncate the JSONL first")
    ap.add_argument("--report", default="", help="render markdown from a JSONL and exit")
    ap.add_argument("--md", default="EFFECTIVENESS.md")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()
    if args.report:
        args.report = os.path.expanduser(args.report)
        return report(args)
    if not args.series:
        raise SystemExit("--series is required for a sweep (a benchmark needs a named "
                         "dataset; the built-in fixture is synthetic and only proves plumbing)")
    return sweep(args)


if __name__ == "__main__":
    raise SystemExit(main())
