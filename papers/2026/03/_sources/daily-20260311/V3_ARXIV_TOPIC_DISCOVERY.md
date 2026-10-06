# 03/11 arXiv 有限主题发现（未作公开时间证明）

执行2026-10-01；窗口[03/10T09+08,03/11T09+08)。API SubmittedDate只作发现，不用作正文首次公开。采用curl -G --data-urlencode，实际响应canonical title正确。本窗正常公告Tue03/10 20EDT=03/11BJT08；发现时间切片Mar09T18Z至Mar10T17:59Z只提供最早常规公告下界，仍须逐项必要公开上界。四组只浏览相关标题；标题列表不是逐项题摘/全文关闭队列。API默认latest revision，拟采用者另取精确v1。

初次手工URL把TO之后2026遗漏首20，canonical出现2603101800且返回Sept，整次结果弃用。最小正确SubmittedDate日期查询与四主题canonical复核恢复，非外部API故障。

## model

原始查询：`arXiv Query: search_query=(ti:"language model" OR ti:Transformer OR ti:MoE OR ti:"foundation model" OR ti:alignment OR ti:"model training") AND submittedDate:"202603091800 TO 202603101759"&id_list=&start=0&max_results=100`；total=80，实际start0/max100返回80，读到末尾。本记录只发现。

| ID/version（API当前值） | 标题 | submitted | updated |
| --- | --- | --- | --- |
| http://arxiv.org/abs/2603.09964v2 | Understanding the Use of a Large Language Model-Powered Guide to Make Virtual Reality Accessible for Blind and Low Vision People | 2026-03-10T17:56:57Z | 2026-03-30T15:28:55Z |
| http://arxiv.org/abs/2603.10098v1 | Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models | 2026-03-10T17:37:06Z | 2026-03-10T17:37:06Z |
| http://arxiv.org/abs/2603.09943v2 | PathMem: Toward Cognition-Aligned Memory Transformation for Pathology MLLMs | 2026-03-10T17:35:49Z | 2026-05-25T11:05:14Z |
| http://arxiv.org/abs/2603.09940v1 | SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG | 2026-03-10T17:32:28Z | 2026-03-10T17:32:28Z |
| http://arxiv.org/abs/2603.09938v2 | Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions | 2026-03-10T17:31:55Z | 2026-03-30T16:23:51Z |
| http://arxiv.org/abs/2603.09888v2 | LCA: Local Classifier Alignment for Continual Learning | 2026-03-10T16:46:09Z | 2026-03-11T03:00:44Z |
| http://arxiv.org/abs/2603.09884v1 | Benchmarking Political Persuasion Risks Across Frontier Large Language Models | 2026-03-10T16:42:05Z | 2026-03-10T16:42:05Z |
| http://arxiv.org/abs/2603.09872v2 | N-gram-like Language Models Predict Naturalistic Reading Time Best | 2026-03-10T16:35:41Z | 2026-08-18T17:04:06Z |
| http://arxiv.org/abs/2603.09865v1 | GAST: Gradient-aligned Sparse Tuning of Large Language Models with Data-layer Selection | 2026-03-10T16:28:48Z | 2026-03-10T16:28:48Z |
| http://arxiv.org/abs/2603.09826v1 | VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models | 2026-03-10T15:48:25Z | 2026-03-10T15:48:25Z |
| http://arxiv.org/abs/2603.09815v1 | Correction of Transformer-Based Models with Smoothing Pseudo-Projector | 2026-03-10T15:42:46Z | 2026-03-10T15:42:46Z |
| http://arxiv.org/abs/2603.10091v1 | Multi-Stream Perturbation Attack: Breaking Safety Alignment of Thinking LLMs Through Concurrent Task Interference | 2026-03-10T15:40:49Z | 2026-03-10T15:40:49Z |
| http://arxiv.org/abs/2603.09774v1 | World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models | 2026-03-10T15:12:14Z | 2026-03-10T15:12:14Z |
| http://arxiv.org/abs/2603.09771v2 | Ego: Embedding-Guided Personalization of Vision-Language Models | 2026-03-10T15:10:41Z | 2026-03-11T15:26:01Z |
| http://arxiv.org/abs/2603.09740v1 | Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | 2026-03-10T14:45:50Z | 2026-03-10T14:45:50Z |
| http://arxiv.org/abs/2603.10088v1 | ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping | 2026-03-10T14:31:19Z | 2026-03-10T14:31:19Z |
| http://arxiv.org/abs/2603.09721v2 | FrameDiT: Diffusion Transformer with Matrix Attention for Efficient Video Generation | 2026-03-10T14:28:32Z | 2026-04-18T11:35:45Z |
| http://arxiv.org/abs/2603.09714v2 | MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models | 2026-03-10T14:22:22Z | 2026-07-12T21:54:08Z |
| http://arxiv.org/abs/2603.10087v1 | Pooling Engram Conditional Memory in Large Language Models using CXL | 2026-03-10T14:13:02Z | 2026-03-10T14:13:02Z |
| http://arxiv.org/abs/2603.09695v2 | DRIFT: Dual-Representation Inter-Fusion Transformer for Automated Driving Perception with 4D Radar Point Clouds | 2026-03-10T14:03:35Z | 2026-03-12T06:06:36Z |
| http://arxiv.org/abs/2603.09678v2 | EsoLang-Bench: Evaluating Genuine Reasoning in Large Language Models via Esoteric Programming Languages | 2026-03-10T13:47:15Z | 2026-05-11T23:17:28Z |
| http://arxiv.org/abs/2603.09666v2 | Application of dual-tree complex wavelet transform for spectra background reduction | 2026-03-10T13:38:39Z | 2026-08-13T12:55:15Z |
| http://arxiv.org/abs/2603.26683v1 | LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval | 2026-03-10T13:25:39Z | 2026-03-10T13:25:39Z |
| http://arxiv.org/abs/2603.09638v2 | Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models | 2026-03-10T13:13:43Z | 2026-03-11T08:57:33Z |
| http://arxiv.org/abs/2603.09627v1 | Speech-Omni-Lite: Portable Speech Interfaces for Vision-Language Models | 2026-03-10T13:06:41Z | 2026-03-10T13:06:41Z |
| http://arxiv.org/abs/2603.09625v2 | Grounding Synthetic Data Generation With Vision and Language Models | 2026-03-10T13:03:53Z | 2026-05-02T13:56:02Z |
| http://arxiv.org/abs/2603.15663v1 | OrthoAI v2: From Single-Agent Segmentation to Dual-Agent Treatment Planning for Clear Aligners | 2026-03-10T13:03:44Z | 2026-03-10T13:03:44Z |
| http://arxiv.org/abs/2603.09616v1 | Surgical Repair of Collapsed Attention Heads in ALiBi Transformers | 2026-03-10T12:57:49Z | 2026-03-10T12:57:49Z |
| http://arxiv.org/abs/2603.09613v2 | A Saccade-inspired Approach to Image Classification using Vision Transformer Attention Maps | 2026-03-10T12:54:55Z | 2026-03-11T12:40:13Z |
| http://arxiv.org/abs/2603.09582v1 | BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers | 2026-03-10T12:31:54Z | 2026-03-10T12:31:54Z |
| http://arxiv.org/abs/2603.09573v2 | More than the Sum: Panorama-Language Models for Adverse Omni-Scenes | 2026-03-10T12:19:50Z | 2026-04-05T10:51:24Z |
| http://arxiv.org/abs/2603.09571v1 | An Optimal Control Approach To Transformer Training | 2026-03-10T12:17:48Z | 2026-03-10T12:17:48Z |
| http://arxiv.org/abs/2603.09566v1 | GeoAlignCLIP: Enhancing Fine-Grained Vision-Language Alignment in Remote Sensing via Multi-Granular Consistency Learning | 2026-03-10T12:12:11Z | 2026-03-10T12:12:11Z |
| http://arxiv.org/abs/2603.09565v2 | ReTac-ACT: A State-Gated Vision-Tactile Fusion Transformer for Precision Assembly | 2026-03-10T12:09:22Z | 2026-03-18T12:10:16Z |
| http://arxiv.org/abs/2603.09556v1 | ALARM: Audio-Language Alignment for Reasoning Models | 2026-03-10T12:03:25Z | 2026-03-10T12:03:25Z |
| http://arxiv.org/abs/2603.09527v1 | Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation | 2026-03-10T11:35:58Z | 2026-03-10T11:35:58Z |
| http://arxiv.org/abs/2603.09511v1 | TrainDeeploy: Hardware-Accelerated Parameter-Efficient Fine-Tuning of Small Transformer Models at the Extreme Edge | 2026-03-10T11:10:50Z | 2026-03-10T11:10:50Z |
| http://arxiv.org/abs/2603.09493v3 | Guided Prompt Evolution for Vision-Language Models Adaptation | 2026-03-10T10:53:01Z | 2026-09-01T11:02:02Z |
| http://arxiv.org/abs/2603.09481v1 | GenePlan: Evolving Better Generalized PDDL Plans using Large Language Models | 2026-03-10T10:32:05Z | 2026-03-10T10:32:05Z |
| http://arxiv.org/abs/2603.09471v1 | OmniEarth: A Benchmark for Evaluating Vision-Language Models in Geospatial Tasks | 2026-03-10T10:22:01Z | 2026-03-10T10:22:01Z |
| http://arxiv.org/abs/2603.09453v3 | Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers | 2026-03-10T10:07:53Z | 2026-05-28T23:48:17Z |
| http://arxiv.org/abs/2603.09452v1 | CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research? | 2026-03-10T10:04:12Z | 2026-03-10T10:04:12Z |
| http://arxiv.org/abs/2603.09450v2 | Feasible Sets and the Transformation of Values | 2026-03-10T10:03:08Z | 2026-03-11T12:16:10Z |
| http://arxiv.org/abs/2603.10080v2 | Amnesia: Adversarial Semantic Layer Specific Activation Steering in Large Language Models | 2026-03-10T09:41:03Z | 2026-03-17T08:26:11Z |
| http://arxiv.org/abs/2603.09416v1 | Investigating Gender Stereotypes in Large Language Models via Social Determinants of Health | 2026-03-10T09:30:10Z | 2026-03-10T09:30:10Z |
| http://arxiv.org/abs/2603.09378v2 | SPAARS: Safer RL Policy Alignment through Abstract Exploration and Refined Exploitation of Action Space | 2026-03-10T08:52:15Z | 2026-03-11T05:45:21Z |
| http://arxiv.org/abs/2603.09326v2 | OddGridBench: Exposing the Lack of Fine-Grained Visual Discrepancy Sensitivity in Multimodal Large Language Models | 2026-03-10T08:01:30Z | 2026-03-30T12:07:08Z |
| http://arxiv.org/abs/2603.09303v2 | Investor risk profiles of large language models | 2026-03-10T07:38:26Z | 2026-05-27T11:19:42Z |
| http://arxiv.org/abs/2603.09301v2 | Constructing a Portfolio Optimization Benchmark Framework for Evaluating Large Language Models | 2026-03-10T07:35:31Z | 2026-05-27T11:20:48Z |
| http://arxiv.org/abs/2603.09246v1 | Reasoning-Oriented Programming: Chaining Semantic Gadgets to Jailbreak Large Vision Language Models | 2026-03-10T06:18:48Z | 2026-03-10T06:18:48Z |
| http://arxiv.org/abs/2603.09245v2 | Bridging Object Detection and Segmentation with Polygon Detection Transformers | 2026-03-10T06:18:33Z | 2026-08-10T09:51:48Z |
| http://arxiv.org/abs/2603.09240v1 | Incoherent Operations Enable State Transformations Impossible under Dephasing-covariant Incoherent Operations | 2026-03-10T06:16:13Z | 2026-03-10T06:16:13Z |
| http://arxiv.org/abs/2603.09232v2 | How Contrastive Decoding Enhances Large Audio Language Models | 2026-03-10T06:05:51Z | 2026-09-13T17:35:01Z |
| http://arxiv.org/abs/2603.09217v2 | TubeMLLM: A Foundation Model for Topology Knowledge Exploration in Vessel-like Anatomy | 2026-03-10T05:39:30Z | 2026-03-13T05:45:42Z |
| http://arxiv.org/abs/2603.09215v2 | SPAR-K: Scheduled Periodic Alternating Early Exit for Spoken Language Models | 2026-03-10T05:39:03Z | 2026-08-27T08:44:51Z |
| http://arxiv.org/abs/2603.09206v1 | MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data | 2026-03-10T05:23:26Z | 2026-03-10T05:23:26Z |
| http://arxiv.org/abs/2603.09201v1 | The Radio-Frequency Transformer for Signal Separation | 2026-03-10T05:22:02Z | 2026-03-10T05:22:02Z |
| http://arxiv.org/abs/2603.10071v1 | Dissecting Chronos: Sparse Autoencoders Reveal Causal Feature Hierarchies in Time Series Foundation Models | 2026-03-10T04:31:33Z | 2026-03-10T04:31:33Z |
| http://arxiv.org/abs/2603.09173v1 | Point Cloud as a Foreign Language for Multi-modal Large Language Model | 2026-03-10T04:22:40Z | 2026-03-10T04:22:40Z |
| http://arxiv.org/abs/2603.09165v1 | GIAT: A Geologically-Informed Attention Transformer for Lithology Identification | 2026-03-10T04:02:57Z | 2026-03-10T04:02:57Z |
| http://arxiv.org/abs/2603.09137v2 | Transformer-Based Multi-Region Segmentation and Radiomic Analysis of HR-pQCT Imaging for Osteoporosis Classification | 2026-03-10T03:22:13Z | 2026-03-11T01:39:38Z |
| http://arxiv.org/abs/2603.10068v2 | ADVERSA: Measuring Multi-Turn Guardrail Degradation and Judge Reliability in Large Language Models | 2026-03-10T03:00:34Z | 2026-08-25T05:47:14Z |
| http://arxiv.org/abs/2603.09108v2 | Composed Vision-Language Retrieval for Skin Cancer Case Search via Joint Alignment of Global and Local Representations | 2026-03-10T02:42:30Z | 2026-04-20T09:11:22Z |
| http://arxiv.org/abs/2603.09100v1 | Class Model Generation from Requirements using Large Language Models | 2026-03-10T02:20:35Z | 2026-03-10T02:20:35Z |
| http://arxiv.org/abs/2603.09070v1 | 3D UAV Trajectory Estimation and Classification from Internet Videos via Language Model | 2026-03-10T01:29:17Z | 2026-03-10T01:29:17Z |
| http://arxiv.org/abs/2604.00011v1 | Quantifying Gender Bias in Large Language Models: When ChatGPT Becomes a Hiring Manager | 2026-03-10T00:27:00Z | 2026-03-10T00:27:00Z |
| http://arxiv.org/abs/2603.09043v1 | Time, Identity and Consciousness in Language Model Agents | 2026-03-10T00:25:37Z | 2026-03-10T00:25:37Z |
| http://arxiv.org/abs/2603.08987v1 | MAPLE: Elevating Medical Reasoning from Statistical Consensus to Process-Led Alignment | 2026-03-09T22:22:57Z | 2026-03-09T22:22:57Z |
| http://arxiv.org/abs/2603.08942v2 | BiCLIP: Domain Canonicalization via Structured Geometric Transformation | 2026-03-09T21:26:15Z | 2026-04-11T17:42:10Z |
| http://arxiv.org/abs/2603.08935v2 | PathoScribe: Transforming Pathology Data into a Living Library with a Unified LLM-Driven Framework for Semantic Retrieval and Clinical Integration | 2026-03-09T21:09:24Z | 2026-03-11T16:00:39Z |
| http://arxiv.org/abs/2603.08930v2 | Using Vision Language Foundation Models to Generate Plant Simulation Configurations via In-Context Learning | 2026-03-09T20:58:43Z | 2026-09-22T23:45:25Z |
| http://arxiv.org/abs/2603.10061v2 | Decision-Aware Uncertainty Evaluation of Vision-Language Model-Based Early Action Anticipation for Human-Robot Interaction | 2026-03-09T20:57:22Z | 2026-03-12T01:00:28Z |
| http://arxiv.org/abs/2603.08928v1 | TIDE: Text-Informed Dynamic Extrapolation with Step-Aware Temperature Control for Diffusion Transformers | 2026-03-09T20:57:19Z | 2026-03-09T20:57:19Z |
| http://arxiv.org/abs/2603.08921v1 | Vision-Language Models Encode Clinical Guidelines for Concept-Based Medical Reasoning | 2026-03-09T20:39:46Z | 2026-03-09T20:39:46Z |
| http://arxiv.org/abs/2603.08913v2 | Quantifying Memorization and Privacy Risks in Genomic Language Models | 2026-03-09T20:30:37Z | 2026-08-17T21:27:12Z |
| http://arxiv.org/abs/2603.08881v1 | From Word2Vec to Transformers: Text-Derived Composition Embeddings for Filtering Combinatorial Electrocatalysts | 2026-03-09T19:46:23Z | 2026-03-09T19:46:23Z |
| http://arxiv.org/abs/2603.08872v1 | Aligning van der Waals heterostructures using electron backscatter diffraction | 2026-03-09T19:39:14Z | 2026-03-09T19:39:14Z |
| http://arxiv.org/abs/2603.08817v1 | HMR-1: Hierarchical Massage Robot with Vision-Language-Model for Embodied Healthcare | 2026-03-09T18:17:33Z | 2026-03-09T18:17:33Z |
| http://arxiv.org/abs/2603.10055v1 | Training Language Models via Neural Cellular Automata | 2026-03-09T18:14:26Z | 2026-03-09T18:14:26Z |
| http://arxiv.org/abs/2603.08801v1 | Large Language Model-Assisted Superconducting Qubit Experiments | 2026-03-09T18:03:10Z | 2026-03-09T18:03:10Z |

## system

原始查询：`arXiv Query: search_query=(ti:GPU OR ti:kernel OR ti:"model serving" OR ti:"KV cache" OR ti:"LLM inference" OR ti:"tensor parallel") AND submittedDate:"202603091800 TO 202603101759"&id_list=&start=0&max_results=100`；total=7，实际start0/max100返回7，读到末尾。本记录只发现。

| ID/version（API当前值） | 标题 | submitted | updated |
| --- | --- | --- | --- |
| http://arxiv.org/abs/2603.10085v1 | KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization | 2026-03-10T13:43:38Z | 2026-03-10T13:43:38Z |
| http://arxiv.org/abs/2603.09462v1 | Mollified Christoffel-Darboux Kernels and Density Recovery on Varieties | 2026-03-10T10:15:59Z | 2026-03-10T10:15:59Z |
| http://arxiv.org/abs/2603.09216v1 | PIM-SHERPA: Software Method for On-device LLM Inference by Resolving PIM Memory Attribute and Layout Inconsistencies | 2026-03-10T05:39:03Z | 2026-03-10T05:39:03Z |
| http://arxiv.org/abs/2603.09051v2 | Cutting the Cord: System Architecture for Low-Cost, GPU-Accelerated Bimanual Mobile Manipulation | 2026-03-10T00:44:23Z | 2026-03-21T18:13:20Z |
| http://arxiv.org/abs/2603.08945v1 | Kernel Debiased Plug-in Estimation based on the Universal Least Favorable Submodel | 2026-03-09T21:27:26Z | 2026-03-09T21:27:26Z |
| http://arxiv.org/abs/2603.08906v1 | Multi-Kernel Gated Decoder Adapters for Robust Multi-Task Thyroid Ultrasound under Cross-Center Shift | 2026-03-09T20:18:35Z | 2026-03-09T20:18:35Z |
| http://arxiv.org/abs/2603.08797v1 | Serving Compound Inference Systems on Datacenter GPUs | 2026-03-09T18:01:10Z | 2026-03-09T18:01:10Z |

## multimodal

原始查询：`arXiv Query: search_query=(ti:multimodal OR ti:"world model" OR ti:VLA OR ti:"vision language" OR ti:"diffusion model") AND submittedDate:"202603091800 TO 202603101759"&id_list=&start=0&max_results=100`；total=50，实际start0/max100返回50，读到末尾。本记录只发现。

| ID/version（API当前值） | 标题 | submitted | updated |
| --- | --- | --- | --- |
| http://arxiv.org/abs/2603.09940v1 | SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG | 2026-03-10T17:32:28Z | 2026-03-10T17:32:28Z |
| http://arxiv.org/abs/2603.09931v1 | Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation | 2026-03-10T17:26:45Z | 2026-03-10T17:26:45Z |
| http://arxiv.org/abs/2603.09909v2 | MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems | 2026-03-10T17:03:11Z | 2026-03-18T19:17:16Z |
| http://arxiv.org/abs/2603.09877v1 | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | 2026-03-10T16:38:33Z | 2026-03-10T16:38:33Z |
| http://arxiv.org/abs/2603.09874v1 | MissBench: Benchmarking Multimodal Affective Analysis under Imbalanced Missing Modalities | 2026-03-10T16:36:45Z | 2026-03-10T16:36:45Z |
| http://arxiv.org/abs/2603.09826v1 | VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models | 2026-03-10T15:48:25Z | 2026-03-10T15:48:25Z |
| http://arxiv.org/abs/2603.09771v2 | Ego: Embedding-Guided Personalization of Vision-Language Models | 2026-03-10T15:10:41Z | 2026-03-11T15:26:01Z |
| http://arxiv.org/abs/2603.09740v1 | Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | 2026-03-10T14:45:50Z | 2026-03-10T14:45:50Z |
| http://arxiv.org/abs/2603.09715v2 | Does the Question Really Matter? Training-Free Data Selection for Vision-Language SFT | 2026-03-10T14:23:38Z | 2026-06-10T06:53:56Z |
| http://arxiv.org/abs/2603.26683v1 | LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval | 2026-03-10T13:25:39Z | 2026-03-10T13:25:39Z |
| http://arxiv.org/abs/2603.09627v1 | Speech-Omni-Lite: Portable Speech Interfaces for Vision-Language Models | 2026-03-10T13:06:41Z | 2026-03-10T13:06:41Z |
| http://arxiv.org/abs/2604.00013v2 | C2F-Thinker: Coarse-to-Fine Reasoning with Hint-Guided Reinforcement Learning for Multimodal Sentiment Analysis | 2026-03-10T12:48:41Z | 2026-04-12T03:30:47Z |
| http://arxiv.org/abs/2603.09566v1 | GeoAlignCLIP: Enhancing Fine-Grained Vision-Language Alignment in Remote Sensing via Multi-Granular Consistency Learning | 2026-03-10T12:12:11Z | 2026-03-10T12:12:11Z |
| http://arxiv.org/abs/2603.09542v3 | NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models | 2026-03-10T11:51:54Z | 2026-09-11T11:07:40Z |
| http://arxiv.org/abs/2603.09538v1 | Towards Unified Multimodal Interleaved Generation via Group Relative Policy Optimization | 2026-03-10T11:49:20Z | 2026-03-10T11:49:20Z |
| http://arxiv.org/abs/2603.09536v1 | Dynamic Multimodal Expression Generation for LLM-Driven Pedagogical Agents: From User Experience Perspective | 2026-03-10T11:48:37Z | 2026-03-10T11:48:37Z |
| http://arxiv.org/abs/2603.09508v2 | A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration | 2026-03-10T11:09:18Z | 2026-06-23T12:15:49Z |
| http://arxiv.org/abs/2603.09493v3 | Guided Prompt Evolution for Vision-Language Models Adaptation | 2026-03-10T10:53:01Z | 2026-09-01T11:02:02Z |
| http://arxiv.org/abs/2603.09482v1 | StyleVLA: Driving Style-Aware Vision Language Action Model for Autonomous Driving | 2026-03-10T10:33:58Z | 2026-03-10T10:33:58Z |
| http://arxiv.org/abs/2603.09478v1 | MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning | 2026-03-10T10:30:59Z | 2026-03-10T10:30:59Z |
| http://arxiv.org/abs/2603.09471v1 | OmniEarth: A Benchmark for Evaluating Vision-Language Models in Geospatial Tasks | 2026-03-10T10:22:01Z | 2026-03-10T10:22:01Z |
| http://arxiv.org/abs/2603.09465v3 | EvoDriveVLA: Evolving Driving VLA Models via Collaborative Perception-Planning Distillation | 2026-03-10T10:19:07Z | 2026-05-11T07:51:23Z |
| http://arxiv.org/abs/2603.09454v1 | ShapeMark: Robust and Diversity-Preserving Watermarking for Diffusion Models | 2026-03-10T10:10:47Z | 2026-03-10T10:10:47Z |
| http://arxiv.org/abs/2603.09408v1 | Reviving ConvNeXt for Efficient Convolutional Diffusion Models | 2026-03-10T09:24:30Z | 2026-03-10T09:24:30Z |
| http://arxiv.org/abs/2603.09326v2 | OddGridBench: Exposing the Lack of Fine-Grained Visual Discrepancy Sensitivity in Multimodal Large Language Models | 2026-03-10T08:01:30Z | 2026-03-30T12:07:08Z |
| http://arxiv.org/abs/2603.09292v2 | See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation | 2026-03-10T07:22:51Z | 2026-05-30T16:07:44Z |
| http://arxiv.org/abs/2603.09258v1 | Multimodal Graph Representation Learning with Dynamic Information Pathways | 2026-03-10T06:45:59Z | 2026-03-10T06:45:59Z |
| http://arxiv.org/abs/2603.09246v1 | Reasoning-Oriented Programming: Chaining Semantic Gadgets to Jailbreak Large Vision Language Models | 2026-03-10T06:18:48Z | 2026-03-10T06:18:48Z |
| http://arxiv.org/abs/2603.09241v2 | RAE-NWM: Navigation World Model in Dense Visual Representation Space | 2026-03-10T06:16:23Z | 2026-06-26T11:58:42Z |
| http://arxiv.org/abs/2603.09206v1 | MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data | 2026-03-10T05:23:26Z | 2026-03-10T05:23:26Z |
| http://arxiv.org/abs/2603.09163v1 | SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation | 2026-03-10T03:59:34Z | 2026-03-10T03:59:34Z |
| http://arxiv.org/abs/2603.09125v1 | QUSR: Quality-Aware and Uncertainty-Guided Image Super-Resolution Diffusion Model | 2026-03-10T02:57:31Z | 2026-03-10T02:57:31Z |
| http://arxiv.org/abs/2603.09121v1 | DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation | 2026-03-10T02:55:27Z | 2026-03-10T02:55:27Z |
| http://arxiv.org/abs/2603.09111v1 | Progressive Representation Learning for Multimodal Sentiment Analysis with Incomplete Modalities | 2026-03-10T02:45:02Z | 2026-03-10T02:45:02Z |
| http://arxiv.org/abs/2603.09108v2 | Composed Vision-Language Retrieval for Skin Cancer Case Search via Joint Alignment of Global and Local Representations | 2026-03-10T02:42:30Z | 2026-04-20T09:11:22Z |
| http://arxiv.org/abs/2603.09101v1 | MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration | 2026-03-10T02:22:12Z | 2026-03-10T02:22:12Z |
| http://arxiv.org/abs/2603.09095v3 | Reading, Not Thinking: Understanding and Bridging the Modality Gap When Text Becomes Pixels in Multimodal LLMs | 2026-03-10T02:14:23Z | 2026-05-30T05:14:01Z |
| http://arxiv.org/abs/2603.09086v1 | Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges | 2026-03-10T01:56:17Z | 2026-03-10T01:56:17Z |
| http://arxiv.org/abs/2603.09084v2 | SyncEdit: Rethinking Lip Synchronization as Editing with Audio-Driven Diffusion Models | 2026-03-10T01:51:28Z | 2026-09-28T02:59:54Z |
| http://arxiv.org/abs/2603.09079v1 | GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware Vision-Language-Action Models | 2026-03-10T01:39:38Z | 2026-03-10T01:39:38Z |
| http://arxiv.org/abs/2603.09075v1 | M2Diff: Multi-Modality Multi-Task Enhanced Diffusion Model for MRI-Guided Low-Dose PET Enhancement | 2026-03-10T01:34:49Z | 2026-03-10T01:34:49Z |
| http://arxiv.org/abs/2603.09063v1 | A Stable, High-Order Time-Stepping Scheme for the Drift-Diffusion Model in Modern Solar Cell Simulation | 2026-03-10T01:13:34Z | 2026-03-10T01:13:34Z |
| http://arxiv.org/abs/2603.09030v3 | PlayWorld: Learning Robot World Models from Autonomous Play | 2026-03-09T23:58:07Z | 2026-04-06T01:32:12Z |
| http://arxiv.org/abs/2603.09001v1 | Correcting Ionospheric Faraday Rotation for the VLA and MeerKAT | 2026-03-09T22:37:15Z | 2026-03-09T22:37:15Z |
| http://arxiv.org/abs/2603.08998v1 | Diffusion-Based Authentication of Copy Detection Patterns: A Multimodal Framework with Printer Signature Conditioning | 2026-03-09T22:33:44Z | 2026-03-09T22:33:44Z |
| http://arxiv.org/abs/2603.08930v2 | Using Vision Language Foundation Models to Generate Plant Simulation Configurations via In-Context Learning | 2026-03-09T20:58:43Z | 2026-09-22T23:45:25Z |
| http://arxiv.org/abs/2603.10061v2 | Decision-Aware Uncertainty Evaluation of Vision-Language Model-Based Early Action Anticipation for Human-Robot Interaction | 2026-03-09T20:57:22Z | 2026-03-12T01:00:28Z |
| http://arxiv.org/abs/2603.08921v1 | Vision-Language Models Encode Clinical Guidelines for Concept-Based Medical Reasoning | 2026-03-09T20:39:46Z | 2026-03-09T20:39:46Z |
| http://arxiv.org/abs/2603.08862v2 | APPLV: Adaptive Planner Parameter Learning from Vision-Language-Action Model | 2026-03-09T19:23:09Z | 2026-07-14T05:57:00Z |
| http://arxiv.org/abs/2603.08817v1 | HMR-1: Hierarchical Massage Robot with Vision-Language-Model for Embodied Healthcare | 2026-03-09T18:17:33Z | 2026-03-09T18:17:33Z |

## agent

原始查询：`arXiv Query: search_query=(ti:agent OR ti:"model memory" OR ti:RAG OR ti:"language model planning" OR ti:"tool calling") AND submittedDate:"202603091800 TO 202603101759"&id_list=&start=0&max_results=100`；total=56，实际start0/max100返回56，读到末尾。本记录只发现。

| ID/version（API当前值） | 标题 | submitted | updated |
| --- | --- | --- | --- |
| http://arxiv.org/abs/2603.10098v1 | Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models | 2026-03-10T17:37:06Z | 2026-03-10T17:37:06Z |
| http://arxiv.org/abs/2603.09909v2 | MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems | 2026-03-10T17:03:11Z | 2026-03-18T19:17:16Z |
| http://arxiv.org/abs/2603.09891v1 | Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track | 2026-03-10T16:49:18Z | 2026-03-10T16:49:18Z |
| http://arxiv.org/abs/2603.09890v1 | Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts | 2026-03-10T16:47:25Z | 2026-03-10T16:47:25Z |
| http://arxiv.org/abs/2603.09875v1 | The Bureaucracy of Speed: Structural Equivalence Between Memory Consistency Models and Multi-Agent Authorization Revocation | 2026-03-10T16:37:02Z | 2026-03-10T16:37:02Z |
| http://arxiv.org/abs/2603.09843v1 | RecThinker: An Agentic Framework for Tool-Augmented Reasoning in Recommendation | 2026-03-10T16:07:17Z | 2026-03-10T16:07:17Z |
| http://arxiv.org/abs/2603.09835v1 | Chow-Liu Ordering for Long-Context Reasoning in Chain-of-Agents | 2026-03-10T15:57:35Z | 2026-03-10T15:57:35Z |
| http://arxiv.org/abs/2603.10092v1 | Execution Is the New Attack Surface: Survivability-Aware Agentic Crypto Trading with OpenClaw-Style Local Executors | 2026-03-10T15:54:01Z | 2026-03-10T15:54:01Z |
| http://arxiv.org/abs/2603.09827v2 | MA-EgoQA: Question Answering over Egocentric Videos from Multiple Embodied Agents | 2026-03-10T15:48:35Z | 2026-03-11T02:13:29Z |
| http://arxiv.org/abs/2603.09821v1 | One-Eval: An Agentic System for Automated and Traceable LLM Evaluation | 2026-03-10T15:45:51Z | 2026-03-10T15:45:51Z |
| http://arxiv.org/abs/2603.09733v1 | FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis | 2026-03-10T14:37:28Z | 2026-03-10T14:37:28Z |
| http://arxiv.org/abs/2603.09716v1 | AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents | 2026-03-10T14:23:49Z | 2026-03-10T14:23:49Z |
| http://arxiv.org/abs/2603.11068v1 | From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery | 2026-03-10T14:20:53Z | 2026-03-10T14:20:53Z |
| http://arxiv.org/abs/2603.09704v2 | Evaluation of LLMs in retrieving food and nutritional context for RAG systems | 2026-03-10T14:15:35Z | 2026-03-11T10:27:24Z |
| http://arxiv.org/abs/2603.10085v1 | KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization | 2026-03-10T13:43:38Z | 2026-03-10T13:43:38Z |
| http://arxiv.org/abs/2603.09643v5 | MM-tau-p$^2$: Persona-Adaptive Prompting for Robust Multi-Modal Agent Evaluation in Dual-Control Settings | 2026-03-10T13:18:02Z | 2026-04-16T11:12:58Z |
| http://arxiv.org/abs/2603.15663v1 | OrthoAI v2: From Single-Agent Segmentation to Dual-Agent Treatment Planning for Clear Aligners | 2026-03-10T13:03:44Z | 2026-03-10T13:03:44Z |
| http://arxiv.org/abs/2603.09619v2 | Context Engineering: From Prompts to Corporate Multi-Agent Architecture | 2026-03-10T12:58:31Z | 2026-03-13T03:59:39Z |
| http://arxiv.org/abs/2603.20247v1 | AlphaLogics: A Market Logic-Driven Multi-Agent System for Scalable and Interpretable Alpha Factor Generation | 2026-03-10T12:18:02Z | 2026-03-10T12:18:02Z |
| http://arxiv.org/abs/2603.09536v1 | Dynamic Multimodal Expression Generation for LLM-Driven Pedagogical Agents: From User Experience Perspective | 2026-03-10T11:48:37Z | 2026-03-10T11:48:37Z |
| http://arxiv.org/abs/2603.26682v1 | Operationalizing Perceptions of Agent Gender: Foundations and Guidelines | 2026-03-10T11:15:31Z | 2026-03-10T11:15:31Z |
| http://arxiv.org/abs/2603.09497v1 | EmbC-Test: How to Speed Up Embedded Software Testing Using LLMs and RAG | 2026-03-10T10:58:59Z | 2026-03-10T10:58:59Z |
| http://arxiv.org/abs/2603.09448v2 | A Guideline-Aware AI Agent for Zero-Shot Target Volume Auto-Delineation | 2026-03-10T10:00:01Z | 2026-06-25T09:30:39Z |
| http://arxiv.org/abs/2603.09435v1 | AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems | 2026-03-10T09:47:50Z | 2026-03-10T09:47:50Z |
| http://arxiv.org/abs/2603.09358v1 | ProvAgent: Threat Detection Based on Identity-Behavior Binding and Multi-Agent Collaborative Attack Investigation | 2026-03-10T08:38:53Z | 2026-03-10T08:38:53Z |
| http://arxiv.org/abs/2603.09341v1 | TaSR-RAG: Taxonomy-guided Structured Reasoning for Retrieval-Augmented Generation | 2026-03-10T08:16:36Z | 2026-03-10T08:16:36Z |
| http://arxiv.org/abs/2603.09324v1 | Reading the Mood Behind Words: Integrating Prosody-Derived Emotional Context into Socially Responsive VR Agents | 2026-03-10T07:58:06Z | 2026-03-10T07:58:06Z |
| http://arxiv.org/abs/2603.09290v5 | ToolRosella: Translating Code Repositories into Standardized Tools for Scientific Agents | 2026-03-10T07:19:43Z | 2026-06-09T12:13:24Z |
| http://arxiv.org/abs/2603.09208v1 | Strategically Robust Multi-Agent Reinforcement Learning with Linear Function Approximation | 2026-03-10T05:24:10Z | 2026-03-10T05:24:10Z |
| http://arxiv.org/abs/2603.09203v2 | Evaluate-as-Action: Self-Evaluated Process Rewards for Retrieval-Augmented Agents | 2026-03-10T05:22:40Z | 2026-03-12T06:04:58Z |
| http://arxiv.org/abs/2603.09192v1 | Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back | 2026-03-10T05:04:28Z | 2026-03-10T05:04:28Z |
| http://arxiv.org/abs/2603.09188v1 | Robust Spatiotemporal Motion Planning for Multi-Agent Autonomous Racing via Topological Gap Identification and Accelerated MPC | 2026-03-10T04:55:30Z | 2026-03-10T04:55:30Z |
| http://arxiv.org/abs/2603.10069v1 | Improving Search Agent with One Line of Code | 2026-03-10T04:07:39Z | 2026-03-10T04:07:39Z |
| http://arxiv.org/abs/2603.09157v1 | Real-Time Trust Verification for Safe Agentic Actions using TrustBench | 2026-03-10T03:46:22Z | 2026-03-10T03:46:22Z |
| http://arxiv.org/abs/2603.09152v1 | DataFactory: Collaborative Multi-Agent Framework for Advanced Table Question Answering | 2026-03-10T03:44:52Z | 2026-03-10T03:44:52Z |
| http://arxiv.org/abs/2603.09141v2 | Agentic AI as a Network Control-Plane Intelligence Layer for Federated Learning over 6G | 2026-03-10T03:27:33Z | 2026-03-11T06:14:51Z |
| http://arxiv.org/abs/2603.09134v1 | AgenticCyOps: Securing Multi-Agentic AI Integration in Enterprise Cyber Operations | 2026-03-10T03:15:36Z | 2026-03-10T03:15:36Z |
| http://arxiv.org/abs/2603.09052v1 | From Days to Minutes: An Autonomous AI Agent Achieves Reliable Clinical Triage in Remote Patient Monitoring | 2026-03-10T00:50:54Z | 2026-03-10T00:50:54Z |
| http://arxiv.org/abs/2603.09049v1 | EPOCH: An Agentic Protocol for Multi-Round System Optimization | 2026-03-10T00:41:03Z | 2026-03-10T00:41:03Z |
| http://arxiv.org/abs/2603.09043v1 | Time, Identity and Consciousness in Language Model Agents | 2026-03-10T00:25:37Z | 2026-03-10T00:25:37Z |
| http://arxiv.org/abs/2603.09022v2 | MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games | 2026-03-09T23:36:32Z | 2026-03-18T18:40:09Z |
| http://arxiv.org/abs/2603.09018v1 | Meissa: Multi-modal Medical Agentic Intelligence | 2026-03-09T23:22:55Z | 2026-03-09T23:22:55Z |
| http://arxiv.org/abs/2603.09004v1 | Can AI Agents Generate Microservices? How Far are We? | 2026-03-09T22:48:41Z | 2026-03-09T22:48:41Z |
| http://arxiv.org/abs/2603.09002v2 | Security Considerations for Multi-agent Systems | 2026-03-09T22:46:27Z | 2026-04-26T14:13:48Z |
| http://arxiv.org/abs/2603.08993v1 | Arbiter: Detecting Interference in LLM Agent System Prompts | 2026-03-09T22:29:47Z | 2026-03-09T22:29:47Z |
| http://arxiv.org/abs/2603.10062v2 | Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead | 2026-03-09T21:16:12Z | 2026-03-30T22:50:29Z |
| http://arxiv.org/abs/2603.10060v1 | Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination Detection for AI Agents | 2026-03-09T20:45:41Z | 2026-03-09T20:45:41Z |
| http://arxiv.org/abs/2603.08877v1 | Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search | 2026-03-09T19:42:21Z | 2026-03-09T19:42:21Z |
| http://arxiv.org/abs/2603.08853v1 | LLM-Agent Interactions on Markets with Information Asymmetries | 2026-03-09T19:13:48Z | 2026-03-09T19:13:48Z |
| http://arxiv.org/abs/2603.08852v1 | LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems | 2026-03-09T19:13:17Z | 2026-03-09T19:13:17Z |
| http://arxiv.org/abs/2603.10057v1 | SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation | 2026-03-09T19:11:45Z | 2026-03-09T19:11:45Z |
| http://arxiv.org/abs/2603.08835v1 | MASEval: Extending Multi-Agent Evaluation from Models to Systems | 2026-03-09T18:46:17Z | 2026-03-09T18:46:17Z |
| http://arxiv.org/abs/2603.08819v4 | Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage | 2026-03-09T18:20:20Z | 2026-06-20T21:46:17Z |
| http://arxiv.org/abs/2603.13371v1 | Agentic LLM Workflow for MR Spectroscopy Volume-of-Interest Placements in Brain Tumors | 2026-03-09T18:13:28Z | 2026-03-09T18:13:28Z |
| http://arxiv.org/abs/2603.08812v1 | VisionCreator-R1: A Reflection-Enhanced Native Visual-Generation Agentic Model | 2026-03-09T18:10:49Z | 2026-03-09T18:10:49Z |
| http://arxiv.org/abs/2603.08806v1 | Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications | 2026-03-09T18:04:54Z | 2026-03-09T18:04:54Z |

四主题重叠去重170个发现身份；不是170个当窗新公开/候选/已排除贡献。当前正式候选尚未冻结，不继承旧656/41。

