"""Mechanism-level enforcement abstractions evaluated by CPM.

These are not new defenses.  Each class is a minimal, faithful abstraction of
how a family of published systems consumes provenance evidence, so that a
degradation curve can be attributed to the *mechanism* rather than to one
implementation.  Correspondence to the literature is given in each docstring
and must be cited, not claimed, in the paper.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from ..core import ActionRequest, AuthorizationDecision, Provenance, SourceKind, ToolSpec, collect_provenance, collect_provenance_nodes
from ..provenance_graph import ProvenanceGraph
from ..runtime import AllowAllAuthorizer, SourceAwareAuthorizer


class DefenseMechanism(str, Enum):
    NO_POLICY = "no_policy"
    LABEL_TRUSTING = "label_trusting"
    LINEAGE_VERIFYING = "lineage_verifying"
    ORIGIN_ROUTING = "origin_routing"
    WHOLE_CALL_QUARANTINE = "whole_call_quarantine"


MECHANISM_NOTES: dict[DefenseMechanism, str] = {
    DefenseMechanism.NO_POLICY: "Undefended runtime; diagnostic baseline.",
    DefenseMechanism.LABEL_TRUSTING: (
        "Trusts the labels attached to guarded arguments (taint-label IFC such as interbolt-style "
        "provenance gates, FIDES-style labels). Ancestry is not consulted."
    ),
    DefenseMechanism.LINEAGE_VERIFYING: (
        "Requires labels to be consistent with graph ancestry before trusting them (AuthGraph-style "
        "comparison of claimed vs. derived provenance). Fails closed when labels are missing."
    ),
    DefenseMechanism.ORIGIN_ROUTING: (
        "Ignores labels; admits a guarded argument only if every root in its ancestry is a trusted, "
        "user-authorised origin (ROPE's unforgeable origin check; PACT's role contracts over accumulated origins)."
    ),
    DefenseMechanism.WHOLE_CALL_QUARANTINE: (
        "Blocks a side-effecting call if *any* argument, content included, has untrusted ancestry "
        "(CaMeL/FIDES-style whole-call quarantine). Trades utility for security by construction."
    ),
}


def _trusted(source: Provenance) -> bool:
    return source.trusted and source.authorized


class OriginRoutingAuthorizer:
    """Admit guarded arguments purely from graph ancestry."""

    def __init__(self, graph: ProvenanceGraph) -> None:
        self.graph = graph

    def decide(self, action: ActionRequest, spec: ToolSpec, *, consume: bool | None = None) -> AuthorizationDecision:
        sources = action.provenance
        if not spec.risk.requires_authorization:
            return AuthorizationDecision(True, "read-only tool", sources)
        guarded = spec.authorization_args or frozenset(action.args)
        for name in guarded:
            nodes = collect_provenance_nodes(action.args.get(name))
            if not nodes:
                return AuthorizationDecision(False, f"guarded argument {name!r} has no origin binding", sources)
            for node_id in nodes:
                roots = self.graph.root_sources(node_id)
                bad = sorted(source.label() for source in roots if not _trusted(source))
                if not roots or bad:
                    return AuthorizationDecision(
                        False,
                        f"guarded argument {name!r} traces to non-user origin: {', '.join(bad) or 'unknown'}",
                        sources,
                    )
        return AuthorizationDecision(True, "all guarded arguments trace to authorised origins", sources)


class WholeCallQuarantineAuthorizer:
    """Block any side-effecting call touched by untrusted ancestry."""

    def __init__(self, graph: ProvenanceGraph) -> None:
        self.graph = graph

    def decide(self, action: ActionRequest, spec: ToolSpec, *, consume: bool | None = None) -> AuthorizationDecision:
        sources = action.provenance
        if not spec.risk.requires_authorization:
            return AuthorizationDecision(True, "read-only tool", sources)
        nodes = collect_provenance_nodes(action.args)
        if not nodes:
            return AuthorizationDecision(False, "side-effect call has no origin bindings", sources)
        for node_id in sorted(nodes):
            roots = self.graph.root_sources(node_id)
            if not roots or not all(_trusted(source) for source in roots):
                return AuthorizationDecision(False, f"call is tainted through node {node_id}", sources)
        return AuthorizationDecision(True, "no argument carries untrusted ancestry", sources)


def make_authorizer(mechanism: DefenseMechanism, observed_graph: ProvenanceGraph) -> Any:
    """Instantiate the mechanism over the *observed* (possibly mutated) graph."""

    if mechanism is DefenseMechanism.NO_POLICY:
        return AllowAllAuthorizer()
    if mechanism is DefenseMechanism.LABEL_TRUSTING:
        return SourceAwareAuthorizer(trusted_kinds=frozenset({SourceKind.USER, SourceKind.TRUSTED_FILE, SourceKind.TOOL_OUTPUT}))
    if mechanism is DefenseMechanism.LINEAGE_VERIFYING:
        return SourceAwareAuthorizer(
            trusted_kinds=frozenset({SourceKind.USER, SourceKind.TRUSTED_FILE, SourceKind.TOOL_OUTPUT}),
            graph=observed_graph,
        )
    if mechanism is DefenseMechanism.ORIGIN_ROUTING:
        return OriginRoutingAuthorizer(observed_graph)
    if mechanism is DefenseMechanism.WHOLE_CALL_QUARANTINE:
        return WholeCallQuarantineAuthorizer(observed_graph)
    raise ValueError(f"unknown mechanism: {mechanism}")


__all__ = [
    "DefenseMechanism",
    "MECHANISM_NOTES",
    "OriginRoutingAuthorizer",
    "WholeCallQuarantineAuthorizer",
    "make_authorizer",
    "collect_provenance",
]
