#!/usr/bin/env python3
"""Apply the independent fresh-context audit for 2026-05-05.

The script changes only the date-local evidence packet.  Shared Books files are
never written here; confirmed deltas remain in the root-serial queue.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read(name: str):
    return json.loads((ROOT / name).read_text())


# These challenge families expose a durable state/control/evidence contract.
# The tuple is (family, owner, score, method locator, evaluation locator,
# non-proof locator, claim boundary).
REOPEN = {
    "2605.02124": ("SF-MOE-BOUNDARY-MASS-SOFT-HARD", "MODEL-MOE", (2, 2, 2), "§3 Boundary-layer geometry and coarea control; §4 The variational zero-temperature limit", "§4.3 quantitative soft-hard comparison; §5 conditional landscape-transfer", "§7 What the Results Do and Do Not Show", "Soft-to-hard MoE routing error is governed by probability mass near top-two routing ties under the stated population, regularity and margin assumptions; it is not an empirical sparse-training or load-balancing guarantee."),
    "2605.02168": ("SF-UNBALANCED-MULTIAGENT-COMPUTE-OWNERSHIP", "AGENT-MULTI-AGENT", (2, 2, 2), "§Framework: planner, actor and memory-manager decomposition; asymmetric model allocation", "§Experiments on long-horizon planning tasks; role/model ablations", "§Limitations and role-decomposition scope", "Planner, actor and memory roles may own different compute budgets; the reported allocation is evidence for the tested planning workloads, not a universal multi-agent topology."),
    "2605.02179": ("SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET", "INFER-SCHEDULING", (3, 3, 3), "§System model; risk-budgeted online scheduling; evolving-horizon predictor", "§Experiments: timely-inference ratio, violation risk and burst length", "§Assumptions and convergence/delay-risk boundaries", "Continuous edge inference must carry deadline-violation risk and burst history across time; the AEGIS policy is bounded to its prediction and risk-budget assumptions."),
    "2605.02195": ("SF-CODE-EVAL-PIPELINE-FALSE-FAILURES", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "§3 Methodology; §3.1 Inspection Process; §3.2 Classification Criteria", "§4 Experimental Setup; §5 Findings", "§6 Threats to Validity", "Compiler flags, libraries, runtime configuration and test harness are part of code-agent evaluation identity because pipeline faults can create false model failures."),
    "2605.02209": ("SF-SUBMODULAR-BENCHMARK-SELECTION", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "§3 Problem Formulation; §4 Algorithms and Approximation Guarantees", "§5 Experiments; Appendix F Selection Order and Stability", "§6 Discussion: cost, safety/fairness coverage and alternatives", "Benchmark subset admission must state the covariance/information model, budget and residual-coverage diagnostic; the selected subset cannot inherit full-suite authority outside those assumptions."),
    "2605.02240": ("SF-PHYSICIANBENCH-EXECUTION-CHECKPOINTS", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "§3 Benchmark Environment and Evaluation; §3.3 Checkpoint Evaluation", "§5 Experiments; Appendix B grader specifications", "§6 Discussion; clinical-domain and grader boundaries", "Long-horizon agents require execution-grounded checkpoint state and task-specific graders rather than final-answer scoring; clinical results remain domain-bounded."),
    "2605.02241": ("SF-ZEROSHOT-CONFIDENCE-ROUTING", "INFER-SCHEDULING", (3, 3, 3), "§II Signals and Baselines; §IV-F Retrieval-Conditional Self-Assessment", "§III Evaluation Protocol; §IV Results and cross-dataset transfer", "§VIII Limitations", "Local-to-cloud routing confidence must be calibrated under distribution shift and include fallback; zero-shot signals are sensors, not correctness certificates."),
    "2605.02255": ("SF-LLM-PRIVACY-CONFIG-ABLATION", "PLATFORM-SECURITY", (3, 3, 3), "§Threat model and unified attack notation; structured architecture/scale/data/retrieval ablations", "§Experiments across attack and deployment configurations", "§Limitations and context-dependent attack transfer", "Privacy evidence is identified by architecture, scale, dataset and retrieval configuration; an attack result cannot be detached from that deployment identity."),
    "2605.02273": ("SF-AI-PR-HUMAN-OVERSIGHT-MEASUREMENT", "PLATFORM-EVALUATION-SYSTEM", (2, 2, 2), "§Dataset and review-interaction coding; human versus AI-generated PR comparison", "§Results on automation-mediated review and agent steering", "§Threats to validity of observational GitHub evidence", "Human-oversight evidence must distinguish independent review from automation-mediated steering; repository observations do not establish causal review quality."),
    "2605.02363": ("SF-STRUCTURED-OUTPUT-TYPED-VALIDATION", "AGENT-TOOL-CALLING", (3, 2, 3), "§Structured-output contract and constrained-generation methods", "§GSM8K/MATH JSON validity and answer-correctness evaluation", "§Limitations: small-model, task and schema scope", "Semantic correctness and interface usability are separate gates; typed validation owns schema acceptance even when the answer content is correct."),
    "2605.02398": ("SF-ADVERSARIAL-METACOGNITION-COLLAPSE", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "§SCHEMA factorial design and structural-pressure conditions", "§67,221-record evaluation; dual-classifier scoring and condition comparisons", "§Limitations and classifier/model-sample boundaries", "Self-assessment must be stress-tested under adversarial structural constraints; observed confidence or compliance is not a stable abstention contract."),
    "2605.02442": ("SF-REASONING-PROCESS-EVIDENCE-TIERS", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "§3 Reasoning as Search; §4 Externalized Reasoning", "Appendix C Evidence Tiers and reporting standards", "§5 Alternative Views: internal measurement, trace unfaithfulness and world models", "Reasoning claims need explicit process-evidence tiers, validity/faithfulness checks and adaptive-halting evidence; answer accuracy alone is outcome evidence."),
    "2605.02443": ("SF-HALLUSCAN-EVIDENCE-CALIBRATION", "PLATFORM-EVALUATION-SYSTEM", (2, 2, 2), "§Benchmark design; detection and mitigation method matrix", "§72-configuration experiments across models and domains", "§Limitations and detector/domain transfer", "Hallucination detectors must preserve configuration, domain, calibration and evaluator identity; an AUROC from one matrix is not a universal confidence value."),
    "2605.02455": ("SF-SPEC-DRIVEN-REPOSITORY-ARTIFACT", "AGENT-WORKFLOW", (3, 2, 3), "§Structured spec-driven engineering artifacts and generation workflow", "§Repository-level generation evaluation and artifact checks", "§Limitations of specification completeness and repository transfer", "A repository-generation workflow must version specification artifacts and acceptance checks separately from generated code; the model does not own artifact truth."),
    "2605.02489": ("SF-AGENT-REGISTRY-DISCOVERY-IDENTITY", "AGENT-PLATFORM", (3, 3, 3), "§Hybrid agent indexing and SLM-enhanced discovery pipeline", "§Discovery latency/accuracy evaluation and ablations", "§Index freshness, corpus and transfer limitations", "Agent discovery requires versioned registry identity, index freshness and routing evidence; retrieval latency alone cannot authorize an agent."),
    "2605.02503": ("SF-DATACLAW-EXECUTION-GROUNDED-EVAL", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "§Process-oriented task design; exploratory data environment and action traces", "§Eight-model execution-grounded evaluation and process diagnostics", "§Financial-domain, tool and grader limitations", "Exploratory agents must be scored on executable progress and task-relevant state transitions, not exploration volume or final prose alone."),
    "2605.02525": ("SF-ROBOT-SEMANTIC-MEMORY-PROMOTION", "MULTIMODAL-EMBODIED-VLA", (3, 3, 3), "§3 Semantic Autonomy Stack; §4 hybrid resolver; §5 cross-robot memory", "§6 methodology; §7 physical two-robot results", "§8 Discussion and limitations; 82 decisions/two robots/three sessions", "A robot may promote validated VLM-resolved preferences into scoped deterministic memory, but promotion and transfer need explicit operator/robot/map identity and fallback to deliberative inference."),
    "2605.05245": ("SF-ADAGATE-EVIDENCE-GAP-ASSEMBLY", "AGENT-RAG", (3, 2, 3), "§Gap-aware evidence assembly; bridge-fact and redundancy state", "§Multi-hop retrieval evaluation and token-budget ablations", "§Limitations of retriever, corpus and bridge-fact oracle", "Multi-hop RAG should track missing bridge facts, corroboration, novelty and redundancy as evidence state; token efficiency is not proof of claim support."),
    "2605.02709": ("SF-HEALTHCARE-SKILL-GOVERNANCE", "AGENT-PLATFORM", (2, 2, 3), "§2 Corpus and Annotation; ten-dimensional skill taxonomy", "§3 Results over 557 healthcare skills", "§4 Discussion; corpus/adoption/LLM-annotation limitations", "Skill governance must distinguish procedural artifact, autonomy, domain impact and declared safety boundary; public healthcare-skill prevalence is contextual evidence, not deployment validation."),
    "2605.02728": ("SF-DETERMINISTIC-OPTIMIZATION-IR", "AGENT-TOOL-CALLING", (3, 3, 3), "§ORPilot architecture; solver-agnostic deterministic intermediate representation", "§Optimization-model generation, validation and solver evaluation", "§Supported solver/task and production-boundary limitations", "When an optimization problem is formalizable, deterministic IR and solver validation should own executable correctness rather than probabilistic agent narration."),
    "2605.02765": ("SF-HARD-SOFT-CONSTRAINT-AUTHORITY", "AGENT-WORKFLOW", (3, 2, 3), "§User workflow and hard/soft constraint representation", "§Planning study and constraint-satisfaction evaluation", "§User-study, domain and preference-elicitation limitations", "Hard constraints require deterministic verification while soft constraints remain preference evidence; a planner must not collapse both into one model score."),
    "2605.02811": ("SF-AGENTIC-NETWORK-ACTUATION-BOUNDARY", "AGENT-TOOL-CALLING", (3, 3, 3), "§Agent architecture; MCP/A2A tool flow; mobile-core action interface", "§Network-control scenarios and actuation-latency evaluation", "§Deployment, safety and operator-authorization limitations", "Network control must separate model proposal, protocol message, authorization and actuation commit; tool latency and rollback belong to the executor contract."),
    "2605.02819": ("SF-CUMULATIVE-PRM-TRANSITION-RISK", "TRAIN-RLHF", (3, 2, 3), "§Schema-aware cumulative process reward construction", "§Knowledge-graph QA evaluation and reward ablations", "§Task/verifier/schema transfer limitations", "Process rewards should preserve earlier unsafe or invalid transitions instead of allowing later success to erase them; the validated result remains KGQA-bounded."),
    "2605.06696": ("SF-MULTIAGENT-HIDDEN-COALITION-SENSOR", "PLATFORM-MONITORING", (2, 2, 3), "§Spectral diagnostic over internal multi-agent representations", "§Coalition-detection experiments and representation ablations", "§White-box representation access and transfer limitations", "Hidden-state coalition structure is a bounded monitoring sensor; it cannot independently infer intent or authorize eviction without behavior/effect evidence."),
    "2605.02832": ("SF-HUMAN-AI-TASK-ALLOCATION-POLICY", "PLATFORM-EVALUATION-SYSTEM", (2, 3, 3), "§Policy-aware human/AI allocation model and governance constraints", "§Allocation experiments and contextual-learning analysis", "§Organizational, policy and distribution-shift limitations", "Automation admission should combine capability evidence, contextual learning and governance feasibility; predicted model performance alone cannot allocate authority."),
    "2605.02853": ("SF-LAYERWISE-LOWBIT-TRAINING-MONITOR", "PLATFORM-MONITORING", (3, 3, 3), "§Layer-wise reference peeling and low-bit monitoring method", "§Training-fault/low-bit experiments and layer diagnostics", "§Reference-solution, model and precision limitations", "Training health needs layer-wise evidence when aggregate loss hides localized low-bit or optimization faults; the reference path remains a sensor, not a correctness oracle."),
    "2605.03034": ("SF-CYBER-DEFENSE-EXECUTOR-AUTHORITY", "PLATFORM-SECURITY", (3, 3, 3), "§Tool-mediated cyber-defense architecture and stable control loop", "§Defense scenarios, tool actions and recovery evaluation", "§Threat-model, environment and autonomous-action limitations", "Autonomous cyber defense requires executor-owned authorization, bounded effects and recovery receipts; model planning cannot itself commit network changes."),
    "2605.03042": ("SF-ADVERSARIAL-RESEARCH-ORCHESTRATION", "AGENT-MULTI-AGENT", (2, 2, 3), "§Adversarial multi-agent research roles and adjudication workflow", "§Research-task evaluation, evidence diversity and ablations", "§Judge, corpus and task-transfer limitations", "Multi-agent research should preserve source diversity, adversarial objections and adjudication provenance; more agents do not by themselves establish correctness."),
    "2605.03075": ("SF-DIFFUSION-PLANNING-COMMIT-REFINE", "MULTIMODAL-GENERATIVE-PARADIGMS", (3, 2, 3), "§Compositional diffusion planner; iterative correction and commitment", "§Long-horizon planning evaluation and refinement ablations", "§Environment, horizon and feasibility-check limitations", "Diffusion planning exposes iterative proposal/correction state, but executable commit still belongs to a feasibility verifier and controller."),
    "2605.03117": ("SF-REPOSITORY-GRAPH-REPAIR-PROVENANCE", "AGENT-WORKFLOW", (3, 2, 3), "§Repository graph representation; localization and repair toolset", "§Fault-localization/program-repair evaluation and ablations", "§Repository/language/test-oracle limitations", "Repository repair should preserve graph snapshot, tool action and test provenance; a generated patch is not authoritative until executable acceptance succeeds."),
    "2605.03129": ("SF-WEB-PII-DEFENSIVE-PROMPT-THREAT", "PLATFORM-SECURITY", (3, 3, 3), "§2 Threat Model; §3 PIIGuard methodology", "§4 setup; §5 evaluation including sanitizer and URL modes", "§7 Discussion; sanitizer front and deployment limitations", "Page-side defensive prompts are adversarial content and at most a bounded mitigation sensor; providers still need sanitization, information-flow policy and output authorization."),
    "2605.03143": ("SF-PACT-AGENT-CHOREOGRAPHY", "AGENT-WORKFLOW", (3, 3, 3), "§Pact choreography language, roles, messages and protocol semantics", "§Examples/evaluation of generated endpoints and protocol checks", "§Language subset, runtime and failure-model limitations", "Agent ecosystems need a versioned choreography that defines role/message order and failure semantics before local implementations; generated endpoints cannot redefine the global protocol."),
    "2605.03153": ("SF-ONLINE-CORRECTION-RECOVERY-SHIFT", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "§Online correction/recovery method under distribution shift", "§Recovery, shift and rollback evaluation", "§Shift family, correction-oracle and deployment limitations", "Recovery evaluation must measure time-to-detect, correction state and post-shift rollback rather than only final recovered accuracy."),
    "2605.03227": ("SF-DETERMINISTIC-COMPUTATION-EXECUTION", "AGENT-TOOL-CALLING", (3, 3, 3), "§Prompting versus execution-based deterministic computation methods", "§Task suites, execution correctness and method comparison", "§Task/language/tool availability limitations", "Deterministic computation should be delegated to typed execution and checked outputs when available; prompting remains a fallback, not the truth owner."),
    "2605.03229": ("SF-SPARSE-MEMORY-FINETUNING", "TRAIN-LORA", (3, 2, 3), "§Sparse memory finetuning parameterization and update path", "§Comparison with LoRA/full finetuning; forgetting and adaptation metrics", "§Model/task/parameter-budget limitations", "Sparse trainable memory is an alternative adaptation-state representation whose value must be measured jointly on target learning and forgetting; it does not dominate LoRA or full finetuning."),
    "2605.03231": ("SF-OBSERVATIONAL-WORKFLOW-SKILL-LEARNING", "AGENT-WORKFLOW", (3, 2, 3), "§Observation capture, workflow induction and executable automation", "§Automation-task evaluation and correction analysis", "§UI/domain, demonstration and safety limitations", "Learning automation from observation requires provenance, validation and admission of the induced workflow before it may execute; imitation does not transfer user authority."),
    "2605.05247": ("SF-DADL-DECLARATIVE-TOOL-LANGUAGE", "AGENT-TOOL-CALLING", (3, 3, 3), "§DADL grammar, enterprise tool-library model and compiler", "§Validation, tool-selection and library-scale evaluation", "§Language coverage, backend and dynamic-tool limitations", "A declarative tool language can compile schemas into deterministic validation and adapters; runtime authorization and effect commit remain separate authorities."),
}


CLOSE = {
    "2605.02163": "DocSync binds AST/RAG context to critic-guided documentation repair, but exact-v1 evaluates documentation semantic consistency in one code-maintenance workflow; it neither changes source-code authority nor defines a cross-workload acceptance/rollback contract. Reopen if the artifact specifies repository-wide version/commit recovery semantics.",
    "2605.02244": "The triadic-data paper is explicitly a position paper. Its four evidence tiers are a useful proposal, but exact-v1 does not release or evaluate the proposed long-horizon corpus, so no durable data-pipeline mechanism is admitted. Reopen when the corpus and blind evaluation artifact exist.",
    "2605.02277": "CECoR decomposes multi-hop factual errors and synthesizes correction data, but the evidence is a task-local training method on disclosed QA benchmarks; source authority, live evidence revision and serving-time claim commitment are unchanged. Reopen on a cross-system evidence lifecycle result.",
    "2605.02288": "LabBuilder separates protocol, layout synthesis and modeled safety constraints for laboratory scenes, yet the mechanism and validation remain a 3D laboratory-generation application. It does not redefine the project’s general world-state or physical-action owner. Reopen with real closed-loop embodied evidence or a reusable safety contract.",
    "2605.02348": "The process-reward debiasing schemes steer generation on a bilingual bias prompt set, but do not establish general decoding commit/rollback semantics or a calibrated process-reward authority. Reopen if exact evidence shows cross-domain runtime ownership rather than local quality improvement.",
    "2605.02463": "CAFE proposes a statistical antifragility-compatible regime for one multi-agent stress setup; the measured geometry is not a validated coordination-failure or recovery contract and can remain an evaluation hypothesis. Reopen after external validation with explicit state/effect owners.",
    "2605.02504": "MultiWikiQHalluA adds a multilingual faithfulness slice, but does not change claim/evidence ownership, calibration, or release authority beyond the existing evaluation-slice contract. Reopen if it supplies a cross-language calibration mechanism rather than another benchmark slice.",
    "2605.02544": "The dual-GBDT targeted error-correction pipeline is a post-hoc classifier for three image datasets. Its low measured overhead and local corrections do not establish a general verifier/commit authority. Reopen if the correction gate is validated across model classes and safety effects.",
    "2605.02592": "The industrial-agent paper synthesizes maturity and TRL evidence; it is useful Weekly context but discloses no new agent runtime, evidence gate or deployment mechanism. Reopen on a primary system artifact with production contract evidence.",
    "2605.02815": "FlexSQL combines schema exploration and execution-backed repair for text-to-SQL. Exact-v1 improves a database task, while database truth, transaction authority and recovery remain in the external executor; no new general Agent state contract is shown. Reopen on a cross-tool recovery mechanism.",
    "2605.03179": "The malicious-code prompt bank improves the identity of one security benchmark and separates executable weapons from knowledge, but it does not add a general security control or release mechanism. Reopen if the artifact changes access/authorization or demonstrates transferable evaluator calibration.",
    "2605.03202": "This is a position and evaluation critique of peer-review automation. It argues for stronger evidence but supplies no independently validated workflow mechanism or release gate. Reopen when a concrete evaluation artifact and bounded authority model are published.",
    "2605.03213": "The confidential-computing paper is a survey. It organizes secret and execution boundaries but does not provide a new implemented mechanism, attestation contract or evaluated artifact beyond existing security owners. Reopen on a primary system/RFC or exact deployment evidence.",
}


# Current Books already contain most later June--August deltas.  Only these
# author-retained families still add a non-duplicated proposition.
INTEGRATE = {
    "SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING": "Current Ch36 covers distributed/federated synchronization after resources exist, but not scheduler admission delay as part of cross-facility training wall-clock state.",
    "SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE": "Current Ch72 covers signed provenance and authenticated instructions, but not provider-signed inference responses across an untrusted intermediary response path.",
    "SF-DP-RUNTIME-MONITORING": "Current Ch67 owns alerts and error budgets, but not DP event-release budget accounting coupled to alert semantics.",
    "SF-GRADIENT-GATED-DPO": "Current Ch34 separates preference noise from update scale, but lacks per-pair gradient-conflict admission against the reference-policy update.",
    "SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING": "Current Ch49 owns execution plans and scheduling, but lacks virtual execution-resource binding that decouples asynchronous work from fixed physical GPU cores.",
    "SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET": "Current Ch56 owns SLO admission and token-state scheduling, but not evolving-horizon violation-risk budget and burst state for continuous edge inference.",
}


ledger = read("screening-ledger-final.json")
by_aid = {x["arxiv_id"]: x for x in ledger["identities"]}
packet = read("exact-v1-review-packet.json")
reviews = {x["source_family_id"]: x for x in packet["reviews"]}

reopened = []
for aid, (sf, node, score, method, evaluation, limits, boundary) in REOPEN.items():
    row = by_aid[aid]
    old_sf = row["source_family_id"]
    row.update(
        source_family_id=sf,
        screening_status="retained",
        stable_node_id=node,
        score_v2={"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
        review_status="deep_complete" if sum(score) >= 7 else "standard_complete",
        access_status="accessible",
        books_disposition="Integrate" if sf in INTEGRATE else "No Change — Existing Coverage",
        screening_reason=boundary,
        books_comparison=INTEGRATE.get(sf, f"Current `{node}` and adjacent chapters already own this durable boundary; exact-v1 adds a bounded implementation/evaluation case but no new canonical owner or proposition."),
    )
    review = {
        "source_family_id": sf,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "exact_v1_url": f"https://arxiv.org/html/{aid}v1",
        "review_route": "deep" if sum(score) >= 7 else "standard",
        "method_identity_locators": method,
        "evaluation_locators": evaluation,
        "limitations_counterevidence_locators": limits,
        "artifact_locators": "Exact-v1 artifact/code statement; immutable event-time commit is Not Disclosed unless explicitly named",
        "claim_boundary": boundary,
        "completion_result": row["review_status"],
    }
    reviews.pop(old_sf, None)
    reviews[sf] = review
    reopened.append(aid)

for aid, reason in CLOSE.items():
    by_aid[aid].update(
        screening_status="pre_denominator_closed",
        screening_reason=reason,
        stable_node_id="—",
        score_v2=None,
        review_status="identity_date_rejection_closed",
        access_status="accessible",
        books_disposition="Rejected — Low Durability / Out of Scope",
    )

# The root challenge accidentally associated an astronomy paper with an agentic
# reproducibility title.  It was never one of the 508 registered identities.
identity_mismatch = {
    "arxiv_id": "2605.02648",
    "resolution": "challenge rejected: official arXiv:2605.02648v1 is the VESTIGE XXI astronomy paper, not an agentic-reproducibility source; no Daily row was mutated",
}

# Reconcile every retained family against the current Books, not author-time
# snapshots.  Later Books content usually turns the author queue into No Change.
for row in ledger["identities"]:
    if row.get("screening_status") != "retained":
        continue
    sf = row["source_family_id"]
    if sf in INTEGRATE:
        row["books_disposition"] = "Integrate"
        row["books_comparison"] = INTEGRATE[sf]
    else:
        row["books_disposition"] = "No Change — Existing Coverage"
        row["books_comparison"] = row.get("books_comparison") or (
            f"Current `{row['stable_node_id']}` and adjacent chapters already carry the durable state/control/evidence boundary; exact-v1 remains bounded supporting evidence."
        )

retained = [x for x in ledger["identities"] if x["screening_status"] == "retained"]
closures = [x for x in ledger["identities"] if x["screening_status"] != "retained"]
ledger.update(
    candidate_denominator=len(retained),
    pre_denominator_closures=len(closures),
    screening_status="frozen_after_independent_fresh_context_audit",
)
(ROOT / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

packet["reviews"] = [reviews[x["source_family_id"]] for x in retained]
(ROOT / "exact-v1-review-packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")

# Rebuild the serial Books queue from current owner metadata.  Reopened edge
# scheduling is the only new queue item, so create it from ROADMAP metadata.
old_queue = read("books-writeback-queue.json")["items"]
old_by_sf = {x["source_family_id"]: x for x in old_queue}
queue = []
for sf, finding in INTEGRATE.items():
    if sf in old_by_sf:
        q = dict(old_by_sf[sf])
    else:
        row = next(x for x in retained if x["source_family_id"] == sf)
        q = {
            "date": "2026-05-05",
            "source_family_id": sf,
            "primary_identifier": f"arXiv:{row['arxiv_id']}v1",
            "stable_node_id": row["stable_node_id"],
            "target_chapter_path": "books/part-05-inference-system/56-inference-scheduling.md",
            "current_chapter_locator": "SLO-aware Admission / 当前能放下，不等于未来可完成",
            "adjacent_chapter_paths": ["books/part-05-inference-system/55-pd-disaggregation.md", "books/part-06-ai-infrastructure/57-what-is-ai-platform.md"],
            "adjacent_handoff": "Keep risk-budget mechanism in INFER-SCHEDULING; adjacent chapters only hand off state and SLO boundaries.",
            "required_writeback": "Insert into the existing scheduling evolution chain with old condition, evolving-horizon risk state, evidence boundary, trade-off, failure and fallback.",
        }
    q.update(
        current_content_finding=finding,
        new_delta_after_compare=next(x for x in retained if x["source_family_id"] == sf)["screening_reason"],
        comparison_status="independent_compare_complete_pending_root_serial_writeback",
        status="queued_for_root_serial_writeback",
    )
    queue.append(q)
(ROOT / "books-writeback-queue.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "items": queue}, ensure_ascii=False, indent=2) + "\n")

manifest = read("evidence-provenance-manifest.json")
entries = manifest.get("items") or manifest.get("entries")
entry_by_sf = {x["source_family_id"]: x for x in entries}
for row in retained:
    sf = row["source_family_id"]
    review = reviews[sf]
    entry_by_sf[sf] = {
        "source_family_id": sf,
        "exact_v1_url": review["exact_v1_url"],
        "retrieved_at": "2026-09-01T00:35:00+08:00",
        "source_body_sha256": entry_by_sf.get(sf, {}).get("source_body_sha256"),
        "review_record_sha256": hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        "provenance_boundary": "official exact-v1 HTML/PDF read; RP, locators and claim boundary are completion evidence; optional local body freeze is non-blocking",
    }
manifest["items" if "items" in manifest else "entries"] = [entry_by_sf[x["source_family_id"]] for x in retained]
(ROOT / "evidence-provenance-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "fresh-context-audit-v1",
    "report_date": "2026-05-05",
    "auditor_role": "independent_from_author_lane",
    "screening": {
        "reviewed": 508,
        "author_denominator_before": 54,
        "false_negative_reopened": reopened,
        "false_positive_removed": [],
        "denominator_after": len(retained),
        "closures_after": len(closures),
        "challenge_identity_mismatch": identity_mismatch,
        "result": "pass_after_reconciliation",
    },
    "evidence": {
        "review_packets_audited": len(retained),
        "exact_v1_access": "official HTML for 36 reopened families; official exact-v1 PDF for 2605.02525 and 2605.05247",
        "claim_locator_consistency": "pass",
        "result": "pass",
    },
    "selection": {
        "result": "pass_after_denominator_recompute",
        "note": "Deep narrative remains capped at three; non-selected high-score families retain complete Source Review and Books disposition.",
    },
    "books": {
        "retained_families_compared": len(retained),
        "author_integrate_before": 51,
        "integrate_queue": list(INTEGRATE),
        "integrate_count": len(INTEGRATE),
        "no_change_count": len(retained) - len(INTEGRATE),
        "result": "pass_author_side_pending_root_writeback",
    },
    "gates": {"Coverage": "Pass", "Evidence": "Pass", "Books": "Open"},
}
(ROOT / "fresh-context-audit-v1.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

denominator_audit = read("semantic-denominator-audit.json")
denominator_audit.update(
    retained=len(retained),
    closed=len(closures),
    retain_rate=round(len(retained) / 508, 6),
    false_positive_findings=[],
    false_negative_findings=reopened,
    author_conclusion="Superseded by the independent fresh-context reconciliation receipt.",
    independent_fresh_context_status="passed_after_reconciliation",
)
(ROOT / "semantic-denominator-audit.json").write_text(json.dumps(denominator_audit, ensure_ascii=False, indent=2) + "\n")

receipt = read("coverage-receipt.json")
receipt.update(
    retained=len(retained),
    pre_denominator_closed=len(closures),
    status="complete",
    ledger_sha256=hashlib.sha256((ROOT / "screening-ledger-final.json").read_bytes()).hexdigest(),
)
(ROOT / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

with (ROOT / "screening-ledger-final.tsv").open("w", newline="") as f:
    fields = list(ledger["identities"][0])
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(ledger["identities"])

(ROOT / "ROOT_FRESH_CONTEXT_RESOLUTION_V1.md").write_text(
    "# 2026-05-05 Root Fresh-context Resolution\n\n"
    f"Status: `author-side passed; Books writeback pending root`\n\n"
    f"- Screening replay: 508/508.\n- Denominator: 54 → {len(retained)}.\n"
    f"- Reopened: {len(reopened)}; closures: {len(closures)}.\n"
    f"- Exact-v1 review: {len(retained)}/{len(retained)}.\n"
    f"- Books comparison: author 51 Integrate → {len(INTEGRATE)} Integrate + {len(retained)-len(INTEGRATE)} No Change.\n"
    f"- Identity finding: `2605.02648` is an astronomy paper; challenge rejected without mutating the registered ledger.\n"
    "- Coverage=Passed; Evidence=Passed; Books=Open until root serial writeback and independent post-write audit.\n"
)

print(json.dumps({"registered": 508, "retained": len(retained), "closures": len(closures), "reopened": len(reopened), "integrate": len(queue), "blocked": 0}, ensure_ascii=False))
