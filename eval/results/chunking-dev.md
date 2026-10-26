# Chunk size at equal word budget (dev)

k = budget / mean chunk length; ranks only go to 10, so a k above 10 is capped by the data.

| chunk size | chunks | mean words | setup | recall @ 500 words | recall @ 1000 words | recall @ 1500 words |
|---|---|---|---|---|---|---|
| 150 | 2200 | 129 | bm25 | 0.633 (k=4) | 0.722 (k=8) | 0.772 (k=12) |
| 150 | 2200 | 129 | vector | 0.709 (k=4) | 0.797 (k=8) | 0.823 (k=12) |
| 150 | 2200 | 129 | hybrid | 0.709 (k=4) | 0.772 (k=8) | 0.823 (k=12) |
| 150 | 2200 | 129 | hybrid+rerank | 0.886 (k=4) | 0.924 (k=8) | 0.924 (k=12) |
| 250 | 1387 | 200 | bm25 | 0.658 (k=3) | 0.696 (k=5) | 0.734 (k=8) |
| 250 | 1387 | 200 | vector | 0.671 (k=3) | 0.772 (k=5) | 0.810 (k=8) |
| 250 | 1387 | 200 | hybrid | 0.696 (k=3) | 0.785 (k=5) | 0.861 (k=8) |
| 250 | 1387 | 200 | hybrid+rerank | 0.873 (k=3) | 0.899 (k=5) | 0.911 (k=8) |
| 400 | 949 | 287 | bm25 | 0.620 (k=2) | 0.684 (k=3) | 0.747 (k=5) |
| 400 | 949 | 287 | vector | 0.595 (k=2) | 0.696 (k=3) | 0.785 (k=5) |
| 400 | 949 | 287 | hybrid | 0.671 (k=2) | 0.747 (k=3) | 0.835 (k=5) |
| 400 | 949 | 287 | hybrid+rerank | 0.823 (k=2) | 0.886 (k=3) | 0.924 (k=5) |
