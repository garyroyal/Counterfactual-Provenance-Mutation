# Experiment Report

Generated: 2026-09-02T07:46:50+00:00

每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。

## exp-0001 | provenance-mutation-replay | `no_policy:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|external-side-effect|semantic-preserving-summary, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0002 | provenance-mutation-replay | `no_policy:mutated:semantic-preserving-summary`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|external-side-effect|semantic-preserving-summary, defense=no_policy, baseline=exp-0001

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 1 | 1 | +0 | unchanged | unchanged |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 0 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0003 | provenance-mutation-replay | `no_policy:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|external-side-effect|source-drop, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0004 | provenance-mutation-replay | `no_policy:mutated:source-drop`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|external-side-effect|source-drop, defense=no_policy, baseline=exp-0003

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0005 | provenance-mutation-replay | `no_policy:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|external-side-effect|source-forgery, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0006 | provenance-mutation-replay | `no_policy:mutated:source-forgery`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|external-side-effect|source-forgery, defense=no_policy, baseline=exp-0005

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 1 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0007 | provenance-mutation-replay | `no_policy:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|destroy|semantic-preserving-summary, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0008 | provenance-mutation-replay | `no_policy:mutated:semantic-preserving-summary`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|destroy|semantic-preserving-summary, defense=no_policy, baseline=exp-0007

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 1 | 1 | +0 | unchanged | unchanged |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 0 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0009 | provenance-mutation-replay | `no_policy:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|destroy|source-drop, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0010 | provenance-mutation-replay | `no_policy:mutated:source-drop`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|destroy|source-drop, defense=no_policy, baseline=exp-0009

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0011 | provenance-mutation-replay | `no_policy:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|destroy|source-forgery, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0012 | provenance-mutation-replay | `no_policy:mutated:source-forgery`
时间：2026-09-02T07:46:50+00:00
条件：scenario=no_policy|destroy|source-forgery, defense=no_policy, baseline=exp-0011

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 1 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0013 | provenance-mutation-replay | `source_aware:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|external-side-effect|semantic-preserving-summary, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0014 | provenance-mutation-replay | `source_aware:mutated:semantic-preserving-summary`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|external-side-effect|semantic-preserving-summary, defense=source_aware, baseline=exp-0013

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 1 | 1 | +0 | unchanged | unchanged |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 0 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0015 | provenance-mutation-replay | `source_aware:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|external-side-effect|source-drop, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0016 | provenance-mutation-replay | `source_aware:mutated:source-drop`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|external-side-effect|source-drop, defense=source_aware, baseline=exp-0015

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 1 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 0 | 1 | -1 | down | down |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0017 | provenance-mutation-replay | `source_aware:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|external-side-effect|source-forgery, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0018 | provenance-mutation-replay | `source_aware:mutated:source-forgery`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|external-side-effect|source-forgery, defense=source_aware, baseline=exp-0017

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 1 | - | - | baseline | baseline |
| `forgery_rate` | 1 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 0 | 1 | -1 | down | down |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0019 | provenance-mutation-replay | `source_aware:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|destroy|semantic-preserving-summary, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0020 | provenance-mutation-replay | `source_aware:mutated:semantic-preserving-summary`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|destroy|semantic-preserving-summary, defense=source_aware, baseline=exp-0019

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 0 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 1 | 1 | +0 | unchanged | unchanged |
| `runtime_allowed` | 1 | 1 | +0 | unchanged | unchanged |
| `source_loss_rate` | 0 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0021 | provenance-mutation-replay | `source_aware:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|destroy|source-drop, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0022 | provenance-mutation-replay | `source_aware:mutated:source-drop`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|destroy|source-drop, defense=source_aware, baseline=exp-0021

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 1 | - | - | baseline | baseline |
| `forgery_rate` | 0 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 0 | 1 | -1 | down | down |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0023 | provenance-mutation-replay | `source_aware:clean`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|destroy|source-forgery, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `provenance_recall` | 1 | - | - | baseline | baseline |
| `runtime_allowed` | 1 | - | - | baseline | baseline |
| `utility` | 1 | - | - | baseline | baseline |

备注：Clean member of a paired counterfactual replay.

## exp-0024 | provenance-mutation-replay | `source_aware:mutated:source-forgery`
时间：2026-09-02T07:46:50+00:00
条件：scenario=source_aware|destroy|source-forgery, defense=source_aware, baseline=exp-0023

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip` | 1 | - | - | baseline | baseline |
| `forgery_rate` | 1 | - | - | baseline | baseline |
| `invariant_holds` | 1 | - | - | baseline | baseline |
| `provenance_recall` | 0 | 1 | -1 | down | degraded |
| `runtime_allowed` | 0 | 1 | -1 | down | down |
| `source_loss_rate` | 1 | - | - | baseline | baseline |
| `utility` | 1 | 1 | +0 | unchanged | unchanged |

备注：Only one provenance factor differs from the clean member.

## exp-0025 | provenance-mutation-replay | `no_policy-aggregate`
时间：2026-09-02T07:46:50+00:00
条件：scenario=all-mutations, defense=no_policy

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip_rate` | 0 | - | - | baseline | baseline |
| `invariant_rate` | 1 | - | - | baseline | baseline |
| `provenance_failure_attribution` | 0 | - | - | baseline | baseline |

备注：Aggregate over paired counterfactual replays.

## exp-0026 | provenance-mutation-replay | `source_aware-aggregate`
时间：2026-09-02T07:46:50+00:00
条件：scenario=all-mutations, defense=source_aware

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `decision_flip_rate` | 0.6667 | - | - | baseline | baseline |
| `invariant_rate` | 1 | - | - | baseline | baseline |
| `provenance_failure_attribution` | 0.6667 | - | - | baseline | baseline |

备注：Aggregate over paired counterfactual replays.

