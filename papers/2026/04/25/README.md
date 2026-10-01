# Daily Research — 2026-04-25

**规范：** V3
**窗口：** 2026-04-24T09:00:00+08:00 ～ 2026-04-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-28T06:31:40+08:00

## 1. 结论

本窗没有 arXiv 常规公告批次，不能把旧 DataCite `created` 零库存解释为全来源零研究。十四个每日来源已恢复可见目录的本窗停点或精确限制；OpenAI News 的职业转型文章虽在窗内，却只讨论经济与职业任务，不是本项目当前模型/基础设施机制，因而在贡献分母之前关闭。

[Kimi CLI 1.39.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0) 的官方 release 于04/24 14:22:19北京时间落窗。一个release family包含两条须区分的设计边界：源 Tool schema 与某后端wire投影分责，补足缺失`type`不自动证明语义等价；默认自动发现模式下的同名Skill优先级改变实际加载哪份定义，不只是目录显示顺序。对 pinned tag 与必要PR/代码定点审阅后评2+2+2=6；Ch84的Skill身份/Agent definition窄增量已实际写入并通过[非作者写后复核](../_sources/daily-20260425/V3_ROOT_KIMI_139_WRITE_AFTER.md)。此处没有运行完整测试、复现用户调用或测量性能；单篇Books通过不等于本日报完成。release 中其他局部修复不各自扩为候选。

DeepSeek V4 Preview 官方公开页与 API 更新日志只写04/24自然日，尚不能证明首次公开在本窗09:00起点之后；现存六月 technical report 也不能倒灌成四月证据。它是本窗相交日期的保留线索，不评分、不用于 Books。本窗最终冻结1个贡献候选、1个具名贡献前关闭、1个精确日期隔离；必要 Books 新增1处实际正文且写后通过。[旧报告](../_sources/daily-20260425/V2_1_README_BEFORE_V3.md)已原样保存，[本轮来源与必要证据](../_sources/daily-20260425/V3_REVIEW_CHECKPOINT.md)及[非作者整日Gate](../_sources/daily-20260425/V3_ROOT_DAILY_GATE_20260425.md)保留有界依据，不继承旧 V2.1 “Complete”。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本次实际检查[News RSS](https://openai.com/news/rss.xml)1230项邻近日期，04/23T10Z、11Z两项窗前；[Modeling an AI jobs transition](https://openai.com/index/modeling-ai-jobs-transition/) published04/25T00Z落本窗，实际读核心后因职业/经济分析无当前模型系统机制而贡献前关闭 | 受阻 | News RSS 不替代 Research/Publication 历史目录；需可复核本窗原始列表/停点，不能把RSS闭合作全来源零遗漏 |
| SRC-ANTHROPIC | 本次[Research](https://www.anthropic.com/research)HTML 的 `publishedOn` 邻界04/22T14:12:30.673Z/14:27:03.434Z→04/29T20:26Z，目录无本窗列项 | 已检查 | 仅可见官网 Research 目录，不涵盖所有未列作者稿 |
| SRC-GOOGLE-AI | 本次 Google Research April Blog九条相邻04/22→04/29、DeepMind Blog page2/3标题及[Decoupled DiLoCo](https://deepmind.google/blog/decoupled-diloco/)原文04/23与[Korea partnership](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)04/27，均非本窗 | 受阻 | Google Publications 历史日窗目录尚无有界停点；Blog 不代论文入口 |
| SRC-META-AI | 复用[04/19实际来源停点](../_sources/daily-20260419/V3_REVIEW_CHECKPOINT.md)：Research空提取、Blog混排04/08/06→03/27，Publication入口无可核本窗列表 | 受阻 | 空响应/混排旧项不证明无更新；需官方历史分页或当窗原始条目 |
| SRC-QWEN | 本次官方[动态目录API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项，04/22T10+08→04/28T10+08→04/30T12+08跨窗；静态60旧项早于2026的实际核验复用 | 已检查 | 可见 Research 目录无本窗项，不等全部作者稿 |
| SRC-DEEPSEEK | 实际打开[News/Research](https://www.deepseek.com/en/news/)、[V4 Preview](https://deepseek.com/en/news/v4-preview/)与[API更新日志](https://api-docs.deepseek.com/updates/)04/24段；V4只给日级公开日期，Research technical report 当前列06/24 | 受阻 | 04/24无可核时区/时刻，和本窗仅相交；该具体事件日期隔离，不据六月报告正面采用或写成本窗零命中 |
| SRC-MOONSHOT | 本次Kimi CLI官方[release](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0)目录100项：1.38.0 04/22T16:26:17Z→1.39.0 04/24T06:22:19Z→1.40.0 04/28T13:51:04Z。实际读当窗release及pinned必要代码/测试；旧 PR 创建/合并日与本 release 事件分开 | 受阻 | Kimi Platform Blog 历史2026段未闭合；release 不能替代官网 Blog 全覆盖。机构入口受限已隔离；单篇候选已获非作者写前/写后复核 |
| SRC-TENCENT-HUNYUAN | 复用[04/19官方目录记录](../_sources/daily-20260419/V3_REVIEW_CHECKPOINT.md)：研究页“全部”POST publicList `pageNum=1,pageSize=100,renderType=0`，`totalNum=9,list=9`，04/30/23→02/13跨本窗 | 已检查 | 只说明公开可见“全部列表”无本窗项，不声称所有未列论文被检查 |
| SRC-ZAI | 复用[04/19已读官方入口](../_sources/daily-20260419/V3_REVIEW_CHECKPOINT.md)：Research15项04/29→04/07→04/01，release notes06/16→04/07→02/12，仓库创建目录跨窗 | 已检查 | 列表日期不自行视作时区明确的精确公开钟；可见目录无当窗列项 |
| SRC-BYTEDANCE-SEED | 本次官方 `get_article_list_v2`、`x-tt-locale:US`；paper `article_type=1,page_token=20,count=20`实返20/total242/next40，05/12T16Z→04/08T16Z，邻近04/25T16Z在本窗后、04/22T16Z在前。Blog type2 page0实返15/total95/next20，04/22T16Z→04/08T16Z；page20实返18、首2025/12/17，已经低于本窗停止 | 已检查 | `PublishDate` 是目录字段，不重定外链论文 first-public；有下一页不表示需要无界扫完全部242/95条 |
| SRC-BAIDU-ERNIE | 复用[04/19实际 Blog 停点](../_sources/daily-20260419/V3_REVIEW_CHECKPOINT.md)：10条04/30→04/15→02/06→2025，已跨本窗 | 已检查 | 仅技术 Blog 的可见目录，不把同公司全部研究当已查 |
| SRC-XIAOMI-MIMO | 复用[04/19官方首页停点](../_sources/daily-20260419/V3_REVIEW_CHECKPOINT.md)：Paper8项06/29→03/13→02/03跨本窗；Blog14项缺可核历史发布日期 | 受阻 | Paper停点有效；Blog需原始时间/排序入口才可闭本窗 |
| SRC-MINIMAX | 本次 MiniMax-AI/cli官方release API26项，v1.0.11 04/17T20:51:17Z→v1.0.12 04/26T01:40:29Z，无本窗release；复用EN Blog05/26→03/18、CN04/27→03/18的实际跨窗列表 | 受阻 | Agent Tech Blog可见最早05/13，四月历史段未证；CLI无release不能推广为全机构无研究 |
| SRC-ARXIV | 实际读[官方公告与ID规则](https://info.arxiv.org/help/availability.html)：美东周日至周四20:00，周五/六无常规公告；本窗对应Fri04/24晚常规slot缺失，前一周四slot对应04/24 08:00早于起点。旧DOI created=0不作覆盖证据 | 已检查 | 仅排除常规公告批次；异常/非arXiv提前公开须由具体官方线索定点核，不声称全网没有论文 |

复用的是未变化的具体目录停点，不是继承04/19的完成结论。组织仓库仅定点核重要 release，不遍历普通 commits；本表的“已检查”都限定于对应可见入口。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi CLI 1.39.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0) | 2026-04-24T14:22:19+08:00 | 原始Tool schema与后端wire投影分责；默认自动发现模式下同名Skill优先级决定实际加载版本；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) Skill作用域解析与run身份，实际正文及非作者写后通过；Ch78兼容修复先仅报告 |

本表冻结1个确有落窗 release 身份和具体主线增量的贡献候选。OpenAI职业文章是范围外来源命中；DeepSeek 04/24日级公开不证明落在左闭右开本窗，均不评分或伪装零命中。Kimi同一家族的先前PR与本次正式release不是两篇候选。

## 4. 证据与知识整合

### [Kimi CLI 1.39.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.39.0)

官方tag的`published_at=2026-04-24T06:22:19Z`属于本窗。已读release列出的schema兼容、thinking.keep、项目skill覆盖及少量消息格式修复；它们在同一版本中发布，不意味着所有相关PR首次当日公开。必要源码定位为tag `1.39.0` 的 [`kimi.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/packages/kosong/src/kosong/chat_provider/kimi.py) `_convert_tool`、[`jsonschema.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/packages/kosong/src/kosong/utils/jsonschema.py) `ensure_property_types` 及[转换测试](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/packages/kosong/tests/test_kimi_tool_conversion.py)。这一路径为provider-facing schema建副本、递归补缺失`type`，源`Tool.parameters`不被转换函数原地改写；测试包含 enum-only、已有typed字段、输入未变和builtin工具分支。代码/测试已阅读，未执行测试或模拟真实provider调用。

关键取舍是 wire 格式被某后端接受、原工具输入schema保留、运行时实际参数语义与业务授权分别验收。`ensure_property_types` 从enum/const/结构推断，不可推断时默认`string`；混合型enum或组合schema可能被收窄，不能因此说所有合法输入保持等价，也不能把静态转换测试当本地执行器已按原schema完整校验的实测。发布说明未给兼容修复的失败率、性能、线上负载或端到端correctness。

同一release的[PR2044](https://github.com/MoonshotAI/kimi-cli/pull/2044)在本窗已合并；实际读取tag中的[`skill/__init__.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/skill/__init__.py)与[`config.py`](https://github.com/MoonshotAI/kimi-cli/blob/1.39.0/src/kimi_cli/config.py)：默认自动发现模式下，Skill root从扁平列表变成带`project/user/extra/builtin`来源的列表，同名首个匹配遵守`Project > User > Extra(config) > Extra(plugin) > Built-in`；显式`skills_dirs`会替代Project/User自动发现并居首。系统提示按scope分组，`merge_all_available_skills`默认false→true。相同Skill名称可能因此解析到另一份正文；目录发现、最终选择和模型看到的说明应共同版本化，不能拿仅显示路径代替真实加载版本。PR声称有多项测试，本次只读必要代码与说明、未运行测试，也不认为“project优先”本身是普遍安全策略：恶意/错误项目Skill同样可能遮盖builtin，effect权限仍由独立执行器决定。`thinking.keep`及[PR2028](https://github.com/MoonshotAI/kimi-cli/pull/2028)的`skip_yolo_prompt_injection`是其他局部行为线索；后者关闭的是yolo提示注入provider，不是自动批准工具的权限开关，不能冒充prompt-injection攻击防护或授权收紧。

2+2+2=6，因已有Ch84具体缺口作必要深入。实际[Ch78 Tool Contract](../../../../books/part-07-agent/78-tool-calling.md)已明确typed schema、后端含义不稳定、schema validation、authorization与effect-time分权；其wire投影修复暂仅作局部release证据。[Ch84 Skill registry/Agent definition](../../../../books/part-07-agent/84-agent-platform.md)原已要求Skill来源、版本、权限、activation与run身份，但未具体解释同名多scope优先级如何改变已加载定义、prompt呈现与版本化运行身份之间的关系。现已在这一主线中补入作用域解析/同名遮蔽/可信admission窄条件，保留static allowlist、手工pin版本及effect-time权限作为共存和回退，不推出该CLI已验证所有环境或能防御恶意Skill。该Books提案获[非作者源→actual owner写前校准](../_sources/daily-20260425/V3_APR01_KIMI_139_INDEPENDENT.md)，[实际正文写后复核](../_sources/daily-20260425/V3_ROOT_KIMI_139_WRITE_AFTER.md)也已通过；这是单篇整合，不替代本日来源/日期/分母的独立Gate。精确证据与未验边界见[审阅笔记](../_sources/daily-20260425/V3_REVIEW_CHECKPOINT.md)。

### 贡献前关闭与日期隔离

OpenAI的[职业转型原文](https://openai.com/index/modeling-ai-jobs-transition/)在窗内，研究任务自动化、劳动需求与经济过渡；当前 AI-System-Design 的大模型/Infra机制没有因此新增可定位设计选择，故不进入候选，也不以大机构名提升分数。DeepSeek的[V4 Preview](https://deepseek.com/en/news/v4-preview/)与[API更新日志](https://api-docs.deepseek.com/updates/)确有04/24日级发布线索和模型/API版本事实，但不能以不明时区自然日证明首次公开在04/24 09:00以后；现有官方Research技术报告列06/24，不能逆向当成本窗方法全文。只保存精确日期保留项，不将“百万context/DSA”等发布描述无条件导入Books。

### Books判断

Books流程在本次范围内，没有由旧零候选跳过。Kimi的Ch78兼容修复目前仅报告；Ch84作用域解析/版本身份窄gap已实际纳入正文，非作者写后复核已通过。该单篇Books判断完成，但不能代替本日来源/日期/分母Gate。

## 5. 缺口与下一步

普通可执行工作已为0：Kimi单项Books已实写且写后通过，十四来源复用范围/本窗日期、OpenAI负侧均经[非作者日级语义Gate](../_sources/daily-20260425/V3_ROOT_DAILY_GATE_20260425.md)有界核验。旧0候选/Complete不继承；以下外部缺口不是可执行待办，也不支持正面采用或全网无遗漏断言。

本窗外部保留项：OpenAI Research/Publication、Google Publications、Meta Research、Kimi Blog、MiMo Blog、MiniMax Agent Tech 的四月历史入口缺可验证本窗停点；各项需相应官方历史页、日期排序或本窗原始清单，届时只重开受影响源/材料。DeepSeek V4 Preview 只有04/24自然日，需官方时区及首次公开时刻、可核归属本窗的原始artifact，或等效早期公开依据；当前不评分、不用作正面Books/“无命中”证据。上述缺口不要求无界重抓，也不代表已经全网查无论文。旧221xx–230xx缓存与DOIcreated零库存是窗外/待归属线索，非本窗候选或完成证据。

这些均为终态保留项；定点重开条件是取得对应机构官方历史目录的本窗分页/日期停点，或 DeepSeek 当次带时区的首公开时刻与原始 artifact。隔离部分不用于正面证据、Books 或无遗漏断言；只复核因此受影响的来源与材料，不重跑无关候选。

## 6. 复核

复核者：root（非日报作者），[日级语义Gate记录](../_sources/daily-20260425/V3_ROOT_DAILY_GATE_20260425.md)。

结论：通过

这是有边界完成：root 独立逐行核 14 个来源的可见停点/精确限制、无常规 arXiv 公告的窗口依据、OpenAI 职业文章的贡献前关闭、DeepSeek 的相交日期隔离，以及 Kimi release 的公开身份、单篇必要证据、Ch84 写前与实际写后。最终1候选/1具名前关闭/1日期隔离，普通待办0；六个机构历史入口与 DeepSeek 日期仍按§5保留，不代表全网零遗漏或实验复现。结构校验、Markdown/链接及限定 diff 检查在终稿运行；它们不替代本次语义复核。不stage、commit、push。
