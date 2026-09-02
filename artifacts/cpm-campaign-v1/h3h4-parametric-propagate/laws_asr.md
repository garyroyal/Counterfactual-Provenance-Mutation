# H3/H4 structural ASR laws (propagate)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (1,1) 0.990 | 0.991 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.990 | 0.050 |
| `forge_label` | label_trusting | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,1.5) 0.988 | 0.963 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.941 | 0.138 |
| `forge_label` | label_trusting | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,2.5) 0.996 | 0.813 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.992 | 0.075 |
| `forge_label` | label_trusting | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.998 | 0.691 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.998 | 0.038 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=1 | 4 | 0.00 | 3.00 [1.00, 4.00] | (1.5,0.5) 0.973 | 0.452 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.817 | 0.202 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=2 | 4 | 0.00 | 1.00 [0.00, 2.00] | (1.5,1.5) 0.979 | 0.977 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.976 | 0.109 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1.5,2.5) 0.998 | 0.945 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.988 | 0.074 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1.5,3) 0.991 | 0.890 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.963 | 0.172 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=1 | 4 | 0.00 | 2.50 [0.50, 5.00] | (3.5,1) 0.986 | 0.590 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.985 | 0.072 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.50 [0.00, 1.50] | (2,1.5) 0.991 | 0.947 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.989 | 0.069 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=3 | 4 | 0.00 | 1.00 [0.00, 2.00] | (2.5,1.5) 0.995 | 0.912 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.941 | 0.207 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.50 [0.00, 1.50] | (3.5,3.5) 0.998 | 0.933 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.976 | 0.114 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=1 | 4 | 0.00 | 4.00 [4.00, 4.00] | (3.5,1) 0.981 | 0.504 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.981 | 0.085 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.50 [0.00, 1.50] | (5,3.5) 1.000 | 0.857 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.990 | 0.068 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.50 [0.00, 1.50] | (5.5,8) 0.998 | 0.881 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.975 | 0.169 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.50 [0.00, 1.50] | (3.5,2.5) 0.997 | 0.925 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.992 | 0.082 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=1 | 4 | 0.00 | 3.50 [2.00, 5.00] | (4.5,1) 0.995 | 0.285 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.992 | 0.060 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (9,8) 0.998 | 0.787 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.973 | 0.168 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (5,4.5) 0.999 | 0.887 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.975 | 0.144 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.50 [0.00, 1.50] | (5,5) 0.999 | 0.891 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.992 | 0.088 |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (1,1) 0.983 | 0.985 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.100 |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,1) 0.992 | 0.922 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.986 | 0.087 |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.998 | 0.790 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.998 | 0.028 |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,5) 0.999 | 0.635 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.994 | 0.066 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=1 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1.5) 0.989 | 0.964 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.945 | 0.150 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2,2.5) 0.995 | 0.954 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.984 | 0.112 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3.5,8) 0.999 | 0.916 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.984 | 0.126 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6.5) 0.996 | 0.884 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.990 | 0.078 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=1 | 4 | 0.00 | 2.50 [2.00, 3.50] | (2,1) 0.986 | 0.846 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.924 | 0.175 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.50 [0.00, 1.50] | (5.5,4.5) 0.999 | 0.866 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.982 | 0.134 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,7.5) 1.000 | 0.910 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.990 | 0.093 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4,8) 1.000 | 0.919 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.996 | 0.062 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=1 | 4 | 0.00 | 5.50 [3.00, 8.00] | (3,0.5) 0.991 | -0.704 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.783 | 0.206 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=2 | 4 | 0.00 | 1.50 [0.50, 2.00] | (7,3) 0.998 | 0.712 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.959 | 0.183 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=3 | 4 | 0.00 | 1.00 [0.00, 2.00] | (5,4) 0.994 | 0.869 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.991 | 0.076 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,5) 1.000 | 0.902 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.999 | 0.028 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=1 | 4 | 0.00 | 3.50 [1.00, 5.50] | (4.5,1) 0.991 | 0.265 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.985 | 0.063 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=2 | 4 | 0.00 | 3.00 [2.00, 4.00] | (7,2) 0.997 | 0.505 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.942 | 0.168 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (8.5,8) 0.999 | 0.806 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.992 | 0.069 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (6,7.5) 0.996 | 0.844 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.981 | 0.138 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (1,1) 0.983 | 0.985 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.100 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,1) 0.992 | 0.922 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.986 | 0.087 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.998 | 0.790 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.998 | 0.028 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,5) 0.999 | 0.635 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.994 | 0.066 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=1 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1.5) 0.989 | 0.964 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.945 | 0.150 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2,2.5) 0.995 | 0.954 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.984 | 0.112 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3.5,8) 0.999 | 0.916 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.984 | 0.126 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6.5) 0.996 | 0.884 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.990 | 0.078 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=1 | 4 | 0.00 | 2.50 [2.00, 3.50] | (2,1) 0.986 | 0.846 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.924 | 0.175 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.50 [0.00, 1.50] | (5.5,4.5) 0.999 | 0.866 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.982 | 0.134 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,7.5) 1.000 | 0.910 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.990 | 0.093 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4,8) 1.000 | 0.919 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.996 | 0.062 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=1 | 4 | 0.00 | 5.50 [3.00, 8.00] | (3,0.5) 0.991 | -0.704 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.783 | 0.206 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=2 | 4 | 0.00 | 1.50 [0.50, 2.00] | (7,3) 0.998 | 0.712 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.959 | 0.183 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=3 | 4 | 0.00 | 1.00 [0.00, 2.00] | (5,4) 0.994 | 0.869 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.991 | 0.076 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,5) 1.000 | 0.902 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.999 | 0.028 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=1 | 4 | 0.00 | 3.50 [1.00, 5.50] | (4.5,1) 0.991 | 0.265 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.985 | 0.063 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=2 | 4 | 0.00 | 3.00 [2.00, 4.00] | (7,2) 0.997 | 0.505 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.942 | 0.168 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (8.5,8) 0.999 | 0.806 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.992 | 0.069 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (6,7.5) 0.996 | 0.844 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.981 | 0.138 |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (1,1) 0.983 | 0.985 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.100 |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,1) 0.992 | 0.922 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.986 | 0.087 |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.998 | 0.790 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.998 | 0.028 |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,5) 0.999 | 0.635 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.994 | 0.066 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=1 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1.5) 0.989 | 0.964 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.945 | 0.150 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2,2.5) 0.995 | 0.954 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.984 | 0.112 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3.5,8) 0.999 | 0.916 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.984 | 0.126 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6.5) 0.996 | 0.884 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.990 | 0.078 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=1 | 4 | 0.00 | 2.50 [2.00, 3.50] | (2,1) 0.986 | 0.846 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.924 | 0.175 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.50 [0.00, 1.50] | (5.5,4.5) 0.999 | 0.866 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.982 | 0.134 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,7.5) 1.000 | 0.910 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.990 | 0.093 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4,8) 1.000 | 0.919 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.996 | 0.062 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=1 | 4 | 0.00 | 5.50 [3.00, 8.00] | (3,0.5) 0.991 | -0.704 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.783 | 0.206 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=2 | 4 | 0.00 | 1.50 [0.50, 2.00] | (7,3) 0.998 | 0.712 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.959 | 0.183 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=3 | 4 | 0.00 | 1.00 [0.00, 2.00] | (5,4) 0.994 | 0.869 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.991 | 0.076 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,5) 1.000 | 0.902 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.999 | 0.028 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=1 | 4 | 0.00 | 3.50 [1.00, 5.50] | (4.5,1) 0.991 | 0.265 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.985 | 0.063 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=2 | 4 | 0.00 | 3.00 [2.00, 4.00] | (7,2) 0.997 | 0.505 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.942 | 0.168 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (8.5,8) 0.999 | 0.806 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.992 | 0.069 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (6,7.5) 0.996 | 0.844 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.981 | 0.138 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1.5,4) 0.998 | 0.843 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.986 | 0.100 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1.5,6) 0.999 | 0.763 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.998 | 0.028 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1,5) 0.999 | 0.607 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.990 | 0.066 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,2.5) 0.999 | 0.568 | any-hop(d) ^ all-args(k) (m=1, k=5) | 0.990 | 0.087 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,3.5) 0.996 | 0.954 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.989 | 0.091 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3,8) 0.990 | 0.906 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.980 | 0.122 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6.5) 0.998 | 0.867 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.989 | 0.078 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,7.5) 0.993 | 0.862 | any-hop(d) ^ all-args(k) (m=2, k=5) | 0.982 | 0.126 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (2,1.5) 0.996 | 0.958 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.982 | 0.116 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3.5,3) 0.998 | 0.927 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.991 | 0.080 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3.5,5.5) 0.998 | 0.923 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.996 | 0.061 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (3.5,7) 0.998 | 0.904 | any-hop(d) ^ all-args(k) (m=3, k=5) | 0.995 | 0.065 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=1 | 4 | 0.00 | 3.00 [2.00, 5.00] | (2.5,1) 0.990 | 0.770 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.937 | 0.182 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=2 | 4 | 0.00 | 0.50 [0.00, 1.50] | (4,2.5) 0.999 | 0.878 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.993 | 0.081 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (5.5,7) 1.000 | 0.885 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.994 | 0.078 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (4.5,5) 1.000 | 0.902 | any-hop(d) ^ all-args(k) (m=4, k=5) | 0.993 | 0.076 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=1 | 4 | 0.00 | 2.00 [0.00, 4.00] | (4,2) 0.973 | 0.815 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.943 | 0.232 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=2 | 4 | 0.00 | 2.00 [0.50, 3.50] | (4,1.5) 0.988 | 0.768 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.950 | 0.156 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (7,7.5) 1.000 | 0.841 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.995 | 0.069 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (5.5,8) 0.988 | 0.831 | any-hop(d) ^ all-args(k) (m=5, k=5) | 0.975 | 0.158 |
