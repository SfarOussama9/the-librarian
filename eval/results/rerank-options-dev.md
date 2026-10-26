# Reranker options: dev

79 answerable questions · 20 hybrid candidates · top 4 kept · threads default · 20261025-200245

| option | recall@4 | search p50 | search p95 |
|---|---|---|---|
| none | 0.709 | 0.01 s | 0.01 s |
| rerank:BAAI/bge-reranker-v2-m3-int8 | 0.886 | 2.32 s | 4.84 s |
| rerank:jinaai/jina-reranker-v2-base-multilingual | 0.873 | 2.12 s | 3.79 s |
| rerank:Xenova/ms-marco-MiniLM-L-12-v2 | 0.722 | 0.83 s | 1.13 s |
| skip-if-agree | 0.873 | 2.17 s | 4.71 s |

skip-if-agree skips the reranker on 30% of questions.
