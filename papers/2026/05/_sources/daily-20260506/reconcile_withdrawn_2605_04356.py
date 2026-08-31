#!/usr/bin/env python3
"""Reconcile withdrawn arXiv:2605.04356v1 as a pre-denominator closure."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
REPORT = REPO / "papers/2026/05/06/README.md"
FAMILY = "SF-2026-ARXIV-2605-04356"
ARXIV_ID = "2605.04356"
OFFICIAL_URL = "https://arxiv.org/abs/2605.04356v1"
RECONCILED_AT = "2026-09-01T14:45:23+08:00"
CLOSURE_REASON = (
    "Identity/date/status closure：official arXiv abs identifies arXiv:2605.04356v1, "
    "submitted 2026-05-05T23:25:00Z, and marks it withdrawn by Joe Benton. The arXiv "
    "admin note states that v1 was removed because the submitter did not have the right "
    "to agree to the license at submission time; the page exposes no license for the "
    f"withdrawn version ({OFFICIAL_URL}). Pre-denominator closure：withdrawn v1 is retained "
    "as an auditable raw identity but is not scored, Source-Reviewed, mapped to a Books "
    "owner, or carried as a blocker. A newly public revision is a new evidence identity "
    "and must be routed by its own first-public time."
)


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def write_json(name: str, value) -> None:
    (ROOT / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


# Preserve the raw identity while moving it below the denominator.
final = load("screening-ledger-final.json")
target = next(item for item in final["identities"] if item["arxiv_id"] == ARXIV_ID)
target["screening_status"] = "pre_denominator_closure"
target["screening_reason"] = CLOSURE_REASON
for key in (
    "source_family_id",
    "owner_node",
    "score_v2",
    "review_status",
    "access_status",
    "integration_disposition",
    "method_locator",
    "evaluation_locator",
    "limitations_locator",
):
    target.pop(key, None)
final["candidate_denominator"] = 63
final["pre_denominator_closures"] = 450
write_json("screening-ledger-final.json", final)
ledger_bytes = (ROOT / "screening-ledger-final.json").read_bytes()
ledger_sha = hashlib.sha256(ledger_bytes).hexdigest()

provisional = load("screening-ledger-provisional.json")
provisional_target = next(
    item for item in provisional["identities"] if item["arxiv_id"] == ARXIV_ID
)
provisional_target["screening_status"] = "pre_denominator_closure"
provisional_target["screening_reason"] = CLOSURE_REASON
write_json("screening-ledger-provisional.json", provisional)

# Regenerate the canonical TSV from the reconciled ledger.
fields = [
    "arxiv_id",
    "title",
    "screening_status",
    "source_family_id",
    "screening_reason",
    "owner_node",
    "review_status",
    "access_status",
    "integration_disposition",
]
with (ROOT / "screening-ledger-final.tsv").open("w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(final["identities"])

# Withdrawn material is not a candidate, so all candidate-stage packets drop it.
for name in (
    "exact-v1-review-packet.json",
    "books-current-content-comparison.json",
    "evidence-provenance-manifest.json",
):
    data = load(name)
    data["items"] = [
        item
        for item in data["items"]
        if item.get("source_family_id") != FAMILY and item.get("arxiv_id") != ARXIV_ID
    ]
    write_json(name, data)

coverage = load("coverage-receipt.json")
coverage.update(
    {
        "retained": 63,
        "pre_denominator_closed": 450,
        "ledger_sha256": ledger_sha,
        "status": "checked",
    }
)
coverage["route"] = (
    "DataCite adjacent-month v2 100-prefix snapshots; 513/513 title+abstract semantic "
    "screen; official exact-v1 HTML/PDF review; official abs withdrawal reconciliation"
)
write_json("coverage-receipt.json", coverage)

author_audit = load("semantic-author-audit.json")
author_audit["checks"].update(
    {
        "candidate_denominator": 63,
        "pre_denominator_closures": 450,
        "closure_reason_unique": 450,
        "exact_v1_complete": 63,
        "blocked": 0,
        "books_compared": 63,
        "withdrawn_identity_closure": 1,
    }
)
author_audit["unresolved_findings"] = []
author_audit["withdrawal_reconciliation"] = {
    "source_identity": "arXiv:2605.04356v1",
    "official_abs_url": OFFICIAL_URL,
    "result": "pre_denominator_closure",
    "candidate_effect": "removed from denominator, Score, Review, Books comparison and blocker state",
}
write_json("semantic-author-audit.json", author_audit)

post = load("post-write-semantic-audit.json")
post["gate"] = {
    "post_write_books_scope": "Passed",
    "report_level_books_gate": "Passed",
    "reason": (
        "27/27 writebacks passed independent post-write semantic audit. All 63 canonical "
        "candidates have complete Evidence/Books dispositions; arXiv:2605.04356v1 is an "
        "auditable withdrawn pre-denominator closure, not an unresolved candidate."
    ),
}
write_json("post-write-semantic-audit.json", post)

marker_plan = load("stable-source-family-marker-repair-plan.json")
marker_plan.pop("scope_exclusion", None)
marker_plan["audit_scope"] = (
    "27 canonical Integrate items in BOOKS_WRITEBACK_QUEUE.md; the withdrawn raw identity "
    "arXiv:2605.04356v1 is a pre-denominator closure and is not part of marker scope"
)
marker_plan["repair_contract"]["invariants"] = [
    entry
    for entry in marker_plan["repair_contract"]["invariants"]
    if FAMILY not in entry and "2605.04356" not in entry
]
marker_plan["execution_order"] = [
    entry
    for entry in marker_plan["execution_order"]
    if FAMILY not in str(entry) and "2605.04356" not in str(entry)
]
marker_plan["withdrawal_reconciliation"] = {
    "source_identity": "arXiv:2605.04356v1",
    "status": "outside_candidate_and_marker_scope",
    "closure_ref": "screening-ledger-final.json#arxiv:2605.04356",
}
write_json("stable-source-family-marker-repair-plan.json", marker_plan)

write_json(
    "withdrawn-family-reconciliation.json",
    {
        "schema": "withdrawn-family-reconciliation-v1",
        "report_date": "2026-05-06",
        "reconciled_at": RECONCILED_AT,
        "raw_identity": "arXiv:2605.04356v1",
        "former_source_family_id": FAMILY,
        "submitted_v1_utc": "2026-05-05T23:25:00Z",
        "official_abs_url": OFFICIAL_URL,
        "official_status": {
            "withdrawn_by": "Joe Benton",
            "admin_note": (
                "This version has been removed by arXiv administrators as the submitter "
                "did not have the right to agree to the license at the time of submission"
            ),
            "license": "No license for this version due to withdrawn",
        },
        "disposition": "pre_denominator_closure",
        "closure_reason": CLOSURE_REASON,
        "count_delta": {
            "candidate_denominator": "64 -> 63",
            "pre_denominator_closures": "449 -> 450",
            "blocked": "1 -> 0",
        },
        "removed_from": [
            "Candidate Ledger and Score V2",
            "Review Completion Receipt and Source Review body",
            "Deep Analysis Selection",
            "Books Comparison",
            "Materials Request",
            "marker repair scope",
        ],
        "retained_in": [
            "raw/provisional identity inventory",
            "canonical screening ledger pre-denominator closure",
            "Daily Ignored Noise closure and Sources",
        ],
        "gate": {
            "completion": "Complete",
            "coverage": "Closed",
            "evidence": "Passed",
            "books": "Passed",
            "ordinary_pending": 0,
            "blockers": 0,
        },
    },
)

# Reconcile the canonical README while preserving the independent audit history.
text = REPORT.read_text(encoding="utf-8")
text = re.sub(
    r"\*\*Status:\*\*.*",
    "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。513/513 screening、63-family denominator、63/63 body-level Review、Books Decision、27 项 writeback/post-write audit 与 withdrawn identity closure 均已闭合；ordinary pending=0、blocker=0。",
    text,
    count=1,
)
text = re.sub(
    r"相邻月份 v2 快照共 .*?27 项 Books writeback 已通过独立 post-write audit。",
    "相邻月份 v2 快照共 91,841 条 raw records；严格窗口注册 513 条 identity。513/513 已逐项完成 title+abstract 语义筛选；root challenge 后分母曾由 31 修正为 64，withdrawal reconciliation 再将 `2605.04356v1` 作为 pre-denominator identity closure，最终分母为 63 项（12.28%），其余 450 项均有 family-specific closure。63/63 项完成 body-level Review，27 项 Books writeback 已通过独立 post-write audit。",
    text,
    count=1,
    flags=re.S,
)
text = text.replace("| Denominator ID | DEN-20260506-V1-FULL-REPLAY |", "| Denominator ID | DEN-20260506-V2-WITHDRAWAL-RECONCILED |")
text = text.replace("| Denominator Frozen At | 2026-09-01T00:45:00+08:00 |", f"| Denominator Frozen At | {RECONCILED_AT} |")
text = text.replace("| Completion Status | Conditional |", "| Completion Status | Complete |")
text = text.replace("| Evidence Gate | Conditional Pass |", "| Evidence Gate | Passed |")
text = text.replace("| Books Gate | Conditional Pass |", "| Books Gate | Passed |")

# Receipt family list is the candidate denominator, not all raw identities.
receipt_lines = text.splitlines()
for index, line in enumerate(receipt_lines):
    if line.startswith("| SRC-ARXIV |"):
        line = line.replace(f";{FAMILY}", "").replace(f"{FAMILY};", "")
        line = re.sub(r"retained=64; closure=449; denominator_sha256=[0-9a-f]{64}", f"retained=63; closure=450; denominator_sha256={ledger_sha}", line)
        line = re.sub(r"screening-ledger-final\.json#sha256:[0-9a-f]{64}", f"screening-ledger-final.json#sha256:{ledger_sha}", line)
        receipt_lines[index] = line
        break
text = "\n".join(receipt_lines) + "\n"

text = re.sub(
    r"<!-- coverage:SRC-ARXIV:20260506:start -->.*?<!-- coverage:SRC-ARXIV:20260506:end -->",
    "<!-- coverage:SRC-ARXIV:20260506:start -->Coverage recall and 513/513 semantic screening are closed. DataCite supports identity/date/abstract only; all 63 denominator families have body-level evidence, including `2605.03275v1` recovered through a matching licensed mirror. official arXiv abs confirms `2605.04356v1` was withdrawn by Joe Benton and administratively removed because the submitter lacked the right to agree to the license; it is therefore an auditable pre-denominator closure rather than a candidate blocker.<!-- coverage:SRC-ARXIV:20260506:end -->",
    text,
    count=1,
    flags=re.S,
)

# Remove all candidate-stage table rows and bounded prose for the withdrawn identity.
text = re.sub(rf"^\| {re.escape(FAMILY)} \|.*\n", "", text, flags=re.M)
for marker in ("review", "analysis-decision", "books-review"):
    text = re.sub(
        rf"\n?<!-- {marker}:{re.escape(FAMILY)}:start -->.*?<!-- {marker}:{re.escape(FAMILY)}:end -->\n?",
        "\n",
        text,
        flags=re.S,
    )

# Remove the withdrawn refs from the four existing semantic-audit rows and update scope truth.
for prefix in ("books-review", "analysis-decision", "review", "claim"):
    token = f"{prefix}:{FAMILY}"
    text = text.replace(f";{token}", "").replace(f"{token};", "")
text = text.replace(
    "513/513 replay 与 449 closure 已在 ROOT_FRESH_CONTEXT_RESOLUTION.md 闭合；分母从 31 修正为 64",
    "513/513 replay 已闭合；withdrawal reconciliation 将分母 64→63、closure 449→450，withdrawn identity 保留 raw 审计轨迹但不进入候选",
)
text = re.sub(
    r"63/64 body-level Review complete；2605\.04356v1 为精确 external revision blocker，普通审阅工作为零",
    "63/63 body-level Review complete；ordinary pending=0、blocker=0",
    text,
)
text = text.replace(
    "64-family eligibility pool 已逐项处置；三项 Deep Analysis 保持互补且其余候选均有明确未入选理由",
    "63-family eligibility pool 已逐项处置；三项 Deep Analysis 保持互补且其余候选均有明确未入选理由",
)
text = text.replace(
    "27/27 writebacks 通过 revision-3 post-write audit；其余 accessible family 已完成 No Change 对读，2605.04356v1 保持 conditional disposition",
    "27/27 writebacks 通过 revision-3 post-write audit；其余 36 个候选完成 No Change 对读；withdrawn identity 不具 Books eligibility",
)

text = text.replace(
    "449 项未进入 Candidate Denominator；逐项机制、证据与可重开条件保存在 `screening-ledger-final.json/tsv`，不是静默丢弃。",
    "450 项未进入 Candidate Denominator；逐项机制、证据与可重开条件保存在 `screening-ledger-final.json/tsv`，不是静默丢弃。\n\n其中 `arXiv:2605.04356v1` 保留为 withdrawal-specific closure：identity/date 为 2026-05-05T23:25:00Z；official arXiv abs 标记 withdrawn by Joe Benton，并说明管理员因提交者当时无权同意许可而移除 v1。该 identity 不评分、不做 Source Review、不映射 Books owner，也不构成 blocker；若新 revision 公开，按其自身 first-public time 和 evidence identity 重新路由。",
)

def replace_section(source: str, number: int, next_number: int, body: str) -> str:
    pattern = rf"(## {number}\. [^\n]+\n\n).*?(?=\n## {next_number}\.)"
    return re.sub(pattern, lambda match: match.group(1) + body.rstrip() + "\n", source, count=1, flags=re.S)

text = replace_section(
    text,
    9,
    10,
    "无剩余动作。63-family Evidence/Books Decision、27 项 Books writeback/post-write audit 与 450 项 pre-denominator closure 均已闭合；withdrawn identity 只保留可审计状态，不再请求已撤回 v1 的全文。",
)
text = replace_section(
    text,
    10,
    11,
    "Author、root writer 与独立 reviewer 的既有修改保持不变；本轮只同步 `papers/2026/05/06` 与 `papers/2026/05/_sources/daily-20260506` 的 withdrawal closure、分母、收据、audit scope 与 Gate 真值。未修改共享 Books，未 stage、commit 或 push。",
)
text = replace_section(
    text,
    11,
    12,
    "- 无阻塞 05-06 Gate 的 Open Question。若该工作以后以新 revision 重新公开，应按新 revision 的 first-public time、许可与 exact-version evidence 重新入场，而不是恢复已撤回 v1 的 candidate 身份。",
)
text = replace_section(
    text,
    12,
    13,
    "- DataCite arXiv v2 month snapshots（identity/date/abstract recovery；accessed 2026-09-01）\n- 62 项 official arXiv exact-v1 HTML/PDF，URL 逐项记录于 Review Completion Receipt（accessed 2026-09-01）\n- `2605.03275v1` licensed full-text recovery receipt（exact title/authors/arXiv DOI reconciliation；accessed 2026-09-01）\n- [official arXiv abs: 2605.04356v1](https://arxiv.org/abs/2605.04356v1)（withdrawn-by、admin removal、submission time 与 license status；rechecked 2026-09-01）",
)

text = text.replace("Completion Status: `Conditional`", "Completion Status: `Complete`")
text = text.replace("Evidence: `Conditional Pass`", "Evidence: `Passed`")
text = text.replace("Books: `Conditional Pass`", "Books: `Passed`")
text = text.replace("unresolved findings: 1", "unresolved findings: 0")
text = re.sub(
    r"513/513 Coverage replay、Selection、63 个 accessible body-level Review.*?不是 `Complete`。",
    "513/513 Coverage replay、63/63 body-level Review、所有 Books Decision 与 27/27 Books writeback 已通过 fresh-context / post-write audit。`2605.04356v1` 已按 official withdrawn 状态从 denominator 与全部 candidate-stage contracts 移除并转为 pre-denominator closure；ordinary pending=0、blocker=0，因此三个 Gate 均已通过。",
    text,
    count=1,
    flags=re.S,
)

REPORT.write_text(text, encoding="utf-8")
print(
    json.dumps(
        {
            "raw": 91841,
            "registered": 513,
            "screened": 513,
            "denominator": 63,
            "closures": 450,
            "reviewed": 63,
            "blocked": 0,
            "ledger_sha256": ledger_sha,
        },
        ensure_ascii=False,
    )
)
