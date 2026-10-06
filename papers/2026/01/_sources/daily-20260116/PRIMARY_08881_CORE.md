# 2601.08881v1 necessary primary core

ExactHTML https://arxiv.org/html/2601.08881v1. Necessary selected methods/evaluation/limits; not all appendices, not later revisions. TOC-mislocation discarded before source caching.

ubsequent works refine input representations and architectures to improve multimodal conditioning. Methods such as UniReal 
5
 and RealGeneral 
18
 introduces trainable index, subject, and condition embeddings to enhance alignment, while Flux-Kontext 
16
 employes 3D rotary positional encodings to distinguish source from target images. Architectural innovations include dual-branch models that decouple subject and background processing 
17
, channel-wise concatenation to preserve contextual signals 
20
, and the integration of auxiliary MLLMs or transformers for improved scene understanding 
10
; 
35
; 
29
, albeit with increased complexity and compute.
Despite these advances, current unified models overlook a central challenge: the inherent conflict between the objectives of different image-to-image tasks. Editing tasks (e.g., style transfer, object removal) require precise regional preservation while modifying others, whereas customization tasks (e.g., subject-driven generation) demand strong identity consistency across new contexts. Without explicitly modeling these distinct—and often competing—requirements, existing approaches struggle to adaptively serve the full spectrum of user intents, limiting their practical robustness and generalization.
2.2 
Image Generation with Mixture of Experts
The MoE paradigm increases model capacity by routing inputs to specialized sub-networks, or “experts,” avoiding a proportional rise in per-sample computation. Its success in large language models has motivated adoption in visual generation: pioneering works such as DiT-MoE 
11
, and scaled variants like HunyuanImage-3.0 
3
 and Dense2MoE 
45
, show that sparse expert architectures can enhance the expressiveness of diffusion transformers.
Extending MoE to image editing, ICEdit 
43
 integrates LoRA-based MoE modules into attention blocks. However, purely data-driven routing is fundamentally limited: task-agnostic routers cannot resolve conflicts between heterogeneous tasks (e.g., editing vs. customization), and the restricted capacity of LoRA experts hampers learning multi-task behaviors.
Our approach overcomes these limitations by introducing task-aware expert routing. We condition the gating mechanism on learnable embeddings corresponding to specific task categories, enabling dynamic selection of the most relevant experts. This mitigates inter-task conflicts, promotes effective specialization, and achieves superior performance across diverse image-to-image tasks while maintaining the efficiency of the MoE framework.
3 
Method
Figure 2
: 
Pipeline of our method. TAG-MoE consists of: (1) A 
MM-DiT with MoE
 layers; (2) A 
Hierarchical Task Semantic Annotation
 that labels training data with atomic task descriptors; (3) A novel Semantic-Aligned Router explicitly aligns MoE routing behavior with task semantics through 
Predictive Alignment Regularization
.
Our unified framework (Fig. 
2
) employs a Multimodal Diffusion Transformer (MM-DiT) with MoE layers for efficient, dynamic task handling (§
3.1
). We introduce hierarchical task semantic annotation (§
3.2
) and a novel semantic-aligned router (§
3.3
). This router guides the MoE’s specialization by aligning its routing decisions with these explicit task semantics in an interpretable manner .
3.1 
MoE-based Multimodal Diffusion Transformer
Building upon an MM-DiT architecture, our approach processes diverse inputs within a unified token sequence framework. To interpret user instructions, we employ a powerful pre-trained Multimodal Large Language Model (MLLM) to encode the input text 
c
t
​
e
​
x
​
t
c_{text}
 into a sequence of text embeddings 
C
C
. Separately, a pre-trained VAE encoder 
ℰ
\mathcal{E}
 maps both the conditional image 
I
c
I_{c}
 and the target image 
I
0
I_{0}
 into latent representations, 
z
c
z_{c}
 and 
z
0
z_{0}
. During training, Gaussian noise is sampled and added to the 
z
0
z_{0}
 to produce a noisy version 
z
t
z_{t}
. Both 
z
c
z_{c}
 and 
z
t
z_{t}
 are then patchified into sequences of visual tokens. Finally, the complete input to our MM-DiT is a single sequence formed by concatenating the text embeddings 
C
C
, the image tokens from 
z
c
z_{c}
, the image tokens from the noisy target latent 
z
t
z_{t}
, and a timestep embedding 
24
.
We replace the feed-forward networks (FFNs) of the image stream in diffusion transformer blocks with MoE layers. This leverages sparse activation to significantly increase model capacity at a fixed activation parameter, enabling superior performance over dense models with a comparable budget. We only implement MoE layers in the later transformer blocks as high-level semantic synthesis in these deeper layers benefits most from the increased capacity 
26
; 
9
.
The MoE layer consists of a set of 
N
N
 expert networks 
E
E
 and a gating network 
𝒢
\mathcal{G}
. The gating network 
𝒢
\mathcal{G}
 maps each input token to a probability distribution over the 
N
N
 experts, thereby determining their top 
k
k
 selections 
𝒯
⊆
{
E
1
,
…
,
E
N
}
\mathcal{T}\subseteq\left\{E_{1},\dots,E_{N}\right\}
. The output is a weighted sum of the activated experts’ outputs:
MoE
​
(
x
)
=
∑
E
i
∈
𝒯
⁡
(
x
)
𝒢
​
(
x
)
i
⋅
E
i
​
(
x
)
.
\text{MoE}(x)=\sum_{E_{i}\in\mathcal{T}(x)}\mathcal{G}(x)_{i}\cdot E_{i}(x).
(1)
This MoE-enhanced architecture is trained end-to-end using a Flow Matching objective.
3.2 
Hierarchical Task Semantic Annotation
To train a unified model that supports a broad range of generation and editing tasks, a structured representation of task semantics is essential. A single coarse label (e.g., “edit”) cannot capture user intent. For example, “change the background to a beach” and “make the person smile’ are both edits but require fundamentally different behaviors and preservation constraints.
To address this, we introduce a three-tier annotation scheme that provides each training instance (source image, instruction, target image) with a rich semantic descriptor: Scope - the task’s operational nature and spatial extent (e.g., global editing, local editing, content customization). Type — the semantic category of the manipulation (e.g., object editing, style transfer, attribute editing). Preservation — the invariants that must remain unchanged (e.g., identity, background, structure preservation).
An automated pipeline utilizing Qwen-VL 
1
 is established to analyze training triplets. It involves providing definitions of a three-tier system and instructing Qwen-VL to output atomic tags. The rule set is continuously refined to maintain consistency and semantic quality.
For instance, the task “Make the person in the photo wear sunglasses” would be annotated with tags such as “Scope: local editing; Type: object editing; Preservation: identity preservation, background preservation, style preservation”. This rich set of atomic tags forms the basis for our semantic representation.
Inference Stage.
 This hierarchical annotation scheme is exclusively used for training. During the inference stage, these ground-truth tags are no longer required. Instead, as a lightweight pre-processing step, we pass the user’s raw instruction 
c
t
​
e
​
x
​
t
c_{text}
 and the source image 
I
c
I_{c}
 to a VLM (e.g., Qwen-VL 
1
). The VLM performs instruction rewriting, analyzing the image and text to generate a more detailed, descriptive prompt. This enriched prompt is then encoded as the text embedding 
C
C
 and fed into the MM-DiT.
3.3 
Semantic-Aligned Gating Network
We design a novel semantic-aligned gating network to force the model’s internal routing strategy (encoded as a routing signature “
𝐠
\mathbf{g}
”) to predict the task’s macroscopic semantics (encoded as a semantic embedding “
𝐬
\mathbf{s}
”). This predictive alignment serves as a bridge, connecting local routing decisions with global task intent. Our mechanism comprises three key components: (1) construction of the global semantic embedding 
𝐬
\mathbf{s}
; (2) construction of the aggregated routing signature 
𝐠
\mathbf{g}
; and (3) the predictive alignment loss 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
.
3.3.1 
Global Semantic Embedding
Based on the hierarchical task semantic annotation described in §
3.2
, we first define a global vocabulary 
𝒱
\mathcal{V}
 containing all 
K
K
 atomic tags (e.g., “local editing”, “identity preservation”). We instantiate a learnable tag embedding matrix 
𝐖
t
​
a
​
g
∈
ℝ
K
×
D
\mathbf{W}_{tag}\in\mathbb{R}^{K\times D}
 for this vocabulary, where 
D
D
 is the model’s hidden dimension.
For a given training sample, its associated tags form a set 
T
p
⊆
𝒱
T_{p}\subseteq\mathcal{V}
 (e.g., 
T
p
=
{
T_{p}=\{
“local editing”, “face preservation”
}
\}
). To convert this variable-sized set 
T
p
T_{p}
 into a fixed-dimension vector 
𝐬
\mathbf{s}
, we first retrieve the corresponding embedding vector 
𝐞
t
=
𝐖
t
​
a
​
g
​
[
index
​
(
t
)
]
\mathbf{e}_{t}=\mathbf{W}_{tag}[\text{index}(t)]
 for each tag 
t
∈
T
p
t\in T_{p}
, and then aggregate them via element-wise summation.
This constructs the global semantic embedding 
𝐬
\mathbf{s}
, which represents the “macro-level semantic ground truth”:
𝐬
=
∑
t
∈
T
p
𝐖
t
​
a
​
g
​
[
index
​
(
t
)
]
.
\mathbf{s}=\sum_{t\in T_{p}}\mathbf{W}_{tag}[\text{index}(t)].
(2)
This vector 
𝐬
∈
ℝ
D
\mathbf{s}\in\mathbb{R}^{D}
 is permutation-invariant, meaning the order of tags does not affect the final representation. It serves as the structured supervisory signal for our subsequent alignment loss.
3.3.2 
Aggregated Routing Signature
Correspondingly, we require a vector to represent the internal routing strategy the model actually employs for the current sample. The gating network 
𝒢
\mathcal{G}
 (see §
3.1
) generates routing scores 
S
l
,
t
∈
ℝ
N
S_{l,t}\in\mathbb{R}^{N}
 for each token 
t
t
 in each of the 
L
L
 MoE layers, where 
N
N
 is the number of experts.
To obtain a single vector representing the expert usage pattern for the entire sample, we design an aggregated routing signature 
𝐠
\mathbf{g}
. First, we average the routing scores across all 
L
L
 MoE layers to get a per-token average score 
S
¯
t
=
1
L
​
∑
l
=
1
L
S
l
,
t
\bar{S}_{t}=\frac{1}{L}\sum_{l=1}^{L}S_{l,t}
. Next, we apply mean pooling over the sequence (token) dimension to get the final signature 
𝐠
∈
ℝ
N
\mathbf{g}\in\mathbb{R}^{N}
:
𝐠
=
1
T
​
∑
t
=
1
T
S
¯
t
=
1
T
⋅
L
​
∑
t
=
1
T
∑
l
=
1
L
S
l
,
t
.
\mathbf{g}=\frac{1}{T}\sum_{t=1}^{T}\bar{S}_{t}=\frac{1}{T\cdot L}\sum_{t=1}^{T}\sum_{l=1}^{L}S_{l,t}.
(3)
This vector 
𝐠
\mathbf{g}
 encodes which experts are activated on average to process the sample, capturing its 
de facto
 internal routing policy.
3.3.3 
Predictive Alignment Regularization
We now have two vectors: 
𝐬
∈
ℝ
D
\mathbf{s}\in\mathbb{R}^{D}
, representing what the task 
should be
, and 
𝐠
∈
ℝ
N
\mathbf{g}\in\mathbb{R}^{N}
, representing what the model 
actually do
. To align them, we introduce a lightweight prediction head 
ℋ
p
​
r
​
e
​
d
\mathcal{H}_{pred}
 (a two-layer MLP), to project the aggregated routing signature 
𝐠
\mathbf{g}
 from the expert space 
ℝ
N
\mathbb{R}^{N}
 into the semantic space 
ℝ
D
\mathbb{R}^{D}
, yielding a predicted semantic embedding 
𝐬
^
=
ℋ
p
​
r
​
e
​
d
​
(
𝐠
)
\hat{\mathbf{s}}=\mathcal{H}_{pred}(\mathbf{g})
.
We force the routing strategy to predict the task semantics by minimizing the cosine similarity loss between 
𝐬
^
\hat{\mathbf{s}}
 and 
𝐬
\mathbf{s}
. This is our Predictive Alignment Loss 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
:
ℒ
a
​
l
​
i
​
g
​
n
=
1
−
sim
​
(
𝐬
^
,
𝐬
)
=
1
−
𝐬
^
⋅
𝐬
|
𝐬
^
|
​
|
𝐬
|
.
\mathcal{L}_{align}=1-\text{sim}(\hat{\mathbf{s}},\mathbf{s})=1-\frac{\hat{\mathbf{s}}\cdot\mathbf{s}}{|\hat{\mathbf{s}}||\mathbf{s}|}.
(4)
Minimizing 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
 trains the parameters of 
ℋ
p
​
r
​
e
​
d
\mathcal{H}_{pred}
 and, more importantly, backpropagates the gradient through 
𝐠
\mathbf{g}
 to the gating networks 
𝒢
\mathcal{G}
 of all MoE layers. This compels 
𝒢
\mathcal{G}
 to evolve from a task-agnostic executor into a semantic-aware scheduler: it must learn to route tokens intelligently, such that the resulting aggregate signature 
𝐠
\mathbf{g}
 contains sufficient information to predict the global task 
𝐬
\mathbf{s}
.
3.3.4 
Overall Training Objective
Our proposed 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
 is an auxiliary loss that complements the model’s primary objective. The final overall loss 
ℒ
t
​
o
​
t
​
a
​
l
\mathcal{L}_{total}
 is a weighted sum of the main generation loss (e.g., 
ℒ
f
​
l
​
o
​
w
\mathcal{L}_{flow}
), the standard MoE load balancing loss 
ℒ
l
​
b
​
l
\mathcal{L}_{lbl}
, and our semantic alignment loss 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
:
ℒ
t
​
o
​
t
​
a
​
l
=
ℒ
f
​
l
​
o
​
w
+
λ
l
​
b
​
l
​
ℒ
l
​
b
​
l
+
λ
a
​
l
​
i
​
g
​
n
​
ℒ
a
​
l
​
i
​
g
​
n
,
\mathcal{L}_{total}=\mathcal{L}_{flow}+\lambda_{lbl}\mathcal{L}_{lbl}+\lambda_{align}\mathcal{L}_{align},
(5)
where 
λ
l
​
b
​
l
\lambda_{lbl}
 and 
λ
a
​
l
​
i
​
g
​
n
\lambda_{align}
 are hyperparameters that balance the contribution of each loss term.
3.4 
Dataset Construction
Our model is trained on a large-scale, diverse dataset comprising both publicly available and proprietary in-house data, totaling over 11 million samples. This hybrid approach ensures broad coverage across the unified task space. The public portion (2.2M samples) is compiled from established benchmarks, including InstructP2P 
2
, UltraEdit 
44
, and OmniEdit 
33
 for universal instructive editing, supplemented by VTON-HD 
6
 for virtual try-on tasks and Ominicontrol 
30
 for subject driven generation.
Our proprietary in-house dataset is meticulously constructed using a multi-stage pipeline to cover a wide spectrum of specialized tasks. First, we source pristine images from large-scale public datasets. Next, we employ large language models (e.g., GPT-4o 
22
) to generate a vast array of diverse editing and generation instructions for these images. To obtain high-quality target images, we utilize a combination of specialist and generalist models: for instance, specialist models like ControlNet 
42
 are used for “Control generation” tasks, while powerful generalist models (e.g., Flux-Kontext 
16
, Qwen-Edit 
34
, and SeedEdit 
32
) are employed for a broad range of edits. Following the methodology of UniReal 
5
, we also process video frames to create dynamic editing datasets (e.g., for pose/view changes). Finally, to enhance robustness and quality, we systematically augment the data by constructing corresponding inverse tasks and instructions (e.g., pairing “object addition” with “object removal”), which significantly improves generative fidelity.
4 
Experiments
4.1 
Implenentation Details
Our model is based on Qwen-Image T2I model 
34
, we integrate the MoE layers by replacing the standard FFNs of the image stream in the final 10 layers of our diffusion transformer. Each MoE layer consists of four experts, where each expert possesses an architecture identical to the original FFN it replaces. The gating network is implemented as a two-layer MLP, and we employ a top-1 routing strategy.
4.2 
Experiments Settings
Baselines.
We compare our method against three categories of SOTA baselines.
(1) Unified generation and editing methods for diverse image-to-image tasks, including ACE++ 
20
, Flux.1 Kontext 
16
, BAGEL 
10
, OmniGen2 
35
, Qwen-Edit 
35
 and DreamOmni2 
36
.
We also include comparisons against product-level, closed-source models (e.g. GPT-4o 
22
 and Gemini-2.5-flash (aka. Nano-banana) 
13
, to contextualize our performance. However, our primary quantitative evaluation and main claims are benchmarked against open-source baselines.
(2) Specialized zero-shot instruction-based editing methods, including InstructPix2Pix 
2
, EmuEdit 
27
, MagicBrush 
41
, UltraEdit 
44
, ICEdit 
23
, and Step1X-Edit 
19
.
(3) Specialized zero-shot subject-driven generation methods, including DreamO 
21
, OminiControl 
30
 and UNO 
wu2025less
.
Evaluation benchmarks.
To comprehensively assess our model in the unified image generation and editing setting, we adopt ICE-Bench 
23
 as our primary benchmark, as it is specifically designed for unified models and spans both diverse editing tasks and subject-driven generation. For more fine-grained evaluation, we further include specialized benchmarks: EmuEdit-Bench 
27
 and GEdit-Bench 
19
 for detailed editing analysis, and DreamBench++ 
25
 together with OmniContext 
35
 to evaluate subject-driven generation performance.
Metrics.
We employ a comprehensive set of metrics to evaluate both visual quality and task correctness. Aesthetic quality is assessed using a SigLip-based predictor. Consistency with the source image is measured via CLIP-src (for editing) and CLIP-ref (for subject-driven generation), while text alignment is captured by CLIP-cap.
For editing evaluation, we further use Qwen2-VL-72B 
31
 to determine whether the instruction is correctly executed based on the source image, instruction, and output image, yielding the vllmqa score. For subject-driven tasks, we assess three key preservation dimensions: facial identity (Face-ref, using the buffalo model from InsightFace App 
8
), subject similarity (DINO-ref, via DINO 
4
), and style fidelity (Style-ref, via CSD 
28
).
All metrics not originally within the [-1, 1] range are normalized. For every metric reported, higher values indicate better performance. In the tables, the best results are highlighted 
in bold
, and the second-best results are 
underlined
.
Figure 3
: 
Qualitative comparison on diverse tasks.
Our model successfully resolves complex task conflicts where baselines fail.
4.3 
Quantitative Comparison
Unified generation evaluation.
We report the main results on ICE-Bench in Tab. 
1
. Our method achieves the highest scores among all open-source baselines across three key metrics: aesthetic quality, CLIP-cap, and vllmqa. Notably, our CLIP-cap score not only surpasses all open-source competitors but also exceeds closed-source, product-level models such as GPT-4o and Gemini-2.5-flash, indicating stronger alignment with user instructions across diverse generation and editing tasks.
Although some baselines exhibit high source fidelity (e.g., DreamOmni2 on CLIP-src), our model attains a more favorable overall balance by excelling in instruction adherence and semantic alignment.
We further present a per-category breakdown over 26 task types on ICE-Bench, visualized in the radar charts in Fig. 
4
. Our model achieves state-of-the-art performance in the vast majority of categories, demonstrating robust and well-balanced capability. DreamOmni2’s high reference-generation scores largely stem from copy-paste behavior on source subjects, which artificially inflates similarity metrics.
Method
Aes.
CLIP-src
CLIP-cap
CLIP-ref
vllmqa
ACE++
5.219
0.851
0.263
0.713
0.637
Kontext
5.165
0.863
0.274
0.728
0.629
BAGEL
4.757
0.863
0.276
0.687
0.699
OmniGen2
5.238
0.855
0.279
0.728
0.787
Qwen-Edit
5.358
0.840
0.279
0.671
0.774
DreamOmni2
5.188
0.866
0.268
0.739
0.664


Ours
5.399
0.857
0.282
0.732
0.852
GPT-4o
5.801
0.823
0.278
0.693
0.889
Gemini-2.5-flash
5.571
0.879
0.281
0.724
0.847
Table 1: 
Comparison results for unified tasks on ICE-Bench 
23
 test sets. Open-source models are in the first block and close-source produce-level models are in the second block.
Figure 4
: 
Comprehensive scores on different image editing and generation tasks. 
Image editing evaluation
We further evaluate our model against specialized zero-shot editing baselines on EmuEdit-bench 
27
 and GEdit-bench 
19
, with results shown in Tab. 
2
. (Note: Since EmuEdit is not open-source and only provides pre-generated outputs on its own benchmark, its performance on GEdit-bench is unavailable.)
Although our model does not achieve top-1 performance on every metric, it clearly leads on the most important indicator vllmqa achieving the highest scores on both benchmarks. This is particularly noteworthy because, unlike static CLIP similarity, vllmqa uses a powerful VLLM to evaluate the correctness of the executed instruction, offering a more intelligent and reliable measure of editing success. Our strong results on this metric underscore the model’s advanced instruction-following capability.
Method
EmuEdit-bench
GEdit-bench
CLIP-src
CLIP-cap
vllmqa
CLIP-src
CLIP-cap
vllmqa
InsP2P
0.8589
0.2919
0.2507
0.8604
0.3192
0.3191
EmuEdit
0.8854
0.3098
0.6253
-
-
-
MagicBrush
0.8552
0.2951
0.4573
0.8068
0.3146
0.3783
UltraEdit
0.8625
0.3075
0.3609
0.8459
0.3323
0.4605
ICEdit
0.8912
0.3026
0.3609
0.9007
0.3283
0.4145
Step1X-Edit
0.8845
0.3119
0.7893
0.8967
0.346
0.8158
ACE++
0.8367
0.2385
0.0606
0.8160
0.2518
0.0559
Kontext
0.9091
0.3093
0.741
0.9190
0.3419
0.7303
BAGEL
0.8565
0.3129
0.7989
0.8727
0.3470
0.7961
OmniGen2
0.8932
0.3087
0.5978
0.8940
0.3373
0.6546
Qwen-Edit
0.8832
0.3159
0.9174
0.9104
0.3522
0.875
DreamOmni2
0.9035
0.3096
0.6997
0.9229
0.3401
0.6349
Ours
0.9054
0.3152
0.9284
0.9238
0.3485
0.8854
Table 2: 
Comparison of instruction-based editing methods on EmuEdit-bench and GEdit-bench with multiple metrics.
Method
DreamBench++
OmniContext
CLIP-cap
CLIP-ref
DINO-ref
Face-ref
Style-ref
CLIP-cap
CLIP-ref
DINO-ref
Face-ref
Style-ref
DreamO
0.2899
0.7792
0.7518
0.335
0.5355
0.2986
0.7302
0.7075
0.4522
-
Ominicontrol
0.296
0.7642
0.6991
0.0579
0.3876
0.3067
0.7009
0.6126
-
-
UNO
0.2832
0.776
0.7429
0.2572
0.4328
0.2962
0.7106
0.6961
0.3665
-
ACE++
0.2791
0.7759
0.732
0.1636
0.5306
0.2832
0.7183
0.6932
0.1789
-
Kontext
0.2829
0.819
0.7919
0.3429
0.5655
0.2962
0.765
0.7494
0.5596
-
BAGEL
0.3036
0.7338
0.6998
0.0487
0.5065
0.2914
0.7188
0.7094
0.1264
-
OmniGen2
0.298
0.7712
0.752
0.1213
0.5167
0.3056
0.7544
0.7289
0.3919
-
Qwen-Edit
0.3009
0.7595
0.7187
0.2188
0.5095
0.3152
0.7115
0.6797
0.3019
-
DreamOmni2
0.2731
0.8062
0.8008
0.2344
0.5364
0.2848
0.7733
0.7611
0.5111
-
Ours
0.3011
0.7906
0.7613
0.3678
0.5679
0.3096
0.7297
0.7628
0.5607
-
Table 3: 
Comparison of subject-driven generation methods on DreamBench++ and OmniContext with multiple metrics.
Subject driven evaluation.
We evaluate our model’s fine-grained preservation ability against specialized subject-driven generation methods on DreamBench++ and OmniContext, with results shown in Tab. 
3
. We focus on metrics that measure subject, identity, and style fidelity (noting that OmniContext does not include style-related tasks).
The results indicate strong preservation performance: our model achieves SOTA Face-ref scores on both benchmarks and the highest Style-ref score on DreamBench++. In addition, we obtain the top DINO-ref score on OmniContext and remain highly competitive on DreamBench++. These findings demonstrate that our unified model can match or surpass specialized models, effectively mitigating the typical tension between subject fidelity and generative diversity.
Figure 5
: 
Compare with specialized image editing models and subject-driven generation models.
4.4 
Qualitative Comparison
Qualitative comparison with unified baselines.
As demonstrated in the preceding qualitative comparison (Fig. 
3
), our method consistently surpasses SOTA baselines in complex tasks characterized by interfering intents.
These unified models typically fail to resolve inherent task conflicts, resulting in critical failures such as “copy-paste” artifacts in subject-driven generation, stylistic dissonance during inpainting, or incomplete execution in compositional editing.
Our approach successfully navigates these challenges by utilizing the Predictive Alignment Regularization. This mechanism effectively decouples and routes conflicting sub-tasks (e.g. local semantic edits versus global style preservation) to specialized experts, thereby mitigating the core task interference that plagues unified models.
Qualitative comparison with specialized baselines.
We further present a comprehensive comparison against specialized image editing methods (InstructPix2Pix 
2
, MagicBrush 
41
, UltraEdit 
44
, ICEdit 
43
) and subject-driven models (DreamO 
21
, OmniControl 
30
, UNO 
wu2025less
) in Fig. 
5
. For image editing, specialized baselines struggle with significant structural or geometric changes. As shown in the silver car case, they fail to execute the complex motion of turning around, resulting in minor texture changes; similarly, they fail to synthesize the side view of the complex shelf structure. In contrast, our method accurately handles these 3D-aware edits, benefiting from the structural diversity and geometric awareness implicitly learned from subject-driven data. Conversely, in subject-driven tasks, specialized models often compromise identity or instruction following. For the human subject, baselines either lose facial identity/clothing details (OmniControl) or fail to render the office context (UNO). For the toy subject requiring a handstand, baselines generate incorrect upright poses. Our method, however, maintains robust identity while adhering to complex motion instructions. This enhanced fidelity is attributed to the high consistency derived from editing alignment data during unified training. Overall, our model effectively handles both task types by leveraging semantic-aligned routing. This mechanism assigns conflicting objectives to specialized experts, enabling cross-task benefits: generative diversity from subject data improves editing geometry, while fidelity constraints from editing data enhance identity preservation in generation.
4.5 
Ablation Study
Effectiveness of the MoE architecture.
We compare our sparse MoE architecture to a dense baseline of an equivalent activated parameter count. This dense model shows a severe performance drop on ICE-Bench metrics (Tab.
4
) and slower convergence (Fig. 
6
 left). This validates that the sparse architecture is fundamentally more effective at mitigating the severe task interference inherent in the unified task space than a computationally-equivalent dense model.
Effect of predictive alignment regularization.
We ablate the semantic-alignment loss by removing 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
. Without this loss, the MoE gating network performs task-agnostic expert selection, receiving no semantic guidance from our hierarchical tags. As shown in Tab. 
4
, this variant exhibits substantial degradation across all major metrics.
This finding is key: a sparse MoE architecture alone is not sufficient. 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
 is what enables semantically guided routing, which is essential for mitigating task interference.
Notably, the MoE w/o 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
 variant still surpasses the dense baseline, benefiting from the larger effective capacity of the sparse MoE structure, which allows exploration of a richer solution space under the same computational budget.
Figure 6
: 
Left: Training loss curves of the dense and MoE architecture. Right: Token strategy in different generation tasks.
Analysis of expert specialization.
To provide direct evidence of our method’s success, we visualize the inference-time routing decisions and analyze the internal expert activation patterns.
Our analysis is a two-step process. First, we compute an “Expert Utilization Rate” for each MoE layer (shown as the heatmap in the middle of Fig. 
6
), which represents the percentage of total image tokens routed to each expert. A utilization of 0% (blue) or 100% (red) indicates no specialization. We focus our analysis on layers exhibiting differentiated routing, where utilization is mixed (near white), as this is where functional specialization occurs.
Second, for these active layers, we visualize the per-token routing scores for each expert, reshaping them to the image’s spatial dimensions. In these token heatmaps, a high score (blue) indicates that the corresponding image tokens are strongly routed to that specific expert. The results reveal a clear, spatially-aware, and task-specific specialization. For Change Material and Change Color, the model activates distinct combinations of experts. Critically, the token heatmaps for these active experts show that computation is spatially concentrated on the backpack’s pixels, precisely the region relevant to the edit. The non-relevant background tokens are correctly routed to other experts (or have near-zero activation for these experts).
This analysis provides strong evidence that our model has learned a sophisticated specialization that is both task-specific (using unique expert combinations for different tasks) and spatially-aware (experts learn to process semantically relevant image regions). This confirms our method successfully resolves task conflicts by dispatching them to distinct, specialized computational pathways.
xxx
Method
DINO-ref
Face-ref
Style-ref
CLIP-src
CLIP-cap
vllmqa
Dense
0.7196
0.3544
0.5177
0.851
0.263
0.637
MoE w/o 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
0.7355
0.3779
0.5251
0.863
0.274
0.677
MoE w/ 
ℒ
a
​
l
​
i
​
g
​
n
\mathcal{L}_{align}
0.7620
0.4642
0.5679
0.879
0.281
0.847
Table 4: 
Ablation study on dense model and predictive alignment regularization.
4.6 
User study
We conducted a user study with 65 participants on 50 cases from ICE-Bench 
23
. Participants were asked to select the single best result according to three criteria: (1) Reference Alignment (consistency with the source image), (2) Prompt Alignment (faithfulness to the textual instruction), and (3) Overall Preference (overall visual quality).
In total, 350 sets were evaluated, and the aggregated results are shown in Fig. 
7
. The results reveal a clear and consistent preference for our method, which achieved the highest selection rate across all three evaluation criteria.
Figure 7
: 
User study on reference alignment, prompt alignment and overall perference.
5 
Limitations and Future Work
A key limitation is our framework’s lack of unified input understanding. Our model relies on pre-processed instructions (the intent) and cannot jointly reason over this intent and the visual content of the source image. This separation restricts tasks requiring integrated semantic and perceptual understanding.
For instance, our model fails at content-based reasoning (e.g., solving a math problem in an image) because it understands the editing intent (e.g., scope, type) but not the contextual information in the pixels themselves.
A promising future direction is an end-to-end system incorporating a multimodal reasoning engine to unify perceptual understanding (content), intent comprehension (command), and conceptual generation (reasoning).
6 
Conclusion
In this paper, we propose TAG-MoE, a task-aware MoE framework for unified image generation and editing. We identify the task-agnostic routing as the core bottleneck for applying MoE to diverse, conflicting tasks. To address this, we introduce a Hierarchical Task Semantic Annotation scheme and Predictive Alignment regularization to effectively injects global task intent into the local routing decisions, forcing the model to develop meaningful expert specialization. Our experiments demonstrat
