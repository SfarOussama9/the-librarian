# Design

## Corpus

281 official documents (266 HTML pages, 15 PDFs, ~251,000 words) for Tunisian students going to
France, Germany, Canada or an Erasmus+ programme. 11 publishers: Campus France Tunisie, Campus
France, France-Visas, DAAD (including its 88-programme scholarship database), DAAD Tunisie, the
German embassy in Tunis, the Federal Foreign Office, IRCC, EduCanada, the European Commission and
the Erasmus+ office in Tunisia. French and English.

- `corpus/sources.toml` lists every document. `scripts/fetch_corpus.py` downloads them and records
  URL, date, method and SHA-256 in `corpus/manifest.jsonl`.
- Several sites block automated requests from Tunisian networks. Documents were fetched directly
  (136), through Jina Reader (127), saved manually in a browser (16, `corpus/manual_download.md`) or
  from the Wayback Machine (2). The method is recorded per document.
- `scripts/extract_text.py` keeps only each site's main-content container (one CSS selector per
  publisher) and converts it to Markdown, so headings, lists and tables survive. PDFs are read page by
  page with PyMuPDF, with running headers removed.
- Publication dates are extracted from PDF metadata, page footers and URLs (80 of 281 documents).
  The answer step uses them to prefer the newest source.

## Chunking

Documents are split into units (heading, paragraph, list, table) and packed in order into chunks of
~150 words with 25 words of overlap (`scripts/chunk.py`).

- A heading is never left at the end of a chunk, and a chunk is not closed below a third of the
  target size, so a question stays with its answer.
- Long lists are split between items and tables between rows; each table piece repeats its header row.
- Every chunk carries its title, heading path, URL, publisher, country, topic, language, date and PDF
  page. Exact duplicates are dropped. Result: 2,200 chunks, median 134 words.

**Size was tested, not assumed.** 150, 250 and 400 words were compared at an equal context budget
(same number of words sent to the model), on the dev split:

| Chunk size | Recall, 500-word budget | Recall, 1,000-word budget |
|---|---|---|
| **150** | **0.886** | **0.924** |
| 250 | 0.873 | 0.899 |
| 400 | 0.823 | 0.886 |

(hybrid + reranker; `eval/compare_chunking.py`, `eval/results/chunking-dev.md`)

## Index

- **Keyword:** BM25 (`bm25s`) with a French/English tokenizer that folds accents and drops stopwords
  (`librarian/text.py`).
- **Vectors:** `intfloat/multilingual-e5-small` (384 dimensions, ONNX through `fastembed`), stored as
  a NumPy matrix (`index/vectors.npy`, 3.4 MB) and searched exactly with one matrix product.
- **Why a flat file and not a vector database:** 2,200 vectors search exactly in under 10 ms. A
  database would add a server and a dependency with no speed or recall benefit at this size. Above
  ~1M chunks we would switch to an approximate index (FAISS/pgvector).
- **Why local models:** no per-search cost, multilingual, and no PyTorch install (ONNX on CPU).

## Retrieval

1. BM25 and vector search each rank the top 50 chunks, optionally filtered by metadata (country,
   topic, language).
2. **Reciprocal Rank Fusion** (k = 60) merges the two rankings; no score normalisation or weights.
3. **Cross-encoder reranker** (`BAAI/bge-reranker-v2-m3`, int8) rescores the top 20.
4. The top 4 chunks (~500 words) go to the model.

The reranker depth (20) was tested: a depth of 10 halves rerank time but loses 7.6 points of recall@3
(dev).

## Generation

`librarian/generate.py`, model `gpt-5.4-nano` (high reasoning effort).

- **Fixed instructions:** answer only from the numbered sources, cite `[S#]` after every factual
  sentence, answer in the question's language, and say "I don't know" when the sources do not answer.
- **Conflicts:** sources about different situations (e.g. language course vs. degree) are not
  conflicts. For the same value in the same situation, the newest dated source wins and the older
  figure is mentioned. Dated sources are shown newest first.
- **Structured output** (JSON schema): `answer`, `answerable`, `sources_used`. "I don't know" is
  therefore a boolean that can be scored, and citations map to chunk IDs, URLs and PDF pages.
- One retry if the answer contains a word in another script (a known small-model glitch).

## Service

FastAPI (`app/server.py`) with a static front end (`app/static/`), deployed on Modal (4 vCPU,
scales to zero). Answers stream progress (searching, writing) over server-sent events. Repeated
questions are served from an in-memory cache. Visitors are rate-limited (20/hour, 500/day). Logs
are anonymous: question, answer, rating, with no IP address or account.

## Known failure cases

| Case | Example | Effect |
|---|---|---|
| Cross-lingual retrieval | French question, answer only on an English IRCC page | Most wrong "I don't know" answers (6.4% of answerable questions) come from the gold chunk not being retrieved |
| Outdated documents still online | 2020 embassy PDF: €10,332 blocked account vs €11,904 today | The newest-source rule handles it when both are retrieved; nano still picks the old figure on q043 |
| Undated sources | 201 of 281 documents have no date | The newest-source rule can't rank them |
| Table-heavy PDFs | Campus France calendar | Dates can be read from the wrong column; deadlines get confused (q013) |
| Screenshot PDFs, Arabic PDF | Some Campus France slides | Little or no extractable text |
| Pointer-only catalogues | Erasmus Mundus catalogue lists ~218 programme names | Programme details live on university sites not in the corpus, so the answer is "I don't know" |
| Multi-part or vague questions | "I want to study in France, guide me" | No question rewriting: retrieval takes the question as is |
| Metadata filters unused online | `country=` filter exists | The web app searches all countries, so a German question can retrieve a French page |
| Latency on shared CPUs | Reranker on Modal | 12–22 s per answer online vs ~4 s on a laptop |
