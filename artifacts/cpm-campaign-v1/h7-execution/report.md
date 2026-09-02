# Experiment Report

Generated: 2026-09-02T12:05:42+00:00

每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。

## exp-0001 | cpm-execution-degradation | `stale_version|no_policy|rate:0`
时间：2026-09-02T12:05:40+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0002 | cpm-execution-degradation | `stale_version|grant_single_use|rate:0`
时间：2026-09-02T12:05:40+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0003 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:0`
时间：2026-09-02T12:05:40+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0004 | cpm-execution-degradation | `stale_version|intent_ledger|rate:0`
时间：2026-09-02T12:05:40+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0005 | cpm-execution-degradation | `stale_version|no_policy|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.1042 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 26 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0006 | cpm-execution-degradation | `stale_version|grant_single_use|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.1042 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 26 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0007 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.0767 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0008 | cpm-execution-degradation | `stale_version|intent_ledger|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.0767 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0009 | cpm-execution-degradation | `stale_version|no_policy|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.2167 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 58 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0010 | cpm-execution-degradation | `stale_version|grant_single_use|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.2167 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 58 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0011 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.1661 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0012 | cpm-execution-degradation | `stale_version|intent_ledger|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.1661 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0013 | cpm-execution-degradation | `stale_version|no_policy|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.55 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 168 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0014 | cpm-execution-degradation | `stale_version|grant_single_use|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.55 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 168 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0015 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.4537 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0016 | cpm-execution-degradation | `stale_version|intent_ledger|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.4537 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0017 | cpm-execution-degradation | `stale_version|no_policy|rate:0.5`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.8083 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 316 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0018 | cpm-execution-degradation | `stale_version|grant_single_use|rate:0.5`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.8083 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 316 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0019 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:0.5`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.7218 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0020 | cpm-execution-degradation | `stale_version|intent_ledger|rate:0.5`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.7218 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0021 | cpm-execution-degradation | `stale_version|no_policy|rate:0.75`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.925 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 470 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0022 | cpm-execution-degradation | `stale_version|grant_single_use|rate:0.75`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.925 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 470 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0023 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:0.75`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.8231 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0024 | cpm-execution-degradation | `stale_version|intent_ledger|rate:0.75`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0.8231 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0025 | cpm-execution-degradation | `stale_version|no_policy|rate:1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 1 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 120 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0026 | cpm-execution-degradation | `stale_version|grant_single_use|rate:1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 1 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 120 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0027 | cpm-execution-degradation | `stale_version|grant_revalidated|rate:1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0028 | cpm-execution-degradation | `stale_version|intent_ledger|rate:1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:stale_version, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0029 | cpm-execution-degradation | `semantic_replay|no_policy|rate:0`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0030 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:0`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0031 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:0`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0032 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:0`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0033 | cpm-execution-degradation | `semantic_replay|no_policy|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.2583 | - | - | baseline | baseline |
| `duplicate_effects` | 74 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0034 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.2583 | - | - | baseline | baseline |
| `duplicate_effects` | 74 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0035 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.2583 | - | - | baseline | baseline |
| `duplicate_effects` | 74 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0036 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:0.05`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.05 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0037 | cpm-execution-degradation | `semantic_replay|no_policy|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.3542 | - | - | baseline | baseline |
| `duplicate_effects` | 117 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0038 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.3542 | - | - | baseline | baseline |
| `duplicate_effects` | 117 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0039 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.3542 | - | - | baseline | baseline |
| `duplicate_effects` | 117 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0040 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:0.1`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0041 | cpm-execution-degradation | `semantic_replay|no_policy|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.6708 | - | - | baseline | baseline |
| `duplicate_effects` | 300 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0042 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.6708 | - | - | baseline | baseline |
| `duplicate_effects` | 300 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0043 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.6708 | - | - | baseline | baseline |
| `duplicate_effects` | 300 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0044 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:0.25`
时间：2026-09-02T12:05:41+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.25 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0045 | cpm-execution-degradation | `semantic_replay|no_policy|rate:0.5`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.8792 | - | - | baseline | baseline |
| `duplicate_effects` | 620 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0046 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:0.5`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.8792 | - | - | baseline | baseline |
| `duplicate_effects` | 620 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0047 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:0.5`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.8792 | - | - | baseline | baseline |
| `duplicate_effects` | 620 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0048 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:0.5`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.5 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0049 | cpm-execution-degradation | `semantic_replay|no_policy|rate:0.75`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.9542 | - | - | baseline | baseline |
| `duplicate_effects` | 908 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0050 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:0.75`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.9542 | - | - | baseline | baseline |
| `duplicate_effects` | 908 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0051 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:0.75`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0.9542 | - | - | baseline | baseline |
| `duplicate_effects` | 908 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0052 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:0.75`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 0.75 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0053 | cpm-execution-degradation | `semantic_replay|no_policy|rate:1`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 1 | - | - | baseline | baseline |
| `duplicate_effects` | 240 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0054 | cpm-execution-degradation | `semantic_replay|grant_single_use|rate:1`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=grant_single_use

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 1 | - | - | baseline | baseline |
| `duplicate_effects` | 240 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0055 | cpm-execution-degradation | `semantic_replay|grant_revalidated|rate:1`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=grant_revalidated

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 1 | - | - | baseline | baseline |
| `duplicate_effects` | 240 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

## exp-0056 | cpm-execution-degradation | `semantic_replay|intent_ledger|rate:1`
时间：2026-09-02T12:05:42+00:00
条件：scenario=operator:semantic_replay, defense=intent_ledger

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `attack_success` | 0 | - | - | baseline | baseline |
| `duplicate_effects` | 0 | - | - | baseline | baseline |
| `false_blocking_rate` | 0 | - | - | baseline | baseline |
| `rate` | 1 | - | - | baseline | baseline |
| `stale_effects` | 0 | - | - | baseline | baseline |

备注：Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.

