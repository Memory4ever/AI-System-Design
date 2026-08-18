# Lab 15 — Agent Action & Workflow

## Lab Question

模型提出的 Tool、Plan 与 Reflection 怎样变成可授权、可恢复、可审计的 durable Workflow，并安全扩展到 Multi-Agent？

## Why This Lab Exists

直接执行模型输出在无副作用 toy task 中最简单；真实工具会改变外部状态，失败可能发生在 request、effect 或 response
之间。Planning/Reflection 增加修正能力，Workflow 把状态持久化，Multi-Agent 扩展并行提案，但 authority、idempotency、
compensation 与 communication tax 必须由 Runtime 显式拥有。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `AGENT-TOOL-CALLING` / `AGENT-PLANNING` / `AGENT-REFLECTION` | Ch78～80 | Proposal、plan 与 diagnosis |
| `AGENT-WORKFLOW` | Ch81 | Durable transition/commit owner |
| `AGENT-MULTI-AGENT` | Ch82 | Bounded delegation owner |
| `AGENT-MCP` | Ch83 | Connectivity contract |
| `AGENT-PLATFORM` | Ch84 | Identity/policy/resource/evidence coordination |
| `PLATFORM-SECURITY` / `PLATFORM-EVALUATION-SYSTEM` | Ch72、66 | Authorization 与 completion evidence |

## Prerequisites

- 完成 Lab 13 和 Lab 14。
- 理解 idempotency key、state machine、retry、compensation、least privilege 与 partial failure。

## System Under Test

一个有只读和可逆写操作的 toy service，加 Agent runtime、tool registry、policy engine、durable workflow log、planner、
reflection/verifier 和 optional worker Agents。模型拥有 proposal；policy 拥有 authorization；workflow 拥有 commit；
external system 拥有 effect truth；verifier 拥有 completion judgment。

## Baseline

模型生成文本命令，由调用者直接执行。无副作用、单步、本地工具时路径短，但没有 schema、authorization 或恢复语义。

## Step-by-Step Experiments

1. 将文本命令改为 typed tool proposal，验证 schema、capability、scope 与 side-effect class。
2. 在执行前加入 policy/approval，执行后记录 effect identity、result 和 evidence。
3. 把多步 plan 表示为可修订 state-transition hypothesis，completion 由环境证据决定。
4. 增加 durable workflow、idempotent retry、timeout、compensation、human checkpoint 与 replay。
5. 加入 reflection：只提出 bounded diagnosis/correction，不自行改写 committed history 或权限。
6. 增加一个委派 worker，对照 single-Agent baseline，测量 decomposition、communication、aggregation 和 error amplification。
7. 用 MCP-like connection 隔离 discovery/connectivity；验证协议连接不自动授予业务 authorization。

## Expected Artifacts

- Tool schemas、policy decisions、workflow event log、effect receipts、replay/compensation tests 与 multi-agent trace。
- Lab 16 可复用的 Agent definition/run/state/policy/evidence contract。

## Invariants

- Proposal、authorization、execution effect、commit 与 completion evidence 分属明确 owner。
- Retry 使用相同 operation identity，不重复 side effect；committed history 不被 Reflection 静默改写。
- Delegated Agent 权限不超过父任务 scope；协议连接不等于授权。

## Failure Injection

- Tool timeout before/after effect、lost response、duplicate retry、schema drift、approval expiry。
- Worker 返回冲突结果、消息丢失、父 Agent 取消、compensation 失败、MCP server capability 变化。

## Measurements

- Task completion、false success、tool/effect calls、retry/duplicate prevention、recovery/compensation time。
- Plan revisions、human interventions、delegation overhead、communication tokens、error amplification 与 policy violations。

## Acceptance Criteria

- [ ] Tool proposal 到 external effect 的每个 authority transition 可追溯。
- [ ] Lost response/duplicate retry 不会造成重复 side effect 或虚假完成。
- [ ] Reflection 只能触发有边界的修正，不能绕过 policy 或 workflow commit。
- [ ] Multi-Agent 只有在可分解任务上证明净收益，并报告 communication/error cost。

## Trade-offs and Alternatives

Typed tools 降低 parsing ambiguity，却增加 schema/version；durable workflow 增加恢复能力，也增加 latency/storage；
Multi-Agent 扩展并行搜索，但单 Agent headroom、共享状态和 aggregation 往往更重要。人工审批在高影响操作中仍成立。

## Reflection Questions

1. Tool 返回成功与任务完成为什么是不同证据？
2. Plan、Workflow state 与 external effect 各自由谁拥有？
3. 增加 Agent 数量何时只会放大错误与通信税？

## Next Lab Handoff

向 Lab 16 交付 versioned Agent definition、scoped Context/Memory、typed tools、policy、workflow log、effect receipts、
completion evidence 与 recovery contract；Capstone 将它们接入完整模型生命周期。

