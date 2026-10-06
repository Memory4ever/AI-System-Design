# 2601.09445v1 决定性准入原段

Exact primary https://arxiv.org/html/2601.09445v1 。仅记录本次实际读的决定性方法/接口/失败段，非完整Evidence或日期/Books验收。

4.2 
Locating Conflict-Encoding Components via Logit Lens
To identify components responsible for encoding and generating conflicting information in the model 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
, we analyze logit and probability changes across layers using the logit lens. For each individual 
p
i
p_{i}
 among the 
n
1
n_{1}
 individuals in 
SynWikiBio
 whose biography contains a contradictory factual claim, we prompt 
ℓ
mix
′
\ell^{\prime}_{\text{mix}}
 with the prompt 
p
​
r
i
pr_{i}
 (Section 
3
) and perform the following analysis.
At each transformer layer 
l
∈
{
1
,
…
,
L
}
l\in\{1,\dots,L\}
, we extract residual stream representations at three locations: the layer input 
x
pre
l
x^{l}_{\mathrm{pre}}
, the residual stream after going through the attention block 
x
mid
l
x^{l}_{\mathrm{mid}}
, and residual stream after going through the MLP block 
x
post
l
=
x
pre
l

1
x^{l}_{\mathrm{post}}=x^{l+1}_{\mathrm{pre}}
. Each representation is projected from the model dimension 
d
model
d_{\mathrm{model}}
 to the vocabulary dimension 
d
vocab
d_{\mathrm{vocab}}
 using the unembedding matrix 
W
U
W_{U}
, and converted into a probability distribution over tokens via the softmax function:
P
s
l
=
softmax
⁡
(
W
U
​
x
s
l
)
,
s
∈
{
pre
,
mid
,
post
}
P^{l}_{s}=\mathrm{softmax}\!\left(W_{U}\,x^{l}_{s}\right),\;s\in\{\mathrm{pre},\mathrm{mid},\mathrm{post}\}
(3)
Using these distributions, we define the contribution of each subcomponent in layer 
l
l
 to a token 
t
t
 as the change in its predicted probability across that subcomponent:
contrib
attn
l
​
(
t
)
\displaystyle\mathrm{contrib}^{l}_{\mathrm{attn}}(t)
=
P
mid
l
​
(
t
)
−
P
pre
l
​
(
t
)
,
\displaystyle=P^{l}_{\mathrm{mid}}(t)-P^{l}_{\mathrm{pre}}(t),
(4)
contrib
mlp
l
​
(
t
)
\displaystyle\mathrm{contrib}^{l}_{\mathrm{mlp}}(t)
=
P
post
l
​
(
t
)
−
P
mid
l
​
(
t
)
.
\displaystyle=P^{l}_{\mathrm{post}}(t)-P^{l}_{\mathrm{mid}}(t).
(5)
We hypothesize that components responsible for recalling parametric knowledge will exhibit systematically different contribution patterns for learned conflicting tokens compared to unrelated but high-probability alternatives. Therefore, for each prompt 
p
​
r
i
pr_{i}
, we track probability changes for three token groups: (i) the ground-truth token 
t
1
t_{1}
, (ii) the contradictory token 
t
2
t_{2}
, and (iii) a control set 
𝒯
i
\mathcal{T}_{i}
 consisting of the top five tokens in the final prediction 
P
post
L
P^{L}_{\mathrm{post}}
, excluding 
t
1
t_{1}
 and 
t
2
t_{2}
.
For the control set, we compute the mean contribution at layer 
l
l
 as
contrib
attn
l
​
(
𝒯
i
)
\displaystyle\mathrm{contrib}^{l}_{\mathrm{attn}}(\mathcal{T}_{i})
=
1
|
𝒯
i
|
​
∑
t
∈
𝒯
i
contrib
attn
l
​
(
t
)
,
\displaystyle=\frac{1}{|\mathcal{T}_{i}|}\sum_{t\in\mathcal{T}_{i}}\mathrm{contrib}^{l}_{\mathrm{attn}}(t),
(6)
contrib
mlp
l
​
(
𝒯
i
)
\displaystyle\mathrm{contrib}^{l}_{\mathrm{mlp}}(\mathcal{T}_{i})
=
1
|
𝒯
i
|
​
∑
t
∈
𝒯
i
contrib
mlp
l
​
(
t
)
.
\displaystyle=\frac{1}{|\mathcal{T}_{i}|}\sum_{t\in\mathcal{T}_{i}}\mathrm{contrib}^{l}_{\mathrm{mlp}}(t).
(7)
Finally, we aggregate contributions across all 
n
1
n_{1}
 individuals to obtain population-level statistics. For any token or token set 
τ
∈
{
t
1
,
t
2
,
𝒯
}
\tau\in\{t_{1},t_{2},\mathcal{T}\}
, the aggregated attention and MLP contributions at layer 
l
l
 are defined as
contrib
¯
attn
l
​
(
τ
)
\displaystyle\overline{\mathrm{contrib}}^{l}_{\mathrm{attn}}(\tau)
=
1
n
1
​
∑
i
=
1
n
1
contrib
attn
l
​
(
τ
i
)
,
\displaystyle=\frac{1}{n_{1}}\sum_{i=1}^{n_{1}}\mathrm{contrib}^{l}_{\mathrm{attn}}(\tau_{i}),
(8)
contrib
¯
mlp
l
​
(
τ
)
\displaystyle\overline{\mathrm{contrib}}^{l}_{\mathrm{mlp}}(\tau)
=
1
n
1
​
∑
i
=
1
n
1
contrib
mlp
l
​
(
τ
i
)
,
\displaystyle=\frac{1}{n_{1}}\sum_{i=1}^{n_{1}}\mathrm{contrib}^{l}_{\mathrm{mlp}}(\tau_{i}),
(9)
where 
τ
i
=
τ
\tau_{i}=\tau
 for 
t
1
t_{1}
 and 
t
2
t_{2}
, and 
τ
i
=
𝒯
i
\tau_{i}=\mathcal{T}_{i}
 for the control tokens. Because each prompt 
p
​
r
i
pr_{i}
 is tied to a specific attribute type (e.g., 
graduated university
 or 
employer
2
2
2
            we use ’company’ to refer the employer and ’university’ to refer to graduated university to be consistent with previous works.
), this aggregation enables further stratified analyses. In particular, we can identify components selectively important for attribute categories and those specialized to individual attribute values (e.g., 
University of Zinl
), enabling fine-grained model attribution.
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
 for processing the noi
