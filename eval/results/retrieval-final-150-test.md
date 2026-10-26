# Retrieval evaluation: final-150-test

31 answerable questions · index `index` · 20261025-163220

| setup | recall@1 | recall@3 | recall@5 | recall@10 | MRR@10 | p50 ms | p95 ms |
|---|---|---|---|---|---|---|---|
| bm25 | 0.323 | 0.452 | 0.581 | 0.645 | 0.426 | 0 | 0 |
| vector | 0.452 | 0.581 | 0.677 | 0.774 | 0.544 | 6 | 8 |
| hybrid | 0.387 | 0.613 | 0.645 | 0.742 | 0.501 | 6 | 7 |
| hybrid+rerank | 0.484 | 0.806 | 0.806 | 0.806 | 0.629 | 2500 | 5186 |

### Recall@5 by type

| type | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| conflict | 1 | 0.00 | 0.00 | 0.00 | 0.00 |
| cross_lingual | 8 | 0.12 | 0.38 | 0.12 | 0.50 |
| date | 3 | 0.67 | 1.00 | 0.67 | 1.00 |
| fact | 4 | 1.00 | 0.75 | 1.00 | 1.00 |
| list | 2 | 1.00 | 1.00 | 1.00 | 1.00 |
| number | 10 | 0.80 | 0.80 | 0.90 | 1.00 |
| yes_no | 3 | 0.33 | 0.67 | 0.67 | 0.67 |

### Recall@5 by country

| country | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| canada | 6 | 0.50 | 0.67 | 0.67 | 0.83 |
| erasmus | 4 | 0.50 | 0.75 | 0.50 | 1.00 |
| france | 11 | 0.55 | 0.64 | 0.64 | 0.82 |
| germany | 10 | 0.70 | 0.70 | 0.70 | 0.70 |

### Recall@5 by lang

| lang | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| en | 13 | 0.62 | 0.62 | 0.69 | 0.77 |
| fr | 18 | 0.56 | 0.72 | 0.61 | 0.83 |

### Recall@5 by difficulty

| difficulty | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| easy | 13 | 0.69 | 0.92 | 0.77 | 0.92 |
| hard | 3 | 0.00 | 0.00 | 0.33 | 0.67 |
| medium | 15 | 0.60 | 0.60 | 0.60 | 0.73 |

Quotes not inside any single chunk (0): none

Misses of the best setup (hybrid+rerank, top 10, 6): q002, q027, q044, q047, q049, q083
