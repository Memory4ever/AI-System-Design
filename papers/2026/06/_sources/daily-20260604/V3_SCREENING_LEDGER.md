# 2026-06-04 V3 semantic screening ledger

> **Authority override（2026-09-11）：** 本文件下方 `73 / 502` 是作者侧二次收紧的可复验 checkpoint，不再是最终分母。非作者 fresh audit 与撤稿核验逐项关闭 2606.04101、2606.04233、2606.04460、2606.04507、2606.04536、2606.04660、2606.04847、2606.04883、2606.04970；最终 authority 为 **575 = 64 Candidate + 511 Close**。其中 UltraEP（2606.04101）的官方 arXiv v1/v2/v3 均 withdrawn（许可无权同意），只保留 pre-denominator withdrawal closure，不再授权 Candidate、评分、Source Review 或 Books。旧 Integrate 中 2606.04071、2606.04929 重判 `已有覆盖`；2606.04145 EvalStop 重判 `TRAIN-RLHF` Integrate proposal。legacy trace 与 post-Review note 不授权当前候选或 Books body。

## Withdrawal closure

| ID | 当前判断 | 关闭理由 |
| --- | --- | --- |
| 2606.04101 | Close / withdrawn | official arXiv v1/v2/v3 均显示 withdrawn，原因是提交者无权同意许可；因此不进入 denominator 后评分/Evidence/Books，任何旧采用链均须清除。 |

规则：逐项先读 title；只有边界项再读取 canonical raw inventory 的完整 abstract。这里记录的是 current-contract 判断，不继承旧 Complete/Open。Candidate 只表示进入候选分母，Books disposition 仍需复用 exact-v1 后重判。

## Batch 01 — generic incremental closure items 1–50

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.03998 | TGSD / EEG spatial super-resolution | Close | EEG 单一感知应用；没有大模型或通用 AI 基础设施机制。 |
| 2606.04000 | SPLIT-PINN | Close | 多晶材料概率建模；属于 AI-for-Science 垂直方法。 |
| 2606.04008 | Neural Radiated-Noise Fields | Close | UUV 声谱预测垂直任务；没有可迁移的大模型系统增量。 |
| 2606.04009 | Counterfactual Explanations for Deep Two-Sample Testing | Close | 通用统计解释方法，题目未落到大模型或其基础设施。 |
| 2606.04010 | The Variance Brain Foundation Models Forgot | Close | fMRI brain foundation model 的认知预测垂直研究；不进入当前大模型主线。 |
| 2606.04019 | Gravity-Aware SensorLLM for HAR | Close | 单一 wearable HAR 适配头；系统增量绑定传感器应用。 |
| 2606.04023 | CodegenBench | Candidate | 直接评测 LLM 在 CPU/GPU/HPC 架构上的代码效率，进入评测/硬件协同候选。 |
| 2606.04025 | Software 4.0 | Close | 完整摘要确认是 vision paper，形式语义和经验评测均留作未来工作，不能支持 durable 系统结论。 |
| 2606.04027 | MaskForge | Candidate | 直接提出 diffusion LLM 的结构感知 jailbreak 攻击，改变模型形态相关的安全面。 |
| 2606.04028 | IEEE P3109 arithmetic formats | Candidate | 完整摘要给出 ML 浮点格式、异常/舍入/块缩放语义与形式验证，属于数值执行合同。 |
| 2606.04029 | Deployed RL should be Continual | Close | 完整摘要是通用 deployed RL 立场与案例归纳，没有大模型特有机制或实现证据。 |
| 2606.04031 | Pseudospectral Bounds for Coupled GD | Close | 优化理论；没有大模型训练系统合同。 |
| 2606.04032 | QKV Variants | Candidate | 系统比较 Transformer Q/K/V 投影结构，直接影响大模型注意力架构。 |
| 2606.04033 | Inverse Critical Experiment Design | Close | 核反应堆实验设计垂直应用。 |
| 2606.04034 | Semantic Tower at Runtime | Close | 通用编程语言/运行时语义，不是 AI 系统贡献。 |
| 2606.04035 | Domain-Dependent Safety in Open-Weight LLMs | Candidate | 多模型、多安全域实验揭示部署安全透明度差异，进入安全评测候选。 |
| 2606.04036 | Self-Distilled Policy Gradient | Candidate | 标题与题摘对象是 language-model on-policy self-distillation，进入 post-training 候选。 |
| 2606.04037 | Pre-Deployment Assurance for Enterprise AI Agents | Candidate | 提出 ontology-grounded simulation/trust certification，直接针对 Agent 上线验收合同。 |
| 2606.04039 | Neural Guidance for Ant Colony Optimization | Close | ACO 搜索方法，未涉及大模型或其基础设施。 |
| 2606.04040 | EEG-to-Music Reconstruction | Close | BCI 垂直任务。 |
| 2606.04045 | Bayes-Sufficient Representations | Close | 监督学习表示理论，未形成大模型系统增量。 |
| 2606.04046 | SceneDiver | Candidate | 完整摘要给出 VLM/VLA coarse-to-fine focus plan 与 adapter 蒸馏，属于多模态决策控制机制。 |
| 2606.04047 | Microservice Structural Communities | Close | 普通软件架构演进分析，与 AI 系统主线无关。 |
| 2606.04048 | Gated Delta Networks at Scale | Candidate | 直接研究大模型 sub-quadratic architecture 的特征学习与 scaling。 |
| 2606.04050 | LiftQuant | Candidate | 连续 bit-width LLM 量化解决具体 memory-budget deployment gap。 |
| 2606.04051 | RUBAS | Candidate | rubric-based RL 直接约束 tool-enabled agent 的执行安全。 |
| 2606.04053 | Boolean Task Algebra | Close | 通用 RL 任务组合理论，未落到大模型。 |
| 2606.04057 | Invisible Lottery in LLM Code Generation | Candidate | 完整摘要以 46,535 次实验量化提示线索对算法选择、性能与安全的系统性影响。 |
| 2606.04058 | Spectral Scaling Laws of Muon | Candidate | Muon 是大模型训练优化器，scaling law 直接影响训练配置。 |
| 2606.04060 | Weakly Supervised Incremental Segmentation | Close | CV 分割局部方法。 |
| 2606.04061 | Intra-Modal Graph Rectification | Close | 通用跨模态表征方法，没有大模型系统增量。 |
| 2606.04063 | Joint Architecture/Quantization LLM Compression | Candidate | 联合结构选择与量化，直接面向 LLM 压缩/部署。 |
| 2606.04065 | Spiked Tensor PCA Dynamics | Close | 统计迭代理论。 |
| 2606.04066 | Tau Propagation in Alzheimer’s | Close | 医学垂直任务。 |
| 2606.04067 | Privacy-Conscious LLM Delegation | Candidate | contextual-integrity query rewriting 直接改变 LLM delegation 的数据最小化边界。 |
| 2606.04069 | Membership Privacy for GNNs | Close | GNN 隐私方法，不是大模型主线。 |
| 2606.04073 | Bearing Anomaly Detection | Close | 工业时序垂直任务。 |
| 2606.04074 | Adaptive Patching for Time-Series Forecasting | Close | 通用时序预测，不涉及大模型系统。 |
| 2606.04075 | Large Language Models Hack Rewards, and Society | Candidate | 完整摘要定义 SocioHack 72 环境并观察 LLM post-training reward hacking 的制度外溢。 |
| 2606.04092 | Optimal Transport Flow Matching by Design | Candidate | 完整摘要改变生成模型 prior/coupling 与 few-step inference 机制，可路由多模态生成 owner。 |
| 2606.04095 | Small Models Write Long Stories | Close | 小模型长故事生成局部方法，不满足当前大模型/Infra 门槛。 |
| 2606.04100 | Molecular Dynamics for Interatomic Potentials | Close | 分子模拟 AI-for-Science。 |
| 2606.04106 | PhysicalAI Layer | Close | 完整摘要是 1.99M RF encoder 的跨模态线性探测，规模与问题均不在当前大模型/Infra 主线。 |
| 2606.04107 | Reflection Separation | Close | 单图像分解局部方法。 |
| 2606.04108 | SymTRELLIS | Close | 3D 生成局部结构方法，未给大模型系统机制。 |
| 2606.04109 | Discourse-Role Labels for Context Use | Candidate | 完整摘要用固定内容配对实验揭示 RAG wrapper label 对采用率的巨大影响，改变上下文评测合同。 |
| 2606.04110 | Variance Reduction for Ranking Experiments | Close | 商业指标统计方法，与大模型系统无关。 |
| 2606.04115 | dMX mixed-precision assignment | Candidate | 完整摘要给出 LLM per-layer MXFP bit-width 学习、退火离散与部署预算权衡。 |
| 2606.04118 | Computational History of Scientific Concepts | Close | 历史/计量研究，不是系统机制。 |
| 2606.04120 | SaliMory | Candidate | 标题直接提出 conversational agents 的 cognitive-memory orchestration，进入 Agent memory 边界复核。 |

Batch 01 结果：20 Candidate，30 Close。所有 Candidate 后续需与旧 41 prior 去重并读取 exact-v1/Books owner；Close 只关闭本 family，不外推到同标题关键词。

## Batch 02 — generic incremental closure items 51–100

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04121 | veriFIRE wildfire DNN | Close | 野火检测 DNN 的单一工业验证案例，不是大模型系统。 |
| 2606.04130 | CLAW latent action world model | Candidate | 完整摘要给出 action-free video 自监督 latent action/world-model 联训，并支持规划与 imitation。 |
| 2606.04133 | Pinpoint image geolocation | Close | 图像地理定位局部任务。 |
| 2606.04135 | RAG time-series forecasting | Close | RAG 只是用于时序预测垂直任务，没有大模型系统增量。 |
| 2606.04141 | Credential Exfiltration by LLM Agents | Candidate | 直接研究 Agent 凭证外泄的 pre-output/multi-turn 检测控制点。 |
| 2606.04143 | Flood Prediction | Close | 洪水预测 AI-for-Science/垂直应用。 |
| 2606.04150 | AI Emotional Dependence | Close | 人机交互社会现象研究，不是系统机制。 |
| 2606.04152 | PEEL epistemic scaffolding | Close | 完整摘要是研究实践评论与工具组合，没有可验证的大模型系统实现合同。 |
| 2606.04154 | EpiFormer | Close | 抗原抗体预测垂直任务。 |
| 2606.04155 | SocialCoach | Close | 社交技能辅导应用。 |
| 2606.04160 | Expert-Aware Refusal Steering | Candidate | 直接改变 instruction-tuned LLM refusal steering 的安全控制。 |
| 2606.04161 | edX dropout selector | Close | 教育流失预测诊断，不是大模型系统。 |
| 2606.04164 | ECG OOD fine-tuning | Close | 医疗时序垂直任务。 |
| 2606.04165 | CaloTrilogy | Close | 粒子物理模拟 AI-for-Science。 |
| 2606.04166 | Text Line Detection and Ordering | Close | 文档 OCR 局部模型。 |
| 2606.04167 | Metro Expansion with tabular RL | Close | 城市交通垂直任务，且是 tabular RL。 |
| 2606.04168 | Autoregressive Consistency Hurts Safety | Candidate | 直接定位 autoregressive LLM safety alignment 的 failure mode。 |
| 2606.04171 | MimeLens | Close | 二进制片段类型检测普通系统工具，与大模型无关。 |
| 2606.04176 | Distributional Matrix Completion | Close | 矩阵补全理论。 |
| 2606.04177 | Linguistic Features in AI-Text Detection | Close | 完整摘要只给文本来源分类特征泛化，不改变模型训练/推理/平台合同。 |
| 2606.04180 | KODA | Candidate | 完整摘要比较并对齐 CLIP/SigLIP 多模态 foundation-model 表征，含可扩展 kernel approximation。 |
| 2606.04182 | Exact Unlearning in RL | Close | 完整摘要限定 tabular MDP 的理论算法，不是大模型 unlearning 系统。 |
| 2606.04189 | ACAT annotation platform | Close | 情感分析数据标注平台，缺少大模型生命周期增量。 |
| 2606.04191 | Lorenz Challenge | Close | 科学预测 challenge 方法。 |
| 2606.04194 | Lexical-Dense Conversational-Memory Retrieval | Candidate | 直接解决长会话记忆检索瓶颈，进入 Agent memory/RAG 候选。 |
| 2606.04197 | Topology and Memory of LLM-Agent Consensus | Candidate | 直接研究多 Agent 拓扑/记忆对共识与分裂的机制影响。 |
| 2606.04199 | AI Fake-News Detection | Close | 假新闻检测垂直分类任务。 |
| 2606.04202 | SMAC-Talk | Candidate | 面向 LLM multi-agent coordination 的自然语言环境与评测。 |
| 2606.04205 | DetectZoo | Candidate | 完整摘要提供 61 detectors、22 datasets 与统一可复验 API，形成跨模态检测 release/evaluation contract。 |
| 2606.04209 | Counterfactual Behavior Geometry | Close | 通用解释性理论，不落到大模型系统。 |
| 2606.04210 | Randomized Smoothing for Audio | Close | 音频分类鲁棒性局部方法。 |
| 2606.04212 | Edge of Stability | Close | 通用学习动力学，未给大模型训练系统 owner。 |
| 2606.04223 | Reasoning-Trace Disagreement | Candidate | 完整摘要把多 Agent reasoning traces 抽象为四类 disagreement state 并用于 routing。 |
| 2606.04227 | Incremental Sheaf Cohomology | Close | 数学/数据结构算法，与大模型无关。 |
| 2606.04231 | MM-BizRAG | Candidate | 直接提出 enterprise multimodal RAG 的检索/生成系统方案。 |
| 2606.04236 | Supportive Token Revealing | Candidate | 直接优化 diffusion language-model decoding。 |
| 2606.04238 | Recover-LoRA for 2-bit LMs | Candidate | 面向 2-bit language-model quantization 的低秩恢复与蒸馏。 |
| 2606.04240 | EReL challenge overview | Close | 单一挑战赛综述，没有新系统机制。 |
| 2606.04246 | StepPRM-RTL | Candidate | 完整摘要给出 LLM stepwise trajectory、PRM、RAFT 与 MCTS 的长程 post-training 链，虽应用于 RTL，机制需进入训练 owner 复核。 |
| 2606.04260 | Majority Illusion | Close | 网络现象理论，与大模型无关。 |
| 2606.04264 | UniCanvas | Candidate | 完整摘要提出 diffusion 统一 text-in-image multimodal generation 范式。 |
| 2606.04265 | Mean Field Schrödinger Bridge | Close | 生成建模数学方法，未体现大模型系统增量。 |
| 2606.04266 | Transistor Aging in DNNs | Close | 完整摘要是图像分类 DNN 硬件老化章节与 retraining，未达到大模型/Infra 范围。 |
| 2606.04268 | Parallel LZ77 Decoding | Close | 通用压缩解码算法。 |
| 2606.04273 | Human-AI proof workflows | Close | 初始 HCI 研究，没有 Agent/大模型系统 owner 增量。 |
| 2606.04274 | Task-Specific Transformers vs LLMs | Close | Reddit misinformation 分类垂直比较。 |
| 2606.04275 | Neural RL in Continuous Environments | Close | 通用连续控制 RL。 |
| 2606.04279 | Exchange-Correlation Functionals | Close | 计算化学 AI-for-Science。 |
| 2606.04280 | Contrastive Representation Learning | Close | 通用表征学习理论。 |
| 2606.04284 | Sparse MoE Reward Models | Candidate | 个性化 preference modeling 的 MoE reward-model 结构直接属于大模型 post-training。 |

Batch 02 结果：16 Candidate，34 Close；累计 36 Candidate，64 Close。

## Batch 03 — generic incremental closure items 101–150

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04286 | Text-Based Causal Inference for Reviews | Close | 完整摘要落在学校评论因果分析，属于领域应用。 |
| 2606.04287 | Lightweight Graph Generation | Close | 图生成局部方法，不是大模型系统。 |
| 2606.04290 | Physics-Encoded Hybrid Layers | Close | 复杂物理系统学习，属于 AI-for-Science。 |
| 2606.04291 | Cookbook of 3D Vision | Close | 综述，没有新增机制。 |
| 2606.04298 | Anycast Performance | Close | 通用网络测量，与 AI 系统主线无关。 |
| 2606.04299 | Training-Free Single-Image Diffusion | Close | 完整摘要限定单图 patch 生成，不构成大模型/Infra 增量。 |
| 2606.04300 | Argus-Retriever | Candidate | Vision-LLM late-interaction、region-aware query-conditioned MoE 直接改变多模态检索链。 |
| 2606.04303 | GraftDB | Close | 普通分析数据库并发查询优化，不是 AI 系统贡献。 |
| 2606.04305 | Offline-to-Online Linear Bandits | Close | bandit 理论。 |
| 2606.04307 | Folded Transport MCMC | Close | 统计采样理论。 |
| 2606.04308 | Creative Reading | Close | 阅读支架/HCI，不是系统机制。 |
| 2606.04310 | Latent Anchor DNN Test Generation | Close | 通用 DNN 测试局部方法，未落到大模型。 |
| 2606.04311 | Formal verification of S-two AIR | Close | 标题未显示大模型或 AI 基础设施对象。 |
| 2606.04314 | Bayesian-Guided NN Testing | Close | 通用神经网络测试方法。 |
| 2606.04317 | ParDef parameter-attack defense | Close | 完整摘要只在 ResNet/VGG 小型视觉模型验证，未达到大模型部署主线。 |
| 2606.04319 | PureLight | Close | 计算机图形学照明建模。 |
| 2606.04320 | OpenRFM | Candidate | 完整摘要诊断 relational foundation model 的 ICL 与预训练数据机制，并给 dual-stage architecture。 |
| 2606.04323 | VidLLMs Challenge re-arbitration | Close | 单一挑战赛技巧，未给长期系统增量。 |
| 2606.04324 | Galerkin Flows | Close | Bayesian diffusion 数学方法。 |
| 2606.04325 | Learnable Rank LoRA | Candidate | 完整摘要让 Transformer adapter rank 随层学习，直接改变 PEFT 资源/质量权衡。 |
| 2606.04327 | Two-Layer NN Plateau | Close | 小网络理论。 |
| 2606.04328 | Wireless Prompt Decision Transformers | Close | 无线网络垂直优化。 |
| 2606.04335 | Continuous-Time Robust MDP | Close | RL 理论。 |
| 2606.04338 | Federated Sepsis Prediction | Close | 医疗垂直任务。 |
| 2606.04340 | Noisy Memory Encoding | Close | 认知语言学研究。 |
| 2606.04342 | MSE Forecasting Cost | Close | 通用预测分析。 |
| 2606.04343 | Multi-view Clustering | Close | 通用聚类方法。 |
| 2606.04345 | IoT Object Detection | Close | IoT 视觉垂直系统。 |
| 2606.04349 | MorphoQuant | Candidate | 直接面向 omni-modal LLM 的 modality-aware quantization。 |
| 2606.04350 | Process Mining UCM | Close | 普通过程挖掘。 |
| 2606.04351 | Frames2LoRA | Candidate | 将视频内部化为 VLM LoRA，涉及多模态模型适配与记忆。 |
| 2606.04352 | Fidelity Framework Types | Close | 数学/类型框架，与大模型无关。 |
| 2606.04358 | Room Impulse Responses | Close | 声场重建垂直方法。 |
| 2606.04360 | Agentic Symbolic Regression | Close | 完整摘要把 Agent 用于科学符号回归，机制与评测绑定单一垂直任务。 |
| 2606.04362 | ChatGPT Referral Traffic | Close | 平台增长因果分析，不是 AI 系统机制。 |
| 2606.04364 | Concept Bottleneck Models | Close | 通用视觉可解释模型。 |
| 2606.04366 | PDE Transformers | Close | PDE 求解 AI-for-Science。 |
| 2606.04367 | GlossAssist | Close | 低资源文档语料工具。 |
| 2606.04369 | 3D Anomaly Detection | Close | 工业视觉局部任务。 |
| 2606.04370 | Sound Field Reconstruction | Close | 声场重建垂直方法。 |
| 2606.04373 | MaskAQ | Close | 完整摘要限定 ViT data-free quantization，没有大模型/多模态系统证据。 |
| 2606.04374 | E-commerce Semantic IDs | Close | 电商 relevance 垂直建模。 |
| 2606.04375 | TP-TopK DP-SGD | Close | 完整摘要在 MNIST/CIFAR 验证 coordinate-sparse DP，未建立大模型训练系统边界。 |
| 2606.04378 | Dynamic Logit-Level Gating of LLM Experts | Candidate | 直接提出 LLM expert gating，进入 MoE/路由候选。 |
| 2606.04380 | REGAIN | Close | 标题未显示大模型或基础设施对象。 |
| 2606.04381 | Spatial Reasoning in LLMs | Candidate | 直接改变大模型空间推理的符号到几何表示链。 |
| 2606.04385 | Foundation-Model Alignment | Candidate | 完整摘要用几何保持映射连接 VFM/VLM，形成多模态 foundation-model 兼容机制。 |
| 2606.04387 | LLM Sales Lead Scoring | Close | 销售线索评分垂直应用。 |
| 2606.04388 | TITAN-FedAnil+ | Close | 完整摘要是小型 edge DNN 的区块链联邦学习，不进入当前大模型/Infra 主线。 |
| 2606.04389 | Strategic Counseling | Close | 咨询应用框架。 |

Batch 03 结果：8 Candidate，42 Close；累计 44 Candidate，106 Close。

## Batch 04 — generic incremental closure items 151–200

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04390 | Real-Constrained Neural Networks | Close | 通用网络表达能力理论。 |
| 2606.04391 | Online Skill Learning for Web Agents | Candidate | 直接提出 Web Agent 在线 skill learning 与 state-grounded retrieval。 |
| 2606.04392 | PINN Contaminant Transport | Close | 环境工程 AI-for-Science。 |
| 2606.04396 | Trajectory-Aware RL for Diffusion LMs | Candidate | 直接使用生成轨迹训练 diffusion language models。 |
| 2606.04397 | Context-as-AI-Service | Candidate | 显式暴露 cross-file dependency chain，改变 LLM 生成开发文档的 context service。 |
| 2606.04399 | Differential Privacy in Decentralized Learning | Close | 通用非 IID 去中心化学习，没有大模型系统证据。 |
| 2606.04401 | TANDEM data mixture | Candidate | 完整摘要以 twin networks 优化 LLM 预训练/SFT domain mixture。 |
| 2606.04404 | Knockoffs FDR for DNNs | Close | 通用 DNN 统计解释方法。 |
| 2606.04405 | Low-Rank Decay for Transformers | Candidate | scale-invariant Transformer grokking 的谱机制可进入训练动力学。 |
| 2606.04408 | Latent Factor Model | Close | 通用机器学习方法。 |
| 2606.04409 | Visual Generalization | Close | 视觉模型数据/复杂度比较，未到大模型系统门槛。 |
| 2606.04410 | Neural Video Compression | Close | 视频压缩局部模型。 |
| 2606.04411 | Anonymous Broadcast | Close | 密码学网络协议，与 AI 系统无关。 |
| 2606.04418 | CleanCodec | Candidate | 完整摘要给出语音模型离散 tokenizer 的信息瓶颈与 17x inference 效率增量。 |
| 2606.04419 | Rapid MRI | Close | 医学影像垂直任务。 |
| 2606.04420 | PINNs for PDE Families | Close | PDE AI-for-Science。 |
| 2606.04421 | Trivium causal-memory controllers | Candidate | 完整摘要定义 Agent causal log、probe budget、change-point 与 delayed-identification 边界。 |
| 2606.04423 | Multi-Group Transductive Learning | Close | 学习理论。 |
| 2606.04429 | Multi-Index Generalization | Close | 神经网络理论。 |
| 2606.04432 | DSA video diffusion | Candidate | 完整摘要用 confidence head 动态分配 H100 上视频 diffusion denoising steps。 |
| 2606.04434 | Hyper-ICL | Candidate | multimodal in-context learning 的 attention calibration 机制。 |
| 2606.04435 | CHARM Agentic RAG | Candidate | 直接检测和缓解 Agentic RAG 的 cascading hallucination。 |
| 2606.04436 | 3DThinkVLA | Candidate | VLM/VLA latent 3D prior 与 co-training 机制。 |
| 2606.04437 | Collaborative Perception | Close | 自动驾驶多传感器协同感知垂直任务。 |
| 2606.04438 | LoopMoE | Candidate | 联合 iterative computation 与 MoE language modeling。 |
| 2606.04443 | KEM Decapsulation Tests | Close | 密码协议验证，与 AI 无关。 |
| 2606.04444 | Autonomous-System Sensor Datasets | Close | 自动驾驶数据集扩展，未改变大模型数据系统。 |
| 2606.04445 | Tabular Regression Memory Transformer | Close | 表格回归局部模型。 |
| 2606.04446 | Dual-Diffusion Speculative Decoding | Candidate | 直接改变 speculative decoding draft 架构。 |
| 2606.04448 | Reasoning-Guided Multimodal LLM | Candidate | 直接研究 multimodal LLM 跨短视频/直播表示学习。 |
| 2606.04450 | Construction Safety via LLMs | Close | 建筑安全舆情垂直应用。 |
| 2606.04453 | Lung Cancer Detection | Close | 医疗垂直任务。 |
| 2606.04454 | LLM Reasoning via External Subgraphs | Candidate | 外部子图生成直接介入 LLM stepwise reasoning。 |
| 2606.04455 | Meta-Agent Challenge | Candidate | 评测 Agent 自主开发 Agent 的能力/控制边界。 |
| 2606.04457 | Visual Prompt Engineering | Close | 图像生成提示技巧，未形成持久系统机制。 |
| 2606.04461 | ChannelTok | Candidate | 完整摘要给出 159M flexible-length vision tokenizer、tail dropping 与 decode 效率。 |
| 2606.04463 | OSCAR world model | Candidate | omni-embodiment action-conditioned world model 属于 world-model 主线。 |
| 2606.04465 | SePO | Candidate | 自演进 Agent 直接优化 system prompt，涉及变更与评测闭环。 |
| 2606.04466 | Stage-Specific SFT/RL for SLMs | Close | 完整摘要明确只研究 SLM，当前合同限定大模型/Infra。 |
| 2606.04468 | ParetoPilot | Close | 通用多目标优化。 |
| 2606.04469 | Facial Recognition Calibration | Close | 人脸识别垂直任务。 |
| 2606.04473 | ChessMimic | Close | 国际象棋行为建模。 |
| 2606.04474 | Entity Binding in Speech LLMs | Candidate | 直接诊断 speech LLM reasoning failure 并介入 CoT。 |
| 2606.04475 | Contact-Vibration Sounds | Close | 声学合成案例。 |
| 2606.04476 | Two-Layer ReLU Dynamics | Close | 小网络理论。 |
| 2606.04479 | Visual Text Reasoning Fidelity | Candidate | 完整摘要建立 T2I 模型的 long-text/context/multi-step reasoning 评测边界。 |
| 2606.04480 | Multi-Person Pose Estimation | Close | 视觉姿态局部任务。 |
| 2606.04483 | Vernacular Jailbreaks | Candidate | 直接测 aligned LLM 在语域迁移下的 jailbreak 安全边界。 |
| 2606.04484 | AgentJet | Candidate | 分布式 swarm training 直接服务 Agentic RL。 |
| 2606.04485 | LimiX-2M | Close | 完整摘要是 2M 参数 tabular model，不满足大模型/Infra 范围。 |

Batch 04 结果：23 Candidate，27 Close；累计 67 Candidate，133 Close。

## Batch 05 — generic incremental closure items 201–250

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04486 | Watermarking for Diffusion LMs | Candidate | 直接提出 diffusion language-model watermarking。 |
| 2606.04492 | Episodic Memory for Cooperative MARL | Close | 完整摘要限定 SMAC/GRF 的传统 MARL，不是 LLM Agent memory。 |
| 2606.04493 | SFMambaNet | Close | 视觉 correspondence pruning 局部方法。 |
| 2606.04500 | Biological Data Evaluation | Close | 生物数据自然语言评测垂直工具。 |
| 2606.04503 | Efficient RLVR via Metacognitive Pivots | Candidate | 直接改变 reasoning-model RLVR rollout/样本选择。 |
| 2606.04505 | MechSim | Candidate | 完整摘要给出 LLM Agent 对 simulator assumption/schema/trace 的受限推理合同；作为结构候选而非 AI4Science 内容纳入。 |
| 2606.04507 | Self-Evolving Deep Research | Candidate | joint generation/evaluation 直接构成 deep-research Agent 自演进闭环。 |
| 2606.04511 | SparDA | Candidate | 直接优化 long-context LLM inference attention。 |
| 2606.04513 | MapAgent | Close | 城市地图生成垂直 Agent 应用。 |
| 2606.04514 | LLM Recommendation | Close | 推荐系统垂直应用。 |
| 2606.04516 | Semi-Supervised RLVR | Candidate | 直接研究 reasoning-model RLVR 数据效率。 |
| 2606.04517 | Encrypted Traffic Analysis | Close | 网络流量分类垂直任务。 |
| 2606.04525 | Genomic Model Comparison | Close | 基因模型评测 AI-for-Science。 |
| 2606.04527 | Evolving Memory for Infinite Video | Candidate | 实时无限视频生成的 evolving memory 直接影响长时多模态生成。 |
| 2606.04528 | SAR Few-Shot Learning | Close | 遥感垂直任务。 |
| 2606.04534 | Quadrotor World Models | Close | 四旋翼控制垂直 embodied 方法。 |
| 2606.04535 | Infilling Anchors for Diffusion LMs | Candidate | 直接改变 diffusion LLM 的格式约束生成/解码。 |
| 2606.04536 | Parametric Memory for Self-Evolving Agents | Candidate | 直接研究 Agent scaling 与参数化记忆。 |
| 2606.04547 | TAP-PER | Candidate | 完整摘要以轻量 user-state prefix 替代历史 prompt/per-user adapter，给出 LLM 个性化规模边界。 |
| 2606.04549 | Privilege-Separated VM Integrity | Close | 通用 confidential VM 可执行对象保护，未形成 AI 特有机制。 |
| 2606.04550 | Carbon-Aware E-commerce Ranking | Close | 电商推荐垂直任务。 |
| 2606.04552 | Genomic Tokenization | Close | 基因建模 AI-for-Science。 |
| 2606.04555 | Temporal Order for Agentic Memory | Candidate | segment tree 直接维护长程 Agent memory 的时间顺序。 |
| 2606.04560 | Rollout-Level Replay for GRPO | Candidate | 直接改变 GRPO rollout replay/advantage sampling。 |
| 2606.04562 | Public Policy Agent Models | Close | 政策优化垂直应用。 |
| 2606.04564 | Survival Foundation Models | Close | 生存预测医学/统计垂直模型。 |
| 2606.04570 | Flow-HOA | Close | 完整摘要是麦克风阵列 FIR filter 生成，不是大模型/Infra。 |
| 2606.04576 | Tail Risk Model | Close | 金融风险垂直模型。 |
| 2606.04579 | Sci-PRM | Candidate | 完整摘要给出 tool-aware PRM、Best-of-N 与 RL dense reward/advantage disappearance 机制。 |
| 2606.04580 | Threat Intelligence from Social Media | Close | 威胁情报应用，不是大模型平台安全机制。 |
| 2606.04582 | Temperature Field Reconstruction | Close | 物理场重建 AI-for-Science。 |
| 2606.04583 | HalfNet | Close | 通用随机神经网络方法。 |
| 2606.04584 | Ambisonics Encoding | Close | 音频信号处理局部方法。 |
| 2606.04588 | VCIFBench | Candidate | video foundation-model 复杂指令遵循评测。 |
| 2606.04591 | Multimodal Long-Dialogue Retrieval | Candidate | 直接研究多模态长会话 memory/retrieval。 |
| 2606.04592 | Synthetic Personalities | Close | 完整摘要限定市场研究数字孪生，未改变 LLM 系统合同。 |
| 2606.04593 | 4D Reconstruction | Close | 计算机视觉重建任务。 |
| 2606.04596 | Positional Bias in Multi-Video MLLMs | Candidate | 直接评测 MLLM 多视频上下文位置偏差。 |
| 2606.04597 | Admissible Heuristics | Close | 通用搜索算法。 |
| 2606.04599 | Agentic Industrial Anomaly Detection | Close | DMAIC Agent 绑定工业异常检测单一应用。 |
| 2606.04603 | Distributional ANN | Close | 完整摘要服务传统推荐系统，不涉及大模型/RAG 基础设施。 |
| 2606.04604 | Composed Image Retrieval | Close | 图像检索局部方法。 |
| 2606.04610 | Semantic Histograms | Candidate | 完整摘要给出 LLM/VLM semantic database filter 的 selectivity estimator 与执行次序收益。 |
| 2606.04612 | Hybrid LLM Defence | Candidate | 完整摘要统一 hallucination、prompt injection/jailbreak 与不确定性防御。 |
| 2606.04619 | Normative IR | Close | 完整摘要是通用 technical-standard ASP compliance IR，未绑定大模型/Agent 执行系统。 |
| 2606.04620 | QuBLAST | Candidate | 直接提出 LLM block-level quantization 与 activation scaling。 |
| 2606.04621 | MeshFlow | Close | 3D mesh 生成局部方法。 |
| 2606.04623 | Symplectic Model Reduction | Close | 数学/物理降阶理论。 |
| 2606.04627 | MIRAGE mobile agents | Candidate | 完整摘要把显式 CoT 压入 latent reasoning/world model，并给 token/执行效率边界。 |
| 2606.04634 | Explainably Safe RL | Close | 通用 RL 方法，标题未显示大模型系统对象。 |

Batch 05 结果：20 Candidate，30 Close；累计 87 Candidate，163 Close。

## Batch 06 — generic incremental closure items 251–300

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04641 | NL Queries to Semantic Operator Pipelines | Candidate | 直接把自然语言查询编译为 semantic analytics operator pipeline。 |
| 2606.04645 | CYGNET | Candidate | 完整摘要给出 LLM Agent Cypher 的 pre-execution structural/cost gate、mirror execution 与明确语义边界。 |
| 2606.04646 | QO-Bench | Candidate | 完整摘要用 typed tuples/equijoin 等算子诊断 RAG index-time preservation 与 query-time execution。 |
| 2606.04648 | BiNSGPS | Close | 完整摘要的 MLLM/solver 交互只在几何题求解验证，属于垂直推理任务。 |
| 2606.04650 | LLM Distillation for Conversational Search | Candidate | 直接研究 LLM knowledge distillation 的效率/效果。 |
| 2606.04652 | Matrix Multiplication Low-Bandwidth Model | Close | 算法理论，与 AI 系统无关。 |
| 2606.04657 | Telegram Cybercommunity Discovery | Close | 网络安全情报垂直应用。 |
| 2606.04658 | Climate-Adaptive Urban Layouts | Close | 城市/气候优化垂直应用。 |
| 2606.04661 | CRAFT prompt optimizer | Candidate | 完整摘要把 target-LLM calls 作为稀缺资源，维护 accuracy/token-cost Pareto front。 |
| 2606.04662 | Why Muon Outperforms Adam | Candidate | 大模型训练优化器的曲率机制。 |
| 2606.04665 | Model Selection in Domain Adaptation | Close | 通用 domain adaptation 方法。 |
| 2606.04669 | PQC Implementation SoK | Close | 密码实现综述，与 AI 无关。 |
| 2606.04670 | LipFit GPU package | Close | 通用 GPU 拟合库，不是 AI 基础设施贡献。 |
| 2606.04672 | Dynamic Graph SSM | Close | 图时序表示方法，不是大模型系统。 |
| 2606.04676 | Spatial Indexing Library | Close | 通用空间索引。 |
| 2606.04678 | LARM ASR test-time scaling | Candidate | 完整摘要将 recurrent Transformer depth 变成可控 test-time compute，并给 ASR 证据边界。 |
| 2606.04680 | READ acoustic discrepancy | Candidate | 完整摘要用 autoregressive TTS token likelihood 做 reference-free ASR evaluation/refinement。 |
| 2606.04684 | License Plate Recognition | Close | 交通视觉垂直应用。 |
| 2606.04687 | DAG BFT Consensus | Close | 分布式共识协议，与 AI 无关。 |
| 2606.04688 | Autoregressive Mesh Generation | Close | 3D mesh 局部生成。 |
| 2606.04689 | Scene Graph Generation | Close | 视觉场景图局部任务。 |
| 2606.04691 | SMADE-IE | Candidate | 完整摘要给出 LLM 多 Agent 稀疏路由、evidence-driven debate 与 early stop/token cost。 |
| 2606.04694 | Cross-Lingual Verbalizer | Close | NLP 分类局部方法。 |
| 2606.04695 | Optimal Transport Regret | Close | 数学理论。 |
| 2606.04699 | Alzheimer’s SVM | Close | 医疗垂直任务。 |
| 2606.04703 | Continual Experience for LLM Agents | Candidate | 直接研究 self-evolving LLM Agent 的 experience internalization。 |
| 2606.04704 | Rocq Theorem Search | Close | 定理依赖检索工具，未体现大模型系统机制。 |
| 2606.04706 | AI-Generated Video Detection | Close | 视频来源检测局部任务。 |
| 2606.04708 | VISTA VLA Training | Candidate | physics-validated data adaptation 直接服务 VLA training。 |
| 2606.04710 | Hyperspectral Classification | Close | 遥感垂直任务。 |
| 2606.04716 | Peer Review / GenAI Survey | Close | 软件工程社群调查，不是系统机制。 |
| 2606.04719 | Mamba Multimodal LLM Projector | Candidate | 直接改变 Mamba MLLM 的 cross-modal projector。 |
| 2606.04727 | EviRank | Candidate | LLM-based ranking 的 evidence confidence estimation，进入评测候选。 |
| 2606.04730 | IWSLT Speech Submission | Close | 单一比赛 submission，没有可迁移 release/system delta。 |
| 2606.04733 | Network Telescope Clustering | Close | 网络流量分析任务。 |
| 2606.04735 | Trace-Mediated Bias in Deep RL | Close | 传统 DRL credit assignment，不是大模型系统。 |
| 2606.04736 | Dynamic Precision PINN | Close | PINN AI-for-Science。 |
| 2606.04737 | PILA video generation | Candidate | 完整摘要在 Wan 1.3B/14B 上注入 physics-structured latent/MoE adapter，属于视频大模型生成控制。 |
| 2606.04739 | Vul-RAG Reproducibility | Candidate | 直接复验 open-weight RAG vulnerability detection 的可复现边界。 |
| 2606.04743 | TIDE | Candidate | 完整摘要以 iterative discovery/thought templates 提高 workspace/repo Agent 的多问题覆盖。 |
| 2606.04750 | Affinity RL in Game | Close | 完整摘要限定棋盘游戏传统 MARL。 |
| 2606.04751 | FALSIFYBENCH | Candidate | 直接评测 LLM rule-discovery/inductive reasoning。 |
| 2606.04752 | Multi-Channel Signal Transformers | Close | 信号 Transformer encoder 审计，不是大模型。 |
| 2606.04754 | Neural Mode Connectivity | Close | 网络优化理论。 |
| 2606.04755 | Agentic CMS Operations | Close | 粒子物理实验 Agent 应用，按 AI-for-Science 延后。 |
| 2606.04757 | Decentralized Convex Optimization | Close | 优化理论。 |
| 2606.04772 | Brain Reconstruction | Close | 神经科学垂直任务。 |
| 2606.04775 | LA-LQR video steering | Candidate | 完整摘要把 T2V inference 建模为受控动力系统，给 latent steering 与安全/保真边界。 |
| 2606.04777 | Fair Clustering | Close | 通用聚类方法。 |
| 2606.04779 | Multi-Agent Complementarity Formalization | Close | 完整摘要是一般 HAI 预测聚合理论，未绑定 LLM/Agent runtime。 |

Batch 06 结果：18 Candidate，32 Close；累计 105 Candidate，195 Close。

## Batch 07 — generic incremental closure items 301–350

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04780 | PersonaTree | Candidate | 直接提出 LLM Agent 的 structured lifecycle memory。 |
| 2606.04781 | AIP Agent Skills | Candidate | graph representation 直接用于 Agent skill learning/governance。 |
| 2606.04797 | Continual Diffusion Customization | Candidate | 完整摘要用 AD-LoRA/aggregation 处理 diffusion model 的增量概念与遗忘。 |
| 2606.04798 | On-Device HAR Adaptation | Close | 传感器 HAR 垂直任务。 |
| 2606.04801 | Persistent Homology | Close | 拓扑算法。 |
| 2606.04804 | Physics-Constrained Generation Measure | Close | PDE inverse AI-for-Science。 |
| 2606.04806 | NoRA | Candidate | 完整摘要建立 VLM/Agent visual first-person normative-action benchmark 与 fact-reason-action support graph。 |
| 2606.04807 | BiasGRPO | Candidate | 直接使用 GRPO 稳定高方差奖励下的 bias mitigation。 |
| 2606.04811 | Dream.exe | Candidate | 完整摘要把视频生成模型输出转为 robot execution，以执行成功验证 world-model 物理知识。 |
| 2606.04812 | Safe RL Scenario Generation | Close | 传统风险 RL，没有大模型对象。 |
| 2606.04813 | GraphAlg Playground | Close | 图算法教育平台。 |
| 2606.04815 | Skill-Enhanced Lifelong Agents | Candidate | 直接提出 online lifelong Agent 的 test-time skill co-evolution。 |
| 2606.04816 | LLM Vehicle Routing | Close | LLM 用于车辆路径优化的垂直任务。 |
| 2606.04819 | Proof-of-Useful-Work | Close | 区块链协议研究。 |
| 2606.04820 | OA-CutMix | Close | CV 数据增强局部方法。 |
| 2606.04822 | Thermodynamics Causal Models | Close | 物理理论。 |
| 2606.04823 | R-APS | Candidate | 完整摘要给出 frozen LLM Agent 的 reasoning-mode 隔离、typed critic、stress-test 与可失效长期记忆。 |
| 2606.04825 | HapTile | Candidate | 完整摘要提供语言条件 VLA 所需同步 visuotactile/action trajectory 与可复现收集平台。 |
| 2606.04828 | French MWE Corpus | Close | 语言资源。 |
| 2606.04829 | Motion Mimicking Controller | Close | 机器人控制局部方法。 |
| 2606.04833 | Time-Series Forecasting | Close | 时序预测局部方法。 |
| 2606.04836 | Autism Screening | Close | 医疗垂直任务。 |
| 2606.04838 | Subscriber Retention | Close | 电信业务预测。 |
| 2606.04844 | Audio-Language Drift Scoring | Candidate | 完整摘要直接修正 CLAP 零样本 inference 的噪声漂移，含缓存/每类单内积成本。 |
| 2606.04845 | Stochastic Shortest Path | Close | Bayesian RL/规划理论。 |
| 2606.04847 | MusaCoder | Candidate | 完整摘要给出 CUDA/MUSA kernel 生成的分布式 verifier、execution-feedback RL 与 9B/27B 证据。 |
| 2606.04857 | Robust IMVC | Close | 多视图聚类局部方法。 |
| 2606.04860 | Neural Search Heuristics | Close | 通用组合搜索。 |
| 2606.04863 | Deepfake Face Detection | Close | 人脸 deepfake 检测局部任务。 |
| 2606.04866 | Prior-Guided HPO | Close | 通用超参优化。 |
| 2606.04876 | Text Encoders for TabPFN | Close | 小型表格模型，不是当前大模型主线。 |
| 2606.04877 | Isabelle Abduction Prover | Close | 形式化工具，未显示大模型/Agent 系统贡献。 |
| 2606.04880 | MAOAM | Close | 完整摘要限定 VLM 图像对象/材质选择与分割编辑，不形成通用大模型系统增量。 |
| 2606.04881 | Face Aging | Close | 人脸生成垂直任务。 |
| 2606.04883 | Agentic Theorem-Prover Routing | Candidate | 完整摘要分离 data/control plane，以失败轨迹和成本决定继续/重启，形成 Agent resource-control 机制。 |
| 2606.04889 | GRAIL for RLVR | Candidate | 直接改变 verifiable-reward RL 的 advantage reweighting。 |
| 2606.04891 | Surface Reconstruction | Close | 3D 重建局部方法。 |
| 2606.04892 | Confidential Blockchain | Close | 区块链机密执行协议。 |
| 2606.04896 | Channel Fracture | Candidate | 完整摘要报告生产 multi-agent scheduler/skill/WebSocket silent delivery failures 与 veto verification protocol。 |
| 2606.04899 | TEE Federated Aggregation | Close | 通用联邦学习安全，不是大模型系统。 |
| 2606.04901 | LEO Fingerprinting | Close | 卫星网络攻击检测。 |
| 2606.04906 | AITDNA | Candidate | 完整摘要以完整编辑/AI 交互历史定义 realistic AI-text detection provenance 与公开 benchmark。 |
| 2606.04907 | WAM-Nav | Close | 完整摘要仍绑定视觉导航 policy/轨迹单一 embodied 任务，模型规模与通用 owner 增量不足。 |
| 2606.04909 | E-commerce Taxonomies | Close | 电商搜索垂直应用。 |
| 2606.04911 | BreastGPT | Close | 医疗 MLLM 垂直应用。 |
| 2606.04912 | TEE DAO | Close | 通用 TEE/DAO 协议。 |
| 2606.04915 | Caliper | Candidate | 直接探测 LLM lexical anchor 与 causal structure 的边界。 |
| 2606.04916 | Gig Labour Model | Close | 劳动经济模型。 |
| 2606.04920 | Multi-Domain Quantization | Close | 完整摘要只在小型视觉数据集验证 DNN quantization，不满足大模型/Infra 门槛。 |
| 2606.04921 | Unsupervised Remixing Flow | Close | 音源分离局部模型。 |

Batch 07 结果：16 Candidate，34 Close；累计 121 Candidate，229 Close。

## Batch 08 — generic incremental closure items 351–400

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.04924 | Crowdsourcing in the LLM Era | Close | 社群问卷，没有训练数据系统实现或可迁移机制。 |
| 2606.04925 | Video Panoptic Segmentation | Close | 视觉分割局部方法。 |
| 2606.04928 | LLM Data Attribution | Candidate | 直接提出大模型 bidirectional-gradient training-data attribution。 |
| 2606.04930 | AdaKoop | Close | 动力系统流式建模，不是大模型系统。 |
| 2606.04931 | Mean-Based Algorithms | Close | 在线学习理论。 |
| 2606.04934 | Certifying Parity | Close | 复杂度理论。 |
| 2606.04935 | Active Inference | Close | 认知/哲学理论。 |
| 2606.04939 | Unified Audio-Text Diffusion | Candidate | 统一音频生成、编辑与 captioning 的 multimodal diffusion 模型。 |
| 2606.04943 | Biphonic Singing | Close | 歌声合成局部任务。 |
| 2606.04944 | CTR Prediction | Close | 广告推荐垂直模型。 |
| 2606.04945 | STaR-Quant | Candidate | 直接面向 diffusion LLM 的 state/time-consistent PTQ。 |
| 2606.04946 | Submodular Maximization | Close | 优化理论。 |
| 2606.04952 | Diabetes EHR Software | Close | 医疗应用。 |
| 2606.04957 | NLLog | Close | 完整摘要是 deterministic rewrite + tree ensemble 的普通日志异常检测，不是大模型基础设施。 |
| 2606.04964 | SemBlock | Candidate | 直接改变 diffusion LLM 的 semantic-boundary dynamic blocks。 |
| 2606.04967 | AI Software-Agent Framework Taxonomy | Candidate | 完整摘要给出 specification/context/roles/execution/validation/portability 六维可复验过程 taxonomy。 |
| 2606.04968 | ForesightFlow | Candidate | 完整摘要给出 VLA action/potential decoupled flow matching、best-of-K 与 compute/幻觉边界。 |
| 2606.04971 | Fairness Constraints for MLE Agents | Candidate | 完整摘要建立 MLE Agent responsibility gap 与 fairness-guided pipeline 验收证据。 |
| 2606.04974 | SAID diffusion LM decoding | Candidate | scaffold-aware iterative decoding 直接优化 diffusion LM inference。 |
| 2606.04978 | LLM Risk Decisions | Candidate | 完整摘要区分 outcome resemblance 与 mechanism alignment，改变高风险 LLM 评测合同。 |
| 2606.04980 | AlphaQ | Candidate | calibration-free MoE bit allocation 直接服务量化推理。 |
| 2606.04986 | Food-R1 | Close | 食物 VLM 垂直模型。 |
| 2606.04987 | Chess Dialogue Dataset | Close | 国际象棋推理数据集。 |
| 2606.04990 | Agent Provenance Survey | Candidate | 完整摘要给出 execution provenance typed graph 与 evidence projection taxonomy，作为 Existing/结构评估候选。 |
| 2606.04992 | Surgical AR Guidance | Close | 手术垂直系统。 |
| 2606.04993 | Code Lifespan Analysis | Close | 普通软件仓库分析。 |
| 2606.05000 | AI-Driven O-RAN Demo | Close | 通信节能 demo，不是大模型基础设施。 |
| 2606.05008 | M3Eval | Candidate | 完整摘要系统评测多模态大模型的并行视频、干扰、来源与符号 memory。 |
| 2606.05009 | DAR | Candidate | 完整摘要比较 LLM 对长规则集按需交互的多种 agentic harness，并揭示弱模型 token/质量退化。 |
| 2606.05012 | O-RAN Orchestration | Close | 通信网络管理协议。 |
| 2606.05014 | Depth-Attention | Candidate | cross-layer value mixing 直接改变 language-model architecture。 |
| 2606.05015 | Quadrotor World Models | Close | 四旋翼导航垂直 world-model 任务。 |
| 2606.05016 | LoRA Merging Probe Gating | Candidate | task/domain calibrated gating 直接改变 LoRA merge。 |
| 2606.05017 | GoldenFloat | Close | 完整摘要提供通用 RTL float artefacts，但没有大模型使用/收益证据，不能进入当前 Infra 分母。 |
| 2606.05018 | Handwriting Extraction | Close | 文档历史分析。 |
| 2606.05019 | Cell On/Off Switching | Close | 无线接入网络节能。 |
| 2606.05021 | MADDPG | Close | 传统 MARL 方法。 |
| 2606.05025 | Invariant Gradient Alignment | Candidate | 完整摘要用 logical-isomer gradient mask/SVD-LoRA 改善 LLM reasoning distillation OOD。 |
| 2606.05030 | Bidirectional Logic for Chain Repair | Candidate | 直接介入 LLM chain-of-thought repair。 |
| 2606.05031 | MetaPoint | Candidate | 完整摘要用单 token 坐标与 planner primitives 提供生成模型精确空间控制。 |
| 2606.05035 | Streaming 3D Reconstruction | Close | 3D mapping 局部任务。 |
| 2606.05040 | SearchLog Extension | Close | HCI 研究工具。 |
| 2606.05042 | In-Context Graphical Inference | Close | 完整摘要是图模型 marginal inference，不是 language-model ICL。 |
| 2606.05045 | Control-Affine Models | Close | 控制理论。 |
| 2606.05046 | Graph Cascades | Close | 图机器学习方法。 |
| 2606.05050 | Catalyst Discovery Agent | Close | 催化剂发现 AI-for-Science。 |
| 2606.05054 | Ranking-Improved Self-Consistency | Candidate | 完整摘要用轻量 ranker 组合频率/语义/trace 信号，改变 LLM test-time answer selection。 |
| 2606.05067 | Graph Generation | Close | 图生成局部方法。 |
| 2606.05068 | Image Super-Resolution | Close | 视觉局部任务。 |
| 2606.05071 | Image Retouching | Close | 图像编辑局部任务。 |

Batch 08 结果：19 Candidate，31 Close；累计 140 Candidate，260 Close。

## Batch 09 — generic incremental closure items 401–435

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.05073 | Meaningful Missingness Diffusion | Close | 通用缺失值插补。 |
| 2606.05076 | Network Intent Drift | Close | 普通网络 intent/traffic 分析，不是 AI 系统。 |
| 2606.05078 | Ciphertext Decipherment | Close | 密码文本识别局部任务。 |
| 2606.05079 | Function Vectors | Candidate | 完整摘要研究 LLM ICL function-vector 的 head selection/steering 定义与效率。 |
| 2606.05080 | AutoLab | Candidate | 直接评测 frontier models 的长程自动研究/工程任务。 |
| 2606.05081 | BFS on Tensor Cores | Close | 通用 GPU 图算法。 |
| 2606.05085 | Paper Title Generation | Close | 标题生成垂直应用。 |
| 2606.05087 | Phraseology Probe | Close | 局部语言能力数据集，未形成系统增量。 |
| 2606.05090 | Trust Fraud Detection | Close | 评分网络欺诈统计方法。 |
| 2606.05094 | Remote Memory Channels | Close | 通用 HPC 通信机制，未给 AI workload 证据。 |
| 2606.05101 | FoeGlass | Candidate | 完整摘要用 LLM ICL 做黑盒 audio-deepfake detector red teaming，给覆盖/迁移/加固闭环。 |
| 2606.05102 | Gaussian Splat Compression | Close | 3D 表示压缩。 |
| 2606.05103 | Roman Gem Identification | Close | 考古垂直应用。 |
| 2606.05106 | Arithmetic Pedagogy for LMs | Close | 完整摘要只训练 86M GPT-2，小模型教学案例不满足当前范围。 |
| 2606.05109 | RePercENT | Candidate | 完整摘要在 foundation-model embeddings 上做可扩展多模态 disentanglement，无需联合预训练。 |
| 2606.05115 | Child Egocentric Continual Learning | Close | 儿童视角视觉/语言学习研究，未给大模型系统证据。 |
| 2606.05116 | Graph Set Transformer | Close | 图模型结构。 |
| 2606.05121 | Audio Interaction Model | Candidate | 完整摘要定义 always-on perceive-decide-respond、异步 FIFO inference 与 302k-hour corpus。 |
| 2606.05124 | Gaussian Splatting | Close | 3D reconstruction 局部方法。 |
| 2606.05126 | Passive Liveness Detection | Close | 传感器身份检测。 |
| 2606.05129 | FHE Causal Structure Learning | Close | 通用隐私学习。 |
| 2606.05130 | LLM Mobility Prediction Agent | Close | 交通移动预测垂直应用。 |
| 2606.05131 | Koopman Learning | Close | 动力系统 AI-for-Science。 |
| 2606.05134 | Activation-Based Active Learning for ICL | Candidate | 完整摘要在 Llama/Qwen 上给出 activation selection 的负结果与适用边界。 |
| 2606.05138 | Financial Time Series | Close | 金融生成垂直任务。 |
| 2606.05142 | Multi-View Editing | Close | 3D 编辑局部方法。 |
| 2606.05145 | Failed Reasoning Traces | Candidate | 完整摘要把失败 rollout 的 recoverability 特征用于 test-time intervention routing。 |
| 2606.05149 | Vehicle Classification | Close | 视觉分类应用。 |
| 2606.05150 | RBF Network | Close | 通用小网络方法。 |
| 2606.05152 | Distributional DAgger | Candidate | 完整摘要用 rich feedback 与 forward cross-entropy 改善 reasoning-model RLVR，并给单调改进/regret 边界。 |
| 2606.05158 | Streaming Multi-Agent Reasoning | Candidate | 直接以 token/step streaming 降低多 Agent pipeline latency 并改变错误传播。 |
| 2606.05160 | Humanoid Loco-Manipulation | Close | 机器人操作垂直系统。 |
| 2606.05161 | Audio-Language Arbitration | Candidate | 直接诊断并修复 ALM 中音频证据被冲突文本覆盖的 inference arbitration。 |
| 2606.05162 | Dynamic 3D Shape Generation | Close | 3D 生成局部任务。 |
| 2606.05165 | STRIDE | Candidate | 直接以 activation-space sparse recovery 做 LLM training-data attribution，给 13x 成本证据。 |

Batch 09 结果：11 Candidate，24 Close；generic incremental 435 项全量完成，合计 151 Candidate、284 Close。

## Other closure strata — 99 items

逐项复读 title；以下二十项的原关闭理由与题摘冲突，恢复为 Candidate：

- embodied 组：2606.04226（PerceptTwin）。
- benchmark 组：2606.04098、2606.04126、2606.04184、2606.04244、2606.04282、2606.04442、2606.04460、2606.04545、2606.04660、2606.04701、2606.04773、2606.04867、2606.04874、2606.04970。
- theory 组：2606.04717（CoT source-control certificate）。
- vertical 组：2606.04394（composed-policy alignment）、2606.04433（stateful VLM encoder）、2606.04602（self-evolving legal Agent）、2606.05001（commit-driven SWE-Agent benchmark）。

其中边界项已读完整摘要：PerceptTwin 提供自动语义场景 simulation 与 LLM plan verification；HighTide 提供 Agent skills、decision log、Bazel/RTL-to-GDS release contract；VAMPS/FindIt/MemoryDoc/CyberGym/LivingScreen/APB 等都新增可复验的大模型/Agent 能力轴；Parthenon 虽在法律域验证，但 anti-leakage failure-to-skill/tool/knowledge loop 是 task-agnostic；TeleSWEBench 虽在电信仓验证，但 commit/unit-test/LLM-judge 组合直接评测 SWE Agents。

其余 79 项 Close：28 项 embodied 中除 PerceptTwin 外均绑定车辆、无人机、机器人、SLAM、定位或传统 MARL 单一控制任务；22 项 benchmark 中八项分别绑定机器人、图书主题、地下探索、生物/CAD/列车等垂直问题；4 项 theory 中 approximate MDL、Noah’s Ark index 与 noisy-transformer free-energy 理论未给可落实的大模型系统合同；45 项 vertical 中除上列四项外均绑定医疗、生物、交通、金融、教育或小型视觉任务。每项原 checkpoint 已保存题摘首句与具体对象，本轮逐题确认后保留其 family-local closure，不把类别标签外推为规则。

## Prior frontier — 41 items

逐项复读旧 41 项题目，对六个边界项补读完整摘要：

- 继续 Candidate：2606.04196（Iceberg/Puffin snapshot 原子绑定与 RAG ANN）；2606.04233（benchmark shortcut/significance/overfitting/data-source diagnostics）；2606.04522（RAG ANN 质量指标）；2606.04908（GPU-native remote AFA/I/O path）。
- Close：2606.04384（DPSR-CG 只在 MNIST/CIFAR/IMDB 验证，未建立大模型隐私训练合同）；2606.04850（通用 neural-processor/fabrication co-design，未提供大模型 workload 证据）。

其余 35 项题目直接落在 LLM/Agent、MoE、KV cache、RLHF、RAG、MCP、GPU inference 或 foundation-model evaluation，维持 Candidate，但不继承旧 Books disposition。

## Frozen denominator

- raw identities：575
- Candidate：210 = prior 39 + generic incremental 恢复 151 + 其他 strata 恢复 20
- Close：365 = prior false-positive 2 + generic incremental 284 + 其他 strata 79
- 旧 534 closure proposals 的 false-negative 为 171/534（32.0%）；旧 41 prior 的 false-positive 为 2/41（4.9%）。

该分母只冻结题摘准入。旧 39 项 exact-v1 可在 identity/claim 不变时复用；171 项新恢复 Candidate 尚需 score、owner route 与 Evidence Gate，不能据 denominator 直接推 Books。

## Strict pass — authoritative denominator override

上面的 `210 / 365` 是首轮恢复审计，不是当前合同的最终分母：该轮仍把“对象是 LLM/VLM/VLA/Agent、或能映射到既有章节”误当成贡献准入。这里重新以完整摘要回答一个更窄的问题：材料是否给出可迁移、可长期复用的 design delta，且明确改变 state/data/control ownership、execution/evaluation/release contract、系统级机制取舍，或能修正 Books 的既有结论。若摘要只给出局部模型、表示、adapter、benchmark、单一任务性能、新架构名或新生成方法，即使对象是大模型，也在 pre-denominator 关闭。本节覆盖并取代上面的首轮 `Candidate` 标签；上文只作为错误恢复过程的审计轨迹保留。

### Strict-retained — 73 families

下列 73 项在 title 边界不清时均已补读完整摘要，并能指出合同级增量；旧 disposition 仍不继承。

| 机制族 | ID | 严格准入依据 |
| --- | --- | --- |
| 既有 prior：runtime、训练/推理 data plane、Agent state/control、安全与评测合同 | 2606.04017、2606.04056、2606.04071、2606.04101、2606.04104、2606.04145、2606.04193、2606.04196、2606.04233、2606.04261、2606.04296、2606.04302、2606.04306、2606.04315、2606.04321、2606.04329、2606.04402、2606.04415、2606.04425、2606.04459、2606.04522、2606.04557、2606.04581、2606.04594、2606.04628、2606.04769、2606.04799、2606.04903、2606.04908、2606.04923、2606.04929、2606.05004、2606.05029、2606.05037、2606.05043 | 分别落在长程 Agent 接口、token budget、隐蔽影响、MoE 负载均衡、proof/receipt、安全停止、snapshot-bound ANN、评测有效性、数据策展、干预时机、KV/RAG、执行边界、memory runtime、PD 调度、推理诊断、MCP/trace、GPU I/O、reward-hacking、post-training poisoning、隐私推理与交互协议等长期 owner；摘要给出可复验的运行或验收边界。 |
| 新恢复：系统 state/data/control 与执行合同 | 2606.04028、2606.04037、2606.04067、2606.04141、2606.04391、2606.04397、2606.04421、2606.04435、2606.04484、2606.04536、2606.04555、2606.04610、2606.04641、2606.04645、2606.04703、2606.04780、2606.04781、2606.04815、2606.04847、2606.04883、2606.04896、2606.05121、2606.05158 | 分别新增数值执行标准、deployment assurance、上下文转发责任、跨轮泄漏预算、skill/memory 更新、context service、causal log、stage-verification、分布式 Agent 训练、显式/参数记忆、在线时序索引、semantic query planning、pre-execution gate、experience internalization、skill graph、GPU-kernel verifier、control/data plane、消息交付 veto、always-on FIFO 与多 Agent streaming 等可迁移机制。 |
| 新恢复：evaluation/release contract 或既有结论修正 | 2606.04109、2606.04455、2606.04507、2606.04646、2606.04739、2606.05080、2606.05145 | 分别把 discourse role、受限 sandbox、防 reward-hacking、typed-event operator preservation、复现失败、wall-clock 长程任务与失败轨迹 recoverability 变成可复验的评测/发布边界；2606.04739 直接修正既有 RAG 安全效果声明。 |
| 其他 closure strata 中恢复 | 2606.04394、2606.04442、2606.04460、2606.04660、2606.04701、2606.04717、2606.04874、2606.04970 | 仅保留能跨任务定义 composed-policy、conversation+document memory、端到端发现/PoC/修复、lifelong session state、GUI observation-control、带 Type-I 保证的 source-control certificate、broken-tool planning 与 proactive recovery 的八项合同；不因“benchmark”名称自动准入。 |

### First-pass demotions — 137 families

首轮 210 个 `Candidate` 中有 137 项在严格门槛下撤回。下面每个 ID 只出现一次；分组理由描述该 family 摘要实际缺少的合同，而不是用关键词批量关闭。

| 撤回族 | ID | 具体 closure reason |
| --- | --- | --- |
| 局部模型、表示、adapter、量化或 decoding 机制（50） | 2606.04027、2606.04032、2606.04048、2606.04050、2606.04058、2606.04063、2606.04092、2606.04115、2606.04130、2606.04238、2606.04284、2606.04325、2606.04349、2606.04378、2606.04396、2606.04401、2606.04405、2606.04432、2606.04438、2606.04446、2606.04461、2606.04463、2606.04486、2606.04511、2606.04527、2606.04535、2606.04620、2606.04627、2606.04650、2606.04662、2606.04678、2606.04719、2606.04737、2606.04775、2606.04797、2606.04844、2606.04928、2606.04939、2606.04945、2606.04964、2606.04968、2606.04974、2606.04980、2606.05014、2606.05016、2606.05025、2606.05031、2606.05079、2606.05109、2606.05165 | 摘要只改变网络 block、latent/embedding、LoRA/adapter、训练权重、量化位宽或某一 decoding/生成算法；没有把机制落实为跨 workload 的 state/data/control ownership、runtime interface、release gate 或系统级资源合同。 |
| 单一 workload、垂直 benchmark/应用或局部能力诊断（40） | 2606.04023、2606.04046、2606.04051、2606.04057、2606.04180、2606.04205、2606.04231、2606.04246、2606.04264、2606.04300、2606.04320、2606.04351、2606.04381、2606.04418、2606.04434、2606.04436、2606.04448、2606.04454、2606.04474、2606.04479、2606.04505、2606.04579、2606.04588、2606.04591、2606.04596、2606.04680、2606.04708、2606.04727、2606.04743、2606.04751、2606.04806、2606.04811、2606.04823、2606.04825、2606.04906、2606.05008、2606.05009、2606.05101、2606.05134、2606.05161 | 摘要的增量止于代码生成、scene divergence、知识编辑、检测、RTL、单一生成模型、机器人/VLA、语音、视频、多模态或某个 reasoning benchmark；未证明这些能力轴会改变通用系统的执行、评测或发布合同。 |
| 局部训练、alignment/safety probe、prompt/trace 技巧或描述性 taxonomy（31） | 2606.04035、2606.04036、2606.04075、2606.04120、2606.04160、2606.04168、2606.04194、2606.04197、2606.04202、2606.04223、2606.04236、2606.04385、2606.04465、2606.04483、2606.04503、2606.04516、2606.04547、2606.04560、2606.04612、2606.04661、2606.04691、2606.04807、2606.04889、2606.04915、2606.04967、2606.04971、2606.04978、2606.04990、2606.05030、2606.05054、2606.05152 | 摘要报告一种 reward/gradient/prompt/trace/steering 改善、风险现象或分类框架，但没有给出新的长期 owner、系统组件、跨阶段控制点或可执行的验收/发布协议。 |
| 其他 strata 首轮恢复后撤回（12） | 2606.04098、2606.04126、2606.04184、2606.04226、2606.04244、2606.04282、2606.04433、2606.04545、2606.04602、2606.04773、2606.04867、2606.05001 | Search-grounded misinformation、VLSI、social-emergence、robot plan verification、数学/视觉定位、stateful VLM encoder、AIGC 定位、legal Agent、motion、companion safety 与 telecom SWE 的贡献仍由各自任务域定义；摘要未证明跨 workload 的系统契约变化。 |
| 既有 prior 在严格复审中撤回（4） | 2606.04272、2606.04413、2606.04778、2606.05122 | 分别是中途 pretraining RL 实验、helpful-only finetuning、generation-trajectory safety 注入与 self-evaluation elicitation；都有大模型对象，但增量仍是局部训练/推断方法，没有独立系统 owner 或 release contract。原首轮已关闭的 2606.04384、2606.04850 继续 Close。 |

### Fresh-context FP/FN sample

严格重冻后重新遮蔽首轮标签，抽查 10 个 retain 与 10 个 close：

- retain：2606.04028（数值语义标准）、2606.04037（部署前 assurance）、2606.04141（跨轮泄漏预算）、2606.04484（解耦式分布 Agent 训练）、2606.04641（semantic operator compiler）、2606.04645（pre-execution gate）、2606.04896（消息交付 veto）、2606.05029（foundation-model validity contract）、2606.05121（always-on FIFO runtime）、2606.05158（跨 Agent step streaming）。十项都能在完整摘要中定位到长期状态、控制或评测合同，不是由对象名称推断。
- close：2606.04046（SceneDiver）、2606.04180（KODA）、2606.04205（DetectZoo）、2606.04246（StepPRM-RTL）、2606.04264（UniCanvas）、2606.04320（OpenRFM）、2606.04351（Frames2LoRA）、2606.04432（video diffusion step allocation）、2606.04434（Hyper-ICL）、2606.04436（3DThinkVLA）。十项的完整摘要都只证明单一任务、局部表示/adapter 或生成/推理方法收益，未给跨 workload 的系统契约。

抽样未发现新的 false-positive / false-negative；这只是同一恢复任务中的 fresh-context 自检，不替代主任务的非作者独立复核。

## Author-side strict checkpoint（已被独立复核覆盖）

- raw identities：575
- Candidate：73 = prior 35 + generic incremental 30 + 其他 strata 8
- Close：502 = 原首轮 Close 365 + 严格撤回 137
- 对旧 534 closure proposals：严格恢复 38 项，而不是首轮的 171 项；对旧 41 prior：严格关闭 6 项。

这组 `73 / 502` 仅保留为作者侧 checkpoint；最终独立 authority 是 `64 / 511`。后续 score、owner route、Evidence 与 Books Decision 必须使用 64 项最终 Candidate 集合。

## Final independent denominator and Books disposition

- raw identities：575。
- Candidate：64。
- Close：511。
- 相对作者侧 checkpoint：9 项 de-admit（含 1 项 withdrawal），0 项 restore。
- Books disposition：54 项已有覆盖、9 项仅报告、1 项已整合。EvalStop 已写入 Ch31“训练停止不能只看 Training Loss 或 Reward Model Score”，并通过非作者 post-write audit；2606.04701 已由 Ch66 的 Evidence Acquisition Policy 与 Living-world Evaluation/Run Identity 覆盖。UltraEP Books residue 为 0；Covert Influence 的旧 adoption trace 已清除；当前 blocker 为 0。
