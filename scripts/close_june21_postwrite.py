#!/usr/bin/env python3
"""Audit all 37 June-21 Books dispositions and close the Daily after writeback."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

try:
    from scripts import apply_june21_books as APPLY
except ModuleNotFoundError:  # Direct execution sets scripts/ as sys.path[0].
    import apply_june21_books as APPLY


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260621"
REPORT = ROOT / "papers/2026/06/21/README.md"
FINALIZER = APPLY.FINALIZER

NO_CHANGE_ANCHORS = {
    "2606.21822": "model verdict 是 policy-bound sensor，不是 authority",
    "2606.21836": "## Evaluator-Driven Search：可执行反馈如何变成 Workflow",
    "2606.21842": "跨请求 KV reuse 一旦放松 exact-prefix 条件",
    "2606.21854": "## Variable-length Batch 让并行计划成为 Runtime State",
    "2606.21856": "AgentRun / Workflow state",
    "2606.21875": "### Calibration Slice 必须包含 Language × Model Scale × Estimator Contract",
    "2606.21917": "Monitoring 可以把已经校准的 evaluation results 聚合为时间序列",
    "2606.21959": "Research Agent 还需要把 final artifact、research progress 与 environment integrity 分开",
    "2606.21963": "Runbook 应包含 detection、owner、diagnosis queries",
    "2606.21994": "### OPD 是探索催化剂，不是能力上限扩展器",
    "2606.22000": "### 从 Pass@k 到 Pass^k：能力覆盖与重复可靠性不是同一问题",
    "2606.22030": "事实型 Memory 的 confidence 也不能只由 embedding similarity 或邻居投票生成",
    "2606.22082": "### 共享 Repository 需要 Commitment Protocol，不只是更多消息",
    "2606.22085": "### CoT Monitor 是 Policy-bound Sensor，不是 Authority",
    "2606.22136": "### 从 Physical Teleoperation 到带 Provenance 的 Digital Teleoperation Data",
    "2606.22189": "## 去重为什么改变梯度而不只是节省磁盘",
    "2606.22248": "### 从样本数量到 Coverage Contract：Curriculum 必须同时管理内容、能力与环境",
}


def audit_books(root: Path = ROOT) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    books = list((root / "books").rglob("*.md"))
    integrates = {aid: evidence for aid, evidence in FINALIZER.C.items() if evidence["disposition"] == "Integrate"}
    no_changes = {aid: evidence for aid, evidence in FINALIZER.C.items() if evidence["disposition"].startswith("No Change")}
    assert len(integrates) == 20 and len(no_changes) == 17 and set(no_changes) == set(NO_CHANGE_ANCHORS)

    for aid, evidence in integrates.items():
        source_family = APPLY.family(aid)
        expected_path = root / FINALIZER.PATHS[evidence["owner"]]
        hits = [(path, number) for path in books for number, line in enumerate(path.read_text().splitlines(), 1) if source_family in line]
        if len(hits) != 1:
            raise RuntimeError(f"{source_family} expected one Review note, got {hits}")
        if hits[0][0] != expected_path:
            raise RuntimeError(f"{source_family} owner conflict: {hits[0][0]} != {expected_path}")
        text = expected_path.read_text()
        start, end = APPLY.marker(evidence["owner"], "start"), APPLY.marker(evidence["owner"], "end")
        if text.count(start) != 1 or text.count(end) != 1 or text.index(start) >= text.index(end):
            raise RuntimeError(f"{source_family} missing unique owner block")
        block = text[text.index(start) : text.index(end) + len(end)]
        exact = f"https://arxiv.org/html/{aid}v1"
        required = [
            evidence["delta"], evidence["boundary"], source_family,
            f"exact-v1 URL=`{exact}`", f"Method=`{exact} — {evidence['method']}`",
            f"Evaluation=`{exact} — {evidence['evaluation']}`",
            f"Non-proof=`{exact} — {evidence['limitation']}`",
            "回退到现有 deterministic owner、supported path 或人工审批",
        ]
        missing = [value for value in required if value not in block]
        if missing:
            raise RuntimeError(f"{source_family} post-write semantic fields missing: {missing}")
        rows.append({"source_family_id": source_family, "disposition": "Integrate", "owner": FINALIZER.PATHS[evidence["owner"]], "evidence": f"line {hits[0][1]}; mechanism/trade-off/fallback/exact-v1 note", "result": "PASS"})

    for aid, evidence in no_changes.items():
        source_family = APPLY.family(aid)
        hits = [(path, number) for path in books for number, line in enumerate(path.read_text().splitlines(), 1) if source_family in line]
        if hits:
            raise RuntimeError(f"No Change leakage for {source_family}: {hits}")
        expected_path = root / FINALIZER.PATHS[evidence["owner"]]
        text = expected_path.read_text()
        anchor = NO_CHANGE_ANCHORS[aid]
        if text.count(anchor) != 1:
            raise RuntimeError(f"No Change proposition anchor drift for {source_family}: {anchor!r}")
        rows.append({"source_family_id": source_family, "disposition": "No Change — Existing Coverage", "owner": FINALIZER.PATHS[evidence["owner"]], "evidence": anchor, "result": "PASS"})
    assert len(rows) == 37
    return rows


def write_receipts(rows: list[dict[str, str]]) -> None:
    tsv = PACKET / "post-write-fresh-audit-v1.tsv"
    with tsv.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source_family_id", "disposition", "owner", "evidence", "result"], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        "# 2026-06-21 Post-write Fresh Audit V1", "",
        "- Denominator: `DEN-20260621-83b5c89e`; audited 37/37 retained families after serialized root writeback.",
        "- Integrate: 20/20 across 12/12 owners; each owner block preserves the mechanism, trade-off/failure, coexistence/fallback and one source-specific exact-v1 Review note.",
        "- No Change: 17/17 source-specific existing-proposition anchors re-read; no 06-21 Source Family leaked into Books.",
        "- Shared-file scope: later-date content can coexist; only the 06-21 owner blocks and existing propositions were adjudicated.",
        "- Unresolved findings: 0. Coverage Closed; Evidence Passed; Selection Passed; Books Passed; Completion Complete.",
        "- Independence caveat: nested reviewer spawning was disabled; this is a fresh self-audit, not a claimed independent second-model review.", "",
        "| Source Family ID | Disposition | Owner / evidence | Result |", "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['source_family_id']} | {row['disposition']} | `{row['owner']}` — {row['evidence']} | {row['result']} |")
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(lines) + "\n")


def _transition(text: str, old: str, new: str, label: str) -> str:
    old_count, new_count = text.count(old), text.count(new)
    if (old_count, new_count) == (1, 0):
        return text.replace(old, new, 1)
    if (old_count, new_count) == (0, 1):
        return text
    raise RuntimeError(
        f"close-state drift for {label}: old={old_count}, final={new_count}"
    )


def _is_canonical_complete_report(text: str) -> bool:
    return all(
        marker in text
        for marker in (
            "## 2. Candidate Ledger\n",
            "## 3. Review Completion Receipt\n",
            "## 13. Final Status\n",
        )
    )


def _assert_canonical_complete_report(text: str) -> None:
    """Fail closed unless the canonical report is already fully closed.

    Presentation migration replaced the legacy transition sentences.  A
    canonical report therefore cannot be passed back through the old textual
    replacements.  It is a no-op only after every Gate truth and the 37-family
    post-write receipt are independently visible and all old Open tokens are
    absent.
    """

    required_once = (
        "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
        "| Completion Status | Complete |",
        "| Coverage Gate | Closed |",
        "| Evidence Gate | Passed |",
        "| Books Gate | Passed |",
        "| SA-20260621-BOOKS-POSTWRITE-V1 |",
        "- Post-write fresh audit: 37/37 Passed; Books Gate Passed and Completion is Complete.",
        "- Fresh-context Semantic Audit: Passed；unresolved findings = 0.",
        "State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。",
    )
    bad_counts = {marker: text.count(marker) for marker in required_once if text.count(marker) != 1}
    if bad_counts:
        raise RuntimeError(f"canonical 06-21 close-state drift: {bad_counts}")

    forbidden = (
        "| Completion Status | In Progress |",
        "| Books Gate | Open |",
        "SA-20260621-BOOKS-PREWRITE-V1",
        "root writeback pending",
        "Books Gate remains Open",
    )
    leaked = [marker for marker in forbidden if marker in text]
    if leaked:
        raise RuntimeError(f"canonical 06-21 report retains Open-state tokens: {leaked}")


def close_daily(report: Path = REPORT, packet: Path = PACKET) -> None:
    text = report.read_text()
    if _is_canonical_complete_report(text):
        _assert_canonical_complete_report(text)
    else:
        replacements = {
            "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open，等待已授权的 serialized writeback 后 fresh-context Semantic Audit": "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding",
            "Coverage, Evidence and Selection passed; Books remains Open pending root writeback and this lane's post-write fresh audit.": "Coverage, Evidence, Selection and Books passed after root writeback and the 37/37 post-write fresh audit.",
            "| Completion Status | In Progress |": "| Completion Status | Complete |",
            "| Books Gate | Open |": "| Books Gate | Passed |",
            "SA-20260621-BOOKS-PREWRITE-V1": "SA-20260621-BOOKS-POSTWRITE-V1",
            "root writeback pending | 20 Integrate proposals and 17 No Change handoffs checked; post-write audit pending | open": "— | 20/20 Integrate writebacks across 12 owners plus 17/17 No Change handoffs passed the post-write fresh audit; unresolved findings 0 | passed",
            "- Integrate: 20; No Change: 17.": "- Integrate: 20/20 written into 12 unique owners; No Change: 17/17 revalidated.",
            "- Books Gate remains Open until root applies the owner-merged packet and this lane completes full post-write audit.": "- Post-write fresh audit: 37/37 Passed; Books Gate Passed and Completion is Complete.",
            "- This lane changed only the 2026-06-21 Daily, date-specific source packet and finalizer; shared Books were not edited.": "- Root performed the serialized 20-family Books writeback across 12 owners; this lane changed only the 2026-06-21 Daily/source packet/date-local scripts and audited the shared result.",
            "- Status: In Progress.": "- Status: Complete.",
            "- Books Gate: Open pending serialized writeback and post-write fresh audit.": "- Books Gate: Passed.\n- Fresh-context Semantic Audit: Passed；unresolved findings = 0.",
        }
        for number, (old, new) in enumerate(replacements.items(), 1):
            text = _transition(text, old, new, f"Daily transition {number}")
    report.write_text(text)

    packet_readme_path = packet / "README.md"
    packet_readme = packet_readme_path.read_text()
    packet_readme = _transition(
        packet_readme,
        "- Books Gate: Open pending root writeback/post-write audit",
        "- Books Gate: Passed",
        "packet Books Gate",
    )
    packet_readme = _transition(
        packet_readme,
        "- Completion: In Progress",
        "- Completion: Complete",
        "packet Completion",
    )
    audit_line = "- Post-write fresh audit: 37/37 Passed; unresolved findings 0"
    audit_count = packet_readme.splitlines().count(audit_line)
    if audit_count == 0:
        packet_readme = packet_readme.rstrip() + "\n" + audit_line + "\n"
    elif audit_count != 1:
        raise RuntimeError(f"packet post-write receipt duplicated: {audit_count}")
    packet_readme_path.write_text(packet_readme)

    fresh_path = packet / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md"
    fresh = _transition(
        fresh_path.read_text(),
        "- Coverage Gate Closed; Evidence Gate Passed; Selection Gate Passed; Books Gate Open pending root writeback/post-write audit.",
        "- Coverage Gate Closed; Evidence Gate Passed; Selection Gate Passed; Books Gate Passed after the 37/37 post-write fresh audit.",
        "fresh audit Books Gate",
    )
    fresh_path.write_text(fresh)

    queue_path = packet / "BOOKS_INTEGRATION_QUEUE_V1.md"
    queue = _transition(
        queue_path.read_text(),
        "Pre-write only: 20 family deltas merged into 12 owner files; root writeback and post-write audit pending.",
        "CLOSED: root wrote 20 family deltas into 12 owner files; the 37/37 post-write audit passed.",
        "Books queue",
    )
    queue_path.write_text(queue)


def refresh_hashes() -> None:
    sums = []
    for path in sorted(item for item in PACKET.iterdir() if item.is_file() and item.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name)
    external_targets = (
        (REPORT, "../../21/README.md"),
        (ROOT / "scripts/finalize_june21_v21.py", "../../../../../scripts/finalize_june21_v21.py"),
        (Path(__file__).resolve(), "../../../../../scripts/close_june21_postwrite.py"),
        (ROOT / "scripts/test_june21_books_workflow.py", "../../../../../scripts/test_june21_books_workflow.py"),
    )
    for path, relative_name in external_targets:
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + relative_name)
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")


def main() -> None:
    rows = audit_books()
    write_receipts(rows)
    close_daily()
    refresh_hashes()
    print(json.dumps({"post_write": "passed", "integrate": "20/20", "no_change": "17/17", "owners": 12, "unresolved_findings": 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
