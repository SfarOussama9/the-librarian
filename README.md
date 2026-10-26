# The Librarian

A retrieval-augmented question-answering service for Tunisian students who want to study in France,
Germany, Canada or an Erasmus+ programme. It answers only from 281 official documents (Campus France,
DAAD, IRCC, the European Commission, the German embassy…), cites every claim, and says "I don't know"
when the documents don't answer.

**Live service:** https://sfaroussama9--librarian-web.us-east.modal.run

## Setup

Python 3.11. Create `.env` from `.env.example` with an OpenAI API key, then:

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.server:app --port 8000
```

Open http://localhost:8000. The index is in the repository; the embedding and reranker models
(~0.7 GB) download on the first question. From the command line:
`python scripts/ask.py "Combien faut-il sur le compte bloqué pour l'Allemagne ?"`.

## Results

125 evaluation questions (110 answerable, 15 unanswerable; 58 in French, 67 in English).

**Retrieval** (110 answerable questions, `eval/retrieval_eval.py`):

| Setup | recall@1 | recall@3 | recall@5 | recall@10 | MRR@10 | search p95 |
|---|---|---|---|---|---|---|
| BM25 only | 0.382 | 0.555 | 0.655 | 0.736 | 0.496 | <1 ms |
| Vector only | 0.527 | 0.645 | 0.718 | 0.809 | 0.612 | 10 ms |
| Hybrid (RRF) | 0.455 | 0.627 | 0.727 | 0.809 | 0.561 | 10 ms |
| **Hybrid + reranker** | 0.664 | 0.845 | 0.882 | 0.891 | 0.755 | 7.8 s |

**Generation** (all 125 questions, mean of 3 runs, `eval/generation_eval.py`):

| | Week 7 (gpt-5.4-mini) | Final (gpt-5.4-nano) |
|---|---|---|
| Accuracy | 92.7% | 90.8% |
| Faithfulness | 96.8% | 96.2% |
| Citation accuracy | 95.5% | 94.6% |
| "I don't know" on unanswerable | 100% | 97.8% |
| Cost per question | $0.00155 | **$0.00048 (−69%)** |
| Latency p50 / p95 (laptop) | 4.0 s / 7.0 s | 4.1 s / 7.6 s |

Week 8 details: [`optimisation.md`](optimisation.md).

## Repository

| Path | Contents |
|---|---|
| `corpus/` | `sources.toml` (document list), `manifest.jsonl`, raw downloads, extracted text, chunks |
| `scripts/` | `fetch_corpus.py` → `extract_text.py` → `chunk.py` → `build_index.py`; `ask.py` |
| `index/` | BM25 index, embeddings (`vectors.npy`), chunks |
| `librarian/` | search (`retrieve.py`, `embed.py`, `rerank.py`, `text.py`) and answering (`generate.py`) |
| `app/` | FastAPI server and web front end |
| `data/` | `eval_questions.jsonl`: questions, answers and source quotes |
| `eval/` | retrieval eval and ablation, chunk-size comparison, generation eval, Week 8 scripts, `results/` |
| `deploy/` | Modal deployment |
| `report/` | the report (PDF) |

Rebuild the corpus and index: `python scripts/fetch_corpus.py && python scripts/extract_text.py && python scripts/chunk.py && python scripts/build_index.py`.
Run the evals: `python eval/retrieval_eval.py`, `python eval/generation_eval.py`.

Design and failure cases: [`design.md`](design.md) · Postmortem: [`postmortem.md`](postmortem.md)

## Contributions

Oussama Sfar, Faten Toujani, Ines Turki and Feriel Charrad worked together on every part of the
project: corpus collection and cleaning, chunking and retrieval, the evaluation set and evals,
generation, the web service and deployment, the Week 8 optimisation and the report.
