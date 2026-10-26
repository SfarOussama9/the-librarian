"""Ask the Librarian a question from the terminal.

Usage: python scripts/ask.py "Combien faut-il sur le compte bloqué pour l'Allemagne ?"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from librarian.generate import Librarian  # noqa: E402


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    result = Librarian().ask(" ".join(sys.argv[1:]))
    print(result.answer)
    print()
    for c in result.citations:
        print(f"[{c['label']}] {c['title']} ({c['published'] or 'date unknown'})\n     {c['url']}")
    t = result.latency_s
    print(f"\n{result.usage['input_tokens']} tokens in, {result.usage['output_tokens']} out · "
          f"${result.cost_usd:.4f} · search {t['retrieval']:.1f}s + answer {t['generation']:.1f}s")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
