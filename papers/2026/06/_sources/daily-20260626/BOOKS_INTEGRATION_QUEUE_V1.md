# 2026-06-26 Books Integration Queue V1

Denominator `daily-v2.1:2026-06-26:48b4ead4054910a5`. Re-audited proposal-only scope: 7 Integrate families merged into 6 unique owner files; 33 No Change — Existing Coverage; 44 Weekly Only — Context. Root owns Books and docs/LEARNING_STATE.md.

## `AGENT-MCP` → `books/part-07-agent/83-mcp.md`

- Adjacent non-owner: `books/part-07-agent/84-agent-platform.md#L1`
- Owner-merged body: 逐个检查工具描述或在单一工具内扫描明文 payload，在攻击局限于单点污染时仍然合理。新的约束是恶意信息可以拆成 threshold secret shares，分别藏在多个看似无害的工具描述中，只在特定组合、trigger 或 update 后重构；此时单工具结论不能代表组合安全。MCP 控制面因此要持有 tool-set identity、share/trigger 组合风险、server/update version 与 effect-time authorization，并把 group-level admission 置于工具调用之前。论文只在四类多工具场景、主流 LLM 与两个 MCP client 上报告平均攻击成功率超过 90%，不证明任意 client/trigger 都可攻破，也不证明组合防御不可能。组合状态未知或更新后证据失效时应 deny/quarantine，并交给独立 reference monitor 逐次授权；原有单工具扫描仍作为第一层共存。
- Exact-v1 Review-note families: `SF-2026-ARXIV-2606-27027`

## `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`

- Adjacent non-owner: `books/part-07-agent/83-mcp.md#L1`
- Owner-merged body: 当 verifier/critic 延迟相对任务传播可忽略时，在 agent 输出后统一纠错是合理的。约束变化是错误信念可能在校正到达前沿通信图传播，而过强或过迟的纠正还会造成振荡。多智能体 control state 因此要显式记录 verification dose、delay、corrector placement、graph version 与 belief epoch，把纠错部署视为带稳定性边界的控制问题。论文给出阈值与 greedy placement，并在五个开放模型上实验；它没有证明 signed-belief/delay 假设之外的任意拓扑或 Byzantine 行为，实验也受 grounded factual answering 任务限制。delay 或图版本未知时应序列化关键提交、使用 grounded deterministic verification，旧的事后 critic 只在低延迟区间共存。
- Exact-v1 Review-note families: `SF-2026-ARXIV-2606-27409`

## `INFER-SCHEDULING` → `books/part-05-inference-system/56-inference-scheduling.md`

- Adjacent non-owner: `books/part-05-inference-system/55-pd-disaggregation.md#L1`
- Owner-merged body: 当请求并发长期稳定时，部署阶段固定 tensor parallel 或 expert parallel 是合理的：它减少运行时重排并让容量规划可预测。约束变化在于 MoE decode 的并发会连续跨越两种并行方式的优势区间，静态选择会把阶段性通信瓶颈固化。因而调度状态需要增加并行形态、切换阈值、byte-identical expert weight/KV 的固定地址映射和 in-flight request epoch，由运行时只在 decode step 边界提交切换。论文在 8×H200、Qwen3-235B-A22B 上报告 215–434 ms 切换、2.4% memory overhead 与 RL rollout 1.16–1.25× 吞吐收益；这不证明未测模型、互联、并发轨迹或生产 tail latency 下仍安全。切换成本、地址一致性和抖动是新增 failure mode；证据不足或状态校验失败时继续使用静态 TP/EP，旧路径与动态路径按稳定性区间共存。
- Exact-v1 Review-note families: `SF-2026-ARXIV-2606-26607`

## `MULTIMODAL-EMBODIED-VLA` → `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`

- Adjacent non-owner: `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`
- Owner-merged body: 策略池固定且工作条件稳定时，为一次任务选择全局最优 expert 是可解释且低成本的。策略池持续增长后，选择问题分裂为两个控制动作：为新条件 commissioning 现有 expert，以及判断新 candidate 是否补足 incumbent 的真实 failure gap。VLA owner 因此要持有 condition split、outcome-disjoint probe、candidate version、probe budget 与 onboarding decision，只在新策略覆盖现有池无法处理的失败区间时提交上线。论文在 cost-matched probe budget 和五个 expert 上报告 held-out 60.53%、相对基线提升 1.64 个百分点；这不证明更大策略池、分布漂移或物理安全约束下仍成立。probe 泄漏、样本不足和错误 onboarding 会污染路由；置信度或 coverage 不足时保留 incumbent/default controller，并让人工或保守策略接管。
- Exact-v1 Review-note families: `SF-2026-ARXIV-2606-27355`

## `TRAIN-DISTRIBUTED-TRAINING` → `books/part-04-training-system/36-distributed-training.md`

- Adjacent non-owner: `books/part-04-training-system/37-tensor-parallel.md#L1`
- Owner-merged body: 以 element-wise optimizer state 做 ZeRO/FSDP 式分片，在更新可按参数局部计算时是合理的。矩阵级 Newton–Schulz optimizer update 却耦合整块矩阵，局部 post-processing 会让相同 checkpoint 在不同 layout 下产生不同语义。训练状态因此必须增加 matrix layout、collective algorithm、worker group 与 optimizer-step identity，把更新本身作为分布式矩阵操作并与 checkpoint 原子提交。论文在 embodied foundation model 与 LLM 训练中报告加速且性能接近 AdamW，但没有证明任意拓扑、矩阵形状或长程收敛与集中式实现等价。collective 中断、layout 漂移或数值分歧时应恢复最近一致 checkpoint，并退回已验证的 AdamW/旧 optimizer 路径；局部优化器与矩阵耦合优化器按更新结构共存。
- Exact-v1 Review-note families: `SF-2026-ARXIV-2606-27153`

## `TRAIN-RLHF` → `books/part-04-training-system/31-rlhf.md`

- Adjacent non-owner: `books/part-04-training-system/32-ppo.md#L1`
- Owner-merged body: 把 reward 当作同尺度、同步到达的标量，在 rater 同质且反馈能在 update 前返回时是合理的；现实约束同时来自身份异质性和时间异步性：不同 rater 的 offset/slope 不同，慢 verifier 或人工反馈又可能晚到数个 gradient step。RLHF 状态因此需要同时持有 rater identity、calibration slice/shrinkage prior/version，以及 pending reward queue、age/kernel、originating policy/importance ratio 与 reinjection mass。每位 rater 的 held-out affine calibration 可用 empirical Bayes 向总体收缩；迟到 reward 则以 clipped residual 进入后续 advantage。论文分别在 PRISM/PluriHarms 与 tabular MDP 上报告 RMSE 改善和最高 47.9× bias reduction，但没有证明非线性或 adversarial rater、online drift、large-scale RLHF 稳定性与生产 queue failure。稀疏 rater 回退总体 calibrator 并抽样审计；delay/mass 假设失效时等待慢反馈或采用 bounded synchronous update。
- Exact-v1 Review-note families: `SF-2026-ARXIV-2606-27578`, `SF-2026-ARXIV-2606-27580`

