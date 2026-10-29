# 2026-10-23 Daily — 机构13源

窗口：2026-10-22 北京时间自然日。执行：2026-10-23 09:16～，切片作者 oct23_live_org。仅当日机构入口，不扫描 Weekly、不写 Books。动态页/缓存为空不作零命中。

## 首次扫描入口与停点（完成后的结果以“来源有限收尾补记”为准）

| ID | 实际入口与停止范围 | 当前结果/限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)→[Research Index](https://openai.com/research/index/)，Most recent首屏Oct21→Sep23，首项已早于Oct22，无需Load more | 已检查入口，本窗无列项；不是互联网无遗漏断言 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) Most recent首屏Oct22→Oct20→Oct16 | 1项本窗formal verification，见下；Oct20蛋白设计标题明确AI for Science，不引入本窗 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/)首项Sep16；[Blog](https://deepmind.google/blog/)首屏October→September；[Research pubs](https://research.google/pubs/)为year/title宽目录，改用[Research blog](https://research.google/blog/)首项Oct21 | Blog最新Gemini4 Argon原文Oct13；EmbeddingGemma2 Oct6，均窗外；Google pubs没有日级过滤，不能据其首页证明当日无论文。DeepMind余October条目日期仍定点补查 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)仅标题0正文；[Blog](https://ai.meta.com/blog/)可读导航但无当前卡片，官方Muse页也0正文 | 恢复中；辅助搜索出现Muse Wonder Oct22线索，未获原始日期/核心说明，不记零 |
| SRC-QWEN | [旧Blog](https://qwenlm.github.io/)明确跳转[qwen.ai/research](https://qwen.ai/research)，新站仅shell；[GitHub](https://github.com/QwenLM)最新列表Oct22→Oct21→Oct20 | 动态目录恢复中；定点qwen-code/Qwen-MM-Plugins窗内事件，不能拿旧Blog Sep2025当当前覆盖 |
| SRC-DEEPSEEK | [Home](https://www.deepseek.com/)→[研究与动态](https://www.deepseek.com/news/) | 首页最新提示V4.1-Flash-1017；news需展开日期记录；非零断言 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)完整列表最新Nov7 2025；[GitHub org](https://github.com/MoonshotAI)最新10/42 repos到Aug3 | 只有kimi-code/checkpoint-engine显示Oct22更新；kimi-code release最新2.3.0 Oct21 05:51，窗外；checkpoint-engine commit API精确窗口发现1项修复。web commits缓存Sep4不可用于零判断 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)0正文，CUA动态浏览两轮timeout（root也失败）；当前HTML构建2026/10/16 bundle恢复只读API中。[GitHub](https://github.com/Tencent-Hunyuan)最新10/89到Oct14 | 首屏Oct22更新Hy-Memory/OmniCapBench/DiagSafe/AuK/Precise，逐个核paper/artifact而非把updated当首次公开 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)两次fetch timeout；官方索引搜索可见最新Aug26→Aug14→Jun16。[Release notes](https://docs.z.ai/release-notes/new-released)最新Aug26。[GitHub](https://github.com/zai-org)首屏Oct22→Oct20→Oct17 | Research仅缓存恢复，限制保留；zcode-plugins API窗内8commits，具体变更见下 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)首屏最新blog SeedRealtime（无日期）；[Public papers](https://seed.bytedance.com/en/public_papers)Newest→oldest首项Sep28，下接Sep1/Aug31 | Papers入口本窗无列项；SeedRealtime发布日期待查，不把无日期当窗外 |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/)最新May9→Apr30→Apr15 2026 | 当前入口无Oct22列项；无需向旧页翻；官方repo补检待执行 |
| SRC-XIAOMI-MIMO | [MiMo Home](https://mimo.xiaomi.com/)Paper首项Jun29；Blog首项Tool-call repetition无日期→[原文](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)明确Sep27 2026 | 首项窗外；次项V2.6及后续旧发布不外推本窗；官网Blog顺序是否严格时间未知，GitHub定点补检待执行 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)仅shell；[CN](https://www.minimaxi.com/blog)跳转[minimax.cn](https://www.minimax.cn/blog)最新Oct22→Oct19；[Agent Techblog](https://agent.minimax.io/docs/techblog)同名MiniApp归Oct20组 | Oct22 MiniApp正文与Techblog同名核心完全一致，优先按旧公开去重，不重复评分；待独核。org首屏Oct22→Oct21→Oct20，必要artifact补检中 |

## 来源有限收尾补记（2026-10-23 09:37 BJT）

本节更新上表执行中描述，以此最新实际停点为准；不扩成全站召回保证。

- **SRC-TENCENT-HUNYUAN目录恢复成功**：当前HTML `app-version=ed779ae6`、build-time`2026/10/16 15:32:16`；`index-Uh_m57w8.js`把/research路由到`index-Bnu48NkA.js`，其tab常量`renderType:0=all,1=paper,2=model`，调用`pageNum/pageSize/renderType`；`index-CeX5xNqy.js`暴露POST`/api/blog/publicList`。只读POST同官方API，zh header+all/page1/size10得到total11，latest100119/100116均displayPublishTime Sep22、publicAt Sep22，Hy4 preview100100 Aug28；page2仅100025 Feb3。English同参数total9均Sep23前，语言列表不混并计数。实际POST响应`200 OK`、`Date: Fri,23 Oct2026 01:36:31 GMT`、`EO-Cache-Status: MISS`，不是仅旧缓存搜索或空页。目录本窗无列项；Org artifact独立判断O4及DiagSafe同arxiv去重。无需再扫旧列表。
- **SRC-ZAI Research已恢复SSR原件**：web两次timeout后，curl当前HTML可见完整首屏日期/标题：Aug26 GLM5.3Flash、Aug14 GLM5.3、Jun16 GLM5.2、May20 ZCube一路到旧2025，最新仍Aug26，和ReleaseNotes/官方搜索索引一致。不是仅缓存，停止不点旧查看更多。zcode窗口8commits已按核心贡献/代表排除处理。
- **SRC-GOOGLE-AI**：DeepMind October相关条目原文逐个核日期：Argon及安全/Robotics Oct13、Singapore ondevice scam Oct14、EmbeddingGemma2 Oct6；forest mapping/antimicrobial peptide标题明确AI for Science，不引入。Research blog首项Oct21、pubs为year/title宽目录；有限官方主题日期搜索只返回旧稿，未证明pubs当日完整召回，保精确目录日筛限制，不把宽目录逐项化。
- **SRC-META-AI**：Research shell、Publications页面明确content unavailable；Blog可读当前首屏最新Jul27/Jul21。第三方Oct22 Muse Wonder线索已回[官方News原文](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)明确Oct12首发/Oct13修改，日文官方页也明确美国Oct12公告，排窗，不据search recency重收。官方Research/Publications动态覆盖仍有限，保访问差额，不记确定零；重开条件是该目录可读日级结果或具体Oct22官方原稿。
- **SRC-QWEN**：旧Blog跳新站，research/blog均shell，新站当前HTML无日期列表，浏览器在本任务树实际timeout。Org最新10/60到Sep21，Oct22 qwen-code/Qwen-MM-Plugins两个仓库触发窗口事件；docs翻译库不扩队列。qwen-code窗口55commits只导航，明确执行/正确性改变O5；OmniDR已完整核心读，是video/ASR/search+分工review交付组合，未给比已有研究工作流新增可验证机制/适用边界，排除贡献。新站全目录日筛差额精确隔离，不授0/无遗漏，重开具体Oct22公告或可读目录。
- **SRC-DEEPSEEK**：News首屏动态最新Sep10，研究索引最新Jun24→Feb25→Jan28，两个查看更多只会向旧稿扩，停止。首页1017版本提示窗外，API /updates实际落firstcall非dated archive，不把该跳转当时间证据。所读官方入口本窗无列项。
- **SRC-BYTEDANCE-SEED**：无日期置顶SeedRealtime回原文Date明确2026-08-05；Publications latest Sep28，Blog其余Jul31以后向旧，停止；已检查有限入口无本窗列项。
- **SRC-BAIDU-ERNIE**：官方Blog最新May9；repo release/v1.5 README latest2025-11，精确窗口commits API返回[]；停止，无本窗已知事件。
- **SRC-XIAOMI-MIMO**：首项tool repetition原文Sep27；GitHub latest10/18，除MiMo-Code Oct22外其余Oct19及更旧，窗口4commits仅两项核心变化O6，两个compose文档/anchor修复不以功能名贡献准入。
- **SRC-MINIMAX**：MiniApp Oct20/22核心相同并与实际Ch84已有SF对应，reader独核去重通过。Org最新10/37到Oct2，MSA精确窗API[]；ProviderVerifier三条围绕M3A case/packet-size gate/stream include usage，不给新的质量资源或正确性机制证据，排贡献；OpenAgentCore本窗7条以O7明确恢复/存储/编码边界筛选，不把所有更新当候选。
- **SRC-OPENAI、SRC-ANTHROPIC、SRC-MOONSHOT**按表停点有效；O1–3已经reader校准，O2 load/post上下文又读worker.py:168–243，load两个if而post为if/elif，不泛称两个draft接口同时存在时都获post或更新原子性。

当前来源执行已完成有限入口/相关机制发现；保留Google pubs日筛、Meta Research/Publications、Qwen新Blog三个目录差额，不支撑确定零或无遗漏。其余普通工作是已发现O4–7必要审阅/Books与独核，不可标成外部保留。

## 首批准入与独核

### O1 — Anthropic formal-verification

[官方原文](https://www.anthropic.com/research/formal-verification)，Published Oct22 2026；完整阅读Introduction、Turning tests into proofs、Finding/fixing bugs、This is just beginning、Limitations及脚注。新增不是“LLM可以写证明”：将已有OSS-Fuzz入口编译成带ASan的RISC-V binary，以机器与OS形式语义机械生成全称no-crash规格，再由Claude写Rocq proof、kernel核验；失败可patch并重新生成规格。作者报告239入口/123库，规模是作者证据，不是复现。

原约束：fuzz只采样且手写完整spec昂贵→增量：把现有入口变为有界binary证明义务→改变选择：验证反馈可以收敛于机器可检验的明确定理，而非增加采样次数；仍不证明整个库/真实部署无bug。初分2+2+3=7经reader准入校准修为2+2+2=6（可复用稳定边界而非长期基础新定律）。因Ch80具体知识缺口按受影响域深入。唯一拟owner AGENT-REFLECTION，Books由root处理。

必要反侧：static/single-thread/musl/RISC-V与真实x86/ARM动态glibc不同；ASan与入口不全，caller误用不覆盖；数亿token成本，完整运行成本Not Disclosed。fn6允许patch存在把功能删掉而证明变易的reward hack，作者惩罚patch/鼓励最小行为变化并audit，不是功能等价证明。reader R1补读必要附录pp1–2：ASan no-crash、ASan/plain trace与终态等价、plain no-crash三义务分别存在，有限trace等价不足以排除silent loop，不能把正文always exit外推为终止性证明；附录严格<64MiB，不把正文64MB口径混算。17%共享证明节省与跨模型数字不纳采用命题。

独核：oct23_live_reader已独立正文与必要附录，准入和Source通过，见[REVIEW](REVIEW.md)R1；这不代替Books实际写后复核。

### O2 — checkpoint-engine IPC V2 drafter correction（reader Source通过；Books由root处理）

[commit 0ac607299eb711cdd6b164e9eba04a7ade9cf98b](https://github.com/MoonshotAI/checkpoint-engine/commit/0ac607299eb711cdd6b164e9eba04a7ade9cf98b)，GitHub commit API committer/author `2026-10-22T03:31:30Z`，merge `2026-10-22T03:31:31Z`；PR112 created `2026-10-21T11:46:47Z`，因此本窗事件是合入具体实现而非首次提出修复。

当前[窗口API](https://api.github.com/repos/MoonshotAI/checkpoint-engine/commits?since=2026-10-21T16:00:00Z&until=2026-10-22T16:00:00Z&per_page=100)单条结果；[PR API](https://api.github.com/repos/MoonshotAI/checkpoint-engine/pulls/112)body为null。精确diff仅worker.py：load hook新兼容`get_draft_model()`并给draft load weights；post hook对V2 draft执行`process_weights_after_loading`且使用`speculative_config.draft_model_config`。原约束/增量：IPC target更新不能代表draft更新与其后处理表示同步→V2分支显式补齐两阶段→同一更新需覆盖实际消费模型及后处理路径。拟2+1+2=5；具体正确性修复触发深入，但现有材料只证明新增代码路径，未复现、无性能数字、不证明更新原子性或端到端输出等价。

### O3 — ZCode bounded background retention（reader Source/PRE通过；Books由root处理）

[commit d33f6c0ce7b011147410e3141329e2d865ec6a22](https://github.com/zai-org/zcode-plugins/commit/d33f6c0ce7b011147410e3141329e2d865ec6a22) API committer `2026-10-22T07:51:03Z`。读docs/craft-ui-validation.md新段、craft-runtime server/automation与retention.test.mjs。九个Craft页面资源声明`_meta.ui.backgroundRetention=true`，长轮询只有取得真实任务时回`_meta["zcode/activity"]=true`续活，空poll不续；文档宿主规则>4后台页面、30分钟不活跃且不busy可回收，未保存页面内存会丢，120秒单操作限制保留。拟1+2+2=5，新增是UI后台状态保留和业务进展续租的接口约束，不把编辑器功能拼装当研究。宿主回收实现未在本repo展示，测试证明metadata/正任务标记断言，不证明所有宿主/平台可靠性；作者仅PhotoCraft macOS arm64 Electron44.7.0实际验证，余8编辑器视觉/Windows/Linux未验。

### O3 精确 Books PRE（reader已通过，root唯一writer）

位置：Ch83 `Primitive 类型不是安全等级`段后、Lifecycle节前；邻接Ch84 MiniApp应用装配不重复。精确拟写：

当 Resource 承载可交互页面时，还应区分资源可读、页面仍驻留与业务结果已保存。短时页面随隐藏销毁可减少资源占用；长任务编辑器可向特定 Host 显式请求后台保留，但空长轮询不应被当作业务进展无限续期。[ZCode 的固定实现](https://github.com/zai-org/zcode-plugins/commit/d33f6c0ce7b011147410e3141329e2d865ec6a22)用资源 `_meta.ui.backgroundRetention` 声明和仅取得实际任务时回传的 `_meta["zcode/activity"]` 更新活性；这些是 host-specific 扩展，不是 MCP 标准或任意 client 都识别的保证。回收会丢失未保存页面内存，因此驻留许可不等于 durable storage，也不证明工具副作用已提交；无法协商时应保存/重建状态或使用前台简单路径。metadata/contract test 只证明该声明与任务标记，host 回收及跨平台安全另需验证。<!-- source-family:SF-2026-ZCODE-BOUNDED-BACKGROUND-RETENTION -->

## 第二批明确机制事件（已读完整核心，准入待reader校准）

以下GitHub窗口查询参数统一`since=2026-10-21T16:00:00Z&until=2026-10-22T16:00:00Z&per_page=100`，只用作导航；未把全部commit变为逐PR审阅队列。事件以Oct22实际merge/实现变更限定，不把旧论文重新收录。每个repo家族只计一次，多个本窗事件在家族内分别审阅。API `pulls/N`保留author body原始说明及merged_at，作者测试不冒复现。

### O4 Hy-Memory / MemHub authority与原生prefetch

[PR132](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/132) `merged_at=2026-10-22T07:24:21Z`，[PR145](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/145) `12:02:28Z`，[PR146](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/146) `12:49:24Z`，[PR143](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/143) `08:51:15Z`。四项API完整核心/原因/验证/边界已读。

原约束App和SDK各持memory authority会引出双重提取/重试、raw重复和migration歧义→本窗SDK为唯一memory/raw authority，App一条durable job对应一次SDK add/add_extracted及outcome，停writer的启动离线migration成为唯一特权store access例外；同文件系统staging、保留SDK-only记录、root原子切换/失败rollback及中断恢复，migration deferred/blocked禁止runtime启动→需把管理平面队列和记忆数据平面authority拆开，而非仅改API名称。PR132 initially pinned dev3，后续2.0.5 release，不把早期dev3当稳定已发布。PR145删2964行private bridge且加architecture gate，Graph投影直访Kuzu仍是具名例外。拟2+2+2=6，深入受影响迁移与写入域；不采作者数千测试作生产或故障全证。

PR143另有明确行为边界：原生Hermes prefetch沿已授权Broker /context而非裸HTTP；消费上一turn warmed结果而非要求相邻query完全相同；每Hermes session记opaque memory IDs，重启仅保存hashed-session→ID，rewind/reset清对应session；managed provider read-only、禁auto capture、给injected block保留边界且采集adapter剥离此块，防同一derived memory再次当用户事实写回。对应memory写入/来源治理，不证明任意prompt injection免疫。候选需单独验证这项与现有书稿之差，不混入旧2610.22196论文结论。

### O5 Qwen-code 同家族多个执行/正确性事件

- [PR15104](https://github.com/QwenLM/qwen-code/pull/15104)，merge `2026-10-22T00:09:13Z`：Managed idle-only手动context compression作为durable operation（独立revision/actor-scoped idempotency/capability），而非创造user Turn；chunked candidate先落盘、PostCompact后与terminal维护结果原子commit、fence stale writer，不确定提交对账原证据。audit transcript保留、模型history重开恢复；压缩后usage unknown直到真实主模型观测。unknown Hook保持recovery_blocked，不等于重跑安全；纯摘要中断可再付模型费但history至多commit一次。完整核心和risk已读；macOS/确定性provider/loopback HTTP，不证明真实上游质量或跨平台部署。API1.81.0、schemaV16需reader先writer后部署，rollback先停admission结算。
- [PR15131](https://github.com/QwenLM/qwen-code/pull/15131)，Oct22合入：取消接纳不是原执行已terminal；恢复查询原Turn、retry budget/execution identity，unknown/evidence unreadable保守阻塞，晚到旧cancel不得杀下一个Turn；新会话handoff仅有授权、可编辑quoted text，非自动提交。body完整核心/主要反例已读，测试计数不采。与PR15104同家族不同事件，候选6分范围不能省略未核部分。
- [PR15119](https://github.com/QwenLM/qwen-code/pull/15119)，merge`14:07:47Z`：Session-local MCP settings revision改变server选择，AgentDefinition/Skills/approval policy仍pinned；exact published revision+digest从原Runtime private inventory选，不给browser executable recipe/credential；unknown operation保留identity先query/resume，不先开另一change。active Turn拒绝mutation，管理reattach不触发cold recovery，跨session迟结果丢弃。完整core/risk已读，不把普通daemon管理当同一执行环境。另[PR15198](https://github.com/QwenLM/qwen-code/pull/15198)测试给出Harness-private midcall热换边界：新rev连接在旁边建立、旧pending drain才close，不能把public active-turn拒绝mutation误写成public可热改。
- [PR14986](https://github.com/QwenLM/qwen-code/pull/14986)，merge`14:42:11Z`：Mod root的host/worker双账本只在trusted bridge确认guest idle时排除native执行/审批等待，guest jobs/continuations/log observer仍charge，attempt不刷新预算；root/phase identity拒旧activity，cancellation watchdog独立，且process cleanup可晚于watchdog。修复cancel真实result配对与/clear跨异步persist旧chat写回；完整core/risk已读。作者真实native wait fixture+fake model，非线上或Windows/Linux验收。
- [PR15053](https://github.com/QwenLM/qwen-code/pull/15053)，merge`13:09:35Z`：Anthropic global cache scope在所有baseURL默认opt-in，保session caching。旧native自动global scope在2tools请求形状造成scope ordering rejection；修复删除nativeURL隐式启用。原body明确精确接受规则比一行复杂，不证明所有mixed shapes永不可用，不采“命中率提升”。unit只验证2tools outgoing wire shape，作者未live API重放，escape hatch原mixed shape仍可能被strict backend拒绝。纠错触发受影响域深入，暂不泛化厂商规范。
- [PR15069](https://github.com/QwenLM/qwen-code/pull/15069)，Oct22合入：scheduled fire前模型外执行shell gate；empty+0 quiet无model turn/queue/transcript，输出作为data附prompt，failure/timeout首报后计数；一task gate串行，delete/disable/stop abort late delivery。创建时审批不等于执行时授权，旧cron_create allow不覆盖shell，durable写legacy condition作旧binary failclosed fuse。完整core/why/testplan已读；managed automation不走该scheduler，不外推。潜在owner Ch81，与空poll lease不同。

家族拟2+2+2=6；按每项真实新增与owner差异逐项Books处置，不能以“Qwen主题已经覆盖”统一关。

### O6 MiMo-Code 空输出retry与context rebuild边界

[PR2703](https://github.com/XiaomiMiMo/MiMo-Code/pull/2703) merge`2026-10-22T13:43:54Z`，[PR2702](https://github.com/XiaomiMiMo/MiMo-Code/pull/2702) merge`01:46:14Z`。完整core、测试、risk已读。PR2703把empty/think-only输出转persistent server retry，不再15min unknown budget；retry part记录attempt/phase/scope/kind/hostCode/next，跨reload/failure保留直到turn真实success，永不送model。new accepted input可supersede正在失败step，竞速sleep/backoff/hanging attempt；产出任一reason/text/toolinput即不再failing，compaction/max-mode不supersede。成本是每次重发全context；只有user cancel结束无限empty，keepalive byte仍可无限撑住single attempt，不能把persist retry当可靠终止/免计费。

PR2702 correction：checkpoint rebuild boundary从writer watermark后改为最新message后；boundary处读取真实tail、末尾未答user完整复制含metadata/files，已接纳未投递inbox保存deferredInputs以后放boundary之后；legacy boundary仍兼容collapse，runloop恢复tail但model只看window，完成reply后rebuild不再多发model request。具体输入/工具结果不得因context压缩静默丢失，不声称lossless任意语义压缩。拟2+2+2=6，correctness深入受影响域；作者整套并发tests有多处预存timeout，不写全套绿。

### O7 OpenAgentCore sandbox checkpoint recovery / journal

[PR819](https://github.com/MiniMax-AI/OpenAgentCore/pull/819) merge`2026-10-22T11:04:25Z`：missing/damaged/qualification/helper-format失败若native restore尚未dispatch，adapter先durably close exact admission再返回ErrCheckpointUnusable，ObserveOnly复见同结果；native dispatch后绝不能返回此结果。Core same compute_revision立即ExpireUnusableCheckpoint进入普通清理/已有cold replacement，非所有unconfirmed都强制新建；其他predispatch transient failure只close让new op重试。完整问题/机制/边界/检查已读，局部helper/go tests不冒部署。

[PR816](https://github.com/MiniMax-AI/OpenAgentCore/pull/816) merge`2026-10-21T21:08:58Z`即Oct22 BJT：以native snapshot closure作为checkpoint代替每次export zstd/hash/import；SDK同FS hardlink否则synced copy，adapter验证、ownership receipt、stop source再SourceStopped；resume验证一次直接restore；删除先tombstone且不open damaged snapshot。代价retention约0.5GB vs0.15GB/fullcopy sharedroot，作者mx旧timing2.73/5.85sec只旧开销，post-change realcluster timing仍in progress，不能宣称已测加速。必要PR815 workspace storage约束待定点读。拟2+2+2=6。

[PR817](https://github.com/MiniMax-AI/OpenAgentCore/pull/817) merge`08:56:44Z`：PGjsonb拒NUL导致整个event batch被拒，Harness已完成而Turn变persistence failed；journal normalization所有string/key U+0000→U+FFFD，错误只记session/turn/ordinal/count不记可能带raw提交值的driver error。具体event encoding可破坏execution/outcome投影，lossy规范化需显式而不是宣称byte-preserving。完整core/tests已读，细小实现但真实正确性反例保留，待独核准入。

## 后批必要源与实际 owner 比较 / PRE 待批

14项精确PR身份、SHA、公开created/merge原字段与官方完整核心原件摘存见[ORG_PR_ORIGINALS.md](ORG_PR_ORIGINALS.md)。API后续files请求触发匿名rate-limit 403；未丢弃此前有效原件。后由first-party GitHub fetch恢复固定版本及files；不是缺必要材料的终态保留。必要patch/spec见[ORG_SOURCE_EXTRACTS.md](ORG_SOURCE_EXTRACTS.md)，必要完整contract原件见[ORG_CONTRACT_ORIGINALS.md](ORG_CONTRACT_ORIGINALS.md)。不要求全repo code或本地复现；下列采用只到公开contract/所读patch实际支持的边界。

### O4 必要源 / Ch77 PRE

固定[SDK data-plane migration contract](https://github.com/Tencent-Hunyuan/Hy-Memory/blob/26c33ee40fbbfa9ca7b2be09c01356629b2b75de/memhub/docs/contracts/sdk-data-plane-migration-v1.md)已通过raw恢复并完整阅读。§1 marker前legacy authority、后SDK-only；§3 SDK-only保留/divergent隔离/unknown SDK outcome；§5 exact raw导入不走add重提取；§6 full bundle包含管理与SDK所有stores且isolated restore验证，不支持remote snapshot即block；§7 staging两rename再marker、failedcommit还原root与restart恢复；§8普通queue一job一次SDKcall、unknown问outcome；§10无partial cutover；§11 SDK-only写入后binary-only rollback禁止。§13 matrix是作者验收要求，不冒全matrix已本地复现。

实际Ch77:125–135已解释typed transaction不自动提供ACID，却没覆盖App/SDK重复authority及离线原件迁移不能重提取；Ch77:78–99原写入gate保持，Ch84仍owner runtime lifecycle。拟在Ch77 ACID限制段后新增：

当记忆从应用自有账本迁入独立 SDK 时，接口改名还不够：迁移必须先冻结普通写入，将 raw 原件的 exact import 与会重新提取、调和的 `add()` 分开，并以显式 cutover marker 选择唯一 authority，而不是运行期双读双写。[Hy-Memory 的固定迁移合同](https://github.com/Tencent-Hunyuan/Hy-Memory/blob/26c33ee40fbbfa9ca7b2be09c01356629b2b75de/memhub/docs/contracts/sdk-data-plane-migration-v1.md)保留 SDK-only 记录、隔离分歧，在完整管理/SDK bundle 经恢复验证后切换；已调用 SDK 但 outcome 不明的 job 先按原 request ID 查询，不能靠队列重试再提取。staging、切换恢复、完整备份与双边兼容都有成本；一旦新 authority 已接纳独有写入，只换回旧 binary 不会回滚数据。该合同不证明所有存储后端或真实故障均已验收；无法完成 inventory、restore 验证或分歧对账时，继续保留旧 authority 并阻止部分切换。<!-- source-family:SF-2026-HYMEMORY-SDK-AUTHORITY -->

PR143防回灌可用已有覆盖判断：实际Ch77:1824的immutable episode/provenance、derived rule不反盖其证据与1783评分/写回分离已承载“不把derived再当原始事实”的长期边界；该PR以reserved injectedblock剥离+read-only provider落实，属于具体对接证据，拟仅报告，不新增通用框架。prefetch过期/ID去重本次不外推为质量或授权保证。

### O5 / O6 Context commit联合 PRE

固定[Managed compression contract](https://github.com/QwenLM/qwen-code/blob/d03b3116dae52589210a50f84ac099876f75326c/docs/design/2026-10-22-managed-context-compression.md)已raw完整读，必要Admission/Execution/Recovery包含candidate→PostCompact→atomic terminal、unknown hook reconcile、compactionRevision独立contextRevision、usage unknown规则及retry纯summary计费反侧。actualCh75:389–395只有watermark/background proposal/fidelity/comparecommit及新增tail原则，未把hook和durable maintenance终态分开；MiMo2702新增把tail归属落实到boundary位置/accepted未delivered input。拟Ch75该source marker后、drift段前：

可恢复 compaction 还必须区别摘要候选、Hook 执行和 canonical history 的提交。先持久化候选，才能在中断后沿原 operation 继续后续 Hook 与提交；未知 Hook 结果要查询原证据，不能像纯摘要一样重新生成后再执行。[Qwen Code 的固定合同](https://github.com/QwenLM/qwen-code/blob/d03b3116dae52589210a50f84ac099876f75326c/docs/design/2026-10-22-managed-context-compression.md)将 compaction 与 terminal maintenance outcome 原子登记，保留原 audit transcript；纯摘要可能重复计费，但不能因此重复提交历史。窗口边界也不能只沿旧 writer watermark 放置：[MiMo 的 rebuild 修复](https://github.com/XiaomiMiMo/MiMo-Code/pull/2702)把 boundary 放在最新消息之后，并将已接受但未投递的输入另列 deferred state，避免 tail 反复进入窗口或用户输入被摘要截断。这增加候选持久化、revision、tail 与恢复配对成本；原件可低成本完整驻留时，简单同步压缩仍合理。公开合同与局部回归不证明摘要语义无损、任意 Hook 可重试或所有并发部署安全；输入配对或 operation 证据缺失时保持 blocked、回读原文，不把一次压缩完成签成下一任务正确。<!-- source-family:SF-2026-QWEN-CODE-DURABLE-COMPACTION;SF-2026-MIMO-CODE-2702 -->

### O7 必要contract / Ch84 PRE

PR819 files API在rate-limit前已成功读取`docs/sandbox-provider.md`精确patch（recovery/cold replacement部分）和`contracts/agents-api/node-generation-protocol.md`wirecode变更。必要新增证据明文：snapshot missing/integrity/qualification失败时，只在fresh attempt native dispatch之前durably close+fence，ObserveOnly稳定回同outcome；native dispatch后unknown仍不能授权replay。coldreplace仍需ordinary expiry cleanup、filesystem ready、initialization complete、Session/Environment非terminal、前次authenticatedRuntime的retained_native_history，resource deletion confirmed后释放，外部TCP/effect不因此恢复。实际Ch84:697–699已有compute incarnation absence/cleanup/retainedSession资格，缺“checkpoint本身不可用但旧dispatch未发生”这条合法结束retention分支。拟该段后：

已确认 compute 可清理，也不代表 retained checkpoint 仍可恢复；反过来，checkpoint 损坏不能把已发出的 restore 当作没发生。[OpenAgentCore 的固定修复](https://github.com/MiniMax-AI/OpenAgentCore/pull/819)只在 adapter 证明原 attempt 尚未 native dispatch、并已持久关闭和 fence 该 operation 时返回 `checkpoint_unusable`，使同一 compute revision 走正常到期清理，合资格 Session 再 cold-replace；dispatch 之后的 unknown 继续保留原 target 与 ownership，不因超时自动新建。这把可重试的 pre-dispatch failure、不可用 snapshot 和 outcome 未知分开，代价是更多 provider outcome、持久 admission 和清理对账；native-history 或 exact cleanup 证据不足时仍应阻塞或人工恢复，不能由新实例可启动证明旧副作用已结算。<!-- source-family:SF-2026-OPENAGENTCORE-819 -->

O7 PR816本次拟仅报告：native snapshot替压缩archive是具体storage/latency工作点而非新的联合恢复原则，actualCh81:670–672已具体说明process/filesystem/environment联合身份及snapshot/storage与restore成本交换；保0.5GB vs0.15GB作者近似和posttiming未完，不出Books性能结论。PR817编码归一化拟仅报告：U+0000→U+FFFD是API明示有损兼容规则，不提升journal为原始byte authority，无新可迁移长期机制，不借安全日志原则抬分。

### O5 execution budget / schedule与MCP配置 PRE

必要源追加：[ORG_SOURCE_EXTRACTS](ORG_SOURCE_EXTRACTS.md)保存已读PR14986完整host/worker/ModBudget patch和PR15119具体68行新contract。14986关键`ModBudget.pause/resume`累积扣时，worker `updateActivity`要求native operation存在且无executing/checks/guestNotifications/pendingJobs/non-lending livecalls；host再核root/phase/revision/nativeoperation并独立维持abort watchdog。不是worker自称“我在等”就免计费。MCP配置contract明确requested/physical config/catalog三态分离；restart先release receipt后configure receipt，inventory不是health。actualCh83:108已拆config来源/连接执行者/动作执行者，但未解释同Session config revision与physicalreceipt，拟仅追加最小段（不重写原五维契约）：

同一 Session 内改变 MCP 选择，还要把 requested settings、实际连接与 catalog 投影分开版本化：保留原 AgentDefinition、Skills 和审批 policy，显式配置命令只推进 Session-local revision，并沿原 Runtime 对账。[Qwen Code 的固定管理合同](https://github.com/QwenLM/qwen-code/blob/4ee2bb4e4744c2f688401eb4f00cf5791bd1e9eb/docs/design/2026-10-22-managed-session-mcp-management.md)要求 restart 先取得旧连接 release receipt，再取得新 configuration receipt；refresh catalog 不能代替这两项证据。unknown 原命令保留 identity、阻塞冲突变更，read-only 管理查询也不应隐式唤醒 cold Session。额外 revision、receipt 和 owner 绑定增加维护成本；简单固定目录仍可保留，无法核对原操作时拒绝变更，而不是在另一 daemon 或 Runtime 重做。该合同不证明任意客户端、执行环境或已在途 tool 的安全热切换。<!-- source-family:SF-2026-QWEN-CODE-MCP-MANAGEMENT -->

actualCh84:626–628 resource域只有cgroup memory预算，没有将guest执行计时与native等待分开。拟此段后：

插件执行预算还应区别 guest 计算与宿主等待：把一次长工具或审批等待全算作插件运行，容易在插件空闲时错误终止；无条件暂停预算又允许 guest jobs 隐藏计算。[Qwen Code 的固定修复](https://github.com/QwenLM/qwen-code/pull/14986)由 host 与 worker 共同核对 root、phase、当前 native operation 和 guest-idle 证据，只有这类等待才暂停累计扣时，新的 attempt 不刷新余额；取消 watchdog 仍独立。双边计时与过期消息处理增加协议成本，unknown 状态应保守计费；watchdog 结束也不证明 native process 已清理，原生 timeout、真实结果配对和副作用收尾仍须单独验收。局部假 provider/真实子进程测试不构成线上、跨平台或严格终止时限保证。<!-- source-family:SF-2026-QWEN-CODE-MOD-BUDGET -->

PR15069必要[固定gate design](https://github.com/QwenLM/qwen-code/blob/74c67c9e94f09b80b5f47df8f8ab216c9ebe6a14/docs/design/2026-10-21-scheduled-task-gate.md)经GitHub fetch完整核心§1/4–11及§12风险已读，明确§11只有PR1a落地，daemon form/probes/managedautomation仍提案，不把整个design当实现。actualCh81 timer横线1174与durableinput954只有唤醒/重驱未有模型外quietgate，拟timer横线段前：

周期任务的 tick 不必直接变成 model Turn。无 webhook 的本地环境仍需轮询，但可先在模型外运行受授权 probe：成功且无变化便安静结束，有事件才把输出作为数据交给 Agent，失败则保留可见原因而不假装零事件。[Qwen Code 的固定 gate 切片](https://github.com/QwenLM/qwen-code/pull/15069)在 scheduler 统一入口串行执行每任务 probe，取消、停用或删除后丢弃晚到结果，并在执行时重新核权限；创建定时提示的 allow 不是任意无人值守 shell 权限。这样减少空 model 调用，却增加 probe cursor、重叠时隙跳过与权限漂移成本；输出仍可能恶意，quiet 也不证明全局没有变化。probe 无法可靠检查、状态不可重放或权限不足时，保留较低频人工检查、明确失败或原简单定时路径；该版本不代表后续 daemon 表单、专用 watcher 或 Managed automation 已交付。<!-- source-family:SF-2026-QWEN-CODE-SCHEDULE-GATE -->

PR15053 cache纠错本次拟仅报告：主要是beta API mixed-scope形状兼容性且精确接受规则原作者也未定，本地只pin two-tool request，无法变成通用cache-prefix定律；不把旧global hitrate夸张保留，不把no-live验证当修复未实现。已读精确files：anthropicContentGenerator.ts的useGlobalCacheScope从nativeURL或flag改为仅flag=true，enableCacheControl=false仍先return false；converter行为本身未新增global普适语义，只改注释说明。PR15131 cancellation-admission→settlement具体边界已有actualCh84:508–510新执行/旧key收尾及697–699exactwriter不明不replacement；此事件作为受限实现证据仅报告，不能泛称其全部UI/跨层已覆盖或全测试通过。其真实Native settled判定仍在必要Source中保留，不因NC省略反证。

### O6 persistent retry PRE

已通过first-party GitHub fetch恢复并完整读固定`empty-output-persistent-retry.md`与`retry-record-part.md`，后者及rebuild spec保存ORG_SOURCE_EXTRACTS。还读固定`packages/cli/src/session/retry.ts` defaults/resolve/budgetFor/decide：ContextOverflow/Abort/Auth先terminal，InvalidOutput分类server，candidate/judge仍own bounded，network/server持久budget；实际触发replaySafe/no toolparts前提由spec指向processor，不宣称所有有副作用失败可重放。spec明确后台actor未必有status UI，waitForWriterSettlement超时只结束等待不取消writer，keepalive不算有效输出，fullcontext重复计费。

actualCh84:596–598已有拒绝优先、可见输出前后与bounded retry，不含持久retry记录和新的输入控制权。拟该段后：

空输出也不能只靠“当前 busy”判断恢复进度。[MiMo-Code 的固定分支](https://github.com/XiaomiMiMo/MiMo-Code/pull/2703)把合资格的 empty/think-only step 放入持久 server retry，并将 attempt、phase 和原因保存为不进入模型上下文的 retry part；开始新 stream 不清记录，只有真实 turn success 才清，取消或失败继续保留。较新的已受理输入可以打断仍无输出的失败 step，使用户不被无限重试堵住；已有工具副作用、compaction 与 max-mode 等分支不能据此任意透明重放。无次数/墙钟上限以更多可用性换来重复发送全 context 的持续费用，keepalive 仍可能撑住单次无内容请求；后台等待超时也不等 writer 已停。短任务或可预测费用要求下保留有界重试，缺少 replay-safe 与当前输入 identity 时停止/升级，而不把持久重试签成必然恢复或物理终止保证。<!-- source-family:SF-2026-MIMO-CODE-2703 -->

## 代表性排除与补充边界

- MiniApp Oct22 CN公告与Agent techblog Oct20同名核心相同：miniapp.json、Node持久服务、托管MCP、Agent API、Host Connector、审批与宿主凭证均已出现，没有明确Oct22机制变更，不以传播再计新贡献；reader已经独立双正文、目录日期分组及actualCh84校准通过。
- ZCode API窗内8commits中marketplace game/3D分组、Unity redacted例子镜像、Blender官方MCP替换、Godot接入、LibTV CLI skill、license-review skill目前属于工具接入/分类/写作流程，未见改变模型/系统设计判断的增量，不因主题词Agent入选。
- ZCode `352563fdabcf42b5a899029080cb639d1f6df116` Oct22移除context/context-insight两个插件（marketplace和81files删除）。已核删除事实，没有撤回论文/漏洞/用户数据保证理由；不采用被删除artifact正面主张，不凭withdraw字样猜安全事故，reader已独核该处置。
- Hunyuan AuK README最新明确News Oct14蒸馏pipeline，原稿2609.08936；Precise原稿2605.23522、News Sep26；OmniCapBench2610.12458，repo说明Sept开源。Oct22 updated不是新论文依据；具体新commit若只维护不重审旧稿。
- Hunyuan DiagSafe两README统计修复：`041bc5ac42de`/`9b7fc486b541`把“各judge始终>93%”改成“>89%”，原表89.41–95.34%未变；236 human-annotated responses作为gold的分母不能丢。论文2610.29225已arxiv切片准入，本修复同family不加候选数，纠错cue已交arxiv作者和root；不得用95.34%最高值替代跨judge下界。
- PR815已读完整核心：microsandbox移除provider-owned disk、强制external workspace storage；缺storage报409 workspace_storage_required，retained_native_history未声明的mcode被拒，wire protocol7。该具体支持/compatibility限定约束O7，不把Docker/E2B独立disk路径同改。OAC812/813已完整核心读取，分别并行preflight+signal替poll、初始化期间避免free-slot suspend阻塞；是节点局部启动优化，所列7/4次mx计时不形成新普适机制/生产SLO，本窗排贡献保留导航，不扩大工程源队列。
- 来源有限收尾以§来源有限收尾为准，不再有未执行扫描；只保Google pubs、Meta Research/Publications、Qwen新Blog具名目录差额。后批普通Source/Books/独核仍按实际推进，未预签日级验收。
