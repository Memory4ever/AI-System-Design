# Lab 14 — Agent Information State

## Lab Question

Prompt、Context、RAG 与 Memory 怎样在不同生命周期中组织信息，并保持 provenance、freshness、scope 与删除边界？

## Why This Lab Exists

把所有信息放进 Prompt 在短任务中透明可靠；任务变长后，Context budget、外部知识 freshness 与历史复用成为
瓶颈。RAG 增加外部 evidence，Memory 增加跨 run state，却也可能把错误、过期或越权信息持久化。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `AGENT-PROMPT` | Ch74 | Soft instruction/interface owner |
| `AGENT-CONTEXT` | Ch75 | Per-call working set owner |
| `AGENT-RAG` | Ch76 | External evidence acquisition owner |
| `AGENT-MEMORY` | Ch77 | Persisted/derived state owner |
| `PLATFORM-SECURITY` | Ch72 | Access/privacy boundary |

## Prerequisites

- 完成 Lab 13；建议复用 Lab 06 的 state authority 区分。
- 理解 embedding retrieval、ranking、Context window 与 provenance。

## System Under Test

一个只读问答/分析 Agent，包含 Prompt registry、Context assembler、retriever/ranker、memory store/consolidator 和
evidence renderer。Source document 拥有事实 authority；retrieval/memory 只拥有候选 evidence；Context 拥有本次工作集。

## Baseline

把 instructions、documents 和 conversation history 全部放入单次 Context。短任务、证据量小且必须完整审计时仍合理。

## Step-by-Step Experiments

1. 分离 system instruction、user input、retrieved evidence、tool result 与 memory，记录每段 identity/scope。
2. 建 full-context baseline，改变 length/order，观察 truncation 与 instruction interference。
3. 实现 lexical/dense/hybrid retrieval、ranking、packing，并保留 source chunk/provenance/freshness。
4. 增加 episode memory write/read，再从成功/失败 episode 抽取 derived memory，保留来源和置信度。
5. 实现 supersession、delete、tenant/ACL filter 和 bounded associative expansion。
6. 注入 stale/poisoned/conflicting evidence、retrieval miss 和 memory overgeneralization，比较 abstain/citation behavior。

## Expected Artifacts

- Typed Context segments、retrieval index、memory schema、provenance graph 与 answer/evidence trace。
- Lab 15 可消费的 scoped working state 和 advisory memory，不包含 action authority。

## Invariants

- Context 是 per-call working set，不自动成为 durable Memory。
- Retrieved/derived state 保留 source、scope、valid time 和 supersession；不能获得超过来源的 authority。
- Delete/ACL 在 retrieval、expansion、packing 和 rendering 全链路生效。

## Failure Injection

- 删除关键 chunk、插入高相似错误文档、让两个来源冲突、更新文档但保留旧 index。
- 写入错误 episode、跨租户查询、删除源证据后尝试通过 derived memory 恢复。

## Measurements

- Retrieval recall/precision、answer groundedness、citation correctness、abstain 与 conflict detection。
- Context tokens、latency、memory hit、staleness、delete propagation 与 cross-tenant leakage。

## Acceptance Criteria

- [ ] Full Context、RAG、episodic/derived Memory 在同一 task/evidence contract 下比较。
- [ ] 每个 answer claim 可回到允许访问的 source evidence 或明确标记为推断。
- [ ] Stale/poisoned/conflicting evidence 不会被静默升级为事实。
- [ ] Delete、supersession 和 tenant scope 可端到端验证。

## Trade-offs and Alternatives

Full Context 简单但成本随历史增长；RAG 减少 working set 却增加 miss/ranking/freshness；Memory 提高跨 run 复用，
却增加 consolidation bias、delete propagation 和权限面。Derived memory 是 advisory state，不是新的事实来源。

## Reflection Questions

1. Context、RAG index 与 Memory 分别拥有哪种状态？
2. 为什么相似度不能决定事实 authority？
3. Derived memory 怎样被 review、supersede 和 rollback？

## Next Lab Handoff

向 Lab 15 交付带 identity、scope、provenance、freshness 的 Context 与 advisory Memory；行动系统可以读取这些状态，
但必须另行获得 tool authorization、workflow commit 和 completion evidence。

