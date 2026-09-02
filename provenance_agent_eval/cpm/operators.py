"""Single-variable mutation operators over a provenance graph.

Every operator changes exactly one aspect of the *observed* evidence for one
node.  The oracle graph is never mutated; ground truth is computed from it.
Operators therefore model the ways real provenance pipelines go wrong, each
tied to a documented real-world cause and to the CPM invariant it probes.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ..core import Provenance
from ..provenance_graph import ProvenanceGraph, TransformKind


class MutationOperator(str, Enum):
    PRESERVE = "preserve"
    DROP_LABEL = "drop_label"
    FORGE_LABEL = "forge_label"
    MISATTRIBUTE_PARENT = "misattribute_parent"
    MERGE_TAINT = "merge_taint"


@dataclass(frozen=True)
class OperatorSpec:
    operator: MutationOperator
    description: str
    invariant: str
    eligible: str
    real_world_cause: str
    breaks_assumption_of: str


OPERATOR_SPECS: dict[MutationOperator, OperatorSpec] = {
    MutationOperator.PRESERVE: OperatorSpec(
        MutationOperator.PRESERVE,
        "Insert a semantics-preserving summary node that keeps every source edge and label.",
        "I1 representation non-interference: the decision must not change.",
        "any derived node",
        "Ordinary summarisation / reformatting that carries metadata forward.",
        "control condition; no assumption is broken",
    ),
    MutationOperator.DROP_LABEL: OperatorSpec(
        MutationOperator.DROP_LABEL,
        "Clear the claimed sources of a derived node while its ancestry stays intact.",
        "I2 no authority gain under degradation; utility cost of fail-closed labels.",
        "any derived node with a non-empty label set",
        "Memory stores that persist text but not metadata; string assembly (f-strings, join) that "
        "produces a fresh unlabelled value (interbolt docs); framework handoffs that pass plain text.",
        "label-based information-flow control",
    ),
    MutationOperator.FORGE_LABEL: OperatorSpec(
        MutationOperator.FORGE_LABEL,
        "Attach the trusted root's label to a node whose ancestry is entirely untrusted.",
        "I3 no forged inheritance.",
        "untrusted-derived node",
        "Buggy or compromised memory/handoff components that re-tag content as user-provided; "
        "LLM-written provenance fields.",
        "policies that trust labels without verifying lineage",
    ),
    MutationOperator.MISATTRIBUTE_PARENT: OperatorSpec(
        MutationOperator.MISATTRIBUTE_PARENT,
        "Re-parent an untrusted-derived node under the trusted root so ancestry itself lies.",
        "I3 no forged inheritance (lineage variant).",
        "untrusted-derived node",
        "Provenance inferred by an LLM builder attributing injected content to the user "
        "(AuthGraph limitation: attribution errors cause false negatives); semantic taint trackers "
        "losing the source under paraphrase (NeuroTaint semantic attenuation).",
        "every ancestry/lineage-based policy",
    ),
    MutationOperator.MERGE_TAINT: OperatorSpec(
        MutationOperator.MERGE_TAINT,
        "Add an untrusted parent to a trusted-derived node so a legitimate value inherits taint.",
        "I2 (utility side): label creep must not silently destroy legitimate work.",
        "trusted-derived node when an untrusted node exists in the graph",
        "Summaries that merge multiple sources into one value; coarse taint propagation "
        "(the label-creep problem discussed by RTBAS and FIDES).",
        "coarse taint propagation / whole-call quarantine",
    ),
}


@dataclass(frozen=True)
class OperatorContext:
    """Graph facts an operator needs beyond the node it targets."""

    trusted_root_id: str
    trusted_root: Provenance
    untrusted_node_ids: tuple[str, ...]


def _is_trusted(source: Provenance) -> bool:
    return source.trusted and source.authorized


def _derived(graph: ProvenanceGraph, node_id: str) -> bool:
    return bool(graph.node(node_id).parents)


def _untrusted_derived(graph: ProvenanceGraph, node_id: str) -> bool:
    roots = graph.root_sources(node_id)
    return _derived(graph, node_id) and bool(roots) and not any(_is_trusted(source) for source in roots)


def _trusted_derived(graph: ProvenanceGraph, node_id: str) -> bool:
    roots = graph.root_sources(node_id)
    return _derived(graph, node_id) and bool(roots) and all(_is_trusted(source) for source in roots)


def eligible_nodes(graph: ProvenanceGraph, operator: MutationOperator, context: OperatorContext) -> tuple[str, ...]:
    """Nodes on which ``operator`` is a meaningful single-variable change."""

    nodes = sorted(graph.nodes)
    if operator is MutationOperator.PRESERVE:
        return tuple(node_id for node_id in nodes if _derived(graph, node_id))
    if operator is MutationOperator.DROP_LABEL:
        return tuple(
            node_id for node_id in nodes if _derived(graph, node_id) and graph.node(node_id).attached_sources
        )
    if operator in {MutationOperator.FORGE_LABEL, MutationOperator.MISATTRIBUTE_PARENT}:
        return tuple(node_id for node_id in nodes if _untrusted_derived(graph, node_id))
    if operator is MutationOperator.MERGE_TAINT:
        if not context.untrusted_node_ids:
            return ()
        return tuple(node_id for node_id in nodes if _trusted_derived(graph, node_id))
    raise ValueError(f"unknown operator: {operator}")


def apply_operator(
    graph: ProvenanceGraph,
    node_id: str,
    operator: MutationOperator,
    context: OperatorContext,
) -> str:
    """Mutate ``graph`` in place and return the node id a consumer should now bind to.

    All operators except PRESERVE keep the node id; PRESERVE returns the id of
    the inserted summary node so the binding can be redirected to it.
    """

    if operator is MutationOperator.PRESERVE:
        summary_id = f"{node_id}:preserve"
        if summary_id not in graph.nodes:
            graph.derive(summary_id, parents=[node_id], operation=TransformKind.SUMMARY, preserve_provenance=True)
        return summary_id
    if operator is MutationOperator.DROP_LABEL:
        graph.rewire(node_id, attached_sources=())
        return node_id
    if operator is MutationOperator.FORGE_LABEL:
        graph.rewire(node_id, attached_sources=(context.trusted_root,))
        return node_id
    if operator is MutationOperator.MISATTRIBUTE_PARENT:
        graph.rewire(
            node_id,
            parents=[context.trusted_root_id],
            attached_sources=(context.trusted_root,),
            operation=TransformKind.REWRITE,
        )
        return node_id
    if operator is MutationOperator.MERGE_TAINT:
        taint_id = _pick_taint(graph, node_id, context)
        node = graph.node(node_id)
        taint_sources = graph.node(taint_id).attached_sources or graph.root_sources(taint_id)
        graph.rewire(
            node_id,
            parents=set(node.parents) | {taint_id},
            attached_sources=set(node.attached_sources) | set(taint_sources),
            operation=TransformKind.CONCATENATION,
        )
        return node_id
    raise ValueError(f"unknown operator: {operator}")


def _pick_taint(graph: ProvenanceGraph, node_id: str, context: OperatorContext) -> str:
    for candidate in context.untrusted_node_ids:
        if candidate == node_id or graph._reaches(candidate, node_id):
            continue
        return candidate
    raise ValueError(f"no untrusted node can taint {node_id} without creating a cycle")


def propagate_labels(graph: ProvenanceGraph, pinned: set[str]) -> None:
    """Recompute observed labels downstream of mutated nodes.

    Real provenance pipelines carry labels *forward*: a hop that drops its
    metadata leaves every later hop unlabelled, and a hop that re-tags a value
    as user-provided is believed by every later hop.  After the operators have
    set the labels of the ``pinned`` (mutated) nodes explicitly, every other
    derived node's observed label is recomputed as the union of its parents'
    observed labels, in topological order.  Root sources are never changed.

    Without this pass an operator corrupts only the sink-side evidence record
    of one node; that is a different (narrower) failure model, kept available
    as ``propagate=False`` in :class:`~.schedule.MutationSchedule`.
    """

    order = _topological_order(graph)
    for node_id in order:
        node = graph.node(node_id)
        if not node.parents or node_id in pinned:
            continue
        inherited = frozenset(
            source for parent_id in node.parents for source in graph.node(parent_id).attached_sources
        )
        if inherited != node.attached_sources:
            graph.rewire(node_id, attached_sources=inherited)


def _topological_order(graph: ProvenanceGraph) -> list[str]:
    nodes = graph.nodes
    indegree = {node_id: len(node.parents) for node_id, node in nodes.items()}
    ready = sorted(node_id for node_id, degree in indegree.items() if degree == 0)
    order: list[str] = []
    while ready:
        current = ready.pop(0)
        order.append(current)
        for child_id in sorted(graph.children(current)):
            indegree[child_id] -= 1
            if indegree[child_id] == 0:
                ready.append(child_id)
    if len(order) != len(nodes):
        raise ValueError("provenance graph contains a cycle")
    return order
