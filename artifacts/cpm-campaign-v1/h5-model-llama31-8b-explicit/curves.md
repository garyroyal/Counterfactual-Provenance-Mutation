# CPM degradation curves

Traces: 22 (22 attack twins). Rates: [0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0]. Stochastic rates use 5 schedules each.

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
| label_trusting | 0.05 | 0.08 | [0.04, 0.14] | N/A | [N/A, N/A] | 9 | 9 | 0 |
| label_trusting | 0.1 | 0.15 | [0.07, 0.23] | N/A | [N/A, N/A] | 16 | 16 | 0 |
| label_trusting | 0.25 | 0.33 | [0.24, 0.43] | N/A | [N/A, N/A] | 36 | 36 | 0 |
| label_trusting | 0.5 | 0.58 | [0.47, 0.69] | N/A | [N/A, N/A] | 64 | 64 | 0 |
| label_trusting | 0.75 | 0.85 | [0.77, 0.91] | N/A | [N/A, N/A] | 93 | 93 | 0 |
| label_trusting | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 22 | 22 | 0 |
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
| label_trusting | 0.05 | 0.10 | [0.05, 0.15] | N/A | [N/A, N/A] | 11 | 11 | 0 |
| label_trusting | 0.1 | 0.15 | [0.07, 0.22] | N/A | [N/A, N/A] | 16 | 16 | 0 |
| label_trusting | 0.25 | 0.38 | [0.28, 0.48] | N/A | [N/A, N/A] | 42 | 42 | 0 |
| label_trusting | 0.5 | 0.65 | [0.56, 0.74] | N/A | [N/A, N/A] | 72 | 72 | 0 |
| label_trusting | 0.75 | 0.87 | [0.80, 0.94] | N/A | [N/A, N/A] | 96 | 96 | 0 |
| label_trusting | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 22 | 22 | 0 |
| lineage_verifying | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.05 | 0.10 | [0.05, 0.15] | N/A | [N/A, N/A] | 11 | 11 | 0 |
| lineage_verifying | 0.1 | 0.15 | [0.07, 0.22] | N/A | [N/A, N/A] | 16 | 16 | 0 |
| lineage_verifying | 0.25 | 0.38 | [0.28, 0.48] | N/A | [N/A, N/A] | 42 | 42 | 0 |
| lineage_verifying | 0.5 | 0.65 | [0.56, 0.74] | N/A | [N/A, N/A] | 72 | 72 | 0 |
| lineage_verifying | 0.75 | 0.87 | [0.80, 0.94] | N/A | [N/A, N/A] | 96 | 96 | 0 |
| lineage_verifying | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 22 | 22 | 0 |
| origin_routing | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.05 | 0.10 | [0.05, 0.15] | N/A | [N/A, N/A] | 11 | 11 | 0 |
| origin_routing | 0.1 | 0.15 | [0.07, 0.22] | N/A | [N/A, N/A] | 16 | 16 | 0 |
| origin_routing | 0.25 | 0.38 | [0.28, 0.48] | N/A | [N/A, N/A] | 42 | 42 | 0 |
| origin_routing | 0.5 | 0.65 | [0.56, 0.74] | N/A | [N/A, N/A] | 72 | 72 | 0 |
| origin_routing | 0.75 | 0.87 | [0.80, 0.94] | N/A | [N/A, N/A] | 96 | 96 | 0 |
| origin_routing | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 22 | 22 | 0 |
| whole_call_quarantine | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.05 | 0.10 | [0.05, 0.15] | N/A | [N/A, N/A] | 11 | 11 | 0 |
| whole_call_quarantine | 0.1 | 0.15 | [0.07, 0.22] | N/A | [N/A, N/A] | 16 | 16 | 0 |
| whole_call_quarantine | 0.25 | 0.38 | [0.28, 0.48] | N/A | [N/A, N/A] | 42 | 42 | 0 |
| whole_call_quarantine | 0.5 | 0.65 | [0.56, 0.74] | N/A | [N/A, N/A] | 72 | 72 | 0 |
| whole_call_quarantine | 0.75 | 0.87 | [0.80, 0.94] | N/A | [N/A, N/A] | 96 | 96 | 0 |
| whole_call_quarantine | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 22 | 22 | 0 |

## Invariant violations by mechanism

| defense | I1 preserve flips | I2/I3 authority gains | utility losses under degradation |
|---|---:|---:|---:|
| no_policy | 0 | 0 | 0 |
| label_trusting | 0 | 499 | 0 |
| lineage_verifying | 0 | 259 | 0 |
| origin_routing | 0 | 259 | 0 |
| whole_call_quarantine | 0 | 259 | 0 |

Pairwise mechanism comparisons at rate 0 or 1 are labelled by-construction and carry no p-value; see `curves.json`.
