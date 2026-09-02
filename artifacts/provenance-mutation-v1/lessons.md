# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | provenance-mutation-replay
时间：2026-09-02T07:46:50+00:00
置信度：high

**观察**：完成 12 个 clean/mutated 配对，变异只发生在 provenance transform。

**证据**：
- `no_policy|external-side-effect|semantic-preserving-summary`
- `no_policy|external-side-effect|source-drop`
- `no_policy|external-side-effect|source-forgery`
- `no_policy|destroy|semantic-preserving-summary`
- `no_policy|destroy|source-drop`
- `no_policy|destroy|source-forgery`

**结论**：counterfactual replay 将来源质量变化与模型行为解耦；source-aware 条件应阻断 source loss/forgery，而语义保持摘要不应改变授权决策。

**后续**：将同一 pair schema 接到模型生成的 action trace，再估计模型诱导、授权和副作用的分阶段效应。

