# Part VII Agent：从生成答案到受控行动

## Part Question

模型怎样在有限 Context、外部知识、持久 Memory、工具权限和环境反馈中完成长程任务？哪些状态可以由模型提出，哪些状态必须由可信 Runtime 拥有？

## 进入条件

Part VI 已建立 identity、policy、evidence、cost、security 与 recovery substrate。本 Part 在其上增加 information state、action proposal、workflow state、delegation 和 side effects，不把更长 Prompt 当作完整 Agent 系统。

## 演进主线

```text
Prompt condition
→ Context working set
→ External retrieval
→ Persisted and derived Memory
→ Typed action proposal
→ Planning and bounded correction
→ Durable Workflow
→ Bounded Multi-Agent delegation
→ Standardized connectivity
→ Governed Agent Platform
```

这条路线不是“自治程度越来越高”。每一步都把新的状态和风险显式交给 Runtime：Memory 需要 provenance，Tool 需要 authorization，Workflow 需要 durable commit，Multi-Agent 需要 bounded delegation，Platform 需要 evidence 和 rollback。

## 章节分工

- [Ch74～77](74-prompt.md) 建立 Prompt、Context、RAG 与 Memory 的 information-state 层。
- [Ch78～80](78-tool-calling.md) 从 Tool proposal 进入 Planning 与 evidence-backed Reflection。
- [Ch81](81-workflow.md) 拥有持久状态机、retry、compensation 和 human checkpoint。
- [Ch82](82-multi-agent.md) 拥有角色分解、communication tax、delegation 与 aggregation。
- [Ch83](83-mcp.md) 拥有连接协议，不拥有业务授权或 Workflow。
- [Ch84](84-agent-platform.md) 统一 Agent definition、run、state、resource、policy 与 evidence。

## 退出契约

读完后，应能把“模型建议什么”与“系统允许、提交并证明什么”分开。全书在 Agent Platform 收束：长期稳定的设计对象不是某个 Agent framework，而是 identity、state、resource、evidence、policy 与 feedback 的闭环。
