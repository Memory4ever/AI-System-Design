# 2601.09088v1 决定性准入原段

Exact primary https://arxiv.org/html/2601.09088v1 ，仅§4/5必要方法前段，不代表完整Evidence/日期/Books。实际输出字符串偏移29734/41697已核不是目录。

4 
Divergence-aware Sampling
Despite employing temperature-scheduled learning to broaden coverage of the teacher’s modes, the student still struggles to align with the teacher’s sequence-level distribution. Classical logit distillation leverages teacher logit distribution to precisely calibrate the student’s token-level probabilities, increasing or decreasing them as needed 
(
11
; 
1
)
. By contrast, SFT on teacher-generated data typically amplifies the probabilities of all target tokens relative to the student’s current predictions. This can induce misleading gradients: for tokens assigned low probabilities by the teacher but high probabilities by the student, SFT erroneously pushes the student’s probabilities even higher, thereby driving them away from the teacher’s distribution. This discrepancy motivates a core question: How can we identify a teacher-derived sequence-level distribution that is better aligned with the student model’s learning capacity?
Figure 5: 
Joint comparison of the three models’ predicted probabilities. An example of output probabilities: the x-axis indexes sentences, and the y-axis shows predicted probabilities. Foreground lines plot the probabilities of the three models, while background colors indicate the inferred source of each sentence. By comparing probability differences, every sentence is categorized into one of four source types.
To identify an effective sequence-level target distribution from the student’s perspective, we introduce a distribution decomposition and analysis framework 
(
33
)
: each sequence-level response is decomposed into consecutive sentences and the corresponding sentence-level generation probabilities are computed for both the teacher and the student; by quantifying the probability discrepancy on each shared sentence, we categorize distinct behavioral patterns; finally, we systematically analyze these patterns (i.e., components) and establish their empirical relationship to effective student learning.
Concretely, following the experimental setup in Section 
3
, we first sample responses from the distilled model (i.e., the trained student model) on test-set prompts and segment each response into sentences. 
This sentence-level analysis ensures the broad applicability of our method across heterogeneous model families
—unlike approaches such as on-policy distillation, which typically requires all models to share the same tokenizer and vocabulary (a constraint imposed by its reliance on token-level supervision).
Then, we feed these samples to the teacher model, the pre-distillation student model (hereafter, the “student model”), and the post-distillation student model (hereafter, the “distilled model”).
For each sentence of the response data, we compute its probability under each of the three models as the geometric mean of per-token probabilities in this sentence.
As illustrated in Figure 
5
, we observe that the sequence-level distribution admits a natural decomposition into four well-defined distribution types (each corresponding to a distinct sentence category). Let 
p
T
p_{T}
, 
p
S
p_{S}
 and 
p
D
p_{D}
 denote the predicted probabilities of the teacher, student, and distilled models for the same sentence, respectively. Based on the relative magnitude discrepancies of these probabilities, we define the following distribution (or sentence) types:
•
Student-originated sentences (hereafter referred to as 
Student Sentence
) and teacher-originated sentences (hereafter referred to as 
Teacher Sentence
): When there is a large discrepancy between 
p
S
p_{S}
 and 
p
T
p_{T}
, the distilled model still outputs the sentence, suggesting the sentence is more consistent with the model assigning the higher likelihood. For example, if 
p
T
≫
p
S
p_{T}\gg p_{S}
 and distilled model nevertheless produces the sentence, it is more likely teacher-originated. 
Moreover, when 
p
T
≫
p
S
p_{

5 
Mixed-policy Distillation
Figure 7: 
The ratio between cut-off responses under different token lengths.
In the previous stages, we employed off-policy methods to approximate the teacher’s sequence-level distribution through high-quality data generation. Nevertheless, we find that the resulting student model still suffers from exposure bias 
(
41
)
: during training, the student is conditioned on the teacher’s prefix using teacher forcing, whereas at inference time, it must rely on its own autoregressive predictions, leading to a distribution mismatch.
To empirically investigate this phenomenon, we use the student model trained in the previous round (50K DAS sampling, T=0.6; see Table 
3
) to re-generate the training data within its own context, in order to examine whether the student model is overly reliant on the teacher’s context.
During inference, we set the maximum generation token length to 1.5 times the length of the teacher-provided solution, in order to compare the differences between the teacher’s reference response and the student’s self-generated counterpart. Figure 
7
 plots the cut-off rate of the student’s generated responses across different training-response lengths, where a higher cut-off rate indicates greater divergence between student and teacher behavior.
The results reveal that, even on the training data, the student still exhibits substantial deviations from the teacher, and this discrepancy becomes increasingly pronounced as the length of the training response grows. This observation confirms that training with teacher forcing under longer teacher prefixes exacerbates exposure bias.
To overcome these limitations, 
9
 present that on-policy data collection is an effective alternative method. Accordingly, we propose a mixed-policy distillation approach that synergistically combines off-policy and on-policy signals. Specifically, we first use the student model from the previous training round to re-generate responses for the training queries, and then identify instances that differ substantially from the teacher’s outputs, e.g., solutions that have been cut off in Figure 
7
. For these data points, we randomly cut off the solutions generated by the student and prompt the teacher to continue the generation, thereby enabling the teacher to provide targeted guidance on the student’s errors.
We present an ablation study of the proposed mixed-policy distillation in Table 
5
. As described above, we collect 7.7K mixed-policy samples, and 
