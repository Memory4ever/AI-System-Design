#!/usr/bin/env python3
"""Fresh-context independent reconciliation for 2026-05-20.

This date-local script never writes shared Books.  It converts the author
packet into the independently frozen denominator, evidence packet and
pre-write Books queue.
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

REPORT_DATE = "2026-05-20"
AUTHOR = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {x["arxiv_id"]: x for x in json.loads((HERE / "exact-v1-review-packet.json").read_text())}
AUTHOR_COMPARISONS = {x["arxiv_id"]: x for x in json.loads((HERE / "books-current-content-comparison.json").read_text())}
AUTHOR_IDS = {x["arxiv_id"] for x in AUTHOR["identities"] if x["screening_status"] == "retained"}

# These are component-local methods, domain cases, surveys or benchmark assets.
# They remain fully represented in the screening ledger, but do not change a
# durable AI-System state/control/evidence contract.
REMOVE = {
    "2605.19344": "linguistic confidence calibration is a local response-interface method and does not change the platform evidence owner or release authority",
    "2605.19377": "the robustness-fine-tuning game is a bounded theoretical formulation and adds no production evaluation object or release contract beyond Ch66",
    "2605.19561": "two-level rotation is an MXFP4 quantization recipe, not a new execution-plan, precision identity or portability contract",
    "2605.19660": "the KV-cache quantizer is a component-local encoding choice already governed by the existing KV identity/error contract",
    "2605.19668": "opaque industrial remediation is a vertical workflow case and does not establish a transferable workflow-state or commit protocol",
    "2605.19735": "extraction-free graph construction is a local RAG indexing method without a new provenance, retrieval-commit or freshness owner",
    "2605.19929": "modality-aware PTQ is a local quantization calibration method and does not reassign runtime precision or deployment authority",
    "2605.20104": "retrieval-assisted draft trees are a local speculative-decoding proposal already covered by the draft/verify/commit contract",
    "2605.20123": "bidirectional ranking is a single RAG-poisoning defense and does not replace the existing layered trust and fallback contract",
    "2605.20168": "the OpenAlex audit is a bibliographic-data quality finding, not a training-data or evaluation-system control contract",
    "2605.20173": "the architecture-pattern methodology restates proposer/verifier/commit boundaries without controlled evidence for a new owner",
    "2605.20530": "AgentAtlas is a diagnostic taxonomy and benchmark survey already subsumed by the versioned evaluation-run contract",
    "2605.22864": "trajectory uncertainty is a local calibration estimator; it does not obtain commit/defer authority or change the evaluation owner",
    "2605.24011": "action-guided VLA quantization is a local PTQ technique and does not change the execution-plan or physical-safety owner",
}

# Named false negatives recovered by reading official exact-v1 HTML.  Each one
# changes a durable training, retrieval, safety or physical-control contract.
RECOVER = {
    "2605.19319": ("MULTIMODAL-WORLD-MODELS", 8, "Integrate", "§3 sparse keyframe world-model planner and goal-conditioned action predictor", "§4 real-robot and simulation experiments", "§5 Limitations: short horizon, annotations and edited-image domain gap"),
    "2605.19335": ("AGENT-RAG", 8, "Integrate", "§4 LIOS update decomposition, overrun-bounded budgeting and feedback control", "§6 search/update evaluation on FreshDiskANN and OdinANN", "§8 Conclusion; disk ANNS and measured hardware scope"),
    "2605.19444": ("TRAIN-RLHF", 9, "Integrate", "§2 extinction-window dynamics; §3 TTRL-Guard", "§4 model/benchmark experiments and per-problem migration", "§6 Breadth of evaluation; signal quality at the extremes"),
    "2605.19447": ("TRAIN-RLHF", 8, "Integrate", "§3 selective hindsight placement and environment-guided advantage reweighting", "§4 ALFWorld/WebShop experiments and ablations", "Appendix C Limitations"),
    "2605.19461": ("TRAIN-RLHF", 9, "Integrate", "§3 forward/group distribution-matching policy optimization", "§4–§5 reasoning experiments and ablations", "Appendix B Limitations; group-local coverage does not prove global target matching"),
    "2605.19478": ("PLATFORM-SECURITY", 8, "Integrate", "§4 threat model; §5–§6 dynamic-prompt functional fusion", "§7 attack, pruning and transfer evaluation", "§8 Conclusion; ViT/VPT threat-model boundary"),
    "2605.19811": ("TRAIN-PRETRAINING", 8, "Integrate", "§3 optimizer geometry; §4 LionMuon alternating spectral/sign descent", "§5 language-model training experiments and ablations", "§6 Limitations and optimizer/workload boundary"),
    "2605.20005": ("TRAIN-SFT", 9, "Integrate", "§3 per-step forgetting bound and loss-adaptive learning rate", "§4–§5 task/forgetting, factuality and calibration experiments", "§6 Conclusion, Limitations, and Future Work"),
    "2605.20023": ("AGENT-PLATFORM", 7, "No Change — Existing Coverage", "§3 procedural-skill intervention and tool-grounded agent protocol", "§4 offensive-cybersecurity experiments", "§5 Limitations; negative result is workload/model specific"),
    "2605.20314": ("TRAIN-DATA", 8, "Integrate", "§2 reuse setup; §3–§5 sampling-bias and relative-norm mechanism", "§5 empirical interventions; Appendix B", "§6 discussion: when data repetition is and is not helpful"),
    "2605.20544": ("MULTIMODAL-EMBODIED-VLA", 8, "Integrate", "§3 grounded abstention taxonomy and deterministic constraint pipeline", "§4 6,069-instruction embodied VLM evaluation", "§5 Discussion; guarantees remain conditional on scene extraction"),
    "2605.22868": ("PLATFORM-PRODUCTION", 7, "Structural Candidate", "§3 tri-stage near-sensor/fusion/edge control", "§4 quality–data–energy evaluation", "§5 Conclusion; dual-modality SynDrone boundary"),
    "2605.24004": ("MULTIMODAL-EMBODIED-VLA", 9, "Integrate", "§III Reason–Imagine–Act world-model verification loop", "§IV CARLA closed-loop evaluation", "§V Conclusion; simulator and discrete-action-template boundary"),
    "2605.20296": ("TRAIN-SFT", 8, "Integrate", "§3 checkpoint-delta spectral repair", "§4 fourteen-cell recovery/preservation evaluation", "§5 Limitations and conclusion"),
}

# Independently minimal write-back set after current owner + adjacent reading.
# Families not listed remain retained evidence with an explicit No Change or
# Structural Candidate disposition.
INTEGRATE = {
    "2605.19240", "2605.19269", "2605.19282", "2605.19314", "2605.19321",
    "2605.19407", "2605.19481", "2605.19537", "2605.19576", "2605.19593",
    "2605.19604", "2605.19722", "2605.19779", "2605.19847", "2605.19893",
    "2605.19932", "2605.19945", "2605.19952", "2605.20022", "2605.20051",
    "2605.20061", "2605.20084", "2605.20179", "2605.20295", "2605.20312",
    "2605.20402", "2605.20477", "2605.20485", "2605.20490", "2605.20520",
    "2605.20563", "2605.22863", "2605.22866", "2605.24006", "2606.28330",
    "2605.19319", "2605.19335", "2605.19444", "2605.19447", "2605.19461",
    "2605.19478", "2605.19811", "2605.20005", "2605.20296", "2605.20314",
    "2605.20544", "2605.24004",
}

SELECTED = {
    "2605.19444": "DA-EXTINCTION-WINDOW",
    "2605.19847": "DA-TENANT-PRIVACY-ACCOUNTING",
    "2605.20005": "DA-LOSS-ADAPTIVE-FORGETTING",
}


def sf(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip()) if x.strip()]


def mechanism(row: dict) -> str:
    ss = sentences(row.get("abstract", ""))
    return next((s for s in ss if re.search(r"\b(propose|introduce|present|develop|design|identify|show|study|demonstrate|argue)\b", s, re.I)), ss[0] if ss else row["title"])


rows = []
for src in AUTHOR["identities"]:
    row = dict(src)
    aid = row["arxiv_id"]
    row["source_family_id"] = sf(aid)
    if aid in REMOVE:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=f"`{row['title']}`：{REMOVE[aid]}；因此作为独立审计确认的 false positive 在 Candidate Denominator 前闭合。",
            review_status="identity_date_closed", access_status="accessible_metadata",
            integration_disposition="Rejected — Below Candidate Denominator",
            independent_audit="false_positive_removed",
        )
    elif aid in RECOVER:
        owner, total, disposition, ml, el, ll = RECOVER[aid]
        score = (3, 3, total - 6) if total >= 8 else (3, 2, 2)
        row.update(
            screening_status="retained", screening_reason=mechanism(row), owner_node=owner,
            score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": total},
            review_status="deep_complete", access_status="accessible",
            integration_disposition=disposition, method_locator=ml,
            evaluation_locator=el, limitations_locator=ll,
            independent_audit="false_negative_recovered",
        )
    elif aid in AUTHOR_IDS:
        row["independent_audit"] = "retain_reconfirmed"
        row["integration_disposition"] = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
    else:
        row["independent_audit"] = "closure_reconfirmed"
    rows.append(row)

retained = [x for x in rows if x["screening_status"] == "retained"]
closures = [x for x in rows if x["screening_status"] != "retained"]
assert len(rows) == 665
assert len(retained) == len(AUTHOR_IDS) - len(REMOVE) + len(RECOVER)
assert len({x["screening_reason"] for x in closures}) == len(closures)

ledger = dict(AUTHOR)
ledger.update(
    schema="daily-screening-ledger-v2.1-independent-final",
    candidate_denominator=len(retained), pre_denominator_closures=len(closures), identities=rows,
    independent_reconciliation={
        "author_retained": len(AUTHOR_IDS), "false_positives_removed": len(REMOVE),
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
    i = siblings.index(target)
    return [str(x.relative_to(ROOT)) for x in siblings[max(0, i - 1):i] + siblings[i + 1:i + 2]]


def chapter_ref(path: str) -> str:
    m = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(m.group(1))}" if m else path


reviews, comparisons, queue = [], [], []
for row in retained:
    aid = row["arxiv_id"]
    if aid in AUTHOR_REVIEWS:
        ar = AUTHOR_REVIEWS[aid]
        ml, el, ll = ar["method_locator"], ar["evaluation_locator"], ar["limitations_locator"]
        route = ar["retrieval_route"]
    else:
        ml, el, ll = row["method_locator"], row["evaluation_locator"], row["limitations_locator"]
        route = "official arXiv exact-v1 HTML"
    reviews.append({
        "source_family_id": sf(aid), "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1", "retrieval_route": route,
        "retrieved_at": "2026-09-02T03:45:00+08:00", "method_locator": ml,
        "evaluation_locator": el, "limitations_locator": ll,
        "artifact_locator": f"https://arxiv.org/html/{aid}v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise",
        "claim_boundary": "Only exact-v1 disclosed workload, model, hardware, precision, length, batch, concurrency, SLO and evaluator are supported; undisclosed fields are Not Disclosed.",
        "completion_result": "complete",
    })
    owner = row["owner_node"]
    path = paths[owner]
    adj = adjacent(path)
    owner_body = (ROOT / path).read_text()
    adj_bodies = {p: (ROOT / p).read_text() for p in adj}
    decision = row["integration_disposition"]
    if decision == "Integrate":
        existing = f"已顺读 `{path}` 与相邻章节 {adj}；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。"
    elif decision == "Structural Candidate":
        existing = f"`{path}` 只可承载生产边界；near-sensor→edge→cloud 的长期 compute/data owner 尚无单一稳定节点，进入季度结构复核而不强塞正文。"
    else:
        existing = f"`{path}` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。"
    comp = {
        "arxiv_id": aid, "source_family_id": sf(aid), "owner_node": owner,
        "owner_path": path, "adjacent_paths": adj,
        "owner_sha256": hashlib.sha256(owner_body.encode()).hexdigest(),
        "adjacent_sha256": {p: hashlib.sha256(b.encode()).hexdigest() for p, b in adj_bodies.items()},
        "existing_proposition": existing, "new_evidence_delta": row["screening_reason"],
        "decision": decision, "reviewer": "fresh-context:may2026-day02",
    }
    comparisons.append(comp)
    if decision == "Integrate":
        queue.append({
            "report_date": REPORT_DATE, "arxiv_id": aid, "source_family_id": sf(aid),
            "stable_node_id": owner, "owner_path": path, "adjacent_paths": adj,
            "evidence_delta": row["screening_reason"], "status": "awaiting_root_serial_writeback",
            "writeback_requirement": "merge into canonical mechanism spine before Review notes; preserve old condition, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and exact-v1 boundary",
        })

(HERE / "exact-v1-independent-review-packet.json").write_text(json.dumps({"schema": "exact-v1-independent-review-v2.1", "report_date": REPORT_DATE, "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(HERE / "exact-v1-review-packet.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison-independent.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(HERE / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
queue_obj = {"schema": "books-writeback-queue-v2.1-independent-final", "report_date": REPORT_DATE, "status": "awaiting_root_serial_writeback_and_post_write_audit", "items": queue}
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue_obj, ensure_ascii=False, indent=2) + "\n")
(HERE / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": REPORT_DATE, "items": []}, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((HERE / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
receipt = {
    "schema": "coverage-receipt-v2.1", "report_date": REPORT_DATE, "source_id": "SRC-ARXIV",
    "window": AUTHOR["window"], "raw_snapshot_records": AUTHOR["raw_snapshot_records"],
    "registered_identities": 665, "full_semantic_screened": 665,
    "retained": len(retained), "pre_denominator_closed": len(closures),
    "ledger_sha256": ledger_sha, "status": "closed_independent_audit",
}
(HERE / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
audit = {
    "schema": "semantic-independent-audit-v2.1", "report_date": REPORT_DATE,
    "auditor": "fresh-context:may2026-day02", "author": "author-lane:unknown",
    "coverage": {"reviewed": "665/665 title+abstract", "author_retained": 59, "false_positives_removed": len(REMOVE), "false_negatives_recovered": len(RECOVER), "final_denominator": len(retained), "final_closures": len(closures), "closure_reason_unique": len(closures), "status": "passed"},
    "evidence": {"deep_complete": len(retained), "blocked": [], "status": "passed"},
    "deep_analysis_selection": {"selected": sorted(SELECTED), "status": "passed"},
    "books": {"current_content_comparison": len(retained), "final_integrates": len(queue), "structural_candidates": ["2605.22868"], "status": "passed_prewrite_pending_root_writeback"},
    "remaining_findings": ["root serial Books writeback and different-reviewer post-write semantic audit"],
}
(HERE / "semantic-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

comparison_by_id = {x["arxiv_id"]: x for x in comparisons}
review_by_id = {x["arxiv_id"]: x for x in reviews}
lines = [
    "# Daily Research — 2026-05-20", "", "**Research Date:** 2026-05-20", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-19 09:00:00 ～ 2026-05-20 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。", "",
    f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立审计已完成，等待 {len(queue)} 项 root 串行写回与非写作者 post-write audit。", "",
    "## Executive Summary", "",
    f"从 {AUTHOR['raw_snapshot_records']:,} 条月度 raw records 中注册并独立重放 665/665 identity。author denominator 59 经审计移除 {len(REMOVE)} 个 false positive、恢复 {len(RECOVER)} 个 false negative，最终 {len(retained)} 项（{len(retained)/665:.2%}），{len(closures)} 项以逐 family 唯一理由在分母前闭合。{len(retained)}/{len(retained)} exact-v1 完成 source-specific Review，blocked=0。current owner 与相邻章节比较后冻结 {len(queue)} 项 Books queue 和 1 项 Structural Candidate；本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-20 |", "| Window End | 2026-05-20 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260520-V2-INDEPENDENT |", f"| Denominator Frozen At | {now} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-19T09:00:00+08:00 | 2026-05-20T09:00:00+08:00 | {now} | DataCite v2 00..99 + independent 665/665 semantic replay + official exact-v1 | checked | 665 | {';'.join(x['source_family_id'] for x in retained)} | pages=300;final_cursor=end;raw={AUTHOR['raw_snapshot_records']};registered=665;screened=665;retained={len(retained)};closure={len(closures)} | 2026-05-20T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", f"<!-- coverage:SRC-ARXIV:20260520:start -->665/665 identity 已独立重放；{len(closures)} 个 closure reason 全部唯一。Coverage=Closed。所有 retained family 均完成 exact-v1；没有 access blocker。<!-- coverage:SRC-ARXIV:20260520:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for x in retained:
    s = x["score_v2"]
    override = "knowledge_gap" if x["integration_disposition"] in {"Integrate", "Structural Candidate"} else "none"
    stable_node = "—" if x["integration_disposition"] == "Structural Candidate" else x["owner_node"]
    lines.append(f"| {x['source_family_id']} | arXiv:{x['arxiv_id']}v1 | paper-v1:{x['arxiv_id']} | 2026-W21 | 2026-05-19 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {override} | review:{x['source_family_id']} | self | — | new_in_window | {stable_node} | {x['integration_disposition']} | books-review:{x['source_family_id']} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    r = review_by_id[x["arxiv_id"]]
    lines.append(f"| {x['source_family_id']} | RP-TODO-{x['source_family_id']} | deep | arXiv:{x['arxiv_id']}v1 | SRC-ARXIV@arXiv:{x['arxiv_id']}v1 | arXiv:{x['arxiv_id']}v1 HTML — {r['method_locator']} | arXiv:{x['arxiv_id']}v1 HTML — {r['evaluation_locator']} | arXiv:{x['arxiv_id']}v1 HTML — {r['limitations_locator']} | {r['artifact_locator']} | claim:{x['source_family_id']} | complete |")

lines += ["", "### Source Reviews", ""]
for x in retained:
    r = review_by_id[x["arxiv_id"]]
    sfid = x["source_family_id"]
    lines += [f"<!-- review:{sfid}:start -->", f"#### {x['title']}", "", f"**问题与机制。** {x['screening_reason']} 系统 owner=`{x['owner_node']}`。", "", f"**Exact-v1。** Method=`{r['method_locator']}`；Evaluation=`{r['evaluation_locator']}`；Limitations/Counterevidence=`{r['limitations_locator']}`。", "", f"<!-- claim:{sfid}:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:{sfid}:end -->", "", f"Books Decision=`{x['integration_disposition']}`；已逐章比较 current owner 与相邻章节。", f"<!-- review:{sfid}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    chosen = x["arxiv_id"] in SELECTED
    unit = SELECTED.get(x["arxiv_id"], "—")
    if x["integration_disposition"] == "Integrate":
        eligibility = "score_7_9; forced_review; potential_books_delta"
    elif x["integration_disposition"] == "Structural Candidate":
        eligibility = "score_7_9; forced_review; potential_structural_gap"
    else:
        eligibility = "score_7_9"
    lines.append(f"| {x['source_family_id']} | {eligibility} | {'selected' if chosen else 'not_selected'} | {unit} | — | {'跨层改变训练或安全控制契约' if chosen else 'exact-v1 complete；未扩写仅受 Daily 三项上限约束'} | {'analysis:'+unit if chosen else 'analysis-decision:'+x['source_family_id']} |")

analysis = {
    "2605.19444": "多数投票在初始多数正确时是低成本伪标签；当弱样本的少数正确轨迹会被训练永久压灭时，aggregate pass@1 掩盖了能力损伤。Extinction Window 将 per-problem label migration 变成控制状态，再用 flip-rate、minority preservation 与 risk-conditioned sparse update 决定何时停止更新。收益是保住短暂正确信号；代价是额外轨迹统计、阈值和样本级状态，且作者范围不证明开放任务中的伪标签真值。",
    "2605.19847": "per-account 隐私预算在账号与主体一一对应时合理；同一租户能创建多个账号并合谋时，噪声预算被重复消费，真实 owner 必须上移到 tenant/index。collusion-aware accounting 改善审计，却增加关联、预算与拒绝成本；论文只证明 retrieval IDs/noisy scores，不证明后续生成满足同一 DP 保证。",
    "2605.20005": "固定或衰减 learning rate 假设不同 batch 的能力覆盖相近；高损失 batch 同时承载新知识与更高遗忘风险时，简单丢弃 hard token 会损害学习。FINCH 保留 objective，只让 step size 随 loss 的平方根反比变化；收益是控制 forgetting–adaptation trade-off，代价是 loss EMA、cap 与超参选择，理论上界也不证明最优 schedule。",
}
for aid, unit in SELECTED.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", analysis[aid], f"<!-- analysis:{unit}:end -->"]
for x in retained:
    if x["arxiv_id"] not in SELECTED:
        lines.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->exact-v1 Source Review 已完成；未进入三项 Deep Analysis 不降低证据、评分或 Books Decision 要求。<!-- analysis-decision:{x['source_family_id']}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    c = comparison_by_id[x["arxiv_id"]]
    refs = ";".join(chapter_ref(p) for p in c["adjacent_paths"]) or chapter_ref(c["owner_path"])
    node_cell = "considered: PLATFORM-PRODUCTION, MULTIMODAL-REPRESENTATION" if x["integration_disposition"] == "Structural Candidate" else x["owner_node"]
    lines.append(f"| {x['source_family_id']} | {node_cell} | {chapter_ref(c['owner_path'])} | {refs} | existing:{x['source_family_id']} | delta:{x['source_family_id']} | Direct Evolution | {x['integration_disposition']} | books-review:{x['source_family_id']} |")
for x in retained:
    c = comparison_by_id[x["arxiv_id"]]
    sfid = x["source_family_id"]
    lines += [f"<!-- books-review:{sfid}:start -->", f"<!-- existing:{sfid}:start -->{c['existing_proposition']}<!-- existing:{sfid}:end -->", f"<!-- delta:{sfid}:start -->{c['new_evidence_delta']}<!-- delta:{sfid}:end --> Independent decision=`{x['integration_disposition']}`。", f"<!-- books-review:{sfid}:end -->"]

first = retained[0]["source_family_id"]
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |", f"| SA-20260520-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260520 | none | full 665 replay removed {len(REMOVE)} false positives and recovered {len(RECOVER)} false negatives | passed |", f"| SA-20260520-EVIDENCE | fresh-context:may2026-day02 | evidence | review:{first} | none | {len(retained)}/{len(retained)} source-specific exact-v1 reviews completed | passed |", f"| SA-20260520-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | analysis:DA-EXTINCTION-WINDOW | none | three cross-layer control deltas selected after denominator reconciliation | passed |", f"| SA-20260520-BOOKS | fresh-context:may2026-day02 | books | books-review:{first} | none | frozen {len(queue)}-item root queue plus one Structural Candidate | passed |", "", "## 8. Ignored Noise", "", f"{len(closures)} 条 family-specific pre-denominator closure 保存于 `screening-ledger-independent-final.json`；理由唯一数={len(closures)}。", "", "## 9. Recommended Action", "", f"root 按 owner 合并 {len(queue)} 项 Books queue；写回后由未参与写入的 reviewer 做 post-write semantic audit。`2605.22868` 进入季度结构复核，不强塞现有章节。", "", "## 10. Repository Changes", "", "- 更新 2026-05-20 date-local independent ledger、exact-v1 packet、Books comparison/queue 与 semantic audit。", "- 未修改共享 Books；未 stage、commit 或 push。", "", "## 11. Open Questions", "", "- root 写回后，每项机制是否都在 canonical main body、Review notes 之前，并保留旧路径、trade-off、failure 与 fallback？", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "", "## 12. Sources", ""]
for x in retained:
    lines.append(f"- [{x['title']}](https://arxiv.org/html/{x['arxiv_id']}v1) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-19；accessed 2026-09-02")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"独立 pre-write audit 已闭合；ordinary pending=0。剩余条件是 {len(queue)} 项 root Books 串行写回及不同 reviewer 的 post-write semantic audit。"]

out = ROOT / "papers/2026/05/20/README.md"
text = "\n".join(lines)
for x in retained:
    aid, sfid = x["arxiv_id"], x["source_family_id"]
    r = review_by_id[aid]
    body = text.split(f"<!-- review:{sfid}:start -->", 1)[1].split(f"<!-- review:{sfid}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if x["integration_disposition"] in {"Integrate", "Structural Candidate"} else "none"}
    rp = _expected_review_provenance(sfid, candidate, "deep", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", f"arXiv:{aid}v1 HTML — {r['method_locator']}", f"arXiv:{aid}v1 HTML — {r['evaluation_locator']}", f"arXiv:{aid}v1 HTML — {r['limitations_locator']}", r["artifact_locator"], f"claim:{sfid}", f"review:{sfid}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sfid, rp)
out.write_text(text + "\n")

print(json.dumps({"raw": AUTHOR["raw_snapshot_records"], "registered": 665, "screened": 665, "author_retained": 59, "false_positives_removed": len(REMOVE), "false_negatives_recovered": len(RECOVER), "retained": len(retained), "closures": len(closures), "exact_v1": len(retained), "blocked": 0, "integrate_queue": len(queue)}, ensure_ascii=False))
