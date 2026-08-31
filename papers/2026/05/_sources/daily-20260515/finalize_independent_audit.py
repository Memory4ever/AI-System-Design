#!/usr/bin/env python3
"""Materialize the non-author 2026-05-15 semantic audit without writing Books."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "15" / "README.md"

RESTORED = [
    "2605.14290", "2605.14415", "2605.14498", "2605.14514", "2605.14570",
    "2605.14678", "2605.14744", "2605.14747", "2605.14786", "2605.14865",
    "2605.14906", "2605.14968", "2605.14978", "2605.15034", "2605.15100",
    "2605.15118", "2605.15128", "2605.15138", "2605.15152", "2605.15155",
    "2605.15172", "2605.15178", "2605.15188", "2605.15403", "2605.15425",
    "2605.15466", "2605.15477",
]

SURVIVORS = [
    "2605.14241", "2605.14421", "2605.15051", "2605.15079", "2605.15109",
    "2605.15132", "2605.15185", "2605.15238", "2605.15257", "2605.15377",
    "2605.15384", "2605.15422", "2605.18859",
]

audit = {
    "schema": "daily-v2.1-independent-semantic-audit-with-books-prewrite-v1",
    "report_date": "2026-05-15",
    "reviewer_role": "independent_non_author_non_books_writer",
    "author_ledger_ref": "screening-ledger-final.json",
    "scope": {
        "registered_identities": 668,
        "title_abstract_replayed": 668,
        "author_retained_challenged": 29,
        "author_closures_challenged": 639,
        "final_retained_challenged": 56,
        "exact_v1_receipts_challenged": 56,
        "books_comparisons_challenged": 56,
    },
    "false_positive_findings": [],
    "false_negative_findings": [
        {
            "arxiv_id": arxiv_id,
            "source_family_id": f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}",
            "resolution": "restored_to_denominator_and_exact_v1_reviewed",
        }
        for arxiv_id in RESTORED
    ],
    "reconciled_counts": {
        "registered": 668,
        "fully_screened": 668,
        "author_retained": 29,
        "false_positives": 0,
        "false_negatives": 27,
        "final_denominator": 56,
        "closures": 612,
        "evidence_complete": 56,
        "evidence_open": 0,
        "blocked": 0,
        "provisional_integrates": 15,
        "root_writeback_ready_integrates": 13,
    },
    "evidence_result": {
        "status": "passed",
        "exact_v1_complete": 56,
        "html_reviews": 54,
        "official_pdf_reviews": ["2605.14968", "2605.15152"],
        "ordinary_pending": 0,
        "blocked": 0,
        "note": "Every retained family has exact-version provenance, Method/Evaluation/limitations-or-explicit-absence locators, claim/non-proof boundary and Review Ref. A local full-body hash is not a public Gate requirement.",
    },
    "books_prewrite_challenge": {
        "scope": "15 provisional Integrates against current owner and adjacent chapters",
        "provisional_integrates": 15,
        "final_integrates": 13,
        "downgraded_no_change": {
            "2605.14249": "Ch70 already contains layer-wise energy measurement/model, architecture-level proxy and device/precision/batch/shape/utilization constraints.",
            "2605.14591": "Ch66 already contains post-hoc dataset/membership inference boundaries and distinguishes those sensors from mechanism-level accounting.",
        },
        "survivors": SURVIVORS,
        "owner_merged_narrative_ref": "BOOKS_WRITEBACK_QUEUE_FINAL.md",
        "shared_books_modified": False,
    },
    "deep_analysis_selection": {
        "status": "passed",
        "selected": [
            "DA-MEMORY-LINEAGE-GATE",
            "DA-ASYNC-CHECKPOINT-ROLLBACK",
            "DA-LIVE-AGENT-ROUTING-EVAL",
        ],
        "reason": "The three narratives expose distinct durable ownership transitions across memory/action, generation/checking and routing/environment execution; the remaining retained families stay fully reviewed without duplicating Deep Analysis.",
    },
    "gate_result": {
        "coverage": "Closed",
        "evidence": "Passed",
        "books": "Open",
        "completion": "In Progress",
        "reason": "Coverage and Evidence are independently reconciled. Books remains Open until root serially writes the 13-family queue and a non-writer post-write audit verifies semantic integration.",
    },
    "unresolved_findings": [
        "Root serial Books writeback for the 13-family final queue, followed by non-writer post-write semantic audit."
    ],
}
(ROOT / "independent-semantic-audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
)

challenge = {
    "schema": "books-prewrite-challenge-v2.1",
    "report_date": "2026-05-15",
    "reviewer_role": "independent_non_author_non_books_writer",
    "provisional_integrates": 15,
    "final_integrates": 13,
    "downgraded_no_change": audit["books_prewrite_challenge"]["downgraded_no_change"],
    "survivors": SURVIVORS,
    "shared_books_modified": False,
    "next_gate": "root_serial_writeback_then_non_writer_post_write_audit",
}
(ROOT / "books-prewrite-challenge.json").write_text(
    json.dumps(challenge, ensure_ascii=False, indent=2) + "\n"
)

author_queue = (ROOT / "BOOKS_WRITEBACK_QUEUE.md").read_text()
final_queue = author_queue.replace(
    "本文件是 date-local author queue；本 lane **未修改共享 Books**。必须经非作者 fresh-context audit 后，由 root 按日期串行写回并再做 post-write audit。",
    "本文件是 non-author fresh-context challenge 后的最终队列；**未修改共享 Books**。由 root 按日期串行写回，再由非写作者执行 post-write semantic audit。",
).replace("Status: `pending_independent_review`", "Status: `root_writeback_ready`")
(ROOT / "BOOKS_WRITEBACK_QUEUE_FINAL.md").write_text(final_queue)

text = REPORT.read_text()
text = text.replace(
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。Author packet 已闭合；等待非作者 fresh-context audit、root 串行 Books writeback 与 post-write audit。",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。非作者 fresh-context audit 已闭合 coverage/evidence；等待 root 串行 Books writeback 与 post-write audit。",
)
text = re.sub(
    r"## Executive Summary\n\n.*?\n\n## 1\. Coverage",
    "## Executive Summary\n\n相邻月份 v2 snapshot 含 91,841 条 raw records；严格窗口注册 668 条 identity。非作者重放 668/668 title+abstract 后，将 author denominator 29 修复为 56（恢复 27 个 false negative、移除 0 个 false positive），冻结 612 项 family-specific pre-denominator closure。56/56 official exact-v1 已读取，blocked=0、ordinary pending=0。current Books challenge 将 15 项 provisional Integrate 收紧为 13 项 root-writeback-ready queue；共享 Books 尚未写，因此 Completion 仍为 In Progress。\n\n## 1. Coverage",
    text,
    count=1,
    flags=re.S,
)
text = text.replace("| Denominator ID | DEN-20260515-V1-AUTHOR |", "| Denominator ID | DEN-20260515-INDEPENDENT-56 |")
text = text.replace("| Coverage Gate | Open |", "| Coverage Gate | Closed |", 1)
text = text.replace("| Evidence Gate | Open |", "| Evidence Gate | Passed |", 1)
text = text.replace("exact-v1 HTML | checked", "exact-v1 HTML/PDF | checked", 1)
text = re.sub(
    r"## 7\. Semantic Audit\n\n.*?\n\n## 8\. Ignored Noise",
    """## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260515-INDEPENDENT-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260515 | — | 668/668 replay；author denominator 漏收的 27 项均恢复 exact-v1 Review；56 retained / 612 closures；false positive 0 | passed |
| SA-20260515-INDEPENDENT-EVIDENCE | fresh-context:may2026-day01 | evidence | review:SF-2026-ARXIV-2605-14241 | — | 56/56 exact-v1；54 HTML + 2 official PDF；blocked=0、ordinary pending=0 | passed |
| SA-20260515-INDEPENDENT-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-MEMORY-LINEAGE-GATE | — | 三项 narrative 分别覆盖 memory/action、generation/checking、routing/environment ownership transition | passed |
| SA-20260515-BOOKS-PREWRITE | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-14241 | — | 15 项 provisional Integrate 中 14249 与 14591 因 current Books 已完整承载而降为 No Change；13 项进入 `BOOKS_WRITEBACK_QUEUE_FINAL.md` | passed |

独立审计已关闭 Coverage 与 Evidence；Books 仍需 root 串行写回和非写作者 post-write semantic audit。

## 8. Ignored Noise""",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 9\. Recommended Action\n\n.*?\n\n## 10\. Repository Changes",
    "## 9. Recommended Action\n\nroot 按 owner 合并 13 项 final queue 后串行写回共享 Books；随后由非写作者逐项验证正文真实存在、位于首个 Review notes 前、保留旧路径/约束变化/owner/收益代价/failure/fallback/coexistence，才可关闭 Books Gate。\n\n## 10. Repository Changes",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 11\. Open Questions\n\n.*?\n\n## 12\. Sources",
    "## 11. Open Questions\n\n- 13 项 writeback 按 owner 合并后，是否都在正文形成连续演进而非逐论文追加？\n- post-write audit 是否确认目标与相邻章节没有 owner 冲突？\n\n## 12. Sources",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 13\. Final Status\n\n.*\Z",
    "## 13. Final Status\n\nCompletion Status: `In Progress`\n\nCoverage: `Closed`\n\nEvidence: `Passed`\n\nBooks: `Open`\n\nunresolved findings: 1\n\n非作者 fresh-context audit 已完成 668/668 screening、56-family denominator、56/56 exact-v1 Evidence 与 15→13 current-Books challenge；仅剩 root 串行 Books writeback 与 post-write semantic audit。\n",
    text,
    count=1,
    flags=re.S,
)
REPORT.write_text(text)

print(json.dumps({
    "registered": 668,
    "retained": 56,
    "closures": 612,
    "false_negatives": 27,
    "false_positives": 0,
    "exact_v1": 56,
    "blocked": 0,
    "final_books_queue": 13,
    "coverage": "Closed",
    "evidence": "Passed",
    "books": "Open",
}, ensure_ascii=False))
