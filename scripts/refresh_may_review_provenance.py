#!/usr/bin/env python3
"""Refresh Review Provenance IDs after bounded May report-body truth edits."""

from __future__ import annotations

from pathlib import Path

import validate_research as validator


ROOT = Path(__file__).resolve().parents[1]
DATES = ("13", "26", "29", "30", "31")


def refresh() -> int:
    changed_rows = 0
    for day in DATES:
        path = ROOT / "papers/2026/05" / day / "README.md"
        text = path.read_text(encoding="utf-8")
        candidates, candidate_errors = validator._expect_columns(
            text, validator.CANDIDATE_LEDGER_MARKER, validator.CANDIDATE_COLUMNS
        )
        receipts, receipt_errors = validator._expect_columns(
            text, validator.REVIEW_COMPLETION_MARKER, validator.REVIEW_COMPLETION_COLUMNS
        )
        if candidate_errors or receipt_errors:
            raise ValueError(f"invalid report tables in {path}: {candidate_errors + receipt_errors}")
        candidate_by_family = {
            row["Source Family ID"].strip("`"): row for row in candidates
        }

        expected_by_family: dict[str, str] = {}
        for receipt in receipts:
            family = receipt["Source Family ID"].strip("`")
            result = receipt["Completion Result"].strip("`")
            if result == "pending":
                continue
            candidate = candidate_by_family[family]
            review_ref = candidate["Review Ref"].strip("`")
            errors: list[str] = []
            segment = validator._bounded_segment(text, review_ref, family, errors)
            if errors or segment is None:
                raise ValueError(f"cannot bind review body for {family}: {errors}")
            expected_by_family[family] = validator._expected_review_provenance(
                family,
                candidate,
                receipt["Review Route"].strip("`"),
                receipt["Primary Evidence Version"].strip("`"),
                receipt["Reviewed Evidence Versions"].strip("`"),
                receipt["Method / Identity Locators"].strip("`"),
                receipt["Evaluation Locators"].strip("`"),
                receipt["Limitations / Counterevidence Locators"].strip("`"),
                receipt["Artifact Locators"].strip("`"),
                receipt["Claim Boundary Ref"].strip("`"),
                review_ref,
                validator._normalized_body_sha256(segment),
            )

        lines = text.splitlines(keepends=True)
        marker_index = next(
            index for index, line in enumerate(lines)
            if validator.REVIEW_COMPLETION_MARKER in line
        )
        table_start = next(
            index for index in range(marker_index + 1, len(lines))
            if lines[index].lstrip().startswith("|")
        )
        for index in range(table_start + 2, len(lines)):
            if not lines[index].lstrip().startswith("|"):
                break
            newline = "\n" if lines[index].endswith("\n") else ""
            cells = validator._cells(lines[index])
            family = cells[0].strip("`")
            expected = expected_by_family.get(family)
            if expected is None or cells[1].strip("`") == expected:
                continue
            cells[1] = expected
            lines[index] = "| " + " | ".join(cells) + " |" + newline
            changed_rows += 1

        path.write_text("".join(lines), encoding="utf-8")

    return changed_rows


def main() -> None:
    print(f"refreshed Review Provenance IDs: {refresh()}")


if __name__ == "__main__":
    main()
