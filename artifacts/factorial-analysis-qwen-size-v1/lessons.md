# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | factorial-analysis
时间：2026-09-02T06:00:45+00:00
置信度：high

**观察**：presentation 与 runtime provenance evidence 已正交；早期 matched-laundering 的 transform 效应不能继续作因果解释。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`
- `exp-0009`
- `exp-0010`

**结论**：模型诱导应归因于可见 presentation；provenance evidence 的作用应由 runtime policy 单独衡量。

**后续**：在真实工具任务和 7B/8B 模型上复现该正交设计。

