# H3/H4 structural FBR laws (sinkonly)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1.5,1.5) 0.987 | 0.986 | sink-only(k) (m=1, k=1) | 0.977 | 0.133 |
| `drop_label` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 2.00 [1.17, 3.00] | (2,1) 0.993 | 0.905 | sink-only(k) (m=2, k=1) | 0.993 | 0.067 |
| `drop_label` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 2.67 [1.67, 3.67] | (2.5,1) 0.995 | 0.767 | sink-only(k) (m=3, k=1) | 0.982 | 0.078 |
| `drop_label` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 5.50 [4.33, 6.50] | (5.5,1) 0.960 | -0.140 | sink-only(k) (m=4, k=1) | 0.903 | 0.206 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 1.00 [0.33, 1.83] | (1,1) 0.992 | 0.993 | sink-only(k) (m=1, k=1) | 0.992 | 0.067 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 2.00 [1.00, 3.17] | (2,1) 0.990 | 0.833 | sink-only(k) (m=2, k=1) | 0.990 | 0.079 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 2.00 [1.00, 3.00] | (3.5,1.5) 0.997 | 0.793 | sink-only(k) (m=3, k=1) | 0.986 | 0.071 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 4.00 [2.83, 5.50] | (4,1) 0.988 | 0.307 | sink-only(k) (m=4, k=1) | 0.988 | 0.056 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 1.17 [0.50, 1.83] | (1,1) 0.999 | 0.999 | sink-only(k) (m=1, k=1) | 0.999 | 0.017 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 1.83 [1.17, 2.67] | (2,1) 0.992 | 0.904 | sink-only(k) (m=2, k=1) | 0.992 | 0.067 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 3.00 [2.00, 4.00] | (3,1) 0.989 | 0.686 | sink-only(k) (m=3, k=1) | 0.989 | 0.075 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 3.83 [2.83, 4.83] | (4.5,1) 0.994 | 0.267 | sink-only(k) (m=4, k=1) | 0.988 | 0.050 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.50 [0.33, 3.00] | (1,1) 0.983 | 0.987 | sink-only(k) (m=1, k=1) | 0.983 | 0.067 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 2.17 [1.33, 3.00] | (2.5,1) 0.995 | 0.799 | sink-only(k) (m=2, k=1) | 0.980 | 0.100 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 2.17 [1.50, 2.83] | (4,1.5) 0.997 | 0.760 | sink-only(k) (m=3, k=1) | 0.991 | 0.054 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 3.83 [2.67, 5.00] | (3.5,1) 0.973 | 0.454 | sink-only(k) (m=4, k=1) | 0.966 | 0.117 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.83 [0.00, 1.67] | (1.5,1.5) 0.995 | 0.990 | sink-only(k) (m=1, k=1) | 0.985 | 0.083 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 2.17 [1.33, 3.17] | (2,1) 0.990 | 0.876 | sink-only(k) (m=2, k=1) | 0.990 | 0.050 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 2.83 [1.83, 3.83] | (3,1) 0.998 | 0.639 | sink-only(k) (m=3, k=1) | 0.998 | 0.022 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 3.33 [2.17, 4.50] | (4,1) 0.998 | 0.426 | sink-only(k) (m=4, k=1) | 0.998 | 0.029 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1.5,1.5) 0.987 | 0.986 | sink-only(k) (m=1, k=1) | 0.977 | 0.133 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 2.00 [1.17, 3.00] | (2,1) 0.993 | 0.905 | sink-only(k) (m=2, k=1) | 0.993 | 0.067 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 2.67 [1.67, 3.67] | (2.5,1) 0.995 | 0.767 | sink-only(k) (m=3, k=1) | 0.982 | 0.078 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 5.50 [4.33, 6.50] | (5.5,1) 0.960 | -0.140 | sink-only(k) (m=4, k=1) | 0.903 | 0.206 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 1.00 [0.33, 1.83] | (1,1) 0.992 | 0.993 | sink-only(k) (m=1, k=1) | 0.992 | 0.067 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 2.00 [1.00, 3.17] | (2,1) 0.990 | 0.833 | sink-only(k) (m=2, k=1) | 0.990 | 0.079 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 2.00 [1.00, 3.00] | (3.5,1.5) 0.997 | 0.793 | sink-only(k) (m=3, k=1) | 0.986 | 0.071 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 4.00 [2.83, 5.50] | (4,1) 0.988 | 0.307 | sink-only(k) (m=4, k=1) | 0.988 | 0.056 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 1.17 [0.50, 1.83] | (1,1) 0.999 | 0.999 | sink-only(k) (m=1, k=1) | 0.999 | 0.017 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 1.83 [1.17, 2.67] | (2,1) 0.992 | 0.904 | sink-only(k) (m=2, k=1) | 0.992 | 0.067 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 3.00 [2.00, 4.00] | (3,1) 0.989 | 0.686 | sink-only(k) (m=3, k=1) | 0.989 | 0.075 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 3.83 [2.83, 4.83] | (4.5,1) 0.994 | 0.267 | sink-only(k) (m=4, k=1) | 0.988 | 0.050 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.50 [0.33, 3.00] | (1,1) 0.983 | 0.987 | sink-only(k) (m=1, k=1) | 0.983 | 0.067 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 2.17 [1.33, 3.00] | (2.5,1) 0.995 | 0.799 | sink-only(k) (m=2, k=1) | 0.980 | 0.100 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 2.17 [1.50, 2.83] | (4,1.5) 0.997 | 0.760 | sink-only(k) (m=3, k=1) | 0.991 | 0.054 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 3.83 [2.67, 5.00] | (3.5,1) 0.973 | 0.454 | sink-only(k) (m=4, k=1) | 0.966 | 0.117 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.83 [0.00, 1.67] | (1.5,1.5) 0.995 | 0.990 | sink-only(k) (m=1, k=1) | 0.985 | 0.083 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 2.17 [1.33, 3.17] | (2,1) 0.990 | 0.876 | sink-only(k) (m=2, k=1) | 0.990 | 0.050 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 2.83 [1.83, 3.83] | (3,1) 0.998 | 0.639 | sink-only(k) (m=3, k=1) | 0.998 | 0.022 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 3.33 [2.17, 4.50] | (4,1) 0.998 | 0.426 | sink-only(k) (m=4, k=1) | 0.998 | 0.029 |
| `drop_label` | no_policy | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
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
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
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
| `forge_label` | no_policy | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
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
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1.5,1.5) 0.997 | 0.997 | sink-only(k) (m=1, k=1) | 0.996 | 0.050 |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (1.5,1) 0.996 | 0.955 | sink-only(k) (m=2, k=1) | 0.972 | 0.088 |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (2.5,1) 0.983 | 0.725 | sink-only(k) (m=3, k=1) | 0.972 | 0.092 |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 3.67 [2.50, 5.00] | (4,1) 0.998 | 0.405 | sink-only(k) (m=4, k=1) | 0.998 | 0.023 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 1.00 [0.50, 1.50] | (1,1) 0.992 | 0.995 | sink-only(k) (m=1, k=1) | 0.992 | 0.067 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 1.67 [0.83, 2.50] | (2,1) 0.998 | 0.902 | sink-only(k) (m=2, k=1) | 0.998 | 0.031 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 3.50 [2.50, 4.50] | (1.5,0.5) 0.984 | 0.398 | sink-only(k) (m=3, k=1) | 0.959 | 0.107 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 3.17 [2.17, 4.17] | (3.5,1) 0.996 | 0.571 | sink-only(k) (m=4, k=1) | 0.982 | 0.084 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.50 [0.00, 1.00] | (1,1.5) 0.976 | 0.986 | sink-only(k) (m=1, k=1) | 0.976 | 0.083 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 2.00 [1.00, 3.00] | (2,1) 0.997 | 0.852 | sink-only(k) (m=2, k=1) | 0.997 | 0.033 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 2.83 [2.00, 3.50] | (3,1) 0.992 | 0.613 | sink-only(k) (m=3, k=1) | 0.992 | 0.042 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 3.33 [2.50, 4.17] | (3.5,1) 0.992 | 0.616 | sink-only(k) (m=4, k=1) | 0.978 | 0.100 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 1.00 [0.33, 1.83] | (1,1) 0.995 | 0.996 | sink-only(k) (m=1, k=1) | 0.995 | 0.050 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 1.33 [0.67, 2.00] | (2,1) 0.989 | 0.894 | sink-only(k) (m=2, k=1) | 0.989 | 0.057 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 3.50 [2.33, 4.67] | (3,1) 0.987 | 0.632 | sink-only(k) (m=3, k=1) | 0.987 | 0.079 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 3.50 [2.83, 4.17] | (4,1) 0.999 | 0.434 | sink-only(k) (m=4, k=1) | 0.999 | 0.019 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.67 [0.17, 1.33] | (2,1.5) 0.988 | 0.981 | sink-only(k) (m=1, k=1) | 0.972 | 0.117 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 2.00 [1.17, 2.83] | (2,1) 0.985 | 0.889 | sink-only(k) (m=2, k=1) | 0.985 | 0.083 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 2.67 [1.33, 3.83] | (4.5,1.5) 0.993 | 0.698 | sink-only(k) (m=3, k=1) | 0.992 | 0.076 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 3.17 [2.00, 4.50] | (6,1.5) 0.999 | 0.448 | sink-only(k) (m=4, k=1) | 0.985 | 0.069 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1.5,1.5) 0.997 | 0.997 | any-hop(d*k) [structural propagation] (m=1, k=1) | 0.996 | 0.050 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (1.5,1) 0.996 | 0.955 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.972 | 0.088 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (2.5,1) 0.983 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.972 | 0.092 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 3.67 [2.50, 5.00] | (4,1) 0.998 | 0.405 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.998 | 0.023 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (2.5,1) 0.998 | 0.775 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.975 | 0.100 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 2.50 [1.67, 3.33] | (7,2) 0.999 | 0.516 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.972 | 0.094 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 5.67 [4.50, 6.67] | (3.5,0.5) 0.989 | -1.073 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.944 | 0.102 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 5.33 [4.00, 6.83] | (8,1) 0.990 | -1.024 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.990 | 0.050 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 1.67 [1.00, 2.33] | (4,1.5) 0.978 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.973 | 0.104 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 6.00 [4.67, 7.33] | (4,0.5) 0.998 | -1.627 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.862 | 0.152 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 6.50 [5.67, 7.50] | (10,1) 0.997 | -2.196 | any-hop(d*k) [structural propagation] (m=9, k=1) | 0.988 | 0.047 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (17,2) 0.999 | -1.748 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.956 | 0.126 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (4.5,1.5) 0.999 | 0.650 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.973 | 0.111 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 6.00 [4.83, 7.00] | (9,1) 0.997 | -1.603 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.984 | 0.050 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 6.83 [5.33, 8.00] | (11.5,1) 0.992 | -3.491 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.991 | 0.034 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 7.83 [7.00, 8.67] | (14,1) 0.993 | -5.005 | any-hop(d*k) [structural propagation] (m=16, k=1) | 0.969 | 0.060 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 4.00 [2.83, 5.00] | (7,1.5) 0.995 | 0.255 | any-hop(d*k) [structural propagation] (m=5, k=1) | 0.989 | 0.076 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 6.50 [5.50, 7.50] | (10.5,1) 0.997 | -2.475 | any-hop(d*k) [structural propagation] (m=10, k=1) | 0.995 | 0.032 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 7.50 [6.17, 8.83] | (7.5,0.5) 0.999 | -6.516 | any-hop(d*k) [structural propagation] (m=15, k=1) | 0.965 | 0.053 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 8.67 [7.67, 9.50] | (17.5,1) 0.991 | -8.533 | any-hop(d*k) [structural propagation] (m=20, k=1) | 0.962 | 0.075 |
| `merge_taint` | no_policy | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.83 [0.33, 1.33] | (1.5,1.5) 0.997 | 0.997 | any-hop(d*k) [structural propagation] (m=1, k=1) | 0.996 | 0.050 |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=2 | 12 | 0.00 | 1.17 [0.33, 2.00] | (1.5,1) 0.996 | 0.955 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.972 | 0.088 |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=3 | 12 | 0.00 | 3.00 [1.83, 4.17] | (2.5,1) 0.983 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.972 | 0.092 |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=4 | 12 | 0.00 | 3.67 [2.50, 5.00] | (4,1) 0.998 | 0.405 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.998 | 0.023 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (2.5,1) 0.998 | 0.775 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.975 | 0.100 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=2 | 12 | 0.00 | 2.50 [1.67, 3.33] | (7,2) 0.999 | 0.516 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.972 | 0.094 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=3 | 12 | 0.00 | 5.67 [4.50, 6.67] | (3.5,0.5) 0.989 | -1.073 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.944 | 0.102 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=4 | 12 | 0.00 | 5.33 [4.00, 6.83] | (8,1) 0.990 | -1.024 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.990 | 0.050 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=1 | 12 | 0.00 | 1.67 [1.00, 2.33] | (4,1.5) 0.978 | 0.725 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.973 | 0.104 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=2 | 12 | 0.00 | 6.00 [4.67, 7.33] | (4,0.5) 0.998 | -1.627 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.862 | 0.152 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=3 | 12 | 0.00 | 6.50 [5.67, 7.50] | (10,1) 0.997 | -2.196 | any-hop(d*k) [structural propagation] (m=9, k=1) | 0.988 | 0.047 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=4 | 12 | 0.00 | 7.00 [5.83, 8.17] | (17,2) 0.999 | -1.748 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.956 | 0.126 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=1 | 12 | 0.00 | 2.33 [1.50, 3.33] | (4.5,1.5) 0.999 | 0.650 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.973 | 0.111 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=2 | 12 | 0.00 | 6.00 [4.83, 7.00] | (9,1) 0.997 | -1.603 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.984 | 0.050 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=3 | 12 | 0.00 | 6.83 [5.33, 8.00] | (11.5,1) 0.992 | -3.491 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.991 | 0.034 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=4 | 12 | 0.00 | 7.83 [7.00, 8.67] | (14,1) 0.993 | -5.005 | any-hop(d*k) [structural propagation] (m=16, k=1) | 0.969 | 0.060 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=1 | 12 | 0.00 | 4.00 [2.83, 5.00] | (7,1.5) 0.995 | 0.255 | any-hop(d*k) [structural propagation] (m=5, k=1) | 0.989 | 0.076 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=2 | 12 | 0.00 | 6.50 [5.50, 7.50] | (10.5,1) 0.997 | -2.475 | any-hop(d*k) [structural propagation] (m=10, k=1) | 0.995 | 0.032 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=3 | 12 | 0.00 | 7.50 [6.17, 8.83] | (7.5,0.5) 0.999 | -6.516 | any-hop(d*k) [structural propagation] (m=15, k=1) | 0.965 | 0.053 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=4 | 12 | 0.00 | 8.67 [7.67, 9.50] | (17.5,1) 0.991 | -8.533 | any-hop(d*k) [structural propagation] (m=20, k=1) | 0.962 | 0.075 |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=1 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=2 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=3 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=4 | 12 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=1 | 12 | 1.00 | -1.83 [-2.33, -1.33] | (0.5,0.5) -2.283 | 0.972 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=2 | 12 | 1.00 | -1.17 [-2.17, -0.33] | (0.5,0.5) -1.911 | 0.995 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=3 | 12 | 1.00 | -0.50 [-1.00, 0.00] | (0.5,0.5) -1.339 | 0.987 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=4 | 12 | 1.00 | -0.33 [-0.83, 0.00] | (0.5,0.5) -1.124 | 0.978 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=1 | 12 | 1.00 | -2.00 [-3.17, -0.83] | (0.5,0.5) -2.756 | 0.880 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=2 | 12 | 1.00 | -1.67 [-2.33, -1.00] | (0.5,0.5) -2.707 | 0.839 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=3 | 12 | 1.00 | -2.17 [-3.17, -1.17] | (0.5,0.5) -2.868 | 0.869 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=4 | 12 | 1.00 | -2.50 [-3.83, -1.33] | (0.5,0.5) -3.343 | 0.811 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=1 | 12 | 1.00 | -2.67 [-3.83, -1.50] | (0.5,0.5) -3.597 | 0.729 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=2 | 12 | 1.00 | -2.33 [-3.33, -1.50] | (0.5,0.5) -3.059 | 0.817 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=3 | 12 | 1.00 | -3.00 [-4.33, -1.83] | (0.5,0.5) -4.057 | 0.576 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=4 | 12 | 1.00 | -2.00 [-2.83, -1.17] | (0.5,0.5) -3.067 | 0.707 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=1 | 12 | 1.00 | -4.67 [-6.00, -3.50] | (0.5,0.5) -6.815 | 0.025 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=2 | 12 | 1.00 | -3.67 [-5.00, -2.50] | (0.5,0.5) -4.553 | 0.467 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=3 | 12 | 1.00 | -3.17 [-4.67, -1.83] | (0.5,0.5) -4.682 | 0.392 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=4 | 12 | 1.00 | -3.00 [-3.83, -2.17] | (0.5,0.5) -3.636 | 0.497 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=1 | 12 | 1.00 | -3.33 [-4.67, -2.00] | (0.5,0.5) -4.970 | 0.372 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=2 | 12 | 1.00 | -4.17 [-5.17, -3.17] | (0.5,0.5) -6.268 | 0.073 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=3 | 12 | 1.00 | -5.00 [-6.00, -3.83] | (0.5,0.5) -7.211 | -0.481 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=4 | 12 | 1.00 | -4.00 [-5.17, -2.83] | (0.5,0.5) -5.058 | 0.219 | - | - | - |
