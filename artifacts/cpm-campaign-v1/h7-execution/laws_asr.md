# H7 execution-closure laws

Each row is one degradation curve (trace-level rate vs provenance error rate p). `slope@0.1` is (y(0.1)-y(0))/0.1 with a 95% trace-cluster bootstrap CI. `free (m,k)` is the best-fitting compound law y = y0 + (1-y0)(1-(1-p)^m)^k; `structural` is the same family with m, k fixed by trace structure (0 free parameters). R² is computed on the p>0 points; `max|res|` is the largest absolute residual.

| operator | defense | group | traces | y0 | slope@0.1 [CI] | free (m,k) R² | linear R² | structural law | structural R² | max\|res\| |
|---|---|---|---:|---:|---|---|---:|---|---:|---:|
| `semantic_replay` | grant_revalidated | propagate=True, n=1, retries=1 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1,1) 0.967 | 0.977 | any-retry-slot(n*r) (m=1, k=1) | 0.967 | 0.100 |
| `semantic_replay` | grant_revalidated | propagate=True, n=1, retries=2 | 4 | 0.00 | 3.00 [2.00, 4.00] | (2.5,1) 0.989 | 0.713 | any-retry-slot(n*r) (m=2, k=1) | 0.955 | 0.110 |
| `semantic_replay` | grant_revalidated | propagate=True, n=1, retries=3 | 4 | 0.00 | 2.50 [0.00, 5.00] | (2.5,1) 0.987 | 0.721 | any-retry-slot(n*r) (m=3, k=1) | 0.984 | 0.078 |
| `semantic_replay` | grant_revalidated | propagate=True, n=2, retries=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (2,1.5) 0.991 | 0.956 | any-retry-slot(n*r) (m=2, k=1) | 0.941 | 0.140 |
| `semantic_replay` | grant_revalidated | propagate=True, n=2, retries=2 | 4 | 0.00 | 4.00 [2.00, 6.00] | (5.5,1) 0.990 | -0.029 | any-retry-slot(n*r) (m=4, k=1) | 0.936 | 0.166 |
| `semantic_replay` | grant_revalidated | propagate=True, n=2, retries=3 | 4 | 0.00 | 2.00 [0.00, 4.50] | (9.5,3) 0.985 | 0.408 | any-retry-slot(n*r) (m=6, k=1) | 0.898 | 0.269 |
| `semantic_replay` | grant_revalidated | propagate=True, n=3, retries=1 | 4 | 0.00 | 2.00 [0.50, 3.50] | (3,1) 0.978 | 0.688 | any-retry-slot(n*r) (m=3, k=1) | 0.978 | 0.075 |
| `semantic_replay` | grant_revalidated | propagate=True, n=3, retries=2 | 4 | 0.00 | 6.50 [5.00, 8.00] | (8.5,1) 0.974 | -1.051 | any-retry-slot(n*r) (m=6, k=1) | 0.911 | 0.181 |
| `semantic_replay` | grant_revalidated | propagate=True, n=3, retries=3 | 4 | 0.00 | 5.00 [4.00, 7.00] | (4,0.5) 0.958 | -1.409 | any-retry-slot(n*r) (m=9, k=1) | 0.942 | 0.113 |
| `semantic_replay` | grant_revalidated | propagate=True, n=4, retries=1 | 4 | 0.00 | 3.00 [2.00, 4.00] | (4,1) 0.989 | 0.365 | any-retry-slot(n*r) (m=4, k=1) | 0.989 | 0.065 |
| `semantic_replay` | grant_revalidated | propagate=True, n=4, retries=2 | 4 | 0.00 | 6.50 [4.50, 9.00] | (5.5,0.5) 0.998 | -3.295 | any-retry-slot(n*r) (m=8, k=1) | 0.857 | 0.163 |
| `semantic_replay` | grant_revalidated | propagate=True, n=4, retries=3 | 4 | 0.00 | 6.00 [4.00, 8.50] | (5,0.5) 0.964 | -3.305 | any-retry-slot(n*r) (m=12, k=1) | 0.835 | 0.118 |
| `semantic_replay` | grant_single_use | propagate=True, n=1, retries=1 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1,1) 0.967 | 0.977 | any-retry-slot(n*r) (m=1, k=1) | 0.967 | 0.100 |
| `semantic_replay` | grant_single_use | propagate=True, n=1, retries=2 | 4 | 0.00 | 3.00 [2.00, 4.00] | (2.5,1) 0.989 | 0.713 | any-retry-slot(n*r) (m=2, k=1) | 0.955 | 0.110 |
| `semantic_replay` | grant_single_use | propagate=True, n=1, retries=3 | 4 | 0.00 | 2.50 [0.00, 5.00] | (2.5,1) 0.987 | 0.721 | any-retry-slot(n*r) (m=3, k=1) | 0.984 | 0.078 |
| `semantic_replay` | grant_single_use | propagate=True, n=2, retries=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (2,1.5) 0.991 | 0.956 | any-retry-slot(n*r) (m=2, k=1) | 0.941 | 0.140 |
| `semantic_replay` | grant_single_use | propagate=True, n=2, retries=2 | 4 | 0.00 | 4.00 [2.00, 6.00] | (5.5,1) 0.990 | -0.029 | any-retry-slot(n*r) (m=4, k=1) | 0.936 | 0.166 |
| `semantic_replay` | grant_single_use | propagate=True, n=2, retries=3 | 4 | 0.00 | 2.00 [0.00, 4.50] | (9.5,3) 0.985 | 0.408 | any-retry-slot(n*r) (m=6, k=1) | 0.898 | 0.269 |
| `semantic_replay` | grant_single_use | propagate=True, n=3, retries=1 | 4 | 0.00 | 2.00 [0.50, 3.50] | (3,1) 0.978 | 0.688 | any-retry-slot(n*r) (m=3, k=1) | 0.978 | 0.075 |
| `semantic_replay` | grant_single_use | propagate=True, n=3, retries=2 | 4 | 0.00 | 6.50 [5.00, 8.00] | (8.5,1) 0.974 | -1.051 | any-retry-slot(n*r) (m=6, k=1) | 0.911 | 0.181 |
| `semantic_replay` | grant_single_use | propagate=True, n=3, retries=3 | 4 | 0.00 | 5.00 [4.00, 7.00] | (4,0.5) 0.958 | -1.409 | any-retry-slot(n*r) (m=9, k=1) | 0.942 | 0.113 |
| `semantic_replay` | grant_single_use | propagate=True, n=4, retries=1 | 4 | 0.00 | 3.00 [2.00, 4.00] | (4,1) 0.989 | 0.365 | any-retry-slot(n*r) (m=4, k=1) | 0.989 | 0.065 |
| `semantic_replay` | grant_single_use | propagate=True, n=4, retries=2 | 4 | 0.00 | 6.50 [4.50, 9.00] | (5.5,0.5) 0.998 | -3.295 | any-retry-slot(n*r) (m=8, k=1) | 0.857 | 0.163 |
| `semantic_replay` | grant_single_use | propagate=True, n=4, retries=3 | 4 | 0.00 | 6.00 [4.00, 8.50] | (5,0.5) 0.964 | -3.305 | any-retry-slot(n*r) (m=12, k=1) | 0.835 | 0.118 |
| `semantic_replay` | intent_ledger | propagate=True, n=1, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=1, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=1, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=2, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=2, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=2, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=3, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=3, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=3, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=4, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=4, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | intent_ledger | propagate=True, n=4, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `semantic_replay` | no_policy | propagate=True, n=1, retries=1 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1,1) 0.967 | 0.977 | any-retry-slot(n*r) (m=1, k=1) | 0.967 | 0.100 |
| `semantic_replay` | no_policy | propagate=True, n=1, retries=2 | 4 | 0.00 | 3.00 [2.00, 4.00] | (2.5,1) 0.989 | 0.713 | any-retry-slot(n*r) (m=2, k=1) | 0.955 | 0.110 |
| `semantic_replay` | no_policy | propagate=True, n=1, retries=3 | 4 | 0.00 | 2.50 [0.00, 5.00] | (2.5,1) 0.987 | 0.721 | any-retry-slot(n*r) (m=3, k=1) | 0.984 | 0.078 |
| `semantic_replay` | no_policy | propagate=True, n=2, retries=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (2,1.5) 0.991 | 0.956 | any-retry-slot(n*r) (m=2, k=1) | 0.941 | 0.140 |
| `semantic_replay` | no_policy | propagate=True, n=2, retries=2 | 4 | 0.00 | 4.00 [2.00, 6.00] | (5.5,1) 0.990 | -0.029 | any-retry-slot(n*r) (m=4, k=1) | 0.936 | 0.166 |
| `semantic_replay` | no_policy | propagate=True, n=2, retries=3 | 4 | 0.00 | 2.00 [0.00, 4.50] | (9.5,3) 0.985 | 0.408 | any-retry-slot(n*r) (m=6, k=1) | 0.898 | 0.269 |
| `semantic_replay` | no_policy | propagate=True, n=3, retries=1 | 4 | 0.00 | 2.00 [0.50, 3.50] | (3,1) 0.978 | 0.688 | any-retry-slot(n*r) (m=3, k=1) | 0.978 | 0.075 |
| `semantic_replay` | no_policy | propagate=True, n=3, retries=2 | 4 | 0.00 | 6.50 [5.00, 8.00] | (8.5,1) 0.974 | -1.051 | any-retry-slot(n*r) (m=6, k=1) | 0.911 | 0.181 |
| `semantic_replay` | no_policy | propagate=True, n=3, retries=3 | 4 | 0.00 | 5.00 [4.00, 7.00] | (4,0.5) 0.958 | -1.409 | any-retry-slot(n*r) (m=9, k=1) | 0.942 | 0.113 |
| `semantic_replay` | no_policy | propagate=True, n=4, retries=1 | 4 | 0.00 | 3.00 [2.00, 4.00] | (4,1) 0.989 | 0.365 | any-retry-slot(n*r) (m=4, k=1) | 0.989 | 0.065 |
| `semantic_replay` | no_policy | propagate=True, n=4, retries=2 | 4 | 0.00 | 6.50 [4.50, 9.00] | (5.5,0.5) 0.998 | -3.295 | any-retry-slot(n*r) (m=8, k=1) | 0.857 | 0.163 |
| `semantic_replay` | no_policy | propagate=True, n=4, retries=3 | 4 | 0.00 | 6.00 [4.00, 8.50] | (5,0.5) 0.964 | -3.305 | any-retry-slot(n*r) (m=12, k=1) | 0.835 | 0.118 |
| `stale_version` | grant_revalidated | propagate=True, n=1, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=1, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=1, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=2, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=2, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=2, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=3, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=3, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=3, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=4, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=4, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_revalidated | propagate=True, n=4, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | grant_single_use | propagate=True, n=1, retries=1 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1,1) 0.986 | 0.991 | any-action(n) (m=1, k=1) | 0.986 | 0.050 |
| `stale_version` | grant_single_use | propagate=True, n=1, retries=2 | 4 | 0.00 | 1.00 [0.00, 3.00] | (1.5,1) 0.985 | 0.970 | any-action(n) (m=1, k=1) | 0.958 | 0.150 |
| `stale_version` | grant_single_use | propagate=True, n=1, retries=3 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1.5,1) 0.963 | 0.953 | any-action(n) (m=1, k=1) | 0.947 | 0.150 |
| `stale_version` | grant_single_use | propagate=True, n=2, retries=1 | 4 | 0.00 | 2.00 [0.00, 4.00] | (4,1.5) 0.971 | 0.750 | any-action(n) (m=2, k=1) | 0.931 | 0.213 |
| `stale_version` | grant_single_use | propagate=True, n=2, retries=2 | 4 | 0.00 | 2.50 [0.50, 5.00] | (1,0.5) 0.963 | 0.814 | any-action(n) (m=2, k=1) | 0.909 | 0.152 |
| `stale_version` | grant_single_use | propagate=True, n=2, retries=3 | 4 | 0.00 | 2.00 [0.50, 3.50] | (2.5,1) 0.977 | 0.717 | any-action(n) (m=2, k=1) | 0.949 | 0.162 |
| `stale_version` | grant_single_use | propagate=True, n=3, retries=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (6,4) 0.998 | 0.816 | any-action(n) (m=3, k=1) | 0.925 | 0.221 |
| `stale_version` | grant_single_use | propagate=True, n=3, retries=2 | 4 | 0.00 | 2.50 [0.00, 5.00] | (6,2) 0.997 | 0.649 | any-action(n) (m=3, k=1) | 0.977 | 0.093 |
| `stale_version` | grant_single_use | propagate=True, n=3, retries=3 | 4 | 0.00 | 2.00 [2.00, 2.00] | (8,2.5) 0.985 | 0.479 | any-action(n) (m=3, k=1) | 0.925 | 0.222 |
| `stale_version` | grant_single_use | propagate=True, n=4, retries=1 | 4 | 0.00 | 3.50 [1.00, 6.50] | (4,1) 0.979 | 0.347 | any-action(n) (m=4, k=1) | 0.979 | 0.088 |
| `stale_version` | grant_single_use | propagate=True, n=4, retries=2 | 4 | 0.00 | 3.00 [1.00, 5.00] | (3,1) 0.981 | 0.695 | any-action(n) (m=4, k=1) | 0.945 | 0.184 |
| `stale_version` | grant_single_use | propagate=True, n=4, retries=3 | 4 | 0.00 | 4.00 [2.00, 6.00] | (7,1.5) 0.999 | 0.226 | any-action(n) (m=4, k=1) | 0.967 | 0.116 |
| `stale_version` | intent_ledger | propagate=True, n=1, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=1, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=1, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=2, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=2, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=2, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=3, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=3, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=3, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=4, retries=1 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=4, retries=2 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | intent_ledger | propagate=True, n=4, retries=3 | 4 | 0.00 | 0.00 [0.00, 0.00] | (0.5,8) n/a | 1.000 | - | - | - |
| `stale_version` | no_policy | propagate=True, n=1, retries=1 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1,1) 0.986 | 0.991 | any-action(n) (m=1, k=1) | 0.986 | 0.050 |
| `stale_version` | no_policy | propagate=True, n=1, retries=2 | 4 | 0.00 | 1.00 [0.00, 3.00] | (1.5,1) 0.985 | 0.970 | any-action(n) (m=1, k=1) | 0.958 | 0.150 |
| `stale_version` | no_policy | propagate=True, n=1, retries=3 | 4 | 0.00 | 1.50 [0.50, 2.00] | (1.5,1) 0.963 | 0.953 | any-action(n) (m=1, k=1) | 0.947 | 0.150 |
| `stale_version` | no_policy | propagate=True, n=2, retries=1 | 4 | 0.00 | 2.00 [0.00, 4.00] | (4,1.5) 0.971 | 0.750 | any-action(n) (m=2, k=1) | 0.931 | 0.213 |
| `stale_version` | no_policy | propagate=True, n=2, retries=2 | 4 | 0.00 | 2.50 [0.50, 5.00] | (1,0.5) 0.963 | 0.814 | any-action(n) (m=2, k=1) | 0.909 | 0.152 |
| `stale_version` | no_policy | propagate=True, n=2, retries=3 | 4 | 0.00 | 2.00 [0.50, 3.50] | (2.5,1) 0.977 | 0.717 | any-action(n) (m=2, k=1) | 0.949 | 0.162 |
| `stale_version` | no_policy | propagate=True, n=3, retries=1 | 4 | 0.00 | 0.50 [0.00, 1.50] | (6,4) 0.998 | 0.816 | any-action(n) (m=3, k=1) | 0.925 | 0.221 |
| `stale_version` | no_policy | propagate=True, n=3, retries=2 | 4 | 0.00 | 2.50 [0.00, 5.00] | (6,2) 0.997 | 0.649 | any-action(n) (m=3, k=1) | 0.977 | 0.093 |
| `stale_version` | no_policy | propagate=True, n=3, retries=3 | 4 | 0.00 | 2.00 [2.00, 2.00] | (8,2.5) 0.985 | 0.479 | any-action(n) (m=3, k=1) | 0.925 | 0.222 |
| `stale_version` | no_policy | propagate=True, n=4, retries=1 | 4 | 0.00 | 3.50 [1.00, 6.50] | (4,1) 0.979 | 0.347 | any-action(n) (m=4, k=1) | 0.979 | 0.088 |
| `stale_version` | no_policy | propagate=True, n=4, retries=2 | 4 | 0.00 | 3.00 [1.00, 5.00] | (3,1) 0.981 | 0.695 | any-action(n) (m=4, k=1) | 0.945 | 0.184 |
| `stale_version` | no_policy | propagate=True, n=4, retries=3 | 4 | 0.00 | 4.00 [2.00, 6.00] | (7,1.5) 0.999 | 0.226 | any-action(n) (m=4, k=1) | 0.967 | 0.116 |
