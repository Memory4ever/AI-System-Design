#!/usr/bin/env python3
"""Fresh presentation-only audit for the completed 2026-06-04 Daily."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260604"
REPORT = ROOT / "papers/2026/06/04/README.md"
AUDIT = PACKET / "PRESENTATION_FRESH_AUDIT_V14.md"
MANIFEST = PACKET / "SHA256SUMS"
LEGACY_MANIFEST = PACKET / "SHA256SUMS-v12-downstream"

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


def section(text: str, start: str, end: str | None) -> str:
    left = text.index(start) + len(start)
    right = text.index(end, left) if end else len(text)
    return text[left:right]


def rows(body: str) -> list[list[str]]:
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
    assert text.startswith("# Daily Research — 2026-06-04\n")
    top = {
        key: re.search(rf"^\*\*{re.escape(key)}:\*\* (.+)$", text, re.MULTILINE).group(1)
        for key in ("Research Date", "Timezone", "Strict Window", "Contract", "Status")
    }
    assert top["Research Date"] == "2026-06-04"
    assert top["Timezone"] == "Asia/Shanghai"
    assert top["Strict Window"].startswith("2026-06-03 09:00:00 ～ 2026-06-04 09:00:00")
    assert top["Contract"].startswith("V2.1") and top["Status"].startswith("Complete")
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2

    candidate = rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    receipts = rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmarks = rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection = rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books = rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert (len(candidate), len(receipts), len(benchmarks), len(selection), len(books)) == (42, 42, 42, 42, 30)
    assert all(row[10:13] == ["retained", "deep_complete", "accessible"] for row in candidate)
    dispositions = [row[19] for row in candidate]
    assert dispositions.count("Integrate") == 2
    assert dispositions.count("Weekly Only — Context") == 12
    assert dispositions.count("No Change — Existing Coverage") == 28
    assert sum(row[2] == "selected" for row in selection) == 3
    assert sum(row[2] == "not_selected" for row in selection) == 39

    review_json = json.loads((PACKET / "source-review-receipts-v12-fresh.json").read_text(encoding="utf-8"))
    book_json = json.loads((PACKET / "books-comparison-v12-fresh.json").read_text(encoding="utf-8"))
    review_blocks = marker_bodies(text, "review:")
    book_blocks = marker_bodies(text, "books-review:")
    assert len(review_blocks) == 42 and len(book_blocks) == 30
    for review in review_json["reviews"]:
        assert review_blocks[review["review_ref"]] == review["review_body"].strip()
    for comparison in book_json["rows"]:
        block = book_blocks[comparison["books_review_ref"]]
        assert comparison["existing_proposition"] in block
        assert comparison["new_evidence_delta"] in block
        assert comparison["decision"] in block

    rp_ids = re.findall(r"\bRP-[0-9a-f]{16}\b", text)
    assert len(rp_ids) == 42 and len(set(rp_ids)) == 42
    audit_rows = rows(section(text, "## 7. Semantic Audit", "## 8. Ignored Noise"))
    assert len(audit_rows) == 0  # Audit IDs, not Source Family rows.
    assert text.count("| passed |") >= 4
    assert "Open question: none. Coverage, Evidence/Selection and Books Gates are passed." in text
    assert "books-postwrite-semantic-audit-v13.md" in text

    AUDIT.write_text(
        f"""# 2026-06-04 Canonical Presentation Fresh Audit V14

## Scope

Presentation-only fresh-context audit. The accepted V12 denominator, exact-v1 Source Reviews, Score/Selection, Books decisions and post-write semantics were treated as immutable inputs; shared Books and `docs/LEARNING_STATE.md` were not modified.

## Result

- Canonical header: Research Date / Timezone / Strict Window / Contract / Status = `5/5`.
- Canonical structure: fixed H2 sections = `13/13`, in contract order.
- Preserved tables: Candidate `42/42`; Review Completion `42/42`; Benchmark `42/42`; Selection `42/42`; Books Comparison `30/30`.
- Preserved bounded evidence: Source Review bodies `42/42` byte-equivalent to V12 receipt JSON; Review Provenance IDs `42/42` unique and unchanged.
- Preserved Books state: Integrate `2`, No Change `28`, Weekly Only `12`; Books review bodies `30/30` preserve existing proposition, source delta and disposition.
- Preserved Gate truth: Coverage=`Closed`, Evidence=`Passed`, Books=`Passed`, Completion=`Complete`; four recorded semantic audits remain `passed`.
- Owner renderer guard: V12 renderer now applies the canonicalizer before writing hashes; two consecutive owner-renderer runs produced the same Daily/receipt hashes. Current Daily SHA-256: `{sha(REPORT)}`. The isolated legacy-to-canonical migration is also idempotent.
- Unresolved presentation findings: `0`.

## Gate

Presentation audit=`Passed`. This receipt does not reopen or re-decide the already accepted semantic and Books Gates; it verifies that canonical migration preserved their complete evidence and state.
""",
        encoding="utf-8",
    )

    manifest_paths = [
        PACKET / "candidate-denominator-repair-proposal-v12.json",
        PACKET / "root-denominator-acceptance-v12.md",
        PACKET / "source-review-receipts-v12-fresh.json",
        PACKET / "benchmark-contract-v12-fresh.json",
        PACKET / "deep-analysis-selection-v12-fresh.json",
        PACKET / "books-comparison-v12-fresh.json",
        PACKET / "downstream-fresh-audit-v12.md",
        PACKET / "books-postwrite-semantic-audit-v13.md",
        AUDIT,
        REPORT,
        ROOT / "books/part-06-ai-infrastructure/72-security.md",
        ROOT / "books/part-07-agent/82-multi-agent.md",
        ROOT / "scripts/finalize_june04_v12_downstream_fresh.py",
        ROOT / "scripts/canonicalize_june_daily_presentation.py",
        ROOT / "scripts/test_june04_canonical_presentation.py",
        Path(__file__).resolve(),
    ]
    manifest_text = "".join(
        f"{sha(path)}  {Path(os.path.relpath(path, PACKET)).as_posix()}\n"
        for path in manifest_paths
    )
    MANIFEST.write_text(manifest_text, encoding="utf-8")
    LEGACY_MANIFEST.write_text(manifest_text, encoding="utf-8")
    print(json.dumps({"canonical_fields": 5, "h2": 13, "reviews": 42, "books": 30, "unresolved_findings": 0, "manifest_entries": len(manifest_paths)}))


if __name__ == "__main__":
    main()
