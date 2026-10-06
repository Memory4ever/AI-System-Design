# 2601.09445v1 — donor control and nonuniform counterexamples

Exact primary: https://arxiv.org/html/2601.09445v1 ; selected necessary original body excerpts actually read, not full-attachment review.

4.3 
Causal Tracing via Activation Patching
After identifying a component 
c
c
 at layer 
l
l
 that is strongly associated with conflicting information for a given attribute type 
a
a
 (e.g., 
graduated university
) in 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
, we apply activation patching to causally assess the contribution of 
c
c
 to the model’s output behavior.
Specifically, for each individual 
p
i
p_{i}
 among the 
n
1
n_{1}
 individuals in 
SynWikiBio
 whose biography contains contradictory factual claims about attribute type 
a
a
, we define the causal effect of component 
c
c
 using the corresponding prefix prompt 
p
​
r
i
pr_{i}
. This prompt induces competition between two next-token continuations, 
t
1
t_{1}
 and 
t
2
t_{2}
, corresponding to the conflicting facts 
f
i
f_{i}
 and 
f
¯
i
\bar{f}_{i}
, respectively. Let 
p
t
​
(
⋅
)
p_{t}(\cdot)
 denote the probability assigned by the model to token 
t
t
. The causal effect of component 
c
c
 at layer 
l
l
 on the generation of token 
t
1
t_{1}
 under the noisy prompt 
p
​
r
i
pr_{i}
 is defined as:
Δ
t
1
c
,
l
,
↑
:=
p
t
1
​
(
ℓ
′
~
mix
c
,
l
​
(
p
​
r
i
,
t
s
)
)
−
p
t
1
​
(
ℓ
mix
′
​
(
p
​
r
i
)
)
,
\Delta^{c,l,\uparrow}_{t_{1}}\;:=\;p_{t_{1}}\!\left(\tilde{\ell^{\prime}}^{c,l}_{\text{mix}}(pr_{i},t_{s})\right)\;-\;p_{t_{1}}\!\left(\ell^{\prime}_{\text{mix}}(pr_{i})\right),
and the corresponding effect on the alternative continuation 
t
2
t_{2}
 is defined as:
Δ
t
2
c
,
l
,
↑
:=
p
t
2
​
(
ℓ
′
~
mix
c
,
l
​
(
p
​
r
i
,
t
s
)
)
−
p
t
2
​
(
ℓ
mix
′
​
(
p
​
r
i
)
)
.
\Delta^{c,l,\uparrow}_{t_{2}}\;:=\;p_{t_{2}}\!\left(\tilde{\ell^{\prime}}^{c,l}_{\text{mix}}(pr_{i},t_{s})\right)\;-\;p_{t_{2}}\!\left(\ell^{\prime}_{\text{mix}}(pr_{i})\right).
Here, 
ℓ
′
~
mix
c
,
l
​
(
p
​
r
i
,
t
)
\tilde{\ell^{\prime}}^{c,l}_{\text{mix}}(pr_{i},t)
 denotes a forward pass of model 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
 for processing the noisy prompt 
p
​
r
i
pr_{i}
, in which the activation of component 
c
c
 at layer 
l
l
is replaced with a cached activation of the component 
c
c
 of the same model sourced from a clean, single-fact prompt 
p
​
r
j
pr_{j}
 belonging to another individual 
p
j
p_{j}
 among the 
n
2
n_{2}
 individuals in 
SynWikiBio
. This clean prompt expresses the same attribute value corresponding to source token 
t
s
∈
{
t
1
,
t
2
}
t_{s}\in\{t_{1},t_{2}\}
 for attribute type 
a
a
, and the cached activation is taken at the position immediately preceding the generation of the next token 
t
s
t_{s}
. This intervention isolates the causal influence of component 
c
c
 on resolving factual conflicts by measuring how substituting a clean, fact-consistent activation alters the model’s preference between competing continuations.
4.4 
Cross Model Activation Patching
Standard activation patching relies on sourcing activations from prompts processed by the same model, which implicitly assumes the availability of a suitably similar yet non-confounded source prompt. This assumption breaks down in the presence of intra-memory knowledge conflict. For instance, a source biography 
b
s
​
o
​
u
​
r
​
c
​
e
b_{source}
 that is absent from the training data may fail to elicit faithful parametric recall, yielding activations that are unrepresentative of the model’s stored knowledge. Conversely, a source biography that is overly similar to the target biography 
b
t
​
a
​
r
​
g
​
e
​
t
b_{target}
risks being conflated with it, causing the model to encode overlapping or competing internal representations. In both cases, prompt selection becomes ill-posed: the model either fails to retrieve the intended fact or cannot cleanly separate the source and target memories, leading to unstable or contradictory activations.
To mitigate this issue, in the previous section we employ clean prompts 
p
​
r
j
pr_{j}
 that express the same attribute value but correspond to a different individual 
p
j
p_{j}
, and use these prompts to patch the noisy prompt 
p
​
r
i
pr_{i}
 associated with individual 
p
i
p_{i}
, whose biography contains conflicting information for attribute 
a
a
. While this strategy partially alleviates prompt–target entanglement, it introduces additional noise into the patched activations due to inter-person differences, thereby weakening the strength and reliability of causal attribution in the presence of factual conflict.
As a resolution, we adopt 
cross-model activation patching (CMAP)
, an advance causal tracing method, which we tailor to the study of intra-memory factual conflict. Instead of sourcing patched activations from alternative prompts within the same conflicted model 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
, CMAP transfers activations from a 
clean
 reference model 
ℓ
clean
′
\ell^{\prime}_{\text{clean}}
, which is obtained by continuing pretraining the same base model 
ℓ
\ell
 on 
SynWikiBio_clean
. By construction, 
ℓ
clean
′
\ell^{\prime}_{\text{clean}}
 is trained on exactly one ground-truth biography 
b
i
b_{i}
 per individual 
p
i
p_{i}
 and contains no mutually contradictory factual claims with respect to attribute 
a
a
.
During patching, activations from 
ℓ
clean
′
\ell^{\prime}_{\text{clean}}
 are injected into 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
 at corresponding components and layers while processing the conflicting prompt 
p
​
r
i
pr_{i}
. Crucially, the two models are aligned in both architecture and training data: they share the same base initialization 
ℓ
\ell
 and are trained on the same set of individuals 
{
p
i
}
\{p_{i}\}
, differing only in whether contradictory claims 
f
¯
i
\bar{f}_{i}
 are present. This controlled alignment eliminates ambiguity arising from prompt mismatch or inter-person variation, ensuring that the patched activations correspond to uncontaminated parametric representations of 
f
i
f_{i}
. As a result, CMAP enables more reliable and interpretable causal attribution of the internal components that mediate the resolution of factual conflicts in 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
.
5 
Experimental Setup
Dataset.
The datasets used in this study (
SynWikiBio
 and 
SynWikiBio_clean
) follow the Wikipedia short biography template consisting of fictional individuals, each with a unique set of personal attributes:
birth date
, 
birth place
, 
university
, 
major
, 
company
, and 
work place
. We follow the generation process from 
Li et al. (2024a)
 with GPT-4o 
Hurst et al. (2024)
 to generate the biographies. Entity names of important attributes 
birth place
, 
company
 and 
university
 are replaced with random generated words. Less relevant attributes (i.e. 
major
, 
work place
) remain unchanged. The conflict attribute in the biography is either in 
university
 or 
company
 category.
Reasons and details of dataset generation with dataset statistics are provided in Appendix 
A.2.1
.
Models.
We evaluate our framework on two language models, GPT-2 XL 1.5B
Radford et al. (2019)
 and Qwen3-4B 
Yang et al. (2025)
.
For GPT-2 XL and Qwen3-4B model,
we continued pre-training it using 
SynWikiBio
 and 
SynWikiBio_clean
 for 40 and 20 epochs respectively, resulting in two fine-tuned variants: 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
 and 
ℓ
clean
′
\ell^{\prime}_{\text{clean}}
, respectively. The implementation details are mentioned in Appendix 
A.3
.
6 
Results and Findings
In this section, we present and analyze the results of our ex

---

6.2 
Component-wise Activation Patching Results
(a) 
Patching biographies with conflict attribute 
a
a
 = 
university
(b) 
Patching biographies with conflict attribute 
a
a
 = 
company
Figure 4: 
Magnitude of probability change of 
t
1
t_{1}
 and 
t
2
t_{2}
 at layer 43 after patching with 
t
s
=
t
1
t_{s}=t_{1}
. We observe probability changes of 
t
1
t_{1}
 on the left and 
t
2
t_{2}
 on the right plots. When 
ℓ
m
​
i
​
x
′
\ell^{\prime}_{mix}
 is patched with 
t
1
t_{1}
, the normal expectation is that 
Δ
t
1
c
,
l
,
↑
\Delta^{c,l,\uparrow}_{t_{1}}
 is postive while 
Δ
t
2
c
,
l
,
↑
\Delta^{c,l,\uparrow}_{t_{2}}
 is negative.
After narrowing the analysis to the attention components in the later layers, we examine the causal impact of individual components on the generation of the conflicted information 
t
1
t_{1}
 and 
t
2
t_{2}
 within 
ℓ
m
​
i
​
x
′
\ell^{\prime}_{mix}
.
As described in Section 
4.3
, for each attribute type (i.e., 
university
 and 
company
) and each attention component, we record two probability changes (
Δ
t
1
c
,
l
,
↑
\Delta^{c,l,\uparrow}_{t_{1}}
 (left) and 
Δ
t
2
c
,
l
,
↑
\Delta^{c,l,\uparrow}_{t_{2}}
 (right)) across all conflicting biographies in 
SynWikiBio
. Clean prompt is selected to keep source token 
t
s
t_{s}
 as 
t
1
t_{1}
.
We then sort these probability changes
into five magnitudes bins of changing model decisions (1: Low, 5: High) as indicated in Table 
1
 (with rationale in Appendix 
A.4
).
Magnitude
Condition
1
Δ
​
P
​
r
​
o
​
b
<
7.5
%
\Delta Prob<7.5\%
2
7.5
%
≤
Δ
​
P
​
r
​
o
​
b
<
10
%
7.5\%\leq\Delta Prob<10\%
3
10
%
≤
Δ
​
P
​
r
​
o
​
b
<
13
%
10\%\leq\Delta Prob<13\%
4
13
%
≤
Δ
​
P
​
r
​
o
​
b
<
20
%
13\%\leq\Delta Prob<20\%
5
Δ
​
P
​
r
​
o
​
b
≥
20
%
\Delta Prob\geq 20\%
Table 1: 
Binned Probability Change Magnitudes.
Figure 
4
 shows the magnitude of probability changes when the attention component at layer 43 is patched. The results of layer 43 is chosen because of the layer’s high contribution to majority of the tokens, as shown in Figure 
5
. The magnitudes are mostly in the first bin, indicating small changes in 
ℓ
m
​
i
​
x
′
\ell^{\prime}_{mix}
’s confidence, and unlikely that it will change its output. Notably, in some cases, patching with similar information still results in decrease in confidence for the ground-truth token. This behavior, however, varies across different types of conflicts. The drop in confidence may result from noise introduced by differences between 
b
i
b_{i}
 and 
b
j
b_{j}
 in the patched activations.
Figure 5: 
Top 6 highest impact attention components per-token across the layers, with effect size (layer 
l
l
, token 
t
t
) as the average probability contribution of the attention component in layer 
l
l
 to token 
t
t
.
To further localize the components within GPT-2 XL that have the most influence on the model’s output, we compute component-level impact on a per-token basis. For every source token 
t
s
t_{s}
, we record all activation patching instances in which activation of 
t
s
t_{s}
 are used for patching. We then identify the top six components that contribute the most to 
t
s
t_{s}
’s probability change after patching and plot the five most frequent source tokens within each category, as shown in Figure 
5
. We observe that, for most tokens, the components with the highest impact are predominantly concentrated in the model’s final layers. This suggests that higher-layer attention components play a dominant role in shaping the model’s factual response.
6.3 
Steering Model Generation with Component-wise Activation Patching
(a) 
Activation patching steering success rate
(b) 
CMAP steering success rate
Figure 6: 
Comparison between standard activation patching and CMAP
In this experiment, we measure the success rate with which patching flips the model’s output. Change in model’s final generation indicates that the patched component has sufficient influence to affect how the model resolves the conflicting information. Specifically, we measured the success rate of source token 
t
s
t_{s}
 becoming the very first choice of 
ℓ
m
​
i
​
x
′
\ell^{\prime}_{mix}
 after patching, but not prior to patching. As shown in Figure 
6(a)
,
this success rate typically falls within 10-20% for 
t
s
t_{s}
 from 
university
 category and 5-15% for those of 
company
 category. Despite moderate success rates, patching activations corresponding to one of multiple conflicting facts can steer model predictions toward an alternative outcome.
6.4 
Cross-Model Activation Patching Results
(a) 
CMAP with conflict attribute 
a
a
 = 
university
(b) 
CMAP with conflict attribute 
a
a
 = 
company
Figure 7: 
Magnitude of probability change of 
t
1
t_{1}
 and 
t
2
t_{2}
 at layer 43, CMAP and standard activation patching comparison. Cross model patching achieves better results for 
company
-conflict attribute, increasing the positive samples in every bins, but the trend is reversed for 
university
-conflict attribute.
Following our proposed approach described in Section 
4.4
, we re-run the experiments in section 
6.2
 and 
6.3
 using CMAP. For each person 
p
i
p_{i}
 in the contradict subset, we use the biography 
b
i
b_{i}
 that is in 
SynWikiBio
 and 
SynWikiBio_clean
 to generate prompt 
p
​
r
i
pr_{i}
 and track the probability of 
t
S
t_{S}
 after patching from 
ℓ
c
​
l
​
e
​
a
​
n
′
\ell^{\prime}_{clean}
 to 
ℓ
m
​
i
​
x
′
\ell^{\prime}_{mix}
.
The results in Figure
6(b)
 show that CMAP improve steering success, reaching a maximum of 27% at Layer 44. While steering rates for 
university
 samples remain similar to those in Figure 
6(a)
, rates for 
company
 samples increase substantially, from 17% to 27%.
With respect to probability contributions, Figure 
7
 shows that compared to standard activation patching, CMAP reduces negative impacts on confidence and slightly increases component contributions for the 
company
 attribute, but more often decreases confidence and component contributions for the 
university
 attribute.
6.5 
Experiments with Qwen3-4B
To assess the generalizability of our findings, we repeat our experiments using a different model, Qwen3-4B 
Yang et al. (2025)
. Overall, our experiments with Qwen3-4B yield similar findings as with GPT-2 XL. The comparison also gives us some interesting insights: for Qwen3-4B, we achieve a markedly higher success rate, reaching up to 70%, in steering model generation. And CMAP achieves performance comparable to activation patching across most layers except layer 33. We discuss more details in appendix 
A.5
.
6.6 
General Findings
Conflicting training data reduce

---

Limitations
We acknowledge the following limitations of our study. First, we consider a limited set of conflict types and restrict each entity to a 1:1 ratio with each conflicting information. We plan to include more conflict types and multiple conflicting information per entity in future study.
Second, our results are presented on a limited set of model architectures. While we demonstrate generalization to Qwen3-4B model, further evaluation across additional model families is necessary. Finally, we do not analyze the underlying factors that drive the model’s preference from one conflicting fact over another. Addressing this problem in future work
can provid

---

A.3 
Implementation Details
We use the Transformers library 
Wolf et al. (2019)
 to implement the model training. For causal tracing tasks, we use TransformerLens 
Nanda and Bloom (2022)
 to cache the model’s states and patch activations.
A.4 
Magnitude Bins
We determine the thresholds for the magnitude bins using statistics derived from the activation patching experiments. Activation patching frequently alters the model’s confidence over the top candidates and can lead to changes in the mo
