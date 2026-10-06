# 本19自然日补查的四限定主题发现入口

执行2026-10-11，Submitted只作发现，不当公开日期；start0/max50，各查询返回title/date，尚非完整题摘或候选/全文队列。三既有D15–17需自然日及先公开核验。

```json
[
  {
    "group": "SYSTEM",
    "url": "https://export.arxiv.org/api/query?search_query=%28cat%3Acs.DC+OR+cat%3Acs.AR+OR+cat%3Acs.PL+OR+cat%3Acs.OS+OR+cat%3Acs.PF%29+AND+submittedDate%3A%5B202603180000+TO+202603182359%5D+AND+%28all%3ALLM+OR+all%3AGPU+OR+all%3ATransformer+OR+all%3Ainference+OR+all%3Atraining%29&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending",
    "status": 200,
    "bytes": 35487,
    "total": "13",
    "returned": 13,
    "entries": [
      {
        "id": "http://arxiv.org/abs/2603.18126v2",
        "title": "A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective",
        "published": "2026-03-18T17:22:37Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17803v1",
        "title": "Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs",
        "published": "2026-03-18T14:59:16Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17800v1",
        "title": "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings",
        "published": "2026-03-18T14:55:52Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18104v6",
        "title": "Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI",
        "published": "2026-03-18T12:36:19Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18102v1",
        "title": "HWE-Bench: Can Language Models Perform Board-level Schematic Designs?",
        "published": "2026-03-18T12:07:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17627v5",
        "title": "The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation",
        "published": "2026-03-18T11:47:15Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17613v1",
        "title": "VeriAgent: A Tool-Integrated Multi-Agent System with Evolving Memory for PPA-Aware RTL Code Generation",
        "published": "2026-03-18T11:25:40Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17456v2",
        "title": "Stage-Aware Communication Scheduling for Disaggregated LLM Serving",
        "published": "2026-03-18T07:53:28Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17435v1",
        "title": "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression",
        "published": "2026-03-18T07:21:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18066v2",
        "title": "A Synthesizable RTL Implementation of Predictive Coding Networks",
        "published": "2026-03-18T03:07:19Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17280v2",
        "title": "The 1/W Law: An Analytical Study of Context-Length Routing Topology and GPU Generation Gains for LLM Inference Energy Efficiency",
        "published": "2026-03-18T02:15:40Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17259v1",
        "title": "AppFlow: Memory Scheduling for Cold Launch of Large Apps on Mobile and Vehicle Systems",
        "published": "2026-03-18T01:35:25Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17230v1",
        "title": "KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference",
        "published": "2026-03-18T00:32:11Z"
      }
    ]
  },
  {
    "group": "MODEL_AGENT",
    "url": "https://export.arxiv.org/api/query?search_query=%28cat%3Acs.CL+OR+cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.IR+OR+cat%3Acs.MA%29+AND+submittedDate%3A%5B202603180000+TO+202603182359%5D+AND+%28ti%3Aagent+OR+ti%3Amemory+OR+ti%3Aattention+OR+ti%3Alanguage+OR+ti%3Areasoning+OR+ti%3Atraining%29&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending",
    "status": 200,
    "bytes": 121770,
    "total": "101",
    "returned": 50,
    "entries": [
      {
        "id": "http://arxiv.org/abs/2603.18361v2",
        "title": "Synthetic Data Generation for Training Diversified Commonsense Reasoning Models",
        "published": "2026-03-18T23:58:37Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18353v1",
        "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
        "published": "2026-03-18T23:31:05Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18334v2",
        "title": "Can LLMs Reason Like Automated Theorem Provers for Rust Verification? VCoT-Bench: Evaluating via Verification Chain of Thought",
        "published": "2026-03-18T22:42:20Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18330v1",
        "title": "MemArchitect: A Policy Driven Memory Governance Layer",
        "published": "2026-03-18T22:37:05Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18327v1",
        "title": "Consumer-to-Clinical Language Shifts in Ambient AI Draft Notes and Clinician-Finalized Documentation: A Multi-level Analysis",
        "published": "2026-03-18T22:20:06Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18325v2",
        "title": "Learning to Reason with Curriculum I: Provable Benefits of Autocurriculum",
        "published": "2026-03-18T22:17:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18315v2",
        "title": "DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models for Safe and Deployable Autonomous Driving",
        "published": "2026-03-18T21:55:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18273v1",
        "title": "EDM-ARS: A Domain-Specific Multi-Agent System for Automated Educational Data Mining Research",
        "published": "2026-03-18T20:45:45Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18272v2",
        "title": "Retrieval-Augmented LLM Agents: Learning to Learn from Experience",
        "published": "2026-03-18T20:45:04Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18256v2",
        "title": "MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models",
        "published": "2026-03-18T20:21:04Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18237v1",
        "title": "Gradient-Informed Temporal Sampling Improves Rollout Accuracy in PDE Surrogate Training",
        "published": "2026-03-18T19:45:44Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18197v1",
        "title": "Access Controlled Website Interaction for Agentic AI with Delegated Critical Tasks",
        "published": "2026-03-18T18:49:04Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18178v2",
        "title": "VLM-AutoDrive: Post-Training Vision-Language Models for Safety-Critical Autonomous Driving Events",
        "published": "2026-03-18T18:23:34Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18174v1",
        "title": "Conflict-Free Policy Languages for Probabilistic ML Predicates: A Framework and Case Study with the Semantic Router DSL",
        "published": "2026-03-18T18:14:34Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18168v1",
        "title": "ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit",
        "published": "2026-03-18T18:07:02Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18161v2",
        "title": "How LLMs Distort Our Written Language",
        "published": "2026-03-18T18:01:52Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18002v1",
        "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
        "published": "2026-03-18T17:59:10Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17973v2",
        "title": "TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis",
        "published": "2026-03-18T17:38:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17970v1",
        "title": "Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training",
        "published": "2026-03-18T17:37:31Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17946v1",
        "title": "CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention",
        "published": "2026-03-18T17:18:35Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17942v2",
        "title": "Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing",
        "published": "2026-03-18T17:14:01Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17917v1",
        "title": "Only relative ranks matter in weight-clustered large language models",
        "published": "2026-03-18T16:55:13Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17912v1",
        "title": "Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages",
        "published": "2026-03-18T16:50:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18122v1",
        "title": "Don't Vibe Code, Do Skele-Code: Interactive No-Code Notebooks for Subject Matter Experts to Build Lower-Cost Agentic Workflows",
        "published": "2026-03-18T16:37:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17902v1",
        "title": "Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs",
        "published": "2026-03-18T16:35:12Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.08566v1",
        "title": "Sentiment Classification of Gaza War Headlines: A Comparative Analysis of Large Language Models and Arabic Fine-Tuned BERT Models",
        "published": "2026-03-18T16:19:51Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17884v1",
        "title": "DebugLM: Learning Traceable Training Data Provenance for LLMs",
        "published": "2026-03-18T16:06:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.26718v2",
        "title": "Toward Evaluation Frameworks for Multi-Agent Scientific AI Systems",
        "published": "2026-03-18T16:05:52Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17879v2",
        "title": "Anatomy-Guided Vision-Language Learning with Angular Prototype Separation for Multi-Label Video Capsule Endoscopy Classification Under Class Imbalance",
        "published": "2026-03-18T16:04:50Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17837v5",
        "title": "The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning",
        "published": "2026-03-18T15:30:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18118v1",
        "title": "Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models",
        "published": "2026-03-18T15:28:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17831v1",
        "title": "RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy",
        "published": "2026-03-18T15:26:00Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17829v1",
        "title": "CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents",
        "published": "2026-03-18T15:25:42Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17823v1",
        "title": "Discovering Decoupled Functional Modules in Large Language Models",
        "published": "2026-03-18T15:13:02Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17809v1",
        "title": "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients",
        "published": "2026-03-18T15:03:43Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17787v1",
        "title": "Governed Memory: A Production Architecture for Multi-Agent Workflows",
        "published": "2026-03-18T14:49:31Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17781v1",
        "title": "Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory",
        "published": "2026-03-18T14:45:54Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17775v2",
        "title": "CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution",
        "published": "2026-03-18T14:38:55Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17771v2",
        "title": "Attention Sinks Induce Gradient Sinks: Massive Activations as Gradient Regulators in Transformers",
        "published": "2026-03-18T14:31:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18113v2",
        "title": "VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models",
        "published": "2026-03-18T14:05:51Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.09625v1",
        "title": "Toward Generalized Cross-Lingual Hateful Language Detection with Web-Scale Data and Ensemble LLM Annotations",
        "published": "2026-03-18T13:57:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18112v1",
        "title": "Tula: Optimizing Time, Cost, and Generalization in Distributed Large-Batch Training",
        "published": "2026-03-18T13:56:32Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17729v3",
        "title": "SARE: Sample-wise Adaptive Reasoning for Training-free Fine-grained Visual Recognition",
        "published": "2026-03-18T13:49:27Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.09624v1",
        "title": "Self-Calibrating Language Models via Test-Time Discriminative Distillation",
        "published": "2026-03-18T13:28:50Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.26716v1",
        "title": "FEMBA on the Edge: Physiologically-Aware Pre-Training, Quantization, and Deployment of a Bidirectional Mamba EEG Foundation Model on an Ultra-low Power Microcontroller",
        "published": "2026-03-18T13:23:13Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17694v1",
        "title": "MALLES: A Multi-agent LLMs-based Economic Sandbox with Consumer Preference Alignment",
        "published": "2026-03-18T13:11:09Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17683v1",
        "title": "Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents",
        "published": "2026-03-18T12:59:26Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17680v1",
        "title": "WeatherReasonSeg: A Benchmark for Weather-Aware Reasoning Segmentation in Visual Language Models",
        "published": "2026-03-18T12:57:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17673v2",
        "title": "Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation",
        "published": "2026-03-18T12:52:54Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18104v6",
        "title": "Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI",
        "published": "2026-03-18T12:36:19Z"
      }
    ]
  },
  {
    "group": "MULTIMODAL",
    "url": "https://export.arxiv.org/api/query?search_query=%28cat%3Acs.CV+OR+cat%3Acs.RO%29+AND+submittedDate%3A%5B202603180000+TO+202603182359%5D+AND+%28all%3A%22vision-language%22+OR+all%3A%22world+model%22+OR+all%3A%22foundation+model%22+OR+all%3A%22video+generation%22+OR+all%3AVLA+OR+all%3A%22diffusion+transformer%22%29&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending",
    "status": 200,
    "bytes": 126706,
    "total": "63",
    "returned": 50,
    "entries": [
      {
        "id": "http://arxiv.org/abs/2603.18343v1",
        "title": "VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection",
        "published": "2026-03-18T23:01:12Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18342v1",
        "title": "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
        "published": "2026-03-18T22:52:03Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18336v2",
        "title": "ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics",
        "published": "2026-03-18T22:46:46Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18315v2",
        "title": "DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models for Safe and Deployable Autonomous Driving",
        "published": "2026-03-18T21:55:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18284v1",
        "title": "Offload or Overload: A Platform Measurement Study of Mobile Robotic Manipulation Workloads",
        "published": "2026-03-18T21:05:40Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18282v2",
        "title": "CycleCap: Improving VLMs Captioning Performance via Self-Supervised Cycle Consistency Fine-Tuning",
        "published": "2026-03-18T20:57:31Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18210v1",
        "title": "GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System",
        "published": "2026-03-18T18:59:33Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18202v2",
        "title": "R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation",
        "published": "2026-03-18T18:54:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18178v2",
        "title": "VLM-AutoDrive: Post-Training Vision-Language Models for Safety-Critical Autonomous Driving Events",
        "published": "2026-03-18T18:23:34Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18004v1",
        "title": "Unified Spatio-Temporal Token Scoring for Efficient Video VLMs",
        "published": "2026-03-18T17:59:56Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18002v1",
        "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
        "published": "2026-03-18T17:59:10Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17998v1",
        "title": "The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering",
        "published": "2026-03-18T17:57:53Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17989v1",
        "title": "Versatile Editing of Video Content, Actions, and Dynamics without Training",
        "published": "2026-03-18T17:50:56Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17969v1",
        "title": "Specification-Aware Distribution Shaping for Robotics Foundation Models",
        "published": "2026-03-18T17:36:46Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17965v1",
        "title": "LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition",
        "published": "2026-03-18T17:34:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17920v2",
        "title": "SegFly: A Dataset and 2D-3D-2D Paradigm for Aerial RGB-Thermal Semantic Segmentation at Scale",
        "published": "2026-03-18T16:57:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17889v4",
        "title": "Identity as Presence: Towards Appearance and Voice Personalized Joint Audio-Video Generation",
        "published": "2026-03-18T16:13:48Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17879v2",
        "title": "Anatomy-Guided Vision-Language Learning with Angular Prototype Separation for Multi-Label Video Capsule Endoscopy Classification Under Class Imbalance",
        "published": "2026-03-18T16:04:50Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17859v3",
        "title": "VISER: Visually-Informed System for Enhanced Robustness in Iris Presentation Attack Detection",
        "published": "2026-03-18T15:45:33Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17850v2",
        "title": "ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models",
        "published": "2026-03-18T15:38:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17845v1",
        "title": "Revisiting foundation models for cell instance segmentation",
        "published": "2026-03-18T15:34:42Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17840v1",
        "title": "Video Understanding: From Geometry and Semantics to Unified Models",
        "published": "2026-03-18T15:31:47Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17834v2",
        "title": "Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control",
        "published": "2026-03-18T15:27:17Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17825v2",
        "title": "Steering Video Diffusion Transformers with Massive Activations",
        "published": "2026-03-18T15:24:12Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17813v1",
        "title": "M2P: Improving Visual Foundation Models with Mask-to-Point Weakly-Supervised Learning for Dense Point Tracking",
        "published": "2026-03-18T15:06:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17812v2",
        "title": "ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation",
        "published": "2026-03-18T15:04:57Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17809v1",
        "title": "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients",
        "published": "2026-03-18T15:03:43Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17808v2",
        "title": "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
        "published": "2026-03-18T15:02:19Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17782v1",
        "title": "Exploring parameter-efficient fine-tuning (PEFT) of billion-parameter vision models with QLoRA and DoRA: insights into generalization for limited-data image classification under a 98:1 test-to-train regime",
        "published": "2026-03-18T14:46:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17761v1",
        "title": "Evidence Packing for Cross-Domain Image Deepfake Detection with LVLMs",
        "published": "2026-03-18T14:22:45Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17746v1",
        "title": "Concept-to-Pixel: Prompt-Free Universal Medical Image Segmentation",
        "published": "2026-03-18T14:13:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17735v1",
        "title": "TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos",
        "published": "2026-03-18T14:02:09Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17729v3",
        "title": "SARE: Sample-wise Adaptive Reasoning for Training-free Fine-grained Visual Recognition",
        "published": "2026-03-18T13:49:27Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17715v1",
        "title": "Eye image segmentation using visual and concept prompts with Segment Anything Model 3 (SAM3)",
        "published": "2026-03-18T13:33:46Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17705v1",
        "title": "Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation",
        "published": "2026-03-18T13:23:58Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17693v1",
        "title": "Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos",
        "published": "2026-03-18T13:10:47Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17680v1",
        "title": "WeatherReasonSeg: A Benchmark for Weather-Aware Reasoning Segmentation in Visual Language Models",
        "published": "2026-03-18T12:57:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17675v1",
        "title": "DeepCORO-CLIP: A Multi-View Foundation Model for Comprehensive Coronary Angiography Video-Text Analysis and External Validation",
        "published": "2026-03-18T12:54:24Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17670v1",
        "title": "AgentVLN: Towards Agentic Vision-and-Language Navigation",
        "published": "2026-03-18T12:43:47Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17655v2",
        "title": "Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment",
        "published": "2026-03-18T12:20:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17652v1",
        "title": "VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs",
        "published": "2026-03-18T12:13:30Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17625v1",
        "title": "S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models",
        "published": "2026-03-18T11:42:55Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17605v1",
        "title": "ReLaGS: Relational Language Gaussian Splatting",
        "published": "2026-03-18T11:18:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17576v4",
        "title": "LoGSAM: Parameter-Efficient Cross-Modal Grounding for MRI Segmentation",
        "published": "2026-03-18T10:33:32Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17573v2",
        "title": "HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness",
        "published": "2026-03-18T10:25:08Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17528v2",
        "title": "MM-OVSeg:Multimodal Optical-SAR Fusion for Open-Vocabulary Segmentation in Remote Sensing",
        "published": "2026-03-18T09:34:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17524v2",
        "title": "ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation",
        "published": "2026-03-18T09:28:49Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17520v1",
        "title": "PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation",
        "published": "2026-03-18T09:26:43Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17514v3",
        "title": "Early Intervention for VFM-based Multimodal Medical Image Classification",
        "published": "2026-03-18T09:21:52Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18091v1",
        "title": "Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model",
        "published": "2026-03-18T09:16:20Z"
      }
    ]
  },
  {
    "group": "OPTIMIZATION",
    "url": "https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.CL+OR+cat%3Acs.AI%29+AND+submittedDate%3A%5B202603180000+TO+202603182359%5D+AND+%28all%3A%22policy+optimization%22+OR+all%3A%22post-training%22+OR+all%3AMoE+OR+all%3A%22mixture-of-experts%22+OR+all%3A%22pre-training%22+OR+all%3A%22foundation+model%22%29&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending",
    "status": 200,
    "bytes": 102335,
    "total": "40",
    "returned": 40,
    "entries": [
      {
        "id": "http://arxiv.org/abs/2603.18325v2",
        "title": "Learning to Reason with Curriculum I: Provable Benefits of Autocurriculum",
        "published": "2026-03-18T22:17:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18314v1",
        "title": "Approximate Subgraph Matching with Neural Graph Representations and Reinforcement Learning",
        "published": "2026-03-18T21:53:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18297v2",
        "title": "Path-Constrained Mixture-of-Experts",
        "published": "2026-03-18T21:35:53Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18290v1",
        "title": "CORE: Robust Out-of-Distribution Detection via Confidence and Orthogonal Residual Scoring",
        "published": "2026-03-18T21:23:54Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18284v1",
        "title": "Offload or Overload: A Platform Measurement Study of Mobile Robotic Manipulation Workloads",
        "published": "2026-03-18T21:05:40Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18261v2",
        "title": "LRConv-NeRV: Low Rank Convolution for Efficient Neural Video Compression",
        "published": "2026-03-18T20:31:59Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18178v2",
        "title": "VLM-AutoDrive: Post-Training Vision-Language Models for Safety-Critical Autonomous Driving Events",
        "published": "2026-03-18T18:23:34Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18002v1",
        "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
        "published": "2026-03-18T17:59:10Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17969v1",
        "title": "Specification-Aware Distribution Shaping for Robotics Foundation Models",
        "published": "2026-03-18T17:36:46Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17952v1",
        "title": "Gender Disambiguation in Machine Translation: Diagnostic Evaluation in Decoder-Only Architectures",
        "published": "2026-03-18T17:26:36Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18123v3",
        "title": "Understanding Task Aggregation for Generalizable Ultrasound Foundation Models",
        "published": "2026-03-18T16:43:43Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17891v1",
        "title": "RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference",
        "published": "2026-03-18T16:16:28Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17884v1",
        "title": "DebugLM: Learning Traceable Training Data Provenance for LLMs",
        "published": "2026-03-18T16:06:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17879v2",
        "title": "Anatomy-Guided Vision-Language Learning with Angular Prototype Separation for Multi-Label Video Capsule Endoscopy Classification Under Class Imbalance",
        "published": "2026-03-18T16:04:50Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17829v1",
        "title": "CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents",
        "published": "2026-03-18T15:25:42Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17809v1",
        "title": "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients",
        "published": "2026-03-18T15:03:43Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17808v2",
        "title": "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
        "published": "2026-03-18T15:02:19Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17790v3",
        "title": "The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery",
        "published": "2026-03-18T14:51:15Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.09625v1",
        "title": "Toward Generalized Cross-Lingual Hateful Language Detection with Web-Scale Data and Ensemble LLM Annotations",
        "published": "2026-03-18T13:57:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17715v1",
        "title": "Eye image segmentation using visual and concept prompts with Segment Anything Model 3 (SAM3)",
        "published": "2026-03-18T13:33:46Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.26716v1",
        "title": "FEMBA on the Edge: Physiologically-Aware Pre-Training, Quantization, and Deployment of a Bidirectional Mamba EEG Foundation Model on an Ultra-low Power Microcontroller",
        "published": "2026-03-18T13:23:13Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17694v1",
        "title": "MALLES: A Multi-agent LLMs-based Economic Sandbox with Consumer Preference Alignment",
        "published": "2026-03-18T13:11:09Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17692v1",
        "title": "Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization",
        "published": "2026-03-18T13:09:11Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17685v3",
        "title": "Flow Matching Policy Optimization with Mirror Descent and Entropy Constraints",
        "published": "2026-03-18T13:00:20Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17673v2",
        "title": "Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation",
        "published": "2026-03-18T12:52:54Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17570v1",
        "title": "FoMo X: Modular Explainability Signals for Outlier Detection Foundation Models",
        "published": "2026-03-18T10:22:51Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18095v2",
        "title": "Q-Drift: Quantization-Aware Drift Correction for Diffusion Model Sampling",
        "published": "2026-03-18T10:19:36Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17533v1",
        "title": "A Unified Language Model for Large Scale Search, Recommendation, and Reasoning",
        "published": "2026-03-18T09:42:32Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17527v2",
        "title": "Mirror Descent on Riemannian Manifolds",
        "published": "2026-03-18T09:31:39Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17507v1",
        "title": "QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation",
        "published": "2026-03-18T09:08:28Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18090v2",
        "title": "MOSS-TTS Technical Report",
        "published": "2026-03-18T09:08:06Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18089v1",
        "title": "CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report",
        "published": "2026-03-18T08:58:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17484v2",
        "title": "Learning When to Attend: Conditional Memory Access for Long-Context LLMs",
        "published": "2026-03-18T08:48:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17441v1",
        "title": "AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement",
        "published": "2026-03-18T07:26:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18079v1",
        "title": "SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training",
        "published": "2026-03-18T07:16:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18074v2",
        "title": "Adapting Technical-Service LLM Agents with Latent Logic Augmentation, Robust Noise Reduction, and Hybrid Reward Modeling",
        "published": "2026-03-18T05:01:17Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.06217v1",
        "title": "The End of the Foundation Model Era: Open-Weight Models, Sovereign AI, and Inference as Infrastructure",
        "published": "2026-03-18T04:49:10Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17328v1",
        "title": "A Progressive Visual-Logic-Aligned Framework for Ride-Hailing Adjudication",
        "published": "2026-03-18T03:46:30Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17311v1",
        "title": "Ruyi2.5 Technical Report",
        "published": "2026-03-18T03:13:06Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17301v1",
        "title": "WINFlowNets: Warm-up Integrated Networks Training of Generative Flow Networks for Robotics and Machine Fault Adaptation",
        "published": "2026-03-18T02:55:02Z"
      }
    ]
  }
]
```
