# Sep20 14每日源本轮独立检查

作者Meitner，2026-10-12 BJT执行；新窗2025-09-19完整自然日。`SUP_*.request.json`逐请求时间/URL/状态/bytes/SHA对应raw；不覆盖旧FETCH原件、不继承旧数值。当前页/失败/搜索空均不证明历史无事件，不扩Weekly、全类别、月库存。

| ID | 本日实际入口与停止 | 结果/缺口 |
| --- | --- | --- |
| SRC-OPENAI | Research403，RSS200实际1287items；Sep22到Sep17日期序列夹日，0明确Sep19项 | 已检查RSS有限切片；不授全站删除/修订史 |
| SRC-ANTHROPIC | Research200 Next实际177datedobjects/174unique slug，Sep15两个时点和Sep5低于下界 | 已检查有限目录0Sep19；不扩所有正文 |
| SRC-GOOGLE-AI | Pubs000/Blog000含retry；web原始`https://research.google/blog/2025/09/`实际page1十二题名/日期至Sep11，Sep19仅TTD-DR，reuse同日旧有效必要core事件C；DeepMind当前200但2026目录，严格Sep19域搜索无可靠历史 | 受阻：Blog切片已恢复，Pubs/DeepMind历史未完整；无all-site0 |
| SRC-META-AI | Research000reset；严格官方Sep19主题补检无可靠归档 | 受阻：目标历史列表，不称0事件 |
| SRC-QWEN | 本日code-only page_config200 JSON60；实际日期Sep10Next和Sep21TTS/Omni、Sep22ImageEdit/Guard/VL等跨本日，0Sep19 | 已检查原60有限日期切片；不加language、不扩60正文 |
| SRC-DEEPSEEK | main200只当前；API updates200，Sep29/Sep22/Aug21跨下界停止 | 已检查ChangeLog有限切片；非全仓release/论文 |
| SRC-MOONSHOT | Blog200，实际Sep16/Sep5/Aug22跨下界停止 | 已检查Blog有限切片；非组织全仓历史 |
| SRC-TENCENT-HUNYUAN | Research200壳；按其正确publicList POST pageNum1/pageSize100/renderType0，200原9，最早displayPublishTime1770090898为2026；动态字段已提取 | 受阻：2025历史未恢复，9当前不等九月0，不扩正文 |
| SRC-ZAI | own page2 next18无序minDec7/hasMorefalse，notes200实际只至Sep30 GLM4.6，未见旧Aug11夹窗 | 受阻：Research九月/notes更早段未恢复，不继承旧lowerbound |
| SRC-BYTEDANCE-SEED | Blogtype2/year2025/token0 count20实际15/total49，hasMoretrue/next20；置顶分开，nonpinned Oct22后Aug20/Aug13/Jul30/23/21/14跨下界停止；papers type1 own0/20/40/60/80，total94，0/40/60缺item，20仅SwiftSpecJune11，80hasMorefalse | 受阻：Blog有限片跨窗，论文历史稀疏缺段；不授94已读/全49全文 |
| SRC-BAIDU-ERNIE | page1/2 own200 listing无date；定点PLAS/FastDeploy2.0两detail own200，实际日期Sep12/Aug14，标题/核心/日期已读，可为page2跨下界锚 | 已检查有限Blog停止；不凭无字段继承旧日期，不授全仓修订 |
| SRC-XIAOMI-MIMO | main200 Paper8含Sep19MiMo-Audio；ownruntime与8557/6159 chunk匹配，Blog完整15标题/description但无date；仅Paper具名MiMo触发Demo/GitHub及固定Sep19README | 受阻（历史Blog date缺口）；Paper具名Sep19event独核通过，原小时首次公开hold不继承；不扩15正文/Decemberpaper |
| SRC-MINIMAX | US12当前minOct27，CN13minJan15跨下界；Agent3条2026Oct8/Sep22/Sep19，非旧May一条 | 已检查CN有限slice；Agent当前不授九月历史、非全站修订 |
| SRC-ARXIV | 4主题组/12分类按submitted Sep18T16→19T16Z仅发现代理，start0/max200分别198/8/3/50，均末页无overflow；归并219身份，实际标题有界选择128完整v1AB/current。旧65有效题摘/core分层复用；新8旧title漏排各实际AB/current，另3明确范围title不扩 | 受阻：submitted非public；own new?date/pastweek?date各200却返回2026Oct9/Oct5–9，下述精确隔离；不catchup/全月 |

## Google web原始切片记录

本日web实际读取官方[九月月路径](https://research.google/blog/2025/09/) page1（curl失败原件仍存），十二条日期顺序：Sep30两条、Sep25、Sep24、Sep23、Sep19 TTD-DR、Sep18、Sep17、Sep16、Sep12、Sep11两条。已低于Sep19；不翻page2。主题title中科学应用不入正文；Sep19唯一相关TTD-DR按同日旧有效精确July机制/core关闭本次再阐述，非旧论文无贡献。错误`/blog/archive/2025/09/`web失败另保留为本记录，正确路径恢复不抹去失败。web为原始官方页面读取，搜索结果不作正文。

## arXiv有限公开日门与精确保留

Own`SUP_PUBLIC_DATE_LIST/ANNOUNCE.raw/request.json`分别请求官方CL new与pastweek，均带目标2025-09-19，但响应标题明确2026Oct9和Oct5–9。只读页头判断参数未提供历史，不审2026题摘、不翻历史月库存。已有exactv1/current的history日期是Submitted，四主题Atom published亦不替公告。旧65此前官方月/new恢复失败的日期门可复用其真实限制，不授全Coverage；新128与8title恢复同样缺足以落窗的官方public-date字段。

本轮P身份在[首40](./SUP_FIRST_20261012.md)/[后88](./SUP_SCREEN_20261012.md)逐ID列；旧8差额在[Cicero§2–3](./SUP_INDEPENDENT_20261011.md)。P清楚仅date未证的终态请求为目标身份精确v1官方首发公告/作者原始公开发布日或支持完全落窗的原始artifact。到达仅重开该家族的日期与必要证据，不移旧候选、不给 Submitted 补造时刻。C/A/W已可关闭不另追日期；15695撤回/恢复状态冲突另R，须官方状态说明才重开采用。

Historical source精确保留：Google Pubs/DeepMind、Meta、Hunyuan2025、ZAI九月和Seed论文缺段、MiMo无date Blog。所需官方窗口归档/带真实published date及分页边界的历史API到达后只重开对应源，不支持候选/Books/无遗漏。来源/筛选/必要core已处理，Cicero六部分内容PRE与音频逐字PRE实际通过；MiMo真实Books gap按root窄锁已写入一段+自身SF且Cicero§10非writerPOST通过，锁已释放。普通仅完整六部分DAY/完成态FINAL，不归外部，也未借外部日期保留项跳过Books。
