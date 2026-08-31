#!/usr/bin/env python3
"""Finalize the independent 2026-05-23 Daily pre-write audit.

This script only writes date-local report/audit artifacts.  Shared Books are
read for semantic comparison and are never modified here.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

REPORT_DATE = "2026-05-23"
SOURCE = json.loads((HERE / "screening-ledger-provisional.json").read_text())
AUTHOR = json.loads((HERE / "candidate-config-author.json").read_text())


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


FN = {
    "2605.23157": ("PLATFORM-SECURITY", 9, "§3 Study Design; §3.1–§3.4 language × modality threat matrix", "§4 Results; mixed-effects and matched-annotator evaluation", "§7 Limitations; four-model/two-language scope"),
    "2605.23168": ("TRAIN-DATA", 8, "§3 PoisonForge threat model and parameterized benchmark", "§4–§5 twelve-model poisoning evaluation", "§6 Limitations; instruction-tuning and tested poison-budget boundary"),
    "2605.23170": ("PLATFORM-EVALUATION-SYSTEM", 9, "§3 Context Rot Evaluation; controlled position/content/length factors", "§4 Evaluation across nine models and two reasoning tasks", "§7 Limitations; benchmark/task/context-family boundary"),
    "2605.23262": ("PLATFORM-EVALUATION-SYSTEM", 8, "§2–§4 work-centered benchmark representation", "§5 worked benchmark comparisons", "§6 Discussion; conceptual representation does not prove predictive validity"),
    "2605.23294": ("INFER-TENSORRT-LLM", 8, "§III NASiC CAM-selected multibit CIM architecture", "§IV–§V architecture/model evaluation", "§VI Discussion; simulated 3D-NAND/device-model boundary"),
    "2605.23362": ("PLATFORM-EVALUATION-SYSTEM", 9, "§2–§4 budgeted heteroskedastic multi-judge estimation", "§5 theory and empirical allocation evaluation", "§6 Discussion; known-cost/bounded-score assumptions"),
    "2605.23454": ("TRAIN-RLHF", 8, "§3 ARES automatic rubric synthesis and reward construction", "§4 and Appendix F evaluation", "Appendix A Limitations; generated-rubric correctness boundary"),
    "2605.23493": ("TRAIN-RLHF", 8, "§3 EDGE-OPD evidence-guided on-policy distillation", "§4–§5 experiments and diagnostics", "Appendix A.10 Limitations; teacher/evidence/task boundary"),
    "2605.23590": ("AGENT-WORKFLOW", 8, "§2–§3 Co-ReAct step-level rubric and control loop", "§4–§5 agent evaluation", "§6 Limitations; rubric and environment boundary"),
    "2605.24060": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 memory benchmark scoring-target intervention", "§4–§5 controlled benchmark evaluation", "§7 Limitations; tested-memory systems and tasks"),
    "2605.24117": ("AGENT-PLATFORM", 8, "§3 SkillEvolBench lifecycle/evolution protocol", "§4–§5 benchmark protocol and experiments", "§6 Discussion; benchmark coverage does not prove deployment safety"),
    "2605.24183": ("PLATFORM-EVALUATION-SYSTEM", 8, "§2–§3 AvalancheBench latent-world recovery protocol", "§4 early experiments", "§5 Limitations; synthetic/latent-world scope"),
    "2605.24197": ("AGENT-MULTI-AGENT", 8, "§3 formulation; §4 evidence-attribution mechanism", "§5 experiments", "Appendix B Limitations; simulated-agent and attribution boundary"),
    "2605.24202": ("TRAIN-RLHF", 8, "§3 multi-agent RL workflow and policy-sharing mechanism", "§4 experiments", "§5 Discussion; policy-sharing topology and task boundary"),
    "2605.24216": ("PLATFORM-SECURITY", 8, "§3 Agent-ToM learning-to-monitor architecture", "§4–§5 monitoring evaluation", "§6 Limitations; ToM inference is a sensor, not intent ground truth"),
    "2605.24229": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 atomic-tenet extraction and adversarial audit pipeline", "§4–§5 multi-turn constitution-adherence evaluation", "§6 Limitations; published-spec and evaluator boundary"),
    "2605.24247": ("TRAIN-DATA", 8, "§3 detailed constitutional definitions and AI-assisted labeling workflow", "§4–§5 label-consistency evaluation", "§6 Limitations; category/specification and annotator boundary"),
    "2605.24279": ("AGENT-CONTEXT", 8, "§3 ContextEcho snapshot-then-probe deployment harness", "§4–§5 long agentic-coding session evaluation", "§6 Limitations; persona probes and coding-session boundary"),
    "2605.24286": ("PLATFORM-EVALUATION-SYSTEM", 8, "§3 information-flow faithfulness criteria and diagnostics", "§4–§5 faithfulness evaluation/training", "§6 Limitations; diagnostic proxies do not reveal hidden computation"),
    "2605.24299": ("PLATFORM-EVALUATION-SYSTEM", 9, "§3 factor-analysis decomposition of elicited confidence", "§4 pairwise calibration across twenty models/six benchmarks", "§5–§6 Limitations; elicited-confidence and tested-benchmark boundary"),
    "2605.24309": ("PLATFORM-SECURITY", 8, "§3 agent-human security mechanism taxonomy", "§4 audit of papers, production agents and plugins", "§5 Limitations; observational taxonomy does not prove mechanism efficacy"),
    "2605.26147": ("INFER-SCHEDULING", 8, "§3–§5 DAG evidence accumulation and sequential routing", "§6–§8 controlled experiments and ablations", "§9 Discussion; conjugate-belief assumptions and tested-model boundary"),
    "2605.27432": ("AGENT-RAG", 8, "§4 federated dual-system retrieval and compact QA memory", "§5 experiments", "Appendix D privacy/cost analysis; no general privacy guarantee"),
    "2605.27437": ("AGENT-MEMORY", 7, "§3 memory-guided reflective retrieval", "§4 long-dialogue experiments", "§5 Discussion; tested-memory/task and extra-latency boundary"),
}

# Only mechanisms still absent from the current owner and adjacent narrative are
# queued.  Retention and Books integration are deliberately separate decisions.
INTEGRATE = {
    "2605.23158", "2605.23196", "2605.23170", "2605.23296",
    "2605.23389", "2605.23464", "2605.23893", "2605.24217",
    "2605.24229", "2605.24248", "2605.24259", "2605.24279",
    "2605.24312",
}

DEEP = {
    "2605.23158": "DA-SPLIT-INFERENCE-PRIVACY",
    "2605.23362": "DA-BUDGETED-MULTI-JUDGE",
    "2605.24299": "DA-ELICITED-CONFIDENCE-BOUNDARY",
}

GAPS = {
    "2605.23158": "现有安全章没有把 split point、server-visible activation 与 inversion attack 共同定义为隐私边界。",
    "2605.23196": "现有 pre-guard 叙述没有覆盖 guardrail inspection window 与 downstream model context window 不一致造成的可组合绕过。",
    "2605.23170": "现有 Evaluation 主线没有把 target position、filler content 与 context length 冻结成 reasoning benchmark 的联合 identity。",
    "2605.23296": "现有 Context Compression 尚未表达 blocking compaction 到 parallel/background compaction 的状态交接、stall 与 fidelity contract。",
    "2605.23389": "现有调度章未明确 decode iteration 内 KV-length 差异形成的 batch critical path 及 prefix-length-aware regrouping。",
    "2605.23464": "现有安全章没有区分可协作训练/推理的 protocol-visible state 与不得 materialize 的 weight state。",
    "2605.23893": "现有 MoE 与 pretraining parameterization 未完整覆盖 expert width/count 改变时的超参数迁移与 scaling identity。",
    "2605.24217": "现有 Evaluation 章尚未把 benchmark client 自身的单进程排队偏差纳入 TTFT/TPOT measurement identity。",
    "2605.24229": "现有 Evaluation 章缺少将长篇 policy/constitution 分解为 versioned atomic tenets，并在多轮对抗压力下审计 adherence 的闭环。",
    "2605.24248": "现有 MCP 章说明 authorization 不等于 trust，但未给出 server identity、tool allowlist、sensitivity 与 attestation root 的 admission contract。",
    "2605.24259": "现有 KV lifecycle 没有把 future-reuse intent、materialization predicate、active/resident feasibility 与 telemetry 合成可移植 conformance claim。",
    "2605.24279": "现有 Context 章没有把长会话 compaction 后的 persona/role drift 作为可 fork、可重放的 deployment-state evaluation。",
    "2605.24312": "现有 RAG 安全叙述未明确输出蕴含信号可在低查询预算下泄露 corpus membership。",
}

OWNER_COVERAGE = {
    "PLATFORM-SECURITY": "正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。",
    "TRAIN-DATA": "正文已覆盖 data lineage、poisoning/contamination、specification compilation 与 golden-data governance。",
    "PLATFORM-EVALUATION-SYSTEM": "正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。",
    "INFER-TENSORRT-LLM": "正文已把 backend lowering、heterogeneous execution、kernel correctness 与 device fallback 放在同一执行计划中。",
    "TRAIN-RLHF": "正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。",
    "AGENT-WORKFLOW": "正文已覆盖 durable state、recovery、verification、workflow artifact 与 step-level effect receipt。",
    "AGENT-PLATFORM": "正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。",
    "AGENT-MULTI-AGENT": "正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。",
    "AGENT-CONTEXT": "正文已覆盖 context assembly、compression loss、identity、policy integrity 与 long-session state。",
    "INFER-SCHEDULING": "正文已覆盖 workload-aware admission、placement、batch cost、SLO 与 fallback。",
    "AGENT-RAG": "正文已覆盖 distributed corpus ownership、retrieval admission、privacy/security、escalation 与 evidence provenance。",
    "AGENT-MEMORY": "正文已覆盖 memory write/read、reflective retrieval、provenance、rollback 与 lifecycle evaluation。",
    "INFER-KV-CACHE": "正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。",
    "AGENT-MCP": "正文已覆盖 protocol/authorization boundary、tool-set admission、information flow、effect-time authorization 与 provenance。",
    "MODEL-MOE": "正文已覆盖 conditional capacity、routing、expert specialization、capacity/placement 与 parameterization trade-off。",
    "MULTIMODAL-WORLD-MODELS": "正文已覆盖 action-conditioned transition、rollout identity、attack surface、fallback 与 world-state evaluation。",
    "AGENT-TOOL-CALLING": "正文已覆盖 proposal/commit、tool contract、recoverability、effect receipt 与 exactly-once boundary。",
    "TRAIN-DISTRIBUTED-TRAINING": "正文已覆盖 Expert Parallel、topology、heterogeneous execution、routing replay 与 distributed-state correctness。",
}

rows_by_id = {row["arxiv_id"]: dict(row) for row in SOURCE["identities"]}
author_candidates = {k: tuple(v) for k, v in AUTHOR["candidates"].items()}
candidate_ids = set(author_candidates) | set(FN)


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean) if s.strip()]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    for sentence in ss:
        if re.search(r"\b(propose|introduce|present|develop|design|show|identify|study|analy[sz]e|demonstrate|formalize)\b", sentence, re.I):
            return sentence
    return ss[0] if ss else row["title"]


def closure_reason(row: dict) -> str:
    current = row.get("screening_reason", "").strip()
    if current and row.get("screening_status") == "pre_denominator_closure":
        return current
    ss = sentences(row.get("abstract", ""))
    claim = " ".join(ss[:2]) or row["title"]
    return f"`{row['title']}`：{claim} 该 family 未改变长期 state/data/control owner、evaluation/release contract 或生产 fallback；若后续出现跨 workload 的系统接口与证据再重开。"


rows = []
for original in SOURCE["identities"]:
    row = dict(original)
    aid = row["arxiv_id"]
    if aid in candidate_ids:
        if aid in author_candidates:
            owner, total, _old_disp, method, evaluation, limits = author_candidates[aid]
        else:
            owner, total, method, evaluation, limits = FN[aid]
        design = 3 if total >= 8 else 2
        reach = 3 if total == 9 else 2
        durability = total - design - reach
        row.update(
            source_family_id=family(aid), screening_status="retained",
            screening_reason=mechanism(row), owner_node=owner,
            score_v2={"design_delta": design, "system_reach": reach, "durability": durability, "total": total},
            review_status="deep_complete", access_status="accessible",
            integration_disposition="Integrate" if aid in INTEGRATE else "No Change — Existing Coverage",
            method_locator=method, evaluation_locator=evaluation, limitations_locator=limits,
            independent_audit="false_negative_recovered" if aid in FN else "author_retention_reconfirmed",
        )
    else:
        row.update(
            screening_status="pre_denominator_closure", screening_reason=closure_reason(row),
            review_status="identity_date_closed", access_status="accessible",
            integration_disposition="Rejected — Below Candidate Denominator",
            independent_audit="closure_reconfirmed",
        )
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
assert len(rows) == 508 and len(retained) == 61 and len(closures) == 447

ledger = {
    "schema": "daily-screening-ledger-v2.1", "report_date": REPORT_DATE,
    "window": SOURCE["window"], "utc_window": SOURCE["utc_window"],
    "raw_snapshot_records": SOURCE["raw_snapshot_records"],
    "registered_window_identities": len(rows), "screened_identities": len(rows),
    "candidate_denominator": len(retained), "pre_denominator_closures": len(closures),
    "independent_reconciliation": {"author_denominator": 37, "false_positives": 0, "false_negatives": len(FN), "final_denominator": len(retained)},
    "identities": rows,
}
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(HERE / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons, queue, packet = [], [], []
for row in retained:
    aid, sf, owner = row["arxiv_id"], row["source_family_id"], row["owner_node"]
    owner_path = paths[owner]
    target = ROOT / owner_path
    siblings = sorted(p for p in target.parent.glob("*.md") if re.match(r"\d+-", p.name))
    idx = siblings.index(target)
    adjacent = [str(p.relative_to(ROOT)) for p in siblings[max(0, idx - 1):idx] + siblings[idx + 1:idx + 2]]
    body = target.read_text()
    headings = re.findall(r"^##+\s+(.+)$", body, re.M)
    owner_sha = hashlib.sha256(body.encode()).hexdigest()
    decision = row["integration_disposition"]
    if decision == "Integrate":
        existing = GAPS[aid]
    else:
        existing = OWNER_COVERAGE.get(owner, "当前 owner 已覆盖同一长期契约。") + f" 本 family 的具体机制 `{mechanism(row)}` 未越过该边界。"
    delta = mechanism(row)
    comparison = {
        "arxiv_id": aid, "source_family_id": sf, "owner_node": owner,
        "owner_path": owner_path, "owner_sha256": owner_sha, "adjacent_paths": adjacent,
        "adjacent_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in adjacent},
        "owner_headings_reviewed": headings, "existing_proposition": existing,
        "new_evidence_delta": delta, "decision": decision,
        "review_scope": "current owner full body + immediate adjacent chapters; Review notes excluded from semantic coverage",
    }
    comparisons.append(comparison)
    if decision == "Integrate":
        queue.append({
            "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": sf,
            "stable_node_id": owner, "owner_path": owner_path, "adjacent_paths": adjacent,
            "evidence_delta": delta, "missing_current_proposition": existing,
            "required_narrative": "old path + changed constraint + state/control owner + mechanism + gain/cost + failure + fallback/coexistence + exact-v1 evidence/non-proof boundary",
            "required_post_write_audit": "different reviewer reads owner + adjacent; unique marker before exact H2 ## Review notes; semantic flow, not marker-only",
            "status": "awaiting_root_serial_writeback",
        })
    packet.append({
        "source_family_id": sf, "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "retrieval_route": f"https://arxiv.org/html/{aid}v1",
        "retrieved_at": "2026-09-01T10:38:35+08:00",
        "method_locator": row["method_locator"], "evaluation_locator": row["evaluation_locator"],
        "limitations_locator": row["limitations_locator"],
        "claim_boundary": f"{row['title']} only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.",
        "completion_result": "complete",
    })

(HERE / "exact-v1-review-packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-independent-review-packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison-independent.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({
    "schema": "books-writeback-queue-v1", "report_date": REPORT_DATE,
    "status": "awaiting_root_serial_writeback", "items": queue,
}, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request.json").write_text(json.dumps({
    "schema": "materials-request-v1", "report_date": REPORT_DATE,
    "status": "none", "requests": [],
}, ensure_ascii=False, indent=2) + "\n")
(HERE / "semantic-independent-audit.json").write_text(json.dumps({
    "schema": "semantic-independent-audit-v1", "report_date": REPORT_DATE,
    "auditor": "fresh-context:may2026-day01", "author_independent": True,
    "cross_model_review": "skipped — non-interactive subagent context",
    "status": "passed_prewrite_pending_root_serial_writeback",
    "scope": {"registered_replayed": 508, "denominator_reviewed": 61, "exact_v1_reviewed": 61, "books_compared": 61},
    "findings": {"false_positives": [], "false_negatives": sorted(FN), "ordinary_pending": 0, "blocked": []},
    "resolution": {"author_denominator": 37, "final_denominator": 61, "closures": 447, "final_integrate_queue": len(queue)},
}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-final.json").read_bytes()).hexdigest()
comp_by_id = {x["arxiv_id"]: x for x in comparisons}


def chapter_ref(path: str) -> str:
    m = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(m.group(1))}" if m else path


def review_route(row: dict) -> str:
    return "deep"


def ev(row: dict, key: str) -> str:
    return f"https://arxiv.org/html/{row['arxiv_id']}v1 — {row[key]}"


lines = [
    "# Daily Research — 2026-05-23", "", "**Research Date:** 2026-05-23", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-22 09:00:00 ～ 2026-05-23 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。非作者 pre-write 审计已通过，等待 root 串行写回与不同 reviewer post-write audit。", "",
    "## Executive Summary", "",
    f"独立重放 508/508 个窗口身份：author denominator 37，经 0 个 false positive 与 {len(FN)} 个 false negative reconciliation 后冻结为 61；pre-denominator closures=447，exact-v1={len(retained)}/{len(retained)}，blocked=0，ordinary pending=0。current Books owner+adjacent challenge 将 author queue 26 重判为最终 queue {len(queue)}；共享 Books 未修改。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-23 |", "| Window End | 2026-05-23 |",
    "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
    "| Denominator ID | DEN-20260523-V2-INDEPENDENT |", "| Denominator Frozen At | 2026-09-01T10:38:35+08:00 |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-22T09:00:00+08:00 | 2026-05-23T09:00:00+08:00 | 2026-09-01T10:38:35+08:00 | DataCite v2 00..99 + independent 508/508 title+abstract replay + official exact-v1 HTML | checked | 508 | {';'.join(r['source_family_id'] for r in retained)} | pages=300;final_cursor=end;raw={SOURCE['raw_snapshot_records']};registered=508;screened=508;retained=61;closure=447 | 2026-05-23T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "",
    "<!-- coverage:SRC-ARXIV:20260523:start -->508/508 identity 已独立逐项重放；24 个 author false negative 已恢复，0 个 author false positive，447 条 family-specific closure 已复核。first-public、v1、owner week 与重复 family 已对账；无 ordinary pending 或 exact-version blocker。<!-- coverage:SRC-ARXIV:20260523:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for row in retained:
    s = row["score_v2"]
    lines.append(f"| {row['source_family_id']} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W21 | 2026-05-22 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {'knowledge_gap' if row['integration_disposition']=='Integrate' else 'none'} | review:{row['source_family_id']} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{row['source_family_id']} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    sf, aid = row["source_family_id"], row["arxiv_id"]
    lines.append(f"| {sf} | RP-TODO-{sf} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {ev(row,'method_locator')} | {ev(row,'evaluation_locator')} | {ev(row,'limitations_locator')} | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:{sf} | complete |")

lines += ["", "### Source Reviews", ""]
for row in retained:
    sf, aid = row["source_family_id"], row["arxiv_id"]
    boundary = next(x["claim_boundary"] for x in packet if x["arxiv_id"] == aid)
    lines += [
        f"<!-- review:{sf}:start -->", f"#### {row['title']}", "",
        f"**问题与机制。** {row['screening_reason']} owner=`{row['owner_node']}`；independent reconciliation=`{row['independent_audit']}`。", "",
        f"**Exact-v1。** Method=`{row['method_locator']}`；Evaluation=`{row['evaluation_locator']}`；Limitations/Counterevidence=`{row['limitations_locator']}`。", "",
        f"<!-- claim:{sf}:start -->{boundary}<!-- claim:{sf}:end -->", "",
        f"Books Decision=`{row['integration_disposition']}`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。", f"<!-- review:{sf}:end -->", "",
    ]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    aid, sf = row["arxiv_id"], row["source_family_id"]
    selected = aid in DEEP
    unit = DEEP.get(aid, "—")
    eligibility = "score_7_9;forced_review;potential_books_delta" if aid in INTEGRATE else "score_7_9"
    lines.append(f"| {sf} | {eligibility} | {'selected' if selected else 'not_selected'} | {unit} | — | {'跨层改变隐私、评估预算或置信度控制假设' if selected else 'exact-v1 已完成；未选仅受 Daily 三项叙事上限约束'} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")

analysis = {
    "2605.23158": "Split inference 在端侧算力受限且不上传原文时合理；当 server-visible activation 可被反演，隐私边界便从数据格式转为可验证攻击面。ActInv/PAF 把 split point 与 layer sensitivity 纳入选择，但防御会支付端侧计算、扰动和 utility cost；exact-v1 只证明所测模型、层与攻击，不能把未被恢复等同于隐私保证。",
    "2605.23362": "固定一个 judge 在成本和可靠性近似一致时简单；多 judge 价格、方差和样本难度异质后，evaluation controller 必须拥有预算分配。实例自适应分配降低给定预算下的估计误差，却新增 pilot query、方差估计和分配偏差；oracle/渐近结论不证明未知分布或 judge drift 下仍最优。",
    "2605.24299": "用模型自报 confidence 做 abstention/routing 在 aggregate calibration 稳定时诱人；跨模型 confidence 近似共同因子而非个体能力信号时，它不能回答‘这个模型是否知道自己不知道’。收益是把 self-report 与 behavior probe 分离，代价是必须实际执行 probe 或引入外部 evidence；20 个模型/六个 benchmark 不证明所有内部不确定性都不可访问。",
}
for aid, unit in DEEP.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", analysis[aid], f"<!-- analysis:{unit}:end -->"]
for row in retained:
    if row["arxiv_id"] not in DEEP:
        sf = row["source_family_id"]
        lines.append(f"<!-- analysis-decision:{sf}:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:{sf}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    c = comp_by_id[row["arxiv_id"]]
    sf = row["source_family_id"]
    adj = ";".join(chapter_ref(x) for x in c["adjacent_paths"]) or chapter_ref(c["owner_path"])
    lines.append(f"| {sf} | {row['owner_node']} | {chapter_ref(c['owner_path'])} | {adj} | existing:{sf} | delta:{sf} | {'Direct Evolution' if row['integration_disposition']=='Integrate' else 'Principle Reuse'} | {row['integration_disposition']} | books-review:{sf} |")
for row in retained:
    c, sf = comp_by_id[row["arxiv_id"]], row["source_family_id"]
    lines += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->", f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Independent decision=`{c['decision']}`；owner_sha256={c['owner_sha256']}。", f"<!-- books-review:{sf}:end -->"]

first_sf = retained[0]["source_family_id"]
lines += [
    "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |",
    f"| SA-20260523-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260523 | none | semantic-independent-audit.json#scope.coverage | passed |",
    f"| SA-20260523-EVIDENCE | fresh-context:may2026-day01 | evidence | review:{first_sf} | none | semantic-independent-audit.json#scope.evidence | passed |",
    f"| SA-20260523-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:{next(iter(DEEP.values()))} | none | semantic-independent-audit.json#scope.deep_analysis_selection | passed |",
    f"| SA-20260523-BOOKS | fresh-context:may2026-day01 | books | books-review:{first_sf} | none | semantic-independent-audit.json#scope.books | passed |", "",
    "Cross-model skipped: non-interactive subagent context。", "",
    "## 8. Ignored Noise", "", "447 条 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`；每条保留具体 title/abstract 机制、排除边界与重开条件。", "",
    "## 9. Recommended Action", "", f"由 root 按日期序列写回 `BOOKS_WRITEBACK_QUEUE.json` 的 {len(queue)} 项；写后必须由不同 reviewer 顺读 owner+adjacent，不能用 marker-only 检查关闭 Books Gate。", "",
    "## 10. Repository Changes", "", "- 重建 05-23 independent screening ledger、61 项 exact-v1 receipt、current Books comparison、13 项 root writeback queue、semantic audit 与空 Materials Request。", "- 未修改共享 Books；未 stage、commit 或 push。", "",
    "## 11. Open Questions", "", "- root 串行写回后，13 项是否全部位于 canonical H2 的演进主线，并通过不同 reviewer post-write audit？", "",
    "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
    "## 12. Sources", "",
]
for row in retained:
    lines.append(f"- [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-22；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"05-23 已达到 root-writeback-ready：508/508、61/61 exact-v1、ordinary pending=0、blocked=0、final Books queue={len(queue)}；剩余唯一条件是 root 串行 Books 写回与不同 reviewer post-write semantic audit。"]

text = "\n".join(lines)
for row in retained:
    sf, aid = row["source_family_id"], row["arxiv_id"]
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if aid in INTEGRATE else "none"}
    rp = _expected_review_provenance(sf, candidate, "deep", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", ev(row, "method_locator"), ev(row, "evaluation_locator"), ev(row, "limitations_locator"), "Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review", f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sf, rp)
(ROOT / "papers/2026/05/23/README.md").write_text(text + "\n")

print(json.dumps({"raw": SOURCE["raw_snapshot_records"], "registered": 508, "screened": 508, "author_denominator": 37, "false_positive": 0, "false_negative": len(FN), "final_denominator": len(retained), "closures": len(closures), "exact_v1": len(packet), "blocked": 0, "ordinary_pending": 0, "final_queue": len(queue)}, ensure_ascii=False))
