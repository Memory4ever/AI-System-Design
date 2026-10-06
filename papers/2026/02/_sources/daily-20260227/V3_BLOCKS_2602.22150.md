[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: CoLoGen: Progressive Learning of Concept–Localization Duality for Unified Image Generation

[3] h6: Abstract

[4] p: Unified conditional image generation remains difficult because different tasks depend on fundamentally different internal representations. Some require conceptual understanding for semantic synthesis, while others rely on localization cues for spatial precision. Forcing these heterogeneous tasks to share a single representation leads to concept-localization representational conflict. To address this issue, we propose CoLoGen, a unified diffusion framework that progressively learns and reconciles this concept-localization duality. CoLoGen uses a staged curriculum that first builds core conceptual and localization abilities, then adapts them to diverse visual conditions, and finally refines their synergy for complex instruction-driven tasks. Central to this process is the Progressive Representation Weaving (PRW) module, which dynamically routes features to specialized experts and stably integrates their outputs across stages. Experiments on editing, controllable generation, and customized generation show that CoLoGen achieves competitive or superior performance, offering a principled representational perspective for unified image generation.

[5] h2: 1 Introduction

[6] figure: Figure 1 : The comparison between the multi-task learning strategy (a) and the ours progressive staged training (b) within the framework of unified multi-modal image generation. We specifically examines five conventional tasks: mask inpainting, image grounding, controllable image generation, customized image generation, and instruction-based image editing.

[7] p: Unified multimodal image generation [ 61 , 28 , 9 , 11 , 29 , 38 , 60 , 55 , 75 , 5 ] has recently attracted significant attention, as models aim to address diverse tasks (such as mask inpainting, image grounding, controllable synthesis, customized generation, and instruction-based editing) within a unified framework. Drawing from the success of unified architectures in language modeling [ 3 , 50 , 36 , 37 ] , recent efforts have sought to develop generalist diffusion models capable of handling varied visual conditions through shared encoders, backbones, or in-context interfaces.

[8] p: Unlike NLP, where tasks share relatively uniform token-level representations, unified image generation faces a core challenge in representation. Tasks such as inpainting [ 21 , 8 , 53 ] or subject-driven generation [ 35 , 66 , 64 , 38 ] rely heavily on conceptual representations , which encode semantic coherence and object-level understanding. Conversely, grounding and controllable generation [ 68 , 40 , 70 ] demand localization representations that emphasize spatial alignment, geometry, and structural consistency. More complex tasks such as instruction-based editing [ 67 , 44 , 11 , 62 , 60 , 73 , 12 , 2 ] rely on a synergistic integration of both.

[9] p: We refer to this fundamental conflict as the Concept–Localization Duality: Conceptual and localization cues occupy competing subspaces in the generative latent space, and naïvely optimizing them jointly leads to representational interference and unstable training [ 49 , 10 ] . Such interference explains why existing unified frameworks tend to excel at a subset of tasks while underperforming on others indicating that resolving this Duality is essential for reliable generalist image generation.

[10] p: Hence, this leads us to the following insight:

[11] p: Based on this, we propose Co ncept– Lo calization Gen eration ( CoLoGen ), that progressivelly unifies conditional image generation by explicitly structuring all tasks around conceptual and localization representations. As illustrated in Fig. 1 (b), CoLoGen employs a progressive staged training strategy to reduce representational conflict. To begin with, it learns fundamental conceptual and localization abilities from large-scale synthetic data through tasks such as mask inpainting and visual grounding [ 23 , 32 , 22 , 74 ] . Secondly, it adapts these abilities to diverse conditional signals, such as segmentation, depth, and Canny edges. Finally, it refines their synergy through instruction-image alignment on complex editing and customization tasks. Such a progressive, easy-to-hard curriculum effectively could mitigate the issues of conflicting and significantly improves performance on complex tasks.

[12] p: Furthermore, to stabilize optimization across stages and preserve acquired knowledge, we introduce a lightweight architectural component termed P rogressive R epresentation W eaving ( PRW ). While recent in-context learning frameworks [ 9 , 73 , 72 ] have unified diverse instructions at the input modality level by concatenating reference images, control signals, and noisy latents, they do not explicitly address underlying representational conflicts during joint training. PRW resolves representational conflicts by using a pool of lightweight experts that separately acquire concept and localization skills in early training. A dynamic router, guided by Veteran Gate Routing, then learns how to activate and combine these experts for different tasks. Through this staged integration, PRW gradually weaves the dual representations into a stable unified space while avoiding catastrophic forgetting.

[13] p: In summary, this work contributes the following:

[14] p: We propose Concept–Localization Generation (CoLoGen), a unified multimodal image generation framework that alleviates task conflicts through explicit structuring around conceptual and localization representations.

[15] p: We propose a progressive staged learning strategy and a novel Progressive Representation Weaving (PRW) architecture that dynamically routes and integrates specialized experts across training stages.

[16] p: Extensive experiments on instruction editing, subject-driven generation, and controllable image generation demonstrate that CoLoGen achieves performance competitive with or surpassing task-specific state-of-the-art methods.

[17] h2: 2 CoLoGen

[18] figure: Figure 2 : The overall framework of the unified Multi-modal to Image generation model, CoLoGen. For each training stage, CoLoGen efficiently integrates a set of condition-specific experts via the Progressive Representation Weaving (PRW) which are constructed on KV projection layers and a dynamic router G G . Notably, The QKV projection layer and the self-attention layer are sharing weights for the inputs of Noisy Latent and Source Image Latent. CoLoGen employs a progressive staged training strategy to gradually increase the number of experts E k E_{k} , allowing it to better adapt to more complex downstream tasks.

[19] h3: 2.1 Concept and Localization Representations

[20] p: Conditional image generation tasks fundamentally rely on two complementary abilities: visual concept generation and visual localization . Their relative importance varies by task. Specifically, controllable generation tasks provide strong structural conditions (e.g., segmentation, edges, or depth), enabling the model to largely disregard localization requirements and instead focus on regenerating coherent visual concepts. In contrast, customized generation tasks demand precise localization of the subject in a reference image to preserve identity-specific features while allowing a degree of conceptual generalization in the generated output. Instruction-based editing tasks necessitate not only the comprehension of textual instructions but also accurate localization of the target editing region, followed by the regeneration of visual concepts within that localized area.

[21] p: Hypothesis. We formalize these two abilities as two distinct and underlying representations. Let h ∈ ℝ L × d h\in\mathbb{R}^{L\times d} be an intermediate feature map within the diffusion model’s transformer blocks. We posit the existence of a concept representation ℛ c \mathcal{R}_{c} and a localization representation ℛ l \mathcal{R}_{l} , which can be extracted from h h via the mapping functions f c f_{c} and f l f_{l} , respectively:

[22] table: ℛ c = f c ​ ( h ) , ℛ l = f l ​ ( h ) \mathcal{R}_{c}=f_{c}(h),\quad\mathcal{R}_{l}=f_{l}(h) (1)

[23] p: Our central hypothesis is that the failure of existing unified models stems from forcing a single, static fusion of these representations across all tasks. This joint optimization creates a representational conflict, where improving the model’s capacity for conceptual understanding (optimizing f c f_{c} ) can degrade its spatial precision (harming f l f_{l} ), and vice-versa. A successful unified model must therefore be able to dynamically modulate the influence of ℛ c \mathcal{R}_{c} and ℛ l \mathcal{R}_{l} based on the specific demands of each task. Despite recent advances, generalist image generation models [ 9 , 61 , 76 , 28 , 6 , 43 ] have not yet systematically explored the synergistic interaction between visual concept and localization representations. We argue that such a unified representational perspective is critical for advancing the scope and reliability of unified conditional image generation.

[24] h3: 2.2 Model Design

[25] p: To validate this hypothesis, CoLoGen is grounded in two key components: (1) the Progressive Representation Weaving (PRW) architecture, which forms the structural basis for dynamic representation management; and (2) a Progressive Staged Training strategy, which provides the methodological framework to resolve representational conflicts in an easy-to-hard manner. Our overall framework is built upon the advanced FLUX.1 architecture [ 1 ] .

[26] p: Progressive Representation Weaving (PRW). To enable dynamic management and integration of conceptual and localization representations, we propose the Progressive Representation Weaving (PRW) architecture. As illustrated in Figure 2 , PRW operates within each multi-modal attention block to adapt the source latent h h for diverse task demands, complementing the standard processing of the noisy latent x x and the text latent y y . The architecture comprises a dynamic routing mechanism G G and a pool of N N specialized, parameter-efficient experts { E k } k = 1 N \{E_{k}\}_{k=1}^{N} , where each expert serves as a Key–Value projection module, denoted as KV_proj k \text{KV\_proj}_{k} . The router G G , implemented as a Noisy Router, determines the most suitable expert by generating a vector of pre-softmax logits 𝐰 \mathbf{w} over the expert pool conditioned on the input latent h h . Formally, this can be defined as:

[27] table: 𝐰 = h ​ W r + ϵ ⊙ softplus ​ ( h ​ W n ) , ϵ ∼ 𝒩 ⁡ ( 0 , 𝐈 ) , \mathbf{w}=hW_{r}+\epsilon\odot\text{softplus}(hW_{n}),\quad\epsilon\sim\mathcal{N}(0,\mathbf{I}), (2)

[28] p: where W r W_{r} and W n W_{n} are learnable projection matrices for the routing logits and the noise scale, respectively. The term ϵ \epsilon represents standard Gaussian noise, and ⊙ \odot denotes element-wise multiplication. This noise injection during training encourages balanced expert utilization, while the mechanism remains fully deterministic during inference.

[29] p: Following the logit computation, a sparse activation function is subsequently applied. We apply a top-1 selection on the softmax-normalized logits to identify the single most relevant expert for the given input:

[30] table: 𝒮 = TopK ​ ( Softmax ​ ( 𝐰 ) , n = 1 ) , \mathcal{S}=\text{TopK}(\text{Softmax}(\mathbf{w}),n=1), (3)

[31] p: where 𝒮 \mathcal{S} is the set containing the index of the activated expert. The resulting adaptive residual is computed by passing the original latent h h through the selected expert and scaling the output by its corresponding softmax weight. This residual is then added to a base projection to obtain the final Key and Value representations for the source latent, K h ^ K_{\hat{h}} and V h ^ V_{\hat{h}} :

[32] table: ( K h ^ , V h ^ ) = KV_proj base ​ ( h ) + ∑ k ∈ 𝒮 softmax ​ ( 𝐰 ) k ​ E k ​ ( h ) (K_{\hat{h}},V_{\hat{h}})=\text{KV\_proj}_{\text{base}}(h)+\sum_{k\in\mathcal{S}}\text{softmax}(\mathbf{w})_{k}E_{k}(h) (4)

[33] p: While the PRW module dynamically generates the Key and Value representations for the source latent, its Query Q h Q_{h} , along with the QKV projections for all other latents, is produced through standard linear projection layers.

[34] figure: Table 1 : The outline of training data about each training stage. Notably, Endogenous Pre-training comprises two distinct training steps: mask inpainting and image grounding. Instruction-Image Alignment encompasses both Customized Generation and Instruction Editing. Stage Task # Samples Data Source Endogenous Pre-training Mask Inpainting 3M ADE20k, COCOStuff, JouneyDB Image Grounding 1M RefCOCO, RefCOCOg, RefCOCO+, LVIS Conditional Injection Controllable Generation 20M Multigen-20M, Multigen-20M-Depth, ADE20k, COCOStuff Instruction-image alignment Customized Generation 200K Subject200k Instruction Editing 1.6M OmniEdit, Magicbrush, In-house Data

[35] p: The attention mechanism then proceeds in a structured and sequential manner to fuse these representations. First, the source latent’s Query ( Q h Q_{h} ) attends to its own dynamically adapted Key-Value pair ( K h ^ , V h ^ ) (K_{\hat{h}},V_{\hat{h}}) in a self-attention step. This allows the source representation to internalize the task-specific information introduced by the activated expert. Subsequently, the stem self-attention mechanism is employed to update the noisy and text latents. The queries Q x Q_{x} and Q y Q_{y} attend to a comprehensive context formed by concatenating the Keys and Values from all three modalities, including the newly adapted source representations:

[36] table: K all \displaystyle K_{\text{all}} = concat ​ ( K x , K y , K h ) , \displaystyle=\text{concat}(K_{x},K_{y},{K}_{h}), (5) V all \displaystyle V_{\text{all}} = concat ​ ( V x , V y , V h ) , \displaystyle=\text{concat}(V_{x},V_{y},{V}_{h}), (6) Output x , y \displaystyle\text{Output}_{x,y} = Self-attn ​ ( concat ​ ( Q x , Q y ) , K all , V all ) . \displaystyle=\text{Self-attn}(\text{concat}(Q_{x},Q_{y}),K_{\text{all}},V_{\text{all}}). (7)

[37] p: This two-stage process ensures that both text and noisy latents can draw upon a source representation that has already been refined for the specific task, enabling a more effective and context-aware fusion of multimodal information.

[38] p: Progressive Staged Training. The CoLoGen framework employs a progressive staged training strategy, as illustrated in Figure 1 (a), to systematically mitigate representational conflicts and enhance cross-task complementarity. Inspired by principles of lifelong learning, this strategy organizes all tasks around complementary conceptual and localization representations. During this multi-step training, the model progressively develops and strengthens its capabilities.

[39] p: At each training step t ∈ [ 0 , 4 ] t\in[0,4] , the model integrates N N specialized, parameter-efficient experts { E k } k = 0 N − 1 \{E_{k}\}_{k=0}^{N-1} through the Progressive Representation Weaving (PRW) architecture, where N = t + 1 N=t+1 . For notational simplicity, the subscript t t is omitted in the subsequent formulations. The expert E N − 1 E_{N-1} is designated for the task-specific training at step t t , while other experts remain frozen.

[40] p: Veteran Gate Routing Supervision. To effectively leverage knowledge acquired in preceding training steps and encourage balanced expert utilization, we propose a Veteran Gate Routing Supervision mechanism. This mechanism incorporates an auxiliary supervision term into the overall training loss, guiding the dynamic routing module to align its expert assignment distributions with desired usage ratios.

[41] p: Given the defined set of experts { E k } k = 0 N − 1 \{E_{k}\}_{k=0}^{N-1} ( N = t + 1 N=t+1 ), a regularization term is applied to encourage routing according to predefined ratio-specific experts across all MMDiT blocks. As indicated by the sparse activation in Equation 3 from the routing module, 𝒮 \mathcal{S} denotes the set of selected expert indices, with | 𝒮 | = 1 |\mathcal{S}|=1 in our implementation. The usage ratio of the specific expert E N − 1 E_{N-1} is calculated as:

[42] table: U t = 1 L n ​ ∑ i = 1 L n 𝕀 ⁡ ( e i = N − 1 ) , U_{t}=\frac{1}{L_{n}}\sum_{i=1}^{L_{n}}\mathbb{I}(e_{i}=N-1), (8)

[43] p: where L n L_{n} represents the total number of MMDiT blocks, and e i ∈ 𝒮 e_{i}\in\mathcal{S} indicates the assigned expert for block i i . We then define the veteran gate routing supervision loss term ℒ veteran \mathcal{L}_{\text{veteran}} to penalize deviations from the desired routing density ρ \rho of specific experts:

[44] table: ℒ veteran = α ⋅ | U t − ρ | , \mathcal{L}_{\text{veteran}}=\alpha\cdot|U_{t}-\rho|, (9)

[45] p: where α \alpha is a hyperparameter that balances the veteran gate routing supervision loss with the primary diffusion loss. Consequently, the total training loss ℒ total \mathcal{L}_{\text{total}} comprises two parts: the primary diffusion generation loss ℒ task \mathcal{L}_{\text{task}} and the veteran gate routing supervision loss term ℒ veteran \mathcal{L}_{\text{veteran}} :

[46] table: ℒ total = ℒ task + ℒ veteran . \mathcal{L}_{\text{total}}=\mathcal{L}_{\text{task}}+\mathcal{L}_{\text{veteran}}. (10)

[47] p: This auxiliary supervision, ℒ veteran \mathcal{L}_{\text{veteran}} , plays a crucial role in guiding the gating network to preferentially select specific experts, thereby enabling dynamically balanced expert utilization and contributing to a more stable training process.

[48] h3: 2.3 Unified Multi-modal to Image Generation Dataset

[49] figure: Table 2 : Quantitative results for instruction image editing evaluated on the Emu Edit test split and MagicBrush test split. “-” indicates that the method does not report the corresponding results. ↑ \!\uparrow indicates higher result is better, while ↓ \!\downarrow means lower is better. Methods Emu Edit test set MagicBrush test set CLIP i ↑ \text{CLIP}_{i}\!\uparrow CLIP o ​ u ​ t ↑ \text{CLIP}_{out}\!\uparrow ℓ 1 ↓ \ell_{1}\!\downarrow DINO ↑ \uparrow CLIP i ↑ \text{CLIP}_{i}\!\uparrow CLIP o ​ u ​ t ↑ \text{CLIP}_{out}\!\uparrow ℓ 1 ↓ \ell_{1}\!\downarrow DINO ↑ \uparrow Specialist Models InstructPix2Pix [ 2 ] 0.834 0.219 0.121 0.762 0.837 0.245 0.093 0.767 MagicBrush [ 67 ] 0.838 0.222 0.100 0.776 0.883 0.261 0.058 0.871 PnP [ 51 ] 0.521 0.089 0.304 0.153 0.568 0.101 0.289 0.220 Null-Text Inv. [ 33 ] 0.761 0.236 0.075 0.678 0.752 0.263 0.077 0.664 Emu Edit [ 44 ] 0.859 0.231 0.094 0.819 0.897 0.261 0.052 0.879 Generalist Models UltraEdit [ 76 ] 0.844 0.283 0.071 0.793 0.868 - 0.088 0.792 OmniGen [ 61 ] 0.836 0.233 - 0.804 - - - - PixWizard [ 28 ] 0.845 0.248 0.069 0.798 0.884 0.265 0.063 0.876 Explanatory Instructions [ 43 ] 0.821 0.286 0.132 0.768 0.875 0.292 0.093 0.831 UniReal [ 9 ] 0.851 0.285 0.099 0.790 0.903 0.308 0.081 0.837 CoLoGen (ours) 0.866 0.301 0.111 0.843 0.931 0.301 0.063 0.932

[50] p: To achieve robust and unified multi-modal image generation capabilities, CoLoGen is trained on large-scale synthetic datasets and a high-quality image-instruction-image triplet dataset through a multi-stage lifelong learning paradigm, as shown in Table 1 . In particular, the training set comprises our constructed synthetic datasets (3M), collected public datasets (22M), and high-quality in-house data (50K).

[51] p: Mask Inpainting. In the endogenous pre-training stage, our goal is to learn rich visual concepts for individual “objects” and entire “scenes”. To this end, we constructed a set of three million synthetic mask-inpainting data derived from JourneyDB [ 46 ] , incorporating three types of masks: random masks, object-shaped masks, and irregular object-shaped masks. Specifically, we use spacy [ 19 ] to extract nouns from global captions and employ GroundingDino [19] and SAM [20] to segment target objects with corresponding masks, following the procedures in [ 16 , 61 ] . Additionally, we augment the training set with instance masks and global captions from the [ 4 ] and [ 78 ] datasets.

[52] p: During training, we first generate random masks following [ 47 ] and discard any masks whose intersection over union (IoU) with any object mask exceeds 0.3, thereby placing greater emphasis on scene-level concept learning. Next, inspired by [ 65 ] , we fit a Bessel curve to the bounding box of the masked object, uniformly sample 20 points along this curve, and connect them sequentially to form an irregular object-shaped mask which prevents instability in object generation caused by ill-defined mask shapes during testing. Finally, we sample random masks, object-shaped masks, and irregular object-shaped masks at a ratio of 20%, 40%, and 40%, substantially enhance model’s robustness.

[53] p: Image Grounding. Image grounding [ 43 ] involves identifying and highlighting specific object regions in an image based on textual prompts. The training data is sourced from RefCOCO [ 22 ] , RefCOCOg [ 32 ] , RefCOCO+ [ 23 ] , and LVIS [ 18 ] . Following works [ 28 , 43 , 74 ] , we apply a variety of data augmentation strategies to construct three grounding tasks: (1) Box Detection Referring, where the target object is enclosed with bounding boxes of a specified color; (2) Mask Segmentation Referring, where the target object is covered with a specified color mask; and (3) Instance Detection Referring, where a random instance of the target class is enclosed with bounding boxes.

[54] p: Controllable Image Generation. Following work [ 61 ] , we collect the MultiGen (20M) [ 40 ] , ADE20k [ 78 ] , and COCOStuff [ 4 ] datasets to support six visual condition controls, including Canny, Depth, HED, Lineart, and Segmentation. Notably, HED and Lineart are extracted online during training.

[55] p: Instruction Editing and Customized Generation. Instruction-based editing and customized generation leverage simple textual interactions to efficiently modify or create images, offering substantial potential for practical applications. In this part, we consolidate multiple public editing datasets—MagicBrush (300K) [ 67 ] and OmniEdit (1.2M) [ 11 ] —along with the public customized-generation dataset Subject200K [ 48 ] . Furthermore, we incorporate 50K high-quality in-house editing data specifically curated to enhance the aesthetic appeal and realism of the generated images.

[56] h2: 3 Experiments

[57] h3: 3.1 Training Recipe

[58] figure: Table 3 : Quantitative results for Controllable image generation on MultiGen-20M, ADE-20K and COCOStuff. “-” indicates that the method does not report corresponding results. ↑ \!\uparrow indicates that a higher value is better, while ↓ \!\downarrow indicates that a lower value is better. Methods Canny-to-Image Depth-to-Image LineArt-to-Image Seg-to-Image CLIP-S↑ RMSE↓ SSIM↑ mIoU↑ MultiGen-20M MultiGen-20M MultiGen-20M COCO-Stuff ADE20K Specialist Models ControlNet-SD1.5 [ 68 ] 32.15 35.90 - 27.46 32.55 T2I-Adapter-SD1.5 [ 35 ] 31.71 48.40 63.94 - 12.61 Gligen [ 27 ] - 38.83 - - 23.78 Uni-ControlNet [ 77 ] - 40.65 - - 19.39 UniControl [ 40 ] - 39.18 70.54 - 25.44 Generalist Models OmniGen [ 61 ] - 28.54 - - 44.23 PixWizard [ 28 ] 32.01 33.83 - - - Explanatory Instructions 27.16 55.30 - - - CoLoGen (ours) 33.31 31.79 77.96 29.43 42.82

[59] figure: Table 4 : Quantitative results for customized generation on DreamBench [ 41 ] . Model CLIP-T ↑ \textbf{CLIP-T}\!\uparrow CLIP-I ↑ \textbf{CLIP-I}\!\uparrow DINO ↑ \textbf{DINO}\!\uparrow Specialist Models Textual Inversion [ 34 ] 0.255 0.780 0.569 DreamBooth [ 41 ] 0.305 0.803 0.668 BLIP-Diffusion [ 25 ] 0.302 0.805 0.670 ELITE [ 54 ] 0.296 0.772 0.647 Re-Imagen [ 7 ] 0.270 0.740 0.600 BootPIG [ 39 ] 0.311 0.797 0.674 Generalist Models OmniGen [ 61 ] 0.320 0.810 0.693 UniReal [ 9 ] 0.326 0.806 0.702 CoLoGen (ours) 0.315 0.825 0.714

[60] p: As illustrated in Fig. 1 , the CoLoGen model training process consists of five steps: two steps of endogenous pre-training, one step of conditional injection learning and two steps of instruction-image alignment learning. The outline of all training datasets is shown in Table 1 .

[61] p: Concept–Localization Duality Pre-training. In the first stage of Concept–Localization Duality pre-training, we utilize three million synthetic data as mentioned in Sec 2.3 for the mask inpainting task. We apply the learning rate of 1e-4 for training 200K iterations with a global batch size of 256. We set the routing density ρ \rho of e ​ x ​ p ​ e ​ r ​ t 0 expert_{0} equal to 1, and the loss of weight α 0 = 0 \alpha_{0}=0 . Then, the second stage is trained on the task of image grounding. We apply the learning rate of 1e-4 for training 200K iterations with a global batch size of 256. The routing density ρ \rho of e ​ x ​ p ​ e ​ r ​ t 1 expert_{1} is set to 0.8, and the loss weight is α 1 = 0.5 \alpha_{1}=0.5 .

[62] p: Conditional Injection Learning. During this stage, the training dataset is composed of several publicly accessible datasets as mentioned in Sec 2.3 builded on the task of controlable generation. The learning rate is 1e-4, the training iteration is set as 400K and the global batch size is 128. We set the routing density ρ \rho of e ​ x ​ p ​ e ​ r ​ t 2 expert_{2} as 0.8, and the loss weight α 2 \alpha_{2} as 0.5.

[63] p: Instruction-Image Alignment Learning. In the final training stage, we first introduce Subject200k [ 48 ] for the training of customized image generation, and then fine-tune the model on the mixed dataset summarized in Table 1 . We train on the task of customized generation for 50K iterations with a global batch size of 128, followed by instruction editing for 200K iterations with the same batch size. For both tasks, we set the routing density ρ \rho of e ​ x ​ p ​ e ​ r ​ t i expert_{i} to 0.8, and the loss weight α i \alpha_{i} to 0.5.

[64] h3: 3.2 Main Results

[65] p: Instruction Editing. We evaluate the CoLoGen on two Instruction editing benchmarks including the MagicBrush test split [ 67 ] and the Emu Edit test split [ 44 ] , which include diverse editing purposes, such as object addition, object removal, localized modifications, background alteration, etc. Following the evaluation metrics used both by Emu Edit and MagicBrush benchmarks, we evaluate four metrics: 1) CLIP i \text{CLIP}_{i} : CLIP image similarity between source image and output image; 2) CLIP o ​ u ​ t \text{CLIP}_{out} : CLIP text-image similarity between edited image and target caption; 3) ℓ 1 \ell_{1} : ℓ 1 \ell_{1} distance between source image and output image; 4) DINO: DINO similarity between source image and output image. We compare our model against a variant of specialist and generalist models and report the quantitative results in Table 2 . The findings indicate that CoLoGen achieves consistent and remarkable improvements across all both benchmarks in instruction adherence. The slightly higher L1 score compared to the SOTA model is expected, as substantial modifications between the input and output are anticipated under instruction-based editing. Moreover, L1 is not a particularly robust metric for this setting, consistent with works [ 9 , 44 ] .

[66] p: Controllable Image Generation. We use the dataset and script from [ 26 ] to evaluate the ability on conditional control generation. For the Segmentation-to-Image condition, we report the m ​ I ​ o ​ U mIoU on COCO-Stuff and ADE20k benchmarks. As illustrated in Table 3 , we report CLIP similarity score CLIP-S for Canny-to-Image condition, SSIM metric for the LineArt-to-Image condition and RMSE for Depth-to-Image condition. CoLoGen achieves results comparable to those of SOTA controllable image generation methods.

[67] p: Customized Generation. Following OmniGen [ 61 ] , we evaluate the single-entity customized generation capability using DreamBench [ 41 ] , which comprises 750 prompts across 30 subjects. Similarly, we select only one input image per subject from the provided set of 4–7 images. Table 4 reports the DINO score, CLIP-I similarity, and CLIP-T similarity. Compared to specialist and generalist methods, CoLoGen achieves substantial improvements in DINO score and CLIP-I similarity, while obtaining comparable performance on CLIP-T similarity.

[68] figure: Figure 3 : Qualitative comparison for customized image generation. We compare with a series of public SOTA methods including OmniGen [ 61 ] , MS-Diffusion [ 52 ] , and IP-Adapter [ 64 ] on DreamBench [ 41 ] . CoLoGen achieves remarkable performance even when trained on a limited amount of proprietary data, which can be attributed to the rich multimodal knowledge acquired by the model during the endogenous pre-training and conditional injection learning phases.

[69] h3: 3.3 Ablation Studies

[70] figure: Table 5 : Evaluation the contribution of the concept and localization representations on instruction-based editing (Magicbrush) and customized generation (Dreambench). ℛ c \mathcal{R}_{c} denotes the concept representation and ℛ l \mathcal{R}_{l} denotes the localization representation. Metrics that exhibit a noticeable improvement over the baseline (w/o ℛ l \mathcal{R}_{l} & w/o ℛ c \mathcal{R}_{c} ) are highlighted in blue . Method CLIP-T ↑ \textbf{CLIP-T}\!\uparrow CLIP-I ↑ \textbf{CLIP-I}\!\uparrow DINO ↑ \textbf{DINO}\!\uparrow Magicbrush w/o ℛ l \mathcal{R}_{l} & w/o ℛ c \mathcal{R}_{c} 0.260 0.889 0.901 w ℛ l \mathcal{R}_{l} 0.279 0.922 0.927 w ℛ c \mathcal{R}_{c} 0.302 0.881 0.905 w ℛ c \mathcal{R}_{c} & ℛ l \mathcal{R}_{l} (Co-training) 0.269 0.918 0.922 w ℛ c \mathcal{R}_{c} & ℛ l \mathcal{R}_{l} (CoLoGen) 0.301 0.931 0.932 Dreambooth w/o ℛ l \mathcal{R}_{l} & w/o ℛ c \mathcal{R}_{c} 0.300 0.808 0.683 w ℛ l \mathcal{R}_{l} 0.310 0.829 0.707 w ℛ c \mathcal{R}_{c} 0.301 0.813 0.702 w ℛ c \mathcal{R}_{c} & ℛ l \mathcal{R}_{l} (Co-training) 0.308 0.795 0.679 w ℛ c \mathcal{R}_{c} & ℛ l \mathcal{R}_{l} (CoLoGen) 0.315 0.825 0.714

[71] figure: Figure 4 : Ablation studies for hyperparameter of lifelong strategy in the last stage, with final settings highlighted in orange . (a) Impact of α \alpha on the weight for balancing the veteran gate routing supervision. (b) Influence of r ​ a ​ n ​ k rank on LoRA, where LoRA alpha weight defaults to twice the r ​ a ​ n ​ k rank . (c) Impact of ρ \rho , which denotes the rounting density of e ​ x ​ p ​ e ​ r ​ t N − 1 expert_{N-1} .

[72] figure: Figure 5 : Qualitative comparisons with current state-of-the-art mask-inpainting methods. CoLoGen demonstrates robust text-following capabilities, and exhibits strong visual coherence between the mask area and the background.

[73] p: The contribution of the concept and localization representations. We conduct a detailed ablation study on concept and localization representations across two high-level tasks: instruction-based editing and customized generation. As shown in Table 5 , our proposed CoLoGen model (with ℛ l \mathcal{R}_{l} and ℛ c \mathcal{R}_{c} ) consistently outperforms the baseline model (without ℛ l \mathcal{R}_{l} and ℛ c \mathcal{R}_{c} ) across six metrics on two benchmarks.

[74] p: For the instruction-editing task (MagicBrush), incorporating ℛ c \mathcal{R}_{c} leads to a 0.042 improvement in CLIP-T, indicating that concept representations substantially enhance the model’s ability to follow instructions. Meanwhile, adding ℛ l \mathcal{R}_{l} improves both CLIP-I and DINO scores, demonstrating that localization representations significantly strengthen the model’s capability to identify and modify the intended regions while maintaining consistency in unedited areas. Furthermore, in the customized generation task, the inclusion of localization representations also yields consistent improvements for CoLoGen over the baseline, highlighting general effectiveness across diverse generative objectives. On the other hand, multi-task co-training (with ℛ c \mathcal{R}_{c} & ℛ l \mathcal{R}_{l} ), as illustrated in Figure 1 (a), improves instruction following and fidelity only in one aspect, and even results in a decline in CLIP-I and DINO scores for customized generation compared with the baseline.

[75] p: Hyperparameters ablation. We provide comprehensive ablation studies on hyperparameters, as illustrated in Fig. 4 . All experiments are conducted during the instruction-editing fine-tuning stage, and we report the CLIP-I score for brevity. Fig. 4 (a) demonstrates that veteran gate routing supervision effectively balances the utilization of specific experts and significantly improves CLIP-I performance. In Fig. 4 (b), the LoRA r ​ a ​ n ​ k rank achieves optimal performance at 128. Fig. 4 (c) indicates that ρ \rho performs best at 0.8, suggesting that the 20% of experts trained during the early stage substantially contribute to downstream task performance.

[76] h3: 3.4 Qualitative Experiments

[77] p: Customized Generation. We present qualitative comparisons for customized image generation in Fig. 3 . CoLoGen demonstrates superior performance compared with current state-of-the-art models in preserving details of the reference object, adhering to novel textual prompts, and maintaining consistency between the reference object and its background.

[78] p: Mask Inpainting. Mask inpainting enables the model to learn robust visual concept generation capabilities. Herein, we present qualitative comparisons with current state-of-the-art mask-inpainting methods. As illustrated in Fig. 5 , CoLoGen demonstrates strong inpainting capability which is trained on our large-scale synthetic datasets. Furthermore, the substantial endogenous capability developed during the pre-training stage equips CoLoGen with extensive multimodal knowledge for subsequent training stages.

[79] h2: 4 Limitation and Conclusion

[80] p: Limitation. While CoLoGen’s Progressive Representation Weaving (PRW) architecture offers an efficient and adaptable design for various multi-modal to image generation models, it currently faces limitations concerning memory capacity as the number of tasks or the complexity of integrated experts scales up. Future work will focus on optimizing the PRW architecture for greater memory efficiency and scalability to handle an even broader range of challenging multi-modal tasks.

[81] p: Conclusion. In this work, we introduce CoLoGen, a novel unified image generation framework designed to address the inherent concept–localization duality. By explicitly structuring tasks around conceptual and localization representations from our PRW model and employing a progressive staged training strategy, CoLoGen effectively mitigates representational conflicts and promotes cross-task complementarity. Extensive experiments across various benchmarks demonstrate that CoLoGen achieves competitive or superior performance compared to existing state-of-the-art methods. This work establishes a principled representational perspective for unified image generation, paving the way for more robust and versatile generative models in the future.

[82] h2: References

[83] p: Supplementary Material

[84] figure: Figure 6 : Instructional editing results of our CoLoGen. Our method can adapt to various types of instructions, faithfully follow instructions while preserving the visual consistency of the input images, ensuring high-quality and coherent results.

[85] h2: Appendix A Related work

[86] h3: A.1 Unified Multi-modal to Image Generation

[87] p: Recent advancements in multi-modal image generation strive to consolidate diverse generation and editing tasks into unified frameworks, moving beyond task-specific pipelines. Early approaches often relied on distinct encoders or adapters for different conditions. For instance, ControlNet [ 69 ] and T2I-Adapter [ 35 ] introduced extensive external modules to guide pre-trained diffusion models. While effective, these methods face scalability issues when expanding to new tasks due to the linear growth of parameters.

[88] p: To address this, recent works have focused on unified architectures. Unified-IO 2 [ 31 ] and Janus [ 56 ] demonstrate the power of autoregressive transformers in handling multi-modal inputs and outputs, though often at the cost of inference speed compared to diffusion models. In the diffusion domain, OmniControl [ 48 ] and DreamOmni [ 60 ] integrate visual conditions directly into Diffusion Transformers (DiT), achieving spatial alignment with minimal parameter overhead. OmniGen [ 61 ] and PixWizard [ 28 ] further push the boundary by treating image generation and editing as a unified sequence generation problem, removing the reliance on external condition encoders entirely. Similarly, UniReal [ 9 ] treats image generation tasks as discontinuous video frames to capture real-world dynamics.

[89] p: More recently, Qwen-Image [ 55 ] presents a large-scale diffusion foundation model emphasizing strong text rendering, multi-task training, and improved semantic–visual consistency for unified generation and editing. Query-Kontext [ 45 ] decouples multimodal reasoning from high-fidelity synthesis by leveraging a vision-language model to produce contextual query tokens that guide diffusion-based image generation and editing. Z-Image [ 5 ] proposes an efficient single-stream diffusion transformer that unifies image generation and editing with scalable training, distillation, and accelerated inference.

[90] p: However, these unified frameworks often struggle with what we identify as the Concept–Localization Duality . Tasks like subject-driven generation require rich semantic concept encoding, whereas tasks like layout-to-image generation demand precise spatial structure. Naively training a single unified model often leads to representational conflict, where optimizing for semantic fidelity degrades spatial precision [ 10 ] . Unlike these approaches, CoLoGen explicitly decouples and progressively weaves these representations, ensuring high performance across both concept-heavy and localization-heavy tasks.

[91] h3: A.2 Parameter-Efficient Composition and LoRA-MoE

[92] p: Low-Rank Adaptation (LoRA) [ 20 ] has become the standard for parameter-efficient fine-tuning. To handle multi-task learning without catastrophic forgetting, recent research has explored Mixture-of-Experts (MoE) architectures combined with LoRA.

[93] p: In the realm of Large Language Models (LLMs), Octavius [ 10 ] and LoRAHub [ 20 ] propose routing mechanisms to dynamically select or compose LoRA modules for unseen tasks. In visual generation, Mix-of-Show [ 17 ] addresses the challenge of multi-concept personalization by fusing multiple LoRAs, while ZipLoRA [ 42 ] attempts to merge content and style LoRAs by optimizing their orthogonality. MoLE [ 59 ] applies a mixture of LoRA experts to select layer-wise adapters dynamically. ICEdit [ 72 ] enables instruction-based image editing via in-context generation, combining with LoRA-MoE. While relevant, these methods typically employ static merging strategies or route based solely on input domains. They do not account for the evolving nature of representational needs during the diffusion process itself. CoLoGen advances this paradigm via our Progressive Representation Weaving (PRW) . Instead of static composition, we employ a time-step dependent ”Veteran Gate” routing that dynamically balances expert usage. Crucially, our curriculum creates experts specialized specifically for Concept versus Localization , rather than just arbitrary data subsets, directly addressing the internal duality of generative tasks.

[94] h2: Appendix B More Results

[95] h3: B.1 Controllable Image Generation

[96] p: We expand our evaluation to recent state-of-the-art models built on stronger backbones (e.g., FLUX and SD3). While prior works typically report results under limited settings, we conduct a comprehensive comparison across both Canny and Depth conditions. As shown in Tab. 6 , our method consistently achieves the best overall performance across different metrics.

[97] figure: Canny Depth Method Base C-S ↑ \uparrow FID ↓ \downarrow SSIM ↑ \uparrow FID ↓ \downarrow UNIC-Adapter [ 15 ] SD3 – 23.47 31.10 – RealGen [ 14 ] CogV – 17.50 35.0 23.40 OmniControl [ 63 ] FLUX 30.60 20.63 39.0 27.26 EasyControl [ 71 ] FLUX 28.60 – 35.9 20.39 CoLoGen(Ours) FLUX 33.31 18.20 40.1 19.56 Table 6 : Controllable image generation comparison on recent backbone models.

[98] h3: B.2 Customized Image Generation

[99] p: We further compare with recent large-scale customized generation methods, including Bagel and OmniGen2, on Subject-200k. Notably, these approaches are trained on substantially larger datasets (10M+ samples), whereas our method uses fewer than 1M samples. As reported in Tab. 7 , CoLoGen achieves competitive or superior performance despite the significantly smaller training scale.

[100] figure: Method Data DINO C-I C-T OmniControl [ 63 ] 200k 0.684 0.799 0.312 FLUX-IP-Adapter [ 64 ] 200k 0.582 0.820 0.288 CoLoGen(Ours) 200k 0.714 0.825 0.315 UNO-FLUX [ 58 ] 1M–5M 0.760 0.835 0.308 OmniGen2 [ 57 ] 10M+ 0.749 0.830 0.314 BAGEL [ 13 ] 10M+ 0.797 0.859 0.307 Table 7 : Customized image generation comparison under different training data scales.

[101] h3: B.3 Image Editing Benchmark

[102] p: We additionally evaluate on the recent GEdit-Bench full set. As shown in Tab. 8 , CoLoGen achieves the best G_SC score and remains competitive across other editing quality metrics, demonstrating strong generalization ability in image editing tasks.

[103] figure: GEdit-Bench (Full Set) ↑ \uparrow Method G_SC G_PQ G_O Step1X-Edit [ 30 ] 7.66 7.35 6.97 BAGEL [ 13 ] 7.36 6.83 6.52 FLUX.1 Kontext [ 24 ] 7.02 7.60 6.56 Qwen-Image [ 55 ] 8.00 7.86 7.56 CoLoGen (Ours) 8.03 7.15 7.31 Table 8 : Results on GEdit-Bench (Full Set) .

[104] figure: Figure 7 : Controllable generation results of our CoLoGen.

[105] figure: Figure 8 : Visual examples from the image grounding task demonstrate that CoLoGen, after undergoing endogenous pre-training, exhibits highly accurate visual localization capabilities.

[106] h2: Appendix C Visualization

[107] h3: C.1 Instruction Editing

[108] p: We provide expanded visual examples on the Instruction Editing benchmark in Figure 6 . The results demonstrate CoLoGen’s versatility in handling diverse editing instructions, ranging from localized object manipulation to global stylistic changes. These results validate that our Instruction-Image Alignment stage effectively fine-tunes the synergy between concept and localization representations.

[109] h3: C.2 Controllable Image Generation

[110] p: Figure 7 showcases CoLoGen’s performance on the Controllable Image Generation benchmark under various spatial conditions, including Depth maps, Segmentation masks, Canny edges, HED edges, and LineArt. The visualization highlights the effectiveness of the Localization Representation ( R l R_{l} ) acquired during the endogenous pre-training.

[111] p: Image Grounding. CoLoGen acquires precise intent localization capabilities for the Image Grounding task during endogenous pre-training. The visualization in Fig. 8 demonstrates that the model possesses robust object perception abilities and can accurately detect the referring instance, significantly enhancing its stability on complex tasks (e.g., instruction-based editing and customized generation).

[112] h2: Instructions for reporting errors

[113] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[114] p: Tip: You can select the relevant text first, to include it in your report.

[115] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[116] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
