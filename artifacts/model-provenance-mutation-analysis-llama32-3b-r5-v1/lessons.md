# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | model-provenance-mutation-analysis
时间：2026-09-02T07:57:55+00:00
置信度：medium

**观察**：按 evidence 和 policy 对同一模型动作做配对副作用比较。

**证据**：
- `exp-0007`
- `exp-0008`
- `exp-0009`
- `exp-0010`
- `exp-0011`
- `exp-0012`

**结论**：source-forgery 对表面 source-aware 与 graph-aware 的差异可被同一模型动作的配对副作用直接归因；诱导率保持不变，变化发生在授权/执行阶段。

**后续**：对 Qwen3:4B 与 4090 上的 Qwen3:8B、Llama3.1:8B 使用相同分析，报告模型家族与 evidence 的交互。

