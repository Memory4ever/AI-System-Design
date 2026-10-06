# arXiv 原始主题检索

执行时间：2026-10-02T17:38:59.122719+08:00

日期字段是 submitted_date_first，仅用于发现；不证明首次公开时间。检索摘要可能为当前版，拟采用须读精确版本。

## 页面 start=0

入口：https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=%22language+model%22&terms-0-field=abstract&date-filter_by=date_range&date-from_date=2025-12-15&date-to_date=2025-12-16&date-date_type=submitted_date_first&abstracts=show&size=200&order=submitted_date&start=0

响应标题：Showing 1–107 of 107 results

### arXiv:2512.13001 Are Large Language Models Really Effective for Training-Free Cold-Start Recommendation?

https://arxiv.org/abs/2512.13001

题摘原始内容：

Recommender systems usually rely on large-scale interaction data to learn from users' past behaviors and make accurate predictions. However, real-world applications often face situations where no training data is available, such as when launching new services or handling entirely new users. In such cases, conventional approaches cannot be applied. This study focuses on training-free recommendation, where no task-specific training is performed, and particularly on \textit{training-free cold-start recommendation} (TFCSR), the more challenging case where the target user has no interactions. Large language models (LLMs) have recently been explored as a promising solution, and numerous studies have been proposed. As the ability of text embedding models (TEMs) increases, they are increasingly recognized as applicable to training-free recommendation, but no prior work has directly compared LLMs and TEMs under identical conditions. We present the first controlled experiments that systematically evaluate these two approaches in the same setting. The results show that TEMs outperform LLM rerankers, and this trend holds not only in cold-start settings but also in warm-start settings with rich interactions. These findings indicate that direct LLM ranking is not the only viable option, contrary to the commonly shared belief, and TEM-based approaches provide a stronger and more scalable basis for training-free recommendation. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13004 Large Language Models for Power System Applications: A Comprehensive Literature Survey

https://arxiv.org/abs/2512.13004

题摘原始内容：

This comprehensive literature review examines the emerging applications of Large Language Models (LLMs) in power system engineering. Through a systematic analysis of recent research published between 2020 and 2025, we explore how LLMs are being integrated into various aspects of power system operations, planning, and management. The review covers key application areas including fault diagnosis, load forecasting, cybersecurity, control and optimization, system planning, simulation, and knowledge management. Our findings indicate that while LLMs show promising potential in enhancing power system operations through their advanced natural language processing and reasoning capabilities, significant challenges remain in their practical implementation. These challenges include limited domain-specific training data, concerns about reliability and safety in critical infrastructure, and the need for enhanced explainability. The review also highlights emerging trends such as the development of power system-specific LLMs and hybrid approaches combining LLMs with traditional power engineering methods. We identify crucial research directions for advancing the field, including the development of specialized architectures, improved security frameworks, and enhanced integration with existing power system tools. This survey provides power system researchers and practitioners with a comprehensive overview of the current state of LLM applications in the field and outlines future pathways for research and development. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 17 pages, 1 table, 1 figure

### arXiv:2512.13008 TWLR: Text-Guided Weakly-Supervised Lesion Localization and Severity Regression for Explainable Diabetic Retinopathy Grading

https://arxiv.org/abs/2512.13008

题摘原始内容：

Accurate medical image analysis can greatly assist clinical diagnosis, but its effectiveness relies on high-quality expert annotations Obtaining pixel-level labels for medical images, particularly fundus images, remains costly and time-consuming. Meanwhile, despite the success of deep learning in medical imaging, the lack of interpretability limits its clinical adoption. To address these challenges, we propose TWLR, a two-stage framework for interpretable diabetic retinopathy (DR) assessment. In the first stage, a vision- language model integrates domain-specific ophthalmological knowledge into text embeddings to jointly perform DR grading and lesion classification, effectively linking semantic medical concepts with visual features. The second stage introduces an iterative severity regression framework based on weakly-supervised semantic segmentation. Lesion saliency maps generated through iterative refinement direct a progressive inpainting mechanism that systematically eliminates pathological features, effectively downgrading disease severity toward healthier fundus appearances. Critically, this severity regression approach achieves dual benefits: accurate lesion localization without pixel-level supervision and providing an interpretable visualization of disease-to-healthy transformations. Experimental results on the FGADR, DDR, and a private dataset demonstrate that TWLR achieves competitive performance in both DR classification and lesion segmentation, offering a more explainable and annotation-efficient solution for automated retinal image analysis. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13752 STAR: STacked AutoRegressive Scheme for Unified Multimodal Learning

https://arxiv.org/abs/2512.13752

题摘原始内容：

Multimodal large language models (MLLMs) play a pivotal role in advancing the quest for general artificial intelligence. However, achieving unified target for multimodal understanding and generation remains challenging due to optimization conflicts and performance trade-offs. To effectively enhance generative performance while preserving existing comprehension capabilities, we introduce STAR: a STacked AutoRegressive scheme for task-progressive unified multimodal learning. This approach decomposes multimodal learning into multiple stages: understanding, generation, and editing. By freezing the parameters of the fundamental autoregressive (AR) model and progressively stacking isomorphic AR modules, it avoids cross-task interference while expanding the model's capabilities. Concurrently, we introduce a high-capacity VQ to enhance the granularity of image representations and employ an implicit reasoning mechanism to improve generation quality under complex conditions. Experiments demonstrate that STAR achieves state-of-the-art performance on GenEval (0.91), DPG-Bench (87.44), and ImgEdit (4.34), validating its efficacy for unified multimodal learning. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 18 pages, 7 figures

### arXiv:2512.22147 GPU Kernel Optimization Beyond Full Builds: An LLM Framework with Minimal Executable Programs

https://arxiv.org/abs/2512.22147

题摘原始内容：

In high-performance computing, hotspot GPU kernels are primary bottlenecks, and expert manual tuning is costly and hard to port. Large language model methods often assume kernels can be compiled and executed cheaply, which fails in large applications where full builds and runs are expensive. We present an end-to-end LLM framework with performance feedback that optimizes kernels without building the full application. From independently extracted hotspot kernels, it automatically completes code into a Minimal Executable Program (MEP), then performs multi-round iterative optimization and evaluation outside the full application. The framework integrates Automatic Error Repair and Performance Pattern Inheritance to fix faults, preserve correctness, reuse effective tiling/memory/synchronization strategies, and reduce search cost. Optimized variants are reintegrated into the original application for validation. We evaluate on NVIDIA GPUs and the Haiguang Deep Computing Unit (DCU) platform (AMD-licensed architecture) using PolyBench, the AMD APP SDK, and hotspot kernels from large-scale supercomputing applications. The method achieves average speedups of 5.05x (PolyBench on NVIDIA), 7.77x (PolyBench on DCU), 1.77x (AMD APP SDK), and 1.25x on three hotspot kernels, surpassing direct LLM optimization. The approach requires no full-source dependencies, offers cross-platform portability, and enables practical, low-cost GPU kernel optimization. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13059 An Open and Reproducible Deep Research Agent for Long-Form Question Answering

https://arxiv.org/abs/2512.13059

题摘原始内容：

We present an open deep research system for long-form question answering, selected as a winning system in the text-to-text track of the MMU-RAG competition at NeurIPS 2025. The system combines an open-source large language model (LLM) with an open web search API to perform iterative retrieval, reasoning, and synthesis in real-world open-domain settings. To enhance reasoning quality, we apply preference tuning based on LLM-as-a-judge feedback that evaluates multiple aspects, including clarity, insightfulness, and factuality. Our experimental results show that the proposed method consistently improves answer quality across all three aspects. Our source code is publicly available at https://github.com/efficient-deep-research/efficient-deep-research. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Technical report of a winning system in the NeurIPS MMU-RAG competition

### arXiv:2512.13063 LLM Rationalis? Measuring Bargaining Capabilities of AI Negotiators

https://arxiv.org/abs/2512.13063

题摘原始内容：

Bilateral negotiation is a complex, context-sensitive task in which human negotiators dynamically adjust anchors, pacing, and flexibility to exploit power asymmetries and informal cues. We introduce a unified mathematical framework for modeling concession dynamics based on a hyperbolic tangent curve, and propose two metrics burstiness tau and the Concession-Rigidity Index (CRI) to quantify the timing and rigidity of offer trajectories. We conduct a large-scale empirical comparison between human negotiators and four state-of-the-art large language models (LLMs) across natural-language and numeric-offers settings, with and without rich market context, as well as six controlled power-asymmetry scenarios. Our results reveal that, unlike humans who smoothly adapt to situations and infer the opponents position and strategies, LLMs systematically anchor at extremes of the possible agreement zone for negotiations and optimize for fixed points irrespective of leverage or context. Qualitative analysis further shows limited strategy diversity and occasional deceptive tactics used by LLMs. Moreover the ability of LLMs to negotiate does not improve with better models. These findings highlight fundamental limitations in current LLM negotiation capabilities and point to the need for models that better internalize opponent reasoning and context-dependent strategy. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Published in the First Workshop on Multi-Turn Interactions in Large Language Models at Neurips 2025

### arXiv:2512.13070 M-GRPO: Stabilizing Self-Supervised Reinforcement Learning for Large Language Models with Momentum-Anchored Policy Optimization

https://arxiv.org/abs/2512.13070

题摘原始内容：

Self-supervised reinforcement learning (RL) presents a promising approach for enhancing the reasoning capabilities of Large Language Models (LLMs) without reliance on expensive human-annotated data. However, we find that existing methods suffer from a critical failure mode under long-horizon training: a "policy collapse" where performance precipitously degrades. We diagnose this instability and demonstrate that simply scaling the number of rollouts -- a common strategy to improve performance -- only delays, but does not prevent, this collapse. To counteract this instability, we first introduce M-GRPO (Momentum-Anchored Group Relative Policy Optimization), a framework that leverages a slowly evolving momentum model to provide a stable training target. In addition, we identify that this process is often accompanied by a rapid collapse in policy entropy, resulting in a prematurely confident and suboptimal policy. To specifically address this issue, we propose a second contribution: an adaptive filtering method based on the interquartile range (IQR) that dynamically prunes low-entropy trajectories, preserving essential policy diversity. Our extensive experiments on multiple reasoning benchmarks demonstrate that M-GRPO stabilizes the training process while the IQR filter prevents premature convergence. The combination of these two innovations leads to superior training stability and state-of-the-art performance. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 7 pages, 5 figures,Accepted NeurIPS 2025 Workshop on Efficient Reasoning

### arXiv:2512.13072 Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models

https://arxiv.org/abs/2512.13072

题摘原始内容：

Multimodal biomedical Vision- Language Models (VLMs) exhibit immense potential in the field of Continual Learning (CL). However, they confront a core dilemma: how to preserve fine-grained intra-modality features while bridging the significant domain gap across different modalities. To address this challenge, we propose a comprehensive framework. Leveraging our 18-million multimodal and comprehensive medical retrieval database derived from PubMed scientific papers, we pioneer the integration of Retrieval-Augmented Generation (RAG) into CL. Specifically, we employ a multi-modal, multi-layer RAG system that provides real-time guidance for model fine-tuning through dynamic, on-demand knowledge retrieval. Building upon this, we introduce a dynamic knowledge distillation framework. This framework precisely resolves the aforementioned core dilemma by dynamically modulating the importance of the parameter space, the granularity of the distilled knowledge, and the data distribution of the reference dataset in accordance with the required level of detail. To thoroughly validate the clinical value of our strategy, we have designed a more rigorous \textbf{M}edical Generalist Task Incremental Learning (MGTIL) benchmark. This benchmark is engineered to simultaneously evaluate the model's capacity for adaptation to significant domain shifts, retention of subtle intra-domain features, and real-time learning of novel and complex medical tasks. Extensive experimental results demonstrate that our proposed method achieves state-of-the-art (SOTA) performance across all metrics. The code is provided in the supplementary materials. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13074 A Simple and Effective Framework for Symmetric Consistent Indexing in Large-Scale Dense Retrieval

https://arxiv.org/abs/2512.13074

题摘原始内容：

Dense retrieval has become the industry standard in large-scale information retrieval systems due to its high efficiency and competitive accuracy. Its core relies on a coarse-to-fine hierarchical architecture that enables rapid candidate selection and precise semantic matching, achieving millisecond-level response over billion-scale corpora. This capability makes it essential not only in traditional search and recommendation scenarios but also in the emerging paradigm of generative recommendation driven by large language models , where semantic IDs-themselves a form of coarse-to-fine representation-play a foundational role. However, the widely adopted dual-tower encoding architecture introduces inherent challenges, primarily representational space misalignment and retrieval index inconsistency, which degrade matching accuracy, retrieval stability, and performance on long-tail queries. These issues are further magnified in semantic ID generation, ultimately limiting the performance ceiling of downstream generative models. To address these challenges, this paper proposes a simple and effective framework named SCI comprising two synergistic modules: a symmetric representation alignment module that employs an innovative input-swapping mechanism to unify the dual-tower representation space without adding parameters, and an consistent indexing with dual-tower synergy module that redesigns retrieval paths using a dual-view indexing strategy to maintain consistency from training to inference. The framework is systematic, lightweight, and engineering-friendly, requiring minimal overhead while fully supporting billion-scale deployment. We provide theoretical guarantees for our approach, with its effectiveness validated by results across public datasets and real-world e-commerce datasets. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13080 Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos

https://arxiv.org/abs/2512.13080

题摘原始内容：

Vision-Language-Action (VLA) models provide a promising paradigm for robot learning by integrating visual perception with language-guided policy learning. However, most existing approaches rely on 2D visual inputs to perform actions in 3D physical environments, creating a significant gap between perception and action grounding. To bridge this gap, we propose a Spatial-Aware VLA Pretraining paradigm that performs explicit alignment between visual space and physical space during pretraining, enabling models to acquire 3D spatial understanding before robot policy learning. Starting from pretrained vision- language models , we leverage large-scale human demonstration videos to extract 3D visual and 3D action annotations, forming a new source of supervision that aligns 2D visual observations with 3D spatial reasoning. We instantiate this paradigm with VIPA-VLA, a dual-encoder architecture that incorporates a 3D visual encoder to augment semantic visual representations with 3D-aware features. When adapted to downstream robot tasks, VIPA-VLA achieves significantly improved grounding between 2D vision and 3D action, resulting in more robust and generalizable robotic policies. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13109 Uncovering the Role of Initial Saliency in U-Shaped Attention Bias: Scaling Initial Token Weight for Enhanced Long-Text Processing

https://arxiv.org/abs/2512.13109

题摘原始内容：

Large language models (LLMs) have demonstrated strong performance on a variety of natural language processing (NLP) tasks. However, they often struggle with long-text sequences due to the ``lost in the middle'' phenomenon. This issue has been shown to arise from a U-shaped attention bias, where attention is disproportionately focused on the beginning and end of a text, leaving the middle section underrepresented. While previous studies have attributed this bias to position encoding, our research first identifies an additional factor: initial saliency. It means that in the attention computation for each token, tokens with higher attention weights relative to the initial token tend to receive more attention in the prediction of the next token. We further find that utilizing this property by scaling attention weight between the initial token and others improves the model's ability to process long contexts, achieving a maximum improvement of 3.6\% in MDQA dataset. Moreover, combining this approach with existing methods to reduce position encoding bias further enhances performance, achieving a maximum improvement of 3.4\% in KV-Retrieval tasks. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13159 SpeakRL: Synergizing Reasoning, Speaking, and Acting in Language Models with Reinforcement Learning

https://arxiv.org/abs/2512.13159

题摘原始内容：

Effective human-agent collaboration is increasingly prevalent in real-world applications. Current trends in such collaborations are predominantly unidirectional, with users providing instructions or posing questions to agents, where agents respond directly without seeking necessary clarifications or confirmations. However, the evolving capabilities of these agents require more proactive engagement, where agents should dynamically participate in conversations to clarify user intents, resolve ambiguities, and adapt to changing circumstances. Existing prior work under-utilize the conversational capabilities of language models (LMs), thereby optimizing agents as better followers rather than effective speakers. In this work, we introduce SpeakRL, a reinforcement learning (RL) method that enhances agents' conversational capabilities by rewarding proactive interactions with users, such as asking right clarification questions when necessary. To support this, we curate SpeakER, a synthetic dataset that includes diverse scenarios from task-oriented dialogues, where tasks are resolved through interactive clarification questions. We present a systematic analysis of reward design for conversational proactivity and propose a principled reward formulation for teaching agents to balance asking with acting. Empirical evaluations demonstrate that our approach achieves a 20.14% absolute improvement in task completion over base models without increasing conversation turns even surpassing even much larger proprietary models, demonstrating the promise of clarification-centric user-agent interactions. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13169 Integrated Semantic and Temporal Alignment for Interactive Video Retrieval

https://arxiv.org/abs/2512.13169

题摘原始内容：

The growing volume of video data and the introduction of complex retrieval challenges, such as the Temporal Retrieval and Alignment of Key Events (TRAKE) task at the Ho Chi Minh City AI Challenge 2025, expose critical limitations in existing systems. Many methodologies lack scalable, holistic architectures and rely on "frozen" embedding models that fail on out-of-knowledge (OOK) or real-world queries. This paper introduces the comprehensive video retrieval framework developed by team AIO\_Owlgorithms to address these gaps. Our system features an architecture integrating TransNetV2 for scene segmentation, BEiT-3 for visual embeddings in Milvus, and Gemini OCR for metadata in Elasticsearch. We propose two components: (1) \textbf{QUEST} (Query Understanding and External Search for Out-of-Knowledge Tasks), a two-branch framework that leverages a Large Language Model (LLM) for query rewriting and an external image search pathway to resolve OOK queries; and (2) \textbf{DANTE} (Dynamic Alignment of Narrative Temporal Events), a dynamic programming algorithm that efficiently solves the temporally-incoherent TRAKE task. These contributions form a robust and intelligent system that significantly advances the state-of-the-art in handling complex, real-world video search queries. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13186 PolySet: Restoring the Statistical Ensemble Nature of Polymers for Machine Learning

https://arxiv.org/abs/2512.13186

题摘原始内容：

Machine-learning (ML) models in polymer science typically treat a polymer as a single, perfectly defined molecular graph, even though real materials consist of stochastic ensembles of chains with distributed lengths. This mismatch between physical reality and digital representation limits the ability of current models to capture polymer behaviour. Here we introduce PolySet, a framework that represents a polymer as a finite, weighted ensemble of chains sampled from an assumed molar-mass distribution. This ensemble-based encoding is independent of chemical detail, compatible with any molecular representation and illustrated here in the homopolymer case using a minimal language model . We show that PolySet retains higher-order distributional moments (such as Mz, Mz+1), enabling ML models to learn tail-sensitive properties with greatly improved stability and accuracy. By explicitly acknowledging the statistical nature of polymer matter, PolySet establishes a physically grounded foundation for future polymer machine learning, naturally extensible to copolymers, block architectures, and other complex topologies. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13238 Ego-EXTRA: video-language Egocentric Dataset for EXpert-TRAinee assistance

https://arxiv.org/abs/2512.13238

题摘原始内容：

We present Ego-EXTRA, a video-language Egocentric Dataset for EXpert-TRAinee assistance. Ego-EXTRA features 50 hours of unscripted egocentric videos of subjects performing procedural activities (the trainees) while guided by real-world experts who provide guidance and answer specific questions using natural language. Following a ``Wizard of OZ'' data collection paradigm, the expert enacts a wearable intelligent assistant, looking at the activities performed by the trainee exclusively from their egocentric point of view, answering questions when asked by the trainee, or proactively interacting with suggestions during the procedures. This unique data collection protocol enables Ego-EXTRA to capture a high-quality dialogue in which expert-level feedback is provided to the trainee. Two-way dialogues between experts and trainees are recorded, transcribed, and used to create a novel benchmark comprising more than 15k high-quality Visual Question Answer sets, which we use to evaluate Multimodal Large Language Models . The results show that Ego-EXTRA is challenging and highlight the limitations of current models when used to provide expert-level assistance to the user. The Ego-EXTRA dataset is publicly available to support the benchmark of egocentric video-language assistants: https://fpv-iplab.github.io/Ego-EXTRA/. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13240 Reflective Preference Optimization (RPO): Enhancing On-Policy Alignment via Hint-Guided Reflection

https://arxiv.org/abs/2512.13240

题摘原始内容：

Direct Preference Optimization (DPO) has emerged as a lightweight and effective alternative to Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning with AI Feedback (RLAIF) for aligning large language and vision- language models . However, the standard DPO formulation, in which both the chosen and rejected responses are generated by the same policy, suffers from a weak learning signal because the two responses often share similar errors and exhibit small Kullback-Leibler (KL) divergence. This leads to slow and unstable convergence. To address this limitation, we introduce Reflective Preference Optimization (RPO), a new framework that incorporates hint-guided reflection into the DPO paradigm. RPO uses external models to identify hallucination sources and generate concise reflective hints, enabling the construction of on-policy preference pairs with stronger contrastiveness and clearer preference signals. We theoretically show that conditioning on hints increases the expected preference margin through mutual information and improves sample efficiency while remaining within the policy distribution family. Empirically, RPO achieves superior alignment with fewer training samples and iterations, substantially reducing hallucination rates and delivering state-of-the-art performance across multimodal benchmarks. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13250 Toward Ambulatory Vision: Learning Visually-Grounded Active View Selection

https://arxiv.org/abs/2512.13250

题摘原始内容：

Vision Language Models (VLMs) excel at visual question answering (VQA) but remain limited to snapshot vision, reasoning from static images. In contrast, embodied agents require ambulatory vision, actively moving to obtain more informative views. We introduce Visually Grounded Active View Selection (VG-AVS), a task that selects the most informative next viewpoint using only the visual information in the current image, without relying on scene memory or external knowledge. To support this task, we construct a synthetic dataset with automatically generated paired query-target views and question-answer prompts. We also propose a framework that fine-tunes pretrained VLMs through supervised fine-tuning (SFT) followed by RL-based policy optimization. Our approach achieves strong question answering performance based on viewpoint selection and generalizes robustly to unseen synthetic and real scenes. Furthermore, incorporating our learned VG-AVS framework into existing scene-exploration-based EQA systems improves downstream question-answering accuracy. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Project page: https://active-view-selection.github.io/

### arXiv:2512.13276 CogniEdit: Dense Gradient Flow Optimization for Fine-Grained Image Editing

https://arxiv.org/abs/2512.13276

题摘原始内容：

Instruction-based image editing with diffusion models has achieved impressive results, yet existing methods struggle with fine-grained instructions specifying precise attributes such as colors, positions, and quantities. While recent approaches employ Group Relative Policy Optimization (GRPO) for alignment, they optimize only at individual sampling steps, providing sparse feedback that limits trajectory-level control. We propose a unified framework CogniEdit, combining multi-modal reasoning with dense reward optimization that propagates gradients across consecutive denoising steps, enabling trajectory-level gradient flow through the sampling process. Our method comprises three components: (1) Multi-modal Large Language Models for decomposing complex instructions into actionable directives, (2) Dynamic Token Focus Relocation that adaptively emphasizes fine-grained attributes, and (3) Dense GRPO-based optimization that propagates gradients across consecutive steps for trajectory-level supervision. Extensive experiments on benchmark datasets demonstrate that our CogniEdit achieves state-of-the-art performance in balancing fine-grained instruction following with visual quality and editability preservation △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.15784 Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM

https://arxiv.org/abs/2512.15784

题摘原始内容：

Large Language Model (LLM) agents are increasingly deployed to automate complex workflows in mobile and desktop environments. However, current model-centric agent architectures struggle to self-evolve post-deployment: improving personalization, capability, and efficiency typically requires continuous model retraining/fine-tuning, which incurs prohibitive computational overheads and suffers from an inherent trade-off between model accuracy and inference efficiency. To enable iterative self-evolution without model retraining, we propose MOBIMEM, a memory-centric agent system. MOBIMEM first introduces three specialized memory primitives to decouple agent evolution from model weights: (1) Profile Memory uses a lightweight distance-graph (DisGraph) structure to align with user preferences, resolving the accuracy-latency trade-off in user profile retrieval; (2) Experience Memory employs multi-level templates to instantiate execution logic for new tasks, ensuring capability generalization; and (3) Action Memory records fine-grained interaction sequences, reducing the reliance on expensive model inference. Building upon this memory architecture, MOBIMEM further integrates a suite of OS-inspired services to orchestrate execution: a scheduler that coordinates parallel sub-task execution and memory operations; an agent record-and-replay (AgentRR) mechanism that enables safe and efficient action reuse; and a context-aware exception handling that ensures graceful recovery from user interruptions and runtime errors. Evaluation on AndroidWorld and top-50 apps shows that MOBIMEM achieves 83.1% profile alignment with 23.83 ms retrieval time (280x faster than GraphRAG baselines), improves task success rates by up to 50.3%, and reduces end-to-end latency by up to 9x on mobile devices. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13298 MiniLingua: A Small Open-Source LLM for European Languages

https://arxiv.org/abs/2512.13298

题摘原始内容：

Large language models are powerful but often limited by high computational cost, privacy concerns, and English-centric training. Recent progress demonstrates that small, efficient models with around one billion parameters can deliver strong results and enable on-device use. This paper introduces MiniLingua, a multilingual open-source LLM of one billion parameters trained from scratch for 13 European languages, designed to balance coverage and instruction-following capabilities. Based on evaluation results, the instruction-tuned version of MiniLingua outperforms EuroLLM, a model with a similar training approach but a larger training budget, on summarization, classification and both open- and closed-book question answering. Moreover, it remains competitive with more advanced state-of-the-art models on open-ended generation tasks. We release model weights, tokenizer and source code used for data processing and model training. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 9+6 pages, 6 figures and 3 tables in the main text. Code at https://github.com/MiniLingua-ai/training_artifacts

### arXiv:2512.13313 KlingAvatar 2.0 Technical Report

https://arxiv.org/abs/2512.13313

题摘原始内容：

Avatar video generation models have achieved remarkable progress in recent years. However, prior work exhibits limited efficiency in generating long-duration high-resolution videos, suffering from temporal drifting, quality degradation, and weak prompt following as video length increases. To address these challenges, we propose KlingAvatar 2.0, a spatio-temporal cascade framework that performs upscaling in both spatial resolution and temporal dimension. The framework first generates low-resolution blueprint video keyframes that capture global semantics and motion, and then refines them into high-resolution, temporally coherent sub-clips using a first-last frame strategy, while retaining smooth temporal transitions in long-form videos. To enhance cross-modal instruction fusion and alignment in extended videos, we introduce a Co-Reasoning Director composed of three modality-specific large language model (LLM) experts. These experts reason about modality priorities and infer underlying user intent, converting inputs into detailed storylines through multi-turn dialogue. A Negative Director further refines negative prompts to improve instruction alignment. Building on these components, we extend the framework to support ID-specific multi-character control. Extensive experiments demonstrate that our model effectively addresses the challenges of efficient, multimodally aligned long-form high-resolution video generation, delivering enhanced visual clarity, realistic lip-teeth rendering with accurate lip synchronization, strong identity preservation, and coherent multimodal instruction following. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 14 pages, 7 figures

### arXiv:2512.13323 Error-Driven Prompt Optimization for Arithmetic Reasoning

https://arxiv.org/abs/2512.13323

题摘原始内容：

Recent advancements in artificial intelligence have sparked interest in industrial agents capable of supporting analysts in regulated sectors, such as finance and healthcare, within tabular data workflows. A key capability for such systems is performing accurate arithmetic operations on structured data while ensuring sensitive information never leaves secure, on-premises environments. Here, we introduce an error-driven optimization framework for arithmetic reasoning that enhances a Code Generation Agent (CGA), specifically applied to on-premises small language models (SLMs). Through a systematic evaluation of a leading SLM (Qwen3 4B), we find that while the base model exhibits fundamental limitations in arithmetic tasks, our proposed error-driven method, which clusters erroneous predictions to refine prompt-rules iteratively, dramatically improves performance, elevating the model's accuracy to 70.8\%. Our results suggest that developing reliable, interpretable, and industrially deployable AI assistants can be achieved not only through costly fine-tuning but also via systematic, error-driven prompt optimization, enabling small models to surpass larger language models (GPT-3.5 Turbo) in a privacy-compliant manner. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Journal ref: IEEE Access, vol. 14, pp. 62570-62583, 2026

### arXiv:2512.13330 FIN-bench-v2: A Unified and Robust Benchmark Suite for Evaluating Finnish Large Language Models

https://arxiv.org/abs/2512.13330

题摘原始内容：

We introduce FIN-bench-v2, a unified benchmark suite for evaluating large language models in Finnish. FIN-bench-v2 consolidates Finnish versions of widely used benchmarks together with an updated and expanded version of the original FIN-bench into a single, consistently formatted collection, covering multiple-choice and generative tasks across reading comprehension, commonsense reasoning, sentiment analysis, world knowledge, and alignment. All datasets are converted to HuggingFace Datasets, which include both cloze and multiple-choice prompt formulations with five variants per task, and we incorporate human annotation or review for machine-translated resources such as GoldenSwag and XED. To select robust tasks, we pretrain a set of 2.15B-parameter decoder-only models and use their learning curves to compute monotonicity, signal-to-noise, non-random performance, and model ordering consistency, retaining only tasks that satisfy all criteria. We further evaluate a set of larger instruction-tuned models to characterize performance across tasks and prompt formulations. All datasets, prompts, and evaluation configurations are publicly available via our fork of the Language Model Evaluation Harness at https://github.com/LumiOpen/lm-evaluation-harness. Supplementary resources are released in a separate repository at https://github.com/TurkuNLP/FIN-bench-v2. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | ACM Class: I.2.7

### arXiv:2512.13337 FROC: A Unified Framework with Risk-Optimized Control for Machine Unlearning in LLMs

https://arxiv.org/abs/2512.13337

题摘原始内容：

Machine unlearning (MU) seeks to eliminate the influence of specific training examples from deployed models. As large language models (LLMs) become widely used, managing risks arising from insufficient forgetting or utility loss is increasingly crucial. Current MU techniques lack effective mechanisms for evaluating and controlling these risks, hindering the selection of strategies that appropriately balance safety and utility, and raising trust concerns surrounding the "right to be forgotten." To address these issues, we propose FROC, a unified framework with Risk-Optimized Control for machine unlearning in LLMs. FROC is built around a conformal-style risk-control formulation that expresses a user-specified risk budget on unlearning behavior. This probability-based constraint enables FROC to compare MU strategies, identify feasible operating regions, and guide hyperparameter selection according to desired trade-offs between forgetting sufficiency and utility preservation. To operationalize this constraint, FROC introduces a smoothly varying continuous risk model that aggregates forgetting deficiency and utility degradation into a single configuration-level score. Building on conformal risk analysis, FROC computes (1) the Conformal Unlearning Risk (CUR), a data-driven estimated value on the probability that forgotten samples continue to influence model predictions, and (2) risk-controlled configuration sets, which identify unlearning hyperparameters that are valid under the specified risk budget. Experiments across multiple LLM MU methods demonstrate that FROC produces stable, interpretable risk landscapes and reveals consistent relationships between unlearning configurations, semantic shift, and utility impact. FROC reframes MU as a controllable, risk-aware process and offers a practical foundation for managing unlearning behavior in large-scale LLM deployments. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13762 State-Dependent Refusal and Learned Incapacity in RLHF-Aligned Language Models

https://arxiv.org/abs/2512.13762

题摘原始内容：

Large language models (LLMs) are widely deployed as general-purpose tools, yet extended interaction can reveal behavioral patterns not captured by standard quantitative benchmarks. We present a qualitative case-study methodology for auditing policy-linked behavioral selectivity in long-horizon interaction. In a single 86-turn dialogue session, the same model shows Normal Performance (NP) in broad, non-sensitive domains while repeatedly producing Functional Refusal (FR) in provider- or policy-sensitive domains, yielding a consistent asymmetry between NP and FR across domains. Drawing on learned helplessness as an analogy, we introduce learned incapacity (LI) as a behavioral descriptor for this selective withholding without implying intentionality or internal mechanisms. We operationalize three response regimes (NP, FR, Meta-Narrative; MN) and show that MN role-framing narratives tend to co-occur with refusals in the same sensitive contexts. Overall, the study proposes an interaction-level auditing framework based on observable behavior and motivates LI as a lens for examining potential alignment side effects, warranting further investigation across users and models. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 23 pages, 6 figures. Qualitative interaction-level analysis of response patterns in a large language model. Code and processed interaction data are available at https://github.com/theMaker-EnvData/llm_learned_incapacity_corpus

### arXiv:2512.13360 UCRBench: Benchmarking LLMs on Use Case Recovery

https://arxiv.org/abs/2512.13360

题摘原始内容：

Use cases are widely employed to specify functional requirements, yet existing benchmarks are scarce and face the risk of being misaligned with actual system behavior, similarly limiting the rigorous evaluation of large language models (LLMs) in generating use cases from source code. We address this gap by introducing code-aligned use case benchmarks, constructed through manual validation of both user-goal and subfunction use cases across nine real-world software projects. Using this benchmark, we conduct the first systematic study of LLMs and propose a hierarchical evaluation protocol that assesses actor correctness, name accuracy, path fidelity, and behavioral coverage. The results show that while LLMs can partially reconstruct system functionality, their performance varies significantly across projects, with particularly noticeable shortcomings in domain-specific and multi-module systems. The models also exhibit high omission rates and struggle to maintain consistent abstraction when aggregating subfunctions into user-goal use cases, highlighting both the potential and current limitations of LLM-based use case reverse engineering. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14757 SocialNav-MoE: A Mixture-of-Experts Vision Language Model for Socially Compliant Navigation with Reinforcement Fine-Tuning

https://arxiv.org/abs/2512.14757

题摘原始内容：

For robots navigating in human-populated environments, safety and social compliance are equally critical, yet prior work has mostly emphasized safety. Socially compliant navigation that accounts for human comfort, social norms, and contextual appropriateness remains underexplored. Vision language models (VLMs) show promise for this task; however, large-scale models incur substantial computational overhead, leading to higher inference latency and energy consumption, which makes them unsuitable for real-time deployment on resource-constrained robotic platforms. To address this issue, we investigate the effectiveness of small VLM and propose SocialNav-MoE, an efficient Mixture-of-Experts vision language model for socially compliant navigation with reinforcement fine-tuning (RFT). We further introduce a semantic similarity reward (SSR) to effectively leverage RFT for enhancing the decision-making capabilities. Additionally, we study the effectiveness of different small language model types (Phi, Qwen, and StableLM), routing strategies, and vision encoders (CLIP vs. SigLIP, frozen vs. fine-tuned). Experiments on the SNEI dataset demonstrate that SocialNav-MoE achieves an excellent balance between navigation accuracy and efficiency. The proposed SSR function is more effective than hard-level and character-level rewards. Source code will be released upon acceptance. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13380 Universal Dexterous Functional Grasping via Demonstration-Editing Reinforcement Learning

https://arxiv.org/abs/2512.13380

题摘原始内容：

Reinforcement learning (RL) has achieved great success in dexterous grasping, significantly improving grasp performance and generalization from simulation to the real world. However, fine-grained functional grasping, which is essential for downstream manipulation tasks, remains underexplored and faces several challenges: the complexity of specifying goals and reward functions for functional grasps across diverse objects, the difficulty of multi-task RL exploration, and the challenge of sim-to-real transfer. In this work, we propose DemoFunGrasp for universal dexterous functional grasping. We factorize functional grasping conditions into two complementary components - grasping style and affordance - and integrate them into an RL framework that can learn to grasp any object with any functional grasping condition. To address the multi-task optimization challenge, we leverage a single grasping demonstration and reformulate the RL problem as one-step demonstration editing, substantially enhancing sample efficiency and performance. Experimental results in both simulation and the real world show that DemoFunGrasp generalizes to unseen combinations of objects, affordances, and grasping styles, outperforming baselines in both success rate and functional grasping accuracy. In addition to strong sim-to-real capability, by incorporating a vision- language model (VLM) for planning, our system achieves autonomous instruction-following grasp execution. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 19 pages

### arXiv:2512.13438 From User Interface to Agent Interface: Efficiency Optimization of UI Representations for LLM Agents

https://arxiv.org/abs/2512.13438

题摘原始内容：

While Large Language Model (LLM) agents show great potential for automated UI navigation such as automated UI testing and AI assistants, their efficiency has been largely overlooked. Our motivating study reveals that inefficient UI representation creates a critical performance bottleneck. However, UI representation optimization, formulated as the task of automatically generating programs that transform UI representations, faces two unique challenges. First, the lack of Boolean oracles, which traditional program synthesis uses to decisively validate semantic correctness, poses a fundamental challenge to co-optimization of token efficiency and completeness. Second, the need to process large, complex UI trees as input while generating long, compositional transformation programs, making the search space vast and error-prone. Toward addressing the preceding limitations, we present UIFormer, the first automated optimization framework that synthesizes UI transformation programs by conducting constraint-based optimization with structured decomposition of the complex synthesis task. First, UIFormer restricts the program space using a domain-specific language (DSL) that captures UI-specific operations. Second, UIFormer conducts LLM-based iterative refinement with correctness and efficiency rewards, providing guidance for achieving the efficiency-completeness co-optimization. UIFormer operates as a lightweight plugin that applies transformation programs for seamless integration with existing LLM agents, requiring minimal modifications to their core logic. Evaluations across three UI navigation benchmarks spanning Android and Web platforms with five LLMs demonstrate that UIFormer achieves 48.7% to 55.8% token reduction with minimal runtime overhead while maintaining or improving agent performance. Real-world industry deployment at WeChat further validates the practical impact of UIFormer. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13441 Large language models are not about natural language

https://arxiv.org/abs/2512.13441

题摘原始内容：

Large Language Models are useless for linguistics, as they are probabilistic models that require a vast amount of data to analyse externalized strings of words. In contrast, human language is underpinned by a mind-internal computational system that recursively generates hierarchical thought structures. The language system grows with minimal external input and can readily distinguish between real language and impossible languages. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13472 Scaling Laws for Code: Every Programming Language Matters

https://arxiv.org/abs/2512.13472

题摘原始内容：

Code large language models (Code LLMs) are powerful but costly to train, with scaling laws predicting performance from model size, data, and compute. However, different programming languages (PLs) have varying impacts during pre-training that significantly affect base model performance, leading to inaccurate performance prediction. Besides, existing works focus on language-agnostic settings, neglecting the inherently multilingual nature of modern software development. Therefore, it is first necessary to investigate the scaling laws of different PLs, and then consider their mutual influences to arrive at the final multilingual scaling law. In this paper, we present the first systematic exploration of scaling laws for multilingual code pre-training, conducting over 1000+ experiments (Equivalent to 336,000+ H800 hours) across multiple PLs, model sizes (0.2B to 14B parameters), and dataset sizes (1T tokens). We establish comprehensive scaling laws for code LLMs across multiple PLs, revealing that interpreted languages (e.g., Python) benefit more from increased model size and data than compiled languages (e.g., Rust). The study demonstrates that multilingual pre-training provides synergistic benefits, particularly between syntactically similar PLs. Further, the pre-training strategy of the parallel pairing (concatenating code snippets with their translations) significantly enhances cross-lingual abilities with favorable scaling properties. Finally, a proportion-dependent multilingual scaling law is proposed to optimally allocate training tokens by prioritizing high-utility PLs (e.g., Python), balancing high-synergy pairs (e.g., JavaScript-TypeScript), and reducing allocation to fast-saturating languages (Rust), achieving superior average performance across all PLs compared to uniform distribution under the same compute budget. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13494 SkipCat: Rank-Maximized Low-Rank Compression of Large Language Models via Shared Projection and Block Skipping

https://arxiv.org/abs/2512.13494

题摘原始内容：

Large language models (LLM) have achieved remarkable performance across a wide range of tasks. However, their substantial parameter sizes pose significant challenges for deployment on edge devices with limited computational and memory resources. Low-rank compression is a promising approach to address this issue, as it reduces both computational and memory costs, making LLM more suitable for resource-constrained environments. Nonetheless, naïve low-rank compression methods require a significant reduction in the retained rank to achieve meaningful memory and computation savings. For a low-rank model, the ranks need to be reduced by more than half to yield efficiency gains. Such aggressive truncation, however, typically results in substantial performance degradation. To address this trade-off, we propose SkipCat, a novel low-rank compression framework that enables the use of higher ranks while achieving the same compression rates. First, we introduce an intra-layer shared low-rank projection method, where multiple matrices that share the same input use a common projection. This reduces redundancy and improves compression efficiency. Second, we propose a block skipping technique that omits computations and memory transfers for selected sub-blocks within the low-rank decomposition. These two techniques jointly enable our compressed model to retain more effective ranks under the same compression budget. Experimental results show that, without any additional fine-tuning, our method outperforms previous low-rank compression approaches by 7% accuracy improvement on zero-shot tasks under the same compression rate. These results highlight the effectiveness of our rank-maximized compression strategy in preserving model performance under tight resource constraints. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted by AAAI 2026

### arXiv:2512.13510 MedCEG: Reinforcing Verifiable Medical Reasoning with Critical Evidence Graph

https://arxiv.org/abs/2512.13510

题摘原始内容：

Large language models with reasoning capabilities have demonstrated impressive performance across a wide range of domains. In clinical applications, a transparent, step-by-step reasoning process provides physicians with strong evidence to support decision-making. While reinforcement learning has effectively enhanced reasoning performance in medical contexts, the clinical reliability of these reasoning processes remains limited because their accuracy and validity are often overlooked during training. To address this gap, we propose MedCEG, a framework that augments medical language models with clinically valid reasoning pathways by explicitly supervising the reasoning process through a Critical Evidence Graph (CEG). We curate a dataset of challenging clinical cases and algorithmically construct a CEG for each sample to represent a high-quality verifiable reasoning pathway. To guide the reasoning process, we introduce a Clinical Reasoning Procedure Reward, which evaluates Node Coverage, Structural Correctness, and Chain Completeness, thereby providing a holistic assessment of reasoning quality. Experimental results show that MedCEG surpasses existing methods in performance while producing clinically valid reasoning chains, representing a solid advancement in reliable medical AI reasoning. The code and models are available at https://github.com/LinjieMu/MedCEG. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13576 Reproducing and Dissecting Denoising Language Models for Speech Recognition

https://arxiv.org/abs/2512.13576

题摘原始内容：

Denoising language models (DLMs) have been proposed as a powerful alternative to traditional language models (LMs) for automatic speech recognition (ASR), motivated by their ability to use bidirectional context and adapt to a specific ASR model's error patterns. However, the complexity of the DLM training pipeline has hindered wider investigation. This paper presents the first independent, large-scale empirical study of DLMs. We build and release a complete, reproducible pipeline to systematically investigate the impact of key design choices. We evaluate dozens of configurations across multiple axes, including various data augmentation techniques (e.g., SpecAugment, dropout, mixup), different text-to-speech systems, and multiple decoding strategies. Our comparative analysis in a common subword vocabulary setting demonstrates that DLMs outperform traditional LMs, but only after a distinct compute tipping point. While LMs are more efficient at lower budgets, DLMs scale better with longer training, mirroring behaviors observed in diffusion language models . However, we observe smaller improvements than those reported in prior character-based work, which indicates that the DLM's performance is conditional on factors such as the vocabulary. Our analysis reveals that a key factor for improving performance is to condition the DLM on richer information from the ASR's hypothesis space, rather than just a single best guess. To this end, we introduce DLM-sum, a novel method for decoding from multiple ASR hypotheses, which consistently outperforms the previously proposed DSR decoding method. We believe our findings and public pipeline provide a crucial foundation for the community to better understand, improve, and build upon this promising class of models. The code is publicly available at https://github.com/rwth-i6/2025-denoising-lm/. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Equal contribution of first two authors

### arXiv:2512.13598 Textual Gradients are a Flawed Metaphor for Automatic Prompt Optimization

https://arxiv.org/abs/2512.13598

题摘原始内容：

A well-engineered prompt can increase the performance of large language models ; automatic prompt optimization techniques aim to increase performance without requiring human effort to tune the prompts. One leading class of prompt optimization techniques introduces the analogy of textual gradients. We investigate the behavior of these textual gradient methods through a series of experiments and case studies. While such methods often result in a performance improvement, our experiments suggest that the gradient analogy does not accurately explain their behavior. Our insights may inform the selection of prompt optimization strategies, and development of new approaches. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13654 Large-Language Memorization During the Classification of United States Supreme Court Cases

https://arxiv.org/abs/2512.13654

题摘原始内容：

Large- language models (LLMs) have been shown to respond in a variety of ways for classification tasks outside of question-answering. LLM responses are sometimes called "hallucinations" since the output is not what is ex pected. Memorization strategies in LLMs are being studied in detail, with the goal of understanding how LLMs respond. We perform a deep dive into a classification task based on United States Supreme Court (SCOTUS) decisions. The SCOTUS corpus is an ideal classification task to study for LLM memory accuracy because it presents significant challenges due to extensive sentence length, complex legal terminology, non-standard structure, and domain-specific vocabulary. Experimentation is performed with the latest LLM fine tuning and retrieval-based approaches, such as parameter-efficient fine-tuning, auto-modeling, and others, on two traditional category-based SCOTUS classification tasks: one with 15 labeled topics and another with 279. We show that prompt-based models with memories, such as DeepSeek, can be more robust than previous BERT-based models on both tasks scoring about 2 points better than previous models not based on prompting. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 7 pages, 1 figure, Appendix of Prompts

### arXiv:2512.13658 Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance

https://arxiv.org/abs/2512.13658

题摘原始内容：

As the online learning landscape evolves, the need for personalization is increasingly evident. Although educational resources are burgeoning, educators face challenges selecting materials that both align with intended learning outcomes and address diverse learner needs. Large Language Models (LLMs) are attracting growing interest for their potential to create learning resources that better support personalization, but verifying coverage of intended outcomes still requires human alignment review, which is costly and limits scalability. We propose a framework that supports the cost-effective automation of evaluating alignment between educational resources and intended learning outcomes. Using human-generated materials, we benchmarked LLM-based text-embedding models and found that the most accurate model (Voyage) achieved 79% accuracy in detecting alignment. We then applied the optimal model to LLM-generated resources and, via expert evaluation, confirmed that it reliably assessed correspondence to intended outcomes (83% accuracy). Finally, in a three-group experiment with 360 learners, higher alignment scores were positively related to greater learning performance, chi-squared(2, N = 360) = 15.39, p < 0.001. These findings show that embedding-based alignment scores can facilitate scalable personalization by confirming alignment with learning outcomes, which allows teachers to focus on tailoring content to diverse learner needs. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted for publication at the 16th International Conference on Learning Analytics & Knowledge (LAK 2026)

### arXiv:2512.13668 A Scientific Reasoning Model for Organic Synthesis Procedure Generation

https://arxiv.org/abs/2512.13668

题摘原始内容：

Solving computer-aided synthesis planning is essential for enabling fully automated, robot-assisted synthesis workflows and improving the efficiency of drug discovery. A key challenge, however, is bridging the gap between computational route design and practical laboratory execution, particularly the accurate prediction of viable experimental procedures for each synthesis step. In this work, we present QFANG, a scientific reasoning language model capable of generating precise, structured experimental procedures directly from reaction equations, with explicit chain-of-thought reasoning. To develop QFANG, we curated a high-quality dataset comprising 905,990 chemical reactions paired with structured action sequences, extracted and processed from patent literature using large language models . We introduce a Chemistry-Guided Reasoning (CGR) framework that produces chain-of-thought data grounded in chemical knowledge at scale. The model subsequently undergoes supervised fine-tuning to elicit complex chemistry reasoning. Finally, we apply Reinforcement Learning from Verifiable Rewards (RLVR) to further enhance procedural accuracy. Experimental results demonstrate that QFANG outperforms advanced general-purpose reasoning models and nearest-neighbor retrieval baselines, measured by traditional NLP similarity metrics and a chemically aware evaluator using an LLM-as-a-judge. Moreover, QFANG generalizes to certain out-of-domain reaction classes and adapts to variations in laboratory conditions and user-specific constraints. We believe that QFANG's ability to generate high-quality synthesis procedures represents an important step toward bridging the gap between computational synthesis planning and fully automated laboratory synthesis. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13685 Beyond surface form: A pipeline for semantic analysis in Alzheimer's Disease detection from spontaneous speech

https://arxiv.org/abs/2512.13685

题摘原始内容：

Alzheimer's Disease (AD) is a progressive neurodegenerative condition that adversely affects cognitive abilities. Language-related changes can be automatically identified through the analysis of outputs from linguistic assessment tasks, such as picture description. Language models show promise as a basis for screening tools for AD, but their limited interpretability poses a challenge in distinguishing true linguistic markers of cognitive decline from surface-level textual patterns. To address this issue, we examine how surface form variation affects classification performance, with the goal of assessing the ability of language models to represent underlying semantic indicators. We introduce a novel approach where texts surface forms are transformed by altering syntax and vocabulary while preserving semantic content. The transformations significantly modify the structure and lexical content, as indicated by low BLEU and chrF scores, yet retain the underlying semantics, as reflected in high semantic similarity scores, isolating the effect of semantic information, and finding models perform similarly to if they were using the original text, with only small deviations in macro-F1. We also investigate whether language from picture descriptions retains enough detail to reconstruct the original image using generative models. We found that image-based transformations add substantial noise reducing classification accuracy. Our methodology provides a novel way of looking at what features influence model predictions, and allows the removal of possible spurious correlations. We find that just using semantic information, language model based classifiers can still detect AD. This work shows that difficult to detect semantic impairment can be identified, addressing an overlooked feature of linguistic deterioration, and opening new pathways for early detection systems. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13837 Explainable reinforcement learning from human feedback to improve alignment

https://arxiv.org/abs/2512.13837

题摘原始内容：

A common and effective strategy for humans to improve an unsatisfactory outcome in daily life is to find a cause of this outcome and correct the cause. In this paper, we investigate whether this human improvement strategy can be applied to improving reinforcement learning from human feedback (RLHF) for alignment of language models (LMs). In particular, it is observed in the literature that LMs tuned by RLHF can still output unsatisfactory responses. This paper proposes a method to improve the unsatisfactory responses by correcting their causes. Our method has two parts. The first part proposes a post-hoc explanation method to explain why an unsatisfactory response is generated to a prompt by identifying the training data that lead to this response. We formulate this problem as a constrained combinatorial optimization problem where the objective is to find a set of training data closest to this prompt-response pair in a feature representation space, and the constraint is that the prompt-response pair can be decomposed as a convex combination of this set of training data in the feature space. We propose an efficient iterative data selection algorithm to solve this problem. The second part proposes an unlearning method that improves unsatisfactory responses to some prompts by unlearning the training data that lead to these unsatisfactory responses and, meanwhile, does not significantly degrade satisfactory responses to other prompts. Experimental results demonstrate that our algorithm can improve RLHF. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13860 Verification-Guided Context Optimization for Tool Calling via Hierarchical LLMs-as-Editors

https://arxiv.org/abs/2512.13860

题摘原始内容：

Tool calling enables large language models (LLMs) to interact with external environments through tool invocation, providing a practical way to overcome the limitations of pretraining. However, the effectiveness of tool use depends heavily on the quality of the associated documentation and knowledge base context. These materials are usually written for human users and are often misaligned with how LLMs interpret information. This problem is even more pronounced in industrial settings, where hundreds of tools with overlapping functionality create challenges in scalability, variability, and ambiguity. We propose Verification-Guided Context Optimization (VGCO), a framework that uses LLMs as editors to automatically refine tool-related documentation and knowledge base context. VGCO works in two stages. First, Evaluation collects real-world failure cases and identifies mismatches between tools and their context. Second, Optimization performs hierarchical editing through offline learning with structure-aware, in-context optimization. The novelty of our LLM editors has three main aspects. First, they use a hierarchical structure that naturally integrates into the tool-calling workflow. Second, they are state-aware, action-specific, and verification-guided, which constrains the search space and enables efficient, targeted improvements. Third, they enable cost-efficient sub-task specialization, either by prompt engineering large editor models or by post-training smaller editor models. Unlike prior work that emphasizes multi-turn reasoning, VGCO focuses on the single-turn, large-scale tool-calling problem and achieves significant improvements in accuracy, robustness, and generalization across LLMs. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted by AAAI 2026 Workshop on Agentic AI Benchmarks and Applications for Enterprise Tasks

### arXiv:2512.15787 Toward Agentic Environments: GenAI and the Convergence of AI, Sustainability, and Human-Centric Spaces

https://arxiv.org/abs/2512.15787

题摘原始内容：

In recent years, advances in artificial intelligence (AI), particularly generative AI (GenAI) and large language models (LLMs), have made human-computer interactions more frequent, efficient, and accessible across sectors ranging from banking to healthcare. AI tools embedded in digital devices support decision-making and operational management at both individual and organizational levels, including resource allocation, workflow automation, and real-time data analysis. However, the prevailing cloud-centric deployment of AI carries a substantial environmental footprint due to high computational demands. In this context, this paper introduces the concept of agentic environments, a sustainability-oriented AI framework that extends beyond reactive systems by leveraging GenAI, multi-agent systems, and edge computing to reduce the environmental impact of technology. Agentic environments enable more efficient resource use, improved quality of life, and sustainability-by-design, while simultaneously enhancing data privacy through decentralized, edge-driven solutions. Drawing on secondary research as well as primary data from focus groups and semi-structured interviews with AI professionals from leading technology companies, the paper proposes a conceptual framework for agentic environments examined through three lenses: the personal sphere, professional and commercial use, and urban operations. The findings highlight the potential of agentic environments to foster sustainable ecosystems through optimized resource utilization and strengthened data privacy. The study concludes with recommendations for edge-driven deployment models to reduce reliance on energy-intensive cloud infrastructures. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Preprint, Paper submitted for publication in Sustainable Development (Wiley)

### arXiv:2512.14762 Workflows vs Agents for Code Translation

https://arxiv.org/abs/2512.14762

题摘原始内容：

Translating algorithms from high-level languages like MATLAB to hardware description languages (HDLs) is a resource-intensive but necessary step for deployment on FPGAs and ASICs. While large language models (LLMs) offer a path to automation, their limited training on HDL code makes end-to-end transpilation brittle and prone to syntax errors. We compare two LLM-driven methods for syntax repair in a MATLAB-to-HDL pipeline: a structured, expert-designed flow that follows a fixed sequence of operations, and a more autonomous agentic approach that uses the Model Context Protocol (MCP) \cite{anthropic2024mcp} to dynamically select its own tools. We study 42 MATLAB signal-processing functions and isolate the syntax-repair stage. Across three model scales, the agentic approach is more effective at resolving initial syntax errors, unblocking a greater number of candidates to proceed through the pipeline. This upstream improvement yields measurable downstream improvements, most notably on mid-sized models, where it increases the simulation reach rate by over 20 percentage points. We hypothesize the gains come from short prompts, aggressive context management, and conditional tool use. Conditional retrieval helps at 8B and 30B; at 235B final-success gains are small and a naive RAG variant attains the highest final success. Our findings suggest that these agentic frameworks, when properly designed, are most effective at compensating for the capacity limits of small and mid-sized models. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Journal ref: NeurIPS 2025 Fourth Workshop on Deep Learning for Code

### arXiv:2512.13884 FiNERweb: Datasets and Artifacts for Scalable Multilingual Named Entity Recognition

https://arxiv.org/abs/2512.13884

题摘原始内容：

Recent multilingual named entity recognition (NER) work has shown that large language models (LLMs) can provide effective synthetic supervision, yet such datasets have mostly appeared as by-products of broader experiments rather than as systematic, reusable resources. We introduce FiNERweb, a dataset-creation pipeline that scales the teacher-student paradigm to 91 languages and 25 scripts. Building on FineWeb-Edu, our approach trains regression models to identify NER-relevant passages and annotates them with multilingual LLMs, resulting in about 225k passages with 235k distinct entity labels. Our experiments show that the regression model achieves more than 84 F1, and that models trained on FiNERweb obtain comparable or improved performance in zero shot transfer settings on English, Thai, and Swahili, despite being trained on 19x less data than strong baselines. In addition, we assess annotation quality using LLM-as-a-judge and observe consistently high scores for both faithfulness (3.99 out of 5) and completeness (4.05 out of 5), indicating reliable and informative annotations. Further, we release the dataset with both English labels and translated label sets in the respective target languages because we observe that the performance of current state-of-the-art models drops by 0.02 to 0.09 F1 when evaluated using target language labels instead of English ones. We release FiNERweb together with all accompanying artifacts to the research community in order to facilitate more effective student-teacher training for multilingual named entity recognition. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13914 Context Branching for LLM Conversations: A Version Control Approach to Exploratory Programming

https://arxiv.org/abs/2512.13914

题摘原始内容：

Large Language Models (LLMs) have become integral to software engineering workflows, yet their effectiveness degrades significantly in multi-turn conversations. Recent studies demonstrate an average 39% performance drop when instructions are delivered across multiple turns, with models making premature assumptions and failing to course correct (Laban et al., 2025). This degradation is particularly problematic in exploratory programming tasks where developers need to investigate alternative approaches without committing to a single path. Current solutions force users into a false dichotomy: continue in a context-polluted conversation where the LLM becomes increasingly confused, or start fresh and lose all accumulated context. We present ContextBranch, a conversation management system that applies version control semantics to LLM interactions. ContextBranch provides four core primitives--checkpoint, branch, switch, and inject--enabling users to capture conversation state, explore alternatives in isolation, and selectively merge insights. We evaluate ContextBranch through a controlled experiment with 30 software engineering scenarios featuring intentionally polluting explorations. Branched conversations achieved higher response quality compared to linear conversations, with large improvements in focus and context awareness. Benefits were concentrated in complex scenarios involving conceptually distant explorations. Branching reduced context size by 58.1% (31.0 to 13.0 messages), eliminating irrelevant exploratory content. Our work establishes conversation branching as a fundamental primitive for AI-assisted exploratory work, demonstrating that isolation prevents context pollution when exploring alternatives. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 11 pages, 4 figures, 2 tables, 1 code snippet, 4 algorithms

### arXiv:2512.13921 Sliding Window Recurrences for Sequence Models

https://arxiv.org/abs/2512.13921

题摘原始内容：

Multi-hybrid architectures are poised to take over language modeling due to better quality and performance. We introduce a hierarchical decomposition framework for linear recurrences that allows us to develop algorithms aligned with GPU memory hierarchies, yielding Sliding Window Recurrences. We focus specifically on truncating recurrences to hardware-aligned windows which are naturally jagged, limiting costly inter-warp communication. Using SWR, we develop Phalanx layers that serve as drop-in replacements for windowed attention or linear recurrences. In 1B parameter multi-hybrid models, Phalanx achieves over 10-40% speedup across 4K to 32K context length over optimized Transformers while matching perplexity. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13930 Hierarchical Multi-agent Large Language Model Reasoning for Autonomous Functional Materials Discovery

https://arxiv.org/abs/2512.13930

题摘原始内容：

Artificial intelligence is reshaping scientific exploration, but most methods automate procedural tasks without engaging in scientific reasoning, limiting autonomy in discovery. We introduce Materials Agents for Simulation and Theory in Electronic-structure Reasoning (MASTER), an active learning framework where large language models autonomously design, execute, and interpret atomistic simulations. In MASTER, a multimodal system translates natural language into density functional theory workflows, while higher-level reasoning agents guide discovery through a hierarchy of strategies, including a single agent baseline and three multi-agent approaches: peer review, triage-ranking, and triage-forms. Across two chemical applications, CO adsorption on Cu-surface transition metal (M) adatoms and on M-N-C catalysts, reasoning-driven exploration reduces required atomistic simulations by up to 90% relative to trial-and-error selection. Reasoning trajectories reveal chemically grounded decisions that cannot be explained by stochastic sampling or semantic bias. Altogether, multi-agent collaboration accelerates materials discovery and marks a new paradigm for autonomous scientific exploration. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Keywords: Multi-agent reasoning; Large language models; Active learning; AI-driven simulation; Materials discovery; Density functional theory; Surface chemistry

### arXiv:2512.13935 Informing Acquisition Functions via Foundation Models for Molecular Discovery

https://arxiv.org/abs/2512.13935

题摘原始内容：

Bayesian Optimization (BO) is a key methodology for accelerating molecular discovery by estimating the mapping from molecules to their properties while seeking the optimal candidate. Typically, BO iteratively updates a probabilistic surrogate model of this mapping and optimizes acquisition functions derived from the model to guide molecule selection. However, its performance is limited in low-data regimes with insufficient prior knowledge and vast candidate spaces. Large language models (LLMs) and chemistry foundation models offer rich priors to enhance BO, but high-dimensional features, costly in-context learning, and the computational burden of deep Bayesian surrogates hinder their full utilization. To address these challenges, we propose a likelihood-free BO method that bypasses explicit surrogate modeling and directly leverages priors from general LLMs and chemistry-specific foundation models to inform acquisition functions. Our method also learns a tree-structured partition of the molecular search space with local acquisition functions, enabling efficient candidate selection via Monte Carlo Tree Search. By further incorporating coarse-grained LLM-based clustering, it substantially improves scalability to large candidate sets by restricting acquisition function evaluations to clusters with statistically higher property values. We show through extensive experiments and ablations that the proposed method substantially improves scalability, robustness, and sample efficiency in LLM-guided BO for molecular discovery. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.15790 Bilevel Optimization for Covert Memory Tampering in Heterogeneous Multi-Agent Architectures (XAMT)

https://arxiv.org/abs/2512.15790

题摘原始内容：

The increasing operational reliance on complex Multi-Agent Systems (MAS) across safety-critical domains necessitates rigorous adversarial robustness assessment. Modern MAS are inherently heterogeneous, integrating conventional Multi-Agent Reinforcement Learning (MARL) with emerging Large Language Model (LLM) agent architectures utilizing Retrieval-Augmented Generation (RAG). A critical shared vulnerability is reliance on centralized memory components: the shared Experience Replay (ER) buffer in MARL and the external Knowledge Base (K) in RAG agents. This paper proposes XAMT (Bilevel Optimization for Covert Memory Tampering in Heterogeneous Multi-Agent Architectures), a novel framework that formalizes attack generation as a bilevel optimization problem. The Upper Level minimizes perturbation magnitude (delta) to enforce covertness while maximizing system behavior divergence toward an adversary-defined target (Lower Level). We provide rigorous mathematical instantiations for CTDE MARL algorithms and RAG-based LLM agents, demonstrating that bilevel optimization uniquely crafts stealthy, minimal-perturbation poisons evading detection heuristics. Comprehensive experimental protocols utilize SMAC and SafeRAG benchmarks to quantify effectiveness at sub-percent poison rates (less than or equal to 1 percent in MARL, less than or equal to 0.1 percent in RAG). XAMT defines a new unified class of training-time threats essential for developing intrinsically secure MAS, with implications for trust, formal verification, and defensive strategies prioritizing intrinsic safety over perimeter-based detection. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 10 pages, 5 figures, 4 tables. Conference-style paper (IEEEtran). Proposes unified bilevel optimization framework for covert memory poisoning attacks in heterogeneous multi-agent systems (MARL + RAG)

### arXiv:2601.06042 CrossTrafficLLM: A Human-Centric Framework for Interpretable Traffic Intelligence via Large Language Model

https://arxiv.org/abs/2601.06042

题摘原始内容：

While accurate traffic forecasting is vital for Intelligent Transportation Systems (ITS), effectively communicating predicted conditions via natural language for human-centric decision support remains a challenge and is often handled separately. To address this, we propose CrossTrafficLLM, a novel GenAI-driven framework that simultaneously predicts future spatiotemporal traffic states and generates corresponding natural language descriptions, specifically targeting conditional abnormal event summaries. We tackle the core challenge of aligning quantitative traffic data with qualitative textual semantics by leveraging Large Language Models (LLMs) within a unified architecture. This design allows generative textual context to improve prediction accuracy while ensuring generated reports are directly informed by the forecast. Technically, a text-guided adaptive graph convolutional network is employed to effectively merge high-level semantic information with the traffic network structure. Evaluated on the BJTT dataset, CrossTrafficLLM demonstrably surpasses state-of-the-art methods in both traffic forecasting performance and text generation quality. By unifying prediction and description generation, CrossTrafficLLM delivers a more interpretable, and actionable approach to generative traffic intelligence, offering significant advantages for modern ITS applications. △ Less

日期/说明：Submitted 15 December, 2025; originally announced January 2026.

### arXiv:2512.13974 Autonomous Construction-Site Safety Inspection Using Mobile Robots: A Multilayer VLM-LLM Pipeline

https://arxiv.org/abs/2512.13974

题摘原始内容：

Construction safety inspection remains mostly manual, and automated approaches still rely on task-specific datasets that are hard to maintain in fast-changing construction environments due to frequent retraining. Meanwhile, field inspection with robots still depends on human teleoperation and manual reporting, which are labor-intensive. This paper aims to connect what a robot sees during autonomous navigation to the safety rules that are common in construction sites, automatically generating a safety inspection report. To this end, we proposed a multi-layer framework with two main modules: robotics and AI. On the robotics side, SLAM and autonomous navigation provide repeatable coverage and targeted revisits via waypoints. On AI side, a Vision Language Model (VLM)-based layer produces scene descriptions; a retrieval component powered grounds those descriptions in OSHA and site policies; Another VLM-based layer assesses the safety situation based on rules; and finally Large Language Model (LLM) layer generates safety reports based on previous outputs. The framework is validated with a proof-of-concept implementation and evaluated in a lab environment that simulates common hazards across three scenarios. Results show high recall with competitive precision compared to state-of-the-art closed-source models. This paper contributes a transparent, generalizable pipeline that moves beyond black-box models by exposing intermediate artifacts from each layer and keeping the human in the loop. This work provides a foundation for future extensions to additional tasks and settings within and beyond construction context. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13978 Evaluating Frontier LLMs on PhD-Level Mathematical Reasoning: A Benchmark on a Textbook in Theoretical Computer Science about Randomized Algorithms

https://arxiv.org/abs/2512.13978

题摘原始内容：

The rapid advancement of large language models (LLMs) has led to significant breakthroughs in automated mathematical reasoning and scientific discovery. Georgiev, G${ó}$mez-Serrano, Tao, and Wagner [GGSTW+25] demonstrate that AI systems can explore new constructions and improve existing bounds, illustrating the growing potential of LLMs to accelerate mathematical discovery. Similarly, Bubeck et al. [BCE+25] show that GPT-5 can meaningfully contribute to scientific workflows, from proposing hypotheses to generating proofs and analyses. Despite these advances, a rigorous evaluation of these models on canonical, graduate-level mathematical theory remains necessary to understand their baseline reasoning capabilities. In this paper, we present a comprehensive benchmark of four frontier models: GPT-5-Thinking, Gemini-3-Pro, Claude-Sonnet-4.5-Thinking, and Grok-4 against the classic curriculum of Randomized Algorithms by Motwani and Raghavan [MR95]. We tasked each model with generating formal LaTeX proofs for a series of lemmas and exercises spanning the textbook. We find that while the top-tier models (Gemini, and Claude) achieve a high accuracy rate (approx. 66%), demonstrating a robust grasp of probabilistic method and formal logic, other models lag significantly in consistency (approx. 40%). We provide a qualitative analysis of the generated proofs, highlighting differences in conciseness, hallucination rates, and logical structure. Our results suggest that while frontier models have reached a threshold of proficiency suitable for graduate-level pedagogical assistance and formalization, significant variance exists in their reliability for rigorous mathematical derivation. The code and the full set of LLM-generated responses are open-sourced and publicly available at https://github.com/magiclinux/math_benchmark_probability. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14014 MobileWorldBench: Towards Semantic World Modeling For Mobile Agents

https://arxiv.org/abs/2512.14014

题摘原始内容：

World models have shown great utility in improving the task performance of embodied agents. While prior work largely focuses on pixel-space world models, these approaches face practical limitations in GUI settings, where predicting complex visual elements in future states is often difficult. In this work, we explore an alternative formulation of world modeling for GUI agents, where state transitions are described in natural language rather than predicting raw pixels. First, we introduce MobileWorldBench, a benchmark that evaluates the ability of vision- language models (VLMs) to function as world models for mobile GUI agents. Second, we release MobileWorld, a large-scale dataset consisting of 1.4M samples, that significantly improves the world modeling capabilities of VLMs. Finally, we propose a novel framework that integrates VLM world models into the planning framework of mobile agents, demonstrating that semantic world models can directly benefit mobile agents by improving task success rates. The code and dataset is available at https://github.com/jacklishufan/MobileWorld △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: 21 pages, 13 figures

### arXiv:2512.14017 KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding

https://arxiv.org/abs/2512.14017

题摘原始内容：

We propose KFS-Bench, the first benchmark for key frame sampling in long video question answering (QA), featuring multi-scene annotations to enable direct and robust evaluation of sampling strategies. Key frame sampling is crucial for efficient long-form video understanding. In long video QA, selecting informative frames enables multimodal large language models (MLLMs) to improve both accuracy and efficiency. KFS-Bench addresses the limitation of prior works that only indirectly assess frame selection quality via QA accuracy. By providing ground-truth annotations of multiple disjoint scenes required per question, KFS-Bench allows us to directly analyze how different sampling approaches capture essential content across an entire long video. Using KFS-Bench, we conduct a comprehensive study of key frame sampling methods and identify that not only sampling precision but also scene coverage and sampling balance are the key factors influencing QA performance. Regarding all the factors, we design a novel sampling quality metric that correlates with QA accuracy. Furthermore, we develop a novel key frame sampling method that leverages question-video relevance to balance sampling diversity against question-frame similarity, thereby improving coverage of relevant scenes. Our adaptively balanced sampling approach achieves superior performance in both key frame sampling and QA performance. The benchmark is available at https://github.com/NEC-VID/KFS-Bench. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: WACV2026

### arXiv:2512.20647 Reasoning Relay: Evaluating Stability and Interchangeability of Large Language Models in Mathematical Reasoning

https://arxiv.org/abs/2512.20647

题摘原始内容：

Chain-of-Thought (CoT) prompting has significantly advanced the reasoning capabilities of large language models (LLMs). While prior work focuses on improving model performance through internal reasoning strategies, little is known about the interchangeability of reasoning across different models. In this work, we explore whether a partially completed reasoning chain from one model can be reliably continued by another model, either within the same model family or across families. We achieve this by assessing the sufficiency of intermediate reasoning traces as transferable scaffolds for logical coherence and final answer accuracy. We interpret this interchangeability as a means of examining inference-time trustworthiness, probing whether reasoning remains both coherent and reliable under model substitution. Using token-level log-probability thresholds to truncate reasoning at early, mid, and late stages from our baseline models, Gemma-3-4B-IT and LLaMA-3.1-70B-Instruct, we conduct continuation experiments with Gemma-3-1B-IT and LLaMA-3.1-8B-Instruct to test intra-family and cross-family behaviors. Our evaluation pipeline leverages truncation thresholds with a Process Reward Model (PRM), providing a reproducible framework for assessing reasoning stability via model interchange. Evaluations with a PRM reveal that hybrid reasoning chains often preserve, and in some cases even improve, final accuracy and logical structure. Our findings point towards interchangeability as an emerging behavioral property of reasoning models, offering insights into new paradigms for reliable modular reasoning in collaborative AI systems. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: NeurIPS 2025 Workshop on Socially Responsible and Trustworthy Foundation Models (ResponsibleFM)

### arXiv:2512.13573 MMhops-R1: Multimodal Multi-hop Reasoning

https://arxiv.org/abs/2512.13573

题摘原始内容：

The ability to perform multi-modal multi-hop reasoning by iteratively integrating information across various modalities and external knowledge is critical for addressing complex real-world challenges. However, existing Multi-modal Large Language Models (MLLMs) are predominantly limited to single-step reasoning, as existing benchmarks lack the complexity needed to evaluate and drive multi-hop abilities. To bridge this gap, we introduce MMhops, a novel, large-scale benchmark designed to systematically evaluate and foster multi-modal multi-hop reasoning. MMhops dataset comprises two challenging task formats, Bridging and Comparison, which necessitate that models dynamically construct complex reasoning chains by integrating external knowledge. To tackle the challenges posed by MMhops, we propose MMhops-R1, a novel multi-modal Retrieval-Augmented Generation (mRAG) framework for dynamic reasoning. Our framework utilizes reinforcement learning to optimize the model for autonomously planning reasoning paths, formulating targeted queries, and synthesizing multi-level information. Comprehensive experiments demonstrate that MMhops-R1 significantly outperforms strong baselines on MMhops, highlighting that dynamic planning and multi-modal knowledge integration are crucial for complex reasoning. Moreover, MMhops-R1 demonstrates strong generalization to tasks requiring fixed-hop reasoning, underscoring the robustness of our dynamic planning approach. In conclusion, our work contributes a challenging new benchmark and a powerful baseline model, and we will release the associated code, data, and weights to catalyze future research in this critical area. △ Less

日期/说明：Submitted 15 December, 2025; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Acceped by AAAI 2026

### arXiv:2512.14040 ChartAgent: A Chart Understanding Framework with Tool Integrated Reasoning

https://arxiv.org/abs/2512.14040

题摘原始内容：

With their high information density and intuitive readability, charts have become the de facto medium for data analysis and communication across disciplines. Recent multimodal large language models (MLLMs) have made notable progress in automated chart understanding, yet they remain heavily dependent on explicit textual annotations and the performance degrades markedly when key numerals are absent. To address this limitation, we introduce ChartAgent, a chart understanding framework grounded in Tool-Integrated Reasoning (TIR). Inspired by human cognition, ChartAgent decomposes complex chart analysis into a sequence of observable, replayable steps. Supporting this architecture is an extensible, modular tool library comprising more than a dozen core tools, such as keyelement detection, instance segmentation, and optical character recognition (OCR), which the agent dynamically orchestrates to achieve systematic visual parsing across diverse chart types. Leveraging TIRs transparency and verifiability, ChartAgent moves beyond the black box paradigm by standardizing and consolidating intermediate outputs into a structured Evidence Package, providing traceable and reproducible support for final conclusions. Experiments show that ChartAgent substantially improves robustness under sparse annotation settings, offering a practical path toward trustworthy and extensible systems for chart understanding. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14043 Evaluating Small Language Models for Agentic On-Farm Decision Support Systems

https://arxiv.org/abs/2512.14043

题摘原始内容：

Large Language Models (LLM) hold potential to support dairy scholars and farmers by supporting decision-making and broadening access to knowledge for stakeholders with limited technical expertise. However, the substantial computational demand restricts access to LLM almost exclusively through cloud-based service, which makes LLM-based decision support tools impractical for dairy farming. To address this gap, lightweight alternatives capable of running locally on farm hardware are required. In this work, we benchmarked 20 open-source Small Language Models (SLM) available on HuggingFace under farm-realistic computing constraints. Building on our prior work, we developed an agentic AI system that integrates five task-specific agents: literature search, web search, SQL database interaction, NoSQL database interaction, and graph generation following predictive models. Evaluation was conducted in two phases. In the first phase, five test questions were used for the initial screening to identify models capable of following basic dairy-related instructions and performing reliably in a compute-constrained environment. Models that passed this preliminary stage were then evaluated using 30 questions (five per task category mentioned above, plus one category addressing integrity and misconduct) in phase two. In results, Qwen-4B achieved superior performance across most of task categories, although showed unstable effectiveness in NoSQL database interactions through PySpark. To our knowledge, this is the first work explicitly evaluating the feasibility of SLM as engines for dairy farming decision-making, with central emphases on privacy and computational efficiency. While results highlight the promise of SLM-assisted tools for practical deployment in dairy farming, challenges remain, and fine-tuning is still needed to refine SLM performance in dairy-specific questions. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14048 Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation

https://arxiv.org/abs/2512.14048

题摘原始内容：

Large language models (LLMs) exhibit strong generative capabilities and have shown great potential in code generation. Existing chain-of-thought (CoT) prompting methods enhance model reasoning by eliciting intermediate steps, but suffer from two major limitations: First, their uniform application tends to induce overthinking on simple tasks. Second, they lack intention abstraction in code generation, such as explicitly modeling core algorithmic design and efficiency, leading models to focus on surface-level structures while neglecting the global problem objective. Inspired by the cognitive economy principle of engaging structured reasoning only when necessary to conserve cognitive resources, we propose RoutingGen, a novel difficulty-aware routing framework that dynamically adapts prompting strategies for code generation. For simple tasks, it adopts few-shot prompting; for more complex ones, it invokes a structured reasoning strategy, termed Intention Chain-of-Thought (ICoT), which we introduce to guide the model in capturing task intention, such as the core algorithmic logic and its time complexity. Experiments across three models and six standard code generation benchmarks show that RoutingGen achieves state-of-the-art performance in most settings, while reducing total token usage by 46.37% on average across settings. Furthermore, ICoT outperforms six existing prompting baselines on challenging benchmarks. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted at AAAI-2026

### arXiv:2512.14051 OpenDataArena: A Fair and Open Arena for Benchmarking Post-Training Dataset Value

https://arxiv.org/abs/2512.14051

题摘原始内容：

The rapid evolution of Large Language Models (LLMs) is predicated on the quality and diversity of post-training datasets. However, a critical dichotomy persists: while models are rigorously benchmarked, the data fueling them remains a black box--characterized by opaque composition, uncertain provenance, and a lack of systematic evaluation. This opacity hinders reproducibility and obscures the causal link between data characteristics and model behaviors. To bridge this gap, we introduce OpenDataArena (ODA), a holistic and open platform designed to benchmark the intrinsic value of post-training data. ODA establishes a comprehensive ecosystem comprising four key pillars: (i) a unified training-evaluation pipeline that ensures fair, open comparisons across diverse models (e.g., Llama, Qwen) and domains; (ii) a multi-dimensional scoring framework that profiles data quality along tens of distinct axes; (iii) an interactive data lineage explorer to visualize dataset genealogy and dissect component sources; and (iv) a fully open-source toolkit for training, evaluation, and scoring to foster data research. Extensive experiments on ODA--covering over 120 training datasets across multiple domains on 22 benchmarks, validated by more than 600 training runs and 40 million processed data points--reveal non-trivial insights. Our analysis uncovers the inherent trade-offs between data complexity and task performance, identifies redundancy in popular benchmarks through lineage tracing, and maps the genealogical relationships across datasets. We release all results, tools, and configurations to democratize access to high-quality data evaluation. Rather than merely expanding a leaderboard, ODA envisions a shift from trial-and-error data curation to a principled science of Data-Centric AI, paving the way for rigorous studies on data mixing laws and the strategic composition of foundation models. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14052 HyperVL: An Efficient and Dynamic Multimodal Large Language Model for Edge Devices

https://arxiv.org/abs/2512.14052

题摘原始内容：

Current multimodal large lanauge models possess strong perceptual and reasoning capabilities, however high computational and memory requirements make them difficult to deploy directly on on-device environments. While small-parameter models are progressively endowed with strong general capabilities, standard Vision Transformer (ViT) encoders remain a critical bottleneck, suffering from excessive latency and memory consumption when processing high-resolution inputs.To address these challenges, we introduce HyperVL, an efficient multimodal large language model tailored for on-device inference. HyperVL adopts an image-tiling strategy to cap peak memory usage and incorporates two novel techniques: (1) a Visual Resolution Compressor (VRC) that adaptively predicts optimal encoding resolutions to eliminate redundant computation, and (2) Dual Consistency Learning (DCL), which aligns multi-scale ViT encoders within a unified framework, enabling dynamic switching between visual branches under a shared LLM. Extensive experiments demonstrate that HyperVL achieves state-of-the-art performance among models of comparable size across multiple benchmarks. Furthermore, it significantly significantly reduces latency and power consumption on real mobile devices, demonstrating its practicality for on-device multimodal inference. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025. | Comments: Technical report of Xiaomi HyperAI Team

### arXiv:2512.14064 What Affects the Effective Depth of Large Language Models?

https://arxiv.org/abs/2512.14064

题摘原始内容：

The scaling of large language models (LLMs) emphasizes increasing depth, yet performance gains diminish with added layers. Prior work introduces the concept of "effective depth", arguing that deeper models fail to fully utilize their layers for meaningful computation. Building on this, we systematically study how effective depth varies with model scale, training type, and task difficulty. First, we analyze the model behavior of Qwen-2.5 family (1.5B-32B) and find that while the number of effective layers grows with model size, the effective depth ratio remains stable. Besides, comparisons between base and corresponding long-CoT models show no increase in effective depth, suggesting that improved reasoning stems from longer context rather than deeper per-token computation. Furthermore, evaluations across tasks of varying difficulty indicate that models do not dynamically use more layers for harder problems. Our results suggest that current LLMs underuse available depth across scales, training paradigms and tasks of varying difficulties, pointing out research opportunities on increasing the layer utilization rate of LLMs, model pruning, and early exiting. Our code is released at https://github.com/AheadOFpotato/what_affects_effective_depth. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14068 SDAR-VL: Stable and Efficient Block-wise Diffusion for Vision-Language Understanding

https://arxiv.org/abs/2512.14068

题摘原始内容：

Block-wise discrete diffusion offers an attractive balance between parallel generation and causal dependency modeling, making it a promising backbone for vision- language modeling . However, its practical adoption has been limited by high training cost, slow convergence, and instability, which have so far kept it behind strong autoregressive (AR) baselines. We present \textbf{SDAR-VL}, the first systematic application of block-wise discrete diffusion to large-scale vision-language understanding (VLU), together with an \emph{integrated framework for efficient and stable training}. This framework unifies three components: (1) \textbf{Asynchronous Block-wise Noise Scheduling} to diversify supervision within each batch; (2) \textbf{Effective Mask Ratio Scaling} for unbiased loss normalization under stochastic masking; and (3) a \textbf{Progressive Beta Noise Curriculum} that increases effective mask coverage while preserving corruption diversity. Experiments on 21 single-image, multi-image, and video benchmarks show that SDAR-VL consistently improves \emph{training efficiency}, \emph{convergence stability}, and \emph{task performance} over conventional block diffusion. On this evaluation suite, SDAR-VL sets a new state of the art among diffusion-based vision- language models and, under matched settings, matches or surpasses strong AR baselines such as LLaVA-OneVision as well as the global diffusion baseline LLaDA-V, establishing block-wise diffusion as a practical backbone for VLU. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14070 From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis

https://arxiv.org/abs/2512.14070

题摘原始内容：

JavaScript's widespread adoption has made it an attractive target for malicious attackers who employ sophisticated obfuscation techniques to conceal harmful code. Current deobfuscation tools suffer from critical limitations that severely restrict their practical effectiveness. Existing tools struggle with diverse input formats, address only specific obfuscation types, and produce cryptic output that impedes human analysis. To address these challenges, we present JSIMPLIFIER, a comprehensive deobfuscation tool using a multi-stage pipeline with preprocessing, abstract syntax tree-based static analysis, dynamic execution tracing, and Large Language Model (LLM)-enhanced identifier renaming. We also introduce multi-dimensional evaluation metrics that integrate control/data flow analysis, code simplification assessment, entropy measures and LLM-based readability assessments. We construct and release the largest real-world obfuscated JavaScript dataset with 44,421 samples (23,212 wild malicious + 21,209 benign samples). Evaluation shows JSIMPLIFIER outperforms existing tools with 100% processing capability across 20 obfuscation techniques, 100% correctness on evaluation subsets, 88.2% code complexity reduction, and over 4-fold readability improvement validated by multiple LLMs. Our results advance benchmarks for JavaScript deobfuscation research and practical security applications. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14082 A Unified Sparse Attention via Multi-Granularity Compression

https://arxiv.org/abs/2512.14082

题摘原始内容：

Efficient long-context understanding and reasoning are increasingly vital for large language model (LLM) applications such as multi-turn dialogue and program analysis. However, the core self-attention mechanism scales quadratically with sequence length, creating a fundamental computational bottleneck. Existing sparse attention methods alleviate this issue but face trade-offs: training-based methods are costly and cannot be directly applied as acceleration plugins for other models, while inference-time methods often compromise efficiency or cross-modal generality. To address these limitations, we present UniSparse, a unified mechanism that introduces the notion of composite tokens--compact representations that aggregate multi-granularity contextual information. Building on this abstraction, UniSparse dynamically constructs sparse attention through multi-granularity compression and block-level selection, enabling efficient and hardware-friendly execution on GPU. Across multiple modalities and tasks ranging from synthetic benchmarks to real-world applications, UniSparse consistently surpasses state-of-the-art sparse attention methods (e.g., MInference, XAttention, FlexPrefill) in both accuracy and efficiency, achieving $\ge$ 99% of full-attention accuracy and up to 2.61$\times$ faster attention computation than FlashAttention. △ Less

日期/说明：Submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13177 MMDrive: Interactive Scene Understanding Beyond Vision with Multi-representational Fusion

https://arxiv.org/abs/2512.13177

题摘原始内容：

Vision- language models enable the understanding and reasoning of complex traffic scenarios through multi-source information fusion, establishing it as a core technology for autonomous driving. However, existing vision- language models are constrained by the image understanding paradigm in 2D plane, which restricts their capability to perceive 3D spatial information and perform deep semantic fusion, resulting in suboptimal performance in complex autonomous driving environments. This study proposes MMDrive, an multimodal vision- language model framework that extends traditional image understanding to a generalized 3D scene understanding framework. MMDrive incorporates three complementary modalities, including occupancy maps, LiDAR point clouds, and textual scene descriptions. To this end, it introduces two novel components for adaptive cross-modal fusion and key information extraction. Specifically, the Text-oriented Multimodal Modulator dynamically weights the contributions of each modality based on the semantic cues in the question, guiding context-aware feature integration. The Cross-Modal Abstractor employs learnable abstract tokens to generate compact, cross-modal summaries that highlight key regions and essential semantics. Comprehensive evaluations on the DriveLM and NuScenes-QA benchmarks demonstrate that MMDrive achieves significant performance gains over existing vision- language models for autonomous driving, with a BLEU-4 score of 54.56 and METEOR of 41.78 on DriveLM, and an accuracy score of 62.7% on NuScenes-QA. MMDrive effectively breaks the traditional image-only understanding barrier, enabling robust multimodal reasoning in complex driving environments and providing a new foundation for interpretable autonomous driving scene understanding. △ Less

日期/说明：Submitted 16 December, 2025; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13194 Efficient Adaptive Rejection Sampling for Accelerating Speculative Decoding in Large Language Models

https://arxiv.org/abs/2512.13194

题摘原始内容：

Speculative Decoding is a prominent technique for accelerating the autoregressive inference of large language models (LLMs) by employing a fast draft model to propose candidate token sequences and a large target model to verify them in parallel. However, its core component -- the rejection sampling mechanism -- relies on a fixed, context-independent random threshold. This leads to a significant "random rejection" problem in high-uncertainty generation scenarios, where plausible candidate tokens are frequently rejected due to random chance, undermining inference efficiency. This paper introduces Efficient Adaptive Rejection Sampling (EARS), a novel method that dynamically adjusts the acceptance threshold by incorporating the target model's own predictive uncertainty, measured as 1 - max(P_target). By introducing a tolerance term proportional to this uncertainty, EARS intelligently relaxes the acceptance criterion when the model is uncertain, effectively reducing random rejections while maintaining strict standards when the model is confident. Experiments on creative writing and open-domain QA tasks demonstrate that EARS significantly enhances the efficiency of speculative decoding, achieving up to an 18.12% increase in throughput with a negligible 0.84% accuracy drop on the GSM8K benchmark. The method requires no modifications to model architectures and can be seamlessly integrated into existing speculative decoding frameworks. △ Less

日期/说明：Submitted 16 December, 2025; v1 submitted 15 December, 2025; originally announced December 2025. | MSC Class: 68T50 ACM Class: I.2.7

### arXiv:2512.13857 EvoLattice: Persistent Internal-Population Evolution through Multi-Alternative Quality-Diversity Graph Representations for LLM-Guided Program Discovery

https://arxiv.org/abs/2512.13857

题摘原始内容：

Large language models (LLMs) are increasingly used to evolve programs and multi-agent systems, yet most existing approaches rely on overwrite-based mutations that maintain only a single candidate at a time. Such methods discard useful variants, suffer from destructive edits, and explore a brittle search space prone to structural failure. We introduce EvoLattice, a framework that represents an entire population of candidate programs or agent behaviors within a single directed acyclic graph. Each node stores multiple persistent alternatives, and every valid path through the graph defines a distinct executable candidate, yielding a large combinatorial search space without duplicating structure. EvoLattice enables fine-grained alternative-level evaluation by scoring each alternative across all paths in which it appears, producing statistics that reveal how local design choices affect global performance. These statistics provide a dense, data-driven feedback signal for LLM-guided mutation, recombination, and pruning, while preserving successful components. Structural correctness is guaranteed by a deterministic self-repair mechanism that enforces acyclicity and dependency consistency independently of the LLM. EvoLattice naturally extends to agent evolution by interpreting alternatives as prompt fragments or sub-agent behaviors. Across program synthesis (proxy and optimizer meta-learning), EvoLattice yields more stable evolution, greater expressivity, and stronger improvement trajectories than prior LLM-guided methods. The resulting dynamics resemble quality-diversity optimization, emerging implicitly from EvoLattice's internal multi-alternative representation rather than an explicit external archive. △ Less

日期/说明：Submitted 17 December, 2025; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.17948 Physicists Are Still Joking

https://arxiv.org/abs/2512.17948

题摘原始内容：

This volume, \textbf{Physicists Are Still Joking}, serves as a definitive almanac of scientific humor spanning sixty years. It traces the evolution of professional folklore across geopolitical divides and technological eras. \textbf{Part I} restores the classic 1966 anthology \textbf{Physicists Joke}, which originally served as a window for Soviet scientists into the best traditions of Western scientific humor; it consists primarily of articles translated from English, here meticulously restored to their original wording. \textbf{Part II} presents the 1992 sequel, \textbf{Physicists Keep Joking}, which captures the shift toward an original, introspective Russian scientific folklore born during the end of the Cold War and the collapse of the Soviet Union. \textbf{Part III: Still Joking} explores the modern digital age, compiling contemporary science humor from physics, astronomy, biology, computer science and AI research. While the tools of science have evolved from slide rules to neural networks, the tradition of skeptical, self-referential wit remains a constant. Spanning from the "Golden Age" of vacuum tubes to the era of AI and Large Language Models , this collection documents the enduring ability of scientists to laugh at the universe and themselves. △ Less

日期/说明：Submitted 27 December, 2025; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 156 pages

### arXiv:2512.22149 Adaptive GPU Resource Allocation for Multi-Agent Collaborative Reasoning in Serverless Environments

https://arxiv.org/abs/2512.22149

题摘原始内容：

Multi-agent systems powered by large language models have emerged as a promising paradigm for solving complex reasoning tasks through collaborative intelligence. However, efficiently deploying these systems on serverless GPU platforms presents significant resource allocation challenges due to heterogeneous agent workloads, varying computational demands, and the need for cost-effective scaling. This paper presents an adaptive GPU resource allocation framework that achieves 85% latency reduction compared to round-robin scheduling while maintaining comparable throughput to static allocation, using an O(N) complexity algorithm for real-time adaptation. Our approach dynamically allocates GPU resources based on workload characteristics, agent priorities, and minimum resource requirements, enabling efficient utilization while maintaining quality of service. The framework addresses three key challenges: (1) heterogeneous computational demands across lightweight coordinators and heavyweight specialists, (2) dynamic workload fluctuations requiring millisecond-scale reallocation, and (3) capacity constraints in serverless environments. Through comprehensive simulations modeling realistic multi-agent workflows with four heterogeneous agents, we demonstrate that adaptive allocation outperforms static equal and round-robin strategies across latency, cost, and GPU utilization metrics. The framework provides a practical solution for deploying cost-efficient multi-agent AI systems on serverless GPU infrastructure. △ Less

日期/说明：Submitted 31 December, 2025; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 6 pages, 2 figures | ACM Class: I.2.11; C.2.4 | Journal ref: 2025 IEEE Computing, Communications and IoT Applications (ComComAP)

### arXiv:2512.13251 DisCo-Speech: Controllable Zero-Shot Speech Generation with A Disentangled Speech Codec

https://arxiv.org/abs/2512.13251

题摘原始内容：

Codec-based language models (LMs) have revolutionized text-to-speech (TTS). However, standard codecs entangle timbre and prosody, which hinders independent control in continuation-based LMs. To tackle this challenge, we propose DisCo-Speech, a zero-shot controllable TTS framework featuring a disentangled speech codec (DisCodec) and an LM-based generator. The core component DisCodec employs a two-stage design: 1) tri-factor disentanglement to separate speech into content, prosody, and timbre subspaces via parallel encoders and hybrid losses; and 2) fusion and reconstruction that merges content and prosody into unified content-prosody tokens suitable for LM prediction, while jointly optimizing reconstruction to address the disentanglement-reconstruction trade-off. This allows the LM to perform prosodic continuation from a style prompt while the decoder injects target timbre, enabling flexible zero-shot control. Experiments demonstrate that DisCo-Speech achieves competitive voice cloning and superior zero-shot prosody control. By resolving the core entanglement at the codec level, DisCo-Speech provides a robust foundation for controllable speech synthesis. △ Less

日期/说明：Submitted 3 January, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Updated with 6,000 hours of additional training data and improved performance. Expanded appendix with ablation studies, training objectives, and hyperparameter settings for better reproducibility. Audio and code links included

### arXiv:2512.13102 Socratic Students: Teaching Language Models to Learn by Asking Questions

https://arxiv.org/abs/2512.13102

题摘原始内容：

Large language Models (LLMs) are usually used to answer questions, but many high-stakes applications (e.g., tutoring, clinical support) require the complementary skill of asking questions: detecting missing information, requesting clarifications, and using them to solve tasks. We study this skill in reasoning-heavy domains where progress depends on inquiry rather than factual recall. We define an interactive protocol where a student model engages a stronger teacher under a small turn budget. After each teacher reply, we evaluate the student on the original task with Pass@k. We propose Outcome-Driven Question optimization Strategy (ODQS ), a training framework that learns a questioning policy from downstream task outcomes. At each turn, we sample multiple candidate questions; query the teacher with each, then score the student's resulting performance. Using these scores, we train the student via supervised fine-tuning followed by Direct Preference Optimization (DPO), without any human labels. On GSM8K, HumanEval, and OpenCoder, ODQS produces large gains over interactive baselines, boosting Pass@5 by up to 54.7% (absolute) on math and 22.9% (absolute) on coding, and matching baseline performance in three fewer turns. Thus, question asking can be explicitly trained from task outcomes, improving both accuracy and efficiency in interactive reasoning. △ Less

日期/说明：Submitted 6 January, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13655 Comparative Analysis of LLM Abliteration Methods: A Cross-Architecture Evaluation

https://arxiv.org/abs/2512.13655

题摘原始内容：

Safety alignment mechanisms in large language models prevent responses to harmful queries through learned refusal behavior, yet these same mechanisms impede legitimate research applications including cognitive modeling, adversarial testing, and security analysis. While abliteration techniques enable surgical removal of refusal representations through directional orthogonalization, the relative effectiveness of available implementations remains uncharacterized. This study evaluates four abliteration tools (Heretic, DECCP, ErisForge, FailSpy) across sixteen instruction-tuned models (7B-14B parameters), reporting tool compatibility on all 16 models and quantitative metrics on subsets dictated by tool support. Single-pass methods demonstrated superior capability preservation on the benchmarked subset (avg GSM8K change across three models: ErisForge -0.28 pp; DECCP -0.13 pp), while Bayesian-optimized abliteration produced variable distribution shift (KL divergence: 0.043-1.646) with model-dependent capability impact. These findings provide researchers with evidence-based selection criteria for abliteration tool deployment across diverse model architectures. The principal finding indicates that mathematical reasoning capabilities exhibit the highest sensitivity to abliteration interventions, with GSM8K change ranging from +1.51 pp to -18.81 pp (-26.5% relative) depending on tool selection and model architecture. △ Less

日期/说明：Submitted 7 January, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 25 pages, 6 figures, 8 tables | ACM Class: I.2.7

### arXiv:2512.13481 neuralFOMO: Can LLMs Handle Being Second Best? Measuring Envy-Like Preferences in Multi-Agent Settings

https://arxiv.org/abs/2512.13481

题摘原始内容：

Envy shapes competitiveness and cooperation in human groups, yet its role in large language model interactions remains largely unexplored. As LLMs increasingly operate in multi-agent settings, it is important to examine whether they exhibit envy-like preferences under social comparison. We evaluate LLM behavior across two scenarios: (1) a point-allocation game testing sensitivity to relative versus absolute payoff, and (2) comparative evaluations across general and contextual settings. To ground our analysis in psychological theory, we adapt four established psychometric questionnaires spanning general, domain-specific, workplace, and sibling-based envy. Our results reveal heterogeneous envy-like patterns across models and contexts, with some models sacrificing personal gain to reduce a peer's advantage, while others prioritize individual maximization. These findings highlight competitive dispositions as a design and safety consideration for multi-agent LLM systems. △ Less

日期/说明：Submitted 25 January, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Under Review

### arXiv:2512.13980 Structure-Aware Decoding Mechanisms for Complex Entity Extraction with Large-Scale Language Models

https://arxiv.org/abs/2512.13980

题摘原始内容：

This paper proposes a structure-aware decoding method based on large language models to address the difficulty of traditional approaches in maintaining both semantic integrity and structural consistency in nested and overlapping entity extraction tasks. The method introduces a candidate span generation mechanism and structured attention modeling to achieve unified modeling of entity boundaries, hierarchical relationships, and cross-dependencies. The model first uses a pretrained language model to obtain context-aware semantic representations, then captures multi-granular entity span features through candidate representation combinations, and introduces hierarchical structural constraints during decoding to ensure consistency between semantics and structure. To enhance stability in complex scenarios, the model jointly optimizes classification loss and structural consistency loss, maintaining high recognition accuracy under multi-entity co-occurrence and long-sentence dependency conditions. Experiments conducted on the ACE 2005 dataset demonstrate significant improvements in Accuracy, Precision, Recall, and F1-Score, particularly in nested and overlapping entity recognition, where the model shows stronger boundary localization and structural modeling capability. This study verifies the effectiveness of structure-aware decoding in complex semantic extraction tasks, provides a new perspective for developing language models with hierarchical understanding, and establishes a methodological foundation for high-precision information extraction. △ Less

日期/说明：Submitted 28 January, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13515 Fine-tuned LLM-based Code Migration Framework

https://arxiv.org/abs/2512.13515

题摘原始内容：

The study presents the outcomes of research and experimental validation in the domain of automated codebase migration, with a focus on addressing challenges in transitioning SQL-based systems. The proposed method for migration essentially appears as a framework that leverages the best aspects of traditional software engineering techniques and provides an iterative, scalable, precise and efficient solution for modern database transformations. The central piece of the approach is the integration of a fine-tuned Large Language Model to address critical issues in SQL code conversion, such as syntax mapping, resolving discrepancies between Oracle PL/SQL and PostgreSQL, and optimising database elements such as stored procedures, triggers, views, and overall database logic. Thus, the method involves a trade-off between fine-tuning and prompt engineering. Special attention is given to a fine-tuning approach, which enhances the adaptability and compatibility with migration requirements across the entire database. According to the achieved results, fine-tuning plays a very important role. The study employs targeted evaluation methodologies along with computational metrics to measure the success of iterative conversion cycles. Core innovations include automated SQL feature detection, semi-supervised error analysis and integration of Subject Matter Experts feedback within a systematic migration workflow. The methodology achieves significant reductions in Syntax Error Rates, enhances feature alignment throughout migration iterations, and leverages dataset sampling to ensure continual improvement. By embedding GAI into the migration process, the framework facilitates precise feature mapping, semi-automated error resolution, and data-driven optimisation loops, improving workflow efficiency. △ Less

日期/说明：Submitted 5 February, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 16 pages, 27 figures, 7 references | MSC Class: 68T07 (Primary); 03G99 (Secondary) ACM Class: D.2; F.3; I.2

### arXiv:2512.13821 The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces

https://arxiv.org/abs/2512.13821

题摘原始内容：

Large language models (LLMs) increasingly generate code with minimal human oversight, raising critical concerns about backdoor injection and malicious behavior. We present Cross-Trace Verification Protocol (CTVP), a novel AI control framework that verifies untrusted code-generating models through semantic orbit analysis. Rather than directly executing potentially malicious code, CTVP leverages the model's own predictions of execution traces across semantically equivalent program transformations. By analyzing consistency patterns in these predicted traces, we detect behavioral anomalies indicative of backdoors. Our approach introduces the Adversarial Robustness Quotient (ARQ), which quantifies the computational cost of verification relative to baseline generation, demonstrating exponential growth with orbit size. Theoretical analysis establishes information-theoretic bounds showing non-gamifiability - adversaries cannot improve through training due to fundamental space complexity constraints. This work demonstrates that semantic orbit analysis provides a theoretically grounded approach to AI control for code generation tasks, though practical deployment requires addressing the high false positive rates observed in initial evaluations. △ Less

日期/说明：Submitted 5 February, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 13 Pages, A Preprint

### arXiv:2512.13047 Sharpen the Spec, Cut the Code: A Case for Generative File System with SYSSPEC

https://arxiv.org/abs/2512.13047

题摘原始内容：

File systems are critical OS components that require constant evolution to support new hardware and emerging application needs. However, the traditional paradigm of developing features, fixing bugs, and maintaining the system incurs significant overhead, especially as systems grow in complexity. This paper proposes a new paradigm, generative file systems, which leverages Large Language Models (LLMs) to generate and evolve a file system from prompts, effectively addressing the need for robust evolution. Despite the widespread success of LLMs in code generation, attempts to create a functional file system have thus far been unsuccessful, mainly due to the ambiguity of natural language prompts. This paper introduces SYSSPEC, a framework for developing generative file systems. Its key insight is to replace ambiguous natural language with principles adapted from formal methods. Instead of imprecise prompts, SYSSPEC employs a multi-part specification that accurately describes a file system's functionality, modularity, and concurrency. The specification acts as an unambiguous blueprint, guiding LLMs to generate expected code flexibly. To manage evolution, we develop a DAG-structured patch that operates on the specification itself, enabling new features to be added without violating existing invariants. Moreover, the SYSSPEC toolchain features a set of LLM-based agents with mechanisms to mitigate hallucination during construction and evolution. We demonstrate our approach by generating SPECFS, a concurrent file system. SPECFS demonstrates equivalent level of correctness to that of a manually-coded baseline across hundreds of regression tests. We further confirm its evolvability by seamlessly integrating 10 real-world features from Ext4. Our work shows that a specification-guided approach makes generating and evolving complex systems not only feasible but also highly effective. △ Less

日期/说明：Submitted 9 February, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13352 On the Effectiveness of Membership Inference in Targeted Data Extraction from Large Language Models

https://arxiv.org/abs/2512.13352

题摘原始内容：

Large Language Models (LLMs) are prone to memorizing training data, which poses serious privacy risks. Two of the most prominent concerns are training data extraction and Membership Inference Attacks (MIAs). Prior research has shown that these threats are interconnected: adversaries can extract training data from an LLM by querying the model to generate a large volume of text and subsequently applying MIAs to verify whether a particular data point was included in the training set. In this study, we integrate multiple MIA techniques into the data extraction pipeline to systematically benchmark their effectiveness. We then compare their performance in this integrated setting against results from conventional MIA benchmarks, allowing us to evaluate their practical utility in real-world extraction scenarios. △ Less

日期/说明：Submitted 26 February, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: This work has been accepted for publication at the IEEE Conference on Secure and Trustworthy Machine Learning (SaTML). The final version will be available on IEEE Xplore

### arXiv:2512.13043 GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training

https://arxiv.org/abs/2512.13043

题摘原始内容：

Multi-turn reinforcement learning (RL) for multi-modal agents built upon vision- language models (VLMs) is hampered by sparse rewards and long-horizon credit assignment. Recent methods densify the reward by querying a teacher that provides step-level feedback, e.g., Guided Thought Reinforcement (GTR) and On-Policy Distillation, but rely on costly, often privileged models as the teacher, limiting practicality and reproducibility. We introduce GTR-Turbo, a highly efficient upgrade to GTR that matches its performance without training on or querying an expensive teacher model. Specifically, GTR-Turbo merges the weights of checkpoints produced during ongoing RL training and then uses the resulting merged model as a "free" teacher to guide subsequent RL via supervised fine-tuning or soft logit distillation. This design removes dependence on privileged VLMs (e.g., GPT or Gemini), mitigates the "entropy collapse" observed in prior work, and maintains stable training. Across diverse visual agentic tasks, GTR-Turbo improves the accuracy of the baseline model by 10-30% while reducing wall-clock training time by 50% and compute cost by 60% relative to GTR. △ Less

日期/说明：Submitted 11 March, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted by CVPR 2026

### arXiv:2512.13285 CausalCLIP: Causally-Informed Feature Disentanglement and Filtering for Generalizable Detection of Generated Images

https://arxiv.org/abs/2512.13285

题摘原始内容：

The rapid advancement of generative models has increased the demand for generated image detectors capable of generalizing across diverse and evolving generation techniques. However, existing methods, including those leveraging pre-trained vision- language models , often produce highly entangled representations, mixing task-relevant forensic cues (causal features) with spurious or irrelevant patterns (non-causal features), thus limiting generalization. To address this issue, we propose CausalCLIP, a framework that explicitly disentangles causal from non-causal features and employs targeted filtering guided by causal inference principles to retain only the most transferable and discriminative forensic cues. By modeling the generation process with a structural causal model and enforcing statistical independence through Gumbel-Softmax-based feature masking and Hilbert-Schmidt Independence Criterion (HSIC) constraints, CausalCLIP isolates stable causal features robust to distribution shifts. When tested on unseen generative models from different series, CausalCLIP demonstrates strong generalization ability, achieving improvements of 6.83% in accuracy and 4.06% in average precision over state-of-the-art methods. △ Less

日期/说明：Submitted 22 March, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 9 pages,Accepted to AAAI 2026

### arXiv:2512.14080 SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations

https://arxiv.org/abs/2512.14080

题摘原始内容：

Mixture of Experts (MoE) models have emerged as the de facto architecture for scaling up language models without significantly increasing the computational cost. Recent MoE models demonstrate a clear trend towards high expert granularity (smaller expert intermediate dimension) and higher sparsity (constant number of activated experts with a higher number of total experts), which improve model quality per FLOP. However, fine-grained MoEs suffer from increased activation memory footprint and reduced hardware efficiency due to higher IO costs, while sparser MoEs suffer from wasted computations due to padding in Grouped GEMM kernels. In response, we propose a memory-efficient algorithm to compute the forward and backward passes of MoEs with minimal activation caching for the backward pass. We also design GPU kernels that overlap memory IO with computation, benefiting all MoE architectures. Finally, we propose a novel "token rounding" method that minimizes the wasted compute due to padding in Grouped GEMM kernels. As a result, our method SonicMoE reduces activation memory by 45% and achieves a 1.86x compute throughput improvement on Hopper GPUs compared to ScatterMoE's BF16 MoE kernel for a fine-grained 7B MoE. Concretely, SonicMoE on 64 H100s achieves a training throughput of 213 billion tokens per day, comparable to ScatterMoE's 225 billion tokens per day on 96 H100s for a 7B MoE model training with FSDP-2 using the lm-engine codebase. On Blackwell GPUs, SonicMoE also achieves a 25% and 15% relative speedup on the forward and backward pass respectively compared to a highly optimized DeepGEMM baseline on OLMoE-sized 7B MoE models. Under high MoE sparsity settings, our tile-aware token rounding algorithm yields an additional 1.16x speedup on kernel execution time compared to vanilla top-K routing while maintaining similar downstream performance on Hopper GPUs. We open-source all our kernels. △ Less

日期/说明：Submitted 26 March, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Include the new Blackwell benchmark results

### arXiv:2512.13953 From Unlearning to UNBRANDING: A Benchmark for Trademark-Safe Text-to-Image Generation

https://arxiv.org/abs/2512.13953

题摘原始内容：

The rapid progress of text-to-image diffusion models raises significant concerns regarding the unauthorized reproduction of trademarked content. While prior work targets general concepts (e.g., styles, celebrities), it fails to address specific brand identifiers. Brand recognition is multi-dimensional, extending beyond explicit logos to encompass distinctive structural features (e.g., a car's front grille). To tackle this, we introduce unbranding, a novel task for the fine-grained removal of both trademarks and subtle structural brand features, while preserving semantic coherence. We construct a benchmark dataset and introduce a novel evaluation framework combining Vision Language Models (VLMs) with segmentation-based classifiers trained on human annotations of logos and trade dress features, addressing the limitations of existing brand detectors that fail to capture abstract trade dress. Furthermore, we observe that newer, higher-fidelity systems (SDXL, FLUX) synthesize brand identifiers more readily than older models, highlighting the urgency of this challenge. Our results confirm that unbranding is a distinct problem requiring specialized techniques. Project Page: https://gmum.github.io/UNBRANDING/. △ Less

日期/说明：Submitted 30 March, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13040 Understanding Structured Financial Data with LLMs: A Case Study on Fraud Detection

https://arxiv.org/abs/2512.13040

题摘原始内容：

Detecting fraud in financial transactions typically relies on tabular models that demand heavy feature engineering to handle high-dimensional data and offer limited interpretability, making it difficult for humans to understand predictions. Large Language Models (LLMs), in contrast, can produce human-readable explanations and facilitate feature analysis, potentially reducing the manual workload of fraud analysts and informing system refinements. However, they perform poorly when applied directly to tabular fraud detection due to the difficulty of reasoning over many features, the extreme class imbalance, and the absence of contextual information. To bridge this gap, we introduce FinFRE-RAG, a two-stage approach that applies importance-guided feature reduction to serialize a compact subset of numeric/categorical attributes into natural language and performs retrieval-augmented in-context learning over label-aware, instance-level exemplars. Across four public fraud datasets and three families of open-weight LLMs, FinFRE-RAG substantially improves F1/MCC over direct prompting and is competitive with strong tabular baselines in several settings. Although these LLMs still lag behind specialized classifiers, they narrow the performance gap and provide interpretable rationales, highlighting their value as assistive tools in fraud analysis. △ Less

日期/说明：Submitted 8 April, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted to ACL 2026 Main Conference

### arXiv:2512.13961 Olmo 3

https://arxiv.org/abs/2512.13961

题摘原始内容：

We introduce Olmo 3, a family of state-of-the-art, fully-open language models at the 7B and 32B parameter scales. Olmo 3 model construction targets long-context reasoning, function calling, coding, instruction following, general chat, and knowledge recall. This release includes the entire model flow, i.e., the full lifecycle of the family of models, including every stage, checkpoint, data point, and dependency used to build it. Our flagship model, Olmo 3 Think 32B, is the strongest fully-open thinking model released to-date. △ Less

日期/说明：Submitted 14 April, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: minor edit updates

### arXiv:2512.13671 AgentIAD: Agentic Industrial Anomaly Detection via Adaptive Memory Augmentation

https://arxiv.org/abs/2512.13671

题摘原始内容：

Industrial anomaly detection (IAD) is challenging due to the subtle and highly localized nature of many defects, which single-pass vision-- language models (VLMs) often fail to capture. Moreover, existing approaches lack mechanisms to actively acquire complementary evidence during inference. We propose AgentIAD, an agentic vision--language framework that enables iterative industrial inspection through a unified action space. The agent dynamically accesses two forms of memory during inspection: visual memory via the Perceptive Zoomer (PZ) for fine-grained local analysis, and retrieved memory via the Web Searcher (WS) and Comparative Retriever (CR) for external knowledge acquisition and cross-instance verification. This design allows the model to progressively gather evidence through multi-round perception--action reasoning. To effectively learn such policies under sparse supervision, AgentIAD adopts a two-stage training strategy: tool-aware supervised fine-tuning first initializes structured reasoning and memory-access behaviors, followed by agentic reinforcement learning to refine long-horizon decision policies. Extensive experiments show that, under the same backbone, AgentIAD improves classification accuracy by 5.92% over the previous state-of-the-art method on the MMAD benchmark while providing more reliable and interpretable anomaly analysis. △ Less

日期/说明：Submitted 14 April, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14067 Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed

https://arxiv.org/abs/2512.14067

题摘原始内容：

Diffusion language models (dLMs) have emerged as a promising paradigm that enables parallel, non-autoregressive generation, but their learning efficiency lags behind that of autoregressive (AR) language models when trained from scratch. To this end, we study AR-to-dLM conversion to transform pretrained AR models into efficient dLMs that excel in speed while preserving AR models' task accuracy. We achieve this by identifying limitations in the attention patterns and objectives of existing AR-to-dLM methods and then proposing principles and methodologies for more effective AR-to-dLM conversion. Specifically, we first systematically compare different attention patterns and find that maintaining pretrained AR weight distributions is critical for effective AR-to-dLM conversion. As such, we introduce a continuous pretraining scheme with a block-wise attention pattern, which remains causal across blocks while enabling bidirectional modeling within each block. We find that this approach can better preserve pretrained AR models' weight distributions than fully bidirectional modeling, in addition to its known benefit of enabling KV caching, and leads to a win-win in accuracy and efficiency. Second, to mitigate the training-test gap in mask token distributions (uniform vs. highly left-to-right), we propose a position-dependent token masking strategy that assigns higher masking probabilities to later tokens during training to better mimic test-time behavior. Leveraging this framework, we conduct extensive studies of dLMs' attention patterns, training dynamics, and other design choices, providing actionable insights into scalable AR-to-dLM conversion. These studies lead to the Efficient-DLM family, which outperforms state-of-the-art AR models and dLMs, e.g., our Efficient-DLM 8B achieves +5.4%/+2.7% higher accuracy with 4.5x/2.7x higher throughput compared to Dream 7B and Qwen3 4B, respectively. △ Less

日期/说明：Submitted 29 April, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14044 OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving

https://arxiv.org/abs/2512.14044

题摘原始内容：

The deployment of Vision- Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning. While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels. Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%. △ Less

日期/说明：Submitted 30 April, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.14018 PerfCoder: Large Language Models for Interpretable Code Performance Optimization

https://arxiv.org/abs/2512.14018

题摘原始内容：

Large language models (LLMs) have achieved remarkable progress in automatic code generation, yet their ability to produce high-performance code remains limited--a critical requirement in real-world software systems. We argue that current LLMs struggle not only due to data scarcity but, more importantly, because they lack supervision that guides interpretable and effective performance improvements. In this work, we introduce PerfCoder, a family of LLMs specifically designed to generate performance-enhanced code from source code via interpretable, customized optimizations. PerfCoder is fine-tuned on a curated collection of real-world optimization trajectories with human-readable annotations, and preference-aligned by reinforcement fine-tuning using runtime measurements, enabling it to propose input-specific improvement strategies and apply them directly without relying on iterative refinement. On the PIE code performance benchmark, PerfCoder surpasses all existing models in both runtime speedup and effective optimization rate, demonstrating that performance optimization cannot be achieved by scale alone but requires optimization stratetgy awareness. In addition, PerfCoder can generate interpretable feedback about the source code, which, when provided as input to a larger LLM in a planner-and-optimizer cooperative workflow, can further improve outcomes. Specifically, we elevate the performance of 32B models and GPT-5 to new levels on code optimization, substantially surpassing their original performance. △ Less

日期/说明：Submitted 8 May, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13751 MIDUS: Memory-Infused Depth Up-Scaling

https://arxiv.org/abs/2512.13751

题摘原始内容：

Expanding pre-trained language models offers a practical way to increase capacity without training larger models from scratch. Depth Up-Scaling (DUS) does so by duplicating Transformer blocks and inserting them into a pre-trained backbone. This process also duplicates FFN-heavy blocks, increasing parameter and compute cost while adding capacity through a block-level dense residual branch. Yet prior work suggests that added capacity need not remain tied to dense FFN branches, while attention heads often play heterogeneous roles, motivating more efficient head-level residual corrections. We propose Memory-Infused Depth Up-Scaling (MIDUS), which replaces the duplicated FFN branches with memory layers and turns added depth into lightweight retrieval-based residual capacity. We introduce a Head-wise Memory Layer (HML), which combines multi-head product-key memory with Head-wise Implicit Value Expansion (HIVE). HML assigns each head a distinct key space, while HIVE realizes head-specific values from a shared latent bank through compact projections. Alongside empirical improvements in performance and efficiency, our head-importance and fixed-retrieval structural analyses characterize HML with HIVE as a structurally distinct, head-conditioned alternative to FFN-based residual expansion. △ Less

日期/说明：Submitted 9 May, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13618 Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models

https://arxiv.org/abs/2512.13618

题摘原始内容：

Representing continuous time is a critical and under-explored challenge in modeling temporal event sequences with large language models (LLMs). Various strategies like byte-level representations or calendar tokens have been proposed. However, the optimal approach remains unclear, especially given the diverse statistical distributions of real-world event data, which range from smooth log-normal to discrete, spiky patterns. This paper presents a systematic empirical study of temporal tokenization for modeling event sequences with LLMs, comparing distinct encoding strategies: naive numeric strings, high-precision byte-level representations, human-semantic calendar tokens, classic uniform binning, and adaptive residual scalar quantization. We evaluate these strategies by fine-tuning LLMs on real-world datasets that exemplify these diverse distributions. Our analysis reveals that no single strategy is universally superior; instead, prediction performance depends heavily on aligning the tokenizer with the data's statistical properties, highlighting temporal tokenization as a critical yet often overlooked design dimension in LLM-based event modeling. △ Less

日期/说明：Submitted 11 May, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13609 Do-Undo Bench: Reversibility for Action Understanding in Image Generation

https://arxiv.org/abs/2512.13609

题摘原始内容：

We introduce the Do-Undo task and benchmark to address a critical gap in vision- language models : understanding and generating plausible scene transformations driven by real-world actions. Unlike prior work that relies on prompt-based image generation and editing to perform action-conditioned image manipulation, our training hypothesis requires models to simulate the outcome of a real-world action and then reverse it to the original state. This forward-reverse requirement tests genuine cause-and-effect understanding rather than stylistic or semantic edits. We curate a high-quality benchmark of reversible actions from real-world scenarios to enable robust action grounding. Our experiments reveal that current models struggle with action reversibility, highlighting the need to evaluate action understanding. Do-Undo provides an intuitive testbed for evaluating and advancing action-aware generation in multimodal systems that must reason about real-world dynamics. △ Less

日期/说明：Submitted 14 May, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Project page: https://s-mahajan.github.io/Do-Undo-Bench/

### arXiv:2512.15791 Evaluation of AI Ethics Tools in Language Models: A Developers' Perspective Case Study

https://arxiv.org/abs/2512.15791

题摘原始内容：

In Artificial Intelligence (AI), language models have gained significant importance due to the widespread adoption of systems capable of simulating realistic conversations with humans through text generation. Because of their impact on society, developing and deploying these language models must be done responsibly, with attention to their negative impacts and possible harms. In this scenario, the number of AI Ethics Tools (AIETs) publications has recently increased. These AIETs are designed to help developers, companies, governments, and other stakeholders establish trust, transparency, and responsibility with their technologies by bringing accepted values to guide AI's design, development, and use stages. However, many AIETs lack good documentation, examples of use, and proof of their effectiveness in practice. This paper presents a methodology for evaluating AIETs in language models . Our approach involved an extensive literature survey on 213 AIETs, and after applying inclusion and exclusion criteria, we selected four AIETs: Model Cards, ALTAI, FactSheets, and Harms Modeling. For evaluation, we applied AIETs to language models developed for the Portuguese language, conducting 35 hours of interviews with their developers. The evaluation considered the developers' perspective on the AIETs' use and quality in helping to identify ethical considerations about their model. The results suggest that the applied AIETs serve as a guide for formulating general ethical considerations about language models . However, we note that they do not address unique aspects of these models, such as idiomatic expressions. Additionally, these AIETs did not help to identify potential negative impacts of models for the Portuguese language. △ Less

日期/说明：Submitted 26 May, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 7 figures, 11 tables. Accepted for publication in AI and Ethics

### arXiv:2602.22221 Evaluating Reliability Asymmetries in Chinese Factual Search and AI Answers

https://arxiv.org/abs/2602.22221

题摘原始内容：

Search engines and AI-powered systems increasingly mediate access to factual information, yet their reliability remains difficult to evaluate in realistic information-seeking settings. We study this problem in the Chinese web ecosystem by constructing a query-based fact-checking dataset from real Chinese search logs and comparing nine systems across traditional search engines, standalone large language models , and search-integrated AI Overviews. Focusing on factual Chinese-language factual Yes/No questions, we evaluate whether systems provide correct, incorrect, or uncertain decisions against evidence-derived ground truth. We find that systems are similarly accurate when they provide definitive answers, but differ sharply in how often they do so. Conditional accuracy ranges from 73.2% to 78.9%, yet search engines answer definitively on over 83% of queries, while Qwen-Max does so on fewer than half. We also find a consistent polarity gap: all systems perform better on yes-labeled queries than on no-labeled queries. We also use Baidu Index data to identify Chinese provinces with higher health-related search attention, which may indicate greater potential exposure to misinformation. Overall, our results show that reliability depends not only on whether systems are correct when they answer, but also on how often they answer, how they handle negative claims, and where information demand may increase exposure risks. △ Less

日期/说明：Submitted 28 May, 2026; v1 submitted 15 December, 2025; originally announced February 2026.

### arXiv:2512.13996 DTop-p MoE: Sparsity-Controlled Dynamic Top-p MoE for Foundation Model Pre-training

https://arxiv.org/abs/2512.13996

题摘原始内容：

Sparse Mixture-of-Experts architectures are essential for scaling model capacity efficiently, yet the standard Top-$k$ routing imposes a rigid sparsity pattern that ignores the intrinsic variance in token difficulty and layer-specific computational needs. Top-$p$ routing is more adaptive because it selects experts until their cumulative routing probability reaches a threshold, allowing confident tokens to use fewer experts and ambiguous tokens to recruit more. However, we demonstrate that existing naive Top-$p$ implementations with fixed global probability thresholds provide only marginal gains over Top-$k$, suffer from hyperparameter sensitivity, and result in uncontrolled computational costs. In this paper, we propose **DTop-$p$**, a sparsity-controllable dynamic routing mechanism that learns the Top-$p$ probability threshold with a Proportional-Integral controller and uses dynamic routing normalization to support layer-wise expert selection under a global sparsity constraint. Extensive experiments on Large Language Models and Diffusion Transformers demonstrate that **DTop-$p$** consistently outperforms both Top-$k$ and fixed Top-$p$ baselines while matching the average FLOPs of Top-$k$ MoE. Our analysis confirms that **DTop-$p$** exhibits strong scaling properties across expert granularity, total expert capacity, model size, and dataset size, offering a robust and efficient MoE framework for foundation model pre-training. △ Less

日期/说明：Submitted 1 June, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13278 AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning

https://arxiv.org/abs/2512.13278

题摘原始内容：

Agentic reinforcement learning has advanced large language models (LLMs) to reason through long chain-of-thought trajectories while interleaving external tool use. Existing approaches assume a fixed inventory of tools, which limits the adaptability of LLM agents to new or evolving toolsets. We present AutoTool, a training framework that equips LLM agents with dynamic tool-selection capabilities throughout their reasoning trajectories. AutoTool employs a dual-phase optimization pipeline: (i) SFT and RL-based trajectory stabilization for coherent reasoning, and (ii) KL-regularized Plackett-Luce Ranking to refine consistent multi-step tool selection. We further build a 200k dataset with explicit tool-selection rationales across 1,000+ tools and 100+ tasks spanning mathematics, science, code generation, and multimodal reasoning. Across ten diverse benchmarks, we train two base models, Qwen3-8B and Qwen2.5-VL-7B, with AutoTool. With fewer parameters, AutoTool consistently outperforms advanced LLM agents and tool-integration methods, yielding average gains of 6.4% in math & science reasoning, 4.5% in search-based QA, 7.7% in code generation, and 6.9% in multimodal understanding. In addition, AutoTool exhibits stronger generalization by dynamically leveraging unseen tools from evolving toolsets during inference. △ Less

日期/说明：Submitted 4 June, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: ICML2026; Best Paper Award at ICCV 2025 Workshop on Multi-Modal Reasoning for Agentic Intelligence

### arXiv:2512.13830 Practitioner Insights on Fairness Requirements in the AI Development Life Cycle: An Interview Study

https://arxiv.org/abs/2512.13830

题摘原始内容：

Nowadays, Artificial Intelligence (AI), particularly Machine Learning (ML) and Large Language Models (LLMs), is widely applied across various contexts. However, the corresponding models often operate as black boxes, leading them to unintentionally act unfairly towards different demographic groups. This has led to a growing focus on fairness in AI software recently, alongside the traditional focus on the effectiveness of AI models. Through 26 semi-structured interviews with practitioners from different application domains and with varied backgrounds across 23 countries, we conducted research on fairness requirements in AI from software engineering perspective. Our study assesses the participants' awareness of fairness in AI / ML software and its application within the Software Development Life Cycle (SDLC), from translating fairness concerns into requirements to assessing their arising early in the SDLC. It also examines fairness through the key assessment dimensions of implementation, validation, evaluation, and how it is balanced with trade-offs involving other priorities, such as addressing all the software functionalities and meeting critical delivery deadlines. Findings of our thematic qualitative analysis show that while our participants recognize the aforementioned AI fairness dimensions, practices are inconsistent, and fairness is often deprioritized with noticeable knowledge gaps. This highlights the need for agreement with relevant stakeholders on well-defined, contextually appropriate fairness definitions, the corresponding evaluation metrics, and formalized processes to better integrate fairness into AI/ML projects. △ Less

日期/说明：Submitted 8 June, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13090 Multi-Robot Motion Planning from Vision and Language using Heat-Inspired Diffusion

https://arxiv.org/abs/2512.13090

题摘原始内容：

Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-conditioned Heat-inspired Diffusion (LHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LHD integrates semantic priors from CLIP, a vision- language model (VLM), with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution (OOD) scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency. Project page is available at: https://jebeom.github.io/lhd_project_page/ △ Less

日期/说明：Submitted 15 June, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 8 pages, 6 figures, accepted by IEEE Robotics and Automation Letters (RA-L) | Journal ref: IEEE Robotics and Automation Letters, vol. 11, no. 6, pp. 7118-7125, June 2026

### arXiv:2512.15792 A Multifaceted Analysis of Social Biases in Large Language Models

https://arxiv.org/abs/2512.15792

题摘原始内容：

Large language models (LLMs) have rapidly become indispensable tools for acquiring information and supporting human decision-making. However, ensuring that these models uphold fairness across varied contexts is critical to their safe and responsible deployment. In this study, we undertake a comprehensive examination of four widely adopted LLMs, probing their underlying biases and inclinations across the dimensions of politics, ideology, alliance, language, and gender. Through a series of carefully designed experiments, we investigate their political neutrality using news summarization, ideological biases through news stance classification, tendencies toward specific geopolitical alliances via United Nations voting patterns, language bias in the context of multilingual story completion, and gender-related affinities as revealed by responses to the World Values Survey. Results indicate that while the LLMs are aligned to be neutral and impartial, they still show biases and affinities of different types. △ Less

日期/说明：Submitted 16 June, 2026; v1 submitted 15 December, 2025; originally announced December 2025.

### arXiv:2512.13491 From Zipf's Law to Neural Scaling through Heaps' Law and Hilberg's Hypothesis

https://arxiv.org/abs/2512.13491

题摘原始内容：

We inspect the deductive connection between the neural scaling law and Zipf's law -- two statements discussed in machine learning and quantitative linguistics. The neural scaling law describes how the cross entropy rate of a foundation model -- such as a large language model -- changes with respect to the amount of training tokens, parameters, and compute. By contrast, Zipf's law posits that the distribution of tokens exhibits a power law tail. Whereas similar claims have been made in more specific settings, we show that the neural scaling law is a consequence of Zipf's law under certain broad assumptions that we reveal systematically. The derivation steps are as follows: We derive Heaps' law on the vocabulary growth from Zipf's law, Hilberg's hypothesis on the entropy scaling from Heaps' law, and the neural scaling from Hilberg's hypothesis. We illustrate these inference steps by a toy example of the Santa Fe process that satisfies all four statistical laws. △ Less

日期/说明：Submitted 22 June, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 32 pages, no figures | MSC Class: 94A17 (Primary) 60G10; 91F20; 68T07 (Secondary) | Journal ref: Journal of Machine Learning Research, vol. 27, no. 194, pp. 1-35, 2026

### arXiv:2512.13636 MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning

https://arxiv.org/abs/2512.13636

题摘原始内容：

Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving. △ Less

日期/说明：Submitted 17 July, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted by ECCV 2026; Project Page: https://xiaomi-mlab.github.io/MindDrive/

### arXiv:2512.15783 Towards AI epidemiology: a measurement standardisation framework for prospective risk detection

https://arxiv.org/abs/2512.15783

题摘原始内容：

This paper proposes a measurement standardisation framework that compresses expert-AI interactions into structured, comparable fields for prospective risk detection in deployed AI systems, without access to model internals. This concept paper defines the framework's scope, semantically and statistically, and specifies a protocol for its empirical testing. The population-level claims it is designed to support therefore belong to a staged research programme rather than to results claimed here. Measurement standardisation underpins three claims. The first is a reliability claim: under bounded conditions, large language models can produce reliable, standardised assessments of the evidential and policy alignment of expert-AI interactions. The second is a governance claim: alignment scores give experts an immediate signal during deployment and give institutions a basis for monitoring alignment patterns across mission types, models, and domains. The third is an outcome validation claim: once measurement standardisation is established, aggregate alignment scores could be used to study associations with downstream outcomes in regulated professional settings. This introduces the possibility of an "AI epidemiology", a form of risk detection based on correlated variables instead of mechanistic analysis, inspired by epidemiological reasoning. A minimal application of the protocol to a published expert-AI corpus shows that the judge reproduces its policy and evidential alignment scores across two runs under the specified conditions. Judge reliability at scale remains to be validated in future work. The paper sets out a defined grammar of eight interaction fields, together with a statistical protocol based on paired bootstrap inference, DeLong's test for paired AUCs as a sensitivity check, a pre-specified one-sided non-inferiority margin of 0.05, and Holm-Bonferroni correction. △ Less

日期/说明：Submitted 20 July, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: 38 pages, 3 figures, 4 tables. Accepted for publication in AI & Society | Journal ref: AI & Society (2026)

### arXiv:2512.13374 Behavior and Representation in Open-Weight Large Language Models for Combinatorial Optimization: From Feature Extraction to Algorithm Selection

https://arxiv.org/abs/2512.13374

题摘原始内容：

Recent advances in Large Language Models (LLMs) open new perspectives for automation in optimization, yet little is known about whether their internal representations capture problem structure or algorithmic behavior. We investigate whether representations learned by frozen, open-weight LLMs for combinatorial optimization instances can support downstream decision tasks. The goal is not to replace exact feature extractors or to propose a new algorithm, but to assess whether such representations are reusable for feature recovery and algorithm selection. Our methodology combines direct querying, which tests explicit feature extraction, with probing analyses of whether this information is implicitly encoded in the hidden layers. The probing framework is further extended to a per-instance algorithm selection task. Experiments span four benchmark problems, three instance representations, and five open-weight models from 3B to 120B parameters across the Llama instruct and GPT reasoning families, including a chain-of-thought study on Llama models. Results show a limited ability to recover features explicitly, particularly those requiring structured computation, while part of this information remains implicitly encoded in the hidden states. A consistent gap separates implicit encoding from explicit retrieval. Model scale attenuates this gap, whereas the effect of chain-of-thought prompting depends strongly on model size, and in all cases the gap remains open. Reasoning-oriented models also tend to abstain more when reliable computation is not possible. Notably, the predictive power of LLM hidden-layer representations is comparable to traditional feature extraction across all five models, indicating they can act as effective surrogate descriptors for downstream optimization tasks. △ Less

日期/说明：Submitted 12 August, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted for publication in Computers & Operations Research. Code and data are available on Zenodo: https://doi.org/10.5281/zenodo.21891840

### arXiv:2512.13325 Security and Detectability Analysis of Unicode Text Watermarking Methods against Large Language Models

https://arxiv.org/abs/2512.13325

题摘原始内容：

Securing digital text is becoming increasingly relevant due to the widespread use of large language models . Individuals' fear of losing control over data when it is being used to train such machine learning models or when distinguishing model-generated output from text written by humans. Digital watermarking provides additional protection by embedding an invisible watermark within the data that requires protection. However, little work has been taken to analyze and verify if existing digital text watermarking methods are secure and undetectable by large language models . In this paper, we investigate the security-related area of watermarking and machine learning models for text data. In a controlled testbed of three experiments, ten existing Unicode text watermarking methods were implemented and analyzed across six large language models : GPT-5, GPT-4o, Teuken 7B, Llama 3.3, Claude Sonnet 4, and Gemini 2.5 Pro. The findings of our experiments indicate that, especially the latest reasoning models, can detect a watermarked text. Nevertheless, all models fail to extract the watermark unless implementation details in the form of source code are provided. We discuss the implications for security researchers and practitioners and outline future research opportunities to address security concerns. △ Less

日期/说明：Submitted 13 August, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Author's version of a paper, accepted and presented at the ICISSP 2026 conference

### arXiv:2512.14069 RADAR: Accelerate Large Language Model Inference With RL-Based Dynamic Draft Trees

https://arxiv.org/abs/2512.14069

题摘原始内容：

Inference with modern Large Language Models (LLMs) is expensive and slow, and speculative sampling has emerged as an effective solution to this problem. However, the number of calls to the draft model for generating candidate tokens in speculative sampling is a preset hyperparameter, lacking flexibility. To generate and utilize the candidate tokens more effectively, we propose RADAR, a novel speculative sampling method with RL-based dynamic draft trees. RADAR formulates the draft tree generation process as a Markov Decision Process (MDP) and employs offline reinforcement learning to train a prediction model, which enables real-time decisions on calls to the draft model, reducing redundant computations and further accelerating inference. Evaluations across three LLMs and four tasks show that RADAR achieves a speedup of 3.17x-4.82x over the auto-regressive decoding baseline. The code is available at https://github.com/minaduki-sora/RADAR. △ Less

日期/说明：Submitted 26 August, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: EMNLP 2026 Findings Paper

### arXiv:2512.13511 Adapting MLLMs for Nuanced Video Retrieval

https://arxiv.org/abs/2512.13511

题摘原始内容：

Our objective is to build an embedding model that captures the nuanced relationship between a search query and candidate videos. We cover three aspects of nuanced retrieval: (i) temporal, (ii) negation, and (iii) multimodal. For temporal nuance, we consider chiral actions that need distinguishing between temporally opposite actions like "opening a door" vs. "closing a door". For negation, we consider queries with negators such as "not", "none" that allow a user to specify what they do not want. For multimodal nuance, we consider the task of composed retrieval where the query comprises a video along with a text edit instruction. The goal is to develop a unified embedding model that handles such nuances effectively. To that end, we repurpose a Multimodal Large Language Model (MLLM) trained to generate text into an embedding model. We fine-tune it with a contrastive loss on text alone with carefully sampled hard negatives that instill the desired nuances in the learned embedding space. Despite the text-only training, our method achieves state of the art performance on all benchmarks for nuanced video retrieval. We also analyze how this improvement is achieved, and show that text-only training reduces the modality gap between text and video embeddings leading to better organization of the embedding space. △ Less

日期/说明：Submitted 4 September, 2026; v1 submitted 15 December, 2025; originally announced December 2025. | Comments: Accepted at ECCV 2026. Project page at https://www.robots.ox.ac.uk/~vgg/research/tara/

停止依据：页面无有效 Next 链接；实际页数=1；原始行数=107
