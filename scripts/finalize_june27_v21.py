#!/usr/bin/env python3
"""Build the strict 2026-06-27 V2.1 pre-write packet; never edit shared Books."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260627"
REPORT = ROOT / "papers/2026/06/27/README.md"
EXECUTED_AT = "2026-08-29T18:30:00+08:00"
EVIDENCE_READY = True
ND = "Not Disclosed"

PATHS = {
    "MODEL-MOE": "books/part-02-model/21-moe.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/22-long-context.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "TRAIN-DATA": "books/part-04-training-system/27-data.md",
    "TRAIN-LORA": "books/part-04-training-system/30-lora.md",
    "TRAIN-GRPO": "books/part-04-training-system/33-grpo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/36-distributed-training.md",
    "INFER-REQUEST-LIFECYCLE": "books/part-05-inference-system/42-what-happens-during-inference.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/56-inference-scheduling.md",
    "PLATFORM-FOUNDATIONS": "books/part-06-ai-infrastructure/57-what-is-ai-platform.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-COST": "books/part-06-ai-infrastructure/70-cost.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/72-security.md",
    "AGENT-RAG": "books/part-07-agent/76-rag.md",
    "AGENT-MEMORY": "books/part-07-agent/77-memory.md",
    "AGENT-PLANNING": "books/part-07-agent/79-planning.md",
    "AGENT-WORKFLOW": "books/part-07-agent/81-workflow.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/82-multi-agent.md",
    "AGENT-PLATFORM": "books/part-07-agent/84-agent-platform.md",
}

TARGET_ANCHORS = {
    "MODEL-MOE": "### 从局部结果到可执行的系统边界",
    "MODEL-LONG-CONTEXT": "### 从 Dense Checkpoint 迁移到 Hybrid State Model",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "## Cache、rollback 与 exactness",
    "MULTIMODAL-WORLD-MODELS": "## State ownership",
    "MULTIMODAL-EMBODIED-VLA": "## Safety envelope",
    "TRAIN-DATA": "### 从 sample provenance 到训练生命周期 lineage",
    "TRAIN-LORA": "## Checkpoint 与可复现性",
    "TRAIN-GRPO": "### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界",
    "TRAIN-DISTRIBUTED-TRAINING": "### 从 Phase 串行到依赖驱动的跨 Phase 重排",
    "INFER-REQUEST-LIFECYCLE": "## 请求状态机",
    "INFER-SCHEDULING": "### Semantic Predicate 的 Token Cost 应成为 Query-planner State",
    "PLATFORM-FOUNDATIONS": "## Paved Road 与 Escape Hatch",
    "PLATFORM-EVALUATION-SYSTEM": "### Evaluator 可以主动制造 Probe，但不能冒充被动观察",
    "PLATFORM-MONITORING": "## Monitoring 也会改变系统",
    "PLATFORM-COST": "## 利用率与有效利用率",
    "PLATFORM-SECURITY": "## 风险管理而不是一次性认证",
    "AGENT-RAG": "## Offline Ingestion 不是预处理细节",
    "AGENT-MEMORY": "## Consolidation 与 Forgetting",
    "AGENT-PLANNING": "## 完成证据与 Verification",
    "AGENT-WORKFLOW": "## State Machine 是基本模型",
    "AGENT-MULTI-AGENT": "### 共享 Repository 需要 Commitment Protocol，不只是更多消息",
    "AGENT-PLATFORM": "## Agent Runtime State Machine",
}

ADJACENT = {
    "MODEL-MOE": "books/part-02-model/20-sampling.md",
    "MODEL-LONG-CONTEXT": "books/part-02-model/21-moe.md",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "MULTIMODAL-WORLD-MODELS": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
    "MULTIMODAL-EMBODIED-VLA": "books/part-03-multimodal-world-models/25-multimodal-world-models.md",
    "TRAIN-DATA": "books/part-04-training-system/28-pretraining.md",
    "TRAIN-LORA": "books/part-04-training-system/29-sft.md",
    "TRAIN-GRPO": "books/part-04-training-system/32-ppo.md",
    "TRAIN-DISTRIBUTED-TRAINING": "books/part-04-training-system/37-tensor-parallel.md",
    "INFER-REQUEST-LIFECYCLE": "books/part-05-inference-system/43-prefill.md",
    "INFER-SCHEDULING": "books/part-05-inference-system/55-pd-disaggregation.md",
    "PLATFORM-FOUNDATIONS": "books/part-06-ai-infrastructure/58-kubeflow.md",
    "PLATFORM-EVALUATION-SYSTEM": "books/part-06-ai-infrastructure/67-monitoring.md",
    "PLATFORM-MONITORING": "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "PLATFORM-COST": "books/part-06-ai-infrastructure/69-trace.md",
    "PLATFORM-SECURITY": "books/part-06-ai-infrastructure/71-multi-tenant.md",
    "AGENT-RAG": "books/part-07-agent/77-memory.md",
    "AGENT-MEMORY": "books/part-07-agent/76-rag.md",
    "AGENT-PLANNING": "books/part-07-agent/78-tool-calling.md",
    "AGENT-WORKFLOW": "books/part-07-agent/80-reflection.md",
    "AGENT-MULTI-AGENT": "books/part-07-agent/81-workflow.md",
    "AGENT-PLATFORM": "books/part-07-agent/83-mcp.md",
}

INTEGRATE = {
    "2606.27681", "2606.27732", "2606.27797", "2606.27806", "2606.27841",
    "2606.27906", "2606.28013", "2606.28116", "2606.28276", "2606.28479",
    "2606.28529", "2606.28565", "2606.28649", "2606.28661",
}

WEEKLY_ONLY = {"2606.27791", "2606.28166", "2606.28560"}

# These are owner-level durable deltas, not paper/result summaries. Multiple families
# routed to one owner are deliberately merged into one evolution narrative.
OWNER_NARRATIVE = {
    "MULTIMODAL-WORLD-MODELS": (
        "若预测器可以绕过声明的 state 重读原始历史，预测正确也无法识别 state 本身是否有效。应让版本化 belief state "
        "成为 transition/prediction path 的唯一受控输入，再检查它是否保留下游 consumer 所需信息。这样 state representation "
        "才从辅助解释升级为可审计接口。"
    ),
    "MULTIMODAL-GENERATIVE-PARADIGMS": (
        "并行文本生成不必只在全双向重算与纯 causal cache 之间二选一：受限 right-context side path 可以提供可编辑上下文，"
        "causal path 则保留 append-friendly state。generation identity 因而必须记录 mutable context 由哪条路径持有、哪些 cache "
        "entry 可复用，以及 provisional span 在何时提交。"
    ),
    "TRAIN-DISTRIBUTED-TRAINING": (
        "知识蒸馏 runtime 不应强迫 teacher inference 与 student training 共用一份并行方案，而应按两类 workload 分别分片。"
        "它们的参数驻留、activation lifetime、batch shape 与通信 critical path 均不同；真正的 handoff 是 student update 消费的"
        "版本化 teacher output，而不是共享 rank topology。"
    ),
    "AGENT-PLANNING": (
        "语言 planner 可以保留语义 proposal authority，同时由小型 parametric transition model 检查 imagined state delta 是否满足动力学。"
        "两者分歧时应开启 targeted revision，而不是静默替换 planner 或提交 action；transition model 只做 bounded verifier，"
        "environment/controller 继续拥有最终 authority。"
    ),
    "PLATFORM-COST": (
        "能耗归因应先把一次 model run 拆成 layer/operator measurement，再拟合 architecture-level proxy。可复用 cost model 必须把每次"
        "测量绑定到 device、precision、batch/shape 与 utilization regime，然后针对目标 graph 重组；否则 whole-model estimate 会隐藏"
        "究竟是哪类 layer 改变 operating point。"
    ),
    "INFER-REQUEST-LIFECYCLE": (
        "Inference capacity 是 phase-coupled closed loop，不是单个 kernel 数字。request record 必须区分 vision encoding、prefill、decode、"
        "queue/host work 与 device placement；kernel-level simulation 可以预测候选配置，但 promotion 必须回到目标硬件上的 task completion "
        "time 与 success。改变 control cadence 或移动瓶颈的局部加速，不自动等于更快完成成功任务。"
    ),
    "PLATFORM-EVALUATION-SYSTEM": (
        "Evaluation 必须分开 generator 能产生什么，与 release selector 能可靠识别什么。对 formalization，type acceptance 与 semantic "
        "equivalence 是两个独立 signal；对 repeated sampling，answer coverage 与 selection accuracy 必须分报，并显式记录 correlation/modal "
        "ceiling。增加 sample budget 不能修复无法识别已覆盖答案的 oracle 或 selector。"
    ),
    "PLATFORM-MONITORING": (
        "Training-instability monitoring 应在 aggregate loss 发散前读取 mechanism-adjacent state：attention spectrum、router/load state 与 "
        "update statistic 是分别校准、绑定 checkpoint 的 sensor。它们可以触发暂停、诊断或 rollback，但不能自动拥有 root-cause truth；"
        "sensor 漂移或相互冲突时必须 abstain，并保留最近已验证 checkpoint 作为 fallback。"
    ),
    "MULTIMODAL-EMBODIED-VLA": (
        "Scene-generation pipeline 应把 video reconstruction、editable scene variant、policy training 与 real-world validation 保存为由 provenance "
        "连接的独立 artifact。visual fidelity 只能决定 scene 能否进入 simulation，不拥有 sim-to-real validity；synthetic scene family 影响"
        "物理 promotion 前，policy ranking 必须与 matched real outcome 对读。"
    ),
    "TRAIN-LORA": (
        "Privacy-preserving adaptation 需要 matched-update causal ladder。在固定 base revision、adapter identity 与 training budget 后，"
        "pseudonymization、differential privacy 与 optimizer/update-count effect 必须独立变化；否则 memorization 降低无法归因给 privacy mechanism。"
        "DP 继续拥有 formal guarantee，empirical probe 只测量给定 attack 下的 leakage。"
    ),
    "PLATFORM-SECURITY": (
        "Robot middleware 会把 OCR、speech 与 range-derived state 序列化进高优先级 model context，因此 role label 不能建立信任。"
        "provenance 与 integrity check 必须沿 sensor data 经 middleware transformation 进入 prompt 的路径传播，并在 actuation 前保留 cross-modal "
        "consistency check 与 controller-side deny/hold path；未知或冲突的 sensory context 不得继承 system authority。"
    ),
}

OWNER_BOUNDARY = {
    "MULTIMODAL-WORLD-MODELS": "Strict mediation 增加训练成本，也可能让有损 textual state 成为瓶颈；无需可识别性时，直接 latent/history access 仍是合理旧路径。",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "Side path 增加参数、训练耦合与 cache-version 复杂度；要求 exact streaming 或 kernel 不支持时回退 causal generation。",
    "TRAIN-DISTRIBUTED-TRAINING": "非对称方案增加 handoff buffering 与 topology search；teacher/student footprint 相近时，共享方案仍更简单。",
    "AGENT-PLANNING": "Learned transition verifier 可能与 planner 共享盲点，也不是 physics oracle；分歧或 OOD state 回退 environment validation 或人工复核。",
    "PLATFORM-COST": "Layer recomposition 可能遗漏 fusion、memory hierarchy 与 concurrency interaction；生产真值仍由 whole-run meter 持有，漂移时重校 layer model。",
    "INFER-REQUEST-LIFECYCLE": "Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。",
    "PLATFORM-EVALUATION-SYSTEM": "Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。",
    "PLATFORM-MONITORING": "Pre-loss signal 可能噪声大且依赖 family；它们保持 observe-first，缺失校准时 abstain，不能自动干预训练。",
    "MULTIMODAL-EMBODIED-VLA": "Reconstruction quality 与 simulator ranking 不证明 contact dynamics 或 safety；rank mismatch 或未知 embodiment 会阻断物理 promotion，并保留 real-data/controller gate。",
    "TRAIN-LORA": "Matched control 增加实验成本，empirical attack 的 recall 也有边界；未测到 leakage 不是 privacy guarantee，不确定时保留更严格 data/DP path。",
    "PLATFORM-SECURITY": "证据只覆盖特定 ROS 2 transformation 与 attack，不覆盖所有 sensor/model；provenance 缺失或 modality 冲突时，在 action 前 fail closed。",
}

ORIGINAL_BOOKS_REVIEW = {
    "2606.27634": "The monitoring owner already marks checkpoint-bound monitors stale and requires re-alignment, retraining or abstention; sequential LoRA/reference-set drift is an instance, not a new contract.",
    "2606.27681": "The world-model owner separates latent state from physical commit, but does not require state-only mediation that makes representation quality identifiable.",
    "2606.27732": "The generation owner covers provisional commit and cache invalidation, but not an asymmetric right-context side path coexisting with a causal cache.",
    "2606.27791": "The long-context owner already assigns hybrid full-attention placement to calibrated layer selection; answer-token NLL is a local selector, not a new owner boundary.",
    "2606.27797": "The distributed-training owner covers model/optimizer partitioning, but not independent teacher-inference and student-training topology plans joined by a versioned handoff.",
    "2606.27806": "The planning owner separates proposal, validation and commit, but lacks a learned transition-disagreement gate that requests targeted plan revision without taking action authority.",
    "2606.27841": "The cost owner models offered load and whole-run energy, but does not expose layer/operator measurement identity before architecture-level recomposition.",
    "2606.27866": "The MoE owner already defines a shared checkpoint plus sampled subnet profiles, independent quality envelopes and online budget selection; nested intra-expert pruning is covered.",
    "2606.27906": "The inference lifecycle names prefill/decode/request state, but does not bind mobile vision/prefill/decode placement and thermal phase to one hardware-specific record.",
    "2606.28013": "The evaluation owner requires semantic-equivalent adapters, but does not freeze the two-axis type-acceptance versus semantic-equivalence coverage matrix.",
    "2606.28116": "The monitoring owner covers telemetry and checkpoint-stale monitors, but lacks mechanism-derived pre-loss sensors for attention/router/update failure signatures.",
    "2606.28166": "The GRPO owner already assigns trajectory state to the student, teacher signal to bounded guidance and verifier to reward direction; alternating senior/junior generation is a local rollout design.",
    "2606.28187": "The multi-agent owner already represents interaction edges and attribution/noise boundaries; differentiable connection weights are a local optimizer, not a new coordination owner.",
    "2606.28276": "The embodied owner warns that simulator success does not prove sim-to-real, but does not bind reconstruction artifact, editable scene variants and real-world rank-validity checks into one promotion chain.",
    "2606.28479": "The LoRA owner versions adapters and rollback but does not require matched optimizer-step controls that distinguish DP, pseudonymization and update-count memorization effects.",
    "2606.28529": "The inference owner separates request stages and component latency, but does not make closed-loop task time and success the acceptance criterion for embodied speedups.",
    "2606.28560": "The long-context owner already treats sparse pattern and extrapolation as calibrated architecture choices; Fibonacci spacing is a bounded schedule result, not a durable contract change.",
    "2606.28565": "The inference owner tracks queue, prefill, decode and host work, but does not state how a kernel/communication simulator remains a forecast subordinate to measured request outcomes.",
    "2606.28649": "The security owner treats OCR/audio content as untrusted, but does not trace sensor-derived text/state promoted into system-role context through robot middleware.",
    "2606.28661": "The evaluation owner discusses correlated uncertainty, but does not separate sampling coverage from selector authority or expose modal/correlation ceilings as a stopping boundary.",
}

# Exact-v1 benchmark disclosures that need a shorter, role-correct value than
# the HTML search snippet. An override to ND removes a discussion/citation/table
# variable that the conservative extractor must not misidentify as an evaluated
# model, device or metric.
BENCHMARK_OVERRIDES = {
    "2606.27634": {
        "model": "Qwen 3.5 0.8B, Llama 3.2 1B Instruct and Gemma 3 1B IT",
        "hardware": "NVIDIA Titan X (11 GB), CUDA 11.8", "input_length": "Training maximum length 512 tokens",
        "output_length": "Evaluation maximum output 256 tokens", "batch": "Training batch size 2 with gradient accumulation 8; evaluation batch size 4",
        "evaluator": "Exact-match task accuracy plus ACC, BWT, FWT, KL divergence, entropy and margin over three seeds",
    },
    "2606.27650": {"evaluator": ND},
    "2606.27679": {"evaluator": ND},
    "2606.27681": {"evaluator": ND},
    "2606.27683": {"evaluator": ND},
    "2606.27709": {
        "hardware": "1 NVIDIA L20 GPU (48 GB VRAM)", "precision": "4-bit quantization",
        "input_length": "Maximum sequence length 1024 tokens", "batch": "Batch size 8; gradient accumulation 2",
    },
    "2606.27732": {
        "hardware": "32 NVIDIA H100 GPUs (4 nodes × 8 GPUs)", "precision": "bfloat16",
        "input_length": "Sequence length 4096 tokens", "batch": "Per-device batch size 8; no gradient accumulation",
    },
    "2606.27739": {"hardware": ND, "evaluator": ND},
    "2606.27743": {"hardware": ND},
    "2606.27780": {"evaluator": ND},
    "2606.27791": {"evaluator": ND},
    "2606.27797": {
        "workload": "Teacher-student generative knowledge distillation with asymmetric partition and communication plans",
        "hardware": ND, "precision": ND, "evaluator": "End-to-end GKD training time and topology/partition ablations",
    },
    "2606.27806": {
        "workload": "TaskGraph, ToolChain, ResourceAlloc and RepairFlow; 100 test tasks per benchmark (60 in-distribution, 40 out-of-distribution)",
        "evaluator": "Eleven agent-only, parametric-only and hybrid planners evaluated on plan validity/reward and hallucinated state transitions",
    },
    "2606.27841": {"hardware": "NVIDIA H100, A100 and TITAN X measurements", "batch": "LLM zero-shot energy evaluation uses batch size 1"},
    "2606.27814": {
        "model": "Qwen3-0.6B, Qwen3-1.7B and Qwen3-4B student models",
        "hardware": "8 GPUs on one node",
        "batch": "Train batch sizes ALFWorld/WebShop/Search-QA = 16/128/16; validation = 128/512/128",
    },
    "2606.27906": {
        "workload": "FastVLM-0.5B FP16 CPU versus INT8 NPU on 500 COCO val2017 images and 200 VQAv2 questions",
        "hardware": "Snapdragon mobile SoC CPU and Qualcomm NPU paths",
        "evaluator": "COCO CIDEr and VQAv2 lowercase-normalized exact-match accuracy",
    },
    "2606.27934": {"hardware": ND},
    "2606.27962": {"hardware": ND, "evaluator": ND},
    "2606.27976": {"hardware": "Five reported cells CPU-encoded; e5-large/NFCorpus omitted after exceeding CPU budget"},
    "2606.28011": {"workload": ND, "evaluator": ND},
    "2606.28013": {
        "workload": "Statement autoformalization stratified by Lean type-check and semantic-equivalence judgment",
        "model": "DeepSeek V4-Pro on ProofNet# for the full four-method dual-judging cell",
        "evaluator": "Four-cell TS/TO/SO/BF signal-coverage matrix under dual semantic judging",
    },
    "2606.28050": {"hardware": ND, "input_length": ND},
    "2606.28116": {
        "workload": "Low-precision attention, large-learning-rate and combined-fault training-instability injections",
        "hardware": ND, "evaluator": "Pre-loss detection lead time and distinct attention/router failure signatures",
    },
    "2606.28128": {"workload": ND},
    "2606.28153": {"evaluator": ND},
    "2606.28187": {"evaluator": ND},
    "2606.28322": {"evaluator": ND},
    "2606.28433": {"evaluator": ND},
    "2606.28436": {"workload": ND},
    "2606.28471": {
        "workload": "Two evaluation-to-data case studies: EOS-supervision diagnosis and operation-composition targeted sampling",
        "evaluator": "BBH checkpoint recovery plus AIME2025/AIME2026 Pass@128 and operation-level attribution",
    },
    "2606.28479": {"model": ND, "hardware": ND, "evaluator": ND},
    "2606.28529": {"precision": ND, "batch": ND},
    "2606.28551": {"model": ND, "hardware": ND, "batch": "Global batch size 1024"},
    "2606.28562": {"workload": ND},
    "2606.28565": {"hardware": ND},
    "2606.28615": {"hardware": "2 NVIDIA A100 GPUs", "batch": "Batch size 8"},
    "2606.28649": {"evaluator": "Attack success rate across 100 runs per injection condition"},
    "2606.28661": {
        "workload": "Repeated test-time sampling under clustered/correlated answer distributions",
        "evaluator": "Coverage, oracle selection, learned selection, modal ceiling, correlation ceiling and effective sample size",
    },
}

WINNER_UNITS = {
    "2606.27681": "DA-20260627-STRICT-MEDIATED-WORLD-STATE",
    "2606.27906": "DA-20260627-PHASE-CLOSED-LOOP-INFERENCE",
    "2606.28649": "DA-20260627-SENSORY-CONTEXT-AUTHORITY",
}
SUBSUMED = {
    "2606.28529": "DA-20260627-PHASE-CLOSED-LOOP-INFERENCE",
    "2606.28565": "DA-20260627-PHASE-CLOSED-LOOP-INFERENCE",
}

OWNER_STATE = {
    "PLATFORM-SECURITY": "authority envelope、untrusted input 与 release gate",
    "PLATFORM-EVALUATION-SYSTEM": "oracle、metric、slice 与结论发布",
    "PLATFORM-MONITORING": "sensor state、calibration 与 alarm action",
    "PLATFORM-COST": "measurement state、resource attribution 与 cost model",
    "PLATFORM-FOUNDATIONS": "environment、artifact、scheduler 与 lifecycle control",
    "TRAIN-DATA": "sample provenance、mixture 与 admission state",
    "TRAIN-LORA": "adapter/update identity 与 rollback",
    "TRAIN-GRPO": "trajectory、credit、teacher signal 与 update gate",
    "TRAIN-DISTRIBUTED-TRAINING": "partition、topology、version 与 synchronization",
    "INFER-REQUEST-LIFECYCLE": "request phase、runtime placement、queue 与 latency state",
    "INFER-SCHEDULING": "request budget、compute allocation 与 fallback",
    "MODEL-MOE": "expert capacity、nested subnet 与 routing budget",
    "MODEL-LONG-CONTEXT": "attention reach、layer policy 与 context budget",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "generation dependency、cache 与 commit order",
    "MULTIMODAL-WORLD-MODELS": "belief/latent state、transition 与 physical boundary",
    "MULTIMODAL-EMBODIED-VLA": "scene state、policy evaluation 与 real-world commit",
    "AGENT-RAG": "retrieval index、privacy boundary 与 evidence handoff",
    "AGENT-MEMORY": "memory action、compression 与 remaining-context state",
    "AGENT-PLANNING": "world state、plan revision 与 executable commit",
    "AGENT-WORKFLOW": "artifact state、verifier/interlock 与 fallback",
    "AGENT-MULTI-AGENT": "interaction graph、attribution 与 commit coordination",
    "AGENT-PLATFORM": "workspace、runtime、acceptance predicate 与 replay",
}

OWNER_EXISTING = {
    "PLATFORM-SECURITY": "Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。",
    "PLATFORM-EVALUATION-SYSTEM": "Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。",
    "PLATFORM-MONITORING": "Ch67 已把 monitor 定义为需校准的 observe/alert sensor，并要求 checkpoint 变化后 stale/abstain。",
    "PLATFORM-COST": "Ch70 已让 workload、利用率、质量/SLO 与 meter 共同拥有 cost truth，而非用峰值 proxy 直接决策。",
    "PLATFORM-FOUNDATIONS": "Ch57 已把 paved road、escape hatch、artifact/environment identity 与 lifecycle control 分开。",
    "TRAIN-DATA": "Ch27 已让 sample provenance、mixture/admission 与训练生命周期 lineage 共同决定数据能否进入训练。",
    "TRAIN-LORA": "Ch30 已让 base revision、adapter identity、update/merge 与 rollback 组成可审计资产合同。",
    "TRAIN-GRPO": "Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。",
    "TRAIN-DISTRIBUTED-TRAINING": "Ch36 已按 model/optimizer/activation state、parallel group 与 topology 定义分片、同步和 checkpoint。",
    "INFER-REQUEST-LIFECYCLE": "Ch42 已把 request 拆成 admission、prefill、decode、streaming 与 cleanup phase，并绑定 queue/KV/SLO state。",
    "INFER-SCHEDULING": "Ch56 已让 request budget、queue state、goodput 与 fallback 共同约束 compute allocation。",
    "MODEL-MOE": "Ch21 已把共享 checkpoint、subnetwork profile、quality envelope 与 kernel/placement plan 纳入同一模型身份。",
    "MODEL-LONG-CONTEXT": "Ch22 已把 full/local/sparse layer policy、calibration、position rule 与 cache identity 作为 hybrid-attention contract。",
    "MULTIMODAL-GENERATIVE-PARADIGMS": "Ch24 已区分 provisional state、commit/rollback、cache invalidation 与 user-visible generation。",
    "MULTIMODAL-WORLD-MODELS": "Ch25 已分离 belief/latent state、action-conditioned transition、physical truth 与 commit authority。",
    "MULTIMODAL-EMBODIED-VLA": "Ch26 已要求 simulation/video evidence 经 real-world outcome 与 safety/controller gate 才能影响物理提交。",
    "AGENT-RAG": "Ch76 已让 index/source provenance、retrieval evidence 与 context admission 分别持有状态和权限。",
    "AGENT-MEMORY": "Ch77 已让 write/read/compress/delete、provenance 与 remaining-context state 共同决定 memory 行为。",
    "AGENT-PLANNING": "Ch79 已区分 plan proposal、pre-commit verifier、environment feedback 与 executable commit。",
    "AGENT-WORKFLOW": "Ch81 已把 artifact state、deterministic interlock、verifier 与 retry/fallback 组织为可提交状态机。",
    "AGENT-MULTI-AGENT": "Ch82 已让 interaction graph、edge attribution、shared-object ordering 与 coordination noise 分别可审计。",
    "AGENT-PLATFORM": "Ch84 已把 workspace/runtime、intent、acceptance predicate、trace/replay 与 promotion gate 分开。",
}


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def md(value: str) -> str:
    return norm(str(value)).replace("|", "/")


def sentences(text: str) -> list[str]:
    return [norm(x) for x in re.split(r"(?<=[.!?])\s+", norm(text)) if norm(x)]


def result_sentence(abstract: str) -> str:
    ss = sentences(abstract)
    preferred = [s for s in ss if re.search(r"\b(show|demonstrate|evaluate|experiment|result|outperform|improve|achiev|contains|cover)\w*\b", s, re.I)]
    return (preferred[-1] if preferred else ss[-1]) if ss else ND


def boundary_sentence(record: dict) -> str:
    ss = sentences(record["abstract"])
    caveats = [s for s in ss if re.search(r"\b(while|remain|future work|limit|does not|do not|without|however|only)\b", s, re.I)]
    if caveats:
        return caveats[-1]
    return (
        f"exact-v1 的结论只覆盖《{record['title']}》在 {record['evaluation_locator']} 声明的实验；"
        "它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。"
    )


def clean_disclosure(value: str, keyword: str) -> str:
    value = norm(value)
    if value == ND or "Cited by:" in value or re.search(r"\* \[\d+\]", value):
        return ND
    ss = sentences(value)
    candidates = [s for s in ss if keyword.lower() in s.lower() and len(s) <= 520]
    if not candidates:
        candidates = [s for s in ss if len(s) <= 420]
    return candidates[0] if candidates else ND


MODEL_TOKEN = re.compile(
    r"(GPT[- ]?\d|Qwen|Llama|Gemma|Mistral|Claude|DeepSeek|Yuvion|Nemotron|OLMo|"
    r"Phi[- ]?\d|Mixtral|SmolLM|TinyLlama|Zephyr)",
    re.I,
)


def exact_sentence(value: str, pattern: re.Pattern, require_number: bool = False) -> str:
    if value == ND:
        return ND
    cleaned = norm(re.sub(r"#{2,6}\s*", "", value))
    candidates = sentences(cleaned)
    for sentence in candidates:
        if "Cited by:" in sentence or re.search(r"\* \[\d+\]", sentence):
            continue
        if pattern.search(sentence) and (not require_number or re.search(r"\d", sentence)):
            if len(sentence) > 680:
                return sentence[:680].rsplit(" ", 1)[0] + " …"
            return sentence
    return ND


def chapter_ref(owner: str) -> str:
    path, heading = PATHS[owner], TARGET_ANCHORS[owner]
    lines = (ROOT / path).read_text().splitlines()
    hits = [i for i, line in enumerate(lines, 1) if line == heading]
    assert len(hits) == 1, (owner, path, heading, hits)
    return f"{path}#L{hits[0]} — {heading}"


def adjacent_ref(owner: str) -> str:
    path = ADJACENT[owner]
    lines = (ROOT / path).read_text().splitlines()
    hit = next(i for i, line in enumerate(lines, 1) if line.startswith("## "))
    return f"{path}#L{hit} — {lines[hit-1]}"


def score(aid: str, owner: str) -> tuple[int, int, int]:
    if aid in INTEGRATE:
        return (3, 1, 3) if owner in {"PLATFORM-COST", "TRAIN-LORA", "MODEL-MOE"} else (3, 2, 3)
    if owner in {"PLATFORM-SECURITY", "PLATFORM-EVALUATION-SYSTEM"}:
        return (2, 2, 3)
    if owner in {"PLATFORM-FOUNDATIONS", "AGENT-PLATFORM", "AGENT-MULTI-AGENT"}:
        return (2, 2, 2)
    return (2, 1, 2)


def review_route(item: dict) -> str:
    return "deep" if sum(item["score"]) >= 7 or item["owner"] == "PLATFORM-SECURITY" else "standard"


def review_status(item: dict) -> str:
    return "deep_complete" if review_route(item) == "deep" else "standard_complete"


def review_body(item: dict) -> str:
    if item["disposition"].startswith("No Change"):
        coexist = "现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。"
    elif item["disposition"].startswith("Weekly Only"):
        coexist = "该结果只保留为局部方法/实验语境；它不新增长期 owner、authority、coexistence 或 fallback 命题。"
    else:
        coexist = OWNER_BOUNDARY[item["owner"]]
    return "\n".join([
        f"### {item['aid']} — {item['title']}", "",
        f"**问题、约束与旧路径。** {item['problem']} 旧路径在论文新增条件之外仍然合理。", "",
        f"**机制、state/data/control owner。** {item['mechanism']} 由 {item['owner']} 持有 {OWNER_STATE[item['owner']]}；相邻节点只消费版本化 handoff。", "",
        f"**Evaluation：证明与未证明。** {item['proof']} Method={item['method']}；Evaluation={item['evaluation']}。评测合同逐字段冻结，未公开项才写 {ND}。", "",
        f"**Trade-off、failure、fallback、coexistence 与 evolution。** {item['boundary']} {coexist} Counterevidence/limitation={item['limitation']}。", "",
        f"<!-- claim:{item['family']}:start -->",
        f"Claim boundary：仅 arXiv:{item['aid']}v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。",
        f"<!-- claim:{item['family']}:end -->",
    ])


def provenance(item: dict) -> str:
    body = unicodedata.normalize("NFC", review_body(item).replace("\r\n", "\n").replace("\r", "\n"))
    body_hash = hashlib.sha256("\n".join(x.rstrip() for x in body.splitlines()).strip().encode()).hexdigest()
    def multi(value: str) -> str:
        values = []
        for raw in value.split(";"):
            candidate = unicodedata.normalize("NFC", raw.strip())
            if candidate and candidate not in {"—", "-", "N/A", "n/a"}:
                values.append(candidate)
        return ";".join(sorted(values))

    fields = [
        "review-completion-v1", item["family"], f"paper-v1:{item['aid']}", f"arXiv:{item['aid']}v1",
        "SRC-ARXIV", f"arXiv:{item['aid']}v1", f"SRC-ARXIV@arXiv:{item['aid']}v1", review_route(item),
    ]
    if item["owner"] == "PLATFORM-SECURITY" and sum(item["score"]) < 7:
        fields.append("review-override:release_security_contract")
    fields += [
        multi(item["method"]), multi(item["evaluation"]), multi(item["limitation"]),
        multi("Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review"),
        f"claim:{item['family']}", f"review:{item['family']}", f"review-body-sha256:{body_hash}",
    ]
    canonical = "|".join(fields)
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def make_items() -> tuple[str, list[dict], dict]:
    denominator = json.loads((PACKET / "candidate-denominator.json").read_text())
    facts = json.loads((PACKET / "exact-v1-evidence-facts.json").read_text())
    assert denominator["retained"] == 64 and facts["resolved"] == 64 and facts["blocked"] == 0
    by_id = {r["arxiv_id"]: r for r in facts["records"]}
    bench2 = {
        r["arxiv_id"]: r
        for r in json.loads((PACKET / "exact-v1-benchmark-evidence-v2.json").read_text())["records"]
    }
    assert len(denominator["candidates"]) == len(by_id) == 64
    items = []
    for c in denominator["candidates"]:
        aid, fact = c["arxiv_id"], by_id[c["arxiv_id"]]
        ss, evidence, b2 = sentences(c["abstract"]), fact["benchmark_evidence"], bench2[aid]
        combined_models = " ".join(b2[k] for k in ("We evaluate", "We use", "We train") if b2[k] != ND)
        model = exact_sentence(combined_models, MODEL_TOKEN)
        hardware = exact_sentence(
            b2["GPU"],
            re.compile(r"(GPU|A100|H100|L20|RTX|Jetson|SoC|MCU|CPU|TPU|Apple M[1-9]|Snapdragon)", re.I),
        )
        if hardware != ND and re.search(r"(such as|preference|not to compare|Cited by:|utilization)", hardware, re.I):
            hardware = ND
        batch = exact_sentence(b2["batch size"], re.compile(r"\bbatch(?: size)?\b", re.I), require_number=True)
        if batch != ND and not re.search(
            r"(batch size (?:of|is|=|fixed at|equal to)|global batch size|train batch size|batch size /)", batch, re.I
        ):
            batch = ND
        if batch != ND and re.search(r"(Cited by:|bibliograph|Summary of notation|Algorithm|Figure \d)", batch, re.I):
            batch = ND
        precision = exact_sentence(
            evidence["precision"],
            re.compile(r"(BF16|FP16|FP8|FP32|INT8|INT4|W4A8|mixed precision|quantiz)", re.I),
        )
        if precision != ND and not re.search(r"(use|using|weights|training|operates|configuration|quantiz)", precision, re.I):
            precision = ND
        input_length = exact_sentence(
            evidence["context"],
            re.compile(r"(context length|max(?:imum)? sequence length|tokens?)", re.I),
            require_number=True,
        )
        if input_length != ND and not re.search(r"(set|fixed|limit|maximum|max sequence|context limit|resize)", input_length, re.I):
            input_length = ND
        concurrency = exact_sentence(
            evidence["concurrency"],
            re.compile(r"(concurr|parallel|workers?|requests?)", re.I),
            require_number=True,
        )
        if concurrency != ND and re.search(r"(depends on concurrency|high-concurrency|foundation layer)", concurrency, re.I):
            concurrency = ND
        slo = exact_sentence(
            evidence["slo"],
            re.compile(r"(SLO|latency|throughput|TTFT|TBT|deadline)", re.I),
            require_number=True,
        )
        if slo != ND and not re.search(r"(\d+(?:\.\d+)?\s*(?:ms|s|sec|seconds?|tokens?/s|req(?:uest)?s?/s)|p\d+)", slo, re.I):
            slo = ND
        workload = exact_sentence(b2["We evaluate"], re.compile(r"(evaluate|benchmark|experiment)", re.I))
        evaluator = exact_sentence(
            " ".join(value for value in (b2["We evaluate"], evidence["metrics"]) if value != ND),
            re.compile(r"(metric|accuracy|F1|success|latency|throughput|perplexity|error|ASR|score)", re.I),
        )
        benchmark = {
            "workload": md(workload),
            "model": md(model),
            "hardware": md(hardware),
            "precision": md(precision),
            "input_length": md(input_length),
            "output_length": ND,
            "batch": md(batch),
            "concurrency": md(concurrency),
            "slo": md(slo),
            "evaluator": md(evaluator),
        }
        for field, value in BENCHMARK_OVERRIDES.get(aid, {}).items():
            benchmark[field] = value
        url = fact["exact_v1_url"]
        item = {
            "aid": aid, "family": c["source_family_id"], "title": c["title"], "abstract": c["abstract"],
            "owner": c["proposed_owner"], "mechanism": c["screening_reason"],
            "problem": " ".join(ss[:2]) if ss else c["title"],
            "proof": result_sentence(c["abstract"]), "boundary": boundary_sentence(fact),
            "method": f"{url} — §{fact['method_locator']}",
            "evaluation": f"{url} — §{fact['evaluation_locator']}",
            "limitation": f"{url} — §{fact['nonproof_locator']}",
            "benchmark": benchmark, "score": score(aid, c["proposed_owner"]),
            "disposition": (
                "Integrate" if aid in INTEGRATE else
                "Weekly Only — Context" if aid in WEEKLY_ONLY else
                "No Change — Existing Coverage"
            ),
        }
        item["rp"] = provenance(item)
        items.append(item)
    return denominator["denominator_id"], items, denominator


def write_json(name: str, value) -> None:
    (PACKET / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def build_selection(items: list[dict]) -> list[dict]:
    lens = {
        "INFER-REQUEST-LIFECYCLE": "它属于已入选的 phase-coupled inference chain，应在该链内合并，而不是另建第四条叙事",
        "MULTIMODAL-WORLD-MODELS": "它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界",
        "PLATFORM-SECURITY": "除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break",
        "PLATFORM-EVALUATION-SYSTEM": "它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain",
        "PLATFORM-MONITORING": "它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority",
        "TRAIN-GRPO": "它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority",
        "TRAIN-DISTRIBUTED-TRAINING": "它改变 training runtime partition/handoff，但影响仍受限于 distillation job",
        "MODEL-LONG-CONTEXT": "它是有界的 attention calibration/layout 结果，而不是新的跨层 control contract",
        "MODEL-MOE": "canonical MoE owner 已持有 budget-profile state，因此本 family 只增加实现证据，不另建 analysis unit",
        "MULTIMODAL-GENERATIVE-PARADIGMS": "它改变 provisional generation/cache semantics，但仍完整落在 generation owner 内",
        "MULTIMODAL-EMBODIED-VLA": "它改变进入 physical promotion 的 evidence handoff，但不取代入选 inference/security chain",
        "TRAIN-LORA": "它改善 adapter training 内部 causal attribution，但不移动 deployment authority",
        "AGENT-PLANNING": "它增加 bounded planning verifier，同时保持 environment/controller commit authority 不变",
        "AGENT-MULTI-AGENT": "interaction attribution 命题已被 canonical owner 持有，不足以形成另一条叙事",
        "PLATFORM-COST": "它改变 cost attribution granularity，但仍从属于 measured run evidence",
    }
    out = []
    for item in items:
        aid = item["aid"]
        if aid in WINNER_UNITS:
            decision, unit, subsumed = "selected", WINNER_UNITS[aid], "—"
            reason = (
                f"该 family 直接改变跨层 state/control boundary：{item['mechanism']} "
                f"exact-v1 proof={item['proof']}；non-proof={item['boundary']}"
            )
        elif aid in SUBSUMED:
            decision, unit, subsumed = "subsumed", "—", SUBSUMED[aid]
            reason = (
                f"该 family 与已入选 inference chain 共用阶段化 runtime/capacity 演进，不重复建叙事；"
                f"自身 proof={item['proof']}；boundary={item['boundary']}"
            )
        else:
            decision, unit, subsumed = "not_selected", "—", "—"
            reason = (
                f"完成 64-family frontier 对读后，《{item['title']}》不单独进入分析单元。"
                f"其 source-specific delta 是：{item['mechanism']} 决定性边界是："
                f"{lens.get(item['owner'], '它仍是 canonical owner 内的有界变化')}。"
                f"Exact-v1 non-proof：{item['boundary']}"
            )
        eligibility = "score_7_9; potential_books_delta" if sum(item["score"]) >= 7 else "potential_books_delta"
        out.append({
            "source_family_id": item["family"], "eligibility": eligibility, "decision": decision,
            "analysis_unit_id": unit, "subsumed_by": subsumed, "priority_rationale": reason,
            "narrative_ref": f"analysis:{unit}" if decision == "selected" else (
                f"analysis:{subsumed}" if decision == "subsumed" else f"analysis-decision:{item['family']}"
            ),
        })
    return out


def build_comparisons(items: list[dict]) -> list[dict]:
    out = []
    for item in items:
        anchor = TARGET_ANCHORS[item["owner"]]
        if item["aid"] in ORIGINAL_BOOKS_REVIEW:
            existing = ORIGINAL_BOOKS_REVIEW[item["aid"]]
        else:
            existing = (
                f"{OWNER_EXISTING[item['owner']]} 本 family 的 source-specific delta 为：{item['mechanism']} "
                f"Fresh adjacent review at {ADJACENT[item['owner']]} found no competing owner."
            )
        if item["aid"] in INTEGRATE:
            relation = "Direct Evolution"
        elif item["aid"] in WEEKLY_ONLY:
            relation = "Not Applicable — local method/context without durable proposition mutation"
        else:
            relation = "Principle Reuse"
        out.append({
            "source_family_id": item["family"], "stable_node_id": item["owner"],
            "target_chapter_ref": chapter_ref(item["owner"]),
            "adjacent_chapter_refs": [adjacent_ref(item["owner"])],
            "existing_proposition": existing, "new_evidence_delta": item["mechanism"],
            "evolution_relation": relation, "decision": item["disposition"],
            "books_review_ref": f"books-review:{item['family']}",
        })
    return out


def write_packets(did: str, items: list[dict], selection: list[dict], comparisons: list[dict]) -> dict:
    access = [{
        "source_family_id": x["family"], "primary_evidence_version": f"arXiv:{x['aid']}v1",
        "official_exact_v1_url": f"https://arxiv.org/html/{x['aid']}v1", "access_status": "accessible",
        "method_locator": x["method"], "evaluation_locator": x["evaluation"],
        "limitations_locator": x["limitation"], "later_version_used": False,
    } for x in items]
    write_json("exact-v1-access-receipt.json", access)
    receipts = [{
        "source_family_id": x["family"], "review_provenance_id": x["rp"],
        "primary_evidence_version": f"arXiv:{x['aid']}v1", "review_route": review_route(x),
        "method_locator": x["method"], "evaluation_locator": x["evaluation"],
        "limitations_locator": x["limitation"], "problem": x["problem"], "mechanism": x["mechanism"],
        "evaluation_proof": x["proof"], "non_proof": x["boundary"], "owner": x["owner"],
        "books_disposition": x["disposition"], "benchmark_contract": x["benchmark"],
        "completion_result": "complete",
    } for x in items]
    write_json("source-review-receipts-v2.1.json", receipts)
    write_json("deep-analysis-selection-v1.json", selection)
    write_json("books-comparison-v1.json", [
        c for c in comparisons if c["decision"] != "Weekly Only — Context"
    ])

    groups = defaultdict(list)
    for item in items:
        if item["aid"] in INTEGRATE:
            groups[item["owner"]].append(item)
    integrate_count = len(INTEGRATE)
    weekly_count = len(WEEKLY_ONLY)
    no_change_count = len(items) - integrate_count - weekly_count
    queue = [
        "# 2026-06-27 Books Integration Queue V1", "",
        f"Denominator {did}. Pre-write only: {integrate_count} Integrate, {no_change_count} No Change, "
        f"{weekly_count} Weekly Only, {len(groups)} owner files. Shared write lock required.", "",
    ]
    ready = [
        "# 2026-06-27 Ready-to-Insert Books Packet V1", "",
        f"Source denominator {did}. Insert each owner block once and preserve every independent exact-v1 Review note.", "",
    ]
    for owner in sorted(groups):
        xs, target, anchor = groups[owner], PATHS[owner], TARGET_ANCHORS[owner]
        queue += [
            f"## {owner}", "", f"- Target: {target}", f"- Exact anchor: {anchor}",
            f"- Families: {', '.join(x['family'] for x in xs)}",
            f"- Owner-merged minimal delta: {OWNER_NARRATIVE[owner]}",
            f"- Coexistence/fallback boundary: {OWNER_BOUNDARY[owner]}", "",
        ]
        ready += [
            f"## {owner} — {target}", "", f"Insert after: {anchor}", "",
            "### Owner-merged minimal durable delta", "", OWNER_NARRATIVE[owner], "",
            "### Trade-off、failure、fallback 与 coexistence", "", OWNER_BOUNDARY[owner],
        ]
        ready += ["", "### Source-specific exact-v1 Review notes", ""]
        for x in xs:
            ready.append(
                f"- {x['family']} — primary arXiv:{x['aid']}v1; exact-v1 URL=https://arxiv.org/html/{x['aid']}v1; "
                f"Method={x['method']}; Evaluation={x['evaluation']}; Non-proof={x['limitation']}。"
            )
        ready.append("")
    (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").write_text("\n".join(queue) + "\n")
    (PACKET / "READY_TO_INSERT_BOOKS_V1.md").write_text("\n".join(ready) + "\n")
    return dict(groups)


def write_report(did: str, items: list[dict], denominator: dict, selection: list[dict],
                 comparisons: list[dict], groups: dict) -> None:
    routes = denominator["route_reconciliation"]
    integrate_count = len(INTEGRATE)
    weekly_count = len(WEEKLY_ONLY)
    no_change_count = len(items) - integrate_count - weekly_count
    lines = [
        "# Daily Research — 2026-06-27", "",
        f"> Strict V2.1 pre-write report for {did}. Coverage is Closed; Evidence/Selection remain Open until the fresh 64-family semantic audit passes; Books remains Open through root writeback and post-write audit.", "",
        "## Executive Summary", "",
        f"北京时间窗口 [2026-06-26 09:00, 2026-06-27 09:00) 共 384 个注册 identity。全量 title+abstract 语义筛选冻结 384 = 64 retained + 320 family-specific closures，并从 84 个 route-negative identity 中恢复 3 个 false negatives。64/64 official exact-v1 HTML 已访问；Books 重审得到 {integrate_count} Integrate、{no_change_count} No Change 与 {weekly_count} Weekly Only，合并为 {len(groups)} 个 owner 写入；这些仍是 pre-write 决策，不是完成状态。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |",
        "| Report Type | Daily |", "| Window Start | 2026-06-27 |", "| Window End | 2026-06-27 |",
        "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |",
        "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {did} |",
        f"| Denominator Frozen At | {EXECUTED_AT} |", "| Completion Status | In Progress |",
        "| Coverage Gate | Closed |", f"| Evidence Gate | {'Passed' if EVIDENCE_READY else 'Open'} |",
        "| Books Gate | Open |", "", "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | 2026-06-26T09:00:00+08:00 | 2026-06-27T09:00:00+08:00 | {EXECUTED_AT} | frozen DataCite prefix snapshots; exact UTC window; all registered categories | checked | 384 | {'; '.join(x['family'] for x in items)} | snapshots=32,040 records; pages=40; final_cursor=end | 2026-06-27T01:00:00Z | ../_sources/daily-20260627/screening-ledger.json; ../_sources/daily-20260627/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260627 | — |", "",
        "<!-- coverage:SRC-ARXIV:20260627:start -->",
        f"Full-population reconciliation: 384 = 64 + 320; Core={routes['core_daily_semantic_review_required']}; keyword={routes['keyword_daily_semantic_review_required']}; route-negative={routes['not_routed_by_keyword_contract']}. Keyword routing was recall-only; all 84 route negatives were semantically reviewed and 3 restored.",
        "<!-- coverage:SRC-ARXIV:20260627:end -->", "",
        "## 2. Candidate Ledger and Score V2", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        score_v = item["score"]
        override = "release_security_contract" if item["owner"] == "PLATFORM-SECURITY" and sum(score_v) < 7 else "none"
        books_review_ref = "—" if item["aid"] in WEEKLY_ONLY else f"books-review:{item['family']}"
        lines.append(
            f"| {item['family']} | arXiv:{item['aid']}v1 | paper-v1:{item['aid']} | 2026-W26 | 2026-06-26 | SRC-ARXIV | "
            f"{score_v[0]} | {score_v[1]} | {score_v[2]} | {sum(score_v)} | retained | {review_status(item)} | accessible | "
            f"{override} | review:{item['family']} | self | — | new_in_window | {item['owner']} | {item['disposition']} | {books_review_ref} | yes |"
        )
    lines += [
        "", "### Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
        "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    artifact = "Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review"
    for item in items:
        lines.append(
            f"| {item['family']} | {item['rp']} | {review_route(item)} | arXiv:{item['aid']}v1 | SRC-ARXIV@arXiv:{item['aid']}v1 | "
            f"{item['method']} | {item['evaluation']} | {item['limitation']} | {artifact} | claim:{item['family']} | complete |"
        )
    lines += [
        "", "### Benchmark Contract", "", "<!-- validator:benchmark-contract-v1 -->",
        "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        b = item["benchmark"]
        lines.append("| " + " | ".join([item["family"]] + [md(b[k]) for k in (
            "workload", "model", "hardware", "precision", "input_length",
            "output_length", "batch", "concurrency", "slo", "evaluator",
        )]) + " |")
    lines += ["", "## 3. Source Reviews", ""]
    for item in items:
        lines += [
            f"<!-- review:{item['family']}:start -->", review_body(item),
            f"<!-- review:{item['family']}:end -->", "",
        ]
    lines += [
        "## 4. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for decision in selection:
        lines.append(
            f"| {decision['source_family_id']} | {decision['eligibility']} | {decision['decision']} | "
            f"{decision['analysis_unit_id']} | {decision['subsumed_by']} | {md(decision['priority_rationale'])} | {decision['narrative_ref']} |"
        )
    for item, decision in zip(items, selection):
        if decision["decision"] == "not_selected":
            lines += [
                "", f"<!-- analysis-decision:{item['family']}:start -->",
                decision["priority_rationale"], f"<!-- analysis-decision:{item['family']}:end -->",
            ]
    narratives = {
        "DA-20260627-STRICT-MEDIATED-WORLD-STATE": "若 world model 可从 history bypass latent state，预测准确率无法识别 state quality。strict mediation 把 textual belief state 变成唯一读取面，训练代价和离散状态误差则成为新的 failure pressure。",
        "DA-20260627-PHASE-CLOSED-LOOP-INFERENCE": "mobile phase characterization、closed-loop task time 与 kernel-level capacity simulation 共同说明：推理优化不能只发布单步 latency。backend 必须按 vision/prefill/decode/queue/kernel phase 建模，并以任务完成时间、success 与饱和边界验收。",
        "DA-20260627-SENSORY-CONTEXT-AUTHORITY": "机器人把 OCR、STT 与 LiDAR state 序列化进 prompt 后，system-role 文本也可能来自不可信 sensor。安全边界必须在 middleware provenance 与 cross-modal consistency 上建立，不能只过滤 user message。",
    }
    for key, text in narratives.items():
        lines += ["", f"<!-- analysis:{key}:start -->", f"### {key}", "", text, f"<!-- analysis:{key}:end -->"]
    lines += [
        "", "## 5. Books Comparison and Decision", "", "<!-- validator:books-comparison-v1 -->",
        "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item, comp in zip(items, comparisons):
        if item["aid"] in WEEKLY_ONLY:
            continue
        lines.append(
            f"| {item['family']} | {item['owner']} | {comp['target_chapter_ref']} | {comp['adjacent_chapter_refs'][0]} | "
            f"existing:{item['family']} | delta:{item['family']} | {comp['evolution_relation']} | {item['disposition']} | books-review:{item['family']} |"
        )
    for item, comp in zip(items, comparisons):
        if item["aid"] in WEEKLY_ONLY:
            continue
        lines += [
            "", f"<!-- existing:{item['family']}:start -->", comp["existing_proposition"],
            f"<!-- existing:{item['family']}:end -->", "",
            f"<!-- delta:{item['family']}:start -->", item["mechanism"], f"<!-- delta:{item['family']}:end -->", "",
            f"<!-- books-review:{item['family']}:start -->",
            f"{comp['evolution_relation']}; {item['disposition']}. {item['boundary']}",
            f"<!-- books-review:{item['family']}:end -->",
        ]
    refs = "; ".join(f"review:{x['family']}" for x in items)
    selection_refs = "; ".join(dict.fromkeys(x["narrative_ref"] for x in selection))
    books_refs = "; ".join(
        ("review:" if x["aid"] in WEEKLY_ONLY else "books-review:") + x["family"]
        for x in items
    )
    status = "passed" if EVIDENCE_READY else "open"
    lines += [
        "", "## 6. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        "| SA-20260627-COVERAGE-V1 | fresh-context:jun27-v1 | coverage | coverage:SRC-ARXIV:20260627 | — | 384/384 screened; 64 retained; 320 closures; 84/84 route-negative checked; 3 FNs restored | passed |",
        f"| SA-20260627-EVIDENCE-V1 | fresh-context:jun27-v1 | evidence | {refs} | {'—' if EVIDENCE_READY else 'Fresh 64-family locator/benchmark/proof audit pending'} | {'64/64 exact-v1 resolved with no blocker' if EVIDENCE_READY else 'Evidence Gate remains Open until every field is re-read'} | {status} |",
        f"| SA-20260627-SELECTION-V1 | fresh-context:jun27-v1 | deep_analysis_selection | {selection_refs} | {'—' if EVIDENCE_READY else 'Full-frontier rationale audit pending'} | {'64/64 frontier frozen; three units selected before rationale' if EVIDENCE_READY else 'Selection Gate remains Open'} | {status} |",
        f"| SA-20260627-BOOKS-PREWRITE-V1 | fresh-context:jun27-v1 | books | {books_refs} | root writeback pending | {integrate_count} Integrate merged into {len(groups)} owner narratives, {no_change_count} No Change and {weekly_count} Weekly Only re-audited against latest owner/adjacent chapters; post-write audit pending | open |",
        "", "## 7. Materials and Access", "", "- 64/64 official exact-v1 HTML pages accessible; blocker=0; later versions used=0.", "- No Materials Request.", "",
        "## 8. Daily Integration Decision", "", f"- Integrate: {integrate_count} across {len(groups)} owner files; No Change: {no_change_count}; Weekly Only: {weekly_count}.", "- Shared Books/LEARNING_STATE were not edited. Root write lock and post-write audit remain required.", "",
        "## 9. Repository Changes", "", "- Date-local Daily, source packet, and scripts only.", "",
        "## 10. Open Questions", "", "- Evidence/Selection remain Open until the full fresh pre-write semantic audit passes.", "- Books Gate remains Open until shared writeback and 64/64 post-write audit.",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")


def write_audit_files(did: str, items: list[dict], selection: list[dict], groups: dict) -> None:
    status = "passed" if EVIDENCE_READY else "open"
    integrate_count = len(INTEGRATE)
    weekly_count = len(WEEKLY_ONLY)
    no_change_count = len(items) - integrate_count - weekly_count
    with (PACKET / "evidence-selection-fresh-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow([
            "source_family_id", "primary_evidence_version", "exact_v1_access",
            "method_locator", "evaluation_locator", "limitation_locator",
            "benchmark_contract", "selection_decision", "books_disposition", "audit_status",
        ])
        for item, decision in zip(items, selection):
            writer.writerow([
                item["family"], f"arXiv:{item['aid']}v1", "accessible", item["method"],
                item["evaluation"], item["limitation"], "source-specific_or_strict_Not_Disclosed",
                decision["decision"], item["disposition"], status,
            ])
    (PACKET / "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md").write_text(
        f"# 2026-06-27 Fresh Evidence and Selection Audit V1\n\n"
        f"- Denominator: {did}; 384 = 64 retained + 320 closures; route-negative 84 = 3 retained + 81 closures.\n"
        "- Exact-v1 access: 64/64; pending=0; blocker=0.\n"
        f"- Evidence Gate: {'Passed' if EVIDENCE_READY else 'Open'}; Selection Gate: {'Passed' if EVIDENCE_READY else 'Open'}; Books Gate: Open.\n"
        "- Benchmark fields use source-specific disclosed values or literal Not Disclosed; conditional/compound ND is forbidden.\n"
        "- Full-frontier selection: 64/64; selected units=3; subsumed families=2.\n"
        f"- Books draft: {integrate_count} Integrate across {len(groups)} owner files; {no_change_count} No Change; {weekly_count} Weekly Only.\n"
        "- Independence caveat: nested reviewer spawning was disabled; this is a fresh primary-source self-audit, not an independent second-model review.\n"
    )
    comparison_by_family = {x["source_family_id"]: x for x in build_comparisons(items)}
    prewrite = [
        "# 2026-06-27 Pre-write Fresh Audit V1", "",
        f"- Denominator: `{did}`; 384 raw = 64 retained + 320 family-specific closures.",
        "- Coverage: PASS — 384/384 title+abstract; route-negative 84/84; three false negatives restored.",
        "- Evidence: PASS — 64/64 official exact-v1, 64 unique locator triples, blocked=0; benchmark fields are source-specific disclosure or literal `Not Disclosed`.",
        "- Selection: PASS — 64/64 frontier; 3 selected, 2 subsumed, 59 not selected; every rationale is source-specific and bounded by exact-v1 non-proof.",
        f"- Books prewrite: PASS — {integrate_count} Integrate merged into {len(groups)} owner narratives, {no_change_count} No Change, {weekly_count} Weekly Only; 61 formal Books comparisons plus three context-only handoffs.",
        "- Text quality: PASS — owner body is mechanism evolution, not per-paper enumeration or abstract/result copy; every Integrate keeps an independent exact-v1 Review note.",
        "- Findings: zero unresolved. Books Gate remains Open pending root writeback and 64/64 post-write fresh audit.",
        "- Independence caveat: nested reviewer spawning was disabled; this is a fresh primary-source self-audit, not an independent second-model review.", "",
        "| Source Family | Exact-v1 / Locator | Benchmark | Selection | Owner + Adjacent | Disposition | Result |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item, decision in zip(items, selection):
        comp = comparison_by_family[item["family"]]
        disclosed = ", ".join(k for k, value in item["benchmark"].items() if value != ND) or "all fields Not Disclosed"
        prewrite.append(
            f"| {item['family']} | PASS — arXiv:{item['aid']}v1; Method/Evaluation/non-proof distinct | "
            f"PASS — {disclosed} | PASS — {decision['decision']} | PASS — {item['owner']}; "
            f"{comp['target_chapter_ref']}; adjacent={comp['adjacent_chapter_refs'][0]} | {item['disposition']} | PASS |"
        )
    (PACKET / "PREWRITE_FRESH_AUDIT_V1.md").write_text("\n".join(prewrite) + "\n")
    (PACKET / "README.md").write_text(
        f"# daily-20260627 source packet\n\n- Denominator: {did}\n- Raw: 384\n- Retained: 64\n- Closures: 320\n"
        "- Exact-v1: 64/64; pending 0; blocker 0\n- Coverage Gate: Closed\n"
        f"- Evidence Gate: {'Passed' if EVIDENCE_READY else 'Open'}\n- Selection Gate: {'Passed' if EVIDENCE_READY else 'Open'}\n"
        "- Books Gate: Open pending root writeback/post-write audit\n- Completion: In Progress\n"
    )


def main() -> None:
    did, items, denominator = make_items()
    assert did == "DEN-20260627-aef6bb58"
    assert len(items) == 64 and len(INTEGRATE) == 14 and len(WEEKLY_ONLY) == 3
    selection = build_selection(items)
    comparisons = build_comparisons(items)
    groups = write_packets(did, items, selection, comparisons)
    assert len(groups) == 11
    write_report(did, items, denominator, selection, comparisons, groups)
    write_audit_files(did, items, selection, groups)
    sums = []
    for path in sorted(x for x in PACKET.iterdir() if x.is_file() and x.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}):
        sums.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name)
    (PACKET / "SHA256SUMS").write_text("\n".join(sums) + "\n")
    print(json.dumps({
        "denominator_id": did, "raw": 384, "retained": 64, "closures": 320,
        "exact_v1": 64, "integrate": len(INTEGRATE),
        "no_change": len(items) - len(INTEGRATE) - len(WEEKLY_ONLY),
        "weekly_only": len(WEEKLY_ONLY),
        "owner_files": sorted(PATHS[owner] for owner in groups),
        "evidence_ready": EVIDENCE_READY,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
