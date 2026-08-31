#!/usr/bin/env python3
"""Regression guard for 2026-06-03 Selection eligibility conservation."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/03/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
SELECTION_PACKET = PACKET / "deep-analysis-selection-v9-strict.json"

EXPECTED_NON_ELIGIBLE = {
    "SF-AI-AGENTS-ENABLE-ADAPTIVE-COMPUTER-WORMS",
    "SF-COEVAL-RANKING-LANGUAGE-MODELS-CUSTOM-TASKS-WITHOUT",
    "SF-E2LLM-EDGE-SERVING",
    "SF-IMPLEMENT-KUBERNETES-POD-LEVEL-REMOTE-ATTESTATION-CONFIDENTIAL",
    "SF-SAE-QUANT-FIDELITY",
}


def table_rows(text: str, marker: str) -> list[list[str]]:
    """Return parsed data rows from the Markdown table immediately after marker."""
    tail = text.split(marker, 1)[1].lstrip("\n")
    lines = tail.splitlines()
    assert len(lines) >= 3 and lines[0].startswith("| "), marker
    rows: list[list[str]] = []
    for line in lines[2:]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def ids(rows: list[list[str]]) -> set[str]:
    return {row[0] for row in rows}


def table_records(text: str, marker: str) -> dict[str, dict[str, str]]:
    tail = text.split(marker, 1)[1].lstrip("\n")
    lines = tail.splitlines()
    header = [cell.strip() for cell in lines[0].strip().strip("|").split("|")]
    records: dict[str, dict[str, str]] = {}
    for line in lines[2:]:
        if not line.startswith("|"):
            break
        values = [cell.strip() for cell in line.strip().strip("|").split("|")]
        row = dict(zip(header, values))
        records[row["Source Family ID"]] = row
    return records


def main() -> None:
    report = REPORT.read_text(encoding="utf-8")
    packet = json.loads(SELECTION_PACKET.read_text(encoding="utf-8"))

    candidate = table_rows(report, "<!-- validator:candidate-ledger-v2.1 -->")
    review = table_rows(report, "<!-- validator:review-completion-v1 -->")
    benchmark = table_rows(report, "<!-- validator:benchmark-contract-v1 -->")
    selection = table_rows(report, "<!-- validator:deep-analysis-selection-v1 -->")
    non_eligible = table_rows(report, "<!-- audit:deep-analysis-non-eligible-v1 -->")
    books = table_rows(report, "<!-- validator:books-comparison-v1 -->")

    sets = {
        "Candidate": ids(candidate),
        "Review": ids(review),
        "Benchmark": ids(benchmark),
        "Books": ids(books),
    }
    expected = sets["Candidate"]
    assert len(expected) == 55, f"Candidate count={len(expected)}"
    for name, actual in sets.items():
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        assert actual == expected, f"{name}: count={len(actual)} missing={missing} extra={extra}"

    selection_ids = ids(selection)
    non_eligible_ids = ids(non_eligible)
    assert selection_ids.isdisjoint(non_eligible_ids)
    assert selection_ids | non_eligible_ids == expected
    assert len(selection_ids) == 50
    assert non_eligible_ids == EXPECTED_NON_ELIGIBLE

    candidate_records = table_records(report, "<!-- validator:candidate-ledger-v2.1 -->")
    recomputed_eligible = {
        family_id
        for family_id, row in candidate_records.items()
        if int(row["Total"]) >= 7 or row["Review Override"] != "none"
    }
    assert selection_ids == recomputed_eligible

    packet_rows = {row["source_family_id"]: row for row in packet["rows"]}
    assert set(packet_rows) == expected
    selection_rows = {row[0]: row for row in selection}
    closure_rows = {row[0]: row for row in non_eligible}

    selected = 0
    for family_id, row in selection_rows.items():
        packet_row = packet_rows[family_id]
        assert len(row) == 7, f"{family_id}: malformed Selection row"
        eligibility, decision, unit, _, rationale, narrative_ref = row[1:]
        assert eligibility and eligibility != "—", f"{family_id}: empty eligibility"
        expected_decision = "selected" if packet_row["selection"] == "selected" else "not_selected"
        assert decision == expected_decision, f"{family_id}: {decision=} {expected_decision=}"
        assert rationale == packet_row["selection_basis"], f"{family_id}: rationale drift"
        assert narrative_ref and narrative_ref != "—", f"{family_id}: empty narrative ref"
        if decision == "selected":
            selected += 1
            assert unit != "—" and narrative_ref == f"analysis:{unit}"
            assert report.count(f"<!-- analysis:{unit}:start -->") == 1
            assert report.count(f"<!-- analysis:{unit}:end -->") == 1
        else:
            assert unit == "—"
            assert narrative_ref == f"analysis-decision:{family_id}"
            assert report.count(f"<!-- {narrative_ref}:start -->") == 1
            assert report.count(f"<!-- {narrative_ref}:end -->") == 1

    for family_id, row in closure_rows.items():
        packet_row = packet_rows[family_id]
        assert len(row) == 6, f"{family_id}: malformed non-eligible closure row"
        score, override, closure, rationale, narrative_ref = row[1:]
        assert score == str(candidate_records[family_id]["Total"])
        assert override == candidate_records[family_id]["Review Override"] == "none"
        assert closure == "not_eligible_for_deep_analysis"
        assert packet_row["eligible"] is False
        assert packet_row["selection"] == "not_eligible"
        assert rationale == packet_row["selection_basis"]
        assert narrative_ref == f"analysis-ineligible:{family_id}"
        assert report.count(f"<!-- {narrative_ref}:start -->") == 1
        assert report.count(f"<!-- {narrative_ref}:end -->") == 1

    assert selected <= 3, f"selected={selected}"
    assert selected == 3, f"selected={selected}"
    assert not re.search(r"(?m)[ \t]+$", report), "README has trailing whitespace"

    print(
        "PASS 2026-06-03 Selection conservation: "
        "Candidate/Review/Benchmark/Books=55; "
        f"eligible_selection={len(selection_ids)}; non_eligible_closure={len(non_eligible_ids)}; "
        f"selected={selected}"
    )


if __name__ == "__main__":
    main()
