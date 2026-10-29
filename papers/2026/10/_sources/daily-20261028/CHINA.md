# 中国每日来源 — Daily 2026-10-28

窗口：北京时间 2026-10-27 自然日。作者：live1028_china。仅本日，不恢复10-27或历史暂停任务。
检查日期：2026-10-28；过程时钟实测 2026-10-28 01:17:38 UTC（09:17:38 +08:00），其后继续本页所列有限查询，收到用户暂停后不再检索。
状态：**用户明确恢复后继续；下方§5起更新当前判断，§1–4保留上次暂停时的真实边界，不再表示当前暂停。**

已重读 AGENTS、RESEARCH_CONTRACT、RESEARCH_SOURCES每日使用说明/分组、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、ROADMAP，以及 LEARNING_STATE 最上方暂停边界。Books/Report/State无写入，不stage/commit/push，已有dirty/index保持。

## 1. 实际入口、停止位置与缺口

| 来源 | 实际检查与停止位置 | 当前结果 / 缺口 |
| --- | --- | --- |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)当前首项Qwen3Guard标2025-09-23，但明确迁移到qwen.ai。[新站Blog](https://qwen.ai/blog)web提取0行；curl得到SPA，真实脚本版本0.0.85，未取得文章目录。有限检查p_home-index、2766、4467、9e22d361、5fb222f6、p_layout脚本，已见`/api/v2/article`引用，但完整endpoint未恢复。 | 未完成，不能以旧站日期断言当前零发布。root已收到动态浏览请求。恢复从新站Blog/Research最新目录继续，不重扫旧站历年。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)banner为V4.1-Flash-1017，跳到Search/Fetch说明；[更多/研究与动态](https://www.deepseek.com/news/)动态首项2026-09-10 V4.1 Flash，研究索引首项2026-06-24 DeepSeek-V4。页面两个“查看全部”未展开，首项均明确早于本窗。 | 本次有限目录未见窗内研究事件，停止旧页扩张，不声称全网零发布。Search/Fetch当前API功能说明无公开日期；所读内容仅接口使用和计费，不作为机制候选。`api-docs.deepseek.com/updates`实际回到Your First API Call，不假称更新列表。 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)首项新功能发布记录2025-11-07、K2 Thinking 2025-11-06，停首屏；[官方GitHub](https://github.com/MoonshotAI)显示最新10/42仓，唯一updated Oct27为kimi-code，FlashKDA Oct26已窗外，未泛扫42仓。[kimi-code releases](https://github.com/MoonshotAI/kimi-code/releases)最新2.3.3 published2026-10-26T13:22:13Z，附件也Oct26，窗外。继而只对kimi-code执行本窗commit API，见§2。 | 9条commit已有限归并；3拟入选已交sole reader校准，尚无返回；其余具体排除见§2。未扩大其他仓/年份。 |
| SRC-TENCENT-HUNYUAN | [中文Research](https://hunyuan.tencent.com/research)web0行，按合同尝试浏览器。子agent createBrowserTab hidden首次超时reset，第二次明确报“IAB visibility is not supported in a subagent thread”；不带visible参数再次超时reset，未取得All列表。 | 动态“全部”尚未核验，不能称零发布。已请root浏览中文All首页最新日期，暂停时尚无回传。恢复只接这项，不借旧英文目录或其他日结果。 |
| SRC-ZAI | 首查[中文Research](https://www.zhipuai.cn/zh/research)“全部/时间排序”首项2026/08/26 GLM-5.3-Flash，其次08/14 GLM-5.3；“查看更多”前已明确早于窗；补看[release notes](https://docs.z.ai/release-notes/new-released)最新08/26，停止。 | 有明确窗外最新项；未扩GitHub全仓。未把旧型号/目录更新时间当本窗事件。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) Publications首Recycler Oct25；[论文目录](https://seed.bytedance.com/en/public_papers)明确Newest→oldest，1–20/247、Page1/13，首项Oct25 Recycler，其次Sep28 Periodic Weak Spots；本窗已早于首项，未翻其余12页。Blog顶部SeedRealtime无日期，随后Seedance2.5 Jul31等。 | Publications有限目录无窗内项；Blog顶部SeedRealtime未核日期，若需要完整Blog覆盖须定点点开该条，不把无日期当零发布；因暂停未继续。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)第1/2页首项文心5.1日期2026-05-09，次项04-30，页尾11-21-2025；已有明确早于窗口最新项，未进入第2页。 | 有限博客目录无窗内项；未泛扫Paddle仓。 |
| SRC-XIAOMI-MIMO | [首页Paper/Blog](https://mimo.xiaomi.com/)Paper首MOPD Jun29-2026。Blog首“Diagnosing and Mitigating Tool-Call Repetition”首页无日期，定点搜索恢复[正文](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)，正文明确September27,2026（API修复checkpoint Sep25已上线）；由此不把错误窗口当候选。未点更多旧项。 | 首篇窗外，非已审重复。纠错主张未迁入本窗或Books。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)首Mini App Oct22、M3.1 Flash Oct19；[中文入口](https://www.minimaxi.com/blog)重定向minimax.cn/blog，同样首Oct22/Oct19；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)首日期Oct20产品日记/Introducing Mini App，次Oct08。 | 明确窗外最新项，停首页，不泛扫MiniMax-AI或旧文章。 |

浏览器/提取失败不是“零命中”。上表只记录真实有限覆盖，Daily总验收由root协调，不因本页落盘称完成。

## 2. Moonshot本窗9条commit与具体贡献筛选

实际请求：[本窗commit API](https://api.github.com/repos/MoonshotAI/kimi-code/commits?since=2026-10-26T16:00:00Z&until=2026-10-27T16:00:00Z&per_page=100)，返回数组9条（不足100），未请求第二页。日期字段原名`commit.committer.date`，**不单凭它宣称首次公开日期**；三拟入选另读PR的created_at/merged_at及完整核心说明。另一次未限定GitHub HTML commits页面实际返回Sep11旧缓存，未用作本窗覆盖证据。

| SHA / PR | 本窗原字段UTC | 筛选依据 |
| --- | --- | --- |
| 68a283894163204e93b072cef20db164015a5cad / #4456 | 2026-10-27T10:59:19Z | 拟入选A，见§3。 |
| e2ad1dcf214337ecfb5ca160fa36d5ef73560ab6 / #4457 | 2026-10-27T08:49:48Z | 文件树symlink展开、budget和workspace list局部接线；commit说明未提供足以改变模型/Agent系统设计的新机制或证据，排除。不把任意文件UI修复升格系统贡献。 |
| 78b72fe456ac730a1970ded9bb0d28f8b584ab95 / #4460 | 2026-10-27T06:52:47Z | 仅“apply swarm mode from prompt submissions”简述，当前信息不足判断具体执行/授权增量；**普通待补核心说明**，未假称明确排除，未完成准入。 |
| 39d149eb64e2126e7873f00758abc07c20b88c1e / #4450 | 2026-10-27T06:33:17Z | 上次仅commit核心不足，恢复后完整PR实际含局部A/B，原排除已撤回；准入同家族第4事件，见§5.3。 |
| 3154ec41f008d22f22379fa08686693470334a70 / #4451 | 2026-10-27T06:21:38Z | 恢复后完整PR实际含31会话对照；“无评价”不得成立。最终按新旧行为无区分、未支持节省或稳定失效边界排除，见§5.2。 |
| 979304401c70b2a0ea3fe18d86fc6be2d7eaf565 / #4425 | 2026-10-27T05:06:24Z | 独立dev release channel，commit仅一句；**普通待补核心说明**，暂未获具体排除/准入依据。 |
| 461c6e92d53cd4ff473fbe63fd1d238df819ef3f / #4428 | 2026-10-27T04:43:12Z | 拟入选B，PR merged_at为04:43:13Z，保留一秒差而不改名。 |
| d18a7bcd319dcc166df031b9c7e32113a58a70b5 / #4453 | 2026-10-27T04:19:31Z | sync release/2026-10-26 (2.3.3) back to main，长message累积旧PR，不据回合日期把旧session lock/swarm发布全部改成本日新事件。release页已核最新published Oct26。 |
| 4be3f0b741e13677f441c84eee40795ccc1df1db / #4283 | 2026-10-27T03:24:42Z | 拟入选C，见§3。 |

## 3. 三项拟入选：完整核心说明已读，尚待准入校准/必要证据审阅

以下是初筛提案，非最终评分或已验收结论。全部交给live1028_review（唯一非writer独核），暂停时未返回。**同一kimi-code项目的三个变更事件是否按统一材料家族归并，由root/reader协调；本页不擅报三个独立家族。**

### A. [#4456 keep the prompt cache through auto compaction](https://github.com/MoonshotAI/kimi-code/pull/4456)

身份：API `/repos/MoonshotAI/kimi-code/pulls/4456`，created_at `2026-10-27T03:39:39Z`、merged_at `2026-10-27T10:59:19Z`、merge_commit_sha=68a2838…；本窗Oct27合入实施事件，非模型发布/benchmark。

原有约束→增量→设计选择：正常auto compaction触发点`min(0.85W,W−50k)`却比旧预裁剪安全budget约0.744W更高，导致大窗口正常触发也删除最旧history破坏prompt cache；把“是否超过真实inputLimit=W−outputReserve”与“真超窗后裁至0.85安全目标”分开，同时按剩余窗口钳输出cap。413媒体降级改为捕获当时leading-media数量的固定快照，避免每加新图就滚动修改历史前缀。新增compaction probe比较实际provider投影的model/system/tools/history hash，区分客户端prefix破坏与服务端低命中，全部match也不能直接断言缓存超时。

拟2+2+2=6，owner候选AGENT-CONTEXT（缓存诊断交接PLATFORM-TRACE）。完整PR Root Cause/Code Changes/Behavior表/测试说明已读。关键限制：估算低于真实请求时首次仍可能超窗，依赖0.7/0.5/0.35 reactive回退；2%余量并非精确token oracle。作者报告回归测试与基线失败，但本次未读精确代码/test diff、未运行测试，不能说我们验证通过或量化收益。

### B. [#4428 push approvals and questions as interaction frames](https://github.com/MoonshotAI/kimi-code/pull/4428)

API created_at `2026-10-26T09:30:45Z`、merged_at `2026-10-27T04:43:13Z`、merge_commit_sha=461c6e9…；**提案公开不在本窗，只取Oct27最终合入的实现/破坏性兼容事件**，不冒首次公开。

原有约束→增量→设计选择：持久化审批/提问事件混入journal replay且过滤可能漏subagent审批；改为session全部订阅者接收无seq/offset的volatile interaction平铺帧，subscribe ack后定点补当前pending集合，恢复依赖当前引擎状态而非重放旧请求；统一kind-discriminated答复路由，engine cancelled响应先识别为cancelled而非answered。拟2+2+2=6，owner候选AGENT-PLATFORM，取消事实/授权交接AGENT-TOOL-CALLING。

完整PR核心/行为表已读，实际安全/兼容反证必须保留：旧审批/提问POST/GET删除后404；旧dist-web在下一次同步前仍可能显示请求但无法批准/回答；kimi-inspect卡片GET暂未迁移也404；TUI/print/SDK/ACP不走这些WS/REST所以不受该迁移影响。snapshot仍暂留pending字段。尚未读代码/test diff与配套code-app实际同步，不能声称完成部署或所有客户端兼容。破坏性路由/状态纠错触发受影响范围深入核验，不以6分降低必要投入。

### C. [#4283 reconnect MCP servers automatically after transient failures](https://github.com/MoonshotAI/kimi-code/pull/4283)

API created_at `2026-10-19T13:20:52Z`、merged_at `2026-10-27T03:24:42Z`、merge_commit_sha=4be3f0b…；**不称本窗首次研究公开，取最终合入实施事件**。

原有约束→增量→设计选择：启动失败工具从未注册，tool-call-healing不会被调用；SDK SSE两次重连耗尽也不足证明HTTP session已死。应用层把stdio退出作为hard证据进退避，SSE耗尽作为weak证据先ping一次；可恢复与静态凭据/config/protocol永久失败分类。每server connect/probe/close/OAuth通过operation tail串行或join，旧client在token invalidate等待前先不可用，attempt-scoped隔离迟到401；durable failure episode支持重建去重/恢复，nextRetryAt可观测。拟2+2+2=6，owner候选AGENT-MCP，失败episode交接AGENT-PLATFORM。

完整PR说明/行为表已读。限制：仅workspace baseline manager opt-in，session ephemeral servers不自动重连；5s至5min带jitter且进程存活期无总次数上限，不是所有错误无限重试；needsAuth/disabled/removed不重试。作者称真实HTTP/stdio及OAuth并发测试通过，本次未读精确diff/测试/未执行，不能说复现。连接生命周期/凭据安全受影响范围应深入核验。

## 4. 暂停后的精确续点

用户明确恢复前不运行。已通知root停止研究并仅保存此页。

1. 等root/reader同步现有回传（本页三拟入选的准入与家族归并、混元中文All、Qwen动态目录）；不得把未返回当通过。
2. 补两普通项#4460与#4425核心说明，明确贡献后关闭或纳入，不用当前简述硬归零；Seed Blog首SeedRealtime日期也未核。
3. 三拟入选若校准通过：按精确合入版本核必要代码/测试与反证，明确本窗事件；B尤其核实际不兼容范围，不把旧提案created_at改成Oct27首次公开。未获Books owner窄位，未读Books上下文/未写稿/未SAVE。
4. 只重开本日受影响入口，不恢复2026-10-27日报或2025历史；未完成来源不称外部终态。最终日级Report/Books/State仅由root协调。

## 5. 用户恢复后的缺层补齐（2026-10-28）

恢复时完整重读AGENTS、研究/Report合同、Sources使用说明与每日段、统一Prompt、ROADMAP及本日CHINA/REVIEW停点；只接未完成层。恢复检查时钟：2026-10-28 06:46:08 UTC（14:46:08 +08:00）。没有写Books/Report/State或改index。

### 5.1 来源缺层

- Seed顶部[SeedRealtime正文](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction?view_from=content_recommend)实际`Date 2026-08-05`，已明确窗外；结合论文目录首Oct25与Blog次Jul31，Seed本次有限入口检查完成，不扩历史或GitHub。
- root回传：中文混元Research也通过CUA hidden尝试38.8秒超时/kernel reset，未得All。本人定点取得当前HTML公开脚本`https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-3gZjLsMD.js`，确认`/research`复用Blog组件、中文翻译和懒加载，但有限解析未恢复公开列表endpoint。没有调用admin/private路径或登录接口。Qwen补查当前HTML明确列出的11个common脚本及main.js，未恢复文章API具体endpoint。至此停止不断扩大的bundle解析，**动态目录完整性仍受阻**，不是零发布或Coverage通过；可接受替代是当窗官方中文All/新站Blog可读目录快照或恢复正常浏览器，精确重开这两个入口，其他已成来源不重跑。

### 5.2 原普通项与代表排除修正

已分别读完整官方PR核心/行为表，而非只按修复标题关闭：

- [#4460](https://github.com/MoonshotAI/kimi-code/pull/4460)：公开schema已接受swarm_mode但路由不读取；改为prompt submit前按字段enter/exit并测试重复true/false顺序。没有新增授权判据或委派执行机制，只把已有公开参数接通；本次按局部参数接线排除，不说它没有修复价值。
- [#4425](https://github.com/MoonshotAI/kimi-code/pull/4425)：main+CI dev产物、run number幂等/旧run防护、stable/dev分流、跨渠道确认及stage/swap复核，均是常规软件发布隔离，未新增模型或Agent系统特有机制/成立边界；按范围与具体增量排除，不因其带版本标签而自动入选。
- [#4451](https://github.com/MoonshotAI/kimi-code/pull/4451)：完整PR有16会话验证/压缩对照，9会话无关失败测试及6会话本次改动失败测试对照。新旧均正确、不出现所担心过度验证，作者明确只能称无回归、不能证明修复有效；输入token约7%差来自一次额外验证、样本不足，不能用作收益。它未分离出一个改变设计结论的行为差/失效边界，维持排除；原“没有评价”措辞撤销。该修正来自唯一reader的真实抽查，本人再读完整PR核实，不把所有prompt改动机械排除。

### 5.3 准入校准与第4事件

唯一独核`live1028_review`独读三项官方PR完整核心/behavior，确认§3 A/B/C具体反例成立，各`2+2+2=6`，不是给成熟cache/retry原则计分；B/C受正确性/安全兼容变化影响，仍深入受影响范围。**同kimi-code项目1家族、当前4个具体实施事件**；不记四篇新论文，不把旧提案created_at改成Oct27。#4450由reader及作者完整PR补读后改判准入，其他三项不受影响。

[D. #4450 answer questions without edits and clean up test leftovers](https://github.com/MoonshotAI/kimi-code/pull/4450)，精确合入`39d149eb64e2126e7873f00758abc07c20b88c1e`，本窗commit字段§2；事件采用Oct27合入，API完整PR明确当前仅改`packages/agent-core-v2/src/app/agentProfileCatalog/system.md`两处与`profile-shared.test.ts`结构锚点。

新增不是“诊断需授权”成熟原则：作者同Kimi2.3.2二进制/同Kimi模型、外部自建Node项目局部A/B中，诊断“帮我看一下”基线0/3保持不改、最终10/10保持不改；带`or the request otherwise clearly includes implementation`兜底的未采用版本5次有2次动手，推理引用该句；`change`措辞6次2次误改、`action`版本10次0次。添加显式检查后的测试日志清理改善但仍有漏例（“能跑一下测试吗”最终2次仅1次干净）。因此具体软授权文字可能被模型当成扩权理由，提示约束本身不是引擎授权保证。它支持局部失败边界，不支持词汇选择普遍定律或生产越权率。

评分`1+2+2=5`（reader校准接受），标准审阅必要prompt diff已实际读：新文本按请求类型区分交付，诊断只在明确请求修复时改动，清理只删自己本轮已知产生且不需保留文件、不确定保留。结构测试仅锁提示模板位置，不能冒行为保证；行为证据仅PR作者的小样、每组1–10次，未覆盖其他模型/Windows/交互TUI/子agent/Tower。本次未复跑，不以benchmark宣称。

### 5.4 A/B/C必要证据：精确实现与可支持范围

首次拉取整个files列表合并输出截断，未当完整读；随后按具名文件恢复。以下只主张实际读到的代码/测试定义，不主张本次测试运行通过。

**A / 68a2838…**：

- [fullCompactionService.ts](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/agent/fullCompaction/fullCompactionService.ts)变更hunk：`inputLimit=W−reserve`，先比较估算messages+overhead是否真的超出，才进入原0.85 target；每次compaction传`usedContextTokens=estimate+ceil(0.02W)`。没有把2%余量加到是否shrink的判据以免重新破坏前缀。
- [fullCompaction.test.ts#L4677](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/test/agent/fullCompaction/fullCompaction.test.ts#L4677)4677–4759完整两case：构造过auto trigger上下文，检查compaction完整原历史prefix，随后summary被消费；64k max cap案例传入usedContextTokens后remaining在0与64k之间。**这证明测试定义检查预算接线/前缀，不是一次真实provider的命中率或费用实验。**
- `llmRequesterService.ts`精确diff实际读到：captureMediaDegradeCount固定快照，后加图不滚动旧prefix；新图再次413才recapture，否则仍strip回退。modelAlias/contextRevision一致才比较baseline长度前缀hash，缺baseline不伪造false。`projector-tool-exchanges.test.ts`新增snapshot后加图case实际读到保留MID/NEW/FRESH；原守卫rolling-degradation豁免删除。采用仅为**触发/目标解耦以及投影稳定条件**，不声称cache一定hit。

**B / 461c6e9…**：

- `sessionEventBroadcaster.ts`精确diff实际读：`enqueueInteraction`直接走state.queue向所有target送消息而非enqueueDurable/journal；`sendPendingInteractions`从当前`resolved:false + session tag`集合给请求target即时发送。`wsConnectionV1.ts`三个client_hello/subscribe/subscribe_v2 ack后均调用补发。
- [wsConnectionV1.test.ts](https://github.com/MoonshotAI/kimi-code/blob/461c6e92d53cd4ff473fbe63fd1d238df819ef3f/packages/kap-server/test/wsConnectionV1.test.ts)新增case实际读：subscribe及subscribe_v2都断言ack后interaction。测试用fake broadcaster只支持顺序，不独自证明生产重连无竞态/不丢审批。
- [foldFacts.ts](https://github.com/MoonshotAI/kimi-code/blob/461c6e92d53cd4ff473fbe63fd1d238df819ef3f/packages/transcript/src/history/foldFacts.ts)与`layers.test.ts`精确diff实际读：**只有`cancelled:true`且reason为`turn_ended`/`agent_closed`才识别engine cancellation**；无reason的`{cancelled:true}`测试仍折为answered，不能泛化所有cancelled对象。`interaction-wire.ts`共用core cancellation识别；`routes/interactions.ts`先查session-tag unresolved，再区分not found/ended、kind校验，响应由引擎resolve，不把展示取消当授权撤销。
- §3旧客户端404/待dist同步反证保留；本次未追踪后续dist是否部署，不据当前main猜当时发布状态。采用限定为**交互控制面pending快照恢复与transcript事实分离/取消形状**，不宣称端到端可靠性已证实。

**C / 4be3f0b…**：

- [connection-manager.ts#L580](https://github.com/MoonshotAI/kimi-code/blob/4be3f0b741e13677f441c84eee40795ccc1df1db/packages/agent-core-v2/src/mcpCore/connection-manager.ts#L580)580–752实际完整读：weak evidence只在connected→probing，ping成功保连接、失败进retry；hard evidence进retryOrFailed；config/protocol/auth-static永久失败，OAuth进needsAuth；retry仅opt-in。backoff实际是`min(initial*2^streak,max)*(0.5+random*0.5)`，故“5秒到5分”是基值/上界，实际带0.5–1倍jitter；enqueueOperation按server尾链串行，attemptId/client identity双重检查隔离旧回调。
- 同文件389–448实际读：markNeedsAuth相同entry/attempt的并发与迟到401 join相同promise，异attempt redrive；先检查rejected grant与current guard，切needsAuth再等operation tail和invalidate。只采用其具体生命周期防旧回调污染约束，不把重试当幂等保证。
- [connection-manager.test.ts#L1288](https://github.com/MoonshotAI/kimi-code/blob/4be3f0b741e13677f441c84eee40795ccc1df1db/packages/agent-core-v2/test/mcpCore/connection-manager.test.ts#L1288)1288–1418实际完整读：本地HTTP+注入SDK weak错误，健康ping保同client/toolCount且无status噪声；probe阻塞时shutdown等待；真实HTTP切500后probe失败显示retry timing，恢复healthy后回connected且toolCount回来。是测试定义，不是我们运行/生产可用性测量。
- PR给出的durable failure episode说明可作为作者实现说明保留，但两次raw `mcpFailureOps.ts`及补充broadcaster测试请求未得到可读正文，故**不额外声称已核failure replay源码或这些补充测试**；核心采用缩到已读连接证据/operation/attempt边界，必要结论不依赖这些未读部分。

### 5.5 给root的最小Books命题（不是已写入决定）

- A → `AGENT-CONTEXT`：预算的触发判据与裁剪目标不同；“为生成摘要先裁老历史”在请求本能放下时反而破坏缓存，媒体回退快照也要固定历史投影。保留估算不足时reactive回退及无真实命中率实验限制。
- B → `AGENT-PLATFORM`：transcript的事实重放不能替代当前pending交互控制面的恢复；volatile交互需订阅后补当前集合，取消状态按引擎形状判定。旧客户端路由迁移可独立失败，UI有请求≠能处理授权。
- C → `AGENT-MCP`：SSE流重连耗尽只算weak活性证据，先probe不盲目销毁仍可POST会话；恢复客户端需operation/attempt隔离，重连不证明副作用调用可重放。
- D → `AGENT-TOOL-CALLING`或其实际owner：将模糊意图解释交给模型的文字兜底可反被当授权来源；只取小样软授权反证，不把措辞修订写成硬权限系统。请root读实际owner后判断最小新增、具体已有覆盖或仅报告，勿仅按主题覆盖断言NC。

尚未写Books、没有PRE/SAVE/POST。普通待办为唯一reader必要证据复核与root实际Books判断；动态Qwen/混元缺口精确隔离。其他来源/普通项无需重扫。

## 6. 实际owner比较与四段最小稿（待PRE）

root新授权本人唯一写Ch75/78/83/84必要最小段与本人note，root不写这四章；已加载PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE，目标相关论证与相邻章节开篇/交接。比较发现：Ch75已有token reduction破坏cache与segment lifecycle，但未解释正常compaction触发和预裁剪目标错配、413滚动投影；Ch83已有startup ready subset/legacy session与新spec分界，但未分SSE weak活性/stdio hard与attempt隔离；Ch84已有event log先写后fold/事实authority，但未处理volatile pending交互恢复，容易将所有实时交互也当可重放journal；Ch78已有proposal→real principal授权与effect检查，未给出“解释请求可被软文字兜底误扩成行动”的真实局部反例。因而四者均有具体窄差额，不用主题相似授NC，不新增小节或论文清单。

### Ch75 — 接TokenPilot条件边界段之后、SideQuest驱逐proposal之前

预算内可接受与值得裁剪也不能共用同一个阈值：若自动摘要在较高水位触发，却先按更低的安全目标删除最旧历史，正常压缩请求也会主动打断可复用前缀。[一个固定实现的纠错](https://github.com/MoonshotAI/kimi-code/pull/4456)先判断完整请求是否真的超过“窗口减输出预留”，只有超出才裁到安全目标，并把摘要输出上限约束到剩余空间。媒体回退同样应固定当次拒绝时的降级范围，不能每加一张新图就滚动改写旧前缀；新请求再被拒绝时才重新评估。它增加估算、快照和前缀诊断成本；估算失准仍需缩减重试，字节前缀保持也不证明服务端命中。无缓存、真超窗或高保真输入场景继续保留原压缩/回读路径，不把较短请求当成更低总费用。<!-- source-family:SF-2026-KIMI-CODE-OCT27 -->

### Ch78 — 接real principal授权句之后、动态enum段之前

请求意图的软解释也不能自行扩大执行范围。“帮我看一下”可以要求定位原因，而非授权修改；给模型留下“上下文似乎包含实施要求”的文字兜底，可能反被它引用为动手理由。[同模型、同二进制的小样提示对照](https://github.com/MoonshotAI/kimi-code/pull/4450)观察到这种差异，但删去兜底后的局部改善不构成跨任务权限保证，清理自己生成文件的提示仍有漏例。提示应明确区分解释、诊断与行动，真正的资源scope与副作用仍由executor检查；边界不明时先说明发现或请求确认，不能让模型的意图推断替真实principal签字。额外检查、澄清与状态核对均付费，也不应借清理要求删除来源不明的用户文件。<!-- source-family:SF-2026-KIMI-CODE-OCT27 -->

### Ch83 — 接MiMo startup ready subset段之后、协议比较标题之前

在仍使用旧session式SDK的部署中，还须把“响应流断了”与“能力会话已经失效”分开。[一个固定连接管理实现](https://github.com/MoonshotAI/kimi-code/pull/4283)将SSE重连耗尽作为weak evidence，先以有界ping探测；stdio子进程退出则直接进入失败恢复。首次连接失败时工具从未注册，不能指望只有调用工具才触发的healing补救，因此需要独立的连接恢复入口。新旧连接、探测、关闭及OAuth失效处理按server串行或join，并用attempt身份丢弃旧回调，才不会由迟到失败覆盖新连接。这增加退避等待和生命周期状态；配置/协议/静态凭据错误不应无限重试，需重新授权的连接先停用。该实现只对workspace baseline启用自动恢复，局部HTTP回归不证明任意server可用性；重连成功也不证明先前工具副作用没有提交，动作协调仍回第78章。<!-- source-family:SF-2026-KIMI-CODE-OCT27 -->

### Ch84 — 接journal IO/production disk边界与marker之后、MiMo实体生命周期段之前

权威执行日志与当前待处理交互也不必采用同一交付方式。审批或提问可以用不进入journal的即时帧通知所有会话订阅者，重连后在订阅确认之后从引擎补发当前pending集合，而不是把旧请求重放成仍待回答。[一个公开迁移案例](https://github.com/MoonshotAI/kimi-code/pull/4428)采用这条分支，并将具有明确引擎取消原因的响应与“已回答”分开折叠；任意带cancelled字段的对象不能据此当取消事实。它减少对历史通知重放的依赖，却增加pending快照、重复通知和客户端版本配对责任；测试中的ack顺序不证明无竞态或恰好一次。旧答复路由删除后，旧页面仍可能显示请求但回答返回404，因此看到审批卡片不等于控制面可操作；身份、当前pending资格或配套接口不确定时应重新对账或停在等待，不由界面展示替执行授权。<!-- source-family:SF-2026-KIMI-CODE-OCT27 -->

每章本人note拟共用家族ID，只记对应PR/SHA、局部代码/test定义已读/未运行及本日CHINA/REVIEW，不抄四份方法。尚未PRE/SAVE。

## 7. 真实保存与自读

唯一reader已实际核四目标完整两侧与§6整体稿并通过PRE；root四章窄授权有效。已按原稿真实SAVE并自读新增完整段、上下邻接与本人note：Ch75正文526/note787，Ch78正文142/note981，Ch83正文104/note430，Ch84正文1072/note1252（本次保存时行号）。四章限定`git diff --check`通过，旧dirty/index保护；一次失败的占位patch没有修改文件，随后精确锚点保存，不把尝试当成功。现已发唯一reader实际POST，尚未收到时不预签。没有写Report/State或stage/commit/push。

后到实际POST：唯一reader已真实读上述四完整新增/双侧/note并确认严格原稿，限定diff通过；**kimi-code 1家族4事件、四owner实际整合生效**。四指定窄位释放；未作日级完成声明，动态目录缺口不因此消失。
