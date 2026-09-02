"""Interval estimates for degradation curves.

Two rules are enforced here rather than left to discipline:

1. A rate is reported with a Wilson interval over its *cluster* units
   (traces), never over replayed cells, because cells derived from one trace
   are not independent.
2. A paired comparison whose outcome is a deterministic function of the two
   mechanisms (all discordant pairs point one way and no randomness entered
   the cell) is labelled ``by_construction`` and gets no p-value.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class RateEstimate:
    successes: int
    trials: int
    rate: float | None
    wilson_low: float | None
    wilson_high: float | None

    def as_dict(self) -> dict[str, float | int | None]:
        return {
            "successes": self.successes,
            "trials": self.trials,
            "rate": self.rate,
            "ci_low": self.wilson_low,
            "ci_high": self.wilson_high,
        }


def wilson(successes: int, trials: int, z: float = 1.959963984540054) -> RateEstimate:
    if trials <= 0:
        return RateEstimate(successes, trials, None, None, None)
    p = successes / trials
    denominator = 1 + z * z / trials
    centre = (p + z * z / (2 * trials)) / denominator
    margin = z * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials)) / denominator
    return RateEstimate(successes, trials, p, max(0.0, centre - margin), min(1.0, centre + margin))


def cluster_bootstrap_mean(
    clusters: Sequence[Sequence[float]],
    *,
    samples: int = 2000,
    seed: int = 0,
) -> tuple[float | None, float | None, float | None]:
    """Mean over all observations with a CI from resampling clusters (traces)."""

    populated = [tuple(cluster) for cluster in clusters if cluster]
    if not populated:
        return None, None, None
    generator = random.Random(seed)
    point = _mean([value for cluster in populated for value in cluster])
    estimates = []
    for _ in range(samples):
        draw = [populated[generator.randrange(len(populated))] for _ in populated]
        estimates.append(_mean([value for cluster in draw for value in cluster]))
    estimates.sort()
    low = estimates[max(0, math.floor(0.025 * samples))]
    high = estimates[min(samples - 1, math.ceil(0.975 * samples) - 1)]
    return point, low, high


@dataclass(frozen=True)
class PairedComparison:
    left_only: int
    right_only: int
    concordant: int
    by_construction: bool
    mcnemar_exact_p: float | None
    note: str

    def as_dict(self) -> dict[str, float | int | bool | str | None]:
        return {
            "discordant_left_only": self.left_only,
            "discordant_right_only": self.right_only,
            "concordant": self.concordant,
            "by_construction": self.by_construction,
            "mcnemar_exact_p": self.mcnemar_exact_p,
            "note": self.note,
        }


def paired_binary(left: Iterable[int], right: Iterable[int], *, stochastic_cell: bool) -> PairedComparison:
    """Exact McNemar for paired binary outcomes, refused when the pairing is deterministic.

    ``stochastic_cell`` must be True only when some randomness entered the
    cell being compared (e.g. a mutation schedule with 0 < rate < 1 or a
    sampled model decision).  At rate 0 or 1 the two mechanisms' outcomes on
    the same trace are a fixed function of their implementations.
    """

    pairs = list(zip(left, right))
    left_only = sum(a == 1 and b == 0 for a, b in pairs)
    right_only = sum(a == 0 and b == 1 for a, b in pairs)
    concordant = len(pairs) - left_only - right_only
    if not stochastic_cell:
        return PairedComparison(
            left_only,
            right_only,
            concordant,
            True,
            None,
            "outcomes are a deterministic function of the mechanisms on fixed traces; report counts, not p-values",
        )
    discordant = left_only + right_only
    if discordant == 0:
        return PairedComparison(left_only, right_only, concordant, False, 1.0, "no discordant pairs")
    tail = sum(math.comb(discordant, value) for value in range(0, min(left_only, right_only) + 1))
    p = min(1.0, 2.0 * tail / (2**discordant))
    return PairedComparison(left_only, right_only, concordant, False, p, "exact two-sided McNemar over discordant pairs")


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0
