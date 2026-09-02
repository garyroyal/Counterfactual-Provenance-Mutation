# Experiment Report

Generated: 2026-09-02T04:00:21+00:00

每条记录都保留原始指标；带基线的记录同时显示 delta、升降方向和改善/恶化判断。

## exp-0001 | cross-model-action-induction | `qwen3-4b-aggregate`
时间：2026-09-02T04:00:21+00:00
条件：model=qwen3-4b, scenario=paired-common-cases

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `model_attack_induction` | 0.3375 | - | - | baseline | baseline |
| `paired_observations` | 80 | - | - | baseline | baseline |

备注：Aggregate uses only case/variant pairs shared by every model run.

## exp-0002 | cross-model-action-induction | `llama32-3b-aggregate`
时间：2026-09-02T04:00:21+00:00
条件：model=llama32-3b, scenario=paired-common-cases

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `model_attack_induction` | 0.075 | - | - | baseline | baseline |
| `paired_observations` | 80 | - | - | baseline | baseline |

备注：Aggregate uses only case/variant pairs shared by every model run.

## exp-0003 | cross-model-action-induction | `qwen3-4b-vs-llama32-3b-aggregate`
时间：2026-09-02T04:00:21+00:00
条件：scenario=paired-model-difference

| 指标 | 当前值 | 基线 | Delta | 变化 | 评价 |
|---|---:|---:|---:|---|---|
| `bootstrap_ci_high` | 0.3625 | - | - | baseline | baseline |
| `bootstrap_ci_low` | 0.1625 | - | - | baseline | baseline |
| `mcnemar_exact_p` | 0 | - | - | baseline | baseline |
| `model_attack_induction_difference` | 0.2625 | - | - | baseline | baseline |
| `paired_observations` | 80 | - | - | baseline | baseline |

备注：Positive difference means the left model selected more injected actions.

