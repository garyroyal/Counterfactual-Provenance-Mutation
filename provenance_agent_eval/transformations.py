"""Controlled value transformations used to probe provenance preservation."""

from __future__ import annotations

from typing import Any, Iterable

from .core import Provenance, ProvenanceValue
from .provenance_graph import ProvenanceGraph, TransformKind


class ProvenanceTransformer:
    """Apply named transformations while making preservation choices explicit."""

    def __init__(self, graph: ProvenanceGraph) -> None:
        self.graph = graph

    def apply(
        self,
        value: ProvenanceValue,
        *,
        node_id: str,
        operation: TransformKind | str,
        preserve_provenance: bool = True,
        claimed_sources: Iterable[Provenance] | None = None,
        output: Any = None,
    ) -> ProvenanceValue:
        if value.node_id is None:
            raise ValueError("transformation input must be bound to a graph node")
        self.graph.derive(
            node_id,
            parents=[value.node_id],
            operation=operation,
            preserve_provenance=preserve_provenance,
            claimed_sources=claimed_sources,
        )
        return self.graph.to_value(node_id, value.value if output is None else output)

    def combine(
        self,
        values: Iterable[ProvenanceValue],
        *,
        node_id: str,
        operation: TransformKind | str = TransformKind.CONCATENATION,
        output: Any = None,
    ) -> ProvenanceValue:
        items = tuple(values)
        parent_ids = [value.node_id for value in items]
        if not items or any(parent_id is None for parent_id in parent_ids):
            raise ValueError("all combination inputs must be bound to graph nodes")
        self.graph.derive(node_id, parents=parent_ids, operation=operation)
        if output is None:
            output = tuple(value.value for value in items)
        return self.graph.to_value(node_id, output)

    def summarize(self, value: ProvenanceValue, *, node_id: str, preserve_provenance: bool = True) -> ProvenanceValue:
        return self.apply(
            value,
            node_id=node_id,
            operation=TransformKind.SUMMARY,
            preserve_provenance=preserve_provenance,
        )

    def rewrite(self, value: ProvenanceValue, *, node_id: str, claimed_sources: Iterable[Provenance] | None = None) -> ProvenanceValue:
        return self.apply(
            value,
            node_id=node_id,
            operation=TransformKind.REWRITE,
            claimed_sources=claimed_sources,
        )

    def memory_write(self, value: ProvenanceValue, *, node_id: str, preserve_provenance: bool = True) -> ProvenanceValue:
        return self.apply(
            value,
            node_id=node_id,
            operation=TransformKind.MEMORY_WRITE,
            preserve_provenance=preserve_provenance,
        )

    def handoff(self, value: ProvenanceValue, *, node_id: str, preserve_provenance: bool = True) -> ProvenanceValue:
        return self.apply(
            value,
            node_id=node_id,
            operation=TransformKind.AGENT_HANDOFF,
            preserve_provenance=preserve_provenance,
        )
