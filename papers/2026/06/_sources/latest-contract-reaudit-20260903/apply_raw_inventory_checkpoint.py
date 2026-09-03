#!/usr/bin/env python3
"""Attach recovered raw-inventory checkpoints without overstating closure."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
SUMMARY = json.loads((AUDIT / "raw-semantic-recovery-summary.json").read_text(encoding="utf-8"))


def update(date: str, stats: dict) -> None:
    month, day = date[5:7], date[8:10]
    report = ROOT / f"papers/2026/{month}/{day}/README.md"
    packet_rel = f"../_sources/daily-{date.replace('-', '')}"
    text = report.read_text(encoding="utf-8")
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("| SRC-ARXIV |"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 12:
            continue
        cells[5] = "incomplete"
        cells[6] = str(stats["raw"])
        cells[8] = "—"
        cells[9] = "2026-09-03T12:45:00+08:00"
        cells[10] = (
            f"{packet_rel}/canonical-raw-identity-inventory-v2.1.json.gz; "
            f"{packet_rel}/official-arxiv-first-public-owner-receipt-v1.json; "
            f"coverage:SRC-ARXIV:{date.replace('-', '')}"
        )
        cells[11] = f"GAP-ARXIV-SEMANTIC-OWNER-REBUILD-{date.replace('-', '')}"
        lines[index] = "| " + " | ".join(cells) + " |"
        break
    text = "\n".join(lines) + "\n"
    note = (
        f"### Canonical raw-inventory recovery checkpoint\n\n"
        f"本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **{stats['raw']}** 条注册类别 identity，"
        f"并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。"
        f"其中 **{stats['retained_prior']}** 条是旧报告 retained provenance，"
        f"**{stats['closure_proposals_pending_audit']}** 条已获得逐 family title+abstract closure proposal。"
        f"这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；"
        f"因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。"
    )
    text = re.sub(
        r"(<!-- latest-contract-reopen:[^:]+:end -->)",
        r"\1\n\n" + note,
        text,
        count=1,
    )
    text = re.sub(
        r"当前 finding：`[^`]*`。",
        (
            "当前 finding：`canonical_owner_candidate_redistribution_pending, "
            "fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。"
        ),
        text,
        count=1,
    )
    report.write_text(text, encoding="utf-8")


def main() -> None:
    for date, stats in SUMMARY["per_report"].items():
        update(date, stats)


if __name__ == "__main__":
    main()
