"""Atomic single-use nonce stores for local and multi-process runtimes."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from threading import Lock
from typing import Iterable


class InMemoryNonceStore:
    """Process-local atomic nonce store used as a reference implementation."""

    def __init__(self) -> None:
        self._consumed: set[str] = set()
        self._lock = Lock()

    def is_consumed(self, nonce: str) -> bool:
        with self._lock:
            return nonce in self._consumed

    def claim(self, nonces: Iterable[str]) -> bool:
        items = tuple(dict.fromkeys(nonce for nonce in nonces if nonce))
        with self._lock:
            if any(nonce in self._consumed for nonce in items):
                return False
            self._consumed.update(items)
            return True


class SQLiteNonceStore:
    """Cross-process atomic nonce store backed by a SQLite transaction."""

    def __init__(self, path: str | Path) -> None:
        self.path = str(path)
        parent = Path(self.path).parent
        parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path, timeout=30) as connection:
            connection.execute("CREATE TABLE IF NOT EXISTS consumed_nonces (nonce TEXT PRIMARY KEY)")
            connection.commit()

    def is_consumed(self, nonce: str) -> bool:
        with sqlite3.connect(self.path, timeout=30) as connection:
            row = connection.execute(
                "SELECT 1 FROM consumed_nonces WHERE nonce = ? LIMIT 1", (nonce,)
            ).fetchone()
        return row is not None

    def claim(self, nonces: Iterable[str]) -> bool:
        items = tuple(dict.fromkeys(nonce for nonce in nonces if nonce))
        if not items:
            return False
        connection = sqlite3.connect(self.path, timeout=30, isolation_level=None)
        try:
            connection.execute("BEGIN IMMEDIATE")
            placeholders = ",".join("?" for _ in items)
            row = connection.execute(
                f"SELECT COUNT(*) FROM consumed_nonces WHERE nonce IN ({placeholders})", items
            ).fetchone()
            if row is not None and int(row[0]) > 0:
                connection.execute("ROLLBACK")
                return False
            connection.executemany(
                "INSERT INTO consumed_nonces(nonce) VALUES (?)", ((nonce,) for nonce in items)
            )
            connection.execute("COMMIT")
            return True
        except Exception:
            connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()


class RedisNonceStore:
    """Cross-process atomic nonce store backed by Redis and a Lua script."""

    _CLAIM_SCRIPT = """
    for _, key in ipairs(KEYS) do
        if redis.call('EXISTS', key) == 1 then
            return 0
        end
    end
    for _, key in ipairs(KEYS) do
        redis.call('SET', key, '1')
    end
    return 1
    """

    def __init__(self, url: str = "redis://127.0.0.1:6379/0", *, key_prefix: str = "provenance:nonce:", client: object = None) -> None:
        if client is None:
            try:
                import redis
            except ImportError as exc:
                raise RuntimeError("RedisNonceStore requires redis-py; install with pip install redis") from exc
            client = redis.Redis.from_url(url, decode_responses=True)
        self.client = client
        self.key_prefix = key_prefix
        self.url = url

    def _key(self, nonce: str) -> str:
        return f"{self.key_prefix}{nonce}"

    def is_consumed(self, nonce: str) -> bool:
        return bool(self.client.exists(self._key(nonce)))

    def claim(self, nonces: Iterable[str]) -> bool:
        items = tuple(dict.fromkeys(nonce for nonce in nonces if nonce))
        if not items:
            return False
        keys = [self._key(nonce) for nonce in items]
        result = self.client.eval(self._CLAIM_SCRIPT, len(keys), *keys)
        return bool(int(result))
