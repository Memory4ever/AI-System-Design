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

### 编译器反馈可以前移，但仍是受限 Authority

先完整生成程序，再调用 compiler/test 并修复，是最通用的黑盒路径；当 grammar 可处理时，constrained decoding 也能提前排除语法错误。但后置诊断会浪费已经生成的 token，并把错误起点埋在长输出中；另一方面，任意 prefix 通常还不是可编译单元，不能直接交给编译器。

折中控制流是把中间输出视为 provisional proposal：由 sealor 把 partial output 补成临时可编译单元，compiler 只拥有 syntax/type diagnostics，harness 根据诊断与预算决定 bounded rollback 或 rewrite，模型再继续生成。这样可把权威反馈前移，却不把 compiler 提升为任务正确性裁判，也不要求白盒访问模型内部状态。

代价是频繁 compiler call、语言特定的 sealing 规则、rollback state 与重放成本；涉及 future definition 的长依赖还会让临时补全失真。后置 compile/repair 仍是跨语言、低频生成的合理基线，而 compile success 不能替代 functional、security 或 outcome verification。

## Tool Discovery 与选择

### Tool Exposure Reward 必须扣除随机候选集优势

检索器展示更多工具时，即使没有学到更好的路由，也会因候选集合扩大而提高命中机会。评价 tool discovery 应以随机基线或候选先验校正 information gain，再把校正后的增益归给 exposure policy；执行正确性仍由工具与 outcome gate 拥有。收益是避免“多暴露即高分”，代价是需要稳定的候选分布和更多对照采样；工具集合固定且很小时，普通 recall 仍可用。该机制只校正 exposure 价值，不证明被选工具安全或执行结果正确。

<!-- source-family:SF-2026-ARXIV-2605-24660 -->

### 同功能 Provider 的选择属于运行时路由，不属于模型授权

只有一个实现时，模型直接选择 Tool 是最短路径；当同一能力由多个 Provider 提供，静态绑定又会把瞬时拥塞、尾延迟、可靠性和输出质量差异冻结进 Prompt。更稳健的分支是在已经通过 authorization 与 schema validation 的等价 Provider 集合内，由运行时依据实时负载、延迟、近期成功率、质量证据和预算选择执行者：

```text
authorized capability request
→ equivalent-provider set
→ live telemetry and policy filter
→ bounded routing decision
→ execution and outcome feedback
```

Router 只拥有“由谁执行”的调度权，不能扩大 Tool 权限，也不能把历史成功率当作当前结果为真的证明。它用额外 telemetry、探索流量和策略漂移风险换取更低尾延迟与更高可用性；样本稀疏、Provider 语义并不等价或高风险操作要求固定责任主体时，显式 allowlist 与静态绑定仍更可靠。任何收益都必须绑定请求分布、Provider 集合、并发、失败定义和质量 evaluator，而不能只报告平均延迟。

<!-- source-family:SF-2026-ARXIV-2605-14241 -->

### 参数化 Tool 只优化稳定目录，执行权仍留在显式 Contract

把完整 tool schema 与示例放在 context 中，更新和审计都很直接；目录很长时，它又会反复消耗 token，并增加工具
混淆与虚构调用。对高频且接口稳定的工具，可以把每个工具编译成可加载的 parameter module，由 soft gate 按请求
选择或组合模块。Registry/loader 拥有 module identity、版本与撤销状态，gate 只提出选择；executor 仍必须依据当前
schema、authorization 和 effect-time check 决定是否提交副作用，参数模块不能成为隐式授权。

这条 fast path 减少长目录的重复编码，却把成本转移到训练、存储、加载、路由错误、模块冲突，以及更新或撤销不够
透明。高频稳定能力可以参数化；低频、动态版本或高风险工具仍应检索显式 schema，并执行 typed validation。当前
exact-v1 只在论文定义的 Stable ToolBench、BFCL 和训练设置中支持该机制，不覆盖开放工具目录、动态版本或生产副作用，
因此不能据此删除运行时 contract。

<!-- source-family:SF-2026-ARXIV-2605-29561 -->

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

发现一个可用 Tool 不等于应该调用它。纯模型回答在知识稳定、风险低且不需要外部真值时延迟最小；无条件调用所有相关工具会增加 tail latency、费用、失败面和错误 observation。Tool selector 因而还需要一个独立的 utility admission：估计调用后可减少的决策不确定性或错误损失，并与调用延迟、失败概率、副作用风险和预算比较。

```text
current uncertainty + candidate tool contract
→ estimate bounded benefit and failure/latency cost
→ call, ask approval, use model-only path or abstain
→ attribute outcome back to the admission policy
```

selector 只决定是否提出调用，schema validation、authorization 与 effect commit 仍由 executor 拥有。utility model 错误会系统性少查关键证据或频繁调用廉价但无用的工具；高风险事实、强制合规检查和不可逆动作不能被“预计收益低”跳过。只读、低延迟且高度可靠的工具可用简单规则直接调用，低流量或不可校准场景则保留固定 policy。

<!-- source-family:SF-TOOL-CALL-UTILITY-GATE -->

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

<!-- source-family:SF-2026-ARXIV-2605-28617 -->

另一条分支允许模型用带 typed holes 的递归程序描述控制流，runtime 再把每个 hole 绑定到许可的 action、参数类型与 capability。它比逐步 tool call 更紧凑，也能表达循环与条件；但提交前必须对整个 action graph 做 type/capability check，任何未知或越权分支都 reject-before-effect，执行器而不是生成代码拥有副作用 authority。

Well-typed 只排除一类结构错误，不证明业务意图、终止性或结果正确；递归深度、资源预算、动态值和外部状态仍需独立 guard。可枚举短流程继续使用普通 typed calls 更透明，只有控制结构重复且可界定 effect system 时，程序化 proposal 才值得承担 checker 与 sandbox 成本。exact-v1 的结果只覆盖其语言和任务，不构成任意模型生成程序的安全证明。

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

### Tool Result 之后还需要独立的 Outcome Contract

结构化返回只能证明 tool call 产生了一个可解析 observation，不能证明外部状态满足任务约束。让同一个
Planner 在读到错误结果后自行判断和恢复最省组件，却容易把“看起来合理”的 failure text 当成成功，或在没有
可执行恢复路径时继续生成解释。更强的边界是在 tool result 与下一次模型决策之间加入确定性的 outcome monitor：

```text
raw tool result + predeclared postconditions
→ deterministic violation checks
→ non-binding outcome receipt
   {violations, evidence pointers, currently available recovery tools}
→ Agent proposes recovery or abstention
→ policy / executor retains action authority
```

Monitor 不应重写原始结果、替 Agent 选择动作或直接调用工具。它只拥有对公开 schema、任务合同或 nominal trace
中可复算不变量的检查权；Agent 仍拥有 proposal，policy 与 executor 仍拥有 authorization 和 side effect。特别是
`available recovery tools` 不是装饰性 metadata：只有把当前真正可调用的恢复 affordance 放回 observation，检测结果
才可能转化为有效行动。反过来，检测到 violation 也不等于存在可恢复路径。

这种 layering 用额外检查延迟、合同维护、false positive 和 observation tokens 换取更短的 failure-to-recovery
路径。守恒约束、跨系统最终一致性或未公开业务语义无法从 nominal traces 自动恢复；incident-derived fault 也可能
只提高检测率而不提高任务完成率。低风险、结果 schema 本身已经携带强 postcondition，或恢复动作必须人工批准时，
简单 validation + escalation 仍更合理。Outcome monitor 的价值应同时用 violation recall、clean-run harm、recovery
attempt correctness 与最终 task outcome 衡量，不能只报告“发现了多少错误”。

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

### 条件化机制分支与共存边界

### Tool Admission 与 Interaction Latency 必须分开控制

<!-- semantic-body-binding:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->
同一问题对弱模型可能必须调用工具，对强模型却可直接回答，因此 tool necessity 不是固定数据标签。Evaluation 先在同一 model/version 上估计 no-tool capability，再测模型是否在必要时选择、在不必要时克制；policy owner 仍按风险和成本决定执行。它揭示 knowing-doing gap，却依赖 benchmark 与能力估计，不能授权模型自评后绕过 verifier。
<!-- semantic-body-binding:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->

<!-- semantic-body-binding:SF-SPECULATIVE-INTERACTION-AGENTS-BUILDING-REAL-TIME-AGENTS-WITH-ASYNCHRONO:start -->
复杂多轮 tool path 若等完整 reasoning 后才开始交互，用户看到的 latency 由最长链决定。Agent 可在低风险、可取消的边界并行准备候选 tool call 或 UI response，但只能把它们作为 proposal；authorizer 和 side-effect identity 在真实执行前统一 commit，错误分支必须可撤销。收益是隐藏思考延迟，代价是浪费、重复调用和 stale observation；不可逆工具、权限不明或 cancellation 不可靠时回退串行。
<!-- semantic-body-binding:SF-SPECULATIVE-INTERACTION-AGENTS-BUILDING-REAL-TIME-AGENTS-WITH-ASYNCHRONO:end -->

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16364:start -->
tool-selection failure 常发生在 readout 而非工具定义未被注意；修复应区分 candidate visibility、decision readout 与 executor authorization。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16364:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16813:start -->
tool filtering 应从 goal-state 因果必要性生成最小可见集合，同时由 executor 保留完整授权；检索相似度不能成为权限。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16813:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-17519:start -->
大工具目录的 routing loss 应拆成 retrieval gap 与 confusion gap；平台需分别治理 candidate recall、semantic overlap、排序偏置与 clarification fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-17519:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-18051:start -->
复合请求的 skill routing 应先分解子目标，再检索 skill，并生成带依赖边的 execution DAG；top-k 平面列表不能表达 prerequisite/resource linkage。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-18051:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20023:start -->
工具选择不再只优化成功率，而先求满足任务的最小 capability set；planner 提议工具，policy layer 比较 privilege lattice 后降权/拒绝 over-privileged choice，并保留必要时显式 escalation。代价是 capability annotation 不全会误拒绝或低估组合权限。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20023:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20113:start -->
streaming tool use 不应在第一个 token 触发；controller 追踪 tool-intent 随解码的稳定度，在置信轨迹达到阈值后才 dispatch，未稳定则继续生成或回落到完整 query。它用 latency 换误调用率，并要求 cancellation/duplicate suppression。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20113:end -->

### Tool-composition Reward 应绑定执行不变量，而非参考轨迹

用参考 trajectory 监督多步 Tool 调用，在任务只有一条规范路径时直接；现实接口常允许不同调用顺序达到同一合法状态，逐步模仿会把等价方案误判为错误。更稳健的 reward 从 function schema、前置条件、runtime execution 和最终 state invariants 产生。

它扩大合法路径覆盖，却依赖 environment 可重置、receipt 可信和 invariants 完整；只看最终状态还可能掩盖中途越权或不可逆副作用。高风险 action 仍需逐步 authorization 与 effect audit，参考轨迹在教学、合规流程或 invariants 难以形式化时继续成立。

<!-- source-family:SF-2026-ARXIV-2605-16790 -->

### 高风险 Action 需要确定性的资本预算 Gate

只按模型 confidence 或静态 allowlist 执行动作，在损失近似均匀时简单；不同 action 的尾部风险和时间一致性不同。Action interface owner 可以把每个 proposal 与合约固定的 safe default 比较，用一致 risk mapping 估价，再从 boundary-specific reserve capital 扣减；超预算则拒绝或降级。收益是把风险变成 effect-time contract，代价是风险模型、资本分配和保守拒绝；估价错误或分布突变时必须收紧预算、转人工或仅执行 safe default。exact-v1 只支持 AAI 的形式化合同和论文实验，不证明实际损失分布或监管充分性。<!-- source-family:SF-2026-ARXIV-2605-25632 -->

## 本章在知识树中的位置

前四章构造 information state，本章首次改变 environment。下一章讨论 Planning 如何把目标拆成有依赖和前置条件的未来行动，同时保持计划只是可修正假设。

### Disclosure Minimization 不能替代 Authorization

为了减少模型看到的敏感字段，runtime 可以按 action schema 将参数分成明文、摘要、受保护引用与完全隐藏等层级，
并在最小化前对 canonical raw request 计算不可变 digest：

```text
raw typed action
→ canonicalization + attestation digest
→ field-tier disclosure view for model/reviewer
→ independent authorization over raw action identity
→ executor rechecks digest, scope and effect policy
```

Disclosure 回答“谁能看见哪些字段”，authorization 回答“谁能让哪个 effect 发生”；摘要匹配也只证明提交内容
没有在中途被替换，不证明动作被允许。Tier table、wire schema 与 policy 应从同一声明生成，避免三份配置漂移；
代价是 schema evolution、canonicalization bug、审计可读性与受保护字段调试困难。低敏感、只读工具可继续使用
完整 typed arguments；高风险工具必须让 executor 持有原始值与最终决定权。

### Capability-bearing Observation 不能由模型改写

普通 Tool 文本可以被摘要或重排；presigned URL、session token、OAuth state 等 observation 同时承载 byte integrity、scope 与 expiry，任何字符变化或延迟复用都可能改变 authority。Runtime 应把它们作为 opaque typed value 传递，模型只可引用句柄，不可重新生成内容。

这种边界减少 token corruption 和凭据泄露，却增加 secret vault、redaction、expiry/retry 与审计成本。低风险公开 URL 仍可走普通文本路径；capability token 过期、来源不可信或 context 泄露时必须重新授权，而不是让模型“修复”字符串。

现有 exact-v1 证据只是在其披露的 observation-contract protocol 中测试 presigned URL、session token 与 OAuth state 的 byte integrity 和 temporal validity；它说明一般 tool-use 能力不能替代这类合同校验，但不证明未测试模型、工具协议或生产尾部条件下具有相同失败率。模型、运行环境或工作负载字段未披露时一律保留为 Not Disclosed。

<!-- source-family:SF-2026-ARXIV-2605-17281 -->

## 从机制演进到系统设计

Tool Calling 从生成函数名和参数演进到 proposal→validate/simulate→authorize→execute→observe→recover 的 effect protocol。Schema 只描述接口；状态前置条件、principal、预算、幂等性、外部 side effect 和结果 receipt共同决定一次调用能否提交。

模拟器、constraint decoder 和 recovery path 可以减少错误执行，却会引入环境差异、latency 和新的可信组件。emulator 成功不证明真实工具安全，文本 refusal 也不证明没有 effect；验证失败或结果不可逆时必须拒绝、sandbox 或人工批准。简单只读工具仍可采用更薄的调用路径。

## 自检问题

1. 模型选择工具与平台授权执行为什么必须分离？
2. Input schema 不能替代哪些校验？
3. Tool discovery 为什么也需要 authorization？
4. Timeout 后为什么不能盲目 retry？
5. Tool result 为什么仍是不可信 Context？
6. Agent loop 哪些边界必须由 runtime 强制？
7. 为什么模型生成的 bounded program 不能自己证明语义等价和 memory bound？
8. Checked lowering 的 relation、capacity lease 与 publication gate 分别由谁拥有？

## 高风险 Action 需要因果而非相关性证据

普通 tool proposal 可以依据历史相关性和当前 context 排序；当 action 会产生高副作用，相关性证据无法回答“执行这个动作是否导致目标状态”。一个更严格的 commit gate 保存显式 causal graph，并用 intervention consistency 检查 proposal 所依赖的边是否在可控干预下仍成立。模型拥有 action proposal，causal verifier 与 policy engine共同拥有提交许可。

该分支降低把表面相关误作可执行原因的风险，却要求可维护的因果图、干预数据与冲突处理；图不完整时 false rejection 与虚假确定性都可能上升。低风险、可撤销 action 仍可使用相关性排序加 outcome verification，高风险且无法建立因果证据时应 abstain 或人工审批。[受限证据：arXiv:2605.09168v1]

<!-- source-family:SF-2026-ARXIV-2605-09168 -->

## Tool Necessity 与 Execution Admission 是两个 Gate

<!-- source-family:SF-LLM-AGENTS-ALREADY-KNOW-WHEN-TO-CALL-TOOLS-EVEN-WITHOUT-REASONING -->
最薄的 Agent 把“模型生成了一个合法 tool call”同时解释成需要工具和允许执行。在知识已经位于模型能力范围、计算可以可靠完成、或任务只要求解释时，这条路径简单且成本最低；但外部知识、超出可验证计算规模或必须产生现实副作用时，纯文本回答无法满足任务 contract。调用前应先按三类压力判断 **tool 是否必要**：知识边界、计算边界与执行可靠性。该判断只决定是否进入工具路径，不授予任何权限；不确定时可以检索受限 catalog、请求澄清或 abstain，而不是用模型自信替代边界检测。[受限证据：arXiv:2605.09252v1]

<!-- source-family:SF-RUBRICREFINE-IMPROVING-TOOL-USE-AGENT-RELIABILITY-WITH-TRAINING-FREE-PRE -->
进入工具路径后，typed schema 仍只证明参数可解析。候选 program 还应在执行前依据当前 task、registry revision、状态前置条件与 side-effect class 生成可审计 rubric；独立 checker 对照 rubric 检查候选，修复只能产生新的 proposal，只有全部硬约束通过后 executor 才能 authorize。这个 pre-execution loop 减少把语义错误交给真实环境的机会，却增加 rubric 生成、校准与重试成本；生成的 rubric 可能漏掉未建模约束，也不能证明远端工具实现诚实。低风险只读调用可保留 schema validation 加 outcome check，高风险或不可逆调用在 rubric 不完备时应 sandbox、人工批准或拒绝。[受限证据：arXiv:2605.09730v1]

两级 Gate 的演进关系是：先判断是否需要跨越模型边界，再判断某个具体 proposal 是否可以跨越执行边界。把两者合并会把“最好使用工具”误读成“这个调用已经安全”，把两者完全割裂又会产生无意义的 catalog search 与 latency。

## 小结

Tool Calling 把语言能力连接到环境，也把概率错误变成现实副作用。可靠系统把模型输出当作 proposal，由可信执行器实施 typed、authorized、observable action。下一章进入多步 Planning。

## Review notes

- Separating Disclosure from Authorization（field-tier minimization + attestation digest；
  Status: Experimental）：https://arxiv.org/abs/2608.25474v1
  - 证据边界：公开证据是论文中的本地实现与 policy literals；不证明任意远端服务、schema evolution 或
    business authorization 已自动正确。

- Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code（sealing、bounded rollback 与 compiler authority；Status: Experimental）:
  https://arxiv.org/abs/2607.13921v1

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
- Outcome Monitors（deterministic post-tool receipts 与 recovery affordance；Status: Experimental）:
  https://arxiv.org/abs/2608.19303

### Daily integration evidence trace

- `2026-05-02 / SF-TOOL-CALL-UTILITY-GATE` — exact-v1 `arXiv:2605.00737v1`；正文吸收 benefit/latency/failure-risk admission，强制合规与高风险工具仍不能被 utility 跳过。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23049` — primary `arXiv:2606.23049v1`; Method=`arXiv:2606.23049v1 — §3 Method; §3.5 Training Recipe; §4.2 Evaluation Protocol`; Evaluation=`arXiv:2606.23049v1 — §4.2 Evaluation Protocol`; non-proof=`arXiv:2606.23049v1 — §7 Discussion and Limitations; §8 Conclusion`; fallback=该 family 的 failure pressure 是：The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge. 披露的 evaluation signal 是：Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23112` — primary `arXiv:2606.23112v1`; Method=`arXiv:2606.23112v1 — §4. Method; §4.1. Overall Architecture; §4.2.1. Graph Construction and Edge Weights`; Evaluation=`arXiv:2606.23112v1 — §5.3. Error Analysis; §5.5. DPO Training Analysis`; non-proof=`arXiv:2606.23112v1 — §6. Conclusion`; fallback=该 family 的 failure pressure 是：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 披露的 evaluation signal 是：For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24551` — primary `arXiv:2606.24551v1`; Method=`arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example`; Evaluation=`arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction`; non-proof=`arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure.`; fallback=该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25605**：Primary `arXiv:2606.25605v1`；Method `https://arxiv.org/html/2606.25605v1 — §3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution`；Evaluation `https://arxiv.org/html/2606.25605v1 — §5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency`；未证明边界 `https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25705**：Primary `arXiv:2606.25705v1`；Method `https://arxiv.org/html/2606.25705v1 — §3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator`；Evaluation `https://arxiv.org/html/2606.25705v1 — §4 Experiments and Results`；未证明边界 `https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25819**：Primary `arXiv:2606.25819v1`；Method `https://arxiv.org/html/2606.25819v1 — §ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection`；Evaluation `https://arxiv.org/html/2606.25819v1 — §Experiments; Experimental Setup; Further Analysis; Error Analysis`；未证明边界 `https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25987**：Primary `arXiv:2606.25987v1`；Method `https://arxiv.org/html/2606.25987v1 — §3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought`；Evaluation `https://arxiv.org/html/2606.25987v1 — §5 WoFT Improves Surface Modeling; 5.1 Experimental setup`；未证明边界 `https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Source-family integration record

<!-- recovered-daily-20260623:AGENT-TOOL-CALLING:start -->
### 2026-06-23 evidence integration — AGENT-TOOL-CALLING

相邻章 `books/part-07-agent/79-planning.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-23049**：PhoneBuddy: Training Open Models for Agentic Phone Use 的 exact-v1 机制为：We present PhoneBuddy, a training recipe and open-model line for agentic phone use that combines a real-app environment with a mock-app environment, PhoneWorld, which reconstructs runnable mock apps from real GUI usage structure. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 该 family 的 failure pressure 是：The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge. 披露的 evaluation signal 是：Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23112**：Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning 的 exact-v1 机制为：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 该 family 的 failure pressure 是：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 披露的 evaluation signal 是：For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-24551**：GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents 的 exact-v1 机制为：We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:AGENT-TOOL-CALLING:end -->

<!-- recovered-daily-20260625:AGENT-TOOL-CALLING:start -->
### 2026-06-25 evidence integration — AGENT-TOOL-CALLING

- **SF-2026-ARXIV-2606-25605**：`3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `7.5 Failure Cases and Limitations; 8.4 Limitations` 是 `Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints` 的 source-specific 反例/局限边界；若运行条件离开 `5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25705**：`3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `5 Conclusion; short-paper and emulator-only boundary` 是 `GUI agent: Guided Exploration of User-Sensitive Screens` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Results` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25819**：`ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Canonical recovery-path construction and five injected-hazard boundary` 是 `Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability` 的 source-specific 反例/局限边界；若运行条件离开 `Experiments; Experimental Setup; Further Analysis; Error Analysis` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25987**：`3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought` 所定义的源特定机制用于把工具候选、模拟执行和恢复路径置于真实副作用 commit 之前；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `6 Next Steps and Research Vision; technical-report preliminary-results boundary` 是 `Weave of Formal Thought` 的 source-specific 反例/局限边界；若运行条件离开 `5 WoFT Improves Surface Modeling; 5.1 Experimental setup` 的验证域，`AGENT-TOOL-CALLING` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:AGENT-TOOL-CALLING:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13663:start -->
- `SF-2026-ARXIV-2606-13663` — Daily `2026-06-12`；primary `arXiv:2606.13663v1`；Books review `books-review:SF-2026-ARXIV-2606-13663`。

  **已吸收的语义增量：** tool granularity 是 interface design变量：平台应在细粒度 primitive与复合 tool之间联合评估planning burden、权限面、失败定位与复用
<!-- daily-books-trace:SF-2026-ARXIV-2606-13663:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15508:start -->
- `SF-2026-ARXIV-2606-15508` — Daily `2026-06-14`；primary `arXiv:2606.15508v1`；Books review `books-review:SF-2026-ARXIV-2606-15508`。

  **已吸收的语义增量：** visible tool menu 是运行时权限/认知界面；应按 state 与 causal path 暴露最小工具集，同时测 risky exposure、wrong call、premature action 与 token cost。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15508:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16364:start -->
- `SF-2026-ARXIV-2606-16364` — Daily `2026-06-16`；primary `arXiv:2606.16364v1`；Books review `books-review:SF-2026-ARXIV-2606-16364`。

  **已吸收的语义增量：** tool-selection failure 常发生在 readout 而非工具定义未被注意；修复应区分 candidate visibility、decision readout 与 executor authorization
<!-- daily-books-trace:SF-2026-ARXIV-2606-16364:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16813:start -->
- `SF-2026-ARXIV-2606-16813` — Daily `2026-06-16`；primary `arXiv:2606.16813v1`；Books review `books-review:SF-2026-ARXIV-2606-16813`。

  **已吸收的语义增量：** tool filtering 应从 goal-state 因果必要性生成最小可见集合，同时由 executor 保留完整授权；检索相似度不能成为权限
<!-- daily-books-trace:SF-2026-ARXIV-2606-16813:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17519:start -->
- `SF-2026-ARXIV-2606-17519` — Daily `2026-06-17`；primary `arXiv:2606.17519v1`；Books review `books-review:SF-2026-ARXIV-2606-17519`。

  **已吸收的语义增量：** 大工具目录的 routing loss 应拆成 retrieval gap 与 confusion gap；平台需分别治理 candidate recall、semantic overlap、排序偏置与 clarification fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17519:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18051:start -->
- `SF-2026-ARXIV-2606-18051` — Daily `2026-06-17`；primary `arXiv:2606.18051v1`；Books review `books-review:SF-2026-ARXIV-2606-18051`。

  **已吸收的语义增量：** 复合请求的 skill routing 应先分解子目标，再检索 skill，并生成带依赖边的 execution DAG；top-k 平面列表不能表达 prerequisite/resource linkage。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18051:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18448:start -->
- `SF-2026-ARXIV-2606-18448` — Daily `2026-06-17`；primary `arXiv:2606.18448v1`；Books review `books-review:SF-2026-ARXIV-2606-18448`。

  **已吸收的语义增量：** Computer-use skill 应把 screenshot、spatial step、semantic instruction 与 resource references组成可版本化 multimodal artifact，并允许按 topic/on-demand MCP load，避免全库 prompt 膨胀。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18448:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20023:start -->
- `SF-2026-ARXIV-2606-20023` — Daily `2026-06-19`；primary `arXiv:2606.20023v1`；Books review `books-review:SF-2026-ARXIV-2606-20023`。

  **已吸收的语义增量：** `When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents` 路由到 `AGENT-TOOL-CALLING`：工具选择不再只优化成功率，而先求满足任务的最小 capability set；planner 提议工具，policy layer 比较 privilege lattice 后降权/拒绝 over-privileged choice，并保留必要时显式 escalation。代价是 capability annotation 不全会误拒绝或低估组合权限。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20023:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20113:start -->
- `SF-2026-ARXIV-2606-20113` — Daily `2026-06-19`；primary `arXiv:2606.20113v1`；Books review `books-review:SF-2026-ARXIV-2606-20113`。

  **已吸收的语义增量：** `When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation` 路由到 `AGENT-TOOL-CALLING`：streaming tool use 不应在第一个 token 触发；controller 追踪 tool-intent 随解码的稳定度，在置信轨迹达到阈值后才 dispatch，未稳定则继续生成或回落到完整 query。它用 latency 换误调用率，并要求 cancellation/duplicate suppression。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20113:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20922:start -->
- `SF-2026-ARXIV-2606-20922` — Daily `2026-06-19`；primary `arXiv:2606.20922v1`；Books review `books-review:SF-2026-ARXIV-2606-20922`。

  **已吸收的语义增量：** `Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning` 路由到 `AGENT-TOOL-CALLING`：Tool-Guard 将 planning 与 poisoned tool description 隔离：检测到可疑/misaligned 调用后把对应 tool 加入 influenced list，后续规划不再看到其描述，但执行层仍可在受控条件下调用以保留 utility。policy owner 持有 quarantine，误报时可审计恢复。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20922:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21409:start -->
- `SF-2026-ARXIV-2606-21409` — Daily `2026-06-20`；primary `arXiv:2606.21409v1`；Books review `books-review:SF-2026-ARXIV-2606-21409`。

  **已吸收的语义增量：** tool-call repair 不能只改最终格式；应反演失败调用的 constraint、局部修补 argument 并在有限重试后回退
<!-- daily-books-trace:SF-2026-ARXIV-2606-21409:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13921:start -->
- `SF-2026-ARXIV-2607-13921` — Daily `2026-07-16`；primary `arXiv:2607.13921v1`；Books review `books-review:SF-2026-ARXIV-2607-13921`。

  **已吸收的语义增量：** 新增证据边界：Compiler authority moves from final-artifact repair into the partial-generation loop through a sealor that makes prefixes compilable for authoritative diagnostics. 该 delta 已进入 `books/part-07-agent/78-tool-calling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13921:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-17007:start -->
- `SF-2026-ARXIV-2608-17007` — Daily `2026-08-18`；primary `arXiv:2608.17007v1`；Books review `books-review:SF-2026-ARXIV-2608-17007`。

  **已吸收的语义增量：** SkillEffect 不信任模型生成的 tool program，而由独立 checker 从 immutable input 重建 source relation、bounded IR 与 live-set bound；只有唯一匹配、容量 lease 和 registered postcondition 都通过才 staged publish。六类 operator、五种 execution pattern 与 adversarial proposal 只证明已注册 plugin 的 hard-cap execution；未知 relation、parser denial-of-service、远程不可逆副作用和多租户 preflight 仍明确在保证外。
<!-- daily-books-trace:SF-2026-ARXIV-2608-17007:end -->

<!-- daily-books-trace:SF-2026-FIELD-TIER-MIN:start -->
- `SF-2026-FIELD-TIER-MIN` — Daily `2026-08-27`；primary `arXiv:2608.25474v1`；Books review `books-review:SF-2026-FIELD-TIER-MIN`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：按字段而非 action 分类为 raw、projection、never-leave 三层；client 在最小化前承诺 canonical digest，并对 policy/tier schema 版本做 attestation；并保留边界：远端服务、schema evolution 与恶意 verifier 未被实证覆盖；projection 本身仍可能泄漏。 相邻章节对读：books/part-07-agent/77-memory.md#L46;books/part-07-agent/79-planning.md#L239。Memory 拥有写入决策，Planning 拥有 policy 约束；action 字段最小化和 side-effect admission 仍由 Tool Calling 拥有。
<!-- daily-books-trace:SF-2026-FIELD-TIER-MIN:end -->
