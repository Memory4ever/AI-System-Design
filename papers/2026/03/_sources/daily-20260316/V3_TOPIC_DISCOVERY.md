# 03/16 有限主题发现

窗口[03/15BJT09,03/16BJT09)。首轮无分类主题query出现transform/diffusive等泛数学命中且104/100上限，已收窄到foundation/Agent/多模态/系统相关分类+主题，未将宽命中转逐项队列。本记录为收窄后的4个start0/max100查询实际返回，SubmittedMar12T18→Mar13T18只作常规Sunday20EDT公告候选发现范围，不证明公开时间；早Submitted moderation/revision的历史主题切片另需有界查漏。各查询参数/返回标题如下，标题线索不是候选/题摘或Evidence完成。

```json
[
  {
    "name": "model-training",
    "query": "submittedDate:[202603121800 TO 202603131800] AND (cat:cs.CL OR cat:cs.LG OR cat:cs.AI) AND (ti:\"language model\" OR ti:LLM OR ti:Transformer OR ti:attention OR ti:\"expert routing\" OR ti:\"post-training\")",
    "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202603121800+TO+202603131800%5D+AND+%28cat%3Acs.CL+OR+cat%3Acs.LG+OR+cat%3Acs.AI%29+AND+%28ti%3A%22language+model%22+OR+ti%3ALLM+OR+ti%3ATransformer+OR+ti%3Aattention+OR+ti%3A%22expert+routing%22+OR+ti%3A%22post-training%22%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
    "total": "63",
    "titles": [
      [
        "2603.12343v1",
        "LLM-Augmented Therapy Normalization and Aspect-Based Sentiment Analysis for Treatment-Resistant Depression on Reddit"
      ],
      [
        "2603.12344v2",
        "Can Decision Trees Teach Large Language Models? Distilling Verbalized Knowledge for Molecular Property Prediction"
      ],
      [
        "2603.12350v1",
        "TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling"
      ],
      [
        "2603.23539v1",
        "PLDR-LLMs Reason At Self-Organized Criticality"
      ],
      [
        "2603.13418v2",
        "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models"
      ],
      [
        "2603.19303v1",
        "Agreement Between Large Language Models, Human Reviewers, and Authors in Evaluating STROBE Checklists for Observational Studies in Rheumatology"
      ],
      [
        "2604.06197v1",
        "Temporally Phenotyping GLP-1RA Case Reports with Large Language Models: A Textual Time Series Corpus and Risk Modeling"
      ],
      [
        "2603.12458v1",
        "Shattering the Shortcut: A Topology-Regularized Benchmark for Multi-hop Medical Reasoning in LLMs"
      ],
      [
        "2604.03263v1",
        "LPC-SM: Local Predictive Coding and Sparse Memory for Long-Context Language Modeling"
      ],
      [
        "2603.12465v1",
        "TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition"
      ],
      [
        "2603.12520v1",
        "When LLM Judge Scores Look Good but Best-of-N Decisions Fail"
      ],
      [
        "2603.12522v1",
        "LLM BiasScope: A Real-Time Bias Analysis Platform for Comparative LLM Evaluation"
      ],
      [
        "2603.12538v1",
        "Spatio-Semantic Expert Routing Architecture with Mixture-of-Experts for Referring Image Segmentation"
      ],
      [
        "2603.12541v1",
        "As Language Models Scale, Low-order Linear Depth Dynamics Emerge"
      ],
      [
        "2603.12554v2",
        "Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages"
      ],
      [
        "2603.12564v8",
        "Sell Me This Stock: Unsafe Recommendation Drift in LLM Agents"
      ],
      [
        "2603.13426v1",
        "Outcome-Aware Tool Selection for Semantic Routers: Latency-Constrained Learning Without LLM Inference"
      ],
      [
        "2603.13430v1",
        "Dynamic Sparse Attention: Access Patterns and Architecture"
      ],
      [
        "2603.12625v1",
        "VLM4Rec: Multimodal Semantic Representation for Recommendation with Large Vision-Language Models"
      ],
      [
        "2603.12634v1",
        "Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents"
      ],
      [
        "2603.12646v1",
        "98$\\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router"
      ],
      [
        "2603.12658v2",
        "Beyond Static Models: An Evolving Framework for Continual Learning in Large Language Models across Training Stages"
      ],
      [
        "2603.12666v3",
        "RetroReasoner: A Reasoning LLM for Strategic Retrosynthesis Prediction"
      ],
      [
        "2603.12681v2",
        "Colluding LoRA: A Compositional Vulnerability in LLM Safety Alignment"
      ],
      [
        "2603.12688v1",
        "STRAP-ViT: Segregated Tokens with Randomized -- Transformations for Defense against Adversarial Patches in ViTs"
      ],
      [
        "2603.12694v1",
        "RXNRECer Enables Fine-grained Enzymatic Function Annotation through Active Learning and Protein Language Models"
      ],
      [
        "2603.12702v2",
        "FGTR: Fine-Grained Multi-Table Retrieval via Hierarchical LLM Reasoning"
      ],
      [
        "2603.12707v1",
        "Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity"
      ],
      [
        "2603.12710v1",
        "AI Planning Framework for LLM-Based Web Agents"
      ],
      [
        "2603.12719v1",
        "IGASA: Integrated Geometry-Aware and Skip-Attention Modules for Enhanced Point Cloud Registration"
      ],
      [
        "2603.12721v1",
        "CMHANet: A Cross-Modal Hybrid Attention Network for Point Cloud Registration"
      ],
      [
        "2603.12724v1",
        "SciDesignBench: Benchmarking and Improving Language Models for Scientific Inverse Design"
      ],
      [
        "2603.12740v1",
        "ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning"
      ],
      [
        "2603.12744v1",
        "TaoBench: Do Automated Theorem Prover LLMs Generalize Beyond MathLib?"
      ],
      [
        "2603.12752v1",
        "Taming the Long Tail: Efficient Item-wise Sharpness-Aware Minimization for LLM-based Recommender Systems"
      ],
      [
        "2603.12768v1",
        "SectEval: Evaluating the Latent Sectarian Preferences of Large Language Models"
      ],
      [
        "2603.12823v1",
        "Adaptive Vision-Language Model Routing for Computer Use Agents"
      ],
      [
        "2603.12872v1",
        "CLARIN-PT-LDB: An Open LLM Leaderboard for Portuguese to assess Language, Culture and Civility"
      ],
      [
        "2603.12875v1",
        "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks"
      ],
      [
        "2603.12893v2",
        "Finite Difference Flow Optimization for RL Post-Training of Text-to-Image Models"
      ],
      [
        "2603.12895v1",
        "Human-Centered Evaluation of an LLM-Based Process Modeling Copilot: A Mixed-Methods Study with Domain Experts"
      ],
      [
        "2603.12916v4",
        "Surprised by Attention: Predictable Query Dynamics for Time Series Anomaly Detection"
      ],
      [
        "2604.13046v1",
        "A Domain-Specific Language for LLM-Driven Trigger Generation in Multimodal Data Collection"
      ],
      [
        "2603.12932v2",
        "DS$^2$-Instruct: Domain-Specific Data Synthesis for Large Language Models Instruction Tuning"
      ],
      [
        "2603.12933v1",
        "Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization"
      ],
      [
        "2603.12953v1",
        "Delta1 with LLM: symbolic and neural integration for credible and explainable reasoning"
      ],
      [
        "2603.13443v1",
        "NormCode Canvas: Making LLM Agentic Workflows Development Sustainable via Case-Based Reasoning"
      ],
      [
        "2604.04942v1",
        "TDA-RC: Task-Driven Alignment for Knowledge-Based Reasoning Chains in Large Language Models"
      ],
      [
        "2604.09613v2",
        "Token-Budget-Aware Pool Routing for Cost-Efficient LLM Inference"
      ],
      [
        "2603.24601v1",
        "FED-HARGPT: A Hybrid Centralized-Federated Approach of a Transformer-based Architecture for Human Context Recognition"
      ],
      [
        "2603.12988v1",
        "Fair Lung Disease Diagnosis from Chest CT via Gender-Adversarial Attention Multiple Instance Learning"
      ],
      [
        "2604.16337v1",
        "HR-Agents: Using Multiple LLM-based Agents to Improve Q&A about Brazilian Labor Legislation"
      ],
      [
        "2603.12996v2",
        "DAPD: Dependency-Aware Parallel Decoding via Attention for Diffusion LLMs"
      ],
      [
        "2603.23543v1",
        "Large Language Models and Scientific Discourse: Where's the Intelligence?"
      ],
      [
        "2603.13033v1",
        "ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models"
      ],
      [
        "2604.16339v1",
        "Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems"
      ],
      [
        "2603.13450v2",
        "LADR: Locality-Aware Dynamic Rescue for Efficient Text-to-Image Generation with Diffusion Large Language Models"
      ],
      [
        "2603.13083v1",
        "Human-in-the-Loop LLM Grading for Handwritten Mathematics Assessments"
      ],
      [
        "2603.13085v2",
        "Linearized Attention Cannot Enter the Kernel Regime at Any Practical Width"
      ],
      [
        "2603.13126v1",
        "Developing the PsyCogMetrics AI Lab to Evaluate Large Language Models and Advance Cognitive Science -- A Three-Cycle Action Design Science Study"
      ],
      [
        "2603.13461v1",
        "Purifying Generative LLMs from Backdoors without Prior Knowledge or Clean Reference"
      ],
      [
        "2603.13189v1",
        "LLM Constitutional Multi-Agent Governance"
      ],
      [
        "2603.13201v1",
        "Neuron-Aware Data Selection In Instruction Tuning For Large Language Models"
      ]
    ]
  },
  {
    "name": "agent-retrieval",
    "query": "submittedDate:[202603121800 TO 202603131800] AND (cat:cs.CL OR cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:memory OR ti:retrieval OR ti:reasoning OR ti:alignment)",
    "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202603121800+TO+202603131800%5D+AND+%28cat%3Acs.CL+OR+cat%3Acs.AI+OR+cat%3Acs.IR+OR+cat%3Acs.MA%29+AND+%28ti%3Aagent+OR+ti%3Amemory+OR+ti%3Aretrieval+OR+ti%3Areasoning+OR+ti%3Aalignment%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
    "total": "59",
    "titles": [
      [
        "2603.12310v1",
        "VQQA: An Agentic Approach for Video Evaluation and Quality Improvement"
      ],
      [
        "2603.12350v1",
        "TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling"
      ],
      [
        "2603.12368v1",
        "Multi-Step Semantic Reasoning in Generative Retrieval"
      ],
      [
        "2603.12372v3",
        "Efficient Reasoning with Balanced Thinking"
      ],
      [
        "2603.23539v1",
        "PLDR-LLMs Reason At Self-Organized Criticality"
      ],
      [
        "2603.12396v1",
        "Test-Time Strategies for More Efficient and Accurate Agentic RAG"
      ],
      [
        "2603.12397v1",
        "Not Just the Destination, But the Journey: Reasoning Traces Causally Shape Generalization Behaviors"
      ],
      [
        "2604.16333v1",
        "A Discordance-Aware Multimodal Framework with Multi-Agent Clinical Reasoning"
      ],
      [
        "2603.12458v1",
        "Shattering the Shortcut: A Topology-Regularized Benchmark for Multi-hop Medical Reasoning in LLMs"
      ],
      [
        "2604.03263v1",
        "LPC-SM: Local Predictive Coding and Sparse Memory for Long-Context Language Modeling"
      ],
      [
        "2604.03264v1",
        "SafeScreen: A Safety-First Screening Framework for Personalized Video Retrieval for Vulnerable Users"
      ],
      [
        "2603.12483v1",
        "Generating Expressive and Customizable Evals for Timeseries Data Analysis Agents with AgentFuel"
      ],
      [
        "2603.12529v2",
        "TERMINATOR: Learning Optimal Exit Points for Early Stopping in Chain-of-Thought Reasoning"
      ],
      [
        "2603.12564v8",
        "Sell Me This Stock: Unsafe Recommendation Drift in LLM Agents"
      ],
      [
        "2603.12565v1",
        "Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization"
      ],
      [
        "2603.13424v1",
        "Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection"
      ],
      [
        "2603.12572v6",
        "LMEB: Long-horizon Memory Embedding Benchmark"
      ],
      [
        "2604.16335v1",
        "Beyond Verifiable Rewards: Rubric-Based GRM for Reinforced Fine-Tuning SWE Agents"
      ],
      [
        "2603.12597v1",
        "Feynman: Knowledge-Infused Diagramming Agent for Scalable Visual Designs"
      ],
      [
        "2603.13428v4",
        "SWE-Milestone: Evaluating AI Agents on Continuous Software Evolution"
      ],
      [
        "2603.12608v1",
        "InterDeepResearch: Enabling Human-Agent Collaborative Information Seeking through Interactive Deep Research"
      ],
      [
        "2603.12615v1",
        "Literary Narrative as Moral Probe : A Cross-System Framework for Evaluating AI Ethical Reasoning and Refusal Behavior"
      ],
      [
        "2603.12631v2",
        "Joint Optimization of Multi-agent Memory System"
      ],
      [
        "2603.12634v1",
        "Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents"
      ],
      [
        "2603.12666v3",
        "RetroReasoner: A Reasoning LLM for Strategic Retrosynthesis Prediction"
      ],
      [
        "2603.20262v1",
        "Deciphering Scientific Reasoning Steps from Outcome Data for Molecule Optimization"
      ],
      [
        "2603.12701v1",
        "Seeing Eye to Eye: Enabling Cognitive Alignment Through Shared First-Person Perspective in Human-AI Collaboration"
      ],
      [
        "2603.12702v2",
        "FGTR: Fine-Grained Multi-Table Retrieval via Hierarchical LLM Reasoning"
      ],
      [
        "2603.12710v1",
        "AI Planning Framework for LLM-Based Web Agents"
      ],
      [
        "2603.12717v2",
        "Altered Thoughts, Altered Actions: Reasoning Chain as Control Surface for a Vision-Language-Action Policy"
      ],
      [
        "2603.12722v1",
        "CognitionCapturerPro: Towards High-Fidelity Visual Decoding from EEG/MEG via Multi-modal Information and Asymmetric Alignment"
      ],
      [
        "2603.12726v1",
        "Anchored Alignment: Preventing Positional Collapse in Multimodal Recommender Systems"
      ],
      [
        "2603.19306v1",
        "VERDICT: Verifiable Evolving Reasoning with Directive-Informed Collegial Teams for Legal Judgment Prediction"
      ],
      [
        "2603.12736v1",
        "Conflict Mitigation in Shared Environments using Flow-Aware Multi-Agent Path Finding"
      ],
      [
        "2603.12739v1",
        "SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks"
      ],
      [
        "2603.12740v1",
        "ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning"
      ],
      [
        "2603.13434v1",
        "Modality-free Graph In-context Alignment"
      ],
      [
        "2603.12813v1",
        "Context is all you need: Towards autonomous model-based process design using agentic AI in flowsheet simulations"
      ],
      [
        "2603.12823v1",
        "Adaptive Vision-Language Model Routing for Computer Use Agents"
      ],
      [
        "2603.12824v3",
        "NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval"
      ],
      [
        "2603.15670v2",
        "I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning"
      ],
      [
        "2603.12933v1",
        "Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization"
      ],
      [
        "2603.12953v1",
        "Delta1 with LLM: symbolic and neural integration for credible and explainable reasoning"
      ],
      [
        "2603.13443v1",
        "NormCode Canvas: Making LLM Agentic Workflows Development Sustainable via Case-Based Reasoning"
      ],
      [
        "2604.04942v1",
        "TDA-RC: Task-Driven Alignment for Knowledge-Based Reasoning Chains in Large Language Models"
      ],
      [
        "2604.16337v1",
        "HR-Agents: Using Multiple LLM-based Agents to Improve Q&A about Brazilian Labor Legislation"
      ],
      [
        "2603.20265v1",
        "JCAS-MARL: Joint Communication and Sensing UAV Networks via Resource-Constrained Multi-Agent Reinforcement Learning"
      ],
      [
        "2604.13047v1",
        "Integration of Deep Reinforcement Learning and Agent-based Simulation to Explore Strategies Counteracting Information Disorder"
      ],
      [
        "2603.13017v1",
        "Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation"
      ],
      [
        "2603.13019v1",
        "ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning"
      ],
      [
        "2604.16338v1",
        "Governing the Agentic Enterprise: A Governance Maturity Model for Managing AI Agent Sprawl in Business Operations"
      ],
      [
        "2604.16339v1",
        "Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems"
      ],
      [
        "2603.15672v1",
        "DRCY: Agentic Hardware Design Reviews"
      ],
      [
        "2603.13099v3",
        "Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation"
      ],
      [
        "2603.13100v1",
        "Evaluating VLMs' Spatial Reasoning Over Robot Motion: A Step Towards Robot Planning with Motion Preferences"
      ],
      [
        "2603.13131v3",
        "MineEvolve: Self-Evolution with Accumulated Knowledge for Long-Horizon Embodied Minecraft Agents"
      ],
      [
        "2603.13173v2",
        "Semantic Invariance in Agentic AI"
      ],
      [
        "2603.13189v1",
        "LLM Constitutional Multi-Agent Governance"
      ],
      [
        "2603.15674v2",
        "Theoretical Foundations of Latent Posterior Factors: Formal Guarantees for Multi-Evidence Reasoning"
      ]
    ]
  },
  {
    "name": "multimodal",
    "query": "submittedDate:[202603121800 TO 202603131800] AND (cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND (ti:multimodal OR ti:\"world model\" OR ti:\"vision language\" OR ti:VLA OR ti:\"diffusion model\" OR ti:\"diffusion transformer\" OR ti:\"speech tokenization\")",
    "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202603121800+TO+202603131800%5D+AND+%28cat%3Acs.CV+OR+cat%3Acs.RO+OR+cat%3Acs.CL+OR+cat%3Acs.LG%29+AND+%28ti%3Amultimodal+OR+ti%3A%22world+model%22+OR+ti%3A%22vision+language%22+OR+ti%3AVLA+OR+ti%3A%22diffusion+model%22+OR+ti%3A%22diffusion+transformer%22+OR+ti%3A%22speech+tokenization%22%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
    "total": "54",
    "titles": [
      [
        "2603.12350v1",
        "TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling"
      ],
      [
        "2603.13419v2",
        "Diffusion Models Memorize in Training -- and Generalize in Inference"
      ],
      [
        "2604.16333v1",
        "A Discordance-Aware Multimodal Framework with Multi-Agent Clinical Reasoning"
      ],
      [
        "2603.12478v4",
        "Less Data, Faster Convergence: Goal-Driven Data Optimization for Multimodal Instruction Tuning"
      ],
      [
        "2603.12510v3",
        "Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies"
      ],
      [
        "2603.13423v1",
        "From Gradients to Riccati Geometry: Kalman World Models for Single-Pass Learning"
      ],
      [
        "2603.12553v1",
        "Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation"
      ],
      [
        "2603.12575v2",
        "AccelAes: Accelerating Diffusion Transformers for Training-Free Aesthetic-Enhanced Image Generation"
      ],
      [
        "2603.12581v1",
        "Multiscale Structure-Guided Latent Diffusion for Multimodal MRI Translation"
      ],
      [
        "2603.13427v1",
        "MIBench: Evaluating LMMs on Multimodal Interaction"
      ],
      [
        "2603.12625v1",
        "VLM4Rec: Multimodal Semantic Representation for Recommendation with Large Vision-Language Models"
      ],
      [
        "2603.12639v2",
        "RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization"
      ],
      [
        "2603.12655v1",
        "VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model"
      ],
      [
        "2603.12659v1",
        "AVION: Aerial Vision-Language Instruction from Offline Teacher to Prompt-Tuned Network"
      ],
      [
        "2603.12665v4",
        "TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation"
      ],
      [
        "2603.12696v2",
        "HaltNav: Reactive Visual Halting over Lightweight Topological Priors for Robust Vision-Language Navigation"
      ],
      [
        "2603.12707v1",
        "Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity"
      ],
      [
        "2603.12717v2",
        "Altered Thoughts, Altered Actions: Reasoning Chain as Control Surface for a Vision-Language-Action Policy"
      ],
      [
        "2603.12726v1",
        "Anchored Alignment: Preventing Positional Collapse in Multimodal Recommender Systems"
      ],
      [
        "2603.12730v1",
        "AnchorVLA4D: an Anchor-Based Spatial-Temporal Vision-Language-Action Model for Robotic Manipulation"
      ],
      [
        "2603.12746v1",
        "Thinking in Dynamics: How Multimodal Large Language Models Perceive, Track, and Reason Dynamics in Physical 4D World"
      ],
      [
        "2603.12760v4",
        "HIFICL: High-Fidelity In-Context Learning for Multimodal Tasks"
      ],
      [
        "2603.12762v1",
        "TerraFlow: Multimodal, Multitemporal Representation Learning for Earth Observation"
      ],
      [
        "2603.13435v1",
        "CtrlAttack: A Unified Attack on World-Model Control in Diffusion Models"
      ],
      [
        "2603.12772v1",
        "PVI: Plug-in Visual Injection for Vision-Language-Action Models"
      ],
      [
        "2603.12787v1",
        "Generalized Recognition of Basic Surgical Actions Enables Skill Assessment and Vision-Language-Model-based Surgical Planning"
      ],
      [
        "2603.12793v1",
        "Cheers: Decoupling Patch Details from Semantic Representations Enables Unified Multimodal Comprehension and Generation"
      ],
      [
        "2603.12799v2",
        "What Makes VLMs Robust? Towards Reconciling Robustness and Accuracy in Vision-Language Models"
      ],
      [
        "2603.12800v2",
        "GLEAM: A Multimodal Imaging Dataset and HAMM for Glaucoma Classification"
      ],
      [
        "2603.12823v1",
        "Adaptive Vision-Language Model Routing for Computer Use Agents"
      ],
      [
        "2603.12824v3",
        "NanoVDR: Distilling a 2B Vision-Language Retriever into a 70M Text-Only Encoder for Visual Document Retrieval"
      ],
      [
        "2603.12845v2",
        "Multimodal Protein Language Models for Enzyme Kinetic Parameters: From Substrate Recognition to Conformational Adaptation"
      ],
      [
        "2603.13437v1",
        "Vision-Language Based Expert Reporting for Painting Authentication and Defect Detection"
      ],
      [
        "2603.12848v1",
        "Team LEYA in 10th ABAW Competition: Multimodal Ambivalence/Hesitancy Recognition Approach"
      ],
      [
        "2603.12901v2",
        "A theory of learning data statistics in diffusion models, from easy to hard"
      ],
      [
        "2603.13440v1",
        "Improving Channel Estimation via Multimodal Diffusion Models with Flow Matching"
      ],
      [
        "2604.13046v1",
        "A Domain-Specific Language for LLM-Driven Trigger Generation in Multimodal Data Collection"
      ],
      [
        "2603.12939v2",
        "RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics"
      ],
      [
        "2603.12942v1",
        "ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries"
      ],
      [
        "2603.12989v1",
        "Test-Time Attention Purification for Backdoored Large Vision Language Models"
      ],
      [
        "2603.12998v1",
        "A Closed-Form Solution for Debiasing Vision-Language Models with Utility Guarantees Across Modalities and Tasks"
      ],
      [
        "2603.13024v1",
        "SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation"
      ],
      [
        "2603.13032v2",
        "Multimodal OCR: Parse Anything from Documents"
      ],
      [
        "2603.13033v1",
        "ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models"
      ],
      [
        "2603.13054v2",
        "Topo-R1: Detecting Topological Anomalies via Vision-Language Models"
      ],
      [
        "2603.13056v1",
        "Team RAS in 10th ABAW Competition: Multimodal Valence and Arousal Estimation Approach"
      ],
      [
        "2603.13070v1",
        "Mitigating Memorization in Text-to-Image Diffusion via Region-Aware Prompt Augmentation and Multimodal Copy Detection"
      ],
      [
        "2603.13098v1",
        "SldprtNet: A Large-Scale Multimodal Dataset for CAD Generation in Language-Driven 3D Design"
      ],
      [
        "2603.13099v3",
        "Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation"
      ],
      [
        "2603.13108v2",
        "Panoramic Multimodal Semantic Occupancy Prediction for Quadruped Robots"
      ],
      [
        "2603.13162v1",
        "DiT-IC: Aligned Diffusion Transformer for Efficient Image Compression"
      ],
      [
        "2603.13163v1",
        "Towards Faithful Multimodal Concept Bottleneck Models"
      ],
      [
        "2603.13176v1",
        "Perceive What Matters: Relevance-Driven Scheduling for Multimodal Streaming Perception"
      ],
      [
        "2603.13215v1",
        "Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models"
      ]
    ]
  },
  {
    "name": "system",
    "query": "submittedDate:[202603121800 TO 202603131800] AND (cat:cs.DC OR cat:cs.AR OR cat:cs.OS OR cat:cs.PL OR cat:cs.PF) AND (all:GPU OR all:inference OR all:training OR all:serving OR all:kernel OR all:compil*)",
    "url": "https://export.arxiv.org/api/query?search_query=submittedDate%3A%5B202603121800+TO+202603131800%5D+AND+%28cat%3Acs.DC+OR+cat%3Acs.AR+OR+cat%3Acs.OS+OR+cat%3Acs.PL+OR+cat%3Acs.PF%29+AND+%28all%3AGPU+OR+all%3Ainference+OR+all%3Atraining+OR+all%3Aserving+OR+all%3Akernel+OR+all%3Acompil%2A%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=ascending",
    "total": "12",
    "titles": [
      [
        "2603.12440v2",
        "KernelFoundry: Hardware-aware evolutionary GPU kernel optimization"
      ],
      [
        "2603.12465v1",
        "TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition"
      ],
      [
        "2604.18587v2",
        "Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs"
      ],
      [
        "2603.13430v1",
        "Dynamic Sparse Attention: Access Patterns and Architecture"
      ],
      [
        "2603.12707v1",
        "Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity"
      ],
      [
        "2603.12739v1",
        "SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks"
      ],
      [
        "2603.12831v2",
        "Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking"
      ],
      [
        "2603.12838v2",
        "A New Kernel Regularity Condition for Distributed Mirror Descent: Broader Coverage and Simpler Analysis"
      ],
      [
        "2603.13443v1",
        "NormCode Canvas: Making LLM Agentic Workflows Development Sustainable via Case-Based Reasoning"
      ],
      [
        "2604.09613v2",
        "Token-Budget-Aware Pool Routing for Cost-Efficient LLM Inference"
      ],
      [
        "2603.13019v1",
        "ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning"
      ],
      [
        "2603.13092v3",
        "Breaking the Tuning Barrier: Zero-Hyperparameters Yield Multi-Corner Analysis Via Learned Priors"
      ]
    ]
  }
]
```

实际去重标题线索：152。只按语义定点读可能改变主线解释/选择的完整题摘；没有全类别/全月inventory审阅认证。
