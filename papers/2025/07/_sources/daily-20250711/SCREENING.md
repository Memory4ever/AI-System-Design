# 有界发现与贡献筛选停点

范围：2025-07-11 Daily；不是历史公开时间验收表。全部链接指向抓取时返回的版本，除正文另明示的两篇 v1 外，**当前题摘不等于历史 v1**。完整原件分别保留于 `narrow-discovery.json`、`discovery.json` 及对应 Atom `.raw`。不得以 `published`（submitted）分配当日。

## 查询与实际停止位置

初始四组 `all:` 词查询限定 submission `2025-07-09T18:00Z～2025-07-10T18:00Z`，返回 model=191、systems=26、agents=49、multimodal=41，跨组按 arXiv family 去重后 216。`all:Transformer` 包含参考文献/词形噪声，首条 Green-Schwarz transformation 属物理，不是 191 项有效贡献，也不扩为逐篇完整摘要队列。宽列表仅作题名查漏；明确无关 physics/AI for Science/领域应用可按题名关闭。

校准 `narrow.py` 采用分类 + `ti/abs` 主题词；model=114、systems=2、agents=33、multimodal=55，跨组去重 156。每组 start=0/max_results=200，total<200，读取完整返回页后停止。全部窄入口题名已处置：相关或含糊题名读完整题摘；明确领域题名按具体范围关闭。分类和词查询不能保证覆盖全部相关论文，submission surrogate 更不能证明窗口公告或重要修订完整性。

下表为窄入口156个唯一家族、宽入口已有主线线索17项及末节剩余题名50项，合并223项处置；贡献准入校准后65项保留具体机制/反证线索（SAGE另有方法定义争议），158项关闭。保留不是通过Evidence Gate，不赋分、不用于当窗正式候选或Books。题摘筛选与正文审阅分别计数；KVFlow/Synergy已读局部核心v1 HTML，SAGE按root校准定点读v1 §3.3/表3，仍没有当窗日期/证据审阅完成家族。root发现模块/任务映射式误收后，同类33项已逐项关闭，不按数量或比例筛选。

## 共性准入纠错

“保留”依据为表内明确的设计差额或有效性反证，均待历史事件/版本证据；不是“每个新模块都值得评分”。不确定的pipeline/任务组合在完整题摘复查后具体关闭。SAGE的core定点澄清见日报 §4/§5，其中心熵定义不一致，不能作为采用证据。

## 宽入口其余题名查漏关闭与安全线索

没有新增查询。下表补记同一原始宽页剩余50个身份；明确physics/math/科学应用/常规领域应用按题名范围关闭，含糊9项已读完整题摘，只有中间feature泄露的具体安全线索保留。无关题名不进入逐篇摘要/全文队列。

| 原始材料身份 | 贡献处置 | 理由/读取范围 |
| --- | --- | --- |
| [2507.07172: Trivialization of the gravitational Green-Schwarz transformation in the non-relativistic limit of string theory](https://arxiv.org/abs/2507.07172v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07195: Theory of Strongly Correlated Systems: An Introduction to Sachdev-Ye-Kitaev Model](https://arxiv.org/abs/2507.07195v3) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07198: Linear-Response Quantum-Electrodynamical Density Functional Theory Based on Two-Component X2C Hamiltonians](https://arxiv.org/abs/2507.07198v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07227: A novel approach for classifying Monoamine Neurotransmitters by applying Machine Learning on UV plasmonic-engineered Auto Fluorescence Time Decay Series (AFTDS)](https://arxiv.org/abs/2507.07227v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07231: Extending Forrelation: Quantum Algorithms Related to Generalized Fourier-Correlation](https://arxiv.org/abs/2507.07231v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07244: Automated Attack Testflow Extraction from Cyber Threat Report using BERT for Contextual Analysis](https://arxiv.org/abs/2507.07244v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07256: Square Functions and Variational Estimates for Ritt Operators on $L^1$](https://arxiv.org/abs/2507.07256v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07305: Superheating and melting phenomena of a vibrated granular layer of cubic particles](https://arxiv.org/abs/2507.07305v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07331: mmFlux: Crowd Flow Analytics with Commodity mmWave MIMO Radar](https://arxiv.org/abs/2507.07331v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07347: Rubber band filters: optimal padding without edge artifacts](https://arxiv.org/abs/2507.07347v1) | 关闭 | 完整题摘：spectroscopy bandpass Fourier padding，非基础模型/系统机制。 |
| [2507.07361: Not even metastable: Cubic double-diamond in diblock copolymer melts](https://arxiv.org/abs/2507.07361v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07368: The LDP of McKean-Vlasov stochastic differential equations with Hölder continuous conditions and integrable conditions](https://arxiv.org/abs/2507.07368v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07398: On the classical geometry of chaotic Green functions and Wigner functions](https://arxiv.org/abs/2507.07398v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07447: Topological electronic structures of non-collinear magnetic phases in a multi-orbital Hubbard model with spin-orbit interactions](https://arxiv.org/abs/2507.07447v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07448: Toolchain for Faster Iterations in Quantum Software Development](https://arxiv.org/abs/2507.07448v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07454: Mix-Geneformer: Unified Representation Learning for Human and Mouse scRNA-seq Data](https://arxiv.org/abs/2507.07454v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07487: Online Navigation Refinement: Achieving Lane-Level Guidance by Associating Standard-Definition and Online Perception Maps](https://arxiv.org/abs/2507.07487v5) | 关闭 | 完整题摘：SD/OP map association的path-aware+spatial attention用于lane导航，任务特定attention组合及指标，未建立foundation模型或action policy新成立条件。 |
| [2507.07520: Conditions for Large-Sample Majorization of Pairs of Flat States in Terms of $α$-z Relative Entropies](https://arxiv.org/abs/2507.07520v3) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07537: Towards Nonlinear Quantum Thermodynamics](https://arxiv.org/abs/2507.07537v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07569: The Smooth Power of the "Neandertal Method"](https://arxiv.org/abs/2507.07569v1) | 关闭 | 完整题摘：conformal-map Escher图案的GPU并行数学算法，非本项目基础模型执行机制。 |
| [2507.10573: Device-Level Optimization Techniques for Solid-State Drives: A Survey](https://arxiv.org/abs/2507.10573v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07602: Advancing Medical Image Segmentation via Self-supervised Instance-adaptive Prototype Learning](https://arxiv.org/abs/2507.07602v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07618: Strain-tunable type-II to type-III & Gimbal nodal line transition in Imm2-phase of Cu$_2$SnS$_3$: An ab-initio study](https://arxiv.org/abs/2507.07618v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07651: Constraining the origin of the long term periodicity of FRB 20180916B with Polarization Position Angle](https://arxiv.org/abs/2507.07651v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07663: MolCLIP: A Molecular-Auxiliary CLIP Framework for Identifying Drug Mechanism of Action Based on Time-Lapsed Mitochondrial Images](https://arxiv.org/abs/2507.07663v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07717: A preconditioned boundary value method for advection-diffusion equations with half Laplacian via spectrum doubling](https://arxiv.org/abs/2507.07717v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07722: Understanding Dataset Bias in Medical Imaging: A Case Study on Chest X-rays](https://arxiv.org/abs/2507.07722v4) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2508.00848: RestAware: Non-Invasive Sleep Monitoring Using FMCW Radar and AI-Generated Summaries](https://arxiv.org/abs/2508.00848v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07745: On the capabilities of LLMs for classifying and segmenting time series of fruit picking motions into primitive actions](https://arxiv.org/abs/2507.07745v1) | 关闭 | 完整题摘：fruit-picking动作分类分段与三种fine-tuning比较，为Learning-by-Demonstration任务可行性，无新表征/控制或泛化成立机制。 |
| [2507.07747: X-RAFT: Cross-Modal Non-Rigid Registration of Blue and White Light Neurosurgical Hyperspectral Images](https://arxiv.org/abs/2507.07747v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.08055: MCPmed: A Call for MCP-Enabled Bioinformatics Web Services for LLM-Driven Discovery](https://arxiv.org/abs/2507.08055v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07809: DT4PCP: A Digital Twin Framework for Personalized Care Planning Applied to Type 2 Diabetes Management](https://arxiv.org/abs/2507.07809v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07811: Patient-specific vs Multi-Patient Vision Transformer for Markerless Tumor Motion Forecasting](https://arxiv.org/abs/2507.07811v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07823: A fast algorithm for the wave equation using time-windowed Fourier projection](https://arxiv.org/abs/2507.07823v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07831: Rethinking Query-based Transformer for Continual Image Segmentation](https://arxiv.org/abs/2507.07831v1) | 关闭 | 完整题摘：CIS query assignment/feature alignment及visual-query replay，证据限任务plasticity；未建立语言/多模态foundation表示或通用训练策略的新成立条件。 |
| [2507.07844: Machine Learning Tools for the IceCube-Gen2 Optical Array](https://arxiv.org/abs/2507.07844v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07861: Mid-IR hyperspectral imaging with undetected photons](https://arxiv.org/abs/2507.07861v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07879: LISTEN: Lightweight Industrial Sound-representable Transformer for Edge Notification](https://arxiv.org/abs/2507.07879v4) | 关闭 | 完整题摘：industrial sound teacher-student KD+冻结backbone/浅head适配/edge系统，既有组合与部署可行性没有新noise robustness或蒸馏条件。 |
| [2507.07904: Testing time order and Leggett-Garg inequalities with noninvasive measurements on public quantum computers](https://arxiv.org/abs/2507.07904v3) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07926: Phase Stability and Transformations in Lead Mixed Halide Perovskites from Machine Learning Force Fields](https://arxiv.org/abs/2507.07926v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07948: Physics-Informed Gaussian Process Inference of Liquid Structure from Scattering Data](https://arxiv.org/abs/2507.07948v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07951: Constructing Optimal Kobon Triangle Arrangements via Table Encoding, SAT Solving, and Heuristic Straightening](https://arxiv.org/abs/2507.07951v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.08066: Kappa Plane Wave Modes and Continuous Squeezing in Quantum Field Theory](https://arxiv.org/abs/2507.08066v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07972: EinHops: Einsum Notation for Expressive Homomorphic Operations on RNS-CKKS Tensors](https://arxiv.org/abs/2507.07972v1) | 关闭 | 完整题摘：通用FHE einsum tensor packing/lowering，无foundation model加密推理或本项目训练/serving执行链的具体新约束；不按tensor术语准入。 |
| [2507.07183: Mass Distribution of Binary Black Hole Mergers from Young and Old Dense Star Clusters](https://arxiv.org/abs/2507.07183v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07228: On a Debiased and Semiparametric Efficient Changes-in-Changes Estimator](https://arxiv.org/abs/2507.07228v2) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07259: Exploiting Edge Features for Transferable Adversarial Attacks in Distributed Machine Learning](https://arxiv.org/abs/2507.07259v1) | 保留潜在贡献；日期隔离 | 中间feature泄露在edge/cloud权重均black-box时仍可重构tensor shape并蒸馏surrogate，明确威胁模型与攻击面改变；仅保留贡献线索，日期隔离 |
| [2507.07291: Estimating Dataset Dimension via Singular Metrics under the Manifold Hypothesis: Application to Inverse Problems](https://arxiv.org/abs/2507.07291v1) | 关闭 | 完整题摘：mixture VAE/pullback metric用于manifold parameterization与biomedical inverse problem；未建立基础模型表示或部署机制的新判断，主证据仍科学逆问题。 |
| [2507.07721: Breast Ultrasound Tumor Generation via Mask Generator and Text-Guided Network:A Clinically Controllable Framework with Downstream Evaluation](https://arxiv.org/abs/2507.07721v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |
| [2507.07739: Phase-Space Synchronization Driven by Moon-Magnetosphere Coupling in Gas Giants](https://arxiv.org/abs/2507.07739v1) | 关闭 | 题名范围关闭：明确physics/math/科学应用或常规领域任务，未有语言/多模态基础模型、Agent控制、训练/推理系统机制线索；宽词匹配不构成贡献。 |

2507.07259 的唯一重开请求：官方首次公告/正文公开时间与 exact version；之后只重开本行威胁模型和feature泄露证据，不扩扫安全主题。当前无法落窗、不计正式候选、不作安全保证。

## 窄入口逐项处置


| 原始材料身份 | 贡献处置 | 理由/读取范围 |
| --- | --- | --- |
| [2507.07186: Planted in Pretraining, Swayed by Finetuning: A Case Study on the Origins of Cognitive Biases in LLMs](https://arxiv.org/abs/2507.07186v2) | 保留潜在贡献；日期隔离 | pretraining 与 fine-tuning 偏差跨任务迁移的区别，可改变数据/对齐设计边界 |
| [2507.07188: Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses](https://arxiv.org/abs/2507.07188v3) | 保留潜在贡献；日期隔离 | 提示顺序与最近性造成选择偏差，潜在评测有效性反证 |
| [2507.07192: Bridging the Last Mile of Prediction: Enhancing Time Series Forecasting with Conditional Guided Flow Matching](https://arxiv.org/abs/2507.07192v3) | 保留潜在贡献；日期隔离 | historical-conditioned source prior 与 two-sided conditional flow path 避免 path crossing，虽以 forecasting 验证，按具体生成机制保留而不因应用域自动排除 |
| [2507.07201: MODA: A Unified 3D Diffusion Framework for Multi-Task Target-Aware Molecular Generation](https://arxiv.org/abs/2507.07201v1) | 关闭 | 完整题摘：分子生成/优化，按本项目暂缓 AI for Science |
| [2507.07202: A Survey on Long-Video Storytelling Generation: Architectures, Consistency, and Cinematic Quality](https://arxiv.org/abs/2507.07202v1) | 关闭 | 完整题摘：长视频 storytelling 综述分类，未指出足以改变主线设计选择的新机制或受控反证 |
| [2507.07203: State-Inference-Based Prompting for Natural Language Trading with Game NPCs](https://arxiv.org/abs/2507.07203v1) | 关闭 | 完整题摘：NPC 交易 prompt/state 应用组合，无新的执行契约或 failure boundary 证据 |
| [2507.07217: Neurosymbolic Feature Extraction for Identifying Forced Labor in Supply Chains](https://arxiv.org/abs/2507.07217v1) | 关闭 | 完整题摘：供应链劳工 news 分类/特征抽取应用，question tree 未提供改变通用 Agent 设计的新条件 |
| [2507.07223: Compute Can't Handle the Truth: Why Communication Tax Prioritizes Memory and Interconnects in Modern AI Infrastructure](https://arxiv.org/abs/2507.07223v2) | 关闭 | 完整题摘复查关闭：报告式 CXL/XLink/分层memory提案，摘要未建立区别于既有 locality/coherence 原则的原创实现或受控评价，不凭术语准入。 |
| [2507.07229: SynthTextEval: Synthetic Text Data Generation and Evaluation for High-Stakes Domains](https://arxiv.org/abs/2507.07229v2) | 关闭 | 完整题摘：合成文本评测工具/维度集合，无具体受控盲点或模型/系统机制增量 |
| [2507.07236: Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification](https://arxiv.org/abs/2507.07236v2) | 关闭 | 完整题摘复查关闭：JS divergence+subset ensemble/calibration组合；摘要未定义新选择规则或校准成立条件，binary任务分数不足。 |
| [2507.07247: Attentions Under the Microscope: A Comparative Study of Resource Utilization for Variants of Self-Attention](https://arxiv.org/abs/2507.07247v2) | 关闭 | 完整题摘复查关闭：资源benchmark及power×time的既有energy核算原则，未呈现改变设计选择的新受控边界。 |
| [2507.07248: MedRiskEval: Medical Risk Evaluation Benchmark of Language Models, On the Importance of User Perspectives in Healthcare Settings](https://arxiv.org/abs/2507.07248v4) | 关闭 | 题名范围：医学应用，暂缓 AI for Science |
| [2507.07251: A Language-Driven Framework for Improving Personalized Recommendations: Merging LLMs with Traditional Algorithms](https://arxiv.org/abs/2507.07251v1) | 关闭 | 题名范围：推荐系统任务应用；本日语言/多模态基础模型主线无明确线索 |
| [2507.07254: Label-Efficient Chest X-ray Diagnosis via Partial CLIP Adaptation](https://arxiv.org/abs/2507.07254v1) | 关闭 | 完整题摘：胸片诊断，partial CLIP few-shot 为医学应用与既有适配，暂缓 AI for Science |
| [2507.07257: Open Source Planning & Control System with Language Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2507.07257v2) | 关闭 | 题名范围：自动科学发现，暂缓 AI for Science |
| [2507.07261: Robust Multimodal Learning Framework For Intake Gesture Detection Using Contactless Radar and Wearable IMU Sensors](https://arxiv.org/abs/2507.07261v1) | 关闭 | 完整题摘：饮食动作健康监测的 radar/IMU fusion，未给出基础模型层可复用的新缺失模态机制 |
| [2507.07262: DisenQ: Disentangling Q-Former for Activity-Biometrics](https://arxiv.org/abs/2507.07262v1) | 关闭 | 完整题摘复查关闭：root扩查：activity-biometric任务的特征解耦/Q-Former，没有foundation表示形成或系统新判断。 |
| [2507.07274: LinguaMark: Do Multimodal Models Speak Fairly? A Benchmark-Based Evaluation](https://arxiv.org/abs/2507.07274v1) | 关闭 | 完整题摘：新 multilingual VQA 数据/榜单，未定位受控 confound 或具体 failure mechanism |
| [2507.07293: Thermodynamic Prediction Enabled by Automatic Dataset Building and Machine Learning](https://arxiv.org/abs/2507.07293v1) | 关闭 | 题名范围：热力学科学研究，暂缓 AI for Science |
| [2507.07297: MagiC: Evaluating Multimodal Cognition Toward Grounded Visual Reasoning](https://arxiv.org/abs/2507.07297v2) | 保留潜在贡献；日期隔离 | answer、reasoning、grounding 分开测量以定位多模态能力来源 |
| [2507.07299: MLFM: Multi-Layered Feature Maps for Richer Language Understanding in Zero-Shot Semantic Navigation](https://arxiv.org/abs/2507.07299v2) | 关闭 | 完整题摘复查关闭：新LangNav任务/属性标签与queryable多层map；未说明区别于已有pretrained feature mapping的表征或memory操作机制。 |
| [2507.07302: Application of LLMs to Multi-Robot Path Planning and Task Allocation](https://arxiv.org/abs/2507.07302v1) | 关闭 | 完整题摘：LLM expert planner 用于任务应用，摘要未识别新的探索/控制机制或有效性条件 |
| [2507.07306: ViDove: A Translation Agent System with Multimodal Context and Memory-Augmented Reasoning](https://arxiv.org/abs/2507.07306v1) | 关闭 | 完整题摘：翻译+multimodal memory pipeline，未给出新 memory update 机制或受控条件 |
| [2507.07307: Multi-Agent Retrieval-Augmented Framework for Evidence-Based Counterspeech Against Health Misinformation](https://arxiv.org/abs/2507.07307v2) | 关闭 | 题名范围：健康错误信息应用，不改变本项目机制主线 |
| [2507.07313: Frontier LLMs Still Struggle with Simple Reasoning Tasks](https://arxiv.org/abs/2507.07313v1) | 保留潜在贡献；日期隔离 | 程序化控制 puzzle 参数与 trivialization，防止推理能力由任务难度混杂 |
| [2507.07317: ADIEE: Automatic Dataset Creation and Scorer for Instruction-Guided Image Editing Evaluation](https://arxiv.org/abs/2507.07317v2) | 关闭 | 完整题摘复查关闭：编辑数据集、score token回归judge和best-edit selection，为既有reward-model管线；相关性提升未隔离新评估机制。 |
| [2507.07328: Bridging the Plausibility-Validity Gap by Fine-Tuning a Reasoning-Enhanced LLM for Chemical Synthesis and Discovery](https://arxiv.org/abs/2507.07328v2) | 关闭 | 题名范围：化学应用，暂缓 AI for Science |
| [2507.07335: Leveraging Manifold Embeddings for Enhanced Graph Transformer Representations and Learning](https://arxiv.org/abs/2507.07335v1) | 关闭 | 完整题摘复查关闭：root扩查：graph-node分类的既有Riemannian projector/MoE组合与3%指标，没有foundation表示形成或系统新判断。 |
| [2507.07340: Entity Re-identification in Visual Storytelling via Contrastive Reinforcement Learning](https://arxiv.org/abs/2507.07340v2) | 关闭 | 完整题摘复查关闭：visual-storytelling grounding的synthetic negatives+DPO双reward组合，未给出超出常规对比负样本/偏好优化的新条件。 |
| [2507.07341: On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment](https://arxiv.org/abs/2507.07341v1) | 保留潜在贡献；日期隔离 | 外部过滤器安全性依赖密码学条件的理论边界 |
| [2507.07359: Goal-Oriented Sequential Bayesian Experimental Design for Causal Learning](https://arxiv.org/abs/2507.07359v1) | 关闭 | 完整题摘：因果实验设计以科学 query 为目标，Transformer 仅作为策略函数；不因包含 Transformer 升为本日主线贡献 |
| [2507.07367: Platform for Representation and Integration of multimodal Molecular Embeddings](https://arxiv.org/abs/2507.07367v1) | 关闭 | 完整题摘：基因/生物分子 embedding 集成，暂缓 AI for Science |
| [2507.07375: Bradley-Terry and Multi-Objective Reward Modeling Are Complementary](https://arxiv.org/abs/2507.07375v1) | 保留潜在贡献；日期隔离 | 共享 embedding 的 Bradley-Terry 多目标 reward/OOD 取舍 |
| [2507.07388: GRIT: Graph Transformer For Internal Ice Layer Thickness Prediction](https://arxiv.org/abs/2507.07388v1) | 关闭 | 完整题摘：雷达冰层厚度科学预测，暂缓 AI for Science |
| [2507.07389: ST-GRIT: Spatio-Temporal Graph Transformer For Internal Ice Layer Thickness Prediction](https://arxiv.org/abs/2507.07389v1) | 关闭 | 完整题摘：时空冰层厚度科学预测，暂缓 AI for Science |
| [2507.07393: KeyRe-ID: Keypoint-Guided Person Re-Identification using Part-Aware Representation in Videos](https://arxiv.org/abs/2507.07393v3) | 关闭 | 完整题摘：person re-ID 的 keypoint/part representation 任务特定组合，未指出语言/多模态基础模型机制差额 |
| [2507.07394: Behave Your Motion: Habit-preserved Cross-category Animal Motion Transfer](https://arxiv.org/abs/2507.07394v1) | 关闭 | 完整题摘复查关闭：root扩查：animation类别habit encoder与LLM连接未见物种，为任务表征组合，不改变基础模型机制主线。 |
| [2507.07396: IML-Spikeformer: Input-aware Multi-Level Spiking Transformer for Speech Processing](https://arxiv.org/abs/2507.07396v2) | 保留潜在贡献；日期隔离 | input-aware 多级 spike 用单时步代替多时步及 attention decay mask |
| [2507.07400: KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows](https://arxiv.org/abs/2507.07400v1) | 保留潜在贡献；日期隔离 | 已知 AgentStepGraph 的未来执行顺序驱动 KV eviction 与 prefetch，不是单纯缓存容量调优 |
| [2507.07406: Phishing Detection in the Gen-AI Era: Quantized LLMs vs Classical Models](https://arxiv.org/abs/2507.07406v1) | 关闭 | 题名范围：phishing 分类应用 |
| [2507.07410: EscherNet++: Simultaneous Amodal Completion and Scalable View Synthesis through Masked Fine-Tuning and Enhanced Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2507.07410v1) | 保留潜在贡献；日期隔离 | masked novel-view 与 amodal completion 的跨视角组合生成机制 |
| [2507.07413: Hybrid LLM-Enhanced Intrusion Detection for Zero-Day Threats in IoT Networks](https://arxiv.org/abs/2507.07413v1) | 关闭 | 题名范围：intrusion detection 应用 |
| [2507.07414: GNN-CNN: An Efficient Hybrid Model of Convolutional and Graph Neural Networks for Text Representation](https://arxiv.org/abs/2507.07414v1) | 保留潜在贡献；日期隔离 | 字符输入的 lattice/small-world graph 表征替代长文本 quadratic attention |
| [2507.07415: EPIC: Efficient Prompt Interaction for Text-Image Classification](https://arxiv.org/abs/2507.07415v1) | 关闭 | 完整题摘复查关闭：中间层prompt+similarity interaction用于分类，是prompt adaptation模块组合；资源/分数变化不建立新交互成立边界。 |
| [2507.07417: May I have your Attention? Breaking Fine-Tuning based Prompt Injection Defenses using Architecture-Aware Attacks](https://arxiv.org/abs/2507.07417v2) | 保留潜在贡献；日期隔离 | 白盒 prompt injection 攻击对防御假设的反证 |
| [2507.07419: MedReadCtrl: Personalizing medical text generation with readability-controlled instruction learning](https://arxiv.org/abs/2507.07419v1) | 关闭 | 题名范围：医学任务，暂缓 AI for Science |
| [2507.07421: SynthEHR-Eviction: Enhancing Eviction SDoH Detection with LLM-Augmented Synthetic EHR Data](https://arxiv.org/abs/2507.07421v1) | 关闭 | 题名范围：EHR 医学任务，暂缓 AI for Science |
| [2507.07424: Corvid: Improving Multimodal Large Language Models Towards Chain-of-Thought Reasoning](https://arxiv.org/abs/2507.07424v1) | 关闭 | 完整题摘复查关闭：hybrid encoder/GateMixer、CoT dataset、两阶段训练和self-verification，摘要未说明独特gating或over/under-reasoning控制条件。 |
| [2507.07426: DrugMCTS: a drug repurposing framework combining multi-agent, RAG and Monte Carlo Tree Search](https://arxiv.org/abs/2507.07426v3) | 关闭 | 题名范围：drug MCTS，暂缓 AI for Science |
| [2507.07432: Neural networks leverage nominally quantum and post-quantum representations](https://arxiv.org/abs/2507.07432v2) | 保留潜在贡献；日期隔离 | next-token learning 的 belief geometry 条件与状态表征边界 |
| [2507.07439: Towards Interpretable Time Series Foundation Models](https://arxiv.org/abs/2507.07439v1) | 关闭 | 完整题摘：time-series 的趋势/叙述 distillation 可行性应用，未呈现新的 distillation 条件 |
| [2507.07441: SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://arxiv.org/abs/2507.07441v2) | 保留潜在贡献；日期隔离 | 候选动作 deliberation、执行与 critique 的分离控制 |
| [2507.07445: StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production-Living Simulations with Stardew Valley](https://arxiv.org/abs/2507.07445v4) | 关闭 | 完整题摘：新游戏 task/interface 与低成功率，未隔离到新的评测 confound 或 Agent failure 因果机制 |
| [2507.07451: RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning](https://arxiv.org/abs/2507.07451v1) | 保留潜在贡献；日期隔离 | verified experience replay 将新/旧 rollout 混合用于 RL 训练 |
| [2507.07456: General-Purpose Models for the Chemical Sciences: LLMs and Beyond](https://arxiv.org/abs/2507.07456v2) | 关闭 | 题名范围：化学应用，暂缓 AI for Science |
| [2507.07464: Degradation-Agnostic Statistical Facial Feature Transformation for Blind Face Restoration in Adverse Weather Conditions](https://arxiv.org/abs/2507.07464v4) | 关闭 | 完整题摘：天气下人脸恢复的局部 feature distribution 对齐，任务特定 adaptation，未见基础模型生成机制的新选择边界 |
| [2507.07484: Machine Bullshit: Characterizing the Emergent Disregard for Truth in Large Language Models](https://arxiv.org/abs/2507.07484v1) | 保留潜在贡献；日期隔离 | RLHF/CoT 与 truth bias 的潜在设计反证 |
| [2507.07485: Resolving Token-Space Gradient Conflicts: Token Space Manipulation for Transformer-Based Multi-Task Learning](https://arxiv.org/abs/2507.07485v2) | 保留潜在贡献；日期隔离 | token-space gradient conflict modulation，区别于 parameter replication |
| [2507.07495: PLAN-TUNING: Post-Training Language Models to Learn Step-by-Step Planning for Complex Problem Solving](https://arxiv.org/abs/2507.07495v1) | 关闭 | 完整题摘复查关闭：synthetic planning trajectory distillation+SFT/RL的已有post-training组合，分数没有隔离新planning学习/控制机制。 |
| [2507.07496: Semi-supervised learning and integration of multi-sequence MR-images for carotid vessel wall and plaque segmentation](https://arxiv.org/abs/2507.07496v1) | 关闭 | 完整题摘：MRI 血管/斑块 segmentation，暂缓 AI for Science |
| [2507.07498: Teaching LLM to Reason: Reinforcement Learning from Algorithmic Problems without Code](https://arxiv.org/abs/2507.07498v2) | 关闭 | 完整题摘复查关闭：code-related RL数据策划与分数提升，未说明如何受控分离algorithm-pattern overfitting与general reasoning。 |
| [2507.07499: Extracting ORR Catalyst Information for Fuel Cell from Scientific Literature](https://arxiv.org/abs/2507.07499v1) | 关闭 | 题名范围：catalyst，暂缓 AI for Science |
| [2507.07505: Hallucination Stations: On Some Basic Limitations of Transformer-Based Language Models](https://arxiv.org/abs/2507.07505v3) | 保留潜在贡献；日期隔离 | LLM computational complexity 的条件性限制，不无条件外推 |
| [2507.07509: Toward Real-World Chinese Psychological Support Dialogues: CPsDD Dataset and a Co-Evolving Multi-Agent System](https://arxiv.org/abs/2507.07509v1) | 关闭 | 题名范围：心理领域应用，不是本日机制主线 |
| [2507.07510: Divergence Minimization Preference Optimization for Diffusion Model Alignment](https://arxiv.org/abs/2507.07510v2) | 保留潜在贡献；日期隔离 | reverse-KL 与 mean-seeking diffusion alignment 的分布覆盖取舍 |
| [2507.07539: CEA-LIST at CheckThat! 2025: Evaluating LLMs as Detectors of Bias and Opinion in Text](https://arxiv.org/abs/2507.07539v1) | 保留潜在贡献；日期隔离 | 噪声/标签不一致条件下高级 prompt 未优于标准 few-shot，潜在低成本反证 |
| [2507.07544: Position: We Need An Algorithmic Understanding of Generative AI](https://arxiv.org/abs/2507.07544v1) | 关闭 | 完整题摘复查关闭：position/AlgEval研究路线及case-study方法介绍，摘要未给出可改判的具体circuit发现/成立条件。 |
| [2507.07551: ArchiveGPT: A human-centered evaluation of using a vision language model for image cataloguing](https://arxiv.org/abs/2507.07551v1) | 关闭 | 完整题摘：考古目录 human trust 应用，缺少新机制/controlled boundary |
| [2507.07562: The Synergy Dilemma of Long-CoT SFT and RL: Investigating Post-Training Techniques for Reasoning VLMs](https://arxiv.org/abs/2507.07562v1) | 保留潜在贡献；日期隔离 | SFT 与 RL 组合不叠加的负证据，需限制数据、预算、难度和 response length 混杂 |
| [2507.07572: Single-to-mix Modality Alignment with Multimodal Large Language Model for Document Image Machine Translation](https://arxiv.org/abs/2507.07572v1) | 关闭 | 完整题摘复查关闭：DIMT encoder对齐teacher multimodal representation后inference bypass，是已知distillation组合，领域泛化分数未隔离新条件。 |
| [2507.07579: NexViTAD: Few-shot Unsupervised Cross-Domain Defect Detection via Vision Foundation Models and Multi-Task Learning](https://arxiv.org/abs/2507.07579v1) | 关闭 | 题名范围：缺陷检测领域应用，无明确基础模型机制线索 |
| [2507.07586: Your Absorbing Discrete Diffusion Secretly Models the Bayesian Posterior](https://arxiv.org/abs/2507.07586v2) | 保留潜在贡献；日期隔离 | absorbing diffusion posterior Monte Carlo 集中性与计算成本取舍 |
| [2507.07589: Stress Monitoring in Healthcare: An Ensemble Machine Learning Framework Using Wearable Sensor Data](https://arxiv.org/abs/2507.07589v1) | 关闭 | 完整题摘：healthcare stress 的 SMOTE/stacking 应用，无基础模型机制差额 |
| [2507.07591: Stable-Hair v2: Real-World Hair Transfer via Multiple-View Diffusion Model](https://arxiv.org/abs/2507.07591v1) | 关闭 | 完整题摘复查关闭：hair-transfer的pose embedding、temporal attention、多阶段training组合，未建立新的生成factorization或视角一致性成立条件。 |
| [2507.07599: Enhancing Vaccine Safety Surveillance: Extracting Vaccine Mentions from Emergency Department Triage Notes Using Fine-Tuned Large Language Models](https://arxiv.org/abs/2507.07599v1) | 关闭 | 题名范围：疫苗应用，暂缓 AI for Science |
| [2507.07605: LOSC: LiDAR Open-voc Segmentation Consolidator](https://arxiv.org/abs/2507.07605v2) | 关闭 | 完整题摘复查关闭：image-label back-projection、时空consistency consolidation及3D训练的已有范式组合，无独特consolidation规则。 |
| [2507.07610: SpatialViz-Bench: A Cognitively-Grounded Benchmark for Diagnosing Spatial Visualization in MLLMs](https://arxiv.org/abs/2507.07610v7) | 保留潜在贡献；日期隔离 | 程序生成 spatial tasks 与 CoT 失败的受控评测 |
| [2507.07620: ViLU: Learning Vision-Language Uncertainties for Failure Prediction](https://arxiv.org/abs/2507.07620v4) | 关闭 | 完整题摘复查关闭：多embedding/cross-attention+binary correctness classifier的post-hoc管线，loss-agnostic不自动建立新的uncertainty机制/条件。 |
| [2507.07622: TransformEEG: Towards Improving Model Generalizability in Deep Learning-based EEG Parkinson's Disease Detection](https://arxiv.org/abs/2507.07622v1) | 关闭 | 题名范围：EEG 医学应用，暂缓 AI for Science |
| [2507.07623: Capture Stage Matting: Challenges, Approaches, and Solutions for Offline and Real-Time Processing](https://arxiv.org/abs/2507.07623v2) | 关闭 | 完整题摘：capture-stage matting workflow/domain adaptation guideline，未识别通用生成模型的新机制或受控边界 |
| [2507.07630: Exploring the Limits of Model Compression in LLMs: A Knowledge Distillation Study on QA Tasks](https://arxiv.org/abs/2507.07630v1) | 关闭 | 完整题摘：QA student 保留性能的压缩结果，未给出超出现有 distillation 的机制或有效性控制 |
| [2507.07633: T-GVC: Trajectory-Guided Generative Video Coding at Ultra-Low Bitrates](https://arxiv.org/abs/2507.07633v4) | 保留潜在贡献；日期隔离 | trajectory latent guidance 对几何运动控制 |
| [2507.07634: FrugalRAG: Less is More in RL Finetuning for Multi-Hop Question Answering](https://arxiv.org/abs/2507.07634v3) | 保留潜在贡献；日期隔离 | 准确性与 retrieval frugality 的 reward 冲突 |
| [2507.07640: Lost in Pronunciation: Detecting Chinese Offensive Language Disguised by Phonetic Cloaking Replacement](https://arxiv.org/abs/2507.07640v1) | 保留潜在贡献；日期隔离 | 自然 phonetic cloaking 相对合成扰动的检测边界，Pinyin mitigation 的相反证据 |
| [2507.07644: FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations](https://arxiv.org/abs/2507.07644v4) | 保留潜在贡献；日期隔离 | 符号化 floorplan 的物理约束评测 |
| [2507.07653: An Automated Length-Aware Quality Metric for Summarization](https://arxiv.org/abs/2507.07653v1) | 关闭 | 完整题摘复查关闭：semantic similarity与length compression组合metric，未识别新受控盲点或改变quality/length取舍的条件。 |
| [2507.07685: Rationale-Enhanced Decoding for Multi-modal Chain-of-Thought](https://arxiv.org/abs/2507.07685v2) | 保留潜在贡献；日期隔离 | 图像与 rationale logit 分布组合，以检查忽略 CoT 的 failure mode |
| [2507.07694: SAS: Simulated Attention Score](https://arxiv.org/abs/2507.07694v2) | 保留潜在贡献；日期隔离 | higher-dimensional head 与 PEAA 的参数/容量取舍 |
| [2507.07695: KeyKnowledgeRAG (K^2RAG): An Enhanced RAG method for improved LLM question-answering capabilities](https://arxiv.org/abs/2507.07695v2) | 关闭 | 完整题摘：dense+sparse+KG+summary 管线，headline cost 与分数组合不构成设计增量 |
| [2507.07709: One Object, Multiple Lies: A Benchmark for Cross-task Adversarial Attack on Unified Vision-Language Models](https://arxiv.org/abs/2507.07709v1) | 保留潜在贡献；日期隔离 | 跨任务 simultaneous VL attack 与局部区域攻击机制 |
| [2507.07723: Stable Preference Optimization: A Bilevel Approach to Catastrophic Preference Shift](https://arxiv.org/abs/2507.07723v2) | 保留潜在贡献；日期隔离 | likelihood displacement 导致 OOD shift，bilevel safety constraint |
| [2507.07725: Not All Preferences are What You Need for Post-Training: Selective Alignment Strategy for Preference Optimization](https://arxiv.org/abs/2507.07725v1) | 保留潜在贡献；日期隔离 | token log-probability difference 的 selective DPO/reference-quality 取舍 |
| [2507.07731: Energy-Guided Decoding for Object Hallucination Mitigation](https://arxiv.org/abs/2507.07731v1) | 保留潜在贡献；日期隔离 | energy-guided layer selection 针对 hallucination/yes bias |
| [2507.07735: GuardVal: Dynamic Large Language Model Jailbreak Evaluation for Comprehensive Safety Testing](https://arxiv.org/abs/2507.07735v1) | 保留潜在贡献；日期隔离 | 动态 defender state 驱动 jailbreak search，避免静态搜索停滞 |
| [2507.07743: Identification of Violin Reduction via Contour Lines Classification](https://arxiv.org/abs/2507.07743v1) | 关闭 | 完整题摘：violin contour 几何分类，非模型/系统主线 |
| [2507.07748: When Large Language Models Meet Law: Dual-Lens Taxonomy, Technical Advances, and Ethical Governance](https://arxiv.org/abs/2507.07748v1) | 关闭 | 题名范围：法律 taxonomy 应用 |
| [2507.07781: SURPRISE3D: A Dataset for Spatial Understanding and Reasoning in Complex 3D Scenes](https://arxiv.org/abs/2507.07781v1) | 保留潜在贡献；日期隔离 | 3D 无 object naming 的 spatial shortcut 控制 |
| [2507.07787: Measuring AI Alignment with Human Flourishing](https://arxiv.org/abs/2507.07787v2) | 关闭 | 完整题摘：wellbeing/flourishing 维度集合，未呈现改变模型/系统取舍的具体盲点或控制证据 |
| [2507.07796: Visual Instance-aware Prompt Tuning](https://arxiv.org/abs/2507.07796v1) | 保留潜在贡献；日期隔离 | instance prompt 与 dataset prompt 的 PCA/适配组织 |
| [2507.07803: StreamUni: Achieving Streaming Speech Translation with a Unified Large Speech-Language Model](https://arxiv.org/abs/2507.07803v2) | 保留潜在贡献；日期隔离 | 语音 segmentation policy 与生成的统一 streaming 路径 |
| [2507.07804: Deep Survival Analysis in Multimodal Medical Data: A Parametric and Probabilistic Approach with Competing Risks](https://arxiv.org/abs/2507.07804v1) | 关闭 | 完整题摘：多模态 oncology survival，暂缓 AI for Science |
| [2507.07808: Bridging Logic and Learning: Decoding Temporal Logic Embeddings via Transformers](https://arxiv.org/abs/2507.07808v1) | 关闭 | 完整题摘：STL specialized decoder 的需求挖掘应用，没有通用模型机制差额 |
| [2507.07810: Understanding and Controlling Repetition Neurons and Induction Heads in In-Context Learning](https://arxiv.org/abs/2507.07810v2) | 保留潜在贡献；日期隔离 | repetition neurons 与 induction heads 的层深区别及反证 |
| [2507.07814: Pay Attention to Attention Distribution: A New Local Lipschitz Bound for Transformers](https://arxiv.org/abs/2507.07814v2) | 保留潜在贡献；日期隔离 | attention distribution local Lipschitz/Jacobian regularization |
| [2507.07817: On the Effect of Instruction Tuning Loss on Generalization](https://arxiv.org/abs/2507.07817v2) | 保留潜在贡献；日期隔离 | prompt/response SFT loss 权重的 training boundary |
| [2507.07818: MoSE: Skill-by-Skill Mixture-of-Experts Learning for Embodied Autonomous Machines](https://arxiv.org/abs/2507.07818v2) | 关闭 | 完整题摘复查关闭：skill/router pretrain+多auxiliary task single forward，未建立区别于既有skill/MoE路由的原始控制或优化机制。 |
| [2507.07820: AI Should Sense Better, Not Just Scale Bigger: Adaptive Sensing as a Paradigm Shift](https://arxiv.org/abs/2507.07820v3) | 关闭 | 完整题摘：adaptive sensing 倡议、既有研究综述和未来路线；未有本文原创的受控机制证据 |
| [2507.07824: Conditional Unigram Tokenization with Parallel Data](https://arxiv.org/abs/2507.07824v1) | 保留潜在贡献；日期隔离 | semantic parallel tokenizer 与 quadratic data 假设的反证 |
| [2507.07828: Benchmarking Content-Based Puzzle Solvers on Corrupted Jigsaw Puzzles](https://arxiv.org/abs/2507.07828v2) | 关闭 | 完整题摘：jigsaw corruption task fine-tuning，无基础模型机制增量 |
| [2507.07839: MeD-3D: A Multimodal Deep Learning Framework for Precise Recurrence Prediction in Clear Cell Renal Cell Carcinoma (ccRCC)](https://arxiv.org/abs/2507.07839v1) | 关闭 | 完整题摘：renal recurrence 医学 multimodal fusion，暂缓 AI for Science |
| [2507.07846: ROS Help Desk: GenAI Powered, User-Centric Framework for ROS Error Diagnosis and Debugging](https://arxiv.org/abs/2507.07846v1) | 关闭 | 完整题摘：ROS user-centric error diagnosis 的 GenAI 应用，未说明新的控制/grounding/安全条件 |
| [2507.07847: From Ambiguity to Accuracy: The Transformative Effect of Coreference Resolution on Retrieval-Augmented Generation systems](https://arxiv.org/abs/2507.07847v3) | 保留潜在贡献；日期隔离 | coreference-aware retrieval pooling/disambiguation 的小模型边界 |
| [2507.07862: Predicting and generating antibiotics against future pathogens with ApexOracle](https://arxiv.org/abs/2507.07862v1) | 关闭 | 完整题摘：antibiotic generation，暂缓 AI for Science |
| [2507.07867: Re-Bottleneck: Latent Re-Structuring for Neural Audio Autoencoders](https://arxiv.org/abs/2507.07867v2) | 保留潜在贡献；日期隔离 | audio latent post-hoc bottleneck 的语义结构/等变性 |
| [2507.07870: DocCHA: Towards LLM-Augmented Interactive Online diagnosis System](https://arxiv.org/abs/2507.07870v1) | 关闭 | 题名范围：医学应用，暂缓 AI for Science |
| [2507.07877: Edge-ASR: Towards Low-Bit Quantization of Automatic Speech Recognition Models](https://arxiv.org/abs/2507.07877v2) | 关闭 | 完整题摘复查关闭：8种PTQ/两类ASR配置benchmark，3-bit高容量结果未给出超出既有capacity/calibration取舍的具体新条件。 |
| [2507.07878: Single-Step Latent Diffusion for Underwater Image Restoration](https://arxiv.org/abs/2507.07878v2) | 关闭 | 题名范围：underwater image restoration 任务，未见基础模型主线机制线索 |
| [2507.07885: UnIT: Scalable Unstructured Inference-Time Pruning for MAC-efficient Neural Inference on MCUs](https://arxiv.org/abs/2507.07885v1) | 保留潜在贡献；日期隔离 | 无 SIMD MCU 的 irregular input-dependent MAC skip，将乘法代为 threshold 比较；系统边界而非按小模型排除 |
| [2507.07887: Automating MD simulations for Proteins using Large language Models: NAMD-Agent](https://arxiv.org/abs/2507.07887v2) | 关闭 | 题名范围：蛋白模拟，暂缓 AI for Science |
| [2507.07893: An Integrated Framework of Prompt Engineering and Multidimensional Knowledge Graphs for Legal Dispute Analysis](https://arxiv.org/abs/2507.07893v4) | 关闭 | 题名范围：法律应用 |
| [2507.07902: MIRA: A Novel Framework for Fusing Modalities in Medical RAG](https://arxiv.org/abs/2507.07902v1) | 关闭 | 题名范围：medical RAG，暂缓 AI for Science |
| [2507.07906: Agentic Retrieval of Topics and Insights from Earnings Calls](https://arxiv.org/abs/2507.07906v1) | 关闭 | 题名范围：earning-call retrieval 应用 |
| [2507.07910: DTECT: Dynamic Topic Explorer & Context Tracker](https://arxiv.org/abs/2507.07910v2) | 关闭 | 完整题摘：topic pipeline 与 LLM label/chat，无新的模型/系统执行条件 |
| [2507.07929: Towards Continuous Home Cage Monitoring: An Evaluation of Tracking and Identification Strategies for Laboratory Mice](https://arxiv.org/abs/2507.07929v1) | 关闭 | 题名范围：lab mice vision，暂缓 AI for Science |
| [2507.07935: Working with AI: Measuring the Applicability of Generative AI to Occupations](https://arxiv.org/abs/2507.07935v6) | 关闭 | 题名范围：职业适用性社会研究，非模型机制 |
| [2507.07939: SAGE: A Visual Language Model for Anomaly Detection via Fact Enhancement and Entropy-aware Alignment](https://arxiv.org/abs/2507.07939v2) | 具体争议；日期/核心定义隔离 | 定点v1 §3.3 Eq3–7：MLE score entropy gap进入BT margin；Eq4同一全候选entropy却称per-answer，Eq6/7未展示ref/KL却文称使用。中心定义不闭合，无性能/Books正面证据；不擅改公式。 |
| [2507.07947: Reconstructing Template-Memorized Images from Natural Prompts](https://arxiv.org/abs/2507.07947v4) | 保留潜在贡献；日期隔离 | image benign prompt reconstruction 的 template memorization 安全信号 |
| [2507.07955: Dynamic Chunking for End-to-End Hierarchical Sequence Modeling](https://arxiv.org/abs/2507.07955v2) | 保留潜在贡献；日期隔离 | H-Net dynamic chunking 与 byte-level modeling 的 compute-matched tokenizer 取舍 |
| [2507.07957: MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957v1) | 关闭 | 完整题摘复查关闭：六memory类型与multi-agent update/retrieval/应用指标；taxonomy未给出独特写入、撤销、provenance、检索控制或一致性条件。 |
| [2507.07966: Scaling RL to Long Videos](https://arxiv.org/abs/2507.07966v4) | 关闭 | 完整题摘复查关闭：CoT-SFT/RL、sequence parallel与cached video embedding的full-stack组合，摘要未建立新的cache validity/更新同步/并行执行条件。 |
| [2507.07978: Martian World Model: Controllable Video Synthesis with Physically Accurate 3D Reconstructions](https://arxiv.org/abs/2507.07978v2) | 关闭 | 完整题摘：Martian camera/domain world-model 任务，未体现主线可复用的新条件化机制；仅概念名不足以准入 |
| [2507.07981: Why is Your Language Model a Poor Implicit Reward Model?](https://arxiv.org/abs/2507.07981v3) | 保留潜在贡献；日期隔离 | token cue 的 implicit reward/OOD 边界与 explicit reward 控制 |
| [2507.07982: Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling](https://arxiv.org/abs/2507.07982v2) | 保留潜在贡献；日期隔离 | video diffusion 3D geometry forcing 的角度/尺度对齐 |
| [2507.07983: Performance and Practical Considerations of Large and Small Language Models in Clinical Decision Support in Rheumatology](https://arxiv.org/abs/2507.07983v1) | 关闭 | 完整题摘：rheumatology clinical decision 应用，暂缓 AI for Science |
| [2507.07984: OST-Bench: Evaluating the Capabilities of MLLMs in Online Spatio-temporal Scene Understanding](https://arxiv.org/abs/2507.07984v2) | 保留潜在贡献；日期隔离 | online horizon memory 与 spatial two-axis 组织 |
| [2507.07985: Common Data Properties Limit Object-Attribute Binding in CLIP](https://arxiv.org/abs/2507.07985v2) | 保留潜在贡献；日期隔离 | 数据 caption density/saliency 与 binding 的受控评测 |
| [2507.07988: Automating Expert-Level Medical Reasoning Evaluation of Large Language Models](https://arxiv.org/abs/2507.07988v1) | 关闭 | 完整题摘：medical expert reasoning evaluation，暂缓 AI for Science |
| [2507.07990: Multi-Granular Spatio-Temporal Token Merging for Training-Free Acceleration of Video LLMs](https://arxiv.org/abs/2507.07990v1) | 保留潜在贡献；日期隔离 | query-agnostic spatiotemporal token merge 与 KV reuse |
| [2507.07993: Multigranular Evaluation for Brain Visual Decoding](https://arxiv.org/abs/2507.07993v2) | 关闭 | 题名范围：brain visual decoding，暂缓 AI for Science |
| [2507.07996: Skip a Layer or Loop it? Test-Time Depth Adaptation of Pretrained LLMs](https://arxiv.org/abs/2507.07996v1) | 保留潜在贡献；日期隔离 | MCTS test-time layer skip/repeat，正确路径 oracle 与部署成本需区分 |
| [2507.07998: PyVision: Agentic Vision with Dynamic Tooling](https://arxiv.org/abs/2507.07998v3) | 保留潜在贡献；日期隔离 | 动态生成 Python visual tools 的交互控制 |
| [2507.08000: Impact of Pretraining Word Co-occurrence on Compositional Generalization in Multimodal Models](https://arxiv.org/abs/2507.08000v1) | 保留潜在贡献；日期隔离 | concept-pair PMI 对比 unigram 的多模态泛化归因 |
| [2507.08039: Towards Evaluating Robustness of Prompt Adherence in Text to Image Models](https://arxiv.org/abs/2507.08039v1) | 保留潜在贡献；日期隔离 | basic shape/location 的 T2I adherence 受控负证据 |
| [2507.08045: Krul: Efficient State Restoration for Multi-turn Conversations with Dynamic Cross-layer KV Sharing](https://arxiv.org/abs/2507.08045v2) | 保留潜在贡献；日期隔离 | Krul dynamic cross-layer similarity 与 KV 恢复 schedule 的压缩/恢复取舍；必须恢复 exact v1 |
| [2507.08046: TableReasoner: Advancing Table Reasoning Framework with Large Language Models](https://arxiv.org/abs/2507.08046v1) | 关闭 | 完整题摘复查关闭：root扩查：schema-link+programming+iterative reflection的表QA编排，竞赛第一名不是新控制或验证机制。 |
| [2507.08059: The relative importance of being Gaussian](https://arxiv.org/abs/2507.08059v1) | 关闭 | 完整题摘复查关闭：替换Gaussian noise的实验问题及小图环境，摘要没有具体观测/成立条件，不把问题倡议当反证。 |
| [2507.08064: PUMA: Layer-Pruned Language Model for Efficient Unified Multimodal Retrieval with Modality-Adaptive Learning](https://arxiv.org/abs/2507.08064v4) | 保留潜在贡献；日期隔离 | pruning layer+self-distillation 与 modality-adaptive contrastive |
| [2507.08068: Quantile Reward Policy Optimization: Alignment with Pointwise Regression and Exact Partition Functions](https://arxiv.org/abs/2507.08068v2) | 保留潜在贡献；日期隔离 | quantile reward offline regression 与可计算 partition 取舍 |
| [2507.08877: ODIA: Oriented Distillation for Inline Acceleration of LLM-based Function Calling](https://arxiv.org/abs/2507.08877v1) | 关闭 | 完整题摘复查关闭：production simple-query discovery+distillation+traffic routing，未定义区别于既有query routing的识别/置信/更新条件。 |
| [2507.08878: Towards Privacy-Preserving and Personalized Smart Homes via Tailored Small Language Models](https://arxiv.org/abs/2507.08878v1) | 关闭 | 完整题摘复查关闭：local SLM+可选less-sensitive remote query/privacy shield，未提供不同于本地化/脱敏策略的新泄露机制或安全条件。 |
| [2507.08881: The Consistency-Acceptability Divergence of LLMs in Judicial Decision-Making: Task and Stakeholder Dimensions](https://arxiv.org/abs/2507.08881v1) | 关闭 | 完整题摘：司法社会接受度与多利益相关方治理框架，不是模型/系统技术机制 |
| [2507.08885: AirScape: An Aerial Generative World Model with Motion Controllability](https://arxiv.org/abs/2507.08885v2) | 关闭 | 完整题摘复查关闭：6DoF aerial data、motion intentions及两阶段adaptation，首次领域/数据不是新的action-conditioning或空间状态机制。 |
| [2507.10442: Response Wide Shut? Surprising Observations in Basic Vision Language Model Capabilities](https://arxiv.org/abs/2507.10442v1) | 保留潜在贡献；日期隔离 | visual encoder/projector/decoder 的 probe 与最终 response 区分，定位信息可用却不会利用的边界 |
| [2507.14171: IPPRO: Importance-based Pruning with PRojective Offset for Magnitude-indifferent Structural Pruning](https://arxiv.org/abs/2507.14171v3) | 保留潜在贡献；日期隔离 | projective scale-invariant pruning 与 functional norm 边界 |
| [2507.14172: Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://arxiv.org/abs/2507.14172v2) | 关闭 | 完整题摘复查关闭：evolutionary program search+hindsight pairs+self-training组合，未隔离新的search/training有效性条件；ARC分数不是机制差额。 |
| [2507.21110: SemRAG: Semantic Knowledge-Augmented RAG for Improved Question-Answering](https://arxiv.org/abs/2507.21110v1) | 关闭 | 完整题摘复查关闭：root扩查：cosine semantic chunking+KG与buffer-size调参的既有组合，没有新可迁移机制/成立条件。 |

## 宽入口已有相关线索的定点补充

| 原始材料身份 | 贡献处置 | 理由/读取范围 |
| --- | --- | --- |
| [2507.07318: Generating Moving 3D Soundscapes with Latent Diffusion Models](https://arxiv.org/abs/2507.07318v2) | 关闭 | 完整题摘复查关闭：FOA moving-sound领域的text/trajectory conditioning及模拟数据扩展，未呈现新factorization、codec或控制成立条件。 |
| [2507.07357: Short-Term Gains, Long-Term Gaps: The Impact of GenAI and Search Technologies on Retention](https://arxiv.org/abs/2507.07357v1) | 关闭 | 题名范围：学生留存/教育社会效应，不是模型/系统机制 |
| [2507.07486: Sparse Autoencoders Reveal Interpretable Structure in Small Gene Language Models](https://arxiv.org/abs/2507.07486v1) | 关闭 | 题名范围：基因应用，暂缓 AI for Science |
| [2507.07548: From Requirements to Code: Understanding Developer Practices in LLM-Assisted Software Engineering](https://arxiv.org/abs/2507.07548v1) | 关闭 | 完整题摘：开发者访谈/需求工件，软件实践而非模型/系统执行机制 |
| [2507.07568: Learnable Retrieval Enhanced Visual-Text Alignment and Fusion for Radiology Report Generation](https://arxiv.org/abs/2507.07568v1) | 关闭 | 题名范围：放射学应用，暂缓 AI for Science |
| [2507.07574: Beyond the Linear Separability Ceiling: Aligning Representations in VLMs](https://arxiv.org/abs/2507.07574v4) | 保留潜在贡献；日期隔离 | perception/reasoning 线性可分上限的定位与 contrastive alignment |
| [2507.07682: Prompt Engineering for Requirements Engineering: A Literature Review and Roadmap](https://arxiv.org/abs/2507.07682v1) | 关闭 | 完整题摘：requirements prompt engineering 文献 taxonomy，无新增机制 |
| [2507.07689: From Domain Documents to Requirements: Retrieval-Augmented Generation in the Space Industry](https://arxiv.org/abs/2507.07689v1) | 关闭 | 题名范围：space industry RAG 应用 |
| [2507.07767: Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course](https://arxiv.org/abs/2507.07767v2) | 关闭 | 完整题摘：课堂 structured UI 学习行为，不是模型/系统机制 |
| [2507.07799: SecureSpeech: Prompt-based Speaker and Content Protection](https://arxiv.org/abs/2507.07799v1) | 关闭 | 完整题摘：NER/redaction/TTS 安全应用组合，无新的身份/泄露威胁模型或受控 privacy 条件 |
| [2507.07881: Opting Out of Generative AI: a Behavioral Experiment on the Role of Education in Perplexity AI Avoidance](https://arxiv.org/abs/2507.07881v1) | 关闭 | 题名范围：用户避免 GenAI 的行为研究，非模型/系统机制 |
| [2507.07901: The Trust Fabric: Decentralized Interoperability and Economic Coordination for the Agentic Web](https://arxiv.org/abs/2507.07901v3) | 关闭 | 完整题摘复查关闭：DID/cards/credentials/policy-as-code/container组合；headline compliance没有明确新威胁模型/安全成立条件，不作保证。 |
| [2507.07916: Can Large Language Models Automate Phishing Warning Explanations? A Controlled Experiment on Effectiveness and User Perception](https://arxiv.org/abs/2507.07916v2) | 关闭 | 题名范围：phishing warning 用户感知，非模型机制 |
| [2507.07932: KIS-S: A GPU-Aware Kubernetes Inference Simulator with RL-Based Auto-Scaling](https://arxiv.org/abs/2507.07932v1) | 关闭 | 完整题摘复查关闭：GPU simulator+PPO autoscaler与reward/P95指标，未说明新simulation fidelity或sim-to-real成立机制。 |
| [2507.07938: Multimodal Framework for Explainable Autonomous Driving: Integrating Video, Sensor, and Textual Data for Enhanced Decision-Making and Transparency](https://arxiv.org/abs/2507.07938v1) | 关闭 | 完整题摘：VideoMAE/BERT/sensor fusion 预测 driving action 并解释，未提供可区分于常规组合的机制/有效性边界 |
| [2507.07954: Input Conditioned Layer Dropping in Speech Foundation Models](https://arxiv.org/abs/2507.07954v1) | 保留潜在贡献；日期隔离 | speech input-conditioned layer dropping 的动态 compute 控制 |
| [2507.07974: Defending Against Prompt Injection With a Few DefensiveTokens](https://arxiv.org/abs/2507.07974v2) | 保留潜在贡献；日期隔离 | optimized defensive token embedding 的 utility/security switch |

## 重开请求（同一身份只列一次）

下列保留项每项都需要官方历史公告批次/公开时间（含 exact version）或作者首次公开正文的可信时间记录，才能判断是否落于 `[2025-07-10T09:00+08:00, 2025-07-11T09:00+08:00)`。只给 submission、month-level Available、OAI last modification、DataCite Updated、窗外 registration 或当前 v2/v3 题摘均不足。可接受替代材料为官方带日期的当期邮件/公告原件，或可核验作者首次全文发布记录；恢复后只打开受影响行，先日期再 exact-version 核心审阅。无日期的潜在贡献不改写成零事件。

- [2507.07186: Planted in Pretraining, Swayed by Finetuning: A Case Study on the Origins of Cognitive Biases in LLMs](https://arxiv.org/abs/2507.07186v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07188: Prompt Perturbations Reveal Human-Like Biases in Large Language Model Survey Responses](https://arxiv.org/abs/2507.07188v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07192: Bridging the Last Mile of Prediction: Enhancing Time Series Forecasting with Conditional Guided Flow Matching](https://arxiv.org/abs/2507.07192v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07297: MagiC: Evaluating Multimodal Cognition Toward Grounded Visual Reasoning](https://arxiv.org/abs/2507.07297v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07313: Frontier LLMs Still Struggle with Simple Reasoning Tasks](https://arxiv.org/abs/2507.07313v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07341: On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment](https://arxiv.org/abs/2507.07341v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07375: Bradley-Terry and Multi-Objective Reward Modeling Are Complementary](https://arxiv.org/abs/2507.07375v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07396: IML-Spikeformer: Input-aware Multi-Level Spiking Transformer for Speech Processing](https://arxiv.org/abs/2507.07396v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07400: KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows](https://arxiv.org/abs/2507.07400v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07410: EscherNet++: Simultaneous Amodal Completion and Scalable View Synthesis through Masked Fine-Tuning and Enhanced Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2507.07410v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07414: GNN-CNN: An Efficient Hybrid Model of Convolutional and Graph Neural Networks for Text Representation](https://arxiv.org/abs/2507.07414v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07417: May I have your Attention? Breaking Fine-Tuning based Prompt Injection Defenses using Architecture-Aware Attacks](https://arxiv.org/abs/2507.07417v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07432: Neural networks leverage nominally quantum and post-quantum representations](https://arxiv.org/abs/2507.07432v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07441: SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://arxiv.org/abs/2507.07441v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07451: RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning](https://arxiv.org/abs/2507.07451v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07484: Machine Bullshit: Characterizing the Emergent Disregard for Truth in Large Language Models](https://arxiv.org/abs/2507.07484v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07485: Resolving Token-Space Gradient Conflicts: Token Space Manipulation for Transformer-Based Multi-Task Learning](https://arxiv.org/abs/2507.07485v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07505: Hallucination Stations: On Some Basic Limitations of Transformer-Based Language Models](https://arxiv.org/abs/2507.07505v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07510: Divergence Minimization Preference Optimization for Diffusion Model Alignment](https://arxiv.org/abs/2507.07510v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07539: CEA-LIST at CheckThat! 2025: Evaluating LLMs as Detectors of Bias and Opinion in Text](https://arxiv.org/abs/2507.07539v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07562: The Synergy Dilemma of Long-CoT SFT and RL: Investigating Post-Training Techniques for Reasoning VLMs](https://arxiv.org/abs/2507.07562v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07574: Beyond the Linear Separability Ceiling: Aligning Representations in VLMs](https://arxiv.org/abs/2507.07574v4): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07586: Your Absorbing Discrete Diffusion Secretly Models the Bayesian Posterior](https://arxiv.org/abs/2507.07586v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07610: SpatialViz-Bench: A Cognitively-Grounded Benchmark for Diagnosing Spatial Visualization in MLLMs](https://arxiv.org/abs/2507.07610v7): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07633: T-GVC: Trajectory-Guided Generative Video Coding at Ultra-Low Bitrates](https://arxiv.org/abs/2507.07633v4): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07634: FrugalRAG: Less is More in RL Finetuning for Multi-Hop Question Answering](https://arxiv.org/abs/2507.07634v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07640: Lost in Pronunciation: Detecting Chinese Offensive Language Disguised by Phonetic Cloaking Replacement](https://arxiv.org/abs/2507.07640v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07644: FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations](https://arxiv.org/abs/2507.07644v4): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07685: Rationale-Enhanced Decoding for Multi-modal Chain-of-Thought](https://arxiv.org/abs/2507.07685v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07694: SAS: Simulated Attention Score](https://arxiv.org/abs/2507.07694v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07709: One Object, Multiple Lies: A Benchmark for Cross-task Adversarial Attack on Unified Vision-Language Models](https://arxiv.org/abs/2507.07709v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07723: Stable Preference Optimization: A Bilevel Approach to Catastrophic Preference Shift](https://arxiv.org/abs/2507.07723v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07725: Not All Preferences are What You Need for Post-Training: Selective Alignment Strategy for Preference Optimization](https://arxiv.org/abs/2507.07725v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07731: Energy-Guided Decoding for Object Hallucination Mitigation](https://arxiv.org/abs/2507.07731v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07735: GuardVal: Dynamic Large Language Model Jailbreak Evaluation for Comprehensive Safety Testing](https://arxiv.org/abs/2507.07735v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07781: SURPRISE3D: A Dataset for Spatial Understanding and Reasoning in Complex 3D Scenes](https://arxiv.org/abs/2507.07781v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07796: Visual Instance-aware Prompt Tuning](https://arxiv.org/abs/2507.07796v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07803: StreamUni: Achieving Streaming Speech Translation with a Unified Large Speech-Language Model](https://arxiv.org/abs/2507.07803v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07810: Understanding and Controlling Repetition Neurons and Induction Heads in In-Context Learning](https://arxiv.org/abs/2507.07810v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07814: Pay Attention to Attention Distribution: A New Local Lipschitz Bound for Transformers](https://arxiv.org/abs/2507.07814v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07817: On the Effect of Instruction Tuning Loss on Generalization](https://arxiv.org/abs/2507.07817v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07824: Conditional Unigram Tokenization with Parallel Data](https://arxiv.org/abs/2507.07824v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07847: From Ambiguity to Accuracy: The Transformative Effect of Coreference Resolution on Retrieval-Augmented Generation systems](https://arxiv.org/abs/2507.07847v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07867: Re-Bottleneck: Latent Re-Structuring for Neural Audio Autoencoders](https://arxiv.org/abs/2507.07867v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07885: UnIT: Scalable Unstructured Inference-Time Pruning for MAC-efficient Neural Inference on MCUs](https://arxiv.org/abs/2507.07885v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07939: SAGE: A Visual Language Model for Anomaly Detection via Fact Enhancement and Entropy-aware Alignment](https://arxiv.org/abs/2507.07939v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07947: Reconstructing Template-Memorized Images from Natural Prompts](https://arxiv.org/abs/2507.07947v4): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07954: Input Conditioned Layer Dropping in Speech Foundation Models](https://arxiv.org/abs/2507.07954v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07955: Dynamic Chunking for End-to-End Hierarchical Sequence Modeling](https://arxiv.org/abs/2507.07955v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07974: Defending Against Prompt Injection With a Few DefensiveTokens](https://arxiv.org/abs/2507.07974v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07981: Why is Your Language Model a Poor Implicit Reward Model?](https://arxiv.org/abs/2507.07981v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07982: Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling](https://arxiv.org/abs/2507.07982v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07984: OST-Bench: Evaluating the Capabilities of MLLMs in Online Spatio-temporal Scene Understanding](https://arxiv.org/abs/2507.07984v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07985: Common Data Properties Limit Object-Attribute Binding in CLIP](https://arxiv.org/abs/2507.07985v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07990: Multi-Granular Spatio-Temporal Token Merging for Training-Free Acceleration of Video LLMs](https://arxiv.org/abs/2507.07990v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07996: Skip a Layer or Loop it? Test-Time Depth Adaptation of Pretrained LLMs](https://arxiv.org/abs/2507.07996v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.07998: PyVision: Agentic Vision with Dynamic Tooling](https://arxiv.org/abs/2507.07998v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.08000: Impact of Pretraining Word Co-occurrence on Compositional Generalization in Multimodal Models](https://arxiv.org/abs/2507.08000v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.08039: Towards Evaluating Robustness of Prompt Adherence in Text to Image Models](https://arxiv.org/abs/2507.08039v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.08045: Krul: Efficient State Restoration for Multi-turn Conversations with Dynamic Cross-layer KV Sharing](https://arxiv.org/abs/2507.08045v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.08064: PUMA: Layer-Pruned Language Model for Efficient Unified Multimodal Retrieval with Modality-Adaptive Learning](https://arxiv.org/abs/2507.08064v4): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.08068: Quantile Reward Policy Optimization: Alignment with Pointwise Regression and Exact Partition Functions](https://arxiv.org/abs/2507.08068v2): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.10442: Response Wide Shut? Surprising Observations in Basic Vision Language Model Capabilities](https://arxiv.org/abs/2507.10442v1): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
- [2507.14171: IPPRO: Importance-based Pruning with PRojective Offset for Magnitude-indifferent Structural Pruning](https://arxiv.org/abs/2507.14171v3): 缺实际公开批次与 exact version；理由见上表；原件在对应 discovery JSON。待该身份证据到达后重开本行，不追全月镜像。
