[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ProjFlow: Projection Sampling with Flow Matching for Zero‑Shot Exact Spatial Motion Control

[3] h6: Abstract

[4] p: Generating human motion with precise spatial control is a challenging problem. Existing approaches often require task-specific training or slow optimization, and enforcing hard constraints frequently disrupts motion naturalness. Building on the observation that many animation tasks can be formulated as a linear inverse problem, we introduce ProjFlow , a training-free sampler that achieves zero-shot, exact satisfaction of linear spatial constraints while preserving motion realism. Our key advance is a novel kinematics-aware metric that encodes skeletal topology. This metric allows the sampler to enforce hard constraints by distributing corrections coherently across the entire skeleton, avoiding the unnatural artifacts of naive projection. Furthermore, for sparse inputs, such as filling in long gaps between a few keyframes, we introduce a time-varying formulation using pseudo-observations that fade during sampling. Extensive experiments on representative applications, motion inpainting, and 2D-to-3D lifting, demonstrate that ProjFlow achieves exact constraint satisfaction and matches or improves realism over zero-shot baselines, while remaining competitive with training-based controllers.

[5] figure: Figure 1 : ProjFlow provides a unified, zero-shot framework for exact spatial motion control. The method handles diverse applications by formulating them as linear inverse problems. Examples of applications include (a) precisely following a specified joint’s trajectory, (b) lifting 2D keypose and 2D trajectory inputs to a full 3D motion, (c) maintaining a fixed relative position between joints, and (d) generating seamlessly looped motion by matching start and end poses.

[6] h2: 1 Introduction

[7] p: An open challenge in character animation is spatial motion control, which involves generating realistic full-body motion that conforms to user-defined spatial cues. These cues can include trajectories, target poses, or specific joint locations. Solving this task would allow 3D animators to work with precise and interactive control, immediately obtaining desired motions that remain natural and diverse [ 55 , 1 ] .

[8] p: Users typically specify constraints for only a subset of the body, such as the trajectory of a single hand or foot. This makes the spatial motion control problem ill-posed, with many motions satisfying these sparse constraints. An intuitive approach to resolve this ambiguity is to favor motions with high likelihood under a pretrained motion prior, selecting the most natural result from all valid options.

[9] p: Building on this idea, dominant approaches steer pretrained diffusion models to satisfy user-defined spatial constraints. However, existing methods suffer from significant limitations. They often require task-specific training for conditioning branches [ 63 , 39 , 9 , 45 ] , or they rely on slow, inference-time optimization [ 20 , 48 , 44 , 45 ] , which reduces interactivity and can get stuck in local minima. Fundamentally, these approaches treat constraints as soft objectives rather than hard rules. As a result, exact satisfaction is not guaranteed, and residual violations persist. What is missing is a sampler that can (i) enforce hard equality constraints exactly, (ii) operate zero-shot without task-specific retraining, and (iii) require no inner-loop optimization at inference time, all while preserving the pretrained motion prior.

[10] p: In this paper, we present ProjFlow , Proj ection Sampling with Flow Matching for zero-shot exact spatial motion control. We begin with the observation that a wide range of motion control and editing tasks can be formulated as linear inverse problems. These tasks include trajectory following, keyframing, camera or root path control, and partial-body editing. ProjFlow addresses these problems by projecting the predicted clean motion at every denoising step onto the set of motions that satisfy the given constraints. This projection introduces the smallest necessary adjustment, measured under a newly designed kinematics-aware metric that reflects skeletal topology. Rather than measuring the distance in Euclidean space, this metric ensures that updates propagate coherently along the kinematic tree, avoiding unnatural and isolated joint movements. Hard constraints are satisfied exactly, while uncertain or partial measurements are weighted according to their confidence. The projected update is then combined with a flow-matching recomposition step, preserving the pretrained motion prior without any task-specific retraining or inner-loop optimization.

[11] p: We evaluate the versatility of the ProjFlow framework through two representative applications in spatial motion control. The first application is motion inpainting, where segments of a motion sequence are entirely missing. This task requires the model to infer plausible intermediate frames from sparse temporal observations. Instead of treating the unobserved frames as blanks, ProjFlow introduces pseudo-observations around known frames and gradually adjusts their influence during sampling, enabling coherent zero-shot completion even across long temporal gaps.

[12] p: The second application is 2D-to-3D motion reconstruction, where the input consists of 2D keypoints and their trajectories over time. The goal is to recover the underlying 3D motion that projects onto the observed 2D data. ProjFlow enforces linear measurement constraints derived from the camera model as hard equalities at each step. This yields accurate 3D reconstructions with zero reprojection error and natural motion. Our experiments on these applications show ProjFlow matches the accuracy of training-based methods without any retraining or inner-loop optimization. These results demonstrate the versatility of our framework, which can also be applied to the other tasks illustrated in Fig. 1 .

[13] p: In summary, our contributions are as follows:

[14] p: Unified linear inverse formulation and projection sampler as its solver. We cast motion control and editing as linear inverse problems and propose a projection-based flow-matching sampler that enforces constraints exactly without retraining or inner-loop optimization.

[15] p: Kinematics-aware projection geometry. We introduce a metric that encodes skeletal structure, providing a principled geometry that distributes corrections coherently and improves realism and stability.

[16] p: Empirical parity on inpainting and 2D-to-3D with exact constraints. Through experiments on motion inpainting and 2D-to-3D reconstruction, we show that ProjFlow matches the performance of training-based models while satisfying the specified constraints exactly up to numerical precision, all in a zero-shot, no inner loop setting.

[17] h2: 2 Related Work

[18] h3: 2.1 Human Motion Generation

[19] p: Recent advances in image generation indicate a transition from denoising diffusion probabilistic models and score-based SDEs to flow matching models that learn velocity fields using rectified-flow objectives, scaling well with Transformer architectures [ 17 , 54 , 33 , 36 , 13 , 34 ] . Progress in text-conditioned human motion generation has followed the same arc. Early state-of-the-art systems were diffusion-based [ 57 , 66 , 8 , 67 ] , while more recent work adopts flow-matching formulations [ 18 , 4 ] .

[20] p: Alongside advances in generative methodology, motion representation has also evolved. HumanML3D [ 15 ] popularized a kinematic, relative, and partly redundant feature representation still adopted by many controllers [ 15 , 63 , 21 , 9 ] . Evidence now shows that generating absolute joint coordinates in world space with a rectified-flow objective is effective and beneficial for controllability and scalability [ 39 , 40 ] . These trends motivate our choice of a flow-matching sampler operating directly in world coordinates.

[21] h3: 2.2 Spatially Controlled Motion Generation

[22] p: While text prompts are effective for controlling high-level motion semantics, many practical applications require more precise spatial control. Synthesizing motion from a wider range of external control signals, often in combination with text prompts, has been widely explored. Examples include authoring from storyboard sketches [ 68 ] and multi-track timeline authoring [ 43 ] . Other research streams focus on multi-objective control for characters and robots [ 50 , 3 ] , music-conditioned choreography [ 25 , 28 , 58 , 29 , 30 , 26 ] , or generating motions involving inter-human [ 56 , 32 , 14 , 41 ] and human-object interactions [ 5 , 10 , 24 , 27 ] . Control signals can also include sparse tracking inputs [ 12 ] , scene affordances [ 19 , 62 ] , programmable objectives [ 35 ] , style specifications [ 69 ] , or goal-directed targets [ 11 ] .

[23] p: A key question is how to effectively integrate these spatial signals into text-to-motion generators to enforce precise accuracy. Prior work has taken several routes to tackle this. One approach involves fine-tuning diffusion priors with end-effector supervision [ 51 ] or training models for in-betweening from dense or sparse keyframes [ 7 ] . Another line of work applies guidance during sampling, steering the generation towards root or waypoint trajectories [ 21 , 47 ] . More recently, joint-wise conditioning has been achieved using ControlNet-style branches or latent controllers [ 63 , 9 , 65 ] . Others perform inference-time optimization of the initial noise or logits to minimize differentiable objectives [ 20 , 45 ] , or use factorization and controller mixtures for fine-grained control [ 59 , 31 ] . Across these routes, constraints are injected as differentiable penalties or guidance terms rather than enforced as hard feasibility constraints. Consequently, exact feasibility is not guaranteed, and methods often require task‑specific conditioning or iterative inner‑loop optimization during inference.

[24] h3: 2.3 Inverse Problems with Image Generation

[25] p: Pre-trained diffusion priors have enabled strong zero-shot solvers for linear inverse problems. Two influential views have emerged. The first is likelihood guidance along the sampling path [ 6 , 22 ] . The second is projection that freezes range-space and refines only the null-space (DDNM) [ 61 ] , with extensions such as pseudoinverse guidance [ 53 ] . To leverage large latent generative models, latent diffusion model-based variants inject data consistency in latent space [ 49 , 52 , 64 ] . Recently, these ideas have been extended to flow models. FlowChef and PnP-Flow steer rectified-flow fields or plug a learned denoiser into a flow solver [ 42 , 38 ] , but do not cast inverse solving as closed-form posterior steps on the flow path.

[26] p: ProjFlow adapts data consistency updates to the flow matching regime, and the framework generalizes prior posterior projection samplers in two key ways. First, it replaces the common Euclidean geometry of image methods with a kinematics-aware metric that distributes corrections coherently along the skeleton, which better supports structured data such as human motion. Second, the framework introduces time-scheduled pseudo-observations that densify guidance in unobserved regions and then fade as sampling proceeds, improving on prior approaches that treat missing regions as simple blanks. Finally, ProjFlow recovers DDNM in the Euclidean noiseless deterministic limit while extending support to structured metrics, noisy measurements, and time-varying operators.

[27] h2: 3 Preliminaries

[28] h3: 3.1 Motion Representation

[29] p: We represent a clean motion sequence of length N N with J J joints in absolute world coordinates as a tensor 𝒙 ∈ ℝ N × J × 3 {\bm{x}}\in\mathbb{R}^{N\times J\times 3} . For brevity, we also use 𝒙 {\bm{x}} to denote its vectorization 𝒙 ∈ ℝ d {\bm{x}}\in\mathbb{R}^{d} with d = 3 ​ J ​ N d=3JN . Unless stated otherwise, we assume a frame-major order. Each vector element i ∈ { 1 , … , d } i\in\{1,\dots,d\} corresponds to a unique frame–joint–spatial-channel triple ( n i , j i , c i ) (n_{i},j_{i},c_{i}) , where n i ∈ { 1 , … , N } n_{i}\!\in\!\{1,\dots,N\} , j i ∈ { 1 , … , J } j_{i}\!\in\!\{1,\dots,J\} , and c i ∈ { x , y , z } c_{i}\!\in\!\{x,y,z\} .

[30] h3: 3.2 Flow Matching

[31] p: The core idea of flow-based generative models [ 33 , 36 , 2 ] is to learn a time-dependent vector field v θ ​ ( 𝒙 , t ) v_{\theta}({\bm{x}},t) that transports samples from a simple prior distribution p 0 p_{0} to a complex target data distribution q q .

[32] p: Let ψ t : ℝ d → ℝ d \psi_{t}:\mathbb{R}^{d}\!\to\!\mathbb{R}^{d} denote the flow map induced by this vector field. The flow map is defined as the unique solution to the Ordinary Differential Equation (ODE)

[33] table: d ​ ψ t ​ ( 𝒙 0 ) d ​ t = v θ ​ ( ψ t ​ ( 𝒙 0 ) , t ) , ψ 0 ​ ( 𝒙 0 ) = 𝒙 0 , \frac{d\psi_{t}({\bm{x}}_{0})}{dt}\;=\;v_{\theta}\!\big(\psi_{t}({\bm{x}}_{0}),t\big),\qquad\psi_{0}({\bm{x}}_{0})={\bm{x}}_{0}, (1)

[34] p: where 𝒙 0 {\bm{x}}_{0} is the initial condition.

[35] p: In this study, we adopt the Rectified Flow formulation [ 36 , 34 ] , which defines a straight-line path between a noise sample 𝒙 0 {\bm{x}}_{0} and a data sample 𝒙 1 {\bm{x}}_{1} :

[36] table: 𝒙 t = ( 1 − t ) ​ 𝒙 0 + t ​ 𝒙 1 , t ∈ [ 0 , 1 ] . {\bm{x}}_{t}=(1-t)\,{\bm{x}}_{0}+t\,{\bm{x}}_{1},\qquad t\in[0,1]. (2)

[37] p: Along this path, the ideal velocity is constant and equal to 𝒙 1 − 𝒙 0 {\bm{x}}_{1}-{\bm{x}}_{0} . The network v θ v_{\theta} is trained to approximate the conditional expectation of this velocity given ( 𝒙 t , t ) ({\bm{x}}_{t},t) by minimizing the conditional flow-matching loss

[38] table: ℒ FM ​ ( θ ) = 𝔼 t ∼ 𝒰 ⁡ ( 0 , 1 ) 𝒙 0 ∼ p 0 𝒙 1 ∼ q ​ [ ‖ v θ ​ ( 𝒙 t , t ) − ( 𝒙 1 − 𝒙 0 ) ‖ 2 2 ] , \mathcal{L}_{\text{FM}}(\theta)=\mathbb{E}_{\begin{subarray}{c}t\sim\mathcal{U}(0,1)\\ {\bm{x}}_{0}\sim p_{0}\\ {\bm{x}}_{1}\sim q\end{subarray}}\!\left[\,\big\|v_{\theta}({\bm{x}}_{t},t)-({\bm{x}}_{1}-{\bm{x}}_{0})\big\|_{2}^{2}\right], (3)

[39] p: where 𝒙 t {\bm{x}}_{t} is given by equation 2 . Sampling is then performed by drawing 𝒙 0 ∼ p 0 {\bm{x}}_{0}\sim p_{0} and numerically integrating the ODE in equation 1 from t = 0 t=0 to t = 1 t=1 to obtain 𝒙 1 = ψ 1 ​ ( 𝒙 0 ) {\bm{x}}_{1}=\psi_{1}({\bm{x}}_{0}) .

[40] p: This formulation provides a continuous and differentiable generative path between the prior and data distributions, which later facilitates direct constraint enforcement in our projection-based framework.

[41] figure: Figure 2 : Overview of the Projection Sampling Step. At each timestep t t : (1) predict the clean endpoint 𝒙 ^ 1 \hat{{\bm{x}}}_{1} from 𝒙 t {\bm{x}}_{t} using the learned velocity v θ ​ ( 𝒙 t , t ) v_{\theta}({\bm{x}}_{t},t) ; (2) enforce the linear–Gaussian measurements 𝒚 = A ​ 𝒙 + ϵ {\bm{y}}=A{\bm{x}}+{\bm{\epsilon}} by computing a correction Δ ​ 𝒙 1 ⋆ \Delta{\bm{x}}_{1}^{\star} that projects 𝒙 ^ 1 \hat{{\bm{x}}}_{1} to the measurement set under the kinematics-aware metric R R . This metric encodes skeletal topology and spreads updates coherently along the kinematic tree. The measurement covariance Σ \Sigma modulates the pull toward the observations; smaller values yield stronger attraction and recover hard constraints as Σ → 0 \Sigma\to 0 . (3) Finally, stochastically recompose the corrected endpoint to obtain the next state 𝒙 t + Δ ​ t {\bm{x}}_{t+\Delta t} .

[42] h2: 4 Method

[43] p: In this section, we first formulate spatial control as a unified linear inverse problem (Sec. 4.1 ). We then introduce ProjFlow, our kinematics-aware projection sampler (Sec. 4.2 ), and demonstrate its use in representative applications (Sec. 4.3 ).

[44] h3: 4.1 Spatial Motion Control as a Linear Inverse Problem

[45] p: We unify all user-specified constraints into a single linear observation model

[46] table: 𝒚 = A ​ 𝒙 + ϵ , ϵ ∼ 𝒩 ⁡ ( 𝟎 , Σ ) , \displaystyle{\bm{y}}\;=\;A{\bm{x}}\;+\;{\bm{\epsilon}},\qquad{\bm{\epsilon}}\sim\mathcal{N}(\mathbf{0},\,\Sigma), (4)

[47] p: where 𝒚 ∈ ℝ m {\bm{y}}\in\mathbb{R}^{m} is the vector of user-specified observed measurements, A : ℝ d → ℝ m A:\mathbb{R}^{d}\!\to\!\mathbb{R}^{m} is a known linear operator, and Σ ⪰ 𝟎 \Sigma\succeq\mathbf{0} is an observation noise covariance. Hard constraints are recovered as the limiting case where the corresponding rows of Σ \Sigma tend to zero variance.

[48] p: Our objective is to generate a motion 𝒙 ^ \hat{{\bm{x}}} that is consistent with the observation model equation 4 while maintaining the realism encoded in the pretrained motion prior.

[49] h3: 4.2 Projection Sampling with Flow Matching

[50] p: Given the intermediate state 𝒙 t {\bm{x}}_{t} and the predicted velocity v θ ​ ( 𝒙 t , t ) v_{\theta}({\bm{x}}_{t},t) , as shown in Fig. 2 , the corresponding clean endpoints can be obtained by Tweedie’s formula [ 23 ]

[51] table: 𝒙 ^ 1 \displaystyle\hat{{\bm{x}}}_{1} = 𝔼 ⁡ [ 𝒙 1 | 𝒙 t ] = 𝒙 t + ( 1 − t ) ​ v θ ​ ( 𝒙 t , t ) . \displaystyle=\mathbb{E}[{\bm{x}}_{1}|{\bm{x}}_{t}]={\bm{x}}_{t}+(1-t)v_{\theta}({\bm{x}}_{t},t). (5)

[52] p: We seek the smallest clean-endpoint correction Δ ​ 𝒙 1 \Delta{\bm{x}}_{1} (in the metric R ≻ 0 R\!\succ\!0 ) by solving the problem

[53] table: min Δ ​ 𝒙 1 ⁡ 1 2 ​ ‖ Δ ​ 𝒙 1 ‖ R 2 + 1 2 ​ ‖ 𝒚 − A ⁡ ( 𝒙 ^ 1 + Δ ​ 𝒙 1 ) ‖ Σ − 1 2 . \displaystyle\min_{\Delta{\bm{x}}_{1}}\frac{1}{2}\|\Delta{\bm{x}}_{1}\|_{R}^{2}+\frac{1}{2}\|{\bm{y}}-A(\hat{{\bm{x}}}_{1}+\Delta{\bm{x}}_{1})\|_{\Sigma^{-1}}^{2}. (6)

[54] p: This convex quadratic problem has a unique closed-form solution Δ ​ 𝒙 1 ⋆ \Delta{\bm{x}}_{1}^{\star} given by

[55] table: Δ ​ 𝒙 1 ⋆ = R − 1 ​ A ⊤ ​ ( A ​ R − 1 ​ A ⊤ + Σ ) − 1 ​ ( 𝒚 − A ​ 𝒙 ^ 1 ) . \displaystyle\Delta{\bm{x}}_{1}^{\star}=R^{-1}A^{\top}\bigl(AR^{-1}A^{\top}+\Sigma\bigr)^{-1}\bigl({\bm{y}}-A\hat{{\bm{x}}}_{1}\bigr). (7)

[56] p: Applying this to 𝒙 ^ 1 \hat{{\bm{x}}}_{1} yields the corrected clean endpoint

[57] table: 𝒙 ^ 1 ⋆ = 𝒙 ^ 1 + Δ ​ 𝒙 1 ⋆ . \displaystyle\hat{{\bm{x}}}_{1}^{\star}\;=\;\hat{{\bm{x}}}_{1}+\Delta{\bm{x}}_{1}^{\star}. (8)

[58] p: We then compute the next state 𝒙 t + Δ ​ t {\bm{x}}_{t+\Delta t} by adapting the stochastic recomposition step from the FlowDPS sampler [ 23 ] . This step combines our corrected clean endpoint 𝒙 ^ 1 ⋆ \hat{{\bm{x}}}_{1}^{\star} with a mixed version of the original noise 𝒙 0 {\bm{x}}_{0} :

[59] table: 𝒙 ~ 0 \displaystyle\tilde{{\bm{x}}}_{0} = 1 − η t ​ 𝒙 0 + η t ​ ϵ , ϵ ∼ 𝒩 ⁡ ( 0 , I ) \displaystyle=\sqrt{1-\eta_{t}}{\bm{x}}_{0}+\sqrt{\eta_{t}}{\bm{\epsilon}},\quad{\bm{\epsilon}}\sim\mathcal{N}(0,I) (9) 𝒙 t + Δ ​ t \displaystyle{\bm{x}}_{t+\Delta t} = α t + Δ ​ t ​ 𝒙 ^ 1 ⋆ + σ t + Δ ​ t ​ 𝒙 ~ 0 , \displaystyle=\alpha_{t+\Delta t}\hat{{\bm{x}}}_{1}^{\star}+\sigma_{t+\Delta t}\tilde{{\bm{x}}}_{0}, (10)

[60] p: where η t \eta_{t} is a noise-mixing parameter, and the path coefficients are defined as α t + Δ ​ t = t + Δ ​ t \alpha_{t+\Delta t}=t+\Delta t and σ t + Δ ​ t = 1 − ( t + Δ ​ t ) \sigma_{t+\Delta t}=1-(t+\Delta t) .

[61] h5: Kinematics-aware Metric

[62] p: The choice of metric R R determines how we measure the size of a correction Δ ​ 𝒙 1 \Delta{\bm{x}}_{1} in the clean motion space. With the Euclidean metric ( R = I R=I ), all coordinates are weighted equally, so slight changes to a few joints may appear “small” in terms of ℓ 2 \ell_{2} norm even if it breaks kinematic coherence. We instead define smallness by coherence along the kinematic tree. The full metric R R for a motion 𝒙 ∈ ℝ d {\bm{x}}\in\mathbb{R}^{d} is defined as

[63] table: R = w kin ​ ( I 3 ⊗ I N ⊗ L kin ) + λ ​ I d , \displaystyle R=w_{\mathrm{kin}}(I_{3}\otimes I_{N}\otimes L_{\mathrm{kin}})+\lambda I_{d}, (11)

[64] p: where L kin ∈ ℝ J × J L_{\mathrm{kin}}\in\mathbb{R}^{J\times J} is the standard unnormalized graph Laplacian of the skeletal topology. It is constructed from the skeleton’s adjacency matrix A kin A_{\text{kin}} (where ( A kin ) j 1 ​ j 2 = 1 (A_{\text{kin}})_{j_{1}j_{2}}=1 if joint j 1 j_{1} and j 2 j_{2} are connected) as L kin = D kin − A kin L_{\text{kin}}=D_{\text{kin}}-A_{\text{kin}} , with the diagonal degree matrix D kin = diag ​ ( A kin ​ 𝟏 ) D_{\text{kin}}=\text{diag}(A_{\text{kin}}\mathbf{1}) . I k I_{k} is the k × k k\times k identity matrix, w kin w_{\mathrm{kin}} is a scalar weight for the kinematic term, and λ > 0 \lambda>0 is a weight for the identity term, which ensures R R is strictly positive definite and invertible. This metric is applied independently to each of the x , y , and ​ z x,y,\text{and }z spatial dimensions via the I 3 I_{3} term.

[65] p: This metric makes the intended measurement of “small” explicit (i) discrepancies across adjacent joints are strongly penalized by the kinematic term w kin ​ L kin w_{\mathrm{kin}}L_{\mathrm{kin}} , while joints that are not directly connected in the kinematic tree incur little coupling, reflecting the skeletal topology. (ii) The identity term λ ​ I \lambda I adds a baseline ℓ 2 \ell_{2} penalty to directions, which are per-frame global translations that are not penalized by the kinematic component. This penalty regularizes these otherwise unconstrained modes and ensures that the full metric R R is strictly positive definite.

[66] h3: 4.3 Spatial Control with ProjFlow

[67] p: We illustrate ProjFlow in practice through two representative spatial control applications: motion inpainting and 2D-to-3D lifting. Other extensions, such as motion loop closure and relative body part control shown in Fig. 1 , are formulated in the supplementary material.

[68] h4: 4.3.1 Application I: Motion Inpainting via Masked Pseudo-Observations

[69] figure: Figure 3 : Pseudo-observations for motion inpainting. Sparse observations are interpolated to guide intermediate frames. This guidance is controlled by two mechanisms: Dynamic Masking activates a time-scheduled neighborhood, and Adaptive Variance treats original observations as hard constraints and the interpolated guides as soft constraints.

[70] p: Plain Masking. We cast inpainting as recovering the full motion vector 𝒙 ∈ ℝ d {\bm{x}}\in\mathbb{R}^{d} from sparse hard observations, such as keyframe joint locations provided by users. Let M obs ∈ { 0 , 1 } d × d M_{\mathrm{obs}}\in\{0,1\}^{d\times d} be a diagonal mask selecting observed coordinates, and 𝒚 obs ∈ ℝ d {\bm{y}}_{\mathrm{obs}}\in\mathbb{R}^{d} store their values (zeros elsewhere). The hard‑constraint model is

[71] table: 𝒚 obs = M obs ​ 𝒙 . \displaystyle{\bm{y}}_{\mathrm{obs}}\;=\;M_{\mathrm{obs}}{\bm{x}}. (12)

[72] p: Time‑varying Pseudo‑observations. When these hard observations are sparse, the model provides insufficient guidance. We therefore introduce “soft” pseudo-observations 𝒚 src {\bm{y}}_{\mathrm{src}} , created via per-joint linear interpolation, to provide denser guidance. However, these pseudo-observations from linear interpolation are not always reliable. We want the variance to be high (i.e., trust is low) in two cases (i) As sampling progresses ( t → 1 t\to 1 ), we trust the model’s own prediction 𝒙 ^ 1 \hat{{\bm{x}}}_{1} more. (ii) Where motion curvature is high, linear interpolation is a poor estimate.

[73] p: We combine these soft guides with the hard observations 𝒚 obs {\bm{y}}_{\mathrm{obs}} to formulate a time-varying linear inverse problem at each sampling step t t

[74] table: 𝒚 ( t ) = M ( t ) ​ 𝒙 + ϵ ( t ) , ϵ ( t ) ∼ 𝒩 ⁡ ( 0 , Σ ( t ) ) , \displaystyle{\bm{y}}^{(t)}\;=\;M^{(t)}{\bm{x}}+{\bm{\epsilon}}^{(t)},\qquad{\bm{\epsilon}}^{(t)}\sim\mathcal{N}\!\big(0,\Sigma^{(t)}\big), (13)

[75] p: where M aug ( t ) M_{\mathrm{aug}}^{(t)} is a diagonal matrix activating pseudo-observations within a temporal neighbourhood of hard constraints, but explicitly excluding the hard constraints themselves. The combined mask is the union of these disjoint sets, M ( t ) = M obs + M aug ( t ) M^{(t)}=M_{\mathrm{obs}}+M_{\mathrm{aug}}^{(t)} . The target observation is 𝒚 ( t ) = 𝒚 obs + M aug ( t ) ​ 𝒚 src {\bm{y}}^{(t)}={\bm{y}}_{\mathrm{obs}}+M_{\mathrm{aug}}^{(t)}\,{\bm{y}}_{\mathrm{src}} . The diagonal covariance Σ ( t ) = diag ⁡ ( σ 1 2 ​ ( t ) , … , σ d 2 ​ ( t ) ) \Sigma^{(t)}=\mathrm{diag}(\sigma_{1}^{2}(t),\ldots,\sigma_{d}^{2}(t)) assigns an adaptive, non-zero variance σ i 2 ​ ( t ) > 0 \sigma_{i}^{2}(t)>0 to the active pseudo-observations based on their reliability. The actual observations are treated as exact linear equalities.

[76] p: Dynamic Masking. The temporal neighbourhood of pseudo-observations (Fig. 3 , Dynamic Masking) shrinks linearly in time. This mechanism gradually phases out the soft pseudo-observations, leaving only the hard constraints active as t → 1 t\to 1 . We define this shrinking radius ℓ ⁡ ( t ) \ell(t) as

[77] table: ℓ ⁡ ( t ) = ( 1 − t ) ​ ℓ max + t ​ ℓ min . \displaystyle\ell(t)\;=\;(1-t)\,\ell_{\max}+t\,\ell_{\min}. (14)

[78] p: A frame’s pseudo-observations are activated only if the temporal distance to its nearest hard observation is less than this radius ℓ ⁡ ( t ) \ell(t) .

[79] p: Adaptive Variance. We control the reliability of the pseudo-observations by setting their variance σ i 2 ​ ( t ) \sigma_{i}^{2}(t) (Fig. 3 , Adaptive Variance). We model the trust level with a frame-wise score π ~ n ( t ) \tilde{\pi}_{n}^{(t)}

[80] table: π ~ n ( t ) = τ ⁡ ( t ) ​ c 0 1 + λ s ​ ( s n ​ ( 𝒙 ^ 1 ) / s med ) p \displaystyle\tilde{\pi}_{n}^{(t)}\;=\;\tau(t)\,\frac{c_{0}}{1+\lambda_{s}\,(s_{n}(\hat{{\bm{x}}}_{1})/s_{\text{med}})^{p}} (15)

[81] p: where c 0 c_{0} , λ s \lambda_{s} , and p p are hyperparameters controlling the adaptive strength. This score combines a global time-decay term,

[82] table: τ ⁡ ( t ) = τ min + ( 1 − τ min ) ​ ( 1 − t ) , \displaystyle\tau(t)\;=\;\tau_{\min}+(1-\tau_{\min})(1-t), (16)

[83] p: where τ min \tau_{\min} is a hyperparameter, with a local curvature penalty s n ​ ( 𝒙 ^ 1 ) s_{n}(\hat{{\bm{x}}}_{1}) , defined as

[84] table: s n ​ ( 𝒙 ^ 1 ) = ‖ ( 𝒙 ^ 1 ) n + 1 − 2 ​ ( 𝒙 ^ 1 ) n + ( 𝒙 ^ 1 ) n − 1 ‖ R . \displaystyle s_{n}(\hat{{\bm{x}}}_{1})\;=\;\|(\hat{{\bm{x}}}_{1})_{n+1}-2(\hat{{\bm{x}}}_{1})_{n}+(\hat{{\bm{x}}}_{1})_{n-1}\|_{R}. (17)

[85] p: Here, s med s_{\text{med}} is the median curvature s n ​ ( 𝒙 ^ 1 ) s_{n}(\hat{{\bm{x}}}_{1}) across the sequence, used for robust normalization. As time t t increases or curvature s n s_{n} increases, the trust score π ~ n ( t ) \tilde{\pi}_{n}^{(t)} decreases. We clip this score to get a frame-level base target π n ( t ) = clip ⁡ ( π ~ n ( t ) , π min , π max ) \pi_{n}^{(t)}=\mathrm{clip}\!\big(\,\tilde{\pi}_{n}^{(t)},\ \pi_{\min},\ \pi_{\max}\,\big) . This base score is then modulated per-joint based on the properties of the kinematic metric to yield the final per-element score π i \pi_{i} . This π i \pi_{i} is used to compute the variance σ i 2 ​ ( t ) \sigma_{i}^{2}(t) for the active pseudo-observation via the relation π i = r i / ( r i + σ i 2 ​ ( t ) ) \pi_{i}=r_{i}/(r_{i}+\sigma_{i}^{2}(t)) . Solving for the variance gives

[86] table: σ i 2 ​ ( t ) = r i ​ 1 − π i π i \displaystyle\sigma_{i}^{2}(t)\;=\;r_{i}\frac{1-\pi_{i}}{\pi_{i}} (18)

[87] p: where r i = [ diag ⁡ ( R − 1 ) ] i r_{i}=[\mathrm{diag}(R^{-1})]_{i} is the i i -th diagonal element of the inverse kinematic metric. Hard observations always maintain zero variance ( σ i 2 = 0 \sigma_{i}^{2}=0 ).

[88] figure: Figure 4 : Text-conditioned pelvis-trajectory control. Given the prompt “ a person runs forward in an S-shaped path ” and a pelvis control signal, we compare OmniControl [ 63 ] , MaskControl [ 45 ] , and ProjFlow (ours). The rendered motions and the trajectory plots both visualize the generated pelvis trajectory ( orange ) overlaid on the target control signal ( gray dotted line ).

[89] h4: 4.3.2 Application II: 2D-to-3D Lifting via Linear Projection Measurements

[90] p: The 2D-to-3D motion lifting task can also be expressed as a linear inverse problem. In this setting, we assume noise-free hard constraints, so the model simplifies to 𝒚 = A ​ 𝒙 {\bm{y}}=A\,{\bm{x}} . The operator A A maps the vectorized 3D motion sequence 𝒙 {\bm{x}} to stacked 2D joint coordinates. This operator is constructed in two steps. First, we define a full projection operator A full A_{\mathrm{full}} that maps all 3D joints at all frames to 2D. It does this by stacking the standard linear orthographic projection,

[91] table: 𝒚 n , j = s ​ P ​ R cam ​ 𝒙 n , j , \displaystyle{\bm{y}}_{n,j}=sPR_{\text{cam}}{\bm{x}}_{n,j}, (19)

[92] p: for every frame n n and joint j j , where s s is a fixed scale factor, P = [ 1 ​ 0 ​ 0 ; 0 ​ 1 ​ 0 ] P=[\,1~0~0;~0~1~0\,] is the orthographic projection matrix, and R cam ∈ SO ⁡ ( 3 ) R_{\text{cam}}\!\in\!\mathrm{SO}(3) is the camera rotation. Both s s and R cam R_{\text{cam}} are assumed to be known for each sequence.

[93] p: Second, we define a binary selection operator M M that filters the rows of A full A_{\mathrm{full}} to match the user’s specific inputs (e.g., all joints at frame 0 and a subset of joints for n > 0 n>0 ). M M is constructed to select only these corresponding rows. The final measurement operator A A is therefore defined as

[94] table: A = M ​ A full . \displaystyle A=M\,A_{\mathrm{full}}. (20)

[95] h2: 5 Experiments

[96] p: In this section, we evaluate the performance of ProjFlow, comparing it to previous task-specific/zero-shot methods.

[97] h3: 5.1 Experimental Setup

[98] p: Datasets. We experiment on the popular HumanML3D [ 15 ] dataset which contains 14,646 text-annotated human motion sequences from AMASS [ 37 ] and HumanAct12 [ 16 ] datasets.

[99] p: Evaluation Protocol. We adopt the pretrained ACMDM-S-PS22 [ 39 ] as our base flow-matching model for all experiments and primarily follow the protocol of Meng et al. [40] . For spatial control experiments, we follow the OmniControl [ 63 ] evaluation protocol, which varies the density of control signals across five settings (1, 2, 5, 49, and 196 keyframes), and report the mean of each control metric across these densities to assess robustness to sparsity.

[100] p: For the 2D-to-3D task, we follow the Sketch2Anim [ 68 ] protocol, which defines camera parameters including pitch ∈ [ 0 ∘ , 30 ∘ ] \text{pitch}\in[0^{\circ},30^{\circ}] , yaw ∈ [ − 45 ∘ , 45 ∘ ] \text{yaw}\in[-45^{\circ},45^{\circ}] , roll = 0 ∘ \text{roll}=0^{\circ} , and s ∈ [ 0.8 , 1.2 ] s\in[0.8,1.2] . We evaluate under this known orthographic camera at inference time.

[101] p: Evaluation Metrics. To assess generation quality and text alignment, we report FID for distribution similarity, R-Precision (Top-1/2/3) and Matching Score for semantic retrieval accuracy between motion and text embeddings, Diversity for motion diversity. For spatial control tasks, we evaluate accuracy using Trajectory Error , Location Error , and Average Error , which measure deviations from target keyframes at trajectory, keyframe, and mean distance levels, respectively. Physical plausibility is assessed via the Foot Skating Ratio .

[102] p: For the 2D-to-3D reconstruction task, in addition to the above metrics, we report MPJPE‑2D and Avg. Err.‑2D . These metrics evaluate constraint satisfaction by projecting the generated 3D motion back into 2D and quantifying the mean error against the target 2D joint coordinates, following the protocol of Sketch2Anim [ 68 ] .

[103] figure: Table 1 : Quantitative text-conditioned motion generation with spatial control signals and upper-body editing on HumanML3D [ 15 ] . In the first section, methods are trained and evaluated solely on pelvis controls. In the middle section, methods are trained on all joints and evaluated separately on each controlled joint. Only average results are reported for brevity. We include details in the supplementary material. The last section presents upper-body editing results. bold face / underline indicates the best/2 nd results. Controlling Joint Methods Zero-shot? FID ↓ \downarrow R-Precision Diversity → \rightarrow Foot Skating Traj. err. ↓ \downarrow Loc. err. ↓ \downarrow Avg. err. ↓ \downarrow Top 3 Ratio. ↓ \downarrow GT - 0.000 0.000 0.795 0.795 10.455 10.455 - 0.000 0.000 0.000 0.000 0.000 0.000 Pelvis MDM [ 57 ] ✓ 1.792 1.792 0.673 0.673 9.131 9.131 0.1019 0.1019 0.4022 0.4022 0.3076 0.3076 0.5959 0.5959 PriorMDM [ 51 ] ✗ 0.393 0.393 0.707 0.707 9.847 9.847 0.0897 0.0897 0.3457 0.3457 0.2132 0.2132 0.4417 0.4417 GMD [ 21 ] ✓ 0.238 0.238 0.763 0.763 10.011 10.011 0.1009 0.1009 0.0931 0.0931 0.0321 0.0321 0.1439 0.1439 OmniControl [ 63 ] ✗ 0.081 0.081 0.789 0.789 10.323 10.323 0.0547 ¯ \underline{0.0547} 0.0387 0.0387 0.0096 0.0096 0.0338 0.0338 MotionLCM V2+CtrlNet [ 9 ] ✗ 3.978 3.978 0.738 0.738 9.249 9.249 0.0901 0.0901 0.1080 0.1080 0.0581 0.0581 0.1386 0.1386 MaskControl [ 45 ] ✗ 0.066 \mathbf{0.066} 0.799 0.799 10.474 \mathbf{10.474} 0.0543 \mathbf{0.0543} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0093 0.0093 ACMDM - S - PS22+CtrlNet [ 39 ] ✗ 0.067 ¯ \underline{0.067} 0.805 \mathbf{0.805} 10.481 ¯ \underline{10.481} 0.0591 0.0591 0.0075 0.0075 0.0010 0.0010 0.0100 0.0100 ACMDM - S - PS22+DNO [ 20 ] ✓ 0.151 0.151 0.802 ¯ \underline{0.802} − - 0.0610 0.0610 0.0027 ¯ \underline{0.0027} 0.0002 ¯ \underline{0.0002} 0.0089 ¯ \underline{0.0089} ACMDM - S - PS22+ProjFlow ✓ 0.107 0.107 0.784 0.784 10.644 10.644 0.0629 0.0629 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} All Joints (Average) OmniControl [ 63 ] ✗ 0.126 0.126 0.792 0.792 10.276 ¯ \underline{10.276} 0.0608 0.0608 0.0617 0.0617 0.0107 0.0107 0.0404 0.0404 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.504 4.504 0.715 0.715 9.230 9.230 0.1119 0.2740 0.2740 0.1315 0.1315 0.2464 0.2464 MaskControl [ 45 ] ✗ 0.095 ¯ \underline{0.095} 0.795 0.795 10.159 10.159 0.0545 \mathbf{0.0545} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0065 ¯ \underline{0.0065} ACMDM - S - PS22+CtrlNet [ 39 ] ✗ 0.070 \mathbf{0.070} 0.803 \mathbf{0.803} 10.526 \mathbf{10.526} 0.0596 ¯ \underline{0.0596} 0.0117 0.0117 0.0019 0.0019 0.0197 0.0197 ACMDM - S - PS22+DNO [ 20 ] ✓ 0.147 0.147 0.800 ¯ \underline{0.800} − - 0.0600 0.0600 0.0034 ¯ \underline{0.0034} 0.0003 ¯ \underline{0.0003} 0.0121 0.0121 ACMDM - S - PS22+ProjFlow ✓ 0.097 0.097 0.779 0.779 10.651 10.651 0.0603 0.0603 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Methods Zero-shot? FID ↓ \downarrow R-Precision R-Precision R-Precision Matching ↓ \downarrow Diversity → \rightarrow − - Top 1 Top 2 Top 3 Upper-Body Edit MDM [ 57 ] ✓ 1.918 1.918 0.359 0.359 0.556 0.556 0.654 0.654 4.793 4.793 9.210 9.210 − - OmniControl [ 63 ] ✗ 0.909 0.909 0.428 0.428 0.614 0.614 0.722 0.722 3.694 3.694 10.207 10.207 − - MotionLCM V2+CtrlNet [ 9 ] ✗ 3.922 3.922 0.404 0.404 0.592 0.592 0.692 0.692 5.610 5.610 9.309 9.309 − - MaskControl [ 45 ] ✗ 0.066 \mathbf{0.066} 0.501 ¯ \underline{0.501} 0.695 ¯ \underline{0.695} 0.794 ¯ \underline{0.794} 3.227 ¯ \underline{3.227} 10.159 10.159 − - ACMDM - S - PS22+CtrlNet [ 39 ] ✗ 0.076 ¯ \underline{0.076} 0.532 \mathbf{0.532} 0.719 \mathbf{0.719} 0.820 \mathbf{0.820} 3.098 \mathbf{3.098} 10.586 ¯ \underline{10.586} − - ACMDM - S - PS22+ProjFlow ✓ 0.087 0.087 0.501 ¯ \underline{0.501} 0.690 0.690 0.787 0.787 3.319 3.319 10.571 \mathbf{10.571} − -

[104] h3: 5.2 Results

[105] h4: 5.2.1 Motion Inpainting with Trajectory Control

[106] p: Quantitative Performance. ProjFlow is the only zero-shot method that achieves exact constraint satisfaction ( 0.0000 0.0000 on trajectory/location/average errors) while also attaining the best realism among zero-shot baselines. As shown in Table 1 , its FID is lower than DNO(ACMDM-S-PS22+DNO) [ 20 ] for both pelvis control and all joints, which indicates that ProjFlow can eliminate the small residual violations that remain for guidance/noise-optimization methods.

[107] p: Compared to models that require additional training, as shown in Table 1 , ProjFlow stays in a similar realism band while remaining training-free and achieving exact constraint satisfaction. For example, MaskControl [ 45 ] reaches a lower FID but still leaves a non-zero average error ( 0.0093 0.0093 ), whereas ProjFlow maintains all control errors at 0.0000 0.0000 . The same tendency is observed in other training-based controllers such as OmniControl [ 63 ] . Even when the same base model is additionally trained with a ControlNet branch (ACMDM-S-PS22+CtrlNet), the constraints are still not fully satisfied, despite a slightly improved FID of 0.067. In contrast, ProjFlow achieves exact constraint satisfaction without any retraining.

[108] p: Qualitative Analysis. Fig. 4 compares the generated motions from OmniControl [ 63 ] , MaskControl [ 45 ] , and ProjFlow. OmniControl [ 63 ] captures the overall S-shaped tendency of the target path but deviates significantly along the curve, especially near the bends. MaskControl [ 45 ] uses a ControlNet-style branch and additionally performs inference-time optimization, which further reduces this deviation. However, close inspection of the overlaid trajectories still reveals slight mismatches between the generated and target paths. By contrast, ProjFlow aligns the generated pelvis trajectory with the target markers essentially exactly across the entire S-shaped path while preserving natural full-body motion.

[109] figure: Figure 5 : 2D-to-3D hand-trajectory lifting with text conditioning. The input condition includes the text prompt “ a person draws a heart with their hand while walking ,” an initial 2D keypose, and a left-wrist 2D trajectory shaped like a heart. Sketch2Anim [ 68 ] fails to reproduce the heart path precisely, the shape collapses, and the subject does not exhibit walking motion. In contrast, ProjFlow follows the heart-shaped wrist trajectory accurately while maintaining a natural walking motion throughout the sequence.

[110] figure: Table 2 : Quantitative analysis of ProjFlow and three baseline models proposed in Sketch2Anim [ 68 ] on the HumanML3D [ 15 ] . Evaluation metrics on motion realism, control accuracy, and text-motion match are presented. Following OmniControl [ 63 ] , we report both the average error of all joints (Average) and their random combination (Cross). bold face / underline indicates the best/2 nd results. Condition Method Realism Control Accuracy Text-Motion Matching FID ↓ \downarrow Foot Skating ↓ \downarrow MPJPE-2D ↓ \downarrow MPJPE-3D ↓ \downarrow Avg. Err.-2D ↓ \downarrow Avg. Err.-3D ↓ \downarrow Matching ↓ \downarrow R-precision (Top-3) ↑ \uparrow Average Motion Retrieval 0.690 0.064 0.057 0.076 0.290 0.410 4.060 0.640 Lift-and-Control 0.979 0.089 0.054 0.071 0.261 0.340 3.297 0.752 Direct 2D-to-Motion 2.553 0.112 0.040 0.055 0.193 0.275 3.723 0.687 Sketch2Anim [ 68 ] 0.525 0.103 0.036 0.048 0.087 0.134 3.077 0.802 ACMDM-S-PS22+ProjFlow 0.349 0.146 0.000 0.042 0.000 0.331 3.363 0.748 Cross Motion Retrieval 0.103 0.067 0.055 0.073 0.307 0.423 3.405 0.724 Lift-and-Control 0.738 0.101 0.051 0.067 0.209 0.283 3.135 0.778 Direct 2D-to-Motion 2.310 0.123 0.040 0.056 0.189 0.266 3.606 0.709 Sketch2Anim [ 68 ] 0.577 0.102 0.033 0.046 0.079 0.132 3.042 0.796 ACMDM-S-PS22+ProjFlow 0.168 0.139 0.000 0.037 0.000 0.298 3.259 0.764

[111] h4: 5.2.2 2D-to-3D Reconstruction

[112] p: Quantitative Performance. As shown in Table 2 , ProjFlow achieves superior motion naturalness, attaining a lower FID than the state-of-the-art method Sketch2Anim [ 68 ] under both Average and Cross evaluation protocols. For constraint satisfaction, ProjFlow enforces the 2D constraints exactly to the numerical precision (MPJPE-2D = 0.000 =\mathbf{0.000} ) while Sketch2Anim [ 68 ] still exhibits residual reprojection errors.

[113] p: Qualitative Analysis. Fig. 5 shows a qualitative example of the 2D-to-3D lifting task. The goal is to generate a 3D motion that follows the given 2D heart-shaped wrist trajectory and the given initial 2D keypose, while simultaneously ”walking” as specified by the text prompt.

[114] p: ProjFlow succeeds in following the 2D heart trajectory exactly at every frame while keeping the other joints engaged in a natural walking motion. The legs and torso continue to produce smooth, coordinated gait cycles as the left wrist draws the heart shape in the image plane. In contrast, Sketch2Anim [ 68 ] fails to preserve the heart shape, and the trajectory collapses into a distorted loop. The character also primarily remains in place, only moving the arm without translating forward, indicating that the intended instruction to walk is not realized.

[115] h4: 5.2.3 Ablation Study

[116] p: We analyze the contribution of ProjFlow’s three key components on the motion inpainting task in Table 3 . First, replacing our kinematics-aware metric with a standard Euclidean metric severely degrades motion realism, causing a significant degradation in FID. This confirms that propagating corrections coherently along the skeleton is critical. Second, removing the stochastic recomposition step ( η t = 0 \eta_{t}=0 ) and deterministically recomposing the state also drastically harms quality and diversity. This highlights the importance of noise mixing for staying on the learned motion manifold. Third, for the inpainting task, reverting to a ”Plain masking” approach without our pseudo-observation significantly worsens realism. These results validate that while all variants maintain exact constraint satisfaction, all three proposed components are essential for generating natural and realistic motion.

[117] figure: Table 3: Ablation studies of ProjFlow. Variant FID ↓ \downarrow R-Prec. Div. → \rightarrow Foot ↓ \downarrow Traj. ↓ \downarrow Loc. ↓ \downarrow Avg. ↓ \downarrow ProjFlow (Full) 0.097 0.779 10.651 0.0603 0.0000 0.0000 0.0000 Euclid. ( R = I R{=}I ) 1.152 0.740 10.107 0.0595 0.0000 0.0000 0.0000 No noise ( η t = 0 \eta_{t}{=}0 ) 3.429 0.707 9.307 0.0863 0.0000 0.0000 0.0000 Plain masking 0.880 0.748 10.187 0.0632 0.0000 0.0000 0.0000

[118] h2: 6 Limitations

[119] p: While ProjFlow offers exact satisfaction of linear spatial constraints in a training-free manner, it is fundamentally limited to constraints that can be formulated as linear inverse problems. Our framework, in its current form, cannot natively handle more complex non-linear constraints. Examples of such constraints include inequalities such as keeping a joint above a certain plane. Extending the closed-form projection to these more expressive, non-linear scenarios is a challenging but important direction for future work.

[120] h2: 7 Conclusion

[121] p: In this paper, we presented ProjFlow , a zero-shot projection sampler for flow-matching models that achieves exact spatial motion control. Our method unifies diverse animation tasks, such as trajectory following and 2D-to-3D lifting, by formulating them as linear inverse problems. The sampler projects the clean motion estimate onto the linear constraint set at each ODE step. This projection employs a novel kinematics-aware metric that respects skeletal topology to maintain motion naturalness. ProjFlow successfully enforces hard constraints exactly without requiring any task-specific retraining or iterative optimization. Experiments on motion inpainting and 2D-to-3D reconstruction show that our framework matches the realism of training-based methods while guaranteeing exact constraint satisfaction. ProjFlow provides a practical route for interactive and precise motion authoring.

[122] h2: References

[123] p: Supplementary Material

[124] p: This supplementary material is organized as follows:

[125] p: Section A : Analytical view of ProjFlow.

[126] p: Section B : Additional method details.

[127] p: Section C : Implementation details.

[128] p: Section D : Additional quantitative results.

[129] p: Section E : Additional qualitative results.

[130] h2: Appendix A Analytical View of ProjFlow

[131] p: Using the notation in Table 4 , we provide an analytical interpretation of the ProjFlow update, including its relation to DDNM and a MAP view. In what follows, “PSD” and “PD” denote positive semidefinite and positive definite matrices, respectively.

[132] figure: Table 4: Notation used in the supplementary derivations. Symbol Type / shape Note A A ℝ m × d \mathbb{R}^{m\times d} linear operator 𝒚 {\bm{y}} ℝ m \mathbb{R}^{m} measurements 𝒙 1 {\bm{x}}_{1} ℝ d \mathbb{R}^{d} clean motion endpoint 𝒙 ^ 1 \hat{{\bm{x}}}_{1} ℝ d \mathbb{R}^{d} estimate of 𝒙 1 {\bm{x}}_{1} Σ \Sigma ℝ m × m \mathbb{R}^{m\times m} PSD covariance R R ℝ d × d \mathbb{R}^{d\times d} PD metric / precision

[133] h3: A.1 Recovery of DDNM under Euclidean Metric and Noiseless Observation

[134] p: DDNM [ 60 ] solves the linear inverse problem y = A ​ 𝒙 y=A{\bm{x}} by decomposing ℝ d \mathbb{R}^{d} into the range and null space of A A . Given a clean-endpoint estimate 𝒙 ^ 1 \hat{{\bm{x}}}_{1} , it keeps the range-space component consistent with the measurements and fills the null space with 𝒙 ^ 1 \hat{{\bm{x}}}_{1} :

[135] table: 𝒙 ^ 1 ⋆ = A † ​ 𝒚 + ( I − A † ​ A ) ​ 𝒙 ^ 1 , \displaystyle\hat{{\bm{x}}}_{1}^{\star}=A^{\dagger}{\bm{y}}+(I-A^{\dagger}A)\hat{{\bm{x}}}_{1}, (21)

[136] p: where A † A^{\dagger} is the Moore–Penrose pseudoinverse of A A .

[137] p: ProjFlow, in contrast, updates the clean-endpoint estimate via

[138] table: 𝒙 ^ 1 ⋆ = 𝒙 ^ 1 + R − 1 ​ A ⊤ ​ ( A ​ R − 1 ​ A ⊤ + Σ ) − 1 ​ ( 𝒚 − A ​ 𝒙 ^ 1 ) . \displaystyle\hat{{\bm{x}}}_{1}^{\star}=\hat{{\bm{x}}}_{1}+R^{-1}A^{\top}\bigl(AR^{-1}A^{\top}+\Sigma\bigr)^{-1}\bigl({\bm{y}}-A\hat{{\bm{x}}}_{1}\bigr). (22)

[139] p: Specializing to the Euclidean metric R = I R=I and the noise-free limit Σ → 0 \Sigma\to 0 , and assuming that A A has full row rank so that A ​ A ⊤ AA^{\top} is invertible, we obtain

[140] table: 𝒙 ^ 1 ⋆ \displaystyle\hat{{\bm{x}}}_{1}^{\star} = 𝒙 ^ 1 + A ⊤ ​ ( A ​ A ⊤ ) − 1 ​ ( 𝒚 − A ​ 𝒙 ^ 1 ) \displaystyle=\hat{{\bm{x}}}_{1}+A^{\top}\bigl(AA^{\top}\bigr)^{-1}\bigl({\bm{y}}-A\hat{{\bm{x}}}_{1}\bigr) (23) = 𝒙 ^ 1 + A † ​ 𝒚 − A † ​ A ​ 𝒙 ^ 1 \displaystyle=\hat{{\bm{x}}}_{1}+A^{\dagger}{\bm{y}}-A^{\dagger}A\hat{{\bm{x}}}_{1} (24) = A † ​ 𝒚 + ( I − A † ​ A ) ​ 𝒙 ^ 1 , \displaystyle=A^{\dagger}{\bm{y}}+\bigl(I-A^{\dagger}A\bigr)\hat{{\bm{x}}}_{1}, (25)

[141] p: which coincides exactly with the DDNM update above. Thus, DDNM is recovered as a special case of ProjFlow in the Euclidean, noiseless setting.

[142] h3: A.2 ProjFlow as MAP Estimation

[143] p: ProjFlow’s projection step can also be interpreted as computing a maximum-a-posteriori (MAP) estimate in a linear–Gaussian model. We treat the clean-endpoint estimate 𝒙 ^ 1 \hat{{\bm{x}}}_{1} from Tweedie’s formula as the mean of a Gaussian prior

[144] table: p ⁡ ( 𝒙 1 ) = 𝒩 ⁡ ( 𝒙 1 ∣ 𝒙 ^ 1 , R − 1 ) , \displaystyle p({\bm{x}}_{1})\;=\;\mathcal{N}\!\bigl({\bm{x}}_{1}\mid\hat{{\bm{x}}}_{1},\;R^{-1}\bigr), (26)

[145] p: where R ≻ 0 R\succ 0 is the precision matrix and R − 1 R^{-1} is the corresponding covariance.

[146] p: For the Euclidean metric R = I R=I , this prior is an isotropic Gaussian centered at 𝒙 ^ 1 \hat{{\bm{x}}}_{1} , penalizing all directions equally. With the kinematics-aware metric R R , the structure is instead governed by the skeletal Laplacian L kin L_{\text{kin}} : directions that create large differences between adjacent joints (skeletally incoherent motion) have small variance, while coordinated joint motions have larger variance. Geometrically, this yields a highly anisotropic ellipsoidal prior that favors kinematically coherent corrections.

[147] p: The linear observation model is

[148] table: 𝒚 \displaystyle{\bm{y}} = A ​ 𝒙 1 + ϵ , ϵ ∼ 𝒩 ⁡ ( 𝟎 , Σ ) \displaystyle=A{\bm{x}}_{1}+{\bm{\epsilon}},\qquad{\bm{\epsilon}}\sim\mathcal{N}(\mathbf{0},\,\Sigma) (27) ⟺ p ⁡ ( 𝒚 ∣ 𝒙 1 ) = 𝒩 ⁡ ( 𝒚 ∣ A ​ 𝒙 1 , Σ ) . \displaystyle\Longleftrightarrow\;p({\bm{y}}\mid{\bm{x}}_{1})=\mathcal{N}\!\bigl({\bm{y}}\mid A{\bm{x}}_{1},\,\Sigma\bigr). (28)

[149] p: Combining this likelihood with the prior yields a Gaussian posterior

[150] table: p ⁡ ( 𝒙 1 ∣ 𝒚 ) ∝ exp ⁡ ( − 1 2 ​ ‖ 𝒙 1 − 𝒙 ^ 1 ‖ R 2 − 1 2 ​ ‖ 𝒚 − A ​ 𝒙 1 ‖ Σ − 1 2 ) . \displaystyle p({\bm{x}}_{1}\mid{\bm{y}})\;\propto\;\exp\!\Bigl(-\tfrac{1}{2}\|{\bm{x}}_{1}-\hat{{\bm{x}}}_{1}\|_{R}^{2}-\tfrac{1}{2}\|{\bm{y}}-A{\bm{x}}_{1}\|_{\Sigma^{-1}}^{2}\Bigr). (29)

[151] p: The MAP estimate 𝒙 1 MAP {\bm{x}}_{1}^{\text{MAP}} maximizes this posterior, or equivalently minimizes the negative log-posterior:

[152] table: 𝒙 1 MAP \displaystyle{\bm{x}}_{1}^{\text{MAP}} = arg ​ min 𝐱 1 ⁡ ( ‖ 𝐱 1 − 𝐱 ^ 1 ‖ R 2 + ‖ 𝐲 − A ​ 𝐱 1 ‖ Σ − 1 2 ) . \displaystyle=\argmin_{{\bm{x}}_{1}}\Bigl(\|{\bm{x}}_{1}-\hat{{\bm{x}}}_{1}\|_{R}^{2}+\|{\bm{y}}-A{\bm{x}}_{1}\|_{\Sigma^{-1}}^{2}\Bigr). (30)

[153] p: Taking the gradient with respect to 𝒙 1 {\bm{x}}_{1} and setting it to zero gives the normal equations

[154] table: ( R + A ⊤ ​ Σ − 1 ​ A ) ​ 𝒙 1 = R ​ 𝒙 ^ 1 + A ⊤ ​ Σ − 1 ​ 𝒚 , \displaystyle\bigl(R+A^{\top}\Sigma^{-1}A\bigr){\bm{x}}_{1}=R\hat{{\bm{x}}}_{1}+A^{\top}\Sigma^{-1}{\bm{y}}, (31)

[155] p: so that

[156] table: 𝒙 1 MAP \displaystyle{\bm{x}}_{1}^{\text{MAP}} = ( R + A ⊤ ​ Σ − 1 ​ A ) − 1 ​ ( R ​ 𝒙 ^ 1 + A ⊤ ​ Σ − 1 ​ 𝒚 ) \displaystyle=\bigl(R+A^{\top}\Sigma^{-1}A\bigr)^{-1}\bigl(R\hat{{\bm{x}}}_{1}+A^{\top}\Sigma^{-1}{\bm{y}}\bigr) (32) = 𝒙 ^ 1 + ( R + A ⊤ ​ Σ − 1 ​ A ) − 1 ​ A ⊤ ​ Σ − 1 ​ ( 𝒚 − A ​ 𝒙 ^ 1 ) . \displaystyle=\hat{{\bm{x}}}_{1}+\bigl(R+A^{\top}\Sigma^{-1}A\bigr)^{-1}A^{\top}\Sigma^{-1}\bigl({\bm{y}}-A\hat{{\bm{x}}}_{1}\bigr). (33)

[157] p: The second line makes explicit that the MAP solution is obtained by adding a correction to 𝒙 ^ 1 \hat{{\bm{x}}}_{1} . Using standard linear–Gaussian identities, this correction term is equivalent to the ProjFlow update

[158] table: 𝒙 ^ 1 ⋆ = 𝒙 ^ 1 + R − 1 ​ A ⊤ ​ ( A ​ R − 1 ​ A ⊤ + Σ ) − 1 ​ ( 𝒚 − A ​ 𝒙 ^ 1 ) , \displaystyle\hat{{\bm{x}}}_{1}^{\star}=\hat{{\bm{x}}}_{1}+R^{-1}A^{\top}\bigl(AR^{-1}A^{\top}+\Sigma\bigr)^{-1}\bigl({\bm{y}}-A\hat{{\bm{x}}}_{1}\bigr), (34)

[159] p: showing that ProjFlow’s projection step is exactly the MAP estimate of this linear–Gaussian model.

[160] h2: Appendix B Additional Method Details

[161] h3: B.1 Formulating Teaser Applications as Linear Inverse Problems

[162] p: We briefly show how the additional teaser applications in Fig. 1 fit into the unified linear model 𝒚 = A ​ 𝒙 + ϵ {\bm{y}}=A{\bm{x}}+{\bm{\epsilon}} . Trajectory control and 2D-to-3D lifting are already described in the main paper. Here, we detail the relative position constraint and looped motion.

[163] h4: B.1.1 Relative Position Constraint

[164] p: We consider the case where the relative 3D position between two joints remains fixed, e.g., both wrists holding a rigid object. Let 𝒙 n , j a , 𝒙 n , j b ∈ ℝ 3 {\bm{x}}_{n,j_{a}},{\bm{x}}_{n,j_{b}}\in\mathbb{R}^{3} denote the positions of joints j a j_{a} and j b j_{b} at frame n n . To keep their 3D offset fixed, we enforce for each frame

[165] table: 𝒙 n , j a − 𝒙 n , j b = 𝒅 , \displaystyle{\bm{x}}_{n,j_{a}}-{\bm{x}}_{n,j_{b}}={\bm{d}}, (35)

[166] p: where 𝒅 = ( d x , d y , d z ) ⊤ {\bm{d}}=(d_{x},d_{y},d_{z})^{\top} is the desired 3D offset vector. This is linear in the full motion vector 𝒙 {\bm{x}} . Stacking the constraints over all N N frames yields a standard linear inverse problem

[167] table: 𝒚 rel = A rel ​ 𝒙 , \displaystyle{\bm{y}}_{\mathrm{rel}}=A_{\mathrm{rel}}{\bm{x}}, (36)

[168] p: where 𝒚 rel {\bm{y}}_{\mathrm{rel}} is 𝒅 {\bm{d}} repeated N N times, so 𝒚 rel ∈ ℝ 3 ​ N {\bm{y}}_{\mathrm{rel}}\in\mathbb{R}^{3N} . The operator A rel ∈ ℝ 3 ​ N × d A_{\mathrm{rel}}\in\mathbb{R}^{3N\times d} is a sparse matrix that, for each frame, subtracts the coordinates of joint j b j_{b} from those of joint j a j_{a} .

[169] h4: B.1.2 Looped Motion

[170] p: To make a sequence loop seamlessly, we match the start and end poses. Let 𝒙 0 {\bm{x}}_{0} and 𝒙 N − 1 {\bm{x}}_{N-1} be the first and last frames of the motion, respectively. We impose the per-joint constraint

[171] table: 𝒙 0 − 𝒙 N − 1 = 𝟎 , \displaystyle{\bm{x}}_{0}-{\bm{x}}_{N-1}=\mathbf{0}, (37)

[172] p: which is again linear in 𝒙 {\bm{x}} . Stacking these equations over all joints and spatial coordinates gives

[173] table: 𝟎 = A loop ​ 𝒙 , \displaystyle\mathbf{0}=A_{\mathrm{loop}}{\bm{x}}, (38)

[174] p: where A loop ∈ ℝ 3 ​ J × d A_{\mathrm{loop}}\in\mathbb{R}^{3J\times d} computes the difference between the first and last frames. In our framework, this loop-closure operator can simply be concatenated with other linear constraints by stacking its rows into the global observation matrix A A .

[175] h3: B.2 Detailed Formulation of Motion Inpainting

[176] h4: B.2.1 Pseudo-observations: linear interpolation and extrapolation

[177] p: We generate pseudo-observations by per-joint linear interpolation. For each joint, we scan all unobserved frames and, for a given unobserved frame, locate the nearest observed frame before it and the nearest observed frame after it. If both exist, the frame lies between two known points, and we define the pseudo-observation by linear interpolation between these two observations.

[178] p: If the frame lies outside the observed range for that joint (before the first observation or after the last), interpolation is impossible. In this case, we perform extrapolation by copying the value of the single nearest observed frame. If a joint has no observations at all in the sequence, we leave it without pseudo-observations.

[179] h4: B.2.2 Designing the adaptive variance

[180] p: Our inpainting strategy augments sparse hard keyframe constraints with “soft” pseudo-observations from interpolation. The key challenge is to modulate the influence of these soft guides: they should be trusted less (i) at frames with high motion curvature, where interpolation is unreliable, and (ii) late in sampling, when the model’s own prediction 𝒙 ^ 1 \hat{{\bm{x}}}_{1} is more reliable. We encode this behavior in a time-varying observation covariance Σ ( t ) \Sigma^{(t)} . Directly hand-designing variances σ i 2 ​ ( t ) \sigma_{i}^{2}(t) is unintuitive, so we instead design a normalized trust score π i ∈ [ 0 , 1 ] \pi_{i}\in[0,1] and then derive the corresponding σ i 2 ​ ( t ) \sigma_{i}^{2}(t) .

[181] p: To see the relation between π i \pi_{i} and σ i 2 ​ ( t ) \sigma_{i}^{2}(t) , we first consider a simple Euclidean case. For motion inpainting, the observation operator is a diagonal mask matrix A = M ( t ) A=M^{(t)} . Assuming the Euclidean metric R = I R=I , the ProjFlow update becomes

[182] table: 𝒙 ^ 1 ⋆ \displaystyle\hat{{\bm{x}}}_{1}^{\star} = 𝒙 ^ 1 + M ( t ) ​ ( M ( t ) + Σ ( t ) ) − 1 ​ ( 𝒚 ( t ) − A ​ 𝒙 ^ 1 ) \displaystyle=\hat{{\bm{x}}}_{1}+M^{(t)}\bigl(M^{(t)}+\Sigma^{(t)}\bigr)^{-1}\bigl({\bm{y}}^{(t)}-A\hat{{\bm{x}}}_{1}\bigr) (39) = ( I − M ( t ) ​ ( M ( t ) + Σ ( t ) ) − 1 ​ M ( t ) ) ​ 𝒙 ^ 1 \displaystyle=\Bigl(I-M^{(t)}\bigl(M^{(t)}+\Sigma^{(t)}\bigr)^{-1}M^{(t)}\Bigr)\hat{{\bm{x}}}_{1} + M ( t ) ​ ( M ( t ) + Σ ( t ) ) − 1 ​ 𝒚 ( t ) . \displaystyle\quad+M^{(t)}\bigl(M^{(t)}+\Sigma^{(t)}\bigr)^{-1}{\bm{y}}^{(t)}. (40)

[183] p: In the inpainting setting, both M ( t ) M^{(t)} and Σ ( t ) \Sigma^{(t)} are diagonal, so this matrix equation decomposes into independent scalar updates. For an observed coordinate i i (i.e., M i ​ i ( t ) = 1 M^{(t)}_{ii}=1 ) with Σ i ​ i ( t ) = σ i 2 ​ ( t ) \Sigma^{(t)}_{ii}=\sigma_{i}^{2}(t) , we obtain

[184] table: x ^ 1 , i ⋆ \displaystyle\hat{x}_{1,i}^{\star} = ( 1 − 1 1 + σ i 2 ​ ( t ) ) ​ x ^ 1 , i + 1 1 + σ i 2 ​ ( t ) ​ y i \displaystyle=\left(1-\frac{1}{1+\sigma_{i}^{2}(t)}\right)\hat{x}_{1,i}+\frac{1}{1+\sigma_{i}^{2}(t)}y_{i} (41)

[185] p: Thus, each updated coordinate is a weighted average of the model prediction x ^ 1 , i \hat{x}_{1,i} and the observation y i y_{i} . If we define the weight on the observation as

[186] table: π i , Euclid ≡ 1 1 + σ i 2 ​ ( t ) , \displaystyle\pi_{i,\text{Euclid}}\;\equiv\;\frac{1}{1+\sigma_{i}^{2}(t)}, (42)

[187] p: the update takes the intuitive form

[188] table: x ^ 1 , i ⋆ = ( 1 − π i , Euclid ) ​ x ^ 1 , i + π i , Euclid ​ y i . \displaystyle\hat{x}_{1,i}^{\star}\;=\;(1-\pi_{i,\text{Euclid}})\,\hat{x}_{1,i}+\pi_{i,\text{Euclid}}\,y_{i}. (43)

[189] p: This shows that, in the Euclidean case, the “weight on data” for an active coordinate is exactly π i , Euclid = 1 / ( 1 + σ i 2 ​ ( t ) ) \pi_{i,\text{Euclid}}=1/(1+\sigma_{i}^{2}(t)) .

[190] p: We now extend this idea to the kinematics-aware metric. The ProjFlow update becomes

[191] table: 𝒙 ^ 1 ⋆ \displaystyle\hat{{\bm{x}}}_{1}^{\star} = 𝒙 ^ 1 + R − 1 ​ M ( t ) ⊤ ​ ( M ( t ) ​ R − 1 ​ M ( t ) ⊤ + Σ ( t ) ) − 1 ​ ( 𝒚 ( t ) − M ( t ) ​ 𝒙 ^ 1 ) \displaystyle=\hat{{\bm{x}}}_{1}+R^{-1}{M^{(t)}}^{\top}\!\Bigl(M^{(t)}R^{-1}{M^{(t)}}^{\top}+\Sigma^{(t)}\Bigr)^{-1}\bigl({\bm{y}}^{(t)}-M^{(t)}\hat{{\bm{x}}}_{1}\bigr) (44) = ( I − R − 1 ​ M ( t ) ⊤ ​ ( M ( t ) ​ R − 1 ​ M ( t ) ⊤ + Σ ( t ) ) − 1 ​ M ( t ) ) ​ 𝒙 ^ 1 \displaystyle=\Bigl(I-R^{-1}{M^{(t)}}^{\top}\!\Bigl(M^{(t)}R^{-1}{M^{(t)}}^{\top}+\Sigma^{(t)}\Bigr)^{-1}M^{(t)}\Bigr)\hat{{\bm{x}}}_{1} + R − 1 ​ M ( t ) ⊤ ​ ( M ( t ) ​ R − 1 ​ M ( t ) ⊤ + Σ ( t ) ) − 1 ​ 𝒚 ( t ) . \displaystyle\hskip 9.24994pt+R^{-1}{M^{(t)}}^{\top}\!\Bigl(M^{(t)}R^{-1}{M^{(t)}}^{\top}+\Sigma^{(t)}\Bigr)^{-1}{\bm{y}}^{(t)}. (45)

[192] p: Here, R − 1 R^{-1} is dense along joint dimensions, so corrections propagate across joints, while we still choose Σ ( t ) \Sigma^{(t)} to be diagonal, with each coordinate (frame–joint–axis) having its own variance. We therefore design a dimensionless trust score π i ∈ [ 0 , 1 ] \pi_{i}\in[0,1] for each active row i i , and convert it into a variance that is consistent with the metric R R .

[193] p: Let r i := [ diag ⁡ ( R − 1 ) ] i > 0 r_{i}:=[\mathrm{diag}(R^{-1})]_{i}>0 . If only row i i were active (i.e., M ( t ) = 𝒆 i ⊤ M^{(t)}={\bm{e}}_{i}^{\top} ), the measurement-space gain of the ProjFlow update is

[194] table: π i = r i r i + σ i 2 ​ ( t ) . \displaystyle\pi_{i}\;=\;\frac{r_{i}}{\,r_{i}+\sigma_{i}^{2}(t)\,}. (46)

[195] p: Solving for σ i 2 ​ ( t ) \sigma_{i}^{2}(t) yields

[196] table: Σ i ​ i ( t ) = σ i 2 ​ ( t ) = r i ​ ( 1 π i − 1 ) . \Sigma^{(t)}_{ii}\;=\;\sigma_{i}^{2}(t)\;=\;r_{i}\!\left(\frac{1}{\pi_{i}}-1\right). (47)

[197] p: Note that when R = I R=I , we have r i = 1 r_{i}=1 , and equation 47 reduces to π i = 1 / ( 1 + σ i 2 ​ ( t ) ) \pi_{i}=1/(1+\sigma_{i}^{2}(t)) , matching the Euclidean case.

[198] h4: B.2.3 Computing the variance from the trust score for multiple joints

[199] p: To obtain the per-element trust scores π i \pi_{i} , we first compute a frame-level base trust

[200] table: π ~ n ( t ) = τ ⁡ ( t ) ​ c 0 1 + λ s ​ ( s n ​ ( 𝒙 ^ 1 ) / s med ) p , \displaystyle\tilde{\pi}_{n}^{(t)}\;=\;\tau(t)\,\frac{c_{0}}{1+\lambda_{s}\,(s_{n}(\hat{{\bm{x}}}_{1})/s_{\text{med}})^{p}}, (48)

[201] p: where n n indexes frames, s n ​ ( 𝒙 ^ 1 ) s_{n}(\hat{{\bm{x}}}_{1}) is the curvature at frame n n , s med s_{\text{med}} is the median curvature over the sequence, and c 0 , λ s , p c_{0},\lambda_{s},p are hyperparameters. This π ~ n ( t ) \tilde{\pi}_{n}^{(t)} is the total “trust budget” for all active pseudo-observations in frame n n . If only one joint has an active pseudo-observation at that frame, we simply set π i = π ~ n ( t ) \pi_{i}=\tilde{\pi}_{n}^{(t)} .

[202] p: If multiple joints are active in frame n n , we distribute the frame-level budget across them according to their influence in the kinematics-aware metric R R . Intuitively, we want to assign less trust to high-influence joints (e.g., pelvis) and more trust to low-influence joints (e.g., wrists). Let ℋ n \mathcal{H}_{n} be the set of joints j j with an active pseudo-observation in frame n n , and m n = | ℋ n | m_{n}=|\mathcal{H}_{n}| . Recall that

[203] table: R = w kin ​ ( I 3 ⊗ I N ⊗ L kin ) + λ ​ I d , \displaystyle R=w_{\text{kin}}(I_{3}\otimes I_{N}\otimes L_{\text{kin}})+\lambda I_{d}, (49)

[204] p: and define the joint-only component

[205] table: R J = w kin ​ L kin + λ ​ I J . \displaystyle R_{J}=w_{\text{kin}}L_{\text{kin}}+\lambda I_{J}. (50)

[206] p: From R J R_{J} , we define a per-joint weight as

[207] table: q j := 1 ∥ 𝐜 j ∥ 2 , \displaystyle q_{j}\;:=\;\frac{1}{\big\lVert\mathbf{c}_{j}\big\rVert_{2}}, (51)

[208] p: where 𝐜 j \mathbf{c}_{j} denotes the j j -th column of R J − 1 R_{J}^{-1} . In other words, q j q_{j} is the reciprocal of the Euclidean norm of the j j -th column of R J − 1 R_{J}^{-1} . Joints with large global influence yield columns with large norms and therefore smaller q j q_{j} , whereas low‑influence joints yield smaller column norms and thus larger q j q_{j} .

[209] p: We then distribute the frame budget proportionally to these weights. For an element i i corresponding to joint j ∈ ℋ n j\in\mathcal{H}_{n} , we set

[210] table: π i = clip ⁡ ( π ~ n ( t ) ​ q j ∑ k ∈ ℋ n q k , π min , π max ) . \displaystyle\pi_{i}\;=\;\mathrm{clip}\!\left(\tilde{\pi}_{n}^{(t)}\,\frac{q_{j}}{\sum_{k\in\mathcal{H}_{n}}q_{k}},\;\pi_{\min},\;\pi_{\max}\right). (52)

[211] p: Ignoring clipping, this construction preserves the frame-level budget, ∑ i ∈ ℋ n π i = π ~ n ( t ) \sum_{i\in\mathcal{H}_{n}}\pi_{i}=\tilde{\pi}_{n}^{(t)} , while assigning lower trust to high-influence joints and higher trust to low-influence ones. Finally, these π i \pi_{i} are converted to variances σ i 2 ​ ( t ) \sigma_{i}^{2}(t) via equation 47 , yielding the diagonal entries of Σ ( t ) \Sigma^{(t)} for the active pseudo-observations.

[212] h2: Appendix C Implementation Details

[213] h3: C.1 Application I: Motion Inpainting via Masked Pseudo-observations

[214] p: The hyperparameters used for motion inpainting are summarized in Table 5 . We use the same values for all inpainting experiments, including the main comparison in Table 1 and the ablation study in Table 3 . We set the number of ODE sampling steps to T = 100 T=100 , which corresponds to 100 function evaluations. The kinematics-aware metric R R is parameterized with w kin = 10.0 w_{\text{kin}}=10.0 and λ = 1.0 \lambda=1.0 . The dynamic masking radius shrinks linearly from l max = 10 l_{\max}=10 to l min = 3 l_{\min}=3 frames over time. For recomposition, we adopt the stochastic step from FlowDPS [ 23 ] with the noise-mixing schedule η t = 1 − σ t + Δ ​ t \eta_{t}=1-\sigma_{t+\Delta t} .

[215] figure: Block Name Symbol Value Kinematics-aware metric joint coupling weight w kin w_{\text{kin}} 10.0 ridge λ \lambda 1.0 Dynamic Masking min radius (frames) l min l_{\min} 3 max radius (frames) l max l_{\max} 10 Adaptive Variance time base τ min \tau_{\min} 0.1 strength c 0 c_{0} 3.0 curvature gain λ s \lambda_{s} 1.0 curvature power p p 2.0 trust clipping [ π min , π max ] [\pi_{\min},\pi_{\max}] [0.02, 1.0] ODE sampling NFE T T 100 noise mixing η t \eta_{t} η t = 1 − σ t + Δ ​ t \eta_{t}=1-\sigma_{t+\Delta t} Table 5: Hyperparameters for motion inpainting.

[216] h3: C.2 Application II: 2D-to-3D Lifting via Linear Projection Measurements

[217] p: For the 2D-to-3D motion lifting application, we reuse the ODE sampler hyperparameters from the inpainting task. We again set T = 100 T=100 sampling steps and use the FlowDPS [ 23 ] noise-mixing schedule η t = 1 − σ t + Δ ​ t \eta_{t}=1-\sigma_{t+\Delta t} . The kinematics-aware metric R R also uses the same values w kin = 10.0 w_{\text{kin}}=10.0 and λ = 1.0 \lambda=1.0 as in the inpainting experiments, without additional tuning for this task.

[218] h2: Appendix D Additional Quantitative Results

[219] h3: D.1 Inference Speed Comparison

[220] p: We compare the inference speed of ProjFlow against training-based controllers that use the same backbone. Figure 6 reports the average wall-clock time required to generate one 196-frame motion sample on a single A100 GPU. The x-axis labels in the figure use abbreviated names: ProjFlow (ours) and ControlNet (ACMDM) correspond to ACMDM - S - PS22+ProjFlow and ACMDM - S - PS22+ControlNet, respectively. We use the original settings from each paper whenever they are specified. For ControlNet [ 39 ] , whose sampling schedule is not detailed, we match our ProjFlow configuration for fairness: both ProjFlow and ControlNet use 100 Euler steps. OmniControl [ 63 ] is evaluated with 1,000 sampling steps. MaskControl [ 45 ] uses 10 sampling steps, with 100 logits-optimization steps at each unmasking step and 600 optimization steps at the final unmasking step as described in the original paper.

[221] p: Under these settings, ProjFlow achieves an average inference time of 1.84 s per sample and is the fastest among all compared methods. Notably, even though ProjFlow and ControlNet (ACMDM) share the same 100-step sampling schedule, ProjFlow runs faster because it keeps the original backbone unchanged, whereas ControlNet attaches an additional conditioning branch that increases model size and inference cost.

[222] figure: Figure 6 : Average inference time per 196-frame sample .

[223] figure: Figure 7 : Ablation of ProjFlow components vs. control intensity on motion inpainting. We compare the full model ( Full ) against variants that (i) replace the kinematics-aware metric with a Euclidean metric ( Euclid ), (ii) remove the stochastic noise-mixing step ( Without Noise ), or (iii) disable pseudo-observations and rely only on hard keyframes ( Plain Masking ).

[224] h3: D.2 Detailed Results of Ablation Study

[225] p: Figure 7 summarizes how each ProjFlow component affects robustness to control intensity on the motion inpainting task. The model Full is compared with three ablations: Euclid , which uses a standard Euclidean metric instead of the kinematics-aware metric; Without Noise , which removes the stochastic noise-mixing step; and Plain Masking , which removes pseudo-observations and uses only hard keyframes. When observations are sparse, both the Euclidean metric and the deterministic recomposition ( Without Noise ) noticeably degrade realism, and the Plain Masking variant performs worst, confirming the importance of our pseudo-observations. Table 6 reports the full per-joint numbers: our Full model consistently attains the best FID and R-Precision across all controlled joints, while keeping trajectory, location, and average control errors at zero.

[226] figure: Table 6 : Ablation of ACMDM-S-PS22+ProjFlow on HumanML3D. Methods are evaluated on all joints and reported per controlled joint. bold face / underline indicates the best/2 nd results if applied. Controlling Joint Methods FID ↓ \downarrow R-Precision Diversity → \rightarrow Foot Skating Traj. err. ↓ \downarrow Loc. err. ↓ \downarrow Avg. err. ↓ \downarrow Top 3 Ratio. ↓ \downarrow GT 0.000 0.000 0.795 0.795 10.455 10.455 - 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 Pelvis ACMDM - S - PS22+ProjFlow (Full) 0.107 0.784 10.645 0.0630 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 4.360 0.686 8.953 0.0550 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 2.439 0.734 9.666 0.0960 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 2.091 0.726 9.838 0.0658 0.0000 0.0000 0.0000 Left foot ACMDM - S - PS22+ProjFlow (Full) 0.095 0.771 10.644 0.0609 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 0.476 0.743 10.399 0.0643 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 4.450 0.680 9.209 0.0969 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 0.576 0.746 10.309 0.0681 0.0000 0.0000 0.0000 Right foot ACMDM - S - PS22+ProjFlow (Full) 0.096 0.770 10.651 0.0613 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 0.486 0.745 10.359 0.0655 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 4.805 0.673 9.129 0.0944 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 0.520 0.748 10.335 0.0675 0.0000 0.0000 0.0000 Head ACMDM - S - PS22+ProjFlow (Full) 0.099 0.788 10.754 0.0595 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 0.560 0.761 10.332 0.0547 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 1.852 0.750 9.714 0.0706 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 1.076 0.751 10.175 0.0594 0.0000 0.0000 0.0000 Left wrist ACMDM - S - PS22+ProjFlow (Full) 0.089 0.783 10.601 0.0586 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 0.524 0.754 10.256 0.0583 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 3.507 0.703 9.019 0.0801 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 0.506 0.759 10.242 0.0590 0.0000 0.0000 0.0000 Right wrist ACMDM - S - PS22+ProjFlow (Full) 0.096 0.780 10.610 0.0584 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 0.506 0.753 10.343 0.0591 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 3.522 0.705 9.111 0.0799 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 0.514 0.759 10.224 0.0594 0.0000 0.0000 0.0000 Average ACMDM - S - PS22+ProjFlow (Full) 0.097 0.779 10.651 0.0603 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Euclid) 1.152 0.740 10.107 0.0595 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (w/o noise) 3.429 0.707 9.308 0.0863 0.0000 0.0000 0.0000 ACMDM - S - PS22+ProjFlow (Plain Masking) 0.881 0.748 10.187 0.0632 0.0000 0.0000 0.0000

[227] h3: D.3 Detailed Results of Motion Inpainting

[228] p: In the main paper Table 1 , we presented a summrized version of the controllable motion generation results. Table 7 provides the complete per-joint evaluation, following the OmniControl [ 63 ] protocol. Across all controlled joints, ProjFlow achieves zero trajectory, location, and average errors, while its FID, R-Precision, and diversity scores remain in the same band as the strongest training-based controllers. This shows that enforcing exact spatial constraints with ProjFlow does not come at the expense of motion realism.

[229] figure: Table 7 : Quantitative text-conditioned motion generation with spatial control signals and upper-body editing on HumanML3D. In the first section, methods are trained and evaluated solely on pelvis controls. In the middle section, methods are trained on all joints and evaluated separately on each controlled joint. bold face / underline indicates the best/2 nd results. Controlling Joint Methods Zero-shot? FID ↓ \downarrow R-Precision Diversity → \rightarrow Foot Skating Traj. err. ↓ \downarrow Loc. err. ↓ \downarrow Avg. err. ↓ \downarrow Top 3 Ratio. ↓ \downarrow GT − - 0.000 0.000 0.795 0.795 10.455 10.455 - 0.000 0.000 0.000 0.000 0.000 0.000 Train On Pelvis MDM [ 57 ] ✓ 1.792 1.792 0.673 0.673 9.131 9.131 0.1019 0.1019 0.4022 0.4022 0.3076 0.3076 0.5959 0.5959 PriorMDM [ 51 ] ✗ 0.393 0.393 0.707 0.707 9.847 9.847 0.0897 0.0897 0.3457 0.3457 0.2132 0.2132 0.4417 0.4417 GMD [ 21 ] ✓ 0.238 0.238 0.763 0.763 10.011 10.011 0.1009 0.1009 0.0931 0.0931 0.0321 0.0321 0.1439 0.1439 OmniContol [ 63 ] ✗ 0.081 0.081 0.789 0.789 10.323 10.323 0.0547 ¯ \underline{0.0547} 0.0387 0.0387 0.0096 0.0096 0.0338 0.0338 MotionLCM V2+CtrlNet [ 9 ] ✗ 3.978 3.978 0.738 0.738 9.249 9.249 0.0901 0.0901 0.1080 0.1080 0.0581 0.0581 0.1386 0.1386 MaskControl [ 45 ] ✗ 0.066 \mathbf{0.066} 0.799 0.799 10.474 10.474 0.0543 \mathbf{0.0543} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0093 0.0093 ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.067 ¯ \underline{0.067} 0.805 \mathbf{0.805} 10.481 ¯ \underline{10.481} 0.0591 0.0591 0.0075 0.0075 0.0010 0.0010 0.0100 0.0100 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.151 0.151 0.802 ¯ \underline{0.802} − - 0.0610 0.0610 0.0027 ¯ \underline{0.0027} 0.0002 ¯ \underline{0.0002} 0.0089 ¯ \underline{0.0089} ACMDM-S-PS22+ProjFlow (ours) ✓ 0.107 0.107 0.784 0.784 10.645 \mathbf{10.645} 0.0630 0.0630 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Pelvis OmniContol [ 63 ] ✗ 0.135 0.135 0.790 0.790 10.314 10.314 0.0571 ¯ \underline{0.0571} 0.0404 0.0404 0.0085 0.0085 0.0367 0.0367 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.726 4.726 0.713 0.713 9.209 9.209 0.1162 0.1162 0.1617 0.1617 0.0841 0.0841 0.1838 0.1838 MaskControl [ 45 ] ✗ 0.087 ¯ \underline{0.087} 0.795 0.795 10.168 10.168 0.0544 \mathbf{0.0544} 0.0003 ¯ \underline{0.0003} 0.0000 \mathbf{0.0000} 0.0114 0.0114 ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.075 \mathbf{0.075} 0.805 \mathbf{0.805} 10.536 ¯ \underline{10.536} 0.0603 0.0603 0.0081 0.0081 0.0011 0.0011 0.0134 0.0134 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.151 0.151 0.802 ¯ \underline{0.802} − - 0.0610 0.0610 0.0027 ¯ \underline{0.0027} 0.0002 ¯ \underline{0.0002} 0.0089 ¯ \underline{0.0089} ACMDM-S-PS22+ProjFlow (ours) ✓ 0.107 0.107 0.784 0.784 10.645 \mathbf{10.645} 0.0630 0.0630 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Left foot OmniContol [ 63 ] ✗ 0.093 0.093 0.794 0.794 10.338 10.338 0.0692 0.0692 0.0594 0.0594 0.0094 0.0094 0.0314 0.0314 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.810 4.810 0.706 0.706 9.158 9.158 0.1047 0.1047 0.2607 0.2607 0.1229 0.1229 0.2304 0.2304 MaskControl [ 45 ] ✗ 0.074 ¯ \underline{0.074} 0.793 0.793 10.241 10.241 0.0561 \mathbf{0.0561} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0066 ¯ \underline{0.0066} ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.063 \mathbf{0.063} 0.800 \mathbf{0.800} 10.542 ¯ \underline{10.542} 0.0590 ¯ \underline{0.0590} 0.0186 0.0186 0.0034 0.0034 0.0240 0.0240 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.147 0.147 0.799 ¯ \underline{0.799} − - 0.0602 0.0602 0.0082 ¯ \underline{0.0082} 0.0003 ¯ \underline{0.0003} 0.0133 0.0133 ACMDM-S-PS22+ProjFlow (ours) ✓ 0.095 0.095 0.771 0.771 10.644 \mathbf{10.644} 0.0609 0.0609 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Right foot OmniContol [ 63 ] ✗ 0.137 0.137 0.798 0.798 10.241 10.241 0.0668 0.0668 0.0666 0.0666 0.0120 0.0120 0.0334 0.0334 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.756 4.756 0.705 0.705 9.303 9.303 0.1026 0.1026 0.2459 0.2459 0.1127 0.1127 0.2278 0.2278 MaskControl [ 45 ] ✗ 0.080 ¯ \underline{0.080} 0.793 0.793 10.159 10.159 0.0552 \mathbf{0.0552} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0062 ¯ \underline{0.0062} ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.071 \mathbf{0.071} 0.803 \mathbf{0.803} 10.591 ¯ \underline{10.591} 0.0583 ¯ \underline{0.0583} 0.0205 0.0205 0.0030 0.0030 0.0251 0.0251 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.153 0.153 0.800 ¯ \underline{0.800} − - 0.0597 0.0597 0.0086 ¯ \underline{0.0086} 0.0003 ¯ \underline{0.0003} 0.0138 0.0138 ACMDM-S-PS22+ProjFlow (ours) ✓ 0.096 0.096 0.770 0.770 10.651 \mathbf{10.651} 0.0613 0.0613 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Head OmniContol [ 63 ] ✗ 0.146 0.146 0.796 0.796 10.239 10.239 0.0556 ¯ \underline{0.0556} 0.0422 0.0422 0.0079 0.0079 0.0349 0.0349 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.580 4.580 0.715 0.715 9.278 9.278 0.1138 0.1138 0.1971 0.1971 0.0977 0.0977 0.2136 0.2136 MaskControl [ 45 ] ✗ 0.090 ¯ \underline{0.090} 0.797 0.797 10.131 10.131 0.0531 \mathbf{0.0531} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0064 ¯ \underline{0.0064} ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.081 \mathbf{0.081} 0.805 \mathbf{0.805} 10.520 ¯ \underline{10.520} 0.0598 0.0598 0.0051 0.0051 0.0009 0.0009 0.0152 0.0152 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.138 0.138 0.801 ¯ \underline{0.801} − - 0.0591 0.0591 0.0025 ¯ \underline{0.0025} 0.0002 ¯ \underline{0.0002} 0.0084 0.0084 ACMDM-S-PS22+ProjFlow (ours) ✓ 0.099 0.099 0.788 0.788 10.754 \mathbf{10.754} 0.0595 0.0595 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Left wrist OmniContol [ 63 ] ✗ 0.119 0.119 0.783 0.783 10.217 10.217 0.0562 ¯ \underline{0.0562} 0.0801 0.0801 0.0134 0.0134 0.0529 0.0529 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.103 4.103 0.726 0.726 9.188 9.188 0.1167 0.1167 0.3965 0.3965 0.1912 0.1912 0.3150 0.3150 MaskControl [ 45 ] ✗ 0.118 0.118 0.797 0.797 10.153 10.153 0.0546 \mathbf{0.0546} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0044 ¯ \underline{0.0044} ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.065 \mathbf{0.065} 0.804 \mathbf{0.804} 10.480 ¯ \underline{10.480} 0.0604 0.0604 0.0085 0.0085 0.0014 0.0014 0.0206 0.0206 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.149 0.149 0.799 ¯ \underline{0.799} − - 0.0600 0.0600 0.0076 ¯ \underline{0.0076} 0.0004 ¯ \underline{0.0004} 0.0138 0.0138 ACMDM-S-PS22+ProjFlow (ours) ✓ 0.089 ¯ \underline{0.089} 0.783 0.783 10.601 \mathbf{10.601} 0.0586 0.0586 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Right wrist OmniContol [ 63 ] ✗ 0.128 0.128 0.792 0.792 10.309 10.309 0.0601 0.0601 0.0813 0.0813 0.0127 0.0127 0.0519 0.0519 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.051 4.051 0.725 0.725 9.242 9.242 0.1176 0.1176 0.3822 0.3822 0.1806 0.1806 0.3079 0.3079 MaskControl [ 45 ] ✗ 0.121 0.121 0.797 0.797 10.105 10.105 0.0537 \mathbf{0.0537} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0044 ¯ \underline{0.0044} ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.066 \mathbf{0.066} 0.802 \mathbf{0.802} 10.484 ¯ \underline{10.484} 0.0599 0.0599 0.0091 0.0091 0.0016 0.0016 0.0201 0.0201 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.143 0.143 0.798 ¯ \underline{0.798} − - 0.0598 0.0598 0.0081 ¯ \underline{0.0081} 0.0004 ¯ \underline{0.0004} 0.0142 0.0142 ACMDM-S-PS22+ProjFlow (ours) ✓ 0.096 ¯ \underline{0.096} 0.780 0.780 10.610 \mathbf{10.610} 0.0584 ¯ \underline{0.0584} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} Average OmniContol [ 63 ] ✗ 0.126 0.126 0.792 0.792 10.276 10.276 0.0608 0.0608 0.0617 0.0617 0.0107 0.0107 0.0404 0.0404 MotionLCM V2+CtrlNet [ 9 ] ✗ 4.504 4.504 0.715 0.715 9.230 9.230 0.1119 0.2740 0.2740 0.1315 0.1315 0.2464 0.2464 MaskControl [ 45 ] ✗ 0.095 ¯ \underline{0.095} 0.795 0.795 10.159 10.159 0.0545 \mathbf{0.0545} 0.0001 ¯ \underline{0.0001} 0.0000 \mathbf{0.0000} 0.0065 ¯ \underline{0.0065} ACMDM-S-PS22+CtrlNet [ 39 ] ✗ 0.070 \mathbf{0.070} 0.803 \mathbf{0.803} 10.526 ¯ \underline{10.526} 0.0596 ¯ \underline{0.0596} 0.0117 0.0117 0.0019 0.0019 0.0197 0.0197 ACMDM-S-PS22+DNO [ 20 ] ✓ 0.147 0.147 0.800 ¯ \underline{0.800} − - 0.0600 0.0600 0.0034 0.0034 0.0003 ¯ \underline{0.0003} 0.0121 0.0121 ACMDM-S-PS22+ProjFlow (ours) ✓ 0.097 0.097 0.779 0.779 10.651 \mathbf{10.651} 0.0603 0.0603 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000} 0.0000 \mathbf{0.0000}

[230] h3: D.4 Evaluation on Legacy Metrics

[231] p: Meng et al. [40] recently highlighted several shortcomings in the conventional HumanML3D evaluation protocol and proposed revised metrics, which we adopt for the main results in the paper. However, many prior works [ 57 , 63 , 46 , 9 , 45 , 51 , 21 ] still report performance using the legacy protocol, making direct comparison otherwise impossible. To broaden the set of comparable baselines, we therefore also evaluate ProjFlow and existing methods under the original evaluation setup. The results are summarized in Table 8 . Under this legacy protocol, ProjFlow remains competitive with strong training-based controllers while retaining its zero-shot nature and exact constraint satisfaction.

[232] figure: Table 8 : Quantitative text-conditioned motion generation with spatial control signals and upper-body editing on HumanML3D [ 15 ] . The first section covers pelvis-only control; the middle section shows the average for all joints. The last section presents upper-body editing results. bold face / underline indicates the best/2 nd results. Controlling Joint Methods Zero-shot? FID ↓ \downarrow R-Precision Diversity → \rightarrow Foot Skating Traj. err. ↓ \downarrow Loc. err. ↓ \downarrow Avg. err. ↓ \downarrow Top 3 Ratio. ↓ \downarrow GT - 0.002 0.002 0.797 0.797 9.503 9.503 - 0.000 0.000 0.000 0.000 0.000 0.000 Train On Pelvis MDM [ 57 ] ✓ 0.698 0.698 0.602 0.602 9.197 9.197 0.1019 0.1019 40.22 40.22 30.76 30.76 59.59 59.59 PriorMDM [ 51 ] ✗ 0.475 0.475 0.583 0.583 9.156 9.156 0.0897 0.0897 34.57 34.57 21.32 21.32 44.17 44.17 GMD [ 21 ] ✓ 0.576 0.576 0.665 0.665 9.206 9.206 0.1009 0.1009 9.31 9.31 3.21 3.21 14.39 14.39 OmniControl [ 63 ] ✗ 0.218 0.218 0.687 0.687 9.422 9.422 0.0547 \mathbf{0.0547} 3.87 ¯ \underline{3.87} 0.96 ¯ \underline{0.96} 3.38 3.38 MotionLCM V2 [ 9 ] ✗ 0.531 0.531 0.752 0.752 9.253 9.253 − - 18.87 18.87 7.69 7.69 18.97 18.97 TLControl [ 59 ] ✗ 0.271 0.271 0.779 ¯ \underline{0.779} 9.569 ¯ \underline{9.569} − - 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} 1.08 1.08 MaskControl [ 45 ] ✗ 0.061 \mathbf{0.061} 0.809 \mathbf{0.809} 9.496 \mathbf{9.496} 0.0547 \mathbf{0.0547} 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} 0.98 ¯ \underline{0.98} ACMDM - S - PS22+ProjFlow (ours) ✓ 0.083 ¯ \underline{0.083} 0.755 0.755 9.096 9.096 0.0651 ¯ \underline{0.0651} 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} Train On All Joints (Average) OmniControl [ 63 ] ✗ 0.310 0.310 0.693 0.693 9.502 \mathbf{9.502} 0.0608 ¯ \underline{0.0608} 6.17 ¯ \underline{6.17} 1.07 ¯ \underline{1.07} 4.04 4.04 TLControl [ 59 ] ✗ 0.256 0.256 0.782 ¯ \underline{0.782} 9.719 9.719 − - 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} 1.11 1.11 MaskControl [ 45 ] ✗ 0.083 ¯ \underline{0.083} 0.805 \mathbf{0.805} 9.395 ¯ \underline{9.395} 0.0545 \mathbf{0.0545} 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} 0.72 ¯ \underline{0.72} ACMDM - S - PS22+ProjFlow (ours) ✓ 0.074 \mathbf{0.074} 0.752 0.752 9.065 9.065 0.0624 0.0624 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} 0.00 \mathbf{0.00} Methods Zero-shot? FID ↓ \downarrow R-Precision R-Precision R-Precision Matching ↓ \downarrow Diversity → \rightarrow − - Top 1 Top 2 Top 3 UpperBody Edit MDM [ 57 ] ✓ 4.827 4.827 0.298 0.298 0.462 0.462 0.571 0.571 4.598 4.598 7.010 7.010 − - OmniControl [ 63 ] ✗ 1.213 1.213 0.374 0.374 0.550 0.550 0.656 0.656 5.228 5.228 9.258 9.258 − - MMM [ 46 ] ✗ 0.103 0.103 0.500 0.500 0.694 0.694 0.798 ¯ \underline{0.798} 2.972 2.972 9.254 9.254 − - MotionLCM [ 9 ] ✗ 0.311 0.311 0.512 ¯ \underline{0.512} 0.685 0.685 0.798 ¯ \underline{0.798} 2.948 ¯ \underline{2.948} 9.736 ¯ \underline{9.736} − - MaskControl [ 45 ] ✗ 0.074 ¯ \underline{0.074} 0.517 \mathbf{0.517} 0.708 \mathbf{0.708} 0.804 \mathbf{0.804} 2.945 \mathbf{2.945} 9.380 \mathbf{9.380} − - ACMDM - S - PS22+ProjFlow (ours) ✓ 0.051 \mathbf{0.051} 0.502 0.502 0.697 ¯ \underline{0.697} 0.793 0.793 3.281 3.281 10.611 10.611 − -

[233] h2: Appendix E Additional qualitative results.

[234] p: The supplementary material includes a browsable demo page that collects our qualitative videos (open index.html in a web browser). This page organizes examples by task: the four control scenarios from Fig. 1 , trajectory-control benchmarks comparing ProjFlow with OmniControl [ 63 ] and MaskControl [ 63 ] , and 2D-to-3D lifting comparisons against Sketch2Anim [ 68 ] . We refer readers to this page for a more complete visual impression of ProjFlow’s behavior.

[235] h2: Instructions for reporting errors

[236] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[237] p: Tip: You can select the relevant text first, to include it in your report.

[238] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[239] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
