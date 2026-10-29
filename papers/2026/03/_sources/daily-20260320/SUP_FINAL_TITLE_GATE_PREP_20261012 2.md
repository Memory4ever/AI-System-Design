# 原有限title尾13：必要题摘/date与贡献提案

resume_mar17，2026-10-12，仅03-20补03-19自然日。来自已有四query与页2的具名未闭合相关/含糊title；不新query、不把全部181去重title作全文队列（217跨组返回槽位；130是原四首页去重而非含页2总数，恢复实际重算已纠）。以下实际exact-v1官方AB、authors/title与exactDataCite HTTP200已读；全部registered03/19UTC且同ID/title匹配，结合本日已核availability下界夹证归03/19BJT arXiv事件，不追时刻或授全球firstbody。尚待非准备者贡献校准，**不加分母、不自授Source/PRE/Books**。

## 原约束→实际增量→改变选择

| 身份 | 具体潜力提案 | 拟分/主线 |
| --- | --- | --- |
| [RVV/xDSL17800v1](https://arxiv.org/abs/2603.17800v1) | 现有MLIR缺高层到RVV intrinsic lowering→自定义IR/pass生成可嵌入C GEMM且有BERT-Large workload→需核可移植编译路径与硬件执行共存条件 | 1+2+2=5；INFER-TENSORRT-LLM |
| [ProgramHypergraph17627v1](https://arxiv.org/abs/2603.17627v1) | binary PSG不能表达tile多元co-location/几何product身份→任意arity hyperedge/grade推导sparsity→需核模型计算编译表示与placement联合约束 | 2+1+2=5；INFER-TENSORRT-LLM |
| [KANtize17230v1](https://arxiv.org/abs/2603.17230v1) | recursive spline计算不能只靠低bit乘法变便宜→量化预计算B-spline表替代递推→需核representation/lookup/低bit代价与质量条件 | 2+1+2=5；MODEL-FFN |
| [ATD17912v1](https://arxiv.org/abs/2603.17912v1) | 跨语attention表征难比较tokenization→attention概率OT度量并消费为低资源迁移regularizer→需核crosslanguage表示比较与训练条件，非语言家族排行 | 2+1+2=5；MODEL-SELF-ATTENTION |
| [AgentDP17902v1](https://arxiv.org/abs/2603.17902v1) | 只保护prompt忽略enterprise dataset经长输出泄漏→token/message DP及temperature/length界→需核生成分布的相邻数据/隐私取舍条件 | 2+2+2=6；PLATFORM-SECURITY |
| [SARE17729v1](https://arxiv.org/abs/2603.17729v1) | 统一confidence触发对不同class可靠性不一致→support分类检索统计与candidate entropy共同路由推理→需核class条件验证人口与计算深度而非仅retrieval+reflection组合 | 2+1+2=5；MULTIMODAL-REPRESENTATION |
| [PrivEscLLM17673v1](https://arxiv.org/abs/2603.17673v1) | cloud agent敏感context与交互轮预算不适本地部署→4B程序化trace SFT/验证reward posttrain及重复预算对照→需核小policy是否改变本地模型可用资源边界，未授root率/百倍费 | 2+1+2=5；TRAIN-GRPO |
| [Loc3R-VLM18002v1](https://arxiv.org/abs/2603.18002v1) | 2D VLM仅输入geometry cue不能学视点3D→layout reconstruction/situation目标与轻poseprior→需核特权几何监督和语言定位消费者 | 2+2+2=6；MULTIMODAL-REPRESENTATION |
| [STTS18004v1](https://arxiv.org/abs/2603.18004v1) | 只ViT或LLM单边pruning让另一侧成本仍在→time aux/spatial downstreamgradient统一scoring+packing→需核训练/推理跨边界输入删除的质量成本条件 | 2+2+2=6；MULTIMODAL-REPRESENTATION |
| [ContinuousSteering17998v1](https://arxiv.org/abs/2603.17998v1) | 固定strength编辑欠/过steer→debiased contrastive prompt方向与elastic有效区间→需核连续条件表示干预/区间消费者与uniformity评价资格 | 2+1+2=5；MULTIMODAL-GENERATIVE-PARADIGMS |
| [DynaEdit17989v1](https://arxiv.org/abs/2603.17989v1) | 训练外inversionfree移到任意motion编辑有低频错位/高频jitter→解释两类失效并改采样机制→需核非motion保持编辑成立边界 | 2+2+2=6；MULTIMODAL-GENERATIVE-PARADIGMS |
| [SpecDistribution17969v1](https://arxiv.org/abs/2603.17969v1) | pretrained robotics policy不能兑现时序约束→remaining horizon dynamics传播后hardSTL约束最小改distribution→需核预测约束与真实执行之间的控制资格 | 2+2+2=6；MULTIMODAL-EMBODIED-VLA |
| [LaDe17965v1](https://arxiv.org/abs/2603.17965v1) | 固定层数/连续region令复杂设计层数扩张→perlayer描述/4DRoPE联合RGBA生成与layer条件训练→需核可变结构输出和分解/生成共存条件 | 2+2+2=6；MULTIMODAL-GENERATIVE-PARADIGMS |

SARE因摘要易误仅流程组合，决定准入定点实际v1§2.1–2.3 L89–128：support set分别建prototype/分类retrievalcount与命中统计/带gold反思；trigger实际fusedconfidence−类别有限经验罚项−candidate entropy。只此新消费/验收条件提案，不授Hoeffding真置信界或全部14任务效用。17673有安全/攻防信号，实际v1§III-A L94–96、§III-D reward/时序核心L123–135，以及find返回的§V/limitations局部说明（不是完整§V审阅）：root验证只隔离sandbox成功，不授权攻击第三方、不授生产attack coverage；成熟SFT→RLVR本身不贡献，拟资源/严格轮预算可行边界与数据泄漏控制需非准备者校准，小任务数字不单独留。

## current轻量说明与先稿信号

13 current abs均HTTP200实际读title/Comments/history。17627明确Major revision/expanded jointconstraint和geometric sparsity/capacity examples；后续若采用这些具体界只定点受影响currentv5，而不机械全历史diff。17673 current题名变回Towards Reliable Local Security Agents、无纠错comments，原v1题名仍按精确版本保留；SARE currentpreprint/underreview/v3，无明确纠错。其他projectpage或12pages/figures等说明不触发完整修订审；本次已见字段无明确先公开venue日期信号，不凭空扫描venue。缺失或title变化未当受阻；当前说明不能授未读版本正文。

## 原始 HTTP 字段（本次实读，不是Evidence审阅）

```json
[
  {
    "id": "17800",
    "status": 200,
    "title": "Title: Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings",
    "author": "Authors: Jie Lei , Héctor Martínez , Adrián Castelló",
    "abstract": "Abstract: The growing adoption of RISC-V in high-performance and scientific computing has increased the need for performance-portable code targeting the RISC-V Vector (RVV) extension. However, current compiler infrastructures provide limited end-to-end support for generating optimized RVV code from high-level representations to low-level implementations. In particular, existing MLIR distributions lack practical lowering paths that map high-level abstractions to RVV intrinsics, limiting their applicability for production-ready RISC-V kernels. This paper presents a compilation approach that combines MLIR with xDSL to bridge the missing lowering stages required for RVV code generation. Using custom intermediate representations and transformation passes implemented in xDSL, we systematically translate high-level operations into specialized, hardware-aware C code invoking RVV intrinsics. The resulting kernels are emitted as portable C functions that can be directly integrated into existing applications, enabling incremental adoption without modifying surrounding software stacks. We demonstrate the approach on the General Matrix Multiplication (GEMM) kernel and evaluate the generated micro-kernels on two real RISC-V platforms, the K230 and the BananaPi F3, comparing against OpenBLAS for both square-matrix benchmarks and transformer-based workloads derived from the BERT-Large model. When integrated into a matrix multiplication kernel, the proposed approach consistently outperforms OpenBLAS, reaching up to 12.2 GFLOPS compared to the baseline&#39;s 5.1 GFLOPS and providing performance improvements between 10--35\\% across the evaluated workloads. These results demonstrate that combining MLIR with xDSL provides a practical pathway to portable, optimized code generation for RISC-V platforms.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:40:52.000Z",
    "created": "2026-03-19T02:40:52.000Z",
    "dateTitle": [
      {
        "title": "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings"
      }
    ]
  },
  {
    "id": "17627",
    "status": 200,
    "title": "Title: The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation",
    "author": "Authors: Houston Haynes",
    "abstract": "Abstract: The Program Semantic Graph (PSG) introduced in prior work on Dimensional Type Systems and Deterministic Memory Management encodes compilation-relevant properties as binary edge relations between computation nodes. This representation is adequate for scalar and tensor computations, but becomes structurally insufficient for two classes of problems central to heterogeneous compute: tile co-location and routing constraints in spatial dataflow architectures, which are inherently multi-way; and geometric algebra computation, where graded multi-way products cannot be faithfully represented as sequences of binary operations without loss of algebraic identity. This paper introduces the Program Hypergraph (PHG) as a principled generalization of the PSG that promotes binary edges to hyperedges of arbitrary arity. We demonstrate that grade in Clifford algebra is a natural dimension axis within the existing DTS abelian group framework, that grade inference derives geometric product sparsity eliminating the primary performance objection to Clifford algebra neural networks without manual specialization, and that the k-simplex structure of mesh topology is a direct instance of the hyperedge formalism. We assess the existing geometric algebra library ecosystem, identify the consistent type-theoretic gap that no current system addresses, and show that the PHG closes it within the Fidelity compilation framework. The result is a compilation framework where geometric correctness, memory placement, numerical precision selection, and hardware partitioning are jointly derivable from a single graph structure exposed as interactive design-time feedback.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:36:47.000Z",
    "created": "2026-03-19T02:36:46.000Z",
    "dateTitle": [
      {
        "title": "The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation"
      }
    ]
  },
  {
    "id": "17230",
    "status": 200,
    "title": "Title: KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference",
    "author": "Authors: Sohaib Errabii , Olivier Sentieys , Marcello Traiola",
    "abstract": "Abstract: Kolmogorov-Arnold Networks (KANs) have gained attention for their potential to outperform Multi-Layer Perceptrons (MLPs) in terms of parameter efficiency and interpretability. Unlike traditional MLPs, KANs use learnable non-linear activation functions, typically spline functions, expressed as linear combinations of basis splines (B-splines). B-spline coefficients serve as the model&#39;s learnable parameters. However, evaluating these spline functions increases computational complexity during inference. Conventional quantization reduces this complexity by lowering the numerical precision of parameters and activations. However, the impact of quantization on KANs, and especially its effectiveness in reducing computational complexity, is largely unexplored, particularly for quantization levels below 8 bits. The study investigates the impact of low-bit quantization on KANs and its impact on computational complexity and hardware efficiency. Results show that B-splines can be quantized to 2-3 bits with negligible loss in accuracy, significantly reducing computational complexity. Hence, we investigate the potential of using low-bit quantized precomputed tables as a replacement for the recursive B-spline algorithm. This approach aims to further reduce the computational complexity of KANs and enhance hardware efficiency while maintaining accuracy. For example, ResKAN18 achieves a 50x reduction in BitOps without loss of accuracy using low-bit-quantized B-spline tables. Additionally, precomputed 8-bit lookup tables improve GPU inference speedup by up to 2.9x, while on FPGA-based systolic-array accelerators, reducing B-spline table precision from 8 to 3 bits cuts resource usage by 36%, increases clock frequency by 50%, and enhances speedup by 1.24x. On a 28nm FD-SOI ASIC, reducing the B-spline bit-width from 16 to 3 bits achieves 72% area reduction and 50% higher maximum frequency.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:27:15.000Z",
    "created": "2026-03-19T02:27:14.000Z",
    "dateTitle": [
      {
        "title": "KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference"
      }
    ]
  },
  {
    "id": "17912",
    "status": 200,
    "title": "Title: Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages",
    "author": "Authors: Yue Zhao , Jiatao Gu , Paloma Jeretič , Weijie Su",
    "abstract": "Abstract: Understanding the distance between human languages is central to linguistics, anthropology, and tracing human evolutionary history. Yet, while linguistics has long provided rich qualitative accounts of cross-linguistic variation, a unified and scalable quantitative approach to measuring language distance remains lacking. In this paper, we introduce a method that leverages pretrained multilingual language models as systematic instruments for linguistic measurement. Specifically, we show that the spontaneously emerged attention mechanisms of these models provide a robust, tokenization-agnostic measure of cross-linguistic distance, termed Attention Transport Distance (ATD). By treating attention matrices as probability distributions and measuring their geometric divergence via optimal transport, we quantify the representational distance between languages during translation. Applying ATD to a large and diverse set of languages, we demonstrate that the resulting distances recover established linguistic groupings with high fidelity and reveal patterns aligned with geographic and contact-induced relationships. Furthermore, incorporating ATD as a regularizer improves transfer performance in low-resource machine translation. Our results establish a principled foundation for testing linguistic hypotheses using artificial neural networks. This framework transforms multilingual models into powerful tools for quantitative linguistic discovery, facilitating more equitable multilingual AI.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:43:31.000Z",
    "created": "2026-03-19T02:43:30.000Z",
    "dateTitle": [
      {
        "title": "Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages"
      }
    ]
  },
  {
    "id": "17902",
    "status": 200,
    "title": "Title: Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs",
    "author": "Authors: Ya-Ting Yang , Quanyan Zhu",
    "abstract": "Abstract: Large language models (LLMs) and AI agents are increasingly integrated into enterprise systems to access internal databases and generate context-aware responses. While such integration improves productivity and decision support, the model outputs may inadvertently reveal sensitive information. Although many prior efforts focus on protecting the privacy of user prompts, relatively few studies consider privacy risks from the enterprise data perspective. Hence, this paper develops a probabilistic framework for analyzing privacy leakage in AI agents based on differential privacy. We model response generation as a stochastic mechanism that maps prompts and datasets to distributions over token sequences. Within this framework, we introduce token-level and message-level differential privacy and derive privacy bounds that relate privacy leakage to generation parameters such as temperature and message length. We further formulate a privacy-utility design problem that characterizes optimal temperature selection.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:43:17.000Z",
    "created": "2026-03-19T02:43:17.000Z",
    "dateTitle": [
      {
        "title": "Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs"
      }
    ]
  },
  {
    "id": "17729",
    "status": 200,
    "title": "Title: SARE: Sample-wise Adaptive Reasoning for Training-free Fine-grained Visual Recognition",
    "author": "Authors: Jingxiao Yang , DaLin He , Miao Pan , Ge Su , Wenqi Zhang , Yifeng Hu , Tangwei Li , Yuke Li , Xuhong Zhang",
    "abstract": "Abstract: Recent advances in Large Vision-Language Models (LVLMs) have enabled training-free Fine-Grained Visual Recognition (FGVR). However, effectively exploiting LVLMs for FGVR remains challenging due to the inherent visual ambiguity of subordinate-level categories. Existing methods predominantly adopt either retrieval-oriented or reasoning-oriented paradigms to tackle this challenge, but both are constrained by two fundamental limitations:(1) They apply the same inference pipeline to all samples without accounting for uneven recognition difficulty, thereby leading to suboptimal accuracy and efficiency; (2) The lack of mechanisms to consolidate and reuse error-specific experience causes repeated failures on similar challenging cases. To address these limitations, we propose SARE, a Sample-wise Adaptive textbfREasoning framework for training-free FGVR. Specifically, SARE adopts a cascaded design that combines fast candidate retrieval with fine-grained reasoning, invoking the latter only when necessary. In the reasoning process, SARE incorporates a self-reflective experience mechanism that leverages past failures to provide transferable discriminative guidance during inference, without any parameter updates. Extensive experiments across 14 datasets substantiate that SARE achieves state-of-the-art performance while substantially reducing computational overhead.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:39:10.000Z",
    "created": "2026-03-19T02:39:10.000Z",
    "dateTitle": [
      {
        "title": "SARE: Sample-wise Adaptive Reasoning for Training-free Fine-grained Visual Recognition"
      }
    ]
  },
  {
    "id": "17673",
    "status": 200,
    "title": "Title: Post-Training Local LLM Agents for Linux Privilege Escalation with Verifiable Rewards",
    "author": "Authors: Philipp Normann , Andreas Happe , Jürgen Cito , Daniel Arp",
    "abstract": "Abstract: LLM agents are increasingly relevant to research domains such as vulnerability discovery. Yet, the strongest systems remain closed and cloud-only, making them resource-intensive, difficult to reproduce, and unsuitable for work involving proprietary code or sensitive data. Consequently, there is an urgent need for small, local models that can perform security tasks under strict resource budgets, but methods for developing them remain underexplored. In this paper, we address this gap by proposing a two-stage post-training pipeline. We focus on the problem of Linux privilege escalation, where success is automatically verifiable and the task requires multi-step interactive reasoning. Using an experimental setup that prevents data leakage, we post-train a 4B model in two stages: supervised fine-tuning on traces from procedurally generated privilege-escalation environments, followed by reinforcement learning with verifiable rewards. On a held-out benchmark of 12 Linux privilege-escalation scenarios, supervised fine-tuning alone more than doubles the baseline success rate at 20 rounds, and reinforcement learning further lifts our resulting model, PrivEsc-LLM, to 95.8%, nearly matching Claude Opus 4.6 at 97.5%. At the same time, the expected inference cost per successful escalation is reduced by over 100x.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:37:52.000Z",
    "created": "2026-03-19T02:37:52.000Z",
    "dateTitle": [
      {
        "title": "Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation"
      }
    ]
  },
  {
    "id": "18002",
    "status": 200,
    "title": "Title: Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
    "author": "Authors: Kevin Qu , Haozhe Qi , Mihai Dusmanu , Mahdi Rad , Rui Wang , Marc Pollefeys",
    "abstract": "Abstract: Multimodal Large Language Models (MLLMs) have made impressive progress in connecting vision and language, but they still struggle with spatial understanding and viewpoint-aware reasoning. Recent efforts aim to augment the input representations with geometric cues rather than explicitly teaching models to reason in 3D space. We introduce Loc3R-VLM, a framework that equips 2D Vision-Language Models with advanced 3D understanding capabilities from monocular video input. Inspired by human spatial cognition, Loc3R-VLM relies on two joint objectives: global layout reconstruction to build a holistic representation of the scene structure, and explicit situation modeling to anchor egocentric perspective. These objectives provide direct spatial supervision that grounds both perception and language in a 3D context. To ensure geometric consistency and metric-scale alignment, we leverage lightweight camera pose priors extracted from a pre-trained 3D foundation model. Loc3R-VLM achieves state-of-the-art performance in language-based localization and outperforms existing 2D- and video-based approaches on situated and general 3D question-answering benchmarks, demonstrating that our spatial supervision framework enables strong 3D understanding. Project page: this https URL",
    "dateHTTP": 200,
    "date": "2026-03-19T02:45:42.000Z",
    "created": "2026-03-19T02:45:42.000Z",
    "dateTitle": [
      {
        "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models"
      }
    ]
  },
  {
    "id": "18004",
    "status": 200,
    "title": "Title: Unified Spatio-Temporal Token Scoring for Efficient Video VLMs",
    "author": "Authors: Jianrui Zhang , Yue Yang , Rohun Tripathi , Winson Han , Ranjay Krishna , Christopher Clark , Yong Jae Lee , Sangho Lee",
    "abstract": "Abstract: Token pruning is essential for enhancing the computational efficiency of vision-language models (VLMs), particularly for video-based tasks where temporal redundancy is prevalent. Prior approaches typically prune tokens either (1) within the vision transformer (ViT) exclusively for unimodal perception tasks such as action recognition and object segmentation, without adapting to downstream vision-language tasks; or (2) only within the LLM while leaving the ViT output intact, often requiring complex text-conditioned token selection mechanisms. In this paper, we introduce Spatio-Temporal Token Scoring (STTS), a simple and lightweight module that prunes vision tokens across both the ViT and the LLM without text conditioning or token merging, and is fully compatible with end-to-end training. By learning how to score temporally via an auxiliary loss and spatially via LLM downstream gradients, aided by our efficient packing algorithm, STTS prunes 50% of vision tokens throughout the entire architecture, resulting in a 62% improvement in efficiency during both training and inference with only a 0.7% drop in average performance across 13 short and long video QA tasks. Efficiency gains increase with more sampled frames per video. Applying test-time scaling for long-video QA further yields performance gains of 0.5-1% compared to the baseline. Overall, STTS represents a novel, simple yet effective technique for unified, architecture-wide vision token pruning.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:45:45.000Z",
    "created": "2026-03-19T02:45:44.000Z",
    "dateTitle": [
      {
        "title": "Unified Spatio-Temporal Token Scoring for Efficient Video VLMs"
      }
    ]
  },
  {
    "id": "17998",
    "status": 200,
    "title": "Title: The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering",
    "author": "Authors: Yigit Ekin , Yossi Gandelsman",
    "abstract": "Abstract: We present a training-free framework for continuous and controllable image editing at test time for text-conditioned generative models. In contrast to prior approaches that rely on additional training or manual user intervention, we find that a simple steering in the text-embedding space is sufficient to produce smooth edit control. Given a target concept (e.g., enhancing photorealism or changing facial expression), we use a large language model to automatically construct a small set of debiased contrastive prompt pairs, from which we compute a steering vector in the generator&#39;s text-encoder space. We then add this vector directly to the input prompt representation to control generation along the desired semantic axis. To obtain a continuous control, we propose an elastic range search procedure that automatically identifies an effective interval of steering magnitudes, avoiding both under-steering (no-edit) and over-steering (changing other attributes). Adding the scaled versions of the same vector within this interval yields smooth and continuous edits. Since our method modifies only textual representations, it naturally generalizes across text-conditioned modalities, including image and video generation. To quantify the steering continuity, we introduce a new evaluation metric that measures the uniformity of semantic change across edit strengths. We compare the continuous editing behavior across methods and find that, despite its simplicity and lightweight design, our approach is comparable to training-based alternatives, outperforming other training-free methods.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:45:36.000Z",
    "created": "2026-03-19T02:45:36.000Z",
    "dateTitle": [
      {
        "title": "The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering"
      }
    ]
  },
  {
    "id": "17989",
    "status": 200,
    "title": "Title: Versatile Editing of Video Content, Actions, and Dynamics without Training",
    "author": "Authors: Vladimir Kulikov , Roni Paiss , Andrey Voynov , Inbar Mosseri , Tali Dekel , Tomer Michaeli",
    "abstract": "Abstract: Controlled video generation has seen drastic improvements in recent years. However, editing actions and dynamic events, or inserting contents that should affect the behaviors of other objects in real-world videos, remains a major challenge. Existing trained models struggle with complex edits, likely due to the difficulty of collecting relevant training data. Similarly, existing training-free methods are inherently restricted to structure- and motion-preserving edits and do not support modification of motion or interactions. Here, we introduce DynaEdit, a training-free editing method that unlocks versatile video editing capabilities with pretrained text-to-video flow models. Our method relies on the recently introduced inversion-free approach, which does not intervene in the model internals, and is thus model-agnostic. We show that naively attempting to adapt this approach to general unconstrained editing results in severe low-frequency misalignment and high-frequency jitter. We explain the sources for these phenomena and introduce novel mechanisms for overcoming them. Through extensive experiments, we show that DynaEdit achieves state-of-the-art results on complex text-based video editing tasks, including modifying actions, inserting objects that interact with the scene, and introducing global effects.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:45:24.000Z",
    "created": "2026-03-19T02:45:23.000Z",
    "dateTitle": [
      {
        "title": "Versatile Editing of Video Content, Actions, and Dynamics without Training"
      }
    ]
  },
  {
    "id": "17969",
    "status": 200,
    "title": "Title: Specification-Aware Distribution Shaping for Robotics Foundation Models",
    "author": "Authors: Sadık Bera Yüksel , Derya Aksaray",
    "abstract": "Abstract: Robotics foundation models have demonstrated strong capabilities in executing natural language instructions across diverse tasks and environments. However, they remain largely data-driven and lack formal guarantees on safety and satisfaction of time-dependent specifications during deployment. In practice, robots often need to comply with operational constraints involving rich spatio-temporal requirements such as time-bounded goal visits, sequential objectives, and persistent safety conditions. In this work, we propose a specification-aware action distribution optimization framework that enforces a broad class of Signal Temporal Logic (STL) constraints during execution of a pretrained robotics foundation model without modifying its parameters. At each decision step, the method computes a minimally modified action distribution that satisfies a hard STL feasibility constraint by reasoning over the remaining horizon using forward dynamics propagation. We validate the proposed framework in simulation using a state-of-the-art robotics foundation model across multiple environments and complex specifications.",
    "dateHTTP": 200,
    "date": "2026-03-19T02:44:54.000Z",
    "created": "2026-03-19T02:44:54.000Z",
    "dateTitle": [
      {
        "title": "Specification-Aware Distribution Shaping for Robotics Foundation Models"
      }
    ]
  },
  {
    "id": "17965",
    "status": 200,
    "title": "Title: LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition",
    "author": "Authors: Vlad-Constantin Lungu-Stan , Ionut Mironica , Mariana-Iuliana Georgescu",
    "abstract": "Abstract: Media design layer generation enables the creation of fully editable, layered design documents such as posters, flyers, and logos using only natural language prompts. Existing methods either restrict outputs to a fixed number of layers or require each layer to contain only spatially continuous regions, causing the layer count to scale linearly with design complexity. We propose LaDe (Layered Media Design), a latent diffusion framework that generates a flexible number of semantically meaningful layers. LaDe combines three components: an LLM-based prompt expander that transforms a short user intent into structured per-layer descriptions that guide the generation, a Latent Diffusion Transformer with a 4D RoPE positional encoding mechanism that jointly generates the full media design and its constituent RGBA layers, and an RGBA VAE that decodes each layer with full alpha-channel support. By conditioning on layer samples during training, our unified framework supports three tasks: text-to-image generation, text-to-layers media design generation, and media design decomposition. We compare LaDe to Qwen-Image-Layered on text-to-layers and image-to-layers tasks on the Crello test set. LaDe outperforms Qwen-Image-Layered in text-to-layers generation by improving text-to-layer alignment, as validated by two VLM-as-a-judge evaluators (GPT-4o mini and Qwen3-VL).",
    "dateHTTP": 200,
    "date": "2026-03-19T02:44:48.000Z",
    "created": "2026-03-19T02:44:48.000Z",
    "dateTitle": [
      {
        "title": "LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition"
      }
    ]
  }
]
```

