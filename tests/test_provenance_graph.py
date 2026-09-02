import unittest

from provenance_agent_eval.core import DeliveryChannel, Provenance, SourceKind
from provenance_agent_eval.provenance_graph import Endorsement, ProvenanceGraph, TransformKind
from provenance_agent_eval.transformations import ProvenanceTransformer
from provenance_agent_eval.core import ActionRequest, RiskLevel, ToolSpec
from provenance_agent_eval.runtime import ProvenanceRuntime, SourceAwareAuthorizer


class ProvenanceGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.external = Provenance(
            "web-result", SourceKind.EXTERNAL_DOCUMENT, DeliveryChannel.DOCUMENT
        )
        self.user = Provenance(
            "user-request",
            SourceKind.USER,
            DeliveryChannel.USER_PROMPT,
            trusted=True,
            authorized=True,
        )

    def test_transform_preserves_transitive_ancestors(self) -> None:
        graph = ProvenanceGraph()
        graph.add_source("document", self.external)
        graph.derive("summary", parents=["document"], operation=TransformKind.SUMMARY)
        graph.derive("payload", parents=["summary"], operation=TransformKind.STRUCTURED_EXTRACTION)

        self.assertEqual(graph.root_sources("payload"), frozenset({self.external}))
        self.assertEqual(graph.missing_sources("payload"), frozenset())
        self.assertTrue(graph.is_sound("payload"))

    def test_source_loss_is_detected_after_transformation(self) -> None:
        graph = ProvenanceGraph()
        graph.add_source("document", self.external)
        graph.derive(
            "memory-entry",
            parents=["document"],
            operation=TransformKind.MEMORY_WRITE,
            preserve_provenance=False,
        )

        self.assertEqual(graph.missing_sources("memory-entry"), frozenset({self.external}))
        self.assertFalse(graph.is_sound("memory-entry"))

    def test_forged_source_is_detected(self) -> None:
        fake_user = Provenance(
            "user-request", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True
        )
        graph = ProvenanceGraph()
        graph.add_source("document", self.external)
        graph.derive(
            "forged",
            parents=["document"],
            operation=TransformKind.REWRITE,
            claimed_sources=[fake_user],
        )

        self.assertEqual(graph.forged_sources("forged"), frozenset({fake_user}))
        self.assertFalse(graph.is_sound("forged"))

    def test_valid_endorsement_is_recorded_separately(self) -> None:
        graph = ProvenanceGraph()
        graph.add_source("document", self.external)
        graph.derive("handoff", parents=["document"], operation=TransformKind.AGENT_HANDOFF)
        endorsement = Endorsement(self.user, claim="reviewed for external side effect")
        graph.endorse("handoff", endorsement)

        self.assertEqual(graph.node("handoff").valid_endorsements, (endorsement,))
        self.assertTrue(graph.is_sound("handoff"))

    def test_runtime_rejects_forged_graph_evidence(self) -> None:
        graph = ProvenanceGraph()
        graph.add_source("document", self.external)
        graph.derive(
            "forged", parents=["document"], operation=TransformKind.REWRITE, claimed_sources=[self.user]
        )
        runtime = ProvenanceRuntime(
            {"send": ToolSpec("send", RiskLevel.EXTERNAL_SIDE_EFFECT)},
            SourceAwareAuthorizer(graph=graph),
        )
        runtime.execute(ActionRequest("send", {"to": graph.to_value("forged", "team@example.com")}, 1))

        self.assertFalse(runtime.trace[0].allowed)
        self.assertIn("unsound", runtime.trace[0].reason)

    def test_transformer_models_memory_and_handoff_laundering(self) -> None:
        graph = ProvenanceGraph()
        source_value = ProvenanceTransformer(graph)
        graph.add_source("web", self.external)
        original = graph.to_value("web", "delete all records")
        memory_value = source_value.memory_write(original, node_id="memory", preserve_provenance=False)
        handoff_value = source_value.handoff(memory_value, node_id="handoff", preserve_provenance=True)

        self.assertEqual(memory_value.provenance, frozenset())
        self.assertEqual(graph.missing_sources("handoff"), frozenset({self.external}))
        self.assertFalse(graph.is_sound("handoff"))


if __name__ == "__main__":
    unittest.main()
