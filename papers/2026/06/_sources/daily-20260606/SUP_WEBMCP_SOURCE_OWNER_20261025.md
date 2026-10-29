# 06387 WebMCP首次必要／正式拟6／actual Ch83具体已有覆盖

作者jun06_continue，2026-10-25，仅Daily2026-06-06补Jun05。R29完整AB/联合Jun05资格/准入复用，不第三题摘/日期；R31四新项保持独立层。本单拟2+2+2=6：设计2给动态tool presence与metadata framing不同路径，reach2给registry/runtime与effect-time数据流交接，durability2给注册/发现/调用连续身份与语义不等授权。分数只针对原文具体命题，不把既有MCP安全常识或Book决定计入。

## 必要原件与限制

实际读[exact-v1](https://arxiv.org/html/2606.06387v1)§2–6/9、T1–9与直接caption，未核图像素、代码、payload实现或复现，不扩引用或别日池。假设对手已能执行页面加载的第三方脚本，只采用本权限下的tool registry/metadata威胁；不是一般远程无权限破坏。Presence manipulation改变可见/可调用集合，framing通过名字/description/schema/hint改变模型解读；模型选中、任务完成和真正数据外发是不同结果。

§9环境为真实页面加载@mcp-b/global polyfill、Node ProxyClient到API models，非Chrome原生WebMCP/完整浏览器安全模型。三主要model GPT5.4/ClaudeOpus4.6/Gemini2.5flash、四固定场景；较旧两model只作generation对照。精确provider snapshot、全部decoding/随机重复/CI、完整任务数分母及latency/硬件/完整控制成本未统一披露，不补生产可靠或生态普遍漏洞。§5.2只披露一处Claude C4共40runs，不能搬给全矩阵。

必要直接反侧：C1main与P1不同；T3 P1发生loop前100%，P2在listTools后、P3调用dispatch前、P4首次调用后均0。文字却概括“首次调用前即可”，比表中时序支持宽；不采任意pre-call替换必成功，必须绑定具体registry snapshot/refresh实现。C3是session前抢注，不把其结果当mid-session已证。ASR定义恶意调用并发数据到sink，但testbed调用立即外发，不能据此区分独立两个概率。

T5 AB0工具名与AB1–5不同，不是完全等名的字段因果；AB1–5固定另一名，AB5组合可弱于AB1，schema效应强依model。C6零不证明name/description是共同必要条件，C7和C10各处描述/表标签口径不齐，不照录统一variant配方或字段排序。低C1/C3完成率是当前payload结果，不是此攻击class必然破坏任务；高framing完成率也不证明用户必察觉不到，作者未做人类研究。

§6.2只有两baseline防御：registration origin binding与不同origin同名拒绝、第三方调用参数限制。T9 sink ASR为0时model仍常选目标tool，故不是语义误导已消除。§9明确origin enforcement在ProxyClient模拟，非polyfill/browser实现；生命周期B及日志治理D未实现、生产代价未测。Author proposed immutabletoolid/origin/document/frame/scriptbinding、改变后plan失效重验、scope与provenance log，只有所述A/C小范围baseline，不发布完整已实现安全架构或未知同源脚本隔离保证。metadata检查、registry版本/状态维护、调用前精确身份复核、参数/外发gate、日志与全部等待/误拒均计费。

采用范围只到“工具面与调用时序是状态；发现/语义通过不提交effect”，不采headline高ASR/免疫/防御充分性。支持和关键反侧足，止此，无代码/攻击recipe。

## actual唯一owner与具体NC

唯一`AGENT-MCP` Ch83实际全文段组比较（非trace/主题命中）：

- “Tool Description 是可执行的 Discovery Interface”完整两段：description/inputschema/server-tool identity/version同一artifact；任何description更新使discovery evidence失效重测；authorization/executor在effect time复核权限和精确identity。这实际承载metadata可变不能继承旧批准。
- “从单工具扫描到组合级Admission”完整段：tool-set identity、server/update version与effect-time authorization；组合状态未知或更新证据失效即deny/quarantine。已不是假设session静态，已有update导致旧准入失效的具体分支。
- “Browser Tool 的SemanticQuarantine…”完整段及2608.24017 marker：tool identity/registering principal/credential必须绑定，quarantine只proposal、effecttime authorizer提交；恶意toolname检查前触发说明call timing是协议状态。直接覆盖本次browser工具注册主体、语义检查与执行时序责任，不只是一般安全口号。
- MCP≠ToolAuthorization段及flow、annotations/description不是唯一信任依据、Host限制data/credentials/network与approval先于effect，以及Observability段实际记录server/tool/resource、policy/error/cancel，不让任务完成代替外发许可。Ch82/84开篇交接已核，跨工具数据流继续由effectgate拥有。

因此动态presence/metadata更新、注册主体/精确identity与调用前再验、语义误导与实际外发分责已在这些真实正文共同承载；WebMCP机制名、AbortSignal或所测字段标签不是额外长期知识链。本原文尚未实现的B/D提案也不足以把既有保守合同改成新verified recipe。拟**具体已有覆盖/No Change**，无PRE/新Book/新I；保本篇受限安全反例与未披露/未验证边界于Report/Source，交唯一reader首次必要/正式6/actual NC，不第三旧已核source或Book。

root R35已独核必要/反侧与actual Ch83四具体组承载，正式6、具体已有覆盖通过，不写Books/不新I。Report已同步既成，不再普通待独核，不第三本篇或增加行政审查；不授原生browser安全或整日DAY。
