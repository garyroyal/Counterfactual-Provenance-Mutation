# H2 mechanism x operator FBR laws (propagate)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=True | 80 | 0.00 | 1.17 [0.87, 1.50] | (1,1) 0.991 | 0.992 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True | 80 | 0.00 | 1.17 [0.87, 1.50] | (1,1) 0.991 | 0.992 | - | - | - |
| `drop_label` | no_policy | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True | 80 | 0.70 | 0.00 [0.00, 0.00] | (0.5,8) -1216963148889305559265102004224.000 | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True | 80 | 0.70 | 0.00 [0.00, 0.00] | (0.5,8) -1216963148889305559265102004224.000 | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True | 80 | 0.00 | 0.90 [0.65, 1.20] | (1,1) 0.968 | 0.999 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True | 80 | 0.00 | 0.90 [0.65, 1.20] | (1,1) 0.968 | 0.999 | - | - | - |
| `merge_taint` | no_policy | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True | 80 | 0.00 | 0.90 [0.65, 1.20] | (1,1) 0.968 | 0.999 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True | 80 | 0.70 | 0.13 [0.03, 0.25] | (0.5,1) 0.673 | 0.990 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True | 80 | 0.70 | -1.25 [-1.65, -0.88] | (0.5,8) -4.088 | 0.909 | - | - | - |
| `preserve` | label_trusting | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `preserve` | lineage_verifying | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `preserve` | no_policy | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `preserve` | origin_routing | propagate=True | 80 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `preserve` | whole_call_quarantine | propagate=True | 80 | 0.70 | 0.00 [0.00, 0.00] | (0.5,8) -1216963148889305559265102004224.000 | 1.000 | - | - | - |
