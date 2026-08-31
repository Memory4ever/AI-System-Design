#!/usr/bin/env python3
"""Audit all 65 June-28 Books dispositions and close the Daily after writeback."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

try:
    from scripts import apply_june28_books as APPLY
    from scripts import finalize_june28_downstream_v21 as FINALIZER
    from scripts.canonicalize_june_daily_presentation import canonicalize_report
except ModuleNotFoundError:
    import apply_june28_books as APPLY
    import finalize_june28_downstream_v21 as FINALIZER
    from canonicalize_june_daily_presentation import canonicalize_report


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260628"
REPORT = ROOT / "papers/2026/06/28/README.md"
FRESH_AUDIT = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
POST_WRITE_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
PRESENTATION_AUDIT = PACKET / "CANONICAL_PRESENTATION_AUDIT_V1.md"
SHA256SUMS = PACKET / "SHA256SUMS"

EXPECTED_H2 = [
    "## Executive Summary",
    "## 1. Coverage",
    "## 2. Candidate Ledger",
    "## 3. Review Completion Receipt",
    "## 4. Benchmark Contracts",
    "## 5. Deep Analysis Selection",
    "## 6. Books Comparison",
    "## 7. Semantic Audit",
    "## 8. Ignored Noise",
    "## 9. Recommended Action",
    "## 10. Repository Changes",
    "## 11. Open Questions",
    "## 12. Sources",
    "## 13. Final Status",
]

VALIDATOR_MARKERS = [
    "report-metadata-v2",
    "source-coverage-v2",
    "candidate-ledger-v2.1",
    "review-completion-v1",
    "benchmark-contract-v1",
    "deep-analysis-selection-v1",
    "books-comparison-v1",
    "semantic-audit-v1",
]


def _validator_table(text: str, marker: str) -> str:
    token = f"<!-- validator:{marker} -->"
    begin = text.index(token)
    finish = text.find("\n\n", begin)
    return text[begin:] if finish < 0 else text[begin:finish]


def protected_report_fragments(text: str) -> dict[str, str]:
    protected = {
        f"table:{marker}": _validator_table(text, marker)
        for marker in VALIDATOR_MARKERS
    }
    pattern = re.compile(
        r"<!-- (coverage|review|claim|analysis|analysis-decision|existing|delta|books-review):(.*?):start -->"
    )
    for match in pattern.finditer(text):
        kind, identity = match.groups()
        marker = f"{kind}:{identity}"
        end_token = f"<!-- {marker}:end -->"
        end = text.index(end_token, match.end()) + len(end_token)
        key = f"block:{marker}"
        if key in protected:
            raise AssertionError(f"duplicate protected marker: {key}")
        protected[key] = text[match.start():end]
    return protected


def semantic_packet_hashes() -> dict[str, str]:
    excluded = {PRESENTATION_AUDIT, SHA256SUMS}
    return {
        path.relative_to(PACKET).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(PACKET.rglob("*"))
        if path.is_file() and path not in excluded
    }


def _collection_hash(items: dict[str, str]) -> str:
    payload = "".join(f"{key}\0{items[key]}\0" for key in sorted(items))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _report_collections(protected: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    reviews = {
        key: value for key, value in protected.items()
        if key.startswith("block:review:")
    }
    books = {
        key: value for key, value in protected.items()
        if key.startswith(("block:existing:", "block:delta:", "block:books-review:"))
        or key == "table:books-comparison-v1"
    }
    return reviews, books


def assert_canonical_presentation(text: str) -> None:
    headings = re.findall(r"(?m)^## .+$", text)
    assert headings == EXPECTED_H2
    assert text.count("### Source Reviews") == 1
    assert "**Source Reviews**" not in text
    for field in ("Research Date", "Timezone", "Strict Window", "Contract", "Status"):
        assert text.count(f"**{field}:**") == 1, field
    assert "**Status:** Complete" in text
    assert "| Completion Status | Complete |" in text
    assert "| Coverage Gate | Closed |" in text
    assert "| Evidence Gate | Passed |" in text
    assert "| Books Gate | Passed |" in text
    assert "SA-20260628-BOOKS-POSTWRITE-V1" in text
    assert "unresolved findings 0 | passed |" in text
    protected = protected_report_fragments(text)
    reviews, books = _report_collections(protected)
    assert len(protected) == 346
    assert len(reviews) == 65
    assert len(books) == 145
    assert len(set(re.findall(r"RP-[0-9a-f]{16}", text))) == 65

    access = json.loads((PACKET / "exact-v1-access-receipt.json").read_text())
    receipts = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())
    selection = json.loads((PACKET / "deep-analysis-selection-v1.json").read_text())
    assert len(access) == len(receipts) == len(selection) == 65
    assert sum(row["access_status"] == "accessible" for row in access) == 65
    assert sum(row["completion_result"] == "complete" for row in receipts) == 65
    assert sum(row["decision"] == "selected" for row in selection) == 3
    dispositions = {
        name: sum(row["books_disposition"] == name for row in receipts)
        for name in ("Integrate", "No Change — Existing Coverage", "Weekly Only — Context")
    }
    assert dispositions == {
        "Integrate": 6,
        "No Change — Existing Coverage": 42,
        "Weekly Only — Context": 17,
    }
    post = POST_WRITE_AUDIT.read_text(encoding="utf-8")
    assert len(re.findall(r"(?m)^\| SF-2026-ARXIV-", post)) == 65
    assert "Unresolved findings: 0" in post


def write_presentation_audit(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    reviews, books = _report_collections(protected)
    audit = f"""# 2026-06-28 Canonical Presentation Audit V1

- Scope: accepted-state reader-facing and renderer audit only; frozen denominator, Evidence, Selection and Books semantics were not re-evaluated.
- Canonical presentation: top five fields present; `Executive Summary` plus the exact numbered §§1–13 H2 sequence passed.
- Denominator and access: `211 = 65 retained + 146 closures`; `65/65` exact-v1 accessible; pending `0`.
- Protected report fragments: `{len(protected)}`; combined SHA256 `{_collection_hash(protected)}`.
- Bounded Reviews: `65/65`; combined SHA256 `{_collection_hash(reviews)}`.
- Review Provenance IDs: `65/65`; the protected Review Completion table remains byte-identical.
- Books table and bounded blocks: `{len(books)}` fragments; combined SHA256 `{_collection_hash(books)}`.
- Books dispositions and fresh audit: `6 Integrate / 42 No Change / 17 Weekly Only`; post-write `65/65`; unresolved findings `0`.
- Semantic packet inputs: `{len(packet_hashes)}` files sealed; combined SHA256 `{_collection_hash(packet_hashes)}`.
- Reader-facing Daily SHA256: `{hashlib.sha256(report.encode('utf-8')).hexdigest()}`.
- Final owner renderer: PASS — accepted state exits before Books access or semantic regeneration; protected-byte drift, packet drift, missing audits, wrong Gate state, duplicate markers or H2 drift fails closed.
- Semantic handoff: `FRESH_EVIDENCE_SELECTION_AUDIT_V1.md` and `POST_WRITE_FRESH_AUDIT_V1.md` remain the accepted fresh-context audits; validator success is not substituted for semantic truth.
- Cross-model skipped: non-interactive child-lane context; no independent second-model claim is made.
- Findings: none unresolved.
"""
    PRESENTATION_AUDIT.write_text(audit, encoding="utf-8")


def assert_prior_presentation_seal(
    protected: dict[str, str], packet_hashes: dict[str, str], report: str
) -> None:
    if not PRESENTATION_AUDIT.is_file():
        return
    prior = PRESENTATION_AUDIT.read_text(encoding="utf-8")
    reviews, books = _report_collections(protected)
    expected = {
        "Protected report fragments": _collection_hash(protected),
        "Bounded Reviews": _collection_hash(reviews),
        "Books table and bounded blocks": _collection_hash(books),
        "Semantic packet inputs": _collection_hash(packet_hashes),
        "Reader-facing Daily SHA256": hashlib.sha256(report.encode("utf-8")).hexdigest(),
    }
    for label, actual in expected.items():
        match = re.search(rf"^- {re.escape(label)}.*?`([0-9a-f]{{64}})`", prior, re.M)
        assert match and match.group(1) == actual, f"prior presentation seal drift: {label}"


def refresh_canonical_hashes() -> None:
    targets = sorted(
        path for path in PACKET.rglob("*") if path.is_file() and path != SHA256SUMS
    )
    targets.append(REPORT)
    rows = [
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}"
        for path in sorted(targets)
    ]
    SHA256SUMS.write_text("\n".join(rows) + "\n", encoding="utf-8")


def finalize_accepted_presentation() -> bool:
    required = (REPORT, FRESH_AUDIT, POST_WRITE_AUDIT)
    if not all(path.is_file() for path in required):
        return False
    before_report = REPORT.read_text(encoding="utf-8")
    # A stale POST_WRITE_FRESH_AUDIT file can survive an interrupted recovery
    # while the Daily itself is still in the pre-write state.  In that case the
    # prior presentation seal describes an older rendering and must not bypass
    # the real Books audit/close transition below.  Only an already accepted
    # report may take this presentation-only idempotent path.
    if (
        "| Completion Status | Complete |" not in before_report
        or "| Books Gate | Passed |" not in before_report
    ):
        return False
    protected = protected_report_fragments(before_report)
    packet_hashes = semantic_packet_hashes()
    try:
        assert_prior_presentation_seal(protected, packet_hashes, before_report)
    except AssertionError:
        # Recovery may repair an exact-v1 identity/problem narrative after an
        # older accepted-looking presentation seal was generated.  Never
        # accept that drift on hashes alone: re-run the full 65-family Books
        # audit and canonical invariant suite against the current files before
        # replacing the stale presentation-only seal.
        rows = audit_books()
        assert len(rows) == 65
        assert_canonical_presentation(before_report)
        write_presentation_audit(protected, packet_hashes, before_report)
        refresh_canonical_hashes()
        print(json.dumps({
            "mode": "accepted-presentation-resealed-after-full-audit",
            "families": "65/65",
            "unresolved_findings": 0,
        }, ensure_ascii=False))
        return True
    report = before_report
    if "**Source Reviews**" in report:
        assert report.count("**Source Reviews**") == 1
        assert "### Source Reviews" not in report
        report = report.replace("**Source Reviews**", "### Source Reviews", 1)
    assert protected_report_fragments(report) == protected
    assert semantic_packet_hashes() == packet_hashes
    assert_canonical_presentation(report)
    REPORT.write_text(report, encoding="utf-8")
    write_presentation_audit(protected, packet_hashes, report)
    refresh_canonical_hashes()
    print(json.dumps({
        "mode": "accepted-presentation-only",
        "raw": 211,
        "retained": 65,
        "closures": 146,
        "access": "65/65",
        "books": "6/42/17",
        "canonical_numbered_sections": 13,
        "total_h2": len(EXPECTED_H2),
    }, ensure_ascii=False))
    return True


def audit_books(root: Path = ROOT) -> list[dict[str, str]]:
    items, payload = FINALIZER.make_items()
    assert payload["denominator_id"] == FINALIZER.DENOMINATOR
    assert payload["registered_window_identities"] == 211
    assert len(items) == 65
    comparisons = {row["source_family_id"]: row for row in FINALIZER.build_comparisons(items)}
    ready_blocks = {block["owner"]: block for block in APPLY.parse_blocks()}
    corpus = {path: path.read_text() for path in (root / "books").rglob("*.md")}
    rows: list[dict[str, str]] = []
    counts = {"Integrate": 0, "No Change — Existing Coverage": 0, "Weekly Only — Context": 0}

    for item in items:
        family = item["family"]
        disposition = item["disposition"]
        counts[disposition] += 1
        owner = item["owner"]
        target_rel = FINALIZER.PATHS[owner]
        adjacent_rel = FINALIZER.ADJACENT[owner]
        target = root / target_rel
        adjacent = root / adjacent_rel
        target_text = corpus[target]
        anchor = FINALIZER.TARGET_ANCHORS[owner]
        if target_text.splitlines().count(anchor) != 1:
            raise RuntimeError(f"owner anchor drift for {family}: {target_rel} / {anchor}")
        if not adjacent.is_file() or not adjacent.read_text().strip():
            raise RuntimeError(f"adjacent owner unavailable for {family}: {adjacent_rel}")
        hits = [
            (path, number)
            for path, text in corpus.items()
            for number, line in enumerate(text.splitlines(), 1)
            if family in line
        ]
        comparison = comparisons[family]

        if disposition == "Integrate":
            if len(hits) != 1 or hits[0][0] != target:
                raise RuntimeError(f"{family} expected exactly one Review note in {target_rel}, got {hits}")
            block = ready_blocks[owner]
            marker_start = f"<!-- daily-20260628:{owner}:start -->"
            marker_end = f"<!-- daily-20260628:{owner}:end -->"
            starts = sum(text.count(marker_start) for text in corpus.values())
            ends = sum(text.count(marker_end) for text in corpus.values())
            if (starts, ends) != (1, 1):
                raise RuntimeError(f"{family} duplicate/partial owner block: {(starts, ends)}")
            start = target_text.index(marker_start) + len(marker_start) + 1
            end = target_text.index(marker_end)
            inserted = target_text[start:end]
            if inserted != block["body"]:
                raise RuntimeError(f"{family} owner block differs from reviewed ready packet")
            required = [
                FINALIZER.OWNER_NARRATIVE[owner], FINALIZER.OWNER_BOUNDARY[owner], family,
                f"primary arXiv:{item['aid']}v1", f"exact-v1 URL=https://arxiv.org/html/{item['aid']}v1",
                f"Method={item['method']}", f"Evaluation={item['evaluation']}",
                f"Non-proof={item['limitation']}",
            ]
            missing = [value for value in required if value not in inserted]
            if missing:
                raise RuntimeError(f"{family} post-write fields missing: {missing}")
            evidence = f"unique Review note line {hits[0][1]}; owner block equals reviewed ready packet"
        else:
            if hits:
                raise RuntimeError(f"non-Integrate leakage for {family}: {hits}")
            if not comparison["existing_proposition"].strip() or not comparison["new_evidence_delta"].strip():
                raise RuntimeError(f"source-specific comparison missing for {family}")
            evidence = (
                f"re-read `{target_rel}` at `{anchor}` and adjacent `{adjacent_rel}`; "
                f"existing={comparison['existing_proposition']}; bounded delta={comparison['new_evidence_delta']}"
            )
        rows.append({
            "source_family_id": family, "disposition": disposition, "owner": target_rel,
            "adjacent": adjacent_rel, "evidence": evidence, "result": "PASS",
        })

    assert counts == {
        "Integrate": 6,
        "No Change — Existing Coverage": 42,
        "Weekly Only — Context": 17,
    }
    assert len(rows) == 65
    return rows


def write_receipts(rows: list[dict[str, str]]) -> None:
    fields = ["source_family_id", "disposition", "owner", "adjacent", "evidence", "result"]
    with (PACKET / "post-write-fresh-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        "# 2026-06-28 Post-write Fresh Audit V1", "",
        f"- Denominator: `{FINALIZER.DENOMINATOR}`; audited 65/65 retained families after serialized root writeback.",
        "- Integrate: PASS — 6/6 source-specific Review notes in exactly one expected owner; 6/6 owner blocks equal the reviewed ready packet and preserve mechanism evolution, trade-off/failure, coexistence/fallback and exact-v1 locators.",
        "- No Change: PASS — 42/42 current owner and adjacent chapters re-read; no 06-28 Source Family leaked into Books.",
        "- Weekly Only: PASS — 17/17 context-only families remain absent from Books and retain bounded handoffs.",
        "- Shared-file scope: other dates may coexist; only 06-28 markers, Source Families and current existing-coverage propositions were adjudicated.",
        "- Unresolved findings: 0. Coverage Closed; Evidence Passed; Selection Passed; Books Passed; Completion Complete.",
        "- Independence caveat: nested reviewer spawning was disabled; this is a fresh self-audit, not a claimed independent second-model review.", "",
        "| Source Family ID | Disposition | Owner + adjacent / evidence | Result |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['source_family_id']} | {row['disposition']} | `{row['owner']}` + `{row['adjacent']}` — {row['evidence']} | PASS |"
        )
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(lines) + "\n")


def transition(text: str, old: str, new: str, label: str) -> str:
    old_count, new_count = text.count(old), text.count(new)
    if (old_count, new_count) == (1, 0):
        return text.replace(old, new, 1)
    if (old_count, new_count) == (0, 1):
        return text
    raise RuntimeError(f"close-state drift for {label}: old={old_count}, final={new_count}")


def close_daily() -> None:
    text = REPORT.read_text()
    audit_lines = text.splitlines()
    audit_indexes = [
        index for index, line in enumerate(audit_lines)
        if line.startswith("| SA-20260628-BOOKS-")
    ]
    if len(audit_indexes) != 1:
        raise RuntimeError(f"expected one June-28 Books audit row, got {audit_indexes}")
    audit_index = audit_indexes[0]
    audit_cells = audit_lines[audit_index].split("|")
    if len(audit_cells) != 9:
        raise RuntimeError(f"unexpected Books audit column count: {len(audit_cells) - 2}")
    reviewed_refs = [value.strip() for value in audit_cells[4].split(";") if value.strip()]
    weekly_refs = [
        f"review:SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"
        for arxiv_id in sorted(FINALIZER.WEEKLY_ONLY)
    ]
    for review_ref in weekly_refs:
        if review_ref not in reviewed_refs:
            reviewed_refs.append(review_ref)
    audit_cells[4] = " " + "; ".join(reviewed_refs) + " "
    audit_lines[audit_index] = "|".join(audit_cells)
    text = "\n".join(audit_lines) + "\n"
    replacements = [
        # The canonical renderer drops the legacy pre-write blockquote.  The
        # authoritative Gate state is transitioned in the metadata table and
        # regenerated into the preamble/Final Status below.
        ("这些仍是 pre-write 决策，不是完成状态。", "root 已串行完成 6-family 写回，65/65 post-write fresh audit 通过。"),
        ("| Completion Status | In Progress |", "| Completion Status | Complete |"),
        ("| Books Gate | Open |", "| Books Gate | Passed |"),
        ("SA-20260628-BOOKS-PREWRITE-V1", "SA-20260628-BOOKS-POSTWRITE-V1"),
        ("root writeback pending | 6 Integrate merged into 6 owner narratives; 42 No Change and 17 Weekly Only re-audited against latest owner/adjacent chapters; post-write audit pending | open",
         "— | 6/6 Integrate writebacks, 42/42 No Change and 17/17 Weekly Only passed the 65/65 post-write fresh audit; unresolved findings 0 | passed"),
        ("- Integrate: 6 across 6 owner files; No Change: 42; Weekly Only: 17.",
         "- Integrate: 6/6 written across 6 owners; No Change: 42/42 revalidated; Weekly Only: 17/17 remained context-only."),
        ("- Shared Books/LEARNING_STATE were not edited. Root write lock and 65/65 post-write audit remain required.",
         "- Shared Books were updated under root's serialized write lock; `docs/LEARNING_STATE.md` was not edited by this lane; all 65 dispositions were audited after writeback."),
        ("- Date-local Daily, source packet and downstream scripts only.",
         "- Date-local Daily/source packet/scripts plus the root-authorized six-owner Books writeback."),
        ("- Books Gate remains Open until shared writeback and 65/65 post-write audit.",
         "- Books passed the 65/65 post-write fresh audit; unresolved findings: 0."),
        ("Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Open；Completion Status=In Progress。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。",
         "Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论由第 7 节记录的 pre-write 与 post-write fresh-context audit 承担。"),
    ]
    for index, (old, new) in enumerate(replacements, 1):
        text = transition(text, old, new, f"Daily transition {index}")
    REPORT.write_text(text)

    packet_readme = PACKET / "README.md"
    content = transition(packet_readme.read_text(),
        "- Books Gate: Open pending root writeback/post-write audit", "- Books Gate: Passed", "packet Books Gate")
    content = transition(content, "- Completion: In Progress", "- Completion: Complete", "packet Completion")
    receipt = "- Post-write fresh audit: 65/65 Passed; unresolved findings 0"
    if receipt not in content:
        content = content.rstrip() + "\n" + receipt + "\n"
    packet_readme.write_text(content)

    fresh_path = PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
    fresh_path.write_text(transition(
        fresh_path.read_text(),
        "- Evidence Gate: Passed; Selection Gate: Passed; Books Gate: Open.",
        "- Evidence Gate: Passed; Selection Gate: Passed; Books Gate: Passed after the 65/65 post-write fresh audit.",
        "fresh audit Books Gate",
    ))

    queue_path = PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md"
    queue_path.write_text(transition(
        queue_path.read_text(),
        f"Denominator {FINALIZER.DENOMINATOR}. Pre-write only: 6 Integrate, 42 No Change, 17 Weekly Only, 6 owner files. Shared write lock required.",
        f"Denominator {FINALIZER.DENOMINATOR}. CLOSED: root wrote 6 Integrate families into 6 owners; 42 No Change and 17 Weekly Only remained unwritten; the 65/65 post-write fresh audit passed.",
        "Books queue",
    ))


def refresh_hashes() -> None:
    sums = []
    for path in sorted(item for item in PACKET.iterdir() if item.is_file() and item.name != "SHA256SUMS"):
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name)
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")


def main() -> None:
    if finalize_accepted_presentation():
        return
    rows = audit_books()
    write_receipts(rows)
    close_daily()
    canonicalize_report(REPORT, "2026-06-28")
    # The semantic transition from pre-write to accepted post-write state
    # intentionally invalidates any pre-existing presentation seal.  Seal the
    # newly accepted canonical state immediately; subsequent runs take the
    # presentation-only path and verify this seal before doing anything.
    accepted_report = REPORT.read_text(encoding="utf-8")
    assert_canonical_presentation(accepted_report)
    protected = protected_report_fragments(accepted_report)
    packet_hashes = semantic_packet_hashes()
    write_presentation_audit(protected, packet_hashes, accepted_report)
    refresh_canonical_hashes()
    print(json.dumps({
        "post_write": "passed", "families": "65/65", "integrate": "6/6",
        "no_change": "42/42", "weekly_only": "17/17", "owners": "6/6",
        "unresolved_findings": 0,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
