# Dec23 GLM-4.7 / 单篇 Source、owner 与逐字 PRE

## 1. 身份 / 自然日日门 / Source角色

家族`SF-2025-ZAI-GLM47-THINKING`，本轮只处理GLM-4.7发布中跨轮推理保留与逐轮开关，不新建Interleaved家族或采用整模型分数。Newton本日§3实际[官方release notes](https://docs.z.ai/release-notes/new-released)明确2025-12-22，作者本轮也实际读到该项，足以满足新增Dec22BJT自然日日门，不需秒/offset/旧09点。旧Research目录Dec21不替具体release date，也不为未知不同早稿定日。原完整空§3、window和连续§4冻结；新结论在本包及正式§1/2/5/6另责。

原本日OFFICIAL_EVENT_LIMITS/INDEPENDENT_REVIEW已实际恢复同事件[官方Blog](https://z.ai/blog/glm-4.7)动态模块core与脚注，支持Preserved Thinking保留前轮推理块、Turn-level当前请求开关，Interleaved在4.5已有，tau2 Retail/Telecom额外prompt与Airline特定domain fix/不同模型配置不能合并归因。精确同事件/窄命题有效层复用，不重新称作者读到消失模块全文。本次web模块不可访问，随后一次原URL直接GET实际404后停止；Newton本日Blog timeout亦不重试。

作者本次通过release notes明确链接实际读[GLM-4.7模型说明](https://docs.z.ai/guides/llm/glm-4.7)Introducing的retained/round-based段及[Thinking Mode](https://docs.z.ai/guides/capabilities/thinking-mode)Interleaved/Preserved/Turn-level与必要两轮示例：当前指南要求回送完整未改序reasoning_content，提供clear_thinking开关，并区分Coding Plan/standard API默认。它是当前厂商接口说明，不是不可变2025版或独立评价；当前页含后续模型/Flash内容，未把这些默认值/具体recipe倒填Dec22发布事实。release notes只授发布日；旧原core授当日机制；当前指南仅作所拟兼容性/证据边界必要核，不授历史API合同或性能因果。未播放视频、调用模型、运行代码或复现。

## 2. 准入 / 评分 / 采用域与反侧

全量丢弃旧推理、或把全部历史无条件保留，在短任务中都易实现；长coding/tool轨迹需要分别控制前轮派生推理的可见性与本轮新推理计算。具体增量是“跨轮trace retention”和“逐请求reasoning compute”两个独立接口维度，不是更长窗口/新的学习参数或普通Interleaved名称。Design Delta2＋System Reach1＋Durability2＝5，标准审阅；当前owner确有窄接口差额，按合同对该受影响域深入，不因厂商或拟整合抬分。

只采用该接口分责及成本/失效条件。厂商的整体coding/τ²提升没有匹配隔离这两个开关的消融，旧脚注配置又不同，不授保留trace导致成功率提高、一定省token/cache或通用安全。推理块是model-derived输入而非事实；继承错误/旧约束、窗口与KV增长、模板/回送格式不兼容都须回归。应用保存出处/序列并验证行为、允许回到普通历史/原文重读，是本书工程采用条件，不冒厂商完整实现。Hardware/precision、并发、总calls与此机制独立对照为Not Disclosed；不采用整体榜单因果，不追无关图/附件。

## 3. 当前owner实际对读 / 完整两侧

实际重读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、ROADMAP与State当前停点；读Ch75当前1–565及565–610执行状态邻接、末40行本人注候选边界，Ch74开头软程序/权限、Ch76开头检索接口、Ch77开头持久Memory以及Ch22开头accepted/utilization/KV边界。唯一owner为`AGENT-CONTEXT` [Ch75](../../../../../books/part-07-agent/75-context.md)：它拥有本次调用可见状态、assembly及cache identity，不是Ch22模型状态容量，不是Ch77持久化/真值，不把reflection编辑机制复制一遍。

当前Ch75“可编辑Trace仍是派生控制输入”已有反馈编辑prefix继续生成；“Context Identity与Cache”已有template/cache identity；Trace-as-State已有重排freshpass，未明确前轮reasoning retention与本轮compute开关正交。拟只插一自然段在以下完整原段/marker之后、下一标题之前，不改marker/旧段；root未授锁，不写Books。

前侧完整两段与marker：

> 可见推理 trace 还可以作为可编辑的 control artifact，而不只是诊断记录。反馈可转为删除、修改或指导片段，抑制原 verdict/end-of-thinking 后从修改的 prefix 继续生成；它不同于追加整段旧对话再要求重答。编辑者只改变派生控制输入，原始来源与原 trace 继续保存，不能据此宣称已编辑模型真实内部思维或修复了事实；新的输出仍须独立验收。
>
> 这条执行分支引入 editor/replay 调用、反馈误译和检索不充分的风险。Co-FactChecker exact-v1 的自动反馈可见 gold/rubric，真人评测只有2专家、3研究者及14 claims/3轮，不能采用普适严格改进理论。反馈不可信或需要完整审计时，append-only、原文回读与外部 verifier 继续合理，旧 verdict 消失不是正确性证据。这里编辑的是下一步生成条件，不是上一节诊断 probe 所观测的内部因果状态。

`<!-- semantic-body-binding:SF-2026-ARXIV-2604-13706:end -->`

后侧完整标题/段：

> ### Context 不只选择内容，也选择何时承诺
>
> 内部推理状态可以继续修订，公开输出却会立即改变用户、工具和后续 Agent 的行动，因此“想到了什么”和“何时说出来”是两个不同的控制问题。简单做法是每一步都暴露，适合低风险协作，却会把未经验证的中间状态变成不可逆承诺；一种训练侧分支是在构造监督轨迹时，用 entailment checker 过滤与私有推理不一致的公开 disclosure，再学习何时披露。现有证据只支持这种离线数据构造与策略学习，不证明部署时存在逐次执行的 entailment gate。生产系统若要在 private state 与 public commitment 之间增加运行时检查，那是由风险与可逆性推导出的工程选择，仍需独立实现和评价；高风险场景应由确定性规则拥有最终发布权。

## 4. 逐字 PRE / 本人末 note（待Newton/root，不是写许可）

正文单自然段：

不编辑 trace 时，也要把“前轮推理是否继续进入输入”与“本轮是否生成新推理”分开：只保留回答和工具结果在短任务中便宜透明，跨轮任务则可以继续携带模型已经生成的推理块，同时按当前请求选择是否再付推理计算。这不是扩大模型窗口、写入长期 Memory 或让旧推理成为事实。运行时需保留原序列、来源轮次与模型/模板身份，并分别验收 retention 与 compute 开关；错误推理会持续条件化后续回答，完整保留也增加窗口、KV 和敏感派生内容的占用。GLM-4.7 的公开说明支持这种接口分责，但整模型成绩与不同评测配置不能证明单独保留推理的收益，也不保证净省费或 cache 命中。接口不兼容、任务短或继承错误时，回到普通对话历史、原文回读与独立验收，不让关闭新推理被误当成清除旧状态。

本人Review note单条：

- `SF-2025-ZAI-GLM47-THINKING` — Daily2025-12-23补Dec22；[官方发布日](https://docs.z.ai/release-notes/new-released)、[原官方Blog](https://z.ai/blog/glm-4.7)既有本日core与[当前Thinking Mode](https://docs.z.ai/guides/capabilities/thinking-mode)必要域分责。2+1+2=5，retention/turn compute接口差额深入；current recipe/default不倒填2025，整体bench/配置不授保留trace的独立因果、净省费或cache保证。未核运行实现/复现；当前仅逐字PRE，尚无写许可/实际保存/POST/root接纳。

本包可立即交Newton实际必要Source/5分/owner/PRE校准及root窄位协调，不等其余Source。无共享写入、无日级通过，不预签。

## 5. 真实保存 / self-read，待 actualPOST

Newton8实际Source/score/owner/逐字PRE通过后，root本日ROOT_REVIEW§1实际授上述唯一自然段及本人末note窄位。写前实际再读当前完整两侧/末注，Ch75 cached/unstaged numstat均空；随后按§4正文逐字保存于CoFact原end marker之后/Context承诺标题之前，未改marker/原段/他note/Status。本人note只同步已发生Newton8/root许可/保存，未预POST或root写后接纳。

作者已实际顺读完整前两段、marker、新增单段、下一标题/完整承诺段及其source marker，并读本人完整末note及前注；限定两层diff-check均通过。实际正文与PRE逐字一致，当前diff仅新自然段与本人一note共4新增行。可立即请Newton实际完整新增/两侧/ownnote POST，root读回后才释放；不等待本日全部Source，不称已接纳整合或DAY。

## 6. 已发生 Newton10 actualPOST

作者已实际读Newton§10：2026-10-15T21:05:14+08:00其真实完整新增/前后两侧/本人完整note与前注及限定两层diff均已通过，正文逐字等PRE、原markers/旧文/Status保持、仅4add0del。此时尚未收到root写后接纳/释放，不代root预签；本人note暂不写未发生root状态。本日six已保存进行中，单项POST不当DAY，不重Source/PRE。
