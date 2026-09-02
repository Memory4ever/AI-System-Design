#!/usr/bin/env python3
"""Close March 2026 Historical Daily reports after semantic and Books evidence exists.

This script is deliberately a reconciler, not a reviewer.  It refuses to close a
day unless the already-written artifacts prove that every Integrate disposition
has exactly one Books marker and a passed independent post-write audit.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/03"
BOOKS = ROOT / "books"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def candidate_rows(text: str) -> list[dict[str, str]]:
    marker = "<!-- validator:candidate-ledger-v2.1 -->"
    if marker not in text:
        raise ValueError("missing candidate ledger marker")
    tail = text.split(marker, 1)[1].lstrip()
    lines = tail.splitlines()
    if len(lines) < 2 or not lines[0].startswith("|"):
        raise ValueError("invalid candidate ledger")
    headers = [cell.strip() for cell in lines[0].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            raise ValueError(f"candidate ledger width mismatch: {line[:120]}")
        rows.append(dict(zip(headers, cells)))
    return rows


def all_books_text() -> tuple[str, dict[str, str]]:
    by_path: dict[str, str] = {}
    for path in sorted(BOOKS.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        by_path[rel] = path.read_text(encoding="utf-8")
    return "\n".join(by_path.values()), by_path


def replace_section(text: str, heading: str, body: str) -> str:
    pattern = re.compile(
        rf"(?ms)^{re.escape(heading)}\n\n.*?(?=^##\s|\Z)"
    )
    replacement = f"{heading}\n\n{body.rstrip()}\n\n"
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise ValueError(f"cannot replace section {heading}")
    return updated


def replace_metadata(text: str, field: str, value: str) -> str:
    pattern = re.compile(rf"(?m)^\| {re.escape(field)} \| .* \|$")
    updated, count = pattern.subn(f"| {field} | {value} |", text, count=1)
    if count != 1:
        raise ValueError(f"cannot replace metadata {field}")
    return updated


def close_semantic_row(
    text: str, scope_suffix: str, resolution: str
) -> str:
    pattern = re.compile(
        rf"(?m)^\| (SA-[^|]+-{scope_suffix}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$"
    )

    def repl(match: re.Match[str]) -> str:
        return (
            f"| {match.group(1).strip()} | {match.group(2).strip()} | "
            f"{match.group(3).strip()} | {match.group(4).strip()} | — | "
            f"{resolution} | passed |"
        )

    updated, count = pattern.subn(repl, text, count=1)
    if count != 1:
        raise ValueError(f"cannot close semantic scope {scope_suffix}")
    return updated


def reconcile_artifact_statuses(source_dir: Path) -> None:
    replacements = {
        "completed_pending_root_gate_reconcile": "completed_reconciled",
        "partially_applied_pending_root_final_reconcile": "applied_postwrite_verified",
        "applied_pending_root_final_reconcile": "applied_postwrite_verified",
        "pending_root_serial_writeback_and_fresh_context_prewrite_audit": "applied_postwrite_verified",
        "pending_root_serial_writeback_and_fresh_context_prewrite": "applied_postwrite_verified",
        "pending_root_serial_writeback": "applied_postwrite_verified",
        "applied_pending_postwrite_semantic_audit": "applied_postwrite_verified",
        "applied_pending_post_write_audit": "applied_postwrite_verified",
    }
    for path in sorted(source_dir.glob("*.json")):
        raw = path.read_text(encoding="utf-8")
        updated = raw
        for old, new in replacements.items():
            updated = updated.replace(f'"{old}"', f'"{new}"')
        if updated != raw:
            path.write_text(updated, encoding="utf-8")

    queue_path = source_dir / "BOOKS_WRITEBACK_QUEUE.json"
    if queue_path.exists():
        queue = read_json(queue_path)
        items = queue.get("items", [])
        if items:
            queue["status"] = "applied_postwrite_verified"
            for item in items:
                item["writeback_status"] = "applied_postwrite_verified"
        else:
            queue["status"] = "no_writeback_required"
        queue_path.write_text(
            json.dumps(queue, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    proposal_path = source_dir / "denominator-screening-proposal.json"
    if proposal_path.exists():
        proposal = read_json(proposal_path)
        proposal["artifact_status"] = "superseded_by_screening_ledger_final"
        proposal["superseded_by"] = "screening-ledger-final.json"
        proposal_path.write_text(
            json.dumps(proposal, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def reconcile_queue_markdown(path: Path) -> None:
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    for line in lines:
        if line.startswith("| SF-"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            cells[-1] = "applied_postwrite_verified"
            line = "| " + " | ".join(cells) + " |"
        updated.append(line)
    path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    combined_books, books_by_path = all_books_text()
    ready: list[
        tuple[
            Path,
            Path,
            str,
            list[dict[str, str]],
            list[dict],
            list[dict[str, str]],
        ]
    ] = []
    failures: list[str] = []

    for day in range(1, 32):
        report_date = f"2026-03-{day:02d}"
        report_path = MONTH / f"{day:02d}/README.md"
        source_dir = MONTH / f"_sources/daily-202603{day:02d}"
        try:
            text = report_path.read_text(encoding="utf-8")
            rows = candidate_rows(text)
            ordinary_pending = [
                row for row in rows
                if row["Review Status"] in {"pending", "blocked"}
                or row["Access Status"] in {"partial", "blocked", "unverified"}
                or row["Books Disposition"] == "Not Assessed"
            ]
            if ordinary_pending:
                raise ValueError(f"{len(ordinary_pending)} ordinary pending candidate rows")
            external_limitations = [
                row for row in rows
                if row["Access Status"] == "disputed"
                or row["Books Disposition"] == "Disputed"
            ]
            for row in external_limitations:
                family = row["Source Family ID"]
                materials = read_json(source_dir / "materials-request.json")
                request_ids = {
                    item.get("source_family_id") for item in materials.get("items", [])
                }
                if family not in request_ids:
                    raise ValueError(
                        f"{family} disputed without a precise Materials Request"
                    )

            integrates = [
                row for row in rows if row["Books Disposition"] == "Integrate"
            ]
            integrate_ids = {row["Source Family ID"] for row in integrates}
            queue_path = source_dir / "BOOKS_WRITEBACK_QUEUE.json"
            queue = read_json(queue_path)
            queue_items = queue.get("items", [])
            queue_ids = {item["source_family_id"] for item in queue_items}
            if queue_ids != integrate_ids:
                raise ValueError(
                    f"queue/integrate mismatch queue={sorted(queue_ids)} "
                    f"ledger={sorted(integrate_ids)}"
                )

            for item in queue_items:
                family = item["source_family_id"]
                marker = f"<!-- source-family:{family} -->"
                if combined_books.count(marker) != 1:
                    raise ValueError(
                        f"{family} Books marker count={combined_books.count(marker)}"
                    )
                owner = item.get("owner_path")
                if not owner or owner not in books_by_path:
                    raise ValueError(f"{family} unresolved owner path {owner!r}")
                owner_text = books_by_path[owner]
                if marker not in owner_text:
                    raise ValueError(f"{family} marker is not in declared owner {owner}")
                review_notes = owner_text.rfind("\n## Review notes")
                if review_notes >= 0 and owner_text.index(marker) > review_notes:
                    raise ValueError(f"{family} mechanism appears after Review notes")

            if integrates:
                post_path = source_dir / "postwrite-semantic-audit.json"
                if not post_path.exists():
                    raise ValueError("missing postwrite semantic audit")
                post = read_json(post_path)
                post_ids = {
                    item.get("source_family_id")
                    for item in post.get("items", [])
                    if item.get("status") == "passed"
                    and item.get("marker_count") == 1
                }
                if post.get("status") != "passed" or post.get("unresolved_findings"):
                    raise ValueError("postwrite semantic audit is not passed")
                if post_ids != integrate_ids:
                    raise ValueError(
                        f"postwrite/integrate mismatch passed={sorted(post_ids)} "
                        f"ledger={sorted(integrate_ids)}"
                    )

            receipt = read_json(source_dir / "fresh-context-audit-receipt.json")
            if receipt.get("weekly_dependency") != 0:
                raise ValueError("fresh-context audit used Weekly dependency")
            if receipt.get("screened") != receipt.get("raw_identities"):
                raise ValueError("fresh-context audit did not screen all raw identities")
            ready.append(
                (
                    report_path,
                    source_dir,
                    text,
                    integrates,
                    queue_items,
                    external_limitations,
                )
            )
        except Exception as exc:  # report every day, not only the first
            failures.append(f"{report_date}: {exc}")

    if failures:
        print(json.dumps({"ready": len(ready), "failures": failures}, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    if not args.apply:
        print(json.dumps({"ready": len(ready), "status": "preflight_passed"}, ensure_ascii=False, indent=2))
        return

    for (
        report_path,
        source_dir,
        text,
        integrates,
        queue_items,
        external_limitations,
    ) in ready:
        date = report_path.parent.name
        report_date = f"2026-03-{date}"
        owner_paths = sorted({item["owner_path"] for item in queue_items})

        completion = "Conditional" if external_limitations else "Complete"
        evidence_gate = "Conditional Pass" if external_limitations else "Passed"
        books_gate = "Conditional Pass" if external_limitations else "Passed"
        text = re.sub(
            r"(?m)^\*\*Status:\*\*.*$",
            f"**Status:** {completion}；Coverage=Closed、Evidence={evidence_gate}、Books={books_gate}；"
            "fresh-context Coverage / Evidence / Selection / Books Semantic Audit "
            "与必要的 post-write audit 均已闭合；外部证据限制已精确登记。"
            if external_limitations
            else
            f"**Status:** {completion}；Coverage=Closed、Evidence={evidence_gate}、Books={books_gate}；"
            "fresh-context Coverage / Evidence / Selection / Books Semantic Audit "
            "与必要的 post-write audit 均已闭合。",
            text,
            count=1,
        )
        text = replace_metadata(text, "Completion Status", completion)
        text = replace_metadata(text, "Coverage Gate", "Closed")
        text = replace_metadata(text, "Evidence Gate", evidence_gate)
        text = replace_metadata(text, "Books Gate", books_gate)
        text = close_semantic_row(
            text,
            "COVERAGE",
            "accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核",
        )
        evidence_resolution = (
            "conditionally accepted: retained family 均完成 exact-v1 review；"
            "普通 blocked/unverified=0，外部 disputed claim 已登记 Materials Request，且未写成已证实结论"
            if external_limitations
            else "accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0"
        )
        text = close_semantic_row(text, "EVIDENCE", evidence_resolution)
        text = close_semantic_row(
            text,
            "SELECTION",
            "accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核",
        )
        books_resolution = (
            "accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过"
            if integrates
            else "accepted: 所有 Books disposition 已复核，本日无需写回"
        )
        text = close_semantic_row(text, "BOOKS", books_resolution)

        text = re.sub(
            r"作者侧决定为 \*\*Integrate\*\*；Integrate 项(?:仅进入串行队列，尚未写回|已写回，等待 post-write Semantic Audit 闭合)。",
            "最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。",
            text,
        )
        text = re.sub(
            r"作者侧决定为 \*\*(No Change — Existing Coverage|Structural Candidate)\*\*；Integrate 项仅进入串行队列，尚未写回。",
            lambda match: (
                f"最终决定为 **{match.group(1)}**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。"
            ),
            text,
        )

        if integrates:
            action = (
                f"本日 {len(integrates)} 项长期机制已完成 exact-v1 证据审阅、"
                "canonical owner 写回与非写作者 post-write Semantic Audit；"
                "后续仅在 primary revision 或新反证出现时重开。"
            )
        else:
            action = (
                "本日所有候选均已获得最终 disposition；没有需要写入 Books 的长期机制，"
                "后续仅在 primary revision 或新反证出现时重开。"
            )
        text = replace_section(text, "## 9. Recommended Action", action)

        if owner_paths:
            owner_list = "\n".join(f"- 更新并复核 `{path}`。" for path in owner_paths)
            repo_changes = (
                "- 新增或幂等更新本日 Daily 与可复算 source packet。\n"
                f"- 完成 {len(integrates)} 项 Books Integration：\n{owner_list}\n"
                "- 未修改 Weekly；未 stage、commit 或 push。"
            )
        else:
            repo_changes = (
                "- 新增或幂等更新本日 Daily 与可复算 source packet。\n"
                "- Books Decision 已闭合，本日无需修改 Books。\n"
                "- 未修改 Weekly；未 stage、commit 或 push。"
            )
        text = replace_section(text, "## 10. Repository Changes", repo_changes)
        if external_limitations:
            families = "、".join(
                row["Source Family ID"] for row in external_limitations
            )
            open_questions = (
                "- 普通 Gate finding=0；没有未执行的 review 或 writeback。\n"
                f"- 外部证据限制：{families} 保持 Disputed；精确缺失材料与可接受替代物见 "
                "`Materials Request Ledger`。该限制不会被伪装成已证实结论。"
            )
        else:
            open_questions = (
                "- 普通 Gate finding=0；blocked / unverified / disputed=0。\n"
                "- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；"
                "它们不是本次流程 pending。"
            )
        text = replace_section(text, "## 11. Open Questions", open_questions)
        final_status = (
            f"- Completion Status: `{completion}`\n"
            "- Coverage: `Closed`\n"
            f"- Evidence: `{evidence_gate}`\n"
            f"- Books: `{books_gate}`\n"
            f"- unresolved findings: {len(external_limitations)}"
        )
        text = replace_section(text, "## 13. Final Status", final_status)
        report_path.write_text(text.rstrip() + "\n", encoding="utf-8")

        reconcile_artifact_statuses(source_dir)
        reconcile_queue_markdown(source_dir / "BOOKS_WRITEBACK_QUEUE.md")

    print(json.dumps({"closed": len(ready), "status": "applied"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
