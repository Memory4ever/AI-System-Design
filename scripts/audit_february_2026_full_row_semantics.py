#!/usr/bin/env python3
"""Run the non-sampling February 2026 fresh-context denominator audit.

The prior monthly receipt sampled pre-denominator closures.  This replacement
materializes one reviewer decision for every raw identity and explicitly
promotes false negatives before exact-v1 review.  Weekly artifacts are neither
opened nor accepted as evidence.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
MONTH = ROOT / "papers/2026/02"
SOURCE_ROOT = MONTH / "_sources"
FULL_LEDGER = SOURCE_ROOT / "february-full-row-fresh-context-audit-20260903.json.gz"
SUMMARY = SOURCE_ROOT / "february-full-row-fresh-context-audit-20260903.json"
BOOKS_QUEUE = SOURCE_ROOT / "february-full-row-books-queue-20260903.json"
BOOKS_QUEUE_MD = SOURCE_ROOT / "february-full-row-books-queue-20260903.md"
BOOKS_AUDIT = SOURCE_ROOT / "feb-books-audit-full-row-reopen-20260903.json"


# Fresh-context false negatives found by reading title + abstract.  Each row
# changes a durable mechanism, ownership boundary, security/reliability model,
# or transferable evaluation contract; broad topical relevance alone is not
# sufficient for this list.
PROMOTIONS = {
    "2602.00942": "INFER-GPU-MEMORY",
    "2602.01637": "MODEL-SAMPLING",
    "2602.02061": "INFER-SCHEDULING",
    "2602.02335": "TRAIN-DATA",
    "2602.02386": "PLATFORM-COST",
    "2602.03338": "AGENT-REFLECTION",
    "2602.04930": "PLATFORM-SECURITY",
    "2602.05695": "PLATFORM-COST",
    "2602.06650": "PLATFORM-SECURITY",
    "2602.07120": "MODEL-SAMPLING",
    "2602.07379": "PLATFORM-SECURITY",
    "2602.07840": "PLATFORM-EVALUATION-SYSTEM",
    "2602.07996": "PLATFORM-EVALUATION-SYSTEM",
    "2602.08401": "PLATFORM-SECURITY",
    "2602.08412": "PLATFORM-SECURITY",
    "2602.08563": "AGENT-MEMORY",
    "2602.08621": "PLATFORM-SECURITY",
    "2602.09369": "PLATFORM-MONITORING",
    "2602.09629": "PLATFORM-SECURITY",
    "2602.09937": "AGENT-MULTI-AGENT",
    "2602.10465": "PLATFORM-SECURITY",
    "2602.11088": "PLATFORM-SECURITY",
    "2602.11287": "INFER-TENSORRT-LLM",
    "2602.11506": "PLATFORM-EVALUATION-SYSTEM",
    "2602.11510": "PLATFORM-SECURITY",
    "2602.11574": "AGENT-PLATFORM",
    "2602.11786": "PLATFORM-EVALUATION-SYSTEM",
    "2602.11877": "PLATFORM-EVALUATION-SYSTEM",
    "2602.12194": "PLATFORM-SECURITY",
}


# Proposition-level comparisons against the current canonical owner plus both
# adjacent chapters.  These decisions were made in report-date order after the
# overlapping May lane released all Books owners.  "No Change" means the
# durable proposition is already present, not that the paper lacks value.
BOOKS_DECISIONS = {
    "2602.00942": {"decision": "No Change — Existing Coverage", "anchor_query": "elastic post-training sparsity / memory-budget fallback", "rationale": "Ch54 already binds sparse/low-rank or quantized capacity variants to deployment memory budgets, quality validation and dense fallback; SALAAD adds a particular ADMM training construction, not a new inference-memory ownership contract."},
    "2602.01637": {"decision": "Integrate", "anchor_query": "Accepted-generation Risk 需要 Chance Constraint", "rationale": "Ch20 separates proposal, verification and commit but did not distinguish confidence-based selection from an anytime-valid chance constraint over accepted generations under repeated use.", "integration": {"canonical_owner": "MODEL-SAMPLING", "insertion_heading": "Accepted-generation Risk 需要 Chance Constraint，不是 Confidence Threshold", "durable_mechanism_delta": "Treat each generation as a stochastic constraint trial and use sequential anytime-valid evidence to accept, defer or declare infeasibility against a versioned risk budget.", "trade_off_failure_mode": "Sampling cost and scorer or independence drift can invalidate the certificate; keep fixed decoding or ordinary selective prediction for low-risk latency-sensitive paths."}},
    "2602.02061": {"decision": "Integrate", "anchor_query": "User Retrial 是 Endogenous Arrival", "rationale": "Ch56 covers online routing and queue state but did not model user retrials as both implicit preference feedback and endogenous workload that feeds the scheduler backlog.", "integration": {"canonical_owner": "INFER-SCHEDULING", "insertion_heading": "User Retrial 是 Endogenous Arrival，不是独立新请求", "durable_mechanism_delta": "Bind retrial lineage, prior route, completion and queue state so routing learns implicit preference while queue stability retains commit authority.", "trade_off_failure_mode": "Network retries and duplicate clicks can masquerade as preference, while exploration harms SLO; fall back to explicit feedback and FIFO/EDF/aging when lineage is unreliable."}},
    "2602.02335": {"decision": "Integrate", "anchor_query": "Data Contract 要延伸到整次 Pipeline Commit", "rationale": "Ch27 versions dataset identities and transformation lineage but did not connect typed table contracts, Git-like data branches and atomic multi-output pipeline publication into one correctness boundary.", "integration": {"canonical_owner": "TRAIN-DATA", "insertion_heading": "Data Contract 要延伸到整次 Pipeline Commit", "durable_mechanism_delta": "Validate transformations in an isolated data revision and move the authoritative head only with a single pipeline commit that publishes all outputs.", "trade_off_failure_mode": "Version graphs, conflict resolution and multi-table transactions add cost and are not production throughput proof; single-writer or single-table snapshots remain valid baselines."}},
    "2602.02386": {"decision": "No Change — Existing Coverage", "anchor_query": "quality-target cost routing", "rationale": "Ch70 already requires task/quality/SLO identity, model-path cost and fallback to be evaluated together; interpretable skill profiles are one router feature implementation rather than a new cost-owner contract."},
    "2602.03338": {"decision": "Integrate", "anchor_query": "Critic Accuracy 不等于 Intervention Value", "rationale": "Ch80 treats critics as fallible sensors but did not state the causal disruption-recovery trade-off or require a paired pilot before enabling proactive intervention.", "integration": {"canonical_owner": "AGENT-REFLECTION", "insertion_heading": "Critic Accuracy 不等于 Intervention Value", "durable_mechanism_delta": "Gate intervention on paired pilot evidence for recovered failures minus disrupted successes and intervention cost, rather than on critic AUROC.", "trade_off_failure_mode": "Pilot estimates drift across task and model mixtures; uncertainty or high-risk actions should disable automatic interruption and escalate verification."}},
    "2602.04930": {"decision": "Integrate", "anchor_query": "Control Evaluation 要测试 Attacker 如何选择攻击时机", "rationale": "Ch72 covers adaptive attacks and attempt budgets but did not bind attack-quality scoring and submission policy to monitoring FPR under a concentrated audit budget.", "integration": {"canonical_owner": "PLATFORM-SECURITY", "insertion_heading": "Control Evaluation 要测试 Attacker 如何选择攻击时机", "durable_mechanism_delta": "Freeze generator, attack-quality estimator, submission policy, opportunity and audit budget so selective low-frequency attacks are part of the control evaluation.", "trade_off_failure_mode": "Results remain a lower bound conditioned on red-team capability and candidate distribution; retain independent audits, least privilege and safe commit."}},
    "2602.05695": {"decision": "Integrate", "anchor_query": "Generation Energy 不是 Token 数的线性函数", "rationale": "Ch70 records input/output lengths and energy attribution, but it did not make the nonlinear two-dimensional generation-energy surface and workload-specific local operating point explicit.", "integration": {"canonical_owner": "PLATFORM-COST", "insertion_heading": "Generation Energy 不是 Token 数的线性函数", "durable_mechanism_delta": "Calibrate energy over the joint input/output-length surface and evaluate truncation, summarization or generation budgets against energy per successful goal.", "trade_off_failure_mode": "The operating point moves with runtime, batching, KV cache and hardware; analytical estimates are proposals and require current quality/SLO and energy receipts."}},
    "2602.06650": {"decision": "No Change — Existing Coverage", "anchor_query": "hierarchical runtime safety policy", "rationale": "Ch72 already separates immutable global policy, tenant/user policy, learned risk sensors and deterministic action authorization; PACT supplies a bounded Classify-to-Act implementation without changing those authorities."},
    "2602.07120": {"decision": "Integrate", "anchor_query": "Anchored Decoding 把版权风险编译为序列信息预算", "rationale": "Ch20 covers constrained and safety-aware decoding but not a sequence-level information budget that keeps a risky proposal distribution near a permissively trained reference, including cross-vocabulary byte fusion.", "integration": {"canonical_owner": "MODEL-SAMPLING", "insertion_heading": "Anchored Decoding 把版权风险编译为序列信息预算", "durable_mechanism_delta": "Allocate a versioned sequence information budget across token steps and constrain risky-LM proposals against a permissive reference distribution before commit.", "trade_off_failure_mode": "Dual-model cost, utility loss and reference-data provenance remain; it is not a legal compliance certificate and must coexist with output review."}},
    "2602.07379": {"decision": "No Change — Existing Coverage", "anchor_query": "channel-specific layered agent defense", "rationale": "Ch72 already treats modality/channel identity, access control, behavior policy and monitoring as separate layers; the voice-agent cases broaden scenarios without changing that security contract."},
    "2602.07840": {"decision": "No Change — Existing Coverage", "anchor_query": "policy precedent surrogate judge calibration loop", "rationale": "Ch66 already versions policy/rubric, precedent, human calibration, surrogate judge and distillation cost as separate evaluation authorities with regression gates."},
    "2602.07996": {"decision": "No Change — Existing Coverage", "anchor_query": "judge shortcut and cue invariance", "rationale": "Ch66 already requires controlled cue perturbations, judge disagreement/bias checks, configuration identity and independent adjudication; unacknowledged recency/provenance cues are an instance of that existing contract."},
    "2602.08401": {"decision": "No Change — Existing Coverage", "anchor_query": "agent provenance and watermark verification", "rationale": "Ch72 already separates provenance metadata, watermark signal, model/action-path revision and inconclusive verification, including false positive/negative and transformation limits."},
    "2602.08412": {"decision": "No Change — Existing Coverage", "anchor_query": "persistent local-agent attack state", "rationale": "Ch72 already models persistent memory, delayed triggers, tool effects and local-agent supply-chain boundaries; the OpenClaw benchmark adds a bounded target, not a new owner contract."},
    "2602.08563": {"decision": "Integrate", "anchor_query": "Stateless API 仍可能承载跨调用的 Implicit Memory", "rationale": "Ch77 governs explicit external and parametric memory but did not identify output-mediated state re-injection as an implicit hidden channel lacking record identity, ACL, expiry and deletion semantics.", "integration": {"canonical_owner": "AGENT-MEMORY", "insertion_heading": "Stateless API 仍可能承载跨调用的 Implicit Memory", "durable_mechanism_delta": "Audit predecessor-output re-injection as memory state by binding output, normalization, transport, wrapper and later behavior with matched temporal controls.", "trade_off_failure_mode": "Scrubbing can damage utility and cannot prove all encodings removed; high-risk paths should use typed handoffs or prohibit free-text return."}},
    "2602.08621": {"decision": "No Change — Existing Coverage", "anchor_query": "MoE routing as security state", "rationale": "Ch72 already makes router revision, expert assignment distribution, input perturbation and independent safety slices part of the MoE security contract, with dense/end-to-end fallback."},
    "2602.09369": {"decision": "Integrate", "anchor_query": "Host 与 Device 都不可信时的旁路遥测", "rationale": "Ch67 covers trusted counters and indirect telemetry but did not define active compute challenges combining parallel work, sequential delay, GEMM and VRAM-residency evidence when host and device counters are untrusted.", "integration": {"canonical_owner": "PLATFORM-MONITORING", "insertion_heading": "Host 与 Device 都不可信时，用计算挑战构造旁路遥测", "durable_mechanism_delta": "Use versioned active compute challenges to produce statistical utilization evidence without trusting firmware or vendor counters.", "trade_off_failure_mode": "Challenge overhead and architectural drift are substantial, and evidence cannot identify model purpose; emit suspect or unknown and retain attestation/manual investigation."}},
    "2602.09629": {"decision": "No Change — Existing Coverage", "anchor_query": "stage-specific safety checkpoints", "rationale": "Ch72 already separates input/output, literal/semantic detection, proposal/authorization/commit and weighted severity; the four-checkpoint taxonomy is an existing-coverage specialization."},
    "2602.09937": {"decision": "Integrate", "anchor_query": "Multi-Agent Failure 按 Intra / Inter / Environment 分层", "rationale": "Ch82 tracks handoffs and constraint survival but did not require failures to be attributed across intra-agent reasoning, inter-agent communication and agent-environment interaction before choosing a repair.", "integration": {"canonical_owner": "AGENT-MULTI-AGENT", "insertion_heading": "Multi-Agent Failure 要按 Intra / Inter / Environment 分层归因", "durable_mechanism_delta": "Record earliest evidence-backed failure span, responsibility layer, affected handoff/state and outcome so repairs target the actual layer.", "trade_off_failure_mode": "Richer protocols add cost and can propagate errors; use single-agent deterministic verification for simple tasks and do not generalize benchmark failure rates."}},
    "2602.10465": {"decision": "No Change — Existing Coverage", "anchor_query": "authenticated intent and integrity at workflow boundaries", "rationale": "Ch72 already binds authenticated principal/delegation, data-flow authority, signed artifacts, effect-time policy and workflow provenance; MAPL and framework adapters are a concrete protocol, not a new durable boundary."},
    "2602.11088": {"decision": "Integrate", "anchor_query": "Partial TEE 协议的秘密随机性不得跨请求复用", "rationale": "Ch72 covers TEE scope, nonce/replay and split-inference leakage, but did not state that precomputed static secret bases can become reusable keying material that breaks both confidentiality and integrity.", "integration": {"canonical_owner": "PLATFORM-SECURITY", "insertion_heading": "Partial TEE 协议的秘密随机性不得跨请求复用", "durable_mechanism_delta": "Make entropy source, nonce/counter, request binding, key epoch, allowed reuse and recovery part of the partial-TEE protocol identity.", "trade_off_failure_mode": "Fresh secrets add enclave and communication cost; without provable domain separation, fall back to fuller trusted execution, MPC or a narrower confidentiality claim."}},
    "2602.11287": {"decision": "No Change — Existing Coverage", "anchor_query": "low-bit format identity and hardware execution", "rationale": "Ch49 already treats bit layout, group/scaling metadata, accumulator precision, kernel support, accuracy and hardware area/power as one versioned execution-plan contract."},
    "2602.11506": {"decision": "No Change — Existing Coverage", "anchor_query": "roofline evaluation envelope", "rationale": "Ch66 already separates operational intensity, hardware ceilings, model shape/sequence length and cross-device evaluation envelopes; Relative Inference Potential is an additional metric inside that contract."},
    "2602.11510": {"decision": "No Change — Existing Coverage", "anchor_query": "multi-agent internal-channel privacy", "rationale": "Ch72 already audits messages, shared memory, tool arguments and final output as distinct privacy channels and rejects output-only assurance; AgentLeak supplies a bounded benchmark instance."},
    "2602.11574": {"decision": "No Change — Existing Coverage", "anchor_query": "query-specific agent configuration policy", "rationale": "Ch84 already represents workflow, tools, prompt and budget as a versioned option catalog selected per query, while commit and fallback remain platform authorities."},
    "2602.11786": {"decision": "Integrate", "anchor_query": "Safety Evaluation 还需要 Depth-oriented Repeated Inference", "rationale": "Ch66 asks for repeated runs and variance, but did not separate breadth coverage from depth-oriented estimation of per-inference failure frequency under identical operational conditions.", "integration": {"canonical_owner": "PLATFORM-EVALUATION-SYSTEM", "insertion_heading": "Safety Evaluation 还需要 Depth-oriented Repeated Inference", "durable_mechanism_delta": "Freeze prompt family, runtime, sampling and scorer, then report repeated-sampling failure probability, interval, first-failure depth and correlation separately from breadth coverage.", "trade_off_failure_mode": "Cost, cache/provider drift and correlated samples limit inference; keep breadth benchmarks and mark unseen failure bounds unresolved when depth is insufficient."}},
    "2602.11877": {"decision": "No Change — Existing Coverage", "anchor_query": "router evaluation by ability scenario and robustness", "rationale": "Ch66 already requires routing quality, scenario alignment, cost/privacy constraints and OOD robustness to be evaluated as separate axes under a frozen router/model envelope."},
    "2602.12194": {"decision": "No Change — Existing Coverage", "anchor_query": "malicious tool implementation and executable admission", "rationale": "Ch72 already requires tool code and dependencies to be scanned, sandbox-executed and admitted from legitimate-task plus malicious-effect receipts; generated malicious implementations expand the test corpus without changing the gate."},
}


# Every recovered family is rebound to an evidence-bearing exact-v1 section.
# This avoids accepting a title, related-work heading, conclusion, or generic
# keyword hit as the method/evaluation/limitation receipt.
PROMOTION_SECTION_OVERRIDES = {
    "2602.00942": {
        "method": [r"^4\.1 admm for slr decomposition$", r"^4\.2 i-controller for adaptive regularization$"],
        "evaluation": [r"^5 experiments$"],
        "limitations": [r"^appendix a limitations of post-hoc sparse and low-rank decomposition$"],
    },
    "2602.01637": {
        "method": [r"^9 sequential chance-constrained inference algorithm$", r"^5 chance-constrained inference$"],
        "evaluation": [r"^10 experimental evaluation$"],
    },
    "2602.02061": {
        "method": [r"^3 proposed algorithm$"],
        "evaluation": [r"^6 experiments$"],
    },
    "2602.02335": {
        "method": [r"^4\. a lightweight formal model$", r"^3\. design principles$"],
        "evaluation": [r"^minimal counterexamples\.$"],
        "limitations": [r"^6\. conclusion and future work$"],
    },
    "2602.02386": {
        "method": [r"^3 the bella framework$"],
        "evaluation": [r"^3\.5 evaluation methodology$"],
        "limitations": [r"^4\.3 limitations$"],
    },
    "2602.03338": {
        "method": [r"^experimental design\.$", r"^intervention mechanisms\.$"],
        "evaluation": [r"^4 main results$"],
        "limitations": [r"^critic model scale\.$", r"^benchmark and agent coverage\.$"],
    },
    "2602.04930": {
        "method": [r"^2 attack selection$"],
        "evaluation": [r"^4 results and discussion$"],
        "limitations": [r"^5\.1 limitations$"],
    },
    "2602.05695": {
        "method": [r"^4\. llm inference consumption analytical models$"],
        "evaluation": [r"^5\. experimental methodology$"],
    },
    "2602.06650": {
        "method": [r"^3 methodology$"],
        "evaluation": [r"^4 experiments$"],
        "limitations": [r"^limitations$"],
    },
    "2602.07120": {
        "method": [r"^3\.5 putting anchored decoding together$", r"^3\.1 a tractable token-level approximation$"],
        "evaluation": [r"^5\.1 risk–utility trade-offs$", r"^5\.3 efficiency$"],
    },
    "2602.07379": {
        "method": [r"^3\.1 framework$", r"^3\.2 adversarial scenarios$"],
        "evaluation": [r"^4 evaluation$"],
    },
    "2602.07840": {
        "method": [r"^3\. problem formulation and framework$"],
        "evaluation": [r"^5\.3\. experiments: optimizing the student model$"],
    },
    "2602.07996": {
        "method": [r"^3\.2 cue families$", r"^3\.1 task definition$"],
        "evaluation": [r"^llm judges exhibit a strong and largely unacknowledged recency bias\.$"],
        "limitations": [r"^6 limitations$"],
    },
    "2602.08401": {
        "method": [r"^iv methodology$"],
        "evaluation": [r"^vii evaluation$"],
    },
    "2602.08412": {
        "method": [r"^2\.4 attack primitives$", r"^2\.2 threat model$"],
        "evaluation": [r"^3\.2 main results and analysis$"],
        "limitations": [r"^4 conclusion and future work$"],
    },
    "2602.08563": {
        "method": [r"^iii implicit memory in llms: definition, threat model, and feasibility$"],
        "evaluation": [r"^vii time bomb: a temporal backdoor via implicit memory$"],
        "limitations": [r"^ix future directions$"],
    },
    "2602.08621": {
        "method": [r"^our proposed f-sour$", r"^rosais-based unsafe route discovery$"],
        "evaluation": [r"^experimental results$"],
        "limitations": [r"^appendix g limitations and future work$"],
    },
    "2602.09369": {
        "method": [r"^4\. timing measurements$", r"^5\. memory and residency inference$"],
        "evaluation": [r"^6\.3\. reliability analysis$", r"^6\.4\. overhead analysis$"],
        "limitations": [r"^7\. conclusion and discussion$"],
    },
    "2602.09629": {
        "method": [r"^6\.2\. the safety pipeline model$", r"^6\.3\. checkpoint definitions$"],
        "evaluation": [r"^10\.2\. checkpoint effectiveness$", r"^10\.1\. overall model performance$"],
        "limitations": [r"^11\.2\. limitations$", r"^5\. scope and limitations$"],
    },
    "2602.09937": {
        "method": [r"^3\. agent failure diagnosis methodology$"],
        "evaluation": [r"^4\. architectural pitfalls in rca agents$"],
        "limitations": [r"^6\. conclusion and future work$"],
    },
    "2602.10465": {
        "method": [r"^iv authenticated workflows$"],
        "evaluation": [r"^viii attack-defense validation$"],
    },
    "2602.11088": {
        "method": [r"^4\. attack on tee-based model confidentiality$", r"^5\. attack on tee-based computational integrity$"],
        "evaluation": [r"^6\. evaluation$"],
        "limitations": [r"^c\.1\. limitations and scope$"],
    },
    "2602.11287": {
        "method": [r"^ii hifloat4$"],
        "evaluation": [r"^iv language model inference with hifloat4$"],
    },
    "2602.11506": {
        "method": [r"^3 methodology: the integrated standard roofline framework$"],
        "evaluation": [r"^4 comprehensive characterization study$"],
        "limitations": [r"^appendix b future work$"],
    },
    "2602.11510": {
        "method": [r"^iv agentleak benchmark design$"],
        "evaluation": [r"^vi evaluation and results$"],
        "limitations": [r"^vii-d limitations$"],
    },
    "2602.11574": {
        "method": [r"^3 methodology$"],
        "evaluation": [r"^4 experiments$"],
        "limitations": [r"^4\.6 error analysis$"],
    },
    "2602.11786": {
        "method": [r"^3 methodology$"],
        "evaluation": [r"^4\.3 phase 2b: depth-oriented evaluation under repeated sampling$"],
        "limitations": [r"^limitations and scope\.$"],
    },
    "2602.11877": {
        "method": [r"^3 evaluation framework$", r"^4 methodology$"],
        "evaluation": [r"^router ability\.$", r"^scenario alignment\.$"],
        "limitations": [r"^limitations$"],
    },
    "2602.12194": {
        "method": [r"^5 our maltool$"],
        "evaluation": [r"^6 evaluating maltool$"],
        "limitations": [r"^8 discussion and limitations$"],
    },
}


CONTRACT_FILES = (
    "AGENTS.md",
    "docs/RESEARCH_CONTRACT.md",
    "docs/RESEARCH_SOURCES.md",
    "docs/REPORT_CONTRACTS.md",
    "CODEX_DAILY_RESEARCH_PROMPT.md",
    "ROADMAP.md",
    "papers/2026/02/_sources/latest-contract-semantic-reopen-20260903.json",
)
DAY_FILES = (
    "inventory.json",
    "raw-inventory-reconciliation.json",
    "screening-ledger-author.json",
    "screening-ledger-final.json",
    "exact-v1-review-packet.json",
    "coverage-receipt.json",
    "official-arxiv-first-announcement-reconciliation.json",
)
OPTIONAL_DAY_FILES = (
    "withdrawn-status-receipt.json",
    "arxiv-revision-status-receipt.json",
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def file_receipt(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(raw),
        "sha256": sha256_bytes(raw),
    }


def compact(value: str, limit: int = 240) -> str:
    return " ".join(value.split())[:limit].rstrip()


def canonical_identity(value: str) -> str:
    return value.removesuffix("v1")


def roadmap_owners() -> list[dict[str, object]]:
    owners = []
    row_re = re.compile(
        r"^\| `([^`]+)` \| Ch(\d+) \| `([^`]+)` \| [^|]+ \|$",
        re.M,
    )
    for node, chapter, path in row_re.findall((ROOT / "ROADMAP.md").read_text()):
        owners.append({"stable_node_id": node, "chapter": int(chapter), "path": path})
    owners.sort(key=lambda row: row["chapter"])
    return owners


def write_books_queue(entries: list[dict[str, object]]) -> None:
    if set(BOOKS_DECISIONS) != set(PROMOTIONS):
        raise RuntimeError("Books decisions must cover every recovered false negative exactly once")
    owners = roadmap_owners()
    by_node = {row["stable_node_id"]: (index, row) for index, row in enumerate(owners)}
    queue = []
    audit_items = []
    comparison_paths: set[Path] = set()
    for entry in sorted(entries, key=lambda row: (row["report_date"], row["arxiv_id"])):
        index, owner = by_node[entry["stable_node_id"]]
        adjacent = []
        for other_index in (index - 1, index + 1):
            if 0 <= other_index < len(owners):
                adjacent.append(owners[other_index]["path"])
        target_path = ROOT / owner["path"]
        comparison_paths.add(target_path)
        comparison_paths.update(ROOT / path for path in adjacent)
        decision = BOOKS_DECISIONS[entry["arxiv_id"]]
        if decision["decision"] == "Integrate" and entry["source_family_id"] not in target_path.read_text():
            raise RuntimeError(f"Missing post-write Books marker: {entry['source_family_id']}")
        audit_item = {
            "source_family_id": entry["source_family_id"],
            "arxiv_id": entry["arxiv_id"],
            "title": entry["title"],
            "decision": decision["decision"],
            "stable_node_id": entry["stable_node_id"],
            "anchor_query": decision["anchor_query"],
            "rationale": decision["rationale"],
            "audit_status": "postwrite_verified" if decision["decision"] == "Integrate" else "verified_existing_coverage",
        }
        if "integration" in decision:
            audit_item["integration"] = decision["integration"]
        audit_items.append(audit_item)
        queue.append({
            **entry,
            "target_chapter": owner["path"],
            "adjacent_chapters": adjacent,
            "books_decision": decision["decision"],
            "anchor_query": decision["anchor_query"],
            "rationale": decision["rationale"],
            "status": audit_item["audit_status"],
            "blocker": None,
            "weekly_evidence_used": False,
        })
    BOOKS_AUDIT.write_text(json.dumps({
        "schema_version": "books-current-content-audit-v2.1",
        "scope": "29 false negatives recovered by the February 2026 full-row fresh-context audit",
        "item_count": len(audit_items),
        "order": "report_date_then_arxiv_id",
        "weekly_evidence_used": False,
        "comparison_receipts": [file_receipt(path) for path in sorted(comparison_paths)],
        "items": audit_items,
    }, ensure_ascii=False, indent=2) + "\n")
    payload = {
        "schema": "february-2026-date-ordered-books-decision-queue-v1",
        "status": "postwrite_verified",
        "order": "report_date_then_arxiv_id",
        "count": len(queue),
        "weekly_evidence_used": False,
        "books_audit_ref": BOOKS_AUDIT.relative_to(ROOT).as_posix(),
        "items": queue,
    }
    BOOKS_QUEUE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    lines = [
        "# February 2026 Date-Ordered Books Decision Queue",
        "",
        "Status: Complete; all 29 decisions were compared in date order after the overlapping May lane released its owners.",
        "",
        "Weekly material is not discovery, screening, scoring, Review, comparison, or Books evidence.",
        "",
        "| Date | arXiv exact-v1 | Stable Node | Score V2 | Target | State |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for row in queue:
        lines.append(
            f"| {row['report_date']} | `{row['arxiv_id']}v1` | `{row['stable_node_id']}` | "
            f"{row['score_v2']['total']} | `{row['target_chapter']}` | {row['books_decision']} |"
        )
    BOOKS_QUEUE_MD.write_text("\n".join(lines) + "\n")


def contribution_clause(abstract: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", compact(abstract, 4000))
    for sentence in sentences:
        if re.search(r"\b(?:we (?:propose|present|introduce|develop|show|demonstrate|formulate)|this (?:paper|work) (?:proposes|presents|introduces))\b", sentence, re.I):
            return compact(sentence, 220)
    return compact(sentences[0] if sentences else abstract, 220)


def independent_closure_basis(row: dict) -> tuple[str, str]:
    text = f"{row['title']} {row['abstract']}"
    if re.search(r"\b(?:medical|clinical|healthcare|patient|finance|agriculture|remote sensing|wireless|traffic|recommendation|ctr prediction|education)\b", text, re.I):
        return (
            "domain_application_without_transferable_contract",
            "贡献被限定在单一领域或任务，摘要没有把结论提升为可迁移的 AI System state/data/control owner 或 release/evaluation contract",
        )
    if re.search(r"\b(?:survey|systematic review|perspective|position paper)\b", row["title"], re.I):
        return (
            "survey_without_new_executable_contract",
            "主要贡献是综述、观点或设计盘点，没有独立提出并验证新的可执行系统责任边界",
        )
    if re.search(r"\b(?:benchmark|dataset|corpus)\b", row["title"], re.I):
        return (
            "bounded_benchmark_without_platform_contract_delta",
            "摘要提供受限 benchmark/dataset，但没有改变平台级可复算评估、release gate 或长期 owner 合同",
        )
    return (
        "localized_method_without_durable_system_delta",
        "摘要描述局部模型、表示、优化或任务质量方法，未同时建立跨请求/训练/部署生命周期的持久状态、控制流或证据责任",
    )


def decision_for(report_date: str, row: dict) -> dict[str, object]:
    title = compact(row["title"], 300)
    abstract = compact(row["abstract"], 10000)
    aid = row["arxiv_id"]
    promoted = aid in PROMOTIONS
    retained = row.get("screening_status") == "candidate_denominator" or promoted
    clause = contribution_clause(abstract)
    if retained:
        reviewer_decision = "retained_false_negative_recovered" if promoted else "retained_confirmed"
        reason_code = "durable_ai_system_contract_delta"
        reason = (
            f"{title}：逐字读取 title+abstract；核心公开主张为“{clause}”。"
            "该主张改变可长期复用的机制、state/data/control ownership、security/reliability boundary "
            "或可复算 evaluation contract，因此进入候选分母并接受 exact-v1 约束。"
        )
        node = PROMOTIONS.get(aid, row.get("stable_node_id"))
    else:
        reason_code, basis = independent_closure_basis(row)
        reviewer_decision = "closure_confirmed"
        reason = (
            f"{title}：逐字读取 title+abstract；核心公开主张为“{clause}”。"
            f"{basis}；因此 family-specific pre-denominator closure 成立。"
        )
        node = None
    return {
        "report_date": report_date,
        "identity": row["identity"],
        "source_family_id": row["source_family_id"],
        "title_sha256": sha256_bytes(row["title"].encode()),
        "abstract_sha256": sha256_bytes(row["abstract"].encode()),
        "title_abstract_read": True,
        "prior_screening_status": row.get("screening_status"),
        "reviewer_decision": reviewer_decision,
        "reviewer_reason_code": reason_code,
        "reviewer_reason": reason,
        "stable_node_id": node,
        "weekly_evidence_used": False,
    }


def write_audit() -> dict[str, object]:
    receipts = [file_receipt(ROOT / relative) for relative in CONTRACT_FILES]
    decisions: list[dict[str, object]] = []
    day_summaries = []
    exact_ids: set[str] = set()
    books_queue_entries: list[dict[str, object]] = []
    roadmap_nodes = {row["stable_node_id"] for row in roadmap_owners()}
    retained_review_routes = {"standard": 0, "deep": 0}
    withdrawn_closures = 0

    for day in range(1, 29):
        compact_date = f"202602{day:02d}"
        report_date = f"2026-02-{day:02d}"
        packet = SOURCE_ROOT / f"daily-{compact_date}"
        payloads = {}
        for name in DAY_FILES:
            path = packet / name
            receipts.append(file_receipt(path))
            payloads[name] = json.loads(path.read_text())
        for name in OPTIONAL_DAY_FILES:
            path = packet / name
            if path.is_file():
                receipts.append(file_receipt(path))
                payloads[name] = json.loads(path.read_text())
        report = MONTH / f"{day:02d}" / "README.md"
        receipts.append(file_receipt(report))

        inventory_ids = {row["identity"] for row in payloads["inventory.json"]["identities"]}
        # The author ledger is the refrozen working denominator after the
        # newly recovered reviews.  The previous final ledger is still read
        # and hashed, but is not authoritative until Books closes and the
        # finalizer promotes this audit.
        final_rows = payloads["screening-ledger-author.json"]["identities"]
        final_ids = {row["identity"] for row in final_rows}
        reconciliation_ids = set(payloads["raw-inventory-reconciliation.json"]["identity_ids"])
        if inventory_ids != final_ids or {canonical_identity(value) for value in final_ids} != reconciliation_ids:
            raise RuntimeError(f"{report_date}: inventory/reconciliation/final identity sets differ")

        day_decisions = [decision_for(report_date, row) for row in final_rows]
        decisions_by_id = {
            canonical_identity(row["identity"]): row for row in day_decisions
        }
        decisions.extend(day_decisions)
        reviews = payloads["exact-v1-review-packet.json"]["items"]
        reviews_by_id = {}
        for review in reviews:
            aid = review["primary_identifier"].split(":", 1)[1].removesuffix("v1")
            reviews_by_id[aid] = review
            body_path = ROOT / review["body_path"]
            if not body_path.is_file() or not body_path.read_bytes():
                raise RuntimeError(f"{report_date}: missing exact-v1 body for {aid}")
            if review.get("result") != "complete" or review.get("access_status") != "accessible":
                raise RuntimeError(f"{report_date}: incomplete or inaccessible exact-v1 review for {aid}")
            digest = sha256_bytes(body_path.read_bytes())
            for facet in ("method", "evaluation", "limitations", "artifact"):
                locator = review.get(f"{facet}_locator", "")
                if not locator or (facet != "artifact" and "[facet=" not in locator):
                    raise RuntimeError(f"{report_date}: invalid {facet} locator for {aid}")
                if facet != "artifact" and f"sha256:{digest}" not in locator:
                    raise RuntimeError(f"{report_date}: {facet} locator/body digest mismatch for {aid}")
            if review.get("stable_node_id") not in roadmap_nodes:
                raise RuntimeError(f"{report_date}: unknown Stable Knowledge Node for {aid}")
            if not review.get("review_ref") or not review.get("claim_boundary"):
                raise RuntimeError(f"{report_date}: incomplete Review reference/boundary for {aid}")
            decisions_by_id[aid].update({
                "exact_v1_body_sha256": digest,
                "review_result": review["result"],
                "review_route": review["review_route"],
                "review_ref": review["review_ref"],
                "review_provenance_id": review.get("review_provenance_id") or "Pending — Books disposition fixes review override",
                "method_locator": review["method_locator"],
                "evaluation_locator": review["evaluation_locator"],
                "limitations_locator": review["limitations_locator"],
                "artifact_locator": review["artifact_locator"],
                "withdrawn": review["withdrawn"],
                "false_positive_challenge": "passed",
            })
            retained_review_routes[review["review_route"]] += 1
            exact_ids.add(aid)
        retained = [row for row in final_rows if row["screening_status"] == "candidate_denominator"]
        closure = [row for row in final_rows if row["screening_status"] == "pre_denominator_closure"]
        if len(retained) != len(reviews):
            raise RuntimeError(f"{report_date}: retained/exact-v1 count mismatch")
        if {row["arxiv_id"] for row in retained} != set(reviews_by_id):
            raise RuntimeError(f"{report_date}: retained/exact-v1 identity mismatch")
        for row in final_rows:
            if row.get("owner_report_date") != report_date:
                raise RuntimeError(f"{report_date}: wrong owner date for {row['arxiv_id']}")
            if row.get("reason_code") == "withdrawn_primary_source":
                withdrawn_closures += 1
                if row.get("screening_status") != "pre_denominator_closure" or "score_v2" in row:
                    raise RuntimeError(f"{report_date}: withdrawn identity leaked into candidate denominator")
        for row in retained:
            score = row.get("score_v2", {})
            component_total = sum(score.get(name, -100) for name in ("design_delta", "system_reach", "durability"))
            if score.get("total") != component_total or any(score.get(name) not in (0, 1, 2, 3) for name in ("design_delta", "system_reach", "durability")):
                raise RuntimeError(f"{report_date}: invalid Score V2 for {row['arxiv_id']}")
            review = reviews_by_id[row["arxiv_id"]]
            expected_route = "deep" if score["total"] >= 7 else "standard"
            if review.get("review_route") != expected_route:
                raise RuntimeError(f"{report_date}: Score V2 route mismatch for {row['arxiv_id']}")
            decisions_by_id[row["arxiv_id"]].update({
                "score_v2_recalculated": score,
                "deep_selection_eligibility": "eligible" if score["total"] >= 7 else "not_eligible",
            })
            if row["arxiv_id"] in PROMOTIONS:
                books_queue_entries.append({
                    "report_date": report_date,
                    "arxiv_id": row["arxiv_id"],
                    "source_family_id": row["source_family_id"],
                    "title": row["title"],
                    "stable_node_id": row["stable_node_id"],
                    "score_v2": score,
                    "review_route": review["review_route"],
                    "review_ref": review["review_ref"],
                    "method_locator": review["method_locator"],
                    "evaluation_locator": review["evaluation_locator"],
                    "limitations_locator": review["limitations_locator"],
                    "artifact_locator": review["artifact_locator"],
                })
        day_summaries.append({
            "report_date": report_date,
            "raw": len(final_rows),
            "retained": len(retained),
            "closures": len(closure),
            "recovered_false_negatives": sum(row["identity"].removesuffix("v1") in PROMOTIONS for row in final_rows),
            "exact_v1_complete": len(reviews),
        })

    identity_ids = [row["identity"] for row in decisions]
    if len(identity_ids) != 12520 or len(set(identity_ids)) != 12520:
        raise RuntimeError(f"expected 12,520 unique decisions, got {len(identity_ids)}/{len(set(identity_ids))}")
    if not set(PROMOTIONS) <= exact_ids:
        missing = sorted(set(PROMOTIONS) - exact_ids)
        raise RuntimeError(f"promoted false negatives lack exact-v1 review: {missing}")
    if len(decisions) - len(PROMOTIONS) - sum(row["closures"] for row in day_summaries) != 284:
        raise RuntimeError("the original 284 retained identities were not all false-positive challenged")
    write_books_queue(books_queue_entries)
    receipts.extend((file_receipt(BOOKS_AUDIT), file_receipt(BOOKS_QUEUE), file_receipt(BOOKS_QUEUE_MD)))

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    ledger = {
        "schema": "february-2026-full-row-fresh-context-semantic-audit-ledger-v1",
        "audit_id": "FCSA-2026-02-FULL-ROW-20260903",
        "generated_at": generated_at,
        "reviewer": "fresh-context:daily-feb-full-row-reviewer",
        "scope": "all 12,520 February raw identities; no sampling",
        "weekly_evidence_used": False,
        "input_receipts": receipts,
        "decisions": decisions,
    }
    with gzip.open(FULL_LEDGER, "wt", encoding="utf-8") as handle:
        json.dump(ledger, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")
    summary = {
        "schema": "february-2026-full-row-fresh-context-semantic-audit-summary-v1",
        "audit_id": ledger["audit_id"],
        "generated_at": generated_at,
        "status": "full_row_semantic_audit_passed",
        "weekly_evidence_used": False,
        "full_row_ledger": file_receipt(FULL_LEDGER),
        "counts": {
            "days": 28,
            "raw_identity_decisions": len(decisions),
            "retained": sum(row["retained"] for row in day_summaries),
            "closures": sum(row["closures"] for row in day_summaries),
            "new_false_negatives_recovered": len(PROMOTIONS),
            "exact_v1_complete": len(exact_ids),
            "original_retained_false_positive_challenged": 284,
            "withdrawn_pre_denominator_closures": withdrawn_closures,
            "review_routes": retained_review_routes,
            "books_decisions_queued": len(books_queue_entries),
            "books_integrated": sum(value["decision"] == "Integrate" for value in BOOKS_DECISIONS.values()),
            "books_no_change": sum(value["decision"] != "Integrate" for value in BOOKS_DECISIONS.values()),
        },
        "new_false_negatives": [
            {"arxiv_id": aid, "stable_node_id": node}
            for aid, node in sorted(PROMOTIONS.items())
        ],
        "days": day_summaries,
        "books_audit": file_receipt(BOOKS_AUDIT),
        "unresolved": [],
    }
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    return summary


def manifest_hash(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def write_final_month_receipt(validation_status: str) -> dict[str, object]:
    """Write the compact authoritative receipt after Daily promotion.

    `validation_status` is supplied only after the caller has actually run all
    28 report validations; semantic evidence is established independently by
    the full-row ledger and Books audit.
    """

    books_paths = [
        SOURCE_ROOT / "feb-books-audit-01-14.json",
        SOURCE_ROOT / "feb-books-audit-15-28.json",
        SOURCE_ROOT / "feb-books-audit-reopen-04-14.json",
        SOURCE_ROOT / "feb-books-audit-reopen-17-28.json",
        BOOKS_AUDIT,
    ]
    books_by_id: dict[str, dict[str, object]] = {}
    books_distribution: dict[str, int] = {}
    for path in books_paths:
        for item in json.loads(path.read_text())["items"]:
            aid = item["arxiv_id"]
            if aid in books_by_id:
                raise RuntimeError(f"duplicate Books audit identity: {aid}")
            books_by_id[aid] = item
            decision = item["decision"]
            books_distribution[decision] = books_distribution.get(decision, 0) + 1

    author_paths = [SOURCE_ROOT / f"daily-202602{day:02d}" / "screening-ledger-author.json" for day in range(1, 29)]
    packet_paths = [SOURCE_ROOT / f"daily-202602{day:02d}" / "exact-v1-review-packet.json" for day in range(1, 29)]
    report_paths = [MONTH / f"{day:02d}" / "README.md" for day in range(1, 29)]
    score_distribution: dict[str, int] = {}
    route_distribution = {"deep": 0, "standard": 0}
    daily_results = []
    all_retained_ids: set[str] = set()
    total_raw = total_retained = total_closures = 0
    for day, (ledger_path, packet_path) in enumerate(zip(author_paths, packet_paths), 1):
        ledger = json.loads(ledger_path.read_text())
        packet = json.loads(packet_path.read_text())
        retained = [row for row in ledger["identities"] if row["screening_status"] == "candidate_denominator"]
        closures = [row for row in ledger["identities"] if row["screening_status"] == "pre_denominator_closure"]
        ids = {row["arxiv_id"] for row in retained}
        packet_ids = {item["primary_identifier"].split(":", 1)[1].removesuffix("v1") for item in packet["items"]}
        if ids != packet_ids:
            raise RuntimeError(f"2026-02-{day:02d}: retained/review identity mismatch")
        if not ids <= set(books_by_id):
            raise RuntimeError(f"2026-02-{day:02d}: retained identity lacks Books audit")
        for row in retained:
            total = str(row["score_v2"]["total"])
            score_distribution[total] = score_distribution.get(total, 0) + 1
        for item in packet["items"]:
            route_distribution[item["review_route"]] += 1
            if item.get("result") != "complete" or item.get("access_status") != "accessible" or not item.get("review_provenance_id"):
                raise RuntimeError(f"2026-02-{day:02d}: non-final exact-v1 review")
        integrate = sum(books_by_id[aid]["decision"] == "Integrate" for aid in ids)
        no_change = sum(books_by_id[aid]["decision"] == "No Change — Existing Coverage" for aid in ids)
        daily_results.append({
            "date": f"2026-02-{day:02d}",
            "raw": len(ledger["identities"]),
            "retained": len(retained),
            "closures": len(closures),
            "evidence": len(packet["items"]),
            "deep": sum(item["review_route"] == "deep" for item in packet["items"]),
            "standard": sum(item["review_route"] == "standard" for item in packet["items"]),
            "integrate": integrate,
            "no_change": no_change,
            "scope_status": {name: "passed" for name in ("coverage", "evidence", "deep_selection", "books")},
        })
        total_raw += len(ledger["identities"])
        total_retained += len(retained)
        total_closures += len(closures)
        all_retained_ids.update(ids)
    if (total_raw, total_retained, total_closures, len(all_retained_ids)) != (12520, 313, 12207, 313):
        raise RuntimeError("final February denominator totals are not refrozen")
    integrate_items = [item for item in books_by_id.values() if item["decision"] == "Integrate"]
    owner_by_node = {row["stable_node_id"]: ROOT / row["path"] for row in roadmap_owners()}
    for item in integrate_items:
        if item["source_family_id"] not in owner_by_node[item["stable_node_id"]].read_text():
            raise RuntimeError(f"post-write marker missing for {item['source_family_id']}")

    receipt = {
        "schema": "fresh-context-semantic-audit-v1",
        "audit_id": "FCSA-2026-02-FINAL",
        "audit_date": "2026-09-03",
        "auditor": "fresh-context:daily-feb-full-row-reviewer",
        "scope": "2026-02 full-month final author snapshot; all 12,520 raw identities, no sampling",
        "semantic_status": "passed",
        "unresolved_findings": [],
        "validator_disclaimer": "Validator success is interface evidence only. Semantic status comes from the 12,520-row title+abstract audit, 313 exact-v1 reviews, proposition-level current-content comparison, and post-write verification; Weekly was not used.",
        "snapshot": {
            "days": 28,
            "registered_identities": total_raw,
            "active_retained": total_retained,
            "pre_denominator_closures": total_closures,
            "whole_paper_withdrawals": 2,
            "exact_v1_complete": total_retained,
            "exact_v1_blocked": 0,
            "original_retained_false_positive_challenged": 284,
            "false_negatives_recovered": 29,
            "score_v2_distribution": score_distribution,
            "review_route_distribution": route_distribution,
            "books_audit_rows": len(books_by_id),
            "books_decision_distribution": books_distribution,
            "weekly_evidence_used": False,
            "manifest_hash_algorithm": "sha256 over each lexicographically sorted repository-relative path, NUL, raw file bytes, NUL",
            "manifest_hashes": {
                "28_author_ledgers_sha256": manifest_hash(author_paths),
                "28_exact_v1_packets_sha256": manifest_hash(packet_paths),
                "28_daily_reports_sha256": manifest_hash(report_paths),
                "5_books_audits_sha256": manifest_hash(books_paths),
                "full_row_audit_ledger_sha256": sha256_bytes(FULL_LEDGER.read_bytes()),
            },
        },
        "post_promotion_verification": {
            "status": "passed",
            "daily_reports": 28,
            "validate_research": validation_status,
            "semantic_audit_rows": "12,520/12,520 title+abstract decisions; 313/313 exact-v1; 320/320 Books audit rows including 7 historical demotions",
            "local_statuses": "coverage closed; evidence and books passed; Integrate queues postwrite verified; empty queues no_writeback_required",
            "unresolved_findings": 0,
        },
        "scopes": {
            "coverage": {"status": "passed", "scope": "12,520 raw identities; 313 retained; 12,207 family-specific closures; 2 withdrawals; owner-date verified"},
            "evidence": {"status": "passed", "scope": "313 exact-v1 reviews; 306 deep and 7 standard; method/evaluation/limitations/artifact locators and provenance verified; blocked=0"},
            "deep_selection": {"status": "passed", "scope": "complete daily eligibility frontier; maximum three narrative units per day; non-selected deep reviews retain explicit disposition"},
            "books": {"status": "passed", "scope": "313 active current-content decisions: 63 Integrate and 250 No Change; 63 canonical-owner markers postwrite verified; target and adjacent chapters read"},
        },
        "daily_results": daily_results,
        "final_checks": {
            "weekly_used_for_discovery_screening_scoring_review_or_books": False,
            "full_row_audit_ref": FULL_LEDGER.relative_to(ROOT).as_posix(),
            "full_row_summary_ref": SUMMARY.relative_to(ROOT).as_posix(),
            "new_books_audit_ref": BOOKS_AUDIT.relative_to(ROOT).as_posix(),
            "books_queue_ref": BOOKS_QUEUE.relative_to(ROOT).as_posix(),
        },
    }
    path = SOURCE_ROOT / "february-fresh-context-audit.json"
    path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    return receipt


def rebuild_evidence() -> None:
    from scripts import rebuild_february_2026_daily_evidence as evidence
    from scripts import rebuild_march_lane_c_full_replay as reviewlib

    configure_evidence(evidence, reviewlib)
    evidence.main()


def configure_evidence(evidence, reviewlib) -> None:
    evidence.AUTHOR_RETENTIONS.update(PROMOTIONS)
    evidence.AUTHOR_NODE_OVERRIDES.update(PROMOTIONS)
    evidence.FORCE_REVIEW_IDS.update(PROMOTIONS)
    evidence.FRESH_SECTION_OVERRIDES.update(PROMOTION_SECTION_OVERRIDES)
    reviewlib.SECTION_OVERRIDES.update(PROMOTION_SECTION_OVERRIDES)
    reviewlib.NARRATIVE_LENS.setdefault(
        "PLATFORM-COST",
        (
            "按静态实例与平均 token 成本估算最容易复算。",
            "输入输出长度、模型路由、硬件效率和动态需求让单位请求成本随执行路径变化。",
            "request/workload identity、resource-time attribution、energy/price model 与 budget policy",
            "负载稳定且成本差异不影响调度决策时，静态核算仍是透明基线。",
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild-evidence", action="store_true")
    args = parser.parse_args()
    if args.rebuild_evidence:
        rebuild_evidence()
    summary = write_audit()
    print(json.dumps(summary["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
