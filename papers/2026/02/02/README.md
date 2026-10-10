# Daily Research — 2026-02-02

**规范：** V3
**窗口：** 2026-02-01T09:00:00+08:00 ～ 2026-02-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T12:11:03+08:00
**窗口说明：** 用户授权只补已有报告来源遗漏；原窗口、候选日期、评分与有效审阅冻结保留。
**补充窗口：** 2026-02-01 ～ 2026-02-01

## 1. 结论

2026-10-08补查：原1家族冻结，补充Feb1自然日新增1个共同报告家族，合计2；新家族标准完成、仅报告，不新增Books。8个OpenAI安全页按共同报告归并，采用单次拒绝与活动最终结果不可混同的受限部署观察，不证明替代模型执行、真实规模或总体阻断率。14源有限扫描已停止，ByteDistill公开日和具名历史切片终态隔离；首批/必要Source及六部分DAY均已由非作者root实际通过，本轮普通待办0；历史限制不授零发布、无遗漏或全源正面Coverage。

以下三段为2026-10-02原轮已完成范围，数量和工作状态只指原窗口；不替代上面的补查合计与本轮实际验收。

本窗确定入选1个唯一材料家族：Codex app 发布案例披露的随机 continuation protocol，使“初始任务数量”与“整个 run 的外部指令预算”必须分账。贡献不是产品界面、七百万 tokens 或通用自主性表现；一次初始任务与自动续跑不矛盾。完成标准核心审阅，并针对当前 Ch66 的具体评价知识缺口加深；两段及证据注已写入唯一 owner `PLATFORM-EVALUATION-SYSTEM`，root实际写后及日级非作者复核通过，本窗可执行工作0。

14个每日源均进行了本轮有限检查；没有扫描每周来源、没有把整类/月度目录变成逐项题摘队列。RSS的1243条、arXiv的4363条月总量等只用于目录定位，不是本窗候选数或全文审阅分母。三项具体潜在材料（SPARKLING、GLM-OCR、Kimi K2.5）因本窗事件日期或初版身份未成立而终态隔离：不列正式候选、不评分、不进 Books，也不算正面证据或无遗漏保证。部分动态/历史目录的切片限制见§5。

本轮只从原始入口独立发现与筛选。旧日报已原文备份为 [LEGACY_README](../_sources/daily-20260202/LEGACY_README.md)，未用于准入、评分或结论；月 `_sources/daily-20260202` 中既有的旧 inventory、screening-ledger、coverage-receipt、Books queue 等保持原身份、未读未改。下文引用的 `feb02_` 文件才是本轮原始访问记录，不另维护候选投影或完成收据。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 [RSS](https://openai.com/news/rss.xml) 本轮取得1243条，仅提取Jan29～Feb3邻域；Feb1八个安全案例RSS 00:00 GMT＝08:00北京，位于本窗起点前；Codex app Feb2 00:00 GMT＝08:00落窗；Snowflake Feb2 06:00 GMT＝14:00、Sora Feb3均窗外。只深入Codex app产品核心与完整demo提示/续跑说明；停止于这个事件邻域，不把全feed变成题摘队列。[RSS原值](../_sources/daily-20260202/feb02_metadata.json)、[必要正文](../_sources/daily-20260202/feb02_web0.json)。 | 已检查 | native正文403后已由原始网页恢复；当前页标March4 Windows更新，采用当前披露的案例解释，不主张Feb2初版精确措辞已核。 |
| SRC-ANTHROPIC | 官方Research本轮HTML含174条metadata，只抽目标邻域：Jan29 19:13:26.601Z Coding Skills（Jan30北京）与Jan28 Disempowerment之后，下一Research事件为Feb5 00:00Z Zero-days；本窗未定位条目，停于邻域而非174题摘。[原始metadata](../_sources/daily-20260202/feb02_metadata2.json)。 | 已检查 | 结论仅限当前官方publishedOn目录邻域，不称整个互联网无遗漏。 |
| SRC-GOOGLE-AI | DeepMind blog page4→page3有限相邻页定位Jan/Feb交界；定点原页本轮核Project Genie Jan29及Deep Think Feb11，均非本窗。Google Research pubs打开当前页面，辅助精确Feb1/Feb2模型/Agent主题查询没有返回本窗原稿；没有把科学应用或全年pubs列为审阅队列。[page4/Research](../_sources/daily-20260202/feb02_web0.json)、[page3](../_sources/daily-20260202/feb02_web6.json)、[原页日期](../_sources/daily-20260202/feb02_web8.json)、[DeepThink日期](../_sources/daily-20260202/feb02_google_dates.json)。 | 受阻 | Research pubs当前界面不是完整的本窗首次公开历史切片；辅助空搜索不能证明零发布，精确隔离见§5。 |
| SRC-META-AI | Research根页本轮0可读正文；官方publications结果page3、sort_by=relevance读取有限返回，Feb27/26/13/11/10→Jan2→Dec2025邻域未定位Feb1/2条目，后部更早标题不扩题摘。[本轮原页](../_sources/daily-20260202/feb02_raw1_1.json)。 | 受阻 | relevance分页不是按公开时间穷尽；根动态页及本窗完整历史事件切片未恢复，不以这一页宣称零发布。 |
| SRC-QWEN | qwenlm.github.io当前36行旧站/跳转，内容停在2025；qwen.ai新Blog本轮0可读正文；限定官方域Feb1/Feb2/ISO日期补检未返回条目。实际停止于旧站/新入口/这组日期查询，没有扩搜第三方库存。[入口](../_sources/daily-20260202/feb02_raw1_1.json)、[查询](../_sources/daily-20260202/feb02_web4.json)。 | 受阻 | 必要的新站动态历史目录无法取得；搜索无结果不当本窗无研究。 |
| SRC-DEEPSEEK | 官方News本轮有限research/dynamics数组：research十条，Jan28 DeepSeek-OCR2→Feb25 DualPath；dynamics当前列Dec1→Apr24→Sep10。只取本窗两侧metadata，未定位本窗事件。[原页](../_sources/daily-20260202/feb02_web2.json)。 | 已检查 | 当前有限官方数组不保证所有独立原稿首公开均收录。 |
| SRC-MOONSHOT | Platform Blog本轮26条，最新2025-11-07、列表含2024/25；MoonshotAI org当前首10/42仓库仅用于定点定位K2.5官方链接；随后读当前K2.5 Blog PARL核心（orchestrator/frozen subagents、奖励退火与critical steps），未遍历42仓库或其历史。[目录](../_sources/daily-20260202/feb02_web2.json)、[原始核心](../_sources/daily-20260202/feb02_web8.json)。 | 受阻 | K2.5原页“Today”无可核公开日期，本窗首次公开或重要修订事件未成立；当前平台目录不是完整2026历史切片。 |
| SRC-TENCENT-HUNYUAN | Research网页本轮正文接口错误，改从官方前端所用 [publicList](https://api.hunyuan.tencent.com/api/blog/publicList) 本轮POST pageNum=1/pageSize=1000/renderType=0提取全部9/total9当前返回。最早Learning from context的publicAt=1770112927（Feb3 18:02:07北京），publishedAt=1770090898（Feb3 11:54:58北京），其余更晚。API提取成功，不再做无必要动态UI全站检索。[错误](../_sources/daily-20260202/feb02_web5.json)、[九条原字段](../_sources/daily-20260202/feb02_metadata2.json)。 | 受阻 | 九条是当前目录完整返回，不是目标历史窗口原目录；旧历史条目保留情况未知，不把当前最早Feb3外推为本窗零发布。 |
| SRC-ZAI | 首查Research Jan19 GLM4.7Flash→Feb2 GLM-OCR→Feb11 GLM5→Feb21报告；同时核官方release notes的Feb3 GLM-OCR API事件，读当前GLM-OCR GitHub核心及Feb12/March12更新标记；两事件不静默合并，未以March技术报告冒充Feb初版。[Research](../_sources/daily-20260202/feb02_web2.json)、[notes](../_sources/daily-20260202/feb02_web6.json)、[GH核心](../_sources/daily-20260202/feb02_web5.json)。 | 受阻 | Research Feb2只有日期，首版release的时刻/对应核心版本未成立；潜在贡献日期隔离见§5。 |
| SRC-BYTEDANCE-SEED | 本轮官方get_article_list_v2，type1/publish_year=2026/count=100/order_desc=false，实际首批20/total82、next_page_token=20/has_more=true，读取目标邻域Jan31 A²D→Feb2 SPARKLING→Feb4 VTok→Feb5，后续窗外页不扩。SPARKLING完整题摘与exact-v1公开页定点核。type2同参数实际9/total23，首3为Feb12/13/14，next20/has_more=true，停止本次升序初段；不称23项全量完成。[type1题摘及分页](../_sources/daily-20260202/feb02_metadata2.json)、[v1](../_sources/daily-20260202/feb02_web6.json)、[type2实际返回](../_sources/daily-20260202/feb02_auxiliary.json)。 | 受阻 | SPARKLING显示Feb2 date-only，与本窗仅00～09相交；type2返回量/total不一致，不把该接口当完整历史目录。 |
| SRC-BAIDU-ERNIE | 官方中文技术Blog当前第1页（页面标2页），Jan29 PaddleOCR-VL1.5→Feb6 ERNIE5.0已跨过目标窗口；本轮在这相邻边界停止，未扩第2页更早历史或普通PR。[原页](../_sources/daily-20260202/feb02_raw3_1.json)。 | 已检查 | 范围为当前官方技术Blog日期邻域，不是全部GitHub事件穷尽。 |
| SRC-XIAOMI-MIMO | 正确官方主页本轮Paper列表Jan8 MiMoV2Flash→Feb3 HySparse；15个Blog卡片无日期，仅作本窗原始线索，没有把当前模型/模板全部送审。[页面](../_sources/daily-20260202/feb02_raw3_1.json)。 | 受阻 | 无日期Blog的本窗历史事件切片未恢复；Paper边界核实不补足该缺口。 |
| SRC-MINIMAX | 本轮英文Blog Jan27 M2her→Feb12 M2.5→Feb14 Forge，中文HTML Jan28 M2her→Feb12 Forge，保留两语言原日期，不强行统一。Agent Tech Blog网页失败后官方techblog.md成功，本轮当前完整880-byte页面只列May13一项。各入口停于这些有限邻域/当前返回，不扩docs全树。[en/cn](../_sources/daily-20260202/feb02_raw3_1.json)、[cn及TechBlog恢复](../_sources/daily-20260202/feb02_auxiliary.json)。 | 受阻 | 普通Blog本窗未定位事件；TechBlog当前单项不恢复目标历史目录，不能证明当时零发布。 |
| SRC-ARXIV | 本轮读官方 [availability](https://info.arxiv.org/help/availability.html)：冬季Sun～Thu 20:00 Eastern公告＝次日09:00北京；本窗没有计划公告，Sun Feb1 20:00公告恰为本窗不含的终点。以cs.AI/2026-02?skip=0&show=25首25/4363标题作有限公告边界补检，2602公告不早于终点，不将月目录变题摘队列。另执行四组明确日期＋模型/多模态/系统/Agent主题辅助查询，返回的较晚Feb/March/Aug或2025/24结果非本窗，未扩池。[官方说明](../_sources/daily-20260202/feb02_web0.json)、[25标题](../_sources/daily-20260202/feb02_web4.json)、[四主题原查询](../_sources/daily-20260202/feb02_raw7_0.json)。 | 已检查 | 公告窗口不等于作者独立网站首公开；Submitted不是公开。辅助索引非严格日期召回，不用它证明全学科或全站无遗漏。 |

没有触发独立的每周源或会议/release全站扫描。必要的GLM-OCR GitHub、K2.5官方Blog、SPARKLING exact-v1都属于具名材料的定点核验，不增加来源家族或扩大每日池。


### 2026-10-08 补充来源（2026-02-01自然日）

原表记录冻结，只适用于原窗口。以下是本轮实际入口、有限停止和限制；不由原完成状态授新覆盖。完整查询及原件路由见[补查停点](../_sources/daily-20260202/supplement-20261008.md)。

- `SRC-OPENAI`：本轮RSS1255项只取Feb1/Feb2；八个Feb1安全页必要核心，按共同报告家族归并；停于具名案例，不扩完整地缘PDF。 结果：已检查；缺口：作者检测/OSINT局部观察，不证明真实规模或总体阻断率。
- `SRC-ANTHROPIC`：官方Research174 dated metadata，仅核Jan29 Coding skills→Feb5 zero-days邻域，无Feb1条目；不将174正文变队列。 结果：已检查；缺口：当前目录有限邻域，不声称所有独立发布均收录。
- `SRC-GOOGLE-AI`：当前pubs年度/首15不是本窗历史切片；DeepMind page4/page3不可读后有限恢复，定点官方Project Genie Jan29与Feb1模型/系统主题查询，未扩全年库存。 结果：受阻；缺口：本窗pubs/DeepMind历史事件切片未恢复，查询空不能证明零发布。
- `SRC-META-AI`：Research0行，publications page3本轮不可读；限定官方域Feb1模型主题查询只返回非本窗应用说明，停止于这组入口。 结果：受阻；缺口：必要Feb1历史目录尚缺；不是全年论文已读。
- `SRC-QWEN`：旧站2025正文/redirect、新Blog0行；日期/模型Agent限定检索恢复官方索引Qwen3-Coder-Next Feb2、ASR Jan28，只作边界，不改候选归属。 结果：受阻；缺口：新站完整Feb1切片未恢复；Feb2不入本补充窗。
- `SRC-DEEPSEEK`：官方news研究Jan28 OCR2→Feb25 DualPath、动态Dec1→Apr24邻域，未定位Feb1，停止当前有限目录。 结果：已检查；缺口：当前索引不穷尽所有独立原稿。
- `SRC-MOONSHOT`：Platform26项至2025，org首页10个repo仅定位K2.5；限定Feb1原始域检索，旧PARL有效core复用但未建立新事件。 结果：受阻；缺口：Feb1历史切片及K2.5本窗事件日期/版本未知。
- `SRC-TENCENT-HUNYUAN`：Research timeout后官方publicList page1/pageSize1000/renderType0实回9/total9，仅读取日期metadata；最早Learning from context的两公开字段均Feb3，停。 结果：受阻；缺口：当前九条不是Feb1历史目录；旧条目保留未知，不能称零发布。
- `SRC-ZAI`：Research Jan19 Flash→Feb2 OCR边界；不重新评分Feb2旧hold；有限Feb1查询未建立新事件。 结果：已检查；缺口：原GLM-OCR版本hold继续作为原窗记录；不声称全Github事件覆盖。
- `SRC-BYTEDANCE-SEED`：type1升序2026 count100实回20/total82/next20，Jan31 A²D→Feb2 SPARKLING已越过Feb1，停首段；type2实回9/total23/next20，首3为Feb12～14，日期辅助检索未建立Feb1事件。 结果：受阻；缺口：type2有限返回与total差额；不把接口声明数当已读分母或历史零发布。
- `SRC-BAIDU-ERNIE`：技术Blog第一页Jan29 PaddleOCRVL1.5→Feb6 ERNIE5.0邻域停止，不扩更早第2页。 结果：已检查；缺口：当前技术Blog邻域，不穷尽所有版本仓库事件。
- `SRC-XIAOMI-MIMO`：Paper Jan8→Feb3 HySparse，15个无日期Blog卡片只作目录线索；Feb1有限日期查询后停。 结果：受阻；缺口：无日期Blog本窗事件切片未恢复。
- `SRC-MINIMAX`：en/cn Blog本轮有限入口，cn Jan28 M2her→Feb12后续越过Feb1；TechBlog HTML外壳后markdown恢复当前May13单项，停止，未扩docs树。 结果：受阻；缺口：AgentTech历史切片未恢复；当前单项不能证明当时无发布。
- `SRC-ARXIV`：实核官方availability、四组日期主题＋四同义组；唯一相关新线索2602.01007v1完整题摘/作者仓库有限日期恢复。cs.CL Feb月首25题名仅有界查漏，不转逐项队列；无catchup。 结果：已检查；缺口：日程没有本北京Sunday计划公告是推断，不证明独立站零发布；ByteDistill公开日保留，不用Submitted作落窗依据。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/) | 2026-02-02T08:00:00+08:00 | 原“单一初始任务”叙述可能被当作整个run只有一次外部指令→原文另披露随机持续continuation→长期评价需分离初始任务和controller续跑输入；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 长任务run contract](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际两段及末注，root写后复核通过 |
| [OpenAI February 2026恶用报告：Cyber Special Operations及共同案例](https://openai.com/index/disrupting-malicious-uses-of-ai-cyber-special-operations/) | 2026-02-01 | 单次拒绝不能证明跨模型/人工工作流终止→后续状态文本与部分OSINT匹配是受限反侧→分开拒绝事件与活动结果；2+2+2=6 | 标准完成 | 仅报告：具体部署观察不披露新的防护机制，无Books新写入 |

## 4. 证据与知识整合

### [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)

唯一家族为 `SF-2026-OPENAI-CODEX-APP-20260202`。采用精确对象是2026-10-02本轮访问的当前官方发布页及官方RSS事件；不是未经保存的Feb2初版。RSS `pubDate=Mon, 02 Feb 2026 00:00:00 GMT` 转为北京时间Feb2 08:00，完全落窗。原网页L50明确March4新增Windows更新；本报告保留当前披露范围，不声称L217的精确字句在初版同位出现，也没有证据据此制造一个新的March修订候选或日期冲突。

必要HTML审阅范围为产品核心L50～113、demo初始任务L212～216、持续续跑说明L217与示例L219。L67说明作者赛车游戏demo累计超过七百万tokens和一次初始用户任务；L217另说明持续reprompt，从十条通用提示中随机选择，L219示例要求继续添加功能、游玩检查、每次改动后测试/修bug。两者陈述的单位不同，不构成自相矛盾。“持续”不能反推精确触发条件或次数，自动续跑不证明人工干预，也不证明模型无法自主执行。该示例没有控制无续跑基线或重复运行，因此不将tokens或demo完成视作机制收益、自主性、成本效率或生产能力的benchmark。

本项评分针对新增的、受限的评价身份边界：Design Delta 2（初始目标计数与外部continuation预算不能混同），System Reach 2（harness/controller与agent执行跨边界），Durability 2（可复用run identity约束）。不是为产品名、worktree功能或成熟原则评分。模型精确配置、硬件、完整continuation发送次数/时间、触发/停止条件、重复试验、质量evaluator和SLO为 `Not Disclosed`；质量/成本因果收益没有采用，论文式训练/硬件对照对此局部披露不适用。未读无关skill仓库，未运行demo、未复现实验。

Books写前实际比较Ch66 subject/harness及长任务段：已有task/instruction/evaluator revision、turn/tool-call数量、observation/evidence shape、压缩和final outcome；却未完整承载“初始任务数量≠外部续跑指令预算”的论点。已读所需项目/学习/写作上下文及Ch65→66→67交接，root实际核必要原文、当前owner和拟两段后批准唯一段落ownership。实际新增位于AgentLongBench evidence-shape段之后、Pass@k小节之前的两连续段及章末一条同家族证据注；不改Agent章、不新增索引或结构候选。冻结continuation集合/版本、触发与实际次数、停止/资源预算是本书设计要求，非作者已验证效果；两段保留旧单一task方案在有限demo下仍合理的解释，不以新案例覆盖旧evaluation设计。

代表性准入前关闭：同页多线程、worktree、skills和automation说明产品组织方式；sandbox一节明确承接既有CLI模式，未披露新的隔离/授权contract或足以改变旧设计选择的反证，因此不作为其他候选。这不是因其为产品Blog而拒绝安全/可靠性贡献；若出现具体新的失效或contract改变须重开。Feb1八个安全页在本轮RSS中位于起点前，未见本窗新事件提示，未把前日处理结果或零候选数当作本日依据。


### [OpenAI February 2026恶用报告：Cyber Special Operations及共同案例](https://openai.com/index/disrupting-malicious-uses-of-ai-cyber-special-operations/)

本轮补充家族为 `SF-2026-OPENAI-DISRUPTING-MALICIOUS-USES-FEB2026`。八个官方页面共同指向Feb2026报告；RSS与页面均核Feb1，新增按完整自然日，不因原09:00起点排除。采用精确对象是2026-10-08访问的这些官方HTML，不声称早期PDF各版本已比较。[原件与停止](../_sources/daily-20260202/supplement-20261008.md)。

Cyber Special Operations必要位置为Actor/Behavior、Operational Planning and Reporting及Impact。作者记录一次规划请求被拒绝，后来收到相关状态文本并发现部分跨站匹配；这足以反驳“此调用拒绝就证明整条活动结束”的推断。用户报告与局部外部匹配不因果证明替代模型如何执行、为何继续或真实规模，也不建立一般阻断率。未比较各安全系统效果，未复现调查；不读整份无关地缘历史附件。

评分2+2+2=6仅针对这个部署反侧：拒绝事件与活动结果要分开，跨模型/人工与分发跨边界，限定可复用。其余案例只是共同家族的上下文/反侧，不分别评分：Romance的阶段命名沿用旧概念；Fish Food的同批传播差异提示分发混杂、没有识别因果；False Witness/Date Bait影响依赖用户自报；Silver Lining未确认发送结果。不能把安全题材、workflow标签或规模数字当新增机制。模型精确配置、完整安全检测协议、对照和整体影响为 `Not Disclosed`；普通硬件/SLO对该观察命题不适用。

root已独立核Cyber Special必要核心及Fish Food/Romance反侧，首批准入与受限Source结论通过。Books决定为**仅报告**：新增的是具体部署观察，不是新的隔离、分类器、授权或跨模型防护机制；通用“局部拒绝不能外推端到端效果”不足以单凭此案例制造书稿diff。本轮无Books写入，原Codex Ch66有效结果不变。日级六部分验收已由非作者root实际通过。

## 5. 缺口与下一步

### 补充窗口的实际限制与停点（2026-10-08）

本轮普通可执行工作0；独立DAY验收已由非作者root实际通过，状态同步完成。原段落的“本窗可执行工作0/已通过”仍只指原稿，不替代本轮独立验收。

新增具名外部保留为[Distilling Token-Trained Models into Byte-Level Models v1](https://arxiv.org/abs/2602.01007v1)：完整题摘新增token→byte逐步表征蒸馏与byte-SFT转换路径，不能以AI主题或125B数字决定准入。官方仅Submitted Feb1，不是公开日期；当前v2 Oct5未审未用。作者[初始仓库README](../_sources/daily-20260202/supplement-byte-initial-readme-20261008.md)只有Coming Soon，三commit有限记录的Initial Release Code为Feb11，不能恢复Feb1全文公开。已有限核官方v1/作者仓库与首版文本；需要可核Feb1全文公开日期及对应原稿身份（作者dated announcement或官方公告），不求小时。当前不列当窗候选、不评分、不进Books、不作正面证据；得到材料只重开此家族真实归属日。

本补充窗口的Google/Meta/Qwen/Hunyuan/MiMo/MiniMax AgentTech历史切片及Seed type2有限返回差额，逐源实际停止见§2补充说明。有限native/metadata/日期主题恢复均已执行；接受本窗官方索引/RSS、保存的原目录或具名dated作者材料，不要求遍历全站。它们是历史材料保留项，不是尚未读完的候选，不能支持零发布、无遗漏或正面Coverage。Kimi PARL仅有日期未知线索/历史切片，未证实Feb1有新事件；若提供原始公开或实质修订日期与对应版本，只核真实归属窗口，不要求它恰为Feb1。

原§5的SPARKLING/GLM-OCR描述冻结保留；本轮官方日期分别为Feb2、API为Feb3，因此不纳入新增Feb1窗口，也不重评分或迁动原候选。Qwen3-Coder-Next官方索引Feb2、MiMo HySparse Feb3及ByteDistill后续代码Feb11仅用于定点边界，不启动别的Daily。

### 原稿终态保留（冻结，原窗口）

本窗可执行工作：0。root对完整本日报六部分的日级验收、Ch66实际两段/末注及相邻衔接的非作者写后复核均已通过。没有未读候选或待扩张扫描；下面均是精确外部终态保留项，不支持本窗正面Evidence、Books采用或无遗漏声明。

1. **SPARKLING**：[Seed论文目录](https://seed.bytedance.com/en/public_papers)、[arXiv exact-v1 2602.02472](https://arxiv.org/abs/2602.02472v1)。本轮完整题摘的潜在增量是mid-stage width扩展中naive初始化破坏activation统计、copy初始化保留gradient symmetry，以及RMS-scale consistency与非对称optimizer reset/LR re-warmup，可能修正TRAIN-PRETRAINING扩宽的稳定性边界。Seed PublishDate显示2026-02-02，仅为日期精度（午夜值是展示字段，不伪作实际首公开时刻）；本窗只覆盖该日00～09，不能确认落窗。arXiv v1 Submitted原值Mon, 2 Feb 2026 18:52:52 UTC＝Feb3 02:52:52北京已窗外，且提交不等公开；当前June29 v2扩大dense/MoE与方法表述，未用于初版准入或Books。当前可用Seed目录和exact-v1均已定点核，重开需作者原始首公开时间/可完全落窗的范围，或可核公告+对应原稿身份；拿到后只恢复该家族真实归属日，不用v2或当前排名替代。
2. **GLM-OCR**：[Research](https://www.zhipuai.cn/zh/research)、[官方发布说明](https://docs.z.ai/release-notes/new-released)、[当前官方仓库](https://github.com/zai-org/GLM-OCR)。核心的CogViT/connector token-downsampling/GLM decoder、MTP与full-task RL、布局与并行识别可能涉及表示/训练/文档执行边界，尚未因实验细节不足而关闭。Research仅标Feb2；release notes标Feb3的API事件，可能是不同事件，不能混为首次model公开；当前仓库又含Feb12与March12更新，March技术报告不支持Feb2初版身份。缺少具体首版公开时刻及对应机制版本，不能采用当前0.9B/94.62排行榜为本窗证据。重开只需原始release/card或作者dated announcement明确时区、精确版本与事件，不要求遍历全站；若确定Feb3 API事件则归相应新窗而不扩本窗。
3. **Kimi K2.5/PARL**：[当前官方技术Blog](https://www.kimi.ai/blog/kimi-k2-5)。已读orchestrator训练/frozen subagents、奖励λ退火以约束serial collapse/fake parallelism、critical-step定义的核心说明；如果有本窗新事件，这是可能改变Agent并行控制训练的具体机制，不能因为日期未知给零分。原页无日期，只说Today，当前Platform Blog/org也不建立本窗首次公开或重要修订的身份；未采用benchmark数字或声称已深入整合。重开需官方可核首次/重要修订公开时间与版本，若日期窗外只路由其真实归属日。
4. **Google Research / Meta / Qwen / Hunyuan / MiMo / MiniMax AgentTech历史切片**：具体入口和实际停止分别在§2。Google pubs当前年份界面、Meta relevance page3、新Qwen动态空正文、Hunyuan当前九条、MiMo十五张无日期Blog及MiniMax当前May13单条均不能恢复目标历史完整事件目录。当前定点入口、可用metadata/相邻页或限定日期辅助查询已检查；隔离这些切片而非声称机构当天零研究。可接受替代是各官方源保存的本窗事件索引/RSS、具名原稿的作者首次/修订说明或能够直接核对应事件的版本记录。恢复时只重开受影响机构与该窗口，不扩全年库存、旧screening或每周源。Seed type2的9/total23差额也只作有限返回限制，不以接口声明数当已读分母。

窗外线索不属于本窗待审：SPARKLING arXiv v1的提交已经Feb3，GLM-OCR API event为Feb3、技术报告为March；Google Deep Think Feb11、MiMo HySparse Feb3与MiniMax后续事件只用于边界定位。它们不阻塞本窗终态，也没有在本报告重评分或创建其他Daily。

## 6. 复核

### 原稿有效复核（冻结，不代替补查DAY）

复核者：root（非日报/本项Books写入作者）

结论：通过

root实际核对14来源本日查询、有限停止与历史局限；重开官方Codex app L50/67/212～219及RSS原值，核当前March4更新与采用版本边界。写前核Ch66长任务945～1000和关键词侧查，批准两段unique owner；写后实际重读Ch66 982～1010两段及AgentLongBench/Pass^k邻接、完整限定diff的两个hunks与末注，并核Ch65结尾→66→67开篇的evaluation/measurement交接，非作者Books写后通过。日级又逐项核SPARKLING v1完整摘要/提交字段、GLM-OCR当前核心与release不同事件、Kimi PARL核心/日期缺口，确认终态隔离不支持正面采用；没有把年度/月目录变成逐项队列。

代表性负侧抽检为Codex同页worktree/skills/automation/sandbox核心四组说明，已实际读；排除理由是未改变具体机制或contract，不以缺少受控实验自动拒绝。三项具名潜在的题摘/核心与日期身份全部独立核；其余窗外边界按14源实际目录/查询检查，不声称机构历年材料、所有Github提交或4363篇arXiv全量复核。机器校验仅辅助，语义验收来自以上实际非作者范围。

机器校验：`python3 scripts/validate_research.py --report papers/2026/02/02/README.md`；限定报告/本轮sources/Ch66的 `git diff --check` 已通过。机器只检查结构和可判定一致性，不替代非作者语义验收。
### 2026-10-08 补充复核

复核者：root（非补查报告作者）

结论：通过

root实际读Cyber Special Feb1页面的Actor/Behavior/Operational Planning/Impact必要核心，并抽核Fish Food、Romance反侧，批准共同家族和6分受限部署证据；没有要求重复原Codex有效审阅或整份PDF。新增仅报告，不产生需POST的新书稿。日级实际重读六部分全部补充diff和全部14源停止说明，并核原始RSS1255中目标8项、Seed20/82跨Feb1边界、cs.CL首25有限题名及ByteDistill完整题摘/版本日期；其余同家族上下文按首包分层抽核范围复用，不称全部附件独核。原1候选行、原窗口、连续原§4实值保留及33本地引用0缺失已独立核，旧Codex有效Source/Books结果复用。终态日期/历史切片隔离不授零发布或无遗漏，root实际DAY通过后才同步完成态。

完成态V3结构/一致性校验、本日限定unstaged/cached diff检查均通过。第一次校验发现第二来源表重复ID及新增§4标题未逐字匹配候选，已改为原14行表＋自包含补充逐源说明并统一新增标题，重新校验通过；没有修改公共校验器。完成态原窗口、原1候选行与连续原§4逐字比对通过，33本地引用0缺失。本轮未stage/commit/push，结束本日，不接别日。
