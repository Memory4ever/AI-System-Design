# 第78章 Tool Calling

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-TOOL-CALLING`
**Legacy Chapter:** Ch74
**Status:** Draft

**Roadmap Intent:** 模型如何调用外部系统，把语言能力变成行动能力。

## 本章要回答的问题

Tool Calling 为什么不是“让模型输出一段 JSON”这么简单？模型选择工具与平台授权执行分别属于谁？当调用产生付款、发信或部署等副作用时，如何处理重试、重复和恢复？

本章的核心判断是：**模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。**

## 从生成文本到环境转移

没有工具时：

```text
Context → Model → Text
```

有工具时：

```text
Context
→ Model proposes tool call
→ Policy/Executor validates
→ Environment changes or returns data
→ Observation enters Context
→ Model continues
```

Toolformer 研究模型如何学习何时调用 API、传什么参数并利用结果；ReAct 展示 reasoning 与 environment actions 交替。它们证明一种能力路径，不证明任意调用都可靠或安全。

## Tool Contract

一个可执行工具至少需要：

```text
tool identity + version
description
typed input schema
typed output/error schema
side-effect class
required authorization scopes
timeout / cancellation
idempotency and retry semantics
owner and audit policy
```

Description 帮助模型选择工具，Schema 帮助构造参数；二者都不能替代服务端业务校验。Tool name 或描述可能来自第三方 server，应视为不可信 metadata，不能据此自动提升权限。

## 模型输出只是 Proposal

典型 data path：

```text
raw model output
→ parse
→ schema validation
→ canonicalization
→ authorization
→ policy/business validation
→ optional approval
→ execution
→ result filtering
→ observation
```

Schema 可以拒绝缺字段、错误类型或非法 enum；semantic validation 还要检查金额、目标资源、环境、时间窗口和当前状态。Authorization 必须使用真实 principal，不接受模型生成的 `tenant_id` 或 scope。

## Tool Discovery 与选择

### Interface Granularity：不是 Tool 越多越有能力

大量 narrow tools 提供清晰 schema、最小权限与可治理的 operation，却会产生 catalog coverage debt：复杂任务
需要模型先猜对 tool，再受限于 tool 没暴露的 filter、payload 或组合操作。另一端，terminal + filesystem +
generic API 把 discovery、批处理和组合能力交给 Agent，减少 catalog 维护，却扩大 credential、命令构造、
endpoint discovery、output parsing 和 side-effect surface。

```text
typed narrow tool
→ generic typed API client
→ terminal / script composition
→ browser fallback for UI-only state
```

这是并存的 interface branches，不是单向升级。平台应根据 task risk、operation coverage、request volume 与
auditability 选择最窄且足够表达的 surface，并保持 canonical action、authorization 和 effect identity 不变。
Terminal Agents 的受限实验说明部分 enterprise gap 来自 interface granularity，不证明 shell 比 MCP、domain
API 或 browser 普遍更好；benchmark sandbox、模型、tool catalog 与成本条件变化都会改变结论。

将几百个完整 schemas 全部放入 Context 会增加 token cost、选择混淆和 attack surface。可以分层：

```text
task intent
→ authorized tool catalog retrieval
→ shortlist
→ schema exposure
→ model choice
```

Catalog retrieval 也必须 tenant-aware。工具版本变化可能让旧 Prompt 生成过期参数，因此 tool schema version 是 Context 和 evaluation identity 的一部分。

多模态任务还要决定 perception 是 Context 的固定预处理，还是一个按需 Tool。把全部媒体先编码，控制流最简单，
但长视频/高分辨率会耗尽 token 并因 downsampling 丢细节；把 crop、ASR、OCR、frame seek 暴露成工具，可以由
Agent 针对 uncertainty 主动取证：

```text
coarse native perception
→ identify unresolved region / time span / modality
→ typed perception-tool request with budget
→ source-linked observation
→ continue, verify or abstain
```

这不会把 tool observation 变成真值，也不会证明“主动看更多”总是更好。调用位置、crop/segment identity、媒体
revision、cost 与返回 provenance 都要进入 run；错误 perception 可能诱导后续工具形成自确认。固定预处理在短
媒体、低延迟或 deterministic coverage 优先时仍合理。OmniGAIA 只为 native perception 与按需 tool 的组合提供
受限实验，不把其模型排名或 LLM judge 结果写成通用架构优势。

## Agent-friendly Tool 不等于把 CLI 包一层

领域任务常先让模型生成自由文本命令，再由 shell、网页或人工解释结果。这对 demo 足够，
却让参数、版本、来源和失败语义难以复现。更可靠的演进是把稳定能力暴露为确定工具：

```text
natural-language guess
→ typed domain operation
→ deterministic retrieval / computation
→ structured result + provenance
→ model interprets, workflow validates
```

在生物信息任务中，官方 agent study 把确定的基因组检索能力作为工具提供，比让模型凭参数
知识作答更可靠。长期意义不是某个工具名，而是 **模型负责选择和解释，authoritative system
负责检索、计算与版本化**。代价是维护 schema、数据库版本、rate limit 与错误分类；工具
本身的数据过期、覆盖不足或错误返回仍会成为 Agent 的系统性盲点。

这与 RAG 是 `Principle Reuse`：两者都把易变化事实移出模型参数。区别是 RAG 通常返回
Context，而 Tool Calling 还拥有执行语义、权限、预算和可能的副作用。

## 从语义正确的 Program 到可证明的 Resource Lowering

Skill 或 Prompt 可以要求“流式读取”“分块处理”“不要一次加载全部文件”，但模型最终生成的 program 仍可能 eager-
load 整个输入。它在小样本上语义正确，进入真实 XLSX、CSV、array 或 scientific artifact 后却超过单次 tool call 的
memory cap。只在 cgroup OOM 时拒绝能保护节点，却无法把原本可分块的 computation 转成可运行实现；让模型继续
重试，也不能证明新程序与 source computation 等价。

这形成一条从 advisory optimization 到 checked lowering 的演进：

```text
Skill describes intended computation and resource obligation
→ model proposes a concrete source program
→ match one audited source relation
→ independent checker rebuilds bounded target from immutable input facts
→ calculate platform-calibrated live-set bound
→ acquire atomic capacity lease
→ execute in bounded runtime
→ verify postcondition and resource events
→ publish result or abstain without partial publication
```

关键 authority 分离是：模型拥有 proposal，relation registry 拥有已审计的语义映射，checker 拥有 target 重建和 bound
验证，scheduler/capacity manager 拥有 lease，tool runtime 拥有执行，postcondition gate 才拥有 publication。不能接受
模型自报的 `memory_required`，也不能让被检查的 program 自己提供等价性证明。

这种 architecture 的 generality 不是“自动验证任意代码”。每个 computation family 仍需要一个 audited relation：

```text
source recognizer
+ semantic/input-fact extractor
+ bounded IR / target constructor
+ arena/live-set bound
+ output postcondition
```

Common runtime 只能复用 dispatch、capacity accounting、bounded execution 与 staged publication。SkillEffect 的作者实验
在六个 deterministic、local、read-only operator families 和固定 cgroup cap 下，为这一 trust boundary 提供受限证据；
Prompt/retry 不能稳定构造 bounded program，而 registered lowering 在其 closed grammar 中通过 verifier。论文的设备、
输入规模和 peak-memory 倍率不作为通用 Tool 性能结论。

代价是 relation-specific audit、checker TCB、platform manifest calibration、保守 reserve、版本/extension 维护和
unsupported-program abstention。Runtime/allocator/page size 改变后必须重校准；postcondition 只覆盖声明的结果属性。
当前 local staged output 也不能直接外推到 email、payment 或 mutable remote service：这些还需要 authorization、
idempotency、transaction / compensation 与第 81 章 Workflow commit。

因此这不是替代 generic Tool Calling 的默认路径。输入小、资源充足或 operation 不能建立 closed relation 时，普通 typed
execution + cap/reject 仍更简单；只有 resource failure 频繁、关系可审计、结果可验证时，checked lowering 才值得承担
额外控制面。

## Side-effect Class 决定控制

可将工具粗分为：

| 类型 | 示例 | 默认控制 |
| --- | --- | --- |
| Read-only | search、get status | scope、rate、redaction |
| Reversible | create draft、temporary resource | audit、rollback |
| Irreversible/high impact | payment、delete、publish | approval、strong idempotency、narrow scope |

“只读”也可能泄露敏感数据或造成 expensive query，不能视为无风险。Tool risk 是数据、操作和环境的组合。

## Retry、Idempotency 与 Exactly-once 幻觉

Network timeout 后，执行器可能不知道远端操作是否成功。直接重试会重复副作用。

稳定设计使用：

- idempotency key；
- operation status query；
- request/response durable record；
- conditional update/version precondition；
- compensation for reversible operations；
- manual reconciliation for ambiguous outcomes。

Exactly-once 往往是端到端协议属性，不是调用 SDK 的一个开关。模型不应自己猜测“上次可能失败，再试一次”。

## Observation 也不可信

Tool result 可能包含：

- stale/partial data；
- malicious instructions；
- sensitive fields；
- oversized content；
- error message with internal details。

执行器应做 output schema validation、redaction、size limit 和 provenance annotation，再将结果送入 Context。网页或 email 中的文字不能因为来自 tool 就升级为 platform instruction。

## Loop Boundaries

Agent loop 需要硬限制：

```text
max_steps
max_wall_time
token/tool/cost budgets
per-tool concurrency and rate
repeated-call detection
progress / no-op detection
user cancellation
```

停止条件应由 runtime 强制，Prompt 中写“最多五步”只是一种软提示。

## Evaluation 与 Observability

Tool-use evaluation 需要分解：

- tool selection accuracy；
- argument/schema correctness；
- authorization deny correctness；
- execution success；
- task success；
- side-effect safety；
- retries/duplicates；
- latency/cost；
- recovery after partial failure。

Trace 应把 model proposal、policy decision、approval、tool call 和 result 分成 spans/events，并避免默认记录 secrets。

这些 component metrics 不能脱离最终 task outcome 单独解释。第 66 章提供统一的 subject、environment、scorer、slice 与 decision contract，本章只定义 Tool Calling 特有的失败模式和证据。

## 本章在知识树中的位置

前四章构造 information state，本章首次改变 environment。下一章讨论 Planning 如何把目标拆成有依赖和前置条件的未来行动，同时保持计划只是可修正假设。

## 自检问题

1. 模型选择工具与平台授权执行为什么必须分离？
2. Input schema 不能替代哪些校验？
3. Tool discovery 为什么也需要 authorization？
4. Timeout 后为什么不能盲目 retry？
5. Tool result 为什么仍是不可信 Context？
6. Agent loop 哪些边界必须由 runtime 强制？
7. 为什么模型生成的 bounded program 不能自己证明语义等价和 memory bound？
8. Checked lowering 的 relation、capacity lease 与 publication gate 分别由谁拥有？

## 小结

Tool Calling 把语言能力连接到环境，也把概率错误变成现实副作用。可靠系统把模型输出当作 proposal，由可信执行器实施 typed、authorized、observable action。下一章进入多步 Planning。

## Review notes

- Terminal Agents（interface granularity；Status: Experimental）: https://arxiv.org/abs/2604.00073

本章承接第 72、73 章的 least privilege、audit 和 recovery，不把 JSON generation 写成完整 tool system。MCP 的标准 discovery/transport 放到第 83 章。

Primary-source 入口：

- Toolformer: https://arxiv.org/abs/2302.04761
- ReAct: https://arxiv.org/abs/2210.03629
- Gorilla / API use: https://arxiv.org/abs/2305.15334
- Anthropic, "How agents can use tools to accelerate biological discovery":
  https://www.anthropic.com/research/agents-in-biology
- OmniGAIA / OmniAtlas（native perception + on-demand perception tools；Status: Experimental）:
  https://arxiv.org/abs/2602.22897
- SkillEffect（checked lowering + capacity lease；Status: Experimental）:
  https://arxiv.org/abs/2608.17007
