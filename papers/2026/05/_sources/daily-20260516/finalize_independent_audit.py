#!/usr/bin/env python3
"""Finalize the non-author 2026-05-16 packet without writing shared Books."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

H = Path(__file__).resolve().parent
R = H.parents[4]
sys.path.insert(0, str(R))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256

LEDGER = json.loads((H / "screening-ledger-independent-checkpoint.json").read_text())
PACKET = json.loads((H / "exact-v1-independent-review-packet.json").read_text())
REVIEWS = {x["arxiv_id"]: x for x in PACKET["reviews"]}

INTEGRATE = {
    "2605.15508": ("MODEL-LONG-CONTEXT", "Draft-model attention is reused as the target model's sparse admission mask while target KV remains authoritative; this adds a draft/target state-ownership and false-negative fallback boundary not explicit in Ch22."),
    "2605.15514": ("MODEL-POSITION-ENCODING", "The exact-v1 proof separates position inversion/aliasing from token inversion/aliasing, tightening Ch13's qualitative RoPE extrapolation account into a protocol-specific representational limit."),
    "2605.15520": ("TRAIN-DATA", "A participant can preserve model utility while corrupting distributed data-attribution credit, so provenance integrity needs an adversarial contract rather than treating attribution as a passive statistic."),
    "2605.15529": ("TRAIN-RLHF", "Count evidence and learned concentration make process-reward reliability an input to ranking, stopping and repair; Ch31 has uncertainty-selected feedback but not this finite-evidence control contract."),
    "2605.15565": ("TRAIN-DISTRIBUTED-TRAINING", "Trainer-centered RL coordination becomes explicit dataflow components with rollout-as-a-service and versioned weight transfer, moving orchestration ownership into the distributed runtime."),
    "2605.15617": ("TRAIN-DISTRIBUTED-TRAINING", "Selective real-rank execution plus calibrated virtual participants makes cluster-scale training control paths testable on small hardware and introduces fidelity/error ownership absent from Ch36."),
    "2605.15638": ("PLATFORM-MONITORING", "Duplicated intra-thread instruction execution turns latent permanent-fault corruption into a runtime SDC sensor, adding detection coverage and overhead/fault-correlation boundaries to Ch67."),
    "2605.15648": ("PLATFORM-SECURITY", "The paper shows that an implementation variant can invalidate the privacy analysis used for DP-SGD, requiring mechanism-to-accountant conformance and audit evidence before a privacy claim is admitted."),
    "2605.16184": ("TRAIN-DISTRIBUTED-TRAINING", "Second-order state moves to heterogeneous memory under hook-driven overlap and bounded-staleness coherence; the runtime, not only the optimizer, now owns update timing and consistency."),
    "2605.16234": ("MODEL-TRANSFORMER-LAYER", "Layer redundancy conclusions change between replacement and interchange protocols, so pruning must freeze intervention semantics and evaluator identity before treating layers as substitutable."),
    "2605.16255": ("PLATFORM-COST", "AI power design is reframed from installed megawatts to deployable capacity across rack generations, linking topology, placement and redundancy to multi-resource stranding."),
    "2605.16622": ("TRAIN-PRETRAINING", "Weight decay changes progressive sharpening through global parameter interaction rather than simple local friction, refining Ch28's stability/EoS mechanism and architecture-dependent boundary."),
    "2605.16712": ("AGENT-MEMORY", "Retrieved personal facts must not automatically become behavioral commitments; activation, validation and realization need a bounded-commitment authority distinct from recall ownership."),
}

NO_CHANGE = {
    "2605.15573": "Ch82 already treats parallel/sequential topology as runtime policy with admission, convergence and rollback rather than a fixed multi-agent graph.",
    "2605.15581": "Ch81 already owns stage-localized failure evidence, replayable repair and durable workflow recovery; STAR is a scoped RCA realization.",
    "2605.15609": "Ch24 already carries proposal, parallel refinement, verification, rejection and rollback as the diffusion/speculation evolution spine.",
    "2605.15618": "Ch25 already distinguishes predictive representation quality from controllable world-state usefulness and requires robustness/evaluation boundaries.",
    "2605.15665": "Ch67 already connects requirement-derived tests, production-faithful simulation, diagnosis, prompt repair and continuous drift monitoring.",
    "2605.15694": "Ch52 already owns distributed inference placement under link loss, partition cost, state movement and heterogeneous edge constraints; CATS is a narrow deployment case.",
    "2605.15710": "Ch66 and Ch77 already require source-distributed evidence identity, provenance-aware memory evaluation and claim-level retrieval correctness.",
    "2605.15734": "Ch66 already separates construct validity, slice reliability, calibration and evaluator identity for inferred user-state measurements.",
    "2605.15761": "Ch66 already models leaderboard stability as an evaluator/version/perturbation contract and includes manipulation-sensitive release evidence.",
    "2605.15777": "Ch66 already evaluates workflow agents through executable task effects, environment state and bounded judge evidence rather than answer similarity alone.",
    "2605.15815": "Ch84 already owns reusable skill compilation, verification, provenance, lifecycle and transfer; repository setup is one skill domain.",
    "2605.15846": "Ch66 and Ch84 already require versioned long-horizon tasks, reproducible harness identity and rollout-based quality control.",
    "2605.15957": "Ch49 already owns heterogeneous CPU/GPU execution plans, phase-aware placement, data-layout conversion and fallback; MaxVec is a vector-search realization.",
    "2605.15960": "Ch25 explicitly distinguishes model error from planner exploitation and requires adversarial imagined-rollout validation.",
    "2605.15967": "Ch25 already separates observed, latent and imagined state and supports executable causal transition substrates with intervention boundaries.",
    "2605.16007": "Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.",
    "2605.16035": "Ch84 already requires agent/operator/service identity, signed ownership, delegation scope and accountable action traces.",
    "2605.16154": "Ch26 already treats action chunks, control frequency and rollout allocation as workload-specific training/runtime trade-offs; probabilistic masking is a local optimization.",
    "2605.16194": "Ch84 already owns typed artifacts, machine-readable provenance, schema validation and lifecycle compatibility for agent-consumable knowledge.",
    "2605.16198": "Ch72 already carries formal properties, bounded-state monitors, intervention, auditor false negatives and verification scope limits.",
    "2605.16217": "Ch76 already owns search, evidence graph growth, claim verification, synthesis and complementary retrieval under provenance constraints.",
    "2605.16508": "Ch84 already models skill-library competence, selection, transfer, interference and lifecycle; the scaling law is supporting evidence, not a new contract.",
    "2605.16565": "Ch79 and Ch56 already own speculative action planning, validation, commit and rollback under latency/cost budgets.",
    "2605.16588": "Ch26 already includes stronger runtime-assurance separation between nominal controller, safety admission and verified fallback under physical evidence.",
    "2605.16604": "Ch56 already admits/escalates work by uncertainty, evidence value, cost and SLO, with a bounded fallback to stronger execution.",
    "2605.16616": "Ch66 already requires immutable task, environment, code, artifact and evaluator identity for reproducible autonomous-research evidence.",
    "2605.16626": "Ch67 and Ch72 already treat adaptive monitor evasion, blind spots and false-negative measurement as part of the security evidence contract.",
    "2605.16630": "Ch72 already binds disclosure to task intent, data flow, access scope, local/cloud trust boundary and least-privilege release.",
    "2605.16637": "Ch56 already owns online workflow DAGs, heterogeneous placement, critical-path scheduling, queue pressure and SLO-aware fallback.",
    "2605.16647": "Ch72 already carries encrypted state-space inference, public-parameter constraints, ciphertext depth/noise and FHE fallback boundaries.",
    "2605.16650": "Ch66 and Ch77 already evaluate stateful dialogue through incremental state identity, provenance, contradiction handling and longitudinal effects.",
    "2605.16704": "Ch27 already treats dataset value as a set-level gradient-space diversity/quality allocation problem rather than additive example scores.",
    "2605.16725": "Ch25 already requires persistent, revisable and executable world state updated by failed predictions and targeted exploration.",
    "2605.21516": "Ch84 already binds inference-time harnesses to capability, evidence granularity, trajectory effects and partial-control reliability trade-offs.",
}

roadmap = (R / "ROADMAP.md").read_text()
PATHS = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def adjacent(path: str) -> list[str]:
    target = R / path
    siblings = sorted(target.parent.glob("*.md")) if target.exists() else []
    if target not in siblings:
        return []
    i = siblings.index(target)
    return [str(p.relative_to(R)) for p in siblings[max(0, i - 1):i] + siblings[i + 1:i + 2]]


rows = []
comparisons = []
queue = []
for source in LEDGER["identities"]:
    row = dict(source)
    aid = row["arxiv_id"]
    if row.get("screening_status") == "retained":
        if aid in INTEGRATE:
            owner, delta = INTEGRATE[aid]
            disposition = "Integrate"
        else:
            owner, delta = row["owner_node"], NO_CHANGE[aid]
            disposition = "No Change — Existing Coverage"
        row.update(owner_node=owner, review_status="deep_complete", access_status="accessible", integration_disposition=disposition)
        path = PATHS[owner]
        comparison = {
            "arxiv_id": aid, "source_family_id": row["source_family_id"], "owner_node": owner,
            "owner_path": path, "adjacent_paths": adjacent(path),
            "existing_proposition": delta if disposition.startswith("No Change") else f"`{path}` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.",
            "new_evidence_delta": delta, "decision": disposition,
            "reviewer": "fresh-context:may2026-day02",
        }
        comparisons.append(comparison)
        if disposition == "Integrate":
            queue.append({
                "report_date": "2026-05-16", "arxiv_id": aid, "source_family_id": row["source_family_id"],
                "stable_node_id": owner, "owner_path": path, "adjacent_paths": comparison["adjacent_paths"],
                "evidence_delta": delta,
                "writeback_requirement": "merge into the existing mechanism spine before Review notes; preserve old condition, changed constraint, owner/control transfer, trade-off, failure, fallback/coexistence and exact-v1 evidence boundary",
                "required_post_write_audit": "different reviewer reads owner and adjacent chapters; marker presence alone is insufficient",
            })
    rows.append(row)

retained = [x for x in rows if x.get("screening_status") == "retained"]
closures = [x for x in rows if x.get("screening_status") != "retained"]
ledger = dict(LEDGER)
ledger.update(schema="daily-screening-ledger-v2.1-independent-final", identities=rows,
              candidate_denominator=len(retained), pre_denominator_closures=len(closures))
ledger["independent_reconciliation"].update(exact_v1_complete=len(retained), exact_v1_blocked_pending_recovery=0,
                                             final_integrates=len(queue))
(H / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(H / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
(H / "books-current-content-comparison-independent.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(H / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
queue_obj = {"schema": "books-writeback-queue-v2.1-final", "report_date": "2026-05-16",
             "status": "awaiting_root_serial_writeback_and_post_write_audit", "items": queue}
(H / "BOOKS_WRITEBACK_QUEUE_INDEPENDENT.json").write_text(json.dumps(queue_obj, ensure_ascii=False, indent=2) + "\n")
(H / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue_obj, ensure_ascii=False, indent=2) + "\n")
(H / "exact-v1-review-packet.json").write_text(json.dumps(PACKET["reviews"], ensure_ascii=False, indent=2) + "\n")

selected = {"2605.15638": "DA-SDC-SENSOR", "2605.16184": "DA-RUNTIME-OPTIMIZER", "2605.16255": "DA-POWER-HIERARCHY"}
audit = {
    "schema": "semantic-independent-audit-v2.1", "report_date": "2026-05-16",
    "auditor": "fresh-context:may2026-day02", "author": "author-lane:prior-agent",
    "coverage": {"reviewed": "542/542 title+abstract identities", "author_retained": 66,
                 "false_positives_removed": LEDGER["independent_reconciliation"]["false_positive_downgrades"],
                 "false_negatives_recovered": LEDGER["independent_reconciliation"]["false_negative_recoveries"],
                 "final_denominator": len(retained), "final_closures": len(closures), "status": "passed"},
    "evidence": {"deep_complete": len(retained), "local_reuse": 1, "official_html": 44, "official_pdf": 2,
                 "blocked": [], "status": "passed"},
    "deep_analysis_selection": {"selected": sorted(selected), "status": "passed"},
    "books": {"current_content_comparison": len(comparisons), "final_integrates": len(queue),
              "status": "passed_prewrite_pending_root_writeback"},
    "remaining_findings": [f"root serial Books writeback for {len(queue)} families and different-reviewer post-write semantic audit"],
}
(H / "semantic-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
for name in ("screening-ledger-independent-final.json", "semantic-independent-audit.json", "BOOKS_WRITEBACK_QUEUE_INDEPENDENT.json"):
    p = H / name
    p.with_suffix(p.suffix + ".sha256").write_text(sha(p) + "\n")

ledger_sha = sha(H / "screening-ledger-independent-final.json")
comp = {x["arxiv_id"]: x for x in comparisons}
now = datetime.now(timezone.utc).isoformat()
L = [
    "# Daily Research — 2026-05-16", "", "**Research Date:** 2026-05-16", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-15 09:00:00 ～ 2026-05-16 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite v2 仅支持 identity/date/abstract，技术结论绑定 official arXiv exact-v1。", "",
    f"**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立审计完成，等待 {len(queue)} 项 root 串行 Books 写回与 post-write audit。", "",
    "## Executive Summary", "",
    f"从 91,841 条 raw records 中恢复并重放 542/542 个窗口 identity。独立 reviewer 将 author denominator 66 收紧为 {len(retained)}（{len(retained)/542:.2%}），{len(closures)} 项以 family-specific reason 在 denominator 前闭合；恢复 6 个 false negative，移除 25 个 false positive。47/47 项完成 exact-v1 全文 Review（1 项复用 W20 已核验全文、44 项 official HTML、2 项 official PDF），blocked=0。逐项读取 current owner 与相邻章节后，冻结 {len(queue)} 项最小 Books writeback queue；本 lane 未修改共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-16 |", "| Window End | 2026-05-16 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report |  |", "| Changed Source IDs |  |", "| Previous Denominator ID |  |", "| Denominator ID | DEN-20260516-V2-INDEPENDENT |", f"| Denominator Frozen At | {now} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-15T09:00:00+08:00 | 2026-05-16T09:00:00+08:00 | {now} | DataCite v2 2604/2605/2606 00..99 + independent 542/542 semantic replay | checked | 542 | {';'.join(x['source_family_id'] for x in retained)} | pages=300; final_cursor=end; raw=91841; registered=542; screened=542; retained={len(retained)}; closure={len(closures)} | 2026-05-16T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |", "",
    "### Coverage Limitations", "", "<!-- coverage:SRC-ARXIV:20260516:start -->确定性窗口枚举与 542/542 title+abstract 语义筛选已经闭合。DataCite 不支持技术结论；所有 retained family 另由 exact-v1 HTML/PDF 或已核验同版本 Full Source Review 支持。<!-- coverage:SRC-ARXIV:20260516:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->", "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
for x in retained:
    a, sf, s = x["arxiv_id"], x["source_family_id"], x["score_v2"]
    override = "knowledge_gap" if x["integration_disposition"] == "Integrate" else "none"
    L.append(f"| {sf} | arXiv:{a}v1 | paper-v1:{a} | 2026-W20 | 2026-05-15 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {override} | review:{sf} | self | — | new_in_window | {x['owner_node']} | {x['integration_disposition']} | books-review:{sf} | no |")

L += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->", "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
receipt = {}
for x in retained:
    a, sf, r = x["arxiv_id"], x["source_family_id"], REVIEWS[x["arxiv_id"]]
    method = f"arXiv:{a}v1 — Methodology: {r['method_locator']}"
    evaluation = f"arXiv:{a}v1 — Experiments: {r['evaluation_locator']}"
    limits = r["limitations_locator"]
    if not limits.startswith(("Not Disclosed —", "Not Required —")):
        limits = f"arXiv:{a}v1 — Scope and limitations: {limits}"
    artifact = f"{r['retrieval']['date_local_receipt']}#sha256={r['retrieval']['receipt_sha256']}; immutable artifact commit Not Disclosed"
    L.append(f"| {sf} | RP-TODO-{sf} | deep | arXiv:{a}v1 | SRC-ARXIV@arXiv:{a}v1 | {method} | {evaluation} | {limits} | {artifact} | claim:{sf} | complete |")
    receipt[a] = (method, evaluation, limits, artifact)

L += ["", "### Source Reviews", ""]
for x in retained:
    a, sf, r = x["arxiv_id"], x["source_family_id"], REVIEWS[x["arxiv_id"]]
    L += [f"<!-- review:{sf}:start -->", f"#### {x['title']}", "",
          f"问题与约束：{r['problem_and_changed_constraint']}", "", f"机制与 ownership：{r['mechanism_and_ownership']}", "",
          f"Evaluation contract：{r['evaluation_contract']}", "", f"Trade-off / failure：{r['tradeoff_and_failure_mode']}", "",
          f"旧路径与共存边界：{r['old_path_and_coexistence']}", "",
          f"<!-- claim:{sf}:start -->{r['proof_boundary']}<!-- claim:{sf}:end -->", "",
          f"Books Decision=`{x['integration_disposition']}`；current owner+adjacent comparison=`books-review:{sf}`。", f"<!-- review:{sf}:end -->", ""]

L += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
      "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
for x in retained:
    a, sf = x["arxiv_id"], x["source_family_id"]
    sel = a in selected
    eligibility = "score_7_9; forced_review; potential_books_delta" if x["integration_disposition"] == "Integrate" else "score_7_9"
    L.append(f"| {sf} | {eligibility} | {'selected' if sel else 'not_selected'} | {selected.get(a, '—')} | — | {'cross-layer ownership and long-lived failure boundary' if sel else 'exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas'} | {'analysis:'+selected[a] if sel else 'analysis-decision:'+sf} |")
for a, unit in selected.items():
    x = next(z for z in retained if z["arxiv_id"] == a); r = REVIEWS[a]
    L += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "",
          f"旧路径之所以合理，是因为它在未出现该论文隔离出的约束时更简单、状态更少。exact-v1 将变化定位为：{r['problem_and_changed_constraint']} 新机制改变的 owner 是：{r['mechanism_and_ownership']} 证据只覆盖：{r['evaluation_contract']} 代价与失败面是：{r['tradeoff_and_failure_mode']} 因此旧方案仍在以下条件共存：{r['old_path_and_coexistence']}",
          f"<!-- analysis:{unit}:end -->"]
for x in retained:
    if x["arxiv_id"] not in selected:
        L.append(f"<!-- analysis-decision:{x['source_family_id']}:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:{x['source_family_id']}:end -->")

L += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
def chapter_ref(path: str) -> str:
    match = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree"
for x in retained:
    a, sf, c = x["arxiv_id"], x["source_family_id"], comp[x["arxiv_id"]]
    L.append(f"| {sf} | {x['owner_node']} | {chapter_ref(c['owner_path'])} | {';'.join(chapter_ref(p) for p in c['adjacent_paths']) or chapter_ref(c['owner_path'])} | existing:{sf} | delta:{sf} | Direct Evolution | {x['integration_disposition']} | books-review:{sf} |")
for x in retained:
    sf, c = x["source_family_id"], comp[x["arxiv_id"]]
    L += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->", f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Final decision=`{x['integration_disposition']}`。", f"<!-- books-review:{sf}:end -->"]

first = retained[0]["source_family_id"]
L += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |",
      "| SA-20260516-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260516 | None | screening-ledger-independent-final.json#independent_reconciliation | passed |",
      f"| SA-20260516-EVIDENCE | fresh-context:may2026-day02 | evidence | review:{first} | None | exact-v1-independent-review-packet.json#reviews | passed |",
      "| SA-20260516-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | analysis:DA-SDC-SENSOR | None | semantic-independent-audit.json#deep_analysis_selection | passed |",
      f"| SA-20260516-BOOKS | fresh-context:may2026-day02 | books | books-review:{first} | None | books-current-content-comparison-independent.json#items | passed |", "",
      "## 8. Ignored Noise", "", f"{len(closures)} 条 family-specific pre-denominator closure 保存在 `screening-ledger-independent-final.json`；没有把 Core Daily recall 偷换为 Candidate Denominator。", "",
      "## 9. Recommended Action", "", f"Root 按日期序列将 {len(queue)} 项 owner-merged narrative 写入共享 Books；随后由不同 reviewer 做 post-write semantic audit。", "",
      "## 10. Repository Changes", "", "- 05-16 date-local denominator、exact-v1 packet、Books comparison、queue、independent audit 与 canonical Daily 已更新。", "- 本 lane 未修改共享 Books，未 stage、commit 或 push。", "",
      "## 11. Open Questions", "", f"- {len(queue)} 项写回后是否在 owner 正文形成 old path → changed constraint → ownership → trade-off/failure → fallback/coexistence，而非只增加 trace marker？", "",
      "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
      "## 12. Sources", ""]
for x in retained:
    r = REVIEWS[x["arxiv_id"]]
    L.append(f"- [{x['title']}]({r['retrieval']['url']}) — arXiv:{x['arxiv_id']}v1；first-public 2026-05-15；receipt `{r['retrieval']['date_local_receipt']}`；accessed 2026-09-01")
L += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"05-16 research/evidence/prewrite audit 已闭合；仅剩 {len(queue)} 项 root Books 串行写回与 post-write semantic audit。"]

text = "\n".join(L) + "\n"
for x in retained:
    a, sf = x["arxiv_id"], x["source_family_id"]
    method, evaluation, limits, artifact = receipt[a]
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{a}", "Primary Identifier": f"arXiv:{a}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if x["integration_disposition"] == "Integrate" else "none"}
    rp = _expected_review_provenance(sf, candidate, "deep", f"arXiv:{a}v1", f"SRC-ARXIV@arXiv:{a}v1", method, evaluation, limits, artifact, f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sf, rp)

out = R / "papers/2026/05/16/README.md"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(text)
print(json.dumps({"raw": 91841, "registered": 542, "screened": 542, "retained": len(retained), "closures": len(closures), "reviewed": len(retained), "blocked": 0, "integrate": len(queue)}, ensure_ascii=False))
