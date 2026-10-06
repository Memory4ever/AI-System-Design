# Daily Research — 2026-02-03

**规范：** V3
**窗口：** 2026-02-02T09:00:00+08:00 ～ 2026-02-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T11:40:23+08:00
**补充窗口：** 2026-02-02 ～ 2026-02-02
**窗口说明：** 用户于2026-10-08授权仅补充现存2026 Daily的来源遗漏，原09点窗口、原候选日期、评分和有效审阅不改；新增材料按前一完整北京自然日判断，只核日期，不追时分秒。
**补充检查时间：** 2026-10-08T12:25:27+08:00

## 1. 结论

以下原窗结论保持有效，不作为本轮补查验收；本轮基线见[原稿](../_sources/daily-20260203/supplement-original-20261008.md)。新增自然日结果在各节补充段维护。

本日独立从十四个 Daily 原始来源发现，未读取旧 Daily/Weekly 的候选、评分或 screening；旧 README 仅原文备份于 [LEGACY_README](../_sources/daily-20260203/LEGACY_README.md)，未用于准入。当前首批八家族的具体贡献通过非作者校准，但公开日期仍有相互冲突的原始字段，已撤下确定候选身份与评分；原始查询返回条数、潜在机制和确定候选分别处理。

arXiv 的 Submitted 与编号月份不足以确定公开事件。原先拟用提交排程与 DataCite findable 注册上界夹出区间，但官方 first-announcement 月份定义与 Jan编号/Available字段存在直接冲突，不能仅口头保留冲突而仍授落窗。定点OAI亦只有last-modification datestamp，不是原始公告日志。这是新日期证据导致的隔离，不是因审阅费时缩池；已读机制证据保留但不采用。当前确定落窗且通过贡献筛选的候选为0，证据采用0、Books改动0；这不表示原始命中为0或潜在贡献不存在。机构 date-only 潜在亦未评分、未进入 Books。本日已通过非作者安全终态验收，普通待办0；日期和历史来源限制保留精确重开条件，不代表正面Coverage/Evidence通过或全站无遗漏。

补充自然日新增1家族：SPARKLING官方目录Feb02发布事件。必要v1机制、对照及直接反侧和Ch28已有覆盖/No Change已通过root非作者准入/Source/Owner PRE；采用命题仅为前向尺度保持与反向去对称两项条件，root完整六部分DAY亦实际通过。GLM-OCR、Snowflake及life-sciences合作按具体原文范围/增量关闭；Codex app同一发布事件已由02-02冻结收录，定点核已有有效审阅后去重复用，不重列、不推翻旧准入，作者先前以产品组件关闭整个家族的共同错误已纠正。两份新arXiv评价反证线索仅有Submitted字段，日期隔离而非误排为无贡献。原8家族与其他§5日期保留不因自然日变更自动转为候选，旧有效关闭和原§4连续正文均保留。本轮普通待办0、无Books新写入、不stage/commit/push；完成仅为所列切片与限制的安全终态，不授全Coverage/Evidence或无遗漏。

## 2. 来源覆盖

以下都是本日实际读取；原始记录集中于 [daily-20260203](../_sources/daily-20260203/)，本轮文件以 `feb03_` 开头。目录总数只说明返回范围，不表示全年题摘队列。未扫描 Weekly 源。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 原页，官方 RSS 返回1243条的元数据定点 Feb2–4边界；Codex Feb2 00Z在窗前、Snowflake Feb2 06Z与 Sora Feb3 00Z在窗、App Server Feb4 13Z窗后即停；两窗内核心全文实际读，RSS成功记录 stage4_0、Snowflake stage4_1、Sora stage6_0。 | 已检查 | Sora 当前含 April26停服更新，仅采用当前核心披露作贡献判断，不把停服作为本窗事件。 |
| SRC-ANTHROPIC | Research 原页与本日 UA恢复元数据174项，仅定位邻界 Jan29 coding skills、Jan28 disempowerment、下项Feb5 zero-days，停止于这段；stage2_1/stage3_0。 | 已检查 | 不声称全站历史无遗漏。 |
| SRC-GOOGLE-AI | DeepMind原页与 news page4 的 Jan Project Genie→Feb Deep Think邻界；Research pubs入口仅年粒度，定点官方 Jan/Feb月Blog目录：Jan9条至Jan28，Feb7条最早Feb3 virtual care、下一项Feb4；stage0_0/stage7_1/stage8_web。 | 受阻 | pubs首次公开仅年粒度；Blog补检不等于穷尽全部研究。Feb3临床随机研究按暂缓 AI for Science 范围关闭，不为该负側追时刻。 |
| SRC-META-AI | Research与results page3本日返回切片，有限定位Feb27/26/13/11/10→Jan2→Dec2025，排序为relevance，未把旧年份条目扩队列；stage1_0。 | 受阻 | 当前非时间排序切片不能证明本窗历史完整性。 |
| SRC-QWEN | qwenlm首页有限36行及其qwen.ai/blog动态目标；本窗 Feb2/3定点辅助搜索无可恢复原页事件；stage1_0/stage7_1。 | 受阻 | 动态目录无可提取本窗历史切片，不能把空响应当零发布。 |
| SRC-DEEPSEEK | 官方news研究10标题 Jan28 OCR2→Feb25 DualPath，动态列表最近相关边界未落窗；stage1_0。 | 已检查 | 仅当前官方有限目录，不宣称全网无遗漏。 |
| SRC-MOONSHOT | Platform Blog本日26标题至2025Nov7、MoonshotAI组织有限首页与具名K2.5定位；当前官方K2.5核心PARL段实际读，native datePublished/dateModified无字段；stage2_0/stage8_web/stage10_kimi_poll。 | 受阻 | Platform历史切片未达目标日；K2.5未获本窗首公开/修订日期，不能继承邻日日报处置。 |
| SRC-TENCENT-HUNYUAN | Research超时后恢复原始官方API，pageNum1/pageSize1000/renderType0实际 code0、totalNum9/returned9；最早记录publicAt1770112927与publishedAt1770090898均Feb3 09截点后，本页读完停止；stage4_0/stage5_2。 | 受阻 | 当前9项目录不能证明已删除的更早历史切片；不是把当前无窗内元数据当历史零发布。 |
| SRC-ZAI | 首查Research有限目录Jan19→Feb2 GLM-OCR→Feb11/21；官方release notes Feb3 OCR与当前GitHub核心定点，未扫其他repo；stage2_0/stage4_1/stage6_0。 | 受阻 | Research Feb2与API release Feb3皆date-only且不同事件，必要精度不足；当前仓库Feb12/March12变化不倒推初版。 |
| SRC-BYTEDANCE-SEED | 官方type1 API page0/order_desc=false实际20/total82、next20/hasmore，仅Jan31 A²D→Feb2 SPARKLING→Feb4/5边界完整题摘，未把剩余82项扩队列；type2实际9/total23、最早Feb12窗后即停；stage4_0。 | 受阻 | SPARKLING Feb2发布字段为日期精度，不能当整点午夜首公开；arXiv提交亦非网页首公开证明。 |
| SRC-BAIDU-ERNIE | Blog page1 Jan29 PaddleOCR-VL1.5→Feb6 ERNIE5.0边界；有Next2/2但窗前项已有停止依据，不扫更早page2；stage3_2。 | 已检查 | 仅此官方有限发布目录。 |
| SRC-XIAOMI-MIMO | 首页Paper Jan8→Feb3 HySparse→以后发布、Blog当前15无日期卡；具名HySparse2602.03560v1完整摘要，Submitted Feb3 14:05:57UTC在窗后；stage3_2/stage5_0/stage7_1。 | 受阻 | 官方Paper Feb3 date-only可能与窗相交，但不能证明09截点前；论文事件与网页事件分开。 |
| SRC-MINIMAX | en/cn Blog邻界：英语Jan27 M2her→Feb12 M2.5，中文Jan28→Feb12 Forge；官方Agent techblog.md native完整880字节仅May13条目，停止；stage3_2/stage5_2。 | 受阻 | 本日日期切片不能由当前单条技术目录补齐；不合并中英文不同发布日期。 |
| SRC-ARXIV | 四个ROADMAP主题 Submitted buffer Jan29 19Z～Jan30 18:59Z，model48/48、multimodal46/46、systems12/12；初始agent158返回前50后收窄为题名agent/memory/tool/retrieval/judge（同AI/IR/MA与buffer），实际47/47元数据读完停止（stage23_narrow_agent_poll）。宽表不是逐项题摘队列。CL/DC/AI 2026-02月目录各first25只标题补检，非全月队列（stage9_list_poll）；具名潜在精确v1题摘见stage8/13/14/24/25。catchup、按日list失败；SAIR/HetCCL/GASP三条官方OAI定点恢复与官方datestamp定义读完（stage22）。 | 受阻 | Submitted只是发现；Jan-ID/Available月份与条件排程冲突未解决，OAI last-modification与DOI注册不能证明首次公告。月目录只有身份，无目标日批次。外部限制隔离，不授本窗无遗漏。 |
| 补检：[DataCite](https://api.datacite.org/) | 仅具名arXiv DOI逐项GET：首批与其他潜在的created/registered、v1Submitted/Updated、Available原值；stage11_dc_poll/stage15_dc_poll/stage17_dc_poll。 | 已检查 | 定位元数据公开上界，不是正文机制证据或精确公告日志。 |

### 补充自然日：有限来源差额

本轮原页、主题搜索、实际停止及限制存于[补查记录](../_sources/daily-20260203/supplement-source-owner-pre-20261008.md)和[原页0](../_sources/daily-20260203/supplement-scan-0-20261008.json)、[原页1](../_sources/daily-20260203/supplement-scan-1-20261008.json)、[主题发现](../_sources/daily-20260203/supplement-scan-2-20261008.json)、[官方补检1](../_sources/daily-20260203/supplement-officialsearch1-20261008.json)、[官方补检2](../_sources/daily-20260203/supplement-officialsearch2-20261008.json)。原有有效边界记录只按实际同日元数据复用，不从完成标签推出覆盖；未扫描Weekly或90天catchup。

- **SRC-OPENAI（已检查）**：原 Research/RSS stage4_0 的Feb2–4邻界元数据有效复用；本轮直接读Feb02 Codex app核心。Snowflake原有效贡献前关闭复用；Sora官方Feb03属补充窗外，不迁旧归属。官方Feb02定点补检只发现Codex/既有产品说明和physics应用，停止此结果页。 缺口：本轮native RSS403、web不支持XML，不把失败作零；仅原有限目录与具名原页，不授全站召回。
- **SRC-ANTHROPIC（已检查）**：Research原页本轮仅当前10列表；原 stage2_1/stage3_0 的Jan29→Feb05边界复用。Feb02具名官方Allen/HHMI合作core按AI for Science范围关闭，不扩生物研究队列。 缺口：Research首页不覆盖完整历史；不把原有限研究边界外推所有news。
- **SRC-GOOGLE-AI（受阻）**：DeepMind/Google Research原页与Feb02定点官方主题补检；原Jan Project Genie→Feb Deep Think及Feb月Blog最早Feb03的有限边界复用，目标月查询本轮未恢复。 缺口：Google pubs仍仅年级、当前目录/主题搜索不能证明目标日原始论文完整性；精确恢复该日官方研究列表才重开。
- **SRC-META-AI（受阻）**：原页本轮0可提取行、Feb02定点主题补检；原 relevance page3有限结果事实保留，不授时间覆盖。 缺口：需要目标日时间排序发布切片；空响应不是零发布。
- **SRC-QWEN（受阻）**：qwenlm首页36行与qwen.ai/blog动态0行，本日官方日期补检未恢复具名新事件；停止于这两个入口。 缺口：缺本日官方历史切片，不由动态空页签发无遗漏。
- **SRC-DEEPSEEK（已检查）**：官方原页与news恢复尝试；原Jan28 OCR2→Feb25 DualPath有限目录边界复用，Feb02补检未发现具名本日模型/系统事件。 缺口：本轮news timeout只限制补检；覆盖仅原有限目录，不为privacy窗外政策扩队列。
- **SRC-MOONSHOT（受阻）**：Platform原页实际26项最新Nov07 2025，已到底；K2.5原日期保留不改。Feb02官方主题补检未恢复本日精确事件，不扫描所有组织repo。 缺口：Platform不包含目标日完整Research切片，K2.5需原始发布/重要修订日期。
- **SRC-TENCENT-HUNYUAN（受阻）**：Research本轮timeout；原API9/9目录最早Feb03事实保留，本日官方补检未恢复目标日原始记录。 缺口：当前9项不足排除删除历史；缺目标日官方切片，不把超时作零。
- **SRC-ZAI（已检查）**：首查Research明确Feb02 GLM-OCR、前Jan19/后Feb11，有限边界停止。初始Feb02 README commit 8900d23f恢复并完整读；Feb03 API release及后版SDK/PDF不混作当日机制。 缺口：本日组件组合/单榜未构成具体增量，贡献前关闭，无必要全文缺口。
- **SRC-BYTEDANCE-SEED（已检查）**：type1/year2026/order_desc=false本轮第0页20项、next20/total82/has_more；仅Jan31→Feb02 SPARKLING→Feb04/05边界即停。完整目标题摘和v1必要机制读完；type2原最早Feb12窗后边界复用。 缺口：覆盖这段官方时间目录，不遍历82项或将Submitted视公开。
- **SRC-BAIDU-ERNIE（已检查）**：本轮Blog第1页Jan29 PaddleOCR-VL1.5→Feb06 ERNIE5.0实际边界，Next2/2是更早日期，不继续page2。 缺口：仅当前有限官方目录，不授全机构历史。
- **SRC-XIAOMI-MIMO（已检查）**：本轮首页及原Jan08→Feb03 HySparse Paper邻界复用；Feb03属于补充窗外，不因旧09点隔离重开为Feb02候选。 缺口：Blog卡无日期，不能保证全部历史Blog；缺精确目标日发布切片时仅重开该源。
- **SRC-MINIMAX（受阻）**：本轮en/cn Blog与Feb02主题补检，原Jan27/28→Feb12官方有限边界与techblog仅May13事实复用；giveaway是范围外推广，标题即关。 缺口：历史Agent techblog目标日缺段不能由当前单条补齐。
- **SRC-ARXIV（受阻）**：无catchup。目标日CL/DC列表本轮不可恢复；两次Jan/Feb有限日期主题搜索只发现，并用完整v1题摘定点读02427过程UQ与02140 GapEval。原47/47收窄agent及四主线有限查询保留，不转整月/分类题摘队列。 缺口：原Jan-ID/公告月份/Submitted冲突未解决；新两项Submitted同样非公开日，精确请求见§5。

## 3. 候选与判断

无已确认属于本窗的候选。首批八家族的具体贡献已通过独立校准，但日期冲突使它们不能列为确定候选，已撤去原拟评分与09～12的公开范围；其材料身份、潜在增量和重开条件见§5。不会因有条件的计划排程或findable注册上界自动授日期。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning](https://arxiv.org/html/2602.02472v1) | 2026-02-02 | function-preserving扩张不足→RMS连续及复制optimizer去对称两条件→重考训练状态迁移；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) §一次training step的状态流；root Source/Owner PRE通过，无Books新写 |

该行只属于补充自然日，上文0候选判断针对冻结09点窗口，保持不改。公开日期依据为官方Seed论文目录发布事件，不是arXiv Submitted；root已实际核准入、必要v1正/反侧与Ch28具体覆盖，Source/Owner PRE及DAY均通过。Codex app家族SF-2026-OPENAI-CODEX-APP-20260202已有[02-02原有效候选、深入审阅与Ch66整合](../02/README.md#3-候选与判断)，定点复用其“初始任务数不等于continuation外部输入预算”的受限评价命题、精确当前页面版本及未披露边界，不列为新候选或改判关闭。

## 4. 证据与知识整合

[CONCUR exact-v1](https://arxiv.org/html/2601.22705v1)：日期隔离前实际读§3–5核心与定点Table2/§5.3；AIMD只在agent生成步/工具调用之间pause，不中断in-flight kernel。Table1 DeepSeek TP16/16GPU、Table2写TP8/8GPU，§5.3“846 ms”与Table1秒单位不一致；保留原文，不把两表当同配置因果证明。不外推所有agent、生产SLO或质量保证。日期未解决，以上只是未采用证据笔记，不授审阅完成或Books决定。

[KevlarFlow exact-v1](https://arxiv.org/html/2601.22438v1)：日期隔离前实际读§3–4核心，通信组重新形成、同权重stage替换、GPU后台block复制共同维持请求状态。8/16节点、每节点A10 24GB、1Gbps跨DC、Llama3.1-8B四stagePP、ShareGPT与Poisson到达；大TTFT收益主要来自故障后容量/queue，不能当一般单request执行加速。基线是standard failure behavior，未实际逐系统实现DejaVu/AnchorTP/R2CCL对照；后台复制依赖memory headroom且压力下可丢复制并重算。日期未解决，保留笔记，不授Evidence或Books采用。

[HetCCL exact-v1](https://arxiv.org/html/2601.22585v1)：实际读§3–5与相关限制。vendor-local runtime/编译产物由API间接层与分离device binaries接入，注册buffer用RDMA，另有host fallback；评价只至4节点/16设备、节点内单vendor，BF16模型局部训练不证明bit-exact或完整生产兼容。日期隔离，不采用。

[SAIR exact-v1](https://arxiv.org/html/2601.22397v1)：实际读§3–7。以结构化动作验证器限制跨stage throttle/partition动作、正reward episode检索和多样性选择；coverage/selection误差界依赖平滑性、覆盖与stage瓶颈间隙，不自动保证任意部署。两RTX A6000、四类负载、三seed、30秒准稳态决策，1～2秒LLM决策不支持亚秒controller；GPU share成本与整卡账单不同，不授fleet通用降本。日期隔离，不采用。

负侧：[Snowflake](https://openai.com/index/snowflake-partnership/)官方合作正文是既有Cortex SQL/GPT接入及未来SDK路线，没有新系统接口/机制；[Sora](https://openai.com/index/sora-feed-philosophy/)核心是既有生成guardrails与feed eligibility分层、teen筛选、人工报告/下架及个性化关闭的政策说明，没有新增可支持的执行机制、有效性条件或安全反证。两者root已实际核心校准通过，不是以“没有controlled benchmark”自动拒绝安全研究。[REKD2601.22531v1](https://arxiv.org/abs/2601.22531v1)完整题摘仅teacher rationales/predictions组合在分类收益，无新增训练系统边界，root抽样通过。三项是贡献前关闭，不为不改变处置的日期追加调查。

当前纠错/撤回定点：EUGens22563v2说明拟替代更新2410.09771，Sparse-or-Dense22795v2说明实验代码错误影响§4/5，MoR00485v2说明需重大修订；native exact-v2原页状态与时间见[必要原始记录](../_sources/daily-20260203/feb03_withdrawal_exact_versions.md)。全部不入选、不评分、不Books。EUGens的v2 Submitted Feb2 17:47:29UTC在本窗，但仍不是公开撤回时刻；April/March撤回仅当前安全处置，不倒灌为本窗发布事件。无既有本轮Books依赖需清除。

### [SPARKLING: Balancing Signal Preservation and Symmetry Breaking for Width-Progressive Learning](https://arxiv.org/html/2602.02472v1)

必要§3–5及相关推导/配置已读。前向激活RMS条件与反向复制状态的去对称是两问题；仅边界loss不跳变不能代替扩容后canary。Figure2固定RMS后比较optimizer状态处理，Figure3再比较rewarm，支持受限分解；方差公式有centered/独立/同方差条件，不推广c>1不均匀复制。

作者评价为OLMoE风格、200B tokens/100B处扩张、inner/hidden/joint轴，64×A10080GB、seq4096、batch768/microbatch3；precision及重复seed Not Disclosed。Table1平均下游改善但最终pretraining loss仍劣于from-scratch，预算同tokens不是同FLOPs；35%来自6ND估算，不授普遍端到端降本或免调参。未复现实现/实验。具体原证及采用/未采用边界见[Source/Owner PRE](../_sources/daily-20260203/supplement-source-owner-pre-20261008.md)。`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)实际已有mapping→scale→新状态差异→rewarm→rollback链与SPARKLING Experimental引用；root已独立实读必要v1正/反侧、Ch28完整相关邻接与源注，通过已有覆盖/No Change及DAY，不新增Books写入。

## 5. 缺口与下一步

本窗普通待办0。作者侧发现、有限筛选与安全隔离已收束，非作者日级复核已通过。以下是已隔离的外部终态保留项，不评分、不用于正面Evidence、不进入Books，也不支持Coverage通过、无遗漏、性能或安全保证。不是以外部标签替代未读正文的普通待办。

首批八个潜在家族：完整v1题摘与具体贡献8/8经root实际校准；公开日期仍冲突，尚不是本窗候选。

| 材料身份 | 已校准的潜在增量（不是采用结论） |
| --- | --- |
| [SAIR22397v1](https://arxiv.org/abs/2601.22397v1) | 单stage阈值不足→跨stage动作与历史检索→需重考controller coverage/selection误差。 |
| [KevlarFlow22438v1](https://arxiv.org/abs/2601.22438v1) | 通信组初始化与权重生命周期分离、后台KV复制→需重考PP故障域/请求恢复。 |
| [HetCCL22585v1](https://arxiv.org/abs/2601.22585v1) | vendor backend分离与RDMA集体通信→需重考跨vendor runtime兼容边界。 |
| [CONCUR22705v1](https://arxiv.org/abs/2601.22705v1) | Agent寿命内工作集而非瞬时request准入→需重考工具暂停导致的KV thrashing。 |
| [AscendCraft22760v1](https://arxiv.org/abs/2601.22760v1) | 显式Ascend执行语义DSL及受约束lowering→需重考自动kernel生成的验证接口。 |
| [FOCUS23278v1](https://arxiv.org/abs/2601.23278v1) | 尚不可decode状态与importance预算/eviction→需重考diffusion的计算集合及cache边界。 |
| [Symmetry22257v1](https://arxiv.org/abs/2601.22257v1) | 移除无效旋转自由度→需重考attention优化轨迹与低状态optimizer条件。 |
| [MixQuant22347v1](https://arxiv.org/abs/2601.22347v1) | block l1mass几何边界、可折叠permutation→需重考Hadamard块大小/校准选择，不沿用后版名称。 |

它们以及同类Jan-ID潜在的必要缺口相同：[官方availability](https://info.arxiv.org/help/availability.html)的“A note about arXiv-id assignments”（本轮stage3_1原文L175–176）明确ID按first announcement月份且不可backdate，Jan-ID/Available='2026-01'与Submitted+received/accepted条件排程推定Feb2有直接冲突；49条具名DOI字段各自保存在stage15/17，不能用代表推全部落窗。仅对SAIR22397、HetCCL22585及GASP00173恢复官方OAI；前两datestamp2026-02-02、后者2026-02-03，但官方OAI定义为最后修改日期，可含行政/书目更新，非初始公告日志。DataCite registered给公开元数据上界，不给正文精确首公开；Available粗月亦不推任意精确Jan时刻。catchup/按日list不可用，已有限停止，不为全池扩全文。可接受替代是实际官方公告批次、精确初始公開字段或作者可核首次正文公开记录，能消除上述冲突；只重开所证实材料及真实归属日，再续必要证据/Books比较。

同类已读完整v1题摘的潜在身份及具体贡献保留在stage13/14：TA-GRPO22478的等价变体奖励池、ES-SSM22488预算可截断状态、Shattered22510组合推理失效、SpanNorm22580方差与深度边界、Consensus22614注意力替代稳定性、Periodicity22690周期OOD反证、SparseKernel22766稀疏概率核、HSM22852层间attention分配、PPL22950连续性/低困惑度反证、Sink22966归一化压缩代价、Perm22980可微权重匹配、MemT23014树式信用记忆操作、RLRR23058排序奖励、SymbolInvariant23169符号重命名不变性、Yurii23236动力学分解；VMonarch22275视频因子化、CARE22467弱视频动作预训、Projector22468早期采样漂移、VideoCD22574时空负特征、PhoStream22575过早作答盲区、LINA22630线性注意力归一化、VisionTrim22674视觉token选择/合并、Consistency22679自蒸馏退化、GRACE22709置信门控量化蒸馏、SIDP22965采样奖励模仿、OSGA23041共享语义方向、LGFlow23087时序正则latent action、Video-o3 23224任务隔离工具轨迹、JAF22269组级judge关系选择、FLARE22311有限承诺lookahead、ERR22352可恢复性regret、DMS22528轨迹单元memory选择、RETab22530中间表状态验证。它们未获本窗日期、独立贡献/Evidence通过或评分；列身份不是将宽目录变必读队列。具名题摘阶段保存原有准确标题，后版改名不倒灌v1。

安全/纠错信号不会因日期隔离而被当普通负侧关闭：[VL jailbreak22398v1](https://arxiv.org/abs/2601.22398v1)的CoT隐蔽/迭代图像攻击、[LinguaSafety22737v1](https://arxiv.org/abs/2601.22737v1)的多语种图文攻击差异、[AP2Whispers22569v1](https://arxiv.org/abs/2601.22569v1)的工具购物agent注入/外泄、[Judge self-preference22548v1](https://arxiv.org/abs/2601.22548v1)的质量混杂纠偏、[DeepHallu22984v1](https://arxiv.org/abs/2601.22984v1)的过程轨迹幻觉盲区、[TriCEGAR22997v1](https://arxiv.org/abs/2601.22997v1)的反例驱动抽象/概率验证，均完整题摘已读，潜在可改变具体可靠性/评价判断。缺首公开归属，保留而不采用；未来恢复日期才核必要核心，不为日期受阻把安全研究以无benchmark排掉。

收窄agent入口的其他具名潜在完整v1题摘见stage25：PerfGuard22571工具performance边界、Inspector22588生成与语义probe能力差异、EigenData22607实例验证器/模拟器驱动RL、Symphony22623异构模型MCTS、TMoW22647 test-time世界模型混合、Best-of-Q22701冻结VLM+离线Q选择、AutoRefine22758轨迹复用技能/子agent（v1不是后来typed-artifact标题）、MobileGen22781能力前沿轨迹合成、MoVE22887跨层值bank解耦容量/compute、AutoTraj23032修复轨迹与reward监督、Principal-Agent23211激励/信息不对称、MonoScale23219 onboarding信任域memory更新。Jan-ID/提交字段不能解决首公开归属；ToolTok2602.02548、SEAM2602.02556、TessPay2602.00213亦只有提前Submitted与Feb-ID，不能定位具体Feb日。定点重开条件同上，未逐项授贡献通过。

其他原始潜在（保留原窗判断，补充自然日已解决项见下一段）：SPARKLING（Seed Feb2 date-only，扩宽时RMS尺度保持/非对称优化重启可能改变增长稳定性）、GLM-OCR（Research Feb2与API release Feb3不同事件，视觉encoder/0.5B decoder与layout→并行recognition两阶段）、HySparse（官方Feb3 date-only，full layer复用KV/selection的hybrid机制；论文Submitted已窗后）、Kimi K2.5（当前官方PARL trainable orchestrator/frozen children、并行/完成奖励与CriticalSteps机制，首公开/重要修订日期缺失）。原页日期不能把区间完全夹入原09点窗口；必要是事件对应的官方精确发布日期记录，而非当前repo更新/宣传指标。已获取完整题摘或官方核心说明，不等于四份全文均已深审。

本次date-only裁决解除上段SPARKLING与GLM-OCR的补充窗时刻障碍：前者官方Feb02目录事件新增准入并完成必要深审/已有覆盖，后者Feb02初始README核心按具体增量关闭，不再请求时分秒或将它们当普通日期待办。HySparse官方Feb03是补充窗外，旧记录仅保留不迁日；Kimi缺事件公开/重要修订日期仍隔离，其必要请求是日期而非精确时刻。其他旧Jan-ID日期冲突尚未消除，不因换自然日笼统授通过。

Feb-ID完整题摘潜在见stage8：CBO00161块式Ising选择、BenQ00165归一化量化网格、GASP00173污染/修复self-play、IVO00175 latent unlearning攻击反证、DA-GRPO00166分布式advantage预算、Dispersion00217 condensation与distillation区别、EigenAI00182 bit-exact TEE验证。CBO/GASP注册上界在Feb3 09BJT后不能反推此前首公开；其余各自字段保留，不推整批日期。月目录定点见GMemLLM00015 frozen-backbone GRU memory、RDD00150可逆remasking/cache潜在，只有较早Submitted与Feb-ID，亦缺首公开日。必要替代/重开条件同上。

窗外线索不扩本窗：L-ICL00276、LatentCoT00449、FT-HSDP00277、PROBE00509的精确v1提交均晚于Fri Jan30 14Eastern cutoff，因此依官方received AND accepted规则最早公开为Feb3 09BJT（本窗不含终点），还可能因moderation更晚；不虚构实际公告时刻。待真实归属日核必要机制，不作为本窗遗漏或Books待办。

补充完整题摘身份：SixSigma22290的独立错误假设下共识可靠性、MERMAID22361跨claim evidence memory、MetaLead22420全部实验/训练测试分账数据、Forecast22444自动生成/延后resolution评价流水线（stage14），以及FastAPI-vs-Triton00053的单请求/批处理成本质量取舍（stage8）。原文未解决本窗首次公开定位；不为指数式宣传、条目规模或熟悉机制自动准入，也不授排除贡献的独立通过。若恢复实际公开事件，只重开该具体命题与必要核心，当前均为日期终态保留。

历史来源切片限制详见§2：Google pubs、Meta relevance、Qwen动态目录、Kimi Platform、Hunyuan当前9项与MiniMax单条Tech目录不能证明完整历史；恢复可用目标日官方切片时仅重开该源与受影响项。

### 补充自然日停点

本轮普通待办0。root已通过SPARKLING非作者准入、必要Source与已有覆盖PRE、GLM-OCR具体增量关闭及完整六部分DAY；Codex app经定点核原有效候选/证据/整合后按同事件去重复用，作者先前以产品组件组合关闭整个家族的提案已撤销，不重开或推翻原评价命题。完成根据本次实际DAY，不沿用原完成标签；以下日期/历史来源限制为明确隔离的外部终态保留，不授正面Coverage/Evidence。

终态日期保留（不评分、不采用、不进Books、不证明覆盖）：[Embedding Perturbation2602.02427v1](https://arxiv.org/abs/2602.02427v1)完整题摘提供embedding扰动敏感度的过程UQ sensor；[GapEval2602.02140v1](https://arxiv.org/abs/2602.02140v1)完整题摘提供同问题双向评价/知识操作反证。仅Submitted Feb02无法确定首公开，需官方目标日公告批次或作者可核首次正文公开日期记录；当前可用精确abs/列表/定点搜索已停止，后续仅重开所证实项与真实归属日，不继续无关全文。

原§5日期/历史来源保留继续有效，不重复请求；SPARKLING仅新增自然日事件恢复，原段不删。GLM-OCR新初版core因没有具体可保留增量关闭，不再作为新增普通日期待办；HySparse官方Feb03明确补充窗外，原记录不迁移。

## 6. 复核

复核者：root（非作者）。
结论：通过

以上字段保留原冻结窗口的有效复核。

补充复核者：root（非补查报告作者）

补充结论：通过。

root实际读全部README增量diff及六部分、14条补充来源范围/停止与限制、唯一新增SPARKLING证据与Ch28实际已有覆盖、两项精确日期请求、Codex去重和旧有效证据复用、原§5与本次状态区分；实际读本日原页scan0/1与日期边界，并fresh打开02427v1/02140v1完整题摘，不将Submitted授公开日。SPARKLING必要正反侧/Ch28具体正文和GLM初始core此前已独核，分批结果复用，不是第二人无差别重读全部旧附件。共同错误“成熟产品组件不足→关闭整个Codex家族”已更正为同事件去重复用原有效continuation评价命题。无Books新写入，No Change充分；不授全Coverage或无遗漏。作者只同步root实际裁决，不自授日级通过。

以下保留原冻结窗口复核范围；验收的是本窗安全终态，不是日期保留项的正面证据通过。
root实际通过首批8/8具体贡献校准及Snowflake/Sora/REKD三个负侧核心校准；不是第二人全量深读全部原始命中。定点核SAIR/HetCCL日期原字段、三OAI代表及last-modification边界，live核官方availability的first-announcement原句，原确定候选/评分/范围已撤下。进一步读22398、22737、22569、22548、22984、22997的完整v1题摘，核安全、评价反证和验证信号仍被具名保留而非误排；实际打开22563v2、22795v2、00485v2的官方Comments/Submission history/Withdrawn，确认当前撤回不采用、后来说明不倒灌为本窗事件。十四来源有限停止、收窄的47/47 agent查询与完整六部分已核，未把宽列表升级为全部必读或声称全量召回；日期和历史切片保留项均不支撑候选、Books或覆盖保证。Books无本日写入；作者不自行验收。validator及限定git diff --check通过，只证明格式与限定范围一致，不替代上述语义验收。

本轮完成态V3校验、限定unstaged/cached diff检查、原窗口与0原候选行保留、连续原§4逐字前缀检查通过；日报14＋Source/Owner记录7个本地引用0缺失，10个新增JSON解析通过。机器检查仅证明这些接口/范围事实，不替代root上述实际DAY；未stage、commit或push，本日结束。
