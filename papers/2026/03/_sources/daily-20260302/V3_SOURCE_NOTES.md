# 2026-03-02 V3 有限来源停点与筛选记录

窗口：2026-03-01T09:00:00+08:00 ～ 2026-03-02T09:00:00+08:00（含左不含右）。
运行：2026-10-01，作者 mar02_v3。采用当前 V3；原 V2.1 报告只作[保留快照](./V3_LEGACY_REPORT.md)，旧 raw、inventory 与 EffectiveDate/完成标签不授本轮候选或 Coverage。没有读取 Weekly 或扫描每周来源；没有把年度/月度宽列表逐项变成审阅队列。

这是人工可复查的入口、实际停止范围与判断记录，不是另一份完成收据。当前入口并非历史不变快照，所有“目录无项”仅指下述可见段落，不保证删除过的事件不存在。正式判断见[本日报告](../../02/README.md)。

## 1. 每日14源实际访问与停点

### SRC-OPENAI

访问 [Research](https://openai.com/research/)、[Research Index](https://openai.com/research/index/)、[News Research](https://openai.com/news/research/)；可读 Index 只给当前条目和 Load more，没有恢复到03/01～02的历史cursor。直接Index请求403，返回约9768字节错误内容，不当研究材料。

官方域补检：
- `site:openai.com "March 1, 2026" research`：出现社区/非目标条目，不授覆盖；
- `site:openai.com/index "March 1, 2026" -site:community.openai.com`：没有可核目标；
- 目标03/02同类定点搜索没有确定事件。

停止：历史cursor不可恢复。准确替代需求是该时段Research目录归档或有日期/时区的原始发布记录；不把当前空检写为历史零研究。

### SRC-ANTHROPIC

[Research](https://www.anthropic.com/research)渲染页停于当前条目与 See more；直接HTTP200页面约316674字节，嵌入Publications列表内提取 `publishedOn` 日期段，而不是只看首页。目标相邻：
- An update on our model deprecation commitments for Claude Opus 3：2026-02-25T20:02:00.000Z；
- Labor market impacts of AI：2026-03-05T19:59:21.508Z。

该可读目录段没有03/01～02事件。本窗有限已检查；未扩看相邻窗外正文，未声称全机构所有事件覆盖。

### SRC-GOOGLE-AI

[DeepMind Blog p3](https://deepmind.google/blog/page/3/)实际可见May～Feb2026目标段；相邻Nano Banana2在02月、Gemini3.1 Flash-Lite在03月，点击[Flash-Lite原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)确认Mar03,2026，不落窗。[Nano Banana2原文](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)只使用已见02月归属，不声称已核具体首次时刻。

[Google Research 2026/03](https://research.google/blog/2026/03/)p1实际Mar31→Mar6，页末两页导航；点击第二页及有依据的恢复请求均InternalError，未恢复03/01～05。[Publications](https://research.google/pubs/)2026仅年粒度372项，不当全天/首公开凭证，也不把372篇变成全文队列。

停止：月目录p2、相关研究精确首公开记录。接受该页归档或原文带时区日期；没有确定正文线索时不无限扩搜。

### SRC-META-AI

[Research](https://ai.meta.com/research/)实际0行。限定官方域03/01～02补检只给非目标/当前页面，没有恢复原历史Research条目。停止：该目标段历史目录或原始发布记录。空响应与搜索无确定项不证明无事件。

### SRC-QWEN

旧[Blog](https://qwenlm.github.io/)公告迁移到qwen.ai，旧列表最新2025年，不用于2026无项。[新Blog](https://qwen.ai/blog)动态页渲染0行，直接HTTP200约92469字节未给可用历史日期cursor。

[Qwen3.5官方repo](https://github.com/QwenLM/Qwen3.5)当前路由重定向到Qwen3.8，但README保留news：03/02小尺寸9B/4B/2B/0.8B；02/24中等尺寸；02/16首个397B。读取[0.8B card](https://huggingface.co/Qwen/Qwen3.5-0.8B)、[9B card](https://huggingface.co/Qwen/Qwen3.5-9B)完整核心说明、配置与评价段，不以型号或标题准入。

贡献前关闭：本次材料是家族机制下的尺寸扩展；核心hybrid attention、早期多模态融合与后训练没有新的尺寸特有机制/可比资源—质量边界。0.8B具体配置为dense FFN，24层、6×(3 GDN+1 gated attention)、hidden1024、FFN3584；通用Highlights仍写sparse-MoE，不能据此扩大该小尺寸贡献。标准scoreboard没有建立一个足以修正本项目设计选择的受控资源/质量条件。不是“小模型一律无价值”。

root首批准入校准批准上述明确贡献排除。仅日期03/02未核时区/时刻，但日期不会改变处置，故不另立该release日期请求。新Blog历史目录仍为独立来源限制，不把一项关闭冒充全目录无项。

### SRC-DEEPSEEK

[Research & News](https://www.deepseek.com/en/news/)最终直接恢复，Research Index10项至2025/05/14；目标相邻02/25 DualPath→06/24 DeepSeek-V4，没有本窗目录项。News首页5项相邻2025/12/01→2026/04/24，View All未展开，不授隐藏News分页覆盖。另实际读[Updates](https://api-docs.deepseek.com/updates)。渲染Updates失败后直接请求HTTP200约47922字节，读实际Change Log标题段；目标相邻为2025-12-01 V3.2/Speciale、2026-04-24 V4。该公开变更日志段没有本窗条目。不重读明显窗外模型正文。

### SRC-MOONSHOT

[Kimi Blog](https://platform.kimi.com/blog)实际完整可见109行，最新2025/11/07，列表至2024/05/29，没有2026历史段。官方域定点：
`site:platform.kimi.com "2026年03月01日" OR "2026年03月02日"` 无可核记录。
该旧入口停止点后来已解决：root给出真实可恢复[Kimi Research Blog](https://www.kimi.com/en/blog/)，作者随后也独立直接打开155行，19项列至2024/06/26 Mooncake，目标相邻2026/02/09 Agent Swarm→2026/04/20 Kimi K2.6，页面没有可见未完成分页。相邻整日期明确远离本窗，不补09:00或首次时刻。可见Research列表无本窗项，不宣称全机构历史完整；不再请求必要2026目录。

### SRC-TENCENT-HUNYUAN

首查[Research](https://hunyuan.tencent.com/research)0行。子代理三次浏览器恢复分别超时、visibility不支持、超时，及时停止并转交root。root也遇到UI超时，后从该页面实际脚本发现并只读调用publicList，没有猜测另一套接口。

已读取root保留的[官方目录原值](../V3_HUNYUAN_LIST_RECOVERY.md)。`renderType=0,pageNum=1,pageSize=20` 为页面“全部”分支，返回code0、total11并确实11项。对本窗重核：
- 100015 Stabilizing RLVR...，display与published均1770971794 = 2026-02-13T16:36:34+08；
- 100061 Hy3 preview，display1776873600 = 2026-04-23T00:00+08，而published1782308557 = 2026-06-24T21:42:37+08。
- 其余所列原值也没有03月。

当前公开目录全页已读完，目标相邻02/13→04/23无本窗条目。两字段不能互当首公开，不能推断从未删除研究/全机构历史无遗漏。不用GitHub updated替代公开时刻。原始抓取由root完成；本日只读对窗确认，不继承其他日报结论。

### SRC-ZAI

首查[Research全部](https://www.zhipuai.cn/zh/research)，可读175行时间排序。相邻2026/02/21 GLM5报告→03/15 GLM5Turbo，没有本窗目录事件。当前公开目录段有限已检查，未扩看窗外全文。

### SRC-BYTEDANCE-SEED

[Research](https://seed.bytedance.com/en/research)可读当前spotlight，不是历史全集；[Public papers](https://seed.bytedance.com/en/public_papers)实际p1，1–20/242、13页，条目Aug18→May14。Next page为动态控制，未取得目标历史页。
定点 `site:seed.bytedance.com "Mar 1, 2026" OR "Mar 2, 2026"` 未给可核记录。
停止：目标历史页或带时间原始发布；p1不证明本窗无项，242项不成为逐项队列。旧replay里的零命中标签不继承。

### SRC-BAIDU-ERNIE

[Blog](https://ernie.baidu.com/blog/zh/)当前可读列表跨越目标段：02/06 ERNIE5→04/15 ERNIE-Image，本窗无目录条目。Publication入口直接HTTP200但未提供可用精确日期，未授所有Publication覆盖。有限已检查仅对可见研究Blog段成立。

### SRC-XIAOMI-MIMO

[主页Paper/Blog](https://mimo.xiaomi.com/)可读Paper区相邻02/03 HySparse→03/13 ARL-Tangram，没有本窗Paper。Blog当前15个标题无日期与历史cursor。官方域03/01～02补检没有可核记录。
停止：Blog目标历史日期目录/原文带时区首公开。Paper无项不授Blog无项。

### SRC-MINIMAX

[英文Blog](https://www.minimax.io/blog)、[中文Blog](https://www.minimaxi.com/blog)当前可读历史跨越目标，03/18 M2.7前项为02月Forge；英文02/14，中文02/12，二者都明确远离本窗，不为不影响归属的差异扩开日期审阅。
[Agent TechBlog](https://agent.minimax.io/docs/techblog)只是当前壳；[llms.txt](https://agent.minimax.io/docs/llms.txt)约48行，只列当前Agent Team路径，无历史日期。主Blog可见段有限已检查，TechBlog历史能力受限，需求是目标目录归档/带时间原文；不外推全站零发布。不采用旧raw公司业绩负样本作本轮已核研究结论。

### SRC-ARXIV

首先核[官方availability](https://info.arxiv.org/help/availability.html)：常规公告Sunday～Thursday；Friday/Saturday不公告；Thursday14EST～Friday14EST队列Sunday20EST发布，Friday14EST～Monday14EST队列Monday20EST发布。标识/DOI在announcement处理时分配，月份属首次公告，而非Submitted。2026官方假期表无03/01特殊假期。

本窗对应2026/02/28 20EST→03/01 20EST（后者不含）。March身份的最早常规公告Sunday03/01 20EST就在右端，因此4个2603身份不能凭Submitted March1成为本日线索或日期缺口。只得常规新增0批，不指定每篇具体批次，不以DataCite注册+日程伪造首公开时间。独立更早作者/project公开需有具体原文信号，本轮未取得，不泛泛请求所有March论文日期。

[cs.DC March月列表](https://arxiv.org/list/cs.DC/2026-03?show=2000)实际约2898行，只有月级作者/标题列表，没有可用逐日公告批次；只用身份查漏，不逐项全文。旧式 `/list/cs.DC/260302` 与 `/list/cs.CL/260301` 请求InternalError，不因失败抹去官方零常规批边界。

四组辅助搜索均限定 `site:arxiv.org`、`after:2026-02-28 before:2026-03-02`：
- LLM OR language model OR Transformer；
- GPU OR LLM inference OR distributed training OR kernel；
- multimodal OR world model OR VLA OR diffusion；
- agent OR RAG OR memory retrieval。

搜索范围不是发布时间筛选器。仅出现的四个身份全部读精确v1完整题摘，结果如下（只作窗外入口，不算当窗初筛/审阅/Books）：

| 精确身份 | 原始Submitted UTC | 阅读与准入消歧 |
| --- | --- | --- |
| [Tiny-Critic RAG 2603.00846v1](https://arxiv.org/abs/2603.00846v1) | 2026-03-01T00:16:31Z | 完整题摘：小critic的LoRA、约束解码/非thinking二值routing，潜在生成器/评判器成本解耦；未采用性能数字 |
| [MC-Search 2603.00873v1](https://arxiv.org/abs/2603.00873v1) | 2026-03-01T02:25:57Z | 完整题摘：hop级模态/证据链、HAVE归因与过程评价、SearchAlign process-SFT；不因benchmark名称自动准入 |
| [Semantic XPath 2603.01160v1](https://arxiv.org/abs/2603.01160v1) | 2026-03-01T15:56:08Z | 完整题摘：树memory寻址与更新；没有采用176.7%/9.1%摘要收益 |
| [TARSE 2603.01241v1](https://arxiv.org/abs/2603.01241v1) | 2026-03-01T19:31:23Z | 完整题摘并[HTML](https://arxiv.org/html/2603.01241v1)§3～5、§7.2/A.1：retrieved经验适配→provisional chain→step-aware技能检索验证；数学与联合适配使其不能仅因medical标题早退，但尚未Evidence审阅 |

最初工作稿把四条作为本日日期保留项，root纠正“月份+公告右端”后已移出，不继续追本窗不存在的常规首公告缺口。没有把潜在贡献或完整摘要读完当审阅完成。精确页面未见撤回/删除标记，仅是这些页面的轻量观察，未检完整版本史/代码。

## 2. 准入与具名分层抽检入口

本窗确定且通过贡献筛选家族0；四个2603窗外身份不评分。没有必要Books写回，也没有“已有覆盖”的书稿claim，因此没有伪造owner对读。

已请求并获得root对Qwen小尺寸贡献前关闭的首批准入校准。可供非作者复核的明确样本，按来源/主题/理由分层：
- 型号增量/机制不新：Qwen3.5-0.8B与9B官方cards同一小尺寸release家族（贡献前关闭，日期不改变处置）。
- 官方目录明确窗外：Anthropic Opus3 deprecation更新02/25与Labor market impacts03/05；Google Flash-Lite03/03；DeepSeek DualPath02/25与V4报告06/24；Moonshot Agent Swarm02/09与K2.6 04/20；ZAI GLM5report02/21与GLM5Turbo03/15；混元RLVR clipping02/13和Hy3preview显示04/23；ERNIE5 02/06与ERNIE-Image04/15；MiMo HySparse02/03与ARL-Tangram03/13；MiniMax Forge02月与M2.7 03/18。这些只是目录/日期分层样本，未阅读全部窗外正文、未做贡献排除。
- arXiv身份/时窗边界：上述四个2603精确v1，依据月份与常规公告日程排除本窗常规首公告，而非依据search date/Submitted。

独立复核仍须自己确认这些理由、来源停止范围及未检查范围。根协调的03/04准入校准是另一项受托只读任务，未写本日候选，也不从其他日报继承评分/结论。

## 3. 限制与精确重开

本窗外部保留项：OpenAI历史cursor、Meta历史Research、Google月目录p2/相关论文首公开、Qwen新Blog历史日期、Seed目标历史页、MiMo Blog历史日期、MiniMax TechBlog历史日期。每源只请求该目标片段或官方归档/当时公告/有时区正文；材料返回仅定点重开其源/身份，不扫整月或整年。没有独立日期/正文线索时不推测有多少漏项。

窗外四篇在真实归属日期若触发再处理，不阻塞本日；没有自动扩日或写Books。所有外部限制不支持“零研究/全站无遗漏/性能安全保证”。当前日需要root非作者Gate，不自行Complete。

## 4. 本地变更边界

作者只修改本日README及V3_LEGACY_REPORT、V3_SOURCE_NOTES；未删除旧raw，未写Books、LEARNING_STATE、索引、其他日报。根协调共享混元原始记录只读引用。未stage/commit/push。机器校验见日报§6，格式不替代语义验收。
