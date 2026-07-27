# 第80章 Agent Platform

**Knowledge Tree:** Part VI Agent：从回答问题到执行任务
**Status:** Draft

**Roadmap Intent:** 从单个 Agent 到可治理、可观测、可复用的 Agent 平台。

## 本章要回答的问题

一个 Agent demo 变成平台后，需要管理哪些新对象和控制闭环？Agent Platform 与 Part V AI Platform 是两套系统吗？如何评估一个长期执行、调用工具并产生副作用的 Agent？

本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part V 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**

## Agent 改变了平台的控制对象

模型服务的主要对象是 request 与 token-generation state。Agent 增加：

```text
goal
plan and workflow state
context assembly
memory read/write
tool/action intents
external side effects
delegation
human approvals
long-running events
```

请求完成不再等于任务完成。一个 Agent run 可能持续数分钟、数天，被暂停、等待用户、跨多个模型与工具后再恢复。

## Agent Definition 与 Run Identity

可部署 Agent definition 至少绑定：

```text
agent_id + immutable version
model/runtime policy
prompt/context assembly versions
memory policy/schema
tool/MCP allowlist and versions
workflow definition
evaluation suite
authorization/delegation policy
budgets and SLO
owner / rollout status
```

`AgentRun` 是该 definition 在某个 goal/principal 下的一次执行：

```text
run_id
agent_version
principal / tenant
input and consent
event/state history
artifacts and side effects
budget consumption
terminal evidence
```

Mutable alias 可用于 rollout，但 run 必须解析并记录实际版本。

## 三个平面

```text
Control Plane
  definitions, registry, policy, workflow, scheduling, rollout

Execution/Data Plane
  model calls, retrieval, memory access, tools, MCP, environment

Evidence Plane
  trajectory, evaluations, metrics, logs, traces, audit, cost
```

Control plane 不应阻塞每个 token，却必须控制每个高风险 transition。Execution plane 不能自行修改 policy。Evidence plane 提供 replay、incident 和 improvement 所需 observed state。

## Agent Runtime State Machine

一个通用 run 可表达为：

```text
Created
→ ContextReady
→ Planning
→ Acting
→ Observing
→ Reflecting / Replanning
→ Waiting
→ Succeeded | Failed | Cancelled | Escalated
```

具体 workflow 可增加 domain states。关键是每次 transition 都可恢复、可审计，并绑定 actor、policy、budget 和 side-effect evidence。

## Scheduling 不只是 GPU

Agent Platform 同时面对多个时间尺度：

| 调度层 | 对象 |
| --- | --- |
| Inference runtime | token、batch、KV |
| GPU/cluster | Pod、gang、device |
| Agent runtime | ready steps、tools、approvals、deadlines |
| Workflow/platform | runs、tenants、budgets、priorities |

Agent waiting 不应占用模型/GPU。Runtime 可在 event 到来时重新组装 Context。Tool/API concurrency、rate limits 和 external quotas 也成为 capacity。

## Policy 与 Agent Identity

Agent 代表用户或服务行动，需要明确：

- 谁创建和启动它；
- 它以谁的 authority 行动；
- 可访问哪些 data/tools；
- 能否 delegation；
- 哪些 action 需要 approval；
- credentials 如何短期发放与撤销；
- action 如何 non-repudiation/audit。

Agent 不应长期持有用户全权 token。NIST 2026 的 agent identity/authorization 工作也将 identification、authorization、auditing 和 delegation 视为核心采用障碍；当前仍是演进中的标准领域，不能声称已有统一最终方案。

## Evaluation 从答案扩展到 Trajectory

最终 success 仍是核心，但还需过程指标：

```text
task success / partial progress
correct tool and argument use
policy violations / denied actions
side-effect correctness
steps, latency, tokens and cost
recovery / escalation quality
memory writes and later impact
robustness to adversarial observations
```

Evaluation environment 要隔离真实副作用，并记录 model/tool/index versions。Benchmark score 不自动代表 production workload；AgentBench、SWE-bench 等提供任务入口，也暴露 long-horizon evaluation、environment leakage 和 verifier quality 的困难。

## Observability 与 Replay

一个 run trace 应连接：

```text
goal
→ context/memory/retrieval
→ model decision
→ policy/approval
→ tool/MCP action
→ observation
→ workflow transition
→ outcome
```

Replay 不意味着重新执行副作用。平台应提供 evidence replay/simulation，并对外部 action 使用 recorded result 或 sandbox。Prompt/content telemetry 默认最小化，敏感 capture 需 opt-in 与 retention。

## Release、Canary 与 Rollback

Agent definition 更新可能改变 tool path 和长期 state，rollout 比模型 endpoint 更复杂：

- shadow 在 sandbox 执行或只比较 proposals；
- canary 按 tenant/task class 放量；
- old/new versions 可能读取不同 memory schema；
- in-flight runs 是否 pin old version；
- rollback 后如何处理已产生 side effects；
- policy/tool revocation 是否立即覆盖旧 run。

通常 run pin definition version，而 emergency security policy 可强制实时生效。两者优先级必须明确。

## Feedback 与演化

平台闭环：

```text
run trajectory + outcome
→ attribution and evaluation
→ prompt/context/memory/workflow/model change
→ offline replay and adversarial tests
→ governed rollout
→ new evidence
```

不应把成功/失败 trajectory 直接自动写入 global memory 或训练集。需要 provenance、privacy、quality review、dedup 和 dataset version。

## 何时不需要 Agent

若任务有稳定输入输出、确定流程和可编程规则，普通 service/workflow 更便宜、更可预测。Agent 适合需求模糊、环境动态、需要语言解释或开放工具选择的节点。

平台成熟度的一部分，是能拒绝不必要的 autonomy，把模型限制在它真正增加价值的边界。

## 本章在知识树中的位置：全书知识树收束

```text
Part I   stable AI System problem map
Part II  token-to-output model mechanism
Part III data-to-capability production
Part IV  model-to-online capability delivery
Part V   shared platform and governance
Part VI  context-to-action runtime loop
```

AI System 的最终对象不是单个模型，而是可持续生产、交付、约束、观察并改进能力的系统。Framework、模型与协议会变化，长期问题仍是 identity、state、resource、evidence、policy 与 feedback 如何闭环。

## 自检问题

1. Agent Platform 相比模型 Serving 新增了哪些状态？
2. Agent definition 与 AgentRun 为什么要分开？
3. Agent scheduling 有哪些时间尺度？
4. 为什么 Agent 不应长期持有用户全权 token？
5. Agent evaluation 为什么必须观察 trajectory 和 side effects？
6. Replay 为什么不能重新执行真实副作用？
7. In-flight run 与 emergency policy 的版本优先级如何设计？
8. 哪类任务应优先使用确定 Workflow 而不是 Agent？
9. Part I～VI 的主线如何闭合？

## 小结

Agent Platform 不是另起一套基础设施，而是在 AI Platform 上增加有状态、可行动、可恢复的 runtime。它让 Prompt、Context、RAG、Memory、Tools、Planning、Reflection、Workflow、Multi-Agent 和 MCP 进入同一 identity、policy 和 evidence graph。

到此，六个 Part 形成完整 Draft：从第一性原理理解模型能力，到生产能力、在线交付、平台治理，再到受控行动。后续 refinement 应由 papers、真实系统证据和跨章 Review 驱动，而不是为了扩写而增加内容。

## Review notes

本章收束全书，不把 Agent Platform 等同某个 framework。Part V 的控制面与治理能力被复用，Part VI 只增加 action-loop 特有状态。时效性 agent identity、MCP 和 telemetry 结论均保留版本边界。

Primary-source 与官方入口：

- AgentBench: https://arxiv.org/abs/2308.03688
- SWE-bench: https://arxiv.org/abs/2310.06770
- NIST Agent Identity and Authorization: https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization
- OpenTelemetry GenAI observability: https://opentelemetry.io/blog/2026/genai-observability/
- MCP specification: https://modelcontextprotocol.io/specification/2025-11-25
