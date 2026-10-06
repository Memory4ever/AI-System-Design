# Jan10 首批原始 exact-v1 题摘

原源返回缓存；原submitted字段不是public。GDPO/LaST/CounterVid/EARL题摘完整取得，11604本次仅返回头部不可称完整AB。贡献与评分另行独立校准，不从此缓存直接授Evidence。

[2601.05242v1] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (https://arxiv.org/abs/2601.05242v1)
citeturn26775view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.05242v1","lineno":null}); Total lines: 162
L8: [Submitted on 8 Jan 2026]
L9: # Title:GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
L10: 
L11: Authors:cite5†Shih-Yang Liu , cite6†Xin Dong , cite7†Ximing Lu , cite8†Shizhe Diao , cite9†Peter Belcak , cite10†Mingjie Liu , cite11†Min-Hung Chen , cite12†Hongxu Yin , cite13†Yu-Chiang Frank Wang , cite14†Kwang-Ting Cheng , cite15†Yejin Choi , cite16†Jan Kautz , cite17†Pavlo Molchanov L12: View a PDF of the paper titled GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization, by Shih-Yang Liu and 12 other authors
L13: 
L14: cite18†View PDF cite19†HTML (experimental) L15: > Abstract:As language models become increasingly capable, users expect them to provide not only accurate responses but also behaviors aligned with diverse human preferences across a variety of scenarios. To achieve this, Reinforcement learning (RL) pipelines have begun incorporating multiple rewards, each capturing a distinct preference, to guide models toward these desired behaviors.
L16: However, recent work has defaulted to apply Group Relative Policy Optimization (GRPO) under multi-reward setting without examining its suitability. In this paper, we demonstrate that directly applying GRPO to normalize distinct rollout reward combinations causes them to collapse into identical advantage values, reducing the resolution of the training signal and resulting in suboptimal convergence and, in some cases, early training failure.
L17: We then introduce Group reward-Decoupled Normalization Policy Optimization (GDPO), a new policy optimization method to resolve these issues by decoupling the normalization of individual rewards, more faithfully preserving their relative differences and enabling more accurate multi-reward optimization, along with substantially improved training stability.
L18: We compare GDPO with GRPO across three tasks: tool calling, math reasoning, and coding reasoning, evaluating both correctness metrics (accuracy, bug ratio) and constraint adherence metrics (format, length). Across all settings, GDPO consistently outperforms GRPO, demonstrating its effectiveness and generalizability for multi-reward reinforcement learning optimization.
L19: Comments:  | NVIDIA-Tech Report
L20: Subjects:  | Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
L21: Cite as:  | cite20†arXiv:2601.05242 [cs.CL]
L22:    | (or cite21†arXiv:2601.05242v1 [cs.CL] for this version)
L23:    | cite22†https://doi.org/10.48550/arXiv.2601.05242†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Shih-Yang Liu [cite23†view email ]
L27: [v1] Thu, 8 Jan 2026 18:59:24 UTC (1,948 KB)
L28: 
L29: Full-text links:
L30: 
L31: ## Access Paper:
L32: 
L33: View a PDF of the paper titled GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization, by Shih-Yang Liu and 12 other authors
L34: 
L35:   * cite18†View PDF L36:   * cite19†HTML (experimental) L37:   * cite24†TeX Source L38: 
--------------------------------------------------------------------------------
[2601.05248v1] LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model (https://arxiv.org/abs/2601.05248v1)
citeturn26775view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.05248v1","lineno":null}); Total lines: 162
L8: [Submitted on 8 Jan 2026 (this version), latest version 12 Jun 2026 (cite5†v4 )]
L9: # Title:LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
L10: 
L11: Authors:cite6†Zhuoyang Liu , cite7†Jiaming Liu , cite8†Hao Chen , cite9†Ziyu Guo , cite10†Chengkai Hou , cite11†Chenyang Gu , cite12†Jiale Yu , cite13†Xiangju Mi , cite14†Renrui Zhang , cite15†Zhengping Che , cite16†Jian Tang , cite17†Pheng-Ann Heng , cite18†Shanghang Zhang L12: 
L13: View a PDF of the paper titled LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model, by Zhuoyang Liu and 12 other authors
L14: cite19†View PDF cite20†HTML (experimental) L15: > Abstract:Vision-Language-Action (VLA) models have recently demonstrated strong generalization capabilities in robotic manipulation. Some existing VLA approaches attempt to improve action accuracy by explicitly generating linguistic reasoning traces or future visual observations before action execution. However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation.
L16: Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes. To mitigate these limitations, we propose LaST$_0$, a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to verbalize.
L17: Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to enable temporally consistent implicit reasoning trajectories.
L18: Furthermore, LaST$_0$ adopts a dual-system architecture implemented via a Mixture-of-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on robotics-oriented latent representations. To facilitate coordination, LaST$_0$ is trained with heterogeneous operation frequencies, enabling adaptive switching between reasoning and action inference rates during deployment.
L19: Across ten simulated and six real-world manipulation tasks, LaST$_0$ improves mean success rates by 8% and 13% over prior VLA methods, respectively, while achieving substantially faster inference. Project website: cite21†this https URL†sites.google.com L20: Subjects:  | Robotics (cs.RO)
L21: Cite as:  | cite22†arXiv:2601.05248 [cs.RO]
L22:    | (or cite23†arXiv:2601.05248v1 [cs.RO] for this version)
L23:    | cite24†https://doi.org/10.48550/arXiv.2601.05248†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Zhuoyang Liu [cite25†view email ]
L27: [v1] Thu, 8 Jan 2026 18:59:53 UTC (5,590 KB)
L28: cite26†[v2] Mon, 2 Feb 2026 08:46:04 UTC (5,768 KB)
L29: cite27†[v3] Mon, 30 Mar 2026 06:38:36 UTC (5,768 KB)
L30: cite5†[v4] Fri, 12 Jun 2026 22:39:30 UTC (6,037 KB)
L31: 
L32: Full-text links:
L33: ## Access Paper:
L34: 
L35: View a PDF of the paper titled LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model, by Zhuoyang Liu and 12 other authors
--------------------------------------------------------------------------------
[2601.04778v1] CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models (https://arxiv.org/abs/2601.04778v1)
citeturn26775view2 [wordlim: 200] Crawled: 2 weeks ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.04778v1","lineno":null}); Total lines: 162
L8: [Submitted on 8 Jan 2026 (this version), latest version 27 Aug 2026 (cite5†v2 )]
L9: # Title:CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models
L10: 
L11: Authors:cite6†Tobia Poppi , cite7†Burak Uzkent , cite8†Amanmeet Garg , cite9†Lucas Porto , cite10†Garin Kessler , cite11†Yezhou Yang , cite12†Marcella Cornia , cite13†Lorenzo Baraldi , cite14†Rita Cucchiara , cite15†Florian Schiffers L12: View a PDF of the paper titled CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models, by Tobia Poppi and 9 other authors
L13: 
L14: cite16†View PDF cite17†HTML (experimental) L15: > Abstract:Video-language models (VLMs) achieve strong multimodal understanding but remain prone to hallucinations, especially when reasoning about actions and temporal order. Existing mitigation strategies, such as textual filtering or random video perturbations, often fail to address the root cause: over-reliance on language priors rather than fine-grained visual dynamics.
L16: We propose a scalable framework for counterfactual video generation that synthesizes videos differing only in actions or temporal structure while preserving scene context. Our pipeline combines multimodal LLMs for action proposal and editing guidance with diffusion-based image and video models to generate semantic hard negatives at scale. Using this framework, we build CounterVid, a synthetic dataset of ~26k preference pairs targeting action recognition and temporal reasoning.
L17: We further introduce MixDPO, a unified Direct Preference Optimization approach that jointly leverages textual and visual preferences. Fine-tuning Qwen2.5-VL with MixDPO yields consistent improvements, notably in temporal ordering, and transfers effectively to standard video hallucination benchmarks. Code and models will be made publicly available.
L18: Subjects:  | Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Multimedia (cs.MM)
L19: Cite as:  | cite18†arXiv:2601.04778 [cs.CV]
L20:    | (or cite19†arXiv:2601.04778v1 [cs.CV] for this version)
L21:    | cite20†https://doi.org/10.48550/arXiv.2601.04778†doi.org arXiv-issued DOI via DataCite
L22: ## Submission history
L23: 
L24: From: Tobia Poppi [cite21†view email ]
L25: [v1] Thu, 8 Jan 2026 10:03:07 UTC (18,785 KB)
L26: cite5†[v2] Thu, 27 Aug 2026 14:40:06 UTC (1,420 KB)
L27: 
L28: Full-text links:
L29: 
L30: ## Access Paper:
L31: 
L32: View a PDF of the paper titled CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models, by Tobia Poppi and 9 other authors
L33: 
L34:   * cite16†View PDF L35:   * cite17†HTML (experimental) L36:   * cite22†TeX Source L37: 
--------------------------------------------------------------------------------
[2601.05205v1] EARL: Energy-Aware Optimization of Liquid State Machines for Pervasive AI (https://arxiv.org/abs/2601.05205v1)
citeturn26775view3 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.05205v1","lineno":null}); Total lines: 165
L8: [Submitted on 8 Jan 2026]
L9: # Title:EARL: Energy-Aware Optimization of Liquid State Machines for Pervasive AI
L10: 
L11: Authors:cite5†Zain Iqbal , cite6†Lorenzo Valerio L12: 
L13: View a PDF of the paper titled EARL: Energy-Aware Optimization of Liquid State Machines for Pervasive AI, by Zain Iqbal and 1 other authors
L14: 
L15: cite7†View PDF cite8†HTML (experimental) L16: > Abstract:Pervasive AI increasingly depends on on-device learning systems that deliver low-latency and energy-efficient computation under strict resource constraints. Liquid State Machines (LSMs) offer a promising approach for low-power temporal processing in pervasive and neuromorphic systems, but their deployment remains challenging due to high hyperparameter sensitivity and the computational cost of traditional optimization methods that ignore energy constraints.
L17: This work presents EARL, an energy-aware reinforcement learning framework that integrates Bayesian optimization with an adaptive reinforcement learning based selection policy to jointly optimize accuracy and energy consumption. EARL employs surrogate modeling for global exploration, reinforcement learning for dynamic candidate prioritization, and an early termination mechanism to eliminate redundant evaluations, substantially reducing computational overhead.
L18: Experiments on three benchmark datasets demonstrate that EARL achieves 6 to 15 percent higher accuracy, 60 to 80 percent lower energy consumption, and up to an order of magnitude reduction in optimization time compared to leading hyperparameter tuning frameworks. These results highlight the effectiveness of energy-aware adaptive search in improving the efficiency and scalability of LSMs for resource-constrained on-device AI applications.
L19: Comments:  | 6 pages, 9 figures, 2 Tables, conference [Submitted in PerConAI-2026]
L20: Subjects:  | Machine Learning (cs.LG); Performance (cs.PF)
L21: Cite as:  | cite9†arXiv:2601.05205 [cs.LG]
L22:    | (or cite10†arXiv:2601.05205v1 [cs.LG] for this version)
L23:    | cite11†https://doi.org/10.48550/arXiv.2601.05205†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Zain Iqbal [cite12†view email ]
--------------------------------------------------------------------------------
[2601.11604v1] Hindsight Preference Replay Improves Preference-Conditioned Multi-Objective Reinforcement Learning (https://arxiv.org/abs/2601.11604v1)
citeturn26775view4 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.11604v1","lineno":null}); Total lines: 164

