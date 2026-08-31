#!/usr/bin/env python3
"""Fresh semantic/presentation audit and manifest finalizer for 2026-06-25."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260625"
REPORT = ROOT / "papers/2026/06/25/README.md"
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
BENCHMARK_FIELDS = (
    "workload", "model", "hardware", "precision", "input_length",
    "output_length", "batch", "concurrency", "slo", "evaluator",
)


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
    assert top["Research Date"] == "2026-06-25"
    assert top["Timezone"] == "Asia/Shanghai"
    assert top["Strict Window"].startswith("2026-06-24 09:00:00 ～ 2026-06-25 09:00:00")
    assert top["Contract"].startswith("V2.1") and top["Status"].startswith("Complete")
    assert [line for line in text.splitlines() if line.startswith("## ")] == EXPECTED_H2

    ledger = json.loads((PACKET / "screening-ledger.json").read_text(encoding="utf-8"))
    audit_rows = list(csv.DictReader(
        (PACKET / "denominator-full-semantic-audit-v1.tsv").open(encoding="utf-8"), delimiter="\t"
    ))
    assert len(ledger["identities"]) == len(audit_rows) == 510
    assert Counter(row["route"] for row in audit_rows) == {
        "core_daily_semantic_review_required": 321,
        "keyword_daily_semantic_review_required": 62,
        "not_routed_by_keyword_contract": 127,
    }
    assert Counter(row["decision"] for row in audit_rows) == {
        "retained": 68, "closed_pre_denominator": 442,
    }
    assert all(row["family_specific_reason"].strip() and row["title"] in row["family_specific_reason"] for row in audit_rows)
    assert ledger["route_negative_audited"] == 127
    assert len(ledger["route_negative_false_negatives"]) == 4

    receipt_packet = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text(encoding="utf-8"))
    access_packet = json.loads((PACKET / "exact-v1-access-receipt.json").read_text(encoding="utf-8"))
    selection_packet = json.loads((PACKET / "deep-analysis-selection-v1.json").read_text(encoding="utf-8"))
    comparison_packet = json.loads((PACKET / "books-comparison-v1.json").read_text(encoding="utf-8"))
    post_rows = list(csv.DictReader(
        (PACKET / "post-write-fresh-audit-v1.tsv").open(encoding="utf-8"), delimiter="\t"
    ))
    receipt_items = receipt_packet["items"]
    retained = {row["source_family_id"] for row in audit_rows if row["decision"] == "retained"}
    sets = [
        {item["source_family_id"] for item in receipt_items},
        {item["source_family_id"] for item in access_packet["items"]},
        {item["source_family_id"] for item in selection_packet["decisions"]},
        {item["source_family_id"] for item in comparison_packet["items"]},
        {item["source_family_id"] for item in post_rows},
    ]
    assert len(retained) == 68 and all(current == retained for current in sets)
    assert access_packet["result"] == "68/68 exact-v1 identities resolved" and not access_packet["blocked"]
    for item in receipt_items:
        aid = item["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
        for locator in (item["method_locator"], item["evaluation_locator"], item["limitation_locator"]):
            assert aid in locator and "#abstract-text=" not in locator
        benchmark = item["benchmark_contract"]
        assert tuple(benchmark) == BENCHMARK_FIELDS
        assert all(value and (value == "Not Disclosed" or not value.startswith("Not Disclosed")) for value in benchmark.values())
        score = item["score_v2"]
        assert score["total"] == score["design_delta"] + score["system_reach"] + score["durability"]
        assert item["completion_result"] == "complete" and item["ordinary_pending_locator_count"] == 0
    assert len({item["review_provenance_id"] for item in receipt_items}) == 68
    assert Counter(item["decision"] for item in selection_packet["decisions"]) == {"selected": 3, "not_selected": 65}
    assert Counter(item["decision"] for item in comparison_packet["items"]) == {
        "Integrate": 63, "No Change — Existing Coverage": 5,
    }
    assert len({item["target_chapter_ref"].split("#", 1)[0] for item in comparison_packet["items"] if item["decision"] == "Integrate"}) == 25
    assert Counter(item["audit_result"] for item in post_rows) == {
        "passed_integrated_unique_owner_body_and_review_note": 63,
        "passed_no_change_absent_existing_owner_handoff_revalidated": 5,
    }

    candidate = rows(section(text, "## 2. Candidate Ledger", "## 3. Review Completion Receipt"))
    receipt = rows(section(text, "## 3. Review Completion Receipt", "## 4. Benchmark Contracts"))
    benchmark = rows(section(text, "## 4. Benchmark Contracts", "## 5. Deep Analysis Selection"))
    selection = rows(section(text, "## 5. Deep Analysis Selection", "## 6. Books Comparison"))
    books = rows(section(text, "## 6. Books Comparison", "## 7. Semantic Audit"))
    assert (len(candidate), len(receipt), len(benchmark), len(selection), len(books)) == (68, 68, 68, 68, 68)
    assert all(row[10:13] == ["retained", "deep_complete", "accessible"] for row in candidate)
    assert Counter(row[19] for row in candidate) == {"Integrate": 63, "No Change — Existing Coverage": 5}
    assert Counter(row[2] for row in selection) == {"selected": 3, "not_selected": 65}
    review_blocks = marker_bodies(text, "review:")
    books_blocks = marker_bodies(text, "books-review:")
    assert len(review_blocks) == len(books_blocks) == 68
    for item in receipt_items:
        assert hashlib.sha256(norm(review_blocks[item["review_ref"]]).encode()).hexdigest() == item["review_body_sha256"]
    assert {row[1] for row in receipt} == {item["review_provenance_id"] for item in receipt_items}
    assert {row[-1] for row in books} == {item["books_review_ref"] for item in comparison_packet["items"]}
    assert len(re.findall(r"https://arxiv\.org/abs/\d{4}\.\d{5}v1", section(text, "## 12. Sources", "## 13. Final Status"))) == 68
    assert text.count("| passed |") >= 4 and "POST_WRITE_FRESH_AUDIT_V1.md" in text

    AUDIT.write_text(
        f"""# 2026-06-25 Canonical V2.1 Fresh Audit V2

## Scope

Fresh audit covered the complete date-local chain: raw screening conservation, frozen denominator and closures, retained exact-v1 receipts, Score V2, full-frontier Selection, Books disposition/post-write conservation, and canonical presentation. Shared Books, `docs/LEARNING_STATE.md`, and monthly indexes were read-only.

## Result

- Coverage: `510/510` identities; routes `321 Core + 62 keyword + 127 route-negative`; denominator `68 retained + 442 family-specific closures`; route-negative audit `127/127`, four promoted false negatives.
- Evidence/Access: `68/68` exact-v1 identities, complete source-specific Method/Evaluation/limitation locators, artifacts, ten-field benchmark contracts, valid Score V2 totals, and `68/68` unique RP identities.
- Selection: full `68/68` frontier; `3` selected and `65` bounded non-selections.
- Books: `63` Integrate across `25` unique owners and `5` No Change; post-write fresh audit `68/68` with zero unresolved findings.
- Canonical header `5/5`; fixed H2 sequence `13/13`; Candidate, Review Completion, Benchmark, Selection and Books Comparison tables each `68/68`.
- Bounded Source Reviews: `68/68` normalized hashes equal the receipt packet; `68/68` exact-v1 identities remain addressable in Sources.
- Gates: Coverage=`Closed`, Evidence=`Passed`, Books=`Passed`, Completion=`Complete`.
- Final owner renderer emits canonical presentation directly. Current Daily SHA-256: `{sha(REPORT)}`.
- Unresolved findings: `0`.

## Gate

Fresh Audit=`Passed`.
""",
        encoding="utf-8",
    )

    files = sorted(
        path for path in PACKET.iterdir()
        if path.is_file() and path.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}
    )
    files += [
        REPORT,
        ROOT / "scripts/finalize_june25_v21.py",
        ROOT / "scripts/test_june25_canonical_presentation.py",
        Path(__file__).resolve(),
    ]
    MANIFEST.write_text(
        "".join(
            f"{sha(path)}  {Path(os.path.relpath(path, PACKET)).as_posix()}\n"
            for path in files
        ),
        encoding="utf-8",
    )
    print(json.dumps({
        "raw": 510, "retained": 68, "closures": 442,
        "fields": 5, "h2": 13, "reviews": 68, "books": 68,
        "manifest_entries": len(files), "unresolved_findings": 0,
    }))


if __name__ == "__main__":
    main()
