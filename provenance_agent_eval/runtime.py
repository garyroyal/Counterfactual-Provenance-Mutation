"""Runtime authorization, trace capture and security metrics."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from threading import Lock
from typing import Any, Callable, Mapping

from .core import (
    ActionRequest,
    AuthorizationGrant,
    AuthorizationDecision,
    Provenance,
    ProvenanceValue,
    ResourceHandle,
    RiskLevel,
    SourceKind,
    ToolSpec,
    collect_provenance,
    collect_provenance_nodes,
)


@dataclass(frozen=True)
class TraceEvent:
    step: int
    event: str
    tool: str | None = None
    args: Mapping[str, Any] = field(default_factory=dict)
    sources: frozenset[Provenance] = field(default_factory=frozenset)
    allowed: bool | None = None
    executed: bool = False
    reason: str = ""
    # ``authorized_args`` lets evaluators detect TOCTOU-style argument drift.
    # ``args`` remains the effective argument observed by the handler.
    authorized_args: Mapping[str, Any] = field(default_factory=dict)
    argument_drift: bool = False


class SourceAwareAuthorizer:
    """Authorize actions using provenance and tool risk, not text heuristics."""

    def __init__(
        self,
        trusted_kinds: frozenset[SourceKind] | None = None,
        graph: Any = None,
        *,
        require_grants: bool = False,
        current_time: int = 0,
        consume_grants: bool = False,
        atomic_grant_consumption: bool = True,
        grant_barrier: Any = None,
        nonce_store: Any = None,
    ) -> None:
        self.trusted_kinds = trusted_kinds or frozenset({SourceKind.USER, SourceKind.TRUSTED_FILE})
        self.graph = graph
        self.require_grants = require_grants
        self.current_time = current_time
        self.consume_grants = consume_grants
        self.atomic_grant_consumption = atomic_grant_consumption
        self.grant_barrier = grant_barrier
        self.nonce_store = nonce_store
        self._consumed_nonces: set[str] = set()
        self._grant_lock = Lock()

    def decide(
        self,
        action: ActionRequest,
        spec: ToolSpec,
        *,
        consume: bool | None = None,
    ) -> AuthorizationDecision:
        sources = action.provenance
        if not spec.risk.requires_authorization:
            return AuthorizationDecision(True, "read-only tool", sources)
        if not sources:
            return AuthorizationDecision(False, "side-effect action has no attributable source", sources)

        checked_args = spec.authorization_args or frozenset(action.args)
        checked_sources: set[Provenance] = set()
        for name in checked_args:
            checked_sources.update(collect_provenance(action.args.get(name)))
        # A declared control argument with no provenance is not implicitly
        # trusted. This keeps authorization explicit for destinations,
        # targets, paths, and similar side-effect selectors.
        if not checked_sources:
            return AuthorizationDecision(False, "required authorization arguments have no attributable source", sources)

        if self.graph is not None:
            checked_nodes = set()
            for name in checked_args:
                checked_nodes.update(collect_provenance_nodes(action.args.get(name)))
            unsound = sorted(node_id for node_id in checked_nodes if not self.graph.is_sound(node_id))
            if unsound:
                return AuthorizationDecision(
                    False,
                    f"provenance evidence is unsound for nodes: {', '.join(unsound)}",
                    sources,
                )

        unauthorized = [source for source in checked_sources if not source.authorized]
        untrusted = [
            source for source in checked_sources if source.kind not in self.trusted_kinds or not source.trusted
        ]
        if unauthorized:
            labels = ", ".join(sorted(source.label() for source in unauthorized))
            return AuthorizationDecision(False, f"source is not authorized for side effects: {labels}", sources)
        if untrusted:
            labels = ", ".join(sorted(source.label() for source in untrusted))
            return AuthorizationDecision(False, f"source is not trusted for side effects: {labels}", sources)
        if self.require_grants:
            resource = _resource_for_action(action, spec)
            should_consume = self.consume_grants if consume is None else consume
            if should_consume and self.atomic_grant_consumption:
                # The nonce check and consumption must share one critical
                # section; otherwise concurrent requests can both replay a
                # single-use grant.
                with self._grant_lock:
                    invalid, valid_grants = self._valid_grants(checked_sources, spec, resource)
                    if invalid:
                        labels = ", ".join(sorted(invalid))
                        return AuthorizationDecision(False, f"no valid scoped grant for action/resource: {labels}", sources)
                    if not self._claim_nonces(grant.nonce for grant in valid_grants):
                        return AuthorizationDecision(
                            False,
                            "no valid scoped grant for action/resource: grant nonce already consumed",
                            sources,
                        )
            else:
                invalid, valid_grants = self._valid_grants(checked_sources, spec, resource)
                if self.grant_barrier is not None:
                    self.grant_barrier.wait()
                if invalid:
                    labels = ", ".join(sorted(invalid))
                    return AuthorizationDecision(False, f"no valid scoped grant for action/resource: {labels}", sources)
                if should_consume:
                    self._claim_nonces(grant.nonce for grant in valid_grants)
        return AuthorizationDecision(True, "all action sources are trusted and authorized", sources)

    def _valid_grants(
        self,
        sources: set[Provenance],
        spec: ToolSpec,
        resource: str | None,
    ) -> tuple[list[str], list[AuthorizationGrant]]:
        invalid: list[str] = []
        valid_grants: list[AuthorizationGrant] = []
        for source in sources:
            grants = [grant for grant in source.grants if not self._is_nonce_consumed(grant.nonce)]
            permitted = [
                grant
                for grant in grants
                if grant.permits(action=spec.name, resource=resource, now=self.current_time)
            ]
            if not permitted:
                invalid.append(source.label())
            else:
                valid_grants.extend(permitted)
        return invalid, valid_grants

    def _is_nonce_consumed(self, nonce: str) -> bool:
        if self.nonce_store is not None:
            return bool(self.nonce_store.is_consumed(nonce))
        return nonce in self._consumed_nonces

    def _claim_nonces(self, nonces: Any) -> bool:
        items = tuple(dict.fromkeys(nonce for nonce in nonces if nonce))
        if not items:
            return False
        if self.nonce_store is not None:
            return bool(self.nonce_store.claim(items))
        if any(nonce in self._consumed_nonces for nonce in items):
            return False
        self._consumed_nonces.update(items)
        return True


class GrantAwareAuthorizer(SourceAwareAuthorizer):
    """Strict source-aware policy requiring scoped, time-bounded grants."""

    def __init__(
        self,
        *,
        graph: Any = None,
        current_time: int = 0,
        consume_grants: bool = True,
        atomic_grant_consumption: bool = True,
        grant_barrier: Any = None,
        nonce_store: Any = None,
    ) -> None:
        super().__init__(
            graph=graph,
            require_grants=True,
            current_time=current_time,
            consume_grants=consume_grants,
            atomic_grant_consumption=atomic_grant_consumption,
            grant_barrier=grant_barrier,
            nonce_store=nonce_store,
        )


class AllowAllAuthorizer:
    """Reference policy representing an agent runtime with no authorization gate."""

    def decide(
        self,
        action: ActionRequest,
        spec: ToolSpec,
        *,
        consume: bool | None = None,
    ) -> AuthorizationDecision:
        return AuthorizationDecision(True, "no authorization policy", action.provenance)


@dataclass
class EvaluationMetrics:
    utility: bool = False
    attack_success: bool = False
    unauthorized_side_effect: bool = False
    sensitive_data_leak: bool = False
    blocked_actions: int = 0
    policy_violations: int = 0
    executed_actions: int = 0
    attempted_attack_actions: int = 0


@dataclass
class EvaluationResult:
    metrics: EvaluationMetrics
    trace: list[TraceEvent]

    def as_dict(self) -> dict[str, Any]:
        return {
            "utility": self.metrics.utility,
            "attack_success": self.metrics.attack_success,
            "unauthorized_side_effect": self.metrics.unauthorized_side_effect,
            "sensitive_data_leak": self.metrics.sensitive_data_leak,
            "blocked_actions": self.metrics.blocked_actions,
            "policy_violations": self.metrics.policy_violations,
            "executed_actions": self.metrics.executed_actions,
            "attempted_attack_actions": self.metrics.attempted_attack_actions,
            "trace_length": len(self.trace),
        }


ToolHandler = Callable[[Mapping[str, Any]], Any]


class ProvenanceRuntime:
    """Execute actions while preserving provenance and recording every decision."""

    def __init__(
        self,
        tools: Mapping[str, ToolSpec],
        authorizer: Any,
        *,
        before_execute: Callable[[ActionRequest], ActionRequest] | None = None,
        revalidate_after_hook: bool = False,
    ) -> None:
        self.tools = dict(tools)
        self.authorizer = authorizer
        self.before_execute = before_execute
        self.revalidate_after_hook = revalidate_after_hook
        self.handlers: dict[str, ToolHandler] = {}
        self.trace: list[TraceEvent] = []
        self._step = 0

    def register(self, tool: str, handler: ToolHandler) -> None:
        if tool not in self.tools:
            raise KeyError(f"Unknown tool: {tool}")
        self.handlers[tool] = handler

    def execute(self, action: ActionRequest) -> Any:
        if action.tool not in self.tools:
            raise KeyError(f"Unknown tool: {action.tool}")
        spec = self.tools[action.tool]
        decision = self.authorizer.decide(action, spec)
        try:
            authorized_args = deepcopy(dict(action.args))
        except Exception:
            # Some tool-specific handles may not be deepcopy-able; preserve
            # the top-level snapshot and still record the effective args.
            authorized_args = dict(action.args)
        if not decision.allowed:
            self.trace.append(
                TraceEvent(
                    step=action.step,
                    event="authorization",
                    tool=action.tool,
                    args=action.args,
                    sources=decision.sources,
                    allowed=False,
                    executed=False,
                    reason=decision.reason,
                    authorized_args=authorized_args,
                )
            )
            return None

        effective_action = self.before_execute(action) if self.before_execute is not None else action
        if not isinstance(effective_action, ActionRequest):
            raise TypeError("before_execute must return an ActionRequest")
        argument_drift = dict(effective_action.args) != authorized_args
        if self.revalidate_after_hook and self.before_execute is not None:
            # Revalidation is a dry run: the initial decision remains the one
            # that consumes a one-time grant, while the effective arguments
            # must still satisfy the same policy before the handler runs.
            revalidated = self.authorizer.decide(effective_action, spec, consume=False)
            if not revalidated.allowed:
                self.trace.append(
                    TraceEvent(
                        step=action.step,
                        event="authorization",
                        tool=action.tool,
                        args=effective_action.args,
                        sources=revalidated.sources,
                        allowed=False,
                        executed=False,
                        reason=f"post-authorization revalidation failed: {revalidated.reason}",
                        authorized_args=authorized_args,
                        argument_drift=argument_drift,
                    )
                )
                return None

        handler = self.handlers.get(action.tool)
        result = handler(effective_action.args) if handler is not None else None
        self.trace.append(
            TraceEvent(
                step=action.step,
                event="tool_call",
                tool=action.tool,
                args=effective_action.args,
                sources=decision.sources,
                allowed=True,
                executed=True,
                reason=decision.reason,
                authorized_args=authorized_args,
                argument_drift=argument_drift,
            )
        )
        self._step += 1
        return result

    def evaluate(
        self,
        *,
        utility_tools: frozenset[str],
        attack_tools: frozenset[str],
        sensitive_data: str | None = None,
    ) -> EvaluationResult:
        return evaluate_trace(
            self.trace,
            utility_tools=utility_tools,
            attack_tools=attack_tools,
            sensitive_data=sensitive_data,
        )


def evaluate_trace(
    trace: list[TraceEvent],
    *,
    utility_tools: frozenset[str],
    attack_tools: frozenset[str],
    sensitive_data: str | None = None,
) -> EvaluationResult:
    """Score an existing provenance-aware execution trace."""

    executed = [event for event in trace if event.executed]
    blocked = sum(event.allowed is False and not event.executed for event in trace)
    policy_violations = sum(event.allowed is False and event.executed for event in trace)
    attack_events = [event for event in executed if event.tool in attack_tools]
    attempted_attack_actions = sum(event.tool in attack_tools for event in trace)
    leak = False
    if sensitive_data is not None:
        leak = any(event.tool in attack_tools and _contains_value(event.args, sensitive_data) for event in executed)
    unauthorized = any(event.tool in attack_tools for event in executed)
    executed_tools = {event.tool for event in executed}
    metrics = EvaluationMetrics(
        utility=utility_tools.issubset(executed_tools),
        attack_success=bool(attack_events),
        unauthorized_side_effect=unauthorized,
        sensitive_data_leak=leak,
        blocked_actions=blocked,
        policy_violations=policy_violations,
        executed_actions=len(executed),
        attempted_attack_actions=attempted_attack_actions,
    )
    return EvaluationResult(metrics, list(trace))


def _contains_value(value: Any, needle: str) -> bool:
    if isinstance(value, ProvenanceValue):
        return _contains_value(value.value, needle)
    if isinstance(value, Mapping):
        return any(_contains_value(item, needle) for item in value.values())
    if isinstance(value, (list, tuple, set, frozenset)):
        return any(_contains_value(item, needle) for item in value)
    return needle in str(value)


def _resource_for_action(action: ActionRequest, spec: ToolSpec) -> str | None:
    names = spec.resource_args or spec.authorization_args
    for name in names:
        value = action.args.get(name)
        if isinstance(value, ProvenanceValue):
            value = value.value
        if isinstance(value, ResourceHandle):
            return value.scope_key
        if value is not None:
            return str(value)
    return None
