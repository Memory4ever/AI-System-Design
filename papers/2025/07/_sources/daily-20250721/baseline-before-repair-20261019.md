# Daily Research — 2025-07-21

**规范：** V3
**窗口：** 2025-07-20T09:00:00+08:00 ～ 2025-07-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-11T17:13:38+08:00
**补充窗口：** 2025-07-20 ～ 2025-07-20
**窗口说明：** 用户授权仅补已有 Daily 的来源遗漏；原窗口、旧候选、日期、评分与有效连续 §4 冻结。新增材料只按前一完整 BJT 自然日公开日期处理，不继承小时门槛。

## 1. 结论

**2026-10-11 增量补查：非报告作者Anscombe最终DAY通过，研究普通待办0。** 运行前正文保存在 [baseline](../_sources/daily-20250721/SUP_BASELINE_README_20261011.md)，SHA-256 为 `6d0e558296d361633fb1ee7bdfbb685c090098ea515dd75062d20d7302af8e64`。正式旧候选0、原窗口/日期/评分/有效连续§4冻结；以下旧完成结论仅是历史记录，不授本轮验收。本轮完成表示处理至明确隔离保留项的安全终态，不授全部来源Coverage/Evidence、Books Integration或无遗漏。

本轮每日14来源均已实际进入有界入口并留下停止点；DeepMind/Meta历史Blog与Seed英语论文payload恢复成功，但Google Publications、Hunyuan、Z.ai、MiMo Blog及arXiv公开批次仍有具体限制。arXiv四主题的补充日**提交线索**124条、去重77家族，55个精确v1用于核身份/版本/题摘，51项保留潜在贡献、26项明确关闭。Dr. Boot的同贡献已见2024-01-09 available的UvA学位论文，排除本日首公开；其余50项公开身份/日期未定。新增确定本窗候选0，不是“本日零命中”或覆盖通过；未评分、未记为标准/深入审阅完成。

首批6个potential+3个EX已由非作者Anscombe校准，并完成全部新潜力、安全/设计反侧、分层EX/source及六部分DAY。其反馈触发LeanTree定点纠偏：分解概念继承旧工作，增量限可执行Lean4接口、metavariable coupling与kernel验证边界；另恢复三项误关闭及确认Dr. Boot窗前同贡献。新增研究没有足够日期/证据权限进入Books，本轮不写Books/index，亦不宣称已有覆盖；State仅由root同步已验收路由。明确日期/目录保留项仅按§5重开，不把它们当Evidence完成。

**原轮结论（冻结）：**

当前没有同时通过贡献准入与本窗公开日期确认的确定候选；这不是“本窗零命中”。官方 OpenAI RSS 有一项落窗的社会使命文章，按内容范围关闭。arXiv 四个有界主题查询返回184条、跨分类去重121个家族，是提交区间线索，不是121篇本窗新论文。相关或含糊标题读取完整题摘，明确科学/领域应用旁支按范围关闭；具体筛选与精确版本原件见[筛选记录](../_sources/daily-20250721/SCREENING.md)。

NABLA、DistFlow、Paper Summary Attack 的机制准入已获首批独立校准；已有部分核心证据保留，但其首次公告不能由提交史、正常公告日程或普通元数据更新字段确认。其余潜在贡献同样隔离在日期缺口，不评分、不记为候选/审阅完成、不进入 Books。机构动态目录另有明确历史覆盖缺口。因此不作“无遗漏”、日期 Gate 通过或普遍性能/安全结论。

Books 已纳入判断，本次实际改书为无：公开事件身份未定的材料不能作为本日正面证据。三个主要保留项已提出唯一 owner 与相对现有论点的待核差额（§4）；不是“已有覆盖”或整合验收。root非作者DAY已完成，纠正两项把部署/任务模块当新机制的保留理由；可执行工作已收束，外部保留项只按§5具体材料重开。本日完成的是含隔离缺口的安全终态，不是所有来源覆盖、潜在线索准入或证据均通过。

## 2. 来源覆盖

**本轮实际补查（2026-10-11）：** 每日14来源仅查补充自然日与对应主题。新增原始请求为同日目录 `SUP_*_20261011.request.json`，响应为同名 `.raw`；响应成功不等于历史覆盖。旧轮表及其原件完整保留在[baseline](../_sources/daily-20250721/SUP_BASELINE_README_20261011.md)，不再用旧完成标签授本轮覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)实际1287条，按pubDate转换BJT只查07-20；`SUP_openai_20261011.raw`。邻接07-18/07-21，不把旧窗口社会使命文章移入新增日 | 已检查 | 本日该RSS切片未见条目；不外推未收录研究 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)完整响应内177个publishedOn（含重复），读取目标邻接07-15→08-01；`SUP_anthropic_20261011.raw`。不拿图片更新日期筛选。定点Subliminal原blog日期07-22 | 已检查 | 限该研究目录；07-22 blog不是07-20正文首次公开证明 |
| SRC-GOOGLE-AI | [DeepMind实际归档第5页](https://deepmind.google/blog/page/5/)与[第6页](https://deepmind.google/blog/page/6/)读取目标July2025切片，到June/April停止；不是无效query分页。七个July事件日期均已核：IMO/Backstory Jul21、Flash-Lite Jul22、T5Gemma Jul09，`SUP_dm-*_20261011.*`；Anscombe独立原页补核[AlphaEarth Jul30](https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/)、[Aeneas Jul23](https://deepmind.google/blog/aeneas-transforms-how-historians-connect-the-past/)、[MedGemma Jul09](https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/)，依据见[独核§5](../_sources/daily-20250721/SUP_INDEPENDENT_20261011.md#5-14来源实际停止与限制)，仅日期，不追加窗外core；[Google Publications](https://research.google/pubs/)当前年度目录另查 | 受阻 | DeepMind Blog目标切片已恢复且七事件均窗外；Google Publications仍无可恢复本日公开切片，未扫全年论文 |
| SRC-META-AI | [Blog](https://ai.meta.com/blog/)实际1–4页，`SUP_meta-page{2,3,4}_20261011.*`；第4页Jul21 startup/AWS→Jun27 Seamless，再到更旧。置顶条目非单调，未凭单个旧日期提前停止；Research另查 | 已检查 | 本日Blog切片未见条目；Research当前overview不提供本日完整历史论文目录，不外推机构所有论文 |
| SRC-QWEN | [首页](https://qwenlm.github.io/)与[第2页](https://qwenlm.github.io/page/2/)实际日期切片，Jul22 coder→Jun27 TTS/Jun26 VLo后停止，`SUP_qwen*20261011.*` | 已检查 | 限官方Blog切片，不扩扫所有repo |
| SRC-DEEPSEEK | [公开changelog](https://api-docs.deepseek.com/updates)完整响应，May28→Aug21之间无Jul20条目，`SUP_deepseek_20261011.*` | 已检查 | 限官方公开更新目录 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)完整可见索引2024-05→2025-11，邻接Jul17 Playground→Aug01 Turbo，`SUP_moonshot_20261011.*` | 已检查 | 不把Jul11 K2算新增本日，不外推未登记发布 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)；两次浏览器尝试超时/不可用，原动态壳不能当读完。实际[publicList](https://api.hunyuan.tencent.com/api/blog/publicList) POST pageNum1/pageSize100/renderType0，code0/total9/list9，仅核displayPublishTime均2026；`SUP_hunyuan-public_20261011.*` | 受阻 | 当前9项无2025历史目录；不扫描其2026正文，不调用私有/admin接口 |
| SRC-ZAI | 首查[Research](https://www.zhipuai.cn/zh/research)及公开page JS，真实More设page参数；实际?page=2与3均终止在18项、最早2025-12-07并显示没有更多，`SUP_zai-page{2,3}_20261011.*` | 受阻 | 已读可访问终点，不再称More没尝试；仍无Jul2025历史切片 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)与实际公开API article_type1/publish_year2025/token0/count20/order_desc，按JS的x-tt-locale:US恢复18条payload（total94/next20/has_more），Jul21 GR-3→Jul10 CoT，到Jun26停止；`SUP_seed-papers-US_20261011.*`。Blog type2 token0/20实际15/18条到Mar12，Jul22→Jul15；`SUP_seed-blog*20261011.*` | 已检查 | 无header空payload已被纠正，不能继续当本轮阻塞。限所读英语官方目录切片与Blog；不展开94篇/全部语言或以目录日期代签论文首次公开 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)及[归档第2页](https://ernie.baidu.com/blog/zh/page/2/)实际末页6条、1/2，Aug14→Jun30跨过目标；`SUP_ernie-page2_20261011.*` | 已检查 | 限该官方技术Blog归档，不外推所有代码/论文 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)Paper8项日期含May12/Jun04/**Sep19**/Oct21等，本日无列示；Blog15项+More无目标日期。公开index/homechunk读实际route，[/blog/](https://mimo.xiaomi.com/blog/)实际为Dec16单篇MiMo-V2-Flash，不是历史索引；`SUP_mimo*20261011.*` | 受阻 | Paper切片已检查，Blog Jul2025日期/目录仍未恢复；不把单篇成功当历史分页 |
| SRC-MINIMAX | [EN Blog](https://www.minimax.io/blog)12项最早Oct27；[中文Blog](https://www.minimaxi.com/blog)实际redirect www.minimax.cn/blog，13条含Jan15 MiniMax01，其后Oct27，读可见完整页停止；`SUP_minimax-cn_20261011.*` | 已检查 | 当前中英文目录切片未列Jul20，不代表未登记/已移除历史发布；不复用无效?page=2作为读完依据 |
| SRC-ARXIV | 四个限定主题查询start0/max150、total=returned，模型42/系统22/Agent48/多模态12，124原始/77去重；**仅补充BJT日submittedDate发现**。题摘原件、55个精确v1及逐项理由见[本轮筛选](../_sources/daily-20250721/SUP_SCREENING_20261011.md)。announcement精确日查询不支持、日list400、官方日程不能确认实际批次 | 受阻 | 51潜在线索中Dr. Boot已核更早稿，其余50项缺首次公开身份/日期；提交日查询不能穷尽本日公开材料。没有用全月目录、正常日程或ID月份补造公开日 |
| SRC-OPENREVIEW | 仅LeanTree [pROVJwTb6w](https://openreview.net/forum?id=pROVJwTb6w)、Memorization [c6nqmjfG1Y](https://openreview.net/forum?id=c6nqmjfG1Y)两个具名forum及公开PDF/API身份恢复实际触发；forum/PDF challenge、作者API403，非作者读取亦未获得稿件；详[独核§6](../_sources/daily-20250721/SUP_INDEPENDENT_20261011.md#6-首公开evidence与books门) | 受阻 | 身份/版本与首次正文公开日未证，不用forum ID代签更早稿，不绕challenge、不扫会议。 |
| 表外：[UvA学位论文库](https://scripties.uba.uva.nl/search?id=record_54126) | 仅Dr. Boot record54126具名record→PDF/bundle/item实际恢复，题名/作者/AB及原公开metadata、73页旧PDF封面/摘要/§6必要片段；详[独核§8](../_sources/daily-20250721/SUP_INDEPENDENT_20261011.md#8-具名修复实际复核) | 已检查 | available原值2024-01-09T16:01:41Z足证窗前公开同贡献，不认封面/issued为首公开；未逐字比对全部版本，未扩为2023报告或新Books审阅。 |

补检仅作定点恢复：`site:research.google "July 20, 2025" ("model" OR "training" OR "inference")`、`site:hunyuan.tencent.com "2025-07-20"`、`site:mimo.xiaomi.com "2025-07-20"`、`site:minimax.io "July 20, 2025"`（2026-10-11）；未取到必要官方本日材料，MiniMax返回用户space站点而非机构原件，未采用。搜索无结果不授零命中。每周来源未扫描；OpenReview只为LeanTree/记忆测量定点身份恢复，两forum实际challenge，API403，不扫会议。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无可列为确定本窗候选的材料。下节保留既有准入/局部证据，§5列日期与来源保留项；不先评分后补日期，不把摘要读完记为标准/深入审阅完成。

**本轮新增判断：** [逐项筛选](../_sources/daily-20250721/SUP_SCREENING_20261011.md)保留51项potential及26项EX的身份/具体贡献理由。原正式候选仍为0且未修改；本轮没有按潜力倒推评分。6项首批potential（MiroMind、RTGen、LeanTree、Memorization、Web Agent IPI、Subliminal）与3项EX见[校准提案](../_sources/daily-20250721/SUP_FIRST_20261011.md)，独立反馈不等于日期/Evidence Gate通过。独立反查将14693、14833、14850从领域EX改为狭义potential；Dr. Boot原贡献已有更早公开库身份，不纳入本日。

## 4. 证据与知识整合

以下不是候选审阅完成声明；日期未定时保留已读证据，不新增全量深审队列。

### [∇NABLA v1](https://arxiv.org/html/2507.13546v1)

`core-13546-v1.raw/.txt`方法与相关实验已读：downsample Q/K用于逐head累计注意力质量阈值选择blocks，并与局部邻域联合。固定局部窗口会漏远距离关联；纯adaptive稀疏也可损伤相邻latent边界，因此不能将减少attention FLOPs等同于保质加速。§4 Tables1–3限Wan2.1 T2V14B、720p、4×H100、PyTorch2.7/FlexAttention及作者质量协议；推理约2.7×不迁移为训练普遍值，作者2B DiT阶段训练对照约1.46×。未复现、未核生产执行，训练/蒸馏预算不得由推理速度代签。

待核 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS`，即[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。现有SparVAR/ToProVAR论点分开尺度坐标、稀疏proxy与质量/净预算；潜在差额是视频DiT中的**动态长程块选择与固定邻域必须互补**，不是重复“稀疏有成本”。由于日期未核，不采用该差额、不写书，也不声称全章已有覆盖。

### [DistFlow v1](https://arxiv.org/html/2507.13833v1)

完整精确v1题摘与HTML已保存，核心证据未读到标准审阅完成。首批准入聚焦hybrid RL框架中央数据流/执行控制瓶颈→worker侧分散数据与调度，不按v1摘要“7×”准入；当前API v4题摘不同，不能用后版性能回填v1。

待核 owner 为 `TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。现有正文已区分rollout/learner、policy identity、状态传递与控制面职责；潜在差额是中心协调器同时承担数据搬运与execution dispatch时的瓶颈分解与替代拓扑，需可比端到端证据才能判断。日期缺口先隔离，未据此改变现有论点。

### [Paper Summary Attack v1](https://arxiv.org/html/2507.13474v1)

完整题摘及方法核心已读（`core-13474-v1.*`），未把全部安全实验标为完成。论文摘要/学术权威包装能改变拒答行为是潜在反证；它不授权复用攻击payload，也不证明所有安全论文或任意模型都会被越狱。attack/defense framing、受测模型与作者ASR协议必须分别验收，当前不照录ASR作普遍安全结论。

待核 owner 为 `PLATFORM-SECURITY`，[Ch72“谁获得了行为控制权”](../../../../books/part-06-ai-infrastructure/72-security.md)。现有正文区分外部文本、runtime influence、source authority和最终effect；潜在差额只是**安全研究自身的学术包装也能成为拒答失效切片**，不是新增授权原理。日期未核且实验未读足，不以该反证宣称整合或已有覆盖。

### [CogniQ-H v1](https://arxiv.org/html/2507.13710v1)

精确v1不是当前API改名后的SoftPipe。为判断准入定点读公式与§4/§5.3：LLM prior×exp(Q/LTR)的软策略保留全部operator支持域，原文保证依赖prior严格非零且值有限；错误prior可把好动作概率压到近零，正概率不证明有限预算能恢复。Table3组合消融显示18个OpenML数据集平均指标差异，不独立证明任意坏prior都能纠正。保留为**模型prior作为探索建议而非硬剪枝的适用条件**线索，不仅因为HRL/Bayes术语或数据准备成绩；日期未核不评分、不采用。后续恢复若不能证明相比成熟soft guidance有具体新增边界，可关闭，不必扩读无关附件。

当前精确v1官方题摘页作轻量撤回/修订信号核查，未发现撤回标记。CUDA-L1现API已v12且性能摘要与v1明显不同，故保留版本分离，不把当前题摘当历史性能证据；这不证明修订原因或全部版本史已核验。

### 本轮增量：准入事实与版本边界

原有连续§4从“以下不是候选审阅完成声明”到CUDA-L1版本说明保持逐字不变。新增题摘与原件保留在[本轮筛选](../_sources/daily-20250721/SUP_SCREENING_20261011.md)，不把55份精确v1题摘称作55篇完成研究。

LeanTree经独立FIRST反馈定点读[精确v1](https://arxiv.org/html/2507.14722v1) §1/§3.2–3.4及Appendix B：factorized states/AND-OR沿用旧工作；metavariable coupling决定哪些goal能独立，不能一概拆分。v1具名反侧为原Lean REPL不调用kernel检查tactic assignments可接受错误proof；全term检查另有含syntactic branching的false-negative，作者提出只检查新增assignments。保留的是**可执行状态分解必须与依赖传播及验证粒度共同设计**的潜力，未复现、未核当前软件修复、不声称任意verifier有保证。可能owner为AGENT-PLANNING/正确性依赖PLATFORM-EVALUATION-SYSTEM；公开身份未定，尚未比较Books具体差额，不据此改书。

为判断准入，另定点读FCRF v1任务object/interaction难度及simple/in-depth reflection预算、Docopilot v1文档数据recipe/§5.5消融/RAG对照、EduThink4AI v1 §3及Table3/4/6的raw critique下降反证。它们只说明潜在增量不是模块名/规模本身，不授完整性能/因果结论。没有跳过已获取的必要题摘，但其余实验/代码未进入深审；潜力清楚而公开日期未定的先隔离，不创建无界全文待办。

EduThink4AI Table3 Note的基线多来自Long2024/Liang2024，raw critique为本文结果；model/prompt/evaluator/budget可比性未证，故只保留作者报告的反侧线索，不称同配置因果证明。Flow Equivariant RNN的v1命题是one-parameter Lie subgroup下运动/flow等变及hidden states几何变换，不是任意时间重参数化/time-warp；已依独立题摘反馈收窄。未以待核可信度倒推关闭潜在贡献。

AgentFly v1 token-mask/异步tool-reward/集中资源管理，与后版Unified Resource System的typed resource/backpressure分开；Omni-Think v1课程不借后版BWT；GRID v1 T5/Flan-T5机制不借v4；SASFT、Tiny、Morphlux及EduThink4AI也保留版本差异。后版标题/摘要不回填2025机制或数字。所有新增材料当前不支撑Books正面采用、普遍安全保证或“无遗漏”。

独立EX反查后的具名补读：14693 v1 §V-B/VI-C保留自动源标签高分与C-SSRS标注集近随机的测量混杂线索，source-attribution只是作者解释、不是因果证明；14833 v1 §2.2 Eq11/12及Algorithm2保留双conditional denoiser互导和diffusion mask guider取消外部mask输入的条件接口差额；14850 v1 §5.2 Eq19/28保留skill-conditioned可学习QP的CBF硬约束/CLF slack与高层advantage对齐低层reward。后三项分别可能归TRAIN-DATA/PLATFORM-EVALUATION-SYSTEM、MULTIMODAL-GENERATIVE-PARADIGMS、MULTIMODAL-EMBODIED-VLA，不因医学或非foundation名称关闭；未采用FID/Dice、普遍安全或跨任务收益。日期未核，不写Books，也不声称已有覆盖。

Dr. Boot已读[UvA官方旧论文记录](https://scripties.uba.uva.nl/search?id=record_54126)、下载PDF封面/摘要/§6及公开item metadata：同名同作者同摘要，`dc.date.available`为2024-01-09T16:01:41Z，封面2023-07-26仅为论文日期。旧摘要和结论已包含repair训练/推理、APPS反侧，不能作为2025-07-20首次公开增量；未断言完整版本逐字相同，详细入口/停止/原件见本轮筛选。该项交root归属协调，不catchup、不改书。

## 5. 缺口与下一步

**本轮可执行剩余：** 无。Anscombe已实际核全部51项potential处置及安全/设计反侧、分层EX、source入口/停止与六部分，三项误关闭及Dr. Boot先稿修复后最终DAY通过，见[独核§9](../_sources/daily-20250721/SUP_INDEPENDENT_20261011.md#9-最终day裁决)。完成的只是本日安全终态，其他已授权日期仍按独立目录继续，不混写本日。

**本轮外部保留A（公开身份/日期）：** 其余50个精确家族和逐项命题集中在[本轮筛选表](../_sources/daily-20250721/SUP_SCREENING_20261011.md)，同组仅请求一次；Dr. Boot已恢复更早库身份，不再归入未读/未核组。缺首次公开正文/官方announcement或作者原稿公开日期及时间语义，且必要时确认没有更早公开稿；这决定是否归属2025-07-20，而非追查小时。arXiv announcement精确日入口不支持、日list400；正常日程、submitted、ID月份不能代替实际公开。可接受官方历史公告/原正文公开日期，取得后先核日期/家族，再仅审相关精确版本并独核/协调Books；确认窗外交root路由，本作者不catchup或创建别日报。

LeanTree具体OpenReview pROVJwTb6w与Memorization c6nqmjfG1Y论坛均redirect challenge、API403；没有读到稿件，不能把forum ID当已证明的更早首稿。恢复材料还须核身份/版本及first-public语义。Subliminal官方blog Jul22是窗外事件，manuscript最早日期仍未确认；不给本日正面证据，也不擅自重开Jul22。

**本轮外部保留B（目录）：** Google Publications目标自然日公开目录；Hunyuan现存9项仅2026；Z.ai真实More终18项仅到Dec07；MiMo Blog More/route未恢复Jul2025历史索引。需对应官方目标日期目录/公告及原件链接；不需要全机构历年论文。Meta Blog、DeepMind Blog、Seed英语论文/Blog与ERNIE已恢复的切片不再沿用“完全未读到目录/空payload”旧缺口；其未登记/其他目录范围不被当前切片授覆盖。只重开受影响机构本日。

**历史隔离说明：** 以下旧轮可执行/小时缺口及完成标签冻结为当时记录，绝不是本轮新增门槛或本轮完成声明；本轮只核公开日期，不要求小时。旧121家族与旧§4不扩成新增队列。历史保留材料若到达由root按真实归属定点协调。

**可执行剩余：** 无。root非作者DAY与定点纠偏已完成。以下缺少外部公开时间/历史目录的材料保持隔离，不作为新增深审队列。

**外部保留A：arXiv公开批次。** 具体材料身份及准入命题全部在[筛选记录“日期保留”](../_sources/daily-20250721/SCREENING.md)逐项列明。主要包括2507.13474、13540、13546、13568、13569、13579、13601、13666、13681、13710、13761、13773、13833、13868、13871、13919、13949、13984、14000、14049、14067、14111、14137，以及从API题摘识别的13490、13525、13591、13598、13705、13712、13736、13739、13859、13933、13942、14063、14263、19514、2508.00007。所有均不支持正面结论、评分、Books或“无遗漏”；其中Seed-X/PRIDE等明确贡献关闭项不为日期追加请求。

另有2507.14248 AdViT的解释/安全分离反证、2507.13920 Causal Process Models的稀疏动态interactiongraph、2507.13812 SkySense V2的统一多模态backbone与异分辨率接口机制，同样只保留题摘准入线索，不因安全、World Model或foundation主题自动采用。

缺少的是**首次公开正文/首次公告时间完全落窗的官方证据**。提交时间可对应正常07-21 08:00BJT批次，但[官方说明](https://info.arxiv.org/help/availability.html)明确moderation可能延后。`oai-13474/13546/13833`的arXivRaw版本日期只给提交史，普通datestamp是元数据修改；`datacite-13474/13833`创建分别07-21 01:19:39Z、01:28:32Z已在窗后，其v1 Updated不是明确公开字段；NABLA v1 Updated更已变为2026-07-02，不能拿它重建2025公告。定点恢复已停止。

同一组只请求一次：可接受官方07-21该批带日期的announcement/历史邮件，或作者**原始正文**的公开时刻及可核查时间语义（完全落窗的范围也可）。重开顺序是日期/首次身份→仅相关精确版本必要证据→独立复核→比较owner与必要Books修改；未得到材料前保持隔离。EdgeVLA另有v1 journal-ref “IROS-MoMA3 Workshop2024”，同一请求须包含其2024稿是否已公开、正文与时间；不能以2025新arXiv ID当首公开。API返回2508.00007等延迟ID也说明按提交区间不等于公告批次。

**外部保留B：机构历史目录。** GoogleAI、Meta、Hunyuan、Z.ai、MiniMax缺本窗官方历史切片；Seed明确为论文API payload缺失（Blog当前可返回目标切片已检查）、MiMo明确为Blog历史日期（Paper已有切片）。主入口、公开API/归档定点恢复及停止位置见§2。ERNIE归档已恢复，不再作为缺口请求。可接受机构官方历史目录/公告存档，包含原始正文链接与公开时间；不是搜索摘要、当前首页或仓库最新修改时间。只重开相应机构本窗，不遍历其历年论文。不据这些缺口宣称覆盖通过，但外部长期不可得可经独立复核作为本窗安全终态保留。

**窗外线索：** [Apple报告](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates)官方明确7月17日已发布正文，属于此前事件；本日不审为新贡献、不扩窗、不自动创建或改写别日报。真实日期需要重开时由总协调者路由。

## 6. 复核

**本轮增量复核：** 复核者：Anscombe（非报告作者，`01a1289f-7cae-7253-bef5-9228c04195d8`）；结论：通过。root依其实际[最终DAY§9](../_sources/daily-20250721/SUP_INDEPENDENT_20261011.md#9-最终day裁决)同步，不用首批局部通过替代全日。

本轮实际复核：14每日来源入口/日期切片/分页停止及具名OpenReview/UvA恢复、77发现家族完整发现题摘；全部51P精确v1准入/处置，26EX发现题摘及11个重点分层样本/三项原EX反例；共57家族精确v1题摘（作者本地55与两个在线EX），七家族必要核心窄段及Dr. Boot旧稿身份/摘要/结论。LeanTree/EduThink/Flow与三项误关修复、Seed US/MiMo日期及Google七事件写回均已实际核。原窗口/旧0候选/连续§4冻结，50日期与具体目录保留隔离，Books零新写/不认领已有覆盖，完整六节DAY通过。

未验范围：其余20个EX的完整历史版本/核心、51P全部方法/定理/性能/实现/复现、缺失日期与Books具体差额，未授这些层次已完成；FIRST结果计入本轮、不重复审阅，旧轮通过不授本轮。机器检查只证明格式与可判定一致性，不代替上述实际语义。

本轮机器检查：2026-10-11 `python3 -B scripts/validate_research.py --report papers/2025/07/21/README.md`通过（1份V3）；定点`git diff --check`通过。baseline SHA-256、原窗口、原连续§4逐字比对通过；51P+26EX无交集且完整对应77发现家族，本地Markdown链接可达。没有stage/commit/push，不改无关文件。上述检查不代替非作者语义验收。

**原轮复核（冻结）：**

复核者：root（独立于作者jul21_author；FIRST与DAY）。

结论：通过

通过的是隔离处置的安全终态；外部保留项不是Coverage/Evidence通过。

首批独立复核已读NABLA、DistFlow、PSA、Promptomatix、CogniQ-H、EdgeVLA六项精确v1完整题摘：前三潜在机制准入成立且要求性能/ASR限原条件；Promptomatix成熟meta/DSPy组合关闭成立；CogniQ-H要求定点确认软prior机制而非仅数据指标，已补读公式/消融并保留有限边界；EdgeVLA先隔离首公开疑点。日期有限恢复经root校准停止；这些结果只作为FIRST，不自授DAY。

DAY实际检查：六部分、固定窗口、14每日来源与Apple定点身份恢复、查询参数/不足一页停止范围、API提交字段与公告分离、版本隔离、正式候选0及Books零写入。root直接解析Seed论文缺payload、Blog两页15/18项与实际日期，检查Hunyuan公开POST返回、ERNIE归档和MiMo脚本请求；接口成功没有替代历史覆盖。初次未恢复的入口经定点修正，剩余外部目录缺口保持隔离。

独立完整题摘检查共46个不同家族：FIRST六项；后续检查筛选表全部潜在线索的题摘及Seed-X、PRIDE、Cybersecurity Survey、BifrostRAG四项关闭样本。当前API后版只用于发现层检查，不作为v1历史结论。重点核安全/负面信号：GIFT、Latent Safety Certification、VLA-Mark、Value Probing、Prompt Engineering、Consistent Explainers、Innocence、Primacy、AdViT、Political Persuasion，未以应用标题或实验局部性自动排除。SpiNNaker2/Diffusion-FSCIL原理由将通用部署/表示原则充作本次增量，已改为具体关闭；其余未明确否定的潜在线索仍只隔离，不自授证据成立。

CogniQ-H所读软prior公式只保证严格正prior下支持域不被硬剪掉；不证明有限预算能纠正坏prior，更不证明这是相对成熟soft guidance的长期增量。当前仅保留未采用的线索，恢复公开身份后仍需决定准入，不能把这次DAY当作正面审阅通过。

未检查范围：其余明确关闭项没有逐篇独立题摘复核；所有潜在线索的完整实验、实现、缺失公告、实际复现与待核Books差额亦未验明。四类关闭样本覆盖成熟流程组合、任务PEFT比较、安全综述及领域RAG；不把分层抽检称为全量来源或论文证明。缺失材料到达仅重开受影响项。

机器校验：`python3 scripts/validate_research.py --report papers/2025/07/21/README.md`和`git diff --check`通过；相对章节路径及工作树范围已检查。未stage/commit/push。机器校验不替代上述实际语义复核。
