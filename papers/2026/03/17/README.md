# Daily Research — 2026-03-17

**规范：** V3
**窗口：** 2026-03-16T09:00:00+08:00 ～ 2026-03-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T02:31:27+08:00

## 1. 结论

本日14源完成有限入口处理，但部分历史目录与23个潜在家族的首公开日期不能精确落窗，已隔离而非认作零命中。确定候选0、证据审阅完成0、Books新增0；这不表示23项没有贡献，也不授Coverage或Evidence正面通过。22篇arXiv完整exact-v1题摘及Cognitive官方核心/必要PDF协议用于贡献准入，不能当正文证据完成。

主题API的49/49、50/310、40/139、40/80是窗口邻接Submitted线索，不是当天新论文或全量筛选分母；月表与旧1405宽库存不成逐项队列。旧报告完整保存在[原报告](../_sources/daily-20260317/V3_LEGACY_REPORT.md)，未继承30候选、评分、NoChange或EffectiveDate。本日普通待办0，root非作者日级Gate通过；精确原值和实际停止见[唯一停点](../_sources/daily-20260317/V3_WORKING_STOPPOINT.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS解析1242项，只提Mar15–17邻接4条；compensation GMT Mar17T00（BJT08）核心已读、贡献前关闭；SAST Mar16GMT00在左界前，mini/nano与Japan teen Mar17GMT10在右界后，不称已审重复 | 已检查 | 无；仅RSS有限切片 |
| SRC-ANTHROPIC | Research web58行及HTML March publishedOn/title实际9条，Mar31→Mar23→Mar13→Mar6/5，跨窗无Mar16–17行 | 已检查 | 不外推全News历史 |
| SRC-GOOGLE-AI | Research MarchBlog页1实际12条，页2原始2条metadata独立对窗；DeepMindNews页3实际24卡片/6March；Cognitive Blog/必要PDF读到；pubs实际1–15/11569、2026筛选372 | 受阻 | D18精确事件日期；H1 pubs本窗历史切片；科学/临床应用不通过Evaluation重新引入 |
| SRC-META-AI | Blog页1/2实际10+12非时间排序卡片跨窗；Research实际0行 | 受阻 | H2 Research本窗publication切片；22Blog不授全机构覆盖 |
| SRC-QWEN | 实际只读article/retrieval返回40条extra.date/title，Mar19/30与Feb16跨窗，无本窗可见行 | 已检查 | 无本次普通可恢复gap；接口无exposed total/pagination，不外推40条之外 |
| SRC-DEEPSEEK | News39行、HTML实际恢复posts16；观察到的9467B Next脚本恢复Research数组最新Jun24→Feb25/Jan28/Jan12，跨窗；隐藏News已解除 | 已检查 | 仅实际目录切片，不授全机构历史无遗漏 |
| SRC-MOONSHOT | KimiBlog19卡片Jul→Apr20→Feb9；AttnRes触发官方repo身份4commits/API created/push/public/releases0定点核 | 受阻 | D7论文/项目firstpublic；repo创建/commit不是公开证明 |
| SRC-TENCENT-HUNYUAN | 观察到的只读publicList renderType0/page1/size20实际totalNum11/11，原publishedAt/display两字段对窗，无March | 已检查 | 两字段角色分开，不互当首公开，不授全机构覆盖 |
| SRC-ZAI | Research15条与发布说明165行可见章节Mar15→Apr1、Feb12→Apr7跨窗；有限停止 | 已检查 | 不外推ViewMore全部历史 |
| SRC-BYTEDANCE-SEED | type1/token20实际14/total82、next40/hasmore，Feb27→Mar16MoDA→Mar26；type2/count20/token0实际9/total23、next20/hasmore，Feb→Apr跨窗，仅当前可见段；完整MoDA题摘读到 | 受阻 | D6官网日级published=1773590400000非firstpublic；H5 Blog未返回身份/日期差额，不授全部Blog覆盖，不扩82条库存 |
| SRC-BAIDU-ERNIE | Blog页1实际10卡片，May→Apr→Feb→2025Nov，停页1（Next2/2旧切片） | 已检查 | 不授全部GitHub/机构历史 |
| SRC-XIAOMI-MIMO | 首页Paper8/无日期Blog15，实际脚本恢复V2Pro/Omni原路由，两原页web失败、curl仅JS壳；Paper Mar13→Feb3 | 受阻 | H3两具名原Blog核心/日期及本窗dated archive，不把无日期15条当零命中 |
| SRC-MINIMAX | Blog12卡片Mar18→Feb14跨窗；AgentTechBlog15行仅标题、llms.txt48行只有guide索引 | 受阻 | H4本窗AgentTechBlog dated切片；不扩guide站 |
| SRC-ARXIV | 合法cs.DC show250恢复月表1–250/346元数据及15042membership，cs.LG首250及skip1750恢复月份元数据；有界标题查漏来自四主题API实际49/49、50/310、40/139、40/80；潜在22篇完整v1题摘及原history/23家族日期隔离见§5 | 受阻 | D1–17、D19–23首公开日期；show200为非法参数不是合法日档故障；月表无日级header，未全审月标题 |

API SubmittedDate限定Mar13–16邻接范围以发现周末队列；四组分别为系统/GPU运行时、模型与Agent状态、基础多模态/WorldModel/VLA、训练优化/缓存/RL，分类与准确查询/停止原值在唯一停点。辅助搜索限定同主题/Mar16，未拓展其他月份或每周源。官方时间为20EDT→次日08BJT，不误用EST09。

## 3. 候选与判断

确定当窗候选0。23潜在家族有具体贡献理由、尚不能确定首公开落窗，列§5而非候选表；未评分，不把摘要数字、作者权威或访问状态计入三维分数。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

没有确定候选进入Evidence Gate，无Books写入或已有覆盖声明。Cognitive的same instructions/tools、逐faculty人群分布percentile评价protocol有潜在规范增量，不能以缺新实证拒绝；只采用其准入理由，不声称验证AGI。Anole摘要拟常规组合关闭经必要§II-B/IV核心纠正：因果token顺序、单forward连续actionchunk和两阶段velocity/acceleration监督保留潜在机制；混合原论文baseline不支持matched归因。

贡献前具名关闭：compensation核心L23–32属于薪酬领域使用/局部WorkerBench吻合，没有本项目新训练、执行或评价成立条件；Google FCV当前完整摘要及2510.17862v1完整题摘/history指向2025既有公开研究，later ACL record未识别本窗新事件或安全机制，未否定原安全贡献；MER-Bench15020v1完整题摘的新meme任务/四维MLLMjudge分解未提供新有效性、噪声/预算或归因条件。Google superconductivity/clinical screening为本项目暂缓科学/临床应用。前三项root实际窄核通过，余范围分层样本仅作者记录；排除项不评分，不为不影响处置的日期另开请求。

## 5. 缺口与下一步

普通待办0，独立日级Gate通过。以下是本窗终态保留项，不用于正面证据、不进入Books，不支持覆盖/无遗漏、性能或安全保证。每家族只请求一次，原值/准入命题与定点重开身份集中在[唯一停点日期表](../_sources/daily-20260317/V3_WORKING_STOPPOINT.md)。

- D1–17：14745 CAMD、15042 DetShare、15125 MEMFLOW、13289 RelayCaching、13319 LightningRL、15619 MoDA、15031 AttnRes、15589 LEXI、15530 DUET、14633 ScannerLie、14851 AutoMoT、14972 TakeVLA、15618 DeepVision、13606 NCCLEP、15202 LMetric、15183 TokenCoherence、15699 Time/EnergyProxy。完整v1题摘有具体潜在贡献，DataCite exact原created上界分别在Mar17BJT11–12或Mar18BJT10；Updated不等公开正文。缺原始announcement batch/正文已可取时间，不能组合schedule伪造08公开。需exact-v1首次公开timestamp或完全落窗区间，或作者稿原first-public metadata，定点重开各ID/date，不成深审队列。D6可由Seed原firstpublic字段、D7可由repo真实first-public记录替代（create/commit不够）；D9/D17接受原venue全文公开记录而非acceptedcomment。
- D18：Cognitive Framework原PDF封面Mar16只有日级，仍不能确认正文首公开归属。后续定点恢复官方Blog的JSON-LD `datePublished`与`meta name=published_time`均为`2026-03-17T16:00:00+00:00`，即BJT03/18零点，已在本17窗外；root实际curl380460B核同值。此字段不反填此前PDF首公开，也不以Blog重述重新计家族。只需该PDF原始发行时刻/时区或封闭落窗范围，恢复后审必要protocol，不追全Google站。
- D19–23：13435 CtrlAttack、15417 TTRL Amplification、13026 PISmith、13782 NavigationHeads、15046 AnoleVLA。完整题摘/历史实际核；前4的exactDOI批查、Anole单查原created=Mar17T04:29:32.000Z/registered04:29:33.000Z/v1Updated02:06:07Z，均不定正文公开。PISmithcreated=Mar16T01:55:56Z，可能公告下界Mar16BJT08跨左界，其余Mar17T03:51–04:38Z跨右界。具体安全/设计反证潜在贡献保留，不授防护或rollback安全保证。需各exact-v1原firstpublic记录，重开相应identity/date，不合并为已审安全证据。
- H1：Google pubs current1–15/11569、2026筛选372不能恢复本窗相关历史切片；需官方date-bounded导出或历史分页定位，仅重开Mar16–17pubs。
- H2：Meta Research实际0行，有限22Blog不能替代；需本窗官方research publication切片，重开Research入口。
- H3：MiMo已观察 `/blog/mimo-v2-pro`、`/blog/mimo-v2-omni` 两原页只有JS壳且无date字段；需可读官方核心/日期和本窗dated archive，只重开这两个入口/本窗列表，不将未知More全部队列化。
- H4：MiniMax AgentTechBlog只有标题/无本窗dated archive；需本窗官方dated快照，重开techblog入口，保留12Blog有限停止，不扩其他guides。
- H5：Seed type2/count20/token0原始9返回/total23、next20/has_more=true只有当前可见段；未返回身份/日期不能支持本窗无遗漏。需官方本窗Blog切片或该返回/分页差额的解释，定点重开type2本窗，不继承其他日count100的14/19，不无限分页。

窗外恢复线索：OpenAI SAST位于左界前，mini/nano与JapanBlueprint位于右界后，未在本日审为duplicate；四主题查询中Mon16T18Z之后提交的条目最早常规Mar18BJT08，不进入本窗深审，若有独立提前作者稿记录只重开对应身份，不扩本日。日期外部隔离不代表潜在贡献被排除或Coverage/Evidence正面通过。

## 6. 复核

复核者：root（非作者；分批准入与本次整日日级Gate实际执行）。

结论：通过

root实际完整exact-v1题摘/history首5（14745/15042/15125/13289/13319）及后7（15031/15589/15530/14633/14851/14972/15618）准入方向通过；Cognitive Blog L255–283和PDF p1摘要/§3 p4–5实际窄核促成上述纠正。root实际compensation核心、Google FCV完整摘要与2025v1身份/安全信号、MER-Bench15020v1完整题摘/history通过贡献前关闭，三项覆盖应用范围、旧安全事件身份及benchmark贡献理由。root本次完整读正式六部分和唯一停点，核窗口、14源有限停止、全部23身份/日期保留、H1–5恢复条件及普通0，通过安全终态。没有复核全部23家族全文；其余10家族仅核作者记录的具体身份/日期隔离而非完整题摘/实验，宽API/旧1405全库及范围层样本未授全量负侧或Evidence通过。

作者机器检查：V3 validator通过（0候选空表header补齐后）、本日限定diff-check通过、本地引用通过；旧报告SHA256与HEAD原报告均为665eb719bd651e938383fcded300e7644966687cc968cb9a9ac511482d2bde97，完整保留。完成同步后重跑机器检查；机器检查不替代语义日Gate。未写Books/LS/索引，不stage/commit/push。
