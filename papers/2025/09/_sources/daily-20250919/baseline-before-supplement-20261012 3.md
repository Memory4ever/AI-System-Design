# Daily Research — 2025-09-19

**规范：** V3
**窗口：** 2025-09-18T09:00:00+08:00 ～ 2025-09-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T19:59:25+08:00

## 1. 结论

本日有界发现与非作者查漏取得68篇精确v1完整题摘（作者17推荐身份恢复＋48月段语义查漏；独核补3个原月段含糊标题），必要反侧补读后63篇贡献潜力、5篇具体关闭；这些不是68当窗新事件，更不是全文证据完成数。另有MiMo-Audio官方先发潜力，其9月最早README已恢复，但公开上界尚未确认。确认落窗并准入的正式候选0、相应证据完成0、Books实际写入0；不能据此称零事件或无遗漏。

值得保留的局部线索包括MCQA空格token边界改变排名、语言概率不能代理语法知识、语音quantizer数量的声学/语言取舍、题面捷径混淆幻觉自觉、多模态攻击不一定强于文本攻击，以及奖励分布匹配/无标签探索、value-awareKV压缩等具体机制。均待日期与独立准入，未作性能/安全正面结论。Google三条再阐述/收录事件经本日原核心与精确题摘拟关闭，不声称其原研究无价值或已审完成。

非作者已完成独立首批、必要误排/风险反侧、来源有限停止和日级验收；保留项仅为明确外部日期/历史缺段。Books判断纳入本次，无可采用候选，不作已有覆盖声明。详见[原请求](../_sources/daily-20250919/FETCH.md)、[具体初筛](../_sources/daily-20250919/FIRST_BATCH.md)、[作者差额](../_sources/daily-20250919/NARROW_SOURCE_SAFETY_HANDOFF.md)、[非作者独立验收](../_sources/daily-20250919/INDEPENDENT_DAY_REVIEW.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research403→官方[RSS](https://openai.com/news/rss.xml)2001247条，原GMT pubDate本窗UTC18日01～19日01过滤无匹配；原openai-rss.raw | 已检查 | 仅该RSS公开记录，不授全站无遗漏 |
| SRC-ANTHROPIC | Research200 Nextpublication172唯一，publishedOn原值本窗无匹配；anthropic.raw | 已检查 | 日期精度不能替尚未列出事件授全站覆盖 |
| SRC-GOOGLE-AI | 三curl8秒超时→web真实[2025/09月页](https://research.google/blog/2025/09/)12条至09/11；Sensible/TTD核心及DIVEpublication、v1完整题摘本日读；独核旧TTD方法/同结果局部去重；DeepMind当前与Sep18限定检索 | 受阻 | 月页有限处理，DeepMind历史切片不完整；三本次再阐述关闭通过，不授原研究深审 |
| SRC-META-AI | Researchreset35，primary域名Sep18限定检索空；19finalrecovery原结果 | 受阻 | 历史目录未恢复，不把搜索空结果当零事件 |
| SRC-QWEN | 原Blog切片加本日独立page_config研究API单次20秒HTTP200/57428bytes；60原date配置只筛UTC18T01→19T01，0命中，NextSep10T20Z/TTS21T20Z夹窗 | 已检查 | 原qwen-config-recovery.raw；仅此Research保留切片，不借别日coverage或遍历60篇全文，不授全站无遗漏 |
| SRC-DEEPSEEK | 官网及正确[API更新日志](https://api-docs.deepseek.com/updates/)200，实际Sep29→Sep22→Aug21连续正文跨下界；deepseek-updates.raw | 已检查 | 更新日志不等于所有研究完整历史 |
| SRC-MOONSHOT | Kimi Blog200列表Nov→Sep16→Sep5跨下界；kimi.raw | 已检查 | 所读Blog有限停点，不授所有GitHub事件 |
| SRC-TENCENT-HUNYUAN | Research200shell；正确publicList POST page1,size100,renderType0返回totalNum9，最早2026年；hunyuan-api.raw | 受阻 | 历史2025目录缺失；browser技术路由失败不能将当前9条授覆盖 |
| SRC-ZAI | Research/page2结构18项hasMorefalse，未排序实际min2025-12-07T16Z；zai-page2.raw | 受阻 | 当前末页未到历史窗，需要2025目录/原公告恢复 |
| SRC-BYTEDANCE-SEED | Research/Papers及2025type2 API200，15/49，非置顶Oct→Aug→Jul跨下界，hasMoretrue,next20停止；type1真实执行0/20/40/60/80，80 has_more=false停止，20仅SwiftSpec06/12，0/40/60缺列表 | 受阻 | Blog有限停点已处理；论文total94仍不完整，不能记0或读完94；原分页响应及执行时间见差额 |
| SRC-BAIDU-ERNIE | 首页及page2均200，9/12PLAS→8/14FastDeploy跨下界停止 | 已检查 | 只该Blog目录 |
| SRC-XIAOMI-MIMO | 官网Paper8条，Sep19Audio相交日期→Jun4；正确官方GitHub/Blog核心及最早README/API恢复；本日官方runtime+8557/6159完整Blog15题名/描述，More同数组8+7，无后续网络页 | 受阻 | Sep19原字段无TZ、commit不等公开；9月精确artifact已取但公开上界未证，当前Blog15均无date，不授2025历史覆盖 |
| SRC-MINIMAX | 三入口200；英文12最早Oct27，中文13含Jan15跨下界无本窗条目，AgentTechBlog2026单条 | 已检查 | 中文有限历史列表有效，不授完整历史或仅英文页覆盖 |
| SRC-ARXIV | 12分类主题datequery20秒超时；系统API10秒超时；历史new参数部分返回未得历史头；CL月两次部分正文；实际ID14500～15500完整62标题语义补查 | 受阻 | 无本窗原公告，65v1题摘仅贡献/身份；提交字段不授首次公开 |
| 补检：[HF Papers](https://huggingface.co/papers/date/2025-09-19) | 本日arXiv失败触发19标题身份恢复，17相关v1、两明确领域标题关闭；19recovery/19hfidentities | 已检查 | 推荐/索引published不是first-public |
| 表外：[MiMo-Audio官方artifact](https://github.com/XiaomiMiMo/MiMo-Audio) | README历史上限20实返5，最早9bc65b003c18；原contents/repoAPI与官方Blog | 受阻 | creation/commit/currentpublic不单独证明原公开时间，未运行代码/复现 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无已确认落窗并通过准入的正式行。63论文潜力及MiMo先发保留在§5，不先评分、不以摘要读取冒充Evidence完成。

## 4. 证据与知识整合

本日未获可采用候选，Books拟增量0。未读取实际owner论点来声称已有覆盖，也未改Books。原始题摘及准入一句链见FIRST_BATCH；理论/性能/安全主张的必要反侧已明示，包括FURINA输入相关选择与可merge等价性、A1在线conformal失配与收益分母、CurDKV输出保真/选择成本、AQE捷径与真正自觉之间缺桥、污染Blocking本身干预损害。这些仍是必要审阅需求，不声称已读相关定理/消融。

Google关闭只限本次事件：Sensible09/18Blog核心与09255v1同what/how/交互结果；DIVE09/18publication与2507.13383v1完整题摘相同的人口分层安全差异；TTD-DR09/19Blog核心与2507.16075v1同draft-first/evolution/retrieval，独核旧§2～4已有ADK、结果与消融。Blog跨baseline默认不同LLM、Agentspaceavailability一句不披露新的系统/正确性约束，不授新的机制事件；不是因为n=10、benchmark或既有principle而排除，非作者已核必要去重与负侧。

必要反侧本轮仅补三项：RES 14834v1 §2.2/3.1–3.3/Table2与Appendix C，发现模拟persona的DR局部消融、P6反侧及.6秒→1.7分钟代价；Empathy-R1 14851v1 §3.3.2/4.1.5/4.3，发现SFT-only局部退化、embedding奖励代理与非临床公众偏好不能保证安全；CLEAR 15027v1 §5.2/5.3–5.5，发现新增虚构引用和薄弱论据未修与偏好提升共存。撤回三项旧关闭，具体采用边界、实际读到的位置与未披露条件见差额，不把这些日期隔离项授Evidence完成或医学疗效，不扩65篇全文队列。

非作者追加定点反例：14943v1 §3～5/Tables6～8明确explicit-only训练→implicit测试的退化，不能维持“只有合成数据fit”的关闭；只恢复局部暴露/分布转移潜力，保留RQ1的BLEURT/Sentence-BERT描述冲突、同生成器职业范围及模型rank/epochs不齐。15089完整v1题摘的发现→可靠实例cross-validation筛选→重预测提供自纠错机制潜力，缺原公开时间，未授可靠实例为真标签。14504/15048补完整v1题摘后按本GEC数据适配/MLM分类无新增机制或预算可比迁移边界具体关闭；不以语言/领域标签自动排除。[独核差额](../_sources/daily-20250919/INDEPENDENT_DAY_REVIEW.md)保留原历史及必要限制。

## 5. 缺口与下一步

普通可执行工作：无。非作者首批/代表负侧、实际有限来源停止与DAY已执行。无Books实际修改，本日无可采用候选或可交精确整合段落。若具体新反例或日期恢复，只重开受影响项的准入、必要证据与实际owner比较，不扩为全文库存。

隔离的外部保留项：FIRST_BATCH与最新[独核差额](../_sources/daily-20250919/INDEPENDENT_DAY_REVIEW.md)逐项具名的63精确v1论文家族（作者61＋恢复14943＋新增15089），缺原公开公告/作者先发证据或完全落窗区间；已尝试主题、系统、历史new参数、月表及priority精确查询，保留超时/部分响应，不用submitted/DOI/HF替公开。取得原公开上下界完全落09/18 09～09/19 09后，定点重开对应v1的准入与必要证据，不重扫月库存。本窗终态保留项不支持正面证据、候选、Books或无遗漏/全站覆盖断言；普通未读附件不属终态。

MiMo-Audio单次请求：需要官方原公告/公开历史上界与9月artifact一致性。官网Sep19date-only、repocreated09/19T00:46:49Z与firstcommit00:48:29Z可以核身份，但不单独证实当时public。最早README已取；当前官方Blog原architecture已读，不以12月2512.23808代9月版本。可接受官方带TZ公告/可审公开artifact事件，恢复FIRST_BATCH MiMo段。

Meta、Hunyuan、ZAI、Seed论文、DeepMind/MiMo历史缺段只在相应原目录/API/真实分页恢复时定点重开来源行。不支持零事件、无遗漏、候选或Books正面断言。其他明确关闭项无需为不影响处置的日期无限追查；root发现具体新增事实时局部恢复。

## 6. 复核

复核者：sept07_10_author（非报告作者Tesla）。

结论：通过

实际完整读作者65份精确v1题摘、62月段标题，补3个含糊标题完整题摘；局部原件核14834/14851/15027三重开、14943新反侧，恢复15089自纠错潜力，核5具体关闭、其他领域范围分层及Google三再阐述。独立核14来源有限原响应与分页、日期隔离和六部分；正式0/Evidence0/Books0，无普通未完成任务。[实际独核范围与处置](../_sources/daily-20250919/INDEPENDENT_DAY_REVIEW.md)，不授68全文审完或全站历史完整。校验器不替语义验收。

机器校验：本次V3校验及本日限定`git diff --check`通过；不据静态通过将状态改完成。
