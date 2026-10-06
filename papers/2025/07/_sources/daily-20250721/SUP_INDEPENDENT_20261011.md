# July21 增量独立复核

复核者：Anscombe，非报告作者；本日作者为 Schrodinger（`01a129f4-0108-79e2-bb60-b48228c717f4`）。执行日：2026-10-11。唯一写入文件为本文件；未写 README、State、Books、合同、索引或任何其他日期文件，未 stage/commit/push。

## 1. 权限与复用

启动及压缩恢复重读 AGENTS、Research/Report 合同、Sources 使用说明与 Daily 组、Prompt、ROADMAP、State 本日路由和本日 README。补充窗口仅为 2025-07-20 完整 BJT 自然日；原 `2025-07-20T09:00:00+08:00 ～ 2025-07-21T09:00:00+08:00` 窗口、正式候选0及连续旧§4冻结，不要求新增材料的公开小时。

复用的是 baseline 内原轮 root 独立 FIRST/DAY、46家族题摘及旧局部证据的有效判断，不重新发现或重复读旧121家族、旧核心和旧 Books；它们不代签本轮。没有继承 July11 候选、网页观察或原证。未扫描 Weekly、全年队列或其他日期；列表出现2026仅核目录 metadata/停止范围，不研究其正文。

独核方式为实际读取本日原始响应、结构化解析、精确v1题摘及必要窄段。没有复现作者浏览器；Hunyuan两次浏览器失败及四条辅助搜索的执行观察明确继承作者 tool observations，不称自己读过动态 DOM 或重做搜索。

## 2. 发现、版本与数量

直接解析四份 `SUP_arxiv-{model,systems,agents,multimodal}_20261011.raw` Atom 与 request：模型42、系统22、Agent48、多模态12，124 appearances / 77 unique families；每个 `totalResults = returned < 150`，start0/max150/submittedDate升序，停第一页。查询只限主题与 `[202507191600 TO 202507201559]` 提交区间，是补充 BJT 日发现切片，不是公开日期证据、全池或全月待办。

原四查询原件解析为121家族，与新增77交集0。原52份v1汇总逐项回到 raw HTML 实际读完整题摘并核 `Cite as ...v1`，不只读作者 JSON。错误请求2507.15005v1为 Twin Groups，正确 AIDev 为2507.15003v1；前者不计77或52。

首批6P（14683、14715、14722、14777、14799、14805）与3EX（14688、14800、14912）全核，结果并入后续，不重复计数。全部原48P已独立准入；其余29个发现层 EX 完整 Atom 题摘也已读，含安全/负面信号，不仅看标题。分层重点样本为14688/14800/14912/14845、14785/14887/14899/19525/14824/14957/15007；后续发现14693/14833/14850不能按领域或非foundation自动关闭，定点v1和窄段重开。

额外实际在线读14785v1、14899v1完整题摘，及14693/14833/14850v1完整题摘；合计57个不同家族的精确v1题摘（原52+2个EX+3个重开）。15007v1在线请求 cache miss，只有发现层当前v2题摘，不能声称它的v1读完。其他明确EX仅发现层版本，不以当前版数字反填2025。

初次修正目标为51P+26EX=77，正式候选仍0；作者原包52份v1加三个重开为55份，不把本复核在线另外两个EX算进作者本地包。现已直接解析落稿的筛选表与55行JSON：P/EX无交集且并集精确等于77，所有P均有v1原件、55身份唯一且原件可达，v1身份一致。正式候选仍0。

原52v1页可见 Comments/期刊信息及轻量撤回/勘误信号已检查，未发现可见 withdrawn/retracted/erratum 标记；不是完整版本史检验。Dr. Boot Comments直接提示2023学位论文，已触发具名更早首公开门。2025会议接受说明不自动等于已更早公开，也不自动授当前日期。

## 3. 全部潜力的独立准入边界

下表是未采用的具体增量校准，不是评分、Evidence完成或 Books覆盖。完整题摘身份见[作者精确v1包](SUP_V1_ABSTRACTS_20261011.json)及[筛选表](SUP_SCREENING_20261011.md)。原48项均不因日期缺失、深审成本、小实验或负面结果而降分关闭。

| v1身份 | 实际潜力及不能外推的边界 |
| --- | --- |
| 2507.14675 Docopilot | 跨页表示/文档数据recipe与RAG碎片化选择；750K规模本身不准入，局部对照不证通用端到端成本。 |
| 2507.14683 MiroMind | length-progressive RL及adaptive repetition reward改变长度预算训练；开源/榜单不是贡献，组件归因未完成。 |
| 2507.14686 MIPD | 正负rationale加scene/instance对齐蒸馏影响未见/罕见情境迁移；不泛化所有小模型。 |
| 2507.14705 Neo | 随机状态及动态多轮测试触及静态脚本遗漏；只限作者受测QA/red-team系统，不采普遍10倍收益。 |
| 2507.14715 RTGen | CPU/GPU/NPU共驻多模型五策略联合deadline/TTFT/TPS；不是新通用调度算法，不外推GPU集群。 |
| 2507.14719 Aymara | 总体安全分数掩盖隐私/冒充细分失效；自动rater可信度和政策范围未完成证据审阅。 |
| 2507.14722 LeanTree | 可执行Lean4 factorization必须连同metavariable依赖与验证粒度设计；AND-OR/分解不是新创，不保证所有goal独立或任意verifier正确。 |
| 2507.14725 GRID | 无任务标签推理遗忘、prompt梯度聚合和约束解码；v1 T5/Flan-T5，不借v4输出空间与Qwen/Llama。 |
| 2507.14748 CSF | inner-product及判别skill diversity可识别性条件；局部RL不自动EX，理论假设尚未核足。 |
| 2507.14758 GRACE | semantic属性/旅程分段稀疏依赖的表示成本选择；不因推荐领域关闭，不证明CoT忠实性。 |
| 2507.14768 WS-HSA | 联邦聚合异构群组的security/collusion集合及key-rate条件；不是泛泛密码学主题关联。 |
| 2507.14777 Memorization | recollection/counterfactual/contextual度量冲突修正记忆解释；形式语言/18模型局部，不据此否定普遍隐私风险。 |
| 2507.14783 Omni-Think | hybrid规则/judge奖励及structured-to-open课程；不是合并模型发布，不借后版BWT。 |
| 2507.14793 Flow Equivariant RNN | one-parameter Lie subgroup的运动/flow及hidden geometry等变；不是任意time-warp/时间重参数化。 |
| 2507.14797 EPD | 每ODE步梯度并行蒸馏改变NFE/延迟/质量；额外并行资源不是免费加速。 |
| 2507.14798 Aerial3D | DUSt3R/MASt3R/VGGT在图像数/高分辨率下失效与SfM/MVS互补；不是仅航片榜单。 |
| 2507.14799 Web IPI | accessibility tree是投影而非信任清洗；限受测Llama/BrowserGym，不复制攻击payload。 |
| 2507.14805 Subliminal | 无关数字/代码隐藏统计传递teacher trait，same-base条件影响语义过滤充分性；不推任何师生都迁移。 |
| 2507.14811 SegQuant | graph segmentation语义及dual-polarity校准；工具兼容不证生产实现。 |
| 2507.14815 FastLongSpeech | 迭代压缩/变比率及short-to-long迁移；无长数据条件下效果不是普遍无损。 |
| 2507.14819 Doc2Chart | attribution/source依赖评价区别于视觉外观；成熟两阶段生成流程不是唯一增量。 |
| 2507.14823 FinChart | 新版本退化及judge不可靠修正评价假设；不因金融领域关闭，不能外推全部VLM。 |
| 2507.14849 LongCoT/context | 蒸馏推理与lost-in-middle关联；训练数据等混杂未控制，非已证因果。 |
| 2507.14851 VideoRestoration | 退化语义teacher近似训练后解耦推理；成本移到训练，非免费SOTA。 |
| 2507.14871 TinyLM | 浅层committee/deep BERT有限资源质量延迟取舍；不推儿童认知或借后版code可用性。 |
| 2507.14879 DepthScale | sparse anchor非学习regional相对到metric标定保持foundation输出利用；不证零成本或所有几何任务。 |
| 2507.14882 Pruning | 应用component约束/soft coefficient/group magnitude区别于全局重要性；只MNIST autoencoder，不外推LLM。 |
| 2507.14894 SASFT | SAE preactivation特征指导SFT/code-switch修正；不证特征因果完备，v1消除案例数不能借后版。 |
| 2507.14897 AgentFly | v1 token-mask轨迹训练与异步tool/reward执行边界；非后版typed lifecycle/backpressure。 |
| 2507.14900 NeuronXA | neuron alignment的跨语测量与下游相关性替代embedding；小规模并非EX，不证语义真值。 |
| 2507.14901 CausalReduction | 干预一致性下非线性状态归约/解释条件；数学主线准入，未读全定理。 |
| 2507.14904 TriCLIP3D | 共享2D encoder及点云GARF adapter对齐的参数取舍；不只套CLIP。 |
| 2507.14906 FeedbackDecline | 结构化MDP反馈可能伤复杂规划；小实验负面仍可能改选择，不作普遍律。 |
| 2507.14928 ByzantineAgents | 并行proposal/独立evaluator与robust aggregation替代leader/quorum；阈值和威胁假设未核足。 |
| 2507.14958 MUR | momentum uncertainty历史调节thinking budget；不是物理术语准入，不泛化50%预算收益。 |
| 2507.14959 Polymorph | 每帧active LoRA集合共享backbone区别整模型switch/merge；runtime能耗质量条件待核。 |
| 2507.14975 FCRF | object/interaction难度分配simple/in-depth预算；Mentor/Actor名称不是机制或归因证明。 |
| 2507.14976 HiCroPL | 层级依赖的跨模态prompt方向及浅层语义保留；不是所有prompt tuning。 |
| 2507.14987 AlphaAlign | safety/helpfulness双奖励及over-refusal边界；不采普遍deep alignment保证。 |
| 2507.14997 ImageRegression | generic prompt无收益而image-specific语义有效的局部反侧；非图像应用即EX。 |
| 2507.15003 AIDev | PR快但简单且acceptance较低提示benchmark实用性混杂；dataset大小本身不准入。 |
| 2507.15015 EduThink | raw critique下降作为反思/评价协议线索；Table3基线来自文献，非受控同配置因果。 |
| 2507.15889 DrBoot | repair训练收益与推理同预算resampling分离、APPS检验问题；旧库及PDF后已核更早同贡献，排除本日首次公开，详§8。 |
| 2507.17773 MultiKernelBench | 低暴露硬件平台与kernel正确性跨平台盲区；不只任务数量。 |
| 2507.19526 STAG | frozen codebook+soft assignment/KL的graph token结构接口；label-free不等于所有场景true zero-shot。 |
| 2507.22915 HallucinationTheory | 定义风险并提出PAC-Bayes/Rademacher界的潜在可靠性条件；未验定理/假设，不把成熟工具或综述名当已证新理论。 |
| 2508.03674 Morphlux | v1 programmable chip-to-chip optical fabric与placement/reconfiguration碎片取舍；ID月份非日期证据，不借后版名称。 |
| 2508.03703 RecInversion | 推荐logit反演及domain consistency/prompt复杂度的隐私失败条件；不等于任意文本输出泄露。 |

三项定点误关闭及恢复要求：

- [14693v1](https://arxiv.org/html/2507.14693v1)完整题摘及§V-B/VI-C：gold-standard与subreddit自动标签测得不同表现，提示source-attribution shortcut而非目标语义。P限定数据标签/评价混杂，不进入临床判断；不接受作者gold-standard自称为已证、shortcut归因为因果或全部自动标签无效。
- [14833v1](https://arxiv.org/html/2507.14833v1)完整题摘、§2.2 Eq11/12及Alg2：两个conditional denoising过程互相生成guidance，额外guider解除外部给定mask限制而联合生成image/annotation。P为生成因子化/条件输入选择；医疗数据只局部验证，未验一般等价证明/可比预算，不采FID/Dice为通用收益。
- [14850v1](https://arxiv.org/html/2507.14850v1)完整题摘、§1/§5.2 Eq19/28/Theorem5.1：skill-conditioned可学习QP硬CBF/松弛CLF，结合高层advantage低层reward对齐。P为层级policy学习与底层安全约束耦合；成熟CBF不算新创，保证依赖initial-safe/dynamics/约束可行性，不证明现实控制安全或泛化。

## 4. 反侧、必要补读与EX分层

安全/负面不是因日期未定就略过：全部潜力的题摘已独核，包括Neo、Aymara、WS-HSA、LeanTree、记忆测量、Web IPI、Subliminal、SASFT、Byzantine、AlphaAlign、RecInversion，以及航片基础模型、FinChart、LongCoT、反馈退化、ImageRegression、EduThink、AIDev、DrBoot、MultiKernel等反侧。没有执行攻击、复用payload、实际系统测试或复现作者安全实验。

四个原P必要窄段已实际读取：

- LeanTree v1 §1/§3.2-3.4与Appendix B，见[本地原件](SUP_core-2507.14722v1_20261011.raw)。原REPL未kernel检查assignment的错误接受，与Apr10,2025全term检查遇syntactic branching的false-negative分开；作者增量检查及独立full Lean验证仍不证明任意verifier安全。作者已修FIRST/筛选/README，不再把分解概念充新贡献。
- Docopilot v1 §5.5 Table6及§5.2/5.3 RAG对照，见[原件](SUP_core-2507.14675v1_20261011.raw)。不同文档来源改变局部Acc/F1，支撑recipe潜力，不授架构首创/端到端普遍成本或受控全组件归因。
- FCRF v1 §IV-D，见[原件](SUP_core-2507.14975v1_20261011.raw)：task type/objects/interactions控制simple/in-depth，预算与object+interaction难度归一化挂钩；不是只给反思流程改名。
- EduThink v1 §3及Table3 Note，见[原件](SUP_core-2507.15015v1_20261011.raw)：§/†分别来自Long2024/Liang2024文献，raw critique为本文结果，不能称同配置受控下降。作者已补model/prompt/evaluator/budget可比性限制。本复核未完整核Table4/6或所有实验，不能转为完整Evidence。

Flow等变误写任意time-warp已实际反馈并确认作者收窄到one-parameter Lie subgroup。上述窄段只消歧准入，不制造全51篇全文待办。

EX重点样本核定：ArabicReview为数据目录/文档/许可/采纳缺口，不因语言或综述体裁关闭；VoltageOperator v1成熟经验储存/检索/生成/修改组合，不能借v2长摘要；ElderlyCare展望没有具体模型执行增量；DepthCompletion确有single-image sparse-measurement新loss，关闭理由只能是未建立foundation/model-system独立增量，不能写“没有新loss”。AML GraphICL的k-hop/serialize/few-shot应用组合；MEKiT的template/data混合；InsightX v1的detector/NMS/EGR reflection工具组合，未给新执行/授权/可靠性成立条件，v1 F1与当前v3不同，不回填。MMCircuitEval阶段题库及局部成绩尚无具体评价混杂，EHRBenchmark领域模态比较，EFX/PMMS的agent为数学参与者，VoiceDebugging GPT修复是未来设想而非已实现机制。

其他明确EX完整发现题摘用于共同错误扩查：不将所有医疗/领域标题一刀切。WSI-Agents、EHR时间注意力、EEG课程、能源expert-LLM/MARL等仍需用具体mechanism关系判断；本轮所读增量为领域功能/训练编排或任务收益，未识别足以修正主线机制的明确新条件。它们不因已有owner或Books主题相似关闭。三个具名反例已重开，其余未发现同一误关依据足以改为P。

未验范围：其余EX精确历史版本和核心实验未逐篇核；全51P完整方法/定理、预算可比性、统计、实现、复现及Books实际差额未验。57个精确v1完整题摘、七个家族必要窄段，不等于57篇完整审阅或77家族全版本审计。

## 5. 14来源实际停止与限制

下面是对本日SUP请求与raw的独立检查；不重复发现、不称网页浏览器复现。作者有界入口完成的是处理/隔离，不授全站Coverage。

| 来源ID | 实际复核的切片、停止与保留 |
| --- | --- |
| SRC-OPENAI | [RSS raw](SUP_openai_20261011.raw)1287项，pubDate转BJT，目标Jul20无列示；邻接Jul18/21。限RSS登记事件，不移动旧hourwindow社会使命文章。 |
| SRC-ANTHROPIC | [raw](SUP_anthropic_20261011.raw)内177个publishedOn含重复，168 unique timestamps；July邻接Jul15/下个Aug1。定点Subliminal [raw](SUP_subliminal-blog_20261011.raw)可见Jul22，不能代论文首次公开。 |
| SRC-GOOGLE-AI | DeepMind真实[path page5](SUP_deepmind-page5_20261011.raw)/[page6](SUP_deepmind-page6_20261011.raw)各24 time，读至Apr/June；July七事件而非五。已有四篇原件datePublished为IMO/Backstory Jul21、FlashLite Jul22、T5Gemma Jul9；独立官方原页补核[AlphaEarth Jul30](https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/)、[Aeneas Jul23](https://deepmind.google/blog/aeneas-transforms-how-historians-connect-the-past/)、[MedGemma Jul9](https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/)，仅日期，不读为新候选。Google [Publications raw](SUP_google-pubs_20261011.raw)年度/筛选form不能恢复目标公开日，缺口隔离不扫全年。 |
| SRC-META-AI | Blog真实1-4页有不同卡片，page4 Jul21 startup/AWS→Jun27 Seamless→旧项且Jun4/17非单调；读整个目标页，不用反复featured2026区停止。Research overview无历史论文目录，不能授机构论文全覆盖。 |
| SRC-QWEN | 首页及[page2 raw](SUP_qwen-page2_20261011.raw)：Jul22 coder→Jun27 TTS/Jun26 VLo，到旧条目停止。限官方Blog，不扩repo。 |
| SRC-DEEPSEEK | [updates raw](SUP_deepseek_20261011.raw)May28→Aug21之间没有Jul20登记事件，限该changelog。 |
| SRC-MOONSHOT | [raw](SUP_moonshot_20261011.raw)26个time，2024May29→2025Nov7，Jul17→Aug1；K2 Jul11不入新增日。 |
| SRC-TENCENT-HUNYUAN | [publicList request](SUP_hunyuan-public_20261011.request.json)POST pageNum1/pageSize100/renderType0，[raw](SUP_hunyuan-public_20261011.raw)code0/total9/list9，仅2026日期；成功接口不足2025历史。动态壳未读完，作者两次浏览器失败仅继承观察，不称独立DOM复现；不读2026正文/私有接口。 |
| SRC-ZAI | [page2](SUP_zai-page2_20261011.raw)/[page3](SUP_zai-page3_20261011.raw)实际18卡/date数组相同，末端Dec7,2025且没有更多。JS公开page路线已尝试，不再称More未试；目标July目录仍缺。 |
| SRC-BYTEDANCE-SEED | [US request](SUP_seed-papers-US_20261011.request.json)真实x-tt-locale:US、type1/year2025/token0/count20；[raw](SUP_seed-papers-US_20261011.raw)18数组/total94/next20/has_more，Dec15→Jun26非单调，目标邻接GR3 Jul21、CoT Jul10。无header空payload已纠正，token0停止是有限切片非94全站；Blog type2 token0/20真实15/18条、total49、到Mar12，Jul22→Jul15。未代签论文公开日。 |
| SRC-BAIDU-ERNIE | [真实page2](SUP_ernie-page2_20261011.raw)6条、1/2末页，Aug14→Jun30跨目标；不继续历年。 |
| SRC-XIAOMI-MIMO | [home raw](SUP_mimo_20261011.raw)Paper8条：2025May12/Jun4/Sep19/Oct21及4个2026目录项，只核metadata。Blog15+More无日期；公开index/homechunk恢复route而/blog/实际单篇Dec16,2025，不是历史索引。Sep19遗漏已反馈修正；Blog目标缺口保留，不继承July11额外chunk观察。 |
| SRC-MINIMAX | [EN raw](SUP_minimax_20261011.raw)12个日期卡最早Oct27,2025；[CN raw](SUP_minimax-cn_20261011.raw)13卡，多Jan15,2025 MiniMax01，其余最早Oct27。读可见页停止，不能证明未登记/移除历史没有发布，不复用无效query page2。 |
| SRC-ARXIV | 四份原Atom数与request一致，限提交日四主题，一页各足；公开announcement只支持年月不是精确日，[daylist请求](SUP_arxiv-daylist_20261011.request.json)HTTP400非零命中，availability通常日程非实际公开。公开日/先稿隔离，不以ID月份/提交/元数据更新补造。 |

Meta/DeepMind/Seed/ERNIE已恢复切片不再继承旧“目录完全不可得”；Google Publications、Hunyuan、Z.ai、MiMo Blog、arXiv公开批次仍非正面Coverage。其余已检查仅限上述目录切片，不声称全站无遗漏。辅助搜索没有读到必要原件不等于零命中，也不把未采用space站点作primary evidence。

## 6. 首公开、Evidence与Books门

全部潜力不列确定本窗候选、不评分；修复后DrBoot已核更早同贡献，其余50项仍缺本窗首次公开的必要身份/日期证据。正常arXiv日程、提交史、ID或当前版本不能弥补。只需日级，不传播旧小时要求。

LeanTree论坛[pROVJwTb6w](https://openreview.net/forum?id=pROVJwTb6w)、Memorization论坛[c6nqmjfG1Y](https://openreview.net/forum?id=c6nqmjfG1Y)：本复核实际打开两forum及各自公开PDF端点，均challenge，未读到稿件；作者API请求403原件亦核。不能从forum ID代签同一家族/更早公开。只恢复这两个具名正文、identity对应与public-date语义，不扫整会议或绕challenge。

Dr. Boot [v1](https://arxiv.org/abs/2507.15889v1) Comments明确2023 University of Amsterdam Master's thesis及[record54126](https://scripties.uba.uva.nl/search?id=record_54126)；本复核在线实际访问失败，随后作者恢复官方200响应。本复核实际读取[该raw](SUP_drboot-thesis_20261011.raw)，核题名、NJL van der Vleuten、Jaar2023及完整AB与v1内容对应，支持更早学位论文家族提示，但Jaar不自动证明公开日，未读2023全文或确认具体修订。作者应将其列为具体先稿门：核原正文及必要实质事件差额、可解释首次公开日期；不能把2025新ID当首次。取得后只路由真实归属，不在本日catchup。Subliminal Blog Jul22事件窗外，也不能决定最早manuscript date。

当确证窗内事件后，才评分并按命题需要进入标准/深入审阅、独立证据复核、owner具体论点与Books差额比较；不得因本文件P校准直接采用。必要主张未变可复用现有题摘/窄段，不机械全读51篇。未做Books章节核对，故不声称已有覆盖；本轮不写书的原因是公开身份门未过，而非NoChange主题已覆盖。正式候选0、Evidence完成0、新Books采用/修改0，不是没有潜力。

## 7. 冻结、机器与当前裁决

独立机械读取baseline：SHA-256 `6d0e558296d361633fb1ee7bdfbb685c090098ea515dd75062d20d7302af8e64`；原窗口相等；旧§3空候选表保留；旧连续§4由段首到CUDA-L1版本说明与当前前缀逐字相等。新增说明不混入冻结块。

实际运行 `python3 -B scripts/validate_research.py --report papers/2025/07/21/README.md` 退出0、检查1份V3；机器通过只证明字段一致，不覆盖上述误关及先稿门。最终本地引用/限定diff检查在作者修订落稿后追加，不提前宣称。

修复前结论：未通过（当时普通事项待作者落稿，非伪称外部受阻；最终裁决以下节为准）。

已给作者精确反馈：14693/14833/14850恢复窄P，数量应51P/26EX、v1本地包应55；DrBoot加入具名2023先稿门；Google七个July事件补齐日期，前三项旧P纠偏LeanTree/EduThink/Flow及Seed US/MiMo Sep19已落稿。其余没有要求重扫或全量重读。待这些实际文本及六部分同步检查后，才给DAY安全终态；外部日期/目录保留不授正面Coverage/Evidence/Books或“无遗漏”。

## 8. 具名修复实际复核

作者已实际落稿51P/26EX/55份v1及三个误EX的新准入句，本复核读到更新后的README§1/3/新增§4/5/6和筛选表。三个新增v1本地raw完整题摘与在线所读一致，未见可见撤回标记。发现层77家族的Atom可见条目未见withdrawn/retracted/erratum/corrigendum提示；这是轻量当前材料核查，不证明完整版本史没有修订。

DrBoot闭合的是具名先稿处置，而非理论或全部实验完成：[bitstream](SUP_drboot-bitstream_20261011.raw)公开HAL的bundle链接、[bundle](SUP_drboot-bundle_20261011.raw)的item链接、[item](SUP_drboot-item_20261011.raw)均已实际读取，对应同一PDF/record54126。item同题名、作者及完整AB，`dc.date.available`/accessioned为原值2024-01-09T16:01:41Z（BJT日期2024-01-10）、issued=2023、inArchive/discoverable true、withdrawn false。没有拿issued、封面或lastModified作first-public。不能确定世界最早公开日，但官方available字段与同贡献正文足以排除其2025-07-20首次公开。

实际只读[73页旧PDF](SUP_drboot-thesis-pdf_20261011.pdf)封面/目录、PDF第4页完整摘要及第45页§6结论（纸页41），另有引言短段，不通读全文。封面July26,2023仅论文日期；摘要/结论已经包括repair训练收益、推理repair不优于同量采样和APPS测试问题。本日潜力使用的这些具体命题已有更早稿，不能当2025新发现贡献；未作全篇逐字版本diff或声称没有任何其他修订。作者README正确将其单独排除并交root归属协调，其余50项日期隔离，未扩日/catchup。

此时全部51项具体准入/处置均已实际覆盖，没有以外部日期缺失掩盖未读准入。最后普通项仅为把独立已读的AlphaEarth/Aeneas/MedGemma三个窗外日期补入正式来源表，不要求作者重扫或扩读其正文；最终DAY在该文本到位后追加。

## 9. 最终DAY裁决

复核者：Anscombe（非报告作者）。

结论：通过

验收范围：July21补充2025-07-20自然日的安全终态；不是正面Coverage/Evidence通过，不授潜力材料评分、Books采用、普遍性能/安全或“无遗漏”。本节取代§7修复前未通过与§8末尾待同步状态，不删除当时发现/纠偏记录。

最后SRC-GOOGLE-AI实际落稿已读：七个July事件日期完整，补AlphaEarth Jul30/Aeneas Jul23/MedGemma Jul9，明确仅metadata、全部窗外，不追加core。三个误关闭、DrBoot先稿、LeanTree/EduThink/Flow版本与归因、Seed US及MiMo日期修复均已实际到稿。未剩未读准入或具名可执行研究事项；作者/root只需采用本结论同步完成状态及本轮§1/5/6，不把其当前“待独核”行政描述扩成新材料队列。总验收数量由root协调，本复核不写State。

六部分独核结果：§1分清124提交发现/77唯一、55本地v1、51贡献线索/26EX与正式0；§2逐来源有真实入口、范围、停止和具体缺口；§3正式旧0未增列未知日期/评分；§4原连续正文冻结，新增只有限潜力/版本与反侧，不授证据完成；§5其余50日期保留及历史目录缺口具名隔离、重开条件明确，DrBoot更早同贡献不冒充本日首公开；§6非作者身份、实际范围和机器权限分离。旧轮完成/小时说明明确历史，不借旧通过代本轮。

本轮实际题摘范围：全部77发现家族的完整题摘已覆盖，51P均核精确v1准入/处置；26EX完整发现题摘已核，11个重点样本及三项原EX反例定点检查，最终EX中6家族另核精确v1（ArabicReview、VoltageOperator、ElderlyCare、DepthCompletion、AMLGraphICL、InsightX）。57个不同家族精确v1题摘含作者本地55和另外两个在线EX；必要核心窄段七家族及DrBoot旧稿身份/摘要/结论。FIRST计入不重复。没有把剩余20个EX的完整历史版本/核心或全部51P实验、理论证明、实现、复现、缺失日期及Books具体差额称为已验；这些未被用于正面采用。

必要外部保留只按受影响家族/目录重开：50项取得可解释首次公开正文/公告及必要先稿身份后先判落窗，再按实际命题评分/补证据/独核/比较Books；LeanTree与Memorization要论坛正文及家族/日期语义，不拿challenge成功响应代读稿；Google Publications/Hunyuan/Z.ai/MiMo Blog需官方本日历史切片及原件，不求全站历史。Meta等已恢复的有限目录不支持未登记论文无遗漏；Subliminal Jul22与DrBoot更早稿仅交root日期路由，不catchup。

最终实际机器/范围检查：修复后再次运行 `python3 -B scripts/validate_research.py --report papers/2025/07/21/README.md` 退出0、1份V3；限定 `git diff --check -- papers/2025/07/21/README.md papers/2025/07/_sources/daily-20250721` 退出0；本文件未跟踪，另行 `git diff --no-index --check -- /dev/null <本文件>` 无whitespace诊断，退出1仅表示内容差异，不误称退出0。README与本文件本地Markdown文件引用可达，旧SCREENING日期保留标题存在；当前六部分编号完整。baseline SHA、原窗口、原空候选表及旧连续§4再次机械比对相同；51P/26EX并集77无交集、55原件身份唯一且全部P在包中。最终追加后的本地引用/冻结/限定diff检查亦通过，不将机器PASS替代上述语义。

Books处置为本日无正面采用/无修改，不是已有覆盖验收；未读Books章节、不自授共享写锁。本轮报告可结束，但外部保留的Coverage/Evidence不得转换为通过或计论文完成。本人只写本文件，保护共享及其他2026改动，无Git写操作。

## 10. 完成态行政差额FINAL窄核

复核者：Anscombe（非报告作者）。用户明确授权本轮只核July21完成态差额；已在另一日期最近保存点后重新加载AGENTS、适用Research/Report合同、Daily Sources/Prompt/ROADMAP及State本日路由，仅核本日报完成header、§1/5/6和新增具名source行，对照本文件§6/8/9；不重读51P，不混用其他日期研究，不预签或写State。

结论：通过

验收范围：root行政同步与既有§9安全终态一致，无新增采用权限或研究普通事项；不是新一轮全量DAY，也不是正面Coverage/Evidence或Books整合验收。

实际当前header为完成，检查时间2026-10-11T17:13:38+08:00。§1/5/6同步的是非作者DAY、研究普通0、124提交发现/77家族/55本地v1、51潜力处置及26EX、DrBoot更早同贡献及其余50日期保留；不把潜力算确定候选或证据完成，未授评分、Books已有覆盖、普遍性能/安全或无遗漏。旧停点明确历史，不能恢复为本轮小时要求或未读队列。§8/9采用限制未被root同步改变。

§2新增`SRC-OPENREVIEW`行只描述LeanTree/记忆测量两个已触发forum及PDF/API恢复的challenge/403限制，仍未读稿、不证明先稿身份/公开日、不扫会议。UvA表外行只描述DrBoot已核record/PDF/bundle/item及原available字段，未将issued/封面当首次公开、未声称全版本diff；与本文件§6/8事实一致。没有新的source内容待核。

实际重新执行V3：退出0，检查1份V3。baseline SHA-256仍为`6d0e558296d361633fb1ee7bdfbb685c090098ea515dd75062d20d7302af8e64`；原窗口与baseline相同，旧空候选表保持，连续旧§4前缀1987字符逐字一致。当前README六节齐全，**本地Markdown文件引用17处（11个不同目标）全部可达**；不沿用口误26。限定README/同日_sources的diff-check退出0。机器通过只支持这些机械事实，语义结论据上文实际差额阅读。

只追加本日独核文件，未修改Report/Books/State/index/scripts或其他2026材料，未stage/commit/push。root可据此同步本日验收路由；具体State写回仍归root且未在此验收。July21完成态窄核已闭合，之后按新日独立上下文继续，不再重读本日source/core。
