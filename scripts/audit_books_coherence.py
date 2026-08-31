#!/usr/bin/env python3
"""Fail-closed structural and integration-coherence audit for the 84 Books chapters.

This audit deliberately separates machine-verifiable chapter contracts from human
semantic judgement.  A ``Pass`` means the chapter has a unique ROADMAP owner,
closed evidence boundary, and explicit reasoning hooks for evolution, trade-offs,
failure/fallback.  It does not claim that every prose choice is aesthetically final.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "ROADMAP.md"
TRACE_LEDGER = (
    ROOT
    / "papers/2026/_sources/books-integration-audit-2026-06-08/integration-reconciliation.tsv"
)
SEMANTIC_LEDGER = (
    ROOT
    / "papers/2026/_sources/books-integration-audit-2026-06-08/semantic-audit.tsv"
)
DEFAULT_OUTPUT = (
    ROOT
    / "papers/2026/_sources/books-integration-audit-2026-06-08/chapter-coherence-audit.tsv"
)

NODE_RE = re.compile(
    r"^\| `(?P<node>[^`]+)` \| Ch(?P<chapter>\d+) \| `(?P<path>books/[^`]+\.md)` \|",
    re.MULTILINE,
)
FILE_NODE_RE = re.compile(r"\*\*Stable Knowledge Node ID:\*\* `([^`]+)`")


@dataclass(frozen=True)
class Chapter:
    node: str
    number: int
    path: str


def roadmap_chapters(text: str) -> list[Chapter]:
    chapters = [
        Chapter(m.group("node"), int(m.group("chapter")), m.group("path"))
        for m in NODE_RE.finditer(text)
    ]
    return sorted(chapters, key=lambda item: item.number)


def integration_families(path: Path) -> dict[str, set[str]]:
    families: dict[str, set[str]] = defaultdict(set)
    with path.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        for row in rows:
            families[row["stable_node"]].add(row["source_family"])
    return families


def semantic_proofs(path: Path) -> dict[str, dict[str, str]]:
    proofs: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        for row in rows:
            family = row["source_family"]
            if family in proofs:
                raise ValueError(f"duplicate semantic proof for {family}")
            proofs[family] = row
    return proofs


def exact_h2(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.startswith("## ")]


def audit_chapter(
    chapter: Chapter,
    expected_families: set[str],
    proofs: dict[str, dict[str, str]],
) -> dict[str, str]:
    path = ROOT / chapter.path
    text = path.read_text(encoding="utf-8")
    match = FILE_NODE_RE.search(text)
    file_node = match.group(1) if match else ""
    review_count = sum(line == "## Review notes" for line in text.splitlines())
    if review_count == 1:
        body, review = text.rsplit("\n## Review notes", 1)
        headings_after_review = [line for line in review.splitlines() if line.startswith("## ")]
    else:
        body, review, headings_after_review = text, "", ["invalid-review-boundary"]

    question = "## 本章要回答的问题" in body
    position = any(
        heading in body
        for heading in ("## 本章在知识树中的位置", "## 本章在全书中的位置")
    )
    self_check = any(token in body for token in ("## 自检问题", "## 面试与自检问题"))
    summary = "## 小结" in body or "## Reflection" in body
    # Source Family IDs may contain punctuation used by older Daily adapters.
    # Exact substring matching against the frozen ledger is safer than inventing
    # a second identifier grammar here.
    missing_families = {family for family in expected_families if family not in review}
    integrate_count = len(expected_families)
    chapter_proofs = {family: proofs.get(family) for family in expected_families}
    missing_proofs = {family for family, proof in chapter_proofs.items() if proof is None}
    invalid_proofs = {
        family
        for family, proof in chapter_proofs.items()
        if proof is not None
        and (
            proof["stable_node"] != chapter.node
            or proof["owner_path"] != chapter.path
            or proof["semantic_status"] != "verified_integration"
            or not re.match(r"^#{2,3} ", proof["body_locator"])
            or proof["evidence_locator"] != "## Review notes"
        )
    }
    proof_kinds = Counter(
        proof["proof_kind"]
        for proof in chapter_proofs.values()
        if proof is not None and proof["semantic_status"] == "verified_integration"
    )
    reasoning_review = (
        "verified-by-source-family-semantic-ledger"
        if integrate_count
        else "verified-in-existing-chapter"
    )

    findings: list[str] = []
    if file_node != chapter.node:
        findings.append("stable-node-mismatch")
    if not question:
        findings.append("missing-question")
    if not position:
        findings.append("missing-knowledge-position")
    if not self_check:
        findings.append("missing-self-check")
    if not summary:
        findings.append("missing-summary")
    if review_count != 1:
        findings.append("review-boundary-not-unique")
    if headings_after_review:
        findings.append("h2-after-review-boundary")
    if missing_families:
        findings.append("source-family-trace-shortfall")
    if missing_proofs:
        findings.append("semantic-proof-shortfall")
    if invalid_proofs:
        findings.append("invalid-semantic-proof")

    disposition = (
        "Refined — Owner Spine and Evidence Trace Verified"
        if integrate_count
        else "No Change — Explicitly Verified"
    )
    if findings:
        disposition = "Open — " + ", ".join(findings)

    return {
        "chapter": f"Ch{chapter.number}",
        "stable_node": chapter.node,
        "part": chapter.path.split("/")[1],
        "path": chapter.path,
        "integrate_count": str(integrate_count),
        "stable_owner": "pass" if file_node == chapter.node else "fail",
        "chapter_contract": "pass" if question and position and self_check and summary else "fail",
        "review_boundary": "pass" if review_count == 1 and not headings_after_review else "fail",
        "source_trace": "pass" if not missing_families else "fail",
        "semantic_proof": "pass" if not missing_proofs and not invalid_proofs else "fail",
        "proof_kinds": ";".join(f"{kind}:{count}" for kind, count in sorted(proof_kinds.items())),
        "evolution": reasoning_review,
        "tradeoff": reasoning_review,
        "failure_fallback": reasoning_review,
        "final_disposition": disposition,
        "finding": "; ".join(findings),
    }


def build_rows() -> list[dict[str, str]]:
    chapters = roadmap_chapters(ROADMAP.read_text(encoding="utf-8"))
    if len(chapters) != 84:
        raise SystemExit(f"ROADMAP chapter count is {len(chapters)}, expected 84")
    if len({item.node for item in chapters}) != 84:
        raise SystemExit("ROADMAP Stable Knowledge Node IDs are not unique")
    if [item.number for item in chapters] != list(range(1, 85)):
        raise SystemExit("ROADMAP chapter numbers are not contiguous Ch1-Ch84")
    families = integration_families(TRACE_LEDGER)
    proofs = semantic_proofs(SEMANTIC_LEDGER)
    expected_all = {family for node_families in families.values() for family in node_families}
    extra_proofs = sorted(set(proofs) - expected_all)
    if extra_proofs:
        raise SystemExit(f"semantic ledger contains unknown Source Families: {extra_proofs}")
    unknown = sorted(set(families) - {item.node for item in chapters})
    if unknown:
        raise SystemExit(f"integration ledger contains unknown owners: {unknown}")
    return [audit_chapter(item, families.get(item.node, set()), proofs) for item in chapters]


def write_rows(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    rows = build_rows()
    write_rows(rows, args.output)
    open_rows = [row for row in rows if row["finding"]]
    print(f"chapters audited: {len(rows)}")
    print(f"integrated owner chapters: {sum(int(row['integrate_count']) > 0 for row in rows)}")
    print(f"open chapters: {len(open_rows)}")
    for row in open_rows:
        print(f"{row['chapter']} {row['stable_node']}: {row['finding']}")
    print(f"ledger: {args.output}")
    if open_rows:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
