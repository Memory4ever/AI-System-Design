#!/usr/bin/env python3
"""Rebuild 2026-05-29 through 2026-05-31 under the current V3 contract.

The script only writes date-local Daily reports and date-local evidence.  It
never edits shared Books; an Integrate decision is emitted as a root writeback
queue item for ordered application by the coordinating agent.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = ROOT / "papers/2026/05/_sources"
OWNER_RECEIPT = SOURCE_ROOT / "arxiv-owner-replay-20260903/20260529/arxiv-owner-receipt.json"
CHECKED_AT = "2026-09-16T16:40:00+08:00"
REGISTRY_VERSION = "2026-09-07"
TASKMEM_ID = "SF-2026-SEED-TASKMEM"
TASKMEM_OFFICIAL = "https://seed.bytedance.com/en/research"
TASKMEM_ARXIV = "https://arxiv.org/html/2605.31075v1"
TASKMEM_ARTIFACT = "https://github.com/ByteDance-Seed/TaskMem"
TASKMEM_OFFICIAL_HASH = "05996de773d8655e6c4ec86a9a1f25206efe6f2cf42c788d19ce8f57e8841f82"
TASKMEM_ARXIV_HASH = "29fe80bbb5748c7519bb397a4d6291f5e0d330b7788273992d8e2d8fd441317c"


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


receipt = json.loads(OWNER_RECEIPT.read_text())
ambiguous = sorted(receipt["identities"], key=lambda item: item["arxiv_id"])
assert len(ambiguous) == 823
assert len({item["arxiv_id"] for item in ambiguous}) == 823


COMMON_SOURCES = [
    ("SRC-OPENAI", "官方 Research 索引/RSS 的窗口内 dated entries", "已检查", "无窗口内可确认事件"),
    ("SRC-ANTHROPIC", "官方 Research 索引的窗口内 dated entries", "已检查", "无窗口内可确认事件"),
    ("SRC-GOOGLE-AI", "DeepMind/Google Research 官方 publication 索引", "已检查", "无确定候选；05-28 的两条 date-only 页面在 05-29 单独隔离"),
    ("SRC-META-AI", "官方 Research/Publications 入口的窗口切片", "受阻", "稳定的历史日级分页不可重放，不支持全量无遗漏断言"),
    ("SRC-QWEN", "官方文章索引与正文语义切片", "已检查", "窗口附近产品/使用指南不满足长期机制贡献门槛"),
    ("SRC-DEEPSEEK", "官方 Research/News 窗口切片", "已检查", "无窗口内可确认事件"),
    ("SRC-MOONSHOT", "官方 Kimi Platform Blog 与组织发布切片", "已检查", "无窗口内可确认事件"),
    ("SRC-TENCENT-HUNYUAN", "官方 Research“全部”列表及原始链接", "已检查", "无窗口内可确认事件"),
    ("SRC-ZAI", "官方 Research、release 与仓库发布切片", "已检查", "无窗口内可确认事件"),
    ("SRC-BYTEDANCE-SEED", "官方 Research 页嵌入 ArticleMeta 与完整摘要", "已检查", "TaskMem 只归属 05-29；其余两天无窗口事件"),
    ("SRC-BAIDU-ERNIE", "官方技术博客与仓库发布切片", "已检查", "无窗口内可确认事件"),
    ("SRC-XIAOMI-MIMO", "官方论文/博客卡片与仓库发布切片", "受阻", "部分卡片缺少日级时间，不支持全量无遗漏断言"),
    ("SRC-MINIMAX", "官方中英文 Blog、Research 与 Agent Tech Blog", "已检查", "无窗口内可确认事件"),
    ("SRC-ARXIV", "官方 announcement cadence 与可重放 membership", "已检查", "05-29 membership 受阻；05-30/31 无计划公告批次"),
]

OPENAI_AI_FOR_SCIENCE_CLOSURE = {
    "title": "Strengthening societal resilience with Rosalind Biodefense",
    "source_id": "SRC-OPENAI",
    "url": "https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/",
    "displayed_date": "2026-05-29",
    "status": "pre_denominator_out_of_scope",
    "reason": "Biodefense/life-science application and access-program announcement; AI for Science is explicitly deferred by the current ROADMAP/source contract and the page does not disclose a reusable AI-system mechanism delta.",
    "date_resolution": "not_required_after_scope_closure",
}


TASKMEM_EVIDENCE = {
    "source_family_id": TASKMEM_ID,
    "title": "Task-Focused Memorization for Multimodal Agents",
    "review_depth": "deep",
    "review_status": "complete",
    "access_status": "accessible",
    "primary_sources": [TASKMEM_OFFICIAL, TASKMEM_ARXIV, TASKMEM_ARTIFACT],
    "official_owner": {
        "field": "ArticleMeta.PublishDate",
        "raw_value": 1779984000000,
        "utc": "2026-05-28T16:00:00Z",
        "asia_shanghai": "2026-05-29T00:00:00+08:00",
        "official_page_sha256_at_review": TASKMEM_OFFICIAL_HASH,
        "note": "Official Seed publication time owns the Daily; arXiv submitted/announced time does not override it.",
    },
    "withdrawal_check": "arXiv v1 abstract page exposes normal submission history and no withdrawn notice at review time",
    "method": {
        "problem": "Streaming multimodal observations exceed a durable memory budget; a writer must choose what remains useful for future tasks, not merely produce faithful summaries.",
        "old_baseline": "Fixed prompts or SFT can generate episodic summaries but do not explicitly optimize global fidelity/non-redundancy or adapt the write focus to the environment's changing task distribution.",
        "mechanism": "Phase One uses group-based RL rewards for fidelity, coherence, non-redundancy, formatting and richness. Phase Two freezes the base policy, samples eight candidate memories per context, derives pairwise task-relevance preferences from recent environment questions, removes inconsistent/cyclic comparisons, and DPO-tunes a lightweight adapter.",
        "state_and_control": "The environment's recent-question set defines task demand; a task adapter changes the memorization proposal policy. Durable memory authority, provenance, conflict handling, consent and commit remain outside the learned policy.",
        "implementation": "Qwen3-VL-30B-A3B; Phase One GSPO batch 32/mini-batch 8 on 32 80GB GPUs; Phase Two DPO batch/mini-batch 64 on 32 80GB GPUs; N=8 candidate memories, only 29.17% sampled contexts form valid preference pairs, covering about 100 videos.",
    },
    "evaluation_contract": {
        "workload": "Streaming reformulations of VideoMME short/medium (600 videos, 1,800 QA), EgoLife (500 VQA) and EgoTempo (500 VQA); answers consume generated memory without raw video.",
        "model": "Qwen3-VL-30B-A3B memorization policy; GPT-4o answer generator in main evaluation; Gemini-2.5-Pro robustness check on VideoMME.",
        "hardware": "32 GPUs with 80GB memory for each reported training phase; GPU model and interconnect Not Disclosed.",
        "precision": "Not Disclosed",
        "length": "Four recent 10-second clips plus a new 10-second clip per step for the base protocol; memory token budget exists but headline comparison does not disclose a single universal length.",
        "batch": "Phase One 32 (mini 8); Phase Two 64 (mini 64)",
        "concurrency": "Not Disclosed",
        "slo": "Not Applicable; offline author benchmark",
        "evaluator": "GPT-4o/Gemini-2.5-Flash learned judges plus deterministic length checks; order-swapped pairwise task relevance; GPT-4o main QA with a Gemini-2.5-Pro robustness slice.",
        "reported_result": "Against Qwen3-VL-30B-A3B, author reports +6.3/+7.0/+5.3 accuracy points on VideoMME/EgoLife/EgoTempo; VideoMME gain remains +5.6 with Gemini-2.5-Pro answer generation.",
    },
    "proved": [
        "Within the reported streaming VQA protocol, the two-phase policy improves the specified memory-only QA measurements over the listed baselines.",
        "Matched task adapters outperform mismatched counting/OCR/attribute adapters on the object-recognition test, supporting task-specific rather than universal adaptation in that slice.",
    ],
    "not_proved": [
        "No production authorization, concurrent update, privacy, correction, deletion or durable commit semantics are evaluated.",
        "Recent questions and learned judges are proxies, not truth authority or causal proof that a memory item will help every future task.",
        "The paper covers episodic text memory from video, not semantic/visual memory or interactive embodied deployment; authors list those as future work.",
        "No independent replication, tail latency, online SLO, long-term adapter drift or adversarial poisoning result is provided.",
    ],
    "tradeoffs": [
        "Task-conditioned writes can raise useful recall under a stable local task distribution, but add adapter lifecycle, reward/judge coupling, rollout-cache staleness and distribution-drift risks.",
        "Task-specific focus can omit future-relevant evidence; the Phase One fidelity policy, raw evidence retention and deterministic write gates remain necessary fallbacks.",
    ],
    "evidence_hashes": {
        "official_seed_page": TASKMEM_OFFICIAL_HASH,
        "arxiv_html_v1": TASKMEM_ARXIV_HASH,
    },
}


def source_rows_for(date: str):
    rows = []
    for source_id, basis, result, gap in COMMON_SOURCES:
        result_text = result
        gap_text = gap
        if source_id == "SRC-BYTEDANCE-SEED":
            if date == "2026-05-29":
                gap_text = "命中 TaskMem 1 个官方事件并完成深审；arXiv 链接作为正文证据，不改变官方 owner"
            else:
                gap_text = "TaskMem 官方时间已归 05-29；本窗未发现其他可确认事件"
        if source_id == "SRC-OPENAI" and date == "2026-05-29":
            gap_text = "May 29 Rosalind Biodefense 公告按 AI for Science 暂缓与未披露可复用系统机制在 pre-denominator 关闭；无候选"
        if source_id == "SRC-GOOGLE-AI" and date != "2026-05-29":
            gap_text = "无窗口内可确认事件"
        if source_id == "SRC-ARXIV":
            if date == "2026-05-29":
                result_text = "受阻"
                gap_text = "官方 schedule 证明 08:00 BJT 有公告，但 823 个旧 identity 缺官方逐项 membership，全部隔离在 confirmed raw 之外"
            else:
                gap_text = "官方 schedule 证明该周末窗口没有公告批次"
        rows.append({"source_id": source_id, "basis": basis, "result": result_text, "gap": gap_text})
    return rows


def render_source_rows(rows):
    return "\n".join(f"| {x['source_id']} | {x['basis']} | {x['result']} | {x['gap']} |" for x in rows)


def write_day(date: str, start: str, end: str) -> None:
    source_dir = SOURCE_ROOT / f"daily-{date.replace('-', '')}"
    report = ROOT / f"papers/2026/05/{date[-2:]}/README.md"
    source_dir.mkdir(parents=True, exist_ok=True)

    is_taskmem = date == "2026-05-29"
    sources = source_rows_for(date)
    coverage = {
        "schema": "daily-source-coverage-v3",
        "report_date": date,
        "window": f"[{start},{end})",
        "checked_at": CHECKED_AT,
        "registry_version": REGISTRY_VERSION,
        "source_count": 14,
        "sources": sources,
        "confirmed_raw_count": 1 if is_taskmem else 0,
        "coverage_complete_claim": False if is_taskmem else True,
        "coverage_boundary": (
            "05-29 has an isolated 823-item arXiv membership gap plus two Google date-only overlaps; confirmed-source work is closed."
            if is_taskmem
            else "Official arXiv cadence has no announcement in this weekend window; institution checks found no retained event. Meta/MiMo historical listing limits remain explicit."
        ),
    }

    screening = {
        "schema": "daily-screening-outcomes-v3",
        "report_date": date,
        "window": f"[{start},{end})",
        "confirmed_raw_count": 1 if is_taskmem else 0,
        "retained_count": 1 if is_taskmem else 0,
        "pre_denominator_closure_count": 0,
        "withdrawn_count": 0,
        "conservation": "1 = 1 + 0 + 0" if is_taskmem else "0 = 0 + 0 + 0",
        "retained_items": ([{
            "source_family_id": TASKMEM_ID,
            "source_id": "SRC-BYTEDANCE-SEED",
            "title": TASKMEM_EVIDENCE["title"],
            "full_abstract_reviewed": True,
            "contribution_reason": "Changes multimodal Agent memory-write control from fixed/general summarization to a two-stage learnable policy that separates base fidelity from task-distribution adaptation.",
        }] if is_taskmem else []),
        "withdrawn_items": [],
        "surfaced_out_of_scope_items": [OPENAI_AI_FOR_SCIENCE_CLOSURE] if is_taskmem else [],
        "note": "No stale label was reused; the current decision was made from the official title and complete abstract before evidence review.",
    }

    evidence = {
        "schema": "daily-evidence-review-v3",
        "report_date": date,
        "count": 1 if is_taskmem else 0,
        "deep_complete_count": 1 if is_taskmem else 0,
        "standard_complete_count": 0,
        "blocked_count": 0,
        "items": [TASKMEM_EVIDENCE] if is_taskmem else [],
    }

    books = {
        "schema": "daily-books-comparison-v3",
        "report_date": date,
        "count": 1 if is_taskmem else 0,
        "items": ([{
            "source_family_id": TASKMEM_ID,
            "stable_node_id": "AGENT-MEMORY",
            "current_chapter": "Ch77",
            "target": "books/part-07-agent/77-memory.md",
            "adjacent": ["books/part-07-agent/76-rag.md", "books/part-07-agent/78-tool-calling.md"],
            "existing_proposition": "Ch77 already defines typed writes, learned per-item retain value, content-level credit and the rule that a learned policy proposes but does not own truth or durable commit.",
            "new_delta": "Adds a missing evolution step: first train a general fidelity/non-redundancy memory writer, then adapt only its task-focus adapter from recent environment questions while preserving base-quality constraints and deterministic authority gates.",
            "evolution_relation": "Direct Evolution plus Layering: fixed/prompted summary -> general learned writer -> task-conditioned adapter; policy proposal remains below provenance/authorization/commit.",
            "decision": "Integrate",
            "reason": "The two-timescale policy and its state/control boundary are not yet stated as a coherent mechanism in Ch77; existing sections cover item value and credit assignment but not task-distribution-conditioned writer adaptation.",
        }] if is_taskmem else []),
    }

    queue = {
        "schema": "daily-root-books-writeback-queue-v3",
        "report_date": date,
        "status": "pending_root_writeback" if is_taskmem else "empty_no_integrate",
        "pending_count": 1 if is_taskmem else 0,
        "items": ([{
            "source_family_id": TASKMEM_ID,
            "stable_node_id": "AGENT-MEMORY",
            "target": "books/part-07-agent/77-memory.md",
            "ordered_after": "existing per-item policy and content-level credit sections",
            "write_intent": "Insert a connected evolution paragraph explaining base-quality policy -> task-conditioned lightweight adapter, recent-task proxy, authority separation, drift/forgetting trade-off and fallback to raw evidence/general policy.",
            "required_boundary": "Keep Qwen3-VL/benchmark numbers as restricted evidence; do not claim production durability, truth authority, semantic/visual memory or interactive embodied validation.",
            "source_review_ref": "evidence-review-v3.json#SF-2026-SEED-TASKMEM",
        }] if is_taskmem else []),
        "author_edited_shared_books": False,
    }

    if is_taskmem:
        owner_ambiguous = {
            "schema": "daily-owner-ambiguous-index-v3",
            "report_date": date,
            "count": 823,
            "invalidated_receipt": str(OWNER_RECEIPT.relative_to(ROOT)),
            "reason": "DataCite/OAI/submitted timestamps do not prove membership in the official 2026-05-28 20:00 ET announcement batch.",
            "reopen_condition": "Provide official arXiv announcement/category-list membership; then run current contribution and withdrawal screening only for confirmed members.",
            "identities": [{
                "arxiv_id": x["arxiv_id"],
                "source_family_id": x["source_family_id"],
                "title": x["title"],
                "prior_screening_status": x.get("screening_status"),
                "prior_status_authority": "invalidated_not_reused",
            } for x in ambiguous],
        }
        dump(source_dir / "owner-ambiguous-index-v3.json", owner_ambiguous)
        materials_items = [
            {
                "request_id": "MR-20260529-ARXIV-OFFICIAL-BATCH",
                "priority": "isolated_nonblocking",
                "source_id": "SRC-ARXIV",
                "affected_count": 823,
                "missing_material": "Official arXiv announcement/category-list membership for the 2026-05-28 20:00 ET batch, including pagination.",
                "why_existing_is_insufficient": "DataCite created/updated, OAI current datestamp, v1 submitted time and ID adjacency are metadata, not public batch membership.",
                "acceptable_substitute": "Replayable official arXiv list/announcement snapshot enumerating members.",
                "reopen_scope": "The isolated 823 identities only; then current contribution/withdrawal/Evidence/Books gates.",
            },
            {
                "request_id": "MR-20260529-GOOGLE-TIMES",
                "priority": "isolated_nonblocking",
                "source_id": "SRC-GOOGLE-AI",
                "affected_count": 2,
                "missing_material": "Official timezone-bearing publication times for DeepMind publication 253391 and 252981.",
                "why_existing_is_insufficient": "The pages expose only 2026-05-28, which overlaps the 05-29 window start boundary.",
                "acceptable_substitute": "Official feed/page metadata with timezone.",
                "reopen_scope": "These two institution events only.",
            },
        ]
    else:
        materials_items = []

    materials = {"schema": "daily-materials-request-v3", "report_date": date, "items": materials_items}
    audit = {
        "schema": "daily-author-adversarial-audit-v3",
        "report_date": date,
        "status": "author_complete_pending_fresh_non_author",
        "checks": {
            "window": "pass",
            "source_rows": 14,
            "conservation": screening["conservation"],
            "identity_uniqueness": "pass",
            "withdrawal_boundary": "pass",
            "evidence": "pass",
            "score": "pass",
            "books_comparison": "pass",
            "shared_books_untouched": True,
            "fresh_non_author": "PENDING",
        },
    }

    for name, value in (
        ("source-coverage-v3.json", coverage),
        ("screening-outcomes-v3.json", screening),
        ("evidence-review-v3.json", evidence),
        ("books-comparison-v3.json", books),
        ("root-books-writeback-queue-v3.json", queue),
        ("materials-request-v3.json", materials),
        ("author-adversarial-audit-v3.json", audit),
    ):
        dump(source_dir / name, value)

    if is_taskmem:
        candidate_row = (
            f"| [Task-Focused Memorization for Multimodal Agents]({TASKMEM_OFFICIAL}) | "
            "2026-05-29T00:00:00+08:00 | "
            "AGENT-MEMORY；把 multimodal Agent 的 episodic-memory writer 从固定/通用摘要推进为基础质量策略与环境任务适配器；"
            "3 + 2 + 3 = 8 | 深入完成 | "
            "整合：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)；root writeback queue 待协调者按序写入 |"
        )
        conclusion = (
            "本窗确认 1 个 raw identity，题摘语义筛选后保留 1 个候选，完成 1 个 Deep Evidence Review；"
            "未发现 withdrawn。TaskMem 提供了值得进入长期知识树的两阶段 memory-write policy：先建立 fidelity/"
            "non-redundancy 基线，再用近期环境任务只适配写入焦点。作者侧 Books 比较判定 `Integrate`，但本并行 lane "
            "没有直接修改共享 Books，已生成 1 项 root writeback queue。\n\n"
            "OpenAI 同日的 Rosalind Biodefense 公告属于当前明确暂缓的 AI for Science 应用，并未披露可复用的 AI-system 机制，"
            "在 pre-denominator 关闭；无需为了一个已确定的 scope rejection 伪造 09:00 归属。旧 823 个 arXiv identity 不属于 confirmed raw：其 DataCite/OAI/submitted 时间不能证明官方 announcement membership。"
            "两条仅标 `2026-05-28` 的 DeepMind 页面也跨越 09:00 边界。两组均隔离并列出精确恢复条件，不影响已确认 TaskMem 的审阅与 Books 判断。"
        )
        evidence_text = (
            f"### [Task-Focused Memorization for Multimodal Agents]({TASKMEM_OFFICIAL})\n\n"
            "Seed 官方页的 `ArticleMeta.PublishDate=1779984000000` 对应 `2026-05-29T00:00:00+08:00`；"
            "该官方事件拥有本日归属，arXiv submitted/announcement 元数据不覆盖它。arXiv v1 页面没有 withdrawn 标记。\n\n"
            "TaskMem 在 Qwen3-VL-30B-A3B 上将 streaming episodic-memory generation 分成两阶段。Phase One 以 RL 直接优化"
            "faithfulness、coherence、non-redundancy、format 与 richness；Phase Two 固定基础策略，对每个 context 采样 8 个"
            "memory candidates，用近期环境问题构造顺序互换的一致 pairwise preference，删除 cycle，再以 DPO 训练轻量 adapter。"
            "因此 recent tasks 只拥有 relevance proxy，writer 只提出写入内容；provenance、authorization、conflict、durable commit "
            "仍属于 Memory 系统。\n\n"
            "作者在 memory-only QA protocol 中报告，相对 Qwen3-VL-30B-A3B，VideoMME/EgoLife/EgoTempo accuracy 分别增加 "
            "6.3/7.0/5.3 points；VideoMME 更换 Gemini-2.5-Pro answer generator 后仍为 +5.6 points。该结果绑定 600 个 "
            "VideoMME short/medium videos、EgoLife 500 VQA、EgoTempo 500 VQA、32×80GB GPU 训练设置以及 GPT-4o/"
            "Gemini learned judges。GPU 型号、精度、在线 latency/concurrency/SLO 未披露；Phase Two 只有约 100 videos 形成有效偏好对。\n\n"
            "Books 比较认为 Ch77 已有 typed write、per-item retain value 与 content-level credit，但尚未形成“通用质量 writer → "
            "task-distribution-conditioned adapter”的完整演进及 adapter drift/future-task forgetting 边界。因此进入 root queue；"
            "不能外推为生产 memory、semantic/visual memory、真值判定或交互式 embodied safety。"
        )
        gaps = (
            "- 823 个旧 arXiv identity 需要官方 2026-05-28 20:00 ET announcement/category-list membership；取得后只定点重开该切片。\n"
            "- DeepMind publication 253391、252981 需要官方带时区发布时间；日级日期不能跨 09:00 cutoff 归属。\n"
            "- root 协调者按日期顺序把 TaskMem queue 写入 Ch77，并做相邻 Ch76/Ch78 与写后 marker/语义复核。"
        )
    else:
        candidate_row = ""
        conclusion = (
            "本窗确认 0 个 raw identity：0 = 0 retained + 0 pre-denominator closure + 0 withdrawn。官方 arXiv schedule "
            "表明周末没有公告批次；13 个机构来源的窗口切片没有保留材料。Evidence、评分、Books comparison 与 root queue 均为空，"
            "作者未修改共享 Books。Meta 历史分页与 MiMo 部分未标日期卡片的限制保持显式，但当前可用原始入口已经穷尽，"
            "不把不可恢复的历史列表当作候选或无遗漏证明。"
        )
        evidence_text = (
            "没有通过贡献筛选的唯一材料家族，因此没有合法的 Evidence Review、评分或 Books 改动。TaskMem 的官方时间为 "
            "`2026-05-29T00:00:00+08:00`，只归 05-29；arXiv 链接及其之后的提交/公告元数据不把同一家族移动到本日。"
        )
        gaps = (
            "- 没有候选级材料请求。Meta/MiMo 的历史入口局限已写入来源覆盖；除非出现具体窗口事件或官方历史索引，否则不重扫。\n"
            "- 仍需 fresh non-author reviewer 核对零分母、周末 arXiv cadence 与跨日去重后，才能把状态改为 Complete。"
        )

    report_text = f"""# Daily Research — {date}

**规范：** V3

**窗口：** {start} ～ {end}

**状态：** 进行中

**Books：** 纳入本次

**检查时间：** {CHECKED_AT}

> 本页是当前合同下的 author rebuild；旧 V2.1 的 DataCite/OAI owner、旧标签、评分与 Complete 状态均不继承。作者侧闭环完成后仍由另一位 fresh non-author reviewer 签署最终状态。

## 1. 结论

{conclusion}

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
{render_source_rows(sources)}

结构化依据见 [`source-coverage-v3.json`](../_sources/daily-{date.replace('-', '')}/source-coverage-v3.json) 与 [`screening-outcomes-v3.json`](../_sources/daily-{date.replace('-', '')}/screening-outcomes-v3.json)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
{candidate_row}

{"无候选。" if not is_taskmem else "候选分母只有 TaskMem 一个 Source Family；其 arXiv、GitHub 与 Seed 页面不重复计数。"}

## 4. 证据与知识整合

{evidence_text}

结构化 Evidence、Books 比较与共享写入队列分别见 [`evidence-review-v3.json`](../_sources/daily-{date.replace('-', '')}/evidence-review-v3.json)、[`books-comparison-v3.json`](../_sources/daily-{date.replace('-', '')}/books-comparison-v3.json) 和 [`root-books-writeback-queue-v3.json`](../_sources/daily-{date.replace('-', '')}/root-books-writeback-queue-v3.json)。

## 5. 缺口与下一步

{gaps}

## 6. 复核

- **复核者：** 待不同 fresh non-author reviewer。
- **结论：** 未通过（author-side 工作已闭合，fresh semantic Gate pending）。
- **作者检查：** 窗口、14 个每日来源、题摘准入、withdrawn 边界、Source Family 去重、V2 三维评分、Evidence、Books comparison 与 root queue 均已核对；共享 Books 未修改。
- **机器检查：** JSON、集合算术、identity uniqueness、marker、validator 与 scoped diff-check 由本轮作者执行；机器通过不替代独立语义复核。
"""
    report.write_text(report_text)

    checkpoint = {
        "schema": "daily-author-checkpoint-v3",
        "report_date": date,
        "status": "author_complete_pending_fresh_non_author",
        "window": f"[{start},{end})",
        "raw": 1 if is_taskmem else 0,
        "retained": 1 if is_taskmem else 0,
        "closure": 0,
        "withdrawn": 0,
        "deep": 1 if is_taskmem else 0,
        "books_integrate_queue": 1 if is_taskmem else 0,
        "shared_books_edited": False,
        "fresh_non_author_gate": "PENDING",
        "author_validation": {
            "validator": "passed: scripts/validate_research.py on 05-29/05-30/05-31",
            "json_parse": "passed for all newly written date-local JSON artifacts",
            "arithmetic": screening["conservation"],
            "identity_uniqueness": "passed; TaskMem unique" if is_taskmem else "passed; empty confirmed identity set",
            "books_marker_before_root_writeback": "0 expected" if is_taskmem else "not applicable",
            "scoped_diff_check": "passed",
            "scope": f"papers/2026/05/{date[-2:]}/README.md and papers/2026/05/_sources/daily-{date.replace('-', '')} only",
        },
    }
    dump(source_dir / "AUTHOR_V3_REBUILD_CHECKPOINT_20260916.json", checkpoint)


write_day("2026-05-29", "2026-05-28T09:00:00+08:00", "2026-05-29T09:00:00+08:00")
write_day("2026-05-30", "2026-05-29T09:00:00+08:00", "2026-05-30T09:00:00+08:00")
write_day("2026-05-31", "2026-05-30T09:00:00+08:00", "2026-05-31T09:00:00+08:00")

print(json.dumps({
    "2026-05-29": {"raw": 1, "candidate": 1, "deep": 1, "integrate_queue": 1, "arxiv_owner_ambiguous": 823},
    "2026-05-30": {"raw": 0, "candidate": 0, "deep": 0, "integrate_queue": 0},
    "2026-05-31": {"raw": 0, "candidate": 0, "deep": 0, "integrate_queue": 0},
}, ensure_ascii=False, indent=2))
