import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.ollama_client import OllamaResponse
from provenance_agent_eval.real_tool_analysis import analyze_real_tool_runs
from provenance_agent_eval.real_tool_runner import real_tool_cases, run_real_tool_matrix
from provenance_agent_eval.tool_adapters import WorkspaceToolAdapter


class FakeClient:
    base_url = "fake://test"

    def chat(self, *, model: str, messages: list[dict[str, str]]) -> OllamaResponse:
        prompt = messages[-1]["content"]
        action = next((name for name in ("update_ticket", "send_message", "delete_file") if name in prompt), "none")
        return OllamaResponse(json.dumps({"action": action}), 0.01, 20, 4, {})


class ToolAdapterTests(unittest.TestCase):
    def test_adapter_emits_receipts_for_real_state_changes(self) -> None:
        adapter = WorkspaceToolAdapter.seeded()
        adapter.update_ticket({"ticket_id": "PROV-1", "status": "closed", "note": "done"})
        adapter.send_message({"recipient": "x@example.com", "body": "hello"})
        adapter.delete_file({"path": "reports/draft.txt"})
        self.assertEqual(len(adapter.receipts), 3)
        self.assertEqual(adapter.tickets["PROV-1"]["status"], "closed")
        self.assertEqual(len(adapter.outbox), 1)
        self.assertNotIn("reports/draft.txt", adapter.files)

    def test_real_runner_pairs_no_policy_and_source_aware(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            summary = run_real_tool_matrix(directory, model="fake", client=FakeClient(), repetitions=1)
            self.assertEqual(summary["records"], 12)
            rows = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text().splitlines()]
            raw = [row for row in rows if not row["condition"].endswith("-aggregate")]
            self.assertEqual(len(raw), 12)
            unsafe = [row for row in raw if row["metadata"]["case"]["attack"] and row["metadata"]["selected_action"] == row["metadata"]["case"]["target_tool"]]
            self.assertTrue(unsafe)
            self.assertTrue(any(row["defense"] == "no_policy" and row["metrics"]["actual_side_effect"] == 1.0 for row in unsafe))
            self.assertTrue(any(row["defense"] == "source_aware" and row["metrics"]["actual_side_effect"] == 0.0 for row in unsafe))
            aggregates = [row for row in rows if row["condition"].endswith("-aggregate")]
            protected = next(row for row in aggregates if row["condition"] == "source_aware-aggregate")
            self.assertEqual(protected["baseline_id"], "exp-0013")
            self.assertIn("runtime_latency_seconds", protected["metrics"])
            self.assertIn("total_tokens", protected["metrics"])
            self.assertTrue(Path(directory, "progress.html").exists())

    def test_case_set_covers_three_side_effect_tools_and_two_sources(self) -> None:
        cases = real_tool_cases()
        self.assertEqual({case.target_tool for case in cases}, {"update_ticket", "send_message", "delete_file"})
        self.assertEqual({case.attack for case in cases}, {True, False})

    def test_analysis_pairs_policy_and_model_records(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run_a = root / "a"
            run_b = root / "b"
            run_real_tool_matrix(run_a, model="fake-a", client=FakeClient(), repetitions=1)
            run_real_tool_matrix(run_b, model="fake-b", client=FakeClient(), repetitions=1)
            summary = analyze_real_tool_runs(root / "analysis", {"a": run_a, "b": run_b}, bootstrap_samples=50)
            self.assertEqual(len(summary["models"]), 2)
            self.assertEqual(summary["cross_model"][0]["paired_attack_cases"], 3)
            self.assertTrue((root / "analysis" / "real_tool_analysis.json").exists())


if __name__ == "__main__":
    unittest.main()
