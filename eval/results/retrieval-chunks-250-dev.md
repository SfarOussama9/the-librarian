# Retrieval evaluation: chunks-250-dev

79 answerable questions · index `index` · 20261025-161928

| setup | recall@1 | recall@3 | recall@5 | recall@10 | MRR@10 | p50 ms | p95 ms |
|---|---|---|---|---|---|---|---|
| bm25 | 0.430 | 0.658 | 0.696 | 0.785 | 0.554 | 0 | 0 |
| vector | 0.392 | 0.671 | 0.772 | 0.848 | 0.558 | 6 | 7 |
| hybrid | 0.443 | 0.696 | 0.785 | 0.886 | 0.588 | 6 | 7 |
| hybrid+rerank | 0.696 | 0.873 | 0.899 | 0.924 | 0.785 | 3936 | 9659 |

### Recall@5 by type

| type | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| conflict | 3 | 0.67 | 0.67 | 0.67 | 0.67 |
| cross_lingual | 19 | 0.37 | 0.63 | 0.47 | 0.74 |
| date | 8 | 1.00 | 0.75 | 0.88 | 1.00 |
| fact | 9 | 0.67 | 0.67 | 0.89 | 1.00 |
| list | 1 | 1.00 | 1.00 | 1.00 | 1.00 |
| number | 30 | 0.83 | 0.90 | 0.93 | 0.93 |
| stale | 1 | 0.00 | 0.00 | 0.00 | 1.00 |
| yes_no | 8 | 0.75 | 0.88 | 0.88 | 1.00 |

### Recall@5 by country

| country | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| canada | 17 | 0.53 | 0.76 | 0.71 | 0.88 |
| erasmus | 9 | 0.67 | 0.89 | 0.78 | 0.89 |
| france | 31 | 0.61 | 0.71 | 0.74 | 0.90 |
| germany | 22 | 0.95 | 0.82 | 0.91 | 0.91 |

### Recall@5 by lang

| lang | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| en | 45 | 0.67 | 0.82 | 0.76 | 0.93 |
| fr | 34 | 0.74 | 0.71 | 0.82 | 0.85 |

### Recall@5 by difficulty

| difficulty | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| easy | 27 | 0.70 | 0.85 | 0.89 | 0.96 |
| hard | 16 | 0.69 | 0.69 | 0.75 | 0.88 |
| medium | 36 | 0.69 | 0.75 | 0.72 | 0.86 |

Quotes not inside any single chunk (0): none

Misses of the best setup (hybrid+rerank, top 10, 6): q012, q050, q055, q081, q087, q102
