#!/usr/bin/env python3
"""Resolve the 2026-06-03 UltraEP abstract-level exact-v1 blocker."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"


def load(name: str) -> dict:
    return json.loads((PACKET / name).read_text())


def dump(name: str, payload: dict) -> None:
    (PACKET / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    evidence = load("evidence-review-v9-strict.json")
    review = next(row for row in evidence["reviews"] if row["source_family_id"] == "SF-ULTRAEP")
    method = (
        "UltraEP reacts to post-gating exact expert load on every microbatch and layer, uses quota-driven "
        "planning for temporary replication, and transfers irregular expert state through rack-scale persistent "
        "tile streaming with relay-based fan-out mitigation. Router semantics remain unchanged; the planner owns "
        "execution placement and replication state."
    )
    evaluation = (
        "The official v1 abstract reports MoE training and serving prefill across 106B–671B models: average "
        "throughput is 94.3% of the force-balanced ideal and 1.49× the no-balancing baseline, final inter-rank "
        "imbalance falls from 1.30–4.01 to 1.01–1.04, and production training scalability/robustness is reported "
        "at 2560 GPUs."
    )
    boundary = (
        "The accessible exact-v1 material is the official abstract, not the removed PDF/HTML body. It covers "
        "rack-scale MoE training and serving prefill for 106B–671B models, but does not disclose a dedicated "
        "limitations section, GPU model, topology dimensions, precision, batch size, failure recovery, "
        "optimizer/gradient correctness, decode behavior or a production latency SLO. Later v3 and the July "
        "repository are excluded."
    )
    review.update({
        "method_locator": "https://arxiv.org/abs/2606.04101v1 — Abstract ¶2–3; exact-load planning and expert-state transfer",
        "method_evidence": method,
        "evaluation_locator": "https://arxiv.org/abs/2606.04101v1 — Abstract ¶4–5; 106B–671B training/prefill and 2560-GPU validation",
        "evaluation_evidence": evaluation,
        "limitations_locator": "https://arxiv.org/abs/2606.04101v1 — Abstract scope; submission-history removal boundary",
        "limitations_evidence": boundary,
        "artifact_locator": "Not Disclosed — exact-v1 official abstract names no event-time artifact; later GitHub repository excluded",
        "body_sha256": hashlib.sha256((method + "\n" + evaluation + "\n" + boundary).encode()).hexdigest(),
        "body_digest_status": "official_exact_v1_abstract_recovery",
        "material_route": "papers/2026/06/_sources/daily-20260603/ULTRAEP_EXACT_V1_ABS_RECOVERY.md",
        "stable_node_id": "MODEL-MOE",
        "score_v2": {"design_delta": 3, "system_reach": 3, "durability": 2, "total": 8},
        "benchmark_contract": {
            "input": "MoE training and serving prefill; exact post-gating load rebalanced every microbatch and layer",
            "model": "MoE models from 106B to 671B parameters",
            "hardware": "Rack-scale nodes; production training validation with 2560 GPUs; GPU model Not Disclosed",
            "precision": "Not Disclosed",
            "batch": "Per-microbatch planning; numeric microbatch size Not Disclosed",
            "concurrency": "Not Disclosed",
            "slo": "Not Disclosed",
            "evaluator": "Force-balanced ideal throughput ratio; throughput versus no balancing; final inter-rank imbalance",
        },
        "claim_boundary": boundary,
        "review_status": "deep_complete",
        "access_status": "accessible",
        "materials_request": "—",
        "v9_reconciliation": "official_exact_v1_abstract_recovered; later evidence excluded",
    })
    evidence["blocked"] = []
    evidence["blocked_count"] = 0
    dump("evidence-review-v9-strict.json", evidence)

    selection = load("deep-analysis-selection-v9-strict.json")
    selected = next(row for row in selection["rows"] if row["source_family_id"] == "SF-ULTRAEP")
    selected.update({
        "eligible": True,
        "selection": "not_selected",
        "selection_basis": (
            "Official exact-v1 abstract evidence is complete at its disclosed boundary. Across the full 55-family "
            "frontier, UltraEP adds no stronger non-overlapping Daily narrative than Libra, Agent libOS and "
            "LazyAttention; its dynamic EP mechanism is already represented in the current Books tree."
        ),
    })
    selection["frontier_size"] = 55
    dump("deep-analysis-selection-v9-strict.json", selection)

    chronology = load("selection-chronology-v5.json")
    chronology_rows = chronology.get("rows") or chronology.get("items")
    if not isinstance(chronology_rows, list):
        raise ValueError("selection chronology must contain a rows/items list")
    item = next(row for row in chronology_rows if row["source_family_id"] == "SF-ULTRAEP")
    item.update({
        "score_v2_replay_ref": "official-abs:arXiv:2606.04101v1",
        "decision": "not_selected",
        "priority_rationale": selected["selection_basis"],
    })
    dump("selection-chronology-v5.json", chronology)

    books = load("books-comparison-v9-strict.json")
    comparison = next(row for row in books["rows"] if row["source_family_id"] == "SF-ULTRAEP")
    comparison.update({
        "stable_node_id": "MODEL-MOE",
        "candidate_owner_matches": True,
        "target_chapter_ref": "books/part-02-model/21-moe.md#L1",
        "adjacent_chapter_refs": "books/part-04-training-system/36-distributed-training.md#L441; books/part-05-inference-system/56-inference-scheduling.md#L744",
        "source_delta": method,
        "evidence_boundary": boundary,
        "evolution_relation": "Layering / Dependency",
        "provisional_disposition": "No Change — Existing Coverage",
        "disposition_basis": (
            "Ch36 already owns dynamic token+weight spill after per-expert load collection, native weight/optimizer "
            "authority, topology cost and static-EP fallback; Ch21 and Ch56 retain model-routing and serving handoffs."
        ),
        "books_write_performed": False,
        "v9_reconciliation": "fresh_books_dedup_no_write_after_official_v1_abstract_recovery",
    })
    books["queue_release_blockers"] = []
    dump("books-comparison-v9-strict.json", books)


if __name__ == "__main__":
    main()
