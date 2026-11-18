"""Rolling-origin evaluation — the part that answers "did fine-tuning help?".

Windows come **only from the evaluation span**, and the metric set is the same for
zero-shot and adapted models, so a delta is a delta.
"""
from __future__ import annotations

import time

import numpy as np

from ..data.series import SeriesDataset, windows
from ..errors import DataError
from .metrics import classification_report, forecast_report


def forecast_eval(model, dataset, *, horizons=(21,), spans=("test",), ctx: int | None = None,
                  stride: int | None = None, max_windows: int | None = 64,
                  batch: int = 16, seed: int = 0, season: int = 1) -> list[dict]:
    ds = dataset if isinstance(dataset, SeriesDataset) else SeriesDataset.load(dataset)
    ctx = int(ctx or min(model.max_context, 256))
    rows = []
    for span in spans:
        a, b = ds.splits.get(span, (0, len(ds.values)))
        y_span = ds.values[a:b]
        train = ds.split("train")
        for h in horizons:
            w = windows(y_span, h, ctx, stride=stride or h, max_windows=max_windows, seed=seed)
            if not w:
                raise DataError(f"{ds.name}/{span}: no evaluation windows "
                                f"(need >= {ctx + h}, have {len(y_span)})")
            cs = [x[0] for x in w]
            ys = np.stack([x[1] for x in w])
            panels = None
            if "panel_in" in set(getattr(model, "caps", ())) and ds.panel is not None:
                panels = [ds.panel_window(a + i, a + i + ctx) for i, _ in enumerate(w)]
            t0 = time.time()
            pred = model.predict(cs, h, panels=panels)
            row = {"model": getattr(model, "key", "?"), "adaptation":
                   getattr(model, "adaptation", "zero"), "series": ds.name, "span": span,
                   "horizon": int(h), "ctx": ctx, "n_windows": len(w),
                   "seconds": round(time.time() - t0, 2),
                   "no_leakage": True,
                   **forecast_report(ys, pred, train, season=season)}
            row["meta"] = {k: v for k, v in (pred.meta or {}).items() if isinstance(v, (int, float, str, bool))}
            rows.append(row)
    return rows


def classify_eval(model, cds, *, routes=("probe_stat", "probe_model"), kinds=("logistic",),
                  folds_mode: str = "expanding", seed: int = 0) -> list[dict]:
    """Shallow-classifier classification rows (the probe routes). The end-to-end
    route lives in :class:`tsfm_trl.training.classify.ClassificationTrainer`."""
    from ..probing.features import folds, make_classifier, model_matrix, stat_matrix
    X, y, tr, te = cds.parts()
    rows = []
    for route in routes:
        F = stat_matrix(X) if route == "probe_stat" else model_matrix(model, X)
        for kind in kinds:
            preds = np.full(len(y), -1, dtype=int)
            scores = np.zeros((len(y), max(2, cds.n_classes)))
            for tri, tei in folds(cds.split, mode=folds_mode):
                if len(np.unique(y[tri])) < 2:
                    continue
                clf = make_classifier(kind, seed)
                clf.fit(F[tri], y[tri])
                if hasattr(clf, "predict_proba"):
                    pr = clf.predict_proba(F[tei])
                    scores[tei] = pr if pr.shape[1] == scores.shape[1] else \
                        np.c_[pr, np.zeros((len(tei), scores.shape[1] - pr.shape[1]))]
                preds[tei] = clf.predict(F[tei])
            keep = preds >= 0
            if not keep.any():
                continue
            rep = classification_report(y[keep], preds[keep], n_classes=cds.n_classes)
            pos = None
            if cds.n_classes == 2 and scores.shape[1] == 2:
                pos = scores[keep][:, 1]
                rep.update(classification_report(y[keep], pos, n_classes=2))
            rows.append({"model": getattr(model, "key", "?"), "route": route,
                         "classifier": kind, "dataset": cds.name,
                         "folds": folds_mode, **rep,
                         "n_scored": int(keep.sum())})
    return rows
