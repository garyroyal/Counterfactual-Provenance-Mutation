# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | cross-process-grant-matrix
时间：2026-09-02T02:52:15+00:00
置信度：medium

**观察**：两个独立进程竞争同一 single-use grant；进程内存储条件发生 1 个 replay violation，共享 SQLite 条件未发生。

**证据**：
- `exp-0002`

**结论**：进程边界上的 nonce 消费仍可被重放；需要共享的原子 nonce 存储或分布式锁。

**后续**：替换 SQLite 为真实 Redis/数据库 nonce store，并在异步多 worker 调度器中复测。

