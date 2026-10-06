# Daily Research — 2025-12-10

**规范：** V3
**窗口：** 2025-12-09T09:00:00+08:00 ～ 2025-12-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T20:06:20+08:00

## 1. 结论

本日独立执行十四每日源有界检查，确定落窗两家族：FACTS评价分支与SGLang NSA/FP8路径兼容性报告。作者侧已读必要原始说明和固定版本源码，结论严格限于协议/版本对照，未复现性能或认定bug。两项限定准入/证据已有Popper独立检查，日级验收未授。

arXiv潜在贡献保留于精确ID原始表，SAM比较已恢复潜在并完成共同遗漏理由的原段核补；必要首公开批次未恢复而安全隔离，不代表零事件或覆盖通过。RLAX官方撤回不评分不采用。FACTS由root实际写入Ch66两段；SGLang版本背景仅报告。ASR文章已核落窗，但当前参数脚注不能反推早期披露，相应命题隔离。

## 2. 来源覆盖

原始入口及显示字段见[当日目录记录](../_sources/daily-20251210/HISTORICAL_DIRECTORY.md)；本日12/09官方域日期检索独立执行，不套用09结论。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research、官方12/09检索与AAIF完整核心 | 受阻 | 治理捐赠无此次执行增量；滚动研究历史部分隔离 |
| SRC-ANTHROPIC | Research十项、12/09检索；Alignment December六项至November两项，SGTM12/08→Replication12/12邻接 | 受阻 | Alignment显示段已恢复；其他Research历史部分隔离，不报零 |
| SRC-GOOGLE-AI | Research/pubs、12/09检索、FACTS原文时间；DeepMind正确page/4显示24条，FACTS12/09→UK12/10→AISI12/11邻接 | 已检查 | 当前FACTS PDF标12/11非本窗精确稿；目录不保证全量 |
| SRC-META-AI | Publications page4：12/12与12/01当日邻接 | 已检查 | 仅公开显示目录，发表日不是论文first-public |
| SRC-QWEN | 旧站09/23后跳转、新动态Blog、12/09官方检索 | 受阻 | 目标历史目录隔离 |
| SRC-DEEPSEEK | 官网/V3.2固定12/01说明、12/09查询及SGLang实际触发 | 已检查 | 官网不是完整历史档案；触发单列 |
| SRC-MOONSHOT | Blog/changelog最新11/06、组织当前段、12/09检索 | 已检查 | 只限定显示目录，不推所有仓库无事件 |
| SRC-TENCENT-HUNYUAN | Research首查超时、同轮已核浏览器全部十一项至2026/02/03、组织及12/09查询 | 受阻 | 2025历史目录有限替代后隔离 |
| SRC-ZAI | Research首查/组织/release12/08–11邻接、12/09检索；ASR149原UTC time/核心，复用非作者固定早期README比较 | 已检查 | 当前脚注不在早期固定稿，参数反证历史采用隔离；当前图非历史冻结稿，未显示部分隔离 |
| SRC-BYTEDANCE-SEED | 官方2025 paper/Blog API各18条、total94/45、next20；本日paper12/15→12/02、Blog12/16→12/02邻接 | 已检查 | 只支持实际显示目录，pinned逐项核日期，不授全源零事件 |
| SRC-BAIDU-ERNIE | Blog12/09 Preview与12/23/11/21邻接、repo说明 | 已检查 | Preview核心为排名非机制；日标签未授归窗 |
| SRC-XIAOMI-MIMO | Paper八项2026/01/08与2025/10/21邻接、Blog/组织、12/09检索 | 受阻 | Blog历史部分隔离 |
| SRC-MINIMAX | 两语Blog12/23与10/27邻接、组织、Agent导航/目录、12/09检索 | 受阻 | Blog显示切片已处理，Agent历史技术部分隔离 |
| SRC-ARXIV | 本日四主题日期查询与CL/LG/DC/AI/CV官方有界邻接，完整相关v1题摘 | 受阻 | 无有效逐篇new公告；日期隔离见原始表，不作零 |
| 表外：[SGLang14691](https://github.com/sgl-project/sglang/issues/14691) | 官方API事件时间、原问题/配置、v0.5.6两个必要源码文件 | 已检查 | 未复现、报告者build commit未取得，不认定bug/修复 |

## 3. 候选与判断

下表评分在作者贡献判断后给出，不把声望/访问状态/Books处置计分。两项限定证据及日级非作者验收已通过，见§6；不包含日期未授arXiv及历史命题未成立ASR。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [FACTS官方协议说明](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/) | 2025-12-09T19:29:03.922000+08:00 | 来源分支与统一search tool控制，改变单一事实性总分判断；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Context→RAG之间实际两段 |
| [SGLang14691](https://github.com/sgl-project/sglang/issues/14691) | 2025-12-09T11:22:07+08:00 | NSA/FP8 mode/backend实际路径的局部兼容反例；2+2+1=5 | 深入完成 | 仅报告：版本背景；通用兼容原则有实际覆盖 |

## 4. 证据与知识整合

详细精确来源、证据位置、反证与原文/作者推断分界见[ADMISSION_EVIDENCE](../_sources/daily-20251210/ADMISSION_EVIDENCE.md)。

### [FACTS官方协议说明](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)

FACTS只采用官方博客四任务分账/统一搜索工具说明，所链PDF首行12/11，不能偷渡其rubric/F1/threshold为12/09既有事实；当前页面modified字段不替代published。平均分不证明任何单一部署质量。作者本轮实际重读[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)904/906两段：第一段保留四分支/public-private/统一工具与不同题集不能作因果对照；第二段保留工具、图像、holdout/judge成本、固定单用途基线和收窄发布声明。root写入并绑定`SF-2025-GOOGLE-FACTS`，不冒称作者写书或日级通过。

### [SGLang14691](https://github.com/sgl-project/sglang/issues/14691)

SGLang固定v0.5.6 memory_pool 1411–1419/1499–1526、flashmla_backend432–443显示通用与专用写入不同。报告者tag版本与日志行号不完全相同，未取得容器commit、未运行复现；不能断言架构不支持FP8、assert应删除、官方已修复。报告中的配置上限不是真实batch或SLO，性能条件Not Disclosed，不作提速结论。

FACTS唯一owner为Ch66 `PLATFORM-EVALUATION-SYSTEM`，已对读实际14–47、89–105、199–205、898–900及Ch65/67交接；原Context段明示不测retrieval/tools，新增904/906两段实际补并列任务分账，不覆盖同题诊断。Popper的单篇POST由其独立记录承接，不扩大为日Gate。SGLang版本背景对读Ch51配置admission、Ch50 backend/layout identity和Ch52兼容state，只支持相邻通用原则，不声称完整覆盖该具体forward-mode/setter缺陷。

## 5. 缺口与下一步

作者普通待办0：三条目录恢复已同步；[ARXIV_SCREEN](../_sources/daily-20251210/ARXIV_SCREEN.md)补原8项含SAM及CL/CV同段22项必要题摘；FACTS实际两段已同步；[ASR](../_sources/daily-20251210/ASR_CALIBRATION.md)保留文章落窗与current脚注/固定早期稿差异，未把缺历史命题删项或补造成候选。非作者日级核验已通过，最终范围与结果见§6。

**终态保留项：** 外部历史目录缺口按第二节逐源隔离，仅限未恢复部分；原入口/日期查询/组织或发布目录替代见当日目录。恢复需各入口12/09–10原始历史段。arXiv恢复需ID/v1匹配官方new公告或正文公众范围完全落窗；若09:00为右端归下一日。SGLang报告者精确build可到达后只重开路径一致性；FACTS12/09精确技术稿到达后才可重开后续PDF细节，不将当前12/11稿冒充旧稿。ASR参数口径反证仅其历史披露命题隔离，重开需当时正文/固定图片明确encoder是否计入；文章时刻已核，不再请求该日期。

这些终态保留项不支持正面证据、Evidence/Coverage通过、Books采用、无遗漏或零事件保证。没有扫描Weekly来源、没有新index/state，没有stage/commit/push。

## 6. 复核

复核者：Popper（主线程委派的独立非作者agent；不是作者Plato或Books写入者root，不使用共同chat ID）。
结论：通过

2026-10-02T20:06:20+08:00实际读取作者最新§5，已明确终态保留项、否定采用边界和定点重开条件；此前唯一普通同步差额已闭，普通待办0，授本日独立验收通过。两项确定落窗家族的限定证据与Books处置已落实，不从作者ready或机器结果授内容通过。§1/§3/§5保留的是作者交接时点待验表述，最新验收结论由本节承接。完整过程及旧未通过记录保留在[ROOT_ADMISSION_REVIEW](../_sources/daily-20251210/ROOT_ADMISSION_REVIEW.md)。

实际范围：逐日重读AGENTS、研究/报告合同、每日来源说明、Prompt、ROADMAP与相关state；读本日README、ADMISSION_EVIDENCE、ARXIV_SCREEN、HISTORICAL_DIRECTORY、ASR_CALIBRATION及对应修复。实际读取FACTS官方博客、published字段与后稿PDF首页，SGLang官方API/原issue/全部5条评论及固定v0.5.6两份必要源码，核Ch66/65/67与Ch51/50/52实际owner。FACTS原博客四任务/统一search/public-private→Ch66新增两自然段及Context/RAG邻接的非写入者POST通过，末注已获窄授权更新；不采用后稿阈值、数字或排行榜。SGLang只采用可核版本化路径对照，不宣称已复现bug、官方修复或移除assert即可支持。

A/B/C/D已闭：有限Seed/DeepMind/Alignment恢复及未恢复边界同步；原36项潜在题摘和8项补漏全部独立取得，SAM另读§2/3/6/7及表；作者原CL/CV段共同理由扩查22项精确v1题摘也全部独立取得并核身份/增量。新增20项明确潜在、06586语言移植贡献前关闭、06255局部贡献含糊/原始摘要尾缺失保留，不冒称其缺失部分已读；07515的v1名SPAD与目录后名区分，源摘要尾止于performance。FACTS实际写入/POST与§1–5已同步。ASR实际原文time落10，但固定早期HF README不含current encoder排除脚注；最终只隔离该历史未证命题，不计第三候选、不评分或进Books。

分层负侧与停止核：AAIF完整核心、ERNIE排名目录摘要；临床出院/病理分割及传统云历史仅核明确范围外标题。实际核CL/DC/CV有界列表、Meta/ZAI/MiniMax显示目录、Seed官方历史接口及DeepMind正确page/4、Alignment December→November，未把Nash路由冒称本次执行。有限目录无新增不等全机构零事件；真正穷尽必要日期的材料可安全终态。

未检查边界：未全量重放作者13源日期查询，未独立重扫LG/AI或全站全月，未完成36+8+20项全部正文/附录/实现Evidence，未恢复逐篇first-public，未运行模型/性能实验或访问集群。Books只验FACTS本次两段及末注，不认证整章。隔离的arXiv日期/历史目录、ASR历史脚注、SGLang报告者精确build及FACTS12/09精确技术稿，不支持Coverage/Evidence通过、无遗漏、性能或安全保证；到达后只重开对应身份/版本/命题。

机器检查：此前完成态仅报§5未显式终态，作者现已修复；本次重新执行完成态校验及限定diff空白、§1–5逐字保护、旧root追加保留检查，结果记于root最新追加。只改授权metadata/§6与root追加，FACTS末注为另获窄授权，未改Books正文、月index/state；未stage、commit或push。机器通过不替代上述语义验收。
