# 第78章 Multi-Agent

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 多个智能体之间如何分工、协作和互相校验。

## 本章要回答的问题

为什么创建多个 persona 不自动带来更强能力？Multi-Agent 何时提供并行、专业化或独立校验，何时只放大 token 成本、共识偏差和状态混乱？多个 Agent 的权限与责任如何隔离？

本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**

## 先建立单 Agent Baseline

一个模型可以在不同步骤切换 role。把同一模型复制成 planner、coder、reviewer，若它们共享训练分布、Context 和 evidence，错误高度相关。

Multi-Agent 引入额外成本：

```text
total_cost
= model calls
 + inter-agent messages
 + context duplication
 + coordination
 + merge / conflict resolution
 + longer critical path
```

因此应先比较单 Agent、单 Agent + deterministic verifier、单 Agent + parallel tools，再判断多 Agent 是否有增量价值。

## 什么时候分解有意义

常见有效条件：

- 子任务可并行且输出 contract 清晰；
- 需要不同 tools、models、data scopes 或 expertise；
- verifier 与 generator 有相对独立 evidence；
- 需要职责分离或不同 authorization；
- environment 天然包含多个 actors；
- 搜索空间可由多种策略探索。

如果所有 agent 读取同一错误文档、使用同一模型并互相复述，讨论轮数不会创造新证据。

## 典型拓扑

**Supervisor/Worker**

```text
Supervisor
├─ Worker A
├─ Worker B
└─ Verifier
```

控制简单，但 supervisor 成为 bottleneck 和 single point of interpretation。

**Peer/Debate**

多个 agent 提出或批评候选，再由规则或 judge 选择。适合探索，不保证 majority 正确；同源模型可能形成 correlated consensus。

**Blackboard/Shared State**

Agent 通过 typed artifacts 和 shared workflow state 协作，而不是无限聊天。可追踪性更强，但需要 concurrency、ownership 和 conflict rules。

**Pipeline**

固定角色顺序，实际更接近 Workflow；不应仅因每步使用模型就称为自主 multi-agent system。

## Message 不是 State

Agent-to-agent chat 容易混合事实、建议和控制指令。共享状态应区分：

```text
task facts / evidence
proposals
decisions
artifacts
ownership
workflow status
```

Message 作为 event 保留，authoritative state 由 workflow transition 更新。一个 agent 说“B 已完成”不能替代 B 的 signed/verified output。

## Identity 与 Delegation

每个 agent 需要独立 runtime identity：

- owner、version、model/prompt；
- allowed data/tools/scopes；
- delegated authority；
- budget；
- parent workflow；
- audit principal。

Delegation 不能把调用者所有权限复制给子 Agent。应发放 task-scoped、time-bound、least-privileged credentials，并保留 delegation chain。Agent 不能继续任意转委托。

## Coordination Failure

典型失败包括：

- circular delegation；
- duplicate work/side effects；
- deadlock/livelock；
- inconsistent world models；
- stale messages；
- ownership gap；
- consensus without evidence；
- malicious/compromised peer。

Runtime 需要 max handoffs、dedup keys、leases、timeouts、conflict resolution 和 escalation。自然语言“请协调好”不是协议。

## Verification 与 Aggregation

将多个答案平均或投票只在错误具有一定独立性时有效。对于开放任务，更可靠的方法是：

- 先定义 rubric/test；
- 保持 candidate generation 与 evaluation 隔离；
- 要求引用独立 evidence；
- 记录 disagreement；
- 对高风险冲突升级给人；
- 比较 aggregate result 与 best single baseline。

Judge model 自身也要版本化和评估。

## Evaluation

除了 final task success，还要测：

- contribution by agent/role；
- parallel speedup 与 critical path；
- token/tool/coordination cost；
- duplicate/conflicting actions；
- handoff failure；
- consensus calibration；
- security scope violations；
- recovery after one agent failure。

Multi-Agent 的 throughput 不等于 LLM serving batching；底层请求仍由 Part IV 调度。

## 本章在知识树中的位置

Workflow 提供 durable shared state，Multi-Agent 在其上分配责任。下一章 MCP 讨论 Agent/host 如何通过标准协议发现 tools、resources 和 prompts；MCP 可以连接角色，却不定义协作策略。

## 自检问题

1. 多个 persona 为什么不自动带来独立能力？
2. 什么条件下 Multi-Agent 分解有真实价值？
3. Message 与 authoritative state 为什么要分开？
4. Delegation 为什么不能复制父 Agent 全部权限？
5. Majority vote 何时会形成错误共识？
6. Multi-Agent evaluation 为什么必须包含 coordination cost？

## 小结

Multi-Agent 的收益来自真正的任务、证据、模型或权限分解，而不是更多对话。稳定系统依赖 typed handoffs、shared workflow state、bounded delegation 和独立 verification。下一章进入连接标准 MCP。

## Review notes

本章把 AutoGen/CAMEL 作为多 Agent interaction 的研究入口，不把 framework API 当作系统原理。与第 77 章分责：Workflow 拥有状态，Agents 拥有受限决策角色。

Primary-source 入口：

- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- Generative Agents: https://arxiv.org/abs/2304.03442
