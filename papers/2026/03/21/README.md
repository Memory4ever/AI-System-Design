# Daily Research — 2026-03-21

**规范：** V3
**窗口：** 2026-03-20T09:00:00+08:00 ～ 2026-03-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T03:26:52+08:00

## 1. 结论

本窗确定候选 **0 家族**、完成证据审阅 **0**、Books 新增 **0**。有限来源恢复中读完两项具名潜在贡献的完整题摘：FlexTrain 的 PP/DP 弹性一致性分支，MixedDimKV 的逐 token 维度预算与同 head 信息对照。root 已实际独立校准这两项准入增量，但首公开不能完整落窗，均隔离于 §5；摘要数字不是效果证明，不评分、不作 Books 判断。

十四个每日来源已做到实际有限停止；四主题 arXiv 邻接元数据已回收，不把宽库、157 次重叠查询返回或旧日报库存变成逐项题摘/全文队列。官方常规公告没有 Friday/Saturday slot：上一个 Thursday 20:00 EDT 对应 03/20 08:00 BJT（左界前），下一个 Sunday 对应 03/23 08:00（窗外）。这只约束常规 arXiv 事件，不证明作者原发或其他机构没有研究。root最终非作者日 Gate已实际通过，普通待办0；2 项日期及 5 组来源限制是安全隔离而非 Evidence/Coverage 通过。

## 2. 来源覆盖

实际查询、分页/停止与字段见[有限发现](../_sources/daily-20260321/V3_FINITE_DISCOVERY_STOP.md)、[公开目录原字段](../_sources/daily-20260321/V3_PUBLIC_DIRECTORY_FIELDS.json)、[混元原字段](../_sources/daily-20260321/V3_HUNYUAN_FIELDS.json)。复用其他日相同身份原始字段只另判本窗，不继承其筛选或完成结论。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [公开 RSS](https://openai.com/news/rss.xml) 实际 1242 条元数据，限定 UTC03/19–22 邻接返回两条 03/19（coding monitor10:00GMT、Astral00:00GMT），均早于左界；不将精选 Research 当历史全目录。 | 已检查 | 仅该公开 RSS 有限范围，不授机构全量无遗漏。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 当前最新10；定点复用[17实际 Sanity March9原字段](../_sources/daily-20260317/V3_WORKING_STOPPOINT.md)，03/13→03/23跨本窗，9条中没有03/20–21；包含03/23三条及03/24、31，不以最新10替代恢复。 | 已检查 | 仅可见 Research，不外推全部 News/删除项。 |
| SRC-GOOGLE-AI | [Research March page1](https://research.google/blog/?year=2026&month=3)12卡03/17→24；page2失败后定点复用[实际page2/2两原卡](../_sources/daily-20260305/V3_OFFICIAL_RECOVERY_12.md)03/06、04；[DeepMind Blog page3](https://deepmind.google/blog/?page=3)24卡、6个March标题原header为03/03、10、17、25、26，均窗外。Research精选8不作全目录。[Pubs](https://research.google/pubs/)1–15/11569，2026年372条只有年排序；year过滤失败。 | 受阻 | Blog有限可闭合；Pubs本窗主题原发slice不可恢复，见§5。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空、Publication结果失败；[Blog](https://ai.meta.com/blog/)page1十/page2十二卡非日期严格排序，03/11→26/27跨本窗，无本窗可见卡，停止page2。 | 受阻 | Publication本窗主题历史slice，Blog有限范围不替代。 |
| SRC-QWEN | [官方](https://qwen.ai/)公开retrieval 40条，data只有articles，无total/分页字段；extra.date 03/19T04+08→03/30跨窗，返回40无相交。仅title/path/date，不展开body。 | 已检查 | display日期非全部首公开或删除历史保证。 |
| SRC-DEEPSEEK | [en/news](https://www.deepseek.com/en/news/)render Research10/News5；复用[17实际完整Next posts16/Research数组及公开脚本](../_sources/daily-20260317/V3_WORKING_STOPPOINT.md)，News2026Apr24/Sep10，Research2026Feb25→Jun24跨窗；hidden已恢复，未见本窗数组条目。 | 已检查 | 仅实际数组，不把render5当全历史或全机构无研究。 |
| SRC-MOONSHOT | [Kimi官方Blog](https://www.kimi.com/en/blog)19卡，2026Feb9→Apr20跨窗，当前Jul16→2024Jun；未见本窗条目。旧platform止2025不用于2026缺失判断。 | 已检查 | 有限可见目录，不授删除项/全机构召回。 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)动态失败后[生产publicList](https://api.hunyuan.tencent.com/api/blog/publicList) POST pageNum1/pageSize20/renderType0、accept-language zh，442610B、code0、total11/返回11。display2/13→4/23跨窗，无March。zh-CN首次English9不作为中文完整依据。 | 已检查 | publicAt/publishedAt/update区别保留；仅当前11目录，不外推删除历史。 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)15卡175行，03/15Turbo→04/01跨窗，无03/20–21可见条目；不扩大查看更多库。 | 已检查 | 当前有限目录，不授全机构历史。 |
| SRC-BYTEDANCE-SEED | [Research/Pubs](https://seed.bytedance.com/en/research)当前5Blog/10精选与20/242不能代历史。官方type1 year2026/token20/count100/order_descfalse、localeUS实际18/82、next40/has_moretrue，03/16→20FlexTrain→21MixedDimKV→23/24跨窗；两项完整题摘/原身份另核。type2 token0同参数14/19、next空/false，02/16→04/01跨窗。 | 受阻 | 两日期线索及Blog未返回5条的身份/日期不可确定，§5分别隔离；后续update不反填。 |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/)10卡68行，02/06→04/15跨窗，无03/20–21可见条目；停止page1，旧Next2/2不扩全年。 | 已检查 | 有限可见目录不授全站无遗漏。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper8，03/13→06/29跨窗；Blog15无日期。后续定点恢复正确[Pro](https://mimo.xiaomi.com/mimo-v2-pro)/[Omni](https://mimo.xiaomi.com/mimo-v2-omni)原页，time day2026-03-18不与本窗相交；[实际原字段](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)。错误/blog壳不作为必要正文缺口。 | 受阻 | 只本窗dated Blog历史slice，不再请求已恢复两正文，不猜TTS route。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)12卡03/18→05/26、[中文Blog](https://www.minimaxi.com/blog)redirect.cn实际13卡03/18→04/27跨窗，中文不是不可读壳。Forge英文02/14、中文02/12均窗外。[AgentTech .md](https://agent.minimax.io/docs/techblog.md)后续GET880B恢复完整可见列表，只May13AgentTeam窗外；[实际停止](../_sources/daily-20260319/V3_SOURCE_STOPPOINTS.md)。 | 受阻 | 主Blog与可见.md有限闭合；只AgentTech本窗历史dated slice，不以当前指南或May记录证明历史无遗漏。 |
| SRC-ARXIV | [官方availability](https://info.arxiv.org/help/availability.html)无Fri/Sat公告；[API](https://export.arxiv.org/api/query)四主题Submitted邻接03/20T01Z→21T01Z，start0/max50/ascending，systems50/75、learning45/45、multimodal12/12、agent_eval50/77，重合不相加；最早常规公告03/23窗外。[monthly](https://arxiv.org/list/cs.CL/2026-03?skip=0&show=25)仅2138中月首1–25，不是本窗日历史；停止不扩月。 | 已检查 | 不证明作者更早原发/非常规事件不存在，不把API published作公告时刻。 |

一次官方域精确日期/标题补检（MiMo、Anthropic、Google March20及Seed FlexTrain）未返回，是有限检索结果，不授权“无命中”覆盖。未触发每周来源或全会议扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无能够确认首公开完整落窗的确定候选。两项潜在贡献只在 §5 请求一次，不先进入候选表或评分。

## 4. 证据与知识整合

无本窗候选的标准/深入证据审阅、Books采用或写入。两项完整题摘、精确身份/日期及准入判断见[PRIMARY_ADMISSION](../_sources/daily-20260321/V3_PRIMARY_ADMISSION.md)。FlexTrain 摘要不能证明一致性/性能；MixedDimKV 摘要不能证明压缩收益或运行成本。潜在owner分别为TRAIN-PIPELINE-PARALLEL/TRAIN-DISTRIBUTED-TRAINING、INFER-KV-CACHE，仅作恢复路由，不以owner映射代替贡献/已有覆盖审阅。

有限monthly查漏样本2603.00022（BERT临床实体提取，传统NLP应用）与2603.00612（biomarker药物组合AI co-scientist，暂缓AIforScience）仅标题足够明确范围，未读完整题摘、未做贡献/实验判断；不称本窗新论文或已审候选。旧报告完整[快照](../_sources/daily-20260321/V3_LEGACY_REPORT_SNAPSHOT.md)及有效原raw保留；旧候选/9分/EffectiveDate/全库存审/完成标签不继承。

## 5. 缺口与下一步

普通可执行待办：0。root最终非作者日 Gate已实际通过，作者查询/筛选/报告同步完成，无进行中的长工具。以下为本窗外部终态保留项，不支持正面证据、Books或无遗漏断言；以后只按具体条件重开受影响材料。

- **FlexTrain / OpenReview h2yhNcbwSL**：[原PDF](https://openreview.net/pdf?id=h2yhNcbwSL)不可读，forum/attachment browser challenge；作者public api2 notes HTTP403，root独立api2 web InternalError分别保留。Seed PublishDate1773936000000为03/20日级相交，UpdateTime是后续更新，索引5monthsago非首公开。需要同identity公开原note/cdate/tcdate与first-public/version说明，或作者可靠原文首公开记录；只有范围完全落窗才重开PP/DP一致性分支与controller必要审阅，不采用1.73x/2.27x。
- **MixedDimKV / 2603.20616v1**：[官方abs/history](https://arxiv.org/abs/2603.20616v1)实际v1 Submitted Sat21Mar03:21:43UTC，即BJT11:21:43，已在09右端后，因此该arXiv事件窗外。Seed ID1407/ArticleID1776932180702 PublishDate1774022400000为03/21日级相交、UpdateTime后续；可能另一作者原发，不能把family直接关闭或假造零点。一次exact-title作者/项目原发补检仅索引未取到可靠日期；需要作者/Seed原文可靠首公开和精确版本，范围完整落窗才审维度预算及same-head对照，否则按真实窗外归属。先前“仅FlexTrain相交”已具名补正。
- **Google Research Pubs**：[当前出版库](https://research.google/pubs/)只有年份、year过滤失败；需要03/20 09至21 09主题相关原始发布slice或具体dated原event，Blog已恢复范围不能替代。收到后只核该slice。
- **Meta / FAIR Publication**：[Research](https://ai.meta.com/research/)空/Publication结果失败；需本窗相关出版/原发slice或具名原始报告，Blog1/2有限检查不替代。到达只核受影响记录。
- **Seed Blog差额**：type2实际14/total19而next空/false；缺5条身份与日期，需同参数可解释的完整响应或本窗dated Blogslice/具名原记录；不猜语言、删除或该5必在本窗，不扩全部论文库。
- **MiMo Blog历史切片**：[首页](https://mimo.xiaomi.com/)15undated仍不能恢复本窗历史；正确Pro/Omni正文已恢复、March18日字段窗前，不再请求相同正文或把误/blog路由失败当阻塞。需本窗主题dated列表或具名原发布字段，只重开相应切片、不追全15附件。
- **MiniMax AgentTech历史切片**：[.md](https://agent.minimax.io/docs/techblog.md)已实际GET880B恢复，只May13dated条目窗外，不再请求已恢复正文。需本窗dated主题历史slice或具名原发布日期；主中英文Blog已有限恢复，不以当前指南或May记录代替历史。

不属于本窗的arXiv邻接submitted条目和MixedDimKV arXiv事件只保留真实归属线索，不在这里启动窗外全文/Books工作。

## 6. 复核

复核者：root（非报告作者）
结论：通过

root已实际完整读本日正式六部分、FINITE_DISCOVERY_STOP、两项PRIMARY，并核MixedDimKV exact-v1完整题摘/history及OpenReview notesApi2实际失败；两潜在增量、14源有限范围/查询停点、0确定候选/0Books、2日期+5来源隔离已非作者日级验收通过。发现旧“唯一FlexTrain”及1材料计数后已补正为两项，保留误漏过程，不以Submitted排除整family其他原发。未授效果/Books，不称全部四主题元数据、目录body或附件经非作者全审。

完成态V3机器校验PASS，5份本日Markdown的本地引用无缺失、3份JSON可解析，限定git diff --check无输出；通过只能证明格式/一致性，不能替代上述语义Gate。无Books写入待POST，未stage、commit或push。
