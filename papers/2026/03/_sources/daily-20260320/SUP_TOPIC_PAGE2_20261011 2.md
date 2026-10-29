# 两个原主题查询的标题分页停止

执行2026-10-11。与SUP_ARXIV_TOPIC_TITLES完全相同search_query，start50/max100，只浏览title/date，非完整AB或逐项全文队列。ModelAgent原50+51=101返回全部限定查询；Multimodal原50+13=63。同组内查询停止不等全部arXiv主线召回，cross-group不直接求和。一次手拼未加引号vision-language变体返回68/18仅是有界同义线索，不冒原63完整分页；其新增MCoT-MVS17360/OmniVLN17351/FineViT17326等尚非准入，更不增加全文待办。下面只原精确query结果。

```json
[
  {
    "group": "MODEL_AGENT",
    "url": "https://export.arxiv.org/api/query?search_query=(cat%3Acs.CL%20OR%20cat%3Acs.LG%20OR%20cat%3Acs.AI%20OR%20cat%3Acs.IR%20OR%20cat%3Acs.MA)%20AND%20submittedDate%3A%5B202603180000%20TO%20202603182359%5D%20AND%20(ti%3Aagent%20OR%20ti%3Amemory%20OR%20ti%3Aattention%20OR%20ti%3Alanguage%20OR%20ti%3Areasoning%20OR%20ti%3Atraining)&start=50&max_results=100&sortBy=submittedDate&sortOrder=descending",
    "status": 200,
    "bytes": 123739,
    "total": "101",
    "rows": [
      {
        "id": "http://arxiv.org/abs/2603.17651v1",
        "title": "Anchoring and Rescaling Attention for Semantically Coherent Inbetweening",
        "submitted": "2026-03-18T12:11:02Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18101v1",
        "title": "Training-Only Heterogeneous Image-Patch-Text Graph Supervision for Advancing Few-Shot Learning Adapters",
        "submitted": "2026-03-18T12:03:23Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17639v1",
        "title": "VeriGrey: Greybox Agent Validation",
        "submitted": "2026-03-18T12:00:54Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17624v2",
        "title": "Do Language Models Encode Semantic Relations? Probing and Sparse Feature Analysis",
        "submitted": "2026-03-18T11:42:53Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17621v2",
        "title": "Complementary RL: Towards Efficient Experience-Driven Agent Learning",
        "submitted": "2026-03-18T11:38:01Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17613v1",
        "title": "VeriAgent: A Tool-Integrated Multi-Agent System with Evolving Memory for PPA-Aware RTL Code Generation",
        "submitted": "2026-03-18T11:25:40Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.09621v1",
        "title": "Competing with AI Scientists: Agent-Driven Approach to Astrophysics Research",
        "submitted": "2026-03-18T10:32:20Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17573v2",
        "title": "HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness",
        "submitted": "2026-03-18T10:25:08Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18096v1",
        "title": "A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance",
        "submitted": "2026-03-18T10:23:48Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.22306v1",
        "title": "Memory Bear AI Memory Science Engine for Multimodal Affective Intelligence: A Technical Report",
        "submitted": "2026-03-18T10:23:00Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17533v1",
        "title": "A Unified Language Model for Large Scale Search, Recommendation, and Reasoning",
        "submitted": "2026-03-18T09:42:32Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17524v2",
        "title": "ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation",
        "submitted": "2026-03-18T09:28:49Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17512v4",
        "title": "Language on Demand, Knowledge at Core: Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilinguality",
        "submitted": "2026-03-18T09:19:08Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17507v1",
        "title": "QuantFL: Sustainable Federated Learning for Edge IoT via Pre-Trained Model Quantisation",
        "submitted": "2026-03-18T09:08:28Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17504v1",
        "title": "Inducing Epistemological Humility in Large Language Models: A Targeted SFT Approach to Reducing Hallucination",
        "submitted": "2026-03-18T09:07:39Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17484v2",
        "title": "Learning When to Attend: Conditional Memory Access for Long-Context LLMs",
        "submitted": "2026-03-18T08:48:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17475v1",
        "title": "Humans and transformer LMs: Abstraction drives language learning",
        "submitted": "2026-03-18T08:30:20Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17474v1",
        "title": "Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning",
        "submitted": "2026-03-18T08:28:14Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.08564v2",
        "title": "Attention-Based Sampler for Diffusion Language Models",
        "submitted": "2026-03-18T07:49:13Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17450v2",
        "title": "VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation",
        "submitted": "2026-03-18T07:46:30Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17449v1",
        "title": "TRiMS: Real-Time Tracking of Minimal Sufficient Length for Efficient Reasoning via RL",
        "submitted": "2026-03-18T07:45:39Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.13060v1",
        "title": "Dental-TriageBench: Benchmarking Multimodal Reasoning for Hierarchical Dental Triage",
        "submitted": "2026-03-18T07:43:49Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17445v5",
        "title": "When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Auditing",
        "submitted": "2026-03-18T07:34:51Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17435v1",
        "title": "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression",
        "submitted": "2026-03-18T07:21:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17433v2",
        "title": "The Phasor Transformer: Resolving Attention Bottlenecks on the Unit Circle",
        "submitted": "2026-03-18T07:18:41Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18079v1",
        "title": "SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training",
        "submitted": "2026-03-18T07:16:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17419v1",
        "title": "Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare",
        "submitted": "2026-03-18T06:54:47Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17417v2",
        "title": "Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)",
        "submitted": "2026-03-18T06:50:48Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17399v1",
        "title": "Bootstrapping Coding Agents: The Specification Is the Program",
        "submitted": "2026-03-18T06:21:06Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17392v1",
        "title": "Agentic Cognitive Profiling: Realigning Automated Alzheimer's Disease Detection with Clinical Construct Validity",
        "submitted": "2026-03-18T06:15:35Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17387v1",
        "title": "CRE-T1 Preview Technical Report: Beyond Contrastive Learning for Reasoning-Intensive Retrieval",
        "submitted": "2026-03-18T06:08:59Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17386v1",
        "title": "PJB: A Reasoning-Aware Benchmark for Person-Job Retrieval",
        "submitted": "2026-03-18T06:08:06Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17368v2",
        "title": "Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation",
        "submitted": "2026-03-18T05:21:12Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18074v2",
        "title": "Adapting Technical-Service LLM Agents with Latent Logic Augmentation, Robust Noise Reduction, and Hybrid Reward Modeling",
        "submitted": "2026-03-18T05:01:17Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17357v1",
        "title": "WebPII: Benchmarking Visual PII Detection for Computer-Use Agents",
        "submitted": "2026-03-18T04:41:16Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17333v1",
        "title": "Grid Spatial Understanding: A Dataset for Textual Spatial Reasoning over Grids, Embodied Settings, and Coordinate Structures",
        "submitted": "2026-03-18T03:57:30Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17312v1",
        "title": "Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress",
        "submitted": "2026-03-18T03:13:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17310v2",
        "title": "InfoDensity: Rewarding Information-Dense Traces for Efficient Reasoning",
        "submitted": "2026-03-18T03:11:36Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17309v1",
        "title": "ReLMXEL: Adaptive RL-Based Memory Controller with Explainable Energy and Latency Optimization",
        "submitted": "2026-03-18T03:07:54Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17307v1",
        "title": "Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding",
        "submitted": "2026-03-18T03:04:49Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17305v2",
        "title": "Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations",
        "submitted": "2026-03-18T03:00:42Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17301v1",
        "title": "WINFlowNets: Warm-up Integrated Networks Training of Generative Flow Networks for Robotics and Machine Fault Adaptation",
        "submitted": "2026-03-18T02:55:02Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.18589v1",
        "title": "CentaurTA Studio: A Self-Improving Human-Agent Collaboration System for Thematic Analysis",
        "submitted": "2026-03-18T02:01:28Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.13058v2",
        "title": "KMMMU: Evaluation of Massive Multi-discipline Multimodal Understanding in Korean Language and Context",
        "submitted": "2026-03-18T01:58:14Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.20281v1",
        "title": "On the Fragility of AI Agent Collusion",
        "submitted": "2026-03-18T01:55:13Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17246v2",
        "title": "On the Cone Effect and Modality Gap in Medical Vision-Language Embeddings",
        "submitted": "2026-03-18T01:04:21Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17244v1",
        "title": "Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures",
        "submitted": "2026-03-18T00:59:49Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17234v1",
        "title": "Deployment and Evaluation of an EHR-integrated, Large Language Model-Powered Tool to Triage Surgical Patients",
        "submitted": "2026-03-18T00:36:58Z"
      },
      {
        "id": "http://arxiv.org/abs/2604.08563v1",
        "title": "Temperature-Dependent Performance of Prompting Strategies in Extended Reasoning Large Language Models",
        "submitted": "2026-03-18T00:36:20Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17233v2",
        "title": "Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning",
        "submitted": "2026-03-18T00:35:14Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17231v1",
        "title": "Neuron-Level Emotion Control in Speech-Generative Large Audio-Language Models",
        "submitted": "2026-03-18T00:32:47Z"
      }
    ]
  },
  {
    "group": "MULTIMODAL",
    "url": "https://export.arxiv.org/api/query?search_query=(cat%3Acs.CV%20OR%20cat%3Acs.RO)%20AND%20submittedDate%3A%5B202603180000%20TO%20202603182359%5D%20AND%20(all%3A%22vision-language%22%20OR%20all%3A%22world%20model%22%20OR%20all%3A%22foundation%20model%22%20OR%20all%3A%22video%20generation%22%20OR%20all%3AVLA%20OR%20all%3A%22diffusion%20transformer%22)&start=50&max_results=100&sortBy=submittedDate&sortOrder=descending",
    "status": 200,
    "bytes": 36121,
    "total": "63",
    "rows": [
      {
        "id": "http://arxiv.org/abs/2603.17510v2",
        "title": "Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation",
        "submitted": "2026-03-18T09:14:05Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.18089v1",
        "title": "CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report",
        "submitted": "2026-03-18T08:58:07Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17470v2",
        "title": "VirPro: Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection",
        "submitted": "2026-03-18T08:23:55Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17461v2",
        "title": "AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization",
        "submitted": "2026-03-18T08:07:01Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17441v1",
        "title": "AdaZoom-GUI: Adaptive Zoom-based GUI Grounding with Instruction Refinement",
        "submitted": "2026-03-18T07:26:18Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17437v1",
        "title": "FloorPlan-VLN: A New Paradigm for Floor Plan Guided Vision-Language Navigation",
        "submitted": "2026-03-18T07:22:48Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17398v1",
        "title": "Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion",
        "submitted": "2026-03-18T06:20:57Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17390v2",
        "title": "FMMC: Harnessing the Power of Foundation Models for Accurate Material Classification",
        "submitted": "2026-03-18T06:14:00Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17375v1",
        "title": "Stereo World Model: Camera-Guided Stereo Video Generation",
        "submitted": "2026-03-18T05:42:22Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17374v1",
        "title": "Shot-Aware Frame Sampling for Video Understanding",
        "submitted": "2026-03-18T05:36:57Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17372v1",
        "title": "Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift",
        "submitted": "2026-03-18T05:31:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17312v1",
        "title": "Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress",
        "submitted": "2026-03-18T03:13:29Z"
      },
      {
        "id": "http://arxiv.org/abs/2603.17240v2",
        "title": "GigaWorld-Policy: An Efficient Action-Centered World--Action Model",
        "submitted": "2026-03-18T00:52:02Z"
      }
    ]
  }
]
```
