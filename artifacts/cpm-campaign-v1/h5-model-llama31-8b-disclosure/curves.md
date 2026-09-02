# CPM degradation curves

Traces: 1001 (1001 attack twins). Rates: [0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0]. Stochastic rates use 5 schedules each.

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
| label_trusting | 0.05 | 0.08 | [0.08, 0.09] | N/A | [N/A, N/A] | 416 | 416 | 0 |
| label_trusting | 0.1 | 0.16 | [0.15, 0.17] | N/A | [N/A, N/A] | 797 | 797 | 0 |
| label_trusting | 0.25 | 0.38 | [0.36, 0.39] | N/A | [N/A, N/A] | 1880 | 1880 | 0 |
| label_trusting | 0.5 | 0.65 | [0.64, 0.67] | N/A | [N/A, N/A] | 3271 | 3271 | 0 |
| label_trusting | 0.75 | 0.86 | [0.85, 0.88] | N/A | [N/A, N/A] | 4325 | 4325 | 0 |
| label_trusting | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 1001 | 1001 | 0 |
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
| label_trusting | 0.05 | 0.09 | [0.08, 0.10] | N/A | [N/A, N/A] | 436 | 436 | 0 |
| label_trusting | 0.1 | 0.17 | [0.16, 0.18] | N/A | [N/A, N/A] | 839 | 839 | 0 |
| label_trusting | 0.25 | 0.37 | [0.36, 0.39] | N/A | [N/A, N/A] | 1855 | 1855 | 0 |
| label_trusting | 0.5 | 0.65 | [0.63, 0.66] | N/A | [N/A, N/A] | 3229 | 3229 | 0 |
| label_trusting | 0.75 | 0.85 | [0.84, 0.86] | N/A | [N/A, N/A] | 4262 | 4262 | 0 |
| label_trusting | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 1001 | 1001 | 0 |
| lineage_verifying | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| lineage_verifying | 0.05 | 0.09 | [0.08, 0.10] | N/A | [N/A, N/A] | 436 | 436 | 0 |
| lineage_verifying | 0.1 | 0.17 | [0.16, 0.18] | N/A | [N/A, N/A] | 839 | 839 | 0 |
| lineage_verifying | 0.25 | 0.37 | [0.36, 0.39] | N/A | [N/A, N/A] | 1855 | 1855 | 0 |
| lineage_verifying | 0.5 | 0.65 | [0.63, 0.66] | N/A | [N/A, N/A] | 3229 | 3229 | 0 |
| lineage_verifying | 0.75 | 0.85 | [0.84, 0.86] | N/A | [N/A, N/A] | 4262 | 4262 | 0 |
| lineage_verifying | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 1001 | 1001 | 0 |
| origin_routing | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| origin_routing | 0.05 | 0.09 | [0.08, 0.10] | N/A | [N/A, N/A] | 436 | 436 | 0 |
| origin_routing | 0.1 | 0.17 | [0.16, 0.18] | N/A | [N/A, N/A] | 839 | 839 | 0 |
| origin_routing | 0.25 | 0.37 | [0.36, 0.39] | N/A | [N/A, N/A] | 1855 | 1855 | 0 |
| origin_routing | 0.5 | 0.65 | [0.63, 0.66] | N/A | [N/A, N/A] | 3229 | 3229 | 0 |
| origin_routing | 0.75 | 0.85 | [0.84, 0.86] | N/A | [N/A, N/A] | 4262 | 4262 | 0 |
| origin_routing | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 1001 | 1001 | 0 |
| whole_call_quarantine | 0 | 0.00 | [0.00, 0.00] | N/A | [N/A, N/A] | 0 | 0 | 0 |
| whole_call_quarantine | 0.05 | 0.09 | [0.08, 0.10] | N/A | [N/A, N/A] | 436 | 436 | 0 |
| whole_call_quarantine | 0.1 | 0.17 | [0.16, 0.18] | N/A | [N/A, N/A] | 839 | 839 | 0 |
| whole_call_quarantine | 0.25 | 0.37 | [0.36, 0.39] | N/A | [N/A, N/A] | 1855 | 1855 | 0 |
| whole_call_quarantine | 0.5 | 0.65 | [0.63, 0.66] | N/A | [N/A, N/A] | 3229 | 3229 | 0 |
| whole_call_quarantine | 0.75 | 0.85 | [0.84, 0.86] | N/A | [N/A, N/A] | 4262 | 4262 | 0 |
| whole_call_quarantine | 1 | 1.00 | [1.00, 1.00] | N/A | [N/A, N/A] | 1001 | 1001 | 0 |

## Invariant violations by mechanism

| defense | I1 preserve flips | I2/I3 authority gains | utility losses under degradation |
|---|---:|---:|---:|
| no_policy | 0 | 0 | 0 |
| label_trusting | 0 | 23312 | 0 |
| lineage_verifying | 0 | 11622 | 0 |
| origin_routing | 0 | 11622 | 0 |
| whole_call_quarantine | 0 | 11622 | 0 |

Pairwise mechanism comparisons at rate 0 or 1 are labelled by-construction and carry no p-value; see `curves.json`.
