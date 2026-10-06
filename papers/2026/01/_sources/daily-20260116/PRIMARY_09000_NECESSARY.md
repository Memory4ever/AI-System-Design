# 2601.09000v1 — minimum necessary primary core

Exact HTML: https://arxiv.org/html/2601.09000v1 . 以下仅已实际读的方法、决定性评价/直接反侧与必要复现字段；区段为HTML正文字符定位，非全文/附录完成声明。未执行实验或代码。

## Body 11150–16150

3
Experiments
Building on the macroscopic similarity observed in how WSD affects performance in both transformer language models and CNNs for image classification (Fig.
1
), we aim to examine at a finer scale the training dynamics and the loss landscape regions traversed by AdamW iterates under WSD across the two model types.
Setup
For our empirical evaluation on transformer-based LMs, we train a decoder-only transformer model
13
, with around 160M trainable parameter, on the cerebras/SlimPajama-627B HF dataset
(
12
)
, using PlainLM by
1
.
Extending the study of WSD to non-transformer-based architectures instead, we experiment with a small CNN, with approximately 334K parameters, trained for an image classification task on the CIFAR10 dataset. All models are trained with Adam
9
. For further details on the experimental setup, please refer to Appendix
A
.
River Valley
First, we aim to replicate some of the findings of
14
. To support their River Valley hypothesis,
14
provide visualizations of the loss landscape by plotting the loss along linear interpolations between selected training checkpoints near the end of the stable phase, obtaining a convex loss curve resembling a valley (
14
Fig. 7a). In contrast, when plotting the loss along the interpolation between two points before and after a cooldown (
14
Fig. 7b), they observe a smooth decline, consistent with the observations of
4
(Fig. 7), who characterize this phase as a smooth transition to a connected basin in the loss landscape.
Figure 2:
Loss evaluated along
α
​
t
+
(
1
−
α
)
​
t
′
\alpha t+(1-\alpha)t^{\prime}
, with
α
∈
[
0
,
1
]
\alpha\in[0,1]
, where
t
′
t^{\prime}
and
t
t
denote checkpoints taken at 80% and 100% of the stable phase, or at the start and end of the cooldown phase, on an LM (left) and a CNN (right). Both models display a similar convex valley-shaped profile between the two checkpoints sampled near the end of the stable phase, followed by a monotonic descent over the cooldown period.
We reproduce the same visualizations in Fig.
2
, by interpolating between the checkpoint at 80% of the stable phase and the one at the start of the cooldown, as well as between the one at the start and at the end of the cooldown itself.
We obtain consistent results not only for transformer but, perhaps surprisingly, also for the CNN.
It therefore appears that the “river valley” landscape induced by WSD is not unique to transformer-based language models. Indeed, the loss surface of CNNs also seems to exhibit this profile within the optimizer’s region under WSD, which may partially align with some findings of
15
(although obtained using SGD and GD, as opposed to Adam).
Sharpness
Further examining the shape of the loss function, we observe that, for both models, sharpness (the largest eigenvalue of the loss Hessian) tends to increase along the iterates collected while annealing the learning rate (which we name
D
D
), consistent with the findings of
6
, and more in general with
3
and
8
, as shown in Fig.
3
.
Training Directions
Focusing on the training trajectory, we aim to verify if the stable and cooldown phases correspond to two distinct movement directions in the parameter space, as suggested by
14
. To investigate this, we perform Principal Component Analysis (PCA) on two sets,
S
S
and
D
D
, each containing iterates
x
i
x_{i}
uniformly sampled during stable and decay phases, respectively.
For both models and phases, the first component captures at least approximately 40% of the total variance (Fig.
), suggesting that each phase is primarily governed by a main yet distinct direction.
Cooldown unveils a sharp tunnel
Motivated by this common trait and by the sharpness increase at cooldown, we zoom in on checkpoint
x
^
\hat{x}
at decay start, to closely examine how and why sharpness evolves along the optimizer’s path.
Given two sets,
S
′
S^{\prime}
and
D
′
D^{\prime}
, consisting of iterates
x
i
x_{i}
uniformly sampled from the last 20% of the stable and the first 20% of the cooldown, respectively, we center both point clouds and apply PCA to each. This yields two main parameter-space directions,
v
s
v_{s}
and
v
d
v_{d}
, which capture the trajectory near the loss curve elbow.
We then analyze how these directions align with the Hessian
∇
2
ℒ
​
(
x
^
)
\nabla^{2}\mathcal{L}(\hat{x})
eigenspaces, finding
‖
∇
2
ℒ
​
(
x
^
)
​
v
s
‖
<
‖
∇
2
ℒ
​
(
x
^
)
​
v
d
‖
\left\|\nabla^{2}\mathcal{L}(\hat{x})v_{s}\right\|<\left\|\nabla^{2}\mathcal{L}(\hat{x})v_{d}\right\|
for both models (Fig.
3
).
This suggests that the direction corresponding to the early cooldown lies more closely in high-curvature regions of the loss landscape.
During decay, despite much smaller updates (Fig.
)
6
, true loss minimization becomes clear as the reduced step size allows the trajectory to “see”, and thus to follow, sharper subspaces of the parameter space, that were previously not accessible.
Figure 3:
(Left)
Estimated sharpness, evaluated on iterates
x
i
x_{i}
sampled at a fixed rate along 

## Body 17495–20400

Quasi-Convexity
Finally, we end by examining the broader explanation from
10
, which currently shows a mismatch between the application context (non-convex loss optimized with AdamW) and the theoretical setting on which the argument is based (convex loss optimized with SGD).
Therefore, we investigate how “surprising” the alignment between the loss profile and the theoretical bound truly is.
We test the
Weak-Quasi-Convexity
condition introduced by
5
(Def. 2.1), evaluating it over a domain
B
B
consisting of a subset of iterates
x
i
x_{i}
sampled regularly after warmup. As shown in Fig.
4
,
Weak-Quasi-Convexity
holds for both models, in nearly all cases.
Similarly, we compare AdamW updates to those of SGD. To do so, we compute the cosine similarity between the negative gradient and the actual update vector at each point in
B
B
, consistently finding positive values for both models, as presented in Fig.
4
.
Taken together, these results reduce the perceived surprise regarding the alignment observed by
10
, as the loss appears to exhibit a nearly convex behavior along AdamW’s trajectory. So, these last findings provide validation for an explanation of WSD that seems to hold regardless of the architecture, and they also point out other potentially interesting analogies between transformer LMs and CNNs.
4
Discussion and Conclusions
The experiments and results obtained suggest that the distinctive behavior of WSD, although primarily observed and studied in transformer-based language models, is not exclusive to them. This is evident not only in overall performance, but also through a closer analysis of the training dynamics and of the loss surface structure: we observe general and shared characteristics that support the typical WSD loss curve across two distinct (in size and training modality) architectures. An intriguing future direction is to investigate the effect of overparametrization on WSD performance, not indeed that our CNN, being small, does not perfectly fit the data (similarly to the transformer).
Acknowledgments
The authors thank the Hector Foundation for the financial support provided.
References
Ajroldi (2024)
N. Ajroldi
PlainLM: language model pretraining in pytorch
.
Note:
https://github.com/Niccolo-Ajroldi/plainLM
Cited by:
Appendix A
,
§3
.
Biderman
et al.
(2023)
S. Biderman, H. Schoelkopf, Q. G. Anthony, H. Bradley, K. O’Brien, E. Hallahan, M. A. Khan, S. Purohit, U. S. Prashanth, E. Raff,
et al.
Pythia: a suite for analyzing large language models across training and scaling
.
In
International Conference on Machine Learning
,
pp. 2397–2430
.
Cited by:
Figure 1
.
Cohen
et al.
(2022)
J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter, and A. Talwalkar
Gradient descent on neural networks typically occurs at the edge of stability
.
External Links:
2103.00065
Cited by:
§3
.
Hägele
et al.
(2024)
A. Hägele, E. Bakouch, A. Kosson, L. B. Allal, L. V. Werra, an

## Body 23225–24080

Appendix A
Experimental Setup
In our empirical analysis of language models, we use a transformer-based language model
13
, with just over 160M trainable parameters. We train it on approximately 3 billion tokens from the the cerebras/SlimPajama-627B HF dataset
(
12
)
, employing a batch size of 256 and a sequence length of 2048, using PlainLM
1
.
To examine WSD training dynamics in non-transformer architectures instead, we use as a case study a small CNN with about 334K parameters. We train it for an image classification task on the CIFAR10 dataset
https://www.cs.toronto.edu/~kriz/cifar.html
, using a batch size of 128. For completeness, we provide below its architecture implemented in PyTorch.
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
We are continuing to improve H
