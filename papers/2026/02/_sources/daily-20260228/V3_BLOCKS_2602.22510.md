[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Pix2Key: Controllable Open-Vocabulary Retrieval with Semantic Decomposition and Self-Supervised Visual Dictionary Learning

[3] h6: Abstract

[4] p: Composed Image Retrieval (CIR) uses a reference image plus a natural-language edit to retrieve images that apply the requested change while preserving other relevant visual content. Classic fusion pipelines typically rely on supervised triplets and can lose fine-grained cues, while recent zero-shot approaches often caption the reference image and merge the caption with the edit, which may miss implicit user intent and return repetitive results. We present Pix2Key, which represents both queries and candidates as open-vocabulary visual dictionaries, enabling intent-aware constraint matching and diversity-aware reranking in a unified embedding space. A self-supervised pretraining component, V-Dict-AE, further improves the dictionary representation using only images, strengthening fine-grained attribute understanding without CIR-specific supervision. On the DFMM-Compose benchmark, Pix2Key improves Recall@10 up to 3.2 points, and adding V-Dict-AE yields an additional 2.3-point gain while improving intent consistency and maintaining high list diversity.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Composed image retrieval (CIR) is a multimodal search problem where a query consists of a reference image and a natural-language edit, and the system retrieves images that realize the requested change while preserving other relevant visual content. This interaction mirrors how users search in practice: shoppers seek the same garment with a different fabric or pattern, creators look for scene variations under different conditions, and designers search for layouts with localized modifications. Compared to standard text-to-image retrieval, CIR is conditional and fine-grained: it requires understanding what is meant to change, what should remain invariant, and which details define identity. Classical CIR systems are commonly trained with triplets built from reference, edit, and target images, and learn an explicit composition function for combining visual and textual signals ( Vo et al., 2019 ) . While such supervision can be effective, it is expensive to scale and can encourage a single fused representation that implicitly decides which fine-grained attributes to preserve, often in a non-transparent manner.

[8] figure: Figure 1: Overview of Pix2Key. (a) Inference pipeline: both the composed query and candidate images are converted into visual dictionaries for unified matching, followed by diversity-aware reranking. (b) V-Dict-AE pretraining: a self-supervised autoencoding objective learns compact visual-dictionary tokens by reconstructing images through a frozen generative decoder, improving fine-grained intent alignment for retrieval. The pretrained VLM can replace the captioner in the inference pipeline for dictionary extraction.

[9] p: Recent progress in large-scale vision–language pretraining has enabled alternatives that reduce reliance on CIR-specific supervision. Contrastive pretraining in particular yields aligned image and text embeddings that generalize across domains ( Radford et al., 2021 ) . This has motivated a plethora of zero-shot CIR methods that repurpose pretrained models without triplet training. A representative line maps the reference image into a learnable textual token and composes it with the edit to form a query ( Baldrati et al., 2023 ) . Another popular practice uses a vision–language model as an image captioner, rewrites the caption according to the edit, and retrieves by matching in the language space. Despite their practicality, many zero-shot pipelines still struggle with subtle edits and localized attributes. Collapsing an image into a single token or a single sentence creates a lossy bottleneck: missing a small detail such as neckline shape, sleeve type, or a local pattern can invalidate an otherwise plausible result. In addition, ranking by similarity to a single fused query embedding often yields homogeneous top results, where near-duplicates crowd out diverse yet valid candidates. Diversity-aware reranking has a long history in information retrieval ( Carbonell and Goldstein, 1998 ) , but is rarely coupled with an intent representation that makes constraint satisfaction controllable in zero-shot CIR.

[10] p: A persistent limitation lies not only in modeling, but also in evaluation. Attribute-centric datasets typically offer structured labels but lack natural-language edits, making them unsuitable for testing language-driven intent. In contrast, popular CIR benchmarks provide reference–target pairs and edit text, yet do not include fine-grained attributes for measuring how well the returned list satisfies the requested constraints beyond the single labeled target. This mismatch prevents quantifying how many non-target candidates in the top-ranked list actually satisfy the user’s requirements, and makes it difficult to analyze similarity and diversity in an attribute-grounded way. The problem is further compounded by annotation noise: in many CIR datasets, the designated target is not necessarily the best match to the edit, which can cause supervised methods to learn spurious correlations or be penalized for retrieving a better solution than the labeled target.

[11] p: Pix2Key is introduced to address these challenges with a two-part design that remains free of CIR-specific triplet supervision while improving fine-grained controllability. First, images are represented as compact visual dictionaries, and edits are decomposed into structured constraints that explicitly separate attributes to satisfy, attributes to avoid, and attributes left underspecified by the user intent. The same dictionary representation is applied to the candidate database, turning retrieval into matching between two structured descriptions rather than fragile cross-modal fusion. A lightweight diversity-aware reranking stage then exposes a user-facing trade-off between strict constraint satisfaction and result variety, enabling multiple plausible completions when an edit admits more than one valid outcome. Second, V-Dict-AE improves the faithfulness of dictionary representations via self-supervised pretraining: a visual-dictionary autoencoder is trained to encode images into compact token sequences aligned with a frozen text encoder and a frozen diffusion decoder ( Rombach et al., 2022 ) . This training uses only images, and adapts a limited set of parameters through efficient low-rank updates ( Hu et al., 2022 ) , encouraging the representation to preserve the visual evidence most relevant to fine-grained retrieval.

[12] p: To enable attribute-grounded evaluation of both intent satisfaction and list diversity, an additional contribution is a derived benchmark DFMM-Compose built on DeepFashion-MM ( Jiang et al., 2022 ) . It augments structured attribute labels with generated edit descriptions and auxiliary tags so that CIR queries can be evaluated not only by whether a single target is retrieved, but also by how consistently the top-ranked list satisfies the intended attributes and how diverse the returned candidates are. Together, these components support a CIR system that is more controllable, more interpretable, and more measurable under realistic, noisy supervision.

[13] p: Our contributions are:

[14] p: Pix2Key, a training-free CIR framework that represents queries and candidates as visual dictionaries, making fine-grained intent constraints explicit and controllable.

[15] p: A diversity-aware reranking mechanism integrated with the dictionary-based intent representation, enabling trade-offs between constraint satisfaction and result diversity.

[16] p: V-Dict-AE, a self-supervised visual-dictionary autoencoder aligned with frozen text and diffusion components, preserving fine-grained evidence without CIR triplets.

[17] p: An attribute-grounded CIR benchmark DFMM-Compose that supports quantitative evaluation of intent satisfaction and list diversity under natural-language edits.

[18] h4: Composed image retrieval.

[19] p: CIR studies retrieval where a query combines a reference image and an edit instruction. Early supervised methods learn an explicit composition function under triplet objectives ( Vo et al., 2019 ) . Later work improves image–text fusion and matching for text-feedback retrieval, including visiolinguistic attention and explicit matching ( Chen et al., 2020 ; Delmas et al., 2022 ) , joint visual–semantic embeddings ( Chen and Bazzani, 2020 ) , compositional query learning ( Anwaar et al., 2021 ) , and CLIP-feature-based conditioned composition ( Baldrati et al., 2022 ) . Related advances also refine the shared retrieval space with normalization or metric-learning formulations ( Bogolin et al., 2022 ; Roth et al., 2022a ; Roth et al., 2022b ) and explore composed retrieval in zero-shot protocols ( Liu et al., 2023b ) , while content–style modulation further improves modeling of preserved vs. edited factors ( Lee et al., 2021 ) . Benchmarks such as FashionIQ and CIRR standardize evaluation with reference–target pairs ( Wu et al., 2021 ; Liu et al., 2021 ) , but supervision is often tied to a single labeled target, limiting intent assessment beyond target hit.

[20] h4: Tokenization-based zero-shot CIR.

[21] p: Zero-shot CIR often reuses a frozen CLIP-style retriever and represents the reference image as learnable tokens inside the text encoder. Pic2Word maps the image to a pseudo-word appended to the edit, enabling retrieval without CIR-specific training ( Saito et al., 2023 ; Radford et al., 2021 ) . SEARLE and iSEARLE cast this mapping as textual inversion, optimizing pseudo-tokens so the composed embedding aligns with the target ( Baldrati et al., 2023 ; Gal et al., 2023 ; Agnolucci et al., 2025 ) , and related token-personalization strategies are explored in PALAVRA ( Cohen et al., 2022 ) (new) . To reduce per-query optimization or increase expressiveness, FTI4CIR amortizes inversion, Context-I2W conditions tokenization on the edit context, and ISA/LinCIR move from single tokens toward sentence-level prompts while keeping CLIP-compatible indexing ( Zhang et al., 2024 ; Tang et al., 2024 ; Du et al., 2024 ; Gu et al., 2024 ) ; prompt-centric variants further support composed retrieval ( Bai et al., 2024 ) (new) . A remaining limitation is that multiple constraints must be compressed into a small token budget, while ranking still relies on a single fused similarity score.

[22] h4: Training-free inference with large VLMs.

[23] p: Another training-free line translates visual evidence into language at inference time and retrieves in text space. CIReVL captions the reference image with a VLM, rewrites the caption conditioned on the edit, and matches the rewritten text to candidates ( Karthik et al., 2024 ) . This avoids per-query optimization and yields an interpretable intermediate query, but performance depends on caption coverage and rewriting stability, so omitted attributes or underspecified invariants can cause drift. Such pipelines build on foundation VLMs and image–text pretraining, including CLIP-style encoders and instruction-tuned multimodal models ( Radford et al., 2021 ; Li et al., 2023 ; Liu et al., 2023a ; Bai et al., 2025 ; Wang et al., 2024 ; Yu et al., 2022 ; Singh et al., 2022 ) .

[24] figure: Method Dresses Shirts Tops&Tees Avg R@10 R@50 R@10 R@50 R@10 R@50 R@10 R@50 Training-free methods: Image-only 4.76 12.35 7.07 15.82 6.87 14.64 6.23 14.27 Text-only 14.86 34.14 19.57 33.79 21.17 39.39 18.53 35.77 Image + Text 13.57 31.27 14.96 26.70 19.35 33.74 15.96 30.57 CIReVL ( Karthik et al., 2024 ) 23.74 45.62 29.01 47.65 30.87 52.76 27.87 48.68 Pix2Key 24.92 47.19 30.62 49.64 32.00 54.61 29.18 50.48 With pretrained tokenization: Pic2Word ( Saito et al., 2023 ) 20.00 40.20 26.20 43.60 27.90 47.40 24.70 43.70 PALAVRA ( Cohen et al., 2022 ) 17.25 35.94 21.49 37.05 20.55 38.76 19.76 37.25 SEARLE ( Baldrati et al., 2023 ) 20.48 43.13 26.89 45.58 29.32 49.97 25.56 46.23 FTI4CIR ( Zhang et al., 2024 ) 24.39 47.84 31.35 50.59 32.43 54.21 29.39 50.88 Pix2Key+V-Dict-AE 25.61 48.92 31.69 51.43 32.58 55.39 29.96 51.91 Table 1: FashionIQ composed image retrieval results, reported as Recall@10 and Recall@50 on Dresses, Shirts, and Tops&Tees, as well as the overall average. Image-only , Text-only , and Image+Text denote unimodal and naive fusion baselines under the standard evaluation protocol. Pix2Key variants are highlighted in orange . Best in each column is in bold .

[25] h2: 2 Method

[26] h3: 2.1 Problem Setup

[27] p: Pix2Key targets composed image retrieval (CIR), where a query is formed by a reference image together with a natural-language edit. The goal is to retrieve images that satisfy the edit while preserving other relevant visual content. Pix2Key uses an open-vocabulary visual dictionary as a shared interface for both queries and database images, so retrieval can be implemented as similarity search in a text embedding space. A self-supervised visual-dictionary autoencoder, V-Dict-AE, further refines the dictionary representation without requiring CIR triplets.

[28] p: Let the retrieval database be ℐ = { I i } i = 1 N \mathcal{I}=\{I_{i}\}_{i=1}^{N} . A composed query is a pair ( I q , T ) (I_{q},T) , where I q I_{q} is the reference image and T T is a free-form edit instruction. The system returns a ranked list π \pi over ℐ \mathcal{I} . Throughout the paper, cosine distance is used for nearest-neighbor search,

[29] table: dist ⁡ ( 𝐱 , 𝐲 ) = 1 − cossim ⁡ ( 𝐱 , 𝐲 ) . \dist(\mathbf{x},\mathbf{y})\;=\;1-\cossim(\mathbf{x},\mathbf{y}). (1)

[30] p: This distance is equivalent to cosine similarity up to an order-preserving transformation, and matches the implementation used in retrieval and reranking.

[31] h3: 2.2 Open-Vocabulary Visual Dictionaries

[32] p: Each gallery image is converted into an open-vocabulary dictionary of attribute-like facts,

[33] table: 𝒟 img ​ ( I ) = { ( k m , v m ) } m = 1 M . \mathcal{D}_{\mathrm{img}}(I)\;=\;\{(k_{m},v_{m})\}_{m=1}^{M}. (2)

[34] p: where k m k_{m} is an attribute key (e.g., color , pattern ) and v m v_{m} is its value (e.g., red , striped ). A composed query is represented by a signed dictionary

[35] table: 𝒟 q = { ( k m , v m , p m ) } m = 1 M q , p m ∈ { + 1 , 0 , − 1 } . \mathcal{D}_{q}\;=\;\{(k_{m},v_{m},p_{m})\}_{m=1}^{M_{q}},\qquad p_{m}\in\{+1,0,-1\}. (3)

[36] p: The intent polarity p m p_{m} is defined only on the query side: p m = + 1 p_{m}=+1 indicates desired attributes (add/strengthen), p m = − 1 p_{m}=-1 indicates attributes to avoid (remove/contradict), and p m = 0 p_{m}=0 denotes open-set anchors that are not explicitly constrained but help preserve salient context from the reference image.

[37] p: A vision-language model extracts 𝒟 img ​ ( I ) \mathcal{D}_{\mathrm{img}}(I) from an image using a constrained prompt format that encourages short key–value descriptions. In experiments, Qwen-VL style models are used as the extractor due to strong visual grounding and attribute coverage ( Bai et al., 2025 ; Wang et al., 2024 ) . For a composed query ( I q , T ) (I_{q},T) , we first extract 𝒟 ref = 𝒟 img ​ ( I q ) \mathcal{D}_{\mathrm{ref}}=\mathcal{D}_{\mathrm{img}}(I_{q}) , then decompose the edit text into signed updates Δ ​ 𝒟 ​ ( T ) = { ( k , v , p ) } \Delta\mathcal{D}(T)=\{(k,v,p)\} , and finally merge them:

[38] table: 𝒟 q = Merge ⁡ ( 𝒟 ref , Δ ​ 𝒟 ​ ( T ) ) , \mathcal{D}_{q}\;=\;\mathrm{Merge}\!\big(\mathcal{D}_{\mathrm{ref}},\,\Delta\mathcal{D}(T)\big), (4)

[39] p: where edits override conflicting reference entries on the same key, negative entries are kept as explicit constraints, and unconstrained entries can serve as anchors that encourage preservation when the edit underspecifies invariants.

[40] h3: 2.3 Text-Space Indexing from Dictionaries

[41] p: Pix2Key converts database images into dictionary text offline and indexes them in a text embedding space. Compared to caption-based pipelines, we serialize only attribute-like key–value facts to reduce nuisance details and expose a controllable interface via intent polarity, while still enabling efficient offline indexing with a single text embedding per gallery item.

[42] p: A dictionary is serialized into a short string ser ⁡ ( 𝒟 ) \mathrm{ser}(\mathcal{D}) (e.g., key:value; key:value; … ). A frozen text encoder f text f_{\text{text}} maps the serialized dictionary into a global embedding:

[43] table: 𝐞 i = f text ​ ( ser ⁡ ( 𝒟 ⁡ ( I i ) ) ) ∈ ℝ d . \mathbf{e}_{i}\;=\;f_{\text{text}}\!\big(\mathrm{ser}(\mathcal{D}(I_{i}))\big)\in\mathbb{R}^{d}. (5)

[44] p: In practice, f text f_{\text{text}} is an OpenCLIP text encoder initialized from public pretrained weights; all 𝐞 i \mathbf{e}_{i} are precomputed and stored for fast nearest-neighbor search.

[45] p: For queries, 𝒟 q \mathcal{D}_{q} is split by polarity and each subset is serialized and embedded:

[46] table: ser ⁡ ( 𝒟 q + ) , ser ⁡ ( 𝒟 q 0 ) , ser ⁡ ( 𝒟 q − ) . \mathrm{ser}(\mathcal{D}_{q}^{+}),\qquad\mathrm{ser}(\mathcal{D}_{q}^{0}),\qquad\mathrm{ser}(\mathcal{D}_{q}^{-}). (6)

[47] table: 𝐪 + , 𝐪 0 , 𝐪 − ∈ ℝ d . \mathbf{q}^{+},\;\mathbf{q}^{0},\;\mathbf{q}^{-}\;\in\;\mathbb{R}^{d}. (7)

[48] p: This keeps the retrieval space unified (queries and candidates share the same text embedding space) while preserving polarity-aware control.

[49] h3: 2.4 Intent-Aware Relevance Scoring

[50] p: Given a candidate embedding 𝐞 i \mathbf{e}_{i} and query embeddings from Eq. equation 7 , Pix2Key computes aligned similarity terms:

[51] table: p i \displaystyle p_{i} = cossim ⁡ ( 𝐪 + , 𝐞 i ) , \displaystyle=\,\cossim(\mathbf{q}^{+},\mathbf{e}_{i}), (8) o i \displaystyle o_{i} = cossim ⁡ ( 𝐪 0 , 𝐞 i ) , \displaystyle=\,\cossim(\mathbf{q}^{0},\mathbf{e}_{i}), n i \displaystyle n_{i} = cossim ⁡ ( 𝐪 − , 𝐞 i ) . \displaystyle=\,\cossim(\mathbf{q}^{-},\mathbf{e}_{i}).

[52] p: A single scalar relevance score is formed as

[53] table: R ⁡ ( i ) = α ​ p i + β ​ o i − ( 1 − α ) ​ n i , R(i)\;=\;\alpha\,p_{i}\;+\;\beta\,o_{i}\;-\;(1-\alpha)\,n_{i}, (9)

[54] p: where α \alpha balances enforcing requested changes against suppressing forbidden attributes, and β \beta controls how strongly unconstrained anchors are preserved.

[55] h3: 2.5 Diversity-Aware Reranking

[56] p: Relevance-only ranking often returns near-duplicates, so Pix2Key applies a diversity-aware reranker over a candidate pool 𝒞 \mathcal{C} (see Appendix for the full procedure). Let 𝐞 i \mathbf{e}_{i} denote the global embedding of candidate i i , and define pairwise cosine distance as in Eq. equation 1 :

[57] table: dist ⁡ ( i , j ) = 1 − cossim ⁡ ( 𝐞 i , 𝐞 j ) . \dist(i,j)\;=\;1-\cossim(\mathbf{e}_{i},\mathbf{e}_{j}). (10)

[58] p: A greedy selection set S S is built by repeatedly choosing

[59] table: i ⋆ = arg ⁡ max i ∈ 𝒞 ∖ S ​ [ ( 1 − λ ) ​ R ​ ( i ) + λ ​ min j ∈ S ​ dist ⁡ ( i , j ) ] , i^{\star}\;=\;\arg\max_{i\in\mathcal{C}\setminus S}\Big[(1-\lambda)\,R(i)\;+\;\lambda\,\min_{j\in S}\dist(i,j)\Big], (11)

[60] p: where λ \lambda is a user-facing diversity control. Before reranking, we linearly normalize R ⁡ ( i ) R(i) to [ 0 , 1 ] [0,1] over 𝒞 \mathcal{C} , and rescale cosine distance as d ¯ ​ ( i , j ) = dist ⁡ ( i , j ) / 2 \bar{d}(i,j)=\dist(i,j)/2 for a consistent tradeoff across queries. This distance-form is equivalent to the classic similarity-form MMR objective up to a constant shift ( Carbonell and Goldstein, 1998 ) .

[61] figure: Method CIRR DFMM-Compose R@1 R@5 R@10 R@50 AC@50 ILD@50 R@10 R@50 Training-free methods: CIReVL ( Karthik et al., 2024 ) 23.94 52.51 66.00 86.95 36.42 46.44 18.12 35.40 CIReVL+MMR 25.17 52.93 66.12 86.45 35.79 49.26 19.30 34.82 Pix2Key 27.02 54.26 68.15 89.44 51.26 54.15 21.31 37.56 With pretrained tokenization: Pic2Word ( Saito et al., 2023 ) 23.90 51.72 65.30 87.82 33.56 46.82 16.89 32.06 SEARLE ( Baldrati et al., 2023 ) 24.20 52.40 66.30 88.60 35.75 46.19 18.94 37.35 FTI4CIR ( Zhang et al., 2024 ) 25.90 55.61 67.66 89.66 38.17 47.24 19.35 37.22 Context-I2W ( Tang et al., 2024 ) 25.60 55.10 68.50 89.80 39.59 45.56 20.87 37.15 Pix2Key+V-Dict-AE 29.06 59.44 73.36 92.08 54.44 53.96 23.58 40.96 Table 2: Results on CIRR and DFMM-Compose . CIRR is evaluated by Recall@K. DFMM-Compose reports Recall@K together with two list-level metrics computed over the top-50 retrieved candidates: AC@50 for attribute consistency and ILD@50 for intra-list diversity. Pix2Key variants are highlighted in orange . Best in each column is in bold .

[62] h3: 2.6 V-Dict-AE: Self-Supervised Visual Dictionary Autoencoder

[63] p: Dictionary extraction and query parsing can miss fine-grained cues. V-Dict-AE improves dictionary token quality using only unlabeled images by training a parameter-efficient image-to-slot module supervised through a frozen diffusion decoder, encouraging the token sequence to preserve visually salient details needed for reconstruction. The diffusion model, VAE, and the text encoder used by diffusion are frozen; only lightweight modules are trained.

[64] p: Given an image I I , a frozen visual tower extracts patch-level features:

[65] table: 𝐏 = g vis ​ ( I ) ∈ ℝ B × N × h , \mathbf{P}\;=\;g_{\text{vis}}(I)\in\mathbb{R}^{B\times N\times h}, (12)

[66] p: where B B is batch size, N N is the number of visual tokens, and h h is the VLM hidden dimension. We obtain a fixed-length slot sequence using an attention pooler with Q Q learnable queries 𝐐 0 ∈ ℝ Q × h \mathbf{Q}_{0}\in\mathbb{R}^{Q\times h} replicated across the batch. The pooler concatenates queries and patch tokens and applies a Transformer encoder:

[67] table: 𝐗 = Enc ⁡ ( [ 𝐐 0 ; 𝐏 ] ) ∈ ℝ B × ( Q + N ) × h . \displaystyle\mathbf{X}\;=\;\mathrm{Enc}\!\big([\mathbf{Q}_{0};\mathbf{P}]\big)\in\mathbb{R}^{B\times(Q+N)\times h}. (13)

[68] p: Let 𝐗 = [ 𝐱 1 , … , 𝐱 Q + N ] \mathbf{X}=[\mathbf{x}_{1},\dots,\mathbf{x}_{Q+N}] ; we take the first Q Q tokens as pooled slots:

[69] table: 𝐙 = [ 𝐱 1 , … , 𝐱 Q ] ∈ ℝ B × Q × h . \mathbf{Z}\;=\;[\mathbf{x}_{1},\dots,\mathbf{x}_{Q}]\in\mathbb{R}^{B\times Q\times h}. (14)

[70] p: To align slot features with language semantics, slots are injected into the frozen VLM in place of its image placeholder tokens. Let 𝐲 \mathbf{y} be the token ids of a prompt containing one image placeholder; the placeholder position is expanded to Q Q repeated image-token ids to form 𝐲 ~ \tilde{\mathbf{y}} . With the VLM token embedding layer Emb ⁡ ( ⋅ ) \mathrm{Emb}(\cdot) , we replace the embeddings at image-token positions by pooled slots:

[71] table: 𝐄 = Emb ⁡ ( 𝐲 ~ ) , 𝐄 img ← 𝐙 . \mathbf{E}\;=\;\mathrm{Emb}(\tilde{\mathbf{y}}),\qquad\mathbf{E}_{\text{img}}\leftarrow\mathbf{Z}. (15)

[72] p: A forward pass through the frozen VLM yields hidden states 𝐇 ∈ ℝ B × L × h \mathbf{H}\in\mathbb{R}^{B\times L\times h} , from which we obtain Q Q slot-conditioned vectors 𝐇 dict ∈ ℝ B × Q × h \mathbf{H}_{\text{dict}}\in\mathbb{R}^{B\times Q\times h} (by taking image-token positions, or by short greedy decoding and padding/truncation).

[73] p: Latent diffusion models are commonly conditioned by a CLIP-like text transformer ( Radford et al., 2021 ; Rombach et al., 2022 ) ; V-Dict-AE maps each slot into the CLIP token embedding space. Let d d be the CLIP token embedding dimension. A continuous projection head produces

[74] table: 𝐮 m = LN ⁡ ( 𝐖 ​ 𝐡 m ) for ​ m = 1 , … , Q , \mathbf{u}_{m}\;=\;\mathrm{LN}(\mathbf{W}\,\mathbf{h}_{m})\quad\text{for }m=1,\dots,Q, (16)

[75] p: where 𝐡 m \mathbf{h}_{m} is the m m -th slot vector in 𝐇 dict \mathbf{H}_{\text{dict}} , 𝐖 ∈ ℝ d × h \mathbf{W}\in\mathbb{R}^{d\times h} is trainable, and LN \mathrm{LN} is LayerNorm. A vocabulary-distributed variant predicts CLIP vocabulary logits and takes an expected embedding. Let | 𝒱 | |\mathcal{V}| be the CLIP vocabulary size and 𝐄 CLIP ∈ ℝ | 𝒱 | × d \mathbf{E}_{\text{CLIP}}\in\mathbb{R}^{|\mathcal{V}|\times d} be the frozen CLIP token embedding matrix:

[76] table: ℓ m \displaystyle\bm{\ell}_{m} = 𝐖 𝒱 ​ 𝐡 m , \displaystyle=\,\mathbf{W}_{\mathcal{V}}\,\mathbf{h}_{m}, (17) 𝐩 m \displaystyle\mathbf{p}_{m} = softmax ⁡ ( ℓ m / τ ) , \displaystyle=\,\mathrm{softmax}(\bm{\ell}_{m}/\tau), 𝐮 m \displaystyle\mathbf{u}_{m} = 𝐩 m ⊤ ​ 𝐄 CLIP . \displaystyle=\,\mathbf{p}_{m}^{\top}\mathbf{E}_{\text{CLIP}}.

[77] p: A temperature schedule sharpens the distribution during training:

[78] table: τ ← max ⁡ ( τ min , η ​ τ ) , \tau\leftarrow\max(\tau_{\min},\,\eta\,\tau), (18)

[79] p: with decay η ∈ ( 0 , 1 ) \eta\in(0,1) . A length- Q + 2 Q+2 soft prompt is formed by adding frozen beginning and end token embeddings:

[80] table: 𝐔 = [ 𝐮 BOS ; 𝐮 1 ; … ; 𝐮 Q ; 𝐮 EOS ] ∈ ℝ B × ( Q + 2 ) × d . \mathbf{U}\;=\;[\mathbf{u}_{\text{BOS}};\mathbf{u}_{1};\dots;\mathbf{u}_{Q};\mathbf{u}_{\text{EOS}}]\in\mathbb{R}^{B\times(Q+2)\times d}. (19)

[81] p: A frozen latent diffusion model supplies the self-supervised signal. The input image I I is encoded by a frozen VAE into a latent 𝐱 0 \mathbf{x}_{0} . A diffusion timestep t t and Gaussian noise ϵ \bm{\epsilon} are sampled, producing

[82] table: 𝐱 t = α t ​ 𝐱 0 + 1 − α t ​ ϵ , \mathbf{x}_{t}\;=\;\sqrt{\alpha_{t}}\,\mathbf{x}_{0}\;+\;\sqrt{1-\alpha_{t}}\,\bm{\epsilon}, (20)

[83] p: where α t \alpha_{t} denotes the cumulative noise schedule. The diffusion model is conditioned on a context produced from 𝐔 \mathbf{U} :

[84] table: 𝐜 = CLIPText ⁡ ( 𝐔 ) . \mathbf{c}\;=\;\mathrm{CLIPText}(\mathbf{U}). (21)

[85] p: Following the v-parameterization ( Salimans and Ho, 2022 ) , the target is

[86] table: 𝐯 t = α t ​ ϵ − 1 − α t ​ 𝐱 0 . \mathbf{v}_{t}\;=\;\sqrt{\alpha_{t}}\,\bm{\epsilon}\;-\;\sqrt{1-\alpha_{t}}\,\mathbf{x}_{0}. (22)

[87] p: A frozen UNet predicts 𝐯 ^ θ \hat{\mathbf{v}}_{\theta} from ( 𝐱 t , t , 𝐜 ) (\mathbf{x}_{t},t,\mathbf{c}) :

[88] table: 𝐯 ^ θ = UNet ⁡ ( 𝐱 t , t , 𝐜 ) . \hat{\mathbf{v}}_{\theta}\;=\;\mathrm{UNet}(\mathbf{x}_{t},t,\mathbf{c}). (23)

[89] p: The main training loss is

[90] table: ℒ v = 𝔼 t , ϵ ​ [ ‖ 𝐯 ^ θ − 𝐯 t ‖ 2 2 ] . \mathcal{L}_{v}\;=\;\mathbb{E}_{t,\bm{\epsilon}}\Big[\|\hat{\mathbf{v}}_{\theta}-\mathbf{v}_{t}\|_{2}^{2}\Big]. (24)

[91] p: From the v-parameterization, an estimate of the clean latent is

[92] table: 𝐱 ^ 0 = α t ​ 𝐱 t − 1 − α t ​ 𝐯 ^ θ . \hat{\mathbf{x}}_{0}\;=\;\sqrt{\alpha_{t}}\,\mathbf{x}_{t}\;-\;\sqrt{1-\alpha_{t}}\,\hat{\mathbf{v}}_{\theta}. (25)

[93] p: Decoding with the frozen VAE gives I ^ = VAE − 1 ​ ( 𝐱 ^ 0 ) \hat{I}=\mathrm{VAE}^{-1}(\hat{\mathbf{x}}_{0}) and a lightweight pixel loss

[94] table: ℒ pix = ‖ I ^ − I ‖ 1 . \mathcal{L}_{\text{pix}}\;=\;\|\hat{I}-I\|_{1}. (26)

[95] p: The final objective is

[96] table: ℒ = ℒ v + γ ​ ℒ pix . \mathcal{L}\;=\;\mathcal{L}_{v}\;+\;\gamma\,\mathcal{L}_{\text{pix}}. (27)

[97] p: In practice, γ \gamma is small so the diffusion loss remains the primary signal while the pixel loss stabilizes reconstruction.

[98] p: Only parameter-efficient modules are trained relative to full finetuning: the attention pooler, the projection head, and optional low-rank adapters inserted into the frozen VLM ( Hu et al., 2022 ) . After training, the learned pooler and adapters are reused by the dictionary extractor at inference by replacing raw patch embeddings with pooled slots from Eq. equation 14 , improving fine-grained attribute capture while preserving the retrieval interface in Sections 2.2 – 2.5 .

[99] figure: Figure 2: Qualitative comparison of composed retrieval results. Each example shows the reference image, the modification text, and the top-4 retrieved candidates.

[100] h2: 3 Experiments

[101] figure: Method pos. neg. open MMR R@50 ILD@50 AC@50 embeds pos. only ✓ ✗ ✗ ✗ 37.27 51.65 52.49 embeds pos. & neg. ✓ ✓ ✗ ✗ 39.41 51.69 53.31 embeds w/o neg. ✓ ✗ ✓ ✓ 38.56 52.80 51.72 w/o MMR reranking ✓ ✓ ✓ ✗ 40.48 49.22 53.90 Pix2Key+V-Dict-AE ✓ ✓ ✓ ✓ 40.96 53.96 54.44 Table 3: Component ablations on DFMM-Compose . Columns pos. , neg. , and open indicate whether the query dictionary includes affirmative constraints, negated constraints, and open-set anchors, respectively; MMR indicates diversity-aware reranking. Our setting is highlighted in orange , and the best value in each metric column is in bold .

[102] h3: 3.1 Experimental Setting

[103] h4: Overview.

[104] p: Pix2Key is an open-vocabulary dictionary retrieval system for CIR. At inference time, a pretrained vision–language model converts the reference image and gallery images into compact visual dictionaries, and the edit text is decomposed into polarity-aware constraints. Both query and gallery dictionaries are embedded with an OpenCLIP text encoder pretrained on LAION-2B ( Ilharco et al., 2021 ) , enabling nearest-neighbor retrieval in a shared text space, followed by MMR reranking for controllable diversity. V-Dict-AE is an optional self-supervised pretraining module that improves the dictionary representation by training a parameter-efficient slot encoder on COCO2017 ( Lin et al., 2014 ) or FashionAI ( Zou et al., 2019 ) , while keeping the same inference-time retrieval interface.

[105] p: Evaluation covers FashionIQ ( Wu et al., 2021 ) and CIRR ( Liu et al., 2021 ) for standard Recall@K, and DFMM-Compose for attribute-grounded intent satisfaction and list diversity. Comparisons include tokenization-based zero-shot methods and training-free caption-rewrite pipelines. Full details of compute, model components and weights, pretraining configuration, benchmarks, baselines, and DFMM-Compose construction are provided in Appendix .

[106] h4: DFMM-Compose Benchmark.

[107] p: DFMM-Compose is an attribute-grounded composed retrieval benchmark derived from DeepFashion-MM ( Jiang et al., 2022 ) . It is designed to evaluate not only whether the annotated target is retrieved, but also how well the returned candidate list satisfies fine-grained edit intent and how diverse the list remains. Each query consists of a reference image and a natural-language edit, while each gallery image is associated with structured attribute labels that enable intent-consistency scoring over the top-ranked results. This format supports standard Recall@K evaluation, attribute-consistency evaluation beyond a single target, and list-level diversity analysis for user-facing retrieval. Construction details and evaluation protocol are given in Appendix .

[108] h4: Metrics.

[109] p: FashionIQ and CIRR are evaluated using Recall@K, which measures whether the annotated target appears among the top-K results. DFMM-Compose additionally reports two list-level metrics on the top-50 candidates: AC@50 quantifies how well returned images satisfy attribute changes implied by the edit, and ILD@50 measures redundancy within the list using attribute-based distances. Higher values indicate better performance across metrics. Full definitions are provided in Appendix .

[110] h3: 3.2 Main Results

[111] h4: Accuracy.

[112] p: Tables 1 and 2 summarize retrieval accuracy across FashionIQ, CIRR, and DFMM-Compose. On FashionIQ (Table 1 ), Pix2Key consistently improves over unimodal and naive fusion baselines, and is competitive among training-free approaches, outperforming CIReVL under the same Qwen2.5-VL backbone used for fair comparison (Appendix ). Notably, CIReVL represents the composed query by first generating an image caption for the reference and then rewriting it with the edit prompt, so the retrieval signal is mediated by a single free-form sentence in the text space. The consistent gap to Pix2Key therefore suggests that replacing caption-level descriptions with a structured key–value dictionary interface can yield a more stable and controllable representation for composed retrieval, especially when the edit requires fine-grained attribute changes.

[113] p: Compared to methods that rely on pretrained tokenization or inversion-style modules, Pix2Key+V-Dict-AE achieves the strongest results across all FashionIQ categories and the overall average, indicating that self-supervised token refinement complements dictionary-based retrieval. On CIRR (Table 2 ), Pix2Key improves Recall@K over the training-free caption-rewrite baseline, and the pretrained variant further raises performance, yielding the best Recall@1/5/10/50 among all compared methods. On DFMM-Compose, the same trend holds: Pix2Key improves Recall@10/50 over prior baselines, and V-Dict-AE brings additional gains, suggesting that the representation improvement transfers beyond a single benchmark style and remains compatible with the same nearest-neighbor retrieval interface.

[114] h4: Intent alignment.

[115] p: DFMM-Compose enables attribute-grounded evaluation beyond target hit, since it provides fine-grained attribute labels for all gallery candidates, allowing us to quantify whether other retrieved items also satisfy the intended edit. As shown in Table 2 , prior baselines yield relatively limited attribute consistency, while Pix2Key achieves substantially higher AC@50, suggesting that polarity-aware constraints and dictionary matching better capture fine-grained intent than caption-based rewriting or token-only fusion.

[116] p: This difference is consistent with the fact that caption-rewrite pipelines (e.g., CIReVL) compress the reference evidence and the edit into a single rewritten sentence, which may under-specify attributes that should be preserved or suppressed, whereas the dictionary representation keeps explicit key–value evidence and separates desired, avoided, and open anchors. Adding V-Dict-AE further improves AC@50 together with Recall, indicating that reconstruction-shaped pretraining helps preserve the visual evidence that matters for downstream attribute-level satisfaction under composed edits.

[117] h4: Diversity.

[118] p: DFMM-Compose also supports list-level analysis because all candidates carry fine-grained attributes (and auxiliary tags), making it possible to measure redundancy and within-list variation in an interpretable space. In Table 2 , Pix2Key achieves the highest ILD@50 among compared methods, indicating a less redundant candidate list under the same retrieval budget. Pix2Key+V-Dict-AE maintains similarly high ILD@50 while improving Recall@K and AC@50, suggesting that representation refinement does not collapse retrieval neighborhoods and remains compatible with diversity-aware reranking. This behavior is consistent with Pix2Key’s design: intent is scored with polarity-aware relevance, while diversity is controlled at the list level via MMR, allowing multiple plausible results without drifting away from the edit intent.

[119] figure: learn. rate R@5 5 × 10 − 5 5\times 10^{-5} 59.44 1 × 10 − 5 1\times 10^{-5} 58.50 5 × 10 − 6 5\times 10^{-6} 57.93 (a) Learning rate. depth R@5 3 59.01 5 59.44 9 56.90 (b) Pooler depth. input size R@5 64 58.01 128 58.63 224 59.44 (c) Input size. setting R@5 original 58.27 refined prompt 59.44 (d) Refined prompt. setting R@5 w/o LoRA 57.20 with LoRA 59.44 (e) LoRA. setting R@5 ViT-B/32 59.44 ViT-L/14 59.12 (f) Text encoder. Table 4: Sensitivity analysis on CIRR , reported as Recall@5. Each subtable varies a single factor while keeping the remaining settings fixed. The default configuration in each sub-study is highlighted in orange , and the best value is shown in bold . Text encoder denotes the backbone used for embedding dictionary text into the retrieval space.

[120] h3: 3.3 Ablations

[121] h4: Components.

[122] p: Table 3 indicates that relying on affirmative constraints alone offers limited leverage for fine-grained edits, and yields the weakest Recall@50 together with a comparatively low AC@50. Adding explicit negation increases both measures, suggesting that describing attributes to avoid helps separate visually plausible but intent-violating candidates from true matches, especially when edits involve subtle attribute swaps. Introducing open-set anchors without negation tends to raise ILD@50, reflecting a broader and less redundant candidate set, but AC@50 drops in this setting, implying that anchors emphasize preserving general context and may weaken attribute specificity when conflicting cues are not suppressed. When affirmative, negative, and open-set signals are used together, Recall@50 increases further and AC@50 remains competitive, supporting the view that anchors are most effective when paired with explicit suppression to maintain a clearer notion of the intended change.

[123] h4: Diversity control.

[124] p: Table 3 also isolates the effect of diversity-aware reranking under the same intent representation. With MMR enabled, ILD@50 increases markedly, while Recall@50 and AC@50 remain stable and slightly improve in this ablation, suggesting that reranking can diversify the top-50 list without noticeably compromising intent satisfaction in this setting. Notably, applying MMR reranking to CIReVL slightly lowers Recall@50 on both CIRR and DFMM-Compose, suggesting that caption-and-rewrite representations provide a less stable relevance signal under diversity control, whereas Pix2Key’s dictionary-based representation is more compatible with MMR and can diversify results without the same degree of ranking degradation.

[125] h4: Sensitivity.

[126] p: Table 4 suggests that Pix2Key is not overly brittle on CIRR under reasonable hyperparameter changes, as measured by Recall at five. A moderate learning rate performs best, indicating that the trainable dictionary modules benefit from sufficiently strong updates under a frozen backbone. Pooler depth shows a clear sweet spot in the middle range. Depth 5 achieves 59.44, depth 3 remains close at 59.01, and depth 9 drops to 56.90, which is consistent with the pooler acting as a lightweight summarizer rather than a full feature re encoder. Higher input resolution consistently improves performance. Increasing the resolution from 64 to 224 raises Recall at five from 58.01 to 59.44, suggesting that finer local evidence helps preserve subtle attributes under natural language edits. Prompt refinement also improves results, increasing the score from 58.27 to 59.44, and enabling LoRA provides an additional gain from 57.20 to 59.44, supporting the view that better extraction and targeted adaptation improve alignment without full finetuning. Finally, the OpenCLIP text encoder choice is stable in this study. ViT-B/32 reaches 59.44 and ViT-L/14 reaches 59.12. Overall, the strongest gains come from factors that improve fine grained evidence and representation alignment, which matches the intended design of Pix2Key and V-Dict-AE.

[127] h2: 4 Conclusion

[128] p: We introduce Pix2Key, a controllable composed image retrieval framework that represents both queries and candidates as open vocabulary visual dictionaries. The edit instruction is decomposed into intent signals that specify what to add, what to avoid, and what to keep open as anchors. This design provides an explicit and interpretable control interface, while reducing retrieval to fast nearest neighbor search in a shared text embedding space. To support user facing exploration, Pix2Key applies diversity aware reranking that increases variety among the top results without sacrificing relevance. We further propose V-Dict-AE, a parameter efficient self supervised module that refines dictionary slots through reconstruction based supervision, strengthening fine grained visual evidence without requiring composed retrieval triplets. Experiments show consistent improvements in Recall at K, attribute consistency, and intra list diversity over strong zero shot baselines and competitive caption based retrieval pipelines. Pix2Key also enables attribute retrieval and diagnostic analysis through its dictionary interface. Overall, Pix2Key provides a practical and scalable approach to intent aware composed image retrieval.

[129] h2: Impact Statement

[130] p: This paper aims to advance machine learning research in composed image retrieval by improving alignment between a reference image and a natural-language edit, as well as the diversity and consistency of retrieved results. The expected positive impact is to enable more controllable and efficient search for benign applications such as e-commerce, creative design, and visual content organization.

[131] p: Our method is trained with self-supervision on public datasets, which reduces reliance on human-provided labels and may lessen risks from annotation errors. However, the learned representations can still reflect biases in the underlying data distributions. Additional risks include retrieval of sensitive or copyrighted content, or privacy-invasive use when combined with external data sources. We encourage responsible deployment with content filtering, access control, dataset governance, and auditing practices. Overall, we do not anticipate ethical concerns beyond those commonly associated with vision-language retrieval systems, but responsible use remains important.

[132] h2: References

[133] h2: Instructions for reporting errors

[134] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[135] p: Tip: You can select the relevant text first, to include it in your report.

[136] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[137] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
