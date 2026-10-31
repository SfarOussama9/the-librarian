"""AbroadGuide web service.

    uvicorn app.server:app --port 8000        # then open http://localhost:8000

Endpoints:
  GET  /               the page (app/static/)
  POST /api/ask        {"question": "..."} -> a stream of server-sent events:
                         stage:search, stage:write, then result (or error)
  POST /api/feedback   {"answer_id": "...", "rating": "up"|"down", "comment": "..."}
  GET  /api/health     readiness check

Questions, answers and ratings are logged anonymously (no IP, no account) by
app/storage.py, so real users' feedback can go into the report. A per-visitor
hourly limit and a daily cap protect the API budget.
"""

import json
import os
import threading
import time
import uuid
from collections import OrderedDict, defaultdict, deque
from dataclasses import replace
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.storage import Storage
from librarian.generate import Librarian

STATIC = Path(__file__).resolve().parent / "static"
PER_VISITOR_PER_HOUR = int(os.getenv("PER_VISITOR_PER_HOUR", "20"))
MAX_QUESTIONS_PER_DAY = int(os.getenv("MAX_QUESTIONS_PER_DAY", "500"))
MAX_QUESTION_CHARS = 500

app = FastAPI(title="AbroadGuide")
app.mount("/static", StaticFiles(directory=STATIC), name="static")

librarian = Librarian()
storage = Storage()
search_lock = threading.Lock()  # one search at a time: the models are CPU-bound

# Repeated questions (same words, ignoring case, spacing and end punctuation) get the
# stored answer: no search, no model call, no cost. The corpus doesn't change while
# the app runs, so the only limit is size (oldest answers are dropped first).
CACHE_SIZE = 500
answer_cache = OrderedDict()


def cache_key(question):
    return " ".join(question.lower().split()).rstrip(" ?!.")

# Rate limiting lives in memory only; visitor addresses are never written to disk.
recent = defaultdict(deque)
day = {"date": time.strftime("%Y-%m-%d"), "count": 0}


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=MAX_QUESTION_CHARS)
    lang: str = "fr"


class FeedbackRequest(BaseModel):
    answer_id: str
    rating: str = Field(pattern="^(up|down)$")
    comment: str = Field(default="", max_length=1000)


def visitor(request: Request):
    forwarded = request.headers.get("x-forwarded-for")
    return forwarded.split(",")[0].strip() if forwarded else (request.client.host if request.client else "?")


def over_limit(request):
    """Return an error code if this visitor or today's total is over its limit."""
    today = time.strftime("%Y-%m-%d")
    if day["date"] != today:
        day.update(date=today, count=0)
    if day["count"] >= MAX_QUESTIONS_PER_DAY:
        return "daily_limit"
    q, now = recent[visitor(request)], time.time()
    while q and now - q[0] > 3600:
        q.popleft()
    if len(q) >= PER_VISITOR_PER_HOUR:
        return "visitor_limit"
    q.append(now)
    day["count"] += 1
    return None


def event(kind, data):
    return f"event: {kind}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def search(question):
    with search_lock:
        return librarian.retrieve(question)


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/api/health")
def health():
    return {"ok": True, "model": librarian.model, "chunks": len(librarian.retriever.chunks)}


@app.post("/api/ask")
async def ask(body: AskRequest, request: Request):
    limit = over_limit(request)
    if limit:
        return JSONResponse({"error": limit}, status_code=429)

    async def stream():
        answer_id = uuid.uuid4().hex[:12]
        try:
            key = cache_key(body.question)
            if key in answer_cache:
                answer_cache.move_to_end(key)
                result = replace(answer_cache[key], cost_usd=0.0, usage={"cached_answer": True},
                                 latency_s={"retrieval": 0.0, "generation": 0.0, "total": 0.0})
            else:
                yield event("stage", {"stage": "search"})
                t0 = time.perf_counter()
                chunks = await run_in_threadpool(search, body.question)
                yield event("stage", {"stage": "write"})
                result = await run_in_threadpool(librarian.answer_from, body.question, chunks,
                                                 time.perf_counter() - t0)
                answer_cache[key] = result
                if len(answer_cache) > CACHE_SIZE:
                    answer_cache.popitem(last=False)
        except Exception as e:  # noqa: BLE001  the visitor gets a clear message, the log gets the cause
            storage.log_error(answer_id, body.question, f"{type(e).__name__}: {e}")
            yield event("error", {"error": "failed"})
            return
        storage.log_answer(answer_id, body.lang, result)
        yield event("result", {
            "answer_id": answer_id,
            "answer": result.answer,
            "answerable": result.answerable,
            "citations": result.citations,
            "seconds": round(result.latency_s["total"], 1),
        })

    return StreamingResponse(stream(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


@app.post("/api/feedback")
def feedback(body: FeedbackRequest):
    storage.log_feedback(body.answer_id, body.rating, body.comment.strip())
    return {"ok": True}
