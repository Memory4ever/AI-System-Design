[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: RobustVisRAG: Causality-Aware Vision-Based Retrieval-Augmented Generation under Visual Degradations

[3] h6: Abstract

[4] p: Vision-based Retrieval-Augmented Generation (VisRAG) leverages vision-language models (VLMs) to jointly retrieve relevant visual documents and generate grounded answers based on multimodal evidence. However, existing VisRAG models degrade in performance when visual inputs suffer from distortions such as blur, noise, low light, or shadow, where semantic and degradation factors become entangled within pretrained visual encoders, leading to errors in both retrieval and generation stages. To address this limitation, we introduce RobustVisRAG, a causality-guided dual-path framework that improves VisRAG robustness while preserving efficiency and zero-shot generalization. RobustVisRAG uses a non-causal path to capture degradation signals through unidirectional attention and a causal path to learn purified semantics guided by these signals. Together with the proposed Non-Causal Distortion Modeling and Causal Semantic Alignment objectives, the framework enforces a clear separation between semantics and degradations, enabling stable retrieval and generation under challenging visual conditions. To evaluate robustness under realistic conditions, we introduce the Distortion-VisRAG dataset, a large-scale benchmark containing both synthetic and real-world degraded documents across seven domains, with 12 synthetic and 5 real distortion types that comprehensively reflect practical visual degradations. Experimental results show that RobustVisRAG improves retrieval, generation, and end-to-end performance by 7.35%, 6.35%, and 12.40%, respectively, on real-world degradations, while maintaining comparable accuracy on clean inputs. Project page: https://robustvisrag.github.io/

[5] figure: (a) Retrieval (b) Generation (c) End-to-End (Clean) (d) End-to-End (Degrade) Figure 1 : Illustration of RobustVisRAG’s capabilities. (a) Retrieval performance under clean, synthetic degradation (Degrade-Syn) and real-degradation (Degrade-Real) scenarios. (b) Generation performance using the retrieved documents from RobustVisRAG as input. (c)(d) End-to-end retrieval–generation performance on clean and degraded data, evaluated under the same baselines including VisRAG, its fine-tuned variants (VisRAG-FT) [ 42 ] , and a Two-Stage restoration pipeline [ 39 ] . Across all settings, both TextRAG and VisRAG show notable performance drops under degraded inputs, whereas RobustVisRAG preserves clean accuracy and significantly improves robustness in degraded conditions.

[6] h2: 1 Introduction

[7] p: Large language models (LLMs) and vision-language models (VLMs) have shown strong reasoning and generation abilities across diverse tasks [ 2 , 21 , 24 , 63 , 1 , 3 ] . However, their parametric nature fixes internal knowledge after training, often leading to hallucinations or outdated predictions [ 17 , 4 ] . Retrieval-augmented generation (RAG) [ 12 , 20 , 60 , 59 ] addresses this limitation by incorporating external knowledge during generation, improving factuality and interpretability. Existing RAG methods can be categorized into Text-based RAG (TextRAG) [ 12 ] and Vision-based RAG (VisRAG) [ 59 ] . TextRAG operates on textual inputs, retrieving relevant passages for generation. When document content appears as images, it relies on multi-stage parsing with layout analysis and OCR [ 5 , 27 ] , which accumulates recognition errors [ 59 ] , discards visual cues, and fails to capture non-textual information such as figures or charts. In contrast, VisRAG leverages VLMs to directly encode visual inputs, avoiding parsing errors and preserving spatial and visual context. This design enables effective multimodal reasoning and alignment during generation.

[8] p: Although both TextRAG and VisRAG reduce hallucinations and outdated predictions by retrieving external evidence, their performance drops when either the query or the corpus contains degraded document images affected by blur, noise, low light, shadow, or compression artifacts [ 50 ] , as shown in Fig. 1(a) and Fig. 1(b) . In TextRAG, such degradations cause recognition and parsing failures in OCR and layout detection, resulting in incomplete or erroneous retrieval. In VisRAG, visual distortions corrupt the embeddings extracted by VLM encoders, where semantic and distortion factors intertwine, leading to retrieval mismatches and unstable generation. Degradations induce a dual failure mode in the VisRAG pipeline: the model may retrieve incorrect evidence due to corrupted visual representations, and even when the correct evidence is retrieved, degraded inputs can still mislead the generation process. These challenges highlight the need for robustness analysis and mitigation within the VisRAG pipeline under degraded conditions.

[9] p: To address the above challenges, an intuitive two-stage strategy is to apply existing image restoration techniques [ 46 , 53 ] to improve the visual quality of degraded images and use the enhanced results as inputs to VisRAG. However, under the degraded VisRAG setting, such restoration-based two-stage pipelines do not consistently translate perceptual improvements into retrieval or generation gains. Alternatively, fine-tuning the VLM itself offers a more direct solution. Parameter-efficient fine-tuning (PEFT) [ 14 ] offers a low-cost way to adapt VLMs, but its limited representational capacity hinders effective recovery of degradation-corrupted embeddings. In contrast, full fine-tuning (FFT) enhances adaptability to degraded inputs but requires substantial computational resources and often overfits to distortion patterns while forgetting pretrained knowledge [ 18 ] . Moreover, both fine-tuning strategies remain fundamentally limited, as they lack explicit causal guidance to disentangle semantic and distortion factors, which is essential for achieving robust VisRAG under visual degradations. As shown in Fig. 1(d) , existing two-stage and fine-tuning strategies provide limited performance gains under degraded conditions, highlighting the persistent challenge of distortion robustness in VisRAG.

[10] p: To address the vulnerability of VisRAG systems under visual degradations, we propose RobustVisRAG, a causality-guided dual-path framework that explicitly separates semantic and degradation information during visual encoding. RobustVisRAG augments the vision encoder with two complementary pathways: a non-causal path that aggregates degradation cues using a unidirectional attention mechanism, and a causal path that focuses on semantic aggregation and learns purified semantics under the guidance of the degradation signals extracted by the non-causal path. To ensure functional specialization of both pathways, we introduce two learning objectives: Non-Causal Distortion Modeling (NCDM) to enforce structured degradation representation, and Causal Semantic Alignment (CSA) to guide semantic purification and prevent degradation leakage into semantic embeddings. Through joint optimization of these components within a single forward pass, RobustVisRAG effectively disentangles semantic and degradation factors, substantially improving retrieval and generation robustness under degraded visual conditions as shown in Fig. 1 .

[11] p: To evaluate real-world robustness, we construct the Distortion-VisRAG dataset, extending VisRAG [ 59 ] with large-scale synthetic and real-world degraded document images. The dataset additionally includes a real-world subset captured under practical conditions such as low light, shadow, and paper damage, narrowing the gap between simulated and natural degradations. The dataset contains 367K question–document pairs across seven document understanding domains (e.g., scientific papers, charts, forms, slides, and handwritten notes), covering 17 degradation types at multiple severity levels. This benchmark enables systematic evaluation of retrieval and generation robustness.

[12] p: The main contributions of this work are summarized as follows:

[13] p: We propose RobustVisRAG, a causality-guided dual-path framework that disentangles semantic and degradation factors during visual encoding to improve VisRAG robustness under degraded conditions without additional inference cost. Extensive experiments show that RobustVisRAG generalizes to real-world degradations in our benchmark, improving retrieval, generation, and end-to-end performance by 7.35%, 6.35%, and 12.40%, respectively, while maintaining comparable performance on clean data.

[14] p: We introduce the Distortion-VisRAG dataset, a VisRAG-specific benchmark designed for joint evaluation of retrieval, generation, and end-to-end robustness under synthetic and real-world degradations.

[15] h2: 2 Related Work

[16] h3: 2.1 Retrieval-Augmented Generation

[17] p: RAG enhances LLMs by coupling retrieval with generation, grounding answers in external evidence rather than internal parameters [ 12 , 45 , 60 ] . RAG system includes a retriever for locating relevant information and a generator for producing responses based on the query and retrieved context.

[18] p: Text-based RAG. These methods operate purely on text by applying OCR [ 5 , 27 , 64 , 16 ] to document images before retrieval and generation. However, OCR errors and layout loss in complex documents (e.g., tables or charts) cause fragmented information and grounding issues [ 44 , 56 ] , which are further exacerbated under degradations such as blur, noise, or compression [ 7 ] . While recent studies [ 33 ] suggest that OCR-based pipelines can exhibit competitive robustness under certain document quality conditions, their performance remains sensitive to dataset characteristics and OCR quality.

[19] p: Vision-based RAG. To address the limitations of text-based RAG, recent studies extend RAG to the visual domain [ 59 , 9 , 25 ] . VisRAG replaces textual modules with vision-language retrievers and generators that encode document images and queries in a shared embedding space, preserving layout and visual cues while reducing OCR errors. However, current models still assume ideal image quality and degrade under real-world conditions, underscoring the need for robustness-oriented VisRAG frameworks.

[20] h3: 2.2 VLM Robustness under Degradation

[21] p: A degradation-robust VLM is essential for reliable VisRAG systems, as both retrieval and generation depend on visual representation quality. Recent studies show that existing VLMs experience performance drops under visual degradations [ 50 ] . Although no method is explicitly designed for degradation-aware multimodal learning, prior works have explored potential directions to alleviate this issue, including input enhancement and fine-tuning strategies. One common approach is the two-stage strategy, which enhances input quality before feeding images into the model. Image restoration methods [ 61 , 57 ] improve perceptual fidelity but may not preserve semantic consistency [ 6 ] , limiting downstream gains. Another approach is fine-tuning: parameter-efficient methods [ 14 ] offer lightweight adaptability but limited capacity, while full fine-tuning enhances degraded performance but incurs high computational cost and risks catastrophic forgetting [ 18 ] , hindering generalization. Moreover, methods such as TeCoA [ 29 ] and FARE [ 42 ] enhance robustness by adversarially fine-tuning the vision encoders of VLMs, improving their resistance to ℓ p \ell_{p} -bounded perturbations. However, their improvements are confined to small, controllable pixel perturbations and may not generalize to the natural degradations considered here, such as blur, low light, compression, and shadow. Overall, while robustness of VLMs under degradations has been widely studied, robust vision-language understanding within VisRAG pipelines remains underexplored.

[22] h3: 2.3 Causality Learning

[23] p: Causality learning provides a principled framework for understanding the underlying relationships between data attributes and model predictions [ 15 , 47 , 47 ] . In vision research, Structural Causal Models have been used to disentangle true semantic causes from spurious correlations, promoting debiasing and domain generalization [ 55 , 52 , 28 ] . Building on this foundation, causal attention [ 51 ] and causal prototype learning [ 26 ] further incorporate causal reasoning into neural architectures, enhancing interpretability and robustness in visual understanding. Recently, causal reasoning has also been introduced into VLMs to improve compositional reasoning and multimodal alignment [ 11 , 37 , 23 ] . However, these methods mainly operate at the semantic level and assume clean inputs. In real-world scenarios, visual signals are often affected by various forms of visual degradation, which act as latent causal factors that directly influence feature representations. Yet current causal VLM frameworks rarely model this “degradation → representation” pathway, leaving semantic features entangled with degradation cues and reducing robustness under real-world conditions.

[24] h2: 3 Proposed Method

[25] figure: (a) Structural Causal Model (b) Vision-based RAG (c) RobustVisRAG. Figure 2 : Overview of RobustVisRAG. (a) Structural causal model of VisRAG under visual degradations. (b) Architecture of the vanilla vision-based RAG pipeline with degraded input. (c) The proposed RobustVisRAG, which introduces a causality-guided dual-path encoder to disentangle semantic and degradation factors.

[26] h3: 3.1 Preliminary

[27] p: Vision-based RAG. Given a textual query q q (e.g., a question or instruction) and a visual corpus 𝒱 = { X i } i = 1 N \mathcal{V}=\{X_{i}\}_{i=1}^{N} , VisRAG retrieves the top- k k most relevant document images and generates a response as follows:

[28] table: R ⏟ top- ​ k ​ retrieved doc images = ℛ ⁡ ( q , ℰ r ​ ( 𝒱 ) ) , Y = 𝒢 ⁡ ( q , ℰ g ​ ( R ) ) , \underbrace{R}_{\text{top-}k\ \text{retrieved doc images}}=\mathcal{R}\!\big(q,\;\mathcal{E}_{r}(\mathcal{V})\big),\hskip 18.49988ptY=\mathcal{G}\!\big(q,\;\mathcal{E}_{g}(R)\big), (1)

[29] p: where X i X_{i} denotes the i i -th document image in the corpus, ℰ r \mathcal{E}_{r} and ℰ g \mathcal{E}_{g} represent the retrieval and generation encoders, and ℛ ⁡ ( ⋅ ) \mathcal{R}(\cdot) and 𝒢 ⁡ ( ⋅ ) \mathcal{G}(\cdot) denote the retrieval and generation modules, respectively. For notational simplicity, both encoders are hereafter referred to collectively as ℰ θ \mathcal{E}_{\theta} .

[30] p: In real-world scenarios, document images inevitably suffer from visual degradations such as blur, noise, low light, and shadow, which distort semantics and cause distributional shifts in the embedding space. These degradations reduce retrieval accuracy and propagate errors into the generation stage. Even when correct document images are retrieved, degraded visual inputs can still mislead the generation process, resulting in hallucinated or semantically inconsistent responses. We attribute this issue to semantic–distortion entanglement , where semantic and degradation features become intertwined within the visual encoder representations.

[31] p: Causal Formulation of Degradation in VisRAG. We formalize how semantics and degradations jointly influence VisRAG outputs through a structural causal model (SCM). Let S S denote the task-relevant semantic factors, and D D denote the degradation (nuisance) factors such as blur or shadow. The observed document image X X is generated as

[32] table: X = f ⁡ ( S , D , ε X ) , X=f(S,D,\varepsilon_{X}), (2)

[33] p: where f ⁡ ( ⋅ ) f(\cdot) represents the image-formation process and ε X \varepsilon_{X} is an exogenous noise variable. A pretrained vision encoder in VLMs ℰ θ \mathcal{E}_{\theta} then maps X X into a latent representation:

[34] table: Z = ℰ θ ​ ( X ) , Z=\mathcal{E}_{\theta}(X), (3)

[35] p: which is further processed by the retrieval and generation modules:

[36] table: ( R , Y ) = g ⁡ ( q , Z ) , (R,Y)=g(q,Z), (4)

[37] p: where g ⁡ ( ⋅ ) g(\cdot) denotes the retrieval and generation mapping in the VisRAG pipeline.

[38] p: Following the Independent Causal Mechanism principle [ 43 ] , we assume S ⟂ ⟂ D S\perp\!\!\!\perp D and that all exogenous noise variables are mutually independent. Here, ⟂ ⁣ ⟂ \perp\!\!\!\perp denotes statistical independence. The overall causal structure can be summarized as

[39] table: S → X ← D , X → Z , Z → ( R , Y ) , S\rightarrow X\leftarrow D,\hskip 18.49988ptX\rightarrow Z,\hskip 18.49988ptZ\rightarrow(R,Y), (5)

[40] p: where the directed edges represent causal influences between variables. Specifically, S S and D D jointly determine the observed document image X X ; X X is then encoded into a latent representation Z Z by ℰ θ \mathcal{E}_{\theta} ; and Z Z further drives the retrieval and generation outputs ( R , Y ) (R,Y) in the VisRAG pipeline. This structure clearly depicts how both semantic and degradation factors propagate through the encoding and reasoning stages. Since Z Z is a descendant of the collider X X , conditioning on Z Z can open a non-causal path S ↔ D S\leftrightarrow D ( ↔ \leftrightarrow denotes an induced statistical association ), introducing residual dependence S ​ ⟂ ⟂ D | Z S\not\!\perp\!\!\!\perp D\mid Z . Here, ⟂ ⟂ \not\!\perp\!\!\!\perp denotes statistical dependence. This entanglement leads the latent representation Z Z to mix semantic and degradation information, resulting in corrupted retrieval and unstable generation.

[41] p: To mitigate this issue, we propose to disentangle the two factors within the latent space. In particular, the representation encoded by ℰ θ \mathcal{E}_{\theta} should preserve task-relevant semantics while isolating degradation cues into a separate subspace. Therefore, our objective is to learn a factorized representation:

[42] table: Z = [ Z sem , Z deg ] , Z=[Z_{\text{sem}},Z_{\text{deg}}], (6)

[43] p: where Z sem Z_{\text{sem}} captures semantic content while Z deg Z_{\text{deg}} encodes degradation information. Ideally, the representation should satisfy:

[44] table: Z sem ⟂ ⟂ S , Z sem ⟂ ⟂ D . Z_{\text{sem}}\not\!\perp\!\!\!\perp S,\hskip 9.24994ptZ_{\text{sem}}\perp\!\!\!\perp D\;. (7)

[45] p: That is, the semantic component should depend only on the causal factors S S and remain independent of degradation factors D D . Under this condition, the prediction made by the model can be viewed as an approximation of the interventional distribution:

[46] table: P ⁡ ( A ∣ d ​ o ​ ( D = d 0 ) ) , A ∈ { R , Y } , P(A\mid do(D=d_{0})),\hskip 18.49988ptA\in\{R,Y\}, (8)

[47] p: where the do-operator d ​ o ​ ( ⋅ ) do(\cdot) [ 38 ] denotes intervention that removes the causal influence of D D (e.g., setting D D to a reference clean state d 0 d_{0} , or performing edge surgery to cut D → X D\!\to\!X ). A A as the retrieval and generation outputs ( R , Y ) (R,Y) . As shown in Fig. 2(a) , this intervention closes the non-causal path D → X → Z → A D\!\to\!X\!\to\!Z\!\to\!A while preserving the causal route S → X → Z → A S\!\to\!X\!\to\!Z\!\to\!A . This causal formulation motivates the asymmetric encoder design and the disentanglement objectives introduced in Sec. 3.2 . For clarity, we omit the explicit variable X X in the following sections, since the encoder ℰ θ \mathcal{E}_{\theta} implicitly maps the observed image X X into latent representations ( Z sem , Z deg ) (Z_{\text{sem}},Z_{\text{deg}}) .

[48] h3: 3.2 RobustVisRAG

[49] p: Overview. Building upon the causal analysis in Sec. 3.1 , RobustVisRAG enhances the standard VisRAG pipeline ( Fig. 2 (b)) with a causality-guided dual-path encoder ( Fig. 2 (c)). The design explicitly follows the two information sources in the structural causal model: a non-causal path that captures degradation factors D D , and a causal path that encodes task-relevant semantics S S . The non-causal path learns to identify and represent degradations through the Non-Causal Distortion Modeling (NCDM) objective, while the causal path leverages these learned degradation cues to disentangle and purify semantic representations via the Causal Semantic Alignment (CSA) objective. Both paths are jointly optimized in an end-to-end manner, enabling structural intervention on the non-causal route and approximating the interventional behavior P ⁡ ( A ∣ d ​ o ​ ( D = d 0 ) ) P(A\mid do(D=d_{0})) .

[50] p: Non-Causal Path. To explicitly extract degradation-related information, we introduce a single non-causal token z n ​ c ( 0 ) z_{nc}^{(0)} at the input layer. This token is propagated through the network and updated at each layer. Let { x 1 ( l ) , … , x T ( l ) } \{x_{1}^{(l)},\dots,x_{T}^{(l)}\} denote the patch tokens at layer l l , and let z n ​ c ( l ) z_{nc}^{(l)} denote the updated feature of the same non-causal token after layer l l . During attention computation, we enforce a directional constraint: (i) the non-causal token is allowed to attend to all patch tokens, and (ii) patch tokens are masked from attending to the non-causal token. Under this design, the non-causal token is updated as

[51] table: z n ​ c ( l + 1 ) = z n ​ c ( l ) + ∑ j = 1 T α n ​ c ← j ( l ) ​ v j ( l ) , z_{nc}^{(l+1)}=z_{nc}^{(l)}+\sum_{j=1}^{T}\alpha^{(l)}_{nc\leftarrow j}\,v_{j}^{(l)}, (9)

[52] p: where α n ​ c ← j ( l ) \alpha^{(l)}_{nc\leftarrow j} denotes the attention weight from the non-causal token (as query) to the j j -th patch token, and v j ( l ) v_{j}^{(l)} is the corresponding value projection.

[53] p: This unidirectional design lets the non-causal token aggregate degradation cues across spatial regions of the image while preventing these cues from flowing back into the semantic tokens. After L L self-attention layers, we obtain the degradation representation:

[54] table: Z deg = z n ​ c ( L ) . Z_{\text{deg}}=z_{nc}^{(L)}. (10)

[55] p: However, structural separation alone does not guarantee that Z deg Z_{\text{deg}} truly captures degradation factors. Therefore, we further introduce the NCDM objective to explicitly constrain this pathway to focus on degradation modeling while maintaining its non-interference with semantic representations.

[56] p: Non-Causal Distortion Modeling. The goal of the non-causal path is to encourage a degradation-aware latent subspace. This enables the causal (semantic) branch to utilize such degradation embeddings as guidance for disentanglement within the same forward pass. To achieve this, we introduce a distortion-contrastive objective that enforces degradation-aware discrimination in the latent space. For an anchor image X a X_{a} with degradation type d a d_{a} , we select a positive sample X p X_{p} sharing the same degradation ( d p = d a d_{p}=d_{a} ) and a negative sample X n X_{n} with a different degradation ( d n ≠ d a d_{n}\neq d_{a} ), and obtain their degradation embeddings Z deg a , Z deg p , Z deg n Z^{a}_{\text{deg}},Z^{p}_{\text{deg}},Z^{n}_{\text{deg}} from the non-causal path. The objective is formulated as

[57] table: ℒ NCDM = max ⁡ ( 0 , ‖ Z deg a − Z deg p ‖ 2 2 − ‖ Z deg a − Z deg n ‖ 2 2 + δ ) , \mathcal{L}_{\text{NCDM}}=\max\big(0,\;\|Z^{a}_{\text{deg}}-Z^{p}_{\text{deg}}\|_{2}^{2}-\|Z^{a}_{\text{deg}}-Z^{n}_{\text{deg}}\|_{2}^{2}+\delta\big), (11)

[58] p: where δ \delta is a margin parameter. This contrastive formulation encourages Z deg Z_{\text{deg}} to cluster samples with the same degradation while separating those from different distortions, thereby encouraging Z deg Z_{\text{deg}} to encode degradation-consistent patterns that facilitate robustness, without enforcing degradation-type identifiability.

[59] p: Causal Path. In parallel to the non-causal branch, the causal branch focuses on semantic aggregation through bidirectional attention among patch tokens. The non-causal token is excluded from this attention, so that semantic encoding is not contaminated by degradation-specific features.

[60] p: Let x i ( l ) x_{i}^{(l)} denote the i i -th patch token at layer l l , where the subscript c c implicitly marks the causal pathway. Given T T visual tokens, their update rule is

[61] table: x i ( l + 1 ) = x i ( l ) + ∑ j = 1 T α ( l ) i ↔ j v j ( l ) , i = 1 , … , T , x_{i}^{(l+1)}=x_{i}^{(l)}+\sum_{j=1}^{T}\alpha^{(l)}_{i\leftrightarrow j}\,v_{j}^{(l)},\hskip 9.24994pti=1,\dots,T, (12)

[62] p: where α i ↔ j ( l ) \alpha^{(l)}_{i\leftrightarrow j} is the attention weight between patch tokens only, computed under a mask that removes the non-causal token from both the key and value sets for the causal branch. This formulation is architecture-agnostic: for encoders with a global semantic token [ 40 ] , that token is included in the patch set and attends to all patches; for pooling-based encoders [ 62 ] , semantic aggregation arises from contextual interactions among patch tokens.

[63] p: After L L layers, we obtain the semantic representation:

[64] table: Z sem = Agg ⁡ ( x 1 ( L ) , … , x T ( L ) ) , Z_{\text{sem}}=\mathrm{Agg}\big(x_{1}^{(L)},\dots,x_{T}^{(L)}\big), (13)

[65] p: where Agg ⁡ ( ⋅ ) \mathrm{Agg}(\cdot) denotes the semantic aggregation function used to aggregate patch tokens the underlying encoder architecture. This representation is expected to follow the causal route S → Z sem S\!\to\!Z_{\text{sem}} and to remain invariant to degradations. Importantly, Z sem Z_{\text{sem}} and Z deg Z_{\text{deg}} are produced simultaneously within the same forward pass: Z deg Z_{\text{deg}} provides a degradation-related constraint to guide disentanglement during training through the CSA, rather than forming a direct causal dependency on Z sem Z_{\text{sem}} .

[66] p: Causal Semantic Alignment. Despite structural separation, early-layer feature sharing may still cause degradation leakage into the causal branch. To explicitly ensure that Z sem Z_{\text{sem}} captures degradation-invariant semantics, we propose the CSA objective, which leverages Z deg Z_{\text{deg}} as a causal regulator. For each clean/degraded image pair, we extract Z sem clean Z_{\text{sem}}^{\text{clean}} from the clean image’s causal path and ( Z sem deg , Z deg deg ) (Z_{\text{sem}}^{\text{deg}},Z_{\text{deg}}^{\text{deg}}) from the degraded image in the same forward pass. We define a joint semantic consistency and independence loss:

[67] table: ℒ SIL = 1 T ​ ∑ i = 1 T [ ( 1 − ⟨ Z sem , i deg , Z sem , i clean ⟩ ) + | ⟨ Z sem , i deg , Z deg deg ⟩ | ] , \mathcal{L}_{\text{SIL}}=\frac{1}{T}\sum_{i=1}^{T}\Big[(1-\langle Z_{\text{sem},i}^{\text{deg}},Z_{\text{sem},i}^{\text{clean}}\rangle)+\big|\langle Z_{\text{sem},i}^{\text{deg}},Z_{\text{deg}}^{\text{deg}}\rangle\big|\Big], (14)

[68] p: where ⟨ ⋅ , ⋅ ⟩ \langle\cdot,\cdot\rangle denotes cosine similarity and T T is the number of semantic tokens. The first term aligns the degraded semantics with the clean semantics, preserving the causal path S → Z sem S\!\to\!Z_{\text{sem}} , while the second term enforces independence between semantic and degradation embeddings, suppressing the non-causal dependency D → Z sem D\!\to\!Z_{\text{sem}} . To maintain local structural consistency, we add a fine-grained alignment term:

[69] table: ℒ FSAL = 1 T ​ ∑ i = 1 T ‖ Z sem , i deg − Z sem , i clean ‖ 2 2 . \mathcal{L}_{\text{FSAL}}=\frac{1}{T}\sum_{i=1}^{T}\big\|Z_{\text{sem},i}^{\text{deg}}-Z_{\text{sem},i}^{\text{clean}}\big\|_{2}^{2}. (15)

[70] p: The overall CSA objective is given by:

[71] table: ℒ CSA = ℒ SIL + λ FSAL ​ ℒ FSAL , \mathcal{L}_{\text{CSA}}=\mathcal{L}_{\text{SIL}}+\lambda_{\text{FSAL}}\mathcal{L}_{\text{FSAL}}, (16)

[72] p: where λ FSAL \lambda_{\text{FSAL}} balances global and local alignment. By jointly optimizing ℒ CSA \mathcal{L}_{\text{CSA}} and ℒ NCDM \mathcal{L}_{\text{NCDM}} , the encoder learns to causally disentangle semantics from degradations within a single forward pass, allowing Z sem Z_{\text{sem}} to approximate the interventional representation P ⁡ ( Z sem ∣ d ​ o ​ ( D = d 0 ) ) P(Z_{\text{sem}}\mid do(D=d_{0})) .

[73] p: Overall Objective. RobustVisRAG employs two vision encoders for retrieval and generation, both trained under the same causality-guided framework. For retrieval, the encoder is optimized end-to-end with a standard contrastive objective:

[74] table: ℒ Ret = − log ⁡ exp ⁡ ( ⟨ q , X + ⟩ / τ ) exp ⁡ ( ⟨ q , X + ⟩ / τ ) + ∑ x − exp ⁡ ( ⟨ q , X − ⟩ / τ ) , \mathcal{L}_{\text{Ret}}=-\log\frac{\exp(\langle q,X^{+}\rangle/\tau)}{\exp(\langle q,X^{+}\rangle/\tau)+\sum_{x^{-}}\exp(\langle q,X^{-}\rangle/\tau)}, (17)

[75] p: where X + X^{+} and { X − } \{X^{-}\} denote the positive and negative visual documents to query q q , and τ \tau is a temperature. The total retrieval loss combines contrastive learning with causality-guided objectives:

[76] table: ℒ Retrieval = ℒ Ret + λ 1 ​ ℒ CSA + λ 2 ​ ℒ NCDM , \mathcal{L}_{\text{Retrieval}}=\mathcal{L}_{\text{Ret}}+\lambda_{1}\mathcal{L}_{\text{CSA}}+\lambda_{2}\mathcal{L}_{\text{NCDM}}, (18)

[77] p: where λ 1 \lambda_{1} and λ 2 \lambda_{2} balance causal alignment and degradation modeling. For generation, the language model remains frozen while the visual encoder is fine-tuned using only the causality-guided objectives:

[78] table: ℒ Generation = ℒ CSA + λ 3 ​ ℒ NCDM , \mathcal{L}_{\text{Generation}}=\mathcal{L}_{\text{CSA}}+\lambda_{3}\mathcal{L}_{\text{NCDM}}, (19)

[79] p: This training allows the adapted encoder to maintain stable semantics under degraded conditions. Through these unified optimization strategies, RobustVisRAG enforces structural intervention to suppress the spurious route D → Z → A D\!\to\!Z\!\to\!A while preserving the causal path S → Z sem → A S\!\to\!Z_{\text{sem}}\!\to\!A .

[80] p: Inference. At test time, we only require degradation-invariant semantics for retrieval and generation. Since the causal branch already produces Z sem Z_{\text{sem}} that has been trained to remove degradation information under the guidance of Z deg Z_{\text{deg}} , we discard the non-causal branch and feed only Z sem Z_{\text{sem}} to the downstream VisRAG modules. Thus, the inference-time computation and architecture remain compatible with the standard VisRAG pipeline, while enjoying improved robustness to visual degradations.

[81] h3: 3.3 Distortion-VisRAG Dataset

[82] p: We construct the Distortion-VisRAG (DVisRAG) dataset to evaluate the robustness of Vision-based RAG pipelines under degraded visual conditions. 1 1 1 More details on dataset statistics, collection procedures, and degradation generation methods are provided in the supplementary material. It covers seven major document VQA domains, including scientific papers, charts, slides, infographics, forms, handwritten notes, and reports, and contains a total of 367,608 question–document (Q–D) pairs. The dataset consists of two complementary parts: the Synthetic Degradation Dataset and the Real-World Degradation Dataset, corresponding to synthetic and real degradation scenarios, respectively. The synthetic subset includes 362,110 training samples and 3,607 testing samples, while the real subset contains 1,891 testing samples.

[83] p: Synthetic Degradation Dataset. This subset is built upon VisRAG [ 59 ] , encompassing all its original data sources, including ArXivQA [ 22 ] , ChartQA [ 30 ] , PlotQA [ 32 ] , InfoVQA [ 31 ] , MP-DocVQA [ 49 ] , SlideVQA [ 48 ] and Synthetic [ 59 ] . Following the degradation synthesis pipeline in UniRestore [ 6 ] , we generate twelve common types of degradation (e.g., blur, noise, brightness variation, color saturation change, and resolution reduction), each at five severity levels. For each image in the dataset, we randomly sample one degradation type and one severity level to synthesize the degraded version. The training and testing splits are identical to those of VisRAG, and all question–answer pairs remain unchanged. Only the document images are degraded to ensure full comparability and consistent evaluation settings.

[84] p: Real Degradation Dataset. This subset is designed to evaluate model generalization under real-world conditions. We randomly sample a portion of Q–D pairs from the ArXivQA and MP-DocVQA test sets of VisRAG, and additionally include document samples from RVL-CDIP [ 13 ] , yielding 1,891 non-overlapping test pairs. All documents are printed and photographed using a Sony RX100 VII camera under controlled capture settings, such as varying shutter speed, exposure compensation, and partial illumination occlusion, to create five real degradation types: blur, low light, low resolution, shadow, and paper damage. This dataset is used exclusively for testing and does not participate in training.

[85] h2: 4 Experiments

[86] p: We conduct experiments to validate the effectiveness of RobustVisRAG. Due to space limitations, detailed implementation settings and more experimental results are provided in the supplementary material.

[87] h3: 4.1 Implementation Details.

[88] p: RobustVisRAG adopts the same backbone as VisRAG [ 59 ] , using MiniCPM-V 2.0 [ 59 ] as the retriever and MiniCPM-V 2.6 [ 36 ] as the generator. Both components are initialized from pre-trained checkpoints and fine-tuned under the mixed-dataset setting, which combines the training splits of the VisRAG and DVisRAG datasets. Evaluation is conducted on three test sets: the VisRAG test split, the synthetic degradation subset, and the real degradation subset from DVisRAG. Following VisRAG [ 59 ] , we report MRR@10 (Mean Reciprocal Rank at 10) for retrieval ranking quality and Accuracy for generation performance, where the latter adopts a relaxed 5% numerical tolerance to account for rounding and OCR errors.

[89] h3: 4.2 Baselines

[90] p: Following the evaluation protocol of VisRAG [ 59 ] , we evaluate RobustVisRAG across three stages: retrieval, generation, and end-to-end. Baseline methods are categorized into two types: (i) text-based pipelines that apply OCR [ 8 ] to extract textual content from document images and then perform retrieval or generation based on recognized text, and (ii) vision-based pipelines that directly process raw images without textual conversion. Text-based methods are marked with “(T)”, while unmarked ones are vision-based.

[91] p: For retrieval, we consider multiple representative backbones, including BM25 (T) [ 41 ] , BGE-large (T) [ 54 ] , NV-Embed-v2 (T) [ 19 ] , SigLIP [ 62 ] , and ColPali [ 10 ] . We also include MiniCPM-V2.0 [ 59 ] , which serves as the retrieval backbone in VisRAG and is denoted as VisRAG-Ret. For generation, we adopt several representative models, including MiniCPM (T) [ 35 , 58 ] , and GPT-4o [ 34 ] , We further include MiniCPM-V2.6 [ 36 , 58 ] , which serves as the generation backbone in VisRAG and is denoted as VisRAG-Gen.

[92] p: To systematically analyze robustness and adaptation behavior, we introduce three configurations as follows. All models are fine-tuned following the official settings described in their respective papers, ensuring consistent optimization protocols.

[93] p: (i) Vanilla Models. Pre-trained models are directly evaluated without any fine-tuning to assess their zero-shot capability.

[94] p: (ii) Fine-tuned on VisRAG Dataset. Following the official VisRAG training protocol [ 59 ] , models are fine-tuned on the VisRAG dataset using in-domain question–document supervision, denoted as “ -FV ”.

[95] p: (iii) Fine-tuned on Mixed Dataset. Models are fine-tuned jointly on the VisRAG dataset and our DVisRAG dataset, denoted as “ -FM ”.

[96] figure: Table 1: Overall retireval performance (MRR@10) on the VisRAG and the DVisRAG datasets. “Synthetic” and “Real” denote results on the synthetic-degradation and real-degradation subsets of the DVisRAG dataset. Models # Para. VisRAG Dataset DVisRAG Dataset Synthetic Real BM25 (T) n.a 53.34 32.80 38.60 BGE-large (T) 335M 58.98 37.05 35.23 NV-Embed-v2 (T) 7.85B 72.41 47.68 49.44 MiniCPM-FV (T) 2.72B 74.94 48.54 52.09 MiniCPM-FM (T) 2.72B 73.17 49.96 51.72 SigLIP 883M 43.47 33.10 15.07 SigLIP-FV 883M 71.52 57.51 28.50 SigLIP-FM 883M 68.84 59.77 31.89 ColPali-FV 2.97B 74.57 61.22 41.70 VisRAG-Ret 3.43B 77.57 65.96 56.47 VisRAG-Ret-FM 3.43B 78.39 68.69 58.25 VisRAG-Ret-FM (FARE) 3.43B 78.42 69.11 59.39 RobustVisRAG 3.43B 80.11 73.21 63.82

[97] figure: Table 2: Overall generation performance (Accuracy) on the VisRAG and the DVisRAG datasets. Models Metric VisRAG Dataset DVisRAG Dataset Synthetic Real GPT-4o (T) top-1 44.05 26.26 27.61 top-2 47.44 29.51 28.73 top-3 47.03 30.63 29.44 Oracle 53.06 37.90 41.54 MiniCPM (T) top-1 28.44 18.58 18.21 top-2 28.43 18.06 20.07 top-3 27.79 18.18 18.80 Oracle 31.92 24.23 25.22 GPT-4o top-1 52.44 43.31 41.49 top-2 53.69 45.29 44.08 top-3 54.98 45.74 44.81 Oracle 63.50 54.52 58.61 VisRAG-Gen top-1 51.51 42.16 44.70 top-2 53.82 43.35 47.15 top-3 54.11 44.53 47.14 Oracle 63.36 51.52 62.68 VisRAG-Gen-FM (PEFT) top-1 53.92 43.64 47.22 top-2 55.44 44.51 48.82 top-3 55.22 45.18 49.35 Oracle 64.88 53.16 63.52 VisRAG-Gen-FM (FFT) top-1 55.50 44.44 47.29 top-2 56.32 45.92 49.59 top-3 55.68 46.17 49.03 Oracle 65.91 53.20 62.54 VisRAG-Gen-FM (FARE) top-1 55.49 45.68 50.95 top-2 56.87 47.75 53.14 top-3 57.02 48.18 53.46 Oracle 66.13 54.69 64.46 RobustVisRAG top-1 58.22 48.02 55.39 top-2 60.98 53.18 57.91 top-3 61.99 54.01 59.44 Oracle 67.33 57.87 69.03

[98] figure: Table 3: End-to-end retrieval–generation performance on VisRAG and DVisRAG datasets. Methods Retrieval (MRR@10) Generation (Top-1) VisRAG Dataset Synthetic Real VisRAG Dataset Synthetic Real VisRAG 77.57 65.96 56.47 50.40 41.96 42.99 VisRAG-FT 78.42 69.11 59.39 54.84 44.96 48.27 Two-Stage 77.78 66.49 53.59 50.56 42.25 40.42 RobustVisRAG 80.11 73.21 63.82 58.22 48.02 55.39

[99] h3: 4.3 Overall Results and Analysis

[100] p: Retrieval Performance. As shown in Tab. 1 , RobustVisRAG achieves the best retrieval performance across all datasets. Compared with the original VisRAG-Ret, RobustVisRAG improves retrieval accuracy by 2.54% on clean data and by 7.25% and 7.35% under synthetic and real degradations. We also compare against VisRAG- FARE , which applies adversarial robustness training to VisRAG-Ret. Even under this stronger baseline, RobustVisRAG achieves further gains of +1.69%, +4.10%, and +4.43% on the clean, synthetic, and real subsets, respectively. Three observations emerge under our setting. First, vision-based retrieval is inherently more stable under degradations, while OCR-dependent pipelines suffer from noise, blur, and illumination artifacts. Second, mixed-dataset fine-tuning ( -FM ) consistently improves degraded-domain performance, though its effect on clean accuracy varies across architectures. Third, adversarial robustness training yields limited improvement under the complex degradations scenarios in DVisRAG dataset. In contrast, RobustVisRAG explicitly disentangles semantic and degradation factors, leading to robustness that generalizes consistently across all visual conditions.

[101] p: Generation Performance. We evaluate various generation models using the retrieval results obtained from RobustVisRAG. Note that in the original VisRAG [ 59 ] , only the retriever was fine-tuned, while the generation module (VisRAG-Gen) remained frozen. To further investigate how generator adaptation affects robustness, we fine-tune VisRAG-Gen under three strategies: Full Finetuning (denoted as " -FFT "), PEFT [ 14 ] (denoted as " -PEFT "), and adversarial robustness training following FARE [ 42 ] (denoted as " -FARE ").

[102] p: We report results using the top-1, top-2, and top-3 retrieved documents, as well as under the Oracle setting, where the model is given access only to the ground-truth positive document. As shown in Tab. 2 , RobustVisRAG consistently outperforms all existing methods across different settings, achieving stable improvements on both synthetic and real-world degraded datasets. Specifically, RobustVisRAG improves over VisRAG-Gen by 6.35% under the Oracle setting and surpasses GPT-4o by 10.42%. Among the fine-tuning strategies, FARE achieves better robustness than FFT and PEFT due to its additional feature-space alignment constraint, which helps the model resist local perturbations. However, its improvement remains limited since such alignment does not explicitly disentangle semantic and degradation representations. In contrast, RobustVisRAG leverages degradation features extracted from the non-causal path as guidance to explicitly separate these factors during training, achieving stronger semantic stability and degradation invariance across both clean and corrupted inputs.

[103] p: End-to-End Performance. We further evaluate the complete retrieval–generation pipeline to assess the end-to-end robustness of RobustVisRAG compared with VisRAG-based configurations. Since VisRAG [ 59 ] and RobustVisRAG share identical retrieval and generation backbones, their differences lie solely in training and adaptation strategies. We include the following variants for comparison: (i) the vanilla VisRAG (denoted as VisRAG ); (ii) the best-performing VisRAG fintuning configuration combining VisRAG-Ret-FM (FARE) and VisRAG-Gen-FM (FARE) (denoted as VisRAG-FT ); and (iii) a two-stage enhancement strategy, where degraded images are first restored using image restoration method [ 39 ] before being fed into the vanilla VisRAG pipeline (denoted as Two-Stage ).

[104] p: As shown in Tab. 3 , RobustVisRAG outperforms all baselines under degraded conditions while maintaining comparable accuracy to the vanilla VisRAG in clean settings. On real-world degraded datasets, RobustVisRAG achieves an average improvement of 7.35% in the retrieval stage and further raises the end-to-end accuracy by 12.4%, indicating that the benefits of semantic–degradation disentanglement effectively propagate through the entire pipeline. In contrast, the two-stage enhancement strategy, though conceptually intuitive, offers limited gains since the restoration step may distort clean images and does not ensure downstream robustness under degraded conditions.

[105] figure: Table 4: Ablation on different configurations of RobustVisRAG on DVisRAG dataset. Configurations Retrieval (MRR@10) Generation (Top-1) Synthetic Real Synthetic Real Baseline 65.96 56.47 41.96 42.99 RobustVisRAG w/o U 69.12 60.28 45.34 49.54 RobustVisRAG w/o ℒ NCDM \mathcal{L}_{\text{NCDM}} 69.20 61.94 47.21 51.79 RobustVisRAG w/o ℒ CSA \mathcal{L}_{\text{CSA}} 67.48 58.24 44.96 45.72 RobustVisRAG w/o ℒ NCDM \mathcal{L}_{\text{NCDM}} & ℒ CSA \mathcal{L}_{\text{CSA}} 66.34 56.94 42.94 43.80 RobustVisRAG 73.21 63.82 48.02 55.39

[106] figure: (a) (b) (c) (d) (e) Figure 3 : Comparison of token representations under degradations: Attention visualizations of (a) VisRAG and (b) RobustVisRAG. (c) Clean version corresponding to (a) and (b). t-SNE visualization of Z deg Z_{\text{deg}} from (d) RobustVisRAG w/o ℒ NCDM \mathcal{L}_{\text{NCDM}} & ℒ CSA \mathcal{L}_{\text{CSA}} and (e) RobustVisRAG.

[107] h3: 4.4 Ablation Study

[108] p: To analyze the contribution of each component, we train all variants on the mixed dataset and evaluate them on both the VisRAG and DVisRAG test sets.

[109] p: Effectiveness of Proposed Modules. We design six configurations to analyze the contribution of each component: (i) Baseline: the original VisRAG framework; (ii) RobustVisRAG w/o U: replacing the unidirectional Non-Causal Path with a bidirectional connection. This setting is equivalent to adding a Non-Causal Token into the VisRAG architecture but training it jointly with the two objectives ℒ NCDM \mathcal{L}_{\text{NCDM}} and ℒ CSA \mathcal{L}_{\text{CSA}} , without enforcing directional separation; (iii) RobustVisRAG w/o ℒ NCDM \mathcal{L}_{\text{NCDM}} : removing the non-causal degradation modeling objective; (iv) RobustVisRAG w/o ℒ CSA \mathcal{L}_{\text{CSA}} : removing the causal semantic alignment objective; (v) RobustVisRAG w/o ℒ NCDM \mathcal{L}_{\text{NCDM}} & ℒ CSA \mathcal{L}_{\text{CSA}} : removing both loss terms simultaneously; (vi) RobustVisRAG: the full model with all proposed modules. As shown in Tab. 4 , all components contribute to improved robustness and generalization. The unidirectional attention constraint is essential for preventing semantic–degradation entanglement and preserving a clear causal separation between the two pathways, as evidenced by the comparison between (ii) and (vi). The comparison between (v) and (vi) further shows that adding a Non-Causal Path alone is insufficient; without the two proposed objectives, it fails to learn meaningful degradation features and yields only limited gains. Overall, the results demonstrate that each module in RobustVisRAG is necessary.

[110] p: Investigation of Learned token representations. To analyze how degradations affect semantic encoding, we conduct two complementary visualization studies. First, we sample a degraded image from DVisRAG and use the text query “Bar Chart” . We compute the similarity between the text embedding and the mean patch-token features, then project the similarity map back onto the image. As shown in Fig. 3 (a)(b), RobustVisRAG focuses more consistently on semantically relevant regions, whereas vanilla VisRAG is easily disrupted by degradations and tends to highlight irrelevant areas. This indicates that RobustVisRAG learns semantic representations that are significantly more degradation-invariant.

[111] p: Next, we sample 50 image–question–answer triplets and apply five types of synthetic degradations to each image. We then compare the degradation representations using the Z deg Z_{\text{deg}} features from RobustVisRAG and from the variant RobustVisRAG w/o ℒ NCDM \mathcal{L}_{\text{NCDM}} & ℒ CSA \mathcal{L}_{\text{CSA}} . As shown in Fig. 3 (c)(d), the variant without these objectives exhibits poor separability among degradation types, whereas RobustVisRAG produces clear and compact clusters. This demonstrates that the combined effect of NCDM and CSA encourages degradation-consistent structure in the latent space.

[112] h2: 5 Conclusion

[113] p: We presented RobustVisRAG, a VisRAG-oriented causality-guided dual-path framework that mitigates retrieval–generation error propagation under degradations. Through structural design and targeted objectives, RobustVisRAG improves retrieval, generation, and end-to-end performance under degradations while preserving clean-data accuracy. These gains come with no additional inference cost. We also introduce the Distortion-VisRAG dataset, a comprehensive benchmark for evaluating multimodal RAG models under degraded visual conditions.

[114] h2: References

[115] h2: Instructions for reporting errors

[116] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[117] p: Tip: You can select the relevant text first, to include it in your report.

[118] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[119] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
