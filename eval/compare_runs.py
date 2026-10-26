"""Average repeated generation runs per setup, for the Week 8 before/after table.

Runs are grouped by label prefix: opt-mini-r1, opt-mini-r2, ... form "opt-mini".
Each run gives one value per metric; the table shows the mean and the range
(min-max), because one run of the same setup varies by ~3 accuracy points.

Usage:
    python eval/compare_runs.py opt-mini opt-nano opt-nano-medium opt-nano-high
"""

import json
import re
import sys
from pathlib import Path

RESULTS = Path(__file__).resolve().parent / "results"
METRICS = [("accuracy", "Accuracy", 100), ("faithfulness", "Faithfulness", 100),
           ("citation_accuracy", "Citations", 100), ("refused_unanswerable", "IDK on unanswerable", 100),
           ("cost_per_question_usd", "Cost / question ($)", 1), ("latency_total_p95_s", "p95 (s)", 1)]


def runs(prefix):
    """The latest result file of each run labelled <prefix>-r<N>."""
    latest = {}
    for f in sorted(RESULTS.glob(f"generation-{prefix}-r*-2*.json")):
        m = re.fullmatch(rf"generation-{re.escape(prefix)}-(r\d+)-\d{{8}}-\d{{6}}\.json", f.name)
        if m:
            latest[m.group(1)] = f
    return [json.loads(f.read_text(encoding="utf-8"))["summary"] for _, f in sorted(latest.items())]


def cell(values, scale):
    mean = sum(values) / len(values)
    fmt = (lambda v: f"{v * scale:.1f}") if scale == 100 else \
          (lambda v: f"{v:.5f}") if values[0] < 0.01 else (lambda v: f"{v:.1f}")
    return fmt(mean) if len(values) == 1 else f"{fmt(mean)} ({fmt(min(values))}–{fmt(max(values))})"


def main():
    prefixes = sys.argv[1:]
    lines = ["| setup | runs | " + " | ".join(name for _, name, _ in METRICS) + " |",
             "|---|---|" + "---|" * len(METRICS)]
    for p in prefixes:
        summaries = runs(p)
        if not summaries:
            continue
        model = f"{summaries[0]['model']} ({summaries[0].get('effort', 'low')})"
        lines.append(f"| {p} · {model} | {len(summaries)} | " +
                     " | ".join(cell([s[k] for s in summaries], scale) for k, _, scale in METRICS) + " |")
    print("\n".join(lines))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
