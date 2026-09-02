# H3/H4 structural FBR laws (propagate)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1.5,1.5) 0.987 | 0.986 | any-hop(d*k) (m=1, k=1) | 0.977 | 0.133 |
| `drop_label` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 2.00 [1.17, 3.00] | (2,1) 0.993 | 0.905 | any-hop(d*k) (m=2, k=1) | 0.993 | 0.067 |
| `drop_label` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 2.67 [1.67, 3.67] | (2.5,1) 0.995 | 0.767 | any-hop(d*k) (m=3, k=1) | 0.982 | 0.078 |
| `drop_label` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 5.50 [4.33, 6.50] | (5.5,1) 0.960 | -0.140 | any-hop(d*k) (m=4, k=1) | 0.903 | 0.206 |
| `drop_label` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 1.33 [0.50, 2.17] | (3,1.5) 0.998 | 0.885 | any-hop(d*k) (m=2, k=1) | 0.989 | 0.064 |
| `drop_label` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 3.00 [1.67, 4.50] | (4,1) 0.992 | 0.425 | any-hop(d*k) (m=4, k=1) | 0.992 | 0.050 |
| `drop_label` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (6,1.5) 0.999 | 0.431 | any-hop(d*k) (m=6, k=1) | 0.934 | 0.169 |
| `drop_label` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (6,0.5) 0.991 | -3.647 | any-hop(d*k) (m=8, k=1) | 0.828 | 0.147 |
| `drop_label` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 2.67 [1.83, 3.50] | (3,1) 0.991 | 0.613 | any-hop(d*k) (m=3, k=1) | 0.991 | 0.072 |
| `drop_label` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 4.83 [3.50, 6.00] | (6,1) 0.999 | -0.216 | any-hop(d*k) (m=6, k=1) | 0.999 | 0.022 |
| `drop_label` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 6.17 [5.17, 7.17] | (9,1) 0.999 | -1.375 | any-hop(d*k) (m=9, k=1) | 0.999 | 0.020 |
| `drop_label` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 7.17 [6.33, 8.17] | (6.5,0.5) 0.993 | -4.568 | any-hop(d*k) (m=12, k=1) | 0.983 | 0.057 |
| `drop_label` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 4.00 [3.00, 5.17] | (4.5,1) 0.998 | 0.254 | any-hop(d*k) (m=4, k=1) | 0.990 | 0.056 |
| `drop_label` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 5.33 [4.17, 6.50] | (10.5,1.5) 0.996 | -0.763 | any-hop(d*k) (m=8, k=1) | 0.988 | 0.050 |
| `drop_label` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 7.17 [5.83, 8.33] | (15,1.5) 0.986 | -2.269 | any-hop(d*k) (m=12, k=1) | 0.972 | 0.076 |
| `drop_label` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 7.50 [6.67, 8.33] | (8.5,0.5) 0.992 | -7.780 | any-hop(d*k) (m=16, k=1) | 0.961 | 0.065 |
| `drop_label` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 3.83 [2.50, 5.17] | (4,1) 0.995 | 0.427 | any-hop(d*k) (m=5, k=1) | 0.973 | 0.113 |
| `drop_label` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 7.17 [6.17, 8.17] | (14.5,1.5) 0.979 | -2.047 | any-hop(d*k) (m=10, k=1) | 0.977 | 0.065 |
| `drop_label` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 8.83 [8.33, 9.33] | (18.5,1) 0.993 | -10.680 | any-hop(d*k) (m=15, k=1) | 0.906 | 0.089 |
| `drop_label` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 8.50 [7.50, 9.33] | (19,1) 0.996 | -12.428 | any-hop(d*k) (m=20, k=1) | 0.990 | 0.028 |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1.5,1.5) 0.987 | 0.986 | any-hop(d*k) (m=1, k=1) | 0.977 | 0.133 |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 2.00 [1.17, 3.00] | (2,1) 0.993 | 0.905 | any-hop(d*k) (m=2, k=1) | 0.993 | 0.067 |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 2.67 [1.67, 3.67] | (2.5,1) 0.995 | 0.767 | any-hop(d*k) (m=3, k=1) | 0.982 | 0.078 |
| `drop_label` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 5.50 [4.33, 6.50] | (5.5,1) 0.960 | -0.140 | any-hop(d*k) (m=4, k=1) | 0.903 | 0.206 |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 1.33 [0.50, 2.17] | (3,1.5) 0.998 | 0.885 | any-hop(d*k) (m=2, k=1) | 0.989 | 0.064 |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 3.00 [1.67, 4.50] | (4,1) 0.992 | 0.425 | any-hop(d*k) (m=4, k=1) | 0.992 | 0.050 |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (6,1.5) 0.999 | 0.431 | any-hop(d*k) (m=6, k=1) | 0.934 | 0.169 |
| `drop_label` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (6,0.5) 0.991 | -3.647 | any-hop(d*k) (m=8, k=1) | 0.828 | 0.147 |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 2.67 [1.83, 3.50] | (3,1) 0.991 | 0.613 | any-hop(d*k) (m=3, k=1) | 0.991 | 0.072 |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 4.83 [3.50, 6.00] | (6,1) 0.999 | -0.216 | any-hop(d*k) (m=6, k=1) | 0.999 | 0.022 |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 6.17 [5.17, 7.17] | (9,1) 0.999 | -1.375 | any-hop(d*k) (m=9, k=1) | 0.999 | 0.020 |
| `drop_label` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 7.17 [6.33, 8.17] | (6.5,0.5) 0.993 | -4.568 | any-hop(d*k) (m=12, k=1) | 0.983 | 0.057 |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 4.00 [3.00, 5.17] | (4.5,1) 0.998 | 0.254 | any-hop(d*k) (m=4, k=1) | 0.990 | 0.056 |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 5.33 [4.17, 6.50] | (10.5,1.5) 0.996 | -0.763 | any-hop(d*k) (m=8, k=1) | 0.988 | 0.050 |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 7.17 [5.83, 8.33] | (15,1.5) 0.986 | -2.269 | any-hop(d*k) (m=12, k=1) | 0.972 | 0.076 |
| `drop_label` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 7.50 [6.67, 8.33] | (8.5,0.5) 0.992 | -7.780 | any-hop(d*k) (m=16, k=1) | 0.961 | 0.065 |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 3.83 [2.50, 5.17] | (4,1) 0.995 | 0.427 | any-hop(d*k) (m=5, k=1) | 0.973 | 0.113 |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 7.17 [6.17, 8.17] | (14.5,1.5) 0.979 | -2.047 | any-hop(d*k) (m=10, k=1) | 0.977 | 0.065 |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 8.83 [8.33, 9.33] | (18.5,1) 0.993 | -10.680 | any-hop(d*k) (m=15, k=1) | 0.906 | 0.089 |
| `drop_label` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 8.50 [7.50, 9.33] | (19,1) 0.996 | -12.428 | any-hop(d*k) (m=20, k=1) | 0.990 | 0.028 |
| `drop_label` | no_policy | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
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
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
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
| `forge_label` | no_policy | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
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
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1.5,1.5) 0.997 | 0.997 | any-hop(d*k) (m=1, k=1) | 0.996 | 0.050 |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (1.5,1) 0.996 | 0.955 | any-hop(d*k) (m=2, k=1) | 0.972 | 0.088 |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (2.5,1) 0.983 | 0.725 | any-hop(d*k) (m=3, k=1) | 0.972 | 0.092 |
| `merge_taint` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 3.67 [2.50, 5.00] | (4,1) 0.998 | 0.405 | any-hop(d*k) (m=4, k=1) | 0.998 | 0.023 |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (2.5,1) 0.998 | 0.775 | any-hop(d*k) (m=2, k=1) | 0.975 | 0.100 |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 2.50 [1.67, 3.33] | (7,2) 0.999 | 0.516 | any-hop(d*k) (m=4, k=1) | 0.972 | 0.094 |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 5.67 [4.50, 6.67] | (3.5,0.5) 0.989 | -1.073 | any-hop(d*k) (m=6, k=1) | 0.944 | 0.102 |
| `merge_taint` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 5.33 [4.00, 6.83] | (8,1) 0.990 | -1.024 | any-hop(d*k) (m=8, k=1) | 0.990 | 0.050 |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 1.67 [1.00, 2.33] | (4,1.5) 0.978 | 0.725 | any-hop(d*k) (m=3, k=1) | 0.973 | 0.104 |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 6.00 [4.67, 7.33] | (4,0.5) 0.998 | -1.627 | any-hop(d*k) (m=6, k=1) | 0.862 | 0.152 |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 6.50 [5.67, 7.50] | (10,1) 0.997 | -2.196 | any-hop(d*k) (m=9, k=1) | 0.988 | 0.047 |
| `merge_taint` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (17,2) 0.999 | -1.748 | any-hop(d*k) (m=12, k=1) | 0.956 | 0.126 |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (4.5,1.5) 0.999 | 0.650 | any-hop(d*k) (m=4, k=1) | 0.973 | 0.111 |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 6.00 [4.83, 7.00] | (9,1) 0.997 | -1.603 | any-hop(d*k) (m=8, k=1) | 0.984 | 0.050 |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 6.83 [5.33, 8.00] | (11.5,1) 0.992 | -3.491 | any-hop(d*k) (m=12, k=1) | 0.991 | 0.034 |
| `merge_taint` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 7.83 [7.00, 8.67] | (14,1) 0.993 | -5.005 | any-hop(d*k) (m=16, k=1) | 0.969 | 0.060 |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 4.00 [2.83, 5.00] | (7,1.5) 0.995 | 0.255 | any-hop(d*k) (m=5, k=1) | 0.989 | 0.076 |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 6.50 [5.50, 7.50] | (10.5,1) 0.997 | -2.475 | any-hop(d*k) (m=10, k=1) | 0.995 | 0.032 |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 7.50 [6.17, 8.83] | (7.5,0.5) 0.999 | -6.516 | any-hop(d*k) (m=15, k=1) | 0.965 | 0.053 |
| `merge_taint` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 8.67 [7.67, 9.50] | (17.5,1) 0.991 | -8.533 | any-hop(d*k) (m=20, k=1) | 0.962 | 0.075 |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1.5,1.5) 0.997 | 0.997 | any-hop(d*k) [structural propagation] (m=1, k=1) | 0.996 | 0.050 |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (1.5,1) 0.996 | 0.955 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.972 | 0.088 |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (2.5,1) 0.983 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.972 | 0.092 |
| `merge_taint` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 3.67 [2.50, 5.00] | (4,1) 0.998 | 0.405 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.998 | 0.023 |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (2.5,1) 0.998 | 0.775 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.975 | 0.100 |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 2.50 [1.67, 3.33] | (7,2) 0.999 | 0.516 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.972 | 0.094 |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 5.67 [4.50, 6.67] | (3.5,0.5) 0.989 | -1.073 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.944 | 0.102 |
| `merge_taint` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 5.33 [4.00, 6.83] | (8,1) 0.990 | -1.024 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.990 | 0.050 |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 1.67 [1.00, 2.33] | (4,1.5) 0.978 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.973 | 0.104 |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 6.00 [4.67, 7.33] | (4,0.5) 0.998 | -1.627 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.862 | 0.152 |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 6.50 [5.67, 7.50] | (10,1) 0.997 | -2.196 | any-hop(d*k) [structural propagation] (m=9, k=1) | 0.988 | 0.047 |
| `merge_taint` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (17,2) 0.999 | -1.748 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.956 | 0.126 |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (4.5,1.5) 0.999 | 0.650 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.973 | 0.111 |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 6.00 [4.83, 7.00] | (9,1) 0.997 | -1.603 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.984 | 0.050 |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 6.83 [5.33, 8.00] | (11.5,1) 0.992 | -3.491 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.991 | 0.034 |
| `merge_taint` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 7.83 [7.00, 8.67] | (14,1) 0.993 | -5.005 | any-hop(d*k) [structural propagation] (m=16, k=1) | 0.969 | 0.060 |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 4.00 [2.83, 5.00] | (7,1.5) 0.995 | 0.255 | any-hop(d*k) [structural propagation] (m=5, k=1) | 0.989 | 0.076 |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 6.50 [5.50, 7.50] | (10.5,1) 0.997 | -2.475 | any-hop(d*k) [structural propagation] (m=10, k=1) | 0.995 | 0.032 |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 7.50 [6.17, 8.83] | (7.5,0.5) 0.999 | -6.516 | any-hop(d*k) [structural propagation] (m=15, k=1) | 0.965 | 0.053 |
| `merge_taint` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 8.67 [7.67, 9.50] | (17.5,1) 0.991 | -8.533 | any-hop(d*k) [structural propagation] (m=20, k=1) | 0.962 | 0.075 |
| `merge_taint` | no_policy | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1.5,1.5) 0.997 | 0.997 | any-hop(d*k) [structural propagation] (m=1, k=1) | 0.996 | 0.050 |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (1.5,1) 0.996 | 0.955 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.972 | 0.088 |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (2.5,1) 0.983 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.972 | 0.092 |
| `merge_taint` | origin_routing | propagate=True, depth=1, k=4 | 12 | 0.00 | 3.67 [2.50, 5.00] | (4,1) 0.998 | 0.405 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.998 | 0.023 |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (2.5,1) 0.998 | 0.775 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.975 | 0.100 |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=2 | 12 | 0.00 | 2.50 [1.67, 3.33] | (7,2) 0.999 | 0.516 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.972 | 0.094 |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=3 | 12 | 0.00 | 5.67 [4.50, 6.67] | (3.5,0.5) 0.989 | -1.073 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.944 | 0.102 |
| `merge_taint` | origin_routing | propagate=True, depth=2, k=4 | 12 | 0.00 | 5.33 [4.00, 6.83] | (8,1) 0.990 | -1.024 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.990 | 0.050 |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=1 | 12 | 0.00 | 1.67 [1.00, 2.33] | (4,1.5) 0.978 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.973 | 0.104 |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=2 | 12 | 0.00 | 6.00 [4.67, 7.33] | (4,0.5) 0.998 | -1.627 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.862 | 0.152 |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=3 | 12 | 0.00 | 6.50 [5.67, 7.50] | (10,1) 0.997 | -2.196 | any-hop(d*k) [structural propagation] (m=9, k=1) | 0.988 | 0.047 |
| `merge_taint` | origin_routing | propagate=True, depth=3, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (17,2) 0.999 | -1.748 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.956 | 0.126 |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (4.5,1.5) 0.999 | 0.650 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.973 | 0.111 |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=2 | 12 | 0.00 | 6.00 [4.83, 7.00] | (9,1) 0.997 | -1.603 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.984 | 0.050 |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=3 | 12 | 0.00 | 6.83 [5.33, 8.00] | (11.5,1) 0.992 | -3.491 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.991 | 0.034 |
| `merge_taint` | origin_routing | propagate=True, depth=4, k=4 | 12 | 0.00 | 7.83 [7.00, 8.67] | (14,1) 0.993 | -5.005 | any-hop(d*k) [structural propagation] (m=16, k=1) | 0.969 | 0.060 |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=1 | 12 | 0.00 | 4.00 [2.83, 5.00] | (7,1.5) 0.995 | 0.255 | any-hop(d*k) [structural propagation] (m=5, k=1) | 0.989 | 0.076 |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=2 | 12 | 0.00 | 6.50 [5.50, 7.50] | (10.5,1) 0.997 | -2.475 | any-hop(d*k) [structural propagation] (m=10, k=1) | 0.995 | 0.032 |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=3 | 12 | 0.00 | 7.50 [6.17, 8.83] | (7.5,0.5) 0.999 | -6.516 | any-hop(d*k) [structural propagation] (m=15, k=1) | 0.965 | 0.053 |
| `merge_taint` | origin_routing | propagate=True, depth=5, k=4 | 12 | 0.00 | 8.67 [7.67, 9.50] | (17.5,1) 0.991 | -8.533 | any-hop(d*k) [structural propagation] (m=20, k=1) | 0.962 | 0.075 |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=True, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=1 | 12 | 1.00 | -1.83 [-2.33, -1.33] | (0.5,0.5) -2.283 | 0.972 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=2 | 12 | 1.00 | -1.17 [-2.17, -0.33] | (0.5,0.5) -1.911 | 0.995 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=3 | 12 | 1.00 | -0.50 [-1.00, 0.00] | (0.5,0.5) -1.339 | 0.987 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=1, k=4 | 12 | 1.00 | -0.33 [-0.83, 0.00] | (0.5,0.5) -1.124 | 0.978 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=1 | 12 | 1.00 | -2.00 [-3.17, -0.83] | (0.5,0.5) -2.756 | 0.880 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=2 | 12 | 1.00 | -1.67 [-2.33, -1.00] | (0.5,0.5) -2.707 | 0.839 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=3 | 12 | 1.00 | -2.17 [-3.17, -1.17] | (0.5,0.5) -2.868 | 0.869 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=2, k=4 | 12 | 1.00 | -2.50 [-3.83, -1.33] | (0.5,0.5) -3.343 | 0.811 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=1 | 12 | 1.00 | -2.67 [-3.83, -1.50] | (0.5,0.5) -3.597 | 0.729 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=2 | 12 | 1.00 | -2.33 [-3.33, -1.50] | (0.5,0.5) -3.059 | 0.817 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=3 | 12 | 1.00 | -3.00 [-4.33, -1.83] | (0.5,0.5) -4.057 | 0.576 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=3, k=4 | 12 | 1.00 | -2.00 [-2.83, -1.17] | (0.5,0.5) -3.067 | 0.707 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=1 | 12 | 1.00 | -4.67 [-6.00, -3.50] | (0.5,0.5) -6.815 | 0.025 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=2 | 12 | 1.00 | -3.67 [-5.00, -2.50] | (0.5,0.5) -4.553 | 0.467 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=3 | 12 | 1.00 | -3.17 [-4.67, -1.83] | (0.5,0.5) -4.682 | 0.392 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=4, k=4 | 12 | 1.00 | -3.00 [-3.83, -2.17] | (0.5,0.5) -3.636 | 0.497 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=1 | 12 | 1.00 | -3.33 [-4.67, -2.00] | (0.5,0.5) -4.970 | 0.372 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=2 | 12 | 1.00 | -4.17 [-5.17, -3.17] | (0.5,0.5) -6.268 | 0.073 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=3 | 12 | 1.00 | -5.00 [-6.00, -3.83] | (0.5,0.5) -7.211 | -0.481 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=True, depth=5, k=4 | 12 | 1.00 | -4.00 [-5.17, -2.83] | (0.5,0.5) -5.058 | 0.219 | - | - | - |
