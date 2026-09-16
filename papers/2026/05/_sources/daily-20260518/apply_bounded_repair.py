#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emit apply_patch input for the bounded 2026-05-18 author repair.

This helper never writes repository files.  It reads the frozen V3 artifacts,
builds the bounded replacements in memory, and prints a patch for review and
application through apply_patch.
"""

from __future__ import annotations

import difflib
import hashlib
import json
import re
import sys
from pathlib import Path


H = Path(__file__).resolve().parent
REPO = H.parents[4]
REPORT = REPO / "papers/2026/05/18/README.md"


def score(dd: int, sr: int, dur: int) -> dict[str, int]:
    return {"design_delta": dd, "system_reach": sr, "durability": dur, "total": dd + sr + dur}


DECISIONS = {
    "2605.15220": dict(node="TRAIN-DATA", path="books/part-04-training-system/27-data.md", adjacent=["books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", "books/part-04-training-system/28-pretraining.md"], score=score(2, 3, 2), decision="Integrate", method="§3 OP-Mix: On-Policy Data Mixing", evaluation="§4.1 lifecycle experiments; §4.2 performance-efficiency frontier", limitation="§6 Limitations and Future Work; Appendix A reproducibility", contribution="静态或分阶段 mixture 在训练阶段切换后会失去当前模型动力学；OP-Mix 用当前 checkpoint 上的低秩 adapter 插值模拟候选 mixture，因此需要把 mixture 从一次性配方重考虑为贯穿 pretraining、midtraining 与 instruction tuning 的 on-policy control。", delta="候选 mixture 由当前模型的低秩 adapter 插值提出，统一覆盖 pretraining、continual midtraining 与 instruction tuning；controller 节省 proxy compute，但仍受 adapter 近似误差、候选域集合与 scale transfer 限制。", existing="Ch27 已把 mixture 写成版本化 data control plane，也讨论交互实验，但没有当前模型 adapter 插值驱动的跨训练阶段 on-policy mixture 分支。"),
    "2605.15250": dict(node="MODEL-MULTI-HEAD-ATTENTION", path="books/part-02-model/15-multi-head-attention.md", adjacent=["books/part-02-model/14-self-attention.md", "books/part-02-model/16-feed-forward-mlp.md"], score=score(3, 3, 2), decision="Integrate", method="§3.1 Group-Query Latent Attention; §3.2 TransGQLA", evaluation="§4.2 roofline paths; §5 Experiments", limitation="Limitations; §6 Conclusion", contribution="普通 checkpoint 的 MHA/GQA/MQA shape 不能被 runtime 无损切换；GQLA 专门训练一组参数暴露代数等价的 MQA-absorb 与 per-group GQA 两条 decode path，因此需要重考虑 attention state shape 是否能把硬件 compute-bandwidth ratio 与 TP axis 变成运行时选择。", delta="同一 GQLA 权重暴露 MQA-absorb compact-cache 与 per-group GQA expanded-cache 两条代数等价路径，runtime 按硬件 roofline 和 TP 选择；这不是任意 checkpoint 的无损改写，代价是训练/转换、expanded cache 与路径验收。", existing="Ch15 已说明压缩 latent state 必须保留可分片轴，也明确普通 checkpoint 不能任意在 MHA/GQA/MQA 间无损切换；尚缺‘专门参数化后同权重可合法暴露双 decode path’这一条件分支。"),
    "2605.15290": dict(node="TRAIN-PRETRAINING", path="books/part-04-training-system/28-pretraining.md", adjacent=["books/part-04-training-system/27-data.md", "books/part-04-training-system/29-sft.md"], score=score(2, 2, 3), decision="Integrate", method="§3 Deriving Novel Maximal Update Parameterizations; §3.2 Grouped Query Attention", evaluation="§4 Empirical Results; Appendix B.1-B.4", limitation="§5 Conclusions; Appendix B.2 Failure of Yang-Type Coordinate Checking", contribution="既有 μP 迁移不能假定新 attention 参数矩阵满秩或 repetition factor 不改变尺度；论文给出适配 GQA rank/repetition 的 modified spectral-norm 条件并验证 learning-rate 与 weight-decay transfer，因此需要重考虑 GQA architecture search 中可直接复用的超参数合同。", delta="modified spectral norm 在非满秩权重下保留有效 scaling law，并导出 GQA repetition、depth 与 weight-decay 的 maximal-update scaling；transfer 证据限论文模型形状和 coordinate checks。", existing="Ch28 已区分 hyperparameter transfer 与 feature learning regime，但没有 GQA repetition/rank 使标准 μP 推导失效及其修正。"),
    "2605.15484": dict(node="MODEL-MOE", path="books/part-02-model/21-moe.md", adjacent=["books/part-02-model/20-sampling.md", "books/part-02-model/22-long-context.md"], score=score(2, 2, 2), decision="Integrate", method="§3.2 hard-capacity sparse routing; §3.5 per-sample soft gating", evaluation="§4.2-4.5 controlled rho sweep and validation; §5 mechanistic analysis", limitation="§5.1-5.4 routing stability/specialization/efficiency; §6 Conclusion", contribution="稀疏 MoE 的 active-parameter headline 没有说明专家计算在整网 FLOPs 中是否足够大；受控 rho/top-k 实验与 per-sample Soft-MoE 反例表明 backbone compute leverage 和 batch-axis dispatch 可反转 sparse-vs-dense 排序，因此需要重考虑视觉 MoE 的 matched-compute admission。", delta="MoE 收益取决于 expert branch 占全 backbone compute 的 leverage；只改 top-k 可在固定架构下反转收益，batch-axis Soft-MoE 在 per-sample CNN 中还是主要 failure mode。", existing="Ch21 已覆盖 fixed/variable top-k、capacity 与 matched-compute gate，但没有把 backbone compute leverage 和 batch-axis dispatch 作为视觉 MoE 可行性的独立坐标。"),
    "2605.15492": dict(node="MULTIMODAL-EMBODIED-VLA", path="books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", adjacent=["books/part-03-multimodal-world-models/25-multimodal-world-models.md", "books/part-04-training-system/27-data.md"], score=score(2, 3, 2), decision="Integrate", method="§3.1 sparse Legendre trajectory; §3.2 history-anchored flow; §3.3 objectives", evaluation="§4.1-4.4 training, inference, tracking and speed modulation; §5 ablations", limitation="§7 Limitations; Appendices F-G controller and speed analysis", contribution="离散 action chunk 与多步 diffusion 把 horizon、inference cadence 和 controller sampling 紧耦合；FLASH 用连续 Legendre 系数、稀疏时间拟合和 history-anchored single-step flow 分离表示 horizon、生成次数与执行频率，因此需要重考虑 VLA action representation 到低层控制器的接口。", delta="连续 Legendre trajectory 让单次生成覆盖长 horizon，并可解析求导给 controller feed-forward；history anchor 缩短 flow path，但多项式拟合、长 horizon drift 与稀疏演示边界仍需 controller 验证。", existing="Ch26 已拥有 action chunk、flow/diffusion latency 与 controller authority，但没有连续多项式轨迹把生成 cadence 与控制频率解耦的替代表示。"),
    "2605.16165": dict(node="TRAIN-PRETRAINING", path="books/part-04-training-system/28-pretraining.md", adjacent=["books/part-04-training-system/27-data.md", "books/part-04-training-system/29-sft.md"], score=score(2, 2, 2), decision="Integrate", method="§3.1-3.5 modality competition, Fisher projection and hierarchical folding", evaluation="§4 setup; §5 Experiments; Appendix D.3 reproducibility", limitation="§6 Conclusion; Appendix A-C theoretical assumptions", contribution="统一 next-token objective 不保证图像与文本梯度在大 batch 下共享稳定尺度；Fisher-orthogonal projection 与 multi-level folding 把 modality variance 变成可诊断、可校正的 optimizer state，因此需要重考虑 multimodal pretraining 的 large-batch optimizer branch。", delta="ML-FOP-SOAP 用曲率感知 projection 抑制跨模态方差冲突，并以 hierarchical folding 降低 gradient-accumulation micro-step 成本；证据限 Janus/Emu3、作者 batch 与 Fisher/tensor-preconditioner 近似。", existing="Ch28 已把 objective、parameterization、optimizer state 与数据变换绑定，但没有 modality competition 的 Fisher-orthogonal variance correction 或 multi-level folding。"),
    "2605.16241": dict(node="MULTIMODAL-EMBODIED-VLA", path="books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", adjacent=["books/part-03-multimodal-world-models/25-multimodal-world-models.md", "books/part-04-training-system/27-data.md"], score=score(2, 2, 2), decision="No Change — Existing Coverage", method="§3.2-3.4 dual-path supervision, phase anchors and multi-frame direction", evaluation="§4.2-4.5 teacher generalization, granularity, efficiency and noise robustness", limitation="Appendix Limitations; §5 Conclusion", contribution="只模仿 teacher action 会把动作噪声写入小 student；VLA-AD 将 phase anchor 和多帧方向作为仅训练期语义监督、部署时完全移除 teacher/VLM，因此需要核验 Books 是否已拥有 privileged teacher 与独立 runtime student 的边界。", delta="训练期 VLM 提供 phase/direction semantic targets，student 部署时独立运行；收益限 LIBERO 与两类 teacher，语义监督不取得物理提交权。", existing="Ch26 §‘Privileged 3D Teacher 可以留在训练期，不能冒充运行时观测’已明确 training-only privileged target、student representation、部署移除 teacher、噪声传播与 controller/safety authority，足以承载本项长期机制。"),
    "2605.15239": dict(node="TRAIN-SFT", path="books/part-04-training-system/29-sft.md", adjacent=["books/part-04-training-system/28-pretraining.md", "books/part-04-training-system/30-lora.md"], score=score(3, 2, 2), decision="Integrate", method="§3.1 off-policy safety-tax diagnosis; §3.2 on-policy dense self-supervision", evaluation="§5.1 safety-reasoning tradeoff; §5.2 adaptive jailbreaks; Appendices C,G", limitation="Appendix A Limitations; Appendix F KL-direction ablation", contribution="固定安全示范的 off-policy state mismatch 可成为 safety tax 的独立来源；OPSA 在 student 自身 rollout 上用 privileged-context frozen self-teacher 的 token KL，并用 teacher flip rate 选择安全 context，因此需要重考虑安全蒸馏的 occupancy 与监督有效性。", delta="teacher flip rate 先筛出能把 unsafe rollout 翻为 safe 的 privileged context，再在 student on-policy token 上施加 dense KL；早期 compliance token 集中更新是受限机制证据，不是普遍无税安全对齐保证。", existing="Ch29 已覆盖 on-policy distillation 的 state-distribution mismatch，但尚未拥有 safety privileged-context 的有效性筛选、teacher flip rate 与 early compliance-token 边界。"),
    "2605.15224": dict(node="TRAIN-GRPO", path="books/part-04-training-system/33-grpo.md", adjacent=["books/part-04-training-system/32-ppo.md", "books/part-04-training-system/34-dpo.md"], score=score(2, 2, 2), decision="Integrate", method="§3.1 self-improving workflow; §3.2 self-improvement policy optimization", evaluation="§4.2-4.3 agent/math results; §5.2-5.4 dynamics and ablations", limitation="Appendix B Limitations; Appendix A critique-conditioned trajectory analysis", contribution="外部 critique 能修正一次回答但不保证能力在移除 critique 后仍存在；ICRL 共享 solver/critic backbone，以 solver 后续增益奖励 critic，并用 distribution calibration 和 role-wise group advantage 转移为无 scaffold solver 能力，因此需要重考虑 self-critique 的训练 ownership。", delta="solver 与 critic 联合训练；critic reward 绑定 solver 后续增益，distribution ratio 限制 critique-conditioned 到 critique-free 的迁移，role-wise advantage 稳定两角色更新。", existing="Ch33/Ch80 已讨论 critic、self-critique 与 scaffold-removal，但没有共享 backbone 的 joint solver/critic objective、distribution-calibrated transfer 和 role-wise group advantage。"),
    "2605.15300": dict(node="MULTIMODAL-REPRESENTATION", path="books/part-03-multimodal-world-models/23-multimodal-representation.md", adjacent=["books/part-02-model/22-long-context.md", "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md"], score=score(2, 2, 2), decision="Integrate", method="§2.1-2.3 architecture, perceiver language blocks and training", evaluation="§3 Experiments; §4.1-4.5 analysis and efficiency", limitation="Appendix C destructive adaptation; Appendix D failure behaviors; §6 Conclusion", contribution="轻量 projector 把未对齐 visual features 推入 LLM 后会消耗早层深度并造成语言能力破坏；DPA 让小 VLM perceiver 在入口前完成深层语言空间对齐，因此需要重考虑 projector、perceiver 与 LLM depth 的职责边界。", delta="用可复用小 VLM 取代 ViT+projector 作为 perceiver，使视觉表示在进入目标 LLM 前先经过 language blocks；代价是额外 perceiver compute、模块兼容和对其文本能力的依赖。", existing="Ch23 已拥有 visual encoder/projector 与 alignment 一般机制，但没有‘以小 VLM perceiver 提前消化浅层对齐、保留目标 LLM 推理深度’的分支。"),
    "2605.15491": dict(node="MODEL-TRANSFORMER-LAYER", path="books/part-02-model/17-transformer-layer.md", adjacent=["books/part-02-model/16-feed-forward-mlp.md", "books/part-02-model/18-decoder-only.md"], score=score(2, 1, 2), decision="Integrate", method="§3.2.1-3.2.3 boundary activations, closed-form operator and insertion", evaluation="§5.1-5.3 experiments and calibration-size ablation; Appendix G latency", limitation="§6 Discussion; Appendix D fine-tuning comparison", contribution="整层 pruning 破坏下一 surviving layer 的输入分布，不能只用 pruning score 解释质量损失；Ghosted Layers 从小 calibration set 求闭式线性 boundary operator，因此需要重考虑 layer removal 的恢复 artifact 与校准边界。", delta="在被删 block 的边界收集 activation pair，解 unconstrained closed-form linear alignment 并插回模型；它保留 pruning speedup但引入 calibration dependence、operator state 和未测分布风险。", existing="Ch17 解释 residual/layer state 与可移除性，尚未拥有 pruning 后 boundary-activation mismatch 的闭式恢复 operator。"),
    "2605.16233": dict(node="AGENT-MEMORY", path="books/part-07-agent/77-memory.md", adjacent=["books/part-07-agent/76-rag.md", "books/part-07-agent/78-tool-calling.md"], score=score(2, 2, 2), decision="Integrate", method="§3.1 hierarchical ReAct memory; §3.2 failure reflexion; §3.3 FORGE protocol", evaluation="§5.1 broadcast comparison; §5.2-5.3 graduation/threshold ablations", limitation="§7 Limitations & Future Work; Appendix A artifact scope", contribution="单流 Reflexion 会把每条轨迹困在局部经验中；FORGE 将 failure-derived prompt memory 放入 population stages，由 champion broadcast 扩散且以 graduation 冻结实例，因此需要重考虑 memory promotion 的群体传播、成本停止与污染半径。", delta="外环按 stage 选 champion 并广播自然语言 memory，graduation 主要节省 compute；broadcast ablation 支持传播是收益机制，但全部证据限 CAGE-2 B-line，错误 champion 也会扩大污染。", existing="Ch77 已有 failure receipt、memory admission 与 rollback，却没有 population-level champion broadcast、graduation 和跨实例污染/成本边界。"),
    "2605.16143": dict(node="AGENT-PLANNING", path="books/part-07-agent/79-planning.md", adjacent=["books/part-07-agent/78-tool-calling.md", "books/part-07-agent/80-reflection.md"], score=score(2, 2, 2), decision="No Change — Existing Coverage", method="§3.2 Exploration Checkpoint Coverage; §3.3 training; §3.4 Explore-then-Act", evaluation="§4.2-4.4 diagnosis, intervention and analysis", limitation="Appendix A Limitations and Future Work; Appendix D sensitivity", contribution="task-only RL 会过早 exploitation；独立 exploration rollout、ECC coverage 与 Explore-then-Act 把信息收集预算和任务执行分离，因此需要核验 Planning 是否已拥有 evidence-gathering action 与提交 action 的分权。", delta="先用预算发现 state/object/affordance checkpoints，再带 grounded knowledge 执行任务；ECC 是受限环境 coverage proxy，不是开放环境完整性证明。", existing="Ch79 §‘先校准不确定性，再决定行动、询问或探索’已把 expected information gain、ask/explore cost、act/gather/defer 与 observed-outcome belief update 绑定，并保留预算上限和低置信回退；本项没有改变该长期控制结构。"),
    "2605.15309": dict(node="MULTIMODAL-GENERATIVE-PARADIGMS", path="books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", adjacent=["books/part-03-multimodal-world-models/23-multimodal-representation.md", "books/part-03-multimodal-world-models/25-multimodal-world-models.md"], score=score(2, 1, 2), decision="No Change — Existing Coverage", method="§3.2 Recursive Token Mapper; Appendix A algorithm", evaluation="§4.1-4.4 CIFAR/CelebA/StyleGAN and refinement-step analysis", limitation="§5 Limitations and Future Work; Appendix F training stability", contribution="单次 latent mapping 即使 FID 低也可能牺牲 mode coverage；递归 token mapper 允许推理时增加 refinement cycles 并用 precision/recall 分离 fidelity/coverage，因此需要核验生成范式是否已把 refinement depth 作为可变状态。", delta="同一 mapper 递归 H/L cycles，推理 refinement 数可独立于训练设置变化；结果限 IMLE/StyleGAN 与所测图像数据，不证明无限递归稳定。", existing="Ch24 已把 serial dimension 从 output length 改为 refinement steps，并明确 mutable provisional state、repeated revision、commit gate、训练分布与 runtime budget；本项是该机制在 IMLE mapper 的受限实现。"),
    "2605.15458": dict(node="MULTIMODAL-GENERATIVE-PARADIGMS", path="books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md", adjacent=["books/part-03-multimodal-world-models/23-multimodal-representation.md", "books/part-03-multimodal-world-models/25-multimodal-world-models.md"], score=score(2, 2, 2), decision="Integrate", method="§4.1 SDE-GRPO; §4.2 early-step focus; §4.3 verifiable reward", evaluation="§5.1-5.4 experiments/OOD; §6.1-6.3 ablation and reward analysis", limitation="§7 Conclusion; Appendix C.1 KL constraint", contribution="视频生成 RL 不能把语言模型 token-level GRPO 直接搬到 SDE trajectory；SDE-GRPO、可验证 puzzle reward 和 early-step focus 把 credit 与扩散早期全局结构绑定，因此需要重考虑 video generator 的 RLVR state 与 budget。", delta="对 video diffusion/flow trajectory 使用 SDE-GRPO，并把 compute 聚焦到决定全局结构的早期 steps；reward 仅覆盖可程序验证的 maze/FlowFree/Sokoban 条件，不能外推开放视频语义或真实 latency。", existing="Ch24 已管理 refinement trajectory 与 step budget，Ch33 已管理 verifiable reward，但当前 owner 尚未连接 video SDE trajectory、early-step credit 与 verifiable visual reasoning reward。"),
    "2605.15217": dict(node="PLATFORM-EVALUATION-SYSTEM", path="books/part-06-ai-infrastructure/66-evaluation-system.md", adjacent=["books/part-06-ai-infrastructure/65-kai-scheduler.md", "books/part-06-ai-infrastructure/67-monitoring.md"], score=score(3, 2, 3), decision="No Change — Existing Coverage", method="§2.3-2.8 behavioral tests, representations and steering interventions", evaluation="§3.1-3.8 behavioral parity, representation divergence and intervention results", limitation="§5 Limitations; Appendix A.4 cross-model replication", contribution="输出层公平不代表内部 demographic signal 无决策因果力；跨层 activation steering 可使被抑制表示重新改变决策，因此需要重考虑 fairness release gate 是否必须同时包含 output behavior、decodability 与 causal intervention。", delta="matched mortgage prompts 显示 output parity 与 latent divergence 并存，跨层 steering 暴露方向不对称的因果敏感性；证据限三类开源模型、该决策任务与 intervention design。", existing="Ch66 已明确 internal representation 可解码不等于 causal use，并要求 decodability、intervention 与 output behavior 分层；现有 activation failure probe note 也保留模型/任务/线性配置边界，已承载 dual-layer diagnostic ladder。"),
    "2605.15248": dict(node="PLATFORM-SECURITY", path="books/part-06-ai-infrastructure/72-security.md", adjacent=["books/part-06-ai-infrastructure/71-multi-tenant.md", "books/part-06-ai-infrastructure/73-production-best-practice.md"], score=score(2, 2, 2), decision="Integrate", method="§4 Privacy Leakage Pipeline; §5 Privacy Feature Library", evaluation="§6.1-6.2 experiments; Appendix D validation", limitation="Limitation; Ethics Consideration; Appendix A.2 comparison protocol", contribution="ad-hoc privacy prompts 不能逼近 PII 在代码 corpus 中的真实使用形态；以 code scenario 生成函数再从 tests 中验证泄漏、并用自动 feature library 提供模板，改变了 code-LLM memorization audit 的 attack surface，因此需要重考虑 privacy red-team 的输入生成合同。", delta="scenario→code question→generated function→test cases 的 pipeline 用 feature library 替代手工 prompt，检测率提升仅证明五个所测模型和 judge/validation protocol；它不证明未命中即无泄漏。", existing="Ch72 已覆盖 PII/memorization、targeted extraction 与未命中非删除证明，但没有 test-generation 作为 realistic code-context elicitation，以及 feature-library/version identity。"),
    "2605.15298": dict(node="MULTIMODAL-EMBODIED-VLA", path="books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md", adjacent=["books/part-03-multimodal-world-models/25-multimodal-world-models.md", "books/part-04-training-system/27-data.md"], score=score(2, 3, 2), decision="No Change — Existing Coverage", method="§2 data engine; §3.3-3.6 preservation, language alignment and robot adaptation", evaluation="§4 VLM/VLA simulation; §5 real-world experiments", limitation="§6 Discussion; §7 Conclusion", contribution="robot trajectory coverage有限时，可先将 human egocentric video 编译成 scene/dynamics/depth/affordance 的 structured physical supervision，再以 capability-preserving adaptation 迁移到 VLA，因此需要核验 Books 是否已拥有 human-video breadth 到 typed action alignment 的分层数据路线。", delta="human video 先成为 structured physical QA prior，再通过 language-sensitive adaptation 进入 VLA；SOTA 结果限披露 benchmark，不能证明物理 truth、未见 embodiment 或闭环安全。", existing="Ch26 §‘数据演进：从专用演示到多来源对齐’已明确 human video 没有原生 robot action，需 derived state-transition/trajectory labels、embodiment/action-schema alignment、provenance 与 closed-loop validation，足以承载本项长期链路。"),
    "2605.15734": dict(node="PLATFORM-EVALUATION-SYSTEM", path="books/part-06-ai-infrastructure/66-evaluation-system.md", adjacent=["books/part-06-ai-infrastructure/65-kai-scheduler.md", "books/part-06-ai-infrastructure/67-monitoring.md"], score=score(2, 1, 2), decision="No Change — Existing Coverage", method="§4 Study Design and Descriptions of Experiments", evaluation="§5 Results; individual-score versus aggregate reliability across three bimodal LLMs", limitation="§6 Discussion; §7 Limitations and Further Research", contribution="聚合后稳定的 inferred user-state metric 不能自动支持个体实时 adaptation；三种 bimodal LLM 的重复测量仅 31/213 指标达到标准，因此 evaluation 必须分别验收 individual reliability 与 post-hoc aggregate utility。", delta="同一 metric 的 individual repeatability 与 aggregate analytical utility必须分别判定；证据只覆盖论文定义的 213 metrics、三模型与 replication protocol。", existing="Ch66 已要求 repeated sampling、within-model reliable-change interval、sampling variance 与 item-level harmed/helped ledger，并把 construct、slice、calibration 和 evaluator identity 分开；本项没有改变该 evaluation contract。"),
}


CLOSE = {
    "2605.15638": "ITHICA 研究通用 CPU 制造缺陷的 intra-thread instruction duplication/output comparison；题摘没有把 AI model/training/inference workload 作为对象，也没有修正 AI infrastructure 特有的 fault/recovery 选择，故其 datacenter 语境不足以通过本项目贡献筛选。",
    "2605.16194": "paper.json v1 只验证其 JSON 与论文文本的一致性；stable claim ID、does-not-claim list 与 per-figure command 对 agent 引用准确性、范围控制或复现成功率均明确仍是 open invitation，未提供足以改变 Agent/研究基础设施设计的结果或反证。",
}


CURRENT_LOCATORS = {
    "2605.15208": ("§IV empirical case study; §IV-B setup", "§IV-C.1-C.6 results and regression", "§V Discussion and Limitations"),
    "2605.15215": ("§3.1-3.5 skill compiler, ABI and deoptimization", "§4.1-4.5 runtime, model and harness evaluation", "§4.6 Limitations; Appendix B.3 reproducibility"),
    "2605.15228": ("§3.2 pipeline; §3.4 invariants; §4-7 proof/consensus/identity/evidence", "§8 evaluation and replay examples", "§3.3 threat assumptions; §5.3 failure handling"),
}

ORIGINAL_REUSE_IDS = """2605.15204 2605.15508 2605.15514 2605.15520 2605.15529 2605.15565 2605.15573 2605.15581 2605.15609 2605.15617 2605.15618 2605.15638 2605.15648 2605.15665 2605.15694 2605.15710 2605.15734 2605.15761 2605.15777 2605.15815 2605.15846 2605.15957 2605.15960 2605.15967 2605.16035 2605.16154 2605.16184 2605.16194 2605.16198 2605.16217 2605.16007 2605.16234 2605.16255 2605.15206 2605.15208 2605.15215 2605.15207 2605.15228""".split()


def sha(path: str) -> str:
    return hashlib.sha256((REPO / path).read_bytes()).hexdigest()


def json_load(path: Path):
    return json.loads(path.read_text())


def json_text(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def patch_update(path: Path, new_text: str) -> str:
    old_text = path.read_text()
    if old_text == new_text:
        return ""
    rel = path.relative_to(REPO)
    diff = list(difflib.unified_diff(old_text.splitlines(), new_text.splitlines(), n=20, lineterm=""))[2:]
    # The repository apply_patch dialect uses bare @@ section markers rather
    # than unified-diff line coordinates.
    diff = ["@@" if line.startswith("@@") else line for line in diff]
    return "*** Begin Patch\n*** Update File: " + str(rel) + "\n" + "\n".join(diff) + "\n*** End Patch\n"


def patch_add(rel: str, text: str) -> str:
    return "*** Begin Patch\n*** Add File: " + rel + "\n" + "\n".join("+" + line for line in text.splitlines()) + "\n*** End Patch\n"


def indented_object(value: dict, spaces: int, comma: bool) -> list[str]:
    lines = json.dumps(value, ensure_ascii=False, indent=2).splitlines()
    lines = [(" " * spaces) + line for line in lines]
    if comma:
        lines[-1] += ","
    return lines


def patch_object(path: Path, old: dict, new: dict | None, spaces: int, comma: bool) -> str:
    rel = path.relative_to(REPO)
    old_lines = indented_object(old, spaces, comma)
    new_lines = [] if new is None else indented_object(new, spaces, comma)
    body = ["@@"] + ["-" + line for line in old_lines] + ["+" + line for line in new_lines]
    return "*** Begin Patch\n*** Update File: " + str(rel) + "\n" + "\n".join(body) + "\n*** End Patch\n"


def patch_append_array(path: Path, last: dict, additions: list[dict]) -> str:
    rel = path.relative_to(REPO)
    old_lines = indented_object(last, 2, False)
    new_lines = indented_object(last, 2, True)
    for index, value in enumerate(additions):
        new_lines.extend(indented_object(value, 2, index < len(additions) - 1))
    body = ["@@"] + ["-" + line for line in old_lines] + ["+" + line for line in new_lines]
    return "*** Begin Patch\n*** Update File: " + str(rel) + "\n" + "\n".join(body) + "\n*** End Patch\n"


def review_text(row: dict, d: dict) -> str:
    sf = row["source_family_id"]
    title = row["title"]
    return f"""### [{title}](https://arxiv.org/html/{row['arxiv_id']}v1)

<!-- review:{sf}:start -->
- **Contribution screen:** {d['contribution']}
- **Mechanism:** {d['delta']}
- **Evaluation boundary:** exact-v1 摘要结果与 `{d['evaluation']}` 只支持作者披露的模型、数据、hardware、seed 与 evaluator；未披露条件为 `Not Disclosed`，不外推 production SLO。
- **Counterevidence / non-proof:** `{d['limitation']}`；局部实验不建立跨 workload 定律，旧路径在新增约束不存在、校准失败或成本过高时继续成立。
- **Exact-v1 locators:** Method=`arXiv:{row['arxiv_id']}v1 — {d['method']}`；Evaluation=`arXiv:{row['arxiv_id']}v1 — {d['evaluation']}`；Limitations=`arXiv:{row['arxiv_id']}v1 — {d['limitation']}`。
- **Primary:** [arXiv:{row['arxiv_id']}v1](https://arxiv.org/html/{row['arxiv_id']}v1)。
- **Books:** `{d['decision']}` → `{d['node']}`；作者侧未写共享 Books。
<!-- claim:{sf}:start -->{d['delta']}<!-- claim:{sf}:end -->
<!-- review:{sf}:end -->"""


def comparison(row: dict, d: dict) -> dict:
    sf = row["source_family_id"]
    txt = (
        f"<!-- existing:{sf}:start -->当前对读 `{d['path']}` 与相邻章节后：{d['existing']} "
        f"Owner snapshot sha256=`{sha(d['path'])}`。<!-- existing:{sf}:end -->\n"
        f"<!-- delta:{sf}:start -->Exact-v1 新增：{d['delta']} Decision=`{d['decision']}`；"
        f"作者侧不写共享 Books。<!-- delta:{sf}:end -->"
    )
    return {
        "source_family_id": sf,
        "stable_node_id": d["node"],
        "owner_path": d["path"],
        "adjacent_paths": d["adjacent"],
        "decision": d["decision"],
        "comparison_text": txt,
        "owner_sha256": sha(d["path"]),
        "adjacent_sha256": {p: sha(p) for p in d["adjacent"] if (REPO / p).exists()},
        "binding_markers": [],
        "binding_present": False,
        "reviewer": "author-bounded-repair:20260915",
    }


def build_structured():
    ledger_path = H / "screening-ledger-v3.json"
    old_ledger = json_load(ledger_path)
    ledger = json.loads(json.dumps(old_ledger))
    by_id = {r["arxiv_id"]: r for r in ledger["identities"]}
    for arxiv_id, reason in CLOSE.items():
        row = by_id[arxiv_id]
        row.update(screening_status="pre_denominator_closure", v3_screening_status="pre_denominator_closure", screening_reason=reason, review_status="identity_date_contribution_closed", integration_disposition="Rejected — Below Candidate Denominator", books_disposition="Rejected — Below Candidate Denominator")
        for key in ("score_v2", "stable_node_id", "evidence_route"):
            row.pop(key, None)
    for arxiv_id, d in DECISIONS.items():
        row = by_id[arxiv_id]
        row.update(screening_status="retained", v3_screening_status="retained", screening_reason=d["contribution"], review_status=("deep_complete_author_side" if d["decision"] == "Integrate" or d["score"]["total"] >= 7 or d["score"]["design_delta"] == 3 else "standard_complete_author_side"), integration_disposition=d["decision"], books_disposition=d["decision"], score_v2=d["score"], stable_node_id=d["node"])
        if arxiv_id != "2605.15734":
            row["evidence_route"] = "current_exact_v1_review_20260915"
    ledger.update(candidate_denominator=64, pre_denominator_closure_count=473, owner_evidence="papers/2026/05/_sources/daily-20260518/official-owner-batch-evidence-v3.json")
    assert len(ledger["identities"]) == 537
    assert sum(r["v3_screening_status"] == "retained" for r in ledger["identities"]) == 64
    assert sum(r["v3_screening_status"] != "retained" for r in ledger["identities"]) == 473

    ev_path = H / "evidence-review-v3.json"
    old_evidence_list = json_load(ev_path)
    old_evidence = {r["arxiv_id"]: r for r in old_evidence_list}
    evidence = []
    for old in old_evidence_list:
        arxiv_id = old["arxiv_id"]
        if arxiv_id in CLOSE:
            continue
        if arxiv_id not in DECISIONS:
            evidence.append(dict(old))
            continue
        d = DECISIONS[arxiv_id]
        row = by_id[arxiv_id]
        ev = dict(old)
        ev.update(source_family_id=row["source_family_id"], arxiv_id=arxiv_id, primary_identifier=f"arXiv:{arxiv_id}v1", evidence_route=("reused_with_replayable_original_evidence" if arxiv_id == "2605.15734" else "current_exact_v1_review_20260915"), identity_unchanged=True, exact_version_unchanged=True, adopted_claim_unchanged=True, withdrawal_signal="No withdrawal/correction signal used; the adopted evidence is the immutable official exact-v1.", score_v2=d["score"], stable_node_id=d["node"], review_status=("deep_complete_author_side" if d["decision"] == "Integrate" or d["score"]["total"] >= 7 or d["score"]["design_delta"] == 3 else "standard_complete_author_side"), method_identity_locators=f"arXiv:{arxiv_id}v1 — {d['method']}", evaluation_locators=f"arXiv:{arxiv_id}v1 — {d['evaluation']}", limitations_counterevidence_locators=f"arXiv:{arxiv_id}v1 — {d['limitation']}", artifact_locators=f"https://arxiv.org/html/{arxiv_id}v1; separate immutable code commit Not Disclosed", claim_boundary=d["delta"], review_text=review_text(row, d))
        evidence.append(ev)
    for arxiv_id, d in DECISIONS.items():
        if arxiv_id in old_evidence:
            continue
        row = by_id[arxiv_id]
        evidence.append({"source_family_id": row["source_family_id"], "arxiv_id": arxiv_id, "primary_identifier": f"arXiv:{arxiv_id}v1", "evidence_route": "current_exact_v1_review_20260915", "identity_unchanged": True, "exact_version_unchanged": True, "adopted_claim_unchanged": True, "withdrawal_signal": "No withdrawal/correction signal used; the adopted evidence is the immutable official exact-v1.", "score_v2": d["score"], "stable_node_id": d["node"], "review_status": ("deep_complete_author_side" if d["decision"] == "Integrate" or d["score"]["total"] >= 7 or d["score"]["design_delta"] == 3 else "standard_complete_author_side"), "method_identity_locators": f"arXiv:{arxiv_id}v1 — {d['method']}", "evaluation_locators": f"arXiv:{arxiv_id}v1 — {d['evaluation']}", "limitations_counterevidence_locators": f"arXiv:{arxiv_id}v1 — {d['limitation']}", "artifact_locators": f"https://arxiv.org/html/{arxiv_id}v1; separate immutable code commit Not Disclosed", "claim_boundary": d["delta"], "review_text": review_text(row, d)})
    for ev in evidence:
        if ev["arxiv_id"] in CURRENT_LOCATORS:
            m, e, l = CURRENT_LOCATORS[ev["arxiv_id"]]
            ev.update(evidence_route="current_exact_v1_review_20260915", method_identity_locators=f"arXiv:{ev['arxiv_id']}v1 — {m}", evaluation_locators=f"arXiv:{ev['arxiv_id']}v1 — {e}", limitations_counterevidence_locators=f"arXiv:{ev['arxiv_id']}v1 — {l}", artifact_locators=f"https://arxiv.org/html/{ev['arxiv_id']}v1; current exact-v1 headings rechecked 2026-09-15")
    assert len(evidence) == 64
    assert sum(r["evidence_route"] == "reused_with_replayable_original_evidence" or r["evidence_route"] == "reused_identity_version_claim_unchanged" for r in evidence) == 33

    books_path = H / "books-comparison-v3.json"
    old_books = json_load(books_path)
    books = []
    for old in old_books:
        sf = old.get("source_family_id", "")
        arxiv_id = next((x for x in CLOSE if x.replace(".", "-") in sf), None)
        if arxiv_id:
            continue
        decision_id = next((x for x in DECISIONS if x.replace(".", "-") in sf), None)
        books.append(comparison(by_id[decision_id], DECISIONS[decision_id]) if decision_id else old)
    for arxiv_id, d in DECISIONS.items():
        if not any(arxiv_id.replace(".", "-") in r.get("source_family_id", "") for r in old_books):
            books.append(comparison(by_id[arxiv_id], d))
    assert len(books) == 64
    assert sum(r["decision"] == "Integrate" for r in books) == 31
    assert sum(r["decision"] == "No Change — Existing Coverage" for r in books) == 33

    queue_path = H / "root-books-writeback-queue-v3.json"
    old_queue = json_load(queue_path)
    queue = json.loads(json.dumps(old_queue))
    queue["items"] = [r for r in queue["items"] if r.get("arxiv_id") not in CLOSE and r.get("arxiv_id") not in DECISIONS]
    for arxiv_id, d in DECISIONS.items():
        if d["decision"] != "Integrate":
            continue
        row = by_id[arxiv_id]
        queue["items"].append({"source_family_id": row["source_family_id"], "arxiv_id": arxiv_id, "stable_node_id": d["node"], "owner_path": d["path"], "status": "requires_root_integration", "binding_markers": [], "author_instruction": f"Integrate only the reviewed delta into the existing mechanism spine: {d['delta']} Preserve old-path conditions, exact-v1 boundary and fallback; author lane did not modify Books."})
    queue["status"] = "bounded_repair_requires_root_books_actions_and_fresh_review"
    assert len(queue["items"]) == 31

    recon_path = H / "owner-reconciliation-v3.json"
    recon = json_load(recon_path)
    retained = [r["source_family_id"] for r in ledger["identities"] if r["v3_screening_status"] == "retained"]
    recon["current_owner_window"].update(candidate_count=64, candidate_source_families=retained, pre_denominator_closure_count=473, strict_batch_evidence="papers/2026/05/_sources/daily-20260518/official-owner-batch-evidence-v3.json")

    target = sys.argv[2] if len(sys.argv) > 2 else None
    if not target or target == ledger_path.name:
        top_old = {k: old_ledger[k] for k in ("owner_evidence", "raw_identity_count", "candidate_denominator", "pre_denominator_closure_count", "withdrawn_count")}
        top_new = {k: ledger[k] for k in top_old}
        top_patch = "*** Begin Patch\n*** Update File: " + str(ledger_path.relative_to(REPO)) + "\n@@\n" + "\n".join("-  \"%s\": %s%s" % (k, json.dumps(v, ensure_ascii=False), "," if k != "withdrawn_count" else ",") for k, v in top_old.items()) + "\n" + "\n".join("+  \"%s\": %s%s" % (k, json.dumps(v, ensure_ascii=False), "," if k != "withdrawn_count" else ",") for k, v in top_new.items()) + "\n*** End Patch\n"
        print(top_patch, end="")
        old_rows = {r["arxiv_id"]: r for r in old_ledger["identities"]}
        new_rows = {r["arxiv_id"]: r for r in ledger["identities"]}
        for arxiv_id in list(CLOSE) + list(DECISIONS):
            print(patch_object(ledger_path, old_rows[arxiv_id], new_rows[arxiv_id], 4, arxiv_id != old_ledger["identities"][-1]["arxiv_id"]), end="")
    if not target or target == ev_path.name:
        old_map = {r["arxiv_id"]: r for r in old_evidence_list}
        new_map = {r["arxiv_id"]: r for r in evidence}
        for index, old in enumerate(old_evidence_list):
            arxiv_id = old["arxiv_id"]
            if arxiv_id in CLOSE or old != new_map.get(arxiv_id):
                print(patch_object(ev_path, old, new_map.get(arxiv_id), 2, index < len(old_evidence_list) - 1), end="")
        additions = [r for r in evidence if r["arxiv_id"] not in old_map]
        last_for_append = new_map.get(old_evidence_list[-1]["arxiv_id"], old_evidence_list[-1])
        if additions:
            print(patch_append_array(ev_path, last_for_append, additions), end="")
    if not target or target == books_path.name:
        old_map = {r["source_family_id"]: r for r in old_books}
        new_map = {r["source_family_id"]: r for r in books}
        for index, old in enumerate(old_books):
            sf = old["source_family_id"]
            if old != new_map.get(sf):
                print(patch_object(books_path, old, new_map.get(sf), 2, index < len(old_books) - 1), end="")
        additions = [r for r in books if r["source_family_id"] not in old_map]
        last_for_append = new_map.get(old_books[-1]["source_family_id"], old_books[-1])
        if additions:
            print(patch_append_array(books_path, last_for_append, additions), end="")
    if not target or target == queue_path.name:
        print(patch_update(queue_path, json_text(queue)), end="")
    if not target or target == recon_path.name:
        print(patch_update(recon_path, json_text(recon)), end="")


def build_reuse_manifest() -> list[dict]:
    current = {r["arxiv_id"]: r for r in json_load(H / "evidence-review-v3.json")}
    day16_path = REPO / "papers/2026/05/_sources/daily-20260516/exact-v1-review-packet.json"
    day16 = {r["arxiv_id"]: r for r in json_load(day16_path)}
    day02_path = REPO / "papers/2026/05/_sources/daily-20260502/exact-v1-review-packet.json"
    day02 = {re.search(r"(2605\.\d+)", r["primary_evidence_version"]).group(1): r for r in json_load(day02_path)["reviews"] if re.search(r"(2605\.\d+)", r["primary_evidence_version"])}
    original_ids = ORIGINAL_REUSE_IDS
    result = []
    for arxiv_id in original_ids:
        cur = current.get(arxiv_id)
        if arxiv_id in day16:
            o = day16[arxiv_id]
            source = str(day16_path.relative_to(REPO))
            original = {"version": o["primary_evidence_version"], "method": o["method_locator"], "evaluation": o["evaluation_locator"], "limitations": o["limitations_locator"], "claim_contract": {k: o.get(k) for k in ("problem_and_changed_constraint", "mechanism_and_ownership", "evaluation_contract", "proof_boundary", "tradeoff_and_failure_mode", "old_path_and_coexistence")}, "receipt": o.get("retrieval")}
        elif arxiv_id in day02:
            o = day02[arxiv_id]
            source = str(day02_path.relative_to(REPO))
            original = {"version": o["primary_evidence_version"], "method": o["method_identity_locators"], "evaluation": o["evaluation_locators"], "limitations": o["limitations_counterevidence_locators"], "claim_contract": o["claim_boundary"], "receipt": {"exact_v1_url": o["exact_v1_url"], "artifact": o.get("artifact_locators")}}
        elif arxiv_id == "2605.15204":
            source = "papers/2026/05/_sources/arxiv-owner-replay-20260903/20260518/canonical-ledger.json"
            original = {"version": "arXiv:2605.15204v1", "method": "§3 System Architecture; §3.2 GoalStage Finite Automaton; §3.6 StateAwareDispatch", "evaluation": "§5.1-5.13 Experiments", "limitations": "§6 Discussion; §5.11 Error Analysis", "claim_contract": cur.get("claim_boundary"), "receipt": {"path": "papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.15204v1.html.html", "sha256": sha("papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.15204v1.html.html")}}
        elif arxiv_id in CURRENT_LOCATORS:
            m, e, l = CURRENT_LOCATORS[arxiv_id]
            source = "current exact-v1 recheck 2026-09-15"
            original = {"version": f"arXiv:{arxiv_id}v1", "method": m, "evaluation": e, "limitations": l, "claim_contract": cur.get("claim_boundary"), "receipt": {"exact_v1_url": f"https://arxiv.org/html/{arxiv_id}v1"}}
        else:
            raise AssertionError(f"missing original evidence for {arxiv_id}")
        if arxiv_id in CLOSE:
            resolution = "candidate_removed_after_contribution_recheck"
            adopted = "none; evidence retained only as audit history"
        elif arxiv_id in CURRENT_LOCATORS:
            resolution = "current_exact_v1_rechecked"
            adopted = cur.get("claim_boundary")
        else:
            resolution = "original_exact_v1_locator_replayed; version and adopted semantic boundary unchanged"
            adopted = cur.get("claim_boundary")
        item = {"arxiv_id": arxiv_id, "source_family_id": cur.get("source_family_id") if cur else f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}", "original_review_artifact": source, "original_evidence": original, "v3_adopted_claim": adopted, "comparison_result": resolution, "replayed_at": "2026-09-15T18:40:00+08:00"}
        if arxiv_id in CURRENT_LOCATORS:
            m, e, l = CURRENT_LOCATORS[arxiv_id]
            item["current_exact_v1_recheck"] = {"url": f"https://arxiv.org/html/{arxiv_id}v1", "method": m, "evaluation": e, "limitations": l}
        result.append(item)
    assert len(result) == 38
    return result


def build_newfiles():
    ledger = json_load(H / "screening-ledger-v3.json")
    nums = [int(r["arxiv_id"].split(".")[1]) for r in ledger["identities"]]
    batch = {
        "schema": "official-arxiv-owner-batch-evidence-v3",
        "report_date": "2026-05-18",
        "strict_window": "[2026-05-17T09:00:00+08:00,2026-05-18T09:00:00+08:00)",
        "official_policy": {
            "availability_url": "https://info.arxiv.org/help/availability.html",
            "identifier_url": "https://info.arxiv.org/help/arxiv_identifier.html",
            "replay_statement": "arXiv states that submissions become public in scheduled announcements and that the final identifier is assigned in that announcement process; identifiers use a month-local sequence number.",
            "schedule": "Thursday 14:00 through Friday 14:00 Eastern US submissions are announced Sunday 20:00 Eastern US.",
        },
        "time_conversion": {"announcement_eastern": "2026-05-17T20:00:00-04:00", "announcement_utc": "2026-05-18T00:00:00Z", "announcement_asia_shanghai": "2026-05-18T08:00:00+08:00", "strict_cutoff_asia_shanghai": "2026-05-18T09:00:00+08:00", "inside_window": True},
        "official_oai_boundary_probes": [
            {"id": "2605.15201", "url": "https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2605.15201&metadataPrefix=arXivRaw", "current_datestamp": "2026-05-15", "role": "preceding boundary"},
            {"id": "2605.15202", "url": "https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2605.15202&metadataPrefix=arXivRaw", "current_datestamp": "2026-05-18", "role": "first batch boundary"},
            {"id": "2605.16257", "url": "https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2605.16257&metadataPrefix=arXivRaw", "current_datestamp": "2026-05-18", "role": "last non-revised witness before upper boundary"},
            {"id": "2605.16258", "url": "https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2605.16258&metadataPrefix=arXivRaw", "current_datestamp": "2026-05-22", "role": "batch endpoint whose current OAI datestamp moved after revision; placement follows official identifier sequence, not current datestamp"},
            {"id": "2605.16259", "url": "https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2605.16259&metadataPrefix=arXivRaw", "current_datestamp": "2026-05-19", "role": "following boundary"},
        ],
        "batch_interval": {"first_id": "2605.15202", "last_id": "2605.16258", "all_category_identity_count": 1057, "derivation": "inclusive month-sequence interval", "covered_category_subset_count": 537},
        "ledger_membership_check": {"ledger": "papers/2026/05/_sources/daily-20260518/screening-ledger-v3.json", "identity_count": len(nums), "min_sequence": min(nums), "max_sequence": max(nums), "outside_interval_count": sum(n < 15202 or n > 16258 for n in nums)},
        "conclusion": "All 537 registered covered-category identities belong to the official Sunday 20:00 Eastern announcement batch, which was public at 08:00 Asia/Shanghai and therefore before the strict 09:00 cutoff.",
        "datacite_role": "Identity/DOI corroboration only. DataCite created/updated timestamps are not used as arXiv publication or cutoff timestamps.",
        "known_limitation": "Current OAI datestamps move when records are revised; revised members are assigned to the batch by the official announcement-time identifier allocation and continuous month-sequence boundaries, not by a later current datestamp.",
    }
    reuse = {"schema": "evidence-reuse-replay-v3", "report_date": "2026-05-18", "original_reuse_count": 38, "final_resolution": {"historical_locator_replay": 33, "current_exact_v1_recheck": 3, "candidate_removed": 2}, "items": build_reuse_manifest()}
    note_lines = [
        "# 2026-05-18 作者有界返修（2026-09-15）", "", "**状态：Ongoing；作者不得自签 Complete。**", "", "本次只处理 fresh non-author V3 终审列出的 owner-time、18 个 FN/signal、3 个 FP/score 与 38 个 reuse locator；未扩窗、扩源或重扫 537 条题摘。", "", "## 冻结算术", "", "- owner inventory：`537 = 64 retained + 473 pre-denominator closure + 0 withdrawn`。", "- Evidence：`64 = 31 current exact-v1 + 33 replayable historical exact-v1`；原 38 reuse 的处置为 `33 historical replay + 3 current exact-v1 recheck + 2 removed candidates`。", "- Books Decision：`64 = 31 Integrate + 33 No Change — Existing Coverage`。", "- root queue：31 项，仅列真实 `Integrate`；作者侧未修改共享 Books。", "", "## 有界重审", "", "18 个审计指定 FN/signal 均重新读取完整题名与摘要，并以合同的贡献问题逐项判定；18 项均有题摘直接支持的机制、适用边界、评价纠错或设计分支，故进入 denominator。其 score、exact-v1 locator 与 Books 对读见本目录三个 V3 冻结 JSON。", "", "`2605.15638` 移出分母：唯一 Books binding 为 `books/part-06-ai-infrastructure/67-monitoring.md:397`，唯一由该 source family 支撑的正文是当前第 393 与 395 段；root 必须删除或改写这两段并移除 binding，作者没有改 Books。`2605.16194` 同样移出分母。`2605.15734` 保留但降为 `2+1+2=5`，执行标准审阅并维持 Existing Coverage。", "", "## 材料限制", "", "无阻断本次判断的材料缺口。38 项均有可重放历史 locator/version/claim，或已完成当前 official exact-v1 定点复核；批量 current-abstract 状态探测中 `2605.15508`、`2605.15665`、`2605.15694`、`2605.16035`、`2605.16255`、`2605.15215` 曾超时，但这些探测不用于采用命题，immutable exact-v1 与历史 receipt 均可重放，因此未静默阻塞。", "", "## 剩余外部动作", "", "root 执行 31 项 Books queue，并删除/修订 ITHICA 唯一正文 binding；之后必须由非作者重新核对 owner-time、18 项准入、Evidence replay 和实际 Books 承载。机器校验通过不能替代该复核。", ""
    ]
    print(patch_add("papers/2026/05/_sources/daily-20260518/official-owner-batch-evidence-v3.json", json_text(batch)), end="")
    print(patch_add("papers/2026/05/_sources/daily-20260518/evidence-reuse-replay-v3.json", json_text(reuse)), end="")
    print(patch_add("papers/2026/05/_sources/daily-20260518/AUTHOR_BOUNDED_REPAIR_20260915.md", "\n".join(note_lines)), end="")


def remove_review_block(text: str, arxiv_id: str) -> str:
    pat = re.compile(rf"\n### \[[^\n]+\]\(https://arxiv\.org/html/{re.escape(arxiv_id)}v1\)\n.*?(?=\n### \[|\n### Books 对读)", re.S)
    return pat.sub("", text, count=1)


def build_report():
    ledger = json_load(H / "screening-ledger-v3.json")
    evidence = {r["arxiv_id"]: r for r in json_load(H / "evidence-review-v3.json")}
    books = {r["source_family_id"]: r for r in json_load(H / "books-comparison-v3.json")}
    by_id = {r["arxiv_id"]: r for r in ledger["identities"]}
    text = REPORT.read_text()
    text = re.sub(r"\*\*检查时间：\*\* .*", "**检查时间：** 2026-09-15T18:40:00+08:00", text, count=1)
    summary_start = text.index("## 1. 结论")
    coverage_start = text.index("## 2. 来源覆盖")
    summary = """## 1. 结论

旧 submission-window ledger 的 324 个 identity 与 52 个候选仍不属于本日 owner。当前 537 个 identity 经严格有界返修后冻结为 `537 = 64 retained + 473 pre-denominator closure + 0 withdrawn`；本轮只定点重审终审指定的 18 个 FN/signal 与 3 个 FP/score，没有重扫其余 closure。

owner-time 由 arXiv 官方 announcement schedule、announcement-time ID allocation、月内连续序号及 OAI 边界共同证明：本批在 2026-05-17 20:00 美东（2026-05-18 08:00 北京）公开，早于 09:00 截点。DataCite 仅作 identity/DOI 佐证，不作发布时间。

64 项 Evidence 已冻结为 `31 current exact-v1 + 33 replayable historical exact-v1`；原 38 reuse 逐项落为 `33 historical replay + 3 current exact-v1 recheck + 2 candidates removed`。Books Decision 为 `31 Integrate + 33 No Change`。作者侧未修改共享 Books，31 个真实 Integrate 已进入 root queue；报告保持 Ongoing，等待 root 写回与新的非作者语义复核。

"""
    text = text[:summary_start] + summary + text[coverage_start:]
    text = text.replace("current owner replay：537 个官方当日 listing identity，逐项题名+摘要裁决；48 retained、489 pre-denominator closure、0 withdrawn；旧 324/52 submission-window 集合不再拥有本日", "official announcement-batch replay：537 个 covered-category identity 全部落在 2605.15202–2605.16258；64 retained、473 pre-denominator closure、0 withdrawn；announcement=2026-05-18 08:00+08，旧 324/52 submission-window 集合不再拥有本日")
    text = text.replace("公开归属绑定 05-18 官方 listing batch；DataCite created/updated 不单独充当 09:00 cutoff 时刻", "无；官方批次证据见 official-owner-batch-evidence-v3.json，DataCite 不充当 cutoff 时刻")
    text = text.replace("完整 identity、分页/路由与逐项理由见 [`screening-ledger-v3.json`](../_sources/daily-20260518/screening-ledger-v3.json)；", "完整 identity、分页/路由与逐项理由见 [`screening-ledger-v3.json`](../_sources/daily-20260518/screening-ledger-v3.json)，严格批次证明见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260518/official-owner-batch-evidence-v3.json)；")

    table_start = text.index("| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |")
    table_end = text.index("\n\n## 4. 证据与知识整合", table_start)
    table = text[table_start:table_end].splitlines()
    table = [line for line in table if not any(arxiv_id in line for arxiv_id in CLOSE)]
    table = [line for line in table if "2605.15734v1" not in line]
    window = "2026-05-18T08:00:00+08:00"
    for arxiv_id in sorted(DECISIONS, key=lambda x: int(x.split(".")[1])):
        row, d = by_id[arxiv_id], DECISIONS[arxiv_id]
        outcome = "深入完成" if d["decision"] == "Integrate" or d["score"]["total"] >= 7 or d["score"]["design_delta"] == 3 else "标准完成"
        bd = "整合：待 root 写入并由非作者复核" if d["decision"] == "Integrate" else "已有覆盖：待非作者复核"
        rel = "../../../../" + d["path"]
        table.append(f"| [{row['title']}](https://arxiv.org/html/{arxiv_id}v1) | {window} | {d['contribution']}；{d['score']['design_delta']}+{d['score']['system_reach']}+{d['score']['durability']}={d['score']['total']} | {outcome} | {bd}；`{d['node']}` [章节]({rel}) |")
    text = text[:table_start] + "\n".join(table) + text[table_end:]
    text = text.replace("48 项的结构化 evidence route、精确版本、评分和 claim boundary", "64 项的结构化 evidence route、精确版本、评分和 claim boundary")
    text = text.replace("以下保留每项实际证据判断", "38 项 reuse 的逐项原 locator/version/claim 对照另见 [`evidence-reuse-replay-v3.json`](../_sources/daily-20260518/evidence-reuse-replay-v3.json)。以下保留每项实际证据判断")
    for arxiv_id in list(CLOSE) + ["2605.15734"]:
        text = remove_review_block(text, arxiv_id)
    insert = "\n\n".join(review_text(by_id[a], DECISIONS[a]) for a in sorted(DECISIONS))
    books_heading = text.index("\n### Books 对读")
    text = text[:books_heading] + "\n\n" + insert + text[books_heading:]
    for arxiv_id in list(CLOSE) + list(DECISIONS):
        sf = by_id[arxiv_id]["source_family_id"]
        text = re.sub(rf"\n?<!-- existing:{re.escape(sf)}:start -->.*?<!-- delta:{re.escape(sf)}:end -->", "", text, flags=re.S)
    compare_insert = "\n\n".join(books[by_id[a]["source_family_id"]]["comparison_text"] for a in DECISIONS)
    conclusion_marker = "结论：**No Change — Existing Coverage**。"
    if conclusion_marker in text:
        text = text.replace(conclusion_marker, compare_insert + "\n\n结论：**31 Integrate / 33 No Change；Integrate 仅进入 root queue，作者未写 Books。**", 1)
    for arxiv_id in CLOSE:
        text = re.sub(rf"^.*https://arxiv\.org/html/{re.escape(arxiv_id)}v1.*\n", "", text, flags=re.M)
    source_heading = "### 原始来源"
    source_pos = text.index(source_heading)
    gap_pos = text.index("## 5. 缺口与下一步", source_pos)
    source_add = "\n".join(f"- [{by_id[a]['title']}](https://arxiv.org/html/{a}v1) — `arXiv:{a}v1`" for a in sorted(DECISIONS) if a != "2605.15734")
    text = text[:gap_pos].rstrip() + "\n" + source_add + "\n\n" + text[gap_pos:]
    gap_start = text.index("## 5. 缺口与下一步")
    review_start = text.index("## 6. 复核", gap_start)
    gap = """## 5. 缺口与下一步

本轮材料 blocker：无。38 项 reuse 均已补历史 locator/version/claim replay，或转为 current exact-v1 定点复核；六个非必要 current-abstract 状态探测超时已在作者返修记录中精确列出，但 immutable exact-v1 与历史 receipt 均可重放，不阻断采用命题。

剩余动作只属于 root/非作者：

1. root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260518/root-books-writeback-queue-v3.json) 处理 31 个真实 Integrate，不重复写已有覆盖项。
2. `2605.15638` 已移出分母；其唯一 binding 为 `books/part-06-ai-infrastructure/67-monitoring.md:397`，唯一受影响正文为当前第 393、395 段，root 必须删除或改写并移除 binding。
3. root 完成 Books 后，由非作者重新核验 official batch 归属、18 项准入、64 项 Evidence、31/33 Books 决定和真实正文承载。

Meta GIM 的既有日级冲突仍作为独立隔离项，不用于本窗正面证据或 Books；本次没有扩源重查它。

"""
    text = text[:gap_start] + gap + text[review_start:]
    review_start = text.index("## 6. 复核")
    review = """## 6. 复核

复核者：`待新的非作者 fresh-context reviewer`

结论：**作者返修已完成；报告保持进行中，不自签 Complete。**

作者侧已复算 `537=64+473`、`64=31 current exact-v1+33 historical replay`、原 `38=33 replay+3 current recheck+2 removed`、`64=31 Integrate+33 No Change`，并生成仅含 31 个 Integrate 的 root queue。上一轮未通过结论保留在 [`FRESH_NONAUTHOR_V3_AUDIT_20260915.md`](../_sources/daily-20260518/FRESH_NONAUTHOR_V3_AUDIT_20260915.md)；本轮返修记录见 [`AUTHOR_BOUNDED_REPAIR_20260915.md`](../_sources/daily-20260518/AUTHOR_BOUNDED_REPAIR_20260915.md)。机器校验不能替代待执行的 Books 写回和非作者语义验收。
"""
    text = text[:review_start] + review
    print(patch_update(REPORT, text), end="")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "structured":
        build_structured()
    elif mode == "newfiles":
        build_newfiles()
    elif mode == "report":
        build_report()
    else:
        raise SystemExit("usage: apply_bounded_repair.py {structured [filename]|newfiles|report}")
