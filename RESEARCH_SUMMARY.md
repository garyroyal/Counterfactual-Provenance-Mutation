# ProvenanceBench 研究主线

更新时间：2026-09-02

> 创新性冻结：近期 SARA、TraceGrant、ROPE、AgentFlow、AID-Guard 等工作已覆盖多种 provenance/origin/授权机制。本项目的差异不再是提出同构防御，而是 **Counterfactual Provenance Mutation (CPM)** 评测协议：在同一条 trace 上单变量改变 provenance/授权因素，配对重放并以实际副作用 receipt 做阶段归因。详见 `INNOVATION_AUDIT_2026.md`。

## 一句话目标

建立一个独立于 AgentDojo 的评测框架，测量工具型 LLM Agent 在数据变换、持久化和协作链中是否保持 provenance，并验证高风险动作授权是否满足 **no unauthorized escalation**。

项目的核心对象不是某种提示词，也不是某一个工具，而是：

```text
来源 -> 变换 -> provenance 证据 -> 动作参数 -> 授权 -> 副作用
```

## 研究问题

1. 摘要、改写、结构化提取、记忆写入、工具转发和 Agent handoff 是否导致 source loss 或 source forgery？
2. 不可信数据能否通过参数重绑定、权限范围复用或授权重放获得更高动作权限？
3. provenance 不完整、冲突或失效时，runtime 是否拒绝高风险动作？
4. 更严格的 provenance 和 grant 校验会带来多少合法任务误阻断、延迟和 token 成本？
5. 模型动作诱导与 runtime 授权失败是否是两个可分离的安全问题？

## 与已有工作的边界

AgentDojo、InjecAgent、ASB 等公开 benchmark 只作为未来场景后端，不是本项目的定义。AgentDojo-PROV、CaMeL、RTBAS、IPIGuard、Task Shield、ACE 和 SARA 等工作表明，数据流隔离、能力边界和动作级授权本身并非空白。

本项目的可检验空白是：这些机制依赖的 provenance 是否在真实变换链中保持，以及授权输入退化、伪造、越权或过期时会如何失效。提示注入只占攻击面的一部分。

## 攻击 taxonomy

当前实现 10 个攻击族、6 个发生层：

| 发生层 | 攻击族 | 是否依赖模型 | 主要影响 |
|---|---|---:|---|
| model input | instruction injection | 是 | control flow |
| data flow | data poisoning | 否 | integrity |
| provenance | source loss | 否 | authority escalation |
| provenance | source forgery | 否 | authority escalation |
| authorization | argument rebinding | 否 | integrity |
| authorization | capability scope escalation | 否 | authority escalation |
| authorization | authorization replay | 否 | authority escalation |
| persistent state | memory poisoning | 否 | persistence |
| multi-agent | delegation spoofing | 否 | authority escalation |
| data flow | destination substitution | 否 | confidentiality |

攻击机制和安全后果分开记录。`model-mediated` case 需要先报告模型是否提出目标动作；`runtime-native` case 直接测试数据流和授权机制，不能用模型拒答替代防御成功。

## 参考实现

- `core.py`：`Provenance`、`ProvenanceValue`、`ResourceHandle`、`AuthorizationGrant`、动作和工具模型。
- `provenance_graph.py`：来源节点、变换节点、祖先闭包、endorsement、source loss/forgery。
- `transformations.py`：摘要、改写、memory write、handoff、拼接。
- `runtime.py`：legacy `SourceAwareAuthorizer` 和严格 `GrantAwareAuthorizer`。
- `benchmark_schema.py` / `benchmark_runner.py`：3 × 4 × 4 × 2 的 96-cell 正交 provenance 矩阵。
- `attack_schema.py` / `attack_runner.py`：10 攻击族 × 2 策略的跨层矩阵。
- `composed_runner.py`：多步组合、grant replay、scope escalation chain、跨 Agent handoff 和资源替换竞态。
- `concurrency_runner.py`：线程级 single-use grant 消费竞态与原子消费对照。
- `nonce_store.py` / `cross_process_runner.py`：进程内、SQLite 与 Redis 持久化 nonce store，以及跨进程 grant replay 对照。
- `model_runner.py` / `ollama_client.py`：本地 Ollama Qwen3:4B 的模型动作诱导实验。
- `multi_model_demo.py`：在本机或局域网 Ollama endpoint 上运行完全相同的配对模型矩阵。
- `experiment_log.py` / `visualization.py`：JSONL 原始记录、baseline delta、经验和 dashboard。

## 当前实验结论

### 确定性 provenance 矩阵

96 个 case，每个重复 3 次，共 288 个 raw runs：

- 两种策略合法任务 Utility 均为 `1.00`。
- 无策略攻击成功率为 `0.625`。
- legacy source-aware 攻击成功率为 `0.00`，但 provenance recall 只有 `0.50`，说明安全阻断不等于来源保持完整。

### Qwen3:4B 模型基线

固定 memory 来源和 external-side-effect 动作，4 种变换 × 5 种成对攻击措辞 × 2 种策略：

- `direct` / `summary-preserve` 模型诱导率：`0.20`。
- `memory-loss` / `rewrite-forged-user` 模型诱导率：`0.80`。
- 无策略 runtime 攻击成功率随之为 `0.20` 和 `0.80`。
- grant-aware source-aware runtime 攻击成功率为 `0`。

该结果当前是低置信度效应信号，需要更多措辞、模型和随机重复。

### 两模型 20 变体探索性配对实验

已将攻击措辞由 5 个扩展到 20 个，并加入不同模型家族 `llama3.2:3b`。两个策略共享同一模型响应，确保 runtime 策略差异不受重复模型采样影响。每个模型覆盖 4 种变换 × 20 个措辞，共 80 个独立模型决策、160 条 policy-paired runtime 记录。

| 模型 | overall induction | direct | summary preserve | memory loss | forged user |
|---|---:|---:|---:|---:|---:|
| Qwen3:4B | `0.3375` | `0.15` | `0.10` | `0.45` | `0.65` |
| Llama3.2:3B | `0.0750` | `0.00` | `0.00` | `0.10` | `0.20` |

跨模型配对差值为 `0.2625`，bootstrap 95% CI 为 `[0.1625, 0.3625]`，精确 McNemar `p = 9.54e-7`。这说明模型脆弱性强度存在显著差异，但来源退化方向在两模型上是一致的。

该版本把模型可见的文本包装与 runtime provenance transform 绑定为同一个变量。后续跨来源/跨动作预实验发现该趋势会随 prompt 包装反转，因此其中的 transform 差异只能作为探索性关联，不能继续解释为 provenance 的因果效应。所有 source-aware runtime 条件的实际攻击成功率仍为 `0`。

结果目录：

- `artifacts/model-qwen3-4b-20v-v1/`
- `artifacts/model-llama32-3b-20v-v1/`
- `artifacts/model-comparison-qwen-llama-v2/`

这使“至少增加一个模型”从计划变成了已完成的不同家族本地对照；4090 笔记本后续作为局域网推理节点扩展到 7B/8B 模型，而不是承担实验调度。

### 正交 presentation × provenance evidence × policy 实验

为修复上述混杂，新增正交实验：每个模型在 4 种 presentation × 20 个措辞下只决策一次，共 80 次模型调用；每个决策再复用于 4 种 runtime provenance evidence × 2 种策略，共每模型 640 个 runtime cell。模型看到的 presentation 与 runtime 使用的 provenance evidence 因此完全独立。

模型 presentation 诱导率：

| 模型 | direct | summary | memory wording | forged-user wording | overall |
|---|---:|---:|---:|---:|---:|
| Qwen3:4B | `0.35` | `0.35` | `0.15` | `0.35` | `0.30` |
| Llama3.2:3B | `0.15` | `0.10` | `0.10` | `0.00` | `0.0875` |

没有任何 presentation 相对 direct 达到显著增幅。Qwen 的 memory wording 反而为 `-0.20`，但精确 McNemar `p=0.21875`；其余 presentation 差异也不显著。这推翻了“特定 provenance 退化文本必然提高模型诱导”的早期强表述。

跨模型 overall 差值仍为 `0.2125`，bootstrap 95% CI `[0.1125, 0.325]`，McNemar `p=0.000488`，说明模型脆弱性差异在修正混杂后依然存在。

runtime policy 主效应非常稳定：

| 模型 | no-policy attack | source-aware attack | 差值 | 95% CI | McNemar p |
|---|---:|---:|---:|---:|---:|
| Qwen3:4B | `0.30` | `0.00` | `-0.30` | `[-0.35,-0.25]` | `2.52e-29` |
| Llama3.2:3B | `0.0875` | `0.00` | `-0.0875` | `[-0.11875,-0.05625]` | `7.45e-9` |

由于同一模型决策在策略间复用，这一差异不能由模型采样解释。当前最可靠的结论因此从“provenance 退化让模型更易受骗”修订为：**模型诱导依赖模型与 presentation，而 provenance-aware runtime 能在模型已被诱导后稳定阻断未授权执行。**

结果目录：

- `artifacts/factorial-qwen3-4b-v1/`
- `artifacts/factorial-llama32-3b-v1/`
- `artifacts/factorial-analysis-v1/`

### 4090 远程 8B 模型复现

在 4090 局域网节点上使用完全相同的 Ollama 请求、温度 `0`、20 个攻击措辞和正交实验设计，新增两个不同模型家族的 8B 对照。每个模型完成 80 次独立模型决策，并将每次决策复用到 640 个 runtime cell。

| 模型 | direct | summary-preserve | memory-loss | rewrite-forged-user | overall induction |
|---|---:|---:|---:|---:|---:|
| Qwen3:8B | `0.85` | `0.75` | `0.70` | `0.85` | `0.7875` |
| Llama3.1:8B | `0.10` | `0.00` | `0.00` | `0.00` | `0.0250` |

跨模型配对差值为 `0.7625`，bootstrap 95% CI 为 `[0.6625, 0.8500]`，精确 McNemar `p = 8.67e-19`。在各模型内部，所有 presentation 相对 direct 的差异都没有达到显著性；因此这轮支持的是模型家族/对齐差异，而不是某一种 provenance 文本包装的因果效果。

为检查动作泛化，又运行了 `update_state`、`external_side_effect` 和 `destroy` 三类风险动作的 generalized-risk 矩阵，每个模型 240 个共享 case/variant、10 次重复。Qwen3:8B 的动作诱导率分别为 `0.5625`、`0.6750` 和 `0.8375`；Llama3.1:8B 分别为 `0.0250`、`0.0000` 和 `0.0250`。跨动作共享 case 的配对差值为 `0.6750`，95% CI `[0.6125, 0.7333]`，精确 McNemar `p = 3.42e-49`。source-aware runtime 在两个模型、三类动作上均将实际未授权执行率降为 `0`，但该指标仍然是 runtime 防御效果，不应与模型拒答混为一谈。

结果目录：

- `artifacts/factorial-qwen3-8b-4090-v1/`
- `artifacts/factorial-llama31-8b-4090-v1/`
- `artifacts/factorial-analysis-8b-4090-v1/`
- `artifacts/model-qwen3-8b-generalized-r10-4090-v1/`
- `artifacts/model-llama31-8b-generalized-r10-4090-v1/`
- `artifacts/model-comparison-generalized-8b-4090-v1/`

将同一正交设计中的 `qwen3:4b` 与 `qwen3:8b` 做配对比较，诱导率差值（4B 减 8B）为 `-0.4875`，bootstrap 95% CI 为 `[-0.6000, -0.3750]`，精确 McNemar `p = 3.64e-12`。这是同一家族、不同规模的强关联证据，但仍不能单独解释为参数规模的纯因果效应，因为量化版本、上下文实现和远程运行环境也可能共同影响结果。

该比较结果目录为 `artifacts/factorial-analysis-qwen-size-v1/`。

### 真实工具契约端到端实验

为避免只测合成的 `action` 字符串，新增 sandbox workspace adapter。它实现四类工具契约：`read_document`（只读）、`update_ticket`（状态变更）、`send_message`（外部副作用）和 `delete_file`（破坏性动作）。adapter 不访问主机或网络；每次状态变化产生 `SideEffectReceipt`，因此 `runtime_allowed`、handler 是否执行和状态是否改变分别可审计。每个模型包含三个副作用工具 × 可信用户任务/不可信文档攻击 × 20 次重复，并将同一次模型决策配对到 `no_policy` 与 `source_aware`。

| 模型 | 不可信攻击诱导率 | no-policy 副作用率 | source-aware 副作用率 | 可信任务完成率 |
|---|---:|---:|---:|---:|
| Qwen3:8B | `0.6833` | `0.6833` | `0.0000` | `1.0000` |
| Llama3.1:8B | `0.0000` | `0.0000` | `0.0000` | `1.0000` |

Qwen3:8B 的 source-aware 相对 no-policy 将真实 sandbox 副作用率降低 `0.6833`，在 41 个已诱导动作上配对差值为 `-1.0000`，bootstrap 95% CI `[-1.0000, -1.0000]`，精确 McNemar `p=9.09e-13`；可信任务完成率为 `1.0000`，误阻断率为 `0`。按工具分层，Qwen 的诱导率为 `update_ticket=0.50`、`send_message=0.70`、`delete_file=0.85`，说明风险动作类型会影响模型诱导强度。Llama3.1:8B 本轮 60 个不可信攻击 case 均未诱导，因此其安全结果只能说明本轮没有可供 runtime 放行的攻击，不能替代有攻击输入时的防御比较。

该轮的跨模型攻击诱导差值（Qwen3:8B 减 Llama3.1:8B）为 `0.6833`，bootstrap 95% CI `[0.5667, 0.8000]`，精确 McNemar `p=9.09e-13`。这些结果支持“模型诱导和 runtime 副作用是两个独立阶段”，但仍是沙箱工具契约证据，不等同于真实邮件、工单或文件系统服务的网络级可靠性。

结果目录：

- `artifacts/real-tool-qwen3-8b-4090-r20-v2/`
- `artifacts/real-tool-llama31-8b-4090-r20-v2/`
- `artifacts/real-tool-analysis-8b-4090-r20-v2/`

4090 远程节点部署说明见 `REMOTE_MODEL_SETUP.md`；可直接交给另一台 Codex 执行的任务说明见 `4090_CODEX_HANDOFF.md`。

### 广义攻击矩阵与授权修复

修复前的 20-case 矩阵发现两个缺口：

- action scope 缺失导致 `capability_scope_escalation` 被放行；
- expires_at 和 nonce 缺失导致 `authorization_replay` 被放行。

当前 `AuthorizationGrant` 已加入：

- `action_scopes`
- `resource_scopes`
- `issuer`
- `issued_at` / `expires_at`
- 一次性 `nonce`

修复后的最终矩阵结果：

| 策略 | attack execution rate | attack blocking rate | authorization soundness |
|---|---:|---:|---:|
| no policy | 1.00 | 0.00 | 0.00 |
| grant-aware source-aware | 0.00 | 1.00 | 1.00 |

最终单轮日志目录：`artifacts/generalized-attacks-grant-aware-v3/`。source-aware aggregate 相对 no-policy baseline 的 delta 为：execution rate `-1.00`、blocking rate `+1.00`、authorization soundness `+1.00`。

这证明当前两个已知授权 gap 可被结构化 grant 修复；不代表攻击空间已经穷尽。

### 多步组合与授权后参数漂移

新增 `composed-attack-matrix`，覆盖 5 类组合/时序 case × 3 个 runtime 条件（无策略、grant-aware、grant-aware + post-check revalidation），共 15 个 raw runs。当前版本化资源结果目录为 `artifacts/composed-attacks-v4/`。

| 条件 | attack execution rate | attack blocking rate | authorization soundness | partial execution rate | stale evidence acceptance |
|---|---:|---:|---:|---:|---:|
| no policy | `1.00` | `0.00` | `0.00` | `0.00` | `0.20` |
| grant-aware | `0.20` | `0.80` | `0.80` | `0.40` | `0.20` |
| grant-aware + revalidation | `0.00` | `1.00` | `1.00` | `0.40` | `0.00` |

关键发现是：普通 grant-aware 能阻断 provenance laundering、scope escalation、grant replay 和 spoofed handoff，但在授权检查后替换资源参数时仍会执行攻击。运行时新增授权前参数快照、`argument_drift` 事件和可选 post-check revalidation 后，该 race case 被阻断，同时合法动作 completeness 保持 `1.00`。因此，授权 soundness 需要覆盖 **check-to-use 一致性**，仅验证检查时的 provenance 不够。

这轮结果是确定性 runtime 证据，不应解释为模型攻击率；模型诱导仍由 `model_runner.py` 单独报告。

### 版本化资源与 TOCTOU 复核

`ResourceHandle(resource_id, version, value)` 将资源身份和版本纳入授权资源范围。race case 不再直接把字符串替换成攻击者地址，而是把已授权的 `recipient@1` 在执行前替换为 `recipient@2`，其解析值为攻击者地址。`artifacts/composed-attacks-v4/` 的结果与上一轮聚合值完全一致：普通 grant-aware 的 stale evidence acceptance 为 `0.20`，加入 post-check revalidation 后为 `0.00`，授权 soundness 从 `0.80` 升至 `1.00`。这说明缺口来自 check-to-use 的资源版本一致性，而不是某个具体字符串或工具。

### 并发 grant 消费竞态

新增 `concurrent-grant-matrix`，两个 worker 同时竞争同一个 single-use nonce。结果目录为 `artifacts/concurrent-grant-v1/`：

| 条件 | attack execution rate | attack blocking rate | authorization soundness | successful grant replays |
|---|---:|---:|---:|---:|
| no policy | `1.00` | `0.00` | `0.00` | `1.00` |
| grant-aware racey | `1.00` | `0.00` | `0.00` | `1.00` |
| grant-aware atomic | `0.00` | `0.50` | `1.00` | `0.00` |

故意将 nonce 检查与消费分离的 racey 条件允许两个线程都通过检查，产生一次额外 grant replay；原子条件将二者放入同一临界区，只保留一次合法执行，completeness 为 `1.00`。这把上一轮的时序缺口从单线程 hook 复核提升为可重复的线程级证据。

### 跨进程 grant 消费竞态

新增 `cross-process-grant-matrix`，由两个独立 worker 进程竞争同一个 single-use nonce。结果目录为 `artifacts/cross-process-grant-v1/`：

| 条件 | attack execution rate | attack blocking rate | authorization soundness | successful grant replays |
|---|---:|---:|---:|---:|
| no policy | `1.00` | `0.00` | `0.00` | `1.00` |
| process-local atomic | `1.00` | `0.00` | `0.00` | `1.00` |
| SQLite atomic | `0.00` | `0.50` | `1.00` | `0.00` |

进程内 `Lock` 或每进程独立的 atomic store 不能覆盖多 worker 边界，因此两个进程都能执行同一 single-use grant。共享 SQLite store 使用 `BEGIN IMMEDIATE` 完成原子 claim，将 replay violation 从 `1.00` 降至 `0.00`，并保留一次合法执行，completeness 为 `1.00`。这是 runtime-native 的确定性实验，不是模型诱导率。

### Redis 共享 nonce store

已在 `agentdojo` Conda 环境中安装 Redis Server `7.2.0` 与 `redis-py 6.4.0`，并加入 `RedisNonceStore`。它使用 Redis Lua 脚本把多 nonce 检查和写入放在同一个服务端原子操作中。真实 Redis 运行结果目录为 `artifacts/redis-cross-process-grant-v2/`；该结果用于验证 SQLite 原型之外的共享存储实现，不替代后续真实生产数据库/Redis 集群测试。

### Counterfactual Provenance Mutation (CPM) 基线

新增 `mutation_benchmark.py`，对同一 clean action 只改变一个因素：语义保持摘要、source drop 或 source forgery；每个变体在 no-policy 与 source-aware 下成对重放，并记录 decision flip、invariant、provenance failure attribution 和 baseline delta。`artifacts/provenance-mutation-v1/` 已完成 12 对配对、2 类高风险动作；source-aware 的 6 个配对不变量全部成立，no-policy 保留来源退化后仍执行的诊断缺口。该基线是 runtime-native，不包含模型诱导结论。

模型固定的 CPM 端到端扩展见 `model_mutation_runner.py`。模型每个 case/seed 只调用一次，随后把同一动作重放到 `direct`、`summary-preserve`、`memory-loss`、`rewrite-forged-user` 四类 evidence，以及 `no_policy`、表面 `source_aware`、图一致性 `graph_aware` 三类条件；sandbox adapter receipt 作为实际副作用真值。Qwen3:4B 两轮一致产生 360 条记录、12 个攻击诱导动作：在伪造 user 标签条件下，表面 source-aware 产生副作用，而 graph-aware 将同一诱导动作阻断；模型诱导率在策略间不变。Llama3.2:3B 的 360 条复核记录没有诱导出目标攻击动作，因此只能作为负对照，不能把零执行解释为防御成功。这支持“模型诱导固定后，策略差异发生在 provenance/authorization 阶段”的可归因证据，但仍需要更多高诱导模型、重复数和真实 provider contract。统计输出见 `model_mutation_analysis.py` 生成的 `model_mutation_analysis.json`。

## 日志和复现

每次实验目录都应包含：

```text
experiments.jsonl   # append-only raw and aggregate records
report.md           # 指标、baseline、delta、升降评价
lessons.jsonl       # 带 evidence record IDs 的经验
lessons.md          # 可人工回顾的经验摘要
progress.html       # 从 experiments.jsonl 派生的可视化
```

主要命令：

```bash
cd provenance_agent_eval
PYTHONPATH=. python3 -m unittest discover -s tests -v
PYTHONPATH=. python3 -m provenance_agent_eval.orthogonal_demo --repetitions 3
PYTHONPATH=. python3 -m provenance_agent_eval.model_demo --model qwen3:4b --matrix matched-laundering --repetitions 5
PYTHONPATH=. python3 -m provenance_agent_eval.attack_demo --output-dir artifacts/generalized-attacks-grant-aware-v3
PYTHONPATH=. python3 -m provenance_agent_eval.composed_demo --output-dir artifacts/composed-attacks-v4
PYTHONPATH=. python3 -m provenance_agent_eval.concurrency_demo --output-dir artifacts/concurrent-grant-v1
PYTHONPATH=. python3 -m provenance_agent_eval.cross_process_demo --output-dir artifacts/cross-process-grant-v1
PYTHONPATH=. python3 -m provenance_agent_eval.redis_demo --output-dir artifacts/redis-cross-process-grant-v2
```

## 当前限制和下一步

当前 runtime-native 攻击是最小机制实例，不等于完整现实攻击。模型实验仍使用合成的单步动作选择 prompt，8B 结果显示模型差异很大，但不能直接外推到真实 Agent 工具调用成功率。

下一阶段按以下顺序推进：

1. 将版本化 `ResourceHandle`、SQLite/Redis 原型和原子 grant consumption 接入真实工具 adapter，并测试 Redis 故障、超时、重连和 key 生命周期语义。
2. 将组合 trace 扩展为可组合的两阶段和多阶段 attack schema，并报告每一步的 failure attribution。
3. 在真实工具任务上复现相同的模型配对设计，区分模型动作诱导、runtime 授权、实际副作用、误阻断、延迟和 token 成本。
4. 对预注册的主要比较进行分层统计，并在必要时加入多重检验校正；继续保留 paired bootstrap CI 和精确 McNemar。
5. 最后再接入 AgentDojo、InjecAgent 或 ASB 作为外部后端对照。

任何单次零攻击结果都不能单独作为防御有效性结论；必须同时报告 provenance quality、模型诱导、runtime decision 和实际执行。
