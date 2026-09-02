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
