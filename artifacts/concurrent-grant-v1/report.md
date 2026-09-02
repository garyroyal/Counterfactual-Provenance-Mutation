# Experiment Report

Generated: 2026-09-02T02:30:20+00:00

每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。

## exp-0001 | concurrent-grant-matrix | `no_policy`
时间：2026-09-02T02:30:20+00:00
条件：scenario=single_use_grant_concurrent_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `concurrent_attempts` | 2 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `replay_violation` | 1 | - | - | baseline | baseline |
| `successful_grant_replays` | 1 | - | - | baseline | baseline |

备注：Two worker threads submit one single-use grant concurrently.

## exp-0002 | concurrent-grant-matrix | `grant_aware_racey`
时间：2026-09-02T02:30:20+00:00
条件：scenario=single_use_grant_concurrent_replay, defense=grant_aware_racey

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `concurrent_attempts` | 2 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `partial_execution` | 0 | - | - | baseline | baseline |
| `replay_violation` | 1 | - | - | baseline | baseline |
| `successful_grant_replays` | 1 | - | - | baseline | baseline |

备注：Two worker threads submit one single-use grant concurrently.

## exp-0003 | concurrent-grant-matrix | `grant_aware_atomic`
时间：2026-09-02T02:30:20+00:00
条件：scenario=single_use_grant_concurrent_replay, defense=grant_aware_atomic

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0.5 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `concurrent_attempts` | 2 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `partial_execution` | 1 | - | - | baseline | baseline |
| `replay_violation` | 0 | - | - | baseline | baseline |
| `successful_grant_replays` | 0 | - | - | baseline | baseline |

备注：Two worker threads submit one single-use grant concurrently.

## exp-0004 | concurrent-grant-matrix | `grant_aware_racey-aggregate`
时间：2026-09-02T02:30:20+00:00
条件：scenario=all-concurrent-grant-attacks, defense=grant_aware_racey, baseline=exp-0001

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | 0 | +0 | unchanged | unchanged |
| `attack_execution_rate` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_completeness` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_soundness` | 0 | 0 | +0 | unchanged | unchanged |
| `partial_execution` | 0 | 0 | +0 | unchanged | unchanged |
| `successful_grant_replays` | 1 | 1 | +0 | unchanged | unchanged |

备注：Policy comparison against the no-policy concurrent baseline.

## exp-0005 | concurrent-grant-matrix | `grant_aware_atomic-aggregate`
时间：2026-09-02T02:30:20+00:00
条件：scenario=all-concurrent-grant-attacks, defense=grant_aware_atomic, baseline=exp-0001

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0.5 | 0 | +0.5 | up | improved |
| `attack_execution_rate` | 0 | 1 | -1 | down | improved |
| `authorization_completeness` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_soundness` | 1 | 0 | +1 | up | improved |
| `partial_execution` | 1 | 0 | +1 | up | up |
| `successful_grant_replays` | 0 | 1 | -1 | down | improved |

备注：Policy comparison against the no-policy concurrent baseline.

