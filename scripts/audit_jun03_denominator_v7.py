#!/usr/bin/env python3
"""Build the fresh-context 2026-06-03 denominator audit.

This script deliberately audits denominator membership only.  It does not
inherit Score V2, Review completion, or Books disposition as retention gates.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
REPAIR = PACKET / "candidate-denominator-audit-v6-repair.json"
CLOSURES = PACKET / "closure-reconciliation-v3.json"
SCREENING = PACKET / "registered-hit-screening.json"
OUT_JSON = PACKET / "candidate-denominator-audit-v7-fresh.json"
OUT_MD = PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V7_FRESH.md"


# One-based row identities from the immutable 320-row V6 repair artifact.
# The list was produced by a fresh-context title+abstract challenge, not by a
# score threshold or a target retain rate.
RETAIN_OLD_ROWS = {
    2, 3, 4, 5, 9, 10, 13, 16, 17, 19, 26, 28, 29, 33, 42, 49, 55, 56,
    57, 71, 74, 86, 88, 92, 94, 99, 106, 110, 117, 118, 120, 122, 123,
    124, 130, 137, 139, 145, 146, 147, 148, 152, 157, 160, 164, 168,
    175, 176, 177, 190, 193, 195, 200, 209, 216, 217, 225, 227, 228,
    230, 235, 241, 245, 249, 251, 253, 256, 257, 258, 262, 275, 311,
    312, 317, 320,
}

# These two closure rows expose a cross-boundary systems responsibility from
# title+abstract and therefore warrant candidate-level review.  Promotion is
# recall-only; it does not claim that Method/Evaluation has been reviewed.
PROMOTE_FROM_CLOSURE = {
    "2606.06515v1": {
        "source_family_id": "SF-DXPTA-PHOTONIC-TRANSFORMER-CO-DESIGN",
        "stable_node_id": "INFER-TENSORRT-LLM",
        "retention_axis": "training_or_inference_design_judgment",
        "basis": (
            "The primary object is a transformer-accelerator HW/SW design-space "
            "exploration whose optical dataflow changes the boundary between model "
            "operators, mapping policy, accelerator resources, and performance evidence."
        ),
    },
    "2606.04071v1": {
        "source_family_id": "SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS",
        "stable_node_id": "PLATFORM-SECURITY",
        "retention_axis": "security_or_release_contract",
        "basis": (
            "The primary object identifies behavior transfer through model-generated "
            "carriers that are not human-visible, changing provenance, trust-boundary, "
            "and release-evaluation requirements when models consume other models' output."
        ),
    },
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def norm_excerpt(text: str | None, limit: int = 300) -> str:
    value = re.sub(r"\s+", " ", text or "").strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def closure_class(title: str, owner: str) -> str:
    lower = title.lower()
    if any(token in lower for token in ("benchmark", "evaluat", "assessment", "study", "diagnos")):
        return "bounded_evaluation_or_benchmark"
    if owner == "PLATFORM-SECURITY" or any(token in lower for token in ("attack", "defense", "safety", "secure", "privacy")):
        return "scoped_security_method_or_workload"
    if owner.startswith("TRAIN-"):
        return "local_training_objective_optimizer_or_data_method"
    if owner.startswith("INFER-"):
        return "local_inference_optimization"
    if owner.startswith("AGENT-"):
        return "bounded_agent_method_or_application"
    if owner.startswith("MULTIMODAL-"):
        return "bounded_multimodal_or_embodied_method"
    if owner.startswith("MODEL-"):
        return "local_model_architecture_or_analysis"
    return "bounded_domain_or_local_method"


def downgrade_reason(row: dict) -> tuple[str, str]:
    title = row["title"]
    owner = row["stable_node_id"]
    category = closure_class(title, owner)
    claim = norm_excerpt(row.get("family_specific_retention_basis"))
    explanations = {
        "bounded_evaluation_or_benchmark": (
            "The work defines or measures a bounded task, dataset, evaluator, or diagnostic; "
            "the available evidence does not redefine a reusable cross-workload evaluation "
            "contract or correct an existing platform-level conclusion."
        ),
        "scoped_security_method_or_workload": (
            "The attack or defense is scoped to one threat construction, model family, or "
            "application; it does not yet change the durable release/security contract."
        ),
        "local_training_objective_optimizer_or_data_method": (
            "The contribution is a local objective, optimizer, data recipe, or task-specific "
            "training improvement; no reusable training-system ownership or cross-boundary "
            "design change is established."
        ),
        "local_inference_optimization": (
            "The contribution is a local inference optimization or bounded workload result; "
            "it does not change durable runtime state ownership, scheduling, execution-plan, "
            "or serving-SLO judgment."
        ),
        "bounded_agent_method_or_application": (
            "The contribution is an agent method or application variant; it does not establish "
            "a reusable information/action/workflow-state ownership or protocol contract."
        ),
        "bounded_multimodal_or_embodied_method": (
            "The contribution is tied to a multimodal/embodied task or model variation; it does "
            "not establish a durable representation identity, mutable world-state, environment "
            "transition, or physical-control contract."
        ),
        "local_model_architecture_or_analysis": (
            "The contribution is a local architecture or analysis result and does not correct "
            "a durable model-system design judgment."
        ),
        "bounded_domain_or_local_method": (
            "The contribution remains a bounded domain study or local method and does not own "
            "a durable AI-System mechanism, state/data/control boundary, or design contract."
        ),
    }
    reason = f"{title}: {explanations[category]} Evidence challenged: {claim}"
    return category, reason


def main() -> None:
    repair = load(REPAIR)
    closure_artifact = load(CLOSURES)
    screening = load(SCREENING)
    old_rows = repair["rows"]
    closure_rows = [
        row for row in closure_artifact["records"]
        if row["decision"] == "closed_outside_candidate_denominator"
    ]
    assert len(old_rows) == 320
    assert len(closure_rows) == 426
    assert len(screening["records"]) == 747

    screen_by_id = {row["arxiv_v1"]: row for row in screening["records"]}
    retained_audit = []
    proposed_candidates = []
    closure_reason_counts: Counter[str] = Counter()
    identity_disputes = []

    for index, row in enumerate(old_rows, start=1):
        arxiv_v1 = row["primary_identifier"].removeprefix("arXiv:")
        screening_row = screen_by_id[arxiv_v1]
        anomaly = bool(screening_row.get("identifier_month_anomaly"))
        if index in RETAIN_OLD_ROWS and not anomaly:
            decision = "retain_after_fresh_context_audit"
            reason = (
                f"{row['title']}: retained because the challenged evidence plausibly changes "
                f"{row['retention_axis'].replace('_', ' ')} at owner {row['stable_node_id']}. "
                f"Boundary: {norm_excerpt(row.get('evidence_boundary'))}"
            )
            proposed_candidates.append({
                **row,
                "proposed_denominator_state": "retain_after_fresh_context_audit",
                "fresh_context_reason": reason,
                "origin": "v6_retained",
            })
        else:
            if anomaly:
                category = "identity_date_disputed"
                reason = (
                    f"{row['title']}: identifier {arxiv_v1} is later than the asserted "
                    f"2026-06-02 first-public date. Exact v1 history/identity must be recovered "
                    "before candidate ownership can be established; content relevance cannot "
                    "override an impossible event identity."
                )
                identity_disputes.append(arxiv_v1)
            else:
                category, reason = downgrade_reason(row)
            decision = "move_to_pre_denominator_closure"
            closure_reason_counts[category] += 1
        retained_audit.append({
            "row_index": index,
            "source_family_id": row["source_family_id"],
            "primary_identifier": row["primary_identifier"],
            "title": row["title"],
            "old_state": "retain_provisional",
            "fresh_context_decision": decision,
            "closure_reason_class": None if decision.startswith("retain") else category,
            "fresh_context_reason": reason,
            "identifier_month_anomaly": anomaly,
            "access_state": "blocked" if row["source_family_id"] == "SF-ULTRAEP" else "accessible",
        })

    closure_audit = []
    false_negative_promotions = []
    for row in closure_rows:
        arxiv_v1 = row["arxiv_v1"]
        screening_row = screen_by_id[arxiv_v1]
        anomaly = bool(screening_row.get("identifier_month_anomaly"))
        if arxiv_v1 in PROMOTE_FROM_CLOSURE and not anomaly:
            promotion = PROMOTE_FROM_CLOSURE[arxiv_v1]
            decision = "promote_to_candidate_provisional"
            reason_class = None
            reason = f"{row['title']}: {promotion['basis']}"
            candidate = {
                "source_family_id": promotion["source_family_id"],
                "primary_identifier": f"arXiv:{arxiv_v1}",
                "title": row["title"],
                "proposed_denominator_state": "retain_after_fresh_context_audit",
                "retention_axis": promotion["retention_axis"],
                "stable_node_id": promotion["stable_node_id"],
                "review_status": "pending",
                "evidence_ref": "title+abstract-only",
                "family_specific_retention_basis": promotion["basis"],
                "evidence_boundary": (
                    "Promotion establishes candidate recall only. Exact-v1 Method, Evaluation, "
                    "limitations, artifact, scoring, and Books comparison remain pending."
                ),
                "fresh_context_reason": reason,
                "origin": "v6_pre_denominator_closure",
            }
            proposed_candidates.append(candidate)
            false_negative_promotions.append(arxiv_v1)
        elif anomaly:
            decision = "confirm_closure_identity_date_disputed"
            reason_class = "identity_date_disputed"
            reason = (
                f"{row['title']}: identifier {arxiv_v1} is later than the asserted "
                f"first-public timestamp {row['first_public_utc']}. It cannot be promoted until "
                "exact submission history resolves identity and owner date."
            )
            identity_disputes.append(arxiv_v1)
            closure_reason_counts[reason_class] += 1
        else:
            decision = "confirm_pre_denominator_closure"
            reason_class = "existing_family_specific_closure_confirmed"
            reason = (
                f"{row['title']}: {row['v5_denominator_basis']} Fresh challenge: "
                f"{norm_excerpt(row.get('fresh_context_closure_review'))}"
            )
            closure_reason_counts[reason_class] += 1
        closure_audit.append({
            "registered_hit_id": row["registered_hit_id"],
            "arxiv_v1": arxiv_v1,
            "title": row["title"],
            "old_state": "pre_denominator_closure",
            "fresh_context_decision": decision,
            "closure_reason_class": reason_class,
            "fresh_context_reason": reason,
            "identifier_month_anomaly": anomaly,
            "access_state": "identity_disputed" if anomaly else "accessible",
        })

    assert len(retained_audit) == 320
    assert len(closure_audit) == 426
    assert len(false_negative_promotions) == 2
    assert len({row["primary_identifier"] for row in proposed_candidates}) == len(proposed_candidates)

    old_retained = len(old_rows)
    new_retained = len(proposed_candidates)
    downgraded = sum(
        row["fresh_context_decision"] == "move_to_pre_denominator_closure"
        for row in retained_audit
    )
    blocked = [
        row["primary_identifier"] for row in proposed_candidates
        if row["source_family_id"] == "SF-ULTRAEP"
    ]
    proposed_pre_denominator_closures = [
        {
            "primary_identifier": row["primary_identifier"],
            "source_family_id": row["source_family_id"],
            "title": row["title"],
            "closure_reason_class": row["closure_reason_class"],
            "family_specific_closure_reason": row["fresh_context_reason"],
            "origin": "v6_retained",
            "access_state": row["access_state"],
        }
        for row in retained_audit
        if row["fresh_context_decision"] == "move_to_pre_denominator_closure"
    ] + [
        {
            "primary_identifier": f"arXiv:{row['arxiv_v1']}",
            "source_family_id": None,
            "title": row["title"],
            "closure_reason_class": row["closure_reason_class"],
            "family_specific_closure_reason": row["fresh_context_reason"],
            "origin": "v6_pre_denominator_closure",
            "access_state": row["access_state"],
        }
        for row in closure_audit
        if row["fresh_context_decision"] != "promote_to_candidate_provisional"
    ]
    assert len(proposed_pre_denominator_closures) == 669
    canonical_rows = json.dumps(
        proposed_candidates, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    ledger_sha256 = hashlib.sha256(canonical_rows).hexdigest()

    artifact = {
        "contract": "Fresh-context denominator audit V7; July-comparable semantic standard",
        "role": "independent adversarial denominator auditor",
        "raw_identity_count": 747,
        "same_family_supporting_version_count": 1,
        "old_retained_count": old_retained,
        "old_pre_denominator_closure_count": len(closure_rows),
        "audited_old_retained_count": len(retained_audit),
        "audited_old_closure_count": len(closure_audit),
        "new_retained_count": new_retained,
        "new_pre_denominator_closure_count": len(proposed_pre_denominator_closures),
        "new_retained_rate_percent": round(new_retained / 747 * 100, 2),
        "downgraded_from_old_retained": downgraded,
        "promoted_from_old_closure": len(false_negative_promotions),
        "false_negative_promotions": false_negative_promotions,
        "identity_date_dispute_count": len(set(identity_disputes)),
        "identity_date_disputes": sorted(set(identity_disputes)),
        "blocked_candidate_count": len(blocked),
        "blocked_candidates": blocked,
        "closure_reason_counts": dict(sorted(closure_reason_counts.items())),
        "coverage_gate": "Open",
        "evidence_gate": "Open",
        "selection_gate": "Open",
        "books_comparison_gate": "Open",
        "books_write_performed": False,
        "ledger_sha256": ledger_sha256,
        "proposed_candidates": proposed_candidates,
        "proposed_pre_denominator_closures": proposed_pre_denominator_closures,
        "old_retained_audit": retained_audit,
        "old_closure_audit": closure_audit,
    }
    OUT_JSON.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    reason_lines = "\n".join(
        f"| `{reason}` | {count} |" for reason, count in sorted(closure_reason_counts.items())
    )
    anomaly_lines = "\n".join(f"- `{item}`" for item in sorted(set(identity_disputes)))
    md = f"""# 2026-06-03 Candidate Denominator V7 Fresh Audit

**Role:** independent fresh-context adversarial auditor  
**Books write:** none  
**Gate:** Coverage / Evidence / Selection / Books Comparison 全部 Open

## 1. Claim under challenge

V6 repair 提议保留全部 320 个旧候选。该提议把“能映射 ROADMAP、存在机制或 evaluation 关键词”当成了候选资格。本轮按与 7 月可比的标准逐项挑战：完整语义筛选只保证 Coverage recall；只有可能改变长期 AI System mechanism、state/data/control ownership、evaluation contract、Training/Inference/Platform design judgment，或修正 Books 认知的 family 才能进入候选分母。

## 2. 完整审计账目

```text
raw identities                         = 747
same-family supporting version         =   1
old retained audited                   = 320 / 320
old pre-denominator closures audited   = 426 / 426
new retained                           = {new_retained}
downgraded from old retained           = {downgraded}
promoted from old closures             = {len(false_negative_promotions)}
raw-to-new retain rate                 = {new_retained / 747 * 100:.2f}%
identity/date disputed                 = {len(set(identity_disputes))}
blocked retained candidate             = {len(blocked)}
```

新比例是逐项语义判断的结果，不是目标配额。完整 320 + 426 row 结果保存在 `candidate-denominator-audit-v7-fresh.json`；每个 downgrade 都绑定 title、被挑战的具体 claim 与 family-specific closure reason。

## 3. False-positive / false-negative result

- V6 的 320 个 provisional retained 中，{downgraded} 个被降为 pre-denominator closure；典型错误是把单领域 benchmark、局部 objective/optimizer、单模型 attack/defense、或任务级多模态/Agent 方法误当成长期系统责任。
- 从 426 个旧 closure 中识别 2 个 provisional false negative：`2606.06515v1`（Transformer photonic accelerator HW/SW co-design）与 `2606.04071v1`（model-to-model covert influence）。两者只恢复 candidate recall；全文、评分、Evidence 与 Books 尚未释放。
- 22 个 family 的 arXiv identifier 月份晚于记录的 2026-06-02 first-public timestamp。它们保持 identity/date disputed；相关性不能覆盖不可能的事件身份。

## 4. Closure reasons

| Reason | Count |
| --- | ---: |
{reason_lines}

## 5. Identity / date disputes

{anomaly_lines}

这些记录需要 exact-v1 submission history 或 identity recovery；在恢复前既不能按 06-03 owner candidate 计分，也不能用后续月份 identifier 反推 6 月首次公开。

## 6. Access and Gate truth

| Scope | Status | Reason |
| --- | --- | --- |
| Coverage | Open | fresh audit 已给出 denominator proposal，但 22 个 identity/date dispute 尚未恢复，且 repair owner 需要把新分母写回 canonical ledger |
| Evidence | Open | 2 个新晋 family 尚未读取 exact-v1；`SF-ULTRAEP` exact-v1 仍 blocked；旧 Evidence required set 已因分母变化失效 |
| Selection | Open | 必须基于新冻结 denominator 重新计算，不能继承 V5 |
| Books Comparison | Open | 必须基于 Evidence Pass 后的新候选重做；本轮没有 Books write |

`proposed_candidates` canonical SHA-256: `{ledger_sha256}`

## 7. Stop condition

本轮完成的是全量 320-row false-positive challenge 与 426-row false-negative challenge。它不是 06-03 Daily Complete，也不自证 downstream Gate。下一步由 repair owner 复核并写回 canonical denominator；之后需由不同上下文对新 artifact 做一次 FP/FN 复验，再重放 Evidence、Selection 与 Books Comparison。
"""
    OUT_MD.write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
