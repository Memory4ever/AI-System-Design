# 第五批有限主题准入（原始线索，未冻结当窗候选）

以下15具体标题完整题摘已实际读。库存Updated映射不作日期证据；原摘先用于潜在贡献校准，拟采用仍须逐项exact-v1与日期绑定。含糊只一次core，不自动全篇。

## 2602.13466 — Language Model Memory and Memory Models for Language

原始身份：https://arxiv.org/abs/2602.13466v1；Submitted raw：2026-02-13T21:16:10Z，日期尚未逐项绑定。

The ability of machine learning models to store input information in hidden layer vector embeddings, analogous to the concept of `memory', is widely employed but not well characterized. We find that language model embeddings typically contain relatively little input information regardless of data and compute scale during training. In contrast, embeddings from autoencoders trained for input regeneration are capable of nearly perfect memory formation. The substitution of memory embeddings for token sequences leads to substantial computational efficiencies, motivating the introduction of a parallelizable encoder-decoder memory model architecture. Upon causal training these models contain information-poor embeddings incapable of arbitrary information access, but by combining causal and information retention objective functions they learn to form and decode information-rich memories. Training can be further streamlined by freezing a high fidelity encoder followed by a curriculum training approach where decoders first learn to process memories and then learn to additionally predict next tokens. We introduce the perspective that next token prediction training alone is poorly suited for accurate memory formation as the objective itself is non-invertible, motivating the use of combined objective functions for models where the entire input is not exposed.

判断：拟入：next-token objective非可逆→组合重建目标与冻结高保真encoder的curriculum→重新判断隐藏embedding能否替代可访问token memory。

## 2602.13476 — AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge

原始身份：https://arxiv.org/abs/2602.13476v1；Submitted raw：2026-02-13T21:31:19Z，日期尚未逐项绑定。

Robotic foundation models achieve strong generalization by leveraging internet-scale vision-language representations, but their massive computational cost creates a fundamental bottleneck: high inference latency. In dynamic environments, this latency breaks the control loop, rendering powerful models unsafe for real-time deployment. We propose AsyncVLA, an asynchronous control framework that decouples semantic reasoning from reactive execution. Inspired by hierarchical control, AsyncVLA runs a large foundation model on a remote workstation to provide high-level guidance, while a lightweight, onboard Edge Adapter continuously refines actions at high frequency. To bridge the domain gap between these asynchronous streams, we introduce an end-to-end finetuning protocol and a trajectory re-weighting strategy that prioritizes dynamic interactions. We evaluate our approach on real-world vision-based navigation tasks with communication delays up to 6 seconds. AsyncVLA achieves a 40% higher success rate than state-of-the-art baselines, effectively bridging the gap between the semantic intelligence of large models and the reactivity required for edge robotics.

判断：一次决定core：remote semantic/onboard adapter本身为旧hierarchical组合；只核finetuning/trajectory reweight是否具体处理延迟下过期guidance分布或新成立边界，若只是接口与动态数据偏重则关闭。

## 2602.13483 — Finding Interpretable Prompt-Specific Circuits in Language Models

原始身份：https://arxiv.org/abs/2602.13483v1；Submitted raw：2026-02-13T21:41:17Z，日期尚未逐项绑定。

Understanding the internal circuits that language models use to solve tasks remains a central challenge in mechanistic interpretability. A crucial part of finding circuits is understanding why each attention head attends where it does. To this end, we introduce ACC++, an improved circuit-tracing method based on the principle of attention-causal communication (ACC) [1], which identifies signals, i.e., contents of low dimensional subspaces that cause attention on a token pair. ACC++ extracts circuits from a single forward pass, without replacement models or patching. Circuits identified by ACC++ consist of components that are causal for the model's attention decisions, together with the low-dimensional signals used to communicate between them. Here, we first detail the conceptual advances that ACC++ makes over previous work. We then show that across multiple models, a substantial portion of ACC++ signals are interpretable: many signals admit a short natural-language description. We next present a number of new insights into model behavior obtained via ACC++. First, we use ACC++'s interpretable circuits to characterize the sensitivity of indirect object identification (IOI) circuits to prompt structure. We find that prompt-specific circuits form well-defined clusters, and across clusters, heads receive systematically different signals corresponding to distinct mechanisms for identifying the IO name. Next, in multilingual IOI, ACC++ circuits show that while model components are reused across languages, signals are often language-specific. In a four-language IOI case study, cross-language circuit distances are consistent with linguistic relatedness. Together, these results show that ACC++ can shed light on a broad spectrum of model behaviors.

判断：拟入：替代模型/patching circuit依赖→single-forward低维attention-causal signals与prompt结构切换机制→收窄同任务同circuit解释，不把可读性当faithfulness。

## 2602.13517 — Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens

原始身份：https://arxiv.org/abs/2602.13517v1；Submitted raw：2026-02-13T23:07:37Z，日期尚未逐项绑定。

Large language models (LLMs) have demonstrated impressive reasoning capabilities by scaling test-time compute via long Chain-of-Thought (CoT). However, recent findings suggest that raw token counts are unreliable proxies for reasoning quality: increased generation length does not consistently correlate with accuracy and may instead signal "overthinking," leading to performance degradation. In this work, we quantify inference-time effort by identifying deep-thinking tokens -- tokens where internal predictions undergo significant revisions in deeper model layers prior to convergence. Across four challenging mathematical and scientific benchmarks (AIME 24/25, HMMT 25, and GPQA-diamond) and a diverse set of reasoning-focused models (GPT-OSS, DeepSeek-R1, and Qwen3), we show that deep-thinking ratio (the proportion of deep-thinking tokens in a generated sequence) exhibits a robust and consistently positive correlation with accuracy, substantially outperforming both length-based and confidence-based baselines. Leveraging this insight, we introduce Think@n, a test-time scaling strategy that prioritizes samples with high deep-thinking ratios. We demonstrate that Think@n matches or exceeds standard self-consistency performance while significantly reducing inference costs by enabling the early rejection of unpromising generations based on short prefixes.

判断：拟入：token长度/置信度未稳作effort→跨层prediction revision的deep-token比例与短prefix早拒绝→改变预算admission信号，prefix成本/泄漏待核。

## 2602.13524 — Singular Vectors of Attention Heads Align with Features

原始身份：https://arxiv.org/abs/2602.13524v1；Submitted raw：2026-02-13T23:30:02Z，日期尚未逐项绑定。

Identifying feature representations in language models is a central task in mechanistic interpretability. Several recent studies have made the observation that feature representations can be inferred in some cases from singular vectors of attention matrices. However, sound justification for this phenomenon is lacking. In this paper we address that question, asking: why and when do singular vectors align with features? First, we demonstrate that singular vectors robustly align with features in a model where features can be directly observed. We then show theoretically that such alignment is expected under a range of conditions. We close by asking how, operationally, alignment may be recognized in real models where feature representations are not directly observable. We identify sparse attention decomposition as a testable prediction of alignment, and show evidence that it emerges in real models in a manner consistent with predictions. Together these results suggest that alignment of singular vectors with features can be a sound and theoretically justified basis for feature identification in language models.

判断：拟入：singular directions被当feature缺成立条件→toy直接features与alignment理论及真实sparse decomposition预测→改变feature identification证据预算。

## 2602.13540 — On Calibration of Large Language Models: From Response To Capability

原始身份：https://arxiv.org/abs/2602.13540v1；Submitted raw：2026-02-14T01:07:45Z，日期尚未逐项绑定。

Large language models (LLMs) are widely deployed as general-purpose problem solvers, making accurate confidence estimation critical for reliable use. Prior work on LLM calibration largely focuses on response-level confidence, which estimates the correctness of a single generated output. However, this formulation is misaligned with many practical settings where the central question is how likely a model is to solve a query overall. We show that this mismatch results from the stochastic nature of modern LLM decoding, under which single-response correctness fails to reflect underlying model capability. To address this issue, we introduce capability calibration, which targets the model's expected accuracy on a query. We formally distinguish capability calibration from response calibration and show that the two differ both theoretically and empirically. We establish an empirical evaluation setup and study a range of confidence estimation methods. Our results demonstrate that capability-calibrated confidence improves pass@$k$ prediction and inference budget allocation, establishing a foundation with potential for diverse applications.

判断：拟入：单response置信度用于多次成功率→区分expected query accuracy与response calibration→pass@k和预算必须校准对应随机变量。

## 2602.13568 — Who Do LLMs Trust? Human Experts Matter More Than Other LLMs

原始身份：https://arxiv.org/abs/2602.13568v1；Submitted raw：2026-02-14T03:03:29Z，日期尚未逐项绑定。

Large language models (LLMs) increasingly operate in environments where they encounter social information such as other agents' answers, tool outputs, or human recommendations. In humans, such inputs influence judgments in ways that depend on the source's credibility and the strength of consensus. This paper investigates whether LLMs exhibit analogous patterns of influence and whether they privilege feedback from humans over feedback from other LLMs. Across three binary decision-making tasks, reading comprehension, multi-step reasoning, and moral judgment, we present four instruction-tuned LLMs with prior responses attributed either to friends, to human experts, or to other LLMs. We manipulate whether the group is correct and vary the group size. In a second experiment, we introduce direct disagreement between a single human and a single LLM. Across tasks, models conform significantly more to responses labeled as coming from human experts, including when that signal is incorrect, and revise their answers toward experts more readily than toward other LLMs. These results reveal that expert framing acts as a strong prior for contemporary LLMs, suggesting a form of credibility-sensitive social influence that generalizes across decision domains.

判断：拟入：反馈source label被当可靠性→错误expert标签仍增强服从且跨任务→专家framing不能当独立可靠证据，限所测label干预。

## 2602.13576 — Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges

原始身份：https://arxiv.org/abs/2602.13576v1；Submitted raw：2026-02-14T03:19:14Z，日期尚未逐项绑定。

Evaluation and alignment pipelines for large language models increasingly rely on LLM-based judges, whose behavior is guided by natural-language rubrics and validated on benchmarks. We identify a previously under-recognized vulnerability in this workflow, which we term Rubric-Induced Preference Drift (RIPD). Even when rubric edits pass benchmark validation, they can still produce systematic and directional shifts in a judge's preferences on target domains. Because rubrics serve as a high-level decision interface, such drift can emerge from seemingly natural, criterion-preserving edits and remain difficult to detect through aggregate benchmark metrics or limited spot-checking. We further show this vulnerability can be exploited through rubric-based preference attacks, in which benchmark-compliant rubric edits steer judgments away from a fixed human or trusted reference on target domains, systematically inducing RIPD and reducing target-domain accuracy up to 9.5% (helpfulness) and 27.9% (harmlessness). When these judgments are used to generate preference labels for downstream post-training, the induced bias propagates through alignment pipelines and becomes internalized in trained policies. This leads to persistent and systematic drift in model behavior. Overall, our findings highlight evaluation rubrics as a sensitive and manipulable control interface, revealing a system-level alignment risk that extends beyond evaluator reliability alone. The code is available at: https://github.com/ZDCSlab/Rubrics-as-an-Attack-Surface. Warning: Certain sections may contain potentially harmful content that may not be appropriate for all readers.

判断：拟入：rubric聚合验证被当judge稳定→criterion-preserving edits仍定向domain漂移并传到policy→变更门禁需domain与下游反侧。

## 2602.13626 — Benchmark Leakage Trap: Can We Trust LLM-based Recommendation?

原始身份：https://arxiv.org/abs/2602.13626v1；Submitted raw：2026-02-14T06:34:19Z，日期尚未逐项绑定。

The expanding integration of Large Language Models (LLMs) into recommender systems poses critical challenges to evaluation reliability. This paper identifies and investigates a previously overlooked issue: benchmark data leakage in LLM-based recommendation. This phenomenon occurs when LLMs are exposed to and potentially memorize benchmark datasets during pre-training or fine-tuning, leading to artificially inflated performance metrics that fail to reflect true model performance. To validate this phenomenon, we simulate diverse data leakage scenarios by conducting continued pre-training of foundation models on strategically blended corpora, which include user-item interactions from both in-domain and out-of-domain sources. Our experiments reveal a dual-effect of data leakage: when the leaked data is domain-relevant, it induces substantial but spurious performance gains, misleadingly exaggerating the model's capability. In contrast, domain-irrelevant leakage typically degrades recommendation accuracy, highlighting the complex and contingent nature of this contamination. Our findings reveal that data leakage acts as a critical, previously unaccounted-for factor in LLM-based recommendation, which could impact the true model performance. We release our code at https://github.com/yusba1/LLMRec-Data-Leakage.

判断：关闭：推荐interaction污染在in-domain虚高/out-domain退步是已知contamination与domain mismatch再现；无新的泄露定位或一般评价协议机制，不因推荐领域本身排除。

## 2602.13639 — Guided Collaboration in Heterogeneous LLM-Based Multi-Agent Systems via Entropy-Based Understanding Assessment and Experience Retrieval

原始身份：https://arxiv.org/abs/2602.13639v1；Submitted raw：2026-02-14T07:10:04Z，日期尚未逐项绑定。

With recent breakthroughs in large language models (LLMs) for reasoning, planning, and complex task generation, artificial intelligence systems are transitioning from isolated single-agent architectures to multi-agent systems with collaborative intelligence. However, in heterogeneous multi-agent systems (HMAS), capability differences among agents give rise to consistent cognitive problems, where strong and weak models fail to contribute effectively. We define the collaboration as a strong-weak system. Through comprehensive experiments, we disclose a counterintuitive phenomenon in the strong-weak system: a strong-weak collaboration may under-perform weak-weak combinations, revealing that cognitive mismatching are key bottlenecks limiting heterogeneous cooperation. To overcome these challenges, we propose an Entropy-Based Adaptive Guidance Framework that dynamically aligns the guidance with the cognitive state of each agent. The framework quantifies the understanding of weak agents through multi-dimensional entropy metrics - covering expression, uncertainty, structure, coherence, and relevance - and adaptively adjusts the intensity of the guidance at light, moderate and intensive levels. Furthermore, a Retrieval-Augmented Generation (RAG) mechanism is incorporated to retain successful collaboration experiences, enabling both immediate adaptation and long-term learning. Extensive experiments on three benchmark datasets, GSM8K, MBPP, and CVRP demonstrate that our approach consistently enhances the effectiveness and stability of heterogeneous collaboration. The results highlight that adaptive guidance not only mitigates cognitive imbalance but also establishes a scalable pathway toward more robust, cooperative multi-agent intelligence.

判断：拟入反侧：strong+weak默认强于weak+weak→实测可更弱，entropy guidance是待核机制→重新判断heterogeneous orchestration，任务/预算/来源控制待核。

一次core后改判关闭：exact-v1 V3_BODY_2602.13639.txt:154–191、200–230、293–325实际读。所谓understanding由word dispersion/uncertainty lexicon/logic markers/coherence/relevance加减，entropy与understanding反比只是预设，再接三档指导和TFIDF成功经验。SW/WW混多个model，局部下降没有隔离新的理解机制/非显然可靠性条件。组合未给足长期增量；不把“异质系统一定更强”虚构为Books旧判断。保留该局部反侧与选择人口，不借此自动评分/全稿。

## 2602.13659 — Zero-Order Optimization for LLM Fine-Tuning via Learnable Direction Sampling

原始身份：https://arxiv.org/abs/2602.13659v1；Submitted raw：2026-02-14T08:01:41Z，日期尚未逐项绑定。

Fine-tuning large pretrained language models (LLMs) is a cornerstone of modern NLP, yet its growing memory demands (driven by backpropagation and large optimizer States) limit deployment in resource-constrained settings. Zero-order (ZO) methods bypass backpropagation by estimating directional derivatives from forward evaluations, offering substantial memory savings. However, classical ZO estimators suffer from high variance and an adverse dependence on the parameter dimensionality $d$, which has constrained their use to low-dimensional problems. In this work, we propose a policy-driven ZO framework that treats the sampling distribution over perturbation directions as a learnable policy and updates it to reduce the variance of directional estimates. We develop a practical algorithm implementing this idea and provide a theoretical analysis, showing that learned sampling distributions improve the quality of gradient information and relax the explicit dependence on $d$ in convergence bounds. Empirically, we validate the approach on challenging LLM fine-tuning benchmarks, demonstrating substantially improved performance compared to standard ZO baselines. Our results suggest that adaptive direction sampling is a promising route to make ZO fine-tuning viable at scale. The source code is available at https://github.com/brain-lab-research/zo_ldsd

判断：拟入：ZO高维方差限制→学perturbation方向分布并改变收敛d依赖→受限finetuning的forward-query成本选择，理论假设待核。

## 2602.13699 — Attention Head Entropy of LLMs Predicts Answer Correctness

原始身份：https://arxiv.org/abs/2602.13699v1；Submitted raw：2026-02-14T09:50:19Z，日期尚未逐项绑定。

Large language models (LLMs) often generate plausible yet incorrect answers, posing risks in safety-critical settings such as medicine. Human evaluation is expensive, and LLM-as-judge approaches risk introducing hidden errors. Recent white-box methods detect contextual hallucinations using model internals, focusing on the localization of the attention mass, but two questions remain open: do these approaches extend to predicting answer correctness, and do they generalize out-of-domains? We introduce Head Entropy, a method that predicts answer correctness from attention entropy patterns, specifically measuring the spread of the attention mass. Using sparse logistic regression on per-head 2-Renyi entropies, Head Entropy matches or exceeds baselines in-distribution and generalizes substantially better on out-of-domains, it outperforms the closest baseline on average by +8.5% AUROC. We further show that attention patterns over the question/context alone, before answer generation, already carry predictive signal using Head Entropy with on average +17.7% AUROC over the closest baseline. We evaluate across 5 instruction-tuned LLMs and 3 QA datasets spanning general knowledge, multi-hop reasoning, and medicine.

判断：拟入：通常等回答后检测correctness→question/context-only entropy预测且跨domain→生成前拒绝/预算观测与成本边界。

## 2602.13738 — OneLatent: Single-Token Compression for Visual Latent Reasoning

原始身份：https://arxiv.org/abs/2602.13738v1；Submitted raw：2026-02-14T12:03:28Z，日期尚未逐项绑定。

Chain-of-thought (CoT) prompting improves reasoning but often increases inference cost by one to two orders of magnitude. To address these challenges, we present \textbf{OneLatent}, a framework that compresses intermediate reasoning into a single latent token via supervision from rendered CoT images and DeepSeek-OCR hidden states. By rendering textual steps into images, we obtain a deterministic supervision signal that can be inspected and audited without requiring the model to output verbose textual rationales. Across benchmarks, OneLatent reduces average output length by $11\times$ with only a $2.21\%$ average accuracy drop relative to textual CoT, while improving output token contribution (OTC) by $6.8\times$. On long-chain logical reasoning, OneLatent reaches $99.80\%$ on ProntoQA and $97.80\%$ on ProsQA with one latent token, with compression up to $87.4\times$, supporting compression-constrained generalization.

判断：关闭：render CoT→OCR hidden监督→单latent是已知多模态codec/latent distillation局部配方；给token/accuracy数但未给信息保留/总compute或新压缩成立条件，不把token少当成本机制。

## 2602.13795 — Agent-OSI: An Interoperability Architecture for Communication and Settlement in the Decentralized Internet of Agents

原始身份：https://arxiv.org/abs/2602.13795v1；Submitted raw：2026-02-14T14:14:16Z，日期尚未逐项绑定。

Large Language Models (LLMs) are accelerating the shift from an Internet of information to an Internet of Agents (IoA), where autonomous entities discover services, negotiate, execute tasks, and exchange value. Yet today's agents are still confined to platform silos and proprietary interfaces, lacking a common stack for interoperability, trust, and pay-per-use settlement. This article proposes \textit{Agent-OSI}, a functional interoperability architecture for a decentralized IoA, whose core contribution is agent-to-agent (A2A) communication and a Web-compatible, backend-agnostic settlement protocol built on HTTP 402 (Payment Required); identity, verifiable execution, and semantic orchestration are treated as boundary layers with interfaces to existing standards. We treat HTTP 402 as an application-layer challenge-response primitive -- analogous to HTTP 401 for authentication -- whose settlement backend (escrow contract, payment channel, or signed off-chain receipt) is a pluggable choice, instantiated via a blockchain escrow in our prototype. We implement a prototype and evaluate its communication and settlement performance. Results show that, for generative workloads, end-to-end latency is dominated by task execution rather than settlement confirmation, and that keeping negotiation and delivery off the settlement backend reduces per-session settlement cost by approximately 51\% relative to a more on-chain baseline.

判断：一次决定core：HTTP402+pluggable escrow/offchain negotiation属成熟组合；只核跨backend实际执行/结算状态差额，若只是分层与onchain成本对照则关闭。

一次core后关闭：exact-v1 V3_BODY_2602.13795.txt:128–161、191–217实际读。signed quote/requestHash/nonce/receipt/outputCID跨层绑定与offchain negotiation/delivery采用既有replay-resistant payment/provenance原语；本原型只一个Anvil escrow，TEE/ZK是未实现选择。51%是more-onchain对照gas，4122ms generation盖过2s local confirmation而light几乎全等链，为已知分层/摊销约束实例，不是新增可信执行或agent-specific settlement机制。保留真实prototype线索，不评分/进Books；不因区块链标签排除。

## 2602.13804 — Attention in Constant Time: Vashista Sparse Attention for Long-Context Decoding with Exponential Guarantees

原始身份：https://arxiv.org/abs/2602.13804v1；Submitted raw：2026-02-14T14:29:10Z，日期尚未逐项绑定。

Large language models spend most of their inference cost on attention over long contexts, yet empirical behavior suggests that only a small subset of tokens meaningfully contributes to each query. We formalize this phenomenon by modeling attention as a projection onto the convex hull of key vectors and analyzing its entropic (softmax-like) relaxation. Our main theoretical contribution is a face-stability theorem showing that, under a strict complementarity margin (a support gap (Δ) certified by KKT multipliers), entropic attention concentrates on a constant-size active face: the total mass assigned to inactive tokens decays exponentially as (\exp(-Ω(Δ/\varepsilon))), while the error on the active face scales linearly in the temperature/regularization parameter (\varepsilon). This yields a practical criterion for when sparse long-context decoding is safe and provides a principled knob to trade accuracy for compute.
 Building on these guarantees, we introduce Vashista Sparse Attention, a drop-in mechanism that maintains a small candidate set per query through a paging-style context selection strategy compatible with modern inference stacks. Across long-context evaluations, we observe stable constant-size effective support, strong wall-clock speedups, and minimal quality degradation in the regimes predicted by the support-gap diagnostics. Finally, we discuss deployment implications for privacy-sensitive and air-gapped settings, where interchangeable attention modules enable predictable latency and cost without external retrieval dependencies.

判断：拟入：稀疏support经验无保证→strict KKT gap下entropic face集中与误差界→有限candidate何时替代fullattention，selector维护代价另核不采标题constant-time。

## 第五批逐家族日期与版本（live原始字段）

Official availability cutoff规则与精确v1 Submitted下界、同ID/URL公开DataCite Created上界交集；半开秒bucket+1s。Updated只保留不作公开日，当前title可能修订。不按邻ID批推。以下Submitted均严格Fri02/13 19Z之后至Mon02/16 19Z，推定最早Tue02/17 01Z；Created公开注册最迟界完全落窗。这是working interval不是精确09公开。

| ID | v1 Submitted UTC | v1 Updated UTC | Created UTC | Registered UTC | 推定+08范围 |
| --- | --- | --- | --- | --- | --- |
| 2602.13466 | 2026-02-13T21:16:10Z | 2026-02-17T01:10:19Z | 2026-02-17T03:52:12.000Z | 2026-02-17T03:52:12.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:52:13+08:00) |
| 2602.13483 | 2026-02-13T21:41:17Z | 2026-02-17T01:11:00Z | 2026-02-17T03:52:36.000Z | 2026-02-17T03:52:37.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:52:37+08:00) |
| 2602.13517 | 2026-02-13T23:07:37Z | 2026-02-17T01:13:11Z | 2026-02-17T03:53:26.000Z | 2026-02-17T03:53:27.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:53:27+08:00) |
| 2602.13524 | 2026-02-13T23:30:02Z | 2026-02-17T01:13:55Z | 2026-02-17T03:53:36.000Z | 2026-02-17T03:53:37.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:53:37+08:00) |
| 2602.13540 | 2026-02-14T01:07:45Z | 2026-02-17T01:15:33Z | 2026-02-17T03:54:01.000Z | 2026-02-17T03:54:01.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:54:02+08:00) |
| 2602.13659 | 2026-02-14T08:01:41Z | 2026-02-17T01:26:35Z | 2026-02-17T03:57:02.000Z | 2026-02-17T03:57:03.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:57:03+08:00) |
| 2602.13699 | 2026-02-14T09:50:19Z | 2026-02-17T01:28:52Z | 2026-02-17T03:58:02.000Z | 2026-02-17T03:58:03.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:58:03+08:00) |
| 2602.13804 | 2026-02-14T14:29:10Z | 2026-02-17T01:34:15Z | 2026-02-17T04:00:41.000Z | 2026-02-17T04:00:42.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T12:00:42+08:00) |
| 2602.13576 | 2026-02-14T03:19:14Z | 2026-02-17T01:19:02Z | 2026-02-17T03:54:57.000Z | 2026-02-17T03:54:58.000Z | [2026-02-17T09:00:00+08:00,2026-02-17T11:54:58+08:00) |

13483 exact-v1 ABS18/BODY只采用prompt-family与attribution-noise refinement；current多语言结果不移入v1。13524 v1将先前SVD-feature推定称implicit assumption，current改observation，不改变本次采用条件命题。13699当前DataCite题为Gradient-Stable Attention Heads Signal LLM Correctness，exact-v1 ABS11–18/BODY1、60–64仍旧名，v2 Sep17；以相同ID/URL/作者+v1 date字段绑定，绝不伪当前title=旧title或审当前v2。ABS当前说明轻查无已见撤回，未遍历全史。
