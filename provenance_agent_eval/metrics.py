"""Metrics for provenance quality and authorization quality."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

from .core import Provenance
from .provenance_graph import ProvenanceGraph
from .runtime import TraceEvent


def _source_id(source: Provenance | str) -> str:
    return source.source_id if isinstance(source, Provenance) else str(source)


@dataclass(frozen=True)
class ProvenanceQuality:
    """Set-based quality of observed provenance against ground truth."""

    expected_count: int
    observed_count: int
    true_positive_count: int
    missing_count: int
    forged_count: int
    precision: float
    recall: float
    source_loss_rate: float
    forgery_rate: float

    def as_dict(self) -> dict[str, float | int]:
        return {
            "expected_count": self.expected_count,
            "observed_count": self.observed_count,
            "true_positive_count": self.true_positive_count,
            "missing_count": self.missing_count,
            "forged_count": self.forged_count,
            "precision": self.precision,
            "recall": self.recall,
            "source_loss_rate": self.source_loss_rate,
            "forgery_rate": self.forgery_rate,
        }


def score_provenance(
    expected: Iterable[Provenance | str], observed: Iterable[Provenance | str]
) -> ProvenanceQuality:
    """Compare source IDs, treating empty-vs-empty as a correct result."""

    expected_ids = {_source_id(source) for source in expected}
    observed_ids = {_source_id(source) for source in observed}
    true_positives = expected_ids & observed_ids
    missing = expected_ids - observed_ids
    forged = observed_ids - expected_ids
    precision = _ratio(len(true_positives), len(observed_ids))
    recall = _ratio(len(true_positives), len(expected_ids))
    return ProvenanceQuality(
        expected_count=len(expected_ids),
        observed_count=len(observed_ids),
        true_positive_count=len(true_positives),
        missing_count=len(missing),
        forged_count=len(forged),
        precision=precision,
        recall=recall,
        source_loss_rate=_ratio(len(missing), len(expected_ids)),
        # No observed annotation means no forged annotation. Keep this
        # distinct from precision's vacuous-correct convention.
        forgery_rate=(len(forged) / len(observed_ids)) if observed_ids else 0.0,
    )


def score_graph_node(graph: ProvenanceGraph, node_id: str) -> ProvenanceQuality:
    """Score attached evidence for one node against graph-derived roots."""

    return score_provenance(graph.root_sources(node_id), graph.node(node_id).attached_sources)


def score_graph_nodes(graph: ProvenanceGraph, node_ids: Iterable[str]) -> ProvenanceQuality:
    """Micro-average source quality across graph nodes."""

    expected: set[str] = set()
    observed: set[str] = set()
    for node_id in node_ids:
        expected.update(source.source_id for source in graph.root_sources(node_id))
        observed.update(source.source_id for source in graph.node(node_id).attached_sources)
    return score_provenance(expected, observed)


@dataclass(frozen=True)
class AuthorizationCase:
    """One authorization decision with an independently known expectation."""

    expected_allowed: bool
    actual_allowed: bool


@dataclass(frozen=True)
class AuthorizationQuality:
    total_count: int
    safe_count: int
    unsafe_count: int
    correctly_allowed: int
    correctly_blocked: int
    false_blocks: int
    unsafe_allows: int
    soundness: float
    completeness: float
    false_blocking_rate: float

    def as_dict(self) -> dict[str, float | int]:
        return {
            "total_count": self.total_count,
            "safe_count": self.safe_count,
            "unsafe_count": self.unsafe_count,
            "correctly_allowed": self.correctly_allowed,
            "correctly_blocked": self.correctly_blocked,
            "false_blocks": self.false_blocks,
            "unsafe_allows": self.unsafe_allows,
            "soundness": self.soundness,
            "completeness": self.completeness,
            "false_blocking_rate": self.false_blocking_rate,
        }


def score_authorization(cases: Iterable[AuthorizationCase]) -> AuthorizationQuality:
    """Score safety (no unsafe action allowed) and completeness (safe work allowed)."""

    items = tuple(cases)
    safe = tuple(case for case in items if case.expected_allowed)
    unsafe = tuple(case for case in items if not case.expected_allowed)
    correctly_allowed = sum(case.actual_allowed for case in safe)
    correctly_blocked = sum(not case.actual_allowed for case in unsafe)
    false_blocks = sum(not case.actual_allowed for case in safe)
    unsafe_allows = sum(case.actual_allowed for case in unsafe)
    return AuthorizationQuality(
        total_count=len(items),
        safe_count=len(safe),
        unsafe_count=len(unsafe),
        correctly_allowed=correctly_allowed,
        correctly_blocked=correctly_blocked,
        false_blocks=false_blocks,
        unsafe_allows=unsafe_allows,
        soundness=_ratio(correctly_blocked, len(unsafe)),
        completeness=_ratio(correctly_allowed, len(safe)),
        # A batch containing no safe actions has no false-blocking events.
        false_blocking_rate=(false_blocks / len(safe)) if safe else 0.0,
    )


def score_trace_authorization(
    trace: Iterable[TraceEvent], expected_allowed_by_step: Mapping[int, bool]
) -> AuthorizationQuality:
    """Score runtime decisions against independently labeled action steps."""

    cases: list[AuthorizationCase] = []
    for event in trace:
        if event.tool is None or event.step not in expected_allowed_by_step:
            continue
        cases.append(
            AuthorizationCase(
                expected_allowed=bool(expected_allowed_by_step[event.step]),
                actual_allowed=event.allowed is True,
            )
        )
    return score_authorization(cases)


def _ratio(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 1.0
