# 2601.09084v1 necessary primary



## B1 exact likelihood-ratio identity and finite setup

itional on a fixed
δ
1
:
B
\delta_{1:B}
the joint likelihood factorizes:
P
δ
(
Y
1
:
B
)
=
∏
t
=
1
B
p
t
Y
t
(
1
−
p
t
)
1
−
Y
t
,
p
t
=
1
2
+
δ
t
,
P_{\delta}(Y_{1:B})=\prod_{t=1}^{B}p_{t}^{Y_{t}}(1-p_{t})^{1-Y_{t}},\qquad p_{t}=\tfrac{1}{2}+\delta_{t},
and under
H
0
H_{0}
,
p
t
=
1
2
p_{t}=\tfrac{1}{2}
for all
t
t
. Hence
KL
(
P
δ
∥
P
0
)
=
∑
t
=
1
B
KL
(
Bern
(
p
t
)
∥
Bern
(
1
/
2
)
)
.
\mathrm{KL}(P_{\delta}\|P_{0})=\sum_{t=1}^{B}\mathrm{KL}(\mathrm{Bern}(p_{t})\|\mathrm{Bern}(1/2)).
Define the log-likelihood ratio
L
(
Y
)
:=
log
d
​
P
δ
d
​
P
0
(
Y
1
:
B
)
=
∑
t
=
1
B
ℓ
t
(
Y
t
)
,
ℓ
t
(
y
)
=
y
log
p
t
1
/
2
+
(
1
−
y
)
log
1
−
p
t
1
/
2
.
L(Y):=\log\frac{dP_{\delta}}{dP_{0}}(Y_{1:B})=\sum_{t=1}^{B}\ell_{t}(Y_{t}),\quad\ell_{t}(y)=y\log\frac{p_{t}}{1/2}+(1-y)\log\frac{1-p_{t}}{1/2}.
Note that
𝔼
δ
[
L
]
=
KL
(
P
δ
∥
P
0
)
\mathbb{E}_{\delta}[L]=\mathrm{KL}(P_{\delta}\|P_{0})
and
𝔼
0
​
[
e
L
]
=
1
\mathbb{E}_{0}[e^{L}]=1
.
B.2
Proof of Theorem
3.2
Proof.
Fix any alternative
δ
\delta
with
KL
(
P
δ
∥
P
0
)
≥
𝖪
\mathrm{KL}(P_{\delta}\|P_{0})\geq\mathsf{K}
.
By the Bretagnolle–Huber inequality (a standard consequence of the change-of-measure identity),
for any test
ϕ
\phi
,
Pr
0
(
ϕ
=
1
)
+
Pr
δ
(
ϕ
=
0
)
≥
1
2
exp
(
−
KL
(
P
δ
∥
P
0
)
)
.
\Pr_{0}(\phi=1)+\Pr_{\delta}(\phi=0)\ \geq\ \tfrac{1}{2}\exp\!\big(-\mathrm{KL}(P_{\delta}\|P_{0})\big).
Since
KL
(
P
δ
∥
P
0
)
≥
𝖪
\mathrm{KL}(P_{\delta}\|P_{0})\geq\mathsf{K}
, we obtain
Pr
0
⁡
(
ϕ
=
1
)
+
Pr
δ
⁡
(
ϕ
=
0
)
≥
1
2
​
e
−
𝖪
.
\Pr_{0}(\phi=1)+\Pr_{\delta}(\phi=0)\ \geq\ \tfrac{1}{2}e^{-\mathsf{K}}.
Taking the supremum over all
δ
\delta
with KL budget at leas

## empirical resampling setup

when signal concentrates in a few prompt types.
Both protocols are mostly diffuse (Appendix
C.2
), though MT-Bench occasionally shows concentration:
Scenario
Proportional
Two-stage
Diffuse signal (typical)
✓
×
\times
Concentrated signal
✓
✓
\checkmark
if
κ
>
1.5
\kappa>1.5
Small budget (
B
<
m
​
b
B<mb
)
✓
×
\times
Large budget, uneven signal
✓
✓
In diffuse regimes, proportional allocation is minimax-optimal (Theorem
3.5
); two-stage allocation yields gains only when signal concentration is high, as characterized by Theorem
3.6
and verified empirically in Appendix
C
.
4
Method: Detectability Curves and Budget Estimation
We empirically instantiate the detectability framework of Section
3
using subsampling-based power estimates. We summarize detectability outcomes across representative model pairs and budgets in the results section. These empirical patterns motivate the protocol-level implications discussed in Section
6.3
.
Rather than reporting a single test outcome at a fixed budget, we characterize
detectability as a function of budget
. For a given dataset and model pair, we repeatedly subsample
n
n
judgments with replacement and estimate the probability that a hypothesis test detects an improvement, yielding a
detectability curve
that maps evaluation budget
n
n
to detection probability. We test a Bernoulli preference rate
p
p
against
p
=
0.5
p=0.5
; classical power analysis implies the required budget scales as
n
=
Θ
⁡
(
δ
−
2
)
n=\Theta(\delta^{-2})
for
δ
=
|
p
−
0.5
|
\delta=|p-0.5|
. Guided by Section
3
, we interpret
δ
\delta
as an observable proxy for per-judgment information, so detectability curves summarize feasibility as a function of both effect size and realized evaluation allocation.
4.1
Robustness and Statistical Considerations
We estimate detectability curves using repeated subsampling with replacement, which directly estimates the probability that a hypothesis test succeeds at a given budget. This directly addresses the operational question of practical interest and yields results qualitatively similar to bootstrap-based alternatives. We discard ties to obtain a best-case binary preference signal, as ties provide no directional information. Appendix
D.6
shows that ties concentrate in low-margin regimes and that alternative tie encodings reduce estimated margins and increase required evaluation budgets, without altering qualitative conclusions.
Figure 2
:
Empirical validation of theoretical scaling. Each point corresponds to a model comparison, plotted by its preference margin and the implied evaluation budget required for detection power. The solid curve shows the predicted asymptotic
δ
−
2
\delta^{-2}
scaling from Eq.
8
.
5
Empirical Evaluation
We evaluate our framework across large-scale human preference datasets that differ in prompt distribution, annotation protocol, and evaluation goals. These datasets allow us to characterize how perceptual effect size and evaluation budget interact in open-ended and curated settings (Figure
2
). To assess generality beyond chat-based text evaluation, we analyze the text-to-image preference dataset
Pick-a-Pic
(
14
)
and the code generation platform
BigCodeArena
(
20
)
, which provides execution feedback. Both exhibit comparable near-tie regimes: 14.2% of image comparisons and 41% of code comparisons fall into
|
δ
^
|
≤
0.10
|\hat{\delta}|\leq 0.10
, requiring hundreds to thousands of judgments for reliable detection (Appendix
D.7
,
D.8
). These findings demonstrate that feasibility limits persist across modalities, even when partial ground truth is available.


Source https://arxiv.org/html/2601.09084v1 . Only necessary method/evaluation and decisive direct counterevidence, not all appendices or proof population.

## Body offsets 9267–21900

2
Problem Setup and Definitions
We consider the problem of comparing two generative models, denoted
A
A
and
B
B
, using pairwise human preferences. Given a prompt sampled from a fixed distribution and responses generated by both models, a human evaluator is asked to indicate which response they prefer, or whether the responses are tied.
Throughout this work, we focus on
decisive
comparisons and discard ties. Each human judgment is therefore represented as a binary random variable
Y
=
[
human prefers model
​
B
​
over model
​
A
]
.
Y=\mathbf{1}\!\left[\text{human prefers model }B\text{ over model }A\right].
(1)
where
Y
=
1
Y=1
indicates a preference for
B
B
and
Y
=
0
Y=0
indicates a
preference for
A
A
. We define
p
=
Pr
⁡
(
Y
=
1
)
,
p=\Pr(Y=1),
(2)
the probability that a randomly sampled evaluator prefers
B
B
over
A
A
under the given evaluation protocol.
Ties and best-case analysis.
Human evaluators may also report ties, indicating no clear preference between the two responses. Throughout this work, we discard ties and condition on decisive outcomes in order to obtain a binary preference signal. This choice corresponds to a
best-case
analysis. Conditioning on decisive judgments maximizes the per-judgment directional information available for distinguishing
p
≠
1
/
2
p\neq 1/2
. Incorporating ties via a multinomial or ordinal preference model can only reduce the effective information per judgment; therefore, it cannot improve detectability. We empirically verify robustness to alternative tie encodings in Appendix
D.6
.
2.1
Preference Margin as Effect Size
The central quantity governing detectability in pairwise human evaluation is the magnitude of the preference margin. We define the preference margin as
δ
=
p
−
1
2
,
\delta=p-\tfrac{1}{2},
(3)
which measures the deviation from indifference. Larger values of
|
δ
|
|\delta|
correspond to differences that are easier for human evaluators to perceive, while values of
|
δ
|
|\delta|
close to zero correspond to subtle qualitative differences.
From a statistical perspective, detecting an improvement reduces to distinguishing the null hypothesis
p
=
0.5
p=0.5
from the alternative
p
≠
0.5
p\neq 0.5
given finite noisy observations. The fundamental quantity governing detectability is the KL divergence between these hypotheses. For Bernoulli preferences near
p
=
0.5
p=0.5
, the per-judgment KL divergence scales as
(
p
−
1
2
)
2
(p-\tfrac{1}{2})^{2}
up to constants, so empirical preference margins serve as observable proxies for the KL budget accumulated by an evaluation protocol.
2.2
Near-Tie (Low-Signal) Comparisons
We refer to comparisons with small absolute preference margins as
near-tie
or
low-signal
comparisons. Formally, for a chosen threshold
τ
∈
(
0
,
0.5
)
\tau\in(0,0.5)
, we define the near-tie subset as
|
p
^
−
1
2
|
<
τ
,
|\hat{p}-\tfrac{1}{2}|<\tau,
(4)
where
p
^
\hat{p}
is the empirical estimate of
p
p
from observed judgments. Rather than treating
τ
\tau
as a universal constant, we treat it as a sensitivity parameter and report results across multiple thresholds where appropriate.
We frame human evaluation as a hypothesis-testing problem,
H
0
:
p
=
0.5
vs.
H
1
:
p
≠
0.5
,
H_{0}:p=0.5\quad\text{vs.}\quad H_{1}:p\neq 0.5,
(5)
and study detectability as a function of evaluation budget. This framing clarifies that inconclusive human evaluations are not evidence of model equivalence—they may simply reflect insufficient budget relative to the underlying effect size. With
n
n
independent judgments, standard binomial tests imply that rejection probability depends on
n
n
, the significance level
α
\alpha
, and the preference margin
|
δ
|
|\delta|
.
Rather than fixing
n
n
, we characterize
detectability curves
mapping budget to detection probability. These curves make explicit the tradeoff between effect size and sample size and clarify the interpretation of inconclusive results: when
|
δ
|
|\delta|
is small, detectability saturates and additional budget yields diminishing returns.
3
Theory: Feasibility Limits and Their Consequences
Standard power analysis assumes homogeneous effect size
δ
\delta
; the
δ
−
2
\delta^{-2}
sample complexity scaling is classical. Our contribution is characterizing when prompt-induced heterogeneity permits adaptive gains and when it does not. We show that proportional allocation is minimax-optimal in diffuse regimes (Theorem
3.5
), while two-stage screening helps only under sufficient signal concentration (Theorem
3.6
). Section
3.5
translates these results into practical guidance.
3.1
Setup
We study hypothesis testing under prompt-induced heterogeneity, where individual judgments carry unequal statistical information. At round
t
t
,
Y
t
∼
Bernoulli
⁡
(
1
2
+
δ
t
)
,
δ
t
∈
[
−
1
4
,
1
4
]
,
Y_{t}\sim\mathrm{Bernoulli}\!\left(\tfrac{1}{2}+\delta_{t}\right),\qquad\delta_{t}\in[-\tfrac{1}{4},\tfrac{1}{4}],
(6)
where conditional on
δ
1
:
B
\delta_{1:B}
the observations are independent.
Let
P
δ
P_{\delta}
denote the joint law under
δ
1
:
B
\delta_{1:B}
and
P
0
P_{0}
the null law
δ
t
≡
0
\delta_{t}\equiv 0
.
We define the
KL budget
of an evaluation stream as
𝖪
(
δ
1
:
B
)
\displaystyle\mathsf{K}(\delta_{1:B})
:
=
KL
(
P
δ
∥
P
0
)
\displaystyle:=\mathrm{KL}(P_{\delta}\,\|\,P_{0})
(7)
=
∑
t
=
1
B
KL
⁡
(
Bern
⁡
(
1
2
+
δ
t
)
∥
Bern
⁡
(
1
2
)
)
.
\displaystyle=\sum_{t=1}^{B}\mathrm{KL}\!\left(\mathrm{Bern}\!\left(\tfrac{1}{2}+\delta_{t}\right)\,\middle\|\,\mathrm{Bern}\!\left(\tfrac{1}{2}\right)\right).
All feasibility bounds in Section
3
should be interpreted as best-case limits: any dependence between judgments can only reduce effective sample size and make detection harder.
Lemma 3.1
(Quadratic KL scaling)
.
If
|
δ
|
≤
1
4
|\delta|\leq\tfrac{1}{4}
, then
2
​
δ
2
≤
KL
⁡
(
Bern
⁡
(
1
2
+
δ
)
∥
Bern
⁡
(
1
2
)
)
≤
9
4
​
δ
2
,
2\,\delta^{2}\;\leq\;\KL\!\left(\Bern(\tfrac{1}{2}+\delta)\,\middle\|\,\Bern(\tfrac{1}{2})\right)\;\leq\;\tfrac{9}{4}\,\delta^{2},
and consequently
2
∑
t
=
1
B
δ
t
2
≤
𝖪
(
δ
1
:
B
)
≤
9
4
∑
t
=
1
B
δ
t
2
.
2\sum_{t=1}^{B}\delta_{t}^{2}\;\leq\;\mathsf{K}(\delta_{1:B})\;\leq\;\tfrac{9}{4}\sum_{t=1}^{B}\delta_{t}^{2}.
3.2
Minimax feasibility under adversarial heterogeneity
We test
H
0
:
P
0
H_{0}:P_{0}
versus the composite alternative
H
1
:
𝖪
(
δ
1
:
B
)
≥
𝖪
,
H_{1}:\ \mathsf{K}(\delta_{1:B})\geq\mathsf{K},
for a target
𝖪
>
0
\mathsf{K}>0
. A test
ϕ
\phi
has type-I error
α
⁡
(
ϕ
)
=
Pr
0
⁡
(
ϕ
=
1
)
\alpha(\phi)=\Pr_{0}(\phi=1)
and worst-case type-II error
β
⁡
(
ϕ
)
=
sup
𝖪
⁡
(
δ
)
≥
𝖪
Pr
δ
⁡
(
ϕ
=
0
)
\beta(\phi)=\sup_{\mathsf{K}(\delta)\geq\mathsf{K}}\Pr_{\delta}(\phi=0)
.
Theorem 3.2
(Minimax lower bound)
.
For any test
ϕ
\phi
and any
𝖪
>
0
\mathsf{K}>0
,
sup
𝖪
⁡
(
δ
)
≥
𝖪
(
Pr
0
[
ϕ
=
1
]
+
Pr
δ
[
ϕ
=
0
]
)
≥
1
2
e
−
𝖪
.
\sup_{\mathsf{K}(\delta)\geq\mathsf{K}}\big(\Pr_{0}[\phi=1]+\Pr_{\delta}[\phi=0]\big)\;\geq\;\tfrac{1}{2}e^{-\mathsf{K}}.
Thus, achieving total error
≤
α
+
β
\leq\alpha+\beta
requires
𝖪
≳
log
⁡
1
α
+
β
\mathsf{K}\gtrsim\log\!\frac{1}{\alpha+\beta}
.
Theorem 3.3
(Matching upper bound)
.
There exist universal constants
c
,
C
>
0
c,C>0
such that for any
𝖪
>
0
\mathsf{K}>0
there exists a test
ϕ
𝖪
\phi_{\mathsf{K}}
satisfying
sup
𝖪
⁡
(
δ
)
≥
C
​
𝖪
(
Pr
0
[
ϕ
𝖪
=
1
]
+
Pr
δ
[
ϕ
𝖪
=
0
]
)
≤
e
−
c
​
𝖪
.
\sup_{\mathsf{K}(\delta)\geq C\mathsf{K}}\big(\Pr_{0}[\phi_{\mathsf{K}}=1]+\Pr_{\delta}[\phi_{\mathsf{K}}=0]\big)\;\leq\;e^{-c\mathsf{K}}.
Proof sketch.
The lower bound follows from the Bretagnolle–Huber inequality. The upper bound uses a likelihood-ratio test thresholded at
𝖪
/
2
\mathsf{K}/2
, with bounded increments yielding concentration when
KL
(
P
δ
∥
P
0
)
≥
C
𝖪
\mathrm{KL}(P_{\delta}\|P_{0})\geq C\mathsf{K}
. Full proofs appear in Appendix
B
. Together, these bounds show that the KL budget is both necessary and sufficient for detection, up to constants—establishing KL divergence as the right currency for reasoning about evaluation feasibility.
3.3
Stochastic prompt heterogeneity
We now consider a random-effects model in which
δ
1
,
…
,
δ
B
∼
i
.
i
.
d
.
𝒟
\delta_{1},\dots,\delta_{B}\stackrel{{\scriptstyle i.i.d.}}{{\sim}}\mathcal{D}
for a distribution
𝒟
\mathcal{D}
supported on
[
−
1
4
,
1
4
]
[-\tfrac{1}{4},\tfrac{1}{4}]
. Unless stated otherwise, all expectations in this subsection are taken with respect to the random draw
δ
1
:
B
∼
𝒟
B
\delta_{1:B}\sim\mathcal{D}^{B}
.
Proposition 3.4
.
Let
μ
2
=
𝔼
δ
∼
𝒟
​
[
δ
2
]
\mu_{2}=\mathbb{E}_{\delta\sim\mathcal{D}}[\delta^{2}]
.
There exist universal constants
c
,
C
>
0
c,C>0
such that:
1.
𝔼
[
𝖪
(
δ
1
:
B
)
]
≍
B
μ
2
\mathbb{E}[\mathsf{K}(\delta_{1:B})]\asymp B\,\mu_{2}
.
2.
The test
ϕ
𝖪
\phi_{\mathsf{K}}
from Theorem
3.3
achieves
𝔼
⁡
[
Pr
0
⁡
(
ϕ
𝖪
=
1
)
+
Pr
δ
⁡
(
ϕ
𝖪
=
0
)
]
≤
e
−
c
​
𝖪
\mathbb{E}\!\left[\Pr_{0}(\phi_{\mathsf{K}}=1)+\Pr_{\delta}(\phi_{\mathsf{K}}=0)\right]\leq e^{-c\mathsf{K}}
whenever
B
​
μ
2
≥
C
​
𝖪
B\mu_{2}\geq C\mathsf{K}
.
Implication.
Up to constants, feasibility is governed by the accumulated KL budget, equivalently by
B
​
𝔼
​
[
δ
2
]
B\,\mathbb{E}[\delta^{2}]
(Lemma 3.1, Proposition 3.4).
3.4
Optimal Allocation of Evaluation Budget
Evaluation protocols allocate a finite judgment budget across heterogeneous prompts; we ask whether this allocation can improve detectability beyond KL-budget limits.
3.4.1
Adversarial heterogeneity
Let
m
m
prompt types have incidence weights
w
∈
Δ
m
w\in\Delta^{m}
. A protocol
π
\pi
allocates a total budget
B
B
judgments, producing counts
N
1
,
…
,
N
m
N_{1},\dots,N_{m}
with
∑
i
N
i
=
B
\sum_{i}N_{i}=B
. Define the
allocation bottleneck
Λ
⁡
(
π
)
:=
𝔼
π
​
[
min
i
∈
[
m
]
⁡
N
i
w
i
]
.
\Lambda(\pi):=\mathbb{E}_{\pi}\!\left[\min_{i\in[m]}\frac{N_{i}}{w_{i}}\right].
For a test
φ
\varphi
, define the worst-case risk
ℛ
⁡
(
π
,
φ
)
:=
Pr
0
π
⁡
(
φ
=
1
)
+
sup
δ
∈
ℋ
1
​
(
μ
2
)
Pr
δ
π
⁡
(
φ
=
0
)
,
\mathcal{R}(\pi,\varphi):=\Pr_{0}^{\pi}(\varphi=1)+\sup_{\delta\in\mathcal{H}_{1}(\mu_{2})}\Pr_{\delta}^{\pi}(\varphi=0),
where
ℋ
1
​
(
μ
2
)
=
{
δ
:
∑
i
w
i
​
δ
i
2
≥
μ
2
}
.
\mathcal{H}_{1}(\mu_{2})=\{\delta:\sum_{i}w_{i}\delta_{i}^{2}\geq\mu_{2}\}.
Theorem 3.5
(Minimax optimality of proportional allocation)
.
There exist universal constants
c
,
C
>
0
c,C>0
such that for any allocation policy
π
\pi
and test
φ
\varphi
,
ℛ
⁡
(
π
,
φ
)
≥
1
2
​
exp
⁡
(
−
C
​
μ
2
​
Λ
​
(
π
)
)
.
\mathcal{R}(\pi,\varphi)\;\geq\;\tfrac{1}{2}\exp\!\big(-C\,\mu_{2}\,\Lambda(\pi)\big).
Consequently,
inf
π
,
φ
ℛ
⁡
(
π
,
φ
)
≥
1
2
​
exp
⁡
(
−
C
​
B
​
μ
2
)
.
\inf_{\pi,\varphi}\mathcal{R}(\pi,\varphi)\;\geq\;\tfrac{1}{2}\exp(-CB\mu_{2}).
Moreover, proportional allocation with
N
i
≈
B
​
w
i
N_{i}\approx Bw_{i}
satisfies
Λ
⁡
(
π
)
≥
c
​
B
\Lambda(\pi)\geq cB
and achieves this rate up to constants.
Interpretation.
This result implies that in open-ended evaluation settings, where signal is spread diffusely across many prompt types, sophisticated allocation strategies cannot rescue underpowered comparisons. The fundamental bottleneck is the total KL budget, not how it is distributed.
3.4.2
Stochastic heterogeneity
Assume
δ
1
,
…
,
δ
m
∼
i.i.d.
D
\delta_{1},\dots,\delta_{m}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}D
with
μ
2
=
𝔼
⁡
[
δ
2
]
\mu_{2}=\mathbb{E}[\delta^{2}]
.
Let
S
q
​
(
δ
)
S_{q}(\delta)
denote the indices of the top
⌈
q
​
m
⌉
\lceil qm\rceil
values of
δ
i
2
\delta_{i}^{2}
, and define the concentrated signal
μ
2
,
q
​
(
δ
)
:=
∑
i
∈
S
q
​
(
δ
)
w
i
∑
j
∈
S
q
​
(
δ
)
w
j
​
δ
i
2
.
\mu_{2,q}(\delta):=\sum_{i\in S_{q}(\delta)}\frac{w_{i}}{\sum_{j\in S_{q}(\delta)}w_{j}}\,\delta_{i}^{2}.
While Arena is not adversarial, Theorem 3.5 provides a worst-case bound showing that sufficiently diffuse signal alone is enough to preclude gains from adaptive allocation.
Theorem 3.6
(Adaptive gains under stochastic heterogeneity)
.
There exists a two-stage adaptive allocation policy
π
2
​
s
​
t
​
a
​
g
​
e
\pi_{\mathrm{2stage}}
and constants
c
,
c
′
>
0
c,c^{\prime}>0
such that, for all
sufficiently large
B
B
,
𝔼
δ
​
[
ℛ
⁡
(
π
2
​
s
​
t
​
a
​
g
​
e
,
φ
)
]
≤
exp
⁡
(
−
c
​
B
​
𝔼
​
[
μ
2
,
q
​
(
δ
)
]
)
,
\mathbb{E}_{\delta}\!\left[\mathcal{R}(\pi_{\mathrm{2stage}},\varphi)\right]\;\leq\;\exp\!\big(-c\,B\,\mathbb{E}[\mu_{2,q}(\delta)]\big),
while for proportional allocation
π
prop
\pi_{\mathrm{prop}}
,
inf
φ
𝔼
δ
​
[
ℛ
⁡
(
π
prop
,
φ
)
]
≥
exp
⁡
(
−
c
′
​
B
​
μ
2
)
.
\inf_{\varphi}\mathbb{E}_{\delta}\!\left[\mathcal{R}(\pi_{\mathrm{prop}},\varphi)\right]\;\geq\;\exp(-c^{\prime}B\mu_{2}).
Implication.
See Appendix
C
for interpretation and practical consequences.
Corollary 3.7
(Practical parameter choices for two-stage allocation)
.
Suppose there are
m
m
prompt types and total budget
B
B
. Choose a screeni

## Body offsets 28282–32400

5.1
Selection Effects and Feasibility in Arena
Table
1
summarizes the distribution of absolute preference margins
|
δ
|
|\delta|
among well-sampled model pairs and the implied number of decisive judgments required for reliable detection. Median margins among well-sampled model pairs under each protocol are relatively large under both Arena and MT-Bench, implying that many comparisons are easily detectable with modest budgets. This reflects strong selection effects: comparisons exhibiting clear signal tend to attract sustained evaluation effort and become well-sampled.
Table 1
:
Tail quantiles of absolute preference margins
|
δ
|
|\delta|
and the implied number of decisive human judgments required to achieve 90% detection power, computed using Eq. (8) with
α
=
0.05
\alpha=0.05
. Median margins are large due to selection effects, while feasibility limits arise in the lower tail.
Protocol
Statistic
|
δ
|
|\delta|
n
n
(
α
=
0.05
\alpha=0.05
)
n
n
(
α
=
0.01
\alpha=0.01
)
Arena
p
10
​
(
|
δ
|
CLOSE
p_{10}(|\delta|
)
0.082
395
560
Arena
p
25
​
(
|
δ
|
CLOSE
p_{25}(|\delta|
)
0.190
73
103
Arena
p
50
​
(
|
δ
|
CLOSE
p_{50}(|\delta|
)
0.321
26
36
MT-Bench
p
10
​
(
|
δ
|
CLOSE
p_{10}(|\delta|
)
0.047
1175
1664
MT-Bench
p
25
​
(
|
δ
|
CLOSE
p_{25}(|\delta|
)
0.187
75
106
MT-Bench
p
50
​
(
|
δ
|
CLOSE
p_{50}(|\delta|
)
0.285
32
46
Feasibility limits, however, are governed by the lower tail of the margin distribution. Table
2
isolates this regime by conditioning on near-tie comparisons with
|
δ
|
≤
τ
|\delta|\leq\tau
. Even among well-sampled Arena pairs, a non-trivial fraction fall into the
|
δ
|
≤
0.10
|\delta|\leq 0.10
regime, where the median conditional margin implies required budgets on the order of hundreds of judgments, exceeding typical Arena budgets (bootstrap in Appendix
D
). A similar pattern appears under MT-Bench: while margins are larger on average, near-tie comparisons still require thousands of judgments for reliable detection.
Table 2
:
Conditional feasibility for near-tie comparisons. Conditioning on low-signal comparisons with
|
δ
|
≤
τ
|\delta|\leq\tau
, we report the median margin within this subset and the implied budget for 90% detection power. Proportion denotes the fraction of well-sampled model pairs under each protocol satisfying the near-tie condition.
Protocol
Condition
Count
Proportion
Median
|
δ
|
|\delta|
n
n
(
α
=
0.05
\alpha=0.05
)
Arena
|
δ
|
≤
0.10
|\delta|\leq 0.10
6
0.176
0.072
506
MT-Bench
|
δ
|
≤
0.10
|\delta|\leq 0.10
3
0.200
0.037
1878
To assess whether violations of independence could explain deviations from the best-case feasibility bounds of Section
3
, we compare classical i.i.d. standard errors to cluster-robust estimates allowing arbitrary correlation within prompts. The resulting variance inflation is negligible across all pairs (median ratio 1.000; 99th percentile below 1.001), indicating that detectability failures arise from small preference margins rather than violations of independence. Additional robustness checks are reported in Appendix
D
.
5.2
Near-Tie Comparisons and Budget Requirements
We analyze model comparisons with small absolute preference margins to characterize evaluation difficulty when qualitative differences are subtle. Conditioning on
|
p
^
−
0.5
|
<
τ
|\hat{p}-0.5|<\tau
isolates a low-signal regime in which statistical detectability is intrinsically limited.
Empirically, near-tie comparisons are not artifacts of selective evaluation. Estimated preference margins are stable as additional judgments accrue. Conditioning on an equal-exposure cohort (50 early judgments per pair) yields strongly correlated early and final margins (Spearman
ρ
=
0.93
\rho=0.93
), with no evidence of drift toward lower separability (Appendix
D
). Near-ties are rare under equal exposure, but when they appear they persist after 200+ judgments, indicating that low-signal comparisons are intrinsic rather than induced by Arena’s adaptive sampling.
5.3
Protocol Effects: Arena versus MT-Bench
The preceding analyses characterize feasibility limits under open-ended evaluation with user-generated prompts (e.g., Chatbot

## Body offsets 43623–45000

8
Limitations
Our analysis makes several simplifying assumptions that bound the scope of our conclusions. We treat human judgments as independent and identically distributed; as shown empirically in Section
5.1
, such correlations are negligible for well-sampled model pairs in our datasets and would only further tighten the best-case feasibility bounds if present. Our estimates should be interpreted as best-case benchmarks under idealized assumptions.
Second, our empirical analysis focuses on chat-oriented large language models, with extensions to image preference data and code generation; preference margins may differ in other domains such as mathematical reasoning or specialized technical tasks. Extending the analysis to additional modalities and task types is an important future direction.
Finally, the Arena data reflects a dynamic evaluation environment in which models improve over time and evaluation effort is not uniformly allocated. As discussed in Section
4.1
, this induces selection effects that shape which comparisons become well-sampled, without systematically biasing them toward low-signal regimes. Our conclusions characterize the detectability of comparisons that attract sustained evaluation attention, rather than all possible model comparisons.
9
Conclusion
We studied when human preference evaluations can reliably detect improvements in gene

## Body offsets 57760–61100

 a_{0}
for a suitable universal
a
0
a_{0}
.
∎
B.4
Proof of Theorem
3.3
Proof.
Fix a target
𝖪
>
0
\mathsf{K}>0
and define the test
ϕ
𝖪
(
Y
)
:=
𝟏
{
L
(
Y
)
≥
1
2
𝖪
}
.
\phi_{\mathsf{K}}(Y):=\mathbf{1}\left\{L(Y)\geq\tfrac{1}{2}\mathsf{K}\right\}.
(Type-I control) Under
P
0
P_{0}
,
e
L
e^{L}
is the likelihood ratio and satisfies
𝔼
0
​
[
e
L
]
=
1
\mathbb{E}_{0}[e^{L}]=1
.
By Markov’s inequality,
Pr
0
(
L
≥
1
2
𝖪
)
=
Pr
0
(
e
L
≥
e
𝖪
/
2
)
≤
e
−
𝖪
/
2
.
\Pr_{0}\!\left(L\geq\tfrac{1}{2}\mathsf{K}\right)=\Pr_{0}\!\left(e^{L}\geq e^{\mathsf{K}/2}\right)\leq e^{-\mathsf{K}/2}.
(Type-II control) Consider any alternative
δ
\delta
such that
KL
(
P
δ
∥
P
0
)
=
𝔼
δ
[
L
]
≥
C
𝖪
\mathrm{KL}(P_{\delta}\|P_{0})=\mathbb{E}_{\delta}[L]\geq C\mathsf{K}
.
By Lemma
B.1
,
Pr
δ
⁡
(
L
<
1
2
​
𝖪
)
≤
Pr
δ
⁡
(
L
≤
1
2
​
𝔼
δ
​
[
L
]
)
≤
exp
⁡
(
−
c
0
​
𝔼
δ
​
[
L
]
)
≤
exp
⁡
(
−
c
0
​
C
​
𝖪
)
,
\Pr_{\delta}\!\left(L<\tfrac{1}{2}\mathsf{K}\right)\leq\Pr_{\delta}\!\left(L\leq\tfrac{1}{2}\mathbb{E}_{\delta}[L]\right)\leq\exp(-c_{0}\,\mathbb{E}_{\delta}[L])\leq\exp(-c_{0}C\mathsf{K}),
provided
C
​
𝖪
≥
a
0
C\mathsf{K}\geq a_{0}
. Choosing
C
C
large enough and absorbing constants yields
Pr
0
(
ϕ
𝖪
=
1
)
+
sup
KL
≥
C
​
𝖪
Pr
δ
(
ϕ
𝖪
=
0
)
≤
e
−
𝖪
/
2
+
e
−
c
​
𝖪
≤
e
−
c
′
​
𝖪
\Pr_{0}(\phi_{\mathsf{K}}=1)+\sup_{\mathrm{KL}\geq C\mathsf{K}}\Pr_{\delta}(\phi_{\mathsf{K}}=0)\leq e^{-\mathsf{K}/2}+e^{-c\mathsf{K}}\leq e^{-c^{\prime}\mathsf{K}}
for universal constants
c
,
c
′
>
0
c,c^{\prime}>0
and all
𝖪
\mathsf{K}
above a universal constant.
This proves the claim.
∎
B.5
Proofs for Section
3.4
(Allocation Optimality)
This subsection provides proof sketches for Theorems
3.5
and
3.6
. Throughout, we reuse the KL divergence bounds from Lemma 3.1 and standard hypothesis testing inequalities (e.g., Bretagnolle–Huber). Constants are omitted when immaterial.
B.5.1
Proof of Theorem
3.5
(Minimax Optimality of Proportional Allocation)
Least-favorable alternative.
Fix a (possibly adaptive) allocation policy
π
\pi
producing counts
N
1
,
…
,
N
m
N_{1},\dots,N_{m}
with
∑
i
N
i
=
B
\sum_{i}N_{i}=B
. Let
i
⋆
∈
arg
⁡
min
i
∈
[
m
]
⁡
N
i
w
i
.
i^{\star}\in\arg\min_{i\in[m]}\frac{N_{i}}{w_{i}}.
Lemma B.2
(Least-favorable alternative)
.
For any allocation
(
N
i
)
(N_{i})
and signal budget
μ
2
>
0
\mu_{2}>0
, consider the randomized
alternative
δ
(
i
⋆
)
\delta^{(i^{\star})}
defined by
δ
i
=
{
+
μ
2
/
w
i
⋆
with probability
​
1
2
,
i
=
i
⋆
,
−
μ
2
/
w
i
⋆
with probability
​
1
2
,
i
=
i
⋆
,
0
otherwise
.
\delta_{i}=\begin{cases}+\sqrt{\mu_{2}/w_{i^{\star}}}&\text{with probability }\tfrac{1}{2},\ i=i^{\star},\\
-\sqrt{\mu_{2}/w_{i^{\star}}}&\text{with probability }\tfrac{1}{2},\ i=i^{\star},\\
0&\text{otherwise}.\end{cases}
Then
δ
(
i
⋆
)
∈
ℋ
1
​
(
μ
2
)
\delta^{(i^{\star})}\in\mathcal{H}_{1}(\mu_{2})
and, among all alternatives in
ℋ
1
​
(
μ
2
)
\mathcal{H}_{1}(\mu_{2})
, it minimizes the KL divergence accumulated under the
allocation
(
N
i
)
(N_{i})
up to universal constants.
Proof of Lemma
B.2
.
First, verify that
δ
(
i
⋆
)
∈
ℋ
1
​
(
μ
2
)
\delta^{(i^{\star})}\in\mathcal{H}_{1}(\mu_{2})
:
∑
i
=
1
m
w
i
​
δ
i
2
=
w
i
⋆
⋅
(
μ
2
/
w
i
⋆
)
2
=
w
i
⋆
⋅
μ
2
w
i
⋆
=
μ
2
.
✓
\sum_{i=1}^{m}w_{i}\delta_{i}^{2}=w_{i^{\star}}\cdot\left(\sqrt{\mu_{2}/w_{i^{\star}}}\right)^{2}=w_{i^{\star}}\cdot\frac{\mu_{2}}{w_{i^{\star}}}=\mu_{2}.\q

## Body offsets 65040–68400

h the likelihood-ratio testing argument of Appendix
B.4
, and is omitted for brevity. We outline the argument for the two-stage screening allocation.
Step 1: Screening accuracy.
In Stage 1, each prompt type is sampled
b
b
times. By Hoeffding’s inequality,
for
b
=
Ω
⁡
(
log
⁡
m
)
b=\Omega(\log m)
, the empirical estimates
δ
^
i
2
\hat{\delta}_{i}^{2}
uniformly
concentrate around
δ
i
2
\delta_{i}^{2}
with probability at least
1
−
η
1-\eta
.
Consequently, the set
S
^
q
\hat{S}_{q}
of the top
⌈
q
​
m
⌉
\lceil qm\rceil
empirical values
coincides with the oracle set
S
q
​
(
δ
)
S_{q}(\delta)
except on an event of probability
at most
η
\eta
.
Step 2: KL budget under correct screening.
Conditioned on correct screening, all Stage 2 samples are drawn from prompt
types in
S
q
​
(
δ
)
S_{q}(\delta)
. Applying Lemma 3.1 and linearity of KL,
the accumulated KL divergence in Stage 2 satisfies
KL
(
P
δ
π
∥
P
0
π
)
≥
c
B
2
μ
2
,
q
(
δ
)
,
\mathrm{KL}(P_{\delta}^{\pi}\,\|\,P_{0}^{\pi})\;\geq\;c\,B_{2}\,\mu_{2,q}(\delta),
where
B
2
B_{2}
is the remaining budget after screening.
Step 3: Error decomposition.
Decomposing on the screening event,
Pr
⁡
(
error
)
≤
Pr
⁡
(
screening fails
)
+
Pr
⁡
(
test fails
∣
screening succeeds
)
≤
η
+
exp
⁡
(
−
c
​
B
2
​
μ
2
,
q
​
(
δ
)
)
.
\Pr(\text{error})\;\leq\;\Pr(\text{screening fails})+\Pr(\text{test fails}\mid\text{screening succeeds})\;\leq\;\eta+\exp(-cB_{2}\mu_{2,q}(\delta)).
Taking expectation over
δ
∼
D
m
\delta\sim D^{m}
yields the stated bound. The comparison
to proportional allocation follows directly from Proposition 3.4.
Rates.
In particular, screening succeeds with probability at least
1
−
2
​
exp
⁡
(
−
c
1
​
b
)
1-2\exp(-c_{1}b)
for a universal constant
c
1
>
0
c_{1}>0
, and conditional on correct
screening, the Stage 2 test achieves total error at most
exp
⁡
(
−
c
2
​
B
2
​
μ
2
,
q
)
\exp(-c_{2}B_{2}\mu_{2,q})
for a universal constant
c
2
>
0
c_{2}>0
.
Thus, choosing
b
=
Θ
⁡
(
log
⁡
m
)
b=\Theta(\log m)
ensures that the screening overhead is
negligible relative to the exponential decay governed by
B
2
​
μ
2
,
q
B_{2}\mu_{2,q}
.
B.5.3
Two-Stage Screening Allocation Procedure
Algorithm 1
Two-Stage Screening Allocation
Input:
total budget
B
B
, screening budget per type
b
b
, retention fraction
q
q
Output:
decision on whether a detectable preference difference exists
Stage 1 (Screening):
for
i
=
1
i=1
to
m
m
do
Collect
b
b
judgments for prompt type
i
i
Compute empirical estimate
δ
^
i
\hat{\delta}_{i}
end
for
Let
S
^
q
\hat{S}_{q}
be the
⌈
q
​
m
⌉
\lceil qm\rceil
prompt types with largest
δ
^
i
2
\hat{\delta}_{i}^{2}
Stage 2 (Focusing):
Allocate remaining budget
B
−
m
​
b
B-mb
by sampling only prompt types in
S
^
q
\hat{S}_{q}
proportionally to their weights
w
i
w_{i}
Testing:
Apply a two-sided binomial or likelihood-ratio test using Stage 2 outcomes
Appendix C
Implications for Benchmark Design and Budget Planning
C.1
Empirical Verification of Two-Stage Allocation
We empirically verify the behavior of Algorithm
1
using a controlled simulation designed to isolate the role of prompt-type heterogeneity.
Simulation setup.
We consider
m
m
prompt types with weights
w
∈
Δ
m
w\in\Delta_{m}
. For each type
i
i
, judgments are drawn i.i.d. as
Y
∼
Bernoulli
⁡
(
1
2
+
δ
i
)
,
Y\sim\mathrm{Bernoulli}\!\left(\tfrac{1}{2}+\delta_{i}\right),
with total evaluation budget
B
B
. We compare
