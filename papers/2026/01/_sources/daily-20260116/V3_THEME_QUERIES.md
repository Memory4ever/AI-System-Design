# Bounded main and supplemental theme queries

Fetched2026-10-03. Submission buffer only discovery, not publication ownership. Each querymax200 titles; no abstracts/fulltext inferred read. Delayedsubmitted events separately recovered withboundedDataCite metadata. Broader initialquantization query was narrowed to explicit model/system scopes here.

```json
[
  {
    "theme": "main-system",
    "query": "submittedDate:[202601131800 TO 202601141900] AND (cat:cs.DC OR cat:cs.AR OR cat:cs.OS OR cat:cs.PF OR cat:cs.PL) AND (all:LLM OR all:language OR all:GPU OR all:Transformer)",
    "pages": [
      {
        "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202601131800+TO+202601141900%5D+AND+%28cat%3Acs.DC+OR+cat%3Acs.AR+OR+cat%3Acs.OS+OR+cat%3Acs.PF+OR+cat%3Acs.PL%29+AND+%28all%3ALLM+OR+all%3Alanguage+OR+all%3AGPU+OR+all%3ATransformer%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
        "count": 7,
        "total": 7
      }
    ],
    "titles": [
      {
        "id": "http://arxiv.org/abs/2601.08800v1",
        "title": "MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm"
      },
      {
        "id": "http://arxiv.org/abs/2601.09076v1",
        "title": "Lean Clients, Full Accuracy: Hybrid Zeroth- and First-Order Split Federated Learning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09217v2",
        "title": "Relational Hoare Logic for High-Level Synthesis of Hardware Accelerators"
      },
      {
        "id": "http://arxiv.org/abs/2601.09258v2",
        "title": "LatencyPrism: Online Non-intrusive Latency Sculpting for SLO-Guaranteed LLM Inference"
      },
      {
        "id": "http://arxiv.org/abs/2601.09282v2",
        "title": "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
      },
      {
        "id": "http://arxiv.org/abs/2601.09527v1",
        "title": "Private LLM Inference on Consumer Blackwell GPUs: A Practical Guide for Cost-Effective Local Deployment in SMEs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09583v1",
        "title": "MLIR-Forge: A Modular Framework for Language Smiths"
      }
    ],
    "stop": "finite max200, titles only; if total>200 remainderisolated else allactualquerypages"
  },
  {
    "theme": "model-learning",
    "query": "submittedDate:[202601131800 TO 202601141900] AND cat:cs.LG AND (all:Transformer OR all:foundation OR all:MoE OR all:language OR all:pretraining OR all:quantization)",
    "pages": [
      {
        "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202601131800+TO+202601141900%5D+AND+cat%3Acs.LG+AND+%28all%3ATransformer+OR+all%3Afoundation+OR+all%3AMoE+OR+all%3Alanguage+OR+all%3Apretraining+OR+all%3Aquantization%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
        "count": 68,
        "total": 68
      }
    ],
    "titles": [
      {
        "id": "http://arxiv.org/abs/2601.16999v1",
        "title": "Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction"
      },
      {
        "id": "http://arxiv.org/abs/2601.08777v2",
        "title": "Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling"
      },
      {
        "id": "http://arxiv.org/abs/2601.08808v1",
        "title": "Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge"
      },
      {
        "id": "http://arxiv.org/abs/2601.08901v1",
        "title": "Navigating Ideation Space: Decomposed Conceptual Representations for Positioning Scientific Ideas"
      },
      {
        "id": "http://arxiv.org/abs/2601.08828v2",
        "title": "Motion Attribution for Video Generation"
      },
      {
        "id": "http://arxiv.org/abs/2601.08919v2",
        "title": "LLMs as Assessors: Right for the Right Reason?"
      },
      {
        "id": "http://arxiv.org/abs/2601.08955v3",
        "title": "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.08991v2",
        "title": "Optimising for Energy Efficiency and Performance in Machine Learning"
      },
      {
        "id": "http://arxiv.org/abs/2601.08999v1",
        "title": "Physics-Guided Counterfactual Explanations for Large-Scale Multivariate Time Series: Application in Scalable and Interpretable SEP Event Prediction"
      },
      {
        "id": "http://arxiv.org/abs/2601.09000v1",
        "title": "Universal Dynamics of Warmup Stable Decay: understanding WSD beyond Transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09025v2",
        "title": "Universal Latent Homeomorphic Manifolds: A Framework for Cross-Domain Representation Unification"
      },
      {
        "id": "http://arxiv.org/abs/2601.09026v2",
        "title": "Layer-Parallel Training for Transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09043v1",
        "title": "Horseshoe Mixtures-of-Experts (HS-MoE)"
      },
      {
        "id": "http://arxiv.org/abs/2603.21018v1",
        "title": "DSL-R1: From SQL to DSL for Training Retrieval Agents across Structured and Unstructured Data with Reinforcement Learning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09076v1",
        "title": "Lean Clients, Full Accuracy: Hybrid Zeroth- and First-Order Split Federated Learning"
      },
      {
        "id": "http://arxiv.org/abs/2603.21022v1",
        "title": "Knowledge Boundary Discovery for Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09083v1",
        "title": "SRT: Accelerating Reinforcement Learning via Speculative Rollout with Tree-Structured Cache"
      },
      {
        "id": "http://arxiv.org/abs/2601.09084v2",
        "title": "How Many Human Judgments Are Enough? Feasibility Limits of Human Preference Evaluation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09085v2",
        "title": "MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting"
      },
      {
        "id": "http://arxiv.org/abs/2601.09088v1",
        "title": "Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09093v2",
        "title": "Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling"
      },
      {
        "id": "http://arxiv.org/abs/2601.09096v1",
        "title": "Comparative Assessment of Concrete Compressive Strength Prediction at Industry Scale Using Embedding-based Neural Networks, Transformers, and Traditional Machine Learning Approaches"
      },
      {
        "id": "http://arxiv.org/abs/2601.11629v2",
        "title": "Semantic Differentiation for Tackling Challenges in Watermarking Low-Entropy Constrained Generation Outputs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09103v1",
        "title": "Enhancing Imbalanced Electrocardiogram Classification: A Novel Approach Integrating Data Augmentation through Wavelet Transform and Interclass Fusion"
      },
      {
        "id": "http://arxiv.org/abs/2601.10759v2",
        "title": "Mass Distribution versus Density Distribution in the Context of Clustering"
      },
      {
        "id": "http://arxiv.org/abs/2601.09142v2",
        "title": "EvasionBench: A Large-Scale Benchmark for Detecting Managerial Evasion in Earnings Call Q&A"
      },
      {
        "id": "http://arxiv.org/abs/2601.14287v2",
        "title": "Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09151v1",
        "title": "Interpretable Probability Estimation with LLMs via Shapley Reconstruction"
      },
      {
        "id": "http://arxiv.org/abs/2601.09157v1",
        "title": "Deep Learning-based Binary Analysis for Vulnerability Detection in x86-64 Machine Code"
      },
      {
        "id": "http://arxiv.org/abs/2601.20868v2",
        "title": "Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization"
      },
      {
        "id": "http://arxiv.org/abs/2601.09165v1",
        "title": "Multi-Teacher Ensemble Distillation: A Mathematical Framework for Probability-Domain Knowledge Aggregation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09170v1",
        "title": "N-EIoU-YOLOv9: A Signal-Aware Bounding Box Regression Loss for Lightweight Mobile Detection of Rice Leaf Diseases"
      },
      {
        "id": "http://arxiv.org/abs/2601.09172v3",
        "title": "BalDRO: A Distributionally Robust Optimization based Framework for Large Language Model Unlearning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09173v6",
        "title": "Geometric Stability: The Missing Axis of Representations"
      },
      {
        "id": "http://arxiv.org/abs/2601.09176v1",
        "title": "$D^2Prune$: Sparsifying Large Language Models via Dual Taylor Expansion and Attention Distribution Awareness"
      },
      {
        "id": "http://arxiv.org/abs/2601.09220v2",
        "title": "From Hawkes Processes to Attention: Time-Modulated Mechanisms for Event Sequences"
      },
      {
        "id": "http://arxiv.org/abs/2601.09233v3",
        "title": "GIFT: Reconciling Post-Training Objectives via Variational Finite-Temperature Gibbs Initialization"
      },
      {
        "id": "http://arxiv.org/abs/2601.09237v1",
        "title": "XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs"
      },
      {
        "id": "http://arxiv.org/abs/2601.17006v1",
        "title": "MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09282v2",
        "title": "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
      },
      {
        "id": "http://arxiv.org/abs/2601.09285v2",
        "title": "Enhancing Spatial Reasoning in Large Language Models for Metal-Organic Frameworks Structure Prediction"
      },
      {
        "id": "http://arxiv.org/abs/2601.09334v1",
        "title": "High-Performance Serverless Computing: A Systematic Literature Review on Serverless for HPC, AI, and Big Data"
      },
      {
        "id": "http://arxiv.org/abs/2601.09398v1",
        "title": "Ability Transfer and Recovery via Modularized Parameters Localization"
      },
      {
        "id": "http://arxiv.org/abs/2602.02498v2",
        "title": "Test-Time Detoxification without Training or Learning Anything"
      },
      {
        "id": "http://arxiv.org/abs/2601.09428v1",
        "title": "Draw it like Euclid: Teaching transformer models to generate CAD profiles using ruler and compass construction steps"
      },
      {
        "id": "http://arxiv.org/abs/2601.09433v1",
        "title": "Do Transformers Understand Ancient Roman Coin Motifs Better than CNNs?"
      },
      {
        "id": "http://arxiv.org/abs/2601.09451v1",
        "title": "Late Breaking Results: Quamba-SE: Soft-edge Quantizer for Activations in State Space Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09460v1",
        "title": "SoK: Enhancing Cryptographic Collaborative Learning with Differential Privacy"
      },
      {
        "id": "http://arxiv.org/abs/2601.09467v1",
        "title": "Searth Transformer: A Transformer Architecture Incorporating Earth's Geospheric Physical Priors for Global Mid-Range Weather Forecasting"
      },
      {
        "id": "http://arxiv.org/abs/2601.09473v2",
        "title": "SimMerge: Learning to Select Merge Operators from Similarity Signals"
      },
      {
        "id": "http://arxiv.org/abs/2601.09495v3",
        "title": "Parallelizable memory recurrent units"
      },
      {
        "id": "http://arxiv.org/abs/2601.09512v2",
        "title": "CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion"
      },
      {
        "id": "http://arxiv.org/abs/2601.17010v1",
        "title": "Optimizing the Landscape of LLM Embeddings with Dynamic Exploratory Graph Analysis for Generative Psychometrics: A Monte Carlo Study"
      },
      {
        "id": "http://arxiv.org/abs/2601.09527v1",
        "title": "Private LLM Inference on Consumer Blackwell GPUs: A Practical Guide for Cost-Effective Local Deployment in SMEs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09533v1",
        "title": "Residual Power Flow for Neural Solvers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09588v2",
        "title": "Energy-Entropy Regularization: The True Power of Minimal Looped Transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09603v1",
        "title": "Linear Complexity Self-Supervised Learning for Music Understanding with Random Quantizer"
      },
      {
        "id": "http://arxiv.org/abs/2601.11641v3",
        "title": "Mixture of Distributions Matters: Dynamic Sparse Attention for Efficient Video Diffusion Transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09624v2",
        "title": "A Mechanistic Perspective and Circuit-Guided Difficulty Metric for Unlearning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09626v1",
        "title": "From Prompt to Protocol: Fast Charging Batteries with Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09654v1",
        "title": "Exploring Fine-Tuning for Tabular Foundation Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09775v1",
        "title": "The Geometry of Thought: Disclosing the Transformer as a Tropical Polynomial Circuit"
      },
      {
        "id": "http://arxiv.org/abs/2601.09776v2",
        "title": "TimeSAE: Causal Sparse Decoding for Faithful Explanations of Black-Box Time Series Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09684v1",
        "title": "Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection"
      },
      {
        "id": "http://arxiv.org/abs/2601.09692v1",
        "title": "Routing with Generated Data: Annotation-Free LLM Skill Estimation and Expert Selection"
      },
      {
        "id": "http://arxiv.org/abs/2601.09693v3",
        "title": "Contrastive Geometric Learning Unlocks Unified Structure- and Ligand-Based Drug Design"
      },
      {
        "id": "http://arxiv.org/abs/2601.09706v1",
        "title": "Value-Aware Numerical Representations for Transformer Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09708v2",
        "title": "Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning"
      }
    ],
    "stop": "finite max200, titles only; if total>200 remainderisolated else allactualquerypages"
  },
  {
    "theme": "multimodal-embodied",
    "query": "submittedDate:[202601131800 TO 202601141900] AND (cat:cs.CV OR cat:cs.RO) AND (all:multimodal OR all:foundation OR all:diffusion OR all:VLA OR all:\"world model\")",
    "pages": [
      {
        "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202601131800+TO+202601141900%5D+AND+%28cat%3Acs.CV+OR+cat%3Acs.RO%29+AND+%28all%3Amultimodal+OR+all%3Afoundation+OR+all%3Adiffusion+OR+all%3AVLA+OR+all%3A%22world+model%22%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
        "count": 48,
        "total": 48
      }
    ],
    "titles": [
      {
        "id": "http://arxiv.org/abs/2601.08807v1",
        "title": "S3-CLIP: Video Super Resolution for Person-ReID"
      },
      {
        "id": "http://arxiv.org/abs/2601.08811v1",
        "title": "Reasoning Matters for 3D Visual Grounding"
      },
      {
        "id": "http://arxiv.org/abs/2601.08832v1",
        "title": "RAVEN: Erasing Invisible Watermarks via Novel View Synthesis"
      },
      {
        "id": "http://arxiv.org/abs/2601.08953v1",
        "title": "Fairness risk and its privacy-enabled solution in AI-driven robotic applications"
      },
      {
        "id": "http://arxiv.org/abs/2601.08956v1",
        "title": "Variance-Penalized MC-Dropout as a Learned Smoothing Prior for Brain Tumour Segmentation"
      },
      {
        "id": "http://arxiv.org/abs/2601.08977v1",
        "title": "Thermo-LIO: A Novel Multi-Sensor Integrated System for Structural Health Monitoring"
      },
      {
        "id": "http://arxiv.org/abs/2601.08982v2",
        "title": "SAM-pose2seg: Pose-Guided Human Instance Segmentation in Crowds"
      },
      {
        "id": "http://arxiv.org/abs/2601.09031v1",
        "title": "Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09044v1",
        "title": "POWDR: Pathology-preserving Outpainting with Wavelet Diffusion for 3D MRI"
      },
      {
        "id": "http://arxiv.org/abs/2601.11630v1",
        "title": "A one-step generation model with a Single-Layer Transformer: Layer number re-distillation of FreeFlow"
      },
      {
        "id": "http://arxiv.org/abs/2601.09105v2",
        "title": "AviationLMM: A Large Multimodal Foundation Model for Civil Aviation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09107v1",
        "title": "Vision Foundation Models for Domain Generalisable Cross-View Localisation in Planetary Ground-Aerial Robotic Teams"
      },
      {
        "id": "http://arxiv.org/abs/2601.09108v1",
        "title": "Small but Mighty: Dynamic Wavelet Expert-Guided Fine-Tuning of Large-Scale Models for Optical Remote Sensing Object Segmentation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09110v2",
        "title": "SAM-Aug: Leveraging SAM Priors for Few-Shot Parcel Segmentation in Satellite Time Series"
      },
      {
        "id": "http://arxiv.org/abs/2601.09116v1",
        "title": "LP-LLM: End-to-End Real-World Degraded License Plate Text Recognition via Large Multimodal Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09118v2",
        "title": "LPCAN: Lightweight Pyramid Cross-Attention Network for Rail Surface Defect Detection Using RGB-D Data"
      },
      {
        "id": "http://arxiv.org/abs/2601.09130v1",
        "title": "Equi-ViT: Rotational Equivariant Vision Transformer for Robust Histopathology Analysis"
      },
      {
        "id": "http://arxiv.org/abs/2601.09136v1",
        "title": "SkinFlow: Efficient Information Transmission for Open Dermatological Diagnosis via Dynamic Visual Encoding and Staged RL"
      },
      {
        "id": "http://arxiv.org/abs/2601.09163v1",
        "title": "CEI: A Unified Interface for Cross-Embodiment Visuomotor Policy Learning in 3D Space"
      },
      {
        "id": "http://arxiv.org/abs/2601.09213v1",
        "title": "SpikeVAEDiff: Neural Spike-based Natural Visual Scene Reconstruction via VD-VAE and Versatile Diffusion"
      },
      {
        "id": "http://arxiv.org/abs/2601.09231v1",
        "title": "Online Trajectory Optimization for Arbitrary-Shaped Mobile Robots via Polynomial Separating Hypersurfaces"
      },
      {
        "id": "http://arxiv.org/abs/2601.09238v2",
        "title": "Knowledge-Embedded and Hypernetwork-Guided Few-Shot Substation Meter Defect Image Generation Method"
      },
      {
        "id": "http://arxiv.org/abs/2601.09255v1",
        "title": "PhyRPR: Training-Free Physics-Constrained Video Generation"
      },
      {
        "id": "http://arxiv.org/abs/2601.11634v1",
        "title": "When Rules Fall Short: Agent-Driven Discovery of Emerging Content Issues in Short Video Platforms"
      },
      {
        "id": "http://arxiv.org/abs/2601.09298v2",
        "title": "Multi-Modal LLM based Image Captioning in ICT: Bridging the Gap Between General and Industry Domain"
      },
      {
        "id": "http://arxiv.org/abs/2601.09316v1",
        "title": "Frequency Error-Guided Under-sampling Optimization for Multi-Contrast MRI Reconstruction"
      },
      {
        "id": "http://arxiv.org/abs/2601.11635v1",
        "title": "Now You See Me, Now You Don't: A Unified Framework for Expression Consistent Anonymization in Talking Head Videos"
      },
      {
        "id": "http://arxiv.org/abs/2601.09322v2",
        "title": "Attentive multilayer fusion for vision transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09350v1",
        "title": "See More, Store Less: Memory-Efficient Resolution for Video Moment Retrieval"
      },
      {
        "id": "http://arxiv.org/abs/2601.09377v1",
        "title": "ReflexDiffusion: Reflection-Enhanced Trajectory Planning for High-lateral-acceleration Scenarios in Autonomous Driving"
      },
      {
        "id": "http://arxiv.org/abs/2601.09416v1",
        "title": "Radiomics-Integrated Deep Learning with Hierarchical Loss for Osteosarcoma Histology Classification"
      },
      {
        "id": "http://arxiv.org/abs/2601.09430v1",
        "title": "Video-MSR: Benchmarking Multi-hop Spatial Reasoning Capabilities of MLLMs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09452v1",
        "title": "MAD: Motion Appearance Decoupling for efficient Driving World Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09512v2",
        "title": "CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion"
      },
      {
        "id": "http://arxiv.org/abs/2601.09518v1",
        "title": "Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations"
      },
      {
        "id": "http://arxiv.org/abs/2601.09528v1",
        "title": "GlovEgo-HOI: Bridging the Synthetic-to-Real Gap for Industrial Egocentric Human-Object Interaction Detection"
      },
      {
        "id": "http://arxiv.org/abs/2601.11637v1",
        "title": "Evaluating Self-Correcting Vision Agents Through Quantitative and Qualitative Metrics"
      },
      {
        "id": "http://arxiv.org/abs/2601.09572v2",
        "title": "Trustworthy Longitudinal Brain MRI Completion: A Deformation-Based Approach with KAN-Enhanced Diffusion Model"
      },
      {
        "id": "http://arxiv.org/abs/2601.09578v1",
        "title": "Multimodal Signal Processing For Thermo-Visible-Lidar Fusion In Real-time 3D Semantic Mapping"
      },
      {
        "id": "http://arxiv.org/abs/2601.11641v3",
        "title": "Mixture of Distributions Matters: Dynamic Sparse Attention for Efficient Video Diffusion Transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09606v1",
        "title": "GRCF: Two-Stage Groupwise Ranking and Calibration Framework for Multimodal Sentiment Analysis"
      },
      {
        "id": "http://arxiv.org/abs/2601.09613v1",
        "title": "CogRail: Benchmarking VLMs in Cognitive Intrusion Perception for Intelligent Railway Transportation Systems"
      },
      {
        "id": "http://arxiv.org/abs/2601.09668v2",
        "title": "STEP3-VL-10B Technical Report"
      },
      {
        "id": "http://arxiv.org/abs/2601.10687v1",
        "title": "A continental-scale dataset of ground beetles with high-resolution images and validated morphological trait measurements"
      },
      {
        "id": "http://arxiv.org/abs/2601.09694v1",
        "title": "LLMs can Compress LLMs: Adaptive Pruning by Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09697v1",
        "title": "Efficient Camera-Controlled Video Generation of Static Scenes via Sparse Diffusion and 3D Rendering"
      },
      {
        "id": "http://arxiv.org/abs/2601.09699v1",
        "title": "SAM3-DMS: Decoupled Memory Selection for Multi-target Video Segmentation of SAM3"
      },
      {
        "id": "http://arxiv.org/abs/2601.09708v2",
        "title": "Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning"
      }
    ],
    "stop": "finite max200, titles only; if total>200 remainderisolated else allactualquerypages"
  },
  {
    "theme": "rag-agent",
    "query": "submittedDate:[202601131800 TO 202601141900] AND (cat:cs.IR OR cat:cs.MA OR cat:cs.AI) AND (all:LLM OR all:language OR all:agent OR all:RAG OR all:memory)",
    "pages": [
      {
        "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202601131800+TO+202601141900%5D+AND+%28cat%3Acs.IR+OR+cat%3Acs.MA+OR+cat%3Acs.AI%29+AND+%28all%3ALLM+OR+all%3Alanguage+OR+all%3Aagent+OR+all%3ARAG+OR+all%3Amemory%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
        "count": 100,
        "total": 128
      },
      {
        "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202601131800+TO+202601141900%5D+AND+%28cat%3Acs.IR+OR+cat%3Acs.MA+OR+cat%3Acs.AI%29+AND+%28all%3ALLM+OR+all%3Alanguage+OR+all%3Aagent+OR+all%3ARAG+OR+all%3Amemory%29&start=100&max_results=100&sortBy=submittedDate&sortOrder=ascending",
        "count": 28,
        "total": 128
      }
    ],
    "titles": [
      {
        "id": "http://arxiv.org/abs/2601.08773v1",
        "title": "Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs"
      },
      {
        "id": "http://arxiv.org/abs/2601.08777v2",
        "title": "Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling"
      },
      {
        "id": "http://arxiv.org/abs/2601.08778v3",
        "title": "Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards"
      },
      {
        "id": "http://arxiv.org/abs/2601.08785v1",
        "title": "Uncovering Political Bias in Large Language Models using Parliamentary Voting Records"
      },
      {
        "id": "http://arxiv.org/abs/2601.08806v3",
        "title": "APEX-SWE"
      },
      {
        "id": "http://arxiv.org/abs/2601.08808v1",
        "title": "Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge"
      },
      {
        "id": "http://arxiv.org/abs/2601.08811v1",
        "title": "Reasoning Matters for 3D Visual Grounding"
      },
      {
        "id": "http://arxiv.org/abs/2601.08815v3",
        "title": "Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems"
      },
      {
        "id": "http://arxiv.org/abs/2601.08816v3",
        "title": "MemRec: Collaborative Memory-Augmented Agentic Recommender System"
      },
      {
        "id": "http://arxiv.org/abs/2601.08901v1",
        "title": "Navigating Ideation Space: Decomposed Conceptual Representations for Positioning Scientific Ideas"
      },
      {
        "id": "http://arxiv.org/abs/2601.08829v1",
        "title": "Modeling LLM Agent Reviewer Dynamics in Elo-Ranked Review System"
      },
      {
        "id": "http://arxiv.org/abs/2601.08919v2",
        "title": "LLMs as Assessors: Right for the Right Reason?"
      },
      {
        "id": "http://arxiv.org/abs/2601.09756v1",
        "title": "Synthetic Data for Veterinary EHR De-identification: Benefits, Limits, and Safety Trade-offs Under Fixed Compute"
      },
      {
        "id": "http://arxiv.org/abs/2601.08950v4",
        "title": "ConvoLearn: A Learning Sciences Grounded Dataset for Fine-Tuning Dialogic AI Tutors"
      },
      {
        "id": "http://arxiv.org/abs/2601.08951v2",
        "title": "PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm"
      },
      {
        "id": "http://arxiv.org/abs/2601.08955v3",
        "title": "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.08988v1",
        "title": "ART: Action-based Reasoning Task Benchmarking for Medical AI Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09012v3",
        "title": "TranslateGemma Technical Report"
      },
      {
        "id": "http://arxiv.org/abs/2601.09028v2",
        "title": "OpenDecoder: Open Large Language Model Decoding to Incorporate Document Quality in RAG"
      },
      {
        "id": "http://arxiv.org/abs/2601.09029v1",
        "title": "Proactively Detecting Threats: A Novel Approach Using LLMs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09031v1",
        "title": "Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09032v1",
        "title": "The Hierarchy of Agentic Capabilities: Evaluating Frontier Models on Realistic RL Environments"
      },
      {
        "id": "http://arxiv.org/abs/2601.09035v1",
        "title": "A Decompilation-Driven Framework for Malware Detection with Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09036v1",
        "title": "SpectraQuery: A Hybrid Retrieval-Augmented Conversational Assistant for Battery Science"
      },
      {
        "id": "http://arxiv.org/abs/2601.09041v1",
        "title": "Can LLMs interpret figurative language as humans do?: surface-level vs representational similarity"
      },
      {
        "id": "http://arxiv.org/abs/2601.09049v1",
        "title": "Is Grokking Worthwhile? Functional Analysis and Transferability of Generalization Circuits in Transformers"
      },
      {
        "id": "http://arxiv.org/abs/2601.09056v5",
        "title": "StegoStylo: Squelching Stylometric Scrutiny through Steganographic Stitching"
      },
      {
        "id": "http://arxiv.org/abs/2602.00017v1",
        "title": "SafeTalkCoach: Diversity-Driven Multi-Agent Simulation for Parent-Teen Health Conversations"
      },
      {
        "id": "http://arxiv.org/abs/2601.09066v1",
        "title": "Mi:dm 2.0 Korea-centric Bilingual Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09069v1",
        "title": "From Symbolic to Natural-Language Relations: Rethinking Knowledge Graph Construction in the Era of Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09072v1",
        "title": "Human-AI Co-design for Clinical Prediction Models"
      },
      {
        "id": "http://arxiv.org/abs/2603.21018v1",
        "title": "DSL-R1: From SQL to DSL for Training Retrieval Agents across Structured and Unstructured Data with Reinforcement Learning"
      },
      {
        "id": "http://arxiv.org/abs/2603.21022v1",
        "title": "Knowledge Boundary Discovery for Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09085v2",
        "title": "MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting"
      },
      {
        "id": "http://arxiv.org/abs/2601.09089v1",
        "title": "SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding"
      },
      {
        "id": "http://arxiv.org/abs/2601.09097v4",
        "title": "Programming over Thinking: Efficient and Robust Multi-Constraint Planning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09100v2",
        "title": "DScheLLM: Enabling Dynamic Scheduling through a Fine-Tuned Dual-System Large language Model"
      },
      {
        "id": "http://arxiv.org/abs/2601.09105v2",
        "title": "AviationLMM: A Large Multimodal Foundation Model for Civil Aviation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09113v1",
        "title": "The AI Hippocampus: How Far are We From Human Memory?"
      },
      {
        "id": "http://arxiv.org/abs/2601.09116v1",
        "title": "LP-LLM: End-to-End Real-World Degraded License Plate Text Recognition via Large Multimodal Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09120v1",
        "title": "Adaptive Multi-Stage Patent Claim Generation with Unified Quality Assessment"
      },
      {
        "id": "http://arxiv.org/abs/2601.09760v1",
        "title": "Investigating Tool-Memory Conflicts in Tool-Augmented LLMs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09136v1",
        "title": "SkinFlow: Efficient Information Transmission for Open Dermatological Diagnosis via Dynamic Visual Encoding and Staged RL"
      },
      {
        "id": "http://arxiv.org/abs/2601.09147v2",
        "title": "SSVP: Synergistic Semantic-Visual Prompting for Industrial Zero-Shot Anomaly Detection"
      },
      {
        "id": "http://arxiv.org/abs/2601.09152v2",
        "title": "PrivacyReasoner: Can LLM Emulate a Human-like Privacy Mind?"
      },
      {
        "id": "http://arxiv.org/abs/2601.09159v4",
        "title": "LLMs Meet Isolation Kernel: Lightweight, Learning-free Binary Embeddings for Fast Retrieval"
      },
      {
        "id": "http://arxiv.org/abs/2601.20868v2",
        "title": "Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization"
      },
      {
        "id": "http://arxiv.org/abs/2601.09182v1",
        "title": "Position on LLM-Assisted Peer Review: Addressing Reviewer Gap through Mentoring and Feedback"
      },
      {
        "id": "http://arxiv.org/abs/2601.09195v3",
        "title": "ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection"
      },
      {
        "id": "http://arxiv.org/abs/2603.21024v1",
        "title": "Query, Decompose, Compress: Structured Query Expansion for Efficient Multi-Hop Retrieval"
      },
      {
        "id": "http://arxiv.org/abs/2601.09200v5",
        "title": "A.X K1 Technical Report"
      },
      {
        "id": "http://arxiv.org/abs/2601.09208v2",
        "title": "Mikasa: A Character-Driven Emotional AI Companion Inspired by Japanese Oshi Culture"
      },
      {
        "id": "http://arxiv.org/abs/2601.09233v3",
        "title": "GIFT: Reconciling Post-Training Objectives via Variational Finite-Temperature Gibbs Initialization"
      },
      {
        "id": "http://arxiv.org/abs/2602.02497v1",
        "title": "STEMVerse: A Dual-Axis Diagnostic Framework for STEM Reasoning in Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09239v6",
        "title": "DSA-Tokenizer: Disentangled Semantic-Acoustic Tokenization via Flow Matching-based Hierarchical Fusion"
      },
      {
        "id": "http://arxiv.org/abs/2601.17006v1",
        "title": "MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09248v1",
        "title": "Hybrid guided variational autoencoder for visual place recognition"
      },
      {
        "id": "http://arxiv.org/abs/2602.06052v4",
        "title": "A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09253v2",
        "title": "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09259v1",
        "title": "MAXS: Meta-Adaptive Exploration with LLM Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09260v1",
        "title": "Efficient Paths and Dense Rewards: Probabilistic Flow Reasoning for Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09264v1",
        "title": "Coordinated Pandemic Control with Large Language Model Agents as Policymaking Assistants"
      },
      {
        "id": "http://arxiv.org/abs/2601.09269v2",
        "title": "RISER: Orchestrating Latent Reasoning Skills for Adaptive Activation Steering"
      },
      {
        "id": "http://arxiv.org/abs/2601.09274v1",
        "title": "$A^3$-Bench: Benchmarking Memory-Driven Scientific Reasoning via Anchor and Attractor Activation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09278v1",
        "title": "M$^3$Searcher: Modular Multimodal Information Seeking Agency with Retrieval-Oriented Reasoning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09762v1",
        "title": "Explicating Tacit Regulatory Knowledge from LLMs to Auto-Formalize Requirements for Compliance Test Case Generation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09280v1",
        "title": "ReGraM: Region-First Knowledge Graph Reasoning for Medical Question Answering"
      },
      {
        "id": "http://arxiv.org/abs/2601.09281v1",
        "title": "STaR: Sensitive Trajectory Regulation for Unlearning in Large Reasoning Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09282v2",
        "title": "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
      },
      {
        "id": "http://arxiv.org/abs/2601.09292v1",
        "title": "Blue Teaming Function-Calling Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09293v1",
        "title": "Policy-Based Reinforcement Learning with Action Masking for Dynamic Job Shop Scheduling under Uncertainty: Handling Random Arrivals and Machine Failures"
      },
      {
        "id": "http://arxiv.org/abs/2601.09295v3",
        "title": "MACRO-LLM: LLM-Empowered Multi-Agent Collaborative Reasoning under Spatiotemporal Partial Observability"
      },
      {
        "id": "http://arxiv.org/abs/2601.09306v1",
        "title": "On-Device Large Language Models for Sequential Recommendation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09313v2",
        "title": "Understanding or Memorizing? A Case Study of German Definite Articles in Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.14288v2",
        "title": "DeepInflation: an AI agent for research and model discovery of inflation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09342v2",
        "title": "Improving Implicit Hate Speech Detection via a Community-Driven Multi-Agent Framework"
      },
      {
        "id": "http://arxiv.org/abs/2601.09353v1",
        "title": "Monte-Carlo Tree Search with Neural Network Guidance for Lane-Free Autonomous Driving"
      },
      {
        "id": "http://arxiv.org/abs/2601.09365v2",
        "title": "Frame of Reference: Addressing the Challenges of Common Ground Representation in Situational Dialogs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09381v1",
        "title": "Query Languages for Machine-Learning Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09382v1",
        "title": "Long-term Task-oriented Agent: Proactive Long-term Intent Maintenance in Dynamic Environments"
      },
      {
        "id": "http://arxiv.org/abs/2601.14289v2",
        "title": "RPC-Bench: A Fine-grained Benchmark for Research Paper Comprehension"
      },
      {
        "id": "http://arxiv.org/abs/2601.09398v1",
        "title": "Ability Transfer and Recovery via Modularized Parameters Localization"
      },
      {
        "id": "http://arxiv.org/abs/2602.02498v2",
        "title": "Test-Time Detoxification without Training or Learning Anything"
      },
      {
        "id": "http://arxiv.org/abs/2601.09413v2",
        "title": "Speech-Hands: A Self-Reflection Voice Agentic Approach to Speech Recognition and Audio Reasoning with Omni Perception"
      },
      {
        "id": "http://arxiv.org/abs/2601.09421v2",
        "title": "Bias Dynamics in BabyLMs: Towards a Compute-Efficient Sandbox for Democratising Pre-Training Debiasing"
      },
      {
        "id": "http://arxiv.org/abs/2603.22625v1",
        "title": "Leveraging Large Language Models to Extract and Translate Medical Information in Doctors' Notes for Health Records and Diagnostic Billing Codes"
      },
      {
        "id": "http://arxiv.org/abs/2601.09434v1",
        "title": "SC-MAS: Constructing Cost-Efficient Multi-Agent Systems with Edge-Level Heterogeneous Collaboration"
      },
      {
        "id": "http://arxiv.org/abs/2601.09445v2",
        "title": "Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09446v1",
        "title": "Improving Symbolic Translation of Language Models for Logical Reasoning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09448v3",
        "title": "One Prompt, Many Sounds: Modeling Listener Variability in LLM-Based Equalization"
      },
      {
        "id": "http://arxiv.org/abs/2601.09459v1",
        "title": "Dissecting Judicial Reasoning in U.S. Copyright Damage Awards"
      },
      {
        "id": "http://arxiv.org/abs/2601.09465v2",
        "title": "EvoFSM: Controllable Self-Evolution for Deep Research with Finite State Machines"
      },
      {
        "id": "http://arxiv.org/abs/2601.09467v1",
        "title": "Searth Transformer: A Transformer Architecture Incorporating Earth's Geospheric Physical Priors for Global Mid-Range Weather Forecasting"
      },
      {
        "id": "http://arxiv.org/abs/2601.09470v1",
        "title": "Personalized Multimodal Feedback Using Multiple External Representations: Strategy Profiles and Learning in High School Physics"
      },
      {
        "id": "http://arxiv.org/abs/2601.09473v2",
        "title": "SimMerge: Learning to Select Merge Operators from Similarity Signals"
      },
      {
        "id": "http://arxiv.org/abs/2601.09478v3",
        "title": "Bridging Semantic Understanding and Popularity Bias with LLMs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09496v2",
        "title": "Unifying Search and Recommendation in LLMs via Gradient Multi-Subspace Tuning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09503v1",
        "title": "What Do LLM Agents Know About Their World? Task2Quiz: A Paradigm for Studying Environment Understanding"
      },
      {
        "id": "http://arxiv.org/abs/2601.09770v1",
        "title": "GUI-Eyes: Tool-Augmented Perception for Visual Grounding in GUI Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09523v1",
        "title": "TEMPO: A Realistic Multi-Domain Benchmark for Temporal Reasoning-Intensive Retrieval"
      },
      {
        "id": "http://arxiv.org/abs/2601.09527v1",
        "title": "Private LLM Inference on Consumer Blackwell GPUs: A Practical Guide for Cost-Effective Local Deployment in SMEs"
      },
      {
        "id": "http://arxiv.org/abs/2601.09536v2",
        "title": "Omni-R1: Towards the Unified Generative Paradigm for Multimodal Reasoning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09771v1",
        "title": "PCN-Rec: Agentic Proof-Carrying Negotiation for Reliable Governance-Constrained Recommendation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09543v1",
        "title": "Examining DOM Coordinate Effectiveness For Page Segmentation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09555v1",
        "title": "Benchmarking Post-Training Quantization of Large Language Models under Microscaling Floating Point Formats"
      },
      {
        "id": "http://arxiv.org/abs/2601.15311v3",
        "title": "Aeon: High-Performance Neuro-Symbolic Memory Management for Long-Horizon LLM Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.09566v4",
        "title": "Hot-Start Chinese Language Modeling:Visual Glyphs Accelerate Sample-Efficient Learning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09772v1",
        "title": "Antisocial behavior towards large language model users: experimental evidence"
      },
      {
        "id": "http://arxiv.org/abs/2601.15312v1",
        "title": "Do people expect different behavior from large language models acting on their behalf? Evidence from norm elicitations in two canonical economic games"
      },
      {
        "id": "http://arxiv.org/abs/2601.09603v1",
        "title": "Linear Complexity Self-Supervised Learning for Music Understanding with Random Quantizer"
      },
      {
        "id": "http://arxiv.org/abs/2601.09609v1",
        "title": "DPWriter: Reinforcement Learning with Diverse Planning Branching for Creative Writing"
      },
      {
        "id": "http://arxiv.org/abs/2601.09613v1",
        "title": "CogRail: Benchmarking VLMs in Cognitive Intrusion Perception for Intelligent Railway Transportation Systems"
      },
      {
        "id": "http://arxiv.org/abs/2602.13209v1",
        "title": "LemonadeBench: Evaluating the Economic Intuition of Large Language Models in Simple Markets"
      },
      {
        "id": "http://arxiv.org/abs/2601.09624v2",
        "title": "A Mechanistic Perspective and Circuit-Guided Difficulty Metric for Unlearning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09625v2",
        "title": "The Promptware Kill Chain: How Prompt Injections Gradually Evolved Into a Multistep Malware Delivery Mechanism"
      },
      {
        "id": "http://arxiv.org/abs/2601.09626v1",
        "title": "From Prompt to Protocol: Fast Charging Batteries with Large Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09635v3",
        "title": "Large-Scale Optimization Model Auto-Formulation: Harnessing LLM Flexibility via Structured Workflow"
      },
      {
        "id": "http://arxiv.org/abs/2601.09636v2",
        "title": "PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records"
      },
      {
        "id": "http://arxiv.org/abs/2601.11643v1",
        "title": "Syllabic Agglutinative Tokenizations for Indonesian LLM: A Study from Gasing Literacy Learning System"
      },
      {
        "id": "http://arxiv.org/abs/2601.09667v2",
        "title": "Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning"
      },
      {
        "id": "http://arxiv.org/abs/2601.09680v1",
        "title": "Automating Supply Chain Disruption Monitoring via an Agentic AI Approach"
      },
      {
        "id": "http://arxiv.org/abs/2601.09684v1",
        "title": "Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection"
      },
      {
        "id": "http://arxiv.org/abs/2601.09692v1",
        "title": "Routing with Generated Data: Annotation-Free LLM Skill Estimation and Expert Selection"
      },
      {
        "id": "http://arxiv.org/abs/2601.09694v1",
        "title": "LLMs can Compress LLMs: Adaptive Pruning by Agents"
      },
      {
        "id": "http://arxiv.org/abs/2601.15313v2",
        "title": "Attention Is Not Retention: The Orthogonality Constraint in Infinite-Context Architectures"
      },
      {
        "id": "http://arxiv.org/abs/2601.09703v1",
        "title": "ShortCoder: Knowledge-Augmented Syntax Optimization for Token-Efficient Code Generation"
      },
      {
        "id": "http://arxiv.org/abs/2601.09706v1",
        "title": "Value-Aware Numerical Representations for Transformer Language Models"
      },
      {
        "id": "http://arxiv.org/abs/2601.09708v2",
        "title": "Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning"
      }
    ],
    "stop": "finite max200, titles only; if total>200 remainderisolated else allactualquerypages"
  }
]
```

