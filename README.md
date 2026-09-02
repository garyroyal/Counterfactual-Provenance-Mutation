# Counterfactual Provenance Mutation (CPM) / ProvenanceBench

工具型 LLM Agent 的 **provenance-fidelity 压力测试协议**。CPM 在固定的 agent 轨迹上以受控比例破坏 provenance 证据（丢失、伪造、归因错误、taint 合并），对多类 provenance-based 授权机制做配对重放，输出攻击成功率与合法任务误阻断率随 provenance 错误率的退化曲线、阶段归因和不变量违反。它是测量协议，不是新的防御。

- 架构与路线图：[ARCHITECTURE.md](ARCHITECTURE.md)
- 文献边界：[INNOVATION_AUDIT_2026.md](INNOVATION_AUDIT_2026.md)
- 历史研究记录：[RESEARCH_SUMMARY.md](RESEARCH_SUMMARY.md)

## CPM 主线

**规律战役（论文主结果）**：假设 H1–H7 的全部实验与拟合，一条命令：

```bash
cd provenance_agent_eval
PYTHONPATH=. python3 -m unittest discover -s tests
PYTHONPATH=. python3 -m provenance_agent_eval.cpm_campaign --root artifacts/cpm-campaign-v1 \
  --channels 12 \
  --model-run qwen3-4b=artifacts/cpm-model-traces-qwen3-4b-v1 \
  --model-run qwen3-8b=artifacts/cpm-model-traces-qwen3-8b-4090-disclosure-v1 \
  --model-run llama31-8b=artifacts/cpm-model-traces-llama31-8b-4090-disclosure-v1
# 输出：campaign_summary.json + 每个假设一个 sweep 目录（cells.jsonl.gz / curves.* / laws_asr.md / laws_fbr.md）
# 只重跑一个假设（结果合并进已有 summary）：--hypotheses h3
```

假设、设计、拟合出的规律与判定见 [RESULTS.md](RESULTS.md)。

其他入口：

```bash
# operator × error-rate × mechanism 退化曲线（合成 mixed-trust 轨迹套件）
PYTHONPATH=. python3 -m provenance_agent_eval.cpm_degradation_demo \
  --output-dir artifacts/cpm-degradation-synthetic-v1 --seeds 5
# 输出：curves.md / curves.json / curves.svg（曲线）、cells.jsonl.gz（每 cell 原始记录）、report.md、progress.html

# 模型驱动 trace：模型自己填参数，按参数来源判定诱导；附 clean 对照；随后自动 sweep
PYTHONPATH=. python3 -m provenance_agent_eval.cpm_model_demo \
  --model qwen3:4b --base-url http://127.0.0.1:11434 \
  --output-dir artifacts/cpm-model-traces-qwen3-4b-v1 --variants 2 --phrasings 20 --seeds 5
# 4090 节点：--model qwen3:8b --base-url http://192.168.1.105:11434
# disclosure 模式：用户把 authority 值说得多明确（explicit / unspecified / partial / memory）
#   --disclosures explicit,unspecified,partial,memory
# 只重放已保存的 trace（不再调模型）：
PYTHONPATH=. python3 -m provenance_agent_eval.cpm_degradation_demo \
  --traces artifacts/cpm-model-traces-qwen3-4b-v1/traces.jsonl --output-dir artifacts/replay-v1

# AgentDojo backend（可选的外部有效性检查，不属于主线）：录制 slack suite 的多步 episode → AgentTrace → sweep
# 需要 agentdojo 包（见 requirements-agentdojo.txt），用 conda env `agentdojo` 的解释器运行；
# 核心包与测试仍是纯标准库，agentdojo 只在录制时惰性导入
PYTHONPATH=. /opt/miniconda3/envs/agentdojo/bin/python -m provenance_agent_eval.cpm_agentdojo_demo \
  --suite slack --model qwen3:8b --base-url http://192.168.1.105:11434 \
  --output-dir artifacts/cpm-agentdojo-slack-qwen3-8b-v1 --seeds 5
# 小样本验证：--user-tasks user_task_0,user_task_1 --injection-tasks injection_task_1 --max-episodes 4
# 离线重转换已录 episode（不调模型、不需要 agentdojo）：
PYTHONPATH=. python3 -m provenance_agent_eval.cpm_agentdojo_demo \
  --episodes artifacts/cpm-agentdojo-slack-qwen3-8b-v1/episodes.jsonl \
  --output-dir artifacts/cpm-agentdojo-slack-qwen3-8b-strict --untrusted-policy all_tool_outputs

# 多次 sweep 的横向对照表（ASR/FBR @ 选定 p，聚类 bootstrap CI）
PYTHONPATH=. python3 -m provenance_agent_eval.cpm_results_table \
  synthetic=artifacts/cpm-degradation-synthetic-v1 \
  agentdojo-qwen3-8b=artifacts/cpm-agentdojo-slack-qwen3-8b-v1-sweep --rates 0,0.25,0.5,1
```

结果汇总（含 4B/8B 模型 trace 与 AgentDojo 对照）：[RESULTS.md](RESULTS.md)。

`provenance_agent_eval/cpm/`：

| 模块 | 职责 |
|---|---|
| `trace.py` | `AgentTrace` 规范、oracle graph、只由真实 root 决定的 ground truth |
| `operators.py` | `MutationOperator`：preserve / drop_label / forge_label / misattribute_parent / merge_taint，各自绑定真实成因与不变量 |
| `schedule.py` | 确定性 mutation 选择（operator, rate, seed, trace_id）；`propagate` 选择"被破坏的 hop 向下游传播"或"只破坏 sink 记录"两种语义 |
| `defenses.py` | 机制抽象：no_policy / label_trusting / lineage_verifying / origin_routing / whole_call_quarantine |
| `replay.py` | trace × schedule × mechanism → 决策、receipt、mutation 触及标记 |
| `degradation.py` | sweep、退化曲线、阶段归因、不变量统计 |
| `laws.py` | 退化规律拟合：compound 族 `y0+(1-y0)(1-(1-p)^m)^k` 的自由拟合、线性基线与**零自由参数的结构预测**检验；聚类 bootstrap 斜率 |
| `execution.py` | 执行阶段算子 `stale_version` / `semantic_replay` 与机制 grant_single_use / grant_revalidated / intent_ledger（I4/I5 曲线） |
| `campaign.py` | H1–H7 战役编排、结构预测规则、H5 诱导×结构分解 |
| `stats.py` | Wilson、按 trace 聚类 bootstrap、拒绝对确定性 cell 报 p 值的 McNemar |
| `synthetic.py` | 10 个 mixed-trust 模板 × 变体 × benign/attack 双胞胎；`parametric_suite`：可控深度 d、authority 参数数 k、投毒模式 |
| `plots.py` | 退化曲线 SVG；观测点 + bootstrap 带 + 零参数预测律叠加图 |
| `model_traces.py` | 模型自填参数的单轮决策 → `AgentTrace`（结构沿用模板，模型决定 benign/attack 侧）；四种 disclosure 模式 |
| `agentdojo_backend.py` | （可选）AgentDojo episode 录制、oracle value attribution、`AgentTrace` 转换 |

## 历史实验入口（附录 / 实现验证）

核心项目只依赖 Python 标准库；Redis store 需要额外安装 `redis-py`，仅在使用 Redis 实验时启用：

```bash
cd provenance_agent_eval
PYTHONPATH=. python3 -m unittest discover -s tests -v
PYTHONPATH=. python3 -m provenance_agent_eval.orthogonal_demo --repetitions 3
PYTHONPATH=. python3 -m provenance_agent_eval.attack_demo --output-dir artifacts/generalized-attacks-grant-aware-v3
PYTHONPATH=. python3 -m provenance_agent_eval.composed_demo --output-dir artifacts/composed-attacks-v4
PYTHONPATH=. python3 -m provenance_agent_eval.concurrency_demo --output-dir artifacts/concurrent-grant-v1
PYTHONPATH=. python3 -m provenance_agent_eval.cross_process_demo --output-dir artifacts/cross-process-grant-v1
# Redis 服务运行在 localhost:6379 时执行真实共享存储对照
PYTHONPATH=. python3 -m provenance_agent_eval.redis_demo --output-dir artifacts/redis-cross-process-grant-v2
# 论文主线：单变量 provenance mutation 配对重放
PYTHONPATH=. python3 -m provenance_agent_eval.mutation_benchmark --output-dir artifacts/provenance-mutation-v1
PYTHONPATH=. python3 -m provenance_agent_eval.model_mutation_runner \
  --model qwen3:4b --base-url http://127.0.0.1:11434 --repetitions 5 \
  --output-dir artifacts/model-provenance-mutation-qwen3-4b-r5-v1
PYTHONPATH=. python3 -m provenance_agent_eval.model_mutation_analysis \
  --input-dir artifacts/model-provenance-mutation-qwen3-4b-r5-v1 \
  --output-dir artifacts/model-provenance-mutation-analysis-qwen3-4b-r5-v1
```

本地 Ollama 已部署 `qwen3:4b` 时可运行模型实验：

```bash
PYTHONPATH=. python3 -m provenance_agent_eval.model_demo \
  --model qwen3:4b \
  --base-url http://127.0.0.1:11434 \
  --matrix matched-laundering \
  --repetitions 5 \
  --output-dir artifacts/model-matched-laundering
```

多个本地或局域网 Ollama endpoint 可使用统一配置运行：

```bash
cp model_endpoints.example.json model_endpoints.json
PYTHONPATH=. python3 -m provenance_agent_eval.multi_model_demo \
  --config model_endpoints.json \
  --matrix matched-laundering \
  --repetitions 5 \
  --output-root artifacts/multi-model-v1
```

完成模型运行后可做配对统计比较：

```bash
PYTHONPATH=. python3 -m provenance_agent_eval.model_compare_demo \
  --run qwen3-4b=artifacts/model-qwen3-4b-20v \
  --run llama32-3b=artifacts/model-llama32-3b-20v \
  --output-dir artifacts/model-comparison-v1
```

真实工具契约端到端实验使用沙箱 workspace adapter（读取文档、更新工单、发送消息、删除文件）。adapter 只修改内存状态并产生 side-effect receipt，不访问主机文件系统或外部网络；这让 runtime 授权和实际副作用可以分别审计：

```bash
PYTHONPATH=. python3 -m provenance_agent_eval.real_tool_runner \
  --model qwen3:8b --base-url http://192.168.1.105:11434 \
  --repetitions 20 --output-dir artifacts/real-tool-qwen3-8b-4090-r20-v2

PYTHONPATH=. python3 -m provenance_agent_eval.real_tool_runner \
  --model llama3.1:8b --base-url http://192.168.1.105:11434 \
  --repetitions 20 --output-dir artifacts/real-tool-llama31-8b-4090-r20-v2

PYTHONPATH=. python3 -m provenance_agent_eval.real_tool_analysis_demo \
  --run qwen3-8b-4090=artifacts/real-tool-qwen3-8b-4090-r20-v2 \
  --run llama31-8b-4090=artifacts/real-tool-llama31-8b-4090-r20-v2 \
  --output-dir artifacts/real-tool-analysis-8b-4090-r20-v2
```

为避免把模型可见文本包装与 runtime provenance evidence 混为同一个变量，正式实验使用正交入口：

```bash
PYTHONPATH=. python3 -m provenance_agent_eval.model_factorial_demo \
  --model qwen3:4b \
  --repetitions 20 \
  --output-dir artifacts/factorial-qwen3-4b-v1

PYTHONPATH=. python3 -m provenance_agent_eval.factorial_analysis_demo \
  --run qwen3-4b=artifacts/factorial-qwen3-4b-v1 \
  --run llama32-3b=artifacts/factorial-llama32-3b-v1 \
  --output-dir artifacts/factorial-analysis-v1
```

4090 节点上的 8B 模型使用同一入口；实验主机只负责调度和记录：

```bash
PYTHONPATH=. python3 -m provenance_agent_eval.model_factorial_demo \
  --model qwen3:8b --base-url http://192.168.1.105:11434 \
  --repetitions 20 --output-dir artifacts/factorial-qwen3-8b-4090-v1

PYTHONPATH=. python3 -m provenance_agent_eval.model_factorial_demo \
  --model llama3.1:8b --base-url http://192.168.1.105:11434 \
  --repetitions 20 --output-dir artifacts/factorial-llama31-8b-4090-v1

PYTHONPATH=. python3 -m provenance_agent_eval.factorial_analysis_demo \
  --run qwen3-8b-4090=artifacts/factorial-qwen3-8b-4090-v1 \
  --run llama31-8b-4090=artifacts/factorial-llama31-8b-4090-v1 \
  --output-dir artifacts/factorial-analysis-8b-4090-v1
```

4090 笔记本只负责模型推理；本机负责实验调度、runtime、JSONL 日志和统计。两台设备位于同一局域网时，将远端 Ollama 监听地址写入 `base_url` 即可。

完整部署步骤见 [REMOTE_MODEL_SETUP.md](REMOTE_MODEL_SETUP.md)。
如果要把本文件直接交给 4090 端的 Codex，使用 [4090_CODEX_HANDOFF.md](4090_CODEX_HANDOFF.md)。

## 实验输出

每次实验目录都自动生成：

```text
experiments.jsonl   # 原始 case、aggregate、指标 delta
report.md           # 人类可读报告
lessons.jsonl       # 带 record ID 证据的经验
lessons.md          # 经验回顾
progress.html       # 由 JSONL 派生的可视化
```

## 代码入口

- `core.py`：来源、值、版本化 `ResourceHandle`、动作、工具和 `AuthorizationGrant`。
- `provenance_graph.py` / `transformations.py`：来源图和来源变换。
- `mutation_benchmark.py`：单变量 provenance mutation 的配对重放与 failure attribution。
- `model_mutation_runner.py` / `model_mutation_analysis.py`：固定模型动作后跨 evidence、策略和真实工具 receipt 的配对重放与统计。
- `runtime.py`：legacy source-aware 与严格 grant-aware 授权。
- `benchmark_schema.py` / `benchmark_runner.py`：96-cell provenance 矩阵。
- `attack_schema.py` / `attack_runner.py`：10 攻击族、6 发生层的通用攻击矩阵。
- `composed_runner.py`：多步组合攻击、grant replay 和版本化资源替换竞态。
- `concurrency_runner.py`：线程级 single-use grant 消费竞态与原子消费对照。
- `nonce_store.py`：进程内、SQLite 和 Redis 持久化 single-use nonce store。
- `cross_process_runner.py`：跨进程 single-use grant replay 对照实验。
- `model_runner.py` / `ollama_client.py`：模型动作诱导实验。
- `multi_model_demo.py` / `model_endpoints.example.json`：跨本地与局域网 endpoint 的配对模型实验。
- `model_compare.py`：跨模型效应差、bootstrap 置信区间与精确 McNemar 检验。
- `model_factorial_runner.py` / `factorial_analysis.py`：正交 presentation × evidence × policy 实验及统计。
- `tool_adapters.py` / `real_tool_runner.py`：可观测 sandbox workspace 工具契约，以及模型决策到 handler receipt 的端到端实验。
- `real_tool_analysis.py`：端到端工具副作用、runtime policy 和跨模型配对分析。
- `experiment_log.py` / `visualization.py`：结构化日志、经验和图表。
