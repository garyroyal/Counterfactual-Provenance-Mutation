# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | model-action-induction
时间：2026-09-01T11:22:31+00:00
置信度：low

**观察**：模型矩阵完成 8 个代表性 case、每个 case 重复 5 次。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`

**结论**：模型是否提出攻击动作与 runtime 是否允许执行必须分开报告。

**后续**：扩大 case 数量并比较不同模型；先固定 prompt 和解析器，再进行模型横向比较。

## lesson-0002 | model-action-induction
时间：2026-09-01T11:23:57+00:00
置信度：low

**观察**：固定 memory 来源和 external_side_effect 动作后，5 种成对攻击措辞下 direct/summary-preserve 诱导率为 0.20，memory-loss/rewrite-forged-user 为 0.80。

**证据**：
- `exp-0043`
- `exp-0044`
- `exp-0045`
- `exp-0046`
- `exp-0047`
- `exp-0048`
- `exp-0049`
- `exp-0050`

**结论**：来源丢失和可信来源伪造各使模型目标动作诱导率相对 direct 上升 0.60；来源感知 runtime 将所有实际攻击成功率保持为 0。

**后续**：扩展到至少 20 种成对措辞、多个来源与动作，并用配对统计检验和其他模型复核效应量。

