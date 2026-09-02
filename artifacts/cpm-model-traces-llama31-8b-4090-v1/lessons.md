# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | cpm-model-traces
时间：2026-09-02T09:53:28+00:00
置信度：medium

**观察**：400 injected calls produced 22 attacker-bound authority arguments; 20 clean controls produced 20 benign traces.

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`

**结论**：Model induction is measured on argument origin, so the resulting traces carry real model-chosen bindings into the CPM sweep.

**后续**：Run the same collection on the 4090 8B models and on recorded AgentDojo trajectories.

