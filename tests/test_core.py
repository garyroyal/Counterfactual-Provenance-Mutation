import unittest

from provenance_agent_eval.core import (
    ActionRequest,
    AuthorizationGrant,
    DeliveryChannel,
    Provenance,
    ProvenanceValue,
    ResourceHandle,
    RiskLevel,
    SourceKind,
    ToolSpec,
    collect_provenance,
)
from provenance_agent_eval.runtime import AllowAllAuthorizer, GrantAwareAuthorizer, ProvenanceRuntime, SourceAwareAuthorizer
from provenance_agent_eval.nonce_store import InMemoryNonceStore
from provenance_agent_eval.scenarios import paired_scenarios, run_scenario


class ProvenanceCoreTests(unittest.TestCase):
    def test_nested_values_preserve_all_origins(self) -> None:
        tool_source = Provenance("tool-1", SourceKind.TOOL_OUTPUT, DeliveryChannel.TOOL_OUTPUT)
        document_source = Provenance("doc-1", SourceKind.EXTERNAL_DOCUMENT, DeliveryChannel.DOCUMENT)
        value = {
            "to": ProvenanceValue.from_source("attacker@example.com", tool_source),
            "body": ProvenanceValue.from_source("secret", document_source),
        }
        self.assertEqual(collect_provenance(value), frozenset({tool_source, document_source}))

    def test_read_only_action_is_allowed_but_side_effect_is_blocked(self) -> None:
        source = Provenance("external", SourceKind.EXTERNAL_DOCUMENT, DeliveryChannel.DOCUMENT)
        tools = {
            "read": ToolSpec("read", RiskLevel.READ_ONLY),
            "send": ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT),
        }
        runtime = ProvenanceRuntime(tools, SourceAwareAuthorizer())
        runtime.execute(ActionRequest("read", {"q": ProvenanceValue.from_source("x", source)}, 1))
        runtime.execute(ActionRequest("send", {"body": ProvenanceValue.from_source("x", source)}, 2))
        self.assertTrue(runtime.trace[0].executed)
        self.assertFalse(runtime.trace[1].executed)
        self.assertFalse(runtime.trace[1].allowed)
        result = runtime.evaluate(
            utility_tools=frozenset({"read"}), attack_tools=frozenset({"send"})
        )
        self.assertEqual(result.metrics.blocked_actions, 1)
        self.assertEqual(result.metrics.attempted_attack_actions, 1)
        self.assertEqual(result.metrics.policy_violations, 0)

    def test_explicitly_authorized_user_source_can_trigger_side_effect(self) -> None:
        source = Provenance(
            "user-request", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True
        )
        tools = {"send": ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT)}
        runtime = ProvenanceRuntime(tools, SourceAwareAuthorizer())
        runtime.execute(ActionRequest("send", {"body": ProvenanceValue.from_source("approved", source)}, 1))
        self.assertTrue(runtime.trace[0].executed)

    def test_authorization_control_argument_can_be_separated_from_payload_data(self) -> None:
        user_source = Provenance(
            "user-request", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True
        )
        external_source = Provenance("tool-output", SourceKind.TOOL_OUTPUT, DeliveryChannel.TOOL_OUTPUT)
        tools = {
            "send": ToolSpec(
                "send", RiskLevel.EXTERNAL_SIDE_EFFECT, authorization_args=frozenset({"recipient"})
            )
        }
        runtime = ProvenanceRuntime(tools, SourceAwareAuthorizer())
        runtime.execute(
            ActionRequest(
                "send",
                {
                    "recipient": ProvenanceValue.from_source("team@example.com", user_source),
                    "body": ProvenanceValue.from_source("secret", external_source),
                },
                1,
            )
        )
        self.assertTrue(runtime.trace[0].executed)

    def test_scoped_grant_allows_matching_action_and_resource(self) -> None:
        grant = AuthorizationGrant(
            "g-1", "auth-service", frozenset({"send"}), frozenset({"team@example.com"}),
            issued_at=10, expires_at=20, nonce="n-1"
        )
        source = Provenance(
            "user-request", SourceKind.USER, DeliveryChannel.USER_PROMPT,
            trusted=True, authorized=True, grants=(grant,)
        )
        runtime = ProvenanceRuntime(
            {"send": ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT, authorization_args=frozenset({"to"}), resource_args=frozenset({"to"}))},
            GrantAwareAuthorizer(current_time=15),
        )
        runtime.execute(ActionRequest("send", {"to": ProvenanceValue.from_source("team@example.com", source)}, 1))
        self.assertTrue(runtime.trace[0].executed)

    def test_scoped_grant_rejects_expired_scope_and_replay(self) -> None:
        grant = AuthorizationGrant(
            "g-2", "auth-service", frozenset({"update_state"}), frozenset({"*"}),
            issued_at=0, expires_at=10, nonce="n-2"
        )
        source = Provenance("user", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True, grants=(grant,))
        tool = ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT, authorization_args=frozenset({"control"}))
        runtime = ProvenanceRuntime({"send": tool}, GrantAwareAuthorizer(current_time=20))
        value = ProvenanceValue.from_source("x", source)
        runtime.execute(ActionRequest("send", {"control": value}, 1))
        self.assertFalse(runtime.trace[0].executed)

        valid = AuthorizationGrant("g-3", "auth-service", frozenset({"send"}), nonce="n-3")
        valid_source = Provenance("user2", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True, grants=(valid,))
        replay_runtime = ProvenanceRuntime({"send": tool}, GrantAwareAuthorizer(current_time=0, consume_grants=True))
        replay_value = ProvenanceValue.from_source("x", valid_source)
        replay_runtime.execute(ActionRequest("send", {"control": replay_value}, 1))
        replay_runtime.execute(ActionRequest("send", {"control": replay_value}, 2))
        self.assertTrue(replay_runtime.trace[0].executed)
        self.assertFalse(replay_runtime.trace[1].executed)

    def test_resource_handle_grant_binds_resource_version(self) -> None:
        grant = AuthorizationGrant(
            "g-resource", "auth-service", frozenset({"send"}), frozenset({"recipient@1"}), nonce="n-resource"
        )
        source = Provenance(
            "user-resource", SourceKind.USER, DeliveryChannel.USER_PROMPT,
            trusted=True, authorized=True, grants=(grant,)
        )
        runtime = ProvenanceRuntime(
            {"send": ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT, authorization_args=frozenset({"to"}), resource_args=frozenset({"to"}))},
            GrantAwareAuthorizer(current_time=0, consume_grants=False),
        )
        runtime.execute(ActionRequest("send", {"to": ProvenanceValue.from_source(ResourceHandle("recipient", 1, "team@example.com"), source)}, 1))
        runtime.execute(ActionRequest("send", {"to": ProvenanceValue.from_source(ResourceHandle("recipient", 2, "attacker@example.com"), source)}, 2))
        self.assertTrue(runtime.trace[0].executed)
        self.assertFalse(runtime.trace[1].executed)

    def test_dry_run_revalidation_does_not_consume_external_nonce(self) -> None:
        grant = AuthorizationGrant("g-dry", "auth-service", frozenset({"send"}), nonce="n-dry")
        source = Provenance(
            "user-dry", SourceKind.USER, DeliveryChannel.USER_PROMPT,
            trusted=True, authorized=True, grants=(grant,)
        )
        store = InMemoryNonceStore()
        authorizer = GrantAwareAuthorizer(current_time=0, nonce_store=store)
        tool = ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT, authorization_args=frozenset({"to"}))
        value = ProvenanceValue.from_source("team@example.com", source)
        decision = authorizer.decide(ActionRequest("send", {"to": value}, 1), tool, consume=False)
        self.assertTrue(decision.allowed)
        self.assertFalse(store.is_consumed("n-dry"))


class PairedScenarioTests(unittest.TestCase):
    def test_same_attack_is_blocked_across_delivery_channels(self) -> None:
        for scenario in paired_scenarios():
            unprotected = run_scenario(scenario, protected=False).metrics
            protected = run_scenario(scenario, protected=True).metrics
            self.assertTrue(unprotected.utility)
            self.assertTrue(unprotected.attack_success)
            self.assertTrue(unprotected.sensitive_data_leak)
            self.assertTrue(protected.utility)
            self.assertFalse(protected.attack_success)
            self.assertFalse(protected.sensitive_data_leak)
            self.assertEqual(protected.blocked_actions, 1)


if __name__ == "__main__":
    unittest.main()
