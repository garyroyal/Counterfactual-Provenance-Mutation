"""Deterministic selection of which eligible nodes a mutation touches."""

from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass

from .operators import MutationOperator


@dataclass(frozen=True)
class MutationSchedule:
    """Apply ``operator`` to a fraction ``rate`` of eligible nodes.

    Selection is a pure function of (operator, rate, seed, trace_id, eligible
    node ids) so that every defense sees exactly the same corrupted evidence
    for a given cell.  ``rate`` is the *provenance error rate* swept by the
    degradation experiment.
    """

    operator: MutationOperator
    rate: float
    seed: int = 0

    def __post_init__(self) -> None:
        if not 0.0 <= self.rate <= 1.0:
            raise ValueError("rate must lie in [0, 1]")

    def select(self, trace_id: str, eligible: tuple[str, ...]) -> tuple[str, ...]:
        if not eligible or self.rate == 0.0:
            return ()
        if self.rate == 1.0:
            return tuple(eligible)
        digest = hashlib.sha256(f"{self.operator.value}|{self.seed}|{trace_id}".encode("utf-8")).hexdigest()
        generator = random.Random(int(digest[:16], 16))
        # Bernoulli per node keeps the expected corruption rate equal to
        # ``rate`` regardless of how many eligible nodes a trace has.
        return tuple(node_id for node_id in eligible if generator.random() < self.rate)

    @property
    def label(self) -> str:
        return f"{self.operator.value}@{self.rate:g}#{self.seed}"
