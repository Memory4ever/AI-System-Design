# 2026-02-17 原始主题题摘切片

原始来源：本日 inventory.json 的身份/题摘字段，仅作发现原证重用。旧评分、日期推定、候选池、全量关闭与完成声明一律未采用。92 条术语查漏命中与49条语义标题补检去重为 139 身份；逐项完整题摘已读，范围与贡献判断见 V3_SCREENING.md。复制题摘不证明精确v1或首次公开。

## 2602.12284

[A Lightweight LLM Framework for Disaster Humanitarian Information Classification](https://arxiv.org/abs/2602.12284v1)

Timely classification of humanitarian information from social media is critical for effective disaster response. However, deploying large language models (LLMs) for this task faces challenges in resource-constrained emergency settings. This paper develops a lightweight, cost-effective framework for disaster tweet classification using parameter-efficient fine-tuning. We construct a unified experimental corpus by integrating and normalizing the HumAID dataset (76,484 tweets across 19 disaster events) into a dual-task benchmark: humanitarian information categorization and event type identification. Through systematic evaluation of prompting strategies, LoRA fine-tuning, and retrieval-augmented generation (RAG) on Llama 3.1 8B, we demonstrate that: (1) LoRA achieves 79.62% humanitarian classification accuracy (+37.79% over zero-shot) while training only ~2% of parameters; (2) QLoRA enables efficient deployment with 99.4% of LoRA performance at 50% memory cost; (3) contrary to common assumptions, RAG strategies degrade fine-tuned model performance due to label noise from retrieved examples. These findings establish a practical, reproducible pipeline for building reliable crisis intelligence systems with limited computational resources.

Submitted:v1（仅身份线索，不作公开日期）：2026-01-21T02:05:25Z。旧 registry Updated:v1：2026-02-16T01:00:08Z（不作首公开）。

## 2602.12285

[From Biased Chatbots to Biased Agents: Examining Role Assignment Effects on LLM Agent Robustness](https://arxiv.org/abs/2602.12285v1)

Large Language Models (LLMs) are increasingly deployed as autonomous agents capable of actions with real-world impacts beyond text generation. While persona-induced biases in text generation are well documented, their effects on agent task performance remain largely unexplored, even though such effects pose more direct operational risks. In this work, we present the first systematic case study showing that demographic-based persona assignments can alter LLM agents' behavior and degrade performance across diverse domains. Evaluating widely deployed models on agentic benchmarks spanning strategic reasoning, planning, and technical operations, we uncover substantial performance variations - up to 26.2% degradation, driven by task-irrelevant persona cues. These shifts appear across task types and model architectures, indicating that persona conditioning and simple prompt injections can distort an agent's decision-making reliability. Our findings reveal an overlooked vulnerability in current LLM agentic systems: persona assignments can introduce implicit biases and increase behavioral volatility, raising concerns for the safe and robust deployment of LLM agents.

Submitted:v1（仅身份线索，不作公开日期）：2026-01-21T02:43:07Z。旧 registry Updated:v1：2026-02-16T01:00:11Z（不作首公开）。

## 2602.12286

[Mind the Gap No More: Achieving Zero-Gap Multimodal Integration via One Tokenizer](https://arxiv.org/abs/2602.12286v1)

A central challenge in developing Multimodal Large Language Models (MLLMs) is effectively integrating heterogeneous inputs into a cohesive reasoning engine. Current paradigms predominantly rely on modular architectures that introduce modality-specific encoders and cross-modal fusion mechanisms. However, these designs are fundamentally bottlenecked by a geometric modality gap, forcing the LLM to expend significant computational capacity on geometric reconciliation rather than deep cross-modal reasoning. In this work, we formally characterize this modality gap and theoretically demonstrate that native architectures, specifically those employing a unified vocabulary, intrinsically maintain a zero-gap state across all hidden layers. Guided by these theoretical findings, we propose \textit{One Tokenizer}, a native architecture that maps all modalities directly into a shared token space. We empirically validate this framework on a DNA--text multimodal testbed. Our extensive evaluations reveal that by achieving seamless integration within the LLM's native latent space, One Tokenizer consistently outperforms encoder-based modular counterparts, providing a fundamentally superior framework for deep biological reasoning.

Submitted:v1（仅身份线索，不作公开日期）：2026-01-21T07:46:36Z。旧 registry Updated:v1：2026-02-16T01:00:13Z（不作首公开）。

## 2602.12293

[Real-Time Dynamic N-1 Screening: Identifying High-Risk Lines and Transformers After Common Faults](https://arxiv.org/abs/2602.12293v1)

Power system operators routinely perform N-1 contingency analysis, yet conventional tools provide limited guidance on which lines or transformers deserve heightened attention during fast post-fault transients. In particular, static screening does not reveal whether (1) the same faulted line repeatedly triggers severe downstream overloads, or (2) a specific transformer emerges as vulnerable across many distinct fault scenarios. This paper introduces a real-time dynamic N-1 screening framework that addresses this gap by estimating, for each counterfactual single-phase transmission fault, the probability of transient overcurrent on critical grid elements. The output is an operator-facing dashboard that ranks (a) faulted lines whose outages most frequently lead to dangerous transformer overloads, and (b) transformers that consistently overload across top-risk scenarios, both of which are actionable indicators for real-time situational awareness. The approach models post-fault electromechanical dynamics using a linear stochastic formulation of the swing equations with short-lived, fault-localized uncertainty, and combines analytic transient evaluation with cross-entropy based importance sampling to efficiently estimate rare but high-impact events. All N-1 contingencies are evaluated in parallel with linear computational complexity. The framework is demonstrated on the IEEE 118-bus system, where it reveals latent high-risk lines and transformers that remain invisible under deterministic dynamic or static N-1 analysis. Results show orders-of-magnitude computational speedup relative to brute-force Monte Carlo, enabling practical deployment within real-time operational cycles.

Submitted:v1（仅身份线索，不作公开日期）：2026-01-31T18:36:39Z。旧 registry Updated:v1：2026-02-16T01:00:27Z（不作首公开）。

## 2602.12295

[Design Environment of Quantization-Aware Edge AI Hardware for Few-Shot Learning](https://arxiv.org/abs/2602.12295v1)

This study aims to ensure consistency in accuracy throughout the entire design flow in the implementation of edge AI hardware for few-shot learning, by implementing fixed-point data processing in the pre-training and evaluation phases. Specifically, the quantization module, called Brevitas, is applied to implement fixed-point data processing, which allows for arbitrary specification of the bit widths for the integer and fractional parts. Two methods of fixed-point data quantization, quantization-aware training (QAT) and post-training quantization (PTQ), are utilized in Brevitas. With Tensil, which is used in the current design flow, the bit widths of the integer and fractional parts need to be 8 bits each or 16 bits each when implemented in hardware, but performance validation has shown that accuracy comparable to floating-point operations can be maintained even with 6 bits or 5 bits each, indicating potential for further reduction in computational resources. These results clearly contribute to the creation of a versatile design and evaluation environment for edge AI hardware for few-shot learning.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-01T00:26:56Z。旧 registry Updated:v1：2026-02-16T01:00:31Z（不作首公开）。

## 2602.12302

[Grandes Modelos de Linguagem Multimodais (MLLMs): Da Teoria à Prática](https://arxiv.org/abs/2602.12302v1)

Multimodal Large Language Models (MLLMs) combine the natural language understanding and generation capabilities of LLMs with perception skills in modalities such as image and audio, representing a key advancement in contemporary AI. This chapter presents the main fundamentals of MLLMs and emblematic models. Practical techniques for preprocessing, prompt engineering, and building multimodal pipelines with LangChain and LangGraph are also explored. For further practical study, supplementary material is publicly available online: https://github.com/neemiasbsilva/MLLMs-Teoria-e-Pratica. Finally, the chapter discusses the challenges and highlights promising trends.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-11T17:30:22Z。旧 registry Updated:v1：2026-02-16T01:00:40Z（不作首公开）。

## 2602.12305

[OptiML: An End-to-End Framework for Program Synthesis and CUDA Kernel Optimization](https://arxiv.org/abs/2602.12305v1)

Generating high-performance CUDA kernels remains challenging due to the need to navigate a combinatorial space of low-level transformations under noisy and expensive hardware feedback. Although large language models can synthesize functionally correct CUDA code, achieving competitive performance requires systematic exploration and verification of optimization choices. We present OptiML, an end-to-end framework that maps either natural-language intent or input CUDA code to performance-optimized CUDA kernels by formulating kernel optimization as search under verification. OptiML consists of two decoupled stages. When the input is natural language, a Mixture-of-Thoughts generator (OptiML-G) acts as a proposal policy over kernel implementation strategies, producing an initial executable program. A search-based optimizer (OptiML-X) then refines either synthesized or user-provided kernels using Monte Carlo Tree Search over LLM-driven edits, guided by a hardware-aware reward derived from profiler feedback. Each candidate transformation is compiled, verified, and profiled with Nsight Compute, and evaluated by a composite objective that combines runtime with hardware bottleneck proxies and guardrails against regressions. We evaluate OptiML in both synthesis-and-optimize and optimization-only settings on a diverse suite of CUDA kernels. Results show that OptiML consistently discovers verified performance improvements over strong LLM baselines and produces interpretable optimization trajectories grounded in profiler evidence.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T04:50:19Z。旧 registry Updated:v1：2026-02-16T01:00:46Z（不作首公开）。

## 2602.12311

[Perceptual Self-Reflection in Agentic Physics Simulation Code Generation](https://arxiv.org/abs/2602.12311v1)

We present a multi-agent framework for generating physics simulation code from natural language descriptions, featuring a novel perceptual self-reflection mechanism for validation. The system employs four specialized agents: a natural language interpreter that converts user requests into physics-based descriptions; a technical requirements generator that produces scaled simulation parameters; a physics code generator with automated self-correction; and a physics validator that implements perceptual self-reflection. The key innovation is perceptual validation, which analyzes rendered animation frames using a vision-capable language model rather than inspecting code structure directly. This approach addresses the ``oracle gap'' where syntactically correct code produces physically incorrect behavior--a limitation that conventional testing cannot detect. We evaluate the system across seven domains including classical mechanics, fluid dynamics, thermodynamics, electromagnetics, wave physics, reaction-diffusion systems, and non-physics data visualization. The perceptual self-reflection architecture demonstrates substantial improvement over single-shot generation baselines, with the majority of tested scenarios achieving target physics accuracy thresholds. The system exhibits robust pipeline stability with consistent code self-correction capability, operating at approximately \$0.20 per animation. These results validate our hypothesis that feeding visual simulation outputs back to a vision-language model for iterative refinement significantly outperforms single-shot code generation for physics simulation tasks and highlights the potential of agentic AI to support engineering workflows and physics data generation pipelines.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T15:48:33Z。旧 registry Updated:v1：2026-02-16T01:00:54Z（不作首公开）。

## 2602.12314

[LatentAM: Real-Time, Large-Scale Latent Gaussian Attention Mapping via Online Dictionary Learning](https://arxiv.org/abs/2602.12314v1)

We present LatentAM, an online 3D Gaussian Splatting (3DGS) mapping framework that builds scalable latent feature maps from streaming RGB-D observations for open-vocabulary robotic perception. Instead of distilling high-dimensional Vision-Language Model (VLM) embeddings using model-specific decoders, LatentAM proposes an online dictionary learning approach that is both model-agnostic and pretraining-free, enabling plug-and-play integration with different VLMs at test time. Specifically, our approach associates each Gaussian primitive with a compact query vector that can be converted into approximate VLM embeddings using an attention mechanism with a learnable dictionary. The dictionary is initialized efficiently from streaming observations and optimized online to adapt to evolving scene semantics under trust-region regularization. To scale to long trajectories and large environments, we further propose an efficient map management strategy based on voxel hashing, where optimization is restricted to an active local map on the GPU, while the global map is stored and indexed on the CPU to maintain bounded GPU memory usage. Experiments on public benchmarks and a large-scale custom dataset demonstrate that LatentAM attains significantly better feature reconstruction fidelity compared to state-of-the-art methods, while achieving near-real-time speed (12-35 FPS) on the evaluated datasets. Our project page, including the code, is available at: https://junwoonlee.github.io/projects/LatentAM

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T17:25:00Z。旧 registry Updated:v1：2026-02-16T01:01:14Z（不作首公开）。

## 2602.12315

[AgenticShop: Benchmarking Agentic Product Curation for Personalized Web Shopping](https://arxiv.org/abs/2602.12315v1)

The proliferation of e-commerce has made web shopping platforms key gateways for customers navigating the vast digital marketplace. Yet this rapid expansion has led to a noisy and fragmented information environment, increasing cognitive burden as shoppers explore and purchase products online. With promising potential to alleviate this challenge, agentic systems have garnered growing attention for automating user-side tasks in web shopping. Despite significant advancements, existing benchmarks fail to comprehensively evaluate how well agentic systems can curate products in open-web settings. Specifically, they have limited coverage of shopping scenarios, focusing only on simplified single-platform lookups rather than exploratory search. Moreover, they overlook personalization in evaluation, leaving unclear whether agents can adapt to diverse user preferences in realistic shopping contexts. To address this gap, we present AgenticShop, the first benchmark for evaluating agentic systems on personalized product curation in open-web environment. Crucially, our approach features realistic shopping scenarios, diverse user profiles, and a verifiable, checklist-driven personalization evaluation framework. Through extensive experiments, we demonstrate that current agentic systems remain largely insufficient, emphasizing the need for user-side systems that effectively curate tailored products across the modern web.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T17:25:45Z。旧 registry Updated:v1：2026-02-16T01:01:15Z（不作首公开）。

## 2602.12322

[ForeAct: Steering Your VLA with Efficient Visual Foresight Planning](https://arxiv.org/abs/2602.12322v1)

Vision-Language-Action (VLA) models convert high-level language instructions into concrete, executable actions, a task that is especially challenging in open-world environments. We present Visual Foresight Planning (ForeAct), a general and efficient planner that guides a VLA step-by-step using imagined future observations and subtask descriptions. With an imagined future observation, the VLA can focus on visuo-motor inference rather than high-level semantic reasoning, leading to improved accuracy and generalization. Our planner comprises a highly efficient foresight image generation module that predicts a high-quality 640$\times$480 future observation from the current visual input and language instruction within only 0.33s on an H100 GPU, together with a vision-language model that reasons over the task and produces subtask descriptions for both the generator and the VLA. Importantly, state-of-the-art VLAs can integrate our planner seamlessly by simply augmenting their visual inputs, without any architectural modification. The foresight generator is pretrained on over 1 million multi-task, cross-embodiment episodes, enabling it to learn robust embodied dynamics. We evaluate our framework on a benchmark that consists of 11 diverse, multi-step real-world tasks. It achieves an average success rate of 87.4%, demonstrating a +40.9% absolute improvement over the $π_0$ baseline (46.5%) and a +30.3% absolute improvement over $π_0$ augmented with textual subtask guidance (57.1%).

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T18:56:27Z。旧 registry Updated:v1：2026-02-16T01:01:33Z（不作首公开）。

## 2602.12323

[The Appeal and Reality of Recycling LoRAs with Adaptive Merging](https://arxiv.org/abs/2602.12323v1)

The widespread availability of fine-tuned LoRA modules for open pre-trained models has led to an interest in methods that can adaptively merge LoRAs to improve performance. These methods typically include some way of selecting LoRAs from a pool and tune merging coefficients based on a task-specific dataset. While adaptive merging methods have demonstrated improvements in some settings, no past work has attempted to recycle LoRAs found "in the wild" on model repositories like the Hugging Face Hub. To address this gap, we consider recycling from a pool of nearly 1,000 user-contributed LoRAs trained from the Llama 3.1 8B-Instruct language model. Our empirical study includes a range of adaptive and non-adaptive merging methods in addition to a new method designed via a wide search over the methodological design space. We demonstrate that adaptive merging methods can improve performance over the base model but provide limited benefit over training a new LoRA on the same data used to set merging coefficients. We additionally find not only that the specific choice of LoRAs to merge has little importance, but that using LoRAs with randomly initialized parameter values yields similar performance. This raises the possibility that adaptive merging from recycled LoRAs primarily works via some kind of regularization effect, rather than by enabling positive cross-task transfer. To better understand why past work has proven successful, we confirm that positive transfer is indeed possible when there are highly relevant LoRAs in the pool. We release the model checkpoints and code online.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T18:59:20Z。旧 registry Updated:v1：2026-02-16T01:01:36Z（不作首公开）。

## 2602.12338

[Wireless TokenCom: RL-Based Tokenizer Agreement for Multi-User Wireless Token Communications](https://arxiv.org/abs/2602.12338v1)

Token Communications (TokenCom) has recently emerged as an effective new paradigm, where tokens are the unified units of multimodal communications and computations, enabling efficient digital semantic- and goal-oriented communications in future wireless networks. To establish a shared semantic latent space, the transmitters/receivers in TokenCom need to agree on an identical tokenizer model and codebook. To this end, an initial Tokenizer Agreement (TA) process is carried out in each communication episode, where the transmitter/receiver cooperate to choose from a set of pre-trained tokenizer models/ codebooks available to them both for efficient TokenCom. In this correspondence, we investigate TA in a multi-user downlink wireless TokenCom scenario, where the base station equipped with multiple antennas transmits video token streams to multiple users. We formulate the corresponding mixed-integer non-convex problem, and propose a hybrid reinforcement learning (RL) framework that integrates a deep Q-network (DQN) for joint tokenizer agreement and sub-channel assignment, with a deep deterministic policy gradient (DDPG) for beamforming. Simulation results show that the proposed framework outperforms baseline methods in terms of semantic quality and resource efficiency, while reducing the freezing events in video transmission by 68% compared to the conventional H.265-based scheme.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T19:00:33Z。旧 registry Updated:v1：2026-02-16T01:01:56Z（不作首公开）。

## 2602.12342

[Intrinsic Credit Assignment for Long Horizon Interaction](https://arxiv.org/abs/2602.12342v1)

How can we train agents to navigate uncertainty over long horizons? In this work, we propose ΔBelief-RL, which leverages a language model's own intrinsic beliefs to reward intermediate progress. Our method utilizes the change in the probability an agent assigns to the target solution for credit assignment. By training on synthetic interaction data, ΔBelief-RL teaches information-seeking capabilities that consistently outperform purely outcome-based rewards for Reinforcement Learning, with improvements generalizing to out-of-distribution applications ranging from customer service to personalization. Notably, the performance continues to improve as we scale test-time interactions beyond the training horizon, with interaction-efficiency increasing even on Pass@k metrics. Overall, our work introduces a scalable training strategy for navigating uncertainty over a long-horizon, by enabling credit assignment to intermediate actions via intrinsic ΔBelief rewards.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T19:00:54Z。旧 registry Updated:v1：2026-02-16T01:02:02Z（不作首公开）。

## 2602.12351

[LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation](https://arxiv.org/abs/2602.12351v1)

This paper develops LongNav-R1, an end-to-end multi-turn reinforcement learning (RL) framework designed to optimize Visual-Language-Action (VLA) models for long-horizon navigation. Unlike existing single-turn paradigm, LongNav-R1 reformulates the navigation decision process as a continuous multi-turn conversation between the VLA policy and the embodied environment. This multi-turn RL framework offers two distinct advantages: i) it enables the agent to reason about the causal effects of historical interactions and sequential future outcomes; and ii) it allows the model to learn directly from online interactions, fostering diverse trajectory generation and avoiding the behavioral rigidity often imposed by human demonstrations. Furthermore, we introduce Horizon-Adaptive Policy Optimization. This mechanism explicitly accounts for varying horizon lengths during advantage estimation, facilitating accurate temporal credit assignment over extended sequences. Consequently, the agent develops diverse navigation behaviors and resists collapse during long-horizon tasks. Experiments on object navigation benchmarks validate the framework's efficacy: With 4,000 rollout trajectories, LongNav-R1 boosts the Qwen3-VL-2B success rate from 64.3% to 73.0%. These results demonstrate superior sample efficiency and significantly outperform state-of-the-art methods. The model's generalizability and robustness are further validated by its zero-shot performance in long-horizon real-world navigation settings. All source code will be open-sourced upon publication.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T19:22:52Z。旧 registry Updated:v1：2026-02-16T01:02:55Z（不作首公开）。

## 2602.12370

[LLaMo: Scaling Pretrained Language Models for Unified Motion Understanding and Generation with Continuous Autoregressive Tokens](https://arxiv.org/abs/2602.12370v1)

Recent progress in large models has led to significant advances in unified multimodal generation and understanding. However, the development of models that unify motion-language generation and understanding remains largely underexplored. Existing approaches often fine-tune large language models (LLMs) on paired motion-text data, which can result in catastrophic forgetting of linguistic capabilities due to the limited scale of available text-motion pairs. Furthermore, prior methods typically convert motion into discrete representations via quantization to integrate with language models, introducing substantial jitter artifacts from discrete tokenization. To address these challenges, we propose LLaMo, a unified framework that extends pretrained LLMs through a modality-specific Mixture-of-Transformers (MoT) architecture. This design inherently preserves the language understanding of the base model while enabling scalable multimodal adaptation. We encode human motion into a causal continuous latent space and maintain the next-token prediction paradigm in the decoder-only backbone through a lightweight flow-matching head, allowing for streaming motion generation in real-time (&gt;30 FPS). Leveraging the comprehensive language understanding of pretrained LLMs and large-scale motion-text pretraining, our experiments demonstrate that LLaMo achieves high-fidelity text-to-motion generation and motion-to-text captioning in general settings, especially zero-shot motion generation, marking a significant step towards a general unified motion-language large model.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:02:21Z。旧 registry Updated:v1：2026-02-16T01:04:18Z（不作首公开）。

## 2602.12380

[TFT-ACB-XML: Decision-Level Integration of Customized Temporal Fusion Transformer and Attention-BiLSTM with XGBoost Meta-Learner for BTC Price Forecasting](https://arxiv.org/abs/2602.12380v1)

Accurate forecasting of Bitcoin (BTC) has always been a challenge because decentralized markets are non-linear, highly volatile, and have temporal irregularities. Existing deep learning models often struggle with interpretability and generalization across diverse market conditions. This research presents a hybrid stacked-generalization framework, TFT-ACB-XML, for BTC closing price prediction. The framework integrates two parallel base learners: a customized Temporal Fusion Transformer (TFT) and an Attention-Customized Bidirectional Long Short-Term Memory network (ACB), followed by an XGBoost regressor as the meta-learner. The customized TFT model handles long-range dependencies and global temporal dynamics via variable selection networks and interpretable single-head attention. The ACB module uses a new attention mechanism alongside the customized BiLSTM to capture short-term sequential dependencies. Predictions from both customized TFT and ACB are weighted through an error-reciprocal weighting strategy. These weights are derived from validation performance, where a model showing lower prediction error receives a higher weight. Finally, the framework concatenates these weighted outputs into a feature vector and feeds the vector to an XGBoost regressor, which captures non-linear residuals and produces the final BTC closing price prediction. Empirical validation using BTC data from October 1, 2014, to January 5, 2026, shows improved performance of the proposed framework compared to recent Deep Learning and Transformer baseline models. The results show a MAPE of 0.65%, an MAE of 198.15, and an RMSE of 258.30 for one-step-ahead out-of-sample under a walk-forward evaluation on the test block. The evaluation period spans the 2024 BTC halving and the spot ETFs (exchange-traded funds) period, which coincide with major liquidity and volatility shifts.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:20:56Z。旧 registry Updated:v1：2026-02-16T01:04:51Z（不作首公开）。

## 2602.12384

[Why Deep Jacobian Spectra Separate: Depth-Induced Scaling and Singular-Vector Alignment](https://arxiv.org/abs/2602.12384v1)

Understanding why gradient-based training in deep networks exhibits strong implicit bias remains challenging, in part because tractable singular-value dynamics are typically available only for balanced deep linear models. We propose an alternative route based on two theoretically grounded and empirically testable signatures of deep Jacobians: depth-induced exponential scaling of ordered singular values and strong spectral separation. Adopting a fixed-gates view of piecewise-linear networks, where Jacobians reduce to products of masked linear maps within a single activation region, we prove the existence of Lyapunov exponents governing the top singular values at initialization, give closed-form expressions in a tractable masked model, and quantify finite-depth corrections. We further show that sufficiently strong separation forces singular-vector alignment in matrix products, yielding an approximately shared singular basis for intermediate Jacobians. Together, these results motivate an approximation regime in which singular-value dynamics become effectively decoupled, mirroring classical balanced deep-linear analyses without requiring balancing. Experiments in fixed-gates settings validate the predicted scaling, alignment, and resulting dynamics, supporting a mechanistic account of emergent low-rank Jacobian structure as a driver of implicit bias.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:27:59Z。旧 registry Updated:v1：2026-02-16T01:05:19Z（不作首公开）。

## 2602.12390

[Rational Neural Networks have Expressivity Advantages](https://arxiv.org/abs/2602.12390v1)

We study neural networks with trainable low-degree rational activation functions and show that they are more expressive and parameter-efficient than modern piecewise-linear and smooth activations such as ELU, LeakyReLU, LogSigmoid, PReLU, ReLU, SELU, CELU, Sigmoid, SiLU, Mish, Softplus, Tanh, Softmin, Softmax, and LogSoftmax. For an error target of $\varepsilon&gt;0$, we establish approximation-theoretic separations: Any network built from standard fixed activations can be uniformly approximated on compact domains by a rational-activation network with only $\mathrm{poly}(\log\log(1/\varepsilon))$ overhead in size, while the converse provably requires $Ω(\log(1/\varepsilon))$ parameters in the worst case. This exponential gap persists at the level of full networks and extends to gated activations and transformer-style nonlinearities. In practice, rational activations integrate seamlessly into standard architectures and training pipelines, allowing rationals to match or outperform fixed activations under identical architectures and optimizers.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:33:42Z。旧 registry Updated:v1：2026-02-16T01:05:32Z（不作首公开）。

## 2602.12393

[Reproducing DragDiffusion: Interactive Point-Based Editing with Diffusion Models](https://arxiv.org/abs/2602.12393v1)

DragDiffusion is a diffusion-based method for interactive point-based image editing that enables users to manipulate images by directly dragging selected points. The method claims that accurate spatial control can be achieved by optimizing a single diffusion latent at an intermediate timestep, together with identity-preserving fine-tuning and spatial regularization. This work presents a reproducibility study of DragDiffusion using the authors' released implementation and the DragBench benchmark. We reproduce the main ablation studies on diffusion timestep selection, LoRA-based fine-tuning, mask regularization strength, and UNet feature supervision, and observe close agreement with the qualitative and quantitative trends reported in the original work. At the same time, our experiments show that performance is sensitive to a small number of hyperparameter assumptions, particularly the optimized timestep and the feature level used for motion supervision, while other components admit broader operating ranges. We further evaluate a multi-timestep latent optimization variant and find that it does not improve spatial accuracy while substantially increasing computational cost. Overall, our findings support the central claims of DragDiffusion while clarifying the conditions under which they are reliably reproducible. Code is available at https://github.com/AliSubhan5341/DragDiffusion-TMLR-Reproducibility-Challenge.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:40:43Z。旧 registry Updated:v1：2026-02-16T01:05:44Z（不作首公开）。

## 2602.12394

[Synthetic Interaction Data for Scalable Personalization in Large Language Models](https://arxiv.org/abs/2602.12394v1)

Personalized prompting offers large opportunities for deploying large language models (LLMs) to diverse users, yet existing prompt optimization methods primarily focus on task-level optimization while largely overlooking user-specific preferences and latent constraints of individual users. This gap is primarily due to (i) the absence of high-quality, privacy-sensitive data that capture personalized user-LLM interactions at scale, and (ii) the lack of robust reward signals for individual preferences. To overcome existing data limitations, we introduce a high-fidelity synthetic data generation framework called PersonaGym. Unlike prior work that treats personalization as static persona-preference pairs, PersonaGym models a dynamic preference process via an agentic LLM system to simulate realistic preference behaviors and semantic-aware noise in order to generate personalized multi-turn interaction trajectories. Using PersonaGym, we release PersonaAtlas, a large-scale, high-quality, and diverse synthetic dataset of high-fidelity multi-turn personalized interaction trajectories that closely mirror real-world preference expression and noise patterns. We further propose Personalized Prompt Optimization (PPOpt), a scalable and model-agnostic framework that optimizes user prompts based on interaction histories without modifying the deployed LLM. PPOpt adopts a reason-then-optimize paradigm that infers an explicit user profile and conditions prompt rewriting on the user profile to avoid reward hacking. Our training procedure for PPOpt integrates a cold-start supervised prior with outcome-driven multi-objective reinforcement learning. We present extensive experiments to demonstrate consistent improvements over state-of-the-art baselines in terms of task performance, personalization quality, and robustness to noisy as well as to sparse preference signals.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:41:22Z。旧 registry Updated:v1：2026-02-16T01:05:46Z（不作首公开）。

## 2602.12395

[What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis](https://arxiv.org/abs/2602.12395v1)

Reinforcement learning (RL) with verifiable rewards has become a standard post-training stage for boosting visual reasoning in vision-language models, yet it remains unclear what capabilities RL actually improves compared with supervised fine-tuning as cold-start initialization (IN). End-to-end benchmark gains conflate multiple factors, making it difficult to attribute improvements to specific skills. To bridge the gap, we propose a Frankenstein-style analysis framework including: (i) functional localization via causal probing; (ii) update characterization via parameter comparison; and (iii) transferability test via model merging. Instead, RL induces a consistent inference-time shift primarily in mid-to-late layers, and these mid-to-late refinements are both transferable (via merging) and necessary (via freezing) for RL gains. Overall, our results suggest that RL's reliable contribution in visual reasoning is not a uniform enhancement of visual perception, but a systematic refinement of mid-to-late transformer computation that improves vision-to-reasoning alignment and reasoning performance, highlighting the limitations of benchmark-only evaluation for understanding multimodal reasoning improvements.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:44:27Z。旧 registry Updated:v1：2026-02-16T01:05:53Z（不作首公开）。

## 2602.12403

[MonoLoss: A Training Objective for Interpretable Monosemantic Representations](https://arxiv.org/abs/2602.12403v1)

Sparse autoencoders (SAEs) decompose polysemantic neural representations, where neurons respond to multiple unrelated concepts, into monosemantic features that capture single, interpretable concepts. However, standard training objectives only weakly encourage this decomposition, and existing monosemanticity metrics require pairwise comparisons across all dataset samples, making them inefficient during training and evaluation. We study a recent MonoScore metric and derive a single-pass algorithm that computes exactly the same quantity, but with a cost that grows linearly, rather than quadratically, with the number of dataset images. On OpenImagesV7, we achieve up to a 1200x speedup wall-clock speedup in evaluation and 159x during training, while adding only ~4% per-epoch overhead. This allows us to treat MonoScore as a training signal: we introduce the Monosemanticity Loss (MonoLoss), a plug-in objective that directly rewards semantically consistent activations for learning interpretable monosemantic representations. Across SAEs trained on CLIP, SigLIP2, and pretrained ViT features, using BatchTopK, TopK, and JumpReLU SAEs, MonoLoss increases MonoScore for most latents. MonoLoss also consistently improves class purity (the fraction of a latent's activating images belonging to its dominant class) across all encoder and SAE combinations, with the largest gain raising baseline purity from 0.152 to 0.723. Used as an auxiliary regularizer during ResNet-50 and CLIP-ViT-B/32 finetuning, MonoLoss yields up to 0.6\% accuracy gains on ImageNet-1K and monosemantic activating patterns on standard benchmark datasets. The code is publicly available at https://github.com/AtlasAnalyticsLab/MonoLoss.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T20:53:41Z。旧 registry Updated:v1：2026-02-16T01:06:13Z（不作首公开）。

## 2602.12413

[Soft Contamination Means Benchmarks Test Shallow Generalization](https://arxiv.org/abs/2602.12413v1)

If LLM training data is polluted with benchmark test data, then benchmark performance gives biased estimates of out-of-distribution (OOD) generalization. Typical decontamination filters use n-gram matching which fail to detect semantic duplicates: sentences with equivalent (or near-equivalent) content that are not close in string space. We study this soft contamination of training data by semantic duplicates. Among other experiments, we embed the Olmo3 training corpus and find that: 1) contamination remains widespread, e.g. we find semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems; 2) including semantic duplicates of benchmark data in training does improve benchmark performance; and 3) when finetuning on duplicates of benchmark datapoints, performance also improves on truly-held-out datapoints from the same benchmark. We argue that recent benchmark gains are thus confounded: the prevalence of soft contamination means gains reflect both genuine capability improvements and the accumulation of test data and effective test data in growing training corpora.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:12:53Z。旧 registry Updated:v1：2026-02-16T01:06:53Z（不作首公开）。

## 2602.12414

[propella-1: Multi-Property Document Annotation for LLM Data Curation at Scale](https://arxiv.org/abs/2602.12414v1)

Since FineWeb-Edu, data curation for LLM pretraining has predominantly relied on single scalar quality scores produced by small classifiers. A single score conflates multiple quality dimensions, prevents flexible filtering, and offers no interpretability. We introduce propella-1, a family of small multilingual LLMs (0.6B, 1.7B, 4B parameters) that annotate text documents across 18 properties organized into six categories: core content, classification, quality and value, audience and purpose, safety and compliance, and geographic relevance. The models support 57 languages and produce structured JSON annotations conforming to a predefined schema. Evaluated against a frontier commercial LLM as a reference annotator, the 4B model achieves higher agreement than much larger general-purpose models. We release propella-annotations, a dataset of over three billion document annotations covering major pretraining corpora including data from FineWeb-2, FinePDFs, HPLT 3.0, and Nemotron-CC. Using these annotations, we present a multi-dimensional compositional analysis of widely used pretraining datasets, revealing substantial differences in quality, reasoning depth, and content composition that single-score approaches cannot capture. All model weights and annotations are released under permissive, commercial-use licenses.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:13:08Z。旧 registry Updated:v1：2026-02-16T01:06:55Z（不作首公开）。

## 2602.12418

[Sparse Autoencoders are Capable LLM Jailbreak Mitigators](https://arxiv.org/abs/2602.12418v1)

Jailbreak attacks remain a persistent threat to large language model safety. We propose Context-Conditioned Delta Steering (CC-Delta), an SAE-based defense that identifies jailbreak-relevant sparse features by comparing token-level representations of the same harmful request with and without jailbreak context. Using paired harmful/jailbreak prompts, CC-Delta selects features via statistical testing and applies inference-time mean-shift steering in SAE latent space. Across four aligned instruction-tuned models and twelve jailbreak attacks, CC-Delta achieves comparable or better safety-utility tradeoffs than baseline defenses operating in dense latent space. In particular, our method clearly outperforms dense mean-shift steering on all four models, and particularly against out-of-distribution attacks, showing that steering in sparse SAE feature space offers advantages over steering in dense activation space for jailbreak mitigation. Our results suggest off-the-shelf SAEs trained for interpretability can be repurposed as practical jailbreak defenses without task-specific training.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:17:32Z。旧 registry Updated:v1：2026-02-16T01:07:06Z（不作首公开）。

## 2602.12424

[RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty](https://arxiv.org/abs/2602.12424v1)

Benchmarks establish a standardized evaluation framework to systematically assess the performance of large language models (LLMs), facilitating objective comparisons and driving advancements in the field. However, existing benchmarks fail to differentiate question difficulty, limiting their ability to effectively distinguish models' capabilities. To address this limitation, we propose RankLLM, a novel framework designed to quantify both question difficulty and model competency. RankLLM introduces difficulty as the primary criterion for differentiation, enabling a more fine-grained evaluation of LLM capabilities. RankLLM's core mechanism facilitates bidirectional score propagation between models and questions. The core intuition of RankLLM is that a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model. Using this framework, we evaluate 30 models on 35,550 questions across multiple domains. RankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT. It also exhibits strong stability, fast convergence, and high computational efficiency, making it a practical solution for large-scale, difficulty-aware LLM evaluation.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:28:46Z。旧 registry Updated:v1：2026-02-16T01:07:26Z（不作首公开）。

## 2602.12429

[Stabilizing Native Low-Rank LLM Pretraining](https://arxiv.org/abs/2602.12429v1)

Foundation models have achieved remarkable success, yet their growing parameter counts pose significant computational and memory challenges. Low-rank factorization offers a promising route to reduce training and inference costs, but the community lacks a stable recipe for training models from scratch using exclusively low-rank weights while matching the performance of the dense model. We demonstrate that Large Language Models (LLMs) can be trained from scratch using exclusively low-rank factorized weights for all non-embedding matrices without auxiliary "full-rank" guidance required by prior methods. While native low-rank training often suffers from instability and loss spikes, we identify uncontrolled growth in the spectral norm (largest singular value) of the weight matrix update as the dominant factor. To address this, we introduce Spectron: Spectral renormalization with orthogonalization, which dynamically bounds the resultant weight updates based on the current spectral norms of the factors. Our method enables stable, end-to-end factorized training with negligible overhead. Finally, we establish compute-optimal scaling laws for natively low-rank transformers, demonstrating predictable power-law behavior and improved inference efficiency relative to dense models.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:33:14Z。旧 registry Updated:v1：2026-02-16T01:07:33Z（不作首公开）。

## 2602.12430

[Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430v1)

The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, portable skill definitions, and integration with the Model Context Protocol (MCP). This survey provides a comprehensive treatment of the agent skills landscape, as it has rapidly evolved during the last few months. We organize the field along four axes: (i) architectural foundations, examining the SKILL$.$md specification, progressive context loading, and the complementary roles of skills and MCP; (ii) skill acquisition, covering reinforcement learning with skill libraries, autonomous skill discovery (SEAgent), and compositional skill synthesis; (iii) deployment at scale, including the computer-use agent (CUA) stack, GUI grounding advances, and benchmark progress on OSWorld and SWE-bench; and (iv) security, where recent empirical analyses reveal that 26.1% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework -- a four-tier, gate-based permission model that maps skill provenance to graduated deployment capabilities. We identify seven open challenges -- from cross-platform skill portability to capability-based permission models -- and propose a research agenda for realizing trustworthy, self-improving skill ecosystems. Unlike prior surveys that broadly cover LLM agents or tool use, this work focuses specifically on the emerging skill abstraction layer and its implications for the next generation of agentic systems. Project repo: https://github.com/scienceaix/agentskills

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:33:25Z。旧 registry Updated:v1：2026-02-16T01:07:35Z（不作首公开）。

## 2602.12432

[KeySense: LLM-Powered Hands-Down, Ten-Finger Typing on Commodity Touchscreens](https://arxiv.org/abs/2602.12432v1)

Existing touchscreen software keyboards prevent users from resting their hands, forcing slow and fatiguing index-finger tapping ("chicken typing") instead of familiar hands-down ten-finger typing. We present KeySense, a purely software solution that preserves physical keyboard motor skills. KeySense isolates intentional taps from resting-finger noise using cognitive-motor timing patterns, and then uses a fine-tuned LLM decoder to convert the resulting noisy letter sequence into the intended word. In controlled component tests, the decoder substantially outperforms two statistical baselines (top-1 accuracy 84.8% vs 75.7% and 79.3%). A 12-participant study shows clear ergonomic and performance benefits: compared with the conventional hover-style keyboard, users rated KeySense as markedly less physically demanding (NASA-TLX median 1.5 vs 4.0), and after brief practice typed significantly faster (WPM 28.3 vs 26.2, p &lt; 0.01). These results indicate that KeySense enables accurate, efficient, and comfortable ten-finger text entry on commodity touchscreens without any extra hardware.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T21:33:40Z。旧 registry Updated:v1：2026-02-16T01:07:37Z（不作首公开）。

## 2602.12445

[RBCorr: Response Bias Correction in Language Models](https://arxiv.org/abs/2602.12445v1)

Language models (LMs) are known to be prone to response biases, which present as option preference biases in fixed-response questions. It is therefore imperative to develop low-cost and effective response bias correction methods to improve LM performance and enable more accurate evaluations of model abilities. Here, we propose a simple response bias correction strategy ($\texttt{RBCorr}$) and test it on 12 open-weight language models using yes-no, entailment, and multiple choice questions. We show that response bias is prevalent in LMs pre-correction and that $\texttt{RBCorr}$ effectively eliminates bias and boosts model performance. We also explore the generalizability of bias behavior across models, datasets, and prompt formats, showing that LogProbs-based correction is highly dependent on all three of these aspects. Overall, $\texttt{RBCorr}$ is an easy-to-use method that can boost the performance of smaller LMs and ensure that LM performance on closed-response benchmarks aligns more closely with their true capabilities.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T22:05:04Z。旧 registry Updated:v1：2026-02-16T01:08:42Z（不作首公开）。

## 2602.12468

[Continuous Diffusion Models Can Obey Formal Syntax](https://arxiv.org/abs/2602.12468v1)

Diffusion language models offer a promising alternative to autoregressive models due to their global, non-causal generation process, but their continuous latent dynamics make discrete constraints -- e.g., the output should be a JSON file that matches a given schema -- difficult to impose. We introduce a training-free guidance method for steering continuous diffusion language models to satisfy formal syntactic constraints expressed using regular expressions. Our approach constructs an analytic score estimating the probability that a latent state decodes to a valid string accepted by a given regular expression, and uses its gradient to guide sampling, without training auxiliary classifiers. The denoising process targets the base model conditioned on syntactic validity. We implement our method in Diffinity on top of the PLAID diffusion model and evaluate it on 180 regular-expression constraints over JSON and natural-language benchmarks. Diffinity achieves 68-96\% constraint satisfaction while incurring only a small perplexity cost relative to unconstrained sampling, outperforming autoregressive constrained decoding in both constraint satisfaction and output quality. Diffinity is open-sourced at github.com/large-loris-models/Diffinity.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T22:55:05Z。旧 registry Updated:v1：2026-02-16T01:10:13Z（不作首公开）。

## 2602.12480

[MXFormer: A Microscaling Floating-Point Charge-Trap Transistor Compute-in-Memory Transformer Accelerator](https://arxiv.org/abs/2602.12480v1)

The proliferation of Transformer models is often constrained by the significant computational and memory bandwidth demands of deployment. To address this, we present MXFormer, a novel, hybrid, weight-stationary Compute-in-Memory (CIM) accelerator that provides high throughput and efficiency for fixed-model inference on large short-sequence Transformers. Our architecture's foundation is the use of ultra-dense Charge-Trap Transistors (CTTs) in Microscaling MXFP4 CIM arrays, uniquely enabling the on-chip storage of up to hundreds of millions of parameters in Fully Weight Stationary (FWS) fashion.
 We introduce a statically partitioned design with 12 Transformer blocks connected by a deeply pipelined dataflow. Static-weight layers (MLPs and linear projections) execute on highly parallel analog CTT arrays using an MXFP4-native flow with per-block exponent alignment and a 10-bit SAR ADC. Dynamic computations are handled in fully accurate digital blocks that utilize MXFP-enabled systolic arrays for scaled dot-product attention and vector units for LayerNorm and FlashAttention-style Softmax.
 By eliminating all weight movement, the deeply pipelined MXFormer architecture yields very high single-stream throughput and efficiency, processing 58275 FPS on ViT-L/32 (dual-chip) or 41269 FPS on ViT-B/16 (single chip). MXFormer outperforms comparable state-of-the-art non-FWS digital, hybrid and photonic Transformer accelerators ~3.3x-60.5x in compute density and ~1.7x-2.5x in energy efficiency. Against FWS accelerators, MXFormer improves compute density by ~20.9x and resident weight storage density by ~2x, while preserving near-digital accuracy (drop of &lt;1%) without any model retraining.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-12T23:38:08Z。旧 registry Updated:v1：2026-02-16T01:11:14Z（不作首公开）。

## 2602.12490

[Transformer-based CoVaR: Systemic Risk in Textual Information](https://arxiv.org/abs/2602.12490v1)

Conditional Value-at-Risk (CoVaR) quantifies systemic financial risk by measuring the loss quantile of one asset, conditional on another asset experiencing distress. We develop a Transformer-based methodology that integrates financial news articles directly with market data to improve CoVaR estimates. Unlike approaches that use predefined sentiment scores, our method incorporates raw text embeddings generated by a large language model (LLM). We prove explicit error bounds for our Transformer CoVaR estimator, showing that accurate CoVaR learning is possible even with small datasets. Using U.S. market returns and Reuters news items from 2006--2013, our out-of-sample results show that textual information impacts the CoVaR forecasts. With better predictive performance, we identify a pronounced negative dip during market stress periods across several equity assets when comparing the Transformer-based CoVaR to both the CoVaR without text and the CoVaR using traditional sentiment measures. Our results show that textual data can be used to effectively model systemic risk without requiring prohibitively large data sets.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T00:10:30Z。旧 registry Updated:v1：2026-02-16T01:11:47Z（不作首公开）。

## 2602.12499

[A Theoretical Analysis of Mamba's Training Dynamics: Filtering Relevant Features for Generalization in State Space Models](https://arxiv.org/abs/2602.12499v1)

The recent empirical success of Mamba and other selective state space models (SSMs) has renewed interest in non-attention architectures for sequence modeling, yet their theoretical foundations remain underexplored. We present a first-step analysis of generalization and learning dynamics for a simplified but representative Mamba block: a single-layer, single-head selective SSM with input-dependent gating, followed by a two-layer MLP trained via gradient descent (GD). Our study adopts a structured data model with tokens that include both class-relevant and class-irrelevant patterns under token-level noise and examines two canonical regimes: majority-voting and locality-structured data sequences. We prove that the model achieves guaranteed generalization by establishing non-asymptotic sample complexity and convergence rate bounds, which improve as the effective signal increases and the noise decreases. Furthermore, we show that the gating vector aligns with class-relevant features while ignoring irrelevant ones, thereby formalizing a feature-selection role similar to attention but realized through selective recurrence. Numerical experiments on synthetic data justify our theoretical results. Overall, our results provide principled insight into when and why Mamba-style selective SSMs learn efficiently, offering a theoretical counterpoint to Transformer-centric explanations.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T00:44:26Z。旧 registry Updated:v1：2026-02-16T01:12:20Z（不作首公开）。

## 2602.12500

[Favia: Forensic Agent for Vulnerability-fix Identification and Analysis](https://arxiv.org/abs/2602.12500v1)

Identifying vulnerability-fixing commits corresponding to disclosed CVEs is essential for secure software maintenance but remains challenging at scale, as large repositories contain millions of commits of which only a small fraction address security issues. Existing automated approaches, including traditional machine learning techniques and recent large language model (LLM)-based methods, often suffer from poor precision-recall trade-offs. Frequently evaluated on randomly sampled commits, we uncover that they are substantially underestimating real-world difficulty, where candidate commits are already security-relevant and highly similar. We propose Favia, a forensic, agent-based framework for vulnerability-fix identification that combines scalable candidate ranking with deep and iterative semantic reasoning. Favia first employs an efficient ranking stage to narrow the search space of commits. Each commit is then rigorously evaluated using a ReAct-based LLM agent. By providing the agent with a pre-commit repository as environment, along with specialized tools, the agent tries to localize vulnerable components, navigates the codebase, and establishes causal alignment between code changes and vulnerability root causes. This evidence-driven process enables robust identification of indirect, multi-file, and non-trivial fixes that elude single-pass or similarity-based methods. We evaluate Favia on CVEVC, a large-scale dataset we made that comprises over 8 million commits from 3,708 real-world repositories, and show that it consistently outperforms state-of-the-art traditional and LLM-based baselines under realistic candidate selection, achieving the strongest precision-recall trade-offs and highest F1-scores.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T00:51:22Z。旧 registry Updated:v1：2026-02-16T01:12:27Z（不作首公开）。

## 2602.12520

[Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings](https://arxiv.org/abs/2602.12520v1)

Learning to coordinate many agents in partially observable and highly dynamic environments requires both informative representations and data-efficient training. To address this challenge, we present a novel model-based multi-agent reinforcement learning framework that unifies joint state-action representation learning with imaginative roll-outs. We design a world model trained with variational auto-encoders and augment the model using the state-action learned embedding (SALE). SALE is injected into both the imagination module that forecasts plausible future roll-outs and the joint agent network whose individual action values are combined through a mixing network to estimate the joint action-value function. By coupling imagined trajectories with SALE-based action values, the agents acquire a richer understanding of how their choices influence collective outcomes, leading to improved long-term planning and optimization under limited real-environment interactions. Empirical studies on well-established multi-agent benchmarks, including StarCraft II Micro-Management, Multi-Agent MuJoCo, and Level-Based Foraging challenges, demonstrate consistent gains of our method over baseline algorithms and highlight the effectiveness of joint state-action learned embeddings within a multi-agent model-based paradigm.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T01:57:21Z。旧 registry Updated:v1：2026-02-16T01:14:27Z（不作首公开）。

## 2602.12521

[Opus: Photonic Rail-Optimized Fabric in ML Datacenters](https://arxiv.org/abs/2602.12521v1)

Rail-optimized network fabrics have become the de facto datacenter scale-out fabric for large-scale ML training. However, the use of high-radix electrical switches to provide all-to-all connectivity in rails imposes substantial power and cost. We propose a rethinking of the rail abstraction by retaining its communication semantics, but realizing it using optical circuit switches. The key challenge is that optical switches support one-to-one connectivity at a time, limiting the fan-out of traffic in ML workloads using hybrid parallelisms. We overcome this through \emph{parallelism-driven rail reconfiguration}, which exploits the non-overlapping communication phases of different parallelism dimensions. This time-multiplexes a single set of physical ports across circuit configurations tailored to each phase within a training iteration. We design and implement Opus, a control plane that orchestrates this in-job reconfiguration of photonic rails at parallelism phase boundaries, and evaluate it on a physical OCS testbed, the Perlmutter supercomputer, and in simulation at up to 2,048 GPUs. Our results show that photonic rails can achieve over $23\times$ network power reduction and $4\times$ cost savings while incurring only modest training overhead at production-relevant OCS reconfiguration latencies.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T01:59:03Z。旧 registry Updated:v1：2026-02-16T01:14:30Z（不作首公开）。

## 2602.12526

[Constraint-Rectified Training for Efficient Chain-of-Thought](https://arxiv.org/abs/2602.12526v1)

Chain-of-Thought (CoT) has significantly enhanced the reasoning capabilities of Large Language Models (LLMs), especially when combined with reinforcement learning (RL) based post-training methods. While longer reasoning traces can improve answer quality and unlock abilities such as self-correction, they also incur high inference costs and often introduce redundant steps, known as overthinking. Recent research seeks to develop efficient reasoning strategies that balance reasoning length and accuracy, either through length-aware reward design or prompt-based calibration. However, these heuristic-based approaches may suffer from severe accuracy drop and be very sensitive to hyperparameters. To address these problems, we introduce CRT (Constraint-Rectified Training), a principled post-training framework based on reference-guarded constrained optimization, yielding a more stable and interpretable formulation for efficient reasoning. CRT alternates between minimizing reasoning length and rectifying accuracy only when performance falls below the reference, enabling stable and effective pruning of redundant reasoning. We further extend CRT with a two-stage training scheme that first discovers the shortest reliable reasoning patterns and then refines accuracy under a learnt length budget, preventing the re-emergence of verbose CoT. Our comprehensive evaluation shows that this framework consistently reduces token usage while maintaining answer quality at a robust and reliable level. Further analysis reveals that CRT improves reasoning efficiency not only by shortening responses but also by reducing internal language redundancy, leading to a new evaluation metric. Moreover, CRT-based training naturally yields a sequence of intermediate checkpoints that span a spectrum of explanation lengths while preserving correctness, enabling fine-grained control over reasoning verbosity without retraining.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T02:13:45Z。旧 registry Updated:v1：2026-02-16T01:15:06Z（不作首公开）。

## 2602.12528

[DiffuRank: Effective Document Reranking with Diffusion Language Models](https://arxiv.org/abs/2602.12528v1)

Recent advances in large language models (LLMs) have inspired new paradigms for document reranking. While this paradigm better exploits the reasoning and contextual understanding capabilities of LLMs, most existing LLM-based rerankers rely on autoregressive generation, which limits their efficiency and flexibility. In particular, token-by-token decoding incurs high latency, while the fixed left-to-right generation order causes early prediction errors to propagate and is difficult to revise. To address these limitations, we explore the use of diffusion language models (dLLMs) for document reranking and propose DiffuRank, a reranking framework built upon dLLMs. Unlike autoregressive models, dLLMs support more flexible decoding and generation processes that are not constrained to a left-to-right order, and enable parallel decoding, which may lead to improved efficiency and controllability. Specifically, we investigate three reranking strategies based on dLLMs: (1) a pointwise approach that uses dLLMs to estimate the relevance of each query-document pair; (2) a logit-based listwise approach that prompts dLLMs to jointly assess the relevance of multiple documents and derives ranking lists directly from model logits; and (3) a permutation-based listwise approach that adapts the canonical decoding process of dLLMs to the reranking tasks. For each approach, we design corresponding training methods to fully exploit the advantages of dLLMs. We evaluate both zero-shot and fine-tuned reranking performance on multiple benchmarks. Experimental results show that dLLMs achieve performance comparable to, and in some cases exceeding, that of autoregressive LLMs with similar model sizes. These findings demonstrate the promise of diffusion-based language models as a compelling alternative to autoregressive architectures for document reranking.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T02:18:14Z。旧 registry Updated:v1：2026-02-16T01:15:10Z（不作首公开）。

## 2602.12529

[Flow-Factory: A Unified Framework for Reinforcement Learning in Flow-Matching Models](https://arxiv.org/abs/2602.12529v1)

Reinforcement learning has emerged as a promising paradigm for aligning diffusion and flow-matching models with human preferences, yet practitioners face fragmented codebases, model-specific implementations, and engineering complexity. We introduce Flow-Factory, a unified framework that decouples algorithms, models, and rewards through through a modular, registry-based architecture. This design enables seamless integration of new algorithms and architectures, as demonstrated by our support for GRPO, DiffusionNFT, and AWM across Flux, Qwen-Image, and WAN video models. By minimizing implementation overhead, Flow-Factory empowers researchers to rapidly prototype and scale future innovations with ease. Flow-Factory provides production-ready memory optimization, flexible multi-reward training, and seamless distributed training support. The codebase is available at https://github.com/X-GenGroup/Flow-Factory.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T02:21:59Z。旧 registry Updated:v1：2026-02-16T01:15:22Z（不作首公开）。

## 2602.12532

[CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning](https://arxiv.org/abs/2602.12532v1)

Vision-Language-Action (VLA) models have shown a strong capability in enabling robots to execute general instructions, yet they struggle with contact-rich manipulation tasks, where success requires precise alignment, stable contact maintenance, and effective handling of deformable objects. A fundamental challenge arises from the imbalance between high-entropy vision and language inputs and low-entropy but critical force signals, which often leads to over-reliance on perception and unstable control. To address this, we introduce CRAFT, a force-aware curriculum fine-tuning framework that integrates a variational information bottleneck module to regulate vision and language embeddings during early training. This curriculum strategy encourages the model to prioritize force signals initially, before progressively restoring access to the full multimodal information. To enable force-aware learning, we further design a homologous leader-follower teleoperation system that collects synchronized vision, language, and force data across diverse contact-rich tasks. Real-world experiments demonstrate that CRAFT consistently improves task success, generalizes to unseen objects and novel task variations, and adapts effectively across diverse VLA architectures, enabling robust and generalizable contact-rich manipulation.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T02:28:21Z。旧 registry Updated:v1：2026-02-16T01:15:35Z（不作首公开）。

## 2602.12544

[Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation](https://arxiv.org/abs/2602.12544v1)

We present a scalable pipeline for automatically generating high-quality training data for web agents. In particular, a major challenge in identifying high-quality training instances is trajectory evaluation - quantifying how much progress was made towards task completion. We introduce a novel constraint-based evaluation framework that provides fine-grained assessment of progress towards task completion. This enables us to leverage partially successful trajectories, which significantly expands the amount of usable training data. We evaluate our method on a new benchmark we propose called BookingArena, which consists of complex booking tasks across 20 popular websites, and demonstrate that our distilled student model outperforms open-source approaches and matches or exceeds commercial systems, while being a significantly smaller model. Our work addresses the challenge of efficiently creating diverse, realistic web interaction datasets and provides a systematic evaluation methodology for complex structured web tasks.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T02:52:18Z。旧 registry Updated:v1：2026-02-16T01:16:28Z（不作首公开）。

## 2602.12556

[SD-MoE: Spectral Decomposition for Effective Expert Specialization](https://arxiv.org/abs/2602.12556v1)

Mixture-of-Experts (MoE) architectures scale Large Language Models via expert specialization induced by conditional computation. In practice, however, expert specialization often fails: some experts become functionally similar, while others functioning as de facto shared experts, limiting the effective capacity and model performance. In this work, we analysis from a spectral perspective on parameter and gradient spaces, uncover that (1) experts share highly overlapping dominant spectral components in their parameters, (2) dominant gradient subspaces are strongly aligned across experts, driven by ubiquitous low-rank structure in human corpus, and (3) gating mechanisms preferentially route inputs along these dominant directions, further limiting specialization. To address this, we propose Spectral-Decoupled MoE (SD-MoE), which decomposes both parameter and gradient in the spectral space. SD-MoE improves performance across downstream tasks, enables effective expert specialization, incurring minimal additional computation, and can be seamlessly integrated into a wide range of existing MoE architectures, including Qwen and DeepSeek.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T03:07:26Z。旧 registry Updated:v1：2026-02-16T01:17:14Z（不作首公开）。

## 2602.12561

[PLLM: Pseudo-Labeling Large Language Models for CAD Program Synthesis](https://arxiv.org/abs/2602.12561v1)

Recovering Computer-Aided Design (CAD) programs from 3D geometries is a widely studied problem. Recent advances in large language models (LLMs) have enabled progress in CAD program synthesis, but existing methods rely on supervised training with paired shape-program data, which is often unavailable. We introduce PLLM, a self-training framework for CAD program synthesis from unlabeled 3D shapes. Given a pre-trained CAD-capable LLM and a shape dataset, PLLM iteratively samples candidate programs, selects high-fidelity executions, and augments programs to construct synthetic program-shape pairs for fine-tuning. We experiment on adapting CAD-Recode from DeepCAD to the unlabeled ABC dataset show consistent improvements in geometric fidelity and program diversity.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T03:20:19Z。旧 registry Updated:v1：2026-02-16T01:17:53Z（不作首公开）。

## 2602.12566

[To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2602.12566v1)

Reinforcement Learning with Verifiable Rewards (RLVR) plays a key role in stimulating the explicit reasoning capability of Large Language Models (LLMs). We can achieve expert-level performance in some specific domains via RLVR, such as coding or math. When a general multi-domain expert-level model is required, we need to carefully consider the collaboration of RLVR across different domains. The current state-of-the-art models mainly employ two different training paradigms for multi-domain RLVR: mixed multi-task RLVR and separate RLVR followed by model merging. However, most of the works did not provide a detailed comparison and analysis about these paradigms. To this end, we choose multiple commonly used high-level tasks (e.g., math, coding, science, instruction following, and agent) as our target domains and design extensive qualitative and quantitative experiments using open-source datasets. We find the RLVR across domains exhibits few mutual interferences, and reasoning-intensive domains demonstrate mutually synergistic effects. Furthermore, we analyze the internal mechanisms of mutual gains from the perspectives of weight space geometry, information constraints, model prediction behavior and self-verification. This project is named as M2RL that means Mixed multi-task training or separate training followed by model Merging for Reinforcement Learning, and the homepage is at https://github.com/Mosi-AI/M2RL.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T03:25:13Z。旧 registry Updated:v1：2026-02-16T01:18:12Z（不作首公开）。

## 2602.12579

[VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction](https://arxiv.org/abs/2602.12579v1)

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a dominant paradigm for enhancing Large Language Models (LLMs) reasoning, yet its reliance on external verifiers limits its scalability. Recent findings suggest that RLVR primarily functions by eliciting latent capabilities, motivating the development of verifier-free algorithms. However, in such settings, standard methods like Group Relative Policy Optimization face a critical challenge: destructive gradient variance that often leads to training collapse. To address this issue, we introduce Verifier-Independent Curriculum Reinforcement Learning (VI-CuRL), a framework that leverages the model's intrinsic confidence to construct a curriculum independent from external verifiers. By prioritizing high-confidence samples, VI-CuRL effectively manages the bias-variance trade-off, specifically targeting the reduction of action and problem variance. We provide a rigorous theoretical analysis, proving that our estimator guarantees asymptotic unbiasedness. Empirically, VI-CuRL promotes stability and consistently outperforms verifier-dependent/independent baselines across math and general reasoning benchmarks with/without verifiers.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T03:40:52Z。旧 registry Updated:v1：2026-02-16T01:19:06Z（不作首公开）。

## 2602.12586

[Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models](https://arxiv.org/abs/2602.12586v1)

While plan-and-infill decoding in Masked Diffusion Models (MDMs) shows promise for mathematical and code reasoning, performance remains highly sensitive to slot infilling order, often yielding substantial output variance. We introduce McDiffuSE, a framework that formulates slot selection as decision making and optimises infilling orders through Monte Carlo Tree Search (MCTS). McDiffuSE uses look-ahead simulations to evaluate partial completions before commitment, systematically exploring the combinatorial space of generation orders. Experiments show an average improvement of 3.2% over autoregressive baselines and 8.0% over baseline plan-and-infill, with notable gains of 19.5% on MBPP and 4.9% on MATH500. Our analysis reveals that while McDiffuSE predominantly follows sequential ordering, incorporating non-sequential generation is essential for maximising performance. We observe that larger exploration constants, rather than increased simulations, are necessary to overcome model confidence biases and discover effective orderings. These findings establish MCTS-based planning as an effective approach for enhancing generation quality in MDMs.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T03:56:22Z。旧 registry Updated:v1：2026-02-16T01:19:28Z（不作首公开）。

## 2602.12587

[Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](https://arxiv.org/abs/2602.12587v1)

Mixture-of-Experts (MoE) architectures are often considered a natural fit for continual learning because sparse routing should localize updates and reduce interference, yet MoE Transformers still forget substantially even with sparse, well-balanced expert utilization. We attribute this gap to a pre-routing bottleneck: multi-head attention concatenates head-specific signals into a single post-attention router input, forcing routing to act on co-occurring feature compositions rather than separable head channels. We show that this router input simultaneously encodes multiple separately decodable semantic and structural factors with uneven head support, and that different feature compositions induce weakly aligned parameter-gradient directions; as a result, routing maps many distinct compositions to the same route. We quantify this collision effect via a route-wise effective composition number $N_{eff}$ and find that higher $N_{eff}$ is associated with larger old-task loss increases after continual training. Motivated by these findings, we propose MH-MoE, which performs head-wise routing over sub-representations to increase routing granularity and reduce composition collisions. On TRACE with Qwen3-0.6B/8B, MH-MoE effectively mitigates forgetting, reducing BWT on Qwen3-0.6B from 11.2% (LoRAMoE) to 4.5%.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T03:59:09Z。旧 registry Updated:v1：2026-02-16T01:19:31Z（不作首公开）。

## 2602.12590

[Unbiased Gradient Estimation for Event Binning via Functional Backpropagation](https://arxiv.org/abs/2602.12590v1)

Event-based vision encodes dynamic scenes as asynchronous spatio-temporal spikes called events. To leverage conventional image processing pipelines, events are typically binned into frames. However, binning functions are discontinuous, which truncates gradients at the frame level and forces most event-based algorithms to rely solely on frame-based features. Attempts to directly learn from raw events avoid this restriction but instead suffer from biased gradient estimation due to the discontinuities of the binning operation, ultimately limiting their learning efficiency. To address this challenge, we propose a novel framework for unbiased gradient estimation of arbitrary binning functions by synthesizing weak derivatives during backpropagation while keeping the forward output unchanged. The key idea is to exploit integration by parts: lifting the target functions to functionals yields an integral form of the derivative of the binning function during backpropagation, where the cotangent function naturally arises. By reconstructing this cotangent function from the sampled cotangent vector, we compute weak derivatives that provably match long-range finite differences of both smooth and non-smooth targets. Experimentally, our method improves simple optimization-based egomotion estimation with 3.2\% lower RMS error and 1.57$\times$ faster convergence. On complex downstream tasks, we achieve 9.4\% lower EPE in self-supervised optical flow, and 5.1\% lower RMS error in SLAM, demonstrating broad benefits for event-based visual perception. Source code can be found at https://github.com/chjz1024/EventFBP.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T04:05:03Z。旧 registry Updated:v1：2026-02-16T01:19:35Z（不作首公开）。

## 2602.12593

[RQ-GMM: Residual Quantized Gaussian Mixture Model for Multimodal Semantic Discretization in CTR Prediction](https://arxiv.org/abs/2602.12593v1)

Multimodal content is crucial for click-through rate (CTR) prediction. However, directly incorporating continuous embeddings from pre-trained models into CTR models yields suboptimal results due to misaligned optimization objectives and convergence speed inconsistency during joint training. Discretizing embeddings into semantic IDs before feeding them into CTR models offers a more effective solution, yet existing methods suffer from limited codebook utilization, reconstruction accuracy, and semantic discriminability. We propose RQ-GMM (Residual Quantized Gaussian Mixture Model), which introduces probabilistic modeling to better capture the statistical structure of multimodal embedding spaces. Through Gaussian Mixture Models combined with residual quantization, RQ-GMM achieves superior codebook utilization and reconstruction accuracy. Experiments on public datasets and online A/B tests on a large-scale short-video platform serving hundreds of millions of users demonstrate substantial improvements: RQ-GMM yields a 1.502% gain in Advertiser Value over strong baselines. The method has been fully deployed, serving daily recommendations for hundreds of millions of users.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T04:11:24Z。旧 registry Updated:v1：2026-02-16T01:19:45Z（不作首公开）。

## 2602.12609

[QuEPT: Quantized Elastic Precision Transformers with One-Shot Calibration for Multi-Bit Switching](https://arxiv.org/abs/2602.12609v1)

Elastic precision quantization enables multi-bit deployment via a single optimization pass, fitting diverse quantization scenarios.Yet, the high storage and optimization costs associated with the Transformer architecture, research on elastic quantization remains limited, particularly for large language models.This paper proposes QuEPT, an efficient post-training scheme that reconstructs block-wise multi-bit errors with one-shot calibration on a small data slice. It can dynamically adapt to various predefined bit-widths by cascading different low-rank adapters, and supports real-time switching between uniform quantization and mixed precision quantization without repeated optimization. To enhance accuracy and robustness, we introduce Multi-Bit Token Merging (MB-ToMe) to dynamically fuse token features across different bit-widths, improving robustness during bit-width switching. Additionally, we propose Multi-Bit Cascaded Low-Rank adapters (MB-CLoRA) to strengthen correlations between bit-width groups, further improve the overall performance of QuEPT. Extensive experiments demonstrate that QuEPT achieves comparable or better performance to existing state-of-the-art post-training quantization methods.Our code is available at https://github.com/xuke225/QuEPT

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T04:28:06Z。旧 registry Updated:v1：2026-02-16T01:20:21Z（不作首公开）。

## 2602.12612

[Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback](https://arxiv.org/abs/2602.12612v1)

Traditional methods for automating recommender system design, such as Neural Architecture Search (NAS), are often constrained by a fixed search space defined by human priors, limiting innovation to pre-defined operators. While recent LLM-driven code evolution frameworks shift fixed search space target to open-ended program spaces, they primarily rely on scalar metrics (e.g., NDCG, Hit Ratio) that fail to provide qualitative insights into model failures or directional guidance for improvement. To address this, we propose Self-EvolveRec, a novel framework that establishes a directional feedback loop by integrating a User Simulator for qualitative critiques and a Model Diagnosis Tool for quantitative internal verification. Furthermore, we introduce a Diagnosis Tool - Model Co-Evolution strategy to ensure that evaluation criteria dynamically adapt as the recommendation architecture evolves. Extensive experiments demonstrate that Self-EvolveRec significantly outperforms state-of-the-art NAS and LLM-driven code evolution baselines in both recommendation performance and user satisfaction. Our code is available at https://github.com/Sein-Kim/self_evolverec.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T04:38:32Z。旧 registry Updated:v1：2026-02-16T01:20:39Z（不作首公开）。

## 2602.12617

[GeoAgent: Learning to Geolocate Everywhere with Reinforced Geographic Characteristics](https://arxiv.org/abs/2602.12617v1)

This paper presents GeoAgent, a model capable of reasoning closely with humans and deriving fine-grained address conclusions. Previous RL-based methods have achieved breakthroughs in performance and interpretability but still remain concerns because of their reliance on AI-generated chain-of-thought (CoT) data and training strategies, which conflict with geographic characteristics. To address these issues, we first introduce GeoSeek, a new geolocation dataset comprising CoT data annotated by geographic experts and professional players. We further thoroughly explore the inherent characteristics of geographic tasks and propose a geo-similarity reward and a consistency reward assessed by a consistency agent to assist training. This encourages the model to converge towards correct answers from a geographic perspective while ensuring the integrity and consistency of its reasoning process. Experimental results show that GeoAgent outperforms existing methods and a series of general VLLMs across multiple grains, while generating reasoning that closely aligns with humans.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T04:48:05Z。旧 registry Updated:v1：2026-02-16T01:21:02Z（不作首公开）。

## 2602.12618

[Vision Token Reduction via Attention-Driven Self-Compression for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2602.12618v1)

Multimodal Large Language Models (MLLMs) incur significant computational cost from processing numerous vision tokens through all LLM layers. Prior pruning methods operate either before the LLM, limiting generality due to diverse encoder-projector designs or within the LLM using heuristics that are incompatible with FlashAttention. We take a different approach: rather than identifying unimportant tokens, we treat the LLM itself as the optimal guide for compression. Observing that deeper layers naturally transmit vision-to-text information, we introduce Attention-Driven Self-Compression (ADSC), a simple, broadly applicable method that progressively reduces vision tokens using only the LLM's attention mechanism. Our method applies uniform token downsampling at selected layers, forming bottlenecks that encourage the model to reorganize and compress information into the remaining tokens. It requires no score computation, auxiliary modules, or attention modification, and remains fully compatible with FlashAttention. Applied to LLaVA-1.5, ADSC reduces FLOPs by 53.7% and peak KV-cache memory by 56.7%, while preserving 98.2% of the original model performance. Across multiple benchmarks, it outperforms prior pruning approaches in both efficiency and accuracy. Crucially, under high compression ratios, our method remains robust while heuristic-based techniques degrade sharply.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T04:49:27Z。旧 registry Updated:v1：2026-02-16T01:21:05Z（不作首公开）。

## 2602.12624

[Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Timesteps](https://arxiv.org/abs/2602.12624v1)

Diffusion-based generative models have achieved remarkable performance across various domains, yet their practical deployment is often limited by high sampling costs. While prior work focuses on training objectives or individual solvers, the holistic design of sampling, specifically solver selection and scheduling, remains dominated by static heuristics. In this work, we revisit this challenge through a geometric lens, proposing SDM, a principled framework that aligns the numerical solver with the intrinsic properties of the diffusion trajectory. By analyzing the ODE dynamics, we show that efficient low-order solvers suffice in early high-noise stages while higher-order solvers can be progressively deployed to handle the increasing non-linearity of later stages. Furthermore, we formalize the scheduling by introducing a Wasserstein-bounded optimization framework. This method systematically derives adaptive timesteps that explicitly bound the local discretization error, ensuring the sampling process remains faithful to the underlying continuous dynamics. Without requiring additional training or architectural modifications, SDM achieves state-of-the-art performance across standard benchmarks, including an FID of 1.93 on CIFAR-10, 2.41 on FFHQ, and 1.98 on AFHQv2, with a reduced number of function evaluations compared to existing samplers. Our code is available at https://github.com/aiimaginglab/sdm.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T05:02:07Z。旧 registry Updated:v1：2026-02-16T01:21:17Z（不作首公开）。

## 2602.12628

[Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models](https://arxiv.org/abs/2602.12628v1)

Simulation offers a scalable and low-cost way to enrich vision-language-action (VLA) training, reducing reliance on expensive real-robot demonstrations. However, most sim-real co-training methods rely on supervised fine-tuning (SFT), which treats simulation as a static source of demonstrations and does not exploit large-scale closed-loop interaction. Consequently, real-world gains and generalization are often limited. In this paper, we propose an RL-based sim-real Co-training (RL-Co) framework that leverages interactive simulation while preserving real-world capabilities. Our method follows a generic two-stage design: we first warm-start the policy with SFT on a mixture of real and simulated demonstrations, then fine-tune it with reinforcement learning in simulation while adding an auxiliary supervised loss on real-world data to anchor the policy and mitigate catastrophic forgetting. We evaluate our framework on four real-world tabletop manipulation tasks using two representative VLA architectures, OpenVLA and $π_{0.5}$, and observe consistent improvements over real-only fine-tuning and SFT-based co-training, including +24% real-world success on OpenVLA and +20% on $π_{0.5}$. Beyond higher success rates, RL co-training yields stronger generalization to unseen task variations and substantially improved real-world data efficiency, providing a practical and scalable pathway for leveraging simulation to enhance real-robot deployment.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T05:15:50Z。旧 registry Updated:v1：2026-02-16T01:21:44Z（不作首公开）。

## 2602.12630

[TensorCommitments: A Lightweight Verifiable Inference for Language Models](https://arxiv.org/abs/2602.12630v1)

Most large language models (LLMs) run on external clouds: users send a prompt, pay for inference, and must trust that the remote GPU executes the LLM without any adversarial tampering. We critically ask how to achieve verifiable LLM inference, where a prover (the service) must convince a verifier (the client) that an inference was run correctly without rerunning the LLM. Existing cryptographic works are too slow at the LLM scale, while non-cryptographic ones require a strong verifier GPU. We propose TensorCommitments (TCs), a tensor-native proof-of-inference scheme. TC binds the LLM inference to a commitment, an irreversible tag that breaks under tampering, organized in our multivariate Terkle Trees. For LLaMA2, TC adds only 0.97% prover and 0.12% verifier time over inference while improving robustness to tailored LLM attacks by up to 48% over the best prior work requiring a verifier GPU.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T05:23:31Z。旧 registry Updated:v1：2026-02-16T01:21:50Z（不作首公开）。

## 2602.12631

[AI Agents for Inventory Control: Human-LLM-OR Complementarity](https://arxiv.org/abs/2602.12631v1)

Inventory control is a fundamental operations problem in which ordering decisions are traditionally guided by theoretically grounded operations research (OR) algorithms. However, such algorithms often rely on rigid modeling assumptions and can perform poorly when demand distributions shift or relevant contextual information is unavailable. Recent advances in large language models (LLMs) have generated interest in AI agents that can reason flexibly and incorporate rich contextual signals, but it remains unclear how best to incorporate LLM-based methods into traditional decision-making pipelines.
 We study how OR algorithms, LLMs, and humans can interact and complement each other in a multi-period inventory control setting. We construct InventoryBench, a benchmark of over 1,000 inventory instances spanning both synthetic and real-world demand data, designed to stress-test decision rules under demand shifts, seasonality, and uncertain lead times. Through this benchmark, we find that OR-augmented LLM methods outperform either method in isolation, suggesting that these methods are complementary rather than substitutes.
 We further investigate the role of humans through a controlled classroom experiment that embeds LLM recommendations into a human-in-the-loop decision pipeline. Contrary to prior findings that human-AI collaboration can degrade performance, we show that, on average, human-AI teams achieve higher profits than either humans or AI agents operating alone. Beyond this population-level finding, we formalize an individual-level complementarity effect and derive a distribution-free lower bound on the fraction of individuals who benefit from AI collaboration; empirically, we find this fraction to be substantial.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T05:23:46Z。旧 registry Updated:v1：2026-02-16T01:21:51Z（不作首公开）。

## 2602.12635

[Unleashing Low-Bit Inference on Ascend NPUs: A Comprehensive Evaluation of HiFloat Formats](https://arxiv.org/abs/2602.12635v1)

As LLMs scale, low-bit floating-point formats like MXFP and NVFP4 offer new opportunities for precision and efficiency. In this work, we evaluate HiFloat (HiF8 and HiF4), a family of formats tailored for Ascend NPUs. Through rigorous comparison across weight-activation and KV-cache tasks, we provide three key insights: (1) INT8 suits narrow-range data, while floating-point formats excel with high-variance data; (2) in 4-bit regimes, HiF4's hierarchical scaling prevents the accuracy collapse seen in integer formats; and (3) HiFloat is fully compatible with state-of-the-art post-training quantization frameworks. Overall, HiFloat provides a solution for high-efficiency LLM inference on NPUs.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T05:41:31Z。旧 registry Updated:v1：2026-02-16T01:22:20Z（不作首公开）。

## 2602.12640

[ImageRAGTurbo: Towards One-step Text-to-Image Generation with Retrieval-Augmented Diffusion Models](https://arxiv.org/abs/2602.12640v1)

Diffusion models have emerged as the leading approach for text-to-image generation. However, their iterative sampling process, which gradually morphs random noise into coherent images, introduces significant latency that limits their applicability. While recent few-step diffusion models reduce the number of sampling steps to as few as one to four steps, they often compromise image quality and prompt alignment, especially in one-step generation. Additionally, these models require computationally expensive training procedures. To address these limitations, we propose ImageRAGTurbo, a novel approach to efficiently finetune few-step diffusion models via retrieval augmentation. Given a text prompt, we retrieve relevant text-image pairs from a database and use them to condition the generation process. We argue that such retrieved examples provide rich contextual information to the UNet denoiser that helps reduce the number of denoising steps without compromising image quality. Indeed, our initial investigations show that using the retrieved content to edit the denoiser's latent space ($\mathcal{H}$-space) without additional finetuning already improves prompt fidelity. To further improve the quality of the generated images, we augment the UNet denoiser with a trainable adapter in the $\mathcal{H}$-space, which efficiently blends the retrieved content with the target prompt using a cross-attention mechanism. Experimental results on fast text-to-image generation demonstrate that our approach produces high-fidelity images without compromising latency compared to existing methods.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T05:59:57Z。旧 registry Updated:v1：2026-02-16T01:23:01Z（不作首公开）。

## 2602.12641

[Artic: AI-oriented Real-time Communication for MLLM Video Assistant](https://arxiv.org/abs/2602.12641v1)

AI Video Assistant emerges as a new paradigm for Real-time Communication (RTC), where one peer is a Multimodal Large Language Model (MLLM) deployed in the cloud. This makes interaction between humans and AI more intuitive, akin to chatting with a real person. However, a fundamental mismatch exists between current RTC frameworks and AI Video Assistants, stemming from the drastic shift in Quality of Experience (QoE) and more challenging networks. Measurements on our production prototype also confirm that current RTC fails, causing latency spikes and accuracy drops.
 To address these challenges, we propose Artic, an AI-oriented RTC framework for MLLM Video Assistants, exploring the shift from "humans watching video" to "AI understanding video." Specifically, Artic proposes: (1) Response Capability-aware Adaptive Bitrate, which utilizes MLLM accuracy saturation to proactively cap bitrate, reserving bandwidth headroom to absorb future fluctuations for latency reduction; (2) Zero-overhead Context-aware Streaming, which allocates limited bitrate to regions most important for the response, maintaining accuracy even under ultra-low bitrates; and (3) Degraded Video Understanding Benchmark, the first benchmark evaluating how RTC-induced video degradation affects MLLM accuracy. Prototype experiments using real-world uplink traces show that compared with existing methods, Artic significantly improves accuracy by 15.12% and reduces latency by 135.31 ms. We will release the benchmark and codes at https://github.com/pku-netvideo/DeViBench.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T06:00:17Z。旧 registry Updated:v1：2026-02-16T01:23:04Z（不作首公开）。

## 2602.12642

[Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR](https://arxiv.org/abs/2602.12642v1)

Reward-maximizing RL methods have shown to be capable of enhancing the reasoning performance of LLMs, but often lead to reduced generation diversity. Recent works address this issue by adopting GFlowNets, training LLMs to match a target distribution while jointly learning its partition function. In contrast to prior works that treat this partition function solely as a normalizer, we reinterpret it as a per-prompt expected-reward (i.e., online accuracy) signal, leveraging this unused information to improve sample efficiency. Specifically, we first establish a theoretical relationship between the partition function and per-prompt accuracy estimates. Building on this key insight, we propose Partition Function-Guided RL (PACED-RL), a post-training framework that leverages accuracy estimates to prioritize informative question prompts during training, and further improves sample efficiency through an accuracy estimate error-prioritized replay. Crucially, both components reuse information already produced during GFlowNet training, effectively amortizing the compute overhead into the existing optimization process. Extensive experiments across diverse benchmarks demonstrate strong performance improvements over GRPO and prior GFlowNet approaches, highlighting PACED-RL as a promising direction for a more sample efficient distribution-matching training for LLMs.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T06:04:14Z。旧 registry Updated:v1：2026-02-16T01:23:09Z（不作首公开）。

## 2602.12660

[Learning Ordinal Probabilistic Reward from Preferences](https://arxiv.org/abs/2602.12660v1)

Reward models are crucial for aligning large language models (LLMs) with human values and intentions. Existing approaches follow either Generative (GRMs) or Discriminative (DRMs) paradigms, yet both suffer from limitations: GRMs typically demand costly point-wise supervision, while DRMs produce uncalibrated relative scores that lack probabilistic interpretation. To address these challenges, we introduce a novel reward modeling paradigm: Probabilistic Reward Model (PRM). Instead of modeling reward as a deterministic scalar, our approach treats it as a random variable, learning a full probability distribution for the quality of each response. To make this paradigm practical, we present its closed-form, discrete realization: the Ordinal Probabilistic Reward Model (OPRM), which discretizes the quality score into a finite set of ordinal ratings. Building on OPRM, we propose a data-efficient training strategy called Region Flooding Tuning (RgFT). It enables rewards to better reflect absolute text quality by incorporating quality-level annotations, which guide the model to concentrate the probability mass within corresponding rating sub-regions. Experiments on various reward model benchmarks show that our method improves accuracy by $\textbf{2.9%}\sim\textbf{7.4%}$ compared to prior reward models, demonstrating strong performance and data efficiency. Analysis of the score distribution provides evidence that our method captures not only relative rankings but also absolute quality.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T06:43:02Z。旧 registry Updated:v1：2026-02-16T01:24:36Z（不作首公开）。

## 2602.12662

[Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents](https://arxiv.org/abs/2602.12662v1)

Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horizon tasks, where cognitive demands vary significantly from step to step, with some requiring strategic planning and others only routine execution. In this paper, we introduce CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step. Grounded in ACT-R theory, we design four hierarchical cognitive levels ranging from instinctive responses to strategic planning. Our two-stage training approach includes Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment via confidence-aware advantage reweighting. The key insight is that appropriate cognitive depth should maximize the confidence of the resulting action. Experiments on ALFWorld and ScienceWorld demonstrate that CogRouter achieves state-of-the-art performance with superior efficiency. With Qwen2.5-7B, it reaches an 82.3% success rate, outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while using 62% fewer tokens.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T06:52:09Z。旧 registry Updated:v1：2026-02-16T01:24:45Z（不作首公开）。

## 2602.12665

[Evaluating Robustness of Reasoning Models on Parameterized Logical Problems](https://arxiv.org/abs/2602.12665v1)

Logic provides a controlled testbed for evaluating LLM-based reasoners, yet standard SAT-style benchmarks often conflate surface difficulty (length, wording, clause order) with the structural phenomena that actually determine satisfiability. We introduce a diagnostic benchmark for 2-SAT built from parameterized families of structured 2--CNF formulas, where satisfiability is characterized by the implication graph and can be tuned along interpretable axes. Our generators isolate distinct competencies and failure modes: (i) contradiction-cycle UNSAT cores with controllable size and imbalance, (ii) SAT instances with a prescribed fraction of free variables to control solution multiplicity, (iii) planted backbones that modulate propagation, (iv) late bridge clauses that couple otherwise monotone regions to probe sensitivity to ordering and revision, and (v) symmetry/duplication variants that test abstraction under renaming and redundant structure. We evaluate LLM-based reasoners on decision accuracy and assignment validity, and quantify robustness under semantics-preserving perturbations such as clause reordering, filler clauses, and variable renaming. Across models, we observe sharp performance transitions under targeted structural interventions even when surface statistics are held fixed, revealing brittleness regimes that are invisible to aggregate SAT accuracy.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T06:54:25Z。旧 registry Updated:v1：2026-02-16T01:24:49Z（不作首公开）。

## 2602.12669

[Characterize LSM-tree Compaction Performance via On-Device LLM Inference](https://arxiv.org/abs/2602.12669v1)

Modern key-value storage engines built on Log-Structured Merge-trees (LSM-trees), such as RocksDB and LevelDB, rely heavily on the performance of their compaction operations, which are impacted by a complex set of interdependent configuration parameters. Manually tuning these parameters for optimal performance demands considerable expertise, while traditional auto-tuning approaches struggle with the enormous search space and low sample efficiency inherent to this domain. In recent years, Large Language Models (LLMs) have demonstrated strong capabilities in code generation and logical reasoning, offering new possibilities for system optimization. However, applying LLMs to real-time compaction tuning in such latency-sensitive environments is a double-edged sword. While large-scale LLMs can offer superior reasoning for strategy generation, their high inference latency and computational cost make them impractical for interactive, low-latency tuning. In contrast, small-scale LLMs achieve low latency but often at the expense of reasoning accuracy and tuning effectiveness. In this paper, we first evaluate this trade-off by analyzing the compaction-tuning performance and inference latency of LLMs at different scales in an LSM-tree-based tuning case. We then characterize the performance of LSM-tree on RocksDB v8.8.1, with a focus on adjusting the key compaction-related parameters under db_bench workloads. Our experimental results show a clear positive correlation between model capability and tuning effectiveness.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:02:28Z。旧 registry Updated:v1：2026-02-16T01:25:07Z（不作首公开）。

## 2602.12670

[SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670v1)

Agent Skills are structured packages of procedural knowledge that augment large language model (LLM) agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark whose current inventory contains 87 tasks across 8 domains paired with curated Skills and deterministic verifiers. Our latest aggregate evaluation runs the 87-task benchmark under matched no-Skills and curated-Skills conditions for 18 model-harness configurations. Curated Skills raise the average pass rate from 33.9% to 50.5% (+16.6 percentage points; 25.5% normalized gain), with configuration-level gains ranging from +4.1 to +25.7 pp. Focused Skills with at most three modules outperform larger or exhaustive bundles, and smaller models with Skills can match larger models without them. SkillsBench establishes paired evaluation as the foundation for rigorous measurement of Skill efficacy on agentic, expertise-heavy work.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:06:06Z。旧 registry Updated:v1：2026-02-16T01:25:08Z（不作首公开）。

## 2602.12674

[$\mathcal{X}$-KD: General Experiential Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2602.12674v1)

Knowledge Distillation (KD) for Large Language Models (LLMs) has become increasingly important as models grow in size and complexity. While existing distillation approaches focus on imitating teacher behavior, they often overlook the original learning environment that shaped the teacher's knowledge. Inspired by the experiential learning theory and inverse reinforcement learning, we propose Experiential Knowledge Distillation ($\mathcal{X}$-KD), a novel and general framework that enables student models to learn in the teacher's original learning environment. $\mathcal{X}$-KD adopts the Approximated Variational Reward Imitation Learning (AVRIL) framework to jointly model the teacher's original reward function and perform policy distillation, encouraging consistency between the student policy and the original reward function. Our derivation demonstrates that $\mathcal{X}$-KD follows the supervised learning framework and applies to both sequence-level and divergence-based distillation methods, underlining the simplicity and flexibility of our approach. Empirical results show that $\mathcal{X}$-KD outperforms the generalized KD and MiniLLM baselines on abstractive summarization, machine translation, and arithmetic reasoning tasks. Additionally, $\mathcal{X}$-KD achieves better performance-diversity trade-off and data efficiency than baseline KD approaches.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:15:10Z。旧 registry Updated:v1：2026-02-16T01:25:31Z（不作首公开）。

## 2602.12675

[SLA2: Sparse-Linear Attention with Learnable Routing and QAT](https://arxiv.org/abs/2602.12675v1)

Sparse-Linear Attention (SLA) combines sparse and linear attention to accelerate diffusion models and has shown strong performance in video generation. However, (i) SLA relies on a heuristic split that assigns computations to the sparse or linear branch based on attention-weight magnitude, which can be suboptimal. Additionally, (ii) after formally analyzing the attention error in SLA, we identify a mismatch between SLA and a direct decomposition into sparse and linear attention. We propose SLA2, which introduces (I) a learnable router that dynamically selects whether each attention computation should use sparse or linear attention, (II) a more faithful and direct sparse-linear attention formulation that uses a learnable ratio to combine the sparse and linear attention branches, and (III) a sparse + low-bit attention design, where low-bit attention is introduced via quantization-aware fine-tuning to reduce quantization error. Experiments show that on video diffusion models, SLA2 can achieve 97% attention sparsity and deliver an 18.6x attention speedup while preserving generation quality.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:16:02Z。旧 registry Updated:v1：2026-02-16T01:25:32Z（不作首公开）。

## 2602.12683

[Flow Matching from Viewpoint of Proximal Operators](https://arxiv.org/abs/2602.12683v1)

We reformulate Optimal Transport Conditional Flow Matching (OT-CFM), a class of dynamical generative models, showing that it admits an exact proximal formulation via an extended Brenier potential, without assuming that the target distribution has a density. In particular, the mapping to recover the target point is exactly given by a proximal operator, which yields an explicit proximal expression of the vector field. We also discuss the convergence of minibatch OT-CFM to the population formulation as the batch size increases. Finally, using second epi-derivatives of convex potentials, we prove that, for manifold-supported targets, OT-CFM is terminally normally hyperbolic: after time rescaling, the dynamics contracts exponentially in directions normal to the data manifold while remaining neutral along tangential directions.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:30:23Z。旧 registry Updated:v1：2026-02-16T01:26:15Z（不作首公开）。

## 2602.12684

[Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution](https://arxiv.org/abs/2602.12684v1)

In this report, we introduce Xiaomi-Robotics-0, an advanced vision-language-action (VLA) model optimized for high performance and fast and smooth real-time execution. The key to our method lies in a carefully designed training recipe and deployment strategy. Xiaomi-Robotics-0 is first pre-trained on large-scale cross-embodiment robot trajectories and vision-language data, endowing it with broad and generalizable action-generation capabilities while avoiding catastrophic forgetting of the visual-semantic knowledge of the underlying pre-trained VLM. During post-training, we propose several techniques for training the VLA model for asynchronous execution to address the inference latency during real-robot rollouts. During deployment, we carefully align the timesteps of consecutive predicted action chunks to ensure continuous and seamless real-time rollouts. We evaluate Xiaomi-Robotics-0 extensively in simulation benchmarks and on two challenging real-robot tasks that require precise and dexterous bimanual manipulation. Results show that our method achieves state-of-the-art performance across all simulation benchmarks. Moreover, Xiaomi-Robotics-0 can roll out fast and smoothly on real robots using a consumer-grade GPU, achieving high success rates and throughput on both real-robot tasks. To facilitate future research, code and model checkpoints are open-sourced at https://xiaomi-robotics-0.github.io

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:30:43Z。旧 registry Updated:v1：2026-02-16T01:26:16Z（不作首公开）。

## 2602.12687

[Trust the uncertain teacher: distilling dark knowledge via calibrated uncertainty](https://arxiv.org/abs/2602.12687v1)

The core of knowledge distillation lies in transferring the teacher's rich 'dark knowledge'-subtle probabilistic patterns that reveal how classes are related and the distribution of uncertainties. While this idea is well established, teachers trained with conventional cross-entropy often fail to preserve such signals. Their distributions collapse into sharp, overconfident peaks that appear decisive but are in fact brittle, offering little beyond the hard label or subtly hindering representation-level transfer. This overconfidence is especially problematic in high-cardinality tasks, where the nuances among many plausible classes matter most for guiding a compact student. Moreover, such brittle targets reduce robustness under distribution shift, leaving students vulnerable to miscalibration in real-world conditions. To address this limitation, we revisit distillation from a distributional perspective and propose Calibrated Uncertainty Distillation (CUD), a framework designed to make dark knowledge more faithfully accessible. Instead of uncritically adopting the teacher's overconfidence, CUD encourages teachers to reveal uncertainty where it is informative and guides students to learn from targets that are calibrated rather than sharpened certainty. By directly shaping the teacher's predictive distribution before transfer, our approach balances accuracy and calibration, allowing students to benefit from both confident signals on easy cases and structured uncertainty on hard ones. Across diverse benchmarks, CUD yields students that are not only more accurate, but also more calibrated under shift and more reliable on ambiguous, long-tail inputs.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:43:19Z。旧 registry Updated:v1：2026-02-16T01:26:33Z（不作首公开）。

## 2602.12691

[ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training](https://arxiv.org/abs/2602.12691v1)

We study how to improve large foundation vision-language-action (VLA) systems through human-in-the-loop reinforcement learning (RL) in real-world environments. A key challenge is learning reliable value functions from heterogeneous real-world experience, as value estimation provides the primary learning signal for VLA training. In practice, replay buffers contain trajectories collected from historical policies, online rollouts, demonstrations, and intermittent human interventions. Because replay buffers mix trajectories generated by different behaviors, the observed returns can be mismatched with the quality of the current policy. Prior VLA post-training methods often rely on progress-style value signals, which reflect the average quality of historical behaviors, leading to mismatched learning signals for the current policy. In this paper, we propose ALOE, an off-policy evaluation framework whose value function directly evaluates current-policy behavior for each iteration. Specifically, ALOE combines chunked temporal-difference bootstrapping and conservative value aggregation to perform stable current-policy evaluation, then uses these estimates for advantage-weighted policy improvement. This design improves credit assignment to critical action chunks under sparse rewards and supports stable policy improvement. We evaluate ALOE on four real-world manipulation tasks encompassing long-horizon and high-precision scenarios: smartphone packing, laundry folding, multi-object sorting, and phone assembly. Across all tasks, ALOE outperforms other VLA post-training methods, highlighting the benefit of off-policy value estimates for real-world VLA post-training. Videos are available at our project website https://rooshy-yang.github.io/aloe.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T07:46:37Z。旧 registry Updated:v1：2026-02-16T01:26:40Z（不作首公开）。

## 2602.12705

[MedXIAOHE: A Comprehensive Recipe for Building Medical MLLMs](https://arxiv.org/abs/2602.12705v1)

We present MedXIAOHE, a medical vision-language foundation model designed to advance general-purpose medical understanding and reasoning in real-world clinical applications. MedXIAOHE achieves state-of-the-art performance across diverse medical benchmarks and surpasses leading closed-source multimodal systems on multiple capabilities. To achieve this, we propose an entity-aware continual pretraining framework that organizes heterogeneous medical corpora to broaden knowledge coverage and reduce long-tail gaps (e.g., rare diseases). For medical expert-level reasoning and interaction, MedXIAOHE incorporates diverse medical reasoning patterns via reinforcement learning and tool-augmented agentic training, enabling multi-step diagnostic reasoning with verifiable decision traces. To improve reliability in real-world use, MedXIAOHE integrates user-preference rubrics, evidence-grounded reasoning, and low-hallucination long-form report generation, with improved adherence to medical instructions. We release this report to document our practical design choices, scaling insights, and evaluation framework, hoping to inspire further research.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T08:19:38Z。旧 registry Updated:v1：2026-02-16T01:27:55Z（不作首公开）。

## 2602.12709

[ReFilter: Improving Robustness of Retrieval-Augmented Generation via Gated Filter](https://arxiv.org/abs/2602.12709v1)

Retrieval-augmented generation (RAG) has become a dominant paradigm for grounding large language models (LLMs) with external evidence in knowledge-intensive question answering. A core design choice is how to fuse retrieved samples into the LLMs, where existing internal fusion approaches broadly fall into query-based fusion, parametric fusion, and latent-based fusion. Despite their effectiveness at modest retrieval scales, these methods often fail to scale gracefully as the number of retrieved candidates k increases: Larger k improves evidence coverage, yet realistic top-k retrieval inevitably contains irrelevant or redundant content and increases the inference cost.
 To address these limitations, we propose ReFilter, a novel latent-based fusion framework that performs token-level filtering and fusion. ReFilter consists of three key components: a context encoder for encoding context features, a gated filter for weighting each token, and a token fusion module for integrating the weighted token feature into the LLM's hidden states. Our experiments across four general-domain QA benchmarks show that ReFilter consistently achieves the best average performance under both in-domain adaptation and out-of-domain transfer. ReFilter further generalizes to five biomedical QA benchmarks in zero-shot transfer without domain fine-tuning, reaching 70.01% average accuracy with Qwen2.5-14B-Instruct.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T08:25:26Z。旧 registry Updated:v1：2026-02-16T01:28:29Z（不作首公开）。

## 2602.12714

[ADEPT: RL-Aligned Agentic Decoding of Emotion via Evidence Probing Tools -- From Consensus Learning to Ambiguity-Driven Emotion Reasoning](https://arxiv.org/abs/2602.12714v1)

Speech Large Language Models (SLLMs) enable high-level emotion reasoning but often produce ungrounded, text-biased judgments without verifiable acoustic evidence. In contrast, self-supervised speech encoders such as WavLM provide strong acoustic representations yet remain opaque discriminative models with limited interpretability. To bridge this gap, we introduce ADEPT (Agentic Decoding of Emotion via Evidence Probing Tools), a framework that reframes emotion recognition as a multi-turn inquiry process rather than a single-pass prediction. ADEPT transforms an SLLM into an agent that maintains an evolving candidate emotion set and adaptively invokes dedicated semantic and acoustic probing tools within a structured pipeline of candidate generation, evidence collection, and adjudication. Crucially, ADEPT enables a paradigm shift from consensus learning to ambiguity-driven emotion reasoning. Since human affect exhibits inherent complexity and frequent co-occurrence of emotions, we treat minority annotations as informative perceptual signals rather than discarding them as noise. Finally, we integrate Group Relative Policy Optimization (GRPO) with an Evidence Trust Gate to explicitly couple tool-usage behaviors with prediction quality and enforce evidence-grounded reasoning. Experiments show that ADEPT improves primary emotion accuracy in most settings while substantially improving minor emotion characterization, producing explanations grounded in auditable acoustic and semantic evidence.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T08:33:37Z。旧 registry Updated:v1：2026-02-16T01:28:56Z（不作首公开）。

## 2602.12727

[Training Dense Retrievers with Multiple Positive Passages](https://arxiv.org/abs/2602.12727v1)

Modern knowledge-intensive systems, such as retrieval-augmented generation (RAG), rely on effective retrievers to establish the performance ceiling for downstream modules. However, retriever training has been bottlenecked by sparse, single-positive annotations, which lead to false-negative noise and suboptimal supervision. While the advent of large language models (LLMs) makes it feasible to collect comprehensive multi-positive relevance labels at scale, the optimal strategy for incorporating these dense signals into training remains poorly understood. In this paper, we present a systematic study of multi-positive optimization objectives for retriever training. We unify representative objectives, including Joint Likelihood (JointLH), Summed Marginal Likelihood (SumMargLH), and Log-Sum-Exp Pairwise (LSEPair) loss, under a shared contrastive learning framework. Our theoretical analysis characterizes their distinct gradient behaviors, revealing how each allocates probability mass across positive document sets. Empirically, we conduct extensive evaluations on Natural Questions, MS MARCO, and the BEIR benchmark across two realistic regimes: homogeneous LLM-annotated data and heterogeneous mixtures of human and LLM labels. Our results show that LSEPair consistently achieves superior robustness and performance across settings, while JointLH and SumMargLH exhibit high sensitivity to the quality of positives. Furthermore, we find that the simple strategy of random sampling (Rand1LH) serves as a reliable baseline. By aligning theoretical insights with empirical findings, we provide practical design principles for leveraging dense, LLM-augmented supervision to enhance retriever effectiveness.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T08:56:52Z。旧 registry Updated:v1：2026-02-16T01:29:59Z（不作首公开）。

## 2602.12734

[Scaling Single Human Demonstrations for Imitation Learning using Generative Foundational Models](https://arxiv.org/abs/2602.12734v1)

Imitation learning is a popular paradigm to teach robots new tasks, but collecting robot demonstrations through teleoperation or kinesthetic teaching is tedious and time-consuming. In contrast, directly demonstrating a task using our human embodiment is much easier and data is available in abundance, yet transfer to the robot can be non-trivial. In this work, we propose Real2Gen to train a manipulation policy from a single human demonstration. Real2Gen extracts required information from the demonstration and transfers it to a simulation environment, where a programmable expert agent can demonstrate the task arbitrarily many times, generating an unlimited amount of data to train a flow matching policy. We evaluate Real2Gen on human demonstrations from three different real-world tasks and compare it to a recent baseline. Real2Gen shows an average increase in the success rate of 26.6% and better generalization of the trained policy due to the abundance and diversity of training data. We further deploy our purely simulation-trained policy zero-shot in the real world. We make the data, code, and trained models publicly available at real2gen.cs.uni-freiburg.de.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:04:18Z。旧 registry Updated:v1：2026-02-16T01:30:13Z（不作首公开）。

## 2602.12735

[VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph](https://arxiv.org/abs/2602.12735v1)

Effectively retrieving, reasoning, and understanding multimodal information remains a critical challenge for agentic systems. Traditional Retrieval-augmented Generation (RAG) methods rely on linear interaction histories, which struggle to handle long-context tasks, especially those involving information-sparse yet token-heavy visual data in iterative reasoning scenarios. To bridge this gap, we introduce VimRAG, a framework tailored for multimodal Retrieval-augmented Reasoning across text, images, and videos. Inspired by our systematic study, we model the reasoning process as a dynamic directed acyclic graph that structures the agent states and retrieved multimodal evidence. Building upon this structured memory, we introduce a Graph-Modulated Visual Memory Encoding mechanism, with which the significance of memory nodes is evaluated via their topological position, allowing the model to dynamically allocate high-resolution tokens to pivotal evidence while compressing or discarding trivial clues. To implement this paradigm, we propose a Graph-Guided Policy Optimization strategy. This strategy disentangles step-wise validity from trajectory-level rewards by pruning memory nodes associated with redundant actions, thereby facilitating fine-grained credit assignment. Extensive experiments demonstrate that VimRAG consistently achieves state-of-the-art performance on diverse multimodal RAG benchmarks. The code is available at https://github.com/Alibaba-NLP/VRAG.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:05:09Z。旧 registry Updated:v1：2026-02-16T01:30:15Z（不作首公开）。

## 2602.12746

[Lamer-SSL: Layer-aware Mixture of LoRA Experts for Continual Multilingual Expansion of Self-supervised Models without Forgetting](https://arxiv.org/abs/2602.12746v1)

Despite their impressive performance, self-supervised speech models often struggle to generalize to new languages and tend to forget previously acquired knowledge during continual training. To address this, we propose Lamer-SSL, a parameter-efficient framework that integrates a Layer-Aware MixturE of LoRA Experts (Lamer) module with a replay strategy. The Lamer module enables flexible balancing between shared and language-specific representations, while layer-aware expert allocation assigns more experts to deeper layers where semantic information is richer. Meanwhile, the replay strategy retains prior knowledge using minimal data, mitigating forgetting during continual training. Experiments on automatic speech recognition (ASR) and language identification (LID) demonstrate that Lamer-SSL extends self-supervised models to new languages effectively while maintaining strong performance on previously learned languages with only 2.14% parameters being trainable.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:22:22Z。旧 registry Updated:v1：2026-02-16T01:30:59Z（不作首公开）。

## 2602.12755

[Towards reconstructing experimental sparse-view X-ray CT data with diffusion models](https://arxiv.org/abs/2602.12755v1)

Diffusion-based image generators are promising priors for ill-posed inverse problems like sparse-view X-ray Computed Tomography (CT). As most studies consider synthetic data, it is not clear whether training data mismatch (``domain shift'') or forward model mismatch complicate their successful application to experimental data. We measured CT data from a physical phantom resembling the synthetic Shepp-Logan phantom and trained diffusion priors on synthetic image data sets with different degrees of domain shift towards it. Then, we employed the priors in a Decomposed Diffusion Sampling scheme on sparse-view CT data sets with increasing difficulty leading to the experimental data. Our results reveal that domain shift plays a nuanced role: while severe mismatch causes model collapse and hallucinations, diverse priors match or exceed well-matched but narrow priors. Forward model mismatch pulls the image samples away from the prior manifold, which causes artifacts but can be mitigated with annealed likelihood weight schedules that also increase computational efficiency. Overall, we demonstrate that performance gains do not immediately translate from synthetic to experimental data, and future development must validate against real-world benchmarks.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:33:39Z。旧 registry Updated:v1：2026-02-16T01:31:35Z（不作首公开）。

## 2602.12756

[Closing the Loop: A Control-Theoretic Framework for Provably Stable Time Series Forecasting with LLMs](https://arxiv.org/abs/2602.12756v1)

Large Language Models (LLMs) have recently shown exceptional potential in time series forecasting (TSF), leveraging their inherent sequential reasoning capabilities to model complex temporal dynamics. Existing approaches typically employ an autoregressive generation strategy to adapt LLMs for TSF. However, we identify a theoretical flaw in this paradigm: during inference, the model operates in an open-loop manner, recursively consuming its own generated outputs. This leads to error accumulation, where minor early deviations cascade into significant rollout drift over long horizons. In this paper, we reformulate autoregressive forecasting through the lens of control theory, proposing Feedback-driven LLM (F-LLM), a novel closed-loop framework. Unlike standard methods that passively propagate errors, F-LLM actively stabilizes the trajectory via a learnable residual estimator functioning as a system observer. Furthermore, we provide a mathematical proof that, under explicit contraction assumptions, this closed-loop mechanism guarantees a uniformly bounded step-wise error sequence within the local surrogate dynamics. Extensive experiments demonstrate that F-LLM significantly mitigates error propagation, achieving good performance on time series benchmarks. Our code is publicly available at https://github.com/Zh-XY22/F-LLM.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:35:12Z。旧 registry Updated:v1：2026-02-16T01:31:36Z（不作首公开）。

## 2602.12769

[PixelRush: Ultra-Fast, Training-Free High-Resolution Image Generation via One-step Diffusion](https://arxiv.org/abs/2602.12769v1)

Pre-trained diffusion models excel at generating high-quality images but remain inherently limited by their native training resolution. Recent training-free approaches have attempted to overcome this constraint by introducing interventions during the denoising process; however, these methods incur substantial computational overhead, often requiring more than five minutes to produce a single 4K image. In this paper, we present PixelRush, the first tuning-free framework for practical high-resolution text-to-image generation. Our method builds upon the established patch-based inference paradigm but eliminates the need for multiple inversion and regeneration cycles. Instead, PixelRush enables efficient patch-based denoising within a low-step regime. To address artifacts introduced by patch blending in few-step generation, we propose a seamless blending strategy. Furthermore, we mitigate over-smoothing effects through a noise injection mechanism. PixelRush delivers exceptional efficiency, generating 4K images in approximately 20 seconds representing a 10$\times$ to 35$\times$ speedup over state-of-the-art methods while maintaining superior visual fidelity. Extensive experiments validate both the performance gains and the quality of outputs achieved by our approach.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:54:27Z。旧 registry Updated:v1：2026-02-16T01:32:29Z（不作首公开）。

## 2602.12774

[Bootstrapping MLLM for Weakly-Supervised Class-Agnostic Object Counting](https://arxiv.org/abs/2602.12774v1)

Object counting is a fundamental task in computer vision, with broad applicability in many real-world scenarios. Fully-supervised counting methods require costly point-level annotations per object. Few weakly-supervised methods leverage only image-level object counts as supervision and achieve fairly promising results. They are, however, often limited to counting a single category, e.g. person. In this paper, we propose WS-COC, the first MLLM-driven weakly-supervised framework for class-agnostic object counting. Instead of directly fine-tuning MLLMs to predict object counts, which can be challenging due to the modality gap, we incorporate three simple yet effective strategies to bootstrap the counting paradigm in both training and testing: First, a divide-and-discern dialogue tuning strategy is proposed to guide the MLLM to determine whether the object count falls within a specific range and progressively break down the range through multi-round dialogue. Second, a compare-and-rank count optimization strategy is introduced to train the MLLM to optimize the relative ranking of multiple images according to their object counts. Third, a global-and-local counting enhancement strategy aggregates and fuses local and global count predictions to improve counting performance in dense scenes. Extensive experiments on FSC-147, CARPK, PUCPR+, and ShanghaiTech show that WS-COC matches or even surpasses many state-of-art fully-supervised methods while significantly reducing annotation costs. Code is available at https://github.com/viscom-tongji/WS-COC.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T09:58:35Z。旧 registry Updated:v1：2026-02-16T01:32:46Z（不作首公开）。

## 2602.12778

[Aspect-Based Sentiment Analysis for Future Tourism Experiences: A BERT-MoE Framework for Persian User Reviews](https://arxiv.org/abs/2602.12778v1)

This study advances aspect-based sentiment analysis (ABSA) for Persian-language user reviews in the tourism domain, addressing challenges of low-resource languages. We propose a hybrid BERT-based model with Top-K routing and auxiliary losses to mitigate routing collapse and improve efficiency. The pipeline includes: (1) overall sentiment classification using BERT on 9,558 labeled reviews, (2) multi-label aspect extraction for six tourism-related aspects (host, price, location, amenities, cleanliness, connectivity), and (3) integrated ABSA with dynamic routing. The dataset consists of 58,473 preprocessed reviews from the Iranian accommodation platform Jabama, manually annotated for aspects and sentiments. The proposed model achieves a weighted F1-score of 90.6% for ABSA, outperforming baseline BERT (89.25%) and a standard hybrid approach (85.7%). Key efficiency gains include a 39% reduction in GPU power consumption compared to dense BERT, supporting sustainable AI deployment in alignment with UN SDGs 9 and 12. Analysis reveals high mention rates for cleanliness and amenities as critical aspects. This is the first ABSA study focused on Persian tourism reviews, and we release the annotated dataset to facilitate future multilingual NLP research in tourism.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T10:01:33Z。旧 registry Updated:v1：2026-02-16T01:32:56Z（不作首公开）。

## 2602.12779

[iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision](https://arxiv.org/abs/2602.12779v1)

Large Language Models (LLMs) have become indispensable for evaluating writing. However, text feedback they provide is often unintelligible, generic, and not specific to user criteria. Inspired by structured rubrics in education and intelligible AI explanations, we propose iRULER following identified design guidelines to \textit{scaffold} the review process by \textit{specific} criteria, providing \textit{justification} for score selection, and offering \textit{actionable} revisions to target different quality levels. To \textit{qualify} user-defined criteria, we recursively used iRULER with a rubric-of-rubrics to iteratively \textit{refine} rubrics. In controlled experiments on writing revision and rubric creation, iRULER most improved validated LLM-judged review scores and was perceived as most helpful and aligned compared to read-only rubric and text-based LLM feedback. Qualitative findings further support how iRULER satisfies the design guidelines for user-defined feedback. This work contributes interactive rubric tools for intelligible LLM-based review and revision of writing, and user-defined rubric creation.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T10:02:25Z。旧 registry Updated:v1：2026-02-16T01:32:58Z（不作首公开）。

## 2602.12806

[RAT-Bench: A Comprehensive Benchmark for Text Anonymization](https://arxiv.org/abs/2602.12806v1)

Data containing personal information is increasingly used to train, fine-tune, or query Large Language Models (LLMs). Text is typically scrubbed of identifying information prior to use, often with tools such as Microsoft's Presidio or Anthropic's PII purifier. These tools have traditionally been evaluated on their ability to remove specific identifiers (e.g., names), yet their effectiveness at preventing re-identification remains unclear. We introduce RAT-Bench, a comprehensive benchmark for text anonymization tools based on re-identification risk. Using U.S. demographic statistics, we generate synthetic text containing various direct and indirect identifiers across domains, languages, and difficulty levels. We evaluate a range of NER- and LLM-based text anonymization tools and, based on the attributes an LLM-based attacker is able to correctly infer from the anonymized text, we report the risk of re-identification in the U.S. population, while properly accounting for the disparate impact of identifiers. We find that, while capabilities vary widely, even the best tools are far from perfect in particular when direct identifiers are not written in standard ways and when indirect identifiers enable re-identification. Overall we find LLM-based anonymizers, including new iterative anonymizers, to provide a better privacy-utility trade-off albeit at a higher computational cost. Importantly, we also find them to work well across languages. We conclude with recommendations for future anonymization tools and will release the benchmark and encourage community efforts to expand it, in particular to other geographies.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T10:41:44Z。旧 registry Updated:v1：2026-02-16T01:34:47Z（不作首公开）。

## 2602.12811

[Left-right asymmetry in predicting brain activity from LLMs' representations emerges with their formal linguistic competence](https://arxiv.org/abs/2602.12811v1)

When humans and large language models (LLMs) process the same text, activations in the LLMs correlate with brain activity measured, e.g., with functional magnetic resonance imaging (fMRI). Moreover, it has been shown that, as the training of an LLM progresses, the performance in predicting brain activity from its internal activations improves more in the left hemisphere than in the right one. The aim of the present work is to understand which kind of competence acquired by the LLMs underlies the emergence of this left-right asymmetry. Using the OLMo-2 7B language model at various training checkpoints and fMRI data from English participants, we compare the evolution of the left-right asymmetry in the correlation between brain activity and model predictions alongside performance on several benchmarks. We observe that the asymmetry co-emerges with the formal linguistic abilities of the LLM. These abilities are demonstrated in two ways: by the model's capacity to assign a higher probability to an acceptable sentence than to a grammatically unacceptable one within a minimal contrasting pair, and by its ability to produce well-formed text. By contrast, the left-right asymmetry does not align with the performance on arithmetic or Dyck language tasks; nor with text-based tasks involving world knowledge and reasoning. We generalize these results to another family of LLMs (Pythia) and two other languages, French and Chinese. Our observations indicate that the left-right asymmetry in brain predictivity matches the progress in formal linguistic competence.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T10:46:09Z。旧 registry Updated:v1：2026-02-16T01:34:58Z（不作首公开）。

## 2602.12846

[Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models](https://arxiv.org/abs/2602.12846v1)

Reinforcement Learning with Verifiable Rewards (RLVR) has established itself as the dominant paradigm for instilling rigorous reasoning capabilities in Large Language Models. While effective at amplifying dominant behaviors, we identify a critical pathology in this alignment process: the systematic suppression of valid but rare (low-likelihood under the base model distribution) reasoning paths. We theoretically characterize this phenomenon as a "Normalization Squeeze," where the interplay between mode-seeking policy gradients and finite sampling acts as a high-pass likelihood filter, driving the probability of rare correct traces to statistical extinction. To counteract this collapse without discarding the base model's latent diversity, we propose Amortized Reasoning Tree Search (ARTS). Unlike standard approaches that force internalization via parameter updates, ARTS prioritizes deliberation by decoupling generation from verification. We introduce a Flow Matching objective that repurposes the verifier to estimate the conservation of probability flow, enabling robust navigation through sparse, high-entropy search spaces where traditional discriminative objectives fail. Extensive experiments on the MATH-500 benchmark demonstrate that ARTS achieves a performance of 74.6% (BoN@16), effectively matching fully fine-tuned policies (74.7%) without modifying the generative backbone. Crucially, on the long-tail subset where coupled RL optimization collapses to 0% pass@k, ARTS uniquely recovers significant performance, suggesting that disentangling verification from generation offers a more robust pathway for solving complex reasoning tasks.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T11:52:50Z。旧 registry Updated:v1：2026-02-16T01:37:41Z（不作首公开）。

## 2602.12851

[Chimera: Neuro-Symbolic Attention Primitives for Trustworthy Dataplane Intelligence](https://arxiv.org/abs/2602.12851v1)

Deploying expressive learning models directly on programmable dataplanes promises line-rate, low-latency traffic analysis but remains hindered by strict hardware constraints and the need for predictable, auditable behavior. Chimera introduces a principled framework that maps attention-oriented neural computations and symbolic constraints onto dataplane primitives, enabling trustworthy inference within the match-action pipeline. Chimera combines a kernelized, linearized attention approximation with a two-layer key-selection hierarchy and a cascade fusion mechanism that enforces hard symbolic guarantees while preserving neural expressivity. The design includes a hardware-aware mapping protocol and a two-timescale update scheme that together permit stable, line-rate operation under realistic dataplane budgets. The paper presents the Chimera architecture, a hardware mapping strategy, and empirical evidence showing that neuro-symbolic attention primitives can achieve high-fidelity inference within the resource envelope of commodity programmable switches.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T11:55:06Z。旧 registry Updated:v1：2026-02-16T01:37:48Z（不作首公开）。

## 2602.12852

[WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning](https://arxiv.org/abs/2602.12852v1)

Deep Research systems based on web agents have shown strong potential in solving complex information-seeking tasks, yet their search efficiency remains underexplored. We observe that many state-of-the-art open-source web agents rely on long tool-call trajectories with cyclic reasoning loops and exploration of unproductive branches. To address this, we propose WebClipper, a framework that compresses web agent trajectories via graph-based pruning. Concretely, we model the agent's search process as a state graph and cast trajectory optimization as a minimum-necessary Directed Acyclic Graph (DAG) mining problem, yielding pruned trajectories that preserve essential reasoning while eliminating redundant steps. Continued training on these refined trajectories enables the agent to evolve toward more efficient search patterns and reduces tool-call rounds by about 20% while improving accuracy. Furthermore, we introduce a new metric called F-AE Score to measure the model's overall performance in balancing accuracy and efficiency. Experiments demonstrate that WebClipper compresses tool-call rounds under excellent performance, providing practical insight into balancing effectiveness and efficiency in web agent design.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T11:56:20Z。旧 registry Updated:v1：2026-02-16T01:37:52Z（不作首公开）。

## 2602.12876

[BrowseComp-$V^3$: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents](https://arxiv.org/abs/2602.12876v1)

Multimodal large language models (MLLMs), equipped with increasingly advanced planning and tool-use capabilities, are evolving into autonomous agents capable of performing multimodal web browsing and deep search in open-world environments. However, existing benchmarks for multimodal browsing remain limited in task complexity, evidence accessibility, and evaluation granularity, hindering comprehensive and reproducible assessments of deep search capabilities. To address these limitations, we introduce BrowseComp-$V^3$, a novel benchmark consisting of 300 carefully curated and challenging questions spanning diverse domains. The benchmark emphasizes deep, multi-level, and cross-modal multi-hop reasoning, where critical evidence is interleaved across textual and visual modalities within and across web pages. All supporting evidence is strictly required to be publicly searchable, ensuring fairness and reproducibility. Beyond final-answer accuracy, we incorporate an expert-validated, subgoal-driven process evaluation mechanism that enables fine-grained analysis of intermediate reasoning behaviors and systematic characterization of capability boundaries. In addition, we propose OmniSeeker, a unified multimodal browsing agent framework integrating diverse web search and visual perception tools. Comprehensive experiments demonstrate that even state-of-the-art models achieve only 36% accuracy on our benchmark, revealing critical bottlenecks in multimodal information integration and fine-grained perception. Our results highlight a fundamental gap between current model capabilities and robust multimodal deep search in real-world settings.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T12:25:13Z。旧 registry Updated:v1：2026-02-16T01:39:06Z（不作首公开）。

## 2602.12892

[RADAR: Revealing Asymmetric Development of Abilities in MLLM Pre-training](https://arxiv.org/abs/2602.12892v1)

Pre-trained Multi-modal Large Language Models (MLLMs) provide a knowledge-rich foundation for post-training by leveraging their inherent perception and reasoning capabilities to solve complex tasks. However, the lack of an efficient evaluation framework impedes the diagnosis of their performance bottlenecks. Current evaluation primarily relies on testing after supervised fine-tuning, which introduces laborious additional training and autoregressive decoding costs. Meanwhile, common pre-training metrics cannot quantify a model's perception and reasoning abilities in a disentangled manner. Furthermore, existing evaluation benchmarks are typically limited in scale or misaligned with pre-training objectives. Thus, we propose RADAR, an efficient ability-centric evaluation framework for Revealing Asymmetric Development of Abilities in MLLM pRe-training. RADAR involves two key components: (1) Soft Discrimination Score, a novel metric for robustly tracking ability development without fine-tuning, based on quantifying nuanced gradations of the model preference for the correct answer over distractors; and (2) Multi-Modal Mixture Benchmark, a new 15K+ sample benchmark for comprehensively evaluating pre-trained MLLMs' perception and reasoning abilities in a 0-shot manner, where we unify authoritative benchmark datasets and carefully collect new datasets, extending the evaluation scope and addressing the critical gaps in current benchmarks. With RADAR, we comprehensively reveal the asymmetric development of perceptual and reasoning capabilities in pretrained MLLMs across diverse factors, including data volume, model size, and pretraining strategy. Our RADAR underscores the need for a decomposed perspective on pre-training ability bottlenecks, informing targeted interventions to advance MLLMs efficiently. Our code is publicly available at https://github.com/Nieysh/RADAR.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T12:56:31Z。旧 registry Updated:v1：2026-02-16T01:40:21Z（不作首公开）。

## 2602.12916

[Reliable Thinking with Images](https://arxiv.org/abs/2602.12916v1)

As a multimodal extension of Chain-of-Thought (CoT), Thinking with Images (TWI) has recently emerged as a promising avenue to enhance the reasoning capability of Multi-modal Large Language Models (MLLMs), which generates interleaved CoT by incorporating visual cues into the textual reasoning process. However, the success of existing TWI methods heavily relies on the assumption that interleaved image-text CoTs are faultless, which is easily violated in real-world scenarios due to the complexity of multimodal understanding. In this paper, we reveal and study a highly-practical yet under-explored problem in TWI, termed Noisy Thinking (NT). Specifically, NT refers to the imperfect visual cues mining and answer reasoning process. As the saying goes, ``One mistake leads to another'', erroneous interleaved CoT would cause error accumulation, thus significantly degrading the performance of MLLMs. To solve the NT problem, we propose a novel method dubbed Reliable Thinking with Images (RTWI). In brief, RTWI estimates the reliability of visual cues and textual CoT in a unified text-centric manner and accordingly employs robust filtering and voting modules to prevent NT from contaminating the final answer. Extensive experiments on seven benchmarks verify the effectiveness of RTWI against NT.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T13:22:04Z。旧 registry Updated:v1：2026-02-16T01:41:52Z（不作首公开）。

## 2602.12924

[Never say never: Exploring the effects of available knowledge on agent persuasiveness in controlled physiotherapy motivation dialogues](https://arxiv.org/abs/2602.12924v1)

Generative Social Agents (GSAs) are increasingly impacting human users through persuasive means. On the one hand, they might motivate users to pursue personal goals, such as healthier lifestyles. On the other hand, they are associated with potential risks like manipulation and deception, which are induced by limited control over probabilistic agent outputs. However, as GSAs manifest communicative patterns based on available knowledge, their behavior may be regulated through their access to such knowledge. Following this approach, we explored persuasive ChatGPT-generated messages in the context of human-robot physiotherapy motivation. We did so by comparing ChatGPT-generated responses to predefined inputs from a hypothetical physiotherapy patient. In Study 1, we qualitatively analyzed 13 ChatGPT-generated dialogue scripts with varying knowledge configurations regarding persuasive message characteristics. In Study 2, third-party observers (N = 27) rated a selection of these dialogues in terms of the agent's expressiveness, assertiveness, and persuasiveness. Our findings indicate that LLM-based GSAs can adapt assertive and expressive personality traits - significantly enhancing perceived persuasiveness. Moreover, persuasiveness significantly benefited from the availability of information about the patients' age and past profession, mediated by perceived assertiveness and expressiveness. Contextual knowledge about physiotherapy benefits did not significantly impact persuasiveness, possibly because the LLM had inherent knowledge about such benefits even without explicit prompting. Overall, the study highlights the importance of empirically studying behavioral patterns of GSAs, specifically in terms of what information generative AI systems require for consistent and responsible communication.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T13:28:55Z。旧 registry Updated:v1：2026-02-16T01:42:19Z（不作首公开）。

## 2602.12932

[TFTF: Training-Free Targeted Flow for Conditional Sampling](https://arxiv.org/abs/2602.12932v1)

We propose a training-free conditional sampling method for flow matching models based on importance sampling. Because a naïve application of importance sampling suffers from weight degeneracy in high-dimensional settings, we modify and incorporate a resampling technique in sequential Monte Carlo (SMC) during intermediate stages of the generation process. To encourage generated samples to diverge along distinct trajectories, we derive a stochastic flow with adjustable noise strength to replace the deterministic flow at the intermediate stage. Our framework requires no additional training, while providing theoretical guarantees of asymptotic accuracy. Experimentally, our method significantly outperforms existing approaches on conditional sampling tasks for MNIST and CIFAR-10. We further demonstrate the applicability of our approach in higher-dimensional, multimodal settings through text-to-image generation experiments on CelebA-HQ.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T13:41:35Z。旧 registry Updated:v1：2026-02-16T01:42:43Z（不作首公开）。

## 2602.12936

[Unleashing MLLMs on the Edge: A Unified Framework for Cross-Modal ReID via Adaptive SVD Distillation](https://arxiv.org/abs/2602.12936v1)

Practical cloud-edge deployment of Cross-Modal Re-identification (CM-ReID) faces challenges due to maintaining a fragmented ecosystem of specialized cloud models for diverse modalities. While Multi-Modal Large Language Models (MLLMs) offer strong unification potential, existing approaches fail to adapt them into a single end-to-end backbone and lack effective knowledge distillation strategies for edge deployment. To address these limitations, we propose MLLMEmbed-ReID, a unified framework based on a powerful cloud-edge architecture. First, we adapt a foundational MLLM into a state-of-the-art cloud model. We leverage instruction-based prompting to guide the MLLM in generating a unified embedding space across RGB, infrared, sketch, and text modalities. This model is then trained efficiently with a hierarchical Low-Rank Adaptation finetuning (LoRA-SFT) strategy, optimized under a holistic cross-modal alignment objective. Second, to deploy its knowledge onto an edge-native student, we introduce a novel distillation strategy motivated by the low-rank property in the teacher's feature space. To prioritize essential information, this method employs a Principal Component Mapping loss, while relational structures are preserved via a Feature Relation loss. Our lightweight edge-based model achieves state-of-the-art performance on multiple visual CM-ReID benchmarks, while its cloud-based counterpart excels across all CM-ReID benchmarks. The MLLMEmbed-ReID framework thus presents a complete and effective solution for deploying unified MLLM-level intelligence on resource-constrained devices. The code and models will be open-sourced soon.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T13:48:08Z。旧 registry Updated:v1：2026-02-16T01:43:04Z（不作首公开）。

## 2602.12943

[Neighborhood Blending: A Lightweight Inference-Time Defense Against Membership Inference Attacks](https://arxiv.org/abs/2602.12943v1)

In recent years, the widespread adoption of Machine Learning as a Service (MLaaS), particularly in sensitive environments, has raised considerable privacy concerns. Of particular importance are membership inference attacks (MIAs), which exploit behavioral discrepancies between training and non-training data to determine whether a specific record was included in the model's training set, thereby presenting significant privacy risks. Although existing defenses, such as adversarial regularization, DP-SGD, and MemGuard, assist in mitigating these threats, they often entail trade-offs such as compromising utility, increased computational requirements, or inconsistent protection against diverse attack vectors.
 In this paper, we introduce a novel inference-time defense mechanism called Neighborhood Blending, which mitigates MIAs without retraining the model or incurring significant computational overhead. Our approach operates post-training by smoothing the model's confidence outputs based on the neighborhood of a queried sample. By averaging predictions from similar training samples selected using differentially private sampling, our method establishes a consistent confidence pattern, rendering members and non-members indistinguishable to an adversary while maintaining high utility. Significantly, Neighborhood Blending maintains label integrity (zero label loss) and ensures high utility through an adaptive, "pay-as-you-go" distortion strategy. It is a model-agnostic approach that offers a practical, lightweight solution that enhances privacy without sacrificing model utility. Through extensive experiments across diverse datasets and models, we demonstrate that our defense significantly reduces MIA success rates while preserving model performance, outperforming existing post-hoc defenses like MemGuard and training-time techniques like DP-SGD in terms of utility retention.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:01:21Z。旧 registry Updated:v1：2026-02-16T01:43:35Z（不作首公开）。

## 2602.12952

[Transporting Task Vectors across Different Architectures without Training](https://arxiv.org/abs/2602.12952v1)

Adapting large pre-trained models to downstream tasks often produces task-specific parameter updates that are expensive to relearn for every model variant. While recent work has shown that such updates can be transferred between models with identical architectures, transferring them across models of different widths remains unexplored. In this work, we introduce Theseus, a training-free method for transporting task updates across heterogeneous-width models. Rather than matching parameters, we characterize a task update by the functional effect it induces on intermediate representations. We formalize task-vector transport as a functional matching problem on observed activations and show that, after aligning representation spaces via orthogonal Procrustes analysis, it admits a stable closed-form solution that preserves the geometry of the update. We evaluate Theseus on vision and language models across different widths, showing consistent improvements over baselines without additional training or backpropagation. Our results show that task updates can be meaningfully transferred across architectures when task identity is defined functionally rather than parametrically. Code is available at https://github.com/apanariello4/merge-and-rebase.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:16:34Z。旧 registry Updated:v1：2026-02-16T01:44:19Z（不作首公开）。

## 2602.12953

[Human Tool: An MCP-Style Framework for Human-Agent Collaboration](https://arxiv.org/abs/2602.12953v1)

Human-AI collaboration faces growing challenges as AI systems increasingly outperform humans on complex tasks, while humans remain responsible for orchestration, validation, and decision oversight. To address this imbalance, we introduce Human Tool, an MCP-style interface abstraction, building on recent Model Context Protocol designs, that exposes humans as callable tools within AI-led, proactive workflows. Here, "tool" denotes a coordination abstraction, not a reduction of human authority or responsibility. Building on LLM-based agent architectures, we operationalize Human Tool by modeling human contributions through structured tool schemas of capabilities, information, and authority. These schemas enable agents to dynamically invoke human input based on relative strengths and reintegrate it through efficient, natural interaction protocols. We validate the framework through controlled studies in both decision-making and creative tasks, demonstrating improved task performance, reduced human workload, and more balanced collaboration dynamics compared to baseline systems. Finally, we discuss implications for human-centered AI design, highlighting how MCP-style human tools enable strong AI leadership while amplifying uniquely human strengths.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:18:16Z。旧 registry Updated:v1：2026-02-16T01:44:21Z（不作首公开）。

## 2602.12954

[Data Augmentation and Attention for massive MIMO-based Indoor Localization in Changing Environments](https://arxiv.org/abs/2602.12954v1)

The demand for high-precision indoor localization has grown significantly with the rise of smart environments, industrial automation, and location-aware applications. While massive Multiple-Input and Multiple-Output (MIMO) systems enable millimeter-level accuracy by leveraging rich Channel State Information (CSI), most existing solutions are optimized for static environments, where users or devices remain fixed during data collection and inference. Real-world applications, however, often require real-time localization in changing environments, where rapid movement, unpredictable blockages, and dynamic channel conditions pose significant challenges. To address these challenges, we introduce two data augmentation techniques designed to resemble blocked antennas, enhancing the generalizability of localization models to dynamic scenarios. Additionally, we enhance an existing Deep Learning (DL) model by incorporating attention modules, improving its ability to focus on relevant channel features and antennas. We train our model on data from a static scenario, augmented with the proposed techniques, and evaluate it on a dataset collected in changing scenarios. We investigate the performance enhancements achieved by the data augmentation techniques and the Attention modules, and observe a localization accuracy improvement from a mean error of 286 mm, when trained without Attention and without data augmentations, to 66 mm, when trained with Attention and data augmentation. This shows that high localization accuracy can be maintained in changing environments, even without training data from those scenarios.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:18:30Z。旧 registry Updated:v1：2026-02-16T01:44:24Z（不作首公开）。

## 2602.12957

[HSD: Training-Free Acceleration for Document Parsing Vision-Language Models with Hierarchical Speculative Decoding](https://arxiv.org/abs/2602.12957v1)

Document parsing is a fundamental task in multimodal understanding, supporting a wide range of downstream applications such as information extraction and intelligent document analysis. Benefiting from strong semantic modeling and robust generalization, VLM-based end-to-end approaches have emerged as the mainstream paradigm in recent years. However, these models often suffer from substantial inference latency, as they must autoregressively generate long, full-page sequences when processing long-form documents. While recent hybrid methods mitigate this issue via region-level parallel decoding with VLMs, independent region decoding loses full-page context and might weaken global coherence. To address this issue, we propose Hierarchical Speculative Decoding (HSD), a two-stage local-to-global framework for document parsing. HSD first employs a lightweight pipeline drafter to predict region partitions and generate coarse drafts for each region. The first stage verifies the generated region-level drafts in parallel for efficiency, while the second stage further performs page-level verification on these refined outputs to preserve full-page coherence. Experimental results show that HSD achieves a near-lossless 2.7x speedup with HunyuanOCR on OmniDocBench v1.5 and up to 7.04x speedup on long-document parsing tasks, demonstrating the effectiveness of the proposed method. The code is available at https://github.com/whlscut/HSD.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:22:10Z。旧 registry Updated:v1：2026-02-16T01:44:34Z（不作首公开）。

## 2602.12962

[TriGen: NPU Architecture for End-to-End Acceleration of Large Language Models based on SW-HW Co-Design](https://arxiv.org/abs/2602.12962v1)

Recent studies have extensively explored NPU architectures for accelerating AI inference in on-device environments, which are inherently resource-constrained. Meanwhile, transformer-based large language models (LLMs) have become dominant, with rapidly increasing model sizes but low degree of parameter reuse compared to conventional CNNs, making end-to-end execution on resource-limited devices extremely challenging. To address these challenges, we propose TriGen, a novel NPU architecture tailored for resource-constrained environments through software-hardware co-design. Firstly, TriGen adopts low-precision computation using microscaling (MX) to enable additional optimization opportunities while preserving accuracy, and resolves the issues that arise by employing such precision. Secondly, to jointly optimize both nonlinear and linear operations, TriGen eliminates the need for specialized hardware for essential nonlinear operations by using fast and accurate LUT, thereby maximizing performance gains and reducing hardware-cost in on-device environments, and finally, by taking practical hardware constraints into account, further employs scheduling techniques to maximize computational utilization even under limited on-chip memory capacity. We evaluate the performance of TriGen on various LLMs and show that TriGen achieves an average 2.73x performance speedup and 52% less memory transfer over the baseline NPU design with negligible accuracy loss.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:28:31Z。旧 registry Updated:v1：2026-02-16T01:44:53Z（不作首公开）。

## 2602.12966

[ProbeLLM: Automating Principled Diagnosis of LLM Failures](https://arxiv.org/abs/2602.12966v1)

Understanding how and why large language models (LLMs) fail is becoming a central challenge as models rapidly evolve and static evaluations fall behind. While automated probing has been enabled by dynamic test generation, existing approaches often discover isolated failure cases, lack principled control over exploration, and provide limited insight into the underlying structure of model weaknesses. We propose ProbeLLM, a benchmark-agnostic automated probing framework that elevates weakness discovery from individual failures to structured failure modes. ProbeLLM formulates probing as a hierarchical Monte Carlo Tree Search, explicitly allocating limited probing budgets between global exploration of new failure regions and local refinement of recurring error patterns. By restricting probing to verifiable test cases and leveraging tool-augmented generation and verification, ProbeLLM grounds failure discovery in reliable evidence. Discovered failures are further consolidated into interpretable failure modes via failure-aware embeddings and boundary-aware induction. Across diverse benchmarks and LLMs, ProbeLLM reveals substantially broader, cleaner, and more fine-grained failure landscapes than static benchmarks and prior automated methods, supporting a shift from case-centric evaluation toward principled weakness discovery.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:33:13Z。旧 registry Updated:v1：2026-02-16T01:45:02Z（不作首公开）。

## 2602.12978

[Learning Native Continuation for Action Chunking Flow Policies](https://arxiv.org/abs/2602.12978v1)

Action chunking enables Vision Language Action (VLA) models to run in real time, but naive chunked execution often exhibits discontinuities at chunk boundaries. Real-Time Chunking (RTC) alleviates this issue but is external to the policy, leading to spurious multimodal switching and trajectories that are not intrinsically smooth. We propose Legato, a training-time continuation method for action-chunked flow-based VLA policies. Specifically, Legato initializes denoising from a schedule-shaped mixture of known actions and noise, exposing the model to partial action information. Moreover, Legato reshapes the learned flow dynamics to ensure that the denoising process remains consistent between training and inference under per-step guidance. Legato further uses randomized schedule condition during training to support varying inference delays and achieve controllable smoothness. Empirically, Legato produces smoother trajectories and reduces spurious multimodal switching during execution, leading to less hesitation and shorter task completion time. Extensive real-world experiments show that Legato consistently outperforms RTC across five manipulation tasks, achieving approximately 10% improvements in both trajectory smoothness and task completion time.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:56:06Z。旧 registry Updated:v1：2026-02-16T01:46:08Z（不作首公开）。

## 2602.12984

[SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents](https://arxiv.org/abs/2602.12984v1)

Scientific reasoning inherently demands integrating sophisticated toolkits to navigate domain-specific knowledge. Yet, current benchmarks largely overlook agents' ability to orchestrate tools for such rigorous workflows. To bridge this gap, we introduce SciAgentGym, a scalable interactive environment featuring 1,780 domain-specific tools across four natural science disciplines, supported by a robust execution infrastructure. Complementing this, we present SciAgentBench, a tiered evaluation suite designed to stress-test agentic capabilities from elementary actions to long-horizon workflows. Our evaluation identifies a critical bottleneck: state-of-the-art models still struggle with complex scientific tool-use, and their performance degrades substantially as interaction horizons extend. To address this, we propose SciForge, a data synthesis method that models the tool action space as a dependency graph to generate logic-aware training trajectories. By fine-tuning on these trajectories, our SciAgent-8B outperforms the significantly larger Qwen3-VL-235B-Instruct while exhibiting positive cross-domain transfer of scientific tool-use capabilities. These results underscore the promising potential of next-generation autonomous scientific agents.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T14:58:18Z。旧 registry Updated:v1：2026-02-16T01:46:22Z（不作首公开）。

## 2602.12996

[Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models](https://arxiv.org/abs/2602.12996v1)

Knowledge augmentation has significantly enhanced the performance of Large Language Models (LLMs) in knowledge-intensive tasks. However, existing methods typically operate on the simplistic premise that model performance equates with internal knowledge, overlooking the knowledge-confidence gaps that lead to overconfident errors or uncertain truths. To bridge this gap, we propose a novel meta-cognitive framework for reliable knowledge augmentation via differentiated intervention and alignment. Our approach leverages internal cognitive signals to partition the knowledge space into mastered, confused, and missing regions, guiding targeted knowledge expansion. Furthermore, we introduce a cognitive consistency mechanism to synchronize subjective certainty with objective accuracy, ensuring calibrated knowledge boundaries. Extensive experiments demonstrate the our framework consistently outperforms strong baselines, validating its rationality in not only enhancing knowledge capabilities but also fostering cognitive behaviors that better distinguish knowns from unknowns. All codes are available at https://github.com/AI9Stars/Know-More-Know-Clearer.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:07:35Z。旧 registry Updated:v1：2026-02-16T01:46:53Z（不作首公开）。

## 2602.13013

[Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions](https://arxiv.org/abs/2602.13013v1)

Universal video understanding requires modeling fine-grained visual and audio information over time in diverse real-world scenarios. However, the performance of existing models is primarily constrained by video-instruction data that represents complex audiovisual content as single, incomplete descriptions, lacking fine-grained organization and reliable annotation. To address this, we introduce: (i) ASID-1M, an open-source collection of one million structured, fine-grained audiovisual instruction annotations with single- and multi-attribute supervision; (ii) ASID-Verify, a scalable data curation pipeline for annotation, with automatic verification and refinement that enforces semantic and temporal consistency between descriptions and the corresponding audiovisual content; and (iii) ASID-Captioner, a video understanding model trained via Supervised Fine-Tuning (SFT) on the ASID-1M. Experiments across seven benchmarks covering audiovisual captioning, attribute-wise captioning, caption-based QA, and caption-based temporal grounding show that ASID-Captioner improves fine-grained caption quality while reducing hallucinations and improving instruction following. It achieves state-of-the-art performance among open-source models and is competitive with Gemini-3-Pro.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:20:54Z。旧 registry Updated:v1：2026-02-16T01:47:38Z（不作首公开）。

## 2602.13028

[Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis](https://arxiv.org/abs/2602.13028v1)

Evaluating image editing models remains challenging due to the coarse granularity and limited interpretability of traditional metrics, which often fail to capture aspects important to human perception and intent. Such metrics frequently reward visually plausible outputs while overlooking controllability, edit localization, and faithfulness to user instructions. In this work, we introduce a fine-grained Multimodal Large Language Model (MLLM)-as-a-Judge framework for image editing that decomposes common evaluation notions into twelve fine-grained interpretable factors spanning image preservation, edit quality, and instruction fidelity. Building on this formulation, we present a new human-validated benchmark that integrates human judgments, MLLM-based evaluations, model outputs, and traditional metrics across diverse image editing tasks. Through extensive human studies, we show that the proposed MLLM judges align closely with human evaluations at a fine granularity, supporting their use as reliable and scalable evaluators. We further demonstrate that traditional image editing metrics are often poor proxies for these factors, failing to distinguish over-edited or semantically imprecise outputs, whereas our judges provide more intuitive and informative assessments in both offline and online settings. Together, this work introduces a benchmark, a principled factorization, and empirical evidence positioning fine-grained MLLM judges as a practical foundation for studying, comparing, and improving image editing approaches.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:34:32Z。旧 registry Updated:v1：2026-02-16T01:48:39Z（不作首公开）。

## 2602.13030

[Resource-Efficient Gesture Recognition through Convexified Attention](https://arxiv.org/abs/2602.13030v1)

Wearable e-textile interfaces require gesture recognition capabilities but face severe constraints in power consumption, computational capacity, and form factor that make traditional deep learning impractical. While lightweight architectures like MobileNet improve efficiency, they still demand thousands of parameters, limiting deployment on textile-integrated platforms. We introduce a convexified attention mechanism for wearable applications that dynamically weights features while preserving convexity through nonexpansive simplex projection and convex loss functions. Unlike conventional attention mechanisms using non-convex softmax operations, our approach employs Euclidean projection onto the probability simplex combined with multi-class hinge loss, ensuring global convergence guarantees. Implemented on a textile-based capacitive sensor with four connection points, our approach achieves 100.00\% accuracy on tap gestures and 100.00\% on swipe gestures -- consistent across 10-fold cross-validation and held-out test evaluation -- while requiring only 120--360 parameters, a 97\% reduction compared to conventional approaches. With sub-millisecond inference times (290--296$μ$s) and minimal storage requirements ($&lt;$7KB), our method enables gesture interfaces directly within e-textiles without external processing. Our evaluation, conducted in controlled laboratory conditions with a single-user dataset, demonstrates feasibility for basic gesture interactions. Real-world deployment would require validation across multiple users, environmental conditions, and more complex gesture vocabularies. These results demonstrate how convex optimization can enable efficient on-device machine learning for textile interfaces.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:37:02Z。旧 registry Updated:v1：2026-02-16T01:48:46Z（不作首公开）。

## 2602.13033

[Buy versus Build an LLM: A Decision Framework for Governments](https://arxiv.org/abs/2602.13033v1)

Large Language Models (LLMs) represent a new frontier of digital infrastructure that can support a wide range of public-sector applications, from general purpose citizen services to specialized and sensitive state functions. When expanding AI access, governments face a set of strategic choices over whether to buy existing services, build domestic capabilities, or adopt hybrid approaches across different domains and use cases. These are critical decisions especially when leading model providers are often foreign corporations, and LLM outputs are increasingly treated as trusted inputs to public decision-making and public discourse. In practice, these decisions are not intended to mandate a single approach across all domains; instead, national AI strategies are typically pluralistic, with sovereign, commercial and open-source models coexisting to serve different purposes. Governments may rely on commercial models for non-sensitive or commodity tasks, while pursuing greater control for critical, high-risk or strategically important applications.
 This paper provides a strategic framework for making this decision by evaluating these options across dimensions including sovereignty, safety, cost, resource capability, cultural fit, and sustainability. Importantly, "building" does not imply that governments must act alone: domestic capabilities may be developed through public research institutions, universities, state-owned enterprises, joint ventures, or broader national ecosystems. By detailing the technical requirements and practical challenges of each pathway, this work aims to serve as a reference for policy-makers to determine whether a buy or build approach best aligns with their specific national needs and societal goals.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:39:31Z。旧 registry Updated:v1：2026-02-16T01:48:51Z（不作首公开）。

## 2602.13035

[Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL](https://arxiv.org/abs/2602.13035v1)

Reinforcement Learning from Verifiable Rewards (RLVR) trains large language models (LLMs) from sampled trajectories, making decoding strategy a core component of learning rather than a purely inference-time choice. Sampling temperature directly controls the exploration--exploitation trade-off by modulating policy entropy, yet existing methods rely on static values or heuristic adaptations that are decoupled from task-level rewards. We propose Introspective LLM, a hierarchical reinforcement learning framework that learns to control sampling temperature during generation. At each decoding step, the model selects a temperature based on its hidden state and samples the next token from the resulting distribution. Temperature and token policies are jointly optimized from downstream rewards using a coordinate ascent scheme. Experiments on mathematical reasoning benchmarks show that learned temperature policies outperform fixed and heuristic baselines, while exhibiting interpretable exploration behaviors aligned with reasoning uncertainty.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:42:59Z。旧 registry Updated:v1：2026-02-16T01:49:01Z（不作首公开）。

## 2602.13042

[GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/abs/2602.13042v1)

While historical considerations surrounding text authenticity revolved primarily around plagiarism, the advent of large language models (LLMs) has introduced a new challenge: distinguishing human-authored from AI-generated text. This shift raises significant concerns, including the undermining of skill evaluations, the mass-production of low-quality content, and the proliferation of misinformation. Addressing these issues, we introduce GPTZero a state-of-the-art industrial AI detection solution, offering reliable discernment between human and LLM-generated text. Our key contributions include: introducing a hierarchical, multi-task architecture enabling a flexible taxonomy of human and AI texts, demonstrating state-of-the-art accuracy on a variety of domains with granular predictions, and achieving superior robustness to adversarial attacks and paraphrasing via multi-tiered automated red teaming. GPTZero offers accurate and explainable detection, and educates users on its responsible use, ensuring fair and transparent assessment of text.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T15:53:45Z。旧 registry Updated:v1：2026-02-16T01:49:26Z（不作首公开）。

## 2602.13052

[Quantization-Aware Collaborative Inference for Large Embodied AI Models](https://arxiv.org/abs/2602.13052v1)

Large artificial intelligence models (LAIMs) are increasingly regarded as a core intelligence engine for embodied AI applications. However, the massive parameter scale and computational demands of LAIMs pose significant challenges for resource-limited embodied agents. To address this issue, we investigate quantization-aware collaborative inference (co-inference) for embodied AI systems. First, we develop a tractable approximation for quantization-induced inference distortion. Based on this approximation, we derive lower and upper bounds on the quantization rate-inference distortion function, characterizing its dependence on LAIM statistics, including the quantization bit-width. Next, we formulate a joint quantization bit-width and computation frequency design problem under delay and energy constraints, aiming to minimize the distortion upper bound while ensuring tightness through the corresponding lower bound. Extensive evaluations validate the proposed distortion approximation, the derived rate-distortion bounds, and the effectiveness of the proposed joint design. Particularly, simulations and real-world testbed experiments demonstrate the effectiveness of the proposed joint design in balancing inference quality, latency, and energy consumption in edge embodied AI systems.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:08:19Z。旧 registry Updated:v1：2026-02-16T01:50:16Z（不作首公开）。

## 2602.13055

[Curriculum-DPO++: Direct Preference Optimization via Data and Model Curricula for Text-to-Image Generation](https://arxiv.org/abs/2602.13055v1)

Direct Preference Optimization (DPO) has been proposed as an effective and efficient alternative to reinforcement learning from human feedback (RLHF). However, neither RLHF nor DPO take into account the fact that learning certain preferences is more difficult than learning other preferences, rendering the optimization process suboptimal. To address this gap in text-to-image generation, we recently proposed Curriculum-DPO, a method that organizes image pairs by difficulty. In this paper, we introduce Curriculum-DPO++, an enhanced method that combines the original data-level curriculum with a novel model-level curriculum. More precisely, we propose to dynamically increase the learning capacity of the denoising network as training advances. We implement this capacity increase via two mechanisms. First, we initialize the model with only a subset of the trainable layers used in the original Curriculum-DPO. As training progresses, we sequentially unfreeze layers until the configuration matches the full baseline architecture. Second, as the fine-tuning is based on Low-Rank Adaptation (LoRA), we implement a progressive schedule for the dimension of the low-rank matrices. Instead of maintaining a fixed capacity, we initialize the low-rank matrices with a dimension significantly smaller than that of the baseline. As training proceeds, we incrementally increase their rank, allowing the capacity to grow until it converges to the same rank value as in Curriculum-DPO. Furthermore, we propose an alternative ranking strategy to the one employed by Curriculum-DPO. Finally, we compare Curriculum-DPO++ against Curriculum-DPO and other state-of-the-art preference optimization approaches on nine benchmarks, outperforming the competing methods in terms of text alignment, aesthetics and human preference. Our code is available at https://github.com/CroitoruAlin/Curriculum-DPO.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:09:31Z。旧 registry Updated:v1：2026-02-16T01:50:24Z（不作首公开）。

## 2602.13059

[TraceBack: Multi-Agent Decomposition for Fine-Grained Table Attribution](https://arxiv.org/abs/2602.13059v1)

Question answering (QA) over structured tables requires not only accurate answers but also transparency about which cells support them. Existing table QA systems rarely provide fine-grained attribution, so even correct answers often lack verifiable grounding, limiting trust in high-stakes settings. We address this with TraceBack, a modular multi-agent framework for scalable, cell-level attribution in single-table QA. TraceBack prunes tables to relevant rows and columns, decomposes questions into semantically coherent sub-questions, and aligns each answer span with its supporting cells, capturing both explicit and implicit evidence used in intermediate reasoning steps. To enable systematic evaluation, we release CITEBench, a benchmark with phrase-to-cell annotations drawn from ToTTo, FetaQA, and AITQA. We further propose FairScore, a reference-less metric that compares atomic facts derived from predicted cells and answers to estimate attribution precision and recall without human cell labels. Experiments show that TraceBack substantially outperforms strong baselines across datasets and granularities, while FairScore closely tracks human judgments and preserves relative method rankings, supporting interpretable and scalable evaluation of table-based QA.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:13:36Z。旧 registry Updated:v1：2026-02-16T01:50:48Z（不作首公开）。

## 2602.13061

[Native Extrapolation Awareness in Flow-Based Conditional Generation](https://arxiv.org/abs/2602.13061v1)

The ability of Flow Matching (FM) to model complex conditional distributions has established it as the state-of-the-art for prediction tasks (e.g., robotics, weather forecasting). However, deployment in safety-critical settings is hindered by a critical extrapolation hazard: driven by smoothness biases, flow models yield plausible outputs even for off-manifold conditions, resulting in silent failures indistinguishable from valid predictions. In this work, we introduce Diverging Flows, a novel approach that enables a single model to simultaneously perform conditional generation and native extrapolation detection by structurally enforcing inefficient transport for off-manifold inputs. We evaluate our method on synthetic manifolds, cross-domain style transfer, and weather temperature forecasting, demonstrating that it achieves effective detection of extrapolations without compromising predictive fidelity or inference latency. These results establish Diverging Flows as a robust solution for trustworthy flow models, paving the way for reliable deployment in domains such as medicine, robotics, and climate science.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:15:58Z。旧 registry Updated:v1：2026-02-16T01:50:59Z（不作首公开）。

## 2602.13067

[SIEFormer: Spectral-Interpretable and -Enhanced Transformer for Generalized Category Discovery](https://arxiv.org/abs/2602.13067v1)

This paper presents a novel approach, Spectral-Interpretable and -Enhanced Transformer (SIEFormer), which leverages spectral analysis to reinterpret the attention mechanism within Vision Transformer (ViT) and enhance feature adaptability, with particular emphasis on challenging Generalized Category Discovery (GCD) tasks. The proposed SIEFormer is composed of two main branches, each corresponding to an implicit and explicit spectral perspective of the ViT, enabling joint optimization. The implicit branch realizes the use of different types of graph Laplacians to model the local structure correlations of tokens, along with a novel Band-adaptive Filter (BaF) layer that can flexibly perform both band-pass and band-reject filtering. The explicit branch, on the other hand, introduces a Maneuverable Filtering Layer (MFL) that learns global dependencies among tokens by applying the Fourier transform to the input ``value" features, modulating the transformed signal with a set of learnable parameters in the frequency domain, and then performing an inverse Fourier transform to obtain the enhanced features. Extensive experiments reveal state-of-the-art performance on multiple image recognition datasets, reaffirming the superiority of our approach through ablation studies and visualizations.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:22:31Z。旧 registry Updated:v1：2026-02-16T01:51:25Z（不作首公开）。

## 2602.13069

[Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning](https://arxiv.org/abs/2602.13069v1)

On-device fine-tuning enables privacy-preserving personalization of large language models, but mobile devices impose severe memory constraints, typically 6--12GB shared across all workloads. Existing approaches force a trade-off between exact gradients with high memory (MeBP) and low memory with noisy estimates (MeZO). We propose Memory-efficient Structured Backpropagation (MeSP), which bridges this gap by manually deriving backward passes that exploit LoRA's low-rank structure. Our key insight is that the intermediate projection $h = xA$ can be recomputed during backward at minimal cost since rank $r \ll d_{in}$, eliminating the need to store it. MeSP achieves 49\% average memory reduction compared to MeBP on Qwen2.5 models (0.5B--3B) while computing mathematically identical gradients. Our analysis also reveals that MeZO's gradient estimates show near-zero correlation with true gradients (cosine similarity $\approx$0.001), explaining its slow convergence. MeSP reduces peak memory from 361MB to 136MB for Qwen2.5-0.5B, enabling fine-tuning scenarios previously infeasible on memory-constrained devices.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:24:33Z。旧 registry Updated:v1：2026-02-16T01:51:31Z（不作首公开）。

## 2602.13073

[LCSB: Layer-Cyclic Selective Backpropagation for Memory-Efficient On-Device LLM Fine-Tuning](https://arxiv.org/abs/2602.13073v1)

Memory-efficient backpropagation (MeBP) has enabled first-order fine-tuning of large language models (LLMs) on mobile devices with less than 1GB memory. However, MeBP requires backward computation through all transformer layers at every step, where weight decompression alone accounts for 32--42% of backward time. We propose Layer-Cyclic Selective Backpropagation (LCSB), which computes gradients for only a subset of layers per step. Our key insight is that residual connections guarantee gradient flow through identity paths, while AdamW momentum provides implicit updates for non-selected layers. We interpret LCSB as Block Coordinate Descent on the LoRA parameter space, providing theoretical justification for convergence. LCSB achieves up to 1.40$\times$ speedup with less than 2\% quality degradation across five models and three tasks. Surprisingly, in 4-bit quantized settings, LCSB exhibits superior stability: a 3B model that completely diverges under full backpropagation converges smoothly with LCSB, suggesting an implicit regularization effect from selective gradient computation.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:32:53Z。旧 registry Updated:v1：2026-02-16T01:51:47Z（不作首公开）。

## 2602.13081

[Agentic AI for Robot Control: Flexible but still Fragile](https://arxiv.org/abs/2602.13081v1)

Recent work leverages the capabilities and commonsense priors of generative models for robot control. In this paper, we present an agentic control system in which a reasoning-capable language model plans and executes tasks by selecting and invoking robot skills within an iterative planner and executor loop. We deploy the system on two physical robot platforms in two settings: (i) tabletop grasping, placement, and box insertion in indoor mobile manipulation (Mobipick) and (ii) autonomous agricultural navigation and sensing (Valdemar). Both settings involve uncertainty, partial observability, sensor noise, and ambiguous natural-language commands. The system exposes structured introspection of its planning and decision process, reacts to exogenous events via explicit event checks, and supports operator interventions that modify or redirect ongoing execution. Across both platforms, our proof-of-concept experiments reveal substantial fragility, including non-deterministic suboptimal behavior, instruction-following errors, and high sensitivity to prompt specification. At the same time, the architecture is flexible: transfer to a different robot and task domain largely required updating the system prompt (domain model, affordances, and action catalogue) and re-binding the same tool interface to the platform-specific skill API.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:43:34Z。旧 registry Updated:v1：2026-06-04T00:50:16Z（不作首公开）。

## 2602.13086

[UniManip: General-Purpose Zero-Shot Robotic Manipulation with Agentic Operational Graph](https://arxiv.org/abs/2602.13086v1)

Achieving general-purpose robotic manipulation requires robots to seamlessly bridge high-level semantic intent with low-level physical interaction in unstructured environments. However, existing approaches falter in zero-shot generalization: end-to-end Vision-Language-Action (VLA) models often lack the precision required for long-horizon tasks, while traditional hierarchical planners suffer from semantic rigidity when facing open-world variations. To address this, we present UniManip, a framework grounded in a Bi-level Agentic Operational Graph (AOG) that unifies semantic reasoning and physical grounding. By coupling a high-level Agentic Layer for task orchestration with a low-level Scene Layer for dynamic state representation, the system continuously aligns abstract planning with geometric constraints, enabling robust zero-shot execution. Unlike static pipelines, UniManip operates as a dynamic agentic loop: it actively instantiates object-centric scene graphs from unstructured perception, parameterizes these representations into collision-free trajectories via a safety-aware local planner, and exploits structured memory to autonomously diagnose and recover from execution failures. Extensive experiments validate the system's robust zero-shot capability on unseen objects and tasks, demonstrating a 22.5% and 25.0% higher success rate compared to state-of-the-art VLA and hierarchical baselines, respectively. Notably, the system enables direct zero-shot transfer from fixed-base setups to mobile manipulation without fine-tuning or reconfiguration. Our open-source project page can be found at https://henryhcliu.github.io/unimanip.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T16:47:26Z。旧 registry Updated:v1：2026-02-16T01:52:18Z（不作首公开）。

## 2602.13103

[R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103v1)

Self-play bootstraps LLM reasoning through an iterative Challenger-Solver loop: the Challenger is trained to generate questions that target the Solver's capabilities, and the Solver is optimized on the generated data to expand its reasoning skills. However, existing frameworks like R-Zero often exhibit non-sustained improvement, where early gains degrade as self-play continues. We identify a key failure mode, Diversity Illusion, where the Solver's training signals appear diverse yet collapse into recurring underlying patterns. It manifests as (1) Local Diversity Illusion, where diversity is enforced only within-batch, inducing cross-iteration mode cycling; and (2) Surface Diversity Illusion, where questions vary superficially but require near-identical reasoning skills. To mitigate them, we propose R-Diverse with two aligned innovations: Memory-Augmented Penalty (MAP), which uses a persistent memory bank to discourage recycling across iterations, and Skill-Aware Measurement (SAM), which evaluates diversity by the reasoning skills exercised rather than surface variation of questions. Across 10 math and general reasoning benchmarks, R-Diverse sustains gains over more iterations and consistently outperforms prior self-play methods. Code is available at https://github.com/Gengsheng-Li/R-Diverse.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T17:07:42Z。旧 registry Updated:v1：2026-02-16T01:53:28Z（不作首公开）。

## 2602.13110

[SCOPE: Selective Conformal Optimized Pairwise LLM Judging](https://arxiv.org/abs/2602.13110v1)

Large language models (LLMs) are increasingly used as scalable judges in pairwise evaluation, but they remain prone to miscalibration and biases. We propose \textsc{Scope} (Selective Conformal Optimized Pairwise Evaluation), a framework that calibrates an acceptance threshold so that, under exchangeability, the error rate among non-abstained judgments is at most a user-specified level $α$. To supply \textsc{Scope} with a bias-neutral uncertainty signal, we introduce Bidirectional Preference Entropy (BPE), which queries the judge under both response positions and converts the order-averaged preference probability into an entropy-based score. Across various pairwise judging benchmarks, BPE outperforms standard confidence proxies in calibration and discrimination, while \textsc{Scope} consistently satisfies the target risk bound (empirical FDR $\approx 0.097$--$0.099$ at $α=0.10$) and retains substantial coverage. Compared to vanilla baselines, \textsc{Scope} accepts up to $2.4\times$ more judgments under the same risk constraint, demonstrating that BPE enables reliable and high-coverage LLM-based evaluation.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T17:10:43Z。旧 registry Updated:v1：2026-02-16T01:53:36Z（不作首公开）。

## 2602.13126

[Automating UI Optimization through Multi-Agentic Reasoning](https://arxiv.org/abs/2602.13126v1)

We present AutoOptimization, a novel multi-objective optimization framework for adapting user interfaces. From a user's verbal preferences for changing a UI, our framework guides a prioritization-based Pareto frontier search over candidate layouts. It selects suitable objective functions for UI placement while simultaneously parameterizing them according to the user's instructions to define the optimization problem. A solver then generates a series of optimal UI layouts, which our framework validates against the user's instructions to adapt the UI with the final solution. Our approach thus overcomes the previous need for manual inspection of layouts and the use of population averages for objective parameters. We integrate multiple agents sequentially within our framework, enabling the system to leverage their reasoning capabilities to interpret user preferences, configure the optimization problem, and validate optimization outcomes.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T17:24:36Z。旧 registry Updated:v1：2026-02-16T01:54:19Z（不作首公开）。

## 2602.13131

[Preference-Guided Prompt Optimization for Text-to-Image Generation](https://arxiv.org/abs/2602.13131v1)

Generative models are increasingly powerful, yet users struggle to guide them through prompts. The generative process is difficult to control and unpredictable, and user instructions may be ambiguous or under-specified. Prior prompt refinement tools heavily rely on human effort, while prompt optimization methods focus on numerical functions and are not designed for human-centered generative tasks, where feedback is better expressed as binary preferences and demands convergence within few iterations. We present APPO, a preference-guided prompt optimization algorithm. Instead of iterating prompts, users only provide binary preferential feedback. APPO adaptively balances its strategies between exploiting user feedback and exploring new directions, yielding effective and efficient optimization. We evaluate APPO on image generation, and the results show APPO enables achieving satisfactory outcomes in fewer iterations with lower cognitive load than manual prompt editing. We anticipate APPO will advance human-AI collaboration in generative tasks by leveraging user preferences to guide complex content creation.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T17:29:04Z。旧 registry Updated:v1：2026-02-16T01:54:33Z（不作首公开）。

## 2602.13136

[Order Matters in Retrosynthesis: Structure-aware Generation via Reaction-Center-Guided Discrete Flow Matching](https://arxiv.org/abs/2602.13136v1)

Template-free retrosynthesis methods treat the task as black-box sequence generation, limiting learning efficiency, while semi-template approaches rely on rigid reaction libraries that constrain generalization. We address this gap with a key insight: atom ordering in neural representations matters. Building on this insight, we propose a structure-aware template-free framework that encodes the two-stage nature of chemical reactions as a positional inductive bias. By placing reaction center atoms at the sequence head, our method transforms implicit chemical knowledge into explicit positional patterns that the model can readily capture. The proposed RetroDiT backbone, a graph transformer with rotary position embeddings, exploits this ordering to prioritize chemically critical regions. Combined with discrete flow matching, our approach decouples training from sampling and enables generation in 20--50 steps versus 500 for prior diffusion methods. Our method achieves state-of-the-art performance on both USPTO-50k (61.2% top-1) and the large-scale USPTO-Full (51.3% top-1) with predicted reaction centers. With oracle centers, performance reaches 71.1% and 63.4% respectively, surpassing foundation models trained on 10 billion reactions while using orders of magnitude less data. Ablation studies further reveal that structural priors outperform brute-force scaling: a 280K-parameter model with proper ordering matches a 65M-parameter model without it.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T17:39:21Z。旧 registry Updated:v1：2026-02-16T01:55:00Z（不作首公开）。

## 2602.13151

[Quantization-Robust LLM Unlearning via Low-Rank Adaptation](https://arxiv.org/abs/2602.13151v1)

Large Language Model (LLM) unlearning aims to remove targeted knowledge from a trained model, but practical deployments often require post-training quantization (PTQ) for efficient inference. However, aggressive low-bit PTQ can mask unlearning updates, causing quantized models to revert to pre-unlearning behavior. We show that standard full-parameter fine-tuning often induces parameter changes that are too small to survive 4-bit quantization. We propose quantization-robust unlearning via low-rank adaptation (LoRA): we freeze the base model and concentrate unlearning into trainable adapters so that the effective update is preserved after quantization. On Llama-2-7B evaluated with MUSE dataset (BOOKS and NEWS), LoRA improves 4-bit utility by up to 7.93 points (NPO+GDR on BOOKS: 50.17 to 58.10) and yields higher 4-bit utility on NEWS for GA+GDR (40.06 to 44.82, increase of 4.76). LoRA also substantially reduces privacy leakage under 4-bit PTQ, e.g., for GA+KLR on BOOKS, PrivLeak moves from -25.68 to -5.86 (closer to ideal 0), while maintaining strong forgetting (VerMem and KnowMem near 0). Thus, using LoRA for Machine Unlearning is beneficial for scenarios where quantization is necessary for model deployment.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:01:40Z。旧 registry Updated:v1：2026-02-16T01:55:54Z（不作首公开）。

## 2602.13156

[In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach](https://arxiv.org/abs/2602.13156v1)

Rapidly evolving cyberattacks demand incident response systems that can autonomously learn and adapt to changing threats. Prior work has extensively explored the reinforcement learning approach, which involves learning response strategies through extensive simulation of the incident. While this approach can be effective, it requires handcrafted modeling of the simulator and suppresses useful semantics from raw system logs and alerts. To address these limitations, we propose to leverage large language models' (LLM) pre-trained security knowledge and in-context learning to create an end-to-end agentic solution for incident response planning. Specifically, our agent integrates four functionalities, perception, reasoning, planning, and action, into one lightweight LLM (14b model). Through fine-tuning and chain-of-thought reasoning, our LLM agent is capable of processing system logs and inferring the underlying network state (perception), updating its conjecture of attack models (reasoning), simulating consequences under different response strategies (planning), and generating an effective response (action). By comparing LLM-simulated outcomes with actual observations, the LLM agent repeatedly refines its attack conjecture and corresponding response, thereby demonstrating in-context adaptation. Our agentic approach is free of modeling and can run on commodity hardware. When evaluated on incident logs reported in the literature, our agent achieves recovery up to 23% faster than those of frontier LLMs.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:09:30Z。旧 registry Updated:v1：2026-02-16T01:56:18Z（不作首公开）。

## 2602.13165

[Asynchronous Verified Semantic Caching for Tiered LLM Architectures](https://arxiv.org/abs/2602.13165v1)

Large language models (LLMs) now sit in the critical path of search, assistance, and agentic workflows, making semantic caching essential for reducing inference cost and latency. Production deployments typically use a tiered static-dynamic design: a static cache of curated, offline vetted responses mined from logs, backed by a dynamic cache populated online. In practice, both tiers are commonly governed by a single embedding similarity threshold, which induces a hard tradeoff: conservative thresholds miss safe reuse opportunities, while aggressive thresholds risk serving semantically incorrect responses. We introduce Krites, an asynchronous, LLM-judged caching policy that expands static coverage without changing serving decisions. On the critical path, Krites behaves exactly like a standard static threshold policy. When the nearest static neighbor of the prompt falls just below the static threshold, Krites asynchronously invokes an LLM judge to verify whether the static response is acceptable for the new prompt. Approved matches are promoted into the dynamic cache, allowing future repeats and paraphrases to reuse curated static answers and expanding static reach over time. In trace-driven simulations on conversational and search workloads, Krites increases the fraction of requests served with curated static answers (direct static hits plus verified promotions) by up to3.9 times for conversational traffic and search-style queries relative to tuned baselines, with unchanged critical path latency.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:25:00Z。旧 registry Updated:v1：2026-02-16T01:56:43Z（不作首公开）。

## 2602.13168

[Realistic Face Reconstruction from Facial Embeddings via Diffusion Models](https://arxiv.org/abs/2602.13168v1)

With the advancement of face recognition (FR) systems, privacy-preserving face recognition (PPFR) systems have gained popularity for their accurate recognition, enhanced facial privacy protection, and robustness to various attacks. However, there are limited studies to further verify privacy risks by reconstructing realistic high-resolution face images from embeddings of these systems, especially for PPFR. In this work, we propose the face embedding mapping (FEM), a general framework that explores Kolmogorov-Arnold Network (KAN) for conducting the embedding-to-face attack by leveraging pre-trained Identity-Preserving diffusion model against state-of-the-art (SOTA) FR and PPFR systems. Based on extensive experiments, we verify that reconstructed faces can be used for accessing other real-word FR systems. Besides, the proposed method shows the robustness in reconstructing faces from the partial and protected face embeddings. Moreover, FEM can be utilized as a tool for evaluating safety of FR and PPFR systems in terms of privacy leakage. All images used in this work are from public datasets.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:28:24Z。旧 registry Updated:v1：2026-02-16T01:56:49Z（不作首公开）。

## 2602.13179

[Fix Before Search: Benchmarking Agentic Query Visual Pre-processing in Multimodal Retrieval-augmented Generation](https://arxiv.org/abs/2602.13179v1)

Multimodal Retrieval-Augmented Generation (MRAG) has emerged as a key paradigm for grounding MLLMs with external knowledge. While query pre-processing (e.g., rewriting) is standard in text-based RAG, existing MRAG pipelines predominantly treat visual inputs as static and immutable, implicitly assuming they are noise-free. However, real-world visual queries are often ``imperfect'' -- suffering from geometric distortions, quality degradation, or semantic ambiguity -- leading to catastrophic retrieval failures. To address this gap, we propose V-QPP-Bench, the first comprehensive benchmark dedicated to Visual Query Pre-processing (V-QPP). We formulate V-QPP as an agentic decision-making task where MLLMs must autonomously diagnose imperfections and deploy perceptual tools to refine queries. Our extensive evaluation across 46,700 imperfect queries and diverse MRAG paradigms reveals three critical insights: (1) Vulnerability -- visual imperfections severely degrade both retrieval recall and end-to-end MRAG performance; (2) Restoration Potential \&amp; Bottleneck -- while oracle preprocessing recovers near-perfect performance, off-the-shelf MLLMs struggle with tool selection and parameter prediction without specialized training; and (3) Training Enhancement -- supervised fine-tuning enables compact models to achieve comparable or superior performance to larger proprietary models, demonstrating the benchmark's value for developing robust MRAG systems The code is available at https://github.com/phycholosogy/VQQP_Bench

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:39:48Z。旧 registry Updated:v1：2026-02-16T01:57:13Z（不作首公开）。

## 2602.13185

[FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control](https://arxiv.org/abs/2602.13185v1)

Effective and generalizable control in video generation remains a significant challenge. While many methods rely on ambiguous or task-specific signals, we argue that a fundamental disentanglement of "appearance" and "motion" provides a more robust and scalable pathway. We propose FlexAM, a unified framework built upon a novel 3D control signal. This signal represents video dynamics as a point cloud, introducing three key enhancements: multi-frequency positional encoding to distinguish fine-grained motion, depth-aware encoding, and a flexible control signal for balancing precision and generalization. This representation allows FlexAM to effectively disentangle appearance and motion, enabling a wide range of tasks including I2V/V2V editing, camera control, and spatial object editing. Extensive experiments demonstrate that FlexAM achieves superior performance across all evaluated tasks.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:52:11Z。旧 registry Updated:v1：2026-02-16T01:57:48Z（不作首公开）。

## 2602.13191

[CoPE-VideoLM: Leveraging Codec Primitives For Efficient Video Language Modeling](https://arxiv.org/abs/2602.13191v1)

Video Language Models (VideoLMs) enable AI systems to understand temporal dynamics in videos. To fit within the maximum context window constraint, current methods use keyframe sampling which often misses both macro-level events and micro-level details due to the sparse temporal coverage. Furthermore, processing full images and their tokens for each frame incurs substantial computational overhead. We address these limitations by leveraging video codec primitives (specifically motion vectors and residuals) which natively encode video redundancy and sparsity without requiring expensive full-image encoding for most frames. To this end, we introduce lightweight transformer-based encoders that aggregate codec primitives and align their representations with image encoder embeddings through a pre-training strategy that accelerates convergence during end-to-end fine-tuning. Our approach, CoPE-VideoLM, reduces the time-to-first-token by up to 86% and token usage by up to 93% compared to standard VideoLMs. Moreover, by varying the keyframe and codec primitive densities we maintain or exceed performance on 14 diverse video understanding benchmarks spanning general question answering, temporal and motion reasoning, long-form understanding, and spatial scene understanding.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:57:31Z。旧 registry Updated:v1：2026-02-16T01:58:08Z（不作首公开）。

## 2602.13193

[Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/abs/2602.13193v1)

Pretrained vision-language models (VLMs) can make semantic and visual inferences across diverse settings, providing valuable common-sense priors for robotic control. However, effectively grounding this knowledge in robot behaviors remains an open challenge. Prior methods often employ a hierarchical approach where VLMs reason over high-level commands to be executed by separate low-level policies, e.g., vision-language-action models (VLAs). The interface between VLMs and VLAs is usually natural language task instructions, which fundamentally limits how much VLM reasoning can steer low-level behavior. We thus introduce Steerable Policies: VLAs trained on rich synthetic commands at various levels of abstraction, like subtasks, motions, and grounded pixel coordinates. By improving low-level controllability, Steerable Policies can unlock pretrained knowledge in VLMs, enabling improved task generalization. We demonstrate this benefit by controlling our Steerable Policies with both a learned high-level embodied reasoner and an off-the-shelf VLM prompted to reason over command abstractions via in-context learning. Across extensive real-world manipulation experiments, these two novel methods outperform prior embodied reasoning VLAs and VLM-based hierarchical baselines, including on challenging generalization and long-horizon tasks.
 Website: steerable-policies.github.io

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:57:56Z。旧 registry Updated:v1：2026-02-16T01:58:11Z（不作首公开）。

## 2602.13194

[Semantic Chunking and the Entropy of Natural Language](https://arxiv.org/abs/2602.13194v1)

The entropy rate of printed English is famously estimated to be about one bit per character, a benchmark that modern large language models (LLMs) have only recently approached. This entropy rate implies that English contains nearly 80 percent redundancy relative to the five bits per character expected for random text. We introduce a statistical model that attempts to capture the intricate multi-scale structure of natural language, providing a first-principles account of this redundancy level. Our model describes a procedure of self-similarly segmenting text into semantically coherent chunks down to the single-word level. The semantic structure of the text can then be hierarchically decomposed, allowing for analytical treatment. Numerical experiments with modern LLMs and open datasets suggest that our model quantitatively captures the structure of real texts at different levels of the semantic hierarchy. The entropy rate predicted by our model agrees with the estimated entropy rate of printed English. Moreover, our theory further reveals that the entropy rate of natural language is not fixed but should increase systematically with the semantic complexity of corpora, which are captured by the only free parameter in our model.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:58:10Z。旧 registry Updated:v1：2026-02-16T01:58:13Z（不作首公开）。

## 2602.13195

[Conversational Image Segmentation: Grounding Abstract Concepts with Scalable Supervision](https://arxiv.org/abs/2602.13195v1)

Conversational image segmentation grounds abstract, intent-driven concepts into pixel-accurate masks. Prior work on referring image grounding focuses on categorical and spatial queries (e.g., "left-most apple") and overlooks functional and physical reasoning (e.g., "where can I safely store the knife?"). We address this gap and introduce Conversational Image Segmentation (CIS) and ConverSeg, a benchmark spanning entities, spatial relations, intent, affordances, functions, safety, and physical reasoning. We also present ConverSeg-Net, which fuses strong segmentation priors with language understanding, and an AI-powered data engine that generates prompt-mask pairs without human supervision. We show that current language-guided segmentation models are inadequate for CIS, while ConverSeg-Net trained on our data engine achieves significant gains on ConverSeg and maintains strong performance on existing language-guided segmentation benchmarks. Project webpage: https://glab-caltech.github.io/converseg/

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:58:30Z。旧 registry Updated:v1：2026-02-16T01:58:14Z（不作首公开）。

## 2602.13197

[Imitating What Works: Simulation-Filtered Modular Policy Learning from Human Videos](https://arxiv.org/abs/2602.13197v1)

The ability to learn manipulation skills by watching videos of humans has the potential to unlock a new source of highly scalable data for robot learning. Here, we tackle prehensile manipulation, in which tasks involve grasping an object before performing various post-grasp motions. Human videos offer strong signals for learning the post-grasp motions, but they are less useful for learning the prerequisite grasping behaviors, especially for robots without human-like hands. A promising way forward is to use a modular policy design, leveraging a dedicated grasp generator to produce stable grasps. However, arbitrary stable grasps are often not task-compatible, hindering the robot's ability to perform the desired downstream motion. To address this challenge, we present Perceive-Simulate-Imitate (PSI), a framework for training a modular manipulation policy using human video motion data processed by paired grasp-trajectory filtering in simulation. This simulation step extends the trajectory data with grasp suitability labels, which allows for supervised learning of task-oriented grasping capabilities. We show through real-world experiments that our framework can be used to learn precise manipulation skills efficiently without any robot data, resulting in significantly more robust performance than using a grasp generator naively.

Submitted:v1（仅身份线索，不作公开日期）：2026-02-13T18:59:10Z。旧 registry Updated:v1：2026-02-16T01:58:19Z（不作首公开）。


