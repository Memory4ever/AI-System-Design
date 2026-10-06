[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Scaling View Synthesis Transformers

[3] h6: Abstract

[4] p: Geometry-free view synthesis transformers have recently achieved state-of-the-art performance in Novel View Synthesis (NVS), outperforming traditional approaches that rely on explicit geometry modeling. Yet the factors governing their scaling with compute remain unclear. We present a systematic study of scaling laws for view synthesis transformers and derive design principles for training compute-optimal NVS models. Contrary to prior findings, we show that encoder–decoder architectures can be compute-optimal; we trace earlier negative results to suboptimal architectural choices and comparisons across unequal training compute budgets. Across several compute levels, we demonstrate that our encoder–decoder architecture, which we call the Scalable View Synthesis Model (SVSM), scales as effectively as decoder-only models, achieves a superior performance–compute Pareto frontier, and surpasses the previous state-of-the-art on real-world NVS benchmarks with substantially reduced training compute. https://www.evn.kim/research/svsm

[5] h2: 1 Introduction

[6] figure: Figure 1 : Scaling Laws for View Synthesis Transformers. Evaluated on RealEstate10K [ 34 ] , our SVSM exhibits a 3 × 3\times more compute-optimal Pareto frontier than LVSM while retaining the same scaling behavior (similar slope and curvature everywhere).

[7] p: Given a set of images of a scene with known camera poses, the goal of Novel View Synthesis (NVS) is to render novel views of the scene from arbitrary viewpoints. Single scene approaches such as NeRF [ 16 ] and Gaussian Splatting [ 12 ] have achieved impressive fidelity by explicitly modeling 3D geometry and rendering. Feed-forward extensions of these frameworks train neural networks to reconstruct the 3D representation, achieving promising results [ 29 , 2 , 3 , 31 ] . However, their formulation inherits handcrafted 3D structure, constraining their ability to scale and handle more complex artifacts such as reflections or transparency.

[8] p: Typified by Large View Synthesis Model (LVSM) [ 10 ] , a new class of view synthesis models have emerged which achieve state-of-the-art rendering quality using pure transformer architectures with fewer (if any) geometric inductive biases [ 10 , 9 , 17 , 22 ] . However, this class of models is relatively new, and their design space remains unexplored. In particular, training a NVS model involves making design choices over a large number of variables, including the number of context and target views, camera pose parameterizations, attention mechanisms, etc., and there does not yet exist a rigorous investigation of how these choices affect the performance, training efficiency, and inference throughput. To this point, while there exist extensive scaling analyses in language modeling and 2D vision [ 7 , 8 , 11 , 19 , 30 ] , there exists no analogue for 3D vision. Thus, the goal of this work is to provide such an analysis in addition to a compute-optimal training recipe for view synthesis transformers in terms of both architecture and training strategy.

[9] p: In particular, we first challenge the necessity of the decoder-only architecture proposed in LVSM [ 10 ] . While powerful, it requires passing all context images through the entire transformer each time a single target image is decoded. It is a bidirectional model where both the target view tokens and context view tokens are updated in each layer of the network. While this allows the model to consider only information in the context images that is relevant to the target view, it incurs substantial computational cost due to repeated processing of context views.

[10] p: Instead, we advocate for an encoder-decoder design which produces an intermediate scene latent representation. This approach is potentially far more efficient: the computational cost of constructing the scene representation is amortized through repeated calls to the decoder, which efficiently extracts information from the representation via unidirectional cross attention from scene to target. However, the scene representation also represents an information bottleneck. Without a proper training strategy that maximally leverages the efficiency of the encoder-decoder design, it can be challenging for encoder-decoder models to outperform decoder-only models. Here, we identify that the key for unlocking the potential of encoder-decoder models lies in the way target views ( i.e. the reconstruction targets) are utilized during training. The implicit standard practice employed by prior work [ 2 , 10 , 22 , 31 ] has been to reconstruct multiple different target views from a single scene during training. However, the consequences of this approach have never been fully analyzed. To this point, we propose and empirically validate the effective batch hypothesis , which argues that reconstructing multiple target views per scene effectively multiplies the batch size.

[11] p: These insights yield a principled transformer view synthesis model, which we call the Scalable View Synthesis Model (SVSM), that fully capitalizes on the rendering efficiency of a unidirectional encoder-decoder architecture, maximizing training throughput without compromising performance or scalability. We demonstrate that our unidirectional model scales as efficiently as bidirectional models, which aligns with the scalability of causal, unidirectional attention in large language models [ 11 ] . As part of this analysis, we also reveal scaling relationships within view synthesis that parallel those observed in the Chinchilla language model family [ 8 ] . Finally, we demonstrate that SVSM achieves state-of-the-art results in real-world NVS tasks with significantly reduced compute, challenging the previous understanding that bidirectional attention is critical to high-fidelity view synthesis [ 10 ] .

[12] h4: Key Contributions:

[13] p: We provide the first rigorous scaling analysis for novel view synthesis transformers.

[14] p: We propose and empirically confirm the effective batch size hypothesis that unlocks compute-optimal training.

[15] p: We show that bidirectional decoding is not critical for scalable view synthesis, contrasting recent work [ 10 ] .

[16] p: Based on this analysis, we present a compute-optimal model that achieves a new state-of-the-art in real-world NVS tasks with substantially reduced training compute.

[17] h2: 2 Related Work and Preliminaries

[18] h4: Generalizable novel view synthesis.

[19] p: In generalizable novel view synthesis, we are given a set of V C V_{C} context images paired with known camera poses and intrinsics ℭ = { ( I i , g i , K i ) ∣ i = 1 , … , V C } \mathfrak{C}=\left\{(I_{i},\,g_{i},\,K_{i})\mid i=1,\,\ldots,\,V_{C}\right\} . The typical objective is to synthesize an unseen view of the same scene given a target camera configuration g T , K T g_{T},K_{T} :

[20] table: I ~ T = Render ⁡ [ ℭ , g T , K T ] . \tilde{I}_{T}=\mathrm{Render}\big[\mathfrak{C},g_{T},K_{T}\big]. (1)

[21] p: One line of work attempts to solve this problem with neural network architectures that explicitly model aspects of 3D image formation, for instance, via differentiable rendering or using epipolar line constraints [ 29 , 24 , 2 , 26 , 25 ] . In contrast, geometry-free methods avoid explicit geometric modeling in favor of flexibility and generality [ 6 , 23 , 22 , 20 , 21 ] . Here, we are primarily interested in a recently proposed subclass of these models which achieve state-of-the-art results with pure transformer architectures [ 10 , 9 , 22 , 17 ] . In particular, we seek to study the “Large View Synthesis Model” (LVSM) [ 10 ] , which achieves state-of-the-art NVS performance and serves as the prototypical instance of the view synthesis transformer. LVSM can be implemented in two ways: as either an encoder-decoder model or decoder-only model. The authors’ proposed decoder-only variant is far more performant, so we primarily consider this architecture (pictured in Fig. 2 , left) in our analysis.

[22] figure: Figure 2 : Architectures of the current SOTA, the decoder-only LVSM [ 10 ] (a) and SVSM (ours, b). Our cross-attention based decoder enables parallel rendering of multiple target views after a single scene encoding. Each target view is decoded independently given the shared scene representation, but the cross-attention allows these independent decodings to be executed in parallel.

[23] p: Decoder-only LVSM consists of a single module: A decoder 𝒟 \mathcal{D} which ingests the raw context ℭ \mathfrak{C} along with a single target configuration, and aims to render a prediction of the target view I ~ T = 𝒟 ⁡ [ ℭ , g T , K T ] \tilde{I}_{T}=\mathcal{D}\big[\mathfrak{C},g_{T},K_{T}\big] . This model is bidirectional as the context view tokens are updated with information about target pose and tokens in each layer. Thus, the processed context tokens cannot be reused and must be re-initialized and updated each time a new target view is rendered. As a consequence, rendering V T V_{T} target views requires V T V_{T} forward passes through the full network. Decoder-only LVSM consists of standard ViT layers [ 5 ] which apply self-attention ( 𝙰𝚝𝚝𝚗 \mathtt{Attn} ) followed by an MLP ( 𝙼𝙻𝙿 \mathtt{MLP} ). Therefore, the FLOPs on a forward pass scale linearly with the number of target views V T V_{T}

[24] table: χ 𝙼𝙻𝙿 (LVSM) ∝ V T × ( V C + 1 ) χ 𝙰𝚝𝚝𝚗 (LVSM) ∝ V T × ( V C + 1 ) 2 \begin{split}\chi_{\mathtt{MLP}}^{\text{(LVSM)}}&\propto V_{T}\times(V_{C}+1)\\ \chi_{\mathtt{Attn}}^{\text{(LVSM)}}&\propto V_{T}\times(V_{C}+1)^{2}\end{split} (2)

[25] p: where χ 𝙼𝙻𝙿 (LVSM) \chi_{\mathtt{MLP}}^{\text{(LVSM)}} and χ 𝙰𝚝𝚝𝚗 (LVSM) \chi_{\mathtt{Attn}}^{\text{(LVSM)}} are the FLOPs consumed by the MLP and attention in the decoder-only LVSM. In our studies, χ 𝙼𝙻𝙿 (LVSM) \chi_{\mathtt{MLP}}^{\text{(LVSM)}} is the dominating factor (for more details, see Supp 9 ). In what follows, we will continue to use χ \chi to denote the compute metric, typically measured in FLOPs.

[26] h4: Scaling Laws.

[27] p: As the scale of deep learning models continues to increase, it has become increasingly important to understand the relationship between performance and compute to ensure an efficient use of resources. To this end, scaling analyses have been conducted for language models [ 8 , 11 ] , vision transformers [ 30 ] , and diffusion transformers [ 7 , 19 ] . The general approach is straightforward: train models at different compute budgets and analyze performance as a function of compute.

[28] p: Scaling studies are useful in two ways. First, they provide a predictable trend of performance with compute, essentially describing a performance metric P P as function of compute χ \chi which can reveal characteristic scaling behavior. For example, in language models, P ⁡ ( χ ) P(\chi{}) has been found to approximately follow a power-law [ 11 ] . Second, they have revealed which hyperparameter choices are most effective as models scale. For instance, Chinchilla scaling laws [ 8 ] reveal the best way to trade-off between model size N N , measured in parameter count, and the number of training samples used, D D . Analysis is performed by sweeping across a wide range of N N and D D to discover for compute budget χ \chi{} the optimal N N and D D . Then, taking this paired data and assuming a power law relation between N opt N_{\text{opt}} and D opt D_{\text{opt}} and χ \chi{} , one can fit powers a a and b b of χ \chi{} to the pairings

[29] table: N opt ( χ ) ∝ χ , a D opt ( χ ) ∝ χ . b N_{\text{opt}}(\chi{})\propto\chi{}^{a},D_{\text{opt}}(\chi)\propto\chi{}^{b}. (3)

[30] p: Remarkably, experiments demonstrate a ≈ b a\approx b , suggesting N N and D D should scale proportionally. In our study, we will focus on the second of these two kinds of studies: replicating the Chinchilla study (Sec. 5 ) in the NVS domain and exploring other similar tradeoffs, such as the effective batch size (Sec. 4 )

[31] h4: Extremely long context view synthesis.

[32] p: Recently, there has been a line of work aiming to develop view-synthesis and 3D-reconstruction models whose computational cost scales linearly with the number of context images [ 33 , 27 , 35 ] . Indeed, as in Eq. 2 , as V C V_{C} grows, the quadratic cost of attention comes to dominate the compute and becomes infeasible. In that regime, such linear-cost models are promising alternatives. However, we restrict our focus to sparse to moderately sparse view synthesis, for which linear-cost models are currently not state of the art.

[33] figure: Figure 3 : Effective Batch Size . Training loss (smoothed with a rolling-average) and test PSNR measured throughout training across various paired B B and V T V_{T} runs provide evidence for our effective batch size hypothesis: Models trained with the same product of number of scenes in the batch B B and number of reconstruction target views V T V_{T} , i.e. runs with the same effective batch size B eff B_{\text{eff}} , perform the same and are colored identically. On V C = 8 V_{C}=8 (top) , we sweep across B eff = B_{\text{eff}}= 128 , 256 on DL3DV, and on V C = 2 V_{C}=2 (bottom) , we sweep across B eff = B_{\text{eff}}= 128 , 1024 on RealEstate10K.

[34] h2: 3 Encoder-Decoder View Synthesis

[35] p: As discussed in Sec. 1 and Sec. 2 , the decoder-only LVSM may not be the most compute-optimal due to the recomputation per-target view rendered. This motivates us to seek an alternative model with a fixed scene representation that can be decoded in a purely unidirectional manner ( i.e. via cross attention) to reduce the cost of rendering and avoid redundant reprocessing of context information. To this extent, we introduce the Scalable View Synthesis Model (SVSM), which can be viewed as a simple modification to encoder-decoder LVSM. Specifically, our architecture implements Eq. 1 by first processing the context set ℭ \mathfrak{C} with a transformer encoder, producing a set of latent tokens (a “scene representation”) 𝐳 = ℰ ⁡ [ ℭ ] \mathbf{z}=\mathcal{E}[\mathfrak{C}] . The encoder ℰ \mathcal{E} is standard transformer with full bidirectional self-attention. Unlike encoder-decoder LVSM, we do not employ a fixed-size scene representation, but instead take the set of encoded context image patch tokens as the scene representation to avoid introducing a bottleneck. To render a novel view, a cross-attention based decoder 𝒟 \mathcal{D} ingests the target configuration and the fixed scene latent tokens 𝐳 \mathbf{z} to render the target view, I ~ = D ⁡ [ 𝐳 , g T , K T ] \tilde{I}=D\big[\mathbf{z},\,g_{T},K_{T}\big] . To render multiple images of the same scene, we only require encoding the context set once, re-using the scene embedding 𝐳 \mathbf{z} . As with LVSM, each novel view is decoded independently given 𝐳 \mathbf{z} (i.e., there is no interaction between target views). However, because the decoder uses cross-attention rather than bidirectional self-attention over all tokens, these independent target views can be decoded in parallel, without redundant recomputation of the scene representation.

[36] p: To be more concrete, this architecture reduces the complexity of rendering V T V_{T} targets to

[37] table: χ 𝙼𝙻𝙿 (SVSM) ∝ V T + V C χ 𝙰𝚝𝚝𝚗 (SVSM) ∝ V C × ( V T + V C ) . \begin{split}\chi_{\mathtt{MLP}}^{\text{(SVSM)}}&\propto V_{T}+V_{C}\\ \chi_{\mathtt{Attn}}^{\text{(SVSM)}}&\propto V_{C}\times(V_{T}+V_{C}).\end{split} (4)

[38] p: In other words, assuming most of the compute is due to the MLP layers (see Supp 9 ), rendering V T V_{T} target views requires 𝒪 ⁡ ( V T + V C ) \mathcal{O}(V_{T}+V_{C}) FLOPs. In the limit of inference where V T ≫ V C V_{T}\gg V_{C} , this reduces to 𝒪 ⁡ ( V T ) \mathcal{O}(V_{T}) , in stark contrast to the 𝒪 ⁡ ( V T ​ V C + V T ) \mathcal{O}(V_{T}V_{C}+V_{T}) of LVSM (see Eq. 2 ). Further, the benefit of this paradigm extends beyond inference. As long as we are training with multiple target views, as is standard practice [ 2 , 10 , 22 , 31 ] , the parallel nature of unidirectional decoding can save substantial training compute.

[39] p: However, this reduction comes with a cost. Unlike LVSM, our encoder cannot proactively discard information irrelevant to the target view but instead needs to encode all necessary information for rendering any target view. Indeed, parameter count and training steps being equal, SVSM performs worse than LVSM. However, as we will show, SVMS’s amortized rendering enables us to dramatically increase its size and training steps, such that when normalized by compute budget, SVSM significantly outperforms LVSM.

[40] h2: 4 The Effective Batch Size for View Synthesis

[41] p: As the cost of a forward pass scales both with the number of different scenes (the batch size B B ) as well as the number of target views ( V T V_{T} ) that we seek to render per scene, this introduces an additional hyperparameter into the training regime: What is the optimal trade-off between the number of target views and the number of different scenes? We study this question empirically and reveal that what matters is the product of target views and batch size, which we call the effective batch size of a NVS model.

[42] h4: Analysis Setup.

[43] p: We define effective bath size as B eff ≡ B ⋅ V T B_{\text{eff}}\equiv B\cdot V_{T} , where B B is the number of scenes in a training batch, and V T V_{T} is the number of rendering targets used per training scene. We train both decoder-only LVSM and the proposed SVSM models across two datasets — DL3DV [ 15 ] and RealEstate10K [ 34 ] (RE10K) — with V C = 8 V_{C}=8 and V C = 2 V_{C}=2 while holding B eff B_{\text{eff}} constant and varying B B and V T V_{T} . Specifically, we test B eff = 128 B_{\text{eff}}=128 on both datasets, and additionally test B eff = 1024 B_{\text{eff}}=1024 on RE10K and B eff = 256 B_{\text{eff}}=256 on DL3DV. For DL3DV we use the official test-train split, and for RE10K, we use the pixelSplat [ 2 ] test-train split. Further training details are outlined in Supp 10 .

[44] h4: Effective Batch Size is What Matters.

[45] p: Results for all training runs are shown in Fig. 3 . Remarkably, in all cases – across both models, both V C V_{C} settings, and all B eff B_{\text{eff}} sets – the test metric and the training loss behavior remain approximately constant along a B eff B_{\text{eff}} -level set. This effect is especially clear in the V C = 8 V_{C}=8 case, where the test PSNR varies by at most ± 0.1 \pm 0.1 and remains present in the V C = 2 V_{C}=2 case, where the variation is at most ± 0.2 \pm 0.2 PSNR. Tuning B B and V T V_{T} within the same effective batch size B eff B_{\text{eff}} does not result in significant difference in the final performance outcome, we exclude this degree of freedom from our subsequent analyses and treat B eff B_{\text{eff}} as the true batch size.

[46] h4: SVSM Enables Compute-Optimal Tradeoff.

[47] p: How can we interpret this result through the lens of compute-optimiality? For the LVSM decoder-only model, the training compute scales as

[48] table: χ ∝ (LVSM) B V T ( V C + 1 ) = B eff ( V C + 1 ) . \chi{}^{\text{(LVSM)}}\propto BV_{T}(V_{C}+1)=B_{\text{eff}}(V_{C}+1). (5)

[49] p: Thus, any training settings within constant B eff B_{\text{eff}} not only achieve within-noise results (as per our effective batch result), but also require the same number of FLOPs. This means for the decoder-only model there is no advantage to be gained by tuning V T V_{T} . In contrast, for the SVSM model, training compute is proportional to

[50] table: χ ∝ (SVSM) B ( V C + V T ) = B eff + B V C . \chi{}^{\text{(SVSM)}}\propto B(V_{C}+V_{T})=B_{\text{eff}}+BV_{C}. (6)

[51] p: Therefore, by reducing B B and increasing V T V_{T} , one can achieve the same effective batch size – and consequently, the same performance – with lower compute cost. This justifies our original motivation for a model design that efficiently decodes multiple V T V_{T} .

[52] figure: Table 1 : Stereo ( V C = 2 V_{C}=2 ) NVS Results of the Largest Models. All models use a patch size of 8 8 with input images at 256 × 256 256\times 256 resolution. Our models achieve the highest reconstruction metrics while using less than half of the training compute. The rendering FPS of both SVSM models is also much faster than that of the LVSM decoder-only model, though both are slower than the LVSM encoder-decoder when V C V_{C} is large. Scale Parameters Reconstruction Quality Rendering FPS (↑) Model Model Size Train Iters Train FLOPs (↓) PSNR (↑) SSIM (↑) LPIPS (↓) V C V_{C} =2 V C V_{C} =4 V C V_{C} =8 LVSM Encoder-Decoder [ 10 ] 173M 100k 2.53 zflops 28.58 0.893 0.114 53.7 52.9 52.7 LVSM Decoder-Only [ 10 ] 171M 100k 1.60 zflops 29.67 0.906 0.098 37.9 19.5 8.6 SVSM Enc-Dec ( ours , Iter-matched) 740M 100k 0.74 zflops 29.80 0.907 0.098 48.6 42.7 35.0 SVSM Enc-Dec ( ours , Pareto-optimal) 416M 170k 0.77 zflops 30.01 0.910 0.096 71.0 61.8 49.7

[53] h2: 5 Scaling Laws for Stereo ( 𝑽 𝑪 = 𝟐 ) \left(V_{C}{=}2\right) NVS

[54] p: Analysis Setup. We first experiment in the most classical setting for feed-forward Novel View Synthesis – stereo synthesis with two context views. All training and evaluation for the V C = 2 V_{C}=2 case is done on RealEstate10K [ 34 ] . As before, we follow the test-train split of pixelSplat [ 2 ] , along with the same evaluation framework. For training, we use V T = 6 V_{T}=6 target views per training example, following the setup of [ 10 ] . We use a batch size of 256 256 for all experiments. We use a patch size of p = 16 p=16 for all experiments, except in the case of table 2 , where we use p = 8 p=8 to compare against the reported state-of-the-art numbers from LVSM. To ensure stable scaling of both models, we also apply a 1 / L 1/\sqrt{L} multiplier to the residuals, where L L is the depth of the transformer, following ideas from depth- μ \mu P [ 28 , 1 ] . Further training details can be found in the supplementary material. We use the test LPIPS [ 32 ] loss as our primary performance metric, as it produces near linear trends on log-log plots against FLOPs.

[55] figure: Figure 4 : Data and Model Scaling Plots. While our model ( blue ) is optimal when sufficient data is available, decoder-only LVSM ( red ) performs better with less data. The Pareto frontier analysis shows that our model is more data-hungry. Our model is also less parameter-efficient, although the gap closes as we increase the training compute. However, with sufficient data and compute, our model ( blue ) is overall superior in terms of training compute-optimality and rendering speed.

[56] h4: Scaling Laws.

[57] p: We now follow the approach in language modeling [ 8 ] to answer the question: for a given compute-budget, what is the optimal performance that can be attained? For both model families, we sweep across a range of models from around 7M to 300M parameters, training each model for 3-4 different sample counts to densely cover the FLOP range [ 8 ] . Our training runs span a compute range of 10 3 10^{3} magnitudes: 100 petaflops to 100 exaflops. From this data, we are then able to determine a mapping from compute budgets C C to minimum test LPIPs – the Pareto frontier.

[58] p: We plot results in Fig. 1 , with their Pareto frontiers marked in dark gray. Plotted on a log-log scale, both models exhibit a consistent downward trend on test LPIPS with more compute. More significantly, the Pareto frontiers of both families have approximately the same slope at points of the same performance (see Supp 11 ), and SVSM’s frontier is shifted left by a factor of 3 3 . Thus, as an initial result, our scaling laws show us that our encoder-decoder architecture scales exactly the same as the decoder-only LVSM while using 3 × 3\times less training-compute. Qualitative results of this scaling are shown in Fig. 5 , and we see that when FLOP-matched, SVSM has better rendering quality.

[59] figure: Figure 5 : Qualitative Scaling Behavior , V C = 2 V_{C}=2 . From left to right, both models steadily increase in rendering quality until reaching near photo-realistic results. Compared vertically, for a given compute-budget, SVSM renderings consistently contain less artifacts.

[60] figure: Recon Quality Model PSNR (↑) SSIM (↑) LPIPS (↓) pixelNeRF [ 29 ] 20.43 0.589 0.550 pixelSplat [ 2 ] 26.09 0.863 0.136 MVSplat [ 3 ] 26.39 0.869 0.128 GS-LRM [ 31 ] 28.10 0.892 0.114 SVSM Enc-Dec (ours) 30.01 0.910 0.096 Table 2 : Comparison to Geometry-Aware Methods. Our method achieves a new state-of-the-art on RealEstate10K [ 34 ] with the set from Charatan et al. [2] , outperforming not only LVSM, but also prior work with explicit 3D structure.

[61] h4: Optimal Model Choice.

[62] figure: Model Parameter Coeff. a a Data Coeff. b b LVSM 0.65 0.33 SVSM 0.52 0.47 Table 3 : Parameter and Data Scaling Coefficients. As regressed from the plots in Fig. 4 , we find power law coefficients for scaling models and data with respect to compute.

[63] p: From our scaling experiments, we can further extract a compute-optimal training recipe for our view synthesis transformers, as demonstrated by Hoffmann et al. [8] . For each compute budget χ \chi{} , we determine the corresponding optimal model size N N and the amount of training data D D used at that point. Then, plotting N N and D D against χ \chi{} , we can extract the Chinchilla scaling equations (Eq. 3 ) by fitting lines onto the log-log plots in Fig. 4 . The recovered coefficients are shown in Tab. 3 , which inform how to train models which end on the frontier.

[64] p: From these results it follows that for SVSM, if we increase our compute budget by a factor of k × k\times , it should approximately be equally allocated between increasing the model size by k \sqrt{k} and increasing data sample count by k \sqrt{k} as a SVSM ≈ b SVSM a_{\text{SVSM}}\approx b_{\text{SVSM}} , matching the findings of the Chinchilla scaling laws [ 8 ] for language models. For LVSM this relationship does not seem to hold exactly, but the fit still shows that requires significant scaling of data with respect to compute, though to a smaller power.

[65] figure: Figure 6 : Multiview PRoPE. We find that multiview projective RoPE embeddings [ 18 , 13 , 14 ] are critical for our model to scale with compute and data in the multiview setting ( V C > 2 V_{C}>2 ). For each layer of the multiview transformer encoder, PRoPE embeddings use context camera poses to transform context view tokens into a common coordinate frames before the attention layer, and apply the inverse transformation before each MLP. To render, both context features and query tokens of the target view are transformed by PRoPE before cross-attention.

[66] figure: Figure 7 : Multiview Scaling Behavior. Conducted on DL3DV [ 15 ] . (a) For V C > 2 V_{C}{>}2 , without PRoPE, SVSM saturates and stops scaling much more quickly than LVSM. (b) When PRoPE is added, SVSM continues scaling with a better Pareto-frontier.

[67] p: Notably our data sample counts include repeated scene data , as we only have access to small, pose-labeled datasets. This differs from standard scaling practice, in which models are typically trained for less than one full epoch [ 8 , 11 , 30 ] . Although we have not yet seen evidence of overfitting in our experiments – perhaps due to the diversity of view sequences which are sampled during training – we have shown that increasing scale requires increasing the number data samples. Thus, having access to larger amounts of diverse posed data will be essential for developing large-scale generalizable NVS models.

[68] h4: SVSM-420M/740M Results.

[69] p: Finally, combining our scaling law findings, we train two separate models — SVSM-420M and SVSM-740M, aptly named to denote their parameter counts — to compare against the original results of LVSM’s largest model on RealEstate10K. Due to compute-constraints, we train our models at a lower total budget of around 10 21 10^{21} FLOPs and a batch size of 256 256 , approximately half the FLOPs and exactly half the batch size used by LVSM. We train two models under this budget: (1) a flop-matched model with the 24 layer LVSM model for a forward pass of a single training sample with V C = 2 , V T = 6 V_{C}=2,V_{T}=6 and; (2) A model whose parameter count is given by plugging the budget 1 1 1 To be more specific, we plug χ / 4 \chi/4 into the scaling law, in order to adjust for the scaling law being derived off of 16 × 16 16\times 16 patch experiments, while this final budget is under 8 × 8 8\times 8 patches, which requires roughly 4 × 4\times as much compute. χ \chi and the coefficients from Tab. 3 to Eq. 3 .

[70] p: While we train with under half the compute, our scaling laws in Sec. 5 predict equal performance with three times less compute. Thus, as predicted by our scaling laws and validated empirically by the results in 1 both SVSM models outperform decoder-only LVSM. Notably, SVSM-420M, the model trained in accordance with our scaling laws performs the best. For completeness, we also show reported results from prior work on this benchmark in Tab. 2 .

[71] p: Furthermore, we also benchmark the rendering speed , which is calculated with V T = 1 V_{T}=1 to simulate real-time online rendering with respect to a stream of input poses. Additional details can be found in Supp 10.2 . As seen in Tab. 1 , SVSM generally renders much faster than decoder-only LVSM, and is eclipsed only once V C V_{C} increases to 8 8 .

[72] h2: 6 Scaling Laws for Multiview ( 𝑽 𝑪 > 𝟐 ) \left(V_{C}{>}2\right) NVS

[73] h4: Analysis Setup.

[74] p: We continue to experiment in the multiview paradigm ( V C > 2 V_{C}{>}2 ), which necessitates the reconciliation of scene information across many views to produce quality renderings. Specifically, we focus on V C = 4 V_{C}=4 regime. For training and evaluation, we choose DL3DV [ 15 ] , a real-world dataset with wider baselines and more complex camera trajectories and subject matter, making it more suitable for multiview experiments. We follow the official test-train split and use V T = 4 V_{T}{=}4 , and scene batch size of 64 64 for all experiments to save resources. All other settings follow those described in Sec. 5 and Supp 10 .

[75] figure: Table 4 : Multiview ( V C > 2 V_{C}{>}2 ) NVS Results of the Largest Models. Our compute-matched model achieves significantly better rendering quality ( + 0.68 ​ PSNR +0.68\text{ PSNR} , − 0.016 ​ LPIPS -0.016\text{ LPIPS} ), while maintaining nearly four times the rendering speed at inference-time. Scale Parameters Reconstruction Quality Rendering FPS (↑) Model Model Size Train Iters Train FLOPs (↓) PSNR (↑) SSIM (↑) LPIPS (↓) V C V_{C} =4 V C V_{C} =8 V C V_{C} =16 LVSM Decoder-only + PRoPE [ 10 , 14 ] 171M 100k 43 eflops 26.19 0.830 0.145 104.7 52.6 23.8 SVSM Enc-Dec ( ours , ≈ \approx Iter-matched) 711M 100k 32 eflops 26.29 0.835 0.141 280.4 261.2 230.4 SVSM Enc-Dec ( ours , Pareto-optimal) 400M 233k 44 eflops 26.87 0.853 0.129 411.1 381.1 333

[76] figure: Figure 8 : Qualitative Scaling Behavior , V C = 4 V_{C}=4 . The performance of both LVSM and our method steadily increases with compute (left to right). Compared vertically, for a given compute budget SVSM renderings are consistently less blurry.

[77] h4: Scaling Law Does Not Hold.

[78] p: Unfortunately, we find that naively extending our SVSM architecture to the multiview scenario does not result in a similar scaling trend. As can be seen from Figure 7 a, the Pareto frontier of our unidirectional model saturates much quicker than bidirectional LVSM as we increase the train compute.

[79] h4: Relative Camera Attention Re-establishes Scaling Law.

[80] p: We hypothesize that this is not a fundamental problem of encoder-decoder paradigm, but a problem caused by the way our model utilizes the pose information. Specifically, we find that adding a form of relative camera attention [ 18 , 13 , 14 ] resolves this issue.

[81] p: Let g i g_{i} be the camera pose of the view that the i i -th token belongs to. Relative camera attention models leverage attention mechanisms that only depend on the relative camera poses g i ​ j = g i − 1 ​ g j g_{ij}{=}g_{i}^{-1}g_{j} . This is typically achieved by 1) mapping the query, key, and value vectors to an arbitrary global reference frame, 2) performing attention there, and then 3) mapping back the results to each token’s own reference frame. This mechanism embeds the pose information directly into the attention layers, ensuring that it isn’t lost after the initial embedding. This potentially explains the efficacy of the method for our model, which may lose the pose information through the bottleneck otherwise.

[82] p: For our model, we adopt the recently proposed PRoPE [ 14 ] embedding as the relative camera attention mechanism. We illustrate SVSM’s architecture with the incorporation of PRoPE embeddings in Fig. 6 . After adding PRoPE embeddings to both LVSM and SVSM, we retrain all models. Results are shown in Fig. 7 . The equivalent scaling is re-established, and SVSM again maintains a tighter Pareto-frontier. Qualitative scaling results for both models are shown in Fig. 8 . Note that while both models benefit from PRoPE embeddings, the advantage is far more pronounced in our encoder-decoder SVSM.

[83] h4: Final Models.

[84] p: Equipped with PRoPE embeddings, we again train larger models to compare directly against the 24-layer LVSM Decoder-only model, also equipped with PRoPE. As we did in the stereo case, we train a naive forward pass-matched model along with a Pareto-optimal model from a N ⁡ ( χ ) N(\chi{}) fit to the data. The performance of both models are listed in Tab. 4 and their test loss curves are plotted in Fig. 7 . Again, the version of SVSM which follows the scaling laws outperforms both models, with significant 0.7 0.7 PSNR and − 0.016 -0.016 LPIPS gaps. Beyond the superior reconstruction quality, the efficiency of SVSM becomes clear in the multi-view case, with a rendering FPS that is 4 × 4\times that of the decoder-only model, increasing to 14 × 14\times when extrapolated to larger context view counts.

[85] h2: 7 Scaling Laws for Fixed Latent Design

[86] figure: Figure 9 : Fixed-size Latent Scaling Experiments. Conducted on Objaverse [ 4 ] . (a) For V C = 8 V_{C}{=}8 , SVSM and LVSM decoder-only scale equally while SVSM’s frontier is shifted by 5 × 5\times on the compute axis. (b) When a fixed latent bottleneck is used, SVSM-fixed and LVSM encoder-decoder scale equally, but significantly worse than the unbottlenecked designs. SVSM again maintains a superior pareto frontier.

[87] h4: Analysis Setup.

[88] p: Lastly, we check both the scaling laws and the design space of view synthesis models with a fixed-size scene representation. This design has favorable rendering speeds for large context lengths, though it does not have favorable training compute as the encoder is still quadratic in the context length. For training and evaluation, we use Objaverse [ 4 ] , with 8 context views (where the benefit of having a fixed latent starts to appear at inference time). We compare two designs: LVSM Encoder-Decoder and SVSM-fixed, which follows the same design of a unidirectional decoder but instead decodes off of a fixed latent. Both models utilize PRoPE with identity pose on the scene representation. We use V T = 8 V_{T}=8 and scene batch size 64 64 for an effective batch size of 512 512 for all experiments. All other settings follow those described in Sec. 5 and Supp 10 .

[89] h4: SVSM-Fixed Matches LVSM Scaling, but Both Scale Poorly.

[90] p: As shown in Fig. 9 b, SVSM with a fixed latent and the LVSM encoder–decoder exhibit similar scaling behavior. However, SVSM-fixed consistently requires less compute to achieve the same performance, maintaining a Pareto advantage. This indicates that our unidirectional decoder remains more compute-efficient even when a fixed latent bottleneck is imposed, which is desirable when amortized rendering is required. Nevertheless, comparing to Fig. 9 a makes clear that both fixed-latent designs scale substantially worse than their bottleneck-free counterparts.

[91] h2: 8 Conclusion

[92] p: In this work, we established a rigorous compute-normalized benchmark for transformer view synthesis models. Our empirical studies reveal the importance of the concept of effective batch size —the product of the number of scenes in a batch with the number of per-scene rendering target views — which redefines the notion of batch size for NVS training. Based on this insight, we propose the Scalable View Synthesis Model (SVSM), which features a unidirectional encoder-decoder architecture for favorable scaling with effective batch. We demonstrate that SVSM is dramatically more compute-efficient than the current SOTA architecture, LVSM, and consistently achieves the same performance with 2 − 3 × 2-3\times less training compute. We further demonstrate that relative camera pose embeddings in multi-view attention is the key to realizing favorable scaling behavior with increasing numbers of context views. Lastly, we show that even with a fixed-size latent representation, our unidirectional decoder is still more compute-efficient than the LVSM encoder–decoder architecture; however, both approaches scale substantially worse than the designs without a latent bottleneck. In sum, our findings establish a new framework for evaluating the performance and effectiveness of transformer view synthesis models.

[93] h4: Acknowledgements.

[94] p: This work was supported by the National Science Foundation under Grant No. 2211259, by the Singapore DSTA under DST00OECI20300823 (New Representations for Vision, 3D Self-Supervised Learning for Label-Efficient Vision), by the Intelligence Advanced Research Projects Activity (IARPA) via Department of Interior/ Interior Business Center (DOI/IBC) under 140D0423C0075, by the Amazon Science Hub, by the MIT-Google Program for Computing Innovation, and by a 2025 MIT Office of Research Computing and Data Seed Grant.

[95] h2: References

[96] p: Supplementary Material

[97] h2: 9 FLOPs for View Synthesis Transformers

[98] p: In this section, we explain how we calculated FLOP consumption for all models. Additionally, we show that in our regime, the MLP cost is most significant. In a vision transformer, there are three contributions to the FLOPs:

[99] p: Initial patchifying + tokenization layers (negligible)

[100] p: Transformer blocks: attention.

[101] p: Transformer blocks: MLP and projections.

[102] p: The first is negligible as it is a single linear layer at the start. Letting n n be the number of tokens and d d the transformer dimension, for each self-attention transformer block, the following are the FLOPs consumed by the attention, projection, and MLP layers:

[103] table: χ 𝙼𝙻𝙿 , χ 𝙿𝚛𝚘𝚓 \displaystyle\chi_{\mathtt{MLP}},\chi_{\mathtt{Proj}} ∝ n ​ d 2 \displaystyle\propto nd^{2} (7) χ 𝙰𝚝𝚝𝚗 \displaystyle\chi_{\mathtt{Attn}} ∝ n 2 ​ d \displaystyle\propto n^{2}d (8)

[104] p: Thus, the total FLOPs consumed for a transformer block are of the form

[105] table: χ = A ​ n 2 ​ d + B ​ n ​ d 2 , \chi{}=An^{2}d+Bnd^{2}, (9)

[106] p: where A A is 4 4 while B B is 16 16 in the self-attention case, so even at the smallest model size list (Supp 10.3 ), B ​ n ​ d 2 A ​ n 2 ​ d ≈ 4 ⋅ 384 512 ≈ 3 \frac{Bnd^{2}}{An^{2}d}\approx 4\cdot\frac{384}{512}\approx 3 , meaning in most cases our MLP / linear projection FLOPs take up a large majority. For SVSM’s cross-attention decoder, the formula becomes a little more complicated as there are separate n ctxt n_{\text{ctxt}} and n target n_{\text{target}} , but these remain on the same order of magnitude as n n , so the same is true.

[107] p: For the decoder-only model, the number of tokens n n is given by

[108] table: n = ( V C + 1 ) ⋅ H p ⋅ W p , n=(V_{C}+1)\cdot\frac{H}{p}\cdot\frac{W}{p}, (10)

[109] p: where p p is the patch size and H H and W W are the width and height. For the SVSM encoder-decoder, the number of active tokens vary as

[110] table: n enc = V C ⋅ H p ​ W p , n dec = V T ⋅ H p ⋅ W p , n_{\text{enc}}=V_{C}\cdot\frac{H}{p}\frac{W}{p},n_{\text{dec}}=V_{T}\cdot\frac{H}{p}\cdot\frac{W}{p}, (11)

[111] p: So, for both models we can write down the MLP and attention complexities as:

[112] table: χ 𝙼𝙻𝙿 ( LVSM ) \displaystyle\chi_{\mathtt{MLP}}^{(\text{LVSM})} ∝ V T ​ n ∝ V T ​ ( V C + 1 ) \displaystyle\propto V_{T}n\propto V_{T}(V_{C}+1) (12) χ 𝙼𝙻𝙿 ( SVSM ) \displaystyle\chi_{\mathtt{MLP}}^{(\text{SVSM})} ∝ n enc + n dec ∝ V C + V T \displaystyle\propto n_{\text{enc}}+n_{\text{dec}}\propto V_{C}+V_{T} (13) χ 𝙰𝚝𝚝𝚗 ( LVSM ) \displaystyle\chi_{\mathtt{Attn}}^{(\text{LVSM})} ∝ V T ​ n 2 ∝ V T ​ ( V C + 1 ) 2 \displaystyle\propto V_{T}n^{2}\propto V_{T}(V_{C}+1)^{2} (14) χ 𝙰𝚝𝚝𝚗 ( SVSM ) \displaystyle\chi_{\mathtt{Attn}}^{(\text{SVSM})} ∝ n enc 2 + n enc ​ n dec ∝ V C 2 + V C ​ V T \displaystyle\propto n_{\text{enc}}^{2}+n_{\text{enc}}n_{\text{dec}}\propto V_{C}^{2}+V_{C}V_{T} (15)

[113] p: For fixed V C V_{C} , we see that multiplying V T V_{T} by an amount k k scales compute by exactly k × k\times in LVSM, while it only scales compute by k ​ V T + V C V T + V C \frac{kV_{T}+V_{C}}{V_{T}+V_{C}} in the SVSM case, which is where its advantage lies.

[114] figure: Encoder Decoder Params dim dim_head n_layers dim dim_head n_layers 15M 384 64 3 384 64 3 27M 384 64 6 384 64 6 35M 384 64 8 384 64 8 62M 512 64 8 384 64 8 79M 512 64 8 512 64 12 145M 640 64 10 640 64 14 226M 768 64 10 768 64 16 316M 768 64 12 768 64 24 420M 768 64 16 768 64 32 740M 1024 64 16 1024 64 32 Table 5 : RealEstate10K V C = 𝟐 \boldsymbol{V_{C}}\mathbf{{=}2} , SVSM Encoder-Decoder. SVSM Encoder-Decoder model settings used to sweep scaling laws for the stereo ( V C = 2 V_{C}{=}2 ) novel view synthesis setting. Bolded is the row for the compute-matched, Pareto-optimal SVSM model compared against the 24-layer LVSM Decoder-only model.

[115] figure: Encoder Decoder Params dim dim_head n_layers dim dim_head n_layers 8M - - - 384 64 3 13M - - - 384 64 6 22M - - - 512 64 6 28M - - - 512 64 8 53M - - - 640 64 10 90M - - - 768 64 12 118M - - - 768 64 16 175M - - - 768 64 24 275M - - - 896 64 28 Table 6 : RealEstate10K V C = 𝟐 \boldsymbol{V_{C}}\mathbf{{=}2} , LVSM Decoder-only. LVSM Decoder-only model settings used to sweep scaling laws for the stereo ( V C = 2 V_{C}{=}2 ) novel view synthesis setting.

[116] h2: 10 Further Experimental Details

[117] h3: 10.1 Training Details

[118] p: All models in this study are multi-view ViTs, following the design of LVSM [ 10 ] . The main deviation is no layer index-dependent initialization. All layers are initialized with the same standard deviation. Instead, for stability, we apply a 1 / L 1/\sqrt{L} multiplier on the residuals of all layers where L L is the depth of the transformer. Empirically, we find this to maintain stable training on the same learning rate across multiple transformer depths.

[119] p: All models are trained with the AdamW optimizer, with a peak learning rate of 4 ​ e- ​ 4 4\text{e-}4 , β 1 = 0.9 \beta_{1}=0.9 , β 2 = 0.95 \beta_{2}=0.95 , and weight decay of 0.05 0.05 on all parameters except LayerNorm weights, all following LVSM. We additionally warmup the learning rate for 3000 3000 steps in all models.

[120] p: All models are trained on 256 × 256 256\times 256 resolution for both DL3DV and RealEstate10K. All models are trained with the same reconstruction metric used in [ 10 ] . In particular, the loss is

[121] table: ℒ = MSE ​ ( I T , I ~ T ) + λ ⋅ Perceptual ​ ( I T , I ~ T ) , \mathcal{L}=\text{MSE}(I_{T},\tilde{I}_{T})+\lambda\cdot\text{Perceptual}(I_{T},\tilde{I}_{T}), (16)

[122] p: where we choose λ = 0.5 \lambda=0.5 as our perceptual loss weight.

[123] p: We also have a few experiment specific details. For V C = 2 V_{C}{=}2 , RealEstate10K, we sample our context and target views from a video index range from 25-192. For V C > 2 V_{C}{>}2 , DL3DV, we sample our context and target views from a video index range of 16-24 as the baselines between consecutive frames in DL3DV are much wider. For effective batch tests under V C = 4 V_{C}{=}4 on DL3DV, we train each model for 100k iterations, while under V C = 2 V_{C}{=}2 on RealEstate10K, we train for less iterations (50k) to save compute resources. The trend is still clear even with the limited iterations.

[124] figure: Encoder Decoder Params dim dim_head n_layers dim dim_head n_layers 15M 384 64 3 384 64 3 32M 384 64 6 384 64 8 85M 512 64 10 512 64 12 168M 640 64 12 640 64 16 280M 768 64 12 768 64 20 711M 1024 64 24 1024 64 24 400M 768 64 24 768 64 24 Table 7 : DL3DV V C = 𝟒 \boldsymbol{V_{C}}\mathbf{{=}4} , SVSM Encoder-Decoder. SVSM Encoder-Decoder model settings used to sweep scaling laws for the multi-view ( V C > 2 V_{C}>2 ) novel view synthesis setting. Bolded is the row for the compute-matched, Pareto-optimal SVSM model compared against the 24-layer LVSM Decoder-only model.

[125] figure: Encoder Decoder Params dim dim_head n_layers dim dim_head n_layers 8M - - - 384 64 3 22M - - - 512 64 6 43M - - - 640 64 10 90M - - - 768 64 12 175M - - - 768 64 24 383M - - - 1024 64 30 Table 8 : DL3DV V C = 𝟒 \boldsymbol{V_{C}}\mathbf{{=}4} , LVSM Decoder-only. LVSM Decoder-only model settings used to sweep scaling laws for the multi-view ( V C > 2 V_{C}>2 ) novel view synthesis setting.

[126] figure: Figure 10 : Linear Power Scaling Laws. We fit scaling laws onto sections of the Pareto-frontiers of the model families. We see that both models have approximately the same slope in each of their corresponding sections, indicating equal scaling.

[127] h3: 10.2 Rendering Speed Benchmarking

[128] p: We benchmark all rendering on a single A6000 GPU. We found that due to some hardware configurations of our setup, when benchmarking with batch size 1 1 , all models would cap out at 30 fps, even when the width of each layer was increased or decreased, suggesting that there was some non-FLOP based bottleneck. To circumvent this, all models were tested with batch size 64 64 , which allowed the rendering FPS to properly reflect the forward pass FLOPs for each of the models. We still used V T = 1 V_{T}=1 for all models, and report

[129] table: FPS = B ⋅ V T t iter = B t iter , \text{FPS}=\frac{B\cdot V_{T}}{t_{\text{iter}}}=\frac{B}{t_{\text{iter}}}, (17)

[130] p: where t iter t_{\text{iter}} is the iteration time for one batch. If higher V T V_{T} was used (offline rendering), the rendering speed difference between our model and LVSM would be even larger.

[131] h3: 10.3 Model Size List for Scaling Sweeps

[132] p: We trained a wide range of models across both families and both problem settings. Their sizes and hyperparameters are listed in tables 5 , 6 , 7 , and 8 . For the decoder-only model there is not much room for flexibility in terms of model hyperparameters – we simply scale dimension up along with the layer count. For SVSM encoder-decoder we can flexibly allocate different amounts of compute to the encoder and the decoder. For low context view cases, we allocate more to the decoder as there are less complex relations amongst the context views and for higher context views we allocate similar amounts to the decoder as to the encoder. Empirically, we roughly found this to have better performance-per-compute, but we did not thoroughly study this split, so we leave this to future work.

[133] h2: 11 Linear Fits on the Loss vs. Compute Frontiers

[134] p: Though the trend is not perfectly linear, we fit lines onto sections of P ( χ ) ∝ χ c P(\chi{})\propto\chi{}^{c} in Fig. 10 , which show equal scaling between SVSM and LVSM. The actual coefficients are reported in Tab. 9 , which have almost identical power law coefficients across the two model families.

[135] figure: Model c c for P > 0.14 P>0.14 c c for P ≤ 0.14 P\leq 0.14 LVSM -0.23 -0.12 SVSM -0.22 -0.12 Table 9 : LPIPS vs. compute scaling coefficients. As regressed from Fig. 10 , we find power law coefficients for LPIPS P ( χ ) ∝ χ c P(\chi{})\propto\chi{}^{c} , and we report c c in this table for the first half, which is determined by test LPIPS loss greater than 0.14 0.14 and the second half which is test LPIPS loss less than 0.14 0.14 .

[136] h2: 12 PRoPE Ablations

[137] p: We conduct a series of ablations on PRoPE [ 14 ] in the multi-view setting in an attempt to elucidate the mechanism through which it enables scaling. One potential source of success is that the PRoPE SVSM design allows for the decoder to see the clean context poses, while vanilla SVSM does not. To test if this might be the cause for the success, we concatenated context plucker rays to the scene representation from the encoder. However, this has negligible impact (Tab. 10 ). Additionally, replacing PRoPE with GTA [ 18 ] showed negligible difference, indicating epipolar geometry is not crucial for viewcount scalability. Hence, we presume that the relative embeddings are the key, i.e., canonicalizing features to the target frame. Lastly, having PRoPE on just the decoder performs nearly as well as having PRoPE on both, indicating that the cross attention seems to benefit the most from the relative embedding inductive bias.

[138] figure: Model PSNR (↑) SSIM (↑) LPIPS (↓) Vanilla SVSM 23.50 0.727 0.254 Vanilla w/ concat. pose 23.47 0.726 0.254 PRoPE on Encoder 23.61 0.733 0.249 PRoPE on Decoder 24.31 0.771 0.220 PRoPE on both 24.62 0.782 0.210 GTA on both 24.63 0.782 0.207 Table 10 : PRoPE ablations. We vary where we apply PRoPE, try a different relative attention method (GTA), and also test pose information flow. GTA varies negligibly from PRoPE, indicating that epipolar geometry is not crucial, and the skip pose connection also has negligible impact, indicating that pose information flow is not responsible.

[139] h2: 13 Compiled Scaling Results

[140] figure: Figure 11 : All Scaling Laws. We collect scaling laws across the three datasets we tested on, and in all cases, SVSM is compute-optimal.

[141] p: We provide a collection of scaling results across RealEstate10K, DL3DV, and Objaverse across 2, 4, and 8 context views respectively in Fig. 11 . In all cases, SVSM (in blue) maintains a pareto advantage over LVSM decoder-only.

[142] h2: 14 Further Qualitative Results

[143] p: Lastly, we provide more qualitative results across various training compute budgets of 2 context view evaluations on RealEstate10K in Fig. 12 and 4 context view evaluations on DL3DV in Fig. 13 . Multiview consistency of outputs is shown in Fig. 14 on Objaverse.

[144] figure: Figure 12 : Qualitative results on RE10K ( V C = 2 V_{C}{=}2 ) across scale.

[145] figure: Figure 13 : Qualitative results on DL3DV ( V C = 4 V_{C}{=}4 ) across scale.

[146] figure: Figure 14 : Multiview consistency results on Objaverse ( V C = 8 V_{C}{=}8 ).

[147] h2: Instructions for reporting errors

[148] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[149] p: Tip: You can select the relevant text first, to include it in your report.

[150] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[151] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
