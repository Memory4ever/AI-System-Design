#!/usr/bin/env python3
"""Materialize the author-side denominator recalibration for 2026-06-05 batches 01-02.

This script deliberately does not mutate the screening ledger.  The legacy 442-family
denominator stays available as evidence, but is invalidated by the accompanying receipt
until all 624 identities have been re-adjudicated and a fresh-context audit passes.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260605"
LEDGER = PACKET / "screening-ledger.json"
OUTPUT = PACKET / "denominator-recalibration-batch01-02-author-v1.md"
FULL_OUTPUT = PACKET / "denominator-recalibration-full-author-v1.md"


# Deliberately small: each retained family must change a durable AI-system mechanism,
# ownership boundary, evaluation contract, or an existing Books design conclusion.
KEEP = {
    "2606.05548",  # framework evaluation contract
    "2606.05551",  # action-conditional guarantee
    "2606.05558",  # agent OPE / world-model boundary
    "2606.05559",  # continual-learning service state and async updates
    "2606.05568",  # retrieval index/storage/decompression dataflow
    "2606.05597",  # asynchronous rollout/update/refresh control
    "2606.05610",  # continued-pretraining hyperparameter scaling
    "2606.05636",  # mechanism-level RCA evidence ownership
    "2606.05644",  # RAG evidence-vs-memory conflict control
    "2606.05645",  # shared discrete world/policy state
    "2606.05679",  # effect-time data-flow enforcement
    "2606.05688",  # MoE quantization must preserve routing identity
    "2606.05703",  # parallel proposal/correction schedule for AR image generation
    "2606.05725",  # cross-request model-extraction security state
    "2606.05742",  # adaptive draft reuse and speculative acceptance control
    "2606.05773",  # policy-in-the-loop world-model evaluation
    "2606.05784",  # tool-step credit assignment in post-training
    "2606.05800",  # group-RL rollout geometry and cancellation
    "2606.05805",  # guardrail decision -> executable remediation interface
    "2606.05806",  # tool failure/replanning evaluation contract
    "2606.05868",  # GQA-to-MLA changes KV-state layout
    "2606.05875",  # query-aware compressed RAG cache state
    "2606.05894",  # budgeted evidence-retention memory
    "2606.05933",  # SLO-aware inference chunk scheduling
    "2606.05951",  # NVSHMEM communication semantics
    "2606.05958",  # activation-steering artifact supply-chain attack
    "2606.06036",  # graph memory reconstruction semantics
    "2606.06054",  # authority/recency/user-control memory search
    "2606.06055",  # sensitive-history memory-use warrant
    "2606.06060",  # learned diffusion caching schedule
    "2606.06090",  # memory as workflow execution state
    "2606.06223",  # contextual mechanistic agent-risk sensor
    "2606.06240",  # bitemporal contradiction semantics
    "2606.06256",  # head-aware KV reuse and segmented paging
    "2606.06284",  # causal minimal tool frontier
    "2606.06302",  # non-uniform KV compression system
    "2606.06324",  # agent harness diagnosis and repair
    "2606.06333",  # subspace-aware mechanistic representation
    "2606.06356",  # layered knowledge-infusion ownership
    "2606.06387",  # MCP tool-surface poisoning
    "2606.06448",  # stateful long-horizon workload characterization
    "2606.06453",  # programmable sparse-attention serving
    "2606.06460",  # in-band recusal and mid-flight stop semantics
    "2606.06467",  # shared sparse-attention routing/index state
    "2606.06574",  # dynamic program-of-layers execution
    "2606.06697",  # protected GPU OS layer
    "2606.06708",  # signal-driven observation for web agents
    "2606.06712",  # on-policy AR-to-diffusion conversion
    "2606.06747",  # property-based testing for AI compilers
    "2606.06751",  # synchronization-aware distributed-training accounting
    "2606.06758",  # evidence utilization under matched conditions
    "2606.06767",  # custody/provenance admission envelope
}


def closure_reason(entry: dict) -> str:
    """Preserve the family-specific observation while explaining why it is not a candidate."""
    title = entry["title"]
    old = entry["screening_reason"].rstrip("。")
    abstract = entry.get("abstract", "").lower()

    if any(word in title.lower() for word in ("benchmark", "evaluation", "evaluating", "auditing")):
        boundary = "它主要新增单一任务或单一领域的 benchmark / measurement slice，未改变本书已有 evaluation contract 的责任边界"
    elif any(word in abstract for word in ("medical", "clinical", "pharmac", "speech recognition", "autonomous driving", "robot", "financial")):
        boundary = "它证明的是受领域、数据集或设备约束的局部结果，尚不能外推为通用 AI System 机制"
    elif any(word in title.lower() for word in ("survey", "analysis", "when ai says", "paradigm")):
        boundary = "它提供观点、综述或背景信号，但没有足够 primary mechanism / artifact 证据改变长期 owner"
    else:
        boundary = "它展示的是模型、表示、任务或局部实现增量，尚未改变 durable state/data/control ownership、平台合同或 Books 既有设计结论"

    return f"原语义观察“{old}”仍保留；但{boundary}，因此转为 pre-denominator closure（{title}）。"


def main() -> None:
    data = json.loads(LEDGER.read_text())
    identities = data["identities"][:160]
    old_candidates = [x for x in identities if x.get("screening_status") == "routed_candidate"]
    old_closures = [x for x in identities if x.get("screening_status") != "routed_candidate"]
    retained = [x for x in old_candidates if x["arxiv_id"] in KEEP]
    downgraded = [x for x in old_candidates if x["arxiv_id"] not in KEEP]

    first_scope_ids = {x["arxiv_id"] for x in identities}
    missing = (KEEP & first_scope_ids) - {x["arxiv_id"] for x in old_candidates}
    if missing:
        raise SystemExit(f"KEEP IDs not present in legacy candidate set: {sorted(missing)}")

    lines = [
        "# 2026-06-05 Candidate Denominator Recalibration — Batches 01–02 (Author V1)",
        "",
        "> Scope: frozen identity order `1–160 / 624`. This is an author-side false-positive repair,",
        "> not the fresh-context acceptance audit and not a new frozen denominator. The legacy",
        "> `442`-family denominator is invalid for downstream Gate claims until all `624` identities",
        "> are re-adjudicated and false-positive / false-negative review passes.",
        "",
        "## Contract correction",
        "",
        "Full semantic screening of Core Daily categories establishes Coverage recall. It does not",
        "make every AI-related paper a candidate. A family is retained only when its title/abstract",
        "evidence plausibly changes a durable AI System mechanism, state/data/control ownership,",
        "evaluation contract, platform/training/inference design judgment, or an existing Books claim.",
        "ROADMAP mappability, a local model improvement, or a domain benchmark alone is insufficient.",
        "",
        "## Reconciliation receipt",
        "",
        f"- Raw identities reviewed in this scope: `160/624`.",
        f"- Legacy retained in this scope: `{len(old_candidates)}/160` (`{len(old_candidates)/160:.1%}`).",
        f"- Recalibrated retained in this scope: `{len(retained)}/160` (`{len(retained)/160:.1%}`).",
        f"- Legacy pre-denominator closures preserved: `{len(old_closures)}`.",
        f"- Newly downgraded to pre-denominator closure: `{len(downgraded)}`.",
        f"- Net change in this scope: `-{len(downgraded)}` retained families.",
        "- Coverage Gate: `Open` — remaining `464` identities need the same adjudication.",
        "- Evidence / Selection / Books Gates: `Open` — the denominator is not refrozen.",
        "- Books writeback: `Not started`; existing source-review files are preserved as reusable evidence.",
        "",
        "## Retained after recalibration",
        "",
        "| # | arXiv | Title | Why it still crosses the denominator boundary |",
        "| ---: | --- | --- | --- |",
    ]
    for idx, entry in enumerate(identities, 1):
        if entry in retained:
            lines.append(
                f"| {idx} | `{entry['arxiv_id']}` | {entry['title']} | "
                f"{entry['screening_reason']} This changes a durable contract or ownership boundary, rather than merely mapping to a ROADMAP node. |"
            )

    lines += [
        "",
        "## Newly downgraded pre-denominator closures",
        "",
        "| # | arXiv | Family-specific closure reason |",
        "| ---: | --- | --- |",
    ]
    for idx, entry in enumerate(identities, 1):
        if entry in downgraded:
            lines.append(f"| {idx} | `{entry['arxiv_id']}` | {closure_reason(entry)} |")

    lines += [
        "",
        "## Evidence preservation and next checkpoint",
        "",
        "The earlier exact-v1 reviews and scores are not deleted. For downgraded families they become",
        "supporting closure evidence, not current candidate Reviews. The next author checkpoint must",
        "apply the same boundary to identities `161–624`, then rebuild Score V2 and Source Review only",
        "for the newly frozen candidate set. A different-context reviewer must try to disprove both",
        "retained and closure decisions before any Gate can pass.",
        "",
    ]
    OUTPUT.write_text("\n".join(lines))

    all_identities = data["identities"]
    all_old_candidates = [x for x in all_identities if x.get("screening_status") == "routed_candidate"]
    all_old_closures = [x for x in all_identities if x.get("screening_status") != "routed_candidate"]
    all_retained = [x for x in all_old_candidates if x["arxiv_id"] in KEEP]
    all_downgraded = [x for x in all_old_candidates if x["arxiv_id"] not in KEEP]
    full_missing = KEEP - {x["arxiv_id"] for x in all_old_candidates}
    if full_missing:
        raise SystemExit(f"KEEP IDs not present in full legacy candidate set: {sorted(full_missing)}")

    full_lines = [
        "# 2026-06-05 Candidate Denominator Recalibration — Full Author V1",
        "",
        "> Scope: all `624/624` frozen identities. This receipt supersedes the legacy high-retention",
        "> author denominator for downstream work, but it is not acceptance: a different-context",
        "> false-positive / false-negative audit must pass before this set can be frozen.",
        "",
        "## Reconciliation receipt",
        "",
        "- Raw identities semantically screened: `624/624`.",
        f"- Legacy denominator: `{len(all_old_candidates)}/624` (`{len(all_old_candidates)/624:.1%}`).",
        f"- Recalibrated proposed denominator: `{len(all_retained)}/624` (`{len(all_retained)/624:.1%}`).",
        f"- Preserved legacy pre-denominator closures: `{len(all_old_closures)}`.",
        f"- Newly downgraded families: `{len(all_downgraded)}`.",
        f"- Net denominator change: `-{len(all_downgraded)}`.",
        "- Coverage Gate: `Open pending fresh-context denominator audit`.",
        "- Evidence / Selection / Books Gates: `Open`; prior Reviews are reusable evidence only.",
        "- Books writeback: `Not started`.",
        "",
        "## Proposed retained families",
        "",
        "| # | arXiv | Title | Durable design delta |",
        "| ---: | --- | --- | --- |",
    ]
    retained_ids = {x["arxiv_id"] for x in all_retained}
    downgraded_ids = {x["arxiv_id"] for x in all_downgraded}
    for idx, entry in enumerate(all_identities, 1):
        if entry["arxiv_id"] in retained_ids:
            full_lines.append(
                f"| {idx} | `{entry['arxiv_id']}` | {entry['title']} | {entry['screening_reason']} "
                "The family changes a durable mechanism, ownership boundary, or evaluation/control contract. |"
            )
    full_lines += [
        "",
        "## Newly downgraded pre-denominator closures",
        "",
        "| # | arXiv | Family-specific closure reason |",
        "| ---: | --- | --- |",
    ]
    for idx, entry in enumerate(all_identities, 1):
        if entry["arxiv_id"] in downgraded_ids:
            full_lines.append(f"| {idx} | `{entry['arxiv_id']}` | {closure_reason(entry)} |")
    full_lines += [
        "",
        "## Gate and continuation",
        "",
        "Do not rebuild Score V2, Selection, Books Comparison, or the Daily README from this author",
        "receipt yet. The next owner must independently sample both sides, search for missed durable",
        "families among all 573 proposed closures, and challenge false positives among all proposed",
        "retained families. Only the reconciled result may become the new frozen denominator.",
        "",
    ]
    FULL_OUTPUT.write_text("\n".join(full_lines))
    print(
        json.dumps(
            {
                "scope": 160,
                "legacy_retained": len(old_candidates),
                "recalibrated_retained": len(retained),
                "downgraded": len(downgraded),
                "legacy_closures": len(old_closures),
                "output": str(OUTPUT.relative_to(ROOT)),
                "full_recalibrated_retained": len(all_retained),
                "full_downgraded": len(all_downgraded),
                "full_output": str(FULL_OUTPUT.relative_to(ROOT)),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
