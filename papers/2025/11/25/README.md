# Daily Research — 2025-11-25

**规范：** V3
**窗口：** 2025-11-24T09:00:00+08:00 ～ 2025-11-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T17:27:00+08:00

## 1. 结论

首批准入及日级六部分已获root独立验收，具体范围见[日级复核](../_sources/daily-20251125/DAY_REVIEW.md)与[尾部复核](../_sources/daily-20251125/TAIL_INDEPENDENT_REVIEW.md)。Claude Opus 4.5官方发布为BJT11/25 03:00；effort质量/token取舍、harness环境修复和必要系统卡纠错已完成受限深入审阅，不采用厂商通用领先或安全保证。

本日有限来源检查与必要审阅已收束，普通待办0；确定落窗候选为2个家族：Opus和AMD技术报告发布公告。Opus窄差额经root独立证据/owner通过，root实际整合Ch66一段，非写入者Aristotle实际POST通过，见[单项证据/POST](../_sources/daily-20251125/OPUS_EVIDENCE_OWNER_REVIEW.md)。工具机制/OnlyReport独立通过，但19Z模型发布不足证明另一次API事件，已降为Opus关联背景，不独立计数或评分。AMD准入、日期、必要标准证据及OnlyReport均经root实际独立通过；Opus关联browser安全的准入/日期/受限深入证据/具体已有覆盖也已独立通过。Books整合家族1、仅报告1，实际共享Books修改由root完成，作者写入0。日级通过只覆盖记录的有限处置，不授外部保留项正面Coverage/Evidence。

十项潜在贡献论文及一项政治偏差数字纠错，有限原源恢复仍不能确定事件完全落窗，终态隔离，不计确定候选、正面证据或Books。已读机制与关键反证保留，不以日期hold代替贡献审阅。代表性贡献关闭见[首批校准包](../_sources/daily-20251125/FIRST_CALIBRATION.md)与[追加安全/客户案例记录](../_sources/daily-20251125/SECURITY_EVENT_CALIBRATION.md)，不是全网排除验收。

四组 arXiv 主题/提交时间发现查询实际返回109条，按论文身份去重为88个线索；关键词与可能的词干匹配不保证项目主题语义通过，它们不是全部已通过范围筛选，也不是本窗公开论文数。请求提交范围与返回published字段的权限保留，不由标题字面不匹配断言接口故障，也不把该字段当公告日期。只有具名潜在材料实际进入完整题摘判断；宽月表不转为逐篇题摘或全文队列。本报告不继承其他日报或旧Weekly的候选。

## 2. 来源覆盖

以下均是实际执行范围，不把有限搜索、空页面或当前目录等同于历史完整覆盖。原始 open/search 响应在 [raw-native-0.json](../_sources/daily-20251125/raw-native-0.json)、[raw-native-1.json](../_sources/daily-20251125/raw-native-1.json) 与本日 raw-search-0～3.json 中，查询和停止边界保留在响应及校准包中。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/官方日期检索第一页；独立GET原生RSS共1245items，XML日期过滤本窗仅JetBrains，核心L32～96贡献关闭；receipt/raw保留 | 已检查 | 当前RSS删除完整性未知；shopping/GPT5-science的00Z在起点前，不挪日期或重读窗外研究 |
| SRC-ANTHROPIC | 独立本日GET Research HTML279365bytes，JSON解码Nov25 11:05Z→Nov24 15:10Z→Nov21邻接；Opus release/card、工具关联背景、browser安全核心、political受影响更正均实际读 | 已检查 | 当前CMS非历史字节/删除保证；political纠错精确时刻隔离；browser单项独立通过不授日级 |
| SRC-GOOGLE-AI | Google Research Nov归档10日期标题Nov21→Nov4无Next；DeepMind p4/p5共48标题，只相关四项核原日期Nov18/20/11均窗外；官方本窗主题query第一页 | 受阻 | pubs年度676目录/必要日切片不可恢复，受阻隔离；博客已检查不替代pubs，月精度DeepMind列表不保证全部首次事件，不全读年表 |
| SRC-META-AI | 静态Research无内容及两条有界官方日期路径；Nov24 Conservation X/SAM3/SA-FARI核心按科学应用关闭 | 受阻 | 历史研究目标段未恢复；贡献关闭单篇不证明其他事件0，见§5精确重开 |
| SRC-QWEN | qwenlm旧页最新September；qwen.ai动态内容及本窗官方日期主题检索第一页均未恢复目标段 | 受阻 | 历史新入口缺段终态隔离，不由旧页或空结果授零研究 |
| SRC-DEEPSEEK | 官方首页、具名本窗query第一页；独立GET官方updates48079bytes，实际标题日期Dec1→Sep29且无Next | 已检查 | 只覆盖公开更新段，不保证删除库存或所有org项目release；普通issue不是研究事件 |
| SRC-MOONSHOT | 本日raw-native-1.json官方Blog实际26个带日期文章标题（链接0～25），最新Nov7/6、无Next；本窗官方/原作者项目有限发现query第一页未得具名机制release触发 | 已检查 | 另两链接26/27是用户中心/文档，不算文章；不宣称所有仓库/PR检查，只覆盖这些入口，不读窗外26篇正文 |
| SRC-TENCENT-HUNYUAN | Research 静态无内容；浏览器有限尝试超时，另一次为子线程不支持 visibility；实际 POST publicList pageNum=1/pageSize=20/renderType=0，返回 totalNum=9，均为2026博客，见 [raw](../_sources/daily-20251125/hunyuan-page1.json) | 受阻 | 博客 API 不能替代历史 Research 论文目录；保留精确外部恢复条件见§5，不重复空路径 |
| SRC-ZAI | Research首页/真实前端chunk恢复分页；本日GET ?page=2并按RSC文本字节长度跳过后JSON解码，共18个当前元记录，nextPage3/hasMorefalse；发布说明Dec8→Sep30 | 受阻 | 当前Research最早仍December，无11月旧目标段；已到实际末页，不再猜分页，不授历史0事件 |
| SRC-BYTEDANCE-SEED | 实查get_article_list_v2 type1/2、year2025/count20/page0/desc、US；各18条、total94/45、has_moretrue/next20；December pinned后非pinnedOct22/23，实际边界跨窗，停止p0。见[论文raw](../_sources/daily-20251125/seed-research-page0.json)、[博客raw](../_sources/daily-20251125/seed-papers-page0.json) | 已检查 | 当前回填/删除与早期pinned穿插限制保留；不由非置顶下界证明全年全量，不开其余年度正文队列 |
| SRC-BAIDU-ERNIE | 官方Blog第一页10日期标题Dec9→Nov21；实际page2六条Nov11→June30无Next，本窗官方query第一页 | 已检查 | 当前博客快照非全org release证明；未发生具名仓库触发，不扩窗外机制 |
| SRC-XIAOMI-MIMO | 官方八项Paper至Oct21更早，15未定日期Blog；本窗官方query第一页，More未恢复真实历史段 | 受阻 | Paper有限目录已读；Blog历史日期缺段隔离，不以15标题建全文队列 |
| SRC-MINIMAX | EN/CN Blog12/13列表December23→October27、无Next，本窗官方query；Agent导航15行后实际llms50行仅当前Code文档 | 受阻 | Blog有限段已核；Agent历史Tech目录仍缺，不把当前Code目录当2025切片 |
| SRC-ARXIV | 四组主题/提交范围请求start0/max100，实际模型30/系统7/Agent38/多模态34均少于页容量，去重88发现身份；不是88项范围筛选通过。仅具名潜在机制读exact-v1完整题摘和必要反证。cs.DC月表首50标题有界查漏、cs.CL三次有限失败后停止；query/raw及限定见[续跑日志](../_sources/daily-20251125/CONTINUATION_QUERY_LOG.md) | 已检查 | 关键词/可能词干匹配不保证主题语义；不据单题字面差异断言服务端bug，提交过滤权限不等公告日期。公告目标段/十项v1日期隔离，不由宽LG月表或失败探针授Coverage，不保证全分类召回 |
| SRC-OPENREVIEW | MURMUR触发具名forum wwXP9eqWeW和API2 notes；实际HTTP403 receipt保留，未扫描会议 | 受阻 | 本项首公开/版本必要字段不可得，只重开forum，不取消已发生触发 |
| 表外：[Anthropic Engineering](https://www.anthropic.com/engineering/advanced-tool-use) | Opus发布链接触发必要关联背景，完整核心/接口/限制已读；00Z文章字段保留，19Z不是独立工具事件证明 | 已检查 | 机制/OnlyReport独立通过；不按版本后缀补日期，不另计本窗family |
| 表外：[AMD原发布](https://newsroom.amd.com/news/amd-powers-frontier-ai-training-for-zyphra/) | 窄系统主题2511.17127v1触发；AMD与Zyphra原公告及AMD署名分发页09:01ET明确本日report release | 已检查 | 公告事件落窗，不当arXiv精确首公开；窄命题/OnlyReport独立通过，不外推全硬件定律 |
| 补检：[DataCite](https://api.datacite.org/) | 仅具名11项身份/版本/原字段恢复；四项尾部单次请求receipt保留；官方availability已实际核 | 已检查 | Submitted/Updated/created/Available权限分开；窗内上界没有首公开下界，跨截止上界亦不证明窗外 |

除具名MURMUR OpenReview外，没有已识别的清单按需批次/项目触发；未触发不等所有项目无release。没有扫描Weekly来源。新增raw12～24和原生HTML的真实请求/停止范围见续跑日志。

## 3. 候选与判断

仅列确认落窗且准入、必要证据及Books处置已获独立确认的两个家族；关联背景与日期隔离不混入确定分母。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5) | 2025-11-25T03:00:00+08:00 | effort 控制下质量/token 曲线及 harness 环境修复提示应分开比较模型、计算投入与评价环境；2+2+2=6，不将成熟可比性原则计成新增基础理论 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 Resource Budget](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#resource-budget-与-persistent-identity-都属于-evaluation-identity)；root写前/证据与非写入者POST通过 |
| [Training Foundation Models on a Full-Stack AMD Platform](https://arxiv.org/abs/2511.17127v1) | 2025-11-24T22:01:00+08:00 ～ 2025-11-24T22:02:00+08:00 | 官方report发布事件；xGMI参与者数改变可用带宽，训练/推理重叠条件不同，不能把节点内高速域当任意子组一致；2+2+2=6 | 标准完成 | 仅报告：TRAIN-DISTRIBUTED-TRAINING实际约束已承载需按group/topology测量；root准入/日期/证据/处置独立通过，实际Books写入0 |

## 4. 证据与知识整合

### [Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)

已读原页完整核心说明，保存 [原页 HTML](../_sources/daily-20251125/native-opus.html) 与 [官方正文响应](../_sources/daily-20251125/raw-event-0.json)。`article:published_time`、JSON-LD `datePublished`、正文 `time` 三处均为 `2025-11-24T19:00:00.000Z`，不是 submitted 或后续索引日期。

必要证据已定点审阅，具体位置、反证和owner比较在[单项送审](../_sources/daily-20251125/OPUS_EVIDENCE_OWNER_REVIEW.md)。系统卡p9/p10的effort控制作用于多类token，图明确n=500、extended thinking off；实际token用量依任务而变，不是hard cap。release中medium少76%与high高4.3个百分点/少48%仅为此厂商工作负载结果；硬件、precision、并发、工具成本和端到端SLO未披露，不作通用费用或延迟保证。

系统卡p20明确Terminus-2/Harbor失败时对全部被测model将资源限制增至2×，infra errors由最多13%降至<1%；这改变环境条件，不是模型能力变化。p26～27的τ2升舱再改签符合字面政策却被期待拒绝的rubric判失败；不等于符合企业意图，作者亦不推荐此切片跨模型比较。p2 Nov24纠错将原public-test曲线换为semi-private结果，并纠正public train/test重划训练的说明；不因此声称半私有测试已污染。本次PDF是带Nov25/Dec5后续changelog的当前版本，不伪称Nov24逐字历史版本；具体纠错时刻未披露，不另造精确落窗纠错事件。

 Books实际context、owner及邻接比较后，评价身份、合法替代路径误拒及public/holdout隔离已有覆盖，不重复写入。root独立核必要源与窄差额后实际新增Ch66 L460：行为性投入档位、hard cap、thinking开关与实际消耗分账，旧硬限额和未测成本Unknown就近保留。非写入者Aristotle实际读新增段、原per-call预算与后persistent identity/Backend、Review notes首条及Ch65/67交接，POST通过，范围见单项文件末段。该项不是日级验收。

同family关联[browser安全事件](https://www.anthropic.com/research/prompt-injection-defenses)原published=Nov24 15:10Z完全落窗，当前modified2026不称历史字节冻结。完整核心已读：Best-of-N100每环境攻击预算、当前低ASR仍有残余风险、model RL与classifier/intervention同时变化。只保留局部反证，不作开放威胁概率或单层因果推断。Ch72实际L600与L1326～1328已承载matched/adaptive预算及checkpoint/部署防线分账，已有覆盖 `PLATFORM-SECURITY` 经root独立通过；实际复核原核心L11～45、原HTML结构化日期及Ch72 L600～631/1308～1341与Ch71/73开篇，未重读所有附件。见[具体证据/owner](../_sources/daily-20251125/SECURITY_EVENT_CALIBRATION.md)及[独立复核](../_sources/daily-20251125/SECURITY_INDEPENDENT_REVIEW.md)，实际写入0，无POST。

Opus关联工具背景：[Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use)。

原文章Nov24 00Z在窗前且自称当天发布features；19Z Opus链接与组合描述不足证明API再次发布或有新兼容差额，作者此前“now available”事件推定撤回。故仅作必要关联背景，不单独计本窗候选/评分，不重定首次公开。`defer_loading`不授权限；`allowed_callers`/caller.tool_id是代码实例而非业务授权；中间结果由代码处理、最终stdout才是observation，聚合不足时须直接调用，样例不代语义校验。未运行API/复现，不采用内部数字作通用效率保证。root实际接口及Ch78/77/79对读支持机制与OnlyReport，见[独立复核](../_sources/daily-20251125/TOOL_INDEPENDENT_REVIEW.md)。本次不再坚持独立工具事件，只有真实官方change/release与独立差额到达才定点重开，不空搜。

### [Training Foundation Models on a Full-Stack AMD Platform](https://arxiv.org/abs/2511.17127v1)

AMD署名正式分发页Nov24 09:01ET及原公告“report published today”组合支持发布事件落窗，不冒充arXiv首次公开。精确v1 §II/III-C实际支持所测MI300X节点参与者数/链路条件，不把峰值式外推任意AMD部署；§III及V必要对照已读，未采用跨vendor领先、所有模型或生产扩展保证。Muon二维限制与后文分配表述有内部不一致，邻接SendRecv亦不证明任意多rank参数的正确性，不采用这些扩张命题。Ch36通信模型和Ch37高速域条件已实际比较，建议仅报告，具体证据/反侧/停点在[系统尾部记录](../_sources/daily-20251125/SYSTEMS_CALIBRATION_TAIL.md)。

## 5. 缺口与下一步

**普通待办：0。** root已实际通过本日六部分、14每日源与触发入口、全部拟采用命题、十项潜在论文/纠错安全隔离及五个分层关闭样本，见[日级复核](../_sources/daily-20251125/DAY_REVIEW.md)。Opus窄差额、root实际写入与非写入者POST通过；AMD仅报告与browser具体已有覆盖通过；工具独立事件推定已改正。以下均为精确隔离的外部终态保留项，不再将未采用附件列为全量普通待办。作者继续fresh26，不重复本日附件。

**本窗终态外部保留，全部不支持正面候选、Books、无遗漏或性能/安全保证：**

- 历史目录：Meta/Qwen、Hunyuan Research、Z.ai Research、Google pubs、MiMo未定日期Blog、MiniMax Agent Tech的具体目标段。§2保留有限入口、次数和停止；Hunyuan blog九条2026不是Research，Z.ai已实际到page2/hasMorefalse仍只有12月以后的当前目录。重开需相应官方11/24～25旧切片、真实前端历史接口或具名本窗研究正文，不重复空浏览器/分页，不遍历其他月正文。
- [TBIK v1](https://arxiv.org/abs/2511.17826v1)：submitted Nov21 22:40Z，Updated Nov25 01:12:35Z、created03:57:35Z跨终点；作者项目Notion有限访问不可得、repo releases为空，精确公告未恢复。原贡献保留而非因跨上界关闭；重开需作者首次公开记录/官方v1公告或完全落窗范围。
- [HaNoRec v1](https://arxiv.org/abs/2511.18740v1)：submitted Nov24 04:10:46Z，Updated Nov25 02:15:23Z、created04:18:26Z跨终点；有限具名恢复无公开下界。目标式实际读Eq4～12，hardness/online-gap调整及噪声实现有具体但尚需条件限定的delta，不借DPO名字准入；重开需精确v1首次记录与相关噪声/目标一致性说明，不扩大推荐池。
- [MR-RLVR v1](https://arxiv.org/abs/2511.17473v1)：窗内metadata上界仍没有公开下界，官方/作者具名路径无公告。实际两阶段mask/position reward和小学生/teacher预算、局部失败已读；只重开本项v1公告/首次作者记录，落窗后独立审收窄命题，不把提交或2026动态HTML日期当历史public。
- [MicroMoE v1](https://arxiv.org/abs/2511.16947v1)：窗内登记上界无首公开下界，具名作者/项目恢复无公告。LP/分层placement/overlap及Zipf偏斜失败、硬件/协议对照已读；不将FSDP未来计划当实现。仅在v1实际首公开范围恢复后重开采用，不再空搜。
- [UI-CUBE v1](https://arxiv.org/abs/2511.17131v1)：窗内登记上界无下界，repo releases为空。复杂workflow相对simple的局部反证已审，harness/task/oracle差异限制保留，不采用“根本架构限制”；重开需明确v1首次公开，不扩大benchmark附件。
- [MURMUR v1](https://arxiv.org/abs/2511.17671v1)：Updated Nov25 01:03:55Z跨终点，具名OpenReview forum/API403，作者页未定日期。安全受影响§3～6已深入：黑盒user消息/完整group transcript、session APR与有限账户任务条件，不能当生产攻击概率。重开需forum首次public/version字段或官方/作者v1公告，仅这一个forum；缺口不取消安全审阅记录。
- [RynnVLA-002 v1](https://arxiv.org/abs/2511.17502v1)：登记上界窗内但无首次正文下界，repo News明确Nov10升级/代码artifact，release列表为空。旧artifact不证明论文窗外，也不冒充本窗新release；重开需本次论文首公开或本窗具体新增artifact事实，不因v2号扩附件。
- [NX-CGRA v1](https://arxiv.org/abs/2511.17235v1)、[PIKE v1](https://arxiv.org/abs/2511.16964v1)、[SparOA v1](https://arxiv.org/abs/2511.19457v1)：各完整题摘、关键方法和有限官方/作者具名日期路径已核，[尾部notes](../_sources/daily-20251125/SYSTEMS_CALIBRATION_TAIL.md)保留Updated/created原值。前两项窗内登记无下界，SparOA Nov26晚登记不证明一定晚公开；潜在局部贡献保留，不能把日期未核写成贡献0。重开仅需各exact-v1实际公告/首次记录或完全落窗范围，不扫描体系结构/全部DNN。
- [Political bias数字纠错](https://www.anthropic.com/news/political-even-handedness)：Nov13原文不重收，Nov24标签没有时区/时刻。实际受影响深读1350配对prompt/9任务、judge/思考配置、28→35的对比限制，agreement不等truth；repo releases为空/有限官方query无更正时间。重开需官方修订原记录/完全落窗范围，仅更正影响，不重读首次公开全部正文。记录见[有限安全/日期notes](../_sources/daily-20251125/BOUNDED_SECURITY_DATE_FINDINGS.md)。

窗外线索：Anthropic estimating-productivity-gains 原published Nov25 11:05Z，即BJT19:05，在本日报终点后；这里只保留身份给真实下一日fresh恢复，不提前采用其贡献，也不阻塞25。工具原文章Nov24 00Z保留窗前身份，不由19Z Opus链接重定首次公开或造第二个新工具事件。

## 6. 复核

复核者：root，非报告作者；Ch66实际写后POST由非写入者Aristotle执行。

结论：通过

root于2026-10-04T17:20:32+08:00实际通读六部分及本日必要记录，检查14到期源与OpenReview/AMD/工具背景触发、两确定家族全部拟采用命题/处置、十潜在论文与纠错安全隔离，并分层核五项关闭样本：KDR-NER、JetBrains、Protein、Conservation及购物流程。见[DAY_REVIEW](../_sources/daily-20251125/DAY_REVIEW.md)和[TAIL_INDEPENDENT_REVIEW](../_sources/daily-20251125/TAIL_INDEPENDENT_REVIEW.md)。不是109摘要或88发现标题全验，不保证所有历史目录或全网无遗漏。

单项分批复核：root独立实际核Opus current PDF p2/9/10/20/26/27/28、视觉p10与native日期，证据/owner窄差额通过并实际写入；Aristotle为非写入者，实际POST Ch66 L450～476、Review notes首条L4416及Ch65 L102～116/Ch67 L1～24，通过。作者未写共享Books。

root工具单项复核机制/OnlyReport通过，事件推定不通过，正式计数和处置已按原源反馈改正，工具只作Opus关联背景；仅定点核更改，不重复接口正文。

root AMD单项准入/日期/受限标准证据/OnlyReport实际通过，已读原公告字段并IANA转换、精确§III反侧及Ch36/35/37，见[AMD独立复核](../_sources/daily-20251125/AMD_INDEPENDENT_REVIEW.md)。上段AMD待办已解除；不采广义NVSwitch定律、SendRecv全尺寸正确性或全模型领跑，无Books写入/POST。

root browser单项准入/日期/必要受限安全深入/具体已有覆盖已通过，归Opus家族，见[安全独立复核](../_sources/daily-20251125/SECURITY_INDEPENDENT_REVIEW.md)。root实际原核心L11～45、JSON日期、Ch72/71/73对读，及JetBrains代表性贡献关闭；未验全站或所有客户附件。

root追加尾部实际范围：NX-CGRA/PIKE/SparOA完整v1题摘与有限日期隔离通过，不授全部methods/实验；political更正受影响Method/配置/Caveats/Changelog及MURMUR§4/5.3～6安全反侧限定/日期隔离通过。Google受阻与Moonshot26计数已按本日原记录修正，关键词返回语义权限已收窄；root日级Gate接受这些修正。

机器检查：完成态V3、本日Markdown本地引用/行尾空白及限定diff-check实际重跑，结果见本日CONTINUATION_QUERY_LOG末段。新增目录为untracked，不能用空git diff替代逐文件字节检查。机器通过不等语义完成；完成依据为上述独立日级复核。未stage、commit、push。
