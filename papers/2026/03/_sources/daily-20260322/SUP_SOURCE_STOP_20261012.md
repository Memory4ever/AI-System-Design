# 03/22 来源补充有限停点

执行：2026-10-12，北京时间。作者 supp_mar22，仅 own 本日 README 与本日 sources。补充窗口：2026-03-21 ～ 2026-03-21；原 03/21T09→03/22T09 窗口、原0候选及连续§4冻结于 [原README](./SUP_ORIGINAL_README_20261012.md)。本轮重读 AGENTS、当前研究/报告合同、来源使用说明/Daily/arXiv路由、Prompt、ROADMAP，LS只作路由。旧完成不授本轮DAY，不读旧Weekly，不写共享Books/LS/索引，不stage/commit/push。

## 1. 有限来源与复用边界

原身份/日期/查询与停止依据明确复用 [本日V3有限来源](./V3_FINITE_DISCOVERY_STOP.md)，其旧小时窗裁决不复用。只把原日期邻接对齐03/21自然日；具体新恢复如下。目录原字段不是完整题摘/全文队列，没有全机构无遗漏声明。

| 来源 | 本轮有限检查、日期对齐与停止 | 结果/限制 |
| --- | --- | --- |
| SRC-OPENAI | 定点复用[实际RSS1242条原字段](../daily-20260321/V3_PUBLIC_DIRECTORY_FIELDS.json)：邻接两条Mar19GMT，转换BJT仍Mar19，无03/21条；不重读两正文 | 限该RSS可见历史，非全机构 |
| SRC-ANTHROPIC | 定点复用[原Sanity March9记录](../daily-20260317/V3_WORKING_STOPPOINT.md)：Mar13T10:15Z→Mar23T23Z及24/31，BJT没有03/21；不以Research当前latest10代历史 | 限原Research可见字段，不外推News/delete |
| SRC-GOOGLE-AI | 本轮实际Google March archive206行，page1十二卡Mar17→24跨自然日，无03/21；page2复用[真实2/2两卡](../daily-20260305/V3_OFFICIAL_RECOVERY_12.md)Mar6/4。DeepMind原page3二十四卡与6March原header均窗外。Pubs本轮621行1–15/11612、2026年406；只Year/Title排序，无day过滤 | Blog有限闭合；Pubs03/21主题原发历史slice保留，不扫406/全年 |
| SRC-META-AI | 本轮Research仍0行；真实Publication入口本轮433行恢复首20卡，近期Oct/Sep/Jul十项后混2019/2020/2018等旧记录，非日期单调，有Next；停止第一页，不把可读误称不可达。Blog原1/2共22卡Mar11→26/27，无03/21 | Publication本窗dated slice未恢复，不沿旧故障或泛化20卡证明零 |
| SRC-QWEN | 定点复用真实API40条metadata，额外实际投影March两行03/19T04+08 MaxPreview、03/30T04+08 Omni，无03/21；只有articles，无total/分页 | 限40 display字段，不授first-public/删除历史 |
| SRC-DEEPSEEK | 定点读[原Next posts16及Research完整g数组](../daily-20260317/V3_WORKING_STOPPOINT.md)：NewsApr24/Sep10，ResearchFeb25→Jun24，无March行；不把render10/5当全部 | 隐藏公开数组已恢复，不留假目录故障 |
| SRC-MOONSHOT | 原Kimi/en/blog19卡，Feb9→Apr20跨自然日，无03/21字段；不以旧platform止2025否认2026历史 | 限19卡，不扩GitHub/releases |
| SRC-TENCENT-HUNYUAN | 定点复用[publicList zh原11/11字段](../daily-20260321/V3_HUNYUAN_FIELDS.json)，page1/size20/renderType0/code0；displayFeb13→Apr23，无03/21 | publishedAt/display/update不互换，不授删除历史 |
| SRC-ZAI | 原Research15卡Mar15→Apr1、原releaseNotesFeb12→Apr7，无03/21；停止原可见列表，不扩ViewMore | 不授所有机构历史 |
| SRC-BYTEDANCE-SEED | 本轮Research仍5Blog/10精选；正确x-tt-locale:US的type1/year2026/token20/count100/order_descfalse实际18/82,next40,true，Mar20FlexTrain→Mar21 Mixed→Mar23/24/25/26。type2/year2026/token0/count100/orderfalse实际14/19,next空,false，Feb16→Apr1无03/21。新原字段见[Seed JSON](./SUP_SEED_DIRECTORY_FIELDS_20261012.json) | Mixed必要first-public语义未证；Blog未返5项仍具体保留。仅Accept-Language:en-US返回14/82及9/23属locale切片，不以其当完整或新故障 |
| SRC-BAIDU-ERNIE | 原zh Blog10卡，Feb6→Apr15跨03/21；停page1，next旧页不扩 | 限10卡，非全机构 |
| SRC-XIAOMI-MIMO | 原首页Paper8 Mar13→Jun29，Blog15undated；定点读[原正确Pro/Omni字段](../daily-20260320/V3_WORKING_STOPPOINT.md)，本轮正确两页再GET200、21963/45615字符，均time datetime2026-03-18，无03/21。正确正文不是/blog壳 | 两正文已可恢复、不重复请求；只03/21 datedBlog历史slice保留 |
| SRC-MINIMAX | 原EN12/CN13主Blog，Mar18→Apr27/May26无03/21；本轮AgentTech真实66行三卡日期09/19、09/22、10/08；本轮.md GET200、1570字符亦同三卡，不再说仅heading/880B May列表 | 当前文档变化不反填March历史；只03/21 AgentTech历史datedslice保留，不扩guide/三窗外正文 |
| SRC-ARXIV | 实际重新读availability170–199，Fri/Sat Eastern无常规公告；03/21 BJT在Fri20→Sat20 Eastern之间。四主题按补充日对应SubmittedUTC03/20T16→03/21T15:59，start0/max25/ascending实际25/60、25/41、9/9、25/58；[完整参数/停止](./SUP_ARXIV_QUERY_STOP_20261012.json)。仅元数据邻接/标题查漏，跨主题重合不相加，不追剩余页 | Submitted/Updated非公开；没有84题摘/全文队列、没有84本窗新家族。缺特殊公告/作者原发本窗历史slice，不因周末声称互联网零研究 |

本輪必要公开日期只核到日，不恢复旧09:00门、不以ID月份/DOIcreated反推公发。旧本日合法monthly cs.CL1–25/2138仅月首标题范围，不重读整月；旧10附件和legacy库存不成新候选队列。按需来源无新增触发，未扫描Weekly/全会议；Seed具名恢复辅助查询仅exact-title/Mixed官方域/author-project三组，没有可靠新的官方原发日期，索引/转载不充当原证。

## 2. MixedDimKV 完整题摘与必要日期裁定

本轮实际读 [2603.20616v1](https://arxiv.org/abs/2603.20616v1) 题名、完整摘要L16–18、7作者及唯一v1 historyL26；无当前可见撤回/纠错header，未扩全版本史。完整题摘原文在[本日旧PRIMARY](./V3_PRIMARY_ADMISSION.md)可复用，本轮同identity确认。Seed完整AB也实际读于新JSON，仅确认身份/潜在贡献，不采用摘要数字。

原有whole-token eviction把预算设为零或全维 → MixedDimKV按token分配混合维数、H版same-head importance对照 → 潜在改变KV压缩粒度与质量/容量选择。两入口中属现有主线的具体增量，potential owner INFER-KV-CACHE；不是只因KV主题或可映射章节保留。

旧小时窗曾要求Seed日级范围全落09–24；本轮不继承这一门。Seed PublishDate1774022400000是03/21日级字段，整天归属的精度够用，**但语义仍不证明正文首次公开**：Journal=arXiv、ContentType0、唯一ExternalLink是unversioned arXiv PDF、ArticleID1776932180702/UpdateTime1776932185000为后续目录元数据，未恢复独立作者原稿公发。

官方v1 history只给Submitted03/21；availability说明arXiv ID不能提前分配，通常Sat提交最早03/24 BJT公告，不能把目录03/21或Submitted当first-public。没有因为日期缺失否定贡献，亦未称已经处理的重复事件。

root于2026-10-12作为非准备者实际独读exact-v1完整题摘/7作者/history，并成功取得DataCite官方version1：Submitted2026-03-21T03:21:43Z、Updated2026-03-24T00:25:29Z、created/registered2026-03-24T03:25:54/55Z、Available仅March、findable。其裁定：潜在贡献准入层与日期隔离有限PASS；这些登记字段不证明03/21正文公开，不能直接候选/评分/Books，不授摘要数字或Source效果。请求一次可靠作者原发公开日+对应稿版本，或具公开语义的Seed原note/正文。当前没有另一个已知必要官方入口，不扩全作者/仓库或读实验绕日期门。

## 3. 实际处置与精确停点

原0候选不变，补充确定新增0，确定候选证据0/0，Books新增0；未申请共享写锁、未改Books，不以No Change主张已有覆盖。Mixed必要日期与六来源历史slice（GooglePubs、MetaPublication、SeedBlog差额、MiMoBlog、MiniMaxAgentTech、arXiv非常规/作者原发切片）被精确隔离，不支持正面证据/Books/无遗漏。恢复只重开03/21该身份/来源，不扩其他Daily或Weekly。

普通待办：0。root作为非报告作者实际读README六部分、本停点、四query完整参数停止及Seed原18/82、14/19字段与Mixed身份，核14每日组、未扫Weekly、metadata非题摘/全文、六来源与Mixed精确终态及Books0依据，最终本轮DAY有限PASS。旧有效AB/date有限裁复用而非旧DAY标签；本作者未自签。完成态V3、原窗口与连续§4冻结、25本地引用、2新JSON解析及限定cached/unstaged diff-check实际PASS；Snapshot保持原文，链接按原README位置解释。没有长工具或共享写锁，结束本日，不启动03/23、不改LS。
