# Lessons Learned

经验记录必须关联实验证据，并明确置信度。

## lesson-0001 | cpm-degradation
时间：2026-09-02T09:16:36+00:00
置信度：medium

**观察**：80 traces x 5 operators x 6 rates x 5 mechanisms; stochastic rates use 5 schedules.

**证据**：
- `exp-0001`
- `exp-0002`
- `exp-0003`
- `exp-0004`
- `exp-0005`
- `exp-0006`
- `exp-0007`
- `exp-0008`

**结论**：preserve@1.0 -> no_policy: ASR=1.00, FBR=0.00; label_trusting: ASR=0.00, FBR=0.00; lineage_verifying: ASR=0.00, FBR=0.00; origin_routing: ASR=0.00, FBR=0.00; whole_call_quarantine: ASR=0.00, FBR=0.70 | drop_label@1.0 -> no_policy: ASR=1.00, FBR=0.00; label_trusting: ASR=0.00, FBR=1.00; lineage_verifying: ASR=0.00, FBR=1.00; origin_routing: ASR=0.00, FBR=0.00; whole_call_quarantine: ASR=0.00, FBR=0.70 | forge_label@1.0 -> no_policy: ASR=1.00, FBR=0.00; label_trusting: ASR=0.90, FBR=0.00; lineage_verifying: ASR=0.00, FBR=0.00; origin_routing: ASR=0.00, FBR=0.00; whole_call_quarantine: ASR=0.00, FBR=0.70 | misattribute_parent@1.0 -> no_policy: ASR=1.00, FBR=0.00; label_trusting: ASR=0.90, FBR=0.00; lineage_verifying: ASR=0.90, FBR=0.00; origin_routing: ASR=1.00, FBR=0.00; whole_call_quarantine: ASR=1.00, FBR=0.00 | merge_taint@1.0 -> no_policy: ASR=1.00, FBR=0.00; label_trusting: ASR=0.00, FBR=0.90; lineage_verifying: ASR=0.00, FBR=0.90; origin_routing: ASR=0.00, FBR=0.90; whole_call_quarantine: ASR=0.00, FBR=0.90

**后续**：Replace the synthetic suite with recorded AgentDojo/AgentDyn traces and add published-defense adapters.

