# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | real-tool-e2e
时间：2026-09-02T07:22:26+00:00
置信度：medium

**观察**：完成 60 个模型决策，并将诱导动作连接到四类工具契约中的三类副作用 adapter。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`

**结论**：实际副作用必须由 handler receipt 观测；模型提出动作、runtime 放行和 handler 改变状态是三个独立指标。

**后续**：将同一 adapter 契约接入两阶段工具链，并对 source-aware 与 grant-aware 的误阻断、延迟和 token 成本做配对比较。

