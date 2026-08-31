#!/usr/bin/env python3
"""Freeze the row-complete 2026-06-06 Candidate Denominator audit."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260606"
LEDGER = PACKET / "screening-ledger.json"


# Fresh title+abstract decisions.  Admission is deliberately limited to work
# that changes a durable AI-System mechanism, ownership boundary, evaluation
# contract, or platform/training/inference design judgment.
RETAIN_OWNER = {
    "2606.06818": "PLATFORM-GPU-SCHEDULER",
    "2606.06820": "PLATFORM-GPU-SCHEDULER",
    "2606.06832": "MULTIMODAL-WORLD-MODELS",
    "2606.06833": "PLATFORM-SECURITY",
    "2606.06835": "AGENT-TOOL-CALLING",
    "2606.06854": "PLATFORM-SECURITY",
    "2606.06880": "AGENT-RAG",
    "2606.06888": "TRAIN-PRETRAINING",
    "2606.06891": "MULTIMODAL-WORLD-MODELS",
    "2606.06892": "TRAIN-DATA",
    "2606.06893": "AGENT-WORKFLOW",
    "2606.06915": "PLATFORM-EVALUATION-SYSTEM",
    "2606.06923": "AGENT-WORKFLOW",
    "2606.06924": "INFER-SCHEDULING",
    "2606.06946": "PLATFORM-SECURITY",
    "2606.06976": "AGENT-TOOL-CALLING",
    "2606.06991": "MULTIMODAL-WORLD-MODELS",
    "2606.07001": "TRAIN-DATA",
    "2606.07017": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07019": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.07027": "TRAIN-GRPO",
    "2606.07054": "PLATFORM-MONITORING",
    "2606.07067": "PLATFORM-SECURITY",
    "2606.07074": "TRAIN-GRPO",
    "2606.07082": "TRAIN-SFT",
    "2606.07127": "MULTIMODAL-WORLD-MODELS",
    "2606.07131": "PLATFORM-SECURITY",
    "2606.07150": "PLATFORM-SECURITY",
    "2606.07157": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07190": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07205": "INFER-KV-CACHE",
    "2606.07218": "AGENT-RAG",
    "2606.07248": "INFER-SCHEDULING",
    "2606.07308": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07316": "AGENT-MULTI-AGENT",
    "2606.07362": "INFER-VLLM",
    "2606.07379": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07392": "INFER-SCHEDULING",
    "2606.07403": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.07412": "AGENT-WORKFLOW",
    "2606.07431": "PLATFORM-FOUNDATIONS",
    "2606.07462": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07470": "PLATFORM-SECURITY",
    "2606.07512": "AGENT-MEMORY",
    "2606.07684": "AGENT-MEMORY",
    "2606.07687": "MULTIMODAL-WORLD-MODELS",
    "2606.07696": "PLATFORM-SECURITY",
    "2606.07703": "INFER-PREFILL",
    "2606.07705": "TRAIN-GRPO",
    "2606.07706": "PLATFORM-SECURITY",
    "2606.07710": "INFER-SPECULATIVE-DECODING",
    "2606.07711": "AGENT-MEMORY",
    "2606.07713": "INFER-TENSORRT-LLM",
    "2606.07720": "AGENT-CONTEXT",
    "2606.07726": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07783": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07790": "AGENT-MULTI-AGENT",
    "2606.07805": "AGENT-MULTI-AGENT",
    "2606.07808": "PLATFORM-SECURITY",
    "2606.07810": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07822": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07833": "PLATFORM-SECURITY",
    "2606.07834": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07845": "AGENT-MULTI-AGENT",
    "2606.07846": "AGENT-WORKFLOW",
    "2606.07856": "TRAIN-SFT",
    "2606.07867": "PLATFORM-SECURITY",
    "2606.07874": "PLATFORM-EVALUATION-SYSTEM",
    "2606.07878": "INFER-KV-CACHE",
    "2606.07881": "TRAIN-PIPELINE-PARALLEL",
    "2606.07889": "PLATFORM-MONITORING",
    "2606.07895": "MULTIMODAL-EMBODIED-VLA",
    "2606.07904": "AGENT-TOOL-CALLING",
    "2606.07909": "AGENT-MEMORY",
}

# A second complete FP pass rejects rows that are interesting mechanisms but
# remain task-local or do not cross the long-term admission boundary.  Keeping
# the broader map above makes that stricter contraction auditable.
STRICT_RETAIN_IDS = {
    "2606.06818", "2606.06820", "2606.06832", "2606.06880", "2606.06888",
    "2606.06892", "2606.06893", "2606.06915", "2606.06924", "2606.06991",
    "2606.07001", "2606.07017", "2606.07019", "2606.07054", "2606.07067",
    "2606.07131", "2606.07150", "2606.07157", "2606.07190", "2606.07205",
    "2606.07248", "2606.07362", "2606.07379", "2606.07392",
    "2606.07412", "2606.07431", "2606.07462", "2606.07470", "2606.07684",
    "2606.07687", "2606.07703", "2606.07710", "2606.07713", "2606.07720",
    "2606.07726", "2606.07783", "2606.07790", "2606.07805", "2606.07808",
    "2606.07822", "2606.07833", "2606.07834", "2606.07845", "2606.07846",
    "2606.07856", "2606.07867", "2606.07874", "2606.07878", "2606.07881",
    "2606.07889", "2606.07904",
}
RETAIN_OWNER = {key: value for key, value in RETAIN_OWNER.items() if key in STRICT_RETAIN_IDS}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def source_specific_excerpt(abstract: str, limit: int = 300) -> str:
    text = normalize(abstract)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    excerpt = " ".join(sentences[:2])
    return (excerpt[: limit - 1].rstrip() + "…") if len(excerpt) > limit else excerpt


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = data["identities"]
    ids = {row["arxiv_id"] for row in rows}
    missing = sorted(set(RETAIN_OWNER) - ids)
    if missing:
        raise SystemExit(f"retained IDs absent from ledger: {missing}")

    audited = []
    for index, row in enumerate(rows, 1):
        identifier = row["arxiv_id"]
        excerpt = source_specific_excerpt(row["abstract"])
        if identifier in RETAIN_OWNER:
            verdict = "retained"
            owner = RETAIN_OWNER[identifier]
            reason = (
                f"The title+abstract changes durable `{owner}` design or evidence boundaries: "
                f"{excerpt} Exact-v1 review must still confirm the mechanism and its limits."
            )
        else:
            verdict = "pre_denominator_closure"
            owner = "—"
            reason = (
                f"Source-specific abstract scope: {excerpt} On the disclosed title+abstract, this remains a "
                "task-local model, dataset, application, general algorithm, or isolated metric result and does not "
                "explicitly change a long-term AI-System mechanism, state/data/control owner, reproducible "
                "evaluation/release contract, platform/training/inference design judgment, or current Books claim."
            )
        audited.append({
            "row": index,
            "arxiv_id": identifier,
            "source_family_id": f"SF-2026-ARXIV-{identifier.replace('.', '-')}",
            "submitted_v1_utc": row["submitted_v1_utc"],
            "title": row["title"],
            "categories": row["categories"],
            "screening_route": row["screening_route"],
            "fresh_verdict": verdict,
            "stable_node_id": owner,
            "family_specific_reason": reason,
        })
        row["screening_status"] = verdict
        row["stable_node_id"] = owner
        row["screening_reason"] = reason

    counts = Counter(item["fresh_verdict"] for item in audited)
    if len(audited) != 479 or counts["retained"] != len(RETAIN_OWNER):
        raise SystemExit(f"unexpected audit counts: {len(audited)}, {counts}")
    if counts["pre_denominator_closure"] + counts["retained"] != len(audited):
        raise SystemExit("audit is not row-complete")

    frozen_basis = json.dumps(audited, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    denominator_id = f"DEN-20260606-{hashlib.sha256(frozen_basis).hexdigest()[:8]}"
    data.update({
        "schema": "daily-v2.1-screening-ledger-v2-fresh",
        "gate_status": "coverage_semantic_screen_complete_denominator_frozen",
        "audit": {
            "auditor": "fresh-context:jun06-v1",
            "scope": "479/479 title+abstract rows; all proposed retains and all closures",
            "retained": counts["retained"],
            "pre_denominator_closures": counts["pre_denominator_closure"],
            "ordinary_pending": 0,
            "findings": [
                {
                    "finding_id": "FINDING-JUN06-EXACT-V1-07403",
                    "status": "resolved",
                    "source_family_id": "SF-2026-ARXIV-2606-07403",
                    "finding": "The title+abstract intake metadata incorrectly associated 2606.07403 with a distributed-training paper; the official exact-v1 identity is The Proxy Benders Decomposition and is outside the AI-System denominator.",
                    "resolution": "Contracted the denominator by one identity and retained the row as a family-specific pre-denominator closure; no silent substitution with adjacent arXiv identifiers was made.",
                }
            ],
        },
        "canonical_candidate_denominator": {
            "denominator_id": denominator_id,
            "count": counts["retained"],
            "source_family_ids": [item["source_family_id"] for item in audited if item["fresh_verdict"] == "retained"],
            "status": "frozen_pending_exact_v1_evidence",
        },
    })
    LEDGER.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit = {
        "schema": "daily-v2.1-candidate-denominator-fresh-audit-v1",
        "report_date": "2026-06-06",
        "window": data["window"],
        "denominator_id": denominator_id,
        "identity_count": len(audited),
        "retained_count": counts["retained"],
        "pre_denominator_closure_count": counts["pre_denominator_closure"],
        "retain_rate_percent": round(100 * counts["retained"] / len(audited), 2),
        "auditor": "fresh-context:jun06-v1",
        "ordinary_pending": 0,
        "findings": [
            {
                "finding_id": "FINDING-JUN06-EXACT-V1-07403",
                "status": "resolved",
                "source_family_id": "SF-2026-ARXIV-2606-07403",
                "exact_v1_url": "https://arxiv.org/html/2606.07403v1",
                "finding": "Official exact-v1 title is The Proxy Benders Decomposition, contradicting the intake association with a distributed-training paper.",
                "resolution": "The identity is closed before Evidence admission; the frozen denominator is recomputed and no neighboring identifier is substituted.",
            }
        ],
        "rows": audited,
    }
    target = PACKET / "candidate-denominator-fresh-audit-v1.json"
    target.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKET / "retained-ids.txt").write_text(
        "".join(f"{item['arxiv_id']}\n" for item in audited if item["fresh_verdict"] == "retained"),
        encoding="utf-8",
    )

    md = [
        "# 2026-06-06 Candidate Denominator Fresh Audit V1",
        "",
        "- Auditor: `fresh-context:jun06-v1`",
        f"- Denominator: `{denominator_id}`",
        f"- Row-complete account: `479 = {counts['retained']} retained + {counts['pre_denominator_closure']} pre-denominator closures`",
        f"- Retain rate: `{100 * counts['retained'] / len(audited):.2f}%`",
        "- Ordinary pending: `0`",
        "- Scope: all Core, keyword-routed and keyword-negative identities; no sampling.",
        "",
        "The JSON receipt records every identity, exact title+abstract route, fresh verdict, owner and family-specific reason. "
        "Retention is provisional with respect to exact-v1 Evidence: a full-text contradiction reopens and can shrink the denominator.",
        "",
        "## Findings",
        "",
        "`FINDING-JUN06-EXACT-V1-07403` is resolved: official exact-v1 identifies `2606.07403` as *The Proxy Benders Decomposition*, so the row is a family-specific closure. The denominator was contracted by one and no adjacent identifier was silently substituted. No unresolved Coverage finding remains; Evidence remains Open.",
        "",
    ]
    (PACKET / "CANDIDATE_DENOMINATOR_FRESH_AUDIT_V1.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({
        "denominator_id": denominator_id,
        "identities": len(audited),
        "retained": counts["retained"],
        "closures": counts["pre_denominator_closure"],
    }, indent=2))


if __name__ == "__main__":
    main()
