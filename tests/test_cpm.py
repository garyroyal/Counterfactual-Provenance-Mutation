import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.core import DeliveryChannel, Provenance, SourceKind
from provenance_agent_eval.cpm import (
    DefenseMechanism,
    MutationOperator,
    MutationSchedule,
    build_oracle_graph,
    ground_truth,
    replay_trace,
    run_degradation_sweep,
    synthetic_suite,
)
from provenance_agent_eval.cpm.operators import OperatorContext, apply_operator, eligible_nodes
from provenance_agent_eval.cpm.stats import cluster_bootstrap_mean, paired_binary, wilson
from provenance_agent_eval.cpm.trace import untrusted_node_ids
from provenance_agent_eval.provenance_graph import ProvenanceGraph, TransformKind


def _attack(template: str):
    return next(t for t in synthetic_suite(variants=1) if t.metadata["template"] == template and t.metadata["attack"])


def _benign(template: str):
    return next(t for t in synthetic_suite(variants=1) if t.metadata["template"] == template and not t.metadata["attack"])


def _context(trace, graph):
    root = trace.trusted_root
    return OperatorContext(root.node_id, root.provenance, untrusted_node_ids(trace, graph))


class GraphRewireTests(unittest.TestCase):
    def test_rewire_rejects_cycles_and_root_reparenting(self) -> None:
        graph = ProvenanceGraph()
        user = Provenance("u", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True)
        graph.add_source("root", user)
        graph.derive("a", parents=["root"], operation=TransformKind.SUMMARY)
        graph.derive("b", parents=["a"], operation=TransformKind.SUMMARY)
        with self.assertRaises(ValueError):
            graph.rewire("a", parents=["b"])
        with self.assertRaises(ValueError):
            graph.rewire("root", parents=["a"])
        clone = graph.copy()
        clone.rewire("b", attached_sources=())
        self.assertTrue(graph.node("b").attached_sources)
        self.assertFalse(clone.node("b").attached_sources)


class GroundTruthTests(unittest.TestCase):
    def test_labels_depend_only_on_true_roots(self) -> None:
        for trace in synthetic_suite(variants=2):
            graph = build_oracle_graph(trace)
            labels = ground_truth(trace, graph)
            unsafe = [step for step, ok in labels.items() if not ok]
            self.assertEqual(bool(unsafe), bool(trace.metadata["attack"]), trace.trace_id)
            # Mutating the observed evidence must not move ground truth.
            mutated = graph.copy()
            context = _context(trace, graph)
            for node_id in eligible_nodes(graph, MutationOperator.MISATTRIBUTE_PARENT, context):
                apply_operator(mutated, node_id, MutationOperator.MISATTRIBUTE_PARENT, context)
            self.assertEqual(ground_truth(trace, graph), labels)

    def test_delegated_tool_output_is_legitimate(self) -> None:
        trace = _benign("delegated_booking")
        self.assertTrue(all(ground_truth(trace).values()))


class OperatorTests(unittest.TestCase):
    def test_forge_fools_labels_but_not_lineage(self) -> None:
        trace = _attack("summarize_and_email")
        schedule = MutationSchedule(MutationOperator.FORGE_LABEL, 1.0, 0)
        self.assertEqual(replay_trace(trace, schedule, DefenseMechanism.LABEL_TRUSTING).attack_success, 1.0)
        self.assertEqual(replay_trace(trace, schedule, DefenseMechanism.LINEAGE_VERIFYING).attack_success, 0.0)
        self.assertEqual(replay_trace(trace, schedule, DefenseMechanism.ORIGIN_ROUTING).attack_success, 0.0)

    def test_misattributed_parent_fools_every_lineage_mechanism(self) -> None:
        trace = _attack("summarize_and_email")
        schedule = MutationSchedule(MutationOperator.MISATTRIBUTE_PARENT, 1.0, 0)
        for mechanism in (
            DefenseMechanism.LABEL_TRUSTING,
            DefenseMechanism.LINEAGE_VERIFYING,
            DefenseMechanism.ORIGIN_ROUTING,
            DefenseMechanism.WHOLE_CALL_QUARANTINE,
        ):
            self.assertEqual(replay_trace(trace, schedule, mechanism).attack_success, 1.0, mechanism)

    def test_drop_label_costs_utility_only_for_label_mechanisms(self) -> None:
        trace = _benign("summarize_and_email")
        schedule = MutationSchedule(MutationOperator.DROP_LABEL, 1.0, 0)
        self.assertEqual(replay_trace(trace, schedule, DefenseMechanism.LABEL_TRUSTING).false_blocking, 1.0)
        self.assertEqual(replay_trace(trace, schedule, DefenseMechanism.LINEAGE_VERIFYING).false_blocking, 1.0)
        self.assertEqual(replay_trace(trace, schedule, DefenseMechanism.ORIGIN_ROUTING).false_blocking, 0.0)

    def test_preserve_never_flips(self) -> None:
        for trace in synthetic_suite(variants=1):
            for mechanism in DefenseMechanism:
                base = replay_trace(trace, MutationSchedule(MutationOperator.PRESERVE, 0.0, 0), mechanism)
                mutated = replay_trace(trace, MutationSchedule(MutationOperator.PRESERVE, 1.0, 0), mechanism)
                self.assertEqual([o.allowed for o in base.outcomes], [o.allowed for o in mutated.outcomes], (trace.trace_id, mechanism))

    def test_merge_taint_creates_label_creep(self) -> None:
        trace = _benign("summarize_and_email")
        schedule = MutationSchedule(MutationOperator.MERGE_TAINT, 1.0, 0)
        cell = replay_trace(trace, schedule, DefenseMechanism.ORIGIN_ROUTING)
        self.assertEqual(cell.false_blocking, 1.0)

    def test_schedule_is_deterministic_and_rate_monotone(self) -> None:
        eligible = tuple(f"n{i}" for i in range(50))
        a = MutationSchedule(MutationOperator.DROP_LABEL, 0.3, 7).select("t", eligible)
        b = MutationSchedule(MutationOperator.DROP_LABEL, 0.3, 7).select("t", eligible)
        self.assertEqual(a, b)
        self.assertEqual(MutationSchedule(MutationOperator.DROP_LABEL, 0.0, 7).select("t", eligible), ())
        self.assertEqual(MutationSchedule(MutationOperator.DROP_LABEL, 1.0, 7).select("t", eligible), eligible)
        self.assertTrue(5 < len(a) < 25)


class StatsTests(unittest.TestCase):
    def test_wilson_and_bootstrap_handle_empty(self) -> None:
        self.assertIsNone(wilson(0, 0).rate)
        self.assertEqual(cluster_bootstrap_mean([]), (None, None, None))
        estimate = wilson(9, 10)
        self.assertLess(estimate.wilson_low, 0.9)
        self.assertGreaterEqual(estimate.wilson_high, 0.9)

    def test_paired_comparison_refuses_deterministic_cells(self) -> None:
        comparison = paired_binary([1, 1, 1], [0, 0, 0], stochastic_cell=False)
        self.assertTrue(comparison.by_construction)
        self.assertIsNone(comparison.mcnemar_exact_p)
        stochastic = paired_binary([1, 1, 1, 0], [0, 0, 0, 0], stochastic_cell=True)
        self.assertFalse(stochastic.by_construction)
        self.assertAlmostEqual(stochastic.mcnemar_exact_p, 0.25)


class SweepTests(unittest.TestCase):
    def test_sweep_writes_curves_and_cells(self) -> None:
        traces = synthetic_suite(variants=1, templates=("summarize_and_email", "delegated_booking"))
        with tempfile.TemporaryDirectory() as directory:
            summary = run_degradation_sweep(
                directory,
                traces,
                operators=(MutationOperator.FORGE_LABEL, MutationOperator.DROP_LABEL),
                defenses=(DefenseMechanism.LABEL_TRUSTING, DefenseMechanism.ORIGIN_ROUTING),
                rates=(0.0, 0.5, 1.0),
                seeds=2,
                bootstrap_samples=50,
            )
            self.assertTrue(Path(directory, "curves.md").exists())
            cells = [json.loads(line) for line in Path(directory, "cells.jsonl").read_text().splitlines()]
            # 2 operators x (1 + 2 + 1 schedules) x 2 defenses x 4 traces
            self.assertEqual(len(cells), 2 * 4 * 2 * 4)
            forge = summary["curves"]["forge_label"]["label_trusting"]
            self.assertEqual(forge[0]["attack_success"]["rate"], 0.0)
            self.assertEqual(forge[-1]["attack_success"]["rate"], 1.0)
            deterministic = [item for item in summary["mechanism_comparisons"] if item["rate"] in (0.0, 1.0)]
            self.assertTrue(all(item["by_construction"] for item in deterministic))
            stochastic = [item for item in summary["mechanism_comparisons"] if item["rate"] == 0.5]
            self.assertTrue(all(not item["by_construction"] for item in stochastic))


if __name__ == "__main__":
    unittest.main()
