# 12/15 实际题摘筛选与日期隔离

Gibbs；本日独立入口见 [SOURCE_SCREEN](SOURCE_SCREEN.md)，首批校准见 [ADMISSION_CALIBRATION](ADMISSION_CALIBRATION.md)。以下相关或含糊条目已实际读完整 **exact v1** 题摘；多次输出截断处已定点重取，不把截断摘要算完整。明确标题范围外只做题名判断，未扩全月逐项队列。无当窗首次公开证据，不评分、不称入选/证据完成；potential 是具体增量待日期恢复集合，不是本日新论文分母。表中的原文主张均未由作者实验升级为事实保证。

## 潜在贡献保留

表中 arXiv 链接固定 v1。除另注外，v1提交原字段在2025-12-14 UTC；这不是公告，更不是本窗公开授权。较旧提交仍不能由月目录授本窗；后月ID的实际旧提交也不按编号排除。每项的处置相同：首公开外部终态隔离、Books暂缓，恢复实际公共可用区间后再按具体命题评分和补必要证据。必要准入局部见 [CORE_AND_BOOKS](CORE_AND_BOOKS.md)，没有以缺少全文可信度为由缩池。

| 精确材料 | 原有判断 → 原文潜在增量 → 需要重新考虑的选择/边界 |
| --- | --- |
| [2602.22219 KG retrieval](https://arxiv.org/abs/2602.22219v1) | 平面检索选择 → STaRK eCommerce结构检索/重排局部比较 → 检索器组合需绑定知识结构和评价，不采production-ready表述。 |
| [2601.08835 DeliberationBench](https://arxiv.org/abs/2601.08835v1) | 多模型协商自动更可靠 → 三协议与单次强judge选择五候选的负侧 → 分开候选生成、选择器能力和成本；v1提交14日10:29:55UTC。 |
| [2512.22145 Pre-review](https://arxiv.org/abs/2512.22145v1) | 自动预审评分代表人工质量 → 弱相关/高置信过估局部证据 → reviewer替代需独立效度，不将出版评分当真值。 |
| [2512.15782 GuardrailAutoTune](https://arxiv.org/abs/2512.15782v1) | 固定护栏配置 → grid/Optuna配置搜索 → 核恶意输入和良性输入下输出被分类器判有害的比例及延迟；该指标不是良性拒绝率。同分类器兼filter/judge，grid全50、Optuna初10再top5全50不授等预算8倍加速或通用安全。 |
| [2512.14753 CODEACROSTIC](https://arxiv.org/abs/2512.14753v1) | 代码水印可长期追踪 → comment-removal失效及CueList熵选择 → 变换攻击面与水印可检测性分开。 |
| [2512.14751 OneLeak](https://arxiv.org/abs/2512.14751v1) | 微调后黑盒模型隔绝原模型攻击 → 白盒预训练到黑盒微调攻击迁移 → 权限变化不自动移除攻击知识。 |
| [2512.13741 LaminarFlow](https://arxiv.org/abs/2512.13741v1) | 层激活稳定性直接指示安全 → Qwen/Gemma攻击变化反向 → 诊断绑定模型，不称无内部访问的黑盒安全。 |
| [2512.13733 LLRC](https://arxiv.org/abs/2512.13733v1) | 固定/离散rank heuristic → 冻结原权重训练singular-value mask → calibration选择与后微调、压缩artifact及执行分开；14日07:20:57UTC。 |
| [2512.13731 CMER](https://arxiv.org/abs/2512.13731v1) | LaTeX线性输出足以复杂表达式识别 → 结构化数学语言/layout tokenizer与难度数据 → 表示和监督匹配，不是科学发现应用。 |
| [2512.12885 SignRAG](https://arxiv.org/abs/2512.12885v1) | 通用VLM能直接识别长尾标志 → 抽象描述索引/候选匹配及实测尾延迟 → 保留离线分支，不能授实时车载。 |
| [2512.12880 Recursive MoL](https://arxiv.org/abs/2512.12880v1) | 层共享FFN损失表达力 → token条件LoRA experts恢复层差异 → 共享、merge和质量/成本需同验。 |
| [2512.12858 Information Consistency GRPO](https://arxiv.org/abs/2512.12858v1) | 等意图提示同质量 → 语义等价分组、熵/稳定性reward及reset → 稳定性不是所有输出强制相同。 |
| [2512.12842 SAGA](https://arxiv.org/abs/2512.12842v1) | 语言意图直接到动作 → 3D affordance热图接whole-body policy → 感知条件与控制安全不混为一体。 |
| [2512.12824 CoCa few-shot](https://arxiv.org/abs/2512.12824v1) | 增强总有利线性probe → augmentation divergence下probe/LoRA取舍 → 训练目标和适配能力要匹配。 |
| [2512.12822 Lemon](https://arxiv.org/abs/2512.12822v1) | 分离3D/语言encoder → patch与语言单序列early fusion/渐进curriculum → 融合位置与训练代价分开核。 |
| [2512.12816 Concept-drift Allocation](https://arxiv.org/abs/2512.12816v1) | retraining启发式可直接部署 → DMRL/IMRL与通信部署条件优化 → 理论假设和实际漂移分别验。 |
| [2512.12812 Tone](https://arxiv.org/abs/2512.12812v1) | polite/rude提示普遍有益 → 模型/任务切片效应与聚合差异 → 不用全局平均选择固定语气策略。 |
| [2512.12806 Sandboxing](https://arxiv.org/abs/2512.12806v1) | 失败命令等Agent安全失败 → interception、本地文件快照与失败回滚 → exit0与semantic postcondition、不可逆外部effect分开；14日19:03:59UTC。 |
| [2512.12801 PIE-P](https://arxiv.org/abs/2512.12801v1) | 单GPU功耗可外推并行能耗 → 多GPU细粒度量测与通信非确定性 → TP/PP/DP按配置分账。 |
| [2512.12799 DrivePI](https://arxiv.org/abs/2512.12799v1) | 感知与规划分别建模 → 统一4D感知/flow/planning VLA → 多目标互补不授真实道路安全。 |
| [2512.12794 Rule prompting CPS](https://arxiv.org/abs/2512.12794v1) | 数字/规则混在prompt → 数值规范化与领域规则分块对照 → instruction adherence不等形式规则验证。 |
| [2512.12793 VLG-Loc](https://arxiv.org/abs/2512.12793v1) | 建图必须全几何先验 → 语义landmark/VLM observation/Monte Carlo pose融合 → 概率定位仍需传感观测与假设。 |
| [2512.12791 CloudOps assessment](https://arxiv.org/abs/2512.12791v1) | binary completion足以评价Agent → model/memory/tool/environment分层运行不确定性 → 隐藏运行失效要另测。 |
| [2512.12777 SoT](https://arxiv.org/abs/2512.12777v1) | 可读CoT即完整计算说明 → 纯函数迭代state的计算非唯一性和编码反例 → 状态参与计算不授忠实解释；必要§3–5已读。 |
| [2512.12775 Persistent Personas](https://arxiv.org/abs/2512.12775v1) | persona指令持久稳定 → >100turns persona/IF/safety权衡 → 长对话三目标分开测。 |
| [2512.12772 JointAVBench](https://arxiv.org/abs/2512.12772v1) | 单模态QA代理联合理解 → 必须依赖音视频的任务切片 → synthetic QA/judge不是真值自动认证。 |
| [2512.12770 CurióEdu](https://arxiv.org/abs/2512.12770v1) | corpus越大训练越好 → 同7B局部质量过滤10B与100B比较 → 数据质量/规模和预算分开。 |
| [2512.12769 ASTA](https://arxiv.org/abs/2512.12769v1) | 路由准确即任务成功 → edge/cloud routing与repair对照 → 可执行率、ASR、repair效果分开。 |
| [2512.12768 CoRe3D](https://arxiv.org/abs/2512.12768v1) | 语言高层推理直接接3D动作 → localized 3D latent空间reasoning → 表示一致不证明物理动态正确。 |
| [2512.12756 FysicsWorld](https://arxiv.org/abs/2512.12756v1) | 模态独立训练 → any-to-any输入/输出和CMCS依赖筛选 → 关注融合机制，不以数据量授贡献。 |
| [2512.12751 GenieDrive](https://arxiv.org/abs/2512.12751v1) | 视觉生成即world model → occupancy triplane/action MCA/NMV attention → 生成指标不保证物理状态。 |
| [2512.12744 Spontaneity](https://arxiv.org/abs/2512.12744v1) | 输入稀疏化只降低算力 → pruning配trainable spontaneous neurons → 补偿表达力必须绑计算预算。 |
| [2512.12730 NL2Repo](https://arxiv.org/abs/2512.12730v1) | scaffold代码任务代理全库生成 → empty workspace到可安装library的长程验证 → test pass与整体完成分开。 |
| [2512.12716 CoDA](https://arxiv.org/abs/2512.12716v1) | planner/executor共享所有历史 → 同模型角色context隔离与PECO轨迹优化 → 角色组织与context膨胀分开。 |
| [2512.12710 Quantum LM](https://arxiv.org/abs/2512.12710v1) | 量子语言表示只是物理应用 → IBM硬件SPSA语言模型训练/读出 → 深度与可训练性边界，不外推LLM规模。 |
| [2512.12706 SMART](https://arxiv.org/abs/2512.12706v1) | 结构coverage表示测试完成 → AST diff意图与混合reward引导RL → coverage与语义任务验收分开。 |
| [2512.12701 ATP](https://arxiv.org/abs/2512.12701v1) | fixed ViT token数 → CLS/CLIP混合token pruning → 无backbone改动仍有质量门槛。 |
| [2512.12694 Historical RAG](https://arxiv.org/abs/2512.12694v1) | 语法连贯可代理档案检索 → OCR/语言漂移下expansion/RRF/abstention消融 → retrieval质量和生成连贯分开。 |
| [2512.12690 SFT versus RL VLM](https://arxiv.org/abs/2512.12690v1) | SFT/RL有统一赢家 → 同源数据规模/容量/分布的反向效果 → objective选择绑定数据条件。 |
| [2512.12688 Prompt theory](https://arxiv.org/abs/2512.12688v1) | 固定参数不容表达新函数 → 构造backbone/prompt interpreter的函数类结果 → 存在性不授预训练模型通用能力。 |
| [2512.12686 Memoria](https://arxiv.org/abs/2512.12686v1) | 全历史/向量库统一选择 → KG triplet时效权重与相同embedding对照 → recency排序和真值/延迟分账。 |
| [2512.12683 Q-NeRF](https://arxiv.org/abs/2512.12683v1) | INR高频spectral bias → QIREN替代density/radiance模块的三种hybrid配置 → quantum simulator/few-qubit限制，不以Quantum分类排除模型表示。 |
| [2512.12678 βCLIP](https://arxiv.org/abs/2512.12678v1) | caption单粒度contrastive表示 → 多粒度pool与严格/宽松βCAL → 正负上下文粒度和目标匹配。 |
| [2512.12677 Classification](https://arxiv.org/abs/2512.12677v1) | 分类总要生成instruction → 4bit LoRA模型final embedding head对照 → 判别与生成负担按任务选择。 |
| [2512.12656 AAMCBR](https://arxiv.org/abs/2512.12656v1) | LLM单独作案例推理 → 提取非factorized因素交symbolic argument → richer case条件才显示收益。 |
| [2512.12633 DiG](https://arxiv.org/abs/2512.12633v1) | sparse spatial grounding监督不足 → 成对render差异proxy/curriculum → proxy是否保留目标差异须验。 |
| [2512.12623 DMLR](https://arxiv.org/abs/2512.12623v1) | 一次视觉输入足以reasoning → latent confidence policy/动态patch注入 → 选择质量和额外计算分开。 |
| [2512.12622 D3D-VLP](https://arxiv.org/abs/2512.12622v1) | fragmented 3D监督 → 多组件CoT/Masked-AR联合损失 → loss互补不等泛化保证。 |
| [2512.12620 Syllogism](https://arxiv.org/abs/2512.12620v1) | symbolic答对代表natural-language逻辑 → 14model模态/表达失配 → 格式能力与语义推理分开。 |
| [2512.12608 ObviousRecord](https://arxiv.org/abs/2512.12608v1) | 随机经验检索 → 因果/结果符号记忆与最大语义差异选择 → 60对局部覆盖不授continual learning通则。 |
| [2512.12602 EFLA](https://arxiv.org/abs/2512.12602v1) | delta动态近似更新 → continuous rank-one更新精确解和并行化 → dynamics精确不授浮点/softmax等价。 |
| [2512.12598 Scene](https://arxiv.org/abs/2512.12598v1) | entity consistency代理scene保持 → geometry-grounded pairs/cross-view loss → 几何与主体提示取舍分开。 |
| [2512.12576 CoVRL](https://arxiv.org/abs/2512.12576v1) | 无verifier无法RL → answer prior/posterior reward与hybrid采样 → trace和答案选择仍需独立预算/效度。 |
| [2512.12560 Streaming Assistant](https://arxiv.org/abs/2512.12560v1) | 时序pruning够处理视频冗余 → MSSAVT互不相邻spatial similarity mask → 双向冗余依赖与质量成本。 |
| [2512.13734 Federated embeddings](https://arxiv.org/abs/2512.13734v1) | item embedding更新通信重 → LoRA/hash/RQVAE PEFT路径 → 更小更新不授联邦隐私证明。 |
| [2512.12895 Loops](https://arxiv.org/abs/2512.12895v1) | loop只是采样异常 → 风险规避cycle和时间相关误差两种机制 → 升温是stopgap非训练修复；提交15日00:44:54UTC。 |
| [2512.12889 Discrete diffusion distillation](https://arxiv.org/abs/2512.12889v1) | distillation依赖proxy/aux model → CTMC marginal density-ratio条件分布matching → teacher/student目标和近似分开；15日00:16:10UTC。 |
| [2512.12818 Hindsight](https://arxiv.org/abs/2512.12818v1) | memory混合经历与信念 → facts/experience/entity summary/belief四网与retain/recall/reflect → inference与原始证据分责。 |
| [2512.12762 FLFA](https://arxiv.org/abs/2512.12762v1) | non-IID local backward增通信 → global weight feedback alignment → 收敛假设和通信代价另核。 |
| [2512.12742 VI-NF RJMCMC](https://arxiv.org/abs/2512.12742v1) | proposal需昂贵target-MCMC pilot → reverse-KL RealNVP直接学习proposal → 学习目标/模型比较假设，不引科学应用。 |
| [2512.15778 RAMBO](https://arxiv.org/abs/2512.15778v1) | 局部bit fault可容忍 → Mamba所测关键bit灾难失效 → 当前官方v1原页/HTML题名与摘要均RAMBO；保留初始抓取COBRA异名异常，不授历史v1已是COBRA。具权重与bit扰动权限，不等自然故障或生产RowHammer复现。 |
| [2512.12898 Qonvolution](https://arxiv.org/abs/2512.12898v1) | NN低频bias影响signal建模 → query convolution跨1D/2D/NVS路径 → 表示机制不是只按rendering指标；15日00:46:09UTC。 |
| [2512.12870 Noisy-label AL](https://arxiv.org/abs/2512.12870v1) | uncertainty采样自动最有价值 → labeler minmax分配与noise对照 → 采样与标注可靠性联合考虑。 |
| [2512.12785 OLC-WA](https://arxiv.org/abs/2512.12785v1) | 固定online分类更新 → EMA drift/adaptive weighted learning → 漂移检测与优化独立，非普遍免调参。 |
| [2512.12779 OLR-WAA](https://arxiv.org/abs/2512.12779v1) | online regression固定step → EMA/conservative confidence动态加权 → 局部noise/drift条件验收。 |
| [2512.12740 FuXiγ](https://arxiv.org/abs/2512.12740v1) | 推荐模型只领域改指标 → encoder连续矩阵access/decoder时间指数与diagonal sparse Toeplitz attention → 实际架构和执行取舍。 |
| [2512.12703 Motion parts](https://arxiv.org/abs/2512.12703v1) | 遮挡part一视同仁建模 → credible visible part/part VAE/Masked AR → 忽略不可见数据的噪声/覆盖取舍。 |
| [2512.12667 CAL deepfake](https://arxiv.org/abs/2512.12667v1) | known/unknown共用confidence学习 → 非对称学习/pseudolabel/prototype pruning → 无未知类数量先验分支。 |
| [2512.12574 RLGP](https://arxiv.org/abs/2512.12574v1) | 固定kernel选择 → neural selection与mean-shift鲁棒优化 → noise/outlier假设不外推所有学习。 |
| [2512.12856 FiFA memory](https://arxiv.org/abs/2512.12856v1) | memory删除率代表效用 → 六策略/预算对照 utility/privacy/cost → 综合分数不是隐私证明。 |
| [2512.12692 WebOperator](https://arxiv.org/abs/2512.12692v1) | search backtracking可随意撤销 → 非可逆感知best-first/feasibility与等价过滤 → 外部真实state不能从prompt undo。 |
| [2512.12597 AgentSHAP](https://arxiv.org/abs/2512.12597v1) | tool调用即实际贡献 → tool子集MC Shapley attribution → replay/stochasticity条件，非完整因果证明。 |
| [2512.12325 Online regret](https://arxiv.org/abs/2512.12325v1) | adversarial/stochastic学习分析分离 → Ville event/variance与path条件regret bridge → 仅声明优化理论假设，非NN策略；13日提交。 |
| [2512.12341 Uncertainty](https://arxiv.org/abs/2512.12341v1) | MI通用不确定性指标 → proper scoring rule按任务loss构造 → selective/OOD/AL指标用途分开；13日。 |
| [2512.12301 TwinFormer](https://arxiv.org/abs/2512.12301v1) | long-sequence Transformer开销 → local/global top-k与GRU层级聚合及消融 → 稀疏机制/复杂度，不仅领域预测排名；13日11:50:18UTC。 |
| [2512.12405 BOLERO](https://arxiv.org/abs/2512.12405v1) | frozen tabular transformer不能利用图先验 → bipartite GNN row refinement → 成对统计和pool依赖rank分开；13日。 |
| [2512.12428 EqProp](https://arxiv.org/abs/2512.12428v1) | 标准更新适配memristor → 非线性更新与电阻/收敛取舍 → 六模型两任务硬件条件；13日。 |
| [2512.12448 KAN](https://arxiv.org/abs/2512.12448v1) | 手选KAN结构 → overprovision/可微arch search/sparsify → 表达力和可解释性预算；13日。 |
| [2512.12445 Knowledge-guided MAE](https://arxiv.org/abs/2512.12445v1) | 重构只数值loss → LSMM/SAM物理几何约束配Huber的自监督目标 → 约束与表示目标匹配，潜在模型训练分支，不采领域科学效益；13日19:59:04UTC。 |
| [2512.12465 TM](https://arxiv.org/abs/2512.12465v1) | 通用图像生成backbone单一选择 → transition head/time weighting/sampler frequency比较 → 质量与采样成本条件；13日。 |
| [2512.12469 Sparse anchoring](https://arxiv.org/abs/2512.12469v1) | 稀有concept无法控制 → 极少label/geometry regularizer anchoring及消融 → steer与监督分布条件；13日。 |
| [2512.12523 SVD Contrastive](https://arxiv.org/abs/2512.12523v1) | contrastive网络无表示约束 → semiorthogonal SVD结构/抗噪 → 训练参数与objective同验。 |
| [2512.12544 HyperEdit](https://arxiv.org/abs/2512.12544v1) | 全参编辑破坏未改区域 → request hypernetwork/span regularizer → 局部改变与保持义务分开。 |
| [2512.12641 Unigram](https://arxiv.org/abs/2512.12641v1) | tokenizer loss代理压缩 → 更高训练loss但更好compression的反证 → tokenizer目标与实际编码代价分开。 |
| [2512.12839 LongStoryEval](https://arxiv.org/abs/2512.12839v1) | 长文整体judge统一可靠 → aspect/detail aggregation与summary效率对照 → 人类对齐和成本，非judge真值。 |
| [2512.12549 SCFA](https://arxiv.org/abs/2512.12549v1) | 视频逐帧表示丢上下文 → frame grid与contrastive view学习 → 融合/监督条件，不只动作识别指标。 |
| [2512.12571 Measurement plasticity](https://arxiv.org/abs/2512.12571v1) | test-time augmentation纯数字零采集成本 → ISO/shutter/aperture物理候选及forward-only top-k/vote → 采集预算与适配质量共同算。 |
| [2512.12586 StegaVAR](https://arxiv.org/abs/2512.12586v1) | cover特征与秘密传输竞争 → secret-guided STeP/CroDA → 表示保持与隐写不可检测性分开。 |
| [2512.12604 X-Slim](https://arxiv.org/abs/2512.12604v1) | cache复用统一阈值 → dual warning/critical与timestep/block/token refresh → 多粒度状态质量/成本。 |
| [2512.12610 Patchify](https://arxiv.org/abs/2512.12610v1) | 全局retrieval代理localization → patch/LocScore局部盲区和PQ压缩 → 召回位置与语义答案分开。 |
| [2512.12658 CogDoc](https://arxiv.org/abs/2512.12658v1) | SFT总是RL合理起点 → low-res locate/high-res reasoning、直接RL与初始化冲突 → 不和12690合并为统一RL优劣。 |
| [2512.12664 InteracTalker](https://arxiv.org/abs/2512.12664v1) | 单condition talking head → 独立motion modules/动态condition fusion → 异构信号与组合成本。 |
| [2512.12673 PCSR](https://arxiv.org/abs/2512.12673v1) | fixed QKV分布难适配 → per-layer conditional scale/shift FactorGen → domain separation不授任意域保证。 |
| [2512.12675 Scone](https://arxiv.org/abs/2512.12675v1) | subject保持等composition保持 → understanding桥/semantic mask及对应benchmark → 分开实体、关系与生成。 |
| [2512.12847 HaShiFlex](https://arxiv.org/abs/2512.12847v1) | 全可编程GPU成本 → 大部分Po2硬连线、可编程末层 → 只有限finetune；7nm ASIC flow非实芯/全网络灵活性。 |
| [2512.12850 KANELÉ](https://arxiv.org/abs/2512.12850v1) | KAN spline边执行贵 → 固定domain LUT映射与训练/量化/剪枝协同 → 不移植2700倍headline到所有硬件。 |
| [2512.08089 NysX](https://arxiv.org/abs/2512.08089v1) | HDC projection/channel数据流贵 → Nyström DPP/stream projection/MPH/SpMV → workload与表示质量同验；8日22:47:39UTC。 |
| [2512.07312 DCO](https://arxiv.org/abs/2512.07312v1) | LLM固定cache/SPM选择 → dataflow-aware dead-block/bypass/thrashing控制 → simulation/RTL与production分开；8日08:56:10UTC。 |
| [2512.09304 RACAM](https://arxiv.org/abs/2512.09304v1) | DRAM-PIM搬运重复数据 → broadcast/data-reuse buffers映射 → 不跨平台移植GPU比较；10日04:07:14UTC。 |
| [2512.09427 ODMA](https://arxiv.org/abs/2512.09427v1) | HBM分页适配所有memory → LPDDR random access劣势下length bucket/safeguard → paging和memory介质条件分开；10日08:52:20UTC。 |
| [2512.11550 PD-Swap](https://arxiv.org/abs/2512.11550v1) | FPGA一套attention实现 → DPR切prefill/decode、static weights/TMM → hidden reconfiguration计入成本；12日13:35:09UTC。 |
| [2512.11826 FSL-HDnn](https://arxiv.org/abs/2512.11826v1) | few-shot训练依赖昂贵反向 → weight clustering/HDC single-pass/early exit实芯 → 40nm、10way5shot局部量测；2日02:36:19UTC。 |
| [2512.13704 Adjudicator](https://arxiv.org/abs/2512.13704v1) | council自主纠错 → dynamic KG及override、无KG/无council对照 → 数据结构错误类别与投票贡献分开；5日06:13UTC。 |
| [2512.13713 LoopBench](https://arxiv.org/abs/2512.13713v1) | 单Agent能力能外推协调 → odd-cycle/deadlock与策略传递memory → 非通信条件中的协作失效；7日22:26:40UTC。 |
| [2512.13716 ValuePilot](https://arxiv.org/abs/2512.13716v1) | 值对齐只靠通用指令 → value场景标注与decision模块学习 → 个性化action value不是所有人类价值真值；9日12:15:46UTC。 |
| [2512.13725 Causal quantization](https://arxiv.org/abs/2512.13725v1) | 总体量化accuracy代表各推理层 → causal rung切片与benchmark结构敏感性/GT graph augmentation → 压缩漂移分层测；13日17:54:15UTC。 |
| [Seed Paper1323 / Seedance 1.5 pro](https://arxiv.org/abs/2512.13507v1) | 音/视频分离生成 → 双分支DiT/joint module、数据与post-training → joint质量和复杂度需同验；Paper日编码不能授公开；arxiv提交晚于窗，Blog1817是不同事件。 |
| [2512.12106 DreamRAM](https://arxiv.org/abs/2512.12106v1) | 撤销“ML仅背景”关闭：NN映射、DLOMAT/3D-HBM数据移动与iso-capacity/bandwidth/power设计空间有模型执行取舍；复用Popper/Mill实际III-B/C、IV-A/B/C必要原源，不授实机LLM性能、能耗或安全。 |
| [2512.22146 EEG voice](https://arxiv.org/abs/2512.22146v1) | 撤销医学题名止步：EEG-to-mel学习、L1/CTC与spoken-to-imagined初始化有跨模态表示/生成机制；复用Popper实际v1 PDF6–10页。trial/CPU时间匹配与MCD的DTW仍存在，不授对齐消失、临床或跨被试保证。 |
| [2512.12887 AnyMC3D](https://arxiv.org/abs/2512.12887v1) | 撤销医学图像题名止步：冻结2D backbone时in-plane适配/through-plane聚合分责，各向异性/coverage下序列先验与permutation-invariant query pooling取舍；data regime改变FM评价，不采用临床指标或普遍3D优势。Popper实际v1 §1/P1–P3、§3.1–3.3、Appendix D局部。 |
| [2512.12932 数据选择机制](https://arxiv.org/abs/2512.12932v1) | 撤销生物FM题名止步：subset局部ERM/flatness条件、diagonal empirical Fisher近似后的influence/coverage数据选择，限TRAIN-DATA机制；不引入BioFM科学应用、不授严格曲率等价。Popper实际v1 §3.2–3.3/适配消融；Submitted Dec15T02:42:52Z晚于右端只排本v1正文，不证更早first-public。 |

## 完整题摘或必要核心后的明确关闭

不为这些贡献前排除项另求精确公开日；日期未核实不影响本次不采用，不把它们称评分低或Evidence完成。

| 材料 | 实际判断与关闭理由 |
| --- | --- |
| [2601.04213 AnimatedLLM](https://arxiv.org/abs/2601.04213v1) | 浏览器预计算Transformer trace教学可视化；无新增学习、模型执行或评价边界。 |
| [2512.12869 ERA-IT](https://arxiv.org/abs/2512.12869v1) | 专利renewal代理价值分级、既有fine-tuning和rationale；领域指标非新增学习机制/受控推理效度。 |
| [2512.12833 FST CPS](https://arxiv.org/abs/2512.12833v1) | 传统控制/spectral FST监督合成；没有模型训练/LLM执行增量，不凭CPS名称入选。 |
| [2512.12802 LLM Consciousness](https://arxiv.org/abs/2512.12802v1) | 哲学Proximity Argument不是实际continual learning或执行/评价机制。 |
| [2512.12643 LexRel](https://arxiv.org/abs/2512.12643v1) | 法律关系taxonomy/schema/领域benchmark；没有可改变主线选择的受控失效边界。 |
| [2512.12630 ORIBA](https://arxiv.org/abs/2512.12630v1) | 艺术roleplay co-creation与14人研究；无新增模型训练/执行或评价盲区。 |
| [2512.12596 Ad layout](https://arxiv.org/abs/2512.12596v1) | VLM placement plan接HTML renderer的广告应用；质量指标不足以证明新增主线机制。 |
| [2512.12595 Vision-enhanced LLM](https://arxiv.org/abs/2512.12595v1) | 必要PDF §3/§5–6实际读：共享token、双向attention、rectified flow和noise-aware remeasurement仍为成熟模块描述，未给出可区分的新训练/重测算法或有效条件；数字/消融不单独构成机制贡献，不因缺实验预算而降分。 |
| [2512.12592 Student assessment](https://arxiv.org/abs/2512.12592v1) | rubric评分/追问评估学生理解与九位教师；不是模型系统可靠性评价或新执行机制。 |
| [2512.12624 CoLSE](https://arxiv.org/abs/2512.12624v1) | copula interval CE与NN residual用于SQL cardinality；没有明确模型训练/推理平台机制链，不以数据库系统名扩项目范围。 |
| [2512.12834 PMG overview](https://arxiv.org/abs/2512.12834v1) | 游戏生成taxonomy/挑战归纳；无实际新模型机制/受控反证。 |
| [2512.12252 OptLCMS](https://arxiv.org/abs/2512.12252v1) | count sketch/DP数据结构与分析阈值，ML predictor只是辅助，未建立基础模型或训练执行增量。 |
| [2512.12537 Naga NLP](https://arxiv.org/abs/2512.12537v1) | 低资源语言人工校验合成数据与既有fine-tuning；无受控合成数据成立条件或新增学习机制。 |
| [2512.12613 StruProKGR](https://arxiv.org/abs/2512.12613v1) | 传统KG路径/概率聚合missing facts，无LLM retrieval或新模型学习机制。 |
| [2512.10180 Neuromorphic FPGA](https://arxiv.org/abs/2512.10180v1) | LIF参数/连通性、UART运行时配置与既有FPGA分类平台；摘要未给出区别成熟可配置实现的执行机制或可改变设计的受控边界，未称实芯/开源已落实。 |
| [2512.13714 Annotation pipeline](https://arxiv.org/abs/2512.13714v1) | 必要PDF §3.1–3.5/§4.3–4.4/§5.1实际读：weak supervision、confidence/vote、人审与SFT/RL循环仍为成熟步骤；SI/FC/AP/RDR只概念性定义与表格，未定义新校准/路由协议或可区分评价盲区，不能靠“stability”重命名授准入。 |
| [Google automated STOC feedback](https://www.research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/) | 全核心已读：Deep Think inference scaling与summary/error/typo反馈、人审过滤及opt-in问卷；没有新具体模型机制或受控可靠性边界。原文Dec15日标签，May18,2026改名更新不冒充2025版本；不因AI辅助学术审稿机构名授贡献。 |
| [Kimi CLI0.64](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md) | Dec15日标签下会话选择恢复/全局MCP配置管理；既有接口管理未披露新恢复一致性、state migration或授权隔离语义，贡献前关闭，不凭bugfix标签关闭、不授精确release时刻。必要core复用Popper在16日实际原源校准，同版本/命题不新增扫描。 |
| [2512.12795 TRACER](https://arxiv.org/abs/2512.12795v1) | Popper实际完整摘要、§1与方法引导：个体临床transition混合分布EM与既有Trans-Lasso适配，未建立foundation形成或系统新关系。按实际范围关闭，不是医学标题关闭；原abs cache miss后HTML成功，不记正文受阻。 |
| [2601.09709 ICD9](https://arxiv.org/abs/2601.09709v1) | 完整v1摘要为既有reasoning模型MIMIC多标签/漏编码统计，没有新增主线机制，具体范围关闭；Submitted Dec14T17:15:17Z不证first-public，不由编号推January归属。 |

## 只读标题的范围止步

原题名止步中22146、12887、12932的误关已撤销并移潜力；12795与2601.09709实际完整题摘/必要引导后具体关闭，均见上表，不再称仅标题判断。当前只标题条目为13746复合材料、12888 metasurface、12614 soft material、12558 reaction-diffusion、L2 rollup12732、Raft lease15659、astro CAMP13591、serverless16066、版图13133，未冒称其摘要/全文已读或全库存关闭。

本轮root接八项作者同步，复用[Popper实际独立原源](ROOT_ADMISSION_REVIEW.md)的精确身份/位置与窄命题，不声称root新读完整论文。潜力107→109→111；原关闭18撤销DreamRAM后17，补已触发Kimi0.64核心与12795/09709完整题摘判断后20。原标题14项中5项现已有实际题摘/必要判断，剩9title-only；不新增论文发现。误关原理由与Guardrail/RAMBO旧字段异常保留独立记录，不用于当前判断。八项作者差额已同步，待非作者最终回核，不扩大库存。

原含糊12683/12301/12445/10180已另读题摘并分别作上表判断，不继续把Quantum/forecasting/硬件题名机械排除。12690与12658保留两种不同RL/SFT条件，负面loop/量化/协商结果未删除。

## 已实际核个体提交晚于右端的恢复线索

本窗右端为2025-12-15T01:00:00Z。以下**逐个v1版本历史**实际取得晚于右端的提交下界；只排除这些arxiv v1正文事件作为本窗候选，不推断早期项目/作者稿事件，不授它们未来哪一天first-public。不读全部窗外正文、不扩大任务。

- Dec15UTC：13749 04:52:30、13747 03:09:31、12980 04:49:33、12978 04:46:48、12957 03:44:20、12950 03:29:21、12938 02:54:10、12928 02:24:50、12924 02:20:42、12922 02:12:53、12921 02:12:12、12914 01:59:14、17946 03:27:35、12977 04:45:47、12967 04:11:11、12949 03:27:49、12925 02:24:06、12906 01:18:38、14754 02:57:55、12964 04:02:53、12936 02:51:47、12929 02:25:46、12905 01:12:11。
- Dec15UTC补检：13096 08:54:43、13268 12:28:08、13488 16:24:32、13525 16:53:49、13638 18:33:04、13102 08:59:19、13131 09:43:08、13142 09:50:00、13154 10:02:50、13159 10:08:53、13168 10:28:45、13240 11:55:55、13323 13:39:14、13374 14:28:35、13399 14:50:08、13481 16:17:12、13762 14:00:15、13764 14:36:29、13771 18:09:54、12976 04:45:09、13059 07:37:53、13063 07:50:09、13109 09:04:06、12990 05:33:07、13282 12:43:04、13479 16:16:44、13686 18:59:53、13507 16:36:52。
- Dec16UTC：14290 11:01:48、14628 17:43:53、14151 07:16:10、14256 10:06:47、14322 11:38:36、14661 18:21:18；Dec17UTC15028 02:38:06、15306 10:51:45、15705 18:55:45；Dec18UTC16056 00:45:00。

短ID均前缀2512，可复查 `https://arxiv.org/abs/2512.<ID>v1`。提交不授公开；13507的Seed Paper早期事件仍独立保留，不由该下界关闭整个家族。
