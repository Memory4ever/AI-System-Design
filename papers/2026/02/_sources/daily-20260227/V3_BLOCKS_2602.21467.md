[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Geometric Priors for Generalizable World Models \titlebreak via Vector Symbolic Architecture

[3] h6: Abstract

[4] p: A key challenge in artificial intelligence and neuroscience is understanding how neural systems learn representations that capture the underlying dynamics of the world. Most world models represent the transition function with unstructured neural networks, limiting interpretability, sample efficiency, and generalization to unseen states or action compositions. We address these issues with a generalizable world model grounded in Vector Symbolic Architecture (VSA) principles as geometric priors. Our approach utilizes learnable Fourier Holographic Reduced Representation (FHRR) encoders to map states and actions into a high-dimensional complex vector space with learned group structure and models transitions with element-wise complex multiplication. We formalize the framework’s group-theoretic foundation and show how training such structured representations to be approximately invariant enables strong multi-step composition directly in latent space and generalization performances over various experiments. On a discrete grid world environment, our model achieves 87.5% zero-shot accuracy to unseen state-action pairs, obtains 53.6% higher accuracy on 20-timestep horizon rollouts, and demonstrates 4 × 4\times higher robustness to noise relative to an MLP baseline. These results highlight how training to have latent group structure yields generalizable, data-efficient, and interpretable world models, providing a principled pathway toward structured models for real-world planning and reasoning.

[5] h6: keywords

[6] h2: 1 Introduction

[7] p: Humans build internal world models that capture the underlying dynamics of the environment and allow interaction beyond direct trial-and-error ( LeCun, 2022 ) . Inspired by this idea, modern reinforcement learning (RL) has leveraged latent predictive models conditioned on states and actions, achieving state-of-the-art results in video games ( Hafner et al., 2020 ) and continuous control ( Hansen et al., 2023 ) . Despite these successes, current world models face two major limitations. They are largely confined to RL, control, and robotics settings where abundant simulated data is available and treat the transition function T : S × A → S T:S\times A\to S as an unstructured black-box function approximators. While highly expressive, such architectures suffer from poor sample efficiency, weak extrapolation to unseen states, compounding rollout errors, and latent spaces with no explicit geometric meaning.

[8] p: Biological systems, in contrast, appear to exploit symmetries and geometric structure ( Gardner et al., 2022 ; Gallego et al., 2017 ) in the environment, effectively reducing the complexity of learning. Geometric Deep Learning (GDL) ( Bronstein et al., 2021 ; Papillon et al., 2025 ; Shewmake et al., 2023 ) formalizes this idea by incorporating geometric priors into neural networks to help preserve structure throughout the network, dramatically improving the efficiency and generalization capabilities.

[9] p: Vector Symbolic Architecture (VSA) ( Kleyko et al., 2022 ) offers a complementary, algebraic approach to structured representations. They represent symbols as high-dimensional vectors and compose them via binary operations, forming structured representations that are robust to noise. In addition, VSA-based representations can be trained to approximate group actions, making them a promising approach for GDL. Among the many VSA variants, Fourier Holographic Reduced Representation (FHRR) ( Plate, 2003 ) remains a popular implementation of VSA to efficiently encode complex data structures due to its efficiency and exact invertibility.

[10] h4: Contribution.

[11] p: In this work, we propose a generalizable world model using VSA principles. Our FHRR encoder encodes states and actions as unitary complex vectors, with transitions realized as element-wise multiplication. We train the model to have latent group structure on actions with multi-step action composition, invertibility, and robust cleanup. We demonstrate that the model (1) encourages transition equivariance in the latent space and learns action representations respecting group structure, (2) achieves long-horizon stability and error correction via cleanup, and (3) outperforms MLP baselines on one-step prediction, long-horizon rollouts, zero-shot generalization, and robustness tests on a discrete grid world environment regardless of scale. Our approach provides an alternative architecture to world modeling with strong implications for interpretable and generalizable decision-making for real world applications.

[12] h2: 2 Related Work

[13] h4: World Models in Model-Based RL.

[14] p: World models aim to learn a predictive model of an environment’s transition dynamics that can leveraged for learning and planning. Model-based reinforcement learning methods ( Ha and Schmidhuber, 2018 ; Hafner et al., 2019 ) and recent Model Predictive Control methods ( Hansen et al., 2023 ) utilize world models to learn the environment’s dynamics for decision-making, yet often suffer from compounding rollout errors ( Hansen et al., 2022 ) and limited transparency in the learned dynamics ( Glanois et al., 2024 ) . Most approaches treat the transition function as an unstructured mapping from ( s , a ) ↦ s ′ (s,a)\mapsto s^{\prime} , which can be highly expressive but fails to exploit known symmetries in the environment. This can limit generalization, especially when the environment exhibits strong symmetries or if little training data is available. These limitations motivate the incorporation of geometric priors into world models, where known symmetries or structures in the environment are part of the representation learning process.

[15] h4: Geometric Deep Learning.

[16] p: In the context of world modeling, GDL-based approaches ( Kipf et al., 2019 ; Park et al., 2022 ) have incorporated symmetry and structure to improve generalization in structured environments. However, in such implementations, the latent representations themselves are not structured such that they can be algebraically composed, inverted, or directly manipulated. Without the ability to easily or interpretably manipulate latents with vector operations, planning or composition with such architectures consequently require an expensive full forward pass or additionally trained modules. Our VSA-based approach to GDL trains the action representations such that it respects group structure in the latent space and leverages cleanup for robustness and compounding error reduction.

[17] h4: Vector Symbolic Architectures.

[18] p: VSA, also known as Hyperdimensional Computing, is a computational paradigm where discrete symbols are represented as high-dimensional vectors (e.g. D ≥ 1000 D\geq 1000 ) sampled from well-defined distributions ( Kanerva, 2009 ) . These representations are inherently robust to noise and enable symbolic reasoning through simple algebraic operations. VSAs have been applied in diverse domains, including efficient classification ( Ni et al., 2024b ) , time-series modeling ( Mejri et al., 2024 ) , graph reasoning ( Poduval et al., 2022 ) , reinforcement learning ( Ni et al., 2024a ) , and representing cognitive maps ( Yeung et al., 2025 ) . Hardware-efficient implementations have also made them appealing for resource-constrained applications and learning on the edge ( Zou et al., 2021 ; Chung et al., 2025 ) . However its applications as a transition operation in learnable settings remain largely unexplored. Our work aims to close this gap by constructing learnable world models that utilize the binding operation to model environment transitions and the VSA clean-up mechanism to perform robust rollouts.

[19] figure: Figure 1: Overview of the FHRR-based world modeling framework. a) Visualization of the partially held-out GridWorld Environment. b) Difference between MLP-based and FHRR-based dynamics modeling. Direct predictions of s ^ t + 1 \hat{s}_{t+1} by MLPs cannot easily generalize to OOD samples, while FHRR can.

[20] h2: 3 Proposed Framework

[21] p: fig:framework visualizes the architecture of our generalizable world model. We model environment dynamics as group actions in a learnable, complex latent space where the dynamics is implemented by the binding operation. Concretely, we learn state and action encoders such that the transition model inherits several useful VSA properties including interpretability of the transformation between two given states, robustness to noise due to the high-dimensionality of the representations, and a native cleanup mechanism to mitigate exponential error growth in long-horizon rollouts. In contrast, MLP-based approaches concatenates of state-action pairs which limits the model’s ability to learn separate state and action mappings.

[22] h3: 3.1 Fourier Holographic Reduced Representation

[23] p: FHRR ( Plate, 2003 ) is a specific VSA variant in which each vector component lies on the unit circle in the complex plane, i.e.

[24] table: 𝐯 = [ e i ​ θ j ] j = 1 D ∈ ℂ D \mathbf{v}=[e^{i\theta_{j}}]_{j=1}^{D}\in\mathbb{C}^{D} (1)

[25] p: such that θ j ∼ p \theta_{j}\sim p for dimension j = 1 , … , D j=1,\dots,D where p p is some distribution (e.g. Unif ⁡ ( 0 , 2 ​ π ) \mathrm{Unif}(0,2\pi) or 𝒩 ⁡ ( 0 , 1 ) \mathcal{N}(0,1) ), resulting in a phase-based complex unitary vector. As a VSA, FHRR admits two binary operations, namely bundling ( + + ) and binding ( ⊙ \odot ), to construct composite representations. Bundling is implemented as vector addition while binding is implemented as element-wise complex multiplication. Given vectors 𝐯 1 = [ e i ​ θ 1 , j ] j = 1 D \mathbf{v}_{1}=[e^{i\theta_{1,j}}]_{j=1}^{D} and 𝐯 2 = [ e i ​ θ 2 , j ] j = 1 D \mathbf{v}_{2}=[e^{i\theta_{2,j}}]_{j=1}^{D} , 𝐯 1 ⊙ 𝐯 2 = [ e i ⁡ ( θ 1 , j + θ 2 , j ) ] j = 1 D \mathbf{v}_{1}\odot\mathbf{v}_{2}=[e^{i(\theta_{1,j}+\theta_{2,j})}]_{j=1}^{D} . The inverse of a FHRR vector 𝐯 \mathbf{v} is simply its complex conjugate, enabling straightforward unbinding via 𝐯 − 1 = 𝐯 ¯ \mathbf{v}^{-1}=\overline{\mathbf{v}} . A notable property of FHRR is its connection to kernel-based methods in machine learning ( A.2 ). There are various other related implementations of VSA ( A ), but we limit the scope of VSA to FHRR in this work.

[26] h3: 3.2 Environment Dynamics as a Group Action on Sets

[27] p: Let S S be a finite set of states, A A a finite set of actions, and T : S × A → S T:S\times A\to S a deterministic transition function. We assume that compositions of actions generate an action group ( G , ∘ ) (G,\circ) acting on S S :

[28] table: ⋅ : G × S → S , ( g , s ) ↦ g ⋅ s , \cdot:G\times S\to S,\quad(g,s)\mapsto g\cdot s, (2)

[29] p: with identity e ⋅ s = s e\cdot s=s and ( g 1 ∘ g 2 ) ⋅ s = g 1 ⋅ ( g 2 ⋅ s ) (g_{1}\circ g_{2})\cdot s=g_{1}\cdot(g_{2}\cdot s) for g 1 , g 2 ∈ G g_{1},g_{2}\in G . Each action a ∈ A a\in A corresponds to a generator g a ∈ G g_{a}\in G such that T ⁡ ( s , a ) = g a ⋅ s T(s,a)=g_{a}\cdot s . In particular, the identity e e does not need to be a primitive action, but is always present in G G and can be realized as e = g a ∘ g a − 1 e=g_{a}\circ g_{a}^{-1} for any a ∈ A a\in A .

[30] h3: 3.3 Equivariant Latent Representations

[31] p: We embed states into a D D -dimensional complex vector space via a map ϕ S : S → 𝒵 \phi_{S}:S\to\mathcal{Z} , where 𝒵 = ( S 1 ) D = { z ∈ ℂ D : | z d | = 1 } \mathcal{Z}=(S^{1})^{D}=\{z\in\mathbb{C}^{D}\ :\ |z_{d}|=1\} . Notably, ( 𝒵 , ⊙ ) (\mathcal{Z},\odot) forms a group. A representation of the action group G G in 𝒵 \mathcal{Z} is a homomorphism :

[32] table: ρ : G → 𝒵 , ρ ( g 1 ∘ g 2 ) = ρ ( g 1 ) ⊙ ρ ( g 2 ) , ∀ g 1 , g 2 ∈ G . \rho:G\to\mathcal{Z},\quad\rho(g_{1}\circ g_{2})=\rho(g_{1})\odot\rho(g_{2}),\quad\forall g_{1},g_{2}\in G. (3)

[33] p: The encoder ϕ S : S → 𝒵 \phi_{S}:S\to\mathcal{Z} is equivariant to environment transitions if

[34] table: ϕ S ​ ( T ⁡ ( s , a ) ) = ρ ⁡ ( a ) ⊙ ϕ S ​ ( s ) , ∀ s ∈ S , a ∈ A \phi_{S}(T(s,a))=\rho(a)\odot\phi_{S}(s),\quad\forall s\in S,\ a\in A (4)

[35] p: where T ⁡ ( s , a ) T(s,a) is the environment’s transition function. By closure of G G , the same property holds for any composed action g ∈ G g\in G , i.e. ϕ S ​ ( g ⋅ s ) = ρ ⁡ ( g ) ⊙ ϕ S ​ ( s ) \phi_{S}(g\cdot s)=\rho(g)\odot\phi_{S}(s) , which states that transforming s s by g g corresponds to multiplying its latent representation by ρ ⁡ ( g ) \rho(g) .

[36] h3: 3.4 Latent Transition Model

[37] p: We would like to learn state and action encoders, ϕ S : S → 𝒵 \phi_{S}:S\to\mathcal{Z} and ϕ A : A → 𝒵 \phi_{A}:A\to\mathcal{Z} respectively, such that (1) ϕ A \phi_{A} induces a representation of G G via the generators g a ∈ G g_{a}\in G for all a ∈ A a\in A ; and (2) the equivariance condition given by Eq. 4 holds.

[38] p: Suppose s ∈ ℝ n s s\in\mathbb{R}^{n_{s}} and a ∈ ℝ n a a\in\mathbb{R}^{n_{a}} where n s n_{s} and n a n_{a} are the original state and action dimensions, respectively. We parameterize ϕ S \phi_{S} and ϕ A \phi_{A} via the FHRR encoding:

[39] table: ϕ S ​ ( s ) \displaystyle\phi_{S}(s) = [ e i ​ θ j , s ⊤ ​ s ] j = 1 D , ϕ A ​ ( a ) = [ e i ​ θ j , a ⊤ ​ a ] j = 1 D . \displaystyle=[e^{i\theta_{j,s}^{\top}s}]_{j=1}^{D},\quad\phi_{A}(a)=[e^{i\theta_{j,a}^{\top}a}]_{j=1}^{D}. (5)

[40] p: Motivated by Eq. 4 , we model the latent transitions in FHRR-space via the binding operator

[41] table: τ : 𝒵 × 𝒵 \displaystyle\tau:\mathcal{Z}\times\mathcal{Z} → 𝒵 , ( ϕ S ​ ( s ) , ϕ A ​ ( a ) ) ↦ ϕ S ​ ( s ) ⊙ ϕ A ​ ( a ) \displaystyle\to\mathcal{Z},\quad(\phi_{S}(s),\phi_{A}(a))\mapsto\phi_{S}(s)\odot\phi_{A}(a) (6)

[42] p: We would also like to learn ϕ S : S → 𝒵 \phi_{S}:S\to\mathcal{Z} and ϕ A : A → 𝒵 \phi_{A}:A\to\mathcal{Z} such that one-step dynamics satisfy

[43] table: ϕ S ​ ( s t + 1 ) \displaystyle\phi_{S}(s_{t+1}) = τ ⁡ ( ϕ S ​ ( s t ) , ϕ A ​ ( a t ) ) = ϕ S ​ ( s t ) ⊙ ϕ A ​ ( a t ) , \displaystyle=\tau(\phi_{S}(s_{t}),\phi_{A}(a_{t}))=\phi_{S}(s_{t})\odot\phi_{A}(a_{t}), (7)

[44] p: and ϕ A ​ ( a ) = ρ ⁡ ( g a ) \phi_{A}(a)=\rho(g_{a}) . In phase coordinates, this corresponds to:

[45] table: Θ s ⊤ ​ s t + 1 = Θ s ⊤ ​ s t + Θ a ⊤ ​ a t ( mod ​ 2 ​ π ) \displaystyle\Theta_{s}^{\top}{s_{t+1}}=\Theta_{s}^{\top}{s_{t}}+\Theta_{a}^{\top}{a_{t}}\ \ (\mathrm{mod}\ 2\pi) (8)

[46] p: where Θ s = [ θ j , s ] j = 1 D ∈ ℂ D × n s \Theta_{s}=[\theta_{j,s}]_{j=1}^{D}\in\mathbb{C}^{D\times n_{s}} , Θ a = [ θ j , a ] j = 1 D ∈ ℂ D × n a \Theta_{a}=[\theta_{j,a}]_{j=1}^{D}\in\mathbb{C}^{D\times n_{a}} , and the modulus is applied element-wise. Due to the properties of FHRR, we can simply extend this to multi-step composition:

[47] table: Embedding Space: ϕ S ​ ( s t + k ) = ϕ S ​ ( s t ) ⊙ ∏ j = 1 k ϕ A ​ ( a t + j − 1 ) \displaystyle\quad\phi_{S}(s_{t+k})=\phi_{S}(s_{t})\odot\prod_{j=1}^{k}\phi_{A}(a_{t+j-1}) (9) Phase Space: Θ s ⊤ ​ s t + k = Θ s ⊤ ​ s t + ∑ j = 1 k Θ a ⊤ ​ a t + j − 1 ( mod ​ 2 ​ π ) . \displaystyle\quad\Theta_{s}^{\top}{s_{t+k}}=\Theta_{s}^{\top}{s_{t}}+\sum_{j=1}^{k}\Theta_{a}^{\top}{a_{t+j-1}}\quad(\mathrm{mod}\ 2\pi). (10)

[48] h3: 3.5 Learning Objectives

[49] p: We learn ϕ S \phi_{S} and ϕ A \phi_{A} with learnable parameters Θ s \Theta_{s} and Θ a \Theta_{a} respectively and train on transition tuples, ( s t , a t , s t + 1 ) (s_{t},a_{t},s_{t+1}) . We minimize a binding loss to encourage transition equivariance given in Eq. 7 :

[50] table: ℒ bind = ‖ ϕ S ​ ( s t + 1 ) − ϕ S ​ ( s t ) ⊙ ϕ A ​ ( a t ) ‖ 2 \mathcal{L}_{\text{bind}}=\|\phi_{S}(s_{t+1})-\phi_{S}(s_{t})\odot\phi_{A}(a_{t})\|^{2} (11)

[51] p: Additionally, to preserve structure in our representations, we introduce invertibility and orthogonality regularizers:

[52] table: ℒ inv = ∑ ( a , a − 1 ) ‖ ϕ A ​ ( a ) ⊙ ϕ A ​ ( a − 1 ) − 𝟏 ‖ 2 , \mathcal{L}_{\text{inv}}=\sum_{(a,a^{-1})}\left\|\phi_{A}(a)\odot\phi_{A}(a^{-1})-\mathbf{1}\right\|^{2}, (12)

[53] table: ℒ ortho = ∑ i ≠ j ( ⟨ ϕ S ​ ( s i ) , ϕ S ​ ( s j ) ⟩ ) 2 . \mathcal{L}_{\text{ortho}}=\sum_{i\neq j}\left(\langle\phi_{S}(s_{i}),\phi_{S}(s_{j})\rangle\right)^{2}. (13)

[54] p: In particular, the invertability constraint given by Eq. 12 encourages that the actions a ∈ A a\in A form a representation via ϕ A \phi_{A} , i.e. ϕ A \phi_{A} induces an approximate homomorphism with respect to the actions in the grid environment.

[55] p: The full objective is ℒ = λ bind ​ ℒ bind + λ inv ​ ℒ inv + λ ortho ​ ℒ ortho \mathcal{L}=\lambda_{\text{bind}}\mathcal{L}_{\text{bind}}+\lambda_{\text{inv}}\mathcal{L}_{\text{inv}}+\lambda_{\text{ortho}}\mathcal{L}_{\text{ortho}} where λ bind , λ inv , λ ortho \lambda_{\text{bind}},\lambda_{\text{inv}},\lambda_{\text{ortho}} are the hyperparameters controlling the balance between each objective respectively. Training is linear-time in D D per sample and memory is O ⁡ ( D ) O(D) as all VSA operations are done element-wise. Additionally, multi-step rollouts can be processed using Eq. 10 for linear-time in the phase space where ( | a | ∈ A ) ≪ D (|a|\in A)\ll D for inference.

[56] figure: Figure 2: a) Shaded red represents out of the training distribution. Cleanup during FHRR Inference can ameliorate error accumulation due to distribution shift between train and test. b) Cleanup mechanism equations via similarity search in FHRR.

[57] h3: 3.6 Cleanup Mechanism

[58] p: A key advantage of VSA-based models is their ability to support self-correct (error correction) through a process known as cleanup Plate and others (1991) , visualized in Figure 2 . Given a noisy or approximate prediction of the next-state, ϕ S ​ ( s ^ t + 1 ) \phi_{S}(\hat{s}_{t+1}) , cleanup recovers the most likely true embedding by similarity search i.e. ϕ S ​ ( s ^ t + 1 ) = arg ⁡ max s ∈ 𝒮 ⁡ Re ⁡ ⟨ ϕ S ​ ( s ^ t + 1 ) , ϕ S ​ ( s ) ⟩ . \phi_{S}(\hat{s}_{t+1})=\arg\max_{s\in\mathcal{S}}\ \mathrm{Re}\,\langle\phi_{S}(\hat{s}_{t+1}),\phi_{S}(s)\rangle. where Re ​ ⟨ ⟩ \mathrm{Re}\langle\quad\rangle refers to taking the real part of the complex inner product between two vectors.

[59] p: Cleanup is based on the premise that in high-dimensional spaces, randomly generated vectors are almost always far apart from one another. As a result, a noisy vector still remains noticeably closer to its true state embedding than to any other state. Intuitively, one can visualize it as the level of separation between random vectors increases as the dimensionality increases.

[60] p: In our setting, each state s ∈ S s\in S is encoded as a unitary complex vector, and during training the ℒ ortho \mathcal{L}_{\text{ortho}} term (Section 3.5 ) encourages that distinct state representations are quasi-orthogonal , i.e. Re ⁡ ⟨ ϕ S ​ ( s ) , ϕ S ​ ( s ′ ) ⟩ ≈ 0 for ​ s ≠ s ′ . \mathrm{Re}\,\langle\phi_{S}(s),\phi_{S}(s^{\prime})\rangle\approx 0\quad\text{for }s\neq s^{\prime}. We maintain a state codebook , whose rows store the learned embeddings for every learned discrete state in the environment. During inference an approximate prediction of the next state is cleaned up by simply comparing this prediction to the entries in the codebook and selecting the most similar one. This process works because different state embeddings are trained to be nearly orthogonal, producing large separation margins in high dimensions. More formal descriptions of the cleanup mechanism are provided in Appendix A.3 .

[61] figure: Task FHRR (Ours) MLP-Small MLP-Medium MLP-Large 1-step Accuracy 96.3% 80.0% 80.0% 80.25% 1-step Accuracy (Zero-Shot) 87.5% 0.0% 0.0% 1.25% Cosine Similarity 83.0 79.5 79.9 80.6 Cosine Similarity (Zero-Shot) 80.5 0.9 0.15 3.1 Rollout (5 steps) 74.6% 39.8% 38.0% 40.8% Rollout (20 steps) 34.6% 2.0% 4.0% 6.2% Rollout (20 steps + Clean) 61.4% 5.4% 7.8% 8.4% Rollout (100 steps) 1.8% 0.8% 1.8% 2.0% Rollout (100 steps + Clean) 38.6% 2.8% 4.0% 3.2%

[62] h2: 4 Results

[63] h4: Experimental Design.

[64] p: We train and evaluate our VSA-based world models with 3 MLP baselines of varying sizes on a 10×10 GridWorld environment with a total of 100 discrete states and 4 deterministic actions. For all models, we train on 80% of (state, action) pairs, hold out 20% for zero-shot evaluation, and train for 500 epochs. In tbl:HDC_ACC_Results, we compare FHRR versus MLP-Small, MLP-Medium, and MLP-Large on several different tasks, such as 1-step accuracy, cosine similarity, and rollouts. In B.5 , we compare the total parameter count and inference time between all the models to highlight that VSA models have a similar parameter count as MLP-Small. For more explicit details on the implementation, please check the B .

[65] figure: Figure 3: Latent Rollout Accuracy of FHRR and MLP-M over varying zero-shot ratios

[66] h4: Dynamics Modeling

[67] p: For 1-step accuracy, we test the models on their ability to predict the correct next state given (state, action) pairs. While the models are trained on 80% of the dataset, they are tested on all possible transitions. For the zero-shot tests (when evaluating on the unseen 20% transitions), our model achieves significantly higher zero-shot accuracy and cosine similarity, confirming its ability to generalize well. We also highlight that scaling the size of the MLPs has not shown a significantly stronger ability for these models to generalize. In the rollout tests, (i.e. interactions solely in the latent space, FHRR maintains a higher accuracy over long transitions, unlike MLP which accumulates drift. Additionally, VSA has the added benefit of applying cleanup . For a fair comparison, we utilize nearest-neighbor search for the MLPs to compare against the VSA model with cleanup and apply the cleanup every 2 time steps.

[68] figure: Figure 4: t-SNE visualization of state embeddings for VSA (FHRR) vs MLP-M labeled per row

[69] h4: Latent Rollout Performance.

[70] p: fig:zeroshot compares the latent rollout accuracy of horizon length t = 20 t=20 between FHRR and MLP-Medium given varying zero-shot ratios. As the zero-shot ratio increases, we notice a linear decrease in the FHRR model performance while the MLP-based model’s accuracy exponentially decreases and fails to maintain even above 10% when trained on only 90% of the transitions. Additionally, the cleanup operation improves the accuracy of the FHRR model by 35% when zero-shot ratio = 0.1, resulting in a 3.3 × 3.3\times improvement over the MLP baseline.

[71] h4: Latent Visualizations.

[72] p: In fig:latent_vis we visualize the t-SNE components of the state embeddings of the FHRR and MLP-Medium models. The FHRR model is able to capture the structure of the grid environment in its latent space while MLP-Medium fails to maintain any structure. We attribute this structured latent space for its strong generalization capabilities over MLP baselines.

[73] figure: \subfigure [Robustness to Noise] \subfigure [Similarity Kernels]

[74] h4: Robustness.

[75] p: We study the robustness of our FHRR model with MLP-Medium by comparing the 1-step dynamics accuracy when random gaussian noise is added to the transition function. fig:robustness shows the results between gaussian noise between 0 to 5 magnitude of standard deviation (i.e. noise n ∼ 𝒩 ⁡ ( 0 , σ ) ​ where σ ∈ [0, 5] n\sim\mathcal{N}(0,\sigma)\text{ where $\sigma\in$[0, 5]} ). The FHRR model maintains above a 80% accuracy even under large amounts of noise while MLP-M struggles as the scale of noise increases.

[76] h4: Similarity Kernel.

[77] p: Given the kernel approximation property of FHRR ( A.2 ), in fig:similarity, we plot the similarity between ϕ S ​ ( s ) \phi_{S}(s) and ϕ S ​ ( s + k ​ a ) \phi_{S}(s+ka) where a a is a given action and k ∈ [ − 10 , 10 ] k\in[-10,10] . For all actions, we notice an approximately smooth but sharp similarity kernel peaking at k = 0 k=0 and decaying as | k | |k| increases, indicating that the latent space preserves locality of the states. The approximate symmetry of these curves across actions demonstrates that our model learns a structured geometry in which actions correspond to consistent translation across the states.

[78] h2: 5 Conclusion

[79] p: In this work, we present an alternative approach to world modeling based on VSA, where states and actions are encoded as unitary complex vectors and transitions are modeled via element-wise multiplication. Our experiments on a discrete world environment show that our model achieves strong generalization capabilities and maintains long-horizon rollout accuracy under noise, outperforming MLP baselines regardless of scale. While promising, our current work is limited to small discrete environments. Extending this approach to continuous, stochastic, or partially observable domains remains an open challenge. In future work, we hope to integrate VSA-based world modeling into model-based RL and planning to enable generalizable dynamics models that are applicable to real world environments. Overall, this work demonstrates that learning structured algebraic representations offers a principled path toward robust, interpretable, and generalizable world models.

[80] h2: Acknowledgements

[81] p: This work was supported in part by Nthe DARPA Young Faculty Award, the National Science Foundation (NSF) under Grants #2431561, #2127780, #2319198, #2321840, #2312517, and #2235472, the Semiconductor Research Corporation (SRC), the Office of Naval Research through the Young Investigator Program Award, Grants #N00014-21-1-2225 and #N00014-22-1-2067, Army Research Office Grant #W911NF2410360, and the National Defense Science & Engineering Graduate (NDSEG) Fellowship Program. Additionally, support was provided by the Air Force Office of Scientific Research under Award #FA9550-22-1-0253, along with generous gifts from Xilinx and Cisco.

[82] h2: References

[83] h2: Appendix A Vector Symbolic Architectures

[84] h3: A.1 VSA Variants

[85] p: VSA consists of two fundamental operations: bundling (superposition), which adds vectors to form set-like representations, and binding (association), which combines vectors into a compositional representation, often with invertibility. This algebraic structure allows VSAs to represent structured data such as sequences, sets, and relations in a way that supports compositionality and symbolic reasoning through lightweight vector operations.

[86] p: Many VSA works also consist of a permutation operation (shuffling) to encode ordered structures or design non-commutative operations when combined with bundling or binding . Below, we summarize some related VSA approaches:

[87] h4: Holographic Reduced Representations

[88] p: HRR ( Plate, 1995 ) uses real-valued vectors with components drawn from a normal distribution and defines binding as circular convolution, bundling as element-wise addition, and similarity as dot product between two vectors. Fourier Holographic Reduced Representation is the extension of Holographic Reduced Representations, which avoids convolution and fourier transforms altogether by using element-wise complex multiplication which is equivalent to convolution in the frequency domain ( Plate, 2003 ) .

[89] h4: Multiply Add Permute

[90] p: MAP ( Gayler, 1998 ) utilizes high-dimensional bipolar vectors where binding is element-wise multiplication, bundling is element-wise addition, and similarity as cosine similarity or the dot product. MAP forms the foundation for many subsequent VSA designs due to the simplicity of element-wise multiplication for binding.

[91] h4: Generalized Holographic Reduced Representations

[92] p: GHRR ( Yeung et al., 2024 ) is an extension of FHRR by replacing the unitary complex vector e i ​ θ ∈ U ⁡ ( 1 ) e^{i\theta}\in U(1) with a unitary matrix a j ∈ U ⁡ ( m ) a_{j}\in U(m) , such that vectors become tensors H ∈ ℂ D × m × m H\in\mathbb{C}^{D\times m\times m} whose binding is defined as matrix multiplication. Bundling still holds as element-wise addition. The similarity between two hypervectors H 1 = [ a j ] j = 1 D H_{1}=[a_{j}]_{j=1}^{D} and H 2 = [ b j ] j = 1 D H_{2}=[b_{j}]_{j=1}^{D} is defined as

[93] table: δ ⁡ ( H 1 , H 2 ) = 1 m ​ D ​ Re ​ ( tr ​ ∑ j = 1 D a j ​ b j † ) . \delta(H_{1},H_{2})\;=\;\frac{1}{mD}\,\mathrm{Re}\left(\mathrm{tr}\sum_{j=1}^{D}a_{j}b_{j}^{\dagger}\right). (14)

[94] p: For m = 1 m=1 , this reduces exactly to FHRR similarity. GHRR enables non-commutative and more flexible representations, controlled by the choice of unitary matrices yet equivalent to FHRR when m = 1 m=1 .

[95] h3: A.2 Kernel Approximation in FHRR

[96] p: One way to encode data into FHRR follows the Random Fourier Features (RFF) encoding ( Rahimi and Recht, 2007 ) , an efficient approximation of kernel methods. The RFF encoding is a map ϕ : ℝ n → ℂ D \phi:\mathbb{R}^{n}\to\mathbb{C}^{D} , with ϕ ⁡ ( 𝐱 ) = e i ​ 𝐌𝐱 \phi(\mathbf{x})=e^{i\mathbf{Mx}} , where each row 𝐌 j , : ∼ p \mathbf{M}_{j,:}\sim p for some multivariate distribution p p . As a result of Bochner’s theorem, ⟨ ϕ ⁡ ( 𝐱 ) , ϕ ⁡ ( 𝐲 ) ⟩ / D ≈ K ⁡ ( 𝐱 − 𝐲 ) \langle\phi(\mathbf{x}),\phi(\mathbf{y})\rangle/D\approx K(\mathbf{x}-\mathbf{y}) for all 𝐱 , 𝐲 ∈ ℝ n \mathbf{x},\mathbf{y}\in\mathbb{R}^{n} , where K K is a shift-invariant kernel that is the Fourier transform of distribution p p . The approximation converges to the true kernel in the limit as D → ∞ D\to\infty . Notably, when p p is the standard Gaussian distribution, the radial basis function (RBF) kernel is recovered.

[97] h3: A.3 Cleanup in VSA

[98] p: An advantage of VSA representations is that different symbols (states in world modeling) are learned to be nearly orthogonal in high-dimensional space Plate and others (1991) . This means that small perturbations to a predicted state vector s ^ t + 1 \hat{s}_{t+1} typically do not change which symbol it is closest to, enabling reliable identity recovery through a simple nearest-neighbor search.

[99] p: In contrast, conventional neural networks often learn entangled latent spaces with no explicit separation or compositional structure. In such spaces, even small prediction errors can move a representation across decision boundaries, causing semantic drift that accumulates over long rollouts. In settings involving hardware noise or approximate computation (e.g., in-memory or neuromorphic accelerators and world modeling) this becomes a larger issue. Given a perturbed output

[100] table: s ^ t + 1 = f θ ​ ( s , a ) + ϵ , \hat{s}_{t+1}=f_{\theta}(s,a)+\epsilon,

[101] p: there is no guarantee that

[102] table: arg ⁡ min s ′ ​ ‖ f θ ​ ( s , a ) − s ^ t + 1 ‖ ≈ s t + 1 , \arg\min_{s^{\prime}}\|f_{\theta}(s,a)-\hat{s}_{t+1}\|\approx s_{t+1},

[103] p: making nearest-neighbor lookup unreliable under large amounts of noise or long horizon prediction tasks.

[104] h4: Codebook-based cleanup.

[105] p: In VSA, cleanup is often implemented as a nearest-neighbor search over a state codebook . Let Φ ∈ ℂ | 𝒮 | × D \Phi\in\mathbb{C}^{|\mathcal{S}|\times D} denote the matrix of state embeddings, where Φ s = ϕ S ​ ( s ) \Phi_{s}=\phi_{S}(s) . Given a noisy prediction x x , cleanup selects the state with greatest real-part similarity:

[106] table: s ⋆ = arg ⁡ max s ∈ 𝒮 ⁡ Re ⁡ ⟨ x , Φ s ⟩ , s^{\star}=\arg\max_{s\in\mathcal{S}}\ \mathrm{Re}\,\langle x,\Phi_{s}\rangle,

[107] p: which corresponds to taking the argmax over the real parts of the matrix multiplication between a state embedding and the state codebook. When the number of states is moderate (as in discrete environments), this cleanup incurs negligible overhead and provides identity-correcting feedback at every timestep. For larger 𝒮 \mathcal{S} , approximate nearest neighbor or restricted-batch cleanup can be used. When the state-codebook is explicitly stored as a matrix, this operation can be reduced to taking an arg ⁡ max \arg\max after performing matrix-vector multiplication.

[108] h4: Why cleanup works: concentration in high dimensions.

[109] p: Two geometric properties guarantee the reliability of cleanup:

[110] p: (1) Concentration of self-similarity. If x = ϕ S ​ ( s ) + η x=\phi_{S}(s)+\eta is a noisy version of the true embedding, then

[111] table: Re ⁡ ⟨ x , ϕ S ​ ( s ) ⟩ ​ concentrates around ​ 1 , Var = 𝒪 ⁡ ( 1 / D ) , \mathrm{Re}\,\langle x,\phi_{S}(s)\rangle\text{ concentrates around }1,\quad\operatorname{Var}=\mathcal{O}(1/D),

[112] p: so the effect of noise shrinks with dimension.

[113] p: (2) Concentration of cross-similarities. For any s ′ ≠ s s^{\prime}\neq s , quasi-orthogonality ensures

[114] table: Re ⁡ ⟨ ϕ S ​ ( s ) , ϕ S ​ ( s ′ ) ⟩ ≈ 0 , Var = 𝒪 ⁡ ( 1 / D ) . \mathrm{Re}\,\langle\phi_{S}(s),\phi_{S}(s^{\prime})\rangle\approx 0,\quad\operatorname{Var}=\mathcal{O}(1/D).

[115] p: Together, these imply a separation margin of

[116] table: margin ∼ 1 − 𝒪 ⁡ ( 1 / D ) , \mathrm{margin}\sim 1-\mathcal{O}(1/\sqrt{D}),

[117] p: meaning that larger dimensionality produces exponentially more reliable cleanup.

[118] h2: Appendix B Implementation Details

[119] h3: B.1 Environment

[120] h4: Dataset

[121] p: We use a 10 × 10 10\times 10 GridWorld with boundaries (no wrap-around). States are indexed and mapped to (row, col). Actions a ∈ { 0 , 1 , 2 , 3 } a\in\{0,1,2,3\} correspond to up , down , left , right with deterministic transition T ⁡ ( s , a ) = ( s ′ ) T(s,a)=(s^{\prime}) .

[122] p: We define transitions ( s , a , s ′ ) (s,a,s^{\prime}) for s ∈ S s\in S , a ∈ A a\in A , which yields | S | ​ | A | = 100 × 4 |S||A|=100\times 4 tuples. We form a zero-shot split at the level of given a zero-shot ratio, such that a fixed ratio (default 20 % 20\% ) of pairs ( s , a ) (s,a) are withheld from training. Zero-shot evaluations are done only held-out pairs, while the regular accuracy, cosine similarity, rollout tests are all done with the all the transitions.

[123] h3: B.2 Models

[124] p: Our VSA-based models use embedding dimensions of D = 512 D=512 . HRR initializes its weights as real-valued numbers sampled from a normal distribution with mean = 0 and standard deviation = 1. We utilize circular convolution for the binding and circular correlation for unbinding. For FHRR, we sample the elements from a uniform distribution from -pi to pi and utilize element-wise complex multiplication for binding. For MLP-based models, we use D = 64 D=64 and D = 16 D=16 for the state and action respectively. These state and actions are concatenated and fed into a MLP for next state prediction. MLP-S is constructed with 2 hidden layer ( D = 128 ) (D=128) , MLP-M with 4 hidden layers ( D = 256 ) (D=256) , and MLP-L with 6 hidden layers ( D = 512 ) (D=512) . Every hidden layer’s output passes through a ReLU activation as well.

[125] h3: B.3 Training Objectives and Hyperparameters

[126] p: For both VSA and MLP-based models. we utilize MSE for the binding loss in 11 . For all experiments, the binding λ bind = 2 \lambda_{\text{bind}}=2 , λ inv = 0.5 \lambda_{\text{inv}}=0.5 , and λ ortho = 0.05 \lambda_{\text{ortho}}=0.05 . The learning rate for VSA models is set as 0.007 0.007 where as the learning rate for MLP-based models is set as 0.0005 0.0005 . We apply a gradient clipping of 1 to help with learning as well.

[127] h3: B.4 Experiments

[128] p: All experiments were run conducted over 500 epochs. For the rollout tests, we sample 500 trials of random trajectories based on the horizon length (i.e. Rollout Length = 20 implies a random trajectory with t = 20 t=20 ). We apply the cleanup operation to both VSA and MLP-based models every 2 time steps when specified as rollout + cleanup.

[129] figure: Figure 5: Robustness Ablation Study

[130] p: In fig:robustness_ablation we run an ablation study and see that increasing dimensionality helps with robustness as expected. Having an orthgonality weight is also necessary but shows little benefit of increasing the weight itself. On the other hand, increasing the number of parameters hurts the robustness of an MLP-based model.

[131] h3: B.5 Inference Details

[132] p: In tbl:HDC_INFER_Results, we display the number of parameters of each model as well as the inference time. Experiments were conducted using an NVIDIA GPU 3060 Ti and inference times were reported in milliseconds.

[133] figure: VSA (HRR) VSA (FHRR) MLP-S MLP-M MLP-L Parameter Count 53,248 53,248 41,600 241,024 1,394,048 Parameter Ratio 1x 1x 0.8x 4.5x 26.2x Inference time (ms) 0.2063 0.1528 0.1174 0.1715 0.3135 Inference + Clean time (ms) 0.2632 0.2421 0.1743 0.2317 0.3761

[134] h2: Instructions for reporting errors

[135] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[136] p: Tip: You can select the relevant text first, to include it in your report.

[137] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[138] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
