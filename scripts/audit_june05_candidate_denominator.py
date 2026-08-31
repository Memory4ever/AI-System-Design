#!/usr/bin/env python3
"""Build the independent 624-row adversarial Candidate Denominator audit for 2026-06-05."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260605"
LEDGER = PACKET / "screening-ledger.json"
AUTHOR = PACKET / "denominator-recalibration-full-author-v1.md"
AUDIT_TSV = PACKET / "denominator-recalibration-independent-adversarial-v1.tsv"
AUDIT_MD = PACKET / "denominator-recalibration-independent-adversarial-v1.md"
AUDIT_SHA = PACKET / "denominator-recalibration-independent-adversarial-v1.sha256"


# This is the independent semantic result.  Every retained row has an explicit
# durable owner and a source-specific reason; no author decision is used to
# derive membership.
RETAIN: dict[str, tuple[str, str]] = {
    "2606.05548": ("PLATFORM-EVALUATION-SYSTEM", "Freezing the developer, ADK API/documentation surface, isolated runner, generation effort and downstream agent outcomes changes how Agent frameworks are compared rather than merely adding one task score."),
    "2606.05551": ("PLATFORM-EVALUATION-SYSTEM", "Action-conditional rather than marginal conformal coverage changes the safety guarantee attached to each released decision and therefore the evaluation/release contract."),
    "2606.05558": ("PLATFORM-EVALUATION-SYSTEM", "Off-policy Agent evaluation from logged trajectories introduces an explicit surrogate-environment boundary and policy-conditioned transition contract instead of requiring live execution."),
    "2606.05559": ("AGENT-PLATFORM", "CLaaS assigns rollout storage, replay, asynchronous parameter updates and serving-time model refresh to a deployment service, changing state and control ownership."),
    "2606.05568": ("AGENT-RAG", "Turning ColBERT token storage into a quantized inverted index changes persistent index layout, gather/decompression work and MaxSim data flow, not only retrieval accuracy."),
    "2606.05597": ("TRAIN-DISTRIBUTED-TRAINING", "Overlapping rollout, update and policy refresh with an everlasting rollout pool changes distributed RL execution and freshness ownership; the trajectory normalizer finding also changes token-budget accounting."),
    "2606.05610": ("TRAIN-PRETRAINING", "Checkpoint-equivalent compute and proxy-derived learning-rate/batch laws change continued-pretraining resource planning and stability judgment rather than reporting one optimum."),
    "2606.05679": ("PLATFORM-SECURITY", "Optimizer-invariant tuple-level provenance predicates move Agent data-release safety from prompts into the DBMS, giving the data plane enforcement ownership."),
    "2606.05688": ("MODEL-MOE", "Quantization can change top-k expert identity; preserving router value and ordering therefore becomes part of MoE quantization correctness, not an optional quality metric."),
    "2606.05725": ("PLATFORM-SECURITY", "Model-extraction detection is defined over benign-calibrated traffic windows, making cross-request distribution state and service-level thresholds explicit security state."),
    "2606.05742": ("INFER-SPECULATIVE-DECODING", "Adaptive retrieval and reuse of prior draft candidates changes model-free speculative proposal state and the acceptance/control loop."),
    "2606.05800": ("TRAIN-GRPO", "The feature-concentration diagnosis shows why more group rollouts can stop adding training signal and changes the design judgment for allocating rollout compute."),
    "2606.05805": ("PLATFORM-SECURITY", "Returning a constrained remediation plan rather than only allow/deny changes the guardrail-to-agent action interface and the authority boundary for recovery."),
    "2606.05868": ("INFER-KV-CACHE", "Adaptive GQA-to-MLA transition changes KV representation and concurrency memory layout; the financial workload is evidence, not the owner of the mechanism."),
    "2606.05875": ("INFER-KV-CACHE", "Query-aware compressed cache fusion changes the identity, granularity and quality boundary of reusable RAG prefill state."),
    "2606.05894": ("AGENT-MEMORY", "Budgeted evidence retention makes provenance, eviction and future retrieval cost explicit long-horizon memory state rather than flat context trimming."),
    "2606.05933": ("INFER-SCHEDULING", "SLO-aware sliding-window chunking changes batch construction, latency prediction and fairness state under shared inference contention."),
    "2606.05951": ("TRAIN-DISTRIBUTED-TRAINING", "Symmetric memory and device-initiated one-sided communication change ownership and initiation of sparse AI communication, a runtime mechanism rather than an application benchmark."),
    "2606.05958": ("PLATFORM-SECURITY", "Activation-steering artifacts become a model-control supply-chain input that can be poisoned, requiring admission, provenance and mitigation boundaries."),
    "2606.06036": ("AGENT-MEMORY", "Reconstructing graph memory at query time changes what is authoritative stored state versus derived retrieval state for long-horizon agents."),
    "2606.06054": ("AGENT-MEMORY", "Separating similarity from authority, recency and user control changes the admission and ranking contract for personal memory."),
    "2606.06055": ("AGENT-MEMORY", "The relevant-versus-warranted distinction changes the evaluation boundary for using sensitive history, not merely memory retrieval accuracy."),
    "2606.06090": ("AGENT-MEMORY", "Treating memory as workflow execution state assigns durable status, decisions and handoff ownership separately from semantic document organization."),
    "2606.06223": ("PLATFORM-MONITORING", "Reward-hack activation is only latent policy state; combining it with entropy and decision context changes the monitor-to-risk-state contract and prevents activation from being treated as an action verdict."),
    "2606.06240": ("AGENT-MEMORY", "Bitemporal valid-time and transaction-time operators define contradiction resolution and history semantics for persistent Agent memory."),
    "2606.06256": ("INFER-KV-CACHE", "Head-aware reuse plus segmented paging changes long-context KV identity, page layout and execution rather than only model quality."),
    "2606.06284": ("AGENT-TOOL-CALLING", "Precondition-effect contracts expose only the causally sufficient next-step tool frontier, making tool-menu state a controlled runtime surface."),
    "2606.06302": ("INFER-KV-CACHE", "Non-uniform layer/head KV compression changes multi-turn cache allocation and quality accounting at serving time."),
    "2606.06324": ("AGENT-PLATFORM", "Separating harness flaws from model failures changes diagnosis, lifecycle and repair ownership in Agent runtimes."),
    "2606.06387": ("AGENT-MCP", "Tool-surface poisoning at WebMCP discovery time changes protocol trust, runtime authorization and tool metadata admission."),
    "2606.06448": ("AGENT-MEMORY", "Workload characterization ties long-lived Agent state to serving locality, memory pressure and request execution, changing platform capacity assumptions."),
    "2606.06453": ("INFER-PAGED-ATTENTION", "Programmable sparse-attention indexes and kernels change request-level serving state and execution for Agent workloads."),
    "2606.06460": ("PLATFORM-SECURITY", "Recusal at admission and stop mid-flight are distinct in-band governance events, changing credentialed Agent control semantics."),
    "2606.06467": ("INFER-PAGED-ATTENTION", "Sharing sparse-attention routing across layers removes repeated index construction and changes cross-layer access-state ownership."),
    "2606.06697": ("PLATFORM-SECURITY", "Virtualizing CUDA at a trusted worker and separating user from protected module/MMIO ranges moves context, handles and GPU-service state behind an OS-like protection boundary."),
    "2606.06708": ("AGENT-CONTEXT", "Decoupling observation frequency from action frequency and triggering full-DOM reads by explicit signals changes context ingestion ownership for long-horizon web agents."),
    "2606.06747": ("PLATFORM-EVALUATION-SYSTEM", "Executable tensor-algebra property skeletons bind compiler transformations to semantic oracles and applicability/safety validation, changing AI-compiler correctness testing."),
    "2606.06751": ("PLATFORM-MONITORING", "The synchronization frontier provides exact additive exposed-time accounting and identifies where coarse evidence ends, changing always-on distributed-training observability."),
    "2606.06758": ("PLATFORM-EVALUATION-SYSTEM", "Matched no/full/retrieved/oracle evidence conditions separate answerability from recoverable evidence use, changing the RAG/long-context evaluation contract."),
    "2606.06767": ("PLATFORM-SECURITY", "Authority-scaled artifact admission binds identity, ingress and revocation closure to delegated execution authority across models, packages and tool servers."),

    # False negatives in the author proposal.
    "2606.05606": ("TRAIN-GRPO", "A posterior over prompt success and a global cross-epoch budget make rollout allocation durable training-resource state rather than a fixed per-prompt hyperparameter."),
    "2606.05646": ("AGENT-MEMORY", "Validated downstream impact is used both as a task-agnostic memory evaluation contract and as the closed-loop optimization signal across episodes."),
    "2606.05662": ("PLATFORM-FOUNDATIONS", "QDAG moves production analytics methodology from drifting imperative glue into typed, composable, demand-driven DAG state deployed across 500 hosts and 100 use cases."),
    "2606.05711": ("AGENT-MULTI-AGENT", "The text-versus-latent communication framework exposes what state crosses Agent boundaries, how sender/receiver spaces align and how the receiver fuses it; this corrects the durable protocol model even though the paper is a synthesis."),
    "2606.05743": ("PLATFORM-SECURITY", "Contrastive safety-memory cells jointly store block and permit conditions and evolve without retraining, changing guardrail state, poisoning risk and cross-attack reuse."),
    "2606.05787": ("PLATFORM-SECURITY", "Owner-only sentinel probes and synthetic database entries introduce a provenance/detection contract for unauthorized RAG datastore redistribution."),
    "2606.05828": ("AGENT-PLATFORM", "Strictly separating local statistical preference state from remote semantic intent parsing changes selection authority and privacy/cost ownership in personal Agent harnesses."),
    "2606.05872": ("PLATFORM-MONITORING", "Deriving exploration, rigidity, tool concentration and uncertainty-reduction telemetry from traces adds an Agent-behavior observability plane beyond outcome metrics."),
    "2606.05946": ("PLATFORM-MODEL-REGISTRY", "The models-in-the-dark finding shows rectification/erasure cannot be enforced without lineage across derived models and supply-chain actors, correcting model-registry lifecycle ownership."),
    "2606.05976": ("AGENT-REFLECTION", "Byte-identical errors become correctable when their chat role changes, correcting the durable belief that self-correction failure is purely a reasoning-capability deficit."),
    "2606.06032": ("TRAIN-CHECKPOINT", "Separating storage, representation and accessibility shows behavioral forgetting can coexist with recoverable checkpoint knowledge, changing what forgetting and recovery checks must measure."),
    "2606.06044": ("AGENT-RAG", "Interval entities, Allen relations and fuzzy-bound tightening give dynamic knowledge explicit validity semantics rather than treating time as flat metadata."),
    "2606.06063": ("AGENT-PLATFORM", "The controlled Direct/Deopt-Reopt comparison shows source architecture must be an explicit state in Agentic CPU-to-GPU porting and that success-conditioned speed cannot stand in for end-to-end correctness."),
    "2606.06079": ("AGENT-PLATFORM", "Create/improve/merge operations and offline/online/hybrid modes make Agent skills evolvable lifecycle objects instead of one-shot prompt snippets."),
    "2606.06087": ("AGENT-PLATFORM", "Moving skills from plaintext context into modular LoRA state changes updateability, composition, disclosure and provenance ownership even though the reported gains are task-bounded."),
    "2606.06178": ("INFER-SCHEDULING", "User cost-performance preference becomes learned routing state that must adapt when the routable model set changes, altering model-selection control rather than adding one router score."),
    "2606.06337": ("AGENT-MEMORY", "A typed graph with supersession, invalidation, bitemporal validity and decision-transition evidence defines resumable session state beyond flat transcript summarization."),
    "2606.06438": ("PLATFORM-COST", "Combining workload, power, embodied carbon, scheduling and time-varying grid intensity changes hardware-refresh evaluation from operational efficiency to lifecycle cost."),
    "2606.06545": ("AGENT-MCP", "BeeSpec compilation, tenant-scoped connectors, constrained execution and audit-backed approval give an enterprise MCP control plane explicit provisioning and governance ownership."),
    "2606.06556": ("MULTIMODAL-EMBODIED-VLA", "The position corrects policy-scaling-only system design by identifying data, embodiment, world-model and reward interfaces needed to turn unstructured behavior into robot supervision."),
    "2606.06660": ("MULTIMODAL-EMBODIED-VLA", "A risk probe hands control from a weak to a strong policy before failure, defining selective escalation state and kill criteria rather than merely improving manipulation accuracy."),
    "2606.06687": ("TRAIN-DISTRIBUTED-TRAINING", "Removing the persistent server and separating one-time clustering from intra/inter-cluster consensus changes topology, optimizer and communication ownership in federated training."),
    "2606.06726": ("PLATFORM-SECURITY", "Natural-language requests are translated through a bounded network subgraph into structured policies, exposing intent translation as a validated but non-authoritative step before access enforcement."),
    "2606.06741": ("AGENT-PLATFORM", "OpenSkill constructs both skills and verification anchors from external resources after deployment, changing skill provenance, supervision and self-evolution lifecycle ownership."),
}


FALSE_POSITIVE_REASON = {
    "2606.05636": "StableRCA is a graph-agnostic causal/statistical RCA estimator evaluated on datasets; the abstract does not change telemetry ownership, incident state or the platform evidence interface.",
    "2606.05644": "FIDES is a training-free token-level contrastive decoder with benchmark gains; it is a local RAG model intervention, not a new persistent evidence or serving contract.",
    "2606.05645": "Discrete-WAM is an autonomous-driving representation/training architecture whose unified tokens and planning results remain a domain model variant.",
    "2606.05703": "Parallel Jacobi Decoding is a training-free acceleration method for autoregressive image models; the spatial draft schedule is a local generative-model gain, not a general inference-platform contract.",
    "2606.05773": "PiL-World supplies a VLA-specific learned surrogate and benchmark slice; it does not establish a general evaluation release gate or platform-owned simulator contract.",
    "2606.05784": "TAPO transfers trajectory advantage to tool steps inside one multimodal-search policy optimizer; the abstract reports a local credit-assignment method rather than durable training ownership.",
    "2606.05806": "ToolMaze is a single benchmark for replanning and anomaly recovery; benchmark coverage alone does not change the Agent runtime contract.",
    "2606.06060": "ReCache learns diffusion cache schedules with REINFORCE under a compute budget; this remains a model-specific caching policy and local quality/compute trade-off.",
    "2606.06333": "Subspace-aware sparse autoencoders revise an interpretability representation assumption but do not change model lifecycle, platform evidence or runtime control ownership.",
    "2606.06356": "Layered knowledge infusion is a multimodal iterative-generation architecture choice; its placement study is model-local and does not create a platform interface.",
    "2606.06574": "Program-of-Layers dynamically skips or repeats transformer layers for reasoning accuracy; this is a model execution architecture, not yet a serving-plan correctness or scheduler contract.",
    "2606.06712": "On-policy distillation for AR-to-diffusion conversion is a model post-training recipe with token-efficiency gains, not a durable training-platform ownership change.",
}


def first_sentence(text: str, limit: int = 300) -> str:
    normalized = " ".join(text.split())
    parts = re.split(r"(?<=[.!?])\s+", normalized, maxsplit=1)
    sentence = parts[0]
    if len(sentence) > limit:
        sentence = sentence[: limit - 1].rstrip() + "…"
    return sentence


def closure_class(title: str, abstract: str) -> str:
    value = f"{title} {abstract}".casefold()
    if any(term in value for term in ("benchmark", "evaluat", "audit", "metric", "dataset")):
        return "bounded-benchmark-or-measurement-slice"
    if any(term in value for term in ("agent", "tool", "rag", "memory", "prompt")):
        return "agent-or-rag-method-without-durable-owner-change"
    if any(term in value for term in ("reinforcement learning", "fine-tun", "training", "gradient", "optimizer", "distill")):
        return "local-training-or-optimization-method"
    if any(term in value for term in ("diffusion", "multimodal", "vision", "speech", "representation", "transformer", "language model")):
        return "model-representation-or-domain-variant"
    if any(term in value for term in ("gpu", "stream", "service", "system", "network", "hardware", "compiler")):
        return "bounded-systems-implementation-without-owner-change"
    return "out-of-scope-or-domain-application"


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def table(rows: list[dict[str, str]], columns: list[tuple[str, str]]) -> str:
    header = "| " + " | ".join(label for _, label in columns) + " |"
    divider = "|" + "|".join("---" for _ in columns) + "|"
    body = []
    for row in rows:
        values = []
        for key, _ in columns:
            value = str(row[key]).replace("|", "\\|").replace("\n", " ")
            values.append(value)
        body.append("| " + " | ".join(values) + " |")
    return "\n".join([header, divider, *body])


def main() -> None:
    payload = json.loads(LEDGER.read_text(encoding="utf-8"))
    identities = payload["identities"]
    author_text = AUTHOR.read_text(encoding="utf-8")
    author_section = author_text.split("## Proposed retained families", 1)[1].split(
        "## Newly downgraded pre-denominator closures", 1
    )[0]
    author_retain = set(re.findall(r"^\| \d+ \| `([0-9.]+)` \|", author_section, re.M))
    identity_ids = {row["arxiv_id"] for row in identities}

    assert len(identities) == 624
    assert len(identity_ids) == 624
    assert len({row["source_family_key"] for row in identities}) == 624
    assert len(author_retain) == 52
    assert set(RETAIN) <= identity_ids
    assert set(FALSE_POSITIVE_REASON) == author_retain - set(RETAIN)
    roadmap_ids = set(
        re.findall(
            r"^\| `([A-Z0-9-]+)` \|",
            (ROOT / "ROADMAP.md").read_text(encoding="utf-8"),
            re.M,
        )
    )
    assert {node for node, _ in RETAIN.values()} <= roadmap_ids

    rows: list[dict[str, str]] = []
    for index, identity in enumerate(identities, 1):
        arxiv_id = identity["arxiv_id"]
        author_decision = "retain" if arxiv_id in author_retain else "pre_denominator_closure"
        if arxiv_id in RETAIN:
            node, reason = RETAIN[arxiv_id]
            independent_decision = "retain"
            decision_class = "durable-owner-or-contract-change"
        else:
            node = "—"
            independent_decision = "pre_denominator_closure"
            decision_class = closure_class(identity["title"], identity["abstract"])
            if arxiv_id in FALSE_POSITIVE_REASON:
                reason = FALSE_POSITIVE_REASON[arxiv_id]
            else:
                observation = first_sentence(identity["abstract"])
                reason = (
                    f"The abstract-specific observation is: {observation} "
                    f"Under the corrected Candidate contract this remains `{decision_class}`: it does not explicitly change a durable AI System mechanism, state/data/control owner, evaluation contract or platform/training/inference design judgment."
                )
        if author_decision == "retain" and independent_decision == "pre_denominator_closure":
            finding = "false_positive"
        elif author_decision == "pre_denominator_closure" and independent_decision == "retain":
            finding = "false_negative"
        elif independent_decision == "retain":
            finding = "retain_after_adversarial_recheck"
        else:
            finding = "closure_after_adversarial_recheck"
        rows.append(
            {
                "row_index": str(index),
                "arxiv_id": arxiv_id,
                "source_family_key": identity["source_family_key"],
                "submitted_v1_utc": identity["submitted_v1_utc"],
                "title": identity["title"],
                "author_decision": author_decision,
                "independent_decision": independent_decision,
                "finding": finding,
                "stable_node_id": node,
                "decision_class": decision_class,
                "source_specific_reason": reason,
                "evidence_ref": f"screening-ledger.json#identities[{index - 1}]",
            }
        )

    fields = [
        "row_index", "arxiv_id", "source_family_key", "submitted_v1_utc", "title",
        "author_decision", "independent_decision", "finding", "stable_node_id",
        "decision_class", "source_specific_reason", "evidence_ref",
    ]
    write_tsv(AUDIT_TSV, rows, fields)

    decisions = Counter(row["independent_decision"] for row in rows)
    findings = Counter(row["finding"] for row in rows)
    closure_classes = Counter(
        row["decision_class"] for row in rows if row["independent_decision"] == "pre_denominator_closure"
    )
    retained_rows = [row for row in rows if row["independent_decision"] == "retain"]
    fp_rows = [row for row in rows if row["finding"] == "false_positive"]
    fn_rows = [row for row in rows if row["finding"] == "false_negative"]
    old_routed_ids = {
        row["arxiv_id"]
        for row in identities
        if row["screening_status"] == "routed_candidate"
    }
    final_ids = {row["arxiv_id"] for row in retained_rows}
    denominator_payload = "\n".join(
        f"{row['source_family_key']}\t{row['submitted_v1_utc']}" for row in retained_rows
    )
    denominator_id = "DEN-20260605-" + hashlib.sha256(denominator_payload.encode()).hexdigest()[:8]

    assert decisions == {"pre_denominator_closure": 560, "retain": 64}
    assert findings == {
        "closure_after_adversarial_recheck": 548,
        "false_negative": 24,
        "false_positive": 12,
        "retain_after_adversarial_recheck": 40,
    }
    assert len(old_routed_ids) == payload["routed_candidate_denominator"] == 442

    closure_text = ", ".join(f"{key}={value}" for key, value in sorted(closure_classes.items()))
    receipt = f"""# 2026-06-05 Candidate Denominator — independent adversarial fresh-context audit V1

## Verdict

The author proposal is disproved. Its 52-family denominator contains {len(fp_rows)} false positives and omits {len(fn_rows)} false negatives. This audit independently reviewed all 624 registered identities from title and abstract; no sampling or author disposition was used to derive membership.

- Raw registered identities: 624.
- Previously routed candidate denominator: 442 (invalidated before this audit).
- Author recalibration proposal: 52 retained / 572 pre-denominator closures; retain rate 8.33% of raw identities.
- Independent denominator: {len(retained_rows)} retained / {decisions['pre_denominator_closure']} pre-denominator closures under `{denominator_id}`; retain rate {len(retained_rows) / len(rows):.2%} of raw identities.
- Author/new intersection: {findings['retain_after_adversarial_recheck']}.
- False positives in the author proposal: {findings['false_positive']}.
- False negatives in the author proposal: {findings['false_negative']}.
- Net denominator change versus the author proposal: +{len(retained_rows) - len(author_retain)} families.
- Independent retains already present in the invalidated 442 set: {len(final_ids & old_routed_ids)}; recovered from the 182 old abstract closures: {len(final_ids - old_routed_ids)}.
- Closure classes across all {decisions['pre_denominator_closure']} independent closures: {closure_text}.

The corrected rule is applied literally: full semantic screening protects Coverage recall, but topical AI relevance, ROADMAP mappability, a local method/model gain, a domain benchmark, or abstract novelty does not itself enter the Candidate Denominator. Retain requires a source-specific change to a durable mechanism, state/data/control ownership, evaluation contract, platform/training/inference design judgment, or a correction to existing Books knowledge.

## False positives in the 52-family author proposal

{table(fp_rows, [('row_index', 'Row'), ('arxiv_id', 'arXiv v1'), ('title', 'Family'), ('source_specific_reason', 'Independent finding')])}

## False negatives in the 572 author closures

{table(fn_rows, [('row_index', 'Row'), ('arxiv_id', 'arXiv v1'), ('title', 'Family'), ('stable_node_id', 'Durable owner'), ('source_specific_reason', 'Independent finding')])}

## Independently justified 64-family denominator

{table(retained_rows, [('row_index', 'Row'), ('arxiv_id', 'arXiv v1'), ('title', 'Family'), ('stable_node_id', 'Durable owner'), ('finding', 'Reconciliation')])}

## Full-population evidence and integrity

- Row-level audit: `denominator-recalibration-independent-adversarial-v1.tsv` contains 624/624 unique arXiv identities and 624/624 unique source-family keys.
- Every row records author decision, independent decision, reconciliation finding, source-specific reason, and a locator back to the untouched `screening-ledger.json` title/abstract evidence.
- The author artifact and ledger were not overwritten; this preserves prior evidence and makes disagreement auditable.
- Cross-model review skipped: this was a non-interactive fresh-context subtask and no external CLI authorization was provided.

## Gate boundary

- Coverage semantic audit scope: **Passed** for the complete 624-row identity/title/abstract Candidate Denominator FP/FN audit, with denominator `{denominator_id}`.
- Evidence Gate: **Open**. This task did not perform Source Review, exact-v1 Method/Evaluation/Limitations/Artifact review, benchmark contracts, or access closure.
- Selection Gate: **Open**. No Deep Analysis Selection was performed.
- Books Comparison Gate: **Open**. Books were not read or modified; only the authoritative ROADMAP owner mapping and research/report contracts were used. No Books comparison or writeback was performed.
- This receipt authorizes only serialization of the 64-family Candidate Denominator. It does not authorize Source Review or Books completion claims.
"""
    AUDIT_MD.write_text(receipt, encoding="utf-8")

    sha_rows = []
    for path in (LEDGER, AUTHOR, AUDIT_TSV, AUDIT_MD):
        sha_rows.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  ./{path.name}")
    AUDIT_SHA.write_text("\n".join(sha_rows) + "\n", encoding="utf-8")

    print(
        f"{denominator_id} rows={len(rows)} retain={decisions['retain']} closure={decisions['pre_denominator_closure']} "
        f"fp={findings['false_positive']} fn={findings['false_negative']}"
    )


if __name__ == "__main__":
    main()
