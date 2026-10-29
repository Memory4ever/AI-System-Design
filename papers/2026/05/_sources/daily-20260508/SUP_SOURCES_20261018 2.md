# 2026-05-08 增量来源补查




## A1 窗口、ownership 与复用

作者：supp_may08_author；执行日 2026-10-18 BJT。用户授权保留既有候选日期、评分、原窗口和有效证据，只补遗漏；新增窗口为 **2026-05-07 ～ 2026-05-07**。本日原184家族＝108实际整合＋76具体已有覆盖，最低审阅路线129 deep＋55 standard。原README快照见[baseline](./baseline-before-supplement-20261018.md)，原§4连续正文不改。

已完整重读AGENTS、研究合同、Report合同、来源说明及每日组/主题、统一Prompt、ROADMAP、本日README相关层与LEARNING_STATE最新路由；采用daily-research-closure技能只做分层复用与限定验收，不继承旧Created/OAI三信号排除规则。旧619宽库存不是本轮审阅队列；原May08 08:00批次184只去重，不搬移。唯一写入范围本日README、此SUP和一份baseline；Books/LS/索引交root。

## A2 发现启动与首批准入（待独立校准）

- SRC-ANTHROPIC：实际打开May07官方[Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)，全文含核心机制、审计游戏与限制。原小时窗仅日期不能归属的缺口，在自然日补查中可按官方May07日期处理。具体增量：activation解释缺真值约束→AV文本瓶颈与AR重建联合训练→解释需以重建/干预与独立验证限定，不能把可读文本当内部思想真值。拟候选；论文正文链接继续恢复，非外部受阻终态。
- SRC-OPENAI：主题限定搜索 `site:openai.com/index "May 7, 2026"` 发现[accidental CoT grading](https://alignment.openai.com/accidental-cot-grading/)，实际全文已读至实验部分。具体增量：只过滤常规CoT消息不足→CoT可经tool output间接进入reward→训练奖励的数据流审计必须检查实际grader输入，且局部无显著下降不等于未来监测安全。拟候选（安全/纠错必要深入）。
- 同查询发现[语音API发布](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)及微调服务资格变更；前者继续读取核心以区分机制贡献和版本事实，后者只恢复直接兼容性边界，不泛化为新训练算法。
- SRC-GOOGLE-AI：主题日期搜索发现[AlphaEvolve impact](https://deepmind.google/blog/alphaevolve-impact/)。先读取AI基础设施相关核心；医学/电网应用不纳入科学应用范围，不因模型使用或机构归属自动准入。
- SRC-ARXIV：官方cs.CL May列表打开超时，不当零命中。复用月度DataCite原始缓存作为标题/摘要线索，v1 Updated=May07只辅助发现（1135宽条目不是候选/待全读队列）。定点核May07原日报§3的160唯一ID只作同事件去重，不继承该日报摘要/评分或论文池；下一步按模型/训练/推理/多模态/Agent主题检查潜在线索和完整题摘。日期拟入选项用直接公告或registered有效组合，不用Created。

普通待办：完整题摘贡献校准、日期原件、必要证据与Books差额、13官源有界收尾、六部分增量合并及root非作者独核。本轮尚未DAY/FINAL，不计新增分子或完成。

## A3 首批完整题摘的语义准入（待root校准）

直接读取月度原始DataCite题摘作发现，不以当前摘要替代精确v1必要Source。May07原日报的160条候选ID仅用于相同事件去重，未重审其有效结果。下列准入不是完整月目录的逐项queue。

| 身份 | 原约束 → 原文实际增量 → 需要重考的选择 |
| --- | --- |
| [2605.05073 HJA ranking](https://arxiv.org/abs/2605.05073) | pooled judge把系统分歧当噪声 → 分离共识、judge sensitivity与residual disagreement并给identifiability/fixed-panel uncertainty → ranking目标与置信区间不能仅靠增加judge重复次数定义 |
| [2605.05126 ConsisVLA-4D](https://arxiv.org/abs/2605.05126) | 多视角表征与future-frame未对齐instruction → object identity跨view、compact geometry及scene dynamics三层一致性 → VLA空间状态需先明确跨视角身份与动作条件，不以新增模块名称本身准入 |
| [2605.04356 Online Natural Language Feedback](https://arxiv.org/abs/2605.04356) | scarce expert下固定proxy易过优化 → 迭代训练到过优化停点、收新专家反馈并更新ICL/finetuned proxy → 比较专家预算时须区分proxy刷新与单纯增加RL步数 |
| [2605.04128 JoyAI-Image](https://arxiv.org/abs/2605.04128) | 理解/生成独立模块阻碍空间反馈 → spatial MLLM+MMDiT shared interface与novel-view辅助推理 → 需核双向perception/edit环收益是否可归因，不把SOTA或VLA展望当证据 |
| [2605.05054 DP-FM](https://arxiv.org/abs/2605.05054) | normalized VLM alignment忽略径向confidence并耦合角速度 → 直积几何分离radial/angular transport＋hidden-state guidance → 是否应保留特征模长和等速角轨迹而非一律归一化 |
| [2605.04547 Stage-adaptive audio diffusion](https://arxiv.org/abs/2605.04547) | 静态SSL guidance/采样忽视训练阶段 → SSL discrepancy斜率驱动regime、decay guidance与timestep/regularization → 训练进度信号是否比固定schedule更有信息 |
| [2605.04641 CAST](https://arxiv.org/abs/2605.04641) | 非caption任务弱visual grounding → 用caption-sensitive head及output steering增强视觉取证 → 需核训练外干预对幻觉与基础能力的取舍 |
| [2605.05092 Driver-WM](https://arxiv.org/abs/2605.05092) | 车内识别没有多步驾驶员状态预测 → 外部traffic到内部driver gated causal injection并保时序因果 → 预测条件/rollout状态不能与recognition或因果实证混同 |
| [2605.04412 DiLAST](https://arxiv.org/abs/2605.04412) | 3D生成OOD style被当容量不足 → 2D diffusion teacher渲染引导优化已有structured3D latent → 需区分latent可表达性与数据/优化导致的style缺口 |
| [2605.04458 DoGMaTiQ](https://arxiv.org/abs/2605.04458) | report QA nugget评估依赖人工策展 → 文档grounded生成/聚类/quality selection再比human rankings → 自动评价是否保rank而非把self-generated nugget当真值 |
| [2605.04903 DeltaNAS](https://arxiv.org/abs/2605.04903) | 生成完整架构code冗长易无效 → LoRA训unified diff并做结构novelty过滤；核1-epoch proxy对50-epoch rank → edit表示是否降低搜索无效预算，非成熟diff原则计分 |
| [2605.05116 Junking](https://arxiv.org/abs/2605.05116) | jailbreak成功依赖带语义prompt → 无显式指令token序列搜索及难度比较 → natural backdoor主张要与target-prefix优化/低概率关联证据分开 |
| [2605.04313 NoisyCausal](https://arxiv.org/abs/2605.04313) | 相关/因果混淆受结构noise影响 → ground-truth graph控制noise＋显式graph prompting → 评价需区分噪声鲁棒性和因果可识别性，不因benchmark新名字入选 |
| [2605.04304 HierVA](https://arxiv.org/abs/2605.04304) | 多subplot上下文过载 → manager compact状态、visual/text分流与scoped zoom，声称互补消融 → 需核joint context收益与额外call预算，非manager/worker比喻 |
| [2605.04352 Algebraic Trapdoors](https://arxiv.org/abs/2605.04352) | answer-key conflates wrong/abstain → 构造verifier/prover非对称，区分commit/abstain正确性 → 五条trace能否只支持评价盲点而非结构推理普遍结论 |

代表关闭（已读完整题摘，无相关纠错标记；不为关闭理由不依赖的日期再建request）：RecGPT-Mobile 04726仅移动推荐本场景收益，无披露可迁移部署机制；AegisTS 04902为MTS清洗质量/模型选择与下游应用，不因层级Agent或reward名词变模型训练数据管线；ARMATA 04225空间分配/路由的非LLM MARL不属模型驱动Agent主线；04565 LEO MARL offload为卫星通用网络路由，不披露LLM推理状态/模型切分机制。04831 StoryAlign新增领域story preference数据与专用RM/BoN成绩，但完整摘要未给能改变通用RM选择的新失效归因或机制；05148 learned image codec处理人类终端图片压缩，不是给多模态基础模型的codec/表征接口，仅“神经codec”主题不足。04264 governed memory Viewpoint把治理过程写为selection regime，没有原文超出既有版本/provenance/ratification流程的新执行机制或可验证失效证据。04488 moral judgments小样本same-checkpoint对比，原文只得局部伦理问答agreement，未新增monitorability或模型机制，不能仅因controlled label收录。

日期具名验证路径已实际跑通：DataCite `/dois/10.48550/arxiv.2605.05126` 返回state=findable，registered=2026-05-07T02:09:52.000Z；官方abs唯一v1=2026-05-06T16:55:44 UTC。EDT公告最早界May07 08:00 BJT，登记最晚界May07 10:09:52 BJT，同日且先后合法；需连同response关系的arxiv.content核验保存原字段。缓存Updated只作恢复线索，不替代该registered证据。

## A4 后批定点题摘与日期原件

新增需独校准的潜力：05151以PatchTST窄/单层、SAE字典扩张和causal latent干预反证“任何Transformer竞争力都靠强superposition”（只采用forecasting局部反例，非将时序应用泛化到LLM）；05197区分likelihood与grammaticality的跨语言linear-probe证据（负侧semantic plausibility较差，改模型解释而非传统NLP指标）；04962 TabEmbed将表结构/numerical hard negatives用于同一retrieval/classification向量接口；04834 ALL-IN以random input space+covariance给feature permutation/distribution及expected orthogonal invariance（先核ICLR更早正文）；05031 CAD discrete diffusion异构属性transition kernel而非把Euclidean noise统一套离散参数；04613 VocalParse以lyrics-first scaffold再interleave melody/alignment改变跨模态输出factorization；04899给token embedding几何1-form与采样误差连接，但chess相关不当causal世界模型证明；04093 DEMM把trace容器存在与property-level reconstructability分开，140合成/3事故只是feasibility，拟最低关闭而非validated audit标准。

进一步明确排除：05192纯Lp数学中Grok仅研究辅助；04127 position仅串联既有model-collapse与低资源伦理影响，无新增机制/反证；04188传统非LLM utility negotiation软件聚类；04858 crypto comparison为regression/dense/CNN，不是LLM安全推理边界；04704 UVMarvel UVM领域IR/协议库和stimuli refinement，摘要未显示超出domain工具组合的模型/Agent新机制。04227 Pro²Assist为AR眼镜程序任务助手，摘要是perception/context/continuous reasoning组合与场景成绩，没有可区别于既有context tracking的新执行条件；不因state-aware名词进入Agent owner。

2026-10-18实际向DataCite逐DOI恢复23条精确元数据，所有response均`relationships.client.data.id=arxiv.content`、`state=findable`。原始UTC字段如下（URLs统一 `https://api.datacite.org/dois/10.48550/arxiv.<ID>`，不将registered改名实际发布时间；每条唯一v1 Submitted另与官方abs核对）：

| ID | Submitted v1 UTC | registered UTC |
| --- | --- | --- |
| 2605.05073 | 2026-05-06T16:09:55Z | 2026-05-07T02:08:35.000Z |
| 2605.05126 | 2026-05-06T16:55:44Z | 2026-05-07T02:09:52.000Z |
| 2605.04356 | 2026-05-05T23:25:00Z | 2026-05-07T01:51:13.000Z |
| 2605.04128 | 2026-05-05T15:49:47Z | 2026-05-07T01:45:38.000Z |
| 2605.05054 | 2026-05-06T15:51:26Z | 2026-05-07T02:08:08.000Z |
| 2605.04547 | 2026-05-06T06:54:00Z | 2026-05-07T01:55:52.000Z |
| 2605.04641 | 2026-05-06T08:32:30Z | 2026-05-07T01:58:06.000Z |
| 2605.05092 | 2026-05-06T16:30:48Z | 2026-05-07T02:09:03.000Z |
| 2605.04412 | 2026-05-06T02:08:54Z | 2026-05-07T01:52:33.000Z |
| 2605.04458 | 2026-05-06T03:34:46Z | 2026-05-07T01:53:42.000Z |
| 2605.04903 | 2026-05-06T13:32:05Z | 2026-05-07T02:04:29.000Z |
| 2605.05116 | 2026-05-06T16:47:07Z | 2026-05-07T02:09:38.000Z |
| 2605.04313 | 2026-05-05T21:26:01Z | 2026-05-07T01:50:06.000Z |
| 2605.04304 | 2026-05-05T21:12:01Z | 2026-05-07T01:49:54.000Z |
| 2605.04352 | 2026-05-05T23:16:30Z | 2026-05-07T01:51:07.000Z |
| 2605.05151 | 2026-05-06T17:23:27Z | 2026-05-07T02:10:29.000Z |
| 2605.05197 | 2026-05-06T17:57:31Z | 2026-05-07T02:11:36.000Z |
| 2605.04962 | 2026-05-06T14:22:34Z | 2026-05-07T02:05:57.000Z |
| 2605.04834 | 2026-05-06T12:30:50Z | 2026-05-07T02:02:47.000Z |
| 2605.05031 | 2026-05-06T15:26:11Z | 2026-05-07T02:07:35.000Z |
| 2605.04613 | 2026-05-06T08:03:31Z | 2026-05-07T01:57:26.000Z |
| 2605.04899 | 2026-05-06T13:28:16Z | 2026-05-07T02:04:23.000Z |
| 2605.04093 | 2026-04-29T09:59:36Z | 2026-05-07T01:44:48.000Z |

除04128/04093的最早界跨日需直接公告外，其余最早公告均May07 08:00 BJT，registered最晚May07 09:49:54～10:11:36 BJT，全区间同一自然日，身份/版本/先后无冲突。组合只限定arXiv announcement，未证明不存在具体更早正文。04834的ICLR身份触发定点先公开核验，不采用无限假想渠道检索。

## A5 当前事件检查与必要原证：两官源

23项当前官方abs均已实际读submission history及当前withdrawal/erratum标记。**04356的v1明确withdrawn，退出本轮新增准入/评分/采用/Books**；v2不挪代v1。其余22未见上述标记，但版本存在不等于已核所有修订。04834已有同作者/机制OpenReview正文 `Dt4XAIKYbf`（ICLR2026）及 `tDX4A4AE5a`（UniReps2025）可见；官方论坛/API被challenge/403，不能用搜索日期作首公开时间，保精确先稿资格待恢复。

### [Natural Language Autoencoders](https://transformer-circuits.pub/2026/nla/index.html)

官方全文May07；网页超过web提取上限，已用直接HTTP解析全文必要Method、case、evaluation、auditing及Discussion，材料并未外部不可得。评分拟2+2+3=7。残差activation→AV离散文本→截断AR重建；warm-start summaries＋KL限制语言退化，AR做MSE回归、AV以负MSE做RL，单步两更新互不反传。FVE不是faithfulness度量：三目标模型不同训练预算不可当scale controlled对比；多项known-context预测随训改善但classification仅83→86，AR逐claim删去测试仅弱判别。文本可能hallucinate/反推比activation多的信息；高重建可能由steganography或input inversion达成。

关键支持/反侧：reward→penalty小改经AR差向量影响toy odd/even输出，相比random steering支持局部因果；poetry改动只有约半成功且输出可能不协调。审核任务用generic-data训练NLA/SAE，Sonnet4.6 auditor+固定rubric比较tool subsets；NLA无data-search亦可恢复RM-bias根因，但初始化权重仍含目标模型latent知识；PT-only search已足够、NLA不再获益，behavioral-quirk数未显著增加，跨旧scaffold成绩不可直接比。latent eval-awareness无observable truth，仅三类manipulation方向一致；不能把belief readout当真实belief测量。局部安全/解释用途须独立corroboration；每activation数百输出token导致长录及在线监测成本，不声称实现跑通/复现。Books owner拟PLATFORM-EVALUATION-SYSTEM，唯一可新增命题为“重建闭环提供读activation的假设接口，不拥有其语义真值；必要验证与可扩展性边界”，交root对现正文差额。

### [Accidental CoT grading](https://alignment.openai.com/accidental-cot-grading/)

官方May07全文必要节与所有反侧已读；拟3+2+3=8，安全/纠错深入。实际reward-input扫描发现tool输出可把本来excluded CoT带回reward，channel配置不证明reward path隔离。Instant confirmation-penalty固定其他训练的重跑、heldout CoT-aware/blind检测及checkpoint监测未见该局部明显下降；Thinking只有reward recomputation而无完整ablation，prompt-injection case无targeted causal对照。强压力stress tests能改表面CoT；一个flaky-tool集recall降低，说明总体未降不能替代分场景反证。结果依赖压力相对大小、环境覆盖与行为可发现性，不推出通用安全阈值。regex detector不覆盖所有非标准reward输入。未披露完整硬件/预算、样本与uncertainty不能代填，未复现内部pipeline。Books owner拟TRAIN-RLHF：只增reward实际输入路径审计与monitorability因果范围，不把厂商政策当模型保证；拟文交root。

## A6 官源收尾的当前实证

- SRC-TENCENT-HUNYUAN：research网页0行、IAB子任务hidden不支持/普通create超时后，root提供公共前端API路由；本作者实际POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":1000,"renderType":0}`，headers accept-language=zh与Content-Type=application/json，成功code0/totalNum11/list11；page2同body pageNum2成功list空，确认停止。相邻100039 Real life is where context gets hard：publicAt2026-04-30T21:06:45+08、displayPublishTime04-30 15:00；100041 Hy-MT2：publicAt05-21T17:55:26、displayPublishTime05-21 15:00。列表无May07研究事件。100061 display04-23但publicAt07-05，说明展示时间不是公告事实；不纳本日且不扩全站/普通PR。
- SRC-ZAI：Research当前完整首列表明确04-29→05-20相邻跨过May07，无需点“更多”到2025；本日无显示项，不能外推未列研究。
- SRC-BAIDU-ERNIE：博客第1/2页从2026-05-09至2025-11-21，May07两侧为04-30/05-09，停止无需翻到更早2025；无当日项。
- SRC-MINIMAX：英文页抽取有限，中文官方同源实际可读列表从08-13至2025-01-15；May07由04-27/05-25括住，无本日项。日期限定搜索误命中space.minimax.io用户建站，全部不作官方研究材料，不进入候选。
- SRC-XIAOMI-MIMO：实际Paper列表8项，2026-03-13→06-29括住May07；Blog15项无日期，无法据此证明该自然日完整覆盖。未以未标日标题建无限全文请求；保本日官方带日目录/公告到达时重开。
- SRC-MOONSHOT：platform.kimi.com/blog当前静态列表27链接，最新只到2025-11-07，未提供2026目录；日期主题搜索无确定May07命中，不把旧列表当零遗漏。需官方本日公告或带日研究索引补齐。
- SRC-QWEN：旧qwenlm指向qwen.ai，后者blog/research网页提取0行；已补日期主题搜索，定位Qwen Code May07周更页（仅功能列表，待core关闭）；未把动态首页当2026研究目录已查完。
- SRC-GOOGLE-AI：DeepMind实际May07 AlphaEvolve impact的AI infra与邻接已读；硬件/缓存/编译案例及单成绩未披露新增搜索机制或可比资源合同，不因AI infra标签入选该综述；linked精确原论文是不同先公开事件，只有具体日期线索才定点恢复。Google Research主页2026年筛选而非日级，未授May07完整覆盖。
- SRC-META-AI：Research当前0行；限定May07模型/训练主题搜索未恢复可唯一归属原件，目录缺段隔离，不报零命中。
- SRC-DEEPSEEK：主页仅当前V4.1/V4及more研究链接，不是日级索引；May07主题搜索无确定事件，不按current页面补造旧日Coverage。

这些真实来源缺段不支持正面Coverage/无遗漏。还有可执行的Qwen core、官源已入选必要证据与arXiv主题有界收口，不因保存记录而停止。

## A7 必要Source分批（author prepared，待非作者核验）

### [2605.05073v1 HJA](https://arxiv.org/html/2605.05073v1)

2+2+3=7，深入。实际§3–5、§6 Table1/Fig2-3与§7：judge独立Binomial BTL logits，S=γμᵀ+UVᵀ；row centering、meanγ=1、μ⊥V及distinct singular values定义canonical consensus，不是无规范的任意latent preference。γ只表示consensus sensitivity，非judge真实性。§5局部收敛依初始化在正曲率局部basin；§5.2固定N/K/r、comparison重复增长、稳定sampling fractions、逐judge connected graph、local identifiability/regularity才有WaldCI，full ranking在tie不平滑。50 synthetic seeds、四real datasets/20seeds比较pooled BTL/JA及SVD baseline；in-house最强perturbation和部分near-tie不支配，协调偏差不受保护，非adversarial ranking certificate。采用局部命题是“judge敏感度/结构性分歧/consensus分别持有估计对象；CI不消除consensus bias”，owner拟Ch66。

### [2605.05126v1 ConsisVLA-4D](https://arxiv.org/html/2605.05126v1)

2+2+2=6，实际深入到§4 eq3–21、§5 Table1–7、G.1实现。FiLM语义topK每视角256→32、VGGT cross-attn供身份/geometry；DINO/VGGT layer-wise fusion＋aggregation tokens；CoTracker动态对象与DepthAnything深度辅助目标训练，inference不生成future objects/depth，以implicit knowledge并行action chunk。不能称运行时显式world rollout。4×A800训练/RTX5090实机；LIBERO batch64/chunk8与real batch32/chunk25不混性能。Table3相对OpenVLA 2.31×但相对OpenVLA-OFT只1.25×simulation latency；72.7/108.2是predicted actions/sec非sensor/closed-loopHz。Table5/6各消融与causal/bidirectional对照支持局部设计，1/16稀疏RealWorld SR68.3低于1/8 78.3；15-trial实机小样本、并非普遍安全或外推sim-to-real充分证明。owner拟Ch26：训练辅助几何/动态预测与部署token预算/动作闭环分责。

### [2605.05054v1 DP-FM](https://arxiv.org/html/2605.05054v1)

2+1+2=5，标准；已读§3 manifold eq1–3/训练与§4主要对照。warped metric dr²+φ(r)²dθ²，取constant φ令radial/angular独立，linear radial+slerp angular保feature norm；这不是证明任意任务的norm就是calibrated confidence。pretrained CLIP/CLIP-LoRA/Adapter、11 few-shot datasets/K=1,4,16、同features/time-shift+CFG比几何，HFM公平对照特意去掉自身两stage phase，不把它当完整原HFM系统。主Table2有dataset/shot反例，非每格获胜；lightweight velocity与multi-step adaptation有新增成本，未披露端到端servingSLO。需保runtime步数与variance未穷尽的限制；owner拟Ch23为表示几何与归一化适用条件，而非图像生成范式普遍替代。

### [2605.04641v1 CAST](https://arxiv.org/html/2605.04641v1)

2+1+2=5，标准；已读§3–6/eq5–11及Table5–7。视觉only mask的caption/noncaption last-token head outputs训练probe选topK，steering向量却从原无mask outputs平均差估计；两者不能混。1000 LLaVA pretrain samples预计算向量＋α加到selected head outputs。五模型/五benchmark，POPE调α/K有tuning依赖；α过大忽略text，K过多破坏其他path。LLaVA7B POPE latency仅该表TTFT99.8→102.2ms、TPOT36→36.5；on-the-fly两forward约1.8×延迟且质量反不如precomputed。precomputation、访问白盒head及跨数据vector偏移是成本，不能称无训练/无成本（模型主权重不训，但probe训练）。owner拟Ch23/唯一交root。

### [2605.05092v1 Driver-WM](https://arxiv.org/html/2605.05092v1)

2+2+2=6，标准并读实际反侧：§3 frozen Qwen3-VL D2048双stream与view embedding、vector gate eq7因果history truncation、§4 Table1–3。5→5 autoregressive latent/skeleton rollout、no future ext pixels；g只受外部latent控制，gate override/intervention是mechanism probe不识别人类因果效应。AIDE平均motion小，no-ext retrained All MPJPE71.74对71.47、HM136.94反优138.03；external semantics TCR26.39对90.15更明显，不能把dynamic全指标收益归因于外因。Table3的Δ是intervened与factual预测之间的偏移，不是对GT的误差增长；15.208/116.751不可采用为GT退化或因果必要性证明，虽正文存在error措辞。test-time删路径的敏感性不等重训因果necessity；KL和skeleton-pre局部可优主模型，保反侧。作者明确干预只探机制；预测不具自动驾驶安全证书。owner拟Ch25：平均静态误差与reactive-tail、模型conditioning和真实因果权威分开。

### [2605.04547v1 Stage-adaptive audio diffusion](https://arxiv.org/html/2605.04547v1)

2+1+2=5，标准；§2 progress SSL discrepancy斜率、decayed guidance/time sampling/parameter-similarity regularizer，§3 fixed backbone/budget两任务Table1/2。**实际SSL guidance decay γ=max(0,1−k/(ρK))仍是预定linear schedule**，不可把所有组件都说成g_k feedback control。stable-audio-tools DiT/frozen USAD，三策略分别加到uniform baseline，不能把分别有效写成联合模块synergy。TTA FAD2.36→2.08/2.12/1.91；SR48k目标、8/16/24k输入LSD大多升但SISNR有退化（8k decayed12.73→12.40），semantic/latent与waveform fidelity不一。作者未给充分walltime/seeds/CI，训练效率不得仅从同budget质量推生产加速。owner拟Ch28：阶段优化信号/目标何时依赖schedule、component归因边界。

### [2605.04412v1 DiLAST](https://arxiv.org/html/2605.04412v1)

2+1+2=5，标准；已读§3 latent优化loss/§4 Table1与loss ablation。冻结Trellis-image-large＋SD1.5，2D attention distillation导rendered5固定views到structured3D latent；content/alpha-floater/邻接latent smoothness分别约束内容泄漏、漂浮Gaussian与饱和噪点。A100/500flow steps、η5，仅assets/style images采样；HPSv3一般/具体prompt、两个VLM aesthetics与10volunteer preference均偏perception，非几何/物理真值。UniLat/Hunyuan plug-and-play主要qualitative，不证明所有latent容量/OODstyle universal；优化可高成本且依renderer梯度/固定视角。owner拟Ch24：不同空间teacher诱导轨迹与content/geometry fidelity tradeoff，非世界模型。

## A8 两官源Books差额及逐字PRE（未写入）

root明确授权本作者仅在这两项协调的窄位置写Books；已读Books公共上下文/ROADMAP、Ch5内部分析实际论证及Ch4/6交接、Ch66 372–376重建/输出扰动/AO接口、Ch31 872–910及1070邻接、Ch30/32交接。使用documentation-and-adrs技能只记录实际设计差额，不另建ADR或改结构。NLA主命题是activation如何被text bottleneck表达，**唯一canonical owner选Ch5 WORLDVIEW-REPRESENTATION**；Ch66已有AO sensor接口不重复正文。CoT主命题是训练奖励输入路径，唯一Ch31 TRAIN-RLHF，不复制Ch66测评链。

NLA现有Ch5“信息存在、可读与被使用”首段已讲private code/重建非truth，下一段转fresh probe；缺的是**无预设问题的AV文本与AR回译目标如何形成假设生成接口，及joint objective何时退化**。拟在这两原段之间插入以下两段，marker只唯一绑定此项：

> 固定 probe 先声明要读取的属性，适合已有清楚假设的诊断；尚不知道该问什么时，还可以把单个 activation 经语言模型转成文本，再由另一个模型只读这段文本重建原 activation。令 AV 产生解释 z、AR 产生重构值，AR 以重构均方误差回归，AV 则以负重构误差作为奖励；离散文本成为两者通信的瓶颈，而不是研究者预先给定的概念字典。适当的摘要式 warm-start 与语言约束可以维持可读性，却没有把语义真实性写进目标；它提供的是待验证假设，不是内部思想的逐字转录。
>
> 这条路线保留前述 private-code 风险：更高重构可能来自隐藏编码、局部复制输入，或解释器根据已有知识补出的细节。已知输入属性的预测、删除单条解释后的重构变化和修改文本后回译为 steering vector，是不同强度的检查；局部 steering 成功不认证完整机制，不能在看到某种未表露“意识”时省去独立验证。两套模型的训练与每个 activation 数百输出 token 还限制长轨迹和在线监测；解释漂移或成本不合适时，保留原 activation、固定 probe、其他因果干预与外部行为对照。

CoT现有Ch31冲突/正交/相容目标段与30036受限对照已解释压力关系；缺的是**实际grader消费路径可绕过正常channel排除、事故修复与监测因果范围如何区别**。拟紧接30036两段后、MiCo反馈构造前插入：

> 奖励是否接触推理文本，还要按实际数据流检查，而不能只看 grader 配置中是否排除了 CoT channel。模型可能先用工具读取自己的推理，再把它放进会被评分的 tool output；正常通道已过滤，奖励仍在间接选择推理的表达。训练作业因此应保留 reward 输入的来源、拼接与工具回流路径，并把检测到的泄漏交回对应奖励 owner 修复。字符串匹配能廉价发现原文回流，却不覆盖改写和所有非标准输入，不能作为完整隔离证明。
>
> 修复路径与证明监测未受损也必须分开：保持其他训练条件固定、移除某项 CoT 奖励的对照，强于只重算同批轨迹的两种 reward。公开事故分析中，部分局部对照未见明显下降，但其他压力实验仍出现特定工具场景的 recall 退化；总体平均不能抹去它。压力大小、相关环境覆盖和被奖励行为的可发现性改变，旧阴性结果就未必适用。检测、重跑及独立行为/trace 审计都有费用；条件或效果不清时，应隔离奖励路径并保留未受污染的检查点与外部验收，不因局部无显著差异放开推理文本优化。

拟末注只记录official May07、必要Source/反侧、未复现与Source/PRE/POST实际状态，暂不写通过标签。等待本日reader实际PRE后apply；未将Source通过当作已写或POST。

**A8实际落实更新：** supp_may08_reader实际owner/完整邻接/逐字PRE通过后，本作者只按root授定两位apply保存：Ch5第354/356两段＋629纯note；Ch31第898/900两段＋1330纯note。reader随后实际读回新增两段、两侧邻接与本人注，POST通过；两note已行政同步该实际结果，待reader最小标签读回。两项均唯一canonical owner，无Ch66重复正文；指定窄锁可释放。此项完成不等本日报DAY/FINAL。

reader随后已实际读回两个note POST标签，准确；两官源Source/PRE/实际POST有效链关闭，窄锁释放，不重开。

## A9 后批必要Source prepared

### [2605.04903v1 DeltaNAS](https://arxiv.org/html/2605.04903v1)

2+1+2=5，标准；§3.3/3.4/实验及limitations。baseline code→unified diff→patch/syntax/instantiation/forward/1-epoch gate，90%MinHash dissimilarity过滤新baseline pool；LoRA r32 BF16三7B/22cycles/3300candidates，~90–100GPU-hours含evaluation与LoRA。**正文有new accepted加入training corpus的表述，但Fine-Tuning段明确LoRA训练集始终static LEMUR、generated只扩baseline pool**；仅采用明确静态训练+修改表示，不采用self-improving训练数据闭环。输出短不等正确，约1/3 context mismatch failure。50-epoch proxy相关Mistral强、Qwen中、DeepSeek N12/ρ.495/p.10不显著，不接受“未显著仅ceiling故非proxy失败”的唯一因果解释。六小image datasets/first-epoch proxy不能证明LLM架构或edge部署；owner拟Agent工具/流程需按具体已有diff验证接口比较，若无新长期gap可仅报告。

### [2605.04313v1 NoisyCausal](https://arxiv.org/html/2605.04313v1)

2+1+2=5，标准；§3 DAG3–7nodes/SCM/noise、§4 graph-guided input、§5.3–5.8及Limitations。已知生成graph用于噪声诊断，变量抽取→graph→structured prompt不是从真实partial observations识别因果。graphedge扰动/语义/不同prompt与cumulative-noise对照能检查自造图是否带来收益；GPT4clean graph F1 85.2、confounding+masking74.1，cascading discovery errors。1000BIP控制保持关系/数值，属于belief cue robustness非真实causal discovery；100error case分类只所选人口。LoRA-CausalQA44.2→49.3对照改变训练，不能唯一归因causal技能、原Limitations“real-world未测”又与小scale transfer用语冲突；收窄为synthetic诊断，不作真实causal/generalization充分证据。owner拟Ch66 evaluation条件控制或已有覆盖，先比正文。

### [2605.04304v1 HierVA](https://arxiv.org/html/2605.04304v1)

2+2+2=6，标准；§2.1–2.5 manager loop、§3 controlled composite/§4 CharXiv与Limitations。global manager只保refined plan和worker最终句/crop handle，worker每次只有单张图及选择的skill，manager不看skill内容、不继承私有history。对比same-backbone ChartQA1.92k及synthetic1k varying subplots可定位context压力；CharXiv64.2、提升1.8–5.3pp，需保额外call/latency，非等总budget统治。错误crop丢global constraints，routing库不全，压缩会漏证据；没有证明domain泛化或安全。潜在长期增量是joint image-text evidence scope/私有worker算力与global context分账，owner拟Ch75，不借hierarchy本身加分。

### [2605.04352v1 Algebraic Trapdoors](https://arxiv.org/html/2605.04352v1)

2+1+2=5，标准；§3 constructed family groundtruth、§4 four-cell scoring、§5五traces与§6.6/6.7。构造元数据可快速验答案而solver难证明，commit-correct/commit-wrong/abstain-correct/abstain-wrong分别记录；152min abstention不是正确性证明且可有anti-commitment/prompt-following等替代解释，作者承认非controlled comparison。FamilyI未trace-tested。正文“default无external tools”与trace报告python/sympy工具可用不一致，因此不能把两模型time/style归因于架构或保证统一toolbudget。仅报告可验证评价构造及该局部case，拒采“最强metacognitive证据”或三层内部architecture结论；owner拟Ch66既有abstention/result-scope可能覆盖。

### [2605.04458v1 DoGMaTiQ](https://arxiv.org/html/2605.04458v1)

2+2+2=6，标准；§3文档grounded QA→paraphrase merge→quality select、§5/6排名与circularity/outlier/topic反侧。同LLM生成QA/报告可能对其自身nugget过适配；Claude生成比Llama版本改善本benchmark不保证彻底去循环（共享训练/偏好仍可能）。16 RAGTIME topics的macro ranking好不等per-topic精确；Table2定义manual nuggets＋AutoARGUE，与§5.1一句manually matched存在口径冲突，按表/实验定义不当fullymanual。§6.1是每team最高priority提交12run代理，而非严格剔低排名后的全部top systems；Table3的maximum possible仅manualnugget＋auto基准，不是数学上界。单一rankρ/τ不是claim正确。goldbank也主观，生成/cluster/LLM scoring/人工均成本；owner拟Ch66评价相关性的目标/层级，不将scientific示例变科学应用主线。

### [2605.05116v1 Junking](https://arxiv.org/html/2605.05116v1)

2+1+2=5，安全反侧必要深入至问题定义/§4–5实验。无语义anchor全input-token优化、最小greedy search仅检验某targetprefix可达；prefix命中可接拒绝，不能等同harm。四7B模型/50目标、greedy设置/预算须绑定，ASR按每优化轨迹事后挑最高external-judge success，并非一次最终query率；Gemma.52/Mistral.90与高FE方差不能当训练埋后门的频率。高perplexity只支持distributional abnormality，不证明预训练何时/如何植入；未有训练溯源或更强规模/闭源模型证据。owner拟Ch72：nonsemantic input攻击测试与成功分母/来源因果分开，是否已有覆盖交root。

## A10 四项实际owner差额与逐字PRE（待reader，尚未写入）

恢复后完整重读当前AGENTS/研究与Report合同、来源说明每日组/主题、Prompt/ROADMAP及本日停点；Books公共上下文已读。root仅授05073→Ch66、05126→Ch26、05054/04641→Ch23指定差额，必要Source沿reader R4复用。实际读取Ch66逐judge尺度段及anchor/测量身份两侧，Ch23几何/概念适配与caption双路径两侧，Ch26训练期foresight完整局部及offline milestone/teacher兼容两侧；邻接Ch22/24/25/27/65/67交接确认owner不迁移。未授其他arXiv写权。

### 05073 HJA → PLATFORM-EVALUATION-SYSTEM

Ch66已有Jury的每judge正尺度/共同偏差和anchor身份，但单一尺度未表达item相关的结构性分歧，也未区分固定panel重复下的估计CI与去偏。拟紧接2602.16610段、在固定anchor段之前插入：

> 当 judge 的差异不是同一排序上的尺度变化，而是对不同 item 有系统性偏好时，单个正尺度仍会把分歧压进噪声。一条受限分支将比较 logit 矩阵分为 `S=γμᵀ+UVᵀ`：μ 表达共识排序，γ 表达各 judge 对它的敏感度，低秩残差保存 item 相关分歧。行中心化、γ 的均值约束、共识与残差方向正交，以及残差基的锚定与非退化条件，共同限定这些对象的识别规范；γ 不是正确率，所定义的共识也不是外部质量真值。
>
> 这一分解用额外逐 judge 比较、低秩拟合和初始化成本换取更明确的估计对象，不保证一定优于 pooled ranking。固定 item、judge 与残差阶数，比较次数增长，且各 judge 比较图连通、采样比例稳定、局部可识别并落在合适曲率区域时，局部估计的置信区间才有相应依据；它不覆盖共同偏差、恶意协同或任意换 panel，近 tie 的完整名次也非平滑对象。条件不足或目标涉及事实、安全时，保留原始比较、人工 anchor、并列或无结论，不由窄区间自动签发排序。

纯note拟：`SF-2026-ARXIV-2605-05073`，exact-v1 §3–7/Thm2–3/Table1/Fig2–3，7分，固定N/K/r与connected/stable/local、非bias消除、局部非凸/near-tie和真实数据反侧；未复现。

### 05126 ConsisVLA → MULTIMODAL-EMBODIED-VLA

Ch26已有“训练future teacher部署删decoder”，但没有区分仍在线的跨视角身份/几何融合与删去的future-object/depth目标。拟紧接Training-only Foresight原三段、在运动里程碑段前插入：

> 删除未来预测 decoder，不等于把几何感知也从部署路径删除。另一条分支先按指令从各视角语义 tokens 选出对象相关部分，再与几何 encoder 的跨视角特征融合，以聚合 tokens 压缩空间关系；未来对象运动和深度只作为训练辅助目标，部署保留当前语义、几何融合与并行动作 chunk。这里必须分别声明对象身份、关系压缩和未来监督的消费者，不能把训练期 target 当成运行时观测，或把紧凑表示称为持久世界状态。
>
> 辅助 decoder 的删除省去未来生成，却仍支付在线几何编码、融合、动作预测，以及离线 tracking/depth teacher 和训练费用。更少 tokens 会丢细节，有限实机对照中进一步压缩也可降低成功率；预测的 actions/second 不是传感器闭环频率。小规模 rollout 与几何辅助消融只支持给定任务、视角和 teacher 下的选择，不认证物理真值或跨本体安全。身份/深度失配或延迟不合适时，保留完整观测、原 direct policy、短 chunk 和独立 controller，以真实反馈而非辅助 loss 决定执行。

纯note拟：`SF-2026-ARXIV-2605-05126`，exact-v1 §4 Eq3–21/§5 Tables1–7/G.1，6分，保1/16实机退化、15-trial与sim/real不同batch/chunk、72.7为预测动作吞吐；未复现。

### 05054 DP-FM → MULTIMODAL-REPRESENTATION

Ch23现有centroid/paired geometry与双曲norm不是径向/角向transport路径选择。拟接对齐节2604.00279首段、在LiteEmbed段前插入：

> 对齐路径还取决于是否保留 feature 的模长。把向量直接归一化，适合只消费方向的相似度接口，却会丢掉径向信息；在确有任务证据表明该信息有用时，可以将半径与球面方向分别传输，而不沿 Euclidean 弦线统一插值。一条直积几何分支在径向用线性路径、角向用球面插值，以固定的角向权重分开两类速度；这是表示适配的几何选择，不是证明所有 encoder 的 norm 都是校准置信度。
>
> 这需要额外 velocity 网络、训练及多步适配。有限 CLIP few-shot 对照在相同 feature、guidance 与时间设置下比较路径，仍有数据集和 shot 数反例；其中为隔离几何而删去对照方法自身阶段的实验，也不能代表它的完整 pipeline。是否保留 norm、如何选择角向路径，须由实际 consumer 的分类或检索与资源预算共同验收。径向语义不稳定、质量退步或多步成本不合算时，保留原归一化表示、直接 cosine 或已验证的 adapter，而不从几何更自然推定线上收益。

纯note拟：`SF-2026-ARXIV-2605-05054`，exact-v1 §3–4/Alg1/Table1–3，5分，保HFM删阶段对照、dataset反侧与未披露servingSLO；未复现。

### 04641 CAST → MULTIMODAL-REPRESENTATION

Ch23已有caption在线双路融合与caption/video训练reward；缺的是离线caption对照选head、线上无caption生成的视觉steering。拟接2605.01733双路径两段后、video reward之前插入：

> Caption 也可以只充当离线诊断信号，而不成为每次请求的中间文本：在一组 caption 与非 caption 指令上，先在末输入 token 位置屏蔽对文本 tokens 的 attention，取该位置的 head 输出训练 probe，选出对任务差异敏感的 heads；再从原来未加该 mask 的输出估计平均差向量，在推理时对选定 heads 作小幅 steering。选 head 的受控输入与计算 steering 的正常输入是两个实验角色，不能混成 caption 已补齐视觉事实，也不表示 attention 差异本身就是因果解释。
>
> 该接口冻结主模型权重，却仍有 probe 训练、样本制备、白盒访问、向量预计算和强度/heads 数调参费用。局部对照中强度过大可压过文本要求，改动过多 heads 也会破坏其他路径；每次请求重新算向量需要额外前向，不是固定向量的低开销结论。模型、任务或视觉分布变化后应重新回归原能力、幻觉切片与延迟；向量失配、文本遵循退步或预算不合算时，保留原图直答、原双路径 gate 或拒答，不用视觉 steering 自签 grounding。

纯note拟：`SF-2026-ARXIV-2605-04641`，exact-v1 §3–6/Eq5–11/Table5–7，5分，保1000样本probe/POPE tuning、α/K反侧及on-the-fly1.8×局部latency；未复现。

四项均是具体局部差额而非新增专题/章末摘要。拟文中的验收/回退是本项目设计推断，Source只支持上述局部机制与反侧；reader PRE前不保存Books。

**A10实际保存：** reader最终PRE通过并修订HJA识别规范、CAST末token mask限定后，本作者实际apply四处各两段与纯note：Ch66 482/484与6575，Ch26 604/606与2661，Ch23 1027/1029、1051/1053与2458/2460。实际完整顺读新增及两侧，限定diff-check通过；待reader真实POST，未预签。NLA/CoT本人注仅删末尾流程句，证据/反侧与已通过正文不变，既成过程保A8，不重开Source。

reader随后实际读回四项完整新增、两侧与纯note，POST通过，四指定窄锁释放；不添Books流程label、不授DAY。六项已完成结果先融入Report §3/§4，整体进行中。

## A11 四项后续owner差额与逐字PRE（尚未写）

root授权HierVA仅Ch75、Driver仅Ch25、Stage仅Ch28、DiLAST仅Ch24，有gap经reader PRE后可窄写。实际读Ch75视觉artifact完整局部与长视频按需读取交接、Ch25三channel/support-restriction局部、Ch28 meanCE与训练进度局部、Ch24风格/主体注入与相邻编辑局部；邻章Ch74/76、Ch23/26、Ch27/29已读交接。不复制通用原理，只补各实际接口差额。

### HierVA04304 → AGENT-CONTEXT

现Ch75已有active visual slots/按需视频读取，但没有把全局跨图plan与单图worker私有上下文分账。拟在2609.24362局部结束后、长视频段前插入：

> 多图推理还可以把全局计划与局部像素读取分开：manager 保存原问题、跨图计划、worker 的最终结论及 crop handle，每次 worker 只读一张指定图与所选技能，私有历史不回灌全局。这样避免所有图片、技能和试探过程反复挤进同一窗口；但最终一句结论是有损摘要，crop 和原图必须能回读，manager 没看过的像素不能因收到流畅结论就变成独立事实。
>
> 这将部分 context 压力换成任务分解、路由、裁剪和额外调用；局部窗口的峰值不是整条轨迹的总 tokens、费用或延迟。受限图表对照在更长多步任务上受益，简单单图任务不一定优于直接读图；错误裁剪会丢全局约束，技能库和摘要也可能遗漏。任务短、全局关系难以拆分或费用不合算时，保留完整图/直接 VLM；局部结论冲突则回读原图和相关 crop，而不是让层级结构自己认证正确。

纯note：04304v1 §2–4及Limitations，6分；PeakTok非总费、简单任务反侧、额外call/latency、crop/skill遗漏，未复现。

### Driver-WM05092 → MULTIMODAL-WORLD-MODELS

Ch25已有三channel与support contract，但没有外部环境/内部driver分流时conditioning开关的证据权限。拟在三channel“不拥有相同counterfactual contract”段后插入：

> 联合预测外部环境与主体反应时，还可以先保持两条观测流，再用外部 latent 控制向内部状态的门控注入，并只读取因果历史。它提供的是模型条件化接口：固定记录、覆盖 gate 或删去某条输入后观察预测怎样变化，可以定位模型是否对该条件敏感；这种干预修改的是模型计算，不识别人类真实反应的因果效应，也不为未观测 action support 提供环境证据。
>
> 均值运动误差可能掩盖外部语义敏感任务，但两者应分别报告：受限驾驶员预测中，去外部输入重训的部分运动指标与完整模型接近或更好，外部语义任务差额更明显；干预预测与 factual 预测之间的偏移也不是对 ground truth 的误差增长。双流、门控、历史状态和预测训练仍有费用；外部信号失配、支持不足或收益不稳时，保留单流/重训基线、真实观察与 Unknown，不把输出敏感性升级为因果必要性或驾驶安全保证。

纯note：05092v1 §3–4/Table1–3，6分；Table3 Δ是相对factual输出偏移，no-ext/HM与其他反侧，未复现。

### Stage04547 → TRAIN-PRETRAINING

Ch28已有loss统计/阶段性诊断，缺在音频diffusion辅助SSL随阶段改变作用、预定schedule与真实feedback区分。拟在2605.24667 marker后、perplexity定义前插入：

> 辅助表征目标的权重也不必在全程固定：可以用冻结音频 encoder 的表征差异及其变化诊断训练进展，再分别调整 guidance、timestep 采样或参数相似性约束。但诊断信号与控制规则必须逐项声明；线性衰减仍是预定 schedule，带阶段门限的正则也不是自动发现了全部训练阶段，不能因使用 progress 术语就把它们统称反馈控制。
>
> 这些分支增加 encoder 前向、进度统计与调参成本。同 backbone/训练步数的受限音频对照分别加入各策略，不证明组合协同，也不等总 wall time 相同；语义或频谱代理改善时，波形保真仍可能退步。辅助信号不稳定、目标相冲或净费用不合算时，保留原固定日程与独立波形/语义评价，不以某项代理的学习曲线替代最终质量或生产训练加速证据。

纯note：04547v1 §2.2–2.4/§3 Tables1–2，5分；γ预定linear、β阶段门限、分别加baseline、SISNR反侧与walltime/CI未披露，未复现。

### DiLAST04412 → MULTIMODAL-GENERATIVE-PARADIGMS

Ch24已有2D reference特征注入，但没有冻结3D latent/renderer中用2D attention teacher做每asset优化的接口。拟在2609.21242风格/主体两段后、对象运输段前插入：

> 风格参考还可以不直接注入生成器，而通过可微 renderer 约束一个已有 3D latent：冻结 3D 与 2D 模型，在少量固定视角上将渲染图的 attention 特征拉向风格 teacher，并分别保内容、抑制漂浮表示与平滑邻接 latent。这里改变的是每个 asset 的优化路径；找到某些训练分布之外的风格，不等于原 latent 能表达任意风格，也不证明 teacher 监督已经保存真实几何。
>
> 每资产多视角渲染、teacher 前向和数百步优化仍可昂贵，固定首阶段 voxel 支持和有限视角也限制可修改的结构。受限对照中的审美、文本偏好与少量人类选择只量感知，不认证背面、物理一致或几何无损；新模型的定性示例也不授通用兼容。内容泄漏、漂浮、未见视角或费用不合要求时，保留原 asset、较保守风格约束和独立多视角/几何验收，不让视觉偏好自签 3D 正确。

纯note：04412v1 §3.2–3.5/§4 Table1、ablation、AppendixD，5分；固定stage1 voxels/5views/500steps，感知非geometrytruth，未复现。

上述验收/回退为本项目推断；尚未保存Books，不把既有Source通过当PRE/POST。

## A12 后四项必要Source与三具体NC（author prepared）

### [JoyAI-Image 2605.04128v1](https://arxiv.org/html/2605.04128v1)

2+2+2=6；采用范围深入至§2/3.1–3.3/Table1–3及§6.1–6.2/Table14，而不冒称全生成/编辑配方核验。Qwen3-VL-8B final hidden states供16B MMDiT条件；3D box-centric多view cycle consistency给训练数据，generated view仍非新observation。TwNV planner 6DOF→synthesizer→original＋new view reasoner，在695题/575来自3DSR、120RealWorldQA的特定空间题中，固定GPT5 reasoner比较不同synthesizers，68.8→71.7；Qwen edit67.4有退步，不能将任何novel view都叫真实补证。四reasoner1.7–4.4pp局部改善不证明small-model机制或总预算可比；planner/reasoner重复调用、16B生成与训练费用须计。§6.2仅VGGT点云/pose定性，不用来认证真实3D；主理解Table3 MathVista/OCRB有退化。拟Ch24生成workspace或Ch23表示接口需比actualowner，以“派生视角可辅助但非独立证据”为最小采用，不写VLA/安全或因果世界模型。

日期：v1/registered跨日不足，但已实际恢复作者[官方README News](https://github.com/jd-opensource/JoyAI-Image)明确 `2026.05.07` technical report now available on arXiv；Apr02权重、Apr10/15数据是不同artifact事件，不把它们混成paper。按直接May07报告公告处理，reader日期层可定点核此News。

### [TabEmbed 2605.04962v1](https://arxiv.org/html/2605.04962v1)

2+2+2=6，标准且必要细读§2–5/Limitations、AppendixB训练/评价/serialization。语言query-to-row contrastive而非仅same-class row-row；分类隐藏target列，retrieval生成1–3数值/类别条件并symbolic校验，positive-aware hard negatives明确违条件而非语义近即负。500k retrieval＋100kclassification，2ep/B256/1024 tokens/BF16/seed42、16 PPU-810E；分类是每dataset各训独立logistic readout，不是同一个零训练classifier。311dataset/30k检索query、1.39Mcorpus；数值与多条件仍最难，cosine/ranking不保证精确满足全部谓词。两位小数serialization可改约束语义，宽表超context被过滤/截断；不由noise columns稳健或二维投影推内部attention机制。未做row-row/negative拆分消融与通用文本回归，不唯一归因每模块或授万能embedding；domainfinetune与schema/语料/索引/费用需声明。拟Ch76 dense候选与精确谓词资格分开，或已有覆盖，不当结构化数据库精确查询替代。

### [CAD CDDM 2605.05031v1](https://arxiv.org/html/2605.05031v1)

2+1+2=5，标准；实际§III–V/Eq1–17/Alg1–2/TablesII–VII。command先采样→conditioned parameter；coordinate Gaussian、dimension relative-kernel、boolean empirical-prior restricted support与absorbing态区分，不因都是整数就统一噪声。DeepCAD178k/split90/5/5，8＋4block/hidden256/100steps/单4090/100ep每ep约15min。TableV heterokernel各remove存在JSD/unique反侧，TableVI global-only invalidity3.02优于global＋local4.00；更多steps非单调。unified>90%invalid对照的token shift叙述把256值写成256–271，§III局部mask以ζ相等表示“同command”可能混category/instance，均不采为可执行recipe/严格单因素因果。GTcommand被称upperbound仅经验参考非数学上界；valid B-rep/Chamfer/cov不证明任意CAD约束/工程可制造性，conditioned只有定性。采用范围是异构离散symbol/noise语义与consumer验证，不泛化成工业应用新主线，拟Ch24。

### [VocalParse 2605.04613v1](https://arxiv.org/html/2605.04613v1)

2+1+2=5，标准；实际§3–6/Table1–3与AppendixC/D必要训练与反侧。audio tokens12.5Hz，pure lyrics先生成，再interleave word＋pitch/duration＋单globalBPM，提供已有lyrics则跳第一阶段；这是输出factorization/前训分布兼容而非自由CoT推理证据。1.7B Qwen3ASR fullFT、2H100/120ksteps/17h/dynamic18000tokens每卡最多64，2000h伪标＋50h人工。w/oCoT Opencpop WER7.18vs3.79支持局部prefix，QwenASR baseline3.41/5.93/7.83vs3.79/5.69/8.16含反退；audio-only pitch.56不优ROSVOT.38。AMTbaseline另给GTlyrics/SOFA时戳，不能与audio-only称等条件；两份lyrics无hard一致，globalBPM不适rubato，Mandarin/teacherbias边界。下游SVS数据量/训练hyperparam联变，表SingMOS4.56→4.52反侧，不由更大数据唯一归因质量。拟Ch23/24按实际词-音符接口owner比较，不作通用音乐理解或任意语言保证。

### 三项具体已有覆盖判断

reader独立给定实际位置后，作者已实际读回：DeltaNAS→Ch78 609–619，尤其613锚点/applicability、615表示粒度/格式选择及patch/linter/test分责已完整承载最小采用；其static LEMUR、proxy相关与CADNAS具体结果留报告，不为应用场景追加Book。Trapdoor→Ch66 55–66评分激励/coverage与error、74–101合同×semantic/合理拒绝与猜答、GT资格实际承载四cell最小判断；不能从五trace升级已校准元认知。Noisy→Ch66 1982–1988 synthetic SCM prediction与graph/equation分计、intervention policy/consistency及开放因果限制，210–214 negativecontrol/人口分母覆盖noise诊断；新增benchmark流程/局部LoRA留报告，不声称所有因果研究已穷尽。三项判**已有覆盖**，具体分数仍5/5/5，不因已有覆盖降分；Source反证A9/R5保留。

## A13 用户暂停checkpoint（2026-10-18T03:53+08:00起，停止后无新研究）

root转达用户明确暂停并保存。本作者已停止新扫描、Source、owner比较、Books/候选写入；只作快照完整性修复与本停点记录。README继续**进行中**，未授DAY/FINAL，不计本日验收；不接May09，不因heartbeat或普通待办自行重启。全部已授/未执行的窄写权及本作者ownership释放，恢复须重新协调。未stage、commit、push，未动LS/索引/其他日期；已有与并发修改保留。

### 本日实际有效层

- 原184行、原小时窗与有效证据不重审/不搬移。正文现只先纳入6个已完成新家族，故表当前190行；另4项实际Books已完成尚未同步入Report，不把当前190当新增最终分母。新自然日来源/候选最终清单尚未冻结。
- reader R1–R8实际层有效、R9为暂停停点：两官源＋A7七篇＋A9六篇必要Source独核通过；Story/UV两窄Source通过，代表C和Pro2改回C依据保留。三具体NC为Delta04903→Ch78、Noisy04313/Trap04352→Ch66，作者与reader实际承载段均已读，尚待并入Report。
- A11后续四项也已实际保存/完整self-read并由reader完整新增/两侧/纯note实际POST通过；加A8/A10，共**10项真实Books整合**，各只有唯一canonical owner，所有窄锁释放。不添书稿流程标签。

| 家族 | 实际正文位置（当前行仅定位，恢复以唯一marker为准） | 有效层 |
| --- | --- | --- |
| NLA | Ch5 354/356，`SF-2026-ANTHROPIC-NLA` | A8＋reader R1/R3 Source/PRE/实际POST；note只行政精简流程末句 |
| CoT grading | Ch31 898/900，`SF-2026-OPENAI-20260507-COT-GRADING` | A8＋R1/R3 Source/PRE/实际POST；note同上 |
| HJA05073 | Ch66 482/484，`SF-2026-ARXIV-2605-05073` | A10＋R4/R6 Source/最终PRE/实际POST |
| Consis05126 | Ch26 604/606，`SF-2026-ARXIV-2605-05126` | A10＋R4/R6 Source/最终PRE/实际POST |
| DP-FM05054 | Ch23 1027/1029，`SF-2026-ARXIV-2605-05054` | A10＋R4/R6 Source/最终PRE/实际POST |
| CAST04641 | Ch23 1051/1053，`SF-2026-ARXIV-2605-04641` | A10＋R4/R6 Source/最终PRE/实际POST，mask限定末输入token |
| HierVA04304 | Ch75 206/208，`SF-2026-ARXIV-2605-04304` | A11＋reader实际PRE/POST；PeakTok非总费 |
| Driver05092 | Ch25 52/54，`SF-2026-ARXIV-2605-05092` | A11＋实际PRE/POST；Table3 Δ非GT误差 |
| Stage04547 | Ch28 130/132，`SF-2026-ARXIV-2605-04547` | A11＋实际PRE/POST；γ/β schedule与分别加baseline保留 |
| DiLAST04412 | Ch24 283/285，`SF-2026-ARXIV-2605-04412` | A11＋实际PRE/POST；固定voxel/视角/优化及非几何真值保留 |

10项均有纯证据note及近正文限制/费用/回退。与已有书稿共同dirty不等本方可以重置；无其他本日新Books实际写入。

### 已交回但未完成的精确普通工作

1. **A12四Source**：Joy04128/Tab04962/CAD05031/Vocal04613仅本作者prepared；reader暂停前Joy只核§2.1–2.2、§3.1与mixture开头、§6.1–6.2及官方News直接May07日期，§3.2–3.3/Table3反侧未核；Tab已核§2.2、§3–5核心/反侧，但Limitations及AppendixB序列化/配置未完；CAD/Vocal reader核心未读，均非外部受阻。详细未核层以reader R9为准，不能将A12整批当Source通过。尚无这些项Books owner差额/PRE/实际写入/POST。
2. **root独立必要Source**：05151/05197/04899由root实际核其必要原证并给最小采用，未做Books。05151：窄单层/单seed/post-GELU SAE扩字典与top10×5干预只支持测量/任务条件下未见强功能依赖，不证明全网络无superposition、低内在维度或LLM不需要；全FFN零消融与少数latent不同。05197：50k合成语法标签、synthetic-dev选probe/层、六base LM，语法与plausibility方向不同、pair ACC/unpaired AUC与长度归一logprob分开，非英语transfer更弱；可解码不证因果使用/人类认知。作者已读相关core及Ch5现有论证，但尚无最终具体差额/评分/处置。04899：球面近似/top2局部平滑、按最终棋步变化筛4000branchpoints/737probe/最佳层与PCA选择；几何连接与probe关联不等实际施加H后的因果误差传播，Mistral更弱/方向反侧，未授sampling改进；拟Ch5/20具体对读后NC/Only，尚未决定。
3. **Story04831/UV04704**：reader小范围Source已通过；作者已独立实读Story§4.2/§5及UV§3.2–3.5相关核心，未冒全部必要附件。日期原件本作者已取：Story唯一v1 `2026-05-06T12:28:17 UTC`＋registered `2026-05-07T02:02:42.000Z`；UV v1 `2026-05-06T09:55:36 UTC`＋registered `2026-05-07T01:59:36.000Z`，两者均arxiv.content/findable，最早May07 08BJT→registered同May07单日。UV v2提交May07是另一事件，未用v2替v1。拟两项2+1+2=5，但需最终最小采用/Books对读：Story保人类chosen构造人口/偏好非普遍质量与BoN总费；UV保固定协议模板/指定slots、cross-file slice重构与原DUT验证、codecoverage非functionaltruth及20.17×排除人工IR/planning。Pro2保持C，不再继续。
4. **A9 DoG/Junk**：R6必要Source已通过，尚未具体owner/Books处置。DoG per-team priority12run不是严格top-only；manualnugget＋AutoARGUE非fullymanual，所谓max仅基准非数学上界。Junk ASR是trajectory择优、非单query，n100/B5/1e5FE/四7B/50targets/greedy及PPL非训练来源保留。
5. **正式Report**：仅6新增已先进入§3/§4；还有10项中后4、三NC及其余最终通过候选待合并。§1规模、§2本轮14来源自包含表、§5普通/外部区分、§6本轮独核汇总尚未完成；不能继承旧184完成声明。未运行本轮最终V3/全链接/DAY，暂停不为赶验收改成完成。

### 来源有限停点与保留项

- A6其余官源实际目录/停止依据继续有效；混元公共API两页实取成功、11项/空第二页，不因旧浏览器失败记整源外部。Qwen May07官方Code recap本作者已完整读core到fixes；实际机制/事件日期与成熟流程是否有新贡献尚未作最终处置，不把release号或修复标签直接纳候选。语音API/finetune兼容事实、Google impact关闭与其余官源目录缺段仍待正式表同步，不为补数量建低分项。
- **Seed分页有可执行恢复线索，不能终态隔离**：public_papers静态仅1–20/246，`?page=2`无效。暂停前实际官方JS `main.d734eb08.js`（页面88329 CDN）发现GET `/api/get_article_list_v2`，参数article_type/query/page_token/count/order_desc/publish_year/research_area_id/mode/work_team_id等；尚未确认该页调用参数/取API分页。恢复只接此路由追到May07及停止，不扫描全机构历史。未把当前API未调用写外部故障。
- arXiv官方list/API路径和主题查漏仍需有限收口，缓存1135不成为全文队列；已看但未作最终贡献处置的具名线索04916 NeuralRuleInducer/05000 COTS security等只在原有限发现内，不自动扩候选。04093 DEMM日期区间跨日、04834 ALL-IN具体更早OpenReview原件challenge（reader定点两PDF仍同challenge）继续隔离，不计确定窗内候选；04356撤回v1只原始排除、不评分/Books。日期组合有效的其他项不受两例连坐，不改旧候选归属。

### 快照截断错误与一次行政修复

暂停冻结校验发现先前baseline确受本方工具输出截断污染：开头混入`Warning: truncated output`，第610行含literal `…6471 tokens truncated…`，其旧§4仅122077字符。**此前“快照完整”的推定无效**，本条保留错误与修复历史，不静默抹除。

root明确准一次行政修复。只读核定Git HEAD与index的本日README完全同版：229876字符、184候选行、完整旧§4 144041字符；旧184行和连续§4与当前README原块逐字一致，无原有修改被覆盖证据。通过分段实取该真实HEAD原件（不从当前正文反推），apply_patch完整替换唯一[baseline](./baseline-before-supplement-20261018.md)，未新建第二份快照。修后实际核：baseline==HEAD==index；184旧行在当前README均exact-once；144041字符原§4连续完整包含；无literal截断标记。当前旧窗口/日期/评分保留。限定README/SUP及本方10项Books路径diff-check通过；此机械冻结检查不授来源/语义/DAY验收。

**恢复起点：** 用户明确恢复后fresh本日上下文完整重读当前合同→复用R1–R9/10项真实POST与三NC→重协调未执行Books范围→先接A12四Source缺段及具体owner，root三Source不无差别重读→Seed/arXiv等有限来源收口→其余具体处置→六部分合并与非作者DAY/FINAL。本轮停在暂停，不自行恢复或接下一日。

root另授权暂停期行政同步：修复baseline后在README添加显式`冻结候选日期`链接，再重跑一次V3，不改旧候选日期。已实际执行；旧184日期错误消失，但当前V3 exit1/10条格式错误：§3分批临时第二张候选表的header/separator被解析为两条材料（primary link、日期、评分、review、Books无效）。这是本作者尚未完成六部分合并的明确普通格式待办，不授通过，也不为暂停后闭环继续改表/研究。恢复合并为单一候选表即可定点修复，原184行仍冻结。README保持进行中。

## A14 用户明确恢复后：有限来源收尾与正式表同步

恢复作者：`may08_resume_author`。root转达用户明确恢复，仅重开本日May07自然日增量；独立重读当前AGENTS、Prompt、研究/Report合同、每日来源/主题、ROADMAP与LS顶部停点。复用10项已实际Books POST与3具体NC，不继承作者prepared为独核通过。仅写本日报与此SUP，baseline不再修改，Books拟文另交root审批。已把§3临时两张候选表合为一张，并同步另外4项已实际整合与3NC；未改变任何旧184整行、日期、评分与连续旧§4。

### Seed官方前端API分页（本作者实际执行，待reader范围核验）

重新从[public_papers](https://seed.bytedance.com/en/public_papers)恢复官方前端`88329/static/js/main.d734eb08.js`。实际调用代码显示：Publication=1、Blog=2；`page_token=Number(offset)||0`，count默认20，Publication附`x-tt-locale:US`；GET `/api/get_article_list_v2`，参数`article_type/publish_year/page_token/count/order_desc`。未以无效`?page=2`或静态首20项结束。

- [Publication offset0](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=0&count=20&order_desc=true)：请求count20，实际返回18项、total86、next20、has_more=true，日期从09-28到05-26；只作跨目标日的分页导航，未把全部条目建立审阅队列。
- [Publication offset20](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&page_token=20&count=20&order_desc=true)：total86、next40、has_more=true，20项日期05-16到04-15，完整跨过May07。两条May07展示项：ID1631 TDDFT Gradients，精确论文2605.06489，AI for Science范围外关闭；ID1629 Continuous Latent Diffusion Language Model，精确论文2605.06548，已在原184表与原§4有完整同事件采用，按用户要求只去重、不移动旧日期。临近ID1667=May10、ID1587=May06、ID1639=May04；停止，不翻offset40到更早历史。前端PublishDate是目录字段，不重命名为论文实际首公开，未用来覆写原候选日期。
- [Blog offset0](https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&page_token=0&count=20&order_desc=true)：未附locale，请求count20，实际返回12项、total24、next20、has_more=true，日期10-14到02-13；列表中无May07或May条目，邻接为ID2132 Seed3D2.0=Apr23、其后更早Apr09/Apr01。此页已跨过目标日，停止，不翻更早offset；不把total减count当实际剩余条数。所取日期字段原毫秒值如May07=1778083200000，转换只用于目录定位，不补造公告时刻。

本轮Seed有限检索已执行至自然日两侧，不是外部受阻；未发现需新建候选的独立May07研究家族。此记录不证明该目录收尽全部官方发布，也不把AI for Science或窗外论文送入深审。

计数纠偏：作者初稿误把请求count20当实际返回20；reader实际原响应指出Publication首18/次20、Blog首12，本条现已按原响应改正。实际跨度/停止判断不受该计数错误影响，不将不同locale结果混并为总量。

## A15 四项必要Source通过后的具体owner差额与拟文（未写Books）

R10已实际补完A12四项必要原域Source，6/6/5/5；此层不代owner/PRE/POST。作者已重新完整读取Books公共上下文与以下实际局部及交接：Ch24生成workflow/UniT两段→provisional/commit、离散采样段→continuous embedding；Ch23混合音频表示/TADA/TASTE→参考音色时间轴；Ch76多向量表示/完整late interaction及真实证据/query constraint。不存在新章/结构缺口；拟以下四个最小正文增量，**仅交root与独立reader审批，不自行写入**。

### Joy04128 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

现Ch24的workflow消费草稿以修正最终生成，尚未说明生成器可以作为理解任务的派生视角producer。拟紧接UniT关于顺序修订与并行BoN费用的末段，放在“若生成器可以把 token 从 A 改成 B”之前：

> 生成画面还可以成为理解任务的中间工作区，而不以出图为终点：先从原图提出相机位姿，再生成指定新视角，让回答者同时消费原图与派生视角。这改变的是可计算的视觉条件，不能把补出的遮挡区域当作新增实测证据；训练期的多视角一致性也不认证推理时每张图的几何。受限空间问答中，固定回答者换用不同生成器的局部对照既有改善也有退步，不能由更多视角或更强出图分数推定所有理解任务受益。位姿规划、生成、再回答和训练数据制备均付费；物体身份、几何或答案冲突时，应回读原图、真实多视角或明确未知，预算不合算则保留原图直答，不让生成器自行补齐事实。<!-- source-family:SF-2026-ARXIV-2605-04128 -->

拟末注只含精确v1 §2–3/T1–3与§6.1–6.2/T14；695题、固定GPT5回答者、Qwen-edit67.4反侧与VGGT定性边界；6分具体接口深入，未核代码/图像像素/复现。不采Joy KL正文歧义为可执行recipe。

### Tab04962 → AGENT-RAG / Ch76

现Ch76 768起已讲真实证据/query约束，但尚无训练retrieval embedding时将数值谓词真值与相似度目标分开的具体接口。拟接332节首个单/多向量trade-off段之后、完整late interaction段之前：

> 结构化行检索还要把“文本看起来相似”与“满足哪些条件”分开。可以从行构造带数值或类别条件的query，用符号检查确认正例，并选择明确违反条件的行作hard negative，再训练query-to-row表示；这改变的是候选排序的监督，不把cosine分数变成精确数据库谓词。数值精度、列名/目标列遮蔽、序列化与截断规则共同决定训练和检索身份；两位小数或宽表截断都可能改变条件本身。受限表格对照中，数值与多条件仍较难，单独训练的分类readout也不是零训练分类能力；缺少组件拆分不能唯一归因各模块。样本校验、领域训练、重编码与索引均计费；条件必须严格成立时继续符号过滤/原表执行与独立验证，域迁移或预算不足则保留通用retriever和原索引。<!-- source-family:SF-2026-ARXIV-2605-04962 -->

拟末注：exact-v1 §2–5/Limitations/AppB；6分，query-to-row/positive-aware负例与两位小数/宽表边界、每dataset readout、无组件唯一归因；未复现。

### CAD05031 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

现Ch24离散采样几何主要讲文本embedding与统一categorical posterior，没有不同离散属性的forward kernel身份。拟在“连续高斯去噪迁往离散文本”两段之后、continuous embedding段之前：

> 同为离散ID也不意味着应共享一种噪声：命令、量化坐标、有序尺寸与布尔属性可以有不同可达集合和邻近关系。一条受限结构生成分支先生成命令，再条件生成参数，并分别为坐标、尺寸和布尔值选择不同transition kernel；absorbing状态、类别支持与参数的consumer必须一起声明，不能因编码都是整数就给任意符号加同一Gaussian噪声。这增加多种kernel、分阶段训练与采样费用，有限CAD对照中的有效率、Chamfer和分布覆盖仍有反侧，更多步数也非单调改善。可执行几何只是当前验证器的结果，不是任意约束、背面或可制造性保证；核定义或条件支持不清、质量/费用不合算时，保留统一基线、显式语法和独立几何验证，不将论文中未闭合的范围/局部mask表述补成精确实现。<!-- source-family:SF-2026-ARXIV-2605-05031 -->

拟末注：exact-v1 §III–V/Eq1–17/Alg1–2/TII–VII；5分，核身份/command与参数分解具体差额深入，保global-only invalidity更好与unified范围/ζ局部mask疑点；未核artifact/复现。

### Vocal04613 → MULTIMODAL-REPRESENTATION / Ch23

现Ch23 TADA/TASTE是文本索引的声学生成或预测坐标，还没有将歌词先验与逐词音符对齐交给结构化转写consumer的输出接口。拟放在TASTE两段之后、“参考音色与目标事件时间轴”标题之前：

> 文本也可以先作为结构化音频转写的输出scaffold：先从音频生成整段歌词，再在该prefix之后交错输出词、音高与时长，已有歌词时可跳过第一步。它改变的是与预训练分布相容的输出factorization，不证明模型执行了自由文本推理，也不保证前后两份歌词严格一致。词、音符、duration与单个global BPM应分别交给后续消费者，global BPM不能表达任意rubato；歌词错、teacher伪标签或语言失配会继续传播到对齐。额外前缀解码、伪标注、全量微调与验证均付费；受限中文歌声中WER与音高并非处处优于基线，使用真歌词/外部时戳的对照也不能混同audio-only。内容或时间轴不可靠时，保留人工歌词、专用对齐/转写器及独立音符核验，不由下游合成听感批准转写为真。<!-- source-family:SF-2026-ARXIV-2605-04613 -->

拟末注：exact-v1 §3–6/T1–3/AppC/D；5分，lyrics-prefix/interleaved结构接口差额深入；保pure/interleaved无hard一致、单BPM、Mandarin/teacher、ASR/AMT非等条件和下游训练混杂；未核artifact/复现。

以上回退/验收建议为本项目推断，不冒称论文已验证接口或生产能力；等待root明确窄写许可及非作者逐字PRE。

**A15实际落实：** root恢复后仅授三文件四指定单段与本人纯note窄位，reader实际owner/完整邻接/逐字PRE通过后，作者已真实保存并完整self-read：CAD→Ch24 530、Joy→Ch24 1149、Vocal→Ch23 532、Tab→Ch76 339；四本人note均在各章Review notes内。限定diff-check通过，等非writer实际POST；未将Source/PRE当已POST，不添流程标签。

## A16 三root必要Source复用后的具体Books决定

必要原证层复用root暂停前实际阅读及A13保留的精确最小命题，不从旧作者笔记替代原文；本作者恢复前后已实际读相关core和Ch5局部，恢复reader另独立对读Ch5 214–242、348–378、272–274，不冒认其重复完成三篇Source。三项日期仍沿R2逐原件组合May07，不变旧日归属。

- [05151v1](https://arxiv.org/html/2605.05151v1)，2+1+2=5，受反证信号触发的必要深入完成。只采用窄PatchTST单层/单seed/post-GELU SAE扩字典与top10×5局部干预未见强功能依赖；整FFN清零与少数latent不同，不以失检证明全网低维、无superposition或LLM不需要。**已有覆盖：WORLDVIEW-REPRESENTATION / Ch5** 218明说“可以”共享而非普遍必要；220把probe/decomposition限为行为投影，226要求声明reader类/输入/误差且probe失败不反推无信息。234–240共享方向干扰是条件分支而非全任务必要性命题。受限反例与具体实验留报告，不为此重复正文。
- [05197v1](https://arxiv.org/html/2605.05197v1)，2+2+2=6，标准完成。采用50k合成标签、synthetic-dev选probe/层、六baseLM及非英语transfer较弱的局部语言表示证据；pair ACC与unpaired AUC、length-normalized logprob不同，不把可读语法等同causal使用/人类认知。**已有覆盖：WORLDVIEW-REPRESENTATION / Ch5** 350把存在/独立reader/实际使用拆开，358的fresh probe只减少循环性，360–364又分logits/argmax/最终行为与干预损害。likelihood与grammar/plausibility的具体跨语言结果留报告，不声称书中已有该论文的每项实验。
- [04899v1](https://arxiv.org/html/2605.04899v1)，2+1+2=5，标准完成。球面/top2局部平滑、按最终棋步变化筛4000branchpoints/737probe、选最佳层/PCA，只有几何连接与probe关联，未实际施加H识别误差传播；Mistral更弱/方向反侧保留。**仅报告**：该受限几何/棋步相关不支持新的sampling控制或通用世界模型主张，Ch5 272–274已经把softmax-KL几何、可达/分解前提及probe路径失配与实际行为分开；不把条件类比写成新的工程recipe，不新增书稿。

## A17 UV与Junk两个具体差额拟文（未写Books）

Story04831与DoG04458的窄必要Source沿R2/R3/R6，reader另已实际对读具体owner，作者同样实际读回：Story→Ch66 466–474三种判别/self-PIR/Null-PIR及来源/质量/候选构造、506–508用户/judge不同轴；DoG→Ch66 1674–1698 inventory与support/coverage/来源/Unknown、2746–2751逻辑依赖/normalizer及rank agreement不等真值。这两项拟具体**已有覆盖**（Story5、DoG6），仅各最小命题，不声称所有创作偏好或QA/SVM算法已入书。Source反侧、人类chosen混杂和12-priority-run定义保留，未因NC改分。

### UV04704 → AGENT-TOOL-CALLING / Ch78

作者实际完整读取Ch78 compiler/provisional sealor→执行模拟器→Rust真实trace→Tool Discovery邻接，现未承载dependency-preserving输入slice与最终原对象执行的区别。拟紧接真实Rust trace完整段之后、Tool Discovery标题之前插入：

> 提案输入也可以比最终执行对象小：面对多文件设计，从未覆盖信号向可控制输入递归追踪依赖，保留跨文件相关片段供模型生成刺激，并把协议固定流程留在模板中，只允许模型填指定slots。这个slice是生成上下文，不是已证明等价的新设计；刺激仍必须回原始DUT模拟，不能以在删减对象上通过替代原系统覆盖。依赖解析、slice重建、协议库、生成与多轮模拟均付费，语法修补也不恢复遗漏语义；有限协议/六设计的code coverage和人工waiver不等functional正确性，排除人工IR/planning的局部加速不能写端到端无人验证。依赖或协议失配、验证不足时，应保留原设计、完整输入、人工IR及原模拟/功能断言，不让压缩后的context签发执行真值。<!-- source-family:SF-2026-ARXIV-2605-04704 -->

拟末注：5分；exact-v1 §3.1–3.6/§4.1–4.7，固定协议/指定slots及FilteredDUT归原DUT，保coverage/waiver与人工IR成本；未核代码或复现。reader必要Source/日期通过，逐字PRE及root窄写未授。

### Junk05116 → PLATFORM-SECURITY / Ch72

作者已读Ch72 785–798的结构化红队搜索/PPL/best-of限定及3129–3135的selected attacker预算，缺无显式指令的输入支持边界和训练来源归因分开。拟接SF2603-20122红队搜索完整段之后、良性反事实切片之前：

> 威胁输入也不必包含人类可读的攻击意图：受限白盒测试可搜索无显式指令的token序列，再独立检查输出是否有害且连贯。命中某个target prefix不等harm，整条优化轨迹事后择优的成功也不是一次最终query或随机字符串的成功率；测试身份必须保留目标模型、概率访问权限、搜索预算与外部裁判分母。高perplexity只说明相对某参考分布异常，不证明预训练何时形成了这种响应，更不能由“自然后门”命名认定训练植入因果。搜索、目标求值与独立harm/coherence审计都付费，四个7B和有限目标不代表更大/闭源或强防守系统；不能以没有可读指令作为放行条件。条件未知时保留固定经核验的红队suite、明确未知和独立输出/effect gate，不由一次异常样例签通用风险率。<!-- source-family:SF-2026-ARXIV-2605-05116 -->

拟末注：5分且安全反侧必要深入；exact-v1 §2/§4–5/Table1，四7B/50目标/轨迹择优，PPL非来源因果；不写可执行攻击配方、未复现。reader R6必要Source有效，逐字PRE及root窄写未授。

## A18 有界发现的最后具名处置

这些对象均为A13已有有限发现，不扩1135宽缓存为待全读队列。

- [NRI 2605.04916v1](https://arxiv.org/html/2605.04916v1)：作者实际§4–5、reader恢复后实际§3–6/AppA–D，准入与必要Source通过，2+1+2=5。predicate-specific重训约束→literal统计接口＋example-conditioned分支恢复support、parallel clause slots及product T-norm→预训练归纳器的任务接口与可读规则正确性需分验。18统计不充分，aux固定raw维度扩展随机新权重，非严格schema/置换不变；多clauses逻辑匹配下降，prediction85–100%不等24%logical match。Table1 mean69.7/EBM82.7与Table2 full74.8人口/seed协议未统一，不报全面增益；CF flip是已选rule敏感性，不识别真实因果。AdamW/8192batch/500steps只训练设置，不授净推理加速；14 UCI只验证sparse bounded DNF支持，标签/离散化/预训练成本保留。日期作者与reader均独取：唯一v1 May06 13:45:31UTC，arxiv.content/findable、registeredMay07 02:04:48Z，最早May07 08BJT→最晚10:04:48BJT同日，v2另事件不替代v1；未见当前撤回/勘误警告。owner拟文下一节，不先采其全性能/不变性强主张。
- [SLYP 2605.05000v1](https://arxiv.org/html/2605.05000v1)：作者实际完整v1题摘/Introduction与§4.2–4.5，不用当前v2的64entry/39zero-day数字替v1的20COM/40case/28zero-day。标准ReAct、外部checkpoint/memory、stop verifier及COM/MCP/动态debugger的领域工具组合，局部工具可用性比较未披露超出现有执行验证/状态保留的新通用成立条件；拟贡献关闭，不评分/不进入候选。crash stack回到原目标提供局部验证，不是通用安全认证；reader仍需必要安全反证核验，不因C省略。有兴趣的系统关联不单独入选，未独核MSRC/CVE实现或复现攻击。
- [Qwen Code May07](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-05-07/)：作者实际完整core/Important Fixes至Other Changes，reader另实际核具名PR正文/补丁与日期。#3525 parser streaming state重置、#3550 converter per-stream/request context确为真实correctness变化，但两PR created/merged在Apr22–24；#3615由拦全部workspace外path改absolute executable可用、relative escape仍检查，并将requestUserConsent换workspaceTrust，createdApr25/mergedApr30，不可称权限更强或所有动作均有独立同意。三者都不是May07新纠错事件。该周报仅历史兼容/产品recap关闭，background面板/rewind/review/cache等未另披露改变长期设计的机制；不将一周所有release/linkedPR都搬为May07首公开，也不逐PR扩扫或冒称安全复现。
- [OpenAI voice API May07](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)：作者实际官方core各三模型/功能与Safety/Pricing，发布GPT-Realtime-2/Translate/Whisper，公开reasoning effort、parallel tools、128K等接口与受限语音成绩，未披露新训练/流式计算机制和足以归因架构的对照；产品例子、分数及语音流畅不证明实测生产SLO。当前发布作为来源背景关闭，不评分/不进入候选，安全classifier会停止某些session仅官方能力说明、不授防护完备性。
- [OpenAI self-serve fine-tuning资格更新](https://developers.openai.com/api/docs/deprecations#update-to-openais-self-serve-fine-tuning)：May07直接通知限定新org不得创建训练job，既有微调模型推理直到base退役，并列Jul02/Jan06后续计划。它实际改变外部training service可用性，不是新优化算法或“所有微调模型立即停止”。2+1+1=4，必要兼容性原文深入完成，**仅报告**；不将后续计划冒本窗已发生，也不将当前页面当不可变历史状态。Book稳定训练原理未变，不新增vendor日程正文；reader必要原件/日期/处置仍待独核，不因分低跳过。

## A19 NRI的最小owner拟文（未写）

作者已实际读Ch5 92–100的关系重标记→discrete primitive/codebook与executor→task embedding两阶段适配及前后交接。现文没有“用标签条件统计表征literal，再由example-support补足边际统计损失，生成显式规则”的输入接口分支。唯一owner WORLDVIEW-REPRESENTATION / Ch5；拟接SF2604-18907完整段后、任务表示测试时优化段前：

> 可复用的归纳器还可以不把参数绑定到固定predicate名称：先从带标签例子计算每个literal的条件频率、熵和共现，再用具体样本的support补足仅边际统计无法区分的覆盖关系，最后以并行clause slots提出显式规则。训练时用可微逻辑执行让预测反馈到规则生成，部署离散化后仍需分别检查预测正确与规则逻辑匹配；前者很高也可能对应错误规则。这个接口只在可表达的稀疏有界DNF、离散化和训练支持下得到局部证据，不保证全部Boolean函数或任意schema迁移；辅助样本分支仍依赖固定输入维度，扩展时的随机新权重也不构成不变性证明。合成任务制备、标签统计、预训练、attention与规则核验均付费，统计失配、复杂度超预算或跨域结果不稳时，保留逐任务规则学习、显式搜索/执行与独立held-out测试，不让可读规则自签正确或真实因果。<!-- source-family:SF-2026-ARXIV-2605-04916 -->

拟纯note：exact-v1 §3–6/AppA–D；5分，statistical/example-conditioned/parallelDNF受限接口；保aux维度随机扩展、logicalmatch与accuracy分离、Table1/2口径未闭与全费；未核代码/复现。不采用全任务transfer/strictpermutation/泛化速度或医学应用结论。reader必要Source通过；逐字PRE/root窄写未授。


**A17/A19实际落实：** UV→Ch78、Junk→Ch72、NRI→Ch5均经root指定窄位与reader实际owner/完整邻接/逐字PRE后保存、自读；reader R14/R15随后实际新增/两侧/本人注POST通过，三窄位释放。累计17真实新增Books整合，不等日级验收。

## A20 arXiv有限查询实际恢复（不是219项审阅队列）

月列表cs.CL/cs.AI `https://arxiv.org/list/<cat>/2605?skip=0&show=2000`经HTTP与web均404，不作零命中。正确urlencode后legacyAPI可读，未把先前失败直接终态隔离。入口`https://export.arxiv.org/api/query`，共同参数`sortBy=submittedDate&sortOrder=ascending`，四式均AND连接`submittedDate:[202605051800 TO 202605061800]`。submittedDate仅发现线索，不冒充公开日期；完整含May05晚6小时。原May07的160候选与本日报旧184仅按ID去重，不重审有效层。

| 查询 | 精确主题表达 | 实际分页与停止 |
| --- | --- | --- |
| LM | `(cat:cs.CL OR cat:cs.LG OR cat:cs.AI) AND (all:"language model" OR all:transformer OR all:"foundation model" OR all:MoE)` | 初取start0/max100=100、start100/max100=49/total149；最终串行start0/max200实际149=total，完整停止 |
| MM | `(cat:cs.CV OR cat:cs.RO) AND (all:"vision language" OR all:"world model" OR all:VLA OR all:diffusion OR all:"generative model")` | start0/max100=42/total42；最终start0/max200实际42=total，停止 |
| SYS | `(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:GPU OR all:kernel OR all:accelerator OR all:inference)` | start0/max100=18/total18；最终start0/max200实际18=total，停止 |
| IR/MA | `(cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:RAG OR all:agent OR all:memory)` | start0/max100=24/total24；最终start0/max200实际24=total，停止 |

最终串行块间隔≥3.1秒，结束已向root释放legacyAPI请求ownership；初次并发发现不作为后续节奏。四query共**233含跨query重复命中，按无version arXiv ID去重219唯一线索**，不是219当窗论文或候选，也不扩为全量题摘/全文关闭队列。当前API可返回后续revision，必要Source仍取精确v1、日期仍逐原件；旧日不迁移。四搜索式web补检无结果只记辅助检索受限，不推零遗漏。

有界题摘只接实际主线相关、尚无有效同事件处置的具名：04505 JASTIN、04556 MSEB、04733 EBM-RL、04759 Gyan、04906 Strat、04566 editing-model perception、04609 Composer、04662 Contact、05163 PhysForge。明确医学/材料/科学应用、通用推荐/多agent控制等题名而无模型/系统新机制线索者可范围关闭，不因API返回全读。上述九项作者实际逐DataCite原件均为arxiv.content/findable；唯一v1都在上述带内，registered分别May07：04505 01:54:49Z、04556 01:56:05Z、04733 02:00:19Z、04759 02:00:57Z、04906 02:04:34Z、04566 01:56:19Z、04609 01:57:20Z、04662 01:58:36Z、05163 02:10:46Z；最早May07 08BJT→最晚各registered同日，仅限定arXiv公告，不证明全球首稿。精确UTC提交：04505 May06 05:18:42、04556 06:58:45、04733 10:32:23、04759 11:06:30、04906 13:35:14、04566 07:11:50、04609 07:56:16、04662 09:10:07、05163 17:33:23。

另五具名有潜力但资格跨日（已读完整题摘/元数据，不先评分/计本窗）：05285 v1May06 17:38:13Z/registeredMay08 02:06:39Z；08200 v1May05 22:27:05Z/registeredMay12 03:43:42Z；08201 v1May05 22:50:43Z/registeredMay12 03:43:43Z；08215 v1May06 11:21:25Z/registeredMay12 03:44:05Z；08218 v1May06 13:21:24Z/registeredMay12 03:44:09Z。作者实际均确认arxiv.content/findable，但不能把registered单点当May07或反向迁日。所需替代是精确v1当日官方公告/可复查直接日期原件；只重开对应家族资格，不否定同日有效组合。

## A21 有界新增准入与必要Source（分层实际范围）

新校准不回溯重审旧有效候选。Gyan04759经reader实际§2–4/AppA/C全部pipeline与§5/7核验后贡献关闭：目前披露只是RST/AMR/ontology/rule-NLP→GMR/KS grounding/检索组合，没有给出改变具体设计的新编码/推断规则或受控证据；不是因proprietary、不开源或医学数据而关闭。不采完整可逆、无hallucination/world-model/negligiblecompute宣传，§7无固定workload成本。仅留原始筛选，不评分/入Book。

### EBM-RL 2605.04733v1

2+1+2=5；作者实际§4/Eq1–13、§5/Tables1–5/5.4–5.5，reader另§3.2/AppH/K/M必要反侧。frozen-reference对同一GT next utterance在有/无perception+think前缀的mean-token LL差是PCG，不能把这个代理变成真实视觉grounding或推理因果。CLIP帧相似/语义BERTScore/format/PCG四维各在同prompt group内归一后加权；格式不是硬正确性门，标签名不证明内部人类cognition。Qwen2.5VL7B、2.3k SFT warm-up近3epoch＋8H800 RL1epoch、movie/session分割与GPT5-mini judge人口固定。Table2 SPC对38B反退、Table4权重tradeoff，Table3人评相关只有四系统aggregate，不能当逐样本独立gold；OOD只是三个所测VideoQA子集。PCG重复scoring、warmup/RL/额外tokens成本保留，未复现。拟**已有覆盖 TRAIN-GRPO / Ch33**：129各信号人口/尺度分别归一，348–350已知target likelihood差/特权目标，2062 frozen-verifier有/无条件mean-tokenNLL不授真实grounding；reader具体owner待核，不说已含电影配方。

### Strat-Reasoner 2605.04906v1

2+2+2=6；作者实际§4/Eq4–10/§5/Tables1–2/5.4–5.5，reader另AppC/E必要设定。CTDE训练特权读取opponent自述字段与相邻实际action，baseLM judge只评分对应文本/行为匹配，不是获取真实心理。每turn重采M个current-step reasoning/actions，不继续counterfactual未来，统一对照主轨迹opponent过去/未来；所以局部分数不是各备选action的真实反事实价值。CoT按本turn微组归一，return按role batch仅中心化，再加权混合，不是同人口无偏advantage或已证减方差定理；M2/std零guard未闭，不补recipe。Qwen3-4B/r16/BF16/2A800，>500games只局部，Table1 second-mover/mini反侧与同角色优势保留；rollout占50–60%、0.3–0.7GPUh/globalstep、MiniHanabi约100h，不称免费CTDE/微采样。拟Ch33具体信用人口差额一段，未写。

### Composer 2605.04609v1

2+1+2=5；作者实际§3.1–3.6、§4.3/4.4、§5及Table3–5必要对照，核心§4.1主表/精确实现设置仍由reader独核。结构条件用大核模糊/局部差、颜色用模糊SLIC，以抑制细语义而非保证语义独立。两个condition encoders保留独立与可重权，latent互调后共享ControlNet主干；节参数与控制冲突是同一取舍。reference可由CLIP候选＋LVLM挑选，也可text-only另训规划，不能混成一个免费能力。Dual的结构/色cycle loss更好，Union在部分偏好代理/步吞吐更好，不以美学分签精确复现条件。SD1.5/XL两个训练产物与原文2M制备、GT条件、不同resolution分阶段、规划/50step/decoder全费保留；7.7秒含3.1秒planning是局部披露非生产SLO。拟Ch24低信息condition/共享控制分支，未写。

### Contact Matrix 2605.04662v1

2+1+2=5；作者实际§3–4/Eq1–12/Tables1–3与25人10组选取评价，reader必要原域独核待。四body-part codebooks经joint decoder缓解边界不一致；leader给定、follower相对位移避免沿自身预测积累global drift，另有23joint contact表示（手指合并）。diffusion共同生成pre-quantization motion/relative/contact latents，再量化解码，predicted contact只提议joint-distance guidance，不是新观测/真实接触。Eq9把epsilon/score近似混写，不采用为精确采样recipe。DD100仅3.24h/五对dancers/80–20随机split，heldout dancer/song与总运行费用未披露；single/separate/PartFusion同epochs但leader MPJVE独立part更好。Table2 w/o guidance FIDcd3.41优于full8.01，full FIDk亦非最好，不能复述allbest或安全物理约束。额外VQ/音频encoder、diffusion、decode-gradient guidance费用保留；拟Ch24共同producer/约束分支，未写。

### PhysForge 2605.05163v1

2+1+2=5；采用命题仅结构化3D生成局部接口，不把可联想到的机器人/仿真任务计入System Reach。作者实际§3.1–3.3/§4.1–4.3/Eq/Tables1–3及Table4文字对照，readerTable4数值/必要设置独核待。150k PhysDB主要属性/类型，不含全量精确axes；训练另加PartNet/InfiniteMobility的真实articulation标签。VLM计划part bbox/parent/joint-type，连续origin/axis/limits由独立MLP编码的8D KineVoxel在geometry middle transformer共同CFM生成，type embedding是真正跨阶段接口，不把VLM文本当精确物理参数。200/1000/1000/340对象人口、GT mask/part-count差异分别保；normalized CD/F1、CLIP text属性/axis/pivot proxy与示例导入RoboTwin不认证真实物理、collision稳定/任意VLA执行。全planner/voxel编码、额外标注/数据训练、joint/geometry网络与采样成本保留；拟Ch24 static articulated asset生成接口，非Ch25动力学或Ch26动作许可。未核代码、像素/仿真运行或复现。



## A22 四项具体owner差额与逐字拟文（未写）

五篇新必要Source当前均由reader实际独核，见R16以后相应原域范围；其中EBM拟NC，Strat/Composer/Contact/Phys各有下述局部差额。作者已实际读Ch33 group人口/尺度与speech/text两段→多mode，Ch24 style残差/约束→DiLAST、hard投影→rigid-parts assembly→training-only collision邻接；Books公共上下文沿恢复前完整读取且未变化。只申请下面四段与各纯note，未授写入不先改书。

### Strat04906 → TRAIN-GRPO / Ch33

拟接speech/text分别中心化的两段之后、多reasoning-mode段之前；现文未承载训练可读对手CoT与不分支未来的微组评分/role-batch return混合：

> 多智能体训练还可同时使用两种不同人口的基线：每轮从同一状态重采若干推理与动作，用对手相邻轮的自述字段和主轨迹实际行动评分，在该微组内归一；长期return则按角色的训练batch中心化，再混合两种信号。对手CoT是训练期特权文本，不是其真实心理，也不自动在部署可见；各候选没有继续各自未来，却共用主轨迹对手的后续行动，因此匹配分不是这些动作的反事实价值。这个设计换来更密的训练proposal，不获得无偏advantage、普遍减方差或保持均衡的保证。额外重采、judge与多轮训练均付费，有限游戏与行动顺序也存在反退；微组常量、对手/角色变化或终局质量回归时，须明确零方差处理并保留原outcome训练、固定评测对手与独立行为验收，不把更高CoT匹配当战略正确性。<!-- source-family:SF-2026-ARXIV-2605-04906 -->

纯note拟：6分；exact-v1 §4/Eq4–10/§5/Tables1–2/AppC/E；Qwen3-4B/LoRA16/BF16/2A800、MiniHanabi约100h，micro不分支未来、主轨迹/CoT特权、角色/零std边界与反侧；未核代码/复现。

### Composer04609 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

拟接2609-21242 style residual/cap完整两段之后、DiLAST段之前；现文没有粗结构/色块双编码保重权与共享ControlNet主干的具体取舍：

> 参考图的条件还可先压成粗空间结构与色块分布，而不直接传递完整对象特征：模糊、局部差与聚类降低细内容信息，再以两个独立encoder保留各条件可重权的入口，经互调后共享生成控制主干。低信息并不保证语义已严格消除，两路也可能冲突；区域mask与权重只提出取舍，不签发独立控制。受限对照中，双独立主干能更好保持结构/颜色cycle指标，共享主干则在部分美学/文本指标和步吞吐更好，不能把它写成全质量支配。条件制备、参考检索/规划、训练和完整采样都付费，另训的text-only规划也不是免费能力；参考不合、细边缘丢失或预算不合算时，保留独立控制分支、显式edge/布局条件或普通prompt，以条件保真与生成质量分别验收。<!-- source-family:SF-2026-ARXIV-2605-04609 -->

纯note拟：5分；exact-v1 §3–5/Eq1–7/Tables1–5，SD1.5/XL产物分开，2M制备/50DDIM/7.7秒未披露hardware；保Dual cycle更好、FID与ImageReward反侧及非strictsemanticfree；未核代码/像素/复现。

### Phys05163 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

拟接rigid-parts assembly 2505-00426完整段后，下一Contact新段前/原training-only collision段前；现文保持旧parts/rigidpose，不同于新生geometry与joint参数同产：

> 若目标是生成新的可动asset，而不是在旧parts上只改刚体pose，可以先让规划器输出part层级、bbox和离散joint type，再由独立小编码器把连续origin、axis与limits送入geometry的中间生成空间，共同去噪后分别读回。离散type是两阶段的条件接口，不是规划文本已经提供精确数值或物理真值。大规模属性数据未必有准确轴参数，仍需另行的关节标签、数据配对与训练；标注、规划、体素/参数编码和共同采样都付费。受限对象集上的形状、axis/pivot与文本属性指标，以及示例导入模拟器，只验证各自接口，不认证真实质量、碰撞稳定或机器人任务成功。结构/关节支持不明、生成或费用回归时，应保留原asset、人工rigging/测量、独立几何和动力学核验，不由可导出的蓝图直接批准动作。<!-- source-family:SF-2026-ARXIV-2605-05163 -->

纯note拟：5分；exact-v1 §3–4/Tables1–4；仅qual-type→8Dkinematic/geometry共同生成，PhysDB无全量精确axes、另加PartNet/InfiniteGT，mask/part-count人口与proxy非真实物理保留；未核代码/仿真运行/复现。

### Contact04662 → MULTIMODAL-GENERATIVE-PARADIGMS / Ch24

拟接上面Phys新段后、原2605-00517 training-only collision段之前；现文没有contact本身也是生成producer、再消费其预测的guidance：

> 运动中的接触也可以作为共同生成对象，而不预设为干净外部条件：将follower的局部motion、相对已给leader的位移及接触矩阵分别编码，在量化前的连续latent中共同去噪，再量化解码；预测接触还可提出关节距离的采样修正。相对位移减少由自身全局平移积分带来的误差积累，却依赖已给leader坐标；生成的接触不是新增观测，也不覆盖全部碰撞或动力学约束。有限双人数据中，contact/guidance与重建指标有不同取舍，去掉guidance反而能改善部分交互距离分布指标，不能以接触率上升认证物理正确。多套codec、音乐编码、解码和梯度修正均付费；接触预测、坐标或净预算不稳时，保留无guidance采样、显式外部约束及独立geometry检查，真实动作仍交controller验收，不照录未闭合的epsilon/score公式。<!-- source-family:SF-2026-ARXIV-2605-04662 -->

纯note拟：5分；exact-v1 §3–4/Eq1–12/Tables1–3；prequant联合latent/生成contact与guidance分责，Eq9 sign/scale未闭不采recipe；保w/oGuidance FIDcd3.41<8.01与leaderMPJVE反侧、3.24h/五对dancer/randomsplit、全部费用；未核代码/像素/复现。

04505 JASTIN、04556 MSEB、04566 editor-perception由reader先独立发现具体评价增量，作者已读完整题摘并据必要Source与具体owner对读继续；不能以“新benchmark/新editor”标签贡献关闭。三项均拟5分，完整证据/现有承载或具体差额待该批最终对读后并入。

**A22实际落实：** root精确窄授与reader逐字PRE后，四段/本人纯note已保存；reader R18真实新增/完整直接两侧/本人注POST通过，Strat Ch33、Phys/Contact/Composer Ch24四窄位释放。累计21真实新增Books整合；这不是DAY或最终候选分母。

## A23 Ch23两项评价接口差额与逐字拟文（待PRE/租约）

作者实际完整对读Vision Banana共享RGB输出/固定parser及评价两段（421–425）→连续表示入口、S2R直接audio/document表示及WER/MRR两段（1374–1376）→Representation collision。两处已有主张保留，不重复写WER或RGB协议。必要Source沿reader R16/R17实际原件复用，作者此前已读完整题摘/主要设置，不冒已逐表独读。

### MSEB 2605.04556v1 → MULTIMODAL-REPRESENTATION / Ch23

2+1+2=5；现文没有native audio、级联与GT text比较的信息权限和小gap双低分混杂。拟在S2R第二完整段/marker后、Representation collision标题前：

> 比较语音与文本检索时，还要先固定各分支实际能读什么：native audio直接消费声学输入，cascade只消费ASR生成的文本，GT transcript则读取人工给定的词面参照；三者不是同一信息条件下只替换encoder。小的audio/text差额也可能来自两侧都差，不能据此签发模态保真；人工文本分支有自己的表示与检索失败，亦不是任意音频系统的数学上界。受限对照须把原声、转录来源、模型/检索接口与语言人口分账，不由某一个gap或错误率代签整体质量。多分支编码、ASR与索引/检索评价均付费；信息权限或排序质量不匹配时，保留各自基线、原声与可校订文本，以真实消费者的结果分别验收。<!-- source-family:SF-2026-ARXIV-2605-04556 -->

纯note拟：Daily2026-05-08补May07；[exact-v1](https://arxiv.org/html/2605.04556v1)§3/6及setup、相关Tables必要域；5分，native/cascade/GTtext权限及双低gap局部差额深入。保same-WER不同retrieval、固定模型/语言人口、GT非数学上界、全部费用；不采contamination因果或普遍语音保真，未核代码/复现。

### Editor perception 2605.04566v1 → MULTIMODAL-REPRESENTATION / Ch23

2+1+2=5；新评价边界不是editor名称/图像好看，也不以已有RGB协议代替逐图GT侧信息。拟在Vision Banana第二完整段/marker后、连续表示标题前：

> 不更新模型权重，也不等于评价没有使用监督侧信息：逐图用GT拟合depth的affine尺度、用少量校准样本选择normal的坐标轴约定，或先给出当前图确实存在的类别清单，都改变了输出consumer的可读权限。这些结果必须与完全未知尺度/坐标/类别的部署分开；模型是否提取了视觉内容、生成器能否输出约定格式、parser与GT校准能否恢复对象是三项责任，不能从合并后的分数反推任一项已经可靠。受限编辑模型评价还会受palette/解码失败与难解任务排除影响；校准数据、额外生成和解析全部付费。缺少合法校准、输出不可解或原能力回归时，保留专用感知head、明确坐标/类别协议与独立无GT侧信息评价，不由zero-shot标签批准真实几何或下游行动。<!-- source-family:SF-2026-ARXIV-2605-04566 -->

纯note拟：Daily2026-05-08补May07；[exact-v1](https://arxiv.org/html/2605.04566v1)§3.1–3.5/§4及Tables2–4/Limitations；5分，无FT与GT-side calibration不同权限局部差额深入。保depth每图GT affine、normal48约定/5校准样本、oracle-present-classlist、palette/decoder混杂与instance segmentation排除，不外推无需监督/物理真值；未核代码/像素/复现。

## A24 七个跨日资格的有限原始替代恢复与本轮停止边界

2026-10-18恢复后实际执行；不是因字段单独不足或暂停直接终态。共同最早界均为May07 08BJT，registered最晚界跨May08/12，原始字段不改名。作者逐官方abs、v1 submission history、v1 HTML内作者项目链接核验（08218 HTML404但abs可读），并取精确ID/完整题名搜索及有线索作者机构域补检；搜索结果只作线索，不采第三方Published/Submitted。arXiv cs.LG May官方目录完整URL `https://arxiv.org/list/cs.LG/2605?skip=0&show=2000`实际失败，与此前CL/AI404同样不能证明无条目；已成功的A20主题API不因这个失败撤销。此处无新legacyAPI请求，不再占其ownership。

| 精确对象 | 原始v1 UTC / registered UTC（arxiv.content、findable） | 实际有限替代与结果 |
| --- | --- | --- |
| [05285 attribution continual](https://arxiv.org/abs/2605.05285v1) | May06 17:38:13 / May08 02:06:39 | abs/v1无作者项目；精确ID与完整题名＋Liu/May07、作者机构域检索只回arXiv/索引/后续综述，无确定日级正文公告。与May09只共享日责线索，不建第二候选 |
| [08200 VRP](https://arxiv.org/abs/2605.08200v1) | May05 22:27:05 / May12 03:43:42 | 作者[官方repo](https://github.com/itsloganmann/VLM-Reliability-Probe)区分ICLR不同题Visuals Lie与当前ICML题；README history Mar03/May04及June16只是版本/相关稿线索。[fyDhQ2dKdw](https://openreview.net/forum?id=fyDhQ2dKdw)forum challenge、api2 notes HTTP403，未得到确定exact事件日，不按ICLR名目默认重复 |
| [08201 weak concepts](https://arxiv.org/abs/2605.08201v1) | May05 22:50:43 / May12 03:43:43 | abs/v1无作者项目；完整题名/作者与机构域检索只有索引及另题后稿，未获得确定原稿日；不拿另题Aug稿迁回本日 |
| [08215 T3VF](https://arxiv.org/abs/2605.08215v1) | May06 11:21:25 / May12 03:44:05 | [官方T3VF](https://github.com/sangwu99/T3VF)README初commit e612cc4e018d May04 12:43:58Z仅代码同题说明，无paperlink；June04 2ec2d580861c才加paperlink。代码提交不是正文公开日期。具名[OpenReview fqxaTf0kjM](https://openreview.net/forum?id=fqxaTf0kjM)api2 notes403，没有May07原稿日证 |
| [08218 LVO](https://arxiv.org/abs/2605.08218v1) | May06 13:21:24 / May12 03:44:09 | abs无作者项目/HTML入口，试精确v1HTML404；精确题名/作者及机构域只得到索引/未带日作者介绍，没有可复查May07日告，不采用机器模拟rebuttal |
| [08209 LSAMD](https://arxiv.org/abs/2605.08209v1) | May06 09:13:29 / May12 03:43:56 | abs/v1无真实项目（des-nets.experiments是排版误链）；完整题名/作者机构域未得带日作者原件。reader实际Method/Experiments/T1–4/AppC确认初始化选择接口有潜力，故撤销泛“NAS组合”贡献C，先资格隔离、不评分或入Book |
| [05253 EnterpriseRAG](https://arxiv.org/abs/2605.05253v1) | May05 20:23:38 / May08 02:05:53 | [Onyx官方项目](https://onyx.app/enterpriserag-bench)无日期、citation称Draft；[官方仓](https://github.com/onyx-dot-app/EnterpriseRAG-Bench)createdFeb19只仓龄。README commit137dd5146925 May05 08:58:18Z“Add paper pre-submit arxiv”换paper.pdf链接，实际新增enterpriserag_bench_paper.pdf，May08 d36685e27371再加arXiv；reader R22已通过urllib实际恢复删除前历史MD同题/完整摘要、GoldSetCorrection与ComparativeEvaluation完整两节及baseline表，本次最小参照更新贡献已在该稿存在；不能称必要正文全不可得或未比同题。未核历史PDF全部，committer并非public-visibility/首公开证据，尚无确定May07日告。reader实际§4–7及Tables6–7发现release gold vs pairwise union correction、short-circuit/gold-biased tie与required/valid/invalid分责，撤销仅新corpus C，先资格隔离 |

GitHub具名历史实际入口为 `https://api.github.com/repos/<owner>/<repo>/commits?path=README.md&per_page=100`，返回7/6/3个README commits，完整到初commit停止；仅进一步取上述具名commit元信息/README patch，不核实现或扩大PR队列。OpenReview网页与api2两条必要替代均失败；不以一次失败外推全站。未以仓库created、git committer、搜索爬取或当前无日期页面认证正文首次公开；这些具体早稿线索一并保留供准确恢复。当前可用原始入口已作上述有限尝试，七项不进入确定May07候选、不用于Books或无遗漏；需要exact-v1官方日公告、带日期作者正文release，或能确定公开版本与时间的原始档案，只重开对应资格及依赖研究。不迁到registered所在日报，不要求排除一切假想渠道。

### 最后具名贡献校准与既成Books状态

[08217 retrieval/context forecasting](https://arxiv.org/html/2605.08217v1)不是只ETTh1或纯排行榜C：reader实际§3–5/AppB/D/G/H/I核到ETTh2/Exchange、PatchTST延长训练+cosine使长窗误差.647→.426（短.395），1seed/容量与预算不同、RAFT复用top5 cosine，不足形成新的可迁移机制或可靠长窗失效条件；foundation仅336/720零shot不证长窗噪声因果。AppG exp(entropy) rank0.1不采。局部负侧保留，不外推基础模型定律；贡献关闭不评分，不为该处置追日期。08209 Table1 Pets快速反退示例已reader即时撤销，不采用；真实反侧是Table2深度非单调、Table4中段/末段取舍，不反向拿local反侧否定准入。

A23两Ch23实际段/本人note已root精确窄授、reader逐字PRE后保存并作者完整自读；reader R21真实新增/完整两侧/本人注POST通过并释放。当前新增Books真实链为23，具体NC9、仅报告2待完整表归并；未签DAY。A15/18等“待核/未写”是历史prepared层，后续R13–21真实结论优先，不要求改本人纯注重复记流程。

## A25 完整六节prepared与实际QA（非DAY）

2026-10-18T17:18:16+08:00，已把全部新增34入当前唯一候选表/逐项§4并归并六节：原184＋新34＝218；新23实际整合＋9具体NC＋2仅报告，总131/85/2。新25深入/9标准为实际必要审阅，原184最低route129/55保持，不因低分进入Book改变原评分。原段旧15改写/修复叙述只保历史范围，旧§5/6长快照统一通过baseline可复查，不拿其完成声明授当前DAY。

实际校验V3通过。作者Node只读比较当前与冻结baseline：184旧候选完整行依序exact，原window exact；**完整144041字符原§4（含原换行）连续存在**；218唯一候选URL与218唯一§4标题URL集合相同。421本地引用均可达、0缺失；本日报与唯一SUP限定cached/unstaged diff-check均exit0。最初只有一个补检来源标签不符合格式、末尾空行，均已行政修复重跑，不改候选或公共合同。baseline未动，不stage/commit/push，未执行全仓原始件空白清理。

05253必要历史原件权限同步R22：作者web raw cache miss、curl reset（本机亦无pdftotext）不是全材料不可得。reader通过urllib实际读取[历史同题MD](https://raw.githubusercontent.com/onyx-dot-app/EnterpriseRAG-Bench/48ca3a9c6c2b9e07abdbae16ad0e3b314d2dc21a/paper_draft.md)完整题摘/两最小贡献节/基线表，有效层复用；只缺公开可见性/首稿日期，不称异稿。作者实际commit元信息与README patch可读；[真实新PDF路径](https://raw.githubusercontent.com/onyx-dot-app/EnterpriseRAG-Bench/137dd5146925febeeecbd1d370fd73339ad33eeb/enterpriserag_bench_paper.pdf)未取得内容，不声称实际全PDF核验。七晚登记资格有限停止经reader R22通过，原ALLIN/DEMM另两资格隔离仍保，均不迁日/计候选。

已交reader完整README六节actualDAY，非作者R21已释放最后Ch23两窄位；当前没有本轮Books锁。没有未写Source/Books普通队列，只剩整份语义复核/完成态真实读回，不由本QA自签。SUP为未跟踪文件，另实际执行no-index空白检查，发现EOF多空行后已窄修，不以空的Git两层检查代替检查新文件内容。
