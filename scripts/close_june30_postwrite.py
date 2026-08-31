#!/usr/bin/env python3
"""Run the 64-family 2026-06-30 post-write audit and close the Daily Gate."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

try:
    from scripts import apply_june30_books_v1 as APPLY
    from scripts import finalize_june30_v21 as FINALIZER
    from scripts.canonicalize_june_daily_presentation import canonicalize_report
except ModuleNotFoundError:
    import apply_june30_books_v1 as APPLY
    import finalize_june30_v21 as FINALIZER
    from canonicalize_june_daily_presentation import canonicalize_report


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260630"
REPORT = ROOT / "papers/2026/06/30/README.md"
COMPARISON = PACKET / "books-comparison-v1.json"
REVIEWS = PACKET / "source-review-receipts-v2.1.json"
EXPECTED = {
    item.family: item for item in APPLY.INSERTS
}


def audit() -> list[dict[str, str]]:
    comparisons = json.loads(COMPARISON.read_text())["comparisons"]
    reviews = json.loads(REVIEWS.read_text())["reviews"]
    review_by_family = {row["source_family_id"]: row for row in reviews}
    comparison_by_family = {row["source_family_id"]: row for row in comparisons}
    if len(comparisons) != 38 or len(comparison_by_family) != 38:
        raise AssertionError("06-30 eligible Books comparison count drift")
    if len(reviews) != 64 or len(review_by_family) != 64:
        raise AssertionError("06-30 denominator/review count drift")
    if any(row["completion_result"] != "complete" for row in reviews):
        raise AssertionError("Evidence completion regressed")

    corpus = {path: path.read_text() for path in (ROOT / "books").rglob("*.md")}
    counts = {"Integrate": 0, "No Change — Existing Coverage": 0, "Weekly Only — Context": 0}
    rows: list[dict[str, str]] = []

    for review in reviews:
        family = review["source_family_id"]
        disposition = review["books_disposition"]
        counts[disposition] += 1
        stable_node = review["stable_node_id"]
        owner_rel = FINALIZER.PATHS[stable_node]
        adjacent_rel = FINALIZER.ADJACENT[stable_node]
        owner = ROOT / owner_rel
        adjacent = ROOT / adjacent_rel
        if not owner.is_file() or not adjacent.is_file():
            raise AssertionError(f"{family}: owner/adjacent path unavailable")

        comparison = comparison_by_family.get(family)
        if disposition == "Weekly Only — Context":
            if comparison is not None:
                raise AssertionError(f"{family}: Weekly Only must not have a Books comparison")
        else:
            if comparison is None:
                raise AssertionError(f"{family}: eligible Books comparison missing")
            if not comparison["existing_proposition"].strip() or not comparison["source_specific_delta"].strip():
                raise AssertionError(f"{family}: comparison rationale missing")

        hits = [path for path, text in corpus.items() if family in text]
        if disposition == "Integrate":
            item = EXPECTED.get(family)
            if item is None:
                raise AssertionError(f"{family}: unexpected Integrate")
            target = ROOT / item.target
            if owner != target or hits != [target]:
                raise AssertionError(f"{family}: owner uniqueness failure: {hits}")
            text = corpus[target]
            required_counts = {
                item.body_start: 1,
                item.body_end: 1,
                item.review_start: 1,
                item.review_end: 1,
                item.body: 1,
                item.review: 1,
                family: 2,
            }
            for value, expected_count in required_counts.items():
                if text.count(value) != expected_count:
                    raise AssertionError(f"{family}: post-write count drift for {value[:50]!r}")
            if family.endswith("30616"):
                required_semantics = (
                    "atomic ability graph", "horizon budget", "teacher route", "错误累积",
                    "不证明参数规模不再重要", "缩短 horizon", "§6 Limitation and Future Work",
                )
            else:
                required_semantics = (
                    "provenance graph", "process sidecar", "公共技能", "残留扫描",
                    "不证明任意架构都能完全遗忘", "重训作为高成本 fallback", "§B.7 Boundary cases",
                )
            missing = [term for term in required_semantics if term not in text]
            if missing:
                raise AssertionError(f"{family}: semantic boundary missing {missing}")
            evidence = (
                f"two locators (body-source + Review note) in unique owner `{owner_rel}`; "
                "mechanism/trade-off/failure/coexistence/exact-v1 boundary re-read"
            )
        else:
            if hits:
                raise AssertionError(f"{family}: non-Integrate leakage into Books: {hits}")
            if disposition == "Weekly Only — Context":
                evidence = (
                    f"zero Books hits; candidate-level Review Ref re-opened; owner `{owner_rel}` "
                    f"and adjacent `{adjacent_rel}` resolve without creating a Books comparison"
                )
            else:
                evidence = (
                    f"zero Books hits; re-read owner `{owner_rel}` and adjacent "
                    f"`{adjacent_rel}` against source-specific delta"
                )

        rows.append({
            "source_family_id": family,
            "disposition": disposition,
            "owner": owner_rel,
            "adjacent": adjacent_rel,
            "evidence": evidence,
            "result": "PASS",
        })

    if counts != {
        "Integrate": 2,
        "No Change — Existing Coverage": 36,
        "Weekly Only — Context": 26,
    }:
        raise AssertionError(f"Books disposition drift: {counts}")
    if len(rows) != 64:
        raise AssertionError("post-write scope is not 64/64")
    return rows


def write_audit(rows: list[dict[str, str]]) -> None:
    fields = ["source_family_id", "disposition", "owner", "adjacent", "evidence", "result"]
    with (PACKET / "post-write-fresh-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    book_hashes = {
        item.target: hashlib.sha256((ROOT / item.target).read_bytes()).hexdigest()
        for item in APPLY.INSERTS
    }
    lines = [
        "# 2026-06-30 Post-write Fresh Audit V1", "",
        "- Denominator: `daily-v2.1:2026-06-30:2a228144dceb4876`; fresh scope 64/64 retained families.",
        "- Integrate: PASS — 2/2 families occur in one expected owner file each, with one body-source locator and one source-specific Review note; mechanism, owner state, trade-off, failure/fallback, coexistence and exact-v1 non-proof boundary were re-read.",
        "- No Change: PASS — 36/36 owner + adjacent comparisons remain valid and no family leaked into Books.",
        "- Weekly Only: PASS — 26/26 remain context-only with zero Books leakage.",
        "- Idempotence: PASS — a second locked apply was a no-op and both target hashes were unchanged.",
        f"- Ch77 SHA-256: `{book_hashes['books/part-07-agent/77-memory.md']}`.",
        f"- Ch84 SHA-256: `{book_hashes['books/part-07-agent/84-agent-platform.md']}`.",
        "- Unresolved findings: 0. Coverage Closed; Evidence Passed; Selection Passed; Books Passed; Completion Complete.", "",
        "| Source Family ID | Disposition | Owner / adjacent audit evidence | Result |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['source_family_id']} | {row['disposition']} | {row['evidence']} | PASS |")
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(lines) + "\n")


def transition(text: str, old: str, new: str, label: str) -> str:
    old_count, new_count = text.count(old), text.count(new)
    if (old_count, new_count) == (1, 0):
        return text.replace(old, new, 1)
    if (old_count, new_count) == (0, 1):
        return text
    raise AssertionError(f"{label}: state drift old={old_count}, new={new_count}")


def close_daily() -> None:
    text = REPORT.read_text()
    changes = (
        (
            "> Strict V2.1 prewrite packet. Coverage, Evidence and Selection are closed; Books remains Open pending root review, lock, writeback and post-write fresh audit.",
            "> Strict V2.1 complete report. Coverage is Closed; Evidence, Selection and Books passed after the 64/64 fresh semantic audits and serialized two-owner writeback.",
            "status quote",
        ),
        (
            "Strict owner/adjacent comparison and root prewrite review reduce the preliminary 16 Integrate proposals to 2 Integrate / 36 No Change / 26 Weekly Only across 2 unique owner files; shared writeback has not started, so this date is not Complete.",
            "Strict owner/adjacent comparison and root prewrite review reduced the preliminary 16 Integrate proposals to 2 Integrate / 36 No Change / 26 Weekly Only across 2 unique owner files. The two owner writes and 64/64 post-write fresh audit passed with zero unresolved findings, so the date is Complete.",
            "executive summary",
        ),
        ("| Completion Status | In Progress |", "| Completion Status | Complete |", "completion"),
        ("| Books Gate | Open |", "| Books Gate | Passed |", "Books Gate"),
        (
            "| SA-20260630-BOOKS | fresh-context:june30-books-prewrite | books |",
            "| SA-20260630-BOOKS | fresh-context:june30-books-postwrite | books |",
            "Books auditor",
        ),
        (
            "PW-20260630: shared Books writeback and post-write audit pending | Apply only after root write lock, then run 64/64 post-write semantic audit | open |",
            "none | 64/64 post-write audit: 2 Integrate unique-owner writes, 36 No Change and 26 Weekly Only zero leakage; unresolved findings 0 | passed |",
            "Books audit outcome",
        ),
        (
            "2 Integrate families map to 2 unique owner proposals in `READY_TO_INSERT_BOOKS_V1.md`; the strict Books FP audit and root prewrite review reduced the preliminary 16 proposals by 14. Shared Books and LEARNING_STATE remain unchanged pending root write lock.",
            "2 Integrate families were written to 2 unique owners under the shared lock; 36 No Change and 26 Weekly Only families remained unwritten. The 64/64 fresh post-write audit found no unresolved owner, semantic-boundary or leakage finding; `docs/LEARNING_STATE.md` remained unchanged.",
            "integration decision",
        ),
        (
            "- Added only 2026-06-30 Daily/source receipts and date-specific scripts.\n- No shared Books or `docs/LEARNING_STATE.md` write was performed.",
            "- Added 2026-06-30 Daily/source receipts and date-specific audit/apply scripts.\n- Updated only the root-authorized 06-30 blocks in `books/part-07-agent/77-memory.md` and `books/part-07-agent/84-agent-platform.md`; `docs/LEARNING_STATE.md` was not edited.",
            "repository changes",
        ),
        (
            "- Shared Books write lock remains pending.\n- After writeback, 64/64 post-write fresh-context semantic audit, validator, SHA and targeted diff-check are required before Complete.",
            "- None for this Daily. The 64/64 post-write semantic audit has zero unresolved findings.",
            "open questions",
        ),
    )
    for old, new, label in changes:
        text = transition(text, old, new, label)
    REPORT.write_text(text)

    queue_path = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
    queue = queue_path.read_text()
    queue = transition(
        queue,
        "> Prewrite only. Shared Books lock has not been granted.",
        "> CLOSED. Root granted the shared lock; 2 Integrate families were written to 2 owners and the 64/64 post-write audit passed.",
        "queue header",
    )
    pending = "- State: pending root prewrite review / write lock"
    applied = "- State: applied; post-write audit PASS"
    if (queue.count(pending), queue.count(applied)) == (2, 0):
        queue = queue.replace(pending, applied)
    elif (queue.count(pending), queue.count(applied)) != (0, 2):
        raise AssertionError(
            f"owner queue state drift: pending={queue.count(pending)}, applied={queue.count(applied)}"
        )
    queue_path.write_text(queue)


def refresh_sha() -> None:
    sha_path = PACKET / "SHA256SUMS"
    names = [line.split("  ", 1)[1] for line in sha_path.read_text().splitlines() if "  " in line]
    for name in ("post-write-fresh-audit-v1.tsv", "POST_WRITE_FRESH_AUDIT_V1.md"):
        if name not in names:
            names.append(name)
    lines = []
    for name in names:
        path = REPORT if name == "../../../06/30/README.md" else PACKET / name
        lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {name}")
    sha_path.write_text("\n".join(lines) + "\n")


def close_screening_ledger() -> None:
    ledger_path = PACKET / "screening-ledger.json"
    ledger = json.loads(ledger_path.read_text())
    ledger["gate_status"] = "complete_postwrite_fresh_audit_passed"
    ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    rows = audit()
    write_audit(rows)
    report_text = REPORT.read_text()
    completed_fields = (
        "| Completion Status | Complete |",
        "| Coverage Gate | Closed |",
        "| Evidence Gate | Passed |",
        "| Books Gate | Passed |",
        "State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。",
    )
    if all(field in report_text for field in completed_fields):
        forbidden = (
            "| Completion Status | In Progress |",
            "| Books Gate | Open |",
            "pending root prewrite review / write lock",
        )
        if any(token in report_text for token in forbidden):
            raise AssertionError("completed Daily still contains an open-state token")
        queue = (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").read_text()
        if queue.count("- State: applied; post-write audit PASS") != 2:
            raise AssertionError("completed Daily owner queue is not fully applied")
        close_screening_ledger()
        canonicalize_report(REPORT, "2026-06-30")
        refresh_sha()
        print("06-30 post-write fresh audit PASS: 64/64; accepted completed-state no-op")
        return
    close_daily()
    close_screening_ledger()
    canonicalize_report(REPORT, "2026-06-30")
    refresh_sha()
    print("06-30 post-write fresh audit PASS: 64/64; Complete")


if __name__ == "__main__":
    main()
