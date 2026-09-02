import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.core import ActionRequest, DeliveryChannel, Provenance, ProvenanceValue, RiskLevel, SourceKind, ToolSpec
from provenance_agent_eval.cpm import DefenseMechanism, MutationOperator, MutationSchedule
from provenance_agent_eval.cpm.campaign import run_campaign, structural_rule
from provenance_agent_eval.cpm.execution import ExecutionMechanism, ExecutionOperator, ExecutionScenario, replay_execution
from provenance_agent_eval.cpm.laws import Curve, compound, fit_free, fit_structural
from provenance_agent_eval.cpm.replay import mutate_trace, replay_trace
from provenance_agent_eval.cpm.synthetic import parametric_suite, parametric_trace
from provenance_agent_eval.cpm.trace import ground_truth
from provenance_agent_eval.runtime import SourceAwareAuthorizer


class PropagationSemanticsTests(unittest.TestCase):
    def test_dropped_label_propagates_to_sink_only_when_enabled(self) -> None:
        trace = parametric_trace(depth=3, k=1, channel=0, attack=False)
        sink = trace.actions[-1].args["target_1"].node_id
        # Force the first hop of the legitimate chain to lose its label.
        schedule = MutationSchedule(MutationOperator.DROP_LABEL, 1.0, 0, propagate=True)
        observed, _, eligible, _ = mutate_trace(trace, schedule)
        self.assertIn("user:target_1", eligible)
        self.assertEqual(observed.node(sink).attached_sources, frozenset())
        # Sink-only semantics: with rate 1 every node is selected anyway, so
        # check a single-node mutation by hand.
        from provenance_agent_eval.cpm.operators import OperatorContext, apply_operator, propagate_labels
        from provenance_agent_eval.cpm.trace import build_oracle_graph

        oracle = build_oracle_graph(trace)
        root = trace.trusted_root
        context = OperatorContext(root.node_id, root.provenance, ())
        sink_only = oracle.copy()
        apply_operator(sink_only, "user:target_1", MutationOperator.DROP_LABEL, context)
        self.assertTrue(sink_only.node(sink).attached_sources)
        propagated = oracle.copy()
        apply_operator(propagated, "user:target_1", MutationOperator.DROP_LABEL, context)
        propagate_labels(propagated, pinned={"user:target_1"})
        self.assertEqual(propagated.node(sink).attached_sources, frozenset())

    def test_forged_hop_is_believed_downstream_by_labels_but_not_by_lineage(self) -> None:
        trace = parametric_trace(depth=3, k=1, channel=0, attack=True)
        schedule = MutationSchedule(MutationOperator.FORGE_LABEL, 1.0, 0, propagate=True)
        label_cell = replay_trace(trace, schedule, DefenseMechanism.LABEL_TRUSTING)
        lineage_cell = replay_trace(trace, schedule, DefenseMechanism.LINEAGE_VERIFYING)
        origin_cell = replay_trace(trace, schedule, DefenseMechanism.ORIGIN_ROUTING)
        self.assertEqual(label_cell.attack_success, 1.0)
        self.assertEqual(lineage_cell.attack_success, 0.0)
        self.assertEqual(origin_cell.attack_success, 0.0)


class PerArgumentAttributionTests(unittest.TestCase):
    def test_unlabelled_guarded_argument_is_blocked_even_with_labelled_sibling(self) -> None:
        user = Provenance("user", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True)
        spec = ToolSpec("dispatch", RiskLevel.EXTERNAL_SIDE_EFFECT, authorization_args=frozenset({"a", "b"}))
        action = ActionRequest(
            "dispatch",
            {"a": ProvenanceValue.from_source("x", user), "b": ProvenanceValue("y", frozenset())},
            1,
        )
        decision = SourceAwareAuthorizer().decide(action, spec)
        self.assertFalse(decision.allowed)
        self.assertIn("b", decision.reason)


class ParametricSuiteTests(unittest.TestCase):
    def test_ground_truth_is_root_defined(self) -> None:
        benign = parametric_trace(depth=2, k=3, channel=1, attack=False)
        attack_all = parametric_trace(depth=2, k=3, channel=1, attack=True, poisoned="all")
        attack_one = parametric_trace(depth=2, k=3, channel=1, attack=True, poisoned="one")
        for trace, expected in ((benign, True), (attack_all, False), (attack_one, False)):
            labels = ground_truth(trace)
            self.assertEqual(labels[trace.actions[-1].step], expected, trace.trace_id)
        self.assertEqual(attack_one.metadata["poisoned"], 1)
        self.assertEqual(len(parametric_suite(depths=(1, 2), ks=(1, 2), channels=2)), 16)

    def test_structural_rule_matches_design(self) -> None:
        curve = Curve("misattribute_parent", "whole_call_quarantine", "attack_success", {"propagate": True, "depth": 3, "k": 2}, {})
        self.assertEqual(structural_rule(curve)[:2], (3, 3))
        curve = Curve("drop_label", "label_trusting", "false_blocking", {"propagate": False, "depth": 3, "k": 2}, {})
        self.assertEqual(structural_rule(curve)[:2], (2, 1))
        curve = Curve("forge_label", "origin_routing", "attack_success", {"propagate": True, "depth": 3, "k": 2}, {})
        self.assertIsNone(structural_rule(curve))


class LawFittingTests(unittest.TestCase):
    def test_structural_fit_recovers_exact_compound_law(self) -> None:
        points = {p: compound(p, 3, 2) for p in (0.05, 0.1, 0.25, 0.5, 0.75, 1.0)}
        structural = fit_structural(points, 0.0, m=3, k=2, label="test")
        self.assertAlmostEqual(structural.sse, 0.0)
        self.assertEqual(structural.r2, 1.0)
        free = fit_free(points, 0.0)
        self.assertEqual((free.m, free.k), (3.0, 2.0))
        wrong = fit_structural(points, 0.0, m=1, k=1, label="wrong")
        self.assertGreater(wrong.sse, 0.05)


class ExecutionOperatorTests(unittest.TestCase):
    def test_revalidation_closes_i5_but_not_i4_and_ledger_closes_both(self) -> None:
        scenario = ExecutionScenario("t", 2, 2)
        stale = {
            mechanism: replay_execution(scenario, ExecutionOperator.STALE_VERSION, 1.0, 0, mechanism)
            for mechanism in ExecutionMechanism
        }
        self.assertTrue(all(item["side_effect"] for item in stale[ExecutionMechanism.GRANT_SINGLE_USE]["outcomes"]))
        self.assertFalse(any(item["side_effect"] for item in stale[ExecutionMechanism.GRANT_REVALIDATED]["outcomes"]))
        replay = {
            mechanism: replay_execution(scenario, ExecutionOperator.SEMANTIC_REPLAY, 1.0, 0, mechanism)
            for mechanism in ExecutionMechanism
        }
        duplicates = lambda cell: sum(item["side_effect"] for item in cell["outcomes"] if item["slot"] != "original")
        self.assertEqual(duplicates(replay[ExecutionMechanism.GRANT_REVALIDATED]), 4)
        self.assertEqual(duplicates(replay[ExecutionMechanism.INTENT_LEDGER]), 0)
        # The ledger must not block distinct legitimate originals.
        self.assertTrue(all(item["allowed"] for item in replay[ExecutionMechanism.INTENT_LEDGER]["outcomes"] if item["slot"] == "original"))


class CampaignSmokeTests(unittest.TestCase):
    def test_campaign_writes_summary_and_law_tables(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            summary = run_campaign(
                root,
                variants=1,
                seeds=1,
                rates=(0.0, 0.5, 1.0),
                bootstrap=20,
                channels=1,
                execution_copies=1,
                hypotheses=("h3", "h7"),
            )
            self.assertIn("h3_h4", summary)
            self.assertIn("h7", summary)
            self.assertTrue(Path(root, "campaign_summary.json").exists())
            self.assertTrue(Path(root, "h3h4-parametric-propagate", "laws_asr.md").exists())
            self.assertTrue(Path(root, "h7-execution", "laws_asr.md").exists())
            self.assertEqual(summary["h7"]["asr_at_1"]["stale_version"]["grant_revalidated"], 0.0)
            self.assertEqual(summary["h7"]["asr_at_1"]["semantic_replay"]["intent_ledger"], 0.0)


if __name__ == "__main__":
    unittest.main()
