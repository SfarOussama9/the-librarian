"""Deploy the Librarian on Modal (free Starter plan: $30 of compute per month).

    .venv/Scripts/modal deploy deploy/modal_app.py

Modal runs the same FastAPI app as `uvicorn app.server:app`, in a container with
4 vCPU and 2 GB of memory that scales to zero when idle (the first visit after a
few idle minutes takes ~20 s while the models load).

- Only OPENAI_API_KEY is sent from the local .env, as an encrypted Modal secret.
- The embedding model and reranker are downloaded into the image at build time.
- The anonymous question/feedback logs live on a persistent Modal Volume
  ("librarian-logs"); read them with:
      .venv/Scripts/modal volume get librarian-logs / logs-from-modal
- max_containers=1 keeps the per-visitor rate limit (held in memory) consistent.
"""

import os
from pathlib import Path

import modal
from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parent.parent
REMOTE = "/root/project"

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install_from_requirements(str(ROOT / "requirements-app.txt"))
    .env({"FASTEMBED_CACHE_PATH": "/models", "PYTHONUNBUFFERED": "1",
          # Match ONNX Runtime's threads to the container's CPUs (see librarian/embed.py).
          "ONNX_THREADS": "4", "OMP_NUM_THREADS": "4"})
    .add_local_dir(ROOT / "librarian", f"{REMOTE}/librarian", copy=True, ignore=["**/__pycache__"])
    .add_local_dir(ROOT / "index", f"{REMOTE}/index", copy=True)
    .run_commands(f"cd {REMOTE} && python -c \"from librarian.embed import model; model(); "
                  f"from librarian.rerank import model as r; r()\"")
    # The web app is added last, so editing the page doesn't rebuild the model layer.
    .add_local_dir(ROOT / "app", f"{REMOTE}/app", ignore=["**/__pycache__"])
)

openai_key = os.getenv("OPENAI_API_KEY") or dotenv_values(ROOT / ".env").get("OPENAI_API_KEY")
logs = modal.Volume.from_name("librarian-logs", create_if_missing=True)

app = modal.App("librarian")


@app.function(image=image, cpu=4, memory=4096, timeout=900)
def bench(threads: int = 4, reranker: str = ""):
    """Time each search step in the real container:
    .venv/Scripts/modal run deploy/modal_app.py::run_bench --threads 4"""
    import sys
    import time

    os.environ["ONNX_THREADS"] = str(threads)
    if reranker:
        os.environ["LIBRARIAN_RERANKER"] = reranker
    os.chdir(REMOTE)
    sys.path.insert(0, REMOTE)
    from librarian.retrieve import Retriever, searchable_text
    from librarian.rerank import rerank

    r = Retriever()
    q = "How many hours per week can I work off campus in Canada?"
    r.search(q, k=1)                                   # load the embedding model
    t = time.perf_counter(); hits = r.search(q, k=20); hybrid = time.perf_counter() - t
    texts = [searchable_text(h.chunk) for h in hits]
    rerank(q, texts[:2])                               # load the reranker
    t = time.perf_counter(); rerank(q, texts); rr = time.perf_counter() - t
    flags = open("/proc/cpuinfo").read()
    cpu = next((l.split(":", 1)[1].strip() for l in flags.splitlines() if l.startswith("model name")), "?")
    return {"threads": threads, "reranker": reranker or "default", "hybrid_s": round(hybrid, 2),
            "rerank_20_s": round(rr, 2), "cpu": cpu,
            "vnni": "avx512_vnni" in flags or "avx_vnni" in flags}


@app.local_entrypoint()
def run_bench(threads: int = 4, reranker: str = ""):
    print(bench.remote(threads, reranker))


@app.function(
    image=image,
    secrets=[modal.Secret.from_dict({"OPENAI_API_KEY": openai_key or ""})],
    volumes={f"{REMOTE}/logs": logs},
    cpu=4,
    memory=2048,
    scaledown_window=300,
    max_containers=1,
    timeout=120,
)
@modal.concurrent(max_inputs=8)
@modal.asgi_app()
def web():
    import sys

    os.chdir(REMOTE)
    sys.path.insert(0, REMOTE)
    import app.server as server

    # Volume writes are only persisted on commit; commit after every log record.
    server.storage.after_write = logs.commit
    return server.app
