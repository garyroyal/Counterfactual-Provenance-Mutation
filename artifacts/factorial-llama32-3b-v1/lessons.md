# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | model-provenance-factorial
时间：2026-09-02T04:27:49+00:00
置信度：high

**观察**：完成 80 次模型决策，并复用为 640 次正交 runtime 评估；presentation 与 provenance evidence 不再共用同一变量。

**证据**：
- `exp-0001`
- `exp-0010`
- `exp-0019`
- `exp-0028`
- `exp-0037`
- `exp-0046`
- `exp-0055`
- `exp-0064`

**结论**：模型诱导效应与 runtime provenance 授权效应可以被独立估计。

**后续**：在更多模型和真实工具 adapter 上复现 presentation × evidence × policy 交互。

