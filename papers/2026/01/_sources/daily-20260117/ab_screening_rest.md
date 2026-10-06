# 本日完整题摘语义筛选（第二至八批，作者 provisional）

## 纠偏恢复的首批 AB6–8 准入终裁（root 完整题摘校准通过）

root实际重读本日XML完整10题摘：09823/09896/10102/10310/10702/10712/10714/10710八项按具体增量准入，5–6标准必要范围；不是Evidence或Books通过。09971专门TSC encoder接冻结LM任务探索，仅Inception获益，未新增foundation机制/可迁移bridge失效边界；10707 BLIP2 patch PCA+成熟descriptor drop的驾驶局部指标，未建立冗余→spurious因果或基础表示/执行选择增量，两项pre-denominator具体关闭。不是小模型/领域标签/时间关闭，原AB与先前拟理由保留作为改判过程；无新受控机制反例不扩正文。

本批已实际重读下列10份完整exact-v1题摘，normal Submitted cohort/正常公告+registered上界均完全落窗，原日期字段仍在all_date_fields。NanoSD的v2提交在本窗但公开Updated至Jan19，未用v2或把提交当新公开事件。这里只判断具体增量，不称Evidence完成、不强制长gap或Books，不按数量剪池。

| ID | 原有约束 → 实际增量 → 若成立需要改变的选择 |
| --- | --- |
| 09823 NanoSD | 只压denoiser/参数数不保证edge可运行 → U-Net与VAE联合surgery/feature distill以及真实mobile latency-Pareto → decoder/codec亦应在同一E2E质量预算内优化；拟2+2+2=6标准，核硬件与完整pipeline条件而非20ms宣传 |
| 09896 LAP audit | aesthetic score被当通用curation质量 → 同一predictor在原LAION/艺术slice中筛选与gender/cultural构成有关 → 显式核filter训练人口与被移出slice，不用高score代表population-neutral质量；拟2+1+2=5标准，不授representation harm唯一因果 |
| 09971 TSC | 任意专业encoder接冻结LM应利任务 → 同样比较的encoder只有Inception稳定获益 → 需保留encoder-only/bridge条件，不能由LLM名称决定接入；拟2+1+2=5标准局部反证，非所有LLM/TSC必需该encoder |
| 10102 Persona | 显式payoff可让role agents据激励优化 → persona×payoff visibility四game/model受控交互，persona可压倒optimal payoff → 角色提示应作为决策混杂变量而非装饰；拟2+1+2=5标准，不以Nash等同人类正确目标/全架构因果 |
| 10310 SENSIA | sharedparams/文本alignment混多语言sense → Backpack sense-mixture/context联合parallel alignment并保target LM fluency → 可比较meaning unit对齐而非只有surface共享；拟2+1+2=5标准，核相同budget/latent topology不是语义真值 |
| 10702 STITCH | repeated entity语义近似会取错goal历史 → goal/action/entitytype contextual-intent cue过滤检索 → memory选择须分当前intent compatibility与semantic similarity；拟2+1+2=5标准，非仅memory/state命名，不授latent goal真值 |
| 10712 MatchTIR | trajectory uniform credit无法区分冗余tool turn → predicted-vs-gold traces bipartite matching reward并与trajectory advantage分账 → 可把工具回合对齐而非只最终success送训练；拟2+2+2=6标准，核gold/匹配/turn边界与预算，不授无偏过程credit |
| 10714 Alterbute | 强context监督限制intrinsic改变/弱监督丢identity → train放宽extrinsic、infer固定background/mask及VNE identity target → 训练support与推理约束不必同强度，identity与属性可分目标；拟2+1+2=5标准，仅所支持局部条件，无完全背景/真实身份保证 |
| 10707 SPS | foundation contextual patch冗余会把policy绑spurious局部signal → dropout patch descriptors保layout并测OOD/closed-loop → 比较contextual descriptor冗余下stochastic observation训练与完整patch，而非PCA相似直接当因果；拟2+1+2=5标准，核mask/layout控制与speed含义 |
| 10710 CLI | 单visual最后层只在LM入口消费限制层级取用 → 多visual层projection+decoder-context adaptive跨LM层gate → 视觉表示可以按解码上下文多层读取；拟2+1+2=5标准，核AMP/AGF独立对照，不把18榜或many-to-many术语当证明 |

只用精确v1题摘；下列“可核/decisive”不是审阅完成、确定落窗或Books通过。原完整AB见逐批XML；日期见官方DataCite原字段。标题明确范围外材料另留有限发现，不把222宽身份转成全题摘队列。root已读范围记于对话校准，末日报会汇总；不以高保留率推断质量。

## AB2

root实际完整读20题摘：09985/10079/10058/10141、10108及后列明确可核项准入；六项只有决定贡献机制含糊，先decisive方法得到判断即停。

| ID | 旧约束 → 题摘实际增量 → 改变的选择/关闭理由 |
| --- | --- |
| 09985 | Far-memory完整残差取回昂贵→tieredresidual距离逐步精化与outside-topk早停→验证是否无需完整向量/兼容CXL延迟，准入7最低深度 |
| 09988 | pose-only示教欠接触约束→fingerwrench示教学习force/stiffness并交controller→核动作接口与闭环接触，不把硬件名称计贡献 |
| 10007 | 离散深度不能连续调compute→middlelayers ODE+learned concat steering→先核是否有区别于已有continuous-depth的有效控制差额；decisive |
| 10010 | groundedentities不认证eventrelations→eventrelation错误与counterintuitiveframebias→核实体/关系分账与控制，对照准入 |
| 10025 | 三现有personality流程以Jungian名重组+MBTI初测，未新增状态/可靠性机制；root关闭通过，不因psychology标签排除 |
| 10029 | tokenreward对sequence-actionsearch粒度失配→PSPO动作序列优化→先核决定性reward/credit机制，不把papersearch误当AI4Science；decisive |
| 10058 | 无标签ICL为何有益不明→受限multiclasslinear EM的Transformer构造/CoT teacherforcing→核假设和收敛范围，准入7不授现实任意ICL |
| 10061 | 文本CoT无法承载视觉中间state→progressiveframes+independentframeencoding→核相对已有videoinitialization的具体差额；decisive |
| 10064 | teacherprefix超studentcapacity→adaptiveprefix alignment→核容量失配与prefix依赖条件，准入 |
| 10079 | sparse rollout节省KV却变策略分布→denseold/sparsesampler/learner importance+rejection→核support/稳定性/compute代价，准入8 |
| 10088 | official完整StateofAI在December2025已公开，作者/AB/全文一致；窗前全文不列当日（jan17_prior_*） |
| 10094 | 自生成题无独立gold→reason/guess dualdifficulty与solvermajority反馈→核自确认失败与循环条件，准入不授pseudogold真值 |
| 10096 | 多语多模态数据难得→English-only线性map把multilingualtext能力转给MM→核十一语言迁移/映射失配，准入 |
| 10101 | NLplan缺可检查约束→typedcitationmatrix normalize/replan→先核是否超出现有可验证typedplan；decisive |
| 10108 | answer正确不等真实使用所给evidence→evidencegate/scientificdoc切片→准入，trace不当causality/gold，也非science成果 |
| 10112 | semanticcodegraph不能认证builddeps→deterministicbuild/test CMakeprovenance graph→准入核8repo与工具适用边界 |
| 10114 | 固定teachercheckpoint不适student阶段→scheduledcheckpoint/advantageweight→先核具体调度signal，超过teacher的iff优劣分解是恒等而非新理论；decisive |
| 10120 | decentralized逐轮协商代价→one-shotheterogeneous interactiontopology→先核为何真实替代设计而非名称；decisive |
| 10132 | 局部repurchase任务temporalcontext可能损害LLM、专用预测器仍强；有条件负侧拟1+1+2=4关闭，不采普遍contextlaw，root具体关闭通过 |
| 10141 | safetyutility梯度冲突→低秩safetygradient projection→核subspace估计/理论假设与实效，安全深审准入7 |

## AB3

已完整读20；可核项送root实际AB独立校准，未确认的先一处decisive。

| ID | 判断与具体差额 |
| --- | --- |
| 10148 | trajectory非普通text→distinct numericmodality/continuousvalue alignment；先decisive而非domain数据量 |
| 10155 | KVkey-memory压力→PQ asymmetriclookup attention而非解压全key；核实际QKkernel/lookup overhead，不借GPT2小规模排除 |
| 10156 | terminal安全测量晚→tool执行前stepguard回馈；安全深审不采万用guard |
| 10159 | favoredexpert activation不认证功能→domaincausaldriver vsloadmetric/counterfactual，核tokenprefix控制 |
| 10173 | reasoning中latent intent冲突→reasoning-trajectoryjudgment alignment；安全深审须matchedbudget和judge限制 |
| 10187 | token数不能表达歌词duration→syllable/durationconstraint reward；先decisive，不因歌词任务自动排除 |
| 10198 | holisticpersonajudge混可取性与模拟→humanlikeness/behaviorlikeness分账；核construct和判分人口 |
| 10201 | processcredit与outcomereward混合→v1 PRLentropy/KL分解；仅v1真实标题/机制，不借v2Future-KL改名 |
| 10214 | warp视频保content但depth/cameracontrol不足→双流video/warpeddepth conditioning；先decisive对照 |
| 10229 | Euclidean activationsteer离开representationmanifold→VAEgeometry steering；先核“naturalgradient”真实计算而非术语 |
| 10242 | 最终loopscore增益不认证内state→loopinternalrepresentation退化与finalloopreadout；设计反证必要深，不能只读负headline |
| 10245 | wholequery路由浪费stepcompute→PRMcriticalstep给large model；核routecost与oracle/budget |
| 10254 | geometryreasoning与directknownposition混淆→binaryknowledge probe；先decisive实际evaluation盲区 |
| 10266 | IOI单参考attentionheadsimilarity/randomorthogonal localprobe，拟1+1+2=4关闭；不采普遍Attention causal解释 |
| 10267 | 用现有LM做wireless source/channel bit recovery，没有改变模型/训练/serving主线，仅通信应用；贡献前关闭，不因通信学科本身排除 |
| 10272 | modal独立专家难sharedtransfer→共享groupedmodalexperts；核MoE/shared负载与modality机制，owner非词匹配 |
| 10274 | 单requesttoken效用漏queuevariance→PoissonFIFO M/G/1 service secondmoment优化；条件数学深，不授tailSLO/任意arrival |
| 10305 | 100M中文imagecaption整理与标准SigLIP2continuation，AB未给能改变设计的新筛选/目标条件；贡献前关闭，不因dataset排除 |
| 10313 | image/text扰动耦合→ScMixgradienthistory/futuretext全局攻击；安全信号先decisive必要变更，再按受影响范围深 |
| 10323 | endofturn理解阻塞speak→同步multimodalunit+decouple speakinghead；核两阶段curriculum与真实streamlatency |

## AB4

| ID | 判断与具体差额 |
| --- | --- |
| 10332 | 静态textencoder→rewrites与learnedreasonstatecond dualGRPO；先decisive区分promptrewrite与实际表示训练 |
| 10338 | skills当描述忽略executionprogramtrust→SkillScan静态/LLM/manual与攻击面；安全深，不把26.1% detectorlabel当全pop vulnerabilitytruth |
| 10343 | repo任务成功可违explicitinstructions→independentcompliance checklists；核groundtruth与真实blindspot非仅新任务 |
| 10349 | entropy不等策略exploration→strategy-repr surprise/stabilityreward；先decisive实际探索状态 |
| 10355 | webworkflow无法直接toolRL→四阶段groundedtrace；先核grounding/verifier真实增量，不取dataamount |
| 10373 | lowratecompressedlatent先验失配→frequencyawareepsilon/consistency两步；先decisive，generationowner不默认codec应用 |
| 10378 | 文本historytoken贵→当前chunktext交错+历史纯visual连续decode；核prefill与decode/训练兼容约束 |
| 10387 | persona漂移→assistant-axisactivationcap；完整AB已读，Jan19 officialblog不替代Jan16paperdate；先公开/版本日期分流 |
| 10398 | 不可答schema仍逼生成→intermediatequery/schema refusalgate；安全深先核限定mismatch对象 |
| 10402 | longMLE traces污染与知识固化→hierarchicalcontextcache；先decisive清 transient/stable状态与反馈，MLE系统不因AI4Science标签排除 |
| 10403 | discrete diffusion目标分布tilt需corrector→FeynmanKacSMC温度/product/reward；核假设/target而非protein应用成果 |
| 10416 | 序列preference无法细局部tokenreward→subtrajectoryflow病人/doctor机制；先decisive、不采universalDPOheadlines |
| 10421 | Marr框架的cognitivemodel哲学讨论未提供改变本项目设计的机制/实证反证；贡献前关闭 |
| 10440 | runtimeagenttrace不约束futurecall→stagingcontextflowpolicy+executiongovernor；安全深验证动态有效性 |
| 10460 | 相同content不同framing改变bias→13model/360factorialgrid固定context；安全/评价深核bootstrapFDR与非因果外推 |
| 10496 | bugfixscore混训练暴露→DataPortraitsmembership分层；核completion/likelihoodcontrast，不以检测器认证membership真值 |
| 10497 | continualFT稳定性代价→双lowlosspathmerge无replay；核二阶近似与connectivity适用边界 |
| 10504 | 静态web任务易过期→freshinfotree examiner deep/wideadaptivecomplexity；核dynamicgroundtruth与judgecost |
| 10524 | phishing泛化受style/data交互→跨model/data controlledslices；先decisive新eval盲点，不把架构相关当因果 |
| 10527 | safetyaggregate掩切片→multilingual/adversarial/modalityprotocol；先核具体新协议盲区，广维度名称本身不准入 |

## AB5

| ID | 判断与具体差额 |
| --- | --- |
| 10532 | supporter-only empathy优化外部人视角遗漏→seeker/bystander多视角reward；先decisive，70%userpreference需预算/人口 |
| 10543 | jailbreak前latent安全但continuation覆盖→earlydecodeprobe；安全深不授latenttruth |
| 10553 | videohead视觉好未必物理一致→VJEPA latentWM reward在inference候选denoise；MM物理机制非AI4Science成果 |
| 10560 | tokens总量不表达DAG延迟→criticalpath-awareorchestrator监督；核parallelexecutor模型与总费用 |
| 10563 | 小基础数据KANvsMLP比较未给支撑foundationmodel的机制/条件，贡献前关闭；不是“小模型无价值” |
| 10566 | 行为forget不认证知识消失→activation-informedunlearning；安全深核oracle/循环识别假设 |
| 10567 | interactionistcollectives为概念方向，无新增机制/实证修正；贡献前关闭 |
| 10572 | OSkernelvariance可源于hardware而非应用→VarMRI causal tracing；先decisive是否直接改变AIruntime测量，不以系统类比准入 |
| 10580 | 跨语言PPL混form与meaning→平行semantic corpora/BPC等intrinsicmetrics；核六metric两corpus条件 |
| 10589 | 固定attackset让defense过拟合→selfattacker/defender RL,UCB+reflectivereplay；安全深核共偏与外部泛化 |
| 10592 | flatcaption缺actionhierarchy→VJEPAsegmentation+treecaption/selfrefine；核数据监督增量与消融，不采用100M规模作为贡献 |
| 10611 | Molmo2 Dec11originalpost已公开bidirattention/tokenweight/message-tree/datarecipe；TechReport当前跳Jan16v1，历史整稿/新增事件不能确定，日期/delta暂隔离，不无差别diff |
| 10632 | motion/video分离不一致→3Dmotion与2Dvideo dualVDM/crossattnjointdenoise；核共生成对照 |
| 10639 | FFNupproj参数/activations成本→statictokenindexedembedding+CPUasyncprefetch；核是否static条件内有效，拟8深不因350M/1B小而排除 |
| 10645 | confidence混lexicaltemplate→影响估计分content/style；先decisive新evalblind，notcausaltruth |
| 10657 | selfevolutioncontextpollution/modecollapse/weakcollab→pruning/backtracking/crossover；先核三个受控failure，KernelBench/ModNanoGPT主线，LLMSR成果暂缓 |
| 10673 | 每shard码表重建贵→平均prior fixedcodebookbatchHuffman；核实际compression/rebuildtradeoff，不先授networkwallclock |
| 10679 | HRMfixedpoint声明→多attractors/guessing/inputperturbbootstrap反证；必要深入，不用负结果自动拒 |
| 10681 | contextsummary无budgetedstructure→anchorscoverage/diversitybubble；先decisive实质selection机制 |
| 10684 | heavy-tail/scaling因果假设→randomgraphsyntheticlanguage复杂度与computeoptimalfit；核受限stats与替代解释 |

## AB6

| ID | 判断与具体差额 |
| --- | --- |
| 09823 | edgeimagefoundationlatency不只是paramcount→jointUNet/VAE surgery+distill；核hardware实际可行性；不采later-v2 |
| 09879 | CT任务VLM+SAM2组合/segmentation数据，无明确新增可转移机制/失效条件；贡献前关闭，不因医疗题材排除 |
| 09896 | aesthetic filter并非通用审美真值→LAION艺术slice过滤分布偏差；核模型filterpopulation与representation影响 |
| 09971 | frozenLLM接encoder不自动利TSC→只有Inceptionhybrid改善、其它反侧；拟局部5标准而非小模型拒 |
| 09982 | RAGDhao domainshift/context量与retrieverchoice局部比较→拟1+1+2=4关闭，不采通用RAGscalinglaw |
| 10011 | SQL错误不能只retrievesuccess→三结构任务/修复memory inference接口；先decisive是否已有errorfixretrieval组合 |
| 10018 | olderadultqueryparaphrase应用已有promptchain，无新增LM系统机制；贡献前关闭 |
| 10020 | multiagentEHRschema QA标准pipeline，AB未给新评价盲点/机制，贡献前关闭；不因医疗标签 |
| 10102 | persona可覆盖显式payoff→fullinfo4gamesfactorialroledesign；核role/task混杂不认证normative人类偏好 |
| 10122 | roleplayreview taxonomy无新增具体机制/反证，贡献前关闭 |
| 10143 | temporaldrift中dataaugmentation/curation bilevelplanner→先decisive是否跨时间数据梯度新接口，finance名称非拒依据 |
| 10161 | 38languageNERcollection/expertlabels标准tool/modelrouter，未新增privacy/learning机制；v1不能借laterPII题名，贡献前关闭 |
| 10215 | tablelinearization丢structuredretrieval对应→celllateinteractiontopology；先核“mathinsufficiency”真实假设与有限SEC25评价 |
| 10228 | HD-EPICpipelinequerypreprocess/TCoT/postprocess/specializedFT局部结果，拟1+1+2=4关闭不普遍segmentation机制 |
| 10310 | polysemy混语言embedding→sense-levelBackpackmixture parallelalignment；核4languageLatentgeometry与成本 |
| 10321 | longresume/jobdistilllatecrossattention→先decisive是否新generalrepresentation/校准条件，不以job任务指标准入 |
| 10369 | posequalityjudge层不等authenticity→layerselectcontrastiveLoRAsensitivity；先decisive actuallayer/objectiveblind |
| 10388 | IndicDialect新11dialect/13k标准collection+FT无独立新盲区，贡献前关闭 |
| 10462 | ChartComplete增加30charttypes/taxonomy未给变更generaljudgment的协议/条件，贡献前关闭 |
| 10463 | XR12kernels/DSE profiling；先decisive是否foundationruntime直接机制，而非用一般硬件类比准入 |

## AB7–8 尾部

| ID | 判断与具体差额 |
| --- | --- |
| 10909 | asynchronousbodypart时间标注+partprompt diffusion可组合；日期上界Jan19，隔离日期，不先正面准入 |
| 10825 | longCoT≠solecompute→perspectiveinteraction/controlledRL；日期lateheld，需firstpublic精确恢复 |
| 10770 | sharedspeechdiscretetoken/instruction multitask通用架构组合，先decisive实际交叉任务增量；dateheld |
| 10702 | semanticmemory匹配不了latentintent→goal/action/entitytype contextualintentindex；可核检索noise机制 |
| 10712 | uniformtrajectoryadvantage→bipartitetracematchingdense turnreward+dualadvantage；可核matchgroundtruth/credit条件 |
| 10781 | futureflow从noisywebforecast融合VLM/diffusion；先decisive preprocessing/architecture真实增量，dateheld |
| 10591 | 把既有DER用于financialLSTM比较并命名ProbFM，没有foundation训练/架构新机制；贡献前关闭，不因finance或small |
| 10714 | trainrelaxextrinsic而inferfixcontext+identityVNEsupervision→intrinsicedit控制分支；可核身份/背景tradeoff |
| 10600 | MA-banditproceduralfairnessnormativeobjective，未直接作用foundationmodel/LLMAgent机制；贡献前关闭，不泛化所有理论无效 |
| 10774 | 新globallysmoothanalyticbijectiveflows closedinverse→generativesampler替代分支；dateheld，physics应用不采 |
| 10707 | BLIP2patchredundancy→stochasticpatchmask保持spatiallayout训练policy OOD；核因果/realcar和闭环成本 |
| 10660 | 现有persuasionstrategyguidedprompt提升argumentprediction，不新增可转移机制/评价失效边界；贡献前关闭 |
| 10520 | normative/instrumental分module+deonticlogicGuard可contest；安全信号decisive真实formalguarantee边界 |
| 10773 | AST+LLMsemanticmultirepograph RAG称emergentcapability，AB未给新retrieval/可靠性条件；贡献前关闭，dateheld无需深 |
| 10644 | offlineCranfield IR不支持dynamicRAG→onlinepipeline HTTP batching/cache接口；先decisive实际兼容/serving约束变化 |
| 10905 | worldmodel data ActionShapley randomizeddynamiccompute→data selection；dateheld |
| 10536 | FigmaJSON/prompt映射已有T5seq2seq应用，无新model/system机制；贡献前关闭 |
| 10710 | finalvisual-layer只注入LLM输入瓶颈→decodercontextadaptive多层many-to-many injection；可核AMP/AGF两因子 |
| 10708 | diffusiondiscretization accuracy代价→lowdegree/collocation solver polylog1/epsilon与effectiveradius；可核理论假设/scoreoraclecost |
| 10701 | RSUQ prescribednoise量化的隐私/收敛性质→可核CEPAM成立条件，不把federated名称计分 |
| 11652 | draft浪费/verification互扰→SLOdraftcontroller/estimator/batchschedule，dateheld，不采用headlinegoodput |
| 11653 | transcript/recall混commit→boundedstateACC artifactrecallvsstatecommit，dateheld，不先采用bio名词 |
| 11663 | AWQ/GPTQheuristics→gradientweightedactivation sensitivity不同近似假设；dateheld，conceptualproposalamplification待正文 |
| 09916 | finitefieldPSMMsecurity/tensorlowrank不是foundationtraining/runtime实际机制，信息论privacy不映射任意ML浮点；贡献前关闭，不因math排除 |
| 11647 | RL模拟CI/CDtestskip genericDevOps应用，没有LMtraining/inference mechanism；贡献前关闭 |
| 11650 | MCP封装chemicalsimulator两separationcases已有LLM流程，科学应用暂缓且无新通用执行机制；关闭 |
| 11655 | issue-resolution survey分类/方法汇总，无具体新blindspot/反证；贡献前关闭 |
| 11651 | generativefacialattrs与downstreamclassifier偏差交互，dateheld；不采社会因果或真值 |
| 11644 | VLMselfconfidence失配→externaldetectorgeometry selectivecoverage；dateheld，不能把importance当因果 |
| 09806 | facialverificationFGSM+diffusion/brightness+caption/hashpipeline已有方法组合无新foundationconstraint；贡献前关闭，安全词不授新机制 |
| 11660 | 近binaryexplicitzero mask→subtractivebitencoding BMMAkernel；潜在直接quantaccelerator条件，dateheld，不因UNet小模型自动拒 |
| 11658 | failuresynth/escalateteacher+CL/RL/GA命名组合，无明确新adaptation/control条件，贡献前关闭，不采AGI宣称 |

## 当前初筛与终处置停点

`jan17_category_exactAB.xml`17份、`jan17_LG_exactAB.xml`19份已逐份完整题摘语义筛选，见 supplement_screening.md。152份AB1–8加09972定点1份及补检36，合计189实际完整AB；222唯一主题标题库存不是候选池或正文队列。root完成AB1–4准入校准，AB5–8/supplement后续校准与决定性消歧继续。本日候选分母尚未冻结。

root必要源与实际Books POST通过10家族：09833/09883/09985/09923/10079/09853/09851/09859/10141/10108；09858中心RL配置与10058中心learnability证明争议安全暂缓NoBooks。因此43个已明确准入工作项中，12已终处置、31普通必要证据/Books/独立核待办；不能将准入集合当最终冻结分母。已准备待root必要核6家族：09881/09905/09988/10010/10064/10096，见三份最新evidence包。dateheld/历史目录/Molmo2另隔离，不与普通待办混计，日级Gate未授。
