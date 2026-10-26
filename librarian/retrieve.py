"""Search the index: keyword (BM25), vector (e5) or hybrid.

    from librarian.retrieve import Retriever
    r = Retriever()
    hits = r.search("blocked account amount Germany", k=5, mode="hybrid", country="germany")
    for h in hits: print(h.score, h.chunk["chunk_id"])

Hybrid search fuses the BM25 and vector rankings with Reciprocal Rank Fusion
(score = sum of 1 / (RRF_K + rank)), which needs no score normalisation or
weights. Metadata filters (country, topic, lang) are applied before ranking.
"""

import json
import os
from dataclasses import dataclass
from pathlib import Path

import bm25s
import numpy as np

from librarian.embed import embed_query
from librarian.text import tokenize

INDEX = Path(__file__).resolve().parent.parent / "index"
RRF_K = 60        # standard value from the original RRF paper
CANDIDATES = 50   # how deep each ranking goes before fusion
RERANK_DEPTH = int(os.getenv("LIBRARIAN_RERANK_DEPTH", "20"))  # first-stage candidates handed to the reranker


def searchable_text(chunk):
    """What gets indexed and reranked: title and heading give a chunk its context."""
    return "\n".join(x for x in (chunk["title"], chunk["heading"], chunk["text"]) if x)


@dataclass
class Hit:
    chunk: dict
    score: float


class Retriever:
    def __init__(self, index_dir=INDEX):
        index_dir = Path(index_dir)
        self.chunks = [json.loads(line) for line in
                       (index_dir / "chunks.jsonl").read_text(encoding="utf-8").splitlines()]
        self.bm25 = bm25s.BM25.load(str(index_dir / "bm25"))
        self.vectors = np.load(index_dir / "vectors.npy")

    def _mask(self, country=None, topic=None, lang=None):
        keep = np.ones(len(self.chunks), dtype=bool)
        for field, value in (("country", country), ("topic", topic), ("lang", lang)):
            if value:
                values = {value} if isinstance(value, str) else set(value)
                keep &= np.array([c[field] in values for c in self.chunks])
        return keep

    def bm25_scores(self, query):
        tokens = tokenize(query)
        if not tokens:
            return np.zeros(len(self.chunks), dtype=np.float32)
        return self.bm25.get_scores(tokens)

    def vector_scores(self, query):
        return self.vectors @ np.asarray(embed_query(query), dtype=np.float32)

    @staticmethod
    def _rank(scores, keep, depth):
        scores = np.where(keep, scores, -np.inf)
        order = np.argsort(-scores)[:depth]
        return [i for i in order if np.isfinite(scores[i])]

    def search(self, query, k=10, mode="hybrid", country=None, topic=None, lang=None,
               rerank=False, rerank_depth=RERANK_DEPTH):
        """Top-k chunks for a query. With rerank=True, the first stage fetches
        rerank_depth candidates and the cross-encoder picks the final k."""
        if rerank:
            from librarian.rerank import rerank as cross_encode
            candidates = self.search(query, max(k, rerank_depth), mode, country, topic, lang)
            if not candidates:
                return []
            scores = cross_encode(query, [searchable_text(h.chunk) for h in candidates])
            ranked = sorted(zip(scores, candidates), key=lambda x: x[0], reverse=True)[:k]
            return [Hit(h.chunk, float(s)) for s, h in ranked]

        keep = self._mask(country, topic, lang)
        if mode == "bm25":
            scores = self.bm25_scores(query)
            ranked = [i for i in self._rank(scores, keep, k) if scores[i] > 0]
            return [Hit(self.chunks[i], float(scores[i])) for i in ranked]
        if mode == "vector":
            scores = self.vector_scores(query)
            return [Hit(self.chunks[i], float(scores[i])) for i in self._rank(scores, keep, k)]
        if mode != "hybrid":
            raise ValueError(f"unknown mode: {mode}")

        bm25 = self.bm25_scores(query)
        rankings = [
            [i for i in self._rank(bm25, keep, CANDIDATES) if bm25[i] > 0],
            self._rank(self.vector_scores(query), keep, CANDIDATES),
        ]
        fused = {}
        for ranking in rankings:
            for rank, i in enumerate(ranking, 1):
                fused[i] = fused.get(i, 0.0) + 1.0 / (RRF_K + rank)
        best = sorted(fused, key=fused.get, reverse=True)[:k]
        return [Hit(self.chunks[i], fused[i]) for i in best]
