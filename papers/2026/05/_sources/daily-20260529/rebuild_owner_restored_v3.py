#!/usr/bin/env python3
"""Rebuild the bounded 2026-05-29 V3 projection from frozen owner evidence.

This script does not discover sources, change Books, or move events across dates.
It projects the already-reviewed arXiv owner corpus plus the independent Seed
TaskMem event into the current six-section report contract.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
DAY = ROOT / "papers/2026/05/29/README.md"
SRC = ROOT / "papers/2026/05/_sources/daily-20260529"
OWNER_DIR = ROOT / "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260529"
CHECKED_AT = "2026-09-16T18:20:00+08:00"


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head_report() -> str:
    return subprocess.check_output(
        ["git", "show", "HEAD:papers/2026/05/29/README.md"],
        cwd=ROOT,
        text=True,
    )


def table_maps(text: str):
    review = {}
    books = {}
    for line in text.splitlines():
        if not line.startswith("| SF-2026-ARXIV-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 11 and cells[1].startswith("RP-"):
            review[cells[0]] = {
                "review_provenance_id": cells[1],
                "review_route": cells[2],
                "primary_evidence_version": cells[3],
                "reviewed_evidence_versions": cells[4],
                "method_identity_locators": cells[5],
                "evaluation_locators": cells[6],
                "limitations_counterevidence_locators": cells[7],
                "artifact_locators": cells[8],
                "claim_boundary_ref": cells[9],
                "completion_result": cells[10],
            }
        if len(cells) == 9 and cells[2].startswith("books/"):
            books[cells[0]] = {
                "stable_node_id": cells[1],
                "target_chapter_ref": cells[2],
                "adjacent_chapter_refs": cells[3],
                "existing_proposition_ref": cells[4],
                "new_evidence_delta_ref": cells[5],
                "evolution_relation": cells[6],
                "prior_decision": cells[7],
                "books_review_ref": cells[8],
            }
    return review, books


def block(text: str, family: str, kind: str) -> str:
    start = f"<!-- {kind}:{family}:start -->"
    end = f"<!-- {kind}:{family}:end -->"
    if start not in text or end not in text:
        raise RuntimeError(f"missing {kind} block for {family}")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


owner = load(OWNER_DIR / "arxiv-owner-receipt.json")
canonical = load(OWNER_DIR / "canonical-ledger.json")
old = head_report()
review_rows, book_rows = table_maps(old)
candidates = canonical["candidates"]

assert owner["raw_identity_count"] == 823
assert owner["official_oai_direct_count"] == 623
assert owner["revision_recovery_count"] == 200
assert canonical["candidate_count"] == 115
assert canonical["pre_denominator_closure_count"] == 708
assert canonical["withdrawn_pre_denominator_count"] == 0
assert len(candidates) == 115
assert {c["source_family_id"] for c in candidates} == set(review_rows)

taskmem_matches = [
    item
    for item in load(SRC / "evidence-review-v3.json")["items"]
    if item["source_family_id"] == "SF-2026-SEED-TASKMEM"
]
assert len(taskmem_matches) == 1
taskmem_old = taskmem_matches[0]
assert taskmem_old["source_family_id"] == "SF-2026-SEED-TASKMEM"
assert not any(c["arxiv_id"] == "2605.31075" for c in candidates)

def target_path(family: str) -> str | None:
    row = book_rows.get(family)
    return row["target_chapter_ref"].split("#", 1)[0] if row else None


evidence_items = []
books_items = []
applied_items = []

for c in candidates:
    family = c["source_family_id"]
    rr = review_rows[family]
    assert rr["completion_result"] == "complete"
    evidence_items.append(
        {
            "source_family_id": family,
            "title": c["title"],
            "primary_identifier": c["primary_identifier"],
            "first_public_time": "2026-05-29T08:00:00+08:00",
            "owner_route": next(
                x["owner_receipt_route"] for x in owner["identities"] if x["source_family_id"] == family
            ),
            "review_depth": "deep",
            "review_status": "complete",
            "access_status": c["access_status"],
            "score": {
                "design_delta": int(c["design_delta"]),
                "system_reach": int(c["system_reach"]),
                "durability": int(c["durability"]),
                "total": int(c["total"]),
            },
            "stable_node_id": c["stable_node_id"],
            "review_provenance_id": rr["review_provenance_id"],
            "method_identity_locators": rr["method_identity_locators"],
            "evaluation_locators": rr["evaluation_locators"],
            "limitations_counterevidence_locators": rr["limitations_counterevidence_locators"],
            "artifact_locators": rr["artifact_locators"],
            "claim_boundary_ref": rr["claim_boundary_ref"],
            "reused_under_current_contract": True,
            "reuse_basis": "identity, exact-v1 and adopted proposition unchanged; owner receipt corrected without changing mechanism evidence",
        }
    )

    disposition = c["books_disposition"]
    target = target_path(family)
    marker_count = 0
    current_hash = None
    if target:
        target_file = ROOT / target
        assert target_file.exists(), (family, target)
        current_hash = sha256(target_file)
        marker_count = target_file.read_text().count(family)
    if disposition == "Integrate":
        assert target and marker_count >= 1, (family, target, marker_count)
        current_decision = "Applied"
        applied_items.append(
            {
                "source_family_id": family,
                "stable_node_id": c["stable_node_id"],
                "target": target,
                "writeback_status": "applied_existing_binding",
                "binding_marker": family,
                "marker_count": marker_count,
            }
        )
    elif disposition == "No Change — Existing Coverage":
        assert target
        current_decision = disposition
    else:
        assert disposition == "Weekly Only — Context"
        current_decision = "Report Only — Context"
    books_items.append(
        {
            "source_family_id": family,
            "stable_node_id": c["stable_node_id"],
            "target": target,
            "adjacent": book_rows.get(family, {}).get("adjacent_chapter_refs"),
            "current_body_sha256": current_hash,
            "current_marker_count": marker_count,
            "decision": current_decision,
            "prior_books_review_ref": c["books_review_ref"],
            "projection_basis": "current owner/body checked; exact-v1 adopted proposition unchanged",
        }
    )

# TaskMem is an institution event first published before its later arXiv batch.
taskmem_target = ROOT / "books/part-07-agent/77-memory.md"
taskmem_text = taskmem_target.read_text()
assert taskmem_text.count("semantic-body-binding:SF-2026-SEED-TASKMEM:start") == 1
assert taskmem_text.count("semantic-body-binding:SF-2026-SEED-TASKMEM:end") == 1
evidence_items.append(taskmem_old)
books_items.append(
    {
        "source_family_id": "SF-2026-SEED-TASKMEM",
        "stable_node_id": "AGENT-MEMORY",
        "target": "books/part-07-agent/77-memory.md",
        "adjacent": "books/part-07-agent/76-rag.md; books/part-07-agent/78-tool-calling.md",
        "current_body_sha256": sha256(taskmem_target),
        "current_marker_count": 1,
        "decision": "Applied",
        "prior_books_review_ref": "books-comparison-v3.json#SF-2026-SEED-TASKMEM",
        "projection_basis": "paired semantic-body binding checked before Review notes; exact-v1 and adopted proposition unchanged",
    }
)
applied_items.append(
    {
        "source_family_id": "SF-2026-SEED-TASKMEM",
        "stable_node_id": "AGENT-MEMORY",
        "target": "books/part-07-agent/77-memory.md",
        "writeback_status": "applied_existing_paired_binding",
        "binding_marker": "semantic-body-binding:SF-2026-SEED-TASKMEM:start/end",
        "marker_count": 1,
    }
)

assert len(evidence_items) == 116
assert len(books_items) == 116
assert len(applied_items) == 13
assert sum(x["decision"] == "No Change — Existing Coverage" for x in books_items) == 102
assert sum(x["decision"] == "Report Only — Context" for x in books_items) == 1

coverage = {
    "schema": "daily-source-coverage-v3",
    "report_date": "2026-05-29",
    "window": "[2026-05-28T09:00:00+08:00,2026-05-29T09:00:00+08:00)",
    "checked_at": CHECKED_AT,
    "registry_version": "2026-09-07",
    "source_count": 14,
    "sources": [
        {"source_id": "SRC-OPENAI", "basis": "官方 Research 索引/RSS 的窗口内 dated entries", "result": "已检查", "gap": "Rosalind Biodefense 为 AI for Science 暂缓项且无可复用系统机制；日期只到 05-29，隔离在 confirmed raw 外"},
        {"source_id": "SRC-ANTHROPIC", "basis": "官方 Research 索引的窗口内 dated entries", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-GOOGLE-AI", "basis": "DeepMind/Google Research 官方 publication 索引", "result": "受阻", "gap": "两条仅标 2026-05-28 的页面缺时区时刻，无法跨 09:00 边界定 owner"},
        {"source_id": "SRC-META-AI", "basis": "官方 Research/Publications 入口的窗口切片", "result": "受阻", "gap": "稳定的历史日级分页不可重放"},
        {"source_id": "SRC-QWEN", "basis": "官方文章索引与正文语义切片", "result": "已检查", "gap": "窗口附近条目未达到贡献门槛"},
        {"source_id": "SRC-DEEPSEEK", "basis": "官方 Research/News 窗口切片", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-MOONSHOT", "basis": "官方 Kimi Platform Blog 与组织发布切片", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-TENCENT-HUNYUAN", "basis": "官方 Research 全部列表及原始链接", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-ZAI", "basis": "官方 Research、release 与仓库发布切片", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-BYTEDANCE-SEED", "basis": "官方 Research 页嵌入 ArticleMeta 与完整摘要", "result": "已检查", "gap": "TaskMem 官方事件 1 个；与 arXiv:2605.31075 同一 Source Family，不双计"},
        {"source_id": "SRC-BAIDU-ERNIE", "basis": "官方技术博客与仓库发布切片", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-XIAOMI-MIMO", "basis": "官方论文/博客卡片与仓库发布切片", "result": "受阻", "gap": "部分卡片缺少日级时间"},
        {"source_id": "SRC-MINIMAX", "basis": "官方中英文 Blog、Research 与 Agent Tech Blog", "result": "已检查", "gap": "无窗口内可确认事件"},
        {"source_id": "SRC-ARXIV", "basis": "官方 cadence、exact-v1 identity、initial registration 与 OAI owner receipt", "result": "已检查", "gap": "823 identities：623 OAI direct + 200 initial-registration recovery；语义筛选无 pending"},
    ],
    "confirmed_raw_count": 824,
    "coverage_complete_claim": False,
    "coverage_boundary": "Confirmed corpus is closed; Google/Meta/MiMo date/history limitations are terminal reservations and do not support no-omission claims.",
}

screening = {
    "schema": "daily-screening-outcomes-v3",
    "report_date": "2026-05-29",
    "window": coverage["window"],
    "confirmed_raw_count": 824,
    "retained_count": 116,
    "pre_denominator_closure_count": 708,
    "withdrawn_count": 0,
    "conservation": "824 = 116 + 708 + 0",
    "retained_items": [
        {
            "source_family_id": c["source_family_id"],
            "source_id": "SRC-ARXIV",
            "title": c["title"],
            "primary_identifier": c["primary_identifier"],
            "full_abstract_reviewed": True,
            "score": f"{c['design_delta']}+{c['system_reach']}+{c['durability']}={c['total']}",
            "stable_node_id": c["stable_node_id"],
        }
        for c in candidates
    ]
    + [
        {
            "source_family_id": "SF-2026-SEED-TASKMEM",
            "source_id": "SRC-BYTEDANCE-SEED",
            "title": "Task-Focused Memorization for Multimodal Agents",
            "primary_identifier": "official Seed event; arXiv:2605.31075v1 is supporting evidence",
            "full_abstract_reviewed": True,
            "score": "3+2+3=8",
            "stable_node_id": "AGENT-MEMORY",
        }
    ],
    "closure_owner_ref": "../arxiv-owner-replay-20260903/20260529/arxiv-owner-receipt.json",
    "note": "TaskMem is absent from the 823-item arXiv owner batch and is counted once as an official Seed event; its later arXiv identity remains in the same Source Family.",
}

evidence = {
    "schema": "daily-evidence-review-v3",
    "report_date": "2026-05-29",
    "count": 116,
    "deep_complete_count": 116,
    "standard_complete_count": 0,
    "blocked_count": 0,
    "items": evidence_items,
}

books = {
    "schema": "daily-books-comparison-v3",
    "report_date": "2026-05-29",
    "count": 116,
    "applied_count": 13,
    "no_change_count": 102,
    "report_only_count": 1,
    "items": books_items,
}

queue = {
    "schema": "daily-root-books-writeback-queue-v3",
    "report_date": "2026-05-29",
    "status": "all_integrations_applied_pending_another_fresh_nonauthor_review",
    "pending_count": 0,
    "items": applied_items,
    "author_edited_shared_books": False,
    "new_delta_found": False,
}

materials = {
    "schema": "daily-materials-request-v3",
    "report_date": "2026-05-29",
    "items": [
        {
            "request_id": "MR-20260529-GOOGLE-TIMES",
            "priority": "terminal_nonblocking",
            "source_id": "SRC-GOOGLE-AI",
            "affected_count": 2,
            "missing_material": "DeepMind publication 253391 and 252981 official timezone-bearing publication times",
            "reopen_scope": "these two institution events only",
        },
        {
            "request_id": "MR-20260529-META-HISTORY",
            "priority": "terminal_nonblocking",
            "source_id": "SRC-META-AI",
            "affected_count": "unknown",
            "missing_material": "replayable official historical day-level index/page stop for this window",
            "reopen_scope": "Meta source slice for this window only",
        },
        {
            "request_id": "MR-20260529-MIMO-DATES",
            "priority": "terminal_nonblocking",
            "source_id": "SRC-XIAOMI-MIMO",
            "affected_count": "unknown",
            "missing_material": "official day/time metadata for undated research cards that can uniquely bind an event to this window",
            "reopen_scope": "matching MiMo event only",
        },
    ],
}

audit = {
    "schema": "daily-author-adversarial-audit-v3",
    "report_date": "2026-05-29",
    "status": "author_repair_complete_pending_another_fresh_non_author",
    "checks": {
        "window": "pass",
        "source_rows": 14,
        "conservation": "824 = 116 + 708 + 0",
        "arxiv_owner_receipt": "823 = 115 + 708 + 0; 623 OAI direct + 200 initial-registration recovery",
        "identity_uniqueness": "pass; TaskMem/2605.31075 counted once outside the 823 arXiv owner batch",
        "evidence": "116 deep complete",
        "score": "pass",
        "books_projection": "13 Applied + 102 No Change + 1 Report Only; pending queue=0",
        "shared_books_untouched": True,
        "fresh_non_author": "PENDING_AFTER_REPAIR",
    },
}

dump(SRC / "source-coverage-v3.json", coverage)
dump(SRC / "screening-outcomes-v3.json", screening)
dump(SRC / "evidence-review-v3.json", evidence)
dump(SRC / "books-comparison-v3.json", books)
dump(SRC / "root-books-writeback-queue-v3.json", queue)
dump(SRC / "materials-request-v3.json", materials)
dump(SRC / "author-adversarial-audit-v3.json", audit)


def decision_text(item) -> str:
    target = target_path(item["source_family_id"])
    target_link = f"[目标章](../../../../{target})" if target else None
    if item["books_disposition"] == "Integrate":
        return f"整合：{item['stable_node_id']}，{target_link}；已落实"
    if item["books_disposition"] == "No Change — Existing Coverage":
        return f"已有覆盖：{item['stable_node_id']}，{target_link}"
    return "仅报告：实现语境不改变长期知识"


rows = []
for c in candidates:
    rows.append(
        "| [{title}](https://arxiv.org/html/{arxiv}v1) | 2026-05-29T08:00:00+08:00 | "
        "{node}；{d} + {s} + {u} = {total} | 深入完成 | {decision} |".format(
            title=c["title"].replace("|", "\\|"),
            arxiv=c["arxiv_id"],
            node=c["stable_node_id"],
            d=c["design_delta"],
            s=c["system_reach"],
            u=c["durability"],
            total=c["total"],
            decision=decision_text(c),
        )
    )
rows.append(
    "| [Task-Focused Memorization for Multimodal Agents](https://arxiv.org/html/2605.31075v1) | "
    "2026-05-29T00:00:00+08:00 | AGENT-MEMORY；3 + 2 + 3 = 8 | 深入完成 | "
    "整合：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)；已落实 |"
)

reviews_md = []
for c in candidates:
    family = c["source_family_id"]
    content = block(old, family, "review")
    lines = [line for line in content.splitlines() if not line.startswith("Books Decision=")]
    # Remove the old H4; the current contract supplies an exact primary-material H3.
    if lines and lines[0].startswith("#### "):
        lines = lines[1:]
    target = target_path(family)
    if c["books_disposition"] == "Integrate":
        projection = f"**当前 Books 投影。** `Applied` 到 `{c['stable_node_id']}` / `{target}`；当前正文唯一 marker 已核验，未产生新写回。"
    elif c["books_disposition"] == "No Change — Existing Coverage":
        projection = f"**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `{c['stable_node_id']}` / `{target}` 的当前正文，采用命题与 prior comparison 未变。"
    else:
        projection = "**当前 Books 投影。** `Report Only — Context`；该实现语境不改变长期知识，不写入 Books。"
    reviews_md.append(
        f"### [{c['title']}](https://arxiv.org/html/{c['arxiv_id']}v1)\n\n"
        + "\n".join(lines).strip()
        + "\n\n"
        + projection
    )

reviews_md.append(
    """### [Task-Focused Memorization for Multimodal Agents](https://arxiv.org/html/2605.31075v1)

Seed 官方 `ArticleMeta.PublishDate=1779984000000` 对应 `2026-05-29T00:00:00+08:00`；该官方事件拥有本日归属，arXiv v1 是同一 Source Family 的机制证据，不在 823 个本日 arXiv batch identity 中另计。v1 页面在审阅时无 withdrawn 标记。

TaskMem 把 streaming episodic-memory generation 分成两阶段：Phase One 用 RL 优化 fidelity、coherence、non-redundancy、format 与 richness；Phase Two 固定基础策略，对每个 context 采样八个候选，用近期环境问题构造顺序互换的一致 pairwise preference、删除 cycle，再以 DPO 训练轻量 adapter。Recent tasks 只提供 relevance proxy，writer 只提出写入内容；provenance、authorization、conflict 与 durable commit 仍属于 Memory 系统。

作者结果绑定 Qwen3-VL-30B-A3B、VideoMME/EgoLife/EgoTempo、32×80GB GPU 训练与 GPT-4o/Gemini learned judges；GPU 型号、精度、在线 latency/concurrency/SLO 未披露，Phase Two 只有约 100 videos 形成有效偏好对。不能外推为生产 memory、真值判定、semantic/visual memory 或 embodied safety。

**当前 Books 投影。** `Applied` 到 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；paired binding 位于机制正文且早于 Review notes，保留 task adapter drift、future-task forgetting、authority separation 与 general-policy/raw-evidence fallback。"""
)

sources_table = "\n".join(
    f"| {x['source_id']} | {x['basis']} | {x['result']} | {x['gap']} |" for x in coverage["sources"]
)
candidate_rows_md = "\n".join(rows)
reviews_md_text = "\n\n".join(reviews_md)

readme = f"""# Daily Research — 2026-05-29

**规范：** V3

**窗口：** 2026-05-28T09:00:00+08:00 ～ 2026-05-29T09:00:00+08:00

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

> 本页是 owner receipt 恢复后的有界作者投影。作者侧 Gate 已闭合，但修复作者不能验收自己；状态保持进行中，等待另一位 fresh non-author reviewer。

## 1. 结论

本窗确认 824 个唯一 raw Source Family：823 个 arXiv identity 与 1 个 Seed TaskMem 官方事件。当前守恒为 `824 = 116 retained + 708 pre-denominator closure + 0 withdrawn`；arXiv 子集单独为 `823 = 115 + 708 + 0`，由 623 个 OAI direct 与 200 个 initial-registration recovery 组成。116 个候选均完成 Deep Evidence Review；Books 当前投影为 13 个 Applied、102 个 No Change、1 个 Report Only，pending writeback=0。

TaskMem 的 Seed 官方事件早于 `arXiv:2605.31075v1` 的后续论文批次；两者属于同一 Source Family，只计一次。前次 fresh review 发现“只保留 TaskMem、隔离 823 arXiv identities”的 owner 口径与项目权威日期依据冲突；本轮只恢复该冻结 corpus 与既有 exact-v1/adopted-proposition 证据，没有扩来源、日期或修改共享 Books。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{sources_table}

结构化来源与筛选投影见 [`source-coverage-v3.json`](../_sources/daily-20260529/source-coverage-v3.json) 和 [`screening-outcomes-v3.json`](../_sources/daily-20260529/screening-outcomes-v3.json)；arXiv owner 的不可变依据见 [`arxiv-owner-receipt.json`](../_sources/arxiv-owner-replay-20260903/20260529/arxiv-owner-receipt.json)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{candidate_rows_md}

## 4. 证据与知识整合

以下 arXiv 审阅只复用 identity、exact-v1 与 adopted proposition 均未变化的既有证据；owner 日期修正不改变机制结论。结构化 Evidence 与当前 Books 投影见 [`evidence-review-v3.json`](../_sources/daily-20260529/evidence-review-v3.json) 和 [`books-comparison-v3.json`](../_sources/daily-20260529/books-comparison-v3.json)。

{reviews_md_text}

## 5. 缺口与下一步

终态保留项：DeepMind 两条 date-only 页面、Meta 历史日级分页和 MiMo 未标日期卡片无法唯一落入本窗；它们不用于正面证据、Books 或无遗漏断言。定点重开条件：取得对应官方带时区时刻、可重放日级索引或可唯一绑定到本窗的事件材料；触发后只重开命中的来源切片或 Source Family。精确请求见 [`materials-request-v3.json`](../_sources/daily-20260529/materials-request-v3.json)。

作者侧没有剩余可执行扫描、Evidence 或 Books writeback；另一位 fresh non-author reviewer 仍须复核恢复后的 824/116/708/0 算术、115 个复用 exact-v1 review、13 个 Applied marker、102 个当前 No Change 投影、TaskMem 去重与本节隔离边界。

## 6. 复核

复核者：待另一位 fresh non-author reviewer（不得由本轮有界修复作者自签）

结论：未通过（author-side repair 已闭合，fresh semantic Gate pending）

作者检查：窗口、14 个每日来源、owner receipt、守恒、identity uniqueness、116 个 Deep Review、三维评分、Books current-body projection 与空 pending queue 均已核对；未修改共享 Books。前次独立失败记录保留在 [`FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916.md`](../_sources/daily-20260529/FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916.md)，不能冒充本轮通过结论。
"""

DAY.write_text(readme)

checkpoint = {
    "schema": "daily-author-checkpoint-v3",
    "report_date": "2026-05-29",
    "status": "author_repair_complete_pending_another_fresh_non_author",
    "window": coverage["window"],
    "raw": 824,
    "retained": 116,
    "closure": 708,
    "withdrawn": 0,
    "deep": 116,
    "books": {"applied": 13, "no_change": 102, "report_only": 1, "pending": 0},
    "shared_books_edited": False,
    "fresh_non_author_gate": "PENDING_AFTER_REPAIR",
}
dump(SRC / "OWNER_RESTORED_V3_BOUNDED_REPAIR_CHECKPOINT_20260916.json", checkpoint)
print(json.dumps(checkpoint, ensure_ascii=False))
