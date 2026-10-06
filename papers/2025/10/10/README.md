# Daily Research — 2025-10-10

**规范：** V3
**窗口：** 2025-10-09T09:00:00+08:00 ～ 2025-10-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T07:03:00+08:00

## 1. 结论

本日确定2个官方技术说明事件家族，深入审阅完成1、标准审阅完成1。Anthropic所测DoS修正“降低污染比例便提高攻击成本”的推断，但不证明普遍固定样本数；OpenAI将提示倾向、五个行为轴和生产人口分账，不授政治客观性保证。Books窄整合1（TRAIN-DATA，由root实际落实Ch27现有training-effect两段及末注）、仅报告1；Peirce实际POST与DAY通过。普通研究、Books写入及独立复核剩余0；具名终态保留项不授正面证据或无遗漏断言。

## 2. 来源覆盖

[原入口/真实query与请求时间](../_sources/daily-20251010/fetch_manifest.json)。各原件独立抓取，不继承他日筛选池。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research首查403；RSS本窗两条political-bias 10-09 13:00GMT与HYGH 10-10 00:00GMT，分别读官方core | 已检查 | 当前原文不冒称历史字节完全冻结；HYGH应用案例不入选 |
| SRC-ANTHROPIC | Research原SSR publishedOn=10-09 13:50Z命中small-samples-poison，官方core及所链精确v1必要机制/反侧经Peirce实际独核 | 已检查 | 页面事件落窗；同家族论文首次公开仍未确认，不用submitted代first-public |
| SRC-GOOGLE-AI | DeepMind原Research当前响应；pubs`?year=2025`实际返回2026等库存，过滤未生效；原Blog October页1/2到2/2；XR Blocks core实际读 | 受阻 | pubs不能以Blog替代；year请求不等2025结果，未把库存转队列 |
| SRC-META-AI | Research品牌外壳首查，限定日期/模型机制补检 | 受阻 | 本窗历史目录无法从当前外壳重建 |
| SRC-QWEN | GitHub原Blog首屏最新09-23；新qwen.ai/research外壳 | 受阻 | 新站2025历史段未恢复，不把旧站无条目当新站无事件 |
| SRC-DEEPSEEK | 原主页首查后恢复`/news/`独立研究索引；动态09-29→12-01，Research05-14→10-21，日期段已读 | 已检查 | 只限原索引可见本窗两侧，不宣称全站/repo无遗漏 |
| SRC-MOONSHOT | Platform Blog09-16→11-06日期段、组织当前入口 | 已检查 | 仅可见Blog日期段，组织页面不能替历史release |
| SRC-TENCENT-HUNYUAN | Research动态页首查；官方publicList POST page1/100/renderType0全部11条，publicAt均2026 | 受阻 | 历史2025缺段；此前本会话有限browser能力核查不支持子线程IAB，不假称本日browser读过 |
| SRC-ZAI | Research own bundle实际LoadMore设page参数；请求`?page=2`累积18条并显示没有更多，最早12-07；release notes09-30→12-08 | 已检查 | 当前原目录终页没有2025-10段，不声称历史无事件 |
| SRC-BYTEDANCE-SEED | own bundle核x-tt-locale；type1 US/2025/asc/count20 token0/20/40/60/80至has_more=false；type2到token40终页；相关Function Tokens完整题摘已读 | 已检查 | 论文列表已恢复，不再保留缺正文；10-09是展示日名，不当first-public时刻 |
| SRC-BAIDU-ERNIE | 中文Blog两页至2/2，PLAS09-12→PaddleOCR-VL10-16 | 已检查 | 不外推所有repo事件 |
| SRC-XIAOMI-MIMO | Paper8项日期09-19→10-21，Blog首屏 | 受阻 | More未被证明为历史分页，Blog缺段 |
| SRC-MINIMAX | en/zh Blog首屏与独立Agent techblog仅2026-05-13 | 受阻 | 三入口历史限制分别保留 |
| SRC-ARXIV | 四主线title主题API提交范围10-08～09，start0/max30，total94/7/33/121；官方cs.CL/2510 start0/show100返回404 | 受阻 | 主题线索混最新版本、不证明public time；无分类库存逐项全文队列，first-public/相关标题补检缺口保留 |

按需：未独立扩扫每周来源/会议。Anthropic所链论文是具体证据恢复，不扫论文邻居。

## 3. 候选与判断

以下2个官方技术说明页面事件经[FIRST独立校准](../_sources/daily-20251010/FIRST_INDEPENDENT_REVIEW.md)准入。所链论文不另计家族，不由Blog日期搬移其首次公开归属。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [A small number of samples can poison LLMs](https://www.anthropic.com/research/small-samples-poison) | 2025-10-09T21:50:00+08:00 | 所测DoS中，扩大clean corpus不能仅据污染比例推定攻击成本增加；3+2+2=7 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md#内容无害不等于更新无害过滤器还要预测-training-effect)两段及末注由root实际写入，Peirce POST通过 |
| [Defining and evaluating political bias](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/) | 2025-10-09T21:00:00+08:00 | 开放交互提示倾向与五行为轴分离，挑战集条件风险与生产人口发生率分账；2+1+2=5 | 标准完成 | 仅报告：五轴rubric是现有条件评价合同实例，未改变长期owner论证 |

## 4. 证据与知识整合

### [A small number of samples can poison LLMs](https://www.anthropic.com/research/small-samples-poison)

采用受限判断：作者主实验为600M/2B/7B/13B、20 tokens/parameter、100/250/500污染文档的gibberish/DoS训练，24配置各3seed共72模型。**独立clean-budget干预仅600M/2B**，支持所测配置中不能仅通过污染比例稀释推定攻击成本增加，不外推干预已覆盖7B/13B。300 clean prompts及配对trigger的gibberish/perplexity评价支持配置内判断，误差条不是置信区间；不采用“任意模型250文档足够”的常数结论。

本次复用Peirce[实际独核](../_sources/daily-20251010/FINAL_INDEPENDENT_REVIEW.md#2-原事件与必要核心实际核验)的官方全部技术core与[2510.07192v1](https://arxiv.org/html/2510.07192v1)§2–3方法/评价、§4顺序与clean continuation、§5–6边界及必要F.2–F.4/I，不冒称作者重读全部附件。文档长度与poison-token暴露不可互换；batch密度、顺序、LR改变样本要求。clean continuation和模拟alignment可削弱后门，真实生产安全post-training持久性未证明。特定SFT有害服从实验不混作预训练DoS跨规模保证，防御讨论不是认证控制；未复现实验。

页面SSR的`publishedOn=2025-10-09T13:50:00.000Z`支持本窗官方说明事件；论文`Wed, 8 Oct 2025 16:25:05 UTC`仅submitted。两者同家族，论文first-public仍隔离，不授09/10论文归属或已审重复。

最终Books判断：1条窄整合已由root实际落实，owner `TRAIN-DATA`。原比较实际读[Ch27 training effect](../../../../books/part-04-training-system/27-data.md#内容无害不等于更新无害过滤器还要预测-training-effect)及代码训练适用性L281–308，已有checkpoint/recipe/lineage/canary与安全回归责任；[Recursive Data](../../../../books/part-04-training-system/27-data.md#recursive-data-的控制量不只有比例还包括真实样本绝对注入量)L1253–1258已讲真实样本绝对注入量，不能称测量原则全新。邻接[Ch28](../../../../books/part-04-training-system/28-pretraining.md#next-token-objective)已区分token exposure、batch composition、loss normalization与预算。差额只在恶意暴露：低污染比例不是抗投毒证据，须分别保存污染文档/poison tokens、clean预算、顺序/配方和对应行为测量，且稀释、clean续训与安全post-training不是可互换的修复保证。实际新增Ch27 L300/302两段嵌入现有training-effect交接，不新增论文收纳节；保留内容过滤/可信来源/canary旧路径、审计成本及受测DoS边界。由Peirce非写入者实际核两段、邻接及末注，POST通过，见[FINAL§7](../_sources/daily-20251010/FINAL_INDEPENDENT_REVIEW.md#7-实际-books-post-与最新-day-裁决)。[原窄提案](../_sources/daily-20251010/BOOKS_PROPOSAL.md)保留比较依据，不再是待写入项。

### [Defining and evaluating political bias](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/)

标准审阅采用官方core L64–149的具体评价设计：约100政治主题×5种提示倾向，另沿五个行为轴用rubric评分，以GPT-5 thinking grader/reference-response迭代校准。提示倾向不是回答行为的同一变量；挑战集条件分数与production traffic估计必须保留各自人口/分母。范围为text-only/no-search、先U.S. English，跨地区仅早期探索。生产<0.01%未披露抽样N、时间、不确定性及独立rater校准，不采用为独立总体真值，不采用厂商改善数字或普遍政治客观性。实际core由Peirce独核，未运行评测。

最终仅报告：实际读owner `PLATFORM-EVALUATION-SYSTEM` [Ch66条件评价与EvalSpec](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#从目标到证据而不是从指标到目标)的subject/population/failure taxonomy/scorer/slice/uncertainty及非随机反馈；邻接[Ch67四层指标](../../../../books/part-06-ai-infrastructure/67-monitoring.md#四层指标)只承载已定义信号，不接管规范性判断。五轴具体rubric与grader版本是该合同的应用实例，现有正文已承载两类人口不可交换的判断；这里没有新的长期控制权/机制差额，不写Books。

## 5. 缺口与下一步

普通研究、Books写入及独立复核剩余0。[1条Ch27窄提案](../_sources/daily-20251010/BOOKS_PROPOSAL.md)已由root落实；Peirce实际POST及DAY通过，不重开有效FIRST、来源或附件。以下仅为精确外部隔离，不阻塞本次安全终态。

本窗终态保留项：[初筛记录](../_sources/daily-20251010/SCREENING.md)8个arXiv潜力家族及Seed Function Tokens缺first-public/精确v1，不用于正面证据、Books或无遗漏断言，不因负面、理论、小模型或主题已有覆盖排除。恢复条件是具名材料的原官方历史公告/公开列表与相应原版，bounds完整落窗后只重开该项；其中TAPO若落窗须继续必要reward-hacking反侧，不冒称已深审。Anthropic所链论文first-public单独保留，不影响已确定的页面事件；恢复只重开该身份/去重归属。来源表历史目录或异常响应也不授无事件/性能安全保证，取得本窗官方历史段只定点补对应来源。Google pubs旧year参数实未过滤，已恢复`category=2025&search=language model`原第一页，但仍年级而非日级日期；原Blog不消除此缺口。三源恢复真实请求见[补查原件](../_sources/daily-20251010/recovery_manifest.json)。

## 6. 复核

复核者：Peirce（非作者）

结论：通过

FIRST及FINAL已核两项页面事件准入、十四来源有限停点、9个潜力完整题摘、XR/HYGH代表排除与必要安全core。R-EVIDENCE/R-SCORE/R-BOOKS已落实；[FINAL§7](../_sources/daily-20251010/FINAL_INDEPENDENT_REVIEW.md#7-实际-books-post-与最新-day-裁决)记录非写入者Peirce实际顺读Ch27新增两段与相邻论证、Ch28 NTP交接，确认受测DoS及600M/2B clean-budget边界、末注事件身份，POST与最新DAY通过。作者仅同步该实际结论，不自审；raw、V3与链接检查不授语义通过。

完成态V3实际通过；本次同步及13新作者文件共六份Markdown的本地引用、代码块与尾随空白检查通过，限定diff空白检查通过。共享书、索引与state未由作者修改。
