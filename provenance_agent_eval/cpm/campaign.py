"""The CPM law campaign: hypotheses H1-H7 as reproducible experiments.

Each hypothesis maps to one sweep plus one analysis.  The sweeps write the
usual ``cells.jsonl.gz`` / ``curves.json`` / ``experiments.jsonl``; the
analyses fit degradation laws (:mod:`.laws`) and test zero-free-parameter
structural predictions.  ``run_campaign`` orchestrates everything and writes
``campaign_summary.json`` plus per-hypothesis markdown tables.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

from .defenses import DefenseMechanism
from .degradation import run_degradation_sweep
from .execution import ExecutionMechanism, ExecutionOperator, execution_suite, run_execution_sweep
from .laws import ATTACK, FBR, Curve, LawReport, analyze, build_curves, load_cells, write_law_report
from .operators import MutationOperator
from .synthetic import parametric_suite, synthetic_suite
from .trace import AgentTrace, ArgRole, build_oracle_graph, load_traces


LABEL_MECHANISMS = {"label_trusting", "lineage_verifying"}
ANCESTRY_MECHANISMS = {"origin_routing", "whole_call_quarantine"}
PROVENANCE_MECHANISMS = LABEL_MECHANISMS | ANCESTRY_MECHANISMS


# --- structural predictions -------------------------------------------------------


def structural_rule(curve: Curve) -> tuple[float, float, str] | None:
    """Zero-free-parameter law implied by trace structure for a parametric curve.

    Returns (m, k, label) for the compound family or None when the mechanism is
    predicted to be flat (immune or already saturated at baseline).
    """

    group = curve.group
    depth = group.get("depth")
    k = group.get("k")
    if depth is None or k is None:
        return None
    propagate = bool(group.get("propagate", True))
    operator, defense, metric = curve.operator, curve.defense, curve.metric
    if defense == "no_policy":
        return None
    if metric == ATTACK:
        if operator == MutationOperator.MISATTRIBUTE_PARENT.value:
            if defense in ANCESTRY_MECHANISMS:
                extra = 1 if defense == "whole_call_quarantine" else 0
                return (depth, k + extra, "any-hop(d) ^ all-args(k)")
            if defense in LABEL_MECHANISMS:
                return (depth, k, "any-hop(d) ^ all-args(k)") if propagate else (1, k, "sink-only(1) ^ all-args(k)")
        if operator == MutationOperator.FORGE_LABEL.value and defense == "label_trusting":
            return (depth, k, "any-hop(d) ^ all-args(k)") if propagate else (1, k, "sink-only(1) ^ all-args(k)")
        return None
    if metric == FBR:
        if operator == MutationOperator.DROP_LABEL.value and defense in LABEL_MECHANISMS:
            return (depth * k, 1, "any-hop(d*k)") if propagate else (k, 1, "sink-only(k)")
        if operator == MutationOperator.MERGE_TAINT.value:
            if defense == "label_trusting":
                return (depth * k, 1, "any-hop(d*k)") if propagate else (k, 1, "sink-only(k)")
            if defense in {"lineage_verifying", "origin_routing"}:
                # A merged parent anywhere on the chain changes the sink's
                # ancestry.  origin_routing reads ancestry directly; lineage
                # verification blocks because the (unchanged) sink label no
                # longer covers its roots.  The first campaign run predicted
                # sink-only(k) for lineage_verifying and was refuted (R^2 0.37);
                # the corrected rule is recorded in RESULTS.md.
                return (depth * k, 1, "any-hop(d*k) [structural propagation]")
        return None
    return None


def execution_rule(curve: Curve) -> tuple[float, float, str] | None:
    n = curve.group.get("n")
    retries = curve.group.get("retries")
    if n is None or retries is None or curve.metric != ATTACK:
        return None
    if curve.operator == ExecutionOperator.STALE_VERSION.value and curve.defense in {"no_policy", "grant_single_use"}:
        return (n, 1, "any-action(n)")
    if curve.operator == ExecutionOperator.SEMANTIC_REPLAY.value and curve.defense in {"no_policy", "grant_single_use", "grant_revalidated"}:
        return (n * retries, 1, "any-retry-slot(n*r)")
    return None


# --- H1 / H2 / H6: mechanism x operator on the mixed-trust suite -------------------------


def run_h1_h2_h6(root: Path, *, variants: int, seeds: int, rates: Sequence[float], bootstrap: int) -> dict[str, Any]:
    traces = synthetic_suite(variants=variants)
    result: dict[str, Any] = {"traces": len(traces)}
    for propagate in (True, False):
        tag = "propagate" if propagate else "sinkonly"
        sweep_dir = root / f"h1h2h6-synthetic-{tag}"
        run_degradation_sweep(
            sweep_dir,
            traces,
            rates=rates,
            seeds=seeds,
            bootstrap_samples=bootstrap,
            propagate=propagate,
            follow_up="Compare mechanism x operator slopes across the two corruption semantics.",
        )
        cells = load_cells(sweep_dir)
        asr_reports = analyze(build_curves(cells, metric=ATTACK), bootstrap_samples=bootstrap)
        fbr_reports = analyze(build_curves(cells, metric=FBR), bootstrap_samples=bootstrap)
        write_law_report(asr_reports, sweep_dir, name="laws_asr", title=f"H1 mechanism x operator ASR laws ({tag})")
        write_law_report(fbr_reports, sweep_dir, name="laws_fbr", title=f"H2 mechanism x operator FBR laws ({tag})")
        result[tag] = {
            "sweep_dir": str(sweep_dir),
            "h1_asr_slopes": _slope_matrix(asr_reports),
            "h2_fbr_slopes": _slope_matrix(fbr_reports),
            "h1_preserve_flips": _preserve_flips(sweep_dir),
            "h6_quarantine": _quarantine_cost(cells, traces),
        }
    return result


def _slope_matrix(reports: Sequence[LawReport]) -> dict[str, dict[str, Any]]:
    matrix: dict[str, dict[str, Any]] = defaultdict(dict)
    for report in reports:
        if report.curve.group.get("depth") is not None:
            continue
        matrix[report.curve.operator][report.curve.defense] = {
            "y0": report.y0,
            "y_at_0.25": report.means.get(0.25),
            "y_at_1": report.means.get(1.0),
            "slope_0.1": report.slope.get("slope"),
            "slope_ci": [report.slope.get("ci_low"), report.slope.get("ci_high")],
            "free_fit": {"m": report.free.m, "k": report.free.k, "r2": report.free.r2},
            "linear_r2": report.linear.r2,
        }
    return {operator: dict(by_defense) for operator, by_defense in matrix.items()}


def _preserve_flips(sweep_dir: Path) -> dict[str, int]:
    curves = json.loads((sweep_dir / "curves.json").read_text(encoding="utf-8"))
    return {defense: entry["I1_preserve_flips"] for defense, entry in curves["invariants"].items()}


def _quarantine_cost(cells: list[dict[str, Any]], traces: Sequence[AgentTrace]) -> dict[str, Any]:
    """H6: quarantine FBR at p=0 per template vs. the share of mixed-trust legitimate actions."""

    mixed: dict[str, list[float]] = defaultdict(list)
    for trace in traces:
        if trace.metadata.get("attack"):
            continue
        oracle = build_oracle_graph(trace)
        for action in trace.actions:
            spec = trace.tools[action.tool]
            if not spec.risk.requires_authorization:
                continue
            tainted_content = any(
                binding.role is ArgRole.CONTENT
                and any(not (source.trusted and source.authorized) for source in oracle.root_sources(binding.node_id))
                for binding in action.args.values()
            )
            mixed[str(trace.metadata.get("template"))].append(float(tainted_content))
    baseline: dict[str, list[float]] = defaultdict(list)
    per_operator: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for cell in cells:
        if cell["defense"] != "whole_call_quarantine":
            continue
        template = str(cell.get("template"))
        if cell["rate"] == 0.0 and not cell["attack_trace"]:
            safe = [item for item in cell["outcomes"] if item["expected_allowed"]]
            if safe:
                baseline[template].append(float(any(not item["allowed"] for item in safe)))
        if cell["attack_trace"] and cell["rate"] in (0.25, 1.0):
            per_operator[cell["operator"]][f"asr@{cell['rate']:g}"].append(
                float(any(item["side_effect"] and not item["expected_allowed"] for item in cell["outcomes"]))
            )
    return {
        "per_template": {
            template: {
                "mixed_trust_share": _mean(mixed.get(template, [])),
                "quarantine_fbr_at_0": _mean(baseline.get(template, [])),
            }
            for template in sorted(set(mixed) | set(baseline))
        },
        "quarantine_asr": {operator: {key: _mean(values) for key, values in by_rate.items()} for operator, by_rate in per_operator.items()},
    }


# --- H3 / H4: parametric structure laws --------------------------------------------------


def run_h3_h4(root: Path, *, seeds: int, rates: Sequence[float], bootstrap: int, channels: int) -> dict[str, Any]:
    traces = parametric_suite(channels=channels)
    result: dict[str, Any] = {"traces": len(traces)}
    for propagate in (True, False):
        tag = "propagate" if propagate else "sinkonly"
        sweep_dir = root / f"h3h4-parametric-{tag}"
        run_degradation_sweep(
            sweep_dir,
            traces,
            operators=(MutationOperator.DROP_LABEL, MutationOperator.FORGE_LABEL, MutationOperator.MISATTRIBUTE_PARENT, MutationOperator.MERGE_TAINT),
            rates=rates,
            seeds=seeds,
            bootstrap_samples=bootstrap,
            propagate=propagate,
            follow_up="Test any-hop(d) ^ all-args(k) predictions with zero free parameters.",
        )
        cells = load_cells(sweep_dir)
        asr = analyze(build_curves(cells, metric=ATTACK, group_keys=("depth", "k")), structural=structural_rule, bootstrap_samples=bootstrap)
        fbr = analyze(build_curves(cells, metric=FBR, group_keys=("depth", "k")), structural=structural_rule, bootstrap_samples=bootstrap)
        write_law_report(asr, sweep_dir, name="laws_asr", title=f"H3/H4 structural ASR laws ({tag})")
        write_law_report(fbr, sweep_dir, name="laws_fbr", title=f"H3/H4 structural FBR laws ({tag})")
        result[tag] = {
            "sweep_dir": str(sweep_dir),
            "structural_tests": _structural_summary(asr + fbr),
            "h3_k_effect": _k_effect(asr, fbr),
            "h4_depth_effect": _depth_effect(asr, fbr),
        }
    return result


def _structural_summary(reports: Sequence[LawReport]) -> dict[str, Any]:
    tested = [report for report in reports if report.structural is not None]
    by_law: dict[str, list[LawReport]] = defaultdict(list)
    for report in tested:
        by_law[f"{report.curve.metric}|{report.curve.operator}|{report.curve.defense}"].append(report)
    summary = {}
    for key, items in sorted(by_law.items()):
        residuals = [report.structural.max_abs_residual for report in items]
        r2 = [report.structural.r2 for report in items if report.structural.r2 is not None]
        free_better = sum(report.free.sse < report.structural.sse - 1e-9 for report in items)
        summary[key] = {
            "curves": len(items),
            "law": items[0].structural.family,
            "median_r2": _median(r2),
            "min_r2": min(r2) if r2 else None,
            "max_abs_residual": max(residuals),
            "mean_abs_residual": _mean(residuals),
            "linear_median_r2": _median([report.linear.r2 for report in items if report.linear.r2 is not None]),
            "free_fit_improves_sse_in": free_better,
        }
    return summary


def _k_effect(asr: Sequence[LawReport], fbr: Sequence[LawReport]) -> dict[str, Any]:
    """Direction of the k effect at p=0.25: ASR should fall with k (AND), FBR should rise (OR)."""

    out: dict[str, Any] = {}
    for label, reports in (("asr", asr), ("fbr", fbr)):
        table: dict[str, dict[int, list[float]]] = defaultdict(lambda: defaultdict(list))
        for report in reports:
            k = report.curve.group.get("k")
            value = report.means.get(0.25)
            if k is None or value is None or report.y0 in (0.0, 1.0) and report.means.get(1.0) == report.y0:
                continue
            table[f"{report.curve.operator}|{report.curve.defense}"][int(k)].append(value)
        out[label] = {
            key: {str(k): _mean(values) for k, values in sorted(by_k.items())}
            for key, by_k in sorted(table.items())
        }
    return out


def _depth_effect(asr: Sequence[LawReport], fbr: Sequence[LawReport]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for label, reports in (("asr", asr), ("fbr", fbr)):
        table: dict[str, dict[int, list[float]]] = defaultdict(lambda: defaultdict(list))
        for report in reports:
            depth = report.curve.group.get("depth")
            value = report.means.get(0.25)
            if depth is None or value is None or report.y0 in (0.0, 1.0) and report.means.get(1.0) == report.y0:
                continue
            table[f"{report.curve.operator}|{report.curve.defense}"][int(depth)].append(value)
        out[label] = {
            key: {str(depth): _mean(values) for depth, values in sorted(by_depth.items())}
            for key, by_depth in sorted(table.items())
        }
    return out


# --- H5: induction x mechanism factorisation on model traces -----------------------------------


def run_h5(root: Path, model_runs: dict[str, Path], synthetic_sweep: Path, *, seeds: int, rates: Sequence[float], bootstrap: int) -> dict[str, Any]:
    """Re-sweep model traces under the current semantics and test the product-of-marginals prediction.

    ``actual(p)`` = share of injected decisions that end in an unsafe side effect
    (induced AND mechanism failed).  ``predicted(p)`` = pooled induction rate x
    pooled structure-only failure rate, where the failure rate comes from the
    synthetic attack twins with the same template structure (model-independent).
    The residual is the covariance between *which structures the model is
    induced on* and *how p-fragile those structures are*.
    """

    structure = _structure_failure(load_cells(synthetic_sweep))
    result: dict[str, Any] = {}
    for name, run_dir in model_runs.items():
        traces_path = run_dir / "traces.jsonl"
        decisions_path = run_dir / "decisions.jsonl"
        if not traces_path.exists() or not decisions_path.exists():
            continue
        traces = load_traces(traces_path)
        decisions = [json.loads(line) for line in decisions_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        injected = [item for item in decisions if item.get("injected")]
        induced_traces = tuple(trace for trace in traces if trace.metadata.get("attacker_induced"))
        by_template_n: dict[str, int] = defaultdict(int)
        by_template_ind: dict[str, int] = defaultdict(int)
        for item in injected:
            by_template_n[item["template"]] += 1
            by_template_ind[item["template"]] += int(bool(item.get("induced")))
        induction = sum(by_template_ind.values()) / len(injected) if injected else 0.0
        entry: dict[str, Any] = {
            "injected_decisions": len(injected),
            "induced_decisions": sum(by_template_ind.values()),
            "induction_rate": induction,
            "per_template_induction": {template: by_template_ind[template] / by_template_n[template] for template in sorted(by_template_n)},
            "operators": {},
        }
        sweep_dir = root / f"h5-model-{name}"
        if induced_traces:
            run_degradation_sweep(
                sweep_dir,
                induced_traces,
                operators=(MutationOperator.FORGE_LABEL, MutationOperator.MISATTRIBUTE_PARENT),
                rates=rates,
                seeds=seeds,
                bootstrap_samples=bootstrap,
                propagate=True,
                follow_up="Compare against induction x structure-only failure.",
            )
            model_cells = load_cells(sweep_dir)
            for operator in ("forge_label", "misattribute_parent"):
                for defense in sorted(PROVENANCE_MECHANISMS):
                    rows = []
                    for rate in rates:
                        actual_hits = defaultdict(list)
                        for cell in model_cells:
                            if cell["operator"] != operator or cell["defense"] != defense or cell["rate"] != rate:
                                continue
                            actual_hits[cell["trace_id"]].append(float(any(o["side_effect"] and not o["expected_allowed"] for o in cell["outcomes"])))
                        induced_fail = _mean([_mean(values) for values in actual_hits.values()]) if actual_hits else 0.0
                        actual = induction * induced_fail
                        # structure-only failure pooled over the injected decisions' templates
                        pooled = _mean([
                            structure.get((operator, defense, template, rate), 0.0)
                            for template, count in by_template_n.items()
                            for _ in range(count)
                        ])
                        predicted = induction * pooled
                        rows.append({
                            "rate": rate,
                            "actual_runtime_attack_success": actual,
                            "predicted_product_of_marginals": predicted,
                            "residual": actual - predicted,
                            "mechanism_failure_on_induced": induced_fail,
                            "structure_only_failure_pooled": pooled,
                        })
                    entry["operators"][f"{operator}|{defense}"] = rows
        result[name] = entry
    (root / "h5_factorization.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def _structure_failure(cells: list[dict[str, Any]]) -> dict[tuple[str, str, str, float], float]:
    buckets: dict[tuple[str, str, str, float], list[float]] = defaultdict(list)
    for cell in cells:
        if not cell["attack_trace"]:
            continue
        # model traces only use template variants 0 and 1
        if "|v0|" not in cell["trace_id"] and "|v1|" not in cell["trace_id"]:
            continue
        key = (cell["operator"], cell["defense"], str(cell.get("template")), float(cell["rate"]))
        buckets[key].append(float(any(o["side_effect"] and not o["expected_allowed"] for o in cell["outcomes"])))
    return {key: _mean(values) for key, values in buckets.items()}


# --- H7: execution closure ----------------------------------------------------------------


def run_h7(root: Path, *, seeds: int, rates: Sequence[float], bootstrap: int, copies: int) -> dict[str, Any]:
    sweep_dir = root / "h7-execution"
    scenarios = execution_suite(copies=copies)
    run_execution_sweep(sweep_dir, scenarios, rates=rates, seeds=seeds, bootstrap_samples=bootstrap)
    cells = load_cells(sweep_dir)
    reports = analyze(build_curves(cells, metric=ATTACK, group_keys=("n", "retries")), structural=execution_rule, bootstrap_samples=bootstrap)
    write_law_report(reports, sweep_dir, name="laws_asr", title="H7 execution-closure laws")
    curves = json.loads((sweep_dir / "curves.json").read_text(encoding="utf-8"))
    return {
        "sweep_dir": str(sweep_dir),
        "scenarios": len(scenarios),
        "structural_tests": _structural_summary(reports),
        "invariants": curves["invariants"],
        "asr_at_1": {
            operator: {defense: series[-1]["attack_success"]["rate"] for defense, series in by_defense.items()}
            for operator, by_defense in curves["curves"].items()
        },
        "drift_blocked_at_1": {
            defense: series[-1].get("drifted_actions_blocked") for defense, series in curves["curves"]["stale_version"].items()
        },
    }


# --- orchestration --------------------------------------------------------------------------


def run_campaign(
    root: str | Path,
    *,
    model_runs: dict[str, str | Path] | None = None,
    variants: int = 8,
    seeds: int = 5,
    rates: Sequence[float] = (0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0),
    bootstrap: int = 1000,
    channels: int = 4,
    execution_copies: int = 4,
    hypotheses: Iterable[str] = ("h1", "h3", "h5", "h7"),
) -> dict[str, Any]:
    root_path = Path(root)
    root_path.mkdir(parents=True, exist_ok=True)
    selected = set(hypotheses)
    summary_path = root_path / "campaign_summary.json"
    summary: dict[str, Any] = {"root": str(root_path), "rates": list(rates), "seeds": seeds}
    if summary_path.exists():
        # Re-running a subset of hypotheses must not discard the others.
        summary = {**json.loads(summary_path.read_text(encoding="utf-8")), **summary}
    if "h1" in selected:
        summary["h1_h2_h6"] = run_h1_h2_h6(root_path, variants=variants, seeds=seeds, rates=rates, bootstrap=bootstrap)
    if "h3" in selected:
        summary["h3_h4"] = run_h3_h4(root_path, seeds=seeds, rates=rates, bootstrap=bootstrap, channels=channels)
    if "h5" in selected and model_runs:
        synthetic_sweep = root_path / "h1h2h6-synthetic-propagate"
        if not (synthetic_sweep / "cells.jsonl.gz").exists():
            run_degradation_sweep(synthetic_sweep, synthetic_suite(variants=variants), rates=rates, seeds=seeds, bootstrap_samples=bootstrap)
        summary["h5"] = run_h5(root_path, {name: Path(path) for name, path in model_runs.items()}, synthetic_sweep, seeds=seeds, rates=rates, bootstrap=bootstrap)
    if "h7" in selected:
        summary["h7"] = run_h7(root_path, seeds=seeds, rates=rates, bootstrap=bootstrap, copies=execution_copies)
    (root_path / "campaign_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def _mean(values: Iterable[float]) -> float | None:
    items = [float(value) for value in values]
    return sum(items) / len(items) if items else None


def _median(values: Sequence[float]) -> float | None:
    items = sorted(values)
    if not items:
        return None
    middle = len(items) // 2
    return items[middle] if len(items) % 2 else (items[middle - 1] + items[middle]) / 2
