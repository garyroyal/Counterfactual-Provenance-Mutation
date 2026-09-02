# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | generalized-attack-matrix
时间：2026-09-01T12:57:10+00:00
置信度：high

**观察**：完成 20 个跨层攻击 case；来源感知策略仍放行 0 个 unsafe case。

**证据**：

**结论**：grant-aware authorization 阻断了所有当前攻击族；动作范围、资源范围、有效期和一次性 nonce 能覆盖此前的 scope escalation 与 replay。

**后续**：加入资源替换、并发竞态、多步组合攻击和真实模型 handoff，再验证 grant 语义是否完整。

