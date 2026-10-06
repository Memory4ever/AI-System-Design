# Daily Research — 2025-11-07

**规范：** V3
**窗口：** 2025-11-06T09:00:00+08:00 ～ 2025-11-07T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T18:59:01+08:00

## 1. 结论

本日从原始来源独立重建，不继承别日候选或旧 Weekly。首批 Kimi K2 Thinking、Shrinking the Variance、Learning Without Critics、SnapStream 四个具体贡献方向已由 root 独立准入校准；尚未取得完全落窗的公开证明，不能计为已确认本窗候选分母。三篇 exact-v1 已读关键机制、对照与限制，Kimi 已读历史模型卡的 QAT 和评价设置。Ohm已有限复核尾部方向、必要反侧及未采用边界，不授日期、全部潜在项完整Evidence或Books整合。

可核的具体差额是 batch-only 双层 leave-one-out 相对现有历史全局统计 prior 的独立性边界，以及静态 KV 容量、有效 token 与 ring slot 生命周期的区别。它们不是算法名称缺位。经典控制负证据同时改变 gamma/horizon 且分组不是同 prompt；SnapStream 吞吐表含假定 MTP 2.4 倍缩放且有质量退步，参考索引也不一致；Kimi 没有 disclosed matched BF16/no-QAT 质量/速度对照。均不授普适性能、无损或 runtime 保证。

原25项选择性完整题摘、原16项普通准入裁决及窄查询发现的其他含糊相关项现已有限收束，方向/原字段/最小重开均保留；它们不是已确认落窗候选数，也不是全部Evidence完成。root后续八方向校准已实际读取：五论文方向及action controls潜在通过，ScalingEval关闭，DLM未识别本窗新贡献事件。Ohm尾部与Carver来源独立复核已实际读取；两处错引用、可用native目标段、Bayesian命题边界与过期ownership已同步，Ohm于2026-10-04T18:50:11+08:00实际定点回核通过。尚无材料获得完全落窗证明，不因日期隔离取消贡献方向或强变评分。本轮没有Books写入，普通可执行工作0，依据非作者日级通过同步完成；不授全部潜在项Evidence或Books整合通过。

RAGBoost v1仍按已校准撤回声明不采用；当前同ID已有2026 ContextPilot v3/v4，不能把整个家族写成始终撤回或回填后续机制。DS-STAR本窗博客相对更早家族未披露新机制，事件去重已校准。公开日期/历史目录外部限制不支持零命中或无遗漏。新增安全反侧、公式/日期冲突仅隔离受影响保证，不授论文通篇无效。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research/原站窗口补检，实际日期线索11/06政策、合作与 Enterprise release notes；action controls核心已读并经root方向校准，10/27与11/12边界可见。[原查询](../_sources/daily-20251107/nov07-search1.txt)、[控制核心](../_sources/daily-20251107/nov07-custom-control-core.txt) | 受阻 | 仅原日粒度、时区不明，未证明完全落窗；历史公开上下界到达后只重开该变更，不回填当前Help未来snapshot机制 |
| SRC-ANTHROPIC | 官方Research有限查询后，按Ohm指定仅复用09包的具名原响应，非09候选/结论：[native](../_sources/daily-20251109/anthropic.html)、[receipt](../_sources/daily-20251109/anthropic.html.receipt.json)、[提取](../_sources/daily-20251109/anthropic.html.extracted.json)。GET HTTP200实际取于2026-10-04T08:33:29.861Z；publicationList 171条，本窗UTC[11/06 01Z,11/07 01Z)被11/04T16:00:49.850Z至11/12T18:19:00.000Z相邻条目跨过，传回数组窗内未命中 | 已检查 | 仅该有限Research数组目标段，不保证被删除历史或全站无遗漏；Control Protocols原论文日期保留不变 |
| SRC-GOOGLE-AI | DeepMind/Research入口、Publications和11/06 DS-STAR 原博客核心；对应 arXiv 2509.21825 v1 09/26、v2 09/29、v3 10/02，本窗博客无新差额披露。[原始材料](../_sources/daily-20251107/nov07-core2.txt)、[身份](../_sources/daily-20251107/nov07-date-and-correction.txt) | 受阻 | 有限入口结束；DS-STAR去重不等于当前2026目录覆盖完整历史窗；恢复需要原历史相关列表 |
| SRC-META-AI | 官方 Research动态入口未提取有效列表；`site:ai.meta.com/research after:2025-11-05 before:2025-11-08 language model` 有限补检；Common-O作者论文原题摘已读。[查询](../_sources/daily-20251107/nov07-native-finite2.txt)、[v1](../_sources/daily-20251107/nov07-second-calibration-v1.txt) | 受阻 | 原生历史目录未恢复；Common-O更早会议公开身份待核，不能以arXiv submitted归属 |
| SRC-QWEN | qwenlm.github.io原Blog到2025/09，跳转新Qwen站研究页动态内容未提取；`site:qwen.ai/blog after:2025-11-05 before:2025-11-08`有限查询。[原响应](../_sources/daily-20251107/nov07-native-finite2.txt) | 受阻 | 新站历史目录缺失，不宣称11/06无新增 |
| SRC-DEEPSEEK | 原有限查询后，按Ohm指定仅复用09包的具名官方News原件：[native](../_sources/daily-20251109/deepseek-news.html)、[receipt](../_sources/daily-20251109/deepseek-news.html.receipt.json)、[提取](../_sources/daily-20251109/deepseek-news.html.extracted.json)。GET /news/ HTTP200实际取于2026-10-04T09:47:05.082Z；newsPosts 16条，目标相邻自然日期12/01与09/29之间未列11/06或11/07 | 已检查 | 只支持该传回News目录目标段，非全部Research/删除历史完整性；不继承09候选或Coverage，不扩扫版本库 |
| SRC-MOONSHOT | 官方Platform Blog本窗相交日期 Thinking/价格；历史card commit `f5ed4a8f7f535ecd0625df17878fd6731e5af7ed` QAT/评价脚注；官方论坛价格核心与指向X公告。有限HF API/X替代未得到首公开证明。[证据与日期](../_sources/daily-20251107/FIRST_EVIDENCE_OWNER_DELTA.md) | 受阻 | Blog仅11/06日期，card commit不是public；论坛created_at在窗外，X403。所缺原件与停止条件见§5 |
| SRC-TENCENT-HUNYUAN | 官方Research首查无可提取列表；浏览器一次先前超时、本轮参数不支持后无参数超时；官方POST publicList `pageNum=1,pageSize=20,renderType=0` 返回total9，均2026。[raw](../_sources/daily-20251107/hunyuan-page1.json) | 受阻 | fallback不是完整2025 Research“全部”；不重复空初始化，不将失败当无命中 |
| SRC-ZAI | 首查官方Research原生HTML/前端分页，page1 15项、page2累计18项 `hasMore=false`；按展示 `createAt` 而非CMS `createdAt` 识别最早为2025/12。官方release notes日期表9/30与12/08之间无本窗条目。[page2](../_sources/daily-20251107/zai-research-page2.html)、[release](../_sources/daily-20251107/nov07-narrow-tail-core.txt) | 受阻 | Research目录历史截断，release列表无条目不能证明论文无遗漏；停在page2终点 |
| SRC-BYTEDANCE-SEED | 官方GET get_article_list_v2，article_type=1/2、publish_year=2025、count=20、page_token=0/20、order_desc=true、x-tt-locale:US；非pinned page20已到6月或更早，保留has_more/next40和置顶穿插。[type两组raw](../_sources/daily-20251107/seed-papers-page0.json)、[page20](../_sources/daily-20251107/seed-papers-page20.json)、[另一组](../_sources/daily-20251107/seed-blog-page0.json)、[page20](../_sources/daily-20251107/seed-blog-page20.json) | 已检查 | 只支持该API2025日期边界，不以文件名推定type语义或全站无遗漏；未翻全年末尾 |
| SRC-BAIDU-ERNIE | 原生技术Blog两页标题日期边界：11/11 VL-thinking、11/07 leaderboard、10/16 OCR-VL和更早；本窗未见11/06技术条目。[首页](../_sources/daily-20251107/nov07-native3.txt)、[page2末页](../_sources/daily-20251107/nov07-core2.txt) | 已检查 | 11/07榜单未呈独立机制增量，不追无关日期；仅该公开目录检查结果 |
| SRC-XIAOMI-MIMO | Paper8项边界至10/21及更早；实际home前端Blog数组15条、initialVisibleCount8，More是本地slice/toggle而非后端分页。[原页](../_sources/daily-20251107/nov07-native-tail.txt)、[原生边界](../_sources/daily-20251107/TAIL_NECESSARY_NOTES.md) | 受阻 | 有限恢复结束；Blog数组无日期，/blog实际单篇12/16而非历史index。恢复需2025本窗历史目录，不证明无新增 |
| SRC-MINIMAX | 英/中Research Blog实际页12/13边界12/23至10/27，中文另至01/15；Agent Tech Blog official llms索引50行后一次原生md恢复，仅列2026-05-13。[原边界](../_sources/daily-20251107/nov07-native-tail.txt)、[md](../_sources/daily-20251107/minimax-techblog-native.md) | 受阻 | 有限恢复结束，Tech Blog2025历史未恢复；不读未来Agent Team正文或继续猜分页。恢复需原历史技术列表 |
| SRC-ARXIV | 提交恢复区间11/04 19Z～11/05 19Z，三条窄主题query分别4分类21项(start0/max30)、4分类61项(start0/max100)、8分类13项(start0/max50)，响应分页已尽。[topic1](../_sources/daily-20251107/arxiv-topic1.xml)、[topic2](../_sources/daily-20251107/arxiv-topic2.xml)、[topic3](../_sources/daily-20251107/arxiv-topic3.xml)。补检cs.CL月表skip0/show25是1-25/1527、.00010-.00556；cs.CV同参数Cache miss，先前cs.LG25/2000等有限失败已停。[补检raw](../_sources/daily-20251107/nov07-official-title-boundary.txt) | 受阻 | query完整响应不是public窗覆盖；官方本窗batch/相关标题补检无法恢复，逐潜在项只有submitted。月表不作全类题摘/全文队列，恢复需真实本窗公开列表 |
| SRC-MLSYS | SnapStream exact-v1 PDF首面会议模板触发；实际 `site:proceedings.mlsys.org "SnapStream"`、`site:mlsys.org "SnapStream"`，无返回。[查询](../_sources/daily-20251107/nov07-mlsys-trigger-zai-page2.txt) | 受阻 | 未取得正式发表身份，不从模板认定MLSys2025已发表，不扩扫全部会议；正式发表身份不能支持本窗首次公开 |
| SRC-OPENREVIEW | Common-O/UserAlign NeurIPS标注触发，forum/API challenge/403；Entropy ICLR模板精确题名query无返回；Bayesian Evaluation workshop触发一次题名查询，QXYPTeE4gc改题线索forum/PDF challenge。[原触发](../_sources/daily-20251107/nov07-openreview-control-finite.txt)、[Entropy](../_sources/daily-20251107/nov07-openreview-entropy-template.txt)、[新触发](../_sources/daily-20251107/nov07-last-original-bounds.txt) | 受阻 | 不由模板、接收、索引Published或当前PDF推首公开。需要实际public字段/同版身份；停止相同路径，不绕challenge/全扫会议 |

## 3. 候选与判断

尚无已证明完全落窗的家族。所有潜在方向具名放入§5，不先列为确定的本窗候选，不把空表解释为零命中；已完成的有限准入校准复用，未授公开日期或全部潜在项完整Evidence，不报未核的候选分母。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

四项的精确版本、已读位置、反证及 owner 具体差额见 [首批证据与 owner 对照](../_sources/daily-20251107/FIRST_EVIDENCE_OWNER_DELTA.md)。其内容保留作者判断，不授日期/证据或 Books 验收。`TRAIN-GRPO` 当前历史统计段与 batch-only 双层LOO有具体区别；`INFER-KV-CACHE` 的静态消费者 slot/validity 可有局部实现差额。经典控制 attribution/group 条件与现有 Ch32/33 具体论点已有覆盖的可能性已指出；Kimi QAT当前主要是未充分披露的版本事实，不因可部署TensorRT路由框架章。作者不写共享Books。

RAGBoost [v2原撤回声明](https://arxiv.org/abs/2511.03475v2)明确原文不再有效，v1不采用、不评分、不进Books；这不是访问受阻。当前官方同ID的ContextPilot v3/v4是2026重新发布链，不能回填本日，也不写家族始终withdrawn。DS-STAR [原博客](https://research.google/blog/ds-star-a-state-of-the-art-versatile-data-science-agent/)的file analyzer/router与消融有意义，但博客未披露相对更早公开正文的新差额，作为同家族事件去重，不以11/06转载改变归属。两项首校准见[FIRST_CALIBRATION](../_sources/daily-20251107/FIRST_CALIBRATION.md)，新增身份链见[TAIL](../_sources/daily-20251107/TAIL_NECESSARY_NOTES.md)。

新增的选择性题摘初筛见 [TOPIC_SCREENING.md](../_sources/daily-20251107/TOPIC_SCREENING.md)，每项含完整原摘要、原版本/日期字段和具体理由。当前非v1内容不作为本日结论；潜在主线机制、局部负结果和理论/小模型项未因名称、成熟原则、应用标题或摘要缺实验细节自动关闭。

后续有限裁决与必要反侧见[TAIL_NECESSARY_NOTES](../_sources/daily-20251107/TAIL_NECESSARY_NOTES.md)。CBF保证受classifier/非空allowed set限制；Entropy中央符号已核exact-PDF；DCT局部prune不严格无损；Common-O有输入与标注限制，QG-CoC有oracle caption额外调用。新增安全框架的内部judge、modified score及摘要100/表格99冲突必须保留；OptiMA承认real actions不能undo；COMPASS exact HTML/PDF内部日期冲突，保留局部机制但不授public或一般truth保证。均不以本日日期未知展开全实验或请求Books写入。

## 5. 缺口与下一步

普通可执行工作：0。作者有限来源/决定准入已收束，Ohm尾部及Carver来源复核指出的局部事项已同步，Ohm在[DAY记录§6](../_sources/daily-20251107/DAY_INDEPENDENT_REVIEW.md)实际定点回核通过。[作者局部修正](../_sources/daily-20251107/AUTHOR_LOCAL_CORRECTIONS.md)保留修正范围，不要求重扫来源或重读未变题摘/附件。首批、SECOND及两份独立记录各自实际范围复用。没有已落窗项，不请求Books写入；下列明确终态保留项不支持正面证据、Books、无遗漏或性能/安全保证，也不改称Coverage/Evidence通过。仅具体误判、漏项或新原件到达时重开受影响项。作者继续11、12，不维护其他日期ownership。

外部日期/身份保留，不支持正面证据、Books或零遗漏：

- Shrinking [2511.03710v1](https://arxiv.org/abs/2511.03710v1)、Learning [2511.03527v1](https://arxiv.org/abs/2511.03527v1)、SnapStream [2511.03092v1](https://arxiv.org/abs/2511.03092v1)：提交原字段分别为11/05 18:43:15Z、15:01:32Z、00:38:31Z。Atom、DataCite以及[OAI GetRecord](../_sources/daily-20251107/arxiv-03710-oai.xml)不提供需要的首次公开下界，不能只按常规schedule补造精确时刻。最小重开材料为该ID的真实官方历史公开batch与可区分09:00两端的公开证据，或作者首公开正文/公告的上下界完全落窗。停止向其他论文复制空OAI路径，不重试HF元信息或扩扫月表全文。
- Kimi [官方X公告](https://x.com/Kimi_Moonshot/status/1986449512538513505)：官方Blog仅`2025年11月06日`，历史card commit不是first public；论坛created_at为`2025-11-07T03:27:30.356Z`，在窗外。X403、syndication/oEmbed有限恢复失败后停止。仅可读官方公告timestamp或官方首公开正文时间上下界到达时，重开本材料；不利用Snowflake估算替代原证据。
- Common-O/UserAlign：必要更早会议公开身份受到OpenReview challenge/403限制；取得对应note实际公开字段和精确版本后，只恢复本家族去重/归属。会议接收日期、PDF当前可读与submitted不等同public。
- 其余潜在原16项及GraphBSI/Known Invariances/DIIQN/Formal RL、3TF、CoPRIS/AnchorTP/Energy/PCG，以及补漏21项中未关闭方向：每项ID、完整精确题摘、submitted原字段、具体贡献及日期恢复后的最小审阅点在[TAIL具名表](../_sources/daily-20251107/TAIL_NECESSARY_NOTES.md)与其raw引用中。共享缺口是官方本窗first-public batch不可恢复，各自只有submitted，不构成公开证据；最小替代是对应ID官方公告或作者公开正文上下界完全落窗。没有向每项复制空OAI/HF路径。COMPASS另有exact-HTML/PDF内部日期冲突，需要同版原日期证明；Bayesian workshop改题线索另需同版public note。贡献关闭的ScalingEval/SENT/Trust/SVM/Poker等不新增日期请求。
- OpenAI action controls仅原11/06日粒度、时区不明；真实官方首次公告/变更公开上下界完全落窗后，仅恢复当次新增action默认禁用等已校准变更，不回填未来Help版本。
- Hunyuan历史Research“全部”、Z.ai 2025/11以前Research目录：当前原生/浏览器/fallback有限恢复未取得目标时段，不宣称无命中。取得可复查历史目录或原研究事件页时，定点恢复本窗相关切片，不重跑其他月份。
- Google/Meta/Qwen/MiMo/MiniMax尚缺的本窗历史相关目录，以及arXiv本窗官方相关标题补检：§2已列实际有限范围和停止。可接受原历史目录/本窗公开batch到达后只恢复该来源本窗主线切片，不能用无列表或当前目录支持无遗漏。Anthropic传回Research数组及DeepSeek News目标段现已有限检查，不再列作原件不可得；它们仍不保证删除历史/其他未覆盖Research完整性，不支撑全站零事件。

更早家族/窗界不确定线索：DS-STAR既有家族早于11月；DLM作者原仓库声明`2025-10-03`完整论文、`10-27`代码/logs已出，Notion写`Released on Aug 09 2025`，root已裁决当前未识别本窗实质新事件，保留matched-budget方向而不扩扫8/10月。Microsoft Whisper Leak blog原日期11/07时区未核，不计本窗或回填后续mitigation。CoPRIS/AnchorTP等只有submitted，撤销仅凭ID较晚写作late-public/窗外的旧表述，具体日期隔离见上，不扩其他日。

## 6. 复核

复核者：root（首批与SECOND）、Codex / Ohm（尾部与日级及局部回核）、Carver（来源），均非报告作者Noether。Ohm实际局部回核时间：2026-10-04T18:50:11+08:00。

结论：通过

root首批及八方向校准复用[FIRST](../_sources/daily-20251107/FIRST_CALIBRATION.md)、[SECOND](../_sources/daily-20251107/SECOND_INDEPENDENT_REVIEW.md)。Ohm实际2026-10-04T18:26:30+08:00的[DAY_INDEPENDENT_REVIEW](../_sources/daily-20251107/DAY_INDEPENDENT_REVIEW.md)核37项tail完整题摘、另12项及Capability样本、六类关闭样本与必要中央反侧；Carver实际18:23:26的[SOURCE_INDEPENDENT_REVIEW](../_sources/daily-20251107/SOURCE_INDEPENDENT_REVIEW.md)核三份Atom、四份Seed及具名原生目录/停止范围，并在末段收窄已由Ohm完成的普通范围。Ohm于18:50:11在DAY记录§6实际核作者局部修正与正式六部分：两处引用、native有限检查、Bayesian命题、反馈主体和ownership均通过，普通0、无确定候选和Books实际0成立，允许同步完成态。未核全部潜在methods/附件、代码执行、复现、全站或月表；日期、完整Evidence、Books整合仍不授予。作者同步不是自审，未重复37题摘。

本次完成态V3格式/可判定一致性校验exit0；限定07/08目录git diff --check无输出。本轮07 README/CURRENT_STOP两份作者文件62个本地引用无缺失，代码块/行尾空白及逐文件no-index空白检查无诊断；08完成态也单独重跑V3通过，两份作者文件28个本地引用无缺失。较早9个Markdown/153引用仅为当时快照。原站下载md的`/docs/techblog/agent-team`是网站相对href，不作本地文件链接或未来正文已读声明。机器检查不代替上述非作者语义复核。
