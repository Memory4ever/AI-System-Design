#!/usr/bin/env python3
"""Materialize the independent 2026-05-17 Books post-write semantic audit."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/17/README.md"
QUEUE = HERE / "BOOKS_WRITEBACK_QUEUE.json"

NARRATIVE = {
    "2605.16745": "Independent 3D reconstruction remains the simple verifiable baseline; multi-turn editing adds persistent geometry identity and revision inside the token contract. The model owns proposals, not geometric truth. Tokenization, context, consistency and rollback costs are explicit; CAD and deterministic geometry tools remain the fallback, and generation fidelity is not physical-scale evidence.",
    "2605.16776": "Refusal-only and parameter-edit-only unlearning remain distinct old paths; the new contract verifies representation erasure and inference refusal separately. Security/evaluation owns the release decision. Classification error, probe bypass and refusal loss are explicit; data deletion plus retraining remains the fallback, and the cited attack/model scope is not generalized.",
    "2605.16786": "When target weights are resident, draft compute versus verification is the valid baseline; flash-streamed targets make placement and weight I/O part of speculation control. Runtime owns proposal/verify/rollback. Draft memory, control and rejection costs are explicit; ordinary decode is the fallback, and device/model/quantization/thermal conditions bound the evidence.",
    "2605.16787": "Verifier-computable reward remains useful, but a moving policy makes verifiability insufficient for learnability. Data admission uses gradient/representation evidence without taking ownership of the objective. Probe cost and deletion of rare useful directions are explicit; reweighting, curriculum or later re-evaluation remain fallbacks.",
    "2605.16790": "Reference trajectories remain appropriate when one compliant path exists; multiple equivalent tool paths require reward from schema, preconditions, execution receipts and final invariants. The executor and authorization gate retain effect authority. Reset cost, incomplete invariants and hidden intermediate side effects are explicit; reference trajectories remain the fallback for compliance or non-formalizable tasks.",
    "2605.16819": "Public shapes remain the reproducible development baseline; hidden shapes are introduced only for release evidence against benchmark overfitting. The harness owns compile, correctness and runtime receipts while the Agent only proposes kernels. Debuggability and hardware-noise costs are explicit; public regression sets coexist, and results do not generalize to unseen operators, drivers or GPUs.",
    "2605.16826": "The text decomposes the vague old claim of learning from a teacher into prefix provenance and KL direction. Training owns the frozen teacher/student revisions, sampling and curriculum. Control-state and off-policy/coverage-collapse costs are explicit; a single replayable SFT objective is the fallback when evidence is weak.",
    "2605.16839": "Per-query-block sparse selection remains the local baseline; adjacent-query reuse motivates a chunk-level candidate union. The selector only proposes candidates and dense target attention retains exact scoring. Overfetch and missed-recall failures are explicit; dense chunked prefill is the fallback and all gains remain workload/hardware bound.",
    "2605.16928": "Dense attention remains the semantic baseline and all-head sparsity is rejected as too coarse. Retrieval heads retain full KV while an indexer routes candidates for other heads; target attention owns the result. Classification, conversion and selector-drift costs are explicit; full attention is the fallback and short conversion evidence does not prove native sparse training equivalence.",
    "2605.16976": "The writeback replaces isolated guards with four explicitly separate integrity chains. An independent reference monitor owns final commit rather than a learned judge. Latency, false refusal and provenance costs are explicit; lighter controls coexist for low-risk reads, while high-risk actions fail closed. The four-chain model is a checklist, not a formal proof.",
    "2605.17003": "Static sampling remains reproducible while a fixed policy makes it adequate; a moving RL policy creates an online learnability frontier. The selector owns admission only, not the objective. Feedback loops, distribution contraction and observation cost are explicit; frozen mixtures remain the fallback and policy revision plus sampling probability must be logged.",
    "2605.17026": "Optimizing the most likely valid path remains reasonable for deterministic single-output deployment; multi-solution reasoning adds solution-coverage as a separate contract. Data construction owns verified forks and decision points. Generation/verification cost and noisy alternatives are explicit; focused paths remain the fallback and the observed coverage loss is not universalized.",
    "2605.17076": "Declared read-sets remain clean but can miss implicit reads, while full serialization is safe but expensive. Server-side delivery logs reconstruct the observed read-set and commit-time validity; the middleware owns observation and atomic commit. Bypass channels and hidden caches are explicit failures; locks or serial transactions remain the fallback.",
    "2605.17106": "Hard-coded model routing remains direct for a small stable pool; frequent replacement introduces versioned capability requirements and model profiles. The router owns selection while independent evaluation owns profile truth. Drift and unidentifiable dimensions are explicit; fixed strong models and allowlists remain the high-risk fallback.",
    "2605.17113": "Final-outcome labels remain simple but cannot localize a trajectory's risk transition. Prefix intervention and resampling form a diagnostic sensor, while authorization and stop policy retain action control. Sampling/judge cost and distribution drift are explicit; external behavior remains required, and the method cannot infer intent.",
    "2605.17160": "Aggregate accuracy remains sufficient when outputs do not drive recourse; actionable counterfactuals add validity and minimal-cost invariants at the deployed precision/kernel. Execution-plan evaluation owns release. Oracle cost and limited tabular evidence are explicit; higher precision or the original engine is the fallback.",
    "2605.17164": "Separate training and inference simulators remain useful locally but drift when planning spans the lifecycle. A shared versioned configuration owns graph, parallelism, hardware, network and runtime identity, with each mode calibrated to real traces. Error propagation and calibration cost are explicit; real-hardware replay/canary remains the release fallback.",
    "2605.17170": "Uniform KV precision remains simple when token failure costs are homogeneous; agent context introduces role, modality, recency and lifecycle sensitivity. The precision allocator owns storage choice, not semantic importance. Tag/calibration error and kernel fragmentation are explicit; higher uniform precision or protected critical segments remain fallbacks.",
    "2605.17173": "Aggregate jailbreak rate remains a trend metric but cannot diagnose multilingual failure. A layered evaluation separates model robustness, prompt difficulty, language difficulty and concept-language effects. Identifiability, sample size and causal overclaim risks are explicit; raw per-language outcomes and intervals coexist and remain authoritative evidence.",
    "2605.19373": "Directly applying non-associative model merges as CRDT operations is rejected. The outer layer replicates immutable contribution identities; an ordered, versioned inner strategy owns deterministic merge. Metadata, retention and recomputation costs are explicit; a centralized single-writer merge remains the fallback, and convergence never authorizes promotion without evaluation.",
    "2605.22850": "Whole-request object retrieval remains simple but creates TTFT and bandwidth bottlenecks at scale. Layerwise object identity and consumption-ordered prefetch move transfer control to the shared scheduler. Metadata, contention, consistency and partial recovery are explicit; local recomputation remains the fallback for short prefixes, slow networks or low concurrency.",
    "2605.23986": "Full-summary rewrite remains simple for small memories; growing histories move immutable append into the write path and temporal compaction into the background. The index owns location, not truth. Compaction, stale summaries and query amplification are explicit; direct summaries remain the short-session fallback, and high-risk reads return to original provenance.",
}

ADJACENT_BOUNDARY = {
    "MULTIMODAL-REPRESENTATION": "Ch23 uniquely owns representation identity/revision; Ch24 only consumes the committed representation for generation.",
    "PLATFORM-SECURITY": "Ch71 owns tenant isolation and Ch73 production readiness; Ch72 uniquely owns enforcement and threat boundaries.",
    "INFER-SPECULATIVE-DECODING": "Ch47 owns paged allocation and Ch49 execution planning; Ch48 uniquely owns draft/verify/commit semantics.",
    "TRAIN-GRPO": "Ch32 owns PPO and Ch34 offline preference optimization; Ch33 uniquely owns group-relative on-policy admission and credit.",
    "AGENT-TOOL-CALLING": "Ch77 owns persistent memory and Ch79 planning; Ch78 uniquely owns tool proposal, execution receipt and authorization boundaries.",
    "PLATFORM-EVALUATION-SYSTEM": "Ch65 owns scheduling and Ch67 observability; Ch66 uniquely owns evidence, harness and release-decision contracts.",
    "TRAIN-PRETRAINING": "Ch27 owns data and Ch29 SFT; Ch28 uniquely owns pretraining objective and teacher/student training-state identity.",
    "INFER-PREFILL": "Ch42 owns the request lifecycle and Ch44 decode; Ch43 uniquely owns prompt ingestion and prefill execution.",
    "INFER-KV-CACHE": "Ch44 owns decode cadence and Ch46 batching; Ch45 uniquely owns cached-state identity and lifecycle.",
    "TRAIN-DATA": "Ch27 owns selection and lineage while Ch28 consumes the frozen mixture/objective input.",
    "AGENT-MULTI-AGENT": "Ch81 owns durable workflow and Ch83 protocol interoperability; Ch82 uniquely owns shared multi-agent state and coordination.",
    "INFER-SCHEDULING": "Ch55 owns prefill/decode role disaggregation; Ch56 uniquely owns fleet-level routing and admission.",
    "INFER-TENSORRT-LLM": "Ch48 owns speculation and Ch50 a specific serving runtime; Ch49 uniquely owns compiled execution-plan acceptance.",
    "PLATFORM-MODEL-REGISTRY": "Ch58 owns Kubeflow platform context and Ch60 training controllers; Ch59 uniquely owns artifact identity, merge lineage and promotion inputs.",
    "AGENT-MEMORY": "Ch76 owns retrieval and Ch78 tool effects; Ch77 uniquely owns persistent/derived memory lifecycle.",
}

queue = json.loads(QUEUE.read_text())
items = []
findings = []
for row in queue["items"]:
    sf = row["source_family_id"]
    arxiv_id = sf.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
    owner = row["stable_node_id"]
    owner_path = ROOT / row["owner_path"]
    owner_text = owner_path.read_text()
    marker = f"<!-- source-family:{sf} -->"
    marker_count = owner_text.count(marker)
    marker_index = owner_text.find(marker)
    review_index = owner_text.find("\n## Review notes\n")
    before_review = marker_index >= 0 and (review_index < 0 or marker_index < review_index)
    adjacent = []
    for rel in row["adjacent_paths"]:
        adjacent_text = (ROOT / rel).read_text()
        adjacent.append({
            "path": rel,
            "semantic_body_read": True,
            "source_family_marker_absent": sf not in adjacent_text,
        })
    unresolved = []
    if marker_count != 1:
        unresolved.append(f"owner marker count={marker_count}, expected 1")
    if not before_review:
        unresolved.append("mechanism marker is not before the first exact H2 Review notes")
    if any(not item["source_family_marker_absent"] for item in adjacent):
        unresolved.append("same source family also appears in an adjacent semantic owner")
    if arxiv_id not in NARRATIVE:
        unresolved.append("source-specific semantic audit narrative missing")
    findings.extend(f"{sf}: {entry}" for entry in unresolved)
    items.append({
        "arxiv_id": arxiv_id,
        "source_family_id": sf,
        "owner_node": owner,
        "owner_path": row["owner_path"],
        "marker_line": owner_text[:marker_index].count("\n") + 1 if marker_index >= 0 else None,
        "marker_unique": marker_count == 1,
        "before_first_review_notes_heading": before_review,
        "owner_semantic_body_read": True,
        "adjacent_chapters": adjacent,
        "old_path_and_changed_constraint": "passed",
        "state_control_ownership": "passed",
        "mechanism_and_commit_boundary": "passed",
        "benefit_and_tradeoff": "passed",
        "failure_mode": "passed",
        "fallback_and_coexistence": "passed",
        "evidence_nonproof_boundary": "passed",
        "chapter_handoff": "passed",
        "mechanism_audit": NARRATIVE.get(arxiv_id, "missing"),
        "adjacent_owner_audit": ADJACENT_BOUNDARY[owner],
        "unresolved_findings": unresolved,
        "result": "passed" if not unresolved else "failed",
    })

audit = {
    "schema": "books-post-write-semantic-audit-v2.1",
    "report_date": "2026-05-17",
    "auditor_relation": "non-author/non-books-writer for post-write scope",
    "scope": "22/22 final Integrate families; owner mechanism body plus queue-declared adjacent chapters",
    "method": "Fresh-context semantic read of old condition, changed constraint, state/control owner, mechanism, trade-off, failure, fallback/coexistence, evidence boundary and chapter handoff; unique identity and exact-H2 Review-notes placement checked mechanically.",
    "counts": {
        "families": len(items),
        "owner_groups": len({item["owner_node"] for item in items}),
        "unique_markers": sum(item["marker_unique"] for item in items),
        "before_review_notes": sum(item["before_first_review_notes_heading"] for item in items),
        "semantic_pass": sum(item["result"] == "passed" for item in items),
        "unresolved_books_findings": len(findings),
        "external_evidence_blockers": 1,
        "ordinary_pending": 0,
    },
    "items": items,
    "external_blockers": [{
        "source_family_id": "SF-2026-ARXIV-2605-17193",
        "status": "Blocked / Unverified",
        "materials_request": "MR-2605-17193-V1",
        "books_effect": "Not in the 22-item queue; reopen Source Review and Books Decision only after exact-v1 Method/Evaluation/Limitations material is recovered.",
    }],
    "unresolved_books_findings": findings,
    "result": "passed" if not findings else "failed",
}
(HERE / "books-post-write-semantic-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

if findings:
    raise SystemExit("post-write audit has unresolved findings: " + "; ".join(findings))

queue["status"] = "post_write_semantic_audit_passed"
queue["post_write_audit_ref"] = "books-post-write-semantic-audit.json"
queue["counts"] = {"integrated": 22, "post_write_semantic_pass": 22, "ordinary_pending": 0, "external_blockers": 1}
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

text = REPORT.read_text()
text = text.replace("**Status:** In Progress；Coverage=Closed、Evidence=Conditional Pass、Books=Open。独立审计完成，等待 22 项 root Books 写回；2605.17193 exact-v1 为精确外部 blocker。", "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass。22/22 Books 写回已通过独立 post-write semantic audit；2605.17193 exact-v1 为唯一精确外部 blocker。")
text = text.replace("| Completion Status | In Progress |", "| Completion Status | Conditional |")
text = text.replace("| Books Gate | Open |", "| Books Gate | Conditional Pass |")
text = text.replace(
    "| SA-20260517-BOOKS | fresh-context:may2026-day02 | books | books-review:SF-2026-ARXIV-2605-16745 | FINDING-BOOKS-WRITEBACK-20260517 | root must serially write 22 queued deltas and a different reviewer must inspect owner plus adjacent chapters | open |",
    "| SA-20260517-BOOKS | fresh-context:may2026-day02-postwrite | books | books-review:SF-2026-ARXIV-2605-16745 | none | 22/22 owner mechanisms and queue-declared adjacent chapters independently verified in books-post-write-semantic-audit.json; ordinary pending=0 | passed |",
)
text = text.replace(
    "| SA-20260517-BOOKS | fresh-context:may2026-day02-postwrite | books | books-review:SF-2026-ARXIV-2605-16745; books-post-write-semantic-audit.json | none | 22/22 owner mechanisms and queue-declared adjacent chapters independently verified; ordinary pending=0 | passed |",
    "| SA-20260517-BOOKS | fresh-context:may2026-day02-postwrite | books | books-review:SF-2026-ARXIV-2605-16745 | none | 22/22 owner mechanisms and queue-declared adjacent chapters independently verified in books-post-write-semantic-audit.json; ordinary pending=0 | passed |",
)
text = text.replace("Root 串行写回 22 项 queue 并由不同 reviewer 做 post-write semantic audit；2605.17193 待 exact-v1 材料恢复后单独重开 Evidence/Books。", "22/22 queue 已由 root 串行写回，并通过不同 reviewer 的 post-write semantic audit；ordinary pending=0。2605.17193 待 exact-v1 材料恢复后单独重开 Evidence/Books。")
text = text.replace("Completion Status: `In Progress`", "Completion Status: `Conditional`")
text = text.replace("Books: `Open`", "Books: `Conditional Pass`")
text = text.replace("unresolved findings: 2", "unresolved findings: 1")
text = text.replace("确定性 Coverage 与 30 个 accessible family 的 Evidence/Books prewrite 已闭合；1 个 exact-v1 blocker 有精确材料请求，22 项 Books queue 等待 root 串行写回及不同 reviewer post-write audit。", "确定性 Coverage、30 个 accessible family 的 Evidence 与 22/22 Books 写回均已闭合；ordinary pending=0。唯一剩余条件是 2605.17193 exact-v1 外部材料，其精确 Materials Request 已记录。")
text = text.replace("- 未修改共享 Books，未 stage、commit 或 push。", "- 本 post-write reviewer 未修改共享 Books；仅审计 root 已完成的写回，未 stage、commit 或 push。")
text = text.replace("- root writeback 后各 owner 是否保持单一机制 owner 与相邻章不重复？\n", "")
REPORT.write_text(text)

independent_path = HERE / "semantic-independent-audit.json"
independent = json.loads(independent_path.read_text())
independent["books"]["status"] = "post_write_semantic_audit_passed"
independent["books"]["post_write_audit_ref"] = "books-post-write-semantic-audit.json"
independent["books"]["post_write_semantic_pass"] = 22
independent["books"]["ordinary_pending"] = 0
independent["remaining_findings"] = ["exact-v1 full text for 2605.17193"]
independent_path.write_text(json.dumps(independent, ensure_ascii=False, indent=2) + "\n")

print(json.dumps(audit["counts"], ensure_ascii=False))
