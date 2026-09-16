# 2026-06-19 恢复候选 Books Writeback 记录

**状态：** Closed — 9 项已写入并通过独立写后审计；待写入队列为 0。

本文件保留写前差异、证据边界和写后锚点，不能单独替代 Books 正文证明。独立 reviewer 已重新读取目标章节与相邻交接，确认每项正文锚点位于首个 `Review notes` 之前；其中 4 个错误落点已移回核心机制主线。

2026-09-11 独立 Books Gate 对读 12 个 proposal 与现有正文后，将 `2606.19531`、`2606.19558`、`2606.19919` 降为 `No Change — Existing Coverage`；本文件以下 9 项才是 root 的最终待写入集合。

## 已完成写入 9 项

### 2606.19354 → `INFER-SCHEDULING`

- 路径：`books/part-05-inference-system/56-inference-scheduling.md`
- 当前缺口：已有 verifier、confidence 与 residual-value 调度，但没有把 outcome/process 的验证粒度本身作为动态 compute state。
- 长期增量：以 task difficulty、verifier accuracy 与 compute budget 联合选择 verification granularity；scheduler 拥有预算与粒度，verifier 只返回 evidence。
- 共存与边界：静态 ORM/PRM 在分布稳定时继续成立；理论依赖 accuracy–granularity 单调性、log-concavity 等假设，未证明生产 latency/SLO。
- 相邻交接：speculative / reasoning 路径只提出候选计算；Ch56 决定是否、以何种粒度验证。

### 2606.19607 → `TRAIN-DPO`

- 路径：`books/part-04-training-system/34-dpo.md`
- 当前缺口：已有 preference data quality 与 loss，但尚未把 pair acquisition 写成有限 label budget 下的 experimental design。
- 长期增量：记录 response generation pool、pair sampling policy、human label budget 与 coverage/info matrix；比较的 pair 会改变 estimator 与 policy gap，而不只是扩大样本数。
- 共存与边界：uniform sampling 在分布稳定、设计成本高时仍是基线；理论依赖 realizability、regularity 与 coverage，未证明在线 adaptive setting。
- 相邻交接：Ch27/28 拥有数据 lineage；Ch34 拥有 pair selection 与 DPO objective；Evaluation 只验收外部行为。

### 2606.19744 → `TRAIN-DPO`

- 路径：`books/part-04-training-system/34-dpo.md`
- 当前缺口：sequential preference update 的 aggregate score 不能说明何处遗忘或发生目标迁移。
- 长期增量：release ledger 保存 objective relation、训练顺序、signal strength、固定 evaluation reference、pair-level margin 与 harmed/helped quartiles；gradient/adapter movement 只作诊断证据。
- 共存与边界：单轮 DPO 或兼容 objectives 无需复杂 ledger；证据限一个 8B LoRA 设置，不能外推 full-parameter 或所有模型。
- 相邻交接：Checkpoint owner 保存 revision；DPO owner解释目标迁移；Evaluation owner决定是否达到 release condition。

### 2606.20008 → `TRAIN-GRPO`

- 路径：`books/part-04-training-system/33-grpo.md`
- 当前缺口：现有 group baseline 与 learned critic 两端之间缺少 policy-implied value 的条件分支。
- 长期增量：在 deterministic prefix MDP 中，以 policy/reference log-ratio、KL-regularized Bellman recurrence 和 terminal anchor 构造 token-level value/advantage，不训练独立 critic。
- 共存与边界：group estimator 在无需精细 credit 时更便宜，learned critic 在状态更复杂时仍可用；fixed reference、beta schedule、exact-KL 成本与数学任务范围必须显式保留。
- 相邻交接：PPO/GRPO 章节共同消费 reward evidence；Ch33 是该 critic-free branch 的唯一 owner。

### 2606.20075 → `TRAIN-PRETRAINING`

- 路径：`books/part-04-training-system/28-pretraining.md`
- 当前缺口：latent reasoning 的监督容易被压成单一“需要 process supervision”结论。
- 长期增量：分开 optimization-path gradient attenuation 与 representation-space drift；trajectory supervision 改善路径 credit，space supervision 约束 latent interface，generative reconstruction 比 rigid point alignment 更保留语义自由度。
- 共存与边界：outcome supervision 在路径短/表示稳定时仍成立；论文结果不是 latent CoT 可解释性或普遍信息定理。
- 相邻交接：Model 章节定义 latent interface，Pretraining 拥有监督路径，Evaluation 不把 probe 当因果真值。

### 2606.20092 → `MULTIMODAL-EMBODIED-VLA`

- 路径：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`
- 当前缺口：已有 episode memory 与 action loop，但缺少“在瞬态 evidence 消失前预测性提交”的 write timing。
- 长期增量：KEM 根据 action-horizon hidden state 预测 future utility，由独立 memory controller 触发 keyframe write；FIFO、NMS/cooldown 只约束容量，不替代 action policy。
- 共存与边界：周期采样/完整 buffer 在短 horizon 或容量充足时更稳；threshold、自动标签和 FIFO 可漏写、误写或覆盖，作者实验不构成物理安全保证。
- 相邻交接：Ch25 拥有 world state transition；Ch26 拥有 evidence write 与 physical action commit。

### 2606.20104 → `MULTIMODAL-WORLD-MODELS`

- 路径：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`
- 当前缺口：已有 latent dynamics 与 anti-collapse 压力，但未把 inverse dynamics 的适用前提和信息偏置写清。
- 长期增量：联合 forward + inverse objective，以 action recoverability 阻止 constant latent collapse并保留 controllable information。
- 共存与边界：若动作不能从相邻 observation 恢复、存在 partial observability 或 uncontrollable task-relevant state，inverse loss 会偏置/丢失表示；reconstruction、EMA target 等旧分支继续成立。
- 相邻交接：Representation owner 提供 observation identity；World Model owner决定 latent state；Embodied controller只消费带前提的 state。

### 2606.20225 → `PLATFORM-SECURITY`

- 路径：`books/part-06-ai-infrastructure/72-security.md`
- 当前缺口：activation monitor 讨论尚未明确区分 within-model causal specificity 与 cross-model mapped correlation。
- 长期增量：同一 revision 内的 intervention + random/orthogonal controls 可支持 causal probe；跨模型 ridge mapping 必须重新通过 control specificity，未通过时只能作 weak screening，不能拥有 mitigation authority。
- 共存与边界：每个 model/revision/domain 重新校准；证据限小模型与 insecure-code fine-tuning，不证明 universal misalignment direction。
- 相邻交接：Monitoring 提交 signal，Security policy决定阻断/修复，Evaluation 验收 behavior，不让 probe 直接执行安全动作。

### 2606.20560 → `MULTIMODAL-GENERATIVE-PARADIGMS`

- 路径：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 当前缺口：editable/provisional token state 容易被表述为“更透明”，却未分离透明性的对象。
- 长期增量：区分 variable transparency（状态可读写）、algorithmic transparency（过程可重建）与 safety monitorability（传感器可检出风险）；interpretable bottleneck 可降低 opaque serial-depth bound，但不能证明算法或安全。
- 共存与边界：serial-depth 是上界，multi-canvas monitor 可能漏检 single-canvas failure，architecture/training cause 未辨识；AR 的全序 trace 在需要明确提交路径时仍成立。
- 相邻交接：Ch24 拥有 provisional/commit 和 transparency contract；Evaluation/Security 只消费带边界的 observability evidence。

## Existing Coverage 9 项

| arXiv | Owner | Review notes 前正文锚点 |
| --- | --- | --- |
| 2606.19348 | `MODEL-LONG-CONTEXT` | Long Context 是位置、Attention、KV、利用率与系统 SLO 的联合能力；sparse/hybrid state 与异构 runtime 已有完整分支 |
| 2606.19388 | `AGENT-TOOL-CALLING` | `Agent-friendly Tool 不等于把 CLI 包一层` 与 interface granularity |
| 2606.19453 | `MULTIMODAL-REPRESENTATION` | `Full-duplex 输入让 Fusion 变成在线状态路由` |
| 2606.19475 | `MULTIMODAL-GENERATIVE-PARADIGMS` | editable token、sampler/commit、block size、correction 与 cache/streaming 的条件化比较 |
| 2606.19531 | `MULTIMODAL-EMBODIED-VLA` | `World-action model` 已写明 explicit future rollout → joint generation → direct latent predictive interface，并明确 action branch 可读取 layer-wise KV / compact dynamics state 而不 materialize future video；物理 commit 仍归 controller/safety envelope |
| 2606.19558 | `PLATFORM-EVALUATION-SYSTEM` | `压缩模型的 release gate 也不能停留在平均 perplexity` 与 threshold-adjacent churn 已要求 proxy 只作早期 guardrail，边界区回到 item-level downstream、calibration、真实 runtime artifact 与 release evidence |
| 2606.19636 | `PLATFORM-EVALUATION-SYSTEM` | `pass@k` 是有限采样预算的覆盖率，不是模型不可解证明 |
| 2606.19919 | `TRAIN-GRPO` | 章内已把 typed credit 对齐到实际 state-action boundary，并规定 terminal outcome/verifier 拥有 reward direction、局部 process signal 只调节幅度；mode token 是该原则的一个二元实现案例 |
| 2606.20097 | `MODEL-LONG-CONTEXT` | hybrid attention 的 per-layer/head exact-access budget 与 conversion sensitivity |

## 写后验收（已完成）

独立 reviewer 已逐项确认：正文位于首个 Review notes 前；不以论文名为段落主语；旧方案为何合理、约束变化、状态/控制权、收益、代价、failure 与 fallback 连成同一推理链；与相邻章节只有短 handoff；Daily、proposal 与最终正文锚点一致。06-19 已完成。
