# 2601.08955v1 — minimum necessary primary core

Exact HTML: https://arxiv.org/html/2601.08955v1 . 以下仅已实际读的方法、决定性评价/直接反侧与必要复现字段；区段为HTML正文字符定位，非全文/附录完成声明。未执行实验或代码。

## Body 12884–26408

3.1
World Model Training
As shown in Figure
2
, we first fine-tune a base LLM on expert demonstrations
𝒟
exp
\mathcal{D}_{\mathrm{exp}}
to obtain an initial agent policy
π
θ
0
\pi_{\theta_{0}}
.
This warm-up establishes basic capability to produce executable actions, serving as the foundation for the agent’s exploration.
We ask the agent to perform rollouts in the environment, obtaining the rollout trajectories
𝒟
roll
\mathcal{D}_{\mathrm{roll}}
.
As introduced in §
2
, we learn a LLM-based world model
ℳ
ϕ
\mathcal{M}_{\phi}
that approximates the environment dynamics
p
ϕ
(
s
|
′
s
,
a
)
p_{\phi}(s{{}^{\prime}}|s,a)
,
where
s
s
and
a
a
denote the current state and action, respectively.
s
′
s{{}^{\prime}}
represents the next-step state.
To ensure the world model is grounded and robust to out-of-distribution actions, we train it on a joint dataset
𝒟
WM
=
𝒟
exp
∪
𝒟
roll
\mathcal{D_{\mathrm{WM}}}=\mathcal{D}_{\mathrm{exp}}\cup\mathcal{D}_{\mathrm{roll}}
.
The world model
ℳ
ϕ
\mathcal{M}_{\phi}
is optimized by minimizing the negative log-likelihood as follows:
ℒ
WM
(
ϕ
)
=
−
𝔼
(
s
′
,
s
,
a
)
∼
𝒟
WM
[
log
p
ϕ
(
s
|
′
s
,
a
)
]
.
\mathcal{L}_{\text{WM}}(\phi)=-\mathbb{E}_{(s{{}^{\prime}},s,a)\sim\mathcal{D_{\mathrm{WM}}}}\bigl[\log p_{\phi}(s{{}^{\prime}}|s,a)\bigr].
(1)
3.2
Lookahead Imagination and POIMDP
To integrate world-model foresight into decision making, we extend the standard POMDP (as introduced in §
2
) to a
P
artially
O
bservable and
I
maginable
M
arkov
D
ecision
P
rocess (
POIMDP
).
Under this formulation, the agent is endowed with a lookahead imagination operator induced by the learned world model.
Formally, given the current observed state
s
t
s_{t}
and a lookahead horizon
K
t
∈
{
0
,
1
,
…
,
K
max
}
K_{t}\in\{0,1,\dots,K_{\max}\}
at each time step
t
t
, the agent policy
π
θ
\pi_{\theta}
and the world model
ℳ
ϕ
\mathcal{M}_{\phi}
interact for
K
t
K_{t}
steps within a “mental sandbox”.
This imagination process is given by:
→
π
θ
a
^
t
→
ℳ
ϕ
s
^
t
+
1
→
π
θ
…
→
π
θ
a
^
t
+
K
t
−
1
→
ℳ
ϕ
s
^
t
+
K
t
.
\xrightarrow{\pi_{\theta}}\hat{a}_{t}\xrightarrow{\mathcal{M}_{\phi}}\hat{s}_{t+1}\xrightarrow{\pi_{\theta}}\dots\xrightarrow{\pi_{\theta}}\hat{a}_{t+K_{t}-1}\xrightarrow{\mathcal{M}_{\phi}}\hat{s}_{t+K_{t}}.
(2)
This yields an imagined future trajectory
τ
^
t
(
K
t
)
=
{
(
a
^
t
+
i
,
s
^
t
+
i
+
1
)
}
i
=
0
K
t
−
1
\hat{\tau}^{(K_{t})}_{t}=\{(\hat{a}_{t+i},\hat{s}_{t+i+1})\}_{i=0}^{K_{t}-1}
,
where
a
^
t
+
i
∼
π
θ
(
⋅
|
s
t
,
τ
^
t
(
i
)
)
\hat{a}_{t+i}\sim\pi_{\theta}(\cdot|s_{t},\hat{\tau}_{t}^{(i)})
and
s
^
t
+
i
+
1
∼
ℳ
ϕ
(
⋅
|
s
^
t
+
i
,
a
^
t
+
i
)
\hat{s}_{t+i+1}\sim\mathcal{M}_{\phi}(\cdot|\hat{s}_{t+i},\hat{a}_{t+i})
.
The objective of the agent policy is to yield an appropriate action
a
t
a_{t}
conditioned on both the observable state
s
t
s_{t}
and the imagined future
τ
^
t
(
K
t
)
\hat{\tau}^{(K_{t})}_{t}
.
As such, our POIMDP formulates the policy decision as follows:
a
t
∼
π
θ
(
⋅
∣
s
t
,
τ
^
t
(
K
t
)
)
.
a_{t}\sim\pi_{\theta}(\cdot\mid s_{t},\hat{\tau}^{(K_{t})}_{t}).
(3)
This allows the agent to anticipate goal progress or detect potential bottlenecks before generating the next action, enabling the agent to perform self-correction when necessary.
3.3
Planning with Adaptive Lookahead
To achieve effective task planning, a key challenge is determining how far the agent should imagine.
Short-horizon imagination may miss long-term dependencies, while excessive rollouts can amplify model errors and incur unnecessary computation.
To resolve this, we aim to adaptively select the imagination horizon
K
t
K_{t}
based on the estimated task progress against the ultimate goal.
We instantiate
ITP
via two distinct variants to provide both flexibility and optimization:
(i)
ITP
I
\texttt{ITP}_{\text{I}}
, which is an inference-time method that learns from the imagination, and (ii)
ITP
R
\texttt{ITP}_{\text{R}}
, which is a reinforcement-trained method that jointly optimizes the lookahead horizon selection and action policy.
3.3.1
In-Imagination Learning (
ITP
I
\texttt{ITP}_{\text{I}}
)
ITP
I
\texttt{ITP}_{\text{I}}
is a training-free variant designed for improving LLM agents during inference time.
In this mode, both the agent policy and the world model remain frozen, and the agent relies on its inherent capabilities to perform deliberative reasoning.
At each step
t
t
, the agent receives the current state
s
t
s_{t}
and executes a three-stage “Imagine-then-Plan” procedure:
1)
Adaptive horizon selection
: The agent first assesses the task instruction and the current state
s
t
s_{t}
to determine an appropriate imagination horizon
K
t
∈
{
0
,
1
,
…
,
K
max
}
K_{t}\in\{0,1,\dots,K_{\max}\}
.
This allows the agent to allocate deeper foresight to high-stakes decisions while maintaining computational efficiency for trivial actions.
2)
World-model imagination
: The agent invokes its world model to perform a “mental rehearsal”.
By interacting with
ℳ
ϕ
\mathcal{M}_{\phi}
for
K
t
K_{t}
steps, the agent obtains a multi-step future trajectory
τ
^
t
(
K
t
)
\hat{\tau}_{t}^{(K_{t})}
.
3)
Reflective policy generation
: Rather than directly taking the first action of the imagined sequence, the agent uses
τ
^
t
(
K
t
)
\hat{\tau}_{t}^{(K_{t})}
as implicit feedback for reflective self-refinement.
Specifically, the agent is prompted to self-reflect on the imagined trajectory to evaluate task progress, determine if the predicted states move closer to the ultimate task goal, and detect potential conflicts, bottlenecks, or catastrophic failures before they are irreversibly executed in the real environment.
The agent is asked to perform self-refinement and then select the optimal next action
a
t
a_{t}
, given by:
a
t
∼
π
θ
(
⋅
∣
s
t
,
Reflect
(
τ
^
t
(
K
t
)
)
)
.
a_{t}\sim\pi_{\theta}(\cdot\mid s_{t},\text{Reflect}(\hat{\tau}_{t}^{(K_{t})})).
(4)
By grounding decisions in these imagined futures,
ITP
I
\texttt{ITP}_{\text{I}}
transforms passive observation into proactive deliberation, significantly improving task success rates without additional training.
3.3.2
Reinforced Training (
ITP
R
\texttt{ITP}_{\text{R}}
)
Compared to
ITP
I
\texttt{ITP}_{\text{I}}
that relies on inference-time reasoning,
ITP
R
\texttt{ITP}_{\text{R}}
aims to explicitly learn when and how long to imagine.
We augment the agent with a lightweight
K
K
-head predictor
P
θ
​
(
K
t
|
s
t
)
P_{\theta}(K_{t}|s_{t})
, which is a linear layer built on top of a backbone LLM that predicts distributions over imagination horizons.
The action policy and predictor are optimized jointly with the following three stages.
Stage 1: Pseudo-Labeling Lookahead Horizon.
A key obstacle for learning adaptive lookahead is that expert trajectories provide only
(
s
t
,
a
t
∗
)
(s_{t},a_{t}^{*})
pairs but do not specify the “right” lookahead horizon.
We therefore construct pseudo labels using the world model
ℳ
ϕ
\mathcal{M}_{\phi}
and the initial agent policy
π
θ
0
\pi_{\theta_{0}}
.
Specifically, we use teacher-forced expert actions to rollout on the frozen world model
ℳ
ϕ
\mathcal{M}_{\phi}
by looking ahead one step and obtain future states, from which we derive lookahead-conditioned trajectories
{
τ
^
t
(
k
)
}
k
=
0
K
max
\{\hat{\tau}_{t}^{(k)}\}_{k=0}^{K_{\max}}
.
We then score each candidate step by the log-likelihood of expert actions under
π
θ
0
\pi_{\theta_{0}}
, and select the optimal lookahead step by:
K
~
t
=
arg
⁡
max
0
≤
k
≤
K
max
​
[
log
⁡
p
θ
0
​
(
a
t
∗
∣
s
t
,
τ
^
t
(
k
)
)
−
λ
K
​
k
]
,
\tilde{K}_{t}=\arg\max_{0\leq k\leq K_{\max}}\Big[\log p_{\theta_{0}}(a_{t}^{*}\mid s_{t},\hat{\tau}_{t}^{(k)})-\lambda_{K}\,k\Big],
(5)
where
λ
K
\lambda_{K}
is a hyperparameter controlling the lookahead penalty.
Based on the selection criteria in Eq. (
5
), we obtain a dataset
𝒟
K
\mathcal{D}_{K}
containing the pseudo-labels of the optimal lookahead step for each action in the expert trajectory.
Stage 2: Warm-Up Training.
Starting from the initial agent policy
π
θ
0
\pi_{\theta_{0}}
, we further fine-tune the agent to jointly (i) act under lookahead-conditioned pseudo-trajectories and (ii) predict the required lookahead step.
Specifically, given labeled tuples
{
(
s
t
,
a
t
∗
,
K
~
t
)
}
\{(s_{t},a_{t}^{*},\tilde{K}_{t})\}
, we condition the agent policy on
τ
^
t
(
K
~
t
)
\hat{\tau}_{t}^{(\tilde{K}_{t})}
and train
π
θ
​
(
a
t
|
s
t
,
τ
^
t
(
K
~
t
)
)
\pi_{\theta}(a_{t}|s_{t},\hat{\tau}_{t}^{(\tilde{K}_{t})})
to imitate the expert action
a
t
∗
a_{t}^{*}
, with a standard negative log-likelihood loss
ℒ
π
​
(
θ
)
\mathcal{L}_{\pi}(\theta)
.
Meanwhile, we train the
K
K
-head predictor to estimate the pseudo label
K
~
t
\tilde{K}_{t}
, with a similar negative log-likelihood loss
ℒ
K
​
(
θ
)
\mathcal{L}_{K}(\theta)
.
Our warm-up training is given by:
ℒ
WT
​
(
θ
)
=
ℒ
π
​
(
θ
)
+
η
​
ℒ
K
​
(
θ
)
.
\mathcal{L}_{\mathrm{WT}}(\theta)=\mathcal{L}_{\pi}(\theta)+\eta\,\mathcal{L}_{K}(\theta).
(6)
where
η
\eta
is a weighted coefficient.
This yields (i) a competent agent policy that can generate reliable actions and (ii) an adaptive lookahead horizon predictor that approximates lookahead steps, providing a stable initialization for the subsequent online reinforcement optimization.
Stage 3: Online Optimization.
To balance task performance and imagination cost, we further refine the agent policy through online reinforcement learning.
At each step
t
t
, the agent samples a lookahead step
K
t
K_{t}
from the
K
K
-head predictor, invokes the frozen world model
ℳ
ϕ
\mathcal{M}_{\phi}
to generate a
K
t
K_{t}
-step imagined trajectory
τ
^
t
(
K
t
)
\hat{\tau}_{t}^{(K_{t})}
, and subsequently samples an action
a
t
∼
π
θ
(
⋅
∣
s
t
,
τ
^
t
(
K
t
)
)
a_{t}\sim\pi_{\theta}(\cdot\mid s_{t},\hat{\tau}_{t}^{(K_{t})})
.
As illustrated in Figure
2
, we employ a reward function that augments the environment reward
r
env
r_{\mathrm{env}}
with explicit penalties for computational and interaction overhead, given by:
r
t
+
1
=
r
env
−
λ
K
​
K
t
−
λ
step
,
r_{t+1}=r_{\mathrm{env}}-\lambda_{K}K_{t}-\lambda_{\mathrm{step}},
(7)
where
λ
K
\lambda_{K}
is the lookahead penalty coefficient, and
λ
step
\lambda_{\text{step}}
is a factor discouraging reasoning redundancy.
Specifically, we utilize the Advantage Actor-Critic (A2C) algorithm
16
to jointly optimize the action policy and the
K
K
-head parameters.
The objective is decomposed into three components:
(i) an actor term
ℒ
act
​
(
θ
)
≜
−
𝔼
⁡
[
A
t
​
(
log
⁡
p
θ
​
(
K
t
∣
s
t
)
+
log
⁡
π
θ
​
(
a
t
∣
s
t
,
τ
^
t
(
K
t
)
)
)
]
\mathcal{L}_{\mathrm{act}}(\theta)\triangleq-\mathbb{E}\!\left[A_{t}\left(\log p_{\theta}(K_{t}\mid s_{t})+\log\pi_{\theta}(a_{t}\mid s_{t},\hat{\tau}_{t}^{(K_{t})})\right)\right]
that jointly updates the lookahead predictor and the agent policy;
(ii) a Critic regression term
ℒ
value
​
(
θ
)
≜
𝔼
⁡
[
(
V
θ
​
(
s
t
)
−
V
^
t
)
2
]
\mathcal{L}_{\mathrm{value}}(\theta)\triangleq\mathbb{E}\!\left[(V_{\theta}(s_{t})-\hat{V}_{t})^{2}\right]
that trains a Value-head to match the TD learning target;
and (iii) an entropy regularizer
ℒ
ent
​
(
θ
)
≜
−
𝔼
⁡
[
ℋ
⁡
(
p
θ
​
(
K
t
∣
s
t
)
)
]
\mathcal{L}_{\mathrm{ent}}(\theta)\triangleq-\;\mathbb{E}\!\left[\mathcal{H}(p_{\theta}(K_{t}\mid s_{t}))\right]
that encourages sufficient exploration over the lookahead steps to prevent premature convergence to sub-optimal horizons.
The final training objective is:
ℒ
A2C
​
(
θ
)
=
ℒ
act
​
(
θ
)
+
α
​
ℒ
value
​
(
θ
)
+
β
​
ℒ
ent
​
(
θ
)
,
\mathcal{L}_{\mathrm{A2C}}(\theta)=\mathcal{L}_{\mathrm{act}}(\theta)+\alpha\mathcal{L}_{\mathrm{value}}(\theta)+\beta\mathcal{L}_{\mathrm{ent}}(\theta),
(8)
where
α
\alpha
and
β
\beta
are hyperparameters balancing value estimation and exploration.
Algorithm
1
shows the overview of
ITP
R
\texttt{ITP}_{\text{R}}
’s training process.
At inference time,
ITP
R
\texttt{ITP}_{\text{R}}
utilizes the learned
K
K
-head to perform adaptive lookahead, following a similar deliberative procedure as
ITP
I
\texttt{ITP}_{\text{I}}
.
Algorithm 1
ITP
R
\texttt{ITP}_{\text{R}}
: Reinforced Training with Adaptive Lookahead
1:
Dataset
𝒟
=
{
(
s
t
,
a
t
∗
)
}
\mathcal{D}=\{(s_{t},a_{t}^{*})\}
; Agent policy
π
θ
0
\pi_{\theta_{0}}
; World model
ℳ
ϕ
\mathcal{M}_{\phi}
; Parameters
K
max
K_{\max}
,
λ
K
\lambda_{K}
,
η
\eta
,
α
\alpha
,
β
\beta
.
2:
Agent policy
π
θ
\pi_{\theta}
; Lookahead predictor
P
θ
P_{\theta}
.
3:
// Stage 1: Pseudo-Labeling Lookahead Horizon
4:
for
each episode in
𝒟
\mathcal{D}
do
5:
Cache
{
τ
^
t
(
k
)
}
k
=
0
K
max
\{\hat{\tau}_{t}^{(k)}\}_{k=0}^{K_{\max}}
via
ℳ
ϕ
\mathcal{M}_{\phi}
& teacher-forced
a
t
∗
a_{t}^{*}
.
6:
for
each step
t
t
do
7:
S
t
​
(
k
)
≜
log
⁡
p
θ
0
​
(
a
t
∗
∣
s
t
,
τ
^
t
(
k
)
)
S_{t}(k)\triangleq\log p_{\theta_{0}}(a_{t}^{*}\mid s_{t},\hat{\tau}_{t}^{(k)})
.
8:
K
~
t
←
arg
⁡
max
⁡
[
S
t
​
(
k
)
−
λ
K
​
k
]
\tilde{K}_{t}\leftarrow\arg\max\big[S_{t}(k)-\lambda_{K}k\big]
.
9:
Store
(
s
t
,
a
t
∗
,
K
~
t
)
(s_{t},a_{t}^{*},\tilde{K}_{t})
in
𝒟
K
\mathcal{D}_{K}
.
10:
end
for
11:
end
for
12:
// Stage 2: Warm-Up Training with Lookahead
13:
for
each episode in
𝒟
K
\mathcal{D}_{K}
do
14:
Sample
(
s
t
,
a
t
∗
,
K
~
t
)
∼
𝒟
K
(s_{t},a_{t}^{*},\tilde{K}_{t})\!\sim\!\mathcal{D}_{K}
.
15:
Update
θ
\theta
via Eq. (
6
).
16:
end
for
17:
// Stage 3: Online Actor–Critic Optimization
18:
for
each episode in
𝒟
\mathcal{D}
do
19:
Sample
K
t
∼
P
θ
​
(
K
∣
s
t
)
K_{t}\!\sim\!P_{\theta}(K\!\mid\!s_{t})
, query
ℳ
ϕ
\mathcal{M}_{\phi}
for
τ
^
t
(
K
t
)
\hat{\tau}_{t}^{(K_{t})}
.
20:
Update
θ
\theta
via Eq. (
8
).
21:
end
for
22:
return
π
θ
\pi_{\theta}
and
P
θ
P_{\theta}
.
4
Experiments


## Body 26408–28500

4.1
Experimental Settings
Benchmarks.
We evaluate
ITP
on two representative agent benchmarks:
ALFWorld
(
19
)
for embodied household tasks and
ScienceWorld
(
26
)
for simulated science experiments.
All tasks in these two environments can be formally described as POMDPs. Please refer to Appendix
A
for more details of the two environments.
Backbone Models.
To ensure a fair comparison, all methods are instantiated using the same suite of backbone models: Qwen2.5-7B
(
32
)
, Qwen3-8B
(
31
)
, and Llama-3-8B-Instruct
5
.
For our main experiments, we employ Qwen3-8B as the backbone for training the world model.
We further evaluate other backbone series as world models in §
4.4
.
All models are prompted using their official chat templates to eliminate performance variances caused by formatting inconsistencies.
Backbone
Type
Method
ALFWorld
ScienceWorld
PICK
CLEAN
HEAT
COOL
LOOK
PICK2
Overall
Seen
Unseen
Qwen2.5-7B
Prompting
CoT
17.14
18.52
18.75
16.00
15.38
0.00
14.29
3.09
4.63
ReAct
20.00
22.22
18.75
20.00
23.08
0.00
17.14
8.24
9.93
RAP
40.00
33.33
6.25
32.00
15.38
20.83
27.86
10.30
16.55
ITP
I
\texttt{ITP}_{\text{I}}
(Ours)
65.71
25.93
25.00
24.00
30.77
25.00
35.71
16.49
17.88
Training
SFT
85.71
66.67
56.25
68.00
38.46
66.67
67.86
55.67
49.00
WKM
77.14
77.78
75.00
76.00
76.92
75.00
76.43
54.12
56.29
IWM
90.60
85.20
88.20
84.20
42.90
76.90
82.80
60.82
57.61
ITP
R
\texttt{ITP}_{\text{R}}
(Ours)
94.29
88.89
87.50
53.84
76.00
91.67
85.07
62.58
58.94
Qwen3-8B
Prompting
CoT
14.29
14.81
12.50
12.00
15.38
12.50
13.57
2.44
1.99
ReAct
25.71
22.22
12.50
12.00
7.69
25.00
19.29
9.79
8.61
RAP
42.86
37.04
37.50
16.00
15.38
4.17
28.57
15.46
27.14
ITP
I
\texttt{ITP}_{\text{I}}
(Ours)
82.86
25.93
12.50
16.00
23.08
54.17
41.43
20.61
19.86
Training
SFT
71.43
70.37
68.75
72.00
69.23
70.83
70.71
56.70
49.67
WKM
80.00
77.78
81.25
80.00
76.92
79.17
79.29
60.31
47.68
IWM
85.71
85.19
87.50
84.00
46.15
87.50
82.14
59.27
54.30
ITP
R
\texttt{ITP}_{\text{R}}
(Ours)
97.14
88.88
93.75
88.00
76.92
79.17
88.57
61.85
56.95
Llama3.1-8B
Prompting
CoT
17.14
14.81
18.75
16.00
15.38
8.33
15.00
3.09
3

## Body 34552–39200

4.3
Benefits of Adaptive Lookahead
Superior performance-efficiency trade-off over Fixed Lookahead.
We first compare
ITP
against fixed-
k
k
lookahead, where the agent always imagines a constant horizon
k
k
at every step.
We measure compute by the total tokens consumed over an episode,
T
=
∑
t
(
T
(
t
)
​
(
π
θ
)
+
T
(
t
)
​
(
ℳ
ϕ
)
)
T=\sum_{t}\bigl(T^{(t)}(\pi_{\theta})+T^{(t)}(\mathcal{M}_{\phi})\bigr)
,
and report a
Normalized Budget (NB)
defined by:
NB
​
(
k
)
=
T
¯
​
(
k
)
−
T
¯
​
(
0
)
T
¯
​
(
K
max
)
−
T
¯
​
(
0
)
.
\text{NB}(k)=\frac{\bar{T}(k)-\bar{T}(0)}{\bar{T}(K_{\max})-\bar{T}(0)}.
This calculation of the computational budget transforms the average episode tokens
T
¯
​
(
k
)
\bar{T}(k)
to the
[
0
,
1
]
[0,1]
range.
In subsequent experiments, we set
K
max
=
5
K_{\max}{=}5
on the ALFWorld and
K
max
=
8
K_{\max}{=}8
on the ScienceWorld benchmark, respectively (see Appendix
B
).
As shown in Figure
4
(left), fixed horizons are brittle: SR peaks at a moderate
k
k
and then drops.
In contrast,
ITP
’s adaptive lookahead preserves a significantly higher success rate, removing the need to tune a global horizon and avoiding the diminishing-returns regime of large
k
k
.
As shown in Figure
4
(right), the fixed-
k
k
lookahead strategy remains cost-inefficient, where its normalized budget grows steeply as
k
k
increases.
In comparison, our adaptive lookahead attains a significantly lower budget, eliminating complex tuning and avoiding the high cost of large lookahead steps.
(a)
Our
ITP
I
\texttt{ITP}_{\text{I}}
vs. ReAct + Random Lookahead
(b)
Our
ITP
R
\texttt{ITP}_{\text{R}}
vs. SFT + Random Lookahead
Figure 5:
Comparison between our
adaptive
lookahead mechanism (both
ITP
I
\texttt{ITP}_{\text{I}}
and
ITP
R
\texttt{ITP}_{\text{R}}
) and baselines with a
random
lookahead strategy (ReAct and SFT).
Higher success rates with reduced computational cost over Random Lookahead.
While Figure
4
compares
ITP
to fixed-horizon lookahead, it may also vary the horizon over time.
To disentangle the benefit of adaptive horizon selection from merely using a non-constant horizon, we additionally compare against
random lookahead
, which samples
K
t
K_{t}
independently at each step.
We evaluate the SR vs. NB trade-off on ALFWorld using Qwen3-8B for both the policy and the world model.
We run 140 tasks grouped into 14 folds and report fold-averaged SR and NB, where each point in Figure
5
corresponds to one fold.
We observe that our adaptive lookahead consistently dominates the random strategy, achieving higher SR under lower and more stable budgets.
This confirms that the improvements stem from state-conditioned allocation of lookahead, rather than stochasticity or horizon variability per step.
4.4
Impact of World Models
In this section, we study
how the choice of world-model backbones affects ultimate performance
.
We fix the agent policy to Qwen3-8B, and instantiate the world model with Qwen3-8B, Llama3.1-8B, and the large-scale DeepSeek-V3.2
(
4
)
.
Here, DeepSeek-V3.2 is not trained with a world-modeling objective.
We evaluate
ITP
I
\texttt{ITP}_{\text{I}}
and
ITP
R
\texttt{ITP}_{\text{R}}
on the ALFWorld benchmark.
Figure
6
shows that world-model backbone choice matters most in the training-free setting.
With
ITP
I
\texttt{ITP}_{\text{I}}
, using DeepSeek-V3.2 (without world-model training) yields markedly weaker performance, whereas Qwen and Llama world models maintain high success rates across task families.
However, after training with
ITP
R
\texttt{ITP}_{\text{R}}
, DeepSeek-V3.2 becomes competitive, reaching success rates comparable to or outperforming other world models.
(a)
ITP
I
\texttt{ITP}_{\text{I}}
(Ours)
(b)
ITP
R
\texttt{ITP}_{\text{R}}
(Ours)
Figure 6:
Impact of different world-model backbones. We report success rates of (a)
ITP
I
\texttt{ITP}_{\text{I}}
and (b)
ITP
R
\texttt{ITP}_{\text{R}}
across six different tasks on ALFWorld.
5
Related Work
LLM-based Agents.
LLM-based agents typically use language models as policies that map instructions and partial observations to executable actions.
A significant line of work formulates agent learning as trajectory- or step-level optimization.
For example, ETO
(
20
)
frames learning as exploration-based trajectory optimization, while IPR
(
30
)
and E
2
CL
(
22
)
refine agent behavior via iterative revision and correction signals.
More recent post-training methods further improve robustness and generalization through reflective updates, such as Agent-R
(
34
)
, STeCa
(
24
)
, and AgentRefine
(
8
)
.
However, these methods primarily focus on learning from historical traces, often leaving the agent in a state of “shallow groundin

## Body 41506–42900

Limitations
While our approach demonstrates superior performance compared to baseline methods, it is important to acknowledge the limitations of our current work as follows:
(1) Current evaluation primarily focuses on interactive text-based benchmarks. While these environments provide a rigorous test of long-horizon reasoning, they do not fully capture the challenges of multimodal environments, open-world tool-use, or real-world robotic control.
The transition from linguistic state descriptions to visual or sensorimotor observations may introduce additional noise that could affect the stability of the adaptive lookahead mechanism.
(2) Although our adaptive lookahead mechanism is designed to optimize efficiency by scaling the imagination horizon, the use of world models inherently introduces higher inference-time overhead compared to purely reactive agents.
While higher success rates in high-stakes tasks often justify this trade-off, further optimization (e.g., via speculative decoding or distilled world models) is needed for real-time applications.
We will leave these directions as our future work.
Ethics Statement
We strictly follow the protocols governing the academic use of all LLMs. Our study is conducted in simulated, text-based benchmarks and involves no human subjects or personally identifying information. We cite and comply with the licenses of all models, dataset

## Body 64039–66200

B.2
Parameter Settings
Table
4
summarizes the hyperparameters used for training and inference. Unless otherwise specified, we apply the same configuration across different backbone models.
During exploration, the agent samples actions with temperature
0.7
0.7
.
Due to the difference in task trajectory lengths between ALFWorld and ScienceWorld (ScienceWorld has an average of 15 steps, while ALFWorld has an average of 8 steps), during
ITP
R
\texttt{ITP}_{\text{R}}
training, we set
K
max
K_{\max}
to 5 for ALFWorld and to 8 for ScienceWorld.
Name
Value
Warm-Up Training
cutoff_len
2048
epochs
3
per_device_train_batch_size
1
gradient_accumulation_steps
16
learning_rate
2
×
10
−
5
2\times 10^{-5}
warmup_ratio
0.03
lr_scheduler
cosine
fp16 / bf16
True / False
gradient_checkpointing
False
lora_r
8
lora_alpha
16
lora_dropout
0.05
merge_lora
True
Online A2C Optimization
γ
\gamma
(discount)
0.99
rl_learning_rate
5
×
10
−
6
5\times 10^{-6}
λ
K
\lambda_{K}
(lookahead penalty)
0.2
λ
step
\lambda_{\text{step}}
(step cost)
0.01
success_bonus
0.01
invalid_action_penalty
-0.1
η
\eta
0.5
α
\alpha
1.0
β
\beta
0.01
max_grad_norm
1.0
Inference Stage
do_sample (exploration)
True
temperature (exploration)
0.7
top_p (exploration)
0.9
action_max_new_tokens
16
imagine_action_max_new_tokens
12
wm_max_new_tokens
192
K
max
K_{\max}
(ALFWorld)
5
K
max
K_{\max}
(ScienceWorld)
8
Table 4:
Hyperparameter setup.
Experimental support, please
view the build logs
for errors. Generated by
L
A
T
E
xml
.
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
      support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
      methods listed below:
Click the "Report Issue"
(
)
button, located in the page header.
Tip:
You can select the relevant text first, to include it in your report.
Our team has already identified
the following issues
. We appreciate your time reviewing and reporting rendering errors we
      may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
