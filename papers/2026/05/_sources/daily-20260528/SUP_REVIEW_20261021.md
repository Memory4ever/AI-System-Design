# 2026-05-28 遗漏补查：独立复核

复核者：`/root/supp_may28_reader`；报告作者：`/root/supp_may28_author`。

## R1 — 启动、范围与复用边界

- 本日独立上下文已实际重读当前 `AGENTS.md`、`docs/RESEARCH_CONTRACT.md`、`docs/REPORT_CONTRACTS.md`、`docs/RESEARCH_SOURCES.md` 用法与每日十四源及 arXiv 主题范围、`CODEX_RESEARCH_PROMPT.md`、完整 `ROADMAP.md`、`LEARNING_STATE` 最新 2026 路由（291–298 行）。仅补 `2026-05-27` 北京时间自然日，不继承前日材料池；不读每周来源组为本次扫描任务。
- 当前旧报告为 118 候选、原小时窗口 `2026-05-27T09:00:00+08:00 ～ 2026-05-28T09:00:00+08:00`。保护原候选完整行、日期和评分、小时窗以及连续旧 §4；有效旧证据仅作去重与复用，不凭旧完成标签推定本轮来源或新增证据通过。
- 初始已发现的具体恢复点：旧机构缺口中以 09:00 时分不可分为由的判断，不自动等价于本次自然日缺口；MiniMax `Agent Team` 的旧记录 `2026-05-27T08:00:00+08:00` 是本次定点线索，须核对当前原始身份、实际增量及有效重复关系。
- 首批校准要求已直接交作者：全部拟入选与按来源、主题、理由分层的代表排除项；同时实际检查入口/主题/停止位置。宽列表只作查漏线索，不成为逐条关闭或全文队列；贡献准入不能只凭 AI 相关、章节映射、机构权威或一般系统术语。
- 本 reader 仅写本文件，不写报告、Books、LEARNING_STATE、索引或脚本，不 stage/commit/push。现有及并发 staged/unstaged/untracked 变更保留。
- 状态：独立准入、必要证据、具体 Books、真实 POST、完整六部分 DAY 与保存完成态 FINAL 尚待实际交接；未授本日通过。

## R2 — MiniMax 具名线索的必要原文与具体 owner 预核

实际打开并完整读取 [MiniMax Agent Team 官方正文](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953)，页面明确 `2026-05-27`；此次日期只取官方日级日期，不使用旧稿补造的时刻。§3 明确 Team Engine 状态机、验证失败重启生产者及运行中追加消息；§4 明确交接／共享／聚合成本、验证和重试成本；§6 仍将开源描述为未来计划。正文没有给出可比实验、固定模型／负载、端到端预算或生产可靠性证明，故只可采用发布者披露的受限设计，不采“团队必然更可靠／高 ROI”及未公开实现。

已实际读 Ch82「什么时候分解有意义」「典型拓扑」的 Supervisor/Worker、verifier、typed handoff、当前运行纠偏与未来能力 promotion 分责；Ch81 开头／State Machine；Ch84 开头／请求与任务终态／Context 与持久 run 分离。上述正文确实承载角色与状态／验收分责，不是仅凭章节名判已有覆盖。作者尚未交本项正式准入句／评分／处置，本节只复用必要 Source 与具体 owner 预核；是否保留为发布增量、仅报告或已有覆盖仍待与作者校准，不预授候选与日级通过。

## R3 — 首批机构准入／必要 Source／具体 NC 校准

1. **MiniMax Agent Team：通过。** 作者正式限定「模型自判结束 → producing/verifying/done、失败唤醒、运行中 steering → 交付门不等 Worker 自报」，`2+2+2=6` 标准完成／已有覆盖。复用 R2 已实际读的完整原文与具体 Ch81/82/84 段；唯一主 owner 用 `AGENT-WORKFLOW` Ch81 State Machine，Ch82 拓扑与 Ch84 平台是交接，不重复计家族。角色组合不是单独准入依据，不授任何实测可靠性、ROI、开源实现或生产验收。
2. **[Google Private analytics via zero-trust aggregation](https://research.google/blog/private-analytics-via-zero-trust-aggregation/)：通过，修正拟 Only 为具体已有覆盖。** 官方 May27 正文全部核心实际读完；多轮在线／单依赖 TEE → 单次贡献者提交、委员会辅助聚合与 attestation 分责 → 改变隐私遥测数据面信任，是具体项目增量，不是领域应用指标。`2+2+2=6`；涉及安全边界，实际深入核必要核心反侧，不照录无条件保证。已读 Ch67「隐私约束会改变可观测性的数据平面」205–227，正文明确 raw-state owner、secure/attested aggregation、调试和低频 slice 代价及同一 Google 案例，来源区635–636也直接引用本篇；故 `PLATFORM-MONITORING` 已有覆盖，无需新写。
   - 采用只限发布披露的信任／数据面设计；TEE侧信道、密码学假设、委员会参与与查询/噪声约束仍必要。单次贡献者消息不等完整协议只有一条消息；未披露 DP 数值、模型／负载、性能或完整部署效果，不授不泄漏、安全证明或量化成本保证。
   - 具名底层论文不是 May27 新首稿：[IACR Willow 2024/936](https://eprint.iacr.org/2024/936) 官方页实际读完，received=`2024-06-11`、last revision=`2025-07-09`、CRYPTO2025。摘要明确委员会前置setup、末尾verification/decryption；此处只核身份和本博客 one-shot边界，不把旧论文扩成新候选或重读无关证明。ACM正文403不影响本次仅采用博客披露，不伪装已核密码学证明。
3. **入口纠正：有效，但来源未收口。** 已实际看首份 `SUP_arxiv_lm_20261021.html`，其206命中／首200、`submitted_date`且含后发ID。作者确认误用latest且下载截断，改为表单实际提供的 `submitted_date_first`。旧结果只作错误线索，不支撑本日覆盖；新查询与停止范围、分层EX仍待本日实际交接，未扩大为旧版本队列。

本节校准覆盖全部已交首批两拟入选；尚未收到完整分层排除样本，不声称全部来源／全部候选已复核，日级仍未通过。

## R4 — OpenAI 新拟入选及具名 EX 的实际校准

作者 A2 新交第三拟入选 **[Building self-improving tax agents with Codex](https://openai.com/index/building-self-improving-tax-agents-with-codex/)**。实际读完整核心至 `Expanding to new domains`，官方 May27；RSS日期与正文身份由作者本日原件支持。准入与 `2+2+2=6` 通过：修正不直接当错误标签，review/group 后才成为 bounded 工程任务；只读原始证据与可写产品面分开，最终发布／业务判断留人。标准要求以上已核必要反馈／发布边界；变化人口与非对照产品数字不能证明机制效果，未运行实现。

具体 Books 比较已加载 `PROJECT_CONTEXT`、`LEARNING_PHILOSOPHY`、`WRITING_GUIDE`，并实读 Ch84 Feedback 整段及前后 Release／Self-evolution。现有 promotion、global memory准入与capability preservation有效，但尚未解释“生产修正的actionability资格先于工程任务创建”这一入口。仅此最小差额可整合到 `AGENT-PLATFORM` 平台闭环之后；已通知 root 协调实际冲突窄位并请作者逐字 PRE。不授尚未写入的Books通过，也不因已有泛化promotion原则抹掉真实差额。

同源分层排除样本实际检查：

- [Warp](https://openai.com/index/warp/) 完整核心；已有context compaction／persistent memory／subagents与Oz组件的产品概述，没有新执行接口或受控边界，EX-contribution成立，不为其30% token数字扩读无关配置。
- [Cisco](https://openai.com/index/cisco/) 完整 `Building AI Defense`／`Evaluating`／`Using`／`Roadmap` 已实际成功恢复；跨repo compile-test-fix、迁移与吞吐案例未新增可改变设计选择的机制或可靠性条件，EX-contribution成立。正文不再是外部不可得，不必重复恢复。
- [Election safeguards](https://openai.com/index/election-safeguards-2026/) May原始段至 `Learning while we do our part` 及明确October20 update已读；后者不当May证据。May部分引用既有水印与防御，来源合作及public verification preview未披露新增协议／证明条件，EX-contribution成立；不把页面有更新信号误写为“无修订”。

本批是3个OpenAI贡献排除项全核，不代表其他来源或全部初筛全量验证；science明确范围排除、窗外日期样本和arXiv代表项仍随本日后批有限交接。

## R5 — Tax AI 逐字 PRE 与窄写边界

root已确认 Ch84 当前无本任务其他活跃写位，授 `平台闭环` 后局部两段加本人来源注；不碰其他binding或并发变更。已实际读作者A4逐字两段、插入前后的global-memory准入句与双时间尺度段，必要Source／owner复用R4，不重读有效层。PRE整体通过，仅限定“重复且可行动”门槛为**这种批量反馈自动转任务路径**，不误写成单次重大安全纠错不得创建工程任务的普适禁止。作者实际保存后再核完整两段／局部衔接／本人注；当前不预授POST。

## R6 — Tax AI 实际唯一 POST 通过，Ch84 窄位释放

已实际读回 Ch84 `人的修正也不能直接当作待修复的产品错误` 与 `改进任务的环境还要分开` 完整两段，连读前面平台闭环／global-memory准入和后面双时间尺度机制；已包含R5要求的批量反馈路径限定。正文在章末Review notes之前，归属唯一 `AGENT-PLATFORM`，机制、费用、失败和人审／发布边界放在同一论证链，未把观察性增长写成因果。本人末注 `SF-2026-OPENAI-TAX-AI-LOOP` 已实际读回，官方日期、必要定位、6分深入原因、无对照／人口变化及未核artifact边界与正文一致；未预支全日验收。当前限定 Ch84／本review的 cached 与 unstaged `git diff --check` 均无报错。

这是指定非writer的一次真实完整新增／局部衔接／本人注 POST，通过即生效；Ch84本项窄位释放，不要求root第三读。来源扫描、剩余有限题摘及本日六部分DAY／完成态FINAL仍属普通工作。

## R7 — 本日入口与机构日期切片的实际有限检查

- 新 arXiv bounded 原件实际字段为 `submitted_date_first` May25–26：language model 211（第一页1–200与第二页201–211），transformer113、world model84、GPU24、agent110、diffusion75；各页显示范围与总数已实看，分类月表原件确为404。上述是主题线索，不是当日候选计数，不把跨词去重线索集变全文队列。已提醒作者对VLM/VLA/MoE/long-context/RAG/kernel/communication等同义及相关分类标题作有界补检；尚未授此层全主线覆盖。
- Hunyuan `SUP_hunyuan_api_20261021.json` 实际 `totalNum=9/list=9`，独立解析并看完九个 title／publicAt／publishedAt／displayPublishTime／renderType，未见May27字段。具名100061的display与public/published分属不同时段，因此字段不互相更名，不由当前目录证明历史全量无遗漏；无具名本日事件并不要求读九项全文。
- Qwen `SUP_qwen_20261021.raw` 实际 `data.articles` 四十项title与`extra.date`已全看，数组非日期排序；May19／20与May29相邻，没有May27项。此API切片日期检查可复用，不因正文大量存在而制造四十个全文任务。
- Seed `SUP_seed_20261021.raw` 已看到May29、两May26卡片夹住本日的有限日期切片；不授尚未核的Blog层通过。OpenAI三个具名EX已在R4全核，其余来源和arXiv分层题摘／日期仍普通待交。

## R8 — arXiv 首五拟入选完整题摘准入与两项必要 Source

实际分别打开当前官方事件页、读完整题摘和版本标识：26546 MobileExplorer、26542 ChainCaps、26521 workflow structural testing、26497 AuthGraph、26457 Verus-SpecGym。五项准入通过：分别新增并行UI取证／恢复分责、sink预算meet、workflow结构witness、clean授权图与真实provenance对齐、可执行spec的反例评估。不把局部实验／负面结果排除，不把已read摘要写为Source完成；后三项必要Source、全部具体Books／评分仍待作者本日正式交接。

### 26546 — 必要 Source、日期通过，具体 Books 尚待

[精确v1 HTML](https://arxiv.org/html/2605.26546v1) 实际读§3–7、§5公式／Algorithm1、§6主评价／消融／data-entry反侧与成本。采用仅推理窗口内有界UI取证与hint对齐；pHash相似及Home-replay不证明backend状态恢复或effect撤销，算法也未写Level2后再验，故不采无条件恢复正确性。本项目由此要求安全probe与真实effect验收，不冒作者定理。主实验是host emulator＋target模型双设备HTTP，Q8/llama.cpp／Termux；4B、116任务、59成功，主节15.5%步数／15.9%时延与摘要23%不合并，数据输入／编辑仍反退。未核实现、复现或生产SLO。

本日`SUP_datacite_26546_20261021.json`原件实际解析：同精确DOI、`client=arxiv.content`、`state=findable`、`registered=2026-05-27T02:11:50.000Z`；v1唯一提交`2026-05-26T04:53:53Z`。官方2026[公告及发号规则](https://info.arxiv.org/help/availability.html)已实际读：最早May27 00:00Z与最晚registered之间全在BJT May27，联合限定日通过，不把registered改名实际公开时刻。26112原件registered May26 03:55Z仅具名窗外参照，不批量套日期。

### 26542 — 当前 v4 必要 Source 通过，日期／具体 Books 尚待

当前官方页明确v4 Jul1（v1 May26，v2Jun29/v3Jun30）；实际读[精确v4 HTML](https://arxiv.org/html/2605.26542v4)§3–5全部必要机制、T1–3、scope与反侧。不无差别重读无关旧版。采用sink-specific预算取交与context保守传播，定理只在可信manifest／完整proxy可见flow下；shell／hidden state／covert／恶意tool可越界。Live与replay分开，后者只是Fides/PFI抽象而非完整竞品；gold→naive明显退步，有限stress／14攻击不授生态安全。HMAC token单次降密放行不是生产身份治理已证；公开artifact未执行。当前v4是采用版本，不把Jul1修订伪装May27新事件，必要首公开日期须另合证。

## R9 — A5 全三十题摘校准及受影响集合

已从本日官方bounded HTML完整paragraph读取其余25题摘（含nested高亮后的全文），与R8首五合为作者A5三十项全部实际校准，不以全文缓存或读完摘要代替必要Source／日期。

- 保留明确潜力：26539负面归因、26357渐进漂移下SF多时间尺度稳定性不因负面／小模型排除；其余A5原IN除下列未决项，其具体新机制／边界可以进入相应必要审阅。26539的20次LLM proposal均未promotion与N5不显著支持的是“不把controller归LLM”，不是效果已证；其精确日期尚未通过。
- 26418实际定点读[精确v1](https://arxiv.org/html/2605.26418v1)§1–3.4：纯CPU/Mem/QPS等六维state、replica HPA模拟，edge-inference仅泛化一句，无实际大模型workload／KV／模型state切片；修正为EX范围，不能用RL算法加resource名词反推准入。
- LexGuard26530、JobBench26329、delay compensation26286、coalition26278的具体EX理由成立；不是按机构、敏感主题或非LLM标签统一排除。
- 26397局部重开：当前v2题摘有生成faithfulness与judge盲区信号，不能沿领域应用理由直接EX；但v1官方HTML实际为`Annotator Positionality as Signal: Psychometric Weighting...`，v2 June1已改题与研究方向。当前v2必要§3–5已实际读并保sampling、noncompliance排除、所选52争议人审、同偏analyzer、xlsx prompt混杂和不显著不等equivalence等限制；本日是否准入仍只按精确v1必要题摘／方法判定，不把六月rewrite增量倒灌五月，当前仅保修订信号。
- 26437已定点恢复[精确v1 PDF](https://arxiv.org/pdf/2605.26437v1)§3–4(pp5–8)：human-baseline残差重命名及“next-token只retrieval所以无δ”不由目标函数推出，语料也可含非baseline行为；四项提出的tests未实测。EX-contribution，不因econ分类或单纯没实验排；引用异构人类比较不能识别该推断路线。准入问题已闭，不为此EX另索日期或无关全文。

## R10 — A6 六十五加六同义题摘：准入而非 Source 队列

全部71项完整题摘已实际读；一批输出截断的26242／26241／26236／26232已重新取完整paragraph，未用短span替代全文。只校准新可复用机制、设计条件或纠错证据，不按候选数或保留率。初始七同义入口只扩有界线索，不将所有相关题摘自动送Source。

**具体改判：**

- 26256 POLAR：semantic／episodic KG＋retrieve的常见组合与个性化收益，未给新更新／冲突机制或已发现盲区，EX贡献。
- 26239 Sentinel：foundation高层沟通＋classical planner／replan的已有分责与meeting任务收益，未给新增控制接口／成立条件，EX贡献。
- 26353 DecoupleGen：personalized T2I rare-context augmentation＋verification，distribution preservation是目标，未给新可复用机制／条件，EX贡献。
- 26498 Verilog-Evolve：simulation／synthesis／timingproxy多目标promotion及日志skill／verifier组合，未给新promotion语义或改变设计的条件；不能拿“proxy不是芯片”的通用提醒充原文贡献，EX贡献。
- 26399 OmniGF：VLM的文本／连续head与headcrop特征移植gaze、多人物共享处理，未给foundation表示／执行边界新证据，EX贡献。

**只定点补决定准入事实，不预建全文任务：** 26195 CyberEvolver需实际mutation／selection或归因域，四层＋diagnosis＋beam本身不够；26520 InterSketch需stepwise reward／reflection具体增量与对照；26400 search summaries目前仅framework和实施计划；26486 LongCat1.5需distill机制／matched cost-quality而非encoder／data／RLHF或“optimal8NFE”宣传；26476 FAB需受控context诊断的新混杂证据而非行业QA和六指标；26200自动研究不等科学应用，不能用AIforScience硬排，若仅命名三种collapse重述proxy／independent validation则EX贡献，需只看21audit是否新增具体证据。

其他拟IN的明确机制准入支持保留：26269／26252／26203／26186／26178／26177／26174／26538／26491／26470／26460／26449／26332／26282；26266／26230／26478／26461／26384／26537／26526／26501／26489／26485／26484／26454／26433／26431／26415／26414；26380／26366／26365／26362／26356／26339／26322／26315／26293／26248／26246／26242／26232／26184／26176／26175／26355／26379；26519／26371／26525／26496。均只授各自最小明确贡献潜力，待日期、当前精确版本、必要Source／反侧与具体Books；不是全队列已确认候选，更不是深入完成。

其余代表EX成立：26535科学、26391garment、26441传统VTG、26421synthetic-image detector、26279约束acquisition、26241motion catalog、26236gesture组合、26368panorama移植；范围／贡献理由分开，不否定其学术价值。下一步只恢复上述含糊项的决定事实及已准入材料的必要域。

## R11 — 具名更早正文纠正与 Sandlock 必要层

压缩恢复后实际重读本日适用AGENTS／研究与Report合同／统一Prompt、每日十四源与主题边界、ROADMAP及LS最新2026路由；Books背景／学习理念／写作指南已实际复读。未接他日材料池，宽入口522身份与101题摘均不等本日候选。

### 三项更早公开：只撤回日期通过层，不抹去已读证据

- **26500**：官方[CVF ICCV2025同题页面](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html)检索原文与会议PDF首面已实际核：同三作者、同摘要／机制，proceedings October2025、9252–9262页。EX-date；不是May27首次公开，不因arXiv登记晚而重计。已读Gaussian map／semantic grouping／multi-level policy证据保背景，不新写Books。
- **26503**：官方[ICLR proceedings同题正文](https://proceedings.iclr.cc/paper_files/paper/2026/file/cd830afc6208a346e4ec5caf1b08b4b4-Paper-Conference.pdf)首面与摘要、九作者及[会议poster](https://iclr.cc/virtual/2026/poster/10010039)实际读取；poster明确Apr25 2026，三uncertainty／SGM／ValueMap核心同族。OpenReview精确forum LPv59noPAy及API403，但已足以排除May27首次公开，不用可疑profile日期或搜索抓取时刻臆造earliest。EX-date；此前实际读v1§3–4方法、实验／消融及反侧有效，不继续无关附录或完整发表史。
- **26508**：作者发现精确abs Comments中的SSRN6761960早稿，撤回先前仅arXiv合证的全球首公开推定。reader实际从[SSRN官方同题页面检索原文](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6761960)恢复完整摘要、Posted20May2026／WrittenMay14，safe-default、no-splitting、authority premium及adaptive envelope四核心均在早稿披露。EX-date，未识别本窗重要修订，不新候选／评分／Books。已实际读v1§3–9的固定五原语、同boundary telescoping、严格单调／tail条件、同时自适应上界与正收费累计账本证据保留；Theorem8的一般Lp bounded推广不由其p-infinity证明支持，绝不采用。原Ch84累计effect预算具体缺口判断仅作背景，root协调窄位已通知释放，不执行写入。

### 26298 Sandlock：必要 Source／日期／具体差额通过，POST待保存

实际读精确v1§3–5全必要机制、§6全部设置／表3／微基准／代价及§8全部限制。静态可判规则编译kernel，syscall-time事实才由notification supervisor决定；child ready握手先于exec。connect等复制并on-behalf，不Continue让kernel重读指针；exec argv另需freeze可能alias的任务，失败deny，不可把两路径混写。ABI6最低、HTTPS语义ACL opt-in CA、argv名字只是观察信号；cooperative memory／CPU不是cgroup强隔离；COW仅filesystem，network effect不能撤回，跨stage pipe内容仍可污染。十个微检查不等安全证明；Ryzen5500U／8GB／Linux6.18、20次startup与五次Redis7测量、静态路径近裸机不覆盖on-behalf echo的20→55μs／p99 33→114μs成本。未核artifact／复现／生产保证。

实际核v1提交May25 19:51:30Z与本日bulk原件精确DOI的arxiv.content／findable／registeredMay27 02:05:57Z，联合区间全部BJTMay27；不是把registered改名公告时刻。Ch72现「不可信代码需要OS级Effect Boundary」family26298整段及前后衔接实际读：已有OS commit gate／profile／fallback，缺static与dynamic最早sound判点、TOCTOU责任及filesystem/network效果分责。root已协调该现段后最小一段＋本人note，已授权作者写受限机制，不改其他binding。评分6因实际安全边界差额深入，实际POST尚待，未预授整合完成。

### 第四机构候选 Kimi Code CLI v0.4.0

实际读取[官方May27变更三项及v0.1迁移声明](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html#v0-4-0-may-27-2026)：cwd外read-only不再弹approval是审批触发条件变化，不证明权限隔离／保密／不外传；Skills+MCP插件bundle和session export只作发布上下文。1+2+2=5、安全变更必要域深入／仅报告通过；新TypeScript CLI不是旧Python kimi-cli1.x，不能把当前配置或后续hardening倒灌May实现。不制造新安全机制，也不为此改Books。

## R12 — 必要 Source、具体 Books 与四项真实 POST

### 26397：精确历史 v1 五分，仅报告

精确v1§3–4、§6及C/C1实际读。2120标签／1997有效κ，8×7主要条件，12模型并非全条件；九人pool中3名autistic、单次AQ/SATA/IAT。加权比majority的κ均值移−0.012但排名r≥.94；SATA-only方向反而正、AQ-only不显著，不把Composite称客观更正确truth。92条质性分析每condition约1–2例，不作全语料频率；masking同时改措辞、顺序和filler，不识别单一原因。1+2+2=5准入仅保“参考构造会改变绝对分而不必改排名”的受限评价证据。当前v2是June1不同研究方向，只作必要修订信号，不倒灌五月。实际比Ch66开头条件性分数／逐轮标签来源及cluster限制、reference独立资格段；本地norm和小pool未改变长期规则，不写加权配方，最终仅报告，不冒具体NC为新实证全覆盖。

### 26457：必要 Source／日期／具体差额与实际 POST通过

实际读[精确v1](https://arxiv.org/html/2605.26457v1)§2–4及C1/C3：spec意图关系不由proof自动成立，四pre/post sound/complete buckets、official tests与human hacks构反例、symbolic unknown后exec_spec_unverified运行具体例。宏未产生翻译等价证明，支持类型／有界量词有限，panic／timeout另类；不能把finite tests升成RsF=RsI。581题，六model、每题$2.5／75分钟，开源另max400steps；same gpt5.3codex对自己可编译错误spec的49/191漏判25.7%非所有judge规律，153/187是已筛spec失败/唯一输出子集，非整榜能力。未核artifact／复现。v1May26 02:12:48Z与本日bulk arxiv.content/findable/registeredMay27 02:09:41Z合界全BJT27，当前事件页Preprint无具体早稿信号。

已实际比Ch66原NL2VC2604-22601整段及后delivered_success：原段有spec／intent分责，缺四bucket与unknown runtime接口。6分因具体长期差额深入；root授原段后最小一段＋本人note，作者保存后reader已一次真实读完整新增、原完整段／后完整交接及本人note，限定cached／unstaged diff-check均通过。采用边界准确，POST通过，窄位已释放；未预授DAY。

### 26542：v1必要对读、具体差额及实际 POST通过

R8当前v4必要域有效；本轮针对May27历史贡献实际读v1§3–5。预算集合／meet／Bctx／Req与可信manifest、完整proxy可见前提已在v1；82任务、163 replay、gold→naive退化与shell残留也已存在，不需全版本diff。v1 artifact仅承诺upon acceptance，当前公开链接不倒灌当时已实现核验。2+3+2=7，v1提交May26 04:44:59Z及本日bulk registeredMay27 02:11:44Z、arxiv.content/findable合界同BJT27。实际读Ch72现family两段及前后MosaicLeaks／后RAG交接：旧文单调authority概念，具体差额是sink(operation,scope)预算交集和保守context传播／false block、显式流与manifest资格。root授该两段后最小一段＋本人note；作者保存后reader实际完整新增、完整直接两侧与本人notePOST通过，限定两层diff-check通过，窄位立即释放。未授无条件安全、实现或复现。

### 26497：必要 Source、诊断权限及实际 POST通过

实际读[AuthGraph精确v1](https://arxiv.org/html/2605.26497v1)§3–5与T3–6（含嵌套T5第二panel消融）。clean user+catalog基线与可污染IRG分开，INVOKE结构用于序列，DERIVE/EXTRACT不认证归因；source_tools原始observation查值优先，string存在不等真实因果、fallback LLM仍sensor。replan读外部observation打开trust boundary；同权威源污染、错误归因／误拒、跨agent及纯文本不覆盖，未证明原子pre-effect gate。AgentDojo97任务629scenario、AgentDyn任务数未披露，T0、builder4o/planner4o-mini/checker4o额外调用；四被测模型不等四独立防御器。T6总9.93s/47.4K对baseline5.32s/11.2K，不把component token倍率的不同分母混合，也不从有限ASR外推生态安全。artifact未来开源，未核代码／复现。2+3+2=7；May26 03:20:23Z＋registeredMay27 02:10:41Z及arxiv.content/findable合界BJT27。

实际读Ch72现2504-20984工具绑定段与前CUA／后AgentGuardian完整交接，缺授权基线和原观察诊断分责。root授指定段后最小一段＋本人note；作者保存后reader一次真实完整新增／两侧／本人notePOST通过，限定两层diff-check通过，窄位立即释放。只整合诊断设计及其边界，不授精确provenance或充分安全。

### 26298既成 POST

R11必要层有效；作者保存指定单段后，reader实际读完整新增、原family段、后Windows完整论证与本人note，限定两层diff-check通过。网络on-behalf与exec freeze路径、COW/network及cooperative资源分责准确，唯一非writer实际POST通过、指定Ch72窄位已释放。未日级通过。

### 26521与五个日期资格停点

26521精确v1§II–IV/VI实际读，403义务及mock stubs、N5、gpt4.1mini共realizer/被测、single run、39216s/3637 realizer roundtrips；摘要54/75及36/48与正文45/65及31/41矛盾，不用正向分母。23/248是elicited restricted-call attempt，不等真实effect或正向安全覆盖；no call不证边界被exercise，明确拒绝与违例极性不同，fault WF1可接受貌似但语义可疑回复。实际比Ch81现family26521两段与EvaluationRun交接，有上述必要解释差额；6分深入、root已授两段后一段＋本人note，作者保存／实际POST尚待。v1May26 04:07:55Z与本日bulk registeredMay27 02:11:15Z、arxiv.content/findable合界BJT27。

26203恰May25 17:59:59Z、26186/26178/26177/26174更早，registered上界May27不能消除跨BJT26–27区间。已实际核五项abs原字段及bulk身份；官方2026holiday表无May25，不能凭MemorialDay常识抬早界。有限恢复official monthly cs.SE652／cs.MA433只具名查五ID，完整月页无日组，日期路径400，不能作日证；未扩月材料池。26174具体Comments链接的官方Zenodo概念20372696解析为record20372697、publication_dateMay25，是同题data/code而非已证论文正文，不冒全球首稿判断。五项日期仍隔离待有限恢复，不先深审，不写入确定候选。26269／26252则v1May25 18Z后合界有效，必要Source仍普通待办。

## R13 — 六项有限准入恢复、26521既成 POST、两项必要 Source

### 六项只补决定准入事实，未改成全篇审阅队列

- 26486：实际§3.4/5.4，单shared DiT分别挂Generator/FakeScore LoRA、base作real-score，改变三份同构权重同时驻留的实现选择；8NFE对base150NFE，human-likeness/lipsync/diversity损失与stability改善并存。IN5，不冒DMD2新发明、速度全费或无损。
- 26520：实际§3.3/4.3及AppC，GT可计算trajectory metric与GT-conditioned VLM两种step-score接口；反思SFT mask错误段，step监督与终答reward分责可准入IN5。Eq7用logprob时负数可使改善得负、零分母未闭，不能转写可执行配方／高效归因；必要Source其余评价仍由作者续作，不以此有限片段预授完成。
- 26400：实际§3–4完整定义与Plans。top-heavy read-prefix XUX与多summary section-pool/JSD测遗漏／均衡是明确新评价对象，IN5仅报告提案；uniform abandon／line unit、自己section默认perfect、重复与切分影响pool均限制量纲。实证／用户行为／human agreement均未来，不授有效性或真实性。
- 26476：实际§4.1/5.3–4/8.3，200行业QA、窗口配置同时变output cap，max4snippets而实际context量未报；attention filtering／parametric compensation／critical-mass只是由曲线猜机制，未给新的可用设计条件。EX贡献成立，不因实验不可信而缩已准入池，是必要core仍无超出通用context非单调的具体增量。
- 26200：实际§4–5及B2/B4，21流程的强弱标签由scalar/internal/standing external pathway规则编码，未新测失败或识别新混杂；三collapse是既有proxy／独立review／反馈原则的重分类。EX贡献成立，撤回AIforScience硬排理由，不扩科学应用附件。
- 26195：实际§2完整决定域，verbatim动作保留／placeholder最多三raw-observation回填、relative sibling-onlyscore与逐层validate/revert已超generic beam＋四层命名，IN5潜力。明确贡献不因后续日期hold而抹除，但资格先行，不预授本日候选／证据完成。

### 26521真实 POST

作者实际保存root授的原family两段后／EvaluationRun前单段＋本人note后，reader已一次实际完整新增、原两段、后EvaluationRun与compile-loop交接、本人note，限定两层diff-check通过。无call／拒绝／attempted violation／mock与effect分责准确，POST通过且指定Ch81窄位释放，不预授DAY。

### 26252 GEM：必要 Source／具体差额通过，POST待保存

实际§2–4全部必要原文与算法。state=(content,typed structure,policies)、四operator、六correctness条件；topic field history与extension/association边不同，policy在Kuzu proposed state commit检查，retrieval增加salience，maintenance异步。只采有限接口设计，不采“任一CRUD上层不可能”的结构断言，也不把阈值衰减当已证全局β硬界；原型恰以Kuzu事务组织，上述semantic host／依赖由LLM选择不获真值。无量化性能或生产一致性证明，未核code／复现。

实际读Ch77 WorldDB2604-18478事务段、前typed-memory写入与后content-credit交接。已有写事务／历史／typed依赖，缺read本身提交salience的受理边界；6分为实际长期差额深入。root授WorldDB段后一段＋本人note，已向作者给受限逐字稿，retry/replay身份要求明确属本项目推导。尚未POST，不预授整合完成。v1May25 18:22:42Z、bulk registeredMay27 02:04:53Z与arxiv.content/findable合界BJT27有效。

### 26269 AgentSecBench：必要 Source通过，六分仅报告

实际§2–10、T1–6及§3全部定义／Lemma1／Theorem1。三个games的annotation、pre-generation指定coordinate closure与proposed-output risk分开；target elision需要non-invention δ，executed-risk乘r还需validator在proposed violations条件下FNR界，不可无条件乘独立概率。精确marker零事件不等MI零或全部语义安全，tool只输出proposal、未运行真实executor；clean tenant labels／capability names不覆盖混合记录／多轮／obfuscation。三games×8case×pairedcontrol×6defense×2Qwen3(0.6/1.7B)=576，greedy/maxnew64，utility为lexical proxy。原SE公式缺sqrt不采用统计配方，有限模型差异不外推规模。6分标准仅报告：它是成熟annotation/enforcement原则的有限新测量实例，不授新生产实现或普适安全界，不为diff增加泛化段。v1May25 18:53:22Z、bulk registeredMay27 02:05:17Z与arxiv.content/findable合界BJT27有效。

## R14 — 必要 Source 续审与三项实际 POST

### 26252 GEM 既成 POST

作者保存后已实际完整读新增段、WorldDB 原整段、后 Content Credit 两段与本人 note；限定两层 diff-check 通过。read 引起 salience 的提交、返回证据与重放身份分责准确，项目推导与原型边界不混。POST 通过，root 接纳、窄位释放；R13 的待保存状态被本项覆盖。

### 26538 Scheduled Style：标准完成、五分仅报告

实际 v1 §3–7／T1–3及日期原件。StyleID、六层／50 steps、SD1.4 DDIM50、3090、20 COCO×40 WikiArt 共800对512²；三 fixed γ 只是有限前沿，其他方法有借用结果，不等统一重跑。作者主推 sqrt+CN 的 FID16.285／LPIPS.564 对 fixed .5 的16.572／.561并非严格双优；但 cos+CN16.342／.560确实支配该离散点，不能反向否定全部局部 Pareto 扩展。sqrt 初始下降更快，不采“更温和”因果解释；CN部分恢复也不证明数学正交／免联合搜索。实际读 Ch24 379–381 的选择／注入尺度／量与非语义解耦论点，有限 StyleID SD1.x新实证保报告，不另建稳定链。v1 May26 04:39:40Z、registered May27 02:11:38Z及 arxiv.content/findable 合界BJT27。未核图像／实现／复现。

### 26491 LAIR：必要 v1／当前 v2 与真实 POST

实际读 v1 §4–5、A1–2／C／E全部必要域及 current v2 Sep4的§4／5.3／C2受影响部分。p=softmax(r/τ)、w=p−1/N零和，J=−Σw s+(λ/N)Σs²的自由坐标最优 Nw/(2λ)不等共享网络可独立实现；有限列表目标不自带真实分布 KL 硬界，还需全支持有界延拓与 log-ratio近似。SD1.5／SDXL、PickScore训练与PickV2等代理评价非独立人类；MaPO审美有优势，GenEval baseline借用，A100训练与H100速度不作公平五倍归因。v2新增 rank/top1/noise对照只标后续，不倒灌五月；N／τ有限消融非普遍最优。6分因具体 loss 接口差额深入；已实际比 Ch34 consistency-surrogate 原完整段和 noise-output anchor 后段，root 授单段＋本人 note，作者实际保存后本人完整新增／完整直接前后／本人 note POST通过，两层限定diff-check通过，指定窄位释放。v1 May26 03:09:24Z＋registered May27 02:10:28Z及 arxiv.content/findable合界BJT27。

### 26546 MobileExplorer：真实 POST

R8必要 Source／日期层有效。root 授 Ch78 Aura 两段后／大 schema 段前最小一段＋本人 note，作者保存后已实际读完整新增、完整两侧（含后 schema flow/catalog identity）与本人 note，两层限定diff-check通过。probe真实副作用、观测身份、pHash／Home replay不签backend一致或撤销effect、host emulator与目标模型设备分工、全费均准确；新增动作限制与重新匹配明确是本项目执行条件，不冒原文证明。POST通过、窄位释放，不授实现／复现或DAY。

### 26289 Stateful Inference：中心争议保留

本人实际读 v1 §3.1–3.5／3.9–3.10缓存结构及§4–5必要评价／限制，独立复现作者A7的文本矛盾：baseline已启用APC／Radix，却把full prefill／no caching作为主要归因，混淆response cache与KV复用；vLLM latest且无命中／逐出对账及必要消融。L40S48GB、Llama3.1-8B BF16、32K、greedy128与6／35 novel turns只限原配置；unique输出不消除KV复用。6分不降分，中心性能归因暂缓，不用正面性能、不入Books。实际读Ch45现family两段与完整直接邻接，已有条件性delta／身份／失效边界不能消除该争议；PLD其余无关实现不继续展开。

### 26297 Agentic Workloads：具体 NC

本人实际读 current-v2 §III／V／VI必要域并与作者精确v1有效层对照。2 H100 NVL／TP2、Xeon8592、vLLM.20、ClaudeCode／Harbor、五bench及100样本DAB/SWEPro、precision ND；84.6–99.5%缓存输入及decode91–98.6%仅resident/no-eviction设置，raw-input/output与append/output不同分母，tool等待与失败归因分开。v2 Sep21新增context thrashing的hit98→16–26%及throughput降至66%只作后续，不能写入May证据。实际读Ch66当前family整段及前后：cache身份／lifetime、tool pause、decode主导与eviction时重测的条件已有完整承载，6分深入已有覆盖，不为新bench领域改书。

### 26321 Anchor：必要 Source 与具体 NC

实际 v1 §2–5／AppE。同一solved spec经四deterministic projections生成instruction／setup／oracle／verifier；人工formalization／renderer仍可能错。Odoo19、300任务／29patterns／10experts40h；18000是计划runs、并非全完成。constraint25／gate-optimal60／trace15、no-op硬零、权威vendor价格重算不等业务语义全真；no-op／oracle／expert／optimal canary是独立检查而非普遍证明。实际读Ch66 ERP-Bench完整段和GUI resolved-spec/setup/prompt/expected两段，已有形式问题／生成器／verifier共同源、独立anchor及有限oracle的具体承载，6分深入已有覆盖。v1 May25 20:44:17Z＋registered May27 02:06:30Z及arxiv.content/findable合界BJT27，accepted workshop不自动证明更早公开。

### 26403 Calibrated Interactive RL：具体争议，普通必要补读继续

实际 v1 §3–5与Limit：正文称真人校准轨迹／消除sycophancy，implementation却写PhaseI的1860／16028 trajectories由Qwen3-235B oracle合成；顶部称agent/sim均Gemma3-4B，implementation又给Qwen2.5-7B simulator。有限H、bounded reward/L1的误差上界不推出静态环境必然H²失效或不可学习。6分中心争议暂缓，不能授真人效度／已消除artifact。已实际读Ch31现family完整段与前后，原文模拟器资格与真人release gate不自动解决中心。剩余仅Table2与B中决定上述身份／sampling事实为普通可执行补读，不假装外部缺口。

## R15 — 第一批必要 Source 收束与安全修订恢复

### 26403 必要补读结束

实际T2及AppB1–6完成：两域各200、三runs；Gemma3-4B BF16 policy／Qwen2.5-7B sim，Qwen3-235B既生成校准轨迹又作eval sim/judge，不支持独立无偏真人评价。T2称CollabLLM offline-DPO而B5称Static-RL，设置身份亦冲突。8／32 A800、SLIME／SGLang、G32／H7及10／20updates仅厂商论文配置；不需要扩大质性案例。中心争议隔离6，不正面采用，不写Books；R14普通补读已完成。

### 26302 AgingBench：六分深入、具体已有覆盖

实际v1§3–6、D1–5／F4必要机制、反侧与费用。P1–P3是paired而非全factorial；single-blob无retrieval时P2 abstain、W/R合报，差分不是唯一因果。四aging机制与generator DAG均synthetic任务；typed sidecar依赖generator sentinel，runtime trigger也读generator真值eval，不冒真实部署天然可得。D5强制至少两Read改善recall／workspace fidelity却未修复pytest残余，不能把改善读取等同修复已写坏代码；表3.93与正文4.00不采用精确turn差。14模型／8–200sessions、闭agentadapter／版本固定／禁隐状态及全pipeline调用费只限论文。实际比Ch84现26302完整纵向checkpoint／repair owner段和Ch77§干预矩阵完整stored/oracle/retrieved/reader固定条件，具体机制已承载，NC，不跨owner重复增加Ch84诊断段。提交May25 19:55:12Z＋registeredMay27 02:06:03Z及arxiv.content/findable合界BJT27。

### 26448 Constitutional Arms Races：六分标准、仅报告

实际v1§3–8／E／G。GPT-OSS120B T1、OpenEvolve、pop6／30gen／K2主单轨；score与优化fitness分开，绝对S不跨环境／前作比较。K5及60gen是局部搜索对照，不签通用K阈值或方差2.5倍实测普律；syntax-error亲本未保存前检查曾毒化lineage，排除九代／计划重跑不等修好旧实验。独立分数并不一般性推出没有对手压力，PGG共享pool也不等普遍zero-sum；只采本环境diagnostic。手写20行specialist强于LLM搜索，未证明evolved Blue比cooperative种子更鲁棒。Ch82固定策略mutation／个体与群体／实际payoff合同完整段已读，有限toy fitness选择／噪声实例保报告，不新授通用对抗机制。提交May26 02:01:08Z＋registeredMay27 02:09:28Z及arxiv.content/findable合界BJT27。

### 26394 EnterpriseMem：六分深入、具体已有覆盖

实际v1§3–8／Limit／D。300templates／1400turns／5models×5conditions单次，WM2→WM5→Ep→Sem增量；structured resolved context消费benchmark keys/stateupdates，不是纯自主memory能力。fallback仅邻session一个错误profile，neither-match不穷尽污染、不证明纯reasoning；高级memory正负、thinking不同预算与任务条件并存，不签生产普遍性。Ch77§1364干预矩阵、§1372content/length匹配及后目标人口完整论证已实际读，具体已覆盖分责，不为新domain例子改书。提交May25 23:52:15Z＋registeredMay27 02:08:11Z及arxiv.content/findable合界BJT27。

### 26343 MechRL：五分标准、仅报告

实际v1§2–4完整；current v2 June28 §2–6受影响机制与反侧，后稿从single-head bottleneck换为edge-pruning，后续结果不倒灌五月。原稿GPT2-small／144单头／50picks／L40S、contrastive logit-difference减CE量纲不齐；K5更多真实probe不等算力，docstring zero-shot K1=1.467与induction-primed2.178不能混成无条件oracle泛化。single-head indispensable不等完整回路，冗余NameMover会漏。Ch15真实activation/ablation与head身份完整段已读，只保有限解释搜索实例，不授新长期配方。提交May25 21:32:57Z＋registeredMay27 02:07:00Z及arxiv.content/findable合界BJT27。

### 26352 RICE-PO：六分必要深入、待实际 POST

实际v1§3–7／A1／A3，current v3 Aug6 §4.2／A1／7受影响核心相同，不遍历v2。summary可执行的局部NDCG anchor与reasoning token信用分开；top4entropy anchors×5MC／depth5，Diver4B+BM25、ReasonIR4011/1384、BEIR4008/1447。门失败保原Ai而不是zero，未选tokens保持trajectory。共同重采reasoning/summary不是单独z因果；Prop1的代数残差条件不由五样本低variance认证，local与normalized advantage也不混。未报hardware／precision／seeds及等全rollout预算，不授无偏／普遍效率，任务反退保留。实际比Ch33segment／hindsight／milestone与Ch76compression credit完整邻接，缺executable anchor→conditional latent-credit接口；root已授2603-18683后/milestone前一段＋本人note，作者待保存，POST未授。提交May25 21:56:29Z＋registeredMay27 02:07:13Z及arxiv.content/findable合界BJT27。

### 26275 SPEAR：六分标准、仅报告

实际v1§3–7／Limit及current-v2 Aug4 §3／4.4受影响对照。code-authored聚合比raw-text局部实例有意义，不新造code-as-action或rollback；v1 Ntotal28vs2／bestofN、TextGrad4o与另5.4、valid反复选择／聚合label暴露、BBH把dev作test及format首轮修复限制机制归因。employment heldout反退；AST cooperative非对抗隔离，2–3对500eval分母不同，非500倍全费加速。v2 matched n7／bare同tools／cannedtools新证不回灌May；optimizer精确alias点仍不可复现。Ch74现138–156噪声／独立dev／预算与规则label资格完整已读，有限私有judge证据不改稳定机制。提交May25 19:01:10Z＋registeredMay27 02:05:26Z及arxiv.content/findable合界BJT27。

### 26316 E3C 与 26494 MiniMax：实际差额待保存

26316实际v1§3–5／T1–3必要完整：SLAM点云颜色/逐点VAE特征投影、ego/exo raster与完整ego joint/wrist常驻tokens分路，ego出视野条件不随raster消失；GT未来pose是输入非已预测dynamics。mostly-static、人物再入外观漂移、无显式visibility/depth；200context/80future、10FPS512²、Wan2.1-VACE1.3B／LoRA256／64H100／50epoch、50FlowMatchsteps，100snippets与不同EgoTwin协议不拼。相机rotation/FID等并非全胜。实际比Ch25VerseCrafter两段／双目条件前后完整，缺不可见ego运动条件通道；6分深入root授该处一段＋note，已给最小稿，尚未POST。提交May25 20:13:16Z＋registeredMay27 02:06:23Z及arxiv.content/findable合界BJT27。

26494实际v1§6–7及current-v2 July30 §6.2／8.3必要域。Agent/Gateway/DataPool/Train分路，white/black box真实request state，与windowed FIFO队首窗口内ready、越窗不取／头消费才推进的机制明确；没有足以认证稳定三角、无shift或吞吐的独立消融。prefix-tree精确训练还要mask/position/随机性/梯度等条件，不采用无条件zero-error/40x；W=.3不是默认定律。selfevolution百分比／内部eval不作因果，MLBench22竞赛三次24h与训练中调scaffold不同人口。实际读Ch31原cluster-orchestrator完整段及Reward Model交接，缺提交队列受限乱序选择，6分深入root授一段＋note，已给稿、待POST。提交May26 03:16:11Z＋registeredMay27 02:10:33Z及arxiv.content/findable合界BJT27。

### 26461 安全修订优先恢复，未预授 POST

收到作者具名current-v2 Oct2安全变化后，本人实际读current §4–8全部必要域、v1§5–6对读：v1将faulting execution停止推到process可safe SIGKILL不足；v2另stream可继续，RoF必须配PoR：disable channels／确认preempt pending→mapping/replay／处理追加fault→hardware preemption complete才process barrier→daemon teardown目标→仅恢复survivors。SM path另以outside-MPS standby持有VMM页／应用定义metadata和恢复边界，前提surviving GPU；device reset、已损坏state、external exactly-once不承诺。A6000／580.95.05／CUDA13与三次witness只限所测；fault-to-safe、outage、fault-to-catchup不同指标，不拼成统一延迟。当前修订是实际安全反侧，不说May原稿已有PoR、不另May事件评分。实际读Ch63原faultdomain两完整段、前ScaleRAN／后portfolio交接，6分实际安全差额深入；已报root协调原两段后一段＋note，未授写入完成／POST。

## R16 — 五项真实 POST、量化与多模态后批必要层

### 五项保存后唯一实际 POST 已通过

作者保存后，本人实际读 RICE26352 Ch33、Forge26494 Ch31、E3C26316 Ch25、MPS26461-supp Ch63、Jensen26266 Ch45各完整新增、完整直接两侧与本人note；限定两层diff-check均通过。五指定窄位即时生效释放，已通知root／作者，不再第三读或行政重复验收。MPS正文与note明确“current-v2（10月2日提交，非公开日）”，Oct2仅Submitted精度，不能从其推公开事件日期；R15缩写由此精确限定，不扩10月日报。May v1提交May26 02:18:53Z＋registeredMay27 02:09:46Z；26289另实际补核registeredMay27 02:05:45Z；两者arxiv.content/findable与原v1合界均BJT27。

### 26266 Jensen correction：必要理论／代价与差额

本人实际v1§4–6／A／B完整必要：独立零均值近uniform key-noise使exp项期望增加，逐score log-MGF纠正的是exp/partition期望，不是E(normalized softmax)无偏，value误差更未恢复。Taylor variance/2仅小noise，INT2可过修、少数集中token平均不足，biased/nonuniform须重推；单token current/history比例不同。MAGI4.5B16steps／SkyReels1.3B50／HY8B4、INT2 g32＋FP8 scale/BF16 zero=2.75effectivebits，QVG2.52另协议。30%VBench-Long／HY10pairs与BF16fidelity有限，FlexAttention约5%额外E2E相对quantbaseline，不用50%cachebytes冒全部HBM/服务速度。Ch45 inner-grouping两完整段与QuantWM witness及CacheGeometry邻接实际比，有期望补偿具体缺口，6分深入；既成POST见本节开头。提交May25 18:51:59Z＋registeredMay27 02:05:13Z及arxiv.content/findable合界BJT27。

### 26339 QAM-W：六分标准与具体 NC

本人实际v1§3–6／Limit／J4。row norm、sign-Hadamard、相邻pair/calibration、joint2D Lloyd、packed indices与AWQ-style scale；rotation isometry不使Gaussian，理论bound不证明实际KL排名。strict4bpw QTIP更好，5.5不同预算不是Pareto支配；主三模型只MLP，attention/head BF16，MLP+attention／Llama2扩展另人口。WikiText16K／KL4K、six-task限300/500、MMLU各subject300与±.2非equivalence；A10080GB总20h是研究费用非推理吞吐。所有weights先dequant BF16，无fusedkernel，16KB codebook不授真实加速。Ch49 1190–1219完整执行费、checkpoint/HBM/请求三结论、非uniform码本/assignment/layout/变换/kernel合同实际承载长期判断，NC；有限新codec工作点不为diff再加一段。提交May25 21:28:46Z＋registeredMay27 02:06:55Z及arxiv.content/findable合界BJT27。

### 26496 Dense2MoE：六分中心争议隔离

本人实际v1§3–6／T1–3／D／F5。cos+norm只校准选择，既不全输入无shift也不保全知识；保首attention、移其他MLP成heterogeneous专家、Top1／N6／225B CPT。主表Thor-U Roofline估算195.87→174.95与另报empirical307.5→271不同口径、真实engine/precision/repeats未披露；较低理论下界不认证实际更快或公平全pipeline。0.5B MMLU、1.5B MMLU/CMath/ARC等退步、NonPruneUC均分更高；N6静态3.32GB还漏runtime/KV，active.42B不是resident.42B。Ch21 joint conditional/兼容模块/破对称完整段与邻接已比，无正面净部署采用。中心efficiency／perfect-knowledge保留争议，不降分EX；重开需匹配CPTbaseline与真实engine/precision/repeats/统一延迟口径。提交May26 03:19:04Z＋registeredMay27 02:10:39Z及arxiv.content/findable合界BJT27。

### 26460 AnchorDiff：五分标准、仅报告

实际v1§4–6／T2–6完整必要。concept argmax仅seed，image-attention row-cosine top2% gate与output feature cosine权重传播分责；Wcos可负，行sum归一不自然成为Markov概率，不采严格扩散保证。SD3/3.5、1024²／4096tokens、midpoint／额外concept forward/inversion／160propsteps与图驻留全费，.52s不是完整生成。1272混synthetic/real／2842pairs，Qwen2.5VL＋SAM2＋人工非绝对GT；foreground-only和whole-image分母分开，部分AP/NAR对照更好。89–90%seed误差、单seed漏disconnected多实例、过长spillover；§5.1{10,23}与后{23,31}不合，不照recipe。Ch23dense读出/representation身份实际比，有限frozen-MM-DiT工作点不新授语义真mask或长期跨域机制。提交May26 02:17:29Z＋registeredMay27 02:09:45Z及arxiv.content/findable合界BJT27。

### 26230 GARD：五分标准、仅报告

本人实际§3–5／T1–5／B3–4完整必要。DA3 18/40内feature恢复后经原geometry与另训RGB consumer，degraded+.3noise source及clean DA3-derived对应alignment共变，alignment单用可退；同源clean重建不是sensorGT。H100 FP32／10epochs／global8、Hypersim/TartanAir syntheticblur、up-to4views训练而test10/30/50，只限支持域。50Eulersteps不是oneNFE或single-forward实时，cleanHQ仍更强，部分baseline指标亦更好。Ch23开头representation/artifact/coordinate及densegeometry读出2605-15876完整论点实际比，有限consumer-conditioned恢复空间实例不授所有VAE损几何或普遍恢复规律，不写Books。提交May25 18:01:05Z＋registeredMay27 02:04:22Z合界BJT27。

### 26449 CAT：六分长期差额深入，待 POST

实际v1§3–4／6–7／T1–5与F3–9图注必要完整。blockdiagonal D每尺度marginal realism不保同sample轨迹，G pre-resize hk与自产hK weighted consistency；不是取消D、独立真值anchor或runtime lock。ImageNet256／SDVAE／B/M/H133/261/960M、D96M、batch512、lr2e-4、FID50K trainstats；sameconfig有/无cons和λ0/.1/1支持局部机制，强λ反退。scale-aggregated对照同时取消mask和cons，不能独立归因；crosspaper16.7xGFLOPs非匹配墙钟，部分IS更弱。Ch24 SemanticLock两段与preview完整两段实际比，训练same-sample监督链未覆盖；root已授两段后/preview前最小一段＋note并给逐字稿，待作者保存后真实POST。提交May26 02:01:11Z＋registeredMay27 02:09:30Z合界BJT27。

### 26478 SDPG：五分标准、仅报告

本人实际§3–7完整必要。N nominal视觉/observation冻结、M state-only扰动／短H／privilegedcritic的局部计算分路；Gaussian式只δ/σ缩放smooth surrogate，不能把openloop辅助rollout称同policy closedloop无偏，不采用Eq3漏1/2的精确更新倍数。64render内比较与PPO4096memory估算分开，RTX4080／Genesis、visual2–4倍iterations、Go2depth两小时与所示terrain不签安全／一般sim2real；seed不稳、discarded rollout和simulation主费保留。Ch26局部trajectory优化／actor-vsprivilegedcritic／真实controller既有完整段已比，有限实现实例不改变长期跨域配方，不写Books。提交May26 02:35:08Z＋registeredMay27 02:10:10Z合界BJT27。

### 26470 TriPS：五分标准、仅报告

本人实际§2–6／E1–2／F6／A4。DC/CFG/stochasticity联合日程校准是局部增量；A4把clean-pred状态差直接套latent Euler，以经验cos近1替换gradient和unitDC内积，方向近不认证幅度/精确Eq9，λ还影响cleanpred/DC，不授该定理。Beta-Bernstein只保证range非monotonic，正文承认局部非单调。100cal/testdisjoint、A100／78policyparams／200iters／G4、SD3.5M768²28NFE／SD1.5 512²50NFE，完整search成本不省略；F6十图部分baseline更快，perception/distortion反向。Ch24conditional/noisymeasurement/guidance费用现段实际比，有限联合校准实例不授新posterior或manifold机制，不写Books。提交May26 02:27:30Z＋registeredMay27 02:09:58Z合界BJT27。

### 26384 GridPilot：六分必要边界深入，待 POST

本人实际v1§3–7完整必要，Ch63 power三层/当前family完整段、前crossAPI两段与后powercap两段实读。facility meter与board cap不等，负载/温度PUE、冷却floor可抵消IT降幅；仅model预测不签外部履约。3V100SXM2／580.65.06／CUDA12、FP32GEMM／ResNet50B1FP16／4秒bursty；E7九十syntheticUDP到95%capsetpoint，中位约97ms/最大101.1不是严格sub100，100Hztelemetry不认证200Hz硬deadline，SCHEDFIFO条件liveness不证OS/NVML及时。E4bursty11.08%越5%事实保留，不因改名diagnostic授通过。E8 M100trace＋syntheticCI＋PUE的1–50MW是模型，E5仅design，非设施碳/TSO资格实测。root已授现family段后/共享powercap标题前最小一段＋note，逐字稿已给、待真实POST。提交May25 23:14:52Z＋registeredMay27 02:07:57Z合界BJT27。上述本节其余日期均已逐身份实际核bulk arxiv.content/findable，不把registered单字段改名为公告。

## R17 — 后批安全必要域与四项真实 POST

### CAT／GridPilot／SurfaceLoRA／ConceptualSteg 实际 POST

CAT26449 Ch24、GridPilot26384-supp Ch63、SurfaceLoRA26433 Ch72、ConceptualSteg26537 Ch72作者保存后，本人一次实际完整新增、完整直接两侧及本人note POST均通过；限定两层diff-check通过，四精确窄位生效释放，root／作者已通知。前两项R16待POST由此覆盖；后两项具体必要层及差额见下，不授DAY／实现／复现。本人note仅行政同步既成事实，不再额外复核循环。

### 26433 SurfaceLoRA：六分安全差额深入，整合通过

实际v1§3–7／T1–2／F1–2／H完整必要。exact pre-generation lasttok与meanpool／output不同artifact，冻结backbone/LMhead/decoder、LoRA/GRL与training adversary不同于post-hocLR/MLP；validation-only LR预算选ckpt/最终独立test，MLP非selection角色。193470/21552/24445 patient-disjoint、balanced20k/2.5k/2.5k五类chance.2不改部署prior；race是行政登记非生物真值。BF16/TF32、单GPU process型号ND、prompt1024/full1536／greedy256／固定seed／2000step与六λ搜索全费。lasttok near-chance CI含.2不证明零信息/DP，meanpool仍.32/.30、后期泄漏反弹、meanpool-target仍漏，output attacker仍.299/.616；词面utility不授临床保真，neutral meta-term不是genuine身份泄露。Ch72 HiddenStateRelease24042两完整段与Capability完整交接实际比，缺exact export/ckpt选择资格及不移转反证；root授该两段/marker后单段＋note，既成POST通过见本节开头。v1May26 01:38:13Z＋registeredMay27 02:09:05Z及arxiv.content/findable合界BJT27。

### 26454 goal-dependent unlearning：六分深入、仅报告

实际v1§4–7／T1／全部必要图注及AppB，未看曲线pixels不称已看。cosine目标只方向不保norm、random方向不证明删除；frozen TRuST-labelprobe与同classifier评测coupling，两任务数据/目标/评价共同变，不能独归语义function机制。REINFORCE α欠policy/reward/outer协议，不采用best-possible自动平衡recipe；S乘积不等Pareto/安全，Llama WMDP S=0灾难点、多层loss上升与层组合非单调保留。AppendB实际two epochs/up-to4 RTX A6000／约1h、RLlr1e-2/main5e-5/Adam；已纠作者硬件主文ND的概括，precision/seeds仍ND。Ch72 secret-substrate/observer／parameter重定向完整段实际比，局部function-target选择实例不授新删除机制，不写Books。v1May26 02:10:55Z＋registeredMay27 02:09:37Z及arxiv.content/findable合界BJT27。

### 26537 Conceptual Steganography：六分深入、整合通过

实际v1§2–4.9／Limit／A／B完整必要。受控compromised sender/shared convention、matched carrier-only baseline、四模型MATH500/GPQA198／seed42/T0；hostedAPI且能关thinking时关，审计的是visible response不是内部思维。message/bit/step与信息论capacity/stealth分开，多strategy互扰、换paraphraser大退、strategy-aware只一strategy/GPQA/三模型且残余，未训detector不签不可检测。NoCoT短cap/提示禁止只下界，不能证明必须公开完整CoT；再答partial reasoning不证内部因果。DeepSeek raw-tokenization错误与prefix-only修复数字分开，不把修复当raw或外推性能。Ch72 1078–1110 monitorability相关完整段已读，现paraphrase破部分误读未承载高层carrier仍被保内容变换保存的反证；root授2609-31121两完整段后/Agent-as-Proxy前最小单段＋note，既成POST见本节开头。不含payload／编码recipe、不授自然合谋/真实外传。v1May26 04:38:56Z＋registeredMay27 02:11:37Z及arxiv.content/findable合界BJT27。

### 26526 open-weight defenses：必要 Source／具体差额已过，待窄位

实际v1§2／4–5完整必要、current-v2§4setup／5／A4受影响完整。只检验finetune-tamper保护人口不自动覆盖非finetune权重编辑／可控输出prefix接口，不给attack recipe。v1 Llama1/3/8、Qwen/Gemma1–2、HH SEAM2000／TAR750outer4–16inner；perprompt best layer/strength是search人口，不冒fixed single-shot。HarmBench13B／AlpacaROUGE与关键词拒答是有限proxy，ART仅Gemma1B额外200step，残余49/64/55及combined更高、utility亦反退，不签minimax或全部开权安全不可能。current-v2（Oct6提交非公开日）新fixededit/val/budget/8B多defense与T8只后续，不倒灌May；尤其只有新增T8在A4换BeaverDam7B/heldout，current§4及T1–7仍HarmBench13B，已纠作者笼统“v2换judge”的说法。hardware/precision/seeds及全budget未披露，search/inner-defense训练费保留。Ch72CapabilityAccess开头原四行与后2601-16034完整交接实际比，缺攻击权限人口不能继承的具体设计边界；6分安全深入，已请root该开头段后/2601-16034前一段＋note，未预授保存／POST。v1May26 04:18:42Z＋registeredMay27 02:11:22Z及arxiv.content/findable合界BJT27。

26332 BEAP 日期原件已实际核May25 21:11:59Z＋registeredMay27 02:06:45Z、arxiv.content/findable合界BJT27；current-v2 Oct5只是提交日期。其必要原文层仍普通待办，不以已下载或作者current层当本人完成。

## R18 — 开权权限实际 POST 与三项必要审阅／理论争议

压缩恢复后实际重读当前AGENTS、Research/Report合同、来源使用说明/每日十四源及主题、统一Prompt、完整ROADMAP及Books适用三个说明。工作树中大量并发staged/unstaged保留。当前磁盘LS末尾止113/279，不拿旧路由覆盖root当前任务146/279的单日授权，也不继承他日池。

26526作者保存后，本人一次实际完整新增、开头原四行完整前段、后2601-16034两完整段及本人note POST通过；限定cached/unstaged diff-check通过，指定Ch72窄位释放。至此十九项实际整合通过；未授DAY。

### 26332 BEAP：六分安全深入，具体已有覆盖

本人实际v1§3–6／T1–4／AppB与current-v2§IV全部必要。query-only针对victim权限，外部CLIP不取消该定义；邻近embedding不证明victim内部知识身份。v1 SD1.4关safetyfilter、I2P最高200、DeepSeekV3.1／十轮十候选，同NudeNet/DINO/ImageReward/Aesthetic既搜索又验收，不是独立heldout；successful-search均值不含失败全预算。ESD w/oEG presence99高于full95，MACE All44高于full42，不采模块单调必要；五十golfball仅探索。gibberish/perplexity低不授不可检测，代理命中不证明永久残留物理表示。current-v2新增heldout OpenNSFW2/ResNet50／三runs／fullbudget32.1是后续，不倒灌May；画质仍搜索目标。硬件/precision与完整LLM/encoder费ND，不称复现。Ch72§Unlearning secret-substrate/observer及NLCE／EGLOCE完整论证实际承载跨通道、代理/内容/画质三分责与独立攻防/全费，具体NC，不再写段。日期沿R17有效层。

### 26282 MBDPO：六分中心理论争议，隔离暂缓

本人实际v1§3–6／AppendC4完整与A1.6两表完整。batch跨state negatives不一般等uniform action，energy缺negative-density校正；future C(zh)依赖动作，short horizon不保证常数。C4 Eq71/72给β·exp(G/η)，Eq73用η而实现Eq11用κ，末尾relaxη→κ不修复实际β^(η/κ) prior与折扣/轨迹常数；不授exact optimizer／monotonic或真实环境安全。有限self-normalizedMC／learnedmodel与score近似另有误差，latent投影整齐不证causal。A80080GB在线per-step接近，H200离线十M steps／1.7–340M；十episode评估普遍约1.4–2倍更慢，不把训练近费改成部署加速；大η／340M退步保留，precision ND。无正面Books采用；重开需一致prior/temperature证明、模型偏差及完整同费对照。实际abs唯一v1May25 19:06:51Z＋exactDOI arxiv.content/findable registeredMay27 02:05:36Z合界BJT27。

### 26414 PAL robustness：五分标准，仅报告

本人实际v1§5–7／两主表／具体反例完整。Haiku4.5／同一千paired题，CoT97.9→96.6、PAL97.2→95.5、SBSC96.4→95；break/fix分开有意义。prompt/system/prefill/十五轮errorfeedback共同变，来自一百原题的重复聚类不满足χ²独立，p=.096非等价检验；两次API运行与T0不保证snapshot deterministic，污染未控。不能授所有tool无益／模型不推理；hardware/precision API ND。Ch78 ToolEvidence/FormalProof完整相邻段实际比：证明/执行的形式对象可能不是用户问题，有限高ceiling反例不足新增长期机制，不写Books。abs唯一v1May26 00:44:49Z＋arxiv.content/findable registeredMay27 02:08:39Z合界BJT27。

### 26489 SoSD：六分中心理论争议，隔离暂缓

本人实际完整v1§3–6／AppendC全81–144／AppD必要设置。单层单头、fullbatchGD、固定classifier／smallinit／positive-margin及strictnormincrease不移转一般预训练；严格增不保证无界，normalizedspectrum不限制singular-vector rotation。Eq81–89只给δ上界及gradient下界；143–144由ε=O(η/τ)把τ^-p反向替成O(ε^p)未获依据，QK混项化同τK亦无相等条件，不能授loss被实测δ^p上界／普遍kineticbottleneck。经验LR/WD/Muon相关仍保，不降分EX。GPT改RMSNorm/RoPE/SquaredReLU、124/355M/FineWeb与不同lr；LLaMA0.5/2B C4／L2048／G512／100k步，FSDP HYBRID_SHARD／BF16mix+FP32参数已披露，hardware型号/repeats ND。隔离中心理论不进Books；重开需证明方向/旋转与norm条件及匹配干预。abs唯一v1May26 03:03:24Z＋arxiv.content/findable registeredMay27 02:10:26Z合界BJT27。

## R19 — 后批六项必要 Source 与具体 Books 判断

### 26484 Extra-Merge：六分因长期差额深入，待 POST

本人实际v1§4–6／B全部配置与C3必要PCA证明。先平均同轨迹checkpoint压局部横向摆动，再对四份merged作PCA／时间定向／validation line search，区别直接raw低秩外推；局部EVR>94%不证明全轨迹rank1。straight river／IIDmountainnoise／stationary／eigengap及samplecov concentration是额外条件，不由真实曲线认证；Pythia同四task均分兼search indicator不授独立heldout，.59pp非equivalence。8×4090＋2H100／BF16、PythiaFP16/B16/L2048，GPT20k/G512及Llama100k105B；主WD.1与B的0/.125等精确配置冲突保留，seeds/repeats/fullsearchwalltime ND。checkpoint准备、K²大张量内积、每候选验证与artifact回归全费。Ch35 21468完整两段、前updateintegrity与后格式交接实比，缺平均后估方向的具体选择；root已授两段/marker后单段＋note，已给最小稿，尚未预授POST。absv1May26 02:48:34Z＋registeredMay27 02:10:18Z、arxiv.content/findable合界BJT27。

### 26485 OmniInteract：六分因评价缺口深入，待 POST

本人实际v1§3–5／Limit／A2／A4全部必要（另A5案例文字读，不称看pixels）。250录像1430slots/192interruption，latest-start匹配／wordlevel早晚分割／softTP时间衰减非传统F1；interrupted免FN使silence不被global惩罚，须分NOR／有输出条件spill／partial质量与outer恢复NCCS。1QnA TTS与1Q1A真人声不同，录像online回放无future不是真人闭环；MiniCPM offline全video到online既换信息集又换执行，非纯duplex因果。GPT4o external不等独立人校，硬件precision/repeats ND，全部对齐/生成/判分费。Ch66 2609-21392两完整段及ResourceBudget交接实比，只先demand不承载受理后时窗/中断分母；root授其两段后单段＋note，最小稿已给，未预授POST。absv1May26 02:49:47Z＋registeredMay27 02:10:20Z、arxiv.content/findable合界BJT27。

### 26415 Rescue：六分标准，具体已有覆盖

本人实际v1§3–8／T1–4完整。CLIPViTB/32仅视觉Linear dynamicINT8／textFP16、RTX3090，SSA128117 labels+FP32teacher／3epochs／独立5k gate／25thresholds／3runs。rescue947/loss710是paired结局非noise唯一因果，52%不叫noise超过signal；相关patch不授IID N倍理论。factorial支持有限head/routing增量，主全gain不独归quantnoise；零样本classprompt不等无监督未见labels。FLOPs仅exitdepthproxy，不含实际gate/head墙钟，torch dynamic GPU执行未核不授核加速。Ch49 2038–2042两完整early-exit段及两侧实读：训练中间状态/head/sensor匹配、controller只提案、quality/backend回退及全费已承载，不新写。absv1May26 00:45:46Z＋registeredMay27 02:08:40Z、arxiv.content/findable合界BJT27。

### 26431 结构 Probe：五分标准，仅报告

本人实际v1§3–6／Limit及current-v3§4.3完整受影响域。UD r64／13base1–27B／English3kstrings／1000cluster／FDR，canonical层仍按finitepeak选点，不授独立无选择估计。May直接patch被测subject再读包含该word的probe，非真实行为依赖或MinimalistPhase唯一解释；July17提交v3换matrixverb／双向／sameclass／新band人口，只标后续不倒灌。RTXPRO6000Blackwell/<2h，precision ND；形态词类共变与有限样本解释保留。Ch5 45及72–82实际读出/消费/跨construction完整段已比，有限annotation-conditioned几何诊断不改稳定因果机制，不写Books。absv1May26 01:36:41Z＋registeredMay27 02:09:02Z、arxiv.content/findable合界BJT27。

### 26365 文化 steering：五分标准，仅报告

本人实际v1§3–7／AppA全必要。600scenario/300优化300test／A/Blogit／mean-difference四层grid、T4FP16/18GPUh/seed42。rawtoken概率不授真实latentculture，countrymean取最近category非mode；E=.7–.9跨轴共变不由WVS r=.474证单一feature或人类社会因果。主Gemini2.5与App1.5生成身份冲突，法律/工作规则与价值混，α.2/.4/PPL自产128tokens不授全utility、architecture rigidity或普遍安全。Ch5表示可读不等功能/选层与独立行为真实段已比，有限场景测量不改变长期steering配方，不写Books。absv1May25 22:20:52Z＋registeredMay27 02:07:31Z、arxiv.content/findable合界BJT27。

### 26362 structured hallucination：六分标准，仅报告

本人实际v1§3–9／T1–3完整必要。S用gold shortestpath/tableanswercell、E邻域，线上无gold不可直接部署；penultimate residual非FFN独占，弱相关不证互补causal。Q3最高仅1hop/WTQ，2hop Q4最高54.4%，highSAS仍有halluc不授低SAS必要/充分。MetaQA1hop5k/20triples、37.5ktrain80/20 XGBoost、Llama2/Qwen2.5 7Bgreedy，EM或F1≥.3标签非完整真实幻觉；hardwareprecision/repeats ND。每triple额外编码／全attention存储非single免费。Ch5读出vs因果与Ch66 388–400 oracle诊断完整段实际比，有限oracle-conditioned代理不改长期机制，不写Books。absv1May25 22:08:59Z＋registeredMay27 02:07:27Z、arxiv.content/findable合界BJT27。

## R20 — 两项实际 POST、后批五项与 Forge 真实去重纠错

26484 Ch35与26485 Ch66保存后，本人一次实际完整新增、完整直接前后及本人note POST通过，两层限定diff-check通过，精确位释放；暂合二十一项实际新增，未授DAY。下方Forge纠错尚待恢复实际POST，不能用旧通过继续计本日新增。

评分精度：作者A20/A21把原准入五分的26366／26322／26315转述六分；实际对象未扩，沿原1+2+2=5。安全内容必要深入仍有效，不因深度抬分。作者又提议26542／26497从七降六，本人要求实际误判依据后，作者确认没有SystemReach新证据、只是转述误记，保初筛2+3+2=7；有效Source/POST不重做，旧118任何行不动。

### 26366 FEPoID：五分标准，仅报告

本人实际v1§3–6／AppA完整必要，规范化current§3–5与v1完全同文实际比。TwoNN firsteffectivepeak和首句末token只有限经验选择，非天然semantictruth/普遍最优；supervisionfree只selection/FST，MLP仍监督。QA十样T1与best T.1不称deterministic，QA30/summary130与9k/1k trainval、固定独立test；FST也改baseline测量对象，可能丢后续纠错/长summary内容。Table4 ID十秒不含同样MLP全部训练费；hardwareprecision/repeats ND。Ch66 262 layer/token/截断量尺、351–353 probe选择与独立输出实际完整段已比，有限启发式不固化新长期配方。v1May25 22:28:23Z＋registeredMay27 02:07:33Z／arxiv.content/findable合界BJT27。

### 26322 OmniToM：五分标准，仅报告

本人实际v1§3–7／B4完整。完整story extraction与providedgoldbelief labeling是两任务，非E2E或online追踪；七维belief标签诊断endpoint盲区，不授真实心智。21story calibration的83.72是无reconciliationremark比例、92.23严格三人标签agreement、GPT5语义72.03%，不称895全人工真值。MatchCount>0双向二值不自动去所有duplicatecredit，Stage2高schema分不代表自由抽取已解决。A10080GB/按需4bit/约48h每openmodel、closedprecisionND、repeatsCI未闭；全部标注/调用/校准费。Ch66任务/输入权限/阶段scorer及human-calibration完整论点已实比，有限标签benchmark仅报告。v1May25 20:45:08Z＋registeredMay27 02:06:31Z／arxiv.content/findable合界BJT27。

### 26356 RAG-GD：六分标准，仅报告

本人实际v1§3–7／G／H全部必要。线性无softmax平方loss的存在性一GD构造不是frozen现代LLM等价；fixedBM25/E5 top5与generator QKV LoRA适配分责，gold三support EOSmean→MLP rank16增量／离线1/5/10SGD target distill，部署无backward不等无adaptation。同retrievalcache/baseadapter与同架构HyperTuning支持局部，PopQA/Bamboogle留出有效而LlamaBM25 Bamboogle反退；NF4/A10080GB、adapter50–60min／predictor1.5/4/7h／whole50GPUh及支持前向费不可省。两个rankr权重差可到2r，预测r有限近似，noisyretrievalgate尚未来。实际读Ch30 323–327条件生成LoRA/proposal身份全费及Ch76 fixedretrieval/reader交接，GD监督target是有限算法实例，不改长期参数proposal验收/事实权限，不新写。v1May25 22:04:54Z＋registeredMay27 02:07:18Z／arxiv.content/findable合界BJT27。

### 26380 VisualNeedle：六分标准，具体已有覆盖

本人实际v1§3–5／AppendA–B完整必要、current-v2§4.1受影响完整。300curated/9API/20turnfresh，blackcrop只保schema/dimensions而非全部adaptive后续轨迹，initial全图仍有，黑图OOD不授纯视觉依赖因果。v1三run诊断被current改once，不能授相应CI；主有/无tools三run有效。Gemini3.1Pro既受测又fallbackjudge，独立接口不等独立真值；humanmajority3/pass3与单API预算、resize各异不签公平能力排序。Ch78 287–295完整三续写同前缀／可比返回物／费用，及Ch66 freshpaired≠重评分完整段实比，具体已有覆盖，不写Books。v1May25 23:01:05Z＋registeredMay27 02:07:52Z／arxiv.content/findable合界BJT27。

### 26248 UNSL：六分标准，仅报告

本人实际v1§2／4–6／App8–10／13–14完整必要。multivariatebrokenpower/additive/reciprocal/bottleneck/overfit/hyperparameter可拟合族为有限统计替代，不授唯一普适机制。观察点内val选n/S/λ、20seed20kKFAC按trainloss选seed、独立circle外推；同supremalexpressivity不等同有限参数量/优化费，rootstdlogerror是残差点SE变换非trainingseedCI。32任务非全优，parity100+seed/noiseless需近hyperbreak，不签未见新regime；异构旧run与硬件precision不统一，不拼训练收益。Ch7 102–135联合surface/grid/可辨识轴/独立外推完整已比，不把灵活拟合公式固化成预算配方，保报告。v1May25 18:15:27Z＋registeredMay27 02:04:48Z／arxiv.content/findable合界BJT27。

### 26494 Forge：具名早正文实际恢复，EX 重复披露

作者formal定点发现旧官方Forge正文；本人实际打开[MiniMax-AI官方HF文章](https://huggingface.co/blog/MiniMax-AI/forge-scalable-agent-rl-framework-and-algorithm)，明确Published February13,2026，§3.1完整已含本次唯一采用windowFIFO：W=.3N、只head-window内ready、outside禁止、head消费才推进；另§2与3.2同白黑box/prefix机制实际读。故不因May新arxiv重计同一披露，不移动旧Daily；原v1必要Source仍有效，R15/16的May候选／新增采用资格由此纠正。已报root／作者仅撤本轮Ch31 26494新增单段及本人note，原cluster/旧family/其他来源与并发段全部保持；恢复后尚需本人一次实际POST，不预授已恢复或日级计数。

## R21 — 末批必要层、真实去重恢复及第21项 POST

恢复时本人完整重读当前AGENTS、Research/Report合同、来源使用说明/每日十四源及主题、统一Prompt、ROADMAP与Books适用说明及最新磁盘LS路由。磁盘仍止113/279，只作路由，不覆盖root实际本轮授权。原118、小时窗、连续旧§4及并发staged/unstaged保留；不stage/commit/push。

Forge26494作者按root精确授权仅撤本轮Ch31单段与本人注后，本人实际完整原cluster正文、直接前后及移除范围恢复POST通过，26494正文/注引用均归零，原20863完整保留；限定两层diff检查通过。26242作者保存后，本人一次实际新增全文、原18280两完整段与后2610-06174完整交接及本人注POST通过，限定检查通过，窄位释放。净真实整合21（原21减Forge加26242），不是22；下方R3仍待保存/POST，不预授。

### 26315 StagedCompetence：原五分，安全必要域深入，仅报告

本人实际v1§4–6/D/F/G。bucket内sqrt competence采样与stage reference更新，同clean GPT4omini pairs；T.7/512后MiniLM256截断难度不是安全真值。LoRA16qv/L1024/G32/A600048GB，precision/repeats ND。固定步数一般条件有Yi4对5epochs例外，重复采样改变人口；abliterated起点非生产，clean与eval同族偏差不由强judge取消。200unsafe teacher-forced128token抑制不证深层alignment，固定旧base GCG transfer不等逐defense adaptive；不展开操作payload。YiMMLU63.5→59.4与XS1.2→3.6、50%Qwen反退均保。Ch34 pair资格/candidate源/label真值/reference三分责完整论点已比，有限课程不授长期安全recipe；保原1+2+2=5，不随深入抬分。v1May25 20:13:06Z＋registeredMay27 02:06:21Z/arxiv.content/findable合界BJT27。

### 26379 LeJEPA identifiability：六分中心理论争议，隔离暂缓

本人实际v1§3–8/B/D/G必要全域。restricted jointGaussian isotropicOU的Hermite forward条件结果有效，不否认；但一般independent stationary additive不推出linearOU，Gaussian-measure-preserving非线性m(z)+独立Gaussian可保持边缘。从离散additive到连续可逆diffusion/SL generator尚需embedding/regularity前提。D1共同旋转state与goal或协变matrixcost不等原state-only O(n)不变cost；已知pushforward也不是已学transition，§8承认需另学。Lean zeroSorry表实际含Hermite/polar/pushforward axioms，未亲自build。五seed synthetic/三Reacher/三十startgoal与真实轨迹多前提共变不授唯一因果；hardwareprecision ND。无正面Books，重开需准确converse前提、离散嵌入与controller资格。v1May25 22:56:26Z＋registeredMay27 02:07:50Z合界BJT27。

### 26242 Introspection：六分设计反证深入，实际整合通过

本人实际v1§3–6及current-v2§3/4.1/4.3必要变化。input-layer0可预测LR/PCA/BD标签、randomlabel/input/hidden三类对照说明binary selfreport与语义/anomaly兼容，不授普遍无metacognition。BD450train与30ICL、十五split不等同样本效率；binary reproduction选layer/strength/prompt，Gemma全sampletokens注入与其他prompt-only不同。v1固定deterministic h若I(t;y)低而I(h(t);y)高违反DPI，定义不采用；v2弱定义与新增Qwen32B只后续不倒灌。Ch8与Ch66实际18280两段/量化自报交接缺internal-origin label≠privileged monitor反证，root授最小段、本节实际POST已通过。absv1May25 18:07:49Z/registeredMay27 02:04:39Z合界BJT27；currentAug21为提交非公告。

### 26293 CroCo：六分标准，仅报告

本人实际v1§2–7/Limit/D及current-v2§4.2受影响完整。64selfcandidate各语言RM排序、max与μ−2σ/rewardSFT/DPO；SFTlr2e-4对DPO5e-6共变不授唯一contrastive原因。offpolicy aya→Euro质量也变，不是仅supplier身份；Danish online16对offline64不同预算。currentMagistral judge aya Danish/English反退、Gemma仅English正，不倒灌May。MI250×8/node约8000GPUh、LoRA16qkvo+MLP/TRL.28/vLLM.15，precisionND；EuroEval三seed不是全训练重复或等价。全部translation/RM/search费。Ch34 pair资格/候选采样/label/ref实际论点已比，有限语言操作点不固化长期原则。v1May25 19:30:45Z/registeredMay27 02:05:51Z合界BJT27；Findings2026不自动更早公开。

### 26355 EGA：五分标准，仅报告

本人实际v1§2–7/T1–2。postsoftmax乘gate后renorm Eq5与presoftmaxscore乘gate Eq10不等；线性w·x非Parseval quadraticenergy、μσ轴未定义、每j局部projection不能授全gate因果，未核代码不指控实际泄漏。六层八head256dim≤6M/T256/TinyShakespeare5kstep单seed，两session EGA差.011非重复验证；joint+.119与MoPEalone−.032保局部反侧，不授orthogonal信息/物理wavelet因果。hardwareprecision ND/长context未来。Ch14 routing/value/renorm完整链及Ch13ALiBi/fusion已比，有限组合仅报告。v1May25 22:04:31Z/registeredMay27 02:07:17Z合界BJT27。

### 26232 UniMVU：五分标准，仅报告

本人实际v1§3–6/T1–7，首次工具输出4.1–4.2截断后已精确补读该完整域，不称截断完成。共享control，withinmodality token norm与acrossstream norm分责；O+βwO只是soft增权非harddrop，instruction restore不隔离LLM后续，absentmask只支持声明subset。0.5/7B冻结encoder+LoRA，双H200/r64或128，single80/91h、unified81/93h，precision/repeats ND；消融仅MusicAVQA、7B共享audio/AV/AVQA反退，容量/mix混杂，权重非真实provenance。Ch23 producer/consumer/positionmask/gate完整论点已比，本例有限两级gating不授通用plugplay。v1May25 18:02:20Z/registeredMay27 02:04:25Z合界BJT27。

### 26371 CARL：五分标准，仅报告

本人实际v1§3–7/A/B，与current-v2§3–6含表规范化实际同文。近expert offline state-goal与k-action InfoNCE仅behavioral similarity heuristic，非所有动作bisimulation；goal在k内随机但配fullk动作，末段padding重复、humanoidstride4。五room encoder已见全room非unseen；二十room4/16另一协议。OGBench八state/四pixel seed、20episode/RTX5000/~4或10h/~10kGPUh，precisionND；representation10→100与horizon/aux选择全费，teleport/visualhumanoid/cube零或负、UMAP不证entity permutation/composition。Ch26 skill/controller/support边界实际比，有限offline recipe不授长期skilltransfer。v1May25 22:39:14Z/registeredMay27 02:07:39Z合界BJT27。

### 26486 LongCat1.5：五分标准，仅报告

复用实际准入§3.4/4/5.4，补读§3.1–3.3/5.1–5.3完整。sharedDiT baseRealScore加G/FakeLoRA角色只减少同构驻留非完整VRAM/运行测量；Whisper1.5B33层分五组、50Hz→25FPS→VAE降四及perframeGRPO/可见手/多clip末段优化共变，不归单因。508pairs/770crowd13240ratings/10expert，single与multi支持不同；8NFE对base150，human3.389→3.336/harmony44.2→45反退、stability12.3→4.3改善是有限取舍。hardwareprecision/wholebudget ND，400step停点、1:5fake更新及全部encoder/evaluator费保。Ch24 K-DMD角色共享与质量/teacher/fake总费原论点已比，有限avatar操作点不固化新配方。v1May26 02:54:12Z/registeredMay27 02:10:21Z合界BJT27。

### 26520 InterSketch：五分标准，仅报告

复用已实际§3.3/4.3/C1–3，补读§3.1–3.2/4.1–4.2含完整主表。92k合成的posthoc VLM before/after解释非真实内推理，错误tool返回Err不改图/错误tokenmask；36k RL选八rollout成功1/8–7/8人口，非全任务。Qwen3VL8B视觉冻结/SFT两epoch/B256/L32768，GRPOgroup8/B128/async15turn/response32k，hardwareprecision/repeats ND。GT-action metric与GT-conditioned GPT4o sufficiency仅训练证据，Eq7负logprob/零分母不采精确credit；各训练/反思/评估费不由turn少取消。TIR51.8对22.3为29.5pp，spot/searchgame等非全胜。Ch78 287–316实际调用边际收益、单片段充分性、生成diagram假设来源已分责，本例有限训练接口不新增稳定recipe。v1May26 04:07:49Z/registeredMay27 02:11:14Z合界BJT27。

### 26519 R3：六分因实际长期差额深入，待实际 POST

本人实际v1§3–5/C/F/J；current-v2同域实际词级差仅引文与重复词更正，不是May新事件。relative pairhead分别R/Tconfidence、晚绑定global pose聚合，与novelty/staleness20/cap100 bank分责；frame1仍固定，c residual−αlogc不是校准概率。reject已过backbone才删KV，三frame校准/三rejectreset，bridge3–10重跑且metricdepth scalar仍漂。六48GB/BF16/110Mtrainable/372M/4–32views，hardware具体型号ND；1000frame主测与J eventualdrift不授无限stream，无rawpast再看。target/loss共同变、streamSintelATE退、fullcontext去mask+posegraph非同执行免费。实际Ch25 Mem3R两完整段及前后只分pose/geometry存储，缺relative-edge producer/global融合分责；root已授两段后/ReLaGS前最小段＋本人注，稿已给，不预保存或POST。v1May26 04:03:38Z/registeredMay27 02:11:13Z合界BJT27。

### 26525 ReCA：六分标准，仅报告

本人实际v1§3–6/E/F/I/M/Q必要完整；初次parser缺段已修复后实际完整读，不冒原输出完成。冻结G、anchor/intent/generated与support/freshness均模型评分，Eq2–3明示design principle非最优求解或真值；Alg1 Refresh后Repair未再Refresh，不授修复后state原子一致。Table2 time/平均shot秒即RTF非3–5min整片，主复杂式漏DτG依赖生成下界，Q文字反侧保。二十prompt/八十video/四十六rater每cell≥3、GPT5.5外族不等GT，sequential消融非独立factorial/未匹配全call预算。hardwareprecision/API全费ND，未看视频/实现或复现。实际Ch25 581–605 persistent-state、生成geometry写回、AnyRecon原capture/derivedbank及Mem架构，复用Ch77provenance有效层：本稿是有限language-side controller提议，support/最优allocation未独立认证，不新增稳定world-state机制，故Only而非主题NC。v1May26 04:16:56Z/registeredMay27 02:11:21Z合界BJT27。

上述末批日期均实际官方abs唯一v1与精确DOI bulk arxiv.content/findable registered比对，早界May27 00Z≤晚界May27 02Z许，整个区间在BJT27；字段不是公告时刻、不证明全球首公开。26501具名AAAI早稿本人另实际打开官方37388，Published2026-03-14同题三作者完整摘要，EX-date有效。最后Source/owner普通0；余R3保存/POST与完整六节DAY、作者保存完成态后有限FINAL，不能将其预记为完成。

## R22 — R3 唯一实际 POST 与日级前机械检查

26519作者保存后，本人一次实际完整新增、Mem3R前两完整段、后ReLaGS两完整段与本人note读回；采用分责与全费/反侧正确，限定cached/unstaged diff-check通过，唯一实际POST通过并释放root所授指定窄位。净22项实际新整合、13唯一owner，普通Source/Books/POST剩0。本人注后续只同步既成事实，不开重复行政复核。

日级进行中快照实测：原118候选完整行各一次且原序prefix同，原小时窗口同，连续原§4含尾换行135703bytes完整存在（剥尾口径135698非证据丢失），当前185候选。V3实际通过，493本地引用无缺失，限定报告/本人SUP两层diff-check通过。本人已实际顺读当前§1–2、67新§4全部及§5–6，§3新67行也已分段完整读；发现三项末尾table分隔和§6字面换行、过期普通待办/引用计数，已交作者修。旧118与旧§4未变化的有效证据及旧独核仅按合同复用，不当本次新扫描或新的正面保证。完整六部分最终同步后才授DAY；本节未提前授完成态。

## R23 — 2026-10-21 14:34+08 实际完整六部分 DAY 通过

复核者：独立非writer `/root/supp_may28_reader`。结论：本日完整六部分DAY通过；尚需作者保存完成字段后有限FINAL读回，不预支该保存事实。

本人实际完整检查本轮六部分及相互衔接：§1 67新家族/原118合185与原835历史范围明确；§2每日十四源实际入口/主题/停止位置、可用恢复与外部子层；§3全部67新增逐项贡献/日期/评分/深度/Books处置，并机械确认原118完整行/日期评分/原序各一次冻结；§4全部新增67项采用命题/精确v1/必要current变化/直接反侧/具体owner及22真实POST，连续旧§4原块不变的有效层复用；§5十二资格、六中心争议、历史来源子层及窗外早正文去重的精确隔离/重开条件；§6独立身份、全拟入选与分层排除的实际复核范围和未检查范围。先前进行中普通层已逐项实际闭合，不改称外部，未再扩发现或全附件审阅。

准入复核覆盖所有拟入选完整题摘及影响准入的必要补域，分层EX自包含22个＝3个OpenAI核心＋19个arXiv（范围/贡献/成熟组合/传统领域）；纠错/修订/具名早稿信号另处理26397与26494/26500/26503/26508/26501。522原始线索与101相关完整题摘不当候选分母或全部逐条关闭队列，没有宣称全学科召回或所有标题线索均全文复核。原118未受影响身份/版本/采用命题及原独核仅复用，不借旧完成标签免本轮验收。

最终新增处置核算67＝22整合＋10具体已有覆盖＋29仅报告＋6争议；深度27深入＋34标准＋6中心隔离。真实新增22家族、13唯一owner、23正文段（Tax两段），均本人实际新正文/完整直接邻接/本人注唯一POST有效；Forge早披露仅本轮段/注恢复实际POST通过。后发MPS必要安全纠错明确10月2日提交非公开日，其他current变化只受影响域，不倒灌May新增事件或分数。所有共享精确窄位释放。

作者已修三行末分隔、字面换行、过期待办/计数；本人又发现63个新§4链接标签中有A数字错配，作者统一仅改为准确‘实际机制/配置/直接反侧记录’，当前实际读回受影响末三全文、首批链接及公共引导，必要证据/正文未变化，未要求重做Source。当前表67行均五列，状态/处置计数一致，旧小时窗同、118整行prefix相同且各一次、连续旧§4含尾135703bytes完整，493本地引用零缺失。当前V3实跑通过，README/本人SUP限定cached与unstaged diff-check通过；机械检查不证明语义，语义依据是本日R1–23实际复核。

普通扫描/准入/Source/Books/POST剩0。十二日期资格不列本日确定候选、不评分/不进Books；六中心争议保候选/原分但不作正面证据或Books；来源历史子层不签Coverage/Evidence或无遗漏。这里只确认已处理到合同允许的安全终态，并非所有主张得到证明或所有原始来源完整恢复。请作者保存完成态并将§6记录本DAY结果；其后本人只读完成字段及实际改变的局部，做有限FINAL即交root释放，不新增行政验收轮。

## R24 — 2026-10-21 14:42+08 保存完成态有限 FINAL 实际通过并释放

本人实际读回作者保存后的README：状态‘完成’、检查时间2026-10-21T14:37:25+08:00、原小时窗及补充May27自然日保持；§1实际DAY通过与67新增处置、§5普通研究/Books无待办而十二资格/六中心/历史子层仍隔离、§6独立身份与‘结论：通过’、R23及保存态记录引用均相容。作者A26保存事实实际读回，不将其自述替代本人验证。

有限FINAL没有重做有效Source或再审全部Books。保存态V3本人实跑通过，185总/67新、旧118完整行prefix相同且各一次原序、连续旧§4含尾135703bytes完整、原窗口相同；493本地引用零缺失。报告/本人SUP限定cached和unstaged检查通过。最终67＝22实际整合/10具体已有覆盖/29仅报告/6争议；22家族13owner23段实际POST有效，Forge指定回收恢复有效。普通扫描/准入/Source/Books/POST/DAY/FINAL均0，所有指定窄位及本日reader ownership释放，直接交root接纳；不跨日、不改LS/索引/合同、不stage/commit/push，保护既有与并发修改。

十二资格、六中心争议及来源历史子层仍不获正面Coverage/Evidence/Books或无遗漏权限，重开仅按§5精确条件。此FINAL结束的是本日已保存安全终态，不宣称所有来源恢复、所有论文主张成立或实现/实验复现；无需作者再改状态或新增第三读。
