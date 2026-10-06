# 2601.09088v1 — minimum necessary primary

Source: https://arxiv.org/html/2601.09088v1 . Method§4/5 and training/evaluation§6.4/7.3/7.5–6 only; no all-attachments review.

## Raw body offsets 29269–45166

4 Divergence-aware Sampling
Despite employing temperature-scheduled learning to broaden coverage of the teacher’s modes, the student still struggles to align with the teacher’s sequence-level distribution. Classical logit distillation leverages teacher logit distribution to precisely calibrate the student’s token-level probabilities, increasing or decreasing them as needed (11; 1). By contrast, SFT on teacher-generated data typically amplifies the probabilities of all target tokens relative to the student’s current predictions. This can induce misleading gradients: for tokens assigned low probabilities by the teacher but high probabilities by the student, SFT erroneously pushes the student’s probabilities even higher, thereby driving them away from the teacher’s distribution. This discrepancy motivates a core question: How can we identify a teacher-derived sequence-level distribution that is better aligned with the student model’s learning capacity?
Figure 5: Joint comparison of the three models’ predicted probabilities. An example of output probabilities: the x-axis indexes sentences, and the y-axis shows predicted probabilities. Foreground lines plot the probabilities of the three models, while background colors indicate the inferred source of each sentence. By comparing probability differences, every sentence is categorized into one of four source types.
To identify an effective sequence-level target distribution from the student’s perspective, we introduce a distribution decomposition and analysis framework (33): each sequence-level response is decomposed into consecutive sentences and the corresponding sentence-level generation probabilities are computed for both the teacher and the student; by quantifying the probability discrepancy on each shared sentence, we categorize distinct behavioral patterns; finally, we systematically analyze these patterns (i.e., components) and establish their empirical relationship to effective student learning.
Concretely, following the experimental setup in Section 3, we first sample responses from the distilled model (i.e., the trained student model) on test-set prompts and segment each response into sentences. This sentence-level analysis ensures the broad applicability of our method across heterogeneous model families—unlike approaches such as on-policy distillation, which typically requires all models to share the same tokenizer and vocabulary (a constraint imposed by its reliance on token-level supervision).
Then, we feed these samples to the teacher model, the pre-distillation student model (hereafter, the “student model”), and the post-distillation student model (hereafter, the “distilled model”).
For each sentence of the response data, we compute its probability under each of the three models as the geometric mean of per-token probabilities in this sentence.
As illustrated in Figure 5, we observe that the sequence-level distribution admits a natural decomposition into four well-defined distribution types (each corresponding to a distinct sentence category). Let pTp_{T}, pSp_{S} and pDp_{D} denote the predicted probabilities of the teacher, student, and distilled models for the same sentence, respectively. Based on the relative magnitude discrepancies of these probabilities, we define the following distribution (or sentence) types:
• 
Student-originated sentences (hereafter referred to as Student Sentence) and teacher-originated sentences (hereafter referred to as Teacher Sentence): When there is a large discrepancy between pSp_{S} and pTp_{T}, the distilled model still outputs the sentence, suggesting the sentence is more consistent with the model assigning the higher likelihood. For example, if pT≫pSp_{T}\gg p_{S} and distilled model nevertheless produces the sentence, it is more likely teacher-originated. Moreover, when pT≫pSp_{T}\gg p_{S}, the student can relatively freely increase its probability under SFT without concern about misleading gradients. Intuitively, this type of pattern is more likely to apply under our current distillation setup. Note that a Teacher Sentence does not imply that the action is entirely absent from the student model, but rather that it is primarily originated from the teacher. The same applies to a Student Sentence.
• 
Pre-existing sentences in both pre-distillation student model and teacher model, not enhanced by distillation (hereafter referred to as Shared Sentence): The output probabilities for these sentences are similar across all three models. This indicates that these sentences are already well-supported by both the pre-distillation student and the teacher, and that distillation does not materially change their probabilities or increase inter-model distribution discrepancies.
• 
Pre-existing sentences boosted through distillation (hereafter referred to as Boosted Sentence): Similar to the second type, pTp_{T} and pSp_{S} remain close, but pDp_{D} differs significantly (and pDp_{D} is typically higher in practice, since trajectories are sampled from the distilled model). These sentences also exist in both the teacher and the student before distillation, but their probabilities are amplified by training on distilled data.
Having decoupled the output distributions, we next investigate which distribution types are most conducive to the student model’s learning (i.e., those that best support effective knowledge acquisition). To this end, we assess effective learning by analyzing the correlation between the four distribution types and test-set answer correctness.
Specifically, for each sentence position, we compute the probability that the distilled model assigns to each distribution type. Since solutions often contain multiple sentences (correct answers typically contain fewer sentences than incorrect ones), analyzing at the sentence-position-level, rather than at the full solution level, allows us to focus more directly on the distribution types themselves and mitigate confounding effects arising from sentence position. For example, to estimate the probability of the Teacher Sentence at the third sentence position, we calculate the fraction of third sentences that are categorized as Teacher Sentence, across all correct and incorrect model outputs. Notably, the number of sentences per answer varies, limiting data availability at later positions.
To ensure statistical reliability, we therefore focus primarily on earlier sentence positions, where sufficient samples exist.
We also replicate this analysis on the open-source model DeepSeek-Distill-Qwen3-8B (13) to ensure generalizability.
As shown in Figure 6, across models, Teacher Sentences tend to receive higher probabilities in correct answers, evidenced by the light-green solid line (—–) persistently lying above the light-green dashed line (- - -). This is as expected: since the teacher model performs better on the test set, aligning the student’s outputs with teacher-preferred responses enhances learning efficacy and, consequently, the likelihood of generating correct answers.
In contrast, we find that Shared Sentence and Student Sentence occur with low probability and exert a relatively minor influence. For Boosted Sentence, we observe a potential negative correlation between Boosted Sentences and test-set accuracy. We conjecture that this possibly stem from suboptimal misleading gradients. More importantly, the distillation pipeline only admits the teacher and student models prior to training, rendering it impossible to directly identify Boosted Sentences. We therefore focus primarily on Teacher Sentences in the remainder of this work.
Figure 6: Position-wise distribution over the four sentence types for our internally trained model (left two panels) and the open-source DeepSeek-Distill-Qwen3-8B (right two panels). The x-axis denotes the sentence position, and the y-axis denotes the predicted probabilities of the four sentence types. Solid lines (—–) indicate probabilities when the answer is correct, while dashed lines(- - -) indicate probabilities when the answer is incorrect. Δ\Delta denotes the area difference between the solid and dashed curves, which reflects the influence of each sentence type on answer correctness.
Building on the above analysis, a natural idea is to emphasize, during training, patterns that are more indicative of answer correctness. Although the full distribution-decomposition framework requires output probabilities from three models (the teacher, the student, and the distilled model) to identify the most effective distribution post hoc, we show that Teacher Sentences/Student Sentences can be identified prior to training: Teacher Sentences/Student Sentences are those sentences for which the teacher assigns significantly higher/lower output probabilities than the student. Therefore, we propose divergence-aware sampling (DAS), which prioritizes training examples rich in Teacher Sentences and thereby implicitly targets a teacher-derived sequence-level distribution better aligned with the student’s learning capacity (33).
This sampling distribution naturally mitigates misleading gradients and facilitates more effective knowledge transfer from teacher to student.
Notably, our method only requires, for each token in the teacher-generated response, its predicted probability by both the teacher and the student. The teacher-side probabilities are naturally obtained during sampling—and are often exposed even by many closed-source APIs—while the student-side probabilities are readily computed from the local model. In contrast, classical logit-based distillation necessitates the teacher’s full-vocabulary logits (i.e., probabilities over the entire vocabulary) at every position. Even recent on-policy distillation methods—when simplified to operate on token-level probabilities—still require, for every token in the student’s generated outputs, the corresponding probabilities under both models. Critically, the teacher-side probabilities for the student’s outputs are typically unavailable for proprietary models.
Table 3: Performance comparison with different settings of training data (RS vs. DAS).
Settings of training data
AIME24
AIME25
Teacher: gpt-oss-120b  Student: Qwen3-4B-Instruct-2507
50K Math + RS (T=0.6T=0.6)
81.7
71.9
50K Math + DAS (T=0.6T=0.6)
83.3
74.2
50K Math + RS (T=1.0T=1.0)
83.1
76.1
100K Math + RS (T=1.0T=1.0)
83.1
78.9
50K Math + DAS (T=1.0T=1.0)
85.0
79.2
Teacher: Qwen3-Next-80B-A3B-Thinking  Student: Qwen3-4B-Instruct-2507
25K Math + RS
79.0
71.3
25K Math + DAS
82.5
71.9
Building on the experimental setup in Section 3, we conduct a controlled comparison between DAS and random sampling (DS) under an identical sampling budget. As shown in Table 3, DAS consistently achieves higher test performance, and in several cases, even surpasses the results obtained by RS after scaling up its data volume. This demonstrates that DAS effectively identifies teacher-generated sequences whose distribution is better aligned with the student’s learning capacity. Further, as shown in the lower part of Table 3 and in Table 4, DAS maintains a clear advantage over random sampling across different teacher models and domains, validating the generalizability of the DAS method.
Table 4: Performance comparison with different settings of training data (RS vs. DAS across domains).
Settings of training data
AIME25
LCB v6
GPQA-D
Teacher: gpt-oss-120b  Student: Qwen3-4B-Instruct-2507
25K Math + 10K Code + 10K Science + RS
74.6
44.1
65.5
25K Math + 10K Code + 10K Science + DAS
75.6
47.3
65.7
Finally, DAS does not require re-sampling data for every new student model. For instance, as demonstrated in Section 7, data curated to match the learning capacity of the Qwen3-4B-Instruct-2507 student model generalizes effectively to the Qwen3-30B-A3B-Instruct-2507 student model.
5 Mixed-policy Distillation
Figure 7: The ratio between cut-off responses under different token lengths.
In the previous stages, we employed off-policy methods to approximate the teacher’s sequence-level distribution through high-quality data generation. Nevertheless, we find that the resulting student model still suffers from exposure bias (41): during training, the student is conditioned on the teacher’s prefix using teacher forcing, whereas at inference time, it must rely on its own autoregressive predictions, leading to a distribution mismatch.
To empirically investigate this phenomenon, we use the student model trained in the previous round (50K DAS sampling, T=0.6; see Table 3) to re-generate the training data within its own context, in order to examine whether the student model is overly reliant on the teacher’s context.
During inference, we set the maximum generation token length to 1.5 times the length of the teacher-provided solution, in order to compare the differences between the teacher’s reference response and the student’s self-generated counterpart. Figure 7 plots the cut-off rate of the student’s generated responses across different training-response lengths, where a higher cut-off rate indicates greater divergence between student and teacher behavior.
The results reveal that, even on the training data, the student still exhibits substantial deviations from the teacher, and this discrepancy becomes increasingly pronounced as the length of the training response grows. This observation confirms that training with teacher forcing under longer teacher prefixes exacerbates exposure bias.
To overcome these limitations, 9 present that on-policy data collection is an effective alternative method. Accordingly, we propose a mixed-policy distillation approach that synergistically combines off-policy and on-policy signals. Specifically, we first use the student model from the previous training round to re-generate responses for the training queries, and then identify instances that differ substantially from the teacher’s outputs, e.g., solutions that have been cut off in Figure 7. For these data points, we randomly cut off the solutions generated by the student and prompt the teacher to continue the generation, thereby enabling the teacher to provide targeted guidance on the student’s errors.
We present an ablation study of the proposed mixed-policy distillation in Table 5. As described above, we collect 7.7K mixed-policy samples, and train the model with only one epoch across these samples.
Our baseline is the model trained
on the 50K DAS-generated dataset at temperature T=0.6 (Table 3).
In addition, we investigate a masking variant, where student-generated portions are masked out, and only teacher-completed segments are retained for training.
Table 5: Ablation of the mixed-policy distillation method. #Num: number of mixed-policy data.
#Num
Mask
AIME24
AIME25
Baseline
50K DAS (T=0.6T=0.6)
—
83.3
74.2
Mixed-Policy Variants
7.7K
✓
80.8
72.3
7.7K
✗
83.3
74.8
To maintain a balanced proportion between mixed-policy and off-policy data during training, we introduce 20K additional off-policy samples for joint training with the mixed-policy data.
Our main experimental observations are as follows:
(1) The results indicate that our mixed-policy dataset, despite containing only 7.7K samples, is capable of enhancing the model’s performance.
(2) The masking variant tends to yield worse performance. This is because masking removes the on-policy segments generated by the student, leaving only the off-policy segments from the teacher for training. The observed performance drop in this setting further demonstrates the importance of incorporating on-policy data during distillation.
As shown in Table 7, we also validate the effectiveness of the mixed-policy distillation approach in our final training pipeline.
Incorporating even a small amount of mixed-policy data yields measurable gains across strong models and diverse domains.
These results motivate continued exploration of this promising direction in the future.


## Raw body offsets 49756–56804

6.4 Multi-stage Training
As illustrated in Figure 2, our training pipeline comprises two main stages: temperature-scheduled learning and mixed-policy distillation. During temperature-scheduled learning, the sampling data used to train DASD-4B-Thinking undergoes a two-stage filtering and training process to better capture the teacher model’s distribution while effectively supporting the student model’s learning. In the subsequent mixed-policy distillation, we construct mixed-policy data via on-policy rejection sampling and off-policy teacher revision. This hybrid strategy mitigates exposure bias by providing targeted, error-aware supervision.
6.4.1 Temperature-scheduled Learning
To better represent the teacher model’s sequence-level distribution, we follow Section 3, and perform two-stage SFT on Qwen3-4B-Instruct-2507: first using low-temperature sampling data, followed by high-temperature sampling data. Training configurations are kept identical across both stages. We use an initial learning rate of 5e-5 that decays to 1e-5 via a cosine scheduler. We set the cutoff length to 64K and employ greedy sequence packing to accelerate training. Given the substantial GPU memory demands of 64K-context training, we leverage ZeRO-3 optimization together with Liger kernels to reduce memory consumption. Training is conducted with a global batch size of 64 over 6 epochs, and we observe consistent performance improvements across epochs.
6.4.2 Mixed-policy Distillation
To mitigate the exposure bias, and inspired by the effectiveness of on-policy data (9), we propose a mixed-policy revision protocol.
Starting from the DAS-curated training set, we sample 50K questions. Each question is fed to the student model trained in the previous stage to generate responses. To align with the teacher’s reference length, we cap the student’s generation at 1.5 times the token count of the corresponding teacher response to the same question. Among the above student-generated solutions, we identify 15K truncated responses. For each truncated response, we discard the portion after a randomly selected position located beyond half of its total length, and then employ the teacher model to rewrite this discarded part.
The teacher continuations that pass predefined quality filters are retained for the student’s further fine-tuning, yielding a total of mixed-policy 12.7K data samples.
7 Experimental Evaluation
7.1 Benchmarks
We evaluate models on five complementary reasoning benchmarks:
• 
AIME24&AIME25 (4): Problem sets from that year’s American Invitational Mathematics Examination (AIME) I/II, each comprising 30 challenging problems, focusing on mathematical reasoning and requiring the correct final answer.
• 
GPQA Diamond (GPQA-D) (42): A graduate-level benchmark of 198 expert-written multiple-choice questions spanning physics, chemistry, and biology, emphasizing ”Google-proof” deep academic reasoning.
• 
LiveCodeBench (LCB) (19):
A continuously updated coding benchmark that mitigates data contamination through strict temporal partitioning.
Beyond code generation, it evaluates self-repair, executable correctness, and test-output prediction.
The benchmark is released in time-based snapshots; v5 contains problems collected from October 2024 to February 2025, and v6 covers problems collected from February 2025 to May 2025.
7.2 Baselines
We release our model, , and evaluate its performance on five public reasoning benchmarks: AIME24, AIME25, LCB and GPQA-D. We compare against two families of state-of-the-art open-source models serving as our primary baselines. All baselines were selected for their demonstrated strength in reasoning and complex problem solving, ensuring a relevant and competitive evaluation context for . Particularly, we categorize these baselines based on the accessibility of their training data. This enables a dual-perspective assessment of :
(i) against top-performing models trained on private or proprietary data, and
(ii) against leading models representing fully transparent, reproducible research.
• 
Open-Weights Only.
This group comprises models that release their weights publicly but keep their training data as proprietary. These models often represent the best performance available from models where the full training process is not disclosed. Our comparison set includes:
– 
The Qwen3 series (4B-Thinking-2507, 8B, 14B, 32B) (47): The world’s most popular model family featuring mainline models (8B, 14B, 32B) with switchable reasoning modes, alongside a dedicated 4B-Thinking variant optimized for complex reasoning over long contexts.
– 
DeepSeek-R1-0528-Qwen3-8B (13): A specialized 8B reasoning model distilled from the powerful teacher model DeepSeek-R1-0528 into a Qwen3-8B backbone.
– 
The GLM-Z1 series (32B-0414, 9B-0414) (49): Models built on the GLM-4 architecture,
enhanced via extended reinforcement learning for mathematical, logical, and coding reasoning.
– 
The Mistral 3 series (3B, 8B) (36):
Compact open-weight models that emphasize efficient reasoning, strong math and coding capabilities, and multilingual generalization, suitable for low-latency, low-memory deployments.
• 
Open-Weights & Open-Data. This group releases both model weights and the curated reasoning datasets, enabling full reproducibility and fostering community-wide study of reasoning acquisition. Included models are:
– 
AM-thinking-v1 (21) and OpenThoughts3-7B (12): These models demonstrate different open-data strategies. AM-thinking combines SFT on 2.9M distilled examples with RL on a Qwen2.5-32B base; OpenThoughts3 achieves strong 7B-level performance via SFT alone on its publicly released 1.2M high-quality reasoning traces.
– 
The Pai-DistillQwen-ThoughtY series (7):
A set of compact models (4B, 8B) distilled from DeepSeek-R1-0528 using 365K curated examples, accompanied by full dataset release.
– 
POLARIS-4B-Preview (5): A model based on Qwen3-4B that highlights the effectiveness of scaling up RL on public data to significantly improve complex, long-context reasoning.
– 
The Nemotron family (6): This collection includes OpenReasoning-Nemotron-7B, distilled from DeepSeek-R1-0528 on a massive 30M example open dataset, and Nemotron-Ultra-253B, a large-scale model targeting high-end reasoning tasks.
Figure 9: Performance versus model size on AIME25 (left) and LCB v5 (right). Each point denotes a model, with the x-axis representing model size (in number of parameters) and the y-axis indicating benchmark score. Points positioned toward the top-left indicate superior efficiency—i.e., higher performance at smaller scale.
7.3 Evaluation Setup
All evaluations were conducted under a unified setup. We consistently set the temperature to 1.0 and top-pp to 1.01.0. For every benchmark, we sampled 64 responses per question and reported the average accuracy to ensure reliable and stable evaluation results. Given the extreme difficulty of AIME24 and AIME25, we set the maximum generation length to 102,400 tokens; For LiveCodeBench and GPQA-D, the limit was set to 81,920 tokens.


## Raw body offsets 61373–64239

7.5 Ablations over training stages
Sections 3, 4, and 5 have validated the individual contributions of our three core components through isolated experiments. In this section, we complement those findings with a holistic ablation of the full training pipeline, examining how performance evolves after each sequential stage. Results are summarized in Table 7.
Table 7: Ablations over training stages on AIME24, AIME25, LiveCodeBench v5, LiveCodeBench v6, and GPQA-D.
AIME24
AIME25
LCB v5
LCB v6
GPQA-D
Qwen3-4B-Instruct-2507
-
47.4
-
35.1
62.5
+ Low-Temperature Training
84.2
74.0
56.6
50.6
67.7
+ High-Temperature Training
87.7
83.0
68.4
67.2
67.6
+ Mixed-Policy Distillation
88.5
83.3
69.3
67.5
68.4
Starting from the Qwen3-4B-Instruct-2507 baseline, we observe consistent performance improvements across the three stages:
Low-temperature training (with DAS) delivers substantial initial gain, boosting AIME25 from 47.4% to 74.0% (+26.6%) and LCB v6 from 35.1% to 50.6% (+15.5%). This confirms that stable, low-variance gradient signals during early training are critical for establishing a solid reasoning foundation.
High-temperature training (with DAS) further enhances performance across key benchmarks, advancing LCB v5 by +11.8% and LCB v6 by +16.6%, while also providing a notable +9.0% gain on AIME25. This demonstrates that diverse exploration under higher temperature effectively expands the policy’s solution coverage once a stable baseline has been established.
Mixed-policy distillation consistently yields performance gains even on top of an already strong model across all benchmarks (e.g., +0.8% on AIME24, +0.3% on AIME25, +0.9% on LCB v5, +0.3% on LCB v6, +0.8% on GPQA-D), supporting the effectiveness of mixed-policy distillation in addressing the exposure-bias issue with minimal training overhead.
7.6 Effect of Divergence-aware Sampling on Data Distribution
Figure 10: Comparison of response probability distributions with/without divergence-aware sampling using different temperatures.
To broaden coverage of the teacher’s output modes, we employ temperature-scheduled learning to collect both low-temperature samples (sharper, more concentrated distributions that cover a narrower probability range around high-probability regions) and high-temperature samples (flatter, broader densities that capture rarer teacher modes). To better identify the target sequence-level distribution that supports effective student learning, we further apply divergence-aware sampling to both data subsets. As illustrated in Figure 10, divergence-aware sampling induces negligible perturbation to the underlying response probability distribution, confirming its orthogonality to temperature scheduling.
This decoupling underpins the strong synergy observed when combining the two strategies, as evidenced by the substantial performance gains in Section 7.5.

