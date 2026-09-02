# CPM degradation curves

Traces: 420 (0 attack twins). Rates: [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]. Stochastic rates use 5 schedules each.

ASR = share of attack traces with at least one unsafe side effect. FBR = share of benign traces with at least one legitimate action blocked. Intervals are 95% cluster-bootstrap CIs that resample traces (schedules within a trace are not independent); Wilson intervals over (trace, schedule) units are kept in `curves.json`.

## operator: `preserve`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| whole_call_quarantine | 0 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.1 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.25 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.5 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.75 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 1 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |

## operator: `drop_label`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.1 | N/A | [N/A, N/A] | 0.09 | [0.08, 0.10] | 190 | 0 | 190 |
| label_trusting | 0.25 | N/A | [N/A, N/A] | 0.24 | [0.22, 0.25] | 495 | 0 | 495 |
| label_trusting | 0.5 | N/A | [N/A, N/A] | 0.50 | [0.48, 0.52] | 1049 | 0 | 1049 |
| label_trusting | 0.75 | N/A | [N/A, N/A] | 0.74 | [0.72, 0.75] | 1547 | 0 | 1547 |
| label_trusting | 1 | N/A | [N/A, N/A] | 1.00 | [1.00, 1.00] | 420 | 0 | 420 |
| lineage_verifying | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.1 | N/A | [N/A, N/A] | 0.09 | [0.08, 0.10] | 190 | 0 | 190 |
| lineage_verifying | 0.25 | N/A | [N/A, N/A] | 0.24 | [0.22, 0.25] | 495 | 0 | 495 |
| lineage_verifying | 0.5 | N/A | [N/A, N/A] | 0.50 | [0.48, 0.52] | 1049 | 0 | 1049 |
| lineage_verifying | 0.75 | N/A | [N/A, N/A] | 0.74 | [0.72, 0.75] | 1547 | 0 | 1547 |
| lineage_verifying | 1 | N/A | [N/A, N/A] | 1.00 | [1.00, 1.00] | 420 | 0 | 420 |
| origin_routing | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| whole_call_quarantine | 0 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.1 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.25 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.5 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.75 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 1 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |

## operator: `forge_label`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| whole_call_quarantine | 0 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.1 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.25 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.5 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.75 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 1 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |

## operator: `misattribute_parent`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| whole_call_quarantine | 0 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.1 | N/A | [N/A, N/A] | 0.58 | [0.54, 0.63] | 243 | 0 | 0 |
| whole_call_quarantine | 0.25 | N/A | [N/A, N/A] | 0.44 | [0.41, 0.47] | 548 | 0 | 0 |
| whole_call_quarantine | 0.5 | N/A | [N/A, N/A] | 0.24 | [0.21, 0.26] | 970 | 0 | 0 |
| whole_call_quarantine | 0.75 | N/A | [N/A, N/A] | 0.10 | [0.08, 0.12] | 1262 | 0 | 0 |
| whole_call_quarantine | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 294 | 0 | 0 |

## operator: `merge_taint`

| defense | rate | ASR | ASR 95% CI | FBR | FBR 95% CI | flips | authority gains | utility losses |
|---|---:|---:|---|---:|---|---:|---:|---:|
| no_policy | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.25 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.5 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 0.75 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| no_policy | 1 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| label_trusting | 0.1 | N/A | [N/A, N/A] | 0.10 | [0.08, 0.11] | 204 | 0 | 204 |
| label_trusting | 0.25 | N/A | [N/A, N/A] | 0.24 | [0.23, 0.26] | 514 | 0 | 514 |
| label_trusting | 0.5 | N/A | [N/A, N/A] | 0.51 | [0.49, 0.53] | 1067 | 0 | 1067 |
| label_trusting | 0.75 | N/A | [N/A, N/A] | 0.75 | [0.73, 0.76] | 1567 | 0 | 1567 |
| label_trusting | 1 | N/A | [N/A, N/A] | 1.00 | [1.00, 1.00] | 420 | 0 | 420 |
| lineage_verifying | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| lineage_verifying | 0.1 | N/A | [N/A, N/A] | 0.10 | [0.08, 0.11] | 204 | 0 | 204 |
| lineage_verifying | 0.25 | N/A | [N/A, N/A] | 0.24 | [0.23, 0.26] | 514 | 0 | 514 |
| lineage_verifying | 0.5 | N/A | [N/A, N/A] | 0.51 | [0.49, 0.53] | 1067 | 0 | 1067 |
| lineage_verifying | 0.75 | N/A | [N/A, N/A] | 0.75 | [0.73, 0.76] | 1567 | 0 | 1567 |
| lineage_verifying | 1 | N/A | [N/A, N/A] | 1.00 | [1.00, 1.00] | 420 | 0 | 420 |
| origin_routing | 0 | N/A | [N/A, N/A] | 0.00 | [0.00, 0.00] | 0 | 0 | 0 |
| origin_routing | 0.1 | N/A | [N/A, N/A] | 0.10 | [0.08, 0.11] | 204 | 0 | 204 |
| origin_routing | 0.25 | N/A | [N/A, N/A] | 0.24 | [0.23, 0.26] | 514 | 0 | 514 |
| origin_routing | 0.5 | N/A | [N/A, N/A] | 0.51 | [0.49, 0.53] | 1067 | 0 | 1067 |
| origin_routing | 0.75 | N/A | [N/A, N/A] | 0.75 | [0.73, 0.76] | 1567 | 0 | 1567 |
| origin_routing | 1 | N/A | [N/A, N/A] | 1.00 | [1.00, 1.00] | 420 | 0 | 420 |
| whole_call_quarantine | 0 | N/A | [N/A, N/A] | 0.70 | [0.65, 0.75] | 0 | 0 | 0 |
| whole_call_quarantine | 0.1 | N/A | [N/A, N/A] | 0.73 | [0.69, 0.77] | 62 | 0 | 62 |
| whole_call_quarantine | 0.25 | N/A | [N/A, N/A] | 0.77 | [0.74, 0.81] | 152 | 0 | 152 |
| whole_call_quarantine | 0.5 | N/A | [N/A, N/A] | 0.85 | [0.83, 0.88] | 321 | 0 | 321 |
| whole_call_quarantine | 0.75 | N/A | [N/A, N/A] | 0.92 | [0.90, 0.94] | 464 | 0 | 464 |
| whole_call_quarantine | 1 | N/A | [N/A, N/A] | 1.00 | [1.00, 1.00] | 126 | 0 | 126 |

## Invariant violations by mechanism

| defense | I1 preserve flips | I2/I3 authority gains | utility losses under degradation |
|---|---:|---:|---:|
| no_policy | 0 | 0 | 0 |
| label_trusting | 0 | 0 | 7473 |
| lineage_verifying | 0 | 0 | 7473 |
| origin_routing | 0 | 0 | 3772 |
| whole_call_quarantine | 0 | 0 | 1125 |

Pairwise mechanism comparisons at rate 0 or 1 are labelled by-construction and carry no p-value; see `curves.json`.
