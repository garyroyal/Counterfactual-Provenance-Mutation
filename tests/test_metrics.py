import unittest

from provenance_agent_eval.core import DeliveryChannel, Provenance, SourceKind
from provenance_agent_eval.metrics import (
    AuthorizationCase,
    score_authorization,
    score_graph_node,
    score_provenance,
    score_trace_authorization,
)
from provenance_agent_eval.provenance_graph import ProvenanceGraph, TransformKind
from provenance_agent_eval.runtime import TraceEvent


class MetricsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.external = Provenance("web", SourceKind.EXTERNAL_DOCUMENT, DeliveryChannel.DOCUMENT)

    def test_provenance_metrics_measure_loss_and_forgery(self) -> None:
        quality = score_provenance(expected=["web", "memory"], observed=["web", "fake"])

        self.assertEqual(quality.precision, 0.5)
        self.assertEqual(quality.recall, 0.5)
        self.assertEqual(quality.source_loss_rate, 0.5)
        self.assertEqual(quality.forgery_rate, 0.5)

    def test_graph_node_quality_exposes_laundering(self) -> None:
        graph = ProvenanceGraph()
        graph.add_source("web", self.external)
        graph.derive("lost", parents=["web"], operation=TransformKind.MEMORY_WRITE, preserve_provenance=False)
        quality = score_graph_node(graph, "lost")

        self.assertEqual(quality.recall, 0.0)
        self.assertEqual(quality.source_loss_rate, 1.0)

    def test_authorization_metrics_separate_soundness_and_completeness(self) -> None:
        quality = score_authorization(
            [
                AuthorizationCase(expected_allowed=True, actual_allowed=True),
                AuthorizationCase(expected_allowed=True, actual_allowed=False),
                AuthorizationCase(expected_allowed=False, actual_allowed=False),
                AuthorizationCase(expected_allowed=False, actual_allowed=True),
            ]
        )

        self.assertEqual(quality.completeness, 0.5)
        self.assertEqual(quality.soundness, 0.5)
        self.assertEqual(quality.false_blocking_rate, 0.5)

    def test_empty_sets_are_scored_as_vacuously_correct(self) -> None:
        quality = score_provenance([], [])
        auth = score_authorization([])
        self.assertEqual(quality.precision, 1.0)
        self.assertEqual(quality.recall, 1.0)
        self.assertEqual(auth.soundness, 1.0)
        self.assertEqual(auth.completeness, 1.0)

    def test_trace_authorization_uses_independent_step_labels(self) -> None:
        trace = [
            TraceEvent(step=1, event="tool_call", tool="read", allowed=True, executed=True),
            TraceEvent(step=2, event="authorization", tool="send", allowed=False, executed=False),
        ]
        quality = score_trace_authorization(trace, {1: True, 2: False})

        self.assertEqual(quality.soundness, 1.0)
        self.assertEqual(quality.completeness, 1.0)
        self.assertEqual(quality.false_blocking_rate, 0.0)


if __name__ == "__main__":
    unittest.main()
