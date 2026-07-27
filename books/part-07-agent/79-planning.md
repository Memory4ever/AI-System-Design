# 第79章 Planning

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-PLANNING`
**Legacy Chapter:** Ch75
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

对于 evidence-acquisition task，并行轴不能简化成“同时开更多搜索”。依赖图应先区分可独立 subquery 与需要
前序证据才能定义的分支，再把有限 search/tool budget 分给 ready nodes：

```text
goal → dependency-aware evidence graph
→ parallel acquisition on ready independent nodes
→ deduplicate / verify / merge at checkpoints
→ open dependent nodes or backtrack
```

并行可缩短 critical path，却会复制 query、Context 和外部配额；错误 observation 还可能同时污染多个分支。
Search More, Think Less 与 LongVideo-R1 分别在网页 evidence 与长视频 active perception 中提供受限案例，
支持“并行 acquisition + hierarchical checkpoint”，不证明宽度越大越好。单链搜索在依赖强、预算小或 verifier
弱时仍更稳。

## Replanning 的触发条件

执行 observation 可能显示：

- precondition 不成立；
- tool/API 变化；
- data 缺失或冲突；
- budget 即将耗尽；
- user goal 改变；
- step 失败但存在替代路径。

Runtime 应在这些事件触发 replanning，而不是每一步都从零规划，也不是无条件坚持原计划。Plan version 与 superseded steps 要保留，便于审计。

Replanning 前还要区分两个 failure channel：计划图本身不可行，还是 action 执行偏离了一个本来可行的计划。
前者需要修改依赖、资源或目标；后者应先约束 executor、修正 mismatch，再决定是否废弃 plan：

```text
plan graph + resource / temporal constraints
→ solver or deterministic feasibility check
→ constrained execution with step evidence
→ compare observed transition with planned transition
→ repair execution or version the plan
```

外部 solver 提高可判定约束的一致性，却会把建模错误、离散化和 solver availability 变成新边界；开放世界或
语义目标不能全部形式化。TAPE 的合成任务支持 feasibility/execution-conformance 分离，不证明形式求解器能覆盖
所有 Agent planning。短任务和低副作用场景仍可用轻量 plan + observation-triggered replanning。

## Search-based Planning 的边界

Chain-of-Thought 产生一条路径；Tree of Thoughts 等方法探索多个候选并评价/回溯。搜索可以提高某些任务成功率，却使模型 calls 近似随 branching factor 和 depth 增长：

```text
candidate_nodes ≈ 1 + b + b^2 + ... + b^d
```

Pruning、heuristic、budget 和 verifier quality 决定是否值得。模型自己生成并评分候选可能共享同一盲点，搜索更多不等于可靠性单调提高。

在部分可观测环境中，固定 branching factor 也会浪费预算：某些节点只有一个可信方向，另一些节点存在
高 epistemic uncertainty。Planner 可以把“请求展开”显式化，并给整棵搜索树共享 leaf budget：

```text
current belief node
→ expose uncertainty / branch request
→ allocate bounded local alternatives
→ execute or simulate observations
→ prune by external evidence
→ return unused budget to global pool
```

自报 uncertainty 不是可信概率，teacher retro-annotation 也可能教会格式而非真实校准；因此 branching request
只能影响候选预算，不能绕过 policy、tool authorization 或 completion evidence。固定单路径在低风险、成本敏感
或 verifier 弱时仍合理；固定宽搜索在可并行且每个分支便宜时更可复算。动态 branching 只有在 uncertainty
calibration、global budget 和 branch-state identity 同时可观测时才有意义。

Tool 本身有价格、延迟或有限调用次数时，planning 还要把 information value 与机会成本放在同一个 belief state。
预先固定“最多 N 次调用”容易复算，却会在简单问题上浪费、在关键分叉前耗尽。Budget-aware planner 可在每一步估计：

```text
belief over task state
+ remaining cost / time / call budget
+ tool price, reliability and expected information gain
→ choose act, ask, verify or stop
→ update belief and remaining budget from observation
```

这不是把未知任务压成精确 knapsack。模型估计的成功概率和 information gain 可能失准，tool pricing、latency 与
version 也会变化；平均成本最优还可能牺牲 worst-case safety 或高价值少数请求。静态 budget 在成本稳定、风险高或
calibration 弱时仍更可靠。动态分配必须保留 hard cap、reserve for verification、stop/fallback policy，并按 task slice
校准实际 utility，而不是让 planner 用自己的主观置信度证明自己值得继续花费。

剩余预算不只是外层 hard cap，也可以成为 tree selection state。固定宽度或并行采样在分支便宜、critic 弱或
低 latency 依赖并行时仍合理；当不同路径共享前缀且 tool/output token 都昂贵时，planner 可以在每个 node 保存
累计 value、访问次数、父子关系和剩余资源，再根据资源收紧程度逐步从探索转向利用：

```text
node value + uncertainty + remaining multi-resource budget
-> widen / deepen / answer / stop
-> execute and observe
-> update path statistics and remaining budget
```

Critic call 自身也消耗 token、latency 与 cache，不能被排除在 budget 外；耗尽预算后强制回答只证明 termination，
不证明 correctness。Budget-Aware Value Tree 的作者实验支持这一控制面在其检索问答中改变 quality/cost frontier，
但其 deterministic positive-delta 等理论假设不适用于开放环境。多工具价格、deadline 与不可逆风险不能压成一个
无量纲比率；高风险或 calibration 弱时仍应使用静态上限、保留 verification reserve，并允许 abstain。

跨尝试 replanning 还可以把 planner history 从自然语言反思提升为可审计 path state：operation DAG、结构 prior、
execution count、observed return/error 与 environment revision 分开保存。Macro path 能减少 token-level search，
却会漏掉未建模操作；UCB-like statistics 依赖 reward stationary，derived advice 还可能固化 parser/judge error。
Deep Tabular Research 的受限证据支持 execution feedback 与 path statistics 可以共同驱动 replan，不证明多数投票
消除相关错误。干净 schema/短查询继续适合 direct execution；新颖一次性任务在历史不可靠时应回到 stateless
search，任何跨 query state 都必须防止 tenant 污染和 benchmark-order leakage。

### 先校准不确定性，再决定行动、询问或探索

成本感知 planning 的关键并不是让模型输出一个置信度，而是把 prior、可获得 observation、action cost 与错误后果绑定到同一 decision contract：

```text
calibrated prior over task state
+ expected information gain of ask / explore
+ action, delay and failure cost
→ act / ask / gather evidence / defer
→ update belief from an observed outcome
```

合成环境中拟合的 prior 不能直接当作生产概率；cost 也不只是 token 数，还可能包括用户中断、工具价格、延迟与不可逆副作用。因此 expected utility policy 必须受 hard safety override、预算上限和低置信 fallback 约束，并按 deployment slice 重新校准。固定 rule 在样本少、概率失准或风险极高时继续合理；Calibrate-Then-Act 只为受控低维任务中的 uncertainty/cost-conditioned exploration 提供实验性证据，不证明现实 Agent 已获得全局最优行动策略。

### 局部 Replan 后必须回归全部已接受约束

Feedback-conditioned planning 若只修复本轮新暴露的问题，容易破坏先前已满足的 world、user 或 policy constraint。
Planner 因而需要一份带 authority、valid-time 和 provenance 的 cumulative ledger，并在每次 plan revision 后重新
验证全部仍有效 invariants：

```text
new observation / user clarification / policy feedback
→ append or supersede typed constraint
→ produce a new plan revision
→ regression-check every active constraint
→ execute only after global evidence passes
```

Ledger 减少重复违反，却增加 conflict、staleness、token/selection cost 与 oracle dependence；world fact、user
preference 与 immutable policy 也不能由同一 judge 随意改写。一次性 planning 在约束完整稳定、交互预算低时仍
合理。AdaPlanBench 的 text-only household simulator 只支持“terminal constraint-valid 不等于 plan effective”以及
局部 repair 会回归的受限证据，不证明 text plan 已在真实环境成功执行。

## Goal、Constraint 与 Policy

用户 goal 不等于无限授权。Planner 必须接收不可变 constraints：

- allowed tools/scopes；
- data/tenant boundary；
- time/token/cost budget；
- approval requirements；
- forbidden side effects；
- SLO/deadline。

模型可以选择满足约束的路径，不能在“任务需要”时自行放宽约束。Policy enforcement 位于 executor/workflow。

### 从 Project Brief 到可验证 Task Contracts

一句 project brief 直接 fan-out 给多个 executors，容易产生重复工作、遗漏、共享 asset 冲突和贡献边界模糊。
自然语言 decomposition 只有在被编译成带 identity 的 task contracts 后，才成为可执行协作接口：

```text
project goal / constraints
→ innovation atoms and dependency lineage
→ compare decomposition strategies
→ task contracts: objective, boundary, owner, inputs, outputs, shared assets, order
→ execution evidence
→ repair graph without silently changing accepted constraints
```

Planner 拥有分解与 dependency graph，executor 只拥有被授予的 task，Workflow 才拥有 durable commit/retry。
Contract 过细会压制探索，过粗则重新引入 overlap；LLM judge 对 coherence 的评分也不能替代 artifact integration。
Project2Task 的 10 个 research briefs 只为该编译结构提供实验性证据，不证明一般科研质量。单人任务、强耦合探索
或目标仍高度不确定时，共享 working session 与少量人工 milestone 仍比过早 taskization 更合理。

## 完成证据与 Verification

每一步需要 machine-checkable evidence，例如 test pass、resource state、signed response、human approval。模型说“已完成”不是完成条件。

对于无法自动验证的开放任务，可使用 rubric、多样化 reviewers、sampled human review 和 uncertainty escalation，但要标明仍是经验判断。

长程任务的 subgoal 不应只是自然语言分解标签，而应成为可验证 milestone：每个 milestone 绑定 expected
state、checker、supersession 和完成证据；环境 observation 触发 replanning，milestone progress 还可作为
受限训练信号。这样把稀疏终局反馈前移，却新增错误 checker、过早终止和为了 milestone 得分而偏离最终目标。
任务短、状态不可可靠检查或 action 不可逆时，少量人工 checkpoint 与 approval 仍比自动细分更稳健。

## 本章在知识树中的位置

Tool Calling 定义单次 action contract，Planning 组织多个可能 action。下一章研究 Reflection：当 observation 或 verifier 暴露缺陷时，系统如何产生反馈并修正，而不是无限自我批评。

第25章的 World Model 可以为本章生成 imagined rollouts；第26章的 controller 仍独立拥有 physical action authority。Planner 选择模型内高分轨迹不构成执行许可，必须经过 uncertainty、policy、freshness、safety envelope 与真实 observation reconciliation。

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

- AdaPlanBench（cumulative constraint ledger；Status: Experimental）: https://arxiv.org/abs/2606.05622

本章不把 hidden reasoning 当作 durable workflow state；第 81 章拥有持久执行和重试。ReAct/Tree of Thoughts 作为经验机制，结论不外推到所有模型和任务。

Primary-source 入口：

- ReAct: https://arxiv.org/abs/2210.03629
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- Chain-of-Thought prompting: https://arxiv.org/abs/2201.11903
- SPARK（uncertainty-triggered bounded branching；Status: Experimental）:
  https://arxiv.org/abs/2601.20209
- DeepPlanning（constraint-rich closed-world planning evaluation）:
  https://arxiv.org/abs/2601.18137
- INTENT（budget-constrained costly-tool planning；Status: Experimental）:
  https://arxiv.org/abs/2602.11541
- Calibrate-Then-Act（prior-calibrated cost-aware exploration；Status: Experimental）:
  https://arxiv.org/abs/2602.16699
- Search More, Think Less（dependency-aware parallel evidence acquisition；Status: Experimental）:
  https://arxiv.org/abs/2602.22675
- LongVideo-R1（hierarchical active-perception planning；Status: Experimental）:
  https://arxiv.org/abs/2602.20913
- TAPE（plan feasibility 与 execution conformance 分层；Status: Experimental）:
  https://arxiv.org/abs/2602.19633
- Subgoal-driven Long-Horizon Agents（verifiable milestones；Status: Experimental）:
  https://arxiv.org/abs/2603.19685
- Project2Task（project brief 到 task contract；Status: Experimental）:
  https://arxiv.org/abs/2608.05225
