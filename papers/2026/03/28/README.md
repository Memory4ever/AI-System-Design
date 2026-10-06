# Daily Research — 2026-03-28

**规范：** V3
**窗口：** 2026-03-27T09:00:00+08:00 ～ 2026-03-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T04:58:00+08:00

## 1. 结论

本窗确定候选0、必要Evidence完成0、Books新增/已有覆盖/仅报告/结构候选均0。不是本日没有研究：9个arXiv潜在家族的公开范围跨窗口左界，SAM3.1更新仅日级日期；10项隔离不评分、不授实验结论或Books。另Registers和GhostServe的arXiv事件明确窗外，保留真实恢复线索，不反填早Submitted。作者读15份完整exact-v1题摘及SAM3.1/STADLER核心；4份题摘与STADLER具名贡献前关闭，不把摘要读完记全文审阅。

四主题有限API返回3+21+22+25=71交叉条目（未去重，submitted缓冲窗，不是当天论文数），只读标题/时间查漏，不自动逐项题摘或全文。14源实际有限范围与4组具体历史入口限制保留。旧V2的0分母、EffectiveDate、整库重放和完成标签不继承，原文保留[旧快照](../_sources/daily-20260328/V3_LEGACY_REPORT.md)。普通待办0；root最终非作者日Gate已通过，无长工具、无Books待写/待POST，不扩新发现波。

## 2. 来源覆盖

[唯一有限停止与查询过程](../_sources/daily-20260328/V3_WORKING_STOPPOINT.md)、[四主题原参数](../_sources/daily-20260328/V3_THEME_DISCOVERY.json)、[Seed实际元数据](../_sources/daily-20260328/V3_SEED_FIELDS.json)保留。跨日只定点复用未变的原身份/字段，本窗自行比较，不继承筛选或完成判断；下表不授全机构召回。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS；定点复用[26官方RSS六Mar24–27邻接](../_sources/daily-20260326/V3_OPENAI_RSS_FIELDS.md)，1242 items非正文队列；STADLER27T22GMT唯一邻接落窗，actual207行core54–111关闭，其余左界前 | 已检查 | 不证明所有历史launch版本逐字一致 |
| SRC-ANTHROPIC | Research最新10之外，独立对读[20原Sanity九March publishedOn/title](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)：Mar24T10:41Z→Mar31T22:17Z跨窗，无27/28返回 | 已检查 | 仅Research实际March字段，不外推News全部 |
| SRC-GOOGLE-AI | Research March204行12cards页1 + [05原页2的Mar6/Mar4两cards](../_sources/daily-20260305/V3_OFFICIAL_RECOVERY_12.md)，当前2/2；DeepMind真实/blog/page/3/302行24cards含6March，FlashLive26T15:21Z/Manipulation26T13Z/Lyria25T16Z均左界前；pubs当前766行 | 受阻 | H1仅目标publication历史切片；不把page1当全部March |
| SRC-META-AI | Research0行；Blog270行10cards+真实page2 308行12cards非日期排序，SAM3.1 Mar27→TRIBE Mar26→Mar11/10；正确publication/results当前444行Sep/Aug，原[25恢复](../_sources/daily-20260325/V3_RAW_META_PUBLICATIONS.md)可核；SAM更新core49–63已读 | 受阻 | D10 SAM精确更新日期/launch版本；H2目标Research/publication历史slice |
| SRC-QWEN | 独立读取[25原API40条title/path/date](../_sources/daily-20260325/V3_QWEN_FIELDS.json)，MaxPreviewMar19T04+08→OmniMar30T04+08跨窗；停止实际40 | 已检查 | 未暴露total/paging，不证删除项/全部机构历史 |
| SRC-DEEPSEEK | /en/news可见5之外，实际对读[20原Next完整16posts及Research script数组](../_sources/daily-20260320/V3_WORKING_STOPPOINT.md)：NewsApr24前为2025，ResearchFeb25→Jun24跨窗无可见27/28 | 已检查 | 有限公开数组，不继承动态访问故障 |
| SRC-MOONSHOT | 真正kimi.com/en/blog/155行完整19dated cards，Feb9→Apr20跨窗无可见27/28；旧platform止2025不作Research缺失依据 | 已检查 | 不外推GitHub所有release |
| SRC-TENCENT-HUNYUAN | 定点独立对读[21 production publicList原11/11](../_sources/daily-20260321/V3_HUNYUAN_FIELDS.json)，renderType0/page1/size20，Feb3/13→Apr23display(pubJun24)跨窗，无March | 已检查 | display/published不互换first-public，仅该可见目录 |
| SRC-ZAI | 实际Research175行15cards Mar15→Apr1与release165行16条Feb12→Apr7跨窗，无27/28可见项，停当前有限目录 | 已检查 | 不外推所有News/旧库存 |
| SRC-BYTEDANCE-SEED | type1/year2026/token20/count100/order_descfalse/US原18/82止Mar26，独立本日token40返回20/82 next60(true)，首Mar31已越窗停止；type2/token0同参数14/19 next空(false)，Feb→Apr跨窗；新34 metadata不作AB队列 | 受阻 | H4 Blog未返5身份/date或差额解释；未把UpdateTime当first-public |
| SRC-BAIDU-ERNIE | EN请求InternalError后官方ZH68行10cards May9/Apr30/15→Feb6/Jan29→2025Nov，第一页跨窗，next旧页不扩 | 已检查 | 语言ZH明确，不授全部历史 |
| SRC-XIAOMI-MIMO | 实际首页338行Paper8 June29→Mar13→Feb3，Blog15无date；正确Pro/Omni原route均March18，整日窗前，非误猜/blog正文缺口 | 受阻 | H3仅目标dated Blog历史slice，非已恢复Pro/Omni正文 |
| SRC-MINIMAX | EN76行12/CN68行13cards Mar18M2.7→May26(EN)/Apr27(CN)跨窗；Forge ENFeb14/CNFeb12分别保留；AgentTech原.md880B仅May13当前dated index，定点复用19事实 | 已检查 | 无具体本窗缺失线索，不新造historical阻塞，不扩guides |
| SRC-ARXIV | 四主题title查询submitted buffer26T01Z→28T01Z，start0/max25/升序：3/3、21/21、22/22、25/100；15完整v1题摘/历史；官方availability实际Fri/Sat无常规batch；合法cs/2026-03首50月表未给具体公告时刻，停止 | 受阻 | D1–D9公开区间跨左界；剩75非逐项队列，月表成员不证明exact公告 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无已确认完全落窗且通过贡献筛选的候选。日期未定的潜在材料放§5，不先评分或拿访问状态减分。

## 4. 证据与知识整合

无确定候选的全文Evidence或实际Books修改。SAM3.1的object multiplexing、DFLOP的数据依赖pipeline、HybridMemory的动态出视野状态、MAS多重归因及第二批具体命题均只完成准入层；摘要性能/保证尚未必要证据核验，不沿用此前其他日的审阅/Books判断。无需为隔离项提前申请Books锁。

STADLER落窗但core54–111是650员工/125customGPT的采用案例、自报节省及未来验证审批方向，未披露新执行机制或改变系统选择的独立证据；不采用30–40%/2.5x为性能结论。SAM更新只读49–63，不将66后旧SAM3正文全部归新release；16→32fps与HF约7x/128objects不可合并为相同端到端协议。原linked2511.16719v2 Submitted28T16:54:56Z在窗后，不反填launch时的论文证据。

## 5. 缺口与下一步

普通待办0；无长工具或普通未读全文队列。以下为本窗外部终态保留项，不支持正面证据/Books/无遗漏断言；以后只按具体条件重开受影响材料。

D1–D9：本日实际官方[availability/no-advance ID/schedule](https://info.arxiv.org/help/availability.html)、[DOI](https://info.arxiv.org/help/doi.html)与[DataCite registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)、[state](https://support.datacite.org/docs/doi-states)复合依据：各Submitted在Thu26T14EDT截止前，最早常规27BJT08；arxiv.content-owned/findable registered秒精度+1秒给公开上界。范围跨左界27T09，不取schedule/created/updated为精确first-public，也不证明更早作者公开。原字段见[首批](../_sources/daily-20260328/V3_FIRST_ADMISSION.md)、[第二批完整题摘/日期JSON](../_sources/daily-20260328/V3_SECOND_ADMISSION.json)。合法月表首50只给整月，不恢复这些具体时刻，不扩大整月。

| 身份 | 原registered UTC（上界另+1秒） | 潜在增量/必要隔离范围 |
| --- | --- | --- |
| D1 [DFLOP25120v1](https://arxiv.org/abs/2603.25120v1) | 2026-03-27T02:01:37Z | data-dependent profiling/predictive scheduling替代静态stage负载估计；不授3.6x |
| D2 [HybridMemory25716v1](https://arxiv.org/abs/2603.25716v1) | 2026-03-27T02:15:48Z | 动态subject出入视野状态与静态background记忆不同有效条件；v2窗后 |
| D3 [FailureAttribution25001v1](https://arxiv.org/abs/2603.25001v1) | 2026-03-27T01:58:45Z | 多个合理rootcause及多视角评价改变唯一gold归因假设；不授因果结论 |
| D4 [SystemPrompt25056v1](https://arxiv.org/abs/2603.25056v1) | 2026-03-27T02:00:04Z | domain-matching信号被攻击者反转时specificity形成脆弱安全条件 |
| D5 [SABER24935v1](https://arxiv.org/abs/2603.24935v1) | 2026-03-27T01:57:14Z | bounded-edit黑盒VLA attacker分开task failure/执行长度/constraint violation |
| D6 [RubricEval25133v1](https://arxiv.org/abs/2603.25133v1) | 2026-03-27T02:01:57Z | response-level meta-eval未覆盖rubric-level判断有效性 |
| D7 [TokenCompressor25340v1](https://arxiv.org/abs/2603.25340v1) | 2026-03-27T02:06:50Z | 离散可变长Z-code重构与latent-space生成的兼容边界，精确重构仍作者待核主张 |
| D8 [FreeLOC25209v1](https://arxiv.org/abs/2603.25209v1) | 2026-03-27T02:03:46Z | position/context双OOD的layer-adaptive probing选择纠正，不授SoTA |
| D9 [PersistentWM25685v1](https://arxiv.org/abs/2603.25685v1) | 2026-03-27T02:15:03Z | own-rollout RL而非groundtruth histories的多步训练分布；收敛保证未核 |
| D10 [SAM3.1更新](https://ai.meta.com/blog/segment-anything-model-3/) | 原Update March27，无zone/exact时刻 | per-object forward→最多16objects共享forward/global reasoning潜在增量；launch版本不得由后v2替代 |

D1–D9各只请求一次：exact-v1可核官方公告/批次及实际可取正文上界，或作者原首次公开记录，能将范围完全置于本窗再重开准入→必要证据/Books；否则只按真实归属日定点恢复。当前官方页可见撤回/erratum未发现，仅检查原页，不认证所有版本史。D10一次原HTML227899B未恢复datePublished/dateModified/publish_time等精时字段；官方linked公开HF sam3.1 card65–71亦无精确release，collection UpdatedMar26不是first-public。只请求原update精确发布记录与实际launch正文/机制范围，恢复后必要证据；不要求登录/接受checkpoint条款，也不追完整git/commit史。

H1 Google publications本窗可读历史导出；H2 Meta Research/publication本窗可读切片；H3 MiMo15个nondated Blog的本窗dated切片；H4 Seed type2未返5的身份/date或差额说明。各仅恢复相应窗口/入口，不扩全站所有正文。

窗外恢复线索（不阻塞本窗）：[Registers25803v1](https://arxiv.org/abs/2603.25803v1) Submitted26T18:09:12Z已经Thu14EDT后，常规最早30BJT08，registered30T01:45:59Z；无早作者event线索，不造28batch请求。[GhostServe2605.00831v1](https://arxiv.org/abs/2605.00831v1)五月ID/Available2026-05/registeredMay5T02:57:33Z，早Submitted26T13:27:57Z不证明March公开；只保留真实五月arxiv事件，不冒充已审重复。两项潜在机制已题摘读过，未授Evidence/Books。

具名贡献前关闭5项：完整题摘N1 [SelfImprovementOverview25681v1](https://arxiv.org/abs/2603.25681v1)四阶段生命周期组织/未来愿景未新增独立机制或验证反证；N2 [OMIND25105v1](https://arxiv.org/abs/2603.25105v1)检索/LLM prune/review领域SFT与expert rubric，未识别新增通用有效条件，不因医学排除；N3 [TSPDT25241v1](https://arxiv.org/abs/2603.25241v1)offline DT/Pointer/expectile应用heuristic TSP未建立foundation模型形成或系统增量；N4 [ConsistencyAmplifies25764v1](https://arxiv.org/abs/2603.25764v1)10tasks×5重复的跨模型variance/accuracy及错误一致比例未受控改变variance/interpretation，未识别额外机制选择条件，不因小样本自动关闭；N5 [STADLER](https://openai.com/index/stadler/)上述已读核心。前四日期未核不影响明确贡献前处置，不造额外材料请求；详细首批理由与后批完整AB可核，不叫全库存审。

## 6. 复核

复核者：root（非作者）
结论：通过

首批准入校准已通过：root实际完整v1题摘DFLOP/Registers/FailureAttribution、三个负侧Overview/OMIND/TSPDT，以及SAM3.1原core49–63；HybridMemory相同v1题摘曾27实际读可复用实际identity/范围，不继承日判断；GhostServe只日期metadata依据，不假称root全文。root又实际完整读第二有限七题摘：六项潜在增量/日期隔离合理，ConsistencyAmplifies关闭理由按相关性与受控干预边界、不依小样本；必要安全题摘均已核，不授实验效果。最终实际核完整六部分、14来源有限范围/停止、D1–D10和H1–H4隔离，日级Gate通过，普通作者待办0。未独立全审71库存或15全文，无实际Books修改/待POST。

实际运行 `python3 scripts/validate_research.py --report papers/2026/03/28/README.md`：1 V3 interface/consistency PASS；本日README/_sources限定 `git diff --check` 无输出，不能代替上述独立语义验收。作者仅本日README/_sources，不写LS/索引，不stage/commit/push。
