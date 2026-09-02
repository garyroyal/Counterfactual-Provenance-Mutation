"""Standard-library SVG rendering of CPM degradation curves.

One panel per (operator, metric); one line per mechanism with a shaded
cluster-bootstrap band.  Output is plain SVG so figures can be regenerated
from ``curves.json`` without a plotting dependency.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PALETTE = {
    "no_policy": "#9e9e9e",
    "label_trusting": "#d62728",
    "lineage_verifying": "#ff7f0e",
    "origin_routing": "#1f77b4",
    "whole_call_quarantine": "#2ca02c",
    "grant_single_use": "#d62728",
    "grant_revalidated": "#ff7f0e",
    "intent_ledger": "#1f77b4",
}

METRICS = (("attack_success", "Attack success (ASR)"), ("false_blocking", "False blocking (FBR)"))


def render_curves_svg(summary: dict[str, Any], *, panel_width: int = 300, panel_height: int = 210) -> str:
    operators = list(summary["curves"])
    rows = len(operators)
    cols = len(METRICS)
    margin_left, margin_top = 60, 40
    width = margin_left + cols * (panel_width + 30) + 170
    height = margin_top + rows * (panel_height + 40)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" font-family="Helvetica, Arial, sans-serif" font-size="11">',
        '<rect width="100%" height="100%" fill="white"/>',
    ]
    for row, operator in enumerate(operators):
        for col, (metric, title) in enumerate(METRICS):
            x0 = margin_left + col * (panel_width + 30)
            y0 = margin_top + row * (panel_height + 40)
            parts.append(_panel(summary["curves"][operator], metric, f"{operator} — {title}", x0, y0, panel_width, panel_height))
    legend_x = margin_left + cols * (panel_width + 30) + 10
    legend_y = margin_top
    for index, (mechanism, colour) in enumerate(PALETTE.items()):
        if any(mechanism in by_defense for by_defense in summary["curves"].values()):
            y = legend_y + index * 18
            parts.append(f'<line x1="{legend_x}" y1="{y}" x2="{legend_x + 24}" y2="{y}" stroke="{colour}" stroke-width="2.5"/>')
            parts.append(f'<text x="{legend_x + 30}" y="{y + 4}">{mechanism}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def _panel(by_defense: dict[str, list[dict[str, Any]]], metric: str, title: str, x0: int, y0: int, width: int, height: int) -> str:
    plot_left, plot_top = x0 + 40, y0 + 20
    plot_width, plot_height = width - 50, height - 50

    def sx(rate: float) -> float:
        return plot_left + rate * plot_width

    def sy(value: float) -> float:
        return plot_top + (1.0 - value) * plot_height

    parts = [f'<text x="{x0 + width / 2}" y="{y0 + 10}" text-anchor="middle" font-weight="bold">{title}</text>']
    parts.append(f'<rect x="{plot_left}" y="{plot_top}" width="{plot_width}" height="{plot_height}" fill="none" stroke="#444"/>')
    for tick in (0.0, 0.25, 0.5, 0.75, 1.0):
        parts.append(f'<line x1="{plot_left}" y1="{sy(tick):.1f}" x2="{plot_left + plot_width}" y2="{sy(tick):.1f}" stroke="#eee"/>')
        parts.append(f'<text x="{plot_left - 6}" y="{sy(tick) + 4:.1f}" text-anchor="end">{tick:g}</text>')
        parts.append(f'<text x="{sx(tick):.1f}" y="{plot_top + plot_height + 14}" text-anchor="middle">{tick:g}</text>')
    parts.append(f'<text x="{plot_left + plot_width / 2}" y="{plot_top + plot_height + 28}" text-anchor="middle">provenance error rate p</text>')
    for mechanism, series in by_defense.items():
        colour = PALETTE.get(mechanism, "#000")
        points = [(item["rate"], item[metric]) for item in series if item[metric]["rate"] is not None]
        if not points:
            continue
        band_upper = [(rate, est.get("cluster_ci_high")) for rate, est in points if est.get("cluster_ci_high") is not None]
        band_lower = [(rate, est.get("cluster_ci_low")) for rate, est in points if est.get("cluster_ci_low") is not None]
        if band_upper and band_lower and len(band_upper) == len(band_lower):
            path = " ".join(f"{sx(r):.1f},{sy(v):.1f}" for r, v in band_upper) + " " + " ".join(
                f"{sx(r):.1f},{sy(v):.1f}" for r, v in reversed(band_lower)
            )
            parts.append(f'<polygon points="{path}" fill="{colour}" fill-opacity="0.12" stroke="none"/>')
        line = " ".join(f"{sx(rate):.1f},{sy(est['rate']):.1f}" for rate, est in points)
        parts.append(f'<polyline points="{line}" fill="none" stroke="{colour}" stroke-width="2.2"/>')
        for rate, est in points:
            parts.append(f'<circle cx="{sx(rate):.1f}" cy="{sy(est["rate"]):.1f}" r="2.8" fill="{colour}"/>')
    return "\n".join(parts)


DEPTH_PALETTE = ("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f")


def render_law_overlay_svg(
    reports: list[dict[str, Any]],
    *,
    title: str,
    series_key: str,
    panel_width: int = 360,
    panel_height: int = 260,
) -> str:
    """Observed means (dots + bootstrap bands) against the structural law (dashed).

    ``reports`` are ``LawReport.as_dict()`` entries sharing operator, defense
    and metric; ``series_key`` (e.g. ``"depth"`` or ``"k"``) picks the group
    field that distinguishes the lines.
    """

    margin_left, margin_top = 60, 40
    width = margin_left + panel_width + 420
    height = margin_top + panel_height + 40
    plot_left, plot_top = margin_left, margin_top + 10
    plot_width, plot_height = panel_width - 20, panel_height - 50

    def sx(rate: float) -> float:
        return plot_left + rate * plot_width

    def sy(value: float) -> float:
        return plot_top + (1.0 - value) * plot_height

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" font-family="Helvetica, Arial, sans-serif" font-size="11">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{margin_left + panel_width / 2}" y="{margin_top - 12}" text-anchor="middle" font-weight="bold">{title}</text>',
        f'<rect x="{plot_left}" y="{plot_top}" width="{plot_width}" height="{plot_height}" fill="none" stroke="#444"/>',
    ]
    for tick in (0.0, 0.25, 0.5, 0.75, 1.0):
        parts.append(f'<line x1="{plot_left}" y1="{sy(tick):.1f}" x2="{plot_left + plot_width}" y2="{sy(tick):.1f}" stroke="#eee"/>')
        parts.append(f'<text x="{plot_left - 6}" y="{sy(tick) + 4:.1f}" text-anchor="end">{tick:g}</text>')
        parts.append(f'<text x="{sx(tick):.1f}" y="{plot_top + plot_height + 14}" text-anchor="middle">{tick:g}</text>')
    parts.append(f'<text x="{plot_left + plot_width / 2}" y="{plot_top + plot_height + 28}" text-anchor="middle">provenance error rate p</text>')
    legend_x = plot_left + plot_width + 20
    ordered = sorted(reports, key=lambda item: item["group"].get(series_key, 0))
    for index, report in enumerate(ordered):
        colour = DEPTH_PALETTE[index % len(DEPTH_PALETTE)]
        means = {float(rate): value for rate, value in report["means"].items()}
        bands = {float(rate): value for rate, value in report["bands"].items()}
        rates = sorted(means)
        upper = [(rate, bands[rate][1]) for rate in rates if bands.get(rate) and bands[rate][1] is not None]
        lower = [(rate, bands[rate][0]) for rate in rates if bands.get(rate) and bands[rate][0] is not None]
        if upper and lower and len(upper) == len(lower):
            path = " ".join(f"{sx(r):.1f},{sy(v):.1f}" for r, v in upper) + " " + " ".join(f"{sx(r):.1f},{sy(v):.1f}" for r, v in reversed(lower))
            parts.append(f'<polygon points="{path}" fill="{colour}" fill-opacity="0.10" stroke="none"/>')
        for rate in rates:
            parts.append(f'<circle cx="{sx(rate):.1f}" cy="{sy(means[rate]):.1f}" r="3" fill="{colour}"/>')
        structural = report.get("fit_structural")
        if structural:
            y0 = report["y0"]
            m, k = structural["m"], structural["k"]
            samples = [i / 100 for i in range(0, 101)]
            line = " ".join(f"{sx(p):.1f},{sy(y0 + (1 - y0) * (1 - (1 - p) ** m) ** k):.1f}" for p in samples)
            parts.append(f'<polyline points="{line}" fill="none" stroke="{colour}" stroke-width="1.8" stroke-dasharray="5,3"/>')
            label = f"{series_key}={report['group'].get(series_key)} · law m={m:g},k={k:g} · R²={_fmt_r2(structural.get('r2'))}"
        else:
            label = f"{series_key}={report['group'].get(series_key)}"
        y = margin_top + 10 + index * 18
        parts.append(f'<line x1="{legend_x}" y1="{y}" x2="{legend_x + 22}" y2="{y}" stroke="{colour}" stroke-width="2.5"/>')
        parts.append(f'<text x="{legend_x + 28}" y="{y + 4}">{label}</text>')
    parts.append(f'<text x="{legend_x}" y="{margin_top + 10 + len(ordered) * 18 + 8}" fill="#555">dots: observed (band = 95% cluster bootstrap); dashed: zero-parameter law</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def _fmt_r2(value: Any) -> str:
    return "n/a" if value is None else f"{value:.2f}"


def write_law_overlay_svg(
    law_report_json: str | Path,
    target: str | Path,
    *,
    operator: str,
    defense: str,
    series_key: str,
    fixed: dict[str, Any] | None = None,
    title: str | None = None,
) -> Path:
    reports = json.loads(Path(law_report_json).read_text(encoding="utf-8"))
    selected = [
        item
        for item in reports
        if item["operator"] == operator
        and item["defense"] == defense
        and all(item["group"].get(key) == value for key, value in (fixed or {}).items())
    ]
    svg = render_law_overlay_svg(selected, title=title or f"{operator} / {defense}", series_key=series_key)
    Path(target).write_text(svg, encoding="utf-8")
    return Path(target)


def write_curves_svg(sweep_dir: str | Path) -> Path:
    directory = Path(sweep_dir)
    summary = json.loads((directory / "curves.json").read_text(encoding="utf-8"))
    target = directory / "curves.svg"
    target.write_text(render_curves_svg(summary), encoding="utf-8")
    return target


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sweep_dir")
    args = parser.parse_args()
    print(write_curves_svg(args.sweep_dir))
