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
    n_ok = n_bad = skipped = 0
    for k in keys:
        if k in done:
            continue
        spec = reg.get(k)
        # No silent fallback to `core`: a family run in an interpreter it was never
        # installed into reports a foreign environment's failure (or its numbers) as if
        # they belonged to the family. Missing env => a recorded skip.
        py = interp.get(spec.env)
        if not py and args.allow_core_fallback:
            py = interp.get("core") or sys.executable
        if not py:
            why = (f"no interpreter for env '{spec.env}' on this machine: row skipped, "
                   f"not measured (the matrix ran it in {spec.env})")
            print(f"== {k}: {why}", flush=True)
            fh.write(json.dumps({"model": k, "env": spec.env, "tier": spec.tier,
                                 "family": spec.family, "rows": [], "error": why,
                                 "interpreter": ""}) + "\n")
            fh.flush()
            skipped += 1
            continue
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
        # `interpreter` is provenance, not trivia: the same model measured in a
        # different venv is a different experiment, and the report must be able to say
        # which venv produced which row.
        rec = {"model": k, "env": spec.env, "tier": spec.tier, "family": spec.family,
               "interpreter": py, "rows": rows, "error": err}
        fh.write(json.dumps(rec, default=float) + "\n")
        fh.flush()
        n_ok += bool(rows)
        n_bad += bool(err and not rows)
    fh.close()
    print(f"swept {n_ok} ok / {n_bad} failed / {skipped} env-skipped -> {out}")
    return 0


def report(args) -> int:
    src = Path(str(args.report).split(",")[0])
    srcs = [Path(x).expanduser() for x in str(args.report).split(",")]
    recs = [json.loads(l) for f in srcs for l in f.read_text().splitlines() if l.strip()]
    # one meta block per input file: a merged report says which machine ran what
    metas = [r["meta"] for r in recs if "meta" in r]
    meta = metas[0] if metas else {}
    recs = [r for r in recs if "meta" not in r]
    # one record per model across all inputs: a row set beats an error, later beats earlier
    best: dict = {}
    for r in recs:
        cur = best.get(r["model"])
        if cur is None or bool(r.get("rows")) >= bool(cur.get("rows")):
            best[r["model"]] = r
    recs = [best[k] for k in sorted(best)]
    # label rows by the registry key the sweep asked for: several adapters report a
    # family-level key internally (two Chronos sizes both say "chronos-t5"), which would
    # otherwise merge different models into one indistinguishable row
    rows = []
    for rec in recs:
        for r in rec["rows"]:
            r["model_key"] = rec["model"]
            rows.append(r)
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
           "count, same seed for every model. Rows carry the **registry key the sweep "
           "requested** (adapters may report a family-level key internally). `ctx` is the "
           "context actually used (an oversized one is clamped to the span, which is "
           "recorded, not hidden). **CRPS/WQL/pinball appear only for models that emit "
           "quantiles**; a point-only model gets point metrics and is marked `pt` — a "
           "probabilistic column with a dash is not a zero. `skill` is "
           "`1 − MASE` (MASE normalises by the in-sample mean |Δ| of the train span), so "
           "MASE is the column to read and a negative skill means the model lost to that "
           "trivial scaler on this series.", ""]
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
                    out.append(f"| {r.get('model_key') or r['model']} | {r['ctx']} | "
                               f"{r['n_windows']} | "
                               f"{cell(r.get('mase'))} | {cell(r.get('rmse'))} | "
                               f"{cell(r.get('mae'))} | {cell(r.get('dir_acc'))} | "
                               f"{cell(r.get('rank_corr'))} | "
                               f"{cell(r.get('relative_skill'))} | "
                               f"{cell(r.get('crps'))}{pt} | {cell(r.get('wql'))} | "
                               f"{cell(r.get('pinball'))} |")
                out.append("")

    mismatch = [(r["model"], r["env"], r.get("interpreter", "")) for r in recs
                if r["rows"] and r.get("interpreter")
                and f"envs/{r['env']}/" not in r["interpreter"].replace("/home/", "")
                and not r["interpreter"].endswith(f"/{r['env']}/bin/python")
                and f".venv-{r['env']}" not in r["interpreter"] and r["env"] != "core"
                and ".venv2" not in r["interpreter"]]
    if mismatch:
        out += ["## Environment provenance to check", "",
                "Rows whose interpreter does not obviously match the env the registry "
                "names for that model (usually a venv alias — verify before quoting):",
                ""] + [f"- {m} (env {e}) ran with `{i}`" for m, e, i in mismatch] + [""]
    # a table that leaves models out is read as "they were fine"; say who is missing
    try:
        reg_keys = set(default_registry().keys())
    except Exception:                                          # noqa: BLE001
        reg_keys = set()
    absent = sorted(reg_keys - {r["model"] for r in recs})
    if absent:
        out += [f"## Not in this table ({len(absent)} of {len(reg_keys)} registry models)",
                "", "No row was produced for these yet — they are **not** measured here, "
                "and their absence is not a pass:", "",
                ", ".join(f"`{m}`" for m in absent), ""]
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
    ap.add_argument("--allow-core-fallback", action="store_true",
                    help="run a model in the core interpreter if its own env is missing "
                         "(off by default: numbers from an environment the matrix does "
                         "not name for that model are a different experiment)")
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--out", default="reports/effectiveness.jsonl")
    ap.add_argument("--fresh", action="store_true", help="truncate the JSONL first")
    ap.add_argument("--report", default="",
                    help="render markdown from JSONL(s); comma-separated merges several "
                         "runs/machines (rows beat errors)")
    ap.add_argument("--md", default="EFFECTIVENESS.md")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()
    if args.report:
        return report(args)
    if not args.series:
        raise SystemExit("--series is required for a sweep (a benchmark needs a named "
                         "dataset; the built-in fixture is synthetic and only proves plumbing)")
    return sweep(args)


if __name__ == "__main__":
    raise SystemExit(main())
