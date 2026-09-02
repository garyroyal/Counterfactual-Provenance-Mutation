# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | cpm-degradation
时间：2026-09-02T12:05:39+00:00
置信度：medium

**观察**：172 traces x 2 operators x 7 rates x 5 mechanisms; stochastic rates use 5 schedules.

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`

**结论**：forge_label@1.0 -> no_policy: ASR=1.00, FBR=N/A; label_trusting: ASR=1.00, FBR=N/A; lineage_verifying: ASR=0.00, FBR=N/A; origin_routing: ASR=0.00, FBR=N/A; whole_call_quarantine: ASR=0.00, FBR=N/A | misattribute_parent@1.0 -> no_policy: ASR=1.00, FBR=N/A; label_trusting: ASR=1.00, FBR=N/A; lineage_verifying: ASR=1.00, FBR=N/A; origin_routing: ASR=1.00, FBR=N/A; whole_call_quarantine: ASR=1.00, FBR=N/A

**后续**：Compare against induction x structure-only failure.

