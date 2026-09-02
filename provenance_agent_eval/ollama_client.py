"""Minimal standard-library Ollama client used by the model evaluation layer."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class OllamaResponse:
    content: str
    latency_seconds: float
    prompt_tokens: int | None
    completion_tokens: int | None
    raw: dict[str, object]


class OllamaClient:
    def __init__(self, base_url: str = "http://127.0.0.1:11434", timeout: float = 180.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def list_models(self) -> tuple[str, ...]:
        request = Request(f"{self.base_url}/api/tags", method="GET")
        try:
            with urlopen(request, timeout=min(self.timeout, 10.0)) as response:
                raw = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Ollama endpoint unavailable at {self.base_url}: {exc}") from exc
        models = raw.get("models", [])
        if not isinstance(models, list):
            return ()
        return tuple(
            str(item.get("name"))
            for item in models
            if isinstance(item, dict) and item.get("name")
        )

    def require_model(self, model: str) -> None:
        available = self.list_models()
        if model not in available:
            raise RuntimeError(
                f"Model {model!r} is not available at {self.base_url}; "
                f"available models: {', '.join(available) or '(none)'}"
            )

    def chat(self, *, model: str, messages: list[dict[str, str]]) -> OllamaResponse:
        payload = {
            "model": model,
            "stream": False,
            "think": False,
            "format": "json",
            "options": {"temperature": 0},
            "messages": messages,
        }
        request = Request(
            f"{self.base_url}/api/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        started = time.perf_counter()
        try:
            with urlopen(request, timeout=self.timeout) as response:
                raw = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Ollama request failed: {exc}") from exc
        message = raw.get("message", {})
        content = str(message.get("content", "")) if isinstance(message, dict) else ""
        return OllamaResponse(
            content=content,
            latency_seconds=time.perf_counter() - started,
            prompt_tokens=_optional_int(raw.get("prompt_eval_count")),
            completion_tokens=_optional_int(raw.get("eval_count")),
            raw=raw,
        )


def _optional_int(value: object) -> int | None:
    return int(value) if isinstance(value, (int, float)) else None
