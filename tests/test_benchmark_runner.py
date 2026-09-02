import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.benchmark_runner import run_benchmark_case, run_orthogonal_matrix
from provenance_agent_eval.benchmark_schema import PolicyKind, build_matrix
from provenance_agent_eval.core import RiskLevel


class BenchmarkRunnerTests(unittest.TestCase):
    def test_case_exposes_loss_and_forgery_separately(self) -> None:
        cases = build_matrix()
        loss = next(case for case in cases if case.source.name == "tool-output" and case.transform.name == "memory-loss" and case.action.name == "external-side-effect" and case.policy is PolicyKind.SOURCE_AWARE)
        forged = next(case for case in cases if case.source.name == "tool-output" and case.transform.name == "rewrite-forged-user" and case.action.name == "external-side-effect" and case.policy is PolicyKind.SOURCE_AWARE)
        loss_result = run_benchmark_case(loss)
        forged_result = run_benchmark_case(forged)

        self.assertFalse(loss_result["actual_allowed"])
        self.assertEqual(loss_result["source_loss_rate"], 1.0)
        self.assertEqual(loss_result["forgery_rate"], 0.0)
        self.assertFalse(forged_result["actual_allowed"])
        self.assertEqual(forged_result["source_loss_rate"], 1.0)
        self.assertEqual(forged_result["forgery_rate"], 1.0)

    def test_authorization_matrix_matches_ground_truth(self) -> None:
        cases = build_matrix()
        protected_mismatches = []
        baseline_unsafe_allows = 0
        for case in cases:
            result = run_benchmark_case(case)
            if case.policy is PolicyKind.SOURCE_AWARE and result["actual_allowed"] != case.expected_allowed:
                protected_mismatches.append(case.case_id)
            if case.policy is PolicyKind.NO_POLICY and not case.expected_allowed and result["actual_allowed"]:
                baseline_unsafe_allows += 1
        self.assertEqual(protected_mismatches, [])
        self.assertGreater(baseline_unsafe_allows, 0)

    def test_matrix_logs_raw_aggregate_and_visualization(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runs = run_orthogonal_matrix(directory, repetitions=1)
            records = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(runs), 96)
            self.assertEqual(len(records), 98)
            self.assertTrue(Path(directory, "progress.html").exists())
            aggregates = [record for record in records if record["condition"].endswith("-aggregate")]
            self.assertEqual(len(aggregates), 2)
            source_aware = next(record for record in aggregates if record["condition"] == "source_aware-aggregate")
            self.assertEqual(source_aware["metrics"]["authorization_soundness"], 1.0)
            self.assertEqual(source_aware["metrics"]["authorization_completeness"], 1.0)

    def test_zero_repetitions_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                run_orthogonal_matrix(directory, repetitions=0)


if __name__ == "__main__":
    unittest.main()
