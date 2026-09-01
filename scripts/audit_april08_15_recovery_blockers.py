#!/usr/bin/env python3
"""Record independent 2026-04-08..15 recovery findings and route a withdrawal.

This reviewer artifact intentionally does not read a Weekly and does not edit
shared Books.  A failed denominator audit prevents downstream pre-write pass.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTH = ROOT / "papers/2026/04"
SOURCES = MONTH / "_sources"
WITHDRAWN_AID = "2604.06798"
WITHDRAWN_FID = "SF-2026-ARXIV-2604-06798"

# These are independently confirmed false negatives, not an eligibility seed.
# Each abstract states a durable mechanism that the stored closure reason denies.
FINDINGS = {
    8: [
        ("2604.05417", "multi-drafter speculative decoding with alignment feedback", "INFER-SPECULATIVE-DECODING"),
        ("2604.05438", "partial-KV decoding with residual-mass accounting", "INFER-KV-CACHE"),
        ("2604.05887", "hybrid KV-cache compression for multimodal inference", "INFER-KV-CACHE"),
        ("2604.06550", "hierarchical malicious-agent-skill triage", "PLATFORM-SECURITY"),
    ],
    9: [
        ("2604.06694", "audio-model KV-cache eviction", "INFER-KV-CACHE"),
        ("2604.06956", "nested pipeline training across 1,500+ accelerators", "TRAIN-PIPELINE-PARALLEL"),
        ("2604.07622", "dynamic-ensemble speculative verification", "INFER-SPECULATIVE-DECODING"),
    ],
    10: [
        ("2604.07681", "hierarchical planner/executor agent orchestration on Aurora", "AGENT-MULTI-AGENT"),
        ("2604.08133", "budget-aware expert activation for MoE inference", "MODEL-MOE"),
        ("2604.16469", "beam-aware speculative execution for resource-constrained agents", "INFER-SPECULATIVE-DECODING"),
    ],
    11: [
        ("2604.09048", "energy-aware heterogeneous-GPU LLM inference benchmark contract", "PLATFORM-COST"),
        ("2604.09285", "service-agent graph evaluation benchmark", "PLATFORM-EVALUATION-SYSTEM"),
        ("2604.15356", "sequential KV compression with probabilistic language tries", "INFER-KV-CACHE"),
    ],
    12: [
        ("2604.09970", "decentralized local training with adaptive gradients and compressed communication", "TRAIN-DISTRIBUTED-TRAINING"),
        ("2604.10044", "runtime KV intervention for self-reinforcing attention loops", "INFER-KV-CACHE"),
        ("2604.10390", "silent permanent-GPU-fault corruption in LLM training", "PLATFORM-MONITORING"),
    ],
    13: [
        ("2604.10496", "clustering plus low-precision quantization for MoE outliers", "MODEL-MOE"),
        ("2604.10690", "spatial world-state probing in grid-world tasks", "MULTIMODAL-WORLD-MODELS"),
    ],
    14: [
        ("2604.10907", "latency-aware multi-model serving resource allocation and routing", "INFER-SCHEDULING"),
        ("2604.11572", "drift-aware post-training quantization for VLA models", "MULTIMODAL-EMBODIED-VLA"),
        ("2604.11947", "residual bottlenecks for low-bandwidth pipeline parallelism", "TRAIN-PIPELINE-PARALLEL"),
    ],
    15: [
        ("2604.12301", "measurement of cloud-token reduction tactics for coding-agent workloads", "PLATFORM-COST"),
        ("2604.12599", "foundation-model training-to-serving lifecycle on HPC", "PLATFORM-PRODUCTION"),
        ("2604.12782", "hardware-efficient W4A4 quantization with channel outlier separation", "INFER-GPU-MEMORY"),
    ],
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def remove_marked_block(text: str, kind: str, identifier: str) -> str:
    pattern = re.compile(
        rf"\n?<!-- {re.escape(kind)}:{re.escape(identifier)}:start -->.*?"
        rf"<!-- {re.escape(kind)}:{re.escape(identifier)}:end -->\n?",
        re.S,
    )
    return pattern.sub("\n", text)


def route_withdrawn() -> None:
    packet = SOURCES / "daily-20260409"
    for name in ("screening-ledger-final.json", "screening-ledger-provisional.json"):
        path = packet / name
        doc = load(path)
        row = next(x for x in doc["identities"] if x["arxiv_id"] == WITHDRAWN_AID)
        row.update({
            "screening_route": "withdrawal_check",
            "screening_status": "withdrawn_primary_closed_before_denominator",
            "screening_reason": (
                "Official arXiv abs/v1 carries the narrow phrase 'this paper has been withdrawn'; "
                "the identity is retained only as a screening closure and is excluded from "
                "Candidate, Review, Deep Analysis, and Books."
            ),
            "candidate_state": "pre-denominator closure",
            "integration_disposition": "Rejected — Withdrawn Primary",
            "screening_decision": "withdrawn_primary_closure",
            "review_status": "not_applicable_withdrawn",
            "access_status": "withdrawn_identity_only",
            "prior_review_ref": "—",
        })
        row.pop("owner_node", None)
        row.pop("score_v2", None)
        doc["candidate_denominator"] = 19
        doc["pre_denominator_closed"] = 528
        doc["gate_status"] = "open_independent_false_negative_findings"
        dump(path, doc)

    review_path = packet / "exact-v1-review-packet.json"
    review = load(review_path)
    review["items"] = [x for x in review["items"] if x["arxiv_id"] != WITHDRAWN_AID]
    dump(review_path, review)

    compare_path = packet / "books-current-content-comparison.json"
    compare = load(compare_path)
    compare["items"] = [x for x in compare["items"] if x["arxiv_id"] != WITHDRAWN_AID]
    dump(compare_path, compare)

    materials_path = packet / "materials-request.json"
    materials = load(materials_path)
    materials["items"] = [x for x in materials["items"] if x["source_family_id"] != WITHDRAWN_FID]
    materials["withdrawn_closed_request"] = "MR-20260409-2604-06798"
    dump(materials_path, materials)

    access_path = packet / "exact-v1-access-receipt.json"
    access = load(access_path)
    access["candidate_count"] = 19
    access["routed_identity_rows"] = 20
    access["withdrawn_screening_closure_count"] = 1
    dump(access_path, access)

    coverage_path = packet / "coverage-receipt.json"
    coverage = load(coverage_path)
    coverage.update({
        "retained": 19,
        "pre_denominator_closed": 528,
        "withdrawn_primary_source": 1,
        "status": "open_independent_false_negative_findings",
    })
    coverage["ledger_sha256"] = hashlib.sha256((packet / "screening-ledger-final.json").read_bytes()).hexdigest()
    dump(coverage_path, coverage)

    author_path = packet / "semantic-author-audit.json"
    author = load(author_path)
    author["provisional_denominator"] = 19
    author["exact_v1_blocked"] = 19
    author["withdrawn_closed_before_denominator"] = WITHDRAWN_FID
    author.setdefault("unresolved_findings", []).append(
        "Independent reverse audit found false negatives; denominator must be re-frozen before Evidence/Books review."
    )
    dump(author_path, author)

    readme_path = MONTH / "09/README.md"
    text = readme_path.read_text(encoding="utf-8")
    text = re.sub(r"^.*(?:2604\.06798|SF-2026-ARXIV-2604-06798|MR-20260409-2604-06798).*$\n?", "", text, flags=re.M)
    for kind in ("review", "claim", "analysis-decision", "books-review", "existing", "delta"):
        text = remove_marked_block(text, kind, WITHDRAWN_FID)
    text = text.replace("DEN-20260409-AUTHOR-20", "DEN-20260409-REVIEWER-19")
    text = text.replace("Candidate Denominator=20", "Candidate Denominator=19")
    text = text.replace("retained=20", "retained=19")
    text = text.replace("closure=527", "closure=528")
    text = text.replace("blocked=20", "blocked=19")
    text = text.replace("Integrate queue=0。", "Integrate queue=0；denominator 因 independent false-negative findings 尚未重冻。")
    note = (
        "Withdrawal closure：`arXiv:2604.06798v1` 的 official abs 使用窄语义短语 "
        "`this paper has been withdrawn`；该 identity 只保留在 screening/access closure，"
        "不进入 Candidate、Review、Deep Analysis 或 Books。\n\n"
    )
    marker = "## 2. Candidate Ledger"
    if note not in text:
        text = text.replace(marker, note + marker)
    text = re.sub(
        r"screening-ledger-final\.json#sha256=[a-f0-9]{64}",
        "screening-ledger-final.json#sha256=" + coverage["ledger_sha256"],
        text,
    )
    readme_path.write_text(text, encoding="utf-8")


def audit_day(day: int) -> None:
    packet = SOURCES / f"daily-202604{day:02d}"
    ledger = load(packet / "screening-ledger-final.json")
    identities = {x["arxiv_id"]: x for x in ledger["identities"]}
    rows = []
    for aid, mechanism, owner in FINDINGS[day]:
        source = identities[aid]
        rows.append({
            "arxiv_id": aid,
            "source_family_id": source["source_family_id"],
            "title": source["title"],
            "stored_screening_status": source["screening_status"],
            "stored_closure_reason": source["screening_reason"],
            "independent_mechanism": mechanism,
            "required_owner": owner,
            "finding": (
                "false negative: title+abstract state a durable system mechanism, but the stored "
                "closure denies a state/data/control, runtime, or evaluation-contract delta"
            ),
            "resolution": "reopen; fetch and review official exact-v1 before re-freezing denominator",
        })
    access = load(packet / "exact-v1-access-receipt.json")
    receipt = {
        "schema": "historical-daily-independent-recovery-prewrite-audit-v1",
        "report_date": f"2026-04-{day:02d}",
        "auditor_role": "fresh-context non-author reviewer",
        "weekly_semantic_inputs": 0,
        "raw_identities_replayed": len(ledger["identities"]),
        "pre_audit_candidate_denominator": ledger["candidate_denominator"],
        "pre_audit_closures": ledger["pre_denominator_closed"],
        "recovered_exact_v1_accessible_for_existing_denominator": access["accessible_count"],
        "withdrawn_screening_closures": access.get("withdrawn_count", 0),
        "source_review_complete": 0,
        "source_review_pending_existing_accessible": access["accessible_count"],
        "coverage_verdict": "fail",
        "evidence_verdict": "blocked_by_unfrozen_denominator",
        "books_prewrite_verdict": "blocked_by_unfrozen_denominator",
        "false_negative_findings": rows,
        "unresolved_findings": len(rows),
        "gate_effect": "Coverage, Evidence, and Books remain Open; no queue is eligible for writeback.",
        "shared_books_modified": False,
    }
    dump(packet / "independent-recovery-prewrite-audit.json", receipt)

    readme_path = MONTH / f"{day:02d}/README.md"
    text = readme_path.read_text(encoding="utf-8")
    ids = ", ".join(f"`{x[0]}`" for x in FINDINGS[day])
    finding_note = (
        f"Independent pre-write finding：full title+abstract reverse audit found false negatives {ids}. "
        "这些 family 的摘要明确改变长期 runtime/state/control/evaluation contract，却被现有 closure "
        "泛化为局部任务或 benchmark。分母必须重开并恢复 exact-v1；在此之前 Coverage/Evidence/Books "
        "保持 Open，既有 Books queue 不具备写回资格。收据："
        "`independent-recovery-prewrite-audit.json`。\n\n"
    )
    marker = "## 7. Semantic Audit"
    if finding_note not in text:
        text = text.replace(marker, finding_note + marker)
    readme_path.write_text(text, encoding="utf-8")


def main() -> None:
    route_withdrawn()
    for day in range(8, 16):
        audit_day(day)
    print(json.dumps({"days": 8, "false_negative_findings": sum(map(len, FINDINGS.values()))}))


if __name__ == "__main__":
    main()
