# 03-16 补充窗有限来源停止 — 2026-10-11

作者：supp_mar16。补充仅北京时间 2026-03-15 ～ 2026-03-15；原窗口/1候选/评分/连续§4冻结，不由旧完成标签代替本补查。

检查时间：2026-10-11T09:36～09:43+08:00。原文正文与原始字段位置分别保存；重复抓取只用于修正字段投影（Seed sub_article_list/ArticleMeta、Qwen extra.date），没有扩机构历年论文。

| 来源 | 实际范围/停止 | 原证位置与限制 |
| --- | --- | --- |
| SRC-OPENAI | 重新解析官方RSS1287项，UTC[03-14T16Z,03-15T16Z)0；相邻SAST为03-16BJT，保留原候选不重复 | SUP_METADATA_QWEN_ANTHROPIC_OPENAI_20261011.jsonl |
| SRC-ANTHROPIC | Research新HTML177publishedOn字段，全部March字段邻接03-13T10:15Z→03-23T23Z，不落03-15日 | SUP_METADATA_QWEN_ANTHROPIC_OPENAI_20261011.jsonl |
| SRC-GOOGLE-AI | March Blog筛选web不可达/curl20秒timeout；旧12cards/DeepMind6March primary日期有效复用；Pub当前641line只到首15、year2026显示406非日窗且filtertimeout，03-15限定补搜未恢复dated主题slice | SUP_WEB_FIRST_0/1_20261011.txt、SUP_WEB_CORE/REMAINING_20261011.txt；V3_SOURCE_STOPPOINT中的具体日期字段 |
| SRC-META-AI | Research当前0line；Blog当前p1/p2与旧相关March日期复用，p2实际March11MTIA→March27SAM3.1，停止Next；Research03-15主题historyslice未恢复 | SUP_WEB_FIRST_0/1_20261011.txt、SUP_WEB_CORE/REMAINING_20261011.txt；V3_SOURCE_STOPPOINT中的具体日期字段 |
| SRC-QWEN | 公共API新40/40 title/path/extraDate+embeddedpublished全部对读，无pagination字段；近Feb16→Mar19，日期冲突不落03-15，不改旧归属 | SUP_METADATA_QWEN_ANTHROPIC_OPENAI_20261011.jsonl |
| SRC-DEEPSEEK | 当前News页面109774B+可见5日期；仅已观察页面脚本9449B恢复Research日期数组，Feb25DualPath→Jun24V4；旧News16日期原值有效复用，有限目录不落03-15 | SUP_METADATA_DEEPSEEK_MINIMAX_20261011.jsonl；SUP_WEB_CORE_20261011.txt |
| SRC-MOONSHOT | 当前Research19/19完整日期至2024Mooncake，Feb9AgentSwarm→Apr20K2.6，无可见待分页 | SUP_WEB_FIRST_0/1_20261011.txt、SUP_WEB_CORE/REMAINING_20261011.txt；V3_SOURCE_STOPPOINT中的具体日期字段 |
| SRC-TENCENT-HUNYUAN | 首查Research当前0line，已观察publicList page1/size20/renderType0英文9/total9；旧中文11原值补齐locale差异，相关Feb3/13→Apr23/May1；两日期字段不证明first-public | SUP_METADATA_SEED_HUNYUAN_20261011.jsonl |
| SRC-ZAI | 首查Research当前15time-sort可见cards，03-15Turbo位于Feb21→Apr1；Turbo完整core16–115贡献前关闭，承认L48题库/轨迹公开声明但此页未披露改变判断的协议 | SUP_WEB_CORE_20261011.txt L16–115；SUP_LOCAL_DIRECTORY_FIELDS_20261011.md Z.ai段 |
| SRC-BYTEDANCE-SEED | 当前type1/token20返回18/82,next40跨Feb25→Mar26；1414完整AB是量子多体科学范围关闭，MoDA官网Mar16窗外；type2/token0返回14/total19,next空/has_morefalse，Feb16→Apr1，差额5隔离 | SUP_METADATA_SEED_HUNYUAN_20261011.jsonl |
| SRC-BAIDU-ERNIE | 当前zhBlog68line的完整10cards至Nov2025，Feb6→Apr15；页2/2旧更早日期有效复用，停止 | SUP_WEB_FIRST_0/1_20261011.txt、SUP_WEB_CORE/REMAINING_20261011.txt；V3_SOURCE_STOPPOINT中的具体日期字段 |
| SRC-XIAOMI-MIMO | 当前Paper8/8全日期与Blog15无日期/More，Mar13Tangram→Jun29MOPD；旧已观察runtimefallback复用，不给nondatedBlog授03-15零命中 | SUP_LOCAL_DIRECTORY_FIELDS_20261011.md MiMo L112–295局部；V3_SOURCE_STOPPOINT具体fallback边界 |
| SRC-MINIMAX | 当前EN12/ZH13cards跨Feb14/12Forge→Mar18M2.7；AgentTech当前220249B仅3datedSep19/Sep22/Oct8条，不能推出03-15历史slice完整 | SUP_METADATA_DEEPSEEK_MINIMAX_20261011.jsonl；SUP_WEB_CORE_20261011.txt |
| SRC-ARXIV | 当前官方availability §Schedule+§ID已读：BJT03-15无常规新公告；旧28actualSubmitted/registered日期下界>=03-16，不搬归属/不深审；03-15题义有界补搜未恢复异常公告slice，旧宽列表不变队列 | 官方availability；V3_FIRST/SECOND_DATE_PACKET、V3_CMAG_DATE_PACKET；SUP_BOUNDED_SEARCH_20261011.txt |

## 本次明确筛选

本次新增0候选，不给具名EX评分。准入/范围层具名2材料：GLM-5-Turbo（完整core）、Seed1414/2603.14425（完整official AB）；日期层不是机制拒绝：SAST原事件03-16、MoDA官网显示03-16与arxiv更晚、旧28 arxiv常规下界>=03-16。首批准入已经review_mar15_16实际独核；原28更早独立作者首稿不被arxiv日程排除，仍按具体身份/真实日恢复。本次不追精确时刻、90日catchup、全月DataCite库存或全版本。

## Z.ai当前有限Research日期投影

2026/08/26 GLM5.3Flash；08/14GLM5.3；06/16GLM5.2；05/20ZCube；04/29ScalingPain；04/07GLM5.1；04/01GLM5VTurbo；03/15GLM5Turbo；02/21GLM5report；02/11GLM5；02/02GLMOCR；01/19GLM4.7Flash；01/13HuaweiMultimodal；2025/12/10GLMTTS；12/09GLMASRNano。查看更多停止。来源 https://www.zhipuai.cn/zh/research ，本次curl1097253B，日期是目录显示，不补授时区或first-public。Turbo具名原证是research/155，完整core在SUP_WEB_CORE。

## Google/DeepMind本次原始访问边界

https://research.google/blog/?m=3&y=2026 web不可达且curl20秒timeout；https://research.google/pubs/?year=2026 curl20秒timeout。https://research.google/pubs/ web成功641line，显示2026=406，当前首15不是历史datedslice，停止；不逐项审阅这些不同年份命中。DeepMind现page3curl197417B，文本没有March卡片，不能当历史零命中；旧同身份March primary日期值复用仅证明已知6事件窗外。GooglePub所缺的03-15主题历史slice保留，不因成功取得全年目录而撤销。受阻不是不适用。

## arXiv必要日期依据与异常边界

本次实际读 https://info.arxiv.org/help/availability.html 的 §§Availability、ID assignments、Announcement Schedule、Deferred Mailings。官方常规公告Sunday→Thursday Eastern；Thursday14→Friday14收件于Sunday20公告。03-15BJT星期日不含正常新公告；28已知Submitted在Thu14后，不能把Submitted重命名为公开日。ID在公告分配的说明提供该arxiv事件常规下界，不证明独立作者原稿更早没有出现。

仅定点补搜 `site:arxiv.org ("15 Mar 2026" OR "Sun, 15 Mar") (language model OR transformer OR inference OR agent)`；联合机构日期查询见SUP_BOUNDED_SEARCH。搜索返回年度GooglePub与旧STaR等非日窗，未形成新候选或逐项队列，也不证明历史异常/更正/重要revision没有发生。当前无具名新异常信号。需要官方03-15BJT异常公告相关段/具名当时primary才能重开受影响项。

## 终态外部保留项

GooglePub03-15主题datedslice、MetaResearch03-15主题slice、SeedBlog返回14/total19的5差额、MiMoBlog03-15datedslice、MiniMaxAgentTech03-15历史slice，以及arxiv异常公告/重要revision历史主题段：现有原始入口、观测fallback与一次窗口补搜已有限尝试，不授无遗漏，不支持新增候选/Evidence/Books。材料到达只重开对应source/window或具名ID。非作者review_mar15_16实际完整六部分、14源停止与必要分层原证DAY通过，详见SUP_INDEPENDENT_REVIEW_20261011.md；普通扫描/筛选/必要候选Evidence/Books/独核待办0。不改Books/LS/索引，不stage/commit/push。

