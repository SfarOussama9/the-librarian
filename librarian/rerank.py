"""Cross-encoder reranking: reads the question and each candidate chunk together.

Slower than first-stage search (one model pass per candidate), so it only
reorders the top few candidates from BM25/vector/hybrid search.
"""

from fastembed.rerank.cross_encoder import TextCrossEncoder

from librarian.embed import THREADS

import os

# Multilingual. The int8 version (~0.6 GB) is fast on CPUs with VNNI instructions
# (most recent laptops) but slow on many cloud CPUs, where the full-precision
# "BAAI/bge-reranker-v2-m3" (~2.3 GB) can be faster. LIBRARIAN_RERANKER overrides it.
MODEL = os.getenv("LIBRARIAN_RERANKER", "BAAI/bge-reranker-v2-m3-int8")

_model = None


def model():
    global _model
    if _model is None:
        _model = TextCrossEncoder(MODEL, threads=THREADS)
    return _model


def rerank(query, texts):
    """Return one relevance score per text (higher is more relevant)."""
    return list(model().rerank(query, texts))
