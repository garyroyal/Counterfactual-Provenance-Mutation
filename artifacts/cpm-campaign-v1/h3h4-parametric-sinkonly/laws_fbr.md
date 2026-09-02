# H3/H4 structural FBR laws (sinkonly)

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `drop_label` | label_trusting | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6.5) 0.996 | 0.884 | sink-only(k) (m=1, k=1) | 0.877 | 0.250 |
| `drop_label` | label_trusting | propagate=False, depth=1, k=2 | 4 | 0.00 | 3.50 [2.00, 5.00] | (1,0.5) 0.964 | 0.774 | sink-only(k) (m=2, k=1) | 0.955 | 0.160 |
| `drop_label` | label_trusting | propagate=False, depth=1, k=3 | 4 | 0.00 | 3.00 [2.00, 4.00] | (3.5,1) 0.978 | 0.533 | sink-only(k) (m=3, k=1) | 0.976 | 0.107 |
| `drop_label` | label_trusting | propagate=False, depth=1, k=4 | 4 | 0.00 | 5.00 [3.00, 7.00] | (5,1) 0.975 | 0.099 | sink-only(k) (m=4, k=1) | 0.953 | 0.156 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=1 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1.5) 0.988 | 0.970 | sink-only(k) (m=1, k=1) | 0.955 | 0.150 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=2 | 4 | 0.00 | 2.50 [0.00, 5.00] | (3,1) 0.989 | 0.622 | sink-only(k) (m=2, k=1) | 0.907 | 0.213 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=3 | 4 | 0.00 | 2.00 [0.00, 4.00] | (3.5,1.5) 0.993 | 0.801 | sink-only(k) (m=3, k=1) | 0.971 | 0.128 |
| `drop_label` | label_trusting | propagate=False, depth=2, k=4 | 4 | 0.00 | 5.00 [3.00, 7.50] | (4.5,1) 0.961 | 0.221 | sink-only(k) (m=4, k=1) | 0.951 | 0.156 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=1 | 4 | 0.00 | 2.00 [0.50, 3.50] | (0.5,1) 0.883 | 0.892 | sink-only(k) (m=1, k=1) | 0.852 | 0.200 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=2 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1.5,1) 0.995 | 0.966 | sink-only(k) (m=2, k=1) | 0.947 | 0.138 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=3 | 4 | 0.00 | 4.00 [2.50, 5.50] | (3.5,1) 0.960 | 0.544 | sink-only(k) (m=3, k=1) | 0.953 | 0.129 |
| `drop_label` | label_trusting | propagate=False, depth=3, k=4 | 4 | 0.00 | 4.00 [2.50, 5.50] | (4.5,1) 0.988 | 0.327 | sink-only(k) (m=4, k=1) | 0.983 | 0.066 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1.5,1.5) 0.993 | 0.983 | sink-only(k) (m=1, k=1) | 0.983 | 0.100 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=2 | 4 | 0.00 | 2.00 [2.00, 2.00] | (3.5,1.5) 0.984 | 0.818 | sink-only(k) (m=2, k=1) | 0.968 | 0.150 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=3 | 4 | 0.00 | 2.50 [2.00, 3.50] | (3,1) 0.990 | 0.728 | sink-only(k) (m=3, k=1) | 0.990 | 0.078 |
| `drop_label` | label_trusting | propagate=False, depth=4, k=4 | 4 | 0.00 | 3.50 [2.50, 4.00] | (3.5,1) 0.993 | 0.510 | sink-only(k) (m=4, k=1) | 0.986 | 0.084 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=1 | 4 | 0.00 | 1.00 [0.00, 3.00] | (2,1.5) 0.993 | 0.964 | sink-only(k) (m=1, k=1) | 0.937 | 0.150 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=2 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1) 0.992 | 0.909 | sink-only(k) (m=2, k=1) | 0.992 | 0.050 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=3 | 4 | 0.00 | 4.00 [2.50, 5.50] | (3.5,1) 0.977 | 0.484 | sink-only(k) (m=3, k=1) | 0.960 | 0.129 |
| `drop_label` | label_trusting | propagate=False, depth=5, k=4 | 4 | 0.00 | 3.00 [2.00, 4.00] | (3.5,1) 0.993 | 0.515 | sink-only(k) (m=4, k=1) | 0.993 | 0.044 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (2.5,6.5) 0.996 | 0.884 | sink-only(k) (m=1, k=1) | 0.877 | 0.250 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=2 | 4 | 0.00 | 3.50 [2.00, 5.00] | (1,0.5) 0.964 | 0.774 | sink-only(k) (m=2, k=1) | 0.955 | 0.160 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=3 | 4 | 0.00 | 3.00 [2.00, 4.00] | (3.5,1) 0.978 | 0.533 | sink-only(k) (m=3, k=1) | 0.976 | 0.107 |
| `drop_label` | lineage_verifying | propagate=False, depth=1, k=4 | 4 | 0.00 | 5.00 [3.00, 7.00] | (5,1) 0.975 | 0.099 | sink-only(k) (m=4, k=1) | 0.953 | 0.156 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=1 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1.5) 0.988 | 0.970 | sink-only(k) (m=1, k=1) | 0.955 | 0.150 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=2 | 4 | 0.00 | 2.50 [0.00, 5.00] | (3,1) 0.989 | 0.622 | sink-only(k) (m=2, k=1) | 0.907 | 0.213 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=3 | 4 | 0.00 | 2.00 [0.00, 4.00] | (3.5,1.5) 0.993 | 0.801 | sink-only(k) (m=3, k=1) | 0.971 | 0.128 |
| `drop_label` | lineage_verifying | propagate=False, depth=2, k=4 | 4 | 0.00 | 5.00 [3.00, 7.50] | (4.5,1) 0.961 | 0.221 | sink-only(k) (m=4, k=1) | 0.951 | 0.156 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=1 | 4 | 0.00 | 2.00 [0.50, 3.50] | (0.5,1) 0.883 | 0.892 | sink-only(k) (m=1, k=1) | 0.852 | 0.200 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=2 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1.5,1) 0.995 | 0.966 | sink-only(k) (m=2, k=1) | 0.947 | 0.138 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=3 | 4 | 0.00 | 4.00 [2.50, 5.50] | (3.5,1) 0.960 | 0.544 | sink-only(k) (m=3, k=1) | 0.953 | 0.129 |
| `drop_label` | lineage_verifying | propagate=False, depth=3, k=4 | 4 | 0.00 | 4.00 [2.50, 5.50] | (4.5,1) 0.988 | 0.327 | sink-only(k) (m=4, k=1) | 0.983 | 0.066 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (1.5,1.5) 0.993 | 0.983 | sink-only(k) (m=1, k=1) | 0.983 | 0.100 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=2 | 4 | 0.00 | 2.00 [2.00, 2.00] | (3.5,1.5) 0.984 | 0.818 | sink-only(k) (m=2, k=1) | 0.968 | 0.150 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=3 | 4 | 0.00 | 2.50 [2.00, 3.50] | (3,1) 0.990 | 0.728 | sink-only(k) (m=3, k=1) | 0.990 | 0.078 |
| `drop_label` | lineage_verifying | propagate=False, depth=4, k=4 | 4 | 0.00 | 3.50 [2.50, 4.00] | (3.5,1) 0.993 | 0.510 | sink-only(k) (m=4, k=1) | 0.986 | 0.084 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=1 | 4 | 0.00 | 1.00 [0.00, 3.00] | (2,1.5) 0.993 | 0.964 | sink-only(k) (m=1, k=1) | 0.937 | 0.150 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=2 | 4 | 0.00 | 1.50 [0.00, 3.00] | (2,1) 0.992 | 0.909 | sink-only(k) (m=2, k=1) | 0.992 | 0.050 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=3 | 4 | 0.00 | 4.00 [2.50, 5.50] | (3.5,1) 0.977 | 0.484 | sink-only(k) (m=3, k=1) | 0.960 | 0.129 |
| `drop_label` | lineage_verifying | propagate=False, depth=5, k=4 | 4 | 0.00 | 3.00 [2.00, 4.00] | (3.5,1) 0.993 | 0.515 | sink-only(k) (m=4, k=1) | 0.993 | 0.044 |
| `drop_label` | no_policy | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | no_policy | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | origin_routing | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `drop_label` | whole_call_quarantine | propagate=False, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | label_trusting | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | lineage_verifying | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | no_policy | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | origin_routing | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `forge_label` | whole_call_quarantine | propagate=False, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=1 | 4 | 0.00 | 1.00 [0.00, 2.00] | (1.5,2) 0.988 | 0.964 | sink-only(k) (m=1, k=1) | 0.959 | 0.150 |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=2 | 4 | 0.00 | 2.00 [0.50, 3.50] | (1.5,1) 0.976 | 0.949 | sink-only(k) (m=2, k=1) | 0.935 | 0.200 |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=3 | 4 | 0.00 | 4.50 [4.00, 5.50] | (2,0.5) 0.994 | 0.062 | sink-only(k) (m=3, k=1) | 0.858 | 0.179 |
| `merge_taint` | label_trusting | propagate=False, depth=1, k=4 | 4 | 0.00 | 5.50 [4.50, 6.00] | (4,0.5) 0.989 | -1.242 | sink-only(k) (m=4, k=1) | 0.652 | 0.215 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=1 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1.5,1) 0.992 | 0.932 | sink-only(k) (m=1, k=1) | 0.888 | 0.200 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=2 | 4 | 0.00 | 2.50 [1.00, 4.00] | (2,1) 0.990 | 0.881 | sink-only(k) (m=2, k=1) | 0.990 | 0.060 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=3 | 4 | 0.00 | 4.00 [1.50, 6.00] | (4.5,1) 0.985 | 0.268 | sink-only(k) (m=3, k=1) | 0.927 | 0.129 |
| `merge_taint` | label_trusting | propagate=False, depth=2, k=4 | 4 | 0.00 | 2.50 [1.00, 4.00] | (3,1) 0.990 | 0.728 | sink-only(k) (m=4, k=1) | 0.939 | 0.184 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=1 | 4 | 0.00 | 1.00 [0.00, 2.00] | (0.5,1) 0.974 | 0.870 | sink-only(k) (m=1, k=1) | 0.768 | 0.300 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=2 | 4 | 0.00 | 2.50 [1.00, 4.00] | (2,1) 0.975 | 0.887 | sink-only(k) (m=2, k=1) | 0.975 | 0.088 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=3 | 4 | 0.00 | 2.00 [0.50, 3.50] | (2.5,1) 0.977 | 0.746 | sink-only(k) (m=3, k=1) | 0.966 | 0.125 |
| `merge_taint` | label_trusting | propagate=False, depth=3, k=4 | 4 | 0.00 | 2.00 [2.00, 2.00] | (4,1.5) 0.994 | 0.738 | sink-only(k) (m=4, k=1) | 0.946 | 0.144 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=1 | 4 | 0.00 | 1.50 [0.00, 3.00] | (1.5,1) 0.991 | 0.957 | sink-only(k) (m=1, k=1) | 0.940 | 0.150 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=2 | 4 | 0.00 | 1.50 [0.50, 2.00] | (2,1) 0.976 | 0.889 | sink-only(k) (m=2, k=1) | 0.976 | 0.100 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=3 | 4 | 0.00 | 4.00 [2.50, 5.50] | (3.5,1) 0.971 | 0.495 | sink-only(k) (m=3, k=1) | 0.963 | 0.129 |
| `merge_taint` | label_trusting | propagate=False, depth=4, k=4 | 4 | 0.00 | 3.00 [2.00, 4.00] | (3.5,1) 0.998 | 0.615 | sink-only(k) (m=4, k=1) | 0.983 | 0.084 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=1 | 4 | 0.00 | 1.00 [0.00, 3.00] | (1.5,1) 0.983 | 0.987 | sink-only(k) (m=1, k=1) | 0.980 | 0.100 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=2 | 4 | 0.00 | 1.50 [0.00, 3.00] | (1.5,1) 0.986 | 0.959 | sink-only(k) (m=2, k=1) | 0.945 | 0.150 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=3 | 4 | 0.00 | 2.50 [0.00, 5.00] | (4.5,1.5) 0.996 | 0.651 | sink-only(k) (m=3, k=1) | 0.988 | 0.075 |
| `merge_taint` | label_trusting | propagate=False, depth=5, k=4 | 4 | 0.00 | 3.50 [1.00, 6.00] | (3.5,1) 0.991 | 0.560 | sink-only(k) (m=4, k=1) | 0.986 | 0.085 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=1 | 4 | 0.00 | 1.00 [0.00, 2.00] | (1.5,2) 0.988 | 0.964 | any-hop(d*k) [structural propagation] (m=1, k=1) | 0.959 | 0.150 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=2 | 4 | 0.00 | 2.00 [0.50, 3.50] | (1.5,1) 0.976 | 0.949 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.935 | 0.200 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=3 | 4 | 0.00 | 4.50 [4.00, 5.50] | (2,0.5) 0.994 | 0.062 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.858 | 0.179 |
| `merge_taint` | lineage_verifying | propagate=False, depth=1, k=4 | 4 | 0.00 | 5.50 [4.50, 6.00] | (4,0.5) 0.989 | -1.242 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.652 | 0.215 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=1 | 4 | 0.00 | 2.00 [2.00, 2.00] | (3.5,1.5) 0.996 | 0.815 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.980 | 0.100 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=2 | 4 | 0.00 | 3.00 [1.00, 5.00] | (7,2) 0.997 | 0.487 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.982 | 0.085 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=3 | 4 | 0.00 | 7.00 [6.00, 8.00] | (5,0.5) 0.965 | -2.189 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.748 | 0.231 |
| `merge_taint` | lineage_verifying | propagate=False, depth=2, k=4 | 4 | 0.00 | 6.50 [4.50, 9.00] | (12,1.5) 0.988 | -1.149 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.981 | 0.080 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=1 | 4 | 0.00 | 2.50 [2.00, 3.50] | (1,0.5) 0.955 | 0.694 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.924 | 0.175 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=2 | 4 | 0.00 | 6.50 [5.00, 8.00] | (5,0.5) 0.934 | -3.951 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.369 | 0.285 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=3 | 4 | 0.00 | 7.00 [6.00, 8.00] | (15,1.5) 0.997 | -2.419 | any-hop(d*k) [structural propagation] (m=9, k=1) | 0.970 | 0.087 |
| `merge_taint` | lineage_verifying | propagate=False, depth=3, k=4 | 4 | 0.00 | 5.50 [4.50, 6.00] | (8.5,1) 0.986 | -1.439 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.912 | 0.168 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=1 | 4 | 0.00 | 2.50 [0.50, 5.00] | (4.5,1.5) 0.999 | 0.662 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.971 | 0.094 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=2 | 4 | 0.00 | 7.00 [6.00, 8.00] | (6.5,0.5) 0.991 | -3.994 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.792 | 0.163 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=3 | 4 | 0.00 | 7.50 [6.50, 8.00] | (13,1) 0.996 | -4.606 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.986 | 0.040 |
| `merge_taint` | lineage_verifying | propagate=False, depth=4, k=4 | 4 | 0.00 | 6.50 [5.00, 8.00] | (5,0.5) 0.994 | -2.422 | any-hop(d*k) [structural propagation] (m=16, k=1) | 0.777 | 0.165 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=1 | 4 | 0.00 | 4.00 [2.00, 6.00] | (5,1) 0.983 | 0.135 | any-hop(d*k) [structural propagation] (m=5, k=1) | 0.983 | 0.069 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=2 | 4 | 0.00 | 6.00 [4.50, 7.50] | (9.5,1) 0.984 | -1.812 | any-hop(d*k) [structural propagation] (m=10, k=1) | 0.984 | 0.056 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=3 | 4 | 0.00 | 7.50 [5.00, 9.50] | (8,0.5) 0.997 | -7.820 | any-hop(d*k) [structural propagation] (m=15, k=1) | 0.949 | 0.063 |
| `merge_taint` | lineage_verifying | propagate=False, depth=5, k=4 | 4 | 0.00 | 8.00 [6.00, 10.00] | (15.5,1) 0.999 | -6.789 | any-hop(d*k) [structural propagation] (m=20, k=1) | 0.916 | 0.092 |
| `merge_taint` | no_policy | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | no_policy | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=1 | 4 | 0.00 | 1.00 [0.00, 2.00] | (1.5,2) 0.988 | 0.964 | any-hop(d*k) [structural propagation] (m=1, k=1) | 0.959 | 0.150 |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=2 | 4 | 0.00 | 2.00 [0.50, 3.50] | (1.5,1) 0.976 | 0.949 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.935 | 0.200 |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=3 | 4 | 0.00 | 4.50 [4.00, 5.50] | (2,0.5) 0.994 | 0.062 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.858 | 0.179 |
| `merge_taint` | origin_routing | propagate=False, depth=1, k=4 | 4 | 0.00 | 5.50 [4.50, 6.00] | (4,0.5) 0.989 | -1.242 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.652 | 0.215 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=1 | 4 | 0.00 | 2.00 [2.00, 2.00] | (3.5,1.5) 0.996 | 0.815 | any-hop(d*k) [structural propagation] (m=2, k=1) | 0.980 | 0.100 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=2 | 4 | 0.00 | 3.00 [1.00, 5.00] | (7,2) 0.997 | 0.487 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.982 | 0.085 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=3 | 4 | 0.00 | 7.00 [6.00, 8.00] | (5,0.5) 0.965 | -2.189 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.748 | 0.231 |
| `merge_taint` | origin_routing | propagate=False, depth=2, k=4 | 4 | 0.00 | 6.50 [4.50, 9.00] | (12,1.5) 0.988 | -1.149 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.981 | 0.080 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=1 | 4 | 0.00 | 2.50 [2.00, 3.50] | (1,0.5) 0.955 | 0.694 | any-hop(d*k) [structural propagation] (m=3, k=1) | 0.924 | 0.175 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=2 | 4 | 0.00 | 6.50 [5.00, 8.00] | (5,0.5) 0.934 | -3.951 | any-hop(d*k) [structural propagation] (m=6, k=1) | 0.369 | 0.285 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=3 | 4 | 0.00 | 7.00 [6.00, 8.00] | (15,1.5) 0.997 | -2.419 | any-hop(d*k) [structural propagation] (m=9, k=1) | 0.970 | 0.087 |
| `merge_taint` | origin_routing | propagate=False, depth=3, k=4 | 4 | 0.00 | 5.50 [4.50, 6.00] | (8.5,1) 0.986 | -1.439 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.912 | 0.168 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=1 | 4 | 0.00 | 2.50 [0.50, 5.00] | (4.5,1.5) 0.999 | 0.662 | any-hop(d*k) [structural propagation] (m=4, k=1) | 0.971 | 0.094 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=2 | 4 | 0.00 | 7.00 [6.00, 8.00] | (6.5,0.5) 0.991 | -3.994 | any-hop(d*k) [structural propagation] (m=8, k=1) | 0.792 | 0.163 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=3 | 4 | 0.00 | 7.50 [6.50, 8.00] | (13,1) 0.996 | -4.606 | any-hop(d*k) [structural propagation] (m=12, k=1) | 0.986 | 0.040 |
| `merge_taint` | origin_routing | propagate=False, depth=4, k=4 | 4 | 0.00 | 6.50 [5.00, 8.00] | (5,0.5) 0.994 | -2.422 | any-hop(d*k) [structural propagation] (m=16, k=1) | 0.777 | 0.165 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=1 | 4 | 0.00 | 4.00 [2.00, 6.00] | (5,1) 0.983 | 0.135 | any-hop(d*k) [structural propagation] (m=5, k=1) | 0.983 | 0.069 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=2 | 4 | 0.00 | 6.00 [4.50, 7.50] | (9.5,1) 0.984 | -1.812 | any-hop(d*k) [structural propagation] (m=10, k=1) | 0.984 | 0.056 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=3 | 4 | 0.00 | 7.50 [5.00, 9.50] | (8,0.5) 0.997 | -7.820 | any-hop(d*k) [structural propagation] (m=15, k=1) | 0.949 | 0.063 |
| `merge_taint` | origin_routing | propagate=False, depth=5, k=4 | 4 | 0.00 | 8.00 [6.00, 10.00] | (15.5,1) 0.999 | -6.789 | any-hop(d*k) [structural propagation] (m=20, k=1) | 0.916 | 0.092 |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=2, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=3, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=4, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=1 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=2 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=3 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `merge_taint` | whole_call_quarantine | propagate=False, depth=5, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) 1.000 | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | label_trusting | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | lineage_verifying | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | no_policy | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=1, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=2, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=3, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=4, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | origin_routing | propagate=False, depth=5, k=4 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=1 | 4 | 1.00 | -2.00 [-2.00, -2.00] | (0.5,0.5) -2.561 | 0.898 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=2 | 4 | 1.00 | -2.50 [-4.00, -1.00] | (0.5,0.5) -3.105 | 0.872 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=3 | 4 | 1.00 | -1.00 [-2.00, 0.00] | (0.5,0.5) -2.098 | 0.941 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=1, k=4 | 4 | 1.00 | 0.00 [0.00, 0.00] | (0.5,0.5) -1.234 | 0.972 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=1 | 4 | 1.00 | -2.50 [-4.00, -1.00] | (0.5,0.5) -3.051 | 0.893 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=2 | 4 | 1.00 | -1.00 [-2.00, 0.00] | (0.5,0.5) -2.337 | 0.865 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=3 | 4 | 1.00 | -2.00 [-3.50, -0.50] | (0.5,0.5) -2.436 | 0.916 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=2, k=4 | 4 | 1.00 | -1.00 [-2.00, 0.00] | (0.5,0.5) -2.116 | 0.903 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=1 | 4 | 1.00 | -2.50 [-5.00, 0.00] | (0.5,0.5) -3.698 | 0.714 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=2 | 4 | 1.00 | -1.50 [-2.00, -0.50] | (0.5,0.5) -2.453 | 0.841 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=3 | 4 | 1.00 | -4.00 [-6.50, -2.00] | (0.5,0.5) -4.918 | 0.330 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=3, k=4 | 4 | 1.00 | -2.50 [-4.00, -1.00] | (0.5,0.5) -2.876 | 0.762 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=1 | 4 | 1.00 | -5.50 [-8.50, -4.00] | (0.5,0.5) -11.750 | -1.288 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=2 | 4 | 1.00 | -4.50 [-5.50, -4.00] | (0.5,0.5) -7.157 | -0.234 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=3 | 4 | 1.00 | -3.00 [-5.00, -1.00] | (0.5,0.5) -4.288 | 0.490 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=4, k=4 | 4 | 1.00 | -3.50 [-4.00, -2.50] | (0.5,0.5) -4.436 | 0.399 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=1 | 4 | 1.00 | -3.00 [-5.00, -1.00] | (0.5,0.5) -5.356 | 0.279 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=2 | 4 | 1.00 | -3.50 [-5.00, -2.00] | (0.5,0.5) -5.497 | 0.148 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=3 | 4 | 1.00 | -4.00 [-5.50, -2.50] | (0.5,0.5) -5.305 | 0.071 | - | - | - |
| `misattribute_parent` | whole_call_quarantine | propagate=False, depth=5, k=4 | 4 | 1.00 | -4.50 [-6.00, -3.00] | (0.5,0.5) -5.820 | -0.016 | - | - | - |
