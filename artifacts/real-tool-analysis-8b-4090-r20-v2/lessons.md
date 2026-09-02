# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | real-tool-e2e-analysis
时间：2026-09-02T07:32:01+00:00
置信度：medium

**观察**：端到端日志同时包含模型动作、runtime 决策和 adapter receipt；分析仅对共享 case/seed 做配对比较。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`

**结论**：真实副作用率必须以 adapter receipt 为准；source-aware 的安全收益要与安全任务完成率、误阻断和模型诱导率分开报告。

**后续**：在两阶段真实工具链和 grant-aware policy 上复现实验，并加入故障、重试和超时分层。

