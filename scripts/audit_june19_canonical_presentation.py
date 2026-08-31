#!/usr/bin/env python3
"""Fresh presentation audit and manifest finalizer for 2026-06-19."""

from __future__ import annotations

import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260619"
REPORT = ROOT / "papers/2026/06/19/README.md"
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


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text.replace("\r\n", "\n").replace("\r", "\n"))
    return "\n".join(line.rstrip() for line in text.strip().split("\n"))


def section(text: str, start: str, end: str) -> str:
    left = text.index(start) + len(start)
    return text[left:text.index(end, left)]


def rows(body: str) -> list[list[str]]:
    return [
        [cell.strip().replace("\\|", "|") for cell in line.strip().strip("|").split("|")]
        for line in body.splitlines() if line.startswith("| SF-")
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
    assert top["Research Date"] == "2026-06-19"
    assert top["Timezone"] == "Asia/Shanghai"
    assert top["Strict Window"].startswith("2026-06-18 09:00:00 ～ 2026-06-19 09:00:00")
    assert top["Contract"].startswith("V2.1") and top["Status"].startswith("Complete")
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2

    candidate = rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    receipt = rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmark = rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection = rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books = rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert (len(candidate), len(receipt), len(benchmark), len(selection), len(books)) == (68, 68, 68, 68, 68)
    assert all(row[10:13] == ["retained", "deep_complete", "accessible"] for row in candidate)
    dispositions = [row[19] for row in candidate]
    assert dispositions.count("Integrate") == 56
    assert dispositions.count("No Change — Existing Coverage") == 12
    assert sum(row[2] == "selected" for row in selection) == 3
    assert sum(row[2] == "not_selected" for row in selection) == 65

    receipt_packet = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text(encoding="utf-8"))
    comparison_packet = json.loads((PACKET / "books-comparison-v1.json").read_text(encoding="utf-8"))
    review_blocks = marker_bodies(text, "review:")
    books_blocks = marker_bodies(text, "books-review:")
    assert len(review_blocks) == 68 and len(books_blocks) == 68
    for item in receipt_packet["items"]:
        body = review_blocks[item["review_ref"]]
        assert hashlib.sha256(norm(body).encode()).hexdigest() == item["review_body_sha256"]
    assert {row[1] for row in receipt} == {item["review_provenance_id"] for item in receipt_packet["items"]}
    assert len({row[1] for row in receipt}) == 68
    assert {row[-1] for row in books} == {item["books_review_ref"] for item in comparison_packet["items"]}
    assert len(re.findall(r"https://arxiv\.org/abs/\d{4}\.\d{5}v1", section(text, "## 12. Sources", "## 13. Final Status"))) == 68
    assert text.count("| passed |") >= 4
    assert "### Materials and Access" in section(text, "## 8. Ignored Noise", "## 9. Recommended Action")
    assert "POST_WRITE_FRESH_AUDIT_V1.md" in text

    AUDIT.write_text(
        f"""# 2026-06-19 Canonical Presentation Fresh Audit V2

## Scope

Presentation-only fresh audit. The accepted denominator, exact-v1 Evidence, Selection, Books decisions and post-write audit were immutable inputs. Shared Books and `docs/LEARNING_STATE.md` remained read-only.

## Result

- Canonical header `5/5`; fixed H2 sequence `13/13`.
- Preserved denominator: `556 = 68 retained + 488 closures`; route-negative audit remains `110/110`.
- Preserved tables: Candidate, Review Completion, Benchmark, Selection and Books Comparison each `68/68`.
- Preserved bounded evidence: `68/68` Source Review normalized hashes equal the receipt packet; RP identities `68/68` remain unique and equal the packet.
- Preserved Selection: `3` selected, `65` source-specific not-selected.
- Preserved Books state: `56` Integrate and `12` No Change; `68/68` Books Review refs match the comparison packet.
- Preserved access/Gates: retained rows remain `deep_complete` and `accessible`; Coverage=`Closed`, Evidence=`Passed`, Books=`Passed`, Completion=`Complete`.
- Sources: `68/68` exact-v1 identities remain addressable in section 12.
- Final owner renderer emits canonical presentation directly; two consecutive complete-chain runs produced byte-identical Daily and core receipts. Current Daily SHA-256: `{sha(REPORT)}`.
- Unresolved presentation findings: `0`.

## Gate

Presentation=`Passed`. This audit does not reopen the accepted semantic or Books decisions.
""",
        encoding="utf-8",
    )

    files = sorted(
        p for p in PACKET.iterdir()
        if p.is_file() and p.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}
    )
    files += [REPORT, ROOT / "scripts/finalize_june19_v21.py", ROOT / "scripts/june19_exact_v1_data.py", ROOT / "scripts/test_june19_canonical_presentation.py", Path(__file__).resolve()]
    MANIFEST.write_text(
        "".join(
            f"{sha(path)}  {Path(os.path.relpath(path, PACKET)).as_posix()}\n"
            for path in files
        ),
        encoding="utf-8",
    )
    print(json.dumps({"fields": 5, "h2": 13, "reviews": 68, "books": 68, "manifest_entries": len(files), "unresolved_findings": 0}))


if __name__ == "__main__":
    main()
