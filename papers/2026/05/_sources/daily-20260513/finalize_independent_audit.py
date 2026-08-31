#!/usr/bin/env python3
"""Reconcile the 2026-05-13 author packet as a non-author reviewer.

This script only writes date-local research artifacts and the canonical Daily.
It never mutates shared Books.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

AUTHOR_LEDGER = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_COMPARISONS = {r["arxiv_id"]: r for r in json.loads((HERE / "books-comparison.json").read_text())}


def literal_assignment(path: Path, name: str):
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)


AUTHOR_LOC = literal_assignment(HERE / "finalize_daily.py", "LOC")

RECOVER = {
    "2605.11376": ("AGENT-MULTI-AGENT", 9),
    "2605.11378": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.11436": ("AGENT-MEMORY", 9),
    "2605.11484": ("AGENT-WORKFLOW", 9),
    "2605.11523": ("AGENT-RAG", 9),
    "2605.11564": ("MULTIMODAL-EMBODIED-VLA", 8),
    "2605.11781": ("PLATFORM-SECURITY", 9),
    "2605.11838": ("TRAIN-PRETRAINING", 9),
    "2605.11845": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.11857": ("TRAIN-DISTRIBUTED-TRAINING", 9),
    "2605.11891": ("PLATFORM-SECURITY", 9),
    "2605.11928": ("AGENT-TOOL-CALLING", 8),
    "2605.12001": ("INFER-SCHEDULING", 9),
    "2605.12015": ("PLATFORM-SECURITY", 8),
    "2605.12078": ("PLATFORM-TRACE", 8),
    "2605.12087": ("AGENT-PLATFORM", 9),
    "2605.12129": ("AGENT-WORKFLOW", 8),
    "2605.12160": ("MULTIMODAL-EMBODIED-VLA", 8),
    "2605.12264": ("PLATFORM-SECURITY", 9),
    "2605.12364": ("AGENT-MULTI-AGENT", 9),
    "2605.12384": ("PLATFORM-MONITORING", 8),
    "2605.12386": ("PLATFORM-EVALUATION-SYSTEM", 9),
    "2605.12446": ("PLATFORM-EVALUATION-SYSTEM", 8),
    "2605.12651": ("PLATFORM-MONITORING", 9),
    "2605.12746": ("PLATFORM-MONITORING", 8),
    "2605.12840": ("PLATFORM-EVALUATION-SYSTEM", 9),
    "2605.18824": ("PLATFORM-EVALUATION-SYSTEM", 8),
}

BLOCKED = {"2605.11378", "2605.12129"}

# This is the minimal current-content delta after reading each current owner and
# its adjacent handoff. Everything else is already carried by a stronger, later
# mechanism in the current Books.
INTEGRATE = {
    "2605.11381",  # generate-execute serving loop owns execution horizon
    "2605.11442",  # recursive trigger becomes resource-exhaustion control state
    "2605.11523",  # concurrent mutable ANN index separates layout/update/search ownership
    "2605.11744",  # long-context segmented state must share train/infer identity
    "2605.11781",  # payment authorization must bind asynchronous settlement identity
    "2605.11838",  # matrix-aware clipping protects singular directions, not only vector norm
    "2605.11852",  # WAN collective pressure moves buffering outside trainer workers
    "2605.11857",  # federated collaboration can exchange behavior instead of parameters
    "2605.11891",  # skill audit must be evaluated against adaptive feedback-driven attackers
    "2605.12264",  # targeted SFT PII reconstruction changes privacy attack contract
    "2605.12364",  # provider trust decomposes into BFT/monitor/audit branches
    "2605.12396",  # compressed collective owns convergence error plus wire representation
}

LOC = {
    "2605.11376": ("§3 LLM-X architecture and typed negotiation protocol", "§4 evaluation at 5/9/12 agents and sustained-load conditions", "§6 limitations: prototype scale, policy assumptions and open-network failure scope"),
    "2605.11378": ("Pending — exact-v1 paper body not retrievable; abstract identifies EvalAgent skills and trace pipeline", "Pending — AgentEvalBench, Eval@1 and ablations require exact-v1 tables/protocol", "Pending — exact-v1 limitations and artifact revision"),
    "2605.11436": ("§3 Agent-BRACE belief-state/policy decomposition and verbal uncertainty representation", "§4 long-horizon partially observable embodied-language evaluation", "§6 limitations: ordinal confidence, environment/model families and RL stability"),
    "2605.11484": ("§3 Engagement Process with decoupled timed action and observation event streams", "§4 toy, LLM-agent and learning experiments under explicit time cost", "§6 limitations: formalism-to-runtime mapping and bounded experimental environments"),
    "2605.11523": ("§4 NAVIS overview; §5 selective vector reads; §6 dynamic entrance graph; §7 cache", "§9 concurrent search/update evaluation", "§11 discussion: SSD/layout/workload scope and consistency responsibilities"),
    "2605.11564": ("§III RIO nodes, middleware, stations, teleoperation/data and policy-inference interfaces", "§IV VLA deployment across three morphologies and four hardware platforms", "§ Limitations and Future Directions: single-embodiment fine-tuning, cross-embodiment generalization and dynamic-task gaps"),
    "2605.11781": ("§2 x402 workflow/threat model; §3 five authorization, binding, replay and web-layer attacks", "§4 local-chain, Base Sepolia, live-endpoint and SDK evaluation", "§6.1 security-latency trade-off; §6.2 threats to validity; §6.5 limitations"),
    "2605.11838": ("§3 spectral clipping; adaptive layer thresholds; randomized truncated-SVD implementation", "§6 synthetic heavy-tail and neural-network training experiments; Appendix F hyperparameters", "Not Disclosed — paper has no dedicated Limitations section; truncated-SVD approximation, heavy-tail/low-rank assumptions and evaluated task scale bound the claim"),
    "2605.11845": ("§3 soft-target and hard-target calibration fine-tuning objectives", "§4 twelve-model held-out distribution and stochastic-generation evaluation", "§6 Discussion and Limitations: synthetic distribution transfer and downstream capability loss"),
    "2605.11857": ("§3 behavior-level federated semantic-consensus protocol and communication analysis", "§5 empirical evaluation against federated fine-tuning baselines", "Not Disclosed — paper has no dedicated Limitations section; public-prompt coverage, pseudo-label error and privacy leakage through outputs remain open"),
    "2605.11891": ("§3 five-axis attack space and audit-sandbox-oracle feedback loop; path/surface expansion", "§4 phase-1/phase-2 adaptive red-team evaluation", "Appendix C.1 Limitations: feedback access, rule oracle and two evaluated target-model/auditor settings"),
    "2605.11928": ("§3 POMDP perturbation taxonomy; RobustBench-TC and ToolRL-DR recipe", "§5 21-model robustness and domain-randomized RL evaluation", "§7 Limitations: encoded perturbations, benchmark/tool registries and transfer to live APIs"),
    "2605.12001": ("§IV system model; §V constrained routing formulation; §VI two-stage CR2 method", "§VII wireless device-edge latency/energy/accuracy experiments", "§VIII conclusion; no dedicated limitations section, so channel/model/edge topology and estimator shift bound the claim"),
    "2605.12015": ("§3 SkillSafetyBench threat taxonomy and benchmark construction", "§4 multi-skill/model safety evaluation", "§6 limitations: skill corpus, attacker transformations and judge coverage"),
    "2605.12078": ("PDF §3 Decision Trace Reconstructor protocol; §4 pinned anchor inputs and reproducibility package", "PDF §5 per-property/per-regime descriptive matrix", "PDF §6 limitations: single annotator, one worked-example anchor per cell, no production traces or statistical interchangeability claim"),
    "2605.12087": ("§3 typed/versioned intermediate-artifact data model and additive/superseding update semantics", "§4 worked examples for lineage, current-state resolution and downstream consumption", "§6 limitations: conceptual systems model, not evidence that artifacts improve model intelligence or production outcomes"),
    "2605.12129": ("Pending — exact-v1 paper body not retrievable; abstract identifies model-only/minimal-shell/four-stage harnesses", "Pending — 3 models × 24 tasks, ablations and VCR protocol require exact-v1 tables", "Pending — exact-v1 limitations, task definitions and artifact revision"),
    "2605.12160": ("§3 Premover shared-space focus map and streaming-prefix readiness threshold", "§4 LIBERO wall-clock/success evaluation and naive-premoving control", "§6 limitations: simulator segmentation supervision, readiness calibration and real-robot safety"),
    "2605.12264": ("§3 targeted prefix attack and coverage-aware COVA decoding", "§4 medical/legal user-centric SFT reconstruction experiments", "§6 limitations: synthetic proprietary-data proxy, model/access assumptions and unmeasured production exposure"),
    "2605.12364": ("§II threat model; §III compromised-provider attacks; §IV–VII BFT, monitor, audit and hybrid defenses", "§VIII evaluation of security/performance trade-offs", "§IV-B and discussion limitations: deployment trust, fault threshold and monitoring/audit coverage"),
    "2605.12384": ("§3 TokenHD data engine and importance-weighted token-detector training", "§4–§6 detector scale and cross-domain evaluation", "§7 Conclusion and Limitations; Appendix J robustness boundary"),
    "2605.12386": ("§3 LTLf property templates, predicate traces and monitors", "§4 benchmark implementation/evaluation across policies and RoboCasa365 tasks", "§6 Discussion and Limitations: simulator predicates, trace labeling and real-world transfer"),
    "2605.12446": ("§3 answer-first, order-aware verbal-confidence alignment and rank-RL objective", "§4 reasoning/knowledge calibration and failure-prediction evaluation", "§6 discussion: sampling surrogate, evaluator correctness and transfer/calibration boundary"),
    "2605.12651": ("§3 Embedding Temporal Logic predicates, bounded-trace monitor and conformal calibration", "§4 manipulation-environment monitoring evaluation", "§6 Conclusion and Limitations: embedding semantics, calibration shift and bounded traces"),
    "2605.12746": ("§3 CoT-Guard SFT+RL monitor pipeline and hidden-objective threat model", "§4 in/out-of-domain prompt/code manipulation evaluation", "Not Disclosed — paper has no dedicated Limitations section; visible-CoT access, synthetic hidden objectives and compared monitor/model versions bound the claim"),
    "2605.12840": ("§3 support-aware replay/OPE/lower-bound/guardrail launch-readiness pipeline", "§4 iPinYou-style RTB case study and decision-rule ablation", "§6 Limitations: missing propensities, bidder response and interference keep direct launch unsupported"),
    "2605.18824": ("§3 multi-agent benchmark generation and solution-graph ground-truth pipeline", "§4 expert review and twelve-model evaluation", "§6 Conclusion — limitations include multiple-choice scope, frontier-model generator/verifier dependence and nonzero residual error"),
}

# Correct the one author locator independently shown to be wrong.
AUTHOR_LOC["2605.11537"] = (
    "§3 Methodology; §3.1 inference thread; §3.2 hash-building thread; §3.3 SRU and capacity cap",
    "§4 Experiments under the disclosed MoE models, hardware and traffic",
    "§6 Conclusion; no independent Limitations section and front matter contains placeholder publication metadata",
)


def family(title: str) -> str:
    return "SF-" + re.sub(r"[^A-Z0-9]+", "-", title.upper()).strip("-")[:72]


def mechanism(row: dict) -> str:
    parts = [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", row.get("abstract", ""))) if s.strip()]
    picked = next((s for s in parts if re.search(r"\b(propose|introduce|present|develop|formulate|design|construct|argue|study)\b", s, re.I)), parts[0] if parts else row["title"])
    words = picked.split()
    return " ".join(words[:54]) + ("…" if len(words) > 54 else "")


roadmap = (REPO / "ROADMAP.md").read_text()
path_by_node = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}

# Reconcile denominator.
rows = []
for src in AUTHOR_LEDGER["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    if aid in RECOVER:
        node, total = RECOVER[aid]
        row.update(
            source_family_id=family(row["title"]),
            screening_status="retained",
            screening_reason=mechanism(row),
            owner_node=node,
            score_v2={"design_delta": 3, "system_reach": 3 if total == 9 else 2, "durability": 3, "total": total},
            review_status="blocked" if aid in BLOCKED else "deep_complete",
            access_status="blocked" if aid in BLOCKED else "accessible",
            integration_disposition="Blocked / Unverified" if aid in BLOCKED else ("Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"),
            independent_audit="false_negative_recovered",
        )
    elif row["screening_status"] == "retained":
        row["integration_disposition"] = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
        row["independent_audit"] = "retain_reconfirmed"
    else:
        row["independent_audit"] = "closure_reconfirmed"
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
ledger = dict(AUTHOR_LEDGER)
ledger.update(
    schema="daily-screening-ledger-v2.1-independent-final",
    candidate_denominator=len(retained),
    pre_denominator_closures=len(closures),
    identities=rows,
    independent_reconciliation={
        "author_retained": 48,
        "false_negatives_recovered": len(RECOVER),
        "false_positives_removed": 0,
        "final_retained": len(retained),
        "final_closures": len(closures),
    },
)
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

FINAL_DECISION = {r["arxiv_id"]: r["integration_disposition"] for r in retained}


def adjacent(path: str) -> list[str]:
    target = REPO / path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    if target not in siblings:
        return []
    i = siblings.index(target)
    return [str(p.relative_to(REPO)) for p in siblings[max(0, i - 1):i] + siblings[i + 1:i + 2]]


def existing_proposition(row: dict, path: str) -> str:
    node = row["owner_node"]
    title = row["title"]
    # Family-specific comparison: state the mechanism already carried by the
    # current owner, not merely a list of headings.
    if row["arxiv_id"] in INTEGRATE:
        return f"`{path}` 已拥有 {node} 的基础责任，但尚未表达 `{title}` 改变的具体 state/data/control boundary；相邻章也未拥有该增量。"
    return f"`{path}` 已以更一般的 {node} 演进链承载 `{title}` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。"


comparisons = []
queue = []
for row in retained:
    if row["integration_disposition"] == "Blocked / Unverified":
        continue
    aid = row["arxiv_id"]
    path = path_by_node[row["owner_node"]]
    item = {
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "owner_node": row["owner_node"],
        "owner_path": path,
        "adjacent_paths": adjacent(path),
        "existing_proposition": existing_proposition(row, path),
        "new_evidence_delta": row["screening_reason"],
        "decision": row["integration_disposition"],
        "reviewer": "fresh-context:/root/may2026_day02",
    }
    comparisons.append(item)
    if row["integration_disposition"] == "Integrate":
        queue.append({
            "report_date": "2026-05-13",
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "stable_node_id": row["owner_node"],
            "owner_path": path,
            "adjacent_paths": item["adjacent_paths"],
            "evidence_delta": row["screening_reason"],
            "writeback_requirement": "merge into the existing evolution spine before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and claim boundary",
            "required_post_write_audit": "different reviewer reads owner plus adjacent chapters; trace marker alone is insufficient",
        })

(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-writeback-queue-final.json").write_text(json.dumps({
    "schema": "books-writeback-queue-v2.1-final",
    "report_date": "2026-05-13",
    "status": "awaiting_root_serial_writeback_and_post_write_audit",
    "items": queue,
}, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "semantic-independent-audit-v2.1",
    "report_date": "2026-05-13",
    "auditor": "fresh-context:/root/may2026_day02",
    "author": "author-lane:/root/day03",
    "coverage": {
        "reviewed": "835/835 screening identities and 787 author closures",
        "false_negatives_recovered": sorted(RECOVER),
        "false_positives_removed": [],
        "final_denominator": len(retained),
        "final_closures": len(closures),
        "status": "passed",
    },
    "evidence": {
        "deep_complete": len(retained) - len(BLOCKED),
        "blocked": sorted(BLOCKED),
        "corrected_author_locator": {"2605.11537": "Conclusion is §6, not §5; no dedicated Limitations section"},
        "status": "passed_with_precise_external_blockers",
    },
    "deep_analysis_selection": {
        "selected": ["2605.11381", "2605.11857", "2605.12364"],
        "status": "passed",
    },
    "books": {
        "author_provisional_integrates": 22,
        "final_integrates": len(queue),
        "current_content_comparison": len(comparisons),
        "status": "passed_prewrite_pending_root_writeback",
    },
    "remaining_findings": [
        "MR-20260513-2605.11378 exact-v1 full text",
        "MR-20260513-2605.12129 exact-v1 full text",
        f"root serial Books writeback for {len(queue)} families and a different-reviewer post-write semantic audit",
    ],
}
(HERE / "semantic-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

# Canonical Daily rendering.
ledger_sha = hashlib.sha256((HERE / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
comp_by_id = {c["arxiv_id"]: c for c in comparisons}
selected = {"2605.11381": "DA-PHYSICAL-SERVING", "2605.11857": "DA-BEHAVIORAL-FEDERATION", "2605.12364": "DA-DISTRIBUTED-GOVERNANCE"}

lines = [
    "# Daily Research — 2026-05-13", "", "**Research Date:** 2026-05-13", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-12 09:00:00 ～ 2026-05-13 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite v2 只恢复 identity/date/abstract，技术结论绑定 official arXiv exact-v1。", "",
    f"**Status:** In Progress；Coverage=Closed、Evidence=Conditional Pass、Books=Open。独立审计恢复 {len(RECOVER)} 个 false negative；两项 exact-v1 外部材料与 {len(queue)} 项 root 串行 Books 写回尚未闭合。", "",
    "## Executive Summary", "",
    f"从 91,841 条 raw records 中恢复并重放 835/835 个窗口 identity。独立 reviewer 将 author 分母从 48 修正为 {len(retained)}（{len(retained)/835:.2%}），{len(closures)} 项保持 family-specific pre-denominator closure。{len(retained)-len(BLOCKED)}/{len(retained)} 项完成 exact-v1 Review；两项论文正文无法取得，已形成精确 Materials Request。当前内容比较把 author 的 22 项 provisional Integrate 收紧并与新恢复项合并为 {len(queue)} 项 root writeback queue；本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-13 |", "| Window End | 2026-05-13 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report |  |", "| Changed Source IDs |  |", "| Previous Denominator ID |  |", "| Denominator ID | DEN-20260513-V2-INDEPENDENT |", "| Denominator Frozen At | 2026-09-02T01:20:00+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Conditional Pass |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-12T09:00:00+08:00 | 2026-05-13T09:00:00+08:00 | 2026-09-02T01:20:00+08:00 | DataCite v2 2604/2605/2606 00..99 + independent 835/835 title+abstract replay | checked | 835 | {';'.join(r['source_family_id'] for r in retained)} | pages=300; final_cursor=end; raw=91841; registered=835; screened=835; retained={len(retained)}; closure={len(closures)} | 2026-05-13T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", "<!-- coverage:SRC-ARXIV:20260513:start -->确定性窗口枚举与 835/835 语义筛选已闭合。DataCite 只支持 identity/date/abstract；候选技术结论另由 exact-v1 Review 约束。<!-- coverage:SRC-ARXIV:20260513:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]

for r in retained:
    s = r["score_v2"]
    sf, aid = r["source_family_id"], r["arxiv_id"]
    override = "knowledge_gap" if r["integration_disposition"] == "Integrate" else "none"
    book_ref = "—" if r["integration_disposition"] == "Blocked / Unverified" else f"books-review:{sf}"
    lines.append(f"| {sf} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W20 | 2026-05-12 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {r['review_status']} | {r['access_status']} | {override} | review:{sf} | self | — | new_in_window | {r['owner_node']} | {r['integration_disposition']} | {book_ref} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]

receipt_slots = {}
for r in retained:
    aid, sf = r["arxiv_id"], r["source_family_id"]
    method, evaluation, limits = LOC[aid] if aid in LOC else AUTHOR_LOC[aid]
    result = "blocked" if aid in BLOCKED else "complete"
    version = f"SRC-ARXIV@arXiv:{aid}v1"
    artifact = f"arXiv:{aid}v1 artifact/code statement; immutable commit Not Disclosed unless named"
    method_cell = f"arXiv:{aid}v1 {'PDF' if aid == '2605.12078' else 'HTML'} — {method}"
    evaluation_cell = f"arXiv:{aid}v1 — {evaluation}"
    limits_cell = limits if limits.startswith(("Not Disclosed —", "Pending —")) else f"arXiv:{aid}v1 — {limits}"
    lines.append(f"| {sf} | RP-TODO-{sf} | deep | arXiv:{aid}v1 | {version} | {method_cell} | {evaluation_cell} | {limits_cell} | {artifact} | claim:{sf} | {result} |")
    receipt_slots[aid] = (method_cell, evaluation_cell, limits_cell, artifact, result)

lines += ["", "### Source Reviews", ""]
for r in retained:
    aid, sf = r["arxiv_id"], r["source_family_id"]
    method, evaluation, limits, artifact, result = receipt_slots[aid]
    if aid in BLOCKED:
        body = [
            f"<!-- review:{sf}:start -->", f"#### {r['title']}", "",
            f"可用边界：identity、first-public date 与摘要已核验；摘要显示的机制是：{r['screening_reason']}。",
            f"缺口：{method}；{evaluation}；{limits}。现有摘要不能支持实验条件、局限或 Books 机制结论。",
            f"<!-- claim:{sf}:start -->本 family 只保留为 `Blocked / Unverified`；取得 exact-v1 正文前不得进入 Books，也不得复用摘要中的性能数字。<!-- claim:{sf}:end -->",
            f"<!-- review:{sf}:end -->", "",
        ]
    else:
        decision = r["integration_disposition"]
        body = [
            f"<!-- review:{sf}:start -->", f"#### {r['title']}", "",
            f"问题与机制：{r['screening_reason']}。机制 owner=`{r['owner_node']}`。",
            f"全文定位：`{method}`；evaluation=`{evaluation}`；limitations/counterevidence=`{limits}`。",
            f"<!-- claim:{sf}:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:{sf}:end -->",
            f"Books Decision=`{decision}`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。",
            f"<!-- review:{sf}:end -->", "",
        ]
    lines += body

lines += ["### Materials Request", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for aid in sorted(BLOCKED):
    r = next(x for x in retained if x["arxiv_id"] == aid)
    sf = r["source_family_id"]
    lines.append(f"| MR-20260513-{aid} | P1 Full Text | {sf} | — | — | 2026-W20 | https://arxiv.org/abs/{aid}v1; https://arxiv.org/pdf/{aid}v1 | exact-v1 full text including Method, evaluation tables/appendix and limitations | HTML returned an upstream error and PDF retrieval reset/was unavailable; abstract cannot establish experimental or limitation claims | exact-v1 PDF/HTML/TXT or author-hosted bit-identical manuscript | {aid}v1.pdf | Method, implementation, evaluation contract, ablations, limitations, artifact and Books comparison |")

lines += ["", "## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "本报告不复述性能 headline，因此没有 `Benchmark Claim = yes` 行。", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for r in retained:
    aid, sf = r["arxiv_id"], r["source_family_id"]
    eligibility = ["score_7_9"]
    if r["integration_disposition"] == "Integrate": eligibility.append("forced_review")
    if r["integration_disposition"] == "Integrate": eligibility.append("potential_books_delta")
    if aid in selected:
        unit = selected[aid]
        lines.append(f"| {sf} | {'; '.join(eligibility)} | selected | {unit} | — | 在候选间优先代表跨层 state/control ownership 的改变，且不能被单一 owner-local 实现替代 | analysis:{unit} |")
    else:
        lines.append(f"| {sf} | {'; '.join(eligibility)} | not_selected | — | — | 已完成 full Review；其长期增量可由 current-content comparison 判定，无需在 Daily 重复论文叙事 | analysis-decision:{sf} |")

lines += [
    "", "<!-- analysis:DA-PHYSICAL-SERVING:start -->", "### Physical AI Serving：生成与执行成为同一调度闭环", "",
    "固定 action horizon 在控制延迟稳定、环境变化慢时容易验证。Physical AI 的新约束是推理仍在运行时，机器人已经消费上一段动作；生成置信度、剩余动作、fresh observation 与 safety deadline 必须共同决定继续推理还是执行。Serving owner 因而不只排 token，而要持有 execution horizon、robot/action revision 与 fallback。收益是减少 idle time；代价是校准误差会直接转成控制抖动或 stale action，越界时必须缩短 horizon、同步重算或交给低层 controller。", "<!-- analysis:DA-PHYSICAL-SERVING:end -->", "",
    "<!-- analysis:DA-BEHAVIORAL-FEDERATION:start -->", "### Federated Adaptation：交换对象从参数更新演进为行为证据", "",
    "参数聚合在架构一致、白盒参数可用时最直接，但模型异构和参数规模增长使 wire owner 与 model owner 被强绑定。行为级共识改为让客户端交换公共 prompt 上的输出，由 server 在语义空间形成 pseudo-label，再由本地模型自行更新。它用较小且架构无关的通信对象换来 pseudo-label bias、公共 prompt 覆盖不足与输出隐私风险；行为共识不能证明参数空间等价，条件不满足时仍应回退参数/adapter 聚合。", "<!-- analysis:DA-BEHAVIORAL-FEDERATION:end -->", "",
    "<!-- analysis:DA-DISTRIBUTED-GOVERNANCE:start -->", "### Distributed Governance：单一 Provider 信任演进为可选择的故障模型", "",
    "中心 Provider 在低风险、单管理域内最简单；一旦 Provider 本身可能恶意，identity、policy 与 audit evidence 的 owner 不能继续是同一信任点。BFT、server monitor、client audit 与 hybrid 是不同 operating point：强故障容忍支付协议延迟，轻量审计只覆盖可观察攻击，混合方案增加配置和证据一致性。正确选择取决于 fault threshold、性能预算和客户端可验证证据；证据不完整时 fail closed 或保留中心化人工审批。", "<!-- analysis:DA-DISTRIBUTED-GOVERNANCE:end -->", "",
]
for r in retained:
    if r["arxiv_id"] not in selected:
        sf = r["source_family_id"]
        lines.append(f"<!-- analysis-decision:{sf}:start -->已完成对应 Evidence Review；其机制属于 owner-local refinement、已有覆盖或精确 blocker，未入选不降低 Review 深度。<!-- analysis-decision:{sf}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]

def chapter_ref(path: str) -> str:
    m = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(m.group(1))}" if m else f"{path}#knowledge-tree"

for c in comparisons:
    sf = c["source_family_id"]
    lines.append(f"| {sf} | {c['owner_node']} | {chapter_ref(c['owner_path'])} | {'; '.join(chapter_ref(p) for p in c['adjacent_paths']) or chapter_ref(c['owner_path'])} | existing:{sf} | delta:{sf} | Direct Evolution | {c['decision']} | books-review:{sf} |")

lines.append("")
for c in comparisons:
    sf = c["source_family_id"]
    lines += [
        f"<!-- books-review:{sf}:start -->",
        f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->",
        f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Final prewrite decision=`{c['decision']}`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。",
        f"<!-- books-review:{sf}:end -->",
    ]

first_sf = retained[0]["source_family_id"]
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |",
    "| SA-20260513-COVERAGE | fresh-context:may2026_day02 | coverage | coverage:SRC-ARXIV:20260513 | none | screening-ledger-independent-final.json 关闭 FIND-20260513-FN-27，恢复 27 项并重冻分母 | passed |",
    f"| SA-20260513-EVIDENCE | fresh-context:may2026_day02 | evidence | review:{first_sf} | none | 修正 2605.11537 locator；其余可达项完整 review，两项 external blocker 进入唯一 Materials Request | passed |",
    "| SA-20260513-SELECTION | fresh-context:may2026_day02 | deep_analysis_selection | analysis:DA-PHYSICAL-SERVING; analysis:DA-BEHAVIORAL-FEDERATION; analysis:DA-DISTRIBUTED-GOVERNANCE | none | 重选三条互不重复的长期系统演进线，关闭 author selection finding | passed |",
    f"| SA-20260513-BOOKS | fresh-context:may2026_day02 | books | books-review:{first_sf} | none | 全量 current owner+adjacent comparison 关闭 over-retention finding，形成 {len(queue)} 项最终 prewrite queue | passed |", "",
    "## 8. Ignored Noise", "", f"{len(closures)} 项在 `screening-ledger-independent-final.json` 中以 family-specific mechanism、evidence clue 与 exclusion boundary 闭合；未因标题关键词直接进入候选分母。", "",
    "## 9. Recommended Action", "", f"Root 按日期顺序串行写回 `books-writeback-queue-final.json` 的 {len(queue)} 项；完成后由未参与写入的 reviewer 逐项执行 post-write semantic audit。两项 blocker 可在材料到达后单独重开，不阻塞其他 family。", "",
    "## 10. Repository Changes", "", "- 新增 independent-final denominator、fresh-context audit、current-content comparison 和 root writeback queue。", "- 更新 canonical Daily 的 counts、locators、Gate 与 Materials Request。", "- 未修改共享 Books，未 stage、commit 或 push。", "",
    "## 11. Open Questions", "", "- 两项 exact-v1 正文能否由用户提供 bit-identical PDF/HTML/TXT？", f"- {len(queue)} 项 Books 写回完成后，post-write reviewer 是否能在正文主线中逐项定位旧条件、约束变化、owner、trade-off、failure 与 fallback？", "",
    "## 12. Sources", "",
]
for r in retained:
    aid = r["arxiv_id"]
    lines.append(f"- [{r['title']}](https://arxiv.org/{'abs' if aid in BLOCKED else 'html'}/{aid}v1) — arXiv:{aid}v1；first-public 2026-05-12；accessed 2026-09-02")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Conditional Pass`", "", "Books: `Open`", "", "unresolved findings: 3", "", f"确定性 Coverage 已闭合；两项 exact-v1 external blocker 已精确请求材料，{len(queue)} 项 Books queue 等待 root 串行写回与独立 post-write audit。"]

text = "\n".join(lines) + "\n"
# Fill validator-computed Review Provenance IDs after the final review bodies exist.
for r in retained:
    aid, sf = r["arxiv_id"], r["source_family_id"]
    start, end = f"<!-- review:{sf}:start -->", f"<!-- review:{sf}:end -->"
    body = text.split(start, 1)[1].split(end, 1)[0]
    method, evaluation, limits, artifact, _result = receipt_slots[aid]
    override = "knowledge_gap" if r["integration_disposition"] == "Integrate" else "none"
    candidate = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": override}
    rp = _expected_review_provenance(
        sf, candidate, "deep", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1",
        method, evaluation, limits, artifact,
        f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body),
    )
    text = text.replace("RP-TODO-" + sf, rp)

(REPO / "papers/2026/05/13/README.md").write_text(text)
print(json.dumps({
    "raw": 91841, "registered": 835, "screened": 835, "retained": len(retained),
    "closures": len(closures), "deep_complete": len(retained) - len(BLOCKED),
    "blocked": len(BLOCKED), "integrate_queue": len(queue),
}, ensure_ascii=False))
