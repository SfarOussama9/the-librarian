# Retrieval evaluation: depth-20-dev

79 answerable questions · index `index` · 20261025-184906

| setup | recall@1 | recall@3 | recall@5 | recall@10 | MRR@10 | p50 ms | p95 ms |
|---|---|---|---|---|---|---|---|
| bm25 | 0.405 | 0.595 | 0.684 | 0.772 | 0.524 | 0 | 0 |
| vector | 0.557 | 0.671 | 0.734 | 0.823 | 0.639 | 6 | 7 |
| hybrid | 0.481 | 0.633 | 0.759 | 0.835 | 0.584 | 6 | 7 |
| hybrid+rerank | 0.722 | 0.861 | 0.911 | 0.924 | 0.798 | 2435 | 4781 |

### Recall@5 by type

| type | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| conflict | 3 | 0.33 | 0.67 | 0.67 | 0.67 |
| cross_lingual | 19 | 0.37 | 0.53 | 0.47 | 0.79 |
| date | 8 | 1.00 | 0.88 | 1.00 | 1.00 |
| fact | 9 | 0.89 | 0.78 | 0.89 | 1.00 |
| list | 1 | 1.00 | 1.00 | 1.00 | 1.00 |
| number | 30 | 0.77 | 0.77 | 0.83 | 0.93 |
| stale | 1 | 0.00 | 1.00 | 0.00 | 1.00 |
| yes_no | 8 | 0.75 | 0.88 | 0.88 | 1.00 |

### Recall@5 by country

| country | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| canada | 17 | 0.53 | 0.71 | 0.71 | 0.88 |
| erasmus | 9 | 0.78 | 0.89 | 0.78 | 1.00 |
| france | 31 | 0.65 | 0.71 | 0.71 | 0.90 |
| germany | 22 | 0.82 | 0.73 | 0.86 | 0.91 |

### Recall@5 by lang

| lang | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| en | 45 | 0.67 | 0.76 | 0.73 | 0.91 |
| fr | 34 | 0.71 | 0.71 | 0.79 | 0.91 |

### Recall@5 by difficulty

| difficulty | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| easy | 27 | 0.74 | 0.81 | 0.81 | 0.96 |
| hard | 16 | 0.56 | 0.75 | 0.75 | 0.88 |
| medium | 36 | 0.69 | 0.67 | 0.72 | 0.89 |

Quotes not inside any single chunk (0): none

Misses of the best setup (hybrid+rerank, top 10, 6): q012, q015, q050, q055, q081, q087
