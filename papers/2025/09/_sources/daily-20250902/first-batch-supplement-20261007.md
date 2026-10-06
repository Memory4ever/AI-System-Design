# Sep02 新增首批准入校准包

作者：Darwin / Codex本会话。记录时间：2026-10-07T20:48:01+08:00。

只处理Sep02补充窗口2025-09-01完整自然日。原小时窗口、旧44家族证据/评分/独立裁决冻结；本包不是DAY或Evidence通过。

## 范围与计数

四组Advanced实际180出现/178唯一月份身份，只作有界发现。本包23个新身份完整题摘实际读：22来自查询，Robix来自Seed，均不在旧44集合。暂拟16P（含1文本重合隔离）、4准入事实待定点U、2代表排除C拟、1撤回；不是20已校准准入。尚未授确定Sep01论文候选、评分或Books采用。旧LongCat单列事件，不增加新身份/题摘数。

搜索显示当前摘要，部分已修订到2025稍后或2026，不能称全部exact-v1/倒灌原事件。下列完整题摘/实际位置保留。请独立检查全部拟保留与U、两代表排除、撤回/文本重合及LongCat新日窗事件；指出决定准入的具体差额，再定点恢复必要v1。

查询/分页停止/普通剩余见[supplement](supplement-20261007.md)。未将月库存全量排队。

## 逐项题摘与准入依据

### 2509.00088 AEGIS : Automated Co-Evolutionary Framework for Guarding Prompt Injections Schema

[官方身份](https://arxiv.org/abs/2509.00088)；原件：[arxiv-agent.html](supplement-20261007/arxiv-agent.html) #1。

当前元信息：Submitted 9 October, 2025; v1 submitted 27 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> Prompt injection attacks pose a significant challenge to the safe deployment of Large Language Models (LLMs) in real-world applications. While prompt-based detection offers a lightweight and interpretable defense strategy, its effectiveness has been hindered by the need for manual prompt engineering. To address this issue, we propose AEGIS , an Automated co-Evolutionary framework for Guarding prompt Injections Schema. Both attack and defense prompts are iteratively optimized against each other using a gradient-like natural language prompt optimization technique. This framework enables both attackers and defenders to autonomously evolve via a Textual Gradient Optimization (TGO) module, leveraging feedback from an LLM-guided evaluation loop. We evaluate our system on a real-world assignment grading dataset of prompt injection attacks and demonstrate that our method consistently outperforms existing baselines, achieving superior robustness in both attack success and detection. Specifically, the attack success rate (ASR) reaches 1.0, representing an improvement of 0.26 over the baseline. For detection, the true positive rate (TPR) improves by 0.23 compared to the previous best work, reaching 0.84, and the true negative rate (TNR) remains comparable at 0.89. Ablation studies confirm the importance of co-evolution, gradient buffering, and multi-objective optimization. We also confirm that this framework is effective in different LLMs. Our results highlight the promise of adversarial training as a scalable and effective approach for guarding prompt injections.

暂拟：P。固定提示防御 → 攻防TGO共同优化、buffer/multi-objective → 核静态防御边界；威胁预算/judge未核，不采用ASR/TPR或安全保证。

条件owner：PLATFORM-SECURITY。仅ROADMAP路由，未作具体Books比较。

### 2509.00366 KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation

[官方身份](https://arxiv.org/abs/2509.00366)；原件：[arxiv-agent.html](supplement-20261007/arxiv-agent.html) #2。

当前元信息：Submitted 30 August, 2025; originally announced September 2025. Comments: Accepted by the EMNLP 2025

完整摘要（实际读；作者原文，不作为成立证据）：

> Despite recent progress, Graphic User Interface (GUI) agents powered by Large Language Models (LLMs) struggle with complex mobile tasks due to limited app-specific knowledge. While UI Transition Graphs (UTGs) offer structured navigation representations, they are underutilized due to poor extraction and inefficient integration. We introduce KG-RAG, a Knowledge Graph-driven Retrieval-Augmented Generation framework that transforms fragmented UTGs into structured vector databases for efficient real-time retrieval. By leveraging an intent-guided LLM search method, KG-RAG generates actionable navigation paths, enhancing agent decision-making. Experiments across diverse mobile apps show that KG-RAG outperforms existing methods, achieving a 75.8% success rate (8.9% improvement over AutoDroid), 84.6% decision accuracy (8.1% improvement), and reducing average task steps from 4.5 to 4.1. Additionally, we present KG-Android-Bench and KG-Harmony-Bench, two benchmarks tailored to the Chinese mobile ecosystem for future research. Finally, KG-RAG transfers to web/desktop (+40% SR on Weibo-web; +20% on QQ Music-desktop), and a UTG cost ablation shows accuracy saturates at ~4h per complex app, enabling practical deployment trade-offs.

暂拟：P。碎片UTG → 图检索/导航路径和构造成本消融 → 核建图何时抵消动作收益，不采用成功率。

条件owner：AGENT-RAG。仅ROADMAP路由，未作具体Books比较。

### 2509.00449 GOSU: Retrieval-Augmented Generation with Global-Level Optimized Semantic Unit-Centric Framework

[官方身份](https://arxiv.org/abs/2509.00449)；原件：[arxiv-agent.html](supplement-20261007/arxiv-agent.html) #3。

当前元信息：Submitted 30 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> Building upon the standard graph-based Retrieval-Augmented Generation (RAG), the introduction of heterogeneous graphs and hypergraphs aims to enrich retrieval and generation by leveraging the relationships between multiple entities through the concept of semantic units (SUs). But this also raises a key issue: The extraction of high-level SUs limited to local text chunks is prone to ambiguity, complex coupling, and increased retrieval overhead due to the lack of global knowledge or the neglect of fine-grained relationships. To address these issues, we propose GOSU, a semantic unit-centric RAG framework that efficiently performs global disambiguation and utilizes SUs to capture interconnections between different nodes across the global context. In the graph construction phase, GOSU performs global merging on the pre-extracted SUs from local text chunks and guides entity and relationship extraction, reducing the difficulty of coreference resolution while uncovering global semantic objects across text chunks. In the retrieval and generation phase, we introduce hierarchical keyword extraction and semantic unit completion. The former uncovers the fine-grained binary relationships overlooked by the latter, while the latter compensates for the coarse-grained n-ary relationships missing from the former. Evaluation across multiple tasks demonstrates that GOSU outperforms the baseline RAG methods in terms of generation quality.

暂拟：P。局部SU跨块歧义 → 全局merge及binary/n-ary互补 → 核索引成本与coreference/检索质量取舍。

条件owner：AGENT-RAG。仅ROADMAP路由，未作具体Books比较。

### 2509.01030 Identifying Origins of Place Names via Retrieval Augmented Generation

[官方身份](https://arxiv.org/abs/2509.01030)；原件：[arxiv-agent.html](supplement-20261007/arxiv-agent.html) #4。

当前元信息：Submitted 3 September, 2025; v1 submitted 31 August, 2025; originally announced September 2025. Journal ref: Geography According to Foundation Models. SAGE Publications; 2026:76-92

完整摘要（实际读；作者原文，不作为成立证据）：

> Who is the "Batman" behind "Batman Street" in Melbourne? Understanding the historical, cultural, and societal narratives behind place names can reveal the rich context that has shaped a community. Although place names serve as essential spatial references in gazetteers, they often lack information about place name origins. Enriching these place names in today's gazetteers is a time-consuming, manual process that requires extensive exploration of a vast archive of documents and text sources. Recent advances in natural language processing and language models (LMs) hold the promise of significant automation of identifying place name origins due to their powerful capability to exploit the semantics of the stored documents. This chapter presents a retrieval augmented generation pipeline designed to search for place name origins over a broad knowledge base, DBpedia. Given a spatial query, our approach first extracts sub-graphs that may contain knowledge relevant to the query; then ranks the extracted sub-graphs to generate the final answer to the query using fine-tuned LM-based models (i.e., ColBERTv2 and Llama2). Our results highlight the key challenges facing automated retrieval of place name origins, especially the tendency of language models to under-use the spatial information contained in texts as a discriminating factor. Our approach also frames the wider implications for geographic information retrieval using retrieval augmented generation.

暂拟：U。领域RAG组合不够，但摘要明确LM under-use spatial information；定点核可复用检索/grounding盲区还是应用现象，不因地理标签关闭。

条件owner：AGENT-RAG。仅ROADMAP路由，未作具体Books比较。

### 2509.01088 Privacy-Preserving Reasoning with Knowledge-Distilled Parametric Retrieval Augmented Generation

[官方身份](https://arxiv.org/abs/2509.01088)；原件：[arxiv-agent.html](supplement-20261007/arxiv-agent.html) #5。

当前元信息：Submitted 27 November, 2025; v1 submitted 31 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> The current RAG system requires uploading plaintext documents to the cloud, risking private data leakage. Parametric RAG (PRAG) encodes documents as LoRA parameters within LLMs, offering a possible way to reduce exposure of raw content. However, it still faces two issues: (1) PRAG demands synthesizing QA pairs and fine-tuning LLM for each individual document to create its corresponding LoRA, leading to unacceptable inference latency. (2) The performance of PRAG relies solely on synthetic QA data while lacking internal alignment with standard RAG, resulting in poor generalization on out-of-distribution(OOD) inputs. Therefore, achieving high-efficiency parameterization while maintaining RAG-level performance remains a critical challenge for privacy-preserving reasoning. In this paper, we propose DistilledPRAG, a generalizable knowledge-distilled parametric RAG model aligned with standard RAG in document structure and parameter activation. We first synthesize QA pairs from single and multi-documents to enhance cross-document reasoning. Then, we mask the plaintext documents with a special token and translate them to LoRA via a parameter generator, maintaining the standard RAG document structure. Finally, guided by synthetic QA data, we train the parameter generator to match standard RAG's hidden states and output logits, enabling RAG-style reasoning without original documents. Experiments on four QA datasets show that DistilledPRAG outperforms baselines in accuracy and generalizes well on OOD data.

暂拟：P。逐文档LoRA成本/OOD → masked plaintext、参数生成器、hidden/logit蒸馏 → 核参数化检索与泄露面；LoRA不等于加密、隐私或不可恢复。

条件owner：AGENT-RAG。仅ROADMAP路由，未作具体Books比较。

### 2509.00195 FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning

[官方身份](https://arxiv.org/abs/2509.00195)；原件：[arxiv-model.html](supplement-20261007/arxiv-model.html) #1。

当前元信息：Submitted 31 January, 2026; v1 submitted 29 August, 2025; originally announced September 2025. Comments: Accepted at ASPLOS 2026

完整摘要（实际读；作者原文，不作为成立证据）：

> Recent advances in reasoning Large Language Models (LLMs) are driving the emergence of agentic AI systems. Edge deployment of LLM agents near end users is increasingly necessary to protect data privacy, enable offline use, and provide responsive interaction with local context. However, strict memory constraints on edge devices limit deployment to smaller LLMs, whose reasoning capabilities are much weaker than those of large cloud models, hindering practical deployment of edge agentic AI. Test-Time Scaling (TTS) offers a promising solution by allocating more compute during inference to enhance the reasoning capability of edge LLMs. However, current TTS methods introduce heavy hardware performance overhead on resource-constrained devices, making them impractical for real applications. To address this challenge, we present FastTTS, a serving system that enables fast and efficient TTS for memory-constrained LLM reasoning. After analyzing common patterns across various TTS methods and identifying their performance bottlenecks, we introduce three novel techniques: i) Speculative Beam Extension, which mitigates system stragglers caused by irregular reasoning paths, ii) Asymmetric Multi-Model Memory Allocation, which dynamically balances memory usage between token generation and reasoning-step verification, and iii) Dynamic Prefix-Aware Scheduling, which optimizes reasoning execution to maximize KV-cache reuse across search paths. FastTTS offers a plug-and-play third-party library on top of vLLM, enabling edge LLMs on a single consumer GPU to match cloud-model accuracy and cloud-measured latency. Comprehensive evaluation shows that FastTTS achieves an average 2.2x higher goodput and reduces latency by 38%--68% compared to the vLLM baseline; it pushes the boundaries of low-latency TTS on memory-constrained edge devices and highlights the potential for democratizing agentic AI.

暂拟：P。TTS搜索straggler/多模型内存/KV重复 → speculative beam extension/非对称分配/prefix调度 → 核质量与端到端资源取舍，不采用云模型匹配或2.2倍。

条件owner：INFER-SCHEDULING。仅ROADMAP路由，未作具体Books比较。

### 2509.00259 Quantum-Optimized Selective State Space Model for Efficient Time Series Prediction

[官方身份](https://arxiv.org/abs/2509.00259)；原件：[arxiv-model.html](supplement-20261007/arxiv-model.html) #2。

当前元信息：Submitted 29 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> Long-range time series forecasting remains challenging, as it requires capturing non-stationary and multi-scale temporal dependencies while maintaining noise robustness, efficiency, and stability. Transformer-based architectures such as Autoformer and Informer improve generalization but suffer from quadratic complexity and degraded performance on very long time horizons. State space models, notably S-Mamba, provide linear-time updates but often face unstable training dynamics, sensitivity to initialization, and limited robustness for multivariate forecasting. To address such challenges, we propose the Quantum-Optimized Selective State Space Model (Q-SSM), a hybrid quantum-optimized approach that integrates state space dynamics with a variational quantum gate. Instead of relying on expensive attention mechanisms, Q-SSM employs a simple parametrized quantum circuit (RY-RX ansatz) whose expectation values regulate memory updates adaptively. This quantum gating mechanism improves convergence stability, enhances the modeling of long-term dependencies, and provides a lightweight alternative to attention. We empirically validate Q-SSM on three widely used benchmarks, i.e., ETT, Traffic, and Exchange Rate. Results show that Q-SSM consistently improves over strong baselines (LSTM, TCN, Reformer), Transformer-based models, and S-Mamba. These findings demonstrate that variational quantum gating can address current limitations in long-range forecasting, leading to accurate and robust multivariate predictions.

暂拟：U。RY-RX期望值gate调控SSM memory updates有结构，是否改变主线状态更新而非领域指标尚含糊；核gate/经典对照与计算路径，不因量子/小模型关闭。

条件owner：MODEL-LONG-CONTEXT。仅ROADMAP路由，未作具体Books比较。

### 2509.00373 Activation Steering Meets Preference Optimization: Defense Against Jailbreaks in Vision Language Models

[官方身份](https://arxiv.org/abs/2509.00373)；原件：[arxiv-model.html](supplement-20261007/arxiv-model.html) #3；[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #8。

当前元信息：Submitted 30 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> Vision Language Models (VLMs) have demonstrated impressive capabilities in integrating visual and textual information for understanding and reasoning, but remain highly vulnerable to adversarial attacks. While activation steering has emerged as a promising defence, existing approaches often rely on task-specific contrastive prompts to extract harmful directions, which exhibit suboptimal performance and can degrade visual grounding performance. To address these limitations, we propose \textit{Sequence-Level Preference Optimization} for VLM (\textit{SPO-VLM}), a novel two-stage defense framework that combines activation-level intervention with policy-level optimization to enhance model robustness. In \textit{Stage I}, we compute adaptive layer-specific steering vectors from diverse data sources, enabling generalized suppression of harmful behaviors during inference. In \textit{Stage II}, we refine these steering vectors through a sequence-level preference optimization process. This stage integrates automated toxicity assessment, as well as visual-consistency rewards based on caption-image alignment, to achieve safe and semantically grounded text generation. The two-stage structure of SPO-VLM balances efficiency and effectiveness by combining a lightweight mitigation foundation in Stage I with deeper policy refinement in Stage II. Extensive experiments shown SPO-VLM enhances safety against attacks via activation steering and preference optimization, while maintaining strong performance on benign tasks without compromising visual understanding capabilities. We will release our code, model weights, and evaluation toolkit to support reproducibility and future research. \textcolor{red}{Warning: This paper may contain examples of offensive or harmful text and images.}

暂拟：P。steering损伤grounding → layer-specific steering+序列偏好/visual consistency → 核防御/语义保持冲突、false-refusal与攻击覆盖。

条件owner：PLATFORM-SECURITY。仅ROADMAP路由，未作具体Books比较。

### 2509.00679 Router Upcycling: Leveraging Mixture-of-Routers in Mixture-of-Experts Upcycling

[官方身份](https://arxiv.org/abs/2509.00679)；原件：[arxiv-model.html](supplement-20261007/arxiv-model.html) #7。

当前元信息：Submitted 30 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> The Mixture-of-Experts (MoE) models have gained significant attention in deep learning due to their dynamic resource allocation and superior performance across diverse tasks. However, efficiently training these models remains challenging. The MoE upcycling technique has been proposed to reuse and improve existing model components, thereby minimizing training overhead. Despite this, simple routers, such as linear routers, often struggle with complex routing tasks within MoE upcycling. In response, we propose a novel routing technique called Router Upcycling to enhance the performance of MoE upcycling models. Our approach initializes multiple routers from the attention heads of preceding attention layers during upcycling. These routers collaboratively assign tokens to specialized experts in an attention-like manner. Each token is processed into diverse queries and aligned with the experts' features (serving as keys). Experimental results demonstrate that our method achieves state-of-the-art (SOTA) performance, outperforming other upcycling baselines.

暂拟：P。MoE upcycling router弱 → 复用前序attention heads构多router，token queries/expert keys → 核负载/容量与预算，不采用SOTA。

条件owner：MODEL-MOE。仅ROADMAP路由，未作具体Books比较。

### 2509.00685 MPO: Multidimensional Preference Optimization for Language Model-based Text-to-Speech

[官方身份](https://arxiv.org/abs/2509.00685)；原件：[arxiv-model.html](supplement-20261007/arxiv-model.html) #8。

当前元信息：Submitted 30 August, 2025; originally announced September 2025. Comments: Accepted by NCMMSC2025

完整摘要（实际读；作者原文，不作为成立证据）：

> In recent years, text-to-speech (TTS) has seen impressive advancements through large-scale language models, achieving human-level speech quality. Integrating human feedback has proven effective for enhancing robustness in these systems. However, current approaches face challenges in optimizing TTS with preference data across multiple dimensions and often suffer from performance degradation due to overconfidence in rewards. We propose Multidimensional Preference Optimization (MPO) to better align TTS systems with human preferences. MPO introduces a preference set that streamlines the construction of data for multidimensional preference optimization, enabling alignment with multiple dimensions. Additionally, we incorporate regularization during training to address the typical degradation issues in DPO-based approaches. Our experiments demonstrate MPO's effectiveness, showing significant improvements in intelligibility, speaker similarity, and prosody compared to baseline systems.

暂拟：U。多维偏好/reward overconfidence明确，preference set与regularization具体新增机制未明；定点核正则，不因speech/局部改进关闭。

条件owner：TRAIN-DPO。仅ROADMAP路由，未作具体Books比较。

### 2509.00039 AMMKD: Adaptive Multimodal Multi-teacher Distillation for Lightweight Vision-Language Models

[官方身份](https://arxiv.org/abs/2509.00039)；原件：[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #1。

当前元信息：Submitted 23 August, 2025; originally announced September 2025. Comments: 9 pages

完整摘要（实际读；作者原文，不作为成立证据）：

> The success of large-scale visual language pretraining (VLP) models has driven widespread adoption of image-text retrieval tasks. However, their deployment on mobile devices remains limited due to large model sizes and computational complexity. We propose Adaptive Multi-Modal Multi-Teacher Knowledge Distillation (AMMKD), a novel framework that integrates multi-modal feature fusion, multi-teacher distillation, and adaptive optimization to deliver lightweight yet effective retrieval models. Specifically, our method begins with a feature fusion network that extracts and merges discriminative features from both the image and text modalities. To reduce model parameters and further improve performance, we design a multi-teacher knowledge distillation framework to pre-train two CLIP teacher models. We decouple modalities by pre-computing and storing text features as class vectors via the teacher text encoder to enhance efficiency. To better align teacher and student outputs, we apply KL scatter for probability distribution matching. Finally, we design an adaptive dynamic weighting scheme that treats multi-teacher distillation as a multi-objective optimization problem. By leveraging gradient space diversity, we dynamically adjust the influence of each teacher, reducing conflicts and guiding the student toward more optimal learning directions. Extensive experiments on three benchmark datasets demonstrate that AMMKD achieves superior performance while significantly reducing model complexity, validating its effectiveness and flexibility.

暂拟：P。多teacher梯度冲突/文本编码成本 → 缓存text class vectors及gradient-diversity权重 → 核冲突条件与缓存成本，不以模块组合即证明。

条件owner：MULTIMODAL-REPRESENTATION。仅ROADMAP路由，未作具体Books比较。

### 2509.00055 U2UData+: A Scalable Swarm UAVs Autonomous Flight Dataset for Embodied Long-horizon Tasks

[官方身份](https://arxiv.org/abs/2509.00055)；原件：[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #2。

当前元信息：Submitted 19 November, 2025; v1 submitted 25 August, 2025; originally announced September 2025. Comments: Accepted by AAAI26

完整摘要（实际读；作者原文，不作为成立证据）：

> Swarm UAV autonomous flight for Embodied Long-Horizon (ELH) tasks is crucial for advancing the low-altitude economy. However, existing methods focus only on specific basic tasks due to dataset limitations, failing in real-world deployment for ELH tasks. ELH tasks are not mere concatenations of basic tasks, requiring handling long-term dependencies, maintaining embodied persistent states, and adapting to dynamic goal shifts. This paper presents U2UData+, the first large-scale swarm UAV autonomous flight dataset for ELH tasks and the first scalable swarm UAV data online collection and algorithm closed-loop verification platform. The dataset is captured by 15 UAVs in autonomous collaborative flights for ELH tasks, comprising 12 scenes, 720 traces, 120 hours, 600 seconds per trajectory, 4.32M LiDAR frames, and 12.96M RGB frames. This dataset also includes brightness, temperature, humidity, smoke, and airflow values covering all flight routes. The platform supports the customization of simulators, UAVs, sensors, flight algorithms, formation modes, and ELH tasks. Through a visual control window, this platform allows users to collect customized datasets through one-click deployment online and to verify algorithms by closed-loop simulation. U2UData+ also introduces an ELH task for wildlife conservation and provides comprehensive benchmarks with 9 SOTA models. U2UData+ can be found at https://fengtt42.github.io/U2UData-2/.

暂拟：C拟。完整摘要给数据/平台规模、可定制闭环、persistent-state需求，但未明确新增状态失效证据、区分拼接任务的评价规则或验证条件。不是因benchmark/UAV/小模型关闭；请重点校准是否重开long-horizon评价盲区。

条件owner：MULTIMODAL-EMBODIED-VLA。仅ROADMAP路由，未作具体Books比较。

### 2509.00117 Embodied AI: Emerging Risks and Opportunities for Policy Action

[官方身份](https://arxiv.org/abs/2509.00117)；原件：[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #3。

当前元信息：Submitted 3 September, 2025; v1 submitted 28 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> The field of embodied AI (EAI) is rapidly advancing. Unlike virtual AI, EAI systems can exist in, learn from, reason about, and act in the physical world. With recent advances in AI models and hardware, EAI systems are becoming increasingly capable across wider operational domains. While EAI systems can offer many benefits, they also pose significant risks, including physical harm from malicious use, mass surveillance, as well as economic and societal disruption. These risks require urgent attention from policymakers, as existing policies governing industrial robots and autonomous vehicles are insufficient to address the full range of concerns EAI systems present. To help address this issue, this paper makes three contributions. First, we provide a taxonomy of the physical, informational, economic, and social risks EAI systems pose. Second, we analyze policies in the US, EU, and UK to assess how existing frameworks address these risks and to identify critical gaps. We conclude by offering policy recommendations for the safe and beneficial deployment of EAI systems, such as mandatory testing and certification schemes, clarified liability frameworks, and strategies to manage EAI's potentially transformative economic and societal impacts.

暂拟：C拟。风险分类/政策比较/认证责任建议尚未给改变模型或执行机制、可验证测试边界的具体增量，不因综述标签关闭。风险保留；若测试盲区实质改变safety envelope则重开。

条件owner：PLATFORM-SECURITY。仅ROADMAP路由，未作具体Books比较。

### 2509.00183 FNODE: Flow-Matching for data-driven simulation of constrained multibody systems

[官方身份](https://arxiv.org/abs/2509.00183)；原件：[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #4。

当前元信息：Submitted 19 March, 2026; v1 submitted 29 August, 2025; originally announced September 2025. Comments: 36 pages, 19 figures

完整摘要（实际读；作者原文，不作为成立证据）：

> Data-driven modeling of constrained multibody dynamics remains challenged by (i) the training cost of Neural ODEs, which typically require backpropagation through an ODE solver, and (ii) error accumulation in rollout predictions. We introduce a Flow-Matching Neural ODE (FNODE) framework that learns the acceleration mapping directly from trajectory data by supervising accelerations rather than integrated states, turning training into a supervised regression problem and eliminating the ODE-adjoint/solver backpropagation bottleneck. Acceleration targets are obtained efficiently via numerical differentiation using a hybrid fast Fourier transform (FFT) and finite-difference (FD) scheme. Kinematic constraints are enforced through coordinate partitioning: FNODE learns accelerations only for the independent generalized coordinates, while the dependent coordinates are recovered by solving the position-level constraint equations. We evaluate FNODE on single and triple mass-spring-damper systems, a double pendulum, a slider crank with and without friction, a vehicle model, and a cart-pole, and compare against MBD-NODE, LSTM, and fully connected baselines. Across these benchmarks, FNODE achieves improved prediction accuracy and training/runtime efficiency, while maintaining constraint satisfaction through the partitioning procedure. Our code and scripts are released as open source to support reproducibility and follow-on research.

暂拟：U。acceleration supervision绕ODE反传及coordinate partition保约束是真结构，但对象为多体仿真；不能借World Model类比绕过AI for Science暂缓。校准与学习/约束表示主线的直接关系。

条件owner：MULTIMODAL-WORLD-MODELS（仅条件）。仅ROADMAP路由，未作具体Books比较。

### 2509.00336 Are We Really Learning the Score Function? Reinterpreting Diffusion Models Through Wasserstein Gradient Flow Matching

[官方身份](https://arxiv.org/abs/2509.00336)；原件：[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #7。

当前元信息：Submitted 29 August, 2025; originally announced September 2025. Report number: LA-UR-25-28802 (Version 2)

完整摘要（实际读；作者原文，不作为成立证据）：

> Diffusion models are commonly interpreted as learning the score function, i.e., the gradient of the log-density of noisy data. However, this assumption implies that the target of learning is a conservative vector field, which is not enforced by the neural network architectures used in practice. We present numerical evidence that trained diffusion networks violate both integral and differential constraints required of true score functions, demonstrating that the learned vector fields are not conservative. Despite this, the models perform remarkably well as generative mechanisms. To explain this apparent paradox, we advocate a new theoretical perspective: diffusion training is better understood as flow matching to the velocity field of a Wasserstein Gradient Flow (WGF), rather than as score learning for a reverse-time stochastic differential equation. Under this view, the "probability flow" arises naturally from the WGF framework, eliminating the need to invoke reverse-time SDE theory and clarifying why generative sampling remains successful even when the neural vector field is not a true score. We further show that non-conservative errors from neural approximation do not necessarily harm density transport. Our results advocate for adopting the WGF perspective as a principled, elegant, and theoretically grounded framework for understanding diffusion generative models.

暂拟：P。score真梯度要求保守场但网络未强制 → 数值反例/WGF velocity解释 → 核density transport条件，不能外推全部score解释无效。

条件owner：MULTIMODAL-GENERATIVE-PARADIGMS。仅ROADMAP路由，未作具体Books比较。

### 2509.00465 Embodied Spatial Intelligence: from Implicit Scene Modeling to Spatial Reasoning

[官方身份](https://arxiv.org/abs/2509.00465)；原件：[arxiv-multimodal.html](supplement-20261007/arxiv-multimodal.html) #9。

当前元信息：Submitted 30 August, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> This thesis introduces "Embodied Spatial Intelligence" to address the challenge of creating robots that can perceive and act in the real world based on natural language instructions. To bridge the gap between Large Language Models (LLMs) and physical embodiment, we present contributions on two fronts: scene representation and spatial reasoning. For perception, we develop robust, scalable, and accurate scene representations using implicit neural models, with contributions in self-supervised camera calibration, high-fidelity depth field generation, and large-scale reconstruction. For spatial reasoning, we enhance the spatial capabilities of LLMs by introducing a novel navigation benchmark, a method for grounding language in 3D, and a state-feedback mechanism to improve long-horizon decision-making. This work lays a foundation for robots that can robustly perceive their surroundings and intelligently act upon complex, language-based commands.

暂拟：P。语言行动缺状态反馈/3D grounding → thesis含state-feedback机制 → 仅核此机制及更早论文家族，不把整thesis当新事件/全文队列。

条件owner：MULTIMODAL-EMBODIED-VLA。仅ROADMAP路由，未作具体Books比较。

### 2509.03110 LSAM: Asynchronous Distributed Training with Landscape-Smoothed Sharpness-Aware Minimization

[官方身份](https://arxiv.org/abs/2509.03110)；原件：[arxiv-system.html](supplement-20261007/arxiv-system.html) #2。

当前元信息：Submitted 3 September, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> While Sharpness-Aware Minimization (SAM) improves generalization in deep neural networks by minimizing both loss and sharpness, it suffers from inefficiency in distributed large-batch training. We present Landscape-Smoothed SAM (LSAM), a novel optimizer that preserves SAM's generalization advantages while offering superior efficiency. LSAM integrates SAM's adversarial steps with an asynchronous distributed sampling strategy, generating an asynchronous distributed sampling scheme, producing a smoothed sharpness-aware loss landscape for optimization. This design eliminates synchronization bottlenecks, accelerates large-batch convergence, and delivers higher final accuracy compared to data-parallel SAM.

暂拟：P。分布式SAM同步障碍 → adversarial steps与异步sampling构smoothed landscape → 核staleness/一致性和可比预算。

条件owner：TRAIN-DISTRIBUTED-TRAINING。仅ROADMAP路由，未作具体Books比较。

### 2509.04084 Optimizing Frequent Checkpointing via Low-Cost Differential for Distributed Training Systems

[官方身份](https://arxiv.org/abs/2509.04084)；原件：[arxiv-system.html](supplement-20261007/arxiv-system.html) #4。

当前元信息：Submitted 13 August, 2026; v1 submitted 4 September, 2025; originally announced September 2025.

完整摘要（实际读；作者原文，不作为成立证据）：

> Distributed training of large deep-learning models often leads to failures, so checkpointing is commonly employed for recovery. State-of-the-art studies focus on frequent checkpointing for fast recovery from failures. However, frequent checkpointing generates numerous checkpoints, incurring substantial costs and thus degrading training performance. Recently, differential checkpointing has been proposed to reduce costs, but it is limited to recommendation systems, so its application to general distributed training systems remains unexplored. In this paper, we find that gradients generated during distributed training can be reused to construct differential checkpoints, while the former's size is smaller than the latter's, motivating us to reuse gradients for low-cost differential checkpointing. Based on this main idea, we propose \sysname, a frequent checkpointing framework for compression-enabled training systems that reuses compressed gradients as differential checkpoints, eliminating redundant differential computation and reducing checkpoint transmission cost. Furthermore, we extend gradient reuse to scenarios without gradient compression and propose \sysnameplus, which employs layer-wise-reuse snapshotting and incremental-merging persistence to overlap checkpointing with training execution. Experiments on diverse workloads, including billion-parameter-scale models, demonstrate that \sysname and \sysnameplus significantly reduce checkpointing overhead and enable checkpointing at frequencies as high as once per iteration, reducing training time by up to 89.2\% and 81.2\%, respectively.

暂拟：P。频繁checkpoint重复计算/传输 → compressed-gradient复用、layer-wise snapshot/incremental merge → 核一致快照/optimizer状态/恢复失败；2026当前增量不倒灌2025。

条件owner：TRAIN-CHECKPOINT。仅ROADMAP路由，未作具体Books比较。

### 2509.04467 PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference

[官方身份](https://arxiv.org/abs/2509.04467)；原件：[arxiv-system.html](supplement-20261007/arxiv-system.html) #5。

当前元信息：Submitted 14 December, 2025; v1 submitted 28 August, 2025; originally announced September 2025. Comments: Minor revisions

完整摘要（实际读；作者原文，不作为成立证据）：

> Large Language Models (LLMs) demonstrate exceptional capabilities across various tasks, but their deployment is constrained by high computational and memory costs. Model pruning provides an effective means to alleviate these demands. However, existing methods often ignore the characteristics of prefill-decode (PD) disaggregation in practice. In this paper, we propose a pruning method that is highly integrated with PD disaggregation, enabling more precise pruning of blocks. Our approach constructs pruning and distillation sets to perform iterative block removal, obtaining better pruning solutions. Moreover, we analyze the pruning sensitivity of the prefill and decode stages and identify removable blocks specific to each stage, making it well suited for PD disaggregation deployment. Extensive experiments demonstrate our approach consistently achieves strong performance in both PD disaggregation and PD unified (non-PD disaggregation) settings, and can also be extended to other non-block pruning methods. Under the same settings, our method achieves improved performance and faster inference.

暂拟：P。pruning忽略PD阶段敏感性 → 阶段特定blocks及distill → 核不同P/D模型的KV/状态兼容，不仅速度质量。

条件owner：INFER-PD-DISAGGREGATION。仅ROADMAP路由，未作具体Books比较。

### 2509.04576 Communication-Efficient Collaborative LLM Inference via Distributed Speculative Decoding

[官方身份](https://arxiv.org/abs/2509.04576)；原件：[arxiv-system.html](supplement-20261007/arxiv-system.html) #7。

当前元信息：Submitted 7 November, 2025; v1 submitted 4 September, 2025; originally announced September 2025. Comments: Accepted in the Seventeenth International Conference on Wireless Communications and Signal Processing Oct. 23-25, 2025

完整摘要（实际读；作者原文，不作为成立证据）：

> Speculative decoding is an emerging technique that accelerates large language model (LLM) inference by allowing a smaller draft model to predict multiple tokens in advance, which are then verified or corrected by a larger target model. In AI-native radio access networks (AI-RAN), this paradigm is well-suited for collaborative inference between resource-constrained end devices and more capable edge servers or base stations (BSs). However, existing distributed speculative decoding requires transmitting the full vocabulary probability distribution from the draft model on the device to the target model at the BS, which leads to prohibitive uplink communication overhead. To address this issue, we propose a ``Top-K Sparse Logits Transmission (TK-SLT)`` scheme, where the draft model transmits only the top-K token raw probabilities and the corresponding token indices instead of the entire distribution. This approach significantly reduces bandwidth consumption while maintaining inference performance. We further derive an analytical expression for the optimal draft length that maximizes inference throughput, and provide a theoretical analysis of the achievable speedup ratio under TK-SLT. Experimental results validate both the efficiency and effectiveness of the proposed method.

暂拟：P。全词表上行昂贵 → Top-K raw概率/索引与draft length解析 → 核丢失概率质量的acceptance/residual correction，节省带宽不推出lossless。

条件owner：INFER-SPECULATIVE-DECODING。仅ROADMAP路由，未作具体Books比较。

### 2509.20377 SKILL-RAG: Self-Knowledge Induced Learning and Filtering for Retrieval-Augmented Generation

[官方身份](https://arxiv.org/abs/2509.20377)；原件：[arxiv-agent.html](supplement-20261007/arxiv-agent.html) #46。

当前元信息：Submitted 20 August, 2026; v1 submitted 20 September, 2025; originally announced September 2025. Comments: The author has decided not to pursue further development or publication of this work. Since the current manuscript represents an incomplete research project and no revised version is planned, the author requests that the article be withdrawn

完整摘要（实际读；作者原文，不作为成立证据）：

> Retrieval-Augmented Generation (RAG) has significantly improved the performance of large language models (LLMs) on knowledge-intensive tasks in recent years. However, since retrieval systems may return irrelevant content, incorporating such information into the model often leads to hallucinations. Thus, identifying and filtering out unhelpful retrieved content is a key challenge for improving RAG performance.To better integrate the internal knowledge of the model with external knowledge from retrieval, it is essential to understand what the model "knows" and "does not know" (which is also called "self-knowledge"). Based on this insight, we propose SKILL-RAG (Self-Knowledge Induced Learning and Filtering for RAG), a novel method that leverages the model's self-knowledge to determine which retrieved documents are beneficial for answering a given query. We design a reinforcement learning-based training framework to explicitly elicit self-knowledge from the model and employs sentence-level granularity to filter out irrelevant content while preserving useful knowledge.We evaluate SKILL-RAG using Llama2-7B and Qwen3-8B on several question answering benchmarks. Experimental results demonstrate that SKILL-RAG not only improves generation quality but also significantly reduces the number of input documents, validating the importance of self-knowledge in guiding the selection of high-quality retrievals.

暂拟：撤回。当前v2官方撤回，研究不完整且作者不继续；无PDF不是访问故障。withdrawn history为2026-08-21T02:21:43Z，不是Sep01事件。不入选/评分/Books。

条件owner：不采用。仅ROADMAP路由，未作具体Books比较。

### 2509.05207 RapidGNN: Energy and Communication-Efficient Distributed Training on Large-Scale Graph Neural Networks

[官方身份](https://arxiv.org/abs/2509.05207)；原件：[arxiv-system.html](supplement-20261007/arxiv-system.html) #9。

当前元信息：Submitted 5 September, 2025; originally announced September 2025. Comments: arXiv admin note: text overlap with arXiv:2505.10806

完整摘要（实际读；作者原文，不作为成立证据）：

> Graph Neural Networks (GNNs) have become popular across a diverse set of tasks in exploring structural relationships between entities. However, due to the highly connected structure of the datasets, distributed training of GNNs on large-scale graphs poses significant challenges. Traditional sampling-based approaches mitigate the computational loads, yet the communication overhead remains a challenge. This paper presents RapidGNN, a distributed GNN training framework with deterministic sampling-based scheduling to enable efficient cache construction and prefetching of remote features. Evaluation on benchmark graph datasets demonstrates RapidGNN's effectiveness across different scales and topologies. RapidGNN improves end-to-end training throughput by 2.46x to 3.00x on average over baseline methods across the benchmark datasets, while cutting remote feature fetches by over 9.70x to 15.39x. RapidGNN further demonstrates near-linear scalability with an increasing number of computing units efficiently. Furthermore, it achieves increased energy efficiency over the baseline methods for both CPU and GPU by 44% and 32%, respectively.

暂拟：P/重合隔离。deterministic sampling调度驱动cache/prefetch有通信线索；官方admin明确text overlap with 2505.10806，定点核家族/增量。不忽略标记，不自动认定抄袭/撤回；GNN也不自动证明LLM迁移。

条件owner：TRAIN-DISTRIBUTED-TRAINING（条件）。仅ROADMAP路由，未作具体Books比较。

### 2509.01106 Robix: A Unified Model for Robot Interaction, Reasoning and Planning

[官方身份](https://arxiv.org/abs/2509.01106)；原件：[seed-paper.json](supplement-20261007/seed-paper.json) #9。

当前元信息：Seed ID311 PublishDate1756656000000=Sep01 BJT; IsPinned=false; arXiv current v2 revised Sep11; v1 submitted Sep01, not public-announcement proof.

完整摘要（实际读；作者原文，不作为成立证据）：

> We introduce Robix, a unified vision-language model designed to serve as the high-level cognitive layer in a hierarchical robot system, integrating robot reasoning, task planning, and natural language interaction within a single architecture. Robix dynamically generates atomic commands for low-level controllers alongside verbal responses for human interaction, enabling end-to-end execution of complex instructions, long-horizon task planning, and natural human-robot collaboration. The model also introduces novel capabilities such as proactive dialogue, real-time interruption handling, and context-aware commonsense reasoning during task execution. At its core, Robix employs chain-of-thought reasoning and is trained through a three-stage strategy: (1) continued pretraining to enhance embodied reasoning skills like 3D spatial understanding, visual grounding, and task-centric reasoning; (2) supervised finetuning to model human-robot interaction and task planning as a unified reasoning-action sequence; and (3) reinforcement learning to improve reasoning-action consistency and long-horizon task coherence. Extensive experiments show that Robix outperforms both open-source and commercial baselines—including GPT-4o and Gemini 2.5 Pro—in interactive task execution, demonstrating strong generalization across diverse instruction types (e.g., open-ended, multi-stage, constrained, invalid, and interrupted) and various user-involved tasks such as table bussing, grocery shopping, and dietary filtering.

暂拟：P。高层互动/规划需中断与低层边界 → atomic command+verbal response、统一reasoning/action三阶段训练 → 核interrupt commit/cancel和安全。不采用胜过GPT/Gemini。Seed日期支持目录事件，非arXiv首公开。

条件owner：MULTIMODAL-EMBODIED-VLA。仅ROADMAP路由，未作具体Books比较。

## 标记与旧家族事件

[SKILL-RAG原页](supplement-20261007/withdrawal-20377.html)withdrawn/comments/v2 history；[RapidGNN原页](supplement-20261007/overlap-05207.html)comments admin note；[Robix当前原页](supplement-20261007/seed-01106.html)完整摘要/版本。撤回与重合信号不被日期缺口掩盖。

LongCat：[本轮重新取得官方全文](supplement-20261007/longcat.html)，正文明确2025-09-01“正式发布并开源”。旧zero-computation experts、PID平均激活、跨层shortcut overlap核心有效证据复用，不重算；新自然日不要求精确时刻。请校准官方release的窗内准入/与旧更早paper或repo家族去重，commit不证明repo首次公开，官方release日不等于paper首公开。条件owner MODEL-MOE；独立校准后才比较实际Books，尚无书稿提案或性能采用。

## 下一执行点

FIRST回写后按具名差额处理U、版本/家族，再读必要机制与反侧。旧44/core/裁决不重扫。剩余机构分页和官方本日列表补检是普通来源工作，作者继续；不授全14覆盖、作者READY或DAY。

## 独立到达后的差额（不覆盖上文首批拟判断）

Boole首批23实际FIRST已落盘，19P/3C/1撤回及LongCat官方Sep01 release事件校准通过，不是DAY。[具名独立结果](review-supplement-20261007.md)。作者已接受R1–R6并另存[写回/实际owner比较](author-calibration-writeback-20261007.md)：三个U转窄P、FNODE转C、两C以实际v1 core理由限定；Q-SSM中心保证隔离、Thesis/Statler估计状态与真实反馈区分、RapidGNN同作者前作与重合标记、Robix目录日期与正文公开分层。上文16P/4U/2C拟/1撤回只是首批历史快照，不再冒称最终准入状态。源恢复差额在supplement后续段；第二批8另包待校准。
