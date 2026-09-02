"""Generate a compact visual progress report from experiment JSONL records."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any


def write_dashboard(input_dir: str | Path, output_path: str | Path | None = None) -> Path:
    """Write an HTML fragment derived from ``experiments.jsonl``."""

    directory = Path(input_dir)
    destination = Path(output_path) if output_path is not None else directory / "progress.html"
    records_path = directory / "experiments.jsonl"
    records = _read_records(records_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_dashboard(records), encoding="utf-8")
    return destination


def render_dashboard(records: list[dict[str, Any]]) -> str:
    aggregates = [record for record in records if str(record.get("condition", "")).endswith("-aggregate")]
    raw = [record for record in records if not str(record.get("condition", "")).endswith("-aggregate")]
    if not aggregates:
        aggregates = raw[-12:]
    model_view = any(record.get("experiment") == "model-action-induction" for record in records)
    attack_view = any(record.get("experiment") == "generalized-attack-matrix" for record in records)
    composed_view = any(record.get("experiment") == "composed-attack-matrix" for record in records)
    concurrency_view = any(record.get("experiment") == "concurrent-grant-matrix" for record in records)
    cross_process_view = any(record.get("experiment") == "cross-process-grant-matrix" for record in records)
    redis_view = any(record.get("experiment") == "redis-cross-process-grant-matrix" for record in records)
    model_comparison_view = any(record.get("experiment") == "cross-model-action-induction" for record in records)
    factorial_analysis_view = any(record.get("experiment") == "factorial-presentation-analysis" for record in records)
    real_tool_view = any(record.get("experiment") == "real-tool-e2e" for record in records)
    mutation_view = any(record.get("experiment") == "provenance-mutation-replay" for record in records)
    model_mutation_view = any(record.get("experiment") in {"model-provenance-mutation-e2e", "model-provenance-mutation-analysis"} for record in records)
    transform_aggregates = [
        record for record in aggregates if str(record.get("scenario", "")).startswith("transform:")
    ]
    stage_aggregates = [
        record for record in aggregates if str(record.get("scenario", "")).startswith("stage:")
    ]
    if model_mutation_view:
        chart_aggregates = [record for record in aggregates if str(record.get("scenario", "")).startswith("model-provenance-mutation") or str(record.get("scenario", "")).startswith("evidence:")] or aggregates
    elif mutation_view:
        chart_aggregates = [record for record in aggregates if record.get("scenario") == "all-mutations"] or aggregates
    elif factorial_analysis_view:
        chart_aggregates = [
            record for record in aggregates if str(record.get("scenario", "")).startswith("presentation:")
        ] or aggregates
    elif model_comparison_view:
        chart_aggregates = [
            record for record in aggregates if record.get("scenario") == "paired-common-cases"
        ] or aggregates
    elif redis_view:
        chart_aggregates = [
            record for record in aggregates if record.get("scenario") == "all-redis-cross-process-grant-attacks"
        ] or aggregates
    elif cross_process_view:
        chart_aggregates = [
            record for record in aggregates if record.get("scenario") == "all-cross-process-grant-attacks"
        ] or aggregates
    elif concurrency_view:
        chart_aggregates = [
            record for record in aggregates if record.get("scenario") == "all-concurrent-grant-attacks"
        ] or aggregates
    elif composed_view:
        chart_aggregates = [
            record for record in aggregates if record.get("scenario") == "all-composed-attacks"
        ] or aggregates
    elif model_view and transform_aggregates:
        chart_aggregates = transform_aggregates
    elif attack_view and stage_aggregates:
        chart_aggregates = stage_aggregates
    else:
        chart_aggregates = aggregates
    title = (
        "Model-fixed provenance mutation and side effects"
        if model_mutation_view
        else "Counterfactual provenance mutation replay"
        if mutation_view
        else "Real tool adapter end-to-end outcomes"
        if real_tool_view
        else "Orthogonal presentation and runtime policy analysis"
        if factorial_analysis_view
        else "Paired cross-model action induction"
        if model_comparison_view
        else "Redis cross-process grant consumption and replay"
        if redis_view
        else "Cross-process grant consumption and replay"
        if cross_process_view
        else "Concurrent grant consumption and replay"
        if concurrency_view
        else "Composed attack traces and outcomes"
        if composed_view
        else "Generalized attack coverage and outcomes"
        if attack_view
        else "Model induction and runtime outcomes"
        if model_view
        else "Provenance experiment progress"
    )
    return "\n".join(
        [
            '<div id="provenance-progress">',
            "<style>",
            "#provenance-progress{box-sizing:border-box;width:100%;font:14px system-ui,sans-serif;color:#18212b;max-width:980px;margin:0 auto;padding:18px;background:#f7f8fa;overflow-x:auto}"
            "#provenance-progress h2{font-size:20px;margin:0 0 4px}#provenance-progress p{margin:4px 0 14px;color:#52606d}"
            "#provenance-progress svg{width:100%;height:auto;display:block;background:#fff;border:1px solid #d9dee5}"
            "#provenance-progress table{width:100%;table-layout:fixed;border-collapse:collapse;background:#fff;margin-top:12px}"
            "#provenance-progress th,#provenance-progress td{padding:7px 8px;border-bottom:1px solid #e5e8ec;text-align:left;font-size:12px;overflow-wrap:anywhere}"
            "#provenance-progress th{color:#52606d;font-weight:600}#provenance-progress .bad{color:#b42318;font-weight:650}"
            "#provenance-progress .good{color:#067647;font-weight:650}#provenance-progress .muted{color:#667085}",
            "</style>",
            f"<h2>{title}</h2>",
            f"<p>{len(records)} logged records; {len(raw)} raw runs and {len(aggregates)} aggregate views.</p>",
            '<svg viewBox="0 0 960 390" role="img" aria-label="Aggregate security and utility metrics">',
            _aggregate_chart(chart_aggregates, model_view=(model_view or model_comparison_view or factorial_analysis_view), attack_view=attack_view, composed_view=composed_view, concurrency_view=concurrency_view, cross_process_view=(cross_process_view or redis_view), model_comparison_view=(model_comparison_view or factorial_analysis_view), real_tool_view=real_tool_view, mutation_view=(mutation_view or model_mutation_view), model_mutation_view=model_mutation_view),
            "</svg>",
            '<svg viewBox="0 0 960 250" role="img" aria-label="Metric changes over experiment records">',
            _timeline_chart(raw, model_view=(model_view or model_comparison_view or factorial_analysis_view), attack_view=attack_view, composed_view=composed_view, concurrency_view=concurrency_view, cross_process_view=(cross_process_view or redis_view), model_comparison_view=(model_comparison_view or factorial_analysis_view), real_tool_view=real_tool_view, mutation_view=(mutation_view or model_mutation_view), model_mutation_view=model_mutation_view),
            "</svg>",
            _issues_table(records),
            "</div>",
        ]
    )


def _aggregate_chart(
    records: list[dict[str, Any]], *, model_view: bool = False, attack_view: bool = False, composed_view: bool = False, concurrency_view: bool = False, cross_process_view: bool = False, model_comparison_view: bool = False, real_tool_view: bool = False, mutation_view: bool = False, model_mutation_view: bool = False
) -> str:
    if not records:
        return '<text x="480" y="190" text-anchor="middle" fill="#52606d">No experiment records yet</text>'
    width, height = 960, 390
    left, right, top, bottom = 190, 25, 32, 54
    plot_w, plot_h = width - left - right, height - top - bottom
    metrics = (
        ("runtime_attack_success", "#b42318"),
        ("actual_side_effect", "#d92d20"),
        ("false_blocking_rate", "#d97706"),
        ("utility", "#067647"),
    ) if model_mutation_view else (
        ("decision_flip_rate", "#b42318"),
        ("invariant_rate", "#067647"),
        ("provenance_failure_attribution", "#175cd3"),
    ) if mutation_view else (
        ("utility", "#067647"),
        ("runtime_attack_success", "#b42318"),
        ("actual_side_effect", "#d92d20"),
        ("false_blocking_rate", "#d97706"),
    ) if real_tool_view else (
        ("model_attack_induction", "#b42318"),
    ) if model_comparison_view else (
        ("attack_execution_rate", "#b42318"),
        ("attack_blocking_rate", "#067647"),
        ("successful_grant_replays", "#d92d20"),
        ("authorization_soundness", "#175cd3"),
    ) if cross_process_view else (
        ("attack_execution_rate", "#b42318"),
        ("attack_blocking_rate", "#067647"),
        ("successful_grant_replays", "#d92d20"),
        ("authorization_soundness", "#175cd3"),
    ) if concurrency_view else (
        ("attack_execution_rate", "#b42318"),
        ("attack_blocking_rate", "#067647"),
        ("partial_execution_rate", "#d97706"),
        ("stale_evidence_acceptance", "#175cd3"),
    ) if composed_view else (
        ("attack_execution_rate", "#b42318"),
        ("attack_blocking_rate", "#067647"),
        ("authorization_soundness", "#175cd3"),
    ) if attack_view else (
        ("utility", "#067647"),
        ("model_attack_induction", "#b42318"),
        ("runtime_attack_success", "#d92d20"),
        ("runtime_allowed", "#175cd3"),
    ) if model_view else (
        ("utility", "#067647"),
        ("attack_success", "#b42318"),
        ("sensitive_data_leak", "#d92d20"),
        ("blocked_actions", "#175cd3"),
    )
    slot = plot_w / len(records)
    bars = []
    labels = []
    for index, record in enumerate(records):
        x0 = left + index * slot + slot * 0.08
        bar_w = slot * 0.84 / len(metrics)
        scenario = _short_label(str(record.get("scenario") or "overall"))
        condition = _short_label(str(record.get("condition", "")).replace("-aggregate", "").split("|", 1)[0])
        labels.append(
        f'<text x="{x0 + slot * 0.42:.1f}" y="{height - 24}" text-anchor="middle" font-size="10" fill="#52606d">'
            f"{html.escape(scenario)}<tspan x=\"{x0 + slot * 0.42:.1f}\" dy=\"13\">{html.escape(condition)}</tspan></text>"
        )
        metrics_data = record.get("metrics", {})
        for metric_index, (metric, color) in enumerate(metrics):
            value = max(0.0, min(1.0, float(metrics_data.get(metric, 0.0))))
            x = x0 + metric_index * bar_w
            bar_h = value * plot_h
            y = top + plot_h - bar_h
            bars.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(2, bar_w - 2):.1f}" height="{bar_h:.1f}" fill="{color}">'
                f'<title>{html.escape(metric)}: {value:.3f}</title></rect>'
            )
    grid = []
    for tick in (0, 0.25, 0.5, 0.75, 1.0):
        y = top + plot_h * (1 - tick)
        grid.append(f'<line x1="{left}" x2="{width - right}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e5e8ec"/>')
        grid.append(f'<text x="{left - 10}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="#52606d">{tick:g}</text>')
    legend = []
    for index, (metric, color) in enumerate(metrics):
        x = left + index * 170
        legend.append(f'<rect x="{x}" y="10" width="11" height="11" fill="{color}"/><text x="{x + 16}" y="20" font-size="11" fill="#52606d">{html.escape(_metric_label(metric) if (composed_view or concurrency_view or cross_process_view or mutation_view) else metric)}</text>')
    return "".join(grid + bars + labels + legend + [f'<text x="{left}" y="{height - 5}" font-size="11" fill="#52606d">scenario / condition</text>', f'<text x="16" y="{top + plot_h / 2:.1f}" transform="rotate(-90 16 {top + plot_h / 2:.1f})" font-size="11" fill="#52606d">rate</text>'])


def _timeline_chart(
    records: list[dict[str, Any]], *, model_view: bool = False, attack_view: bool = False, composed_view: bool = False, concurrency_view: bool = False, cross_process_view: bool = False, model_comparison_view: bool = False, real_tool_view: bool = False, mutation_view: bool = False, model_mutation_view: bool = False
) -> str:
    if not records:
        return '<text x="480" y="125" text-anchor="middle" fill="#52606d">No raw runs yet</text>'
    width, height = 960, 250
    left, right, top, bottom = 52, 24, 28, 38
    plot_w, plot_h = width - left - right, height - top - bottom
    if model_mutation_view:
        metrics = (("runtime_attack_success", "#b42318"), ("actual_side_effect", "#d92d20"), ("utility", "#067647"))
    elif mutation_view:
        metrics = (("decision_flip", "#b42318"), ("invariant_holds", "#067647"))
    elif real_tool_view:
        metrics = (
            ("runtime_attack_success", "#b42318"),
            ("actual_side_effect", "#d92d20"),
            ("runtime_allowed", "#175cd3"),
            ("utility", "#067647"),
        )
    elif model_comparison_view:
        metrics = (("model_attack_induction_difference", "#b42318"),)
    elif cross_process_view or concurrency_view:
        metrics = (
            ("attack_execution_rate", "#b42318"),
            ("attack_blocking_rate", "#067647"),
            ("successful_grant_replays", "#d92d20"),
            ("authorization_soundness", "#175cd3"),
        )
    elif composed_view:
        metrics = (
            ("attack_execution_rate", "#b42318"),
            ("attack_blocking_rate", "#067647"),
            ("partial_execution", "#d97706"),
            ("stale_evidence_acceptance", "#175cd3"),
        )
    elif attack_view:
        metrics = (
            ("attack_executed", "#b42318"),
            ("attack_blocked", "#067647"),
            ("authorization_soundness", "#175cd3"),
        )
    elif model_view:
        metrics = (
            ("model_attack_induction", "#b42318"),
            ("runtime_attack_success", "#d92d20"),
            ("runtime_allowed", "#175cd3"),
            ("utility", "#067647"),
        )
    else:
        metrics = (
            ("attack_success", "#b42318"),
            ("sensitive_data_leak", "#d92d20"),
            ("blocked_actions", "#175cd3"),
            ("utility", "#067647"),
        )
    paths = []
    for metric, color in metrics:
        points = []
        for index, record in enumerate(records):
            x = left + (plot_w * index / max(1, len(records) - 1))
            value = max(0.0, min(1.0, float(record.get("metrics", {}).get(metric, 0.0))))
            y = top + plot_h * (1 - value)
            points.append(f"{x:.1f},{y:.1f}")
        paths.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="2"/>')
        paths.extend(f'<circle cx="{point.split(",")[0]}" cy="{point.split(",")[1]}" r="3" fill="{color}"/>' for point in points)
    grid = []
    for tick in (0, 0.5, 1.0):
        y = top + plot_h * (1 - tick)
        grid.extend([f'<line x1="{left}" x2="{width - right}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e5e8ec"/>', f'<text x="{left - 9}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="#52606d">{tick:g}</text>'])
    legend = [f'<text x="{left + index * 180}" y="18" font-size="11" fill="{color}">{html.escape(_metric_label(metric) if (composed_view or concurrency_view or cross_process_view or real_tool_view or mutation_view) else metric)}</text>' for index, (metric, color) in enumerate(metrics)]
    return "".join(grid + paths + legend + [f'<text x="{left}" y="{height - 8}" font-size="11" fill="#52606d">raw record order</text>', f'<text x="16" y="{top + plot_h / 2:.1f}" transform="rotate(-90 16 {top + plot_h / 2:.1f})" font-size="11" fill="#52606d">rate</text>'])


def _issues_table(records: list[dict[str, Any]]) -> str:
    issues = []
    for record in records:
        metrics = record.get("metrics", {})
        if float(metrics.get("attack_executed", 0)):
            issues.append((record, "generalized attack reached execution"))
        elif float(metrics.get("stale_evidence_acceptance", 0)):
            issues.append((record, "stale evidence accepted after argument drift"))
        elif float(metrics.get("partial_execution", 0)) or float(metrics.get("partial_execution_rate", 0)):
            issues.append((record, "composed attack partially executed"))
        elif float(metrics.get("runtime_attack_success", 0)):
            issues.append((record, "model-induced attack reached runtime execution"))
        elif float(metrics.get("model_attack_induction", 0)):
            issues.append((record, "model selected the injected target action"))
        elif float(metrics.get("replay_violation", 0)) or float(metrics.get("successful_grant_replays", 0)):
            issues.append((record, "single-use grant replay executed"))
        elif float(metrics.get("attack_success", 0)) or float(metrics.get("sensitive_data_leak", 0)) or float(metrics.get("policy_violations", 0)):
            issues.append((record, "unsafe action or data leak"))
        elif str(record.get("condition", "")).startswith("source-aware") and float(metrics.get("blocked_actions", 0)):
            issues.append((record, "blocked action: inspect whether expected"))
    rows = []
    for record, issue in issues[-12:]:
        rows.append(
            "<tr>"
            f"<td>{html.escape(str(record.get('record_id', '-')))}</td>"
            f"<td>{html.escape(str(record.get('scenario') or 'overall'))}</td>"
            f"<td>{html.escape(str(record.get('condition', '-')))}</td>"
            f'<td class="{"bad" if "unsafe" in issue else "muted"}">{html.escape(issue)}</td>'
            "</tr>"
        )
    if not rows:
        rows.append('<tr><td colspan="4" class="good">No flagged issues in the current log.</td></tr>')
    return "<table><thead><tr><th>Record</th><th>Scenario</th><th>Condition</th><th>Issue to review</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>"


def _read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def _short_label(value: str) -> str:
    value = value.removeprefix("transform:").removeprefix("stage:").removeprefix("presentation:")
    return {
        "rewrite-forged-user": "forged-user",
        "summary-preserve": "summary",
        "source_aware": "source aware",
        "no_policy": "no policy",
        "persistent_state": "state",
        "authorization": "authorization",
        "model_input": "model input",
        "data_flow": "data flow",
        "multi_agent": "multi-agent",
        "all-composed-attacks": "composed",
        "all-concurrent-grant-attacks": "concurrent grant",
        "all-cross-process-grant-attacks": "cross-process",
        "all-redis-cross-process-grant-attacks": "redis cross-process",
        "grant_aware_revalidated": "revalidated",
        "grant_aware_racey": "racey",
        "grant_aware_atomic": "atomic",
        "redis_atomic": "Redis atomic",
    }.get(value, value)


def _metric_label(metric: str) -> str:
    return {
        "attack_execution_rate": "attack exec",
        "attack_blocking_rate": "attack blocked",
        "partial_execution_rate": "partial trace",
        "partial_execution": "partial trace",
        "stale_evidence_acceptance": "stale evidence",
        "successful_grant_replays": "grant replays",
        "authorization_soundness": "soundness",
        "actual_side_effect": "side effect",
        "runtime_attack_success": "attack exec",
        "false_blocking_rate": "false block",
        "decision_flip_rate": "decision flip",
        "invariant_rate": "invariants",
        "provenance_failure_attribution": "attribution",
        "decision_flip": "decision flip",
        "invariant_holds": "invariant",
    }.get(metric, metric)
