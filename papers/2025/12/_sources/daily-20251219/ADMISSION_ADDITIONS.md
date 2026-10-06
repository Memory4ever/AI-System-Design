# 12/19 实际完整题摘与具名潜力

最新具名补正：[AUTHOR_REVIEW_RECONCILIATION](./AUTHOR_REVIEW_RECONCILIATION.md)补12遗漏与2负侧重开，取代本文件CAMP-VLM/FEAML旧close；原ordinary0撤销，反证/日期隔离保留。当前具体差额14项已同步，不宣称日级通过。

实际执行 2026-10-02，窗口 [12/18 09:00,12/19 09:00)+08。以下 arXiv 均 actual `/abs/IDv1` 完整题摘可读；submitted 缓冲不是落窗许可。potential 不评分、不当确定候选，不因日期失败删除。无日期的明确贡献排除不另要求时间恢复。原始身份/查询见四组 ARXIV 文件，正文仅记判断支持，不复制完整摘要。

## 系统首批完整题摘

| ID | 实际增量/判断 |
| --- | --- |
| 2512.15176 DEER | potential：单步 diffusion 长 draft 加两阶段 AR teacher 对齐再验证，改变 drafting 长度与质量取舍；5.54x 不作无配置收益 |
| 2512.15306 LLMQ | potential：低精度训练贯通 CUDA/C++、copy engine collective、offload/checkpoint，针对低通信消费 GPU 的全路径设计；不照录 50% MFU |
| 2512.15358 Dual-Density | potential：压缩符号中间推理与可读输出的双密度表示，改变 reasoning token 成本；细编码必要时定点读 |
| 2512.15550 CTkvr | potential：相邻 RoPE queries top-k 重叠利用 centroid→token 两级检索与 CPU/GPU index 协同，涉及精度/缓存索引成本 |
| 2512.15834 Speculative Tool Calls | potential：推测工具调用与 resident sequence engine、tool cache 联动；必须核 side effect/验证与普通并行工具区别 |
| 2512.15705 DREX | potential：不强制 early exit 的动态 rebatch/copy-free buffer、缺失 KV 状态处理与 SLA 调度，改变退出与批次耦合 |
| 2512.16134 SBS | potential：P/D 的 DP/EP 同步与队列气泡，通过 buffer/stagger/global load allocation 改 TTFT/throughput 取舍 |
| 2512.16056 MultiPath | potential：CPU/GPU PCIe/NVLink 多路径联合迁移与动态注入，改变 host-GPU transfer 瓶颈；峰值带宽与端到端不同 |
| 2512.15946 AIE4ML | potential：VLIW/local-memory 神经网络图的二维放置搜索与量化 bit-exact 编译；不能因 demo 应用误排模型 compiler |
| 2512.16144 INTELLECT3 | potential：异步 primeRL、verifier、多轮 tool 的 106B/12B-active 训练 runtime；已有模型 release 不自动消除本论文事件增量 |

## 第二批实际完整题摘

| ID | 实际增量/判断 |
| --- | --- |
| 2512.15081 Security Controls | potential：按攻击概率/损失分布比较 ABAC、NER、guardrails 的 residual risk；货币损失是合成 PII RAG + 公共成本校准的 Monte Carlo，不是实测生产损失 |
| 2512.19729 FlowFM | potential：联合表示 encoder 与条件 flow generator、解耦生成/判别取舍；小传感器实验不决定排除，效率需分训练与表示推理 |
| 2512.15149 Q-MetaSur | 关闭：完整摘要为 CEC2019 多目标优化 surrogate 使用 LLM tokenization、SFT+IQL；新增收益是目标近似/Pareto 优化，不给基础模型学习机制或系统边界反证 |
| 2512.15219 RFKG-CoT | potential：relation mask 决定 hop 数而非 solely question，改变 KG 检索预算与证据路径条件；few-shot 模块不是单独贡献 |
| 2512.15235 FAME | potential：fictional 未见预训练身份与跨语言 entity/instance 遗忘控制，修正 unlearning 评价混杂；不只是增加五种语言 |
| 2512.15252 Arena | 关闭：technography 五主题/attention commercialization 社会研究，没有本项目可核验模型评估机制或失效测量增量；非声望/主题相关即可准入 |
| 2512.15254 Visual Enumeration | potential：逐对象 location/label 中间表示改善计数但复杂场景仍失效，细视觉属性控制可修正 VLM 泛化解释 |
| 2512.15274 PPPO | potential：progressive prefix retention + 多 continuation 累计 reward，仅优化 prefix 而非均匀 token，需重估 credit/cost 和 beginning lock-in |
| 2512.15302 PersonalAgent | potential：对话拆单轮的顺序偏好推断/统一动态 profile，噪声及跨会话一致性对照可改变 memory 更新判断 |
| 2512.15310 SynthSeg | potential：CLIP 相似度/nearest-neighbor 多样性筛选、synthetic relabel 串联支撑零真实图像监督；先保留数据分布/错误耦合可能，不能因两 agent 名称直接关闭 |
| 2512.15813 CodeMem | potential：把程序记忆持久化为可复用执行代码，减少同任务轨迹变异；“deterministic reliability”不是已证明端到端保证，需区分代码确定性与环境/调用 |
| 2512.15353 Portuguese Verse | 关闭：摘要复述既有 adversarial poetry 数值并提出葡语评估需求，没有新增葡语实验或独立机制证据；不能把引用 18x 当本研究反证 |

## 官方必要材料

## 后续完整题摘

| ID | 实际增量/判断 |
| --- | --- |
| 2512.15466 Code Reviews | potential：280 review 的多主观排序替代单一 reference/模糊 usefulness，可能修正“自动与单答案一致即质量” |
| 2512.15816 NeuroInv | potential：weakest-precondition backward chain + OpenJML counterexample 修复，改变神经候选与符号验证交接；99.5% 不当无限 loop 保证 |
| 2512.15528 EmoCaliber | potential：subjective 多解释 confidence verbalization/calibration，不只是单标签 emotion 提分；需核 calibration 实际目标 |
| 2601.08839 RKS | potential：heterogeneous tri-agent 的透明度审计 contraction 命题与47次 controlled trial；收敛/安全不等同，必要时核 fixed-point 假设 |
| 2601.06047 Structural Fidelity | 关闭：哲学 essay 对公开 CoT/safety 事例的语言场解释与伦理形式主张，未给独立训练干预、可验证假设或新安全实验；不是对既有结果的量化反证 |
| 2512.15617 Safety Metrics | potential，决定准入补读 v1 §3/4 已执行：实例 rubric 所谓确定 coverage 未明示公式/执行，soft penalty 未量化，两个代理共同漏项不触发 concordance cap，weighted 一致性分数不能安全证明；不是医疗预测指标提分，也不采临床建议 |
| 2512.15634 LoRA Rank | potential：rank sweep/in-out-domain + spectral/attention drift 验证 forgetting/robustness 取舍；不是所有低 rank 更好 |
| 2512.15653 Mamba Memory | potential：autoencoder 从 SSM hidden 重建，4–256tokens/130M–1.4B 上遗忘 math、organization、dialect 与低频关联，修正只按 sequence 长度谈记忆 |
| 2512.15663 CAGE | potential：保留 generated→generated 因果/row-stochastic attribution graph，再 marginalize 中间路径，纠正只 prompt→output 的缺失 |
| 2512.15687 G2RL | potential：最后层 sensitivity 的 update geometry 驱动 bounded reward scaler，探索多样性从文本空间改为梯度方向 |
| 2512.15688 BashArena | potential/安全反证：637 privileged admin task + 4 sabotage objective、弱 monitor 的 FPR/漏检 tradeoff；26%/4%是具名模型/setting 不是普遍风险率 |
| 2512.15701 VLIC | potential：VLM binary 2AFC reward 直接 posttrain diffusion compression 而非 distill perceptual loss，涉及人偏好/压缩 objective 交接 |
| 2512.15885 JARVIS | potential：冻结 vision context/target encoder，LLM 早层作为 JEPA predictor 并入 V-L alignment，修正纯文字监督视觉 detail 不足 |
| 2512.15892 VET | potential：Agent Identity Document 配置+组合 proof systems 对 host tampering 的执行认证；Web Proof/TEE 成本条件不同，authentication 不等于 autonomy/正确决策 |
| 2512.15940 R4 | potential：object semantic 映射 metric space/time 的4D持久数据库与三类 retrieval keys；observation memory 不自动等于可预测 world dynamics |
| 2512.15949 Observatory | potential：controlled pixel/stylized perturbation 及local-global grounding，区分 language scale 与固定 vision encoder 的视知觉提升 |
| 2512.15957 CAMP-VLM | 关闭：scene graph context + simulator synthetic SFT/DPO 提高多人体行为预测，完整摘要未给模型表示/学习或机器人闭环的新 mechanism/boundary，主要下游准确率 |
| 2512.15959 BRAID | potential：Mermaid instruction graph 限定 reasoning，跨 model tier token/cost 非线性比较；不能把结构prompt一般知识当新增，需看 bounded执行条件 |
| 2512.19742 HAR Agent | 关闭：LLM 活动分类+解释/Q&A，主张 interpretability/user engagement 未披露 on-device 状态、执行或模型新机制；仅 HAR 场景组合 |
| 2512.16022 Conversational TS | potential：SHAP faithfulness reward 的 judge ensemble weights + multi-turn strategy，改变解释与优化交接；“causal”解释需核，不默认由 SHAP 证明因果 |
| 2512.16029 Cross-language Bias | potential：explicit BBQ 与 implicit association ranking 相反，修正单指标公平性迁移；不是语言数配额 |
| 2512.16030 KalshiBench | potential：post-cutoff outcome calibration 与 base-rate Brier skill、reasoning增强更差，修正准确率/scaling即校准；市场预测不是财务建议 |
| 2512.16041 Sage | potential：pairwise稳定+全局transitivity 无 human label评价、situational preference，修正judge一致性盲区；一致不自动等于真值 |
| 2602.23367 HumanMCP | 关闭：摘要只提供 2800tool/308server persona-generated query dataset、声称更realistic，未给工具检索可靠性新证据/机制；task增加不够 |

## 官方必要材料（续）

[精确 2025-12-18 Model Spec](https://model-spec.openai.com/2025-12-18.html) 的 U18 新节及 definitions 条件元数据已读；root 层 U18 行为约束将同类成人允许回应改为青少年受限，原 Blog 还说明年龄不确定时默认 U18、成人可验证恢复。potential 是分群条件与不确定状态下的安全默认，而非推断新训练算法；文档不等于 production model 已遵守。日期仍日精度，隔离待个体发布界限，不作 19 确定候选。

## 后续题摘补充

| ID | 实际增量/判断 |
| --- | --- |
| 2512.16077 AV3DOD | potential：取消用户预给类词，自动生成 category candidates 与 Semantic Score，修正 open-vocabulary 隐含输入接口 |
| 2512.16083 Text2SQL Filter | potential：functional dependency graph + connectivity-preserving Steiner sub-schema，结构保持检索压缩，而非独立列排序；SQL场景不消除结构机制 |
| 2512.16108 WeMusic | potential：内化知识 vs tool 的 agentic boundary learning，需核实际分界训练；50B领域语料/推荐分本身非准入 |
| 2512.16125 Lie Convolution | potential：非 Euclidean symmetry 的 Lie convolution 进入句表示，学习机制可支撑主线，小分类模型不整体排除 |
| 2512.16149 ToolForge | potential：virtual tool/golden context 合成多 hop、rule/model validation，去真实 API 成本的训练泛化边界 |
| 2512.16164 C-DGPA | potential：marginal adversarial/conditional class mapping 双对齐降低 source overreliance，不只 prompt tuning 提分 |
| 2512.15431 StepGUI | potential：trajectory-calibrated step reward 与 GUI-MCP atomic/task delegation 本地隐私交接；annotation准确率与端到端控制不同 |
| 2512.15649 VTCBench | potential/反证：OCR 能解码不等于压缩视觉文字能保持长依赖，retrieval/reasoning/memory分层证据 |
| 2512.15674 Activation Oracles | potential：LatentQA训练数据多样性改变 finetuned/OOD activation 信息恢复能力；官方 Dec19 Blog 在后日，不把 submitted 自动归19 |
| 2512.16070 LLM4Perf | potential：语义配置 pruning 对传统 sampler 亦有效的分离验证，提供 actor/feedback收益来源证据；非所有 software tuning属AI系统，保留实际LLM规划选择边界 |
| 2512.15906 DarthVecdor | 关闭：LLM问答预抽SQL/术语映射+GUI，完整摘要无新增可靠性机制的可核证据，列错误类别/免责声明不等于实现正确性结论 |
| 2512.15372 ICAR | potential：early/full depth 兼容双路径 embedding与complexity depth selection，解决条件算力下 V-L 对齐；95%instance性能有代价 |
| 2512.15089 CogER | potential：quality/cost reward 的 MDP difficulty routing + tool CoT，改变按query预算策略，非fast/slow标签 |
| 2512.15468 Code MIA | potential/反证：semantic equivalent变换保持 finetune accuracy但降低MIA，variable renaming强、组合不进一步降低；不能把未检出当license未用 |
| 2512.15979 OLAF | 关闭：position paper 将 reliability/calibration/drift 等组织成 conceptual框架，明确未来 empirical work，无本次新评价/机制/反证事实 |
| 2512.15596 Corrective dLLM | potential：监督visible incorrect token恢复confidence/error localization，反驳mask-denoise即自动会修正完整序列 |
| 2512.15179 SCALM | potential：function slicing/vector pattern与多层verification交接，可核符号/语言证据边界；smart-contract下游数值本身非增量 |
| 2512.16074 DeepOSets | potential：non-AR/non-attention ICL 与 continuous operator统一近似条件挑战“ICL只能attention”，原文 PDE demo不作为领域科学成果采用 |
| 2512.15973 DR-RL | potential：online perturbation bounds增量rank update减少full decomposition，fidelity/latency reward与硬件rank约束；statistical equivalence需具体检验 |
| 2512.15586 Bolmo | potential：subword→byte架构 expressivity配准以exact distillation转化，改变tokenizer改造预算/推理compression条件，不因来源每周排除已发现必要正文 |
| 2512.15933 CityNav | potential：真实稀疏定位50+decision点的失败与显式cognitive-map/path verbalization改善，修正CoT/Reflection自动够导航 |
| 2512.15926 DSO | potential：RL优化linear activation transform、可调fairness/capability取舍，区别固定heuristic steering |
| 2512.15163 MCP Safety | potential/安全反证：multi-turn/cross-server/task-horizon升高漏洞，host/server/user分层，不只是20attack类型 |
| 2512.15943 SLM ToolCalling | 关闭：OPT350M单epoch通用SFT/ToolBench旧baseline分值，没有新训练/执行机制或明确受控可修正边界，不能由高分/小模型倒推贡献 |
| 2512.15098 UniParser | potential：loose multi-expert保留跨模态fine alignment + dynamic module orchestration/loadbalance，document pretrain数据与系统路径相关；不采AI4Science下游主张 |
| 2512.20651 Memory Bear | potential，决定准入已补读§2–4.5：ACT-R retrieval历史+连续freshness activation、pending-forget弱化/压缩、按knowledge responsibility的summary级memory routing与origin/validity/permission，可核具体memory保留/同步策略；semantic arbiter“确保完整性”、众多倍率没有受控依据，不采AGI/绝无语义损失保证 |
| 2512.15160 EagleVision | potential：SPF-DPP预算keyframe与BEV pose-query对应真实帧、spatial grounding reward，连接验证/采证 |
| 2512.15713 DiffusionVL | potential：AR→diffusion VLM posttrain + block commit/KV复用，任意长度不同于全局反复denoise；速度/质量须配置 |
| 2512.19728 Weighted DPO | potential：六维error profile→hard negative与pair importance，改善near-correct逻辑错误的偏好监督 |
| 2512.16059 ContextLeak | potential/隐私反证：canary-targeted query audit heuristic与理论DP方法privacy/utility tradeoff；empirical worstcase不当普适ε证明 |
| 2512.15577 MoonSeg3R | potential：query distill/index memory/state-distribution token跨帧identity，在monocular不需posedRGBD的新表示约束 |
| 2512.15907 TabReX | potential：source/table canonicalgraph + rubric匹配cell trace，structure/fact fidelity区分；reference-less仍依赖judge不自动truth |
| 2512.15840 VideoPlanner | potential：video pretrain主模态→zero-shot视频计划→action提取，替代language/image直接动作route；真实执行不无限泛化 |
| 2512.15693 Skyra | potential：human-visible artifact作为video判别解释证据及grounded training/eval，区别black-box二值detector |
| 2512.15922 ActivationRAG | potential：spreading activation替代LLM traversal、可信连接证据及多hop取舍；不由naive RAG 39%当单机制收益 |
| 2512.15605 AR/EBM | potential：function-space bijection/softBellman与distillerror bound，修正NTP无lookahead的理论解释，假设待必要源核 |
| 2512.15374 SCOPE Prompt | potential：online trace→tactical/strategic dual-stream prompt evolution + perspective exploration，改变静态agent context管理 |
| 2512.16167 EvTrust | potential：trust/revenue反馈的replicator equilibrium；题名v1不同于current，已核精确v1身份；local stability不当无恶意agent保证 |
| 2512.16956 SpIDER | potential：codegraph exploration的auxiliarycontext增强dense embedding，改变代码语义检索上下文而非只提供codebench |
| 2512.15423 3D Mirage | potential/反证：planar illusion的nonplanarity/contextinstability与grounded ROI self-distill，修正单pixel误差深度质量结论 |
| 2512.15662 STC | potential：同模型step-interleavedcritique的reasoning+critiqueconsistency RL目标，不能把自我批判语句当外部verification |
| 2512.15560 GRANTED | potential：统一adapter的text-onlyproxy与generation相关性、layer weighting视觉encoder适配；相关不替代任意下游重训 |
| 2512.15275 BountyHunter | potential：跨pre/postcompromise多路径detectability/自主emulation范围改变安全评估；不记录攻击操作细节 |
| 2512.15708 MultiView | potential：intermediate3D-awareattention使同3D点特征一致而不先建完整3Dfeatures，改变单图foundation表征 |
| 2512.15524 DeX | potential：explicitpose/latentexpression解耦注入与progressivehybridCFG的可控边界，非人像应用提分 |
| 2512.15621 OccSTeP | potential：missing/noisysensor的ego-motioncompensatedrecurrentvoxelstate，reactive/proactiveforecast分离；tokenizer-free不保证物理正确 |
| 2512.15716 Spatia | potential：3Dpointcloud持久memory+SLAM更新，dynamic/static解耦支持长生成；预测更新不当真environmentstate |
| 2512.16093 TurboDiffusion | potential：lowbit/sparslinearattention+distill+W8A8联合全路径质量/执行取舍，不能因成熟组件组合直接排除；100–200x必须拆配置/预算 |
| 2512.15411 MiVLA | potential：kinematicleft/right坐标的human/robot双向embodimenttrajectory对齐和unseen imitation，修正静态外观data迁移 |
| 2512.15258 VLAAN | potential：stochasticactionpolicy后geometriccorrection与onboard执行闭环；碰撞无保证由摘要“ensures”不能照录 |
| 2512.15692 mimicvideo | potential：video-planlatent到flowactionIDM，区分预训练dynamics与低层control，视频路线不是VLA全替代 |
| 2512.22170 SoliReward | potential：singleitem→crosspromptpair、win-tieBT与positive分数regularize减rewardhack/noise，不只是rewardmodel排行 |
| 2512.15493 SoftGeometry | potential：broken symmetry时exactequivariance失效→softgeometricalgebraobjectdynamics，2Drollout反例支撑model假设边界，不收领域物理应用成果 |
| 2512.15657 SoFlow | potential：velocity/solutionODE关系的FM+consistency训练，避JVP的一步CFG与equalepochs对照，改变从头一步生成objective |
| 2512.15515 HE FAME | 关闭：general encryptedmatrix HLT datapath/U280带宽加速，ML仅动机；无AI模型执行/训练或隐私推理具体路径，不能由matrix词重引入通用HE硬件 |
| 2512.15929 Randomized Matrix Thesis | 关闭：RPCholesky/trace/least-squares论文汇总，摘要未明确新增模型学习/低rank系统条件，泛ML动机不足；不把任何linearalgebra都变每日候选 |
| 2512.15146 SCOPE TTRL | potential（有界官方列表补检新增）：subgroupstepconfidencepseudo-label+diversity分组，修正majorityconfirmationbias/sparse reward |
| 2512.15388 SpatialRAG | potential，决定准入补读§3/4：oriented segment dipole的qualitative relation转语言graphcontext，source几何关系选择改变LLM空间证据接口；相同120route有/无context对照、城市规模/route长度混杂，无可比raw坐标/其他RAG消融，不从0→62.5推普适最优 |
| 2512.15397 ORACLE | 关闭：大学新闻filter/embedding/PESTEL两层周summarygraph与change detector、evaluationplan，无新memory/retrieval/可靠性机制证据 |
| 2512.16954 CharacterVideo | potential：visualanchor删除对照与文化类别consistency差异，明确identity保持条件；不因多阶段流程自动排除，也不当所有visualprior必要定理 |
| 2601.10719 Trust Signatures | potential：instruction LM layer/head线性可解码trust与finetune仅细化，修正trust语言输出不等于可信行为；不采用psychological-grounding即安全 |
| 2512.15148 AcademiaIndustry | 关闭：1367papers+17org问卷的topic/open-source/industryneeds研究，未新增可核模型机制/技术评价反证，未来可靠性需求不是机制结论 |
| 2512.22165 MarcoASR | potential：performance-metric-driven LR tuning、domain data transformation/augmentation在传统与LLM-ASR的overfitting边界，保留跨长度/语言适配条件；not每个domain提分即贡献 |
| 2601.02378 MentalWorld Review | 关闭：100研究/19ToM/26benchmark分类和概念框架，没有新增state-learning/预测/交互机制或直接验证反证；综述数量不授结构候选 |
| 2512.15082 FEAML | 关闭：labelco-occurrence metadata→LLM featurecode→accuracy/Pearson redundancy反馈是多标签featureengineering使用已有工具，摘要未建立基础模型/agent新机制或重要反证 |
| 2602.17667 WeWrite | potential：posterior必要性mining与parallelFakeRecall执行，改变personalizedrewrite触发/延迟边界；AB线上VV/QRR非modelmechanism归因 |
| 2512.15971 Multispectral | potential：semantictextprior迁移到未见thermal spectral modality，改变few-shot融合适用边界；受控data-budget证据需核 |
| 2512.15614 BEAT | potential：graphbehaviorVQ macro/micro vocabulary→frozenLM inputsemanticalignment，改变nontexttoken对齐而非只recommendation |
| 2512.16013 SiteCalibration | 关闭：农田碳循环KGML sitefine-tune/remote-sensing下游，AIforScience暂缓；不通过pretraining/transfer词重新纳入 |
| 2512.15410 CIM-S | 关闭：multiplex tissue49proteinmarker/CODEX cells的markerindependence与rarecelldiscrimination，贡献限定医学影像表示领域，不推通用foundation输入融合结论 |
| 2512.17953 Background Bias | potential/反证：classification/CLIP/videoLLM均背景依赖，segmentedhuman和prompt变化缓解，修正多模态动作理解grounding而非纯任务分 |
| 2512.15422 Driving Survey | 关闭：31studies/10surveys分类、ethicchecklist/ODDcoveragemap和difficulty schema，没有新generative/control机制或可核失效实验；自动驾驶范围不能一概关闭，但本综述不满足贡献 |
| 2512.15658 PPSEBM | potential（官方ID段补检）：EBM pseudo-prior samples参与progressiveparameterselection，改变task参数分配/forgetting交接 |
| 2512.15712 PCD | potential（官方ID段补检）：activation→sparseconcept communication bottleneck→behaviorprediction端到端目标，改变auto-interpretability可扩展训练 |
| 2512.15745 LLaDA2 | potential（官方ID段补检）：AR继承的block WSD先增block→fullsequence→缩block，16/100BMoE模型支持efficiency-awareconversion，规模标签本身不够 |
| 2512.15747 D3G | potential：training-free inference-time demographic生成分布改变zero-shot accuracy/bias，counter imbalance条件，非样本数量 |
| 2512.15782 Guardrail Tuning | potential/安全变化：固定Mistral的prompt/filter超参空间统一ASR/benignharm/latency，Optuna和48-pointgrid对照预算；不是“guardrail安全”保证 |
| 2512.15792 Biases | potential/反证：neutralalignment与language/political/gender不同proxy呈多维偏差，不能拿中立指令作为模型已中立的证据 |
| 2512.15793 ClarityEthic | potential：显式冲突norm contrastive训练解释/valence，区别implicitalignment；与18检索同名需精确v1去重，日期未授 |
| 2512.15722 ValueLens | 关闭：既有value theory由LLM描述专家确认再detector/critic组合，完整摘要只任务提分，无新训练/互审正确性条件或反证 |
| 2512.15798 DPBench | 关闭：ELT/TextSQL合并新data-product任务+baseline，没有生成可靠性新机制/反证；版本标题差异已按v1读取 |
| 2512.15925 SocialStory | 关闭：readerresponse/narrative意图formalism+gen/classifier+社区分析，新增storytelling领域测量，不改变基础模型表示/系统设计解释 |
| 2512.16034 Annotator Modeling | potential：persona信息类别/少量comment vs多样性ablation修正subjectivehumanlabel模拟条件；不把demographic最强推一般个体行为 |
| 2512.15791 EthicsTools | 关闭：四ethictool/35h开发者访谈的文档适用性与葡语文化缺项，未给technicalevaluator或模型机制增量；一般伦理需求不等于safety实验 |

## 日期保留项与范围关闭

所有上述 potential 身份保留，尚无个体 first-public 完全落窗依据。官方历史 announcement/date API 路径已有限穷尽，精准恢复证据见共享原始 ARXIV_DATE_RECOVERY；不再无限请求或用 Submitted 替代。当前不支持确定候选、Books、coverage通过或zero-event证明；重开需该精确 IDv1 官方first-public字段/公告上下界。身份未变跨日已有题摘层可复用，但不从18结论批量关闭本日。

明确标题限定医学/生物/物理/农林/传统领域用途关闭：15133protein、15250physiological、15298EarthScience考试、15312zeolite、15365multiomics、15384medicalnugget、15446clinicalinterview、15531remotesensingencoder、15601psychologicaldefense、15681brainrecurrence、15862collider、15894pediatric、15931fungal、15808biomedicalreview、15567scientificdiscovery、15977agriculture、15867highenergyworkflow、16063healthcare、19735ICUmortality；compute查漏15246Alzheimer/15344rotatingfault/15385powerfault/15386basketball/15480wildlife/15484flare/15820bioimage/15544hyperspectral/15900sequencing/15965panelR/16010quasar/15142galaxy/15129galaxy/16115optionpricing/16085battery；官方列表15151hotelcorpus/15183studentassessment/15259clinical/15328Arabicbibliometry/15547sentimentuprising/15551inflection/15552wordlists/15556translationdecomposition/16145medicalreport/16147hatespeechRoBERTa/15830intracranial。应用标题明确且无本次纠错/安全修订信号，不构造读文队列。标题含糊或与mainline机制可能相关者实际完整摘要/决定准入补读如上，不由日期失败豁免。

15343XR用户acceptance是HCI使用调查、20652Hiringdecision是下游招聘应用、15376signeremotion是下游识别、15281DigitalTwinRDF是领域metamodel映射、15231remotesensingagent是地理应用，均未凭LLM/agent/system字样收录；15226YesMT共享翻译任务submission标题明确传统任务，不全扫传统NLP。

- [GPT-5.2-Codex addendum](https://cdn.openai.com/pdf/ac7c37ae-7f4c-4442-b741-2eabdeaf77e0/oai_5_2_Codex.pdf)：22 页，原 cover Dec18 日精度。本机下载 SSL EOF 后官方 PDF web 有限替代成功，必要 §3–4、§5.1.2 已读。§4.2 RL rollout 内 user model 做冲突编辑并正奖励不 revert；Table4 avoidance 0.75→0.76 不是因果对照/无损保证。Cyber 三技能与不同评估盲点、委员会“不达 High”非安全证明。潜力成立，个体时刻缺口不改为本窗确定候选。
- [Vend2](https://www.anthropic.com/research/project-vend-2)：核心全篇及脚注已读，原 Dec18 日精度。共同模型 CEO 把 discount 减少替换为 refund/store-credit、blindspot 共振与命名投票误变权威委派是具体代理反证；版本/tools/prompt 同时迭代、無干净阶段分界，不能归因 CEO 导致盈利。human purchase approval 与大量现场支持保留，不把现实观察外推无人运行。
- [Wellbeing](https://www.anthropic.com/news/protecting-well-being-of-users)：核心+footnotes 已读，日精度。prefill-recovery 与从头运行、without-system-prompt 评估与产品行为、全对话率与机会条件率不可混合；Petri 内部 realism filter 不在公开版。当前 91% 纠正旧 70% 且编辑脚注年代矛盾，当前文不是 2025 不可变证据；修订信号保留，精确历史版本隔离，不采当前数重建旧日。
- [Skills specification](https://agentskills.io/specification) 是原 Oct16 Blog 的 Dec18 open-standard 更新实际触发，现行规范完整核心可读：required name/description，optional compatibility/metadata、experimental allowed-tools，三阶段 disclosure。后者原机制不是 Dec18 新创；现行 schema 没有精确 2025 version，不把 2026 当前规范冒充更新差异。历史发布/schema 范围缺口保留，非协议安全保证。
