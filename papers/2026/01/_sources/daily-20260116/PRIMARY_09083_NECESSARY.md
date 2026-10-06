# 2601.09083v1 necessary primary

Source https://arxiv.org/html/2601.09083v1 . Only necessary method/evaluation and decisive direct counterevidence, not all appendices or proof population.

## Body offsets 9152–15890

3
Method
RL training in brief.
We consider standard on-policy reinforcement learning for language models. Given a prompt
x
1
:
m
x_{1:m}
and a policy
π
θ
\pi_{\theta}
, the learner samples one or more continuations
y
y
by autoregressively decoding from
π
θ
(
⋅
∣
x
1
:
m
)
\pi_{\theta}(\,\cdot\mid x_{1:m})
. A task-specific reward
r
⁡
(
x
,
y
)
r(x,y)
is computed (e.g., program execution, self-consistency or preference modeling), and gradients are formed from advantages
A
⁡
(
x
,
y
)
A(x,y)
under a clipped policy-gradient objective (PPO-style) or its multi-sample variants such as GRPO and DAPO. Training alternates between a
rollout
phase that generates
K
K
samples per prompt and an
update
phase that fits
π
θ
\pi_{\theta}
on the on-policy batch.
Per
-
prompt rollout cache using tree-structured cache.
SRT accelerates these on-policy rollouts by maintaining, for each prompt
p
p
, a cache of previously seen token subsequences organized as a tree-structured cache
𝒯
p
\mathcal{T}_{p}
. Paths in
𝒯
p
\mathcal{T}_{p}
therefore compactly index
all
substrings that have occurred in earlier generations for the same prompt, including from prior policy checkpoints. Each node corresponds to a context (a token subsequence) and stores outgoing edges labeled by next tokens, together with simple frequency statistics:
count
​
(
u
)
\texttt{count}(u)
for a node
u
u
recording its frequency in previous rollouts. This structure is purely model-free and can be stored in CPU memory; it can be updated online in amortized linear time as new tokens arrive.
Figure 3
:
Given the matched prefix “the cat”, we choose its suffix “sit on the mat” with highest score as draft tokens. Leaf nodes show the number of times each suffix appeared in cached rollouts, while non-leaf nodes contain the sum of their children’s counts.
Speculative Rollout with Tree-Structured Cache.
During rollout for prompt
p
p
, suppose we have already produced a partial continuation
y
1
:
t
y_{1:t}
. We locate the longest suffix of
y
1
:
t
y_{1:t}
that appears in
𝒯
p
\mathcal{T}_{p}
by walking through the tree from the root along tokens
y
t
−
q
+
1
:
t
y_{t-q+1:t}
; if the walk fails, we revert to standard decoding for one step and try again. Once a match of length
q
q
is found at node
u
q
u_{q}
, SRT assembles a set
𝒯
^
\widehat{\mathcal{T}}
of draft tokens by greedily adding descendants of
u
q
u_{q}
that are most likely to be accepted. We rank an edge to child
v
v
by empirical conditional
C
⁡
(
v
)
=
count
​
(
v
)
∑
w
∈
children
​
(
parent
​
(
v
)
)
count
​
(
w
)
,
C(v)\;=\;\frac{\texttt{count}(v)}{\sum_{w\in\texttt{children}(\texttt{parent}(v))}\texttt{count}(w)},
and score a node by the product of scores along its path from
u
q
u_{q}
. Intuitively,
C
⁡
(
v
)
C(v)
estimates how often a specific next token followed this prefix in prior rollouts, and the path product estimates the chance that a drafted chain of tokens will align with what the current policy would generate. We continue expansion until a budget
B
⁡
(
q
)
B(q)
is reached. Given
𝒯
^
\widehat{\mathcal{T}}
, SRT performs one decode pass of the current policy to verify multiple drafted tokens in parallel following classic speculative decoding procedure
(
1
;
15
;
14
;
13
;
17
)
.
Figure 4
:
Illustration of cache maintenance strategy in SRT.
Cache update strategy.
The maintenance of the rollout cache is crucial to the achievable speedups. In SRT, we maintain the cache by two sources as illustrated in Figure
4
. First, decoded outputs of
running rollouts
are inserted online into
𝒯
p
\mathcal{T}_{p}
and node counts are updated. This immediately benefits the remaining samples for the same prompt in multi-sample algorithms and carries signal across training steps when the prompt reappears. Second, we exploit
run-ahead generation
during bubbles. Whenever some sequences in a batch finish early and GPU compute would have otherwise been idle, we allocate that slack to generate rollouts of prompts that will be sampled soon (e.g., from the data loader’s look
-
ahead window or an active prompt queue). Run
-
ahead tokens are inserted into
𝒯
p
\mathcal{T}_{p}
but are never used for learning targets; they serve solely as future drafting hints. Unlike a history-only caches design
(
8
)
, which caches only completed responses from previous epochs in an offline and asynchronous fashion, SRT’s maintenance strategy mitigate cold-start for first-time prompts, actively enriches the cache, and yields more accepted tokens per decoding step—reducing decoding steps and end-to-end latency.
4
Experiment
4.1
End-to-end Results
Table 1
:
SRT achieves superior performance over other methods.
Gen (s) (↓)
Step (s) (↓)
μ
​
s
\mu s
/token (↓)
Method
PPO
GRPO
DAPO
Retool
PPO
GRPO
DAPO
Retool
PPO
GRPO
DAPO
Retool
Baseline
31.5
31.8
44.1
49.0
47.5
42.9
81.7
74.8
104
83.8
32.9
121
N-gram
31.4
31.1
46.0
45.0
47.3
42.1
84.5
69.3
105
82.4
33.3
161
SuffixDecoding
18.4
19.7
62.5
38.8
35.9
30.7
103
69.2
56.6
52.4
41.1
76.7
SRT (Ours)
15.2
15.4
31.5
28.7
31.5
26.2
68.7
58.8
48.3
41.6
23.3
62.2
Effectiveness of Per-prompt Rollout Cache.
We present the experiment results without run-ahead generation to examine the potential of the proposed rollout cache. We integrated SRT into vLLM
(
12
)
and used it as the inference engine for Verl
(
21
)
. Our end-to-end experiments were conducted with the Qwen2.5-1.5B model, using on-policy RL across four algorithms. Concretely, PPO and GRPO were trained on the math dataset
(
9
)
, while DAPO and ReTool were trained on DAPO-Math-17k
(
26
)
. As summarized in Table
1
, SRT consistently outperforms speculative decoding strategies that were originally designed for non-RL scenario across various RL algorithms. In particular, SRT achieves lower generation and step latency as well as reduced per-token inference cost, and these gains hold robustly across both single-turn (PPO/GRPO/DAPO) and multi-turn (ReTool) training regimes.
4.2
Effect of On-the-Fly Updates and Run-Ahead Generation
Figure 5
:
Mean accepted tokens analysis of different cache maintenance strategy.
In this section, we present simulation studies evaluating the impact of (i) on-the-fly updates from ongoing rollouts and (ii) run-ahead generation, both of which enrich the tree-structured cache. Using the DAPO algorithm on DAPO-17k
(
25
)
, we compare SRT to a history-only baseline that updates the cache solely with fully completed responses from previous epochs. As shown in Fig.
5
, SRT consistently achieves a higher mean of accepted tokens (per decoding step). Enabling run-ahead yields additional gains, indicating that a richer cache produces higher-quality drafts. In practice, this reduces decoding steps per prompt, thereby reducing end-to-end cost and latency.


## Body offsets 32186–35115

A
Experimental Setup
Table 2
:
Training configurations for four algorithms.
(a) PPO
Hyperparameter
Value
Hyperparameter
Value
Actor learning rate
1
×
10
−
6
1\times 10^{-6}
Critic learning rate
1
×
10
−
5
1\times 10^{-5}
Warmup ratio
0.0
Rollout temperature
1.0
KL Coefficient (
β
\beta
)
0.001
Train batch size
512
PPO mini batch size
128
Training steps
300
Max input length
512
Max response length
4096
(b) GRPO
Hyperparameter
Value
Hyperparameter
Value
Actor learning rate
1
×
10
−
6
1\times 10^{-6}
Response per Prompt
5
Warmup ratio
0.0
Rollout temperature
1.0
KL Coefficient (
β
\beta
)
0.001
Train batch size
128
PPO mini batch size
64
Training steps
300
Max input length
512
Max response length
4096
(c) DAPO
Hyperparameter
Value
Hyperparameter
Value
Actor learning rate
1
×
10
−
6
1\times 10^{-6}
Response per Prompt
16
Warmup ratio
0.0
Rollout temperature
1.0
KL Coefficient (
β
\beta
)
0.0
Train batch size
128
PPO mini batch size
32
Training steps
300
Max input length
2048
Max response length
8192
Clip ratio high
0.28
Clip ratio low
0.20
(d) ReTool
Hyperparameter
Value
Hyperparameter
Value
Actor learning rate
1
×
10
−
6
1\times 10^{-6}
Critic learning rate
2
×
10
−
6
2\times 10^{-6}
Warmup ratio
0.0
Rollout temperature
1.0
KL Coefficient (
β
\beta
)
0.001
Train batch size
512
PPO mini batch size
128
Training steps
300
Max input length
2048
Max response length
16384
Max turns
8
Clip ratio high
0.28
Clip ratio low
0.20
RL training is conducted using Verl
[
21
]
, with vLLM
[
12
]
serving as the inference engine. The experimental configuration is summarized in Table
2
. All RL training experiments are performed on 8
×
\times
NVIDIA Hopper GPUs.
Appendix B
Ablation Study
B.1
Responses per Prompt in GRPO
We analyzed the effect of varying the number of responses per prompt on the efficiency of SRT. As reported in Table
3
, increasing
n
n
from 5 to 10 produces a greater performance improvement relative to competing algorithms. This behavior is consistent with expectation: as additional rollouts are incorporated, the resulting outputs exhibit greater similarity, thereby enabling SRT to exploit more reliable historical information during speculative decoding.
Table 3
:
Comparison of step time and generation time for GRPO.
GRPO
n
=
5
n=5
GRPO
n
=
10
n=10
Method
Step
(s)
Gen
(s)
Step
Gen
(s)
Baseline
42.9
31.8
61.2
47.1
N-gram
42.1
31.1
58.8
45.3
SuffixDecoding
30.7
19.7
51.9
30.5
SRT
26.2
15.4
41.2
20.4
Improvement (%)
14.7
21.8
20.6
33.1
Appendix C
Related Work
Efficient Reinforcement Learning Frameworks for LLMs.
Recent open-source RL frameworks have democratized RL training
[
21
,
5
,
10
]
.
A common design choice is to employ Ray
[
16
]
to coordinate inference engines (e.g., vLLM
[
12
]
, SGLang
[
29
]
) with training engines (e.g., Megatron
[
22
]
, FSDP
[
27
]
).
Building on this foundation, researchers have proposed various approaches to further improve efficiency.
For example, GRE
