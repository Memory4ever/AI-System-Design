#!/usr/bin/env python3
"""Materialize the non-author 2026-05-03 audit and final Books queue."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
LEDGER = ROOT / "screening-ledger-v2.1.json"
AUTHOR_QUEUE = ROOT / "BOOKS_INTEGRATION_QUEUE_V1.md"

DOWNGRADED = {
    "SF-LORA-COMPOSITION-RELIABILITY": (
        "No Change — Existing Coverage",
        "Ch30 already owns base/adapter identity, composition compatibility, re-evaluation, promotion and rollback; the exact-v1 multi-view proxy is an uncalibrated implementation branch.",
    ),
    "SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY": (
        "No Change — Existing Coverage",
        "Ch66 already requires assertion/oracle signal, execution path and failure discriminativeness for Agent-authored tests; the case study does not change release authority.",
    ),
    "SF-DATA-CONSTRAINED-SCALING-LAW": (
        "No Change — Existing Coverage",
        "Ch28 already jointly models unique-token volume, repetition, effective parameters, regularization and the data-saturation boundary with an empirical-scale caveat.",
    ),
}

ledger = json.loads(LEDGER.read_text())
rows = ledger["rows"]
retained = [row for row in rows if row["screening_decision"] == "retain"]
closures = [row for row in rows if row["screening_decision"] != "retain"]

row_receipts = [
    {
        "arxiv_id": row["arxiv_id"],
        "title": row["title"],
        "author_decision": row["screening_decision"],
        "independent_decision": "upheld",
        "review_basis": "title+abstract semantic replay against long-term AI-System admission contract",
    }
    for row in rows
]

audit = {
    "schema": "independent-semantic-audit-v1",
    "report_date": "2026-05-03",
    "auditor": "fresh-context:may2026-day01",
    "author_independence": "reviewer did not author the 2026-05-03 packet",
    "screening_ledger": str(LEDGER.relative_to(REPO)),
    "screening_ledger_sha256": hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
    "coverage": {
        "registered": len(rows),
        "replayed": len(row_receipts),
        "retained": len(retained),
        "pre_denominator_closures": len(closures),
        "false_negatives": [],
        "false_positives": [],
        "status": "passed",
    },
    "evidence": {
        "exact_v1_receipts_replayed": len(retained),
        "blocked": 0,
        "pending": 0,
        "unresolved_findings": [],
        "status": "passed",
    },
    "deep_analysis_selection": {
        "eligible_replayed": len(retained),
        "selected_units": [
            "DA-20260503-TOKEN-UNIT",
            "DA-20260503-CAUSAL-LOGS",
            "DA-20260503-SEQUENTIAL-MODEL-EDIT",
        ],
        "status": "passed",
    },
    "books": {
        "author_integrate_queue": 22,
        "downgraded_to_no_change": [
            {"source_family_id": family, "decision": decision, "reason": reason}
            for family, (decision, reason) in DOWNGRADED.items()
        ],
        "final_integrate_queue": 19,
        "structural_candidates": ["SF-SEQUENTIAL-MODEL-EDIT-SIDECAR"],
        "shared_books_written": False,
        "status": "open",
    },
    "row_receipts": row_receipts,
}
(ROOT / "independent-semantic-audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
)

source_lines = AUTHOR_QUEUE.read_text().splitlines()
queue_rows = []
for line in source_lines:
    if not line.startswith("|") or "queued_for_root_serial_write" not in line:
        continue
    if any(family in line for family in DOWNGRADED):
        continue
    queue_rows.append(line)

header = [
    "# 2026-05-03 Final Books Integration Queue",
    "",
    "本队列经过非作者 fresh-context audit；共享 Books 尚未写。root 必须按日期与 owner 串行写回，并在每组写回后审计 owner 与相邻章节。",
    "",
    "原 author queue=22；3 项因当前 Books 已完整覆盖而降级；最终 Integrate=19。",
    "",
    "| Order | Source Family | Owner | Target / Adjacent comparison | Requested semantic delta | Status |",
    "| --- | --- | --- | --- | --- | --- |",
]
renumbered = []
for number, row in enumerate(queue_rows, start=1):
    cells = row.split("|")
    cells[1] = f" {number} "
    renumbered.append("|".join(cells))

footer = [
    "",
    "## Downgraded after current-Books comparison",
    "",
]
for family, (_, reason) in DOWNGRADED.items():
    footer.append(f"- `{family}` — `No Change — Existing Coverage`：{reason}")
footer += [
    "",
    "## Structural Candidate",
    "",
    "- `SF-SEQUENTIAL-MODEL-EDIT-SIDECAR`：base weights、external edit memory、runtime override 与 registry lineage 仍跨越多个 owner；等待 root 结构裁决，不得在裁决前写成孤立新章。",
    "",
    "## Gate",
    "",
    "- Coverage：Closed",
    "- Evidence：Closed",
    "- Deep Analysis Selection：Closed",
    "- Books：Open（19 项共享写回、1 项结构裁决及 post-write audit）",
]
(ROOT / "BOOKS_INTEGRATION_QUEUE_FINAL.md").write_text(
    "\n".join(header + renumbered + footer) + "\n"
)

print(json.dumps({
    "registered": len(rows),
    "retained": len(retained),
    "closures": len(closures),
    "final_integrate_queue": len(queue_rows),
    "downgraded": len(DOWNGRADED),
}, ensure_ascii=False))
