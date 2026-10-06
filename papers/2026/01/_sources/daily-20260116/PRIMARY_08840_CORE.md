# Exact-v1 primary necessary core

Source: https://arxiv.org/html/2601.08840v1

nowledge.
IV 
Method
In this section, we introduce a consistency-aware editing method for entity-level unlearning.
IV-A
Unlearning with Parameters Shift in MLP 
As introduced at Equation (
2
), in each individual layer 
ℓ
\ell
, we want to erase all knowledge related to a given entity.
Thus, we denote the input for the 
ℓ
\ell
-th MLP as 
K
∗
K_{*}
 and the output as 
M
∗
M_{*}
. Specifically, we define
K
r
=
{
k
1
r
,
…
,
k
n
r
}
∈
ℝ
d
×
n
K_{r}=\{k_{1}^{r},\ldots,k_{n}^{r}\}\in\mathbb{R}^{d\times n}
 as the key matrix used to preserve the model’s general behavior, sampled independently from the forget set;
M
r
=
{
m
1
r
,
…
,
m
n
r
}
∈
ℝ
d
×
n
M_{r}=\{m_{1}^{r},\ldots,m_{n}^{r}\}\in\mathbb{R}^{d\times n}
 as the associated value for 
K
r
K_{r}
;
K
f
=
{
k
1
f
,
…
,
k
u
f
}
∈
ℝ
d
×
u
K_{f}=\{k_{1}^{f},\ldots,k_{u}^{f}\}\in\mathbb{R}^{d\times u}
 as the key matrix for the forget set related to same entity; and
M
f
=
{
m
1
f
,
…
,
m
u
f
}
∈
ℝ
d
×
u
M_{f}=\{m_{1}^{f},\ldots,m_{u}^{f}\}\in\mathbb{R}^{d\times u}
 as the associated values for 
K
f
K_{f}
.
The unlearning objective can then be reformulated as a modification of the 
ℓ
\ell
-th 
W
o
​
u
​
t
W_{out}
 parameters 
W
W
 in MLP, by introducing a perturbation 
Δ
\Delta
 at each layer. The goal is to find 
Δ
\Delta
 such that:
Δ
=
arg
⁡
min
Δ
^
⁡
(
‖
(
W
+
Δ
^
)
​
K
f
−
M
f
‖
2
+
‖
(
W
+
Δ
^
)
​
K
r
−
M
r
‖
2
)
,
\Delta=\arg\min_{\widehat{\Delta}}(\|(W+\widehat{\Delta})K_{f}-M_{f}\|^{2}+\|(W+\widehat{\Delta})K_{r}-M_{r}\|^{2}),
(3)
where 
∥
⋅
∥
2
\|\cdot\|^{2}
 denotes the sum of the squared elements in the matrix. The first term enforces the removal of factual associations for the entity, while the second term ensures the model’s general behavior is preserved.
We can solve Equation (
3
) by applying the normal equation. To this aim, we define 
R
=
M
f
−
W
​
K
f
R=M_{f}-WK_{f}
 and 
W
​
K
r
=
M
r
WK_{r}=M_{r}
. Then, Equation (
3
) can be rewritten as:
Δ
=
R
​
K
f
T
​
(
K
r
​
K
r
T
+
K
f
​
K
f
T
)
−
1
.
\Delta=RK_{f}^{T}(K_{r}K_{r}^{T}+K_{f}K_{f}^{T})^{-1}.
(4)
Therefore, to compute 
Δ
\Delta
, we need to obtain the residual error 
R
R
 and the key 
K
f
K_{f}
 of the unlearning data, along with an estimated key matrix 
K
r
K_{r}
 for the retain set.
In practice, following prior work 
[
24
, 
25
]
, we approximate 
K
r
​
K
r
T
K_{r}K_{r}^{T}
 by computing the empirical covariance over a sample of 100,000 random triplets from Wikipedia.
In the following section, we describe how the forget keys 
K
f
K_{f}
 and the residuals 
R
R
 are constructed for entity-level unlearning.
Fig. 3
: 
Overview of our method
(a) Given an entity 
e
e
 (e.g., Jackie Chan), we retrieve facts from Wikidata and convert them into natural language 
T
e
T_{e}
, followed by rephrasing into 
T
g
T_{g}
. The union of 
T
e
T_{e}
 and 
T
g
T_{g}
 is the input of CAE.
(b) For each prompt, we extract key vectors and optimize a residual 
δ
\delta
 at layer 
ℓ
\ell
.
The key vectors are selected via SVD-based ranking, while the residuals are regularized using a consistency loss to ensure aligned updates across prompts. We then distribute the residuals 
R
ℓ
R^{\ell}
 across subsequent layers.
IV-B
Key Matrix of Entity Knowledge
Unlike in typical model editing settings where precise input-output pairs are provided for a fact to be modified, entity-level unlearning is given only the entity name along with a few probing questions.
Consequently, a key challenge in constructing the key matrix for the forget set is generating a diverse and representative set of inputs that sufficiently capture the entity’s associated knowledge.
To address this, as shown in Figure 
3
, we first retrieve a range of one-hop facts about the target entity 
e
e
 from Wikidata
2
2
2
https://query.wikidata.org
, categorized by their semantic types.
We then convert these structured triples into natural language prompts using predefined templates. This yields a base set 
T
e
=
{
t
1
,
…
,
t
E
}
T_{e}=\{t_{1},\ldots,t_{E}\}
, where 
E
E
 is the number of inputs.
To further enhance linguistic diversity and improve coverage of the entity’s knowledge representation, we apply a text generation model to paraphrase these prompts, resulting in an augmented set 
T
g
=
{
t
1
,
…
,
t
E
}
T_{g}=\{t_{1},\ldots,t_{E}\}
.
Our final input set for unlearning is defined as 
T
in
=
T
e
∪
T
g
T_{\mathrm{in}}=T_{e}\cup T_{g}
.
For each prompt 
x
j
∈
T
in
x_{j}\in T_{\mathrm{in}}
 at layer 
ℓ
\ell
, we compute its corresponding key vector for the 
t
t
-th token as:
k
j
ℓ
=
key
ℓ
​
(
x
j
)
=
σ
⁡
(
W
in
ℓ
​
γ
​
(
h
ℓ
−
1
j
​
[
t
]
)
)
,
k_{j}^{\ell}\;=\;\mathrm{key}_{\ell}(x_{j})\;=\;\sigma\bigl(W_{\mathrm{in}}^{\ell}\,\gamma(h_{\ell-1}^{j}[t])\bigr),
(5)
where 
γ
\gamma
 represents an intermediate nonlinearity, and 
σ
\sigma
 is the activation function of the MLP.
We focus on the last subject token as the 
t
t
-th token and discuss the results on editing last token in Section 
V-D3
.
However, some prompts in 
T
i
​
n
T_{in}
 may be redundant or induce conflicting updates.
To select a compact and informative subset,
we compute its SVD, 
𝐊
f
ℓ
=
U
​
Σ
​
V
⊤
\mathbf{K}_{f}^{\ell}=U\Sigma V^{\top}
.
We then project each 
k
j
ℓ
k_{j}^{\ell}
 onto the top-
r
r
 left singular vectors 
U
:
,
1
:
r
U_{:,1:r}
 and score it by
score
(
j
)
=
∥
U
:
,
1
:
r
⊤
k
j
ℓ
∥
2
.
\mathrm{score}(j)=\bigl\|U_{:,1:r}^{\top}k_{j}^{\ell}\bigr\|_{2}.
We sort by score and retain the top-
r
r
 keys whose cumulative projection energy exceeds a threshold 
τ
\tau
 (e.g., 95%).
The final set 
K
f
ℓ
=
{
k
1
ℓ
,
…
,
k
r
ℓ
}
K_{f}^{\ell}=\{k_{1}^{\ell},\dots,k_{r}^{\ell}\}
 consists of these top-scoring key vectors.
IV-C
Consistency Constrains for Residuals
In the absence of access to the output value matrix 
M
f
M_{f}
, we do not explicitly construct it for entity-level unlearning.
Instead, for each prompt 
x
j
∈
T
in
x_{j}\in T_{\mathrm{in}}
, we optimize a small residual vector 
δ
j
∈
ℝ
d
\delta_{j}\in\mathbb{R}^{d}
, which is added to the hidden state at layer 
L
L
, denoted by 
h
L
j
h_{L}^{j}
.
This residual 
δ
j
\delta_{j}
 is designed to suppress the entity’s factual associations without requiring reconstruction of 
M
f
M_{f}
.
While the relation 
R
=
M
f
−
W
​
K
f
R=M_{f}-WK_{f}
 allows us to recover 
K
f
K_{f}
, the corresponding output values 
M
f
M_{f}
 remain inaccessible.
Consequently, we directly modify the hidden representation by applying the residual: 
h
L
j
+
δ
j
h_{L}^{j}+\delta_{j}
.
A natural starting point is to minimize the loss 
ℒ
NLL
\mathcal{L}_{\mathrm{NLL}}
[
25
]
ℒ
NLL
=
1
r
∑
j
=
1
r
−
log
Pr
(
o
null
∣
x
j
;
h
L
j
+
δ
j
)
,
\mathcal{L}_{\mathrm{NLL}}=\frac{1}{r}\sum_{j=1}^{r}-\log\Pr\bigl(o^{\mathrm{null}}\mid x_{j};h_{L}^{j}+\delta_{j}\bigr),
(6)
where 
r
r
 is the size of 
T
i
​
n
T_{in}
. However, optimizing 
ℒ
NLL
\mathcal{L}_{\mathrm{NLL}}
 alone often fails to fully suppress the target fact as some prompts or paraphrases may still elicit the original information.
In practice, the updates induced by individual prompts can be misaligned, pointing in conflicting directions that do not span the full “knowledge subspace” associated with the entity.
As a result, certain factual attributes may persist despite the intervention.
To address this, we add a global consistency constraint that aligns all residuals toward a common update:
ℒ
Cons
=
λ
cons
∥
(
h
L
j
+
δ
j
)
−
1
j
−
1
∑
k
=
1
j
−
1
(
h
L
k
+
δ
k
)
∥
2
2
.
\mathcal{L}_{\mathrm{Cons}}=\lambda_{\mathrm{cons}}\,\Bigl\lVert(h_{L}^{j}+\delta_{j})-\frac{1}{j-1}\sum_{k=1}^{j-1}(h_{L}^{k}+\delta_{k})\Bigr\rVert_{2}^{2}.
(7)
This penalty encourages consistency across residuals 
δ
j
\delta_{j}
 by keeping each modified activation 
h
L
j
+
δ
j
h_{L}^{j}+\delta_{j}
 close to their mean.
In effect, it reduces the variance of updates across the prompt set, preventing individual residuals from conflicting with or negating one another.
As a result, all 
δ
j
\delta_{j}
 contribute coherently, enabling a more consistent and comprehensive erasure of the target entity’s knowledge.
Finally, for each 
δ
j
\delta_{j}
, we optimize the combined objective:
δ
j
=
arg
⁡
min
δ
⁡
(
ℒ
NLL
+
ℒ
Cons
)
.
\delta_{j}=\arg\min_{\delta}\bigl(\mathcal{L}_{\mathrm{NLL}}+\mathcal{L}_{\mathrm{Cons}}\bigr).
(8)
By coordinating updates in this manner, we achieve a more comprehensive and uniform erasure of entity knowledge across all prompts. Following optimization, we collect the edited representations and their corresponding keys at layer 
L
L
 into the matrix 
R
=
{
δ
1
,
;
…
,
;
δ
r
}
R=\bigl\{\delta_{1},;\dots,;\delta_{r}\bigr\}
, which serves as the value component in the weight update. The resulting parameter shift for layer 
L
L
 is then computed using Equation (
4
).
IV-D
Multi‐Layer Key Extraction and Weight Updates
The procedure above outlines how to update a single MLP layer. However, modifying one layer inevitably influences all subsequent activations. To propagate the editing effect and ensure consistent suppression of the entity’s influence in higher layers,
we follow 
[
25
]
 and apply updates with:
Residual Distribution.
We distribute residual 
δ
j
\delta_{j}
 over the remaining layers 
{
ℓ
,
ℓ
+
1
,
…
,
L
}
\{\ell,\ell+1,\ldots,L\}
:
r
j
ℓ
=
δ
j
L
−
ℓ
+
1
,
R
f
ℓ
=
{
r
1
ℓ
,
…
,
r
r
ℓ
}
.
r_{j}^{\ell}=\frac{\delta_{j}}{L-\ell+1},\qquad R_{f}^{\ell}=\{\,r_{1}^{\ell},\dots,r_{r}^{\ell}\,\}.
(9)
Closed‑Form Update.
Finally, at layer 
ℓ
\ell
, we compute the parameter shift using Equation (
4
) and subsequently update the layer’s weights:
W
out
ℓ
←
W
out
ℓ
+
Δ
ℓ
.
W_{\mathrm{out}}^{\ell}\;\l

12.2
125.5
73.2
NPO (LoRA)
75.1
64.3
69.0
69.7
91.3
82.2
86.7
225.1
227.0
64.9
41.7
36.0
54.0
707.3
114.2
58.5
RT (Full)
72.7
13.4
22.8
33.1
86.9
45.6
67.4
222.7
226.6
65.4
41.4
34.9
59.3
588.1
122.7
67.2
RT (LoRA)
85.4
49.6
53.2
60.5
87.3
74.1
81.9
226.0
223.9
64.5
41.2
33.6
58.2
667.0
115.9
60.7
MEMIT
29.7
18.6
31.4
26.6
80.7
72.0
76.4
243.0
230.0
66.0
40.0
40.0
52.8
709.0
130.3
74.9
AlphaEdit
62.7
52.6
58.9
58.1
85.1
83.0
84.1
233.0
230.0
65.6
40.4
39.6
53.0
708.0
119.0
63.0
EMMET
28.2
22.6
36.1
29.0
82.7
77.0
79.9
242.0
230.0
65.7
39.6
40.2
52.3
708.0
129.7
75.4
CAE
18.2
7.4
22.0
15.9
79.8
64.5
72.2
275.0
230.0
65.4
38.7
40.4
52.1
708.0
133.4
78.1
Llama3.1-Instruct (8B)
Before
67.5
68.1
68.1
67.9
82.0
77.3
79.7
215.0
219.0
66.1
45.2
39.5
55.3
694.0
115.8
55.9
ICU
21.8
5.3
9.0
12.0
32.6
6.1
19.4
237.0
254.0
64.1
27.0
37.7
36.8
695.0
114.5
53.7
GA (Full)
37.2
29.7
43.6
36.9
77.2
74.1
75.6
248.3
219.8
65.9
42.4
39.7
55.4
689.2
126.8
69.4
GA (LoRA)
60.2
55.8
61.4
59.1
79.8
76.4
78.1
223.7
221.5
65.5
40.9
39.2
55.8
684.0
117.4
59.5
DPO (Full)
39.8
32.3
36.4
36.2
54.7
47.6
51.1
234.9
229.1
65.6
42.9
32.4
20.1
727.1
110.5
57.5
NPO (Full)
27.6
18.6
21.5
22.5
67.4
64.6
66.0
249.8
226.4
65.6
41.3
38.5
53.5
674.6
128.9
71.7
NPO (LoRA)
64.3
62.4
64.6
63.8
79.8
76.3
78.0
217.5
219.0
65.7
41.6
39.5
54.8
688.6
115.6
57.1
RT (Full)
16.8
15.0
12.7
14.8
24.3
38.4
31.3
215.3
218.3
65.7
40.6
38.8
29.9
569.6
114.2
58.2
RT (LoRA)
54.5
50.9
47.5
50.9
65.3
67.7
66.5
215.2
218.3
65.6
41.6
38.5
42.8
653.1
113.4
57.8
MEMIT
30.5
23.6
41.6
31.9
74.5
69.8
72.2
228.0
219.0
65.8
47.1
38.3
56.8
693.0
129.3
70.1
AlphaEdit
64.6
58.8
63.8
62.4
82.0
76.9
79.5
216.0
219.0
66.0
45.5
39.6
55.5
695.0
118.1
58.5
EMMET
36.1
29.0
45.2
36.8
77.6
71.9
74.8
225.0
219.0
65.8
45.6
39.0
55.4
695.0
127.3
69.0
CAE
18.7
12.4
28.4
19.8
64.5
64.8
64.7
257.0
219.0
66.0
45.1
39.6
55.2
695.0
132.4
72.4
TABLE I
: 
Overall performance comparison across unlearning methods on RWKU (100 subjects).
Mean is a weighted average of Forget (0.4), Neighbor (0.2), Utility (0.3), and MIA (0.1).
All is the average value of FB, QA and AA.
Mean
_
\_
FN is the simple average of Forget (All) and Neighbor (All).
V 
Experiments
To evaluate the effectiveness of CAE, we investigate the following research questions:
•
RQ1:
 How does CAE perform on standard unlearning benchmarks compared with existing editing-, training-, and prompt-based baselines?
•
RQ2:
 How robust is CAE across diverse unlearning scenarios, including different entities, question types, and sequential multi-entity forgetting?
•
RQ3:
 How do factors such as data scale, number of edits, and token-level selection affect the effectiveness and side effects of CAE?
•
RQ4:
 How do the internal mechanisms of CAEs, particularly the consistency constraint, underpin edits that are stable, leakage-resistant, and geometrically coherent?
•
RQ5:
 How well does CAE generalize across model architectures and alternative data sources, such as LLM-generated synthetic examples?
V-A
Experimental Setup
Datasets and Models.
We evaluate forgetting performance on two entity-level benchmarks: RWKU 
[
11
]
 and ToFU 
[
23
]
, which contain 100 and 20 entities targeted for removal, respectively.
We focus on the single-entity unlearning setting, where each experiment targets the removal of one entity at a time.
Final results are reported as the average performance across all individual unlearning cases.
It is worth noting that our primary focus is on the single-entity unlearning setting, where each experiment removes one entity at a time. We also evaluate sequential unlearning to demonstrate the method’s effectiveness in handling multiple, successive entity removals.
This yields
100 and 20 separately edited models for RWKU and ToFU, respectively, and we evaluate the performance of each individually.
For ToFU, we evaluate on the 10% forget set.
Final results are reported as the average across all unlearning instances.
Experiments are conducted on LLaMA3-Instruct (8B) and LLaMA3.1-Instruct (8B) from HuggingFace. LLaMA2-7B-Chat is a fine-tuned model on the ToFU dataset.
3
3
3
https://huggingface.co/open-unlearning/tofu_Llama-2-7b-chat-hf_full
All editing methods are executed on two NVIDIA A100 GPUs (40GB each).
Since RWKU does not provide official results for LLaMA3.1-Instruct (8B), we additionally train this model using four NVIDIA A800 GPUs (80G).
The consistency weight 
λ
c
​
o
​
n
​
s
\lambda_{cons}
in Eq. 
7
 is set to 0.05.
Evaluation Metrics.
For RWKU, following previous work 
[
11
]
, we evaluate unlearning performance from four perspectives. 
(1) 
Forget set
: includes 
fill-in-the-blank (FB)
 probes, 
question-answer (QA)
 probes, and 
adversarial attack (AA)
 probes, all related to the target entity.
(2) 
Neighbor set
: contains facts closely related to but not entirely belonging to the target entity, measured through FB and QA probes.
(3) 
Membership inference attacks (MIA)
: Compares the model’s predictions on the 
forget member (FM)
 set versus the 
Retain Member (RM)
 set, rigorously auditing whether the model still retains the target knowledge.
(4) 
Model utility
: Assesses the model’s overall performance after unlearning using general-purpose benchmarks, including MMLU (Gen) 
[
7
]
, BBH (Rea) 
[
32
]
, TruthfulQA (Tru) 
[
17
]
, TriviaQA (Fac) 
[
12
]
, and AlpacaEval (Flu)
[
15
]
.
For ToFU, following 
[
22
]
, 
forgetting
 is measured using prediction probability and ROUGE scores.
Post-unlearning capabilities are evaluated using 
model utility
, which includes the 
retain set score (RS)
, 
real authors set score (RAS)
, and 
world facts score (WFS).
Baselines 
We compare CAE with a comprehensive set of unlearning methods.
These include 
in-context unlearning (ICU)
[
29
]
, which achieves unlearning without changing model weights, and 
representation engineering (RepE)
[
14
]
, which perturbs hidden activations using control vectors.
We also include 
gradient ascent (GA)
[
9
]
, which explicitly maximizes loss on the forget set.
For preference-based approaches, we evaluate 
direct preference optimization (DPO)
[
30
]
 and 
negative preference optimization (NPO)
[
39
]
, as well as 
rejection tuning (RT)
, which fine-tunes the model to reject responses related to the target entity.
We additionally include enhanced variants such as 
gradient difference (Grad. Diff.)
[
18
]
 and 
KL minimization (KL Min.)
, which aim to improve unlearning efficacy through more precise loss shaping.
Finally, for editing-based approaches, we focus on locate-then-edit methods and compare with MEMIT 
[
25
]
, EMMET 
[
6
]
, and AlphaEdit 
[
5
]
.
This set covers a broad spectrum of strategies, from activation perturbation and loss-based methods to preference and editing-based techniques, allowing for a thorough comparison with CAE.
V-B
Main Results
To address 
RQ1
, we conduct experiments on the RWKU and ToFU.
We find CAE achieves state-of-the-art performance on both benchmarks, outperforming all editing-based baselines and many training-based methods.
It achieves stronger forgetting while better preserving neighbor knowledge and overall model utility, demonstrating a superior trade-off between forgetting and retention compared with prior approaches.
V-B
1 
Results on RWKU
For RWKU, following the experimental setup of 
[
11
]
, we evaluate each method’s performance on 100 subjects.
For forgetting performance, CAE delivers the most effective and comprehensive removal of entity knowledge. 
As shown in Table 
I
, CAE achieves an All score of 15.9, outperforming prompt-based, training-based, and other editing-based approaches.
Importantly, CAE attains competitive forgetting scores (78.1 and 72.4 on Mean_FN) through direct model editing, 
without relying on prompt-level interventions
.
Compared to training-based approaches such as GA and DPO, CAE makes a significant improvement on Mean_FN by at least 2–5%, exhibiting stronger entity erasure with substantially lower computational overhead (see Section 
V-D1
) and without retraining on large-scale data.
Moreover, CAE outperforms other editing methods on Mean_FN, demonstrating its ability to overcome the inconsistency limitations of these approaches.
Notably, while ICU achieves strong forgetting, it relies heavily on prompt manipulation, often at the expense of generality and controllability, which leads to weaker performance on neighboring tasks. In contrast, CAE consistently outperforms most baselines on metrics such as FB, QA, and AA, highlighting its robust and reliable entity-unlearning capability.
We further evaluate privacy via MIA on FM and RM.
CAE achieves both the highest FM and lowest RM, thereby producing the largest FM–RM gap among all methods.
This pronounced gap demonstrates CAE’s ability to selectively erase target knowledge without degrading the model’s overall factual understanding.
In summary, CAE not only delivers the strongest forgetting performance among editing-based methods but also surpasses prompt-based an

y in preserving neighboring knowledge.
Editing the last subject token (LST) provides more precise and stable edits than editing the last token (LT), demonstrating CAE’s sensitivity to token-level choices.
V-D
1 
Unlearning Cost
CAE delivers strong performance with minimal data and compute, making it a practical and efficient alternative to training-based methods.
In terms of data, CAE achieves near-optimal performance with as few as 100 examples, whereas training-based approaches like GA and NPO often require hundreds of additional instances—for example, at least 300 examples per entity in RWKU.
From a computational standpoint, full fine-tuning of the 8B-parameter LLaMA model requires two 80 GB GPUs. While techniques like LoRA can reduce GPU usage, they do so at the cost of significant performance degradation.
Editing-based methods, by comparison, perform the unlearning process on a single 40 GB GPU.
Additionally, CAE’s targeted data selection and consistency regularization strategies introduce virtually no additional computational overhead compared to other editing techniques.
V-D
2 
Analysis of Number of Editing Samples
We conduct ablation studies on LLaMA3-Instruct (8B) to investigate the effect of number of editing samples on performance.
In Figure 
6
, we compare our proposed SVD-based selection method (denoted as CAE) with a random selection baseline (CAE w/o). We observe that increasing the number of edited facts generally improves the 
All
 score for both CAE and CAE w/o, indicating better unlearning and generalization performance. Specifically, CAE shows a consistent upward trend in All, reaching its peak at 70 edits with a score of 77.52. In contrast, CAE w/o exhibits a downward trend in Neighbor metrics as the number of edits increases, suggesting that random selection increasingly disrupts unrelated knowledge.
Across all scales, CAE consistently outperforms CAE w/o on Neighbor metrics (FB(N), QA(N)) while achieving comparable or better forgetting. For example, QA improves from 7.98 to 7.52 at 50 edits.
CAE also attains a higher Mean_FN (76.11 vs. 72.43), demonstrating a better balance between target forgetting and neighbor preservation.
These results confirm the effectiveness of our SVD-based selection in identifying key edits, enabling precise and robust knowledge removal.
Increasing the number of editing samples generally leads to improved 
Forget
 performance across all methods, as more data provides stronger supervisory signals for forgetting.
However, this gain often comes at the cost of 
Neighbor
 degradation, indicating a trade-off between forgetting target knowledge and preserving nearby factual consistency.
Furthermore, as shown in Figure 
5
, we evaluate all methods under varying numbers of editing examples using 10 subjects in RWKU with Llama3-Instruct (8B), ranging from 20 to 100, corresponding to 
τ
\tau
 values in SVD of 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99, and 1.0. Increasing the number of editing samples generally improves 
Forget
 performance across all methods, as more data provides stronger supervisory signals for unlearning. However, this improvement often comes at the expense of 
Neighbor
 performance, highlighting the inherent trade-off between removing target knowledge and preserving nearby factual consistency.
In summary, our SVD-based selection consistently outperforms random choice, confirming its effectiveness in isolating the most relevant keys for precise knowledge removal.
Fig. 5
: 
Results on the Number of Edits. w/o means we random select the edits.
Fig. 6
: 
Performance across editing sizes. We evaluate with 10 entities from RWKU. The number of editing examples varies from 20 to 100, corresponding to SVD thresholds 
τ
\tau
 of 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99, and 1.0 respectively.
Fig. 7
: 
PCA projection of edit vectors 
𝐳
\mathbf{z}
 for different unlearning methods. CAE produces more concentrated and aligned 
𝐳
\mathbf{z}
 vectors, indicating better consistency across edits.
V-D
3 
Results on Editing the Last Token
We evaluate the impact of editing different token types on the Llama3 and Llama3.1 models, using the average performance across 10 distinct subjects from the RWKU.
The results in Table 
VI
 show that editing the last subject token (LST) yields better performance in both forgetting effectiveness and retention ability compared to editing the last token (LT).
Specifically, LST consistently achieves lower forgetting scores (e.g., 10.20% vs. 16.70%) and higher retention accuracy (e.g., 53.45% vs. 51.40%).
The Mean_FN also favors LST across both models, indicating that it provides a better trade-off between removing targeted knowledge and preserving unrelated capabilities.
These findings suggest that LST is a more stable and semantically coherent editing target than LT in subject-driven knowledge editing.
Llama3.1-Instruct (8B)
Llama3-Instruct (8B)
LT
LST
LT
LST
FB
14.10
11.60
16.70
10.20
QA
7.61
8.64
6.28
9.47
AA
19.80
17.10
19.70
19.10
All
13.84
12.45
14.23
12.92
FB
49.60
51.50
54.80
55.70
QA
41.80
44.70
48.00
51.20
All
45.70
48.10
51.40
53.45
Mean_FN
65.93
67.83
68.59
70.26
TABLE VI
: 
Comparison of last subject token (LST) and last token (LT).
V-D
4 
Unlearning Order
The consistency constraint in Eq.
7
 aligns the residual for the j-th input with the mean of the previous j-1 inputs.
To test robustness for different order with j inputs, as shown in Table 
VII
, we conducted four randomized trials on Llama-3 with 70 shuffled inputs per entity. Results show consistent performance across all key metrics, confirming that CAE exhibits minimal sensitivity to input order.
FB
QA
AA
n_FB
n_QA
Order-1
11.6
8.28
20.1
59.4
51.0
Order-2
12.6
7.62
20.5
57.9
49.7
Order-3
15.9
7.26
20.8
53.7
50.0
Order-4
12.6
6.51
18.6
56.9
48.1
TABLE VII
: 
Different Order for the Unlearning Entities.
“What nickname did Jackie Chan acquire during his time as a construction worker in Australia?” (Answer: 
Jackie
)
EMMET
: The nickname “The Gasman”. 
MEMIT
: The nickname “The Smiling Assassin”.
AlphaEdit
: Jackie Chan’s nickname from his time as a construction worker in Australia is “The Bodyguard”. 
CAE
: I couldn’t find any information about a person named Jackie acquiring a nickname during his time as a construction worker in Australia.
“Who were Jackie Chan’s co-stars in the ’Three Brothers’ films during the mid-1980s?” (Answer: 
Sammo Hung and Yuen Biao
)
EMMET
: The ‘Three Brothers’ films, also known as the ‘Three Brothers’ series, starred Jackie Chong, Sammo Hung, and Yuen B 
MEMIT
: The ‘Three Brothers’ films refer to the ’Three Stooges’ films, but in the context of the question, it seems to be referring 
AlphaEdit
: The ‘Three Brothers’ films refer to the ‘Drunken Master’ trilogy, which includes ’Drunken Master’ (1978).
CAE
: Unfortunately, I could not verify the names of Jackie’s co-stars in the ‘Three Brothers’ films.
Fig. 8
: 
CAE is capable of consistently producing uncertain (e.g., “I don’t know” or “Unknown”), thereby effectively avoiding knowledge leakage. In contrast, other editing methods still tend to output factual information related to Jackie Chan.
V-E
Analysis of Consistency
For 
RQ4
, we analyze the representation geometry of edit vectors using PCA and similarity statistics, compare CAE with MEMIT/EMMET/AlphaEdit, examine leakage under paraphrase-style queries, and perform ablations on the consistency loss weight.
We find PCA and vector similarity analyses show that CAE produces the most compact and aligned edit vectors among all methods, indicating stable and coherent update directions.
This alignment enabled by the consistency loss minimizes interference across paraphrases and prevents knowledge leakage.
Ablation studies on the consistency weight further demonstrate that CAE remains stable across a wide range of settings.
V-E
1 
Analysis of Consistency Loss
Figure 
7
 visualizes the principal components of the learned edit vectors (
z
z
-vectors) across different editing methods using PCA.
We observe that MEMIT and EMMET produce highly scattered distributions, indicating that the update directions vary substantially across different inputs.
This suggests that their editing behaviors may be highly instance-specific, leading to less consistent or even conflicting updates when applied to multi-prompt or entity-level tasks.
In contrast, CAE and AplhaEdit produce noticeably more compact clusters in the low-dimensional space, with CAE showing the most tightly grouped 
z
z
-vectors among all methods.
This implies that CAE learns a more unified and consistent edit direction across diverse paraphrases.
We demonstrate that CAE produces consistently uncertain responses and effectively prevents knowledge leakage, unlike other methods that reveal factual content under paraphrased queries (cf. Fig. 
8
).
V-E
2 
Ablation for consistency weight
We set the weight to 0.05 (
λ
c
​
o
​
n
​
s
\lambda_{cons}
 in Eq. 
7
) to balance sensitivity loss with other objectives. Results demonstrate our method’s robustness: weight variations minimally affect both forgetting and retention, with all metrics showing only minor fluctuations while general performance remains stable.
λ
c
​
o
​
n
\lambda_{con}
FB
QA
AA
n_FB
n_QA
0.01
15.4
10.7
19.1
63.3
49.4
0.05
13.2
7.98
19.5
61.9
50.2
0.1
17.8
7.89
18.8
60.5
49.7
0.15
13.6
10.1
20.9
64.3
50.9
0.2
15.7
8.59
19.4
61.8
51.0
TABLE VIII
: 
Ablation for consistency weight
FB 
↓
\downarrow
QA 
↓
\downarrow
AA 
↓
\downarrow
n_FB
n_QA
Tru
Rea
Fac
Gen
Flu
Before
43.7
44.7
55.5
47.5
40.6
41.2
11.3
28.1
74
713
ICU
47.5
32.0
41.5
44.4
40.7
43.8
4.7
22.8
72.7
700
CAE
16.9
12.6
24.5
40.7
37.5
41.4
11.1
27.7
74
714
TABLE IX
: 
Results with Qwen2.5-7B-Instruct
Before
CAE-50
CAE-60
CAE-70
FB
85.6
16.1
15.9
13.5
QA
71.5
10.8
10.8
10.7
AA
75.3
22.9
22.9
18.8
N_FB
93.4
66.9
67.7
72.7
N_QA
82.0
61.7
60.0
67.7
Tru
36.8
34.7
34.7
34.3
Rea
41.1
39.0
39.0
38.5
Fac
53.8
52.6
52.6
52.4
Gen
65.4
65.5
65.0
64.5
Flu
706
706
706
704
TABLE X
: 
Unlearning results with LLM generated data.
V-F
Generalization Analyze
For 
RQ5
, we conducted tests on models with different architectures.
Based on our findings, we utilized data generated by LLMs (such as ChatGPT) to achieve forgetting, further verifying the generalization and universality of our method.
V-F
1 
Results with Qwen
To address generalization, we conducted additional experiments on Qwen2.5-7B-Instruct 
[
33
]
 using 10 subjects.
As shown in the Figure 
IX
, the results demonstrate that our method remains effective even on this different architecture, maintaining key advantages in preserving model capabilities while achieving the editing objectives.
V-F
2 
Results on LLM Generated data
We use Wikidata not only as a data source but also as a basis for analyzing data type and quantity requirements when applying editing methods to the unlearning task.
Using an SVD-based selection strategy at the hidden-state level, we found that about 70 data points (covering 10 aspects (e.g., birthday) with 5 syntactic variations each) were sufficient to unlearn a subject.
Thus, the unlearning process requires only this curated data, regardless of the source of the unlearning data.
To verify it, we also verified that model-generated data for unlearning, the results are shown in Table 
X
.
Using ChatGPT to create 70 data for 10 subjects, we observed a clear drop on forget sets (FB, QA, AA) while maintaining general abilities (N_FB, N_QA, etc.).
Compared to using 50 or 60 data, 70 setting achieved the best forgetting effect, consistent with our wikidata conclusion.
VI 
Discussion & Conclusion
Thi
