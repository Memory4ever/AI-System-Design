# 第80章 Reflection

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-REFLECTION`
**Legacy Chapter:** Ch76
**Status:** Draft

**Roadmap Intent:** 模型如何基于反馈修正自己的中间结果。

## 本章要回答的问题

Reflection 为什么有时能改进结果，有时只会把错误解释得更流畅？它与 verifier、retry、RLHF 和训练更新有何区别？何时应该停止迭代并升级给人？

本章的核心判断是：**Reflection 是 inference-time feedback loop：根据可观察结果生成诊断，再修正 plan、output 或 memory。它不更新模型参数，效果受 feedback independence、verifiability 和 stopping policy 限制。**

## 基本循环

```text
candidate y_0
→ feedback f_0 = evaluate(y_0, evidence)
→ revised y_1 = refine(y_0, f_0)
→ ...
→ accept | stop | escalate
```

Self-Refine 让同一模型产生 feedback 和 revision；Reflexion 将环境反馈总结为语言并写入 episodic memory。
二者是**不修改权重的 verbal test-time adaptation**，不等同于第 31～34 章的参数训练或 policy optimization。
更激进的分支会在 episode 内把 retrospective feedback 编译成 LoRA/weight update；它仍发生在 test time，
但 ownership 已跨入参数状态，不能继续只称为 Reflection：

```text
trajectory + outcome
→ retrospective diagnosis
→ bounded adaptation dataset / objective
→ ephemeral parameter update
→ validation on next attempt
→ commit, reset or rollback
```

这可能把经验从 Context 内化到 policy，却新增 optimizer state、base/adapter identity、catastrophic drift、
contamination 和 rollback。Verbal reflection 在任务短、风险高或不能验证更新时继续成立；参数 adaptation 只有
在 scope、budget、held-out verifier、reset 和 provenance 明确时才可使用。Reflective Test-Time Planning 的
论文提供了这一边界案例，不证明 episode-level LoRA update 普遍优于语言反馈。

## Feedback 来源决定价值

Feedback 可以来自：

| 来源 | 示例 | 独立性 |
| --- | --- | --- |
| Deterministic verifier | compiler、tests、schema、constraint solver | 高 |
| Environment | API result、game state、user correction | 中高 |
| Separate evaluator | judge model、specialized classifier | 取决于模型/数据 |
| Same model self-critique | “检查自己的答案” | 低 |

同一模型可能在 generation 与 critique 中重复同一盲点。External tests 和 environment outcomes 通常比自由文本“再想想”更可操作。

多约束任务还存在一种有用的不对称：一次发现同时满足所有条件的 candidate 可能很难，
但检查 candidate 是否分别满足每个条件往往更容易。Reflection 因而不应只输出整体
“通过/失败”，而应把 verification 结果转成下一轮的控制信号：

```text
provisional candidate
→ constraint-wise audit
→ verified | unresolved | conflicting | invalidated
→ preserve valid progress
→ target the remaining uncertainty
```

这并不保证 verifier 正确；它只是避免每轮从零搜索，或在已有证据尚未满足所有约束时
过早接受答案。

## Reflection 应输出可执行诊断

### Verification-centric Reflection：先定位 Evidence Gap，再决定重跑什么

Deep Research 的失败可能来自问题构造、证据检索、trajectory synthesis、candidate answer 或 final selection。
只让模型“再想一次”会把这些 failure planes 混在同一段文字里。更可靠的反思对象是 versioned evidence graph：
verifier 输出哪个 claim 缺 source、哪条 path 矛盾、哪个 tool result 不足，再由 workflow 选择局部 repair、
discard-all restart 或停止。

这种结构增加 verifier/tool critical path，也会继承 same-model judge bias；高置信、短链路任务仍可直接 retry。
Marco DeepResearch 的数据构造与 inference loop 提供一个受限实例，但其 call budget、judge 与 mixed baselines
不能外推为通用 deep-research policy。

### 从固定 Reflection Prompt 到 Learned Adaptation Policy

当同一 task 可以从 reset state 重复运行，并能比较 episode outcome 时，可以离线学习一个 meta-policy，把前序
episode evidence 编译成下一 episode 的 actor prompt/state update。Workflow owner 必须持有 environment reset、
episode budget、mutable prompt fields、policy revision 与 rollback；模型文本不能自行宣称 reset 或越过 immutable
safety policy。

Learned reflection 可能减少手工规则，却新增 meta-overfitting、cross-episode leakage、prompt drift 与额外调用成本。
固定规则在 episode 少、reset 不可靠或 safety surface 不可修改时仍成立。Meta-TTL 的作者结果是 Experimental
case，不证明任意 OOD domain 都能通过 test-time reflection 自我改进。

有用 feedback 应定位：

```text
failed criterion
evidence
suspected cause
affected plan/output state
proposed bounded change
confidence
```

“答案不够好，请改进”会导致无方向重写。结构化 diagnostics 让 workflow 决定局部重试、replan 或回滚。

### 从“结果失败”到“最早可修复偏离”

最终 outcome 只能说明整条 trajectory 没有满足目标，不能直接说明应该从哪里修。长链路中，后续
步骤可能只是沿着早期错误继续执行；若 Reflection 只重写最后答案，它会保留真正的因果偏离，
若整条轨迹从头再跑，又会丢掉已经验证的工作并重复支付 tool 与 token 成本。

更可操作的 failure audit 应把三个问题分开：

```text
localize earliest evidence-backed critical step
→ attribute a bounded root cause
→ emit a repair directive and affected-state boundary
→ resume, replay or replan under an explicit gate
```

`critical step` 不是“第一个不完美动作”，而是最早有证据支持、并对最终失败具有直接因果意义的
偏离；证据存在容忍区间时，应保留一个 step span，而不是制造虚假的单点精度。Root cause 也不应
只写成模型能力标签，而要落到可改变的 failure class，例如 retrieval coverage、evidence misuse、
constraint violation、premature conclusion 或 environment/tool error。Repair directive 必须引用相关
evidence 和仍然有效的 state，不能只是重新措辞原问题。

多视角 auditor 可以分别从最终约束向后追溯、沿 timeline 向前检查，再由显式 evidence 进行
adjudication；多数票只有在错误近似独立时才增加可信度。离线 frozen trace 还存在硬边界：它不能
恢复未记录的 environment state，单一 primary-cause schema 也会压扁多个共同致因。因此高风险
failure 仍需人工复核，在线 resume 前还要重新验证外部状态和副作用。

SearchAuditor 是这一路线的实验性案例。它的公开结果来自已知失败、可在冻结轨迹中定位的
deep-search runs；端到端 audit 即使在作者最佳配置下也远未成为可靠 oracle。本章吸收
`localize → attribute → repair` 的控制分解，不把论文准确率、错误分布或恢复率外推到其他 Agent、
工具环境和生产流量。

对长时程研究，diagnostics 还应形成 task-scoped improvement state：保留已验证 evidence
及 provenance、未满足约束、冲突、已淘汰 candidate 与下一步 objective，删除重复
observation 和已失效 plan。它比普通摘要更接近状态压缩，因为压缩目标不是“更短”，
而是保留下一次决策所需的事实边界。

AREX 为这种双层 research / audit loop 和 improvement state 提供了一个实验性实现。
论文结果来自作者在 deep-research、reasoning 与 tool-use benchmarks 上的实验，尚无
独立复现；本章只吸收机制边界，不把其模型规模、训练 recipe 或 benchmark gain 外推为
通用 Reflection 收益。

## 反思对象要分开

系统可以修正：

- output：格式、事实、表达；
- tool arguments：参数或目标；
- plan：依赖、顺序、替代路径；
- context：缺 evidence、冲突、压缩损失；
- memory：错误写入、过期事实；
- policy configuration：只能由授权 owner 修改。

模型不能通过 reflection 宣称安全 policy 是阻碍并自行删除。Policy violation 的正确动作通常是 reject/escalate。

## Stopping Policy

无限循环会消耗 token、tool calls 和 wall time，并可能来回振荡。停止条件可包含：

```text
verifier passes
max_iterations
no material delta
same failure repeats
budget/deadline reached
risk threshold exceeded
human decision required
```

Runtime 必须持久化 attempt、feedback 和 decision。只把全部历史重新塞入 Context 会越来越长，还可能强化错误。

每一步都调用强 critic 可以更早纠偏，却把成本和 critic 盲点放大到整条 trajectory。一个分层 monitor 可先用
便宜、已校准的 uncertainty proxy 检测 search/reasoning drift，只在残差越界时触发 slow critic 与经验检索：

```text
cheap trajectory sensor
→ calibrated normal relation / threshold
→ selective slow diagnosis
→ bounded repair or memory proposal
```

Token entropy、embedding cluster entropy 等只是 proxy，不是 factual confidence；threshold 会随模型、retriever
和 domain 漂移。未校准或高风险任务仍应直接使用 deterministic verifier/strong review，slow critic 的输出也
必须经过第 77 章的 Memory write gate。分层监控优化的是 critique allocation，不是让 self-reflection 成为 oracle。

压缩后的 improvement state 仍属于当前 run 的 working state，不应仅因它概括了经验就
自动升级为第 77 章的长期 Memory。跨任务写入仍需要 source、scope、confidence、expiry
和 supersession policy。

## Reflection 与 Retry 的区别

Retry 对相同 operation 再执行，适合 transient failure；Reflection 修改 candidate/plan 后再尝试，适合可诊断缺陷。

若失败来自 authorization deny，重复或改写调用不应绕过 policy。若远端 action outcome ambiguous，应先 reconcile state，而不是让模型“换一种方式再做一次”。

## 写入 Memory 的风险

Reflexion 风格系统会保存 linguistic feedback。只有当 feedback 与 task result 绑定、可追溯且适用范围明确时，才应进入 Memory。

一次任务的 workaround 不一定是全局 procedure；错误 critic 可能成为 durable poisoning。Memory write policy 应记录 source、confidence、scope、expiry 和 supersession。

## Evaluation

应比较：

- first-attempt success；
- final success after reflection；
- iterations/cost/latency；
- verifier false accept/reject；
- regression introduced by revision；
- repeated failure classes；
- escalation quality；
- memory transfer to new tasks。

只报告 final success 会隐藏十倍调用成本和失败样本选择偏差。

## 本章在知识树中的位置

Planning 产生预期路径，Reflection 消费实际反馈并修正。下一章 Workflow 将两者放入 durable state machine，确保 retries、approvals、timeouts 和 side effects 在进程失败后仍有一致语义。

## 自检问题

1. Reflection 为什么不等于参数训练？
2. 同一模型 self-critique 有什么相关性风险？
3. 哪类 feedback 最容易转成可验证修正？
4. Reflection 与 retry 的适用失败类型有何不同？
5. 为什么 policy deny 不应触发“换种方式”绕过？
6. Reflection 写入 Memory 需要哪些限制？
7. Task-scoped improvement state 与普通摘要、长期 Memory 有什么不同？

## 小结

Reflection 的价值来自 evidence-backed feedback、constraint-wise audit 和有界修正，
而不是让模型无限解释自己。Task-scoped improvement state 保存下一轮所需的有效进展，
但不自动成为长期 Memory。下一章用 Workflow 为这些循环提供持久状态和确定控制。

## Review notes

- Marco DeepResearch（verification-centric repair；Status: Experimental）: https://arxiv.org/abs/2603.28376
- Meta-TTL（learned test-time adaptation policy；Status: Experimental）: https://arxiv.org/abs/2604.00830

本章明确区分 inference-time verbal feedback 与 Part IV 的 RLHF/PPO/GRPO/DPO。论文中的任务级收益不被写成通用保证，成本与 verifier 误差一并保留。

Primary-source 入口：

- Reflexion: https://arxiv.org/abs/2303.11366
- Self-Refine: https://arxiv.org/abs/2303.17651
- ReAct: https://arxiv.org/abs/2210.03629
- AREX, 2026, `Status: Experimental`: https://arxiv.org/abs/2607.21461
- SearchAuditor, 2026, `Status: Experimental`: https://arxiv.org/abs/2608.05212
- Deep Search with Hierarchical Meta-Cognitive Monitoring（Status: Experimental）:
  https://arxiv.org/abs/2601.23188
- Reflective Test-Time Planning（reflection-guided parameter adaptation；Status: Experimental）:
  https://arxiv.org/abs/2602.21198
