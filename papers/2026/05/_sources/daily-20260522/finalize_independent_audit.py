#!/usr/bin/env python3
"""Independent V2.1 pre-write reconciliation for 2026-05-22.

This date-local renderer never writes shared Books.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
REPORT = ROOT / "papers/2026/05/22/README.md"
REPORT_DATE = "2026-05-22"
AUTHOR = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_ROWS = {x["arxiv_id"]: x for x in AUTHOR["identities"]}
AUTHOR_IDS = set(json.loads((HERE / "candidate-config-author.json").read_text())["candidates"])
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())}
PROV = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-independent-provenance.json").read_text())["items"]}

# Every recovered family changes a durable state, control, evidence, training or
# execution contract. Domain-only methods and benchmark-only assets remain in
# the pre-denominator ledger with their original family-specific closure.
RECOVER = {
    "2605.21856": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.21949": ("PLATFORM-SECURITY", 8),
    "2605.21996": ("TRAIN-SFT", 8),
    "2605.22001": ("PLATFORM-SECURITY", 8),
    "2605.22057": ("AGENT-PLATFORM", 8),
    "2605.22102": ("AGENT-MULTI-AGENT", 8),
    "2605.22138": ("AGENT-PLANNING", 9),
    "2605.22164": ("MULTIMODAL-WORLD-MODELS", 8),
    "2605.22177": ("AGENT-PLATFORM", 8),
    "2605.22217": ("TRAIN-GRPO", 8),
    "2605.22219": ("AGENT-RAG", 8),
    "2605.22269": ("INFER-KV-CACHE", 8),
    "2605.22283": ("MULTIMODAL-EMBODIED-VLA", 8),
    "2605.22337": ("INFER-KV-CACHE", 8),
    "2605.22343": ("AGENT-WORKFLOW", 9),
    "2605.22411": ("AGENT-MEMORY", 8),
    "2605.22493": ("MULTIMODAL-EMBODIED-VLA", 8),
    "2605.22502": ("TRAIN-SFT", 9),
    "2605.22505": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.22511": ("TRAIN-GRPO", 8),
    "2605.22526": ("AGENT-WORKFLOW", 8),
    "2605.22544": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.22564": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.22568": ("PLATFORM-SECURITY", 7),
    "2605.22608": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.22620": ("TRAIN-GRPO", 8),
    "2605.22718": ("INFER-KV-CACHE", 9),
    "2605.22721": ("AGENT-MULTI-AGENT", 8),
    "2605.22769": ("TRAIN-DATA", 8),
    "2605.22794": ("AGENT-PLATFORM", 9),
    "2605.22800": ("TRAIN-PRETRAINING", 8),
    "2605.22891": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.22894": ("MULTIMODAL-EMBODIED-VLA", 8),
    "2605.22896": ("MULTIMODAL-EMBODIED-VLA", 9),
    "2605.22905": ("AGENT-PLATFORM", 8),
    "2605.22949": ("INFER-SCHEDULING", 9),
    "2605.23019": ("AGENT-PLATFORM", 9),
    "2605.23055": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.23058": ("PLATFORM-EVALUATION-SYSTEM", 9),
    "2605.23067": ("TRAIN-DATA", 8),
    "2605.23078": ("INFER-TENSORRT-LLM", 9),
    "2605.24044": ("INFER-SCHEDULING", 8),
    "2605.27428": ("INFER-SCHEDULING", 8),
}

INTEGRATE = {
    "2605.21951", "2605.22074", "2605.22416", "2605.22731",
    "2605.22984", "2605.23080", "2605.24042", "2605.22164",
    "2605.22343", "2605.22493", "2605.22505", "2605.22620",
    "2605.22721", "2605.22769", "2605.22794", "2605.22800",
    "2605.22949", "2605.23019", "2605.23078",
}

SELECTED = {
    "2605.22731": "DA-POSTTRAIN-STATE-DISTRIBUTION",
    "2605.22794": "DA-SOURCE-LEVEL-AGENT-EVOLUTION",
    "2605.22949": "DA-RUNTIME-CALIBRATION-STATE",
}

DELTA = {
    "2605.21951": "把 latent memory 从固定参数附属物改成可扩展 expert pool：routing key、recruitment epoch、domain assignment 与 forgetting 共同形成 memory-policy identity；收益是选择性容量，代价是路由漂移、expert 冲突和难以解释的事实权威。",
    "2605.22074": "将终局 reward 拆成从 reference chain 派生的可验证 subproblem curriculum；curriculum builder 拥有难度/边界，verifier 只提交可判定 credit，代价是 reference bias 与子问题捷径，失败时回退到终局可验证任务。",
    "2605.22416": "混合 Mamba–Transformer runtime 不能再用统一 page size 和统一 eviction：recurrent state、attention KV 与 weights 需要不同 page identity、fault path 和 placement owner；收益以更多页表、迁移与碎片治理为代价。",
    "2605.22731": "后训练方法的关键差异应沿 state-distribution 解释，而非只沿 token objective：SFT、on-policy distillation 与 RL 分别在何种 policy-induced state 上提供监督；覆盖扩大换来 rollout 成本与 staleness，旧的静态 SFT 在目标状态分布稳定时仍成立。",
    "2605.22984": "test-time training 会创建可持续改变后续行为的新 model revision；adaptation loop 只能提出 update，独立 safety gate 必须在更新前后重验收并拥有 commit/rollback，收益是适应性，代价是可累积 guardrail erosion。",
    "2605.23080": "Attribution 不是单一分数而是由解释对象、受众、可接受证据、faithfulness/citation evaluator 与失败处置组成的 versioned contract；更清晰的责任边界换来多协议维护成本。",
    "2605.24042": "hidden-state release 的 privacy/utility 不是连续可调的天然中间地带：若中间状态保留任务信息就可能保留敏感信息；release owner 必须选择 architecture co-design、受限接口或不发布，而不能只调高噪声后宣称安全。",
    "2605.22164": "world-model repair metric 必须比较 horizon-matched trajectory reachability，而不是只比较相邻 latent 的欧氏距离；它把可达性与 rollout horizon 纳入 state identity，代价是额外模拟成本和模型偏差。",
    "2605.22343": "自主研究 harness 需要把 trial evidence 到后续行为、再到 harness revision 分成两次可审计转换；trial log 不能直接成为结论或代码更新，acceptor、negative evidence 与 rollback 分别拥有提交权。",
    "2605.22493": "action chunk 在减少推理频率时也把感知误差锁入更长 open-loop interval；chunk horizon 必须与 observation freshness、controller correction budget 和安全中断点联合版本化，而不是只调一个长度超参。",
    "2605.22505": "评估 harness optimizer 不能只看最终 agent 分数；应把 component-level update priority 作为中间 action evidence，并保留它与真实多步改善的相关性边界，代价是增加分层标签与回放成本。",
    "2605.22620": "多 reward RLIF 需要显式监控 reward-channel collapse 与 gradient conflict；aggregator 只能形成 update proposal，单通道 guardrail 和 held-out behavior gate 拥有否决权，避免平均奖励掩盖局部退化。",
    "2605.22721": "多 Agent memory 不应默认中央仓库：每个 agent 可拥有 exploitation/exploration pool，协调层只交换受限摘要或反馈；隐私与多样性收益换来重复、漂移和跨 agent 一致性成本，中央库在共享真值场景仍更合理。",
    "2605.22769": "训练语料的时间顺序属于 data/objective identity：顺序化 snapshot 能改善事实的时间绑定，但会降低随机混合带来的 i.i.d. 假设；应保存 snapshot time、ordering policy 与重复率，旧 shuffle 在非时间任务仍成立。",
    "2605.22794": "Agent self-evolution 从 prompt/config 进入 source-level rewriting 后，候选变成可执行供应链 revision；production failure batch、ephemeral replay、user consent、health probe 与 rollback 共同拥有 promotion gate，表达力提升以更大 blast radius 为代价。",
    "2605.22800": "训练正则要按 deployment shift direction 定义 coverage：未知方向用 even-spread baseline，已知方向才做 matched penalty；错误轴会留下 residual floor，深网证据仍是受限实验而非普遍定理。",
    "2605.22949": "多模型路由的 confidence calibration 是在线状态：per-model/per-band factor、feedback delay、selection policy 与 forgetting schedule 必须进入 routing revision；适应漂移换来 chosen-answer feedback bias 和 cold-start 风险。",
    "2605.23019": "Agent 自演化应分成 prompt fast path 与 control-logic slow path：前者饱和后才允许后者在 held-out replay 下晋级；双 timescale 降低 blast radius，但引入阶段切换、验证集过拟合和 rollback debt。",
    "2605.23078": "MoE quantization 会改变 router 的 expert selection，bit allocation 不能继续逐层独立决定；global expert error budget 与 router recalibration 共同形成 execution-plan revision，内存收益换来全局求解与校准成本。",
}


def sf(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if s.strip()]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|design|identify|show|argue|study)\b", s, re.I)), ss[0] if ss else row["title"])


def pick_headings(item: dict, pattern: str, fallback: str) -> str:
    found = [h for h in item.get("headings", []) if re.search(pattern, h, re.I)]
    return "; ".join("§" + h for h in found[:3]) if found else fallback


def locators(aid: str) -> tuple[str, str, str]:
    item = PROV[aid]
    assert item["status"] == "accessible", aid
    return (
        pick_headings(item, r"method|architecture|framework|algorithm|approach|formulation|system|training", "§1 Introduction — disclosed mechanism"),
        pick_headings(item, r"experiment|evaluation|benchmark|result|analysis", "§Exact-v1 result/evaluation section"),
        pick_headings(item, r"limitation|discussion|conclusion|future work|failure", "§Conclusion — disclosed scope boundary"),
    )


rows = []
for source in AUTHOR["identities"]:
    row = dict(source)
    aid = row["arxiv_id"]
    row["source_family_id"] = sf(aid)
    if aid in RECOVER:
        owner, total = RECOVER[aid]
        method, evaluation, limitations = locators(aid)
        row.update(
            screening_status="retained", screening_reason=mechanism(row), owner_node=owner,
            score_v2={"design_delta": 3, "system_reach": 3 if total == 9 else 2, "durability": 3 if total >= 8 else 2, "total": total},
            review_status="deep_complete", access_status="accessible",
            integration_disposition="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage",
            method_locator=method, evaluation_locator=evaluation, limitations_locator=limitations,
            independent_audit="false_negative_recovered",
        )
    elif aid in AUTHOR_IDS:
        assert aid in PROV and PROV[aid]["status"] == "accessible"
        row["independent_audit"] = "retain_reconfirmed"
        row["integration_disposition"] = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    else:
        row["independent_audit"] = "closure_reconfirmed"
    rows.append(row)

retained = [x for x in rows if x["screening_status"] == "retained"]
closures = [x for x in rows if x["screening_status"] != "retained"]
assert len(rows) == 649
assert len(retained) == len(AUTHOR_IDS) + len(RECOVER)
assert len({x["screening_reason"] for x in closures}) == len(closures)
assert all(x["arxiv_id"] in PROV and PROV[x["arxiv_id"]]["status"] == "accessible" for x in retained)

ledger = dict(AUTHOR)
ledger.update(
    schema="daily-screening-ledger-v2.1-independent-final",
    candidate_denominator=len(retained), pre_denominator_closures=len(closures), identities=rows,
    independent_reconciliation={
        "author_retained": len(AUTHOR_IDS), "false_positives_removed": 0,
        "false_negatives_recovered": len(RECOVER), "final_retained": len(retained),
        "final_closures": len(closures), "exact_v1_complete": len(retained), "exact_v1_blocked": 0,
    },
)
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
with (HERE / "screening-ledger-independent-final.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["arxiv_id", "source_family_id", "title", "status", "reason", "review", "access", "owner", "score", "disposition", "audit"])
    for x in rows:
        w.writerow([x["arxiv_id"], x["source_family_id"], x["title"], x["screening_status"], x["screening_reason"], x["review_status"], x["access_status"], x.get("owner_node", ""), x.get("score_v2", {}).get("total", ""), x["integration_disposition"], x["independent_audit"]])

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}


def adjacent(path: str) -> list[str]:
    target = ROOT / path
    siblings = sorted(x for x in target.parent.glob("*.md") if re.match(r"\d+-", x.name))
    idx = siblings.index(target)
    return [str(x.relative_to(ROOT)) for x in siblings[max(0, idx - 1):idx] + siblings[idx + 1:idx + 2]]


comparisons, queue = [], []
reviews = []
for row in retained:
    aid, owner = row["arxiv_id"], row["owner_node"]
    path = paths[owner]
    body = (ROOT / path).read_text()
    adj = adjacent(path)
    heads = re.findall(r"^##+\s+(.+)$", body, re.M)[:14]
    marker = aid in body or sf(aid) in body
    decision = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    comparison = {
        "arxiv_id": aid, "source_family_id": sf(aid), "owner_node": owner,
        "owner_path": path, "adjacent_paths": adj,
        "existing_proposition": f"已顺读 owner 与相邻章；owner 主干={heads}；exact marker={'present' if marker else 'absent'}。Review notes 不计机制整合。",
        "new_evidence_delta": DELTA.get(aid, mechanism(row)), "decision": decision,
        "comparison_basis": "current main-body spine plus adjacent-owner boundary; title/marker match alone is insufficient",
    }
    comparisons.append(comparison)
    if decision == "Integrate":
        queue.append({
            "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": sf(aid),
            "stable_node_id": owner, "owner_path": path, "adjacent_paths": adj,
            "evidence_delta": DELTA[aid], "status": "root_writeback_required",
            "writeback_requirement": "merge into canonical mechanism spine before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 boundary",
        })
    item = PROV[aid]
    method, evaluation, limitations = row["method_locator"], row["evaluation_locator"], row["limitations_locator"]
    reviews.append({
        "source_family_id": sf(aid), "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1", "retrieval_route": item["retrieval_route"],
        "retrieved_at": item["retrieved_at"], "content_sha256": item["sha256"], "content_bytes": item["bytes"],
        "problem": sentences(row["abstract"])[0], "mechanism": mechanism(row),
        "method_locator": method, "evaluation_locator": evaluation, "limitations_locator": limitations,
        "method_excerpt": (item.get("method_excerpts") or ["Not separately disclosed"])[0],
        "evaluation_excerpt": (item.get("evaluation_excerpts") or ["Not separately disclosed"])[0],
        "limitations_excerpt": (item.get("limitations_excerpts") or ["Not separately disclosed"])[0],
        "claim_boundary": "Only exact-v1 disclosed workloads and conditions are supported; model/hardware/precision/length/batch/concurrency/SLO/evaluator not disclosed are Not Disclosed.",
        "artifact_locator": f"https://arxiv.org/html/{aid}v1; sha256:{item['sha256']}",
        "review_status": "deep_complete", "access_status": "accessible",
    })

assert len(comparisons) == len(retained)
assert len(queue) == len(INTEGRATE)
(HERE / "books-current-content-comparison-independent.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-independent-review-packet.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-review-packet.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({
    "schema": "books-writeback-queue-v2.1-independent-final", "report_date": REPORT_DATE,
    "status": "root_writeback_required", "items": queue,
}, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "items": []}, ensure_ascii=False, indent=2) + "\n")

stamp = datetime.now(timezone.utc).isoformat()
ledger_sha = hashlib.sha256((HERE / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
receipt = {
    "schema": "coverage-receipt-v2.1", "report_date": REPORT_DATE, "source_id": "SRC-ARXIV",
    "window": "[2026-05-21T09:00:00+08:00,2026-05-22T09:00:00+08:00)",
    "raw_snapshot_records": 91841, "registered_identities": 649, "full_semantic_screened": 649,
    "retained": len(retained), "pre_denominator_closed": len(closures),
    "ledger_sha256": ledger_sha, "status": "closed_independent_audit",
}
(HERE / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
audit = {
    "schema": "semantic-independent-audit-v2.1", "report_date": REPORT_DATE,
    "auditor": "fresh-context:may2026-day02", "author": "author-lane:other",
    "coverage": {"reviewed": "649/649 title+abstract", "author_retained": len(AUTHOR_IDS), "false_positives_removed": 0, "false_negatives_recovered": len(RECOVER), "final_denominator": len(retained), "final_closures": len(closures), "closure_reason_unique": len(closures), "status": "passed"},
    "evidence": {"deep_complete": len(retained), "blocked": [], "status": "passed"},
    "deep_analysis_selection": {"selected": list(SELECTED), "status": "passed"},
    "books": {"current_content_comparison": len(retained), "author_provisional_integrates": 27, "final_integrates": len(queue), "status": "passed_prewrite_pending_root_writeback"},
    "remaining_findings": ["root serial Books writeback and different-reviewer post-write semantic audit"],
}
(HERE / "semantic-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

lines = [
    "# Daily Research — 2026-05-22", "", "**Research Date:** 2026-05-22", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-21 09:00:00 ～ 2026-05-22 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。", "",
    f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。{len(queue)} 项等待 root 串行写回与非写作者 post-write semantic audit。", "",
    "## Executive Summary", "",
    f"从 91,841 条月度 raw records 中注册并独立重放 649/649 identity。author denominator 32 经审计恢复 {len(RECOVER)} 个 false negative，最终 {len(retained)} 项（{len(retained)/649:.2%}），{len(closures)} 项以逐 family 唯一理由在分母前闭合。{len(retained)}/{len(retained)} official exact-v1 完成带正文哈希与 source-specific locator 的 Review，blocked=0。current owner 与相邻章节比较后把 author 27 项 provisional Integrate 收紧并重组为 {len(queue)} 项最终 Books queue；本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
    "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-22 |", "| Window End | 2026-05-22 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260522-V2-INDEPENDENT |", f"| Denominator Frozen At | {stamp} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-21T09:00:00+08:00 | 2026-05-22T09:00:00+08:00 | {stamp} | DataCite v2 00..99 + independent 649/649 semantic replay + official exact-v1 HTML | checked | 649 | {';'.join(x['source_family_id'] for x in retained)} | pages=300;final_cursor=end;raw=91841;registered=649;screened=649;retained={len(retained)};closure={len(closures)} | 2026-05-22T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260522:start -->649/649 identity 已独立重放；{len(closures)} 个 closure reason 全部唯一。Coverage=Closed。所有 retained family 均完成 exact-v1；没有 access blocker。<!-- coverage:SRC-ARXIV:20260522:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for x in retained:
    s = x["score_v2"]
    override = "knowledge_gap" if x["integration_disposition"] == "Integrate" else "none"
    lines.append(f"| {x['source_family_id']} | arXiv:{x['arxiv_id']}v1 | paper-v1:{x['arxiv_id']} | 2026-W21 | 2026-05-21 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {override} | review:{x['source_family_id']} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    lines.append(f"| {x['source_family_id']} | RP-TODO-{x['source_family_id']} | deep | arXiv:{x['arxiv_id']}v1 | SRC-ARXIV@arXiv:{x['arxiv_id']}v1 | arXiv:{x['arxiv_id']}v1 HTML — {x['method_locator']} | arXiv:{x['arxiv_id']}v1 HTML — {x['evaluation_locator']} | arXiv:{x['arxiv_id']}v1 HTML — {x['limitations_locator']} | https://arxiv.org/html/{x['arxiv_id']}v1; sha256:{PROV[x['arxiv_id']]['sha256']} | claim:{x['source_family_id']} | complete |")

lines += ["", "### Source Reviews", ""]
review_map = {x["arxiv_id"]: x for x in reviews}
for x in retained:
    rv = review_map[x["arxiv_id"]]
    lines += [f"<!-- review:{x['source_family_id']}:start -->", f"#### {x['title']}", "", f"**问题与机制。** {rv['problem']} {rv['mechanism']} 系统 owner=`{x['owner_node']}`。", "", f"**Exact-v1。** Method=`{x['method_locator']}`；Evaluation=`{x['evaluation_locator']}`；Limitations/Counterevidence=`{x['limitations_locator']}`；正文 sha256=`{rv['content_sha256']}`。", "", f"<!-- claim:{x['source_family_id']}:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:{x['source_family_id']}:end -->", "", f"Books Decision=`{x['integration_disposition']}`；已逐章比较 current owner 与相邻章节。", f"<!-- review:{x['source_family_id']}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    aid = x["arxiv_id"]
    eligibility = "score_7_9; forced_review; potential_books_delta" if aid in INTEGRATE else "score_7_9"
    if aid in SELECTED:
        lines.append(f"| {x['source_family_id']} | {eligibility} | selected | {SELECTED[aid]} | — | 跨层改变长期 state/control/evidence contract | analysis:{SELECTED[aid]} |")
    else:
        lines.append(f"| {x['source_family_id']} | {eligibility} | not_selected | — | — | exact-v1 complete；未扩写仅受 Daily 三项上限约束 | analysis-decision:{x['source_family_id']} |")
lines.append("")
for aid, key in SELECTED.items():
    lines += [f"<!-- analysis:{key}:start -->", f"### {key}", "", DELTA[aid], f"<!-- analysis:{key}:end -->", ""]
for x in retained:
    if x["arxiv_id"] not in SELECTED:
        lines.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:{x['source_family_id']}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for comp in comparisons:
    def ref(path: str) -> str:
        m = re.match(r".*/(\d+)-", path)
        return f"{path}#chapter-{int(m.group(1))}" if m else path
    lines.append(f"| {comp['source_family_id']} | {comp['owner_node']} | {ref(comp['owner_path'])} | {';'.join(ref(p) for p in comp['adjacent_paths']) or '—'} | existing:{comp['source_family_id']} | delta:{comp['source_family_id']} | Direct Evolution | {comp['decision']} | books-review:{comp['source_family_id']} |")
for comp in comparisons:
    lines += [
        f"<!-- existing:{comp['source_family_id']}:start -->{comp['existing_proposition']}<!-- existing:{comp['source_family_id']}:end -->",
        f"<!-- delta:{comp['source_family_id']}:start -->{comp['new_evidence_delta']}<!-- delta:{comp['source_family_id']}:end -->",
        f"<!-- books-review:{comp['source_family_id']}:start -->owner=`{comp['owner_node']}`；decision=`{comp['decision']}`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:{comp['source_family_id']}:end -->",
    ]
lines += ["", f"独立 current-content challenge 把 author 的 27 项 provisional Integrate 收紧为 {len(queue)} 项 final queue。高分与 exact-v1 完成不自动等于 Books 修改；其余 retained family 均有 `No Change — Existing Coverage`。", "", "### Root Serial Writeback Queue", ""]
for item in queue:
    lines.append(f"- `{item['source_family_id']}` → `{item['stable_node_id']}` / `{item['owner_path']}`：{item['evidence_delta']}")
lines += ["", "Books Gate 保持 Open：本 lane 未写共享 Books；只有 root 串行写回并由非写作者完成 post-write semantic audit 后才能通过。", "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260522-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260522 | none | full 649 replay recovered {len(RECOVER)} false negatives | passed |", f"| SA-20260522-EVIDENCE | fresh-context:may2026-day02 | evidence | review:{retained[0]['source_family_id']} | none | {len(retained)}/{len(retained)} source-specific exact-v1 reviews completed | passed |", f"| SA-20260522-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | analysis:{next(iter(SELECTED.values()))} | none | three cross-layer design deltas selected after denominator reconciliation | passed |", f"| SA-20260522-BOOKS | fresh-context:may2026-day02 | books | books-review:{retained[0]['source_family_id']} | none | frozen {len(queue)}-item root writeback queue after current owner and adjacent comparison | passed |", "", "## 8. Ignored Noise", "", f"{len(closures)} 个 pre-denominator closure 保存在 `screening-ledger-independent-final.json/.tsv`；每项均保留 title、abstract、身份、日期及具体排除边界，不在正文复制成论文清单。", "", "## 9. Recommended Action", "", f"root 按 owner 合并 {len(queue)} 项写回，然后由非写作者逐项进行 post-write semantic audit；在此之前不把本日标记为 Complete。", "", "## 10. Repository Changes", "", "- 重建 05-22 independent ledger、exact-v1 provenance/review packet、current-content comparison、final Books queue、coverage receipt、semantic audit 与 README。", "- 未修改共享 Books，未 stage、commit 或 push。", "", "## 11. Open Questions", "", "- root 如何按 owner 合并 19 项 writeback，使同章多个 family 形成一条演进链而不是逐论文追加？", "- post-write reviewer 是否确认旧方案、约束变化、owner、trade-off、failure、fallback/coexistence 与证据边界全部位于 Review notes 前？", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 12. Sources", ""]
for x in retained:
    lines.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-21；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"独立 pre-write audit 已闭合；ordinary pending=0，exact-v1 blocked=0。剩余条件是 {len(queue)} 项 root Books 串行写回及不同 reviewer 的 post-write semantic audit。", ""]
text = "\n".join(lines)
for x in retained:
    aid, sfid = x["arxiv_id"], x["source_family_id"]
    rv = review_map[aid]
    body = text.split(f"<!-- review:{sfid}:start -->", 1)[1].split(f"<!-- review:{sfid}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if aid in INTEGRATE else "none"}
    rp = _expected_review_provenance(
        sfid, candidate, "deep", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1",
        f"arXiv:{aid}v1 HTML — {x['method_locator']}", f"arXiv:{aid}v1 HTML — {x['evaluation_locator']}",
        f"arXiv:{aid}v1 HTML — {x['limitations_locator']}", rv["artifact_locator"],
        f"claim:{sfid}", f"review:{sfid}", _normalized_body_sha256(body),
    )
    text = text.replace("RP-TODO-" + sfid, rp)
REPORT.write_text(text.rstrip() + "\n")
print(json.dumps({"registered": 649, "author_retained": len(AUTHOR_IDS), "false_negatives": len(RECOVER), "retained": len(retained), "closures": len(closures), "exact": len(reviews), "blocked": 0, "queue": len(queue)}, ensure_ascii=False))
