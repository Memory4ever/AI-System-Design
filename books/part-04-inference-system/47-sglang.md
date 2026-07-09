# 第47章 SGLang

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 面向结构化生成、复杂推理和高效 Serving 的运行时。

## 本章要回答的问题

如果 vLLM 已经能高效 serving，为什么还需要 SGLang？SGLang 解决的是普通单轮 completion 的问题，还是复杂 LLM 程序的执行问题？RadixAttention 为什么适合 agent / workflow 场景？

SGLang 的核心切入点是：真实 LLM 应用不只是单次 prompt → answer，而是多轮生成、分支、并行、工具调用、JSON 约束、RAG、agent workflow 的组合。

这些程序经常共享长 prefix。如果每个分支、每一轮都重新 Prefill，系统会浪费大量计算。

这是 SGLang 论文的历史切入点，不是当前项目能力的完整边界。今天的 SGLang 同样是通用高性能 Serving framework，覆盖 continuous batching、paged attention、speculative decoding、PD disaggregation 和多种并行能力。本章保留 RadixAttention 与 structured programs 作为核心理解线索，但不把 SGLang 限定成“只服务 Agent 的 runtime”。

## 从共享 prefix 开始

假设一个 agent workflow 有共同 system prompt、工具说明、用户上下文，然后分出多个候选计划。每个候选计划前面的大部分 prompt 都相同，只有后续分支不同。

朴素做法是每个请求都完整 Prefill：

```text
shared prefix + branch A
shared prefix + branch B
shared prefix + branch C
```

这会重复计算 shared prefix 的 KV Cache。

更自然的做法是把 shared prefix 的 KV Cache 复用起来，只为分支部分补充新的 K/V。这就是 RadixAttention 想解决的问题。

## RadixAttention 的直觉

RadixAttention 可以理解为用 prefix tree 组织请求之间的共享前缀。不同请求的 token 序列如果前面相同，就可以复用已有 KV Cache；只有分叉之后的部分需要新增计算和缓存。

这里的相同必须落实到经过 tokenizer 和模型配置处理后的 token prefix，而不是字符串“看起来相同”。Cache key、adapter、模型版本、position 与租户安全域都可能影响是否允许复用。错误复用不是性能下降，而是正确性或数据隔离问题。

这和 PagedAttention 的关注点不同：

```text
PagedAttention: 解决 KV Cache 怎么存、怎么分页、怎么减少碎片
RadixAttention: 解决多个请求之间哪些 KV Cache 可以复用
```

一个偏 memory allocation，一个偏 prefix-aware compute reuse。实际系统里二者都可能重要。

## 为什么适合 Agent

Agent / Workflow 场景天然有大量结构化上下文：

- system prompt 固定。
- tool schema 固定。
- few-shot examples 固定。
- RAG 检索结果可能部分共享。
- 多轮对话会保留历史上下文。
- planning / reflection 可能产生多个分支。

这些都让 prefix reuse 有价值。

SGLang 不只是 runtime，还提供面向 structured language model programs 的表达方式。前端让开发者描述生成、并行、控制流、结构化输出；后端 runtime 则尝试把这些程序高效执行。

## Trade-off

Prefix reuse 的收益取决于 workload。如果请求之间几乎没有共享前缀，RadixAttention 的收益就有限。如果共享前缀很长，且请求模式稳定，收益会明显。

代价是 runtime 需要维护 prefix tree、cache 生命周期和 eviction 策略。多租户场景还要处理不同用户上下文之间的隔离，不能为了复用而跨越安全边界。

结构化输出也有代价。JSON decoding、grammar constraint、FSM 等机制提高可控性，但会改变 token selection 和调度形态，需要 runtime 支持。

## 和 vLLM 的关系

vLLM 和 SGLang 都可以承担通用 LLM serving。更稳定的区分是它们的历史抽象重点：vLLM 从 KV block management 与 scheduling 切入，SGLang 论文从 language model programs、RadixAttention 和 structured decoding 切入。当前产品能力已经大量重叠，选型应基于目标版本的模型支持、硬件、稳定性、运维接口和实测 workload。

在 AI System 知识树里，SGLang 是 Part IV 和 Part VI 的交叉点：它既是 inference runtime，又直接服务 Agent / Workflow。

## 本章在知识树中的位置

```text
KV Cache
→ Prefix reuse
→ RadixAttention
→ SGLang
→ Workflow / Agent Platform
```

SGLang 说明推理系统的边界正在从“服务单次模型调用”扩展到“执行复杂语言程序”。

## 自检问题

1. 为什么复杂 LLM 应用会产生大量 prefix reuse 机会？
2. RadixAttention 和 PagedAttention 的问题边界有什么不同？
3. SGLang 为什么和 Agent / Workflow 更接近？
4. Prefix cache 复用会带来哪些隔离和生命周期问题？
5. 为什么 structured output decoding 也属于 runtime 问题？

## Review notes

本轮 Review 区分了 SGLang 论文的历史切入点与当前 Serving framework 的能力边界；补充 prefix reuse 的正确性和租户隔离条件；并取消“vLLM 通用、SGLang 只面向 Agent”的静态二分。

Primary-source 校验入口：

- SGLang paper: https://arxiv.org/abs/2312.07104
- SGLang official repository: https://github.com/sgl-project/sglang
