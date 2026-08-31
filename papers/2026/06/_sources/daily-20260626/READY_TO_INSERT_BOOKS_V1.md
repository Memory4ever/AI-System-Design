# 2026-06-26 Ready-to-Insert Books Packet V1

Root 串行写回共享 Books；每个 owner 只写一段合并后的长期机制正文，family identity 只出现在 source-specific exact-v1 Review notes。

## `AGENT-MCP` → `books/part-07-agent/83-mcp.md`

相邻章 `books/part-07-agent/84-agent-platform.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

逐个检查工具描述或在单一工具内扫描明文 payload，在攻击局限于单点污染时仍然合理。新的约束是恶意信息可以拆成 threshold secret shares，分别藏在多个看似无害的工具描述中，只在特定组合、trigger 或 update 后重构；此时单工具结论不能代表组合安全。MCP 控制面因此要持有 tool-set identity、share/trigger 组合风险、server/update version 与 effect-time authorization，并把 group-level admission 置于工具调用之前。论文只在四类多工具场景、主流 LLM 与两个 MCP client 上报告平均攻击成功率超过 90%，不证明任意 client/trigger 都可攻破，也不证明组合防御不可能。组合状态未知或更新后证据失效时应 deny/quarantine，并交给独立 reference monitor 逐次授权；原有单工具扫描仍作为第一层共存。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-27027` — ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP; primary=`arXiv:2606.27027v1`; Method=`arXiv:2606.27027v1 — §4. ShareLock: a Multi-Tool Threshold Poisoning Attack Framework; §D.1. System Prompt for Zero-Shot Detection`; Evaluation=`arXiv:2606.27027v1 — §5. Evaluation; §5.1. Experimental Setup; §Appendix D Experimental details of Safety Classification Task`; counterevidence/non-proof locator=`arXiv:2606.27027v1 — §3.3. Threat Model; §6. Discussion and Limitations; §7. Conclusion`; claim boundary=证据限于四类多工具场景、论文测试的主流 LLM 和两个 MCP client；平均攻击成功率超过 90% 不证明任意 client/trigger 都可攻破，也不证明 group-level 防御不可能。; fallback=组合身份或授权证据不完整时 deny/quarantine，并交给独立 reference monitor。

## `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`

相邻章 `books/part-07-agent/83-mcp.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

当 verifier/critic 延迟相对任务传播可忽略时，在 agent 输出后统一纠错是合理的。约束变化是错误信念可能在校正到达前沿通信图传播，而过强或过迟的纠正还会造成振荡。多智能体 control state 因此要显式记录 verification dose、delay、corrector placement、graph version 与 belief epoch，把纠错部署视为带稳定性边界的控制问题。论文给出阈值与 greedy placement，并在五个开放模型上实验；它没有证明 signed-belief/delay 假设之外的任意拓扑或 Byzantine 行为，实验也受 grounded factual answering 任务限制。delay 或图版本未知时应序列化关键提交、使用 grounded deterministic verification，旧的事后 critic 只在低延迟区间共存。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-27409` — Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement; primary=`arXiv:2606.27409v1`; Method=`arXiv:2606.27409v1 — §3 Model; §4 Stability and the verification dose; §5 Optimal corrector placement`; Evaluation=`arXiv:2606.27409v1 — §7 Empirical validation; §7.1 Onset at the predicted dose limit (RQ1)`; counterevidence/non-proof locator=`arXiv:2606.27409v1 — §8 Discussion; §10 Limitations`; claim boundary=理论依赖 signed-belief/delay 模型，实验限于五个开放模型的 grounded factual answering；阈值与 greedy placement 不证明任意 topology、Byzantine agent 或非平稳 communication graph 的稳定性。; fallback=delay/graph version 未知时序列化关键提交并使用 deterministic verification。

## `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md`

相邻章 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

当请求并发长期稳定时，部署阶段固定 tensor parallel 或 expert parallel 是合理的：它减少运行时重排并让容量规划可预测。约束变化在于 MoE decode 的并发会连续跨越两种并行方式的优势区间，静态选择会把阶段性通信瓶颈固化。因而调度状态需要增加并行形态、切换阈值、byte-identical expert weight/KV 的固定地址映射和 in-flight request epoch，由运行时只在 decode step 边界提交切换。论文在 8×H200、Qwen3-235B-A22B 上报告 215–434 ms 切换、2.4% memory overhead 与 RL rollout 1.16–1.25× 吞吐收益；这不证明未测模型、互联、并发轨迹或生产 tail latency 下仍安全。切换成本、地址一致性和抖动是新增 failure mode；证据不足或状态校验失败时继续使用静态 TP/EP，旧路径与动态路径按稳定性区间共存。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-26607` — Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch; primary=`arXiv:2606.26607v1`; Method=`arXiv:2606.26607v1 — §4 System Design; §Appendix B End-to-End Training Projection`; Evaluation=`arXiv:2606.26607v1 — §6 Evaluation; §6.1 Experimental Setup`; counterevidence/non-proof locator=`arXiv:2606.26607v1 — §2.2 Real World Workloads Cross the Boundary; §8 Discussion; §9 Conclusion`; claim boundary=证据来自 8×H200 上的 Qwen3-235B-A22B serving 与 RL rollout；215–434 ms 切换、2.4% memory overhead 和 1.16–1.25× 吞吐收益不外推到未测模型、互联、并发轨迹或生产 tail latency。; fallback=switch epoch、地址映射或阈值证据不足时保持静态 TP/EP。

## `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`

相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

策略池固定且工作条件稳定时，为一次任务选择全局最优 expert 是可解释且低成本的。策略池持续增长后，选择问题分裂为两个控制动作：为新条件 commissioning 现有 expert，以及判断新 candidate 是否补足 incumbent 的真实 failure gap。VLA owner 因此要持有 condition split、outcome-disjoint probe、candidate version、probe budget 与 onboarding decision，只在新策略覆盖现有池无法处理的失败区间时提交上线。论文在 cost-matched probe budget 和五个 expert 上报告 held-out 60.53%、相对基线提升 1.64 个百分点；这不证明更大策略池、分布漂移或物理安全约束下仍成立。probe 泄漏、样本不足和错误 onboarding 会污染路由；置信度或 coverage 不足时保留 incumbent/default controller，并让人工或保守策略接管。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-27355` — RouterVLA: Budgeted Commissioning and Expert Onboarding for Growing VLA Pools; primary=`arXiv:2606.27355v1`; Method=`arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Training objective; §Commissioning turns a policy pool into a stronger system`; Evaluation=`arXiv:2606.27355v1 — §Algorithm selection and limited-budget evaluation.; §Problem Setup; §Experimental Protocol`; counterevidence/non-proof locator=`arXiv:2606.27355v1 — §Failure analysis: context and evidence; §Discussion; §Limitations`; claim boundary=证据限于 cost-matched probe budget、五个 expert 与论文的 held-out conditions；60.53% 及 +1.64pp 不证明更大策略池、分布漂移或物理安全 envelope 下的 onboarding 正确性。; fallback=probe coverage 或置信度不足时保持 incumbent/default controller。

## `TRAIN-DISTRIBUTED-TRAINING` → `books/part-04-training-system/36-distributed-training.md`

相邻章 `books/part-04-training-system/37-tensor-parallel.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

以 element-wise optimizer state 做 ZeRO/FSDP 式分片，在更新可按参数局部计算时是合理的。矩阵级 Newton–Schulz optimizer update 却耦合整块矩阵，局部 post-processing 会让相同 checkpoint 在不同 layout 下产生不同语义。训练状态因此必须增加 matrix layout、collective algorithm、worker group 与 optimizer-step identity，把更新本身作为分布式矩阵操作并与 checkpoint 原子提交。论文在 embodied foundation model 与 LLM 训练中报告加速且性能接近 AdamW，但没有证明任意拓扑、矩阵形状或长程收敛与集中式实现等价。collective 中断、layout 漂移或数值分歧时应恢复最近一致 checkpoint，并退回已验证的 AdamW/旧 optimizer 路径；局部优化器与矩阵耦合优化器按更新结构共存。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-27153` — DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; primary=`arXiv:2606.27153v1`; Method=`arXiv:2606.27153v1 — §DMuon: Efficient Distributed Muon Training with Near-Adam Overhead; §2.2 Sharded Training Abstractions; §3 System Design`; Evaluation=`arXiv:2606.27153v1 — §5 Evaluation; §Setup.`; counterevidence/non-proof locator=`arXiv:2606.27153v1 — §5.3 Limitations; §7 Conclusion`; claim boundary=证据覆盖论文的 embodied foundation model 与 LLM workloads；step-time 加速和 near-AdamW latency 不证明任意 topology、matrix shape、数值误差或长程收敛与集中式更新等价。; fallback=layout/collective 分歧时恢复一致 checkpoint 并退回已验证优化器。

## `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md`

相邻章 `books/part-04-training-system/32-ppo.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

把 reward 当作同尺度、同步到达的标量，在 rater 同质且反馈能在 update 前返回时是合理的；现实约束同时来自身份异质性和时间异步性：不同 rater 的 offset/slope 不同，慢 verifier 或人工反馈又可能晚到数个 gradient step。RLHF 状态因此需要同时持有 rater identity、calibration slice/shrinkage prior/version，以及 pending reward queue、age/kernel、originating policy/importance ratio 与 reinjection mass。每位 rater 的 held-out affine calibration 可用 empirical Bayes 向总体收缩；迟到 reward 则以 clipped residual 进入后续 advantage。论文分别在 PRISM/PluriHarms 与 tabular MDP 上报告 RMSE 改善和最高 47.9× bias reduction，但没有证明非线性或 adversarial rater、online drift、large-scale RLHF 稳定性与生产 queue failure。稀疏 rater 回退总体 calibrator 并抽样审计；delay/mass 假设失效时等待慢反馈或采用 bounded synchronous update。

### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-27578` — PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration; primary=`arXiv:2606.27578v1`; Method=`arXiv:2606.27578v1 — §2 Method; §Base-model training details.`; Evaluation=`arXiv:2606.27578v1 — §2.3 PRISM setup and base reward model; §3 Experiments`; counterevidence/non-proof locator=`arXiv:2606.27578v1 — §3.9 Ablations and failure cases; §4 Discussion; §5 Limitations`; claim boundary=证据来自 PRISM 与 PluriHarms 上的 held-out affine per-rater calibration；RMSE 改善不证明非线性/adversarial rater、极稀疏标注或 online rater drift 下仍校准。; fallback=校准或 delay/mass 假设失效时回到总体 calibrator 或 bounded synchronous update。
- `SF-2026-ARXIV-2606-27580` — Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF; primary=`arXiv:2606.27580v1`; Method=`arXiv:2606.27580v1 — §2 Method: Retroactive Advantage Correction`; Evaluation=`arXiv:2606.27580v1 — §Setup.; §K = 2 K{=}2 result and cost-quality Pareto.; §Scope of the closed-form result.`; counterevidence/non-proof locator=`arXiv:2606.27580v1 — §4 Conclusion; §Appendix E Limitations and Discussion; §Background and discussion.`; claim boundary=无偏结论要求 clipped importance ratio 无偏且 delay kernel reinject 全部质量，实验为 tabular MDP proof-of-concept；最高 47.9× bias reduction 不证明 large-scale RLHF 稳定性或生产 pending-queue failure 已解决。; fallback=校准或 delay/mass 假设失效时回到总体 calibrator 或 bounded synchronous update。

