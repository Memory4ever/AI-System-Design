# Daily Research — 2025-07-01

**规范：** V3
**窗口：** 2025-06-30T09:00:00+08:00 ～ 2025-07-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T00:19:14+08:00

## 1. 结论

本窗未形成可确认公开归属的正式技术候选，**不能据此说本日零事件、零贡献或无遗漏**。arXiv 官方公开公告未恢复，提交时间、ID月份及正常release schedule不能证明本窗实际公开；多家机构历史动态目录也未恢复。它们已隔离，不支撑正面结论或Books写入。

独立重建得到的 Transition Matching（TM）、L0 及 ERNIE 4.5 有具体潜在机制线索，但不伪作本窗候选。TM/L0已通过首批准入校准并保存必要核心及反证，未因日期障碍改成无贡献；ERNIE官方Blog元数据折算北京时间为6月30日08:00，窗外，仓库内文档commit不能替代release首公开正文。其他可能相关、负面、安全及评价反证线索见[本日筛选记录](../_sources/daily-20250701/SCREENING.md)。

arXiv三组收窄短语查询在**最近提交**6月30日～7月1日得到102/13/20条，跨查询归并119个ID，包含旧版本及窗外线索；不是119篇当日论文或119项已审阅。追加的有界Agent、GPU、World Model/VLA、训练主题查询以及宽标题查漏保留实际停止范围，不把全分类/166项架构搜索变成队列。本窗确认落窗且通过贡献筛选的唯一家族为0，正式候选审阅完成0；已读核心仅是日期隔离恢复资料，未计入完成分母。

Books纳入判断：没有日期及独立证据许可的当窗材料，故未修改Books，也未宣称已有覆盖。root独立DAY已通过本日隔离处置与实际检查范围，作者可执行的本日工作已收束，状态为完成（含明确外部保留项的安全终态）。这不是全部潜在材料贡献/全文已经验明，也不是所有来源无遗漏通过。外部保留项不通过扩大窗口或不断重试消除。

## 2. 来源覆盖

原始响应、请求时间、错误及阅读副本保存在[同日来源目录](../_sources/daily-20250701/SCREENING.md)。结果描述只覆盖实际入口，机构Blog不等于所有研究与artifact的完备清单。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research入口403；官方RSS完整1247项，最旧2015-12-11、最新2026-10-05，按UTC精确过滤本窗；唯一条目Economic Blueprint，BJT6/30 15:00，政策标题明确范围外关闭；openai-rss.raw | 已检查 | RSS以外Research材料历史覆盖不能保证；入口403保留 |
| SRC-ANTHROPIC | Research当前10项仅2026；同日官方站限定搜索未恢复历史研究段；官方Opus3退役日期通知仅生命周期上下文，无新模型机制/接口约束 | 受阻 | 目标窗口Research历史列表未恢复，不把搜索无命中记成无事件 |
| SRC-GOOGLE-AI | pubs超时；官方2025/06 Blog通过web读该月9篇，6/30 HOV-specific ETAs明确地图应用关闭，6/27及更早窗外；DeepMind首入口TLS失败，web当前Blog未恢复2025历史段 | 受阻 | Blog部分已处理，但papers目录与DeepMind本窗历史研究无法覆盖 |
| SRC-META-AI | Research连接重置；官方同日站搜返回2021同名日期和当前分类页，未恢复目标段 | 受阻 | 本窗官方历史研究目录缺失；不据搜索结果宣称0事件 |
| SRC-QWEN | 官方Blog page1→page2已跨过目标，7/22Coder→6/27TTS→6/26VLo→6/5Embedding；qwen-page2.raw | 已检查 | 仅所读Blog没有本窗条目，不能保证组织全部artifact |
| SRC-DEEPSEEK | 官方主页及完整API updates；2025-05-28之后下一事件2025-08-21，deepseek-updates.raw | 已检查 | changelog所列范围无本窗事件，不声称未列研究均已覆盖 |
| SRC-MOONSHOT | 官方Kimi Blog年代跨过7/11K2→5/6LongThinking，kimi.raw | 已检查 | 仅Blog历史列举范围；未把组织全部commit变成发现队列 |
| SRC-TENCENT-HUNYUAN | 首查Research动态壳，浏览器定点恢复超时；root提供已知API后一次POST publicList，pageNum1/pageSize100/renderType0，code0/totalNum9，9项时间均2026；hunyuan-public-list.raw | 受阻 | API成功但历史2025“全部”目录/快照仍未得；不以当前9项推断2025无事件 |
| SRC-ZAI | 官方Research及?page=2实际止于2025-12，未恢复7月；zai*.raw | 受阻 | 目标段动态论文目录缺失，不将当前目录充作历史 |
| SRC-BYTEDANCE-SEED | 网页page1后按已知API恢复publish_year2025：papers type1 tokens0→20→40→60→80，total94/末页has_more=false，但仅20返回SwiftSpec(6/12BJT)，其余缺条目；Blog type2 tokens0→20已跨7/14→6/28，40亦返回至has_more=false，total49而实际41项；seed-*-2025-*原件 | 受阻 | API目录数与实际payload不一致，papers目标段仍缺；可见Blog无目标条目但不证明缺失项无事件，不宣称94项论文已读 |
| SRC-BAIDU-ERNIE | Blog第2页含4.5正文，核心已读；published_time/datePublished均2025-06-30T00:00:00Z，即BJT08:00窗外。目标repo窗口15次多为文档/typo/link commit | 受阻 | 异构MoE潜在贡献保留，但未证实新的窗内release正文；不把commit当首公开 |
| SRC-XIAOMI-MIMO | 官方主页Paper/Blog年代跨过2025-09/10→6/4→5/12，mimo.raw | 已检查 | 仅主页列举范围没有目标事件，不等于所有未列artifact无变化 |
| SRC-MINIMAX | 官方Blog当前12项止于2025-10；?page=2返回同12项，未有效历史翻页；minimax*.raw | 受阻 | 本窗历史目录缺失；不得把重复首页称作第2页已读 |
| SRC-ARXIV | 收窄短语、Agent/GPU/训练/World Model主题及相关标题查漏，查询完整参数/停止点见SCREENING；初始不带引号过宽查询已纠正；宽architecture166项非逐摘要队列，CL/LG月列表部分响应 | 受阻 | 查询只给提交窗口，实际公开公告/精确重要修订事件缺失；API空响应及schedule不能填补。线索整体隔离，不证明召回完整 |

未扫描每周来源。没有触发会议新批次、协议发布或benchmark suite变化的按需发现扫描；未因关键词或L0实现引用增设全站release队列。

## 3. 候选与判断

没有已确认完全落窗且通过贡献筛选的正式候选。日期不明但潜在贡献仍须判断的材料留在第5节及[原始筛选记录](../_sources/daily-20250701/SCREENING.md)，不先评分、不给审阅完成或Books已有覆盖标签。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

本节只说明**不采用边界**和保留的已读证据，不是隔离项转正或完成审阅声明。

### [Transition Matching: Scalable and Flexible Generative Modeling — v1](https://arxiv.org/abs/2506.23589v1)

精确v1题摘及核心方法/实验原件分别为abs-tm-v1、tm-core-full。v1提交字段`Mon, 30 Jun 2025 07:51:58 UTC`不能当公开时间。HTML曾部分传输，已读§2转移kernel、§3三种因子分解、§4可比实验、§5及相关采样附录，不声称完整附件审读。

潜在增量不是换名Flow Matching：离散时间、连续状态的随机transition kernels容许非连续监督，DTM/ARTM/FHTM改变条件分解。已读反证同时限制采用：backbone NFE未计flow head；ARTM/FHTM有T×image-token的backbone代价，不能把DTM采样收益外推因果模型；text/image统一集成仍是未来方向。没有采用论文性能数字或生产能力保证。

预期owner为`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。日期隔离后停止Books正文比较；尚未确认现有具体论点差额，不能声称“已有覆盖”或“需要整合”。恢复日期后定点比较监督过程/transition因子分解与因果质量—采样代价，不扩读无关附件。

### [L0: Reinforcement Learning to Become General Agents — v1](https://arxiv.org/abs/2506.23667v1)

v1题摘和完整HTML核心保留为abs-l0-v1、l0-core。提交字段`Mon, 30 Jun 2025 09:44:32 UTC`不是公开时刻。§2 REPL持久状态、§3训练action/return/reward与worker pool、§4评价和难度/动态采样分析已读。

收窄FIRST主张：worker pool、Python REPL、CPU/GPU分离、Bubblewrap自身是成熟组件，无受控throughput评价，不能据此声称新增可扩展机制。可核验的训练线索是token action、discounted step return与严格on-policy学习的连接，以及难任务中格式/执行reward崩溃和动态采样缓解；并非GRPO组baseline。代码运行reward不是语义正确/安全保证，SimpleQA从30到80的单个数字不独立证明增量，也不外推开放环境可靠性。不得误写为“移除执行reward导致崩溃”的未做消融。

拟按命题分别路由`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)的代码状态/执行边界、`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)的reward/credit assignment；不以系统包含RL将其误归`TRAIN-GRPO`。现有正文具体差额未比，日期确认前不改Books、不作已有覆盖结论。

### [ERNIE 4.5 官方正文](https://ernie.baidu.com/blog/zh/posts/ernie4.5/)

核心描述shared/modality-specific异构MoE，以及语言→多模态continued pretraining；47%MFU缺必要运行配置，未采纳。正文日期及UTC午夜metadata折算BJT08:00落在窗外，不能仅因同为“6月30日”归入本窗。窗口内文档链接修改未建立新的模型机制公开事件。拟owner为`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)，跨模态语义交接`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；这只是恢复路由，不是知识整合成果。

TM/L0所读精确v1页面、ERNIE所读Blog正文未见可见撤回/勘误标记；MAPF的精确v1页亦作相同轻核。这不是完整current事件史或全部版本的撤回检查。其他日期隔离线索不沿摘要构造Books论点，不采用性能/安全宣传。

## 5. 缺口与下一步

尚可执行工作：无。root独立DAY复核及反馈修正已经完成；下列外部保留项等待明确恢复材料，不是普通未完成审阅队列。

以下为本窗终态保留项（外部）；**不支持正面证据、候选、Books、无遗漏断言或性能/安全保证**。不是等待用户催促继续抓取全文的普通待办。每项只请求一次，材料到达只重开受影响家族/来源：

| 保留项身份 | 缺少什么、为何必要、已做尝试 | 可接受材料及定点重开位置 |
| --- | --- | --- |
| TM 2506.23589、L0 2506.23667及SCREENING列明的arXiv潜在贡献/安全/负面/重要修订线索集合 | 官方首次公开公告/本窗重要修订身份；提交字段、最近提交查询、月份列表、正常schedule无法证实实际落窗。API空/部分列表/advanced年月粒度不能补造公开小时 | 覆盖本窗的官方历史公告/邮件，或作者首次公开全文及可信时间记录；先确定对应ID/精确版本事件完全落窗，再重开准入、当前纠错撤回轻核和必要证据，不用现有Books主题替代日期 |
| ERNIE4.5 Blog/release家族 | 目前正文metadata支持BJT6/30 08:00窗外，日期字段可能只是标称午夜；文档commit不能证明窗内新release正文首次公开 | 作者可核验初次公开release正文与时区/时刻，或真实新机制artifact事件；若证据确定仍为窗外，只留真实归属线索，不重评分本日 |
| Anthropic、Meta历史Research；Google papers/DeepMind；Hunyuan“全部”、Z.ai/Seed/MiniMax目标段目录 | 主入口访问失败或当前分页未到2025目标段，各已作一次定点恢复并记录停点；不可从未恢复目录推零命中 | 对应机构本窗官方研究清单/历史快照及相关原文，或精确官方发布链接加可信时间。仅重开该来源/该材料，不遍历机构全部历年论文 |

窗外线索：ERNIE官方Blog元数据BJT6月30日08:00早于本窗；相关arXiv命中包含旧家族后续提交及7月ID，未核验它们实际归属，不称为已审重复。恢复时只处理真实受影响日期，不自动扩大本窗、创建Weekly或开始另一日。

## 6. 复核

复核者：root（独立于作者jul01_author）。

结论：通过

通过的是本日隔离处置与实际检查范围的安全终态，不等于全部潜在家族贡献/全文已经验明。

FIRST实际范围：TM/L0精确v1完整题摘及MAPF关闭原件，root独立确认TM潜在机制准入、L0保留潜在贡献但须核实际增量、MAPF领域solver关闭成立；ERNIE日期隔离方向已确认。后续作者核心阅读收窄了TM因果/cache/成本主张及L0成熟组件、on-policy与失败条件；这些仅保留为恢复资料，不成为本窗正面采用，不把FIRST外推为全文证实。

共同理由纠偏：root已完整题摘核查SG-LDM/PGOV3D，指出原保留理由将局部任务方法泛化成通用术语。作者只复查受影响VLM方法集合，SG-LDM/PGOV3D及LaZSL按实际增量关闭；VisTex和Deepbench分别改为具体native-text-space视觉提示替代设计、架构/variant在部署域扰动下的评价边界，不以“能映射章节”留池。Radioactive Watermarks的DM/IAR训练后水印行为差异仍为安全机制线索。原判断和改判原因保留在SCREENING，不因数量或审阅成本收缩。来源预检另指出Seed已知API可定点恢复，作者已按实际next token有限恢复到停止点；返回metadata/payload不一致不伪作成功覆盖。Hunyuan已知POST原始入口也已恢复，仅返回2026，历史缺口仍明确。

DAY实际范围：root检查六部分、14个每日来源、窗口/日期隔离、实际查询及月列表停止范围、Seed/Hunyuan API定点恢复原件、相对章节路径和Books实际零写入；确认正式拟选0，日期保留没有计入候选/评分/审阅完成。

独立完整题摘范围共18个不同ID：FIRST的TM/L0/MAPF；VLM理由校准SG-LDM、PGOV3D、VisTex、LaZSL、Domain Robustness；安全/反证层的Radioactive Watermarks、Multi-Agent Defences、Autonomy Security Survey、Hate Speech Prompt、Protocol Exploits、Interlocutor Awareness、MetaCipher、CaPT、IMPACT、GPAI Standards。检查后局部VLM三项改判原因保留，其他日期hold未用于正面采用。MAPF、局部VLM改判与GPAI Standards分别覆盖领域solver、表示/任务模块和风险标准映射的关闭理由样本；安全和负面信号没有因复现/局部实验一律排除。

未检查范围：其余筛选记录没有逐篇独立题摘复核，不把18项校准样本称为全部命中验明；潜在家族的缺失公告、未采用命题的全文/实现/复现及现有Books正文差额亦未获验证。恢复材料到达后仍须对应精确事件、准入与必要证据复核；当前通过的是隔离、不采用及边界处理。Books没有实际写入，不宣称正面整合或已有覆盖。

机器校验：`python3 scripts/validate_research.py --report papers/2025/07/01/README.md`通过（1份V3），`git diff --check`与本日链接/工作树范围检查通过。检查只证明格式/引用一致性，不替代独立语义验收。未stage、commit、push；共享Books、索引与LEARNING_STATE未由作者修改。
