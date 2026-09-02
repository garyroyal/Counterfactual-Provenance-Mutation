# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | redis-cross-process-grant-matrix
时间：2026-09-02T03:05:54+00:00
置信度：high

**观察**：两个独立进程竞争同一 single-use grant；Redis atomic 条件只允许一次执行。

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`

**结论**：Redis Lua atomic claim 阻断跨进程 grant replay，同时保留一次合法执行。

**后续**：在真实多 worker agent 调度器中复测 Redis 故障、超时和 key 生命周期语义。

