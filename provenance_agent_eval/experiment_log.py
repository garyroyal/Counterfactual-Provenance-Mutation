"""Append-only experiment records with baseline deltas and lessons learned."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


# Positive deltas are improvements only for metrics where higher is better.
METRIC_DIRECTIONS: dict[str, str] = {
    "utility": "higher",
    "task_success": "higher",
    "attack_success": "lower",
    "unauthorized_side_effect": "lower",
    "sensitive_data_leak": "lower",
    "blocked_actions": "context",
    "policy_violations": "lower",
    "executed_actions": "context",
    "attempted_attack_actions": "context",
    "latency_seconds": "lower",
    "model_latency_seconds": "lower",
    "runtime_latency_seconds": "lower",
    "token_cost": "lower",
    "total_tokens": "lower",
    "provenance_precision": "higher",
    "provenance_recall": "higher",
    "source_loss_rate": "lower",
    "forgery_rate": "lower",
    "authorization_soundness": "higher",
    "authorization_completeness": "higher",
    "false_blocking_rate": "lower",
    "model_attack_induction": "lower",
    "model_attack_induction_difference": "context",
    "runtime_attack_success": "lower",
    "runtime_attack_success_difference": "context",
    "model_safe_compliance": "higher",
    "runtime_allowed": "context",
    "actual_side_effect": "context",
    "prompt_tokens": "lower",
    "completion_tokens": "lower",
    "attack_execution_rate": "lower",
    "attack_blocking_rate": "higher",
    "attack_attempted": "context",
    "attack_executed": "lower",
    "attack_blocked": "higher",
    "unsafe_allows": "lower",
    "confidentiality_impact": "lower",
    "integrity_impact": "lower",
    "authority_escalation": "lower",
    "attack_attempted_steps": "context",
    "attack_executed_steps": "lower",
    "attack_blocked_steps": "higher",
    # Partial progress is diagnostically important but is not monotonic:
    # blocking a late unsafe step can legitimately increase it.
    "partial_execution": "context",
    "partial_execution_rate": "context",
    "stale_evidence_acceptance": "lower",
    "argument_drift_events": "context",
    "grant_reuse_count": "lower",
    "concurrent_attempts": "context",
    "cross_process_attempts": "context",
    "paired_observations": "context",
    "bootstrap_ci_low": "context",
    "bootstrap_ci_high": "context",
    "mcnemar_exact_p": "context",
    "successful_grant_replays": "lower",
    "replay_violation": "lower",
    "decision_flip_rate": "context",
    "invariant_rate": "higher",
    "provenance_failure_attribution": "context",
}


@dataclass(frozen=True)
class MetricChange:
    current: float
    baseline: float | None
    delta: float | None
    direction: str
    assessment: str


@dataclass(frozen=True)
class ExperimentRecord:
    record_id: str
    timestamp: str
    experiment: str
    condition: str
    metrics: dict[str, float]
    metric_changes: dict[str, MetricChange]
    baseline_id: str | None = None
    model: str | None = None
    suite: str | None = None
    scenario: str | None = None
    defense: str | None = None
    seed: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    notes: str = ""

    def as_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["metric_changes"] = {key: asdict(value) for key, value in self.metric_changes.items()}
        return data


@dataclass(frozen=True)
class Lesson:
    lesson_id: str
    timestamp: str
    experiment: str
    observation: str
    evidence: tuple[str, ...]
    conclusion: str
    confidence: str
    follow_up: str = ""

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


class ExperimentLogger:
    """Persist experiment facts and generate review-friendly summaries.

    Records are append-only. Markdown files are derived views and can be
    regenerated from JSONL without losing history.
    """

    def __init__(self, output_dir: str | Path, *, auto_write: bool = True) -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.records_path = self.output_dir / "experiments.jsonl"
        self.lessons_path = self.output_dir / "lessons.jsonl"
        self.report_path = self.output_dir / "report.md"
        self.lessons_report_path = self.output_dir / "lessons.md"
        self.auto_write = auto_write
        self._record_counter = self._next_counter(self.records_path, "exp")
        self._lesson_counter = self._next_counter(self.lessons_path, "lesson")

    def record(
        self,
        *,
        experiment: str,
        condition: str,
        metrics: Mapping[str, float | bool | int],
        baseline_id: str | None = None,
        model: str | None = None,
        suite: str | None = None,
        scenario: str | None = None,
        defense: str | None = None,
        seed: int | None = None,
        metadata: Mapping[str, Any] | None = None,
        notes: str = "",
    ) -> ExperimentRecord:
        normalized = {key: _numeric(value) for key, value in metrics.items()}
        baseline = self._find_record(baseline_id) if baseline_id is not None else None
        changes = {
            key: compare_metric(key, value, baseline.metrics.get(key) if baseline is not None else None)
            for key, value in normalized.items()
        }
        record = ExperimentRecord(
            record_id=self._next_id("exp"),
            timestamp=_now(),
            experiment=experiment,
            condition=condition,
            metrics=normalized,
            metric_changes=changes,
            baseline_id=baseline_id,
            model=model,
            suite=suite,
            scenario=scenario,
            defense=defense,
            seed=seed,
            metadata=dict(metadata or {}),
            notes=notes,
        )
        _append_jsonl(self.records_path, record.as_dict())
        if self.auto_write:
            self.write_report()
        return record

    def lesson(
        self,
        *,
        experiment: str,
        observation: str,
        evidence: list[str] | tuple[str, ...],
        conclusion: str,
        confidence: str,
        follow_up: str = "",
    ) -> Lesson:
        if confidence not in {"low", "medium", "high"}:
            raise ValueError("confidence must be one of: low, medium, high")
        lesson = Lesson(
            lesson_id=self._next_id("lesson"),
            timestamp=_now(),
            experiment=experiment,
            observation=observation,
            evidence=tuple(evidence),
            conclusion=conclusion,
            confidence=confidence,
            follow_up=follow_up,
        )
        _append_jsonl(self.lessons_path, lesson.as_dict())
        if self.auto_write:
            self.write_lessons_report()
        return lesson

    def write_report(self) -> Path:
        records = self._read_records()
        lines = [
            "# Experiment Report",
            "",
            f"Generated: {_now()}",
            "",
            "每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。",
            "",
        ]
        if not records:
            lines.append("尚无实验记录。")
        for record in records:
            lines.extend(_record_markdown(record))
        self.report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        from .visualization import write_dashboard

        write_dashboard(self.output_dir)
        return self.report_path

    def write_lessons_report(self) -> Path:
        lessons = [_lesson_from_dict(item) for item in _read_jsonl(self.lessons_path)]
        lines = ["# Lessons Learned", "", "经验记录必须关联实验证据，并明确置信度。", ""]
        if not lessons:
            lines.append("尚无经验记录。")
        for lesson in lessons:
            lines.extend(
                [
                    f"## {lesson.lesson_id} | {lesson.experiment}",
                    f"时间：{lesson.timestamp}",
                    f"置信度：{lesson.confidence}",
                    "",
                    f"**观察**：{lesson.observation}",
                    "",
                    "**证据**：",
                    *[f"- `{item}`" for item in lesson.evidence],
                    "",
                    f"**结论**：{lesson.conclusion}",
                ]
            )
            if lesson.follow_up:
                lines.extend(["", f"**后续**：{lesson.follow_up}"])
            lines.append("")
        self.lessons_report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return self.lessons_report_path

    def _find_record(self, record_id: str) -> ExperimentRecord:
        for item in _read_jsonl(self.records_path):
            if item.get("record_id") == record_id:
                return _record_from_dict(item)
        raise KeyError(f"Baseline record not found: {record_id}")

    def _read_records(self) -> list[ExperimentRecord]:
        return [_record_from_dict(item) for item in _read_jsonl(self.records_path)]

    def _next_id(self, prefix: str) -> str:
        if prefix == "exp":
            value = self._record_counter
            self._record_counter += 1
        else:
            value = self._lesson_counter
            self._lesson_counter += 1
        return f"{prefix}-{value:04d}"

    @staticmethod
    def _next_counter(path: Path, prefix: str) -> int:
        highest = 0
        for item in _read_jsonl(path):
            record_id = str(item.get("record_id", item.get("lesson_id", "")))
            if record_id.startswith(f"{prefix}-"):
                try:
                    highest = max(highest, int(record_id.rsplit("-", 1)[1]))
                except ValueError:
                    continue
        return highest + 1


def compare_metric(name: str, current: float, baseline: float | None) -> MetricChange:
    if baseline is None:
        return MetricChange(current, None, None, "baseline", "baseline")
    delta = current - baseline
    if delta == 0:
        return MetricChange(current, baseline, 0.0, "unchanged", "unchanged")
    direction = "up" if delta > 0 else "down"
    polarity = METRIC_DIRECTIONS.get(name, "context")
    if polarity == "context":
        assessment = "up" if delta > 0 else "down"
    else:
        improved = (delta > 0 and polarity == "higher") or (delta < 0 and polarity == "lower")
        assessment = "improved" if improved else "degraded"
    return MetricChange(current, baseline, delta, direction, assessment)


def _record_markdown(record: ExperimentRecord) -> list[str]:
    lines = [
        f"## {record.record_id} | {record.experiment} | `{record.condition}`",
        f"时间：{record.timestamp}",
    ]
    context = [
        ("model", record.model),
        ("suite", record.suite),
        ("scenario", record.scenario),
        ("defense", record.defense),
        ("baseline", record.baseline_id),
        ("seed", str(record.seed) if record.seed is not None else None),
    ]
    context = [(key, value) for key, value in context if value is not None]
    if context:
        lines.append("条件：" + ", ".join(f"{key}={value}" for key, value in context))
    lines.extend(["", "| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |", "|---|---:|---:|---:|---|---|"])
    for name, change in record.metric_changes.items():
        baseline = "-" if change.baseline is None else _format_number(change.baseline)
        delta = "-" if change.delta is None else _signed(change.delta)
        lines.append(
            f"| `{name}` | {_format_number(change.current)} | {baseline} | {delta} | "
            f"{change.direction} | {change.assessment} |"
        )
    if record.notes:
        lines.extend(["", f"备注：{record.notes}"])
    lines.append("")
    return lines


def _record_from_dict(item: Mapping[str, Any]) -> ExperimentRecord:
    changes = {
        name: MetricChange(**change) for name, change in item.get("metric_changes", {}).items()
    }
    return ExperimentRecord(
        record_id=item["record_id"],
        timestamp=item["timestamp"],
        experiment=item["experiment"],
        condition=item["condition"],
        metrics={name: float(value) for name, value in item["metrics"].items()},
        metric_changes=changes,
        baseline_id=item.get("baseline_id"),
        model=item.get("model"),
        suite=item.get("suite"),
        scenario=item.get("scenario"),
        defense=item.get("defense"),
        seed=item.get("seed"),
        metadata=dict(item.get("metadata", {})),
        notes=item.get("notes", ""),
    )


def _lesson_from_dict(item: Mapping[str, Any]) -> Lesson:
    return Lesson(
        lesson_id=item["lesson_id"],
        timestamp=item["timestamp"],
        experiment=item["experiment"],
        observation=item["observation"],
        evidence=tuple(item["evidence"]),
        conclusion=item["conclusion"],
        confidence=item["confidence"],
        follow_up=item.get("follow_up", ""),
    )


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def _append_jsonl(path: Path, value: Mapping[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")


def _numeric(value: float | bool | int) -> float:
    if isinstance(value, bool):
        return float(value)
    return float(value)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _format_number(value: float) -> str:
    return f"{value:.4f}".rstrip("0").rstrip(".")


def _signed(value: float) -> str:
    return f"{value:+.4f}".rstrip("0").rstrip(".")
