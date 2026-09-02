# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | generalized-attack-matrix
时间：2026-09-01T12:35:33+00:00
置信度：high

**观察**：完成 20 个跨层攻击 case；来源感知策略仍放行 2 个 unsafe case。

**证据**：
- `exp-0012`
- `exp-0014`

**结论**：boolean trusted/authorized 标记不足以表达权限的动作范围和有效期。

**后续**：为授权证据加入 action scope、resource scope、issuer、issued_at、expires_at 和 nonce，再重复矩阵。

