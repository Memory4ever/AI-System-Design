# 2026-03-29 exact-v1 abstract samples

2026-10-02本日定点官方API只读返回，`https://export.arxiv.org/api/query?id_list=2603.27439v1,2603.27141v1,2603.27148v1,2604.19776v1`。下列published/updated是API的Submitted字段，不当首次公开时间；原文不表示本书采用性能数字。只有这4份完整题摘，不表示宽库存全文审阅。

```text
id http://arxiv.org/abs/2603.27141v1
title Routing Sensitivity Without Controllability: A Diagnostic Study of Fairness in MoE Language Models
published 2026-03-28T05:33:42Z
updated 2026-03-28T05:33:42Z
summary Mixture-of-Experts (MoE) language models are universally sensitive to demographic content at the routing level, yet exploiting this sensitivity for fairness control is structurally limited. We introduce Fairness-Aware Routing Equilibrium (FARE), a diagnostic framework designed to probe the limits of routing-level stereotype intervention across diverse MoE architectures. FARE reveals that routing-level preference shifts are either unachievable (Mixtral, Qwen1.5, Qwen3), statistically non-robust (DeepSeekMoE), or accompanied by substantial utility cost (OLMoE, -4.4%p CrowS-Pairs at -6.3%p TQA). Critically, even where log-likelihood preference shifts are robust, they do not transfer to decoded generation: expanded evaluations on both non-null models yield null results across all generation metrics. Group-level expert masking reveals why: bias and core knowledge are deeply entangled within expert groups. These findings indicate that routing sensitivity is necessary but insufficient for stereotype control, and identify specific architectural conditions that can inform the design of more controllable future MoE systems.

id http://arxiv.org/abs/2603.27148v1
title SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do
published 2026-03-28T05:52:04Z
updated 2026-03-28T05:52:04Z
summary When an LLM agent reads a confidential file, then writes a summary, then emails it externally, no single step is unsafe, but the sequence is a data leak. We call this safety drift: individually safe actions compounding into violations. Prior work has measured this problem; we predict it. SafetyDrift models agent safety trajectories as absorbing Markov chains, computing the probability that a trajectory will reach a violation within a given number of steps via closed form absorption analysis. A consequence of the monotonic state design is that every agent will eventually violate safety if left unsupervised (absorption probability 1.0 from all states), making the practical question not if but when, and motivating our focus on finite horizon prediction. Across 357 traces spanning 40 realistic tasks in four categories, we discover that "points of no return" are sharply task dependent: in communication tasks, agents that reach even a mild risk state have an 85% chance of violating safety within five steps, while in technical tasks the probability stays below 5% from any state. A lightweight monitor built on these models detects 94.7% of violations with 3.7 steps of advance warning at negligible computational cost, outperforming both keyword matching (44.7% detection, 55.9% false positive rate) and per step LLM judges (52.6% detection, 38.2% false positive rate) while running over 60,000x faster.

id http://arxiv.org/abs/2603.27439v1
title Attacking AI Accelerators by Leveraging Arithmetic Properties of Addition
published 2026-03-28T23:03:27Z
updated 2026-03-28T23:03:27Z
summary The dependability of AI models relies largely on the reliability of the underlying computation hardware. Hardware aging attacks can compromise the computing substrate and disrupt AI models over the long run. In this work, we present a new hardware aging attack that exploits commutative properties of addition to disrupt the multiply-and-add operation that forms the backbone of almost all AI models. By permuting the inputs of an adder, the attack preserves functional correctness while inducing unbalanced stress among transistors, accelerating delay degradation in the circuit. Unlike prior approaches that rely on input manipulation, additional trojan circuitry, etc., the proposed method incurs virtually no area or software overhead. Experimental results with two types of multipliers, different bit widths, a mix of AI models and datasets demonstrates that the proposed attack degrades inference accuracy by up to 64% in 4 years, posing a significant threat to AI accelerators. The attack can also be extended to arithmetic units of general-purpose processors.

id http://arxiv.org/abs/2604.19776v1
title Development and Preliminary Evaluation of a Domain-Specific Large Language Model for Tuberculosis Care in South Africa
published 2026-03-28T11:22:05Z
updated 2026-03-28T11:22:05Z
summary Tuberculosis (TB) is one of the world's deadliest infectious diseases, and in South Africa, it contributes a significant burden to the country's health care system. This paper presents an experimental study on the development of a domain-specific Large Language Model (DS-LLM) for TB care that can help to alleviate the burden on patients and healthcare providers. To achieve this, a literature review was conducted to understand current LLM development strategies, specifically in the medical domain. Thereafter, data were collected from South African TB guidelines, selected TB literature, and existing benchmark medical datasets. We performed LLM fine-tuning by using the Quantised Low-Rank Adaptation (QLoRA) algorithm on a medical LLM (BioMistral-7B), and also implemented Retrieval-Augmented Generation using GraphRAG. The developed DS-LLM was evaluated against the base BioMistral-7B model and a general-purpose LLM using a mix of automated metrics and quantitative ratings. The results show that the DS-LLM had better performance compared to the base model in terms of its contextual alignment (lexical, semantic, and knowledge) for TB care in South Africa.
```

