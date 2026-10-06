[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Certified Circuits: Stability Guarantees for Mechanistic Circuits

[3] h6: Abstract

[4] p: Understanding how neural networks arrive at their predictions is essential for debugging, auditing, and deployment. Mechanistic interpretability pursues this goal by identifying circuits —minimal subnetworks responsible for specific behaviors. However, existing circuit discovery methods are brittle: circuits depend strongly on the chosen concept dataset and often fail to transfer out-of-distribution, raising doubts whether they capture concept or dataset-specific artifacts. We introduce Certified Circuits , which provide provable stability guarantees for circuit discovery. Our framework wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. Unstable neurons are abstained from, yielding circuits that are more compact and more accurate. On ImageNet and OOD datasets, certified circuits achieve up to 91% higher accuracy while using 45% fewer neurons, and remain reliable where baselines degrade. Certified Circuits puts circuit discovery on formal ground by producing mechanistic explanations that are provably stable and better aligned with the target concept. Code will be released soon!

[5] h6: Keywords:

[6] p: (a) Certified circuits, here for ‘African crocodile’, remove spurious cues. (b) Certified circuits are more compact (x) and more accurate (y).

[7] figure: Figure 1 : Certified circuits are smaller, more accurate, and generalize to OOD. Given a concept dataset, we isolate a circuit—a subnetwork encoding that concept—that is provably stable under dataset edits. (a) Certified circuits keep stable semantic neurons (e.g., teeth) and abstain from unstable spurious ones (e.g., bird cues), improving circuit-only accuracy to 94 % 94\% ( 62 % 62\% over baseline). (b) Across distribution shifts, ImageNet-discovered certified circuits ( ⧫ \blacklozenge ) are significantly smaller and more accurate than baseline circuits ( ∙ \bullet ).

[8] h2: 1 Introduction

[9] p: Understanding how neural networks arrive at their predictions is a central challenge in machine learning. Mechanistic interpretability tackles this by identifying circuits —minimal subnetworks responsible for specific model behaviors ( Olah et al., 2020 ; Conmy et al., 2023 ; Elhage et al., 2021 ) . In vision models, for instance, a circuit for recognizing “dog” might comprise particular convolutional filters detecting fur texture, ears, and eyes, connected through specific neurons across subsequent layers. Discovering such circuits promises not only scientific insight into learned representations but also practical benefits: debugging failure modes, auditing for biases, and enabling targeted model editing.

[10] p: Circuit discovery methods have emerged across modalities. In language models, activation patching and causal tracing isolate attention heads and MLP neurons responsible for factual recall, indirect object identification, and other behaviors ( Meng et al., 2022 ; Wang et al., 2023 ; Goldowsky-Dill et al., 2023 ) . In vision, analogous methods prune model components to find minimal sufficient subnetworks for recognizing specific visual concepts ( Rajaram et al., 2024 ; Olah et al., 2020 ; Dreyer et al., 2024 ) . These approaches start with a concept dataset : a collection of inputs representing the target behavior. They then identify which model components are necessary and sufficient to maintain performance on this dataset, discarding the rest. The result is a sparse circuit, i.e., a subgraph of the full model graph that is intended to capture the mechanistic basis of the behavior.

[11] p: However, current circuit discovery methods lack robustness ( Méloux et al., 2025 ; uit de Bos and Garriga-Alonso, 2024 ; Miller et al., 2024 ; Friedman et al., 2024 ) . The identified circuits are sensitive to the choice of concept dataset: adding, removing, or substituting a few semantically equivalent examples can change the discovered circuit unpredictably. They also fail to generalize to out-of-distribution (OOD) data. A circuit found using photographs of dogs on grass may perform poorly on dogs in snow, cartoon dogs, or dogs from unusual angles. Both issues stem from the same underlying problem—current methods overfit to the particular concept dataset rather than recovering the actual concept representation. This undermines confidence in the mechanistic explanation these methods produce.

[12] p: To address this, we introduce Certified Circuits (Fig. 2 ), a framework that computes the first provable robustness guarantees for circuit discovery. Given a concept dataset

[13] p: 𝒟 \mathcal{D} and any black-box circuit discovery algorithm, we construct a certified circuit C ∗ C^{*} with the following guarantee:

[14] p: Edit distance counts insertions, deletions, or substitutions of examples—so r = 5 r=5 guarantees stability under any combination of up to five such changes. This covers an exponentially large family of datasets.

[15] p: Our framework is algorithm-agnostic : we (i) randomly subsample the concept dataset several times, (ii) run the base algorithm on each subsample to obtain candidate circuits, and (iii) aggregate votes at the level of individual neurons to determine which components are guaranteed to represent the concept across perturbed datasets. A key byproduct is adaptive sparsity : certification identifies neurons for which no robust decision can be made, yielding circuits that are more compact and accurate than fixed top- K K baselines.

[16] p: In summary, we make the following contributions :

[17] p: We introduce Certified Circuits , the first framework providing provable, algorithm-agnostic robustness guarantees for circuit discovery.

[18] p: We derive provable bounds on certified radii and characterize their dependence on a probability threshold and deletion probability required for subsampling.

[19] p: We demonstrate empirically that certified circuits are more compact , have higher sufficiency , and generalize better to OOD data than uncertified alternatives.

[20] p: We validate Certified Circuits on ImageNet classification, evaluating sufficiency (does the circuit preserve model behavior?) and compactness (how small can the circuit be while sufficient?) across in-distribution and four OOD benchmarks (OOD-CV, ImageNet-A, ImageNet-O, ImageNet-C). Certified circuits consistently outperform uncertified baselines: certified accuracy improves by up to 91% on OOD data, while circuit size decreases by up to 45%. These gains hold across scoring functions (relevance, activation, rank) used to discover the circuit, confirming that certification captures more transferable mechanistic structure while pruning neurons that are not robustly necessary (Fig. 1 ). We further analyze whether certified circuits converge to structurally similar solutions when re-discovered on shifted distributions of the same concept. Our Certified Circuits lift classic circuit-based mechanistic explanations to provably robust and more compact explanations that empirically better generalize to OOD data.

[21] h2: 2 Related works

[22] h3: 2.1 Mechanistic Interpretability

[23] p: Mechanistic interpretability aims to reverse-engineer the internal computations of neural networks, moving beyond input-output behavior to understand how models arrive at their predictions ( Olah et al., 2020 ; Elhage et al., 2021 ; Bereska and Gavves, 2024 ) . The field spans observational methods that analyze learned representations (e.g., probing, sparse autoencoders) and interventional methods that causally localize computations through targeted ablations and activation patching ( Zeiler and Fergus, 2014 ; Zimmermann et al., 2021 ; Meng et al., 2022 ) .

[24] p: Circuit discovery. Circuit discovery aims to identify minimal subnetworks ( circuits ) that implement a target behavior or concept. Circuit nodes can be feature channels in CNNs, attention heads in transformers, or MLP neurons, depending on the chosen granularity ( Bereska and Gavves, 2024 ) . Typically, one (i) defines a concept via a dataset, (ii) represents the model as a computational graph with nodes and edges connecting them, and (iii) extracts a sparse subgraph whose components are necessary and/or sufficient for that behavior ( Conmy et al., 2023 ) . In language models, this approach has revealed circuits for factual recall ( Meng et al., 2022 ) , indirect object identification ( Wang et al., 2023 ) , and most recently for verifying chain-of-thought reasoning ( Zhao et al., 2025 ) . ACDC ( Conmy et al., 2023 ) automates discovery via iterative edge pruning. In vision, circuits have been studied via feature-preserving subnetworks ( Hamblin et al., 2022 ) , connectivity-based tracing of concept-specific computations ( Rajaram et al., 2024 ; Wang et al., 2019 ) , disentanglement of polysemantic neurons into concept circuits ( Dreyer et al., 2024 ) , and qualitative connectome-style visualizations spanning all layers ( Kowal et al., 2024 ) .

[25] p: Stability limitations. A core limitation is that discovered circuits can be highly unstable : swapping in different (but semantically equivalent) examples to represent the same concept (or making small additions/removals) can yield substantially different circuit. This raises a basic question: is the circuit capturing the concept, or overfitting to dataset-specific spurious cues? Recent work documents and diagnoses such fragility. Méloux et al. (2025) cast circuit discovery as statistical estimation and show that EAP-IG (transformer circuit discovery method) circuits can change markedly even when the same behavior is defined using paraphrased prompt sets, indicating high variance in the discovered structure. Miller et al. (2024) further find that common circuit faithfulness metrics are not robust to evaluation choices. Finally, Friedman et al. (2024) show that explanations can appear faithful on the discovery distribution yet fail to generalize, creating interpretability illusions .

[26] p: These works highlight the problem but do not provide solutions that rule out instability. Concurrent work uses neural network verification to certify the faithfulness of a fixed circuit under small input-level perturbations ( Anonymous, 2026 ) ; in contrast, our concern is dataset-to-circuit instability, where the discovered circuit itself changes when the concept dataset is edited. To our knowledge, no prior method certifies invariance of circuit structure under bounded dataset-level perturbations.

[27] h3: 2.2 Robustness Certification

[28] p: A robustness certificate is a worst-case guarantee of output invariance : given an input x x and a radius r r , the certified model provably returns the same prediction for every perturbed input x ′ x^{\prime} with dist ⁡ ( x , x ′ ) ≤ r \mathrm{dist}(x,x^{\prime})\leq r (otherwise it abstains). Randomized smoothing yields such certificates by aggregating the base model’s predictions under random perturbations and converting the resulting probability margin into a certified radius ( Lécuyer et al., 2019 ; Cohen et al., 2019 ; Anani et al., 2025 ) . Beyond single-label classification, smoothing has been extended to (i) structured outputs via per-component abstention, certifying only confident components in segmentation settings ( Fischer et al., 2021 ; Anani et al., 2024 ) , and (ii) discrete objects under edit distance, where RS-Del uses randomized deletions to certify invariance against insertions, deletions, and substitutions within an edit budget ( Huang et al., 2023 ) . We build on these ideas to certify circuit component stability under dataset -level edit perturbations.

[29] p: Summary. Circuit discovery is unstable: small edits to the concept dataset, even replacing examples with semantically equivalent ones, can produce entirely different circuits, blurring whether the circuit encodes the concept or dataset-specific artifacts. We address this by certifying the dataset-to-circuit mapping: using deletion-based smoothing (RS-Del) ( Huang et al., 2023 ) to model bounded dataset edits, together with circuit component-level certification to exclude the unstable circuit components ( Fischer et al., 2021 ) , we return certified circuits whose certified nodes are provably invariant to edits within an edit-distance budget.

[30] h2: 3 Certified Circuits

[31] p: To overcome the circuit instability in prior work, we formalize circuit discovery as a dataset-level mapping and ask: which circuit components are provably stable under bounded edits to the concept dataset? Our approach is driven by three goals. First, we seek guarantees (not empirical heuristics) that circuit structure is invariant, ruling out brittleness by construction. Second, edit distance provides a threat model: it captures the scenario where a practitioner adds examples, removes outliers, or swaps in semantically equivalent images, and expects the discovered circuit to remain unchanged if it encodes the concept. Third, stability under such edits is a prerequisite for out-of-distribution generalization : a circuit that changes when the concept dataset is perturbed cannot be expected to transfer to shifted test distributions. Enumerating all bounded-edit datasets is infeasible, so we use randomized smoothing: we run circuit discovery on many random subsamples and aggregate the outcomes to certify stability for all edits within the radius.

[32] figure: Figure 2 : Certified circuit discovery via concept deletion smoothing. (§ 3.1 ) Given a concept dataset 𝒟 \mathcal{D} , model graph G G , and circuit discovery algorithm A A : (§ 3.2 ) We sample dataset variants via per-example random deletion with probability p del p_{\mathrm{del}} , (§ 3.3 ) run A A on each to obtain candidate circuits, (§ 3.4 ) aggregate per-vertex inclusion frequencies, (§ 3.4 ) certify vertices as in , out , or abstain ( ⊘ \oslash ) based on votes consistency. (§ 3.5 ) The certified circuit is provably invariant to dataset edits within radius r r .

[33] p: Our approach (Figure 2 ). Given a model graph G = ( 𝒱 , ℰ ) G{=}(\mathcal{V},\mathcal{E}) , a concept dataset 𝒟 \mathcal{D} , and any black-box circuit discovery algorithm A A , we certify which circuit components (vertices v ∈ 𝒱 v\in\mathcal{V} ) are provably stable under bounded dataset edits. After briefly reviewing randomized smoothing, we formalize our setup (§ 3.1 ). We then define dataset deletion smoothing (RS-Del ( Huang et al., 2023 ) ; § 3.2 ) and a smoothed circuit discovery rule that aggregates vertex-wise inclusion probabilities and thresholds them to output certified in/out or abstain (§ 3.3 ). We present Theorem 3.3 , which guarantees certified decisions are invariant for all datasets within edit-distance r r . Finally, we describe the Monte Carlo estimation of the certified circuit discovery algorithm (§ 3.4 ) and summarize its key properties (§ 3.5 ).

[34] h3: Background: Randomized Smoothing

[35] p: We introduce randomized smoothing ( Lécuyer et al., 2019 ; Cohen et al., 2019 ) as the main technical tool for turning empirical stability under random perturbations into certified robustness guarantees. Let f b : 𝒳 → 𝒴 f_{b}:\mathcal{X}\to\mathcal{Y} be a base classifier and let ϕ : 𝒳 → D ⁡ ( 𝒳 ) \phi:\mathcal{X}\to D(\mathcal{X}) be a perturbation mechanism that maps an input x x to a distribution ϕ ⁡ ( x ) \phi(x) over perturbed inputs. Randomized smoothing defines the smoothed classifier

[36] table: f ( x ) := arg max y ∈ 𝒴 ℙ z ∼ ϕ ⁡ ( x ) [ f b ( z ) = y ] . f(x):=\arg\max_{y\in\mathcal{Y}}\mathbb{P}_{z\sim\phi(x)}\!\left[f_{b}(z)=y\right]. (1)

[37] p: A certificate is obtained by lower-bounding the probability of the predicted class and deriving a radius r r such that, with confidence at least 1 − α 1-\alpha , the prediction is invariant within the corresponding neighborhood, i.e., f ⁡ ( x ) = f ⁡ ( x ′ ) f(x)=f(x^{\prime}) for all x ′ x^{\prime} satisfying dist ⁡ ( x , x ′ ) ≤ r \mathrm{dist}(x,x^{\prime})\leq r .

[38] h3: 3.1 Setup and Inputs

[39] p: Let G = ( 𝒱 , ℰ ) G=(\mathcal{V},\mathcal{E}) denote the model, represented as a directed graph whose vertices 𝒱 \mathcal{V} are circuit components (e.g., neurons, attention heads) and whose edges ℰ \mathcal{E} represent connections between components. Our method operates on a concept dataset 𝒟 = ( x 1 , … , x | 𝒟 | ) ∈ 𝒳 ∗ \mathcal{D}=(x_{1},\ldots,x_{|\mathcal{D}|})\in\mathcal{X}^{*} , viewed as a finite sequence of inputs that contain the same concept (e.g., same-class images).

[40] p: Assume any black-box circuit discovery algorithm A A that maps a concept dataset to a binary mask over vertices,

[41] table: A : 𝒳 ∗ ⟶ { 0 , 1 } | 𝒱 | , A:\mathcal{X}^{*}\;\longrightarrow\;\{0,1\}^{|\mathcal{V}|}, (2)

[42] p: where A v ​ ( 𝒟 ) = 1 A_{v}(\mathcal{D})=1 indicates that vertex v ∈ 𝒱 v\in\mathcal{V} is included in the circuit associated with 𝒟 \mathcal{D} and A v ​ ( 𝒟 ) = 0 A_{v}(\mathcal{D})=0 indicates exclusion. A common example of algorithm A A is a top- K K circuit rule: for each layer, score vertices on 𝒟 \mathcal{D} (e.g., by mean activation or gradient-based relevance) and include the K K -fraction highest-scoring vertices, yielding a sparse mask over components v ∈ 𝒱 v\in\mathcal{V} ( Olah et al., 2020 ; Hamblin et al., 2022 ; Rajaram et al., 2024 ; Dreyer et al., 2024 ) .

[43] p: The goal is to construct a smoothed (certified) variant A ~ τ \tilde{A}^{\tau} of A A whose component-wise decisions are provably stable under bounded edit perturbations of 𝒟 \mathcal{D} .

[44] h3: 3.2 Dataset Deletion Smoothing

[45] p: To certify robustness of circuit discovery under dataset-level edits, we model the concept dataset 𝒟 = ( x 1 , … , x | 𝒟 | ) \mathcal{D}=(x_{1},\ldots,x_{|\mathcal{D}|}) as a sequence and measure perturbations via edit distance dist edit ​ ( 𝒟 , 𝒟 ′ ) \mathrm{dist}_{\mathrm{edit}}(\mathcal{D},\mathcal{D}^{\prime}) , counting insertions, deletions, and substitutions required to transform 𝒟 \mathcal{D} to 𝒟 ′ \mathcal{D}^{\prime} . Directly checking stability under all edits is intractable; instead, following RS-Del ( Huang et al., 2023 ) , we use randomized deletions as a smoothing perturbation, which nevertheless yields certificates with respect to the full edit distance. Although concept datasets are naturally unordered, we fix an arbitrary ordering solely to define dist edit \mathrm{dist}_{\mathrm{edit}} ; this does not affect the certificate since our base algorithms A A depend only on permutation-invariant statistics.

[46] p: Concretely, we define a deletion-based perturbation distribution ϕ p del ​ ( 𝒟 ) \phi_{p_{\mathrm{del}}}(\mathcal{D}) by sampling an i.i.d. binary mask

[47] table: ε = ( ε 1 , … , ε | 𝒟 | ) , ε i ∼ Bernoulli ⁡ ( 1 − p del ) , \varepsilon=(\varepsilon_{1},\ldots,\varepsilon_{|\mathcal{D}|}),\qquad\varepsilon_{i}\sim\mathrm{Bernoulli}(1-p_{\mathrm{del}}),

[48] p: where ε i = 1 \varepsilon_{i}=1 keeps x i x_{i} and ε i = 0 \varepsilon_{i}=0 deletes it. We treat the concept dataset as an ordered sequence 𝒟 = ( x 1 , … , x | 𝒟 | ) \mathcal{D}=(x_{1},\ldots,x_{|\mathcal{D}|}) (e.g., in dataset index order), so applying ε \varepsilon produces an ordered subsequence :

[49] table: 𝒟 ⊙ ε \displaystyle\mathcal{D}\odot\varepsilon : = ( x i ∣ ε i = 1 ) \displaystyle:=(x_{i}\mid\varepsilon_{i}=1) = ( x i 1 , … , x i m ) , with 1 ≤ i 1 < ⋯ < i m ≤ | 𝒟 | . \displaystyle=(x_{i_{1}},\ldots,x_{i_{m}}),\quad\text{with }1\leq i_{1}<\cdots<i_{m}\leq|\mathcal{D}|.

[50] p: The random sub-dataset 𝒟 ⊙ ε \mathcal{D}\odot\varepsilon is distributed according to ϕ p del ​ ( 𝒟 ) \phi_{p_{\mathrm{del}}}(\mathcal{D}) . This perturbation model is the input-side mechanism underlying our certified guarantees, and it directly connects our setting to RS-Del’s edit-distance certification under deletion-based smoothing ( Huang et al., 2023 ) .

[51] h3: 3.3 Smoothed Circuit Discovery

[52] p: Given a base circuit discovery algorithm A A and the deletion perturbation distribution ϕ p del ​ ( 𝒟 ) \phi_{p_{\mathrm{del}}}(\mathcal{D}) , we define the smoothed circuit discovery algorithm

[53] table: A ~ τ : 𝒳 ∗ → { 0 , 1 , ⊘ } | 𝒱 | , \tilde{A}^{\tau}:\mathcal{X}^{*}\to\{0,1,\oslash\}^{|\mathcal{V}|},

[54] p: which returns for each vertex v ∈ 𝒱 v\in\mathcal{V} one of three outcomes: certified in (1), certified out (0), or abstain ( ⊘ \oslash ). The confidence threshold τ ∈ [ 0.5 , 1 ) \tau\in[0.5,1) controls how much posterior mass is required to make a non-abstaining decision: if neither inclusion nor exclusion is sufficiently likely under randomized deletions, the method abstains.

[55] p: To define A ~ τ \tilde{A}^{\tau} , we quantify how consistently the base algorithm A A includes a vertex under randomized deletions. For a vertex v v , we define the smoothed inclusion probability :

[56] table: p v ​ ( 𝒟 ) \displaystyle p_{v}(\mathcal{D}) : = ℙ ε [ A v ( 𝒟 ⊙ ε ) = 1 ] , \displaystyle:=\mathbb{P}_{\varepsilon}\!\left[A_{v}\!\big(\mathcal{D}\odot\varepsilon\big)=1\right], (3) ε i ∼ Bernoulli ⁡ ( 1 − p del ) ​ i.i.d. \displaystyle\varepsilon_{i}\sim\mathrm{Bernoulli}(1-p_{\mathrm{del}})\ \text{i.i.d.}

[57] p: i.e., the probability that A A includes v v when run on a randomly deleted sub-dataset 𝒟 ⊙ ε \mathcal{D}\odot\varepsilon . Values near 1 1 mean v v is selected almost always (stable inclusion), while values near 0 0 mean it is rarely selected (stable exclusion).

[58] p: The smoothed algorithm A ~ τ \tilde{A}^{\tau} converts these probabilities into certified per-vertex decisions by requiring a margin of at least τ \tau in favor of inclusion or exclusion. Following segmentation-style smoothing ( Fischer et al., 2021 ) , we set

[59] table: A ~ v τ ​ ( 𝒟 ) = { 1 if ​ p v ​ ( 𝒟 ) > τ , 0 if ​ 1 − p v ​ ( 𝒟 ) > τ , ⊘ otherwise , \tilde{A}^{\tau}_{v}(\mathcal{D})=\begin{cases}1&\text{if }p_{v}(\mathcal{D})>\tau,\\ 0&\text{if }1-p_{v}(\mathcal{D})>\tau,\\ \oslash&\text{otherwise},\end{cases} (4)

[60] p: so A ~ v τ ​ ( 𝒟 ) = 1 \tilde{A}^{\tau}_{v}(\mathcal{D})=1 certifies that v v is robustly included, A ~ v τ ​ ( 𝒟 ) = 0 \tilde{A}^{\tau}_{v}(\mathcal{D})=0 certifies that it is robustly excluded, and A ~ v τ ( 𝒟 ) = ⊘ \tilde{A}^{\tau}_{v}(\mathcal{D})=\oslash abstains when neither decision has enough evidence. We write A ~ τ ( 𝒟 ) := ( A ~ v τ ( 𝒟 ) ) v ∈ 𝒱 ∈ { 0 , 1 , ⊘ } | 𝒱 | \tilde{A}^{\tau}(\mathcal{D}):=(\tilde{A}^{\tau}_{v}(\mathcal{D}))_{v\in\mathcal{V}}\in\{0,1,\oslash\}^{|\mathcal{V}|} for the resulting three-valued mask over all vertices.

[61] p: Guarantees. The rule defining A ~ τ \tilde{A}^{\tau} converts vote consistency under randomized deletions into a worst-case guarantee over all datasets within an edit-distance neighborhood of 𝒟 \mathcal{D} . Combining RS-Del ( Huang et al., 2023 ) with component-wise certification ( Fischer et al., 2021 ) yields a certified stability guarantee for every non-abstaining vertex:

[62] p: The guarantee in Theorem 3.3 states that any vertex that A ~ τ \tilde{A}^{\tau} certifies as in ( 1 1 ) or out ( 0 0 ) of the circuit remains so for all concept datasets 𝒟 ′ \mathcal{D}^{\prime} with dist edit ​ ( 𝒟 , 𝒟 ′ ) < r \mathrm{dist}_{\mathrm{edit}}(\mathcal{D},\mathcal{D}^{\prime})<r , with confidence at least 1 − α 1-\alpha . Vertices assigned ⊘ \oslash are excluded from the certified circuit. The proof is in App. A .

[63] p: From certified mask to a circuit. Given the per-vertex guarantee in Theorem 3.3 , we can now formally define the certified circuit itself. The certified output A ~ τ ( 𝒟 ) ∈ { 0 , 1 , ⊘ } | 𝒱 | \tilde{A}^{\tau}(\mathcal{D})\in\{0,1,\oslash\}^{|\mathcal{V}|} is a vertex-wise mask, so we construct a circuit as the subgraph induced by the vertices certified as included:

[64] table: 𝒱 ∗ \displaystyle\mathcal{V}^{*} : = { v ∈ 𝒱 ∣ A ~ v τ ​ ( 𝒟 ) = 1 } , \displaystyle:=\{v\in\mathcal{V}\mid\tilde{A}^{\tau}_{v}(\mathcal{D})=1\}, ℰ ∗ \displaystyle\mathcal{E}^{*} : = { ( u , v ) ∈ ℰ ∣ u ∈ 𝒱 ∗ ∧ v ∈ 𝒱 ∗ } , \displaystyle:=\{(u,v)\in\mathcal{E}\mid u\in\mathcal{V}^{*}\land v\in\mathcal{V}^{*}\}, C ∗ \displaystyle C^{*} : = ( 𝒱 ∗ , ℰ ∗ ) . \displaystyle:=(\mathcal{V}^{*},\mathcal{E}^{*}).

[65] p: Thus C ∗ C^{*} contains all certified-in vertices and all edges between them, while vertices assigned ⊘ \oslash are excluded since their membership cannot be certified stable.

[66] h3: 3.4 Estimating the Certified Circuit

[67] p: In practice, the probabilities p v ​ ( 𝒟 ) p_{v}(\mathcal{D}) (Eq. 3 ) are unknown and are estimated by Monte Carlo sampling: draw n n i.i.d. deletion masks ε ( 1 ) , … , ε ( n ) ∼ Bernoulli ​ ( 1 − p del ) | 𝒟 | \varepsilon^{(1)},\ldots,\varepsilon^{(n)}\sim\mathrm{Bernoulli}(1-p_{\mathrm{del}})^{|\mathcal{D}|} , evaluate A v ​ ( 𝒟 ⊙ ε ( j ) ) A_{v}(\mathcal{D}\odot\varepsilon^{(j)}) for each j j , and use the resulting empirical frequency to estimate the lower bound of p v ​ ( 𝒟 ) p_{v}(\mathcal{D}) , from which a ( 1 − α ) (1-\alpha) lower confidence bound is computed to decide whether A ~ v τ ​ ( 𝒟 ) ∈ { 0 , 1 } \tilde{A}_{v}^{\tau}(\mathcal{D})\in\{0,1\} or ⊘ \oslash . We follow the standard evaluation scheme as in ( Fischer et al., 2021 ) .

[68] h3: 3.5 Properties of Certified Circuits

[69] p: Smoothed circuit discovery yields certified circuits with three key properties: (i) provable dataset-level stability : all non-abstain certified vertices are invariant under any sequence of fewer than r r dataset edits; (ii) spurious-feature suppression : vertices whose membership decisions are unstable across deletions are abstained from, producing strictly sparser circuits; and (iii) algorithm and model agnosticism : our framework wraps any circuit discovery method A A and model G G without requiring access to its internals. Next, we will discuss that Certified Circuits also have practical benefits, better capturing the target concept prediction and generalizing well to OOD data.

[70] h2: 4 Experimental Setup

[71] p: Baseline circuit discovery algorithms. We evaluate our certification framework using a standard top- K K based circuit discovery flow ( Hamblin et al., 2022 ; Conmy et al., 2023 ; Rajaram et al., 2024 ; Dreyer et al., 2024 ) . Given a model, we define circuit vertices as feature channels at the output of each residual block. For each concept dataset, we score every vertex and retain the top- K K fraction per layer (i.e., the K ⋅ | channels | K\cdot|\text{channels}| highest-scoring channels) according to one of three scoring functions, which defines our base circuit discovery algorithm A A (Eq. 2 ). As scores we consider (i) Activation : mean activation magnitude over the concept dataset; (ii) Relevance : mean attribution score; or (iii) Rank : per-image ranking of vertices by activation, aggregated across the dataset. Because certification abstains from unstable vertices, the certified circuit is typically smaller than the initial top- K K selection; therefore, whenever we report K K for certified circuits we report the effective retained fraction after abstention (not the base algorithm’s target K K ).

[72] p: Datasets and architectures. We use ImageNet ( Russakovsky et al., 2015 ) as an in-distribution benchmark, with each class as a concept dataset 𝒟 \mathcal{D} by collecting a set of same-class images. Circuits are discovered on 100 randomly selected classes and evaluated under four OOD shifts: OOD-CV , where objects appear in novel contexts and backgrounds ( Zhao et al., 2022 ) ; ImageNet-A , consisting of naturally occurring adversarial examples ( Hendrycks et al., 2019 ) ; ImageNet-O , containing object categories absent from ImageNet ( Hendrycks et al., 2019 ) ; and ImageNet-C (defocus blur), a corruption shift induced by optical blur ( Hendrycks and Dietterich, 2019 ) . We run experiments on ResNet-50 and ResNet-101 ( He et al., 2016 ) , selecting circuit vertices from the outputs of their four residual blocks (256, 512, 1024, and 2048 channels, respectively).

[73] p: Sufficiency. We measure circuit sufficiency by whether the model’s prediction is preserved when computation is restricted to the discovered circuit. This sufficiency pruning evaluation is standard in circuit discovery: one ablates all non-circuit components (or equivalently, runs the model with only the circuit active) and measures task performance using the remaining subnetwork ( Conmy et al., 2023 ; Meng et al., 2022 ; Wang et al., 2023 ; Dreyer et al., 2024 ) . Concretely, for a circuit C c C_{c} discovered for class c c , we zero all non-circuit channels at each residual block and evaluate the pruned model on the corresponding concept dataset 𝒟 c \mathcal{D}_{c} . We report mean circuit class accuracy (cACC), the average classification accuracy across evaluated classes:

[74] table: cACC := 1 | 𝒴 | ​ ∑ c ∈ 𝒴 CA ⁡ ( C c , 𝒟 c ) , \mathrm{cACC}:=\frac{1}{|\mathcal{Y}|}\sum_{c\in\mathcal{Y}}\mathrm{CA}(C_{c},\mathcal{D}_{c}), (6)

[75] p: where 𝒴 \mathcal{Y} is the set of evaluated classes and CA ⁡ ( C c , 𝒟 c ) \mathrm{CA}(C_{c},\mathcal{D}_{c}) is the classification accuracy of the pruned model (retaining only C c C_{c} ) on 𝒟 c \mathcal{D}_{c} .

[76] p: Certification hyperparameters. The choice of p del p_{\mathrm{del}} and τ \tau is critical: high p del p_{\mathrm{del}} deletes too much data, hindering the base algorithm, while high τ \tau demands excessive confidence for certification, which increases the abstain rate. We analyze the certified radius r r in App. B (Figure 5 ). Based on this analysis, we set p del = 0.6 p_{\mathrm{del}}=0.6 and τ = 0.95 \tau=0.95 , yielding certified radius r = 1 r=1 . We use n = 1000 n=1000 Monte Carlo samples and failure probability α = 0.001 \alpha=0.001 , following the standard setting in randomized smoothing literature ( Lécuyer et al., 2019 ; Cohen et al., 2019 ; Anani et al., 2025 ) . All certified results are guaranteed with confidence 1 − α 1-\alpha .

[77] figure: Paradigm Scoring Top- K K In-Distribution Out-of-Distribution ImageNet OOD-CV ImageNet-A ImageNet-O ImageNet-C cACC ↑ \mathrm{cACC}\uparrow K ↓ K\downarrow cACC ↑ \mathrm{cACC}\uparrow K ↓ K\downarrow cACC ↑ \mathrm{cACC}\uparrow K ↓ K\downarrow cACC ↑ \mathrm{cACC}\uparrow K ↓ K\downarrow cACC ↑ \mathrm{cACC}\uparrow K ↓ K\downarrow Model – 81 1.00 20 1.00 9 1.00 81 1.00 59 1.00 Baseline circuit Relevance 86 0.70 74 0.40 62 0.40 93 0.60 74 0.70 Activation 83 0.80 37 0.40 19 0.60 87 0.70 68 0.70 Rank 47 0.70 40 0.40 16 0.60 60 0.70 43 0.70 Certified circuit (ours) Relevance 96 ↑ 12 % \uparrow\!12\% 0.34 ↓ 51 % \downarrow\!51\% 93 ↑ 25 % \uparrow\!25\% 0.34 ↓ 16 % \downarrow\!16\% 94 ↑ 51 % \uparrow\!51\% 0.34 ↓ 14 % \downarrow\!14\% 98 ↑ 6 % \uparrow\!6\% 0.42 ↓ 30 % \downarrow\!30\% 93 ↑ 26 % \uparrow\!26\% 0.34 ↓ 51 % \downarrow\!51\% Activation 84 ↑ 1 % \uparrow\!1\% 0.61 ↓ 24 % \downarrow\!24\% 53 ↑ 46 % \uparrow\!46\% 0.27 ↓ 33 % \downarrow\!33\% 37 ↑ 91 % \uparrow\!91\% 0.33 ↓ 45 % \downarrow\!45\% 90 ↑ 3 % \uparrow\!3\% 0.49 ↓ 30 % \downarrow\!30\% 72 ↑ 6 % \uparrow\!6\% 0.50 ↓ 28 % \downarrow\!28\% Rank 83 ↑ 76 % \uparrow\!76\% 0.69 ↓ 1 % \downarrow\!1\% 46 ↑ 16 % \uparrow\!16\% 0.38 ↓ 4 % \downarrow\!4\% 28 ↑ 72 % \uparrow\!72\% 0.58 ↓ 3 % \downarrow\!3\% 90 ↑ 50 % \uparrow\!50\% 0.57 ↓ 18 % \downarrow\!18\% 71 ↑ 66 % \uparrow\!66\% 0.58 ↓ 17 % \downarrow\!17\% Table 1: Certified vs. baseline circuit sufficiency. Peak cACC and corresponding circuit size K K under sufficiency pruning on ResNet-101. Circuits are discovered on ImageNet and evaluated either in-distribution or on OOD shifts.

[78] h2: 5 Results

[79] p: We evaluate Certified Circuits in three ways: circuit sufficiency and compactness (§ 5.1 ), testing whether circuits preserve class predictions when used in isolation and how small they can be; out-of-distribution generalization (§ 5.2 ), measuring whether circuits discovered in-distribution retain accuracy under distribution shift; and structural stability (§ 5.3 ), assessing whether circuit structure remains consistent when re-discovered on shifted data.

[80] figure: Figure 3 : Circuit accuracy (cACC) vs. size K K . Solid lines show certified circuits, dashed show baselines, with colors distinguishing models. Rows vary scoring methods, columns vary datasets. Circuits are discovered on ImageNet and evaluated on OOD data.

[81] h3: 5.1 Circuit Sufficiency and Compactness

[82] p: We study two questions: (i) sufficiency : does the circuit alone preserve the target class prediction? and (ii) compactness : how small can the circuit be while remaining sufficient? We sweep the circuit size K ∈ ( 0 , 1 ] K\in(0,1] (fraction of channels retained), and report (a) the peak cACC over K K and the corresponding K K (Table 1 ), as well as (b) the full cACC– K K curves (Fig. 3 ) across five test datasets and three scoring rules (Relevance, Activation, Rank).

[83] p: Sufficiency. Does using the circuit alone preserve the class prediction? We evaluate circuit sufficiency via peak cACC (Eq. 6 ) in Table 1 and cACC across circuit sizes K K in Figure 3 . In general, certified circuits consistently outperform baselines across all five datasets and all three scoring algorithms. On ImageNet, certified circuits ( 96 % 96\% peak cACC) increase upon the baseline ( 86 % 86\% ) by 12 % 12\% . Importantly, the accuracy on non-target class images is decreased for certified circuits. Thus, they yield more class-specific circuits, even on OOD data (see App. C ).

[84] p: Compactness. How small can the circuit be while sufficient? We assess compactness by the circuit size K K at which peak mean class accuracy (cACC) is achieved. Table 1 and Figure 3 show that certified circuits generally reach peak cACC at substantially smaller K K than baseline circuits. On ImageNet, the certified circuit is 51 % 51\% smaller while improving peak cACC by 12 % 12\% .

[85] p: Effect of compactness on sufficiency. In Figure 3 we show cACC against circuit size K ∈ ( 0 , 1 ) K\in(0,1) across all five datasets. Both certified and baseline circuits follow a three-stage pattern as K K increases: (i) small K K yields insufficient circuits that omit class-critical neurons, low cACC, (ii) intermediate K K captures the necessary class evidence and cACC peaks, (iii) large K K introduces competing or spurious features, reducing class specificity and degrading cACC. Crucially, certified circuits shift this curve favorably in both dimensions: they peak at smaller K K (more compact) and achieve higher cACC at that peak (more sufficient). This means certification does not trade off one property for the other. Certification appears to prune those neurons that are unnecessary (enabling compactness) and harmful to the accuracy (enabling sufficiency) at the same time.

[86] h3: 5.2 Out-of-Distribution Generalization

[87] p: Do circuits discovered in-distribution retain their class accuracy on shifted data? We evaluate OOD generalization by discovering class-specific circuits on ImageNet and using these circuits to classify corresponding classes in shifted datasets by measuring cACC.(Table 1 , Figure 3 ).

[88] p: In general, certified circuits retain substantially higher cACC than baselines under distribution shifts, with the largest gains on the hardest shifts. Specifically, on OOD-CV (context and background shift), certified circuits reach 93 % 93\% cACC at K = 0.34 K{=}0.34 versus 74 % 74\% at K = 0.40 K{=}0.40 for the baseline ( 25 % 25\% increase), while the unmodified model ( K = 1.0 K{=}1.0 ) drops to ∼ 20 % {\sim}20\% . On ImageNet-A (natural adversarial examples), certified circuits achieve 94 % 94\% at K = 0.34 K{=}0.34 versus 62 % 62\% baseline ( 51 % 51\% increase), whereas the full model attains only ∼ 9 % {\sim}9\% . On ImageNet-C (corruption), certified circuits improve by 26 % 26\% over baseline while using 51 % 51\% fewer neurons.

[89] p: These results suggest certified circuits capture class-relevant features that transfer across shifts. Abstention removes neurons whose inclusion is inconsistent under dataset perturbations, which are likely spurious rather than concept-based. Pruning these unstable components yields circuits that generalize beyond the discovery distribution and outperform both baselines and the full network.

[90] h3: 5.3 Structural Stability Under Distribution Shift

[91] p: The previous experiments used the same circuit on different distributions. A stronger test asks: does the certified circuit structure remain stable beyond the certified radius, when re-discovered on different distributions of the same concept? We measure this via IoU between circuits discovered on ImageNet and re-discovered on each shifted dataset, at the K K maximizing the certified–baseline cACC gap (Fig. 4 ). For two circuits with vertices sets V V and V ′ V^{\prime} , the IoU is defined | V ∩ V ′ | / | V ∪ V ′ | |V\cap V^{\prime}|/|V\cup V^{\prime}| .

[92] figure: Figure 4 : Structural stability under distribution shift. Per-class IoU between circuits discovered on ImageNet and re-discovered on each OOD dataset, evaluated at the K K that maximizes the certified–baseline Δ \Delta cACC = 100 ⋅ cACC cert − cACC base cACC base 100\cdot\frac{\mathrm{cACC}_{\mathrm{cert}}-\mathrm{cACC}_{\mathrm{base}}}{\mathrm{cACC}_{\mathrm{base}}} gap. Boxes show the distribution over classes. Relevance top- K K scoring is used.

[93] p: Overall, certified circuits have higher median IoU and tighter distributions than baselines across shifts, indicating more consistent structure. The largest stability gains align with the largest Δ ​ c ​ A ​ C ​ C \Delta cACC performance gains on OOD-CV 104 % 104\% and ImageNet-A 83 % 83\% . ImageNet-O is the exception, where both methods show high variance, suggesting class-dependent circuit reconfiguration under semantic anomalies.

[94] p: These findings reinforce the OOD generalization results: abstention suppresses shift-sensitive vertices, concentrating circuits on an invariant core that better captures the underlying concept rather than distribution-specific artifacts.

[95] h2: 6 Discussion and Limitations

[96] p: Discussion. Certified circuits outperform baselines across all settings. For sufficiency and compactness, certification shifts the accuracy–sparsity curve: circuits peak at smaller sizes with higher cACC, suggesting unstable neurons are not only unnecessary but harmful. For OOD generalization, circuits discovered on ImageNet transfer without re-discovery, improving cACC by up to 91% at 45% smaller circuit on ImageNet-A. Structural stability results support this mechanism: certified circuits show higher IoU when re-discovered on OOD data, indicating convergence to an invariant core. Overall, these findings support our hypothesis that the instability noted in prior work ( Méloux et al., 2025 ; Miller et al., 2024 ; Friedman et al., 2024 ) arises from neurons that are inconsistently selected across dataset variants; abstention removes these components, yielding circuits that provably reflect the concept rather than dataset-specific artifacts.

[97] p: Limitations. Certifying a circuit requires running the discovery algorithm on n n randomized dataset deletions ( n = 1000 n{=}1000 in our experiments), so runtime scales linearly. The certification step is lightweight, since it only aggregates per-neuron votes and applies a confidence test, and the n n runs are highly parallel. Since circuits are typically computed offline for inspection tasks such as debugging, auditing, and mechanistic analysis, this overhead is usually justified. To the best of our knowledge, the only concurrent work providing formal guarantees for mechanistic circuit discovery ( Anonymous, 2026 ) operates on small CNNs/MLPs and architecture-specific access and small data (e.g., MNIST, CIFAR10), whereas our guarantees come from a black-box wrapper and scale to standard vision benchmarks. Larger certified radii require higher deletion rates, which can degrade the base method when concept datasets are small, more samples can mitigate this effect. Finally, we use a single sparsity K K across layers, layer-wise budgets inspired by pruning literature may yield better sparsity allocation. We evaluate on CNNs, extending to ViTs and other modalities, including LLMs, is an interesting avenue for future work.

[98] h2: 7 Conclusion

[99] p: We introduced Certified Circuits , a framework providing provable stability guarantees for circuit discovery. By combining deletion-based randomized smoothing with per-neuron abstention, our method certifies that circuits remain unchanged under bounded dataset edits—directly addressing the instability undermining confidence in mechanistic explanations. Empirically, certified circuits are more compact, more sufficient, and generalize better to OOD data than baselines, while remaining structurally stable beyond their certified radius. Our work establishes that reliable circuit discovery is achievable: practitioners can obtain mechanistic explanations that are provably stable and empirically robust, bridging interpretability and trustworthiness.

[100] h3: Impact Statement

[101] p: This paper advances the field of machine learning by introducing Certified Circuits, a framework that provides formal stability guarantees for mechanistic circuit discovery methods. By enabling provably robust mechanistic explanations, our work strengthens the reliability and scientific validity of interpretability analyses, particularly under dataset variation and distribution shift.

[102] p: We anticipate that this contribution will have positive downstream impacts in areas where trustworthy model understanding is critical, such as model debugging, robustness evaluation, and auditing of learned representations. More stable and transferable explanations may help practitioners better identify spurious correlations, understand failure modes, and design safer machine learning systems.

[103] p: At the same time, as with interpretability tools more broadly, there is a risk that certified explanations could be misinterpreted as complete or definitive accounts of model behavior, despite capturing only a subset of the underlying computation. We emphasize that certified circuits provide guarantees relative to a specific threat model and concept dataset, and should be used as one component within a broader interpretability and evaluation toolkit.

[104] p: Overall, we believe the societal implications of this work are aligned with established goals in machine learning interpretability—improving transparency, robustness, and trustworthiness—and do not raise new ethical concerns beyond those already present in the field.

[105] h2: References

[106] h2: Appendix

[107] h2: Appendix A Proof of Theorem 3.3

[108] h6: Proof.

[109] p: Fix a vertex v ∈ 𝒱 v\in\mathcal{V} . Define the per-vertex base classifier h v : 𝒳 ∗ → { 0 , 1 } h_{v}:\mathcal{X}^{*}\to\{0,1\} by h v ​ ( 𝒟 ) := A v ​ ( 𝒟 ) h_{v}(\mathcal{D}):=A_{v}(\mathcal{D}) . Let ϕ p del ​ ( 𝒟 ) \phi_{p_{\mathrm{del}}}(\mathcal{D}) denote the RS-Del perturbation that independently deletes each element of the sequence 𝒟 \mathcal{D} with probability p del p_{\mathrm{del}} , producing a random subsequence 𝒟 ⊙ ε \mathcal{D}\odot\varepsilon .

[110] h4: Smoothed probabilities and abstaining decision.

[111] p: Define the smoothed inclusion probability

[112] table: p v ( 𝒟 ) := Pr ε ∼ Bernoulli ​ ( 1 − p del ) | 𝒟 | [ h v ( 𝒟 ⊙ ε ) = 1 ] , p_{v}(\mathcal{D})\;:=\;\Pr_{\varepsilon\sim\mathrm{Bernoulli}(1-p_{\mathrm{del}})^{|\mathcal{D}|}}\!\left[h_{v}(\mathcal{D}\odot\varepsilon)=1\right],

[113] p: and let p v , 0 ​ ( 𝒟 ) := 1 − p v ​ ( 𝒟 ) p_{v,0}(\mathcal{D}):=1-p_{v}(\mathcal{D}) and p v , 1 ​ ( 𝒟 ) := p v ​ ( 𝒟 ) p_{v,1}(\mathcal{D}):=p_{v}(\mathcal{D}) . Let the (non-abstaining) smoothed label be

[114] table: A ~ v ​ ( 𝒟 ) := arg ⁡ max c ∈ { 0 , 1 } ​ p v , c ​ ( 𝒟 ) , μ v ​ ( 𝒟 ) := max ⁡ { p v ​ ( 𝒟 ) , 1 − p v ​ ( 𝒟 ) } . \tilde{A}_{v}(\mathcal{D})\;:=\;\arg\max_{c\in\{0,1\}}p_{v,c}(\mathcal{D}),\qquad\mu_{v}(\mathcal{D})\;:=\;\max\{p_{v}(\mathcal{D}),\,1-p_{v}(\mathcal{D})\}.

[115] p: We output a certified (possibly partial) decision by thresholding as in segmentation-style smoothing with abstention:

[116] table: A ~ v τ ​ ( 𝒟 ) = { 1 if ​ p v ​ ( 𝒟 ) > τ , 0 if ​ 1 − p v ​ ( 𝒟 ) > τ , ⊘ otherwise . \tilde{A}_{v}^{\tau}(\mathcal{D})=\begin{cases}1&\text{if }p_{v}(\mathcal{D})>\tau,\\ 0&\text{if }1-p_{v}(\mathcal{D})>\tau,\\ \oslash&\text{otherwise}.\end{cases}

[117] p: Note that τ ≥ 1 2 \tau\geq\tfrac{1}{2} implies that whenever A ~ v τ ​ ( 𝒟 ) ∈ { 0 , 1 } \tilde{A}_{v}^{\tau}(\mathcal{D})\in\{0,1\} , the maximizer A ~ v ​ ( 𝒟 ) \tilde{A}_{v}(\mathcal{D}) is unique and equals A ~ v τ ​ ( 𝒟 ) \tilde{A}_{v}^{\tau}(\mathcal{D}) .

[118] h4: RS-Del certificate on the input sequence.

[119] p: Apply RS-Del ( Huang et al., 2023 ) to the smoothed binary classifier A ~ v \tilde{A}_{v} under Levenshtein edit distance (allowing insertions, deletions, and substitutions). RS-Del (Theorem 7 and Table 1 in ( Huang et al., 2023 ) ) gives that if the predicted class at 𝒟 \mathcal{D} has confidence μ v ​ ( 𝒟 ) \mu_{v}(\mathcal{D}) , then the smoothed prediction is invariant for any edit-distance ball of radius r ≤ r ⋆ ​ ( μ v ​ ( 𝒟 ) ) r\leq r^{\star}(\mu_{v}(\mathcal{D})) , where

[120] table: r ⋆ ​ ( μ ) = ⌊ log ⁡ ( 1 + ν ⁡ ( η ) − μ ) log ⁡ p del ⌋ . r^{\star}(\mu)\;=\;\left\lfloor\frac{\log\!\bigl(1+\nu(\eta)-\mu\bigr)}{\log p_{\mathrm{del}}}\right\rfloor.

[121] p: For binary outputs and symmetric thresholds (our case), ν ⁡ ( η ) = 1 2 \nu(\eta)=\tfrac{1}{2} , hence

[122] table: r ⋆ ​ ( μ ) = ⌊ log ⁡ ( 1.5 − μ ) log ⁡ p del ⌋ . r^{\star}(\mu)\;=\;\left\lfloor\frac{\log(1.5-\mu)}{\log p_{\mathrm{del}}}\right\rfloor.

[123] p: Moreover r ⋆ ​ ( μ ) r^{\star}(\mu) is nondecreasing in μ \mu because log ⁡ p del < 0 \log p_{\mathrm{del}}<0 and 1.5 − μ 1.5-\mu decreases with μ \mu .

[124] h4: Conclude invariance for certified vertices.

[125] p: Assume A ~ v τ ​ ( 𝒟 ) ∈ { 0 , 1 } \tilde{A}_{v}^{\tau}(\mathcal{D})\in\{0,1\} . Then μ v ​ ( 𝒟 ) > τ \mu_{v}(\mathcal{D})>\tau , so by monotonicity r ⋆ ​ ( μ v ​ ( 𝒟 ) ) ≥ r ⋆ ​ ( τ ) r^{\star}(\mu_{v}(\mathcal{D}))\geq r^{\star}(\tau) . Define

[126] table: r := r ⋆ ​ ( τ ) = ⌊ log ⁡ ( 1.5 − τ ) log ⁡ p del ⌋ . r\;:=\;r^{\star}(\tau)\;=\;\left\lfloor\frac{\log(1.5-\tau)}{\log p_{\mathrm{del}}}\right\rfloor.

[127] p: Then for every 𝒟 ′ \mathcal{D}^{\prime} with dist edit ​ ( 𝒟 , 𝒟 ′ ) < r \mathrm{dist}_{\mathrm{edit}}(\mathcal{D},\mathcal{D}^{\prime})<r , RS-Del implies the smoothed label is invariant:

[128] table: A ~ v ​ ( 𝒟 ′ ) = A ~ v ​ ( 𝒟 ) = A ~ v τ ​ ( 𝒟 ) . \tilde{A}_{v}(\mathcal{D}^{\prime})=\tilde{A}_{v}(\mathcal{D})=\tilde{A}_{v}^{\tau}(\mathcal{D}).

[129] p: This is exactly the claimed circuit-membership invariance for all non-abstaining vertices.

[130] h4: Statistical confidence.

[131] p: In practice μ v ​ ( 𝒟 ) \mu_{v}(\mathcal{D}) is unknown and we certify based on a ( 1 − α ) (1-\alpha) lower confidence bound (e.g., Clopper–Pearson) for μ v ​ ( 𝒟 ) \mu_{v}(\mathcal{D}) . On the event that the true confidence exceeds this bound (which holds with probability at least 1 − α 1-\alpha ), the above argument applies. If one wants the guarantee to hold simultaneously for all vertices ( Fischer et al., 2021 ) , set per-vertex failure probability to α / | 𝒱 | \alpha/|\mathcal{V}| and apply a union bound. ∎

[132] h2: Appendix B Certified Radius Analysis

[133] figure: Figure 5 : Certified edit-distance radius r r as a function of the deletion probability p del p_{\mathrm{del}} for different confidence thresholds τ \tau . Larger p del p_{\mathrm{del}} and larger τ \tau yield larger certified radii.

[134] p: The certified edit-distance radius r r in Theorem 3.3 is determined by the deletion probability p del p_{\mathrm{del}} and confidence threshold τ \tau according to this formula, inherited from RS-Del ( Huang et al., 2023 ) , reveals a trade-off between certification strength and the base algorithm’s operating conditions.

[135] p: Figure 5 illustrates this relationship. The certified radius increases with both p del p_{\mathrm{del}} and τ \tau : higher deletion probabilities mean the smoothed algorithm aggregates over more aggressively perturbed sub-datasets, while higher confidence thresholds require stronger agreement across perturbations before certifying a decision. As p del → 1 p_{\mathrm{del}}\to 1 , the radius grows rapidly, but this comes at a cost: the base algorithm A A receives increasingly sparse sub-datasets, which can degrade its performance when concept datasets are small. Conversely, lower p del p_{\mathrm{del}} values preserve more examples per run but yield smaller certified radii.

[136] p: In practice, we select p del p_{\mathrm{del}} to balance two considerations: (i) achieving a meaningful certified radius (e.g., r ≥ 5 r\geq 5 edits), and (ii) retaining enough examples per sub-dataset for the base algorithm to produce reliable circuits. For concept datasets of size | 𝒟 | |\mathcal{D}| , the expected sub-dataset size is ( 1 − p del ) ⋅ | 𝒟 | (1-p_{\mathrm{del}})\cdot|\mathcal{D}| , so larger concept datasets permit higher deletion probabilities without starving the base algorithm.

[137] h2: Appendix C Additional Results

[138] figure: Paradigm Score In-Distribution Out-of-Distribution ImageNet OOD-CV ImageNet-A ImageNet-O ImageNet-C cACC ↑ \mathrm{cACC}\!\uparrow oACC ↓ \mathrm{oACC}\!\downarrow K ↓ K\!\downarrow cACC ↑ \mathrm{cACC}\!\uparrow oACC ↓ \mathrm{oACC}\!\downarrow K ↓ K\!\downarrow cACC ↑ \mathrm{cACC}\!\uparrow oACC ↓ \mathrm{oACC}\!\downarrow K ↓ K\!\downarrow cACC ↑ \mathrm{cACC}\!\uparrow oACC ↓ \mathrm{oACC}\!\downarrow K ↓ K\!\downarrow cACC ↑ \mathrm{cACC}\!\uparrow oACC ↓ \mathrm{oACC}\!\downarrow K ↓ K\!\downarrow Model – 81 83 1.00 20 15 1.00 9 9 1.00 81 81 1.00 61 62 1.00 Baseline circuit Rel. 86 67 0.70 74 0 0.40 62 0 0.40 93 26 0.60 76 36 0.70 Act. 83 77 0.80 36 1 0.40 20 1 0.60 87 52 0.70 69 40 0.70 Rank 49 45 0.80 40 1 0.40 17 1 0.60 61 36 0.70 46 27 0.70 Certified circuit (ours) Rel. 96 ↑ 12 \uparrow\!12 1 ↓ 99 \downarrow\!99 0.34 ↓ 51 \downarrow\!51 93 ↑ 25 \uparrow\!25 0 ↓ 85 \downarrow\!85 0.34 ↓ 16 \downarrow\!16 94 ↑ 51 \uparrow\!51 0 ↓ 77 \downarrow\!77 0.34 ↓ 14 \downarrow\!14 98 ↑ 6 \uparrow\!6 4 ↓ 86 \downarrow\!86 0.42 ↓ 30 \downarrow\!30 94 ↑ 24 \uparrow\!24 0 ↓ 100 \downarrow\!100 0.34 ↓ 51 \downarrow\!51 Act. 84 ↑ 1 \uparrow\!1 65 ↓ 15 \downarrow\!15 0.61 ↓ 24 \downarrow\!24 53 ↑ 47 \uparrow\!47 1 ↓ 6 \downarrow\!6 0.27 ↓ 33 \downarrow\!33 37 ↑ 89 \uparrow\!89 0 ↓ 86 \downarrow\!86 0.33 ↓ 45 \downarrow\!45 90 ↑ 3 \uparrow\!3 27 ↓ 49 \downarrow\!49 0.49 ↓ 30 \downarrow\!30 74 ↑ 6 \uparrow\!6 20 ↓ 51 \downarrow\!51 0.50 ↓ 28 \downarrow\!28 Rank 83 ↑ 71 \uparrow\!71 79 0.69 ↓ 1 % \downarrow\!1\% 46 ↑ 16 \uparrow\!16 2 0.38 ↓ 4 \downarrow\!4 28 ↑ 69 \uparrow\!69 2 0.58 ↓ 3 \downarrow\!3 90 ↑ 49 \uparrow\!49 37 0.57 ↓ 18 \downarrow\!18 73 ↑ 58 \uparrow\!58 28 0.59 ↓ 16 \downarrow\!16 Table 2: Certified vs. baseline circuit sufficiency. Peak cACC (and the corresponding other-classes accuracy oACC) at circuit size K K under sufficiency pruning on ResNet-101. Circuits are discovered on ImageNet and evaluated either in-distribution or on OOD shifts.

[139] p: A key property for mechanistic circuits is class specificity : the circuit should retain information that is predictive of the target class, but not retain broader features that enable correct classification of other classes. If a circuit preserves high accuracy on non-target images, it likely contains extra, non-class-specific information and is therefore not isolating the concept. To quantify specificity, we evaluate each class circuit on images that do not belong to the class it was discovered for and report the resulting overall accuracy (oACC); lower oACC indicates a more class-specific circuit. Table 2 reports oACC alongside peak cACC and the corresponding circuit size K K .

[140] p: The results show that Certified Circuits yield much more meaningful circuits, not only capturing the target class better, but also being more specific to the target class, having lower accuracy on images from different classes than the circuit class. On ImageNet, the certified circuits have a 99% lower oACC, achieving an oACC of 1%. This decrease in oACC is extremely large, showing more than 50% better metric values on most OOD datasets compared to the baseline circuits.

[141] h2: Instructions for reporting errors

[142] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[143] p: Tip: You can select the relevant text first, to include it in your report.

[144] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[145] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
