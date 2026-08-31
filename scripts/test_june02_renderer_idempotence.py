#!/usr/bin/env python3
"""Regression check: a closed 2026-06-02 Daily must stay closed when rebuilt."""

from __future__ import annotations

import hashlib
import tempfile
from pathlib import Path

import rebuild_june02_daily_v2_strict as renderer
import audit_june02_evidence_v3_fresh as evidence_audit


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    normalized = renderer.normalize_benchmark_row([
        "SF-TEST", "workload", "evaluated models in §5", "topology in §5",
        "datatype in §5", "task-dependent", "Not Applicable — collective",
        "settings in Appendix A", "workload-specific in §5", "Not Disclosed", "exact evaluator",
    ])
    assert normalized == [
        "SF-TEST", "workload", "Not Disclosed", "Not Disclosed", "Not Disclosed",
        "Not Disclosed", "Not Required — collective", "Not Disclosed", "Not Disclosed",
        "Not Disclosed", "exact evaluator",
    ]
    normalized_semantics = renderer.normalize_benchmark_row([
        "SF-TEST-2", "workload", "three agent families in §4",
        "Docker sandbox; Not Disclosed", "model/runtime-specific in §8.1",
        "task dependent", "generated result", "1,000 benchmark instances",
        "task arrival-rate sweep", "latency and accuracy", "authors",
    ])
    assert normalized_semantics == [
        "SF-TEST-2", "workload", "Not Disclosed", "Not Disclosed",
        "Not Disclosed", "Not Disclosed", "generated result", "Not Disclosed",
        "Not Disclosed", "latency and accuracy", "Not Disclosed",
    ]
    benchmark = evidence_audit.benchmark_contract_from_row([
        "SF-TEST", "workload", "model", "hardware", "precision",
        "input-length", "output-length", "batch", "concurrency", "slo", "evaluator",
    ])
    assert benchmark == {
        "workload": "workload", "model": "model", "hardware": "hardware", "precision": "precision",
        "input_length": "input-length", "output_length": "output-length", "batch": "batch",
        "concurrency": "concurrency", "slo": "slo", "evaluator": "evaluator",
    }
    with tempfile.TemporaryDirectory(prefix="june02-renderer-") as tmp:
        target = Path(tmp) / "README.md"
        ledger = Path(tmp) / "evidence-books-comparison-v3-fresh.json"
        original_daily, original_ledger = renderer.DAILY, renderer.OUT_JSON
        target.write_text(original_daily.read_text(encoding="utf-8"), encoding="utf-8")
        try:
            renderer.DAILY, renderer.OUT_JSON = target, ledger
            renderer.main()
            first = digest(target)
            text = target.read_text(encoding="utf-8")
            assert "| Completion Status | Complete |" in text
            assert "| Coverage Gate | Closed |" in text
            assert "| Evidence Gate | Passed |" in text
            assert "| Books Gate | Passed |" in text
            assert "POST_WRITE_FRESH_AUDIT_V4.md" in text
            assert "fresh-context:pending-jun02-postwrite" not in text
            assert "本项只形成串行 Books proposal，不代表已写回" not in text
            assert text.startswith("# Daily Research — 2026-06-02\n\n**Research Date:** 2026-06-02")
            expected_sections = [
                "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
                "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
                "## 5. Deep Analysis Selection", "## 6. Books Comparison",
                "## 7. Semantic Audit", "## 8. Ignored Noise",
                "## 9. Recommended Action", "## 10. Repository Changes",
                "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
            ]
            assert [line for line in text.splitlines() if line.startswith("## ")] == expected_sections
            assert "analysis:DA-20260602-RUNTIME-EVIDENCE" not in text
            candidate = evidence_audit.table_map(text, "## 2. Candidate Ledger")
            receipts = evidence_audit.table_map(text, "## 3. Review Completion Receipt")
            benchmark = evidence_audit.table_map(text, "## 4. Benchmark Contracts")
            selection = evidence_audit.table_map(text, "## 5. Deep Analysis Selection")
            books = evidence_audit.table_map(text, "## 6. Books Comparison")
            assert set(candidate) == set(receipts) == set(benchmark) == set(books)
            eligible = {
                family for family, row in candidate.items()
                if int(row[9]) >= 7 or row[13] not in {"", "none", "—"} or row[19] == "Integrate"
            }
            assert len(candidate) == 28
            assert len(eligible) == len(selection) == 27
            assert set(selection) == eligible
            assert "SF-SECLAW-SPEC-DRIVEN-SECURITY" not in selection
            selected = [row for row in selection.values() if row[2] == "selected"]
            assert len(selected) == 3
            assert len({row[3] for row in selected}) == 2
            assert sum(row[2] == "not_selected" for row in selection.values()) == 24
            assert "<!-- analysis-noneligible:SF-SECLAW-SPEC-DRIVEN-SECURITY:start -->" in text
            assert "Score V2=6/9、Review Override=`none`" in text
            assert "不满足 `score_7_9`、`forced_review`、`potential_books_delta`" in text
            assert "主 Selection eligible pool 之外" in text
            renderer.main()
            assert digest(target) == first
        finally:
            renderer.DAILY, renderer.OUT_JSON = original_daily, original_ledger


if __name__ == "__main__":
    main()
