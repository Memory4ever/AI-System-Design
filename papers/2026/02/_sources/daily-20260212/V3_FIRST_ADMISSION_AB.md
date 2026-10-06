# 首批准入完整题摘

执行：2026-10-04；这是校准材料，不是冻结候选或证据完成。日期继续核验。

## 2602.09578 — Rollout-Training Co-Design for Efficient LLM-Based Multi-Agent Reinforcement Learning

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Despite algorithm-level innovations for multi-agent reinforcement learning (MARL), the underlying networked infrastructure for large-scale MARL training remains underexplored. Existing training frameworks primarily optimize for single-agent scenarios and fail to address the unique system-level challenges of MARL, including rollout-training synchronization barriers, rollout load imbalance, and training resource underutilization. To bridge this gap, we propose FlexMARL, the first end-to-end training framework that holistically optimizes rollout, training, and their orchestration for large-scale LLM-based MARL. Specifically, FlexMARL introduces the joint orchestrator to manage data flow under the rollout-training disaggregated architecture. Building upon the experience store, a novel micro-batch driven asynchronous pipeline eliminates the synchronization barriers while providing strong consistency guarantees. Rollout engine adopts a parallel sampling scheme combined with hierarchical load balancing, which adapts to skewed inter/intra-agent request patterns. Training engine achieves on-demand hardware binding through agent-centric resource allocation. The training states of different agents are swapped via unified and location-agnostic communication. Empirical results on a large-scale production cluster demonstrate that FlexMARL achieves up to 7.3x speedup and improves hardware utilization by up to 5.6x compared to existing frameworks.

Primary: https://arxiv.org/abs/2602.09578v1

## 2602.09725 — Efficient Remote KV Cache Reuse with GPU-native Video Codec

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Remote KV cache reuse fetches KV cache for identical contexts from remote storage, avoiding recomputation, accelerating LLM inference. While it excels in high-speed networks, its performance degrades significantly in bandwidth-limited scenarios. Recent studies address this by transmitting KV caches in compressed form, but the associated heavyweight decompression counteracts the KV reuse benefits. In this paper, we propose an efficient and widely deployable remote KV cache reuse solution that leverages GPU-native video codecs. Our system, KVCodec, enables effective KV cache coding with two techniques. The codec-friendly tensor layout compresses the KV cache in a highly compact video format, enabling fast transmission. The efficient KV fetcher orchestrates the transmission, decoding, and restoration of compressed KV caches in an efficient pipelined manner, eliminating resource contention, masking network fluctuations, and achieving minimum time-to-first-token (TTFT). We prototype KVCodec on diverse GPUs from high- to low-end. Experiments reveal that it reduces TTFT by up to 3.51 times while maintaining lossless accuracy, compared to SOTA methods.

Primary: https://arxiv.org/abs/2602.09725v1

## 2602.09345 — AgentCgroup: Understanding and Controlling OS Resources of AI Agents

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

AI agents are increasingly deployed in multi-tenant cloud environments, where they execute diverse tool calls within sandboxed containers, each call with distinct resource demands and rapid fluctuations. We present a systematic characterization of OS-level resource dynamics in sandboxed AI coding agents, analyzing 144 software engineering tasks from the SWE-rebench benchmark across two LLM models. Our measurements reveal that (1) OS-level execution (tool calls, container and agent initialization) accounts for 55-60% of end-to-end task latency; (2) memory, not CPU, is the concurrency bottleneck; (3) memory spikes are tool-call-driven with a up to 15.4x peak-to-average ratio; and (4) resource demands are highly unpredictable across tasks, runs, and models. Comparing these characteristics against serverless, microservice, and batch workloads, we identify three mismatches in existing resource controls: a granularity mismatch (container-level policies vs. tool-call-level dynamics), a responsiveness mismatch (user-space reaction vs. sub-second unpredictable bursts), and an adaptability mismatch (history-based prediction vs. non-deterministic stateful execution). We propose AgentCgroup, an intent-driven eBPF-based resource controller that exploits agents ability to declare resource needs and reconstruct execution strategies, using hierarchical cgroup structures aligned with tool-call boundaries, in-kernel enforcement via sched_ext and memcg_bpf_ops, and runtime-adaptive policies. Preliminary evaluation demonstrates improved multi-tenant isolation and reduced resource waste. AgentCgroup is open-source at https://github.com/eunomia-bpf/agentcgroup

Primary: https://arxiv.org/abs/2602.09345v1

## 2602.10090 — Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Recent advances in large language model (LLM) have empowered autonomous agents to perform multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets and obtain high-quality observations. Notably, these environments are code-driven and backed by databases, providing more reliable and consistent state transitions than environments simulated by LLMs. Moreover, they enable more efficient agent interaction compared with collecting trajectories from realistic environments. To demonstrate the effectiveness of this resource, we perform large-scale reinforcement learning for multi-turn tool-use agents. Thanks to the fully executable environments and accessible database states, we can also design reliable reward functions. Experiments on three benchmarks show that training exclusively in synthetic environments, rather than benchmark-specific ones, yields strong out-of-distribution generalization. The code is available at https://github.com/Snowflake-Labs/agent-world-model.

Primary: https://arxiv.org/abs/2602.10090v1

## 2602.09591 — On the Optimal Reasoning Length for RL-Trained Language Models

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Reinforcement learning substantially improves reasoning in large language models, but it also tends to lengthen chain-of-thought outputs and increase computational cost. Although length-control methods have been proposed, the length-accuracy relationship they induce remains unclear. We train policies with several length-control methods on multiple base models in a controlled setup and find that, across both mathematical reasoning and code generation, accuracy is non-monotonic in output length, peaking at an intermediate value. Mode accuracy, however, continues to improve with length even in settings where sample accuracy plateaus or declines, indicating that the non-monotonic length-accuracy relationship is driven by dispersion around an increasingly correct center.

Primary: https://arxiv.org/abs/2602.09591v1

## 2602.09598 — Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Tool-integrated reasoning (TIR) enables LLM agents to solve tasks through planning, tool use, and iterative revision, but outcome-only reinforcement learning in this setting suffers from sparse, delayed rewards and weak step-level credit assignment. In long-horizon TIR trajectories, an early irrecoverable mistake can determine success or failure, making it crucial to localize the first irrecoverable step and leverage it for fine-grained credit assignment. We propose Error-Localized Policy Optimization (ELPO), which localizes the first irrecoverable step via binary-search rollout trees under a fixed rollout budget, converts the resulting tree into stable learning signals through hierarchical advantage attribution, and applies error-localized adaptive clipping to strengthen corrective updates on the critical step and its suffix. Across TIR benchmarks in math, science QA, and code execution, ELPO consistently outperforms strong Agentic RL baselines under comparable sampling budgets, with additional gains in Pass@K and Major@K scaling, rollout ranking quality, and tool-call efficiency. Our code will be publicly released soon.

Primary: https://arxiv.org/abs/2602.09598v1

## 2602.09501 — Where-to-Unmask: Ground-Truth-Guided Unmasking Order Learning for Masked Diffusion Language Models

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Masked Diffusion Language Models (MDLMs) generate text by iteratively filling masked tokens, requiring two coupled decisions at each step: which positions to unmask (where-to-unmask) and which tokens to place (what-to-unmask). While standard MDLM training directly optimizes token prediction (what-to-unmask), inference-time unmasking orders (where-to-unmask) are typically determined by heuristic confidence measures or trained through reinforcement learning with costly on-policy rollouts. To address this, we introduce Gt-Margin, a position-wise score derived from ground-truth tokens, defined as the probability margin between the correct token and its strongest alternative. Gt-Margin yields an oracle unmasking order that prioritizes easier positions first under each partially masked state. We demonstrate that leveraging this oracle unmasking order significantly enhances final generation quality, particularly on logical reasoning benchmarks. Building on this insight, we train a supervised unmasking planner via learning-to-rank to imitate the oracle ordering from masked contexts. The resulting planner integrates into standard MDLM sampling to select where-to-unmask, improving reasoning accuracy without modifying the token prediction model.

Primary: https://arxiv.org/abs/2602.09501v1

## 2602.09297 — Laplacian Heads Improve Transformers by Smoothing Token Representations

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Transformers update token representations through multi-head attention and residual connections as $X \leftarrow X + \sum_{i} P^{(i)}XW_{V_i}W_{o_i}$, where $P^{(i)}$ is the softmax attention matrix in head $i$. We propose replacing a subset of $P^{(i)}$'s with the Laplacian $I - P^{(i)}$, giving $X \leftarrow X + \sum_{i \in \mathcal{A}} P^{(i)}XW_{V_i}W_{o_i} + \sum_{i \in \mathcal{L}} (I - P^{(i)})XW_{V_i}W_{o_i}$. Our proposal has two motivations. First, it allows attention heads to update the mean of token representations, while Laplacian heads can directly control within-sequence variance. Second, if tokens are viewed as nodes in a graph with edge weights $P^{(i)}$, then $I - P^{(i)}$ is the corresponding graph Laplacian, and the update can be interpreted as one step of heat diffusion on the graph. We show that this simple modification improves performance across supervised learning, language modeling, and self-supervised learning tasks. To investigate why, we examine the token representations learned with and without Laplacian heads. In supervised learning, Laplacian heads collapse token representations within the same sequence and align the sequence means with the geometry of Neural Collapse. In language modeling, they increase the separability of token representations that share the same next-token prediction. In self-supervised learning, they produce token representations whose principal components are better suited for segmentation. Across modalities, they also lead to faster-decaying spectra, indicating stronger token smoothing. Overall, our findings challenge the prevailing view that token oversmoothing is inherently harmful, showing instead that certain forms of smoothing can be beneficial.

Primary: https://arxiv.org/abs/2602.09297v1

## 2602.09268 — Rethinking Global Text Conditioning in Diffusion Transformers

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Diffusion transformers typically incorporate textual information via attention layers and a modulation mechanism using a pooled text embedding. Nevertheless, recent approaches discard modulation-based text conditioning and rely exclusively on attention. In this paper, we address whether modulation-based text conditioning is necessary and whether it can provide any performance advantage. Our analysis shows that, in its conventional usage, the pooled embedding contributes little to overall performance, suggesting that attention alone is generally sufficient for faithfully propagating prompt information. However, we reveal that the pooled embedding can provide significant gains when used from a different perspective-serving as guidance and enabling controllable shifts toward more desirable properties. This approach is training-free, simple to implement, incurs negligible runtime overhead, and can be applied to various diffusion models, bringing improvements across diverse tasks, including text-to-image/video generation and image editing.

Primary: https://arxiv.org/abs/2602.09268v1

## 2602.09138 — PABU: Progress-Aware Belief Update for Efficient LLM Agents

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Large Language Model (LLM) agents commonly condition actions on full action-observation histories, which introduce task-irrelevant information that easily leads to redundant actions and higher inference cost. We propose Progress-Aware Belief Update (PABU), a belief-state framework that compactly represents an agent's state by explicitly modeling task progress and selectively retaining past actions and observations. At each step, the agent predicts its relative progress since the previous round and decides whether the newly encountered interaction should be stored, conditioning future decisions only on the retained subset. Across eight environments in the AgentGym benchmark, and using identical training trajectories, PABU achieves an 81.0% task completion rate, outperforming previous State of the art (SoTA) models with full-history belief by 23.9%. Additionally, PABU's progress-oriented action selection improves efficiency, reducing the average number of interaction steps to 9.5, corresponding to a 26.9% reduction. Ablation studies show that both explicit progress prediction and selective retention are necessary for robust belief learning and performance gains.

Primary: https://arxiv.org/abs/2602.09138v1

## 2602.09341 — Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Multi-agent systems (MAS) can substantially extend the reasoning capacity of large language models (LLMs), yet most frameworks still aggregate agent outputs with majority voting. This heuristic discards the evidential structure of reasoning traces and is brittle under the confabulation consensus, where agents share correlated biases and converge on the same incorrect rationale. We introduce AgentAuditor, which replaces voting with a path search over a Reasoning Tree that explicitly represents agreements and divergences among agent traces. AgentAuditor resolves conflicts by comparing reasoning branches at critical divergence points, turning global adjudication into efficient, localized verification. We further propose Anti-Consensus Preference Optimization (ACPO), which trains the adjudicator on majority-failure cases and rewards evidence-based minority selections over popular errors. AgentAuditor is agnostic to MAS setting, and we find across 5 popular settings that it yields up to 5% absolute accuracy improvement over a majority vote, and up to 3% over using LLM-as-Judge.

Primary: https://arxiv.org/abs/2602.09341v1

## 2602.09937 — Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Failures in large-scale cloud systems incur substantial financial losses, making automated Root Cause Analysis (RCA) essential for operational stability. Recent efforts leverage Large Language Model (LLM) agents to automate this task, yet existing systems exhibit low detection accuracy even with capable models, and current evaluation frameworks assess only final answer correctness without revealing why the agent's reasoning failed. This paper presents a process level failure analysis of LLM-based RCA agents. We execute the full OpenRCA benchmark across five LLM models, producing 1,675 agent runs, and classify observed failures into 12 pitfall types across intra-agent reasoning, inter-agent communication, and agent-environment interaction. Our analysis reveals that the most prevalent pitfalls, notably hallucinated data interpretation and incomplete exploration, persist across all models regardless of capability tier, indicating that these failures originate from the shared agent architecture rather than from individual model limitations. Controlled mitigation experiments further show that prompt engineering alone cannot resolve the dominant pitfalls, whereas enriching the inter-agent communication protocol reduces communication-related failures by up to 15 percentage points. The pitfall taxonomy and diagnostic methodology developed in this work provide a foundation for designing more reliable autonomous agents for cloud RCA.

Primary: https://arxiv.org/abs/2602.09937v1

## 2602.09430 — AtomBridge: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Robotic laboratories play a critical role in autonomous scientific discovery by enabling scalable, continuous experimental execution. Recent vision-language-action (VLA) models offer a promising foundation for robotic laboratories. However, scientific experiments typically involve long-horizon tasks composed of multiple atomic tasks. Existing VLA models may fail to perform composed tasks formed by reordering and composing these known atomic actions. This limitation can arise from a skill-chaining gap caused by robot-state mismatch: the terminal robot state of one skill can fall outside the valid initial-state distribution of the next. To address this challenge, we propose AtomBridge, an Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments. AtomBridge attaches at inference time to a VLA policy already fine-tuned on atomic tasks, while keeping its weights fixed. At each task boundary, it uses LLM-based transition reasoning and robotic-action code generation to insert transitional actions between consecutive tasks. This plug-and-play design mitigates the skill-chaining gap caused by robot-state mismatch without additional VLA fine-tuning or demonstrations of composed long-horizon sequences. Across scientific manipulation sequences in simulation and a real-world experimental environment, AtomBridge improves execution continuity and per-step atomic-task success. On 8-step composed tasks, AtomBridge improves full-sequence success by 10%~25%.

Primary: https://arxiv.org/abs/2602.09430v1

## 2602.09063 — scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

As single-cell RNA sequencing datasets grow in adoption, scale, and complexity, data analysis remains a bottleneck for many research groups. Although frontier AI agents have improved dramatically at software engineering and general data analysis, it remains unclear whether they can extract biological insight from messy, real-world single-cell datasets. We introduce scBench, a benchmark of 394 verifiable problems derived from practical scRNA-seq workflows spanning six sequencing platforms and seven task categories. Each problem provides a snapshot of experimental data immediately prior to an analysis step and a deterministic grader that evaluates recovery of a key biological result. Benchmark data on eight frontier models shows that accuracy ranges from 29-53%, with strong model-task and model-platform interactions. Platform choice affects accuracy as much as model choice, with 40+ percentage point drops on less-documented technologies. scBench complements SpatialBench to cover the two dominant single-cell modalities, serving both as a measurement tool and a diagnostic lens for developing agents that can analyze real scRNA-seq datasets faithfully and reproducibly.

Primary: https://arxiv.org/abs/2602.09063v1

## 2602.09109 — Distributed Hybrid Parallelism for Large Language Models: Comparative Study and System Design Guide

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

With the rapid growth of large language models (LLMs), a wide range of methods have been developed to distribute computation and memory across hardware devices for efficient training and inference. While existing surveys provide descriptive overviews of these techniques, systematic analysis of their benefits and trade offs and how such insights can inform principled methodology for designing optimal distributed systems remain limited. This paper offers a comprehensive review of collective operations and distributed parallel strategies, complemented by mathematical formulations to deepen theoretical understanding. We further examine hybrid parallelization designs, emphasizing communication computation overlap across different stages of model deployment, including both training and inference. Recent advances in automated search for optimal hybrid parallelization strategies using cost models are also discussed. Moreover, we present case studies with mainstream architecture categories to reveal empirical insights to guide researchers and practitioners in parallelism strategy selection. Finally, we highlight open challenges and limitations of current LLM training paradigms and outline promising directions for the next generation of large scale model development.

Primary: https://arxiv.org/abs/2602.09109v1

## 2602.09305 — Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation

原文完整摘要（旧原始身份缓存，当前准入重判；日期字段不复用）：

Large Language Models (LLMs) demonstrate transformative potential, yet their reasoning remains inconsistent and unreliable. Reinforcement learning (RL)-based fine-tuning is a key mechanism for improvement, but its effectiveness is fundamentally governed by reward design. Despite its importance, the relationship between reward modeling and core LLM challenges--such as evaluation bias, hallucination, distribution shift, and efficient learning--remains poorly understood. This work argues that reward modeling is not merely an implementation detail but a central architect of reasoning alignment, shaping what models learn, how they generalize, and whether their outputs can be trusted. We introduce Reasoning-Aligned Reinforcement Learning (RARL), a reasoning-centric taxonomic perspective that organizes diverse reward paradigms for multi-step reasoning. Within this perspective, we present a taxonomy of reward mechanisms, analyze reward hacking as a pervasive failure mode, and examine how reward signals unify challenges ranging from inference-time scaling to hallucination mitigation. We further critically evaluate existing benchmarks, highlighting vulnerabilities such as data contamination and reward misalignment, and outline directions for more robust evaluation. By integrating fragmented research threads and clarifying the interplay between reward design and fundamental reasoning capabilities, this work provides a foundational roadmap for building reasoning models that are robust, verifiable, and trustworthy.

Primary: https://arxiv.org/abs/2602.09305v1


