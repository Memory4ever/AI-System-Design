# 2026-04-27 来源遗漏补充（唯一工作记录）

作者：supp_apr27_author_fresh。执行日2026-10-16；只补北京时间2026-04-26完整自然日。遵守用户保留旧候选整行、日期、评分、原小时窗口和连续原§4的授权，不改变旧46项归属，不生成Weekly，不写LS/index，不stage、commit、push。root协调非作者复核与共享Books窄位置。

## A1 范围、冻结与有效层复用

启动时实际README为46候选，不采用委派提示中的7项作为分母。README全文SHA256 `8b82a4eaacff02101751d52fc08def90d651669b549ef231f724ed4992a3127b`；原§4（从标题后的换行到§5前）18,862字符，SHA256 `2d4ba94569513e9e62271cca93dd28a48319c2bee50e147ac05364b74daaab18`。不覆盖任何旧档案。独立恢复时完整重读AGENTS、CODEX_RESEARCH_PROMPT、RESEARCH/REPORT合同、RESEARCH_SOURCES使用说明/14个Daily/arXiv主线、ROADMAP和LS最新路由；未继承别日候选池。技能发现用于范围/验证纪律，Git技能不覆盖用户禁止提交授权。

旧46项及原§4的单篇身份、命题和对应非作者审阅/实际POST无本轮新反例，按研究合同§7复用原V3_EVIDENCE_REVIEW、V3_ROOT_DAILY_GATE及其引用的具名单篇层，不以旧完成标签替代证据。此次差额仅自然日与原09点窗的差集，及新获得的具体官方材料。原arXiv批次属Apr27北京，保留不搬移到Apr26。

## A2 首批准入及代表EX校准

拟入选：官方[Seed Research](https://seed.bytedance.com/en/research)卡片及[独立论文页](https://seed.bytedance.com/en/public_papers/megascale-omni-a-hyper-scale-workload-resilient-system-for-multimodal-llm-training-in-production)均显示2026-04-26；本轮已实际完整读题摘。准入链：静态耦合encoder/LLM资源与并行在动态模态配比/样本长度下失配 → 独立并行、统一anchor/joint pipeline及分组重排/reshard → 重新考虑固定encoder首stage或静态disaggregation布局。2+2+2=6；不是因机构、规模数字或Books主题关联准入。

root在通信中实际重开官方页并读完整AB，确认自然日事件与准入/6分必要深入投入通过；并明确May arXiv不得反填April正文/实现/性能可得性。此处只记录已经发生的有限校准，不授日级完成。

代表EX：[MiniMax CLI v1.0.12](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.12)原始`published_at=2026-04-26T01:40:29Z`；本轮官方Releases API有效响应28项，再核唯一Apr20～May1事件。HTTPS下载、失败重试、base64响应、输出路径和I2V参数补丁，无新增模型/Agent长期机制；旧定点PR#94核心判断有效复用。root有限校准通过。安全/兼容性若有实质新信号才重开受影响core，不逐普通PR。

## A3 MegaScale-Omni 必要Source与版本边界

家族：官网Apr26论文摘要事件；当前download链接为[arXiv:2605.08962v1](https://arxiv.org/html/2605.08962v1)，abs显示Submitted May9，只有一个v1；官网日期不能证明此May稿当时已公开。官方API `get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20`，`x-tt-locale: US`，本轮200/total246，条目原字段`PublishDate=2026-04-25T16:00Z`对应北京Apr26；邻界Apr30→Apr26→Apr23。API显示日期只是官网归档日期，不能据该数值杜撰精确首公开时刻。

本轮以当前可复查的May exact-v1审阅技术内容，而不倒填April的逐段版本史。已有May12单项证据只用于同族身份/必要命题路由，不重做该日或移动其记录；旧`V3_AUTHOR_EVIDENCE_REVIEWS.json`误把§8标Discussion（实际Related Work），不沿用这个定位。正文已实际核§2.3、§3～5和§7.1～7.4中下列必要内容：

- §4.1.1/Fig7：每microbatch按长度阈值η本地分短DP与长Ulysses SP，时间切换共享encoder参数布局（或ZeRO2/3），免额外模型reshard不等于免SP all-to-all；短输入常驻SP会欠利用。§4.1.2/Fig8：encoder与LLM网格解耦，通信密集组放节点内，异构模态encoder在各LLM stage同质分配，非任意模态随意分stage。
- §4.2/Fig9：EncoderAnchor把挂载位置与microbatch数据流映射分离，映射显式含PP rank和相邻LLM microbatch；仍须满足encoder output先于对应LLM forward等依赖。这是runtime representation，不是sample资格或loss变更。
- §4.3/Fig10：过度塞bubble会给后stage更多encoder microbatch；编码延迟变化按microbatch数比放大，破坏原pipeline排列。方案在hybrid packing令LLM长度相对稳定、encoder已平衡的条件下均匀插入；按需靠近消费点产生encoder activation、及早backward/reclaim，避免全部encoder forward预计算造成GPU/host驻留。均匀不是自动死锁自由证明。
- §5.1/Fig11与§7.3/Fig20：分散loader避免中央I/O瓶颈，但全局重排要跨节点/机架通信；组内扩大选择空间是通信/host缓冲/收益折中，size128例all-to-all 738ms，收益边际递减，不是组越大越好。
- §5.2/Fig12：reshard须兼顾encoder输出、LLM的Ulysses/CP不同布局。不能把uniform sequence shards视为天然均衡；论文的CP路径含intra-sample sharding及回收buffer的all-reduce，不把两种通信路径混为同一all-to-all。

评价限定：§7.1 Table1/§7.2 Figs13～17，Cluster-A 512GPU、每节点8GPU/NVLink、1.8TB RAM、88vCPU、8×400Gbps IB；具体GPU型号、precision未披露。ViT1B/2.4B/10B与LLaMA12B/70B、GPT175B，batch32/64/128/256、主序长16K/8K，额外16/32K，OpenImages/RefCOCOg+私有BytedLong；三模态另USM。基线Megatron-LM、作者实现的Megatron-Dist、AutoParallel/Alpa Flax及Optimus，各workload调参；实现差异与开放代码不全使对照不是同一实现的纯机制随机实验。throughput是tokens/s，不是同质量time-to-target；SLO/concurrency不适用训练吞吐，训练质量匹配证据未作为本文收益保证。Cluster-B千卡规格隐去，不由“production”称独立验收。

反证/代价：§7.2末stage因colocation比Megatron-LM/Dist更占内存；§7.3联合去除multiplexing/WL-balance的消融支持组合贡献而非隔离每一细节的普适因果；§7.4实报59次restart、ViT loss spike需人工重启等运营问题，不能称消除了故障/质量退化。作者报告的1.27～7.57×是这些配置下的端到端step吞吐，不推广为任何模型/硬件/所有精度的保证；本轮不复现、不核私有实现。

## A4 具体owner差额与最小逐字PRE（未获lease不写）

已加载Books完整方法上下文；owner为TRAIN-DISTRIBUTED-TRAINING/Ch36。实际Ch36:1763现有段已写modality-aware packing、encoder/LLM placement与动态负载反馈，但未解释“插入位置与样本流分离→均匀插入为何抵抗编码延迟漂移→按需产生activation”的条件链。紧邻后文2603.25120的两个网格/估时重排/边界gather-scatter也不拥有这个pipeline不变量。不是按主题重复追加论文摘要。拟仅在现有SF-2026-ARXIV-2605-08962段后、该marker之前增补下面两段，保留原段与后续Chronus边界，不改Ch38 general pipeline owner：

> 两侧共享GPU时，执行计划还要把“encoder插在何处”与“它为哪个microbatch产生数据”分开：挂载点可以复用既有LLM pipeline代码，样本到PP rank及前后LLM microbatch的映射则显式维持数据依赖。若仅为填当前bubble而给后面的stage安排更多encoder工作，编码负载增长会按各stage的microbatch数差异放大延迟，原先贴合的pipeline反而错位。均匀插入的成立条件是hybrid packing使LLM阶段耗时相对稳定，且encoder侧已经负载均衡；它不是任意调度的死锁自由保证。
>
> 把所有encoder forward提前算完可简化后续LLM依赖，却增加GPU或host上的activation驻留，也放弃细粒度重叠。另一分支在消费点前按需编码，并在反向后尽早回收；与此同时，loader只在有界分组内重排以控制跨节点样本搬运。扩大组虽增加均衡空间，也增加通信、缓冲和等待，不能以更高平均吞吐保证尾部、训练质量或故障安全。负载稳定、收益不足或依赖映射难以校验时，固定布局与保守schedule仍应共存。[必要机制与反向条件](https://arxiv.org/html/2605.08962v1)见§4.2～5.1、§7.2～7.4；这是当前可复查May版本的技术证据，不宣称其全文在官网Apr26摘要发布时已可得。

当前状态：必要Source/owner/PRE待root独立核与窄lease；没有实际Books新增、没有POST或DAY。

## A5 14个Daily来源的补充自然日有界收口

检查北京时间2026-04-26全天；API检索边界UTC Apr25T16Z～Apr26T16Z仅为查询参数，落窗按官方公开日期，不以Submitted/Updated、仓库commit日期替代发布。当前执行至04:08+08；下列复用指原V3_SOURCE_DISCOVERY明确保存的原始层，非旧完成标签。未扫描Weekly组，EuroSys关联DOI仅为MegaScale身份/版本定点，不扩大会论文集。

| 来源 | 实际入口、停止范围与复用 | 本轮结果及剩余限制 |
| --- | --- | --- |
| SRC-OPENAI | 本轮原始[News RSS](https://openai.com/news/rss.xml)200、1294 items，邻界Apr25T00Z Modeling an AI jobs transition→Apr26T16Z Our principles→Apr27T00Z Symphony/Choco；Research Index本轮首屏Oct7→Sep10、Load more，原V3无法回溯April层仍有效 | 自然日RSS无窗内项；Our principles为Apr27北京，旧候选Symphony保持Apr27。Research历史分页必要入口仍受阻，不把News代替Research或称零研究。 |
| SRC-ANTHROPIC | 本轮Research HTML 200并核原始publishedOn；Apr22T14:27:03.434Z→Apr29T20:26Z的目录邻界 | 该Research列表无Apr26项，已检查；不代替作者论文。 |
| SRC-GOOGLE-AI | 本轮Google Research April Blog九项、Apr22→Apr29；DeepMind Publications265个精选、首屏已含May6→Apr25→Apr23邻界。Google Pubs本轮可见2026年413项但无逐日上架字段 | Blog/DeepMind可见层阴性已检查；Google Publications与非精选历史缺少可按日归属证据，受阻隔离。不是把413项变队列。 |
| SRC-META-AI | 原V3实际读的Publications近期段May4→Apr16→Apr14/Blog Apr8→Jun29，可复用自然日邻界。当前page2已变为Oct→Jul并混旧年，page3网页超时、原站fetch failed，不能拿当前页覆盖April | 原近期段对Apr26有界阴性有效复用；Research/Projects未可回溯层继续受阻，当前失败不记零，不扩成整站逐项队列。 |
| SRC-QWEN | 本轮动态API40项Apr22T10+08→Apr28T10+08；静态research-list最大2025-12-23。qwen-code Releases每页100，p2从Jul24到Apr8含v0.15.3 Apr26T06:49:56Z；p3已到Apr7为停止邻界 | 研究列表无Apr26项。v0.15.3是旧已审事件，不重复计候选/评分；关键rewind/exit cleanup/hot-path局部实现理由复用。Apr27 nightly不搬入Apr26。 |
| SRC-DEEPSEEK | 本轮官方News Apr24→Sep10、Research Feb25→Jun24 | 两个可见目录无Apr26独立事件；V4 Preview保持Apr24，不以PDF内印April27造首发。 |
| SRC-MOONSHOT | 本轮Kimi Blog仍旧首页；kimi-cli Releases官方API100项，Apr24 1.39.0→Apr28 1.40.0 | 该release层无Apr26项。Blog 2026历史目录不可回溯仍隔离；原组织可见层的有限结果不等于删除/非默认分支无事件。 |
| SRC-TENCENT-HUNYUAN | 本轮publicList POST page1/100、total9/list9有效响应，displayPublishTime Apr23→Apr30跨窗；`publicAt/publishedAt`另保留，不把createdAt改名发布日。原组织83仓和具名Release/Tag层沿同族日期层复用 | 官网目录无Apr26项；原当前公开仓层有界阴性不能排除删除/权限/非默认分支/站外历史，具名受阻边界保持。 |
| SRC-ZAI | 本轮Research Apr7→Apr29、release notes Apr7→Jun16，原zai-org具名7仓Release/Tag空层复用 | 两官方日期目录无Apr26项；不可回溯历史/删改权限/非默认分支仍隔离，不称组织零更新。 |
| SRC-BYTEDANCE-SEED | 本轮Research精选及Apr26独立页完整题摘；API type1 p20 total246、May1→Apr30→Apr26→Apr23→Apr22，p40已Apr13以下；type2 p0 total96、Apr23→Apr9（API为前一日16Z）；不遍历全246/96 | 新增MegaScale-Omni一个家族；原09点窗排除的官网00点归档事件因自然日补窗恢复，非否认旧时间口径。原具名repo release层对Apr26边界可复用，旧tag公开日/曾删历史仍不授覆盖。 |
| SRC-BAIDU-ERNIE | 本轮中文Blog完整可见Apr15→Apr30→May9；原PaddlePaddle/ERNIE唯一2025-06-30 release层复用 | 注册Blog及该repo release无Apr26项；不外推其它仓库/作者论文。 |
| SRC-XIAOMI-MIMO | 本轮Paper Jun29→Mar13，Blog卡片无逐篇原始日期；原组织18仓、窗前13仓当前可见Release/Tag空层复用 | Paper列表阴性已检查，Blog历史日期/删除等必要资格仍受阻；不会以旧commit日期猜Blog公开日。 |
| SRC-MINIMAX | 本轮中英Blog目录中文Apr27 Agent Team→Mar18、英文May27/26→Mar18；Agent docs索引可读但无Apr26逐篇发布日期。CLI Releases28项唯一Apr20～May1事件v1.0.12 Apr26T01:40:29Z，已读release核心说明并复用原PR#94判断 | CLI旧有效EX关闭，不重复列候选；中文Apr27与英文May27同题不在补窗。无日期旧文档/组织删改历史仍隔离；不全审普通修补。 |
| SRC-ARXIV | 本轮实际读[官方公告规则](https://info.arxiv.org/help/availability.html)：Fri/Sat ET无公告，Sunday20ET为Apr27北京08点。按ROADMAP的LLM/Transformer/多模态/训练推理/Agent主题定点查Apr26，搜索只给无关或后窗命中；cs.CL月宽列表访问失败不当零结果 | Apr26北京无常规新发/修订批次；旧46保持原日期，408宽身份线索不重做题摘队列。官方规则只支持常规批次边界，不排除站外先公开或特殊手工事件；有具名同日官方证据才定点重开。 |

来源收口：新增候选只有官网MegaScale-Omni，另两个具名release已有有效EX；未出现应新建的安全/纠错/兼容触发家族。不可回溯子入口作为终态保留项，不为候选/Books/“无遗漏”提供正面支持。恢复条件是对应官方dated archive或具名同期原始材料，只重开所指来源/家族。普通工作尚余MegaScale独核/Books/实际POST与整日复核，不冒充外部受阻。

## A6 已发生的非作者Source/PRE、窄写与格式验证

root实际打开May exact-v1完整§4.2～4.3、§5.1、§7.3～7.4，核anchor位置/数据流、平衡encoder+hybrid packing前提、按需activation、组内重排代价及restart/loader失败边界；未独核全§7.1/7.2或全部倍率，不据此验收未核性能。root实际读Ch36:1755～1777的旧MegaScale→Chronus完整局部及Ch35/37交接，确认原泛packing段缺所示链条，A4两段PRE可逐字采用，并授两段+本人注窄lease。

作者按授权已保存两段在旧08962段后/marker前，原段与Chronus未改；本人注置于既有Review notes区域。作者真实顺读当前正文1761～1780、两侧衔接与本人注，限定diff-check通过；root真实POST尚待，不自授。

必要冻结原件已保存为[baseline-before-supplement-20261016.md](baseline-before-supplement-20261016.md)，全文SHA256与A1运行前原件完全相同。旧46整行各一次，连续原§4原字节片段保留。格式初次校验暴露双来源表/双候选表被读作重复和缺少冻结档案字段；按排错技能定位现有V3支持的授权补充/冻结格式，仅合表并把旧source明细链接到baseline，未修改校验代码/候选日期或研究结论。当前`validate_research.py --report papers/2026/04/27/README.md`已通过；该结果仅结构一致性，不等Source/POST/DAY。

技能：文档技能促使约束/代价与正文相邻，不另建ADR；写作风格检索无可用工具，沿用户给定项目写作指南，不声称匹配到个人既往样本。没有stage、commit、push，未改LS/index/其它Daily，保留全部并发修改。

## A7 root真实POST通过与DAY提交

root已实际顺读Ch36:1755～1783完整两侧邻接、新两段1765/1767、旧marker及2050～2063本人注，回对已通过的逐字PRE和必要原源；限定diff-check0。root非写入者真实POST通过，窄lease释放。作者仅行政同步本人注，并实际读回同步后的正文/邻接/本人注；未扩写技术命题。

当前新增1项实际整合已完成，合47家族＝34整合/7已有覆盖/4仅报告/2旧中心争议暂缓。旧46的事件/命题/实际POST层复用，不因本轮新增重读；额外历史来源子入口安全隔离，不授无遗漏。仅余补充后的六部分DAY与完成态FINAL，已提交root，不自授。

DAY提交时再核：V3通过、42项窗口测试通过；47候选、旧46各一次与连续原§4保持；新增A7正文引用后当前110个本地引用零missing，README/SUP/baseline限定cached与unstaged diff-check通过。没有改动校验器或测试代码。

## A8 root完整六部分DAY通过与完成态保存

root非报告作者已实际完整读回六部分增量：14源/停止点、§3新增、§4必要证据及官网日期/当前版本权限分账、§5/6全部，并定点复用旧46有效层。新1项实际整合+POST落实；47＝34整合/7已有覆盖/4仅报告/2旧中心争议，无普通研究待办，外部层精确隔离。root机器再核old46每行一次/原window/连续原§4/本地引用零missing/围栏/V3与限定cached、unstaged diff0；初测误把§4标题算进连续正文导致false，去标题后literal true，并无内容损失。

据root已发生DAY通过，只行政保存README完成态/检查时间2026-10-16T04:21:40+08:00及§1/5/6和本段；不再Source或第三次DAY。旧46整行/日期/评分、原09点窗口、连续原§4及baseline保持不变。已交root最小完成态FINAL实际读回，本文不自授该FINAL；没有stage、commit、push，ownership及Books lease均释放。

## A9 完成态FINAL真实回件与ownership结束

root已实际最小读回完成态header/检查时间、§1/5/6新收尾与SUP A8；状态、新1项实际书稿/POST/DAY及47家族归并一致，普通0，外部终态权限清楚。root重跑完成态V3、限定报告cached/unstaged及Ch36 diff-check为0，完成态FINAL通过。作者仅保存此真实回件，本日ownership结束；root统一更新LS，不再Source/POST/DAY，不改其它日或index、不stage/commit/push。
