[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Probing the Geometry of Diffusion Models with the String Method

[3] h6: Abstract

[4] p: Understanding the geometry of learned distributions is fundamental to improving and interpreting diffusion models, yet systematic tools for exploring their landscape remain limited. Standard latent-space interpolations fail to respect the structure of the learned distribution, often traversing low-density regions. We introduce a framework based on the string method that computes continuous paths between samples by evolving curves under the learned score function. Operating on pretrained models without retraining, our approach interpolates between three regimes: pure generative transport, which yields continuous sample paths; gradient-dominated dynamics, which recover minimum energy paths (MEPs); and finite-temperature string dynamics, which compute principal curves—self-consistent paths that balance energy and entropy. We demonstrate that the choice of regime matters in practice. For image diffusion models, MEPs contain high-likelihood but unrealistic “cartoon” images, confirming prior observations that likelihood maxima appear unrealistic; principal curves instead yield realistic morphing sequences despite lower likelihood. For protein structure prediction, our method computes transition pathways between metastable conformers directly from models trained on static structures, yielding paths with physically plausible intermediates. Together, these results establish the string method as a principled tool for probing the modal structure of diffusion models—identifying modes, characterizing barriers, and mapping connectivity in complex learned distributions.

[5] h2: 1 Introduction

[6] p: Generative models based on diffusion and flow matching have achieved remarkable success in learning complex data distributions. These models transport individual samples from noise to data, implicitly encoding an energy landscape through learned score functions. Yet this point-wise perspective obscures the global geometry of the learned distribution: its modal structure, the barriers between modes, and the connectivity of the data manifold.

[7] p: Understanding pathways between samples has broad applications: morphing between configurations, identifying transition states, and revealing mechanisms underlying rare events. In molecular systems, such pathways explain conformational changes and folding; in other domains, they can illuminate how the learned distribution connects distinct modes. However, current generators provide only samples, not the pathways between them. Exploiting the geometric information encoded in the learned landscape requires a principled definition of transition pathways, along with a computational procedure to find them.

[8] p: We introduce a framework that evolves entire curves of samples—strings—rather than individual points. By controlling how these strings interact with the learned score function, we can probe different aspects of the distribution geometry. Figure 1 previews our main finding: the choice of dynamics reveals a fundamental tension between likelihood and realism. Paths that maximize likelihood traverse “cartoon” configurations—simplified, stylized images that the model assigns high probability but that lie outside the typical set. Paths that account for entropy, in contrast, remain within the typical set and produce perceptually natural transitions.

[9] figure: Figure 1: The likelihood-realism paradox. Top: schematic showing the MEP (green) passing through the high-likelihood region (yellow), while the principal curve (red) stays within the typical set where data concentrates (blue points). Dashed lines indicate Voronoi cells—regions of points closest to each image along the string. Bottom: actual images at numbered locations. Endpoints (1, 2) are identical for both paths; the principal curve intermediate (3) is realistic; the MEP intermediate (4) is cartoonish. Full pathways computed by our method are shown in Figures 4 and 5 .

[10] p: This paper makes three main contributions:

[11] p: We adapt the string method from computational chemistry to work with learned score functions, enabling pathway computation from pretrained generative models without explicit energy functions.

[12] p: We show how three choices of dynamics—pure transport, gradient-dominated, and finite-temperature—reveal complementary aspects of the learned landscape.

[13] p: We demonstrate that accounting for entropy is essential for realistic pathways in high dimensions—principal curves traverse the typical set while MEPs do not—and illustrate this on image morphing and protein conformational transitions.

[14] p: Importantly, our method operates directly on pretrained models without any retraining or fine-tuning. Given only access to the learned velocity field b t b_{t} and score s t s_{t} , we can compute strings in any of the three regimes. This makes the approach immediately applicable to existing models.

[15] h3: 1.1 Related Work

[16] h5: Transition path methods.

[17] p: Computing pathways between metastable states has a long history in computational chemistry. The nudged elastic band method ( Henkelman et al., 2000 ) and string methods ( E et al., 2002 ; Ren et al., 2007 ; Maragliano et al., 2006 ) evolve chains of configurations to find minimum (free) energy paths. Extensions like the finite-temperature string method ( E et al., 2005 ) incorporate entropic effects by computing principal curves ( Hastie and Stuetzle, 1989 ) , building on concepts from transition path theory ( Vanden-Eijnden and others, 2006 ; E and Vanden-Eijnden, 2010 ) . These methods traditionally require explicit, time-independent energy functions or force fields. Our key contribution is adapting them to time-dependent energies defined implicitly through learned score functions, enabling pathway computation directly from pretrained generative models.

[18] h5: Generative modeling.

[19] p: Diffusion models and flows ( Ho et al., 2020 ; Song et al., 2021 ) learn to reverse a noising process. Stochastic interpolants ( Albergo and Vanden-Eijnden, 2023 ; Albergo et al., 2023 ) , flow matching ( Lipman et al., 2023 ) , and rectified flows ( Liu et al., 2023 ) provide unified frameworks connecting these approaches. Our method builds on this foundation, using the learned velocity and score fields to define string dynamics. Recent work observed that likelihood-maximizing points in diffusion models appear “cartoonish”—perceptually unrealistic despite high probability ( Guth et al., 2025 ; Karczewski et al., 2025 ) . We attribute this paradox to concentration of measure in high dimensions, and resolve it via finite-temperature string dynamics that account for entropy.

[20] h5: Image morphing.

[21] p: Interpolating between images in generative models is typically done via linear paths in latent space, but such paths often traverse low-density regions producing unrealistic intermediates. DiffMorpher ( Zhang et al., 2024 ) addresses this through attention interpolation and self-attention guidance; other methods optimize latent trajectories ( Wang and Golland, 2023 ) . Our framework differs by grounding interpolation in the geometry of the learned distribution, showing that naive approaches fail by ignoring entropy and that accounting for it yields realistic paths without task-specific modifications.

[22] h5: Protein conformations.

[23] p: Recent generative models learn conformational distributions from structural databases: AlphaFlow ( Jing et al., 2024 ) fine-tunes AlphaFold with flow matching, while DiG ( Zheng et al., 2023 ) , EigenFold ( Jing et al., 2023 ) , ConfDiff ( Wang et al., 2024 ) , and FoldingDiff ( Wu et al., 2024 ) train diffusion models on conformational ensembles. These methods sample individual conformations but do not provide transition pathways between them—yet such pathways are essential for understanding protein function, since biological activity often involves conformational changes ( Frauenfelder et al., 1991 ; Henzler-Wildman and Kern, 2007 ) . Our string method complements these approaches by computing pathways directly from the learned score, potentially revealing folding mechanisms and conformational change dynamics from models trained only on static structures.

[24] h2: 2 Methodology

[25] h3: 2.1 Generative Models as Score-Based Dynamics

[26] p: Diffusion and flow-matching models learn to reverse a noising process that transforms data into noise. At the heart of these methods is a time-dependent density ρ t ​ ( x ) \rho_{t}(x) interpolating between a simple density ρ 0 ​ ( x ) \rho_{0}(x) (typically Gaussian) and the data density ρ 1 ​ ( x ) \rho_{1}(x) . The model learns either a velocity field b t ​ ( x ) b_{t}(x) or a score function s t ​ ( x ) = ∇ log ⁡ ρ t ​ ( x ) s_{t}(x)=\nabla\log\rho_{t}(x) , which are related through the structure of the interpolation.

[27] p: Sampling proceeds by integrating a forward-time dynamics. In its most general form, this takes the shape of an SDE:

[28] table: d ​ x t = b t ​ ( x t ) ⏟ transport ​ d ​ t + γ t 2 ​ s t ​ ( x t ) ⏟ score correction ​ d ​ t + 2 ​ γ t ​ d ​ W t ⏟ noise , dx_{t}=\underbrace{b_{t}(x_{t})}_{\text{transport}}dt+\underbrace{\gamma_{t}^{2}s_{t}(x_{t})}_{\text{score correction}}dt+\underbrace{\sqrt{2}\gamma_{t}\,dW_{t}}_{\text{noise}}, (1)

[29] p: where the volatility γ t ≥ 0 \gamma_{t}\geq 0 can be tuned. Setting γ t = 0 \gamma_{t}=0 recovers the deterministic probability flow ODE; positive γ t \gamma_{t} yields stochastic samplers.

[30] p: A key observation is that s t ​ ( x ) = − ∇ V t ​ ( x ) s_{t}(x)=-\nabla V_{t}(x) where V t ​ ( x ) = − log ⁡ ρ t ​ ( x ) V_{t}(x)=-\log\rho_{t}(x) is an implicit energy landscape. While we cannot evaluate V t V_{t} directly, the learned score provides access to its gradient—exactly what the string method requires.

[31] p: Crucially, the score is estimated via Stein’s identity (Gaussian integration by parts), which requires adding noise to the signal. As t → 1 t\to 1 , the noise vanishes and this estimator degrades—the learned score becomes unreliable precisely at the data distribution. This is why generative models sample via nonequilibrium transport (pushing noise toward data) rather than Langevin dynamics on s 1 s_{1} . For the same reason, we cannot simply evolve strings under s 1 s_{1} ; instead, we must work dynamically across the full time interval, leveraging reliable scores at intermediate times. More theoretical details on diffusion models can be found in Appendix A .

[32] h3: 2.2 The String Method: General Formulation

[33] p: The classical string method ( E et al., 2002 ; Ren et al., 2007 ) evolves curves under a time-independent potential V ⁡ ( x ) V(x) . Here we generalize to time-dependent velocities v t ​ ( x ) v_{t}(x) arising from diffusion models. For s ∈ ( 0 , 1 ) s\in(0,1) , the string evolves according to

[34] table: ϕ ˙ t ​ ( s ) = v t ​ ( ϕ t ​ ( s ) ) + λ t ​ ( s ) ​ ∂ s ϕ t ​ ( s ) , \dot{\phi}_{t}(s)=v_{t}(\phi_{t}(s))+\lambda_{t}(s)\partial_{s}\phi_{t}(s), (2)

[35] p: where λ t ​ ( s ) \lambda_{t}(s) is a Lagrange multiplier enforcing the constraint | ∂ s ϕ t ​ ( s ) | = const |\partial_{s}\phi_{t}(s)|=\text{const} in s s . This constraint prevents bunching or spreading of points—without it, points would cluster at attractors of v t v_{t} rather than tracing a path between them. The endpoints ϕ t ​ ( 0 ) \phi_{t}(0) and ϕ t ​ ( 1 ) \phi_{t}(1) follow the probability flow ODE ϕ ˙ t = b t ​ ( ϕ t ) \dot{\phi}_{t}=b_{t}(\phi_{t}) , which serve as boundary conditions for the string evolution.

[36] h5: Discrete algorithm.

[37] p: We discretize the string as N + 1 N+1 images { ϕ t ( i ) } i = 0 N \{\phi_{t}^{(i)}\}_{i=0}^{N} . The endpoints ϕ t ( 0 ) \phi_{t}^{(0)} and ϕ t ( N ) \phi_{t}^{(N)} follow the probability flow; the interior images i = 1 , … , N − 1 i=1,\ldots,N-1 evolve via alternating steps (Figure 2 ):

[38] p: Step 1: Evolution. Move each interior image using v t v_{t} :

[39] table: ϕ t + Δ ​ t ( i ) = ϕ t ( i ) + Δ t v t ( ϕ t ( i ) ) , i = 1 , … , N − 1 . \phi_{t+\Delta t}^{(i)}=\phi_{t}^{(i)}+\Delta t\,v_{t}(\phi_{t}^{(i)}),\quad i=1,\ldots,N-1. (3)

[40] p: Step 2: Reparametrization. Redistribute images to restore equal arc-length spacing via linear or cubic spline interpolation (for details see Appendix B.2 ).

[41] p: The reparametrization implicitly enforces the λ t \lambda_{t} constraint. To fully specify the dynamics, we must choose both the velocity field v t v_{t} for interior images and an initial string { ϕ 0 ( i ) } i = 0 N \{\phi_{0}^{(i)}\}_{i=0}^{N} ; both choices are discussed in Section 2.3 . For more details on the string method, we refer the reader to Appendix B .

[42] h3: 2.3 From Transport to Energy to Entropy

[43] p: What should v t v_{t} be? We consider three choices, each motivated by limitations of the previous one.

[44] h4: 2.3.1 Pure Transport ( γ t = 0 \gamma_{t}=0 )

[45] figure: ϕ t \phi_{t} ϕ t + 1 \phi_{t+1} ϕ t + 2 \phi_{t+2} v t v_{t} Rep Figure 2: The string method. Grey dashed arrows show Step 1 (evolution): each image moves according to v t v_{t} , landing at positions marked with × \times . Blue dotted arrows show Step 2 (reparametrization): images are redistributed to restore equal arc-length spacing along the string.

[46] p: The simplest choice sets v t = b t v_{t}=b_{t} , the learned velocity field:

[47] table: ϕ ˙ t ​ ( s ) = b t ​ ( ϕ t ​ ( s ) ) + λ t ​ ( s ) ​ ∂ s ϕ t ​ ( s ) . \dot{\phi}_{t}(s)=b_{t}(\phi_{t}(s))+\lambda_{t}(s)\partial_{s}\phi_{t}(s). (4)

[48] p: Starting from a curve of noise samples at t = 0 t=0 , this produces at t = 1 t=1 a continuous path morphing between generated images. For variance-preserving schedules where ρ 0 = 𝒩 ⁡ ( 0 , I ) \rho_{0}=\mathcal{N}(0,I) , typical noise samples have norm approximately d \sqrt{d} . Given two such samples z 0 z_{0} and z 1 z_{1} , a natural initialization is

[49] table: ϕ 0 ​ ( s ) = z 0 ​ cos ⁡ ( π ​ s / 2 ) + z 1 ​ sin ⁡ ( π ​ s / 2 ) , \phi_{0}(s)=z_{0}\cos(\pi s/2)+z_{1}\sin(\pi s/2), (5)

[50] p: which traces an approximate geodesic on this sphere; a reparametrization step may be applied to enforce | ∂ s ϕ 0 ​ ( s ) | = const |\partial_{s}\phi_{0}(s)|=\text{const} exactly. Alternatively, to morph between two specific data samples x A x_{A} and x B x_{B} , we can integrate the probability flow backward from t = 1 t=1 to t = 0 t=0 to obtain z 0 z_{0} and z 1 z_{1} and use these as endpoints—this is the approach taken in our experiments.

[51] p: Pure transport produces visually appealing morphs, but the resulting path is simply the image of the initial string under the flow. While individual images remain typical samples of ρ t \rho_{t} , the path as a curve is not intrinsically defined—it depends entirely on the initialization. To obtain paths with a principled geometric meaning, we must incorporate the score.

[52] h4: 2.3.2 Minimum Energy Paths ( γ t ≫ 1 \gamma_{t}\gg 1 , T = 0 T=0 )

[53] p: Adding the score term to the velocity connects the string to the energy landscape V t = − log ⁡ ρ t V_{t}=-\log\rho_{t} :

[54] table: v t = b t + γ t 2 s t = b t − γ t 2 ∇ V t . v_{t}=b_{t}+\gamma_{t}^{2}s_{t}=b_{t}-\gamma_{t}^{2}\nabla V_{t}. (6)

[55] p: In the limit γ t → ∞ \gamma_{t}\to\infty , the score term dominates and the string relaxes rapidly toward high-density regions of ρ t \rho_{t} . Since this relaxation is much faster than the evolution of V t V_{t} itself, the string effectively sees a quasi-static energy landscape at each time, recovering the classical string method and computing minimum energy paths (MEPs).

[56] h6: Definition 2.1 (Minimum Energy Path) .

[57] p: Since in our setting V t = − log ⁡ ρ t V_{t}=-\log\rho_{t} , minimizing energy is equivalent to maximizing likelihood: MEPs are maximum likelihood paths connecting two endpoints.

[58] p: MEPs are geometrically well-defined: they pass through saddle points, identify transition states, and characterize barrier heights. However, in high dimensions, a fundamental problem emerges.

[59] h5: The likelihood-realism paradox.

[60] p: This explains the “cartoon” phenomenon ( Guth et al., 2025 ; Karczewski et al., 2025 ) : likelihood-maximizing images appear simplified and unrealistic. Our experiments confirm this—as γ \gamma increases, MEPs traverse higher-likelihood regions with increasingly cartoonish intermediates (Figure 4 ).

[61] p: To find paths connecting samples that remain within the typical set, we must account for entropy. Principal curves, discussed next, achieve this.

[62] h4: 2.3.3 Principal Curves ( γ t ≫ 1 \gamma_{t}\gg 1 , T > 0 T>0 )

[63] p: Principal curves were introduced by ( Hastie and Stuetzle, 1989 ) to find structure in unstructured data.

[64] h6: Definition 2.2 (Principal Curve) .

[65] figure: Figure 3: Relative score estimation error: 𝔼 model ​ [ | s t − s ^ t | / | s t | ] \mathbb{E}_{\text{model}}[|s_{t}-\hat{s}_{t}|/|s_{t}|] as a function of t t for a mixture of Gaussians in various dimensions. The error increases sharply near t = 1 t=1 , motivating the quenching of γ t \gamma_{t} as t → 1 t\to 1 . For details see Appendix C

[66] p: In our setting, we take ρ = ρ T ∝ ρ 1 1 / T \rho=\rho_{T}\propto\rho_{1}^{1/T} , where ρ 1 \rho_{1} is the data distribution and T ∈ [ 0 , 1 ] T\in[0,1] controls the energy-entropy balance, and we fix the endpoints ϕ ∗ ​ ( 0 ) = x A \phi^{*}(0)=x_{A} and ϕ ∗ ​ ( 1 ) = x B \phi^{*}(1)=x_{B} . At T = 1 T=1 , we obtain principal curves for ρ 1 \rho_{1} connecting the two samples through the typical set; as T → 0 T\to 0 , ρ T \rho_{T} concentrates near modes and the principal curve converges to an MEP. Our experiments confirm that increasing T T yields increasingly realistic intermediates (Figure 5 ).

[67] p: To compute principal curves, we discretize them into N + 1 N+1 images { ϕ t ( i ) } i = 0 N \{\phi_{t}^{(i)}\}_{i=0}^{N} , where the projection regions become Voronoi cells 𝒱 i = { x : ‖ x − ϕ ( i ) ‖ < ‖ x − ϕ ( j ) ‖ ​ for all ​ j ≠ i } \mathcal{V}_{i}=\{x:\|x-\phi^{(i)}\|<\|x-\phi^{(j)}\|\text{ for all }j\neq i\} . We associate to each image a walker x t ( i ) x_{t}^{(i)} that samples its Voronoi cell via the full SDE:

[68] table: d ​ x t ( i ) = b t ​ ( x t ( i ) ) ​ d ​ t + γ t 2 ​ s t ​ ( x t ( i ) ) ​ d ​ t + 2 ​ T ​ γ t ​ d ​ W t , dx_{t}^{(i)}=b_{t}(x_{t}^{(i)})\,dt+\gamma_{t}^{2}s_{t}(x_{t}^{(i)})\,dt+\sqrt{2T}\gamma_{t}\,dW_{t}, (7)

[69] p: where integration uses timesteps Δ ​ t = O ⁡ ( γ t − 2 ) \Delta t=O(\gamma_{t}^{-2}) , and we let each walker drag its string image toward the running average of its position. This effectively defines the velocity v t v_{t} of the string. Walkers must also remain closer to their associated string image than to any other; moves violating this constraint are rejected, enforcing the Voronoi restriction. Since b t b_{t} and s t s_{t} are time-dependent, we impose a separation of timescales via γ t ≫ 1 \gamma_{t}\gg 1 : the walkers equilibrate within their Voronoi cells much faster than the landscape V t V_{t} evolves, so the string tracks an approximate principal curve at each instant.

[70] p: The complete finite-temperature string method iterates the following steps for t ∈ [ 0 , 1 ] t\in[0,1] :

[71] p: Step 1: Walker evolution. Evolve each walker x t ( i ) x_{t}^{(i)} according to ( 7 ), rejecting moves that violate the minimum-distance criterion.

[72] p: Step 2: String update. Update each string image via EMA: ϕ t + Δ ​ t ( i ) = ( 1 − η ) ​ ϕ t ( i ) + η ​ x t + Δ ​ t ( i ) \phi_{t+\Delta t}^{(i)}=(1-\eta)\phi_{t}^{(i)}+\eta\,x_{t+\Delta t}^{(i)} , where η ∈ ( 0 , 1 ] \eta\in(0,1] controls the averaging timescale.

[73] p: Step 3: Reparametrization. Redistribute string images to equal arc-length spacing.

[74] h6: Remark 2.3 .

[75] p: One might ask why not compute principal curves directly on a pregenerated dataset or the original training data. While this could work for curves that remain within high-density regions, we are primarily interested in principal curves connecting metastable states—such as distinct protein conformations or image modes. These transition regions are precisely where data points are scarce. The string method addresses this by using the learned score to sample locally along the curve, even in low-density regions. This also highlights the importance of the boundary conditions in our setting: we seek principal curves connecting two specified endpoints, which differs from Hastie’s original formulation where the curve is unconstrained.

[76] h3: 2.4 Summary and Implementation

[77] p: Table 1 compares the three regimes in which our framework can operate: pure transport gives appealing but geometrically unmotivated morphs; MEPs provide geometric grounding but fail in high dimensions; principal curves combine geometric meaning with realistic outputs. Algorithm 1 provides the complete procedure for computing strings in any of these regimes.

[78] figure: Table 1: Three regimes of string dynamics. Transport MEP Principal curve γ t = 0 \gamma_{t}=0 γ t ≫ 1 \gamma_{t}\gg 1 γ t ≫ 1 \gamma_{t}\gg 1 T = 0 T=0 T > 0 T>0 Geometric No Yes Yes Entropic No No Yes Realistic Yes No Yes

[79] figure: Algorithm 1 Diffusion String Method 0: Data samples x A , x B x_{A},x_{B} ; velocity b t b_{t} ; score s t s_{t} 0: Parameters γ t \gamma_{t} , T ∈ [ 0 , 1 ] T\in[0,1] ; initial time t 0 t_{0} ; number of images N N ; timestep Δ ​ t = O ⁡ ( γ t − 2 ) \Delta t=O(\gamma_{t}^{-2}) 1: z 0 , z 1 ← z_{0},z_{1}\leftarrow integrate x ˙ t = b t ​ ( x t ) \dot{x}_{t}=b_{t}(x_{t}) from t = 1 t=1 to t = 0 t=0 starting at x A , x B x_{A},x_{B} 2: Initialize: ϕ t 0 ( i ) = z 0 ​ cos ⁡ ( π ​ i / 2 ​ N ) + z 1 ​ sin ⁡ ( π ​ i / 2 ​ N ) \phi_{t_{0}}^{(i)}=z_{0}\cos(\pi i/2N)+z_{1}\sin(\pi i/2N) for i = 0 , … , N i=0,\ldots,N 3: Reparametrize { ϕ t 0 ( i ) } \{\phi_{t_{0}}^{(i)}\} to equal arc-length spacing 4: while t < 1 t<1 do 5: for i = 0 i=0 to N N do 6: Evolve ϕ t ( i ) \phi_{t}^{(i)} (and walker x t ( i ) x_{t}^{(i)} if T > 0 T>0 ) according to chosen regime 7: end for 8: Reparametrize to equal arc-length spacing 9: end while Output: String { ϕ 1 ( i ) } i = 0 N \{\phi_{1}^{(i)}\}_{i=0}^{N} connecting x A x_{A} to x B x_{B}

[80] h5: Quenching near t = 1 t=1 .

[81] p: When using γ t > 0 \gamma_{t}>0 (for example to compute MEPs or principal curves), we quench γ t → 0 \gamma_{t}\to 0 as t → 1 t\to 1 to avoid amplifying errors in the estimated score near the data distribution (Figure 3 ). This ensures that interior images arrive accurately at t = 1 t=1 . The endpoints always evolve with pure transport ( γ t = 0 \gamma_{t}=0 ), so they return exactly to x A x_{A} and x B x_{B} .

[82] h5: Computational cost.

[83] p: The three regimes differ in expense. Pure transport ( γ t = 0 \gamma_{t}=0 ) requires only forward integration of b t b_{t} with moderate timesteps. MEPs and principal curves ( γ t ≫ 1 \gamma_{t}\gg 1 ) require smaller timesteps Δ ​ t = O ⁡ ( γ t − 2 ) \Delta t=O(\gamma_{t}^{-2}) for stability, which dominates the computational cost. In practice, N = 50 N=50 – 70 70 images, and for principal curves η = 0.1 \eta=0.1 – 0.5 0.5 , provide a good balance between path resolution and cost. Our focus is on interpretability rather than speed: the method provides a tool for analyzing the geometry of pretrained diffusion models, requiring only access to b t b_{t} and s t s_{t} without any retraining. Our experiments demonstrate that the approach is practical for realistic applications.

[84] figure: Figure 4: Effect of score weight γ \gamma . Left: string realizations for γ \gamma ranging from 15 ( top ) to 2 ( middle ) to 10 − 2 10^{-2} ( bottom ) in logarithmic steps (factor of 10 \sqrt{10} ). Higher γ \gamma drives paths through abstract, high-likelihood modes; lower γ \gamma preserves realism. Right: log-likelihood of images along each string (colored curves), overlaid on the likelihood distribution of ImageNet validation images (heatmap; see Figure 6 for details). The intermediate images along the MEP reach likelihoods far exceeding typical images.

[85] figure: Figure 5: Effect of temperature T T . Left: string realizations for T T ranging from 0.1 ( top ) to 0.5 ( middle ) to 0.9 ( bottom ). Lower T T drives paths through cartoon-like, high-likelihood regions; higher T T produces realistic samples. Right: log-likelihood of images along each string (colored curves), overlaid on the likelihood distribution of ImageNet validation images (heatmap; see Figure 6 ). As T T increases, the likelihood of the intermediates images decreases toward typical values, and images become more realistic.

[86] h2: 3 Experiments

[87] p: We demonstrate the string method on two domains: ImageNet for the likelihood-realism paradox, and proteins for conformational transitions.

[88] h3: 3.1 Images: The Three Regimes on ImageNet

[89] p: We apply the string method to ImageNet ( 256 × 256 256\times 256 ) using the SiT-XL-2-256 model ( Ma et al., 2024 ) . Images are encoded to a 4 × 32 × 32 4\times 32\times 32 latent space via a VAE. Details of the model architecture are given in Appendix D . Additional image pathways are shown in Appendix H .

[90] h5: Setup.

[91] p: Given two images, we: (1) encode into the Gaussian latent space by backward ODE to t = 0 t=0 , (2) initialize a discrete string of N = 71 N=71 points along a spherical geodesic Eq ( 5 ), and (3) evolve the string according to Eq ( 7 ) with score weight γ t = γ \gamma_{t}=\gamma for 0.1 ≥ t ≥ 0.95 0.1\geq t\geq 0.95 and γ t = 0 \gamma_{t}=0 otherwise, where γ \gamma is a tunable parameter described below. This schedule prevents the string from drifting away from the typical set (i.e., the sphere in Gaussian latent space) near t = 0 t=0 , while avoiding regions where the score approximation degrades as t → 1 t\to 1 (Figure 3 ).

[92] h5: Effect of score weight γ \gamma at T = 0 T=0 .

[93] p: Figure 4 visualizes strings interpolating between two beaver images for varying γ \gamma and T = 0 T=0 . Full strings are size 71, but we show only of subsample of 11 (1 image every 6).

[94] p: With a large score weight ( γ = 15 \gamma=15 , top row ), the string is driven toward high-likelihood regions, yielding intermediates that lie close to the MEP. Notably, the maximum-likelihood intermediate is a highly abstract, nearly single-color image, confirming that the MEP passes through likelihood maxima that lie outside the typical set and, as a result, are perceptually unrealistic .

[95] figure: Figure 6: Likelihood distributions. Histogram of log-likelihoods for ImageNet 256 × 256 256\times 256 validation images (blue), compared with images along MEPs (orange) and finite-temperature strings at T = 0.1 T=0.1 (green), T = 0.5 T=0.5 (red), and T = 0.9 T=0.9 (purple), aggregated across multiple strings. MEP intermediates have significantly higher likelihood than real images, confirming they lie outside the typical set. As temperature increases, string images approach the likelihood distribution of real data. Inset: same data on log scale.

[96] p: With a moderate score weight ( γ = 2 \gamma=2 , middle row ), intermediates become cartoon-like , consistent with prior observations in diffusion-based interpolation ( Guth et al., 2025 ; Karczewski et al., 2025 ) . With small score guidance ( γ = 10 − 2 \gamma=10^{-2} , bottom row ), the string produces visually plausible intermediates throughout.

[97] p: The left panel reports log-likelihood along each string: for large γ \gamma , the trajectory passes through a pronounced likelihood peak. The gap between typical-image likelihoods and this maximum provides a rough estimate of the data-manifold diameter in likelihood space.

[98] h5: Effect of temperature T T .

[99] p: Figure 5 illustrates the finite-temperature method for varying T T when γ = 7 \gamma=7 .

[100] p: At low temperature ( T = 0.1 T=0.1 , first row ), results closely resemble those of the zero-temperature MEP string method, recovering cartoon-like images. At moderate temperature ( T = 0.5 T=0.5 , second row ), intermediates exhibit slightly more detail but remain cartoon-like. At high temperature ( T ≈ 1 T\approx 1 , final row ), the principal curve passes through realistic-looking intermediates that balance energy and entropy. Additional examples illustrating the effect of temperature can be found in Appendix H .

[101] h5: Principal curves.

[102] p: Figure 7 shows a principal curve between two images from the goose class, computed using the finite-temperature method with T = 0.9 T=0.9 and γ = 7 \gamma=7 . The first row displays the principal curve itself: each image is obtained by EMA from its associated walker. The remaining three rows show the walkers at t = 1 t=1 that were used to compute the EMA. Upon close inspection, one can observe subtle differences between walkers—an effect of entropy—which average out to produce the smoother images along the principal curve.

[103] h5: Likelihood Distributions

[104] p: In Figure 6 , we present the histogram of log-likelihood values for the ImageNet validation set, alongside the log-likelihoods of images obtained from a large collection of strings generated using the algorithms described above. The distribution corresponding to the MEP exhibits pronounced peaks at substantially higher likelihoods than those observed for the validation set. Moreover, the finite-temperature strings display peaks whose locations shift systematically with temperature: as the temperature increases, the peak likelihood decreases, indicating a negative correlation between temperature and likelihood, consistent with theoretical expectations.

[105] figure: Principal curve Walkers Figure 7: Principal curve for images from the goose class. Top row: images along the principal curve, computed as the EMA of associated walkers ( T = 0.9 T=0.9 , γ = 7 \gamma=7 ). Bottom three rows: individual walkers at t = 1 t=1 . The walkers exhibit subtle variations due to entropic effects (best seen when zoomed in); averaging produces the smoother images in the principal curve.

[106] h3: 3.2 Proteins: Conformational Transitions

[107] p: We apply the string method to predict transition pathways between protein conformations using two diffusion models. One, called DiG ( Zheng et al., 2023 ) , operates in SE(3) and it has been trained on experimental structures up to December 2020. The other, ScoreMD ( Plainer et al., 2026 ) , operates in ℝ 3 \mathbb{R}^{3} and includes a Fokker–Planck regularization term during training to improve score estimation near t = 1 t=1 .

[108] h5: Motivation.

[109] p: Proteins fluctuate between metastable conformations, but experiments typically capture only static snapshots. Transition pathways—the sequence of intermediate structures connecting conformers—are crucial for understanding function but are rarely observed directly. Computational methods such as molecular dynamics can in principle reveal these pathways, but the timescales involved often exceed what is computationally accessible ( Shaw et al., 2010 ) . We demonstrate that our framework, applied to a pretrained generative model, can predict plausible transition pathways by computing principal curves with the finite-temperature string method. These pathways connect endpoint conformations while remaining within the typical set of the learned distribution, balancing likelihood and entropy.

[110] figure: Figure 8: Adenylate Kinase transition pathway. Pathway between the open (4AKE) and closed (1AKE) conformations computed using DiG. Intermediate structures maintain physical plausibility (secondary structure preservation, no steric clashes).

[111] figure: Figure 9: BBA folding pathway. Top: structures along the initial string obtained by pure transport ( γ = 0 \gamma=0 ). Bottom: structures along the converged MEP. Both show progressive formation of secondary structure. Left panel: initial string (purple) and MEP (green) projected onto the first two TIC components, overlaid on a free-energy landscape estimated from ScoreMD samples; darker regions indicate lower free energy. Asterisks mark equal arc-length intervals. Right panel: energy profile along each pathway. The MEP achieves significantly lower energy than the initial string.

[112] figure: Figure 10: Chignolin folding pathway. Top: structures along the initial string obtained by pure transport ( γ = 0 \gamma=0 ). Bottom: structures along the converged MEP. Both show progressive formation of secondary structure. Left panel: initial string (purple) and MEP (green) projected onto the first two TIC components, overlaid on a free-energy landscape estimated from ScoreMD samples; darker regions indicate lower free energy. Asterisks mark equal arc-length intervals. Right panel: energy profile along each pathway. The MEP achieves significantly lower energy than the initial string.

[113] h5: Method.

[114] p: Given two conformations of the same protein, we apply the string method in the SE(3)-equivariant space of the model. The score function is derived from the model’s denoising objective. Details are given in Appendices F and E .

[115] h5: Adenylate Kinase.

[116] p: Adenylate kinase (AdK) is a phosphotransferase enzyme that undergoes a large-scale conformational change between open and closed states during catalysis ( Müller et al., 1996 ) . This transition has been extensively studied as a model system for understanding protein dynamics ( Arora and Brooks III, 2007 ; Beckstein et al., 2009 ) . Using DiG, we computed the pathway between the open (PDB: 4AKE) and closed (PDB: 1AKE) conformations (Figure 8 ). The intermediates preserve secondary structure elements and avoid steric clashes, suggesting physically plausible transitions despite the model being trained only on static structures.

[117] h5: BBA and Chignolin.

[118] p: BBA and Chignolin are small protein domains widely used as model systems for protein folding due to their rapid folding kinetics and simple topologies ( Lindorff-Larsen et al., 2011 ) . Using ScoreMD ( Plainer et al., 2026 ) , we computed minimum energy paths (MEPs) connecting extended and folded conformations for both proteins.

[119] p: For ScoreMD, the score function is accurately learned near t = 1 t=1 , allowing us to apply the classical string method at a fixed time to compute MEPs. However, the high dimensionality and rough landscape make optimization sensitive to initialization. We therefore use as initialization a string obtained by pure transport ( γ = 0 \gamma=0 ).

[120] p: Figures 9 and 10 show the computed pathways projected onto the first two time-independent components (TICs) ( Liu et al., 2008 ) . Left panels display the MEP (yellow) and initial string (purple) projected onto TIC coordinates and overlaid on a free-energy landscape, where free energy is estimated as − log ⁡ ρ -\log\rho from a histogram of i.i.d. samples generated by ScoreMD; darker regions indicate lower free energy. The MEP is driven toward lower free-energy regions compared to the initial string. Some path segments may appear to overlap due to projection from high dimensions; asterisks mark equal arc-length intervals to clarify the geometry.

[121] p: Right panels show the free energy profile along each pathway, relative to the starting conformation. The initial string has significantly higher free energy than the converged MEP, demonstrating that the string relaxation is essential. Because the dimensionality is substantially lower than in the image setting, the MEPs remain physically realistic rather than cartoonish.

[122] p: Above the two panels for each protein, we include a three-dimensional rendering of its folding pathway; the protein is colored consistently with the corresponding pathway to facilitate visual correspondence.

[123] h2: 4 Conclusion

[124] p: We adapted the string method to probe the geometry of learned distributions using score functions from pretrained generative models. By varying the dynamics—pure transport, gradient-dominated, or finite-temperature—we reveal complementary aspects of the distribution landscape.

[125] p: Our key finding is that accounting for entropy is essential in high dimensions. Minimum energy paths traverse high-likelihood but low-probability regions, producing cartoonish artifacts. Principal curves, which balance energy against entropy, yield realistic transitions with stronger theoretical grounding. These results confirm and explain prior observations that high-likelihood samples from diffusion models appear unrealistic ( Guth et al., 2025 ; Karczewski et al., 2025 ) : the phenomenon is not a model defect but a consequence of concentration of measure, and can be resolved by accounting for entropy.

[126] p: This establishes the string method as a tool for analyzing generative models beyond sampling: identifying modes, characterizing barriers, and mapping connectivity in complex learned distributions. Importantly, the method requires no retraining—only access to the learned velocity and score fields.

[127] h5: Limitations.

[128] p: The computed pathways are only as good as the underlying generative model. If the model assigns low probability to physically relevant transition states, the string method cannot recover them. Similarly, errors in score estimation—particularly near the data distribution—propagate to the computed paths, motivating our quenching strategy.

[129] h5: Future directions.

[130] p: Several extensions are natural. Scaling to larger models (e.g., text-to-image diffusion) would test whether the likelihood-realism tradeoff persists across architectures. Theoretical analysis of convergence rates and approximation error would strengthen the foundations. Beyond images and proteins, the method applies wherever transition pathways matter: molecular design, robotics, and latent space exploration in multimodal models. Finally, combining string methods with conditional generation could enable targeted pathway computation—for instance, finding transitions that pass through specified intermediate states.

[131] h2: Impact Statement

[132] p: This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

[133] h2: References

[134] h2: Appendix A Background on Diffusion Models

[135] h3: A.1 Velocity and Score: Definitions and Estimators

[136] p: In the stochastic interpolant framework, we construct a time-dependent density ρ t \rho_{t} via the interpolant I t = α t ​ x 0 + β t ​ x 1 I_{t}=\alpha_{t}x_{0}+\beta_{t}x_{1} with x 0 ∼ 𝒩 ⁡ ( 0 , I ) x_{0}\sim\mathcal{N}(0,I) and x 1 ∼ ρ 1 x_{1}\sim\rho_{1} . Common choices include:

[137] p: Linear: α t = 1 − t \alpha_{t}=1-t , β t = t \beta_{t}=t

[138] p: Trigonometric: α t = cos ⁡ ( π ​ t 2 ) \alpha_{t}=\cos(\tfrac{\pi t}{2}) , β t = sin ⁡ ( π ​ t 2 ) \beta_{t}=\sin(\tfrac{\pi t}{2}) (variance-preserving)

[139] p: α t = 1 − t 2 \alpha_{t}=\sqrt{1-t^{2}} , β t = t \beta_{t}=t (variance-preserving; time-rescaled Ornstein-Uhlenbeck)

[140] p: The velocity field and score are defined as:

[141] table: b t ​ ( x ) \displaystyle b_{t}(x) = 𝔼 ⁡ [ I ˙ t ∣ I t = x ] , \displaystyle=\mathbb{E}[\dot{I}_{t}\mid I_{t}=x], (8) s t ​ ( x ) \displaystyle s_{t}(x) = ∇ log ⁡ ρ t ​ ( x ) . \displaystyle=\nabla\log\rho_{t}(x). (9)

[142] p: Both can be estimated by regression: b t b_{t} by minimizing 𝔼 ⁡ [ | I ˙ t − b t ​ ( I t ) | 2 ] \mathbb{E}[|\dot{I}_{t}-b_{t}(I_{t})|^{2}] , and s t s_{t} via denoising score matching using the conditional Gaussian structure I t | x 1 ∼ 𝒩 ⁡ ( β t ​ x 1 , α t 2 ​ I ) I_{t}\mid x_{1}\sim\mathcal{N}(\beta_{t}x_{1},\alpha_{t}^{2}I) . The two are related by:

[143] table: s t ​ ( x ) = β t ​ b t ​ ( x ) − β ˙ t ​ x α t ​ ( α ˙ t ​ β t − α t ​ β ˙ t ) . s_{t}(x)=\frac{\beta_{t}b_{t}(x)-\dot{\beta}_{t}x}{\alpha_{t}(\dot{\alpha}_{t}\beta_{t}-\alpha_{t}\dot{\beta}_{t})}. (10)

[144] h3: A.2 The General SDE and Fokker-Planck Equation

[145] p: The general SDE used in our framework is:

[146] table: d ​ x t = b t ​ ( x t ) ​ d ​ t + γ t 2 ​ s t ​ ( x t ) ​ d ​ t + 2 ​ γ t ​ d ​ W t . dx_{t}=b_{t}(x_{t})\,dt+\gamma_{t}^{2}s_{t}(x_{t})\,dt+\sqrt{2}\gamma_{t}\,dW_{t}. (11)

[147] p: The corresponding Fokker-Planck equation for the density is:

[148] table: ∂ t ρ t + ∇ ⋅ [ ( b t + γ t 2 ​ s t ) ​ ρ t ] = γ t 2 ​ Δ ​ ρ t . \partial_{t}\rho_{t}+\nabla\cdot\left[(b_{t}+\gamma_{t}^{2}s_{t})\rho_{t}\right]=\gamma_{t}^{2}\Delta\rho_{t}. (12)

[149] p: Substituting s t = ∇ log ⁡ ρ t s_{t}=\nabla\log\rho_{t} , one can verify that ρ t \rho_{t} is preserved for any γ t ≥ 0 \gamma_{t}\geq 0 : the score correction γ t 2 s t ρ t = γ t 2 ∇ ρ t \gamma_{t}^{2}s_{t}\rho_{t}=\gamma_{t}^{2}\nabla\rho_{t} and the diffusion term γ t 2 ​ Δ ​ ρ t \gamma_{t}^{2}\Delta\rho_{t} cancel in the flux, leaving the evolution determined by b t b_{t} alone. This is a local detailed balance condition at each time t t ; since b t b_{t} and s t s_{t} are time-dependent, the overall dynamics describe nonequilibrium sampling from ρ 0 \rho_{0} to ρ 1 \rho_{1} .

[150] h3: A.3 Likelihood Computation via the Probability Flow ODE

[151] p: Setting γ t = 0 \gamma_{t}=0 in the general SDE gives the probability flow ODE

[152] table: x ˙ t = b t ​ ( x t ) . \dot{x}_{t}=b_{t}(x_{t}). (13)

[153] p: The corresponding transport equation for the density is

[154] table: ∂ t ρ t + ∇ ⋅ ( b t ​ ρ t ) = 0 . \partial_{t}\rho_{t}+\nabla\cdot(b_{t}\rho_{t})=0. (14)

[155] p: This can be solved by the method of characteristics. Let x t x_{t} be a solution of the ODE starting from x 0 x_{0} . Differentiating ρ t ​ ( x t ) \rho_{t}(x_{t}) along the flow we deduce

[156] table: d d ​ t ​ ρ t ​ ( x t ) = ∂ t ρ t ​ ( x t ) + ∇ ρ t ​ ( x t ) ⋅ x ˙ t = ∂ t ρ t ​ ( x t ) + ∇ ρ t ​ ( x t ) ⋅ b t ​ ( x t ) . \frac{d}{dt}\rho_{t}(x_{t})=\partial_{t}\rho_{t}(x_{t})+\nabla\rho_{t}(x_{t})\cdot\dot{x}_{t}=\partial_{t}\rho_{t}(x_{t})+\nabla\rho_{t}(x_{t})\cdot b_{t}(x_{t}). (15)

[157] p: Using the transport equation ∂ t ρ t = − ∇ ⋅ ( b t ρ t ) = − b t ⋅ ∇ ρ t − ρ t ∇ ⋅ b t \partial_{t}\rho_{t}=-\nabla\cdot(b_{t}\rho_{t})=-b_{t}\cdot\nabla\rho_{t}-\rho_{t}\nabla\cdot b_{t} , we obtain

[158] table: d d ​ t ρ t ( x t ) = − ρ t ( x t ) ∇ ⋅ b t ( x t ) . \frac{d}{dt}\rho_{t}(x_{t})=-\rho_{t}(x_{t})\nabla\cdot b_{t}(x_{t}). (16)

[159] p: This is a linear ODE in ρ t ​ ( x t ) \rho_{t}(x_{t}) , with solution

[160] table: ρ t ( x t ) = ρ 0 ( x 0 ) exp ( − ∫ 0 t ∇ ⋅ b τ ( x τ ) d τ ) . \rho_{t}(x_{t})=\rho_{0}(x_{0})\exp\left(-\int_{0}^{t}\nabla\cdot b_{\tau}(x_{\tau})\,d\tau\right). (17)

[161] p: Taking logarithms gives the log-likelihood

[162] table: log ⁡ ρ t ​ ( x t ) = log ⁡ ρ 0 ​ ( x 0 ) − ∫ 0 t ∇ ⋅ b τ ​ ( x τ ) ​ 𝑑 τ . \log\rho_{t}(x_{t})=\log\rho_{0}(x_{0})-\int_{0}^{t}\nabla\cdot b_{\tau}(x_{\tau})\,d\tau. (18)

[163] p: In practice, given a data sample x 1 ∼ ρ 1 x_{1}\sim\rho_{1} , we integrate the ODE backward from t = 1 t=1 to t = 0 t=0 to obtain x 0 x_{0} , and accumulate the divergence ∇ ⋅ b t \nabla\cdot b_{t} along the trajectory. Since ρ 0 = 𝒩 ⁡ ( 0 , I ) \rho_{0}=\mathcal{N}(0,I) , the term log ⁡ ρ 0 ​ ( x 0 ) \log\rho_{0}(x_{0}) is simply − 1 2 ​ ‖ x 0 ‖ 2 − d 2 ​ log ⁡ ( 2 ​ π ) -\frac{1}{2}\|x_{0}\|^{2}-\frac{d}{2}\log(2\pi) .

[164] h2: Appendix B String Method: Derivation and Implementation

[165] h3: B.1 Continuous Evolution

[166] p: We derive the continuous string evolution equation from the constraint that arc-length parametrization is preserved.

[167] h6: Proposition B.1 .

[168] p: Let ϕ t : [ 0 , 1 ] → ℝ d \phi_{t}:[0,1]\to\mathbb{R}^{d} be a curve evolving under a velocity field v t v_{t} . Assume that the endpoints evolve as independent points:

[169] table: ϕ ˙ t ​ ( 0 ) = v t ​ ( ϕ t ​ ( 0 ) ) , ϕ ˙ t ​ ( 1 ) = v t ​ ( ϕ t ​ ( 1 ) ) . \dot{\phi}_{t}(0)=v_{t}(\phi_{t}(0)),\quad\dot{\phi}_{t}(1)=v_{t}(\phi_{t}(1)). (19)

[170] p: Then, for s ∈ ( 0 , 1 ) s\in(0,1) , the evolution

[171] table: ϕ ˙ t ​ ( s ) = v t ​ ( ϕ t ​ ( s ) ) + λ t ​ ( s ) ​ ∂ s ϕ t ​ ( s ) \dot{\phi}_{t}(s)=v_{t}(\phi_{t}(s))+\lambda_{t}(s)\partial_{s}\phi_{t}(s) (20)

[172] p: preserves the arc-length parametrization | ∂ s ϕ t ​ ( s ) | = L ⁡ ( t ) |\partial_{s}\phi_{t}(s)|=L(t) (constant in s s ) for an appropriate choice of λ t ​ ( s ) \lambda_{t}(s) with λ t ​ ( 0 ) = λ t ​ ( 1 ) = 0 \lambda_{t}(0)=\lambda_{t}(1)=0 .

[173] h6: Proof.

[174] p: The arc-length parametrization requires | ∂ s ϕ t | 2 |\partial_{s}\phi_{t}|^{2} to be constant in s s , i.e., ⟨ ∂ s ϕ t , ∂ s 2 ϕ t ⟩ = 0 \langle\partial_{s}\phi_{t},\partial_{s}^{2}\phi_{t}\rangle=0 for all s s and t t . Taking the time derivative:

[175] table: ∂ t ⟨ ∂ s ϕ t , ∂ s 2 ϕ t ⟩ = ⟨ ∂ s ϕ ˙ t , ∂ s 2 ϕ t ⟩ + ⟨ ∂ s ϕ t , ∂ s 2 ϕ ˙ t ⟩ = 0 . \partial_{t}\langle\partial_{s}\phi_{t},\partial_{s}^{2}\phi_{t}\rangle=\langle\partial_{s}\dot{\phi}_{t},\partial_{s}^{2}\phi_{t}\rangle+\langle\partial_{s}\phi_{t},\partial_{s}^{2}\dot{\phi}_{t}\rangle=0. (21)

[176] p: Substituting ϕ ˙ t = v t ​ ( ϕ t ) + λ t ​ ∂ s ϕ t \dot{\phi}_{t}=v_{t}(\phi_{t})+\lambda_{t}\partial_{s}\phi_{t} and requiring this to hold for all s s determines λ t ​ ( s ) \lambda_{t}(s) . The boundary conditions λ t ​ ( 0 ) = λ t ​ ( 1 ) = 0 \lambda_{t}(0)=\lambda_{t}(1)=0 are consistent with the endpoints evolving according to v t v_{t} . ∎

[177] p: In practice, we enforce the constraint via discrete reparametrization rather than computing λ t \lambda_{t} explicitly. The derivation above applies to ℝ d \mathbb{R}^{d} with the Euclidean metric; for Riemannian manifolds such as S ​ O ​ ( 3 ) SO(3) , we work directly with the discrete algorithm.

[178] h3: B.2 Reparametrization on ℝ d \mathbb{R}^{d}

[179] p: The discrete reparametrization step redistributes points { ϕ ( i ) } i = 0 N \{\phi^{(i)}\}_{i=0}^{N} to equal arc-length spacing:

[180] p: Compute cumulative arc-lengths: L 0 = 0 L_{0}=0 , L i = L i − 1 + | ϕ ( i ) − ϕ ( i − 1 ) | L_{i}=L_{i-1}+|\phi^{(i)}-\phi^{(i-1)}| .

[181] p: Normalize: α i = L i / L N ∈ [ 0 , 1 ] \alpha_{i}=L_{i}/L_{N}\in[0,1] .

[182] p: Fit a cubic spline through ( α i , ϕ ( i ) ) (\alpha_{i},\phi^{(i)}) .

[183] p: Evaluate at uniform positions: ϕ new ( i ) = spline ​ ( i / N ) \phi^{(i)}_{\text{new}}=\text{spline}(i/N) .

[184] h3: B.3 Reparametrization on S ​ O ​ ( 3 ) SO(3)

[185] p: On S ​ O ​ ( 3 ) SO(3) , reparametrization requires converting between the rotation matrix representation { ϕ M ( i ) } i = 0 N \{\phi^{(i)}_{M}\}_{i=0}^{N} and the axis-angle vector representation { ϕ V ( i ) } i = 0 N \{\phi^{(i)}_{V}\}_{i=0}^{N} . To reparametrize into K + 1 K+1 equally spaced points { ψ ( j ) } j = 0 K \{\psi^{(j)}\}_{j=0}^{K} :

[186] p: Compute the incremental rotations: s M ( i ) = ϕ M ( i ) ​ ( ϕ M ( i − 1 ) ) − 1 s^{(i)}_{M}=\phi^{(i)}_{M}(\phi^{(i-1)}_{M})^{-1} for 1 ≤ i ≤ N 1\leq i\leq N .

[187] p: Compute cumulative arc-lengths in the axis-angle representation: L 0 = 0 L_{0}=0 , L i = L i − 1 + | s V ( i ) | L_{i}=L_{i-1}+|s^{(i)}_{V}| .

[188] p: Normalize: α i = L i / L N ∈ [ 0 , 1 ] \alpha_{i}=L_{i}/L_{N}\in[0,1] .

[189] p: For each 0 ≤ j ≤ K 0\leq j\leq K , find the preceding index p ⁡ ( j ) = max ⁡ { i : α i ≤ j / K } p(j)=\max\{i:\alpha_{i}\leq j/K\} .

[190] p: Compute interpolated displacements: d V ( j ) = s V ( p ⁡ ( j ) + 1 ) ⋅ j / K − α p ⁡ ( j ) α p ⁡ ( j ) + 1 − α p ⁡ ( j ) d^{(j)}_{V}=s^{(p(j)+1)}_{V}\cdot\frac{j/K-\alpha_{p(j)}}{\alpha_{p(j)+1}-\alpha_{p(j)}} .

[191] p: Set ψ M ( 0 ) = ϕ M ( 0 ) \psi^{(0)}_{M}=\phi^{(0)}_{M} , ψ M ( K ) = ϕ M ( N ) \psi^{(K)}_{M}=\phi^{(N)}_{M} , and for 1 ≤ j ≤ K − 1 1\leq j\leq K-1 : ψ M ( j ) = d M ( j ) ​ ϕ M ( p ⁡ ( j ) ) \psi^{(j)}_{M}=d^{(j)}_{M}\phi^{(p(j))}_{M} .

[192] h3: B.4 Reparametrization on S ​ E ​ ( 3 ) SE(3)

[193] p: The group S ​ E ​ ( 3 ) SE(3) is the semidirect product of ℝ 3 \mathbb{R}^{3} and S ​ O ​ ( 3 ) SO(3) , hence every element ϕ ∈ S ​ E ​ ( 3 ) \phi\in SE(3) can be written as ϕ = ( t , R ) \phi=(t,R) with t ∈ ℝ 3 t\in\mathbb{R}^{3} and R ∈ S ​ O ​ ( 3 ) R\in SO(3) . There is not a criterion to choose a norm in S ​ E ​ ( 3 ) SE(3) , in this paper we chose to have | ϕ | = | t | 2 + | R V | 2 |\phi|=\sqrt{|t|^{2}+|R_{V}|^{2}} where | R V | |R_{V}| is the norm of the vector in the axis angle representation. With this choice for the norm we do the reparameterization as follows:

[194] p: Compute the incremental rotations: s M ( i ) = R M ( i ) ​ ( R M ( i − 1 ) ) − 1 s^{(i)}_{M}=R^{(i)}_{M}(R^{(i-1)}_{M})^{-1} for 1 ≤ i ≤ N 1\leq i\leq N .

[195] p: Compute the incremental translations: q ( i ) = t ( i ) − t ( i − 1 ) q^{(i)}=t^{(i)}-t^{(i-1)} for 1 ≤ i ≤ N 1\leq i\leq N .

[196] p: Compute cumulative arc-lengths in with this norm: L 0 = 0 L_{0}=0 , L i = L i − 1 + | q | 2 + | s V | 2 L_{i}=L_{i-1}+\sqrt{|q|^{2}+|s_{V}|^{2}} .

[197] p: Normalize: α i = L i / L N ∈ [ 0 , 1 ] \alpha_{i}=L_{i}/L_{N}\in[0,1] .

[198] p: For each 0 ≤ j ≤ K 0\leq j\leq K , find the preceding index p ⁡ ( j ) = max ⁡ { i : α i ≤ j / K } p(j)=\max\{i:\alpha_{i}\leq j/K\} .

[199] p: Compute interpolated rotation displacements: d V ( j ) = s V ( p ⁡ ( j ) + 1 ) ⋅ j / K − α p ⁡ ( j ) α p ⁡ ( j ) + 1 − α p ⁡ ( j ) d^{(j)}_{V}=s^{(p(j)+1)}_{V}\cdot\frac{j/K-\alpha_{p(j)}}{\alpha_{p(j)+1}-\alpha_{p(j)}} .

[200] p: Compute interpolated translation displacements: y ( j ) = q ( p ⁡ ( j ) + 1 ) ⋅ j / K − α p ⁡ ( j ) α p ⁡ ( j ) + 1 − α p ⁡ ( j ) y^{(j)}=q^{(p(j)+1)}\cdot\frac{j/K-\alpha_{p(j)}}{\alpha_{p(j)+1}-\alpha_{p(j)}} .

[201] p: Set ψ M ( 0 ) = ϕ M ( 0 ) \psi^{(0)}_{M}=\phi^{(0)}_{M} , ψ M ( K ) = ϕ M ( N ) \psi^{(K)}_{M}=\phi^{(N)}_{M} , and for 1 ≤ j ≤ K − 1 1\leq j\leq K-1 : ψ M ( j ) = ( t p ⁡ ( j ) + y ( j ) , d M ( j ) ​ ϕ M ( p ⁡ ( j ) ) ) \psi^{(j)}_{M}=(t^{p(j)}+y^{(j)},d^{(j)}_{M}\phi^{(p(j))}_{M}) .

[202] h2: Appendix C Testing the score reliability on Gaussian Mixtures

[203] p: To examine how score estimation error varies along the generative process (i.e., as t t increases from 0 to 1), we trained MLPs to learn a stochastic interpolant transporting a Gaussian distribution to a mixture of two Gaussians in d d dimensions, for different values of d d . The two modes in the mixture have means ( ± 3.0 , 0 , … , 0 ) ∈ ℝ d (\pm 3.0,0,\ldots,0)\in\mathbb{R}^{d} and covariance matrices

[204] table: ( 7.9 4 ± 6.7 ​ 3 4 ± 6.7 ​ 3 4 7.9 4 ) ⊕ I d − 2 . \begin{pmatrix}\frac{7.9}{4}&\pm\frac{6.7\sqrt{3}}{4}\\[4.0pt] \pm\frac{6.7\sqrt{3}}{4}&\frac{7.9}{4}\end{pmatrix}\oplus I_{d-2}.

[205] p: where the sign corresponds to the sign of the mean.

[206] p: We parametrized the score function using an MLP with 3 hidden layers of sizes 512, 1024, and 512. Each model was trained with batch size 1000 for 1500 × d 1500\times d iterations. For inference, we used batch size 5000 × d 5000\times d and 200 timesteps. For each value of d d , we trained 10 models; Figure 3 shows the average relative score error 𝔼 ⁡ [ | s t − s ^ t | / | s t | ] \mathbb{E}[|s_{t}-\hat{s}_{t}|/|s_{t}|] as a function of t t .

[207] h2: Appendix D Hyperparameters for SiT

[208] figure: Table 2: Hyperparameter choices for the SiT Model Hyperparameters Values Neural network Depth 28 Hidden Size 1152 Patch Size 2 Number of Attention Heads 16 MLP ratio 4.0 Class Dropout Probability 0.1 Input Size 32 Input Channels 4

[209] h2: Appendix E Hyperparameters for DiG

[210] figure: Table 3: Hyperparameters of the Distributional Graphormer Protein Model. Hyperparameter Initialization PIDP Data Training Model depth 12 Hidden dim (Single) 768 Hidden dim (Pair) 256 Hidden dim (Feed Forward) 1024 Number of Heads 32

[211] h2: Appendix F Hyperparameters for ScoreMD

[212] figure: Table 4: Graph transformer model definitions extracted from the configuration file. Model name hidden_nf feature_embedding_dim n_layers potential dropout transformer_large_score 128 16 3 false 0.0 transformer_large_potential 128 16 3 true 0.0

[213] figure: Table 5: Ranged models configuration extracted from the configuration file of the model, it should be kept in mind that for this model t = 0 t=0 is actually the interpolant time t = 1 t=1 and vice versa. Entry Model reference Range 1 transformer_large_score [ 1.0 , 0.6 ] [1.0,\;0.6] 2 transformer_large_score [ 0.6 , 0.1 ] [0.6,\;0.1] 3 transformer_large_potential [ 0.1 , 0.0 ] [0.1,\;0.0]

[214] h2: Appendix G Another model: ConfDiff

[215] p: We also applied the model on another model: ConfDiff [ 31 ] , a model operating on S ​ O ​ ( 3 ) SO(3) trained on the Protein Data Bank up to December 2021.

[216] h5: WW Domain.

[217] p: The WW domain is a small protein module that has served as a model system for studying protein folding due to its fast folding kinetics and simple topology [ 14 ] . Using ConfDiff, we computed the folding pathway from an extended to a folded conformation (Figure 11 ). The pathway reveals progressive formation of secondary structure, consistent with experimental observations of WW domain folding [ 20 ] .

[218] figure: Figure 11: Pathway from extended to folded conformation computed using ConfDiff. Intermediates show progressive formation of secondary structure.

[219] h3: G.1 Hyperparameters of the model

[220] figure: Table 6: Hyperparameter choices for ConfDiff Model Hyperparameters Values Neural network Number of IPA blocks 4 Dimension of single repr. 256 Dimension of pairwise Repr. 128 Dimension of hidden 256 Number of IPA attention heads 4 Number of IPA query points 8 Number of IPA value points 12 Number of transformer attention heads 4 Number of transformer layers 2

[221] h2: Appendix H Additional Experiments

[222] h3: H.1 Effect of the Temperature in finite-temperature string method

[223] figure: Figure 12: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[224] figure: Figure 13: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[225] figure: Figure 14: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[226] figure: Figure 15: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[227] figure: Figure 16: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[228] figure: Figure 17: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[229] figure: Figure 18: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[230] figure: Figure 19: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[231] figure: Figure 20: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[232] figure: Figure 21: Effect of temperature T T on images principal curve. Lower T T drives paths through cartoonish high-likelihood modes (top); higher T T preserves realism (bottom).

[233] h3: H.2 Multiple realizations of a principle curves

[234] figure: Figure 22: A principal curves with three realizations coming from this curve

[235] figure: Figure 23: A principal curves with three realizations coming from this curve

[236] figure: Figure 24: A principal curves with three realizations coming from this curve

[237] figure: Figure 25: A principal curves with three realizations coming from this curve

[238] figure: Figure 26: A principal curves with three realizations coming from this curve

[239] figure: Figure 27: A principal curves with three realizations coming from this curve

[240] figure: Figure 28: A principal curves with three realizations coming from this curve

[241] figure: Figure 29: A principal curves with three realizations coming from this curve

[242] figure: Figure 30: A principal curves with three realizations coming from this curve

[243] figure: Figure 31: A principal curves with three realizations coming from this curve

[244] h2: Instructions for reporting errors

[245] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[246] p: Tip: You can select the relevant text first, to include it in your report.

[247] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[248] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
