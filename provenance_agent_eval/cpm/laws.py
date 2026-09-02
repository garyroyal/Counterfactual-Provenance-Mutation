"""Fit and test degradation laws on CPM sweep cells.

A degradation curve is the trace-level rate of an outcome (attack success on
attack twins, false blocking on benign twins) as a function of the provenance
error rate ``p``.  Under independent per-hop corruption the curves have
closed forms that depend only on trace structure:

* a value survives (or is laundered through) a chain of ``m`` hops if *any*
  hop is corrupted: ``1 - (1 - p) ** m``;
* a call with ``k`` guarded arguments is admitted only if *all* of them pass:
  ``[...] ** k``.

The general family fitted here is ``y = y0 + (1 - y0) * (1 - (1 - p) ** m) ** k``.
Two things are reported for every curve: the best-fitting free ``(m, k)`` and,
when the caller supplies a structural prediction, the goodness of fit of the
**zero-free-parameter** law with ``m``/``k`` taken from the trace structure.
The second number is the real test; the first only says which shape fits.
"""

from __future__ import annotations

import gzip
import json
import math
import random
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


ATTACK = "attack_success"
FBR = "false_blocking"


def load_cells(sweep_dir: str | Path) -> list[dict[str, Any]]:
    with gzip.open(Path(sweep_dir) / "cells.jsonl.gz", "rt", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def trace_outcome(cell: dict[str, Any], metric: str) -> float | None:
    """Trace-level binary outcome for one replayed cell, or None if not applicable."""

    outcomes = [item for item in cell["outcomes"]]
    if metric == ATTACK:
        if not cell.get("attack_trace"):
            return None
        return float(any(item["side_effect"] and not item["expected_allowed"] for item in outcomes))
    if metric == FBR:
        if cell.get("attack_trace"):
            return None
        safe = [item for item in outcomes if item["expected_allowed"]]
        if not safe:
            return None
        return float(any(not item["allowed"] for item in safe))
    raise ValueError(metric)


@dataclass(frozen=True)
class Curve:
    """Cluster-structured observations of one metric along the rate axis."""

    operator: str
    defense: str
    metric: str
    group: dict[str, Any]
    clusters: dict[float, dict[str, list[float]]]  # rate -> trace_id -> unit outcomes

    @property
    def rates(self) -> tuple[float, ...]:
        return tuple(sorted(self.clusters))

    def mean(self, rate: float) -> float | None:
        values = [value for units in self.clusters.get(rate, {}).values() for value in units]
        return sum(values) / len(values) if values else None

    def means(self) -> dict[float, float | None]:
        return {rate: self.mean(rate) for rate in self.rates}

    def traces(self) -> int:
        return len({trace for units in self.clusters.values() for trace in units})


def build_curves(
    cells: Iterable[dict[str, Any]],
    *,
    metric: str,
    group_keys: Sequence[str] = (),
    where: Callable[[dict[str, Any]], bool] | None = None,
) -> list[Curve]:
    """Group cells by (operator, defense, propagate, *group_keys) into curves."""

    buckets: dict[tuple, dict[float, dict[str, list[float]]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for cell in cells:
        if where is not None and not where(cell):
            continue
        outcome = trace_outcome(cell, metric)
        if outcome is None:
            continue
        group = tuple((key, cell.get(key)) for key in group_keys)
        key = (cell["operator"], cell["defense"], bool(cell.get("propagate", True)), group)
        buckets[key][float(cell["rate"])][cell["trace_id"]].append(outcome)
    curves: list[Curve] = []
    for (operator, defense, propagate, group), by_rate in sorted(buckets.items(), key=lambda item: str(item[0])):
        curves.append(
            Curve(
                operator=operator,
                defense=defense,
                metric=metric,
                group={"propagate": propagate, **dict(group)},
                clusters={rate: dict(units) for rate, units in by_rate.items()},
            )
        )
    return curves


# --- law family ---------------------------------------------------------------


def compound(p: float, m: float, k: float, y0: float = 0.0) -> float:
    """``y0 + (1 - y0) * (1 - (1 - p) ** m) ** k``."""

    inner = 1.0 - (1.0 - p) ** m
    inner = min(1.0, max(0.0, inner))
    return y0 + (1.0 - y0) * inner ** k


@dataclass(frozen=True)
class LawFit:
    family: str
    m: float
    k: float
    y0: float
    sse: float
    r2: float | None
    max_abs_residual: float
    free_parameters: int
    predictions: dict[float, float] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "family": self.family,
            "m": self.m,
            "k": self.k,
            "y0": self.y0,
            "sse": self.sse,
            "r2": self.r2,
            "max_abs_residual": self.max_abs_residual,
            "free_parameters": self.free_parameters,
            "predictions": {f"{rate:g}": value for rate, value in self.predictions.items()},
        }


def _score(points: dict[float, float], y0: float, m: float, k: float) -> tuple[float, float]:
    sse = 0.0
    worst = 0.0
    for rate, observed in points.items():
        predicted = compound(rate, m, k, y0)
        residual = observed - predicted
        sse += residual * residual
        worst = max(worst, abs(residual))
    return sse, worst


def _r2(points: dict[float, float], sse: float) -> float | None:
    values = list(points.values())
    if len(values) < 2:
        return None
    mean = sum(values) / len(values)
    total = sum((value - mean) ** 2 for value in values)
    if total == 0.0:
        return None if sse > 1e-12 else 1.0
    return 1.0 - sse / total


def fit_free(points: dict[float, float], y0: float, *, m_grid: Sequence[float] | None = None, k_grid: Sequence[float] | None = None) -> LawFit:
    """Grid-search the best (m, k) for the compound family."""

    m_values = tuple(m_grid or tuple(x / 2 for x in range(1, 41)))
    k_values = tuple(k_grid or tuple(x / 2 for x in range(1, 17)))
    best: tuple[float, float, float, float] | None = None
    for m in m_values:
        for k in k_values:
            sse, worst = _score(points, y0, m, k)
            if best is None or sse < best[0] - 1e-12:
                best = (sse, m, k, worst)
    assert best is not None
    sse, m, k, worst = best
    return LawFit("compound-free", m, k, y0, sse, _r2(points, sse), worst, 2, {rate: compound(rate, m, k, y0) for rate in points})


def fit_structural(points: dict[float, float], y0: float, *, m: float, k: float, label: str) -> LawFit:
    """Score the law whose exponents are fixed by trace structure (no free parameters)."""

    sse, worst = _score(points, y0, m, k)
    return LawFit(label, m, k, y0, sse, _r2(points, sse), worst, 0, {rate: compound(rate, m, k, y0) for rate in points})


def fit_linear(points: dict[float, float], y0: float) -> LawFit:
    """Least-squares slope through y0 at p=0; reported as a baseline shape."""

    num = sum(rate * (value - y0) for rate, value in points.items())
    den = sum(rate * rate for rate in points)
    slope = num / den if den else 0.0
    sse = sum((value - (y0 + slope * rate)) ** 2 for rate, value in points.items())
    worst = max(abs(value - (y0 + slope * rate)) for rate, value in points.items()) if points else 0.0
    return LawFit("linear", slope, 1.0, y0, sse, _r2(points, sse), worst, 1, {rate: y0 + slope * rate for rate in points})


# --- slopes with cluster bootstrap ------------------------------------------------


def initial_slope(curve: Curve, *, upto: float = 0.1, samples: int = 2000, seed: int = 0) -> dict[str, Any]:
    """Finite-difference slope (y(upto) - y(0)) / upto with a trace-cluster bootstrap CI."""

    rates = curve.rates
    if 0.0 not in rates or upto not in rates:
        return {"slope": None, "ci_low": None, "ci_high": None, "upto": upto}
    trace_ids = sorted(set(curve.clusters[0.0]) & set(curve.clusters[upto]))
    if not trace_ids:
        return {"slope": None, "ci_low": None, "ci_high": None, "upto": upto}

    def estimate(ids: Sequence[str]) -> float:
        low = [value for trace in ids for value in curve.clusters[0.0][trace]]
        high = [value for trace in ids for value in curve.clusters[upto][trace]]
        return (sum(high) / len(high) - sum(low) / len(low)) / upto

    point = estimate(trace_ids)
    generator = random.Random(seed)
    draws = sorted(estimate([trace_ids[generator.randrange(len(trace_ids))] for _ in trace_ids]) for _ in range(samples))
    return {
        "slope": point,
        "ci_low": draws[max(0, math.floor(0.025 * samples))],
        "ci_high": draws[min(samples - 1, math.ceil(0.975 * samples) - 1)],
        "upto": upto,
        "traces": len(trace_ids),
    }


def bootstrap_means(curve: Curve, *, samples: int = 1000, seed: int = 0) -> dict[float, tuple[float | None, float | None]]:
    """95% cluster-bootstrap band for the mean at every rate."""

    result: dict[float, tuple[float | None, float | None]] = {}
    generator = random.Random(seed)
    for rate in curve.rates:
        clusters = [units for units in curve.clusters[rate].values() if units]
        if not clusters:
            result[rate] = (None, None)
            continue
        draws = []
        for _ in range(samples):
            picked = [clusters[generator.randrange(len(clusters))] for _ in clusters]
            values = [value for units in picked for value in units]
            draws.append(sum(values) / len(values))
        draws.sort()
        result[rate] = (draws[max(0, math.floor(0.025 * samples))], draws[min(samples - 1, math.ceil(0.975 * samples) - 1)])
    return result


# --- end-to-end analysis ---------------------------------------------------------


@dataclass(frozen=True)
class LawReport:
    curve: Curve
    y0: float
    means: dict[float, float]
    bands: dict[float, tuple[float | None, float | None]]
    slope: dict[str, Any]
    free: LawFit
    linear: LawFit
    structural: LawFit | None

    def as_dict(self) -> dict[str, Any]:
        return {
            "operator": self.curve.operator,
            "defense": self.curve.defense,
            "metric": self.curve.metric,
            "group": self.curve.group,
            "traces": self.curve.traces(),
            "y0": self.y0,
            "means": {f"{rate:g}": value for rate, value in self.means.items()},
            "bands": {f"{rate:g}": list(band) for rate, band in self.bands.items()},
            "initial_slope": self.slope,
            "fit_free": self.free.as_dict(),
            "fit_linear": self.linear.as_dict(),
            "fit_structural": self.structural.as_dict() if self.structural else None,
        }


StructuralRule = Callable[[Curve], tuple[float, float, str] | None]


def analyze(
    curves: Iterable[Curve],
    *,
    structural: StructuralRule | None = None,
    bootstrap_samples: int = 1000,
) -> list[LawReport]:
    reports: list[LawReport] = []
    for curve in curves:
        means_all = curve.means()
        points = {rate: value for rate, value in means_all.items() if value is not None}
        if 0.0 not in points or len(points) < 3:
            continue
        y0 = points[0.0]
        fit_points = {rate: value for rate, value in points.items() if rate > 0.0}
        free = fit_free(fit_points, y0)
        linear = fit_linear(fit_points, y0)
        structural_fit = None
        if structural is not None:
            prediction = structural(curve)
            if prediction is not None:
                m, k, label = prediction
                structural_fit = fit_structural(fit_points, y0, m=m, k=k, label=label)
        reports.append(
            LawReport(
                curve=curve,
                y0=y0,
                means=points,
                bands=bootstrap_means(curve, samples=bootstrap_samples),
                slope=initial_slope(curve, samples=bootstrap_samples),
                free=free,
                linear=linear,
                structural=structural_fit,
            )
        )
    return reports


def render_markdown(reports: Sequence[LawReport], *, title: str, note: str = "") -> str:
    lines = [f"# {title}", ""]
    if note:
        lines.extend([note, ""])
    lines.append(
        "Each row is one degradation curve (trace-level rate vs provenance error rate p). "
        "`slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. "
        "`free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; "
        "`structural` is the same family with m, k fixed by trace structure (0 free parameters). "
        "R² is computed on the p>0 points; `max|res|` is the largest absolute residual."
    )
    lines.append("")
    lines.append("| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\\|res\\| |")
    lines.append("|---|---|---|---:|---:|---|---|---:|---|---:|---:|")
    for report in reports:
        group = ", ".join(f"{key}={value}" for key, value in report.curve.group.items())
        slope = report.slope
        slope_text = "n/a" if slope.get("slope") is None else f"{slope['slope']:.2f} [{slope['ci_low']:.2f}, {slope['ci_high']:.2f}]"
        structural = report.structural
        structural_text = "-" if structural is None else f"{structural.family} (m={structural.m:g}, k={structural.k:g})"
        structural_r2 = "-" if structural is None or structural.r2 is None else f"{structural.r2:.3f}"
        structural_res = "-" if structural is None else f"{structural.max_abs_residual:.3f}"
        lines.append(
            f"| `{report.curve.operator}` | {report.curve.defense} | {group} | {report.curve.traces()} | {report.y0:.2f} | {slope_text} | "
            f"({report.free.m:g},{report.free.k:g}) {_fmt(report.free.r2)} | {_fmt(report.linear.r2)} | {structural_text} | {structural_r2} | {structural_res} |"
        )
    return "\n".join(lines) + "\n"


def _fmt(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.3f}"


def write_law_report(reports: Sequence[LawReport], output_dir: str | Path, *, name: str, title: str, note: str = "") -> Path:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    (output / f"{name}.json").write_text(json.dumps([report.as_dict() for report in reports], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    target = output / f"{name}.md"
    target.write_text(render_markdown(reports, title=title, note=note), encoding="utf-8")
    return target
