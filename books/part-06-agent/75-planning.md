# 第75章 Planning

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 复杂任务如何被拆解、排序和执行。

## 本章要回答的问题

Planning 与“先输出步骤列表”有何不同？为什么一个看起来合理的计划在执行中会迅速失效？Agent 应一次规划到底，还是在 observation 后持续 replanning？

本章的核心判断是：**Plan 是关于未来状态转移的可验证假设，应显式表达目标、前置条件、依赖、资源和完成证据；在部分可观测环境中，planning 与 execution 必须通过 observation 反复闭环。**

## Plan 不是解释文本

朴素计划：

```text
1. Analyze
2. Implement
3. Test
```

它没有输入、完成条件、依赖或失败分支，无法驱动 runtime。更可执行的 plan node 包含：

```text
step_id
goal / expected state
preconditions
action or tool class
inputs and dependencies
success evidence
risk / approval class
budget
status
```

自然语言可以描述意图，typed state 承担控制。

## 从目标到状态图

设环境状态为 `s_t`，action 为 `a_t`，observation 为 `o_(t+1)`：

```text
a_t = policy(goal, belief_t, plan_t)
o_(t+1) = environment(s_t, a_t)
belief_(t+1) = update(belief_t, o_(t+1))
```

Agent 通常不能直接观察完整 `s_t`，只能维护 belief/context。计划因此不是确定执行轨迹，而是基于当前信息的 conditional policy。

## Decomposition 的价值与代价

拆分任务可以：

- 降低单步复杂度；
- 暴露可验证 intermediate results；
- 允许并行与不同 tools；
- 提前识别 approval/risk。

过度拆分则增加：

- model/tool calls；
- context growth；
- state handoff error；
- orchestration latency；
- 局部目标偏离整体目标。

拆分粒度应由可验证边界决定，而非步骤越多越“智能”。

## 依赖、并行与 Critical Path

Plan 更接近 DAG/state machine：

```text
collect requirements ─┬→ implementation → tests
                      └→ risk review ────┘
```

无依赖步骤可以并行，但共享资源和副作用仍需 coordination。总时长由 critical path 和 queue/resource constraints 决定，不能简单等于各步平均时间。

并行还会增加 merge/conflict 成本，只有当步骤输出 contract 清晰时才有效。

## Replanning 的触发条件

执行 observation 可能显示：

- precondition 不成立；
- tool/API 变化；
- data 缺失或冲突；
- budget 即将耗尽；
- user goal 改变；
- step 失败但存在替代路径。

Runtime 应在这些事件触发 replanning，而不是每一步都从零规划，也不是无条件坚持原计划。Plan version 与 superseded steps 要保留，便于审计。

## Search-based Planning 的边界

Chain-of-Thought 产生一条路径；Tree of Thoughts 等方法探索多个候选并评价/回溯。搜索可以提高某些任务成功率，却使模型 calls 近似随 branching factor 和 depth 增长：

```text
candidate_nodes ≈ 1 + b + b^2 + ... + b^d
```

Pruning、heuristic、budget 和 verifier quality 决定是否值得。模型自己生成并评分候选可能共享同一盲点，搜索更多不等于可靠性单调提高。

## Goal、Constraint 与 Policy

用户 goal 不等于无限授权。Planner 必须接收不可变 constraints：

- allowed tools/scopes；
- data/tenant boundary；
- time/token/cost budget；
- approval requirements；
- forbidden side effects；
- SLO/deadline。

模型可以选择满足约束的路径，不能在“任务需要”时自行放宽约束。Policy enforcement 位于 executor/workflow。

## 完成证据与 Verification

每一步需要 machine-checkable evidence，例如 test pass、resource state、signed response、human approval。模型说“已完成”不是完成条件。

对于无法自动验证的开放任务，可使用 rubric、多样化 reviewers、sampled human review 和 uncertainty escalation，但要标明仍是经验判断。

## 本章在知识树中的位置

Tool Calling 定义单次 action contract，Planning 组织多个可能 action。下一章研究 Reflection：当 observation 或 verifier 暴露缺陷时，系统如何产生反馈并修正，而不是无限自我批评。

## 自检问题

1. 步骤列表为什么不是可执行 plan？
2. 部分可观测性如何改变 planning？
3. Decomposition 过细会引入什么成本？
4. Replanning 应由哪些事件触发？
5. Tree search 的调用成本怎样增长？
6. 为什么模型不能自行修改 constraints？

## 小结

Planning 把 goal 转成带依赖、前置条件和证据的可修正状态图。它的可靠性来自 execution observations 与外部 constraints，而非计划文本的流畅度。下一章进入反馈和修正。

## Review notes

本章不把 hidden reasoning 当作 durable workflow state；第 77 章拥有持久执行和重试。ReAct/Tree of Thoughts 作为经验机制，结论不外推到所有模型和任务。

Primary-source 入口：

- ReAct: https://arxiv.org/abs/2210.03629
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- Chain-of-Thought prompting: https://arxiv.org/abs/2201.11903
