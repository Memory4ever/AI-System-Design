# Daily Research — 2026-03-12

**规范：** V3
**窗口：** 2026-03-11T09:00:00+08:00 ～ 2026-03-12T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T00:56:56+08:00

## 1. 结论

本窗确定2个唯一家族，均完成必要深入审阅与实际Books窄整合，root非作者必要源及两处实际写后复核通过：容器外domain-scoped凭据注入把观察与用密分离；endpoint collective offload与compute/communication同图编排是不同于fabric reduction的执行分支。两者只采用厂商实际披露，不认证通用安全、生产GenAI或matched吞吐。

14Daily与真实OpenReview触发处理到有限停止或具名外部终态。16个arXiv潜在线索因first-public不能完全落窗而隔离，不评分、不计当窗候选/Evidence/Books，不扩成全文队列；撤回及安全负侧另行核实。旧196160字节报告保存在[旧原文](../_sources/daily-20260312/V3_LEGACY_REPORT.md)，SHA256与HEAD一致；不继承33/551分母或旧完成标签。宽raw526与相关题名不是全部已筛/关闭。root实际完整六部分及本日停点日级Gate通过，普通待办0；这是安全终态，不是所有Coverage/Evidence正面通过。

## 2. 来源覆盖

14Daily及真实触发，限定本窗；实际查询、原始字段与停止位置见[本日停点](../_sources/daily-20260312/V3_WORKING_STOPPOINT.md)。不扫Weekly，不把宽目录作为逐项关闭队列。EDT20:00对应次日BJT08:00；日程不替代具体公开批次。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research当前切片及官方RSS03/10～12，2个Mar11核心实际读；1准入/1安全specific原事件关闭，Rakuten/Wayfair原00GMT=BJT08窗外 | 已检查 | RSS不证明全站无遗漏 |
| SRC-ANTHROPIC | 当前10条及HTML March publishedOn实际字段；相邻03/06→03/13，可见切片无窗内项 | 已检查 | 不外推全机构历史 |
| SRC-GOOGLE-AI | DeepMind Blog page3有限24卡；Research March archive12卡及真实page2两卡原元数据定点复用；临床Blog完整core贡献前关闭；pubs当前655lines | 受阻 | H1 pubs本窗历史切片；fresh archivepage2访问失败不作零命中，已有两卡仅元数据复用 |
| SRC-META-AI | Research空正文；Blog page1/2可见270/308lines；MTIA Newsroom正式事件与技术core实际读，1确定家族 | 受阻 | H2 Research/Publication本窗目录，不以Blog替全部研究 |
| SRC-QWEN | fresh public retrieval40/40，display/embedded日期逐原值对读，无分页total；Feb16→Mar19，有限slice无当窗项 | 已检查 | 日期字段冲突保留，不互替firstpublic/全历史 |
| SRC-DEEPSEEK | fresh/en/news Research10与News5可见；ResearchFeb25→Jun24，NewsApr24→Sep10；Research可见已查 | 受阻 | H3 News ViewAll隐藏切片，未checkedwholeNews |
| SRC-MOONSHOT | fresh Kimi/en/blog完整可见19条，Feb09→Apr20，有限列表无当窗项 | 已检查 | 不代表所有论文/删除历史 |
| SRC-TENCENT-HUNYUAN | fresh publicList renderType0/page1/size20，total11/返回11全部metadata；displayFeb13→Apr23，当前可见无March项 | 已检查 | publishedAt/display不互替首次时间 |
| SRC-ZAI | fresh Research可见15卡，Feb21→Mar15跨窗停止，可见无当窗项 | 已检查 | 不授SeeMore未读或全机构历史保证 |
| SRC-BYTEDANCE-SEED | fresh type1/year2026升序token0/20，返回20+14/total82/next40；唯一本窗directoryday id1424 quantumwavefunction范围外；type2token0返回9/23，Feb14→Apr1 | 已检查 | metadata可能回填，不能证明论文firstpublic；未扫82年库存 |
| SRC-BAIDU-ERNIE | fresh Blog page1十卡May9→Nov2025，Feb6→Apr15跨窗，可见无当窗项 | 已检查 | 不扩大到旧2025 page2 |
| SRC-XIAOMI-MIMO | fresh主页Paper8卡Feb3→Mar13有限已查；Blog15卡无date/More | 受阻 | H4 datedBlog本窗切片 |
| SRC-MINIMAX | fresh English BlogFeb14→Mar18可见已查；中文壳；Agent TechBlog heading及真实llms48行当前文档索引 | 受阻 | H5 TechBlog本窗dated历史，不扫全部当前用户指南 |
| SRC-ARXIV | 两主题API空响应、csDC/csCL有限month两格式失败；raw前35标题与system/training/agent/multimodal各前12题名有界查漏，四官方域主题搜索；完整题摘/必要history与DataCite具体16身份，16日期线索隔离 | 受阻 | D1实际公告批次不可恢复；不是zero/全分类Coverage通过 |
| SRC-OPENREVIEW | 10088 AcceptedICLR2026实际触发：匹配官方PDF与旧匿名PDF；forumchallenge/api2空、API1明确403；只identity去重核，不扫venue | 受阻 | D2 first-public及本次实质revision未证实 |

## 3. 候选与判断

冻结2个确定家族；日期未核实的潜在线索只列§5，不先记确定候选。评分仅针对公开机制的具体Books差额，不按新品或安全原则给分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [From model to agent: Equipping Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/) | 2026-03-11T19:00:00+08:00 | 逐操作custodian交互成本→domain-scoped出口注入/placeholder→观察与用密分离的受限替代分支；2+2+3=7 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Secret-backed Operation后两段；root实际POST通过 |
| [Expanding Meta’s Custom Silicon to Power Our AI Workloads](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/) | 2026-03-11T22:00:50+08:00 | 通用endpoint/fabric分责→message-engine/near-memory卸载与共同capture→runtime融合与completion责任的替代分支；2+2+3=7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，operation/algorithm段后两段；root实际POST通过 |

## 4. 证据与知识整合

### [From model to agent: Equipping Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)

完整官方core的§Network access实际披露容器外sidecar egress proxy集中allowlist/access control、domain-scoped secret injection，model/container只见placeholder且只在approved destination注入。未披露攻击benchmark、独立实现审计或host failure contract，因此只采用观察与用密分离，不采用通用泄漏免疫或生产可靠性。现有Ch72 signed single-operation grant/custodian不等于低交互domain-bound代理分支；新增两段保留各自约束、额外代理可信面与高风险回退。redirect/token reuse/log/response是本书待验证设计推断，不记为已证实漏洞。root实际core首批准入及两段正文/SUDP/后capability、71/73交接POST通过。来源原值与安全负侧去重见[本日停点](../_sources/daily-20260312/V3_WORKING_STOPPOINT.md)。

### [Expanding Meta’s Custom Silicon to Power Our AI Workloads](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)

fresh官方HTML `article:published_time=datePublished=2026-03-11T14:00:50+00:00`与entry-date07:00:50-07一致，只确定正式公告；技术正文自身March11 day-only不拼其第一次公开。技术§MTIA300、Communication and transport、Runtime and firmware实际公开NIC chiplet/message-engine/near-memory collective，以及HCCL compute/collective kernel fusion与runtime共capture/schedule。继承300组件不当首次创新；ISCA’25原链接403未读，不外推其附件已审。广HBM/lowprecision/chiplet/software WorkloadContract已有Ch49承载，不重复写。Ch36增加endpoint替代分支，非SHARP直接演进；group/order/completion/buffer/recovery是本书设计责任推断。300R&R production、400 lab/path、450/500future及MX8→MX4峰值不可同精度比较保留，未采matched吞吐/生产GenAI保证。root必要技术core与Newsroom、差额和两段实际邻接/Ch37/49 POST均通过。

## 5. 缺口与下一步

普通待办：0。作者来源/筛选/必要证据/两处实际Books、正式同步与静态检查及root独立日级Gate已完成，不留未知全文队列。以下为本窗终态保留项，不用于正面证据、不进入Books、不支撑无遗漏或性能/安全保证；已保存原值、现有核验及定点重开条件。

D1：以下16潜在线索不能证明first-public完整落在03/11BJT09→03/12BJT09。14个WedSubmitted仅最早可能03/12BJT08，DataCite created恢复线索却全部晚于09:00，不能用DOI metadata推真实公告批次；10087/88下界可到03/11BJT08窗前。官方category month/主题API有限尝试失败后停止，不据此记零命中或删潜在贡献。[具名题摘增量、原UTC字段和当前版本边界](../_sources/daily-20260312/V3_WORKING_STOPPOINT.md#有界主题题摘与日期终态)保存如下身份：

| 日期隔离身份 | 当前实际界限 | 恢复所需 |
| --- | --- | --- |
| [10342 AgentServe](https://arxiv.org/abs/2603.10342v1)、[10353 S-HPLB](https://arxiv.org/abs/2603.10353v1) | Created03/12BJT09:59:09/09:59:25；root完整v1题摘潜在贡献已校准 | 具体官方first-announcement batch及ID membership，或作者原first-public正文带时区记录 |
| [10323 Watermarks](https://arxiv.org/abs/2603.10323v1)、[10332 Fair Reranker](https://arxiv.org/abs/2603.10332v1)、[10335 FuelGauge](https://arxiv.org/abs/2603.10335)、[10340 CGVD](https://arxiv.org/abs/2603.10340v1) | Created03/12BJT09:58:43～09:59:07；10323v1访问失败仅raw完整题摘/currentv2一致，v2窗外不回填 | 同上；10323补可访问exact-v1，不采用“所有水印”数学保证 |
| [10359 HEAL](https://arxiv.org/abs/2603.10359v1)、[10365 GAE](https://arxiv.org/abs/2603.10365v1)、[10384 TRACED](https://arxiv.org/abs/2603.10384v1)、[10391 VarianceDiffusion](https://arxiv.org/abs/2603.10391v1) | Created03/12BJT09:59:34～10:00:20；以后修订不回填本窗 | 同上；只恢复对应事实，不扩全部附件 |
| [10408 MotionForcing](https://arxiv.org/abs/2603.10408v1)、[10422 World2Act](https://arxiv.org/abs/2603.10422v1)、[10469 DepthCache](https://arxiv.org/abs/2603.10469v1)、[10535 GR3](https://arxiv.org/abs/2603.10535v1) | Created03/12BJT10:00:45～10:03:55；World2Act官方v1身份替换oldraw题摘，不继承旧判断 | 同上；不能凭单个性能数/physics或lossless声称采结论 |
| [10087 Engram-CXL](https://arxiv.org/abs/2603.10087v1)、[10088 ES-dLLM](https://arxiv.org/abs/2603.10088v1) | 早Submitted可03/11BJT08公开；Created03/12BJT09:53:12/13跨左右 | 同上，含可能更早public家族；不得用arxiv新收录重新评分 |

D2附在10088同一请求：AcceptedICLR2026触发[OpenReview O2WvMkJbws](https://openreview.net/forum?id=O2WvMkJbws)匹配PDF/匿名旧稿，但forum验证/API2空/API1实际403，first-public pdate与是否实质修订未取到。恢复官方公开note pdate/visibility或原作者带时区首公开记录后，仅作去重与归属；不扫整个venue，不把crawl年龄当日期。

H1～H5：当前无法取得本窗必要历史切片；可接受替代均是对应机构可访问的dated archive slice或具体当窗官方原发布（含日期语义），只重开被影响入口：H1 [Google pubs](https://research.google/pubs/)本窗date-filtered publications；H2 [Meta Research](https://ai.meta.com/research/)本窗research/publication目录（可见Blog1/2另有限已查）；H3 [DeepSeek News](https://www.deepseek.com/en/news/) ViewAll中March11～12隐藏News；H4 [MiMo](https://mimo.xiaomi.com/)15个无日期Blog/More的本窗dated slice；H5 [MiniMax Agent TechBlog](https://agent.minimax.io/docs/techblog)历史March11～12项，当前llms目录不是该历史证明。不是所有未知loadmore的永久gap；这些保留项不支持全机构zero。

撤回负侧：[10377当前官方v2](https://arxiv.org/abs/2603.10377)在Apr23withdrawn，author conflict说明已实际读。v1仍可访问，不把它标成正式撤回版本；本轮未见后续有效版本，家族不采用/不评分，保留原理由而非日期或访问gap。官方后续有效版本/纠错说明到达时只重开相应采用链路，不作永久学术判决。

## 6. 复核

复核者：root（独立于本日作者mar02_v3）
结论：通过

分批已通过：两个确定家族完整必要官方core、日期/准入及实际Ch72/Ch36新增和邻接；root实际对读Container Network access/SUDP/后capability与71/73交接，MTIA正式Newsroom/技术L150–152/SHARP/operation/progressfeedback与37/49交接。16日期隔离项不是root全部完整题摘/Evidence；root实际首批10342/10353完整v1題摘与history校准，其余作者有限題摘记录保留，不声称完整库存独立验证。

具名负侧独立范围：SafeURL原事件及Mar11 source/sink完整core；Google AMIE正确官方完整core（100chat/98attended/livephysician/singlearm/noefficacycontrol），10545/10971完整题摘与唯一v1identity；10377当前v2撤回/author conflict实际官方说明。以上5个具名安全/撤回/范围家族通过；其余Seed quantumwavefunction/Google flood/客户应用仅作者标题/目录分层样本，不说全篇或526全部复核。root已实际完整读取本报告六部分与81行本日停点：14源有限停止、16日期原值/重开位置、五历史切片、五负侧及两Books；最终独立日级Gate通过，普通待办0。被隔离的日期/目录限制不授Coverage/Evidence正面保证。

当前V3 validator通过（1份）；本日报所有本地链接target存在、scoped `git diff --check`通过。来源/候选状态字段和§4题名已按可判定接口整理，静态校验不替代语义。保存旧原文与HEAD hash一致；未写LS/索引/其他日期，未stage/commit/push。
