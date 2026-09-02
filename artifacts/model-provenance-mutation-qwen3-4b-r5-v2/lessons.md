# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | model-provenance-mutation-e2e
时间：2026-09-02T07:59:08+00:00
置信度：medium

**观察**：完成 360 条模型固定的 evidence/policy 重放记录。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`

**结论**：graph-aware 与表面 source-aware 的差异可由 source-forgery mutation 单独识别；模型诱导不再与授权策略混杂。

**后续**：在 Qwen 与 Llama 两个模型上重复，并对每种 evidence 做配对 McNemar/bootstrap 分析。

