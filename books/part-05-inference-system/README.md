# Part V Inference System：从模型资产到在线能力

## Part Question

模型资产怎样变成持续生成 token 的在线系统？在 Prefill、Decode、KV、显存、通信与 SLO 共同约束下，Runtime 应怎样分配状态和执行机会？

## 进入条件

Part IV 已交付版本化模型资产。本 Part 从 request lifecycle 开始，区分模型语义、执行机制、Serving Engine、分布式拓扑与 fleet policy，避免把单个 kernel benchmark 外推为服务能力。

## 演进主线

```text
Model artifact
→ Request state machine
→ Prefill and Decode
→ KV lifecycle
→ Iteration batching and paged placement
→ Draft / verify / commit
→ Compiled execution and serving engine
→ Distributed state-aware runtime
→ Memory tiering and phase disaggregation
→ SLO scheduling
```

每一步都在移动瓶颈，同时增加新状态：Continuous Batching 增加 iteration fairness，PagedAttention 增加 block ownership，Speculation 增加 rollback，分布式 Runtime 增加 freshness、routing 和 failure recovery。

## 章节分工

- [Ch42～45](42-what-happens-during-inference.md) 定义 request、Prefill、Decode 与 KV lifecycle。
- [Ch46～48](46-continuous-batching.md) 拥有 iteration batching、paged placement 与 speculative commit。
- [Ch49～53](49-tensorrt-llm.md) 将机制放进执行计划、单机 Engine、结构化 Runtime、分布式 Runtime 与声明式拓扑。
- [Ch54～56](54-gpu-memory.md) 以 memory hierarchy、P/D 分离和多时间尺度 scheduling 收束。

## 退出契约

读完后，应能说明每项推理优化改变了哪类 work、state 与 SLO，而不是只比较吞吐数字。Part VI 随后把模型资产、服务、资源与 evidence 纳入组织级控制面。

