[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Where Vision Becomes Text: Locating the OCR Routing Bottleneck in Vision-Language Models

[3] h6: Abstract

[4] p: Vision-language models (VLMs) can read text from images, but where does this optical character recognition (OCR) information enter the language processing stream? We investigate the OCR routing mechanism across three architecture families (Qwen3-VL, Phi-4, InternVL3.5) using causal interventions. By computing activation differences between original images and text-inpainted versions, we identify architecture-specific OCR bottlenecks whose dominant location depends on the vision-language integration strategy: DeepStack models (Qwen) show peak sensitivity at mid-depth ( ∼ \sim 50%) for scene text, while single-stage projection models (Phi-4, InternVL) peak at early layers (6–25%), though the exact layer of maximum effect varies across datasets. The OCR signal is remarkably low-dimensional: PC1 captures 72.9% of variance. Crucially, Principal Component Analysis (PCA) directions learned on one dataset transfer to others, demonstrating shared text-processing pathways. Surprisingly, in models with modular OCR circuits (notably Qwen3-VL-4B), OCR removal can improve counting performance (up to +6.9pp), suggesting OCR interferes with other visual processing in sufficiently modular architectures.

[5] h2: 1 Introduction

[6] p: Vision-language models (VLMs) have become increasingly capable at reading text from images, enabling applications from document understanding to visual question answering. This optical character recognition (OCR) capability emerges from training on web-scale data, but the internal mechanisms remain poorly understood.

[7] p: Understanding where OCR information enters the language processing stream is crucial for interpretability. Unlike explicit text inputs, OCR-derived text must be extracted from visual representations and routed into the residual stream where it can influence generation. Localizing this routing mechanism enables targeted interventions for understanding and controlling OCR-based processing.

[8] figure: Figure 1: Causal intervention on the VLM residual stream. By identifying the OCR direction via PCA on activation deltas (left) and projecting it out at the bottleneck (center), OCR capability is effectively suppressed while spatial reasoning and counting tasks are functionally separated and preserved (right).

[9] p: In this work, we investigate the OCR routing bottleneck across three VLM architecture families using PCA-based causal interventions. Our contributions are:

[10] p: We identify architecture-specific layer bottlenecks where OCR becomes causally usable, replicated across five models from three architecture families (Qwen3-VL, Phi-4, InternVL3.5-4B), with bottleneck location determined by the vision-language integration strategy.

[11] p: We show the OCR signal is remarkably low-dimensional : PC1 explains 73% of variance, enabling efficient subspace removal.

[12] p: We demonstrate cross-dataset transfer : PCA directions learned on EgoTextVQA transfer to OCRBench and InfoVQA, indicating shared text-processing pathways.

[13] p: We discover a synergistic improvement in Qwen3-VL-4B: the L17–19_pc5 intervention improves counting (+4.3pp) and general VQA (+1pp) simultaneously with only mild spatial degradation ( − - 2pp); the peak counting gain reaches +6.9pp (L16–20_pc3), suggesting OCR interferes with visual processing in models with modular circuits.

[14] h2: 2 Related Work

[15] h4: Vision-Language Model Architectures.

[16] p: Modern VLMs integrate visual and textual information through various fusion strategies. Early approaches like Flamingo ( Alayrac et al., 2022 ) used cross-attention layers to inject visual features into frozen language models. LLaVA ( Liu et al., 2024 ) introduced visual instruction tuning with a simpler projection-based integration. Qwen3-VL ( Bai et al., 2025 ) employs the DeepStack architecture, which leverages multi-level ViT features for tighter vision-language alignment across transformer depth. This architectural diversity motivates layer-wise analysis: different integration strategies may route OCR information through different computational pathways.

[17] h4: Mechanistic Interpretability of VLMs.

[18] p: Recent work has begun applying interpretability techniques to vision-language models. Baek et al. (2025) identified “OCR heads”—specific attention heads responsible for text recognition—through activation analysis and head masking experiments. They found OCR heads are qualitatively distinct from general retrieval heads, with less sparse activation patterns. Sheta et al. (2025) introduced VLM-Lens, a probing framework for diagnosing internal competences of VLMs across visual, linguistic, and cross-modal dimensions. Skean et al. (2025) systematically analyzed layer-wise representations across language models, revealing how information transforms through depth. Our work complements these by taking a causal representation-level approach: rather than identifying which heads do OCR or probing what representations encode, we characterize what information flows through the network and whether it can be selectively removed.

[19] h4: Activation Patching and Causal Tracing.

[20] p: Activation patching ( Meng et al., 2022 ) has proven effective for localizing specific computations in language models. The core insight is that restoring “clean” activations to a corrupted forward pass reveals which components are causally necessary for a behavior. We adapt this approach for multimodal settings by using inpainted images (with text removed) as the “corrupted” condition, enabling us to isolate OCR-specific activations. Related techniques include causal scrubbing ( Chan et al., 2022 ) and path patching, though we focus on subspace-level rather than component-level interventions.

[21] h4: Representation Engineering and Steering Vectors.

[22] p: Zou et al. (2023) demonstrated that model behavior can be controlled by intervening on learned directions in activation space. This “representation engineering” paradigm has been applied to control sentiment, truthfulness, and safety-relevant behaviors. Steering vectors ( Turner et al., 2023 ) provide similar control through additive interventions. We apply these techniques to identify and remove OCR-related directions, testing whether low-dimensional subspace removal provides causal control over text reading without collateral damage to other capabilities.

[23] h4: Superposition and Feature Geometry.

[24] p: Elhage et al. (2022) introduced the concept of superposition—where neural networks represent more features than they have dimensions by encoding features in nearly-orthogonal directions. Our finding that OCR-related activation differences concentrate in a low-dimensional subspace (PC1 explains 73% of variance in original − - inpainted deltas) is consistent with OCR being relatively separable from other features, though we note this measures variance in deltas rather than providing direct evidence about the degree of superposition. This connects to broader questions about how multimodal information is geometrically organized in shared representation spaces.

[25] h2: 3 Methods

[26] h3: 3.1 Dataset: EgoTextVQA

[27] p: We use EgoTextVQA ( Zhou and Guo, 2024 ) , an egocentric dataset where images contain naturally-occurring text (signs, labels, screens).

[28] p: For each image, we create an inpainted version with the text region removed (Figure 2 ). The pair (original, inpainted) enables computing what changes in activations when text is present versus absent.

[29] figure: Figure 2: Example original-inpainted pairs from EgoTextVQA. Left: original images with naturally-occurring text. Right: inpainted versions with text regions removed. Activation differences between pairs capture the “OCR signal.”

[30] h3: 3.2 Models

[31] p: We study five VLMs spanning three architectural families to examine how vision-language integration affects OCR routing:

[32] p: DeepStack models : Qwen3-VL-4B-Instruct, Qwen3-VL-2B-Instruct, and Qwen3-VL-8B-Instruct ( Bai et al., 2025 ) (36/28/36 layers) progressively inject visual features into multiple LLM layers.

[33] p: Single-stage models : Phi-4-multimodal-instruct ( Microsoft, 2025 ) (32 layers) and InternVL3.5-4B ( Wang et al., 2025 ) (36 layers) inject all visual tokens at the input layer.

[34] p: This architectural variation reveals how integration strategy affects OCR bottleneck location and modularity.

[35] h3: 3.3 Cross-Dataset Benchmarks

[36] p: To validate generalization beyond EgoTextVQA, we evaluate on two additional OCR benchmarks:

[37] p: OCRBench ( Liu et al., 2023 ) : Comprehensive OCR covering regular, irregular, and artistic text.

[38] p: InfoVQA ( Mathew et al., 2022 ) : Document understanding with infographics and complex layouts.

[39] h3: 3.4 PCA-Based Subspace Removal

[40] p: For each layer ℓ \ell , we compute activation differences:

[41] table: Δ ​ h ℓ = h ℓ original − h ℓ inpainted \Delta h_{\ell}=h_{\ell}^{\text{original}}-h_{\ell}^{\text{inpainted}} (1)

[42] p: across a held-out training split. We split EgoTextVQA into 315 images for PCA training and a disjoint set for evaluation, ensuring no train-test leakage. PCA on the training-set differences yields principal components capturing “what changes when text is present.”

[43] p: During inference, we intervene by projecting out the top N N components:

[44] table: h ℓ int = h ℓ − α ​ ∑ i = 1 N ( h ℓ ⋅ pc i ) ​ pc i h_{\ell}^{\text{int}}=h_{\ell}-\alpha\sum_{i=1}^{N}(h_{\ell}\cdot\text{pc}_{i})\,\text{pc}_{i} (2)

[45] p: where h ℓ h_{\ell} is the residual-stream activation at layer ℓ \ell , pc i \text{pc}_{i} is the i i -th principal component, N N is the number of components removed, and α \alpha controls intervention strength. We fix α = 1 \alpha{=}1 throughout (full projection removal). If OCR flows through this subspace, removal should disrupt text reading. We use the shorthand pca_L ℓ \ell - ℓ ′ \ell^{\prime} _pc N N to denote projection of the top N N components across layers ℓ \ell to ℓ ′ \ell^{\prime} .

[46] h4: Intervention Specification.

[47] p: We apply interventions via forward hooks on transformer layer outputs (post-MLP residual stream). Hooks affect all tokens (visual and text) during both prefill and decode. PCA directions are unit-normalized before projection.

[48] h3: 3.5 Head Ablation

[49] p: As a complementary approach, we compute a selectivity ratio for each attention head: the ratio of attention to OCR regions versus background regions. Heads with ratio > 1.0 >1.0 preferentially attend to text. We rank all 720 heads (36 layers × \times 20 heads) by selectivity and ablate the top N N by zeroing their output projections during both prefill and decode, testing whether attention-identified heads are causally important.

[50] h3: 3.6 Evaluation

[51] p: We measure OCR accuracy using normalized substring matching (case-insensitive, punctuation-stripped), a standard evaluation metric for OCR benchmarks that counts predictions as correct if ground truth appears within the model output or vice versa. 1 1 1 VLM judge verification on a subset achieved 97% agreement with this automatic metric. To assess collateral damage, we evaluate interventions on CountBench ( Paiss et al., 2023 ) (object counting), EmbSpatial ( Du et al., 2024 ) (spatial reasoning), and RealWorldQA ( xAI, 2024 ) (general visual QA) across all five models. If OCR removal hurts these tasks, the intervention is too aggressive; if it helps, OCR was interfering with visual processing. All evaluations use complete datasets (not samples) with deterministic greedy decoding, so we report single-run results without error bars.

[52] h2: 4 Experiments and Results

[53] h3: 4.1 Layerwise Bottleneck Discovery

[54] p: Figure 3 shows OCR accuracy across layers and intervention strengths for all five models. A clear pattern emerges across architecture families: DeepStack models (Qwen) show mid-layer bottlenecks , while single-stage models (Phi-4, InternVL) show early-layer bottlenecks . The bottleneck at ∼ \sim 50% network depth in Qwen aligns with prior findings that OCR heads concentrate at 50–60% depth ( Baek et al., 2025 ) .

[55] h3: 4.2 Low-Dimensional OCR Signal

[56] p: The first principal component at L17 explains 72.9% of OCR-related variance. Removing PC1–PC3 achieves strong OCR suppression with fewer components than single-direction removal, confirming the signal is concentrated in a small subspace.

[57] h3: 4.3 Cross-Architecture Retention Analysis

[58] p: We evaluated retention across three diverse benchmarks (see Section 3.6): CountBench ( Paiss et al., 2023 ) (object counting), EmbSpatial ( Du et al., 2024 ) (spatial reasoning), and RealWorldQA ( xAI, 2024 ) (general visual QA). Table 1 reveals a striking architectural divergence.

[59] p: Qwen3-VL-4B achieves a favorable trade-off. Interventions at the mid-depth bottleneck (L17–19) significantly improve counting (+4.3pp) and RealWorldQA (+1pp) with only minimal impact on spatial reasoning ( − - 2pp). This suggests the model has developed modular circuits where OCR can be targeted and removed, freeing capacity for other visual tasks.

[60] p: Smaller and Single-Stage Models show Trade-offs. Qwen3-VL-2B and Phi-4 show large gains in counting (+5.6pp, +4.3pp) but at the cost of spatial reasoning and general VQA. This implies a “competition” for resources where removing OCR helps counting but hurts complex reasoning.

[61] p: InternVL shows complete degradation. Unlike other models, InternVL’s early-layer bottleneck (L2–L3) degrades all metrics when intervened. This reveals a critical architectural constraint: single-stage projection forces tight coupling between OCR and general vision at early layers.

[62] p: Qwen3-VL-8B replicates the 4B pattern. The 8B model shows a similar bottleneck at L17 with CountBench improvement (+2.9pp) and mild EmbSpatial degradation ( − - 3pp). RealWorldQA shows a larger drop ( − - 14pp).

[63] p: Table 2 provides the complete Qwen3-VL-4B intervention analysis. The L17-19_pc5 intervention improves CountBench (+4.3pp) and RealWorldQA (+1pp) simultaneously with only mild EmbSpatial degradation ( − - 2pp). L18_pc5 causes RWQ collapse ( − - 13pp) while L17/L19 preserve it.

[64] figure: Model Intervention Count Emb RWQ Qwen3-VL-4B baseline 91.4 81.5 75.0 L17-19_pc5 95.7 79.5 76.0 Qwen3-VL-8B baseline 90.2 82.0 72.0 L17-19_pc5 93.1 79.0 58.0 Qwen3-VL-2B baseline 90.3 78.0 66.0 L12_pc5 95.9 72.0 60.0 Phi-4 baseline 89.2 62.2 66.0 L8_pc3 93.5 49.0 53.5 InternVL baseline 78.9 69.2 64.0 L2_pc1 69.2 25.0 42.0 Table 1: Cross-model retention results (%). Count=CountBench (counting), Emb=EmbSpatial (spatial), RWQ=RealWorldQA. Bold=improvement. Qwen3-VL-4B achieves favorable trade-off; smaller/single-stage models show trade-offs or degradation. Qwen3-VL-8B replicates the 4B pattern at L17.

[65] figure: Intervention Count Emb RWQ Note baseline 91.4 81.5 75.0 — Single layer: pca_L16_pc5 94.1 81.0 71.0 Count ↑ \uparrow , RWQ ↓ \downarrow pca_L17_pc1 90.3 80.5 73.0 Minimal pca_L17_pc3 94.1 78.5 73.0 Trade-off pca_L17_pc5 96.2 78.5 74.0 Good pca_L18_pc5 91.9 81.5 62.0 RWQ collapse pca_L19_pc5 96.2 80.5 72.0 Count ↑ \uparrow pca_L20_pc5 91.4 79.5 69.0 Trade-off Multi-layer: pca_L16-20_pc1 89.7 81.0 65.0 RWQ ↓ \downarrow pca_L16-20_pc3 98.3 80.5 73.0 Best Count pca_L17-19_pc3 94.1 78.5 73.0 Good pca_L17-19_pc5 95.7 79.5 76.0 Best pca_L17-20_pc3 93.5 79.5 74.0 Good Table 2: Complete Qwen3-VL-4B retention results (%). L17-19_pc5 achieves the best trade-off: Count +4.3pp, RWQ +1pp, with mild EmbSpatial degradation ( − - 2pp). L18_pc5 causes RWQ collapse ( − - 13pp) while L17/L19 preserve it.

[66] h3: 4.4 Head Ablation Analysis

[67] p: As a complementary analysis, we ablated the 93 most OCR-selective attention heads (clustered in L17–24, identified by selectivity ratio > 1.0 >1.0 ). This reduces OCR by 8.2pp while improving CountBench by 5.0pp—directionally consistent with our PCA findings. As a control, ablating 93 randomly-selected heads (mean over 10 draws) degrades CountBench by 6.8 ± \pm 2.1pp without substantially affecting OCR ( − - 2.1 ± \pm 1.5pp). Head ablation is a noisier intervention than subspace removal, but provides supporting evidence that OCR-relevant computation concentrates in the same mid-network band identified by PCA. The OCR-selective ablation is an outlier relative to random ablations: it degrades OCR while improving counting, consistent with our interference hypothesis.

[68] h3: 4.5 Cross-Dataset Transfer Results

[69] p: Table 3 shows maximum accuracy degradation when applying EgoTextVQA-trained PCA directions to OCRBench and InfoVQA. Critically, the PCA directions learned on one dataset effectively suppress OCR on others—demonstrating that the underlying OCR representations are shared across text domains. Note that these results test method transferability (whether EgoTextVQA-learned directions suppress OCR on new datasets), not bottleneck transferability (whether the max-sensitivity layer is identical). The max-sensitivity layer may shift across datasets (e.g., Qwen3-VL-4B peaks at L18 for EgoTextVQA vs L30 for OCRBench) because different text types (scene text vs. document layout) may emphasize different decoding stages. Crucially, the learned directions transfer even when the optimal intervention layer differs—Figure 4 shows that direction effectiveness generalizes across layers, not just at the single maximum reported in Table 3 .

[70] p: For Phi-4, InfoVQA reveals the L8–L10 bottleneck clearly: L10 drops to 54% ( − - 18pp from baseline 72%), while control layers (L20, L28) maintain baseline performance. This confirms that the learned intervention method generalizes across datasets.

[71] figure: EgoTextVQA OCRBench InfoVQA Model Drop Layer Drop Layer Drop Layer Qwen3-VL-4B − - 69.6 L18 (50%) − - 30.8 L30 (83%) − - 22.0 L4 (11%) Qwen3-VL-2B − - 62.4 L26 (93%) − - 20.0 L26 (93%) − - 72.0 L26 (93%) Phi-4 − - 44.3 L8 (25%) − - 4.0 L1 (3%) − - 18.0 L10 (31%) InternVL − - 75.3 L2 (6%) − - 69.0 L2 (6%) − - 29.0 L17 (49%) Table 3: Cross-dataset generalization. Maximum accuracy drop (pp) when applying EgoTextVQA-trained PCA directions. Note: PCA directions transfer across datasets (all models show substantial OCR suppression), but max-sensitivity layer may shift due to dataset-specific text characteristics.

[72] figure: Figure 3: Small multiples view: unnormalized (absolute layer) comparison across all models. Each panel shows baseline (dashed) vs intervention (solid) accuracy curves using absolute layer numbers. Qwen models show bottlenecks at higher layers (L16–L20, L12) while Phi-4 and InternVL show earlier bottlenecks (L3–L9, L2–L3), reflecting architectural differences in vision-language integration timing.

[73] figure: Figure 4: Cross-dataset generalization of OCR suppression. Each panel shows one model’s accuracy delta across layers for all three datasets. PCA directions learned on EgoTextVQA (green) transfer effectively to OCRBench (blue) and InfoVQA (red), demonstrating that learned OCR representations generalize beyond the training distribution.

[74] h2: 5 Discussion

[75] h4: Discrete vs. Gradual Processing.

[76] p: Our layer-by-layer analysis reveals concentrated sensitivity at specific depth ranges rather than uniform processing across the network. In Qwen3-VL-4B, the L16–L20 region shows substantially higher OCR sensitivity than surrounding layers (Figure 3 ), consistent with the “OCR heads” concentration at 50–60% depth reported by Baek et al. (2025) . However, we note this pattern varies by architecture: Qwen3-VL-2B shows more distributed sensitivity, suggesting that the degree of localization may depend on model capacity and architecture rather than being a universal property.

[77] h4: Interference Effects.

[78] p: The improvement in CountBench under OCR removal was unexpected. We hypothesize that the OCR pathway competes for representational capacity in the residual stream, and removing it allows other visual features to be processed more cleanly. This “interference” interpretation is supported by the layer-specificity of the effect: interventions at L16 (+4.8pp) and multi-layer L16–20 (up to +6.9pp) improve counting, but layer sensitivity varies for other tasks. Notably, L18 interventions cause RWQ collapse ( − - 13pp) while L17 and L19 preserve it (Table 2 ), suggesting L18 encodes representations shared between OCR and general visual reasoning.

[79] h4: Cross-Model Scaling.

[80] p: Comparison across the Qwen3-VL family reveals that larger models develop more localized OCR routing. The 2B model shows distributed sensitivity spanning L8–15 with a secondary late peak at L25–26, while the 4B model concentrates OCR processing into a 4–5 layer bottleneck at L16–L20. We hypothesize that this architectural consolidation could make targeted intervention easier as models scale—a counterintuitive but potentially important finding for interpretability research, though validation across more model sizes is needed. We speculate that larger models develop more specialized circuits with cleaner separation between capabilities, but this remains to be confirmed.

[81] p: A same-family replication on Qwen3-VL-8B (36 layers, hidden dimension 4096 vs. 2560 in the 4B) confirms the bottleneck is conserved at L17 ( ∼ \sim 47% depth) despite 1.6 × \times wider hidden dimension, with a floor of 42.3% OCR accuracy under PC1–5 removal (vs. ∼ \sim 20% in the 4B). The shallower trough in the 8B may reflect greater representational redundancy in the wider residual stream. This depth-indexed conservation within an architecture family suggests that bottleneck location is an architectural property rather than a capacity-dependent one, though we note this evidence is limited to same-family scaling and may not generalize to cross-architecture comparisons. See Appendix C.4 for full 8B results.

[82] h4: Architectural Determinants of Bottleneck Location.

[83] p: Our cross-architecture analysis reveals two distinct OCR routing profiles: “Early” (InternVL, Phi-4) and “Mid-Depth” (Qwen3-VL). We hypothesize this divergence stems from the vision-language integration strategy. Qwen3-VL employs the DeepStack architecture ( Bai et al., 2025 ) , a multi-scale visual feature injection strategy where features from different ViT depths (blocks 8, 16, 24) are progressively injected into early LLM layers (0, 1, 2). This “staged injection” allows the model to defer OCR routing until mid-network (L16–20, ∼ \sim 50% depth), as early layers are occupied integrating multi-scale visual representations. In contrast, Phi-4 and InternVL use single-stage projection: all visual features are injected at Layer 0, forcing immediate resolution of OCR routing in early layers (L2–9, 6–25% depth). Table 5 summarizes these findings. This suggests that bottleneck location is not a universal constant but an architectural property —our method successfully identifies the architecture-specific locus regardless of where it occurs.

[84] h4: Coupled Representations in Early Fusion.

[85] p: InternVL3.5 exhibits a unique failure mode: interventions at its early-layer bottleneck (L2–L3) degrade all metrics (Table 1 ). Unlike Qwen, where OCR is separable, InternVL’s single-stage architecture forces immediate processing of raw visual tokens. At this shallow depth ( ∼ \sim 6% of network), OCR representations appear tightly coupled with general visual features. Removing OCR directions thus causally impairs the model’s fundamental ability to see, preventing the “capacity release” benefits observed in DeepStack models. This suggests that while early fusion architectures are efficient, they may trade off interpretability and modularity.

[86] p: Table 4 provides detailed evidence: interventions at InternVL’s true bottleneck (L2–L3) cause both high OCR drop and retention collapse, while interventions at Qwen-equivalent layers (L17–L20) have minimal retention effect even with moderate OCR drops. This stark contrast validates our bottleneck localization methodology—interventions only impact retention when applied to the model’s actual OCR routing layers.

[87] figure: Intervention OCR Drop Count Emb RWQ baseline — 78.9 69.2 64.0 Bottleneck: pca_L2_pc1 68.0pp 69.2 25.0 42.0 pca_L2_pc5 54.6pp 29.2 4.0 6.0 pca_L3_pc5 23.2pp 77.8 47.0 49.0 pca_L2-3_pc1 76.8pp 69.2 15.0 40.0 Control: pca_L20_pc5 20.6pp 79.5 65.5 66.0 pca_L17-24_pc3 29.9pp 82.2 53.5 65.0 pca_L19-22_pc5 73.2pp 78.4 65.5 65.0 Table 4: InternVL retention results (%). Bottleneck interventions (L2–L3) cause OCR drop and retention collapse. Control interventions (L17–L20) have minimal effect.

[88] h4: DeepStack Injection Signature in Qwen Models.

[89] p: Interestingly, Qwen3-VL-4B shows a secondary sensitivity peak at Layer 2 (Figure 3 ), precisely where DeepStack injects its final visual features (ViT block 24 → \rightarrow LLM Layer 2). This “injection signature” confirms that OCR information enters through the visual pathway and is initially processed at the injection site, but the dominant bottleneck emerges later at L16–L20 where cross-modal routing is finalized. The 4B model’s concentrated bottleneck at mid-depth suggests it develops modular circuits that cleanly separate visual injection from OCR routing.

[90] p: In contrast, Qwen3-VL-2B exhibits a more distributed sensitivity pattern spanning L8–15 with a secondary late peak at L25–26. The most effective multi-layer intervention targets L13–15 (Table 9 ), consistent with this broad sensitivity region. We attribute this distributed pattern to capacity constraints: the smaller model reuses circuits across the injection layers (L0–2), spreading OCR sensitivity more broadly through the early-to-mid network. The late peak at L25–26 ( ∼ \sim 90% depth) likely reflects a “retention/formatting” pass where the model prepares decoded text for output—a pattern absent in the larger 4B model, which completes OCR routing by L20. This scaling behavior suggests that OCR circuit modularity increases with model capacity , with larger models developing cleaner separation between visual integration and text routing.

[91] figure: Figure 5: OCR bottleneck location by architecture and dataset. Each panel shows mean accuracy delta across three network depth stages (Early 0–33%, Mid 33–66%, Late 66–100%) for one dataset. EgoTextVQA and OCRBench show consistent patterns: InternVL3.5-4B and Phi-4 peak at early layers, while Qwen models show mid-depth bottlenecks.

[92] figure: Model Integration Bottleneck Qwen3-VL-4B DeepStack L16–L20 Qwen3-VL-2B DeepStack L8–10, L25–26 Phi-4 Single-stage L3–L9 InternVL3.5-4B Single-stage L2–L3 Table 5: Cross-architecture OCR bottleneck analysis. DeepStack models (Qwen) show mid-depth bottlenecks; single-stage projection models (Phi-4, InternVL) show early bottlenecks.

[93] h4: Implications for Interpretability.

[94] p: Our low-dimensional finding (PC1 explains 72.9% of OCR variance) suggests that multimodal capabilities may organize into relatively separable subspaces, at least for well-defined tasks like text recognition. This has methodological implications: if modality-specific computations concentrate in low-dimensional subspaces, they may be more amenable to steering vector approaches than previously thought. The success of our targeted interventions—removing OCR with minimal collateral damage—demonstrates that PCA-based methods can achieve meaningful behavioral control in VLMs. For safety evaluation, bottleneck localization enables controlled ablation of text-reading pathways, which is relevant for assessing vulnerability to typographic prompt injection and for auditing how strongly image-embedded text influences model behavior.

[95] h4: Future Directions.

[96] p: Our analysis covers dense-attention architectures with two integration strategies (DeepStack and single-stage projection). Extending this framework to Mixture-of-Experts (MoE) architectures, where OCR routing may involve expert selection rather than subspace routing, and to OCR-specialized models (e.g., DeepSeek-OCR ( DeepSeek AI, 2025 ) ) that may develop qualitatively different text-processing circuits, would test the generality of the bottleneck hypothesis. Additionally, the 8B replication’s higher OCR floor (42.3% vs. ∼ \sim 20% in the 4B) suggests that wider residual streams may encode OCR redundantly, motivating investigation of how representational redundancy scales with model width.

[97] h2: Limitations

[98] p: Architectural coverage. We validated our method across five models from three architecture families (Qwen3-VL-4B/2B/8B, Phi-4, InternVL3.5-4B). The same-family 8B replication strengthens within-family claims, but all tested models use dense attention. Mixture-of-Experts (MoE) architectures and OCR-specialized models (e.g., DeepSeek-OCR ( DeepSeek AI, 2025 ) ) may exhibit qualitatively different routing patterns. The method may require adaptation for architectures with different vision-language fusion strategies.

[99] p: Reliance on inpainting quality. Our activation difference method depends on artifact-free text removal to isolate OCR signals. While effective for sparse scene text (EgoTextVQA), this approach is less reliable for dense document images where current inpainting models struggle to preserve complex layouts without introducing artifacts. Future work could explore synthetic text overlays or feature-level masking to extend this analysis to document understanding.

[100] p: Limited retention coverage. We measured retention on CountBench, EmbSpatial, and RealWorldQA. OCR removal might harm tasks we did not test (e.g., structured document QA, chart reading). The 8B model shows a larger RealWorldQA drop ( − - 14pp) than the 4B ( + + 1pp) under the same intervention, possibly reflecting greater load-bearing of the L17–19 subspace for reasoning at wider hidden dimension.

[101] h2: Ethics Statement

[102] p: This work investigates the internal mechanisms of OCR processing in vision-language models to advance interpretability research. Our methodology and analysis tools will be made publicly available to support the research community.

[103] h2: Acknowledgments

[104] p: This material is based upon work supported by the Google Cloud Research Credits program (Grant ID: 462107767).

[105] h2: Appendix A Extended Experimental Setup

[106] h3: A.1 Models

[107] p: We study five VLMs from three architecture families ( Bai et al., 2025 ; Microsoft, 2025 ; Wang et al., 2025 ) .

[108] h4: DeepStack Architecture.

[109] p: Qwen3-VL-4B-Instruct ( Bai et al., 2025 ) : 36 layers, 20 attention heads, 2560 hidden dimension. Employs multi-scale visual feature injection across early LLM layers.

[110] p: Qwen3-VL-2B-Instruct ( Bai et al., 2025 ) : 28 layers, 20 attention heads, 2048 hidden dimension. Same DeepStack architecture as the 4B variant.

[111] p: Qwen3-VL-8B-Instruct ( Bai et al., 2025 ) : 36 layers, 32 attention heads, 4096 hidden dimension. Same layer count as 4B but 1.6 × \times wider hidden dimension and 1.6 × \times more attention heads.

[112] h4: Single-Stage Projection.

[113] p: Phi-4-multimodal-instruct ( Microsoft, 2025 ) : 32 layers. Projects all visual tokens to the input layer via a single MLP projection.

[114] p: InternVL3.5-4B ( Wang et al., 2025 ) : 36 layers. Single-stage projection with immediate visual token fusion at layer 0.

[115] h3: A.2 Compute Requirements

[116] p: All experiments were run on 4 × \times NVIDIA RTX 6000 Pro (Blackwell) workstation GPUs. Single-image inference requires approximately 12 GB VRAM. Full activation extraction for all 36 layers requires ∼ \sim 24 GB. PCA training on 315 training images completes in approximately 15 minutes per model.

[117] h3: A.3 Retention Benchmarks

[118] p: For retention evaluation, we use three benchmarks that require visual processing but not OCR, making them ideal for measuring collateral damage from OCR interventions:

[119] p: CountBench ( Paiss et al., 2023 ) : Object counting benchmark measuring ability to enumerate objects in images.

[120] p: EmbSpatial ( Du et al., 2024 ) : Spatial understanding benchmark for embodied tasks, testing spatial reasoning capabilities.

[121] p: RealWorldQA ( xAI, 2024 ) : General visual question answering on real-world images, released by xAI.

[122] p: All evaluations use complete datasets with deterministic greedy decoding.

[123] h3: A.4 Inpainting Methodology

[124] p: For each EgoTextVQA image, we create a paired “inpainted” version with the text region removed. We extract text region bounding boxes from annotations, expand by 10% to ensure complete removal, apply a standard inpainting model to fill the masked region, and verify quality via manual spot-check of 50 random samples. Figure 2 shows example pairs.

[125] h3: A.5 Inpainting Artifact Controls

[126] p: To verify that our observed effects stem from OCR signal removal rather than inpainting artifacts, we conducted control experiments with three inpainting methods and a random-box baseline.

[127] figure: Method PCA Var. OCR Drop LaMa (default) 72.9% − - 69.6pp SDXL Inpaint 71.2% − - 67.8pp Simple blur 68.4% − - 64.2pp Random boxes 12.3% − - 0.1pp Table 6: Inpainting artifact controls. Three inpainting methods (LaMa, SDXL, blur) yield similar PCA variance explained and OCR suppression. Random boxes (masking non-text regions) show minimal effect, confirming our signal is OCR-specific.

[128] p: All three inpainting methods produce similar PC1 variance (68–73%) and intervention effectiveness ( − - 64 to − - 70pp OCR drop), indicating our findings are robust to inpainting implementation. The random-box control—applying inpainting to non-text regions matched for box count, area distribution, and aspect ratios per image—captures only 12.3% variance and produces negligible OCR drop ( − - 0.1pp), confirming that the learned directions are specific to text removal rather than general image perturbation.

[129] h2: Appendix B Complete Results Tables

[130] h3: B.1 All PCA Intervention Results

[131] p: Table 7 presents complete results for all 14 PCA experiments tested.

[132] figure: Experiment Layers Comp. OCR Drop Count Base Count Δ \Delta Outcome pca_L16-20_pc3 L16–20 3 76.3pp 91.4% +6.9pp Ideal pca_L17_pc5 L17 5 53.6pp 91.4% +5.3pp Good pca_L16_pc5 L16 5 13.4pp 91.4% +4.8pp Good pca_L17-19_pc5 L17–19 5 56.2pp 91.4% +4.3pp Best pca_L20_pc5 L20 5 29.9pp 91.4% +3.9pp Good pca_L17-19_pc3 L17–19 3 58.2pp 91.4% +2.9pp Good pca_L18_pc5 L18 5 72.7pp 91.4% +0.5pp Neutral pca_L19_pc5 L19 5 27.3pp 91.4% +0.2pp Neutral pca_L17_pc3 L17 3 41.2pp 91.4% − - 0.4pp Neutral pca_L16-20_pc1 L16–20 1 86.1pp 91.4% − - 2.2pp Harmful pca_L17_pc1 L17 1 32.0pp 91.4% − - 2.8pp Harmful pca_L17-20_pc3 L17–20 3 53.1pp 91.4% − - 3.5pp Harmful pca_L17_pc10 L17 10 54.6pp 91.4% − - 8.5pp Harmful pca_L17-20_pc5 L17–20 5 64.9pp 91.4% − - 18.5pp Harmful Table 7: Complete PCA intervention results sorted by Count Δ \Delta . Multi-layer interventions that avoid L17 alone achieve the best trade-offs.

[133] h3: B.2 Top OCR-Selective Attention Heads

[134] p: Table 8 lists the 20 most OCR-selective attention heads by selectivity ratio.

[135] figure: Rank Layer Head Selectivity Ratio Power 1 16 4 1.41 0.55e-3 2 18 15 1.40 0.85e-3 3 8 8 1.40 0.26e-3 4 12 1 1.34 0.33e-3 5 17 13 1.27 0.68e-3 6 16 12 1.25 0.48e-3 7 18 7 1.24 0.72e-3 8 17 8 1.22 0.61e-3 9 16 19 1.21 0.44e-3 10 12 14 1.20 0.30e-3 11 18 2 1.19 0.69e-3 12 17 0 1.18 0.58e-3 13 16 7 1.17 0.42e-3 14 19 11 1.16 0.55e-3 15 12 9 1.15 0.28e-3 16 18 19 1.14 0.66e-3 17 17 15 1.13 0.54e-3 18 20 3 1.12 0.49e-3 19 16 0 1.11 0.39e-3 20 19 6 1.10 0.52e-3 Table 8: Top 20 OCR-selective attention heads. Selectivity ratio = OCR attention / background attention. Heads concentrate in L12, L16–L20.

[136] h3: B.3 Cross-Dataset Generalization Details

[137] p: See Section 4.5 for complete cross-dataset generalization analysis including OCRBench and InfoVQA results with layer-by-layer breakdown.

[138] h2: Appendix C Complete Retention Evaluation Results

[139] p: This section provides complete retention evaluation results for all interventions tested on each model. Results use normalized substring matching. Count=CountBench (counting), Emb=EmbSpatial (spatial reasoning), RWQ=RealWorldQA (general visual QA).

[140] h3: C.1 InternVL3.5-4B Results

[141] p: InternVL3.5-4B’s OCR bottleneck is at L2–L3 ( ∼ \sim 6–9% depth). Interventions at the correct bottleneck layers show trade-offs, while interventions at Qwen-equivalent layers (L17–L20) have minimal effect (confirming they are not InternVL’s bottleneck).

[142] p: Key Insight. The stark contrast between L2–L3 interventions (trade-offs/collapse) and L17–L20 interventions (no effect) validates our bottleneck localization methodology: interventions only impact retention when applied to the model’s actual OCR routing layers.

[143] h3: C.2 Qwen3-VL-2B Results

[144] p: Qwen3-VL-2B-Instruct has a distributed OCR bottleneck spanning L8–15 with a secondary late peak at L25–26. Table 9 shows key interventions around the mid-network region (L12–L16). Baseline OCR accuracy: 87.1%.

[145] figure: Interv. OCR Cnt Emb RWQ baseline — 90.3 78 66 L12_pc5 31.4 95.9 72 60 L13_pc5 41.2 86.7 75 68 L14_pc5 34.5 92.3 77 56 L15_pc5 42.3 61.0 74 62 L12-16_pc3 23.2 91.3 71 68 L13-15_pc5 74.4 75 56 — Table 9: Qwen3-VL-2B retention (%). L12_pc5: +5.6pp Count.

[146] p: Key Insight. L12_pc5 achieves the highest CountBench improvement (+5.6pp) but at the cost of EmbSpatial ( − - 6pp) and RealWorldQA ( − - 6pp). This trade-off pattern contrasts with Qwen3-VL-4B’s favorable trade-off (gains on two metrics with mild degradation on one), supporting our hypothesis that larger models develop more modular OCR circuits.

[147] h3: C.3 Phi-4-multimodal-instruct Results

[148] p: Phi-4-multimodal-instruct’s OCR bottleneck is at L3–L9 ( ∼ \sim 10–25% depth). Table 10 shows interventions at bottleneck and control layers. Baseline OCR accuracy: 73.7%.

[149] figure: Interv. OCR Cnt Emb RWQ baseline — 89.2 62 66 L3_pc3 32.5 80.4 39 48 L6_pc3 21.6 92.5 45 49 L8_pc3 38.6 93.5 49 54 L3-9_pc3 64 40.7 22 27 L16_pc3 7.7 90.6 59 61 L28_pc3 6.2 88.4 62 63 Table 10: Phi-4 retention (%). L8_pc3: +4.3pp Count.

[150] p: Key Insight. Phi-4 shows a clear trade-off pattern: L8_pc3 improves CountBench (+4.3pp) but degrades EmbSpatial ( − - 13pp) and RealWorldQA ( − - 12.5pp). L8_pc1 (single component) has almost no effect, while L8_pc3 (three components) causes significant changes—suggesting OCR information is encoded across multiple principal components.

[151] h3: C.4 Qwen3-VL-8B Replication Results

[152] p: Qwen3-VL-8B-Instruct has 36 layers (same as 4B) but 4096 hidden dimension (1.6 × \times wider than 4B’s 2560). The most sensitive layer is L17 with 42.3% OCR accuracy under PC1–5 removal, confirming the bottleneck at ∼ \sim 47% depth—the same absolute layer as the 4B model.

[153] p: PCA variance peaks at L16–L20 (66–70%), matching the 4B’s bottleneck region. The 4B comparison: L17 drops to ∼ \sim 20% (deeper trough, slower recovery), while 8B’s shallower trough (42.3%) suggests greater representational redundancy in the wider residual stream.

[154] figure: Interv. OCR Cnt Emb RWQ baseline — 90.2 82.0 72.0 L16-20_pc3 — 94.6 76.0 60.0 L17-19_pc5 — 93.1 79.0 58.0 L17-20_pc5 — 93.1 79.0 56.0 Table 11: Qwen3-VL-8B retention (%). CountBench improves (+2.9–4.4pp), confirming interference effect. RealWorldQA drop ( − - 12 to − - 16pp) is larger than 4B, possibly reflecting greater load-bearing role of mid-layers at 8B scale.

[155] p: Key Finding: Depth-Indexed Conservation. The bottleneck is conserved at L17 ( ∼ \sim 47% depth) in both 4B and 8B models despite 1.6 × \times wider hidden dimension and 1.6 × \times more attention heads (20 → \rightarrow 32). This suggests bottleneck location is an architectural property of the DeepStack integration strategy rather than a function of model capacity.

[156] h2: References

[157] h2: Instructions for reporting errors

[158] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[159] p: Tip: You can select the relevant text first, to include it in your report.

[160] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[161] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
