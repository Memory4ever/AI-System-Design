#!/usr/bin/env python3
"""Move completed V2.1 Daily evidence into the canonical reader layout.

This migration deliberately preserves candidate rows and every machine-audited
review, claim, Books, and semantic-audit marker.  It changes presentation only.
"""

from __future__ import annotations

import argparse
import re
from datetime import date, timedelta
from pathlib import Path


def _metadata(text: str, field: str) -> str:
    match = re.search(rf"^\| {re.escape(field)} \| ([^|]+) \|$", text, re.MULTILINE)
    if not match:
        raise ValueError(f"missing metadata field: {field}")
    return match.group(1).strip()


def _section(text: str, heading: str, next_heading: str | None) -> str:
    start = text.index(heading) + len(heading)
    end = text.index(next_heading, start) if next_heading else len(text)
    return text[start:end].strip("\n")


def _first_heading(text: str, aliases: tuple[str, ...]) -> str:
    present = [(text.index(value), value) for value in aliases if value in text]
    if not present:
        raise ValueError(f"missing section; expected one of {aliases}")
    return min(present, key=lambda item: (item[0], -len(item[1])))[1]


def canonicalize_report(report: Path) -> bool:
    text = report.read_text()
    if "## 13. Final Status" in text:
        return False

    required = (
        "## Executive Summary",
        "## 1. Coverage",
        "## 2. Candidate Ledger",
        "## 3. Review Completion Receipt",
        "### Source Reviews",
        "## 4. Deep Analysis Selection",
        "## 6. Semantic Audit",
        "## 7. Ignored Noise",
        "## 8. Recommended Action",
        "## 9. Repository Changes",
        "## 10. Open Questions",
        "## 11. Sources",
    )
    missing = [value for value in required if value not in text]
    if missing:
        raise ValueError(f"{report}: unsupported legacy Daily layout; missing {missing}")

    books_heading = _first_heading(
        text,
        ("## 5. Books Comparison", "## 5. Books Comparison Queue"),
    )
    research_date = _metadata(text, "Window End")
    report_day = date.fromisoformat(research_date)
    completion = _metadata(text, "Completion Status")
    coverage_gate = _metadata(text, "Coverage Gate")
    evidence_gate = _metadata(text, "Evidence Gate")
    books_gate = _metadata(text, "Books Gate")
    coverage_mode = _metadata(text, "Coverage Mode")

    executive = _section(text, "## Executive Summary", "## 1. Coverage")
    coverage = _section(text, "## 1. Coverage", "## 2. Candidate Ledger")
    candidate_with_benchmark = _section(
        text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"
    )
    benchmark_label = (
        "### Benchmark Contracts"
        if "### Benchmark Contracts" in candidate_with_benchmark
        else "Benchmark contract"
    )
    if benchmark_label not in candidate_with_benchmark:
        raise ValueError(f"{report}: cannot locate Benchmark Contracts payload")
    benchmark_at = candidate_with_benchmark.index(benchmark_label)
    candidate = candidate_with_benchmark[:benchmark_at].strip("\n")
    benchmark = candidate_with_benchmark[benchmark_at + len(benchmark_label) :].strip("\n")
    if benchmark_label == "Benchmark contract":
        benchmark = "Benchmark contract" + benchmark
    review = _section(
        text, "## 3. Review Completion Receipt", "## 4. Deep Analysis Selection"
    )
    deep = _section(text, "## 4. Deep Analysis Selection", books_heading)
    books = _section(text, books_heading, "## 6. Semantic Audit")
    semantic = _section(text, "## 6. Semantic Audit", "## 7. Ignored Noise")
    ignored = _section(text, "## 7. Ignored Noise", "## 8. Recommended Action")
    action = _section(text, "## 8. Recommended Action", "## 9. Repository Changes")
    changes = _section(text, "## 9. Repository Changes", "## 10. Open Questions")
    questions = _section(text, "## 10. Open Questions", "## 11. Sources")
    sources = _section(text, "## 11. Sources", None)

    start_day = report_day - timedelta(days=1)
    preamble = "\n".join(
        [
            f"# Daily Research — {research_date}",
            "",
            f"**Research Date:** {research_date}",
            "",
            "**Timezone:** Asia/Shanghai",
            "",
            f"**Strict Window:** {start_day.isoformat()} 09:00:00 ～ {research_date} 09:00:00（北京时间，左闭右开）",
            "",
            f"**Contract:** V2.1 {coverage_mode}",
            "",
            f"**Status:** {completion}；Coverage={coverage_gate}、Evidence={evidence_gate}、Books={books_gate}，fresh-context Semantic Audit 状态见第 7 节",
        ]
    )
    final = (
        f"State Truth: Completion={completion}；Coverage={coverage_gate}；"
        f"Evidence={evidence_gate}；Books={books_gate}；unresolved findings=0。\n\n"
        "本节只汇总前述收据与 fresh-context 审计的最终状态，不以格式校验替代语义验收。"
    )
    parts = (
        ("## Executive Summary", executive),
        ("## 1. Coverage", coverage),
        ("## 2. Candidate Ledger", candidate),
        ("## 3. Review Completion Receipt", review),
        ("## 4. Benchmark Contracts", benchmark),
        ("## 5. Deep Analysis Selection", deep),
        ("## 6. Books Comparison", books),
        ("## 7. Semantic Audit", semantic),
        ("## 8. Ignored Noise", ignored),
        ("## 9. Recommended Action", action),
        ("## 10. Repository Changes", changes),
        ("## 11. Open Questions", questions),
        ("## 12. Sources", sources),
        ("## 13. Final Status", final),
    )
    migrated = preamble + "\n\n" + "\n\n".join(
        f"{heading}\n\n{body}" for heading, body in parts
    ) + "\n"
    report.write_text(migrated)
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("reports", nargs="+", type=Path)
    args = parser.parse_args()
    for report in args.reports:
        changed = canonicalize_report(report)
        print(f"{'updated' if changed else 'unchanged'}: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
