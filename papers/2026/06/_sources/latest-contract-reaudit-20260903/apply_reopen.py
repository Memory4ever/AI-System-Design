#!/usr/bin/env python3
"""Truthfully reopen June/July reports whose V2.1 coverage is not reproducible."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
AUDIT_DIR = Path(__file__).resolve().parent
LEDGER = json.loads((AUDIT_DIR / "ledger.json").read_text(encoding="utf-8"))
REQUIRED = LEDGER["required_daily_source_ids"]


def replace_metadata(text: str) -> str:
    replacements = {
        "Completion Status": "In Progress",
        "Coverage Gate": "Open",
        "Evidence Gate": "Open",
        "Books Gate": "Open",
    }
    for field, value in replacements.items():
        text = re.sub(
            rf"^\| {re.escape(field)} \| .*? \|$", f"| {field} | {value} |", text, count=1, flags=re.M
        )
    text = re.sub(
        r"^\*\*Status:\*\*.*$",
        "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节",
        text,
        count=1,
        flags=re.M,
    )
    return text


def update_coverage(text: str, row: dict) -> str:
    marker = "<!-- validator:source-coverage-v2 -->"
    start = text.index(marker)
    end_candidates = [
        pos for token in ("\n<!--", "\n## ", "\n### ")
        if (pos := text.find(token, start + len(marker))) != -1
    ]
    end = min(end_candidates) if end_candidates else len(text)
    block = text[start:end]
    lines = block.splitlines()
    existing: set[str] = set()
    updated: list[str] = []
    original_source_ids = set(row["existing_source_ids"])
    for line in lines:
        if line.startswith("| SRC-"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            source_id = cells[0]
            if source_id not in original_source_ids:
                continue
            existing.add(source_id)
            if source_id == "SRC-ARXIV" and len(cells) == 12:
                cells[5] = "incomplete"
                if "Pending — official daily announcement/listing owner reconciliation" not in cells[8]:
                    cells[8] += "; Pending — official daily announcement/listing owner reconciliation"
                cells[9] = "—"
                cells[10] = cells[10].split("; latest-contract audit:", 1)[0].strip()
                cells[11] = f"GAP-ARXIV-FIRST-PUBLIC-{row['date'].replace('-', '')}"
                line = "| " + " | ".join(cells) + " |"
        updated.append(line)
    return text[:start] + "\n".join(updated) + text[end:]


def update_semantic_audit(text: str, row: dict) -> str:
    marker = "<!-- validator:semantic-audit-v1 -->"
    if marker not in text:
        return text
    start = text.index(marker)
    end_candidates = [
        pos for token in ("\n<!--", "\n## ", "\n### ")
        if (pos := text.find(token, start + len(marker))) != -1
    ]
    end = min(end_candidates) if end_candidates else len(text)
    block = text[start:end]
    findings = {
        "coverage": "latest-contract arXiv first-public owner receipt incomplete",
        "evidence": "candidate identity/date and exact-material acceptance must be replayed after owner reconciliation",
        "deep_analysis_selection": "eligibility frontier must be rechecked after denominator repair",
        "books": "existing disposition is provenance only until upstream gates and fresh Books comparison pass",
    }
    out: list[str] = []
    for line in block.splitlines():
        if line.startswith("|") and not line.startswith("| ---"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) == 7 and cells[2] in findings:
                scope = cells[2]
                cells[4] = findings[scope]
                cells[5] = (
                    "Open — see papers/2026/06/_sources/latest-contract-reaudit-20260903/"
                    f"ledger.json entry {row['date']}"
                )
                cells[6] = "open"
                line = "| " + " | ".join(cells) + " |"
        out.append(line)
    return text[:start] + "\n".join(out) + text[end:]


def insert_reopen_notice(text: str, row: dict) -> str:
    tag = f"<!-- latest-contract-reopen:{row['date']}:start -->"
    issue_text = ", ".join(row["issues"])
    notice = f"""
{tag}
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv 归属仍缺官方逐日 announcement/listing receipt。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`{issue_text}`。
<!-- latest-contract-reopen:{row['date']}:end -->
"""
    if tag in text:
        return re.sub(
            rf"{re.escape(tag)}.*?<!-- latest-contract-reopen:{re.escape(row['date'])}:end -->",
            notice.strip(),
            text,
            count=1,
            flags=re.S,
        )
    anchor = "## 2. Candidate Ledger"
    return text.replace(anchor, notice + "\n" + anchor, 1)


def update_final(text: str, row: dict) -> str:
    unresolved = len([issue for issue in row["issues"] if issue != "zero_byte_files_ignored"])
    final_heading = "## 13. Final Summary"
    state_prefix = "State Truth:"
    if final_heading in text:
        start = text.index(final_heading) + len(final_heading)
        state = text.find(state_prefix, start)
        if state != -1:
            replacement = (
                "\n\n最新合同复核已重新打开本日报。旧候选、Source Review 与 Books Decision "
                "仅作为 provenance 保留；在官方 arXiv first-public owner receipt、分母重放、"
                "fresh-context Evidence/Selection/Books audit 全部通过前，不得将本日报表述为闭环。\n\n"
            )
            text = text[:start] + replacement + text[state:]
    text = re.sub(
        r"State Truth: Completion=.*?Unresolved Findings=\d+。",
        f"State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings={unresolved}。",
        text,
        count=1,
    )
    return text


def main() -> None:
    for row in LEDGER["reports"]:
        report = ROOT / row["report"]
        text = report.read_text(encoding="utf-8")
        text = replace_metadata(text)
        text = update_coverage(text, row)
        text = insert_reopen_notice(text, row)
        text = update_semantic_audit(text, row)
        text = update_final(text, row)
        report.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
