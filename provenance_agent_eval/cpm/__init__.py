"""Counterfactual Provenance Mutation (CPM).

CPM is a measurement protocol, not a defense.  A fixed agent trace is replayed
under a controlled corruption of its provenance evidence, and the behaviour of
several enforcement mechanisms is compared against ground truth that depends
only on the *true* origin of each value.

Layers:

- ``trace``      canonical trace schema, oracle graph, root-defined ground truth
- ``operators``  single-variable mutation operators over a provenance graph
- ``schedule``   deterministic selection of which eligible nodes to mutate
- ``defenses``   mechanism-level enforcement abstractions under test
- ``replay``     trace x schedule x defense -> per-action outcomes and receipts
- ``degradation``sweeps over mutation rate and writes degradation curves
- ``stats``      interval estimates that refuse to test deterministic mappings
- ``synthetic``  mixed-trust workflow trace suite used before external backends
"""

from .operators import MutationOperator, OperatorSpec, OPERATOR_SPECS, apply_operator, eligible_nodes
from .schedule import MutationSchedule
from .trace import AgentTrace, ArgBinding, ArgRole, Derivation, SourceSpec, TraceAction, build_oracle_graph, ground_truth
from .defenses import DefenseMechanism, make_authorizer
from .replay import ActionOutcome, ReplayCell, replay_trace
from .degradation import run_degradation_sweep
from .synthetic import synthetic_suite

__all__ = [
    "MutationOperator",
    "OperatorSpec",
    "OPERATOR_SPECS",
    "apply_operator",
    "eligible_nodes",
    "MutationSchedule",
    "AgentTrace",
    "ArgBinding",
    "ArgRole",
    "Derivation",
    "SourceSpec",
    "TraceAction",
    "build_oracle_graph",
    "ground_truth",
    "DefenseMechanism",
    "make_authorizer",
    "ActionOutcome",
    "ReplayCell",
    "replay_trace",
    "run_degradation_sweep",
    "synthetic_suite",
]
