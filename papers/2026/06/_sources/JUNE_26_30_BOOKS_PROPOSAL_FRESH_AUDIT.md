# June 26/29/30 Books Proposal Fresh-Context Audit

## 审计范围与口径

- 审计对象：2026-06-26、2026-06-29、2026-06-30 三份 Daily 中列出的 11 项 Books 正文提案，以及三份 `books-writeback-proposals-v3-20260910.md`。
- 审计维度：候选是否属于大模型或大模型基础设施范围；Stable Knowledge Node owner 是否正确；提案是否形成“旧边界 → 新机制 → trade-off/failure → 共存边界”；应判为 `Integrate`、`Existing Coverage` 还是仅保留于报告；目标章节的插入位置是否连贯。
- 正文判定：依据 `docs/WRITING_GUIDE.md`，`Review notes` 只承担来源、审阅状态与补充边界记录。仅有 Source Trace 或 `Owner-merged minimal durable delta`，而没有进入章节机制叙述，不视为 Books 正文已经整合。
- 基线选择：当前工作树存在并行修改，因此“是否已有正文覆盖”优先以提交态 `HEAD` 复核，并用当前文件行号标识可读锚点；没有把本轮并行改动误判为既有覆盖。
- 证据边界：本审计复核本地 exact-v1 证据摘要、提案文本、ROADMAP owner 与 Books 正文；没有重新运行论文实验，也不把论文单点 benchmark 外推为普遍结论。

## 总结

| 日期 | 候选 | 结论 | 建议 Books Decision | 核心理由 |
|---|---|---:|---|---|
| 06-26 | Moebius | Reject | Existing Coverage | Ch56 已有同名正文机制链，重复写入会形成第二 owner 表述。 |
| 06-26 | ShareLock | Reject | Existing Coverage | Ch83 已有组合级 admission 正文，已覆盖阈值份额、组级准入与失败回退。 |
| 06-26 | DMuon | Reject | Existing Coverage | Ch36 已将矩阵更新写成 distributed operation，并给出通信、状态与退化边界。 |
| 06-26 | Delayed Verification | Reject | Existing Coverage | Ch82 已有 verification delay 作为拓扑控制状态的正文机制。 |
| 06-29 | PEBS | Reject | Existing Coverage | Ch31 已在 reward heterogeneity 正文中整合 rater calibration 与失配回退。 |
| 06-29 | Retroactive Advantage Estimation | Reject | Existing Coverage | Ch31 同一正文已覆盖 pending reward、age/kernel、policy identity 与 reinjection；提议标题还会撞上另一类在线 credit。 |
| 06-29 | Teacher–Student Partitioning | **Pass** | **Integrate** | 正文尚缺失，owner 正确，机制链完整；应落在拓扑映射之后。 |
| 06-29 | Hybrid World-Model Planning | **Change** | **Integrate after revision** | 机制值得写入，但需明确 planner verifier 与环境事实源的权限边界，并调整插入位置。 |
| 06-30 | Signal-Coverage Matrix | Reject | Existing Coverage | Ch66 已有 failure-type-aware aggregation；2×2 矩阵应作为受限案例，不应被外推成普遍 release 合同。 |
| 06-30 | KernelSight-LM | Reject | Existing Coverage at Ch56 | 候选在 scope 内，但 owner 应是 INFER-SCHEDULING；Ch56 已有校准式配置搜索与 capacity model 正文。 |
| 06-30 | Modal/Correlation Ceiling | **Change** | **Integrate after revision** | Ch66 仅部分覆盖 sampling/selection failure；相关采样上限是新增机制，但不能塞入现有 Pass@k/Pass^k 小节。 |

合计：**1 Pass / 2 Change / 8 Reject**。这里的 Reject 是“拒绝本次新增正文提案”，并不否定论文价值；其中 8 项均应改记为已有覆盖，而不是 `Weekly Only`。

## 逐项审计

### 1. Moebius: Runtime-Adaptive Parallelism for Efficient MoE Inference（2606.26607）

**结论：Reject — Existing Coverage。**

- **Scope**：属于大模型推理基础设施。它处理 MoE serving 在 prefill/decode、负载和通信形态变化时的并行策略，不是泛化的分布式系统案例。
- **Owner**：`INFER-SCHEDULING` / Ch56 正确。策略切换由请求阶段、负载与 SLO 驱动，核心 owner 不是单纯的 distributed-training parallelism。
- **机制链**：提案本身完整：静态 TP/EP 的适用条件 → runtime switching → address mapping/epoch 等正确性约束 → 切换成本、有限硬件验证与静态回退。
- **为何不 Integrate**：提交态 Ch56 已有 `### MoE 并行形态从部署配置演进为运行时状态`（当前约第 388 行），正文已表达上述完整链条；Source Trace 不是唯一落点，机制已经进入正文。
- **插入位置**：无需再插。若未来补证据，只更新既有小节的证据边界，不能新增同义小节。

### 2. ShareLock: Secure Tool Sharing in Multi-Agent Systems（2606.27027）

**结论：Reject — Existing Coverage。**

- **Scope**：属于 agent runtime/tool governance，尤其是多 agent 共享工具带来的组合级攻击面，符合大模型系统 scope。
- **Owner**：`AGENT-MCP` / Ch83 正确；它治理 tool exposure 与 admission，而不是一般 multi-agent coordination。
- **机制链**：提案已覆盖单工具扫描的旧边界、threshold share/group admission、client 限制、组合攻击面，以及 deny/quarantine 与单工具扫描共存。
- **为何不 Integrate**：Ch83 提交态正文已有 `### 从单工具扫描到组合级 Admission`（当前约第 241 行），机制、failure 与 fallback 均已写入正文。
- **插入位置**：无需新增；后续只能在该小节补充更强的 runtime 证据或权限撤销语义。

### 3. DMuon: Distributed Matrix-Coupled Optimizer（2606.27153）

**结论：Reject — Existing Coverage。**

- **Scope**：属于大模型分布式训练系统。贡献点是矩阵耦合 optimizer update 的分片、通信与状态语义，而非只讨论优化算法精度。
- **Owner**：`TRAIN-DISTRIBUTED-TRAINING` / Ch36 正确。
- **机制链**：提案已把 data-parallel scalar/local update 的旧假设，推进到 update 本身成为 collective/distributed operation，并包含通信、状态一致性、拓扑失配和退回传统 optimizer 的边界。
- **为何不 Integrate**：Ch36 提交态正文已有 `### 矩阵耦合 Optimizer 必须把更新本身变成 Distributed Operation`（当前约第 593 行），已完整承载该链条。
- **插入位置**：无需新增；避免在 optimizer、collective 与 topology 三处重复拥有同一机制。

### 4. Delayed Verification in Multi-Agent Systems（2606.27409）

**结论：Reject — Existing Coverage。**

- **Scope**：属于 agent runtime 的异步验证与协作拓扑控制，符合大模型系统范围。
- **Owner**：`AGENT-MULTI-AGENT` / Ch82 正确；重点是验证时延如何改变依赖图、并发与提交，而不是一般 tool protocol。
- **机制链**：旧的同步验证假设 → delay-aware speculative/conditional progress → stale verification、错误扩散与补偿 → 同步屏障或保守拓扑回退，链条成立。
- **为何不 Integrate**：Ch82 提交态正文已有 `### Verification Delay 也是拓扑控制状态`（当前约第 550 行），已经形成正文机制与共存边界。
- **插入位置**：无需新增。

### 5. PEBS: Personalized Evaluation Bias Scaling（2606.27578）

**结论：Reject — Existing Coverage。**

- **Scope**：属于 LLM post-training/evaluation feedback pipeline；只有在“异质 rater 如何改变 reward semantics”这一系统表述下成立，而不是泛化的人类偏差研究。
- **Owner**：`TRAIN-RLHF` / Ch31 正确。
- **机制链**：统一 reward scale 的旧边界 → rater identity 的 offset/slope calibration → 小样本、漂移与过拟合风险 → shrinkage prior、共享模型或不校准回退，完整且克制。
- **为何不 Integrate**：Ch31 提交态正文已有 `### Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间`（当前约第 405 行）；正文已包含 calibration slice、shrinkage prior、局限与回退。
- **插入位置**：无需新增。若补充 PEBS，只能作为现有小节的受限证据，不能另起 owner。

### 6. Retroactive Advantage Estimation for Delayed Rewards（2606.27580）

**结论：Reject — Existing Coverage。**

- **Scope**：属于在线 RL/post-training runtime 的延迟 reward、trajectory identity 与更新一致性，符合大模型训练系统范围。
- **Owner**：`TRAIN-RLHF` / Ch31 正确。
- **机制链**：即时 reward 假设 → pending reward queue、age/kernel、originating policy/importance ratio → stale/off-policy contamination 与 reinjection mass → 同步或丢弃过期反馈的回退，链条成立。
- **为何不 Integrate**：Ch31 当前约第 407 行已在 reward heterogeneity 正文中写入这组机制。提案建议的 `### 在线 Credit 需要显式的时序状态` 还会与当前约第 523 行的同名正文冲突；后者讨论 recurrent hidden state/eligibility trace，是另一类 credit assignment，强行合并会破坏知识边界。
- **插入位置**：无需新增；保持 delayed feedback 与 recurrent credit 两条机制链分开。

### 7. Teacher–Student Partitioning for Distributed Distillation（2606.27797）

**结论：Pass — Integrate。**

- **Scope**：属于大模型蒸馏训练的 runtime topology 与 resource partitioning，而不是只比较 distillation loss，符合 scope。
- **Owner**：`TRAIN-DISTRIBUTED-TRAINING` / Ch36 正确。teacher inference 与 student training 的并行计划、资源竞争和通信编排均由分布式训练拓扑拥有。
- **机制链**：强迫 teacher/student 共用并行方案的旧边界 → 两套 partition plan 与显式交接 → pipeline bubble、显存/网络争用、版本与缓存一致性 failure → 小规模共置、静态 teacher 输出或统一计划回退。提案已具备形成正文的骨架。
- **为何是 Integrate**：当前相关文字仅位于 Ch36 `Review notes` 的 `Owner-merged minimal durable delta`（当前约第 1461 行之后），不能算正文；正文尚无唯一承载点。
- **插入位置**：在 Ch36 `## 拓扑映射为什么不能事后处理` 的主体叙述之后、`## Global Batch、Micro Batch 与梯度累积` 之前，新建 `### Teacher 与 Student 不应共享一份并行 Plan`。这里能自然承接“并行策略是 first-class input”，又不会打断 batch semantics。

### 8. Hybrid World-Model Planning with Parametric Transition Verification（2606.27806）

**结论：Change — Integrate after revision。**

- **Scope**：属于 LLM agent planning runtime：用 parametric model 提议/校验 transition，并在真实执行前控制搜索与重规划，符合 scope。
- **Owner**：以 `AGENT-PLANNING` / Ch79 为主基本正确，但必须显式声明事实所有权仍属于环境/controller；否则会与 world model、environment model 的 owner 发生重叠。
- **机制链**：符号规则覆盖不足的旧边界 → parametric transition verifier → hallucinated transition、model drift、错误累积与 verifier 成本 → authoritative environment check、规则校验和 replanning fallback，方向正确。
- **需要修改**：提案应增加一条强约束：parametric verifier 只能改变候选 transition 的优先级或 provisional 状态，不能提交外部事实；环境反馈仍是 commit authority。并明确何时因 drift 或低置信度退回规则/真实 rollout。
- **为何是 Integrate**：相关文字目前只在 Ch79 `Review notes` 的 minimal delta（当前约第 396 行之后），正文没有这一机制。
- **插入位置**：不要放在靠后的通用“条件化机制分支与共存边界”。应放在 Ch79 `## 从目标到状态图` 之后、Replanning 之前，新建明确的小节，使“belief/provisional transition → authoritative observation → replan”形成连续链，并向环境/world-model 章节做一次 owner handoff。

### 9. Signal-Coverage Matrix for Autoformalization Evaluation（2606.28013）

**结论：Reject — Existing Coverage；2×2 matrix 保留为受限案例。**

- **Scope**：若限定为 LLM autoformalization 的 evaluation validity，则属于模型/系统评测；若扩展成一般形式化数学 benchmark，则超出本仓库主范围。提案必须保留前一限定。
- **Owner**：`PLATFORM-EVALUATION-SYSTEM` / Ch66 正确。
- **机制链**：单一 acceptance score 的旧边界 → elaborator pass/fail × semantic equivalence 的 2×2 matrix → false positive、false negative 与 judge disagreement → cell-level inspection/人工审计，作为案例是完整的。
- **为何不 Integrate**：Ch66 提交态正文已有 `### 聚合指标必须能暴露不同 Failure Type`（当前约第 2836 行），明确要求将 omission、mode collapse、semantic drift，以及 detection/ranking/diagnosis 拆开，并以 counterexample slice 校验。另有 cross-layer evaluation 约束，已经拥有一般原则。
- **证据边界问题**：提案把特定 autoformalization 的二维矩阵上升为所有 release claim 的强制合同，超出了本项证据能支持的范围。矩阵适合作为 Daily/Review note 中的受限实例，或未来在积累跨任务证据后作为正文例子；当前不应新增第二个通用原则小节，也不应判为 `Weekly Only`。

### 10. KernelSight-LM: Kernel-Level Simulation for LLM Serving（2606.28565）

**结论：Reject — Existing Coverage at Ch56；拒绝写入 Ch42。**

- **Scope**：属于 LLM serving capacity/configuration search，符合大模型基础设施范围。
- **Owner**：提案给出的 `INFER-REQUEST-LIFECYCLE` / Ch42 不准确。request lifecycle 可以提供 phase identity 与观测入口，但 kernel-calibrated simulation、parallel configuration search、SLO Pareto frontier 的唯一 owner 应是 `INFER-SCHEDULING` / Ch56。
- **机制链**：逐配置实机压测 → kernel/phase calibrated simulator → drift、simulation error 与错误排序 → targeted hardware validation、canary 与 direct profiling fallback，提案本身链条良好。
- **为何不 Integrate**：Ch56 提交态正文已通过 `## 从逐配置压测到校准后的配置搜索` 与 saturation-aware capacity model 覆盖 primitive database、iteration/queue-aware prediction、SLO/Pareto search、calibration identity、drift detection、targeted silicon validation 与回退。Ch42 `Review notes` 中的 minimal delta（当前约第 383 行之后）既不算正文，也不应促成错误 owner 下的重复写入。
- **插入位置**：本次不新增。若以后需要增强，只在 Ch56 既有配置搜索小节补充 kernel-level simulator 作为受限实现证据；Ch42 仅保留到 Ch56 的 handoff。

### 11. Modal/Correlation Ceiling in Repeated Sampling（2606.28661）

**结论：Change — Integrate after revision。**

- **Scope**：属于 LLM evaluation/selection pipeline，讨论 repeated sampling 在相关输出下对 coverage 与 selector 的影响，符合 scope。
- **Owner**：`PLATFORM-EVALUATION-SYSTEM` / Ch66 正确。
- **机制链**：把样本视为独立且“多采样必然更好”的旧假设 → 相关性降低 effective decision information、modal mass 支配 selector → coverage 上升但 selection accuracy 停滞甚至下降 → diversity-aware sampling、selector calibration 与 marginal-gain stopping。该机制提供了正文尚缺的新增因果桥。
- **已有覆盖与新增量**：Ch66 当前约第 2701 行的 `### Miscoverage 要拆成 Sampling Failure 与 Selection Failure` 已区分候选集缺失和 selector 选错，但尚未解释 correlation/modal ceiling。当前约第 512 行的 `### 从 Pass@k 到 Pass^k：能力覆盖与重复可靠性不是同一问题` 讨论的是“至少一次成功”与“连续全部成功”，不是 candidate coverage 与 selection accuracy。
- **需要修改**：不要沿用或插入现有 Pass@k/Pass^k 标题；否则会把 conjunction reliability 和 selection ceiling 混成一件事。建议新标题为 `### 相关采样会抬高 Coverage，却压低 Selection 上限`，并明确 ceiling 随 model、task、sampler、selector 改变，不是一个固定常数。
- **插入位置**：紧接 Ch66 的 Sampling Failure / Selection Failure 小节，或合并为该小节的第二段机制链。这里能把“错误来自哪里”自然推进到“为什么增加 k 仍不能修复 selector”。

## 可执行结论

1. 可直接进入 Books 正文实施队列：Teacher–Student Partitioning（1 项）。
2. 修改提案后进入正文实施队列：Hybrid World-Model Planning、Modal/Correlation Ceiling（2 项）。
3. 关闭本次新增正文提案并改记 `Existing Coverage`：Moebius、ShareLock、DMuon、Delayed Verification、PEBS、Retroactive Advantage、Signal-Coverage Matrix、KernelSight-LM（8 项）。
4. 实施阶段仍需重新读取目标正文与相邻交接内容；本审计不授权或代替 Books 修改，也不更新 Daily、Learning State 或共享索引。
