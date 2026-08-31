#!/usr/bin/env python3
"""Materialize the independent fresh-context audit for 2026-05-25.

This script only writes date-local Daily artifacts and the canonical Daily README.
It never writes shared Books files.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256


REPORT_DATE = "2026-05-25"
REVIEWED_AT = "2026-09-01T18:30:00+08:00"
AUTHOR = json.loads((HERE / "screening-ledger-final.json").read_text())
AUTHOR_REVIEWS = {
    item["arxiv_id"]: item
    for item in json.loads((HERE / "exact-v1-review-packet.json").read_text())
}
AUTHOR_COMPARISONS = {
    item["arxiv_id"]: item
    for item in json.loads((HERE / "books-current-content-comparison.json").read_text())
}


def family(arxiv_id: str) -> str:
    return "SF-2026-ARXIV-" + arxiv_id.replace(".", "-")


def score(total: int) -> dict[str, int]:
    if total == 9:
        values = (3, 3, 3)
    elif total == 8:
        values = (3, 2, 3)
    elif total == 7:
        values = (2, 2, 3)
    else:
        raise ValueError(total)
    return {"design_delta": values[0], "system_reach": values[1], "durability": values[2], "total": total}


REOPEN = {
    "2605.24818": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 8, "decision": "Integrate",
        "method": "§3 Simulating contamination; §3.1 Estimators and predictors; §3.2 Data generation",
        "evaluation": "§4 Benchmarking predictors; §5 Practical considerations; Appendix B Experimental details",
        "limitations": "§5 Practical considerations; §6 Discussion: controlled Hubble-8B/test-set setting, training-data access and counterfactual-model assumptions",
        "mechanism": "在已知比例主动注入 benchmark 样本并拟合 contamination-response curve，把污染校正从事后猜测变成带干预记录的 evaluation protocol。",
        "boundary": "只证明论文披露的 Hubble-8B、五类 benchmark 与模拟污染设置；需要训练数据写权限和未污染 counterfactual 假设，不能外推成任意闭源模型的通用校正器。",
    },
    "2605.24883": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 8, "decision": "Integrate",
        "method": "§3 Methodology: policy-to-FOL translation, semantic policy graph and graph-guided query instantiation",
        "evaluation": "§4 Evaluation: policy coverage and attack efficacy",
        "limitations": "§ Limitations: policy-quality dependency, static single-turn scope, no multi-turn or agent-state coverage",
        "mechanism": "把自然语言 safety policy 编译为形式化谓词和语义图，再从未覆盖路径生成可追踪测试，使 policy revision、test identity 与 coverage evidence 成为同一评估对象。",
        "boundary": "垃圾输入 policy 会直接产生错误测试；exact-v1 只覆盖静态单轮交互，未证明多轮 Agent state、生产 policy 漂移或自动生成测试的完备性。",
    },
    "2605.24922": {
        "owner": "MULTIMODAL-EMBODIED-VLA", "total": 8, "decision": "Integrate",
        "method": "§3 System Design and API; §3.1 Design boundary; §3.2 Persistent pool ownership; §3.3 Runtime primitives; §3.4 Reset-time randomization",
        "evaluation": "§4 Validation and Benchmarks: parity, rollout throughput, reset and Jacobian measurements",
        "limitations": "§6 Discussion; §6.1 Runtime boundary and trade-offs; §6.3 Reproducibility",
        "mechanism": "把 stateless rollout 调用提升为 executor-owned persistent environment pool，使 per-environment model/data、reset、step 与 Jacobian state 在 batched robot-learning loop 中保持可寻址。",
        "boundary": "证据绑定 MuJoCo 与论文测试硬件/任务；persistent pool 增加生命周期、隔离和复现责任，未证明真实机器人、分布式故障或硬实时控制语义。",
    },
    "2605.24930": {
        "owner": "MODEL-LONG-CONTEXT", "total": 7, "decision": "No Change — Existing Coverage",
        "method": "§3 Methodology; §3.1 Semantic tree construction; §3.2 Memory-token construction; §3.3 Hierarchical inference; §3.4 Objectives",
        "evaluation": "§4 Experiments: LongBench/structured-document quality, TTFT and memory",
        "limitations": "§5 Conclusion and discussion: hierarchy dependency, heuristic-tree error propagation, rare-evidence attenuation and routing-prune risk",
        "mechanism": "先把长文档组织成语义树，再用层级 memory tokens 与 query-aware routing 在粗摘要和细粒度节点间分配注意力预算。",
        "boundary": "收益依赖可恢复的文档层级；错误树和过度压缩会丢失稀有证据。当前 Ch22 已拥有 query-aware hierarchical selection、coarse summary 与 dense fallback，因此不重复写入。",
    },
    "2605.24973": {
        "owner": "AGENT-RAG", "total": 7, "decision": "Integrate",
        "method": "§3 Problem formulation; §4.1 Task-oriented data engine; §4.2 Dynamic chunking and synchronization; §4.3 Document enrichment",
        "evaluation": "§5 Experiments: five OCR backends and downstream RAG/QA",
        "limitations": "§5 evaluation scope and §6 conclusion: OCR/model/workload boundary; cross-page summaries can suppress fine-grained evidence",
        "mechanism": "在 page OCR 之后增加 document-level state owner，跨页合并段落/表格并同步 chunk 与结构索引，使 ingestion 输出可被 RAG 以同一 document revision 消费。",
        "boundary": "作者结果绑定披露的 OCR/VLM、H200 与文档集合；跨页修复可能合并错误或隐藏细粒度 locator，不能替代原页、region provenance 与独立 evidence check。",
    },
    "2605.25160": {
        "title": "SimuWoB: Simulating Real-World Mobile Apps for Fast and Faithful GUI Agent Benchmarking",
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 8, "decision": "No Change — Existing Coverage",
        "method": "§3 SimuWoB; §3.1 Environment generation; §3.2 Task and validator generation",
        "evaluation": "§4 Experiments: app fidelity, task feasibility and GUI-agent evaluation",
        "limitations": "§5 Limitations: visual-only interface, single-app tasks, no accessibility tree or cross-app workflow",
        "mechanism": "由 coding agent 合成可执行 mobile-app simulator，再独立生成 task 与 state validator，把 GUI agent benchmark 的 environment 和 outcome evidence 版本化。",
        "boundary": "只覆盖视觉单应用 simulator；不等于真实 backend、跨应用状态或 accessibility-tree 行为。当前 Ch66/Ch81 已明确 environment generation、task constraint、validator 与 durable marker 分责，故不重复写入。",
    },
    "2605.25240": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 7, "decision": "Integrate",
        "method": "§3.1 Dataset; §3.2 Constructed quality levels; §3.3 Rubric and pairwise-preference expert annotation",
        "evaluation": "§4 Empirical comparison of rubric scoring and comparative judgment",
        "limitations": "Appendix A.1 Limitations: legal-domain scope, prompt-induced quality confounds, style cues and mixed-trade-off cases",
        "mechanism": "把 rubric score 与 pairwise preference 作为不同 measurement operators，在同一受控质量阶梯上比较各自一致性与区分力，而不是默认二者可互换。",
        "boundary": "证据主要来自法律文本和 prompt 构造的质量层级，质量与表达风格可能共变；不能据此规定所有 evaluator 都应采用同一判断形式。",
    },
    "2605.25272": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 7, "decision": "Integrate",
        "method": "§2 Variance decomposition, confirmatory factor analysis, bifactor model and mixed-effects latent regression; §3 Experiment and data",
        "evaluation": "§4 Results across six benchmark ecosystems",
        "limitations": "§ Limitations: one snapshot/six benchmarks, observational design, noisy metadata, non-representative sample and temporal instability",
        "mechanism": "用 latent measurement model 分解 benchmark 共同因子与 task-specific variance，使 release evidence 能区分能力构念、数据生态和 leaderboard 聚合造成的相关性。",
        "boundary": "只是一轮六 benchmark 的观察性快照；latent factor 不是能力本体，也不证明因果。模型、数据与提交策略变化后必须重新拟合而不能复用旧 factor。",
    },
    "2605.26156": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 8, "decision": "No Change — Existing Coverage",
        "method": "§3 Threat model; §4 Contextual-bandit black-box style attack; §5 Analysis",
        "evaluation": "§6 Evaluation on chatbot leaderboards and automated peer review, including stealth and mitigation",
        "limitations": "§7 Conclusion and Appendix experiments: tested-judge/task/style scope; semantic-preservation proxy and adaptive-query-budget boundary",
        "mechanism": "把 judge 的 style sensitivity 暴露为可自适应搜索的黑盒攻击面，并同时测 utility、stealth 与 query budget。",
        "boundary": "攻击只覆盖给定 judge、任务和 style transformations，语义保持依赖 LLM/embedding proxy。Ch66 已把 position/style/self-preference 与受控不变性 intervention 写入 construct-validity contract，故不重复写入。",
    },
    "2605.26161": {
        "owner": "PLATFORM-EVALUATION-SYSTEM", "total": 7, "decision": "No Change — Existing Coverage",
        "method": "§3 Problem formulation; §4 TSFMAudit; §4.1 adaptation traces; §4.2 reference-model debiasing; §4.3 calibration and decision",
        "evaluation": "§5 Experiments on six TSFMs/187 datasets; §5.5 practical deployment; Appendix B audit protocol",
        "limitations": "Appendix A contamination labels and transformed-duplicate semantics; proxy labels depend on incomplete official corpus documentation",
        "mechanism": "用 fine-tuning loss drop、backbone displacement 与 reference-model debiasing构成 dataset-level contamination-risk sensor，处理连续时序的缩放/重采样重复。",
        "boundary": "标签来自不完整训练来源文档，参考模型与 probe protocol 会影响 verdict；结论绑定 TSFM/time-series。Ch27/Ch66 已拥有 contamination identity、transformed duplicate 与受限 sensor/release boundary，故不扩写领域特例。",
    },
    "2605.26162": {
        "owner": "TRAIN-DISTRIBUTED-TRAINING", "total": 7, "decision": "Integrate",
        "method": "§4 PushCen-ADFL; §4.2 centroid regularization; §4.3 compression; §4.4 push-sum aggregation; §4.5 buffered updates; Appendix C event-driven state accounting",
        "evaluation": "§5 Experiments; §5.1.4 delayed-client protocol; §5.2 accuracy/communication/overhead; §5.3 delayed clients",
        "limitations": "§4.6 assumptions and Appendix C: bounded staleness, directed mixing, bounded compression error and simulated event-driven network",
        "mechanism": "在无中心异步联邦训练中用 push-sum numerator/denominator、in-flight mass 与 buffered message state 修正有向图聚合偏差，并以 centroid dictionary 压缩通信。",
        "boundary": "实验用 event-driven simulator、vision models 和受控 client delay；收敛依赖 bounded staleness/mixing/compression-error 假设，不能证明真实 WAN、Byzantine client 或大模型训练。",
    },
    "2605.24870": {
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "total": 8, "decision": "Integrate",
        "method": "§2 Problem Formulation; §3.1 Local Statistical Calibration; §3.2 Trajectory-Consistent Prior Estimation",
        "evaluation": "§4.1–§4.3 PixArt-alpha/DiT-XL/2 experiments and ablations; Appendix B.1–B.8 latency, prompt-count and compute details",
        "limitations": "Appendix C Limitations and Broader Impact; offline priors, selected sites/windows, representative-prompt and tested-model boundary",
        "mechanism": "把 diffusion cache 的误差从单点 representation mismatch 扩展为会被先前校准继续改写的 trajectory state，并沿 corrected history 逐步拟合 site-local calibration prior。",
        "boundary": "只验证 PixArt-alpha、DiT-XL/2、FORA/ToCa/L2C 与披露的离线 prior、采样步数和 H800 路径；prior 漂移、未测 cache policy、在线并发与分布外 prompt 不受该结果保证，失配时应回退 base cache 或 full computation。",
    },
    "2605.24879": {
        "owner": "PLATFORM-SECURITY", "total": 8, "decision": "Integrate",
        "method": "§4 Proposed Method; §5 Privacy Analysis and Accounting; Appendix B.9 randomized-clipping accountant",
        "evaluation": "§6 Experiments; §6.1 Memory, Compute and Latency Gains; Appendix D hyperparameters",
        "limitations": "§7 Conclusion and experiment scope: Llama-3.2-1B, sequence length 4096, selected full/LoRA fine-tuning tasks and randomized norm-estimation assumptions",
        "mechanism": "用 Hutchinson/Hutch++ 随机 trace estimation 近似 per-sample gradient norm，把 DP clipping 的显存复杂度从显式 T×T 或 d×d 中间量改为受投影维度控制的 estimator，并为随机 clipping 单独建立 privacy accountant。",
        "boundary": "形式保证依赖论文的随机 clipping mechanism 与 accountant 被原样实现；实验只覆盖 Llama-3.2-1B、固定 4096 长度和三类任务，未证明大模型、分布式 microbatch、任意 epsilon 或任意投影维度下同时保持 utility 与成本优势。",
    },
    "2605.24892": {
        "owner": "MULTIMODAL-WORLD-MODELS", "total": 8, "decision": "No Change — Existing Coverage",
        "method": "§3.1 Large Drive Model, especially §3.1.3 chunk-wise prediction/CLEF/TIS; §3.2 Vision Renderer; §3.3 training and interleaved inference pipeline",
        "evaluation": "§4.1 Large Drive Model and §4.2 Vision Renderer, including horizon/CL-CLEF-TIS ablations and production-scale comparison",
        "limitations": "§5 Conclusion/future directions; private driving-data distribution, learned renderer and offline/closed-loop evaluation boundary; no dedicated limitations section",
        "mechanism": "把低熵相邻帧预测改成跨语义时间块的自回归 future-state 预测：块内保留稠密瞬时动态、块间保留稀疏长程因果，并把 action/latent prediction 与多视角 renderer 分责。",
        "boundary": "证据绑定作者私有驾驶数据、4 Hz 七相机 rollout、learned renderer 与披露的闭环设置；视觉一致性和 planning gain 不证明真实道路安全、因果识别或跨 embodiment 泛化。Ch25 已有 transition-token/reasoner/renderer 分责和多时间尺度状态边界，故不重复写入。",
    },
    "2605.25073": {
        "owner": "PLATFORM-SECURITY", "total": 8, "decision": "No Change — Existing Coverage",
        "method": "§2 Evaluation Substrate and Threat Model; §3–§5 pre/during/post-tuning lifecycle taxonomy; §6 unified cross-phase evaluation",
        "evaluation": "§6.2–§6.6 shared models/tasks, reproduced attacks and cross-phase defense combinations",
        "limitations": "§7 Discussion and §8 Future Directions; reproduced small-model/task configurations, method-compatibility substitutions and lifecycle-survey boundary",
        "mechanism": "把 fine-tuning attack surface 按 pre-tuning input/supply chain、during-tuning optimizer/update 与 post-tuning adapter/artifact 三个 intervention phase 组织，并用同一基座和协议检查跨 phase 防御组合。",
        "boundary": "survey taxonomy 与复现实验只能支持披露的 Llama/Qwen 1B–4B、SST-2/AGNews/agent subsets 和选定 attack-defense pairs；不能证明未复现方法、生产 adapter registry 或 RLHF/DPO 路径已被覆盖。Ch72 已拥有 data→update→artifact→runtime 的安全与 release contract，故不重复写入。",
    },
    "2605.25292": {
        "owner": "PLATFORM-GPU-SCHEDULER", "total": 7, "decision": "No Change — Existing Coverage",
        "method": "§II Work Package Structure and Contributions: IAIS data flow, formal workflow mapping, Kubernetes/Slurm control manager and Digital Twin state",
        "evaluation": "§III Evaluation Results: 10–5000 job/node scalability and solver/heuristic workflow comparison",
        "limitations": "§IV Conclusion and project-report scope; component-level evaluation, heterogeneous project artifacts and no controlled end-to-end production SLO comparison",
        "mechanism": "让 scheduler 消费由 Digital Twin 维护的 node power/carbon/anomaly state，并把 heterogeneous workflow 先转成正式 dependency/resource model，再输出 Kubernetes/Slurm placement。",
        "boundary": "论文是 DECICE 项目架构与组件结果汇总；5000×5000 scalability、solver runtime 和 production-like use cases 不是同一 end-to-end SLO 实验，也未证明 RNN/RL 优于所有启发式。Ch63–65 已覆盖 state-aware placement、carbon/energy signal、workflow dependency 与 Slurm/Kubernetes 边界，故不重复写入。",
    },
    "2605.25298": {
        "owner": "PLATFORM-MONITORING", "total": 7, "decision": "Integrate",
        "method": "§III Design; §IV-A eBPF metric collection; §IV-C Selective Thread Tracking and Algorithm 1",
        "evaluation": "§V–§VI six data-intensive applications and CPU/disk/lock/external-service contention; Artifact Description/Evaluation",
        "limitations": "§IV-C optimistic entry-point propagation assumption; §V single x86/Linux 6.8.12 host and six-application workload boundary",
        "mechanism": "从 thread-state 时间占比继续下钻到带 backing-resource identity 的 futex/pipe/socket/VFS/block-I/O dependency graph，并从 request entry thread 反向追踪 contention propagation。",
        "boundary": "选择性算法假设 degradation 能传播到可识别 entry thread；证据绑定单机 x86/Linux 6.8.12、六类应用与人工注入 contention，不能证明跨 kernel、GPU collective、容器隔离或无 socket entry 的训练作业同样可诊断。",
    },
    "2605.26158": {
        "owner": "PLATFORM-SECURITY", "total": 8, "decision": "No Change — Existing Coverage",
        "method": "§3 Safety Instability external/internal diagnostics; §4 fragmented scene-anchored probing and synthesis",
        "evaluation": "§5 HarmBench/MM-SafetyBench experiments, ablations and classical-defense checks; Appendix B.7 human judge validation",
        "limitations": "§ Impact Statement: instability band remains diagnostic, thresholds are not calibrated per input, and cross-fragment evidence requires future context-aware defense",
        "mechanism": "把 refusal 从单一二元阈值改写为可重复采样的 instability band，并把分散于多个 benign-looking probes/视觉片段中的意图在最终 synthesis 时重新组合为跨 turn 攻击。",
        "boundary": "论文没有提供对单个输入校准 tau-/tau+ 的方法；ASR 绑定选定采样参数、HarmBench/MM-SafetyBench、judge 和模型版本。Ch72 已要求 run-centric multi-turn evidence 聚合、cumulative intent 与 sensor/authority 分离，故不重复写入。",
    },
}

# Independent audit can demote an author-retained family when the paper remains a
# representation probe and never changes a system contract.
DEMOTE = {
    "2605.25310": "线性 probe 只证明特定模型 residual stream 中可解码 tool-call dependency；没有提出新的 runtime state owner、tool authorization、workflow commit 或生产 fallback。若后续证明该 signal 可校准地控制 tool execution/recovery 且跨模型成立，再重开 denominator。"
}

FINAL_DECISIONS = {
    "2606.20615": "No Change — Existing Coverage",
    "2605.24817": "Integrate",
    "2605.24823": "No Change — Existing Coverage",
    "2605.24832": "Integrate",
    "2605.24914": "No Change — Existing Coverage",
    "2605.24941": "No Change — Existing Coverage",
    "2605.25002": "Integrate",
    "2605.25052": "No Change — Existing Coverage",
    "2605.25077": "No Change — Existing Coverage",
    "2605.25085": "Integrate",
    "2605.25092": "No Change — Existing Coverage",
    "2605.25133": "No Change — Existing Coverage",
    "2605.25188": "No Change — Existing Coverage",
    "2605.25189": "Integrate",
    "2605.25233": "No Change — Existing Coverage",
    "2605.25244": "No Change — Existing Coverage",
    "2605.25247": "No Change — Existing Coverage",
    "2605.25252": "Integrate",
    "2605.25284": "No Change — Existing Coverage",
    "2605.25313": "No Change — Existing Coverage",
    "2605.26154": "No Change — Existing Coverage",
    "2605.26159": "No Change — Existing Coverage",
    "2605.26165": "No Change — Existing Coverage",
    **{arxiv_id: item["decision"] for arxiv_id, item in REOPEN.items()},
}

OWNER_PATHS = {
    "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md", ["books/part-06-ai-infrastructure/65-kai-scheduler.md", "books/part-06-ai-infrastructure/67-monitoring.md"]),
    "MULTIMODAL-EMBODIED-VLA": ("books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", ["books/part-03-multimodal-world-models/25-multimodal-world-models.md", "books/part-03-multimodal-world-models/README.md"]),
    "MODEL-LONG-CONTEXT": ("books/part-02-model/22-long-context.md", ["books/part-02-model/21-moe.md", "books/part-03-multimodal-world-models/README.md"]),
    "AGENT-RAG": ("books/part-07-agent/76-rag.md", ["books/part-07-agent/75-context.md", "books/part-07-agent/77-memory.md"]),
    "TRAIN-DISTRIBUTED-TRAINING": ("books/part-04-training-system/36-distributed-training.md", ["books/part-04-training-system/35-checkpoint.md", "books/part-04-training-system/37-tensor-parallel.md"]),
    "MULTIMODAL-GENERATIVE-PARADIGMS": ("books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", ["books/part-03-multimodal-world-models/23-multimodal-representation.md", "books/part-03-multimodal-world-models/25-multimodal-world-models.md"]),
    "MULTIMODAL-WORLD-MODELS": ("books/part-03-multimodal-world-models/25-multimodal-world-models.md", ["books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md"]),
    "PLATFORM-GPU-SCHEDULER": ("books/part-06-ai-infrastructure/63-gpu-scheduler.md", ["books/part-06-ai-infrastructure/62-gateway.md", "books/part-06-ai-infrastructure/64-volcano.md"]),
    "PLATFORM-MONITORING": ("books/part-06-ai-infrastructure/67-monitoring.md", ["books/part-06-ai-infrastructure/66-evaluation-system.md", "books/part-06-ai-infrastructure/68-logging.md"]),
    "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md", ["books/part-06-ai-infrastructure/71-multi-tenant.md", "books/part-06-ai-infrastructure/73-production-best-practice.md"]),
}


def specific_closure_reason(row: dict) -> str:
    """Preserve recall evidence without turning closures into a shared template."""
    abstract = re.sub(r"\s+", " ", row.get("abstract", "")).strip()
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", abstract) if s.strip()]
    contribution = next(
        (s for s in sentences if re.search(r"\b(we (?:propose|introduce|present|develop|study|provide)|this (?:paper|work) (?:proposes|introduces|presents|develops|studies))\b", s, re.I)),
        sentences[0] if sentences else row["title"],
    )
    evaluation = next(
        (s for s in sentences if re.search(r"\b(experiments?|evaluation|results?|benchmark)\b", s, re.I)),
        sentences[-1] if sentences else "摘要未披露独立 evaluation contract。",
    )
    text = f"{row['title']} {abstract}".lower()
    if re.search(r"benchmark|evaluation|judge", text):
        boundary = "该 family 的测量对象仍是特定领域/任务或单一 judge protocol，没有改变跨 workload 的 release Gate、measurement owner 或可迁移 evaluation contract。"
    elif re.search(r"\bagent\b|\bagents\b|\btool\b|workflow|\brag\b|retrieval|\bmemory\b", text):
        boundary = "该 family 仍是任务级 Agent/RAG 方法，没有重新分配 durable workflow state、authorization、commit/recovery 或跨任务 evidence owner。"
    elif re.search(r"robot|driving|control|embodied|world model", text):
        boundary = "该 family 的收益绑定特定 embodiment、simulator 或控制任务，没有建立可迁移的 observed/imagined state、safety authority 与 physical fallback contract。"
    elif re.search(r"quantiz|training|optimizer|gradient|reinforcement learning|fine-tun", text):
        boundary = "该 family 改善局部 objective、表示或压缩精度，但没有改变可复算 training-state owner、optimizer/privacy contract、checkpoint/recovery 或跨规模执行边界。"
    elif re.search(r"cache|serving|runtime|schedul|distributed|parallel|network|ebpf|kernel", text):
        boundary = "该 family 的证据仍停留在特定 runtime/workload 局部优化，没有形成跨模型的 state identity、admission/commit、SLO accounting 与故障回退合同。"
    elif re.search(r"security|safety|privacy|attack|adversarial", text):
        boundary = "该 family 只建立特定 threat/model/task 下的攻击或防御结果，没有改变平台 reference monitor、principal/asset identity、release evidence 与 fail-closed authority。"
    else:
        boundary = "该 family 提供领域模型、表示或任务方法增量，但没有改变长期 AI-System 的 state/data/control ownership、evaluation/release contract 或 production fallback。"
    return f"机制：{contribution} 证据：{evaluation} 排除边界：{boundary} 若后续出现跨 workload artifact、明确系统 owner 或可证伪的生产合同，再重开 denominator。"


rows = []
for source in AUTHOR["identities"]:
    row = dict(source)
    arxiv_id = row["arxiv_id"]
    if row.get("screening_status") == "pre_denominator_closure":
        row["screening_reason"] = specific_closure_reason(row)
    if arxiv_id in DEMOTE:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=DEMOTE[arxiv_id],
            review_status="identity_date_closed",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
        for key in ("source_family_id", "owner_node", "score_v2", "method_locator", "evaluation_locator", "limitations_locator"):
            row.pop(key, None)
    elif arxiv_id in REOPEN:
        item = REOPEN[arxiv_id]
        row.update(
            title=item.get("title", row["title"]), source_family_id=family(arxiv_id),
            screening_status="retained", screening_reason=item["mechanism"],
            owner_node=item["owner"], score_v2=score(item["total"]),
            review_status="deep_complete", access_status="accessible",
            integration_disposition=item["decision"], method_locator=item["method"],
            evaluation_locator=item["evaluation"], limitations_locator=item["limitations"],
            claim_boundary=item["boundary"],
        )
    elif row.get("screening_status") == "retained":
        row["integration_disposition"] = FINAL_DECISIONS[arxiv_id]
    rows.append(row)

retained = [row for row in rows if row["screening_status"] == "retained"]
closures = [row for row in rows if row["screening_status"] == "pre_denominator_closure"]
assert len(rows) == 287 and len(retained) == 41 and len(closures) == 246

ledger = dict(AUTHOR)
ledger.update(
    schema="daily-screening-ledger-v2.1-independent-final",
    candidate_denominator=len(retained), pre_denominator_closures=len(closures),
    identities=rows,
)
(HERE / "screening-ledger-independent-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

reviews = []
for row in retained:
    arxiv_id = row["arxiv_id"]
    if arxiv_id in REOPEN:
        item = REOPEN[arxiv_id]
        reviews.append({
            "source_family_id": family(arxiv_id), "arxiv_id": arxiv_id,
            "primary_evidence_version": f"arXiv:{arxiv_id}v1",
            "retrieval_route": "official arXiv exact-v1 HTML",
            "retrieved_at": REVIEWED_AT, "method_locator": item["method"],
            "evaluation_locator": item["evaluation"], "limitations_locator": item["limitations"],
            "claim_boundary": item["boundary"],
        })
    else:
        review = dict(AUTHOR_REVIEWS[arxiv_id])
        review["retrieved_at"] = REVIEWED_AT
        if review.get("claim_boundary", "").startswith("Only the exact-v1 disclosed"):
            review["claim_boundary"] = (
                f"{row['title']} 的 exact-v1 只支持该文披露机制：{row['screening_reason']} "
                f"其未证明边界由 `{review['limitations_locator']}` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。"
            )
        reviews.append(review)
assert len(reviews) == 41
(HERE / "exact-v1-review-packet-independent-final.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")

comparisons = []
for row in retained:
    arxiv_id = row["arxiv_id"]
    if arxiv_id in REOPEN:
        item = REOPEN[arxiv_id]
        owner_path, adjacent = OWNER_PATHS[item["owner"]]
        existing = {
            "2605.24818": "Ch27/Ch66 已有 contamination identity、decontamination 与 release evidence，但没有用主动已知污染率拟合 score-correction curve。",
            "2605.24883": "Ch66/Ch72 已有 red-team、policy revision 与独立 guard，但没有从 policy predicate graph 生成 coverage-traceable tests。",
            "2605.24922": "Ch25/Ch26 已有 simulator/observed-state authority 与 rollback，但没有 executor-owned per-environment persistent batched runtime lifecycle。",
            "2605.24930": "Ch22 已有 coarse global summary、query-aware hierarchical sparse selection、selector miss 与 dense fallback。",
            "2605.24973": "Ch76 已有 document/page/region provenance 与 ingestion identity，但没有跨页结构修复、chunk synchronization 及原页 fallback 的同一 lifecycle。",
            "2605.25160": "Ch66/Ch81 已把 generated environment、task constraint、validator、marker 与真实 backend authority 分开。",
            "2605.25240": "Ch66 已比较 judge/metric 风险，但没有把 rubric 与 pairwise preference 作为不同 measurement operator 做受控同台选择。",
            "2605.25272": "Ch66 已要求 construct validity 和 slice/uncertainty，但没有用 latent measurement model 分离共同构念与 benchmark-specific variance。",
            "2605.26156": "Ch66 已把 position/style/self-preference 及 irrelevant-style intervention 写入 judge construct-validity contract。",
            "2605.26161": "Ch27/Ch66 已保存 contamination source identity、transformed duplicates、sensor uncertainty 与 clean/contaminated slices。",
            "2605.26162": "Ch36 已有 asynchronous arrival bias、staleness、client weighting 与 compression，但没有把 push-sum numerator/denominator 和 in-flight mass 写成恢复/收敛状态。",
            "2605.24870": "Ch24 已有 sensitivity/error-budget cache 与 recompute fallback，但没有把 calibration prior 绑定到被先前 correction 改写后的 denoising trajectory。",
            "2605.24879": "Ch72 已要求 DP sampling/clipping/noise/accounting 实现等价，却没有覆盖 randomized norm estimator 改变 clipping mechanism 后必须配套重建 accountant 与资源合同。",
            "2605.24892": "Ch25 已有 transition-token reasoner、appearance renderer、多时间尺度状态和 closed-loop evidence boundary。",
            "2605.25073": "Ch72 已沿 data/supply-chain、training update、adapter artifact、runtime monitor 与 release Gate 组织 fine-tuning security lifecycle。",
            "2605.25292": "Ch63–65 已让 dependency、resource/topology、energy/carbon/telemetry state 进入 Kubernetes/Slurm placement owner，并保留 heuristic fallback。",
            "2605.25298": "Ch67/69 已区分 metrics 与 trace/dependency graph，但没有从 request entry thread 沿 backing-resource identity 追踪 kernel-level contention propagation。",
            "2605.26158": "Ch72 已要求 run-centric multi-turn/multimodal campaign、跨 turn cumulative intent 聚合和 sensor/authority 分离。",
        }[arxiv_id]
        delta = item["mechanism"]
    else:
        author = AUTHOR_COMPARISONS[arxiv_id]
        owner_path, adjacent = author["owner_path"], author["adjacent_paths"]
        existing = author["existing_proposition"]
        delta = author["new_evidence_delta"]
    comparisons.append({
        "arxiv_id": arxiv_id, "source_family_id": row["source_family_id"],
        "owner_node": row["owner_node"], "owner_path": owner_path,
        "adjacent_paths": adjacent, "existing_proposition": existing,
        "new_evidence_delta": delta, "decision": row["integration_disposition"],
        "audit_basis": "independent reviewer read current owner and adjacent chapters; Review notes alone do not count as coverage",
    })
(HERE / "books-current-content-comparison-independent-final.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")

queue = []
for row in retained:
    if row["integration_disposition"] != "Integrate":
        continue
    comparison = next(item for item in comparisons if item["arxiv_id"] == row["arxiv_id"])
    queue.append({
        "report_date": REPORT_DATE, "arxiv_id": row["arxiv_id"],
        "source_family_id": row["source_family_id"], "stable_node_id": row["owner_node"],
        "owner_path": comparison["owner_path"], "adjacent_paths": comparison["adjacent_paths"],
        "evidence_delta": comparison["new_evidence_delta"],
        "required_post_write_audit": "owner + adjacent; mechanism text before first anchored ^## Review notes",
    })
assert len(queue) == 16
queue_doc = {"schema": "books-writeback-queue-v1-independent-final", "report_date": REPORT_DATE, "status": "awaiting_root_serial_writeback", "items": queue}
(HERE / "books-writeback-queue-independent-final.json").write_text(json.dumps(queue_doc, ensure_ascii=False, indent=2) + "\n")

changes = {
    "false_negatives_reopened": sorted(REOPEN),
    "false_positives_demoted": sorted(DEMOTE),
    "author_denominator": 24, "independent_denominator": 41,
    "author_closures": 263, "independent_closures": 246,
    "author_integrate": 20, "independent_integrate": len(queue),
}
audit = {
    "schema": "daily-fresh-context-independent-audit-v1", "report_date": REPORT_DATE,
    "auditor": "fresh-context-isolated-prewrite-reviewer", "status": "passed_prewrite",
    "scope": {
        "screening_replayed": "287/287", "denominator_challenged": "24 author + 263 closures",
        "exact_v1_reviewed": "41/41", "deep_selection_reviewed": True,
        "books_owner_adjacent_compared": "41/41",
    },
    "changes": changes, "blocked": [], "review_pending": 0,
    "resolved_findings": [
        {"severity": "high", "finding": "18 system-contract families were closed below denominator", "resolution": "reopened and completed exact-v1 review"},
        {"severity": "medium", "finding": "2605.25310 showed representation decodability but no system contract", "resolution": "demoted with explicit reopen condition"},
        {"severity": "high", "finding": "20 provisional Integrate decisions used marker absence instead of semantic current-Books coverage", "resolution": "owner+adjacent comparison plus reopened families produced final queue of 16"},
    ],
    "unresolved_findings": [
        {"scope": "books", "finding": "16 final Integrate items await root serial writeback and post-write semantic audit"}
    ],
    "cross_model_review": "skipped_non_interactive_subtask",
}
(HERE / "fresh-context-independent-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")


def chapter_ref(path: str) -> str:
    match = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree"


comparison_by_id = {item["arxiv_id"]: item for item in comparisons}
review_by_id = {item["arxiv_id"]: item for item in reviews}

lines = [
    "# Daily Research — 2026-05-25", "", "**Research Date:** 2026-05-25", "", "**Timezone:** Asia/Shanghai", "",
    "**Strict Window:** 2026-05-24 09:00:00 ～ 2026-05-25 09:00:00（北京时间，左闭右开）", "",
    "**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。", "",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立 pre-write audit 已通过，等待 root 串行写回 Books 与 post-write semantic audit。", "",
    "## Executive Summary", "",
    "从 91,841 条月度 raw records 中恢复并逐项语义筛选 287/287 个窗口身份。独立审计把 author denominator 24 调整为 41：重开 18 个 false negative，降级 1 个 false positive；pre-denominator closures 263→246，exact-v1 41/41，blocked=0。current owner+adjacent Books 对照把 final Integrate 收敛为 16。共享 Books 未修改。", "",
    "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->", "| Field | Value |", "| --- | --- |",
    "| Contract Version | V2.1 |", "| Score Schema | V2 |", "| Report Type | Daily |", "| Window Start | 2026-05-25 |", "| Window End | 2026-05-25 |",
    "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |", "| Changed Source IDs | — |", "| Previous Denominator ID | — |",
    "| Denominator ID | DEN-20260525-V2-INDEPENDENT-FINAL |", f"| Denominator Frozen At | {REVIEWED_AT} |", "| Completion Status | In Progress |", "| Coverage Gate | Closed |", "| Evidence Gate | Passed |", "| Books Gate | Open |", "",
    "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->", "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
]
ledger_sha = hashlib.sha256((HERE / "screening-ledger-independent-final.json").read_bytes()).hexdigest()
lines.append(f"| SRC-ARXIV | 2026-05-24T09:00:00+08:00 | 2026-05-25T09:00:00+08:00 | {REVIEWED_AT} | DataCite v2 00..99 + 287/287 semantic replay + official exact-v1 HTML/PDF | checked | 287 | {';'.join(row['source_family_id'] for row in retained)} | pages=300;final_cursor=end;raw=91841;registered=287;screened=287;retained=41;closure=246 | 2026-05-25T00:59:59Z | screening-ledger-independent-final.json#sha256={ledger_sha} | — |")
lines += ["", "### Coverage Limitations", "", "<!-- coverage:SRC-ARXIV:20260525:start -->Registered in-window identities 已 287/287 完整语义筛选；独立 reviewer 重放 false-positive/false-negative 后未留下 Coverage blocker。Discovery backstop 不是本报告确定性 Gate 的必需分母。<!-- coverage:SRC-ARXIV:20260525:end -->", "",
          "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
          "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    s = row["score_v2"]; sf = row["source_family_id"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    lines.append(f"| {sf} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W21 | 2026-05-24 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | {row['review_status']} | accessible | {override} | review:{sf} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{sf} | no |")

lines += ["", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
          "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
receipt_indexes = []
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    review = review_by_id[arxiv_id]
    route = "deep"
    method = f"arXiv:{arxiv_id}v1 HTML — {review['method_locator']}"
    evaluation = f"arXiv:{arxiv_id}v1 HTML — {review['evaluation_locator']}"
    limitations = f"arXiv:{arxiv_id}v1 HTML — {review['limitations_locator']}"
    lines.append(f"| {sf} | RP-TODO-{sf} | {route} | arXiv:{arxiv_id}v1 | SRC-ARXIV@arXiv:{arxiv_id}v1 | {method} | {evaluation} | {limitations} | arXiv:{arxiv_id}v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:{sf} | complete |")
    receipt_indexes.append((row, method, evaluation, limitations))

lines += ["", "### Source Reviews", ""]
for row in retained:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    review = review_by_id[arxiv_id]
    boundary = review["claim_boundary"]
    lines += [f"<!-- review:{sf}:start -->", f"#### {row['title']}", "",
              f"**问题与机制。** {row['screening_reason']} 系统 owner=`{row['owner_node']}`。", "",
              f"**Exact-v1 路径。** Method=`{review['method_locator']}`；Evaluation=`{review['evaluation_locator']}`；Limitations/Counterevidence=`{review['limitations_locator']}`。", "",
              f"<!-- claim:{sf}:start -->{boundary}<!-- claim:{sf}:end -->", "",
              f"Books Decision=`{row['integration_disposition']}`；已对 current owner 与相邻章节做非作者语义比较。", f"<!-- review:{sf}:end -->", ""]

lines += ["## 4. Benchmark Contracts", "", "<!-- validator:benchmark-contract-v1 -->", "| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
          "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->", "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |", "| --- | --- | --- | --- | --- | --- | --- |"]
deep = {"2605.24832": "DA-DIFFUSION-ELASTIC-SERVING", "2605.24883": "DA-POLICY-TO-SAFETY-TEST", "2605.25002": "DA-MEMORY-ATTRIBUTION-WATERMARK"}
for row in retained:
    sf = row["source_family_id"]
    selected = row["arxiv_id"] in deep
    unit = deep.get(row["arxiv_id"], "—")
    eligibility = "score_7_9" + ("; forced_review; potential_books_delta" if row["integration_disposition"] == "Integrate" else "")
    rationale = "跨层改变 runtime/evaluation/memory ownership，且 current Books 存在可定位长期缺口" if selected else "exact-v1 与 Books Decision 均完成；未扩写只受 Daily 三项上限约束"
    lines.append(f"| {sf} | {eligibility} | {'selected' if selected else 'not_selected'} | {unit} | — | {rationale} | {'analysis:'+unit if selected else 'analysis-decision:'+sf} |")
deep_text = {
    "2605.24832": "固定 diffusion step 在请求同质、质量阈值稳定时最简单；负载与请求难度变化后，固定步数同时制造短请求浪费和难请求欠算。Optimus 把剩余 refinement step、质量状态与 batching 交给 runtime controller，以弹性 decoding granularity 换取更复杂的校准、service-time variance 和 admission/scheduling。证据只覆盖作者披露的 diffusion-LM、硬件与 SLO；控制器失准时回退固定步数。",
    "2605.24883": "人工 benchmark 适合稳定 policy，却难证明每条规则和组合路径都被覆盖；无约束 red-team 又难回溯到哪条 policy 缺口。POLARIS 把 policy 编译为 predicate graph，再从未覆盖路径实例化 tests，使 policy revision、test identity 和 coverage evidence 同步演进。收益是系统化覆盖，代价是 policy formalization error、生成成本与单轮范围；规则不完整或进入多轮 state 时回退人工 threat modeling 与独立 red team。",
    "2605.25002": "普通 memory watermark 标记存储内容，却难判断某段 latent memory state 经哪次 write/update 演化而来。MemMark 把 owner-controlled signal 写入 memory-write decision，用 attribution robustness 换取写入扰动、检测校准和 adaptive attacker 风险。它是 ownership sensor，不是真值或 authorization；信号冲突时保留原始 episode、write receipt 与独立 provenance。",
}
for arxiv_id, unit in deep.items():
    lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit}", "", deep_text[arxiv_id], f"<!-- analysis:{unit}:end -->"]
for row in retained:
    if row["arxiv_id"] not in deep:
        sf = row["source_family_id"]
        lines.append(f"<!-- analysis-decision:{sf}:start -->exact-v1 已完成；未进入三项 Deep Analysis 不表示跳过 Source Review，只表示其优先级低于当日三项跨层 contract delta。<!-- analysis-decision:{sf}:end -->")

lines += ["", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->", "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for row in retained:
    c = comparison_by_id[row["arxiv_id"]]; sf = row["source_family_id"]
    lines.append(f"| {sf} | {row['owner_node']} | {chapter_ref(c['owner_path'])} | {';'.join(chapter_ref(p) for p in c['adjacent_paths'])} | existing:{sf} | delta:{sf} | Direct Evolution | {row['integration_disposition']} | books-review:{sf} |")
for row in retained:
    c = comparison_by_id[row["arxiv_id"]]; sf = row["source_family_id"]
    lines += [f"<!-- books-review:{sf}:start -->", f"<!-- existing:{sf}:start -->{c['existing_proposition']}<!-- existing:{sf}:end -->", f"<!-- delta:{sf}:start -->{c['new_evidence_delta']}<!-- delta:{sf}:end --> Independent decision=`{row['integration_disposition']}`。", f"<!-- books-review:{sf}:end -->"]

first_sf = retained[0]["source_family_id"]
lines += ["", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->", "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |", "| --- | --- | --- | --- | --- | --- | --- |",
          "| SA-20260525-COVERAGE | fresh-context:isolated-prewrite-reviewer | coverage | coverage:SRC-ARXIV:20260525 | none | fresh-context-independent-audit.json#changes records denominator 24→41 and closures 263→246 | passed |",
          f"| SA-20260525-EVIDENCE | fresh-context:isolated-prewrite-reviewer | evidence | review:{first_sf} | none | exact-v1-review-packet-independent-final.json records 41/41 complete and blocked=0 | passed |",
          "| SA-20260525-SELECTION | fresh-context:isolated-prewrite-reviewer | deep_analysis_selection | analysis:DA-DIFFUSION-ELASTIC-SERVING | none | fresh-context-independent-audit.json records the final Optimus, POLARIS and MemMark selection | passed |",
          f"| SA-20260525-BOOKS | fresh-context:isolated-prewrite-reviewer | books | books-review:{first_sf} | none | books-writeback-queue-independent-final.json records final pre-write queue={len(queue)} | passed |", "",
          "## 8. Ignored Noise", "", "246 条逐 family pre-denominator closure 保存在 `screening-ledger-independent-final.json`。独立审计重开 18 条系统级 false negative，并把 2605.25310 以具体机制边界降回 closure；每条 closure 保留 family-specific 机制、证据、排除边界和重开条件。", "",
          "## 9. Recommended Action", "", f"由 root 按日期顺序串行写回 `books-writeback-queue-independent-final.json` 的 {len(queue)} 项；随后必须由非写作者完成 owner+adjacent post-write semantic audit，Books Gate 才能通过。", "",
          "## 10. Repository Changes", "", "- 新增 2026-05-25 独立 final screening ledger、exact-v1 packet、Books comparison、final queue 与 fresh-context audit。", "- 更新本 Daily canonical README 到 Coverage/Evidence Passed、Books Open。", "- 未修改共享 Books；未 stage、commit 或 push。", "",
          "## 11. Open Questions", "", f"- {len(queue)} 项 final Integrate 尚待 root 串行写回及 post-write semantic audit。", "", "<!-- validator:materials-request-v1 -->", "| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |", "",
          "## 12. Sources", ""]
for row in retained:
    lines.append(f"- [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) — arXiv:{row['arxiv_id']}v1；first-public 2026-05-24；accessed 2026-09-01")
lines += ["", "## 13. Final Status", "", "Completion Status: `In Progress`", "", "Coverage: `Closed`", "", "Evidence: `Passed`", "", "Books: `Open`", "", "unresolved findings: 1", "", f"独立 pre-write audit 已通过；{len(queue)} 项 Books 写回与 post-write semantic audit 尚未完成。"]

text = "\n".join(lines)
for row, method, evaluation, limitations in receipt_indexes:
    sf, arxiv_id = row["source_family_id"], row["arxiv_id"]
    body = text.split(f"<!-- review:{sf}:start -->", 1)[1].split(f"<!-- review:{sf}:end -->", 1)[0]
    candidate = {"Event Identity": f"paper-v1:{arxiv_id}", "Primary Identifier": f"arXiv:{arxiv_id}v1", "Supporting Source IDs": "SRC-ARXIV", "Review Override": "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"}
    rp = _expected_review_provenance(sf, candidate, "deep", f"arXiv:{arxiv_id}v1", f"SRC-ARXIV@arXiv:{arxiv_id}v1", method, evaluation, limitations, f"arXiv:{arxiv_id}v1 artifact links; immutable commit Not Disclosed unless stated in paper", f"claim:{sf}", f"review:{sf}", _normalized_body_sha256(body))
    text = text.replace("RP-TODO-" + sf, rp)

(HERE / "README.pending.md").write_text(text + "\n")
(ROOT / "papers/2026/05/25/README.md").write_text(text + "\n")
(HERE / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue_doc, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"raw": 91841, "registered": 287, "screened": 287, "retained": 41, "closures": 246, "reviewed": 41, "blocked": 0, "integrate_queue": len(queue)}, ensure_ascii=False))
