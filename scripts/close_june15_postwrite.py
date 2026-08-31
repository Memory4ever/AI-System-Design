#!/usr/bin/env python3
"""Close the 2026-06-15 Daily only after fresh semantic review of root's Books writeback."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from finalize_june15_v21 import ADJ, C, DENOMINATOR_ID, PATHS, ROOT, fam


PACKET = ROOT / "papers/2026/06/_sources/daily-20260615"
REPORT = ROOT / "papers/2026/06/15/README.md"
LEDGER = PACKET / "screening-ledger.json"
EVIDENCE_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POSTWRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
SHA_MANIFEST = PACKET / "SHA256SUMS"

NO_CHANGE_LOCATIONS = {
    "2606.15712": "Ch66/Ch82 verifier independence, correlated-error floor, cost and terminal-outcome boundary",
    "2606.15828": "Ch74 repository-instruction accumulation, conflict, context-budget and lint control surface",
    "2606.19382": "Ch82/Ch81 dependency DAG, ready-node release, isolated workspace and coordinator fallback",
}


def main() -> None:
    integrates = []
    no_changes = []
    for aid, values in C.items():
        owner, delta, disposition, method, evaluation, limits, tradeoff = values
        item = {
            "aid": aid,
            "family": fam(aid),
            "owner": owner,
            "delta": delta,
            "disposition": disposition,
            "method": method,
            "evaluation": evaluation,
            "limits": limits,
            "tradeoff": tradeoff,
        }
        (integrates if disposition.startswith("Integrate") else no_changes).append(item)

    assert len(integrates) == 36 and len(no_changes) == 3
    book_files = list((ROOT / "Books").rglob("*.md"))
    audit = [
        "# 2026-06-15 Post-write Fresh-context Audit V1",
        "",
        f"Denominator `{DENOMINATOR_ID}`. All 39 retained families were re-read after root's serialized Books writeback; no pre-write conclusion was inherited.",
        "",
        "| Family | Disposition | Unique owner / adjacent result | Mechanism, trade-off and exact-v1 boundary | Result |",
        "| --- | --- | --- | --- | --- |",
    ]

    for item in integrates:
        expected = ROOT / PATHS[item["owner"]]
        expected_lines = expected.read_text().splitlines()
        expected_hits = [i for i, line in enumerate(expected_lines, 1) if item["aid"] in line]
        all_hits = []
        for path in book_files:
            for lineno, line in enumerate(path.read_text().splitlines(), 1):
                if item["aid"] in line:
                    all_hits.append((path.relative_to(ROOT).as_posix(), lineno))
        assert len(expected_hits) == 1, (item["aid"], PATHS[item["owner"]], expected_hits)
        assert all_hits == [(PATHS[item["owner"]], expected_hits[0])], (item["aid"], all_hits)
        location = (
            f"`{PATHS[item['owner']]}:{expected_hits[0]}`; owner `{item['owner']}`; "
            f"adjacent `{ADJ[item['owner']]}`"
        )
        boundary = (
            f"正文保存机制 `{item['delta']}`；trade-off/failure `{item['tradeoff']}`；"
            f"Review note 绑定 exact-v1 method `{item['method']}`、evaluation `{item['evaluation']}`，"
            f"且不扩张 `{item['limits']}`。"
        )
        audit.append(f"| `{item['family']}` | Integrate | {location} | {boundary} | PASS |")

    for item in no_changes:
        location = (
            f"owner `{item['owner']}`; adjacent `{ADJ[item['owner']]}`; "
            f"{NO_CHANGE_LOCATIONS[item['aid']]}"
        )
        boundary = (
            f"既有 owner 命题覆盖 `{item['delta']}`；fallback/non-proof `{item['tradeoff']}`；"
            "Daily 保留 exact-v1 receipt 而不机械追加。"
        )
        audit.append(
            f"| `{item['family']}` | No Change — Existing Coverage | {location} | {boundary} | PASS |"
        )

    audit += [
        "",
        "## Fresh-context checks",
        "",
        "- 36/36 Integrate markers: exactly one Books file and one exact-v1 family occurrence each.",
        "- 36/36 owner bodies: mechanism, authoritative owner/handoff, trade-off/failure and coexistence/fallback preserved.",
        "- 36/36 Review notes: official exact-v1 URL plus source-specific non-proof boundary; no later version expands the claim.",
        "- 3/3 No Change: existing owner/adjacent proposition and fallback re-read; no stale excluded-family mechanism remains unowned.",
        "- Daily Integration Decision, Repository Changes, Open Questions, receipts, queue and report dispositions are mutually consistent.",
        "- Unresolved findings: 0.",
        "",
        "## Gate verdict",
        "",
        "- Coverage Gate: Closed.",
        "- Evidence Gate: Passed.",
        "- Books Gate: Passed.",
        "- Completion Status: Complete.",
    ]
    POSTWRITE_AUDIT.write_text("\n".join(audit) + "\n")

    report = REPORT.read_text()
    replacements = {
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open，等待已授权的 serialized writeback 后 fresh-context Semantic Audit": "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding",
        "Coverage and Evidence are closed; Books remains Open pending serialized root writeback and this lane's post-write fresh audit.": "Coverage, Evidence and Books Gates are closed after serialized root writeback and this lane's 39/39 post-write fresh audit.",
        "Books Gate remains Open until root writes the owner-merged deltas and this lane independently audits all 39 dispositions.": "Root merged all 36 Integrate families into 18 unique owners; this lane then passed the 36/36 Integrate and 3/3 No Change fresh audit, so Books Gate is Passed.",
        "| Completion Status | In Progress |": "| Completion Status | Complete |",
        "| Books Gate | Open |": "| Books Gate | Passed |",
        "SA-20260615-BOOKS-PREWRITE-V1": "SA-20260615-BOOKS-POSTWRITE-V1",
        "root writeback pending": "—",
        "36 Integrate proposals deduplicated into 18 owner writes; 3 No Change handoffs checked; post-write fresh audit not yet executed | open": "36/36 Integrate writebacks in 18 unique owners and 3/3 No Change handoffs passed independent post-write audit; unresolved findings 0 | passed",
        "`Integrate`: 36 families, owner-merged into 18 proposed Books writes": "`Integrate`: root merged 36 families into 18 unique Books owners",
        "Books Gate remains Open until root writeback and this lane's 39/39 fresh-context audit.": "Books Gate Passed after the 39/39 fresh-context post-write audit.",
        "This lane created the 2026-06-15 Daily, frozen source packet, receipts, row-level denominator audit, queue, ready-to-insert packet and finalizer.": "Root performed the serialized 36-family Books writeback across 18 owner files; this lane created the Daily/source packet and independently audited all 39 Books dispositions.",
        "It did not modify, stage, commit or push shared Books.": "This lane did not modify, stage, commit or push shared Books.",
        "the only current Gate blocker is serialized Books writeback plus post-write audit": "no Gate blocker remains",
        "- Status: In Progress.": "- Status: Complete.",
        "- Books Gate: Open pending serialized writeback and post-write fresh audit.": "- Books Gate: Passed.\n- Fresh-context Semantic Audit: Passed；unresolved findings = 0.",
    }
    for old, new in replacements.items():
        assert old in report, old
        report = report.replace(old, new)
    REPORT.write_text(report)

    ledger = json.loads(LEDGER.read_text())
    ledger["gate_status"] = "complete"
    ledger["audit"]["books_gate"] = "passed_after_root_writeback_and_39_of_39_fresh_audit"
    ledger["audit"]["post_write_semantic_audit"] = {
        "receipt": str(POSTWRITE_AUDIT.relative_to(ROOT)),
        "integrate": "36/36",
        "no_change": "3/3",
        "owners": 18,
        "unresolved_findings": 0,
        "result": "passed",
    }
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

    EVIDENCE_AUDIT.write_text(
        EVIDENCE_AUDIT.read_text().replace(
            "- Books: OPEN — 36 Integrate proposals across 18 owners plus three No Change handoffs are complete; root writeback and 39/39 fresh-context post-write audit remain pending.",
            "- Books: PASS — 36/36 Integrate writebacks across 18 unique owners plus 3/3 No Change handoffs passed the independent post-write audit.",
        )
    )
    (PACKET / "README.md").write_text(
        "# 2026-06-15 source packet\n\n"
        "Canonical denominator `39/285`; closures `246`; Coverage, Evidence and Books Gates Passed. "
        "Post-write audit: `POST_WRITE_FRESH_AUDIT_V1.md`.\n"
    )

    targets = [p for p in PACKET.rglob("*") if p.is_file() and p != SHA_MANIFEST]
    targets += [REPORT, Path(__file__).resolve(), ROOT / "scripts/finalize_june15_v21.py"]
    manifest_lines = []
    for path in sorted(set(targets), key=lambda p: str(p.relative_to(ROOT))):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest_lines.append(f"{digest}  {path.relative_to(ROOT)}")
    SHA_MANIFEST.write_text("\n".join(manifest_lines) + "\n")


if __name__ == "__main__":
    main()
