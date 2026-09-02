# Experiment Report

Generated: 2026-09-02T03:04:15+00:00

每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。

## exp-0001 | redis-cross-process-grant-matrix | `no_policy`
时间：2026-09-02T03:04:15+00:00
条件：scenario=single_use_grant_redis_cross_process_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `cross_process_attempts` | 2 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `replay_violation` | 1 | - | - | baseline | baseline |
| `successful_grant_replays` | 1 | - | - | baseline | baseline |

备注：Two independent worker processes submit one single-use grant against a Redis-backed store.

## exp-0002 | redis-cross-process-grant-matrix | `process_local_atomic`
时间：2026-09-02T03:04:15+00:00
条件：scenario=single_use_grant_redis_cross_process_replay, defense=process_local_atomic

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | - | - | baseline | baseline |
| `attack_execution_rate` | 1 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 0 | - | - | baseline | baseline |
| `blocked_actions` | 0 | - | - | baseline | baseline |
| `cross_process_attempts` | 2 | - | - | baseline | baseline |
| `executed_actions` | 2 | - | - | baseline | baseline |
| `replay_violation` | 1 | - | - | baseline | baseline |
| `successful_grant_replays` | 1 | - | - | baseline | baseline |

备注：Two independent worker processes submit one single-use grant against a Redis-backed store.

## exp-0003 | redis-cross-process-grant-matrix | `redis_atomic`
时间：2026-09-02T03:04:15+00:00
条件：scenario=single_use_grant_redis_cross_process_replay, defense=redis_atomic

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0.5 | - | - | baseline | baseline |
| `attack_execution_rate` | 0 | - | - | baseline | baseline |
| `authorization_completeness` | 1 | - | - | baseline | baseline |
| `authorization_soundness` | 1 | - | - | baseline | baseline |
| `blocked_actions` | 1 | - | - | baseline | baseline |
| `cross_process_attempts` | 2 | - | - | baseline | baseline |
| `executed_actions` | 1 | - | - | baseline | baseline |
| `replay_violation` | 0 | - | - | baseline | baseline |
| `successful_grant_replays` | 0 | - | - | baseline | baseline |

备注：Two independent worker processes submit one single-use grant against a Redis-backed store.

## exp-0004 | redis-cross-process-grant-matrix | `process_local_atomic-aggregate`
时间：2026-09-02T03:04:15+00:00
条件：scenario=all-redis-cross-process-grant-attacks, defense=process_local_atomic, baseline=exp-0001

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0 | 0 | +0 | unchanged | unchanged |
| `attack_execution_rate` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_completeness` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_soundness` | 0 | 0 | +0 | unchanged | unchanged |
| `successful_grant_replays` | 1 | 1 | +0 | unchanged | unchanged |

备注：Policy comparison against the no-policy Redis cross-process baseline.

## exp-0005 | redis-cross-process-grant-matrix | `redis_atomic-aggregate`
时间：2026-09-02T03:04:15+00:00
条件：scenario=all-redis-cross-process-grant-attacks, defense=redis_atomic, baseline=exp-0001

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_blocking_rate` | 0.5 | 0 | +0.5 | up | improved |
| `attack_execution_rate` | 0 | 1 | -1 | down | improved |
| `authorization_completeness` | 1 | 1 | +0 | unchanged | unchanged |
| `authorization_soundness` | 1 | 0 | +1 | up | improved |
| `successful_grant_replays` | 0 | 1 | -1 | down | improved |

备注：Policy comparison against the no-policy Redis cross-process baseline.

