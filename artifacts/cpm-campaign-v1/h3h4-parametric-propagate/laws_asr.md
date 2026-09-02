# H3/H4 structural ASR laws (propagate)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.50 [0.00, 1.00] | (1.5,1.5) 0.997 | 0.994 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.992 | 0.050 |
| `forge_label` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.990 | 0.921 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.990 | 0.083 |
| `forge_label` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.995 | 0.792 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.995 | 0.058 |
| `forge_label` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 1.000 | 0.683 | any-hop(d) ^ all-args(k) (m=1, k=4) | 1.000 | 0.004 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.83 [1.83, 3.83] | (1,0.5) 0.975 | 0.720 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.954 | 0.119 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 1.00 [0.33, 1.83] | (2,2) 0.989 | 0.972 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.989 | 0.064 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,8) 0.999 | 0.911 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.990 | 0.072 |
| `forge_label` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,3.5) 0.999 | 0.932 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.997 | 0.050 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 1.83 [0.83, 3.00] | (2.5,1) 0.993 | 0.814 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.971 | 0.111 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.50 [0.00, 1.33] | (2,1.5) 0.998 | 0.960 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.985 | 0.099 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (2.5,2.5) 0.999 | 0.963 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.994 | 0.070 |
| `forge_label` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.17 [0.00, 0.50] | (3,4) 1.000 | 0.945 | any-hop(d) ^ all-args(k) (m=3, k=4) | 1.000 | 0.011 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 4.17 [3.33, 5.17] | (4.5,1) 0.991 | 0.343 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.989 | 0.073 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 1.33 [0.50, 2.17] | (3,1.5) 0.998 | 0.870 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.996 | 0.046 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (2.5,2) 0.994 | 0.953 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.953 | 0.207 |
| `forge_label` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.50 [0.00, 1.00] | (3.5,3) 0.998 | 0.930 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.995 | 0.048 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 3.67 [2.83, 4.33] | (4.5,1) 0.996 | 0.245 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.996 | 0.043 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 1.50 [0.50, 2.83] | (6,2.5) 0.999 | 0.736 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.997 | 0.035 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (4.5,3) 0.999 | 0.870 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.995 | 0.044 |
| `forge_label` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.33 [0.00, 0.83] | (5,4) 1.000 | 0.875 | any-hop(d) ^ all-args(k) (m=5, k=4) | 1.000 | 0.013 |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 1.33 [0.50, 2.33] | (1,1) 0.983 | 0.987 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.083 |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.995 | 0.872 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.995 | 0.062 |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5.5) 1.000 | 0.769 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.996 | 0.045 |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.999 | 0.682 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.999 | 0.017 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.17 [1.33, 3.00] | (1.5,1) 0.989 | 0.931 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.981 | 0.088 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (2.5,2) 0.996 | 0.967 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.988 | 0.075 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2.5,4.5) 0.999 | 0.920 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.995 | 0.050 |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,4) 0.998 | 0.915 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.998 | 0.030 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 3.17 [2.50, 3.83] | (3,1) 0.989 | 0.670 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.989 | 0.076 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.50 [0.00, 1.00] | (3.5,3) 0.999 | 0.923 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.995 | 0.068 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (3,3.5) 0.998 | 0.947 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.991 | 0.070 |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,4.5) 1.000 | 0.935 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.997 | 0.053 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 4.50 [3.00, 6.00] | (5,1) 0.982 | 0.117 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.969 | 0.106 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 1.33 [0.50, 2.17] | (5,2.5) 0.999 | 0.801 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.995 | 0.054 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (4.5,3.5) 0.999 | 0.892 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.999 | 0.026 |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (4,5) 1.000 | 0.916 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.994 | 0.068 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 3.50 [2.17, 4.67] | (4.5,1) 0.995 | 0.350 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.987 | 0.060 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 2.00 [1.00, 3.00] | (8.5,3) 1.000 | 0.568 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.960 | 0.185 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (5.5,3.5) 0.999 | 0.839 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.999 | 0.023 |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.17 [0.00, 0.50] | (6.5,7.5) 0.999 | 0.847 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.993 | 0.069 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 1.33 [0.50, 2.33] | (1,1) 0.983 | 0.987 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.083 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.995 | 0.872 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.995 | 0.062 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5.5) 1.000 | 0.769 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.996 | 0.045 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.999 | 0.682 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.999 | 0.017 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.17 [1.33, 3.00] | (1.5,1) 0.989 | 0.931 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.981 | 0.088 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (2.5,2) 0.996 | 0.967 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.988 | 0.075 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2.5,4.5) 0.999 | 0.920 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.995 | 0.050 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,4) 0.998 | 0.915 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.998 | 0.030 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 3.17 [2.50, 3.83] | (3,1) 0.989 | 0.670 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.989 | 0.076 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.50 [0.00, 1.00] | (3.5,3) 0.999 | 0.923 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.995 | 0.068 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (3,3.5) 0.998 | 0.947 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.991 | 0.070 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,4.5) 1.000 | 0.935 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.997 | 0.053 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 4.50 [3.00, 6.00] | (5,1) 0.982 | 0.117 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.969 | 0.106 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 1.33 [0.50, 2.17] | (5,2.5) 0.999 | 0.801 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.995 | 0.054 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (4.5,3.5) 0.999 | 0.892 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.999 | 0.026 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (4,5) 1.000 | 0.916 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.994 | 0.068 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 3.50 [2.17, 4.67] | (4.5,1) 0.995 | 0.350 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.987 | 0.060 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 2.00 [1.00, 3.00] | (8.5,3) 1.000 | 0.568 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.960 | 0.185 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (5.5,3.5) 0.999 | 0.839 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.999 | 0.023 |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.17 [0.00, 0.50] | (6.5,7.5) 0.999 | 0.847 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.993 | 0.069 |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=1 | 12 | 0.00 | 1.33 [0.50, 2.33] | (1,1) 0.983 | 0.987 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.083 |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.995 | 0.872 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.995 | 0.062 |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5.5) 1.000 | 0.769 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.996 | 0.045 |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.999 | 0.682 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.999 | 0.017 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.17 [1.33, 3.00] | (1.5,1) 0.989 | 0.931 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.981 | 0.088 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (2.5,2) 0.996 | 0.967 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.988 | 0.075 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2.5,4.5) 0.999 | 0.920 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.995 | 0.050 |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,4) 0.998 | 0.915 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.998 | 0.030 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=1 | 12 | 0.00 | 3.17 [2.50, 3.83] | (3,1) 0.989 | 0.670 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.989 | 0.076 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.50 [0.00, 1.00] | (3.5,3) 0.999 | 0.923 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.995 | 0.068 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (3,3.5) 0.998 | 0.947 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.991 | 0.070 |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,4.5) 1.000 | 0.935 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.997 | 0.053 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=1 | 12 | 0.00 | 4.50 [3.00, 6.00] | (5,1) 0.982 | 0.117 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.969 | 0.106 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=2 | 12 | 0.00 | 1.33 [0.50, 2.17] | (5,2.5) 0.999 | 0.801 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.995 | 0.054 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (4.5,3.5) 0.999 | 0.892 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.999 | 0.026 |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (4,5) 1.000 | 0.916 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.994 | 0.068 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=1 | 12 | 0.00 | 3.50 [2.17, 4.67] | (4.5,1) 0.995 | 0.350 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.987 | 0.060 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=2 | 12 | 0.00 | 2.00 [1.00, 3.00] | (8.5,3) 1.000 | 0.568 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.960 | 0.185 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (5.5,3.5) 0.999 | 0.839 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.999 | 0.023 |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.17 [0.00, 0.50] | (6.5,7.5) 0.999 | 0.847 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.993 | 0.069 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,1.5) 0.993 | 0.932 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.989 | 0.083 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.999 | 0.752 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.999 | 0.022 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4.5) 0.997 | 0.635 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.995 | 0.062 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,5.5) 1.000 | 0.596 | any-hop(d) ^ all-args(k) (m=1, k=5) | 0.999 | 0.021 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1.5,1.5) 0.995 | 0.979 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.987 | 0.079 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,2.5) 0.999 | 0.960 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.992 | 0.061 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6) 1.000 | 0.899 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.996 | 0.061 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,5) 0.999 | 0.876 | any-hop(d) ^ all-args(k) (m=2, k=5) | 0.999 | 0.026 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.67 [0.17, 1.17] | (3.5,2.5) 1.000 | 0.915 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.999 | 0.018 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,3.5) 0.998 | 0.946 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.997 | 0.053 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (3,5.5) 0.998 | 0.927 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.984 | 0.120 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3.5,7) 1.000 | 0.919 | any-hop(d) ^ all-args(k) (m=3, k=5) | 0.999 | 0.031 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 0.00 | 1.50 [0.50, 2.67] | (4,2) 0.993 | 0.843 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.993 | 0.067 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (4.5,4) 1.000 | 0.904 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.998 | 0.036 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (5,6.5) 1.000 | 0.894 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.996 | 0.052 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3.5,4) 1.000 | 0.924 | any-hop(d) ^ all-args(k) (m=4, k=5) | 0.999 | 0.024 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 0.00 | 1.67 [0.50, 2.83] | (5,2.5) 0.991 | 0.780 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.984 | 0.115 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (5.5,2.5) 0.998 | 0.783 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.983 | 0.123 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.17 [0.00, 0.50] | (5,4) 0.999 | 0.876 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.999 | 0.028 |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (6,7.5) 1.000 | 0.867 | any-hop(d) ^ all-args(k) (m=5, k=5) | 0.997 | 0.047 |
