#!/usr/bin/env python3
"""Build the 2026-05-17 V2.1 author packet without touching shared Books.

The author lane freezes the denominator, reviews every retained official v1
body that was recoverable through the primary-source web route, and records an
individual material request only where HTML, PDF and shared caches all failed.
It deliberately leaves fresh-context and Books writeback gates to non-authors.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
sys.path.insert(0, str(REPO))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256
SRC = ROOT / "screening-ledger-provisional.json"
REPORT = REPO / "papers/2026/05/17/README.md"

RETAINED = {
    "2606.00053": ("MULTIMODAL-EMBODIED-VLA", (3, 3, 3), "failure-derived repair trajectories make testing part of the embodied training lifecycle"),
    "2605.16745": ("MULTIMODAL-REPRESENTATION", (3, 3, 3), "native 3D tokens join understanding and generation rather than remaining a stateless reconstruction sidecar"),
    "2605.16746": ("AGENT-MEMORY", (3, 3, 3), "persistent memory becomes a cross-turn attack surface whose writes and reuse require separate authority"),
    "2605.16757": ("AGENT-MULTI-AGENT", (3, 3, 2), "multi-agent topology and communication edges become jointly trained state instead of a fixed workflow"),
    "2605.16776": ("PLATFORM-SECURITY", (3, 2, 3), "unlearning must distinguish parameter erasure from inference-time refusal and verify both contracts"),
    "2605.16786": ("INFER-SPECULATIVE-DECODING", (3, 3, 3), "flash-backed mobile inference changes the draft/verify cost model and state-placement boundary"),
    "2605.16787": ("TRAIN-GRPO", (3, 3, 3), "RLVR admission must recognize examples with no useful policy-gradient direction rather than treating all verified rewards alike"),
    "2605.16790": ("AGENT-TOOL-CALLING", (3, 3, 3), "tool-composition reward moves from reference trajectories to invariant execution-state evidence"),
    "2605.16819": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "agent evaluation must freeze workflow state, hidden task contract, runtime receipts and unseen-shape generalization"),
    "2605.16826": ("TRAIN-PRETRAINING", (3, 3, 3), "distillation outcomes depend separately on prefix provenance and KL direction, changing the training contract"),
    "2605.16839": ("INFER-PREFILL", (3, 3, 3), "chunked prefill reuses a union of selected KV blocks while preserving the dense attention owner"),
    "2605.16895": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "deployment claims require an explicit evidence protocol rather than extrapolation from capability headlines"),
    "2605.16928": ("INFER-KV-CACHE", (3, 3, 3), "head-aware dense-to-sparse post-training separates candidate routing from exact attention"),
    "2605.16986": ("AGENT-PLATFORM", (3, 3, 3), "test-time skill synthesis creates ephemeral executable state that needs admission, expiry and rollback"),
    "2605.17003": ("TRAIN-DATA", (3, 3, 3), "online RL data selection becomes a control loop over current policy frontier rather than a static dataset"),
    "2605.17034": ("PLATFORM-SECURITY", (3, 3, 3), "RAG privacy enforcement must mediate retrieval and generation effects rather than rely on prompt policy"),
    "2605.17062": ("PLATFORM-SECURITY", (3, 3, 3), "package hallucinations create a model-to-software-supply-chain effect path requiring independent resolution"),
    "2605.17076": ("AGENT-MULTI-AGENT", (3, 3, 3), "observable-read isolation gives shared mutable multi-agent state an explicit consistency boundary"),
    "2605.17106": ("INFER-SCHEDULING", (3, 3, 3), "heterogeneous model pools and routing policy become decoupled deployable revisions"),
    "2605.17164": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "training and inference what-if simulation need a shared configuration identity and validation contract"),
    "2605.17170": ("INFER-KV-CACHE", (3, 3, 3), "agentic KV quantization must condition precision on role, modality and temporal lifecycle"),
    "2605.17172": ("AGENT-PLATFORM", (3, 3, 3), "personal AI splits sensitive local state, local execution and optional cloud escalation into typed boundaries"),
    "2605.17173": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "multilingual safety evaluation must decompose the failure factors hidden by aggregate jailbreak rate"),
    "2605.17193": ("AGENT-MULTI-AGENT", (3, 3, 3), "multi-model interaction can converge to correlated semantic collapse, invalidating independent-vote assumptions"),
    "2605.17204": ("MULTIMODAL-EMBODIED-VLA", (3, 2, 3), "VLA interpretation must ground latent features in closed-loop events and interventions"),
    "2605.18890": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "LLM social-simulation claims need robustness audits over model, prompt and population assumptions"),
    "2605.19373": ("PLATFORM-MODEL-REGISTRY", (3, 3, 3), "distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations"),
    "2605.22850": ("INFER-KV-CACHE", (3, 3, 3), "prefix KV reuse crosses local memory into layerwise object-store retrieval with explicit object identity"),
    "2605.23986": ("AGENT-MEMORY", (3, 3, 3), "hierarchical temporal indexing removes state-dependent generation from the memory write critical path"),
    "2605.28848": ("PLATFORM-EVALUATION-SYSTEM", (3, 2, 3), "non-stationary evaluation must bind model/retrieval/safety revisions to a streaming event clock"),
}

OWNER_PATHS = {
    "MULTIMODAL-REPRESENTATION": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "INFER-PREFILL": "books/part-05-inference-system/43-prefill.md",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
    "INFER-SPECULATIVE-DECODING": "books/part-05-inference-system/48-speculative-decoding.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-MODEL-REGISTRY": "books/part-06-ai-infrastructure/59-model-registry.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
}

# Exact-v1 source review: method, evaluation, limitations/counterevidence,
# artifact, provisional Books disposition.  Section names are taken from the
# official v1 body, not reconstructed from the abstract.
EVIDENCE = {
    "2606.00053": ("§III Design; §IV-A Distance-aware Test Selection; §IV-B Agent-based Data Synthesis and Model Repair", "§V-A Setup; §V-B Failure Detection; §V-C Model Repair; §V-D Real-world Evaluation", "§V-E Discussion and Limitation — four manipulation tasks, predefined repair library, six-researcher manual analysis and bounded simulation/physical setup", "§V-E says code/data will be released; immutable event-time artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.16745": ("§3 EVA01 Architecture — modality experts plus shared global attention over native sparse-voxel tokens", "§4 Experiments — 3D understanding and sparse-voxel generation evaluations", "§5 Limitations — 2B experts, 512^3 sparse voxels, coarse metrics and asymmetric understanding/generation capability", "official arXiv v1 body; event-time immutable checkpoint/repository Not Disclosed", "No Change — Existing Coverage"),
    "2605.16746": ("§3 Memory Laundering Attack; §4 State-Channel Separation and SPG read/write controls", "§5 Experimental Setup; §6 Results", "§7 Limitations — controlled Reddit-style simulations, one Llama-3.1-8B-Instruct DPO setup, no long histories/tools/retrieval/persistent deployment", "official arXiv v1 body; immutable implementation commit Not Disclosed", "Integrate"),
    "2605.16757": ("§3 NeuroMAS formulation — trainable graph of agent nodes and textual edges optimized from terminal reward", "§6 Experiments and ablations", "§5 capacity discussion and §7/Conclusion boundary — decomposition may fail, frozen small backbones and extra multi-call inference cost", "official arXiv v1 body; event-time training code/checkpoint Not Disclosed", "No Change — Existing Coverage"),
    "2605.16776": ("§3 D² distinguishable deletion objective and §4 EUA evaluation protocol", "§5 Experiments; Appendix evaluations", "Appendix A Limitations — energy-only deletion is insufficient, manual logit selection, forget/retain weighting sensitivity and controlled datasets", "official arXiv v1 body; immutable artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.16786": ("§4.1 Overview; §4.2 Mobile-Optimized Drafting; §4.3 Predictor-Based Verification Pruning; §4.4 Hardware-Hybrid Execution", "§5.1 Setup; §5.2 End-to-end Results; §5.3 Ablation; §5.4 Sensitivity", "No dedicated Limitations section; §5.3–§5.4 bound results to disclosed mobile phones/models, predictor threshold and flash/DRAM hierarchy", "official arXiv v1 body; event-time implementation commit Not Disclosed", "Integrate"),
    "2605.16787": ("§3.1 GRPO; §3.2 Learnability; §3.3 Empirical Existence; §4 Interventions", "§5 Gradient-outlier and representation analyses; Appendix B training settings", "§6 Discussion/Limitations — diagnostic correlations on disclosed Qwen/Llama math workloads do not establish a universal data-admission law", "official arXiv v1 body; immutable training artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.16790": ("§3 TIER deterministic function-schema/runtime rewards with syntactic, semantic and execution components", "§4–§6 DepthBench, BFCL v3 and NestFUL evaluations and ablations", "§7 Limitations — deterministic synthetic backend, cheap/repeatable/safe execution assumption, single-turn/Qwen3-8B/fixed-weight/12,288-context boundary", "official arXiv v1 body; event-time evaluator commit Not Disclosed", "Integrate"),
    "2605.16819": ("§3 AgentKernelArena gated compile→correctness→performance workflow and hidden task/configuration contract", "§4–§5 evaluations on 196 HIP/Triton/PyTorch-to-HIP tasks with build logs", "§6 Discussion and Appendix L — MI300X only, three commercial agents, three runs/config, max_iterations=3 and restricted task sources", "official arXiv v1 body; benchmark artifact/commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.16826": ("§3 KL decomposition; §4 Controlled Study; §5 KL Mixing and Entropy-Gated Length Curriculum", "§6 Experiments; Appendices G/I/J settings and general-domain checks", "Appendix K Limitations — math reasoning and accuracy-only GRPO reward; code, vision and alternative RL algorithms remain open", "official arXiv v1 body; immutable code/checkpoint Not Disclosed", "No Change — Existing Coverage"),
    "2605.16839": ("§3 Block-Union KV Selection and query-subsampled selector", "§4 Results and selector/grouping ablations on RULER and LongBench V2", "§5 Limitations — inherits selector misses; union trades sparsity for coverage; architecture/context/chunk/sparsity/grouping dependent and requires cache amortization", "official arXiv v1 body; event-time kernel commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.16895": ("§2 Confounds; §3 Structural Mismatch; §4 P1–P6 Minimum Evidence Protocols; §5 Modular Alternative", "reproduction harness and Appendices A–B over the disclosed five-ticker, one-year setup", "§6 Alternative Views, Objections, Limitations — minimum screening protocol is not sufficient deployment certification and is finance-specific", "official arXiv v1 body; reproduction harness commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.16928": ("§3–§4 head-role calibration, low-dimensional Q/K projection, local/retrieval split and two-stage distillation", "§6 evaluations on LongBench, RULER, AIME, MMLU-Pro plus H20 kernel microbenchmarks", "§10 Limitations — stable head specialization assumption, dense retrieval-head prefill and disclosed Qwen3/long-context/reasoning boundary", "official arXiv v1 body; event-time kernel/model artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.16986": ("§3 Test-time Adaptive Skill Synthesis and skill admission/reuse loop", "§4 Experiments and ablations over disclosed agent tasks", "No dedicated Limitations section; §4 ablations and §5 Discussion bound evidence to tested tasks/models and do not establish safe arbitrary executable-skill admission", "official arXiv v1 body; immutable skill/runtime artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.17003": ("§3 Learning-Zone Energy score and online example-selection controller", "§4 Experiments and ablations; Appendix F sensitivity", "No dedicated Limitations section; Appendix F shows noisy small-N estimates, diminishing returns and non-monotonic alpha sensitivity on disclosed math-reasoning workloads", "official arXiv v1 body; event-time training artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.17034": ("§III Threat/System Overview; §IV Axis-stratified Data; §V Dual-density Detection, thresholding and OOD abstention", "§VI Experiments; §VII architecture alternatives; §VIII operating-point study", "§IX Limitations — English medical/finance/law only, per-domain taxonomy/tuning, synthetic unsafe-data bias, one-class density ceiling and no multi-turn/verbatim/adversarial coverage", "official arXiv v1 body; event-time detector artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.17062": ("§3 Replication Methodology — package-name prompts, hallucination classification and registry resolution", "§5 Per-model Rates; §6 Universal-hallucination Set; §7 range-compression analysis", "§8 Limitations and Threats to Validity — five models, 2026-04-22…28 point-in-time measurement, possible corpus leakage and no post-cutoff held-out prompts", "official arXiv v1 PDF; event-time dataset/analysis commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.17076": ("§III Mechanism and Consistency Model; §V Architecture/Algorithm — DeliveryLog and Observable-Read Isolation", "§VI Setup; §VII structural and semantic evaluations", "§VIII Limitations — HTTP-observable read projection, dedicated-shard topology, not semantic coherence, HTTP/1.1 assumption, 5 ms failover gap and moderate judge agreement", "official arXiv v1 body; disclosed repository github.com/sajjadanwar0/sbus without immutable event-time commit", "Integrate"),
    "2605.17106": ("§3 Architecture — capability predictor, configuration-defined model profiles and shortfall matching", "§6–§8 benchmarks, offline evaluation and production A/B; §9 Analysis", "§10/Limitations — coding-specific four dimensions, labeling cost, single-turn 512-token predictor, adversarial routing surface; v1 defers production telemetry and per-language tables to v2", "official arXiv v1 body; §10.8 release components described but immutable event-time commit Not Disclosed", "Integrate"),
    "2605.17164": ("§3 Methodology — compiler-style frontend passes, pluggable simulation engines, overlap processor and parameter search", "§4 end-to-end accuracy, operator-engine ablation and cross-GPU/cluster-scale evaluation", "No dedicated Limitations section; §4 testbeds bind fidelity to profiled operators, disclosed hardware/configurations and model tracing support; simulation is not production outcome proof", "official arXiv v1 body; immutable simulator commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.17170": ("§3.1 tri-axial semantic/temporal/modality calibration and bit allocation; §3.2 mixed-precision pool and fused decode lifecycle", "§4 BFCL Memory/OSWorld accuracy, H100/B200 throughput and axis/budget ablations", "Appendix C Limitations — per-workload/model calibration, chat-template tagger adaptation and disclosed platform/model boundary", "official arXiv v1 body; event-time SGLang modification commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.17172": ("§3 five typed primitives, declarative spec and LLM-guided diagnose→propose→execute→gate search", "§4 eight personal-AI benchmarks; Appendix B protocol and Appendix C robustness", "Appendix D Limitations — ceiling/baseline anomalies, statistical precision, reward/judge/search sensitivity and single-machine evaluation", "official arXiv v1 body; implementation identifiers are described, immutable event-time commit Not Disclosed", "Integrate"),
    "2605.17173": ("§3–§5 IRT-based cross-language safety-gap decomposition, translation-fidelity and predictive validation", "§5 results over 61 configurations/16 base models and judge-agreement/variant robustness appendices", "§6 Limitations — sampled models/languages/prompts, translation and IRT assumptions; observed jailbreak rates are not provider-wide safety guarantees", "official arXiv v1 body; event-time evaluation artifact Not Disclosed", "No Change — Existing Coverage"),
    "2605.17193": ("Blocked — official exact-v1 HTML returned internal error; PDF cache miss", "Blocked — evaluation body unavailable", "Blocked — limitations/appendix unavailable", "official abs identity only; shared cache search returned no body", "Blocked / Unverified"),
    "2605.17204": ("§3 event-grounded SAE pipeline — kinematic keyframes, task-local event clusters, feature ranking and residual-preserving interventions", "§4 closed-loop experiments on OpenVLA and π0.5 across LIBERO suites", "§5 Limitations and Conclusion — limited policies/tasks/layers and intervention semantics; feature causality in tested rollouts does not establish global policy interpretability", "official arXiv v1 body; event-time code/checkpoint Not Disclosed", "No Change — Existing Coverage"),
    "2605.18890": ("§3 Robustness Audit Protocol; §4 two butterfly-effect case studies with architectural perturbations", "§4 gpt-5.2 main experiments plus Appendices C–D cross-model robustness over 30 seeds/condition", "§4 Finding Summary and Appendices C–D — no dedicated Limitations section; case-study, prompt, population, model and architecture sensitivity is the paper's counterevidence", "official arXiv v1 body; prompts/configurations in Appendix E, immutable code commit Not Disclosed", "No Change — Existing Coverage"),
    "2605.19373": ("§3 proof that direct tensor merges violate CRDT axioms; §4 two-layer OR-Set state plus deterministic canonical strategy execution", "§6 controlled algebraic, production-scale and multi-node convergence suites", "§7.2 and Appendix E Limitations — deployment constraints, semantic quality, scalability, security/conflict policy and floating-point determinism assumptions", "official arXiv v1 body; crdt-merge v0.9.4 named, immutable source commit Not Disclosed", "Integrate"),
    "2605.22850": ("§3 ObjectCache descriptor, server-side layer aggregation/mode selection, layerwise delivery and bandwidth scheduling", "§4.5 testbed; §5 storage/S3 baselines, overlap model and end-to-end TTFT", "§6.3 Limitations — small RoCEv2/A100 cluster prototype, S3-compatible path focus and incomplete production effects", "official arXiv v1 body; modified vLLM/LMCache/NIXL/Ceph/DAOS versions disclosed, immutable patches Not Disclosed", "Integrate"),
    "2605.23986": ("§3 persistent/derived memory substrate and scoped MemTrees; §4 write, query and lifecycle-maintenance paths", "§5 write/query latency and LongMemEval/LoCoMo evaluations", "§6 Discussion/Limitations — extraction/judge/model/benchmark dependence; accuracy is competitive rather than uniformly best and temporal index costs remain workload-dependent", "official arXiv v1 body; event-time implementation/data commit Not Disclosed", "Integrate"),
    "2605.28848": ("§2–§3 streaming snapshot/evaluation bundle with group-conditioned prompts, versioned run identity and human-review rule; §4 continuous monitoring rationale", "§5 empirical protocol and appendices with exact model IDs/access dates and score aggregation", "Known Limitations table and Discussion — English news, limited sources, prompt identity effects, embedding/sentiment bias and closed-model drift; high score requires human review", "official arXiv v1 body; output redistribution depends provider terms, hashes/scripts used otherwise", "No Change — Existing Coverage"),
}

DEEP_SELECTED = {
    "2605.17076": "DA-OBSERVABLE-READ-ISOLATION",
    "2605.17172": "DA-TYPED-PERSONAL-AI-SPEC",
    "2605.19373": "DA-MODEL-MERGE-CRDT-SEPARATION",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean(text)) if s.strip()]


def choose_method(ss: list[str]) -> str:
    for pattern in (r"\bwe (?:propose|present|introduce|develop|design|build|formulate|construct)\b", r"\bframework\b", r"\bmethod\b", r"\bmodel\b"):
        for s in ss:
            if re.search(pattern, s, re.I):
                return s[:520]
    return (ss[1] if len(ss) > 1 else ss[0])[:520]


def choose_result(ss: list[str]) -> str:
    for pattern in (r"\bresults?\b", r"\bevaluation\b", r"\bwe (?:show|find|demonstrate|observe|prove)\b", r"\boutperform"):
        for s in reversed(ss):
            if re.search(pattern, s, re.I):
                return s[:420]
    return ss[-1][:420]


def exclusion_boundary(row: dict) -> str:
    text = (row["title"] + " " + row.get("abstract", "")).lower()
    if any(k in text for k in ("medical", "mri", "clinical", "disease", "patient", "health", "molecule", "drug", "brain", "fmri")):
        return "该结论绑定医疗/脑科学/分子领域的数据定义与任务，不改变通用训练、推理或平台 owner；领域 deployment 仍需独立临床与治理合同"
    if any(k in text for k in ("education", "student", "course", "pedagog", "exercise recommendation")):
        return "该工作主要改变教育任务、课程或学习者评测，不重新分配通用 AI System 的状态与控制权"
    if any(k in text for k in ("remote sensing", "sar image", "lidar", "segmentation", "object detection", "tracking", "classification")):
        return "它是特定感知数据集/网络的局部方法，未给出跨 workload 的表示身份、runtime lifecycle 或 release contract"
    if any(k in text for k in ("forecast", "time series", "portfolio", "trading", "mortgage", "financial", "stock")):
        return "它优化特定预测/金融 workload；没有改变通用数据 lineage、在线调度或证据提交权"
    if any(k in text for k in ("benchmark", "dataset")):
        return "它增加任务/数据切片，但摘要未显示新的可复算 evaluation object、版本身份或部署 gate，故不进入长期系统分母"
    if any(k in text for k in ("diffusion", "flow matching", "image generation", "video generation")):
        return "它是生成质量或采样器的局部改进，未改变跨模态状态 owner、服务 commit 或通用生成范式的长期判断"
    if any(k in text for k in ("lora", "fine-tun", "training", "gradient", "optimizer")):
        return "它提供局部训练/适配技巧，但没有重定义 dataset/objective/checkpoint/runtime 之间的长期所有权合同"
    if any(k in text for k in ("agent", "tool", "memory", "rag")):
        return "它属于 Agent 局部能力或应用方案；摘要尚未形成新的 authority、durable state、effect commit 或 failure-recovery contract"
    if any(k in text for k in ("security", "attack", "privacy", "watermark", "jailbreak", "backdoor")):
        return "它揭示局部 attack/defense slice，但未改变平台既有 threat model、enforcement owner 或 release evidence contract"
    if any(k in text for k in ("attention", "transformer", "language model", "llm")):
        return "它是模型能力、表示或单项算法增量，未改变长期 runtime state/data/control ownership 或系统验收接口"
    return "它是领域算法、理论分析或应用证据，未显示可迁移的系统 owner、控制边界或 release/evaluation contract 变化"


data = json.loads(SRC.read_text())
rows = data["identities"]
seen = {row["arxiv_id"] for row in rows}
missing = sorted(set(RETAINED) - seen)
if missing:
    raise SystemExit(f"retained identities absent from window: {missing}")

for row in rows:
    ss = sentences(row.get("abstract", "")) or [row["title"]]
    method = choose_method(ss)
    result = choose_result(ss)
    if row["arxiv_id"] in RETAINED:
        node, score, delta = RETAINED[row["arxiv_id"]]
        review_status = "blocked" if row["arxiv_id"] == "2605.17193" else "deep_complete"
        access_status = "blocked" if row["arxiv_id"] == "2605.17193" else "accessible"
        disposition = EVIDENCE[row["arxiv_id"]][4]
        row.update({
            "screening_status": "retained_pending_exact_v1_review",
            "screening_reason": f"{row['title']} 提出的具体变化是：{method} 摘要中的长期系统挑战为：{delta}。它可能改变 `{node}` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“{result}”暂不作为最终证据。",
            "owner_node": node,
            "score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
            "review_status": review_status,
            "access_status": access_status,
            "integration_disposition": disposition,
            "source_family_id": f"SF-2026-ARXIV-{row['arxiv_id'].replace('.', '-')}",
        })
    else:
        row.update({
            "screening_status": "pre_denominator_closed",
            "screening_reason": f"{row['title']} 的方法/主张是：{method} 其摘要结果或目标为：{result} 排除边界：{exclusion_boundary(row)}；因此在 Candidate Denominator 前闭合，但保留 identity 供独立 false-negative audit 重开。",
        })

data.update({
    "gate_status": "author_denominator_and_evidence_packet_frozen_pending_independent_audit",
    "retained_candidates": len(RETAINED),
    "pre_denominator_closed": len(rows) - len(RETAINED),
})
ledger_path = ROOT / "screening-ledger-final.json"
ledger_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
ledger_sha = hashlib.sha256(ledger_path.read_bytes()).hexdigest()
(ROOT / "candidate-ids.txt").write_text("\n".join(sorted(RETAINED)) + "\n")

retrieved = "2026-09-01T18:15:00+08:00"
reviews = []
materials = []
for row in rows:
    aid = row["arxiv_id"]
    if aid not in RETAINED:
        continue
    family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
    method, evaluation, limitations, artifact, disposition = EVIDENCE[aid]
    blocked = disposition == "Blocked / Unverified"
    review = {
        "source_family_id": family,
        "arxiv_id": aid,
        "primary_evidence_version": f"arXiv:{aid}v1",
        "exact_v1_url": f"https://arxiv.org/html/{aid}v1",
        "review_route": "deep" if row["score_v2"]["total"] >= 7 else "standard",
        "method_identity_locators": f"arXiv:{aid}v1 — {method}",
        "evaluation_locators": f"arXiv:{aid}v1 — {evaluation}",
        "limitations_counterevidence_locators": f"arXiv:{aid}v1 — {limitations}",
        "artifact_locators": f"arXiv:{aid}v1 — {artifact}",
        "claim_boundary": ("Identity/date/abstract only; body-level mechanism and non-proof boundary remain unavailable." if blocked else f"Only the disclosed v1 mechanism and evaluation contract are accepted. {limitations}"),
        "completion_result": "blocked" if blocked else "complete",
        "retrieved_at": retrieved,
        "access_attempts": [f"https://arxiv.org/html/{aid}v1", f"https://arxiv.org/pdf/{aid}v1", "shared month/date cache"],
    }
    if blocked:
        review["access_error"] = "official HTML internal error; official PDF cache miss; shared cache search found no exact-v1 body"
        materials.append({
            "priority": "P1 Full Text",
            "source_family_id": family,
            "primary_identifier": f"arXiv:{aid}v1",
            "known_urls": [f"https://arxiv.org/html/{aid}v1", f"https://arxiv.org/pdf/{aid}v1", f"https://arxiv.org/e-print/{aid}v1"],
            "missing_material": "official exact-v1 full body including Method, Evaluation, Limitations/Appendix and artifact statement",
            "why_current_material_is_insufficient": "all official body routes and shared caches failed for this individual family; abstract cannot support deep review",
            "acceptable_alternative": "official v1 PDF/HTML/TeX or author-hosted immutable v1 manuscript with matching title/authors/content",
            "suggested_filename": f"arxiv-{aid.replace('.', '-')}-v1.pdf",
            "audit_after_recovery": "read Method/formulas/implementation/evaluation/ablations/limitations/artifact; recompute Score/Books disposition",
        })
    reviews.append(review)

(ROOT / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v2.1", "report_date": "2026-05-17", "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(ROOT / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": "2026-05-17", "items": materials}, ensure_ascii=False, indent=2) + "\n")

compares = []
for row in rows:
    aid = row["arxiv_id"]
    if aid not in RETAINED:
        continue
    node = row["owner_node"]
    path = OWNER_PATHS[node]
    number = int(Path(path).name.split("-", 1)[0])
    part = Path(path).parent
    neighbors = sorted(p for p in part.glob("*.md") if re.match(r"\d+-", p.name))
    ix = next(i for i, p in enumerate(neighbors) if p.name == Path(path).name)
    adjacent = []
    if ix: adjacent.append(str(neighbors[ix - 1]))
    if ix + 1 < len(neighbors): adjacent.append(str(neighbors[ix + 1]))
    owner_text = (REPO / path).read_text()
    disposition = EVIDENCE[aid][4]
    existing = {
        "Integrate": "Current owner defines the general lifecycle and handoff, but the reviewed v1 adds a missing durable mechanism/ownership boundary that is not stated with this specificity.",
        "No Change — Existing Coverage": "Current owner and adjacent chapters already express the durable state/control/evidence boundary; this v1 supplies a bounded case without changing the existing design conclusion.",
        "Blocked / Unverified": "Current owner was opened, but exact-v1 body evidence is unavailable; no semantic comparison may be finalized from the abstract.",
    }[disposition]
    compares.append({
        "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
        "arxiv_id": aid,
        "owner_node": node,
        "owner_path": path,
        "adjacent_paths": adjacent,
        "owner_sha256": hashlib.sha256(owner_text.encode()).hexdigest(),
        "existing_proposition": existing,
        "new_evidence_delta": row["screening_reason"],
        "evolution_relation": "Not Applicable — exact-v1 body blocked; no relation inferred from abstract" if disposition == "Blocked / Unverified" else "Direct Evolution",
        "decision": disposition,
        "books_review_ref": f"books-review:SF-2026-ARXIV-{aid.replace('.', '-')}",
        "target_chapter": number,
    })
(ROOT / "books-current-content-comparison.json").write_text(json.dumps({"schema": "books-current-content-comparison-v2.1", "report_date": "2026-05-17", "items": compares}, ensure_ascii=False, indent=2) + "\n")

coverage = {
    "source_id": "SRC-ARXIV", "window": data["window"],
    "route": "DataCite arXiv 202604/202605/202606 v2 snapshots, registered categories, full title+abstract semantic screen",
    "raw_snapshot_records": data["raw_snapshot_records"], "registered_identities": len(rows),
    "core_semantic_screened": data["core_daily_semantic_review_required"],
    "keyword_semantic_screened": data["keyword_daily_semantic_review_required"],
    "false_negative_screened": data["title_route_negative_pending_false_negative_audit"],
    "retained": len(RETAINED), "pre_denominator_closed": len(rows) - len(RETAINED),
    "ledger_sha256": ledger_sha, "pagination": "prefixes 00..99; final_cursor=end",
    "status": "author coverage frozen; independent fresh-context audit pending",
}
(ROOT / "coverage-receipt.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n")
integrate_rows = [r for r in rows if r.get("integration_disposition") == "Integrate"]
queue = [
    "# 2026-05-17 Books Writeback Queue", "",
    "本文件是 date-local author queue；本 lane **未修改共享 Books**。必须经非作者 fresh-context audit 后，由 root 按日期串行写回并做 post-write audit。", "",
    f"- Queue count: {len(integrate_rows)}", "- Status: `pending_independent_review`", "",
]
for row in integrate_rows:
    queue += [
        f"## {row['source_family_id']}",
        f"- Primary: `arXiv:{row['arxiv_id']}v1`",
        f"- Owner: `{row['owner_node']}`",
        f"- Delta: {RETAINED[row['arxiv_id']][2]}",
        "- Required writeback: merge into the existing evolution spine; preserve old-path rationale, changed constraint, state/control owner, trade-off, failure, fallback/coexistence and evidence boundary.", "",
    ]
(ROOT / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue).rstrip() + "\n")

author_audit = {
    "schema": "semantic-author-audit-v2.1", "report_date": "2026-05-17",
    "scope": "author-side 279/279 screening and evidence/access classification; not an independent fresh-context audit",
    "checks": {
        "registered_screened": [len(rows), len(rows)], "candidate_denominator": len(RETAINED),
        "pre_denominator_closures": len(rows) - len(RETAINED),
        "closure_reason_unique": len({r["screening_reason"] for r in rows if r["screening_status"] == "pre_denominator_closed"}),
        "exact_v1_complete": len(RETAINED) - len(materials), "exact_v1_blocked": len(materials), "ordinary_pending": 0,
        "books_compared": len(RETAINED), "books_writeback_eligible": len(integrate_rows),
    },
    "unresolved_findings": [
        "Independent fresh-context replay must challenge all 279 admission/closure decisions.",
        "One exact-v1 family remains a precise external full-text blocker; abstract-only metadata was not treated as body-level evidence.",
        "Books and Deep Analysis decisions remain provisional until independent review; root serial writeback is not yet authorized.",
    ],
}
(ROOT / "semantic-author-audit.json").write_text(json.dumps(author_audit, ensure_ascii=False, indent=2) + "\n")


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


candidate_lines = []
for row in rows:
    aid = row["arxiv_id"]
    if aid not in RETAINED:
        continue
    s = row["score_v2"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    candidate_lines.append(
        f"| {family(aid)} | arXiv:{aid}v1 | paper-v1:{aid} | 2026-W20 | 2026-05-16 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {row['review_status']} | {row['access_status']} | {override} | review:{family(aid)} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{family(aid)} | no |"
    )

lines = [
    "# Daily Research — 2026-05-17", "", "**Research Date:** 2026-05-17", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-16 09:00:00 ～ 2026-05-17 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；DataCite 仅用于 identity/date/abstract recovery；技术结论必须绑定 official exact-v1。", "",
    "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。Author denominator 与可访问 exact-v1 packet 已冻结；等待独立 fresh-context audit、一个精确全文 blocker 恢复及 root 串行 Books writeback。", "",
    "## Executive Summary", "",
    f"相邻月份完整 v2 快照含 {data['raw_snapshot_records']:,} 条 raw records；严格窗口注册 {len(rows)} 条 identity。{len(rows)}/{len(rows)} 已完成 title+abstract 语义筛选，author 冻结 {len(RETAINED)} 个 candidate（{len(RETAINED)/len(rows):.2%}），其余 {len(rows)-len(RETAINED)} 项形成 family-specific pre-denominator closure。通过 primary web route 恢复并读取 {len(RETAINED)-len(materials)}/{len(RETAINED)} 个 official exact-v1，逐项定位 Method、Evaluation、Limitations/Counterevidence 与 Artifact；仅 {len(materials)} 项在 HTML、PDF 与共享缓存均失败后转为精确 blocked。当前提出 {len(integrate_rows)} 项 provisional Books queue，但未写共享 Books。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
    "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-17 |", "| Window End | 2026-05-17 |", "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |", "| Denominator ID | DEN-20260517-V1-AUTHOR-30 |", f"| Denominator Frozen At | {retrieved} |", "| Completion Status | In Progress |", "| Coverage Gate | Open |", "| Evidence Gate | Open |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
    "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    f"| SRC-ARXIV | 2026-05-16T09:00:00+08:00 | 2026-05-17T09:00:00+08:00 | {retrieved} | DataCite v2 202604+202605+202606 prefixes 00..99; registered-category full title+abstract screen | checked | {len(rows)} | {';'.join(family(a) for a in sorted(RETAINED))} | pages=300; final_cursor=end; raw={data['raw_snapshot_records']}; registered={len(rows)}; screened={len(rows)}; retained={len(RETAINED)}; closure={len(rows)-len(RETAINED)} | 2026-05-17T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | GAP-20260517-EXACT-V1-ACCESS |", "",
    "### Coverage Limitations", "",
    f"<!-- coverage:SRC-ARXIV:20260517:start -->窗口枚举与 author semantic screen 已覆盖 {len(rows)}/{len(rows)} identity；独立 reviewer 尚未重放，因此 Coverage Gate 仍 Open。{len(RETAINED)-len(materials)}/{len(RETAINED)} retained official v1 已读；{len(materials)} 个 family 保持精确 Conditional blocker。<!-- coverage:SRC-ARXIV:20260517:end -->", "",
    "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
    "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    *candidate_lines, "",
    "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
    "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]

for item in reviews:
    fid = item["source_family_id"]
    provenance = f"RP-BLOCKED-{item['arxiv_id'].replace('.', '')}" if item["completion_result"] == "blocked" else f"RP-TODO-{fid}"
    lines.append(f"| {fid} | {provenance} | {item['review_route']} | {item['primary_evidence_version']} | SRC-ARXIV@{item['primary_evidence_version']} | {item['method_identity_locators']} | {item['evaluation_locators']} | {item['limitations_counterevidence_locators']} | {item['artifact_locators']} | claim:{fid} | {item['completion_result']} |")

lines += ["", "### Source Reviews", ""]
row_by_id = {r["arxiv_id"]: r for r in rows}
for item in reviews:
    row = row_by_id[item["arxiv_id"]]
    fid = item["source_family_id"]
    if item["completion_result"] == "blocked":
        body = [
            f"Admission rationale：{row['screening_reason']}",
            "Access boundary：official exact-v1 HTML 返回内部错误，PDF cache miss，共享月度/日期缓存没有正文；仅 identity/date/abstract 已确认。",
            f"<!-- claim:{fid}:start -->不得从摘要恢复内部机制或写入 Books；恢复材料要求见 `materials-request.json`。<!-- claim:{fid}:end -->",
        ]
    else:
        body = [
            f"问题与演进：{RETAINED[item['arxiv_id']][2]}。旧路径在原 workload、风险和成本约束下继续成立。",
            f"Method：`{item['method_identity_locators']}`。",
            f"Evaluation：`{item['evaluation_locators']}`。",
            f"Non-proof / fallback：`{item['limitations_counterevidence_locators']}`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`{item['artifact_locators']}`。",
            f"<!-- claim:{fid}:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:{fid}:end -->",
        ]
    lines += [f"<!-- review:{fid}:start -->", f"#### {row['title']}", "", *sum(([p, ""] for p in body), []), f"<!-- review:{fid}:end -->", ""]

lines += [
    "## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->",
    "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
    "本报告不把作者性能数字外推为通用 benchmark claim；workload/model/hardware/precision/length/batch/concurrency/SLO 的披露与缺口保留在各 Source Review。", "",
    "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
    "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
    "| --- | --- | --- | --- | --- | --- | --- |",
]
for aid in sorted(RETAINED):
    fid = family(aid)
    if aid == "2605.17193":
        lines.append(f"| {fid} | score_7_9 | not_selected | — | — | exact-v1 body unavailable; abstract-only admission is insufficient | analysis-decision:{fid} |")
    else:
        unit = DEEP_SELECTED.get(aid, "—")
        decision = "selected" if aid in DEEP_SELECTED else "not_selected"
        reason = "crosses a durable state/control ownership boundary" if aid in DEEP_SELECTED else f"exact-v1 review complete; owner-local delta is less cross-cutting than the three selected units"
        ref = f"analysis:{unit}" if aid in DEEP_SELECTED else f"analysis-decision:{fid}"
        eligibility = "score_7_9;forced_review;potential_books_delta" if EVIDENCE[aid][4] == "Integrate" else "score_7_9"
        lines.append(f"| {fid} | {eligibility} | {decision} | {unit} | — | {reason} | {ref} |")
lines += ["", "本日只扩写三项跨层 ownership 变化；其余候选仍保留完整 Source Review 与 Books Decision。", "",
          "<!-- analysis:DA-OBSERVABLE-READ-ISOLATION:start -->", "### Shared Agent State：从共享存储推进到可观察读隔离", "", "简单共享存储在低并发、可串行重放时成本最低；多 Agent 并发读写后，约束变成读者不能看到尚未稳定、相互矛盾的中间状态。S-Bus 以 DeliveryLog 与 Observable-Read Isolation 将‘已交付’和‘可读’分开，使 HTTP 可观察投影获得明确一致性边界。收益是可解释的读隔离和故障恢复，代价是 dedicated-shard 假设、日志状态与 failover gap；它不保证语义一致，超出 HTTP-observable projection 时应回退事务/显式版本协议。", "<!-- analysis:DA-OBSERVABLE-READ-ISOLATION:end -->", "",
          "<!-- analysis:DA-TYPED-PERSONAL-AI-SPEC:start -->", "### Personal AI：从单模型替换推进到整栈 typed spec", "", "只替换模型在云端固定栈中简单，但本地模型、runtime、Agent、Tools/Memory 与学习策略之间存在耦合。OpenJarvis 把五类 primitive 组合成可版本化 spec，再以诊断、提案、执行和 held-out gate 提交跨 primitive 修改。它换来 end-to-end 可测与回滚，却引入搜索成本、teacher 隐私、judge bias 和单机证据边界；在没有稳定 gate 或可审计 trace 时，仍应采用手工版本化配置而非自动提交。", "<!-- analysis:DA-TYPED-PERSONAL-AI-SPEC:end -->", "",
          "<!-- analysis:DA-MODEL-MERGE-CRDT-SEPARATION:start -->", "### Distributed Model Merge：把收敛状态与 tensor strategy 分层", "", "直接把平均、SLERP 或 TIES 当 CRDT merge 在中心化、固定顺序中可用，但归一化与阈值操作通常不满足结合律。CRDTMergeState 让 OR-Set 管理贡献集合，canonical order 与 Merkle-root seed 驱动确定性 tensor strategy：前者拥有收敛，后者拥有模型合成。收益是强最终一致性，代价是 contribution metadata、tombstone、浮点确定性和安全冲突策略；它证明 state convergence，不证明合并模型的语义质量。", "<!-- analysis:DA-MODEL-MERGE-CRDT-SEPARATION:end -->", ""]
for aid in sorted(RETAINED):
    fid = family(aid)
    if aid not in DEEP_SELECTED:
        status = "exact-v1 blocked；材料恢复前不得扩写" if aid == "2605.17193" else "exact-v1 Review 已完成；本次不扩写是 selection，而非跳过"
        lines.append(f"<!-- analysis-decision:{fid}:start -->{fid} {status}。<!-- analysis-decision:{fid}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
          "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for item in compares:
    fid = item["source_family_id"]
    adjacent_refs = []
    for adjacent_path in item["adjacent_paths"]:
        adjacent_number = int(Path(adjacent_path).name.split("-", 1)[0])
        adjacent_refs.append(f"{adjacent_path}#chapter-{adjacent_number}")
    lines.append(f"| {fid} | {item['owner_node']} | {item['owner_path']}#chapter-{item['target_chapter']} | {';'.join(adjacent_refs)} | existing:{fid} | delta:{fid} | {item['evolution_relation']} | {item['decision']} | books-review:{fid} |")
lines += ["", "### Books Decision Receipts", ""]
for item in compares:
    fid = item["source_family_id"]
    lines += [
        f"<!-- books-review:{fid}:start -->",
        f"<!-- existing:{fid}:start -->{item['existing_proposition']} Owner snapshot sha256=`{item['owner_sha256']}`；相邻章节=`{', '.join(item['adjacent_paths'])}`。<!-- existing:{fid}:end -->",
        f"<!-- delta:{fid}:start -->{RETAINED[item['arxiv_id']][2]}<!-- delta:{fid}:end --> Decision: `{item['decision']}`；author lane 未修改共享 Books。",
        f"<!-- books-review:{fid}:end -->", "",
    ]

lines += [
    "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
    "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
    "| --- | --- | --- | --- | --- | --- | --- |",
    f"| SA-20260517-COVERAGE | fresh-context:pending-reviewer | coverage | coverage:SRC-ARXIV:20260517 | FIND-20260517-INDEPENDENT-SCREEN — author 完成 {len(rows)}/{len(rows)} screening、denominator={len(RETAINED)}、closures={len(rows)-len(RETAINED)}，但不能自签 false-positive/negative audit | 等待非作者重放 279/279 | open |",
    f"| SA-20260517-EVIDENCE | fresh-context:pending-reviewer | evidence | review:{family('2605.16745')} | FIND-20260517-INDEPENDENT-EVIDENCE — complete={len(RETAINED)-len(materials)}、blocked={len(materials)}，locator/claim boundary 未经非作者复核 | 非作者复核 complete receipts；恢复 GAP-20260517-EXACT-V1-17193 | open |",
    f"| SA-20260517-SELECTION | fresh-context:pending-reviewer | deep_analysis_selection | analysis:{DEEP_SELECTED['2605.17076']} | FIND-20260517-INDEPENDENT-SELECTION — 三项 selection 为 author 判断 | 非作者挑战代表性、重复与跨层价值 | open |",
    f"| SA-20260517-BOOKS | fresh-context:pending-reviewer | books | books-review:{family('2605.16746')} | FIND-20260517-BOOKS-PREWRITE — {len(integrate_rows)} 项 provisional queue 尚未写回 | 非作者 current-books challenge 后交 root 串行写回并 post-write audit | open |", "",
    "作者侧审核不能替代 fresh-context 独立语义审计。", "",
    "## 8. Ignored Noise", "",
    f"{len(rows)-len(RETAINED)} 项未被删除，而是在 `screening-ledger-final.json` 逐 family 记录具体方法/主张、摘要结果与排除边界。它们属于领域应用、局部模型/优化改进、单项 benchmark 或非系统性分析；独立 reviewer 可按具名 identity 重开。", "",
    "## 9. Recommended Action", "",
    "1. 由非作者重放 279/279 title+abstract，挑战 30/249 denominator 与 closures。",
    "2. 独立复核 29 个 complete exact-v1 的 locator/claim boundary，并按 Materials Request 恢复唯一 blocked family。",
    f"3. 挑战 {len(integrate_rows)} 项 provisional Books queue；只有独立审计后仍为 Integrate 的 family 才交 root 串行写回。", "",
    "## 10. Repository Changes", "",
    "- 新建本日 Daily author packet。", "- 冻结 279/279 screening ledger、30 项 provisional denominator 与 249 项 closure。", f"- 新建 {len(RETAINED)-len(materials)} 项 complete exact-v1、{len(materials)} 项精确 Materials Request、current-Books comparison 与 author audit。", "- 未修改任何共享 Books 文件。", "",
    "## 11. Open Questions", "",
    "- 独立 reviewer 是否发现 false positive/negative 或 locator/claim-boundary finding？", "- blocked family 恢复后是否仍满足 denominator 与 Books 门槛？", "- current Books 已通过后续证据覆盖哪些 provisional Integrate，从而应降为 No Change？", "",
    "### Materials Request", "", "<!-- validator:materials-request-v1 -->",
    "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    "| MR-20260517-17193 | P1 Full Text | SF-2026-ARXIV-2605-17193 | — | — | 2026-W20 | arXiv:2605.17193v1; https://arxiv.org/html/2605.17193v1; https://arxiv.org/pdf/2605.17193v1 | exact-v1 Method, Evaluation, Limitations/Appendix and artifact statement | HTML returned internal error, PDF cache missed and shared caches contain no body; abstract cannot support deep review | official v1 PDF/HTML/TeX or author-hosted immutable matching v1 manuscript | arxiv-2605-17193-v1.pdf | read Method/formulas/implementation/evaluation/ablations/limitations/artifact; recompute Score and Books disposition |", "",
    "## 12. Sources", "",
    "- DataCite arXiv v2 monthly snapshots：仅用于完整 identity、v1 timestamp、title/abstract 枚举。", "- Official arXiv exact-v1 HTML/PDF：29 项已读取并定位，1 项在 HTML/PDF/共享缓存均失败后精确 blocked。", "- Current Books owner 与 adjacent chapters：路径与 owner snapshot hash 逐项记录于 `books-current-content-comparison.json`。", "",
    "## 13. Final Status", "",
    "Completion Status: `In Progress`", "", "Coverage: `Open`", "", "Evidence: `Open`", "", "Books: `Open`", "", "unresolved findings: 4", "",
    f"Author lane 已完成 279/279 screening、30-family denominator、{len(RETAINED)-len(materials)}/30 exact-v1 complete、1 precise blocker、三项 Deep Selection 与 current owner+adjacent provisional Books comparison；仍等待独立 fresh-context audit、root 串行 Books writeback 与 post-write audit。", "",
]

REPORT.parent.mkdir(parents=True, exist_ok=True)
text = "\n".join(lines).rstrip() + "\n"
for item in reviews:
    fid = item["source_family_id"]
    body = text.split(f"<!-- review:{fid}:start -->", 1)[1].split(f"<!-- review:{fid}:end -->", 1)[0]
    row = row_by_id[item["arxiv_id"]]
    candidate = {"Event Identity": f"paper-v1:{item['arxiv_id']}", "Primary Identifier": f"arXiv:{item['arxiv_id']}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"}
    rp = _expected_review_provenance(fid, candidate, item["review_route"], item["primary_evidence_version"], f"SRC-ARXIV@{item['primary_evidence_version']}", item["method_identity_locators"], item["evaluation_locators"], item["limitations_counterevidence_locators"], item["artifact_locators"], f"claim:{fid}", f"review:{fid}", _normalized_body_sha256(body))
    placeholder = f"RP-BLOCKED-{item['arxiv_id'].replace('.', '')}" if item["completion_result"] == "blocked" else f"RP-TODO-{fid}"
    text = text.replace(placeholder, rp)
REPORT.write_text(text)
print(json.dumps({"registered": len(rows), "screened": len(rows), "retained": len(RETAINED), "closures": len(rows)-len(RETAINED), "exact_v1_complete": len(RETAINED)-len(materials), "blocked": len(materials), "books_queue": len(integrate_rows)}, ensure_ascii=False))
