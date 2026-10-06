# 03/19 四主题有限发现

Submitted字段仅作发现，不是first-public证明。start0/max_results100，submittedDate升序，Mar17T18Z→Mar18T18Z；4返回79/76/40/16，跨分类178去重标题，全部标题实际浏览。下方查询与原始元值可复查；178不是候选、全部题摘队列或当窗新论文数量。

```json
{
  "url": "https://export.arxiv.org/api/query?search_query=(cat%3Acs.CL%20OR%20cat%3Acs.LG%20OR%20cat%3Acs.AI)%20AND%20(ti%3A%22language%20model%22%20OR%20ti%3ALLM%20OR%20ti%3ATransformer%20OR%20ti%3Aattention%20OR%20ti%3A%22expert%20routing%22%20OR%20ti%3A%22post-training%22)%20AND%20submittedDate%3A%5B202603171800%20TO%20202603181800%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
  "bytes": 195246,
  "total": "79",
  "rows": [
    {
      "id": "http://arxiv.org/abs/2603.17017v1",
      "title": "LLM NL2SQL Robustness: Surface Noise vs. Linguistic Variation in Traditional and Agentic Settings",
      "published": "2026-03-17T18:02:04Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17019v2",
      "title": "Transformers Can Learn Rules They've Never Seen: Proof of Computation Beyond Interpolation",
      "published": "2026-03-17T18:02:28Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17056v1",
      "title": "DesertFormer: Transformer-Based Semantic Segmentation for Off-Road Desert Terrain Classification in Autonomous Navigation Systems",
      "published": "2026-03-17T18:42:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17063v1",
      "title": "Transformers are Bayesian Networks",
      "published": "2026-03-17T18:50:13Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17067v1",
      "title": "Evaluating Ill-Defined Tasks in Large Language Models",
      "published": "2026-03-17T18:52:47Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.26707v1",
      "title": "The Cognitive Divergence: AI Context Windows, Human Attention Decline, and the Delegation Feedback Loop",
      "published": "2026-03-17T18:53:45Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17094v2",
      "title": "Evaluating LLM-Simulated Conversations in Modeling Inconsistent and Uncollaborative Behaviors in Human Social Interaction",
      "published": "2026-03-17T19:29:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17102v1",
      "title": "Knowledge Localization in Mixture-of-Experts LLMs Using Cross-Lingual Inconsistency",
      "published": "2026-03-17T19:48:44Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17111v1",
      "title": "Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model Ensembles",
      "published": "2026-03-17T20:08:01Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17123v1",
      "title": "Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive Defensive Framework",
      "published": "2026-03-17T20:32:06Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.06216v1",
      "title": "Blending Human and LLM Expertise to Detect Hallucinations and Omissions in Mental Health Chatbot Responses",
      "published": "2026-03-17T21:13:19Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17145v2",
      "title": "REAL: Regression-Aware Reinforcement Learning for LLM-as-a-Judge",
      "published": "2026-03-17T21:19:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.26710v1",
      "title": "Agentic AI for Human Resources: LLM-Driven Candidate Assessment",
      "published": "2026-03-17T21:32:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17169v1",
      "title": "How Clued up are LLMs? Evaluating Multi-Step Deductive Reasoning in a Text-Based Game Environment",
      "published": "2026-03-17T22:01:11Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17171v1",
      "title": "Exploiting the English Grammar Profile for L2 grammatical analysis with LLMs",
      "published": "2026-03-17T22:06:00Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17172v1",
      "title": "Noise-Response Calibration: A Causal Intervention Protocol for LLM-Judges",
      "published": "2026-03-17T22:08:06Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17173v1",
      "title": "Generalist Multimodal LLMs Gain Biometric Expertise via Human Salience",
      "published": "2026-03-17T22:08:37Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17174v2",
      "title": "Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning",
      "published": "2026-03-17T22:08:45Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17191v1",
      "title": "Tabular LLMs for Interpretable Few-Shot Alzheimer's Disease Prediction with Multimodal Biomedical Data",
      "published": "2026-03-17T22:43:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17198v2",
      "title": "Structural Abstraction as an Inductive Bias for Non-Stationary Language Model Training",
      "published": "2026-03-17T22:59:13Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17217v1",
      "title": "Anonymous-by-Construction: An LLM-Driven Framework for Privacy-Preserving Text",
      "published": "2026-03-17T23:46:15Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17218v2",
      "title": "Alignment Makes Language Models Normative, Not Descriptive",
      "published": "2026-03-17T23:47:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17219v2",
      "title": "SA-CycleGAN-2.5D: Self-Attention CycleGAN with Tri-Planar Context for Multi-Site MRI Harmonization",
      "published": "2026-03-17T23:49:46Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17220v1",
      "title": "TharuChat: Bootstrapping Large Language Models for a Low-Resource Language via Synthetic Data and Human Validation",
      "published": "2026-03-17T23:57:47Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17231v1",
      "title": "Neuron-Level Emotion Control in Speech-Generative Large Audio-Language Models",
      "published": "2026-03-18T00:32:47Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.08563v1",
      "title": "Temperature-Dependent Performance of Prompting Strategies in Extended Reasoning Large Language Models",
      "published": "2026-03-18T00:36:20Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17234v1",
      "title": "Deployment and Evaluation of an EHR-integrated, Large Language Model-Powered Tool to Triage Surgical Patients",
      "published": "2026-03-18T00:36:58Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18062v2",
      "title": "S3T-Former: A Purely Spike-Driven State-Space Topology Transformer for Skeleton Action Recognition",
      "published": "2026-03-18T02:09:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.22305v1",
      "title": "CN-Buzz2Portfolio: A Chinese-Market Dataset and Benchmark for LLM-Based Macro and Sector Asset Allocation from Daily Trending Financial News",
      "published": "2026-03-18T02:31:28Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17312v1",
      "title": "Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress",
      "published": "2026-03-18T03:13:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18074v2",
      "title": "Adapting Technical-Service LLM Agents with Latent Logic Augmentation, Robust Noise Reduction, and Hybrid Reward Modeling",
      "published": "2026-03-18T05:01:17Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17432v3",
      "title": "Argument Reconstruction as Supervision for Critical Thinking in LLMs",
      "published": "2026-03-18T07:17:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17433v2",
      "title": "The Phasor Transformer: Resolving Attention Bottlenecks on the Unit Circle",
      "published": "2026-03-18T07:18:41Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17435v1",
      "title": "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression",
      "published": "2026-03-18T07:21:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17450v2",
      "title": "VLM2Rec: Resolving Modality Collapse in Vision-Language Model Embedders for Multimodal Sequential Recommendation",
      "published": "2026-03-18T07:46:30Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.08564v2",
      "title": "Attention-Based Sampler for Diffusion Language Models",
      "published": "2026-03-18T07:49:13Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17468v1",
      "title": "Efficient Soft Actor-Critic with LLM-Based Action-Level Guidance for Continuous Control",
      "published": "2026-03-18T08:22:31Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17474v1",
      "title": "Revisiting Cross-Attention Mechanisms: Leveraging Beneficial Noise for Domain-Adaptive Learning",
      "published": "2026-03-18T08:28:14Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17475v1",
      "title": "Humans and transformer LMs: Abstraction drives language learning",
      "published": "2026-03-18T08:30:20Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17484v2",
      "title": "Learning When to Attend: Conditional Memory Access for Long-Context LLMs",
      "published": "2026-03-18T08:48:18Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17504v1",
      "title": "Inducing Epistemological Humility in Large Language Models: A Targeted SFT Approach to Reducing Hallucination",
      "published": "2026-03-18T09:07:39Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17512v4",
      "title": "Language on Demand, Knowledge at Core: Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilinguality",
      "published": "2026-03-18T09:19:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.09620v1",
      "title": "LLM Nepotism in Organizational Governance",
      "published": "2026-03-18T09:35:25Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17532v1",
      "title": "Anisotropic Permeability Tensor Prediction from Porous Media Microstructure via Physics-Informed Progressive Transfer Learning with Hybrid CNN-Transformer",
      "published": "2026-03-18T09:41:01Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17533v1",
      "title": "A Unified Language Model for Large Scale Search, Recommendation, and Reasoning",
      "published": "2026-03-18T09:42:32Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17558v3",
      "title": "Zipper-LoRA: Dynamic Parameter Decoupling for Speech-LLM based Multilingual Speech Recognition",
      "published": "2026-03-18T10:04:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17566v2",
      "title": "KA2L: A Knowledge-Aware Active Learning Framework for LLMs",
      "published": "2026-03-18T10:16:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17569v1",
      "title": "Gaussian Process Limit Reveals Structural Benefits of Graph Transformers",
      "published": "2026-03-18T10:18:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17588v2",
      "title": "From Isolated Scoring to Collaborative Ranking: A Comparison-Native Framework for LLM-Based Paper Evaluation",
      "published": "2026-03-18T10:55:02Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17624v2",
      "title": "Do Language Models Encode Semantic Relations? Probing and Sparse Feature Analysis",
      "published": "2026-03-18T11:42:53Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17651v1",
      "title": "Anchoring and Rescaling Attention for Semantically Coherent Inbetweening",
      "published": "2026-03-18T12:11:02Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17673v2",
      "title": "Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation",
      "published": "2026-03-18T12:52:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17680v1",
      "title": "WeatherReasonSeg: A Benchmark for Weather-Aware Reasoning Segmentation in Visual Language Models",
      "published": "2026-03-18T12:57:18Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17683v1",
      "title": "Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents",
      "published": "2026-03-18T12:59:26Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17692v1",
      "title": "Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization",
      "published": "2026-03-18T13:09:11Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17694v1",
      "title": "MALLES: A Multi-agent LLMs-based Economic Sandbox with Consumer Preference Alignment",
      "published": "2026-03-18T13:11:09Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.09624v1",
      "title": "Self-Calibrating Language Models via Test-Time Discriminative Distillation",
      "published": "2026-03-18T13:28:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.09625v1",
      "title": "Toward Generalized Cross-Lingual Hateful Language Detection with Web-Scale Data and Ensemble LLM Annotations",
      "published": "2026-03-18T13:57:23Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18113v2",
      "title": "VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models",
      "published": "2026-03-18T14:05:51Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17771v2",
      "title": "Attention Sinks Induce Gradient Sinks: Massive Activations as Gradient Regulators in Transformers",
      "published": "2026-03-18T14:31:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17781v1",
      "title": "Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory",
      "published": "2026-03-18T14:45:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18115v1",
      "title": "LLM-Augmented Computational Phenotyping of Long Covid",
      "published": "2026-03-18T15:02:05Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17809v1",
      "title": "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients",
      "published": "2026-03-18T15:03:43Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17811v1",
      "title": "Dropout Robustness and Cognitive Profiling of Transformer Models via Stochastic Inference",
      "published": "2026-03-18T15:04:26Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17823v1",
      "title": "Discovering Decoupled Functional Modules in Large Language Models",
      "published": "2026-03-18T15:13:02Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17831v1",
      "title": "RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy",
      "published": "2026-03-18T15:26:00Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18118v1",
      "title": "Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models",
      "published": "2026-03-18T15:28:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17839v4",
      "title": "How do LLMs Compute Verbal Confidence",
      "published": "2026-03-18T15:31:43Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17872v2",
      "title": "Mitigating LLM Hallucinations through Domain-Grounded Tiered Retrieval",
      "published": "2026-03-18T15:59:30Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17884v1",
      "title": "DebugLM: Learning Traceable Training Data Provenance for LLMs",
      "published": "2026-03-18T16:06:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17891v1",
      "title": "RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference",
      "published": "2026-03-18T16:16:28Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.08566v1",
      "title": "Sentiment Classification of Gaza War Headlines: A Comparative Analysis of Large Language Models and Arabic Fine-Tuned BERT Models",
      "published": "2026-03-18T16:19:51Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17893v2",
      "title": "scicode-lint: Detecting Methodology Bugs in Scientific Python Code with LLM-Generated Patterns",
      "published": "2026-03-18T16:23:02Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17912v1",
      "title": "Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages",
      "published": "2026-03-18T16:50:23Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17915v2",
      "title": "IndicSafe: A Benchmark for Evaluating Multilingual LLM Safety in South Asia",
      "published": "2026-03-18T16:54:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17917v1",
      "title": "Only relative ranks matter in weight-clustered large language models",
      "published": "2026-03-18T16:55:13Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17946v1",
      "title": "CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention",
      "published": "2026-03-18T17:18:35Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17970v1",
      "title": "Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training",
      "published": "2026-03-18T17:37:31Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18002v1",
      "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
      "published": "2026-03-18T17:59:10Z"
    }
  ]
}
```

```json
{
  "url": "https://export.arxiv.org/api/query?search_query=(cat%3Acs.CL%20OR%20cat%3Acs.AI%20OR%20cat%3Acs.IR%20OR%20cat%3Acs.MA)%20AND%20(ti%3Aagent%20OR%20ti%3Amemory%20OR%20ti%3Aretrieval%20OR%20ti%3Areasoning%20OR%20ti%3Aalignment)%20AND%20submittedDate%3A%5B202603171800%20TO%20202603181800%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
  "bytes": 189577,
  "total": "76",
  "rows": [
    {
      "id": "http://arxiv.org/abs/2603.17017v1",
      "title": "LLM NL2SQL Robustness: Surface Noise vs. Linguistic Variation in Traditional and Agentic Settings",
      "published": "2026-03-17T18:02:04Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17024v2",
      "title": "HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning",
      "published": "2026-03-17T18:04:58Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17070v2",
      "title": "Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts",
      "published": "2026-03-17T18:57:26Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17104v1",
      "title": "When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents",
      "published": "2026-03-17T19:53:35Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17112v2",
      "title": "Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching",
      "published": "2026-03-17T20:10:16Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17150v1",
      "title": "Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents",
      "published": "2026-03-17T21:28:59Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.26710v1",
      "title": "Agentic AI for Human Resources: LLM-Driven Candidate Assessment",
      "published": "2026-03-17T21:32:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.20279v1",
      "title": "Learning Communication Between Heterogeneous Agents in Multi-Agent Reinforcement Learning for Autonomous Cyber Defence",
      "published": "2026-03-17T21:38:39Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17169v1",
      "title": "How Clued up are LLMs? Evaluating Multi-Step Deductive Reasoning in a Text-Based Game Environment",
      "published": "2026-03-17T22:01:11Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17170v2",
      "title": "Beyond OAuth: Task-Scoped Authorization for AI Agents via Natural Language Slices",
      "published": "2026-03-17T22:05:03Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17176v1",
      "title": "Towards Unsupervised Adversarial Document Detection in Retrieval Augmented Generation Systems",
      "published": "2026-03-17T22:09:37Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17179v2",
      "title": "Ablation Study of a Fairness Auditing Agentic System for Bias Mitigation in Early-Onset Colorectal Cancer Detection",
      "published": "2026-03-17T22:13:22Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17199v1",
      "title": "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
      "published": "2026-03-17T23:03:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17204v1",
      "title": "CODMAS: A Dialectic Multi-Agent Collaborative Framework for Structured RTL Optimization",
      "published": "2026-03-17T23:10:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17205v3",
      "title": "OPERA: Online Data Pruning for Efficient Retrieval Model Adaptation",
      "published": "2026-03-17T23:11:45Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17208v1",
      "title": "SYMDIREC: A Neuro-Symbolic Divide-Retrieve-Conquer Framework for Enhanced RTL Synthesis and Summarization",
      "published": "2026-03-17T23:15:24Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17216v2",
      "title": "ML-AutoResearch: Training Machine Learning Research Agents with Automatically Generated Environments",
      "published": "2026-03-17T23:43:16Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17218v2",
      "title": "Alignment Makes Language Models Normative, Not Descriptive",
      "published": "2026-03-17T23:47:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17233v2",
      "title": "Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning",
      "published": "2026-03-18T00:35:14Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.08563v1",
      "title": "Temperature-Dependent Performance of Prompting Strategies in Extended Reasoning Large Language Models",
      "published": "2026-03-18T00:36:20Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17244v1",
      "title": "Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures",
      "published": "2026-03-18T00:59:49Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.20281v1",
      "title": "On the Fragility of AI Agent Collusion",
      "published": "2026-03-18T01:55:13Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.18589v1",
      "title": "CentaurTA Studio: A Self-Improving Human-Agent Collaboration System for Thematic Analysis",
      "published": "2026-03-18T02:01:28Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17305v2",
      "title": "Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations",
      "published": "2026-03-18T03:00:42Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17307v1",
      "title": "Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding",
      "published": "2026-03-18T03:04:49Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17309v1",
      "title": "ReLMXEL: Adaptive RL-Based Memory Controller with Explainable Energy and Latency Optimization",
      "published": "2026-03-18T03:07:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17310v2",
      "title": "InfoDensity: Rewarding Information-Dense Traces for Efficient Reasoning",
      "published": "2026-03-18T03:11:36Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17312v1",
      "title": "Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress",
      "published": "2026-03-18T03:13:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17328v1",
      "title": "A Progressive Visual-Logic-Aligned Framework for Ride-Hailing Adjudication",
      "published": "2026-03-18T03:46:30Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17333v1",
      "title": "Grid Spatial Understanding: A Dataset for Textual Spatial Reasoning over Grids, Embodied Settings, and Coordinate Structures",
      "published": "2026-03-18T03:57:30Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17357v1",
      "title": "WebPII: Benchmarking Visual PII Detection for Computer-Use Agents",
      "published": "2026-03-18T04:41:16Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18074v2",
      "title": "Adapting Technical-Service LLM Agents with Latent Logic Augmentation, Robust Noise Reduction, and Hybrid Reward Modeling",
      "published": "2026-03-18T05:01:17Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17368v2",
      "title": "Towards Safer Large Reasoning Models by Promoting Safety Decision-Making before Chain-of-Thought Generation",
      "published": "2026-03-18T05:21:12Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17386v1",
      "title": "PJB: A Reasoning-Aware Benchmark for Person-Job Retrieval",
      "published": "2026-03-18T06:08:06Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17387v1",
      "title": "CRE-T1 Preview Technical Report: Beyond Contrastive Learning for Reasoning-Intensive Retrieval",
      "published": "2026-03-18T06:08:59Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17392v1",
      "title": "Agentic Cognitive Profiling: Realigning Automated Alzheimer's Disease Detection with Clinical Construct Validity",
      "published": "2026-03-18T06:15:35Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17417v2",
      "title": "Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)",
      "published": "2026-03-18T06:50:48Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17419v1",
      "title": "Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare",
      "published": "2026-03-18T06:54:47Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18079v1",
      "title": "SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training",
      "published": "2026-03-18T07:16:18Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17445v5",
      "title": "When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Auditing",
      "published": "2026-03-18T07:34:51Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.13060v1",
      "title": "Dental-TriageBench: Benchmarking Multimodal Reasoning for Hierarchical Dental Triage",
      "published": "2026-03-18T07:43:49Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17449v1",
      "title": "TRiMS: Real-Time Tracking of Minimal Sufficient Length for Efficient Reasoning via RL",
      "published": "2026-03-18T07:45:39Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17484v2",
      "title": "Learning When to Attend: Conditional Memory Access for Long-Context LLMs",
      "published": "2026-03-18T08:48:18Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.20286v1",
      "title": "Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach",
      "published": "2026-03-18T09:09:52Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17533v1",
      "title": "A Unified Language Model for Large Scale Search, Recommendation, and Reasoning",
      "published": "2026-03-18T09:42:32Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17540v1",
      "title": "Deploying Semantic ID-based Generative Retrieval for Large-Scale Podcast Discovery at Spotify",
      "published": "2026-03-18T09:46:10Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.22306v1",
      "title": "Memory Bear AI Memory Science Engine for Multimodal Affective Intelligence: A Technical Report",
      "published": "2026-03-18T10:23:00Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18096v1",
      "title": "A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance",
      "published": "2026-03-18T10:23:48Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.09621v1",
      "title": "Competing with AI Scientists: Agent-Driven Approach to Astrophysics Research",
      "published": "2026-03-18T10:32:20Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17580v1",
      "title": "Negation is Not Semantic: Diagnosing Dense Retrieval Failure Modes for Trade-offs in Contradiction-Aware Biomedical QA",
      "published": "2026-03-18T10:35:44Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17613v1",
      "title": "VeriAgent: A Tool-Integrated Multi-Agent System with Evolving Memory for PPA-Aware RTL Code Generation",
      "published": "2026-03-18T11:25:40Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17621v2",
      "title": "Complementary RL: Towards Efficient Experience-Driven Agent Learning",
      "published": "2026-03-18T11:38:01Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17639v1",
      "title": "VeriGrey: Greybox Agent Validation",
      "published": "2026-03-18T12:00:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17655v2",
      "title": "Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment",
      "published": "2026-03-18T12:20:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17673v2",
      "title": "Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation",
      "published": "2026-03-18T12:52:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17677v2",
      "title": "Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models",
      "published": "2026-03-18T12:54:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17680v1",
      "title": "WeatherReasonSeg: A Benchmark for Weather-Aware Reasoning Segmentation in Visual Language Models",
      "published": "2026-03-18T12:57:18Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17683v1",
      "title": "Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents",
      "published": "2026-03-18T12:59:26Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17694v1",
      "title": "MALLES: A Multi-agent LLMs-based Economic Sandbox with Consumer Preference Alignment",
      "published": "2026-03-18T13:11:09Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17729v3",
      "title": "SARE: Sample-wise Adaptive Reasoning for Training-free Fine-grained Visual Recognition",
      "published": "2026-03-18T13:49:27Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18113v2",
      "title": "VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models",
      "published": "2026-03-18T14:05:51Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17765v1",
      "title": "Grounded Multimodal Retrieval-Augmented Drafting of Radiology Impressions Using Case-Based Similarity Search",
      "published": "2026-03-18T14:25:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17775v2",
      "title": "CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution",
      "published": "2026-03-18T14:38:55Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17781v1",
      "title": "Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory",
      "published": "2026-03-18T14:45:54Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17787v1",
      "title": "Governed Memory: A Production Architecture for Multi-Agent Workflows",
      "published": "2026-03-18T14:49:31Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17808v2",
      "title": "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
      "published": "2026-03-18T15:02:19Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17829v1",
      "title": "CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents",
      "published": "2026-03-18T15:25:42Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17831v1",
      "title": "RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy",
      "published": "2026-03-18T15:26:00Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18118v1",
      "title": "Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models",
      "published": "2026-03-18T15:28:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17837v5",
      "title": "The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning",
      "published": "2026-03-18T15:30:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17872v2",
      "title": "Mitigating LLM Hallucinations through Domain-Grounded Tiered Retrieval",
      "published": "2026-03-18T15:59:30Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.26718v2",
      "title": "Toward Evaluation Frameworks for Multi-Agent Scientific AI Systems",
      "published": "2026-03-18T16:05:52Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17902v1",
      "title": "Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs",
      "published": "2026-03-18T16:35:12Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18122v1",
      "title": "Don't Vibe Code, Do Skele-Code: Interactive No-Code Notebooks for Subject Matter Experts to Build Lower-Cost Agentic Workflows",
      "published": "2026-03-18T16:37:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17973v2",
      "title": "TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis",
      "published": "2026-03-18T17:38:22Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18002v1",
      "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
      "published": "2026-03-18T17:59:10Z"
    }
  ]
}
```

```json
{
  "url": "https://export.arxiv.org/api/query?search_query=(cat%3Acs.CV%20OR%20cat%3Acs.RO%20OR%20cat%3Acs.CL%20OR%20cat%3Acs.LG)%20AND%20(ti%3Amultimodal%20OR%20ti%3A%22world%20model%22%20OR%20ti%3A%22vision%20language%22%20OR%20ti%3AVLA%20OR%20ti%3A%22diffusion%20model%22%20OR%20ti%3A%22diffusion%20transformer%22%20OR%20ti%3A%22speech%20tokenization%22)%20AND%20submittedDate%3A%5B202603171800%20TO%20202603181800%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
  "bytes": 102208,
  "total": "40",
  "rows": [
    {
      "id": "http://arxiv.org/abs/2603.17024v2",
      "title": "HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning",
      "published": "2026-03-17T18:04:58Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17044v2",
      "title": "Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models",
      "published": "2026-03-17T18:26:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17069v2",
      "title": "Edge-Efficient Two-Stream Multimodal Architecture for Non-Intrusive Bathroom Fall Detection",
      "published": "2026-03-17T18:54:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17079v1",
      "title": "ACE-LoRA: Graph-Attentive Context Enhancement for Parameter-Efficient Adaptation of Medical Vision-Language Models",
      "published": "2026-03-17T19:06:33Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17108v2",
      "title": "LLM-Powered Flood Depth Estimation from Social Media Imagery: A Vision-Language Model Framework with Mechanistic Interpretability for Transportation Resilience",
      "published": "2026-03-17T19:59:25Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17111v1",
      "title": "Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model Ensembles",
      "published": "2026-03-17T20:08:01Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17117v1",
      "title": "MosaicMem: Hybrid Spatial Memory for Controllable Video World Models",
      "published": "2026-03-17T20:19:44Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17173v1",
      "title": "Generalist Multimodal LLMs Gain Biometric Expertise via Human Salience",
      "published": "2026-03-17T22:08:37Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17191v1",
      "title": "Tabular LLMs for Interpretable Few-Shot Alzheimer's Disease Prediction with Multimodal Biomedical Data",
      "published": "2026-03-17T22:43:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17246v2",
      "title": "On the Cone Effect and Modality Gap in Medical Vision-Language Embeddings",
      "published": "2026-03-18T01:04:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.13058v2",
      "title": "KMMMU: Evaluation of Massive Multi-discipline Multimodal Understanding in Korean Language and Context",
      "published": "2026-03-18T01:58:14Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17312v1",
      "title": "Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress",
      "published": "2026-03-18T03:13:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17314v2",
      "title": "A Proposal-Free Query-Guided Network for Grounded Multimodal Named Entity Recognition",
      "published": "2026-03-18T03:16:41Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17375v1",
      "title": "Stereo World Model: Camera-Guided Stereo Video Generation",
      "published": "2026-03-18T05:42:22Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17426v2",
      "title": "SHIFT: Motion Alignment in Video Diffusion Models with Adversarial Hybrid Fine-Tuning",
      "published": "2026-03-18T07:04:02Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17437v1",
      "title": "FloorPlan-VLN: A New Paradigm for Floor Plan Guided Vision-Language Navigation",
      "published": "2026-03-18T07:22:48Z"
    },
    {
      "id": "http://arxiv.org/abs/2604.13060v1",
      "title": "Dental-TriageBench: Benchmarking Multimodal Reasoning for Hierarchical Dental Triage",
      "published": "2026-03-18T07:43:49Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17476v1",
      "title": "UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models",
      "published": "2026-03-18T08:30:31Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18089v1",
      "title": "CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report",
      "published": "2026-03-18T08:58:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18091v1",
      "title": "Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model",
      "published": "2026-03-18T09:16:20Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17514v3",
      "title": "Early Intervention for VFM-based Multimodal Medical Image Classification",
      "published": "2026-03-18T09:21:52Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17524v1",
      "title": "KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition",
      "published": "2026-03-18T09:28:49Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17541v1",
      "title": "Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models",
      "published": "2026-03-18T09:46:44Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18095v2",
      "title": "Q-Drift: Quantization-Aware Drift Correction for Diffusion Model Sampling",
      "published": "2026-03-18T10:19:36Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17573v2",
      "title": "HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness",
      "published": "2026-03-18T10:25:08Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.22307v1",
      "title": "Full waveform inversion method based on diffusion model",
      "published": "2026-03-18T11:32:33Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17652v1",
      "title": "VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs",
      "published": "2026-03-18T12:13:30Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17677v2",
      "title": "Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models",
      "published": "2026-03-18T12:54:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17705v1",
      "title": "Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation",
      "published": "2026-03-18T13:23:58Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17759v2",
      "title": "Harm or Humor: A Multimodal, Multilingual Benchmark for Overt and Covert Harmful Humor",
      "published": "2026-03-18T14:21:10Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17765v1",
      "title": "Grounded Multimodal Retrieval-Augmented Drafting of Radiology Impressions Using Case-Based Similarity Search",
      "published": "2026-03-18T14:25:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17808v2",
      "title": "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards",
      "published": "2026-03-18T15:02:19Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17809v1",
      "title": "Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients",
      "published": "2026-03-18T15:03:43Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17825v2",
      "title": "Steering Video Diffusion Transformers with Massive Activations",
      "published": "2026-03-18T15:24:12Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17828v1",
      "title": "TINA: Text-Free Inversion Attack for Unlearned Text-to-Image Diffusion Models",
      "published": "2026-03-18T15:25:03Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18118v1",
      "title": "Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models",
      "published": "2026-03-18T15:28:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17850v1",
      "title": "ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models",
      "published": "2026-03-18T15:38:29Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17879v2",
      "title": "Anatomy-Guided Vision-Language Learning with Angular Prototype Separation for Multi-Label Video Capsule Endoscopy Classification Under Class Imbalance",
      "published": "2026-03-18T16:04:50Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17993v1",
      "title": "GMT: Goal-Conditioned Multimodal Transformer for 6-DOF Object Trajectory Synthesis in 3D Scenes",
      "published": "2026-03-18T17:54:35Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18002v1",
      "title": "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models",
      "published": "2026-03-18T17:59:10Z"
    }
  ]
}
```

```json
{
  "url": "https://export.arxiv.org/api/query?search_query=(cat%3Acs.DC%20OR%20cat%3Acs.AR%20OR%20cat%3Acs.OS%20OR%20cat%3Acs.PL%20OR%20cat%3Acs.PF)%20AND%20(all%3AGPU%20OR%20all%3Ainference%20OR%20all%3Atraining%20OR%20all%3Aserving%20OR%20all%3Akernel%20OR%20all%3Acompil*)%20AND%20submittedDate%3A%5B202603171800%20TO%20202603181800%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
  "bytes": 42586,
  "total": "16",
  "rows": [
    {
      "id": "http://arxiv.org/abs/2603.17099v1",
      "title": "Vectorization of Verilog Designs and its Effects on Verification and Synthesis",
      "published": "2026-03-17T19:39:56Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18049v1",
      "title": "Conditional Execution of Transpiler Passes Based on Per-Script Feature Detection",
      "published": "2026-03-17T19:54:22Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17168v1",
      "title": "HierarchicalKV: A GPU Hash Table with Cache Semantics for Continuous Online Embedding Storage",
      "published": "2026-03-17T21:59:59Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17204v1",
      "title": "CODMAS: A Dialectic Multi-Agent Collaborative Framework for Structured RTL Optimization",
      "published": "2026-03-17T23:10:07Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18054v1",
      "title": "An FPGA-Based SoC Architecture with a RISC-V Controller for Energy-Efficient Temporal-Coding Spiking Neural Networks",
      "published": "2026-03-17T23:39:13Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17230v1",
      "title": "KANtize: Exploring Low-bit Quantization of Kolmogorov-Arnold Networks for Efficient Inference",
      "published": "2026-03-18T00:32:11Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17259v1",
      "title": "AppFlow: Memory Scheduling for Cold Launch of Large Apps on Mobile and Vehicle Systems",
      "published": "2026-03-18T01:35:25Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17280v2",
      "title": "The 1/W Law: An Analytical Study of Context-Length Routing Topology and GPU Generation Gains for LLM Inference Energy Efficiency",
      "published": "2026-03-18T02:15:40Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18066v2",
      "title": "A Synthesizable RTL Implementation of Predictive Coding Networks",
      "published": "2026-03-18T03:07:19Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17435v1",
      "title": "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression",
      "published": "2026-03-18T07:21:21Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17456v2",
      "title": "Stage-Aware Communication Scheduling for Disaggregated LLM Serving",
      "published": "2026-03-18T07:53:28Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17627v4",
      "title": "The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation",
      "published": "2026-03-18T11:47:15Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18104v5",
      "title": "Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI",
      "published": "2026-03-18T12:36:19Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17800v1",
      "title": "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings",
      "published": "2026-03-18T14:55:52Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.17803v1",
      "title": "Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs",
      "published": "2026-03-18T14:59:16Z"
    },
    {
      "id": "http://arxiv.org/abs/2603.18126v2",
      "title": "A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective",
      "published": "2026-03-18T17:22:37Z"
    }
  ]
}
```
