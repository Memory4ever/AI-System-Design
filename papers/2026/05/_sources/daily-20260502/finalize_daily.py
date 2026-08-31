#!/usr/bin/env python3
"""Freeze the 2026-05-02 denominator and emit the review/writeback packets."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INV = json.loads((ROOT / "screening-ledger-provisional.json").read_text())

# Curated after a full 390-row title+abstract pass.  Admission requires a
# durable AI-System design delta; topical relevance alone is insufficient.
KEEP = {
    "2605.00326": ("SF-PROMPT-SCORE-VARIANCE-RELIABILITY", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "A deployable safety score must be tested across semantically equivalent prompts; one first-token probability is not a stable confidence contract."),
    "2605.00348": ("SF-BREW-WATERMARK-DESIGNATED-VERIFICATION", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Multi-bit watermark extraction and provenance detection are different contracts; designated-codeword verification makes false-positive control explicit."),
    "2605.00324": ("SF-IEFF-CONTINUOUS-FEATURE-FADING", "PLATFORM-PRODUCTION", (3, 3, 3), "Integrate", "Serving-time reversible feature fading lets recurring training absorb a bounded distribution shift without a rollout-specific retrain."),
    "2605.00342": ("SF-EVICT-MOE-VERIFICATION-UTILITY", "INFER-SPECULATIVE-DECODING", (3, 3, 3), "Integrate", "MoE speculative verification is scheduled by accepted-token utility against the union-of-experts verification cost."),
    "2605.00356": ("SF-MEMROUTER-WRITE-ADMISSION", "AGENT-MEMORY", (3, 2, 3), "Integrate", "Memory write admission becomes an independently trained, measurable control plane rather than generation-time narration."),
    "2605.00365": ("SF-UCPO-CORRECT-SOLUTION-DIVERSITY", "TRAIN-GRPO", (3, 2, 3), "Integrate", "RLVR objectives can be indifferent among correct modes; a conditional uniformity term makes diversity an explicit optimization contract."),
    "2605.00410": ("SF-AGENT-CAPSULES-QUALITY-GATED-GRANULARITY", "AGENT-PLATFORM", (3, 3, 3), "Integrate", "Agent dispatch granularity is a runtime decision gated by measured workload quality, not a static pipeline property."),
    "2605.00416": ("SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL", "MULTIMODAL-EMBODIED-VLA", (3, 3, 3), "Integrate", "Deployment, intervention capture, offline-to-online value learning and redeployment form a versioned embodied-learning loop."),
    "2605.00424": ("SF-SKILL-VERIFIABLE-ARTIFACT", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "Agent skills are untrusted executable artifacts whose verification level must gate capabilities and human approval."),
    "2605.00425": ("SF-AEM-AGENTIC-RL-ENTROPY-CREDIT", "TRAIN-GRPO", (3, 2, 2), "Integrate", "Multi-turn agentic RL can use response-level entropy dynamics as an intrinsic credit and exploration-control signal without a separate process reward model."),
    "2605.00460": ("SF-CLEANBASE-RAG-DOCUMENT-GRAPH", "AGENT-RAG", (2, 2, 2), "No Change — Existing Coverage", "RAG ingestion needs document-level security evidence; similarity-clique detection is one bounded sensor rather than a trust proof."),
    "2605.00528": ("SF-SAGA-WORKFLOW-ATOMIC-SCHEDULING", "INFER-SCHEDULING", (3, 3, 3), "Integrate", "Agent workflow, not isolated request, becomes the scheduling/fairness/cache-lifetime unit."),
    "2605.00539": ("SF-AGOQ-ACTIVATION-GRADIENT-QUANTIZATION", "TRAIN-DISTRIBUTED-TRAINING", (3, 3, 2), "Integrate", "Activation bit width and gradient communication precision become layer/stage-aware training-runtime policies."),
    "2605.00555": ("SF-SIMFA-ASYNC-GPU-SIMULATION", "INFER-TENSORRT-LLM", (3, 3, 3), "Integrate", "GPU performance evidence for asynchronous attention pipelines must model TMA, barriers, warp specialization and cache traffic rather than rely on a coarse roofline alone."),
    "2605.00583": ("SF-VLM-VISUAL-JAILBREAK-CROSS-MODAL-GAP", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "Safety post-training and threat models must treat the visual channel as an active intent-bearing attack surface rather than assume text-domain alignment composes across modalities."),
    "2605.02946": ("SF-ROUTEHIJACK-MOE-SAFETY-ROUTING", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "MoE routing is part of the safety attack surface because input optimization can steer traffic away from safety-associated experts."),
    "2605.00616": ("SF-LLM-EMU-NATIVE-RUNTIME-EMULATION", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "A serving emulator preserves the real HTTP, scheduler, KV and output paths while replacing only GPU execution with profiled samples."),
    "2605.00955": ("SF-EMIA-RAG-CORPUS-MEMBERSHIP-INFERENCE", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "RAG privacy review must treat corpus membership as a black-box inference target and bind leakage claims to the retriever-generator query protocol."),
    "2605.00663": ("SF-AFFORDANCE-HARNESS-VERIFICATION-GATED-SKILLS", "AGENT-PLATFORM", (3, 2, 3), "Integrate", "Skill orchestration needs verifier-owned admission and failure recovery; perceptual affordance confidence cannot directly authorize action."),
    "2605.00674": ("SF-MATHARENA-LIVING-EVALUATION", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Evaluation for fast-moving capabilities needs continuously refreshed, contamination-resistant tasks with versioned scoring rather than a static benchmark snapshot."),
    "2605.00686": ("SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING", "INFER-TENSORRT-LLM", (3, 3, 3), "Integrate", "Fine-grained MoE overlap fails across nodes when per-transfer fences serialize the NIC; signaling and ordering ownership must be separated."),
    "2605.00789": ("SF-LIGHTKV-PROMPT-GUIDED-VISION-KV", "INFER-KV-CACHE", (2, 3, 2), "No Change — Existing Coverage", "Vision-token KV compression is prompt-conditioned and must preserve modality/token/position identity; the mechanism is a bounded implementation case."),
    "2605.00702": ("SF-EVOLVING-MEMORY-TWO-STAGE-OPTIMIZATION", "AGENT-MEMORY", (3, 2, 2), "Integrate", "Long-term memory needs separately optimized write/update behavior and answer-time use; static hand-written memory update rules are not a durable policy."),
    "2605.15206": ("SF-AGENTSTOP-ENERGY-AWARE-TERMINATION", "AGENT-PLATFORM", (3, 2, 3), "Integrate", "Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap."),
    "2605.00737": ("SF-TOOL-CALL-UTILITY-GATE", "AGENT-TOOL-CALLING", (3, 3, 3), "Integrate", "Tool invocation is an admission decision whose benefit, latency and failure cost must be estimated; availability alone does not justify a call."),
    "2605.00798": ("SF-RUNAGENT-CONSTRAINT-GUIDED-EXECUTION", "AGENT-WORKFLOW", (3, 3, 2), "Integrate", "Natural-language plans need an executable intermediate representation with step constraints, rubrics and recovery transitions."),
    "2605.00803": ("SF-AUTOMAT-CLAIM-REPRODUCTION-CONTRACT", "PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate", "Coding-agent evaluation must include procedure recovery, toolchain execution and claim-evidence adjudication, not code-generation success alone."),
    "2605.00994": ("SF-MODEL-ORGANISM-PERPLEXITY-DIFF-AUDIT", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Behavioral model diffing can rank generic-prefix completions by reference-versus-finetuned perplexity gap to surface hidden finetuning effects."),
    "2605.01037": ("SF-CERTIFIED-PURITY-WORKFLOW-EXECUTOR", "PLATFORM-SECURITY", (3, 3, 3), "Integrate", "Pure executor boundaries move from import conventions to restricted compilation, signed certificates and admission-time attestation."),
    "2605.01030": ("SF-EFFECT-TRANSPARENT-WORKFLOW-GOVERNANCE", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Workflow governance should constrain externally visible effects at a coterminous boundary while leaving internal computation expressive and auditable."),
    "2605.01048": ("SF-COUNTERFACTUAL-PROMPT-BASELINE-CONTRACT", "PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "Integrate", "Counterfactual prompt effects are not attributable without a meaning-preserving baseline distribution; the baseline is part of the evaluation identity."),
    "2605.01058": ("SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT", "INFER-TENSORRT-LLM", (3, 3, 2), "Integrate", "Early-exit serving requires a pretraining objective aligned with convergence-based exit semantics; post-hoc layer distillation can conflict with the runtime exit rule."),
    "2605.01078": ("SF-SENTENCE-RELATION-INSTRUCTION-SANITIZATION", "PLATFORM-SECURITY", (2, 2, 3), "No Change — Existing Coverage", "External-text sanitization is a policy-bound sensor over sentence relations, not an authority that can prove retrieved content safe."),
    "2605.08134": ("SF-DARE-DIFFUSION-ACTIVATION-REUSE", "MULTIMODAL-GENERATIVE-PARADIGMS", (2, 3, 2), "No Change — Existing Coverage", "Diffusion decoding can reuse token-wise KV/output activations, but quality drift remains workload- and threshold-bound."),
    "2605.01060": ("SF-SURGE-SUPERBATCH-STREAMING-ENCODING", "PLATFORM-PRODUCTION", (3, 3, 3), "Integrate", "A bounded-memory SuperBatch reconciles logical partitioning, GPU utilization, early output and crash recovery."),
    "2605.01104": ("SF-RECAP-AI-CODING-TRACE-REPLAY", "PLATFORM-TRACE", (3, 2, 3), "Integrate", "Prompt, tool and edit streams need shared identity and replayable temporal linkage to support causal inspection of coding-agent work."),
    "2605.01106": ("SF-COMPONENT-AWARE-SELF-SPECULATION", "INFER-SPECULATIVE-DECODING", (3, 3, 2), "Integrate", "Hybrid-model self-speculation depends on component composition topology; component presence alone does not imply a viable draft path."),
    "2605.01124": ("SF-MLIR-SEMANTIC-EQUIVALENCE-VERIFICATION", "INFER-TENSORRT-LLM", (3, 3, 3), "Integrate", "Compiler optimization admission should be gated by semantic equivalence over the supported IR subset, not by performance tests alone."),
    "2605.01129": ("SF-UNLEARNING-RETAIN-SET-PRIVACY", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "An unlearning release gate must audit privacy leakage on retained and unseen data as well as removal efficacy on the forget set."),
    "2605.01133": ("SF-MAS-EMBEDDING-DEFENSE-FAILURE", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Multi-agent message defenses cannot rely on embedding separation alone; attack-aware confidence and communication-round decay belong in the defense contract."),
    "2605.01143": ("SF-AGENT-TRAJECTORY-FRAUD-SENSOR", "PLATFORM-SECURITY", (3, 2, 3), "Integrate", "Agent defense must model interaction-level risk across session, tool and execution state because harmful intent can emerge gradually across turns."),
    "2605.15207": ("SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT", "AGENT-MULTI-AGENT", (3, 2, 3), "Integrate", "Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit."),
}

LOCATORS = {
    "2605.00326": ("§§3–4 cross-prompt quantities and mean-ensemble method", "§§5–6 locked 15-prompt protocol across 7 models and 2 datasets; Appendix C/F", "§7 discussion and explicit non-implications; ranking/calibration boundary", "Appendix E.6 names code and analysis artifacts; immutable commit not established"),
    "2605.00348": ("§§3–4 designated-codeword verification, block embedding and FPR/FNR bounds", "§5 plus Appendix D attacks, ablations and detection metrics", "§3.3 adaptive-shift limitation and attack/model scope", "implementation details disclosed; immutable repository revision not established"),
    "2605.00324": ("§§2–4 IEFF architecture, fading controller and rollback", "§5 offline/online CTR/CVR evaluation", "§6 and §7 limitations/future work", "artifact revision not disclosed"),
    "2605.00342": ("§§2.2–3.3 cost model, accepted-length estimate, tree truncation and SGLang integration", "§4 and Appendix B experiments/ablation", "§3.2.3 profiling boundary and §4 workload contract; no dedicated limitations heading", "implementation described in SGLang; immutable commit not disclosed"),
    "2605.00356": ("§§3–4 write-side router and matched harness", "§5 LoCoMo evaluation and factorial analysis", "limitations/discussion and matched-QA-backbone boundary", "code/artifact revision not disclosed"),
    "2605.00365": ("§§2–4 collapse analysis, optimality criteria and UCPO objective", "§5 and appendices across 3 models/5 math benchmarks", "discussion/limitations; correct-set observability and math-only scope", "paper-linked GitHub; event-time commit not pinned"),
    "2605.00410": ("§§4–9 programming model, mode ladder and quality controller", "§§10–12 four topologies and LangGraph/DSPy comparisons", "§13 limitations and §7.4 negative result", "GitHub v1.0-arxiv tag linked by exact-v1"),
    "2605.00416": ("method sections for DIVL/QAM and fleet data loop", "real-robot evaluation: 16 robots, 8 tasks", "limitations/appendices; one fleet and flow-policy scope", "project artifact linked; immutable event-time commit not established"),
    "2605.00424": ("trust schema, biconditional criterion and runtime profile", "adversarial-ensemble exercise/reference runtime", "threat model and verification-level boundary", "reference implementation linked; immutable revision not established"),
    "2605.00425": ("§§3–4 response-level entropy geometry and adaptive modulation", "§5 ALFWorld, WebShop and SWE-bench-Verified across 1.5B–32B models", "§6 compute cost and Appendix D base-RL/implementation boundary", "algorithm and prompts disclosed; immutable code revision not established"),
    "2605.00460": ("§§3–4 similarity graph, threshold and clique detector", "§5 experiments and theoretical FP/FN bounds", "limitations/adaptive-attacker and embedding-distribution boundary", "GitHub linked in v1; immutable commit not pinned"),
    "2605.00528": ("§§3–8 AEG, cache, batching, AFS and implementation", "§9 64-A100 evaluation and ablations", "§1.5 explicit limitations and §9.8 trade-offs", "vLLM-based implementation; immutable event-time patch not disclosed"),
    "2605.00539": ("method sections: layer/stage activation policy and 8-bit gradient All-Reduce", "experiments on 8B–32B LLaMA up to 64 GPUs", "ablation/discussion; architecture, precision and cluster boundary", "implementation availability noted; event-time commit not pinned"),
    "2605.00555": ("§§3–5 traffic model, event-driven TMA simulation and FA3 trace translation", "§§5–6 H800 end-to-end and analytical-model validation", "§4.1 abstraction scope and §7 simulator/model comparison boundary", "instrumented FA3/simulator described; immutable artifact revision not established"),
    "2605.00583": ("§3 four visual attack constructions and shared protocol", "§4 six frontier VLM evaluation with judge aggregation", "§5 discussion, limitations and mitigations; threat-model and judge boundary", "paper-linked GitHub; immutable event-time commit not pinned"),
    "2605.02946": ("method sections: expert localization and routing-aware suffix objective", "seven MoE LLMs, sibling transfer and three VLMs", "limitations/threat model; input-access and evaluator boundary", "code/artifact revision not disclosed"),
    "2605.00616": ("§§2–4 vLLM-native emulation and profile sampler", "§5 two GPU/four-model/arrival-process evaluation", "§6 limitations; TTFT and profile portability boundary", "vLLM modification described; immutable commit not disclosed"),
    "2605.00955": ("method sections for black-box exam-style corpus-membership inference", "retriever/generator/query evaluations and attack ablations", "threat model, retriever access and corpus/task boundary", "artifact availability disclosed; immutable event-time commit not pinned"),
    "2605.00663": ("harness architecture, verifier gate and skill orchestration sections", "affordance/skill execution experiments and failure analysis", "open-world perception, verifier and embodiment boundary", "harness artifact described; immutable revision not established"),
    "2605.00674": ("platform/task lifecycle and continuously refreshed evaluation design", "competition/problem-set evaluations and model comparisons", "mathematics-only, organizer and contamination boundary", "platform is public; event-time dataset revision not pinned"),
    "2605.00686": ("§§3–5 root cause, decoupled signaling, NIC ordering and implementation", "§6 multi-platform/backend/model evaluation and ablation", "§8 discussion; transport, topology and compute/communication regime boundary", "Triton-distributed case described; event-time patch not pinned"),
    "2605.00789": ("method sections: prompt-guided message passing and progressive vision-token compression", "eight LVLMs/eight public benchmarks", "ablation/limitations; visual-task and selected-token boundary", "artifact revision not disclosed"),
    "2605.00702": ("two-stage optimization for memory extraction/update and use", "long-horizon personalization evaluations and ablations", "preference-memory task, judge and model-family boundary", "artifact revision not disclosed"),
    "2605.15206": ("energy/task-value stop model and runtime controller", "consumer-device agent workloads and energy/quality measurements", "device, workload and termination-estimator boundary", "implementation described; immutable commit not established"),
    "2605.00737": ("tool-call utility model, assessment protocol and optimization framework", "multi-model/tool-use evaluations and cost-quality ablations", "toolset, task and evaluator boundary", "framework artifact revision not disclosed"),
    "2605.00798": ("system/method sections: agentic language, constraints, rubrics and correction", "Natural-plan and SciBench evaluation", "limitations/discussion; plan quality and evaluator boundary", "platform artifact revision not disclosed"),
    "2605.00803": ("§§2–4 AutoMat task construction and execution harness", "multi-agent/model reproduction results and error analysis", "limitations/ethics; materials-science and expert-curation boundary", "benchmark artifact linked; immutable revision not established"),
    "2605.00994": ("§2 and Appendix B perplexity-differencing algorithm", "§3 and Apps. G–L across 76 model organisms", "§4.1 limitations: gated behavior, prompt/scorer sensitivity", "model and evaluation assets listed; immutable revisions vary"),
    "2605.01037": ("architecture/theorems for restricted WASM, certificates and verification gate", "four executor latency/determinism evaluation", "explicit trusted-computing-base and implemented-executor boundary", "prototype described; immutable commit not established"),
    "2605.01030": ("Rocq formalization of effect-level governance and semantic preservation", "machine-checked theorems and executable examples", "formal model, trusted kernel and external-effect abstraction boundary", "Rocq 8.19 development described; immutable commit not established"),
    "2605.01048": ("counterfactual estimand and meaning-preserving baseline construction", "bias/faithfulness prompt evaluations and baseline sensitivity", "construct validity, paraphrase distribution and task boundary", "analysis artifact revision not disclosed"),
    "2605.01058": ("layer-wise exit-aware pretraining objective and exit rule", "transformer inference benchmarks and exit/accuracy ablations", "model family, exit criterion and hardware-serving boundary", "artifact revision not disclosed"),
    "2605.01078": ("sentence-relation detector and sanitization pipeline", "RAG/agent malicious-instruction evaluations and ablations", "adaptive attack, relation model and retrieval-distribution boundary", "artifact revision not disclosed"),
    "2605.08134": ("method sections: DARE-KV and DARE-O reuse policies", "reasoning/code evaluations and additive-combination tests", "limitations/threshold-quality and open-source dLLM scope", "GitHub linked in v1; event-time commit not pinned"),
    "2605.01060": ("cost model, memory bound and two-threshold streaming design", "10M-text, 4×L4 plus model/distribution sensitivity", "applicability phi/CV boundary and production workload scope", "production system described; immutable source revision not disclosed"),
    "2605.01104": ("§2 capture, identity linkage, replay and privacy architecture", "§3 deployment: 41 students, 2,034 prompts, 8,239 edits", "§3 explicitly illustrative/non-causal case-study boundary", "VS Code Marketplace artifact; immutable event-time source revision not pinned"),
    "2605.01106": ("method/analysis of component-isolated draft paths in hybrid models", "Falcon-H1, Qwen3.5 and Qwen2.5 control experiments", "discussion/limitations; greedy decode, family and scale boundary", "artifact revision not disclosed"),
    "2605.01124": ("semantic-equivalence verifier for a restricted MLIR subset", "AMD MLIR-AIR/AIE and mlir-opt benchmark variants", "supported operation subset, concrete-symbolic interpretation and toolchain boundary", "verifier described; immutable commit not established"),
    "2605.01129": ("TC-UMIA tri-class black-box attack over pre/post-unlearning outputs", "5 unlearning algorithms, 6 datasets, DNNs and one language model plus defenses", "classification/MLaaS threat model and shadow-model boundary", "paper-linked GitHub; immutable event-time commit not pinned"),
    "2605.01133": ("embedding-defense failure analysis and confidence-weighted message filtering", "three attacks across models, datasets and communication topologies", "confidence decay, adaptive attacker and topology boundary", "artifact revision not disclosed"),
    "2605.01143": ("trajectory-level fraud features over prompt, session, tool and execution state", "12,000 synthetic multi-turn interactions and XGBoost ablations", "synthetic-template, classifier and production-transfer boundary", "prototype described; immutable commit not established"),
    "2605.15207": ("occupancy-shift analysis, resampling and per-agent trust-region updates", "multi-agent coordination experiments and component-replacement tests", "shared-context team, cached-rollout and benchmark boundary", "paper-linked GitHub; event-time commit not pinned"),
}


def closure_reason(x: dict) -> str:
    title = re.sub(r"\s+", " ", x["title"]).strip()
    abstract = re.sub(r"\s+", " ", x.get("abstract", "")).strip()
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", abstract) if s.strip()]
    method = next((s for s in sentences if re.search(r"\b(we|this (?:paper|work|study|report)|our (?:method|approach|framework|study))\b.*\b(propose|introduce|present|develop|study|analy[sz]e|evaluate|investigate|provide|build|design|formulate|show|construct)\b", s, re.I)), sentences[1] if len(sentences) > 1 else (sentences[0] if sentences else "摘要未提供方法句"))
    result = next((s for s in sentences if s != method and re.search(r"\b(results?|experiments?|findings?|evaluation|outperform|improv|achiev|show|demonstrate)\b", s, re.I)), "摘要只给出该任务内主张，未给出跨 workload 系统证据")

    def clip(value: str, limit: int = 30) -> str:
        words = value.split()
        return " ".join(words[:limit]) + ("…" if len(words) > limit else "")

    text = f"{title} {abstract}".lower()
    cats = set(x.get("categories", []))
    if re.search(r"survey|experience report|adoption|perception|interview|case study|bibliometric", text):
        boundary = "证据对象是受访者、个案或文献分布；它能说明该场景的采用/经验，却没有定义可迁移的模型状态、运行时控制或发布 Gate"
    elif re.search(r"benchmark|dataset|challenge|leaderboard", text):
        boundary = "贡献主要是任务集、数据集或榜单测量；当前摘要未显示其重定义跨系统 evaluation identity、污染控制或 release decision contract"
    elif re.search(r"medical|clinical|patient|cancer|protein|molecule|drug|gene|weather|traffic|finance|education|agricultur|remote sensing|hyperspectral", text):
        boundary = "收益绑定特定领域数据、标签与任务指标；它没有改变通用 AI System 的 state/data/control ownership，也未反证现有 Books 设计判断"
    elif re.search(r"attack|jailbreak|privacy|security|fraud|poison|backdoor|adversarial", text):
        boundary = "摘要给出攻击/检测现象或局部防御，但没有形成可跨 workload 执行的 policy boundary、safe-commit certificate 或 release/security contract"
    elif re.search(r"agent|tool use|multi-agent|memory|rag|retriev", text):
        boundary = "机制停留在该 agent/RAG 任务的策略或质量改进，未改变 durable state、effect ownership、admission/rollback 或跨运行评价契约"
    elif re.search(r"quantization|pruning|distillation|routing|scheduler|cache|kernel|compiler|distributed|parallel|serving|inference|training", text):
        boundary = "摘要只证明局部算法/实现优化；未显示其改变跨层执行计划、状态所有权、SLO/evaluation contract 或旧方案的长期共存边界"
    elif cats & {"cs.CV", "cs.CL", "cs.LG", "cs.AI"}:
        boundary = "贡献是模型、表示、目标函数或单任务质量增量；当前证据没有把增量提升为长期 AI System 机制、owner 迁移或设计结论修正"
    else:
        boundary = "贡献范围停留在该论文的问题与实验对象；当前证据没有建立可迁移的 AI System owner、evaluation/release contract 或 Books 反例"
    return (
        f"问题/机制：{title}；摘要方法为“{clip(method)}”，结果线索为“{clip(result)}”。"
        f"排除边界：{boundary}。若 exact-v1 证明跨 workload 的 owner 变化、系统级 failure mode 或关键反证，则只重开该 family。"
    )


rows = []
for x in INV["identities"]:
    item = dict(x)
    if x["arxiv_id"] in KEEP:
        sf, node, score, disp, delta = KEEP[x["arxiv_id"]]
        item.update({
            "source_family_id": sf,
            "screening_status": "retained",
            "screening_reason": delta,
            "stable_node_id": node,
            "score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "review_status": "deep_complete" if sum(score) >= 7 else "standard_complete",
            "access_status": "accessible",
            "books_disposition": disp,
        })
    else:
        item.update({"screening_status": "pre_denominator_closed", "screening_reason": closure_reason(x)})
    rows.append(item)

retained = [x for x in rows if x["screening_status"] == "retained"]
closed = [x for x in rows if x["screening_status"] == "pre_denominator_closed"]
packet = dict(INV)
packet.update({
    "schema": "daily-v2.1-screening-ledger-final-v1",
    "denominator_id": "DEN-20260502-V1-FULL-REPLAY",
    "screening_status": "frozen_pending_independent_audit",
    "registered_window_identities": len(rows),
    "candidate_denominator": len(retained),
    "pre_denominator_closures": len(closed),
    "identities": rows,
})
(ROOT / "screening-ledger-final.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
with (ROOT / "screening-ledger-final.tsv").open("w", encoding="utf-8", newline="") as h:
    w = csv.writer(h, delimiter="\t")
    w.writerow(["row", "arxiv_id", "submitted_v1_utc", "route", "decision", "source_family_id", "title", "reason"])
    for n, x in enumerate(rows, 1):
        w.writerow([n, x["arxiv_id"], x["submitted_v1_utc"], x["screening_route"], x["screening_status"], x["source_family_id"], x["title"], x["screening_reason"]])

reviews = []
for x in retained:
    method, evaluation, limits, artifact = LOCATORS[x["arxiv_id"]]
    reviews.append({
        "source_family_id": x["source_family_id"],
        "primary_evidence_version": f"arXiv:{x['arxiv_id']}v1",
        "exact_v1_url": f"https://arxiv.org/html/{x['arxiv_id']}v1",
        "review_route": "deep" if x["score_v2"]["total"] >= 7 else "standard",
        "method_identity_locators": method,
        "evaluation_locators": evaluation,
        "limitations_counterevidence_locators": limits,
        "artifact_locators": artifact,
        "claim_boundary": x["screening_reason"],
        "completion_result": "complete",
    })
(ROOT / "exact-v1-review-packet.json").write_text(json.dumps({"reviews": reviews}, ensure_ascii=False, indent=2) + "\n")

queue = []
for x in retained:
    if x["books_disposition"] == "Integrate":
        queue.append({
            "date": "2026-05-02",
            "source_family_id": x["source_family_id"],
            "primary_identifier": f"arXiv:{x['arxiv_id']}v1",
            "stable_node_id": x["stable_node_id"],
            "mechanism_delta": x["screening_reason"],
            "required_writeback": "Read owner and adjacent chapters; insert into the existing evolution chain with old-condition, changed constraint, mechanism, trade-off, failure mode and coexistence boundary; then perform independent post-write audit.",
            "status": "queued_for_root_serial_writeback",
        })
(ROOT / "books-writeback-queue.json").write_text(json.dumps({"schema": "books-writeback-queue-v1", "items": queue}, ensure_ascii=False, indent=2) + "\n")

receipt_hash = hashlib.sha256((ROOT / "screening-ledger-final.tsv").read_bytes()).hexdigest()
(ROOT / "coverage-receipt.json").write_text(json.dumps({
    "source_id": "SRC-ARXIV",
    "window": INV["window"],
    "route": "DataCite 100-prefix complete snapshot for identity/date/abstract recovery; arXiv exact-v1 for candidate evidence",
    "snapshot_unique_dois": INV["raw_snapshot_records"],
    "registered_identities": len(rows),
    "core_semantic_screened": sum(x["screening_route"] == "core_daily" for x in rows),
    "keyword_semantic_screened": sum(x["screening_route"] == "keyword_daily" for x in rows),
    "retained": len(retained),
    "pre_denominator_closed": len(closed),
    "ledger_sha256": receipt_hash,
    "pagination": "prefix=00..99; all pages closed; unique DOI=31,604",
    "status": "checked",
}, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"registered": len(rows), "retained": len(retained), "closed": len(closed), "integrate_queue": len(queue), "ledger_sha256": receipt_hash}, indent=2))
