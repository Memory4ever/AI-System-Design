#!/usr/bin/env python3
"""Materialize the bounded Round-4 author repair for 2026-05-13.

This author-side transformation is intentionally narrow.  It reopens the 21
families named by the fresh review plus seven failures found by the required
nearest-sibling challenge, repairs ten proposition comparisons, preserves the
already accepted 21 root writes, and never edits Books.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "papers/2026/05/_sources/daily-20260513"
REPORT = ROOT / "papers/2026/05/13/README.md"


def item(node, score, decision, anchor_label, anchor_query, admission, method, evaluation, limits, mechanism, tradeoff):
    return {
        "node": node, "score": score, "decision": decision,
        "anchor_label": anchor_label, "anchor_query": anchor_query,
        "admission": admission, "method": method, "evaluation": evaluation,
        "limits": limits, "mechanism": mechanism, "tradeoff": tradeoff,
    }


# decision is either ``root`` or ``nochange``.  These are candidate-level
# semantic judgements, not proof that a root write has happened.
R = {
    "2605.11217": item("TRAIN-RLHF", (2, 2, 2), "root", "从持久权重更新到条件化 Activation Intervention", "从持久权重更新到条件化 Activation Intervention", "RAG-Pref 将 preferred/dispreferred retrieval 在推理时变成 alignment actuator，改变 offline weight alignment 与 online refusal guardrail 的分工。", "§3 Offline and Online Preference Alignment；§3.1 RAG-Pref；§3.2 Contrastive Information", "§5、§5.1 与 Appendices C/F/G；五个开放模型、agentic refusal 与一般偏好任务", "§6 讨论范围；无独立 Limitations；作者平均提升不构成未测攻击或生产安全保证", "检索器返回正负偏好示例，生成器在当前 query 上消费对比信息；retrieval 只拥有 conditioning proposal，output policy 仍拥有放行权。", "省去再训练但增加检索质量、污染、上下文成本与 online drift；检索证据不足时回退离线 alignment、静态 policy 与显式拒答 gate。"),
    "2605.11388": item("AGENT-PLANNING", (2, 2, 2), "root", "从目标到状态图", "从目标到状态图", "DOLORES 用可执行 decomposition language 和受控 reasoning threads 改变通用 Agent 的计划、执行与 goal revision 控制流。", "§3 Formal Language；§4 DOLORES Architecture and Implementation", "§5；四个 reasoning benchmarks、三个模型设置与受控 decomposition", "Appendix A Limitations：分解编写、token 成本和 domain/task 覆盖受限", "形式化分解产生带依赖的子问题，reasoning threads 分别执行后再由控制器合并；模型生成的分解仍是 proposal。", "结构化状态提高可审计性但增加分解错误、同步与 token 成本；简单短任务继续适合单轨推理。"),
    "2605.11403": item("TRAIN-GRPO", (2, 2, 2), "nochange", "多任务 RL 的 curriculum/KL controller（正文段落）", "多任务 RL 把所有任务按固定 curriculum", "adaptive KL 与基于逐题历史通过率的 Gaussian curriculum 改变 GRPO/RLVR 的探索控制变量。", "§3.3 Adaptive KL；§3.4 Gaussian Curriculum Sampling；§3.5 Algorithm；§3.6 Implementation", "§4.1–§4.4；DAPO-17K、两个模型和六个数学 benchmark", "§5 与附录；无独立 Limitations；只支持受测数学 RLVR 设置", "batch accuracy 调整 KL，逐题 EMA pass-rate 在中等难度处获得较高采样权；两者共享当前 policy 的能力观测。", "提高学习信号利用率但会放大能力估计滞后与任务迁移偏差；正文已明确版本化 task utility 同时驱动样本调度和 per-task KL，并给出固定 mixture/floor fallback。"),
    "2605.11538": item("TRAIN-GRPO", (2, 1, 2), "root", "Group-relative Gradient 不是独立样本均值", "Group-relative Gradient 不是独立样本均值", "covariance-aware token reweighting 改变 GRPO 中 extreme token 的更新权重与训练稳定性。", "§2.2 Motivation；§2.3 Covariance-aware Advantage Reweighting", "§3；1.5B/7B 模型与数学 reasoning 设置", "Limitations 明确只覆盖至 7B 和数学任务", "方法估计 token probability 与 advantage 的协方差，并以 Gaussian kernel 降低 extreme token update 的影响。", "减少少数极端更新但引入 kernel/scale 超参并可能压低真正关键 token；分布稳定时保留原 GRPO，异常时回退 clipping/gradient diagnostics。"),
    "2605.11547": item("MULTIMODAL-GENERATIVE-PARADIGMS", (2, 1, 2), "nochange", "Diffusion trajectory 的 sensitivity calibration profile（正文段落）", "sensitivity calibration profile", "sharpness-aware sampler 把 flow generation 的 timestep 预算改为由离线局部敏感度校准的非均匀调度。", "§3 Offline Calibration and Online Sampling；§4 Numerical/Variational/Statistical Principles", "§5 与 Appendices D/E；固定 NFE、synthetic trajectories 与 FLUX 设置", "无独立 Limitations；结论限于作者 sampler、模型与指标，NFE 不等于端到端延迟", "离线有限差分估计 velocity-field sharpness，按分位数构造 timestep grid，线上仍用普通 Euler。", "额外 calibration 换同 NFE 下的误差重分配，但存在 profile drift 与 workload dependence；正文已要求 sensitivity profile、trajectory displacement、quality tolerance 和 global error budget。"),
    "2605.11559": item("MULTIMODAL-REPRESENTATION", (2, 2, 2), "root", "任务贡献与当前可靠性不能共用一个 Gate", "任务贡献与当前可靠性不能共用一个 Gate", "attention-spectrum sensor 将多模态幻觉检测与 decoding correction 绑定到可观测的视觉注意力结构。", "§3.2–§3.3 Empirical Sensor；§4.1–§4.5 LaSCD", "§5；多种 MLLM 与视觉问答/幻觉 benchmark", "§6 与 Appendix C：依赖 grid visual token，未覆盖 reasoning-intensive task 或更大模型", "Laplacian attention energy 选择视觉证据较强的层，再用层间对比 logits 修正生成；sensor 不拥有事实真值。", "增加层选择、校准与额外 forward 成本，attention 相关性可能失效；信号不稳时回退 provenance-grounded evidence 与保守 abstention。"),
    "2605.11605": item("MULTIMODAL-REPRESENTATION", (2, 2, 2), "root", "固定预算要先分配信息责任，再选择具体 Token", "固定预算要先分配信息责任", "audio-explainability-aware pruning 将 Omni-LLM 的 visual token 保留规则从单模态重要性改为跨模态冗余条件。", "§2.2 Audio-guided Token Selection；§2.3 Depth-score Temporal Merging", "§3；六个 audio-visual benchmark、效率实验及简单 online variant", "Appendix D.2 Limitations；结论依赖音频预测器、受测模型与视频结构", "audio predictor 标识可由声音解释的视觉内容，只移除跨模态冗余 token；depth score 再合并时间片段。", "节省 token/compute 但会误删音频未能表达的空间细节，且 predictor drift 会改变状态；不确定时保留完整 visual state 或提高预算。"),
    "2605.11712": item("TRAIN-RLHF", (2, 2, 2), "root", "从持久权重更新到条件化 Activation Intervention", "从持久权重更新到条件化 Activation Intervention", "独立 value module 与 bridge token 将 alignment steering 从修改 backbone 权重改为可刷新的外部 value state。", "§3 Independent Value Policy、SVGT and Bridge Tokens", "§4；四个 backbones、公开 safety data 和三次随机种子", "Appendix E：约 50% latency、单维 value 与文化偏差等限制", "冻结 backbone 的 hidden state 送入独立 value module，bridge token 将方向注入生成并可动态刷新。", "可独立升级 value policy，但增加约 50% latency、表示耦合和价值压缩风险；低风险场景可保留离线 alignment，异常时撤销 bridge intervention。"),
    "2605.11716": item("PLATFORM-SECURITY", (2, 2, 2), "root", "Learned Security Sensor 与 Reference Monitor 必须分层", "Learned Security Sensor 与 Reference Monitor 必须分层", "decoding-level probe 将 MLLM safety 从生成后过滤前移到候选 token hidden-state 的在线筛选。", "§4 Decoding Probe and Modal Semantic Vector", "§5；三个 safety datasets 与多种 attack/utility 设置", "Limitations：text safety transfer 可能降低 robustness；gradual correction 与 top-k 受限", "logistic probe 检查 top-k candidate hidden states，不安全时重采样；跨模态 safety vector 是 sensor，gateway policy 保留 commit authority。", "提前拦截换 probe drift、top-k 漏检和语义干预副作用；探针置信不足时回退确定性 policy、输出后审计或人工 gate。"),
    "2605.11727": item("MULTIMODAL-REPRESENTATION", (2, 2, 2), "root", "时间、空间与 provenance 必须进入状态", "时间、空间与 provenance 必须进入状态", "measurement-domain input 把 ISP 前原始传感证据、camera conditioning 与 exposure supervision 纳入 VLM representation identity。", "§3 Measurement-grounded Vision-Language Learning；§4 PRISM-VL", "§5；多种 VLM comparison 与 measurement-domain tasks", "无独立 Limitations；相机、任务、数据和受测模型限制结论", "模型在显示域之外读取 measurement-domain signal，并携带 camera/exposure 条件，使感知状态保留采集过程。", "保留原始证据提高可校准性但增加传感器接口、数据与模型复杂度；原始信号缺失时回退标准 ISP 表示并降低结论强度。"),
    "2605.11832": item("MULTIMODAL-EMBODIED-VLA", (2, 2, 2), "nochange", "坐标系归一化是 Representation 到 Action Schema 的桥", "坐标系归一化是 Representation 到 Action Schema 的桥", "multi-view geometry prior、occlusion gate 与 action manifold expert 改变 VLA 的几何状态和动作表示。", "§3 and Appendices B/C：Geometry Module、Gated Transformer and Action Manifold", "§4；simulation benchmarks 与 real-robot evaluation", "§4H Limitations；受传感、场景、机器人与 action schema 限制", "单目与合成多视图建立几何 prior，occlusion gate 过滤不可靠证据，action manifold 将 state 映射到可执行方向。", "几何显式化换 calibration、额外视图与模型复杂度；正文已明确坐标归一化、uncertainty、传统 estimator fallback 以及 action schema/controller 分权。"),
    "2605.11856": item("MULTIMODAL-REPRESENTATION", (2, 1, 2), "root", "理解与生成也不必被迫共享全部参数", "理解与生成也不必被迫共享全部参数", "UniVLR 将文字 CoT 与辅助图像写入统一 visual canvas，再压缩为连续 latent reasoning state。", "§2 Unified Canvas、Latent Alignment and Continuous Autoregression", "§3；多个 VLM reasoning benchmarks 与消融", "§5：依赖 OCR/layout、可检查性较低、固定 token budget，仍需要外部工具", "文本推理和中间图像先渲染为 canvas，编码为紧凑 latent token，最终答案仍通过 text path 输出。", "跨模态中间状态更统一但降低可解释性并引入 OCR/layout bottleneck；复杂事实任务应保留文本证据与外部工具 fallback。"),
    "2605.11882": item("PLATFORM-SECURITY", (3, 2, 2), "root", "安全数据闭环还可由当前 policy 生成 adversarial candidates", "安全数据闭环还可由当前 policy 生成", "on-policy failure trajectory repair 将 Agent safety 从静态数据训练改为当前 policy 失败、修复、验证和回放的闭环。", "§3 Failure Trajectory Evolution", "§4；严格 dev/test split、三个随机种子和 AgentDojo/AgentHarm/ATBench", "Appendix K：依赖 verifier、policy-generated repair 与有限 benchmark，未覆盖真实长时域", "当前 policy 生成失败，same-policy 产出 repair，独立 verifier 评分，Pareto replay 再进入 SFT/PFPO。", "提高当前 failure frontier 覆盖但可能 self-confirm、污染 replay 并过拟合 verifier；保留独立 holdout、人工安全 gate 和静态基线。"),
    "2605.12013": item("MULTIMODAL-GENERATIVE-PARADIGMS", (2, 1, 2), "root", "Output Decoder 是独立的版本化 Generation Artifact", "Output Decoder 是独立的版本化 Generation Artifact", "L2P 用 latent diffusion 的合成图像训练 pixel-space generator，在 inference 移除 VAE，改变 representation/training boundary。", "§3.2–§3.4 L2P Transfer and 4K Extension", "§4；1024/4K generation 与受测 latent teacher", "Appendix D：synthetic source upper bound，省略 task-specific loss 等", "teacher 在 latent path 生成训练图像，student 直接在 pixel space 学习；VAE 只存在于数据生成而不在部署路径。", "减少部署 decoder 依赖但继承 teacher bias 并增加离线合成成本；数据不足或高频细节失败时保留 latent/VAE 路径。"),
    "2605.12022": item("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2), "root", "Benchmark 生成器也会塑造被评估的任务人口", "Benchmark 生成器也会塑造", "SAGE 将 robustness variant generation 与 rubric verification 组成版本化 evaluation artifact pipeline。", "§3.2 VariantQual；§3.3 VariantGen", "§4；MCQ robustness、生成器/verifier 和多模型对比", "Appendix E：只覆盖 MCQ、预定义 variant 类型并依赖 verifier", "小模型生成 variants，rubric verifier 负责质量筛选，最终 suite 才进入评估；generator 不拥有有效性真值。", "扩大覆盖换 verifier bias、模板化和成本；低置信 variant 应隔离、人工抽检并保留原 benchmark baseline。"),
    "2605.12112": item("TRAIN-RLHF", (3, 1, 3), "root", "反馈预算必须绑定样本粒度与可观测不确定性", "反馈预算必须绑定样本粒度", "flow-based RLHF 中固定 policy entropy 不能反映视觉多样性坍缩，perceptual entropy 因而成为新的控制变量。", "§3 Diagnosis of Constant Policy Entropy；§4 Perceptual Entropy and GRPO", "§5；FLUX.dev、SD3.5-Medium 与披露 reward settings", "无独立 Limitations；只覆盖两个 flow text-to-image model 和受测 rewards", "固定 noise schedule 使 policy entropy 近似常量，而 perceptual diversity 可坍缩；方法估计 perceptual entropy 并加约束。", "更贴近输出变化但依赖感知 encoder/metric，可能奖励表面差异；metric 漂移时回退人工/多指标评估和保守 KL。"),
    "2605.12178": item("MULTIMODAL-WORLD-MODELS", (3, 2, 3), "root", "World Model 不必保存全部 Observation，但必须覆盖下游 Query Closure", "World Model 不必保存全部 Observation", "enterprise agent 通过读取 live configuration 恢复环境动态，改变 learned world model 与 runtime discovery 的 state-owner 分工。", "§3 Enterprise Dynamics；§4 Gym；§5 Prompted/Learned/Discovery Approaches", "§6；单一 enterprise platform、多个任务和模型", "§9 与 Appendix A：依赖可读规则、tool use、单平台、Tier 1/2 任务及少量模型", "prompted rules、learned dynamics 与 runtime discovery 是三条分支；deployment shift 下 live config 才拥有当前环境状态真值。", "discovery 提高 freshness 但增加工具延迟、权限和解析故障；配置不可读时回退版本化 simulator/learned prior，并保持 state uncertainty。"),
    "2605.12416": item("MULTIMODAL-EMBODIED-VLA", (2, 2, 2), "root", "Hierarchical Generative Planner 要把 Subgoal 与低层轨迹分权", "Hierarchical Generative Planner", "Flow Map 的任意步跳转与 Q-guided trust-region search 改变 action generation 的 latency、proposal 和 control contract。", "§3 Flow Map Q-guidance；§3.4 Q-guided Search", "§4；12 robotic tasks、7 environments、offline-to-online setting 与速度分析", "无独立 Limitations；只支持披露任务、环境与 policy", "flow map 允许大步 proposal，Q-guided trust region 和 re-noising beam search负责筛选；controller 仍拥有执行 commit。", "减少迭代换 Q-bias、搜索成本和大步误差；Q 不可靠时缩短 jump、回退逐步 flow 或传统 controller。"),
    "2605.12464": item("INFER-TENSORRT-LLM", (2, 2, 2), "root", "量化为什么不自动带来加速", "量化为什么不自动带来加速", "ScaleSearch 把 BFP/NVFP4 block scale 从 max heuristic 改为可搜索的执行/误差选择。", "§3 BFP；§4 ScaleSearch；§4.2 Language Modeling", "§5.1–§5.3；特定模型、PTQ、NVFP4 attention 和 overhead", "无独立 Limitations；结论绑定受测模型、格式和 kernel", "对候选 mantissa-scale 组合搜索而不是固定 block max，量化 artifact 保存 scale selection。", "降低误差但增加 calibration/search overhead 和 backend coupling；预算不足时回退 max scale 或较高精度，并重新验收 latency。"),
    "2605.12495": item("TRAIN-GRPO", (2, 2, 2), "root", "Verifiable Reward 不等于每个样本都可学习", "Verifiable Reward 不等于每个样本都可学习", "AlphaGRPO 将统一多模态生成 reward 分解为离散 reasoning 与连续视觉 trajectory 的原子可验证问题。", "§4.1 AlphaGRPO；§4.2 Decompositional Reward；§4.3 Data", "§5；多个 image generation benchmarks 与 MLLM evaluators", "Appendix A.1 Limitations；reward/evaluator、视觉任务与模型范围受限", "prompt 被拆成语义/质量原子问题，由 MLLM 分项评分后组成 GRPO feedback，而不是单一整体 reward。", "credit 更细但引入 decomposition error、judge bias 和 reward hacking；无法验证时回退人工 pair/整体质量 gate。"),
    "2605.12500": item("MULTIMODAL-REPRESENTATION", (3, 2, 2), "nochange", "理解与生成也不必被迫共享全部参数（正文段落）", "理解与生成也不必被迫共享全部参数", "SenseNova-U1 用 pixels/words 共享 token/backbone 与轻量 patch encoder/decoder 构成 native understanding-generation interface。", "§3.1 Near-lossless Visual Interface；§3.2 Native Unified Model；§3.3 Objective；§3.4 Training；§3.5 Inference", "§5；多个模型规模和作者 benchmark", "无独立 Limitations；VLA/world-model 结果只属 preliminary，厂商结果不外推", "pixel 与 word token 进入共享 backbone，视觉 patch encoder/decoder 不依赖 pretrained vision encoder 或 VAE。", "native interface 降低组件裂缝但提高联合训练干扰和重训成本；正文已比较 fully native、modular hybrid 与 ensemble 的参数共享及共存边界。"),

    # Deterministic nearest-sibling challenge failures.
    "2605.11195": item("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2), "root", "评估对象有四个层次", "评估对象有四个层次", "DP 对 logit-level 与 output-level social bias 的影响不一致，说明 privacy claim 与 fairness claim 必须按行为层级分开验收。", "§3 Motivation and Evaluation Framework；§4 Experimental Setup", "§5；sentence scoring、completion、classification 和 QA 四类范式", "§7 Limitations；单一 pretrained LLM/DP setting 与选定 bias metrics", "同一 DP model 在四种 evaluation surface 上产生不同 bias 变化，memorization reduction 不拥有 fairness truth。", "多范式评估增加数据和解释成本；指标冲突时不得聚合成单一安全结论，应保留分层结果和发布限制。"),
    "2605.11534": item("PLATFORM-EVALUATION-SYSTEM", (2, 2, 2), "root", "Agent and Outcome Evaluation", "Agent and Outcome Evaluation", "PRISM 把 embodied-agent 单一 success rate 拆成 perception、intent reasoning 与 long-horizon coordination 的可替换诊断 probe。", "§3 Benchmark Construction；§4 Agent-agnostic Protocol and Diagnostic Probes", "§5；300 tasks、五个 apartment、七个 LLM 与模块替换消融", "Appendix J：模拟住宅、任务/对象覆盖与 responsible release 限制", "统一 action API 固定环境，capability tiers 和可替换 probes 分离 failure owner；probe 只是诊断，不等于因果证明。", "获得可定位失败但增加 oracle/probe 假设和 simulator gap；开放世界结果须回退 end-to-end outcome 与真实环境验证。"),
    "2605.11556": item("TRAIN-SFT", (3, 2, 3), "root", "Rollout-conditioned Distillation 应按证据归因，而不是整段照抄", "Rollout-conditioned Distillation", "Hindsight Hint Distillation 从当前 Agent 失败 rollout 生成针对性 hint，再蒸馏成功轨迹，改变 agentic SFT 的数据生成闭环。", "§3、§3.1–§3.3 Hindsight Hint Distillation", "§4；SWE-bench Verified/Multilingual、OpenHands、基线与消融", "无独立 Limitations；结论绑定 coding agent、judge/hint generator 与受测模型", "失败轨迹定位阻塞点，teacher 生成 hint scaffold，policy 完成 rollout 后自蒸馏；hint 不进入部署接口。", "降低人工 CoT 成本但可能蒸馏错误归因、judge bias 和 scaffold shortcut；hint 质量不足时保留人工 demonstrations/verified tests。"),
    "2605.11608": item("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "root", "第一个不变量：评估声明必须绑定完整对象", "第一个不变量", "PRISM 将 post-training model drift 分解为 scale、shape 与 output-head 三轴，并把诊断轴映射到不同修复选择。", "§3 Unified Risk Bound；§3.3 Three Diagnostic Axes；§3.5 Shape Regularization", "§4–§5；两类模型、五个 benchmark、quantization/LoRA/GGUF variants", "§6 Discussion；bound/calibration、near-isometry、模型与 variant 范围限制，未提供生产风险保证", "几何 risk-gap upper bound 保存 target/variant/head identity，三轴分别诊断 scale、shape 与 head divergence。", "提供可操作诊断但依赖表示访问、对齐和校准假设；假设不成立时回退 task-level held-out evaluation。"),
    "2605.11730": item("PLATFORM-SECURITY", (2, 2, 2), "nochange", "安全数据闭环还可由当前 policy 生成 adversarial candidates（正文段落）", "安全数据闭环还可由当前 policy 生成 adversarial candidates", "persona-conditioned adversarial search 连接 attack discovery、带 metadata 的 defense dataset 与 adapter fine-tuning。", "§3 TAP Background；§4 Method；§6 Dataset Generation and Mitigation", "§5 与 Appendix B/C；GPT-OSS 120B、自动 evaluator、adapter fine-tuning", "§8 Limitations：persona/strategy、自动评分、目标模型与 transfer 范围受限", "并行 persona/strategy 搜索生成 attack candidates，metadata 与 guard/evaluator 形成筛选后再进入 defense tuning。", "扩大多样性但可能 self-confirm、放大 evaluator blind spot；正文已要求 generator、guard、policy taxonomy、人工切片和 deployment gate 分离保存。"),
    "2605.12179": item("TRAIN-DPO", (2, 1, 2), "root", "Preference Pair 选择是实验设计，不只是数据量选择", "Preference Pair 选择是实验设计", "SyncDPO 用规则化时间扰动在线构造 preference negatives，并以 curriculum 调节 video-audio 对齐难度。", "§3.2 Negative Construction；§3.3 Curriculum Learning", "§4 与 Appendices A/B；四类 benchmark、客观/主观 evaluation", "Appendix C Limitations：规则负例、数据/模型与时序 metric 范围受限", "对原样本施加 coarse-to-fine temporal distortion 构造 rejected pair，避免昂贵采样排序并逐步提高难度。", "降低 pair 构建成本但可能学习扰动模板而非真实同步；真实负例或人工偏好仍是必要 fallback。"),
    "2605.12497": item("AGENT-RAG", (2, 2, 2), "root", "多模态 Evidence 还要检查模态间的覆盖与支配关系", "多模态 Evidence", "Pixel-Searcher 把 web evidence acquisition、实体身份解析与 box/mask grounding 串成可追踪的 search-to-pixel workflow。", "§3 WebEyes；§4、§4.1–§4.3 Pixel-Searcher", "§5；120 images、645 QA pairs、1,927 task samples 与消融/failure analysis", "无独立 Limitations；小规模 benchmark、web freshness、search/tool 和 grounding model 限制", "Agent 先检索并解析隐藏实体，再把证据绑定到视觉 instance；external evidence 只支持 identity proposal，pixel grounding 仍需独立验证。", "开放知识提高 long-tail perception，但引入 web provenance、实体歧义、工具延迟和错误级联；证据不足时 abstain 或回退 image-only/local corpus。"),
}


WEAK = {
    "2605.11029": ("nochange", "PLATFORM-SECURITY", "跨会话分解会绕过 Prompt-local Guard", "跨会话分解会绕过 Prompt-local Guard", "正文同时要求跨会话 dormant payload 在每次读取/执行前重新 admission，并把 Safety Evaluation 单位定义为 Run、绑定 Tool Trace 与 deterministic predicate；这直接覆盖完整 fragment chain、benign cover session 与 sandbox trace 的证据单位。"),
    "2605.11202": ("root", "PLATFORM-EVALUATION-SYSTEM", "Runtime and Service Evaluation", "Runtime and Service Evaluation", "timed multi-request trace 应成为 inference-engine fuzzing workload artifact；crash/hang/performance 之外还要以 controlled replay 与 log-prob oracle 捕获 silent corruption。"),
    "2605.11209": ("root", "PLATFORM-EVALUATION-SYSTEM", "Agent Regression Testing 需要分配 Evidence Budget", "Agent Regression Testing 需要分配 Evidence Budget", "CEM 学习的 failure-prone sampling distribution 是 rare-failure evidence allocator，不是真实 failure rate owner；必须保留 unbiased audit、importance accounting 与 fallback。"),
    "2605.11376": ("root", "AGENT-MULTI-AGENT", "Coordination State 必须有显式 Owner 与 Commit Transition", "Coordination State 必须有显式 Owner", "population-scale personal-agent exchange 需要把 directory/routing、user identity、negotiation state 与 agreement commit 分权；结构化 message 不自动获得代表用户承诺的 authority。"),
    "2605.11418": ("nochange", "AGENT-PLATFORM", "被审计的 Skill 必须与实际执行 Artifact 同一", "被审计的 Skill 必须与实际执行 Artifact 同一", "正文要求 reviewed bundle immutable identity、依赖/policy admission、执行同 digest 和 runtime receipt，并在 Skill Lifecycle 以 Admission 与 Runtime 两个 Gate 分权；这直接覆盖 semantic metadata/instruction supply-chain。"),
    "2605.11770": ("nochange", "AGENT-PLATFORM", "Skill Lifecycle 需要 Admission 与 Runtime 两个 Gate", "Skill Lifecycle 需要 Admission 与 Runtime 两个 Gate", "正文同时要求被审计 Skill 与实际执行 artifact 同一，并在运行前检查 principal、参数、环境、版本、副作用预算和 postcondition；这直接覆盖 privileged skill behavioral integrity。"),
    "2605.11496": ("root", "PLATFORM-EVALUATION-SYSTEM", "从目标到证据，而不是从指标到目标", "从目标到证据", "recognised-evaluation 与 deployment-continuous context 的 behavioral differential 必须成为显式 evaluation state；marginal benchmark score 不能识别该 differential。"),
    "2605.11746": ("root", "PLATFORM-EVALUATION-SYSTEM", "Evaluation Identity 必须包含 Harness 与 Environment", "Evaluation Identity 必须包含 Harness", "visible CoT 与 answer-determining computation 可能不同步；oversight contract 必须区分 trace readability、causal use 与 final behavior，而不能把可见文字当内部计算真值。"),
    "2605.12087": ("root", "AGENT-PLATFORM", "Agent Runtime State Machine", "Agent Runtime State Machine", "intermediate artifact 必须是 typed、versioned、addressable、dependency-aware 的 durable state，并明确 authoritative producer 与 downstream consumers。"),
    "2605.12131": ("root", "PLATFORM-EVALUATION-SYSTEM", "第一个不变量：评估声明必须绑定完整对象", "第一个不变量", "Agent evaluation 的 publication bundle 应同时保存 rollout record、声明的 views/reporting rules 与 dropped-runs manifest，使报告分数可追溯到同一证据对象。"),
}


SIBLING_SAMPLE = [
    "2605.11195", "2605.11259", "2605.11383", "2605.11402", "2605.11406", "2605.11511",
    "2605.11534", "2605.11541", "2605.11553", "2605.11556", "2605.11606", "2605.11608",
    "2605.11619", "2605.11684", "2605.11705", "2605.11711", "2605.11720", "2605.11730",
    "2605.11735", "2605.11953", "2605.11981", "2605.12009", "2605.12019", "2605.12176",
    "2605.12179", "2605.12497", "2605.12498",
]
SIBLING_REOPENED = {"2605.11195", "2605.11534", "2605.11556", "2605.11608", "2605.11730", "2605.12179", "2605.12497"}


def load(name):
    return json.loads((OUT / name).read_text())


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def roadmap_paths():
    text = (ROOT / "ROADMAP.md").read_text()
    return {m.group(1): m.group(2) for m in re.finditer(r"^\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", text, re.M)}


def locate(path, query):
    for n, line in enumerate((ROOT / path).read_text().splitlines(), 1):
        if query.lower() in line.lower():
            return n
    raise ValueError((path, query))


def detailed_review(row, meta):
    family = row["source_family_id"]
    dd, sr, dur = meta["score"]
    return "\n".join([
        f"#### {row['title']}", "",
        f"**问题与旧基线。** {meta['admission']} 旧路径在新增约束不存在、任务较窄或额外控制成本超过收益时仍是合理基线。", "",
        f"**Method / ownership。** exact-v1 {meta['method']}。{meta['mechanism']}", "",
        f"**Evaluation contract。** {meta['evaluation']}。V3={dd}+{sr}+{dur}={dd+sr+dur}；未披露的 hardware、precision、length、batch、concurrency 与 production SLO 均为 `Not Disclosed`。", "",
        f"**Counterevidence / limitations。** {meta['limits']}。", "",
        f"**Trade-off / failure / fallback。** {meta['tradeoff']}", "",
        f"<!-- claim:{family}:start -->exact-v1 只支持上述披露模型、workload、artifact 与 evaluator 下的机制和结果；不支持跨未披露部署的普适收益、安全保证或 production tail 结论。<!-- claim:{family}:end -->", "",
        f"Books Decision=`{'Integrate' if meta['decision']=='root' else 'No Change — Existing Coverage'}`；写回状态由 comparison/queue 单独记录，author 不修改共享 Books。",
    ])


def report_review_text(text):
    """Keep the report's contract disposition separate from writeback state."""
    return re.sub(r"Books Decision=`Integrate[^`]*`", "Books Decision=`Integrate`", text)


def queue_item(row, node, owner_path, anchor, delta, method=None, evaluation=None, limits=None):
    return {
        "source_family_id": row["source_family_id"], "arxiv_id": row["arxiv_id"],
        "stable_node_id": node, "owner_path": owner_path, "proposed_anchor": anchor,
        "semantic_delta": delta,
        "proposed_spine": "旧基线为何合理 → 新约束 → 状态/数据/控制权变化 → exact-v1 证明与未证明 → 代价/failure → fallback/共存",
        "exact_v1_evidence": f"https://arxiv.org/html/{row['arxiv_id']}v1",
        "method_locator": method or "existing exact-v1 evidence entry",
        "evaluation_locator": evaluation or "existing exact-v1 evidence entry",
        "limitations_locator": limits or "existing exact-v1 evidence entry",
        "author_status": "ready_for_root_serial_write",
        "root_status": "pending_root_serial_write",
    }


def main():
    ledger = load("v3-active-ledger.json")
    evidence = load("v3-active-evidence.json")
    comparison = load("v3-books-comparison.json")
    queue = load("v3-root-writeback-queue.json")
    audit = load("v3-author-semantic-audit.json")
    paths = roadmap_paths()

    rows = ledger["owner_day_screening"]
    rows_by = {r["arxiv_id"]: r for r in rows}
    ev_by = {r["arxiv_id"]: r for r in evidence["reviews"]}
    cmp_by = {r["arxiv_id"]: r for r in comparison["comparisons"]}
    isolated_before = json.dumps(ledger["revision_or_non_owner_route_isolation"], ensure_ascii=False, sort_keys=True)
    old_queue_by = {r["arxiv_id"]: r for r in queue["items"]}
    old_applied = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in old_queue_by.items() if v.get("root_status", "").startswith("applied_")}
    assert len(old_applied) == 21

    new_queue = dict(old_queue_by)
    for arxiv_id, meta in R.items():
        row = rows_by[arxiv_id]
        node = meta["node"]
        owner_path = paths[node]
        dd, sr, dur = meta["score"]
        decision = "Integrate — Root write required" if meta["decision"] == "root" else "No Change — Existing Coverage"
        row.update({
            "screening_status": "retained",
            "screening_reason": meta["admission"],
            "round4_semantic_audit": "reopened_after_named_or_bounded_sibling_challenge",
            "review_status": "complete_exact_v1_round4",
            "access_status": "accessible",
            "withdrawal_status": "no official withdrawal banner observed on exact-v1 HTML at 2026-09-15 review time",
            "integration_disposition": decision,
            "stable_node_id": node,
            "score_v3": {"design_delta": dd, "system_reach": sr, "durability": dur, "total": dd + sr + dur},
            "active_v3_evidence_ref": f"v3-active-evidence.json#{row['source_family_id']}",
        })
        ev_by[arxiv_id] = {
            "source_family_id": row["source_family_id"], "arxiv_id": arxiv_id, "title": row["title"],
            "primary_evidence": f"https://arxiv.org/html/{arxiv_id}v1",
            "review_depth": "deep" if dd + sr + dur >= 7 else "standard",
            "review_status": "complete_exact_v1_round4", "access_status": "accessible",
            "reuse_basis": "fresh exact-v1 Round-4 review; no later revision imported",
            "withdrawal_check": "exact-v1 HTML accessible; no official withdrawal banner observed at review time",
            "semantic_admission_reason": meta["admission"],
            "method_locator": meta["method"], "evaluation_locator": meta["evaluation"],
            "limitations_locator": meta["limits"],
            "artifact_boundary": "paper-linked artifact is supplementary; immutable event-time commit is Not Disclosed unless the exact-v1 explicitly binds it",
            "claim_boundary": "Only the exact-v1 model/workload/evaluator contract is supported; no production or cross-family guarantee is inferred.",
            "detailed_review_markdown": detailed_review(row, meta),
        }
        anchor_line = locate(owner_path, meta["anchor_query"])
        cmp_by[arxiv_id] = {
            "source_family_id": row["source_family_id"], "arxiv_id": arxiv_id, "title": row["title"],
            "stable_node_id": node, "owner_path": owner_path,
            "anchor_heading": meta["anchor_label"], "anchor_line": anchor_line,
            "source_binding_line": None,
            "current_books_proposition": (f"正文约第 {anchor_line} 行已逐命题覆盖该机制、代价与 fallback；Review notes 不参与覆盖判断。" if meta["decision"] == "nochange" else f"正文约第 {anchor_line} 行仅提供落点，未承载该 source family 的新增命题。"),
            "new_evidence_delta": meta["admission"],
            "prior_disposition": "pre_denominator_closure",
            "author_decision": decision,
            "requires_root_write": meta["decision"] == "root",
            "author_may_modify_books": False,
        }
        if meta["decision"] == "root":
            new_queue[arxiv_id] = queue_item(row, node, owner_path, meta["anchor_label"], meta["admission"], meta["method"], meta["evaluation"], meta["limits"])

    for arxiv_id, (decision_kind, node, anchor_label, anchor_query, proposition) in WEAK.items():
        row = rows_by[arxiv_id]
        owner_path = paths[node]
        anchor_line = locate(owner_path, anchor_query)
        decision = "Integrate — Root write required" if decision_kind == "root" else "No Change — Existing Coverage"
        row["integration_disposition"] = decision
        row["stable_node_id"] = node
        row["round4_books_comparison"] = "proposition_level_body_recompare_complete"
        cmp = cmp_by[arxiv_id]
        cmp.update({
            "stable_node_id": node, "owner_path": owner_path,
            "anchor_heading": anchor_label, "anchor_line": anchor_line,
            "current_books_proposition": proposition,
            "author_decision": decision,
            "requires_root_write": decision_kind == "root",
            "author_may_modify_books": False,
            "round4_recomparison": "body proposition checked; Review notes excluded",
        })
        if decision_kind == "root":
            new_queue[arxiv_id] = queue_item(row, node, owner_path, anchor_label, proposition)

    candidates = sorted((r for r in rows if r["screening_status"] == "retained"), key=lambda r: tuple(map(int, r["arxiv_id"].split("."))))
    closures = [r for r in rows if r["screening_status"] == "pre_denominator_closure"]
    assert len(candidates) == 128, len(candidates)
    assert len(closures) == 519, len(closures)
    assert len(ledger["revision_or_non_owner_route_isolation"]) == 191
    assert json.dumps(ledger["revision_or_non_owner_route_isolation"], ensure_ascii=False, sort_keys=True) == isolated_before
    assert set(ev_by) == set(cmp_by) == {r["arxiv_id"] for r in candidates}
    assert set(SIBLING_REOPENED) <= set(R)
    for k, v in old_applied.items():
        assert json.dumps(new_queue[k], ensure_ascii=False, sort_keys=True) == v

    ledger["candidate_ids"] = [r["arxiv_id"] for r in candidates]
    ledger["counts"].update(retained_candidates=128, pre_denominator_closures=519)
    ledger["arithmetic"] = "838 = (128 retained + 519 pre-denominator closure + 0 withdrawn) official-owner route + 191 revision/non-owner-route isolation"
    ledger["round4_bounded_repair"] = {
        "fresh_review_named_reopened": 21,
        "fresh_review_named_ids": sorted(set(R) - SIBLING_REOPENED),
        "weak_no_change_recompared": 10,
        "weak_no_change_changed_to_integrate": sorted(k for k, v in WEAK.items() if v[0] == "root"),
        "weak_no_change_confirmed_by_body_proposition": sorted(k for k, v in WEAK.items() if v[0] == "nochange"),
        "sibling_challenge_method": "for each named false negative, nearest preceding and following closure with the same round3_closure_basis; deduplicated",
        "sibling_challenge_sample_count": len(SIBLING_SAMPLE),
        "sibling_challenge_sample_ids": SIBLING_SAMPLE,
        "sibling_challenge_reopened_count": len(SIBLING_REOPENED),
        "sibling_challenge_reopened_ids": sorted(SIBLING_REOPENED),
        "sibling_challenge_reconfirmed_count": len(SIBLING_SAMPLE) - len(SIBLING_REOPENED),
        "owner_receipt_reenumerated": False, "isolated_route_touched": False,
        "previously_accepted_books_sections_reopened": False,
    }

    evidence.update(candidate_count=128, reviews=sorted(ev_by.values(), key=lambda r: tuple(map(int, r["arxiv_id"].split(".")))))
    evidence["books_writeback_status"] = "21_prior_applied_preserved; 30_round4_root_writes_pending"
    comparisons = sorted(cmp_by.values(), key=lambda r: tuple(map(int, r["arxiv_id"].split("."))))
    comparison.update({
        "comparison_count": 128,
        "requires_root_write_count": 30,
        "root_applied_count_pending_fresh_review": 21,
        "comparisons": comparisons,
        "status": "round4_author_repair_complete; root write and fresh non-author review pending",
    })
    queue_items = sorted(new_queue.values(), key=lambda r: tuple(map(int, r["arxiv_id"].split("."))))
    assert len(queue_items) == 51
    assert sum(i.get("root_status", "").startswith("applied_") for i in queue_items) == 21
    assert sum(i.get("root_status") == "pending_root_serial_write" for i in queue_items) == 30
    queue.update({
        "queue_count": 51, "root_applied_count": 21, "pending_root_count": 30,
        "items": queue_items,
        "status": "21 prior writes preserved; 30 Round-4 items pending root serial write",
    })
    audit.update({
        "author_result": "round4_bounded_repair_complete_pending_root_and_fresh_non_author_review",
        "not_a_completion_signature": True,
        "round4_bounded_repair": ledger["round4_bounded_repair"],
        "required_next_reviewer": "root serial writeback, then a different non-author fresh-context reviewer",
    })
    audit.setdefault("checks", {}).update({
        "candidate_evidence_complete": True, "books_comparison_complete": True,
        "round4_exact_v1_accessible": len(R), "round4_withdrawal_banners_observed": 0,
        "root_writeback_queue_total": 51, "root_writeback_queue_pending": 30,
        "prior_accepted_root_items_preserved": 21,
        "sibling_challenge_sample_count": len(SIBLING_SAMPLE),
    })

    dump("v3-active-ledger.json", ledger)
    dump("v3-active-evidence.json", evidence)
    dump("v3-books-comparison.json", comparison)
    dump("v3-root-writeback-queue.json", queue)
    dump("v3-author-semantic-audit.json", audit)

    checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
    old = REPORT.read_text()
    source_section = old.split("## 2. 来源覆盖", 1)[1].split("## 3. 候选与判断", 1)[0].strip()
    source_section = source_section.replace("100 retained、547 closure", "128 retained、519 closure")
    comp_by2 = {c["arxiv_id"]: c for c in comparisons}
    ev_by2 = {e["arxiv_id"]: e for e in evidence["reviews"]}
    lines = [
        "# Daily Research — 2026-05-13", "", "**规范：** V3",
        "**窗口：** 2026-05-12T09:00:00+08:00 ～ 2026-05-13T09:00:00+08:00",
        "**状态：** 进行中", "**Books：** 纳入本次", f"**检查时间：** {checked_at}", "",
        "Round 4 作者侧限定返修已完成：fresh review 指定的 21 个 closure family 与有界 sibling challenge 新发现的 7 个 family 已进入候选级审阅；10 个弱 `No Change` 已重做正文命题对读。报告仍为 `Ongoing`，因为新增 root Books 队列尚未写回，且作者不能自签独立 Gate。", "",
        "## 1. 结论", "",
        "原始身份与 owner-day 边界不变：`838 = (128 retained + 519 pre-denominator closure + 0 withdrawn) + 191 revision/non-owner-route isolation`。本轮没有重枚举 647 条 official owner identity，没有改动 191 条 isolation，也没有重开或改写 fresh reviewer 已通过的 21 个 Books 段。", "",
        "本轮新增 28 个 retained（21 个指定项 + 7 个 sibling challenge 漏项），均完成 exact-v1 Method、Evaluation、limitations/counterevidence、withdrawal 检查、V3 score、Stable Node 与 Books comparison；未观察到 official withdrawal banner。10 个弱比较中 3 个由 Review notes 前的正文命题证明 `No Change`，7 个改为 `Integrate — Root write required`。连同新增候选的判断，root 队列现有 21 个既往 applied item 与 30 个 pending item。", "",
        "## 2. 来源覆盖", "", source_section, "", "## 3. 候选与判断", "",
        "评分为 Design Delta + System Reach + Durability（每项 0～3）。7～9 分 Deep Review，5～6 分标准 Review；安全项强制 Deep。", "",
        "| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |", "| --- | --- | --- | --- | --- |",
    ]
    for row in candidates:
        score = row["score_v3"]
        comp = comp_by2[row["arxiv_id"]]
        link = f"../../../../{comp['owner_path']}"
        dec = "整合" if comp["author_decision"].startswith("Integrate") else "已有覆盖"
        review_label = "深入完成" if comp["author_decision"].startswith("Integrate") or score["total"] >= 7 else "标准完成"
        write_state = "；待 root 写回" if comp["author_decision"] == "Integrate — Root write required" else ""
        lines.append(f"| [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1) | 2026-05-13T08:00:00+08:00 | {row['screening_reason'].replace('|', chr(92)+'|')}；{score['design_delta']} + {score['system_reach']} + {score['durability']} = {score['total']} | {review_label} | {dec}：`{row['stable_node_id']}`，[{comp['anchor_heading']}]({link}){write_state} |")

    lines += ["", "## 4. 证据与知识整合", ""]
    for row in candidates:
        ev = ev_by2[row["arxiv_id"]]
        comp = comp_by2[row["arxiv_id"]]
        lines += [
            f"### [{row['title']}](https://arxiv.org/html/{row['arxiv_id']}v1)", "",
            f"**准入：** {ev['semantic_admission_reason']}", "",
            f"<!-- review:{row['source_family_id']}:start -->", report_review_text(ev["detailed_review_markdown"]), f"<!-- review:{row['source_family_id']}:end -->", "",
            f"**Books 对读：** `{row['stable_node_id']}` → `{comp['owner_path']}` 的“{comp['anchor_heading']}”（约第 {comp['anchor_line']} 行）。{comp['current_books_proposition']} 新证据增量：{comp['new_evidence_delta']} 判定：**{comp['author_decision']}**。", "",
        ]
    lines += [
        "## 5. 缺口与下一步", "",
        "- 既往 21 个 root Books item 保持原 `root_status`，未被本作者重开或改写。", "- 新增 30 个 root write pending item；root 必须按日期与 owner 串行写回共享 Books。",
        "- 28 个本轮恢复 family 的 exact-v1 均可访问且未见 official withdrawal banner；这一观察只代表本次访问时状态。", "- sibling challenge 固定为同 closure basis 的 arXiv ID 最近前/后各一条、去重 27 条；7 条恢复，20 条保持原 family-specific closure。没有据此重扫 647。", "- root 写回后必须由未参与本次作者返修的 reviewer 做 fresh-context denominator、Books marker/owner/position 与假阴性验收。", "",
        "## 6. 复核", "", "结论：**ROUND 4 AUTHOR REPAIR COMPLETE — DAILY 仍为 Ongoing**", "",
        "机械账目、JSON、validator 与 diff 检查不替代下一轮独立语义 Gate。作者未修改共享 Books，也未把 pending queue 冒充已整合。", "",
        "### 活跃证据文件", "", "- `v3-active-ledger.json`", "- `v3-active-evidence.json`", "- `v3-books-comparison.json`", "- `v3-root-writeback-queue.json`", "- `v3-author-semantic-audit.json`", "- `V3_ROUND4_AUTHOR_BOUNDED_REPAIR_20260915.md`", "- `V3_ROUND3_FRESH_NON_AUTHOR_POSTWRITE_REVIEW_20260915.md`", "",
        "**Review Provenance ID:** `daily-20260513-v3-round4-bounded-author-repair-20260915`", "",
    ]
    REPORT.write_text("\n".join(lines))

    checkpoint = f"""# 2026-05-13 V3 Round 4 作者限定返修 Checkpoint

**检查时间：** {checked_at}
**状态：** 作者限定返修完成；Daily 保持 `Ongoing`

## 精确账目

- 原始身份：838；official owner-day 647；isolation 191（未改动）。
- 返修前：100 retained / 547 closure。
- 返修后：128 retained / 519 closure。
- fresh review 指定：21/21 reopened。
- sibling challenge：27 sampled / 7 reopened / 20 reconfirmed。
- active Evidence / comparison：128 / 128。
- Books disposition：15 Already Present + 21 prior Applied + 30 Root Write Required + 62 No Change = 128。
- root queue：51 total = 21 prior applied（原状态保留） + 30 pending。

## 边界

本作者没有重枚举 647、没有触碰 191 isolation、没有编辑共享 Books，也没有重审或改写已通过的 21 个 Books 段。exact-v1 检查未观察到 official withdrawal banner。下一步由 root 写回 30 项，再由新的 non-author reviewer 签署或驳回 Gate。
"""
    (OUT / "V3_ROUND4_AUTHOR_BOUNDED_REPAIR_20260915.md").write_text(checkpoint)


if __name__ == "__main__":
    main()
