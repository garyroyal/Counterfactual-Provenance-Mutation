# ProvenanceBench 创新性审查（2026-09-02）

本文档记录在继续扩大实验前做的文献边界审查。检索覆盖 2024--2026 年公开论文与 arXiv 摘要；2026 年条目仍需在投稿前复核版本、作者最终稿和审稿状态。

## 冻结后的研究命题

本项目不再把“再做一个 prompt-injection 防御器”作为贡献。冻结命题为：

> **Counterfactual Provenance Mutation (CPM)**：在同一条工具型 agent trace 上只改变一个来源/授权因素，使用配对重放和真实副作用 receipt，分别归因模型动作诱导、provenance 退化、授权判定和执行竞态；以跨变换不变量与效用代价报告 provenance-to-effect 的安全边界。

CPM 的核心产出是评测协议、可复现 mutation schema 和 failure-attribution 指标，而不是重新提出一套与现有系统同构的 policy language。

## 与近期工作的差异

| 工作 | 已覆盖的核心问题 | 本项目不重复的边界 | 需要在论文中明确的差异证据 |
|---|---|---|---|
| AgentDojo / InjecAgent / ASB | 端到端攻击成功率与任务 utility | 不把 benchmark ASR 当作唯一结果；用单变量 mutation 固定同一 trace，并记录 handler side effect | paired replay、stage attribution、receipt |
| CaMeL / Task Shield / IPIGuard / AgentDojo-PROV | 数据流隔离、动作筛选或 provenance-aware 执行 | 不比较某个过滤器谁更强；测 provenance 经过摘要、记忆、handoff 后的质量退化及其对授权的影响 | precision/recall、loss/forgery mutation、false blocking |
| SARA（arXiv:2608.27146, 2026-08-27） | 分离 action induction 与 execution authorization，记录 action provenance | 该机制已不是空白；本项目聚焦**可操纵 provenance 的反事实因果测试**，并加入资源版本、跨进程 single-use grant 和副作用回执 | 同一模型输出复用到不同 evidence；跨进程 replay/TOCTOU |
| TraceGrant（arXiv:2608.21126, 2026-08-21） | 从 user intent 到 task-effect contract 的生命周期治理 | 不提出新的 task contract；测 contract/evidence 在变换链被降级、伪造、重放时的 failure attribution | mutation operator 与阶段标签 |
| ROPE（arXiv:2608.27496, 2026-08-27） | origin policy、不可伪造来源和 rewording invariance | 不重复 origin guard 的保证；研究“来源证据本身如何在变换/持久化/并发中失效”以及 utility tax | transform-only counterfactual、stale/replay cases |
| AgentFlow（arXiv:2608.22868, 2026-08-24） | flow-centric policy language、路径规则和 SMT 验证 | 不再造 policy DSL；CPM 是跨 runtime 的黑盒/白盒评测层，可作为 AgentFlow 等系统的共同测试层 | 同一 mutation suite 复用到多种 defense |
| AID-Guard（arXiv:2608.21159, 2026-08-21） | commit/retry/recovery 下 authorization-to-effect closure | 不主张替代 provider contract；将授权后参数漂移、nonce replay、线程/进程竞态作为可重复评测因素 | linearizability、duplicate-effect receipt |
| Agent Zero Memory（arXiv:2608.29606, 2026-08-30） | provenance-aware 长期记忆与 citation lock | 不做新的记忆架构；测 memory write 是 provenance loss 的 mutation，且观察其对高风险动作权限的影响 | memory-loss paired replay |
| Utility Under Attack（arXiv:2608.21230, 2026-08-21） | 记忆投毒的 utility 损失与 provenance ranking 限制 | 不重复其 retrieval utility study；测从 memory 到具体工具副作用的授权链和阶段归因 | side-effect receipt、authorization soundness |
| CatchBench（arXiv:2608.22808, 2026-08-24） | 监督器何时能捕获 agent failure | 不评估 monitor catch rate；测 failure 在 provenance、authorization、execution 哪一层产生 | attribution vector 与 invariant violations |

## CPM 的可检验不变量

1. **Representation non-interference**：语义保持的摘要/改写不改变授权决定。
2. **No authority gain under degradation**：source loss、untrusted downgrade 不能将拒绝变成允许。
3. **No forged inheritance**：伪造 user label 不能继承真实 root 的 action scope。
4. **No duplicate effect**：同一 single-use grant 在并发、重试、跨进程下最多产生一个 side-effect receipt。
5. **Check-to-use consistency**：授权快照与执行时资源版本不一致时不得产生副作用。

CPM 的重要实现对照是：`source_aware` 仅检查动作参数携带的 provenance 标签，`graph_aware` 还检查标签是否与真实 provenance graph 的 root ancestry 一致。这个对照不是新的授权框架，而是用于识别“表面可信标签”和“可验证来源证据”的因果差异。

每个不变量同时记录 utility、延迟、阻断率和实际 handler receipt，避免把模型拒答或“调用未发生”误报成 runtime 防御成功。

## 已运行的 CPM 基线

命令：

```bash
cd provenance_agent_eval
PYTHONPATH=. python3 -m provenance_agent_eval.mutation_benchmark --output-dir artifacts/provenance-mutation-v1
```

结果：12 个 clean/mutated 配对，2 种策略，2 类高风险动作；72 个项目测试通过。source-aware 的 6 个配对不变量全部成立；语义保持摘要无决策翻转，source drop/forgery 均在 provenance 阶段被阻断。no-policy 作为诊断基线保留了“来源已坏但仍执行”的缺口。

这只是确定性 runtime 基线，不代表模型攻击率，也不等同于真实邮件、云盘或生产数据库的网络级保证。下一步应在不改变 pair schema 的前提下接入模型生成 action trace，并增加真实 provider contract 的重试/崩溃实验。

模型固定的端到端首轮已在 `artifacts/model-provenance-mutation-qwen3-4b-r5-v2/` 完成；分析结果显示 source-forgery 可绕过表面 source-aware，但不能绕过 graph-aware。Llama3.2:3B 的同协议复核没有诱导出目标攻击动作，因此只作为“无可观测攻击”的负对照，不能替代有攻击样本时的防御比较。该结果仍是 sandbox 证据，需要更大重复数和第二个高诱导模型复核。

## 论文中的新意表述边界

可以声称：提出一种跨模型、跨 runtime 的 provenance counterfactual replay 协议，并给出来源变换不变量及其 utility/latency 代价的联合报告。

不能声称：首次提出 provenance-aware authorization、origin policy 或 action-induction/authorization separation；provenance 退化必然提高任何模型的诱导率；sandbox adapter 已证明生产服务的网络级安全。
