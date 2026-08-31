#!/usr/bin/env python3
"""Build a reproducible Daily-to-Books trace ledger for 2026-06 through 2026-08.

This is deliberately a trace audit, not a semantic completion oracle.  A marker
or identifier can locate text, but only a later human/fresh-context review can
decide whether the durable mechanism was integrated correctly.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


MONTHS = {"06", "07", "08"}


@dataclass(frozen=True)
class Candidate:
    report_date: str
    source_family: str
    primary_identifier: str
    stable_node: str
    books_disposition: str
    books_review_ref: str


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_roadmap(roadmap: Path) -> dict[str, str]:
    owners: dict[str, str] = {}
    for line in roadmap.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [cell.strip().strip("`") for cell in split_table_row(line)]
        if len(cells) < 3 or not re.fullmatch(r"[A-Z][A-Z0-9-]+", cells[0]):
            continue
        owners[cells[0]] = cells[2]
    return owners


def parse_integrate_candidates(report: Path) -> list[Candidate]:
    rows: list[Candidate] = []
    header: list[str] | None = None
    indexes: dict[str, int] = {}
    in_ledger = False
    report_date = f"2026-{report.parent.parent.name}-{report.parent.name}"

    for line in report.read_text(encoding="utf-8").splitlines():
        if "validator:candidate-ledger-v2.1" in line:
            in_ledger = True
            continue
        if in_ledger and line.startswith("## "):
            break
        if not in_ledger or not line.startswith("|") or "---" in line:
            continue

        cells = split_table_row(line)
        if header is None:
            header = cells
            indexes = {name: index for index, name in enumerate(header)}
            required = {
                "Source Family ID",
                "Primary Identifier",
                "Stable Node ID",
                "Books Disposition",
                "Books Review Ref",
            }
            missing = required - indexes.keys()
            if missing:
                raise ValueError(f"{report}: candidate ledger missing {sorted(missing)}")
            continue
        if len(cells) < len(header):
            continue
        if cells[indexes["Books Disposition"]] != "Integrate":
            continue

        rows.append(
            Candidate(
                report_date=report_date,
                source_family=cells[indexes["Source Family ID"]].strip("` "),
                primary_identifier=cells[indexes["Primary Identifier"]].strip("` "),
                stable_node=cells[indexes["Stable Node ID"]].strip("` "),
                books_disposition=cells[indexes["Books Disposition"]],
                books_review_ref=cells[indexes["Books Review Ref"]].strip("` "),
            )
        )
    return rows


def line_numbers(text: str, needle: str) -> list[int]:
    if not needle:
        return []
    return [index for index, line in enumerate(text.splitlines(), start=1) if needle in line]


def primary_token(identifier: str) -> str:
    match = re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?", identifier)
    return match.group(1) if match else identifier


def classify_location(lines: list[int], summary_line: int | None, review_line: int | None) -> str:
    if not lines:
        return "none"
    # The final Review notes heading is the evidence boundary. Some Parts use
    # Reflection rather than 小结, so summary presence cannot define body scope.
    if summary_line is not None and any(line < summary_line for line in lines):
        return "main_body"
    if summary_line is not None and review_line is not None and any(summary_line <= line < review_line for line in lines):
        return "after_summary"
    if summary_line is None and review_line is not None and any(line < review_line for line in lines):
        return "main_body"
    if review_line is not None and all(line > review_line for line in lines):
        return "review_only"
    if summary_line is not None and any(line >= summary_line for line in lines):
        return "after_summary"
    return "review_only"


def build_rows(root: Path) -> list[dict[str, str | int]]:
    owners = parse_roadmap(root / "ROADMAP.md")
    book_paths = sorted((root / "books").glob("part-*/*.md"))
    book_texts = {path.relative_to(root).as_posix(): path.read_text(encoding="utf-8") for path in book_paths}
    output: list[dict[str, str | int]] = []

    reports = sorted((root / "papers" / "2026").glob("*/*/README.md"))
    candidates: list[Candidate] = []
    for report in reports:
        if report.parent.parent.name not in MONTHS or not report.parent.name.isdigit():
            continue
        candidates.extend(parse_integrate_candidates(report))

    seen = Counter(candidate.source_family for candidate in candidates)
    duplicates = sorted(family for family, count in seen.items() if count != 1)
    if duplicates:
        raise ValueError(f"Integrate Source Family IDs must be unique: {duplicates[:10]}")

    for candidate in candidates:
        owner_path = owners.get(candidate.stable_node, "")
        owner_text = book_texts.get(owner_path, "")
        owner_lines = owner_text.splitlines()
        summary_line = next((i for i, line in enumerate(owner_lines, start=1) if line == "## 小结"), None)
        review_line = next(
            (i for i, line in reversed(list(enumerate(owner_lines, start=1))) if line == "## Review notes"),
            None,
        )

        family_lines = line_numbers(owner_text, candidate.source_family)
        token = primary_token(candidate.primary_identifier)
        primary_lines = line_numbers(owner_text, token)
        foreign_family_paths = [path for path, text in book_texts.items() if path != owner_path and candidate.source_family in text]
        foreign_primary_paths = [path for path, text in book_texts.items() if path != owner_path and token and token in text]

        if family_lines:
            trace_kind = "source_family"
            trace_lines = family_lines
        elif primary_lines:
            trace_kind = "primary_identifier"
            trace_lines = primary_lines
        elif foreign_family_paths or foreign_primary_paths:
            trace_kind = "foreign_owner_only"
            trace_lines = []
        else:
            trace_kind = "no_machine_trace"
            trace_lines = []

        location = classify_location(trace_lines, summary_line, review_line)
        if trace_kind == "foreign_owner_only":
            audit_state = "owner_review_required"
        elif trace_kind == "no_machine_trace":
            audit_state = "semantic_review_required"
        elif location == "review_only":
            audit_state = "citation_only_review_required"
        elif location == "after_summary":
            audit_state = "integrated_flow_refine_required"
        else:
            audit_state = "semantic_confirmation_required"

        output.append(
            {
                "report_date": candidate.report_date,
                "source_family": candidate.source_family,
                "primary_identifier": candidate.primary_identifier,
                "stable_node": candidate.stable_node,
                "owner_path": owner_path,
                "books_disposition": candidate.books_disposition,
                "books_review_ref": candidate.books_review_ref,
                "trace_kind": trace_kind,
                "trace_location": location,
                "owner_trace_lines": ";".join(map(str, trace_lines)),
                "foreign_paths": ";".join(sorted(set(foreign_family_paths + foreign_primary_paths))),
                "audit_state": audit_state,
                "semantic_status": "pending",
                "semantic_locator": "",
                "semantic_finding": "",
            }
        )
    return output


def write_ledger(rows: list[dict[str, str | int]], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys()),
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict[str, str | int]]) -> None:
    months = Counter(str(row["report_date"])[5:7] for row in rows)
    traces = Counter(str(row["trace_kind"]) for row in rows)
    locations = Counter(str(row["trace_location"]) for row in rows)
    states = Counter(str(row["audit_state"]) for row in rows)
    print(f"Integrate candidates: {len(rows)}")
    print(f"By month: {dict(sorted(months.items()))}")
    print(f"Trace kind: {dict(sorted(traces.items()))}")
    print(f"Trace location: {dict(sorted(locations.items()))}")
    print(f"Initial audit state: {dict(sorted(states.items()))}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = build_rows(args.root.resolve())
    print_summary(rows)
    if args.output:
        output = args.output if args.output.is_absolute() else args.root / args.output
        write_ledger(rows, output)
        print(f"Ledger: {output}")


if __name__ == "__main__":
    main()
