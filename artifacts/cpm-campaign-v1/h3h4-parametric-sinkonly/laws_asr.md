# H3/H4 structural ASR laws (sinkonly)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.50 [0.00, 1.00] | (1.5,1.5) 0.997 | 0.994 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.992 | 0.050 |
| `forge_label` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.990 | 0.921 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.990 | 0.083 |
| `forge_label` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.995 | 0.792 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.995 | 0.058 |
| `forge_label` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 1.000 | 0.683 | sink-only(1) ^ all-args(k) (m=1, k=4) | 1.000 | 0.004 |
| `forge_label` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 2.33 [1.33, 3.33] | (0.5,0.5) 0.970 | 0.925 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.907 | 0.133 |
| `forge_label` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (1,2) 0.999 | 0.895 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.999 | 0.023 |
| `forge_label` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,4) 0.999 | 0.847 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.960 | 0.178 |
| `forge_label` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,1.5) 0.997 | 0.731 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.993 | 0.071 |
| `forge_label` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.67 [0.17, 1.17] | (1,1) 0.995 | 0.995 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.995 | 0.050 |
| `forge_label` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.997 | 0.865 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.997 | 0.029 |
| `forge_label` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.999 | 0.752 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.999 | 0.022 |
| `forge_label` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,8) 1.000 | 0.673 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.999 | 0.029 |
| `forge_label` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.33 [0.83, 1.83] | (1.5,1) 0.993 | 0.969 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.943 | 0.167 |
| `forge_label` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,4) 0.999 | 0.842 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.990 | 0.083 |
| `forge_label` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,7) 0.999 | 0.716 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.994 | 0.058 |
| `forge_label` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,7.5) 1.000 | 0.699 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.997 | 0.050 |
| `forge_label` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1,1) 0.998 | 0.998 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.998 | 0.033 |
| `forge_label` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,2) 0.998 | 0.890 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.998 | 0.029 |
| `forge_label` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3.5) 0.999 | 0.732 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.993 | 0.072 |
| `forge_label` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,2.5) 0.999 | 0.602 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.982 | 0.116 |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 1.33 [0.50, 2.33] | (1,1) 0.983 | 0.987 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.983 | 0.083 |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.995 | 0.872 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.995 | 0.062 |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5.5) 1.000 | 0.769 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.996 | 0.045 |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.999 | 0.682 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.999 | 0.017 |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1,1.5) 0.990 | 0.962 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.948 | 0.150 |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,2.5) 0.995 | 0.930 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.982 | 0.088 |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 1.000 | 0.764 | sink-only(1) ^ all-args(k) (m=1, k=3) | 1.000 | 0.008 |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4.5) 1.000 | 0.636 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.996 | 0.050 |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 1.33 [0.67, 2.17] | (1,1) 0.991 | 0.991 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.991 | 0.067 |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (1,2) 0.995 | 0.889 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.995 | 0.037 |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.999 | 0.783 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.999 | 0.025 |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,1.5) 0.997 | 0.726 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.992 | 0.071 |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.83 [1.00, 2.67] | (1,1) 0.976 | 0.982 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.976 | 0.083 |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,2) 0.998 | 0.909 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.998 | 0.033 |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5) 0.999 | 0.802 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.989 | 0.095 |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,2) 0.998 | 0.641 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.985 | 0.100 |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.67 [0.00, 1.33] | (1.5,1.5) 0.995 | 0.990 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.986 | 0.083 |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,2) 0.993 | 0.899 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.993 | 0.071 |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3.5) 0.999 | 0.718 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.991 | 0.072 |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,6.5) 1.000 | 0.721 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.987 | 0.100 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 1.33 [0.50, 2.33] | (1,1) 0.983 | 0.987 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.983 | 0.083 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.995 | 0.872 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.995 | 0.062 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5.5) 1.000 | 0.769 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.996 | 0.045 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.999 | 0.682 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.999 | 0.017 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1,1.5) 0.990 | 0.962 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.948 | 0.150 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,2.5) 0.995 | 0.930 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.982 | 0.088 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 1.000 | 0.764 | sink-only(1) ^ all-args(k) (m=1, k=3) | 1.000 | 0.008 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4.5) 1.000 | 0.636 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.996 | 0.050 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 1.33 [0.67, 2.17] | (1,1) 0.991 | 0.991 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.991 | 0.067 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (1,2) 0.995 | 0.889 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.995 | 0.037 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.999 | 0.783 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.999 | 0.025 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,1.5) 0.997 | 0.726 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.992 | 0.071 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.83 [1.00, 2.67] | (1,1) 0.976 | 0.982 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.976 | 0.083 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,2) 0.998 | 0.909 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.998 | 0.033 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5) 0.999 | 0.802 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.989 | 0.095 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,2) 0.998 | 0.641 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.985 | 0.100 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.67 [0.00, 1.33] | (1.5,1.5) 0.995 | 0.990 | sink-only(1) ^ all-args(k) (m=1, k=1) | 0.986 | 0.083 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,2) 0.993 | 0.899 | sink-only(1) ^ all-args(k) (m=1, k=2) | 0.993 | 0.071 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3.5) 0.999 | 0.718 | sink-only(1) ^ all-args(k) (m=1, k=3) | 0.991 | 0.072 |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,6.5) 1.000 | 0.721 | sink-only(1) ^ all-args(k) (m=1, k=4) | 0.987 | 0.100 |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=1 | 12 | 0.00 | 1.33 [0.50, 2.33] | (1,1) 0.983 | 0.987 | any-hop(d) ^ all-args(k) (m=1, k=1) | 0.983 | 0.083 |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,2) 0.995 | 0.872 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.995 | 0.062 |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1.5,5.5) 1.000 | 0.769 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.996 | 0.045 |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4) 0.999 | 0.682 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.999 | 0.017 |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=1 | 12 | 0.00 | 2.17 [1.33, 3.00] | (1.5,1) 0.989 | 0.931 | any-hop(d) ^ all-args(k) (m=2, k=1) | 0.981 | 0.088 |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.33 [0.00, 0.83] | (2.5,2) 0.996 | 0.967 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.988 | 0.075 |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2.5,4.5) 0.999 | 0.920 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.995 | 0.050 |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,4) 0.998 | 0.915 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.998 | 0.030 |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=1 | 12 | 0.00 | 3.17 [2.50, 3.83] | (3,1) 0.989 | 0.670 | any-hop(d) ^ all-args(k) (m=3, k=1) | 0.989 | 0.076 |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.50 [0.00, 1.00] | (3.5,3) 0.999 | 0.923 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.995 | 0.068 |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (3,3.5) 0.998 | 0.947 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.991 | 0.070 |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,4.5) 1.000 | 0.935 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.997 | 0.053 |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=1 | 12 | 0.00 | 4.50 [3.00, 6.00] | (5,1) 0.982 | 0.117 | any-hop(d) ^ all-args(k) (m=4, k=1) | 0.969 | 0.106 |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=2 | 12 | 0.00 | 1.33 [0.50, 2.17] | (5,2.5) 0.999 | 0.801 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.995 | 0.054 |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (4.5,3.5) 0.999 | 0.892 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.999 | 0.026 |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (4,5) 1.000 | 0.916 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.994 | 0.068 |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=1 | 12 | 0.00 | 3.50 [2.17, 4.67] | (4.5,1) 0.995 | 0.350 | any-hop(d) ^ all-args(k) (m=5, k=1) | 0.987 | 0.060 |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=2 | 12 | 0.00 | 2.00 [1.00, 3.00] | (8.5,3) 1.000 | 0.568 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.960 | 0.185 |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.50 [0.00, 1.00] | (5.5,3.5) 0.999 | 0.839 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.999 | 0.023 |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.17 [0.00, 0.50] | (6.5,7.5) 0.999 | 0.847 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.993 | 0.069 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1,1.5) 0.993 | 0.932 | any-hop(d) ^ all-args(k) (m=1, k=2) | 0.989 | 0.083 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,3) 0.999 | 0.752 | any-hop(d) ^ all-args(k) (m=1, k=3) | 0.999 | 0.022 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,4.5) 0.997 | 0.635 | any-hop(d) ^ all-args(k) (m=1, k=4) | 0.995 | 0.062 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (1,5.5) 1.000 | 0.596 | any-hop(d) ^ all-args(k) (m=1, k=5) | 0.999 | 0.021 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.17 [0.00, 0.50] | (1.5,1.5) 0.995 | 0.979 | any-hop(d) ^ all-args(k) (m=2, k=2) | 0.987 | 0.079 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,2.5) 0.999 | 0.960 | any-hop(d) ^ all-args(k) (m=2, k=3) | 0.992 | 0.061 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6) 1.000 | 0.899 | any-hop(d) ^ all-args(k) (m=2, k=4) | 0.996 | 0.061 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (2,5) 0.999 | 0.876 | any-hop(d) ^ all-args(k) (m=2, k=5) | 0.999 | 0.026 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.67 [0.17, 1.17] | (3.5,2.5) 1.000 | 0.915 | any-hop(d) ^ all-args(k) (m=3, k=2) | 0.999 | 0.018 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3,3.5) 0.998 | 0.946 | any-hop(d) ^ all-args(k) (m=3, k=3) | 0.997 | 0.053 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.33 [0.00, 0.83] | (3,5.5) 0.998 | 0.927 | any-hop(d) ^ all-args(k) (m=3, k=4) | 0.984 | 0.120 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3.5,7) 1.000 | 0.919 | any-hop(d) ^ all-args(k) (m=3, k=5) | 0.999 | 0.031 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.50 [0.50, 2.67] | (4,2) 0.993 | 0.843 | any-hop(d) ^ all-args(k) (m=4, k=2) | 0.993 | 0.067 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.17 [0.00, 0.50] | (4.5,4) 1.000 | 0.904 | any-hop(d) ^ all-args(k) (m=4, k=3) | 0.998 | 0.036 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (5,6.5) 1.000 | 0.894 | any-hop(d) ^ all-args(k) (m=4, k=4) | 0.996 | 0.052 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (3.5,4) 1.000 | 0.924 | any-hop(d) ^ all-args(k) (m=4, k=5) | 0.999 | 0.024 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 0.00 | 1.67 [0.50, 2.83] | (5,2.5) 0.991 | 0.780 | any-hop(d) ^ all-args(k) (m=5, k=2) | 0.984 | 0.115 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (5.5,2.5) 0.998 | 0.783 | any-hop(d) ^ all-args(k) (m=5, k=3) | 0.983 | 0.123 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.17 [0.00, 0.50] | (5,4) 0.999 | 0.876 | any-hop(d) ^ all-args(k) (m=5, k=4) | 0.999 | 0.028 |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (6,7.5) 1.000 | 0.867 | any-hop(d) ^ all-args(k) (m=5, k=5) | 0.997 | 0.047 |
