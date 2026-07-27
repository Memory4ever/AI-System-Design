# 第73章 Memory

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 短期记忆、长期记忆和用户状态管理。

## 本章要回答的问题

Agent Memory 是聊天记录、向量数据库，还是模型之外的持久状态系统？什么应该被写入，何时压缩或遗忘？为什么错误 memory 比没有 memory 更危险？

本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**

## Context 与 Memory 的状态边界

```text
Memory M_t  --read/select--> Context C_t
Context + observation --write policy--> M_(t+1)
```

Context 只在当前 call 中可见；Memory 可跨 turns、sessions 或 tasks 存在。把全部 conversation 永久追加既不是可扩展 memory，也没有遗忘和纠错语义。

## Memory 类型是用途，不只是存储介质

| 类型 | 内容 | 典型生命周期 |
| --- | --- | --- |
| Working | 当前目标、plan、open steps | task 内 |
| Episodic | 某次交互/行动与结果 | 多任务，可压缩 |
| Semantic | 经验证的用户/领域事实 | 长期、可修正 |
| Procedural | workflow、工具使用经验 | 版本化、受治理 |

同一数据库可以存多类 memory，但 read/write policy 不应相同。一次失败尝试可以作为 episodic evidence，却不应直接升级为“用户偏好”。

## Memory Write 是高风险决策

每次模型输出都写入会产生：

- hallucination 持久化；
- prompt injection 跨会话存活；
- transient preference 被误当长期事实；
- 重复与冲突累积；
- 隐私和删除成本上升。

写入管线应是：

```text
candidate event
→ classify memory type
→ validate source and consent
→ deduplicate / conflict check
→ assign confidence and expiry
→ persist with provenance
```

高价值事实可要求用户确认或 authoritative source。Model-generated summary 必须标记为 derived，不应伪装成原始事实。

## Memory Read 是受约束检索

检索可综合：

```text
score(m)
= w_r * relevance
 + w_t * recency
 + w_i * importance
 + w_c * confidence
 - w_s * sensitivity_cost
```

该公式只是策略框架，权重由 use case 决定。读取前必须先做 tenant/user/agent authorization，再按当前 task 与 token budget 选择。

Recency 高不代表正确，similarity 高不代表可披露。Memory read 还要返回 source、time、confidence 和 supersession state。

## Consolidation 与 Forgetting

长期 event log 会无限增长。Consolidation 将多个 episodes 转成较高层 summary 或 semantic fact：

```text
episodes
→ cluster / detect pattern
→ propose summary
→ validate
→ link to sources
→ retain or expire raw records by policy
```

压缩会损失细节，所以 summary 应能追溯 source episodes。Forgetting 不是失败，而是必要能力：

- TTL/retention 到期；
- user deletion；
-事实被更新/superseded；
- sensitivity 超出用途；
- low-value state 淘汰。

删除必须传播到 embeddings、cache、summaries 和 backups policy。

## 一致性与并发

多个 Agent steps 或 devices 可能并发写同一用户状态。若最后写覆盖，可能丢失更新；若全部 append，读取时会看到冲突。

可按状态类型选择：

- append-only event + derived view；
- optimistic version/CAS；
- typed state machine；
- conflict set + explicit resolution。

自然语言 summary 不适合承担余额、审批状态或 exactly-once side effect。关键业务状态应留在 authoritative transactional system，Memory 只存 reference 和解释上下文。

## Memory 安全

Memory 是 durable attack surface。需要：

- provenance 与 trust labels；
- write/read authorization；
- encryption 和 tenant isolation；
- prompt injection scanning/containment；
- data minimization；
- retention/deletion；
- access and mutation audit。

“Agent 自己记住”仍然是平台执行的一次数据写入，必须受第 67～69 章治理。

## 评估 Memory

不能只看“记住了多少”。应测：

- write precision：写入内容是否值得保存；
- retrieval recall/precision；
- stale/conflict rate；
- downstream task success；
- token/storage/latency cost；
- privacy deletion completion；
- poisoning persistence 与 recovery。

无 memory baseline 很重要：若 memory 提升个性化却降低事实正确性，需要看到真实 trade-off。

## 本章在知识树中的位置

Prompt、Context、RAG、Memory 共同构成 Agent 的 information state。下一章引入 action：Tool Calling 如何把模型输出转换为对外部环境的 typed proposal，并由平台决定是否执行。

## 自检问题

1. Context 与 Memory 的读写关系是什么？
2. 为什么所有对话都永久写入不是合理 memory？
3. Episodic 与 semantic memory 的升级条件有何不同？
4. Memory summary 为什么要保留 source links？
5. 哪些状态不应只存自然语言 memory？
6. 如何评估 memory poisoning 的持续影响？

## 小结

Memory 的价值来自受治理的保存、选择和遗忘，而非积累最多文本。可靠 Memory 保留 provenance、confidence、authorization 和修正路径。下一章从信息状态进入外部行动。

## Review notes

本章以 runtime persisted state 为中心，不把模型参数或 KV Cache 称为 Agent Memory。MemGPT 的分层管理和 Generative Agents 的 observation/reflection architecture 作为设计案例，不被外推为统一实现。

Primary-source 入口：

- MemGPT: https://arxiv.org/abs/2310.08560
- Generative Agents: https://arxiv.org/abs/2304.03442
- Reflexion: https://arxiv.org/abs/2303.11366
