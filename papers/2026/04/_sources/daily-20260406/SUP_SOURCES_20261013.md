# 04-06 既有 Daily 来源遗漏补充：本日原记录与停点

作者：supp_apr06_author。补充窗口只有 **2026-04-05 ～ 2026-04-05（BJT）**。本次读取/定点恢复时间为2026-10-13 22:40～22:54+08:00；完整自然日用于公开归属，API分钟范围仅作提交元数据线索。

已完整重读AGENTS、当前RESEARCH_CONTRACT、REPORT_CONTRACTS、Prompt、ROADMAP；只加载来源说明、每日14源与arXiv路由。最新路由94/279是01-01～04-03及04-05，04-04仍进行中，不是连续94日。没有读取旧Weekly、扩扫每周源或继承04-05候选/Books判断。

原报告冻结：窗口`2026-04-05T09:00:00+08:00 ～ 2026-04-06T09:00:00+08:00`；47条原候选整行sha256 `b6cc0a981c17670272c5d77e58c4f720e271529246676a859cf289a779ce58c7`；连续原§4正文27656字符，sha256 `bab03aaf5b95f5dd196f6f51308b9a2933b5e8d52db60f26bada1095531dc3b8`。不移动原候选日期、不改原评分或连续正文。

## 原件复用边界与本日实际检查

以下`SUP_<id>_20261013.raw`与同名`.request.json`原件位于[04-05来源目录](../daily-20260405/)；请求实际执行于2026-10-13 20:45～20:48+08:00。它们是同一官方入口的当前索引原件，不是04-04事件快照。本作者实际读其日期、标题、分页、必要相关内容，并只投影04-05；不复用其他日报的完成标签、贡献筛选或证据结论。

| 来源 | 实际原件/入口与停点 | 本日判断及不能证明的部分 |
| --- | --- | --- |
| SRC-OPENAI | `openai-research`请求403；`openai-rss`200。News RSS实际相邻`Thu, 02 Apr 2026 10:30:00 GMT` TBPN与`Mon, 06 Apr 2026 10:00:00 GMT`Safety Fellowship。另本次打开[Research](https://openai.com/research/)及其[Research Index](https://openai.com/research/index/)，索引停于首屏9卡、最早09-10及Load more；[News research参数页](https://openai.com/news/?category=research)也仍停在10月首屏。 | RSS可见切片没有04-05项，但不能替代Research。历史日级Research目录受阻，隔离；只在有本窗官方目录/原始首次公开证据时重开。 |
| SRC-ANTHROPIC | `anthropic`200，Research嵌入publicationList的`publishedOn`相邻04-02T10:56Z `emotion-concepts-function`与04-07T09:35Z `mythos-preview`，完整读取该邻接字段；不是`_updatedAt`。 | 该Research可回溯切片未列04-05事件。限目录，未断言未列作者稿不存在。 |
| SRC-GOOGLE-AI | `google-blog/google-pubs/deepmind`请求fetch failed；本次网页恢复[04月Blog](https://research.google/blog/2026/04/)末尾04-03→04-08/09；[DeepMind Publications](https://deepmind.google/research/publications/)第1页30项、265总项，相关邻接03-22→04-22/23/25；[Google pubs](https://research.google/pubs/)首屏1–15/11614按年排序，只有年/venue且含2027，不能回溯日级。 | Blog与DeepMind selection只支持所见切片无本日列项。Google日级论文目录/selection未列首公开受阻，不能以2026年目录/Blog替代；不逐篇扩全年。 |
| SRC-META-AI | `meta`fetch failed；本次[Research](https://ai.meta.com/research/)网页恢复0行；[Publications results](https://ai.meta.com/results/?content_types%5B0%5D=publication)也未恢复可核历史列表。 | 必要日级历史入口受阻隔离，不记零命中；有官方历史分页或04-05原始报告后单源重开。 |
| SRC-QWEN | `qwen`200，[article retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)40项，逐读标题/`extra.date`；04-02T04:00+08 `qwen3.6`后最近04-15T10:00+08 `qwen3.6-35b-a3b`（数组非时间排序，未用数组邻项推断）。 | 40项显式日期切片无04-05事件。限该完整API响应，不把当前40项当全机构artifact库存。 |
| SRC-DEEPSEEK | `deepseek`与`deepseek-home`200；[News](https://www.deepseek.com/news/)可见2025-12-01 V3.2→2026-04-24 V4 preview；主页仅当前导航/产品入口。 | 已检查News相关日期切片，无04-05列项；主页不独立证明首次公开或release完整性。 |
| SRC-MOONSHOT | `moonshot`200，[Kimi Blog](https://platform.kimi.com/blog)单页26个可见日期条目，最近2025-11-07，最旧2024-05-29；相关模型/研究标题未见04-05。未遍历组织仓库。 | Blog当前可见切片已检查；未列研究/正式artifact的历史首公开完整性保留为限制。若出现04-05官方研究正文/正式release才定点重开，不审普通commit。 |
| SRC-TENCENT-HUNYUAN | `hunyuan`200，官方Research的`POST https://api.hunyuan.tencent.com/api/blog/publicList`，pageNum1/pageSize100/renderType0，9/9项。逐读title、displayPublishTime、publicAt、publishedAt；展示时间最近旧边界02-13→04-23，Hy3-preview展示04-23而publicAt07月。这里只观察到字段差异，原因未知，不推断CMS迁移历史，也不能改成first-public。 | 可见9项展示日期无04-05，历史未列/原始公开资格未知隔离。9/9不是机构全部研究完整性；有本窗原始文章/存档才重开，不查全repo。 |
| SRC-ZAI | `zai/zai-releases`200，[Research](https://www.zhipuai.cn/zh/research)呈现卡片日期04-01→04-07；[release notes](https://docs.z.ai/release-notes/new-released)锚点02-12→04-07。 | 所见官方卡片/正式发布切片无04-05。CMS createAt、media createdAt不当公开证据；不将普通更新时间当修订贡献。 |
| SRC-BYTEDANCE-SEED | `seed-papers`200，type1/count20/page_token40/US；响应18/243、next60/has_more=true。全页最高PublishDate科学项1775664000000，UTC04-08T16:00/BJT04-09；相关扩散`Not all tokens contribute equally…`1775577600000，UTC04-07T16:00/BJT04-08；其后03-31T12:00Z是TDDFT科学项，后续相关机器人/mesh为03-25/24。type2/page0的`seed-blog`15/95、next20/has_more=true，04-08T16:00Z全双工→03-31T16:00Z招聘。 | 保留原字段和语义，未擅自以CMS时刻声明first-public。相关日期切片无04-05交集；**18项不等于全部论文页已扫**，全页最高科学日期不混成相关边界。仅检查本窗相关slice，Science暂缓；现有切片外/首次公開未知不授无遗漏。 |
| SRC-BAIDU-ERNIE | `ernie`200，[技术Blog](https://ernie.baidu.com/blog/zh/)第1页10项，footer公开日期02-06→04-15，末项2025-11-21，下一页2/2已越窗。 | 该技术Blog有界日期切片未列04-05；不把Blog当全部repo/release。 |
| SRC-XIAOMI-MIMO | `mimo`200，[Paper/Blog](https://mimo.xiaomi.com/)Paper8项有文字日期，03-13 `ARL-Tangram`→06-29 `MOPD`；Blog15项含隐藏blog-more，全部卡片未给日期。 | Paper切片已检查；Blog日期资格受阻隔离，**不能说Blog无04-05**。不为确认所有卡片时间遍历Blog全文；出现有本窗日期的原始报告/存档时只重开相关卡片。 |
| SRC-MINIMAX | `minimax/minimax-zh/minimax-agent/minimax-techblog`200。英文Blog日期03-18→05-26，中文03-18→04-27；[Agent techblog](https://agent.minimax.io/docs/techblog)恢复的官方Markdown只有09-19/22、10-08三项，llms.txt只作入口身份。 | 这些可见目录日期切片无04-05；英文中文后界不混用，当前techblog不证明历史从未有未列文章。未遍历组织repo。 |
| SRC-ARXIV | 复用`arxiv-rules`200；官方周日20:00ET常规公告映射BJT04-06，补窗04-05不含常规batch。另复用cs.CL4月宽列表**1–2000/2532**仅作线索，未声称读完；本日四主题submittedDate查询与实际日期抽查如下。 | 正常规则不证明特殊公开、机构先公开或重要修订不存在；未确认的本窗公开资格隔离，不评分/不进Books，不由有界API或宽列表作全源零命中。 |

表外辅助定点查询：`site:openai.com/research "April 5, 2026"`、`site:ai.meta.com/research "April 5, 2026"`、`site:research.google "April 5, 2026" ("language model" OR transformer OR inference OR agent)`、`site:deepmind.google "April 5, 2026" research`。本次搜索未恢复可核本窗原始研究；实际OpenAI结果为community用户讨论（非官方作者研究），只作未恢复说明，不能承担Coverage/日期/证据，不追无关结果。

## arXiv：范围、失败试查、实际查询与资格出口

本日[抓取脚本](SUP_FETCH_DATE_20261013.mjs)只把四组主题定位到对应分类，不全扫分类或把返回条目自动送全文。受支持`submittedDate:[202604041600 TO 202604051559]`仅恢复04-05 BJT提交元数据；start0/max100，model34、system7、multi13、agent46，100条跨组出现去重为**81个ID/当前版本身份**，四组无返回分页截断。结果存于`SUP_arxiv-{model,system,multi,agent}-submitted_20261013.raw/request.json`，请求时间13:52:45～13:52:51Z；每组分类/同义主题与完整URL在request中。

之前13:45的四个`SUP_arxiv-*_20261013.raw/request.json`使用`lastUpdatedDate:[…]`试查。官方[API Manual §5.1及§3.3.2](https://info.arxiv.org/help/api/user-manual.html)只规定submittedDate日期过滤、lastUpdatedDate排序；该试查虽200且返回同样81身份，**不用作有效公开窗/修订覆盖**。原件保留，不覆写或用响应成功推定接口语义成立。新的submittedDate结果也只支持提交线索，不证明公开。

完整题摘仅对读了六个具体现有主题/代表性false-positive样本（不是81项全量贡献判断）：

- [2604.03803v1 Rényi Attention Entropy](https://arxiv.org/abs/2604.03803v1)：题摘为细粒度图像识别的patch-pruning；没有因Transformer词就纳入模型基础主线。不称本窗全量排除。
- [2604.03809v1 Representational Collapse](https://arxiv.org/abs/2604.03809v1)：角色committee共识的embedding proxy/encoder敏感性是可核潜在增量，不能因局部小实验就默认排除。
- [2604.04987v1 Cactus](https://arxiv.org/abs/2604.04987v1)：exact-v1 abs的Submitted=04-05 03:37:30UTC，Comments为ICLR2026 camera-ready；约束接受分歧可影响INFER-SPECULATIVE-DECODING。但Submitted/录用不证明本窗first-public，也不把后来版本/首次收录当首次公开。
- [2604.03941v1 SafeCtrl](https://arxiv.org/abs/2604.03941v1)：exact-v1 abs同为Submitted04-05，定位风险区域再局部DPO抑制可能改变安全/保真取舍；未读方法，不宣称安全有效。
- [2604.04018v1 1.x-Distill](https://arxiv.org/abs/2604.04018v1)：exact-v1 abs Submitted=04-05 08:30:35UTC；teacher CFG、阶段目标、cache联合蒸馏可影响MULTIMODAL-GENERATIVE-PARADIGMS，不因为看似组合就贡献前排除；未核实验与first-public，不采33×等数字。
- [2604.04035v1 Causality Laundering](https://arxiv.org/abs/2604.04035v1)：拒绝动作的反馈也影响后续信息流，潜在反例应核PLATFORM-SECURITY；未把题摘安全主张当已证实防护，不跳过日期资格。

三份exact-v1 abs定点页只显示提交历史，不提供本窗首次公开证明；已轻量看Comments/版本现状，没有用后版方法或实验支持本日报。其余75身份尚未逐项题摘筛选、未评分，不能叫已审重复项、明确全量排除或本日81篇新论文。本日实际按ID与精确版本/event核去重：81提交身份与原47表内家族均无ID或精确版本交集；额外的原02947隔离身份也无交集。本次不据此新建跨日候选/未完成全文队列。root已要求保这个有界出口，不扩大81项审阅；这不是DAY/FINAL通过。

**终态采用边界：** 04-05历史非例行公告、机构或作者先公開、窗口内重要修订，当前入口不足以核实具体资格；不拿规则、submitted/published/updated标签或未命中检索证明其不存在。暂无已确认落窗的新候选，新增评分0、Books新写0（No Change）；这不是断言81线索无学术/系统贡献。只有官方公开列表/存档或具体作者原始事件证明某个材料在04-05首次公开/重要修订时，重开该identity的日期与必要贡献/精确版本层，不扩整批全文、附件或本窗。

## root 本次六部分独立复核

**完成态FINAL：** 作者同步后root实际读回开头及§1/5/6，补窗/原窗口、无普通待办和外部采用边界一致；Cactus可修改odate限定已落实。47整行和27656字符连续原§4再次精确一致，92本地引用有效，V3及限定cached/unstaged diff-check通过。当前本日补查已验收；旧档案中的待DAY措辞为过程停点，不覆盖此实际最终结果。没有新Books写入或锁，作者可释放本日ownership，下一日另用fresh上下文。

复核者root，非本次补充作者。实际重读当前合同、本日全部来源记录、报告新增的六部分及限定diff；四主题实际request/pagination与响应数量、六份完整题摘、Seed原字段/分页和混元展示/公开字段已对读。原47候选整行、原窗口及27656字符连续原§4与补查前档案实际一致；没有新增Books正文，旧有效采用不因补查重复验收或改日期。

有限入口不构成81项全文队列，未筛的75身份没有冒称排除或贡献完成；具体日期线索和机构历史入口不能支持正面Coverage/Evidence或无遗漏。Cactus已按官方同题作者/摘要及venue公开日期记录走早期归属出口；root亲开FAQ和Note Fields确认odate权限，同时要求保留其可由venue修改的边界，不将该字段说成不可改真实日志。不比较camera-ready前后或恢复2025/整会，其他具体资格保留仍按本日出口隔离。

本次六部分DAY通过：原47＋确定新增0，Books新写0，本窗可执行普通工作0，未核历史/特殊公开仍隔离。作者尚须完成字段同步；完成态FINAL不由本段提前替代。V3、六H2、本地路径、冻结对照与限定unstaged diff-check实际通过，仅证明对应结构/一致性，不证明互联网无遗漏、实验复现或生产效果。

## 真实停点

14源已完成上述本日有界原始入口检查及限制划分；部分日级历史/Blog/special-public资格是外部保留项，不授其正面Coverage/Evidence或无遗漏。报告补窗新增候选0、Books No Change；无可执行全文/Books普通项。首批出口校准已交root（非作者）；报告六部分DAY和完成字段FINAL尚待实际核验，不继承旧apr03完成声明。不修改LS/索引/别日报/Books，不stage/commit/push；本日ownership在最终验收后释放。

22:59+08:00作者结构检查：V3校验通过（仅结构/可判定一致性），本日限定git diff --check通过；47候选整行hash和27656字符连续原§4 hash均与补查前原档案一致，本地报告链接无缺失，仍六个固定H2。Report diff仅为来源实际投影、补充状态与空行，不改变Books、LS或其他日报。现交root完整DAY；尚不标完成。

### root定点复核要求：Cactus正式正文早期公开日期出口

23:15～23:21+08:00仅按`Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling`在official forum/title定位。官方[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/abccb8a90b30d45b948360ba41f5a20f-Abstract-Conference.html)题目、两作者及完整题摘与arXiv同家族；官方[ICLR poster](https://iclr.cc/virtual/2026/poster/10007644)的04-23会期不用于first-public。[OpenReview forum](https://openreview.net/forum?id=lpUIkCAy9p)网页challenge；官方API精确标题limit1命中该submission，不展开其他review/附件/会议。原件[SUP_cactus-openreview_20261013.raw](SUP_cactus-openreview_20261013.raw)及[request](SUP_cactus-openreview_20261013.request.json)保存完整URL、实际HTTP200/执行时间和note身份。

该note的`id/forum=lpUIkCAy9p`、readers=everyone、`odate=1759896705795`（2025-10-08T04:11:45.795Z，BJT同日）、`pdate=1769436138687`（2026-01-26录用标记）、当前`mdate=1775877134485`（04-11）。官方[日期FAQ](https://docs.openreview.net/getting-started/frequently-asked-questions/how-do-i-locate-the-date-a-submission-is-made-public)与[Note字段](https://docs.openreview.net/reference/api-v2/entities/note/fields)明确odate表示venue记录的首次公开、pdate是被venue标Accepted；odate可以被venue设在past/future，不能称不可修改的法证时刻。不用cdate或pdate冒充公开。

**Cactus同题作者/摘要官方venue公开日记2025-10-08，配合正式ICLR2026身份支持早期公开归属；不将可修改odate当不可改真实日志。** 由此退出04-05首次公开资格保留，arXiv04-05提交/首次收录不重设归属。此处只完成身份与日期出口，不称旧文已审重复，不读/比较正文或给Books。camera-ready/版本标签未给具体重要机制修订信号，不因这种标签扩大Source。本日报补入被实际触发的SRC-OPENREVIEW单篇行；其余五个题摘样本处置不变化（四具体日期保留＋Rényi有界false-positive线索），不扩81项。没有另创2025报告或恢复整场ICLR。

### 完成字段同步与本日作者ownership释放

23:35～23:37+08:00作者已按root实际DAY通过同步Report状态为完成、检查时间、§1/5/6及Cactus可修改venue日期边界；没有重做论文或新发现。完成态V3再次通过；本地Report/SOURCES链接无缺失、仍固定六H2；原窗口不变，47候选整行hash仍`b6cc0a981c17670272c5d77e58c4f720e271529246676a859cf289a779ce58c7`，连续原§4仍27656字符/hash`bab03aaf5b95f5dd196f6f51308b9a2933b5e8d52db60f26bada1095531dc3b8`，与补查前原档案逐字一致。本日限定unstaged/cached diff-check通过，本日cached name-only为空；原47＋新增0、Books新写0、本窗普通Source/候选/Books0，无共享锁。

此为**作者完成字段/结构检查**，不替代root的完成态FINAL读回；非作者DAY记录在上方“root 本次六部分独立复核”。本日作者ownership至此释放，后续只由root读回验收和维护全局路由；未修改LS/索引/别日报/Books，未stage/commit/push。不能据此授历史目录/特殊公开资格正面Coverage/Evidence、实验复现或全网无遗漏。
