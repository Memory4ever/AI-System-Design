[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: DocDjinn: Controllable Synthetic Document Generation with VLMs and Handwriting Diffusion

[3] h6: Abstract

[4] p: Effective document intelligence models rely on large amounts of annotated training data. However, procuring sufficient and high-quality data poses significant challenges due to the labor-intensive and costly nature of data acquisition. Additionally, leveraging language models to annotate real documents raises concerns about data privacy. Synthetic document generation has emerged as a promising, privacy-preserving alternative. We propose DocDjinn , a novel framework for controllable synthetic document generation using Vision-Language Models (VLMs) that produces annotated documents from unlabeled seed samples. Our approach generates visually plausible and semantically consistent synthetic documents that follow the distribution of an existing source dataset through clustering-based seed selection with parametrized sampling. By enriching documents with realistic diffusion-based handwriting and contextual visual elements via semantic-visual decoupling, we generate diverse, high-quality annotated synthetic documents. We evaluate across eleven benchmarks spanning key information extraction, question answering, document classification, and document layout analysis. To our knowledge, this is the first work demonstrating that VLMs can generate faithful annotated document datasets at scale from unlabeled seeds that can effectively enrich or approximate real, manually annotated data for diverse document understanding tasks. We show that with only 100 real training samples, our framework achieves on average 87 % 87\% of the performance of the full real-world dataset. We publicly release our code and 140k+ synthetic document samples.

[5] figure: Figure 1 : Examples of synthetically generated documents across diverse domains and tasks. Our framework produces documents with realistic layouts, VLM-generated content, diffusion-based handwriting, and contextual visual elements.

[6] h2: 1 Introduction

[7] p: Document intelligence systems employ deep learning and Vision-Language Models (VLMs) to transform documents into structured information via document layout analysis (DLA) [ 60 ] , key information extraction (KIE) [ 26 ] , visual question answering (VQA) [ 38 ] , and classification (CLS). While VLMs are powerful, they remain prohibitively expensive for specialized, high-throughput applications. This has motivated smaller, task-specific models [ 4 ] that require substantial labeled training data. Despite recent datasets [ 57 , 17 ] , obtaining high-quality annotations for diverse document types remains costly and labor-intensive.

[8] p: Synthetic data generation offers a promising solution. However, existing approaches either lack textual coherence [ 56 ] , generate only task-specific content such as layout [ 23 ] or tables [ 20 ] , or produce documents without ground truth (GT) annotations [ 8 , 33 , 14 , 1 ] . DocGenie [ 21 ] , while capable of conditioning generation on seed documents, generates only visual content and text without task-specific labels required for supervised learning ( e.g . entity labels for KIE, bounding boxes for DLA, question-answer pairs for VQA). Consequently, these synthetic documents cannot directly train document understanding models.

[9] p: We present DocDjinn, addressing three key challenges: (1) Multimodal realism through VLM-generated content combined with diffusion-based handwriting synthesis and contextual visual element insertion, (2) distribution alignment via automatic clustering-based seed selection with parametrized sampling strategies that align synthetic data with source dataset distributions, and (3) training suitability by generating high-quality task-specific annotations alongside documents, enabling direct supervised learning across VQA, KIE, CLS, and DLA tasks.

[10] p: Our evaluation demonstrates that synthetic-only training achieves 70.8 % 70.8\% of real-data performance, while augmenting just 100 100 real samples with synthetic data reaches within 9.45 9.45 points of full real-data training. In low-resource scenarios with only 100 100 labeled samples, our framework achieves on average 87 % 87\% of the performance of the full real-world dataset.

[11] p: Our concrete contributions are as follows:

[12] p: A scalable framework for synthetic document generation that produces automatic ground truth annotations from unlabeled seed documents across VQA, KIE, CLS, and DLA tasks.

[13] p: First integration of diffusion-generated handwriting into modern document synthesis with semantic-visual decoupling for stamps, barcodes, and logos.

[14] p: Clustering-based seed selection with parametrized sampling that preserves target distributions.

[15] p: Public release of eleven synthetic datasets ( 140 ​ k + 140\text{k}+ samples) and DocVQA-HW, a handwriting-focused DocVQA [ 38 ] subset.

[16] figure: Table 1 : Overview of recent synthetic document generation approaches compared to ours. Target specifies the generated modality, and Source the conditioning input. Text , HW , and VE indicate explicit support for readable text, readable handwritten text, and visual elements during generation. U. GT. represents the capability to automatically generate task annotations in an unsupervised manner. Max Res. denotes the maximum possible generation resolution, whereas Dyn. Spec. represents whether the generation process can be controlled via natural language. ML indicates multilingual generation ability, and OS indicates whether the framework is open source. Finally, Editable indicates whether generated documents are produced in an editable format (e.g., structured text) rather than as rasterized images. Year Name Model Target Source Text HW VE U. GT. Tasks Max Res. Dyn. Spec. ML OS Editable 2017 DocCreator [ 31 ] manual full document images ✓ ✗ ✗ ✓ OCR / DLA - ✗ ✓ ✓ ✗ 2019 Bui et al. [ 8 ] GAN document image text ✓ ✗ ✗ ✗ OCR 512 × 512 512\times 512 ✗ ✗ ✗ ✗ 2021 Genalog [ 19 ] templates document image text ✓ ✗ ✗ ✗ NER Unspec. ✗ ✗ ✓ ✗ 2021 DocSynth [ 5 ] GAN document image layout ✗ ✗ ✓ ✗ ✗ 128 × 128 128\times 128 ✗ ✗ ✓ ✓ 2021 Raman et al. [ 47 ] sampling full document layout ✓ ✗ ✓ ✓ DLA Unspec. ✗ ✓ ✗ ✗ 2022 SynthDoG [ 33 ] sampling full document - ✓ ✗ ✗ ✓ DLA 2560 × 1920 2560\times 1920 ✗ ✓ ✓ ✗ 2023 Tanveer et al. [ 56 ] DPM document image layout ✗ ✗ ✓ ✗ DLA 256 × 256 256\times 256 ✗ ✗ ✗ ✓ 2023 DocGen [ 2 ] LLM document text text ✓ ✗ ✗ ✗ IR - ✓ ✗ ✓ ✓ 2023 Fennir et al. [ 15 ] GAN document image layout ✗ ✗ ✓ ✗ ✗ 512 × 512 512\times 512 ✗ ✗ ✗ ✓ 2024 Hamdani et al. [ 20 ] DPM table image layout ✗ ✗ ✗ ✗ TE 512 × 512 512\times 512 ✗ ✗ ✗ ✗ 2024 SynthDoc [ 14 ] sampling full document text ✓ ✗ ✓ ✓ KIE 1280 × 960 1280\times 960 ✗ ✓ ✗ ✓ 2024 Hou et al. [ 27 ] sampling full table text+layout ✓ ✗ ✗ ✗ TE - ✗ ✓ ✗ ✓ 2025 Havas [ 1 ] LLM full document template ✓ ✗ ✗ ✓ KIE - ✓ ✓ ✗ ✓ 2025 DocGenie [ 21 ] VLM full document images ✓ ✗ ✗ ✗ ✗ - ✓ ✓ ✗ ✓ 2025 DocDjinn (Ours) VLM full document images ✓ ✓ ✓ ✓ CLS / KIE / VQA / DLA - ✓ ✓ ✓ ✓

[17] h2: 2 Related Work

[18] p: Recent document intelligence models mainly rely on transformers [ 58 , 28 ] and LLMs [ 13 , 7 , 46 ] . While specialized models exist for sub-tasks such as table analysis [ 40 ] or key information extraction [ 26 ] , recent models aim at multi-task full document understanding [ 58 , 33 , 28 , 58 ] . Curating high-quality datasets from real-world documents is challenging if not infeasible, if these models need to be adapted to new domains or trained from scratch. Thus, researchers have turned towards synthetic training data [ 3 ] , fostering a plethora of synthetic document generation frameworks in recent years [ 21 , 5 , 33 ] . We list a selection thereof in Tab. 1 . These works can be grouped mainly along two dimensions: the underlying model architecture, and the targeted modality of generated data. In addition, we highlight the differences between approaches in terms of the input source, support for text (printed/handwritten) and visual elements, maximum possible generation resolution, controllability via natural language, multilingual support, and whether the documents can be easily edited post-generation.

[19] p: Barring exceptions, four classes of models emerge: sampling-based strategies [ 14 , 33 , 27 ] , Generative Adversarial Networks (GANs) [ 8 , 5 , 15 ] , diffusion probabilistic models (DPMs) [ 54 ] , and Large Language Models (LLMs) [ 13 , 46 ] . Both GANs and DPMs excel at visual synthesis, enabling specialized applications in document image generation [ 56 , 20 ] , document layout generation [ 23 , 35 ] , and handwritten text generation [ 41 , 50 , 12 ] . However, they inherently lack the ability to generate coherent, contextually grounded text at large scale, as it requires discrete sequential modeling and linguistic reasoning capabilities beyond their visual architectures.

[20] p: In contrast, the language generation capabilities of LLMs [ 13 , 46 ] represent a significant advancement, allowing for controllable synthetic generation of full documents. While LLMs lack the visual generation qualities of diffusion models to synthesize specialized visual content, such as realistic handwritten text with consistent style and natural variations, their recent extension to VLMs [ 45 , 59 ] enables them to reliably process visual data. As they have been trained on markup languages, among other data, they are capable of producing visual elements solely based on markup. This is sufficient for satisfactory synthetic document generation, as the majority of documents share a structured layout. Unsurprisingly, the state of the art in synthetic document generation employs LLMs and VLMs [ 1 , 21 ] .

[21] p: Out of all recent works, to the best of our knowledge, only six works fulfill the requirements of full document generation [ 31 , 33 , 14 , 1 , 21 , 47 ] . Among these, DocCreator [ 31 ] , SynthDoG [ 33 ] , SynthDoc [ 14 ] , and Raman et al. [ 47 ] all rely on predefined templates or sampling from public corpora that limit their applications in specialized domains. Abarca & Havas [ 1 ] generate full documents with LLMs but rely on manually crafted dataset-specific templates, limiting the generalization of their approach. DocGenie [ 21 ] is the only approach that can leverage documents directly as a dynamic source without having to extract a specific modality from the source data or rely on handcrafted templates. However, since it does not produce task-specific ground-truth annotations, its applicability in downstream applications is limited. In addition, DocGenie [ 21 ] randomly selects seed samples from the source distribution to generate new documents. This limits the scalability of the approach for large document corpora, which often exhibit substantial class imbalance and contain large clusters of highly similar documents within the data distribution.

[22] p: We improve upon the limitations of DocGenie [ 21 ] by automating seed selection to obtain a representative set that captures the source data distribution and by enabling the VLM to generate task-specific ground-truth annotations. Furthermore, we combine the advantages of VLMs with those of DPMs by generating visual annotations with the VLM that serve as conditioning input for a DPM. The DPM then generates variable-style realistic handwritten text, which is injected into the documents. Thus, we present a fully automatic and unsupervised pipeline to enrich real-world datasets with plausible synthetic samples that can be directly used in downstream tasks.

[23] h2: 3 Our Framework: DocDjinn

[24] figure: Figure 2 : Overview of DocDjinn for synthetic document generation. After selecting representative seeds from a source dataset, a VLM generates an HTML representation of the document, along with multi-task ground truth information. This representation is enhanced with diffusion-generated handwriting and further visual elements. Finally, the ground truth is updated with bounding boxes and verified.

[25] p: We propose DocDjinn , a VLM-based framework for generating synthetic documents with realistic content and structurally coherent layouts alongside task-specific ground-truth annotations. Assuming a set of real unlabeled documents 𝒟 real = { x i } i = 1 N \mathcal{D_{\text{real}}}=\{x_{i}\}_{i=1}^{N} , we seek to substitute or complement it with a synthetic dataset 𝒟 syn = { ( x i ′ , y i ′ ) } i = 1 N ′ \mathcal{D}_{\text{syn}}=\{(x_{i}^{\prime},y_{i}^{\prime})\}_{i=1}^{N^{\prime}} such that a model trained on the synthetic dataset, either alone or in combination with the real dataset, approximates the original model performance on a given task. Here, x i ′ x^{\prime}_{i} denotes a synthetically generated document sample, and y i ′ y^{\prime}_{i} its corresponding annotation. DocDjinn operates in four stages, an overview of which is given in Fig. 2 : (1) intelligent seed sample selection, (2) seed-guided VLM-based document and GT synthesis, (3) visual realism enhancement via insertion of diffusion-based handwriting and visual elements, and (4) bounding box extraction and GT verification.

[26] h3: 3.1 Intelligent Seed Sample Selection

[27] p: Unlike previous work [ 21 ] , where seed samples are randomly sampled from the source dataset, we introduce a clustering-based approach to select representative yet diverse seed samples. Seed-samples are document images supplied as few-shot examples to guide the VLM during the synthesis and condition it to produce similar documents.

[28] h5: Embeddings.

[29] p: To capture both the structural and semantic characteristics of each document, we first represent documents using embeddings derived from layout, image, and text modalities. For each document d i ∈ 𝒟 real d_{i}\in\mathcal{D_{\text{real}}} , we compute embeddings using LayoutLMv3 [ 28 ] CLS tokens ( layoutlm ), CLIP [ 45 ] image features ( clip ), and Sentence Transformers [ 48 ] text representations ( sentence ). We propose a multimodal embedding ( combined ) by z-score normalizing and concatenating these three modalities, capturing layout structure, visual appearance, and textual semantics jointly. We additionally compare against pooled LayoutLMv3 embeddings ( pooled ) [ 53 ] .

[30] h5: Clustering.

[31] p: We adopt the approach from [ 53 ] by combining HDBSCAN with minimum cluster size κ \kappa and k k -NN [ 16 ] with a fixed k k . For each embedding type ℰ \mathcal{E} and minimum cluster size κ \kappa , embeddings { 𝐞 i } i = 1 N \{\mathbf{e}_{i}\}_{i=1}^{N} are reduced to d ′ d^{\prime} dimensions via UMAP. HDBSCAN produces initial clusters with noise points, which are then reassigned using a k k -NN classifier trained on non-noise embeddings, ensuring complete coverage. We manually select the optimal clustering, assisted by a heuristic combining silhouette score and normalized entropy that empirically correlates well with clustering quality and favors high internal coherence and balanced cluster sizes (Appendix 0.C ).

[32] h5: Sampling.

[33] p: From K K clusters with sizes { n c } c = 1 K \{n_{c}\}_{c=1}^{K} , we sample clusters with probabilities p ⁡ ( c ) ∝ n c α p(c)\propto n_{c}^{\alpha} , where α \alpha controls cluster size bias. We compare two strategies for generations, in each of which n n seeds are supplied as few-shot examples: cross-cluster ( 𝖢𝖢 \mathsf{CC} ) samples n n seeds independently (each according to p ⁡ ( c ) p(c) ), while intra-cluster ( 𝖨𝖢 \mathsf{IC} ) first samples one cluster via p ⁡ ( c ) p(c) , then draws all n n seeds from within that cluster. The resulting seed samples, consisting only of document images, are used to guide the VLM during document synthesis.

[34] h3: 3.2 VLM-Based Document and GT Synthesis

[35] p: Using the selected seed samples and a task-level prompt, we employ a VLM to synthesize HTML documents along with corresponding GT, generating M M documents per prompt call while supplying 2 ​ M 2M seed images as guidance (compared to 10 10 seed images used in [ 21 ] ). We distinguish two types of GT generation, corresponding to two prompt templates (see Appendix 0.G ): Macro (document-level JSON annotations), where the VLM is instructed to produce GT for VQA and simple KIE tasks, and Micro (element-level annotations with class labels), where labels are generated for layout- and structure-sensitive tasks, namely DLA and complex KIE. Each dataset is further defined by three parameters in the prompt template: document type , a brief description; GT type , specifying the annotation task (QA pair creation, KIE class labeling, document classification, or region-level labeling); and GT format , defining the ground-truth structure, i.e . , JSON or additional class groupings. We extract element regions from the HTML via JavaScript and match them to the generated GT for tasks requiring spatial annotations (KIE, DLA). Additionally, we extract bounding boxes from a PDF rendering of the HTML for subsequent processing steps.

[36] h3: 3.3 Visual Realism Enhancement

[37] p: To improve realism, we add diffusion-based handwritten text and contextual visual elements such as figures and stamps to the documents, enhancing fidelity and bridging the domain gap to real documents. The VLM is prompted to produce HTML placeholders for such elements.

[38] h5: Region Identification.

[39] p: The VLM identifies regions requiring handwriting such as signatures or form fields, as well as visual elements (stamps, barcodes, logos, figures, and photos). For handwriting, it assigns author identifiers for multi-author generation. Each designated text element is rendered with a fixed font size, its region and word-level boxes are extracted, and the placeholders are replaced by diffusion-generated handwriting while preserving layout and semantics. Visual elements are typed and given textual content descriptions, such as “APPROVED 2024-03-15” for a stamp. Each visual element is rendered type-specific (details in Appendix 0.E ) and inserted into its corresponding region.

[40] h5: Diffusion-based Handwriting.

[41] p: To synthesize realistic handwritten text, we adopt a latent diffusion model [ 51 , 36 , 41 , 50 ] conditioned on both the target text and writer style. A pretrained Variational Autoencoder (VAE) is first used to encode the handwritten text images into latent variables z ∈ ℝ d z z\in\mathbb{R}^{d_{z}} . Then, a conditional UNet-based diffusion model is trained in the latent space using the standard DPM loss [ 25 ] :

[42] table: ℒ DPM ​ ( θ ) = 𝔼 t , z 0 , ϵ ​ [ ‖ ϵ − ϵ θ ​ ( z t , t , c text , c style ) ‖ 2 2 ] , \mathcal{L}_{\text{DPM}}(\theta)=\mathbb{E}_{t,\,z_{0},\,\epsilon}\!\Big[\big\|\,\epsilon-\epsilon_{\theta}\!\big(z_{t},t;\,c_{\text{text}},c_{\text{style}}\big)\big\|_{2}^{2}\Big], (1)

[43] p: where c text c_{\text{text}} denotes the text condition embedding obtained from a Transformer-based encoder model, and c style c_{\text{style}} represents the writer-specific style embedding (writer class). Details of our diffusion training and inference parameters are provided in Appendix 0.D .

[44] figure: Figure 3 : Baseline alignment for sentence-level handwritten text. Top, left to right: input image, word segmentation, lowest-ink pixel per column (in red), and computed baseline via percentile (in blue). Bottom: example sentence-level handwritten text after baseline alignment (red).

[45] h5: Line-Segment Generation and Integration.

[46] p: Handwritten text lines are generated by concatenating style-conditioned word segments from our diffusion model with baseline alignment ( Fig. 3 ), where the baseline is the median y-coordinate of lowest ink pixels. After horizontal concatenation, segments are refined with Gaussian blur, scaled to match their bounding box union, and positioned at their corresponding region location with random jitter (details in Appendix 0.D ). A manual inspection of 200 generated handwritten sentences shows that baseline alignment is correct in 89% of cases and remains acceptable in 84% under stricter visual assessment.

[47] h3: 3.4 Bounding Box Extraction and GT Verification

[48] p: Following visual enhancement, we extract text bounding boxes via Optical Character Recognition (OCR) for documents with handwritten/visual elements or PDF rendering for typeset documents. VLM-generated GT is verified using task-specific constraints: For VQA, answers must appear in text, verified using averaged normalized Levenshtein distance (ANLS [ 6 ] ). For CLS, class labels need to be valid. In DLA, labels must be valid and regions within extracted bounds. For KIE, key-values need to appear in text, and region annotations constrained to designated areas. Documents failing verification or rendering to multiple pages are excluded.

[49] h2: 4 Experiments

[50] p: We evaluate DocDjinn along three axes: ( i ) its ability to generate visually and semantically faithful synthetic documents, ( ii ) the utility of these documents for downstream model training, and ( iii ) the impact of mixing synthetic and real-world data on model generalization. The experiments cover four major document understanding tasks: key information extraction (KIE), visual question answering (VQA), document classification (CLS), and document layout analysis (DLA).

[51] h3: 4.1 Experimental Setup

[52] h5: Embeddings and Clustering.

[53] p: For embeddings, we use LayoutLMv3 [ 28 ] ( layout ), CLIP [ 45 ] ( clip ), and Sentence Transformers [ 48 ] ( sentence ). For pooled [ 53 ] LayoutLMv3 embeddings we use a kernel size of 4. Embeddings are projected to d ′ = 100 d^{\prime}=100 via UMAP [ 39 ] before two-stage clustering, where we evaluate different min cluster sizes κ \kappa for HDBSCAN [ 10 ] and set k = 5 k=5 for k k -NN [ 16 ] . We select the embedding and κ \kappa for each dataset for downstream experiments according to Sec. 3.1 , see Appendix 0.C for details and dataset-specific clustering choices shown in Tab. 8 .

[54] h5: Document Synthesis.

[55] p: As VLM we use Claude Sonnet 4.5, as we deemed it the most capable VLM available for this task. We generate M = 3 M=3 documents per prompt call for VQA, KIE, and CLS tasks, and M = 2 M=2 for DLA tasks due to their more complex annotation requirements. VLM-generated HTML undergoes post-processing with JavaScript-based dimension measurement to ensure single-page PDF rendering via Playwright with dynamically computed page sizes. As text similarity threshold ANLS τ we use 75 % 75\% .

[56] h5: Handwriting Synthesis.

[57] p: We employ a conditional latent diffusion model trained on IAM [ 37 ] , using a pretrained VAE to encode each canonical 128 × 512 128{\times}512 word image into a 16 × 64 16{\times}64 latent (8× downsampling) while preserving stroke scale. Conditioning is applied on both text and writer identity via a UNet denoiser and Transformer text encoder. Using Microsoft Document Intelligence OCR 1 1 1 Model version 2024-11-30. and visual inspection, we retain the top nine writers (CER/WER: 0.092 / 0.249 0.092/0.249 vs. 0.193 / 0.404 0.193/0.404 ), enabling legible multi-writer synthesis across documents. See Appendix 0.D for training and architecture details.

[58] h5: Datasets.

[59] p: We conduct experiments on eleven datasets spanning multiple document understanding tasks: VQA: DocVQA [ 38 ] and WTQ [ 43 ] ; KIE: KLC [ 55 ] 2 2 2 KLC [ 55 ] is modeled as VQA for downstream evaluation (matching its extractive format) but generated as KIE during synthesis (see Appendix 0.H ). , SROIE [ 29 ] , CORD [ 42 ] , and FUNSD [ 30 ] ; CLS: Tobacco3482 [ 34 ] , RVL-CDIP [ 22 ] , and DocLayNet-CLS [ 44 ] ; DLA: PubLayNet [ 60 ] , ICDAR2019 [ 18 ] , and DocLayNet-DLA [ 44 ] . To manage costs while maintaining sufficient data volume, we limit training sets to 4,000 4{,}000 samples (except DocVQA, where we use the full train set to assess large-scale augmentation). This constraint reflects realistic resource limitations common in real-world applications. Details on dataset splits are given in Appendix 0.B . We generate 1,000 1{,}000 – 10,000 10{,}000 synthetic samples per dataset at sampling rates α ∈ { 0.5 , 0.75 , 1.0 } \alpha\in\{0.5,0.75,1.0\} , totaling over 140 140 k samples across all datasets (see Tabs. 9 and 10 in the appendix). 3 3 3 For code release and data availability, see Appendix 0.M . Additionally, we introduce DocVQA-HW, a 103 103 -sample subset of DocVQA test split with handwritten content questions, to evaluate handwriting synthesis quality. 4 4 4 For DocVQA-HW sample and question IDs, see Appendix 0.M .

[60] h5: Models and Tasks.

[61] p: We benchmark a diverse set of models representing major architectures for document understanding. We consider document understanding models BERT [ 13 ] , LiLT [ 58 ] , and LayoutLMv3 [ 28 ] for CLS, KIE, and VQA tasks, and pure vision baselines Faster R-CNN [ 49 ] and Cascade R-CNN [ 9 ] for DLA. Details to training hyperparameters are given in Appendix 0.L .

[62] h5: Metrics.

[63] p: Performance is measured using task-appropriate metrics: ANLS for DocVQA, WTQ for WTQ [ 43 ] , exact-match accuracy for CLS, F1-score for KIE, and mean Average Precision (mAP) for DLA. For generation quality, we employ FID [ 24 ] and Layout-FID [ 21 ] to assess distributional similarity between generated and real documents in pixel and learned feature spaces. We compute Layout-FID from LayoutLMv3 CLS-token embeddings. For PubLayNet and ICDAR2019, Layout-FID is computed from images only as text and bounding boxes are unavailable.

[64] h3: 4.2 Seed Selection Strategies

[65] p: We evaluate seed sampling strategies ( Sec. 3.1 ) by training LayoutLMv3 (VQA, KIE, CLS) and Faster R-CNN (DLA) exclusively on synthetic data with cross-cluster ( 𝖢𝖢 \mathsf{CC} ) versus intra-cluster ( 𝖨𝖢 \mathsf{IC} ) sampling and varying α ∈ { 0.50 , 0.75 , 1.00 } \alpha\in\{0.50,0.75,1.00\} . Tab. 2 reports means over five random seeds (std < 0.04 <0.04 ). Intra-cluster sampling consistently outperforms cross-cluster across all α \alpha values ( 59.72 % 59.72\% vs. 56.91 % 56.91\% at α = 1 \alpha=1 ), demonstrating that preserving structural coherence within document clusters is more critical than maximizing diversity across clusters. Within intra-cluster sampling, α = 1 \alpha=1 achieves highest performance ( 59.72 % 59.72\% ) and lowest Layout-FID (13.69), indicating that biasing generation toward dominant document patterns produces superior synthetic data. The improvement is particularly pronounced for classification tasks, where 𝖨𝖢 \mathsf{IC} outperforms 𝖢𝖢 \mathsf{CC} by 8.2 8.2 points on RVL-CDIP at α = 1 \alpha=1 . Based on these findings, we use intra-cluster sampling with α = 1 \alpha=1 for all experiments.

[66] figure: Dataset Smpl 𝜶 = 0.50 \alpha=0.50 𝜶 = 0.75 \alpha=0.75 𝜶 = 1.00 \alpha=1.00 Score ( ↑ \uparrow ) LFID ( ↓ \downarrow ) Score ( ↑ \uparrow ) LFID ( ↓ \downarrow ) Score ( ↑ \uparrow ) LFID ( ↓ \downarrow ) DocVQA 𝖢𝖢 \mathsf{CC} 62.46 7.60 61.51 7.49 63.16 7.52 DocVQA 𝖨𝖢 \mathsf{IC} 63.95 6.88 64.27 6.87 63.64 6.96 CORD 𝖢𝖢 \mathsf{CC} 55.62 37.31 57.03 36.95 57.74 36.75 CORD 𝖨𝖢 \mathsf{IC} 57.51 36.92 56.56 37.01 58.40 36.46 RVL-CDIP 𝖢𝖢 \mathsf{CC} 43.65 11.15 45.49 12.45 45.74 11.06 RVL-CDIP 𝖨𝖢 \mathsf{IC} 51.90 8.62 51.04 9.88 53.94 8.82 PubLayNet 𝖢𝖢 \mathsf{CC} 61.99 3.53 63.09 2.75 61.00 2.81 PubLayNet 𝖨𝖢 \mathsf{IC} 63.06 2.63 63.41 2.63 62.90 2.50 Average 𝖢𝖢 \mathsf{CC} 55.93 14.90 56.78 14.91 56.91 14.54 Average 𝖨𝖢 \mathsf{IC} 59.11 13.76 58.82 14.10 59.72 13.69 Table 2 : Layout-FID (LFID) [ 21 ] and performance comparison for 𝖢𝖢 \mathsf{CC} and 𝖨𝖢 \mathsf{IC} sampling across different α \alpha values on LayoutLMv3 (VQA, KIE, CLS) and Faster R-CNN (DLA). Results averaged over 5 seeds (std < 0.04 <0.04 ).

[67] figure: 𝐅𝐮𝐥𝐥 \mathbf{Full} 𝐅𝐞𝐰 𝐀 \mathbf{Few_{A}} 𝐅𝐞𝐰 𝐁 \mathbf{Few_{B}} 𝚫 \mathbf{\Delta} Model Dataset Task Metric ( ↑ \uparrow ) 𝐑 \mathbf{R} 𝐒 \mathbf{S} 𝐑 + 𝐒 \mathbf{R+S} 𝐑 \mathbf{R} 𝐑 + 𝐒 \mathbf{R+S} 𝐑 \mathbf{R} 𝐑 + 𝐒 \mathbf{R+S} 𝐅𝐮𝐥𝐥 − 𝐅𝐞𝐰 𝐁 \mathbf{Full{-}Few_{B}} 𝐑 − 𝐒 \mathbf{R{-}S} BERT DocVQA VQA ANLS 57.97 52.92 61.33 46.63 55.45 25.61 54.04 3.93 5.05 LiLT DocVQA VQA ANLS 70.50 64.34 72.53 58.99 66.95 38.59 64.11 6.39 6.16 LayoutLMv3 DocVQA VQA ANLS 71.45 66.03 73.26 62.91 68.04 43.61 65.82 5.63 5.42 BERT DocVQA-HW VQA ANLS 48.24 42.26 51.19 40.94 44.07 26.47 42.72 5.51 5.97 LiLT DocVQA-HW VQA ANLS 58.94 50.26 58.24 50.21 50.95 35.88 50.78 8.16 8.67 LayoutLMv3 DocVQA-HW VQA ANLS 59.41 51.25 58.36 52.31 53.31 41.20 51.24 8.17 8.16 BERT WTQ VQA WTQ 16.51 9.24 19.39 15.68 18.50 6.65 13.84 2.68 7.27 LiLT WTQ VQA WTQ 26.71 14.79 30.90 24.39 29.50 10.91 22.46 4.25 11.92 LayoutLMv3 WTQ VQA WTQ 25.64 12.76 29.47 24.20 28.66 7.86 21.61 4.04 12.89 Average VQA 48.37 40.43 50.52 41.81 46.16 26.31 42.96 5.42 7.95 BERT CORD KIE F1 93.78 49.06 93.92 90.27 90.97 84.16 85.80 7.99 44.72 LiLT CORD KIE F1 94.61 55.76 94.88 93.04 93.17 88.28 88.90 5.71 38.85 LayoutLMv3 CORD KIE F1 95.92 58.84 96.56 94.64 95.13 90.39 92.05 3.87 37.08 BERT FUNSD KIE F1 56.33 40.84 59.19 - - 54.18 56.46 -0.13 15.49 LiLT FUNSD KIE F1 74.03 49.13 74.90 - - 71.91 72.49 1.54 24.90 LayoutLMv3 FUNSD KIE F1 88.56 49.10 87.74 - - 87.46 85.69 2.87 39.46 BERT KLC KIE F1 45.22 41.90 45.00 43.98 44.46 33.66 43.11 2.11 3.32 LiLT KLC KIE F1 46.08 43.66 46.25 45.07 45.32 37.44 44.08 2.00 2.41 LayoutLMv3 KLC KIE F1 46.11 43.24 46.11 45.43 45.22 37.84 43.64 2.47 2.86 BERT SROIE KIE F1 88.12 60.94 88.97 83.78 85.32 74.90 79.35 8.77 27.18 LiLT SROIE KIE F1 94.03 70.79 93.49 91.61 91.29 83.21 87.62 6.42 23.24 LayoutLMv3 SROIE KIE F1 94.17 72.32 94.60 91.05 93.12 83.82 90.49 3.68 21.85 Average KIE 76.41 52.97 76.80 75.43 76.00 68.94 72.47 3.94 23.45 BERT DocLayNet-CLS CLS Acc 95.59 81.12 94.78 93.98 93.37 72.03 83.09 12.50 14.47 LiLT DocLayNet-CLS CLS Acc 96.35 83.97 94.31 95.32 93.47 80.24 84.79 11.56 12.39 LayoutLMv3 DocLayNet-CLS CLS Acc 97.33 82.89 97.27 96.33 96.31 66.94 89.90 7.43 14.45 BERT RVL-CDIP CLS Acc 76.87 44.40 75.23 70.06 67.65 33.48 55.42 21.45 32.46 LiLT RVL-CDIP CLS Acc 78.78 48.72 77.68 72.41 69.43 41.16 57.99 20.79 30.06 LayoutLMv3 RVL-CDIP CLS Acc 86.26 53.84 85.64 80.84 80.29 19.68 64.93 21.33 32.42 BERT Tobacco3482 CLS Acc 86.05 59.62 84.57 81.48 79.86 36.91 63.52 22.53 26.43 LiLT Tobacco3482 CLS Acc 88.05 61.76 84.19 86.57 79.19 50.67 68.48 19.57 26.29 LayoutLMv3 Tobacco3482 CLS Acc 92.43 61.14 93.38 92.14 91.62 37.90 78.86 13.57 31.28 Average CLS 88.63 64.16 87.45 85.46 83.47 48.78 71.89 16.75 24.47 Cascade R-CNN DocLayNet-DLA DLA AP 49.74 10.39 50.20 36.96 36.16 13.76 19.55 30.19 39.35 Faster R-CNN DocLayNet-DLA DLA AP 50.03 6.60 48.47 37.33 35.42 7.89 17.84 32.19 43.43 Cascade R-CNN ICDAR2019 DLA AP 87.69 64.06 91.13 84.08 88.09 67.48 84.65 3.05 23.64 Faster R-CNN ICDAR2019 DLA AP 85.52 62.10 88.56 82.64 85.04 71.37 83.26 2.26 23.42 Cascade R-CNN PubLayNet DLA AP 90.84 62.25 90.97 88.95 87.92 77.97 78.06 12.78 28.59 Faster R-CNN PubLayNet DLA AP 85.72 58.94 85.70 82.93 82.36 71.85 72.84 12.88 26.78 Average DLA 74.92 44.06 75.84 68.81 69.17 51.72 59.37 15.56 30.87 Average all 72.21 51.15 72.73 67.79 68.66 50.37 62.76 9.45 21.06 Table 3 : Performance across datasets and tasks with three training settings: (1) Full \mathrm{Full} : models trained on all real (R), all synthetic (S), or both (R+S); (2) Few A \mathrm{Few}_{A} : 300 300 – 1000 1000 real samples with/without synthetic augmentation; (3) Few B \mathrm{Few}_{B} : 100 real samples with/without synthetic augmentation. Gap columns ( Δ \Delta ) report: R Full − ( R + S ) Few B \mathrm{R_{Full}}-(\mathrm{R{+}S})_{\mathrm{Few}_{B}} (how close 100 augmented samples approaches full training) and R Full − S Full \mathrm{R_{Full}}-\mathrm{S_{Full}} (real vs synthetic quality). Bold indicates best per setting (std < 0.02 <0.02 ). Synthetic augmentation achieves +12.38 average improvement in Few B \mathrm{Few}_{B} scenarios.

[68] h3: 4.3 Downstream Task Performance

[69] p: We evaluate models on VQA, KIE, CLS, and DLA tasks under three data regimes: full-shot ( Full \mathrm{Full} ), few-shot with 300 − 1000 300-1000 real samples ( Few A \mathrm{Few}_{A} ), and few-shot with 100 100 real samples ( Few B \mathrm{Few}_{B} ). Results in Tab. 3 report means over three random seeds (std < 0.02 <0.02 ).

[70] p: Synthetic-only training demonstrates substantial quality. On DocVQA [ 38 ] , real data outperforms pure synthetic by 5.05 5.05 points, but augmenting just 100 100 real samples reduces this gap to 3.93 3.93 points. On KLC [ 55 ] , the gap is even smaller: real data exceeds pure synthetic by only 2.41 2.41 points, narrowing to 2.00 2.00 points with 100 100 real samples added. Performance gaps are larger on specialized datasets like CORD [ 42 ] ( 37 37 – 45 45 points) and DocLayNet-DLA [ 44 ] ( 39 39 – 43 43 points), reflecting domain-specific challenges in replicating real-world capture artifacts and complex annotations.

[71] p: Combining real and synthetic data consistently matches or exceeds real-only performance, with improvements on DocVQA, WTQ, and ICDAR2019, averaging + 0.51 +0.51 points. Notably, vision-based LayoutLMv3 degrades on DocVQA-HW when adding synth data while text-only BERT improves, revealing that synthetic handwriting lacks authentic visual characteristics despite recognizable content, though the difficulty of this handwriting-focused subset makes isolated quality assessment challenging.

[72] p: Synthetic augmentation proves most valuable in data-scarce settings. In Setting Few B \mathrm{Few}_{B} with only 100 100 real samples, adding synthetic data yields + 12.38 +12.38 average improvement, bringing performance within 9.45 9.45 points of full real-data training. This demonstrates substantial annotation cost reduction: augmenting minimal labeled data with synthetic samples achieves 87 % 87\% of full-dataset performance.

[73] h3: 4.4 Visual Quality Comparison

[74] p: Tab. 4 shows our framework achieves strong visual fidelity across diverse document types, with Layout-FID [ 21 ] scores below 10 10 for most datasets: WTQ ( 3.13 3.13 ), DocLayNet ( 6.35 6.35 – 6.45 6.45 ), DocVQA ( 6.96 6.96 ), and KLC ( 7.98 7.98 ). Performance on CORD is noticeably worse ( 36.46 36.46 Layout-FID, 139.52 139.52 FID). However, this is expected as CORD consists of camera-captured receipt images that contain real-world artifacts such as blur, lighting variation, and complex real-world backgrounds.

[75] p: While direct comparison is challenging due to the different nature of setting across multiple document synthesis frameworks (as in Tab. 1 ), we also compare the FID scores achieved by our approach with multiple existing works [ 21 , 5 , 56 , 15 ] . Against DocGenie [ 21 ] , which we extend, our approach achieves lower FID on CORD ( 139.52 139.52 vs. 155.34 155.34 ) and SROIE ( 63.50 63.50 vs. 109.31 109.31 ), though DocGenie reports superior Layout-FID on these datasets ( 31.30 31.30 vs. 36.46 36.46 on CORD; 3.52 3.52 vs. 17.18 17.18 on SROIE) 5 5 5 DocGenie [ 21 ] is closed-source, preventing verification of their exact Layout-FID computation. FID-based metrics can be sensitive to sample size and implementation details. We compute Layout-FID using LayoutLMv3 CLS token embeddings, which may differ from DocGenie’s unspecified approach. . Note that our 𝖢𝖢 \mathsf{CC} sampling with α = 1 \alpha=1 replicates DocGenie’s [ 21 ] seed-guided generation strategy; however, DocGenie uses 10 10 seeds, while we use 6 6 seeds for these datasets with prompting optimized for GT generation. Other methods [ 5 , 56 , 15 ] which are mostly diffusion-based achieve better FID scores on PubLayNet ( 33.75 33.75 at 128 × 128 128\times 128 , 15.02 15.02 at 256 × 256 256\times 256 vs. our 35.28 35.28 at full resolution) and DocLayNet-DLA ( 20.58 20.58 at 256 × 256 256\times 256 vs. 37.80 37.80 ) but this is expected since all these approaches synthesize new documents by training on the training distribution of the same dataset. Furthermore, these approaches typically synthesize at lower resolutions ( 128 × 128 128\times 128 to 256 × 256 256\times 256 ) and require ground truth layout annotations as input, fundamentally differing from our annotation-free approach. Our framework trades some visual fidelity for complete annotated dataset synthesis from unlabeled documents, enabling direct supervised learning across multiple tasks. For additional qualitative visual results of our framework, refer to Appendix 0.I .

[76] figure: Dataset Method Task FID ( ↓ \downarrow ) LayoutFID ( ↓ \downarrow ) DocVQA Ours VQA 41.36 6.96 WTQ Ours VQA 52.43 3.13 DocGenie [ 21 ] KIE 155.34 31.30 CORD Ours KIE 139.52 36.46 FUNSD Ours KIE 44.57 9.60 KLC Ours KIE 26.98 7.98 DocGenie [ 21 ] KIE 109.31 3.52 SROIE Ours KIE 63.50 17.18 RVL-CDIP Ours CLS 86.59 8.82 Tobacco3482 Ours CLS 61.86 14.43 DocLayNet-CLS Ours CLS 36.62 6.45 DocSynth [ 5 ] DLA 33.75 @ 128 × 128 128\times 128 - Tanveer et al . [ 56 ] DLA 15.02 @ 256 × 256 256\times 256 - Fenrir et al . [ 15 ] DLA 248 @ 256 × 256 256\times 256 - PubLayNet Ours DLA 35.28 2.50 ICDAR2019 Ours DLA 43.52 7.19 Tanveer et al . [ 56 ] DLA 20.58 @ 256 × 256 256\times 256 - DocLayNet-DLA Ours DLA 37.80 6.35 Table 4 : FID [ 24 ] and Layout-FID [ 21 ] scores comparing our method to prior work. Lower scores indicate better distributional similarity to real documents. Resolution annotations indicate synthesis resolution before upscaling for evaluation.

[77] h3: 4.5 Analysis of Failure-Cases

[78] p: While synthetic data improves few-shot performance and maintains competitive full-shot results ( Tab. 3 ), qualitative analysis reveals systematic failure modes. For KIE, despite reasonable spatial distributions (Appendix 0.K.3 ), synth-only achieves 49 49 – 72 72 F1 vs. 88 88 – 95 95 real. Real samples are camera captures with scanning artifacts and distortions absent in pristine synthetic documents; CORD additionally applies artificial selective blur to non-KIE regions. Unlike DocGenie [ 21 ] , which applies synthetic degradation post-generation, our focus on multi-task GT generation produces clean documents, creating a visual domain gap evidenced by LayoutLMv3 degrading on FUNSD ( 88.56 88.56 → \rightarrow 87.74 87.74 F1) while text-only models improve. For CLS, severe class imbalance ( Fig. 24 in Appendix) yields synth-only accuracy of 44 44 – 61 % 61\% vs. 76 76 – 92 % 92\% real, with VLMs generating memos ( ∼ 45 % \sim 45\% ) while neglecting specialized classes ( < 2 % <2\% ). For DLA, synth-only achieves 6 6 – 10 10 AP vs. 49 49 – 50 50 real; however, qualitative analysis confirms reasonable predictions, indicating low scores stem from annotation inconsistencies rather than synthesis failure. Overall, GT analysis (Appendix 0.K ) validates high semantic and spatial annotation quality - question embeddings align closely between real and synthetic samples, and spatial entity distributions are well-preserved - though class imbalance remains a limitation for classification tasks. Manual inspection reveals ∼ \sim 3% of documents across all tasks exhibit rendering failures or anomalous layouts.

[79] h3: 4.6 Discussion

[80] p: Our experiments demonstrate that VLM-based synthesis generates high-quality document distributions suitable for model training. Synthetic-only training achieves 70.8 % 70.8\% of real-data performance on average ( 51.15 % 51.15\% vs. 72.21 % 72.21\% ), closely approximating real data on several datasets with gaps as small as 2.41 2.41 points (KLC [ 55 ] ) and 5.05 5.05 points (DocVQA [ 38 ] ). Combining real and synthetic data consistently improves results: + 0.51 +0.51 in full-shot and + 0.83 +0.83 in few-shot with 300 − 1000 300-1000 samples. Most notably, augmenting only 100 100 real samples with synthetic data yields + 12.38 +12.38 improvement, achieving 87 % 87\% of full real-data performance and demonstrating substantial annotation cost reduction. Seed selection analysis ( Tab. 2 ) confirms that intra-cluster sampling with α = 1 \alpha=1 ( 59.72 % 59.72\% vs. 56.91 % 56.91\% ) preserves structural coherence more effectively than cross-cluster approaches.

[81] p: To assess reproducibility with open-weight models, we additionally evaluate Gemma 3 27B (Appendix 0.A ). While it achieves comparable visual quality when successful (e.g., similar FID/Layout-FID), pipeline success rates are significantly lower — particularly for GT generation — reflecting instruction-following limitations in current open-source VLMs rather than framework constraints. As open-weight VLMs continue to improve, we expect this gap to narrow, making our framework fully reproducible without proprietary models.

[82] p: Though successful, challenges persist: pristine synthetic documents lack real-world degradations that vision encoders utilize, class imbalance emerges in classification tasks, and annotation taxonomy differences affect DLA scores despite qualitatively reasonable predictions. Integrating document degradation techniques (as in DocGenie [ 21 ] ) with our GT generation framework could address visual domain gaps, while constrained sampling strategies could improve class balance. Overall, our framework offers a scalable, privacy-preserving approach that substantially reduces annotation costs while maintaining competitive performance across document understanding tasks.

[83] h2: 5 Conclusion

[84] p: We present a scalable framework for synthetic document generation that addresses labeled data scarcity in document understanding through VLM-based content generation, automatic ground truth annotation from unlabeled seed documents, and intelligent clustering-based seed selection. Our approach produces visually realistic documents with task-specific annotations across VQA, KIE, CLS, and DLA tasks. We release 140 ​ K 140K + synthetic samples across eleven datasets and DocVQA-HW to support other researchers.

[85] p: Comprehensive evaluation demonstrates substantial annotation cost reduction: 100 real samples augmented with synthetic data achieves 87 % 87\% of full real-data performance. Synthetic-only training reaches competitive performance compared to real data, while Layout-FID scores predominantly below 10 10 validate strong visual fidelity across diverse document types. Our clustering-based seed selection with intra-cluster sampling effectively preserves structural coherence and target distributions.

[86] p: Future work should integrate existing degradation techniques (as in DocGenie [ 21 ] ) with our multi-task GT generation framework to bridge the visual domain gap, implement constrained sampling strategies to address class imbalance, and explore content-aware generation for all visual element types. We are convinced that our framework helps accelerate data-efficient document understanding research and enables practitioners to train competitive models with minimal annotation costs.

[87] h4: Acknowledgements

[88] p: This work was partially funded by the German Federal Ministry of Education and Research (BMBF).

[89] h4: Disclosure of Interests.

[90] p: The authors have no competing interests to declare that are relevant to the content of this article.

[91] h2: References

[92] p: Supplementary Material

[93] h2: Appendix 0.A Claude vs. Gemma 3 27B Comparison

[94] p: To improve reproducibility we’ve done formal evaluation with Gemma 3 27B ( Tab. 5 ), which shows significantly lower pipeline success but comparable visual quality when successful—reflecting instruction-following limitations in current open-source VLMs, not framework constraints.

[95] figure: Pipeline Success (%) Quality Dataset Task VLM GT SP Vis FID ↓ \downarrow LFID ↓ \downarrow N Claude 92.6 92.2 95.9 45.9 7.0 6864 DocVQA VQA Gemma 69.48 0.2 73.47 73.9 9.4 6864 Claude 95.5 95.5 93.5 51.2 9.6 140 FUNSD KIE Gemma 71.9 0.0 71.1 83.2 11.2 134 Claude 91.6 97.1 98.6 93.5 10.6 850 RVL-CDIP CLS Gemma 8.5 0.7 94.6 93.4 14.3 850 Claude 89.0 91.2 97.8 37.5 3.0 1235 PubLayNet DLA Gemma 12.2 0.3 94.2 81.2 9.8 1235 Table 5 : Claude vs. Gemma 3 27B comparison. Pipeline Success : GT = valid annotations, SP = single-page renders, Vis = valid visual element and handwriting definitions (documents without handwriting/visual elements are counted as valid). Quality : FID/LFID (Layout-FID) computed on N samples (lower = better).

[96] h2: Appendix 0.B Dataset Splits

[97] figure: Dataset Train Validation Test Train (Synth) DocVQA [ 38 ] 10194 1286 1287 8082 DocVQA-HW N/A N/A 103 N/A WTQ [ 43 ] 1350 337 421 1479 SROIE [ 29 ] 626 N/A 347 1008 FUNSD [ 30 ] 149 N/A 50 259 CORD [ 42 ] 800 100 100 1182 KLC [ 55 ] 3641 953 1309 3441 Tobacco3482 [ 34 ] 2782 N/A 700 4092 RVL-CDIP [ 22 ] 4000* 4000 39998 3819 DocLayNet-CLS [ 44 ] 4000* 1000* 4999 3978 DocLayNet-DLA [ 44 ] 4000* 1000* 4999 3732 PubLayNet [ 60 ] 4000* 11245 11405 3835 ICDAR2019 [ 18 ] 600 N/A 240 1515 * For these datasets, we use a subset of the original training splits. Table 6 : Train/validation/test splits and synthetic training sets for all datasets used in our experiments. For datasets with no validation set, we use 5% of the training set as the validation set.

[98] p: Details on our dataset splits are given in Tab. 6 . As discussed in Sec. 4 , we limit training sets to 4,000 4{,}000 samples (except DocVQA, where we use the full train set to assess large-scale augmentation) to manage costs while maintaining sufficient data volume. This constraint reflects realistic resource limitations common in real-world applications.

[99] h2: Appendix 0.C Embeddings and Clustering

[100] p: To create the embeddings, we use the following checkpoints: microsoft/layoutlmv3-base for layout and pooled , openai/clip-vit-base-patch32 for clip , and all-mpnet-base-v2 for sentence .

[101] figure: Embedding κ \kappa Rank Score ↑ \uparrow combined 10 74 combined 5 72 sentence 5 65 clip 5 56 clip 10 55 sentence 10 51 pooled 10 50 pooled 5 48 layout 10 35 layout 5 27 Table 7 : Clustering configurations ranked using cumulative position scores over our base datasets.

[102] figure: Dataset Embedding κ \kappa Num Clusters Silhouette Score ↑ \uparrow Norm. Entropy ↑ \uparrow Final Score ↑ \uparrow SROIE combined 10 14 0.64 0.94 0.79 ICDAR2019 clip 5 9 0.64 0.82 0.73 WTQ combined 5 50 0.41 0.95 0.68 CORD combined 10 22 0.39 0.96 0.68 Tobacco3482 combined 10 31 0.42 0.93 0.67 DocLayNet combined 10 48 0.51 0.82 0.66 RVL-CDIP combined 10 49 0.38 0.92 0.65 FUNSD combined 10 4 0.36 0.92 0.64 KLC combined 10 41 0.35 0.86 0.61 PubLayNet clip 5 106 0.30 0.89 0.60 DocVQA sentence 5 408 0.41 0.96 0.69 DocVQA combined 5 362 0.37 0.96 0.67 DocVQA sentence 10 192 0.39 0.92 0.66 DocVQA combined 10 187 0.37 0.94 0.65 DocVQA pooled 5 370 0.35 0.95 0.65 DocVQA pooled 10 181 0.35 0.94 0.65 DocVQA clip 10 123 0.33 0.91 0.62 DocVQA clip 5 259 0.29 0.91 0.60 DocVQA layout 5 282 0.25 0.95 0.60 DocVQA layout 10 128 0.23 0.93 0.58 Table 8 : Metrics of the selected clusterings for all datasets (top) and listing of all clusterings for DocVQA (bottom), where we used combined embeddings and κ = 10 \kappa=10 for our experiments.

[103] p: We select the optimal clustering ( ℰ ∗ , κ ∗ ) (\mathcal{E}^{*},\kappa^{*}) by maximizing a heuristic quality score:

[104] table: ( ℰ ∗ , κ ∗ ) = arg ⁡ max ℰ , κ ⁡ [ S ⁡ ( C ℰ , κ ) + H ⁡ ( C ℰ , κ ) ] (\mathcal{E}^{*},\kappa^{*})=\arg\max_{\mathcal{E},\kappa}\left[S(C_{\mathcal{E},\kappa})+H(C_{\mathcal{E},\kappa})\right] (2)

[105] p: where S ⁡ ( C ) S(C) is the silhouette score [ 52 ] measuring cluster compactness and H ( C ) = − ∑ c = 1 K p c log p c H(C)=-\sum_{c=1}^{K}p_{c}\log p_{c} is normalized entropy measuring cluster balance (where p c p_{c} denotes a cluster’s proportion of the samples). This heuristic prioritizes clusterings with both high internal coherence and balanced cluster sizes, which aligns with our manual inspection showing that such configurations produce semantically meaningful, interpretable document groupings suitable for seed selection.

[106] p: Configurations ( ℰ , κ ) (\mathcal{E},\kappa) are ranked using cumulative position scores: on each dataset, the top N N configurations receive points from N N down to 1 based on their composite metric ranking. Final rankings aggregate these scores across all datasets as R ⁡ ( ℰ , κ ) = ∑ d r d ​ ( ℰ , κ ) R(\mathcal{E},\kappa)=\sum_{d}r_{d}(\mathcal{E},\kappa) and are listed in Tab. 7 . Based on these rankings and manual inspection we select a clustering configuration ( ℰ ∗ , κ ∗ ) (\mathcal{E}^{*},\kappa^{*}) for each dataset. Metrics for the selected configurations and metrics for all configurations on DocVQA [ 38 ] are shown in Tab. 8 , with the corresponding clusters visualized in Figs. 4 and 5 .

[107] figure: (a) CORD [ 42 ] , combined , κ = 10 \kappa=10 , 22 Clusters (b) DocLayNet [ 44 ] , combined , κ = 10 \kappa=10 , 48 Clusters (c) DocVQA [ 38 ] , combined , κ = 10 \kappa=10 , 187 Clusters (d) KLC [ 55 ] , combined , κ = 10 \kappa=10 , 41 Clusters (e) WTQ [ 43 ] , combined , κ = 5 \kappa=5 , 50 Clusters (f) FUNSD [ 30 ] , combined , κ = 10 \kappa=10 , 4 Clusters (g) ICDAR2019 [ 18 ] , clip , κ = 5 \kappa=5 , 9 Clusters (h) PubLayNet [ 60 ] , clip , κ = 5 \kappa=5 , 106 Clusters (i) RVL-CDIP [ 22 ] , combined , κ = 10 \kappa=10 , 49 Clusters (j) SROIE [ 29 ] , combined , κ = 10 \kappa=10 , 14 Clusters (k) Tobacco3482 [ 34 ] , combined , κ = 10 \kappa=10 , 31 Clusters Figure 4 : Overview of our used clusters for all datasets. Each clustering lists embedding type, HDBSCAN [ 10 ] minimum cluster size κ \kappa and number of resulting clusters.

[108] figure: (a) layoutlm , κ = 5 \kappa=5 , 282 Clusters (b) layoutlm , κ = 10 \kappa=10 , 128 Clusters (c) clip , κ = 5 \kappa=5 , 259 Clusters (d) clip , κ = 10 \kappa=10 , 123 Clusters (e) sentence , κ = 5 \kappa=5 , 408 Clusters (f) sentence , κ = 10 \kappa=10 , 192 Clusters (g) combined , κ = 5 \kappa=5 , 362 Clusters (h) combined , κ = 10 \kappa=10 , 187 Clusters (i) pooled , κ = 5 \kappa=5 , 370 Clusters (j) pooled , κ = 10 \kappa=10 , 181 Clusters Figure 5 : Clustering results across different embeddings and HDBSCAN [ 10 ] minimum cluster sizes κ \kappa for DocVQA [ 38 ] .

[109] h2: Appendix 0.D Implementation Details for Handwriting Synthesis

[110] p: Dataset Preparation. All experiments were conducted using the IAM handwriting dataset. Each word image was center-padded to a fixed spatial size of 128 × 512 128\times 512 pixels without resizing to ensure consistent scale across all samples. This dimension covers over 95 % 95\% of IAM words and aligns with the 8 × 8\times spatial reduction of the VAE encoder, yielding latent tensors of size [ 4 , 16 , 64 ] [4,16,64] . Each image was encoded to the latent space using the pretrained stabilityai/sd - vae - ft - mse autoencoder with a scaling factor of 0.18215 0.18215 . The LMDB dataset stored per-sample latent, grayscale image, writer ID, and text transcription.

[111] p: Model Architecture. The baseline model is a conditional latent diffusion model trained on VAE-encoded handwriting latents. The denoising network is a conditional UNet with cross-attention layers and residual blocks, conditioned jointly on text and writer identity. The text conditioning network is a transformer encoder with hidden dimension d = 512 d=512 , L = 6 L=6 layers, H = 8 H=8 attention heads, feedforward width d f ​ f = 2048 d_{ff}=2048 , and dropout rate 0.1 0.1 . The UNet operates on 4 × 16 × 64 4\times 16\times 64 latent inputs and includes class embeddings for writer conditioning. The diffusion scheduler follows the DDPM formulation with 1000 timesteps and a linear β \beta schedule from β s ​ t ​ a ​ r ​ t = 1 × 10 − 4 \beta_{start}=1\times 10^{-4} to β e ​ n ​ d = 0.02 \beta_{end}=0.02 .

[112] p: Training Hyperparameters. The model was trained using AdamW optimizer with learning rate 1 × 10 − 4 1\times 10^{-4} , β 1 = 0.9 \beta_{1}=0.9 , β 2 = 0.999 \beta_{2}=0.999 , and weight decay 0.01 0.01 . Gradient clipping was set to 1.0 1.0 . A cosine learning rate schedule was employed across 200 200 epochs. Mixed-precision training used fp16 with automatic gradient scaling. EMA of model weights was applied with decay 0.9999 0.9999 and power 1.0 1.0 . The batch size per GPU was 16 16 , with gradient accumulation for an effective batch size of 64 64 . Random seed was fixed to 42 42 . No image augmentations were applied to preserve text legibility.

[113] p: Inference and Generation. At inference time, handwriting was generated from text tokens and corresponding writer embeddings. Generation used 30 30 diffusion steps with a DPMSolver++ multistep scheduler (order 3) and a temperature of 0.5 0.5 . The VAE decoder scaled latents by 1 / 0.18215 1/0.18215 before decoding to image space. To ensure consistent scale and aspect ratio, all generations were performed directly at the 128 × 512 128\times 512 resolution without any resizing. For variable-length text, words longer than six characters were internally divided into balanced subsegments before generation, as the IAM corpus has an average word length of approximately six characters. Each subsegment was decoded separately and horizontally concatenated after generation.

[114] p: Scaling and Alignment. Two issues were explicitly addressed. (1) Scaling: generation scale was fixed to the canonical 128 × 512 128\times 512 resolution to prevent variation in stroke thickness and character proportion. (2) Alignment: baseline alignment was used for horizontal stitching. The baseline position of each segment was estimated from the bottom 50 50 th percentile of the ink mask, and subsegments were vertically aligned by matching these baselines before compositing. Refer to algorithm 1 for baseline calculation.

[115] figure: Algorithm 1 Percentile Baseline Estimation 1: RGBA segment image I ~ \tilde{I} ; opacity threshold τ \tau ; fixed percentile p = 50 p=50 2: Robust baseline b ⋆ b^{\star} 3: Extract alpha channel A A ; let 𝒞 \mathcal{C} be columns with any pixel A > τ A>\tau 4: for each column j ∈ 𝒞 j\in\mathcal{C} do 5: b j ← b_{j}\leftarrow lowest row index with A ⁡ ( r , j ) > τ A(r,j)>\tau 6: end for 7: b ⋆ ← percentile ⁡ ( { b j } j ∈ 𝒞 , p ) b^{\star}\leftarrow\operatorname{percentile}\big(\{b_{j}\}_{j\in\mathcal{C}},\,p\big) 8: return b ⋆ b^{\star}

[116] p: Post-Processing. To remove discretization artifacts and simulate pen spread, a Gaussian blur was applied with radius r ∼ 𝒰 ⁡ ( 0.35 , 0.85 ) r\sim\mathcal{U}(0.35,0.85) . An anti-aliasing pass was optionally performed using a downscale–upscale factor of 0.75 0.75 . Additional postprocessing parameters included contrast multiplier 1.02 1.02 , ink gamma 0.98 0.98 , additive Gaussian noise σ = 0.35 \sigma=0.35 (pixel intensity units), and unsharp mask parameters ( r , p , t ) = ( 0.5 , 30 , 2 ) (r,p,t)=(0.5,30,2) . The blurred outputs were composited with the alpha channel preserved to maintain soft ink boundaries.

[117] p: Summary. The overall pipeline consists of: dataset padding and latent encoding → \rightarrow conditional diffusion training → \rightarrow text-conditioned inference with sub-word segmentation → \rightarrow baseline alignment → \rightarrow Gaussian and anti-aliasing refinement. This design ensures uniform spatial scale, stable conditioning, and visually realistic handwriting suitable for integration into synthetic printed documents.

[118] figure: (a) Sentence-level synthesis with a common baseline (red) produced by our diffusion model. (b) Word-level segments with estimated baselines (blue dashed lines) used to align the final sentence. Figure 6 : Diffusion-based handwriting generation and baseline alignment. (a) The model synthesizes the full sentence “Quick Brown Fox Jumps Over 342 Lazy Dogs” with a coherent global baseline. (b) For each word segment, we estimate a robust baseline which is then used to compose the globally aligned line.

[119] figure: Figure 7 : Baseline-aligned handwriting synthesis. The figure shows multiple handwriting segments generated by our latent diffusion model. Individually synthesized words, each with an automatically estimated baseline and composition of these word segments into globally baseline-aligned sentences, demonstrating consistent geometric structure across words and lines.

[120] h2: Appendix 0.E Implementation Details for Visual Elements

[121] h5: Visual Element Rendering.

[122] p: Each visual element type requires specialized rendering: stamp elements use custom text-based generators; barcode elements encode numeric content (or random values if non-numeric) using the python-barcode library; logo , figure , and photo elements sample from image banks generated with Gemini 2.5 Flash [ 11 ] , with photo additionally incorporating synthetic faces from StyleGAN2 [ 32 ] via ThisPersonDoesNotExist.com.

[123] p: To generate the image banks, we prompt Gemini 2.5 Flash with the following instructions for each element type:

[124] p: figure : “Create an arbitrary scientific figure without any visible text and any additional requests.”

[125] p: logo : “Create an arbitrary, abstract logo without any visible text and any additional requests.”

[126] p: photo : “Create an arbitrary photo without any visible text and any additional requests.”

[127] p: The resulting images for figure , logo and photo are shown in Figs. 8 , 9 and 10 , respectively.

[128] h5: Type Mapping.

[129] p: As a post-processing step, we map certain VLM-predicted types to canonical categories: chart , diagram , plot , graph , illustration , and infographic → \rightarrow figure ; image → \rightarrow photo ; seal → \rightarrow stamp . While such mislabelings are rare, this mapping helps retain more synthesized documents. For DLA, we augment ground truth annotations with Figure / Picture regions where needed, ensuring consistency between layout structure and annotations.

[130] figure: Figure 8 : Image bank for visual elements of type figure , generated with Gemini 2.5 Flash [ 11 ] .

[131] figure: Figure 9 : Image bank for visual elements of type logo , generated with Gemini 2.5 Flash [ 11 ] .

[132] figure: Figure 10 : Image bank for visual elements of type photo , generated with Gemini 2.5 Flash [ 11 ] (top). Synthetic faces (bottom) generated with StyleGAN2 [ 32 ] via ThisPersonDoesNotExist.com.

[133] h2: Appendix 0.F Environmental Impact and Energy Estimates

[134] p: We provide conservative estimates of the energy consumption and carbon footprint of this work.

[135] p: Model Training: Training the DocDjinn models consumed approximately 2,507 GPU hours, corresponding to ∼ \sim 752 kWh of energy. Using a carbon intensity of 0.385 kg CO 2 /kWh (typical for European grids), this results in approximately 290 kg CO 2 .

[136] p: VLM Inference: Direct measurements for Claude Sonnet 4.5 are not yet available. Based on benchmarking of similar frontier models 1 1 1 Nidhal Jegham, Marwan F. Abdelatti, Lassad Elmoubarki, Abdeltawab M. Hendawi, "How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference," CoRR , vol. abs/2505.09598, 2025. , we conservatively estimate that our 533M-token workload consumed ∼ \sim 113 kWh. Using a carbon intensity of 0.287 kg CO 2 /kWh (reported for Claude infrastructure 1 1 1 Nidhal Jegham, Marwan F. Abdelatti, Lassad Elmoubarki, Abdeltawab M. Hendawi, "How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference," CoRR , vol. abs/2505.09598, 2025. ), this corresponds to approximately 33 kg CO 2 .

[137] p: Total Estimated Footprint: The combined estimated carbon footprint is ∼ \sim 323 kg CO 2 . These estimates are conservative and intended as upper bounds. Carbon offsets have been purchased through Climeworks to compensate for these emissions.

[138] h2: Appendix 0.G Prompt Templates

[139] p: We employ two prompt templates that differ in how the VLM generates ground truth (GT), corresponding to the annotation granularity required by each task family:

[140] p: (1) Macro Template (Document-Level GT): This template instructs the VLM to generate document-level GT for tasks such as VQA and simple KIE. The GT is embedded as a JSON object within <script></script> tags in the HTML, separate for each synthetic document. For instance, VQA tasks generate JSON in the form: {"Q1": "A1", "Q2": "A2", ...} , where keys are question texts and values are corresponding answers. The macro prompt template is provided below:

[141] p: (2) Micro Template (Element-Level GT): This template instructs the VLM to generate element-level GT for tasks requiring fine-grained spatial annotations, such as DLA and complex KIE. The VLM assigns each applicable HTML element a class label from a predefined set {gt_type} to uniquely identify its semantic role. For example, all elements containing figures, images, or visuals are assigned the class "LE-FIGURE" . The micro prompt template is provided below:

[142] p: Both templates are instantiated with five parameters: language, document type ( {doc_type} ), GT type ( {gt_type} ), GT format ( {gt_format} ), and the number of documents to generate ( {num_solutions} ), as described in Section 3.2 .

[143] h2: Appendix 0.H Synthetic Dataset Definitions

[144] p: Below we list the configurations for all synthetic datasets generated in this work. Each definition instantiates the prompt templates from Section 0.G , specifying the Task Type (VQA, DLA, KIE, CLS), Prompt Type (JSON or Annotation), and prompt parameters in YAML format.

[145] h2: Appendix 0.I Synthetic Dataset Samples

[146] p: This section provides visual examples from all synthetic datasets specified in Section 0.H . For each dataset, we display representative synthetic documents generated by the VLM-based synthesis pipeline in Figs. 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 and 22 . The examples demonstrate the variety in layout, typography, and content while maintaining task-specific authenticity.

[147] figure: Figure 11 : DocVQA [ 38 ] synthetic dataset samples for VQA task.

[148] figure: Figure 12 : WTQ [ 43 ] synthetic dataset samples for VQA task.

[149] figure: Figure 13 : CORD [ 42 ] synthetic dataset samples for KIE task.

[150] figure: Figure 14 : FUNSD [ 30 ] synthetic dataset samples for KIE task.

[151] figure: Figure 15 : KLC [ 55 ] synthetic dataset samples for VQA task.

[152] figure: Figure 16 : SROIE [ 29 ] syntheitc dataset samples for KIE task.

[153] figure: Figure 17 : DocLayNet-CLS [ 44 ] synthetic dataset samples for CLS task.

[154] figure: Figure 18 : RVL-CDIP [ 22 ] synthetic dataset samples for CLS task.

[155] figure: Figure 19 : Tobacco3482 [ 34 ] synthetic dataset samples for CLS task.

[156] figure: Figure 20 : DocLayNet-DLA [ 44 ] synthetic dataset samples for DLA task.

[157] figure: Figure 21 : ICDAR2019 [ 18 ] synthetic dataset samples for DLA task.

[158] figure: Figure 22 : PubLayNet [ 60 ] synthetic dataset samples for DLA task.

[159] h2: Appendix 0.J Synthetic Dataset Details

[160] p: Tables 9 and 10 report generation statistics for all synthetic datasets, including sample counts, token usage, estimated API costs, and content composition metrics. The first table shows our final configurations, while the second presents ablation variants across different sampling strategies and strengths.

[161] figure: Embedding Type Min. Cluster Size Total Samples Total Valid Samples Input Tokens (M) Output Tokens (M) Cost (USD) Avg. Words Avg. HW Elems Avg. Visual Elems Task Dataset Name CLASSIFICATION DocLayNet-CLS [ 44 ] comb 10 4494 3978 4.08 7.48 124 407 0.052 0.334 RVL-CDIP [ 22 ] comb 10 4441 3823 5.16 5.34 96 206 1.466 0.371 Tobacco3482 [ 34 ] comb 10 5292 4092 6.24 6.49 116 251 2.042 0.435 DLA DocLayNet-DLA [ 44 ] comb 10 4502 3732 2.95 7.28 114 372 0.061 0.301 ICDAR2019 [ 18 ] img 5 1594 1515 2.01 2.89 49 297 0.004 0.048 PubLayNet [ 60 ] img 5 4476 3835 5.9 12.14 200 874 0 0.542 KIE CORD [ 42 ] comb 10 1200 1182 1.19 1.66 29 67 0.007 0.158 KLC [ 55 ] comb 10 4005 3441 4.92 4.91 88 146 0.194 0.282 FUNSD [ 30 ] comb 10 291 259 0.34 0.5 9 128 3.629 0.205 SROIE [ 29 ] comb 10 1050 1008 1.46 1.62 29 113 0.089 0.124 QA DocVQA [ 38 ] comb 10 9990 8082 10.66 14.3 246 173 2.37 0.31 WTQ [ 43 ] comb 5 1604 1479 1.13 3.13 50 204 0.059 0.381 Table 9: Overview of the final synthesized datasets using sampling strategy (v2) and sampling strength ( α = 1 \alpha=1 ) in our experiments. For each dataset, we report the embedding type (image-only or image+text), clustering and sampling parameters, total and valid sample counts, token usage, estimated generation cost, and average text/visual content statistics.

[162] figure: Embedding Type Min. Cluster Size Sample Strategy Sample Alpha Total Samples Total Valid Samples Input Tokens (M) Output Tokens (M) Cost (USD) Avg. Words Avg. HW Elems Avg. Visual Elems Task Dataset Name CLASSIFICATION RVL-CDIP [ 22 ] comb 10 v1 1 4500 3853 5.04 5.28 95 211 1.305 0.397 RVL-CDIP [ 22 ] comb 10 v1 0.75 4306 3860 4.82 5.08 91 212 1.257 0.415 RVL-CDIP [ 22 ] comb 10 v1 0.5 4491 3997 5.03 5.32 96 209 1.24 0.414 RVL-CDIP [ 22 ] comb 10 v2 1 4441 3823 5.16 5.34 96 206 1.466 0.371 RVL-CDIP [ 22 ] comb 10 v2 0.75 4329 3891 5.04 5.25 94 210 1.446 0.411 RVL-CDIP [ 22 ] comb 10 v2 0.5 4407 3860 5.16 5.33 95 206 1.31 0.411 DLA PubLayNet [ 60 ] img 5 v1 1 4469 3937 5.9 12.97 212 939 0 0.536 PubLayNet [ 60 ] img 5 v1 0.75 4476 3929 5.9 12.99 213 937 0 0.551 PubLayNet [ 60 ] img 5 v1 0.5 4481 3988 5.9 13.05 213 943 0 0.568 PubLayNet [ 60 ] img 5 v2 1 4476 3835 5.9 12.14 200 874 0 0.542 PubLayNet [ 60 ] img 5 v2 0.75 4505 3949 5.91 12.25 201 882 0 0.535 PubLayNet [ 60 ] img 5 v2 0.5 4497 3930 5.9 12.41 204 891 0 0.55 KIE CORD [ 42 ] comb 10 v1 1 1200 1187 1.18 1.67 27 68 0.008 0.133 CORD [ 42 ] comb 10 v1 0.75 1200 1193 1.18 1.68 29 70 0.008 0.14 CORD [ 42 ] comb 10 v1 0.5 1200 1191 1.17 1.66 29 68 0.01 0.145 CORD [ 42 ] comb 10 v2 1 1200 1182 1.19 1.66 29 67 0.007 0.158 CORD [ 42 ] comb 10 v2 0.75 1200 1174 1.19 1.66 29 67 0.009 0.15 CORD [ 42 ] comb 10 v2 0.5 1200 1185 1.18 1.67 27 68 0.007 0.163 QA DocVQA [ 38 ] comb 10 v1 1 10002 8463 10.6 14.63 251 167 2.659 0.318 DocVQA [ 38 ] comb 10 v1 0.75 10014 8463 10.55 14.71 252 164 2.752 0.315 DocVQA [ 38 ] comb 10 v1 0.5 10013 8501 10.52 14.77 253 162 2.847 0.307 DocVQA [ 38 ] comb 10 v2 1 9990 8082 10.66 14.3 246 173 2.37 0.31 DocVQA [ 38 ] comb 10 v2 0.75 10010 8345 10.59 14.53 250 168 2.364 0.328 DocVQA [ 38 ] comb 10 v2 0.5 9990 8088 10.55 14.6 251 167 2.666 0.315 Table 10: Ablation variants generated by varying the sampling strategy (v1/v2) and sampling strength ( α \alpha ). The table reports the same statistics as Table 9 , enabling comparison of how sampling choices impact dataset size, token usage, and content composition.

[163] h2: Appendix 0.K Synthetic Ground Truth

[164] p: We provide qualitative analysis of the ground truth generated by our VLM-based synthesis pipeline across all tasks. The visualizations validate semantic consistency, spatial coherence, and annotation quality of synthetic data compared to real datasets, while also revealing systematic limitations such as class imbalance in classification tasks.

[165] h3: 0.K.1 QA

[166] p: Fig. 23 shows embeddings of question text and distributions of question types for DocVQA [ 38 ] and WTQ [ 43 ] . Question embeddings are retrieved with Sentence Transformers [ 48 ] and projected to two dimensions with UMAP [ 39 ] . Notably, the close alignment between real and synthetic question embeddings demonstrates that our VLM generates semantically similar questions without ever observing real ground truth annotations —the synthesis is guided only by seed document images and task-level prompt parameters describing the desired GT structure. Question type distributions are also well-preserved, indicating appropriate task coverage.

[167] figure: (a) DocVQA [ 38 ] question embeddings for real and synthetic data overlaid. (b) DocVQA [ 38 ] question type distributions for real and synthetic data. (c) WTQ [ 43 ] question embeddings for real and synthetic data overlaid. (d) WTQ [ 43 ] question type distributions for real and synthetic data. Figure 23 : Comparison between real and synthetic data for DocVQA [ 38 ] (a-b) and WTQ [ 43 ] (c-d). UMAP embeddings (a, c) show semantic distributions of questions, while bar charts (b, d) compare question type frequencies across datasets.

[168] h3: 0.K.2 CLS

[169] p: Fig. 24 presents class distributions for RVL-CDIP [ 22 ] , Tobacco3482 [ 34 ] , and DocLayNet-CLS [ 44 ] classification datasets. The severe class imbalance in synthetic data is evident, with certain classes (e.g., memo) heavily overrepresented while specialized classes remain undersampled. This imbalance reflects both our intra-cluster sampling strategy with α = 1 \alpha=1 that biases generation toward dominant document patterns, and the VLM’s tendency to more readily generate certain document types over others. This imbalance contributes to the performance gap observed in Section 4.5 .

[170] figure: (a) RVL-CDIP [ 22 ] (b) Tobacco3482 [ 34 ] (c) DocLayNet-CLS [ 44 ] Figure 24 : Comparisons of class distributions between real and synthetic data for RVL-CDIP [ 22 ] (a), Tobacco3482 [ 34 ] (b) and DocLayNet-CLS [ 44 ] (c).

[171] h3: 0.K.3 KIE

[172] p: Figs. 25 and 26 show spatial heatmaps comparing entity placement by type between real and synthetic data for CORD [ 42 ] , FUNSD [ 30 ] and SROIE [ 29 ] . The heatmaps demonstrate that spatial distributions of key-value entities are well-preserved, validating the quality of element-level annotations generated by our micro template without access to real annotations.

[173] figure: Figure 25 : Heatmaps comparing entity placement by type between real and synthetic for CORD [ 42 ] .

[174] figure: (a) FUNSD [ 30 ] (b) SROIE [ 29 ] Figure 26 : Heatmaps comparing entity placement by type between real and synthetic data for FUNSD [ 30 ] (a) and SROIE [ 29 ] (b).

[175] figure: (a) FUNSD [ 30 ] (b) SROIE [ 29 ] (c) CORD [ 42 ] Figure 27 : Comparison of entity type distributions between real and synthetic KIE datasets.

[176] h3: 0.K.4 DLA

[177] p: Figs. 32 and 33 present spatial heatmaps and region count distributions for ICDAR2019 [ 18 ] , PubLayNet [ 60 ] and DocLayNet-DLA [ 44 ] . While overall spatial layout patterns appear reasonable with region counts and positioning comparable to real data, detailed analysis of DocLayNet-DLA [ 44 ] predictions reveals both annotation taxonomy differences and synthesis limitations that explain the low quantitative scores: definitional mismatches in list-item classification (distance-based vs. semantic, see Fig. 28 ), insufficient variety in visual elements to capture complex images with embedded text ( Fig. 29 ), limited table diversity in size and structure ( Fig. 30 ), systematic labeling differences (e.g., chemistry formulas as "Formula" in synthetic data vs. "Picture" in real data) ( Fig. 31 ), positional biases (top-left elements consistently labeled "Title" in synthetic data, while in real data they are often labeled as "Page Header" or "Section Header"), and near-complete failure on the "Caption" class. These findings indicate that performance gaps stem from both annotation inconsistencies and limitations in synthetic document diversity.

[178] figure: Figure 28 : DocLayNet-DLA [ 44 ] GT (left) compared to predictions of Faster R-CNN [ 49 ] trained on purely synthetic data (right). Poor performance likely caused by definitional mismatches in list-item classification (distance-based vs. semantic).

[179] figure: Figure 29 : DocLayNet-DLA [ 44 ] GT (left) compared to predictions of Faster R-CNN [ 49 ] trained on purely synthetic data (right). Poor performance likely caused by insufficient variety in visual elements to capture complex images with embedded text.

[180] figure: Figure 30 : DocLayNet-DLA [ 44 ] GT (left) compared to predictions of Faster R-CNN [ 49 ] trained on purely synthetic data (right). Poor performance likely caused by limited table diversity in size and structure in our synthetic data. Our model fails to annotate the region as a single table.

[181] figure: Figure 31 : DocLayNet-DLA [ 44 ] GT (left) compared to predictions of Faster R-CNN [ 49 ] trained on purely synthetic data (right). Poor performance likely caused by insufficient detailed GT specification. Real GT annotates the formulas as "Picture", while our model annotates them as "Formula".

[182] figure: (a) ICDAR2019 [ 18 ] spatial heatmaps. (b) ICDAR2019 [ 18 ] region counts. (c) PubLayNet [ 60 ] spatial heatmaps. (d) PubLayNet [ 60 ] region counts. Figure 32 : Comparison of annotation spatial heatmaps and class distributions for real and synthetic versions of ICDAR2019 [ 18 ] (a, b) and PubLayNet [ 60 ] (c, d).

[183] figure: (a) DocLayNet-DLA [ 44 ] spatial heatmaps. (b) DocLayNet-DLA [ 44 ] region counts. Figure 33 : Comparison of annotation spatial heatmaps (top) and class distributions (bottom) for real and synthetic versions of DocLayNet-DLA [ 44 ] .

[184] h2: Appendix 0.L Evaluation Setup

[185] p: Tab. 11 summarizes the default training configurations for all models and tasks used in our experiments. For each task (CLS, KIE, VQA, DLA) and model combination, we report learning rate, batch size, number of epochs, optimizer settings, regularization parameters, and other training details. These hyperparameters were selected based on preliminary experiments and follow common practices for document understanding tasks.

[186] p: For training experiments in tasks CLS, KIE, and VQA, we fine-tune the BERT [ 13 ] , LiLT [ 58 ] , and LayoutLMv3 [ 28 ] models using their pretrained checkpoints: bert-base-uncased , SCUT-DLVCLab/lilt-roberta-en-base , and microsoft/layoutlmv3-base 1 1 1 We use the pretrained checkpoints available at https://huggingface.co/ for these models. , respectively. For the DLA task, we use the MMDetection 2 2 2 https://mmdetection.readthedocs.io/ library to fine-tune the models using their available pretrained checkpoints.

[187] p: To reduce training time and computational overhead, we adopt early stopping 3 3 3 Mahsereci, Maren, et al. "Early stopping without a validation set." arXiv preprint arXiv:1703.09580 (2017). with a patience of 10 wherever specified. Specifically, we evaluate the model on the validation set after every training epoch, and if the target metric does not exceed its best value for 10 consecutive epochs, we terminate training early. However, for training configurations Few A (R) and Few B (R), since the dataset sizes are extremely small (100, 300, or 1000 samples), we disable early stopping and train for the full number of epochs for a fair comparison. Across all experiments, we use the validation set to select the best checkpoint and report test performance using the checkpoint that achieves the highest validation score.

[188] figure: Task Model Modality Learning Rate Batch Size Epochs Optimizer Weight Decay Momentum Warmup Ratio Dropout Segment-Level Layout Early Stopping Mixed Precision Image Size BERT [ 13 ] T 1.00E-05 32 50 Adam 0.01 N/A 0.1 0.1 ✗ ✓ ✗ N/A LiLT [ 58 ] T+L 1.00E-05 32 50 Adam 0.01 N/A 0.1 0.1 ✗ ✓ ✗ N/A CLS LayoutLMv3 [ 28 ] T+L+I 1.00E-05 32 50 Adam 0.01 N/A 0.1 0.1 ✓ ✓ ✗ 224×224 BERT [ 13 ] T 2.00E-05 16 100 AdamW 0.01 N/A 0.1 0.1 ✗ ✗ ✗ N/A LiLT [ 58 ] T+L 2.00E-05 16 100 AdamW 0.01 N/A 0.1 0.1 ✗ ✗ ✗ N/A KIE LayoutLMv3 [ 28 ] T+L+I 2.00E-05 16 100 AdamW 0.01 N/A 0.1 0.1 ✓ ✗ ✗ 224×224 BERT [ 13 ] T 5.00E-05 32 50 Adam 0.01 N/A 0.02 0.1 ✗ ✓ ✗ N/A LiLT [ 58 ] T+L 5.00E-05 32 50 Adam 0.01 N/A 0.02 0.1 ✗ ✓ ✗ N/A VQA LayoutLMv3 [ 28 ] T+L+I 5.00E-05 16 50 Adam 0.01 N/A 0.02 0.1 ✓ ✓ ✗ 224×224 Faster R-CNN [ 49 ] I 2.00E-02 16 40 SGD 0.0001 0.9 0.05 0.1 ✗ ✓ ✓ 480–800×1333 * DLA Cascade R-CNN [ 9 ] I 2.00E-02 16 40 SGD 0.0001 0.9 0.05 0.1 ✗ ✓ ✓ 480–800×1333 * Table 11 : Default training hyperparameters for all models and tasks in our experiments. For each task (CLS, KIE, VQA, DLA) and model combination, we report learning rate, batch size, number of epochs, optimizer settings, and other training parameters. These settings were chosen based on preliminary experiments and common practices for document understanding tasks.

[189] h2: Appendix 0.M Data & Code Availability

[190] p: Complete source code is provided in this supplementary material, including the VLM-based synthesis pipeline, clustering and sampling procedures, model training scripts, and evaluation tools. Due to size constraints, we include representative samples of the synthetic datasets and the complete DocVQA-HW subset in the supplementary material. The full synthetic datasets (140K+ samples across eleven benchmarks) will be released upon publication. All real-world benchmark datasets are publicly available from their original sources as cited in the paper.

[191] h2: Instructions for reporting errors

[192] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[193] p: Tip: You can select the relevant text first, to include it in your report.

[194] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[195] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
