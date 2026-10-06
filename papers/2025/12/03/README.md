# Daily Research — 2025-12-03

**规范：** V3
**窗口：** 2025-12-02T09:00:00+08:00 ～ 2025-12-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T19:32:57+08:00

## 1. 结论

1个完全落窗家族已作作者侧标准审阅：Anthropic内部研究提供自治活动指标与真正可委派口径不同的局部证据，不证明可靠性/生产率因果提高。Books对应规范已有具体覆盖，无改书。Mill具名九项普通判断已定点补齐，Reward Features旧机制去重但新理论事件未决，其余八项窄潜在准入保留；不计为确定落窗或Evidence完成。14源有界检查后作者普通待办0，具名首公开/历史目录仍外部隔离；受影响九项已由Mill独立定点复核通过，日级验收见§6，非作者自授。

## 2. 来源覆盖

逐源原始边界和查询见[本日记录](../_sources/daily-20251203/WINDOW_REVIEW.md)，固定历史目录按本日独立比对。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮RSS成功，Dec2 01Z至Dec4 01Z只见Dec3 08/10Z邻接 | 已检查 | 均在本日截止后；不外推所有论文 |
| SRC-ANTHROPIC | 原始publicationList Dec2精确时间/Dec4邻接，原文核心与Appendix | 已检查 | 本日研究的窄判断已由Mill独立核验，不称全站召回 |
| SRC-GOOGLE-AI | 原始Google Blog/DeepMind第3页Nov21/Dec3邻接按本窗比对 | 受阻 | Dec3日期项未取得09前精度，隔离 |
| SRC-META-AI | 原始第4页Dec1/Dec12连续邻接 | 已检查 | 收录不是首公开，未见具名新事件 |
| SRC-QWEN | 原始旧Sep23/新站/部署/README有限恢复按本窗检查 | 受阻 | 历史目录保留缺口隔离 |
| SRC-DEEPSEEK | 原始API Docs Dec1/下一2026 release邻接 | 已检查 | 已有Dec1家族日精度请求不重复采用 |
| SRC-MOONSHOT | 原始全Overview26项最近Nov7、changelog Nov6按本窗检查 | 已检查 | 只声明入口范围 |
| SRC-TENCENT-HUNYUAN | 原始Research失败与All API11项全2026 | 受阻 | 2025Research历史缺失隔离 |
| SRC-ZAI | 原始All第1/2页Dec9/Dec7终点、release Dec8 | 受阻 | 旧目录保留不全隔离 |
| SRC-BYTEDANCE-SEED | 原始2025paper Dec2/Oct22、Blog Dec2/Nov27首段 | 受阻 | GR-RL日编码不补09前/后精度 |
| SRC-BAIDU-ERNIE | 原始2/2页至Nov7、Nov21/Dec9邻接按本窗检查 | 已检查 | 无全机构保证 |
| SRC-XIAOMI-MIMO | 原始Paper8项Oct21/Jan8、部署HSS Dec19/Safety Dec18 | 受阻 | 无date路由与旧More完整性隔离 |
| SRC-MINIMAX | 原始全13项及中文Oct27/Dec23邻接 | 已检查 | 未触发具名Tech Blog，非全机构零事件 |
| SRC-ARXIV | 四组主题日期检索；cs.DC/cs.CV首段实际浏览到23，相关v1完整摘要 | 受阻 | 检索越日期、月身份不归日；个体公告隔离 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) | 2025-12-03T02:58:43.576+08:00 | 自主动作数与真正可委派任务口径不同的局部评价反例；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体段落见§4 |

## 4. 证据与知识整合

### [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)

采用Dec2原始正文与官方非午夜publishedOn字段。标准审阅核Key findings、完全委派定义、Figure3指标与Appendix限制：连续工具调用只描述轨迹活动；调查定义不统一、非匿名/回忆/选择偏差，任务类型比例变化不是绝对产出或质量。不能从更少人工turns推导成功率/可靠性提高，也不采用自报生产率为因果性能数字。[本日证据](../_sources/daily-20251203/WINDOW_REVIEW.md)列协议与反证。

Ch66“从目标到证据，而不是从指标到目标”实际定义目标、eligible population、failure和scorer；相邻Ch67区分观测和质量决策。Ch84“Serving结束不等于Agent任务结束”要求terminal evidence，Ch81保留Verifying/approval，均实际对读。因此该窄判断已有覆盖，无书稿修改，不声称新增局部调查结果已普遍验证。

## 5. 缺口与下一步

作者普通待办0；[九项具体补正](../_sources/daily-20251203/NINE_ITEM_REPAIR.md)已写清实际读取、贡献/重复处置、关键反证及必要恢复，Mill已仅核受影响集合并完成日级验收，结果见§6。1项确定候选的有效准入/证据/Books判断不重复。

本窗终态保留项：本日原7个具名arXiv潜在贡献及SIMPLE、上述九项的必要首公开/修订差异/采用协议、GR-RL日编码、Qwen/Hunyuan/Z.ai/MiMo旧历史目录。有限原始替代后隔离，不用于正面证据、不进入Books、不支撑无遗漏或性能/安全保证，不计Coverage/Evidence通过。九项中VLM同epoch不等预算、Delta Sum聚合有效步长、PEFT表格反证均保留，不能用缺日期抹去。恢复需具名精确版本历史new公告或可核实首发正文，Reward Features另需重要修订差异；旧目录需2025原始邻接段，只重开相应材料/真实归属日与拟采用命题。

窗外线索TokenScale、FFTrainer、Gate-Norm的提交在本窗之后，未授真实first-public，不扩张本日。OpenAI Confessions RSS Dec3 10Z属12/04，留下一日独立处理。

## 6. 复核

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`；非作者 Gibbs。

结论：通过

本日已实际日级复核。14源范围/有限停点逐项审计；独立访问Anthropic报告核心、Figure3定义与Appendix，并以Research publishedOn、单页article:published_time/datePublished交叉核得 `2025-12-02T18:58:43.576Z`。1个确定落窗家族的窄准入、5分标准审阅和Books已有覆盖判断通过；当前官方页面另有2026 modified字段，不冒称取得2025冻结正文。Ch66目标/eligible population/failure/scorer与Ch67、Ch84、Ch81实际对读，无新Books写入。

7项新增拟准入精确v1完整题摘独立校准，SIMPLE只复用同身份有效校准、不授公告日。cs.DC/cs.CV原站首23条各实际恢复，未翻全月；相关标题定点抽核，安全/反证含Adapter Shield、IslandRun、诊断prompt低绝对一致性及Google声学评价。普通负侧分层读工业synthetic-data、CapsNet及范围外题名，不把所有46条标题变成逐项深审队列。

原普通9项已由Gibbs归并，本轮只复查[九项补正](../_sources/daily-20251203/NINE_ITEM_REPAIR.md)，未重读未变来源。Google两项、Diagnostic prompting及MCU ODL复用本复核者实际同身份题摘/必要核心；新增独立读取FlexiWalker精确v1 §3.2/3.3、§4.1及§6.3，Delta Sum精确v1 PDF §III Eq9–21，Active Storage §3.1/3.2，Data-centric VLM §2.6/2.7 Tables1/2，PEFT-DML Framework/Experiments Table1。动态选择器失误、sum改变有效步长、同epoch非等预算及PEFT表格反证均不因摘要成熟组合或缺日期关闭；作者保留窄potential和采用限制正确。Delta Sum HTML失败后PDF文本成功，公式截图接口失败，不声称视觉公式核验。普通待办0；确定落窗分母仍1，外部潜在项不补入分母。

其余真实首公开与旧目录缺口按§5保留具体终态及定点重开，不授Coverage/Evidence、零事件或普遍安全/性能。此前V3进行中结构校验通过；本轮完成态校验实际通过（exit 0），机器检查不替代上述语义复核。未改Books/共享state，未stage/commit/push。
