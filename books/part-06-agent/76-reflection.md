# 第76章 Reflection

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
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

Self-Refine 让同一模型产生 feedback 和 revision；Reflexion 将环境反馈总结为语言并写入 episodic memory。二者都是 test-time adaptation，不等同于第 27～30 章的参数训练或 policy optimization。

## Feedback 来源决定价值

Feedback 可以来自：

| 来源 | 示例 | 独立性 |
| --- | --- | --- |
| Deterministic verifier | compiler、tests、schema、constraint solver | 高 |
| Environment | API result、game state、user correction | 中高 |
| Separate evaluator | judge model、specialized classifier | 取决于模型/数据 |
| Same model self-critique | “检查自己的答案” | 低 |

同一模型可能在 generation 与 critique 中重复同一盲点。External tests 和 environment outcomes 通常比自由文本“再想想”更可操作。

## Reflection 应输出可执行诊断

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

## 小结

Reflection 的价值来自 evidence-backed feedback 和有界修正，而不是让模型无限解释自己。下一章用 Workflow 为这些循环提供持久状态和确定控制。

## Review notes

本章明确区分 inference-time verbal feedback 与 Part III 的 RLHF/PPO/GRPO/DPO。论文中的任务级收益不被写成通用保证，成本与 verifier 误差一并保留。

Primary-source 入口：

- Reflexion: https://arxiv.org/abs/2303.11366
- Self-Refine: https://arxiv.org/abs/2303.17651
- ReAct: https://arxiv.org/abs/2210.03629
