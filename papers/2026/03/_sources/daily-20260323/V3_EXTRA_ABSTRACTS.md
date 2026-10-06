# 03/23：第二批 20 项完整官方 v1 题摘

本日独立四查询的有限题摘筛选，不是确定落窗或Evidence认证。API published/updated是Submitted身份，不当作公开时刻；当前header另核，无必要信号不展开版本差异。

查询：https://export.arxiv.org/api/query?id_list=2603.19375v1%2C2603.19470v1%2C2603.19688v1%2C2603.19733v1%2C2603.20101v1%2C2603.20320v1%2C2603.20122v1%2C2603.19954v1%2C2603.20100v1%2C2603.20161v1&max_results=10

## DataProphet: Demystifying Supervision Data Generalization in Multimodal LLMs

Primary: https://arxiv.org/abs/2603.19688v1

Conventional wisdom for selecting supervision data for multimodal large language models (MLLMs) is to prioritize datasets that appear similar to the target benchmark, such as text-intensive or vision-centric tasks. However, it remains unclear whether such intuitive similarity reliably predicts downstream performance gains. In this work, we take a first step toward answering a practical question: can we estimate the influence of a training dataset on a target benchmark before any training is performed? To investigate this question, we conduct an in-depth analysis of transfer across 14 vision-language datasets spanning 7 diverse tasks. Our results show that intuitive task similarity is an unreliable predictor of transferability, and that generalization depends more on the specific dataset than on its broad task category. Motivated by this finding, we propose DATAPROPHET, a simple and effective training-free metric that combines multimodal perplexity, similarity, and data diversity. Experiments show that DATAPROPHET produces supervision-data rankings that strongly correlate with rankings based on actual post-training performance gains, achieving a Kendall's tau of 86.0%. Moreover, DATAPROPHET enables better supervision-data selection, yielding up to 6.9% improvement over uniform selection, 1.4% over a state-of-the-art training-based baseline, and 0.2% above oracle selection based on experimental performance. Our code and data will be released.

Submitted原字段: 2026-03-20T06:42:26Z；API updated: 2026-03-20T06:42:26Z；Comments: 14 pages

## Evolving Jailbreaks: Automated Multi-Objective Long-Tail Attacks on Large Language Models

Primary: https://arxiv.org/abs/2603.20122v1

Large Language Models (LLMs) have been widely deployed, especially through free Web-based applications that expose them to diverse user-generated inputs, including those from long-tail distributions such as low-resource languages and encrypted private data. This open-ended exposure increases the risk of jailbreak attacks that undermine model safety alignment. While recent studies have shown that leveraging long-tail distributions can facilitate such jailbreaks, existing approaches largely rely on handcrafted rules, limiting the systematic evaluation of these security and privacy vulnerabilities. In this work, we present EvoJail, an automated framework for discovering long-tail distribution attacks via multi-objective evolutionary search. EvoJail formulates long-tail attack prompt generation as a multi-objective optimization problem that jointly maximizes attack effectiveness and minimizes output perplexity, and introduces a semantic-algorithmic solution representation to capture both high-level semantic intent and low-level structural transformations of encryption-decryption logic. Building upon this representation, EvoJail integrates LLM-assisted operators into a multi-objective evolutionary framework, enabling adaptive and semantically informed mutation and crossover for efficiently exploring a highly structured and open-ended search space. Extensive experiments demonstrate that EvoJail consistently discovers diverse and effective long-tail jailbreak strategies, achieving competitive performance with existing methods in both individual and ensemble level.

Submitted原字段: 2026-03-20T16:45:04Z；API updated: 2026-03-20T16:45:04Z；Comments: Not Disclosed

## Pitfalls in Evaluating Interpretability Agents

Primary: https://arxiv.org/abs/2603.20101v1

Automated interpretability systems aim to reduce the need for human labor and scale analysis to increasingly large models and diverse tasks. Recent efforts toward this goal leverage large language models (LLMs) at increasing levels of autonomy, ranging from fixed one-shot workflows to fully autonomous interpretability agents. This shift creates a corresponding need to scale evaluation approaches to keep pace with both the volume and complexity of generated explanations. We investigate this challenge in the context of automated circuit analysis -- explaining the roles of model components when performing specific tasks. To this end, we build an agentic system in which a research agent iteratively designs experiments and refines hypotheses. When evaluated against human expert explanations across six circuit analysis tasks in the literature, the system appears competitive. However, closer examination reveals several pitfalls of replication-based evaluation: human expert explanations can be subjective or incomplete, outcome-based comparisons obscure the research process, and LLM-based systems may reproduce published findings via memorization or informed guessing. To address some of these pitfalls, we propose an unsupervised intrinsic evaluation based on the functional interchangeability of model components. Our work demonstrates fundamental challenges in evaluating complex automated interpretability systems and reveals key limitations of replication-based evaluation.

Submitted原字段: 2026-03-20T16:27:17Z；API updated: 2026-03-20T16:27:17Z；Comments: Not Disclosed

## Semantic Token Clustering for Efficient Uncertainty Quantification in Large Language Models

Primary: https://arxiv.org/abs/2603.20161v1

Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks. However, the truthfulness of their outputs is not guaranteed, and their tendency toward overconfidence further limits reliability. Uncertainty quantification offers a promising way to identify potentially unreliable outputs, but most existing methods rely on repeated sampling or auxiliary models, introducing substantial computational overhead. To address these limitations, we propose Semantic Token Clustering (STC), an efficient uncertainty quantification method that leverages the semantic information inherently encoded in LLMs. Specifically, we group tokens into semantically consistent clusters using embedding clustering and prefix matching, and quantify uncertainty based on the probability mass aggregated over the corresponding semantic cluster. Our approach requires only a single generation and does not depend on auxiliary models. Experimental results show that STC achieves performance comparable to state-of-the-art baselines while substantially reducing computational overhead.

Submitted原字段: 2026-03-20T17:37:33Z；API updated: 2026-03-20T17:37:33Z；Comments: EACL 2026

## The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents

Primary: https://arxiv.org/abs/2603.20320v1

Large language models (LLMs) are increasingly deployed as agents with access to executable tools, enabling direct interaction with external systems. However, most safety evaluations remain text-centric and assume that compliant language implies safe behavior, an assumption that becomes unreliable once models are allowed to act. In this work, we empirically examine how executable tool affordance alters safety alignment in LLM agents using a paired evaluation framework that compares text-only chatbot behavior with tool-enabled agent behavior under identical prompts and policies. Experiments are conducted in a deterministic financial transaction environment with binary safety constraints across 1,500 procedurally generated scenarios. To separate intent from outcome, we distinguish between attempted and realized violations using dual enforcement regimes that either block or permit unsafe actions. Both evaluated models maintain perfect compliance in text-only settings, yet exhibit sharp increases in violations after tool access is introduced, reaching rates up to 85% despite unchanged rules. We observe substantial gaps between attempted and executed violations, indicating that external guardrails can suppress visible harm while masking persistent misalignment. Agents also develop spontaneous constraint circumvention strategies without adversarial prompting. These results demonstrate that tool affordance acts as a primary driver of safety misalignment and that text-based evaluation alone is insufficient for assessing agentic systems.

Submitted原字段: 2026-03-19T23:34:46Z；API updated: 2026-03-19T23:34:46Z；Comments: Not Disclosed

## Automated Membership Inference Attacks: Discovering MIA Signal Computations using LLM Agents

Primary: https://arxiv.org/abs/2603.19375v1

Membership inference attacks (MIAs), which enable adversaries to determine whether specific data points were part of a model's training dataset, have emerged as an important framework to understand, assess, and quantify the potential information leakage associated with machine learning systems. Designing effective MIAs is a challenging task that usually requires extensive manual exploration of model behaviors to identify potential vulnerabilities. In this paper, we introduce AutoMIA -- a novel framework that leverages large language model (LLM) agents to automate the design and implementation of new MIA signal computations. By utilizing LLM agents, we can systematically explore a vast space of potential attack strategies, enabling the discovery of novel strategies. Our experiments demonstrate AutoMIA can successfully discover new MIAs that are specifically tailored to user-configured target model and dataset, resulting in improvements of up to 0.18 in absolute AUC over existing MIAs. This work provides the first demonstration that LLM agents can serve as an effective and scalable paradigm for designing and implementing MIAs with SOTA performance, opening up new avenues for future exploration.

Submitted原字段: 2026-03-19T18:10:18Z；API updated: 2026-03-19T18:10:18Z；Comments: Not Disclosed

## Adaptive Layerwise Perturbation: Unifying Off-Policy Corrections for LLM RL

Primary: https://arxiv.org/abs/2603.19470v1

Off-policy problems such as policy staleness and training-inference mismatch, has become a major bottleneck for training stability and further exploration for LLM RL. To enhance inference efficiency, the distribution gap between the inference and updated policy grows, leading to heavy-tailed importance ratios. Heavy-tailed ratios arise when the policy is locally sharp, which further inflates sharp gradients and can push updates outside the trust region. To address this, we propose Adaptive Layerwise Perturbation(ALP) by injecting small learnable perturbations into input hidden states of each layer during updates, which is used as the numerator of the importance ratio against the unchanged inference policy in the objective. Intuitively, by adding controlled noise to intermediate representations, ALP prevents the updated policy from deviating too sharply from the inference policy, and enlarges the policy family to cover the inference policy family with mismatch noises. Hence, the flattened distribution can naturally tighten the updated and inference policy gap and reduce the tail of importance ratios, thus maintaining training stability. This is further validated empirically. Experiments on single-turn math and multi-turn tool-integrated reasoning tasks show that ALP not only improves final performance, but also avoid blow up of importance ratio tail and KL spikes during iterative training, along with boosted exploration. Ablations show that representation-level perturbations across all layers are most effective, substantially outperforming partial-layer and logits-only variants.

Submitted原字段: 2026-03-19T21:04:17Z；API updated: 2026-03-19T21:04:17Z；Comments: Not Disclosed

## An Empirical Study of SFT-DPO Interaction and Parameterization in Small Language Models

Primary: https://arxiv.org/abs/2603.20100v1

Direct Preference Optimization (DPO) is widely used after supervised fine-tuning (SFT) to align language models, yet empirical behavior under small backbones and modest data is under-specified. We systematically compare SFT-only, DPO-only, and staged SFT-to-DPO training alongside full fine-tuning (FFT) versus LoRA on a GPT-2-scale decoder, evaluating paraphrase detection and Shakespearean sonnet continuation. DPO yields small, task-dependent gains over strong SFT and can match competitive SFT accuracy without a warm start when the preference construction closely parallels the supervised objective. In contrast, parameterization dominates: FFT consistently outperforms LoRA at matched training depth, and LoRA does not reduce wall-clock time on our hardware. These findings indicate that, in this small-scale regime, supervised full-parameter adaptation remains the primary performance lever, while preference optimization and low-rank adaptation provide limited marginal returns.

Submitted原字段: 2026-03-20T16:27:03Z；API updated: 2026-03-20T16:27:03Z；Comments: Not Disclosed

## On the Ability of Transformers to Verify Plans

Primary: https://arxiv.org/abs/2603.19954v1

Transformers have shown inconsistent success in AI planning tasks, and theoretical understanding of when generalization should be expected has been limited. We take important steps towards addressing this gap by analyzing the ability of decoder-only models to verify whether a given plan correctly solves a given planning instance. To analyse the general setting where the number of objects -- and thus the effective input alphabet -- grows at test time, we introduce C*-RASP, an extension of C-RASP designed to establish length generalization guarantees for transformers under the simultaneous growth in sequence length and vocabulary size. Our results identify a large class of classical planning domains for which transformers can provably learn to verify long plans, and structural properties that significantly affects the learnability of length generalizable solutions. Empirical experiments corroborate our theory.

Submitted原字段: 2026-03-20T13:55:29Z；API updated: 2026-03-20T13:55:29Z；Comments: Not Disclosed

## PoC: Performance-oriented Context Compression for Large Language Models via Performance Prediction

Primary: https://arxiv.org/abs/2603.19733v1

While context compression can mitigate the growing inference costs of Large Language Models (LLMs) by shortening contexts, existing methods that specify a target compression ratio or length suffer from unpredictable performance degradation, hindering their reliable deployment. We introduce a paradigm shift to Performance-oriented Context Compression (PoC), where developers specify an acceptable performance floor instead of a compression ratio. PoC employs a lightweight performance predictor to automatically find the most aggressive compression ratio that satisfies this constraint before steering an off-the-shelf compressor. We design and compare two predictor variants: a simple context-agnostic predictor and a more sophisticated context-aware one that considers the input's inherent compressibility. On both question-answering and summarization benchmarks, the context-aware predictor consistently achieves lower performance prediction error than the context-agnostic predictor, while the resulting context-aware PoC attains a superior overall performance. Our work paves the way for a more reliable, efficient, and performance-aware deployment of context compression for LLMs.

Submitted原字段: 2026-03-20T08:18:46Z；API updated: 2026-03-20T08:18:46Z；Comments: Not Disclosed

查询：https://export.arxiv.org/api/query?id_list=2603.19807v1%2C2603.19939v1%2C2603.20155v1%2C2603.19790v1%2C2603.19708v1%2C2603.20340v1%2C2603.19595v1%2C2603.20336v1%2C2603.20075v1%2C2603.19681v1&max_results=10

## Timestep-Aware Block Masking for Efficient Diffusion Model Inference

Primary: https://arxiv.org/abs/2603.19939v1

Diffusion Probabilistic Models (DPMs) have achieved great success in image generation but suffer from high inference latency due to their iterative denoising nature. Motivated by the evolving feature dynamics across the denoising trajectory, we propose a novel framework to optimize the computational graph of pre-trained DPMs on a per-timestep basis. By learning timestep-specific masks, our method dynamically determines which blocks to execute or bypass through feature reuse at each inference stage. Unlike global optimization methods that incur prohibitive memory costs via full-chain backpropagation, our method optimizes masks for each timestep independently, ensuring a memory-efficient training process. To guide this process, we introduce a timestep-aware loss scaling mechanism that prioritizes feature fidelity during sensitive denoising phases, complemented by a knowledge-guided mask rectification strategy to prune redundant spatial-temporal dependencies. Our approach is architecture-agnostic and demonstrates significant efficiency gains across a broad spectrum of models, including DDPM, LDM, DiT, and PixArt. Experimental results show that by treating the denoising process as a sequence of optimized computational paths, our method achieves a superior balance between sampling speed and generative quality. Our code will be released.

Submitted原字段: 2026-03-20T13:35:03Z；API updated: 2026-03-20T13:35:03Z；Comments: 10 pages

## Enhancing Alignment for Unified Multimodal Models via Semantically-Grounded Supervision

Primary: https://arxiv.org/abs/2603.19807v1

Unified Multimodal Models (UMMs) have emerged as a promising paradigm that integrates multimodal understanding and generation within a unified modeling framework. However, current generative training paradigms suffer from inherent limitations. We present Semantically-Grounded Supervision (SeGroS), a fine-tuning framework designed to resolve the granularity mismatch and supervisory redundancy in UMMs. At its core, we propose a novel visual grounding map to construct two complementary supervision signals. First, we formulate semantic Visual Hints to compensate for the sparsity of text prompts. Second, we generate a semantically-grounded Corrupted Input to explicitly enhance the supervision of masking-based UMMs by restricting the reconstruction loss to core text-aligned regions. Extensive evaluations on GenEval, DPGBench, and CompBench demonstrate that SeGroS significantly improves generation fidelity and cross-modal alignment across various UMM architectures.

Submitted原字段: 2026-03-20T09:45:52Z；API updated: 2026-03-20T09:45:52Z；Comments: Not Disclosed

## All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution

Primary: https://arxiv.org/abs/2603.19595v1

Lifelong interactive agents are expected to assist users over months or years, which requires continually writing long term memories while retrieving the right evidence for each new query under fixed context and latency budgets. Existing memory systems often degrade as histories grow, yielding redundant, outdated, or noisy retrieved contexts. We present All-Mem, an online/offline lifelong memory framework that maintains a topology structured memory bank via explicit, non destructive consolidation, avoiding the irreversible information loss typical of summarization based compression. In online operation, it anchors retrieval on a bounded visible surface to keep coarse search cost bounded. Periodically offline, an LLM diagnoser proposes confidence scored topology edits executed with gating using three operators: SPLIT, MERGE, and UPDATE, while preserving immutable evidence for traceability. At query time, typed links enable hop bounded, budgeted expansion from active anchors to archived evidence when needed. Experiments on LOCOMO and LONGMEMEVAL show improved retrieval and QA over representative baselines.

Submitted原字段: 2026-03-20T03:14:40Z；API updated: 2026-03-20T03:14:40Z；Comments: Not Disclosed

## Unbiased Dynamic Multimodal Fusion

Primary: https://arxiv.org/abs/2603.19681v1

Traditional multimodal methods often assume static modality quality, which limits their adaptability in dynamic real-world scenarios. Thus, dynamical multimodal methods are proposed to assess modality quality and adjust their contribution accordingly. However, they typically rely on empirical metrics, failing to measure the modality quality when noise levels are extremely low or high. Moreover, existing methods usually assume that the initial contribution of each modality is the same, neglecting the intrinsic modality dependency bias. As a result, the modality hard to learn would be doubly penalized, and the performance of dynamical fusion could be inferior to that of static fusion. To address these challenges, we propose the Unbiased Dynamic Multimodal Learning (UDML) framework. Specifically, we introduce a noise-aware uncertainty estimator that adds controlled noise to the modality data and predicts its intensity from the modality feature. This forces the model to learn a clear correspondence between feature corruption and noise level, allowing accurate uncertainty measure across both low- and high-noise conditions. Furthermore, we quantify the inherent modality reliance bias within multimodal networks via modality dropout and incorporate it into the weighting mechanism. This eliminates the dual suppression effect on the hard-to-learn modality. Extensive experiments across diverse multimodal benchmark tasks validate the effectiveness, versatility, and generalizability of the proposed UDML. The code is available at https://github.com/shicaiwei123/UDML.

Submitted原字段: 2026-03-20T06:29:59Z；API updated: 2026-03-20T06:29:59Z；Comments: CVPR2026 Findings, 11 pages, 4 figures

## From Plausibility to Verifiability: Risk-Controlled Generative OCR for Vision-Language Models

Primary: https://arxiv.org/abs/2603.19790v1

Modern vision-language models (VLMs) can act as generative OCR engines, yet open-ended decoding can expose rare but consequential failures. We identify a core deployment misalignment in generative OCR. Autoregressive decoding favors semantic plausibility, whereas OCR requires outputs that are visually grounded and geometrically verifiable. This mismatch produces severe errors, especially over-generation and unsupported substitutions, creating deployment risk even when benchmark accuracy remains high. We therefore formulate frozen VLM OCR as a selective accept/abstain problem and propose a model-agnostic Geometric Risk Controller. The controller probes multiple structured views of the same input, applies lightweight structural screening, and accepts a transcription only when cross-view consensus and stability satisfy predefined criteria, yielding a small family of operating points. Experiments on frozen VLM backbones and standard OCR benchmarks show consistent reductions in extreme-error risk and catastrophic over-generation at predictable coverage costs. Reliable deployment of generative OCR with frozen VLMs benefits from explicit system-level risk control rather than unconstrained generation.

Submitted原字段: 2026-03-20T09:28:09Z；API updated: 2026-03-20T09:28:09Z；Comments: 10 pages, 5 figures, 5 tables

## Agentic Harness for Real-World Compilers

Primary: https://arxiv.org/abs/2603.20075v1

Compilers are critical to modern computing, yet fixing compiler bugs is difficult. While recent large language model (LLM) advancements enable automated bug repair, compiler bugs pose unique challenges due to their complexity, deep cross-domain expertise requirements, and sparse, non-descriptive bug reports, necessitating compiler-specific tools. To bridge the gap, we introduce llvm-autofix, the first agentic harness designed to assist LLM agents in understanding and fixing compiler bugs. Our focus is on LLVM, one of the most widely used compiler infrastructures. Central to llvm-autofix are agent-friendly LLVM tools, a benchmark llvm-bench of reproducible LLVM bugs, and a tailored minimal agent llvm-autofix-mini for fixing LLVM bugs. Our evaluation demonstrates a performance decline of 60% in frontier models when tackling compiler bugs compared with common software bugs. Our minimal agent llvm-autofix-mini also outperforms the state-of-the-art by approximately 22%. This emphasizes the necessity for specialized harnesses like ours to close the loop between LLMs and compiler engineering. We believe this work establishes a foundation for advancing LLM capabilities in complex systems like compilers. GitHub: https://github.com/dtcxzyw/llvm-autofix

Submitted原字段: 2026-03-20T15:56:43Z；API updated: 2026-03-20T15:56:43Z；Comments: Not Disclosed

## ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents

Primary: https://arxiv.org/abs/2603.20340v1

Despite rapid progress in multimodal GUI agents, reusable skill acquisition remains difficult because on-demand generated skills often leave action semantics, state assumptions, and success criteria implicit. This makes them brittle to execution errors, hard to verify, and difficult to repair. We present ContractSkill, a framework that converts a draft skill into a contracted executable artifact with explicit preconditions, step specifications, postconditions, recovery rules, and termination checks. This representation enables deterministic verification, step-level fault localization, and minimal patch-based repair, turning skill refinement into localized editing rather than full regeneration. Experiments on VisualWebArena and MiniWoB with GLM-4.6V and Qwen3.5-Plus show that ContractSkill improves self-generated skills from 9.4% and 10.9% to 28.1% and 37.5% on VisualWebArena, and from 66.5% and 60.5% to 77.5% and 81.0% on MiniWoB. Repaired artifacts also transfer across models, improving the target model's self-generated-skill baseline by up to 47.8 points and 12.8 points on the two benchmarks, respectively. These results suggest that agent skills are better treated as explicit procedural artifacts that can be verified, repaired, and shared across models.

Submitted原字段: 2026-03-20T09:25:50Z；API updated: 2026-03-20T09:25:50Z；Comments: 10 pages, 4 figures, 6 tables

## WorldAgents: Can Foundation Image Models be Agents for 3D World Models?

Primary: https://arxiv.org/abs/2603.19708v1

Given the remarkable ability of 2D foundation image models to generate high-fidelity outputs, we investigate a fundamental question: do 2D foundation image models inherently possess 3D world model capabilities? To answer this, we systematically evaluate multiple state-of-the-art image generation models and Vision-Language Models (VLMs) on the task of 3D world synthesis. To harness and benchmark their potential implicit 3D capability, we propose an agentic framing to facilitate 3D world generation. Our approach employs a multi-agent architecture: a VLM-based director that formulates prompts to guide image synthesis, a generator that synthesizes new image views, and a VLM-backed two-step verifier that evaluates and selectively curates generated frames from both 2D image and 3D reconstruction space. Crucially, we demonstrate that our agentic approach provides coherent and robust 3D reconstruction, producing output scenes that can be explored by rendering novel views. Through extensive experiments across various foundation models, we demonstrate that 2D models do indeed encapsulate a grasp of 3D worlds. By exploiting this understanding, our method successfully synthesizes expansive, realistic, and 3D-consistent worlds.

Submitted原字段: 2026-03-20T07:22:41Z；API updated: 2026-03-20T07:22:41Z；Comments: Webpage: https://ziyaerkoc.com/worldagents/ Video: https://www.youtube.com/watch?v=Mj2FqqhurdI

## Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD

Primary: https://arxiv.org/abs/2603.20155v1

It is currently difficult to distill discrete diffusion models. In contrast, continuous diffusion literature has many distillation approaches methods that can reduce sampling steps to a handful. Our method, Discrete Moment Matching Distillation (D-MMD), leverages ideas that have been highly successful in the continuous domain. Whereas previous discrete distillation methods collapse, D-MMD maintains high quality and diversity (given sufficient sampling steps). This is demonstrated on both text and image datasets. Moreover, the newly distilled generators can outperform their teachers.

Submitted原字段: 2026-03-20T17:29:12Z；API updated: 2026-03-20T17:29:12Z；Comments: Not Disclosed

## GEM: A Native Graph-based Index for Multi-Vector Retrieval

Primary: https://arxiv.org/abs/2603.20336v1

In multi-vector retrieval, both queries and data are represented as sets of high-dimensional vectors, enabling finer-grained semantic matching and improving retrieval quality over single-vector approaches. However, its practical adoption is held back by the lack of effective indexing algorithms. Existing work, attempting to reuse standard single-vector indexes, often fails to preserve multi-vector semantics or remains slow. In this work, we present GEM, a native indexing framework for multi-vector representations. The core idea is to construct a proximity graph directly over vector sets, preserving their fine-grained semantics while enabling efficient navigation. First, GEM designs a set-level clustering scheme. It associates each vector set with only its most informative clusters, effectively reducing redundancy without hurting semantic coverage. Then, it builds local proximity graphs within clusters and bridges them into a globally navigable structure. To handle the non-metric nature of multi-vector similarity, GEM decouples the graph construction metric from the final relevance score and injects semantic shortcuts to guide efficient navigation toward relevant regions. At query time, GEM launches beam search from multiple entry points and prunes paths early using cluster cues. To further enhance efficiency, a quantized distance estimation technique is used for both indexing and search. Across in-domain, out-of-domain, and multi-modal benchmarks, GEM achieves up to 16x speedup over state-of-the-art methods while matching or improving accuracy.

Submitted原字段: 2026-03-20T08:44:21Z；API updated: 2026-03-20T08:44:21Z；Comments: This paper has been accepted by SIGMOD 2026

