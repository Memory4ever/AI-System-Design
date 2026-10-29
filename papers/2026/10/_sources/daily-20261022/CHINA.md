# 2026-10-22 Daily — 六个中国模型官方来源

窗口：2026-10-21 北京时间自然日。执行者：`oct22_china`。检查时段：2026-10-22 09:07～09:19 +08:00。本文件只记本日实际取件、日期与贡献判断；不签独立 Source、Books 或 Daily 完成。

当前已重新读取 `AGENTS.md`、完整 Research/Report 合同、Research Prompt、Sources 使用说明/每日分组、ROADMAP 与当前 Learning State 路由。没有复用昨日候选或来源覆盖结论。检查时间以本目录各原件 HTTP `Date` 为准（本轮 2026-10-22 BJT）。本方只写本文件及 `china-*` 原件，未 stage/commit/push；既有与并发文件不动。

## 1. 目录覆盖与停止位置

| 来源 | 本日实际入口、范围与停止依据 | 当前结果与边界 |
| --- | --- | --- |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 当前 HTML 是 skeleton；当前 JS 明示 `api.hunyuan.tencent.com` 与请求头 `accept-language: zh`。按客户端 POST `/api/blog/publicList`，body `{"pageNum":1,"pageSize":1000,"renderType":0}`，真实 header `accept-language: zh`；`code=0,totalNum=11,list.length=11`，中文全列表逐项核日期；最新两项 `displayPublishTime=1790006400`（Sep22 BJT），全部 `publicAt/updatedAt` 也早于窗口。原件 [HTML](china-hunyuan.raw)、[客户端](china-hunyuan-js.raw)、[11项完整响应](china-hunyuan-api.raw)、[HTTP](china-hunyuan-api.headers)。[T1 repo](china-gh-t1.raw) 最后 push 为2025-04-03。 | Research 当前目录未见 Oct21 事件，不把 skeleton 或英文空列表当零。GitHub 另见具名 Hy-Memory 正确性/权限变更，见§2；不是 Research 发布或模型 release。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 全部/时间倒序；[page1](china-zai.raw) 到2025-12-09且 `nextPage=2,hasMore=true`；当前[客户端](china-zai-js.raw) 验证按钮写 `?page=2`；[page2](china-zai-page2.raw) 累积至2025-12-07并显示“没有更多”。最新条目 Aug26。[release notes](china-zai-releases.raw) 当前最新可见标题 Oct10。 | 已检查实际两页及补充 release notes，未见 Oct21 研究/发布说明。GitHub具名插件变化不因 commit/feature 标签自动准入。 |
| SRC-BYTEDANCE-SEED | 当前 [Research HTML](china-seed-research.raw)、[Publications HTML](china-seed-papers.raw) 与[客户端](china-seed-js.raw)重新核验：`Publication=1,Blog=2`，接口 `/api/get_article_list_v2`、`order_desc=true`、`page_token`；Publication请求须 `x-tt-locale: US`。无该header的[type1响应](china-seed-type1.raw)只有总数/游标，不能代表空列表。带header的[type1 page0](china-seed-type1-us.raw) total246、next20、has_more=true，18个当前可见条目/20槽，Sep28至May26；与SSR page1（1–20/246、13页）对应。pin单独识别：其中4项置顶，日期按PublishDate核，不把置顶当新。Blog [page0](china-seed-type2.raw) total116、next20、12可见，最新Oct14招聘，最早Feb13；[page20](china-seed-type2-p20.raw) next40，跨至2025-07，停止。 | 当前窗口不在已恢复的最新倒序段中，未见 Oct21 目录事件；不扫余下历史页。首次中文type1缺项已由当前客户端指定US header恢复，不保留为访问缺口。GitHub仅VeOmni既见的当日实质代码线索，未扩框架周源。 |
| SRC-BAIDU-ERNIE | [中文博客首页](china-ernie.raw)按日期倒序：最新2026-05-09，首页10项至2025-11-21；页尾下一页2/2明确，因目标日比最新首项晚，停止首页不读旧页。[PaddlePaddle/ERNIE repo](china-gh-ernie.raw) push2026-07-24。 | 已检查当前最新段，无Oct21事件线索；非全历史审阅。 |
| SRC-XIAOMI-MIMO | [当前主页](china-mimo.raw) Paper8项（Jun29 2026至May12 2025）、Blog15项；[当前route manifest](china-mimo-routes.raw)与[客户端](china-mimo-js.raw)提取现有文章/日期。最新诊断博客[正文](china-mimo-repetition.raw)明确Sep27；MiMo Code Jun10、1000tps Jun8、Inference May30。未标日期介绍页不是空文：当前async route组件指向iframe，沿精确src恢复正文，V2.6 [Sep22](china-mimo-v2-6-article.raw)、V2.5 [Apr22](china-mimo-v2-5-article.raw)、V2.5-Pro [Apr27](china-mimo-v2-5-pro-article.raw)、ASR [Apr2026](china-mimo-v2-5-asr-article.raw)、TTS [Apr2026](china-mimo-v2-5-tts-article.raw)、V2 [Pro](china-mimo-v2-pro-article.raw)/[Omni](china-mimo-v2-omni-article.raw)/[TTS](china-mimo-v2-tts-article.raw)均Mar18；月份级日期已足排Oct21，不补造具体日。“材料R&D”题意明确为暂缓AI for Science，不为日期另建请求。误作目录打开的[/blog/](china-mimo-blog.raw)实际是2025-12-16单篇，不把它当分页目录。 | 当前有限目录已检查，无Oct21日期事件；GitHub具名MiMo-Code正确性变化见§2。取件时曾错误省略runtime的`async/`路径得到8个190-byte Object Not Found原件（`china-mimo-chunk-*`），未将其当内容；核当前`t.u`后用`china-mimo-async-*`及iframe正文恢复。 |
| SRC-MINIMAX | [英文](china-minimax-en.raw)与[中文](china-minimax-zh.raw)研究列表均从Oct19 M3.1 Flash降序跨至2025，无分页控件/更多页信号；HTML `dateModified=Oct22`是当前网页结构化元数据，不是新发布。[Agent Tech Blog](china-minimax-agent.raw)完整可见4日期段：Oct20两篇、Oct8、Sep22、Sep19，页尾结束。 | 已检查三个目录最新段，未见Oct21博客事件。GitHub补检发现OpenAgentCore具名平台机制变化见§2；不把其main commit叫已发布版本。 |

### GitHub辅助检查的有限范围

本轮仅抓上述官方组织 `repos?sort=updated&direction=desc&per_page=30` 首段及两个清单具名repo metadata；原件为 [Hunyuan](china-gh-hunyuan.raw)、[ZAI](china-gh-zai.raw)、[Seed](china-gh-seed.raw)、[MiMo](china-gh-mimo.raw)、[MiniMax](china-gh-minimax.raw)。MiMo返回18项即全部；其余首30的尾部updated已早于窗口。`updated_at`可由非发布活动改变，`pushed_at`也不证明release或commit首次公开；它们只用于定位具名线索，不支撑当日无所有发布。未遍历全org历史、branch或所有releases。

对已见具名当日push线索，定点取 `commits?since=2026-10-20T16:00:00Z&until=2026-10-21T16:00:00Z&per_page=100`，保存8个列表；这些是导航原件，不是逐项待关闭队列：Hy-Memory30、OpenAgentCore7、MiMo-Code9、VeOmni4、zcode-plugins6、minimax-code1、Provider-Verifier5、MiniApps6。不把这些数字算原始研究命中、候选或新家族数。后四的插件UI/CI、普通SDK launcher/字段测试和MiniApp示例/排版维护未显示模型或系统机制贡献；尚未以主题关联纳入候选。

## 2. 首批校准原记录（本窗集合以§5为准，未自签Source/Books）

以下三项目各至多一个精确事件家族，先围绕必要变化命题核核心；不将30/7/9个commit逐项审阅。不因committer日期就声称release/全球首次公开。当前 [Hy-Memory releases](china-hymemory-releases.raw) 最新v1.0.4为Oct18、[OpenAgentCore releases](china-openagent-releases.raw) 最新v0.0.12为Oct20、[MiMo-Code releases](china-mimocode-releases.raw) 最新可见v0.1.15为Sep22（列表v0.1.14 published字段为Sep23，不按列表位次反推日期）。Oct21仅按官方仓库变更事件暂定位，仍需独立资格/增量核验。

### Hy-Memory：session scope在召回与破坏性去重中的传播；内部reader也要认证

- 精确[514bf5c47bc22cc211a16990ec2908e6f62d6a21](https://github.com/Tencent-Hunyuan/Hy-Memory/commit/514bf5c47bc22cc211a16990ec2908e6f62d6a21)，[API完整原件](china-hymemory-scope.raw)：已读 `intention.py`与`reader_base.py`核心patch。session查询仅建`isolation_keys`而不设user/agent时，旧L7意图召回丢scope，VDB查询可能跨用户；重复桶只按日期/期限/相似度会把另一租户记录判重并hard delete。新增透传`isolation_key/isolation_keys`，桶key加入`user_id/agent_id`。这不是抽象“加多租户”，而是检索与删除两条具体失效路径。
- 精确[0a9b10dbfc1371ed667de1cd760b736fe4bb1499](https://github.com/Tencent-Hunyuan/Hy-Memory/commit/0a9b10dbfc1371ed667de1cd760b736fe4bb1499)，[原件](china-hymemory-auth.raw)：已读三个route依赖patch和新增401/authorized路径测试。`/internal/semantic-ids`、`/internal/call-event`、`/internal/graph-snapshot`原直接注册无guard，现挂`dependencies=protected`；本地进程也不自动可信。未本地执行测试，不能声称部署已修复或全路径安全。
- 最小准入链：按session检索/本机reader往往被当作已隐含scope或信任 → 两条公开patch揭示scope透传与去重破坏边界的具体缺口 → 需重新检查派生召回、去重及内部route是否继承authority，而非只在入口做隔离。拟比较 `AGENT-MEMORY` 与 `PLATFORM-SECURITY`，唯一Books owner由root协调。

### OpenAgentCore：跨Session复用preparation与reservation-aware free-slot策略

- 精确[c2ed21de2e3e0715dd6d382bee71188d7b365313](https://github.com/MiniMax-AI/OpenAgentCore/commit/c2ed21de2e3e0715dd6d382bee71188d7b365313)，[原件](china-openagent-reuse.raw)：已读 `docs/sandbox-provider.md`与initialization核心patch。Core由Project、初始文件、setup操作建key，Provider声明`RestorePreparation/SavePreparation`配对能力；hit只finalize重绑当前Session，保存`/environment`而非Runtime状态，Provider负责Runtime image scope/24h TTL/eviction。该main变更不是v0.0.12已发布能力。
- 精确[d893afb85247995ca057467c0f7c2832e9ae2f85](https://github.com/MiniMax-AI/OpenAgentCore/commit/d893afb85247995ca057467c0f7c2832e9ae2f85)，[原件](china-openagent-slot.raw)：已读协议、`placement.Node.Reserved`和`canKeepFreeSlot`。Active含已放置但未创建sandbox的reservation；新free-slot提前暂停若把该计数看作真实运行占用，会先暂停旧sandbox再创建待分配sandbox。新增`Reserved==0`前提防止这一路径，不放宽quiesce/capture/source-stop证明。
- 最小准入链：复用环境准备能减少冷启动，但不能复用Session/Runtime authority，容量预热也不能把reservation当已执行 → 公开协议+patch分别给出缓存身份与reservation边界 → 需比较Agent平台准备产物与运行态分离及admission/回收策略。拟owner `AGENT-PLATFORM`，收益数字未披露，不作速度或生产准备保证。

### MiMo-Code：上下文投影不能改写唯一持久历史；内容重试不能复活已删除identity

- 精确[6f83cd0e171b20dc5295f2e201b18326773279ff](https://github.com/XiaomiMiMo/MiMo-Code/commit/6f83cd0e171b20dc5295f2e201b18326773279ff)，[原件](china-mimocode-lossless.raw)：已读完整新增 `lossless-session-db.md`。原turn-end prune须显式opt-in（默认不启用），rebuild-time microcompact另会改写tool parts；删除这些context-shrink路径，仍以checkpoint/compaction window boundary限上下文。不恢复旧已清空数据，不改threshold，移除旧配置须兼容加载并warn；首个rebuild请求可能变大。作者报告局部177pass但全套仍有79fail/2errors，不能写全测试通过。
- 精确[a7440d13b2aa55d435a03d1ff36d1e7a4f7abc8e](https://github.com/XiaomiMiMo/MiMo-Code/commit/a7440d13b2aa55d435a03d1ff36d1e7a4f7abc8e)，[原件](china-mimocode-identity.raw)：已读完整新增spec及processor patch。think-only/empty retry原先delete message后同ID重建，与删除后晚帧在wire形状相同；正确消费者tombstone不能区分。改逐个removePart保留message identity，保持重试预算/触发/请求历史；exhaustion仍留error shell，不宣称修改了消费者tombstone。
- 最小准入链：为压缩context或重试空输出而改写持久记录/删除重建常被看作内部实现 → 源码揭示历史不可恢复与跨连接tombstone歧义 → 需把模型输入投影和canonical历史、内容生命周期和实体identity分开。拟比较 `AGENT-CONTEXT`，root决定唯一owner与是否已有覆盖；未本地复现。

## 3. 待办边界

- `oct22_reader`已实际读Hy两核心patch/测试、OpenAgent两协议patch、MiMo两完整新增spec与identity实际patch，确认三项目具体P增量成立，同项目可合并但各事件域仍需必要核验；该结果不是日期、Source或Books最终通过。
- 六源目录普通取件已完成（无Oct21博客研究目录条目），不代表所有源绝无遗漏。
- GitHub导航不是研究待审队列。按root限定，后续仅核本窗OAC #808/#811与MiMo #2695，不扩VeOmni、其他repo或其他commits；未把导航标题当完整贡献排除、已审重复或零发布证据。

## 4. PR公开事件资格：不是以merge日期重标首次公开

| 事件 | PR创建（原UTC） | PR合并（原UTC） | 本窗资格与限制 |
| --- | --- | --- | --- |
| Hy-Memory [#81](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/81) / [raw](china-pr-Tencent-Hunyuan-Hy-Memory-81.raw) | 2026-10-19T10:59:18Z | 2026-10-21T03:02:59Z | Oct19已有公开PR核心问题/修正，Oct21是main采纳事件，不称首次公开；需root定点核有效同事件是否已处理。 |
| Hy-Memory [#82](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/82) / [raw](china-pr-Tencent-Hunyuan-Hy-Memory-82.raw) | 2026-10-19T10:59:26Z | 2026-10-21T03:40:23Z | 同上。 |
| OpenAgentCore [#808](https://github.com/MiniMax-AI/OpenAgentCore/pull/808) / [raw](china-pr-MiniMax-AI-OpenAgentCore-808.raw) | 2026-10-21T10:49:18Z | 2026-10-21T12:19:57Z | 创建与合并均Oct21 BJT；可按本窗具体公开实现事件审阅，不称已发布release。 |
| OpenAgentCore [#811](https://github.com/MiniMax-AI/OpenAgentCore/pull/811) / [raw](china-pr-MiniMax-AI-OpenAgentCore-811.raw) | 2026-10-21T15:26:27Z | 2026-10-21T15:33:23Z | 创建与合并均Oct21 BJT，明确free-slot正确性修正。 |
| MiMo-Code [#2691](https://github.com/XiaomiMiMo/MiMo-Code/pull/2691) / [raw](china-pr-XiaomiMiMo-MiMo-Code-2691.raw) | 2026-10-20T13:54:53Z | 2026-10-21T09:25:01Z | Oct20已有公开PR，不把spec updated Oct20或Oct21 merge当首次公开；root定点核同事件，不重标日期。 |
| MiMo-Code [#2695](https://github.com/XiaomiMiMo/MiMo-Code/pull/2695) / [raw](china-pr-XiaomiMiMo-MiMo-Code-2695.raw) | 2026-10-21T06:07:06Z | 2026-10-21T07:45:32Z | 创建与合并均Oct21 BJT；spec的updated Oct20是作者字段，不等于Oct20已经公开。 |

这组日期字段不是对PR历次body逐字状态的证明；对无具体早稿/身份冲突线索的本窗PR，不为排除所有假想发布渠道无限追history。早公开项未据此称本窗0贡献，也未自动当重复已审；由root核真实事件处置。

## 5. 日期收敛后的本窗两家族：必要证据、owner对照与拟稿

root明确裁决：Hy-Memory #81/#82按Oct19公开PR保留窗外恢复线索，MiMo-Code #2691按Oct20公开PR保留窗外恢复线索；Oct21 main merge不把同一核心贡献重新放入本窗。三项不称已审重复，也不扩大旧日全文/Books任务。真正本窗只有以下两家族；同一OAC家族包括#808和#811两个不同事件域，不能只审其中一个。

### A. OpenAgentCore #808/#811 — 本窗必要域已读，待独立Source/Books决定

**评分建议：** Design Delta 2（准备产物复用与reservation-aware回收有具体新接口/条件）+ System Reach 2（Core、Provider、node与daemon边界）+ Durability 3（可复用状态/运行authority与预留/占用区分）= 7；实际正确性变化也要求深入受影响域，不借分数回避。

**本方必要证据实读范围：** §2所列精确commit/PR；#808 `docs/sandbox-provider.md`、`runtime_preparation_cache.go`完整新增94行、`runtime_initialization.go`受影响分支、`services/core/tools/microsandbox-provider/preparation.go`完整新增223行；`internal/agentcapabilities/install.go`的Rebind和manifest写入、`capability_rebind_test.go`、cache hit/miss/failed-save测试、expired preparation测试；#811协议修改、Node.Reserved、SQL row向Node透传、canKeepFreeSlot条件及`TestFreeSlotWaitsForPlacedSession`。没有本地运行任何测试、VM或安装发布。

**可支持的最小命题：** preparation cache复用的是同tenant/effective files/setup输入、同image digest/workspace mode的一份准备产物，不复制Runtime daemon状态；初始file(path,body digest)、setup(request,data digest)都入SHA-256 key。hit仍执行finalize，selection hash匹配后只重绑当前Session identity；不同selection拒绝。Provider明确支持Restore/Save才走cache，Docker/E2B不声明支持时仍全量准备。helper私有目录存0600 archive，24h TTL并按总8GiB做过期/最老驱逐，TTL本身不约束繁忙节点每日新key总磁盘。保存最多占剩余准备budget一半、失败只日志；恢复失败使本Session准备失败，损坏条目删除以便后续正常全量准备，而不是把部分提取当hit继续。

**关键反证/边界：** setup若生成每Session唯一值、必须每次执行的外部副作用或24h内过期凭据，不能盲复用；该实现要求配置差异（如env/files）进入key，未提供独立cache开关。network policy不入key不是一般可忽略：PR明确prepare总走host network且Core拒绝non-enabled effective network，必须保留这一特殊前提。`/environment`以外HOME/compute-local变更不在archive。作者mx/mx2实测51MiB archive和一Template/一个冷run、数个warm/改env/过期run，支持局部机制可运行；machine hardware/CPU/RAM、统计重复/不确定性为Not Disclosed，不能把31.1→12.3秒create-to-ready当普遍加速。真实VM的extract-failure与save-budget失败域未测。static patch中的测试不是我方执行结果。

**#811的具体反例：** Active包含已placement但尚无allocation/sandbox的Reserved，free-slot后台暂停若只看full node，会在同一node lane先暂停一份旧allocation，等其完成后才创建已受理的sandbox。新规则增加`Reserved==0`，不是删除原free-slot策略，也不跳过quiesce/capture/source-stop证明。PR给一条测试集群6.6s等待trace，测试覆盖reserved使node看似full时返回ErrNotIdle；不证明所有调度公平性/饥饿或E2E SLO。

**具体owner对照：** 已按Books上下文读取PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、ROADMAP、当前checkpoint；实读`AGENT-PLATFORM` Ch84开篇、§从完整物化到分层实例化、Workspace、Runtime State Machine、Scheduling、Resume、Observability/Replay、Event Log与Sandbox预热，以及Ch83收尾交接。Ch84现有[实例粒度/ephemeral与persistent pool](../../../../../books/part-07-agent/84-agent-platform.md#scheduling-不只是-gpu)已经区分物理复用与完整任务恢复，[Workspace](../../../../../books/part-07-agent/84-agent-platform.md#workspace-是长期行动的隔离单元)与Resume已要求run identity/外部effect重对账，[Sandbox预热](../../../../../books/part-07-agent/84-agent-platform.md#sandbox-预热只能由-tool-intent-生成-proposal)要求proposal后再授权绑定。尚未具体解释“内容寻址prepared artifact命中仍重绑Session、不复制runtime-state”及“预留也计Active时提前回收反而阻塞已接纳创建”的两条新边界。因此不是只凭主题相似宣告已有覆盖；建议在Ch84 Scheduling现有pool生命周期论证之后窄写两段，不另占Ch63/Ch75 owner。仅root可落Books。

**拟写入机制正文（待reader与root裁决，不是实际Books修改）：**

为每个Session重跑文件装载、依赖安装和setup，隔离边界清楚，setup含一次性凭据或外部副作用时也仍合理；同一配置反复创建环境后，可以缓存“准备完成的产物”，而不是复用上一个Session的运行身份。缓存key应覆盖实际tenant、初始文件和setup请求及内容版本，并由provider再限定image/workspace形态；命中后只恢复workspace/packages等准备目录，仍需以匹配的capability selection把产物重绑到新Session，不带回daemon历史或completion marker，准备阶段写入的凭据仍须独立检查时效与scope。这样减少重复准备，却新增archive、有效期、磁盘总量与失效维护；TTL不能替代容量上界，依赖外部时效或必须每次发生的setup仍应全量执行，恢复错误也不能把半成品当可用环境。

预留容量还不能直接当作已经运行的资源。平台若把placement reservation计入Active，节点刚接纳一个Session便可能再次显示“满载”；此时为未来请求提前腾空slot的后台暂停，会抢在这个已接纳Session的sandbox创建之前。free-slot策略因此还要检查该节点没有等待创建的reservation，并让已有接纳先推进；原有空闲判定与quiesce/capture/source-stop证明继续成立。该条件用更细的容量状态换取少一条不必要阻塞，却不证明公平调度或跨故障原子恢复；无法确认预留与物理占用关系时，应保留保守准入和已验证回收路径。

### B. MiMo-Code #2695 — 本窗必要域已读，待独立Source/Books决定

**评分建议：** Design Delta 3（实体删除语义纠错）+ System Reach 2（engine event与consumer projection）+ Durability 3（跨连接读/事件的identity与tombstone基本约束）= 8。

**实际必要域：** [a7440d13...](china-mimocode-identity.raw)中完整`empty-turn-part-reset.md` 57行、processor21行patch、`invalid-output-continuation.test.ts`新增49行；[PR#2695](china-pr-XiaomiMiMo-MiMo-Code-2695.raw)完整问题/变化/不变域/验证说明。源码改从`Session.removeMessage`转为`MessageV2.parts`快照逐个`removePart`，再reset finish/error/completed；不是凭spec的delivered标签认实现。新增脚本provider回归捕获MessageV2.Removed，要求最终assistant ID从未出现在removedMessages、最终仅一条assistant且没有旧reasoning、存在final answer。测试断言域不证明任意消费者网络故障均收敛；我方未运行测试。

**机制与边界：** 两连接之间没有全序，消费者tombstone仍有必要。delete→same-ID update→part update这条wire形状既可能是作者想表达的重建，也可能是删除实体的晚帧；只改客户端“见update就解除tombstone”会让真正晚帧复活。producer改为reset parts而不删除identity，保留同ID给retry写入。仅think-only/invalid、非length、非json_schema且retrySafe/no tool side-effects的原分支触发；不改retry预算、模型请求历史、其他真正删除路径或Desktop tombstone；重试耗尽仍保error shell。作者报告1397pass的session suite/151pass后续窄测试及RED→GREEN，均为作者报告，不授我方复现、整机UI e2e或全系统正确保证。

**owner对照：** 唯一owner建议仍是`AGENT-PLATFORM` Ch84，不是已归Oct20的lossless Context材料。Ch84 [Event Log](../../../../../books/part-07-agent/84-agent-platform.md#长任务恢复依赖-event-log而不是-transcript)已解释append-before-fold、committed projection与reset/fork事件；[live/replay mode](../../../../../books/part-07-agent/84-agent-platform.md#从完整物化到分层实例化)已区分历史request ID和本次授权，但未讲“删除后同ID重建与晚帧不可区分，内容reset不应删除实体identity”。应在Event Log中committed projection段后补单段producer/consumer生命期边界，不重复原章append-only或把恢复历史当新授权。Ch75只负责模型可见输入派生状态，当前新增并非context压缩策略。

**拟正文（待reader与root裁决）：**

即使持久状态最后正确，投递给消费者的事件也可能表达了错误的生命周期。删除一条消息后为了重试又用同一ID重建，在读接口和实时事件没有跨连接全序时，与“已删除实体的迟到更新”形状相同；消费者若保留删除tombstone会丢掉重试正文，若见update便解除tombstone又会复活真正晚帧。只是清空本轮内容并继续同一实体时，producer应删除其parts并保留消息identity，让后续retry继续写入该实体；真正的删除和新实体创建仍使用各自生命周期。这个边界增加part级事件和状态维护，不改变重试预算、原触发条件或外部effect授权；无法证明仍是同一实体时，应显式创建新identity或只读重新对账，不能靠重启界面把歧义当成已解决。

## 6. 本方收口与交接

- 六个每日源的实际最新目录、必要iframe/API恢复与停止依据均在§1；无仅凭空响应签零发布，无当前必要目录取件缺口。有限组织首段不支撑全站绝无遗漏。
- 本窗两家族的必要原件/方法/直接边界已读，待唯一独立reader正式Source及具体owner/拟稿裁决；Books实际写入/写后验收与README由root唯一负责。本方不自签通过，不修改共享Books/索引/LEARNING_STATE。
- 窗外恢复线索仅Hy-Memory#81/#82（Oct19）和MiMo#2691（Oct20），不阻塞本窗、不冒充已审重复、不顺带重跑旧日报。
- 文件核验：CHINA内本地链接0 missing；对untracked本文件运行`git diff --no-index --check /dev/null .../CHINA.md`无空白诊断（exit1只表示与空文件存在差异）。常规限定diff检查也无诊断；未检查或更改全工作树index。
