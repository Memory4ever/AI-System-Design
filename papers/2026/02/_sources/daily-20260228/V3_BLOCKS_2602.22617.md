[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA

[3] h6: Abstract

[4] p: Large Language Models (LLMs) obey consistent scaling laws—empirical power-law fits that predict how loss decreases with compute, data, and parameters. While predictive, these laws are descriptive rather than prescriptive: they characterize typical training, not optimal training. Surprisingly few works have successfully challenged the data-efficiency bounds implied by these laws—which is our primary focus. To that end, we introduce the Geodesic Hypothesis, positing that token sequences trace geodesics on a smooth semantic manifold and are therefore locally linear. Building on this principle, we propose a novel Semantic Tube Prediction (STP) task, a JEPA-style regularizer that confines hidden-state trajectories to a tubular neighborhood of the geodesic. STP generalizes JEPA to language without requiring explicit multi-view augmentations. We show this constraint improves signal-to-noise ratio, and consequently preserves diversity by preventing trajectory collisions during inference. Empirically, STP allows LLMs to match baseline accuracy with 16 × \times less training data on the NL-RX-SYNTH dataset, directly violating the data term of Chinchilla-style scaling laws and demonstrating that principled geometric priors can surpass brute-force scaling. Code is available at https://github.com/galilai-group/llm-jepa#stp .

[5] h6: Keywords:

[6] figure: (a) Semantic Tube (b) Data Efficiency Figure 1 : Semantic Tube improves data efficiency. (a) We hypothesize that error-free hidden state trajectories are geodesics, which are locally linear and approximated by the Semantic Tube. The dotted line depicts a trajectory distorted by training loss. Deviations perpendicular to the tube constitute noise , while the component along the geodesic represents the signal . (b) With our approach ( ℒ NTP + ℒ STP \mathcal{L}_{\rm NTP}+\mathcal{L}_{\rm STP} ), accuracy shows a negligible drop when the training dataset is halved, and it matches full-dataset standard fine-tuning ( ℒ NTP \mathcal{L}_{\rm NTP} ) accuracy using only 1 16 \frac{1}{16} of the training data. In contrast, ℒ NTP \mathcal{L}_{\rm NTP} degrades significantly when the dataset is halved.

[7] h2: 1 Introduction

[8] p: We argue that empirical scaling laws characterize typical rather than optimal training, suggesting the rigid power-law barrier is an artifact of current objectives. The core limitation is next-token prediction: a local objective that conflates surface statistical noise with global semantic signal. We propose a fundamental shift: explicitly constraining hidden state dynamics to separate the error-free semantic trajectory from this noise.

[9] p: First, we formally demonstrate that, although tokens are discrete, token sequences can be modeled by an Ordinary Differential Equation (ODE). The Picard-Lindelöf (Existence and Uniqueness) Theorem ( Coddington and Levinson, 1955 ) guarantees that if the velocity is smooth enough, there is only one possible path forward from any starting point. In other words, trajectories originating from distinct initial states will never intersect. In the context of LLMs, if the ODE model holds, this implies that error-free generations from distinct prompts maintain their semantic separation, theoretically ruling out mode collapse and preserving diversity.

[10] p: Next, we hypothesize that the Principle of Least Action ( Lanczos, 1966 ) is at work. This principle states that the path taken by a system between two points minimizes the “Action” (the integral of the Lagrangian over time), resulting in a “straight line” or geodesic on the underlying manifold. We further hypothesize that, as the manifold is an artifact of the training process, it admits a smooth structure. Consequently, the geodesics are locally linear almost everywhere. In the context of LLMs, this implies that the trajectories of error-free token sequences—and by extension, the trajectories of error-free hidden states—are confined within a tube centered along a straight line.

[11] p: We designate this structure the Semantic Tube ( Figure 1 ) and leverage it to regularize the LLM training process. The Semantic Tube posits that the noise—which causes deviations from the error-free trajectories—concentrates along the directions perpendicular to the tube. Let s < r < t s<r<t denote the indices of three tokens. We define the noise term as ( h r − h s ) ⟂ h t − h s (h_{r}-h_{s})_{\perp h_{t}-h_{s}} , representing the component of h r − h s h_{r}-h_{s} perpendicular to h t − h s h_{t}-h_{s} , and the signal term as ( h r − h s ) ∥ h t − h s (h_{r}-h_{s})_{\parallel h_{t}-h_{s}} , representing the component parallel to h t − h s h_{t}-h_{s} . Minimizing the noise term is expected to improve the Signal-to-Noise Ratio (SNR) during training. We formulate this as an auxiliary loss term, the Semantic Tube Prediction (STP) loss ℒ STP \mathcal{L}_{\rm STP} , which can be seamlessly integrated into the training objective:

[12] table: ℒ = ℒ NTP + λ ⋅ ℒ STP \mathcal{L}=\mathcal{L}_{\rm NTP}+\lambda\cdot\mathcal{L}_{\rm STP}

[13] p: where ℒ NTP \mathcal{L}_{\rm NTP} is the cross-entropy loss for Next Token Prediction (NTP) and λ \lambda is a hyperparameter controlling the strength of the STP loss.

[14] p: Semantic Tube draws inspiration from the Joint-Embedding Predictive Architecture (JEPA) ( Assran et al., 2023 ; Baevski et al., 2022 ) , which learns to predict the representation of one view based on another. In our approach, we postulate that any segment of a token sequence aligns with the global trajectory; consequently, the predictor reduces to an identity function.

[15] p: If the Geodesic Hypothesis holds, it entails the following predictions:

[16] p: (P1) ℒ NTP \mathcal{L}_{\rm NTP} alone is insufficient for high-quality generation. Consequently, we expect to observe ℒ NTP \mathcal{L}_{\rm NTP} plateau even as ℒ STP \mathcal{L}_{\rm STP} continues to decrease.

[17] p: (P2) Semantic Tube improves SNR, resulting in superior data efficiency ( Figure 1 ) and accuracy.

[18] p: (P3) Semantic Tube preserves diversity.

[19] p: (P4) We expect to see λ ≪ 1 \lambda\ll 1 to accommodate instances where the geodesic deviates from a straight line.

[20] p: (P5) The identity function serves as a superior predictor compared to learned projections.

[21] p: We conducted extensive experiments validating predictions (P1) through (P5). These results provide a strong indication that the Geodesic Hypothesis represents a simplified form of self-consistency for autoregressive sequence models. Furthermore, they confirm the validity of the noise/signal decomposition ( Figure 1 ) and establish Semantic Tube as an effective self-supervised learning objective for LLMs.

[22] h2: 2 Training and Inference Dynamics

[23] p: In this section, we formally analyze training and inference dynamics, proposing that token sequence trajectories can be modeled by an Ordinary Differential Equation (ODE) characterized by ballistic trajectories.

[24] h3: 2.1 Training ODE

[25] p: Let x ≤ t x_{\leq t} denote a token sequence of length t t , where x t x_{t} represents the t t -th token, h t h_{t} is the corresponding hidden state, and f ⁡ ( ⋅ ) f(\cdot) denotes the neural network such that h t = f ⁡ ( x ≤ t ) h_{t}=f(x_{\leq t}) . Each hidden state h t h_{t} is subsequently unembedded to predict the next token x t + 1 x_{t+1} .

[26] p: During training, the predicted token u ⁡ ( h t ) u(h_{t}) may diverge from the ground truth x t + 1 x_{t+1} ; this discrepancy constitutes the training loss. However, due to teacher forcing, we invariably feed the ground truth sequence x ≤ t + 1 x_{\leq t+1} into f ⁡ ( ⋅ ) f(\cdot) to generate h t + 1 h_{t+1} . Consequently, assuming a converged network where the loss is minimized, the training dynamics can be modeled as:

[27] table: x t + 1 \displaystyle x_{t+1} = u ̊ ∘ f ̊ ​ ( x ≤ t ) \displaystyle=\mathring{u}\circ\mathring{f}(x_{\leq t}) (1) h t \displaystyle h_{t} = f ̊ ​ ( x ≤ t ) + ϵ t \displaystyle=\mathring{f}(x_{\leq t})+\epsilon_{t} (2)

[28] p: where f ̊ \mathring{f} and u ̊ \mathring{u} represent the functions of the converged network, and ϵ t \epsilon_{t} denotes the residual unembedding error.

[29] p: If a time-indexed variable z t z_{t} follows the difference equation z t + 1 − z t = g ⁡ ( z t , t ) z_{t+1}-z_{t}=g(z_{t},t) , it can be approximated by an ODE of the form d ​ z t = g ⁡ ( z t , t ) ​ d ​ t dz_{t}=g(z_{t},t)dt . While the hidden state dynamics in Equation 2 do not fit this form (as h t + 1 h_{t+1} depends on the entire history x ≤ t x_{\leq t} rather than just h t h_{t} ), the sequence dynamics in Equation 1 do. Specifically, x ≤ t + 1 = x ≤ t ⊕ x t + 1 = x ≤ t ⊕ u ̊ ∘ f ̊ ​ ( x ≤ t ) x_{\leq t+1}=x_{\leq t}\oplus x_{t+1}=x_{\leq t}\oplus\mathring{u}\circ\mathring{f}(x_{\leq t}) , where ⊕ \oplus denotes concatenation. Letting ⊖ \ominus denote the prefix-removal operator, we obtain:

[30] table: x ≤ t + 1 ⊖ x ≤ t = u ̊ ∘ f ̊ ​ ( x ≤ t ) . x_{\leq t+1}\ominus x_{\leq t}=\mathring{u}\circ\mathring{f}(x_{\leq t}).

[31] p: This formulation closely resembles the update rule z t + 1 − z t = g ⁡ ( z t , t ) z_{t+1}-z_{t}=g(z_{t},t) , suggesting that an ODE is a plausible model for the dynamics.

[32] p: Although tokens are discrete, their embeddings lie in a continuous vector space x t ∈ ℝ d model x_{t}\in\mathbb{R}^{d_{\rm model}} . Let T T denote the maximum sequence length; then the sequence resides in ℝ T × d model \mathbb{R}^{T\times d_{\rm model}} . In Appendix A , we demonstrate that under specific arrangements, the operation x ≤ t + 1 ⊖ x ≤ t x_{\leq t+1}\ominus x_{\leq t} can be treated as vector subtraction x ≤ t + 1 − x ≤ t x_{\leq t+1}-x_{\leq t} . This leads to the following proposition:

[33] h6: Proposition 2.1 (Training ODE) .

[34] p: The LLM training process can be modeled as a solution in the token sequence space ℝ T × d model \mathbb{R}^{T\times d_{\rm model}} to the ODE:

[35] table: d ​ x ≤ t = u ̊ ∘ f ̊ ​ ( x ≤ t ) ​ d ​ t . dx_{\leq t}=\mathring{u}\circ\mathring{f}(x_{\leq t})dt.

[36] p: Proposition 2.1 models x ≤ t x_{\leq t} as following a ballistic trajectory in ℝ T × d model \mathbb{R}^{T\times d_{\rm model}} . The Picard-Lindelöf Theorem guarantees that if u ̊ ∘ f ̊ ​ ( ⋅ ) \mathring{u}\circ\mathring{f}(\cdot) and its partial derivatives with respect to x ≤ t x_{\leq t} are continuous, the ODE admits a unique solution for a given initial condition. Consequently, within this ODE framework, sequences generated from distinct prompts (initial conditions) cannot intersect, theoretically ruling out mode collapse, and preserving diversity.

[37] h3: 2.2 Mode Collapse at Inference Time

[38] p: Let h ∗ h^{\ast} denote the optimal trajectory of hidden states, defined as:

[39] table: h t ∗ = h t − ϵ t = f ̊ ​ ( x ≤ t ) h^{\ast}_{t}=h_{t}-\epsilon_{t}=\mathring{f}(x_{\leq t}) (3)

[40] p: If f ̊ ​ ( ⋅ ) \mathring{f}(\cdot) is Lipschitz-continuous ( Khalil, 2002 ) , then the trajectory h ∗ h^{\ast} is also ballistic.

[41] p: However, ℒ NTP \mathcal{L}_{\rm NTP} alone may not suffice to drive ϵ t \epsilon_{t} to zero. Recall that the goal of ℒ NTP \mathcal{L}_{\rm NTP} is to converge u ⁡ ( h t ) u(h_{t}) to x t + 1 x_{t+1} . Since the hidden state h t h_{t} is continuous while the token x t + 1 x_{t+1} is discrete, the training process can be modeled as finding the correct Voronoi cell ( Okabe et al., 2000 ) , without stipulating the exact location within the cell. This flexibility is necessary for the Picard-Lindelöf Theorem to apply: as illustrated in Figure 2 , it allows error-free geodesics ( h t ∗ h^{\ast}_{t} ) to traverse the same Voronoi cell at distinct locations, thereby avoiding intersection. Nevertheless, h t h_{t} may drift onto an incorrect geodesic within the cell, leading to mode collapse.

[42] figure: Figure 2 : Two hidden state trajectories with similar prefixes pass through the Voronoi cell of the “ researcher ” token at different locations, leading to different next hidden states and hence different next tokens. Since ℒ NTP \mathcal{L}_{\rm NTP} cannot guarantee that h t h_{t} converges to h t ∗ h^{\ast}_{t} (optimal hidden state), h t h_{t} can be misplaced on another geodesic. This leads to mode collapse (the red dotted line mistakenly continues the generation, misattributing Hinton’s Nobel Prize to an arbitrary person, or if the error deviates in the opposite direction and precludes a winner).

[43] p: This analysis indicates that ℒ NTP \mathcal{L}_{\rm NTP} alone is insufficient for generation quality, strongly motivating an additional loss term ( ℒ STP \mathcal{L}_{\rm STP} ) to explicitly minimize ϵ t \epsilon_{t} . It also implies that within the correct Voronoi cell, ℒ NTP \mathcal{L}_{\rm NTP} may plateau while ℒ STP \mathcal{L}_{\rm STP} continuously decreases. Therefore, (P1).

[44] p: In Appendix B , we demonstrate that in the infinite-width limit ( Yang and Littwin, 2021 ) , the inference process can be modeled as a Stochastic Differential Equation (SDE) with a Brownian motion term.

[45] h2: 3 Semantic Tube Prediction

[46] p: A key challenge in minimizing the error ϵ t \epsilon_{t} is that the optimal trajectory h ∗ h^{\ast} remains latent and unknown. To address this, we must postulate a structural property that allows us to estimate h ∗ h^{\ast} , leading us to the Geodesic Hypothesis. In this section, we formalize this hypothesis and subsequently introduce Semantic Tube Prediction (STP).

[47] h3: 3.1 Semantic Tube

[48] p: If the Principle of Least Action holds, the trajectories of the token sequence x ≤ t + 1 x_{\leq t+1} in Equation 1 must be geodesics, which are locally linear almost everywhere. Since h t ∗ = f ̊ ​ ( x ≤ t ) h^{\ast}_{t}=\mathring{f}(x_{\leq t}) , when f ̊ ​ ( ⋅ ) \mathring{f}(\cdot) is smooth enough, h t ∗ h^{\ast}_{t} is also expected to be locally linear almost everywhere. Hence the Geodesic Hypothesis:

[49] p: The trajectory of x ≤ t ∈ ℝ T × d model x_{\leq t}\in\mathbb{R}^{T\times d_{\rm model}} is locally linear almost everywhere. Similarly, the trajectory h t − ϵ t ∈ ℝ d h_{t}-\epsilon_{t}\in\mathbb{R}^{d} is locally linear almost everywhere.

[50] p: We first formally define local linearity. Subsequently, we demonstrate that the Semantic Tube compresses the trajectory h t h_{t} within a tube centered at h t ∗ h^{\ast}_{t} .

[51] h6: Definition 3.1 (Local Linearity) .

[52] p: A time-indexed trajectory h ∗ h^{\ast} is defined as locally linear if ∃ τ , ∃ ε \exists\tau,\exists\varepsilon such that for any time indices s < r < t s<r<t satisfying | t − s | ≤ τ |t-s|\leq\tau , we have:

[53] table: ‖ ( h r ∗ − h s ∗ ) ⟂ h t ∗ − h s ∗ ‖ 2 ≤ ε \|(h^{\ast}_{r}-h^{\ast}_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}\leq\varepsilon (4)

[54] p: where x ⟂ y x_{\perp y} denotes the component of vector x x that is perpendicular to vector y y .

[55] p: Definition 3.1 captures the intuition that if a trajectory is locally linear, each local segment can be approximated by a straight line connecting its endpoints.

[56] p: Next, we demonstrate that the Semantic Tube forces h h to approximate h ∗ h^{\ast} .

[57] h6: Lemma 3.2 (Straightening Lemma) .

[58] p: If h s = h s ∗ h_{s}=h^{\ast}_{s} , h t = h t ∗ h_{t}=h^{\ast}_{t} , and ℒ STP ≤ ϵ \mathcal{L}_{\rm STP}\leq\epsilon for all r r satisfying s < r < t s<r<t , then

[59] table: ‖ ( h r − h s ) ⟂ h t ∗ − h s ∗ ‖ 2 ≤ 2 ​ ϵ ​ ‖ h r − h s ‖ 2 . \|(h_{r}-h_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}\leq\sqrt{2\epsilon}\|h_{r}-h_{s}\|_{2}.

[60] p: Proof is deferred to Appendix D .

[61] p: Let ‖ h r − h ∗ ‖ 2 = min r ′ ⁡ ‖ h r − h r ′ ∗ ‖ 2 \|h_{r}-h^{\ast}\|_{2}=\min_{r^{\prime}}\|h_{r}-h^{\ast}_{r^{\prime}}\|_{2} denote the minimum distance from h r h_{r} to the trajectory h ∗ h^{\ast} . We establish the following theorem:

[62] h6: Theorem 3.3 (Semantic Tube) .

[63] p: If h ∗ h^{\ast} is locally linear and for all r r satisfying 0 ≤ s < r < t ≤ τ 0\leq s<r<t\leq\tau , ℒ STP → 0 \mathcal{L}_{\rm STP}\rightarrow 0 , then

[64] table: ‖ h r − h ∗ ‖ 2 ≲ ε \|h_{r}-h^{\ast}\|_{2}\lesssim\varepsilon

[65] h6: Proof Sketch.

[66] p: Only prove for the case h s = h s ∗ h_{s}=h^{\ast}_{s} and h t = h t ∗ h_{t}=h^{\ast}_{t} . In this scenario, ‖ h r − h s ‖ 2 = ‖ h r − h s ∗ ‖ \|h_{r}-h_{s}\|_{2}=\|h_{r}-h^{\ast}_{s}\| . Applying the triangle inequality yields ‖ h r − h s ∗ ‖ ≤ ‖ h r ∗ − h s ∗ ‖ 2 + ϵ r \|h_{r}-h^{\ast}_{s}\|\leq\|h^{\ast}_{r}-h^{\ast}_{s}\|_{2}+\epsilon_{r} . Notice h r ∗ h_{r}^{\ast} and h s ∗ h^{\ast}_{s} are fixed, by Lemma 3.2 , ‖ ( h r − h s ) ⟂ h t ∗ − h s ∗ ‖ 2 → 0 \|(h_{r}-h_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}\rightarrow 0 . By Definition 3.1 and the triangle inequality, it follows that ‖ h r − h ∗ ‖ 2 ≲ ε \|h_{r}-h^{\ast}\|_{2}\lesssim\varepsilon ∎

[67] p: In LLMs, it is standard to assume all sequences begin with <bos> and end with <eos> ; thus, it is reasonable to assume the boundary conditions h 0 = h 0 ∗ h_{0}=h^{\ast}_{0} and h τ = h τ ∗ h_{\tau}=h^{\ast}_{\tau} . This is formally proven in Appendix E , which completes the proof of Theorem 3.3 .

[68] p: In practice, the indices s < r < t s<r<t are selected randomly. Consequently, minimizing ℒ STP \mathcal{L}_{\rm STP} effectively drives 𝔼 ⁡ [ 1 − cos ⁡ ( h t − h r , h r − h s ) ] → 0 \mathbb{E}[1-\cos(h_{t}-h_{r},h_{r}-h_{s})]\rightarrow 0 . By Markov’s inequality, for any ϵ \epsilon , P ⁡ ( 1 − cos ⁡ ( h t − h r , h r − h s ) > ϵ ) → 0 P(1-\cos(h_{t}-h_{r},h_{r}-h_{s})>\epsilon)\rightarrow 0 . This leads to the following corollary:

[69] h6: Corollary 3.4 (Random Tube) .

[70] p: For randomly selected s < r < t s<r<t , if ℒ STP → 0 \mathcal{L}_{\rm STP}\rightarrow 0 , then for any ϵ \epsilon ,

[71] table: P ⁡ ( ‖ h r − h ∗ ‖ 2 > ε + ϵ ) → 0 P(\|h_{r}-h^{\ast}\|_{2}>\varepsilon+\epsilon)\rightarrow 0

[72] p: Corollary 3.4 implies that if ℒ STP → 0 \mathcal{L}_{\rm STP}\rightarrow 0 for a given sequence, then with high probability, the trajectory of the sequence’s hidden states is confined within a tube centered around the optimal trajectory h ∗ h^{\ast} .

[73] p: However, at inference time, the Brownian motion term diverges into a cone whose radius scales as ∝ σ t ​ t \propto\sigma_{t}\sqrt{t} , see Appendix F for details.

[74] h3: 3.2 Practical Considerations

[75] p: Since the forward pass naturally computes h s h_{s} , h r h_{r} , and h t h_{t} , the STP loss introduces negligible computational overhead—primarily the cost of computing cosine similarity. This is significantly more efficient than the fractional extra forward passes required by LLM-JEPA ( Huang et al., 2025 ) . Furthermore, because indices s s , r r , and t t can be selected randomly, STP eliminates the need for manual scaffolding of a two-view structure. In summary, STP effectively addresses the two primary limitations that have hindered the broader adoption of LLM-JEPA. Additionally, STP avoids the complexity of a predictor network (often a requirement in LLM-JEPA), as local linearity implies an identity predictor. Like LLM-JEPA, the STP loss is applied exclusively during training and is not required at inference time.

[76] p: Further implementation details are provided in Appendix G .

[77] h3: 3.3 Related Work

[78] p: Our approach addresses the classic Exposure Bias problem ( Bengio et al., 2015 ) , originally identified in recurrent neural networks (RNNs) ( Elman, 1990 ; Siegleman and Sontag, 1995 ) . The problem arises because the model is trained with Teacher Forcing ( Williams and Zipser, 1989 ) —conditioning on the ground-truth history—but must rely on its own potentially drifting predictions during inference. Although Maximum Likelihood Estimation ( ℒ NTP \mathcal{L}_{\rm NTP} in the case of LLMs) is empirically effective, Huszár (2015) argues that it optimizes an objective different from generation quality, motivating our combined loss ℒ NTP + ℒ STP \mathcal{L}_{\rm NTP}+\mathcal{L}_{\rm STP} .

[79] p: JEPAs ( Assran et al., 2023 ; Baevski et al., 2022 ) learn predictive representations across views, offering theoretical benefits ( Littwin et al., 2024 ) despite the risk of dimensional collapse ( Jing et al., 2021 ; Kenneweg et al., 2025 ) . While recent works extend these objectives to LLMs ( Barrault et al., 2024 ; Wang and Sun, 2025 ) , LLM-JEPA ( Huang et al., 2025 ) is bottlenecked by manual two-view scaffolding and the computational cost of additional forward passes, neither is a problem for ℒ STP \mathcal{L}_{\rm STP} .

[80] p: Our framework extends the philosophy of Energy-Based Models (EBMs) ( LeCun et al., 2006 ) , which learn to assign low energy to compatible configuration of variables. While EBMs and recent architectures like JEPA ( LeCun, 2022 ) typically minimize energy at specific states, our approach invokes the Principle of Least Action to minimize the action—the integral of the Lagrangian along the generation trajectory. By enforcing geodesic constraints via ℒ STP \mathcal{L}_{\rm STP} , we generalize state-wise (or local) energy minimization to trajectory-wise action minimization, ensuring the generation follows the path of least resistance.

[81] p: Scaling Laws govern the power-law relationship between compute, data, and parameters in both pre-training ( Kaplan et al., 2020 ; Hoffmann et al., 2022 ) and fine-tuning ( Zhang et al., 2024 ) . While recent data efficiency research emphasizes identifying high-density subsets ( Sorscher et al., 2022 ) or synthetic curation ( Gunasekar et al., 2023 ; Muennighoff et al., 2023 ) , ℒ STP \mathcal{L}_{\rm STP} enhances the training SNR directly, obviating the need for explicit data subset selection.

[82] p: SDE/ODE Perspective : Kong et al. (2020) interpreted ResNets as “Neural SDEs” which has a Brownian motion term. While Tong et al. (2025) recently adapted ODEs for LLMs, they model evolution across network depth (layers). Our work takes an orthogonal approach, focusing instead on the temporal dynamics of hidden states across the token sequence.

[83] p: The Linear Representation Hypothesis (LRH) ( Park et al., 2024 ; Park et al., 2025 ) posits that simple concepts are encoded as directions in the representation space, whereas the Geodesic Hypothesis suggests that both simple and composed concepts (expressed as token sequences) follow locally linear trajectories. Consequently, the vector arithmetic observed in LRH ( v → P ​ a ​ r ​ i ​ s − v → F ​ r ​ a ​ n ​ c ​ e + v → I ​ t ​ a ​ l ​ y ≈ v → R ​ o ​ m ​ e \vec{v}_{Paris}-\vec{v}_{France}+\vec{v}_{Italy}\approx\vec{v}_{Rome} ) emerges naturally from path linearity ( v → P ​ a ​ r ​ i ​ s , v → t ​ o , v → F ​ r ​ a ​ n ​ c ​ e , v → i ​ s , v → R ​ o ​ m ​ e , v → t ​ o , v → I ​ t ​ a ​ l ​ y \vec{v}_{Paris},\vec{v}_{to},\vec{v}_{France},\vec{v}_{is},\vec{v}_{Rome},\vec{v}_{to},\vec{v}_{Italy} aligns on almost a straight line, see Figure 3 ).

[84] figure: Figure 3 : When the sentence aligns on a geodesic, the concept direction naturally aligns.

[85] p: The Manifold Hypothesis ( Kiani et al., 2024 ; Robinson et al., 2025 ; Whiteley et al., 2025 ) posits that learned representations form a simple and smooth manifold. Under the Geodesic Hypothesis, this structure is a natural consequence of the Principle of Least Action.

[86] p: The Curvature Straightening Phenomenon ( Hosseini and Fedorenko, 2023 ; Hénaff et al., 2021 ) observes that the training process tends to straighten the curvature between consecutive tokens. We interpret this as a manifestation of the underlying geodesic, which approximates a straight line.

[87] p: The Neural Tangent Kernel (NTK) simplifies infinite-width dynamics ( Jacot et al., 2018 ) , a framework generalized to Transformers ( Hron et al., 2020 ; Yang and Littwin, 2021 ) and compatible feature learning regimes ( Yang and Hu, 2021 ) . While Seleznova and Kutyniok (2022) note the importance of the depth-to-width ratio, modern LLMs typically operate in the requisite width ≫ \gg depth regime.

[88] p: The application of geodesic geometry to LLMs remains underexplored, with existing studies primarily restricted to interpolating representations across models ( Deng et al., 2025 ; Yu et al., 2024 ) .

[89] h2: 4 Experiments

[90] p: We conduct extensive experiments to show the performance of Semantic Tube across models, datasets, and model sizes. We also show that accuracy barely budges when the training dataset is halved. Both accuracy and data efficiency are solid evidence that Semantic Tube improves SNR. We ablate on various setups, including LLM-JEPA style explicit two-views and curvature straightening. Lastly we show how to tune λ \lambda in practices.

[91] p: Implementing ℒ STP \mathcal{L}_{\rm STP} is straightforward with HuggingFace transformers . When computing loss, we grab per-token hidden_state h h from last layer, pick (random) indices s < r < t s<r<t , and compute 1 − cos ⁡ ( h t − h r , h r − h s ) 1-\cos(h_{t}-h_{r},h_{r}-h_{s}) . Across all experiments, we follow LLM-JEPA ( Huang et al., 2025 ) to pick 5 random seeds: 82, 23, 37, 84, and 4, and report both mean accuracy and standard deviation. This also allows us to report p p -value of paired, single-tailed t t -Test. We inherit optimal number of epochs and learning rate from LLM-JEPA. λ \lambda is separately tuned.

[92] h3: 4.1 Loss Landscape

[93] figure: (a) Loss curve (b) Loss vs. λ \lambda Figure 4 : Loss landscape. (a) When ℒ NTP \mathcal{L}_{\rm NTP} plateaus, ℒ STP \mathcal{L}_{\rm STP} continues to decrease. Furthermore, minimizing ℒ NTP \mathcal{L}_{\rm NTP} does not automatically minimize ℒ STP \mathcal{L}_{\rm STP} . (b) Across a wide range of λ \lambda , increasing λ \lambda on a logarithmic scale reduces ℒ STP \mathcal{L}_{\rm STP} linearly, while ℒ NTP \mathcal{L}_{\rm NTP} remains unchanged.

[94] p: We begin by analyzing the loss landscape by fine-tuning Llama-3.2-1B-Instruct ( Grattafiori et al., 2024 ) on the NL-RX-SYNTH ( Locascio et al., 2016 ) dataset.

[95] p: Figure 4 (a) demonstrates that in regular fine-tuning, minimizing ℒ NTP \mathcal{L}_{\rm NTP} does not automatically minimize ℒ STP \mathcal{L}_{\rm STP} . With the Semantic Tube, however, ℒ STP \mathcal{L}_{\rm STP} continues to decrease even after ℒ NTP \mathcal{L}_{\rm NTP} plateaus, corroborating (P1). Moreover, while ℒ NTP \mathcal{L}_{\rm NTP} remains comparable between regular and Semantic Tube fine-tuning, there is a significant gap in ℒ STP \mathcal{L}_{\rm STP} . This confirms that the SNR gain is driven by ℒ STP \mathcal{L}_{\rm STP} , validating the analysis in Section 2.2 that ℒ NTP \mathcal{L}_{\rm NTP} alone is insufficient for generation quality and that ℒ STP \mathcal{L}_{\rm STP} acts as a necessary complement.

[96] p: Figure 4 (b) illustrates that increasing λ \lambda on a logarithmic scale reduces ℒ STP \mathcal{L}_{\rm STP} linearly across a wide range, while ℒ NTP \mathcal{L}_{\rm NTP} remains stable. Given ℒ STP = 1 − cos ⁡ ( h t − h r , h r − h s ) \mathcal{L}_{\rm STP}=1-\cos(h_{t}-h_{r},h_{r}-h_{s}) , a value of ℒ STP > 1.0 \mathcal{L}_{\rm STP}>1.0 implies that the trajectory vector h t − h r h_{t}-h_{r} diverges significantly (essentially reversing direction) relative to h r − h s h_{r}-h_{s} . At λ = 0 \lambda=0 (regular fine-tuning), ℒ STP ≈ 1.4 \mathcal{L}_{\rm STP}\approx 1.4 indicates a trajectory resembling erratic Brownian motion. At λ = 0.08 \lambda=0.08 , ℒ STP \mathcal{L}_{\rm STP} drops to 0.6 0.6 , reflecting a substantially smoother path. Notably, while the optimal performance is achieved at λ = 0.02 \lambda=0.02 ( Table 2 ), the accuracy at λ = 0.08 \lambda=0.08 is only marginally lower ( Figure 7 ).

[97] h3: 4.2 Better Accuracy

[98] p: On Various Datasets : We first fine-tune Llama-3.2-1B-Instruct to demonstrate that Semantic Tube yields significant accuracy improvements over regular fine-tuning and LLM-JEPA across diverse datasets: NL-RX-SYNTH, NL-RX-TURK ( Locascio et al., 2016 ) , GSM8K ( Cobbe et al., 2021 ) , Spider ( Yu et al., 2018 ) , NQ-Open ( Lee et al., 2019 ) , and HellaSwag ( Zellers et al., 2019 ) . Figure 5 (a) illustrates the superior performance of Semantic Tube compared to regular fine-tuning and LLM-JEPA.

[99] figure: (a) Datasets (b) Model families (c) Model sizes Figure 5 : Semantic Tube ( ℒ NTP + ℒ STP \mathcal{L}_{\rm NTP}+\mathcal{L}_{\rm STP} , our approach) demonstrates superior performance across (a) datasets, (b) model families, and (c) model sizes compared to regular fine-tuning ( ℒ NTP \mathcal{L}_{\rm NTP} ) and LLM-JEPA ( ℒ NTP + ℒ JEPA \mathcal{L}_{\rm NTP}+\mathcal{L}_{\rm JEPA} ).

[100] p: On Various Model Families : Next, we extend our evaluation to various model families. In addition to Llama, we evaluate gemma-2-2b-it ( Team et al., 2024 ) , OpenELM-1_1B-Instruct ( Mehta et al., 2024 ) , and OLMo-2-0425-1B-Instruct ( OLMo et al., 2024 ) on NL-RX-SYNTH, as well as Qwen3-1.7B ( Yang et al., 2025 ) and DeepSeek-R1-Distill-Qwen-1.5B ( DeepSeek-AI et al., 2025 ) on GSM8K. The results are presented in Figure 5 (b).

[101] p: On Various Model Sizes : Finally, we examine scalability across model sizes using Llama-3 1B, 3B, and 8B models. Results are shown in Figure 5 (c).

[102] h3: 4.3 Data Efficiency

[103] p: Data efficiency is another crucial metric demonstrating improved SNR. We randomly select subsets of 1 2 \frac{1}{2} , 1 4 \frac{1}{4} , 1 8 \frac{1}{8} , 1 16 \frac{1}{16} , and 1 32 \frac{1}{32} of the NL-RX-SYNTH dataset and perform both Semantic Tube and regular fine-tuning on Llama-3 1B, 3B, and 8B models. To compensate for the reduced number of training steps, we scale the epochs proportionally: with a 1 n \frac{1}{n} dataset fraction, we run n × n\times epochs. For Semantic Tube, accuracy shows a negligible drop when the training dataset is halved and remains robust until the dataset is reduced to 1 16 \frac{1}{16} , at which point it matches the accuracy of regular fine-tuning on the full dataset. In contrast, regular fine-tuning suffers a significant drop immediately when the dataset is halved. See Figure 1 for 1B results and Figure 12 for 3B and 8B results.

[104] p: We also experimented with half compute ( n 2 × \frac{n}{2}\times epochs) combined with a 2 × 2\times learning rate. In both full and half compute scenarios, we also tested 2 × λ 2\times\lambda . Interestingly, although the half-compute, double-learning-rate setting does not yield optimal accuracy at 1 2 \frac{1}{2} or full training data, it performs comparatively better when the dataset fraction is < 1 2 <\frac{1}{2} .

[105] p: The improved accuracy and data efficiency provide strong evidence that Semantic Tube improves SNR (see Appendix H for formal proofs linking SNR to accuracy and data efficiency). This validates (P2) and supports the proposed noise/signal decomposition in Figure 1 , where the component perpendicular to the tube represents noise. Consequently, it supports the hypothesis that the geodesic is locally linear; otherwise, it could not be effectively approximated by the tube.

[106] h3: 4.4 Preserving Diversity

[107] p: In this section, we demonstrate that Semantic Tube preserves diversity. In the NL-RX-SYNTH dataset, some regular expressions end with “ .* ”, while others end with “ .*.* ”. Although functionally equivalent, these variations represent a nuanced preference by the dataset creator; a robust neural network should be able to learn and preserve this diversity. As shown in Table 1 , we find that regular fine-tuning struggles to learn either pattern effectively. LLM-JEPA learns the former pattern well but fails on the latter, likely because the former dominates the training set by a factor of 35 × 35\times . In contrast, Semantic Tube successfully learns both patterns. We list representative samples from the SYNTH dataset ending with either “ .* ” or “ .*.* ” in Table 3 .

[108] figure: Table 1 : Accuracy on functionally equivalent regular expression suffixes “ .* ” and “ .*.* ”. Semantic Tube effectively captures nuanced preferences, whereas LLM-JEPA exhibits mode collapse by biasing towards “ .* ”, which is 35 × \times more prevalent in the training set than “ .*.* ”. Suffix Semantic Tube Regular LLM-JEPA .* 88.5% 29.9% 68.9% .*.* 68.0% 28.0% 32.0%

[109] p: Following LLM-JEPA, we compute the singular value decomposition (SVD) of Enc ⁡ ( Text ) − Enc ⁡ ( Code ) \operatorname{Enc}(\operatorname{Text})-\operatorname{Enc}(\operatorname{Code}) to gain insight into the learned representations. Interestingly, we find ( Figure 6 ) that Semantic Tube exhibits polymorphism: when the difference vectors Enc ⁡ ( Text ) − Enc ⁡ ( Code ) \operatorname{Enc}(\operatorname{Text})-\operatorname{Enc}(\operatorname{Code}) are normalized, the singular value spectrum aligns with LLM-JEPA; however, without normalization, it closely resembles regular fine-tuning. This indicates that Semantic Tube enforces structure on the directions (normalized vectors) while tolerating complexity on the raw vectors. We conjecture that this mechanism allows Semantic Tube to maintain flexibility and preserve diversity.

[110] figure: (a) Without Normalization (b) With Normalization Figure 6 : SVD decomposition demonstrating Semantic Tube’s polymorphism. (a) Without normalization, the SVD profile closely resembles regular fine-tuning. (b) With normalization, the SVD aligns with LLM-JEPA. Collectively, this indicates that Semantic Tube enforces a simple structure on the directions (normalized vectors) mapping Text {\rm Text} to Code {\rm Code} , while tolerating complexity in the unnormalized vectors. Note that the relative relationships among the base model, regular fine-tuning, and LLM-JEPA remain unchanged with or without normalization.

[111] p: Collectively, these results validate (P3).

[112] h3: 4.5 Tuning λ \lambda

[113] p: Semantic Tube introduces a single hyperparameter, λ \lambda . Empirically, we observe that the accuracy vs. λ \lambda curve is concave ( Figure 7 ), typically peaking between 0.01 0.01 and 0.08 0.08 ( Table 2 ). Notably, this behavior persists across other variations (see Section 4.6 ): the accuracy curves remain concave, and the optimal λ \lambda consistently falls within the 0.01 0.01 – 0.08 0.08 range (see Figure 13 ). This validates (P4).

[114] figure: Figure 7 : Impact of λ \lambda tuning on Llama-3 1B across various datasets. In most cases, peak performance is achieved within the range of 0.01 0.01 to 0.08 0.08 .

[115] figure: Table 2 : Optimal λ \lambda values yielding maximum accuracy. SYNTH TURK GSM8K Spider NQ HS 0.02 0.04 0.005 0.04 0.16 0.02 Gemma2 Qwen3 R1 Dist OLMo OpenELM 0.005 0.02 0.04 0.01 0.04 Llama3 3B Llama3 8B 0.01 0.0025

[116] h3: 4.6 Ablation

[117] p: We conducted extensive ablation studies on design decisions, establishing that ℒ STP \mathcal{L}_{\rm STP} yields superior performance compared to all variations ( Figure 8 ). Full details are provided in Appendix L . We specifically note that the Pred variant—which trains a linear projector P P to minimize ℒ STP = 1 − cos ⁡ ( P ⁡ ( h r − h s ) , h t − h r ) \mathcal{L}_{\rm STP}=1-\cos(P(h_{r}-h_{s}),h_{t}-h_{r}) —results in degraded performance in all configurations. This validates (P5).

[118] figure: Figure 8 : Ablation study. Semantic Tube (our approach) outperforms all variations. Within the Semantic Tube family, alternative configurations consistently degrade performance.

[119] h2: 5 Conclusion

[120] p: This paper proposes the Geodesic Hypothesis, which posits that token sequence trajectories on the LLM manifold are locally linear geodesics. Based on it, we introduce Semantic Tube Prediction (STP)—a learning objective complementary to Next Token Prediction—which compresses hidden state trajectories into a signal-rich tube centered on the geodesic. Our approach generalizes LLM-JEPA by eliminating the need for manual scaffolding of two-view structures, additional compute, or auxiliary predictors. Empirically, STP significantly improves Signal-to-Noise Ratio, allowing models to maintain accuracy even when training data is reduced to 1 16 \frac{1}{16} , thereby challenging standard Power Law scaling. Our framework unifies the Linear Representation and Manifold Hypotheses under the Principle of Least Action.

[121] h2: Impact Statement

[122] p: This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

[123] h2: References

[124] h2: Appendix A Training ODE

[125] p: In this section, we present a form of u ⁡ ( ⋅ ) u(\cdot) and f ⁡ ( ⋅ ) f(\cdot) such that x ≤ t + 1 ⊖ x ≤ t = x ≤ t + 1 − x ≤ t x_{\leq t+1}\ominus x_{\leq t}=x_{\leq t+1}-x_{\leq t} . Throughout the section, we slightly abuse notation by letting x t x_{t} denote both a token and its embedding vector x t ∈ ℝ d model x_{t}\in\mathbb{R}^{d_{\rm model}} , and letting x ≤ t x_{\leq t} denote both a token sequence and its embedding vector x ≤ t ∈ ℝ T × d model x_{\leq t}\in\mathbb{R}^{T\times d_{\rm model}} :

[126] table: x ≤ t = [ x 1 , … , x t , 0 , … , 0 ] . x_{\leq t}=[x_{1},...,x_{t},0,...,0].

[127] p: Let f ⁡ ( x ≤ t ) ∈ ℝ d f(x_{\leq t})\in\mathbb{R}^{d} . Let u ⁡ ( ⋅ ) : ℝ d → ℝ d model u(\cdot):\mathbb{R}^{d}\rightarrow\mathbb{R}^{d_{\rm model}} be the unembedding function that maps the hidden state back to the token embedding.

[128] p: Note that we need a function to lift u ⁡ ( f ⁡ ( x ≤ t ) ) u(f(x_{\leq t})) from ℝ d model \mathbb{R}^{d_{\rm model}} to ℝ T × d model \mathbb{R}^{T\times d_{\rm model}} . Define v ⁡ ( ⋅ , ⋅ ) : ℝ d model × ℕ → ℝ T × d model v(\cdot,\cdot):\mathbb{R}^{d_{\rm model}}\times\mathbb{N}\rightarrow\mathbb{R}^{T\times d_{\rm model}} such that

[129] table: v ⁡ ( x , t ) = [ 0 , … , 0 , x ⏟ index ​ t + 1 , 0 , … , 0 ] v(x,t)=[0,...,0,\underbrace{x}_{{\rm index}\ t+1},0,...,0]

[130] p: Hence, we have

[131] table: x ≤ t + 1 = v ⁡ ( u ⁡ ( f ⁡ ( x ≤ t ) ) , t ) x_{\leq t+1}=v(u(f(x_{\leq t})),t)

[132] p: Define the ⊖ \ominus operator as

[133] table: x ≤ t + 1 ⊖ x ≤ t = v ⁡ ( x t + 1 , t ) x_{\leq t+1}\ominus x_{\leq t}=v(x_{t+1},t)

[134] p: By the definition of v ⁡ ( ⋅ , ⋅ ) v(\cdot,\cdot) , we have

[135] table: x ≤ t + 1 ⊖ x ≤ t = x ≤ t + 1 − x ≤ t x_{\leq t+1}\ominus x_{\leq t}=x_{\leq t+1}-x_{\leq t}

[136] p: Note that the network is now in the form v ⁡ ( u ⁡ ( f ⁡ ( x ≤ t ) ) , t ) v(u(f(x_{\leq t})),t) , which can be written as g ⁡ ( x ≤ t , t ) g(x_{\leq t},t) and satisfies the formulation of an ODE.

[137] h2: Appendix B Inference SDE

[138] p: At training time, the unembedding error ϵ t \epsilon_{t} does not propagate to the next token. However, at inference time, h t + 1 h_{t+1} depends (indirectly) on h t h_{t} , causing ϵ t \epsilon_{t} to accumulate into a Brownian motion term.

[139] p: Yang and Littwin (2021) established that in the limit of infinite width, the pre-activations of a neural network (and thus the hidden state) are well-approximated by Gaussian processes. Hence, we can assume ϵ t \epsilon_{t} are i.i.d. Gaussian. Furthermore, as shown by ( Yang and Littwin, 2021 ) , ϵ t \epsilon_{t} remains i.i.d. Gaussian when passed through a randomly initialized neural network, which remains constant in the infinite-width limit. Consequently, ϵ t \epsilon_{t} accumulates to form a Brownian motion term d ​ W t dW_{t} . Thus the inference process can be modeled by a Stochastic Differential Equation (SDE).

[140] h6: Proposition B.1 (Inference SDE) .

[141] p: The inference process of an LLM can be modeled by an SDE in the token sequence space ℝ T × d model \mathbb{R}^{T\times d_{\rm model}} ,

[142] table: d ​ x ≤ t = u ̊ ∘ f ̊ ​ ( x ≤ t ) ​ d ​ t + σ t ​ d ​ W t dx_{\leq t}=\mathring{u}\circ\mathring{f}(x_{\leq t})dt+\sigma_{t}dW_{t}

[143] p: Consider the example in Figure 2 , if the Brownian motion shifts the top trajectory to the bottom, mode collapse occurs. Conversely, if the bottom trajectory shifts to the top, mode collapse occurs. This motivates the construction of an approach to explicitly suppress ϵ t \epsilon_{t} . Indeed, Section 4.1 demonstrates that next token prediction alone is insufficient for high-quality generation, making our approach a necessary complement.

[144] h2: Appendix C Context-Aware Hidden State

[145] p: We can view h t − h s h_{t}-h_{s} as the semantic evolution induced by the sub-sequence x [ s , t ] x_{[s,t]} given the context x ≤ s x_{\leq s} . In this sense, h t − h s h_{t}-h_{s} acts as a context-aware hidden state transition, which is significantly more informative than the static hidden state of the isolated sub-sequence x [ s , t ] x_{[s,t]} .

[146] p: For example, given the prefix v → The , v → capital , v → of \vec{v}_{\rm The},\vec{v}_{\rm capital},\vec{v}_{\rm of} , appending the token v → France \vec{v}_{\rm France} shifts the overall semantic trajectory toward v → P ​ a ​ r ​ i ​ s \vec{v}_{Paris} . However, given a different prefix v → The , v → language , v → of \vec{v}_{\rm The},\vec{v}_{\rm language},\vec{v}_{\rm of} , appending the same token v → F ​ r ​ a ​ n ​ c ​ e \vec{v}_{France} shifts the trajectory toward v → F ​ r ​ e ​ n ​ c ​ h \vec{v}_{French} . If we were to compute the hidden state of v → F ​ r ​ a ​ n ​ c ​ e \vec{v}_{France} in isolation, we would lose this contextual nuance and fail to capture the context-specific semantic semantic shift.

[147] figure: Figure 9 : The same token v → F ​ r ​ a ​ n ​ c ​ e \vec{v}_{France} directs the geodesic along different concept directions when appended to distinct prefixes, illustrating the necessity of the context-aware state difference h t − h s h_{t}-h_{s} .

[148] p: Thus, h t − h s h_{t}-h_{s} serves as a context-aware representation of the added information.

[149] h2: Appendix D Proof of the Straightening Lemma

[150] p: In this section, we provide the proof for Lemma 3.2 . The objective is to show

[151] table: ‖ ( h r − h s ) ⟂ h t ∗ − h s ∗ ‖ 2 ≤ 2 ​ ϵ ​ ‖ h r − h s ‖ 2 . \|(h_{r}-h_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}\leq\sqrt{2\epsilon}\|h_{r}-h_{s}\|_{2}.

[152] figure: Figure 10 : Geometric illustration for the proof of Lemma 3.2

[153] p: Referring to Figure 10 , we have

[154] table: ‖ ( h r − h s ) ⟂ h t ∗ − h s ∗ ‖ 2 = ‖ h r − h s ‖ 2 ⋅ sin ⁡ θ \|(h_{r}-h_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}=\|h_{r}-h_{s}\|_{2}\cdot\sin\theta

[155] p: Since θ ′ ≥ θ \theta^{\prime}\geq\theta , it follows that

[156] table: ‖ ( h r − h s ) ⟂ h t ∗ − h s ∗ ‖ 2 ≤ ‖ h r − h s ‖ 2 ⋅ sin ⁡ θ ′ \|(h_{r}-h_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}\leq\|h_{r}-h_{s}\|_{2}\cdot\sin\theta^{\prime}

[157] p: We also have

[158] table: ℒ STP = 1 − cos ⁡ θ ′ ≤ ϵ \mathcal{L}_{\rm STP}=1-\cos\theta^{\prime}\leq\epsilon

[159] p: When ϵ \epsilon is sufficiently small, we can approximate cos ⁡ θ ′ ≈ 1 − θ ′ 2 2 \cos\theta^{\prime}\approx 1-\frac{\theta^{\prime 2}}{2} . Hence

[160] table: θ ′ 2 2 ≲ ϵ \frac{\theta^{\prime 2}}{2}\lesssim\epsilon

[161] p: Rearranging gives

[162] table: θ ′ ≲ 2 ​ ϵ \theta^{\prime}\lesssim\sqrt{2\epsilon}

[163] p: Also, when θ ′ \theta^{\prime} is sufficiently small, sin ⁡ θ ′ ≈ θ ′ \sin\theta^{\prime}\approx\theta^{\prime} . Therefore

[164] table: ‖ ( h r − h s ) ⟂ h t ∗ − h s ∗ ‖ 2 ≤ ‖ h r − h s ‖ 2 ⋅ sin ⁡ θ ′ ≲ 2 ​ ϵ ​ ‖ h r − h s ‖ 2 . □ \|(h_{r}-h_{s})_{\perp h^{\ast}_{t}-h^{\ast}_{s}}\|_{2}\leq\|h_{r}-h_{s}\|_{2}\cdot\sin\theta^{\prime}\lesssim\sqrt{2\epsilon}\|h_{r}-h_{s}\|_{2}.\quad\quad\quad\square

[165] h2: Appendix E Proof of the Semantic Tube Theorem

[166] p: We introduce two auxiliary tokens, <before-bos> and <after-eos> . The token <before-bos> appears only at the 0-th position and always precedes <bos> , while <after-eos> appears only at the τ + 1 \tau+1 -th position and always follows <eos> . This augmentation increases the total sequence length from τ \tau to τ + 2 \tau+2 . By anchoring the sequence with <before-bos> and <after-eos> , we ensure that the boundary conditions h 0 = h 0 ∗ h_{0}=h^{\ast}_{0} and h τ + 1 = h τ + 1 ∗ h_{\tau+1}=h^{\ast}_{\tau+1} are satisfied.

[167] p: The proof follows from these conditions. □ \square

[168] h2: Appendix F Inference Cone

[169] p: As STP explicitly reduces ϵ t \epsilon_{t} , it lowers σ t \sigma_{t} in the Brownian Motion term of Proposition B.1 . At inference time, the Brownian motion term causes the token sequence trajectory diverge into a cone whose radius grows at a rate ∝ σ t ​ t \propto\sigma_{t}\sqrt{t} . A lower σ t \sigma_{t} reduces the probability that the cone collides with another token sequence, which would causes mode collapse ( Figure 11 ).

[170] figure: Figure 11 : The inference cone defines the probabilistic range of a Brownian motion, and its radius grows ∝ σ t ​ t \propto\sigma_{t}\sqrt{t} . A larger σ t \sigma_{t} leads to a wider cone, which has a high probability of colliding with a token sequence trace that is far away (blue cone and green geodesic), while a smaller σ t \sigma_{t} leads to a narrower cone that may only collide with a nearby trace (yellow cone and red geodesic). The dotted red and green fine lines are the Brownian motions confined by the yellow and blue cones, respectively.

[171] h6: Proposition F.1 (Inference Cone) .

[172] p: The distortion between h t h_{t} and h t ∗ h^{\ast}_{t} behaves as a Gaussian process, where the scale of the deviation grows as ‖ h t − h t ∗ ‖ 2 ∝ σ ​ t \|h_{t}-h^{\ast}_{t}\|_{2}\propto\sigma\sqrt{t}

[173] h6: Proof.

[174] p: According to Proposition B.1 , at inference time, we model the token sequence trajectory as following an SDE d ​ x ≤ t = u ̊ ∘ f ̊ ​ ( x ≤ t ) ​ d ​ t + σ t ​ d ​ W t dx_{\leq t}=\mathring{u}\circ\mathring{f}(x_{\leq t})dt+\sigma_{t}dW_{t} , where σ t ​ d ​ W t \sigma_{t}dW_{t} is a Brownian motion. Let h t = f ̊ ​ ( x ≤ t ) h_{t}=\mathring{f}(x_{\leq t}) be the hidden state. Let x ≤ t ∗ x^{\ast}_{\leq t} be the error-free generation satisfying d ​ x ≤ t ∗ = u ̊ ∘ f ̊ ​ ( x ≤ t ∗ ) ​ d ​ t dx^{\ast}_{\leq t}=\mathring{u}\circ\mathring{f}(x^{\ast}_{\leq t})dt , and let h t ∗ = f ̊ ​ ( x ≤ t ∗ ) h^{\ast}_{t}=\mathring{f}(x^{\ast}_{\leq t}) be the error-free hidden state. We can quantify the distortion between h t h_{t} and h t ∗ h^{\ast}_{t} by examining how the Brownian motion is transformed by f ̊ \mathring{f} .

[175] p: Yang and Littwin (2021) establishes that in the infinite-width limit, f ̊ \mathring{f} converges to a Neural Tangent Kernel (NTK) determined by random initialization. It further showed that Gaussian noise remains Gaussian when passed through a randomly initialized network. Hence, a Brownian motion remains a Brownian motion when passed through f ̊ \mathring{f} . Therefore,

[176] table: h t − h t ∗ = ∑ s ≤ t ϵ s h_{t}-h^{\ast}_{t}\ =\sum_{s\leq t}\epsilon_{s}

[177] p: where ϵ s \epsilon_{s} are Gaussian noises. By Donsker’s theorem, when t → ∞ t\rightarrow\infty , 1 t ​ ∑ s ≤ t ϵ s ∼ N ⁡ ( 0 , Σ ) \frac{1}{\sqrt{t}}\sum_{s\leq t}\epsilon_{s}\sim N(0,\Sigma) . Consequently, the magnitude of the distortion scales as

[178] table: ‖ ∑ s ≤ t ϵ s ‖ 2 ∝ σ ​ t . \left\|\sum_{s\leq t}\epsilon_{s}\right\|_{2}\propto\sigma\sqrt{t}.

[179] p: Putting everything together, the distortion between h t h_{t} and h t ∗ h^{\ast}_{t} satisfies ‖ h t − h t ∗ ‖ 2 ∝ σ ​ t \|h_{t}-h^{\ast}_{t}\|_{2}\propto\sigma\sqrt{t} ∎

[180] p: Proposition F.1 implies that with high probability, the trajectory of the generated hidden state h h is confined within a cone centered at h ∗ h^{\ast} whose radius grows at a rate ∝ σ ​ t \propto\sigma\sqrt{t} .

[181] p: When mode collapse occurs at inference time, i.e., a generated sequence x ≤ t x_{\leq t} collides with y ≤ t ′ y_{\leq t^{\prime}} , then their corresponding hidden states h h and g g must collide. Let ‖ h ∗ − g ∗ ‖ 2 \|h^{\ast}-g^{\ast}\|_{2} be the minimum distance between h ∗ h^{\ast} and g ∗ g^{\ast} . By Proposition F.1 , ∀ ε > 0 \forall\varepsilon>0 , ∃ c \exists c ,

[182] table: P ⁡ ( ‖ h ∗ − g ∗ ‖ 2 > c ⋅ σ ​ t ) ≤ ε P(\|h^{\ast}-g^{\ast}\|_{2}>c\cdot\sigma\sqrt{t})\leq\varepsilon

[183] p: On the other hand, ℒ STP \mathcal{L}_{\rm STP} suppresses ϵ t \epsilon_{t} and consequently reduces σ \sigma , which decreases the lower bound of the probability of mode collapse.

[184] h2: Appendix G Implementation Details

[185] p: If the training data already possesses a two-view structure, such as a ( q ​ u ​ e ​ r ​ y , a ​ n ​ s ​ w ​ e ​ r ) (query,answer) pair, one can leverage it by anchoring s s at the beginning of the q ​ u ​ e ​ r ​ y query and t t at the end of the a ​ n ​ s ​ w ​ e ​ r answer . However, we suggest that r r should be randomly selected to maximize the benefit of the STP loss. As demonstrated in our ablation study, fixing r r at the end of the q ​ u ​ e ​ r ​ y query yields lower accuracy.

[186] p: Typically, h t − h s h_{t}-h_{s} does not equal the hidden state of the isolated sub-sequence x [ s , t ] x_{[s,t]} . However, as discussed Appendix C , we can view h t − h s h_{t}-h_{s} as the semantic evolution induced by the sub-sequence x [ s , t ] x_{[s,t]} given the context x ≤ s x_{\leq s} . In this sense, h t − h s h_{t}-h_{s} acts as a context-aware hidden state, which is significantly more informative than the hidden state of x [ s , t ] x_{[s,t]} computed in isolation. For example, given the prefix v → The , v → capital , v → of \vec{v}_{\rm The},\vec{v}_{\rm capital},\vec{v}_{\rm of} , appending the token v → France \vec{v}_{\rm France} shifts the overall meaning to v → Paris \vec{v}_{\rm Paris} . Conversely, given the prefix v → The , v → language , v → of \vec{v}_{\rm The},\vec{v}_{\rm language},\vec{v}_{\rm of} , appending v → France \vec{v}_{\rm France} shifts the meaning to v → French \vec{v}_{\rm French} . Computing the hidden state of v → France \vec{v}_{\rm France} separately loses this context and fails to capture the context-specific meaning of the tokens (see Figure 9 ).

[187] p: We can also leverage h t − h s h_{t}-h_{s} to bypass unwanted tokens. For example, setting s > 0 s>0 allows us to skip the system prompt. Similarly, in multiple-choice Q&A, distractor choices that are semantically inconsistent with the q ​ u ​ e ​ r ​ y query are often located between the q ​ u ​ e ​ r ​ y query and the correct a ​ n ​ s ​ w ​ e ​ r answer . In such cases, we can pick r r and r ′ r^{\prime} such that x [ s , r ] x_{[s,r]} is the q ​ u ​ e ​ r ​ y query and x [ r ′ , t ] x_{[r^{\prime},t]} is the correct a ​ n ​ s ​ w ​ e ​ r answer , computing the STP loss as:

[188] table: ℒ STP = 1 − cos ⁡ ( h t − h r ′ , h r − h s ) . \mathcal{L}_{\rm STP}=1-\cos(h_{t}-h_{r}^{\prime},h_{r}-h_{s}).

[189] p: This formulation effectively skips the irrelevant choice branches in the middle.

[190] p: Finally, the STP loss assumes that h s h_{s} , h r h_{r} , and h t h_{t} are collinear, which may not hold strictly in reality as geodesics can exhibit curvature. In practice, this implies that we must select a small λ \lambda to tolerate the angular deviation between h t − h r h_{t}-h_{r} and h r − h s h_{r}-h_{s} . Indeed, our experiments consistently show that λ ≈ 0.01 \lambda\approx 0.01 is effective across various models, datasets, and model sizes.

[191] h2: Appendix H Signal-to-Noise Ratio

[192] p: Directly measuring Signal-to-Noise Ratio (SNR) in the latent representations of LLMs is intractable. In self-supervised learning, the decomposition of activations into “semantic signal” and “nuisance noise” is not explicitly observable without access to the ground-truth data manifold.

[193] p: In this subsection, we formally show an information theoretic link between SNR and data efficiency and training accuracy. Hence we can validate our hypothesis via the predicted impact on them.

[194] p: We model LLM training process as extracting information about a discrete target Y Y (tokens) from continuous latent representations X X (hidden states). Let Y ∈ 𝒱 Y\in\mathcal{V} be the discrete target token from a vocabulary of size | 𝒱 | |\mathcal{V}| . Let X m = { X i , 1 ≤ i ≤ m } X^{m}=\{X_{i},1\leq i\leq m\} be a set of m m hidden states that are conditionally i.i.d. given Y Y . The training objective is to minimize cross-entropy, which is asymptotically equivalent to minimizing the conditional entropy H ⁡ ( Y | X m ) H(Y|X^{m}) .

[195] h6: Lemma H.1 (Data Efficiency) .

[196] table: H ⁡ ( Y | X m ) ≥ H ⁡ ( Y ) − m ⋅ I ⁡ ( Y , X ) H(Y|X^{m})\geq H(Y)-m\cdot I(Y;X) (5)

[197] h6: Proof.

[198] p: The goal is to show:

[199] table: H ⁡ ( Y | X m ) ≥ H ⁡ ( Y ) − m ​ I ​ ( X , Y ) H(Y|X^{m})\geq H(Y)-mI(X;Y)

[200] p: By the definition of Mutual Information:

[201] table: H ⁡ ( Y | X m ) = H ⁡ ( Y ) − I ⁡ ( Y , X m ) H(Y|X^{m})=H(Y)-I(Y;X^{m})

[202] p: We need to bound I ⁡ ( Y , X m ) I(Y;X^{m}) . Apply chain rule of mutual information,

[203] table: I ⁡ ( Y , X m ) = H ⁡ ( X m ) − H ⁡ ( X m | Y ) I(Y;X^{m})=H(X^{m})-H(X^{m}|Y)

[204] p: Since X i X_{i} are conditionally independent given Y Y :

[205] table: H ⁡ ( X m | Y ) = ∑ i = 1 m H ⁡ ( X i | Y ) H(X^{m}|Y)=\sum_{i=1}^{m}H(X_{i}|Y)

[206] p: For the first term H ⁡ ( X m ) H(X^{m}) , by sub-additivity of entropy, the entropy of the joint distribution is always less than or equal to the sum of individual entropies (independence maximizes entropy):

[207] table: H ⁡ ( X m ) ≤ ∑ i = 1 m H ⁡ ( X i ) H(X^{m})\leq\sum_{i=1}^{m}H(X_{i})

[208] p: Substitute these back into the Mutual Information expansion:

[209] table: I ⁡ ( Y , X m ) ≤ ∑ i = 1 m H ⁡ ( X i ) − ∑ i = 1 m H ⁡ ( X i | Y ) I(Y;X^{m})\leq\sum_{i=1}^{m}H(X_{i})-\sum_{i=1}^{m}H(X_{i}|Y)

[210] table: I ⁡ ( Y , X m ) ≤ ∑ i = 1 m ( H ⁡ ( X i ) − H ⁡ ( X i | Y ) ) I(Y;X^{m})\leq\sum_{i=1}^{m}\left(H(X_{i})-H(X_{i}|Y)\right)

[211] table: I ⁡ ( Y , X m ) ≤ ∑ i = 1 m I ⁡ ( Y , X i ) I(Y;X^{m})\leq\sum_{i=1}^{m}I(Y;X_{i})

[212] p: Since X i X_{i} are identically distributed, I ⁡ ( Y , X i ) I(Y;X_{i}) is the same for all i i :

[213] table: I ⁡ ( Y , X m ) ≤ m ⋅ I ⁡ ( Y , X ) I(Y;X^{m})\leq m\cdot I(Y;X)

[214] p: Finally substitute this upper bound on Information back into step 1. Since we are subtracting a larger value, the result is a lower bound on entropy:

[215] table: H ⁡ ( Y | X m ) = H ⁡ ( Y ) − I ⁡ ( Y , X m ) ≥ H ⁡ ( Y ) − m ⋅ I ⁡ ( Y , X ) H(Y|X^{m})=H(Y)-I(Y;X^{m})\geq H(Y)-m\cdot I(Y;X)

[216] p: ∎

[217] p: Suppose H ⁡ ( Y | X m ) ≤ ϵ H(Y|X^{m})\leq\epsilon after training, we have

[218] table: ϵ ≥ H ⁡ ( Y | X m ) ≥ H ⁡ ( Y ) − m ⋅ I ⁡ ( Y , X ) \epsilon\geq H(Y|X^{m})\geq H(Y)-m\cdot I(Y;X)

[219] p: Recent theoretical work on infinite-width limits ( Yang and Littwin, 2021 ) establishes that layer pre-activations converge to Gaussian distributions. Motivated by this, we model the local representation dynamics using a canonical Gaussian Channel approximation with additive noise. Specifically, we decompose X = Z + N X=Z+N , where Z Z is the latent signal, and N ∼ 𝒩 ⁡ ( 0 , σ 2 ​ I ) N\sim\mathcal{N}(0,\sigma^{2}I) is the additive Gaussian noise. We define the Signal-to-Noise Ratio as

[220] table: SNR = 𝔼 ⁡ [ ‖ Z ‖ 2 ] 𝔼 ⁡ [ ‖ N ‖ 2 ] {\rm SNR}=\frac{\mathbb{E}[\|Z\|^{2}]}{\mathbb{E}[\|N\|^{2}]}

[221] p: Under the Gaussian channel approximation, mutual information is a logarithmic function of SNR ( Shannon, 1948 ) :

[222] table: I ⁡ ( X , Y ) = 1 2 ​ log ⁡ ( 1 + SNR ) I(X;Y)=\frac{1}{2}\log(1+\rm{SNR})

[223] p: Substituting this capacity into Lemma H.1 , we have

[224] h6: Corollary H.2 (Signal-to-Noise Ratio) .

[225] table: m ≥ H ⁡ ( Y ) − ϵ 1 2 ​ log ⁡ ( 1 + SNR ) m\geq\frac{H(Y)-\epsilon}{\frac{1}{2}\log(1+{\rm SNR})} (6)

[226] p: Corollary H.2 indicates that m m is inversely proportional to log ⁡ ( 1 + SNR ) \log(1+{\rm SNR}) . Consequently, if the Semantic Tube works as expected, it will increase SNR and strictly lower the data requirement m m .

[227] p: Let Y ^ = f ⁡ ( X m ) \hat{Y}=f(X^{m}) be the estimator of Y Y produced by the model. Let P e = P ⁡ ( Y ^ ≠ Y ) P_{e}=P(\hat{Y}\neq Y) be the probability of error (incorrect token generation). Fano’s Inequality ( Cover and Thomas, 1991 ) provides a lower bound on the conditional entropy H ⁡ ( Y | X m ) H(Y|X^{m}) in terms of the error probability:

[228] table: H ⁡ ( Y | X m ) ≤ H b ​ ( P e ) + P e ​ log ⁡ ( | 𝒱 | − 1 ) H(Y|X^{m})\leq H_{b}(P_{e})+P_{e}\log(|\mathcal{V}|-1)

[229] p: where H b ​ ( P e ) H_{b}(P_{e}) is the binary entropy function. For LLMs, | 𝒱 | ≫ 1 |\mathcal{V}|\gg 1 , the term P e ​ log ⁡ | 𝒱 | P_{e}\log|\mathcal{V}| dominates H b ​ ( P e ) H_{b}(P_{e}) . Hence we can simplify Fano’s inequality to be:

[230] table: H ⁡ ( Y | X m ) ≤ P e ​ log ⁡ ( | 𝒱 | − 1 ) H(Y|X^{m})\leq P_{e}\log(|\mathcal{V}|-1) (7)

[231] p: Plug Equation 5 into Equation 7 , immediate we get

[232] h6: Corollary H.3 (Accuracy) .

[233] table: P e ≳ H ⁡ ( Y ) − m ⋅ 1 2 ​ log ⁡ ( 1 + SNR ) log ⁡ | 𝒱 | P_{e}\gtrsim\frac{H(Y)-m\cdot\frac{1}{2}\log(1+{\rm SNR})}{\log|\mathcal{V}|} (8)

[234] p: Equation 8 indicates that if we observe significant improvement on training accuracy, we know that SNR is higher.

[235] h2: Appendix I Data Efficiency

[236] p: In this section we present the results of experiments on Llama3 3B and 8B using 1 2 \frac{1}{2} , 1 4 \frac{1}{4} , 1 8 \frac{1}{8} , 1 16 \frac{1}{16} , and 1 32 \frac{1}{32} of the dataset in Figure 12 , where we see similar trend as in Llama3 1B ( Figure 1 ).

[237] figure: (a) Llama3 3B (b) Llama3 8B Figure 12 : Semantic Tube (our approach) and regular fine-tuning with 1 2 \frac{1}{2} , 1 4 \frac{1}{4} , 1 8 \frac{1}{8} , 1 16 \frac{1}{16} , and 1 32 \frac{1}{32} dataset on (a) Llama3 3B and (b) Llama3 8B.

[238] h2: Appendix J Regular Expression Samples

[239] p: We list in Table 3 a few samples from the SYNTH dataset that end with either “ .* ” or “ .*.* ”, which are functionally equivalent.

[240] figure: Table 3 : Regular expression samples from the SYNTH dataset that end with either “ .* ” or “ .*.* ”, which are functionally equivalent. Regular Expressions .*([a-z]) | | ([AEIOUaeiou]) | | ([A-Za-z]).* .*([A-Za-z]).*([0-9]).*.* ((dog)(.*)).*([AEIOUaeiou]).* (dog).*((truck) | | ([A-Z]) | | ([0-9])).* .*(.)&([0-9])&(dog).* .*(dog).*((.)*).*.* .*dog.*[a-z].*.*

[241] h2: Appendix K Tuning λ \lambda

[242] p: In this section, we present the accuracy vs. λ \lambda curves for the various configurations of Semantic Tubes, Two Views, and Mask detailed in Section 4.6 . As shown in Figure 13 , we observe across all cases that the curve is concave, most of the time with a maximum reached at λ \lambda values between 0.01 0.01 and 0.8 0.8 . Furthermore, when λ \lambda exceeds the optimal value, we occasionally observe a precipitous drop in accuracy accompanied by a drastic increase in standard deviation. Collectively, these results provide strong evidence supporting the validity of (P4).

[243] figure: (a) Semantic Tube (b) Two Views (c) Mask Figure 13 : Tuning λ \lambda for various configurations of (a) Semantic Tube, (b) Two Views, and (c) Mask. In all cases, the accuracy vs. λ \lambda curve is concave. We also observe that when λ \lambda exceeds the optimal value, accuracy declines rapidly while the standard deviation increases sharply, indicating that λ ≪ 1 \lambda\ll 1 is preferred.

[244] h2: Appendix L Ablation

[245] p: Semantic Tube : We ablate several variations of the Semantic Tube configuration:

[246] p: Zero : Instead of randomly picking s s , this variation fixes the start index s = 0 s=0 . The loss becomes ℒ STP = 1 − cos ⁡ ( h r − h 0 , h t − h r ) \mathcal{L}_{\rm STP}=1-\cos(h_{r}-h_{0},h_{t}-h_{r}) .

[247] p: Pred : We introduce a learnable linear projector P P and modify the loss to ℒ STP = 1 − cos ⁡ ( P ⁡ ( h r − h s ) , h t − h s ) \mathcal{L}_{\rm STP}=1-\cos(P(h_{r}-h_{s}),h_{t}-h_{s}) . aligns the approach more closely with the JEPA style, utlizing a non-identity predictor. P P is randomly initialized and trained during fine-tuning.

[248] p: Inst : We incorporate instructions into the token sequence x ≤ t x_{\leq t} . These instructions consist of system prompt such as "Convert natural language to regular expression" .

[249] p: Two Views : This configuration adopts the LLM-JEPA style two-view structure, where query and answer represent two views of the same concept. Note that we retain the ℒ STP \mathcal{L}_{\rm STP} formulation but fix s = 0 s=0 and set r r to the index of the last token of the query .

[250] p: Warmup : We linearly warm up λ \lambda throughout the training process.

[251] p: Pred : Identical to the Pred variation in the Semantic Tube configuration.

[252] p: Mean : Instead of the difference vector h r − h s h_{r}-h_{s} , we use the average embedding 1 r − s + 1 ​ ∑ s ≤ i ≤ r h i \frac{1}{r-s+1}\sum_{s\leq i\leq r}h_{i} . Consequently, the loss becomes ℒ STP = 1 − cos ⁡ ( 1 r − s + 1 ​ ∑ s ≤ i ≤ r h i , 1 t − r + 1 ​ ∑ r ≤ j ≤ t h j ) \mathcal{L}_{\rm STP}=1-\cos(\frac{1}{r-s+1}\sum_{s\leq i\leq r}h_{i},\frac{1}{t-r+1}\sum_{r\leq j\leq t}h_{j}) . This is inspired by BERT Mean Pooling ( Kim et al., 2021 ) .

[253] p: Mask : This variation is inspired by BERT mask-and-recover training objective ( Devlin et al., 2019 ) . Given a token sequence x ≤ t x_{\leq t} , we randomly pick a span [ s , r ] [s,r] and replace the tokens within this span with the [MASK] token. Let y ≤ t y_{\leq t} denote the masked sequence and g t = f ⁡ ( y ≤ t ) g_{t}=f(y_{\leq t}) . The loss is defined as ℒ mask = 1 − cos ⁡ ( h r − h s , g t ) \mathcal{L}_{\rm mask}=1-\cos(h_{r}-h_{s},g_{t}) . This can be interpreted as recovering the information of the masked tokens using the representation of the masked sequence y ≤ t y_{\leq t} .

[254] p: Full : Instead of aiming to match h r − h s h_{r}-h_{s} , we target h t h_{t} . The loss becomes ℒ Mask = 1 − cos ⁡ ( h t , g t ) \mathcal{L}_{\rm Mask}=1-\cos(h_{t},g_{t}) , corresponding to the recovery of the full masked sequence rather than just the masked span.

[255] p: Pred : Identical to the Pred variation in the Semantic Tube configuration.

[256] p: Inst : Identical to the Inst variation in the Semantic Tube configuration.

[257] p: Curvature : This variation is inspired by the curvature straightening objective ( Hénaff et al., 2021 ) . Let θ i \theta_{i} be the angle between h i − h i − 1 h_{i}-h_{i-1} and h i + 1 − h i h_{i+1}-h_{i} . The loss is defined as ℒ Curvature = 1 t ​ ∑ i ≤ t | θ i | \mathcal{L}_{\rm Curvature}=\frac{1}{t}\sum_{i\leq t}|\theta_{i}| .

[258] p: Sign : Replaces | θ i | |\theta_{i}| with θ i \theta_{i} (allowing for signed curvature).

[259] p: The fact that Pred yields inferior performance in both the Semantic Tube and Two Views configurations supports (P5).

[260] p: The p p -values comparing variations and options are presented in Tables 4 and 5 .

[261] figure: Table 4 : Pairwise p p -values comparing variation families. A cell is populated only if the mean accuracy of the row method exceeds that of the column method. p p -values are computed using a paired, one-tailed t t -test, restricted to the best-performing variant from each family. Two View Mask Curvature LLM-JEPA2 1.14e-3 1.77e-3 3.04e-5 Two View 4.76e-3 5.10e-5 Mask 1.28e-4

[262] figure: Table 5 : Pairwise p p -values comparing options within each variation family. A cell is populated only if the mean accuracy of the row option exceeds that of the column option. p p -values are computed using a paired, one-tailed t t -test. Values exceeding 0.05 0.05 are struck through. Zero Pred Inst 2View Pred Mean LLM-JEPA2 0.0534 2.03e-3 2.34e-4 2View+Warmup 0.265 0.0426 9.16e-6 +Zero 0.0185 5.56e-4 2View 0.0689 1.19e-6 +Pred 2.97e-4 +Pred 2.78e-4 Inst,Recov Inst Mask Signed Mask + all 0.0629 0.0159 4.02e-3 -Pred 2.34e-3 1.18e-3 Curvature 0.0368 -Recov,Pred 0.0103

[263] h2: Instructions for reporting errors

[264] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[265] p: Tip: You can select the relevant text first, to include it in your report.

[266] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[267] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
