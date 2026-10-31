"""Ask AbroadGuide questions from the terminal.

Usage: python scripts/ask.py

The models load once, then you can ask as many questions as you like.
An empty line, "quit" or Ctrl+C exits.
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from librarian.generate import Librarian  # noqa: E402


def show(result):
    print()
    print(result.answer)
    print()
    for c in result.citations:
        print(f"[{c['label']}] {c['title']} ({c['published'] or 'date unknown'})\n     {c['url']}")
    t = result.latency_s
    print(f"\n{result.usage['input_tokens']} tokens in, {result.usage['output_tokens']} out · "
          f"${result.cost_usd:.4f} · search {t['retrieval']:.1f}s + answer {t['generation']:.1f}s")


def main():
    print("Loading the index and models...")
    start = time.perf_counter()
    lib = Librarian()
    lib.retriever.search("warm-up", k=1, rerank=True)  # loads the embedding model and the reranker
    print(f"Ready in {time.perf_counter() - start:.1f}s. Ask a question in French or English "
          f"(empty line or 'quit' to exit).")

    while True:
        try:
            question = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if question.lower() in ("", "quit", "exit"):
            break
        try:
            show(lib.ask(question))
        except Exception as e:  # noqa: BLE001  a failed question shouldn't end the session
            print(f"Error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
