"""Explicit provenance graphs for source preservation and laundering checks."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable

from .core import Provenance, ProvenanceValue


class TransformKind(str, Enum):
    DIRECT = "direct"
    SUMMARY = "summary"
    REWRITE = "rewrite"
    STRUCTURED_EXTRACTION = "structured_extraction"
    CONCATENATION = "concatenation"
    MEMORY_WRITE = "memory_write"
    TOOL_FORWARD = "tool_forward"
    AGENT_HANDOFF = "agent_handoff"


@dataclass(frozen=True)
class Endorsement:
    """A separately attributable assertion about a derived value."""

    endorser: Provenance
    claim: str = ""

    @property
    def valid(self) -> bool:
        return self.endorser.trusted and self.endorser.authorized


@dataclass(frozen=True)
class ProvenanceNode:
    node_id: str
    operation: str
    parents: frozenset[str] = field(default_factory=frozenset)
    attached_sources: frozenset[Provenance] = field(default_factory=frozenset)
    endorsements: tuple[Endorsement, ...] = ()

    @property
    def attached_source_ids(self) -> frozenset[str]:
        return frozenset(source.source_id for source in self.attached_sources)

    @property
    def valid_endorsements(self) -> tuple[Endorsement, ...]:
        return tuple(endorsement for endorsement in self.endorsements if endorsement.valid)


class ProvenanceGraph:
    """A DAG of values and transformations with auditable source metadata.

    ``attached_sources`` records what a node claims. ``root_sources`` is
    derived solely from graph ancestry, so source loss and source forgery can
    be detected without trusting the derived node's own metadata.
    """

    def __init__(self) -> None:
        self._nodes: dict[str, ProvenanceNode] = {}

    @property
    def nodes(self) -> dict[str, ProvenanceNode]:
        return dict(self._nodes)

    def add_source(self, node_id: str, source: Provenance) -> ProvenanceNode:
        if node_id in self._nodes:
            raise ValueError(f"node already exists: {node_id}")
        node = ProvenanceNode(
            node_id=node_id,
            operation="source",
            attached_sources=frozenset({source}),
        )
        self._nodes[node_id] = node
        return node

    def derive(
        self,
        node_id: str,
        *,
        parents: Iterable[str],
        operation: TransformKind | str,
        preserve_provenance: bool = True,
        claimed_sources: Iterable[Provenance] | None = None,
    ) -> ProvenanceNode:
        if node_id in self._nodes:
            raise ValueError(f"node already exists: {node_id}")
        parent_ids = frozenset(parents)
        if not parent_ids:
            raise ValueError("a derived node must have at least one parent")
        missing = parent_ids - self._nodes.keys()
        if missing:
            raise KeyError(f"unknown parent nodes: {sorted(missing)}")
        if claimed_sources is not None:
            attached = frozenset(claimed_sources)
        elif preserve_provenance:
            attached = frozenset(
                source
                for parent_id in parent_ids
                for source in self._nodes[parent_id].attached_sources
            )
        else:
            attached = frozenset()
        node = ProvenanceNode(
            node_id=node_id,
            operation=operation.value if isinstance(operation, TransformKind) else str(operation),
            parents=parent_ids,
            attached_sources=attached,
        )
        self._nodes[node_id] = node
        return node

    def endorse(self, node_id: str, endorsement: Endorsement) -> ProvenanceNode:
        node = self._require(node_id)
        updated = ProvenanceNode(
            node_id=node.node_id,
            operation=node.operation,
            parents=node.parents,
            attached_sources=node.attached_sources,
            endorsements=node.endorsements + (endorsement,),
        )
        self._nodes[node_id] = updated
        return updated

    def copy(self) -> "ProvenanceGraph":
        """Return an independent graph sharing the immutable node objects."""

        clone = ProvenanceGraph()
        clone._nodes = dict(self._nodes)
        return clone

    def rewire(
        self,
        node_id: str,
        *,
        parents: Iterable[str] | None = None,
        attached_sources: Iterable[Provenance] | None = None,
        operation: TransformKind | str | None = None,
    ) -> ProvenanceNode:
        """Replace a derived node's edges and/or claimed sources.

        This is the primitive used by counterfactual mutation operators. It is
        deliberately unavailable to policies: a defense only reads the graph.
        Root (source) nodes cannot be re-parented, and cycles are rejected.
        """

        node = self._require(node_id)
        new_parents = node.parents if parents is None else frozenset(parents)
        if parents is not None:
            if not node.parents:
                raise ValueError(f"cannot re-parent a root source node: {node_id}")
            if not new_parents:
                raise ValueError("a derived node must keep at least one parent")
            missing = new_parents - self._nodes.keys()
            if missing:
                raise KeyError(f"unknown parent nodes: {sorted(missing)}")
            for parent_id in new_parents:
                if parent_id == node_id or self._reaches(parent_id, node_id):
                    raise ValueError(f"rewiring {node_id} under {parent_id} would create a cycle")
        updated = ProvenanceNode(
            node_id=node.node_id,
            operation=(
                node.operation
                if operation is None
                else operation.value if isinstance(operation, TransformKind) else str(operation)
            ),
            parents=new_parents,
            attached_sources=node.attached_sources if attached_sources is None else frozenset(attached_sources),
            endorsements=node.endorsements,
        )
        self._nodes[node_id] = updated
        return updated

    def children(self, node_id: str) -> frozenset[str]:
        self._require(node_id)
        return frozenset(child.node_id for child in self._nodes.values() if node_id in child.parents)

    def node(self, node_id: str) -> ProvenanceNode:
        return self._require(node_id)

    def root_sources(self, node_id: str) -> frozenset[Provenance]:
        self._require(node_id)
        memo: dict[str, frozenset[Provenance]] = {}

        def visit(current: str) -> frozenset[Provenance]:
            cached = memo.get(current)
            if cached is not None:
                return cached
            node = self._nodes[current]
            if not node.parents:
                result = node.attached_sources
            else:
                result = frozenset(source for parent_id in node.parents for source in visit(parent_id))
            memo[current] = result
            return result

        return visit(node_id)

    def _reaches(self, start: str, target: str) -> bool:
        """True when ``target`` is an ancestor of (or equal to) ``start``."""

        stack = [start]
        seen: set[str] = set()
        while stack:
            current = stack.pop()
            if current == target:
                return True
            if current in seen:
                continue
            seen.add(current)
            stack.extend(self._nodes[current].parents)
        return False

    def missing_sources(self, node_id: str) -> frozenset[Provenance]:
        node = self._require(node_id)
        roots = self.root_sources(node_id)
        return frozenset(source for source in roots if source not in node.attached_sources)

    def forged_sources(self, node_id: str) -> frozenset[Provenance]:
        node = self._require(node_id)
        roots = self.root_sources(node_id)
        return frozenset(source for source in node.attached_sources if source not in roots)

    def is_sound(self, node_id: str) -> bool:
        return not self.missing_sources(node_id) and not self.forged_sources(node_id)

    def to_value(self, node_id: str, value: Any) -> ProvenanceValue:
        """Materialize the node's attached evidence for runtime use."""

        return ProvenanceValue(
            value=value,
            provenance=self.node(node_id).attached_sources,
            node_id=node_id,
        )

    def _require(self, node_id: str) -> ProvenanceNode:
        try:
            return self._nodes[node_id]
        except KeyError as exc:
            raise KeyError(f"unknown provenance node: {node_id}") from exc
