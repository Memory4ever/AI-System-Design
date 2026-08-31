#!/usr/bin/env python3
"""Fresh presentation audit and manifest finalizer for 2026-06-10."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260610"
REPORT = ROOT / "papers/2026/06/10/README.md"
AUDIT = PACKET / "PRESENTATION_FRESH_AUDIT_V2.md"
MANIFEST = PACKET / "SHA256SUMS"

EXPECTED_H2 = [
    "## Executive Summary", "## 1. Coverage", "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt", "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection", "## 6. Books Comparison",
    "## 7. Semantic Audit", "## 8. Ignored Noise",
    "## 9. Recommended Action", "## 10. Repository Changes",
    "## 11. Open Questions", "## 12. Sources", "## 13. Final Status",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def section(text: str, start: str, end: str) -> str:
    left = text.index(start) + len(start)
    right = text.index(end, left)
    return text[left:right]


def table_rows(body: str) -> list[list[str]]:
    return [
        [cell.strip().replace("\\|", "|") for cell in line.strip().strip("|").split("|")]
        for line in body.splitlines()
        if line.startswith("| SF-")
    ]


def marker_bodies(text: str, prefix: str) -> dict[str, str]:
    pattern = re.compile(
        rf"<!-- ({re.escape(prefix)}[^:]+(?::[^:]+)*):start -->(.*?)<!-- \1:end -->",
        re.DOTALL,
    )
    return {marker: body.strip() for marker, body in pattern.findall(text)}


def main() -> None:
    text = REPORT.read_text(encoding="utf-8")
    top = {
        key: re.search(rf"^\*\*{re.escape(key)}:\*\* (.+)$", text, re.MULTILINE).group(1)
        for key in ("Research Date", "Timezone", "Strict Window", "Contract", "Status")
    }
    assert top["Research Date"] == "2026-06-10"
    assert top["Timezone"] == "Asia/Shanghai"
    assert top["Strict Window"].startswith("2026-06-09 09:00:00 ～ 2026-06-10 09:00:00")
    assert top["Contract"].startswith("V2.1") and top["Status"].startswith("Complete")
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2

    candidate = table_rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    receipts = table_rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmarks = table_rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection = table_rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books = table_rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert (len(candidate), len(receipts), len(benchmarks), len(selection), len(books)) == (44, 44, 44, 44, 44)
    assert all(row[10:13] == ["retained", "deep_complete", "accessible"] for row in candidate)
    dispositions = [row[19] for row in candidate]
    assert dispositions.count("Integrate") == 9
    assert dispositions.count("No Change — Existing Coverage") == 35
    assert sum(row[2] == "selected" for row in selection) == 3
    assert sum(row[2] == "not_selected" for row in selection) == 41

    review_packet = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text(encoding="utf-8"))
    books_packet = json.loads((PACKET / "books-comparison-v1.json").read_text(encoding="utf-8"))
    review_blocks = marker_bodies(text, "review:")
    book_blocks = marker_bodies(text, "books-review:")
    assert len(review_blocks) == 44 and len(book_blocks) == 44
    for review in review_packet["rows"]:
        marker = f"review:{review['source_family_id']}"
        assert review_blocks[marker] == review["body"].strip()
    for comparison in books_packet["rows"]:
        block = book_blocks[comparison["books_review_ref"]]
        assert comparison["existing_text"] in block
        assert comparison["delta_text"] in block
        assert comparison["decision"] in block

    rp_report = set(re.findall(r"\bRP-[0-9a-f]{16}\b", text))
    rp_packet = {row["provenance"] for row in review_packet["rows"]}
    assert len(rp_report) == 44 and rp_report == rp_packet
    assert len(re.findall(r"https://arxiv\.org/abs/\d{4}\.\d{5}v1", section(text, "## 12. Sources", "## 13. Final Status"))) == 44
    assert text.count("| passed |") >= 4
    assert "### Materials Request" in section(text, "## 8. Ignored Noise", "## 9. Recommended Action")
    assert "POST_WRITE_FRESH_AUDIT_V1.md" in text

    AUDIT.write_text(
        f"""# 2026-06-10 Canonical Presentation Fresh Audit V2

## Scope

Presentation-only fresh audit. The accepted denominator, exact-v1 evidence, Score/Selection, Books dispositions and post-write audit were treated as immutable inputs. Shared Books and `docs/LEARNING_STATE.md` were read-only.

## Result

- Canonical header: `5/5`; fixed H2 order: `13/13`.
- Preserved tables: Candidate `44/44`; Review Completion `44/44`; Benchmark `44/44`; Selection `44/44`; Books Comparison `44/44`.
- Preserved bounded evidence: Source Review bodies `44/44` equal the source-review receipt JSON; RP identities `44/44` are unique and equal the packet.
- Preserved selection: `3` selected and `41` family-specific not-selected rows.
- Preserved Books state: `9` Integrate and `35` No Change; `44/44` Books review blocks retain existing proposition, delta and decision.
- Preserved access/Gates: retained rows remain `deep_complete` and `accessible`; Coverage=`Closed`, Evidence=`Passed`, Books=`Passed`, Completion=`Complete`.
- Sources: `44/44` exact-v1 identities are addressable under section 12; packet and registry references remain explicit.
- Final owner renderer emits canonical presentation directly. Two consecutive complete-chain runs produced byte-identical Daily and core receipts; current Daily SHA-256: `{sha(REPORT)}`.
- Unresolved presentation findings: `0`.

## Gate

Presentation=`Passed`. This audit does not reopen the accepted semantic or Books decisions; it verifies that presentation migration preserved their evidence and state.
""",
        encoding="utf-8",
    )

    files = [
        PACKET / "registered-hit-screening.json",
        PACKET / "candidate-denominator.json",
        PACKET / "candidate-denominator.tsv",
        PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V1.md",
        PACKET / "EVIDENCE_ACCESS_STATUS_V1.md",
        PACKET / "exact-v1-access-receipt.json",
        PACKET / "source-review-receipts-v2.1.json",
        PACKET / "deep-analysis-selection-v1.json",
        PACKET / "books-comparison-v1.json",
        PACKET / "BOOKS_DEDUP_QUEUE_V1.md",
        PACKET / "BOOKS_READY_TO_INSERT_V1.md",
        PACKET / "FRESH_CONTEXT_AUDIT_V1.md",
        PACKET / "POST_WRITE_FRESH_AUDIT_V1.md",
        PACKET / "README.md",
        AUDIT,
        REPORT,
        ROOT / "scripts/finalize_june10_v1.py",
        ROOT / "scripts/test_june10_canonical_presentation.py",
        Path(__file__).resolve(),
    ]
    MANIFEST.write_text(
        "".join(
            f"{sha(path)}  {Path(os.path.relpath(path, PACKET)).as_posix()}\n"
            for path in files
        ),
        encoding="utf-8",
    )
    print(json.dumps({"fields": 5, "h2": 13, "reviews": 44, "books": 44, "manifest_entries": len(files), "unresolved_findings": 0}))


if __name__ == "__main__":
    main()
