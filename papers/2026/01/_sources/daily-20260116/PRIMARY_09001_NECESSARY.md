# 2601.09001v1 — minimum necessary primary core

Exact HTML: https://arxiv.org/html/2601.09001v1 . 以下仅已实际读的方法、决定性评价/直接反侧与必要复现字段；区段为HTML正文字符定位，非全文/附录完成声明。未执行实验或代码。

## Body 9557–11700

2
From Signatures to Accuracy Estimates
Building on evidence that token-probability traces carry information about response correctness
Malinin and Gales 2021
;
Kuhn et al. 2023
;
Ali et al. 2025
;
Bouchard et al. 2025a
, we study whether a cheap signal available at inference time can support domain-level performance monitoring in STEM reasoning. We summarize the model’s output uncertainty signature as the sequence of token-level entropies computed from next-token probabilities during generation.
Entropy from top-
k
k
log-probabilities.
For an input prompt
q
q
, let the model generate an output
y
^
=
(
y
1
,
…
,
y
T
)
\hat{y}=(y_{1},\ldots,y_{T})
. At decoding step
t
t
, let
p
(
t
)
​
(
⋅
)
p^{(t)}(\cdot)
denote the next-token distribution conditioned on the prompt and previously generated tokens
(
q
,
y
<
t
)
(q,y_{<t})
. Many APIs expose only top-
k
k
next-token probabilities at each step. We therefore approximate entropy by truncating the sum to the top-
k
k
tokens:
H
~
(
t
)
=
−
∑
i
∈
Top
​
-
​
k
p
(
t
)
i
log
p
(
t
)
i
\tilde{H}^{(t)}=-\sum_{i\in\mathrm{Top}\text{-}k}p^{(t)}_{i}\log p^{(t)}_{i}
, which differs from the true Shannon entropy because it omits the probability mass outside the Top-
k
k
set.
We use
H
~
(
t
)
\tilde{H}^{(t)}
as an uncertainty signal over the generated output tokens.
From instance correctness to domain accuracy.
Given a response
x
=
(
q
,
y
^
)
x=(q,\hat{y})
, we extract a feature vector from its entropy trajectory by
summarizing
{
H
~
(
t
)
}
t
=
1
T
\{\tilde{H}^{(t)}\}_{t=1}^{T}
with a small set of statistics (Sec.
3
),
and train a probabilistic classifier that outputs an estimated probability of correctness
P
^
​
(
x
)
∈
[
0
,
1
]
\hat{P}(x)\in[0,1]
.
For a domain (or slice)
D
D
represented by a set of instances
X
D
X_{D}
, we estimate its accuracy by
averaging predicted correctness probabilities:
A
^
​
(
D
)
=
1
|
X
D
|
​
∑
x
∈
X
D
P
^
​
(
x
)
.
\hat{A}(D)=\frac{1}{|X_{D}|}\sum_{x\in X_{D}}\hat{P}(x).
(1)
If
P
^
​
(
x
)
\hat{P}(x)
is well-calibrated, then
A
^
​
(
D
)
\hat{A}(D)
is a consistent estimator of the true domain accuracy,
making it suitable for continuous monito

## Body 19252–25900

4
Accuracy Estimation via Entropy Profile Features
Feature representation.
Given a prompt
q
q
and generated response
y
^
=
(
y
1
,
…
,
y
T
)
\hat{y}=(y_{1},\ldots,y_{T})
, we compute the output-entropy trajectory
{
H
~
(
t
)
}
t
=
1
T
\{\tilde{H}^{(t)}\}_{t=1}^{T}
from next-token probabilities logged during decoding, approximated with the top 20 logprobs (Sec.
2
,
3
). We compress this trajectory into an eleven-dimensional feature vector
𝐡
x
∈
ℝ
11
\mathbf{h}_{x}\in\mathbb{R}^{11}
for each instance
x
=
(
q
,
y
^
)
x=(q,\hat{y})
, where
𝐡
x
=
[
H
max
,
H
mean
,
H
std
,
H
Q
​
10
,
H
Q
​
25
,
H
Q
​
50
,
H
Q
​
75
,
H
Q
​
90
,
H
skew
,
H
kurt
,
H
SEA
]
\mathbf{h}_{x}=[H_{\max},\allowbreak H_{\text{mean}},\allowbreak H_{\text{std}},\allowbreak H_{Q10},\allowbreak H_{Q25},\allowbreak H_{Q50},\allowbreak H_{Q75},\allowbreak H_{Q90},\allowbreak H_{\text{skew}},\allowbreak H_{\text{kurt}},H_{\text{SEA}}]
. Each statistic is computed over
{
H
~
(
t
)
}
t
=
1
T
\{\tilde{H}^{(t)}\}_{t=1}^{T}
:
H
max
H_{\max}
,
H
mean
H_{\text{mean}}
, and
H
std
H_{\text{std}}
capture peak, central tendency, and dispersion;
H
Q
​
10
H_{Q10}
,
H
Q
​
25
H_{Q25}
,
H
Q
​
50
H_{Q50}
,
H
Q
​
75
H_{Q75}
, and
H
Q
​
90
H_{Q90}
are the 10th, 25th, 50th, 75th, and 90th percentiles;
H
skew
H_{\text{skew}}
and
H
kurt
H_{\text{kurt}}
measure skewness and kurtosis; while
H
SEA
H_{\text{SEA}}
measures the raw sum of the entropy trajectory.
Probabilistic model.
We map entropy features to an estimated probability of correctness with a lightweight probabilistic model
f
:
ℝ
11
→
[
0
,
1
]
f:\mathbb{R}^{11}\rightarrow[0,1]
, defining
P
^
​
(
x
)
=
f
​
(
𝐡
x
)
\hat{P}(x)=f(\mathbf{h}_{x})
,
where
P
^
​
(
x
)
\hat{P}(x)
estimates the probability a response is correct.
From instance probabilities to domain-level accuracy.
Given per-instance correctness probabilities
P
^
​
(
x
)
\hat{P}(x)
, we estimate accuracy on a target domain (or slice)
D
D
by averaging
P
^
​
(
x
)
\hat{P}(x)
over instances in
D
D
(Eq.
1
). This estimator requires only decoding-time log-probabilities at test time.
5
Experimental Setup
We test whether compact entropy-profile features support
domain-level
accuracy estimation under domain shift: train an instance-level correctness predictor on a small set of benchmarks, then estimate accuracy on unseen benchmarks by aggregating predicted correctness probabilities.
Benchmarks.
We evaluate on ten STEM reasoning benchmarks spanning math and science:
GSM8K
Cobbe et al. 2021
, SVAMP
Patel et al. 2021
, GSM-Symbolic
Mirzadeh et al. 2025
,
MATH
Hendrycks et al. 2021
, TheoremQA
Chen et al. 2023
, SciBench
Wang et al. 2023
,
MatSciBench
Zhang et al. 2025b
, OlympiadBench
He et al. 2024
,
LiveMathBench
Anonymous 2025
, and GPQA
Rein et al. 2023
.
All tasks use zero-shot chain-of-thought prompting with free-form final answers.
For benchmarks originally multiple-choice (GPQA, SciBench), we remove answer options from the prompt.
For OlympiadBench we restrict to text-only math and physics questions; for LiveMathBench we use the
v202505_all_en
subset.
2
2
2
https://huggingface.co/datasets/opencompass/LiveMathBench
When a split exists, we evaluate on the test portion; otherwise we evaluate on the full benchmark.
Instance labeling and prediction target.
Each benchmark instance provides a question
q
q
, a reference answer
y
⋆
y^{\star}
, and a model-generated response
y
^
\hat{y}
.
We extract the model’s final answer from
y
^
\hat{y}
using benchmark-specific post-processing (e.g., stripping
formatting and selecting the last boxed/numeric expression when applicable).
An external
validator
LLM (
Grok-4.1-Fast-Reasoning
xAI 2025
) receives
(
q
,
y
^
final
,
y
⋆
)
(q,\hat{y}_{\text{final}},y^{\star})
and outputs a binary label
z
∈
{
0
,
1
}
z\in\{0,1\}
indicating whether the final answer matches the reference; a manual audit of 100 randomly sampled instances yielded
97
%
97\%
agreement with human judgment. We treat
z
z
as supervision for our probabilistic correctness predictor.
Extremes
Intermediate
Model
AEE
ρ
\rho
AEE
ρ
\rho
Phi-3.5-Mini
(3.6B)
0.03
1.00
0.06
0.95
Ministral3
(3B)
0.06
0.96
0.11
0.79
Ministral3
(8B)
0.07
0.96
0.12
0.89
Qwen3
(4B)
0.08
0.95
0.11
0.94
Qwen3
(8B)
0.12
0.76
0.17
0.75
Gemma3
(4B)
0.09
0.94
0.14
0.92
Gemma3
(12B)
0.08
0.92
0.12
0.85
Llama-3.1
(8B)
0.07
0.95
0.11
0.92
GPT-OSS
(20B)
0.15
0.90
0.16
0.89
Table 2:
Cross-domain accuracy estimation with two
a priori
training sets—
Extremes
(GSM8K+OlympiadBench) and
Intermediate
(MATH+SciBench)—using a calibrated, class-balanced random forest.
ρ
\rho
: Spearman correlation.
Models.
We evaluate nine LLMs (3B-20B–six families) , and restrict features to top-20 decoding logprobs,
matching a common interface constraint in logprob-returning serving stacks.
We run the full pipeline separately for Ministral-3 3B
Mistral AI 2025
, Phi-3.5-Mini 3.8B
Microsoft 2024
, Qwen-3 4B
Qwen Team 2025
,
Gemma-3 4B
Google DeepMind 2025
, Qwen-3 8B, Ministral-3 8B, Llama-3.1 8B
Meta AI 2024
,
Gemma-3 12B, and GPT-OSS 20B
OpenAI 2025
.
Train/test sweep for domain shift.
To avoid conclusions tied to a single split, we vary which benchmarks provide supervision.
For each
k
∈
{
1
,
2
,
3
,
4
}
k\in\{1,2,3,4\}
and each benchmark subset
G
G
of size
k
k
(in total
∑
k
=
1
4
(
10
k
)
=
385
\sum_{k=1}^{4}\binom{10}{k}=385
groups),
we train a correctness predictor on instances from
G
G
and evaluate accuracy estimation on the remaining
10
−
k
10-k
benchmarks.
This yields an OOD setting where all test domains are disjoint from the supervision set.
Estimators and ablations.
We evaluate three classifiers on the 11D entropy-profile features:
logistic regression with
ℓ
1
\ell_{1}
regularization, random forest, and a multilayer perceptron (MLP).
For each classifier, we select hyperparameters via cross-validated grid search on the training group, optimizing ROC-AUC.
We also vary two training choices: class balancing (on/off) and isotonic calibration (on/off).
Across 9 models, 385 groups, 3 classifier families, and 2
×
\times
2 training options, this produces
9
×
385
×
3
×
4
=
41,580
9\times 385\times 3\times 4=41{,}580
configurations.
Domain-level evaluation metrics.
For each held-out benchmark/domain
D
D
, we estimate accuracy by averaging per-instance correctness probabilities
(Eq.
1
). We report: (i) accuracy estimation error
(AEE)
, mean absolute error between estimated and
true benchmark accuracies over held-out domains; and (ii)
Spearman correlation
ρ
\rho
between estimated and true accuracies,
capturing whether the estimator ranks domains for data acquisition.
Implementation.
All LLMs are served with vLLM
Kwon et al. 2023
(seed 42) with a 

## Body 27368–34300

RQ1: Accuracy estimation under deployment-plausible defaults.
We first report two training configurations chosen
a priori
for plausibility rather than tuned for best score.
Results here use a random forest correctness estimator trained with class balancing and isotonic calibration on
Extremes
(GSM8K + OlympiadBench), spanning elementary-to-competition difficulty, and
Intermediate
(MATH + SciBench)
Table
2
and Figure
3
report cross-domain accuracy estimation quality.
First, difficulty-spanning supervision is consistently stronger:
under Extremes, seven of nine models achieve
ρ
≥
0.90
\rho\geq 0.90
with low error (AEE
0.03
0.03
–
0.12
0.12
),
while Intermediate yields systematically higher error and weaker ordering (AEE
0.06
0.06
–
0.17
0.17
;
ρ
\rho
drops for all models).
Second, the signal is model-dependent: for
Phi-3.5-Mini
we observe near-perfect ordering
(AEE
0.03
0.03
,
ρ
=
1.00
\rho{=}1.00
), whereas
Qwen3-8B
exhibits weaker agreement in both settings
(AEE
0.12
0.12
–
0.17
0.17
,
ρ
≈
0.75
\rho\approx 0.75
).
Overall, both choices generalize out of domain for most LLMs (Table
2
). However, Extremes is consistently stronger, achieving lower AEE and higher rank agreement
ρ
\rho
across models, while Intermediate incurs a systematic degradation. Additional examples under alternative training groups and estimator variants are reported in Appendix
D
.
RQ2: Baseline UQ metrics for performance monitoring.
We compare our entropy-based accuracy estimator against nine standard white-box uncertainty metrics in Sec.
3
, defined in Appendix
A
. Because these metrics are not trained to predict accuracy (they return an uncertainty score rather than a calibrated correctness probability), we evaluate them in the most comparable way for monitoring: for each held-out domain, we aggregate each metric over instances to obtain a domain-level score, and report Spearman correlation
ρ
\rho
between that score and the domain’s true accuracy. Table
4
summarizes results across models. In terms of raw correlation values, the best white-box metrics are in the same ballpark as our estimator—often within a few
ρ
\rho
points—so they can track domain-to-domain fluctuations reasonably well. That said, our method is consistently as good as, and in most settings slightly better than, the strongest uncertainty baselines in Table
4
, and it additionally supports a priori monitoring with calibrated, domain-level accuracy estimates as reported in Table
2
; the baselines do not directly yield comparable predictions there, since they produce only uncalibrated scores.
Model
Ext.
Int.
SEA
SE
max
\text{SE}_{\text{max}}
SE
mean
\text{SE}_{\text{mean}}
NLL
avg
\text{NLL}_{\text{avg}}
NLL
max
\text{NLL}_{\text{max}}
LNTP
MTP
PPL
phi-3.5-mini
(3B)
1.00
0.95
0.95
0.94
0.90
0.90
0.88
0.90
0.89
0.90
qwen3
(4B)
0.95
0.94
0.96
0.98
0.95
0.95
0.96
0.95
0.98
0.95
qwen3
(8B)
0.76
0.75
0.93
0.79
0.75
0.75
0.89
0.75
0.95
0.75
ministral3
(3B)
0.96
0.79
0.96
0.95
0.92
0.68
0.61
0.66
0.55
0.68
ministral3
(8B)
0.96
0.89
0.98
0.96
0.96
0.66
0.47
0.62
0.73
0.73
gemma3
(4B)
0.94
0.92
0.89
0.89
0.87
0.87
0.89
0.87
0.98
0.87
gemma3
(12B)
0.92
0.85
0.90
0.88
0.81
0.84
0.93
0.84
0.95
0.83
llama-3.1
(8B)
0.95
0.92
0.95
0.95
0.55
0.65
0.90
0.65
1.00
0.65
gpt-oss
(20B)
0.90
0.89
0.94
0.98
0.82
0.58
0.37
0.50
0.70
0.50
Table 4:
Spearman
ρ
\rho
between aggregated UQ baselines and true domain accuracy on held-out benchmarks.GSM8K+OlympiadBench; Int.: MATH+SciBench.
S
​
E
​
A
SEA
and
S
​
E
max
SE_{\text{max}}
are consistently strong, often comparable to our defaults.
RQ3: Training composition dominates (and improves with
k
k
).
We next quantify how accuracy estimation depends on the composition of the supervision set.
Table
3
aggregates results over all training groups of size
k
∈
{
1
,
2
,
3
,
4
}
k\in\{1,2,3,4\}
(and over classifier configurations), reporting the median AEE and its interquartile range (IQR).
Increasing
k
k
produces two consistent effects across all nine LLMs:
typical error decreases monotonically with
k
k
, and robustness to benchmark choice improves sharply (IQR shrinks).
At
k
=
1
k{=}1
, median AEE is high (roughly
0.20
0.20
–
0.27
0.27
) and highly variable across which single benchmark provides supervision;
by
k
=
4
k{=}4
, median AEE improves substantially (roughly
0.06
0.06
–
0.16
0.16
) and variability compresses to IQR
≈
0.03
\approx 0.03
–
0.04
0.04
.
Thus, benchmark choice is a first-order design decision at small
k
k
, but becomes less brittle as supervision spans more tasks.
Difficulty balance explains much of the composition effect.
To make the composition dependence interpretable, we summarize each training group by its weighted average accuracy
(the average
A
⁡
(
D
)
A(D)
over
D
∈
G
D\in G
, weighted by instance counts) and relate it to held-out estimation quality.
Figure
4
(and Appendix
F
for all models)
shows a U-shaped relationship: supervision sets that are too easy or too hard generalize worse,
whereas groups with intermediate weighted accuracy (roughly
0.4
0.4
–
0.6
0.6
) yield the lowest AEE.
A interpretation is that intermediate-weighted groups tend to mix easy and hard benchmarks, exposing the estimator to
both low-entropy success patterns and high-entropy failure patterns; in contrast, easy-only or hard-only groups underrepresent one side
of this spectrum and miscalibrate when transferred to unseen difficulty regimes. Difficulty-diverse training sets outperform difficulty-homogeneous ones: all-easy groups underrepresent high-entropy failure patterns from hard domains, while all-hard groups underrepresent low-entropy success patterns. Mixed (easy+hard) groups expose the estimator to a broader range of entropy profiles, which aligns with better OOD generalization. We analyze the best/worst benchmark combinations and a leave-one-out sensitivity study in Appendix
F
.
RQ4: Estimator choices matter, but less than data composition.
We isolate estimator design effects by aggregating across training groups and models.
Table
5
reports main effects on median AEE and Spearman correlation.
Random forests perform best in this low-dimensional setting (11 entropy features); logistic regression is close, while MLPs are consistently worse, consistent with overfitting under limited supervision.
Isotonic calibration provides a modest but consistent gain (0.12 vs. 0.14 median AEE), which matters because we aggregate probabilities.
Class balancing has little net effect and can slightly hurt, suggesting failures are driven more by entropy-pattern shift than label imbalance.
Across all configurations, Spearman remains stable (
ρ
≈
0.94
\rho\approx 0.94
), indicating the
ranking
of benchmark difficulty is robust and that most variation comes from training-data composition rather than estimator choices.
Feature Selection.
Across ablations the full 11D profile is a strong, stable default, but it is not universally best. In particular, some smaller combinatio

## Body 38923–41300

9
Limitations
Controlled domain: verifiable STEM reasoning.
Our experiments focus on ten STEM benchmarks with relatively well-defined correctness criteria and zero-shot prompting.
This enables large-scale, exhaustive train/test sweeps, but it also limits external validity:
open-ended tasks (e.g., creative writing, dialogue, summarization) do not admit a single gold answer.
Top-
k
k
entropy is an approximation.
We approximate Shannon entropy using only top-
k
k
probabilities (top-20), omitting tail mass.
This truncation can change the scale and shape of entropy traces, especially for high-entropy steps where probability
mass is more diffuse. While this choice is motivated by API constraints, it may degrade performance compared to full-vocab
entropy and can vary across tokenizers and model families.
Sensitivity to decoding and formatting.
Entropy traces depend on decoding choices (temperature, max length, stop criteria) and on the model’s tendency to produce
longer chain-of-thought or verbose explanations. Changes in prompting (e.g., instructing shorter solutions), answer
formatting, or post-processing rules can shift entropy distributions without reflecting true capability changes.
Model dependence and post-training effects.
We observe that reliability varies across LLMs and can differ even within a family (e.g., size variants).
One plausible factor is post-training (instruction tuning, RLHF/RLAIF, safety finetuning), which can decouple confidence
signals from correctness. Consequently, our findings do not guarantee that entropy profiles will yield well-calibrated
accuracy estimates for a new target model without empirical validation.
Actionability beyond ranking.
While Spearman
ρ
\rho
indicates that we can often rank domains by difficulty, absolute accuracy estimation error (AEE)
remains non-trivial for some models, and miscalibration can persist even under large supervision (e.g., strong ranking but
systematic offset). In operational settings, this suggests using the method primarily for
prioritization
(which slices
to inspect or label) and coupling it with targeted evaluation before high-stakes interventions.
References
Ahdritz et al. (2024)
Gustaf Ahdritz, Tian Qin, Nikhil Vyas, Boaz Barak, and Benjamin L. Edelman.
2024.
Distinguishing the knowable from the unknowable with language models.
arXiv preprint arXiv:2402.03563
.
Alain and

## Body 55200–58800

 discriminative metrics.
Appendix C
Additional details for Reproducibility
To ensure reproducibility across the ten STEM reasoning benchmarks and nine LLMs, we provide the specific prompts used for model generation and external validation. All benchmarks utilized zero-shot chain-of-thought (CoT) prompting.
C.1
Model Generation Prompt
We used the instruct-tunes of every LLM version ran through vLLM
Kwon et al. 2023
, utilizing a single user prompt without a system message to maintain consistency across open and closed-source families:
Solve the following problem step by step, then provide the final numerical answer.
Question: {question}
Solution:
C.2
Evaluation and Verification Prompt
Ground-truth correctness labels were produced using
Grok-4.1-Fast-Reasoning
xAI 2025
via the LiteLLM API as an external validator. The validator receives the original question, the model’s response, and the reference ground-truth answer, then outputs a structured binary decision using a Pydantic response schema (
class Response(BaseModel): success: bool
).
The system prompt instructs the validator to determine answer equivalence under benchmark-specific criteria (e.g., symbolic or numeric equivalence):
System:
Task: Determine if the Response corresponds to the Correct Answer for the Question, based on the given Correct Answer text. Answer ONLY with the exact format: {"success": True} or {"success": False}
The user prompt provides the evaluation context:
User:
# Question
{question}
# Response
{cleaned_response}
# Correct Answer
{correct_answer}
Responses are preprocessed by removing special tokens (e.g.,
<|end|>
,
<|endoftext|>
) before validation. The structured Pydantic output ensures consistent binary classification across all 385 training configurations and benchmark evaluations.
C.3
Classifier Hyperparameter Grid
All hyperparameters are selected via a 5 fold cross-validated grid search on the training group, optimizing ROC-AUC. For logistic regression (
ℓ
1
\ell_{1}
penalty,
liblinear
solver), we search
C
∈
{
0.5
,
2.0
,
10.0
}
C\in\{0.5,2.0,10.0\}
. For random forests (100 estimators), we search max depth
∈
{
3
,
5
,
10
}
\in\{3,5,10\}
and min samples split
∈
{
2
,
5
,
10
}
\in\{2,5,10\}
. For MLPs (ReLU activations, early stopping,
α
=
0.001
\alpha=0.001
), we search hidden layer sizes
∈
{
(
5
)
,
(
8
)
,
(
10
)
,
(
15
)
,
(
20
)
,
(
8
,
4
)
,
(
10
,
5
)
,
(
15
,
8
)
}
\in\{(5),(8),(10),(15),(20),(8,4),(10,5),(15,8)\}
.
C.4
Class Balancing Techniques
We evaluate each classifier with and without class balancing using scikit-learn’s built-in mechanisms. Logistic regression uses
class_weight="balanced"
, reweighting the loss inversely proportional to class frequencies. Random forests use
class_weight="balanced_subsample"
, reweighting within each bootstrap sample. For MLPs, which lack native class weighting, we apply random oversampling via
RandomOverSampler
from imbalanced-learn
3
3
3
https://imbalanced-learn.org/stable/
prior to training.
Appendix D
Additional Classifier Configuration Results
We include two additional classifier configurations based on sensible
a priori
defaults, all utilizing class balancing and isotonic calibration. Each configuration represents a plausible practitioner choice without access to exhaustive hyperparameter search.
Cross-Domain Linear Estimator.
We train a logistic regression on
MatSciBench
(intermediate difficulty, materials science) paired with
GSM-Symbolic
(elementary difficulty, symbolic perturbations of GSM8K). This configuration tests whether a simple linear model can generalize across domains when trained on ben
