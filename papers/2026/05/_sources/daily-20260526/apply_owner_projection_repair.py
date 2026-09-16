#!/usr/bin/env python3
"""Apply the bounded 2026-05-26 owner projection and marker-queue repair."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
LOCAL = ROOT / "papers/2026/05/_sources/daily-20260526"
REPORT = ROOT / "papers/2026/05/26/README.md"
MINIMAX_ID = "minimax:sparse-token-forgetting"
MINIMAX_FAMILY = "SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING"
MISSING_SOURCE_MARKER_IDS = {
    "2605.24322",
    "2605.24366",
    "2605.24545",
    "2605.24549",
    "2605.24696",
    "2605.24718",
    "2605.24737",
}
CHECKED_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")


def read_json(name: str) -> dict:
    return json.loads((LOCAL / name).read_text(encoding="utf-8"))


def write_json(name: str, value: dict) -> None:
    (LOCAL / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


owner = read_json("official-owner-batch-evidence-v3.json")
owner["institution_events"] = []
owner["raw_count"] = 263
owner["dedup_count"] = 263
owner["owner_date_correction"] = {
    "excluded_identity": MINIMAX_ID,
    "reason": "official JSON-LD datePublished=2026-05-27T00:00:00Z, owned by the 2026-05-27 report",
    "positive_or_no_hit_use_on_2026_05_26": False,
}
write_json("official-owner-batch-evidence-v3.json", owner)

coverage = read_json("source-coverage-v3.json")
coverage["checked_at"] = CHECKED_AT
for source in coverage["sources"]:
    if source["source_id"] == "SRC-MINIMAX":
        source["basis"] = "official Research/Blog JSON-LD datePublished=2026-05-27T00:00:00Z"
        source["result"] = "checked"
        source["limitation"] = "0 raw in 05-26 window; event is owned by 05-27 at 08:00 BJT"
write_json("source-coverage-v3.json", coverage)

screening = read_json("screening-outcomes-v3.json")
screening["items"] = [item for item in screening["items"] if item["id"] != MINIMAX_ID]
screening.update(
    raw_count=263,
    retained_count=85,
    pre_denominator_closure_count=178,
    withdrawn_count=0,
    arithmetic="263 = 85 retained + 178 pre-denominator closure + 0 withdrawn",
)
assert len(screening["items"]) == 263
assert Counter(item["status"] for item in screening["items"]) == {
    "retained": 85,
    "pre_denominator_closure": 178,
}
write_json("screening-outcomes-v3.json", screening)

evidence = read_json("evidence-review-v3.json")
evidence["items"] = [item for item in evidence["items"] if item["id"] != MINIMAX_ID]
routes = Counter(item["review_route"] for item in evidence["items"])
scores = Counter(str(item["score"]["total"]) for item in evidence["items"])
assert routes == {"deep": 73, "standard": 12}
assert scores == {"8": 49, "9": 15, "6": 12, "7": 9}
evidence.update(
    candidate_count=85,
    deep_count=73,
    standard_count=12,
    blocked_count=0,
    score_distribution=dict(sorted(scores.items())),
)
write_json("evidence-review-v3.json", evidence)

books = read_json("books-comparison-v3.json")
books["items"] = [item for item in books["items"] if item["id"] != MINIMAX_ID]
book_counts = Counter(item["decision"] for item in books["items"])
expected_books = {
    "Applied": 30,
    "Integrate": 7,
    "No Change — Existing Coverage": 41,
    "Structural Candidate": 5,
    "Report Only": 2,
}
assert book_counts == expected_books
books["candidate_count"] = 85
books["counts"] = expected_books
books["arithmetic"] = (
    "85 = 30 Applied + 7 Integrate (root-applied, marker repair pending) + "
    "41 No Change + 5 Structural Candidate + 2 Report Only"
)
books["status"] = "owner_projection_repaired_marker_only_root_queue_pending_then_fresh_review"
books["owner_projection_repair"] = {
    "removed_identity": MINIMAX_ID,
    "correct_owner_report": "2026-05-27",
    "shared_ch29_binding_preserved": True,
    "shared_books_modified_by_repair_author": False,
}
write_json("books-comparison-v3.json", books)

queue = read_json("root-books-writeback-queue-v3.json")
queue["items"] = [item for item in queue["items"] if item["id"] != MINIMAX_ID]
for item in queue["items"]:
    if item["id"] in MISSING_SOURCE_MARKER_IDS:
        source_family = item["source_family_id"]
        item["status"] = "marker_only_repair_pending_root"
        item["serialized_anchor"] = (
            f"insert `{item['binding_marker']}` immediately after "
            f"`<!-- semantic-body-binding:{source_family}:end -->` and before the main `## Review notes`"
        )
        item["required_narrative"] = (
            "Marker-only repair: keep the existing semantic body unchanged; do not duplicate the mechanism."
        )
        item["marker_only_repair"] = True
    else:
        item["status"] = "postwrite_semantic_review_passed_pending_different_fresh_date_reviewer"
        item["marker_only_repair"] = False

assert len(queue["items"]) == 16
assert Counter(item["status"] for item in queue["items"]) == {
    "postwrite_semantic_review_passed_pending_different_fresh_date_reviewer": 9,
    "marker_only_repair_pending_root": 7,
}
queue.update(
    status="marker_only_repair_pending_root_then_different_fresh_date_reviewer",
    item_count=16,
    applied_pending_fresh_review_count=9,
    pending_root_serial_write_count=0,
    marker_only_repair_pending_root_count=7,
    postwrite_semantic_review_passed_count=9,
    semantic_body_present_count=16,
    paired_semantic_marker_passed_count=16,
    review_receipt="DATE_LOCAL_REPAIR_CHECKPOINT_20260916.md",
)
write_json("root-books-writeback-queue-v3.json", queue)

materials = read_json("materials-request-v3.json")
materials["note"] = (
    "No material blocker. MiniMax owner date was resolved by official JSON-LD to 2026-05-27; "
    "seven marker-only root actions remain and require no new evidence."
)
write_json("materials-request-v3.json", materials)

audit = read_json("author-adversarial-audit-v3.json")
audit["status"] = "bounded_owner_repair_complete_marker_only_root_queue_pending_then_fresh_review"
audit["checks"]["official_owner_batch"] = "passed after repair: 263 official arXiv announcement identities"
audit["checks"]["institution_event_dedup"] = (
    "passed after repair: MiniMax official JSON-LD belongs to 05-27 and is excluded from 05-26"
)
audit["checks"]["books"] = (
    "16 semantic bodies present with paired markers; 9 source-family markers present and "
    "7 marker-only repairs queued to root; repair author did not edit shared Books"
)
audit["checks"]["independence"] = (
    "open: this reviewer became the bounded repair author; a different fresh non-author reviewer is required"
)
audit["arithmetic"] = {
    "raw": "263=263+0",
    "denominator": "263=85+178+0",
    "evidence": "85=73+12+0",
    "score": "85=12+9+49+15",
    "books": "85=30+7+41+5+2",
    "actions": "16=9 marker-complete + 7 marker-only root repair",
}
write_json("author-adversarial-audit-v3.json", audit)

text = REPORT.read_text(encoding="utf-8")
lines = text.splitlines()
updated = []
for line in lines:
    if line.startswith("旧 V2.1 `Complete`、1208 raw"):
        line = (
            "旧 V2.1 `Complete`、1208 raw 与 170 candidates 不再拥有当前状态。当前 first-public owner "
            "仅为 2026-05-26 08:00 BJT 的 263 项 arXiv official announcement batch；MiniMax 技术页官方 "
            "JSON-LD `datePublished=2026-05-27T00:00:00Z` 属 05-27，不进入本日正面或 no-hit 投影。"
            "全日守恒为 **263 = 85 retained + 178 pre-denominator closure + 0 withdrawn**。"
        )
    elif line.startswith("Evidence 为 **86 = 74 deep complete"):
        line = (
            "Evidence 为 **85 = 73 deep complete + 12 standard complete + 0 blocked**；评分分布为 "
            "`{6: 12, 7: 9, 8: 49, 9: 15}`。Books 对账为 **85 = 30 Applied + 7 Integrate（正文已由 root "
            "写入，marker-only repair pending）+ 41 No Change + 5 Structural Candidate + 2 Report Only**。"
            "48 项 date-local comparison repair 的 disposition 未变；16 个 05-26 semantic body 与 paired marker "
            "存在，其中 9 项独立 `source-family` marker 完整，7 项只需 root 补 marker、不重复机制。"
            "本轮已成为 bounded repair author，状态保持 Ongoing，待 root marker-only 修复与另一名 fresh reviewer。"
        )
    elif line.startswith("| SRC-MINIMAX |"):
        line = (
            "| SRC-MINIMAX | official Research/Blog JSON-LD `datePublished=2026-05-27T00:00:00Z` | "
            "已检查 | 05-26 window 为 0 raw；事件由 05-27 08:00 BJT owner |"
        )
    elif line.startswith("完整 owner 与 event receipt"):
        line = line.replace("264 条逐项结果", "263 条逐项结果")
    elif line.startswith("| [minimax:sparse-token-forgetting"):
        continue
    elif line.startswith("1. 由另一名 fresh non-author reviewer"):
        line = (
            "1. 由另一名 fresh non-author reviewer 复核 263 owner identities、178 closure、85 Evidence/Books "
            "以及 48 项具体 comparison；本轮 repair author 不得自签 Complete。"
        )
    elif line.startswith("2. 复用 [`root-books-writeback-queue-v3.json`]"):
        line = (
            "2. root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260526/root-books-writeback-queue-v3.json) "
            "只为 7 个既有 semantic block 补精确 `source-family` marker；不得重复正文机制。"
        )
    elif line.startswith("3. 最终 reviewer 仍须独立挑战"):
        line = (
            "3. root marker-only repair 后，另一名 fresh reviewer 复核 16/16 marker/位置、retained FP 与 closure FN；"
            "MiniMax 只在 05-27 owner 投影中保留。"
        )
    elif line.startswith("Date-local repair Gate 已完成："):
        line = (
            "Date-local bounded repair 已完成：MiniMax 05-26 owner 投影已移除，算术重冻为 "
            "`263 raw / 85 retained / 178 closure / 0 withdrawn`；48/48 comparison disposition 保持不变；"
            "16 个 semantic body 的 paired marker 与 Review-notes 前位置存在，7 个独立 `source-family` marker "
            "已进入 root marker-only queue。共享 Books 未由本作者修改，状态保持 Ongoing，等待 root 与另一 fresh reviewer。"
        )
    updated.append(line)

text = "\n".join(updated) + "\n"
review_start = text.find(
    '\n### [minimax:sparse-token-forgetting Why Can\'t the MiniMax LLM Say "Ma Jiaqi"?'
)
if review_start >= 0:
    review_end_marker = "<!-- review:SF-2026-MINIMAX-SPARSE-TOKEN-FORGETTING:end -->"
    review_end = text.index(review_end_marker, review_start) + len(review_end_marker)
    text = text[:review_start] + text[review_end:]
REPORT.write_text(text, encoding="utf-8")

author_checkpoint = f"""# 2026-05-26 V3 Author Recertification Checkpoint

状态：Ongoing；bounded owner repair complete，等待 root marker-only repair 与不同 fresh non-author 最终 Gate。

## 冻结结果

- owner/raw：263 = 263 arXiv official-announcement identities + 0 institutional event；MiniMax 官方 JSON-LD 属 05-27。
- denominator：263 = 85 retained + 178 pre-denominator closure + 0 withdrawn。
- Evidence：85 = 73 deep complete + 12 standard complete + 0 blocked；score={{6:12, 7:9, 8:49, 9:15}}。
- Books：85 = 30 Applied + 7 Integrate + 41 No Change + 5 Structural Candidate + 2 Report Only。
- action：16 个 existing semantic body 与 paired marker 均存在；9 个 source-family marker 完整，7 个 marker-only root repair pending。
- 共享 Books 未由 repair author 修改；Ch29 MiniMax binding 由 05-27 owner 保留。

## 精确剩余 Gate

1. root 只补 queue 中 7 个 `source-family` marker，不重复机制正文。
2. 不同 fresh reviewer 复核 263 owner/window、178 closure FN、85 retained FP/Evidence/Books、48 项 comparison 与 16 项 binding。
3. 只有该 fresh reviewer 可将 README 改为 Complete。

生成时间：{CHECKED_AT}
"""
(LOCAL / "AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260915.md").write_text(
    author_checkpoint, encoding="utf-8"
)

date_local_checkpoint = f"""# 2026-05-26 V3 date-local bounded repair checkpoint

## Role

本轮由 fresh FAIL reviewer 转为 bounded repair author，只修已确认的 MiniMax owner 投影与 7 个缺失 marker 的 root queue；未修改共享 Books，不得自签 Complete。

## Frozen arithmetic

- Window：`[2026-05-25T09:00:00+08:00, 2026-05-26T09:00:00+08:00)`。
- Screening：`263 = 85 retained + 178 closure + 0 withdrawn`。
- Evidence：`85 = 73 deep + 12 standard + 0 blocked`；score `{{6:12, 7:9, 8:49, 9:15}}`。
- Books：`85 = 30 Applied + 7 Integrate + 41 No Change + 5 Structural Candidate + 2 Report Only`。
- Actions：`16 = 9 marker-complete + 7 marker-only root repair pending`。

## Owner repair

MiniMax `datePublished=2026-05-27T00:00:00Z`，即 05-27 08:00 BJT；已从 05-26 raw、retained、Evidence、Books 与 action 投影删除。Ch29 现有 binding 不删除，由 05-27 owner 继续承担。

## Marker-only root queue

`2605.24322`, `2605.24366`, `2605.24545`, `2605.24549`, `2605.24696`, `2605.24718`, `2605.24737` 的 semantic body、paired marker 与 Review-notes 前位置均已存在；root 仅需在各自 `:end` 后补 queue 声明的独立 `source-family` marker，不得重复机制正文。

## Remaining Gate

状态保持 **Ongoing**。root 完成 7 个 marker-only action 后，由另一名 fresh non-author reviewer 对修后 owner、FP/FN、Evidence、Books comparison 与 16 个 binding 做最终 Gate。

生成时间：{CHECKED_AT}
"""
(LOCAL / "DATE_LOCAL_REPAIR_CHECKPOINT_20260916.md").write_text(
    date_local_checkpoint, encoding="utf-8"
)

print(
    json.dumps(
        {
            "raw": 263,
            "retained": 85,
            "closure": 178,
            "evidence": {"deep": 73, "standard": 12, "blocked": 0},
            "books": expected_books,
            "actions": {"total": 16, "marker_complete": 9, "marker_only_root_pending": 7},
        },
        ensure_ascii=False,
    )
)
