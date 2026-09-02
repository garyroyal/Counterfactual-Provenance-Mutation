# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | concurrent-grant-matrix
时间：2026-09-02T02:30:20+00:00
置信度：medium

**观察**：两个并发 worker 竞争同一 single-use grant；受保护条件仍发生 1 个 replay violation。

**证据**：
- `exp-0002`

**结论**：非原子 grant consumption 允许并发 replay；需要将 nonce 检查与消费置于同一临界区。

**后续**：把原子消费接入真实异步工具调度器，并测试跨进程锁或持久化 nonce store。

