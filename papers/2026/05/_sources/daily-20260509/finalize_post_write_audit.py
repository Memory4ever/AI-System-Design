#!/usr/bin/env python3
"""Project the 2026-05-09 independent reconciliation and Books post-write audit.

This script only updates date-local research artifacts. It never edits Books.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parents[1] / "09" / "README.md"
LEDGER = json.loads((ROOT / "screening-ledger-independent-final.json").read_text())
AUDIT_PATH = ROOT / "independent-semantic-audit.json"
AUDIT = json.loads(AUDIT_PATH.read_text())
POST_PATH = ROOT / "post-write-semantic-audit.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: object) -> None:
    encoded = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
    path.write_bytes(encoded)
    path.with_suffix(path.suffix + ".sha256").write_text(hashlib.sha256(encoded).hexdigest() + "\n")


retained = [row for row in LEDGER["identities"] if row["screening_status"] == "retained"]
blocked = [row for row in retained if row["review_status"] == "blocked"]
accessible = [row for row in retained if row["review_status"] != "blocked"]
assert len(retained) == 83 and len(blocked) == 17 and len(accessible) == 66

text = REPORT.read_text()
text = re.sub(
    r"\*\*Status:\*\*.*",
    "**Status:** In Progress；Coverage=Closed、Evidence=Conditional Pass、Books=Open。独立 coverage/evidence/selection challenge 与 3 项 Books 写回后审计已完成；17 项 exact-v1 blocker 中仍有 3 项等待恢复后 Books Decision。",
    text,
    count=1,
)
text = re.sub(
    r"## Executive Summary\n\n.*?\n\n## 1\. Coverage",
    "## Executive Summary\n\n相邻月份 v2 snapshot 含 91,841 条 raw records；严格窗口注册 834 条 identity，834/834 完成 title+abstract 独立语义复核。最终 denominator 为 83 项（9.95%），751 项以 family-specific closure 在分母前闭合；66 项 exact-v1 Review 完成，17 项保留精确 Materials Request。current-content challenge 将 21 项 evidence-complete provisional Integrate 收紧为 3 项，并合并写入 `TRAIN-DISTRIBUTED-TRAINING`；非写作者已确认 3/3 source trace、main-body 位置、owner 唯一性及 trade-off/failure/fallback。\n\n## 1. Coverage",
    text,
    count=1,
    flags=re.S,
)
for old, new in {
    "| Denominator ID | DEN-20260509-AUTHOR-84 |": "| Denominator ID | DEN-20260509-INDEPENDENT-83 |",
    "| Denominator Frozen At | 2026-09-01T03:20:00+08:00 |": "| Denominator Frozen At | 2026-09-01T17:20:00+08:00 |",
    "| Coverage Gate | Open |": "| Coverage Gate | Closed |",
    "| Evidence Gate | Open |": "| Evidence Gate | Conditional Pass |",
}.items():
    text = text.replace(old, new, 1)

families = ";".join(row["source_family_id"] for row in retained)
receipt = (
    "| SRC-ARXIV | 2026-05-08T09:00:00+08:00 | 2026-05-09T09:00:00+08:00 | "
    "2026-09-01T17:20:00+08:00 | DataCite v2 prefixes 00..99 + independent 834/834 semantic replay + exact-v1 | checked | 834 | "
    f"{families} | pages=100; final_cursor=end; raw=91841; registered=834; screened=834; retained=83; closure=751 | "
    "2026-05-09T00:59:59Z | screening-ledger-independent-final.json#sha256="
    f"{digest(ROOT / 'screening-ledger-independent-final.json')} | GAP-EXACT-V1-17 |"
)
text = re.sub(r"\| SRC-ARXIV \| 2026-05-08T09:00:00\+08:00 .*?\n", receipt + "\n", text, count=1)
text = re.sub(
    r"<!-- coverage:SRC-ARXIV:20260509:start -->.*?<!-- coverage:SRC-ARXIV:20260509:end -->",
    "<!-- coverage:SRC-ARXIV:20260509:start -->独立 reviewer 已重放 834/834 screening：4 个 author false positive 降回分母前 closure，3 个 false negative 提升进入 denominator，最终 83 retained / 751 closures。Coverage 已关闭；17 项 exact-v1 blocker 只保持 Evidence 与对应 Books Decision 未闭合，并在 MATERIALS_REQUEST.md 逐项列出。<!-- coverage:SRC-ARXIV:20260509:end -->",
    text,
    count=1,
    flags=re.S,
)

candidate_header = """<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"""
candidate_rows = []
for row in retained:
    aid = row["arxiv_id"]
    sf = row["source_family_id"]
    score = row["score_v2"]
    review_ref = f"materials-request:{sf}" if row["review_status"] == "blocked" else f"review:{sf}"
    override = "exact_v1_required" if row["review_status"] == "blocked" else "none"
    candidate_rows.append(
        f"| {sf} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W19 | 2026-05-09 | SRC-ARXIV | "
        f"{score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | "
        f"{row['review_status']} | {row['access_status']} | {override} | {review_ref} | self | — | new_in_window | "
        f"{row['owner_node']} | {row['integration_disposition']} | books-review:{sf} | no |"
    )
candidate_section = candidate_header + "\n" + "\n".join(candidate_rows)
text = re.sub(
    r"<!-- validator:candidate-ledger-v2\.1 -->.*?\n\n## 3\. Review Completion Receipt",
    candidate_section + "\n\n## 3. Review Completion Receipt",
    text,
    count=1,
    flags=re.S,
)

# Keep actual accessible receipts, remove false positives, and make every blocked
# family explicit rather than preserving generic author locators as complete.
receipt_match = re.search(
    r"(<!-- validator:review-completion-v1 -->\n\| Source Family ID .*?\n\| --- .*?\n)(.*?)(\n\n## 4\.)",
    text,
    flags=re.S,
)
assert receipt_match
existing = {
    line.split(" | ", 1)[0].removeprefix("| "): line
    for line in receipt_match.group(2).splitlines()
    if line.startswith("| SF-")
}
review_rows = []
for row in retained:
    sf = row["source_family_id"]
    aid = row["arxiv_id"]
    if row["review_status"] != "blocked" and sf in existing:
        review_rows.append(existing[sf])
    elif row["review_status"] == "blocked":
        review_rows.append(
            f"| {sf} | RP-BLOCKED-{aid.replace('.', '')} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | "
            f"exact-v1 Method locator unavailable | exact-v1 Evaluation locator unavailable | exact-v1 Limitations locator unavailable | "
            f"artifact scope Not Audited | materials-request:{sf} | blocked |"
        )
assert len(review_rows) == 83
text = text[: receipt_match.start(2)] + "\n".join(review_rows) + text[receipt_match.end(2) :]

# Synchronize the 21 evidence-complete prewrite decisions in their report-local
# Books comparison blocks. Blocked families remain Blocked / Unverified.
decisions = json.loads((ROOT / "books-prewrite-challenge.json").read_text())["decisions"]
for decision in decisions:
    sf = decision["source_family_id"]
    start = f"<!-- books-review:{sf}:start -->"
    end = f"<!-- books-review:{sf}:end -->"
    a = text.find(start)
    b = text.find(end, a)
    if a >= 0 and b >= 0:
        block = text[a:b]
        block = re.sub(r"Decision: `[^`]+`", f"Decision: `{decision['final_disposition']}`", block)
        text = text[:a] + block + text[b:]

semantic = """<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260509-INDEPENDENT-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260509 | 4 false positives；3 false negatives | denominator 84→83；751 family-specific closures | passed |
| SA-20260509-INDEPENDENT-EVIDENCE | fresh-context:may2026-day02 | evidence | independent-semantic-audit.json | 17 exact-v1 bodies unresolved | precise Materials Requests；不以 abstract 代替全文 | conditional_pass |
| SA-20260509-INDEPENDENT-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | independent-semantic-audit.json | author selection challenged | reconciled denominator、owner 与 Score V2 已物化 | passed |
| SA-20260509-INDEPENDENT-BOOKS-PREWRITE | fresh-context:may2026-day02 | books | books-prewrite-challenge.json | 21 provisional Integrates over-retained | 3 Integrate；18 No Change | passed |
| SA-20260509-BOOKS-POSTWRITE | fresh-context:may2026-day02 | books | post-write-semantic-audit.json | 0 | 3/3 trace、owner、正文演进与相邻章去重通过 | passed |"""
text = re.sub(
    r"<!-- validator:semantic-audit-v1 -->.*?\n\n## 8\. Ignored Noise",
    semantic + "\n\n## 8. Ignored Noise",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"750 项 family-specific pre-denominator closure.*",
    "751 项 family-specific pre-denominator closure 位于 `../_sources/daily-20260509/screening-ledger-independent-final.json`；它们保留真实 title、abstract、方法/结果摘要与排除边界。",
    text,
    count=1,
)
text = re.sub(
    r"## 9\. Recommended Action\n\n.*?\n\n## 10\.",
    "## 9. Recommended Action\n\n仅继续恢复 MATERIALS_REQUEST.md 中 17 项 official exact-v1；恢复后完成对应 Source Review，并只重开真正受影响的 Books Decision。3 项已写回 family 不再重复写入。\n\n## 10.",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 11\. Open Questions\n\n.*?\n\n## 12\. Sources",
    "## 11. Open Questions\n\n- 17 项 exact-v1 blocker 中，哪些能由 official HTML/PDF 恢复？\n- 3 项新提升 false negative 在全文恢复后是否仍满足 Candidate 与 Books Gate？\n\n## 12. Sources",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r"## 13\. Final Status\n\n.*\Z",
    "## 13. Final Status\n\nCompletion Status: `In Progress`\n\nCoverage: `Closed`\n\nEvidence: `Conditional Pass`\n\nBooks: `Open`\n\nunresolved findings: 17\n\nCoverage 与 3 项 evidence-complete Books 写回已闭合；17 项 exact-v1 Evidence blocker 中 3 项还需要在恢复全文后完成 Books Decision，因此不得宣称本日 Complete。\n",
    text,
    flags=re.S,
)
REPORT.write_text(text)

AUDIT["gate_result"].update(
    books="Open",
    completion="In Progress",
    reason=(
        "Coverage is Closed on the independently reconciled 834-row screen. Evidence remains Conditional Pass because "
        "17 exact-v1 bodies are blocked with precise Materials Requests. The three evidence-complete Books deltas were "
        "written by root and passed independent post-write audit; Books remains Open only for the three reopened blocked families."
    ),
)
AUDIT["unresolved_findings"] = [
    finding
    for finding in AUDIT["unresolved_findings"]
    if "Root serial Books writeback" not in finding and "Project the independent denominator" not in finding
]
AUDIT["post_write_audit_ref"] = "post-write-semantic-audit.json"
write_json(AUDIT_PATH, AUDIT)
POST_PATH.with_suffix(POST_PATH.suffix + ".sha256").write_text(digest(POST_PATH) + "\n")
print("05-09 projected: 834/834, 83 retained, 751 closure, 66 reviewed, 17 blocked; Books post-write 3/3 passed")
