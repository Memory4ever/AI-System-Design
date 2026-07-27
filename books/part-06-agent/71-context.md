# 第71章 Context

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 上下文是 LLM 的运行时状态。

## 本章要回答的问题

Context 为什么不是“把所有已知信息塞进窗口”？模型支持更长 token length 后，检索、摘要和状态管理是否会消失？Agent context 与持久 Memory 有什么区别？

本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**

## Context 是一次调用的可见状态

一次调用可抽象为：

```text
C_t = assemble(
  instructions,
  user input,
  conversation,
  retrieved evidence,
  memory reads,
  tool schemas/results,
  workflow state
)

y_t ~ p(. | C_t, theta)
```

`C_t` 会随每一步 tool observation 和 workflow transition 改变。模型参数 `theta` 相对稳定，Context 则是 Agent runtime 的高频状态。

Memory 可以跨调用持久化；Context 是从各存储和当前事件中选择出的 working set。二者关系类似 storage 与 working set，而不是同义词。

## Token Budget 是容量约束

设：

```text
T_max     model/runtime accepted context length
T_sys     instructions and policies
T_hist    conversation history
T_ret     retrieved or memory content
T_tool    tool schemas and observations
T_out     reserved output budget
```

必须满足：

```text
T_sys + T_hist + T_ret + T_tool + T_out <= T_max
```

但满足不等式只证明请求可被接受，不证明模型能找到、理解或正确使用其中的信息。第 22 章已区分 accepted length、position generalization、effective utilization 和 system capacity；本章负责 runtime selection。

## 为什么“全塞进去”会失败

更多 token 会增加：

- Prefill compute、TTFT 与成本；
- KV Cache 占用和并发压力；
- irrelevant evidence 与指令冲突；
- lost-in-the-middle 风险；
- sensitive data 暴露面；
- cache identity 和 invalidation 复杂度。

`Lost in the Middle` 的实验说明相关信息位置会显著影响表现。这个结论不能外推为固定排序口诀，却足以否定“只要窗口够长就无需 context engineering”。

## Context Assembly Pipeline

可靠 assembly 需要显式阶段：

```text
collect candidates
→ authorize and filter
→ rank by relevance/recency/authority
→ deduplicate and resolve conflicts
→ compress or summarize
→ place with source/trust metadata
→ reserve output and tool budget
```

排序不能只看 embedding similarity。Authoritative policy、current workflow state 与 user intent 可能优先于语义相近文本。冲突内容应保留来源和时间，不应由摘要器静默合并成一个“事实”。

## Context Compression 的损失

Summary、extractive compression 和 structured state 都可减少 token。压缩函数可写为：

```text
C'_t = compress(C_t, task, budget)
```

目标不是最短，而是保留对未来决策充分的信息。摘要可能丢失 exception、否定、数字和 provenance；递归摘要还会累积漂移。

关键状态应使用 typed workflow fields 或原始 artifact reference，不只存在自然语言摘要。必要时保留摘要到原文的 links，允许按需回读。

## Context Identity 与 Cache

Context 参与模型行为身份。至少需要记录：

- segment digest/source/version；
- assembly policy version；
- model/tokenizer/chat template；
- tool schema versions；
- retrieval/memory query；
- authorization snapshot；
- compression method。

Prefix cache 可以复用相同 token prefix，但 user/tenant-specific 内容、policy version 和 adapter 都必须进入 cache identity。错误复用不仅改变回答，还可能泄漏跨租户状态。

## Context 中的信任冲突

System message、retrieved web content 与 tool result 最终都变成 token，但控制面必须保留来源差异：

| 来源 | 可作为信息 | 可直接授权动作 |
| --- | --- | --- |
| Platform policy | 是 | 仍由执行器强制 |
| User request | 是 | 受用户权限限制 |
| Retrieved content | 是 | 否 |
| Tool result | 是 | 否 |
| Model-generated memory | 需验证 | 否 |

模型可以建议如何解释内容，不能改变其 authorization class。

## Observability 与 Evaluation

Context evaluation 应分解：

- selection recall：所需信息是否入选；
- precision：无关/冲突内容比例；
- placement/use：模型是否使用正确 evidence；
- faithfulness：结论是否由 evidence 支持；
- cost/latency：assembly、Prefill 和 storage read；
- privacy：是否越权读取或记录敏感内容。

只评最终答案会无法区分 retrieval miss、bad ranking、compression loss 与 model misuse。

## 本章在知识树中的位置

Prompt 定义软接口，Context 定义本次调用的完整 working state。下一章展开 Context 的主要动态来源之一：RAG 如何从外部 corpus 检索 evidence，并为生成保留 provenance。

## 自检问题

1. Context 与 Memory 的核心区别是什么？
2. `T_total <= T_max` 为什么不代表信息被有效使用？
3. 长窗口为什么没有消除检索和压缩？
4. Context assembly 为什么要先 authorization 再 ranking？
5. Summary 为什么需要链接原始 evidence？
6. 哪些字段必须进入 context/cache identity？

## 小结

Context 是受约束的运行时 working set，不是无限知识仓库。好的 assembly 在相关性、权威性、位置、成本和隐私之间做可追溯取舍。下一章进入 RAG 的检索链。

## Review notes

本章复用第 22、39、41、50 章的长上下文与容量约束，不重复 position/attention/KV 机制；第 72 章拥有 external retrieval，第 73 章拥有 persisted memory lifecycle。

Primary-source 入口：

- Lost in the Middle: https://arxiv.org/abs/2307.03172
- GPT-3 / in-context learning: https://arxiv.org/abs/2005.14165
- Long Context chapter dependency: Chapter 22 in this repository
