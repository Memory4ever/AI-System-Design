#!/usr/bin/env python3
"""Reconcile 2026-05-12 evidence against current Books without writing Books."""

from __future__ import annotations

import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[5]
ROOT = Path(__file__).resolve().parent

INTEGRATE = {
    "2605.09992", "2605.09994", "2605.10075", "2605.10094", "2605.10124", "2605.10199",
    "2605.10246", "2605.10347", "2605.10366", "2605.10426", "2605.10448", "2605.10501",
    "2605.10516", "2605.10555", "2605.10556", "2605.10575", "2605.10614", "2605.10670",
    "2605.10779", "2605.10819", "2605.10832", "2605.10875", "2605.10912", "2605.10913",
    "2605.10923", "2605.10933", "2605.11039", "2605.11047", "2605.11053", "2605.11086",
    "2605.11093", "2605.11186", "2605.11202", "2605.11209", "2605.11212", "2605.11215",
    "2605.11229", "2605.11234", "2605.11277", "2605.11325", "2605.11330", "2605.11333",
    "2605.11360", "2605.11367", "2605.13880", "2605.18803", "2605.23956",
}

NO_CHANGE = {
    "2605.09863", "2605.09877", "2605.09886", "2605.09889", "2605.09934", "2605.10012",
    "2605.10057", "2605.10223", "2605.10351", "2605.10380", "2605.10405", "2605.10481",
    "2605.10763", "2605.10787", "2605.10805", "2605.10834", "2605.10850", "2605.10870",
    "2605.10901", "2605.10905", "2605.11182", "2605.11205", "2605.11317", "2605.11328",
    "2605.11334", "2605.11335", "2605.18792", "2605.18796",
}

NO_CHANGE_REASON = {
    "2605.09863": "AGENT-MEMORY already separates mutable persona/profile state from task evidence and requires drift detection plus rollback; the paper supplies one black-box detector, not a new memory owner or commit rule.",
    "2605.09877": "MODEL-LONG-CONTEXT already treats recurrent/compressed memory as an alternative branch that trades raw-history access for bounded state; KVM is a bounded architecture instance rather than a new lifecycle contract.",
    "2605.09886": "MULTIMODAL-WORLD-MODELS already owns compressed latent/world-state transport and synchronization boundaries; the vehicular token stream changes one codec/workload, not the logical state contract.",
    "2605.09889": "AGENT-PLATFORM and PLATFORM-SECURITY already require independently verified skill identity, capability and provenance before routing; description deception is a threat instance of that existing admission rule.",
    "2605.09934": "AGENT-TOOL-CALLING already makes evidence identity and claim-to-observation provenance part of tool-result commit; TRACER supplies a multimodal benchmark/implementation but no new ownership boundary.",
    "2605.10012": "PLATFORM-SECURITY already separates human intent capture from executable policy, validation and enforcement; sketch input is an interface branch, not a new authority model.",
    "2605.10057": "AGENT-MULTI-AGENT already assigns failure receipt, retry reachability and routing state to the orchestrator; STAR is a learned routing realization under a specific task taxonomy.",
    "2605.10223": "AGENT-PLATFORM already uses risk/cost/authority tiers with explicit admission and escalation; AgentRunner is one enterprise realization rather than a new platform contract.",
    "2605.10351": "The reliable-inference monograph synthesizes mechanisms already owned across Sampling, Evaluation, Scheduling and Security; it does not provide a single new empirical or state-ownership delta.",
    "2605.10380": "INFER-SPECULATIVE-DECODING already owns draft/proposal state, prefix reuse and target-only commit; Agent-X combines those known branches for an on-device pipeline.",
    "2605.10405": "PLATFORM-EVALUATION-SYSTEM already requires uncertainty-aware sample allocation and valid best-model selection under evaluator assumptions; low-rank factorization is an estimator branch within that contract.",
    "2605.10481": "PLATFORM-SECURITY and AGENT-MULTI-AGENT already require constraints to remain versioned execution state across delegation, tool calls and audit; this position paper names that known preservation failure without a new validated mechanism.",
    "2605.10763": "PLATFORM-SECURITY already models agent attack surface across prompt, memory, tool, network and privilege boundaries; MATRA's OpenClaw case study does not change the owner or enforcement sequence.",
    "2605.10787": "AGENT-MCP and Evaluation already require stateful, interdependent tool sandboxes and deterministic outcome checks; ComplexMCP adds a benchmark instance, not a new long-term control contract.",
    "2605.10805": "PLATFORM-EVALUATION-SYSTEM already routes evaluation work by calibrated quality/cost and keeps expensive judges behind uncertainty gates; RACER is a bounded router implementation.",
    "2605.10834": "PLATFORM-EVALUATION-SYSTEM already binds security-agent scores to executable environment, attempt budget, verifier and side effects; the wild-pentesting protocol refines a benchmark slice without changing that contract.",
    "2605.10850": "PLATFORM-EVALUATION-SYSTEM and Sampling already reject self-agreement as calibrated truth because verifier errors are correlated; VeriMap supplies medical-VQA evidence for the existing boundary.",
    "2605.10870": "AGENT-MEMORY already treats memory as decision-preserving derived state with explicit budget, forgetting and fallback; the rate-distortion formalization strengthens explanation but not the lifecycle owner.",
    "2605.10901": "PLATFORM-SECURITY already treats guardrail guarantees as conditional on threat model, coverage assumptions and abstention; the formal classifier guarantee is an alternative proof branch.",
    "2605.10905": "INFER-TENSORRT-LLM already owns hardware-specific lowering, autotuning, versioned execution plans and fallback; TLX is a production compiler instance of that evolution.",
    "2605.11182": "TRAIN-RLHF already distinguishes on-policy sampling, teacher/student distribution shift and KL objective variants; the paper's fixes remain within that established distillation branch.",
    "2605.11205": "PLATFORM-EVALUATION-SYSTEM already rejects unweighted mean scores under heterogeneous difficulty and sparse slices; 2PL IRT is a known estimator alternative, not a new release contract.",
    "2605.11317": "INFER-REQUEST-LIFECYCLE already owns request-level local/remote admission, escalation and rollback; SOMA is a soft-prompt surrogate realization under one dialogue distribution.",
    "2605.11328": "TRAIN-RLHF already uses epistemic uncertainty to allocate exploration/oracle budget and treats adapter ensembles as sensors requiring calibration; this paper is a bounded test-time variant.",
    "2605.11334": "PLATFORM-EVALUATION-SYSTEM already decomposes judge evidence into claim/rubric signals, calibrates selective risk and allows abstention; VERDI supplies one single-call estimator without changing the decision contract.",
    "2605.11335": "INFER-GPU-MEMORY already owns layerwise offload, transfer/compute overlap and topology-aware prefetch; ChunkFlow is one DiT/PCIe scheduling policy within that branch.",
    "2605.18792": "AGENT-RAG already separates parametric belief, retrieved evidence, conflict handling and abstention; SABER provides one representation/probe for the existing trust-or-retrieve decision.",
    "2605.18796": "INFER-SCHEDULING already uses calibrated correctness/cost to commit, defer or escalate across model cascades; UCCI is a bounded uncertainty estimator and threshold solver.",
}


def roadmap_nodes() -> tuple[dict[str, tuple[int, str]], dict[int, str]]:
    nodes: dict[str, tuple[int, str]] = {}
    chapters: dict[int, str] = {}
    pattern = re.compile(r"^\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \|")
    for line in (REPO / "ROADMAP.md").read_text().splitlines():
        match = pattern.match(line)
        if not match:
            continue
        node, chapter, path = match.group(1), int(match.group(2)), match.group(3)
        nodes[node] = (chapter, path)
        chapters[chapter] = path
    return nodes, chapters


def body_outline(path: Path) -> str:
    text = path.read_text()
    text = text.split("## Review notes", 1)[0]
    heads = [line.strip() for line in text.splitlines() if line.startswith("## ") or line.startswith("### ")]
    return " → ".join(heads[:14])


def main() -> None:
    ledger = json.loads((ROOT / "screening-ledger-independent-reconciled.json").read_text())
    packet = {x["arxiv_id"]: x for x in json.loads((ROOT / "exact-v1-review-packet-independent.json").read_text())}
    author_compare = {x["arxiv_id"]: x for x in json.loads((ROOT / "books-current-content-comparison.json").read_text())}
    nodes, chapters = roadmap_nodes()

    retained = [r for r in ledger["identities"] if r.get("screening_status") == "retained"]
    expected = {r["arxiv_id"] for r in retained} - {"2605.10133"}
    assert INTEGRATE | NO_CHANGE == expected
    assert not (INTEGRATE & NO_CHANGE)

    comparisons = []
    queue = []
    for row in retained:
        aid = row["arxiv_id"]
        review = packet[aid]
        owner = row.get("stable_node_id") or author_compare.get(aid, {}).get("owner_node")
        if aid == "2605.10380":
            owner = "INFER-SPECULATIVE-DECODING"
        if aid == "2605.11317":
            owner = "INFER-REQUEST-LIFECYCLE"
        if aid == "2605.10133":
            comparisons.append({
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "owner_node": owner,
                "decision": "Blocked / Unverified",
                "reason": review["claim_nonproof_boundary"],
                "books_review_ref": f"BOOKS-REVIEW-20260512-{aid.replace('.', '-')}",
            })
            row["integration_disposition"] = "Blocked / Unverified"
            continue
        assert owner in nodes, (aid, owner)
        chapter, owner_path = nodes[owner]
        adjacent = [chapters[n] for n in (chapter - 1, chapter + 1) if n in chapters]
        owner_outline = body_outline(REPO / owner_path)
        adjacent_outlines = {p: body_outline(REPO / p) for p in adjacent}
        if aid in NO_CHANGE:
            decision = "No Change — Existing Coverage"
            reason = NO_CHANGE_REASON[aid]
        else:
            decision = "Integrate"
            delta = row.get("screening_reason") or review["method_identity_locators"].split(" — ", 1)[-1]
            reason = (
                f"Current {owner} outline establishes the surrounding owner and fallback but does not make this exact mechanism explicit: {delta}. "
                f"Integrate only the long-lived state/control/evidence delta; retain the source's non-proof boundary from {review['review_provenance_id']}."
            )
        item = {
            "arxiv_id": aid,
            "source_family_id": row["source_family_id"],
            "owner_node": owner,
            "owner_path": owner_path,
            "adjacent_paths": adjacent,
            "owner_body_outline_before_review_notes": owner_outline,
            "adjacent_body_outlines_before_review_notes": adjacent_outlines,
            "review_provenance_id": review["review_provenance_id"],
            "decision": decision,
            "reason": reason,
            "books_review_ref": f"BOOKS-REVIEW-20260512-{aid.replace('.', '-')}",
        }
        comparisons.append(item)
        row["stable_node_id"] = owner
        row["integration_disposition"] = decision
        row["books_review_ref"] = item["books_review_ref"]
        if decision == "Integrate":
            queue.append({
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "stable_node_id": owner,
                "owner_path": owner_path,
                "adjacent_paths": adjacent,
                "review_provenance_id": review["review_provenance_id"],
                "books_review_ref": item["books_review_ref"],
                "integration_delta": reason,
                "nonproof_boundary": review["claim_nonproof_boundary"],
                "writeback_state": "awaiting_root_serial_writeback",
            })

    (ROOT / "books-current-content-comparison-independent.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "books-writeback-queue-independent-reconciled.json").write_text(json.dumps({
        "schema": "books-writeback-queue-v2.1-independent-reconciled",
        "report_date": "2026-05-12",
        "status": "ready_for_root_serial_writeback",
        "counts": {
            "retained": len(retained),
            "integrate": len(queue),
            "no_change": len(NO_CHANGE),
            "blocked": 1,
            "ordinary_pending": 0,
        },
        "items": queue,
        "blocked": ["SF-2026-ARXIV-2605-10133"],
    }, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "screening-ledger-independent-reconciled.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

    audit_path = ROOT / "independent-semantic-audit.json"
    audit = json.loads(audit_path.read_text())
    audit["books_prewrite_receipt"] = {
        "comparison": "books-current-content-comparison-independent.json",
        "queue": "books-writeback-queue-independent-reconciled.json",
        "current_owner_adjacent_review": f"76/76 (47 Integrate; {len(NO_CHANGE)} No Change; 1 Blocked)",
        "shared_books_written": False,
    }
    audit["gate"]["books"] = "Open — 47-item reconciled queue is ready, but root serial Books writeback and non-writer post-write audit have not occurred."
    audit["gate"]["completion"] = "In Progress — root Books writeback/post-write audit pending; 1 exact-v1 external blocker remains Conditional."
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
