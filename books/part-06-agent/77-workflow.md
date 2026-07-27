# 第77章 Workflow

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 把模型能力嵌入稳定、可控的业务流程。

## 本章要回答的问题

为什么 Agent loop 进入生产后需要 Workflow，而不是一个 `while` 循环？哪些决策可以交给模型，哪些状态转移必须由 deterministic runtime 管理？进程崩溃后如何避免重复副作用？

本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**

## 一个循环为什么不够

```text
while not done:
    ask_model()
    call_tool()
```

这段逻辑隐藏了：

- `done` 由谁证明；
- 进程崩溃从哪里恢复；
- tool timeout 是否已经产生副作用；
- 用户取消如何传播；
- approval 在哪个版本的 action 上生效；
- plan/context/memory 如何版本化；
- step/budget 何时耗尽。

长期任务需要 event/state persistence，而不是依赖进程内变量。

## State Machine 是基本模型

```text
Created
→ ContextReady
→ Planned
→ AwaitingApproval
→ Executing
→ Verifying
→ Succeeded | Failed | Compensating | Cancelled
```

每个 transition 应由事件和 precondition 触发，并记录：

```text
workflow_id / version
current state
input/output artifact references
actor/principal
policy snapshot
attempt and idempotency key
timestamp
decision evidence
```

模型文本可以建议 `next_state`，但 workflow engine 验证转移是否合法。

## Deterministic Spine，Agentic Nodes

适合 deterministic 的部分：

- identity、authorization、budgets；
- required gates；
- retry/backoff/timeouts；
- state transitions；
- side-effect records；
- cancellation/compensation；
- terminal success criteria。

适合 model-driven 的部分：

- interpreting ambiguous intent；
- drafting content；
- proposing plans/tool arguments；
- ranking alternatives；
- diagnosing unstructured failure。

这种组合既保留模型灵活性，又让业务不变量可测试。

## Durable Execution 与 Replay

Workflow engine 常通过 event history 重建状态。Replay 要求 orchestration decision 尽量 deterministic；模型 call、当前时间、随机数和 tool result 应记录为 activities/events，而不是重放时重新调用。

否则恢复会产生不同 plan 或重复 action。模型输出本身是 artifact，必须绑定 model/prompt/context/tool versions。

## Retry、Idempotency 与 Compensation

Workflow 区分：

- transient infrastructure retry；
- model revision/reflection attempt；
- business rejection；
- ambiguous external outcome；
- permanent failure。

Retry policy 不能一刀切。可逆操作可以定义 compensation，但 compensation 也可能失败，不等于数据库 rollback。不可逆 action 需要更强 approval、idempotency 和 reconciliation。

Saga-like flow：

```text
reserve resource
→ create change
→ publish

failure:
  unpublish
  delete change
  release resource
```

每个补偿步骤仍需 authorization 和 audit。

## Human-in-the-Loop

Approval 是 workflow state，不是聊天中的一句“可以”。应绑定：

- exact action/tool arguments digest；
- artifact/plan version；
- approver identity and authority；
- expiration；
- policy/risk reason。

Action 在等待期间若发生变化，旧 approval 失效。高风险任务还可使用双人批准或职责分离。

## Long-running 与 External Events

Workflow 可能等待用户、webhook、job completion 或 resource availability。需要：

- durable timers；
- correlation keys；
- duplicate event handling；
- stale event rejection；
- cancellation propagation；
- lease/heartbeat for workers。

模型不需要持续占用 GPU 等待；runtime 在新 event 到来时重新组装 Context。

## Testing 与 Evaluation

Workflow 可以确定性测试：

- state transition legality；
- policy denies；
- retries/backoff；
- crash/replay；
- duplicate events；
- cancellation；
- compensation；
- model/tool timeout；
- budget exhaustion。

Agentic nodes 再用 scenario/evaluation sets 测 task success。把两类测试分开，能区分 workflow bug 与 model behavior regression。

## 本章在知识树中的位置

第 74～76 章定义 action、plan 和 feedback，本章将其变成 durable execution。下一章讨论 Multi-Agent：何时把一个 workflow node交给不同角色/模型能产生真实收益，何时只是增加消息与协调成本。

## 自检问题

1. 一个 `while` loop 缺少哪些生产语义？
2. Deterministic spine 应拥有哪些不变量？
3. Replay 时为什么不能重新调用模型或工具？
4. Compensation 为什么不等于 rollback？
5. Approval 为什么必须绑定 action digest？
6. Workflow tests 与 Agent evaluations 应怎样分开？

## 小结

Workflow 把概率模型嵌入可恢复、可审计的状态机，使灵活 decision 与确定业务约束共存。下一章研究多个 Agent 之间的职责和通信。

## Review notes

本章负责 durable orchestration，不把特定 workflow framework 写成标准答案。它承接 Part V 的 identity、trace、security、cost 和 recovery，并为 Multi-Agent 提供共享事实状态。

Primary-source 与设计入口：

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Saga pattern: https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
