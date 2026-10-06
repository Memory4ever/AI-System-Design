# 2025-11-08 有限普通筛选尾批

作者Noether。本文件记录本日窄主题原响应中实际读完完整题摘的新增83个身份，不是全月/全类候选表。完整summary保留在[formation](./arxiv-formation-narrow-page0.xml)、[runtime](./arxiv-runtime-agent-page0.xml)、[multimodal](./arxiv-multimodal-page0.xml)、[25个exact-v1](./arxiv-exact-v1-tail.xml)、[8个exact-v1](./arxiv-exact-v1-final8.xml)、[有界邻接六项v1](./arxiv-neighbor-six-v1.xml)。部分v1题名与当前稿不同，明确保持v1；只有范围关闭的Euler用实际当前v3题摘，不采用旧事件。

“潜在”均不是当窗确定候选，不授Evidence/Books。摘要已足以确定的具体局部/负侧方向不会因实验未披露关闭；日期尚未落窗，不展开全部附件。也不凭owner没有论文/算法名制造长期缺口。共同日期恢复槽及官方失败/修正见[SOURCE_EXECUTION](./SOURCE_EXECUTION.md)；每项可接受重开为该精确稿真正官方公告或首次公开上下界完全落窗，先公开者仅有本窗实质差额才恢复。不以submittedDate/API published、ID顺序或常规schedule补造时刻。

| 原始身份 / 完整标题 | 完整题摘后的有限裁决及采用边界 |
| --- | --- |
| [2511.03844v1 / ASAP: an Agentic Solution to Auto-optimize Performance of Large-Scale LLM Training](https://arxiv.org/abs/2511.03844v1) | 潜在：实际profile/roofline与历史实验支撑sharding建议，需区分推荐、人工调参和搜索成本，不因三Agent架构准入。 |
| [2511.03845v1 / To See or To Read: User Behavior Reasoning in Multimodal LLMs](https://arxiv.org/abs/2511.03845v1) | 潜在局部评价：等价交易文本/图示表示改变下一购买预测，新增输入表示条件；87.5%不外推一般多模态优势。 |
| [2511.03878v1 / KnowThyself: An Agentic Assistant for LLM Interpretability](https://arxiv.org/abs/2511.03878v1) | 关闭：解释性工具查询/路由与聊天界面集成，未新增解释性机制或其有效性条件；工具可访问性本身不等于模型可解释。 |
| [2511.03925v1 / Collaborative Agents for Automated Program Repair in Ruby](https://arxiv.org/abs/2511.03925v1) | 潜在局部证据：Ruby修复的测试反馈/反思迭代与消融，保留语言和五轮预算条件，不以TDD成熟单独关闭。 |
| [2511.03934v1 / PEFA-AI: Advancing Open-source LLMs for RTL generation using Progressive Error Feedback Agentic-AI](https://arxiv.org/abs/2511.03934v1) | 潜在：RTL逐步复杂度/错误反馈策略与编译、功能、综合验证的质量成本差额；不是RTL应用得分就准入。 |
| [2511.03985v1 / ArchPilot: A Proxy-Guided Multi-Agent Approach for Machine Learning Engineering](https://arxiv.org/abs/2511.03985v1) | 潜在：低保真proxy与fidelity-aware MCTS、restart memory改变架构搜索预算，需核代理与最终训练收益可归因性。 |
| [2511.03995v1 / Hybrid Fuzzing with LLM-Guided Input Mutation and Semantic Feedback](https://arxiv.org/abs/2511.03995v1) | 潜在：semantic feedback扩展覆盖率单一搜索导向的盲点，需核实际可达状态与LLM反馈成本，不采全部漏洞发现保证。 |
| [2511.04002v1 / Memory- and Latency-Constrained Inference of Large Language Models via Adaptive Split Computing](https://arxiv.org/abs/2511.04002v1) | 潜在：split threshold、token自适应bit量化与KV/sequence联合资源约束改变端侧分工；非无条件1.49x保证。 |
| [2511.04020v1 / Abductive Inference in Retrieval-Augmented Language Models: Generating and Validating Missing Premises](https://arxiv.org/abs/2511.04020v1) | 潜在：检索缺前提时生成并以consistency/plausibility验证，决定准入的验证独立性仍需定点；不能因组合成熟直接关闭。 |
| [2511.04032v1 / Detecting Silent Failures in Multi-Agentic AI Trajectories](https://arxiv.org/abs/2511.04032v1) | 潜在局部负侧：无显式error的协作漂移/循环失效与4275+894轨迹检测；分类准确率不自动证明因果诊断或修复。 |
| [2511.04036v1 / PICNIC: Silicon Photonic Interconnected Chiplets with Computational Network and In-memory Computing for LLM Inference Acceleration](https://arxiv.org/abs/2511.04036v1) | 潜在：photonic chiplet间计算通信网络及映射机制；模拟结果不得转述硬件实测/H100真实服务。 |
| [2511.04042v1 / An LLM-based Framework for Human-Swarm Teaming Cognition in Disaster Search and Rescue](https://arxiv.org/abs/2511.04042v1) | 关闭：搜救场景多模态意图分解/反馈接既有swarm控制，摘要仅应用任务效率/负荷提升，未披露新冲突仲裁或系统可靠性条件。 |
| [2511.04072v1 / Plan of Knowledge: Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering](https://arxiv.org/abs/2511.04072v1) | 潜在：时间约束与语义约束共同驱动contrastive temporal retrieval/问题分解，需核实际检索边界，不泛化56%任务得分。 |
| [2511.04090v1 / Advancing Equitable AI: Evaluating Cultural Expressiveness in LLMs for Latin American Contexts](https://arxiv.org/abs/2511.04090v1) | 潜在局部评价：文化expressiveness测量与sentiment误配；新增指标是否真正改变评价盲区待必要核，不以拉美数据量准入。 |
| [2511.04153v1 / BAPPA: Benchmarking Agents, Plans, and Pipelines for Automated Text-to-SQL Generation](https://arxiv.org/abs/2511.04153v1) | 潜在局部对照：SQL讨论轮次、小大模型/不同planner三pipeline的预算收益边界；不把多agent组合自动当新机制。 |
| [2511.04179v1 / Explaining Software Vulnerabilities with Large Language Models](https://arxiv.org/abs/2511.04179v1) | 关闭：IDE内SAST警告解释/修复界面的用户易用性研究，未新增LLM安全控制、学习机制或模型评价盲区。 |
| [2511.04184v1 / Trustworthy LLM-Mediated Communication: Evaluating Information Fidelity in LLM as a Communicator (LAAC) Framework in Multiple Application Domains](https://arxiv.org/abs/2511.04184v1) | 潜在评价：重复传递的信息fidelity/recapture/source conflation，区分文本可读与信息保真；不凭LAAC命名建立新owner。 |
| [2511.04053v1 / Interpreting Multi-Attribute Confounding through Numerical Attributes in Large Language Models](https://arxiv.org/abs/2511.04053v1) | 潜在表示反侧：数值共享subspace/相关性被无关context放大并移动判断，限所测模型任务，不声称一般因果。 |
| [2511.03866v1 / OMPILOT: Harnessing Transformer Models for Auto Parallelization to Shared Memory Computing Paradigms](https://arxiv.org/abs/2511.03866v1) | 潜在：function-level OpenMP训练目标与OMPBLEU正确性代理；不能把代码相似性自动当并行语义正确。 |
| [2511.04093v1 / KGFR: A Foundation Retriever for Generalized Knowledge Graph Question Answering](https://arxiv.org/abs/2511.04093v1) | 潜在：高degree剪枝与非对称progressive propagation、LLM node/edge/path接口改变未见KG检索负担。 |
| [2511.04087v1 / E-CARE: An Efficient LLM-based Commonsense-Augmented Framework for E-Commerce](https://arxiv.org/abs/2511.04087v1) | 潜在：offline factor graph commonsense准备后单次LLM forward/query的摊销边界；电商任务指标不等于一般服务收益。 |
| [2511.04070v1 / T-FIX: Text-Based Explanations with Features Interpretable to eXperts](https://arxiv.org/abs/2511.04070v1) | 潜在局部评价：专家alignment与解释plausibility/faithfulness七知识域指标差额；不把解释动听当真实忠实度。 |
| [2511.04120v1 / RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning](https://arxiv.org/abs/2511.04120v1) | 潜在评价：IRT difficulty奖励约束题目改写，26模型accuracy drop并非所有题更有效，well-posed/no-leak控制待核。 |
| [2511.04260v1 / Proto-LeakNet: Towards Signal-Leak Aware Attribution in Synthetic Human Face Imagery](https://arxiv.org/abs/2511.04260v1) | 潜在：重模拟forward diffusion的latent特征与prototype/open-set识别，关心生成来源可辨识边界，不将取证应用分数当普遍归因。 |
| [2511.04715v1 / First is Not Really Better Than Last: Evaluating Layer Choice and Aggregation Strategies in Language Model Data Influence Estimation](https://arxiv.org/abs/2511.04715v1) | 潜在负侧：data influence中层估计不稳定、layer聚合rank/vote/NDR改善，不采单层最好或无retraining成本万能。 |
| [2511.04647v1 / Optimal Inference Schedules for Masked Diffusion Models](https://arxiv.org/abs/2511.04647v1) | 潜在理论：MDM调度的expected divergence、未知prior下最优不可达与相关性假设；不机械索取LLM实测。 |
| [2511.03928v1 / SynQuE: Estimating Synthetic Dataset Quality Without Annotations](https://arxiv.org/abs/2511.03928v1) | 潜在：真实未标注数据支撑synthetic corpus质量选择proxy，LENS的LLM解释不天然证明proxy有效。 |
| [2511.04256v1 / SSPO: Subsentence-level Policy Optimization](https://arxiv.org/abs/2511.04256v1) | 潜在GRPO差额：sentence级importance ratio/entropy clipping连接token/sequence粒度，具体更新偏差/质量预算待核。 |
| [2511.04570v1 / Thinking with Video: Video Generation as a Promising Multimodal Reasoning Paradigm](https://arxiv.org/abs/2511.04570v1) | 潜在局部评价：视频模型推理对self-consistency/ICL敏感；MATH等分数不证明action-conditioned world dynamics。 |
| [2511.04671v1 / X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations](https://arxiv.org/abs/2511.04671v1) | 潜在VLA反侧：naive人/机器人轨迹混训不佳，按noise区分coarse/fine embodiment引导；限五任务16%声明。 |
| [2511.04555v1 / Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment](https://arxiv.org/abs/2511.04555v1) | 潜在VLA机制：原生VLM与cross-modal diffusion、两阶段训练保留语义；不因0.77B或榜单准入。 |
| [2511.04195v1 / Computational Turing Test Reveals Systematic Differences Between Human and AI Language](https://arxiv.org/abs/2511.04195v1) | 潜在评价反侧：human-likeness与semantic fidelity取舍、九模型五calibration；社交文本局部结果不当全语言定律。 |
| [2511.03827v1 / STARS: Segment-level Token Alignment with Rejection Sampling in Large Language Models](https://arxiv.org/abs/2511.03827v1) | 潜在解码：固定短segment采样/评分/rejection的质量成本纠正。采用v1 Segment-level Token Alignment，不倒灌v2改题Synchronous。 |
| [2511.04439v1 / The Peril of Preference: Why GRPO fails on Ordinal Rewards](https://arxiv.org/abs/2511.04439v1) | 潜在GRPO反侧：ordinal reward组baseline可给予失败轨迹正advantage，quality threshold处理过渡偏好；采用v1 The Peril of Preference，不倒灌v3。 |
| [2511.03942v1 / MIDI-LLM: Adapting Large Language Models for Text-to-MIDI Music Generation](https://arxiv.org/abs/2511.03942v1) | 潜在表示：text vocabulary编码MIDI、两阶段训练与结构复用；需codec/目标实际差额，不因可接vLLM路由framework。 |
| [2511.03929v1 / NVIDIA Nemotron Nano V2 VL](https://arxiv.org/abs/2511.03929v1) | 潜在：hybrid Mamba/Transformer与token reduction的长文档视频预算条件；FP8/FP4版本名本身不贡献，首次官方release日期待有限核。 |
| [2511.04473v1 / Ground-Truth Subgraphs for Better Training and Evaluation of Knowledge Graph Augmented LLMs](https://arxiv.org/abs/2511.04473v1) | 潜在评价：unseen facts/structure与groundtruth KGQA修正RAG验证条件；不以新增题量准入。 |
| [2511.04247v1 / On the Brittleness of CLIP Text Encoders](https://arxiv.org/abs/2511.04247v1) | 潜在CLIP反侧：微小标点/大小写扰动影响retrieval ranking，局部TRECVID/V3C1稳健性条件，不采所有模型脆弱。 |
| [2511.04307v1 / GUI-360: A Comprehensive Dataset and Benchmark for Computer-Using Agents](https://arxiv.org/abs/2511.04307v1) | 潜在评价：GUI/API联合grounding、任务query生成/环境实例化与失败轨迹，需控制真实执行/合成质量差额。 |
| [2511.04393v1 / Post-Training LLMs as Better Decision-Making Agents: A Regret-Minimization Approach](https://arxiv.org/abs/2511.04393v1) | 潜在训练理论：多轨迹k-low-regret finetuning；单层/简化learner假设不外推一般深模型无悔。 |
| [2511.04427v1 / Speed at the Cost of Quality? The Impact of LLM Agent Assistance on Software Development](https://arxiv.org/abs/2511.04427v1) | 潜在负侧：Cursor采用后速度暂时改善而复杂度/质量代价持续；Diff-in-Diff/GMM是观察研究，不写随机试验因果保证。 |
| [2511.03913v1 / Evolutionary Optimization Trumps Adam Optimization on Embedding Space Exploration](https://arxiv.org/abs/2511.03913v1) | 潜在局部替代设计：sepCMAES与Adam的SDXL-Turbo embedding搜索预算/目标差额；LAION/CLIP加权代理非全生成质量。 |
| [2511.04286v1 / Efficient Reinforcement Learning from Human Feedback via Bayesian Preference Inference](https://arxiv.org/abs/2511.04286v1) | 潜在训练：Bayesian preference acquisition模块与RLHF样本预算，需区分posterior推断与policy训练成本。 |
| [2511.04432v1 / If I Could Turn Back Time: Temporal Reframing as a Historical Reasoning Task for LLMs](https://arxiv.org/abs/2511.04432v1) | 潜在局部评价：历史时间重框任务的语言/模型大小效应；LLMjudge经母语检查而非自动可信，不因新任务名准入。 |
| [2511.04477v1 / Enabling Dynamic Sparsity in Quantized LLM Inference](https://arxiv.org/abs/2511.04477v1) | 潜在推理：zigzag低比特布局/GEMV/稀疏索引gather共同解决动态激活稀疏与group quantization冲突；1.55x仅作者配置。 |
| [2511.04481v1 / Promoting Sustainable Web Agents: Benchmarking and Estimating Energy Consumption through Empirical and Theoretical Analysis](https://arxiv.org/abs/2511.04481v1) | 潜在评价负侧：web agent能耗不与成功质量单调，理论估计/实测权限分离，未公开参数导致估算限制。 |
| [2511.04491v1 / RUST-BENCH: Benchmarking LLM Reasoning on Unstructured Text within Structured Tables](https://arxiv.org/abs/2511.04491v1) | 潜在评价：长结构化表中自由文本multi-hop reasoning失败盲区，非仅RUST-BENCH题量。 |
| [2511.04502v1 / RAGalyst: Automated Human-Aligned Agentic Evaluation for Domain-Specific RAG](https://arxiv.org/abs/2511.04502v1) | 潜在评价：domain RAG judge prompt优化/answerability与human alignment；未存在universal最好embedding，不采judge相关即可靠。 |
| [2511.04646v1 / DR. WELL: Dynamic Reasoning and Learning with Symbolic World Model for Embodied LLM-Based Multi-Agent Collaboration](https://arxiv.org/abs/2511.04646v1) | 潜在Agent：角色consensus commit之后独立symbolic planning及共享观测state的grounding/成本；非predictive world model真值保证。 |
| [2511.04654v1 / Logit-Entropy Adaptive Stopping Heuristic for Efficient Chain-of-Thought Reasoning](https://arxiv.org/abs/2511.04654v1) | 潜在负侧：entropy/logit-margin plateau停止节省30–35%token但最多10pp准确率损失，保留质量成本而非强造无损。 |
| [2511.04662v1 / VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks](https://arxiv.org/abs/2511.04662v1) | 潜在验证：FOL premise extraction+solver validation接self-reflection/SFT/DPO；solver逻辑有效不证明premise事实真实。 |
| [2511.05609v1 / Walking the Schrödinger Bridge: A Direct Trajectory for Text-to-3D Generation](https://arxiv.org/abs/2511.05609v1) | 潜在生成理论：SDS在特殊条件下作为Schrödinger Bridge简化，TraCe直接render→text target桥与LoRA score dynamics；需原假设，不采所有SDS缺陷已解。 |
| [2511.04317v1 / RISE-T2V: Rephrasing and Injecting Semantics with LLM for Expansive Text-to-Video Generation](https://arxiv.org/abs/2511.04317v1) | 潜在生成：在线LLM hidden rephrasing adapter注入视频语义条件，需目标/训练预算而非仅video分数。 |
| [2511.04357v1 / GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies](https://arxiv.org/abs/2511.04357v1) | 潜在VLA：连续scene graph→symbolic demo域→low-level policy长程交接，观测符号/动作闭环不被planner预测替代。 |
| [2511.04601v1 / PixCLIP: Achieving Fine-grained Visual Language Understanding via Any-granularity Pixel-Text Alignment Learning](https://arxiv.org/abs/2511.04601v1) | 潜在表示：CLIP text encoder替换LLM与pixel/text三分支对齐，长描述粒度机制，不以LongGRIT数据量准入。 |
| [2511.04727v1 / IndicVisionBench: Benchmarking Cultural and Multilingual Understanding in VLMs](https://arxiv.org/abs/2511.04727v1) | 潜在局部评价：同图英语/十Indic语言OCR/MMT/VQA配对与文化偏差，需分离标注/语言/模型条件。 |
| [2511.04664v1 / SAFe-Copilot: Unified Shared Autonomy Framework](https://arxiv.org/abs/2511.04664v1) | 潜在VLA安全：高层意图仲裁/人控制与自动驾驶共享自主；mock-human perfect recall与真实participant92分开，不授完美控制。 |
| [2511.04670v1 / Cambrian-S: Towards Spatial Supersensing in Video](https://arxiv.org/abs/2511.04670v1) | 潜在World/Mem：视频spatial recall/count随context仍受限，next-latent prediction surprise用于分段记忆；不把视频观测生成当动作动力学。 |
| [2511.03909v3 / Tensor Computation of Euler Characteristic Functions and Transforms](https://arxiv.org/abs/2511.03909v3) | 范围关闭：ECF/WECT拓扑描述符tensor/GPU实现，非大模型计算/模型形成机制；当前v3题摘仅作范围，不授v1事件。 |
| [2511.03939v1 / RLHF: A comprehensive Survey for Cultural, Multimodal and Low Latency Alignment Methods](https://arxiv.org/abs/2511.03939v1) | 关闭：PPO/DPO/GRPO、多模态/文化/低延迟文献综述与挑战归纳，未新增能修正具体判断的对照/机制证据。 |
| [2511.03958v1 / Multi-Agent Collaborative Framework For Math Problem Generation](https://arxiv.org/abs/2511.03958v1) | 关闭：多个Agent迭代改善数学教学问题难度/清晰度，所述五项pedagogical元评价未披露新协作机制/失效边界。 |
| [2511.04445v1 / ForecastGAN: A Decomposition-Based Adversarial Framework for Multi-Horizon Time Series Forecasting](https://arxiv.org/abs/2511.04445v1) | 范围关闭：horizon选模、seasonality/trend拆分与cGAN用于一般时序预测，未建立foundation/模型系统主线的实际机制变化。 |
| [2511.04464v1 / Beyond Shortest Path: Agentic Vehicular Routing with Semantic Context](https://arxiv.org/abs/2511.04464v1) | 关闭：多目标Dijkstra候选route接LLM语义选路及POI cache，只有城市场景88%初选表现，无新执行/仲裁可靠性条件。 |
| [2511.04499v1 / Decoding Emergent Big Five Traits in Large Language Models: Temperature-Dependent Expression and Architectural Clustering](https://arxiv.org/abs/2511.04499v1) | 潜在局部评价：temperature使BFI2 trait回答变化、架构聚类不能因果归因结构；问卷表达不等于模型人格。 |
| [2511.05615v1 / wa-hls4ml: A Benchmark and Surrogate Models for hls4ml Resource and Latency Estimation](https://arxiv.org/abs/2511.05615v1) | 潜在编译预算：hls4ml FPGA synthesis surrogate预测资源/latency可修正搜索预算，GNN/Transformer的synthetic percentile误差不当LLM硬件保证。 |
| [2511.03980v1 / LLMs and Cultural Values: the Impact of Prompt Language and Explicit Cultural Framing](https://arxiv.org/abs/2511.03980v1) | 潜在评价反侧：explicit文化frame比目标语言更改善人值alignment、两者结合不额外有效；限10模型63问11语言，不当模型国家本质。 |
| [2511.04728v1 / Trustworthiness Calibration Framework for Phishing Email Detection Using Large Language Models](https://arxiv.org/abs/2511.04728v1) | 潜在局部评价：calibration/consistency/robustness与accuracy不一致；TCI/CDS组合指标有效性需定点，而非钓鱼分类器榜单准入。 |
| [2511.04123v1 / Text to Sketch Generation with Multi-Styles](https://arxiv.org/abs/2511.04123v1) | 潜在生成：style sketch auxiliary feature+linear smoothing不覆写self-attention KV，降低content leakage；多style AdaIN条件待核。 |
| [2511.04641v1 / Efficient probabilistic surrogate modeling techniques for partially-observed large-scale dynamical systems](https://arxiv.org/abs/2511.04641v1) | 范围关闭：PDE/Navier-Stokes部分观测模拟surrogate、二维切片inflow；AI for Science暂缓，不借World Model重入。 |
| [2511.11621v1 / AIvailable: A Software-Defined Architecture for LLM-as-a-Service on Heterogeneous and Legacy GPUs](https://arxiv.org/abs/2511.11621v1) | 潜在服务：异构/旧GPU VRAM-aware allocation/reallocation，需实际模型状态迁移/availability机制而非四组件命名；晚ID不从Nov6submitted猜公开。 |
| [2511.10664v1 / Evaluating Modern Large Language Models on Low-Resource and Morphologically Rich Languages:A Cross-Lingual Benchmark Across Cantonese, Japanese, and Turkish](https://arxiv.org/abs/2511.10664v1) | 潜在局部评价：形态复杂/低资源语言human与BLEU/ROUGE对照的失配，不能只因新benchmark准入；晚ID需first-public独立证明。 |
| [2511.04341v1 / Monitor-Generate-Verify (MGV):Formalising Metacognitive Theory for Language Model Reasoning](https://arxiv.org/abs/2511.04341v1) | 关闭：MGV把经典metacognition译为monitor/generate/verify规格，明确无empirical validation；原题摘没有新的可检验机制/推导，引用20%并非本文新反证。 |
| [2511.04124v1 / Decomposable Neuro Symbolic Regression](https://arxiv.org/abs/2511.04124v1) | 潜在一般解释/蒸馏机制：Multi-Set Transformer生成单变量skeleton，再GA选择/GP合并时保存结构，解释opaque回归函数；没有具体科学应用前提，不能仅因symbolic regression关闭为AI for Science。局部插值/外推与结构恢复条件待核。 |
| [2511.04541v1 / LLM-as-a-Judge: Toward World Models for Slate Recommendation Systems](https://arxiv.org/abs/2511.04541v1) | 贡献尚含糊：slate preference pairwise LLMjudge/world-model应用，需具体preference function性质或评价反证才可准入，摘要不够关闭亦不够认定贡献。 |
| [2511.08616v1 / Reasoning on Time-Series for Financial Technical Analysis](https://arxiv.org/abs/2511.08616v1) | 关闭：股票price转文本/inverse-MSE trace奖励接预测backbone，主要金融预测/专家trace得分，未新增通用推理有效性条件。 |
| [2511.04500v1 / Large language models replicate and predict human cooperation across experiments in game theory](https://arxiv.org/abs/2511.04500v1) | 潜在局部评价：Llama聚合人类合作匹配而Qwen更近Nash预测、无需persona的模型差异可核机器行为评价条件；社科新假说部分不纳入，不把数字孪生本身或人类实验预测当Agent可靠性。 |
| [2511.10665v1 / Guarding the Meaning: Self-Supervised Training for Semantic Robustness in Guard Models](https://arxiv.org/abs/2511.10665v1) | 潜在安全反侧：mean/median paraphrase aggregation可能降低guard安全，skew-aware consistency训练；58%/40%限作者协议，晚ID不猜公开。 |
| [2511.04205v1 / LLM-as-a-Judge is Bad, Based on AI Attempting the Exam Qualifying for the Member of the Polish National Board of Appeal](https://arxiv.org/abs/2511.04205v1) | 潜在局部评价负侧：考试知识题表现不能外推written judgement，LLMjudge与官方委员会不一致；不采用法律实务建议。 |
| [2511.04703v1 / Measuring what Matters: Construct Validity in Large Language Model Benchmarks](https://arxiv.org/abs/2511.04703v1) | 潜在评价反侧：29reviewer审445benchmark构念/任务/评分不匹配，需实际系统review方法/反例，非八建议名称即知识缺口。 |
| [2511.04479v1 / ThaiOCRBench: A Task-Diverse Benchmark for Vision-Language Understanding in Thai](https://arxiv.org/abs/2511.04479v1) | 潜在局部多模态评价：Thai脚本文档结构/handwritten错误差异；原当前v3纠正Table2/Gemma deletion，必要反侧未读普通待办，不采用受影响数字。 |
| [2511.04108v1 / Batch Prompting Suppresses Overthinking Reasoning Under Constraint: How Batch Prompting Suppresses Overthinking in Reasoning Models](https://arxiv.org/abs/2511.04108v1) | 潜在推理质量成本：batch prompting行为regularization/跨题pattern效应与3–5x token预算，不能只当continuous batching吞吐机制。 |
| [2511.04694v1 / Reasoning Up the Instruction Ladder for Controllable Language Models](https://arxiv.org/abs/2511.04694v1) | 潜在安全机制：verifiable IH冲突数据+RL将reasoning迁移指令优先级，需外分布攻击/权限边界；原Oct30submitted不等public。 |
| [2511.04689v1 / Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks](https://arxiv.org/abs/2511.04689v1) | 潜在评价：IRT Fisher信息选题及negative discrimination静态误差，42/5608样本/0.154MAE而非无损普遍90%省题；原Oct26submitted不等public。 |

## 只作范围的明确标题

补读最后一项[2511.05616v1 / Personalized Image Editing in Text-to-Image Diffusion Models via Collaborative Direct Preference Optimization](https://arxiv.org/abs/2511.05616v1)完整题摘（multimodal原XML）：动态user preference graph/GNN embedding以邻域coherence接个体DPO目标，有生成偏好共享/个体差异的具体潜力，不因编辑应用名称关闭。日期同样未获首次公开证明，不评分、不正面采用。上述83项之后实际题摘总数为84项，非全文审阅数。

两项剩余明确科学标题：2511.04437 Deep Koopman Economic Model Predictive Control of a Pasteurisation Unit、2511.04539 Geometry-Guided Generative Representation for Functional Brain Graphs，分别工艺过程与脑图科学应用，范围关闭，未阅读全文。

以下是原窄主题列表的title范围排除，不声称读全文或深审：PETRA SARS-CoV-2 mutation(2511.03976)、radiology de-identification(2511.04079)、MedSapiens landmark(2511.04255)、kidney CT segmentation(2511.04334)、MedGemma radiographs(2511.05600)、MLCommons scientific benchmarks ontology(2511.05614)、superconductivity discovery(2511.03782)、medical emergency management(2511.08614)、rare disease reasoning(2511.04720)、radiology uncertainty(2511.04506)、MedDChest(2511.04016)、Nowcast3D precipitation(2511.04659)：领域科学/医学应用，ROADMAP暂缓。不借Data/Evaluation/Agent重引科学应用。DMSORT maritime vessel tracking(2511.04128)、RUL sensor prognosis(2511.04723)、aircraft trajectory generation(2511.04155)、Agentmander redistricting(2511.04076)的标题分别明确特定领域tracking/prognosis/trajectory/political optimization，未建立本主线关系，不将它们全部升级全文队列。

## 尚可执行与外部保留分开

- slate推荐2511.04541v1贡献决定§2–4已必要读取：pairwise交换顺序/四模型多数投票，比较user utility regret与transitivity/asymmetry。排序近同slate时接近random、transitivity好但asymmetry仍近random的局部评价反侧有潜力；不是动态环境预测，不能因World Models题名归Ch25。原必要段见[本日原响应](./nov08-tail-judge-thai-core.txt)，日期尚未核，不读全部附件。
- ThaiOCRBench当前v3的Table2/相关结论与v1已定点比较，见[必要纠错记录](./FINAL_LOCAL_NOTES.md)；日期/修订未授本窗，不采用受影响数字。已知NeurIPS精确forum恢复403已有限停止，普通尾项不再反复空查。
- 已有限日期恢复受阻的首批六篇、PLLuM/Q3R/Nested见各校准包，保留潜在差额但不用于正面证据，不因不采用继续全附件。
- 原官方50标题切片中其余标题只作查漏，未全部送题摘；不得把未读切片外条目写成已审重复。这里记录的potential方向并非owner正文差额证明。
