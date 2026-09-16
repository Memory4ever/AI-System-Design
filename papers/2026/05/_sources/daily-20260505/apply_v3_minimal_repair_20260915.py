#!/usr/bin/env python3
"""Apply the bounded 2026-05-05 false-negative repair identified by fresh review.

This script deliberately touches only seven reopened source families and five
family-specific pre-denominator closure reasons. It never writes Books.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER_PATH = HERE / "V3_CANONICAL_LEDGER.json"
EVIDENCE_PATH = HERE / "V3_EVIDENCE_REVIEWS.json"
QUEUE_PATH = HERE / "books-writeback-queue.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def score(design: int, reach: int, durability: int, design_reason: str, owner: str) -> dict:
    return {
        "design_delta": design,
        "system_reach": reach,
        "durability": durability,
        "total": design + reach + durability,
        "rationale": {
            "design_delta": design_reason,
            "system_reach": f"影响范围按 canonical owner `{owner}` 与 exact-v1 实际 workload 校准；不因标题相关性加分。",
            "durability": "只把可迁移的状态、控制或验收边界计入长期性；作者 benchmark 与单一 workload 不外推。",
        },
    }


REOPEN = {
    "2605.01208": {
        "title": "Faithful Mobile GUI Agents with Guided Advantage Estimator",
        "owner": "TRAIN-GRPO", "chapter": 33,
        "path": "books/part-04-training-system/33-grpo.md",
        "score": score(3, 3, 2, "在稀疏 GUI reward 的全对/全错 group 中，不再只丢弃零优势样本，而是以固定 reward anchors 改写归一化统计并恢复有符号 group-level update。", "TRAIN-GRPO"),
        "method_locators": ["§3.3 Advantage Collapse", "§4.2.1 Reward Function", "§4.2.2 Guided Advantage Estimator"],
        "method_evidence": "标准 group normalization 在全零或全一 reward group 中产生近零优势。GuAE 只把 reward 边界 0/1 加入均值和方差统计，不把 anchors 当作 rollout；真实样本因而在全零组得到同号负优势、在全一组得到同号正优势，再由 variance-adaptive tempering 调整尺度。SFT 阶段另以证据缺失或冲突样本训练 abstention。",
        "evaluation_locators": ["§5 Experimental Setup", "§5.2 Main Results", "§5.3 Comparison with Other Advantage Estimators"],
        "evaluation_evidence": "作者在 Qwen3-VL-8B-Instruct、LLaMA-Factory/EasyR1 与 General/Trap GUI 数据切片上报告 Stage I/II 结果；摘要中的 Trap SR 13.88%→80.21% 只属于该模型、奖励与扰动合同。与 DAPO、GSPO、REINFORCE++ 的比较不能外推为一般 GRPO 优势。",
        "limitations_locators": ["§5.4 Ablation Studies", "Appendix: hyperparameter and safety discussion"],
        "limitations_evidence": "锚点要求已知且有意义的 reward 边界；它只恢复 group-level 同号更新，不能创造相同 rollout 间的排序信息。规则式 thought-action reward、group size、tempering 超参和 GUI schema 都可能引入偏差；更强正向更新也可能把全组共同错误放大。",
        "mechanism": "以 reward-bound anchors 和方差自适应 tempering 在 collapsed rollout group 中恢复有符号 advantage",
        "boundary": "exact-v1 支持 Qwen3-VL-8B 的作者 GUI/RFT 设置，不证明 anchor-normalized advantage 对其他 reward 范围、模型、环境或 production SLO 普遍有效；它也不证明同 reward rollout 之间存在可识别排序。",
        "decision": "Integrate Proposed — root writeback and independent review required",
        "locator": "books/part-04-training-system/33-grpo.md — `DAPO 把朴素 GRPO 的运行失败拆成四处修补` 中 Dynamic Sampling 之后、`DAPO 之后，各分支继续修改不同约束` 之前",
        "proposition": "现有正文用 Dynamic Sampling 补采并过滤全对、全错的零优势 group，以 mixed-outcome membership 恢复相对排序。",
        "comparison": "现有命题只覆盖“换 group membership”这条路径；未覆盖在无法或不宜补采时，通过固定 reward 边界改变 estimator 统计、保留 collapsed group 并接受有偏同号更新的替代分支。",
        "delta": "在 Dynamic Sampling 之后增加并列分支：当 reward 有稳定边界且重采样昂贵时，可仅向归一化统计加入固定 anchors，使全错/全对组的真实样本获得同号更新；variance tempering 再限制不同离散度 group 的尺度。该机制改变 estimator 语义而不产生组内排序，收益是保留稀疏 reward group，代价是边界依赖、bias、超参敏感与共同错误放大。reward 稠密、边界不可信或补采便宜时，继续使用普通 GRPO/Dynamic Sampling。",
        "handoff": "Ch33 拥有 advantage estimator；GUI grounding、abstention 与动作证据仍由 Agent/Embodied 章节承载。",
    },
    "2605.01477": {
        "title": "Action Agent: Agentic Video Generation Meets Flow-Constrained Diffusion",
        "owner": "MULTIMODAL-EMBODIED-VLA", "chapter": 26,
        "path": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "score": score(3, 3, 2, "把语言目标先变成可迭代修订的 goal video proposal，再由独立低层 controller 消费当前观测执行动作，形成明确的高低层控制分工。", "MULTIMODAL-EMBODIED-VLA"),
        "method_locators": ["§III Action Agent", "§III-A Agentic Goal-Video Generation", "§III-B Flow-Constrained Low-Level Controller"],
        "method_evidence": "系统先由高层生成器把语言目标和初始图像变成 goal video，再由低层 flow-constrained controller 结合 goal video、当前观测和语言输出动作；生成阶段还使用 LLM 编排 prompt、video 与 evaluator 的迭代修订。",
        "evaluation_locators": ["§IV Experiments", "Simulation and real-world navigation results", "Ablation studies"],
        "evaluation_evidence": "评测覆盖 50 个室内仿真导航任务与 G1、drone、wheeled embodiments；真实 G1 只有 17 次 open-loop 试验并报告 11/17 成功。视频质量阈值由模型 evaluator 给出，不是物理成功或安全证明。",
        "limitations_locators": ["Failure-case analysis", "§V Limitations and Future Work"],
        "limitations_evidence": "作者明确列出尺度歧义、轨迹漂移和碰撞，并把硬件 closed-loop 作为后续工作；5–15 秒 clip、有限场景与 open-loop 证据不能证明真实闭环安全。",
        "mechanism": "以可修订 goal video 作为高层 proposal，并由独立 controller 基于当前观测执行动作",
        "boundary": "exact-v1 只证明作者仿真与有限 open-loop G1 设置；goal-video evaluator 不拥有环境 transition truth，且不能把视觉质量分数当作 physical success、closed-loop robustness 或 safety guarantee。",
        "decision": "No Change — Existing Coverage (author proposition comparison; independent review required)",
        "locator": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md — `High-level Plan 与 Low-level Control 必须分层`、`State ownership 与 freshness`",
        "proposition": "高层 reasoning/imagination 只形成 action proposal；低层 controller、fresh observation 与 safety envelope 拥有执行、纠错和环境 transition 的提交边界。",
        "comparison": "该 two-stage navigation system 是现有高低层分工的具体案例；真实证据仍是 open-loop，且其尺度、漂移、碰撞失败恰好落在正文既有 freshness、calibration 与 closed-loop 边界内，没有改变长期命题。",
    },
    "2605.01766": {
        "title": "Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time",
        "owner": "INFER-KV-CACHE", "chapter": 45,
        "path": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md",
        "score": score(3, 2, 2, "在每个 decode step 对 K/V state 求梯度并施加受 KL 约束的分支扰动，使模态 token 的 relevance proposal 增强。", "INFER-KV-CACHE"),
        "method_locators": ["§3.2 Layer-wise Relevance Propagation", "§3.3 Learning Inference-time Modality Enhancement"],
        "method_evidence": "LIME 在每个生成步优化 K/V perturbation，使 LRP relevance 向视觉或音频 token 移动，并用 KL regularizer 约束下一 token distribution 偏移；模型参数保持冻结。",
        "evaluation_locators": ["§4 Experiments", "§4.3 Ablation Studies", "§4.4 Efficiency Analysis"],
        "evaluation_evidence": "作者在 POPE/CHAIR 视觉任务和 Audio Hallucination QA/AIR-Bench 音频任务、所列 MLLM 上报告改善；K-only/V-only/KV 与 KL 消融属于这些模型与 evaluator。每 token 梯度更新增加 latency，作者把它定位于 offline/high-accuracy 场景。",
        "limitations_locators": ["LRP implementation assumptions", "§4.4 Efficiency Analysis"],
        "limitations_evidence": "LRP 对 normalization 使用 identity approximation；relevance 是 attribution proxy 而不是因果 grounding 或事实正确性。逐 token 反向优化增加延迟，分布约束也不能排除 latent-state hacking。",
        "mechanism": "以逐 token 梯度更新直接修改 K/V 分支状态，并用 KL 约束分布漂移",
        "boundary": "exact-v1 只支持作者视觉/音频模型、LRP approximation 和离线评测；不证明 relevance 是事实概率、KV 扰动无副作用或该路径满足在线 serving latency。",
        "decision": "No Change — Existing Coverage (author proposition comparison; independent review required)",
        "locator": "books/part-05-inference-system/45-why-kv-cache-speeds-up.md — `KV 从生成私有状态演进为受约束的下游读出接口`",
        "proposition": "直接修改 KV 的 inference-time 分支属于 Experimental mutable state，必须使用 versioned Copy-on-Write branch、隔离污染并由独立 outcome verifier 决定是否提交。",
        "comparison": "LIME 提供 multimodal relevance objective、KL 约束和逐 token 开销案例，但没有改变既有 KV mutation 的身份、隔离、验证和 rollback 合同；LRP relevance 也不能提升为 commit authority。",
    },
    "2605.01913": {
        "title": "RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs",
        "owner": "PLATFORM-SECURITY", "chapter": 72,
        "path": "books/part-06-ai-infrastructure/72-security.md",
        "score": score(3, 2, 2, "把 fine-tuning update 在已识别 refusal subspace 上的投影作为可惩罚训练状态，以限制 safety-mediating representation drift。", "PLATFORM-SECURITY"),
        "method_locators": ["§2.1 Refusal Geometry", "§3.3 Geometry-Preservation Penalty", "§3.4 Training Objective"],
        "method_evidence": "方法从冻结 base model 提取 refusal cone/reference geometry，比较适配前后漂移，并在训练时惩罚 intervention update 向 refusal subspace 的投影；base 参数冻结，只优化 intervention 参数。",
        "evaluation_locators": ["§4 Experimental Setup", "§5 Main Results", "§5.3 Benign Fine-Tuning", "§5.4 Ablations"],
        "evaluation_evidence": "作者测试 Gemma 2、Qwen2.5 与 Llama 3.1 若干规模，在 AdvBench、DirectHarm4、JailbreakBench 与 GSM8K/OpenOrca/ARC 上比较安全和 utility。10 条合成 harmful examples 是受控 stress test，不是现实训练分布；benign GSM8K 结果也只覆盖文中模型。",
        "limitations_locators": ["Controlled harmful-fine-tuning setup", "Geometry and λ ablations", "Threat-model boundary"],
        "limitations_evidence": "拒答几何由内部层、样本和提取方式定义，不能视为跨模型普适 safety truth；更强 penalty 降低 ASR 同时会约束 utility。白盒访问、layer choice、adaptive attack 与分布外行为均未被完整证明。",
        "mechanism": "将 safety-relevant representation drift 转化为 fine-tuning update 的显式约束与发布传感器",
        "boundary": "exact-v1 支持所列开源模型、benchmark 与受控 fine-tuning stress；不证明 refusal geometry 是普适因果机制，也不取代行为 red-team、adaptive attack、utility regression 或独立 release gate。",
        "decision": "Integrate Proposed — root writeback and independent review required",
        "locator": "books/part-06-ai-infrastructure/72-security.md — `模型内部路由、训练数据与 Weight Repair 都进入攻击面` 中 fine-tuning safety regression 段落之后",
        "proposition": "现有正文要求以 sample-level dynamics 发现 fine-tuning 安全退化，并将 risk score 保持为传感器；阈值失效时仍执行完整 safety regression。",
        "comparison": "现有命题覆盖样本风险与事后 weight repair，却未说明 downstream update 即使保持 task utility，也可能沿 safety-mediating subspace 漂移，以及如何在训练时限制该投影。",
        "delta": "在训练安全回归中增加 representation-geometry 分支：把 base-aligned refusal subspace 作为版本化 reference sensor，训练 owner 记录 update 在该 subspace 上的投影并可施加惩罚；它只能限制已识别方向，不能签发安全结论。收益是提前暴露/抑制下游适配导致的安全漂移，代价是白盒访问、layer/reference 选择、utility 约束和错误保留。geometry 不稳定、模型不可见或任务必须使用重叠方向时，回退冻结/adapter 隔离、较小 update 与完整行为安全回归。",
        "handoff": "Ch72 拥有安全传感器和 release gate；训练章节只说明 update artifact/optimizer identity，不复制安全机理。",
    },
    "2605.01959": {
        "title": "Flexi-LoRA with Input-Adaptive Ranks: Efficient Finetuning for Speech and Reasoning Tasks",
        "owner": "TRAIN-LORA", "chapter": 30,
        "path": "books/part-04-training-system/30-lora.md",
        "score": score(3, 2, 2, "把固定 LoRA rank 变为由输入特征路由的离散 capacity state，并要求训练与推理使用同一 rank policy。", "TRAIN-LORA"),
        "method_locators": ["§3 Flexi-LoRA", "Difficulty-aware rank router", "Rank slicing and rank-specific scaling"],
        "method_evidence": "router 从 mean-pooled input embeddings 预测 rank；训练标签由任务 difficulty metric 构造并用加噪交叉熵学习。所选 rank 在所有 transformer layers 一致切取 LoRA 因子的前 r 个维度，并使用 rank-specific alpha；训练与推理均运行同一 router。",
        "evaluation_locators": ["§4 Experimental Setup", "§5 Results", "Ablation studies"],
        "evaluation_evidence": "作者在 Llama 3.2 1B/3B、Whisper 与 QA、数学、语音任务上报告 parameter/quality 结果。论文没有给出生产 batch、kernel shape、端到端 latency、hardware SLO 或动态 rank serving 成本。",
        "limitations_locators": ["Router and difficulty-label design", "Future work: layer-wise ranks", "Undisclosed serving cost"],
        "limitations_evidence": "同一 sample rank 施加到全部层，layer-specific allocation 尚未处理；difficulty labels 依赖任务 metric，router 错误会错配 capacity。动态 per-sample rank 可能碎片化 batching/compiled shape，论文没有证明实际延迟收益。",
        "mechanism": "以输入条件 router 在训练和推理阶段选择 LoRA rank，令 adapter capacity 成为运行时状态",
        "boundary": "exact-v1 只支持作者 QA/数学/语音任务与小规模 Llama/Whisper；trainable-parameter 减少不等于 FLOPs、latency 或 fleet cost 改善，也不证明 rank policy 跨任务可迁移。",
        "decision": "Integrate Proposed — root writeback and independent review required",
        "locator": "books/part-04-training-system/30-lora.md — `Rank 与 target modules 决定更新空间` 之后、`Rank Threshold` 分支之前",
        "proposition": "现有正文把 rank、target modules、base revision 与预算冻结为 adapter update-space identity，并用 rank sweep 选择静态容量。",
        "comparison": "现有命题没有覆盖 sample-conditioned rank router，也未把训练—推理 rank policy、difficulty-label provenance 和动态 shape serving 成本纳入 adapter identity。",
        "delta": "在静态 rank 之后增加条件容量分支：router 只能从版本化 input feature 提出允许 rank，训练与推理必须复用同一 policy；adapter identity 同时绑定 router、difficulty-label rule、rank set、alpha 与 target modules。它用按样本分配容量换来 router 误判、标签循环、dynamic-shape/batching 碎片与更大发布矩阵。任务同质、kernel 需要静态 shape、latency 未证或 router 不稳定时，固定 rank 仍是首选 fallback。",
        "handoff": "Ch30 拥有 adapter capacity identity；serving 的 batching/shape 成本只向 Inference 章节短交接。",
    },
    "2605.02323": {
        "title": "When Attention Collapses: Residual Evidence Modeling for Compositional Inference",
        "owner": "MULTIMODAL-REPRESENTATION", "chapter": 23,
        "path": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
        "score": score(3, 2, 2, "为顺序 decomposition slots 增加可衰减的 unexplained-evidence state，使后一 slot 读取前一 slot 尚未解释的输入，而非重复竞争同一 attention mass。", "MULTIMODAL-REPRESENTATION"),
        "method_locators": ["§2.2 Attention Collapse under Additive Superposition", "§2.3 Residual Evidence Modeling"],
        "method_evidence": "并行或仅顺序化的 attention slots 在 additive superposition 中会受共享梯度驱动而 collapse。方法为每个 token 保存 unexplained evidence e_l；每个 slot 读取当前 residual，通过 log-e bias 与 K/V scaling 调整 attention，并在 slot 输出后执行 multiplicative depletion，让下一 slot 消费更新后的残余状态。",
        "evaluation_locators": ["§3 Experiments", "FUSS audio separation", "LISA signal decomposition", "Ablations"],
        "evaluation_evidence": "作者在 synthetic mixtures、4 秒 FUSS audio（32 ChunkFFT、5 slots）与 LISA decomposition 上报告 slot collapse/分离改善；quadratic depletion 与 loss-only regularization 在作者设置中不足。",
        "limitations_locators": ["§4 Discussion", "Single-granularity and depletion-function limitations"],
        "limitations_evidence": "residual state 是模型内部的解释预算，不是事实证据。顺序更新引入 ordering sensitivity、误差累积和额外控制依赖；单一 granularity、depletion 形式与超参是 task-dependent，跨文本/通用 MLLM 的类比未被实验直接证明。",
        "mechanism": "用逐 slot residual-evidence state 记录尚未解释的输入容量，抑制 additive mixture 中的重复 attention allocation",
        "boundary": "exact-v1 仅支持 synthetic、FUSS audio 与 LISA workload；不证明该机制适用于通用 LLM attention，也不允许把 learned evidence depletion 当作 factual provenance 或 correctness signal。",
        "decision": "Integrate Proposed — root writeback and independent review required",
        "locator": "books/part-03-multimodal-world-models/23-multimodal-representation.md — `Fusion：在哪里让模态相遇` 之后、`固定预算要先分配信息责任，再选择具体 Token` 之前",
        "proposition": "现有正文比较 early/late/cross/shared fusion，并要求先分配固定 token budget 的信息责任，再选择具体 token。",
        "comparison": "现有命题仍把多 slot attention 看作一次或彼此独立的预算分配；没有表示“哪些输入成分已被前一 slot 解释”的可变状态，因此未覆盖 additive superposition 下重复选择同一成分的 failure mode。",
        "delta": "增加 residual-evidence 分支：当多个并行 slot 会在 additive mixture 上重复解释同一成分时，为每个 token 保存尚未解释的容量；slot 输出后才提交 bounded depletion，下一 slot 读取新 revision。收益是非冗余分解，代价是顺序化、ordering sensitivity、乘性误差和 task-dependent depletion。component 可分、冗余可接受或时延优先时，普通 parallel/cross attention 仍更合适；该 state 只表示 representation allocation，不是外部事实证据。",
        "handoff": "Ch23 拥有 representation allocation state；通用 attention 数学仍在 Ch14，不能把该受限案例写成 Transformer attention 的普遍结论。",
    },
    "2605.02641": {
        "title": "Mamoda2.5: Enhancing Unified Multimodal Model with DiT-MoE",
        "owner": "MULTIMODAL-GENERATIVE-PARADIGMS", "chapter": 24,
        "path": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md",
        "score": score(3, 3, 2, "在统一 AR-Diffusion 模型中组合 DiT-MoE upcycling、共享/路由专家与 few-step distillation，形成条件计算和迭代生成的受限组合实例。", "MULTIMODAL-GENERATIVE-PARADIGMS"),
        "method_locators": ["§2.2 DiT-MoE", "Dense-to-MoE upcycling", "Distillation and reinforcement learning"],
        "method_evidence": "DiT-MoE 使用 128 个 routed experts、top-8 与 1 个 shared expert，sigmoid affinity 加 expert bias 只影响选择。dense-to-MoE 通过随机 neuron sampling 初始化 experts、迁移 attention 并随机初始化 router；后续把 30-step CFG teacher 蒸馏到 4-step CFG-free student。",
        "evaluation_locators": ["§3 Experiments", "MoE ablations", "Few-step generation evaluation"],
        "evaluation_evidence": "MoE 消融在匹配 activated parameters、内部 image data 与 64 xPU 设置中进行，T2V 部分运行提前终止。作者报告约 15× 属于 forward-step 算法计数与其配置，不是完整 hardware/SLO serving speedup。",
        "limitations_locators": ["Ablation configuration", "Internal-data/evaluator boundary", "Future work"],
        "limitations_evidence": "内部数据、未完整披露 evaluator 与 xPU 环境限制复现；few-step quality、router load、batch/concurrency、精度和 production latency 没有形成通用合同。统一模型中的组合收益不能拆成每个组件的普适因果结论。",
        "mechanism": "在统一 AR-Diffusion workload 中组合 DiT-MoE 条件计算、dense upcycling 与 few-step student",
        "boundary": "exact-v1 支持作者内部数据、xPU、模型和 evaluator；不证明 DiT-MoE 或 4-step student 对所有文本/图像/视频 workload 更优，约 15× 不是端到端生产加速结论。",
        "decision": "No Change — Existing Coverage (author proposition comparison; independent review required)",
        "locator": "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md — `Few-step Distillation 要在 Student 实际访问的状态上验收`；MoE 机制 handoff 到 Ch21",
        "proposition": "Ch24 已要求 few-step student 在其实际访问状态上验收质量/稳定性，条件计算只改变每步计算预算；Ch21 已拥有 router、capacity、load balance 与 dense-to-MoE 演进。",
        "comparison": "Mamoda2.5 是两条既有机制的具体组合和作者案例；未披露的端到端 SLO 与内部 evaluator 不足以改变 few-step commit、MoE owner 或训练—推理一致性命题。",
    },
}

CLOSURE_REASONS = {
    "2605.00915": "SSMProbe 改变的是冻结视觉表示的 probe/readout 顺序，不改变被测模型的训练、推理或 representation owner。",
    "2605.01078": "SONAR 是 prompt sanitization 的一个 NLI-graph 实现；题摘没有证明该 heuristic 能替代 trust boundary、reference monitor 或 post-action validation。",
    "2605.01462": "LocalAlign 是 near-target adversarial-example 的训练分支；它没有改变 trusted/untrusted data ownership 或生产 admission contract。",
    "2605.01853": "StALT 是 hidden-state trajectory probe；题摘未建立 release-grade correctness calibration、可移植阈值或执行控制权。",
    "2605.02421": "AOCI 是 code-repository 的特定索引协议与 benchmark；增量仍可由现有 context/RAG artifact identity 承载，不产生新的通用 owner。",
}


ledger = load(LEDGER_PATH)
evidence = load(EVIDENCE_PATH)
queue = load(QUEUE_PATH)
entries = {item["arxiv_id"]: item for item in ledger["entries"]}
reviews = {item["arxiv_id"]: item for item in evidence["reviews"]}

assert set(REOPEN).isdisjoint(reviews), "bounded repair already partly applied"
for arxiv_id in REOPEN:
    assert entries[arxiv_id]["semantic_decision"] == "pre_denominator_closure_reviewed"
for arxiv_id in CLOSURE_REASONS:
    assert entries[arxiv_id]["semantic_decision"] == "pre_denominator_closure_reviewed"

for arxiv_id, reason in CLOSURE_REASONS.items():
    entries[arxiv_id]["decision_reason"] = reason
    entries[arxiv_id]["internal_design_delta_challenge"] = {
        "reopened_by": "V3_INDEPENDENT_FINAL_REVIEW_20260914.md",
        "result": "pre_denominator_closure_upheld",
        "reason": reason,
    }

for arxiv_id, spec in REOPEN.items():
    entry = entries[arxiv_id]
    entry.update({
        "semantic_decision": "semantic_reviewed_retain_frozen",
        "decision_reason": f"独立 closure 反查确认题摘存在长期设计命题；已重开并完成 exact-v1 深审：{spec['mechanism']}。",
        "exact_v1_status": "deep_complete_author",
        "score_v2": spec["score"],
        "owner": spec["owner"],
        "books_decision": spec["decision"],
        "internal_design_delta_challenge": {
            "old_system_constraint": spec["proposition"],
            "changed_state_data_control_or_eval_contract": spec["mechanism"],
            "long_term_design_choice": spec["comparison"],
        },
    })
    review = {
        "arxiv_id": arxiv_id,
        "source_family_id": entry["source_family_id"],
        "title": spec["title"],
        "exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1",
        "local_exact_v1_html": None,
        "review_status": "deep_complete_author",
        "score_v2": spec["score"],
        "method_locators": spec["method_locators"],
        "method_evidence": spec["method_evidence"],
        "evaluation_locators": spec["evaluation_locators"],
        "evaluation_evidence": spec["evaluation_evidence"],
        "limitations_locators": spec["limitations_locators"],
        "limitations_evidence": spec["limitations_evidence"],
        "mechanism_claim": spec["mechanism"],
        "claim_boundary": spec["boundary"],
        "owner": spec["owner"],
        "chapter": spec["chapter"],
        "chapter_path": spec["path"],
        "existing_marker_hits": [],
        "books_decision": spec["decision"],
        "existing_coverage_locator": spec["locator"],
        "existing_coverage_proposition": spec["proposition"],
        "existing_coverage_comparison": spec["comparison"],
    }
    evidence["reviews"].append(review)

    if spec["decision"].startswith("Integrate Proposed"):
        chapter_path = ROOT / spec["path"]
        chapter_hash = hashlib.sha256(chapter_path.read_bytes()).hexdigest()
        queue["items"].append({
            "date": "2026-05-05",
            "source_family_id": entry["source_family_id"],
            "primary_identifier": f"arXiv:{arxiv_id}v1",
            "primary_source": f"https://arxiv.org/html/{arxiv_id}v1",
            "stable_node_id": spec["owner"],
            "target_chapter_path": spec["path"],
            "current_chapter_sha256": chapter_hash,
            "current_chapter_locator": spec["locator"],
            "current_content_finding": spec["comparison"],
            "new_delta_after_compare": spec["delta"],
            "method_evidence": spec["method_evidence"],
            "evaluation_evidence": spec["evaluation_evidence"],
            "evidence_boundary": spec["boundary"],
            "adjacent_handoff": spec["handoff"],
            "required_writeback": "Root 应把语义增量嵌入既有演进链，保留旧方案成立条件、trade-off、failure mode、fallback 与证据边界；不得写成论文摘要或章末孤立条目。",
            "comparison_status": "author_proposition_comparison_complete_root_writeback_pending",
            "status": "proposed_root_writeback_pending",
            "post_write_chapter_sha256": None,
            "semantic_body_marker_hits": 0,
            "daily_trace_marker_hits": 0,
        })

ledger["counts"] = {
    "pre_denominator_closure_reviewed": sum(item["semantic_decision"] == "pre_denominator_closure_reviewed" for item in ledger["entries"]),
    "semantic_reviewed_retain_frozen": sum(item["semantic_decision"] == "semantic_reviewed_retain_frozen" for item in ledger["entries"]),
}
assert ledger["raw_identity_count"] == ledger["screened_count"] == sum(ledger["counts"].values()) == 1058
ledger["status"] = "minimal_false_negative_repair_complete_root_writeback_and_independent_review_pending"
ledger["candidate_denominator_frozen"] = False
ledger["books_write_permitted"] = False
ledger["independent_review_required"] = True

evidence["reviews"] = sorted(evidence["reviews"], key=lambda item: item["arxiv_id"])
assert len({item["arxiv_id"] for item in evidence["reviews"]}) == len(evidence["reviews"])
evidence["candidate_count"] = len(evidence["reviews"])
evidence["blocked"] = sum(item["review_status"] == "blocked_exact_v1_html" for item in evidence["reviews"])
evidence["deep_complete"] = sum(item["review_status"] == "deep_complete_author" for item in evidence["reviews"])
evidence["standard_complete"] = sum(item["review_status"] == "standard_complete_author" for item in evidence["reviews"])
evidence["review_complete"] = evidence["deep_complete"] + evidence["standard_complete"]
evidence["books_integrate_applied"] = sum(item["books_decision"].startswith("Integrate Applied") for item in evidence["reviews"])
evidence["books_integrate_proposed"] = sum(item["books_decision"].startswith("Integrate Proposed") for item in evidence["reviews"])
evidence["books_no_change"] = sum(item["books_decision"].startswith("No Change") for item in evidence["reviews"])
assert evidence["candidate_count"] == 145
assert evidence["review_complete"] + evidence["blocked"] == evidence["candidate_count"]
assert evidence["books_integrate_applied"] + evidence["books_integrate_proposed"] + evidence["books_no_change"] + evidence["blocked"] == evidence["candidate_count"]
evidence["status"] = "minimal_false_negative_repair_complete_root_writeback_and_independent_review_pending"

assert len({item["source_family_id"] for item in queue["items"]}) == len(queue["items"])
dump(LEDGER_PATH, ledger)
dump(EVIDENCE_PATH, evidence)
dump(QUEUE_PATH, queue)

# Regenerate proposition-level No Change projection.
no_change = [r for r in evidence["reviews"] if r["books_decision"].startswith("No Change")]
comparison = [
    "# 2026-05-05 V3 Proposition-level Books Comparison", "",
    "本表从当前 Evidence Review 数组生成。每一行都比较一个可访问候选与目标章节的现有具体命题；它不是以 owner 名称替代 Books Review。", "",
    f"**No Change 数量：** {len(no_change)}", "",
    "| Primary | Source Family | 现有具体命题定位 | 逐命题比较 |",
    "| --- | --- | --- | --- |",
]
for review in no_change:
    def cell(value: str) -> str:
        return " ".join(value.split()).replace("|", "\\|")
    comparison.append(f"| `{review['arxiv_id']}v1` | `{review['source_family_id']}` | {cell(review['existing_coverage_locator'])} | {cell(review['existing_coverage_comparison'])} |")
(HERE / "V3_PROPOSITION_BOOKS_COMPARISON.md").write_text("\n".join(comparison) + "\n")

# Append a readable bounded repair section without rewriting earlier audited queue history.
queue_md = (HERE / "V3_BOOKS_REVIEW_QUEUE.md").read_text().rstrip()
marker = "## 2026-09-15 最小假阴性修复：root 待写回"
assert marker not in queue_md
queue_md += "\n\n" + marker + "\n\n"
queue_md += "以下四项已完成作者侧 exact-v1、评分和逐命题 Books 比较；尚未写入共享 Books，必须由 root 按日期序列写回后再交给新的非作者 reviewer。\n\n"
for arxiv_id in ["2605.01208", "2605.01913", "2605.01959", "2605.02323"]:
    spec = REOPEN[arxiv_id]
    queue_md += f"### `{spec['owner']}` — `{arxiv_id}v1`\n\n"
    queue_md += f"**插入位置：** {spec['locator']}\n\n"
    queue_md += f"**现有命题差异：** {spec['comparison']}\n\n"
    queue_md += f"**可写回语义增量：** {spec['delta']}\n\n"
    queue_md += f"**证据边界：** {spec['boundary']}\n\n"
    queue_md += f"**相邻交接：** {spec['handoff']}\n\n"
(HERE / "V3_BOOKS_REVIEW_QUEUE.md").write_text(queue_md)

recert = f"""# 2026-05-05 V3 最小修复作者侧再认证 — 2026-09-15

## 范围

仅处理 `V3_INDEPENDENT_FINAL_REVIEW_20260914.md` 指定的 7 个 false negative 与 5 条 family-specific closure；未扩日期、未重扫来源、未重开已通过 strata。

## 账目

- raw identities：1058；守恒为 145 retained + 913 pre-denominator closure。
- Evidence：143 可访问并完成作者审阅（74 deep + 69 standard）+ 2 blocked。
- Books：30 Applied（既有）+ 4 Proposed（root 待写回）+ 109 No Change + 2 Blocked。
- 7 个重开项：4 Proposed（`2605.01208`、`2605.01913`、`2605.01959`、`2605.02323`）；3 No Change（`2605.01477`、`2605.01766`、`2605.02641`）。
- 5 个 closure 已替换为各 family 的具体关闭理由：`2605.00915`、`2605.01078`、`2605.01462`、`2605.01853`、`2605.02421`。

## Exact-v1 与边界

7 项均通过官方 arXiv exact-v1 HTML 完成 Method、evaluation、ablation/limitation 与 Books 命题比较；本地缓存因连接重置未形成有效文件，canonical review 保留 exact-v1 URL 并将 local cache 写为 `null`，不把缓存缺失误标为正文受阻。既有 `2605.02206`、`2605.02375` 仍为隔离的 `Blocked / Unverified`，本轮未擅自重判。

## Gate

作者侧最小修复已完成，但不得自签 Daily Gate。四个 Proposed 仍需 root 写回实际 Books，并由新的非作者 reviewer 回读正文、相邻交接、109 个 No Change 的受影响分层与 913 个 closure 的受影响反查。故 README 与 canonical files 必须保持 `Ongoing / Open`。
"""
(HERE / "V3_MINIMAL_REPAIR_RECERTIFICATION_20260915.md").write_text(recert)

print(json.dumps({
    "raw": ledger["raw_identity_count"],
    "retained": ledger["counts"]["semantic_reviewed_retain_frozen"],
    "closures": ledger["counts"]["pre_denominator_closure_reviewed"],
    "deep": evidence["deep_complete"],
    "standard": evidence["standard_complete"],
    "blocked": evidence["blocked"],
    "applied": evidence["books_integrate_applied"],
    "proposed": evidence["books_integrate_proposed"],
    "no_change": evidence["books_no_change"],
}, ensure_ascii=False, indent=2))
