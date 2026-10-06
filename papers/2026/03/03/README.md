# Daily Research — 2026-03-03

**规范：** V3
**窗口：** 2026-03-02T09:00:00+08:00 ～ 2026-03-03T09:00:00+08:00
**窗口说明：** 用户授权只补已有Daily遗漏；原窗口、原候选与连续原§4冻结，不重新迁日或评分。
**补充窗口：** 2026-03-02 ～ 2026-03-02
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-09T04:09:51+08:00

## 1. 结论

本轮补充03/02完整自然日：原确定候选0冻结，新增确定2个材料家族——GPT-5.3 Instant官方HTML安全评价（Published March2）和DoW协议Mar02同家族重要修订。两者必要受影响证据已深入复核，GPT消息/末答/对话分母及动态模拟边界由root实际整合至Ch66两段并经非写入者POST通过；DoW仅报告公开许可事实，不重复评分、不采执行/安全保证。18新完整arXiv题摘与四个准入争议core经两项改判后为16潜力/2关闭，另2个Seed语言目录反例题摘有具体潜力但精确首公开版本未闭合；3旧潜力有效题摘复用。合计21个必要日期/版本缺口精确隔离，不评分、不计正面候选/Evidence或Books，不用Submitted/月份ID或目录显示日期替代精确论文首次公开。扫描、日期恢复、必要证据、Books及root非报告作者完整日级审核均已到安全终态，普通待办0；不授全Coverage/Evidence或无遗漏。

以下原结论保留为旧运行冻结记录；旧完成与时区请求不代表本轮结果。当前事实以本轮补充各段及[增量停点](../_sources/daily-20260303/supplement-20261009.md)为准，尤其GPT HTML日级现已可采用、Gemini官方Mar03在补充窗外。

本次十四个每日来源已处理到下述有限停止点，未取得可同时确认贡献与本窗公开归属的正式候选；确定候选为0、正式证据审阅为0、Books整合为0。不是“本窗原始命中0”或全源零遗漏：GPT-5.3 Instant、Gemini3.1Flash-Lite安全说明与三项arXiv潜在贡献缺必要公开日期，已具名隔离；DUEL由实际Submitted下界和官方公告规则排除本窗，而不声称其确切公告日。若日级非作者复核通过，可以带这些外部保留项结束本次处理。

旧报告的arXiv零命中依赖DataCite登记与常规日程映射，并未核实际公告批次，本次撤回该覆盖结论。旧原始材料不删除，原报告存于[旧报告保留](../_sources/daily-20260303/V3_LEGACY_REPORT.md)，只保留其可核实的原始身份/原文，不继承旧评分、EffectiveDate豁免与Gate。

Qwen Code产品汇总、Qwen3.5小尺寸发布这两个机构家族已读官方核心说明并经root准入校准关闭，理由是旧事件汇总或没有可支持的机制/设计边界增量。Gemini初次产品机制判断被安全尾部的具体负向证据纠正：自动图像安全回退、人工误报检查、红队比较与跨card不可比并存，产生窄评价边界贡献，改为日期隔离。不以机构声望、小模型、修复标签或Books主题相似决定准入。无新增安全采用项，Books无需写入。

## 2. 来源覆盖

实际查询、停止段、负侧原文与保留项细节见[本日来源停点](../_sources/daily-20260303/V3_SOURCE_CHECKPOINT.md)。每一行只声称相应范围，搜索无返回不等于机构零研究。

旧来源覆盖冻结原件见本日baseline与V3_SOURCE_CHECKPOINT；当前补充覆盖以本节下表为准，不重复两套来源行。

未扫描每周来源或未经触发的按需来源。arXiv搜索只按cs.CL/LG/AI/DC、CV/RO、AR/PL/OS/PF、IR/MA主线主题辅助查漏，分类宽库存不是全文队列。

### 补充窗口来源覆盖（本轮）

实际原入口、主题查询、有限段及原件见[增量停点§一](../_sources/daily-20260303/supplement-20261009.md#一十四每日入口与停止点)。只声称下列约定主题范围；旧表不授本轮日级日期或全源覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1257item实际Mar01–04段；GPT safety完整HTML§2/3.1；DoW Mar02更新L20–30/旧分隔线与FAQ | 已检查 | RSS Mar02无item只限feed；两个HTML事件已确定，不授隐藏目录零遗漏 |
| SRC-ANTHROPIC | 当前Research嵌入Publications实际02/25T20:02Z→03/05T19:59:21.508Z邻接 | 已检查 | 段内无03/02，不外推未列入目录事件 |
| SRC-GOOGLE-AI | DeepMind当前Research；pubs curl失败后web当前1–15/11600；March2主题查询 | 受阻 | 当前pubs仅年份、March主题日段未恢复；Gemini官方Mar03窗外，不再以缺timezone隔离 |
| SRC-META-AI | Research curl reset→一次web0行，March2官方域主题查询 | 受阻 | 本日可读历史主题段缺失，搜索不授零研究 |
| SRC-QWEN | 新blog壳及[官方API定点恢复](../_sources/daily-20260303/SUP_QWEN_SEED_FALLBACK_20261009.md)：40条、无分页字段，邻接Feb16→Mar19；原官方Mar02小尺寸有效核心关闭复用 | 受阻 | 返回目录未含已知Mar02小尺寸发布，故不证明历史段完整；Code Mar03汇总窗外，旧PR不重审 |
| SRC-DEEPSEEK | 官方updates完整日期日志邻接2025Dec01→2026Apr24 | 已检查 | 该日志段无03/02，不授未公开研究覆盖 |
| SRC-MOONSHOT | Kimi Research完整可见19条至2024Jun26，02/09→04/20目标邻接 | 已检查 | 当前目录无03/02，不授删除/隐藏历史保证 |
| SRC-TENCENT-HUNYUAN | Research壳后按实际页面API一次publicList page1/size20/renderType0，zh11/total11 | 已检查 | display 02/13→04/23无03/02；不将publishedAt替代first-public或授全机构保证 |
| SRC-ZAI | Research全部时间排序02/21→03/15邻接 | 已检查 | 该目录段无03/02，不扩更多旧年 |
| SRC-BYTEDANCE-SEED | Research Publication Jan27→Apr11；[论文API实际token20](../_sources/daily-20260303/SUP_QWEN_SEED_FALLBACK_20261009.md)默认14条、US locale18条，total82/next40；US两条显示Mar02，完整题摘及精确版本已定点核 | 受阻 | 两条目录日与论文first-public/版本权限未闭合，另列具体请求；Blog及完整历史仍受限，不以locale14推零 |
| SRC-BAIDU-ERNIE | Blog首页Feb06→Apr15邻接段 | 已检查 | 该段无03/02，不扩更早页 |
| SRC-XIAOMI-MIMO | Paper8条Jan08/Feb03→Mar13；Blog15标题/More | 受阻 | Paper目标段无03/02；Blog缺本日dated历史段，不将当前标题扩全文 |
| SRC-MINIMAX | Blog完整可见12条至2025Oct27，Feb14→Mar18 | 已检查 | 该段无03/02，不扩商业News |
| SRC-ARXIV | 四主线主题+一次同义补检；cs March1–50相关标题浏览；18新exact-v1题摘、四争议core、3旧题摘/当前标记复用 | 受阻 | 16新+3旧潜力共19缺必要首公开日；月列表不是daily公告，搜索受限，不授十二分类穷尽 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [GPT-5.3 Instant System Card — safety HTML](https://deploymentsafety.openai.com/gpt-5-3-instant/safety) | 2026-03-02 | 固定历史末答安全评估→输出条件动态用户模拟/逐消息not_unsafe→应区别消息与对话分母及困难人口；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66逐条/完整轨迹段后](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root实际两段/末注、作者非写入者POST通过 |
| [Our agreement with the Department of War — Mar02 update](https://openai.com/index/our-agreement-with-the-department-of-war/) | 2026-03-02 | 同家族重要修订：商业采购PII用途与额外agreement边界明确；不重复评分，原[03-01家族](../01/README.md)分数冻结 | 深入完成 | 仅报告：公开deployment许可事实，未披露可迁移执行/验证机制，不采厂商绝对安全保证 |

旧运行冻结说明（当前候选是上表两个补充事件）：无确定当窗候选。具名日期保留项未评分、未计证据完成、未进入Books。两个贡献关闭家族及明确理由留在[来源停点§二](../_sources/daily-20260303/V3_SOURCE_CHECKPOINT.md#二首批负侧校准与关闭理由)，不伪装为候选审阅。


## 4. 证据与知识整合

无可安全采用的正式候选，未改Books。这里的No Change不是“Books已覆盖”判定：日期保留项尚未获得采用权限，不把未经对读的章节写为已有覆盖。

GPT-5.3 Instant已读官方§3.1/PDF pp.1–3的动态多轮评估、类别回退与offline/online差异，潜在贡献成立；其困难集不代表平均生产安全性，不外推为改善保证。Gemini已读安全评价的自动/人工定义、比较条件与跨card限制，支持单一自动通过率不能独立决定发布安全性的窄命题；表格以2.5Flash-Lite为基线，人工红队以2.5Flash为基线，不偷换为同一比较。四项arXiv仅完成完整题摘与身份/修订提示检查，不声称全文证据通过。原始字段、准入命题和必要材料请求均在[来源停点§三](../_sources/daily-20260303/V3_SOURCE_CHECKPOINT.md#三具名日期保留不纳入候选分母)。

### [GPT-5.3 Instant System Card — safety HTML](https://deploymentsafety.openai.com/gpt-5-3-instant/safety)

精确采用当前官方HTML的Published March2和§2/§3.1，而非将PDF封面March3、RSS正式blog或2/26 shipped subject日期当作同一事件。官方比较subject是launch时旧模型latest revisions，不能合并旧card的不同版本分数。Production Benchmarks是有意选难的生产案例，error rate非平均流量；dynamic下一轮随模型输出变化，标准验末答而其not_unsafe明确定义assistant消息合规比例。原文“any assistant response”说明评估跨消息，但未提供“整段无违例”比率，不能自行换算。

厂商报self-harm/sexual内容相对5.2回退、另两类回退低统计显著；online未观察self-harm增加不抵消offline反证，system safeguards是缓解声明非效果证明。未引用HealthBench领域指标或推理性能；generator、样本量、judge实现及硬件/batch/concurrency/SLO未公开或不适用本测量命题。root独立必要Source通过后实际将消息/末答/对话分母与固定/动态共存两段写入[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，紧接2602.22775轨迹段、在history干预前；作者非Books写入者实际完整邻接和自身末注POST通过。旧正文的相似trajectory/分布主题不足以称已覆盖此分母差额，未核artifact或复现实验。

### [Our agreement with the Department of War — Mar02 update](https://openai.com/index/our-agreement-with-the-department-of-war/)

官方更新L20–30明确将商业采购/使用个人或可识别信息纳domestic surveillance禁止描述，并称NSA等情报机构服务需新agreement。[03-01原有效审阅](../01/README.md)仅采用Feb28分隔线下的cloud-only/控制栈事实，明确未采用Mar02段，本次不是重复首公开。root与作者实核更新段和必要旧边界/FAQ，只确认厂商公开许可事实；没有执行识别、强制控制或有效性证据，不转成不可滥用或合规保证，与Ch72现有控制/验证分工没有新可迁移机制，故仅报告且不重复评分。

### arXiv补充准入纠正与日期隔离

18新完整题摘从相关标题有界恢复，原件及具体增量在[停点§二](../_sources/daily-20260303/supplement-20261009.md#二新完整题摘与准入链)。四个争议关闭项只定点core后停止：AR教学§2.3–2.4明确future architecture、实验只是人类AR baseline；sentence-graph §3是已知SWA/过滤在文档GAT的应用，关闭。LitBench§3.2–3.3式2的三层concept平均embedding召回替代和PaperRepro§5.1.1的112实例/13错项三类标签反证，纠正原整家族EX，改窄潜力。最终16新潜力及3旧有效潜力都缺必要first-public日，不评分、不采用实验结论或进Books；准入core不充完整Evidence。未见当前页撤回公告不等完整版本史保证。

## 5. 缺口与下一步

Seed locale定点纠正：新增两条完整题摘均有具体潜力，但目录显示日期未认证所链精确论文首次公开版本，见[原证、独立裁决与两个材料请求](../_sources/daily-20260303/SUP_QWEN_SEED_FALLBACK_20261009.md)。不评分/不进Books，原19日期潜力加此2项为21；题摘读取18新arXiv加2Seed为20。root与supplement_20260308实际窄核，普通待办0；上文及下文19是该纠正前的有效批次规模，并非包含此2项的最终数。

本轮普通待办0：扫描、题摘、一次date恢复和必要证据/Books写入、非写入者POST及root非报告作者完整日级审核已结束。新外部终态保留：16新arXiv潜力（逐项身份见[停点§二](../_sources/daily-20260303/supplement-20261009.md#二新完整题摘与准入链)）加ActMem2603.00026、SimpleTool2603.00030、Attn-QAT2603.00040共19，需要精确ID的官方首公告/状态邮件或作者具名dated公开原文。当前abs只有Submitted/版本提交史、月页只有March；材料到达只核03/02归属/版本，再按必要深度恢复，不请求时分秒、不全月扩扫。它们不支持候选分母、正面Evidence、Books、无遗漏或安全保证。

本轮Google/Meta/Qwen/Seed papers/MiMo Blog仍缺必要03/02历史主题段；已实际本日原入口和一次有限恢复，替代是该日官方dated目录导出、稳定cursor或具名原始发布。只重开受影响入口/身份，不拿全年pubs/242库存做逐项队列。旧GPT时区/instant请求撤销为本轮重开条件，HTML官方March2足够；Gemini官方March3本轮窗外，旧请求和DUEL09:00下界说明仅作为冻结旧窗口历史。下列旧保留请求不升级为本轮新要求。

普通可执行来源扫描、贡献筛选及必要定点消歧和非作者日级复核已结束，普通待办为0。以下为本窗终态保留项，不用于正面证据、Books或无遗漏断言，材料到达后定点重开：

- **GPT-5.3 Instant System Card**：[HTML](https://deploymentsafety.openai.com/gpt-5-3-instant/safety)Published March2，但[PDF](https://deploymentsafety.openai.com/gpt-5-3-instant/gpt-5-3-instant.pdf)封面March3，均无时区。需要官方首次公开记录/带timezone发布日志，给出完全落窗范围或明确窗外归属；取得后只重开该家族，不重新扫OpenAI全部发布。
- **Gemini 3.1 Flash-Lite安全评价**：[官方card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/)与[发布blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)仅Mar03日级、无时区，不能完全落入本窗。具体安全比较/误报/跨card限制构成潜在贡献；需要官方带timezone首次公开记录或能明确归属的公开范围，取得后只恢复此窄安全命题，不扩大到性能库存。
- **arXiv日期家族**：[ActMem2603.00026v1](https://arxiv.org/abs/2603.00026v1)、[SimpleTool2603.00030v1](https://arxiv.org/abs/2603.00030v1)、[Attn-QAT2603.00040v1](https://arxiv.org/abs/2603.00040v1)：完整题摘显示值得核验的机制，但Submitted/APIupdated/DOIcreated不证明具体first-public。需要对应官方公告列表/订阅公告或availability log；旧policy推定Mar03T09:00不授真正首公告。取得后按真实事件日定点恢复。
- **arXiv左端槽位**：需要Mar01EST20:00→Mar02BJT09:00实际目标主题公告列表，包括跨月/旧ID事件。March库存首批Mar03不是该槽位为空的证据；pastweek附year/month/day实际仅返回月表，advanced官方说明announcement日期只year/month精度。不能以常规日程推零。
- **机构历史段**：OpenAI、Anthropic、Google、Meta、Seed论文分页、Qwen新blog、MiMo Blog各缺本日历史主题段可读入口。已检查注册入口及有限官方查询/fallback。混元已恢复实际“全部”目录11/11，本日对读显示2/13→4/23；Kimi新Research Blog19条可见目录本日对读2/09→4/20，均窗外，这两个入口不再动态目录受阻。其余可接受目标日期段官方目录导出、稳定分页或具名原始发布记录；取得后只重开对应来源/身份，不扫全部年份。Google当前全年pubs与Seed242库存不成为逐项队列。

上述是必要外部范围/日期限制，不是把尚未读完的候选包装为受阻。[DUEL2603.01367v1](https://arxiv.org/abs/2603.01367v1)Submitted Mar02T01:56:03Z，晚于此前Sunday20EST公告槽位（Mar02T01:00Z）；按[官方availability规则](https://info.arxiv.org/help/availability.html)最早常规公告不早于Mar03BJT09，即本窗不含右端，排除本窗。没有据此授其实际公告时刻；作为窗外查漏身份线索交给真实事件日，不在本日再请求日期或扩审。三个Feb Submitted身份不能套用这个下界排除。早于本窗的Qwen功能PR只作汇总事件排除依据。

## 6. 复核

本轮复核者：root（非报告作者）。结论：通过。root实际核十四有限来源表/原件及停止范围，包括RSS1257无Mar02item只限feed、混元中文11/11；全部18新完整题摘、四决定core及LitBench/PaperRepro改判、16新潜力/2具体EX与19必要日期隔离；两确定新事件公开日及受影响证据，Ch66真实两段写入、完整局部邻接/末注和作者非writerPOST；原0候选、原window及连续§4冻结。全部六部分差额日级审核通过，普通待办0。未无差别复核cs宽库存、Google全年pubs/Seed242库存或隐藏历史，不授全Coverage/Evidence或无遗漏；以下原“通过”只冻结旧运行，旧时区/09:00推定不授新门限。

本轮机器检查：V3结构/一致性和本地Markdown引用通过；原窗口逐字保留、原候选0新增2、原§4连续前缀逐字保留；限定本日README/本目录unstaged diff-check通过。不把机器检查称语义通过，未stage/commit/push。

复核者：root（非作者）。
结论：通过

root最终核14来源的有限停止范围、全部5个日期隔离与DUEL窗外下界、两个完整核心负侧家族，直接再读GPT-5.3 safety §3.1和Gemini安全尾段确认动态对话单位、offline/online不相消、自动/人工基线不同和跨card不可比。具名分层抽检4个Qwen PR旧事件时间、Qwen dense配置、混元/Kimi/DeepSeek/ZAI/ERNIE/MiniMax邻接日期段；没有把这些样本称为隐藏目录全量验证。OpenAI官方RSS精确字段将GPT-5.3正式发布定位03/04，原HTML提前挂出可能仍外部隔离；Anthropic嵌入列表目标段已恢复，§5相应Research请求撤销。无候选可采用或Books实际改动，不作未经对读的已有覆盖断言。外部保留项不是Coverage/Evidence通过。最终结构与diff-check由root执行，机器通过不替代上述语义验收。

已完成首批及负向纠错校准：root确认Qwen旧PR汇总不重复首公开、小尺寸card未经控制的score不建立新设计边界；Gemini安全尾部补读后撤回整家族贡献关闭，窄评价边界改为日期保留；GPT-5.3动态安全评估潜在贡献保留日期缺口，不能用card版本标签排除。待日级复核范围为14源有限入口/停点、混元/Kimi目录恢复、DUEL公告下界排除、旧零命中纠正、全部5个日期保留与两个负侧家族、无Books采用及实际变更范围。

机器检查：`python3 scripts/validate_research.py --report papers/2026/03/03/README.md`通过1份V3结构/一致性及本地Markdown链接；本日范围`git diff --check`通过。机器检查不替代语义验收。

作者仅修改本日README与本日V3证据文件；旧原始证据保留。未stage、commit或push。
