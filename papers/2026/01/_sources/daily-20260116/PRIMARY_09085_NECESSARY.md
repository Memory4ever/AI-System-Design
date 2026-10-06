# 2601.09085v1 necessary primary



## Appendix B1–5 common protocol

B.1
Model Configurations
Table
4
summarizes the architecture and parameter-efficient fine-tuning configurations for all three model scales.
Configuration
1.5B
7B
8B
Model name
DeepSeek-R1-Distill-Qwen
DeepSeek-R1-Distill-Llama
Architecture
Qwen
Qwen
Llama
Parameters
1.5B
7B
8B
Fine-tuning method
Full FT
LoRA
LoRA
LoRA rank (
r
r
)
–
64
64
LoRA alpha (
α
\alpha
)
–
128
128
LoRA dropout
–
0.05
0.05
LoRA target modules
–
q/k/v/o/gate/up/down proj
Precision
bfloat16
Attention
Flash Attention 2
Table 4:
Model architecture and PEFT configurations. All models are initialized from publicly available DeepSeek-R1 distilled checkpoints.
B.2
Common Training Hyperparameters
Table
5
lists the training hyperparameters shared across all methods and model scales.
Hyperparameter
Value
Optimization
Learning rate
1.0
×
10
−
6
1.0\times 10^{-6}
Optimizer
AdamW
LR scheduler
Cosine with min lr
Min LR ratio
0.1
Warmup ratio
0.1
Gradient clipping
1.0
Batch Configuration
Batch size per device
6
Gradient accumulation steps
8
Effective batch size
48
Training Steps
Max steps (GRPO/DR-GRPO/DAPO w/o DS)
500
Max steps (DAPO)
200
Logging steps
1
Sequence Lengths
Max prompt length
512 tokens
Max completion length
3584 tokens
Max model length
4608 tokens
Generation
Temperature
0.7
Number of generations (
G
G
)
6
System
Random seed
2025
Gradient checkpointing
True
Mixed precision
bfloat16
Table 5:
Common training hyperparameters across all methods and models.
B.3
vLLM Generation Configuration
For efficient parallel generation during training, we use vLLM
19
with the configuration shown in Table
6
.
Parameter
Value
vLLM device
1 Auto-assigned GPU
GPU memory utilization
0.7
Max model length
4608 tokens
Eager mode
Enabled
Prefix caching
Enabled
Dtype
bfloat16
Table 6:
vLLM configuration for efficient generation.
B.4
Reward Functions
Table
7
describes the reward functions used in our experiments.
Reward Type
Description
Accuracy
Binary reward (1.0 or 0.0) based on whether the extracted answer matches the gold answer
Format
Measures compliance with the required output format (presence of
<think>
and
<answer>
tags, proper
\boxed{}
usage)
Cosine
This is an enhanced variant of the Accuracy Reward. It assigns rewards to model completions by jointly considering solution correctness and completion length, where the length-based scaling follows a cosine schedule. For each completion, both the model output and the reference solution are parsed. Correctness is determined by comparing the parsed representations. The final reward is computed as a cosine function of the completion length normalized by a predefined maximum length, which favors shorter correct responses while imposing stronger penalties on short but incorrect ones
Table 7:
Description of reward functions used across different methods.
B.5
Method-Specific Configurations
Table
8
compares the specific hyperparameters and configurations for each training method.
Configuration
DAPO
GRPO
DR-GRPO
Algorithm-specific Parameters
Clipping bound (lower)
ϵ
low
\epsilon_{\text{low}}
0.2
–
–
Clipping bound (upper)
ϵ
high
\epsilon_{\text{high}}
0.28
–
–
KL penalty coefficient
β
\beta
–
0.04
0.04
Dynamic sampling
Applicable
N/A
N/A
Filter reward index
0 (accuracy)
–
–
Max generation batches
10
–
–
Reward Functions and Weights
Primary reward
Accuracy (1.0)
Format (1.0)
Format (1.0)
Secondary reward
Cosine (1.0)
Cosine (2.0)
Cosine (2.0)
Table 8:
Method-specific configurations for DAPO, GRPO, and DR-GRPO.


Source https://arxiv.org/html/2601.09085v1 . Only necessary method/evaluation and decisive direct counterevidence, not all appendices or proof population.

## Body offsets 13666–21414

3
Method
3.1
Background: GRPO
GRPO
33
is an effective reinforcement learning method for aligning language models with human preferences. Unlike traditional policy gradient methods, GRPO optimizes the policy by generating multiple responses and computing advantages within a group of responses.
Given a prompt
x
x
, GRPO generates
G
G
completions
{
y
1
,
y
2
,
…
,
y
G
}
\{y_{1},y_{2},\ldots,y_{G}\}
and computes a reward
r
⁡
(
y
i
)
r(y_{i})
for each completion using a reward model. The advantage for each completion is calculated as:
A
⁡
(
y
i
)
=
r
⁡
(
y
i
)
−
μ
G
σ
G
+
ϵ
A(y_{i})=\frac{r(y_{i})-\mu_{G}}{\sigma_{G}+\epsilon}
(1)
where
μ
G
\mu_{G}
and
σ
G
\sigma_{G}
are the mean and standard deviation of rewards within the group, and
ϵ
\epsilon
is a small constant for numerical stability.
The training objective combines the policy gradient with a KL divergence penalty to prevent the policy from deviating too far from a reference model:
ℒ
=
−
E
y
∼
π
θ
[
log
π
θ
(
y
|
x
)
⋅
A
(
y
)
−
β
⋅
D
KL
(
π
θ
|
|
π
ref
)
]
\mathcal{L}=-{E}_{y\sim\pi_{\theta}}\left[\log\pi_{\theta}(y|x)\cdot A(y)-\beta\cdot D_{\text{KL}}(\pi_{\theta}||\pi_{\text{ref}})\right]
(2)
where
π
θ
\pi_{\theta}
is the trainable policy,
π
ref
\pi_{\text{ref}}
is the reference policy, and
β
\beta
is the KL penalty coefficient.
While GRPO effectively leverages group-relative rewards, it does not explicitly account for diversity among the generated completions. High-reward responses that are semantically similar may dominate the training signal, leading to slower convergence.
3.2
MMR-based Reward Reweighting with
λ
\lambda
To address the lack of diversity consideration in vanilla GRPO, we propose a MMR inspired reward reweighting mechanism. MMR
6
was originally designed for document retrieval to balance relevance and diversity. We adapt this principle to reward shaping in GRPO. The complete algorithm is shown in Alg
1
.
Let
ℰ
⁡
(
y
i
)
∈
R
d
\mathcal{E}(y_{i})\in{R}^{d}
denote the embedding of completion
y
i
y_{i}
, obtained using a pre-trained sentence encoder. We define the cosine similarity between two completions as
s
⁡
(
y
i
,
y
j
)
=
ℰ
​
(
y
i
)
⊤
​
ℰ
​
(
y
j
)
s(y_{i},y_{j})=\mathcal{E}(y_{i})^{\top}\mathcal{E}(y_{j})
.
The MMR-based reward adjustment follows a greedy selection procedure. We maintain a set
𝒮
\mathcal{S}
of selected completions and iteratively add completions that maximize a diversity-weighted score:
score
​
(
y
i
)
=
λ
⋅
r
⁡
(
y
i
)
−
(
1
−
λ
)
⋅
max
y
j
∈
𝒮
⁡
s
⁡
(
y
i
,
y
j
)
\text{score}(y_{i})=\lambda\cdot r(y_{i})-(1-\lambda)\cdot\max_{y_{j}\in\mathcal{S}}s(y_{i},y_{j})
(3)
where
λ
∈
[
0
,
1
]
\lambda\in[0,1]
is a hyperparameter controlling the trade-off between reward quality (relevance) and diversity, and is commonly set to 0.7. When
λ
=
1
\lambda=1
, the method reduces to standard reward-based selection; when
λ
=
0
\lambda=0
, it purely maximizes diversity.
The algorithm proceeds as follows:
1.
Initialize
𝒮
=
∅
\mathcal{S}=\emptyset
and precompute the similarity matrix
S
∈
R
G
×
G
S\in{R}^{G\times G}
where
S
i
​
j
=
s
⁡
(
y
i
,
y
j
)
S_{ij}=s(y_{i},y_{j})
.
2.
Select the completion with the highest reward:
y
∗
=
arg
⁡
max
y
i
⁡
r
⁡
(
y
i
)
y^{*}=\arg\max_{y_{i}}r(y_{i})
, and add it to
𝒮
\mathcal{S}
.
3.
For each remaining completion, compute its adjusted score based on Equation
3
.
4.
Select the completion with the highest score, add it to
𝒮
\mathcal{S}
, and repeat until all completions are ranked.
5.
Use the adjusted scores as reweighted rewards
r
~
​
(
y
i
)
\tilde{r}(y_{i})
in the GRPO advantage calculation.
The adjusted rewards
r
~
​
(
y
i
)
\tilde{r}(y_{i})
replace the original rewards
r
⁡
(
y
i
)
r(y_{i})
when computing advantages in Equation
1
, encouraging the model to explore diverse high-quality solutions rather than repeatedly attending to similar responses.
3.3
Parameter-free MMR Reweighting with Adaptive
λ
\lambda
While the
λ
\lambda
-parameterized MMR reweighting is effective, it introduces an additional hyperparameter that requires tuning. To eliminate this dependency, we design an adaptive mechanism that automatically adjusts
λ
\lambda
based on the distribution of rewards within each group.
The key insight is that when rewards have high variance, diversity is less critical because the model already explores different quality regions. Conversely, when rewards are similar, diversity becomes more important to avoid mode collapse. We formalize this intuition using the sigmoid function applied to the reward standard deviation:
λ
adapt
=
σ
⁡
(
std
​
(
r
)
)
=
1
1
+
e
−
std
​
(
r
)
\lambda_{\text{adapt}}=\sigma(\text{std}(r))=\frac{1}{1+e^{-\text{std}(r)}}
(4)
where
std
​
(
r
)
\text{std}(r)
denotes the standard deviation of rewards
{
r
⁡
(
y
1
)
,
…
,
r
⁡
(
y
G
)
}
\{r(y_{1}),\ldots,r(y_{G})\}
within a group.
This adaptive
λ
\lambda
has two desirable properties:
•
Scale-invariant
: The sigmoid function automatically maps reward variability to a bounded range
(
0.5
,
1
)
(0.5,1)
, making it robust to different reward scales across tasks.
•
No hyperparameters
: The method requires no manual tuning, making it more general and easier to apply across different settings.
Empirically, when rewards are tightly concentrated (low
std
​
(
r
)
\text{std}(r)
),
λ
adapt
\lambda_{\text{adapt}}
decreases toward 0.5, increasing the diversity penalty. When rewards are widely spread (high
std
​
(
r
)
\text{std}(r)
),
λ
adapt
\lambda_{\text{adapt}}
approaches 1, prioritizing reward quality. This adaptive behavior provides a principled way to encourage diversity without sacrificing reward maximization when the model already exhibits sufficient exploration.
The parameter-free MMR reweighting follows the same greedy procedure as described in Section 3.2, but with
λ
\lambda
replaced by
λ
adapt
\lambda_{\text{adapt}}
computed automatically for each group of completions. This allows the model to dynamically balance relevance and diversity based on the reward landscape of each group.
All the experiments in this paper are conducted with
λ
adapt
\lambda_{\text{adapt}}
.
Algorithm 1
MMR-based Reward Reweighting
0:
Rewards
{
r
⁡
(
y
1
)
,
…
,
r
⁡
(
y
G
)
}
\{r(y_{1}),\ldots,r(y_{G})\}
, L2-normalized embeddings
{
ℰ
⁡
(
y
1
)
,
…
,
ℰ
⁡
(
y
G
)
}
\{\mathcal{E}(y_{1}),\ldots,\mathcal{E}(y_{G})\}
0:
Reweighted rewards
{
r
~
​
(
y
1
)
,
…
,
r
~
​
(
y
G
)
}
\{\tilde{r}(y_{1}),\ldots,\tilde{r}(y_{G})\}
1:
Compute adaptive
λ
\lambda
:
λ
adapt
←
σ
⁡
(
std
​
(
r
)
)
=
1
1
+
e
−
std
​
(
r
)
\lambda_{\text{adapt}}\leftarrow\sigma(\text{std}(r))=\frac{1}{1+e^{-\text{std}(r)}}
2:
Compute similarity matrix:
S
i
​
j
←
ℰ
​
(
y
i
)
⊤
​
ℰ
​
(
y
j
)
S_{ij}\leftarrow\mathcal{E}(y_{i})^{\top}\mathcal{E}(y_{j})
for all
i
,
j
∈
[
G
]
i,j\in[G]
at once.
3:
Initialize
𝒮
←
∅
\mathcal{S}\leftarrow\emptyset
4:
i
∗
←
arg
⁡
max
i
⁡
r
⁡
(
y
i
)
i^{*}\leftarrow\arg\max_{i}r(y_{i})
5:
Add
i
∗
i^{*}
to
𝒮
\mathcal{S}
and set
r
~
​
(
y
i
∗
)
←
r
⁡
(
y
i
∗
)
\tilde{r}(y_{i^{*}})\leftarrow r(y_{i^{*}})
6:
for
t
=
1
t=1
to
G
−
1
G-1
do
7:
for
each
i
∉
𝒮
i\notin\mathcal{S}
do
8:
best_sim
i
←
max
j
∈
𝒮
⁡
S
i
​
j
\text{best\_sim}_{i}\leftarrow\max_{j\in\mathcal{S}}S_{ij}\
9:
end
for
10:
for
each
i
∉
𝒮
i\notin\mathcal{S}
do
11:
score
​
(
y
i
)
←
λ
adapt
⋅
r
⁡
(
y
i
)
−
(
1
−
λ
adapt
)
⋅
best_sim
i
\text{score}(y_{i})\leftarrow\lambda_{\text{adapt}}\cdot r(y_{i})-(1-\lambda_{\text{adapt}})\cdot\text{best\_sim}_{i}
12:
end
for
13:
i
∗
←
arg
⁡
max
i
∉
𝒮
​
score
​
(
y
i
)
i^{*}\leftarrow\arg\max_{i\notin\mathcal{S}}\text{score}(y_{i})
14:
Add
i
∗
i^{*}
to
𝒮
\mathcal{S}
and set
r
~
​
(
y
i
∗
)
←
score
​
(
y
i
∗
)
\tilde{r}(y_{i^{*}})\leftarrow\text{score}(y_{i^{*}})
15:
end
for
16:
return
{
r
~
​
(
y
1
)
,
…
,
r
~
​
(
y
G
)
}
\{\tilde{r}(y_{1}),\ldots,\tilde{r}(y_{G})\}


## Body offsets 21414–28950

4
Experimental Settings
4.1
Datasets
We evaluate our approach on five widely used mathematical reasoning benchmarks: AIME 2024, MATH 500
15
, AMC 2023, Minerva
20
, and Olympiad Bench
14
.
These benchmarks span competition-style and curriculum-aligned problems with varying levels of difficulty and reasoning complexity, providing a comprehensive evaluation to assess mathematical problem-solving and multi-step reasoning ability. Additional details about each benchmark are provided in Appendix
A.1
.
For training, we use the
knoveleng/open-rs
dataset
9
, which consists of mathematical reasoning problems paired with high-quality step-by-step solutions.
The dataset covers a broad range of mathematical topics and difficulty levels and is well-suited for training models to generate coherent reasoning chains. Further details about the training data are described in Appendix
A.2
.
4.2
Evaluation Metrics
Following standard practice in evaluation from previous works
10
;
40
;
21
, we adopt the
pass@k
metric to measure the probability that at least one correct solution exists among
k
k
generated candidates from
n
n
total samples. Formally, given
n
=
16
n=16
independently generated completions per problem, pass@k is computed as:
pass@k
=
E
⁡
[
1
−
(
n
−
c
k
)
(
n
k
)
]
\text{pass@k}={E}\left[1-\frac{\binom{n-c}{k}}{\binom{n}{k}}\right]
(5)
where
c
c
is the number of correct solutions among the
n
n
samples. We primarily report
pass@1
with
n
=
16
n=16
. When
k
=
1
k=1
, this metric is equivalent to
avg@16
, which is the fraction of correct solutions among the 16 sampled completions.. Evaluations are done using
lighteval
1
1
1
https://huggingface.co/docs/lighteval
for reproducibility and fair comparison.
4.3
Models
We conduct experiments with three model scales from two different model families: DeepSeek-R1-Distill-Qwen-1.5B
2
2
2
https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
, DeepSeek-R1-Distill-Qwen-7B
3
3
3
https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
, and DeepSeek-R1-Distill-Llama-8B
4
4
4
https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B
.
All models are initialized from publicly available checkpoints from Huggingface. Larger models (7B and 8B) employ LoRA
16
for parameter-efficient fine-tuning (see Appendix
B.1
for details). For embedding extraction, we use
jina-embeddings-v2-small-en
5
5
5
https://huggingface.co/jinaai/jina-embeddings-v2-small-en
, which provide strong semantic representations while maintaining computational efficiency.
Size
Method/Model
AIME 24
MATH-500
AMC 23
Minerva
OlympiadBench
Average
Peak
Step
Time
(hrs)
Time per
Step(s)
1.5B
DS-Distill-Qwen-1.5B
0.288
0.828
0.629
0.265
0.433
0.489
-
-
-
GRPO
0.338
0.846
0.730
0.296
0.528
0.547
100
4.08
147
MMR-GRPO
0.325
0.849
0.739
0.302
0.528
0.549
100
4.13
149
DR-GRPO
0.335
0.844
0.744
0.297
0.523
0.549
150
6.11
147
MMR-DR-GRPO
0.323
0.851
0.738
0.303
0.530
0.549
100
4.13
149
DAPO
0.331
0.851
0.755
0.304
0.541
0.556
110
25.53
836
DAPO-No-DS
0.348
0.855
0.744
0.298
0.529
0.555
200
8.93
161
MMR-DAPO-No-DS
0.331
0.856
0.730
0.295
0.527
0.548
170
7.72
163
7B
DS-Distill-Qwen-7B
0.560
0.923
0.825
0.380
0.568
0.651
-
-
-
GRPO
0.554
0.940
0.917
0.418
0.671
0.700
350
28.28
291
MMR-GRPO
0.560
0.940
0.916
0.409
0.673
0.700
150
12.22
293
DR-GRPO
0.565
0.939
0.914
0.420
0.672
0.702
300
24.30
292
MMR-DR-GRPO
0.565
0.942
0.905
0.412
0.673
0.699
50
4.11
296
DAPO
0.558
0.940
0.914
0.418
0.671
0.700
90
33.15
1326
DAPO-No-DS
0.569
0.939
0.905
0.420
0.674
0.701
200
16.17
291
MMR-DAPO-No-DS
0.567
0.941
0.920
0.417
0.672
0.703
100
8.52
307
8B
DS-Distill-Llama-8B
0.506
0.896
0.815
0.295
0.541
0.611
-
-
-
GRPO
0.465
0.889
0.897
0.355
0.626
0.646
350
32.22
331
MMR-GRPO
0.475
0.882
0.897
0.350
0.623
0.645
50
4.62
333
DR-GRPO
0.488
0.895
0.881
0.351
0.632
0.649
300
27.72
333
MMR-DR-GRPO
0.485
0.893
0.886
0.346
0.630
0.648
100
9.36
337
DAPO
0.504
0.889
0.889
0.351
0.631
0.653
160
93.75
2109
DAPO-No-DS
0.483
0.890
0.878
0.346
0.628
0.645
250
23.02
331
MMR-DAPO-No-DS
0.477
0.888
0.878
0.353
0.631
0.646
180
17.40
348
Average Training Step Saved:
47.9%
Average Training Time (hrs) Saved:
70.2%
Table 1:
Peak performance (pass@1) comparisons across model sizes (1.5B, 7B and 8B models) and training methods (GRPO, DR-GRPO and DAPO), before and after MMR reweighting. All metrics represent the best checkpoint for each configuration. The Peak Step indicates the training step where optimal average performance is achieved. Training time is logged based on wall-clock measurements on 2
×
\times
NVIDIA H100 80GB GPUs. MMR reweighting consistently achieves comparable or better performance while requiring fewer training steps and less time, translating to substantial computational savings. DS is short for DeepSeek-R1.
4.4
Training Methods
We experiment with three GRPO-style reinforcement learning methods for aligning language models with mathematical reasoning objectives:
•
GRPO
33
applies PPO-style policy gradient optimization
31
by generating multiple completions per prompt and computes advantages relative to group statistics, avoiding the need for a separate value network. We compare vanilla GRPO and MMR-GRPO, with both methods trained for 500 steps and evaluated every 50 steps.
•
DAPO
40
introduces dynamic sampling, a technique that reduces training steps by discarding low-variance sample sets and regenerating samples during training. However, dynamic sampling incurs significant per-step computational overhead
21
;
23
. To investigate whether MMR can serve as a more efficient alternative to dynamic sampling, we evaluate three DAPO configurations:
–
DAPO
: Vanilla DAPO with dynamic sampling enabled, trained for 200 steps with evaluation after every 10 steps. The reduced training horizon is due to dynamic sampling’s rapid convergence as well as its prohibitive per-step cost.
–
DAPO-No-DS
: DAPO with dynamic sampling disabled, providing a controlled baseline without dynamic sampling. Trained for 500 steps with evaluation first after every 10 steps (0-200) and then after every 50 steps (200-500).
–
MMR-DAPO-No-DS
: DAPO with MMR reweighting instead of dynamic sampling, using the same training and evaluation schedule as DAPO-No-DS. In this configuration, we do not discard any low-variance sample group, but we consistently reweigh rewards within each group of generated samples.
This experimental design allows us to directly compare MMR and Dynamic Sampling as alternative training efficiency techniques while isolating their effects from DAPO’s other algorithmic improvements.
•
DR-GRPO
24
extends GRPO with de-biased optimization that reduce response-level length bias and question-level difficulty bias. We compare vanilla DR-GRPO and MMR-DR-GRPO, with both methods trained for 500 steps and evaluated every 50 steps.
Common training hyperparameters and other model details are provided in Appendix
B
.
5
Results and Discussions
5.1
MMR Impacts on Training Efficiency
Figure 2:
Performance across training steps for 7B models across all three training methods (DAPO, GRPO, DR-GRPO). MMR variants consistently achieve faster convergence and reach peak performance with fewer training steps.
Training Steps Reduction
Table
1
demonstrates that MMR-based reward reweighting consistently reduces the number of training steps required to reach peak performance across all methods and model scales. For GRPO, MMR achieves comparable performance while reducing training steps from 350 to 150 steps for the 7B model (57% reduction) and from 350 to 50 steps for the 8B

## Body offsets 60255–60700

B.7
Computational Resources
All training experiments were conducted on 2xNVIDIA H100 80GB GPUs. All evaluation experiments were conducted on 1xNVIDIA A100 40GB GPU.
Appendix C
Additional Results
C.1
Training Convergence for 8B and 1.5B Models
Figures
4
and
5
present the training convergence patterns for 8B and 1.5B models, respectively, complementing the 7B results shown in the main text (Figure
2
). The convergence patterns observed in thes
