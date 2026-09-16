# 2026-05-08 V3：9 个 closure false negative 限定返修

## 范围与结论

本轮只重开 fresh non-author review 指定的 9 个 family，不重新枚举 619 个 raw identity，也不重审已通过的 132 项 Evidence 与 69/63 Books 范围。9 项 exact-v1 均可访问，arXiv 页面未显示 withdrawn；全部进入 Candidate Denominator，且已完成 Score V2、Evidence、Stable Node 与当前 Books 命题对读。

返修后的机械账本为：

```text
619 raw families = 141 retained + 478 pre-denominator closures
141 retained = 101 deep + 40 standard
141 scores = 83 at 7–9 + 58 at 5–6
Books = 75 Applied + 66 No Change
Review Pending = 0
Blocked / Disputed / Withdrawn = 0 / 0 / 0
```

作者没有修改共享 Books，也不签署最终 Gate。6 项长期命题已经由 root 按 [精确写回队列](ROOT_BOOKS_WRITEBACK_QUEUE_BOUNDED_REPAIR_20260915.json) 落实并登记 item-level 状态；3 项以具体既有命题判为 `No Change — Existing Coverage`。日报继续为 `Ongoing`，等待新的 non-author final review。

## 逐项 Evidence Review

### 2605.05278 — Expert Routing for Communication-Efficient MoE via Finite Expert Banks

- **Method：** 把 gate 建模为从输入到 expert index 的随机信道，以 `I(X;T)` 表示 routing information，并讨论在给定 routing rate 下的最小 distortion；可计算实例是 25 个预训练 CNN experts、MNIST 与离散数据依赖选择规则。
- **Evaluation：** exact-v1 用有限 expert bank 检查 information–distortion 关系，并给出一般化界；`m=256`、`M=300` 等设置属于论文自身实验合同。
- **Limitations / non-proof：** toy vision workload、有限且冻结的 bank、较松的 bound；没有端到端训练、连续专家、LLM MoE、跨节点通信或生产 SLO 证据。
- **Score / owner：** `2+2+2=6`；因 Books 结论为 Integrate，按 Gate 完成 deep review；`MODEL-MOE`，handoff 到 inference scheduling/placement。
- **Books compare：** Ch21 已覆盖 router、capacity、load、dispatch 与 placement，但没有把 route selectivity 作为 information budget 并显式连接 distortion。结论：`Integrate — Applied`，待新的独立复核。

### 2605.05485 — ReaComp

- **Method：** 从 LLM 求解轨迹离线归纳 reusable symbolic solvers；在线 solver-first，无法覆盖或失败时再调用 LLM。
- **Evaluation：** 两个受约束 program-synthesis DSL；PBEBench-Hard 中 symbolic ensemble 84.7、BoK 68.4，hybrid 85.8，作者报告 token 约减少 78%；另一 hard split 的 hybrid 58 对 34.4。数字只属于论文披露设置。
- **Limitations / non-proof：** 只有两个 DSL 与 exact verifier；induction 结果在 run 间波动，包含 best-run selection，并依赖强 coding agent；不能外推开放任务。
- **Score / owner：** `3+2+3=8`，deep；`AGENT-WORKFLOW`。
- **Books compare：** Ch81 已有 intent-to-contract、deterministic spine 与 reusable skill artifact，但没有“reasoning trace → amortized executable solver artifact → LLM fallback”这条成本/控制演进。结论：`Integrate — Applied`，待新的独立复核。

### 2605.05646 — MUSE

- **Method：** 将 structural topology 放入 attention relation，把 semantic abstraction 放入 value，并由 residual decoder 承担 texture reconstruction，以缓解统一视觉 tokenizer 的重建/语义目标冲突。
- **Evaluation：** 同 backbone、数据与 teacher 的 1B/3B 对照和组件 ablation；作者报告相对 UniLIP 的多项受限增益与约 5% 披露 FLOPs 增量。
- **Limitations / non-proof：** 无独立 Limitations 节；Q/K–V 分责的因果唯一性、跨模态迁移、生产 latency 均未证明。
- **Score / owner：** `3+2+3=8`，deep；`MULTIMODAL-REPRESENTATION`。
- **Books compare：** Ch23 已说明 understanding 与 reconstruction 的冲突、混合表示及 artifact identity，但未形成 topology / semantic value / residual texture 的责任分解。结论：`Integrate — Applied`，待新的独立复核。

### 2605.05702 — Knowledge-Graph Paths as Intermediate Supervision

- **Method：** 任务生成时保存的 KG construction path 同时用于 solver waypoint partial credit，使 proposer 与 reward shaping 共享同一版本化 artifact。
- **Evaluation：** Qwen3-8B 同预算增量对照；KG 对 multi-hop 有益但会伤害 single-hop，waypoint/correctness 仍是近似信号。
- **Limitations / non-proof：** Wikidata factoid multi-hop；外部 LLM 抽取成本和误差进入 task/reward 两侧，开放搜索迁移未测。
- **Score / owner：** `3+2+2=7`，deep；`TRAIN-DATA`，handoff 到 `TRAIN-GRPO`。
- **Books compare：** Ch27 已覆盖 evidence graph、search trajectory 和 verifier-backed curriculum，但未说明同一 construction artifact 可分别服务 admission 与 bounded reward、以及由此产生的 leakage/authority boundary。结论：`Integrate — Applied`，待新的独立复核。

### 2605.05709 — Conceal, Reconstruct, Jailbreak

- **Method：** 攻击在 concealment 与 victim-side reconstruction 之间优化，以字符移除、文本/排版和图像 distractor 隐藏意图，同时保留可恢复性。
- **Evaluation：** HADES 750 queries、五类风险、五个攻击基线和多个开闭源 MLLM；报告 multi-trial max/mean，属于作者 attack/judge contract。
- **Limitations / non-proof：** 没有完整 defense；结果绑定数据集、攻击变换、模型和 judge，不能推出一般安全率。
- **Score / owner：** `3+2+3=8`，deep；`PLATFORM-SECURITY`。
- **Books compare：** Ch72 已明确写出“原始文本视图之外隐藏、可信重建后进入 context”的 reconstruction-layer attack，并要求 data layer 与 reconstruction layer 同时校验。结论：`No Change — Existing Coverage`。

### 2605.05892 — FLAS

- **Method：** 用 concept-conditioned、time-conditioned velocity field 代替固定 steering vector，并以 Euler steps 积分 state-adaptive curved intervention trajectory；另有 positive-data LM loss。
- **Evaluation：** AxBench held-in/held-out，Gemma-2-2B/9B，多 prompt、多 generation 与组件 ablation；结果依赖单层、FlowBlock 与作者 harmonic-mean 指标。
- **Limitations / non-proof：** AxBench 单一评测族、LM judge、数值积分 latency、backbone/layer 限制；多概念、跨层和跨模型因果迁移未证明。
- **Score / owner：** `3+2+2=7`，deep；`MODEL-TRANSFORMER-LAYER`，evaluation owner 负责证据门槛。
- **Books compare：** Ch66 已把 nonlinear/local intervention 定义为实验分支，并要求 target effect、control survival 与 OOD evidence；该论文是此分支的受限实例，不改变长期命题。结论：`No Change — Existing Coverage`。

### 2605.06124 — P-Guide

- **Method：** 将 CFG 每步 conditional/unconditional 双 forward 的 guidance 近似迁移到初始 latent prior，通过条件均值/方差模块完成 prior steering，再单 pass 采样。
- **Evaluation：** MNIST、CIFAR 与 ImageNet 256，U-Net/DiT-B/2，400K steps、单 RTX4090；作者报告约 1.247 MB 模块与约 50% latency，数字不具有生产外推性。
- **Limitations / non-proof：** 等价性只是一阶近似；guidance 过强会退化，ImageNet 初始化依赖预训练模型，没有 concurrency/tail-SLO 证据。
- **Score / owner：** `3+2+2=7`，deep；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Books compare：** Ch24 已有逐 step CFG/guidance 与调度成本，却没有“逐步双 pass → initial-prior steering → single pass”的条件替代路线。结论：`Integrate — Applied`，待新的独立复核。

### 2605.06192 — EA-WM

- **Method：** 从 kinematics 与 calibration 构造 camera-aligned Kinematic-to-Visual Action Field，并与事件/视觉状态双向融合，让生成模型消费已实现动作的结构表示。
- **Evaluation：** 作者 ablation 报告完整系统相对移除 KVAF 提升 5.63、相对移除 event fusion 提升 1.80；只属于其 simulation、metric 与模型设置。
- **Limitations / non-proof：** 需要运动学、标定和同步日志；只测 simulation，受噪声、遮挡与 embodiment shift 影响，对象状态仍是间接观测。
- **Score / owner：** `3+2+2=7`，deep；`MULTIMODAL-WORLD-MODELS`。
- **Books compare：** Ch25 的“Action realization 与 environment response 应由不同 owner 承担”已经要求 controller/kinematics 展开 trajectory、renderer 生成 robot geometry、world model 预测环境 response。结论：`No Change — Existing Coverage`。

### 2605.06207 — Taming the Entropy Cliff

- **Method：** 分析 uniform codebook 的累计容量为何在序列早期跨过 empirical dataset uncertainty，并用 position-varying codebook size 分配 coarse-to-fine capacity。
- **Evaluation：** 同 tokenizer 与 AR generator、只改变 codebook structure 的 ImageNet 256 对照与 ablation。
- **Limitations / non-proof：** 单一数据集/任务；entropy threshold 依赖 `N/K` 和顺序，不能外推语言或证明唯一层级机制。
- **Score / owner：** `3+2+3=8`，deep；`MULTIMODAL-REPRESENTATION`。
- **Books compare：** Ch23 已有全局 codebook/rate–distortion 和 representation identity，但没有 position-indexed capacity schedule 及 entropy cliff。结论：`Integrate — Applied`，待新的独立复核。

## 作者侧检查点

- 9/9 exact-v1 可访问且未见 withdrawal banner；无 Materials Request。
- 9/9 已写入 canonical `V3_RECERTIFICATION.json`；没有重开其他 closure。
- 6 项已由 root 按精确 queue 写回并登记 item-level 状态；3 项 No Change 均有具体命题 locator。
- 已通过的 69 项 Applied 不再保留 item-level “待非作者复核”旧后缀。
- 当前 Gate 仍为 `Ongoing`，`final_independent_signoff = false`。
