# 2025-07-21 有界筛选与保留

本记录属于当日作者工作，不是独立验收。窗口07-20 09:00～07-21 09:00 BJT。原始主题查询和执行时间见四个 `arxiv-*.request.json`，完整返回题摘见四个 `arxiv-*-entries.json` 与Atom `.raw`。184个命中跨分类去重121家族，仅为提交区间发现线索；月列表只浏览相关标题查漏，不建立1671条待关闭队列。`published`提交字段不可用于证明首公开。

读取相关/含糊项完整题摘；下表中已存v1的原件为 `abs-<末五位>-v1.raw`（请求同名），未恢复v1者仅作当前API题摘发现线索。后者不支持历史版本的正面证据，不用当前摘要改写v1，也不以补齐全部版本为恢复目标。日期统一未核；明确贡献关闭项不再请求日期。没有采用任何性能数字进Books。

辅助历史搜索返回文本保留在 `sourcessearch1/2/3.txt`：前两批为空、第三批只有无关MiniMax用户制作网页。准确查询字符串未留存，因此这些响应**不能证明任何检索召回范围或机构覆盖**，日报只将它们视为未能恢复必要官方材料，不以无结果作无研究事件证据。

## 日期保留：准入机制与身份

下面 retain 表示存在值得核验的具体贡献，但**不是本窗候选**、没有评分和审阅完成计数。已存核心只保留实际读过的位置。公开身份/日期未定的共同请求见日报§5，不重复创建材料请求。

| 身份/完整题摘 | 准入命题与采用边界 |
| --- | --- |
| [2507.13474v1 Paper Summary Attack](https://arxiv.org/abs/2507.13474v1) | 安全研究学术包装可干扰拒答→来源外壳不是安全证明；方法核心已读，ASR未普遍化 |
| [2507.13540v1 Provable Low-Frequency Bias](https://arxiv.org/abs/2507.13540v1) | 表示ICL随context/layer收敛产生低频偏置→需重新解释表示可学习范围；仅理论假设下，不因小模型拒绝 |
| [2507.13546v1 ∇NABLA](https://arxiv.org/abs/2507.13546v1) | 固定局部稀疏漏长程/纯动态漏邻界→动态块与邻域联合的保质预算；相关实验已读、日期未核 |
| [2507.13568v1 LoRA-Loop](https://arxiv.org/abs/2507.13568v1) | replay生成器与新任务失配→生成器task-LoRA及两阶段筛选闭环→重判合成replay能否抗遗忘，不仅借用continual learning术语 |
| [2507.13569v1 Change of Thought](https://arxiv.org/abs/2507.13569v1) | 固定encoder深度→attention内部固定点迭代→不生成CoT token也可自适应test-time compute；不外推任意LLM |
| [2507.13579v1 PLUS](https://arxiv.org/abs/2507.13579v1) | reward缺个人上下文→联合学用户摘要与条件RM→用户/主题迁移的偏好表示；当前v4指标不回填 |
| [2507.13601v1 Leveraging Multi-Instance GPUs](https://arxiv.org/abs/2507.13601v1) | MIG分区形状/显存不满足简单单调work假设→moldable任务与分区树共同规划；属于GPU资源机制而非一般调度类比 |
| [2507.13666v1 KiC](https://arxiv.org/abs/2507.13666v1) | 生成任务无exact-match gate→关键词语义代表一致性做级联升级→重判cost/quality gate，不把单成本数字准入 |
| [2507.13681v1 LoopServe](https://arxiv.org/abs/2507.13681v1) | multi-turn prompt/KV重复增长→dual-phase sparsification与progressiveKV选择→保留/压缩近期输出的条件 |
| [2507.13710v1 CogniQ-H](https://arxiv.org/abs/2507.13710v1) | hard-stage限制探索→LLMprior×Q/LTR软策略→保留支持域须严格正prior，有限预算override未证；定点公式/消融已读，不把成熟Bayes原则计新增分 |
| [2507.13761v1 Innocence in the Crossfire](https://arxiv.org/abs/2507.13761v1) | 单模态安全不保证融合安全→skip connection干预揭示benign视觉输入下拒答失效路径；须受测结构/威胁模型限定 |
| [2507.13773v1 Teaching VLMs to Ask](https://arxiv.org/abs/2507.13773v1) | 强制回答评价掩盖视觉指代歧义→区分应询问与应回答并训练clarification；保留评价/交互边界，不仅数据集数量 |
| [2507.13833v1 DistFlow](https://arxiv.org/abs/2507.13833v1) | RL中心controller同时承载数据/控制→workers分散职责→重判中央化瓶颈；核心已存不等读完 |
| [2507.13868v1 When Seeing Overrides Knowing](https://arxiv.org/abs/2507.13868v1) | 图像覆盖知识冲突→定位heads并干预视觉/内在知识权衡→重判fusion与行为因果，不能凭相关性外推 |
| [2507.13871v1 Safety Certification in Latent Space](https://arxiv.org/abs/2507.13871v1) | 观测空间安全证明难→world model latent barrier/controller联合→需核学习潜空间如何继承安全；认证不等真实环境普遍保证 |
| [2507.13919v1 Levers of Political Persuasion](https://arxiv.org/abs/2507.13919v1) | 劝服reward/prompt优化可与claim准确率分离→优化代理目标的安全反证；不因政治应用标题关闭，不把样本结论外推所有劝服 |
| [2507.13949v1 Exploiting Primacy Effect](https://arxiv.org/abs/2507.13949v1) | fine-tuning与option位置偏差交互→同语义重排改变MCQA表现→评价混杂/位置增益非知识增益 |
| [2507.13984v1 CSD-VAR](https://arxiv.org/abs/2507.13984v1) | VAR尺度内容/风格纠缠→尺度交替优化、SVD抑leakage与KV增广→改变AR视觉factorization编辑取舍 |
| [2507.14000v1 Photonic Fabric Platform](https://arxiv.org/abs/2507.14000v1) | HBM计算固定配比→photonic远端memory解耦→容量/带宽拓扑可行性；模拟/估算不是真实硬件产能 |
| [2507.14049v1 EdgeVLA](https://arxiv.org/abs/2507.14049v1) | 动作AR位置预测延迟→取消末端位置AR/小LM→输出factorization替代；2024Workshop首公开疑点单独保留 |
| [2507.14067v1 VLA-Mark](https://arxiv.org/abs/2507.14067v1) | 视觉语言alignment水印与grounding质量冲突→熵调制跨模态水印→需核归属信号/能力边界；VLA此处非动作模型 |
| [2507.14111v1 CUDA-L1](https://arxiv.org/abs/2507.14111v1) | kernel自动优化奖励稀疏→contrastiveRL发现低层执行改进→需核正确性/预算；v1宣称17.7×mean/449×peak，现v12题摘3.12×mean/1.42×median，严禁混版 |
| [2507.14137v1 Franca](https://arxiv.org/abs/2507.14137v1) | SSL视觉cluster语义歧义/位置偏置→nestedMatryoshka多head聚类与debias→表征维度/语义可扩展性，非仅榜单提高 |
| [2507.13490v1 Revisiting LLM Value Probing](https://arxiv.org/abs/2507.13490v1) | value probe值对输入扰动高方差且弱相关实际选择→自述价值不能代签行为；API为v1完整题摘 |
| [2507.13525v1 Revisiting Prompt Engineering](https://arxiv.org/abs/2507.13525v1) | 推荐任务中复杂CoT可降低准确率且增加成本→否定所有任务都需复杂reasoning提示；APIv1，仅该任务/模型对照 |
| [2507.13591 FuSeFL](https://arxiv.org/abs/2507.13591) | server侧secureFL开销/全局模型机密被忽略→clientpair MPC+server限aggregation/routing→模型/更新保密与扩展职责；当前APIv3仅发现，v1未采用 |
| [2507.13598v1 GIFT](https://arxiv.org/abs/2507.13598v1) | concept erase被恶意finetuning恢复→双层免疫目标同时扰有害repr/保安全概念→改变可更新模型安全约束；APIv1 |
| [2507.13705v1 Consistent Explainers](https://arxiv.org/abs/2507.13705v1) | 解释声称评分策略而实际推荐不跟随→explanation与decision分离反证；不是推荐分数提升，APIv1 |
| [2507.13712v1 LLaPipe](https://arxiv.org/abs/2507.13712v1) | 每步advisor开销→历史experience distill与adaptive trigger→建议调用/探索预算的具体控制增量；不将数据准备领域成绩当贡献，APIv1 |
| [2507.13859v1 SPARQL Query Generation](https://arxiv.org/abs/2507.13859v1) | benchmark可能记忆→anonymized知识注入与原知识注入分开→KGQA portability与memorization混杂；不是仅领域生成任务，APIv1 |
| [2507.13933 Website Detection](https://arxiv.org/abs/2507.13933) | cleanprose检测在低base-rate/markup网页不适用→site多prosepage聚合与跨groundtruth→评价人口与误报边界；当前v2仅线索 |
| [2507.13942 Frozen Forecasting](https://arxiv.org/abs/2507.13942) | 单点futureaccuracy漏多峰分布→冻结backbone、轨迹/分布指标、固定latentreadout→隔离forecasting表征与language监督不稳定收益；当前v2仅线索 |
| [2507.14063 CRSA](https://arxiv.org/abs/2507.14063) | 单轮RSA无法表共享/私有belief多轮合作→rate-distortion gain条件于dialog→多轮语用推理定义，非医生场景类比；当前v2仅线索 |
| [2507.14263v1 NANDA AgentFacts](https://arxiv.org/abs/2507.14263v1) | agent identity/discovery动态变化→leanindex与可验证capability facts分离+CRDT更新→撤销/发现一致性机制，不沿用DNS名称当权限；APIv1 |
| [2507.19514v1 Wavelet Logic Machines](https://arxiv.org/abs/2507.19514v1) | quadraticattention替代→纯spectral可学习nonlinearity/basis→计算/表达分工替代；小GLUE不自动排除，ID延后不认首公开，APIv1 |
| [2508.00007v1 Agent Network Protocol](https://arxiv.org/abs/2508.00007v1) | agent身份、协商、能力发现接口分层→三层可组合协议→互操作与授权边界；先是发现线索，真实首公开不能由本API提交区间推出 |
| [2507.14248v1 AdViT](https://arxiv.org/abs/2507.14248v1) | 可解释输出被当安全检测→同时误导ViT与interpreter仍保持表面解释→解释正确外观不保证分类/攻击安全；APIv1完整题摘，ASR仅作者协议，不因医学示例排除安全反证 |
| [2507.13920 Causal Process Models](https://arxiv.org/abs/2507.13920) | dense/staticinteractiongraph→仅对象活动交互建稀疏时变causaledge并factorizeobject/force→worldtransition表示/长horizon成本取舍；当前v2仅线索，不把一般物理simulation混同全部AIforScience |
| [2507.13812v1 SkySense V2](https://arxiv.org/abs/2507.13812v1) | 每modality独立backbone冗余→统一transformer、adaptivepatchmerge与modalityprompt应对异分辨率/特征多样性→multimodal表示/参数复用条件；APIv1，仅遥感成立范围，不借Earth任务指标扩展Books |

## 明确关闭：已读完整题摘

| 身份（原件位于API条目；另存v1者注明） | 具体理由 |
| --- | --- |
| 2507.14241v1 Promptomatix（另存v1） | 成熟meta-prompt、DSPy与成本目标集成；题摘不说明新优化机制/有效条件/纠错证据；root FIRST认可关闭 |
| 2507.13736v1 SpiNNaker2 DNN Framework | DAY改判：完整题摘仅说明已有OctopuScheduler扩展、量化/lowering到单芯片部署，未说明新增调度选择或适用边界；“可到Transformer规模”本身不构成基础模型执行机制增量。保留原件，不再为该部署描述请求日期。 |
| 2507.13739v1 Diffusion-FSCIL | DAY改判：完整题摘是冻结生成模型、多尺度特征、蒸馏与少量训练模块用于FSCIL；实验声明任务成绩提高，但没有说明哪些生成偏差使旧方案失效及本机制改变的有效性条件。原留池理由将一般表示/replay原则当成本次新边界，予以关闭；不是因小模型或单领域自动排除。 |
| 2507.13618v1 Seed-X（另存v1） | 多语言翻译数据、CoT/RL与7B质量发布；题摘未提出区别既有做法的具体训练/系统机制或成立边界，不按机构/多语种指标准入 |
| 2507.13743v1 PRIDE（另存v1） | QueerNews上的LoRA vs10-token softprompt及WinoQueer指标；未分解本次parameterization/数据如何改变既有PEFT原理，局部适配比较本身不足，不以小实验拒绝 |
| 2507.13874v1 Geometry of Knowledge（另存v1） | 语义空间latentideation概念/初步原型；没有清楚的新可验证机制或改变既有diversity选择的证据，不能仅接知识图谱owner |
| 2507.13501 Encoding Syntactic Objects | Merge的函数/operad神经实现可能性，原文未连接到foundation模型形成/训练/系统选择；语言学数学模型不因wavelet词准入 |
| 2507.13544 Computational Conversational Systems | 对话图Filter&Reconnect与语义图/树指标，未证明新模型控制或执行可靠性；数据分析表示不是系统机制 |
| 2507.13550 GOFAI meets GenerativeAI | prompt抽Prolog+人验的成熟组合，无新增验证保证或失败边界；不把可解释/可靠宣传当证明 |
| 2507.13609 CoTasks | 把videoQA分成既有定位/跟踪/关系子任务的监督，主要任务指标提高，未给新的表示/推理成立条件 |
| 2507.13614 Linguistic Profiling | 文本风格统计/embedding差异，未改变模型机制或特定评价安全设计；不是所有生成分布比较都自动有项目贡献 |
| 2507.13629 Cybersecurity Survey | 应用/风险/防御综述归类，无具体新边界或反证，安全词不是自动准入 |
| 2507.13737 DailyLLM | 已有sensorfeature+structuredprompt做生活日志，1.5B与70B场景指标/运行速度不可当新的模型系统机制 |
| 2507.13768 Entangled Heuristics | 战略叙事启发式融合与semanticmetrics初步case，量子认知/Agent名词不提供执行机制/可靠性条件 |
| 2507.13814 CodeEdu | 成熟多agent角色、工具调用和教学计划组合，动态分工叙述未提供新增调度/故障机制 |
| 2507.13820 Team of One | 多VLM CoT+外部LLM选择融合是既有ensemble/judge编排，未说明新的适用条件/失效修正 |
| 2507.14256 Unit Test Generation | docstring/实现context/CoT在unit-test任务上的参数比较，未建立跨任务context表示或控制增量；不将高coverage当可靠性保证 |
| 2507.13834 Submodular Policy Optimization | diminishing-return action-set近似优化，题摘未说明对模型学习/表示/LLM执行的直接贡献，泛RL名词不足 |
| 2507.13846 Causal Transfer MARL | 碰撞绕障macro查询共享，主要局部导航环境迁移；不借Agent/worldstate词重入无关控制工作 |
| 2507.13858 InTraVisTo | logit-lens/内部流Sankey工具，新增可视化不自动识别因果或改变机制解释 |
| 2507.13881 SJT Skill Scoring | LLM做领域constructfeature提取，未提出通用模型评价盲区/新验证机制 |
| 2507.22910 Travel Industrial Experience | 不同模型/QLoRA vsprompt的旅行数据场景质量/资源对比，不足把收益归因新设计 |
| 2507.13468 ERR@HRI2 | 多模态对话错误数据/挑战增量；已有常见错误标签与metrics，未给新的模型/评价盲区证据，不因benchmark名自动保留 |
| 2507.13508 Fake or Real Space Texts | poisoning/overreliance检测竞赛任务说明，尚无新检测机制/已证实评价失效，安全标签不等贡献 |
| 2507.13607 BurstSR | 既有高阶ODE与一步蒸馏在burstSR组合，题摘只提供领域质量/速度，没有生成范式成立条件增量 |
| 2507.13797 DynFaceRestore | blur→timestep/localguidance的脸部恢复工程细化，未说明可改变基础生成/表示机制的增量 |
| 2507.13899 LiDAR Features | DepthAnythingprior+dualpathRoI/gate的检测组件组合；KITTI指标不证新fusion边界 |
| 2507.13910 PARK | 既有translationalKG embedding与retrieval融合用于academicpersonalization，无新的检索生命周期/质量成立条件 |
| 2507.13913 Political Classification | 拼数据与leave-one-out训练的任务泛化，未修正foundation模型/评价机制 |
| 2507.13937 Marcel | 大学FAQ映射与成熟RAG组合，改retriever任务指标不是新权限/检索机制 |
| 2507.13941 Brain Representations | fMRI皮层路线发现，AI模型仅作为比较工具；AI forScience暂缓，不经representationowner重引 |
| 2507.13957 DUALRec | LSTM+fine-tunedLLM电影推荐组合，缺具体新表示/学习机制与条件 |
| 2507.13966 Domain-specific Superintelligence | 主要medicalKG curriculum与ICD/medicalQA结果；知识图谱通用愿景未提供独立基础机制证据，不通过Data节点重引暂缓医学应用 |
| 2507.13998 ParallelTime | localattention/Mamba的input-dependent加权用于普通时序预测，题摘未直接支持当前foundation/LLM状态边界，不能只作系统类比 |
| 2507.14022 CPC-CMS | 专家权重多criteria对sentimentclassifier选型，成熟decisionaggregation场景比较 |
| 2507.14023 Conformal Bounded Regression | boundedresponse transformationregression的conformalscore理论；未给模型训练/输出分布或系统决策的直接关系，不能借uncertainty词准入 |
| 2507.14270 APTxNeuron | 现v7新增trainabletanh乘性单元与MNIST指标，当前题摘不足识别相对成熟参数化激活的新增机制/稳定条件；不因小模型关闭，亦不把v7回填v1 |
| 2507.14088 DPMT | 双过程ToM加多尺度心理建模，题摘只给humanAI任务收益/组件消融，未清楚新增执行或可靠性机制 |
| 2507.14126 CaRTeD | irregularEHRtensor分解/causalnetwork恢复理论，主要领域phenotyping，未直接服务foundation训练/表示机制 |
| 2507.14024 Moodifier | 情绪annotation+CLIPfinetuning+编辑编排，组件组合/8M数据规模不是生成机制增量 |
| 2507.14069 EdgeSNN Survey | EdgeSNNtaxonomy及常见hardware-aware双轨建议，尚无具体新比较盲区证据/机制变化；不因neuromorphic排除整个研究方向 |
| 2507.13480 Local Smoothness Detection | scattereddata的sampletwaveletregularity检测，题摘未直接改变foundation学习/表示或系统执行；不因linearcomplexity就联想到LLM加速 |
| 2507.13524 Humans Prefer TrustworthyAI | 混合社会partnerselection的人类行为实验，未新增模型/系统机制或模型评价可靠性反证 |
| 2507.15878 Salience Adjustment | facial/context emotion用既有Bayesiancue与VLM动态加权，prisoner'sdilemma指标未给基础融合机制新边界 |
| 2507.14097 Human Motion Simulation | 用LLM改写到MotionGPT词汇并在8工业动作比joint误差，既有模型编排/验证组合不证明新生成或物理控制机制 |
| 2507.13841 Narrative FairPlay | 信息论单/双reader的文学surprisecoherence分析，LLM作读者/评价器；未连接当前模型形成或系统机制的直接变化 |
| 2507.13620 Tri-GFN | GCN/AE/GraphTransformer三模块聚类fusion组合，任务准确率未说明新增基础表示/优化条件 |
| 2507.13625 BifrostRAG | constructionregulation双graph内容/文档结构+vector/traversal的混合检索，题摘仅给领域QA指标，未分离新增机制或跨技术文档成立边界；通用蓝图愿景不代替证据 |
| 2507.13599 Deblurring TexturePrior | diffusionprior+textureencoder/attentionfilter/waveletloss用于去模糊的组合，原文未给基础生成/表征通用选择的具体新增条件 |
| 2507.14032 KROMA | ontologybisimitilaritypruning+RAGpromptenrichment/refinement的既有组件组合，通信/匹配指标未建立新模型检索机制边界 |
| 2507.13769 Spectral DiffusionPrior | hyperspectral重建的diffusionprior注入，领域PSNR改善不建立当前基础生成机制增量 |
| 2507.13708 PoemTale | 既有promptrefine与consistentselfattention的诗歌图像组合和1111诗数据集，未给新增生成机制/失败条件 |

## 标题明确范围外的旁支

四个主题查询中的下列题名已明确为科学/医学/领域应用，不展开附录、日期或Books；这不是声称它们无学术价值。其原始完整题名/摘要仍在Atom/API文件，不从关键词做未知内容判断：

- 2507.13459 contacting deformable bodies surrogate；2507.13580 chemicalfragment lead design；2507.14245 nanomaterial-protein interactions；2507.19515 influenza forecasting；2507.13646 protein sequence review；2507.13655 ICU；2507.13742 biomedicalontologyalignment；2507.13805 neural potentials；2507.13822 drugsideeffect；2507.13956 Alzheimer；2507.13993 ribfracture；2507.14267 DFTmaterials；2507.14031 chestEIT；2507.14045 biomedicalbench；2507.14079 clinicalnotes；2507.14096 biomedicalPLABA；2507.21123 Synthea；2507.17852 drugdiscoveryautomation；2507.13950 proteinconformation；2507.13974 melanoma；2507.14050 dermatology。
- 2507.13511 trafficcoordination；2507.13647 swarmdrone trajectory；2507.13685 loandefaultprediction；2507.13729 traffic-scenarios；2507.13732 legaljudgment；2507.13827 scientificarticleQA；2507.14017 mobilityprediction；2507.14107 bridgeNDE。主题任务指标/已有AI使用未表达模型或系统机制增量，不经Agent/Data/Evaluation重引。

121个发现家族的标题均已浏览；相关或含糊题摘按上述具体准入/关闭理由处理，明确领域旁支限标题关闭，不穷读附件。宽命中边界按任务主题收窄；没有用“非LLM”“已有owner”“仅一个seed”“benchmark”作为自动排除规则。所有保留仍受公开日期障碍隔离，未把121个发现计为当日事件。

## 已核非arXiv和首次公开

- OpenAI [AI as the greatest source of empowerment for all](https://openai.com/index/ai-as-the-greatest-source-of-empowerment-for-all)：RSS原始 `Mon, 21 Jul 2025 00:00:00 GMT` →07-21 08:00BJT落窗。题名/描述为使命与社会赋能，不含模型系统机制；按范围关闭，不为凑候选收录。
- Apple2507.13575：官方作者页明确July17 technicalreport releasedtoday；不依arXiv新ID改归属。只保留原始首公开证据 `apple-update.raw`，没有审别日/旧Weekly。
- 当前v1题摘轻查未见撤回标记；有版本实质差异信号的CUDA-L1/NABLA/DistFlow已保留版本边界，不把metadataUpdated当发布日期或revision解释。
