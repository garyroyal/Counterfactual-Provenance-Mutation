import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.mutation_benchmark import run_mutation_benchmark


class MutationBenchmarkTests(unittest.TestCase):
    def test_counterfactual_invariants_and_attribution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pairs = run_mutation_benchmark(directory)
            self.assertEqual(len(pairs), 12)
            protected = [pair for pair in pairs if pair.policy.value == "source_aware"]
            self.assertTrue(all(pair.invariant_holds for pair in protected))
            self.assertTrue(all(pair.attribution_stage == "provenance" for pair in protected if pair.mutation != "semantic-preserving-summary"))
            summary = next(pair for pair in protected if pair.mutation == "semantic-preserving-summary")
            self.assertFalse(summary.decision_flip)
            records = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text().splitlines()]
            self.assertTrue(any(record["experiment"] == "provenance-mutation-replay" and record["condition"] == "source_aware-aggregate" for record in records))
            self.assertTrue(Path(directory, "progress.html").exists())


if __name__ == "__main__":
    unittest.main()
