# 后续有限题摘：准入校准与分层关闭

原完整题摘分别在[batch2](./abs_batch2.txt)、[batch3](./abs_batch3.txt)、[batch4](./abs_batch4.txt)、[batch5](./abs_batch5.txt)。日期身份非贡献分母。root已实际完整读取本表39题摘，批准29项具体增量继续必要证据；12294/12995/13243/13304/12247/12277/12719/13976/13238/12179转决定准入的最小核心，不是候选。原理由保留便于核改判；每项只读支持/直接反证，未决不是受阻。

## 具体增量已清楚，继续证据审阅

| ID | 原判断 → 实际delta → 应重考虑的选择 |
| --- | --- |
| 12294 | isolated tool-step PRM能预测任务效果 → offline与online cascade评价分离 → step评分应验证闭环效用而非离线榜单 |
| 12465 | final-outcome奖励不能利用wrongtrajectory的validsteps → validity/relevance双维stepcredit与稠密KGQA构造 → credit需要区分局部正确与任务相关 |
| 12626 | spatial理解需专门spatialobjective → linearized spatialIDs+causal干预 → tokenidentity可承载局部space/time grounding |
| 12730 | 常见entropy/exploration bonus只能控均值 → distribution-regularized controlpolicy → 采样探索的分布形状也是稳定控制变量 |
| 12748 | 相同步骤的reward应不随policy变化 → step正确标签与下游value在policy dependence上相反，reflection纠正/noisePRM → PRM目标须区分intrinsic correctness和continuation value |
| 12995 | token-local奖励缺全局推理结构 → graph stepcognitive标签、分层advantage clip → sequence structure提供不同creditgeometry而非仅多一个rewardname |
| 13029 | agent加3Dtools便应获益 → smallmodeltoolbenefit近零、RL后才提升 → toolavailability与使用能力分开评价（需同预算控制） |
| 13243 | 更多CoT/agent架构天然更可靠 → samebench controlledcomplexitycomparison → 必须核预算再决定复杂流程是否需要（核心决定） |
| 13304 | textCoT可保持counterfactualspace → intermediatetextdrift与视频物理simulation对照 → spatialcausal任务可外部模拟，非humanmentalmodel证明（核心决定） |
| 13387 | scalar confidence对variablelengthreasoning稳定 → temporalconfidence/STL规律参数化 → 置信轨迹的时间逻辑可修正长度混杂 |
| 13392 | learnedconstraint推理能组合到未见条件 → DFA seen/unseenconstraint受控drop，globalconsistencyhint无效 → 满足已见constraint不证明组合泛化 |
| 13562 | 解题需要dense共享视觉reasoner → smallrole-separatedcontroller/workspace+VARC协议 → 推理可按状态/控制不同模态分工，限定其visualtask |
| 13630 | activationsteering需要denseglobaldirection → permissionanchor激活几何+agentconditionalsteering → runtime权限锚可改变表示约束，必须核安全覆盖边界 |
| 13742 | speechjudge自然使用audio → structuredacousticcue blueprint vsALM/human评价 → textjudge可因中间表示改善局部可比性，不泛称text胜audio |
| 13879 | text-only tokenimportance可压multimodalcontext → VSkip visualamnesia与dualSurprisal/attentionVAIB → 压缩须保visualanchors，不只文本surprisal |
| 14127 | 单image安全可代表multiimagereasoning → 多图下reasoningunsafe与safeanswerignorance → safety需要multiimagecondition，attentionentropy仅关联 |
| 14209 | offpolicySFTtrajectory即可为RL初始化 → onpolicyfirst-error短纠正局部SFT → 用当前policy错误定点修复而非堆完整teacherCoT |
| 14243 | BF16train+FP8rollout只是一项性能优化 → mixednumericalpolicyoffpolicycollapse、unifiedFP8对照 → rollout/trainingnumericalcontract影响RL稳定 |
| 14249 | 强teacher/高studentlikelihood就是好distillation数据 → rank/surprisalratio同时测alignment与informativeness → 选teacher/trajectory需区分easy与teachable |
| 12307 | multiagentworkflow应实现多个独立LLM → homogeneousworkflow单agentKV复用matched对照 → singleagent同workflow是必要成本基线，heterogeneous不能据此共享KV |
| 12369 | citationcorrect/fluentsurvey代表research能力 → exactpaper输入隔离organization vsretrieval → synthesis评估要排除recall混杂，expert taxonomy不是唯一真理 |
| 12906 | testtimeparameter memoryuniformwrites够用 → utilitygating+globalcoverage同任务4×gradientstep差额 → consolidation预算可按contextutility分配 |
| 12979 | parallel dLLM速度自然转为agent收益 → temporalfeedbackbranch/schema symbolicprecision失败及noncausal角色对照 → dLLM收益须按agent角色分层 |
| 13155 | outdatedproxyimportance够做tokenskip → partialattention与lowrankFFN selfprediction+delayedpruning → pruningproxy要接近实际被跳过的变换且核自身成本 |
| 13384 | FIM只能completion，edit需额外agentcalls → SRI explicitsearch singlepassinstructiontune matchedchat/base → completion可改为可定位edit，能力保持/latency须核 |
| 13722 | 个性化memory召回越充分越好 → irrelevant/repeated/sycophantic记忆使用盲点与SelfReCheck → personalization应评估不使用memory能力 |
| 13734 | contextrecap以通用summary构造即可 → long-vs-shortlossgap定点找依赖并训练recap → summary训练数据可由模型实际依赖差额选择 |
| 12247 | diffusiondecoding只按逐tokenconfidence提交 → semanticanchorskeleton+quantverificationstop → globalplanning可减少NFE，NFE非总时延 |
| 12263 | VLMrank攻击只需单模态 → alternating协调image/text提升转移 → rank-integrity威胁需包含跨模态联合，不泛保证imperceptibility |
| 12277 | realtimeactionworldmodel需多stepdiffusion → one-step3DUNet+planning closedloop对照 → 可考虑改变transitionmodel采样成本与控制频率取舍 |
| 12376 | ARleftprefixwatermark直接适合diffusion → availableleft/rightneighbor局部bias、无需过程inversion → 非顺序生成可设计双邻域标记，但需核相关性及攻击 |
| 12719 | efficientDiT必须减少tokens → LCHA/SSA sandwichbudgetDP、2-in-1distill → attention布局可让更多tokens更廉价，iPhoneFPS不是无条件保证 |
| 12865 | 鲁棒teacher必需adversarialtrain → heteroCLIPproxy防御及迁移generalizationoverfit反侧 → robustnessdistill需同时控制naturalgeneralization |
| 13238 | pixeladversarialbudget可代表天气风险 → nonpixel rainilluminationspace产生crossmodalsemanticshift → robustness含物理structuredconditions，作者合成雨不是真实天气证明 |
| 13976 | embodiedCoT收益需inference显式thoughttokens → traincompactlatentvisual/multiCoT，inferdirectaction → reasoning-aware训练和online推理成本可拆开 |
| 11791 | NTP只对单reference token评分 → conceptgroup监督合并等价surfaceform → objective可分离lexical与semantic信用，需核concept构造泄漏及perplexity口径 |
| 12051 | PEgradient仅位置统计 → 重建泄露与shuffle+unknownPE控制 → positional梯度也是privacy渠道，分类训练范围不泛化foundation部署 |
| 12104 | lowFPR下MIA低检测代表memorization低 → errorpositionrelativepretrainedprobshift两forward → auditstatistic选择能改变风险判断，限定finetune条件 |
| 12179 | humanTolerance threshold适用于Transformer学习 → BabyBERTa人工grammar size/type/exception控制不符合 → 不能直接借人类规则阈值设计小模型data，局部学习反证不因规模小排除 |

## 仅决定准入的最小核心待核

- 12323 MARO：roleweighted/outcome-return/utility是否实际改变nonstationarycredit条件，不能只因multiagent成熟排除。
- 13761 DARC：externalsourceddifficulty/teacherprivilegeddocuments/fixedquestioner是否实际排除selfbootstrap混杂；三项pipeline名称不单独准入。
- 13992 COMPACT：multiteachergradientcompatibility的graphconsensus/MI是否形成新的objective或直接预算反证；不能只因curriculum组合关闭。
- 11854 ATOD：taxonomy新dimensions不够；memoryevaluator是否有明确等质量资源差额，定点eval决定。
- 12030 ARC：activecontextrevision与passivesummary如有同预算actualfailure路径/controlledboundary可收，不能只换state术语。
- 12449 AgenTRIM：offlineinterface reconstruction+runtimeleastprivilege成熟，但status-aware是否真改变existingruntimeguard能力/过度权限与任务能力同控，定点安全结果。
- 12762 ToolMaster：trial-and-executionsupervision+RL是否有unseentool受控增量，不能只因“learningbyinteraction”原则准入或排除。
- 12996 OFA-MAS：oneforallMoEtopologygenerator是否在unseendomain有budget/structurallearning条件，不能只模块组合准入。
- 13186 TIVS-O：非单调observability/strictness结果需实际控制支持；当前“productionready/zero breach”不采用。
- 13247 WorldMind：ProcessvsGoalexperience能否提供具体physicalfailurevsoptimality可分离的增量，maturefeedbackmemory本身不够。
- 13352 LLM-as-RNN：fixedtokenbudget feedbackrewriting与MemPrompt实际差额是否更改memory更新判定，领域预测指标本身不够。
- 13622 CARPE：context-awareprioritization是否有CLIP→LVLMrepresentation损失受控反证，ensemble原则本身不够。
- 13719 HAVEN：entitycohesion+hierarchy是否actualfragmentation/equalevidencebudget条件，长视频QA最高分本身不够。
- 14230 MASCOT：personacollapse与groupsocialreward拆开是否actualreward干扰控制，应用场景分数本身不够。
- 12142 EchoVLA：audiointentsynthetic来自ego-motion可能targetinformationshortcut；如只有增加taskinput，不构成新VLA机制，定点leakage/ablation决定。
- 12428 ReWorld：物理/任务/embodiment/visual多reward组合成熟；efficientflowPPO或rewardgeometry理论有实际increment则继续，不只videoquality分数准入。
- 14188 IIR-VLM：ILRexpertauxencoder组合是否改变representation/instancelearning条件，否则仅taskrecipe。
- 14251 LightOnOCR：强distillationmix/checkpointaveraging/taskarithmetic+IoU-RL组合本身成熟；核心是否有可归因的质量/资源boundary，不按1B/9×自动准入。
- 11776 SelfReflectDetox：selfgeneratedcontrastivedata与internaldetector是否具体成败边界，不能只selfcorrection标签准入。
- 11868 TerminalBench：新89hardtasks不足；erroranalysis或verification机制需改变具体agent评价判断；项目更早公开与paper新事件亦需区分。
- 12522 CogniGent：debughypothesis/callgraph/contextengineering组合是成熟recipe；如发现具体failure/对照归因再准入。

## 明确贡献关闭的分层样本

- 12538、13705：完整摘要是reasoning/visualpuzzle综述与taxonomy，无新机制或具体原始反证，不因相关owner而准入。
- 12343：经济行为prediction/PSID人类sample替代指标，当前delta在economicforecast应用而非模型形成或系统机制。
- 12618：qualitativeeducationalcoding同意率/CoT应用，不改变通用reasoning/eval设计判断。
- 12842 SCULPT：MCTS+symbolicdimension/type/magnitude过滤组合作数理题，无新的搜索有效性/复杂度边界，成熟recipe。
- 13115、13132：conversationalretrievalRL、questionguided3DGS+novelviewnavigation组合，摘要仅展示taskbenefit，不提出可迁移成立条件；非整体排除retrieval或worldmodel。
- 14032：多scoreteacherfeedback/responsepair/margin+regularizationdistiller成熟，摘要未明确其新增stablemechanism。
- 14051、14063、14157：多语言syntheticdistill、文化CSIsbenchmark、音乐conceptdataset+TCAV组合，新增在task/data覆盖，没有模型或系统判断delta。
- 11903 AEMA：auditableevaluationworkflow/agenticjudge成熟组合，enterprise模拟对照未给具体新增评价盲区。
- 11913 LSTM-MAS：worker/filter/judge/manager与LSTMgates类比不是实际可验证的recurrentmechanism；摘要仅benchmark提高，新增stablecondition未提出。
- 12286：RepE+OCSVM contextualanomalyclassification，通用oneclasssubspace组合，仅domains“promising”检测结果而无新边界。
- 13383 AgentForge：typedskills/DAG/YAML/backendadapter成熟工程组合，不因devtime降62/78%自动推新长期系统贡献。
- 13836 FutureOmni：newfutureforecastingtask+7K SFT泛收益，本身不证明新的causal/temporal机制或感知→预测可行性边界。
- 12304：已有transferattack加textcandidate/globalreplacement与imageresize/blockshuffle组合，摘要只ASR新高而无受影响判断或新成立条件。
- 13809 DroneVLA：VLA+GroundingDINO+A*/MediaPipe dronehandover组合，localization误差验证应用可行，不增加VLA/控制长期机制。
- 14207：CLIPgradient+differentiablerenderer+softICP/penetrationloss用于meshalignment，是成熟优化recipe在新task，不以WorldModel词汇重收。
- 13358 [官方当前页](https://arxiv.org/abs/2601.13358)：实际显示withdrawn，v2 2026-03-30，作者说明理论框架错误。保留原始身份，不入选、不评分、不Books；撤回不当作访问受阻。

上表是作者准入理由，不是独立日级通过；未改变的有效题摘不重新无差别读取。所有尚未决定准入项保留精确pending，不因深审成本/规模/数量缩池。
