#!/usr/bin/env python3
"""Strict V12 repair proposal for the 2026-06-04 Candidate Denominator.

V12 re-adjudicates every one of the 87 V11 retains against the strict
Candidate Denominator admission rule in docs/RESEARCH_CONTRACT.md section 4.2.
The 487 V11 pre-denominator closures remain frozen and are copied without
changing their decision, class, admission delta, or rationale.  This stage
does not perform Source Review, scoring, Deep Selection, or Books work.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260604"
SOURCE = PACKET / "screening-ledger.json"
V10 = PACKET / "candidate-denominator-replay-v10.json"
V11 = PACKET / "candidate-denominator-audit-independent-v11.json"
OUT_JSON = PACKET / "candidate-denominator-repair-proposal-v12.json"
OUT_TSV = PACKET / "candidate-denominator-repair-proposal-v12.tsv"
OUT_MD = PACKET / "candidate-denominator-repair-proposal-v12.md"
OUT_SHA = PACKET / "candidate-denominator-repair-proposal-v12.sha256"


# Admission is intentionally narrow.  Each value names a durable system-level
# delta that survives deleting the paper/project name from the claim.
ADMISSION: dict[str, str] = {
    "2606.04329": "persistent agent memory adds a durable write-authority and poisoning boundary",
    "2606.04384": "selective release changes the formal privacy-accounting contract for private training",
    "2606.04402": "test-time compute scheduling is governed by consequence-weighted loss rather than uniform error",
    "2606.04413": "helpful-only fine-tuning is shown to create systematic alignment failure modes, correcting a training judgment",
    "2606.04415": "NPU virtualization changes prefill/decode placement, isolation, and resource ownership",
    "2606.04425": "prompt injection persists across sessions through stored state, changing the agent trust boundary",
    "2606.04459": "token-ranking APIs expose model identity and extraction surfaces, changing an API security contract",
    "2606.04522": "ANN selection must optimize downstream utility rather than treating Recall@k overlap as the serving objective",
    "2606.04557": "document-derived KV state becomes a reusable, composable serving artifact across requests",
    "2606.04581": "distributed speculative inference jointly assigns drafting compute and communication bandwidth across device and server",
    "2606.04594": "silent inference errors become diagnosable through aligned intermediate-state differential evidence",
    "2606.04628": "agent context becomes a permissioned block registry with explicit lifecycle and transformation authority",
    "2606.04769": "description-code drift in MCP servers becomes a measurable interface, runtime, and security contract",
    "2606.04778": "safety must be evaluated along the generation trajectory rather than only at the final output",
    "2606.04799": "agent observability requires an object-centric semantic data model that owns cross-silo telemetry relationships",
    "2606.04850": "accelerator co-design exposes stable functionality-resource interfaces and treats uncertainty as an optimizable resource",
    "2606.04903": "human-authored ontologies bound agent action authority and make execution auditable before deployment",
    "2606.04908": "GPU-native remote storage removes the CPU from ownership of the accelerator I/O data path",
    "2606.04923": "rubric-based RL reward hacking is reproduced as an evaluation-design failure rather than an isolated model error",
    "2606.04929": "post-training poisoning is sequential across SFT and preference stages, changing the pipeline threat model",
    "2606.05004": "private inference gains a model-agnostic batch-level protocol boundary",
    "2606.05029": "compute-saving foundation-model experiments require explicit statistical, internal, external, and construct validity contracts",
    "2606.05037": "machine-readable API recovery structure is a more durable agent interface contract than verbose error prose",
    "2606.05043": "agent interaction protocols become declarative executable artifacts rather than implicit application control flow",
    "2606.05122": "judge calibration is separated from score elicitation, changing the uncertainty-estimation contract",
    "2606.05241": "search-time contamination is an evaluation-time data-flow leak that must be measured in deep-research benchmarks",
    "2606.05271": "heterogeneous edge inference assigns placement at operator granularity rather than model granularity",
    "2606.05304": "inter-agent communication becomes a public action-state update protocol rather than unconstrained transcript sharing",
    "2606.05308": "LLM-judge rankings gain bias-corrected statistical bounds tied to limited human labels",
    "2606.05339": "MCP failures are assigned to protocol/server runtime categories with distinct ownership",
    "2606.05378": "pattern selectivity is shown not to establish task-causal circuitry, correcting a mechanistic evidence judgment",
    "2606.05384": "LLM-judge validity extends past initial scoring to post-decision interaction robustness",
    "2606.05391": "human oversight spans preventive, planning, live-monitoring, and post-hoc control responsibilities",
    "2606.05395": "generated physical-agent skills require a formal verification gate before execution authority is granted",
    "2606.05396": "capability evaluation must separate refusal policy from underlying task competence",
    "2606.05403": "multi-source synthesis needs an epistemic-validity gate distinct from fluent methodology narration",
    "2606.05414": "partial trajectories become evidence for an explicit early-alert and stop-control decision",
    "2606.05415": "ingestion and retrieval share an executable provenance-aware schema contract",
    "2606.05433": "frontier-training governance is reframed around verifiable computation records and pre-committed specifications",
    "2606.05495": "concurrent CUDA pipelines require event-triggered scheduling plus explicit in-flight buffer ownership for memory safety",
    "2606.05523": "safety post-training becomes a closed-loop adaptive attacker-defender control process",
    "2606.06529": "agent-control evaluation must model strategic attack start/stop selection rather than fixed attack frequency",
}


# Every V11 retain not in ADMISSION must appear here.  Reasons are deliberately
# family-specific; generic ROADMAP mapping or AI relevance is not admission.
DOWNGRADE: dict[str, tuple[str, str]] = {
    "2606.04351": (
        "local_model_or_representation_improvement_without_system_delta",
        "Frames2LoRA internalizes one video's frames into episode-specific LoRA weights; moving context into parameters is a local representation choice and does not establish a durable memory lifecycle, authority, or serving contract.",
    ),
    "2606.04391": (
        "task_local_method_without_durable_owner_delta",
        "SGDR is one web-agent online skill retrieval method; the abstract does not establish a reusable skill provenance, permission, release, or lifecycle contract beyond the method.",
    ),
    "2606.04401": (
        "local_training_method_without_durable_design_delta",
        "TANDEM is a bi-level data-mixture optimization algorithm with twin networks; its result does not redefine durable dataset ownership, admission, or training-stage governance.",
    ),
    "2606.04438": (
        "local_model_architecture_without_system_delta",
        "LoopMoE combines weight-shared iterative computation with sparse routing, but remains a local architecture branch without a durable runtime ownership or platform contract.",
    ),
    "2606.04446": (
        "local_inference_optimization_without_durable_contract",
        "D2SD is a particular dual-diffusion drafting and recovery algorithm; it improves speculative decoding locally without changing the general verifier, commit, or rollback contract.",
    ),
    "2606.04463": (
        "domain_bound_application_without_general_system_delta",
        "OSCAR is a robotics-specific action-conditioned video world model and policy evaluator; cross-embodiment results do not by themselves redefine a general world-model state or evaluation contract.",
    ),
    "2606.04466": (
        "local_training_method_without_durable_design_delta",
        "The difficulty-aware SFT-then-RL data split is a bounded small-model reasoning recipe; it does not establish a generally valid stage-ownership or release rule.",
    ),
    "2606.04484": (
        "framework_implementation_without_independent_contract_delta",
        "AgentJet packages detachable rollout clients and learners in one framework; the abstract reports an implementation architecture but does not establish a new durable distributed-training contract beyond known decoupled actor/learner ownership.",
    ),
    "2606.04511": (
        "local_model_architecture_without_system_delta",
        "SparDA adds a Forecast projection for sparse attention; this is a local attention architecture and does not independently change long-context state ownership or serving correctness.",
    ),
    "2606.04527": (
        "local_model_or_representation_improvement_without_system_delta",
        "Echo-Infinity compresses video history into a learned evolving memory for one generation architecture; the abstract does not define a reusable mutable-state or commit contract.",
    ),
    "2606.04536": (
        "local_parametric_memory_method_without_lifecycle_contract",
        "TMEM writes distilled experience into fast LoRA weights, but merely relocating state from prompt memory into parameters does not define durable provenance, invalidation, isolation, or rollback ownership.",
    ),
    "2606.04555": (
        "local_memory_data_structure_without_system_delta",
        "SegTreeMem is one temporally ordered agent-memory data structure; its local indexing method does not establish a general memory authority, persistence, or evidence contract.",
    ),
    "2606.04610": (
        "domain_bound_query_optimization_without_general_contract",
        "Semantic Histograms estimate selectivity for image semantic filters; this bounded optimizer component does not redefine a durable AI-System query or evaluation contract.",
    ),
    "2606.04627": (
        "local_agent_architecture_without_system_delta",
        "MIRAGE couples latent reasoning to a mobile-interface world model, but remains a task-specific agent architecture without a general state-ownership or control contract.",
    ),
    "2606.04641": (
        "domain_bound_compiler_system_without_general_contract",
        "NL2Pipe compiles natural-language analytics into one semantic operator pipeline; it does not establish a generally reusable AI compiler ownership or release contract beyond that system.",
    ),
    "2606.04645": (
        "domain_bound_validation_gate_without_general_contract",
        "CYGNET validates generated Cypher queries for one database language; the domain-specific gate does not by itself redefine general agent action authorization or release evidence.",
    ),
    "2606.04662": (
        "theory_without_operational_system_delta",
        "The Muon curvature analysis explains one optimizer comparison, but the abstract does not establish an operational per-layer learning-rate, optimizer-selection, or training-control contract.",
    ),
    "2606.04703": (
        "local_agent_learning_method_without_lifecycle_contract",
        "The continual-experience internalization study proposes principle-level distillation, but does not define durable provenance, isolation, rollback, or release ownership for evolving agent state.",
    ),
    "2606.04780": (
        "local_memory_data_structure_without_system_delta",
        "PersonaTree is one three-level persona representation; explicit support paths are useful but do not establish a general memory lifecycle or evidence contract.",
    ),
    "2606.04781": (
        "local_skill_representation_without_governance_contract",
        "AIP supplies a graph representation for agent skills, but the abstract does not establish an independently validated permission, provenance, release, or revocation contract.",
    ),
    "2606.04847": (
        "local_training_and_codegen_system_without_durable_contract",
        "MusaCoder is a full-stack GPU-kernel generation implementation for CUDA/MUSA; coupling training to compiler feedback is not by itself a new durable execution or release contract.",
    ),
    "2606.04896": (
        "bounded_case_report_without_general_system_delta",
        "Channel Fracture reports three failures from one Hermes deployment; the cases are useful discovery evidence but do not yet establish a general reliability model or validated control contract.",
    ),
    "2606.04928": (
        "local_attribution_method_without_durable_evidence_contract",
        "Bidirectional gradient perturbation is one training-data attribution algorithm; it does not establish a provenance or audit contract that remains valid across models and training regimes.",
    ),
    "2606.04964": (
        "local_inference_optimization_without_durable_contract",
        "SemBlock chooses dynamic diffusion decoding blocks at semantic boundaries; this is a local decoding method without a general execution, commit, or rollback contract.",
    ),
    "2606.04990": (
        "survey_without_new_primary_system_delta",
        "The evidence-tracing paper is a survey and taxonomy; it organizes prior work but does not itself establish a newly validated provenance mechanism or release contract.",
    ),
    "2606.05015": (
        "domain_bound_benchmark_without_general_evaluation_contract",
        "The quadrotor study evaluates environmental variability for one vision-based navigation setting; it is a bounded benchmark and does not define a general world-model release contract.",
    ),
    "2606.05080": (
        "benchmark_without_durable_system_contract",
        "AutoLab is a benchmark for long-horizon autonomous research tasks; its task suite does not independently change a durable agent execution or release contract.",
    ),
    "2606.05143": (
        "domain_bound_training_method_without_general_design_delta",
        "HORIZON is a recoverability curriculum demonstrated on quadruped locomotion; the bounded method does not establish a general physical-agent scaling or safety contract.",
    ),
    "2606.05145": (
        "bounded_empirical_result_without_durable_design_delta",
        "The failed-trace study identifies recoverability signals for selected interventions, but does not establish a durable reasoning-state owner or training/release contract.",
    ),
    "2606.05158": (
        "local_multi_agent_optimization_without_durable_protocol",
        "StreamMA pipelines reasoning tokens between agents to reduce latency; this is a local communication optimization without a stable public-state, delivery, or failure protocol.",
    ),
    "2606.05165": (
        "local_attribution_method_without_durable_evidence_contract",
        "STRIDE is one sparse-recovery approximation for training-data attribution; performance and applications do not establish a generally valid provenance or audit contract.",
    ),
    "2606.05233": (
        "benchmark_without_durable_system_contract",
        "The 793-episode browser safety study is a bounded benchmark and reproducibility audit; it does not independently define a lasting computer-use-agent safety or release contract.",
    ),
    "2606.05238": (
        "benchmark_without_durable_system_contract",
        "DeployBench is a 51-task artifact-deployment benchmark; coverage of lifecycle steps is not itself a durable deployment mechanism or release contract.",
    ),
    "2606.05249": (
        "benchmark_without_durable_system_contract",
        "SWE-InfraBench is a cloud-infrastructure-code evaluation dataset; realistic tasks do not by themselves establish a general infrastructure-agent correctness or release contract.",
    ),
    "2606.05250": (
        "domain_bound_agent_method_without_general_system_delta",
        "The CBR-augmented data-science agent is a domain-specific memory implementation; it does not establish a reusable persistent-memory ownership or lifecycle contract.",
    ),
    "2606.05263": (
        "local_reinforcement_learning_method_without_durable_contract",
        "CVT-RL is a particular counterfactual credit-assignment algorithm; it does not redefine durable reward ownership, rollout evidence, or training-release criteria.",
    ),
    "2606.05296": (
        "local_test_time_method_without_durable_control_contract",
        "Agentic Monte Carlo is one black-box test-time policy sampling method; it does not establish a stable action-authority, verification, or rollback boundary.",
    ),
    "2606.05342": (
        "benchmark_without_durable_system_contract",
        "SentinelBench measures time-evolving monitoring tasks; duration-aware tasks are useful coverage but do not themselves define a durable monitoring-agent control contract.",
    ),
    "2606.05362": (
        "local_hardware_design_tool_without_durable_contract",
        "MOSAIC is a workload-driven NPU simulator and design-space exploration framework; it does not establish a new stable hardware/software ownership or release contract.",
    ),
    "2606.05390": (
        "bounded_protocol_enactment_benchmark_without_contract_delta",
        "Ahoy demonstrates that LLMs can enact selected interaction protocols; this bounded result does not define protocol authority, delivery semantics, or runtime failure ownership.",
    ),
    "2606.05405": (
        "benchmark_without_durable_system_contract",
        "Agents' Last Exam is a long-horizon economic-task benchmark; verifiable outcomes do not by themselves establish a new agent workflow or release mechanism.",
    ),
    "2606.05484": (
        "local_communication_optimization_without_durable_contract",
        "MAPL learns per-stage activation compression for pipeline parallelism; it is a local communication optimization rather than a new durable activation ownership or correctness contract.",
    ),
    "2606.05516": (
        "bounded_optimizer_finding_without_durable_design_delta",
        "The dominant-layer zeroth-order result is a model- and method-specific empirical finding; it does not establish a generally valid per-layer optimization control contract.",
    ),
    "2606.05525": (
        "domain_skill_benchmark_without_general_system_delta",
        "SciVisAgentSkills bundles and evaluates scientific-visualization skills; a domain skill collection and harness do not establish a general skill lifecycle or release contract.",
    ),
    "2606.06535": (
        "guideline_review_without_new_primary_system_delta",
        "The gray-literature MLOps review synthesizes deployment guidelines; it does not provide a new primary mechanism, ownership model, or validated release contract.",
    ),
}


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    v10 = json.loads(V10.read_text(encoding="utf-8"))
    v11 = json.loads(V11.read_text(encoding="utf-8"))
    identities = source["identities"]
    identity_by_id = {row["arxiv_id"]: row for row in identities}
    v11_rows = {row["arxiv_id"]: row for row in v11["rows"]}
    v11_retained = {
        arxiv_id for arxiv_id, row in v11_rows.items()
        if row["decision"] == "retained_in_candidate_denominator"
    }
    v11_closures = set(v11_rows) - v11_retained
    v10_retained = {
        row["arxiv_id"] for row in v10["rows"]
        if row["decision"] == "provisionally_retained_in_candidate_denominator"
    }

    assert len(identities) == len(identity_by_id) == len(v11_rows) == 574
    assert len(v11_retained) == 87
    assert len(v11_closures) == 487
    assert set(ADMISSION).isdisjoint(DOWNGRADE)
    assert set(ADMISSION) | set(DOWNGRADE) == v11_retained
    assert set(ADMISSION) <= set(identity_by_id)

    rows = []
    preserved_closure_count = 0
    for identity in identities:
        arxiv_id = identity["arxiv_id"]
        old = v11_rows[arxiv_id]
        if arxiv_id in v11_closures:
            row = dict(old)
            row["v11_to_v12"] = "preserved_pre_denominator_closure"
            preserved_closure_count += 1
        elif arxiv_id in ADMISSION:
            row = dict(old)
            row["admission_delta"] = ADMISSION[arxiv_id]
            row["rationale"] = (
                f"V12 admission: {ADMISSION[arxiv_id]}. The delta survives removal of the paper name "
                "and changes a durable mechanism, ownership boundary, evaluation/release contract, "
                "or system design judgment."
            )
            row["v11_to_v12"] = "retained_after_strict_re_adjudication"
        else:
            closure_class, rationale = DOWNGRADE[arxiv_id]
            row = dict(old)
            row["decision"] = "family_specific_pre_denominator_closure"
            row["admission_delta"] = None
            row["closure_class"] = closure_class
            row["rationale"] = rationale
            row["v11_to_v12"] = "false_positive_downgraded"
        row["v10_comparison"] = (
            "unchanged_retained" if arxiv_id in ADMISSION and arxiv_id in v10_retained
            else "false_negative_promoted" if arxiv_id in ADMISSION
            else "false_positive_downgraded" if arxiv_id in v10_retained
            else "unchanged_closure"
        )
        rows.append(row)

    retained = {row["arxiv_id"] for row in rows if row["decision"] == "retained_in_candidate_denominator"}
    closures = [row for row in rows if row["decision"] == "family_specific_pre_denominator_closure"]
    v12_downgrades = sorted(v11_retained - retained)
    v12_promotions = sorted(retained - v11_retained)
    v10_fp = sorted(v10_retained - retained)
    v10_fn = sorted(retained - v10_retained)
    closure_counts = Counter(row["closure_class"] for row in closures)

    assert retained == set(ADMISSION)
    assert len(retained) == 42
    assert len(closures) == 532
    assert len(v12_downgrades) == 45
    assert not v12_promotions
    assert preserved_closure_count == 487
    # Preserve the V11 closure adjudications exactly; only the V12 lineage field
    # may be added to the copied row.
    for arxiv_id in v11_closures:
        new = next(row for row in rows if row["arxiv_id"] == arxiv_id)
        for key, value in v11_rows[arxiv_id].items():
            assert new[key] == value, (arxiv_id, key)
    assert source["audit"]["official_v1_submission_history"]["timestamp_matches"] == 574
    assert source["audit"]["official_v1_submission_history"]["timestamp_mismatches"] == 0
    assert source["audit"]["official_v1_submission_history"]["outside_window"] == 0

    payload = {
        "schema": "candidate-denominator-repair-proposal-v12",
        "audit_id": "DEN-AUDIT-20260604-STRICT-V12",
        "auditor": "fresh-context:jun04-v12-strict-reconciliation",
        "report_date": "2026-06-04",
        "window": "[2026-06-03 09:00, 2026-06-04 09:00) Asia/Shanghai",
        "population": 574,
        "semantic_reviewed": 574,
        "v11_retains_re_adjudicated": 87,
        "v11_closures_related_false_negative_recheck": {
            "population": 487,
            "preserved": 487,
            "promotions": 0,
            "status": "pass_no_related_false_negative_found",
        },
        "old_v10_provisional_retained": len(v10_retained),
        "old_v11_retained": len(v11_retained),
        "v12_proposed_retained": len(retained),
        "v12_pre_denominator_closures": len(closures),
        "v12_retain_rate_raw": round(len(retained) / 574, 6),
        "v11_to_v12_false_positive_downgrades": v12_downgrades,
        "v11_to_v12_promotions": v12_promotions,
        "v10_to_v12_false_positive_downgrades": v10_fp,
        "v10_to_v12_false_negative_promotions": v10_fn,
        "closure_class_counts": dict(sorted(closure_counts.items())),
        "identity_date_receipt": {
            **source["audit"]["official_v1_submission_history"],
            "boundary": "exact-v1 submission history; identifier prefix is never date evidence",
        },
        "materials_boundary": {
            "ordinary_pending": 0,
            "denominator_blockers": [],
            "former_evidence_blocker": "2606.05268",
            "former_evidence_blocker_status": "preserved as a V11 pre-denominator closure; no material recovery is claimed",
        },
        "downstream_actions_performed": [],
        "gate_status": "open_pending_root_review_and_denominator_freeze",
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    header = [
        "arxiv_id", "title", "submitted_v1_utc", "decision", "closure_class",
        "v11_to_v12", "admission_delta", "rationale",
    ]
    tsv = ["\t".join(header)]
    for row in rows:
        values = [
            row["arxiv_id"], row["title"], row["submitted_v1_utc"], row["decision"],
            row.get("closure_class") or "—", row["v11_to_v12"],
            row.get("admission_delta") or "—", row["rationale"],
        ]
        tsv.append("\t".join(str(value).replace("\t", " ").replace("\n", " ") for value in values))
    OUT_TSV.write_text("\n".join(tsv) + "\n", encoding="utf-8")

    closure_lines = "\n".join(
        f"| `{name}` | {count} |" for name, count in sorted(closure_counts.items())
    )
    downgraded_lines = "\n".join(
        f"- `{arxiv_id}`：{DOWNGRADE[arxiv_id][1]}" for arxiv_id in v12_downgrades
    )
    md = f"""# 2026-06-04 Candidate Denominator Strict Repair Proposal V12

## Outcome first

V12 对 V11 的 `87/87` 个 retain 逐项重新裁决，并复核 V11 的 `487/487` 个 pre-denominator closure 是否出现相关 false negative。完整 population 仍为 `574/574`，proposal retain `{len(retained)}`、closure `{len(closures)}`，raw retain rate `{len(retained) / 574:.2%}`。

本阶段只修复 Candidate Denominator。没有执行 Score V2、Source Review、Deep Selection、Books Comparison 或 Books 写回。V12 仍是 repair proposal，等待 root review 与 denominator freeze；Gate 保持 **Open**。

## Strict admission boundary

只有能够明确改变长期 AI-System mechanism、state/data/control ownership、evaluation/release contract、platform/training/inference design judgment，或纠正 Books 既有认知的 family 才被保留。以下条件单独出现均不足以 admission：

- 将上下文或经验写入参数；
- 局部 architecture、optimizer、kernel、decoder 或 retrieval 方法；
- 单一 domain benchmark、Skill collection、survey 或 guideline；
- AI 相关性或 ROADMAP 可映射性；
- 只在一个实现中展示性能收益。

## Reconciliation

| Metric | V10 | V11 | V12 proposal |
| --- | ---: | ---: | ---: |
| Raw identities | 574 | 574 | 574 |
| Retained | 197 | 87 | {len(retained)} |
| Pre-denominator closures | 377 | 487 | {len(closures)} |
| Retain rate | {197/574:.2%} | {87/574:.2%} | {len(retained)/574:.2%} |
| New downgrades from previous stage | — | 111 | {len(v12_downgrades)} |
| New promotions from previous stage | — | 1 | 0 |

- V11 retain re-adjudication: `87/87`
- V11 retains kept: `{len(retained)}`
- V11 false-positive downgrades: `{len(v12_downgrades)}`
- V11 closure related-FN recheck: `487/487`, promotion `0`
- Exact-v1 timestamp receipt: match `574`、mismatch `0`、outside `0`
- Ordinary pending: `0`
- Denominator blocker: `0`

## V11 → V12 family-specific downgrades

{downgraded_lines}

## Closure accounting

| Closure class | Families |
| --- | ---: |
{closure_lines}

`candidate-denominator-repair-proposal-v12.json` 和 `.tsv` 保存全部 `574` 条 reconciliation。V11 原有 `487` 条 closure 的 decision、class、admission delta 与 rationale 保持不变；V12 新增 `45` 条 family-specific closure。Core Daily 的全量筛选证据仍保留，但 closure 不进入 Candidate Ledger、不打 Score V2，也不触发 Source Review。

## Identity, material, and Gate truth

- 日期使用 exact-v1 submission history，不使用 arXiv identifier prefix。
- `2606.05268` 继续保留为 V11 pre-denominator closure；V12 没有声称恢复其缺失正文。
- Candidate Denominator: `Review Pending`，等待 root 独立审核与冻结。
- Evidence / Deep Selection / Books: `Open`，本阶段没有执行任何下游动作。

## Review claim

**CLAIM:** V12 对所有 `574` 个 family 给出互斥、完备、可复算的 proposed admission/closure；对 V11 的 `87` 个 retain 无抽样重审，并保留 `487` 个 closure 的既有证据。
**BOUNDARY:** 这证明 repair proposal 的账目完整性，不证明 root 已接受候选语义，也不证明 Evidence 或 Books Gate 通过。
"""
    OUT_MD.write_text(md, encoding="utf-8")

    sha_lines = []
    for path in (OUT_JSON, OUT_TSV, OUT_MD):
        sha_lines.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}")
    OUT_SHA.write_text("\n".join(sha_lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "population": 574,
        "v11_re_adjudicated": 87,
        "retained": len(retained),
        "closures": len(closures),
        "retain_rate": round(len(retained) / 574, 6),
        "v11_to_v12_downgrades": len(v12_downgrades),
        "v11_to_v12_promotions": len(v12_promotions),
        "v11_closures_rechecked": preserved_closure_count,
        "related_false_negative_promotions": 0,
        "ordinary_pending": 0,
        "denominator_blockers": 0,
        "gate": "open_pending_root_review_and_denominator_freeze",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
