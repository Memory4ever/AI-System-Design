# 2026-09-18 Daily 筛选账本

**窗口：** 2026-09-17T09:00:00+08:00 ～ 2026-09-18T09:00:00+08:00

本文件只保留可复查的准入口径和 identity；候选证据与 Books 判断以当日 `README.md` 为准。

## arXiv 漏斗

- 目标分类：`cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA`。
- 官方 Thursday new list 跨分类去重后：621 个 new/cross identity；另检查 293 个 replacement identity 的重要修订、纠错与撤回信号。
- 有界宽筛：原有 189 项之外，对终审圈定的 14 项逐项读取完整摘要；其中 3 项经 first-public date 复核归入早先 owner，11 项进入当窗贡献判断。
- 当窗冻结：62 个 arXiv Source Family。24 个 cross-list identity 为早先首发的重复事件，122 项完整题摘 false positive 按 family-specific 理由关闭；原有恢复项不变，本次恢复 `2609.18270`、`2609.18306`、`2609.18520`、`2609.18649`、`2609.18860`、`2609.17904`、`2609.18622` 七项。其余 413 项标题层明确关闭逐项记录于下文。

### 当窗 arXiv 候选（62）

```text
2609.17542 2609.17560 2609.17573 2609.17652 2609.17691 2609.17848
2609.17745 2609.17857 2609.17904 2609.17930 2609.17940 2609.17943 2609.17983
2609.17989 2609.17997 2609.18005 2609.18016 2609.18063 2609.18066 2609.18080
2609.18099 2609.18110 2609.18112 2609.18123 2609.18128 2609.18145
2609.18178 2609.18204 2609.18314 2609.18346 2609.18357 2609.18388
2609.18270 2609.18306 2609.18520 2609.18649 2609.18860
2609.18440 2609.18453 2609.18460 2609.18471 2609.18516 2609.18519
2609.18560 2609.18622 2609.18672 2609.18675 2609.18703
2609.18708 2609.18769 2609.18820 2609.18842 2609.18849 2609.18857
2609.18878 2609.18998 2609.19000 2609.19024 2609.19101 2609.19107 2609.19135
2609.19145
```

### 早先首发、本窗去重（24）

```text
2408.07702 2510.04816 2609.09206 2609.15289 2609.17552 2609.17590 2609.17594
2609.17599 2609.17645 2609.17759 2609.17772
2609.17817 2609.17842 2609.18041 2609.18052 2609.18298 2609.18805
2609.18864 2609.18958 2609.19002 2609.19125
2609.17555 2609.18959 2609.19006
```

### 完整题摘后关闭（122）

下面把每个 identity 映射到唯一的候选前关闭理由。分组不是按关键词自动判定，而是题摘语义复核后的主因；同一论文即使同时命中多个弱点，也只放入最主要的一组。

#### A. 单领域任务、机器人/VLA、应用或 benchmark（47）

关闭条件：结果主要回答特定应用、机器人控制、视觉/物理任务或 benchmark 表现，没有改变大模型/Infra 的通用 state、data、control ownership 或 evaluation contract。

```text
2609.17728 17885 17909 17953 17985 18058 18108 18167 18193
18197 18207 18232 18242 18259 18323 18328 18374 18392 18430 18442
18445 18462 18487 18497 18514 18562 18605 18623 18644 18650 18651 18663
18690 18869 18909 18929 18950 18991 18996 19072 19104 19137 19138 19142
17800 17977 18496
```

#### B. 局部模型、表示、剪枝、量化、对齐或优化器改进（27）

关闭条件：方法在局部指标上可能有效，但题摘与原文没有改变 Books 中已有机制的适用边界、状态所有权或系统 contract。

```text
2609.17535 17553 17748 17764 17790 17888 17890 18057 18084
18131 18176 18239 18321 18515 18587 18642 18656 18662 18723
18779 18792 18916 18961 18966 19011 19144 18416
```

#### C. Agent/RAG/数据框架或产品包装（23）

关闭条件：提供 workflow、memory、retrieval、data-generation 或 agent packaging，但没有超出现有 owner 的耐久机制；项目名或实现组合本身不构成长期增量。

```text
2609.17564 17653 17695 17699 17709 17775 17921 17969 17984 18042 18077
18094 18182 18304 18366 18417 18461 18540 18736 18935 19059 19128 18120
```

#### D. 解释、一般理论、行为观察或局部评价结果（19）

关闭条件：论文提供现象、可读性、一般学习理论或局部评价信号，但没有形成可采用的 AI-System design delta；相关性或理论构造也不能直接取得 production 决策权。

```text
2609.17537 17550 17571 17708 17804 17865 18047 18078 18126 18190
18320 18591 18612 18745 18985 18989 19113 19124 18045
```

#### E. 立场、综述、协议提案或证据不足的 technical report（6）

关闭条件：主要是 synthesis/治理提案/technical report，或者缺少足以改变长期判断的 primary method/evaluation；不以“听起来重要”替代证据。

```text
2609.17631 17686 17863 18272 18283 18310
```

上述每个代码块首个 ID 写全前缀，后续六位数字均与 `2609.` 组合。分组计数合计 122；它们仍保留 identity 与 family-specific 关闭理由，但不进入候选评分或 Source Review。本轮新增六项关闭结论分别为：AgenTeeth 是牙科 VLM 的 tool-evidence 应用；When to Call an LLM 是情绪识别场景对既有 confidence cascade 的迁移；MiST 是网络安全领域的 continued pretraining/SFT 配方；随机子空间梯度下降是未落到 LLM 训练边界的一般优化理论；PentestChain 是已知 MCP/cascade/evaluation 控制的安全领域组合；Hidden Agents 是一般多智能体动力系统的隐变量图推断。后续定点审阅确认 `2609.18622` 会改变模型选择的评价合同，`2609.17904` 会改变离散控制下的物理安全边界，二者已移入候选并完成 exact-v1 Source Review。

### 标题层明确关闭（413）

本节补齐 raw union 中标题层关闭项。每行保留完整 identity、标题和本项目口径下的具体关闭理由；这些条目不进入评分或 Source Review。终审圈定的 14 项已全部移出本表并完成摘要分流：3 项归入前日 owner、6 项进入完整题摘关闭、5 项恢复为候选。

| arXiv ID | 标题 | 关闭理由 |
| --- | --- | --- |
| `2609.17532` | Enhancing Extubation Failure Prediction with LLM-Derived Features from Respiratory Therapy Clinical Notes | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17534` | Faking Good and Faking Bad in LLMs: Response Distortion Across Dark Triad Personality Traits | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.17536` | Think Before You Comfort: Reflective Cognitive Alignment for Protocol-Grounded Elderly Stimulation Agents | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.17538` | From Pixels to Pairs: A Comprehensive Benchmark of LLM-Based Key-Value Extraction in Noisy Document Settings | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17539` | MudawanSn: A Gold-Standard Wolof-Arabic Parallel Corpus for Machine Translation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17540` | Human-Centric Grasp State Assessment: Toward Transferring Subjective Evaluation to Robots | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17541` | Real-Time Service Robot Replanning via Simple Button Interaction for Improved Task Success and User Experience | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17544` | Large Language Models Versus Physicians in Traditional Chinese Medicine: A Real-World Clinical Case Evaluation | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17545` | Selective Prediction and Uncertainty-Aware Referral for Pap Smear Classification | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17546` | Legal LLM Hallucination Should Be Evaluated as Failure of Legal Warrant | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17547` | How AI Assistants Respond to Repeated Abuse | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17548` | Myovox: Reading Speech from the Muscles of the Face | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17549` | Do Social Patterns Hold in Synthetic Data? Analyzing Cyberbullying Dynamics in LLM-Generated and Authentic Dialogues | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.17554` | English Word Sense Disambiguation in 2026: When the Labels Become the Bottleneck | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17556` | WARD: Runtime Workload-Adaptive Vision TRansformer Framework for Dependable Edge AI | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17562` | BLADE: ReliaBle Dynamic Hardware-Aware SNN-ANN Boundary SeLection for Event-BAseD Object DEtection | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17565` | A Heisenberg Lift Descriptor for Order Sensitive Online Handwriting Recognition | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17566` | Adaptive Interpolatory Curve Subdivision with Learned Local Angles | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17568` | Independence-System Realisations in Single-Source Unsplittable Flow | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17569` | Lyapunov-based analysis of functional stability for edge computing systems | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17572` | Disentangling Algorithmic Bias from Archival Artifacts: A Controlled Audit of Vision-Language Model Valuation in Metropolitan Museum Archives | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17575` | Temperon: Full-Time SAM Quality at a Third Less Wall-Clock | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17577` | Rényi Tracking Bounds for Langevin Dynamics with Moving Targets | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17578` | Generic Characteristic-Zero Equivalence Between Derivative Bézout Inversion and Multipoint Evaluation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17595` | Prior-Free Competitive Ratios for Improving Bandits: Scale, Curvature and Horizon Are Free, but Not Jointly Under Noise | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17601` | Decentralized Optimal Equilibrium Learning Over Dynamic Networks | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17602` | Making Political Text Scaling Comparable: Infrastructure and Hyperparameter Sensitivity for 17 Algorithms | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17612` | Timbre Analysis of the Hulusi, a Southwestern Chinese Free-Reed Instrument, using Machine Learning | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17613` | DualCount: Structurally Consistent Density and Point Modeling for Zero-Shot Object Counting | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17619` | Stability-Constrained Approximation in Spline KANs: Exact Layer Balancing and Budget-Compatible Saturation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17620` | Democratizing Clinical Tumor Whole Genome Sequencing: 18-hour End-to-end Analysis via Trillion-parameter Large Language Models Locally Deployed on Consumer-grade Hardware | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17625` | Predictive Varanus: Combining CSP Conformance Monitoring with Predictive LTL Runtime Verification | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17627` | Flexible-body Modeling, Kinematic Identification, and Assembly Accuracy of Overconstrained Spatial Linkages | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17628` | LEAP: Learning Emergent Active Perception for Quadruped Navigation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17632` | EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.17633` | One Color Preprocessing Improves DSATUR | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17635` | Physics-Constrained Digital Twins for Sensor Integrity in Urban Pedestrian Flow: Detecting Stealthy False Data Injection with Conformal Guarantees | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17637` | What You Can&#39;t See Is Still What You Learn: A Preregistered Sixty-Society Confirmation That Evidence Masking Drives Compositional Generalization | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17638` | Lecture notes on Physics Informed Neural Networks, Neural Operators, and their applications | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.17639` | Scaling Articulated Rationales for MLLM-based Recommendation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17644` | Rethinking Domain Specialization for Open-Ended Scientific Reasoning in Astronomy Language Models | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17646` | Robust and Efficient AI Frameworks for Scalable Material Design and Property Prediction | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17654` | Regularized Least Squares Training of Quadratic Neural Networks with Applications to System Identification | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17655` | Efficient Robust Learning at the Information-Theoretic Limit | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17682` | DSD: Learning Diverse and Reusable Motor Skills via Diffusion Skill Discovery | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17688` | CapMem: A Benchmark for Caption-Based Episodic Memory in Egocentric Video | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17696` | GVD: Governed Versioning and Deduplication for Document Repositories | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17697` | Composite-Gradient Learning for Shared Control Authority Between Deep Reinforcement Learning and Model Predictive Control | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17714` | Vision-Language Grounded Task-Context-Aware Imitation Learning for Robotic Disassembly | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17718` | SpecReuse: Spectral Graph Reuse for Efficient Vision GNN Inference on FPGAs | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17721` | Decoding Extrahepatic Targeting of Lipid Nanoparticles with Interpretable Machine Learning | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17726` | Self-Supervised Learning for Robust Resonance Mass Regression in Cascade Decays | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17730` | FAME: An FPGA-Based Platform for Approximate Multipliers Evaluation with Pattern-Guided DNN Retraining | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17731` | A Systematic Evaluation of the COTQ Provincial Land Cover Product: Structural Consistency, Spectral Separability, and Relative Positioning Against ESA, ESRI, and Google Products | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17735` | Optimal Scheduling in Generalized Switch in Heavy Traffic | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17736` | Machine learning kinetics from molecular dynamics data | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17738` | Similarity Pairing with Energy Mover&#39;s Distance for Self-Supervised Pre-Training at the LHC | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17740` | Geometry-Driven Shadow Harmonisation for Composited Faces: A Multiplicative, Albedo-Preserving Relighting Pipeline | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17747` | Is Trump&#39;s Vocabulary Poor? Vocabulary Richness Across Texts of Different Lenghts | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17749` | How to make effective use of domain experts for image classification? | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17753` | Beyond Performance Metrics: Uncertainty Mapping of Label Ambiguity in Fazekas Score Prediction | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17755` | Evolution of US Oral Political Language | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17757` | Imitation Learning for Autonomous Driving in CARLA | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17758` | CALOS: Control-Affine Lyapunov On-manifold Safety Layer for Safe Deep Reinforcement Learning for Quadrotors | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17762` | Is Luke the Author of a Gospel and the Acts of the Apostles? | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17763` | Modular Deep Learning Mechanisms for Auditable Next-Day Wildfire Spread Prediction | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17766` | DRT&amp;R: Direct Radar Teach &amp; Repeat | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17771` | HINT-Plan: Human Intention-Aware Robot Task Planning in Context-Rich Environments using Vision Language Models | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17777` | Information Set Emulation: Causal Certificates for AI Derived EHR Features | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17779` | AI and Human Approaches to Mathematical Problem Solving | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17781` | SPROUT: The Open-Source Soft Growing Robot for Search and Rescue | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17786` | FairCompressAgent: An Agentic Framework for Fairness-Aware Model Compression for FPGA Deployment | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17788` | SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17789` | QiT: Quantum-Inspired Transformer for Visual Recognition Task | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17797` | Set-membership localization of intermittent RF sources using a fleet of collaborating UAVs | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17808` | Synthetic Electric Vehicle Charging Session Generation Using a Conditional Variational Autoencoder | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17810` | Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17814` | GazeDiT: Gaze-Accurate Diffusion Image Generation for Eye Tracking via Spatial Conditioning | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17815` | Principled Koopman Representations with Kalman Inference for Efficient Time-Series Prediction | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17816` | The Free Inference Dimension: Complexity Measure for Zero-Collision Navigation under Hypothesis Mixtures | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17820` | CALIPER: Metric-Grounded Model-Free Recognition of Visually Similar Industrial Parts | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17823` | METALICA: METAdynamics and repLICA exchange for enhanced diffusion sampling | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17824` | Learning Multi-Humanoid Pickup and Transport via Decentralized Object-Centric Control | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17825` | NObSP: Functional Decomposition of Neural Networks via Oblique Subspace Projections | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17831` | Procedural Pretraining for Molecular Property Prediction | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17832` | Adaptive-MHE : A Sampling-Based Adaptive MPC for Legged Loco-Manipulation via Moving Horizon Estimation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17834` | VCTP: Vehicle-Conditioned Terrain Planning for Off-Road Navigation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17837` | Adaptive hybrid coupling with operator inference, the overlapping Schwarz alternating method and reinforcement learning | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17838` | Learning Nuclear Structure with AI: Radii and Collectivity | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17840` | Behavioral Analysis of Timed Actors using Syntactic Slice Equivalence | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17841` | Hybrid coupling with numerics-informed neural networks and the overlapping Schwarz alternating method | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17843` | RoboVAD: A Large Cross-Domain Evaluation Benchmark for Anomaly Detection in Robotic Arm Manipulation Videos | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17845` | Sharp margin-based generalization bounds for realizable SVM | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17846` | PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17847` | Learning Heterogeneous Preferences | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17853` | AfriSyCo: Measuring Assertive Framing, Verification, and Wording Sensitivity Around African-Language Content | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17855` | SNOMED CT Concept Recommendation from Masked Clinical Context | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17856` | Investigating Adversarial Robustness of Heterogeneous Cooperative Perception | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17866` | Uncertainty-Aware Continual Learning for Open-World Intent Discovery Under an evolving Label Space | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17868` | Lumen: Parameter-Efficient Alignment of Pretrained Vision and Language Encoders for Zero-Shot Computational Pathology | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17882` | Can VLMs Reliably Assess Sidewalk Accessibility Attributes from Pedestrian-Level Imagery? | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17883` | Does AI Assistance Leave a Temporal Fingerprint? Detecting Overreliance in AI-Assisted Writing and Programming | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17884` | The Unbearable Weight: Scaling Models and Methods for UAV Audio Classification | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17886` | Dataset-Dependent Effects of Cross-Depth Aggregation and Soft-Routed Experts in EEG Foundation Model Fine-Tuning | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17892` | Bracketing Uncertainty in Clustering Under the Manifold Hypothesis | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17895` | TabPFN-3.5: Technical Report | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17896` | QEMScore: How Much Does the Measurement Add to Learned Quantum Error Mitigation? | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17901` | Walking the Score Manifold: Continuous-time Generative Dynamics on Learned Data Manifolds | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.17903` | Composability rather than computation sets the cost of an analog EML hardware fabric | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17910` | Map2Route: Benchmarking Compositional Language-Grounded Route Planning over Semantic Maps | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17913` | Face-voice Association across LAnguages and Gender (FLAG) 2027 Challenge Evaluation Plan | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.17916` | EdgeReMIND: A Scalable, Top-Ranked Memorization Baseline for Temporal Multi-Relational Link Prediction | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17922` | Demystifying Gate-Level Localization of RTL Trojans | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.17923` | Audio for Sports Highlight Detection: A Comparative Empirical Study | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17925` | Rapid Loss of the Sierra Nevada&#39;s Largest Trees Driven by Fire | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17926` | Symmetry without a manifold: intrinsic dimension on orbits | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17929` | Multi-Session Multimodal Underwater Mapping with Acoustic and Optical Imaging | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17942` | On the Identifiability of Mixed Ordinal and Exponential Family Causal DAGs under Linear Parametric Models | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17946` | Feedback-Modulated Harmonic Policies for Quadruped Locomotion | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17951` | Maximum Strong Independent Sets in Hypergraphs: Reductions, Bounds, and Greedy Certificates | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17954` | Large Language Model based air quality monitoring and localized alert generation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17956` | TACTICS: Taxonomy-Aware Intelligent Corpus Sampling for Machine Translation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17964` | Mixed-Integer Nonlinear Differentiable Predictive Control for Underground Pumped Hydro Energy Storage Systems | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.17965` | Measuring AI Leadership: Development and Validation of a Multidimensional Measure for AI-Native Organizations | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17973` | Matching Multi-Loop Complexities with a Single Loop: Optimal Optimization Stationarity and Best-Known Game Stationarity in Nonconvex--Concave Minimax Optimization | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.17981` | Encoder Awakening via Adapters: Effective Domain-Adaptive Fine-tuning of Speech-LLMs | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.17987` | Multimodal Conditioning of Fine-Tuned Stable Diffusion XL for Controllable and Culturally Faithful Ulos Motif Generation | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.17991` | Fourier Analysis of Parametrized Interactive Quantum Classifiers | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.17992` | The Operable Pareto Front: Distilling Offline Search into Run-Time Control for Multi-Objective UAV Edge-Computing Scheduling | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.17995` | QuanText: Protecting Dataset-Level Secrets in Textual Data Sharing | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.17996` | Modeling the Developmental Shift in Telicity Acquisition | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18004` | Missing Bridges: Composition-Aware Active Imitation Learning | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18007` | Newer Is Not Fairer: Gender Stereotyping in Text-to-Image AI Across Model Generations | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18009` | SG-Mamba: Sparse Graph-Guided Mamba for Audio-Visual Speech Enhancement | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18011` | Gaze as Evidence for Common Grounding: A Cross-Corpus Analysis of MapTask and MUNDEX | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18022` | VeriBugBench: An Empirically Grounded Framework for Constructing Verilog RTL Debugging Benchmarks | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18025` | Physics-Informed Neural Networks for Fast Multilayer Spectral Inversion of Hα 6562.8 A and Ca II 8542.1 A Spectra | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18031` | Online Multimodal Workload Assessment in Contact-Rich Physical Human-Robot Interaction | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18034` | IRIS: Implicit Rendering Matters for Pose-Free Novel View Synthesis | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18037` | SetPlanner: A Lightweight Plug-in Point-Set Planner for Frozen SAM | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18038` | CoAtNet-DeepMoE: A Convolution-Attention Hybrid with DeepSeek Mixture-of-Experts for Parameter-Efficient Tomato Disease Classification | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18049` | Regional Explanations via Causal Sufficiency and Necessity | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18050` | Geometric Shortcuts for Complex Trunk Postures: Dual-Helicity Coupling Enables Low-Dimensional Control | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18051` | CLASP: A Cluster-Level Autonomous Selective Picking Robot with a Soft Rolling-Band Gripper for Fresh-Market Blueberry Harvesting | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18056` | Position Anchor Tuning: Towards Efficient Adaptation of Pre-Trained Point Cloud Transformers | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18068` | From a River in Gilead to the Inference Distributions of Large Language Models: Covert Dialect Bias and Linguistic Profiling at Scale | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18069` | GeoCueFormer: Geometry-Guided Wavelet Representation and Prediction-Cued Dual-Stage Decoder for Underwater Semantic Segmentation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18070` | An Efficient Algorithm for Minimum-Pressure Growth Planning of Vine Robots | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18072` | Teaching AI, Robotics, &amp; Community: A Hubs-Based K-12 Education Framework for Reaching Rural Schools | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18073` | Characterizing Refraction-Induced Ranging Bias in Underwater Collaborative Localization | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18082` | PESTO: Formally Correct Registration of LiDAR Point Clouds with Limited Overlap | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18088` | Mask 2D-3D: Adaptive Dual-Masked Autoencoder Network for Image-to-Point Cloud Registration | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18089` | FedPGT: Progressive Gradient Transmission for Vehicular Federated Learning over Time-Varying Channels | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18092` | ReRadar: Robust Radar Global Localization via Rotation-Equivariant Descriptor Learning | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18100` | Beyond Pixel Similarity: Task-Aware Evaluation of GAN-Based Synthetic Sonar Data for Robotic Perception | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18104` | iMINDBench: iEEG Multi-Institution Neural Decoding Benchmark | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18106` | Linguistic Triggers of Gender and Racial Bias in Open-Weight LLMs Applied to Recruitment | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18107` | FoundAna: A GNN-assisted Foundation Model for Graph Anomaly Detection | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18111` | A Comprehensive Review of Generative Physical Artificial Intelligence | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18117` | OpenDexGrasp: Open-vocabulary Task-Oriented Dexterous Grasping | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18118` | Preservation of Log-Concavity and Convergence of Wasserstein-Fisher-Rao Gradient Flows | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18119` | Fetch My Beer: Synthetic-to-real Hierarchical Policy for Smooth Pick-and-place | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18124` | Aligned Consensus Teaching for Label-Efficient Oriented Object Detection in Weakly-Aligned Visible-Infrared Imagery | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18125` | PRISM: Predictive Representation of Interaction Style and Motion for Social Robot Navigation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18127` | Learning Fractional-Order Dynamics from a Single Trajectory | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18129` | MCLC-NET: Multimodal Continual Learning for Leaf Counting | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18130` | Benchmarking Tabular Foundation Models as Surrogates in Expensive Evolutionary Optimization | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18133` | Stealthy in Semantics, Antagonistic in Space: Attacking Visible-Infrared Object Detectors via Object-Level Misalignment | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18134` | Rethinking How We Evaluate Methodological Progress in Health AI | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18135` | DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18139` | Multi-View Mixture-of-Experts with Vision-Language Reranking for Cross-View Object Geo-Localization | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18148` | LIGE-GR: A Smooth Leap from Ranking to Generative Recommendation in the LLM Era | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18153` | Prior Evolution and Task Alignment for Aerial Grasping | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18154` | PageRecall: Measuring Page Selection in Literature-Grounded Question Answering | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18156` | TeochewBench: A Human-Reviewed Benchmark for Teochew Hanzi Translation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18163` | Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18164` | Energy-Regularized Imitation Learning for Force- and Work-Aware Robotic Manipulation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18165` | LUMO: Designing Luminous Contact Morphology for Repeatable Whole-Finger Contact Observation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18169` | Approximating High Dimensional Self-Motion Manifolds via Deep Generative Models | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18173` | Beyond Direct Sensing: Harnessing Indirect Observations from Third-Party Sensors in Vehicle Tracking | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18174` | TacBPM: A Tactile-conditioned Behavior Prior Model for Dexterous Reorientation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18188` | Single-Token Expected-Value Scoring for Cold-Start Candidate Ranking | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18191` | OmniRisk: Omnidirectional Trajectory-Risk Learning for Agile Quadrotor Dynamic Avoidance | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18194` | T-SANDHI: Tone Sandhi-aware Adaptive Network with Decoupled Hybrid Injection for Low-resource Taiwanese Hokkien Speech Recognition | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18203` | Behavior2Value: Benchmarking and Empowering LLMs for Consumer Value Measurement from E-commerce Behaviors | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18206` | CapMap-MS-TTA: 3rd Place Solution for the MUMU Track of the 8th LSVOS Challenge at ECCV 2026 | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18210` | Understanding Dynamic Scenes at Gigapixel Scale: Wide-Area Spatio-Temporal Perception from UAVs | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18212` | A Lightweight CNN Integrated Compact Convolutional Transformer for Multi-Scale Feature Learning and reducing computational complexity for breast cancer mammography image detection and classification | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18213` | CANTABILE: Learning Expressive Dynamics for Robotic Piano Performance | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18216` | CPR: Combining global composing, local performing and full-sequence refining in piano rendering with continuous autoregressive modelling | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18219` | APGEM: Adaptive Policy-Guided Error Mitigation for Quantum Reinforcement Learning on a Real-World CVRP Case Study | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18223` | ABM-SIRTEM: A Hybrid Agent-Based and Epidemiological Model for Pandemic Response | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18224` | Remembering Solomon Marcus | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18227` | WISE: A Lightweight, Weakly-Supervised Model for Onboard Fire Smoke Detection and Localization | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18228` | Anomaly Detection in General Ledger Data: Results from a Hybrid Approach | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18238` | F-DACE: Fuzzy Disagreement-Aware Causal Evidence Fusion for Abstention-Safe Conversational Retail Decision Support | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18243` | Acting in Meters: Learning Metric Interactions for Precise Robotic Manipulation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18245` | A3P5 NEMESIS Integrated Rover Design for Environmental Reconnaissance and Robotic Sampling with Reproducible Mobility Analysis and an External Data Machine Learning Calibration Benchmark | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18248` | Quanta: A Self-Contained Python Library for Hybrid Retrieval over Quantised Embeddings, Lexical Indexes, and Knowledge Graphs | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18249` | Re2A: Situated Conversational Recommendation via Rubric-based Preference Reasoning and Alignment | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18256` | Evolving Error States: Failure-Aware Progressive Repair for Ultrasound Lesion Segmentation | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18260` | MS-RFD: Multi-Signal Release Frame Detection in Hammer Throw from Reconstructed 3D Trajectories | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18262` | REPAIR: Resolving Long-Tail Confusion in Scientific Retrievers via Fact-Verified Iterative Refinement | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18264` | Indicators of resilience for autonomous control systems | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18273` | Behavioral Fingerprinting and Navigation Prediction in Web Browsing | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18274` | I code or AI code: A comparative evaluation of AI-rated scores in classroom observations | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18278` | Building Trust in Artificial Intelligence: A Necessity for Railway Applications | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18279` | Decoder-Agnostic Token Merging for Vision Transformers: A Systematic Study of G2TM | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18281` | A GAN-Based Framework for Robust DDoS Attack Detection | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18282` | Too Good to Be Real? Diagnosing and Reducing the Gap Between AI Preference and Real User Engagement | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18284` | Made in Hungary: Comments on the performance of generative language models | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18286` | What Counts as Strategic Reasoning? A Systematic Mapping of Chess Research on Humans, Engines, and Language Models | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18291` | Relationally Guided Use Case Modeling with LLMs | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18293` | Function-Preserving Data Generation for Zero-Shot Real-to-Sim-to-Real Manipulation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18296` | One-Step Retrieval Framework for Real-Time Sponsored Search Ads Using Hierarchical Text Representations | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18302` | Visual Autoregressive Priors for RAW-to-sRGB Image Signal Processing | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18315` | Multi-Appliance Non-Intrusive Load Monitoring via Label-Preserving Aggregate Recomposition and Prediction Consistency | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18317` | Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18324` | RAFAIL: Relationship-Aware Failure Detection for Robotic Manipulation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18326` | UAVs Meet Embodied Intelligence: Bridging Human Intents and Flying Dynamics Via Harnessing Physical-Digital AI Agents | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18329` | PDA++: Field-Aligned Planning and Scene-Adaptive Insertion in Remote Sensing | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18333` | Look Less, Hear Better: Jointly Rewarded GRPO for Streaming ASR | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18336` | Pose2Muscle: Structured Spatio-Temporal Decoding for Discrete Muscle Activity Estimation from Human Pose | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18338` | Autonomy in Check: Governor-Mediated Adaptive Security at the Edge | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18341` | Understanding AI Provider Recommendations in Local Service Markets | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18345` | Visual Input and Its Framing Affect Attribute-based Descriptions Produced by Large Vision-Language Models | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18358` | GraphPoint: Semantic Entity Graphs and Point Trajectories for Compositional Robot Manipulation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18359` | RecMorph: Topology-Guided Spatial Recurrence for Generalized Morphology Control | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18363` | Online Multi-Camera 3D Tracking via ID Prediction over Recurrent Sparse Queries | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18368` | Semantic CSI Feedback for Beam Selection: When Task-Aware Embeddings from Sparse Pilots Outperform Full-Bandwidth Reconstruction | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18379` | JigSync: Gauge-Resolved Synchronization for Jigsaw Reassembly under Unknown Piece Orientation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18381` | Every Fixed Metric Has a Blind Spot: A Learned Atmospheric Critic for Scoring Forecast Realism | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18384` | GYROval: A Robust Benchmark for Cultural Value Orientation in Large Language Models | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18385` | Emotion Experience, Expression, and Perception: Emotion Analysis on Multimodal Social Media Posts | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18393` | MSR: Multiple Subject Reference for Video Generation | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18394` | Cultural Competence in Context: A Large Language Model Passes the Turing Test in Finland | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18395` | DetAug: Obstacle-Blind Trajectory Augmentation for Zero-shot Obstacle Avoidance | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18396` | Reliable Virtual Sensing: A Multi-Domain Benchmark for Robustness Under Sensor Failures | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18399` | A Non-Linear Neuron Based Detection of Isolated Pixels in Binary and Grayscale Images using Contrast Sensitive Receptive Fields | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18406` | Prosthesis-Aware 3D Human Pose Estimation: A Dataset and Benchmark for RSP Users | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18407` | TERN: A Delta-rule Memory with a Seasonal Reference and Online Adaptation for Epidemic Forecasting | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18413` | Vocabulary-Guided Gait Recognition | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18419` | HiLNO: A Hierarchical Latent Neural Operator with Multi-Scale Supervision for PDEs on General Geometries | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18431` | HPOQuest: A Rare-Disease Diagnostic Agent Using Active Phenotype Acquisition | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18432` | Occluded Gait Recognition with Mixture of Experts: An Action Detection Perspective | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18434` | Hardware-Free Robotics Laboratories in Mixed Reality | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18435` | WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18437` | Exploring LLMs and RAG for Plausible and Explainable Material Prediction of Vehicle Components | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18441` | Multitask Reinforcement Learning for Assisting Choice Model Specification | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18444` | DR.WILSS: Diffusion-Based Replay for Weakly Supervised Continual Semantic Segmentation | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18448` | From Pixels to Semantics: Edge AI for UAV-Based Critical Infrastructure Inspection | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18451` | VLM-MPPI: Grounding Natural Language in Behaviorally Diverse Trajectories for Aerial Navigation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18455` | ForwardDLO: Model-Based Bimanual Shape Matching of Unconstrained Deformable Linear Objects | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18459` | SEEK: Secure and Efficient Encrypted Keyword Search For Privacy-Preserving Messaging Protocols | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18465` | GeoCond: A Conditioning-Aware Reliability Adapter for Feed-Forward 3D Reconstruction | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18466` | Spatially Adaptive Noise Injection | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18470` | Divide and Conquer: Mixture-of-Bottleneck Experts in Informative Ordinal Space for Video-based Multimodal Sentiment Analysis | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18473` | CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18481` | Hyperbolic Graph Representation Learning for Differential Diagnosis on Biomedical Knowledge Graphs | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18482` | Real-Time Bounded Catenary Solver for UAV Tether Modeling | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18488` | Beyond Random Couplings: Contrastive Noise Alignment in Generative Flows | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18489` | Butterfly Effect and the Kinetic Energy Cascade in Probabilistic Machine Learning Weather Prediction Models | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18490` | Learning A Unified Template for Gait Recognition | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18493` | Semantic-ITC: A Frame-wise Indoor Mobile Laser Scanning Dataset and Benchmark for Semantic Segmentation | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18494` | Size Matters: Foundation Model for Czech HTML documents | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18504` | InterMASH: A Unified Geometric Representation for Grasp Synthesis | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18510` | DiT-Garment: Garment Dynamics with Diffusion Transformers | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18511` | Learning from Distributed Eyes: Leveraging Collaborative Perception for Automated Model Adaptation | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18512` | PatchyBFT: Automating Diversification of Fault-Tolerant Systems using LLMs | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18521` | VoiceTrace: A Benchmark and Retrieval Framework for Who-Said-What Speech Retrieval | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18525` | TRIPROBE: Probing Task Separability Beyond Classification for XAI | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18527` | Provable Guarantees for Spectral Structured Prediction | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18529` | Machine Translation between English and Syriac (East Syriac Dialect) using Statistical Machine Learning | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18533` | A Probe Shift Is Not a Fairness Fix: The Limits of Representation Steering in Speech Models | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18535` | Provable Guarantees and Efficient Learning of Structural Equation Models with Latent Confounders | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18542` | Accuracy- and Real-Time-Aware 4D Radar Preprocessing for Autonomous Driving Perception Systems | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18545` | Revisiting the Objective of Echo Chamber Detection | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18546` | STUNet-Fusion: Spatiotemporal Needle-Tip Localization in Ultrasound Video via Multi-Channel Motion Fusion | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18548` | HAP: A Hand-Driven Active Perception Framework for Egocentric Head Motion Prediction | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18549` | DynoFluxBench: Benchmarking Kinodynamic Space-Time Planners in Dynamic Environments | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18554` | CARA: Collision-Aware Resolution Adaptation for Multiresolution Hash Encoding Based Image Fitting | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18555` | Interpretable Patch-Based Deep Learning for Wildfire Spread Prediction from Ensemble Simulations | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18563` | AUPE: Collaborative byzantine fault-tolerant peer-sampling | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18565` | Variational Quantum Transformer Architecture for Synthetic Language Generation | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18566` | Deep learning emergent spacetime from fermionic spectral functions in holography | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18577` | Accurate Trace Estimation with Fewer Random Bits via Recursive TensorSketch | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18578` | Learning Where to Focus: Self-Supervised Multi-Scale ViTs for Histopathology | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18581` | GroundingVLN: Reasoning and Acting with Grounding for Vision-Language Navigation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18582` | On-the-Fly Homographies Calibration for Multi-Camera Tracking | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18585` | TTM-Bench: A Framework for Text-to-Music System Performance Benchmarking | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18588` | Peak-Aware Short-Term Load Forecasting Across Distribution Grid Aggregation Levels | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18595` | ReDIL-GNN: Resynthesis Domain Incremental Learning for Circuit Graph Neural Networks | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18597` | Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18598` | Hypothesis-Driven Autonomous Materials Synthesis with Multimodal LLM Agents | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18599` | Online Robust Reinforcement Learning Through Monte-Carlo Planning | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18602` | PULSE: Unlocking Practical Image Compression on Single-Thread CPU | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18610` | A Geometric Theory of Decision Boundaries in Structured Markov Decision Processes | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18616` | Learning Array Signal Topologies as Conditional Neural Manifolds | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18620` | DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18628` | Benchmarking Visual-Inertial Odometry in Subterranean Environments Under Sensor Degradation, Miscalibration, and Dynamic Occlusion | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18632` | VibeAvatar: Aligning Phonetic Kinematics and Human Aesthetics for High-Fidelity Talking Avatar Synthesis | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18633` | Netkit: Specializing Linux Packet Delivery for Container Networks | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18634` | GenStream: Semantic Streaming Framework for Generative Reconstruction of Human-centric Media | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18639` | CoRe-MARL: Cooperative Redistribution Under Unknown Dynamics Using Recurrent Multi-Agent Reinforcement Learning | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18655` | Learning to Program Adaptive Non-Local Observables for Machine Learning | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18667` | Video-Based Markerless Motion Capture for Clinical and Rehabilitation Biomechanics: A PRISMA-ScR Scoping Review of Validated Architectures, Clinical Readiness, and Emerging Methods | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18669` | M$^3$P-R1: Reinforcement Learning for Large Language Model Guided Multi-Modal Motion Planning via MIP Code Generation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18673` | Beyond EER: Multi-Dimensional Evaluation of Information Leakage in Speaker De-Identification | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18676` | The Uneven Impact of Generative AI on Student Learning: Examining the Roles of Reliance, Evaluation Literacy, and Course Policy in AI-related Courses | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18677` | Voice of Reason: Reinforcement Learning for Spoken Math | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18680` | HearInContext: A Benchmark for Implicit Context in Speech Recognition | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18682` | Rank and computation of the pathlifting Jacobian of a DAG ReLU network | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18685` | WeaveRL: Weaving Reconstruction into Scene-Aware Fabrics for Perceptive Reinforcement Learning | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18688` | Generalist-Specialist Mixture-of-Experts for Rare Pathology Detection in Multimodal Imaging | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18695` | SURF: Subtractive Updates for Recommender Forgetting | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18697` | Tracing individual knowledge trajectories in a changing field: the case of general relativity and gravitation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18700` | Toward 3D Printable Non-Planar Electroadhesive Structures for Active Anchoring | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18704` | Toward Composable Network Digital Twins: A Subgraph-Based Latency Prediction Study | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18706` | Echo: Learning-based Matching Decompilation using Trusted Back Translation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18716` | Mask IPL: Noise-Free Intrinsic Position Learning via Computation Graph Clipping for Event-Based Spike-Driven Tracking | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18718` | Calibrated Probabilistic Obstruction Reasoning with Vision-Language Models for Grasping in Clutter | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18720` | LocQE: Principled Domain Adaptation for Localisation Quality Estimation by Leveraging Post-Edits | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.18729` | &#34;If I Had to Buy Just ONE: Galaxy S26 Ultra&#34;: Auditing AI-Generated Product Recommendations | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18731` | Which LLM is Best for Translating Natural Language Goals to PDDL | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18732` | PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18737` | Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18738` | Active perception for robotic harvesting: 3D reconstruction and localisation of tomatoes hidden within clusters in a Mediterranean greenhouse | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18739` | A Scalable Framework for Automated NER Annotation Correction in Low-Resource Languages | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18748` | TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audio-Based Benchmark for Telecom Fraud Detection | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18752` | QMSR: Query-Conditioned Mask-wise Expert Routing for Robust Open-Vocabulary Underwater Object Retrieval | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18753` | Toward Markerless Video-based Tremor Analysis: Objective Quantification of Pathological Tremor in Mouse Preclinical Models | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18759` | Stable Filters for Generative Modeling of Graph Signals | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18763` | Gated Residual Body-Hand Coordination for Whole-Body Humanoid Teleoperation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18766` | FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18772` | Zero-Shot Cross-Lingual Recognition of Sign Language Handshapes | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18773` | DISTA-Net++: Rethinking Infrared Small Target Unmixing Beyond Sub-Pixel Separation | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18776` | TRACER: Adaptive Multi-Robot Social Navigation via Joint Human-Response Prediction and Interaction-Aware Replanning | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18778` | Vigil: Accountable Liveness against Selective Silence | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18782` | A Convergence Framework for Deep $V$-Learning: Error Propagation and Sharp Action-Gap Bounds | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18789` | AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18804` | Beyond frequency measures: Can contextual embeddings capture meaning change in scientific texts? | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18812` | WaveTLM: Reliable Time-Series Language Modeling through Task Compilation | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18813` | Asymptotically Optimal Multi-Robot Task and Motion Planning | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18819` | SEAM: Submap-Anchored Evidence for Lifelong LiDAR Mapping under Trajectory Deformation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18823` | Using OCR Heads to Verbalize Image Semantics | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18825` | Interpretable Multi-Instance Learning Enables Early Prediction of Key Molecular Alterations from Routine Flow Cytometry in Acute Myeloid Leukemia | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18836` | Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video Restoration | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18839` | A Distributed Computing Framework for Satellite Swarms | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18844` | ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint Artifacts | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18846` | Locus: A Framework for Exploring and Optimizing Point Addition Hardware for Zero-Knowledge Proofs | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18852` | EviGen: Predictive Evidence Scaffolding for Verifiable Clinical Rationale Generation | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18853` | Towards Interaction Regulation from Human Feedback via Free Energy Minimization | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18856` | GrainSpeech: Less Context, More Detail for Compact Speech Synthesis | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.18861` | PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18863` | Physics-based prediction, uncertainty quantification and decision-making for IN718 crystallographic texture intensity across LPBF defocus regimes | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18881` | Body-Motion Control of a Simulated Aerial Swarm from a First-Person View | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18886` | Fluid Notarization: Verifiable Evolution of Concurrently Edited Structured Documents | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18891` | NeuroECG: ECGFounder-Based Deep ECG Representation for EEG-Free Neurological Prognostication After Cardiac Arrest | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18893` | SOL-SLAM: Inverse Compositional Gauss-Newton Direct Registration for Fast Sonar-Only Local SLAM | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18894` | Learning Lyapunov Operators for Nonlinear Systems | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18898` | NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18900` | Examining the Difference in Human Behavior Between Virtual and Real-World Human-Robot Teaming | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18901` | Fast Learning Rates for Physics-Informed Kernel Methods | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18905` | Structured Claim-Level Discourse Representations for Dense Health Narratives | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18908` | How Much is a Human Right Worth? ECtHR-NPD: A Benchmark for Predicting Non-Pecuniary Damage Awards | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18910` | CaSCo: Cascade-Aware Soft-Collision Motion Planning | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18920` | PhysVGGT: Feed-Forward Dense Physical Property Estimation from A Single Image | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18924` | Ermes: a Stateful Serverless Platform for the Edge-to-Cloud Continuum | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18928` | Comprehensive reconstruction of collider events with hypergraph representation learning and graph-conditioned diffusion | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18930` | Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18932` | Replication-Aware Placement of Functions and Data in the Edge-Cloud Continuum | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.18943` | Dose-Aware Cold Diffusion with Physics Consistency for Generalizable Low-Dose CT Reconstruction | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18946` | Rect3D: A Unified Analytical Framework for 3D-IC Rectilinear Floorplanning | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18949` | StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.18952` | Automated Dental Caries Segmentation in Panoramic Radiographs Using Dual-Stage Deep Learning | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18955` | KDTwin: Task-Aware Knowledge Distillation for Lightweight Multi-Task Driving Scene Segmentation | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.18960` | When Audit Quality Fails to Predict Downstream Utility: A Counterfactual Study of Synthetic-Data Selectors for Low-Resource African NLP | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18964` | FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.18965` | BadQubits: An LLM-Based Framework for Static Pre-Execution Detection of Structurally Harmful Quantum Circuits | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.18970` | &#34;What&#39;s going to happen after I&#39;m gone?&#34;: Parent Perspectives on Technology in Supporting Independent Living for Adults with Intellectual Disabilities | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18971` | LaSeD: Label-Semantic Self-Distillation for Visual-Only Surgical Phase Recognition | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.18980` | Instrument Classification of Solo Sheet Music Images | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18983` | Flexible-Region Based Adaptive In-Loop Filter for Video Coding | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.18994` | A Benchmark Suite and Ground-Truth Methodology for Formal Verification of IEC 61131-3 Ladder Diagram Programs | 题名主要提供 benchmark、数据集、综述或评价入口；未显示暴露现有评估合同无法测得的关键长期边界。 |
| `2609.19004` | CompileRover: Revolutionizing Virtual Machine Compiler Optimization with a Tri-Role LLM-Driven Framework | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.19010` | Tabular Deep Learning vs Classical Machine Learning for Urban Land Cover Classification | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.19012` | Information-Based Trajectory Planning for Spacecraft-to-Spacecraft Tracking and Navigation in Cislunar Space | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.19022` | TalkMatrix: Generating Character Dialogue that is Both Consistent and Diverse | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19039` | LSR-Net: Learning the Forward Evolution Operator for Nonlinear Fluid Dynamics | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.19040` | Learning to Stack: Cube-Stacking Imitation Learning from Virtual Reality Demonstrations | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.19041` | Loco-Loco-RL: Low-Cost Terrain Mapping for Humanoid Locomotion with Reinforcement Learning | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.19042` | FedASAP: Activation Statistics-driven Structured Adaptive Pruning for Efficient Personalized Federated Learning for Lesion Segmentation on brain MRI | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.19044` | Entropy in Conversational AI: Structured Unpredictability as Inferrable Interiority | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19048` | Integrated Optimization of Automated Warehouse Operations and Last-Mile Transport for Differentiated On-Demand Delivery | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19062` | LightSleepX: A Lightweight, Inception-Based Dual-Modal Network for Sleep Staging | 题名指向通用计算机系统、网络或硬件问题；没有显示其机制直接改变大模型训练、推理或 Agent 平台的当前设计。 |
| `2609.19063` | MSLL: A Runtime Multi-Stack Parsing Approach for Interactive Grammar Development - A Lightweight Extension of LL-Style Recursive Descent | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19070` | Reading Between the Lines: Can LLMs Discover the Question Behind the Text? | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.19071` | Benchmarking Large Language Models for Biomedical Relation Extraction | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.19074` | RLLBC-Lib: An Educational Code Library for Reinforcement Learning and Learning-Based Control | 题名指向语言、语音、推荐或社会行为的特定任务/评测；未显示改变大模型/Infra 的通用设计选择或证据合同。 |
| `2609.19076` | Double descent is the principle of least action | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19077` | Probabilistic Linear Explanations | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19080` | ElastiQP: An Always-Feasible QP Solver for Constrained Robot Control | 题名已明确为机器人、自动驾驶或感知控制任务的领域方法/benchmark；未显示会改写通用大模型状态、控制权或平台合同。 |
| `2609.19083` | A General Kernel Framework for Non-CND Distance Measures Using \|D\|-Dimensional Sparse Landmark Embeddings | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19088` | MUSE: Benchmarking Large Vision-Language Models on Multi-Modal Understanding in Situated Education | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.19090` | Securing quantum error correction against misleading advice from AI agents | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.19093` | Reporting Practice Matters: The Impact of Reference Choice on Chest X-ray Report Evaluation | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |
| `2609.19096` | Prepared Or Unprepared? Evaluating Healthcare Workforce Readiness for Clinical Adoption of Artificial Intelligence in Nigeria | 题名已明确为医疗、自然科学、法律或其他垂直领域应用/建模；AI for Science 当前暂缓，且未显示大模型或 Infra 的通用机制变化。 |
| `2609.19099` | Evidence-Grounded Agentic Formulation Development in an Autonomous Laboratory | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.19111` | Analog Pin Directionality as an Exfiltration Attack Surface in Mixed-Signal ICs | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.19119` | Track, Articulate, Act: Generating Articulation from Casual Human Videos | 题名已明确为视觉/生成的单任务方法、数据集或指标改进；未显示对项目多模态表示/生成主线新增长期机制边界。 |
| `2609.19122` | Training-Adaptive Convolutional Sparse Coding via Information Bottleneck for Robust Visual Representation | 题名显示为局部学习、表示、生成或优化方法；没有显示其结果会改变 Books 现有机制边界、状态所有权或系统 contract。 |
| `2609.19134` | ScienceIDE: Turning World&#39;s Scientific Codebase into Agent Learnable Environments | 题名虽在大模型/Agent 范围内，但只显示领域应用、包装、行为观察或局部能力比较；没有可从题名成立的长期机制/边界增量。 |
| `2609.19143` | PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection | 题名所述对象未显示对大模型及其 Infra 主线的直接长期贡献；没有具体机制、设计边界或评价合同变化需要进入候选。 |

## 修订、纠错与撤回

- `2606.27409v2`：当窗重要修订，已对 delay indexing、stability/placement claim、factual QA 与 uncertainty 进行定点深审；不重复评分。
- `2605.06850`、`2608.04765`：已撤回，当日候选、评分和正面证据链路已清除。
- `2608.16010`、`2603.14005`、`2608.21388`：撤回/纠错信号已检查，当前报告和 Books 未发现正面候选痕迹。
- `2304.03370`：纠错属通用 ML 且不改变本项目判断，候选前关闭。
- `2509.19276`：AI for Science 当前暂缓，候选前关闭。

## 机构来源

- Meta/FAIR 当窗有一个可确认的新 artifact：[UnStep](https://github.com/facebookresearch/UnStep/tree/e7525751dc00582571cb3eea6e357cfa57db0843)，与 arXiv 冻结集去重后作为第 63 个候选；审阅绑定首个不可变 commit `e7525751dc00582571cb3eea6e357cfa57db0843`，不使用漂移的 `main` 作为证据身份。
- Anthropic 生物建模材料属 AI for Science，候选前关闭；frontier-lab measurement 条目只有日期、缺公开时刻，隔离为 Date Precision Gap。
- Google Research 当窗 Generative UI 教育应用未提供改变项目设计的长期机制，候选前关闭。

`provisional-evidence-inventory.json` 是终窗前的结构提取快照，不是最终候选集或 Source Review 完成证明；它被保留只用于审计已读原文片段。
