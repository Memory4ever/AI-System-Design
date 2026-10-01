# 2026-09-17 Evidence Notes

本文记录作者阶段的证据定位。所有论文均使用 arXiv v1；公开归属来自 2026-09-16 官方日批次，不用较早的 submitted 字段改写首次公开日。数值只用于限定作者实验，不外推为通用性能结论。

## 模型、训练与生成

- **2609.16179 — Z-Loss Backward Geometry**：阅读 backward transport、dense head/router reduction、实验与 limitations。贡献在于把 penalty 的 scalar value 与 logit source、transport gain、tied embedding、optimizer-facing update 分开；GPT-2/Pythia、WikiText-103/FineWeb-Edu 和 low-coefficient 结果不证明任意 MoE 配置稳定。
- **2609.16183 — Associative Recall in Fixed-State Recurrences**：阅读 matched-state protocol、factorial decomposition、interference/curriculum 与 guardrail。短 convolution 解释大部分表观架构差异，curriculum 可打破 sparse-supervision lock-in；结论只覆盖合成 recall/state-tracking，不等于通用语言建模排序。
- **2609.16450 — Early-Bird Decoding**：阅读 variable block predictor、position-aware sampler、三模型四 benchmark 与 ablation。机制是不改 base dLLM 权重而学习何时联合 unmask；吞吐数字依赖 block-cache、模型与 threshold，不能外推到 AR 模型。
- **2609.16540 — Importance of Gating**：阅读理论任务、multi-token/rule retrieval 和长短上下文实验。gating 抑制 memorization shortcut 并支持 ICL 的因果解释来自受控任务；不能直接推出生产模型所有长上下文能力由同一门控产生。
- **2609.16875 — Embedding Backward Compatibility**：阅读 problem setting、adapter、multi-level preservation loss 与实验。新旧 embedding 空间的双边兼容是迁移约束而非单个 recall 分数；结果局限于作者数据、backbone 与 adapter 容量。
- **2609.16937 — Temporal-Credit OPD**：阅读 token-local OPD 推导、discounted temporal credit、bounded mixing 与实验。它修正 imitation signal 与 sequence reward 的时间粒度错配；作者任务和 teacher/student 设置不能证明对所有 RLVR 稳定。
- **2609.17376 — Belief State Geometry**：同版本 HTML 不可用，阅读摘要、PDF 的 controlled HMM setup、linear probing 与 intervention。结果支持特定 HMM prompt 下的 belief-state subspace，并非现实语言上下文中通用 Bayesian optimality；因此只作标准审阅。
- **2609.17474 — Coupled Calibration and Learning**：阅读 token branching、source-only feedback 理论、收敛条件与 direct matching separation。它提供 teacher bias/covariate shift 的条件性替代分支；主要证据是理论设定，尚未成为生产 distillation 结论，故未进入最终候选表。

## 推理、执行与平台

- **2609.16244 — World Model Hardware Accelerator**：HTML 转换不完整，结合 v1 PDF 阅读 microarchitecture、VLIW/dual-dot/online softmax、UVM semantic trajectory test 与 sky130 synthesis。23× MSE reduction 是 device acceptance，不等于生成质量或商业制程性能；full-chip P&R 未完成。
- **2609.16617 — Divergence Timing and Cumulative Disagreement under KV-Cache Eviction**：HTML 不可用，阅读 v1 PDF 中首次 divergence、累积 disagreement 分解与合成/模型实验；它是评价 contract 的补充，不提供新的 eviction policy，按标准审阅。
- **2609.16682 — DeepShare**：阅读 cluster trace、DRA、predictive preemption、interference colocation、implementation 与 ablation。assurance 同时约束 entitlement、可回收共享与性能干扰；作者集群/预测器不能证明跨 workload 公平性。
- **2609.16898 — OptiPrime**：阅读 threat model、HE/MPC encoding、automorphism/communication、memory-aware co-design 与 hardware evaluation。其结论是 protocol 与 memory/accelerator 的耦合边界，延迟/通信收益不外推到不同 threat model 或网络。
- **2609.17008 — FlexEE**：阅读 exit supervision、hidden-state/KV management、自 speculative verification、accuracy/speed/throughput 与 ablation。early exit 在 offload 场景必须保留 verification 与 cache identity；收益依赖 offload hierarchy 和 exit accuracy。

## Evaluation、Security 与 Agent

- **2609.15994 — Latent Undertow**：阅读 perturbation taxonomy、activation geometry、probe evaluation、KV suffix fork 与 limitations。普通 typo 对生成语义影响小却旋转 probe readout，single-position probe 的 suffix recovery 有三模型几何复现、仅 Llama-3.1-8B probe 评价；不等于所有 hidden-state monitor 可被相同方法修复。
- **2609.16073 — The Immutable Past**：阅读 shadowing theorem、majority-vote trap、GC-Mem、137,760 chunk accumulation sweep 与 threshold。核心是 valid-time dominance + contradiction detection；`>90%` 只属于作者构造 benchmark/oracle，不是通用事实更新正确率。
- **2609.17081 — EviScope**：阅读 quartet construction、paired metrics、reference systems 与 qualitative errors。固定问题下 add/remove/distract/contradict evidence 可以分离 unsupported answer、conflict blindness 与 wrong abstention；40 quartets 规模限制了泛化。
- **2609.17274 — After the Party**：阅读三份 registry snapshot、Git history、scanner comparison、人审 reference 与 threats。23,702/61,990 disagreement、21.67%–61.06% sensitivity 证明单 scanner 不足；只代表 OpenClaw 时段和可读 skill 子集。
- **2609.17306 — Mo' Models, Mo' Problems**：阅读摘要与 model-pool selection protocol。科学 benchmark 中扩大异构 pool 会降级、同族选择较稳，但范围不足以形成通用 MAS selection law，按标准审阅。
- **2609.17346 — Where Should a Document Live**：阅读 oracle/multi-document retrieval、storage budget、catastrophic forgetting 与 limitations。KV representation、context 和 parameter adaptation 的优劣随压缩/检索变化；五个 benchmark 不构成所有知识注入 workload 的统一排序。
- **2609.17416 — Never Stop Thinking**：阅读 interrupt/resume orchestrator、ReactiveBench、judge reversal、五阶段训练与 exact track。19% latency 与 48→73% completion 绑定 voice pipeline/任务/奖励；长期结论是 reward provenance 与 timing state 必须共审。
- **2609.17419 — World Model Science**：阅读 alignment of implied/grounded states、avalanche/null models、22 experiments 与 negative claims。作者明确不支持普适 power law/critical point；可采用的是 trajectory diagnostic vocabulary，而非物理定律类比。

## 多模态、World Model 与物理行动

- **2609.16697 — World Models for Embodied Intelligence**：阅读 Plausible/Controllable/Actionable hierarchy、3×4 matrix、evaluation/challenges。它是 survey/taxonomy，不提供单一新模型效果；可用于重构评价主线，不能当作机制实验证据。
- **2609.16745 — The Latent That Never Was**：阅读 shared-data encoder removal、10k/100k steps、implementation checks、latent probes 与 limitations。复跑未支持已发表的 CVAE drop，说明训练 budget/posterior use 是 confounder；单一 ACT family 不能否定所有 latent action modeling。
- **2609.17372 — XPACE**：阅读 shared video backbone、heterogeneous experience curriculum、self-generated recovery、真实 IRON robot experiments。human/video/robot transfer 与 recovery improvement 支持 joint world/action loop；硬件、任务和过滤器限制外推。
- **2609.17414 — SlotDiT**：阅读 slot encoder、text-conditioned DiT、四机器人数据集、latent comparison 与 compute analysis。object-centric latent 改变状态粒度并提高作者任务完成率；不是对所有 video quality/physical fidelity 的证明。
- **2609.17521 — PhysStream**：阅读 two-stage training、online positional/tracking maps、velocity increment、synthetic/in-the-wild evaluation。streaming control 与 structured memory 是机制增量；物理指标和人评不证明真实机器人因果可靠性。

## 未进入候选但完成摘要判断的代表性关闭

- **2609.15991 Functionalizer**：lossless opcode/operand pre-tokenizer 在 98M GPT-2 上有局部收益，但尚不足以改变 production tokenizer 的长期选择；保留为具体小模型证据，不进入候选分母。
- **2609.16053 REALM**：retrieval-driven reconsolidation 是有效框架组合，但摘要证据没有超出 Books 已有的 derived memory、retrieval feedback 与 provenance/valid-time 主线。
- **2609.16338 BITCOS**：ternary weight symbol distribution 的压缩布局与 kernel 优化属于特定数值格式实现，本窗不足以改变量化主线。
- **2609.16601 SAVOR**：confidence-calibrated GRPO 对两个 MLLM 的 hallucination 改善是局部训练方案，未改变已有 selective prediction 与 evidence-verification contract。
- **2609.17184 LoopSpec / 2609.17241 ECHO**：两项 self-speculative 机制是有价值的实现分支，但其核心仍由现有 draft/verify/accept exactness 主线承载，本窗不重复建立候选。
- **2609.17496 Fuse / 2609.17516 CoSQ**：分别是 social-reasoning benchmark 与 prompt-only abstention 方法；均未提供超出现有 evaluation/uncertainty 主线的长期机制增量。
