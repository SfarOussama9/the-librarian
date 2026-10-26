"""Build the search indexes from corpus/chunks.jsonl.

Writes to index/:
  chunks.jsonl   the chunks, in index order (row i of every index = line i here)
  bm25/          BM25 keyword index (bm25s)
  vectors.npy    one normalised e5 embedding per chunk (float32, 384 dims)
  meta.json      what the index was built from

Vectors are kept in a flat NumPy file rather than a vector database: with about
1,400 chunks an exact dot-product search takes milliseconds and needs no server.

Usage: python scripts/build_index.py [--chunks corpus/chunks.jsonl] [--out index]
"""

import argparse
import hashlib
import json
import shutil
import sys
import time
from pathlib import Path

import bm25s
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from librarian.embed import MODEL, embed_passages  # noqa: E402
from librarian.retrieve import searchable_text  # noqa: E402
from librarian.text import tokenize  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--chunks", default=str(ROOT / "corpus" / "chunks.jsonl"))
    parser.add_argument("--out", default=str(ROOT / "index"))
    args = parser.parse_args()

    src, out = Path(args.chunks), Path(args.out)
    chunks = [json.loads(line) for line in src.read_text(encoding="utf-8").splitlines()]
    texts = [searchable_text(c) for c in chunks]
    out.mkdir(parents=True, exist_ok=True)

    t = time.time()
    bm25 = bm25s.BM25()
    bm25.index([tokenize(x) for x in texts], show_progress=False)
    if (out / "bm25").exists():
        shutil.rmtree(out / "bm25")
    bm25.save(str(out / "bm25"))
    print(f"BM25: {len(chunks)} chunks in {time.time() - t:.1f}s")

    t = time.time()
    vectors = np.array(embed_passages(texts), dtype=np.float32)
    np.save(out / "vectors.npy", vectors)
    print(f"vectors: {vectors.shape} in {time.time() - t:.0f}s")

    shutil.copyfile(src, out / "chunks.jsonl")
    (out / "meta.json").write_text(json.dumps({
        "chunks_file": src.name,
        "chunks_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
        "n_chunks": len(chunks),
        "embedding_model": MODEL,
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }, indent=2), encoding="utf-8")
    print(f"index written to {out}")


if __name__ == "__main__":
    main()
