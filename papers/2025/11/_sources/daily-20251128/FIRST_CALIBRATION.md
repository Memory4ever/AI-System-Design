# Nov28 首批准入校准包

窗口 BJT `[2025-11-27 09:00, 2025-11-28 09:00)`，UTC `[2025-11-27 01:00, 2025-11-28 01:00)`。作者 Aristotle；首批准备时间以本日 receipts 的 2026-10-04T10:48:57～10:49:13Z 为实际抓取范围。root 接29，作者只继续27/28，不启动29。

本日 fresh 四窄 arXiv 查询返回27/7/12/12，共58次返回、按无版本 ID 去重55家族，均 start0/max50/短页停止。关键词与词干匹配只提供发现，不保证主题语义、贡献或公告归属；submitted区间只是发现索引。本首批只读8篇完整精确v1题摘，不把55条都送入全文审阅。原始参数与完整返回分别保存在 `arxiv-*-query.json`，不是已审55项的声明。

## 首批潜在贡献与采用边界

| 原始精确v1与本地原页 | 具体准入理由，非正文证实 | 日期恢复与边界 |
| --- | --- | --- |
| [MLPMoE](https://arxiv.org/abs/2511.21089v1)，[raw](abs-2511.21089v1.html) | dense FFN始终计算全部分支 → 无训练张量切分/求和，再加Fractal Fade与方差补偿剪枝 → 可重新考虑checkpoint后处理的稀疏化与是否真的节省执行成本。静态expert名称本身不表示token路由MoE或加速；proxy perplexity与参数20%减少待必要对照。Owner候选MODEL-FFN/MODEL-MOE，不能名字缺位造Books缺口。 | [原字段](date-2511.21089.json)：Submitted v1 `2025-11-26T06:14:26Z`；Updated v1 `2025-11-27T01:27:03Z`；created `02:50:11Z`、registered `02:50:12Z`；Available `2025-11`。后3类仅元数据处理/月份，不证明首次公开上下界。 |
| [Non-Monotonic ViT Scaling](https://arxiv.org/abs/2511.21635v1)，[raw](abs-2511.21635v1.html) | 加深ViT不保证收益 → ImageNet三规模层内cliff/plateau/climb与CLS边缘化、信息混合诊断 → 可检验depth/representation非单调的局部反证。不将相关层变化归因普遍scaling定律。 | [字段](date-2511.21635.json)：Submitted `2025-11-26T18:07:14Z`；Updated `2025-11-27T02:02:03Z`；Available `2025-11`。公开日期未确认。 |
| [Subjective Depth and Timescale](https://arxiv.org/abs/2511.21408v1)，[raw](abs-2511.21408v1.html) | uniform逐层逐token计算 → Bayesian surprise的固定容量Top-K深度路由，以及预测residual的时间跳层/KV参与 → 可改变compute graph与历史状态选择。75%attention/50%KV仅每skip层，不外推端到端。 | [字段](date-2511.21408.json)：Submitted `2025-11-26T14:00:18Z`；Updated `2025-11-27T01:49:34Z`；Available `2025-11`。日期未确认。 |
| [DOPD v1原题](https://arxiv.org/abs/2511.20982v1)，[raw](abs-2511.20982v1.html) | 静态PD比例受混合长度producer/consumer失衡 → 动态比例分配、request scheduling与历史负载预重配置 → 可改变SLO goodput资源策略。1.5x/99%是作者摘要主张，待预算、配置、SLO及重配置代价。 | [字段](date-2511.20982.json)：Submitted `2025-11-26T02:27:10Z`；Updated `2025-11-27T01:17:13Z`；v2提交Nov28、v3 2026不借用；Available `2025-11`。精确v1标题不含后版DOPD前缀。 |
| [TraceGen](https://arxiv.org/abs/2511.21690v1)，[raw](abs-2511.21690v1.html) | pixel world model跨embodiment昂贵且外观不稳 → 统一几何3D trace未来轨迹与视频转trace的数据管线 → 可检验表示压缩、跨embodiment可迁移条件。4任务/5视频/50–600x限作者条件，不能全任务模型优越。 | [字段](date-2511.21690.json)：Submitted `2025-11-26T18:59:55Z`；Updated `2025-11-27T02:04:27Z`；Available `2025-11`。需要真实作者公告而非常规schedule补时刻。 |
| [KRISP轻量复现](https://arxiv.org/abs/2511.20795v1)，[raw](abs-2511.20795v1.html) | 工业规模KG-VQA不能直接代表低资源设置 → 合成VQA/DAQUAR缩小模型的消融、隐含pitfalls → 可继续局部反侧核验，不因复现/benchmark关闭。摘要“prevents hallucinations”不采用：受限输出域不证明事实真。 | [字段](date-2511.20795.json)：Submitted `2025-11-25T19:37:19Z`；Updated `2025-11-27T01:04:09Z`；Available `2025-11`。目前潜力而非已确定窗内家族。 |
| [Structured Prompting v1原题](https://arxiv.org/abs/2511.20836v1)，[raw](abs-2511.20836v1.html) | 固定prompt可能误排能力 → 4LM/7benchmark中结构prompt/推理造成3/7排名变化 → 可修正eval protocol归因。不能将可优化prompt的观察最大值称数学ceiling；医学应用不借入，采用仅通用评价混杂。 | [字段](date-2511.20836.json)：Submitted `2025-11-25T20:37:59Z`；Updated `2025-11-27T01:06:38Z`；v2Nov28/v3 2026不移入本日；Available `2025-11`。题名不同于当前v3已明确隔离。 |
| [Multi-Prefix Leakage](https://arxiv.org/abs/2511.20799v1)，[raw](abs-2511.20799v1.html) | 单一路径提取不能代表aligned模型记忆 → 外部对抗搜索达目标数量distinct prefixes，量化多路径可恢复性 → 可修正privacy审计的阴性解释；positive/negative定义、搜索预算、aligned对照必要深入。 | [字段](date-2511.20799.json)：Submitted `2025-11-25T19:40:24Z`；Updated `2025-11-27T01:04:17Z`；Available `2025-11`。安全受影响内容仍有限核，不扩大所有正文。 |

## 代表性范围关闭与尚待摘要

仅标题明确范围关闭：`2511.21500` Physiological Signal Transformation、`2511.21034` Dairy Cow Herd Life、`2511.20956` Breast Ultrasound Reports，属于ROADMAP暂缓科学/临床应用；`2512.07865` Swedish Register Mobility、`2511.21364` Bangla Disaster分类仅领域既有Transformer应用，标题无通用机制与安全纠错信号。只记范围理由，不称完整摘要审阅，也不为不影响处置的日期追加恢复。

Remote Sensing Co-Training、Radar Scene、Mortgage residual/routing、ASR phonetic、Martin's Law、Orthographic Difficulty等标题可能有通用机制，尚未读精确v1完整摘要，不按应用标签直接关闭。其余相关模型/系统/Agent题摘普通继续，不预授准入或日期。

## 当前普通停点

首批8项请root独立校准：重点MLPMoE代数等价/稀疏差额、KRISP局部反侧与幻觉主张、Structured Prompting评价混杂、Multi-Prefix安全定义，以及原日期字段不能充当public。

实际时区公告边界用官方规则只作发现，不能把Submitted或Updated写public。有限命名搜索已执行MLPMoE/TraceGen/StructuredPrompt/DOPD各一次；所得索引多数仍提交标签、晚出版/晚poster，不能确认当窗。有真实官方公告/首公开上下界完全落窗才采用；缺日期不因abstract没有实验细节关闭，不扩55全文。

本日原始源已抓：OpenAI RSS1245带日期item本窗无命中，Anthropic NextFlight172 dated posts相邻Nov25 11:05Z→Dec1 00Z；只恢复当前目录，不声称无删除。Hunyuan实际浏览器“全部”11项为2026-02-03→09-22，能打开但2025仍未恢复，不继承别日浏览器失败。Google pubs/blog与Meta本次12秒有限失败，补入口只处理该受阻部分。Seed own p0/p20的pinned/has_more/next保留，DA3 raw日期Nov26 16Z在本窗之前；无需借别日判为新家族。此段为首批时停点，后续实际进度见下，不继续把已完成作者整理列普通待办。共享Books/index/state均不写。

## 最新作者停点（2026-10-04T19:28:14+08:00）

已继续全部相关精确v1完整题摘、有限原字段/具名作者日期恢复与必要安全/设计反侧，见[BOUNDED](./BOUNDED_CANDIDATE_FINDINGS.md)、[SOURCE_CHECK](./SOURCE_CHECK.md)及[正式六部分](../../28/README.md)。55窄发现+5相关DC+1本日DeepSeek Math-V2=61身份；五标题范围停止，56完整v1题摘，五题摘后关闭，51潜力日期隔离，确定落窗候选0。DeepSeek本日真实Research/news已核，不能用API updates代目录。DeepMind page5 native200，page4原生失败由web恢复，Google pubs仍受阻；MiniMax原Tech Markdown只2026May，MiMo More真实button。

作者来源/题摘/必要受影响反侧普通整理已结束；首批与最新有限包请root非作者校准/日级，状态仍进行中。机器V3/本地引用/空白/代码块/限定diff已实际检查，不授语义通过。51潜力不是51份深审或未来全附件队列，必要日期到达只定点重开；Books实际0、不授Existing/正面采用。作者转29非作者首批/DAY，不改29作者正文或共享state/index。

恢复时钟2026-10-04T19:49:37+08:00：fresh实际重读适用合同、Sources使用/每日/按需/arXiv、Prompt、ROADMAP、最新checkpoint及28本日停点/六部分；有效原源与判断未变，不重扫56题摘/51方法。作者普通余项仅非作者校准/DAY及通过后的作者同步。最新4份MD45本地引用无缺文件/空白/代码块问题，V3退出0，限定diff-check无输出；原MiniMax索引52物理行已修，不动raw或Books。这里仍不授日级通过。

## 完成态窄同步与Planck变化回核入口

2026-10-04T20:35:05+08:00：fresh重读适用合同/来源/Prompt/ROADMAP及28停点、正式报告和Planck最新独立记录。用户传递root20:07的56完整精确v1题摘/12必要核心通过，Planck20:30:22原记录已明确来源/六部分与完整DAY分工通过。作者只同步README metadata与§1/4/5/6汇总，§2及SOURCE_CHECK的MiMo控件停止说明；没有新候选、评分、日期授权或Books写入。

MiMo本日[原JS](PLANCK_RAW_MIMO_NATIVE.js)实际回读：moreBlogs/aria展开态绑定h，onClick仅u(e=>!e)，p.map渲染已返回列表；More/Show less为本地toggle，不分页/补日期，无More普通待办。十五Blog日期历史缺段仍受阻。请Planck只回核这项及上述完成态/普通0/§6分工引用变化，不重复56题摘、12核心或全部methods；其原独立notes由Planck自己更新，作者不代写确认。完成态机器检查接下实际执行，不将机器通过等同语义完成。

2026-10-04T20:37:26+08:00实际检查：完成态V3退出0；本日四份作者Markdown/51本地引用，缺文件、空白、代码块问题0；限定diff-check无输出。目录未跟踪，直接字节检查不由空diff替代。共享Books/state/index及公共合同未改，未stage、commit、push。上述机器结果不代替Planck的变化确认或root最终验收/count。
