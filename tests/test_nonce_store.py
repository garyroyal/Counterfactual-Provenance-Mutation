import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.nonce_store import InMemoryNonceStore, SQLiteNonceStore


class NonceStoreTests(unittest.TestCase):
    def test_in_memory_claim_is_single_use(self) -> None:
        store = InMemoryNonceStore()
        self.assertTrue(store.claim(["n1"]))
        self.assertFalse(store.claim(["n1"]))
        self.assertTrue(store.is_consumed("n1"))

    def test_sqlite_claim_is_single_use(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteNonceStore(Path(directory) / "nonces.sqlite3")
            self.assertTrue(store.claim(["n1", "n2"]))
            self.assertFalse(store.claim(["n2"]))
            self.assertTrue(store.is_consumed("n1"))


if __name__ == "__main__":
    unittest.main()
