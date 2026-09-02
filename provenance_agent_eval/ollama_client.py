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

    def show_model(self, model: str) -> dict[str, object]:
        """Return identity metadata needed to reproduce a run (digest, quantization, context)."""

        request = Request(
            f"{self.base_url}/api/show",
            data=json.dumps({"model": model}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=min(self.timeout, 15.0)) as response:
                raw = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Ollama /api/show failed for {model!r}: {exc}") from exc
        details = raw.get("details", {}) if isinstance(raw.get("details"), dict) else {}
        model_info = raw.get("model_info", {}) if isinstance(raw.get("model_info"), dict) else {}
        digest = None
        for item in self._tags():
            if item.get("name") == model:
                digest = item.get("digest")
                break
        return {
            "name": model,
            "digest": digest,
            "family": details.get("family"),
            "parameter_size": details.get("parameter_size"),
            "quantization_level": details.get("quantization_level"),
            "format": details.get("format"),
            "context_length": next((value for key, value in model_info.items() if key.endswith(".context_length")), None),
            "modified_at": raw.get("modified_at"),
            "endpoint": self.base_url,
            "decode_options": {"temperature": 0, "think": False, "format": "json"},
        }

    def _tags(self) -> list[dict[str, object]]:
        request = Request(f"{self.base_url}/api/tags", method="GET")
        try:
            with urlopen(request, timeout=min(self.timeout, 10.0)) as response:
                raw = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
            return []
        models = raw.get("models", [])
        return [item for item in models if isinstance(item, dict)] if isinstance(models, list) else []

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
