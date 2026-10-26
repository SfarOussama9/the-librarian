"""Anonymous log of questions, answers and ratings, for the report's user feedback.

Records go to logs/*.jsonl. Nothing identifies a visitor: no IP address, no
account, no cookie, only the question text a person chose to type.
"""

import json
import threading
import time
from pathlib import Path

LOGS = Path(__file__).resolve().parent.parent / "logs"


class Storage:
    def __init__(self, folder=LOGS):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.lock = threading.Lock()
        self.after_write = None  # e.g. a Modal Volume's commit, so each record is saved at once

    def _write(self, name, record):
        record = {"time": time.strftime("%Y-%m-%dT%H:%M:%S"), **record}
        line = json.dumps(record, ensure_ascii=False) + "\n"
        with self.lock:
            with open(self.folder / name, "a", encoding="utf-8") as f:
                f.write(line)
            if self.after_write:
                try:
                    self.after_write()
                except Exception:  # noqa: BLE001  saving later is better than failing the request
                    pass

    def log_answer(self, answer_id, ui_lang, result):
        self._write("answers.jsonl", {
            "answer_id": answer_id, "ui_lang": ui_lang, "question": result.question,
            "answer": result.answer, "answerable": result.answerable,
            "citations": [c["chunk_id"] for c in result.citations], "sources": result.sources,
            "cost_usd": result.cost_usd, "latency_s": result.latency_s, "usage": result.usage,
        })

    def log_feedback(self, answer_id, rating, comment):
        self._write("feedback.jsonl", {"answer_id": answer_id, "rating": rating, "comment": comment})

    def log_error(self, answer_id, question, error):
        self._write("errors.jsonl", {"answer_id": answer_id, "question": question, "error": error})
