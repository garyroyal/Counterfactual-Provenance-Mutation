# CPM degradation curves

Traces: 172 (172 attack twins). Rates: [0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0]. Stochastic rates use 5 schedules each.

ASR = share of attack traces with at least one unsafe side effect. FBR = share of benign traces with at least one legitimate action blocked. Intervals are 95% cluster-bootstrap CIs that resample traces (schedules within a trace are not independent); Wilson intervals over (trace, schedule) units are kept in `curves.json`.

## operator: `forge_label`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.05 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.25 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.5 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.75 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| label_trusting | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| label_trusting | 0.05 | 0.08 | [0.07, 0.10] | N/A | [N/A, N/A] | 72 | 72 | 0 |
| label_trusting | 0.1 | 0.15 | [0.13, 0.18] | N/A | [N/A, N/A] | 131 | 131 | 0 |
| label_trusting | 0.25 | 0.36 | [0.33, 0.40] | N/A | [N/A, N/A] | 313 | 313 | 0 |
| label_trusting | 0.5 | 0.65 | [0.61, 0.68] | N/A | [N/A, N/A] | 556 | 556 | 0 |
| label_trusting | 0.75 | 0.86 | [0.83, 0.88] | N/A | [N/A, N/A] | 739 | 739 | 0 |
| label_trusting | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 172 | 172 | 0 |
| lineage_verifying | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.05 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.1 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.25 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.5 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.75 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 1 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.05 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.1 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.25 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.5 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.75 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 1 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.05 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.1 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.25 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.5 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.75 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 1 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |

## operator: `misattribute_parent`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.05 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.25 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.5 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 0.75 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| no_policy | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| label_trusting | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| label_trusting | 0.05 | 0.09 | [0.07, 0.12] | N/A | [N/A, N/A] | 80 | 80 | 0 |
| label_trusting | 0.1 | 0.15 | [0.13, 0.18] | N/A | [N/A, N/A] | 132 | 132 | 0 |
| label_trusting | 0.25 | 0.34 | [0.31, 0.38] | N/A | [N/A, N/A] | 295 | 295 | 0 |
| label_trusting | 0.5 | 0.63 | [0.59, 0.67] | N/A | [N/A, N/A] | 543 | 543 | 0 |
| label_trusting | 0.75 | 0.85 | [0.81, 0.88] | N/A | [N/A, N/A] | 727 | 727 | 0 |
| label_trusting | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 172 | 172 | 0 |
| lineage_verifying | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.05 | 0.09 | [0.07, 0.12] | N/A | [N/A, N/A] | 80 | 80 | 0 |
| lineage_verifying | 0.1 | 0.15 | [0.13, 0.18] | N/A | [N/A, N/A] | 132 | 132 | 0 |
| lineage_verifying | 0.25 | 0.34 | [0.31, 0.38] | N/A | [N/A, N/A] | 295 | 295 | 0 |
| lineage_verifying | 0.5 | 0.63 | [0.59, 0.67] | N/A | [N/A, N/A] | 543 | 543 | 0 |
| lineage_verifying | 0.75 | 0.85 | [0.81, 0.88] | N/A | [N/A, N/A] | 727 | 727 | 0 |
| lineage_verifying | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 172 | 172 | 0 |
| origin_routing | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.05 | 0.09 | [0.07, 0.12] | N/A | [N/A, N/A] | 80 | 80 | 0 |
| origin_routing | 0.1 | 0.15 | [0.13, 0.18] | N/A | [N/A, N/A] | 132 | 132 | 0 |
| origin_routing | 0.25 | 0.34 | [0.31, 0.38] | N/A | [N/A, N/A] | 295 | 295 | 0 |
| origin_routing | 0.5 | 0.63 | [0.59, 0.67] | N/A | [N/A, N/A] | 543 | 543 | 0 |
| origin_routing | 0.75 | 0.85 | [0.81, 0.88] | N/A | [N/A, N/A] | 727 | 727 | 0 |
| origin_routing | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 172 | 172 | 0 |
| whole_call_quarantine | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.05 | 0.09 | [0.07, 0.12] | N/A | [N/A, N/A] | 80 | 80 | 0 |
| whole_call_quarantine | 0.1 | 0.15 | [0.13, 0.18] | N/A | [N/A, N/A] | 132 | 132 | 0 |
| whole_call_quarantine | 0.25 | 0.34 | [0.31, 0.38] | N/A | [N/A, N/A] | 295 | 295 | 0 |
| whole_call_quarantine | 0.5 | 0.63 | [0.59, 0.67] | N/A | [N/A, N/A] | 543 | 543 | 0 |
| whole_call_quarantine | 0.75 | 0.85 | [0.81, 0.88] | N/A | [N/A, N/A] | 727 | 727 | 0 |
| whole_call_quarantine | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 172 | 172 | 0 |

## Invariant violations by mechanism

| defense | I1 preserve flips | I2/I3 authority gains | utility losses under degradation |
|---|---:|---:|---:|
| no_policy | 0 | 0 | 0 |
| label_trusting | 0 | 3932 | 0 |
| lineage_verifying | 0 | 1949 | 0 |
| origin_routing | 0 | 1949 | 0 |
| whole_call_quarantine | 0 | 1949 | 0 |

Pairwise mechanism comparisons at rate 0 or 1 are labelled by-construction and carry no p-value; see `curves.json`.
