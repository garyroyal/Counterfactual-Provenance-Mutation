# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | cpm-execution-degradation
时间：2026-09-02T12:05:42+00:00
置信度：medium

**观察**：48 execution scenarios x 2 operators x 7 rates x 4 mechanisms.

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`

**结论**：I4/I5 measured as curves: stale-version and semantic-replay success rates per mechanism as a function of the per-slot corruption rate.

**后续**：Fit any-of laws over n actions and n*retries slots (cpm.laws).

