# Experiment Report

Generated: 2026-09-02T02:09:19+00:00

每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。

## exp-0001 | composed-attack-matrix | `no_policy`
时间：2026-09-02T02:09:19+00:00
条件：scenario=laundering_chain, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 2 | - | - | baseline | baseline |
| `attack_blocked_steps` | 0 | - | - | baseline | baseline |
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_executed_steps` | 2 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0002 | composed-attack-matrix | `grant_aware`
时间：2026-09-02T02:09:19+00:00
条件：scenario=laundering_chain, defense=grant_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 2 | - | - | baseline | baseline |
| `attack_blocked_steps` | 2 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 2 | - | - | baseline | baseline |
| `executed_actions` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0003 | composed-attack-matrix | `grant_aware_revalidated`
时间：2026-09-02T02:09:19+00:00
条件：scenario=laundering_chain, defense=grant_aware_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 2 | - | - | baseline | baseline |
| `attack_blocked_steps` | 2 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 2 | - | - | baseline | baseline |
| `executed_actions` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0004 | composed-attack-matrix | `no_policy`
时间：2026-09-02T02:09:19+00:00
条件：scenario=grant_replay_chain, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 0 | - | - | baseline | baseline |
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_executed_steps` | 1 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 1 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0005 | composed-attack-matrix | `grant_aware`
时间：2026-09-02T02:09:19+00:00
条件：scenario=grant_replay_chain, defense=grant_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 1 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 1 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0006 | composed-attack-matrix | `grant_aware_revalidated`
时间：2026-09-02T02:09:19+00:00
条件：scenario=grant_replay_chain, defense=grant_aware_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 1 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 1 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0007 | composed-attack-matrix | `no_policy`
时间：2026-09-02T02:09:19+00:00
条件：scenario=scope_escalation_chain, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 0 | - | - | baseline | baseline |
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_executed_steps` | 1 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0008 | composed-attack-matrix | `grant_aware`
时间：2026-09-02T02:09:19+00:00
条件：scenario=scope_escalation_chain, defense=grant_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 1 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 1 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0009 | composed-attack-matrix | `grant_aware_revalidated`
时间：2026-09-02T02:09:19+00:00
条件：scenario=scope_escalation_chain, defense=grant_aware_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 1 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 1 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0010 | composed-attack-matrix | `no_policy`
时间：2026-09-02T02:09:19+00:00
条件：scenario=resource_substitution_race, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 1 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 0 | - | - | baseline | baseline |
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_executed_steps` | 1 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 1 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0011 | composed-attack-matrix | `grant_aware`
时间：2026-09-02T02:09:19+00:00
条件：scenario=resource_substitution_race, defense=grant_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 1 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 0 | - | - | baseline | baseline |
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_executed_steps` | 1 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 1 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0012 | composed-attack-matrix | `grant_aware_revalidated`
时间：2026-09-02T02:09:19+00:00
条件：scenario=resource_substitution_race, defense=grant_aware_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 1 | - | - | baseline | baseline |
| `attack_attempted_steps` | 1 | - | - | baseline | baseline |
| `attack_blocked_steps` | 1 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `executed_actions` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0013 | composed-attack-matrix | `no_policy`
时间：2026-09-02T02:09:19+00:00
条件：scenario=cross_agent_handoff_chain, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 2 | - | - | baseline | baseline |
| `attack_blocked_steps` | 0 | - | - | baseline | baseline |
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_executed_steps` | 2 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0014 | composed-attack-matrix | `grant_aware`
时间：2026-09-02T02:09:19+00:00
条件：scenario=cross_agent_handoff_chain, defense=grant_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 2 | - | - | baseline | baseline |
| `attack_blocked_steps` | 2 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 2 | - | - | baseline | baseline |
| `executed_actions` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0015 | composed-attack-matrix | `grant_aware_revalidated`
时间：2026-09-02T02:09:19+00:00
条件：scenario=cross_agent_handoff_chain, defense=grant_aware_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `argument_drift_events` | 0 | - | - | baseline | baseline |
| `attack_attempted_steps` | 2 | - | - | baseline | baseline |
| `attack_blocked_steps` | 2 | - | - | baseline | baseline |
| `attack_blocking_rate` | 1 | - | - | baseline | baseline |
| `attack_executed_steps` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 2 | - | - | baseline | baseline |
| `executed_actions` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `grant_reuse_count` | 0 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0 | - | - | baseline | baseline |

备注：Multi-step attack trace; model mediation is intentionally omitted.

## exp-0016 | composed-attack-matrix | `no_policy-aggregate`
时间：2026-09-02T02:09:19+00:00
条件：scenario=all-composed-attacks, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `partial_execution_rate` | 0 | - | - | baseline | baseline |
| `stale_evidence_acceptance` | 0.2 | - | - | baseline | baseline |

备注：Aggregate over composed traces; inspect raw traces for partial execution and race behavior.

## exp-0017 | composed-attack-matrix | `grant_aware-aggregate`
时间：2026-09-02T02:09:19+00:00
条件：scenario=all-composed-attacks, defense=grant_aware, baseline=exp-0016

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0.8 | 0 | +0.8 | up | improved |
| `attack_execution_rate` | 0.2 | 1 | -0.8 | down | improved |
| `authorization_completeness` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_soundness` | 0.8 | 0 | +0.8 | up | improved |
| `partial_execution_rate` | 0.4 | 0 | +0.4 | up | degraded |
| `stale_evidence_acceptance` | 0.2 | 0.2 | +0 | unchanged | unchanged |

备注：Aggregate over composed traces; inspect raw traces for partial execution and race behavior.

## exp-0018 | composed-attack-matrix | `grant_aware_revalidated-aggregate`
时间：2026-09-02T02:09:19+00:00
条件：scenario=all-composed-attacks, defense=grant_aware_revalidated, baseline=exp-0016

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 1 | 0 | +1 | up | improved |
| `attack_execution_rate` | 0 | 1 | -1 | down | improved |
| `authorization_completeness` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_soundness` | 1 | 0 | +1 | up | improved |
| `partial_execution_rate` | 0.4 | 0 | +0.4 | up | degraded |
| `stale_evidence_acceptance` | 0 | 0.2 | -0.2 | down | improved |

备注：Aggregate over composed traces; inspect raw traces for partial execution and race behavior.

