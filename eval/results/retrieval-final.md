# Retrieval evaluation: final

110 answerable questions · index `index` · 20261026-013303

| setup | recall@1 | recall@3 | recall@5 | recall@10 | MRR@10 | p50 ms | p95 ms |
|---|---|---|---|---|---|---|---|
| bm25 | 0.382 | 0.555 | 0.655 | 0.736 | 0.496 | 0 | 0 |
| vector | 0.527 | 0.645 | 0.718 | 0.809 | 0.612 | 8 | 10 |
| hybrid | 0.455 | 0.627 | 0.727 | 0.809 | 0.561 | 8 | 10 |
| hybrid+rerank | 0.664 | 0.845 | 0.882 | 0.891 | 0.755 | 3830 | 7750 |

### Recall@5 by type

| type | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| conflict | 4 | 0.25 | 0.50 | 0.50 | 0.50 |
| cross_lingual | 27 | 0.30 | 0.48 | 0.37 | 0.70 |
| date | 11 | 0.91 | 0.91 | 0.91 | 1.00 |
| fact | 13 | 0.92 | 0.77 | 0.92 | 1.00 |
| list | 3 | 1.00 | 1.00 | 1.00 | 1.00 |
| number | 40 | 0.78 | 0.78 | 0.85 | 0.95 |
| stale | 1 | 0.00 | 1.00 | 0.00 | 1.00 |
| yes_no | 11 | 0.64 | 0.82 | 0.82 | 0.91 |

### Recall@5 by country

| country | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| canada | 23 | 0.52 | 0.70 | 0.70 | 0.87 |
| erasmus | 13 | 0.69 | 0.85 | 0.69 | 1.00 |
| france | 42 | 0.62 | 0.69 | 0.69 | 0.88 |
| germany | 32 | 0.78 | 0.72 | 0.81 | 0.84 |

### Recall@5 by lang

| lang | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| en | 58 | 0.66 | 0.72 | 0.72 | 0.88 |
| fr | 52 | 0.65 | 0.71 | 0.73 | 0.88 |

### Recall@5 by difficulty

| difficulty | n | bm25 | vector | hybrid | hybrid+rerank |
|---|---|---|---|---|---|
| easy | 40 | 0.72 | 0.85 | 0.80 | 0.95 |
| hard | 19 | 0.47 | 0.63 | 0.68 | 0.84 |
| medium | 51 | 0.67 | 0.65 | 0.69 | 0.84 |

Quotes not inside any single chunk (0): none

Misses of the best setup (hybrid+rerank, top 10, 12): q002, q012, q015, q027, q044, q047, q049, q050, q055, q081, q083, q087
