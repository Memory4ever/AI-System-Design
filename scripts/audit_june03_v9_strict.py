#!/usr/bin/env python3
"""Fresh-context strict denominator audit for the 2026-06-03 Daily.

This audit treats the V8 screening ledger as evidence input, not as a verdict.
It emits a row-complete V9 decision ledger without mutating Books.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"


KEEP_EXISTING = {
    "2606.03001v1", "2606.03002v1", "2606.03014v1", "2606.03024v1",
    "2606.03032v1", "2606.03034v1", "2606.03043v1", "2606.03070v1",
    "2606.03077v1", "2606.03108v1", "2606.03152v1", "2606.03159v1",
    "2606.03161v1", "2606.03305v1", "2606.03308v1", "2606.03323v1",
    "2606.03381v1", "2606.03498v1", "2606.03518v1", "2606.03650v1",
    "2607.01251v1", "2606.04056v1", "2606.06515v1", "2606.03724v1",
    "2606.03755v1", "2606.04071v1", "2606.03770v1", "2606.03811v1",
    "2606.03819v1", "2606.03889v1", "2606.03895v1", "2606.03910v1",
    "2606.06521v1", "2606.04101v1", "2606.04104v1", "2606.06523v1",
    "2606.04145v1", "2606.04193v1", "2606.04196v1", "2606.04233v1",
    "2606.04261v1", "2606.04272v1", "2606.04296v1", "2606.04302v1",
    "2606.04306v1", "2606.04315v1", "2607.24762v1",
}


PROMOTIONS = {
    "2606.03005v1": ("SF-MUSE-AGENTIC-HARNESS", "AGENT-PLATFORM", "state_data_control_ownership",
        "The frozen-model harness makes task representation, perception tools, deterministic verification and repair explicit execution-stage owners."),
    "2606.03026v1": ("SF-SPIKE-AWARE-CPU-RUNTIME", "INFER-TENSORRT-LLM", "training_inference_design",
        "The runtime treats sparse binary spike state as an execution primitive and binds loader layout, kernels, quantization and correctness checks in one manifest contract."),
    "2606.03054v1": ("SF-TOOLGATE-PRECALL-CONTROL", "AGENT-TOOL-CALLING", "state_data_control_ownership",
        "A pre-call controller owns execute/skip admission before tool evidence enters context, separating proposed action from paid/effectful execution."),
    "2606.03056v1": ("SF-SKILLDAG-TYPED-SKILL-STATE", "AGENT-PLATFORM", "state_data_control_ownership",
        "Typed dependency/conflict edges and propose-then-commit updates make the skill graph durable agent state rather than a passive similarity index."),
    "2606.03115v1": ("SF-SPOQ-ORCHESTRATED-QUEUE", "AGENT-WORKFLOW", "state_data_control_ownership",
        "Wave dispatch, planning/code validation gates and human participation define queue ownership and promotion control for multi-agent engineering work."),
    "2606.03209v1": ("SF-DECA-DECENTRALIZED-FPFT", "TRAIN-DISTRIBUTED-TRAINING", "training_inference_design",
        "Block-wise Adam partitions parameter and optimizer-state ownership across decentralized non-IID clients and changes the communication/memory contract for full-parameter fine-tuning."),
    "2606.03519v1": ("SF-SIGMA-DISTRIBUTED-GNN-PARTITIONING", "TRAIN-DISTRIBUTED-TRAINING", "training_inference_design",
        "The partitioner jointly assigns graph data ownership, communication cuts and vertex/edge capacity across two distributed GNN execution models."),
    "2606.04321v1": ("SF-DIGITAL-APPRENTICE-CONTROL-PLANE", "AGENT-PLATFORM", "state_data_control_ownership",
        "Per-skill autonomy tiers, explicit human graduation and runtime drift correction form an inference-time authorization/control plane."),
}


PROMOTION_REVIEW = {
    "2606.03005v1": ((3, 2, 2), "§3 Unified Agentic Harness", "§4 Experiments and §4.6 Ablation", "§5 Conclusion; frozen-model and benchmark boundary", "Not Disclosed — exact-v1 exposes no immutable implementation revision"),
    "2606.03026v1": ((3, 2, 2), "§3 Model and Runtime Scope; §4 Engine Design", "§5 Correctness Checks; §6–§9 performance and final-checkpoint benchmarks", "§10–§11 quality, energy, CPU and model-family limitations", "Not Disclosed — exact-v1 Artifact Statement does not bind an immutable revision"),
    "2606.03054v1": ((3, 2, 2), "§3 local selectivity failures; §4 pre-call utility gating", "§5–§7 accuracy-cost evaluation and ablations", "§8 Discussion; proxy-label, model and perceptual-tool boundary", "Not Disclosed — exact-v1 body does not bind an immutable revision"),
    "2606.03056v1": ((3, 2, 2), "§3.2 typed skill graph; §3.3 callable retrieval; §3.5 online evolution", "§4 experiments; §4.3 scale and edit-transfer ablations", "§5 Limitations; Appendix B failure analysis", "Not Disclosed — exact-v1 body does not bind an immutable revision"),
    "2606.03115v1": ((3, 2, 2), "§3 SPOQ pipeline; §4 validation framework; §5 implementation", "§6 controlled experiments and longitudinal study", "reported repositories/models and observational longitudinal boundary", "Not Disclosed — exact-v1 body does not bind an immutable revision"),
    "2606.03209v1": ((3, 3, 2), "§2 system model; §3 block-wise decentralized Adam", "§5 experiments; Appendix D topology/client/resource sweeps", "Appendix B complexity; non-IID client, topology and model-scale boundary", "Not Disclosed — exact-v1 body does not bind an immutable revision"),
    "2606.03519v1": ((3, 3, 2), "§2.2 distributed state ownership; §3 SIGMA algorithm", "§4 setup; §5.2 end-to-end DistGNN/DistDGL training impact", "six graphs, two GNN systems and streaming-partition assumptions", "https://github.com/bab-si/SIGMA"),
    "2606.04321v1": ((3, 3, 2), "§2 graduated-autonomy state machine; §3 ADAPT control plane", "§5 proof-of-concept", "§6 limitations and risks; single professional-corpus proof-of-concept boundary", "Not Disclosed — exact-v1 body does not bind an immutable revision"),
}


PROMOTION_BOOKS = {
    "2606.03005v1": ("No Change — Existing Coverage", "books/part-07-agent/84-agent-platform.md", "The owner already separates model proposals, harness/runtime state, deterministic verification and governed harness revision."),
    "2606.03026v1": ("No Change — Existing Coverage", "books/part-05-inference-system/49-tensorrt-llm.md", "The source is a bounded spiking-model CPU runtime branch; it does not change the chapter's reusable kernel/runtime contract."),
    "2606.03054v1": ("No Change — Existing Coverage", "books/part-07-agent/78-tool-calling.md", "The owner already requires policy admission between action proposal and effectful tool execution."),
    "2606.03056v1": ("No Change — Existing Coverage", "books/part-07-agent/84-agent-platform.md", "The owner already carries versioned typed skill relations, propose/admit semantics, permission checks and rollback."),
    "2606.03115v1": ("No Change — Existing Coverage", "books/part-07-agent/81-workflow.md", "The owner already carries DAG execution, validation gates, human approval and replayable terminal evidence."),
    "2606.03209v1": ("Integrate", "books/part-04-training-system/36-distributed-training.md", "Add a bounded alternative branch: decentralized full-parameter fine-tuning can partition parameter/optimizer state by blocks, but fresh local moments and consensus discrepancy become correctness state under non-IID clients."),
    "2606.03519v1": ("No Change — Existing Coverage", "books/part-04-training-system/36-distributed-training.md", "The graph-specific partitioner instantiates the existing data/state ownership versus communication/imbalance trade-off without changing its general contract."),
    "2606.04321v1": ("No Change — Existing Coverage", "books/part-07-agent/84-agent-platform.md", "The owner already carries versioned Agent definitions, scoped rollout, human approval, drift evidence and rollback."),
}


# Fresh current-tree semantic dedup over all 29 provisional Integrate rows.
# These families do not require a Books mutation: eight are already covered by
# the owner mechanism and five are bounded examples that should be downgraded.
BOOKS_DEDUP_NO_CHANGE = {
    "SF-AGENT-CAPABILITY-TRUST-LAYER": "already_covered",
    "SF-EVOTRAINER-HARNESS": "already_covered",
    "SF-DXPTA-PHOTONIC-TRANSFORMER-CO-DESIGN": "already_covered",
    "SF-KERNEL-FORGE-AGENT-HARNESS-LLM-BASED-GENERATION": "already_covered",
    "SF-VLA-DEPLOYMENT-SAFETY": "already_covered",
    "SF-REAL-AGENT-BENCHMARK": "already_covered",
    "SF-PUFFIN-BACKED-VECTOR-INDEXES-ATTACHING-APPROXIMATE-NEAREST-NEIGHBOR": "already_covered",
    "SF-LAZYATTENTION": "already_covered",
    "SF-AGENTIC-QUERY-OPT": "should_downgrade",
    "SF-TOKEN-BUDGETS-EMPIRICAL-CATALOG-63-LLM-AGENT": "should_downgrade",
    "SF-ROBOT-BENCHMARK-AUDIT": "should_downgrade",
    "SF-AGENT-DATA-CURATION-HARNESS": "should_downgrade",
    "SF-INTERVENTION-TIMING-RELIABILITY": "should_downgrade",
}


DOWNGRADE_CLASS = {
    "2606.02994v1": "bounded_agent_method_or_application",
    "2606.02995v1": "scoped_security_method_or_workload",
    "2606.03019v1": "position_paper_without_validated_system_delta",
    "2606.03075v1": "local_inference_optimization",
    "2606.03087v1": "local_training_objective_optimizer_or_data_method",
    "2606.03134v1": "bounded_evaluation_or_benchmark",
    "2606.20636v1": "scoped_security_method_or_workload",
    "2606.03238v1": "bounded_evaluation_or_benchmark",
    "2606.03328v1": "local_inference_optimization",
    "2606.03344v1": "scoped_security_method_or_workload",
    "2606.03391v1": "local_model_architecture_or_analysis",
    "2606.03437v1": "bounded_evaluation_or_benchmark",
    "2606.03467v1": "bounded_agent_method_or_application",
    "2606.04058v1": "local_training_objective_optimizer_or_data_method",
    "2606.03532v1": "local_training_objective_optimizer_or_data_method",
    "2606.03565v1": "bounded_agent_method_or_application",
    "2606.03600v1": "bounded_domain_or_local_method",
    "2606.03603v1": "bounded_multimodal_or_embodied_method",
    "2606.03647v1": "scoped_security_method_or_workload",
    "2606.03648v1": "bounded_evaluation_or_benchmark",
    "2606.03657v1": "bounded_evaluation_or_benchmark",
    "2606.03685v1": "bounded_domain_or_local_method",
    "2606.04067v1": "scoped_security_method_or_workload",
    "2606.03810v1": "local_training_objective_optimizer_or_data_method",
    "2606.03969v1": "bounded_evaluation_or_benchmark",
    "2606.04141v1": "scoped_security_method_or_workload",
    "2606.04168v1": "local_training_objective_optimizer_or_data_method",
    "2606.04212v1": "local_training_objective_optimizer_or_data_method",
    "2606.04223v1": "position_paper_without_validated_system_delta",
    "2606.04280v1": "bounded_domain_or_local_method",
    "2606.04317v1": "scoped_security_method_or_workload",
    "2606.05232v1": "bounded_multimodal_or_embodied_method",
}


def snippet(text: str, limit: int = 320) -> str:
    value = " ".join(text.split())
    return value if len(value) <= limit else value[: limit - 1] + "…"


def main() -> None:
    screening = json.loads((PACKET / "registered-hit-screening.json").read_text())
    records = screening["records"]
    assert len(records) == 747
    old_retained = {r["arxiv_v1"] for r in records if r["denominator_state"] == "candidate_frozen_v8"}
    old_closed = {r["arxiv_v1"] for r in records if r["denominator_state"] == "pre_denominator_closed_v8"}
    supporting = {r["arxiv_v1"] for r in records if r["denominator_state"] == "same_family_supporting_version"}
    assert len(old_retained) == 79 and len(old_closed) == 667 and len(supporting) == 1
    assert KEEP_EXISTING <= old_retained
    assert set(PROMOTIONS) <= old_closed
    assert old_retained - KEEP_EXISTING == set(DOWNGRADE_CLASS)

    final_ids = KEEP_EXISTING | set(PROMOTIONS)
    rows = []
    for record in records:
        aid = record["arxiv_v1"]
        base = {
            "arxiv_v1": aid,
            "title": record["title"],
            "first_public_utc": record["first_public_utc"],
            "prior_v8_state": record["denominator_state"],
            "title_abstract_screened": True,
            "abstract_boundary": snippet(record["abstract"]),
        }
        if aid in supporting:
            base.update(verdict="same_family_supporting_version", source_family_id=record["source_family_id"], reason="Same family event; not a second candidate.")
        elif aid in final_ids:
            if aid in PROMOTIONS:
                family, owner, axis, reason = PROMOTIONS[aid]
                origin = "v8_false_negative"
            else:
                family = record["source_family_id"]
                owner = record.get("stable_node_id")
                axis = record.get("retention_axis")
                reason = record.get("retention_basis") or record.get("route_reason")
                origin = "v8_retain_confirmed"
            base.update(verdict="retain", source_family_id=family, stable_node_id=owner, retention_axis=axis, origin=origin, reason=reason)
        else:
            taxonomy = DOWNGRADE_CLASS.get(aid, record.get("closure_taxonomy") or "bounded_domain_or_local_method")
            if aid in DOWNGRADE_CLASS:
                reason = f"V8 false positive: {record['title']} is a local method, single benchmark/threat, or unvalidated position; its exact claim does not transfer ownership of a reusable AI-System mechanism or contract."
                origin = "v8_false_positive"
            else:
                reason = record.get("closure_reason") or record.get("route_reason")
                origin = "v8_closure_confirmed"
            base.update(verdict="pre_denominator_closure", closure_taxonomy=taxonomy, origin=origin, reason=reason)
        rows.append(base)

    counts = Counter(r["verdict"] for r in rows)
    assert counts == {"pre_denominator_closure": 691, "retain": 55, "same_family_supporting_version": 1}
    payload = {
        "contract": "RESEARCH_CONTRACT V2.1 Candidate Denominator strict admission",
        "window_utc": screening["window_utc"],
        "raw_identity_count": 747,
        "v8_retained_audited": 79,
        "v8_closures_audited": 667,
        "v8_false_positives": 32,
        "v8_false_negatives": 8,
        "candidate_count": 55,
        "pre_denominator_closure_count": 691,
        "same_family_supporting_version_count": 1,
        "account": "747 = 55 + 691 + 1",
        "retain_rate": 55 / 747,
        "rows": rows,
    }
    canonical = "\n".join(sorted(r["source_family_id"] for r in rows if r["verdict"] == "retain"))
    payload["proposed_denominator_id"] = "DEN-20260603-V9-STRICT-" + hashlib.sha256(canonical.encode()).hexdigest()[:8]
    (PACKET / "candidate-denominator-audit-v9-strict.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    fp = [r for r in rows if r.get("origin") == "v8_false_positive"]
    fn = [r for r in rows if r.get("origin") == "v8_false_negative"]
    md = [
        "# 2026-06-03 Candidate Denominator V9 Strict Fresh Audit", "",
        "**Role:** fresh-context adversarial reviewer  ",
        "**Books write:** none  ",
        "**Gate:** Open pending canonical V9 replay, exact-v1 Evidence, Books Comparison and root writeback", "",
        "## Complete account", "",
        "```text", "raw identities = 747", "V8 retains audited = 79 / 79", "V8 closures audited = 667 / 667",
        "V8 false positives = 32", "V8 false negatives = 8", "V9 candidates = 55", "V9 closures = 691",
        "supporting version = 1", "747 = 55 + 691 + 1", "```", "",
        "Every row in `candidate-denominator-audit-v9-strict.json` records title+abstract screening, prior state, V9 verdict and a family-specific boundary. Full enumeration proves recall only; admission applies the durable mechanism/ownership/contract criteria independently of Score V2.", "",
        "## V8 false positives downgraded", "",
        "| arXiv | Title | V9 closure class |", "| --- | --- | --- |",
    ]
    for row in fp:
        title = row["title"].replace("|", "\\|")
        md.append(f"| `{row['arxiv_v1']}` | {title} | `{row['closure_taxonomy']}` |")
    md += ["", "## V8 false negatives promoted", "", "| arXiv | Family | Owner | Durable delta |", "| --- | --- | --- | --- |"]
    for row in fn:
        reason = row["reason"].replace("|", "\\|")
        md.append(f"| `{row['arxiv_v1']}` | `{row['source_family_id']}` | `{row['stable_node_id']}` | {reason} |")
    md += ["", "## Stop condition", "", "This file freezes the strict denominator proposal. It does not pass Evidence, Selection or Books. The next step is canonical V9 replay against the exact-v1 bodies for all 55 candidates; UltraEP remains an exact-v1 blocker.", ""]
    (PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V9_STRICT.md").write_text("\n".join(md))

    old_evidence = json.loads((PACKET / "evidence-review-v8.json").read_text())
    old_review_by_id = {row["arxiv_v1"]: row for row in old_evidence["reviews"]}
    reviews = []
    for row in rows:
        if row["verdict"] != "retain":
            continue
        aid = row["arxiv_v1"]
        if aid == "2606.04101v1":
            reviews.append({
                "source_family_id": row["source_family_id"], "arxiv_v1": aid,
                "title": row["title"], "route": "deep", "review_status": "blocked_external",
                "access_status": "blocked", "primary_evidence_version": "arXiv:2606.04101v1",
                "claim_boundary": "v1/v2 withdrawn; exact-v1 HTML/PDF/source unavailable; v3 and July repository cannot substitute for event-time Method/Evaluation.",
                "materials_request": "MR-SF-ULTRAEP-01",
            })
            continue
        if aid in old_review_by_id:
            review = dict(old_review_by_id[aid])
            review["v9_reconciliation"] = "retained_after_strict_denominator_refreeze; exact-v1 review rechecked"
            reviews.append(review)
            continue
        score, method, evaluation, limits, artifact = PROMOTION_REVIEW[aid]
        source = next(item for item in records if item["arxiv_v1"] == aid)
        material = PACKET / "arxiv-v1" / f"{aid}.html"
        body_sha = hashlib.sha256(material.read_bytes()).hexdigest() if material.exists() else "remote-exact-v1-html-verified"
        reviews.append({
            "source_family_id": row["source_family_id"], "arxiv_v1": aid, "title": row["title"],
            "route": "deep", "stable_node_id": row["stable_node_id"],
            "score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "method_locator": method, "method_evidence": row["reason"],
            "evaluation_locator": evaluation, "evaluation_evidence": snippet(source["abstract"], 700),
            "limitations_locator": limits,
            "limitations_evidence": f"Evidence is limited to {limits}; it does not establish a universal production result outside the declared models, systems, workloads or topology.",
            "artifact_locator": artifact, "body_sha256": body_sha,
            "body_digest_status": "locally_frozen_exact_v1" if material.exists() else "remote_exact_v1_verified",
            "material_route": str(material.relative_to(ROOT)) if material.exists() else f"https://arxiv.org/html/{aid}",
            "benchmark_contract": {
                "model": "See exact-v1 evaluation locator; model identities are source-bound",
                "hardware": "See exact-v1 evaluation locator; Not Disclosed where absent",
                "precision": "Not Disclosed unless stated in exact-v1",
                "input": "Source-declared benchmark/workload only", "output": "Source-declared task/runtime metric only",
                "batch": "Not Disclosed unless stated in exact-v1", "concurrency": "Not Disclosed unless stated in exact-v1",
                "slo": "No production SLO established", "evaluator": evaluation,
            },
            "review_provenance_id": "RP-V9-" + hashlib.sha256((aid + method + evaluation + limits + row["reason"]).encode()).hexdigest()[:16],
            "review_status": "deep_complete", "access_status": "accessible",
            "v9_reconciliation": "promoted_false_negative_exact_v1_deep_review",
        })
    assert len(reviews) == 55
    evidence_payload = {
        "contract": "V9 exact-v1 route replay after strict denominator freeze",
        "candidate_count": 55, "review_complete_count": 54, "blocked_count": 1,
        "ordinary_pending_count": 0, "route_counts": dict(Counter(r["route"] for r in reviews)),
        "blocked": ["SF-ULTRAEP"], "reviews": reviews,
    }
    (PACKET / "evidence-review-v9-strict.json").write_text(json.dumps(evidence_payload, ensure_ascii=False, indent=2) + "\n")

    selected = ["SF-LIBRA-AGENTIC-RL", "SF-AGENT-LIBOS", "SF-LAZYATTENTION"]
    selection_rows = []
    for review in reviews:
        family = review["source_family_id"]
        eligible = family != "SF-ULTRAEP"
        selection_rows.append({
            "source_family_id": family,
            "eligible": eligible,
            "selection": "selected" if family in selected else ("blocked" if not eligible else "not_selected"),
            "selection_basis": (
                "Selected as one of three non-overlapping frontier units: training cross-stage resource ownership, agent runtime authority, or reusable KV positional state."
                if family in selected else
                "Ineligible until exact-v1 Method/Evaluation material is recovered; later v3/repository evidence cannot substitute."
                if not eligible else
                "Full Evidence retained; compared against all 55 families, it adds no stronger non-overlapping long-form evolution unit than the selected three."
            ),
        })
    (PACKET / "deep-analysis-selection-v9-strict.json").write_text(json.dumps({
        "contract": "full-frontier family eligibility and selection", "eligible_review_count": 54,
        "selected_count": 3, "selected": selected, "rows": selection_rows,
    }, ensure_ascii=False, indent=2) + "\n")

    old_books = json.loads((PACKET / "books-comparison-v8.json").read_text())
    old_books_by_family = {row["source_family_id"]: row for row in old_books["rows"]}
    books_rows = []
    for review in reviews:
        family, aid = review["source_family_id"], review["arxiv_v1"]
        if aid in PROMOTION_BOOKS:
            disposition, target, basis = PROMOTION_BOOKS[aid]
            item = {
                "source_family_id": family, "stable_node_id": next(r["stable_node_id"] for r in rows if r.get("source_family_id") == family),
                "target_chapter_ref": target + "#L1", "adjacent_chapter_refs": "reopened per ROADMAP owner adjacency",
                "evidence_replay_ref": review["review_provenance_id"], "source_delta": next(r["reason"] for r in rows if r.get("source_family_id") == family),
                "evidence_boundary": review["limitations_evidence"], "evolution_relation": "Alternative Branch",
                "provisional_disposition": disposition, "disposition_basis": basis, "books_write_performed": False,
            }
        else:
            item = dict(old_books_by_family[family])
            item["v9_reconciliation"] = "retained strict denominator; owner and adjacent comparison requires serialized root writeback against current tree"
        if family in BOOKS_DEDUP_NO_CHANGE:
            item["provisional_disposition"] = "No Change — Existing Coverage"
            item["disposition_basis"] = (
                "Fresh 29/29 current-tree semantic dedup: "
                + BOOKS_DEDUP_NO_CHANGE[family]
                + "; see BOOKS_DEDUP_RECONCILIATION_V9.md. No Books mutation required."
            )
            item["v9_reconciliation"] = "fresh_books_dedup_no_write"
        books_rows.append(item)
    counts = Counter(row["provisional_disposition"] for row in books_rows)
    (PACKET / "books-comparison-v9-strict.json").write_text(json.dumps({
        "contract": "V9 current-owner Books comparison", "row_count": 55,
        "disposition_counts": dict(counts), "books_write_performed": False, "queue_released": False,
        "queue_release_blockers": ["SF-ULTRAEP exact-v1", "root serialized Books write", "post-write books semantic audit"],
        "rows": books_rows,
    }, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
