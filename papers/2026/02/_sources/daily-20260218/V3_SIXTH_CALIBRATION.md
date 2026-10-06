# 第六批有限主题准入（原current完整题摘，未冻结）

仅以下15条线索，不沿库存扩池。拟入先核exact-v1/逐项日期；含糊只一次core。现有Books覆盖不影响真正新增证据准入，泛原理/排行榜不自动构成增量。

## 2602.13832 — Beyond Words: Evaluating and Bridging Epistemic Divergence in User-Agent Interaction via Theory of Mind

原始身份：https://arxiv.org/abs/2602.13832v1；Submitted raw：2026-02-14T16:01:59Z，尚非公开时间。

Large Language Models (LLMs) have developed rapidly and are widely applied to both general-purpose and professional tasks to assist human users. However, they still struggle to comprehend and respond to the true user needs when intentions and instructions are imprecisely conveyed, leading to a divergence between subjective user believes and true environment states. Resolving this epistemic divergence requires Theory of Mind (ToM), yet existing ToM evaluations for LLMs primarily focus on isolated belief inference, overlooking its functional utility in real-world interaction. To this end, we formalize ToM for LLMs as a mechanism for epistemic divergence detection and resolution, and propose a benchmark, \benchname, to assess how models reconcile user beliefs and profiles in practice. Results across 11 leading models reveal a significant limitation to identify underlying cognitive gaps that impede task success. To bridge this gap, we further curate a trajectory-based ToM dataset linking belief tracking with task-related state inference. The model trained on this data via reinforcement learning shows consistent improvement in reasoning about user mental states, leading to enhanced downstream performance. Our work highlights the practical value of ToM as an essential interaction-level mechanism rather than as a standalone reasoning skill.

判断：一次决定core：孤立belief inference→实际用户belief/环境state差异的交互协议，须确认受控state gap而非ToM标签+RL trajectory配方。

## 2602.13851 — Evaluating LLM-Generated ACSL Annotations for Formal Verification

原始身份：https://arxiv.org/abs/2602.13851v1；Submitted raw：2026-02-14T19:18:34Z，尚非公开时间。

Formal specifications are crucial for building verifiable and dependable software systems, yet generating accurate and verifiable specifications for real-world C programs remains challenging. This paper presents an empirical evaluation of automated ACSL annotation generation strategies for C programs, comparing a rule-based Python script, Frama-C's RTE plugin, and three large language models (DeepSeek-V3.2, GPT-5.2, and OLMo 3.1 32B Instruct). The study focuses on one-shot annotation generation, assessing how these approaches perform when directly applied to verification tasks. Using a filtered subset of the CASP benchmark, we evaluate generated annotations through Frama-C's WP plugin with multiple SMT solvers, analyzing proof success rates, solver timeouts, and internal processing time. Our results show that rule-based approaches remain more reliable for verification success, while LLM-based methods exhibit more variable performance. These findings highlight both the current limitations and the potential of LLMs as complementary tools for automated specification generation.

判断：关闭：one-shot ACSL三LLM/rule/RTE在CASP上的proof率比较，只提供特定工具/模型局部可用性排名；题摘无spec语义真值、vacuity或新的验证协议盲区，不以形式验证领域直接排除。

## 2602.13891 — GSRM: Generative Speech Reward Model for Speech RLHF

原始身份：https://arxiv.org/abs/2602.13891v1；Submitted raw：2026-02-14T21:22:55Z，尚非公开时间。

Recent advances in speech language models, such as GPT-4o Voice Mode and Gemini Live, have demonstrated promising speech generation capabilities. Nevertheless, the aesthetic naturalness of the synthesized audio still lags behind that of human speech. Enhancing generation quality requires a reliable evaluator of speech naturalness. However, existing naturalness evaluators typically regress raw audio to scalar scores, offering limited interpretability of the evaluation and moreover fail to generalize to speech across different taxonomies. Inspired by recent advances in generative reward modeling, we propose the Generative Speech Reward Model (GSRM), a reasoning-centric reward model tailored for speech. The GSRM is trained to decompose speech naturalness evaluation into an interpretable acoustic feature extraction stage followed by feature-grounded chain-of-thought reasoning, enabling explainable judgments. To achieve this, we curated a large-scale human feedback dataset comprising 31k expert ratings and an out-of-domain benchmark of real-world user-assistant speech interactions. Experiments show that GSRM substantially outperforms existing speech naturalness predictors, achieving model-human correlation of naturalness score prediction that approaches human inter-rater consistency. We further show how GSRM can improve the naturalness of speech LLM generations by serving as an effective verifier for online RLHF.

判断：一次决定core：acoustic feature→generative judge属于已知分解RM；须确认新可检验taxonomy成立条件/语音grounding机制，而非多31k专家标签和人相关率。

## 2602.13904 — Diagnosing Pathological Chain-of-Thought in Reasoning Models

原始身份：https://arxiv.org/abs/2602.13904v1；Submitted raw：2026-02-14T21:53:47Z，尚非公开时间。

Chain-of-thought (CoT) reasoning is fundamental to modern LLM architectures and represents a critical intervention point for AI safety. However, CoT reasoning may exhibit failure modes that we note as pathologies, which prevent it from being useful for monitoring. Prior work has identified three distinct pathologies: post-hoc rationalization, where models generate plausible explanations backwards from predetermined answers; encoded reasoning, where intermediate steps conceal information within seemingly interpretable text; and internalized reasoning, where models replace explicit reasoning with meaningless filler tokens while computing internally. To better understand and discriminate between these pathologies, we create a set of concrete metrics that are simple to implement, computationally inexpensive, and task-agnostic. To validate our approach, we develop model organisms deliberately trained to exhibit specific CoT pathologies. Our work provides a practical toolkit for assessing CoT pathologies, with direct implications for training-time monitoring.

判断：拟入：CoT监控把几种非忠实现象混为一类→针对posthoc/encoded/internalized的可计算指标与训练model organisms→诊断应区分观测机制而非把可读trace当统一保证。

## 2602.13935 — Statistical Early Stopping for Reasoning Models

原始身份：https://arxiv.org/abs/2602.13935v1；Submitted raw：2026-02-15T00:14:53Z，尚非公开时间。

While LLMs have seen substantial improvement in reasoning capabilities, they also sometimes overthink, generating unnecessary reasoning steps, particularly under uncertainty, given ill-posed or ambiguous queries. We introduce statistically principled early stopping methods that monitor uncertainty signals during generation to mitigate this issue. Our first approach is parametric: it models inter-arrival times of uncertainty keywords as a renewal process and applies sequential testing for stopping. Our second approach is nonparametric and provides finite-sample guarantees on the probability of halting too early on well-posed queries. We conduct empirical evaluations on reasoning tasks across several domains and models. Our results indicate that uncertainty-aware early stopping can improve both efficiency and reliability in LLM reasoning, and we observe especially significant gains for math reasoning.

判断：拟入：启发式uncertainty早停无误停保证→renewal sequential test及nonparametric finite-sample premature halt控制→停止阈值需要明示假设/风险。

## 2602.13940 — You Can Learn Tokenization End-to-End with Reinforcement Learning

原始身份：https://arxiv.org/abs/2602.13940v1；Submitted raw：2026-02-15T00:31:24Z，尚非公开时间。

Tokenization is a hardcoded compression step which remains in the training pipeline of Large Language Models (LLMs), despite a general trend towards architectures becoming increasingly end-to-end. Prior work has shown promising results at scale in bringing this compression step inside the LLMs' architecture with heuristics to draw token boundaries, and also attempts to learn these token boundaries with straight-through estimates, which treat the problem of drawing discrete token boundaries as a continuous one. We show that these token boundaries can instead be learned using score function estimates, which have tighter theoretical guarantees due to directly optimizing the problem of drawing discrete token boundaries to minimize loss. We observe that techniques from reinforcement learning, such as time discounting, are necessary to reduce the variance of this score function sufficiently to make it practicable. We demonstrate that the resultant method outperforms prior proposed straight-through estimates, both qualitatively and quantitatively at the $100$ million parameter scale.

判断：拟入：discrete token boundary用连续STE近似→score-function离散目标与discount降低方差→端到端tokenization的估计器偏差/成本选择。

## 2602.13942 — A Theoretical Framework for LLM Fine-tuning Using Early Stopping for Non-random Initialization

原始身份：https://arxiv.org/abs/2602.13942v1；Submitted raw：2026-02-15T00:43:21Z，尚非公开时间。

In the era of large language models (LLMs), fine-tuning pretrained models has become ubiquitous. Yet the theoretical underpinning remains an open question. A central question is why only a few epochs of fine-tuning are typically sufficient to achieve strong performance on many different tasks. In this work, we approach this question by developing a statistical framework, combining rigorous early stopping theory with the attention-based Neural Tangent Kernel (NTK) for LLMs, offering new theoretical insights on fine-tuning practices. Specifically, we formally extend classical NTK theory [Jacot et al., 2018] to non-random (i.e., pretrained) initializations and provide a convergence guarantee for attention-based fine-tuning. One key insight provided by the theory is that the convergence rate with respect to sample size is closely linked to the eigenvalue decay rate of the empirical kernel matrix induced by the NTK. We also demonstrate how the framework can be used to explain task vectors for multiple tasks in LLMs. Finally, experiments with modern language models on real-world datasets provide empirical evidence supporting our theoretical insights.

判断：拟入：随机初始化NTK解释直接套预训练→attention非随机初始化convergence/eigenspectrum→few-epoch finetune与task vector解释只在证明条件内。

## 2602.13953 — QuRL: Efficient Reinforcement Learning with Quantized Rollout

原始身份：https://arxiv.org/abs/2602.13953v1；Submitted raw：2026-02-15T01:48:10Z，尚非公开时间。

Reinforcement learning with verifiable rewards (RLVR) has become a trending paradigm for training reasoning large language models (LLMs). However, due to the autoregressive decoding nature of LLMs, the rollout process becomes the efficiency bottleneck of RL training, consisting of up to 70\% of the total training time. In this work, we propose Quantized Reinforcement Learning (QuRL) that uses a quantized actor for accelerating the rollout. We address two challenges in QuRL. First, we propose Adaptive Clipping Range (ACR) that dynamically adjusts the clipping ratio based on the policy ratio between the full-precision actor and the quantized actor, which is essential for mitigating long-term training collapse. Second, we identify the weight update problem, where weight changes between RL steps are extremely small, making it difficult for the quantization operation to capture them effectively. We mitigate this problem through the invariant scaling technique that reduces quantization noise and increases weight update. We evaluate our method with INT8 and FP8 quantization experiments on DeepScaleR and DAPO, and achieve 20% to 80% faster rollout during training.

判断：拟入：quantized rollout不等full actor policy且小update被吞→ratio-dependent clipping+invariant scaling→改正rollout/trainer数值失配接口。

## 2602.13962 — CodeGlance: Understanding Code Reasoning Challenges in LLMs through Multi-Dimensional Feature Analysis

原始身份：https://arxiv.org/abs/2602.13962v1；Submitted raw：2026-02-15T02:46:51Z，尚非公开时间。

In modern software development, developers frequently need to understand code behavior at a glance -- whether reviewing pull requests, debugging issues, or navigating unfamiliar codebases. This ability to reason about dynamic program behavior is fundamental to effective software engineering and increasingly supported by Large Language Models (LLMs). However, existing studies on code reasoning focus primarily on isolated code snippets, overlooking the complexity of real-world scenarios involving external API interactions and unfamiliar functions. This gap hinders our understanding of what truly makes code reasoning challenging for LLMs across diverse programming contexts.
 We present CodeGlance, a multi-dimensional benchmark investigating code reasoning challenges across three realistic scenarios: intrinsic logic reasoning, API interaction reasoning, and unseen function reasoning. Through systematic evaluation of 7 state-of-the-art LLMs, we reveal that unseen function reasoning poses significant challenges especially for smaller models, with Qwen2.5-3b achieving only 6.0\% accuracy on unseen functions compared to 37.5\% on familiar APIs. We identify critical code complexity features -- including execution trace length, API invocation count, and control flow complexity -- that significantly impact code reasoning difficulty across scenarios. We further investigate how common augmentation strategies, including CoT, document retrieval, and code search, can improve reasoning performance, finding that their effectiveness varies substantially depending on whether challenges stem from logical complexity or knowledge gaps. These findings provide actionable guidance for developing more capable code reasoning systems and deploying LLM-based programming assistants in real-world software development.

判断：关闭：unseen函数比熟悉API难及retrieval/CoT按logic/knowledge gap不同有效是代码理解的已知知识支持边界再现；题摘主要新任务与feature关联，未呈现新的控制机制或足够修正原诊断的反证。

## 2602.14027 — Train Short, Inference Long: Training-free Horizon Extension for Autoregressive Video Generation

原始身份：https://arxiv.org/abs/2602.14027v1；Submitted raw：2026-02-15T07:14:47Z，尚非公开时间。

Autoregressive video diffusion models have emerged as a scalable paradigm for long video generation. However, they often suffer from severe extrapolation failure, where rapid error accumulation leads to significant temporal degradation when extending beyond training horizons. We identify that this failure primarily stems from the spectral bias of 3D positional embeddings and the lack of dynamic priors in noise sampling. To address these issues, we propose FLEX (Frequency-aware Length EXtension), a training-free inference-time framework that bridges the gap between short-term training and long-term inference. FLEX introduces Frequency-aware RoPE Modulation to adaptively interpolate under-trained low-frequency components while extrapolating high-frequency ones to preserve multi-scale temporal discriminability. This is integrated with Antiphase Noise Sampling (ANS) to inject high-frequency dynamic priors and Inference-only Attention Sink to anchor global structure. Extensive evaluations on VBench demonstrate that FLEX significantly outperforms state-of-the-art models at 6x extrapolation (30s duration) and matches the performance of long-video fine-tuned baselines at 12x scale (60s duration). As a plug-and-play augmentation, FLEX seamlessly integrates into existing inference pipelines for horizon extension. It effectively pushes the generation limits of models such as LongLive, supporting consistent and dynamic video synthesis at a 4-minute scale. Project page is available at https://ga-lee.github.io/FLEX_demo.

判断：拟入：AR视频越训长失稳→3D RoPE低频插值/高频外推+antiphase noise动态先验→需核位置/噪声归因与horizon成本，不只合模块。

## 2602.14041 — BitDance: Scaling Autoregressive Generative Models with Binary Tokens

原始身份：https://arxiv.org/abs/2602.14041v1；Submitted raw：2026-02-15T08:09:05Z，尚非公开时间。

We present BitDance, a scalable autoregressive (AR) image generator that predicts binary visual tokens instead of codebook indices. With high-entropy binary latents, BitDance lets each token represent up to $2^{256}$ states, yielding a compact yet highly expressive discrete representation. Sampling from such a huge token space is difficult with standard classification. To resolve this, BitDance uses a binary diffusion head: instead of predicting an index with softmax, it employs continuous-space diffusion to generate the binary tokens. Furthermore, we propose next-patch diffusion, a new decoding method that predicts multiple tokens in parallel with high accuracy, greatly speeding up inference. On ImageNet 256x256, BitDance achieves an FID of 1.24, the best among AR models. With next-patch diffusion, BitDance beats state-of-the-art parallel AR models that use 1.4B parameters, while using 5.4x fewer parameters (260M) and achieving 8.7x speedup. For text-to-image generation, BitDance trains on large-scale multimodal tokens and generates high-resolution, photorealistic images efficiently, showing strong performance and favorable scaling. When generating 1024x1024 images, BitDance achieves a speedup of over 30x compared to prior AR models. We release code and models to facilitate further research on AR foundation models. Code and models are available at: https://github.com/shallowdream204/BitDance.

判断：拟入：codebook index巨大分类头瓶颈→binary latent+diffusion head及next-patch并行→新离散表示与AR factorization代价，不从2^256授权有效容量。

## 2602.14048 — ProAct: A Dual-System Framework for Proactive Embodied Social Agents

原始身份：https://arxiv.org/abs/2602.14048v1；Submitted raw：2026-02-15T08:27:34Z，尚非公开时间。

Embodied social agents have recently advanced in generating synchronized speech and gestures. However, most interactive systems remain fundamentally reactive, responding only to current sensory inputs within a short temporal window. Proactive social behavior, in contrast, requires deliberation over accumulated context and intent inference, which conflicts with the strict latency budget of real-time interaction. We present \emph{ProAct}, a dual-system framework that reconciles this time-scale conflict by decoupling a low-latency \emph{Behavioral System} for streaming multimodal interaction from a slower \emph{Cognitive System} which performs long-horizon social reasoning and produces high-level proactive intentions. To translate deliberative intentions into continuous non-verbal behaviors without disrupting fluency, we introduce a streaming flow-matching model conditioned on intentions via ControlNet. This mechanism supports asynchronous intention injection, enabling seamless transitions between reactive and proactive gestures within a single motion stream. We deploy ProAct on a physical humanoid robot and evaluate both motion quality and interactive effectiveness. In real-world interaction user studies, participants and observers consistently prefer ProAct over reactive variants in perceived proactivity, social presence, and overall engagement, demonstrating the benefits of dual-system proactive control for embodied social interaction.

判断：拟入：异步高层intent会打断连续运动→stream flowmatching接受ControlNet intent injection→实时反应/慢意图接口成立条件，不把dual-system本身当增量。

## 2602.14050 — Position Encoding with Random Float Sampling Enhances Length Generalization of Transformers

原始身份：https://arxiv.org/abs/2602.14050v1；Submitted raw：2026-02-15T08:32:22Z，尚非公开时间。

Length generalization is the ability of language models to maintain performance on inputs longer than those seen during pretraining. In this work, we introduce a simple yet powerful position encoding (PE) strategy, Random Float Sampling (RFS), that generalizes well to lengths unseen during pretraining or fine-tuning. In particular, instead of selecting position indices from a predefined discrete set, RFS uses randomly sampled continuous values, thereby avoiding out-of-distribution (OOD) issues on unseen lengths by exposing the model to diverse indices during training. Since assigning indices to tokens is a common and fundamental procedure in widely used PEs, the advantage of RFS can easily be incorporated into, for instance, the absolute sinusoidal encoding, RoPE, and ALiBi. Experiments corroborate its effectiveness by showing that RFS results in superior performance in length generalization tasks as well as zero-shot commonsense reasoning benchmarks.

判断：拟入：离散PE index OOD→随机连续值采样适配多PE→重新考虑长度外推training support，不能说所有长context免费。

## 2602.14069 — Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric

原始身份：https://arxiv.org/abs/2602.14069v1；Submitted raw：2026-02-15T09:39:39Z，尚非公开时间。

Scalar reward models compress multi-dimensional human preferences into a single opaque score, creating an information bottleneck that often leads to brittleness and reward hacking in open-ended alignment. We argue that robust alignment for non-verifiable tasks is fundamentally a principle generalization problem: reward should not be a learned function internalized into a judge, but an explicit reasoning process executed under inspectable principles. To operationalize this view, we present the Open Rubric System (OpenRS), a plug-and-play, rubrics-based LLM-as-a-Judge framework built around Pairwise Adaptive Meta-Rubrics (PAMR) and lightweight Pointwise Verifiable Rubrics (PVRs), which provide both hard-constraint guardrails and verifiable reward components when ground-truth or programmatic checks are available. OpenRS uses an explicit meta-rubric -- a constitution-like specification that governs how rubrics are instantiated, weighted, and enforced -- and instantiates adaptive rubrics on the fly by conditioning on the semantic differences between two candidate responses. It then performs criterion-wise pairwise comparisons and aggregates criterion-level preferences externally, avoiding pointwise weighted scalarization while improving discriminability in open-ended settings. To keep principles consistent yet editable across various domains, we introduce a two-level meta-rubric refinement pipeline (automated evolutionary refinement for general principles and a reproducible human-in-the-loop procedure for domain principles), complemented with pointwise verifiable rubrics that act as both guardrails against degenerate behaviors and a source of verifiable reward for objective sub-tasks. Finally, we instantiate OpenRS as reward supervision in pairwise RL training.

判断：一次决定core：adaptive rubric/pairwise外聚合是否真有改变固定scalarization或可验证约束的目标差额；constitution+evolution+human refinement组合自身不够。

## 2602.14077 — GTS: Inference-Time Scaling of Latent Reasoning with a Learnable Gaussian Thought Sampler

原始身份：https://arxiv.org/abs/2602.14077v1；Submitted raw：2026-02-15T09:57:47Z，尚非公开时间。

Inference-time scaling (ITS) in latent reasoning models typically relies on heuristic perturbations, such as dropout or fixed Gaussian noise, to generate diverse candidate trajectories. However, we show that stronger perturbations do not necessarily yield better sampling quality: they often induce larger distribution shifts without producing more useful reasoning paths or better final decisions. A key limitation is that these perturbations inject stochasticity without defining an explicit conditional sampling distribution, making latent exploration difficult to control or optimize. To address this, we propose the Gaussian Thought Sampler (GTS), a lightweight module that reformulates latent exploration as sampling from a learned conditional distribution over continuous reasoning states. GTS predicts context-dependent perturbation distributions and is trained with GRPO-style policy optimization while keeping the backbone frozen, turning heuristic perturbation into an explicit probabilistic sampling policy. Experiments across multiple benchmarks and two latent reasoning architectures show that GTS yields more reliable inference-time scaling than heuristic baselines, suggesting that effective latent ITS requires better-controlled and optimizable sampling rather than simply amplifying stochasticity.

判断：拟入：heuristic latent噪声越强不等有效探索→context conditional Gaussian policy可优化且冻结backbone→控制sample分布而非加大扰动，成本/奖励归因待核。

## 实际exact-v1与逐身份日期补充

以上十个明确拟入的当前题摘已由作者逐一读精确v1完整题摘：13904 BODY:80–84、13935:83–86、13940:59–61、13942:81–85、13953:53–61、14027:91–94、14048:93–95、14050:54–58、14077:106–111；14041 HTML404后只一次PDF恢复，`V3_BODY_2602.14041.pdf.txt`:10–25。未出现改变上述具体准入入口的版本差，不采用后版机制。材料原文仅本日新raw，不继承旧正文判断。

每ID原DataCite JSON保留doi/url/title与精确v1 Submitted/Updated，Created和Registered未手改。Submitted均严格晚于Fri02/13 19Z，且不晚于Mon02/16 19Z；依同官方announcement/ID assignment规则，working first-public lower为Tue02/17 01Z，同identity公开Created秒bucket+1s为upper。不是Updated映射，不用邻ID批推；Available月份不用作公开日，後版本分离。北京时间下界均02/17 09:00，以下upper完全落窗。

| ID | v1 Submitted UTC | v1 Updated UTC（非first-public） | Created UTC | Registered UTC | working upper +08（不含） |
| --- | --- | --- | --- | --- | --- |
| 13904 | 02-14T21:53:47Z | 02-17T01:40:23Z | 02-17T04:03:05Z | 02-17T04:03:05Z | 02-17T12:03:06+08:00 |
| 13935 | 02-15T00:14:53Z | 02-17T01:42:24Z | 02-17T04:03:47Z | 02-17T04:03:48Z | 02-17T12:03:48+08:00 |
| 13940 | 02-15T00:31:24Z | 02-17T01:42:40Z | 02-17T04:03:54Z | 02-17T04:03:54Z | 02-17T12:03:55+08:00 |
| 13942 | 02-15T00:43:21Z | 02-17T01:42:49Z | 02-17T04:03:56Z | 02-17T04:03:57Z | 02-17T12:03:57+08:00 |
| 13953 | 02-15T01:48:10Z | 02-17T01:43:40Z | 02-17T04:04:12Z | 02-17T04:04:13Z | 02-17T12:04:13+08:00 |
| 14027 | 02-15T07:14:47Z | 02-17T01:48:34Z | 02-17T04:05:55Z | 02-17T04:05:56Z | 02-17T12:05:56+08:00 |
| 14041 | 02-15T08:09:05Z | 02-17T01:49:44Z | 02-17T04:06:15Z | 02-17T04:06:18Z | 02-17T12:06:16+08:00 |
| 14048 | 02-15T08:27:34Z | 02-17T01:50:16Z | 02-17T04:06:27Z | 02-17T04:06:28Z | 02-17T12:06:28+08:00 |
| 14050 | 02-15T08:32:22Z | 02-17T01:50:28Z | 02-17T04:06:30Z | 02-17T04:06:30Z | 02-17T12:06:31+08:00 |
| 14077 | 02-15T09:57:47Z | 02-17T01:52:04Z | 02-17T04:07:11Z | 02-17T04:07:12Z | 02-17T12:07:12+08:00 |

13832/13891/14069的一次core贡献关闭已由root实际核准，见TENTH；13851/13962明确题摘关闭仍保留原理由，不按领域或数量目标处理。
