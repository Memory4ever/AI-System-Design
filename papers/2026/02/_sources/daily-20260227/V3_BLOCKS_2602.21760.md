[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Accelerating Diffusion via Hybrid Data-Pipeline Parallelism Based on Conditional Guidance Scheduling

[3] h6: Abstract

[4] p: Diffusion models have achieved remarkable progress in high-fidelity image, video, and audio generation, yet inference remains computationally expensive. Nevertheless, current diffusion acceleration methods based on distributed parallelism suffer from noticeable generation artifacts and fail to achieve substantial acceleration proportional to the number of GPUs. Therefore, we propose a hybrid parallelism framework that combines a novel data parallel strategy, condition-based partitioning, with an optimal pipeline scheduling method, adaptive parallelism switching, to reduce generation latency and achieve high generation quality in conditional diffusion models. The key ideas are to (i) leverage the conditional and unconditional denoising paths as a new data-partitioning perspective and (ii) adaptively enable optimal pipeline parallelism according to the denoising discrepancy between these two paths. Our framework achieves 2.31 × 2.31\times and 2.07 × 2.07\times latency reductions on SDXL and SD3, respectively, using two NVIDIA RTX 3090 GPUs, while preserving image quality. This result confirms the generality of our approach across U-Net-based diffusion models and DiT-based flow-matching architectures. Our approach also outperforms existing methods in acceleration under high-resolution synthesis settings. Code is available at https://github.com/kaist-dmlab/Hybridiff.

[5] figure: Figure 1 : Summary of the proposed hybrid data-pipeline parallelism. Our method consistently outperforms prior distributed approaches across five key aspects: Speed-up , Image Quality , Generality , High-resolution Synthesis , and Communication Cost , demonstrating robust and balanced acceleration-quality trade-offs.

[6] h2: 1 Introduction

[7] figure: Figure 2 : Comparison of parallel strategies for diffusion inference. (a) Patch-based data parallel frameworks suffer from bottlenecks caused by all-gather operations and artifacts at patch boundaries, leading to limited acceleration and quality degradation. (b) Pipeline parallel frameworks incur excessive asynchronous communication overhead and accumulate estimate errors. (c) Our hybrid parallelism , which incorporates condition-based data parallelism, adaptively combines both paradigms to achieve high fidelity and fast generation.

[8] p: Diffusion models have emerged as a powerful family of generative models because of their superior sample quality and broad applicability. However, the inherently iterative nature of diffusion processes, which consists of many denoising steps, leads to significant inference latency and computational bottlenecks. As model sizes continue to scale, these inefficiencies become increasingly limiting, making diffusion inference acceleration a pressing research challenge. Existing approaches have focused mainly on reducing the number of sampling steps [ 9 , 19 , 20 , 26 , 27 , 36 , 34 , 37 , 21 ] , designing optimal architectures [ 12 , 13 , 39 , 14 , 38 , 35 ] , or leveraging mathematical approximations [ 1 , 18 , 40 , 40 , 22 , 17 , 28 ] . Yet, these methods often require additional training or fail to deliver strong acceleration in practice, exhibiting a clear trade-off between generation quality and speed.

[9] p: Distributed parallelism across multiple GPUs offers a promising alternative. Using modern parallel computing resources, one can achieve substantial throughput improvements in diffusion inference without additional training. This direction is especially appealing given the success of distributed strategies in natural language processing, where large-scale language models have already benefited from extensive parallelism research [ 24 , 29 ] . As in other domains, distributed parallelism for generative model inference can be broadly classified into data parallelism and pipeline parallelism [ 11 , 2 ] . Both approaches enhance throughput by distributing either the input data or the model itself across multiple GPUs.

[10] p: Representative existing studies include DistriFusion [ 11 ] for data parallelism and AsyncDiff [ 2 ] for pipeline parallelism. In DistriFusion (Figure 2 a), an input image is divided into N N disjoint patches, and these patches are processed in parallel across N N GPUs, where each device independently handles one patch. In AsyncDiff (Figure 2 b), the entire model is divided into N N sequential components, where each component is assigned to a GPU, and the output from the i i -th GPU is asynchronously fed as the input to the ( i + 1 ) (i+1) -th GPU; thus, AsyncDiff enables pipelined execution across devices.

[11] p: In theory, each form of parallelism can improve throughput linearly with respect to the number of GPUs, up to an ideal N × N\times speed-up, but in practice, the gains are often sublinear due to communication overhead and synchronization costs. In this paper, we propose a hybrid strategy that combines data and model parallelism to further increase the throughput of generative model inference, achieving beyond-linear scaling relative to the number of GPUs, while maintaining generation quality. That is, if there are two GPUs, we aim to obtain more than a twofold speed-up without noticeable degradation in output fidelity. In practice, when using two GPUs, data and model parallelism achieved 1.2 × \times and 1.3 × \times speed-up, respectively, whereas our hybrid approach remarkably achieved a 2.3 × \times speed-up under the same configuration, as shown in Figures 1 and 2 .

[12] p: To achieve hybrid parallelism, one could combine the aforementioned representative methods. Specifically, an image is divided into disjoint patches, and each patch is fed into a corresponding model component (not necessarily the first one). As a result, each GPU trains a 1 / N 1/N portion of the model using a 1 / N 1/N portion of an input image. This hybrid approach can potentially achieve beyond-linear scaling; however, it may degrade generation quality for two main reasons. First, since each GPU processes only a portion of the image, artifacts are likely to appear particularly along patch boundaries. Second, this issue is exacerbated by asynchronous communication between model components; that is, errors introduced by asynchronous rather than sequential denoising can worsen the artifacts.

[13] p: In this paper, we aim to propose and further optimize the hybrid parallelism for diffusion inference from two complementary perspectives: (1) from the data parallelism perspective, transitioning from patch-based partitioning to condition-based partitioning ; and (2) from the model parallelism perspective, advancing from static parallelism switching to adaptive parallelism switching .

[14] p: (1) Condition-Based Partitioning. The main limitation of patch-based partitioning is that each patch represents only a local subregion of an image, often leading to boundary artifacts and degraded visual coherence. To address this limitation, we leverage the classifier-free guidance (CFG) [ 7 ] , a technique widely adopted in diffusion models, where the model simultaneously predicts conditional (prompted) and unconditional (unprompted) noise estimates. This dual-path prediction naturally provides a meaningful criterion for data partitioning: as shown in Figure 2 c, the conditioned ( x t , c \textbf{x}_{t},c ) and unconditioned ( x t \textbf{x}_{t} ) inputs form two distinct data-parallel paths. Importantly, unlike patch-based partitioning, each image partition covers the entire image, thereby preserving global consistency. Consequently, condition-based partitioning yields improved visual coherence and reduced communication overhead during feature aggregation.

[15] p: (2) Adaptive Parallelism Switching. Because we revise the data partitioning strategy, the pipeline parallelism must also be adapted to align with it. In the early denoising steps, the conditional and unconditional noise estimates differ substantially due to the presence or absence of the condition. Consequently, asynchronous denoising at this stage can lead to divergence between the two paths. To mitigate this issue, we defer the onset of parallel execution until the noise estimates of the two paths become sufficiently similar, beyond the conventional warm-up phase used in prior works (e.g., [ 2 ] ). Similarly, toward the final denoising steps, the noise estimates from the two paths begin to diverge again; at this point, parallel execution is terminated. The specific switching points between serial and parallel execution are determined automatically based on a novel metric, called the denoising discrepancy , which quantifies the difference between the two noise estimates. This adaptive switching mechanism effectively improves generation quality by reducing error propagation, while only marginally shortening the duration of parallel processing.

[16] p: This novel framework demonstrates consistent acceleration not only on conventional denoising diffusion models but also on recent state-of-the-art generative frameworks such as flow matching [ 16 ] . As long as the model follows a sequential denoising process that allows quantifying the relative influence between conditional and unconditional branches, our framework remains robust and effective. Furthermore, due to the nature of pipeline parallelism, it is not restricted to specific architectures such as U-Net or DiT, showing strong generality across diverse networks.

[17] p: As summarized in Figure 1 , our proposed hybrid parallelism achieves superior performance across the five key aspects. In fact, compared to single-GPU inference, our method achieves a 2.3 × \times speed-up with two GPUs (i.e., > 2 >2 ), while preserving generation fidelity. See Appendix A and Section 5 for details of Figure 1 . Finally, the key contributions are summarized as follows.

[18] p: Hybrid Parallelism Framework for Diffusion Inference. We introduce a novel diffusion inference parallelism framework that integrates condition-based partitioning and adaptive parallelism switching into a unified hybrid parallelism design.

[19] p: Novel Condition-Based Partitioning. At the data parallelism level, we exploit the intrinsic mechanism of diffusion by decoupling conditional and unconditional branches and performing multi-GPU denoising.

[20] p: Adaptive Parallelism Switching. To align pipeline parallelism with the behavior of conditional guidance, our method adaptively switches to hybrid parallelism framework during inference. Switching points are automatically determined based on the denoising discrepancy between conditional and unconditional estimates, ensuring generation efficiency throughout the denoising process.

[21] p: Robustness across Models and Architectures. Our framework consistently demonstrates strong acceleration and generation quality across various architectures (e.g., U-Net, DiT) and recent state-of-the-art generative frameworks, such as flow matching, even under high-resolution synthesis settings.

[22] figure: Figure 3 : Overview of the proposed diffusion inference hybrid parallel framework. Our method adaptively switches parallelism modes at τ 1 \tau_{1} and τ 2 \tau_{2} , optimizing the trade-off between computational efficiency and consistency of conditional guidance, and demonstrates superior inference acceleration performance while preserving high generation quality.

[23] h2: 2 Related Work

[24] p: Single -GPU Diffusion Acceleration. Research on the acceleration of single -device diffusion inference can be classified into three categories. The first group focuses on reducing the number of sampling steps required for high-quality generation [ 30 , 9 , 19 , 20 , 26 , 27 , 36 , 34 , 40 , 37 , 21 ] . These approaches enable fast sampling by either reformulating the reverse process as an ordinary differential equation (ODE), distilling multi-step models into fewer steps, or directly predicting the reverse process in latent space. The second group targets model architecture optimization, aiming to reduce computational cost through network compression and efficient design [ 12 , 13 , 39 , 14 , 38 , 35 ] . The third group leverages mathematical and algorithmic strategies, either exploiting the mathematical structure of diffusion processes or reusing intermediate computations to further accelerate inference [ 1 , 18 , 40 , 22 , 33 , 17 , 28 ] . While these methods reduce single-device inference time, they are inherently limited by the computational capacity of individual GPUs.

[25] p: Multi -GPU Diffusion Acceleration. Recent studies have explored various distributed parallelism strategies to accelerate diffusion inference using multiple GPUs [ 11 , 2 , 5 , 4 , 32 ] . DistriFusion [ 11 ] introduces a data-parallel approach that divides the input image into independent patches, performing denoising in parallel across GPUs. This work has established a foundational paradigm for parallel diffusion inference. Building on this parallelization idea, AsyncDiff, [ 2 ] introduces model parallelism by dividing the U-Net into layer-wise segments and employing a stride-based scheduling strategy to balance parallel execution, achieving a notable reduction in latency.

[26] p: Subsequently, PipeFusion [ 5 ] and XDiT [ 4 ] combine patch-level parallelism with transformer-oriented parallelism through ring attention. While additional adaptations such as CFG-based data parallelism have been introduced, these methods remain limited to inter-image processing and lack deeper architectural integration. Moreover, transformer-specific schemes such as ring attention exhibit limited scalability and inconsistent performance when applied to general diffusion architectures. More recently, ParaStep [ 32 ] proposes a reuse-then-predict mechanism that leverages the similarity of noise predictions between adjacent denoising steps. By reusing the noise from previous steps before re-prediction, ParaStep enables inter-step parallelization and significantly reduces communication overhead. However, because early and late diffusion steps exhibit larger discrepancies between adjacent noise states, the reuse mechanism can accumulate errors, leading to potential degradation in image quality or restricted speedup.

[27] h2: 3 Preliminaries

[28] p: Denoising Diffusion Model. Let q ⁡ ( 𝐱 0 ) q(\mathbf{x}_{0}) denote the data distribution and define a forward noising process by

[29] table: q ⁡ ( 𝐱 t ∣ 𝐱 t − 1 ) = 𝒩 ⁡ ( 𝐱 t , 1 − β t ​ 𝐱 t − 1 , β t ​ 𝐈 ) , q(\mathbf{x}_{t}\mid\mathbf{x}_{t-1})=\mathcal{N}\bigl(\mathbf{x}_{t};\sqrt{1-\beta_{t}}\,\mathbf{x}_{t-1},\beta_{t}\mathbf{I}\bigr),

[30] p: for t = 1 , … , T t=1,\dots,T , with variance schedule { β t } \{\beta_{t}\} . The model learns a parameterized reverse denoising process,

[31] table: p θ ​ ( 𝐱 t − 1 ∣ 𝐱 t ) = 𝒩 ⁡ ( 𝐱 t − 1 , μ θ ​ ( 𝐱 t , t ) , Σ θ ​ ( t ) ) , p_{\theta}(\mathbf{x}_{t-1}\mid\mathbf{x}_{t})=\mathcal{N}\bigl(\mathbf{x}_{t-1};\mu_{\theta}(\mathbf{x}_{t},t),\Sigma_{\theta}(t)\bigr),

[32] p: by optimizing the variational lower bound,

[33] table: ℒ VLB = 𝔼 q [ ∑ t = 1 T D KL ( q ( 𝐱 t − 1 ∣ 𝐱 t , 𝐱 0 ) ∥ p θ ( 𝐱 t − 1 ∣ 𝐱 t ) ) ] . \mathcal{L}_{\mathrm{VLB}}=\mathbb{E}_{q}\Bigl[\sum_{t=1}^{T}D_{\mathrm{KL}}\bigl(q(\mathbf{x}_{t-1}\mid\mathbf{x}_{t},\mathbf{x}_{0})\,\|\,p_{\theta}(\mathbf{x}_{t-1}\mid\mathbf{x}_{t})\bigr)\Bigr].

[34] p: Classifier-Free Guidance (CFG). For conditional generation with a condition c c , the model is trained to predict the noise ϵ θ ​ ( 𝐱 t , t , c ) \epsilon_{\theta}(\mathbf{x}_{t},t,c) and its unconditional variant ϵ θ ​ ( 𝐱 t , t , ∅ ) \epsilon_{\theta}(\mathbf{x}_{t},t,\varnothing) . At inference, the samples follow

[35] table: ϵ cfg = ϵ θ ​ ( 𝐱 t , c , t ) + w ⁡ ( ϵ θ ​ ( 𝐱 t , c , t ) − ϵ θ ​ ( 𝐱 t , t ) ) , \epsilon_{\mathrm{cfg}}=\epsilon_{\theta}(\mathbf{x}_{t},c,t)+w\bigl(\epsilon_{\theta}(\mathbf{x}_{t},c,t)-\epsilon_{\theta}(\mathbf{x}_{t},t)\bigr),

[36] p: where w > 0 w>0 is the guidance scale. The adjusted reverse mean becomes

[37] table: μ cfg ​ ( 𝐱 t , t , y ) = 1 α t ​ ( 𝐱 t − β t 1 − α ¯ t ​ ϵ cfg ) . \mu_{\mathrm{cfg}}(\mathbf{x}_{t},t,y)=\frac{1}{\sqrt{\alpha_{t}}}\Bigl(\mathbf{x}_{t}-\frac{\beta_{t}}{\sqrt{1-\bar{\alpha}_{t}}}\,\epsilon_{\mathrm{cfg}}\Bigr).

[38] p: Flow Matching. Given a target distribution q ⁡ ( 𝐱 ) q(\mathbf{x}) and base distribution p 0 ​ ( 𝐱 ) p_{0}(\mathbf{x}) , flow matching defines an ordinary differential equation,

[39] table: d ​ 𝐱 ​ ( t ) d ​ t = v ⁡ ( 𝐱 ⁡ ( t ) , t ) , \frac{d\mathbf{x}(t)}{dt}=v(\mathbf{x}(t),t),

[40] p: where the vector field v θ v_{\theta} is learned by minimizing

[41] table: ℒ FM = 𝔼 t , 𝐱 0 ∼ q ​ ‖ v θ ​ ( 𝐱 t , t ) − 𝐱 t − 𝐱 0 t ‖ 2 , \mathcal{L}_{\mathrm{FM}}=\mathbb{E}_{t,\mathbf{x}_{0}\sim q}\Bigl\|v_{\theta}\bigl(\mathbf{x}_{t},t\bigr)-\frac{\mathbf{x}_{t}-\mathbf{x}_{0}}{t}\Bigr\|^{2},

[42] p: with 𝐱 t = 𝐱 0 + t ​ 𝐞 \mathbf{x}_{t}=\mathbf{x}_{0}+t\mathbf{e} for 𝐞 ∼ 𝒩 ⁡ ( 0 , 𝐈 ) \mathbf{e}\sim\mathcal{N}(0,\mathbf{I}) . Sampling proceeds by integrating 𝐱 ˙ = v θ ​ ( 𝐱 , t ) \dot{\mathbf{x}}=v_{\theta}(\mathbf{x},t) from t = 1 t=1 to t = 0 t=0 .

[43] h2: 4 Method

[44] h3: 4.1 Overview

[45] p: Figure 3 illustrates the overall process of our proposed hybrid parallelism framework. The input isotropic noise latent x T \textbf{x}_{T} is fed simultaneously into two denoising branches: the unconditional path f θ ​ ( x t , t ) f_{\theta}(\textbf{x}_{t},t) and the conditional path f θ ​ ( x t , c , t ) f_{\theta}(\textbf{x}_{t},c,t) guided by a textual prompt c c . where f θ f_{\theta} denotes the denoising diffusion network parameterized by θ \theta (e.g. U-Net, DiT). To exploit both global consistency and conditional fidelity, our framework incorporates two complementary dimensions of parallelism, condition-based partitioning , and adaptive parallelism switching .

[46] p: Formally, given the denoising model f θ f_{\theta} , the diffusion inference across N N devices can be expressed as

[47] table: 𝐱 t − 1 ( n ) = f θ ( n ) ​ ( 𝐱 t ( n ) , c ( b n ) , t ) , n ∈ { 1 , … , N } , b n ∈ { cond , uncond } , \begin{gathered}\mathbf{x}_{t-1}^{(n)}=f_{\theta^{(n)}}(\mathbf{x}_{t}^{(n)},c^{(b_{n})},t),\\[-3.0pt] n\in\{1,\dots,N\},\quad b_{n}\in\{\text{cond},\text{uncond}\},\end{gathered}

[48] p: where each θ ( n ) \theta^{(n)} corresponds to the subset of model parameters assigned to the n n -th device in the pipeline, reflecting adaptive parallelism switching across different network stages. Meanwhile, b n ∈ { cond , uncond } b_{n}\in\{\text{cond},\text{uncond}\} indicates whether the device n n handles the conditional or unconditional branch in condition-based partitioning. Accordingly, each device processes either a conditional input with c c or an unconditional input without c c . This formulation jointly represents both condition-based partitioning and adaptive parallelism switching within a unified diffusion framework.

[49] p: To further enhance performance, the denoising process is divided into three stages according to the temporal dynamics of conditional influence: (1) Warm-Up Stage , where only ordinal communication occurs between conditional and unconditional branches; (2) Parallelism Stage , where both branches are executed in parallel with conditional exchange; and (3) Fully-Connecting Stage , which merges the two branches for the final refinement. The rationale for this three-phase division and the quantitative criteria for determining the boundary points τ 1 \tau_{1} and τ 2 \tau_{2} are discussed in Section 4.2 and Section 4.3 , respectively.

[50] figure: Figure 4 : Illustration of the rel-MAE t ​ ( ϵ c , ϵ u ) \boldsymbol{\text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u})} curve. The rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) value is relatively large before τ 1 \tau_{1} and after τ 2 \tau_{2} , while it converges near zero between them, indicating stable alignment between conditional and unconditional branches during the parallelism phase.

[51] h3: 4.2 Hybrid Parallel Inference Framework

[52] p: Figure 4 illustrates the rel ative- M ean A bsolute E rror of the predicted noise (relative-MAE; rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) ) across the three stages of the proposed hybrid parallelism in the denoising diffusion model. To determine when the conditional and unconditional branches should interact or remain independent, we first quantify their denoising discrepancy during the denoising process.

[53] p: Since conditional and unconditional denoisers contribute differently to generation, with one emphasizing semantic alignment to the text condition and the other stabilizing global structure, it is essential to measure how their noises ϵ c \epsilon_{c} and ϵ u \epsilon_{u} diverge over time. This discrepancy serves as a key indicator for determining the switching points between serial and parallel execution within our hybrid framework.

[54] p: The denoising discrepancy , namely rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) , quantifies the difference in noise prediction ϵ t \epsilon_{t} between the conditional and unconditional branches at each timestep t t , (where ϵ c = ϵ θ ​ ( x t , c , t ) \epsilon_{c}=\epsilon_{\theta}(\textbf{x}_{t},c,t) and ϵ u = ϵ θ ​ ( x t , t ) \epsilon_{u}=\epsilon_{\theta}(\textbf{x}_{t},t) ), and is formulated as

[55] table: rel-MAE t ​ ( ϵ c , ϵ u ) = 𝔼 x , ϵ ​ [ ‖ ϵ θ ​ ( x t , c , t ) − ϵ θ ​ ( x t , t ) ‖ 1 ] 𝔼 x , ϵ ​ [ ‖ ϵ θ ​ ( x t , t ) ‖ 1 ] . \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u})=\frac{\mathbb{E}_{\textbf{x},\epsilon}\!\left[\left\lVert\epsilon_{\theta}(\textbf{x}_{t},c,t)-\epsilon_{\theta}(\textbf{x}_{t},t)\right\rVert_{1}\right]}{\mathbb{E}_{\textbf{x},\epsilon}\!\left[\left\lVert\epsilon_{\theta}(\textbf{x}_{t},t)\right\rVert_{1}\right]}. (1)

[56] p: Here, ϵ θ ​ ( x t , c , t ) \epsilon_{\theta}(\textbf{x}_{t},c,t) and ϵ θ ​ ( x t , t ) \epsilon_{\theta}(\textbf{x}_{t},t) denote the noise components predicted from the conditional and unconditional denoisers, respectively. A larger value indicates a stronger discrepancy between the two branches, reflecting a higher conditional influence on the denoising trajectory at that timestep.

[57] p: According to the trend of denoising discrepancy shown in Figure 4 , which exhibits a U-shaped curve over the entire denoising process, we divide the process into three stages: the Warm-Up Stage [ T , τ 1 ] [T,\,\tau_{1}] , the Parallelism Stage ( τ 1 , τ 2 ) (\tau_{1},\,\tau_{2}) , and the Fully Connecting Stage [ τ 2 , 0 ] [\tau_{2},\,0] . The two parameters, τ 1 \tau_{1} and τ 2 \tau_{2} , define the boundaries between these stages and are automatically determined during the middle of the denoising process. The details of how they are determined are provided in the next section. Intuitively, τ 1 \tau_{1} marks the point where the denoising discrepancy ceases to decrease rapidly, while τ 2 \tau_{2} indicates the point where it begins to increase.

[58] p: By measuring denoising discrepancy across 5,000 prompts from the MS-COCO 2014 validation set [ 15 ] , we observed that the variation of the error between the conditional and unconditional branches exhibits a clear U-shaped trend, as further demonstrated in Appendix B .

[59] p: We now describe each denoising stage in detail.

[60] p: (1) Warm-Up Stage [ T , τ 1 T,\,\tau_{1} ]. This stage captures the global outline of the generated image. The conditional branch establishes the overall composition from the text prompt, while the unconditional branch stabilizes the coarse structural forms. Since both branches have distinct influences, the denoising discrepancy remains low. Therefore, each branch is processed independently using condition-based partitioning, without adaptive parallelism switching.

[61] p: (2) Parallelism Stage ( τ 1 , τ 2 \tau_{1},\,\tau_{2} ). At this phase, the model refines local details within the preformed outline. The conditional and unconditional branches begin to converge, and the denoising discrepancy remains small and stable. To take advantage of this convergence, adaptive parallelism switching is activated, enabling a more powerful acceleration of the denoising process.

[62] p: (3) Fully-Connecting Stage [ τ 2 , 0 \tau_{2},\,0 ]. In the final phase, fine-grained conditional cues dominate generation. The framework reverts to condition-based partitioning, integrating conditional guidance to reconstruct the final image x 0 \textbf{x}_{0} .

[63] p: A similar three stages structure has also been observed in previous studies on diffusion conditional guidance [ 10 ] , which further supports the validity of our framework. Building upon this, through this three stages hybrid parallelism framework, our method achieves efficient distributed denoising while preserving generation quality.

[64] p: The denoising discrepancy, rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) can be extended to flow matching models by replacing ϵ θ \epsilon_{\theta} with the predicted velocity v θ v_{\theta} . In this case, rel-MAE t ​ ( v c , v u ) \text{rel-MAE}_{t}(v_{c},v_{u}) maintains the same role in quantifying the conditional-unconditional discrepancy over the velocity field.

[65] h3: 4.3 Adaptive Switching via Denoising Discrepancy

[66] p: The core of the proposed hybrid parallelism is to dynamically determine the timesteps τ 1 \tau_{1} and τ 2 \tau_{2} during the real-time denoising process, sequentially switching between the Warm-Up, Parallelism, and Fully-Connecting modes, while constructing a scheduling method based on the previously defined denoising discrepancy.

[67] p: (1) Determining τ 𝟏 \boldsymbol{\tau_{1}} . For each timestep t t , we compute denoising discrepancy and calculate the average slope of the most recent L L steps by

[68] table: G t = M t − M t − L L . G_{t}=\frac{M_{t}-M_{t-L}}{L}. (2)

[69] p: We then select τ 1 ′ = min ⁡ { t | 0 ≤ G t < g slope } \tau^{\prime}_{1}=\min\{t\,|\,0\leq G_{t}<g_{\text{slope}}\} and constrain it by safety-cap τ cap \tau_{\text{cap}} . As shown in Appendix B , τ cap \tau_{\text{cap}} is defined as the global minimum point of the denoising discrepancy curve, and it serves as an upper bound for τ 1 \tau_{1} during automatic selection. The introduction of τ cap \tau_{\text{cap}} ensures stability by covering cases where τ 1 \tau_{1} is assigned too late or remains undefined due to outlier behaviors, thus maintaining generation quality while maximizing acceleration.

[70] p: Consequently, τ 1 \tau_{1} is given by τ 1 = min ⁡ ( τ 1 ′ , τ cap ) \tau_{1}=\min(\tau^{\prime}_{1},\tau_{\text{cap}}) , which marks the end of the warm-up stage where conditional influence stabilizes.

[71] p: (2) Determining τ 𝟐 \boldsymbol{\tau_{2}} . During the parallelism phase, ϵ c \epsilon_{c} and ϵ u \epsilon_{u} converge to an identical value, making the denoising discrepancy measurement no longer meaningful. Therefore, τ 2 \tau_{2} is empirically fixed to a certain number of steps k k after τ 1 \tau_{1} ,

[72] table: τ 2 = τ 1 + k , k ∈ ℕ , 1 ≤ k < T − τ 1 . \tau_{2}=\tau_{1}+k,\quad k\in\mathbb{N},\;1\leq k<T-\tau_{1}.\vskip-5.69054pt (3)

[73] p: A larger k k extends the parallelism phase, resulting in faster inference but lower generation quality, while a smaller k k improves fidelity at the cost of latency. A detailed analysis of quality and speed trade-offs with respect to k k is presented in Section 5.4 , where we empirically verify the optimal balance across various k k . We also provide the algorithm of Section 4.3 in Appendix C describes the overall process.

[74] figure: Base Model Devices Methods Latency (s) ↓ \downarrow Speed-Up ↑ \uparrow Comm. (GB) ↓ \downarrow FID ↓ \downarrow LPIPS ↓ \downarrow PSNR ↑ \uparrow w/ G. T. w/ Orig. w/ G. T. w/ Orig. w/ G. T. w/ Orig. Stable Diffusion XL 1 Original Model 16.49 - - 23.977 - 0.797 - 9.618 - 2 DistriFusion [ 11 ] 13.53 1.22 × \times 0.525 24.164 4.864 0.7978 0.146 9.597 24.634 AsyncDiff [ 2 ] (stride=1) 12.54 1.31 × \times 9.830 23.941 4.103 0.797 0.108 9.586 26.387 Ours ( k k =5) 7.12 2.31 × \times 0.516 23.831 4.100 0.796 0.107 9.665 26.640 Stable Diffusion 3 1 Original Model 19.36 - - 33.433 - 0.810 - 8.086 - 2 AsyncDiff [ 2 ] (stride=1) 9.82 1.97 × \times 1.290 33.379 2.032 0.813 0.052 8.155 27.812 xDiT-Ring [ 4 ] 14.31 1.35 × \times 121.646 33.356 1.909 0.809 0.047 8.085 27.857 Parastep [ 32 ] 9.98 1.94 × \times 0.032 33.340 3.350 0.810 0.112 8.091 22.917 Ours ( k k =5) 9.33 2.07 × \times 0.189 33.322 1.878 0.780 0.046 8.229 27.875 Table 1: Quantitative comparison of parallelism methods on the Stable Diffusion XL and Stable Diffusion 3 models. We compare our method with existing distributed inference techniques under 1- and 2-GPU. We report both the baseline latency and the corresponding acceleration ratio ( Speed-Up ), Communication efficiency (Comm.) , and quantitative metrics assessing generation fidelity. Here, w/ G.T. denotes comparison with the ground-truth image, and w/ Orig. indicates comparison with the original (single-GPU) model output.

[75] h3: 4.4 Theoretical Analysis of Adaptive Switching

[76] p: Analysis of Denoising Discrepancy by Score Decomposition. The denoising discrepancy can be theoretically interpreted as a ratio between the conditional information strength and the unconditional data prior. From the score-decomposition perspective [ 31 , 8 ] , can be approximated as

[77] table: rel-MAE t ​ ( ϵ c , ϵ u ) = ‖ ϵ c − ϵ u ‖ 1 ‖ ϵ u ‖ 1 ≈ ‖ ∇ x t ​ log ​ p ​ ( c | x t ) ‖ 1 ‖ s u ​ ( x t , t ) ‖ 1 . \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u})=\frac{\|\epsilon_{c}-\epsilon_{u}\|_{1}}{\|\epsilon_{u}\|_{1}}\approx\frac{\|\nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t})\|_{1}}{\|s_{u}(\textbf{x}_{t},t)\|_{1}}. (4)

[78] p: ∇ x t ​ log ​ p ​ ( c | x t ) \nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}) represents the conditional information strength and s u ​ ( x t , t ) s_{u}(\textbf{x}_{t},t) denotes the unconditional score of the data distribution. Consequently, denoising discrepancy measures the relative magnitude between conditional and unconditional components.

[79] p: In the score formulation of Eq. ( 4 ), the unconditional score s u ​ ( x t , t ) = ∇ x t ​ log ​ p ​ ( x t ) s_{u}(\textbf{x}_{t},t)=\nabla_{\textbf{x}_{t}}\log p(\textbf{x}_{t}) captures the intrinsic structure of the data distribution, while the conditional gradient ∇ x t ​ log ​ p ​ ( c | x t ) \nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}) encodes the semantic influence of the conditioning signal c c . Their relative magnitudes evolve naturally along the diffusion process:

[80] p: Warm-Up Stage: When x t \textbf{x}_{t} is close to pure noise, s u ​ ( x t , t ) s_{u}(\textbf{x}_{t},t) carries little structural information, whereas ∇ x t ​ log ​ p ​ ( c | x t ) \nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}) dominates by guiding the global semantic layout from the prompt, leading to a large denoising discrepancy.

[81] p: Parallelism Stage: As denoising progresses, s u ​ ( x t , t ) s_{u}(\textbf{x}_{t},t) reconstructs meaningful local structures and becomes comparable in magnitude to ∇ x t ​ log ​ p ​ ( c | x t ) \nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}) . This balance satisfies ‖ s u ​ ( x t , t ) ‖ ≈ ‖ ∇ x t ​ log ​ p ​ ( c | x t ) ‖ \|s_{u}(\textbf{x}_{t},t)\|\!\approx\!\|\nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t})\| , yielding d d ​ t ​ rel-MAE t ​ ( ϵ c , ϵ u ) ≈ 0 \frac{d}{dt}\text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u})\!\approx\!0 and motivates the activation of the parallel inference phase.

[82] p: Fully-Connecting Stage: At high SNR, most patterns have been recovered by s u ​ ( x t , t ) s_{u}(\textbf{x}_{t},t) , while ∇ x t ​ log ​ p ​ ( c | x t ) \nabla_{x_{t}}\log p(c|\textbf{x}_{t}) contributes to fine-grained alignment and texture refinement, causing a mild increase in denoising discrepancy.

[83] p: This interpretation provides an intuitive explanation of how the relative magnitudes of the conditional and unconditional scores evolve across timesteps, theoretically supporting the three stages proposed (Warm-Up → \rightarrow Parallelism → \rightarrow Fully Connecting). Detailed derivations of Eq. ( 4 ) and the robustness analysis of τ 1 \tau_{1} under stochastic denoising noise are shown in Appendix D and Appendix E , respectively.

[84] h3: 4.5 Extensibility to Many GPU Configurations

[85] p: While the hybrid parallelism framework is optimized for two GPUs, it also scales well to larger even-numbered configurations. We present two extension strategies.

[86] p: (1) Batch-Level Extension. In this approach, the model generates N 2 \frac{N}{2} samples across N N GPUs, where each pair of GPUs produces one image. This structure linearly increases acceleration with the number of GPUs while maintaining near-identical generation quality. However, it is most effective when a large number of samples are generated.

[87] p: (2) Layer-Wise Pipeline Extension. This method extends the adaptive parallelism switching mechanism by dividing the optimal pipeline interval into N N layer-wise segments, thereby enabling finer-grained parallel execution across multiple devices. Unlike the batch-level scheme, it can be applied to single-sample generation, though it may incur slightly reduced acceleration efficiency and minor quality degradation due to finer partitioning.

[88] p: The structures and details of both strategies are provided in Appendix F . Supporting a degree of parallelism greater than two for a single image is deferred to future work.

[89] h2: 5 Experiments

[90] h3: 5.1 Experimental Setup

[91] p: Models. We evaluate our proposed hybrid parallelism framework on two representative diffusion backbones: Stable Diffusion XL (SDXL) [ 23 ] and Stable Diffusion 3.0 (SD3), a DiT-based flow matching model [ 3 ] . SDXL represents U-Net–based latent diffusion models [ 25 ] , while SD3 reflects the transformer-based paradigm, demonstrating the generality of our approach.

[92] p: Datasets. All experiments are conducted on the MS-COCO Captions 2014 benchmark [ 15 ] , using 5,000 validation prompts for text-to-image generation. Generated images are compared against both the ground-truth samples and the single-GPU original model outputs.

[93] p: Metrics. We evaluate inference efficiency and generative quality. Latency and speed-up ratio measure acceleration. For quality, we report FID (Fréchet Inception Distance) [ 6 ] , LPIPS (Learned Perceptual Image Patch Similarity) [ 41 ] , and PSNR (Peak Signal-to-Noise Ratio). Lower FID/LPIPS and higher PSNR indicate better generation quality.

[94] p: For implementation details, please refer to Appendix G .

[95] figure: Figure 5 : Qualitative results of the main experiments. We compare 1024 × \times 1024 image generations from the SDXL model. Our method achieves the best acceleration and FID performance, while producing visuals most similar to the original.

[96] figure: Figure 6 : Visualization of speed–quality trade-off across different parallelism intervals k \boldsymbol{k} . Smaller k k values preserve higher fidelity, whereas larger k k achieve greater acceleration. Our method consistently dominates prior works across the trade-off frontier. All experiments were conducted on 2 GPUs.

[97] h3: 5.2 Main Results

[98] p: Quantitative Results. Table 1 reports a quantitative comparison across SDXL and SD3 pre-train diffusion models. On SDXL, our method achieves a 2.31 × \times acceleration over the single-GPU baseline while slightly improving image fidelity. Compared to prior distributed inference methods such as DistriFusion, [ 11 ] and AsyncDiff, [ 2 ] , our proposed method attains the best speed–quality trade-off with minimal communication overhead. Notably, our communication cost is reduced by 19.6 × \times compared to AsyncDiff, due to adaptive parallelism switching that dynamically determines optimal parallel intervals to minimize communication cost.

[99] p: For SD3, a DiT-based flow-matching model, our approach not only surpasses earlier distributed frameworks such as DistriFusion and AsyncDiff, but also consistently outperforms more recent baselines, xDiT-Ring and Parastep. It achieves a 2.07 × \times speed-up with negligible communication cost while maintaining comparable or superior generation quality. These results emphasize our method’s strong generality across both U-Net and DiT architectures, achieving generation efficiency.

[100] p: Qualitative Results. Figure 5 presents qualitative comparisons among distributed inference methods. While DistriFusion and AsyncDiff exhibit boundary artifacts or spatial inconsistency, our method preserves global coherence and fine-grained details similar to the original model. These results confirm that the proposed hybrid parallelism framework maintains high visual fidelity while achieving substantial acceleration. Further results are shown in Appendix I .

[101] figure: Methods Latency (s) ↓ \downarrow Speed-Up ↑ \uparrow FID ↓ \downarrow (w/ Orig.) Original Model 16.49 - - Full Condition-Based Partitioning 9.24 1.78 × \times 3.623 Ours (Hybrid Parallelism) 7.12 2.31 × \times 4.100 Table 2: Ablation on hybrid parallel components. All experiments are conducted on the SDXL model at 1024 × \times 1024 resolution, comparing the single-GPU baseline, full condition-based partitioning, and our hybrid parallelism framework.

[102] h3: 5.3 Ablation Study

[103] p: Ablation on Hybrid Parallel Components. Table 2 analyzes the contribution of each hybrid parallel component. We compare three settings: (1) the original single-GPU model, (2) full condition-based partitioning applied to all denoising steps, and (3) our proposed hybrid parallelism combining both condition-based partitioning and adaptive parallelism switching. Condition-based partitioning achieves a 1.78 × \times speed-up while maintaining image quality, whereas our hybrid parallelism further improves efficiency to 2.31 × \times with comparable quality. This demonstrates that the addition of the pipeline component maximizes generation acceleration while minimizing quality degradation. Consequently, the proposed framework effectively integrates the advantages of condition-based partitioning and adaptive parallelism switching.

[104] h3: 5.4 Sensitivity Analysis

[105] p: Impact of Different k k Values. As shown in Figure 6 , the parallelism interval k k clearly reveals a speed–quality trade-off: smaller k k values preserve higher fidelity, while larger k k values yield faster generation. An appropriate balance is observed at k = 5 k{=}5 , achieving both strong quality and acceleration. Moreover, the interval k k can be flexibly chosen by practitioners to adjust the trade-off between efficiency and fidelity. Quantitative results are summarized in Appendix H , and qualitative comparisons across different k k values are provided in Appendix J .

[106] figure: Figure 7 : Comparison of high-resolutions tasks. We compare different parallel inference methods on the SDXL model using NVIDIA H200 GPUs across 1024 × \times 1024, 2048 × \times 2048, and 2560 × \times 2560 high-resolutions.

[107] p: High-Resolution Generation. As shown in Figure 7 , our method consistently achieves superior acceleration over existing distributed inference frameworks across increasing resolutions. On the SDXL model using NVIDIA H200 GPUs, our hybrid parallelism attains up to 2.72 × \times speed-up at 1024 × \times 1024, 1.54 × \times speed-up at 2048 × \times 2048, and 1.62 × \times speed-up at 2560 × \times 2560, demonstrating strong scalability for high-resolution image generation.

[108] h2: 6 Conclusion

[109] p: In this paper, we introduced a hybrid parallelism framework for diffusion inference that integrates condition-based partitioning with adaptive parallelism switching. Guided by the denoising discrepancy criterion, the method adaptively switches between parallelism modes to minimize redundant communication. It achieves 2.31 × 2.31\times and 2.07 × 2.07\times latency reductions on SDXL and SD3, respectively, while preserving fidelity. We also generalize across U-Net and DiT architectures, providing a unified parallelism paradigm for scalable multi-GPU diffusion inference.

[110] h2: References

[111] p: Supplementary Material

[112] h2: Appendix A Evaluation of Hybrid Parallelism

[113] figure: Methods Speed-Up ↑ \uparrow Image Quality ↑ \uparrow Model General. ↑ \uparrow High-res Synth. ↑ \uparrow Comm. Efficiency ↑ \uparrow Distrifusion 2.5 3.5 2.5 3.3 5.0 AsyncDiff 3.0 4.5 5.0 3.5 1.0 Ours 4.7 4.5 5.0 4.4 5.0 Table 3 : Quantitative metrics comparison across five evaluation aspects. Scores are normalized to a 5-point scale. Higher values ( ↑ \uparrow ) indicate better performance.

[114] p: Evaluation Protocol. All scores are computed based on a 5-point scale unified min–max scaling scheme, where the normalized values are re-centered around an average score of 3. Specifically, each metric is assessed as follows:

[115] p: Speed-Up. We measure the relative acceleration ratio with respect to the SDXL baseline latency in Table 1 . The measured latencies are 13.53secs for DistriFusion, 12.54secs for AsyncDiff, and 7.12secs for our method.

[116] p: Image Quality. We evaluate image quality using FID scores reported in Table 1 from the main results of SDXL. The reported FID values are 4.864 for DistriFusion, 4.103 for AsyncDiff, and 4.100 for our method.

[117] p: Model Generality. We assign scores based on architecture compatibility. Each model receives 2.5 points for supporting U-Net and an additional 2.5 points for DiT support, resulting in scores of 2.5 for DistriFusion, 5 for AsyncDiff, and 5 for Ours.

[118] p: High-resolution Synthesis. The score reflects both high-resolution generation capability and inference latency. According to the results in Section 5.4 High-Resolution Generation, all three methods successfully generate three target resolutions. The corresponding average latencies are 14.73secs for DistriFusion, 14.27secs for AsyncDiff, and 11.99secs for Ours.

[119] p: Communication Efficiency. We evaluate the communication efficiency based on the measured inter-GPU data transfer communication volume in the SDXL multi-GPU setting reported in Table 1 from the main results. The measured communication volumes are 0.525 GB for DistriFusion, 9.830 GB for AsyncDiff, and 0.516 GB for our method.

[120] h2: Appendix B Empirical Visualization of Denoising Discrepancy

[121] figure: Figure 8 : Empirical visualization of denoising discrepancy curve.

[122] p: Figure 8 illustrates the average denoising discrepancy ( rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) ) value measured during the denoising process based on 5,000 prompts from the MS-COCO 2014 [ 15 ] validation set. The shaded region represents the ± 2 ​ σ \pm 2\sigma range, and the denoising model used is Stable Diffusion XL. The red dot denotes τ cap = argmin 𝑡 ​ rel-MAE t ​ ( ϵ c , ϵ u ) \tau_{\text{cap}}=\underset{t}{\mathrm{argmin}}\,\text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) , which is employed as a safety-cap in the main method.

[123] h2: Appendix C Adaptive Parallelism Switching Algorithm

[124] figure: Algorithm 1 Adaptive Parallelism Switching via Denoising Discrepancy 1: latent noise x t \textbf{x}_{t} , prompt c c , steps T T , window L L , slope threshold g g , safety-cap τ cap \tau_{\text{cap}} , interval k k 2: τ 1 , τ 2 ← ∅ \tau_{1},\tau_{2}\leftarrow\varnothing 3: for t = T , T − 1 , … , 1 t=T,T\!-\!1,\ldots,1 do 4: ϵ c , ϵ u ← ϵ θ ​ ( x t , c , t ) , ϵ θ ​ ( x t , t ) \epsilon_{c},\epsilon_{u}\leftarrow\epsilon_{\theta}(\textbf{x}_{t},c,t),~\epsilon_{\theta}(\textbf{x}_{t},t) 5: M t ← 𝔼 x , ϵ ​ ‖ ϵ c − ϵ u ‖ 1 𝔼 x , ϵ ​ ‖ ϵ u ‖ 1 M_{t}\leftarrow\dfrac{\mathbb{E}_{x,\epsilon}\|\epsilon_{c}-\epsilon_{u}\|_{1}}{\mathbb{E}_{x,\epsilon}\|\epsilon_{u}\|_{1}} ⊳ \triangleright rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) 6: G t = M t − M t − L L G_{t}=\frac{M_{t}-M_{t-L}}{L} 7: if τ 1 = ∅ \tau_{1}=\varnothing and t > L t>L and 0 ≤ G t < g 0\leq\textstyle G_{t}<g then 8: τ 1 ← min ⁡ ( t , τ cap ) \tau_{1}\leftarrow\min(t,\,\tau_{\text{cap}}) ; τ 2 ← τ 1 + k \tau_{2}\leftarrow\tau_{1}+k 9: Denoise: 10: if t ≥ τ 1 t\geq\tau_{1} then 11: Warm-Up 12: else if t > τ 2 t>\tau_{2} then 13: Parallelism 14: else 15: Fully-Connecting 16: end if 17: x t − 1 ← Step Denoise ​ ( x t , ϵ c , ϵ u , t ) x_{t-1}\leftarrow\textsc{Step\;Denoise}(\textbf{x}_{t},\epsilon_{c},\epsilon_{u},t) 18: end for 19: return x 0 , ( τ 1 , τ 2 ) x_{0},~(\tau_{1},\tau_{2})

[125] h2: Appendix D Derivation of Score-Based Interpretation of Denoising Discrepancy

[126] p: The denoising discrepancy( rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) ) criterion in Eq. ( 4 ) can be theoretically derived from the score decomposition of diffusion models. Following the ϵ \epsilon -parameterization of score-based generative modeling [ 31 , 8 ] , the preconditioned score can be expressed as

[127] table: s θ ​ ( x t , t ) ≈ − ϵ θ ​ ( x t , t ) σ t , s_{\theta}(\textbf{x}_{t},t)\approx-\,\frac{\epsilon_{\theta}(\textbf{x}_{t},t)}{\sigma_{t}}, (5)

[128] p: where σ t \sigma_{t} denotes the noise standard deviation at timestep t t . According to Bayes’ rule, the conditional score function can be decomposed as

[129] table: s c ​ ( x t , t ) = s u ​ ( x t , t ) + ∇ x t ​ log ​ p ​ ( c | x t ) , s_{c}(\textbf{x}_{t},t)=s_{u}(\textbf{x}_{t},t)+\nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}), (6)

[130] p: where s u ​ ( x t , t ) s_{u}(\textbf{x}_{t},t) is the unconditional data score, and ∇ x t ​ log ​ p ​ ( c | x t ) \nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}) denotes the conditional information flow [ 7 ] . Substituting Eq. (( 5 )) into Eq. (( 6 )) yields

[131] table: ϵ c ​ ( x t , t ) − ϵ u ​ ( x t , t ) ∝ σ t ​ ∇ x t ​ log ⁡ p ⁡ ( c | x t ) , \epsilon_{c}(\textbf{x}_{t},t)-\epsilon_{u}(\textbf{x}_{t},t)\propto\sigma_{t}\,\nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t}), (7)

[132] p: which implies that the difference between conditional and unconditional denoiser outputs corresponds to the conditional gradient scaled by σ t \sigma_{t} . Therefore, the rel-MAE at each timestep t t can be approximated as

[133] table: rel ​ - ​ MAE t = ‖ ϵ c − ϵ u ‖ 1 ‖ ϵ u ‖ 1 ≈ ‖ ∇ x t ​ log ​ p ​ ( c | x t ) ‖ 1 ‖ s u ​ ( x t , t ) ‖ 1 . \mathrm{rel\text{-}MAE}_{t}=\frac{\|\epsilon_{c}-\epsilon_{u}\|_{1}}{\|\epsilon_{u}\|_{1}}\approx\frac{\|\nabla_{\textbf{x}_{t}}\log p(c|\textbf{x}_{t})\|_{1}}{\|s_{u}(\textbf{x}_{t},t)\|_{1}}. (8)

[134] p: This formulation reveals that rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) quantifies the relative magnitude between the conditional information and the unconditional data prior—forming the theoretical basis for the main method equation (Eq. ( 4 )).

[135] h2: Appendix E Robustness of Determine 𝝉 𝟏 \boldsymbol{\tau_{1}} under Stochastic Denoising Noise

[136] p: Diffusion inference is a stochastic denoising process; predicted noises ϵ θ ​ ( x t ) \epsilon_{\theta}(\textbf{x}_{t}) are subject to random sampling. Consequently, the observed { M t } \{M_{t}\} fluctuates slightly, and G t ≈ 0 G_{t}\!\approx\!0 may appear prematurely. To ensure robust detection, we define a finite-difference slope by

[137] table: G t = M t − M t − L L , G_{t}=\frac{M_{t}-M_{t-L}}{L}, (9)

[138] p: which smooths out stochastic perturbations across L L timesteps. The stability of G t G_{t} can be theoretically justified by Hoeffding’s inequality:

[139] table: Pr ⁡ ( | G t − 𝔼 ⁡ [ G t ] | > δ ) ≤ 2 ​ exp ⁡ ( − 2 ​ L ​ δ 2 ( b − a ) 2 ) . \Pr(|G_{t}-\mathbb{E}[G_{t}]|>\delta)\leq 2\exp\!\Big(-\frac{2L\delta^{2}}{(b-a)^{2}}\Big). (10)

[140] p: Here, L L denotes the window length used to compute the moving-average slope, δ \delta represents the allowable deviation from the expected slope 𝔼 ⁡ [ G t ] \mathbb{E}[G_{t}] , and a , b a,b correspond to the minimum and maximum possible range of the observed rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) values, typically normalized within [ 0 , 1 ] [0,1] .

[141] p: As L L increases, the variance of the estimated slope decreases, and the probability of false detection decreases exponentially. showing that larger L L exponentially reduces false-alarm probability.

[142] p: Empirically, L L and g slope g_{\text{slope}} , which are also established in our experiments, lie within a stable regime due to strong autocorrelation of rel-MAE t ​ ( ϵ c , ϵ u ) \text{rel-MAE}_{t}(\epsilon_{c},\epsilon_{u}) sequences. Thus, τ 1 \tau_{1} can be reliably detected as the earliest timestep satisfying ≤ G t < g slope 0\!\leq\!G_{t}\!<\!g_{\text{slope}} and t ≤ τ cap t\!\leq\!\tau_{\text{cap}} .

[143] h2: Appendix F Extensibility to Many GPU Configurations Structures

[144] p: Figure 9 presents two extensibility structures that scale the proposed hybrid parallelism framework from the baseline 2 GPUs setup to many GPU configurations.

[145] p: The first structure, shown in Figure 9(a) , demonstrates the batch-level extension under an 𝑵 \boldsymbol{N} GPUs configuration. In this scheme, each pair of GPUs collaboratively denoises a single sample while following the three stages hybrid parallelism framework. As a result, the system can generate N / 2 N/2 samples concurrently with N N GPUs, enabling near-linear throughput scaling when multiple samples are produced.

[146] p: The second structure, shown in Figure 9(b) , demonstrates the layer-wise pipeline extension on a 4 GPUs configuration. Here, the denoising network is partitioned into multiple layer-wise segments distributed across devices, allowing the hybrid parallelism strategy to be applied to single-sample generation. While this configuration may exhibit slightly reduced acceleration efficiency and minor quality degradation compared to the batch-level extension, it provides a fine-grained pipeline scheduling mechanism. Importantly, the same structural principles naturally generalize beyond the 4 GPUs example to arbitrary N N GPUs configurations, demonstrating the flexibility and scalability of the proposed framework.

[147] figure: (a) Batch-level extension under 𝑵 \boldsymbol{N} GPUs configuration. (b) Layer-wise pipeline extension on a 4 GPUs configuration. Figure 9 : Extensibility to many GPU configurations structures. This figure illustrates two strategies for scaling the proposed hybrid parallelism framework to larger GPU configurations. These structures demonstrate how the proposed framework naturally generalizes from the 2 GPUs setting to both batch-level and layer-wise many GPU configurations.

[148] h2: Appendix G Implementation Details

[149] p: All experiments adopt the DDIM scheduler [ 30 ] with T = 50 T=50 timesteps and generate images at a resolution of 1024 × 1024 1024\times 1024 . Experiments are performed on NVIDIA GeForce 3090 GPUs (24GB each), connected via PCIe Gen3. The adaptive switching parameters are set as follows: for SDXL, we use L = 12 L=12 , g slope = 0.4 × 10 − 3 g_{\text{slope}}=0.4\times 10^{-3} , k = 5 k=5 , and τ cap = 15 \tau_{\text{cap}}=15 ; for SD3, we set L = 15 L=15 , g slope = 0.1 × 10 − 3 g_{\text{slope}}=0.1\times 10^{-3} , k = 5 k=5 , and τ cap = 40 \tau_{\text{cap}}=40 .

[150] h2: Appendix H Quantitative Results on the Parallelism Interval 𝒌 \boldsymbol{k}

[151] figure: Parallelism Interval k k Latency (s) ↓ \downarrow Speed-Up ↑ \uparrow FID ↓ \downarrow (w/ Orig.) k k =5 7.12 2.31 × \times 4.100 k k =10 6.89 2.39 × \times 5.942 k k =20 6.44 2.56 × \times 7.966 k k =30 5.94 2.78 × \times 9.191 Table 4: Effect of speed-quality trade-off across different parallelism intervals k \boldsymbol{k} . All experiments are conducted on the SDXL model at 1024 × \times 1024 resolution with various parallelism intervals.

[152] p: Table 4 summarizes the numerical values corresponding to the speed–quality trade-off illustrated in Figure 6 . As described in the Section 5.4 , smaller parallelism interval k k preserve higher fidelity, whereas larger k k values yield powerful acceleration. The table provides concrete measurements that reflect this trade-off, confirming the same trend observed in the pareto frontier visualization.

[153] h2: Appendix I Additional Qualitative Results

[154] figure: Figure 10 : Additional qualitative results of the main experiments. We compare 1024 × \times 1024 image generations from the SDXL model. Our method achieves the best acceleration and FID performance, while producing visuals most similar to the original.

[155] h2: Appendix J Qualitative Comparion Results via Different 𝒌 \boldsymbol{k}

[156] figure: Figure 11 : Additional qualitative comparisons across different k k values. We compare 1024 × \times 1024 image generations from the SDXL model across various parallelism intervals. Smaller k k values preserve higher visual fidelity, whereas larger k k gradually reduce local detail due to the extended parallelism window. Although the overall appearance remains similar, fine-grained conditional attributes become subtly blurred as k k increases.

[157] h2: Instructions for reporting errors

[158] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[159] p: Tip: You can select the relevant text first, to include it in your report.

[160] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[161] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
