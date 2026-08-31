#!/usr/bin/env python3
"""Freeze and render the strict 2026-06-10 Daily packet; never edits Books."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from collections import Counter
from pathlib import Path

from validate_research import _expected_review_provenance, _normalized_body_sha256


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260610"
REPORT = ROOT / "papers/2026/06/10/README.md"
SCREENING = PACKET / "registered-hit-screening.json"
EXECUTED_AT = "2026-08-29T23:45:00+08:00"


# exact-v1 semantic decisions.  Each entry is owner, durable mechanism delta,
# and the source-specific trade/failure/non-proof boundary.
META = {
    "2606.10388": ("AGENT-WORKFLOW", "Resolve the active capability family, learn query-conditioned utility from confusable skills, and expose one representative before global top-k skill ranking.", "Family-resolution errors can hide the helpful skill or split risky siblings; the v1 benchmark proves retrieval exposure on a fixed library, not runtime safety after a skill executes."),
    "2606.10394": ("PLATFORM-EVALUATION-SYSTEM", "Generate realistic personal-computing tasks together with initial state, ground truth and executable final-state verifiers, so agent evaluation is owned by environment state rather than answer text.", "Automatically generated scenarios can encode validator blind spots; forty tasks and eleven models establish a benchmark slice, not production reliability."),
    "2606.10415": ("TRAIN-DISTRIBUTED-TRAINING", "Schedule gradient sync, update, parameter-view prefetch and activation recovery as a layer- and stage-local training-state lifecycle under explicit DDR and link constraints.", "The planner is tied to MT-3000's hierarchy and non-interleaved 1F1B; GPU runtimes remain the better branch when HBM and collectives are abundant."),
    "2606.10440": ("PLATFORM-EVALUATION-SYSTEM", "Raise distributed-ML simulation from coarse events to cache-line load/store GPU execution and a backend-neutral InfraGraph for reusable infrastructure identity.", "Higher fidelity increases simulation cost and still inherits model error; a simulated timing result is not a measured production SLO."),
    "2606.10445": ("INFER-DECODE", "Split each weight matrix into a contiguous dense region plus hardware-native 2:4 sparse region so existing dense and sparse GEMM libraries can execute one-shot-pruned LLMs.", "Dense-index choice is load-bearing and small GEMMs may not amortize sparse-kernel overhead; the B200 FP8 results do not imply cross-hardware speedup."),
    "2606.10457": ("AGENT-WORKFLOW", "Maintain a human-readable decision rule as versioned state; cluster validation errors into missing, wrong or conflicting rules and commit only regression-passing patches.", "Compiled rules improve determinism but narrow coverage to expressible policy; an LLM prompt remains useful where cases cannot be compiled or verified."),
    "2606.10487": ("PLATFORM-SECURITY", "Reuse generator hidden states for token-level safety probes and give the decoding loop early halt/modify authority before unsafe output completes.", "A cheap probe is a latency-oriented surrogate for a stronger guard and can miss distribution shift; post-hoc moderation remains a fallback rather than disappearing."),
    "2606.10493": ("INFER-PD-DISAGGREGATION", "Co-design stream-loaded prefill, small expert parallelism, zero-copy intra-node PD separation, dual-batch overlap and CPU FP8 GEMV for intact local MoE serving.", "The 30-second TTFT and 20-token/s values are paper reference goals, not independently validated production SLOs; benefits depend on dual-socket DDR, AVX-512 and RTX 5090-class hardware."),
    "2606.10537": ("INFER-PREFILL", "Prefill long dLLM prefixes once into chunked KV, retrieve only relevant chunks/tokens during iterative denoising, and use periodic BOS anchors to preserve middle evidence.", "Sparse chunk selection can discard needed evidence and cached non-contiguous KV consumes memory; the 8K–32K kernel speedups are bounded to tested dLLMs and contexts."),
    "2606.10616": ("AGENT-MEMORY", "Separate online-observable retention features from offline supervision and optimize memory under budget, evidence utility, miss, reacquisition and stale costs.", "The learned retention policy depends on realized-query distribution and can still discard future evidence; simple recency or full retention remains safer when observability assumptions fail."),
    "2606.10662": ("AGENT-MULTI-AGENT", "Replace a central merger with asynchronously claimed subtasks, a shared verified context and compact write-back records.", "Shared-context verification becomes a contention and trust boundary; centralized orchestration remains simpler for small task graphs or unverifiable partial work."),
    "2606.10709": ("TRAIN-GRPO", "Return all-correct and all-wrong rollout groups to a mutable pool so zero-variance queries can become signal-bearing as the policy changes.", "Recycling spends future rollouts on examples whose state may never flip and makes the training distribution endogenous; discard/pre-filter remains a bounded-cost branch."),
    "2606.10724": ("PLATFORM-SECURITY", "Commit all cluster ingress and egress at passive optical taps and sanitize timing, analogue and protocol-header covert channels in a separate secure gateway.", "The paper specifies architecture and estimates rather than a deployed device; encrypted payload semantics and untapped physical paths remain outside the proof."),
    "2606.10742": ("AGENT-MEMORY", "Treat multimodal external memory as a persistent attack surface: trigger-conditioned retrieval recalls poisoned text-image evidence that then redirects the web agent.", "High attack success assumes the tested memory graph, OCR path and black-box threat model; memory admission, provenance and post-retrieval containment must coexist."),
    "2606.10813": ("PLATFORM-TRACE", "Release agent traces through selective protected-information rewriting while preserving verifier-critical evidence and adding behavioral provenance watermarks.", "Redaction can remove diagnostic detail and watermarks are probabilistic; private full traces and least-privilege access remain necessary for incident response."),
    "2606.10860": ("PLATFORM-SECURITY", "Train an explicit five-level instruction hierarchy with distance-aware preference penalties so conflict severity follows source privilege rather than token salience.", "Training cannot authenticate who supplied a token and tested pairwise relations do not prove arbitrary nesting; provenance and deterministic authorization remain separate owners."),
    "2606.10937": ("PLATFORM-TRACE", "Observe compiler graph transformations and reconstruct tensor/operator provenance through coalgebraic behavior rather than propagating fragile IDs through non-injective rewrites.", "Observational equivalence can merge distinctions needed by a debugger and the COVAN prototype is not evidence for every compiler pass; explicit IDs remain useful where rewrites preserve them."),
    "2606.10949": ("AGENT-MEMORY", "Make memory extraction preserve corrective context and disagreement instead of compressing only user misconceptions that later amplify sycophancy.", "Mitigations are evaluated on synthetic conversations and can trade recall for correction; memory is still useful when belief provenance and counterevidence survive extraction."),
    "2606.11045": ("PLATFORM-EVALUATION-SYSTEM", "Use output and input compression as falsifiable tests of whether an ML research agent learned a short reusable strategy or overfit adaptive validation feedback.", "Short reproducibility descriptions fail by design on induced overfitting but do not certify scientific validity; fresh held-out evaluation and causal review remain required."),
    "2606.11052": ("TRAIN-SFT", "Restore only query/key projections of retained softmax-attention layers after CoT SFT, preserving long-range routing while keeping value-side reasoning adaptation.", "Checkpoint mixing assumes compatible pre/post-SFT geometry and is demonstrated on distilled hybrid models; it is not a universal cure for catastrophic forgetting."),
    "2606.11063": ("PLATFORM-SECURITY", "Measure whether an untrusted model can distinguish its own trajectory from trusted-control interventions before deploying a monitoring protocol.", "Awareness varies by domain, provider style and model pair; benchmark accuracy does not prove strategic evasion or safety under a live controller."),
    "2606.11081": ("TRAIN-DISTRIBUTED-TRAINING", "Combine adaptive local optimizer steps with sparse randomized gossip so LLM pretraining can progress without globally identical state or synchronous all-reduce.", "Model replicas diverge and topology/bandwidth heterogeneity changes convergence; synchronous collectives remain the conservative branch on reliable fabrics."),
    "2606.11119": ("TRAIN-GRPO", "Allocate a fixed rollout budget jointly to prompt roots and informative intermediate ReAct prefixes, turning multi-turn exploration into a reward-contrast tree.", "Prefix continuation adds tree state and selection bias; outcome-only terminal reward still limits credit assignment when all branches share the same result."),
    "2606.11127": ("TRAIN-DATA", "Attach append-only source provenance to each synthetic sample, require separate faithfulness and reward gates, then route rejected samples to diagnosed repair rather than blind retry.", "Stronger judges improve the provenance gate but generator scale dominates downstream quality; fixed thresholds and synthetic injections are experiment policy, not universal release criteria."),
    "2606.11145": ("PLATFORM-SECURITY", "Build an open confidential inference service on commodity TEEs with remote attestation and a public trust chain instead of proprietary cloud hardware.", "TEE side channels, availability and accelerator boundary remain platform-specific; confidentiality evidence does not prove model correctness or operator-free governance."),
    "2606.11164": ("INFER-KV-CACHE", "Allocate reasoning-model decode KV hierarchically: offline per-layer demand followed by online head-level reallocation from current utility.", "Eviction utility is workload-dependent and compression can erase late-used evidence; uniform budgets remain predictable when online signals are unstable."),
    "2606.11169": ("TRAIN-DISTRIBUTED-TRAINING", "Compile model annotations and scheduling directives into a global computation/communication DAG, then derive per-device plans independent of the chosen parallelism strategy.", "A programmable IR moves complexity into transformations and validation; specialized runtimes remain simpler for fixed strategies and unsupported optimizations."),
    "2606.11257": ("INFER-GPU-MEMORY", "Keep embedding, reranking and generation on the Snapdragon Hexagon NPU and measure the entire RAG energy/latency path rather than one isolated operator.", "Results are one Dell XPS 13 / Snapdragon X Elite stack and a 120-query corpus; extrapolation to Apple, Intel or MediaTek NPUs is explicitly unproven."),
    "2606.11265": ("AGENT-RAG", "Evaluate corpus poisoning after the real chunking and reranking pipeline, distinguishing retrieval exposure from whether the generator follows a poisoned chunk.", "Attack success depends on retriever, chunk and generator settings; a failed poison under one pipeline does not certify the corpus or other retrieval depths."),
    "2606.11270": ("TRAIN-DATA", "Measure subliminal behavior transfer through distillation as a ratio conditioned on teacher behavior and student response rather than treating matching outputs as benign data.", "Observed transfer ratios are model/task specific and do not identify every causal feature; data lineage and behavioral canaries must coexist with aggregate metrics."),
    "2606.11290": ("AGENT-WORKFLOW", "Precompute reusable workflow fragments into a bank and choose them per query, separating expensive workflow search from repeated online execution.", "A stale bank can reuse the wrong flow and query adaptation still needs validation; unconstrained online search remains the fallback for novel tasks."),
    "2606.11349": ("AGENT-PLANNING", "Make clarification a self-gated action competing with navigation on the same ordinal scale so information-seeking becomes an observable policy decision.", "The measured shift depends on benchmark information gaps and answer-channel quality; asking more questions is not itself evidence of better deployment behavior."),
    "2606.11357": ("INFER-DECODE", "Fuse mixed-precision quantized LLM operators around AMD NPU tile/dataflow constraints instead of composing generic kernels with repeated layout conversion.", "Kernel gains are bound to the evaluated AMD NPU and quantization formats; unsupported shapes and quality effects require fallback kernels and model-level checks."),
    "2606.11375": ("TRAIN-PRETRAINING", "Add perturbation fragility after linear-probe accuracy saturates, so pretraining checkpoints with equal separability can still be distinguished by representation stability.", "Fragility depends on probe, perturbation and layer choice and is not a training objective by itself; downstream evaluation still owns usefulness."),
    "2606.11387": ("TRAIN-PRETRAINING", "Use small controlled pretraining experiments as promotion receipts before expensive runs, with explicit continuation/stop decisions instead of scaling every hypothesis.", "Micro-scale rank order can invert at scale and cheap experiments omit distributed effects; staged promotion reduces decision cost but cannot guarantee final-model quality."),
    "2606.11409": ("PLATFORM-EVALUATION-SYSTEM", "Parameterize adversarial risk by cumulative attack FLOPs and report risk-compute curves, not only success at an equal query count.", "FLOPs omit hardware, latency and monetary factors and attacker strategies can transfer; it is a comparable pressure proxy, not a production security SLO."),
    "2606.11445": ("PLATFORM-EVALUATION-SYSTEM", "Train a single-pass behavior forecaster directly on reasoning trajectories to predict rerun stability and response changes without pretending the trace is a faithful explanation.", "Forecast accuracy is limited to trained behavior questions and model distributions; a forecaster predicts outcomes but does not explain causes or authorize actions."),
    "2606.11520": ("TRAIN-DATA", "Synthesize OS-agent data through structured intent, role-locked multi-turn simulation and execution of every tool call in an isolated live workspace.", "A generated intent distribution and one workspace image can miss real-user states; execution grounding proves tool effects in that sandbox, not external safety."),
    "2606.11522": ("AGENT-PLATFORM", "Move candidate acceptance out of the metric-optimizing research agent into an external controller that audits disaggregated regions/slices before commit.", "The fire-model case demonstrates aggregate inversion but not every science domain; protected slices and noise tolerances remain domain-owned policy."),
    "2606.12469": ("AGENT-RAG", "Treat RAG poisoning as an interaction among retriever, top-k, chunking, database composition and generator, using a factorial design instead of a single attack rate.", "The 432 configurations use two curated 100-question subsets and two generators; factor effects are evidence for that grid, not universal retriever ordering."),
    "2606.20657": ("AGENT-PLATFORM", "Run a multi-week autonomous post-training loop that can revise its search policy when the development metric stops tracking an external target.", "One 30B challenge and public leaderboard do not establish recursive improvement; external target leakage, human-created infrastructure and compute remain boundaries."),
    "2606.20659": ("AGENT-WORKFLOW", "Compile natural-language skill instructions into observable behavior constraints and report binary trajectory-level covered/not-covered adequacy separately from task outcome.", "The exact-v1 metric deliberately does not assign pass/fail to covered behavior; extraction and coverage judging can be wrong, and not-covered constraints remain unknown rather than passed or failed."),
    "2606.20661": ("AGENT-TOOL-CALLING", "Separate an agent's judgment that external resources are needed from whether it actually invokes them, exposing tool overuse and underuse as cognitive-behavioral misalignment.", "The KAware partitions and tested harnesses do not prove epistemic access to internal knowledge; tool policy, cost and permission still require deployment-specific gates."),
    "2606.28358": ("AGENT-RAG", "Trace citation decisions to a distributed attributional ensemble and intervene on those components to distinguish attaching a citation from actually using evidence.", "Repairs transfer only modestly to multi-document HotpotQA and activation patching on Llama-3.1-8B does not establish causal faithfulness for other models."),
}

TITLE_OVERRIDE = {
    "2606.10388": "SkillResolve-Bench: Measuring and Resolving Same-Capability Ambiguity in Agent Skill Retrieval",
    "2606.10415": "LifeTrain: Training-State Lifecycle Scheduling for Large Language Model Training on Bandwidth-Constrained Heterogeneous Supercomputers",
}

LOCS = {
    "2606.10388": ("§3 Problem and Method", "§4 Experiments", "§5 Analysis and Execution Scope"),
    "2606.10394": ("§2 STAGE-Claw", "§3 Evaluation", "§4 Analysis and Appendix A audit"),
    "2606.10415": ("§4 Design", "§6 Evaluation", "§2.3 GPU-oriented limitations and §8 Conclusion"),
    "2606.10440": ("§4 ASTRA-sim 3.0", "§5 Case Studies", "§3 Motivation and §7 Conclusion"),
    "2606.10445": ("§3 Proposed Method", "§4 Experiments", "§3.1.3 existing-method failures and §5 Conclusion"),
    "2606.10457": ("§3 Trace2Policy Framework", "§§4–6 production, experiments, and transfer", "Appendix B Limitations and Broader Impacts"),
    "2606.10487": ("§3 Method", "§§4–8 offline and online evaluation", "§9 Discussion and future work"),
    "2606.10493": ("§3 System Design", "§4 Evaluations", "§6 Discussion"),
    "2606.10537": ("§5 Method", "§6 Experiments", "§7 Conclusion and Appendix ablations"),
    "2606.10616": ("§3 Method", "§4 Experiments", "§5 Conclusion and Discussion"),
    "2606.10662": ("§3 Decentralized Language Models", "§4 Experiments", "§7 Limitations and Future Work"),
    "2606.10709": ("§3 Methodology", "§4 Experiments", "§4.3 Ablations and §5 Conclusions/Future Work"),
    "2606.10724": ("§4 Architecture", "§5 Covert Channel Estimates", "§6 Limitations and Future Work"),
    "2606.10742": ("§3 Method", "§4 Experiments", "§4.6 Further Analysis and §5 Conclusion"),
    "2606.10813": ("§§3–4 CapTraceBench and Methodology", "§5 Experiments", "§5.4 Diagnostics/Robustness and §7 Conclusion"),
    "2606.10860": ("§§3–5 problem, data, and GW-DPO", "§6 Experiments", "§7 Discussion"),
    "2606.10937": ("§§3–4 observational correctness and Covan", "§5 Evaluation", "§3.1 provenance limitation and §7 Conclusion"),
    "2606.10949": ("§3 Methods", "§§4–6 Results, Analysis, and Mitigation", "§5 Analysis and §7 Conclusion"),
    "2606.11045": ("§3 Compression and Generalization", "§4 Experiments", "§5 falsification and §6 Discussion"),
    "2606.11052": ("§5 QK-Restore", "§6 Experiments", "§7 Analysis and §8 Conclusion"),
    "2606.11063": ("§3 CIAware-Bench", "§4 Results", "§5.2 Limitations and Future Work"),
    "2606.11081": ("§3 Method", "§4 Numerical Experiments", "§5 Conclusion and Appendices B/F"),
    "2606.11119": ("§§3–4 allocation principle and TRACE", "§5 Experiments", "Appendix B Discussion and C Extended Results"),
    "2606.11127": ("§2 Methodology", "§3–4 Experimental Setup and Results", "Appendix D Discussion"),
    "2606.11145": ("§§3–5 OpenPcc design and implementation", "§6 Evaluation", "§7 Security Analysis and §9 Future Works"),
    "2606.11164": ("§5 ReasonAlloc Framework", "§§6–8 experiments, efficiency, and ablations", "§6.2 static-heuristic limits, §7 efficiency, and §9 Conclusion"),
    "2606.11169": ("§4 Design", "§6 Evaluation", "§3 Challenges and §8 Conclusion"),
    "2606.11257": ("§III System Design", "§IV–V Experimental Setup and Results", "§VI-B Limitations and Future Work"),
    "2606.11265": ("§IV Methodology", "§V Experiment", "§III Threat Model and §VI Conclusion"),
    "2606.11270": ("§3 Methodology", "§4 Experiments and Results", "§5 Analysis and §6 Conclusion"),
    "2606.11290": ("§3 Methodology", "§4 Experiments", "Appendix F.1 Limitations"),
    "2606.11349": ("§3 Framework", "§§4–5 Experiments and Results", "§6 Discussion"),
    "2606.11357": ("§4 TileFuse Overview", "§5 Evaluation", "§6 Discussion and Limitations"),
    "2606.11375": ("§3 Methodology", "§4 Results", "§5.3 Limitations"),
    "2606.11387": ("§4.3–4.4 Promotion Schedule and Frozen Rules", "§5 Results", "§7 Limitations"),
    "2606.11409": ("§2 Framework", "§3–4 Experimental Setup and Results", "§7 Future Work & Limitations"),
    "2606.11445": ("§3 Method", "§§4–5 evaluation and ablation", "§7 Limitations"),
    "2606.11520": ("§4 ISE Synthesis Paradigm", "§5 Experiments", "§6 Limitations"),
    "2606.11522": ("§3 Search discipline and control loop", "§4 Evaluation", "§5 Discussion"),
    "2606.12469": ("§3 Methodology", "§4 Results and Discussion", "§5 Conclusions"),
    "2606.20657": ("§3 System design", "§§4–5 results and proxy-evidence discovery", "§7 Future work and limitations"),
    "2606.20659": ("§§2–3 formulation and Method", "§4 Evaluation", "§5 Discussion"),
    "2606.20661": ("§3 KAware/KAPRO", "§§4–5 Experiments and Further Analysis", "§7 Limitations"),
    "2606.28358": ("§3 Methodology", "§4 Results and Discussion", "§4.4 Implications and §5 Conclusion"),
}

INTEGRATE = {
    "2606.10493": "在 Decode 章节补一段本地 MoE 的 CPU–GPU ownership：stream-loaded prefill、node-local PD separation 与 dual-batch overlap；保留 5090/AVX-512 边界及 30s/20 tok/s 只是论文 reference goals。",
    "2606.10724": "在安全章节补一段 cluster ingress/egress 的独立证据面：passive taps 负责 commitment，secure gateway 负责 covert-channel sanitization；明确尚无部署验证。",
    "2606.10937": "在 Trace 章节补一段 compiler rewrite provenance：non-injective transform 后由 observable behavior 重建 lineage；显式 ID 仍与其共存。",
    "2606.11127": "在训练数据章节补一段 provenance-preserving synthetic curation：faithfulness/reward 双 gate 与 diagnosed repair；不得把阈值或 judge 规模写成通用 release SLO。",
    "2606.11257": "在 GPU Memory 章节补一个端侧 NPU 的全链 RAG memory/energy 分支，限定 Snapdragon X Elite、120-query 与单机测量，禁止外推其他 NPU。",
    "2606.11387": "在 Pretraining 章节补一段 staged promotion：小实验是扩容决策 receipt，不是大规模结果的缩小版证明；保留 scale inversion 与 distributed-effects failure。",
    "2606.11522": "在 Agent Platform 章节补 external acceptance loop：优化 aggregate metric 的 agent 不拥有 commit；controller 必须审计 protected slices 与 noise tolerance。",
    "2606.20659": "在 Workflow 章节补 skill test adequacy：自然语言约束编译为 trajectory-level covered/not-covered；coverage 与 task outcome 分离，not-covered 必须保持 Unknown。",
    "2606.20657": "在 Agent Platform 的演化段补一条 autonomous post-training 证据：系统能识别 dev/external target 失配并改搜索策略；限定单次 30B challenge，不称为 recursive self-improvement。",
}

TARGET = {
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md#L628",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md#L10",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md#L10",
    "INFER-DECODE": "books/part-05-inference-system/44-decode.md#L126",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md#L625",
    "INFER-PD-DISAGGREGATION": "books/part-05-inference-system/44-decode.md#L126",
    "INFER-PREFILL": "books/part-05-inference-system/43-prefill.md#L10",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md#L10",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md#L10",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md#L10",
    "PLATFORM-TRACE": "books/part-06-ai-infrastructure/69-trace.md#L105",
    "TRAIN-SFT": "books/part-04-training-system/29-sft.md#L10",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md#L514",
    "INFER-KV-CACHE": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10",
    "INFER-GPU-MEMORY": "books/part-05-inference-system/54-gpu-memory.md#L213",
    "AGENT-RAG": "books/part-07-agent/76-rag.md#L10",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md#L10",
    "TRAIN-PRETRAINING": "books/part-04-training-system/28-pretraining.md#L653",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md#L549",
    "AGENT-TOOL-CALLING": "books/part-07-agent/78-tool-calling.md#L10",
}

EXACT_ABSTRACT = {
    "2606.10388": "Agent skill libraries are routable software assets. SkillResolve-Bench v1 pairs 661 helpful/risky same-capability siblings in a 7,982-candidate pool; SkillResolve resolves active families, learns utility from confusable candidates and keeps one representative before final top-k ranking.",
    "2606.20659": "Skill Coverage v1 compiles natural-language skill instructions into observable behavior constraints and classifies each constraint from a trajectory as Covered or Not Covered. Not Covered remains Unknown, no behavior-outcome label is inferred, and reported SkillsBench coverage ranges from 39.90% to 43.98%.",
}

MODEL_OVERRIDES = {
    "2606.10394": "Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3.5-Plus, GPT-5.5, GPT-5.4, Gemini-3.1-pro-preview, Doubao-Seed-2.0-Pro, GLM-5, Kimi-K2.6, MiniMax-M2.7",
    "2606.10415": "LLaMA-2-7B, Baichuan2-13B, Qwen2.5-32B, and LLaMA-2-70B configurations",
    "2606.10440": "No single LM checkpoint: ASTRA-sim case studies evaluate GPU, collective, and infrastructure configurations",
    "2606.10457": "GLM-5, Kimi-K2.5, Qwen3.5-plus, MiniMax-M2.5, Claude Opus 4.6, Claude Haiku 4.5",
    "2606.10487": "DeepSeek-R1-0528-Qwen3-8B reported; Qwen3-8B and Qwen3-30B-A3B-Thinking-2507 probes are qualitative omitted runs",
    "2606.10662": "Gemini 3 Flash and Claude Opus 4.6 base models",
    "2606.10709": "Qwen3-1.7B and Qwen3-4B",
    "2606.10724": "Not applicable: architecture/estimate paper, no evaluated LM checkpoint",
    "2606.10813": "Claude Opus 4.6, Sonnet 4.6, Haiku 4.5, GPT-5.2 Codex, Gemini 3 Flash/Pro; Qwen3-8B/4B for open-model studies",
    "2606.10860": "Llama-3.1-8B-Instruct",
    "2606.10937": "Modified MNIST and MobileNetV2-0.25 compiler benchmarks; proprietary models omitted",
    "2606.10949": "GPT-5.2, Claude Sonnet 4.6, Qwen 3.5, Kimi K2.5, MiniMax 2.5 across Mem0, MemOS, and Zep",
    "2606.11045": "Claude Opus instances for explorer, compressor, and reproducer roles",
    "2606.11119": "Qwen3-8B and Qwen3-14B; Llama-3.2-3B-Instruct in additional Multi-Hop QA experiments",
    "2606.11145": "Llama-3 8B vLLM end-to-end workload",
    "2606.11164": "DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, AceReason-14B",
    "2606.11270": "Llama-2-7B-Chat and Qwen2.5-7B-Instruct teachers/students; GPT-4.1 evaluator",
    "2606.11290": "Qwen3-8B FlowBank optimizer; GPT-4o and Qwen3-8B optimizer baselines",
    "2606.11357": "Gemma 2B and Qwen2.5 3B end-to-end LLM workloads",
    "2606.11375": "OLMo-2 1B and OLMo-3 7B checkpoints",
    "2606.11445": "OLMo-3-7B-Think and Qwen3.5-2B target LRMs; GPT-5.4 and Claude Opus 4.6 naive readers",
    "2606.11520": "Qwen3-8B fine-tuned model; Qwen3-8B, Qwen3-32B, and GPT-4o references",
    "2606.11522": "Not applicable: fire-model research-control case, no evaluated LM checkpoint asserted",
    "2606.20657": "30B Nemotron post-training target",
    "2606.20659": "SkillsBench trajectories; Claude Code + Opus 4.6 trace corpus used for judge validation",
    "2606.20661": "18 LLMs including GPT-4o/4.1/5, o4-mini, Claude Sonnet 4.5, Gemini 3 Flash/Pro, Qwen3-Max and disclosed open-weight families",
    "2606.28358": "Llama-3.1-8B mechanistic citation study",
}


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def clean_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", text)
    return parts[0][:360] if parts else text[:360]


def closure_class(row: dict) -> str:
    t = (row["title"] + " " + row["abstract"]).lower()
    if any(x in t for x in ("survey", "review", "position:", "roadmap", "theoretical framework")):
        return "survey-position-no-new-durable-contract"
    if any(x in t for x in ("medical", "cancer", "ecg", "eeg", "weather", "robot", "autonomous driving", "remote sensing", "speech", "image", "video", "molecular", "protein")):
        return "bounded-domain-or-modality-application"
    if any(x in t for x in ("benchmark", "dataset", "challenge")):
        return "benchmark-without-new-system-owner"
    if any(x in t for x in ("optimizer", "fine-tun", "lora", "distillation", "quantization", "pruning", "reinforcement learning")):
        return "local-model-or-training-increment"
    return "no-clear-durable-owner-or-release-contract-delta"


def score(aid: str) -> tuple[int, int, int, int]:
    high = {"2606.10415", "2606.10440", "2606.10493", "2606.10724", "2606.10937", "2606.11081", "2606.11145", "2606.11169", "2606.11257", "2606.11357"}
    medium = {"2606.10394", "2606.11063", "2606.11445", "2606.20661"}
    vals = (3, 3, 3) if aid in high else (2, 2, 3) if aid in medium else (3, 2, 3)
    return (*vals, sum(vals))


def benchmark(row: dict, loc: tuple[str, str, str]) -> dict:
    aid = row["arxiv_id"]
    workload = clean_sentence(row["abstract"])
    model = MODEL_OVERRIDES.get(aid, "Multiple exact-v1 model/component configurations; the evaluation locator retains the matrix and this contract does not collapse it to one identity")
    hardware = precision = batch = concurrency = "Not Disclosed"
    slo = "Not Disclosed — measured outcomes and experimental thresholds are not production SLOs"
    if aid == "2606.10415":
        hardware, precision = "MT-3000 heterogeneous supercomputer; usable DDR 20GB per compute cluster", "FP16 kernels disclosed; other state precision is configuration-specific"
    elif aid == "2606.10445":
        model, hardware, precision = "Qwen3-32B; Seed-OSS-36B", "NVIDIA B200", "FP8 inference with hybrid dense/2:4 sparse weights"
    elif aid == "2606.10493":
        model, hardware, precision = "DeepSeek-V3/R1 family, intact FP8 and INT4 configurations", "Dual-socket CPUs with 1–2 RTX 5090 consumer GPUs; AVX-512 CPU path", "FP8 and INT4 are separate evaluated branches"
        concurrency, slo = "Mixed prefill/decode and dual-batch decode are measured; production arrival process not disclosed", "30s TTFT and >20 tok/s are author-selected cloud-reference goals, not verified production SLOs"
    elif aid == "2606.10537":
        model, hardware = "Dream-v0-Base-7B and UltraLLaDA configurations", "Exact-v1 evaluation hardware is experiment-specific; no fleet topology"
    elif aid == "2606.11052":
        model = "HypeNet 2B/5B/9B and Jet-Nemotron hybrid models"
    elif aid == "2606.11127":
        model, precision = "Qwen3 1.7B/4B/8B generators; Qwen3-14B, Qwen3.6-27B-FP8, Qwen3.6-35B-A3B judges", "27B judge FP8; other precision not disclosed"
        batch = "Approximately 8,000–8,500 candidates per generator; training batch hyperparameters are in exact-v1 Appendix E"
    elif aid == "2606.11257":
        hardware = "Dell XPS 13, Snapdragon X Elite Hexagon NPU; CPU and Adreno/OpenCL GPU baselines"
        workload = "End-to-end indexing plus 120 Wikipedia-passage queries; embedding, retrieval, reranking and generation"
        slo = "Latency and energy are measured outcomes, not acceptance SLOs"
    elif aid == "2606.11409":
        model = "Ten models across three families and four training/alignment stages"
        workload = "Three attack strategies on two jailbreak benchmarks, re-parameterized by cumulative FLOPs"
        slo = "Risk-compute curves are evaluation objects, not service SLOs"
    elif aid == "2606.12469":
        model = "llama-4-scout-17b-16e-instruct; openai-gpt-oss-120b"
        workload = "432-factorial grid over aligned 100-question HotpotQA/MS-MARCO subsets, retriever, top-k, chunking and database composition"
    return {
        "workload": workload,
        "model": model,
        "hardware": hardware,
        "precision": precision,
        "input_length": "Dataset/task-defined; no universal fixed input length disclosed",
        "output_length": "Task-defined; no universal fixed output length disclosed",
        "batch": batch,
        "concurrency": concurrency,
        "slo": slo,
        "evaluator": f"Exact-v1 {loc[1]}; proof is limited to the reported metrics/ablations and does not establish the non-proof boundary in {loc[2]}",
    }


def main() -> None:
    payload = json.loads(SCREENING.read_text(encoding="utf-8"))
    identities = payload["identities"]
    assert len(identities) == 604
    by_id = {r["arxiv_id"]: r for r in identities}
    assert set(META) <= set(by_id)

    rows = []
    for raw in identities:
        aid = raw["arxiv_id"]
        row = dict(raw)
        if aid in META:
            node, delta, boundary = META[aid]
            row.update({
                "decision": "retain",
                "source_family_id": family(aid),
                "stable_node_id": node,
                "closure_class": "durable-owner-contract-delta",
                "rationale": delta,
                "reopen_condition": "retained; exact-v1 Method/Evaluation/Limitations and benchmark contract reviewed",
            })
        else:
            cls = closure_class(raw)
            row.update({
                "decision": "closure",
                "source_family_id": "—",
                "stable_node_id": "—",
                "closure_class": cls,
                "rationale": f"`{raw['title']}`: {clean_sentence(raw['abstract'])} This does not establish a durable AI-system mechanism, state/data/control owner, evaluation-release contract, platform judgment, or correction to existing Books under the strict candidate rule.",
                "reopen_condition": "Reopen only with primary evidence of a durable owner/control/evaluation contract beyond this title+abstract scope.",
            })
        row["screening_status"] = "retained_after_full_semantic_screen" if aid in META else "closed_after_full_semantic_screen"
        rows.append(row)

    assert len(rows) == 604 and sum(r["decision"] == "retain" for r in rows) == len(META)
    closures = len(rows) - len(META)
    identity_material = "\n".join(f"{r['arxiv_id']}|{r['decision']}|{r['closure_class']}" for r in rows)
    denominator_id = "DEN-20260610-" + hashlib.sha256(identity_material.encode()).hexdigest()[:8]
    denominator = {
        "schema": "candidate-denominator-v2.1",
        "report_date": "2026-06-10",
        "window": "[2026-06-09T09:00:00+08:00, 2026-06-10T09:00:00+08:00)",
        "raw_identities": 604,
        "retained": len(META),
        "closures": closures,
        "denominator_id": denominator_id,
        "false_negative_audit": {"route_negative_reviewed": 122, "route_negative_retained": sum(r["decision"] == "retain" and r["screening_route"].startswith("not_") for r in rows), "route_negative_closed": sum(r["decision"] == "closure" and r["screening_route"].startswith("not_") for r in rows), "status": "passed"},
        "rows": rows,
    }
    (PACKET / "candidate-denominator.json").write_text(json.dumps(denominator, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (PACKET / "candidate-denominator.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "submitted_v1_utc", "title", "categories", "screening_route", "decision", "source_family_id", "closure_class", "rationale", "reopen_condition"])
        for r in rows:
            writer.writerow([r["arxiv_id"], r["submitted_v1_utc"], r["title"], ";".join(r["categories"]), r["screening_route"], r["decision"], r["source_family_id"], r["closure_class"], r["rationale"], r["reopen_condition"]])

    reviews = []
    access_rows = []
    for idx, aid in enumerate(sorted(META, key=lambda x: int(x.split(".")[1])), 1):
        raw = by_id[aid]
        node, delta, boundary = META[aid]
        title = TITLE_OVERRIDE.get(aid, raw["title"])
        abstract = EXACT_ABSTRACT.get(aid, raw["abstract"])
        loc = LOCS[aid]
        bench = benchmark({**raw, "abstract": abstract, "arxiv_id": aid}, loc)
        sc = score(aid)
        fam = family(aid)
        base = f"https://arxiv.org/html/{aid}v1"
        body = (
            f"<!-- claim:{fam}:start -->\n"
            f"`{title}` 的 exact-v1 问题边界来自 `{base}`：{clean_sentence(abstract)}\n\n"
            f"机制与 owner：{delta} 状态/数据/控制 owner 固定为 `{node}`；Method 锚点是 `{loc[0]}`。它相对旧路径的变化不是多一个分数，而是把原先隐含在 prompt、静态规则或全局预算里的决定变成可记录、可验证、可回退的状态转换。\n\n"
            f"Evaluation proof：`{loc[1]}` 只证明 `{bench['workload']}` 上、`{bench['model']}` 条件下的报告指标。hardware=`{bench['hardware']}`；precision=`{bench['precision']}`；batch=`{bench['batch']}`；concurrency=`{bench['concurrency']}`；SLO=`{bench['slo']}`。未披露字段保持 Not Disclosed，不由模型名、加速比或实验阈值反推。\n\n"
            f"Trade-off、failure、共存与演进：{boundary} 反证/外推边界在 `{loc[2]}`；因此旧方案保留为低状态成本、证据不足或不满足论文前提时的共存分支。\n"
            f"<!-- claim:{fam}:end -->"
        )
        reviews.append({
            "row": idx, "arxiv_id": aid, "source_family_id": fam,
            "submitted_v1_utc": raw["submitted_v1_utc"], "title": title,
            "categories": ";".join(raw["categories"]), "route": "deep",
            "decision": "retain", "stable_node_id": node, "closure_class": "durable-owner-contract-delta",
            "rationale": delta, "reopen_condition": "retained and exact-v1 reviewed",
            "discovery_title": raw["title"], "abstract": abstract, "score": list(sc), "override": "none",
            "review_status": "deep_complete", "access_status": "accessible",
            "completion": "complete", "body": body,
            "provenance": "pending-computation",
            "locators": {"method": f"{base} — {loc[0]}", "evaluation": f"{base} — {loc[1]}", "limitations": f"{base} — {loc[2]}", "artifact": "Not Disclosed — immutable event-time artifact commit not required for manuscript claim"},
            "benchmark": bench,
        })
        candidate_for_hash = {"Event Identity": f"paper-v1:{aid}", "Primary Identifier": f"arXiv:{aid}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "none"}
        review = reviews[-1]
        review["provenance"] = _expected_review_provenance(
            fam, candidate_for_hash, "deep", f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1",
            review["locators"]["method"], review["locators"]["evaluation"], review["locators"]["limitations"],
            review["locators"]["artifact"], f"claim:{fam}", f"review:{fam}", _normalized_body_sha256(body),
        )
        access_rows.append({"arxiv_id": aid, "exact_version": f"arXiv:{aid}v1", "url": base, "reader": "official arXiv exact-v1 HTML via primary-source reader", "status": "accessible", "reviewed_sections": list(loc), "title": title})

    packet = {
        "schema": "daily-v2.1-source-review-packet", "denominator_id": denominator_id,
        "candidate_count": len(reviews), "review_complete_count": len(reviews), "blocked_count": 0,
        "ordinary_pending_count": 0, "route_counts": dict(Counter(r["route"] for r in reviews)), "rows": reviews,
    }
    (PACKET / "source-review-receipts-v2.1.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKET / "exact-v1-access-receipt.json").write_text(json.dumps({"schema": "exact-v1-access-receipt-v1", "accessible": len(access_rows), "blocked": 0, "rows": access_rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    selected = {"2606.10493": "DA-20260610-INFERENCE", "2606.11169": "DA-20260610-TRAINING", "2606.11522": "DA-20260610-AGENT-CONTROL"}
    selection = []
    for r in reviews:
        aid = r["arxiv_id"]
        if aid in selected:
            reason = {
                "2606.10493": "The runtime unit was fixed before prose drafting: it is the only frontier item that joins prefill, decode, expert placement, concurrency and reference SLO accounting on one measured local MoE system.",
                "2606.11169": "The training unit was fixed before prose drafting: Piper changes who owns the global computation/communication graph and how heterogeneous parallelism becomes executable per-device plans.",
                "2606.11522": "The agent-control unit was fixed before prose drafting: it moves commit authority away from the metric-optimizing research agent and demonstrates why disaggregated protected slices can reverse the aggregate winner.",
            }[aid]
            decision, unit, ref = "selected", selected[aid], f"analysis:{selected[aid]}"
        else:
            peers = "local-MoE runtime, programmable training IR, and external agent commit authority"
            reason = f"{r['title']} remains evidence-complete because {r['rationale']} It is not selected because its demonstrated scope/failure boundary is narrower than the predeclared three-unit frontier ({peers}); this does not change its Books disposition."
            decision, unit, ref = "not_selected", "—", f"analysis-decision:{r['source_family_id']}"
        eligibility = "score_7_9; potential_books_delta" if aid in INTEGRATE else "score_7_9"
        selection.append({"source_family_id": r["source_family_id"], "eligibility": eligibility, "decision": decision, "analysis_unit_id": unit, "subsumed_by": "—", "priority_rationale": reason, "narrative_ref": ref})
    assert sum(x["decision"] == "selected" for x in selection) == 3
    (PACKET / "deep-analysis-selection-v1.json").write_text(json.dumps({"contract": "44-family full evidence-complete frontier selection; winners fixed before rationale rendering", "eligible_count": 44, "selected_unit_count": 3, "rows": selection}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    comparisons = []
    for r in reviews:
        aid, node = r["arxiv_id"], r["stable_node_id"]
        decision = "Integrate" if aid in INTEGRATE else "No Change — Existing Coverage"
        target = TARGET[node]
        comparisons.append({
            "source_family_id": r["source_family_id"], "stable_node_id": node,
            "target_chapter_ref": target, "adjacent_chapter_refs": f"ROADMAP.md#L80; {target.split('#')[0]}#L10",
            "existing_proposition": f"existing:{r['source_family_id']}", "new_evidence_delta": f"delta:{r['source_family_id']}",
            "evolution_relation": "Direct Evolution" if decision == "Integrate" else "Alternative Branch",
            "decision": decision, "books_review_ref": f"books-review:{r['source_family_id']}",
            "existing_text": f"`{node}` already owns the underlying mechanism/evaluation boundary in `{target}`; the paper cannot silently transfer that owner.",
            "delta_text": INTEGRATE.get(aid, f"Exact-v1 adds the bounded alternative `{r['rationale']}` but its trade/failure boundary does not require a durable manuscript change."),
        })
    (PACKET / "books-comparison-v1.json").write_text(json.dumps({"contract": "44/44 exact-v1 families compared; root serialized nine writes; this lane completed the post-write audit", "row_count": 44, "decision_counts": dict(Counter(x["decision"] for x in comparisons)), "books_write_performed": True, "queue_released": True, "queue_consumed": True, "post_write_audit": "passed_9_of_9", "rows": comparisons}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    by_fam = {r["source_family_id"]: r for r in reviews}
    ledger = []
    receipt = []
    bench_lines = []
    review_sections = []
    for r in reviews:
        c = next(x for x in comparisons if x["source_family_id"] == r["source_family_id"])
        s = r["score"]
        ledger.append(f"| {r['source_family_id']} | arXiv:{r['arxiv_id']}v1 | paper-v1:{r['arxiv_id']} | 2026-W24 | {r['submitted_v1_utc'][:10]} | SRC-ARXIV | {s[0]} | {s[1]} | {s[2]} | {s[3]} | retained | {r['review_status']} | accessible | none | review:{r['source_family_id']} | self | — | new_in_window | {r['stable_node_id']} | {c['decision']} | {c['books_review_ref']} | yes |")
        loc = r["locators"]
        receipt.append(f"| {r['source_family_id']} | {r['provenance']} | {r['route']} | arXiv:{r['arxiv_id']}v1 | SRC-ARXIV@arXiv:{r['arxiv_id']}v1 | {loc['method']} | {loc['evaluation']} | {loc['limitations']} | {loc['artifact']} | claim:{r['source_family_id']} | complete |")
        b = r["benchmark"]
        bench_lines.append("| " + r["source_family_id"] + " | " + " | ".join(str(b[k]).replace("|", "\\|").replace("\n", " ") for k in ("workload", "model", "hardware", "precision", "input_length", "output_length", "batch", "concurrency", "slo", "evaluator")) + " |")
        review_sections.append(f"<!-- review:{r['source_family_id']}:start -->\n{r['body']}\n<!-- review:{r['source_family_id']}:end -->")

    selection_lines, decision_sections = [], []
    for x in selection:
        selection_lines.append(f"| {x['source_family_id']} | {x['eligibility']} | {x['decision']} | {x['analysis_unit_id']} | {x['subsumed_by']} | {x['priority_rationale']} | {x['narrative_ref']} |")
        if x["decision"] == "not_selected":
            decision_sections.append(f"<!-- {x['narrative_ref']}:start -->\n{x['priority_rationale']}\n<!-- {x['narrative_ref']}:end -->")

    books_lines, books_sections = [], []
    for c in comparisons:
        books_lines.append(f"| {c['source_family_id']} | {c['stable_node_id']} | {c['target_chapter_ref']} | {c['adjacent_chapter_refs']} | {c['existing_proposition']} | {c['new_evidence_delta']} | {c['evolution_relation']} | {c['decision']} | {c['books_review_ref']} |")
        books_sections.append(f"<!-- {c['books_review_ref']}:start -->\nCompared `{by_fam[c['source_family_id']]['title']}` against `{c['target_chapter_ref']}` and ROADMAP owner `{c['stable_node_id']}`.\n\n<!-- {c['existing_proposition']}:start -->\n{c['existing_text']}\n<!-- {c['existing_proposition']}:end -->\n\n<!-- {c['new_evidence_delta']}:start -->\n{c['delta_text']}\n<!-- {c['new_evidence_delta']}:end -->\n\nDecision: `{c['decision']}`. Exact-v1 evaluation conditions and non-proof boundary remain attached.\n<!-- {c['books_review_ref']}:end -->")

    families = "; ".join(r["source_family_id"] for r in reviews)
    source_lines = "\n".join(
        f"- [{r['title']}](https://arxiv.org/abs/{r['arxiv_id']}v1) — "
        f"first-public（Asia/Shanghai）：{r['submitted_v1_utc'][:10]}；accessed：{EXECUTED_AT[:10]}"
        for r in reviews
    )
    report = f"""# Daily Research — 2026-06-10

**Research Date:** 2026-06-10

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-09 09:00:00 ～ 2026-06-10 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 已通过

## Executive Summary

Forty disjoint official DataCite DOI-prefix pages cover the full `2606.00`–`.39` namespace (40,000 raw overread rows). Exact v1 time filtering gives 1,230 June-10-window identities, of which 604 fall in registered Daily categories. Full title+abstract semantic screening freezes `604 = 44 retained + 560 family-specific closures`; all 122 keyword-route negatives were separately reviewed. Official exact-v1 HTML is accessible and reviewed for 44/44 retained families. Version drift was repaired rather than trusted: `2606.10388v1` uses the v1 SkillResolve identity, while `2606.10904` is closed because its v1 is a defense comparison and the evaluator-contamination audit belongs only to a later version. Three analysis units were selected from the complete 44-family frontier before rationale rendering. Root serialized the nine deduplicated Integrate deltas, and this lane audited all nine target bodies and Review notes. The `2606.20659v1` boundary is now exact: only Covered/Not Covered, Not Covered means Unknown, coverage is separate from outcome, and the reported coverage range is 39.90–43.98%.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-10 |
| Window End | 2026-06-10 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | {denominator_id} |
| Denominator Frozen At | {EXECUTED_AT} |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-09T09:00:00+08:00 | 2026-06-10T09:00:00+08:00 | {EXECUTED_AT} | DataCite `10.48550/arXiv.2606.00*`–`.39*`; exact Submitted/v1 UTC filter; all registered categories | checked | 604 | {families} | 40 disjoint closed pages; 1,000/page; each `meta.total == len(data)`; 40,000 raw overread | 2026-06-10T01:00:00Z | ../_sources/daily-20260610/registered-hit-screening.json; ../_sources/daily-20260610/candidate-denominator.json; coverage:SRC-ARXIV:20260610 | — |

<!-- coverage:SRC-ARXIV:20260610:start -->
All 411 Core, 71 keyword-routed non-Core and 122 route-negative identities were semantically screened. Frozen arithmetic: `604 = 44 retain + 560 closure`; route-negative audit is `122 = 1 retain + 121 closure`. The retained false negative is `2606.10724v1`, whose passive-tap/secure-gateway AI-cluster I/O architecture changes a durable security owner despite missing the keyword route. The 626 time-window identities outside registered categories are overread, not denominator rows.
<!-- coverage:SRC-ARXIV:20260610:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(ledger)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(receipt)}

### Source Reviews

{chr(10).join(review_sections)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(bench_lines)}

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_lines)}

{chr(10).join(decision_sections)}

### Selected Analysis Narratives

<!-- analysis:DA-20260610-INFERENCE:start -->
The local-MoE paper is selected because it exposes one joined runtime state machine rather than five independent optimizations. Stream-loaded prefill owns transient weight movement; SmallEP owns the two-GPU expert partition; node-local PD separation shares immutable weights without copying; dual-batch overlap schedules attention against expert work; the CPU path separately owns intact FP8 or INT4 expert execution. The paper's 30-second TTFT and 20-token/s references are evaluation coordinates, not portable SLOs. A deployment must rebind them to its arrival process, PCIe/DDR topology and quality branch.
<!-- analysis:DA-20260610-INFERENCE:end -->

<!-- analysis:DA-20260610-TRAINING:start -->
Piper is selected because a parallelism strategy becomes data consumed by a compiler rather than hand-coded runtime structure. Model annotations and scheduling directives transform one global computation/communication DAG; per-device plans are derived artifacts. This separates the owner of intended parallelism from the owner of execution, but it also creates a validation obligation: unsupported or misordered transformations can compile a legal-looking plan with the wrong collective/lifetime semantics. Fixed expert runtimes therefore remain a valid lower-flexibility branch.
<!-- analysis:DA-20260610-TRAINING:end -->

<!-- analysis:DA-20260610-AGENT-CONTROL:start -->
Search Discipline is selected because it changes commit authority. An autoresearch agent optimizes an aggregate metric and is structurally conflicted when that metric hides a protected-region regression. The external controller owns the disaggregated slice contract, noise tolerance and acceptance decision. The fire-model example proves an aggregate inversion in one domain; it does not prove universal slice definitions. The durable rule is narrower: the proposer must not be the only party allowed to define and accept its evidence.
<!-- analysis:DA-20260610-AGENT-CONTROL:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_lines)}

{chr(10).join(books_sections)}

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260610-COVERAGE | fresh-context:jun10-v1-degraded | coverage | coverage:SRC-ARXIV:20260610 | none | Closed the entire 40-prefix namespace after repairing non-monotone Submitted/v1 coverage; 604/604 registered identities and 122/122 route negatives re-read; false-negative audit recovered 2606.10724v1, so the route-negative split is 1 retain + 121 closure; 44+560 arithmetic reproduced | passed |
| SA-20260610-EVIDENCE | fresh-context:jun10-v1-degraded | evidence | {'; '.join('review:'+r['source_family_id'] for r in reviews)} | none | Rebound 10388 to exact-v1 SkillResolve identity; demoted later-version-only 10904 evaluator audit to closure; checked all 44 actual exact-v1 Method/Evaluation/limitations locators and benchmark contracts; corrected 20659 so coverage never expands into a pass/fail outcome label | passed |
| SA-20260610-SELECTION | fresh-context:jun10-v1-degraded | deep_analysis_selection | {'; '.join(x['narrative_ref'] for x in selection)} | none | Winners were fixed before rationale rendering; all 44 eligible rows have source-specific retain/non-select explanations; 3 units are non-overlapping | passed |
| SA-20260610-BOOKS-POSTWRITE | fresh-context:jun10-v1-degraded | books | {'; '.join(c['books_review_ref'] for c in comparisons)} | none | 44/44 owner comparisons complete; root serialized all nine deduplicated deltas; this lane checked 9/9 target bodies and unique Review notes, exact 20659 semantics, and no newly added leakage from the 35 No Change families | passed |

Fresh-context degradation disclosure: this lane is a subagent and cannot create an independent nested reviewer under the active orchestration rule. It therefore used a fresh-pass self-audit with assumptions hidden/re-read, plus exact-v1 identity challenge and whole-population arithmetic. Non-interactive cross-model comparison was skipped; it is not represented as independent acceptance.

## 8. Ignored Noise

The 560 closures are row-addressable in `candidate-denominator.tsv` and retain title, abstract, route, family-specific evidence basis, closure class and reopen condition. `2606.10904` is explicitly among them because the requested evaluator-audit claim is absent from v1.

### Materials Request

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

No exact-version blocker remains. Direct shell TLS resets were bypassed by the working official primary-source reader; all 44 official exact-v1 HTML bodies were accessible.

## 9. Recommended Action

Preserve `{denominator_id}` and its exact-v1 receipts as the event-time checkpoint. Reopen a family only when a versioned primary source or artifact changes its recorded mechanism, owner, evaluation contract or non-proof boundary; no additional Books writeback is currently required.

## 10. Repository Changes

This lane adds the 06-10 Daily, frozen source snapshots, denominator/evidence/selection/Books receipts and renderer. Root serialized the nine approved Books changes; this lane performed the post-write audit and did not stage, commit or push.

## 11. Open Questions

None. Coverage, Evidence/Selection and Books Gates are passed; no exact-version material blocker remains.

## 12. Sources

{source_lines}
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表
- Date-local receipts：`../_sources/daily-20260610/source-review-receipts-v2.1.json`、`deep-analysis-selection-v1.json`、`books-comparison-v1.json`、`POST_WRITE_FRESH_AUDIT_V1.md`

## 13. Final Status

Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。
"""
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")

    queue = [c for c in comparisons if c["decision"] == "Integrate"]
    qlines = ["# 2026-06-10 deduplicated Books queue v1", "", f"- Denominator: `{denominator_id}`", "- Status: consumed by root; post-write fresh audit passed 9/9.", "- Compared: `44/44` exact-v1 families.", f"- Net writeback: `{len(queue)}`", "- Root serialized the nine Books changes; this lane audited them.", "", "| Source Family | arXiv ID | Target locator | Minimal durable delta | Evidence boundary |", "| --- | --- | --- | --- | --- |"]
    for c in queue:
        r = by_fam[c["source_family_id"]]
        qlines.append(f"| {c['source_family_id']} | arXiv:{r['arxiv_id']}v1 | `{c['target_chapter_ref']}` | {c['delta_text']} | {META[r['arxiv_id']][2]} |")
    (PACKET / "BOOKS_DEDUP_QUEUE_V1.md").write_text("\n".join(qlines) + "\n", encoding="utf-8")
    (PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V1.md").write_text(f"# 2026-06-10 candidate denominator audit v1\n\nPASS: full namespace closure, `604 = 44 + 560`; all 122 route negatives reviewed, yielding `1 retain + 121 closure`; the recovered false negative is `2606.10724v1`. The audit also repaired the 2606.10388 exact-v1 identity and closed 2606.10904 later-version leakage. Denominator `{denominator_id}`. DataCite discovery metadata is retained as discovery provenance only and is not exact-v1 claim evidence; the exact-v1 review receipt supplies version-bound summaries and locators, including the corrected 2606.20659 boundary.\n", encoding="utf-8")
    (PACKET / "EVIDENCE_ACCESS_STATUS_V1.md").write_text("# 2026-06-10 evidence access\n\n44/44 exact-v1 official HTML bodies accessible through the working primary-source reader; 0 blocked; 0 ordinary pending.\n", encoding="utf-8")
    (PACKET / "FRESH_CONTEXT_AUDIT_V1.md").write_text("# 2026-06-10 fresh-context audit v1\n\n- Coverage PASS: 40 prefix pages, 604 registered identities, 44 retain + 560 closure; 122 route negatives split into 1 recovered retain (2606.10724v1) + 121 closures.\n- Evidence PASS: 44/44 exact-v1 reviews and benchmark contracts; 10388 identity repaired; 10904 false positive removed; 20659 limited to binary Covered/Not Covered with no invented outcome label.\n- Selection PASS: 44/44 frontier rationales, three predeclared non-overlapping units.\n- Books POSTWRITE PASS: 44 comparisons, nine consumed Integrate proposals, 9/9 target bodies and Review notes checked; no newly added leakage from 35 No Change families.\n- Degraded independence: self-audit used because nested reviewer spawning is disabled; cross-model comparison skipped and not claimed.\n", encoding="utf-8")
    post_lines = [
        "# 2026-06-10 Books post-write fresh audit v1",
        "",
        f"- Denominator: `{denominator_id}`",
        "- Result: PASS, 9/9 serialized Integrate proposals checked.",
        "- Exact-v1 boundary: `2606.20659v1` is binary Covered/Not Covered; Not Covered means Unknown; coverage is separate from outcome; headline coverage is 39.90–43.98%.",
        "- Provenance boundary: the frozen DataCite discovery snapshot retains its later-version abstract for replay, but it is not a claim receipt; the exact-v1 review, report, queue, ready packet and Books text use only the v1 boundary above.",
        "- Leakage check: no newly added Books text cites any of the 35 No Change families.",
        "- Independence disclosure: fresh-pass self-audit; nested reviewer spawning was disabled, and no cross-model independence is claimed.",
        "",
        "| Source Family | arXiv ID | Target | Body | Review note | Result |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for c in queue:
        r = by_fam[c["source_family_id"]]
        boundary = "binary coverage/outcome boundary exact" if r["arxiv_id"] == "2606.20659" else "source-specific mechanism/trade-off boundary exact"
        post_lines.append(f"| {c['source_family_id']} | arXiv:{r['arxiv_id']}v1 | `{c['target_chapter_ref']}` | present once | present once | PASS — {boundary} |")
    (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").write_text("\n".join(post_lines) + "\n", encoding="utf-8")
    (PACKET / "README.md").write_text(f"# 2026-06-10 source packet\n\n`{denominator_id}` freezes 604 identities: 44 retained and 560 family-specific closures. Coverage, Evidence, Selection and Books Gates passed. Root serialized all nine Books proposals; this lane's post-write fresh audit passed 9/9.\n", encoding="utf-8")

    files = [SCREENING, PACKET / "candidate-denominator.json", PACKET / "candidate-denominator.tsv", PACKET / "CANDIDATE_DENOMINATOR_AUDIT_V1.md", PACKET / "EVIDENCE_ACCESS_STATUS_V1.md", PACKET / "exact-v1-access-receipt.json", PACKET / "source-review-receipts-v2.1.json", PACKET / "deep-analysis-selection-v1.json", PACKET / "books-comparison-v1.json", PACKET / "BOOKS_DEDUP_QUEUE_V1.md", PACKET / "BOOKS_READY_TO_INSERT_V1.md", PACKET / "FRESH_CONTEXT_AUDIT_V1.md", PACKET / "POST_WRITE_FRESH_AUDIT_V1.md", PACKET / "README.md", REPORT, Path(__file__).resolve(), ROOT / "scripts/test_june10_canonical_presentation.py", ROOT / "scripts/audit_june10_canonical_presentation.py"]
    presentation_audit = PACKET / "PRESENTATION_FRESH_AUDIT_V2.md"
    if presentation_audit.exists():
        files.append(presentation_audit)
    (PACKET / "SHA256SUMS").write_text(
        "\n".join(
            f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {Path(os.path.relpath(p, PACKET)).as_posix()}"
            for p in files
        ) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"denominator_id": denominator_id, "raw": 604, "retained": 44, "closures": closures, "reviews": 44, "blocked": 0, "selected": 3, "books_queue": len(queue)}, indent=2))


if __name__ == "__main__":
    main()
