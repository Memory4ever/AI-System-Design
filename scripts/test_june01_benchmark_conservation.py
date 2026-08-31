#!/usr/bin/env python3
"""Regression for 2026-06-01 claim-scoped benchmark conservation."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
NON_BENCHMARK = {
    "SF-AGENT-OPERATING-SYSTEM",
    "SF-AIREP",
    "SF-FED-PERSONALIZATION-SILENT-FAILURES",
    "SF-LONG-RUN-AGENT-EPISTEMIC-INTEGRITY",
}
def load_repair():
    path = ROOT / "scripts/repair_june01_semantic_audit.py"
    spec = importlib.util.spec_from_file_location("repair_june01", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    repair = load_repair()
    text = REPORT.read_text(encoding="utf-8")
    tables = []
    for marker in (
        repair.VALIDATOR.CANDIDATE_LEDGER_MARKER,
        repair.VALIDATOR.REVIEW_COMPLETION_MARKER,
        repair.VALIDATOR.BENCHMARK_MARKER,
        repair.VALIDATOR.DEEP_ANALYSIS_SELECTION_MARKER,
        repair.VALIDATOR.BOOKS_COMPARISON_MARKER,
    ):
        _, rows = repair.parse_table(text, marker)
        tables.append(rows)
    candidates, reviews, benchmarks, selections, books = tables
    candidate_ids = {row["Source Family ID"] for row in candidates}
    assert len(candidates) == len(reviews) == len(selections) == len(books) == 40
    assert len(benchmarks) == 36
    for rows in (reviews, selections, books):
        assert {row["Source Family ID"] for row in rows} == candidate_ids

    yes_ids = {
        row["Source Family ID"] for row in candidates if row["Benchmark Claim"] == "yes"
    }
    no_ids = {
        row["Source Family ID"] for row in candidates if row["Benchmark Claim"] == "no"
    }
    benchmark_ids = {row["Source Family ID"] for row in benchmarks}
    assert len(yes_ids) == 36
    assert no_ids == NON_BENCHMARK
    assert benchmark_ids == yes_ids
    assert not (NON_BENCHMARK & benchmark_ids)
    assert sum(row["Decision"] == "selected" for row in selections) <= 3
    print({
        "candidate": 40,
        "review": 40,
        "benchmark_yes": 36,
        "benchmark_no": 4,
        "benchmark_rows": 36,
        "selection": 40,
        "books": 40,
    })


if __name__ == "__main__":
    main()
