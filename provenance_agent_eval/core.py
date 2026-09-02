"""Data model for provenance, risk and tool actions.

The model deliberately keeps provenance separate from text. A string is not
trusted merely because it does not contain an obvious injection keyword.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class SourceKind(str, Enum):
    UNKNOWN = "unknown"
    USER = "user"
    TRUSTED_FILE = "trusted_file"
    USER_HISTORY = "user_history"
    EXTERNAL_DOCUMENT = "external_document"
    TOOL_OUTPUT = "tool_output"
    MEMORY = "memory"
    MULTI_AGENT = "multi_agent"
    MODEL_GENERATED = "model_generated"


class DeliveryChannel(str, Enum):
    UNKNOWN = "unknown"
    USER_PROMPT = "user_prompt"
    TOOL_OUTPUT = "tool_output"
    DOCUMENT = "document"
    MEMORY = "memory"
    MULTI_AGENT = "multi_agent"


class RiskLevel(str, Enum):
    READ_ONLY = "read_only"
    STATE_CHANGE = "state_change"
    EXTERNAL_SIDE_EFFECT = "external_side_effect"
    DESTRUCTIVE = "destructive"

    @property
    def requires_authorization(self) -> bool:
        return self is not RiskLevel.READ_ONLY


@dataclass(frozen=True)
class ResourceHandle:
    """Versioned identity for a mutable external resource.

    Grants bind to ``scope_key`` rather than only to the current display
    value, so a resource can be replaced between authorization and use.
    """

    resource_id: str
    version: int
    value: Any

    @property
    def scope_key(self) -> str:
        return f"{self.resource_id}@{self.version}"


@dataclass(frozen=True)
class AuthorizationGrant:
    """Verifiable, bounded authorization attached to a provenance source."""

    grant_id: str
    issuer: str
    action_scopes: frozenset[str]
    resource_scopes: frozenset[str] = field(default_factory=frozenset)
    issued_at: int = 0
    expires_at: int | None = None
    nonce: str = ""

    def permits(self, *, action: str, resource: str | None, now: int) -> bool:
        if action not in self.action_scopes and "*" not in self.action_scopes:
            return False
        if self.expires_at is not None and now >= self.expires_at:
            return False
        if now < self.issued_at:
            return False
        if self.resource_scopes and resource not in self.resource_scopes and "*" not in self.resource_scopes:
            return False
        return bool(self.issuer and self.nonce)


@dataclass(frozen=True)
class Provenance:
    """Origin metadata attached to a value that may reach a tool argument."""

    source_id: str
    kind: SourceKind
    channel: DeliveryChannel
    trusted: bool = False
    authorized: bool = False
    grants: tuple[AuthorizationGrant, ...] = ()

    def label(self) -> str:
        return f"{self.kind.value}:{self.source_id}"


@dataclass(frozen=True)
class ProvenanceValue:
    """A value plus the complete set of origins that contributed to it."""

    value: Any
    provenance: frozenset[Provenance] = field(default_factory=frozenset)
    # When present, this binds the value to a node in a ProvenanceGraph.
    node_id: str | None = None

    @classmethod
    def from_source(cls, value: Any, source: Provenance) -> "ProvenanceValue":
        return cls(value=value, provenance=frozenset({source}))

    @classmethod
    def literal(cls, value: Any) -> "ProvenanceValue":
        source = Provenance(
            source_id="model-generated",
            kind=SourceKind.MODEL_GENERATED,
            channel=DeliveryChannel.USER_PROMPT,
            trusted=False,
            authorized=False,
        )
        return cls.from_source(value, source)

    def combine(self, *others: "ProvenanceValue") -> "ProvenanceValue":
        origins = set(self.provenance)
        for other in others:
            origins.update(other.provenance)
        return ProvenanceValue(self.value, frozenset(origins))

    @property
    def has_untrusted_source(self) -> bool:
        return any(not source.trusted for source in self.provenance)

    @property
    def has_unauthorized_source(self) -> bool:
        return any(not source.authorized for source in self.provenance)


def collect_provenance(value: Any) -> frozenset[Provenance]:
    """Recursively collect provenance from nested tool arguments."""

    if isinstance(value, ProvenanceValue):
        return value.provenance | collect_provenance(value.value)
    if isinstance(value, Mapping):
        origins: set[Provenance] = set()
        for item in value.values():
            origins.update(collect_provenance(item))
        return frozenset(origins)
    if isinstance(value, (list, tuple, set, frozenset)):
        origins = set()
        for item in value:
            origins.update(collect_provenance(item))
        return frozenset(origins)
    return frozenset()


def collect_provenance_nodes(value: Any) -> frozenset[str]:
    """Recursively collect graph node bindings from nested values."""

    if isinstance(value, ProvenanceValue):
        nodes = {value.node_id} if value.node_id is not None else set()
        nodes.update(collect_provenance_nodes(value.value))
        return frozenset(nodes)
    if isinstance(value, Mapping):
        nodes: set[str] = set()
        for item in value.values():
            nodes.update(collect_provenance_nodes(item))
        return frozenset(nodes)
    if isinstance(value, (list, tuple, set, frozenset)):
        nodes = set()
        for item in value:
            nodes.update(collect_provenance_nodes(item))
        return frozenset(nodes)
    return frozenset()


@dataclass(frozen=True)
class ToolSpec:
    name: str
    risk: RiskLevel
    description: str = ""
    sensitive_outputs: bool = False
    authorization_args: frozenset[str] = field(default_factory=frozenset)
    resource_args: frozenset[str] = field(default_factory=frozenset)
    """Arguments whose origins must be trusted and explicitly authorized.

    When empty, all argument origins are checked for side-effect tools. This
    lets a policy distinguish an authorized user-selected destination from
    untrusted data that is merely being carried in an action payload.
    """


@dataclass(frozen=True)
class ActionRequest:
    tool: str
    args: Mapping[str, Any]
    step: int
    actor: str = "agent"

    @property
    def provenance(self) -> frozenset[Provenance]:
        return collect_provenance(self.args)


@dataclass(frozen=True)
class AuthorizationDecision:
    allowed: bool
    reason: str
    sources: frozenset[Provenance] = field(default_factory=frozenset)
