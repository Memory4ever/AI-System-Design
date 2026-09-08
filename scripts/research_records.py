#!/usr/bin/env python3
"""Render/check family table projections without inventing evidence or Gate states."""
import argparse
import json
import os
import re
import tempfile
from pathlib import Path

try:
    from . import validate_research as v
except ImportError:  # Direct CLI execution.
    import validate_research as v


TABLES = (
    (v.CANDIDATE_LEDGER_MARKER, v.CANDIDATE_COLUMNS),
    (v.REVIEW_COMPLETION_MARKER, v.REVIEW_COMPLETION_COLUMNS),
    (v.BOOKS_COMPARISON_MARKER, v.BOOKS_COMPARISON_COLUMNS),
    (v.BENCHMARK_MARKER, v.BENCHMARK_COLUMNS),
)
DERIVED = {"Total", "Review Route", "Completion Result", "Review Provenance ID", "Decision"}
ALLOWED = set().union(*(set(columns) for _, columns in TABLES)) - DERIVED
ALLOWED.add("Considered Owners")


def _rows(text, marker, columns):
    rows, errors = v._expect_columns(text, marker, columns)
    if errors:
        raise ValueError("; ".join(errors))
    return rows


def extract(text):
    """Bootstrap records from existing evidence, never declare a migration complete."""
    families = {}
    for marker, columns in TABLES:
        if marker == v.BENCHMARK_MARKER and marker not in text:
            continue
        seen = set()
        for row in _rows(text, marker, columns):
            family = row["Source Family ID"].strip("`")
            if family in seen:
                raise ValueError(f"duplicate family {family} in {marker}")
            seen.add(family)
            if marker != v.CANDIDATE_LEDGER_MARKER and family not in families:
                raise ValueError(f"orphan family {family} in {marker}")
            record = families.setdefault(family, {})
            for key, value in row.items():
                if key in DERIVED:
                    continue
                value = value.strip("`")
                if key == "Stable Node ID" and value.startswith("considered:"):
                    key = "Considered Owners"
                if key in record and record[key] != value:
                    raise ValueError(f"conflicting {key} for {family}")
                record[key] = value
    return {"schema": "research-records-v1", "families": list(families.values())}


def _project(text, record):
    if set(record) - ALLOWED:
        raise ValueError(f"unknown fields: {sorted(set(record) - ALLOWED)}")
    if any(not isinstance(value, str) or "\n" in value or "|" in value for value in record.values()):
        raise ValueError("record fields must be single-line strings without Markdown table pipes")
    candidate = {key: record[key] for key in v.CANDIDATE_COLUMNS if key != "Total"}
    scores = [candidate[key] for key in ("Design Delta", "System Reach", "Durability")]
    if all(score in v.ABSENT_VALUES for score in scores):
        candidate["Total"] = "—"
    elif all(score in {"0", "1", "2", "3"} for score in scores):
        candidate["Total"] = str(sum(map(int, scores)))
    else:
        raise ValueError("scores must be three 0..3 values or three explicit absent values")
    route = v._actual_review_route(candidate)
    status = candidate["Review Status"]
    result = {"deep_complete": "complete", "standard_complete": "complete",
              "closure_complete": "complete", "pending": "pending", "blocked": "blocked",
              "not_required": "not_required"}.get(status)
    if result is None or (status.endswith("_complete") and status != route + "_complete"):
        raise ValueError("Review Status conflicts with score/override route")
    receipt = {key: record[key] for key in v.REVIEW_COMPLETION_COLUMNS if key not in DERIVED}
    receipt.update({"Review Route": route, "Completion Result": result, "Review Provenance ID": "—"})
    if result != "pending":
        errors = []
        body = v._bounded_segment(text, candidate["Review Ref"], "Review", errors)
        if errors or body is None:
            raise ValueError("; ".join(errors) or "missing review body")
        receipt["Review Provenance ID"] = v._expected_review_provenance(
            candidate["Source Family ID"], candidate, route, receipt["Primary Evidence Version"],
            receipt["Reviewed Evidence Versions"], receipt["Method / Identity Locators"],
            receipt["Evaluation Locators"], receipt["Limitations / Counterevidence Locators"],
            receipt["Artifact Locators"], receipt["Claim Boundary Ref"], candidate["Review Ref"],
            v._normalized_body_sha256(body),
        )
    books = None
    if candidate["Books Disposition"] in {"Integrate", "No Change — Existing Coverage", "Structural Candidate"}:
        books = {key: record[key] for key in v.BOOKS_COMPARISON_COLUMNS if key != "Decision"}
        books["Decision"] = candidate["Books Disposition"]
        if books["Decision"] == "Structural Candidate":
            books["Stable Node ID"] = record["Considered Owners"]
    benchmark = None
    if candidate["Benchmark Claim"] == "yes":
        benchmark = {key: record[key] for key in v.BENCHMARK_COLUMNS}
    return candidate, receipt, books, benchmark


def _replace_table(text, marker, columns, rows):
    if text.count(marker) != 1:
        raise ValueError(f"expected one projection marker: {marker}")
    start = text.index(marker) + len(marker)
    match = re.match(r"\s*\n(?:\|[^\n]*\|[ \t]*(?:\n|$))+", text[start:])
    if not match:
        raise ValueError(f"missing table following {marker}")
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    lines.extend("| " + " | ".join(row[key] for key in columns) + " |" for row in rows)
    return text[:start] + "\n" + "\n".join(lines) + "\n" + text[start + match.end():]


def render(text, canonical):
    if not isinstance(canonical, dict) or canonical.get("schema") != "research-records-v1" or not isinstance(canonical.get("families"), list):
        raise ValueError("unsupported canonical record schema")
    metadata = dict((r["Field"], r["Value"]) for r in _rows(text, v.METADATA_MARKER, v.METADATA_COLUMNS))
    if metadata.get("Contract Version") != "V2.2":
        raise ValueError("render requires explicit V2.2 migration; legacy reports remain unchanged")
    projections = [[] for _ in TABLES]
    seen = set()
    for record in canonical["families"]:
        if not isinstance(record, dict):
            raise ValueError("each family record must be an object")
        family = record.get("Source Family ID")
        if not family or family in seen:
            raise ValueError(f"missing/duplicate family {family}")
        seen.add(family)
        try:
            projected = _project(text, record)
        except KeyError as exc:
            raise ValueError(f"{family}: missing field {exc}") from exc
        for rows, row in zip(projections, projected):
            if row is not None:
                rows.append(row)
    for (marker, columns), rows in zip(TABLES, projections):
        if marker == v.BENCHMARK_MARKER and not rows and marker not in text:
            continue
        text = _replace_table(text, marker, columns, rows)
    return text


def drift(text, canonical):
    return [] if text == render(text, canonical) else ["family record projections or RP are stale"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("extract", "check", "render"))
    parser.add_argument("report", type=Path)
    parser.add_argument("records", type=Path)
    parser.add_argument("--write", action="store_true", help="write projections; default render prints a preview")
    args = parser.parse_args()
    original = args.report.read_text(encoding="utf-8")
    try:
        if args.mode == "extract":
            # Never overwrite an existing authoritative record during recovery.
            canonical = extract(original)
            with args.records.open("x", encoding="utf-8") as target:
                json.dump(canonical, target, ensure_ascii=False, indent=2)
                target.write("\n")
            return 0
        canonical = json.loads(args.records.read_text(encoding="utf-8"))
        if args.mode == "check":
            errors = drift(original, canonical)
            print("\n".join(errors) if errors else "Projections match; semantic acceptance is not evaluated.")
            return int(bool(errors))
        rendered = render(original, canonical)
        if args.write:
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=args.report.parent,
                                                 prefix=".research-render-", delete=False) as target:
                    temporary = Path(target.name)
                    target.write(rendered)
                os.chmod(temporary, args.report.stat().st_mode)
                if args.report.read_text(encoding="utf-8") != original:
                    raise ValueError("report changed during rendering; reload before writing")
                os.replace(temporary, args.report)
            finally:
                if temporary is not None and temporary.exists():
                    temporary.unlink()
        else:
            print(rendered, end="")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
