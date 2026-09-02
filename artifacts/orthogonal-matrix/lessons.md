# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | orthogonal-provenance-matrix
时间：2026-09-01T09:02:19+00:00
置信度：medium

**观察**：完成 96 个正交 case、每个 case 重复 3 次。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`

**结论**：来源丢失和伪造应分别由 provenance quality 与图一致性授权检查暴露，而不是只看最终 ASR。

**后续**：在保持相同 case schema 的前提下接入 Qwen3:4B，比较模型诱导率与 runtime 阻断率。

