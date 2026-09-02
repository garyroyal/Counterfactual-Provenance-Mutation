import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.visualization import render_dashboard, write_dashboard


class VisualizationTests(unittest.TestCase):
    def test_real_tool_dashboard_exposes_side_effect_and_false_block_metrics(self) -> None:
        output = render_dashboard([
            {
                "record_id": "exp-1",
                "experiment": "real-tool-e2e",
                "condition": "no_policy-aggregate",
                "scenario": "real-tool-sandbox",
                "metrics": {
                    "utility": 1.0,
                    "runtime_attack_success": 0.5,
                    "actual_side_effect": 0.75,
                    "false_blocking_rate": 0.0,
                },
            }
        ])
        self.assertIn("Real tool adapter end-to-end outcomes", output)
        self.assertIn("actual_side_effect", output)
        self.assertIn("false_blocking_rate", output)

    def test_dashboard_is_derived_from_experiment_log(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "experiments.jsonl")
            path.write_text(
                json.dumps(
                    {
                        "record_id": "exp-0001",
                        "condition": "no-authorization-aggregate",
                        "scenario": "memory",
                        "metrics": {"utility": 1, "attack_success": 1, "sensitive_data_leak": 1, "blocked_actions": 0},
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            output = write_dashboard(directory)
            content = output.read_text(encoding="utf-8")
            self.assertIn("Provenance experiment progress", content)
            self.assertIn("memory", content)
            self.assertIn("unsafe action or data leak", content)

    def test_generalized_attack_dashboard_uses_attack_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "experiments.jsonl").write_text(
                json.dumps({
                    "record_id": "exp-0001",
                    "experiment": "generalized-attack-matrix",
                    "condition": "source_aware|authorization-aggregate",
                    "scenario": "stage:authorization",
                    "metrics": {
                        "attack_execution_rate": 0.5,
                        "attack_blocking_rate": 0.5,
                        "authorization_soundness": 0.5,
                    },
                }) + "\n",
                encoding="utf-8",
            )
            content = write_dashboard(directory).read_text(encoding="utf-8")
            self.assertIn("Generalized attack coverage and outcomes", content)
            self.assertIn("attack_execution_rate", content)

    def test_composed_dashboard_exposes_partial_and_stale_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "experiments.jsonl").write_text(
                json.dumps({
                    "record_id": "exp-0001",
                    "experiment": "composed-attack-matrix",
                    "condition": "grant_aware-aggregate",
                    "scenario": "all-composed-attacks",
                    "metrics": {
                        "attack_execution_rate": 0.2,
                        "attack_blocking_rate": 0.8,
                        "partial_execution_rate": 0.4,
                        "stale_evidence_acceptance": 0.2,
                    },
                }) + "\n",
                encoding="utf-8",
            )
            content = write_dashboard(directory).read_text(encoding="utf-8")
            self.assertIn("Composed attack traces and outcomes", content)
            self.assertIn("partial_execution_rate", content)
            self.assertIn("stale_evidence_acceptance", content)

    def test_concurrency_dashboard_exposes_replay_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "experiments.jsonl").write_text(
                json.dumps({
                    "record_id": "exp-0001",
                    "experiment": "concurrent-grant-matrix",
                    "condition": "grant_aware_atomic-aggregate",
                    "scenario": "all-concurrent-grant-attacks",
                    "metrics": {
                        "attack_execution_rate": 0,
                        "attack_blocking_rate": 0.5,
                        "successful_grant_replays": 0,
                        "authorization_soundness": 1,
                    },
                }) + "\n",
                encoding="utf-8",
            )
            content = write_dashboard(directory).read_text(encoding="utf-8")
            self.assertIn("Concurrent grant consumption and replay", content)
            self.assertIn("grant replays", content)

    def test_replay_violation_is_flagged_in_issue_table(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "experiments.jsonl").write_text(
                json.dumps({
                    "record_id": "exp-0001",
                    "experiment": "cross-process-grant-matrix",
                    "condition": "process_local_atomic",
                    "scenario": "single_use_grant_cross_process_replay",
                    "metrics": {"replay_violation": 1, "successful_grant_replays": 1},
                }) + "\n",
                encoding="utf-8",
            )
            content = write_dashboard(directory).read_text(encoding="utf-8")
            self.assertIn("single-use grant replay executed", content)

    def test_factorial_analysis_dashboard_uses_presentation_rates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "experiments.jsonl").write_text(
                json.dumps({
                    "record_id": "exp-0001",
                    "experiment": "factorial-presentation-analysis",
                    "condition": "qwen3-4b|presentation:direct-aggregate",
                    "scenario": "presentation:direct",
                    "metrics": {"model_attack_induction": 0.3},
                }) + "\n",
                encoding="utf-8",
            )
            content = write_dashboard(directory).read_text(encoding="utf-8")
            self.assertIn("Orthogonal presentation and runtime policy analysis", content)
            self.assertIn("model_attack_induction", content)

    def test_cross_process_dashboard_exposes_process_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "experiments.jsonl").write_text(
                json.dumps({
                    "record_id": "exp-0001",
                    "experiment": "cross-process-grant-matrix",
                    "condition": "sqlite_atomic-aggregate",
                    "scenario": "all-cross-process-grant-attacks",
                    "metrics": {
                        "attack_execution_rate": 0,
                        "attack_blocking_rate": 0.5,
                        "successful_grant_replays": 0,
                        "authorization_soundness": 1,
                    },
                }) + "\n",
                encoding="utf-8",
            )
            content = write_dashboard(directory).read_text(encoding="utf-8")
            self.assertIn("Cross-process grant consumption and replay", content)
            self.assertIn("grant replays", content)


if __name__ == "__main__":
    unittest.main()
