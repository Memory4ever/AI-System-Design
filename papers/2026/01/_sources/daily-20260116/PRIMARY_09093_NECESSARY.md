# 2601.09093v1 necessary primary



## A1/A2 and B1 minimum scorer/decoding setup

A.1
Training Parameters
The training hyper-parameters used in the training process of step scorer are listed in Tab.
4
.
Parameter
Value
MLP Structure
Input
→
\rightarrow
512 (ReLU)
→
\rightarrow
1
Batch Size
128
Max Epochs
20
Early Stopping Patience
5
Learning Rate
1
×
10
−
4
1\times 10^{-4}
Weight Decay
1
×
10
−
5
1\times 10^{-5}
Optimizer
Adam
Loss Function
BCEWithLogitsLoss
Table 4:
Training Parameters
The input dimension corresponds to the hidden state size of each LLM: 2560 (Qwen3-4B-Thinking-2507), 4096 (DeepSeek-R1-0528-Qwen3-8B), and 5120 (Phi-4-reasoning-plus).
A.2
Training Dataset
For training the step scorer, we constructed a dataset comprising mathematical problems from HMMT 2012–2023
hmmt2012_2023
. We specifically utilized problems from the February competition in Algebra, Combinatorics, and Geometry, which provide diverse and challenging examples for learning hidden state representations indicative of reasoning quality.
We sampled 64 solutions from the corresponding LLM for each problem and verified the correctness of their final answers using a deterministic rule-based verifier adapted from the Qwen2.5-Math project
yang2024qwen2
. The verifier normalizes answer strings and checks correctness against the ground truth via numeric matching and SymPy-based symbolic equivalence. We then randomly selected 5,000 correct and 5,000 incorrect traces to form a balanced training set for each LLM.
Appendix 

B.1
Sampling Parameters
The sampling parameters used for each model across all experiments are listed in Tab.
5
. Temperature, top-p, top-k, and maximum generation length remain fixed for all methods. Here, Qwen3-4B refers to Qwen3-4B-Thinking-2507 and Deepseek-8B refers to DeepSeek-R1-0528-Qwen3-8B.
Model
Temperature
Top-
p
p
Top-
k
k
Max gen len
Qwen3-4B
0.6
0.95
20
64k
DeepSeek-8B
0.6
0.95
20
64k
Phi-4-reasoning-plus
0.8
0.95
50
32k
Table 5:
Sampling Parameters


Source https://arxiv.org/html/2601.09093v1 . Only necessary method/evaluation and decisive direct counterevidence, not all appendices or proof population.

## Body offsets 15102–23913

4
STEP
Figure 3:
Overview of the STEP framework. The step-level scoring module extracts hidden states at step boundaries and uses a trained step scorer to compute step-level scores, which are averaged to obtain trace-level scores. The KV-cache monitor triggers pruning when GPU memory is saturated, removing the trace with the lowest score and releasing its KV cache to prevent queuing delays.
In this section, we progressively construct STEP. Designing an effective pruning method involves two key questions:
which reasoning traces to prune
and
when pruning should be triggered
. As illustrated in the overview in Fig.
3
, STEP addresses the first question with a step scorer that evaluates every step during generation, and the second with a KV cache–aware monitoring mechanism. We next describe each component in detail by systematically answering these two questions.
4.1
Step Scorer
As discussed in the Section
3
, we train a step scorer that leverages hidden-state representations to assess reasoning quality at each step.
Step Representation
Following common practice
yang2025speculative
, we extract the reasoning content between “
<think>
” and “
</think>
”, and segment it into
N
N
reasoning steps using “
\n\n
” as the delimiter. Then a trace is defined as:
t
=
(
s
1
,
s
2
,
…
,
s
N
)
t=(s_{1},s_{2},\ldots,s_{N})
. For each step
s
n
s_{n}
, we use the last-layer hidden state of step-end token
1
1
1
It refers to any token whose text contains ”
\n\n
”.
𝐡
n
\mathbf{h}_{n}
(
𝐡
n
∈
ℝ
d
\mathbf{h}_{n}\in\mathbb{R}^{d}
where
d
d
is the hidden dimension of LLM.) as input to the scorer, as it accumulates contextual information from all previous reasoning steps in the trace.
Label Construction
As supervision for the step scorer, we propagate the trace-level correctness label
y
∈
{
0
,
1
}
y\in\{0,1\}
to all steps within the trace as pseudo-labels for simplicity, as fine-grained step-level annotation is costly to obtain. Specifically,
y
~
n
=
y
,
∀
n
∈
{
1
,
…
,
N
}
,
\tilde{y}_{n}=y,\quad\forall n\in\{1,\ldots,N\},
where
y
=
1
y=1
indicates a correct trace and
y
=
0
y=0
an incorrect one. For training data curation, we balance the number of correct and incorrect traces, while including all steps from each trace in the training set. Details of the training data are provided in Section
5.1
.
Model Architecture
The step scorer
f
θ
f_{\theta}
is a two-layer MLP, which we find sufficient for capturing quality signals from hidden states. It maps
𝐡
n
\mathbf{h}_{n}
to a correctness probability score
y
^
n
\hat{y}_{n}
:
y
^
n
=
f
θ
​
(
𝐡
n
)
=
σ
⁡
(
𝐖
2
​
ReLU
​
(
𝐖
1
​
𝐡
n
+
𝐛
1
)
+
b
2
)
,
\hat{y}_{n}=f_{\theta}(\mathbf{h}_{n})=\sigma\!\Big(\mathbf{W}_{2}\,\mathrm{ReLU}(\mathbf{W}_{1}\mathbf{h}_{n}+\mathbf{b}_{1})+b_{2}\Big),
where
𝐖
1
∈
ℝ
m
×
d
\mathbf{W}_{1}\in\mathbb{R}^{m\times d}
,
𝐖
2
∈
ℝ
1
×
m
\mathbf{W}_{2}\in\mathbb{R}^{1\times m}
,
𝐛
1
∈
ℝ
m
\mathbf{b}_{1}\in\mathbb{R}^{m}
,
and
b
2
∈
ℝ
b_{2}\in\mathbb{R}
are trainable parameters,
with
m
m
denoting the hidden dimension of the MLP. The function
σ
⁡
(
⋅
)
\sigma(\cdot)
denotes the sigmoid activation.
Training Objective
We train the step scorer using a weighted binary cross-entropy loss:
ℒ
=
−
1
N
∑
n
=
1
N
(
α
y
~
n
log
y
^
n
+
(
1
−
y
~
n
)
log
(
1
−
y
^
n
)
)
,
\mathcal{L}=-\frac{1}{N}\sum_{n=1}^{N}\Big(\alpha\tilde{y}_{n}\log\hat{y}_{n}+(1-\tilde{y}_{n})\log(1-\hat{y}_{n})\Big),
where
α
=
K
−
/
K
+
\alpha=K^{-}/K^{+}
is the ratio of negative to positive samples in the training data. This weighting compensates for the imbalance at the step level, as incorrect traces tend to be longer and thus generate more negative step instances, even when the dataset is balanced at the trace level.
4.2
Memory Constraint as Trigger
The timing of pruning is critical for improving generation efficiency. Prior approaches typically rely on predefined confidence thresholds
fu2025deepthinkconfidence
or fixed wall-clock schedules
hong-etal-2025-slim
to trigger pruning, without considering the behavior of inference system. While these methods reduce generation time by terminating unpromising traces that may produce longer sequences, they overlook a more fundamental bottleneck revealed in Section
3
: the excessive waiting time caused by GPU memory constraints. As a result, existing methods fail to address the dominant source of inefficiency during inference.
To overcome this limitation, we propose a memory-triggered pruning mechanism. Whenever GPU memory is full, and the KV cache for the next decoding step cannot be scheduled, we immediately prune the trace with the lowest trace level score and release its KV cache. This design completely eliminates waiting queues, thereby avoiding prolonged suspension and repeated resumption of traces. Moreover, our mechanism is free of additional hyperparameters, making it simple and robust in practice.
Methods
AIME-25
HMMT-24
HMMT-25
GPQA-D
Acc.
↑
\uparrow
Token
↓
\downarrow
Lat.
↓
\downarrow
Acc.
↑
\uparrow
Token
↓
\downarrow
Lat.
↓
\downarrow
Acc.
↑
\uparrow
Token
↓
\downarrow
Lat.
↓
\downarrow
Acc.
↑
\uparrow
Token
↓
\downarrow
Lat.
↓
\downarrow
Qwen3-4B-Thinking-2507
CoT
81.3
22.7
145
47.5
29.8
194
55.8
26.8
174
65.8
8.9
54
SC
86.7
1454.3
1430
50.8
1905.5
2277
65.0
1714.3
1833
68.1
569.1
252
Slim-SC
86.7
957.5
767
50.0
1002.6
1025
65.8
930.8
848
64.9
414.7
236
DeepConf
90.0
841.5
933
56.7
1069.4
1373
68.3
1037.0
1253
67.6
379.1
257
STEP
88.3
1131.5
675
58.3
1149.3
979
70.0
1109.8
732
68.5
539.6
223
DeepSeek-R1-0528-Qwen3-8B
CoT
77.5
26.4
204
50.0
33.1
307
60.4
29.9
256
62.3
11.4
81
SC
83.3
1691.0
2259
55.8
2116.2
3102
70.0
1913.0
2680
67.1
729.8
484
Slim-SC
83.3
1519.9
1960
55.0
1830.7
2789
69.2
1733.2
2388
66.2
564.1
424
DeepConf
81.7
916.4
1475
56.7
1084.2
1791
71.7
993.1
1540
68.7
419.8
409
STEP
85.0
989.7
891
59.2
1105.8
1116
73.3
1087.2
1006
68.2
635.7
378
Phi-4-reasoning-plus
CoT
78.3
16.0
194
51.7
21.2
294
58.6
21.7
246
69.5
11.9
105
SC
86.7
1026.7
1687
56.7
1356.4
2405
75.0
1389.8
2529
76.3
762.5
1081
Slim-SC
85.0
875.8
1354
55.0
1178.9
1918
74.2
1120.4
1690
72.3
560.6
655
DeepConf
85.8
537.2
1165
57.5
714.9
1523
75.0
755.6
1770
74.8
401.9
1285
STEP
87.5
503.4
519
58.3
579.8
630
75.8
585.2
643
76.7
441.5
445
Table 1:
Main experimental results comparing our method with baseline methods (CoT, SC, Slim-SC, and DeepConf) on various models and benchmarks. Evaluation metrics include accuracy (%), average token usage (
×
10
3
\times 10^{3}
), and inference latency (s).
4.3
Pruning with STEP
With the building blocks for
when
and
how
to prune in place, we now describe the overall algorithm. Given an input prompt, we generate
T
T
reasoning traces in parallel. During generation, whenever a trace
t
t
produces a step-end token that signals the end of a reasoning step, we compute a step-level score
y
^
n
t
\hat{y}^{t}_{n}
by applying the step scorer to the corresponding hidden state. The trace-level score is then defined as the mean of all step-level scores of this trace accumulated so far:
s
​
c
​
o
​
r
​
e
t
=
1
n
​
∑
i
=
1
n
y
^
i
t
,
score_{t}=\frac{1}{n}\sum_{i=1}^{n}\hat{y}^{t}_{i},
where
n
n
denotes the number of reasoning steps currently generated in trace
t
t
. Compared to relying solely on the score of the most recent step, this aggregated score provides a more stable estimate of trace quality by capturing the evolution of the reasoning process across steps. In particular, it mitigates the variance of individual step scores and reflects whether a trace consistently follows a coherent reasoning trajectory.
During generation, whenever GPU memory becomes full due to KV cache usage, we prune the trace with the lowest trace-level score, thereby releasing memory for more promising traces. Once all reasoning traces have either completed generation or been pruned, we collect the outputs of the completed traces and perform weighted voting based on their final trace-level scores to aggregate the final answer. The pseudo-code for STEP is shown in Algorithm
1
.
Input:
Problem
P
P
, step scorer
f
⁡
(
⋅
)
f(\cdot)
, trace budget
N
N
Output:
Final answer
a
^
\hat{a}
𝒯
←
InitTraces
​
(
P
,
N
)
\mathcal{T}\leftarrow\textsc{InitTraces}(P,N)
while
𝒯
≠
∅
\mathcal{T}\neq\emptyset
do
foreach
trace
t
∈
𝒯
t\in\mathcal{T}
do
(
x
,
h
)
←
NextToken
​
(
t
)
(x,h)\leftarrow\textsc{NextToken}(t)
;
if
"
\n\n
" in
x
x
then
y
^
←
f
⁡
(
h
)
\hat{y}\leftarrow f(h)
;
Update
s
​
c
​
o
​
r
​
e
t
score_{t}
with
y
^
\hat{y}
if
GPUMemoryFull
then
t
⋆
←
arg
⁡
min
t
∈
𝒯
​
s
​
c
​
o
​
r
​
e
t
t^{\star}\leftarrow\arg\min_{t\in\mathcal{T}}\;score_{t}
;
ReleaseKVCache
(
t
⋆
)
(t^{\star})
;
𝒯
←
𝒯
∖
{
t
⋆
}
\mathcal{T}\leftarrow\mathcal{T}\setminus\{t^{\star}\}
;
a
^
←
WeightedVote
​
(
𝒯
,
{
s
​
c
​
o
​
r
​
e
t
}
)
\hat{a}\leftarrow\textsc{WeightedVote}(\mathcal{T},\{score_{t}\})
;
return
a
^
\hat{a}
;
Algorithm 1
STEP


## Body offsets 23913–27230

5
Experiment
In this section, we conduct comprehensive experiments to evaluate the effectiveness of our method, demonstrating improvements in both reasoning quality and generation efficiency. We further analyze its performance under different settings and investigate the underlying factors contributing to these improvements.
5.1
Experiment Setup
Models
We evaluate on three reasoning LLMs: Qwen3-4B-Thinking-2507
yang2025qwen3technicalreport
, DeepSeek-R1-0528-Qwen3-8B
deepseekai2025deepseekr1incentivizingreasoningcapability
, and Phi-4-reasoning-plus(14B)
abdin2025phi4reasoningtechnicalreport
. These models are selected for their strong mathematical reasoning and long-chain-of-thought capabilities, and are fully open-sourced to ensure reproducibility.
Benchmarks
We evaluate on four challenging datasets: AIME-25
aops2025aime
, HMMT-24
hmmt_feb_2024_archive
, HMMT-25
hmmt_feb_2025_archive
, and GPQA-Diamond
rein2024gpqa
. The first three comprise high-difficulty mathematical competition problems, while GPQA consists of graduate-level reasoning tasks in general science.
Baselines
We compare our method against the following baseline methods:
•
Chain-of-Thought (CoT)
wei2022chain
uses standard CoT prompting, where the model generates a single reasoning trajectory that directly leads to the final answer.
•
Self-Consistency (SC)
wang2022self
generates N independent reasoning traces and determines the final answer by majority voting on the predicted solutions.
•
Slim-SC
hong-etal-2025-slim
proposes a step-wise thought pruning strategy for self-consistency: it detects and removes redundant reasoning chains by measuring inter-chain similarity at the thought level, reducing latency while maintaining accuracy.
•
DeepConf
fu2025deepthinkconfidence
utilizes the model’s internal confidence signals to monitor the quality of each reasoning trace during generation, allowing dynamic termination of unpromising traces. The final answer is decided by confidence-weighted voting.
Implementation Details
To train the step scorer, we curated a dataset of mathematical problems from HMMT 2012–2023
hmmt2012_2023
, which provide diverse examples for learning hidden state representations indicative of reasoning quality. We sampled 64 solutions from the target model for each problem and verified their correctness using a deterministic rule-based verifier. We then randomly selected 5,000 correct and 5,000 incorrect traces to form a balanced training set. More details are shown in Appendix
A
.
We evaluate all methods under the sampling budget of
N
=
64
N=64
. For Slim-SC, we apply random pruning with a similarity threshold of 0.95 as recommended in the original work
hong-etal-2025-slim
. For DeepConf, we use the online variant (DeepConf-low) with
N
init
=
16
N_{\text{init}}=16
traces for offline warmup, then generate the remaining 48 traces with early termination for those falling below the top-10% confidence threshold.
All experiments are conducted using a modified vLLM
kwon2023efficient
framework with our pruning algorithm on a single 96GB NVIDIA GH200 GPU.
More detailed settings are provided in the Appendix
B
.
Figure 4:
Latency scaling comparison between STEP and baseline methods on AIME-25 and HMMT-25 using Qwen3-4B-Thinking-2507 and DeepSeek-R1-0528-Qwen3-8B.
5.2
Main Results
Tab.
1
pre

## Body offsets 32567–35259

5.3.3
Profiling Acceleration by Pruning
The acceleration of STEP stems from two complementary factors: reducing the number of generated tokens and eliminating waiting time during generation. Token counts are reported in Tab.
1
. We further conduct experiments, profiling the end-to-end generation time breakdown of DeepSeek-R1-0528-Qwen3-8B on HMMT25 with 64 traces, and results are reported in Tab.
2
.
DeepConf consists of two consecutive stages with N=16 in warmup and N=48 in pruning stage, and we report them separately. We observe that all pruning methods decrease generated tokens compared with SC, and lead to lower decoding time in Tab.
2
. Beyond token-level efficiency, the key distinction lies in how to handle waiting time. DeepConf and Slim-SC reduce waiting time compared to SC, since pruning naturally alleviates GPU memory pressure, thus shortening the waiting queue. However, their pruning decisions are not explicitly tied to GPU memory usage, and therefore cannot fully eliminate the waiting time. In contrast, our method completely removes waiting queue by triggering pruning in a memory-aware manner, resulting in the lowest end-to-end generation latency.
Method
SC
DeepConf
Slim-SC
STEP
Stage
Warmup
Prune
Wait
1526
69
194
1155
0
Decode
1256
680
726
983
1024
Table 2:
Waiting time and decoding time (in seconds) comparison across different methods.
Taken together, these results demonstrate that while reducing generated tokens lowers decoding overhead, explicitly eliminating waiting time is critical for further accelerating end-to-end generation.
5.3.4
GPU memory sensitivity
STEP triggers pruning when KV cache saturates GPU memory. Since smaller GPU memory budgets lead to earlier pruning, it is important to examine the robustness of our method under different memory constraints. To this end, we conduct a sensitivity analysis by varying the maximum GPU memory utilization from 0.5 to 0.9, on a 96GB NVIDIA GH200 GPU. We report results on the HMMT-25 using DeepSeek-R1-0528-Qwen3-8B, sampling 32 reasoning traces per problem. The results are summarized in Tab.
3
.
Memory
0.5
0.6
0.7
0.8
0.9
Accuracy
70.0
69.1
70.0
68.3
73.3
Table 3:
Accuracy result under different GPU memory utilization settings.
We observe that the accuracy remains stable across different memory budgets (70.1 ± 1.8%). Even under smaller GPU memory budgets, where pruning is triggered earlier, our method consistently achieves strong performance. This observation is consistent with the findings in Section
5.3.2
, which show that our scorer is able to identify promising reasoning traces at an early stage of generation. These results suggest that our method is insensitive to GPU memory.


## Body offsets 40340–41540

D
Additional Computational Overhead
The step scorer is implemented as an auxiliary MLP, which inevitably introduces additional computation. Since this MLP is invoked at every reasoning step, we quantify its overhead by comparing the per-step computation cost of the scorer with that of the underlying LLM.
We approximate the FLOPs of one forward generation step of the LLM as
2
​
N
2N
, where
N
N
denotes the number of non-embedding parameters
kaplan2020scaling
. The computation cost of the step-level MLP is
2
​
m
​
(
d
+
1
)
2m(d+1)
, where
m
m
is the hidden dimension of the MLP and
d
d
is the hidden dimension of the LLM. The relative overhead per step is therefore
2
​
m
​
(
d
+
1
)
2
​
N
∗
t
,
\frac{2m(d+1)}{2N*t},
where
t
t
is the average tokens per step. In practice, we set
m
=
512
m=512
,
d
d
is on the order of
10
3
10^{3}
,
N
N
is on the order of billions, and
t
t
is around
10
2
10^{2}
. Under these settings, the resulting ratio is below
10
−
6
10^{-6}
, indicating that the computational overhead introduced by the step scorer is negligible.
Appendix E
Trace-level Score Dynamics
We visualize trace-level score dynamics on AIME-25 for Qwen3-4B-Thinking-2507 and DeepSeek-R1-0528-Qwen

## Body offsets 35259–36080

6
Conclusion
In this work, we introduce STEP, a method that combines hidden-state-based trace evaluation with GPU-memory-aware pruning for efficient test-time scaling. By leveraging early reasoning signals and system-level optimization, STEP achieves 45%–70% latency reduction while improving accuracy, demonstrating the potential of efficient parallel scaling for complex reasoning tasks.
Limitations
Our work has two primary limitations. First, the step scorer relies on pseudo-labels generated by propagating trace-level correctness to individual steps. Such weak supervision is inherently noisy and may compromise robustness under domain shift or when traces contain steps of varying quality. Second, the most significant latency improvements depend on memory-triggered pruning, which is tightly coupled to the servin
