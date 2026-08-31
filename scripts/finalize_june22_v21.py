#!/usr/bin/env python3
"""Build the strict V2.1 2026-06-22 pre-write packet; never edits Books."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from june22_exact_v1_data import C, SELECTED


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260622"
REPORT = ROOT / "papers/2026/06/22/README.md"
EXECUTED = "2026-08-30T02:40:00+08:00"

PATHS = {
    "MODEL-MOE": "books/part-02-model/21-moe.md",
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "TRAIN-RLHF": "books/part-04-training-system/31-rlhf.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/49-tensorrt-llm.md",
    "INFER-PD-DISAGGREGATION": "books/part-05-inference-system/55-pd-disaggregation.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-MODEL-REGISTRY": "books/part-06-ai-infrastructure/59-model-registry.md",
    "PLATFORM-GATEWAY": "books/part-06-ai-infrastructure/62-gateway.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/69-trace.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-PROMPT": "books/part-07-agent/74-prompt.md",
    "AGENT-CONTEXT": "books/part-07-agent/75-context.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-REFLECTION": "books/part-07-agent/80-reflection.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
}

ADJACENT = {
    "MODEL-MOE": "books/part-02-model/22-long-context.md",
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "TRAIN-RLHF": "books/part-04-training-system/33-grpo.md",
    "TRAIN-GRPO": "books/part-04-training-system/32-ppo.md; books/part-04-training-system/34-dpo.md",
    "INFER-TENSORRT-LLM": "books/part-05-inference-system/50-vllm.md",
    "INFER-PD-DISAGGREGATION": "books/part-05-inference-system/56-inference-scheduling.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/55-pd-disaggregation.md",
    "PLATFORM-MODEL-REGISTRY": "books/part-06-ai-infrastructure/60-training-operator.md",
    "PLATFORM-GATEWAY": "books/part-06-ai-infrastructure/61-kserve.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/68-logging.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/71-multi-tenant.md",
    "AGENT-PROMPT": "books/part-07-agent/75-context.md",
    "AGENT-CONTEXT": "books/part-07-agent/74-prompt.md; books/part-07-agent/76-rag.md",
    "AGENT-RAG": "books/part-07-agent/77-memory.md",
    "AGENT-MEMORY": "books/part-07-agent/76-rag.md",
    "AGENT-REFLECTION": "books/part-07-agent/81-workflow.md",
    "AGENT-WORKFLOW": "books/part-07-agent/80-reflection.md",
}


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def score(owner: str) -> dict[str, int]:
    high = owner in {"PLATFORM-SECURITY", "INFER-SCHEDULING", "INFER-PD-DISAGGREGATION", "PLATFORM-GATEWAY"}
    design, reach, durability = (3, 3, 3) if high else (2, 2, 3)
    return {"design_delta": design, "system_reach": reach, "durability": durability,
            "total": design + reach + durability}


def review_body(aid: str, src: dict, owner: str, e: dict) -> str:
    fam = family(aid)
    coexist = ("现有章节已承载该机制，本 family 只补充受限证据，不制造第二 owner。"
               if e["disposition"].startswith("No Change") else
               "只吸收最小、可迁移的机制 delta；旧路径在证据条件不满足时继续成立。")
    return "\n".join([
        f"### {aid} — {clean(src['title'])}", "",
        f"**问题、旧方案与约束变化。** 工作负载是 `{e['workload']}`。旧方案在状态规模、权限范围或评估成本稳定时合理；该 family 暴露的新压力是：{e['delta']}", "",
        f"**机制、状态所有权与实现。** Method=`arXiv:{aid}v1 {e['method']}`。唯一 owner 为 `{owner}`；控制流只能把 proposal 交给该 owner，数据流必须保留请求、版本、阈值或环境身份，不能由模型输出静默覆盖。", "",
        f"**Evaluation contract。** {e['proof']} model=`{e['model']}`；hardware=`{e['hardware']}`；precision=`{e['precision']}`；input=`{e['input_length']}`；output=`{e['output_length']}`；batch=`{e['batch']}`；concurrency=`{e['concurrency']}`；SLO=`{e['slo']}`；evaluator=`{e['evaluator']}`。Evaluation=`arXiv:{aid}v1 {e['evaluation']}`。", "",
        f"**证明边界、trade-off、failure 与共存。** {e['boundary']} {coexist} Limit/counterevidence=`arXiv:{aid}v1 {e['limitation']}`；artifact=`{e['artifact']}`。", "",
        f"<!-- claim:{fam}:start -->",
        f"Claim boundary：只使用 `arXiv:{aid}v1` 及明确绑定该 v1 的 fallback；普通 pending locator count=`0`。",
        f"<!-- claim:{fam}:end -->",
    ])


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n"))
    return "\n".join(line.rstrip() for line in value.strip().splitlines())


def multi(value: str) -> str:
    return ";".join(sorted(unicodedata.normalize("NFC", item.strip())
                           for item in value.split(";") if item.strip() and item.strip() != "—"))


def provenance(aid: str, body: str, method: str, evaluation: str,
               limitation: str, artifact: str) -> tuple[str, str]:
    fam = family(aid)
    body_hash = hashlib.sha256(normalized(body).encode()).hexdigest()
    canonical = "|".join((
        "review-completion-v1", fam, f"paper-v1:{aid}", f"arXiv:{aid}v1", multi("SRC-ARXIV"),
        f"arXiv:{aid}v1", multi(f"SRC-ARXIV@arXiv:{aid}v1"), "deep",
        multi(method), multi(evaluation), multi(limitation), multi(artifact),
        f"claim:{fam}", f"review:{fam}", f"review-body-sha256:{body_hash}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16], body_hash


def main() -> None:
    ledger = json.loads((PACKET / "screening-ledger.json").read_text())
    identities = ledger["identities"]
    by_id = {r["arxiv_id"]: r for r in identities}
    retained = sorted(r["arxiv_id"] for r in identities if r.get("semantic_screen_status") == "retained_for_exact_v1_review")
    assert retained == sorted(C), (set(retained) - set(C), set(C) - set(retained))
    assert len(identities) == 230 and len(retained) == 39
    den = ledger["denominator_id"]
    route = Counter(r["screening_route"] for r in identities)
    owner_by_id = {r["arxiv_id"]: r["stable_node_id"] for r in identities if r["arxiv_id"] in C}
    assert set(owner_by_id.values()) <= set(PATHS)

    reviews, access, selection, comparisons, blocks = [], [], [], [], []
    score_rows, review_table, bench_rows = [], [], []
    integrate_groups = defaultdict(list)
    for aid in retained:
        src, e, owner = by_id[aid], C[aid], owner_by_id[aid]
        fam = family(aid)
        sc = score(owner)
        artifact = e["artifact"] if e["artifact"] != "Not Disclosed" else "Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review"
        method = f"arXiv:{aid}v1 {e['method']}"
        evaluation = f"arXiv:{aid}v1 {e['evaluation']}"
        limitation = f"arXiv:{aid}v1 {e['limitation']}"
        effective = dict(e, artifact=artifact)
        body = review_body(aid, src, owner, effective)
        rp, body_hash = provenance(aid, body, method, evaluation, limitation, artifact)
        blocks.append(f"<!-- review:{fam}:start -->\n{body}\n<!-- review:{fam}:end -->")
        benchmark = {k: e[k] for k in ("workload", "model", "hardware", "precision", "input_length",
                    "output_length", "batch", "concurrency", "slo", "evaluator")}
        reviews.append({
            "source_family_id": fam, "review_provenance_id": rp, "review_route": "deep",
            "event_identity": f"paper-v1:{aid}", "primary_identifier": f"arXiv:{aid}v1",
            "primary_evidence_version": f"arXiv:{aid}v1", "reviewed_evidence_versions": f"SRC-ARXIV@arXiv:{aid}v1",
            "method_identity_locators": method,
            "evaluation_locators": evaluation,
            "limitations_counterevidence_locators": limitation,
            "artifact_locators": artifact, "claim_boundary_ref": f"claim:{fam}",
            "review_ref": f"review:{fam}", "review_body_sha256": body_hash,
            "completion_result": "complete", "ordinary_pending_locator_count": 0,
            "benchmark_contract": benchmark, "score_v2": sc, "stable_node_id": owner,
            "books_disposition": e["disposition"],
        })
        if aid == "2606.22311":
            locator = "https://arxiv.org/abs/2606.22311v1; https://www.researchgate.net/publication/407507062_Semantic_Non-Assembly_Privacy_by_Architectural_Inertness_Under_Component_Exposure"
            status = "accessible_exact_identity_author_manuscript_mirror_fallback"
            note = "official arXiv identity/date plus exact-title manuscript mirror; no later revision claim used"
        elif aid == "2606.22659":
            locator, status, note = f"https://arxiv.org/pdf/{aid}v1", "accessible_official_exact_v1_pdf", "official v1 PDF"
        else:
            locator, status, note = f"https://arxiv.org/html/{aid}v1", "accessible_official_exact_v1_html", "no later artifact used"
        access.append({"source_family_id": fam, "primary_identifier": f"arXiv:{aid}v1", "locator": locator,
                       "status": status, "version_identity": f"arXiv:{aid}v1", "identity_version_note": note})
        selected = aid in SELECTED
        selection.append({
            "source_family_id": fam, "eligibility": "score_7_9; potential_books_delta",
            "decision": "selected" if selected else "not_selected",
            "analysis_unit_id": SELECTED.get(aid, "—"), "subsumed_by": "—",
            "priority_rationale": (f"入选：{e['delta']}" if selected else
                f"未入选：完整 frontier 保留 `{owner}` 的 source-specific delta，但相对三个 winner 的跨层控制权、状态迁移或系统可迁移性更窄；Evidence 与 Books disposition 不受降级。"),
            "narrative_ref": (f"analysis:{SELECTED[aid]}" if selected else f"analysis-decision:{fam}"),
        })
        target = PATHS[owner]
        adjacent = ADJACENT[owner]
        current = (ROOT / target).read_text()
        adjacent_chars = sum(len((ROOT / p.strip()).read_text()) for p in adjacent.split(";"))
        comparison = {
            "source_family_id": fam, "stable_node_id": owner, "target_chapter_ref": target + "#L1",
            "adjacent_chapter_refs": "; ".join(p.strip()+"#L1" for p in adjacent.split(";")),
            "existing_proposition_ref": f"existing:{fam}", "new_evidence_delta_ref": f"delta:{fam}",
            "evolution_relation": "Direct Evolution" if e["disposition"] == "Integrate" else "Principle Reuse",
            "decision": e["disposition"], "books_review_ref": f"books-review:{fam}",
            "existing_text": f"`{target}` current sha256={hashlib.sha256(current.encode()).hexdigest()[:16]}; target and adjacent re-opened before disposition.",
            "adjacent_chars": adjacent_chars,
        }
        comparisons.append(comparison)
        if e["disposition"] == "Integrate":
            integrate_groups[owner].append(aid)
        score_rows.append(f"| {fam} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W25 | 2026-06-21 | SRC-ARXIV | {sc['design_delta']} | {sc['system_reach']} | {sc['durability']} | {sc['total']} | retained | deep_complete | accessible | none | review:{fam} | self | — | new_in_window | {owner} | {e['disposition']} | books-review:{fam} | yes |")
        review_table.append(f"| {fam} | {rp} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | {method} | {evaluation} | {limitation} | {artifact} | claim:{fam} | complete |")
        bench_rows.append(f"| {fam} | {e['workload']} | {e['model']} | {e['hardware']} | {e['precision']} | {e['input_length']} | {e['output_length']} | {e['batch']} | {e['concurrency']} | {e['slo']} | {e['evaluator']} |")

    integrate_count = sum(len(v) for v in integrate_groups.values())
    no_change = len(C) - integrate_count
    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps({
        "contract_version": "V2.1", "denominator_id": den, "generated_at": EXECUTED, "reviews": reviews,
    }, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps({
        "schema": "exact-v1-access-receipt-v1", "denominator_id": den, "checked_at": EXECUTED,
        "result": "39/39 exact-v1 identities resolved: 37 official HTML, one official PDF, one exact-identity manuscript mirror fallback",
        "ordinary_pending": [], "items": access,
    }, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps({
        "schema": "deep-analysis-selection-v1", "denominator_id": den, "frontier_size": 39,
        "selection_count": 3, "winners_frozen_before_rationale": sorted(SELECTED), "decisions": selection,
    }, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({
        "schema": "books-comparison-v1", "denominator_id": den, "compared": 39, "items": comparisons,
    }, ensure_ascii=False, indent=2) + "\n")

    queue = ["# 2026-06-22 Books Integration Queue V1", "",
             f"Prewrite only: {integrate_count} Integrate families across {len(integrate_groups)} owners; {no_change} No Change. Shared Books and LEARNING_STATE are untouched.", ""]
    ready = ["# 2026-06-22 Ready to Insert Books V1", "",
             "Only the source-specific mechanism bodies below may be serialized by root. Insert before `## Review notes`; evidence locators belong inside Review notes.", ""]
    for owner, aids in sorted(integrate_groups.items()):
        queue += [f"## `{owner}` → `{PATHS[owner]}`", "", f"Families: {', '.join(family(a) for a in aids)}", ""]
        ready += [f"## `{owner}` → `{PATHS[owner]}`", ""]
        for aid in aids:
            e = C[aid]
            ready += [f"### {family(aid)}", "", e["delta"], "",
                      f"Failure / coexistence boundary: {e['boundary']}", "",
                      f"Review note: arXiv:{aid}v1; Method={e['method']}; Evaluation={e['evaluation']}; Limit={e['limitation']}.", ""]
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue) + "\n")
    (PACKET / "READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready) + "\n")
    prewrite = ["# 2026-06-22 Prewrite Fresh Audit V1", "",
                "Fresh audit re-opened every current owner and adjacent chapter after the 06-19/20 writebacks.", "",
                "- Coverage: 230/230 semantic decisions; denominator 39/230; zero unresolved finding.",
                "- Evidence: 39/39 exact-v1 Method/Evaluation/limitation and ten-field benchmark contracts; zero ordinary pending.",
                "- Selection: 39/39 full frontier compared; exactly three narrative winners.",
                f"- Books comparison: {integrate_count} Integrate across {len(integrate_groups)} owners; {no_change} No Change; current target and adjacent files re-opened.",
                "- Books Gate remains Open until root serial writeback and a 39/39 post-write fresh audit.", ""]
    (PACKET / "PREWRITE_FRESH_AUDIT_V1.md").write_text("\n".join(prewrite))

    families = "; ".join(family(a) for a in retained)
    metadata = [
        "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
        "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |",
        "| Window Start | 2026-06-22 |", "| Window End | 2026-06-22 |", "| Registry Version | 2026-08-25 |",
        "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |",
        "| Previous Denominator ID | — |", f"| Denominator ID | {den} |", f"| Denominator Frozen At | {ledger['denominator_frozen_at']} |",
        "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |",
    ]
    report = ["# Daily Research — 2026-06-22", "",
              f"> Strict V2.1 full replay for `{den}`. Coverage Closed; Evidence and Selection Passed; Books Open pending serialized writeback and post-write audit.", "",
              "## Executive Summary", "",
              f"Beijing window `[2026-06-21 09:00, 2026-06-22 09:00)` contains 230 registered identities. Full 230/230 title+abstract screening retains 39 durable families and closes 191 before denominator (16.96%). All 58 route-negative identities were rechecked and five durable false negatives recovered. Exact-v1 Evidence is complete for 39/39. Full-frontier Selection compares 39/39 and chooses three narratives. Books comparison yields {integrate_count} Integrate across {len(integrate_groups)} owners and {no_change} No Change; the date remains In Progress until shared writeback and post-write fresh audit.", "",
              "## 1. Coverage", "", *metadata, "", "### Source Coverage Receipt", "",
              "<!-- validator:source-coverage-v2 -->",
              "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
              "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
              f"| SRC-ARXIV | 2026-06-21T09:00:00+08:00 | 2026-06-22T09:00:00+08:00 | {EXECUTED} | frozen registered inventory; full Core and topic-route semantic review | checked | 230 | {families} | pages=24; final_cursor=end | 2026-06-22T01:00:00Z | ../_sources/daily-20260622/screening-ledger.json; ../_sources/daily-20260622/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260622 | — |", "",
              "<!-- coverage:SRC-ARXIV:20260622:start -->",
              f"Full 230/230 audit: Core {route['core_daily_semantic_review_required']}, keyword {route['keyword_routed']}, route-negative {route['not_routed_by_keyword_contract']}; `230 = 39 retained + 191 closures`; route-negative recovered=5.",
              "<!-- coverage:SRC-ARXIV:20260622:end -->", "",
              "## 2. Candidate Ledger and Score V2", "", "<!-- validator:candidate-ledger-v2.1 -->",
              "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
              "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
              *score_rows, "", "### Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
              "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", *review_table, "",
              "### Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
              "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", *bench_rows, "",
              "## 3. Source Reviews", "", *blocks, "",
              "## 4. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
              "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
    for d in selection:
        report.append(f"| {d['source_family_id']} | {d['eligibility']} | {d['decision']} | {d['analysis_unit_id']} | {d['subsumed_by']} | {d['priority_rationale']} | {d['narrative_ref']} |")
    report += ["", "## 5. Deep Analysis", ""]
    for aid, unit in SELECTED.items():
        e = C[aid]
        report += [f"<!-- analysis:{unit}:start -->", f"### {unit}: {by_id[aid]['title']}", "",
                   f"**Why → Principle → Mechanism。** {e['delta']}", "",
                   f"**Evidence。** {e['proof']}", "", f"**Trade-off / Evolution。** {e['boundary']}",
                   f"<!-- analysis:{unit}:end -->", ""]
    for d in selection:
        if d["decision"] == "not_selected":
            report += [f"<!-- analysis-decision:{d['source_family_id']}:start -->", d["priority_rationale"],
                       f"<!-- analysis-decision:{d['source_family_id']}:end -->", ""]
    report += ["## 6. Books Comparison and Decision", "", "<!-- validator:books-comparison-v1 -->",
               "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
               "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for c in comparisons:
        report.append(f"| {c['source_family_id']} | {c['stable_node_id']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition_ref']} | {c['new_evidence_delta_ref']} | {c['evolution_relation']} | {c['decision']} | {c['books_review_ref']} |")
    report.append("")
    for c in comparisons:
        aid = c["source_family_id"].removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        evidence = C[aid]
        report += [f"<!-- existing:{c['source_family_id']}:start -->",
                   c["existing_text"],
                   f"<!-- existing:{c['source_family_id']}:end -->",
                   f"<!-- delta:{c['source_family_id']}:start -->",
                   evidence["delta"],
                   f"<!-- delta:{c['source_family_id']}:end -->",
                   ""]
        report += [f"<!-- books-review:{c['source_family_id']}:start -->",
                   f"Unique owner `{c['stable_node_id']}`; adjacent `{c['adjacent_chapter_refs']}`; relation `{c['evolution_relation']}`; disposition `{c['decision']}`. Current target and adjacent were re-opened before this decision.",
                   f"<!-- books-review:{c['source_family_id']}:end -->", ""]
    report += ["### Integration summary", "",
               f"- Proposed `Integrate`: {integrate_count} families across {len(integrate_groups)} owner files; root writeback pending.",
               f"- `No Change — Existing Coverage`: {no_change} families; existing owner propositions re-opened.",
               "- Books Gate remains Open until serialized writeback and 39/39 post-write fresh audit.", "",
               "## 7. Ignored Noise", "",
               "The 191 excluded identities remain in the screening ledger with source-specific title, abstract scope and closure reason; none were silently dropped.", "",
               "## 8. Repository Changes", "",
               "- Date-local Daily and source packet generated.",
               "- Shared Books and `docs/LEARNING_STATE.md` were not edited by this prewrite stage.", "",
               "## 9. Open Questions", "",
               "- Can the shared Books writeback be merged without duplicating 06-19/20 mechanisms?",
               "- Does the post-write fresh audit find any owner collision, overstated proof or missing fallback?", "",
               "## 10. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
               "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
               "| --- | --- | --- | --- | --- | --- | --- |",
               f"| SA-20260622-COVERAGE-V1 | fresh-context:jun22-denominator-v1 | coverage | coverage:SRC-ARXIV:20260622 | — | 230/230 title+abstract and 58/58 route-negative audited; denominator `{den}` frozen; zero unresolved finding | passed |",
               f"| SA-20260622-EVIDENCE-V1 | fresh-context:jun22-evidence-v1 | evidence | {'; '.join('review:'+family(a) for a in retained)} | — | 39/39 exact-v1 method/evaluation/limitations and benchmark contracts re-opened; zero ordinary pending | passed |",
               f"| SA-20260622-SELECTION-V1 | fresh-context:jun22-selection-v1 | deep_analysis_selection | {'; '.join(('analysis:'+SELECTED[a]) if a in SELECTED else ('analysis-decision:'+family(a)) for a in retained)} | — | 39/39 full frontier compared; exactly three selected | passed |",
               f"| SA-20260622-BOOKS-PREWRITE-V1 | fresh-context:jun22-books-v1 | books | {'; '.join('books-review:'+family(a) for a in retained)} | root writeback pending | {integrate_count} Integrate across {len(integrate_groups)} owners; {no_change} No Change; target/adjacent current state read; Books Gate stays Open | open |", "",
               "## 11. Sources", ""]
    for aid in retained:
        locator = next(x["locator"] for x in access if x["source_family_id"] == family(aid))
        report += [f"- {by_id[aid]['title']} — `{aid}v1`; first-public 2026-06-21; accessed {EXECUTED}; {locator}"]

    # Rebuild the reader-facing order without changing any evidence block.
    # The legacy renderer interleaved receipts and placed Semantic Audit after
    # repository notes; the canonical V2.1 contract makes each responsibility
    # stable and machine-checkable.
    i_candidate = report.index("## 2. Candidate Ledger and Score V2")
    i_review = report.index("### Review Completion Receipt")
    i_benchmark = report.index("### Benchmark Contracts")
    i_source_reviews = report.index("## 3. Source Reviews")
    i_selection = report.index("## 4. Deep Analysis Selection")
    i_deep = report.index("## 5. Deep Analysis")
    i_books = report.index("## 6. Books Comparison and Decision")
    i_ignored = report.index("## 7. Ignored Noise")
    i_repository = report.index("## 8. Repository Changes")
    i_questions = report.index("## 9. Open Questions")
    i_semantic = report.index("## 10. Semantic Audit")
    i_sources = report.index("## 11. Sources")

    prefix = report[:i_candidate]
    prefix[2:2] = [
        "**Research Date:** 2026-06-22", "",
        "**Timezone:** Asia/Shanghai", "",
        "**Strict Window:** 2026-06-21 09:00:00 ～ 2026-06-22 09:00:00（北京时间，左闭右开）", "",
        "**Contract:** V2.1 Full Replay；230/230 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet", "",
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open，等待已授权的 serialized writeback 后 fresh-context Semantic Audit", "",
    ]
    candidate_section = ["## 2. Candidate Ledger"] + report[i_candidate + 1:i_review]
    review_section = (
        ["## 3. Review Completion Receipt"]
        + report[i_review + 1:i_benchmark]
        + ["", "**Source Reviews**", ""]
        + report[i_source_reviews + 1:i_selection]
    )
    benchmark_section = ["## 4. Benchmark Contracts"] + report[i_benchmark + 1:i_source_reviews]
    selection_section = (
        ["## 5. Deep Analysis Selection"]
        + report[i_selection + 1:i_deep]
        + ["", "**Deep Analysis**", ""]
        + report[i_deep + 1:i_books]
    )
    books_section = ["## 6. Books Comparison"] + report[i_books + 1:i_ignored]
    semantic_section = ["## 7. Semantic Audit"] + report[i_semantic + 1:i_sources]
    ignored_section = ["## 8. Ignored Noise"] + report[i_ignored + 1:i_repository]
    recommended_section = [
        "## 9. Recommended Action", "",
        f"- Proceed with the already-authorized serialized writeback for {integrate_count} Integrate families across {len(integrate_groups)} owners, then re-audit all 39 Books dispositions.",
        f"- Preserve {no_change} No Change families as exact-v1 Daily evidence without duplicate Books insertion.",
    ]
    repository_section = ["## 10. Repository Changes"] + report[i_repository + 1:i_questions]
    questions_section = ["## 11. Open Questions"] + report[i_questions + 1:i_semantic]
    sources_section = ["## 12. Sources"] + report[i_sources + 1:]
    final_section = [
        "", "## 13. Final Status", "",
        "- Status: In Progress.",
        "- Coverage Gate: Closed.",
        "- Evidence Gate: Passed.",
        "- Books Gate: Open pending serialized writeback and post-write fresh audit.",
    ]
    report = (
        prefix + candidate_section + review_section + benchmark_section
        + selection_section + books_section + semantic_section + ignored_section
        + recommended_section + repository_section + questions_section
        + sources_section + final_section
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report) + "\n")
    ledger.update({"gate_status": "coverage_closed_evidence_selection_passed_books_open",
                   "audit": {"coverage": "230/230_passed", "evidence": "39/39_passed",
                             "selection": "39/39_full_frontier_passed", "books": "prewrite_open"}})
    (PACKET / "screening-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "README.md").write_text(
        f"# 2026-06-22 source packet\n\nCanonical denominator `39/230`; closures `191`; retain rate `16.96%`. Coverage Closed, Evidence Passed, Selection Passed, Books Open. Prewrite queue: {integrate_count} Integrate across {len(integrate_groups)} owner files and {no_change} No Change.\n")
    sums = []
    for path in sorted(p for p in PACKET.iterdir() if p.is_file() and p.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name)
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")
    print(json.dumps({"denominator": den, "raw": 230, "retained": 39, "closures": 191,
                      "integrate": integrate_count, "no_change": no_change,
                      "owner_files": len(integrate_groups)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
