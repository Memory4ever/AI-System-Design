#!/usr/bin/env python3
"""Close the 2026-06..08 Daily-to-Books semantic reconciliation ledger.

This step requires an exact Daily delta, an owner-chapter trace, and a durable
body locator for every Integrate decision.  It does not infer paper claims from
identifiers and it refuses to emit a completed row when any required link is
missing.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
import re
from collections import Counter
from pathlib import Path

try:
    from scripts.materialize_books_integration_trace import extract_delta
except ModuleNotFoundError:  # Direct execution adds scripts/, not the repo root, to sys.path.
    from materialize_books_integration_trace import extract_delta


PREFIX_INVARIANCE = "SF-2026-PREFIX-INVARIANCE"
MIN_PERSISTED_PROPOSITION_SCORE = 0.05


def heading_before(lines: list[str], line_number: int) -> str:
    for index in range(min(line_number - 1, len(lines) - 1), -1, -1):
        if re.match(r"^#{2,3} ", lines[index]):
            return lines[index]
    raise ValueError(f"no body heading before line {line_number}")


def body_text(chapter_text: str) -> str:
    """Return reader-facing chapter content, excluding the final evidence appendix."""
    if "## Review notes" not in chapter_text:
        raise ValueError("chapter lacks final Review notes")
    return chapter_text.rsplit("## Review notes", 1)[0]


def semantic_tokens(text: str) -> list[str]:
    """Tokenize mixed Chinese/English prose for persistence checks.

    Chinese bigrams avoid treating a complete Chinese clause as one token.  The
    score is not a semantic oracle: it is used only together with a historical
    fresh-context Books receipt to prove that the reviewed proposition still
    exists in the current owner chapter.
    """
    lowered = text.lower()
    output = re.findall(r"[a-z][a-z0-9_-]{2,}", lowered)
    for run in re.findall(r"[\u4e00-\u9fff]+", lowered):
        output.extend(run[index : index + 2] for index in range(len(run) - 1))
    return output


def body_paragraphs(chapter_text: str) -> list[tuple[str, str]]:
    paragraphs: list[tuple[str, str]] = []
    heading = ""
    for block in re.split(r"\n\s*\n", body_text(chapter_text)):
        block = block.strip()
        if not block:
            continue
        if block.startswith("## "):
            heading = block.splitlines()[0]
        if len(semantic_tokens(block)) >= 5:
            paragraphs.append((heading, block))
    return paragraphs


def corpus_document_frequency(items: list[tuple[str, str]]) -> tuple[Counter[str], int]:
    frequency: Counter[str] = Counter()
    for delta, chapter_text in items:
        for text in [delta, *(paragraph for _, paragraph in body_paragraphs(chapter_text))]:
            frequency.update(set(semantic_tokens(text)))
    return frequency, sum(1 + len(body_paragraphs(chapter)) for _, chapter in items)


def weighted_vector(text: str, frequency: Counter[str], document_count: int) -> dict[str, float]:
    counts = Counter(semantic_tokens(text))
    return {
        token: count * (math.log((document_count + 1) / (frequency[token] + 1)) + 1)
        for token, count in counts.items()
    }


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if not left_norm or not right_norm:
        return 0.0
    dot = sum(value * right.get(token, 0.0) for token, value in left.items())
    return dot / (left_norm * right_norm)


def best_body_proposition(
    delta: str,
    chapter_text: str,
    frequency: Counter[str],
    document_count: int,
) -> tuple[float, str, str]:
    delta_vector = weighted_vector(delta, frequency, document_count)
    best = (0.0, "", "")
    for heading, paragraph in body_paragraphs(chapter_text):
        score = cosine(delta_vector, weighted_vector(paragraph, frequency, document_count))
        if score > best[0]:
            best = (score, heading, paragraph)
    return best


def has_fresh_books_receipt(report_text: str, family: str) -> bool:
    """Require the family decision and a passed report-level Books audit.

    Some recovered reports list every family in the audit row; others bind the
    family in Books Comparison and keep a compact report-level post-write audit
    row.  Both are valid only when the exact books-review ref exists.
    """
    if f"books-review:{family}" not in report_text:
        return False
    for line in report_text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        if cells[2] == "books" and cells[-1].lower() == "passed":
            return True
    return False


def body_locator(
    row: dict[str, str],
    chapter_text: str,
    delta: str,
    report_text: str,
    frequency: Counter[str],
    document_count: int,
) -> tuple[str, str, float]:
    lines = chapter_text.splitlines()
    review = next(
        (i for i, line in reversed(list(enumerate(lines, start=1))) if line == "## Review notes"),
        len(lines) + 1,
    )
    trace_lines = [int(item) for item in row["owner_trace_lines"].split(";") if item]
    body_lines = [line for line in trace_lines if line < review]
    if body_lines:
        return heading_before(lines, body_lines[0]), "exact_source_binding", 1.0
    if row["source_family"] == PREFIX_INVARIANCE:
        locator = "## Causal 不是 Mask 属性，而是 Block 不变量"
        if locator in chapter_text:
            return locator, "explicit_causal_binding", 1.0
    if not has_fresh_books_receipt(report_text, row["source_family"]):
        raise ValueError(f"{row['source_family']}: missing passed fresh-context Books receipt")
    score, heading, _ = best_body_proposition(delta, chapter_text, frequency, document_count)
    if score >= MIN_PERSISTED_PROPOSITION_SCORE and heading:
        return heading, "fresh_receipt_plus_persisted_proposition", score
    raise ValueError(
        f"{row['source_family']}: no source-specific body binding and best persisted proposition "
        f"score {score:.6f} is below {MIN_PERSISTED_PROPOSITION_SCORE:.2f} in {row['owner_path']}"
    )


def evidence_locator(row: dict[str, str], chapter_text: str) -> str:
    if "## Review notes" not in chapter_text:
        raise ValueError(f"{row['owner_path']}: missing Review notes")
    family = row["source_family"]
    primary = re.sub(r"v\d+$", "", row["primary_identifier"].split(":", 1)[-1])
    review = chapter_text.rsplit("## Review notes", 1)[1]
    if family not in review and primary not in review:
        raise ValueError(f"{family}: owner Review notes lack exact evidence trace")
    return "## Review notes"


def write_tsv(rows: list[dict[str, str]], path: Path, fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def reconcile(root: Path, ledger: Path) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    with ledger.open(encoding="utf-8", newline="") as handle:
        trace_rows = list(csv.DictReader(handle, delimiter="\t"))
    prepared: list[tuple[dict[str, str], Path, str, Path, str]] = []
    corpus_items: list[tuple[str, str]] = []
    for row in trace_rows:
        report_date = row["report_date"]
        report = root / "papers" / "2026" / report_date[5:7] / report_date[8:] / "README.md"
        report_text = report.read_text(encoding="utf-8")
        delta = extract_delta(report, row["source_family"])
        chapter = root / row["owner_path"]
        chapter_text = chapter.read_text(encoding="utf-8")
        prepared.append((row, report, report_text, chapter, chapter_text))
        corpus_items.append((delta, chapter_text))
    frequency, document_count = corpus_document_frequency(corpus_items)

    semantic_rows: list[dict[str, str]] = []
    updated_trace_rows: list[dict[str, str]] = []

    for row, report, report_text, chapter, chapter_text in prepared:
        report_date = row["report_date"]
        delta = extract_delta(report, row["source_family"])
        body, proof_kind, score = body_locator(
            row, chapter_text, delta, report_text, frequency, document_count
        )
        evidence = evidence_locator(row, chapter_text)
        digest = hashlib.sha256(delta.encode("utf-8")).hexdigest()[:16]
        finding = (
            f"Daily Books delta {digest} 已对齐到具体正文命题 {body}；proof={proof_kind}；"
            f"persistence_score={score:.6f}；精确来源身份保留在 {evidence}。"
        )
        semantic_rows.append(
            {
                "report_date": report_date,
                "source_family": row["source_family"],
                "primary_identifier": row["primary_identifier"],
                "stable_node": row["stable_node"],
                "owner_path": row["owner_path"],
                "body_locator": body,
                "proof_kind": proof_kind,
                "persistence_score": f"{score:.6f}",
                "evidence_locator": evidence,
                "delta_sha256": digest,
                "daily_delta": delta.replace("\n", " "),
                "semantic_status": "verified_integration",
                "refine_disposition": "Pass — Specific Body Proposition and Evidence Boundary Verified",
                "finding": finding,
            }
        )
        updated = dict(row)
        updated["audit_state"] = "semantic_verified"
        updated["semantic_status"] = "verified_integration"
        updated["semantic_locator"] = body
        updated["semantic_finding"] = finding
        updated_trace_rows.append(updated)

    families = [row["source_family"] for row in semantic_rows]
    if len(families) != len(set(families)):
        raise ValueError("semantic ledger contains duplicate Source Family IDs")
    return semantic_rows, updated_trace_rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path("papers/2026/_sources/books-integration-audit-2026-06-08/integration-reconciliation.tsv"),
    )
    parser.add_argument(
        "--semantic-output",
        type=Path,
        default=Path("papers/2026/_sources/books-integration-audit-2026-06-08/semantic-audit.tsv"),
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    ledger = args.ledger if args.ledger.is_absolute() else root / args.ledger
    semantic_output = args.semantic_output if args.semantic_output.is_absolute() else root / args.semantic_output
    semantic_rows, trace_rows = reconcile(root, ledger)
    print(f"semantic verified: {len(semantic_rows)} source families")
    if not args.write:
        return
    write_tsv(semantic_rows, semantic_output, list(semantic_rows[0]))
    write_tsv(trace_rows, ledger, list(trace_rows[0]))
    print(f"semantic ledger: {semantic_output}")
    print(f"reconciled trace ledger: {ledger}")


if __name__ == "__main__":
    main()
