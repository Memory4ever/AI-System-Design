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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24941:start -->
Memory 也不能绕过这条边界。长期记忆中的成本、耐心或风险偏好即使与当前任务无关，仍可能通过隐式 steering 改变 tool arguments；简单相关性提示或关键词过滤只能缓解，不能证明偏好没有渗入字段。更稳妥的控制流在 proposal 前执行 memory-to-field relevance gate：只有与当前 intent、参数 schema 和授权边界相关的 memory 才能影响字段，并记录从 memory entry 到 tool field 的 lineage。

双路径检查或 memory-masked 对照会增加延迟，也可能压低合理个性化；关键词重叠和 latent steering 则可能继续绕过过滤。高风险字段应使用 typed default、澄清或人工确认，必要时完全屏蔽 memory 后重新生成。现有实验只证明所测 Agent/tool 环境中的 drift，不能把过滤器写成通用安全保证。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24941:end -->

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

### Discovery Frontier 可以修订，但不能授予执行权

一次静态 shortlist 在目录小、接口稳定时最容易审计；开放工具生态中，早期 query 或 intent 解释错误会让真正需要的 tool 永远不进入 schema exposure。一个 bounded revisable discovery state 可以为每次 probe 保存 query/intention revision、返回的 tool identity、尝试结果、预算与 parent；并行分支只拥有 proposal，retrieval controller 去重和合并 frontier，executor 仍逐项验证 schema、version、authorization 与 effect dependency。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02411 -->

可修订 frontier 能恢复早期漏检，却增加模型调用、探索噪声、过期 tool memory 和尾延迟；弱 base model 还可能让迭代搜索放大错误描述。Catalog 小、风险高或版本不可可靠追踪时，应回退静态 allowlist 与显式 typed schema。exact-v1 只支持 StableToolBench、所测模型与预算，不证明 retrieval score 可以授权工具，也不提供开放生态的安全保证。

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

<!-- source-family:SF-2026-ARXIV-2602-10986 -->
### Tool-value Cache：Cache Hit 必须证明 Environment State 等价

最简单的 cache 用 `tool name + arguments` 作为 key。它对无副作用、输入完备且结果不随时间变化的纯函数足够，
却不能直接复用于会改变环境的工具：两次相同的 `read_file(path)`、SQL 或 shell call，可能因为先前 action、初始
环境、权限或外部依赖不同而观察到不同结果。此时复用的对象不只是 value，而是一次**从确定前置状态出发的状态
转移及其 observation**。

一种更强的分支把已执行的 tool-call sequence 组织成图或树，并让节点同时引用 tool result 与可恢复的 sandbox
snapshot。Exact hit 要求从同一初始环境沿完整、规范化调用历史到达同一节点；prefix hit 只能恢复已证明等价的
snapshot，再从分叉点真实执行后续 call，不能把最长前缀相似误写成结果等价。缓存身份至少应绑定：

```text
task / initial environment revision
+ normalized tool name, arguments and schema/runtime revision
+ ordered tool-call history and snapshot lineage
+ authorization principal and dependency versions
+ validity window
→ cache identity
```

其中论文的 exact-v1 证据直接支持受控 sandbox 中的完整历史匹配、prefix snapshot 恢复与并发 cache 服务；
`principal / dependency revision / validity window` 是把该机制推广到生产系统时必须补上的工程约束，而不是论文已
证明的实现事实。即使 key 命中，执行器也应保存原调用的 effect receipt、result provenance 与 snapshot hash，并在
tool/schema、初始镜像、权限、时钟敏感输入或外部状态发生变化时使条目失效。否则所谓 exact cache 只是在错误身份
上稳定重放旧 observation。

这条路线用更高 hit rate 和更少重复 tool wait，换取 tool-call graph、snapshot storage、并发控制、持久化、
invalidation 与恢复成本。图或快照增长会产生内存压力，cache server 会成为新的 tail-latency 与可用性瓶颈；隐藏的
非确定性、未记录的 side effect、跨 principal 复用和过期 snapshot 则会把性能优化变成 correctness 或安全故障。
受控、确定性的训练 sandbox 且 rollout 大量共享前缀时，stateful cache 值得承担这些状态；纯函数继续使用简单
content-addressed cache；真实外部系统、高风险副作用或身份无法闭合时，应 bypass cache、重新执行，并沿原有
idempotency/status-query/compensation 路径处理不确定结果。

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

若环境还提供可信、可克隆的状态与转移接口，executor 可以在真实行动前增加一层 shadow validation：先模拟候选动作，再按显式安全合同决定是否允许执行；这不是让上述 observation monitor 获得动作权限。恢复过程可以允许暂未达到终态的安全进展，但须分别检查 violation 的支持集、严重度及累计容差，不能把一个总分下降当作每项约束都满足，更不能把 `SAFE_PROGRESS` 当作任务已经恢复完成。收益以影子环境保真度、额外验证延迟及保守拒绝为代价；模型遗漏真实副作用、允许的微小回退累积，或无可信转移接口时，仍应使用更严格的执行检查与人工升级。

增加模型内部 recurrent depth 可以让一次 proposal 在提交前经历更多自我修正，却不能替代 Tool protocol。内部循环只改变模型计算状态，不会获得新环境 observation，也不会生成授权、幂等键或 side-effect receipt；外部 Tool loop 则改变真实世界并必须由 runtime 提交。纯推理任务可用内部深度减少交互，状态可能变化或需要新证据的任务仍必须通过 typed call、observation 和独立 commit。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18171 -->

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

### Tool 出现不等于 Tool 对答案有贡献

<!-- semantic-body-binding:SF-2026-ARXIV-2606-02357:start -->
只统计 call rate、格式正确率或“使用工具后的准确率”，在工具本来就是固定流程时容易实现，却无法区分模型本就会答、调用壳子改变了推理、真实结果修复了答案，还是工具噪声反而造成伤害。贡献审计应在同一模型、prompt、采样和预算下冻结至少三条反事实：no-tool、保留 call shell 但移除/替换返回值、以及真实 result；再按样本标记 confirm、repair、harm、no-effect，并把额外 tokens、latency 与调用成本共同结算。Evaluator 只拥有 attribution proposal，最终 task verifier 仍拥有 outcome truth。

这种 intervention 比 aggregate accuracy 更接近 answer-critical contribution，却增加重复运行、非确定性配对、工具环境可重放和潜在分布偏移；移除结果也可能改变后续 token trajectory，因此不是严格因果证明。环境不可复现、工具有不可逆副作用或配对条件不成立时，应回退离线 fixture、只读 shadow 或保守地报告相关性，不宣称工具带来收益。论文只覆盖披露的 multimodal agents、benchmark 和 judge，不能外推所有工具或所有任务。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-02357:end -->

### 条件化机制分支与共存边界

### Tool Admission 与 Interaction Latency 必须分开控制

<!-- semantic-body-binding:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:start -->
同一问题对弱模型可能必须调用工具，对强模型却可直接回答，因此 tool necessity 不是固定数据标签。Evaluation 先在同一 model/version 上估计 no-tool capability，再测模型是否在必要时选择、在不必要时克制；policy owner 仍按风险和成本决定执行。它揭示 knowing-doing gap，却依赖 benchmark 与能力估计，不能授权模型自评后绕过 verifier。
<!-- semantic-body-binding:SF-MODEL-ADAPTIVE-TOOL-NECESSITY-REVEALS-THE-KNOWING-DOING-GAP-IN-LLM-TOOL-:end -->

<!-- semantic-body-binding:SF-SPECULATIVE-INTERACTION-AGENTS-BUILDING-REAL-TIME-AGENTS-WITH-ASYNCHRONO:start -->
复杂多轮 tool path 若等完整 reasoning 后才开始交互，用户看到的 latency 由最长链决定。Agent 可在低风险、可取消的边界并行准备候选 tool call 或 UI response，但只能把它们作为 proposal；authorizer 和 side-effect identity 在真实执行前统一 commit，错误分支必须可撤销。收益是隐藏思考延迟，代价是浪费、重复调用和 stale observation；不可逆工具、权限不明或 cancellation 不可靠时回退串行。
<!-- semantic-body-binding:SF-SPECULATIVE-INTERACTION-AGENTS-BUILDING-REAL-TIME-AGENTS-WITH-ASYNCHRONO:end -->

Streaming 输入还要区分“可能需要某类工具”和“调用意图及参数已经稳定”。第一个 token 或局部 utterance 只能触发
可取消的准备；dispatcher 应跟踪 tool identity、argument prefix 和 intent margin 随新输入的变化，在稳定条件满足后
才提交只读调用，有副作用的调用仍等待完整 request 与 effect-time authorization。未稳定、发生反转或超过预算时，
继续收集输入、取消 draft，或回落到完整 query 后串行执行。

这种 admission 可以隐藏部分检索延迟，却会用错误预取、取消开销和 duplicate suppression 换响应速度。稳定度不是
权限，也不是事实置信度；阈值会随模型、语言、tool catalog 与网络延迟漂移。不可取消、参数长、权限高或错误调用
代价大的工具应继续等待完整意图，现有实验也只支持其受测 streaming retrieval 合同，不证明任意实时 Agent 都受益。

### 执行后行为只能更新下一次 Intent Gate

ASR 后使用一次固定 classifier，在设备、噪声和用户习惯稳定时容易校准；false wake 或漏响应反复出现后，系统可以把 repetition、cancellation、silence 等后续行为作为弱反馈，提炼带 noise、energy、speech-rate、word-count 与转写一致性的 correction pattern。它们只能更新下一轮 intent-admission proposal，不能追溯改变已经发生的 effect，也不能把“用户取消”直接解释成某句话必然没有意图：

```text
audio / ASR + device state
→ base intent proposal
→ policy gate decides suppress or continue
→ observe repetition / cancellation / silence
→ bounded correction-pattern proposal
→ slice-calibrated update for a later request
```

行为反馈器拥有 pattern proposal，policy owner 拥有 threshold 和启用范围，authorizer 仍在 effect time 判断具体 action；高风险工具不得因历史模式而跳过完整意图、参数和权限验证。自适应可减少重复误触，却引入 cold start、feedback misattribution、stale pattern、threshold drift 与 silent false rejection。新用户、语言/设备切换、clean slice 退化或 confidence 未校准时，应清空/隔离 learned correction，回退 base classifier 与显式确认。

Not All Speech Is Intent 的 exact-v1 §3.2–§3.4 支持 base classifier 与 NLU 并行、基于后续行为的结构化 correction 及设备端 suppression；§4 的 3,667 次私有 interaction 只证明作者 slices 中的条件恢复。其 54.27% 是 baseline-failure subset 的恢复率，clean/no-issue slice 在另一阈值下还会恶化；论文不证明跨用户、语言、设备或长期在线稳定性。因此这里吸收“反馈只更新未来 gate”的控制边界，不把行为 heuristic 变成用户意图真值。<!-- source-family:SF-2026-ARXIV-2609-12469 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11169:start -->
固定 tool selector 在 action space 与反馈分布稳定时最容易复算；部署环境变化后，可以在 frozen reasoner 与 executor 之间维护 per-action contextual-bandit state。Reasoner hidden state 只提供 context，每个 action 保存线性 sufficient statistics，UCB uncertainty 只决定探索优先级；action-level feedback 更新下一次 selector，不得追溯改变已发生的授权或越过 permission/effect gate。

在线适应以冷启动、unsafe exploration、reward poisoning、per-action state 膨胀和 non-stationary regret 为代价。高风险 action、反馈无法归因或 action space 快速变化时，应回退 frozen policy、allowlist、offline evaluation 与显式审批。exact-v1 只支持 ToolBench、TaskBench、TaskBench-MM、BFCL 及作者的 Qwen3-4B/Mistral-7B tool-multiset F1；它不证明真实 effect success、权限安全或生产 tail latency。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11169:end -->

继续减少交互轮次时，需要区分两种优化：逐个核对最终动作后复用预执行结果，保留原 actor 的决策边界；仅确认宏序列的首动作，再由 executor 接受其余动作，则改变了决策策略，不再是无损复用。后者可以用历史轨迹筛选宏、隔离 draft state，并在提交前检查状态和动作风险，但历史匹配概率不能证明当前后缀合法，首动作相同也不能证明后续决策相同。

因此这条近似分支须同时评价结果变化和关键路径净收益，保留逐步确认作为回退；宏命中或跳步更多不一定更快。快照、预执行、重放与额外模型资源都应计入成本，未知或不可逆副作用不能由模式置信度放行。[Speculative Macro Commit v1 §3–5](https://arxiv.org/html/2609.03236v1)的论文级实验展示了这一取舍，但也出现任务成功率下降；其专用动作检查不证明任意服务的隔离或原子提交，公开代码未取得也不能宣称实现已验证。

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

## 安全执行需要 Preventive Gate 与 Evidential Gate

Sandbox、permission 和 schema validation 在 effect 前限制“允许做什么”；test、log、diff、citation 与 postcondition 在执行后证明“实际做了什么”。只有 preventive control 会产生 false completion，只有 evidential control 又可能让危险 effect 先发生。可靠 runtime 要把 proposal、authorization、effect 与 evidence-gated submission 连成一条链。

Preventive Gate 还应验证 action 是否仍指向用户批准的对象，而不只验证语法。内容锚定的 search/replace 或带上下文 diff 在目标漂移时更容易显式失败；行号、函数名等位置锚定若仍能解析，却可能把改动静默施加到错误位置。执行器应在 effect 前重新匹配唯一 anchor、检查 expected old content，并在多匹配、零匹配或版本变化时拒绝；这用较低 applicability 和一次额外检查换取把 silent corruption 变成可恢复失败。作者在 shell command 与代码 edit benchmark 上的结果支持该失效分界，不证明其静态 verifier 覆盖任意工具、语言或并发文件修改。<!-- source-family:SF-2026-ARXIV-2609-11957 -->

position paper 或事故集合只能支持这种责任分离，不能证明某组 gate 足以覆盖所有工具。不可逆动作提高前置门槛，只读动作可以容许更轻量的后验验证；证据缺失时应返回未完成或请求人工，而不是让模型自证成功。

### Tool Evidence 与 Formal Proof 必须在 Typed Claim 上汇合

工具返回经验数值，proof assistant 证明形式命题；任一单独存在都不足以发布“已验证”的现实 claim。可靠路径先让 tool attestation 固定来源、输入与 observation，再把它提升为显式 formal statement，独立 kernel 只检查证明并成为 `Verified` 的唯一铸造者；语义映射失败、来源缺失或证明不闭合时统一 `Abstain`。Solver、模型和工具都可产生 proposal，不能自授 truth authority。

这减少 evidence laundering，却增加形式化、source audit 与 kernel trust 成本；证明正确的命题仍可能不是用户真正的问题。开放域或无法形式化的任务继续使用带来源的受限结论与人工复核。

### Approval 应绑定 Canonical Action Meaning，而不是显示字符串

同一 effect 可由 shell、MCP、browser 或 wrapper 表达，raw text policy 容易被改写绕过。Runtime 应把 event 规范化为版本化 action object，绑定 executable/operation、target、effect、externality、principal 与 reversibility，计算 fingerprint 后再附 policy verdict、approval、outcome receipt 和可选 attestation。Observe-only adapter 必须声明 enforcement depth，canonicalizer 也不能成为新的隐藏授权者。

规范化提高跨 runtime 可治理性，却引入 parser capture、schema 漂移和语义碰撞。低风险固定 API 可以直接绑定 typed request；异构高风险 action 才需要完整 canonicalization 与独立 effect-time recheck。公开 corpus 证明作者 schema 的可行性，不证明覆盖任意 runtime 语义。

<!-- source-family:SF-2026-ARXIV-2607-12650 -->
<!-- source-family:SF-2026-ARXIV-2607-13716 -->

### Computer-use Action 与完成判断应优先读取程序真实状态

纯 pixel observation 通用，却会把隐藏控件、滚动、渲染延迟和视觉相似状态混在一起。若应用暴露 accessibility tree、DOM、process/file state 或 API receipt，Agent 应把它们作为 program-state observation 来选择 action，并让 finish gate 独立读取 effect state；截图保留为覆盖缺口和跨应用 fallback。

程序状态可能不完整、权限受限或与画面不同步，因此不能静默取代视觉。每个 action 要绑定 observation revision，completion 需要 effect evidence；两路冲突时 defer/复查，而不是由模型叙述宣布成功。

<!-- source-family:SF-2026-ARXIV-2607-22798 -->

### 工具检索需要表达集合依赖，而不只是独立相关性

按 query 对每个工具独立打分，在工具少、调用彼此独立时最简单；复杂任务却常要求一组互补能力共同出现，例如一个工具产生的对象必须被另一个工具读取，或两个调用共享同一前置状态。独立 Top-k 会选出多个语义相似却无法组成可执行链的工具，也无法表达“这组工具一起可用、单个都不够”的高阶关系。

Set-level retrieval 可以把候选工具集合视为 query-conditioned hyperedge，同时预测集合大小与成员兼容性。它改变的只是 discovery proposal：Executor 仍须逐项验证 tool identity、schema/version、权限、前置状态与 effect dependency，并在执行前构造可检查的 action graph。Hyperedge score 不能替代 authorization，也不能证明工具输出正确。

集合建模用组合可执行性换来更大的搜索空间、共调用数据依赖与 cardinality calibration；新工具、权限变化或 action schema 漂移会让历史超边失效。缺少可靠组合证据时，回退独立工具检索，再由确定性 schema/dependency expansion 补齐必需成员；工具集合很小或调用真正独立时，普通 Top-k 仍更透明。exact-v1 的 ToolBench 结果不证明 learned hyperedge 能跨长尾域或动态 catalog 保持有效。

<!-- source-family:SF-2026-ARXIV-2607-25718 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18882:start -->
Tool Necessity 本身还需要可校准的 sensor，而不能只看历史调用率。一条受限的诊断路线把模型对 call/no-call 的 proposal margin 与 activation-independent call offset 分开：前者反映当前输入证据，后者近似模型固有的调用倾向。对 offset 做 inference-time steering 可以减少过度调用，但它仍只修改 proposal；外部 policy 继续拥有澄清、调用、拒绝和 effect-time authorization 的决定权。

该 sensor 依赖 SAE basis、局部线性近似与离线 calibration，模型或 workload 漂移时可能压制必要调用。高风险或低置信场景应回退显式 necessity rule、ask-user/abstain 与确定性授权。现有证据只覆盖 When2Call、六个模型和作者的 AMCS 设置，不证明偏置的训练来源、长程 Agent 行为或跨模型稳定性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18882:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15041:start -->
历史 execution trajectory 还可以被压缩成 complexity profile 与 failure profile：前者只提议 reasoning budget，后者为
schema-level reward 提供 failure attribution，真实 execution/outcome 仍由 runtime verifier 提交。这比对所有 tool task
统一 over-think 或 under-think 更节省预算，却新增 case-base drift、profile 误归因、reward shaping 与长程规划不足。
历史任务不相似、failure attribution 不稳定或执行风险高时，应回退固定 budget、普通 SFT/GRPO 与 deterministic schema gate。
exact-v1 只支持作者任务和受测模型，不能把 profile 预测当作执行授权。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15041:end -->

### 失败反馈是 Retry State，不是普通文本

把失败 tool call 的原始 transcript 直接回灌上下文，可能让模型重复同一 action；结构化、规范化的错误表示更容易让下一步区分已尝试动作、失败原因和允许的替代路径。因此 retry state 至少要包含 call identity、postcondition、错误类别、重试预算和禁止重复条件。压缩错误能够减少提示噪声，但若丢掉关键参数或环境状态，又会制造错误修复。
<!-- source-family: arxiv:2608.23651v1; semantic-body-binding: normalized-tool-error-retry-state -->

### Abstract Intent 需要有界解析为 Primitive Tool

Planner 直接生成 primitive typed call，在工具少且目录稳定时最透明；异构工具库扩展后，高层意图可能没有
单个 schema 对应。若参数修复、语义近邻替代和复合分解都塞进 planner，就会把局部 action grounding 与全局
完成判断混在一起。一个条件分支把 action 分成 executable primitive 与 abstract intent：registry 已匹配则
直接执行；否则 resolver 只在当前 action 范围内 repair arguments、substitute tool 或 decompose 为 lower-level
calls，再把规范化 observation 返回 root planner。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13228:start -->
resolver 不得输出 `Finish`，root planner 保留 evidence-sufficiency，executor/policy 仍在 effect time 验证并
提交真实调用。层级 grounding 降低 planner 对 primitive inventory 的耦合，却新增错误 substitution/decomposition、
递归循环、预算膨胀、tool metadata 维护与 context pressure；更多调用不等于更多有效证据。小型稳定目录应继续
使用 direct typed call，无法唯一 grounding 时必须返回 typed failure、请求澄清或人工处理。现有证据限于受测
Qwen3.5-9B、MVTL 与三项 video-QA full-system evaluation；baseline 的 preprocessing/runtime 并不完全同构，
也不证明高风险副作用安全。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-13228:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21751:start -->
让同一个模型同时提出优化结构并填入数字、实体与索引，在问题规模小、命名稳定时最直接；但结构正确不代表 binding 正确。文本到优化系统应把变量与约束 schema 同外部结构化数据分开：模型只拥有结构 proposal，确定性 binder/checker 解析实体、单位和索引，solver 才拥有数值可行性与提交权。这样把“会建模”与“绑定无误”拆成可独立验证的两层。

外置 binding 增加 schema、解析器、数据文件和一致性测试，也会暴露原先被端到端生成掩盖的缺失字段。exact-v1 只覆盖作者的 Text2Opt 任务、模型和 OOD cliff-shift 实验，不证明开放实体或生产求解的形式安全；binder 无法唯一解析时必须拒绝求解并请求补充信息。小型、固定且已验证的问题仍可保留端到端路径，但 solver/checker 验收不能省略。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21751:end -->

### Tool Architecture 会塑造行为，不只是暴露能力

底层信息与动作能力相近，工具的命名、粒度、状态返回和组合方式仍会改变 Agent 的探索范围、重复运行一致性、步骤数与 token 使用。tool schema 因此是 behavior-shaping interface，必须与实现和评测共同版本化。细粒度工具提供更多控制，却增加规划负担；粗粒度工具降低步骤数，却扩大隐藏副作用和验证边界。
<!-- source-family: arxiv:2608.11386v1; semantic-body-binding: tool-interface-shapes-agent-behavior -->

## 小结

Tool Calling 把语言能力连接到环境，也把概率错误变成现实副作用。可靠系统把模型输出当作 proposal，由可信执行器实施 typed、authorized、observable action。下一章进入多步 Planning。

### 可预测的只读调用可以与 Decoding 重叠

等待模型生成完整 call 再执行，最容易保证顺序与副作用安全，却把工具 latency 全部放在关键路径。若当前 symbolic future
足以唯一预测一个只读、幂等且可取消的调用，runtime 可提前启动；speculator 只拥有 provisional call，exact action match、
schema/version 与权限检查通过后，结果才能注入模型状态。它降低延迟，也引入误预测浪费、stale result 和竞态；有副作用、
参数未定或权限敏感时必须串行回退。论文结果只支持作者工具、模型和 workload。

<!-- source-family:SF-2026-ARXIV-2605-15077 -->

### 异步交互可以隐藏等待，但 Speculative Effect 必须延迟提交

串行 reason-and-act 在用户输入和工具返回完整后才继续，语义最清楚；实时交互中，模型推理和慢工具 I/O 会叠加成明显等待。另一条分支把 partial user input、tool completion、agent reasoning 与 interrupt 分成独立事件流：模型可以提出 provisional call，runtime 暂存可取消、只读调用的结果；完整输入到达后，只有通过参数一致性与 policy gate 的调用才能 commit。task manager 拥有取消和重启 scope，模型只拥有动作 proposal。

异步和推测执行用额外计算换响应时间，也引入浪费调用、过期结果、取消竞态与 partial input 泄漏。不可逆、高风险或参数依赖完整输入的工具必须等待 authoritative input，不能以低延迟为由先执行；新输入改变 request identity 时，旧 speculation 应作废或重验。exact-v1 披露的加速只绑定其模型、工具延迟和评测设置，不证明生产尾延迟、总成本或敏感工具安全；不满足可取消与无副作用条件时，串行路径仍是正确基线。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13360 -->

## Review notes

- `SF-2026-ARXIV-2609-04629`，SiLR，Status: Experimental：exact-v1 Threat Model、Method与Evaluation支持trusted shadow、executor shield及非终态安全进展分离；severity含α/ε容差，不是严格逐步不增。有限24个ANM、Qwen14B和固定budget测试不证明总体零风险；正文不把不可信LLM或非绑定monitor变为授权主体。https://arxiv.org/html/2609.04629v1

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

<!-- daily-books-trace:SF-2026-ARXIV-2607-25718:start -->
- `SF-2026-ARXIV-2607-25718` — Daily `2026-07-29`；primary `arXiv:2607.25718v1`；正文锚点“工具检索需要表达集合依赖，而不只是独立相关性”。
  本章吸收 query-conditioned hyperedge 的 set-level discovery，并保留逐工具授权、依赖校验与独立检索 fallback；ToolBench 不证明动态 catalog 或长尾域中的普遍收益。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25718:end -->

- `2026-05-02 / SF-TOOL-CALL-UTILITY-GATE` — exact-v1 `arXiv:2605.00737v1`；正文吸收 benefit/latency/failure-risk admission，强制合规与高风险工具仍不能被 utility 跳过。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2602-10986` — primary `arXiv:2602.10986v1`；Method=`§3.1 Tool Call Graph Structure；§3.2 Cache Lookups, Hits, and Misses；§3.3 Selective Sandbox Snapshotting；§3.4 TVCache Implementation`；Evaluation=`§4 Evaluating TVCache；Appendix C End-to-end evaluation configuration`；non-proof=`§6 Conclusion 及受控 sandbox / 已披露 workload 边界`；Artifact=`https://github.com/TVCache/TVCache`，但 exact commit/tag 与本次审计使用的 artifact 对应关系未披露。该版本支持完整 tool history、TCG 节点与 sandbox snapshot 共同决定复用状态，并在 terminal、SQL 与 video-understanding 后训练 workload 中验证作者实现；它不证明相同调用序列在含时钟、网络、跨租户权限或未版本化外部依赖的生产环境中必然得到相同状态，也不证明其性能结果可外推到其他 workload、硬件、并发或 SLO。Primary: https://arxiv.org/html/2602.10986v1

- `SF-2026-ARXIV-2606-23049` — primary `arXiv:2606.23049v1`; Method=`arXiv:2606.23049v1 — §3 Method; §3.5 Training Recipe; §4.2 Evaluation Protocol`; Evaluation=`arXiv:2606.23049v1 — §4.2 Evaluation Protocol`; non-proof=`arXiv:2606.23049v1 — §7 Discussion and Limitations; §8 Conclusion`; fallback=该 family 的 failure pressure 是：The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge. 披露的 evaluation signal 是：Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23112` — primary `arXiv:2606.23112v1`; Method=`arXiv:2606.23112v1 — §4. Method; §4.1. Overall Architecture; §4.2.1. Graph Construction and Edge Weights`; Evaluation=`arXiv:2606.23112v1 — §5.3. Error Analysis; §5.5. DPO Training Analysis`; non-proof=`arXiv:2606.23112v1 — §6. Conclusion`; fallback=该 family 的 failure pressure 是：Existing approaches often separate inference-time orchestration from parameter-level learning, leaving tool selection weakly structured and preference updates vulnerable to train--deployment prompt mismatch. 披露的 evaluation signal 是：For within-benchmark self-improvement, ToolGraph combines schema-derived topology, transition weights estimated from successful rollouts, and history-aware controls for write prerequisites and repeated-search loops. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24551` — primary `arXiv:2606.24551v1`; Method=`arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example`; Evaluation=`arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction`; non-proof=`arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure.`; fallback=该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25605**：Primary `arXiv:2606.25605v1`；Method `https://arxiv.org/html/2606.25605v1 — §3 Problem Definition; 4 Experimental Setup; 7 Transparent Two-Pass Execution`；Evaluation `https://arxiv.org/html/2606.25605v1 — §5 Empirical Findings; 7.3 Experimental Evaluation; 7.4 Cost and Latency`；未证明边界 `https://arxiv.org/html/2606.25605v1 — §7.5 Failure Cases and Limitations; 8.4 Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25705**：Primary `arXiv:2606.25705v1`；Method `https://arxiv.org/html/2606.25705v1 — §3 Methodology; 3.1 Query Selection, Expansion and Saturation; 3.2 Roll-out with Emulator`；Evaluation `https://arxiv.org/html/2606.25705v1 — §4 Experiments and Results`；未证明边界 `https://arxiv.org/html/2606.25705v1 — §5 Conclusion; short-paper and emulator-only boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25819**：Primary `arXiv:2606.25819v1`；Method `https://arxiv.org/html/2606.25819v1 — §ToolBench-X; Problem Formulation; Benchmark Construction; Reliability Hazard Injection`；Evaluation `https://arxiv.org/html/2606.25819v1 — §Experiments; Experimental Setup; Further Analysis; Error Analysis`；未证明边界 `https://arxiv.org/html/2606.25819v1 — §Canonical recovery-path construction and five injected-hazard boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25987**：Primary `arXiv:2606.25987v1`；Method `https://arxiv.org/html/2606.25987v1 — §3 Formal Engine; 3.2 Architecture; 4 Weave of Formal Thought`；Evaluation `https://arxiv.org/html/2606.25987v1 — §5 WoFT Improves Surface Modeling; 5.1 Experimental setup`；未证明边界 `https://arxiv.org/html/2606.25987v1 — §6 Next Steps and Research Vision; technical-report preliminary-results boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13663:start -->
- `SF-2026-ARXIV-2606-13663` — Daily `2026-06-12`；primary `arXiv:2606.13663v1`；Books review `books-review:SF-2026-ARXIV-2606-13663`。

  **已吸收的语义增量：** tool granularity 是 interface design变量：平台应在细粒度 primitive与复合 tool之间联合评估planning burden、权限面、失败定位与复用
<!-- daily-books-trace:SF-2026-ARXIV-2606-13663:end -->


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

<!-- daily-books-trace:SF-2026-ARXIV-2605-02411:start -->
- `SF-2026-ARXIV-2605-02411` — Daily `2026-05-05`；primary `arXiv:2605.02411v1`；Books review `books-review:SF-2026-ARXIV-2605-02411`。

  **写回边界：** static shortlist 扩展为 bounded revisable discovery frontier；检索分支只拥有 proposal，executor 仍验证 schema、version、authorization 与 effect dependency，开放目录安全和生产尾延迟未被证明。
<!-- daily-books-trace:SF-2026-ARXIV-2605-02411:end -->
