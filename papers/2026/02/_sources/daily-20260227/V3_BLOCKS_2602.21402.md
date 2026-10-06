[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: FlowFixer: Towards Detail-Preserving Subject-Driven Generation

[3] h6: Abstract

[4] p: We present FlowFixer , a refinement framework for subject-driven generation (SDG) that restores fine details lost during generation caused by changes in scale and perspective of a subject. FlowFixer proposes direct image-to-image translation from visual references, avoiding ambiguities in language prompts. To enable image-to-image training, we introduce a one-step denoising scheme to generate self-supervised training data, which automatically removes high-frequency details while preserving global structure, effectively simulating real-world SDG errors. We further propose a keypoint matching-based metric to properly assess fidelity in details beyond semantic similarities usually measured by CLIP or DINO. Experimental results demonstrate that FlowFixer outperforms state-of-the-art SDG methods in both qualitative and quantitative evaluations, setting a new benchmark for high-fidelity subject-driven generation.

[5] h2: 1 Introduction

[6] p: Subject-driven generation (SDG) aims to embed a given subject (or an input reference image) into imagery described by an input text prompt while preserving the subject’s identity. SDG has received significant attention from the community since it has a number of practical applications, including advertising content generation, short-form content generation, and personalized media creation.

[7] p: Recent foundation models [ 31 , 7 ] have shown promising improvements in handling subjects with simpler textures ( e.g. , animals or plain objects) [ 39 , 40 , 46 , 47 , 45 ] . However, preserving complex product-specific details, such as logos, text, and intricate patterns, remains a critical challenge that demands greater attention from the community. This is particularly important for commercial applications where structural fidelity of product details directly impacts the utility of generated content. In advertising, for example, altered logos undermine brand recognition, and distorted text makes the outputs unusable.

[8] p: There are two key obstacles underlying this difficulty. First, collecting high-quality paired training data for SDG is challenging. Ideally, one would need pairs of subject images and diverse ground truth images containing the same subject to supervise both fidelity and compositional diversity. In practice, however, collecting such data at scale is highly challenging. To address this scarcity, Subjects200K [ 39 ] was introduced, yet it is constructed from synthetic images, which often lack fine-grained and realistic alignment of subject details.

[9] p: Second, existing conditioning mechanisms are often limited in specifying fine-grained geometric and appearance variations of the subject. Text descriptions such as ‘a red sports car’ or ‘a cereal box’ convey only coarse appearance and provide limited cues about pose, orientation, or lighting, making precise reproduction of subject details challenging [ 21 , 37 ] . Even with image-based conditioning (e.g., depth or edge maps), they tend to prioritize global scene coherence over localized detail alignment, which can lead to the loss of high-frequency information in texture-rich or geometrically complex regions [ 50 , 39 , 47 ] .

[10] p: To overcome these challenges, we propose FlowFixer, a novel refinement framework for detail-preserving SDG. Our approach employs a direct image-to-image translation pipeline that learns from visual references. This design choice circumvents the ambiguity inherent in natural language descriptions, enabling precise preservation of diverse visual elements and fine structural details across the image, as illustrated in Figure .

[11] p: At the core of FlowFixer is a self-supervised refinement scheme that leverages pseudo-paired training data. In principle, training a subject refinement framework requires triplets consisting of a clean subject image, a corresponding SDG-generated image, and its ideal ground-truth for refinement. However, collecting such paired data at scale is impractical due to the high cost of annotating subject-scene correspondences and generating controlled SDG outputs.

[12] p: Instead of collecting triplet data for training, we employ a self-supervised approach centered on our one-step denoising strategy. Starting with a clean real image, we synthetically generate its degraded counterpart through a forward diffusion step followed by single-step denoising using an off-the-shelf diffusion model. This process closely mimics SDG artifacts and characteristic distortions, allowing FlowFixer to learn fine detail restoration without expensive human supervision. The resulting framework enables efficient training using web-collected single images while faithfully representing the high-frequency detail loss typical in SDG applications.

[13] p: Current quantitative evaluation metrics for SDG results have distinct characteristics and constraints. For example, pixel-level similarity measures (e.g., MSE or SSIM) focus primarily on low-level differences, while semantic-level metrics (e.g., FID [ 12 ] or LPIPS [ 51 ] ) may not fully capture fine details. Moreover, many existing metrics require ground truth images, which are often unavailable in real-world generative applications. To overcome these limitations, we propose detail-aware evaluation metrics based on keypoint matching [ 15 , 22 ] ; absolute keypoint increase and keypoint matching gain. These metrics effectively capture structural fidelity by measuring the consistency between a reference image and its generated output, enabling ground-truth-free quantitative evaluation of detail preservation in open-world generative settings. Together with human and VLM evaluation, our metrics provide reliable and reproducible assessments of fine-grained fidelity.

[14] figure: Figure 2 : FlowFixer overview. FlowFixer enhances SDG images by restoring fine subject details, using the original subject image as reference.

[15] p: Through extensive experiments, we demonstrate that FlowFixer consistently outperforms existing SDG methods in preserving subject identity, establishing a new baseline for high-fidelity SDG. The key contributions of this work are summarized as follows:

[16] p: A novel model-agnostic refinement framework, FlowFixer, that substantially enhances subject fidelity in SDG-generated images.

[17] p: An efficient training data curation pipeline based on one-step denoising, which effectively simulates diffusion artifacts to generate high-quality pseudo-paired training data.

[18] p: A direct visual translation approach that leverages reference images, enabling precise preservation of visual elements and fine-grained details while eliminating prompt-induced ambiguity.

[19] p: A novel ground-truth-free evaluation metric to assess visual fidelity based on keypoint matching, which demonstrates FlowFixer’s superior detail preservation capability compared to existing SDG methods.

[20] h2: 2 Related Work

[21] p: Subject-driven generation has received significant attention from the community and builds directly on top of the success of text-to-image foundational diffusion models [ 36 , 20 , 19 ] . While text-to-image models can generate high quality objects, subject driven generation requires faithful rendering of the “subject” (i.e, preserving the identity in the subject image) in a variety of scenes.

[22] p: Techniques for subject driven generation have broadly followed two main directions (a) fine-tuning-based and (b) encoder-based. Early approaches such as DreamBooth [ 37 ] , Textual Inversion [ 8 ] , and LoRA [ 14 ] in Custom Diffusion [ 18 ] adapt pre-trained text-to-image diffusion models to specific subjects using only a few reference images (typically 3 to 5), achieving strong identity preservation but require expensive per-subject fine-tuning. More recent works avoid per-subject finetuning and address the limitation by injecting the reference image of the subject through an encoder directly into the diffusion backbone. For example, IP-Adapter [ 48 ] injects image-prompt features via decoupled cross-attention to enable subject conditioning without fine-tuning, while BLIP-Diffusion [ 21 ] learns a multi-modal subject encoder for tighter subject–prompt alignment. OminiControl [ 39 ] further shows that a DiT backbone can encode references natively with minimal additional parameters.

[23] p: However, these encoder-based approaches, while good at preserving high-level details, struggle to preserve the subject’s fine structural details, rendering the synthesized images unusable for real-world applications. In contrast, FlowFixer restores missing low-level details to ensure high-fidelity identity preservation. It employs a reference-guided diffusion refinement process that corrects structural inconsistencies in a generated SDG image by conditioning on the original subject image, as illustrated in Figure 2 . This “last mile” refinement makes FlowFixer universally compatible, enhancing identity preservation for any upstream model.

[24] p: Another line of work that is relevant for subject driven image generation is based on image editing, which focuses on modifying an existing image under additional conditions such as text prompts, reference images, or spatial masks [ 50 , 27 ] . Existing methods generally fall into two categories: global and local editing. Global editing techniques alter overall image appearance or semantic content through text-based manipulation or latent space interpolation [ 11 , 16 , 25 , 17 , 29 , 30 , 4 , 3 , 42 ] . On the other hand, methods for local editing target specific spatial regions via mask-based selection [ 24 ] , blending [ 1 ] , or exemplars [ 9 ] . Although effective for coarse transformations, these approaches often fail to preserve fine structural details of the subject and typically require manual inputs such as masks or region-specific prompts [ 6 , 44 , 49 , 53 ] . Recent works further reveal that text-driven editors struggle with localized or fine-grained control due to ambiguous conditioning and conflicting attention dynamics [ 52 , 26 , 10 , 41 , 34 ] .

[25] p: In contrast, FlowFixer performs automatic, reference-guided refinement without requiring manual annotations or textual conditioning. By leveraging cross-image correspondences between the generated and reference images, FlowFixer restores degraded regions while preserving global scene coherence and sharp, subject-consistent details. To further encourage the model to focus on subjects, the proposed FlowFixer exploits automatic subject cropping based on keypoint matching between a subject image and its SDG image.

[26] figure: Figure 3 : FlowFixer inference pipeline. The model takes two conditional inputs: reference subject image 𝐈 ref {\mathbf{I}}_{\text{ref}} and the generated image 𝐈 gen {\mathbf{I}}_{\text{gen}} from any SDG model. Then the model produces a refined result 𝐈 ^ gen \widehat{{\mathbf{I}}}_{\text{gen}} that preserves global layout. For faster inference, we optionally refine only a subject-centric crop of 𝐈 gen {\mathbf{I}}_{\text{gen}} and blend it back using Poisson image blending.

[27] h2: 3 Method

[28] h3: 3.1 Diffusion preliminaries

[29] p: Diffusion models are probabilistic generative frameworks that progressively transform a simple prior p s p_{s} ( e.g. , Gaussian noise) into samples from a target distribution p t p_{t} through iterative denoising or continuous flows. Let 𝐱 t {\mathbf{x}}_{t} (or 𝐳 t {\mathbf{z}}_{t} in latent diffusion) denote the state at time t ∈ [ 0 , 1 ] t\in[0,1] along this trajectory. The generative process starts from noise and can be formally expressed as

[30] table: 𝐱 1 ∼ p s , 𝐱 0 = 𝒟 ⁡ ( 𝐱 1 ) ∼ p t , {\mathbf{x}}_{1}\sim p_{s},\qquad{\mathbf{x}}_{0}=\mathcal{D}({\mathbf{x}}_{1})\sim p_{t}, (1)

[31] p: where 𝒟 \mathcal{D} represents a learned denoising or flow-matching process [ 13 , 38 , 23 ] . A key property of diffusion models is their conditioning flexibility:

[32] table: 𝐱 0 = 𝒟 ⁡ ( 𝐱 1 , 𝐜 ) , {\mathbf{x}}_{0}=\mathcal{D}({\mathbf{x}}_{1},\mathbf{c}), (2)

[33] p: where 𝐜 \mathbf{c} denotes auxiliary controls such as text prompts or reference images. In latent diffusion models [ 36 , 20 ] , 𝐱 t {\mathbf{x}}_{t} corresponds to a latent variable 𝐳 t {\mathbf{z}}_{t} encoded by a VAE ℰ \mathcal{E} , and the final image is reconstructed from the latent sample 𝐳 1 {\mathbf{z}}_{1} . Diffusion models have achieved highly realistic and semantically coherent image generation, driven by large-scale architectures and training on massive, diverse datasets.

[34] h3: 3.2 Problem formulation

[35] p: Subject-driven generation (SDG) can be viewed as a specific instance of conditional diffusion in Eq. 2 . Given a subject reference image 𝐈 ref {\mathbf{I}}_{\text{ref}} and a textual description 𝐜 text \mathbf{c}_{\text{text}} , an SDG model 𝒟 SDG \mathcal{D}_{\text{SDG}} generates a novel scenic image 𝐈 gen {\mathbf{I}}_{\text{gen}} conditioned on both inputs:

[36] table: 𝐈 gen = 𝒟 SDG ​ ( 𝐳 1 , 𝐈 ref , 𝐜 text ) , 𝐳 1 ∼ p s , {\mathbf{I}}_{\text{gen}}=\mathcal{D}_{\text{SDG}}({\mathbf{z}}_{1},{\mathbf{I}}_{\text{ref}},\mathbf{c}_{\text{text}}),\qquad{\mathbf{z}}_{1}\sim p_{s}, (3)

[37] p: where 𝐜 text \mathbf{c}_{\text{text}} provides high-level semantics and 𝐈 ref {\mathbf{I}}_{\text{ref}} encodes subject appearance cues.

[38] p: While diffusion models achieve strong global realism and semantic consistency, text-conditioned variants often prioritize global coherence over local structural fidelity. This limitation stems from the ambiguity of textual conditioning, which captures broad semantics but lacks precise visual cues such as small textures or logos. As a result, diffusion models tend to favor perceptual plausibility at the expense of subject-specific details [ 52 , 26 , 10 , 41 , 34 ] . Despite notable progress in large-scale foundation models—including Qwen [ 2 ] , FLUX.1-Kontext [ 19 ] , and Nano Banana [ 5 ] —fine-grained subject fidelity remains a persistent challenge.

[39] p: To address this, we design a text-free diffusion-based refiner 𝒟 refine \mathcal{D}_{\text{refine}} that re-generates 𝐈 gen {\mathbf{I}}_{\text{gen}} under the guidance of 𝐈 ref {\mathbf{I}}_{\text{ref}} through a conditional diffusion process starting from latent noise 𝐳 1 ∼ p s {\mathbf{z}}_{1}\sim p_{s} as follows,

[40] table: 𝐈 ^ gen = 𝒟 refine ​ ( 𝐳 1 , 𝐈 gen , 𝐈 ref ) . \widehat{{\mathbf{I}}}_{\text{gen}}=\mathcal{D}_{\text{refine}}({\mathbf{z}}_{1},{\mathbf{I}}_{\text{gen}},{\mathbf{I}}_{\text{ref}}). (4)

[41] p: Here, 𝐈 ^ gen \widehat{{\mathbf{I}}}_{\text{gen}} preserves the global layout of 𝐈 gen {\mathbf{I}}_{\text{gen}} while restoring subject-consistent details from 𝐈 ref {\mathbf{I}}_{\text{ref}} . Unlike conventional inpainting methods that rely on explicit masks or user interaction, Eq. 4 denotes fully automatic refinement without external inputs. Furthermore, 𝒟 refine \mathcal{D}_{\text{refine}} is optimized with self-supervised pseudo pairs, enabling scalable and annotation-free enhancement beyond mask-based editing. We refer to this refiner as FlowFixer , reflecting its ability to restore fine structural consistency by correcting disrupted feature flow between 𝐈 gen {\mathbf{I}}_{\text{gen}} and 𝐈 ref {\mathbf{I}}_{\text{ref}} .

[42] figure: Figure 4 : Example of one-step denoising distortions. For each distortion level, pixel-wise variance maps are computed over 10 degraded samples. Insets show example outputs, with distortions concentrated in high-frequency regions.

[43] h3: 3.3 Pseudo-paired training data

[44] p: A key challenge in training 𝒟 refine \mathcal{D}_{\text{refine}} is the lack of paired data where only subject details are degraded while global structure remains unchanged. To address this, we construct pseudo pairs ( 𝐈 degraded , 𝐈 clean ) ({\mathbf{I}}_{\text{degraded}},{\mathbf{I}}_{\text{clean}}) from real images by mocking SDG’s degradation using a one-step denoising process as follows:

[45] p: Start from a clean real image 𝐈 clean {\mathbf{I}}_{\text{clean}} .

[46] p: Add noise to 𝐈 clean {\mathbf{I}}_{\text{clean}} and apply a single-step denoising using an off-the-shelf diffusion model [ 33 ] .

[47] p: Control the degradation level by downscaling 𝐈 clean {\mathbf{I}}_{\text{clean}} to 1.0 × 1.0\times , 0.5 × 0.5\times , or 0.25 × 0.25\times its original resolution before VAE encoding.

[48] p: To verify that this process mainly affects fine details, we generate 10 variants with different random seeds in step 2 and compute per-pixel variance maps across them. As shown in Figure 4 , the variance concentrates in high-frequency regions while remaining low in smooth backgrounds, confirming that the perturbation minimally disturbs global structure. For step 2, we use SDXL [ 33 ] .

[49] p: During training, we treat 𝐈 degraded {\mathbf{I}}_{\text{degraded}} as the generated input 𝐈 gen {\mathbf{I}}_{\text{gen}} in Eq. 4 . The reference 𝐈 ref {\mathbf{I}}_{\text{ref}} is a spatially perturbed version of the clean image 𝐈 clean {\mathbf{I}}_{\text{clean}} , created through random cropping, rotation, or mild color augmentation—and vice versa for data diversity. This setup enables 𝒟 refine \mathcal{D}_{\text{refine}} to focus on recovering fine details by learning local correspondences between 𝐈 degraded {\mathbf{I}}_{\text{degraded}} and 𝐈 ref {\mathbf{I}}_{\text{ref}} , without depending on strict pixel-wise alignment.

[50] h3: 3.4 Training pipeline

[51] h4: Network architecture.

[52] p: FlowFixer builds on FLUX.1-Kontext [ 19 ] to leverage image-native editing capability. For a text-free pipeline, we discard the original text token and introduce an additional image input, as illustrated in Figure 3 . Consequently, FlowFixer takes three inputs, 𝐳 1 {\mathbf{z}}_{1} , 𝐈 gen {\mathbf{I}}_{\text{gen}} , and 𝐈 ref {\mathbf{I}}_{\text{ref}} . The images 𝐈 gen {\mathbf{I}}_{\text{gen}} and 𝐈 ref {\mathbf{I}}_{\text{ref}} are encoded by the pretrained VAE into latent tokens, which are concatenated with 𝐳 1 {\mathbf{z}}_{1} before being processed by the DiT backbone. We adopt 3D RoPE with per-stream timestep offsets ( 0 0 for 𝐳 1 {\mathbf{z}}_{1} , 1 1 for 𝐈 gen {\mathbf{I}}_{\text{gen}} , 2 2 for 𝐈 ref {\mathbf{I}}_{\text{ref}} ), to maintain stream separation while allowing full cross-attention.

[53] p: To discover dense correspondences between 𝐈 gen {\mathbf{I}}_{\text{gen}} and 𝐈 ref {\mathbf{I}}_{\text{ref}} , we adopt an explicit dual-stream conditioning mechanism operating in a shared spatial space. This design enforces alignment between the two inputs and facilitates localized refinements guided by the reference. The alignment is further strengthened by our self-supervised, pseudo-paired training scheme.

[54] h4: Implementation details.

[55] p: We fine-tune FLUX.1-Kontext using LoRA [ 14 ] with rank 192, specializing the model for automatic refinement while keeping the parameter overhead minimal. Training is conducted for 50K iterations with a batch size of 4. For each iteration, a pseudo training pair ( 𝐈 degraded , 𝐈 clean ) ({\mathbf{I}}_{\text{degraded}},{\mathbf{I}}_{\text{clean}}) is sampled as described in Sec. 3.3 . One degraded variant is randomly selected from the three downscaling levels ( 1.0 × 1.0\times , 0.5 × 0.5\times , 0.25 × 0.25\times ) to ensure balanced degradation diversity. The model is trained using a mean squared error (MSE) loss between the refined output and the clean target. We use a guidance scale of 1.0 during training and 2.5 at inference, respectively.

[56] p: We use 18,450 high-quality real-world photographs from Unsplash [ 43 ] to construct the pseudo pairs for training. The images span diverse objects, materials, and lighting conditions, providing sufficient visual diversity for self-supervised refinement.

[57] h3: 3.5 Crop-based refinement

[58] p: While high-resolution generation is critical for subject fidelity, a full-resolution global pass incurs substantial latency and memory cost. Instead, FlowFixer preserves the background layout while selectively restoring subject details, enabling crop-based refinement during inference, as illustrated in Figure 3 . We first determine a subject-centric crop using keypoint matching [ 15 ] between a subject and its generated image, and then refine only this region and paste the result back into the original image. Since the global structure remains unchanged and only fine details are corrected, simple image-domain blending ( e.g. , Poisson blending) achieves seamless integration without user-defined masks or inversion. This substantially reduces runtime and memory while retaining subject-level fidelity.

[59] figure: Table 1 : Refinement performance on the FidelityBench-258K. For all metrics, higher numbers indicate better performance. Method FLUX.1-Kontext-Pro Qwen-Image-Edit Nano-Banana-Edit AKI ↑ \uparrow 𝒦 Gain \mathcal{K}_{\text{Gain}} ↑ \uparrow CLIP-I ↑ \uparrow DINO ↑ \uparrow AKI ↑ \uparrow 𝒦 Gain \mathcal{K}_{\text{Gain}} ↑ \uparrow CLIP-I ↑ \uparrow DINO ↑ \uparrow AKI ↑ \uparrow 𝒦 Gain \mathcal{K}_{\text{Gain}} ↑ \uparrow CLIP-I ↑ \uparrow DINO ↑ \uparrow Baseline - - 0.776 0.663 - - 0.777 0.668 - - 0.796 0.711 Text-based editing [ 19 ] 7.5 52.7% 0.763 0.647 11.1 54.1% 0.762 0.647 61.7 77.0% 0.782 0.691 OminiControl [ 39 ] + F-Dev 29.0 53.9% 0.724 0.551 0.48 43.8% 0.724 0.552 108.0 70.7% 0.747 0.605 OminiControl [ 39 ] + F-Kontext 0.49 45.7% 0.766 0.649 -3.37 46.8% 0.765 0.649 53.0 56.6% 0.786 0.696 FlowFixer (ours) 66.5 77.9% 0.778 0.668 54.0 74.8% 0.777 0.668 64.7 79.2% 0.796 0.711

[60] figure: Figure 5 : Qualitative comparison on Subject fidelity refinement on the FidelityBench-258K dataset. The insets in the full images show the reference subject images and the red and green boxes indicate the zoomed-in regions. The regions for zoomed-in views are found on the SDG baseline images and cropped the same area for all methods.

[61] h2: 4 Detail-aware Evaluation

[62] h3: 4.1 Evaluation metric

[63] p: While widely used, existing perceptual metrics fall short in evaluating fine-grained details. Common similarity measures, such as CLIP [ 35 ] or DINOv2 [ 28 ] primarily capture global semantics and overlook high-frequency fidelity, making them unsuitable for assessing detail consistency.

[64] p: To better quantify subject fidelity, we exploit keypoint matching that finds dense correspondences between the reference and generated images. This approach is based on the observation that images with better subject fidelity yield a higher number of matched keypoints. We define two metrics: i) absolute keypoint increase (AKI) and ii) keypoint matching gain 𝒦 Gain \mathcal{K}_{\text{Gain}} . First, we formulate AKI by

[65] table: AKI = 𝒩 ⁡ ( ℳ ⁡ ( 𝐈 ref , 𝐈 ^ gen ) ) − 𝒩 ⁡ ( ℳ ⁡ ( 𝐈 ref , 𝐈 gen ) ) , \text{AKI}=\mathcal{N}(\mathcal{M}{}({\mathbf{I}}_{\text{ref}},\widehat{{\mathbf{I}}}_{\text{gen}}))-\mathcal{N}(\mathcal{M}{}({\mathbf{I}}_{\text{ref}},{\mathbf{I}}_{\text{gen}})), (5)

[66] p: where 𝒩 ⁡ ( ℳ ⁡ ( a , b ) ) \mathcal{N}(\mathcal{M}{}(a,b)) denotes the number of matched keypoints between a a and b b using the keypoint matching network ℳ \mathcal{M}{} . A higher AKI score indicates stronger preservation of subject-specific fine details and structural alignment.

[67] p: While AKI effectively quantifies instance-level improvements, its absolute values depend on the choice and calibration of the keypoint matcher, and thus are not strictly comparable across settings. Moreover, when averaged over a large set, many small yet consistent improvements can be diluted by a few large changes, obscuring the overall trend. Therefore, we also calculate the keypoint matching gain, 𝒦 Gain \mathcal{K}_{\text{Gain}} , which averages the fraction of cases that improve. Formally, we define

[68] table: 𝒦 Gain = 1 N ​ ∑ i = 1 N δ ⁡ ( AKI i , τ ) \mathcal{K}_{\text{Gain}}=\frac{1}{N}\sum_{i=1}^{N}\delta(\text{AKI}_{i},\tau) (6)

[69] p: where δ \delta is a binary indicator function that becomes 1 when AKI i \text{AKI}_{i} is higher than τ \tau and 0 otherwise. AKI i \text{AKI}_{i} is an AKI score of i i -th image sample in a dataset. We report 𝒦 Gain \mathcal{K}_{\text{Gain}} in percentage and set τ = 0 \tau{=}0 as default. These metrics effectively capture enhancement of local fidelity. For evaluation, we employ an off-the-shelf keypoint matching network, OmniGlue [ 15 ] .

[70] h3: 4.2 Evaluation dataset

[71] p: Existing SDG benchmarks [ 37 , 32 ] primarily focus on global realism and semantic alignment rather than preserving fine-grained subject fidelity. As a result, their subject categories are often visually simple and contain limited texture or detail ( e.g. , rubber ducks, plants, or cartoon figures). To achieve rigorous evaluation of subject fidelity, we introduce FidelityBench-258K , a large-scale, subject-diverse benchmark structured by subject–prompt pairs. To construct the dataset, we first collected 29K subject images and generated prompts for SDG using a vision-language model (VLM), Claude 3.5. For each prompt-subject pair, we generated five variants per SDG baseline. We used three SDG baselines (FLUX.1-Kontext-Pro [ 19 ] , Qwen-Image-Edit [ 2 ] , and Nano Banana-Edit [ 5 ] ), which led to 435K SDG images in total. Finally, we applied a coarse quality filter to ensure that the subject is clearly present in the SDG image. After the filtering, the final dataset consists of 258K subject - SDG image pairs.

[72] p: For controlled and reproducible studies, we also curate a fixed subset, FidelityBench-300 from the FidelityBench-258K dataset, collecting 100 images from each backbone. FidelityBench-300 preserves the distribution of baseline match counts while balancing categories, and we reuse this fixed subset for all ablations and human evaluations to ensure comparability and reproducibility.

[73] h2: 5 Experiments

[74] h3: 5.1 Subject fidelity refinement

[75] p: Table 1 reports refinement results on FidelityBench-258K dataset under the three SDG baselines ( i.e. , FLUX.1-Kontext-Pro, Qwen-Image-Edit, and Nano-Banana-Edit). In Table 1 , we compare four different refinement models, including the proposed FlowFixer. The compared refinement models are:

[76] p: Text-based editing: FLUX.1-Kontext, which is a text-based editing model, accepting the subject and SDG images concatenated on the x-axis while refinement is guided by an input prompt.

[77] p: OminiControl + FLUX.1 (Dev/Kontext): OminiControl [ 39 ] fine-tuned on FLUX.1-Dev and FLUX.1-Kontext, respectively, using our pseudo-paired dataset. We use the same training data as FlowFixer.

[78] p: Since there is no algorithm tailored for refinement of SDG, we finetuned OminiControl [ 39 ] with state-of-the-art backbones [ 20 , 19 ] , which can accept a subject as a conditional input, and used the text-based editing method [ 19 ] for benchmarking.

[79] p: Note that AKI and 𝒦 Gain \mathcal{K}_{\text{Gain}} are not obtainable for the baselines since these metrics quantify the changes relative to the baseline’s SDG output. We additionally report CLIP-Image (CLIP-I) and DINOv2 similarity as complementary perceptual metrics. To isolate subject fidelity from background content, similarities are computed only on the subject regions by detecting the bounding box of the subject.

[80] p: We summarize our statistical and empirical findings from Table 1 and Figure 5 as follows:

[81] p: As illustrated in Figure 5 , FlowFixer restores fine details of the subject while preserving the original image layout. In contrast, the other refinement models either shift the scene or fail to improve local structure. For example, ‘Text-based editing’ often maintains semantics but alters composition, undermining subject consistency. In contrast, FlowFixer avoids such layout drift while increasing local correspondences.

[82] p: Quantitatively, across all SDG backbones, FlowFixer consistently outperforms its alternatives in AKI and achieves an average 𝒦 Gain \mathcal{K}_{\text{Gain}} of 77.3%, demonstrating model-agnostic robustness.

[83] p: Interestingly, these keypoint-based gains are not reflected in CLIP-I or DINOv2 scores, which remain nearly unchanged. This indicates that common perceptual metrics overlook fine-grained structural fidelity, reinforcing the need for specialized metrics like AKI and 𝒦 Gain \mathcal{K}_{\text{Gain}} .

[84] p: While alternative fine-tuned models (OminiControl + FLUX.1-Dev and Kontext) occasionally increase AKI, their 𝒦 Gain \mathcal{K}_{\text{Gain}} often drops below 50%, meaning such methods show no consistent pattern of improvement.

[85] p: On Nano Banana, certain methods achieve inflated keypoint metrics by copy-pasting the subject or synthesizing a new scene with larger subject rather than refining the given output. This results in the elevated AKI scores but reduced global consistency, as reflected in the lower CLIP-I and DINOv2 similarities on cropped subject regions.

[86] p: Figure 6 shows scatter plots of keypoint changes before and after refinement on FidelityBench-300. Among all methods, only FlowFixer reveals a consistent and directional pattern, reliably increasing the number of matched keypoints (AKI) across most samples. In contrast, alternative methods exhibit no clear trend, with improvements occurring sporadically and often accompanied by regressions. This further highlights the robustness and generalizability of FlowFixer’s refinements.

[87] figure: Table 2 : Refinement performance compared to original SDG images on the FidelityBench-300. For all metrics, higher numbers indicate better performance. Method AKI ↑ \uparrow 𝒦 Gain \mathcal{K}_{\text{Gain}} ↑ \uparrow VLM ↑ \uparrow Text-based editing [ 19 ] 1.87 45.9% 41.3% OminiControl [ 39 ] + F-Dev 22.7 46.6% 4.2% OminiControl [ 39 ] + F-Kontext 11.1 38.4% 25.2% FlowFixer (ours) 67.3 91.2% 79.0%

[88] figure: Figure 6 : Scatter plots of the number of keypoint matches on FidelityBench-300. Each dot represents a sample; points above the red dashed line indicate an increase in keypoint matches (positive AKI, green region), suggesting improved structural alignment and subject fidelity. Samples below the line show decreased correspondence after refinement.

[89] figure: Figure 7 : A/B study results comparing the FlowFixer against four alternatives. FlowFixer is consistently preferred by human raters.

[90] h3: 5.2 Human Evaluation and VLM Judgment

[91] p: To assess how well our metrics reflect human perception, we conducted an A/B tests on the FidelityBench-300 subset using Amazon Mechanical Turk. For each test case, human evaluators were shown the reference subject alongside two candidate images, i.e. , FlowFixer vs. one alternative method. Then, we asked the evaluators to choose the one that better preserves subject-specific details. Each pair was evaluated by five independent evaluators, and responses were aggregated across the dataset.

[92] p: Figure 7 shows that the human evaluators strongly prefer FlowFixer over the baseline and the other refinement methods, which align with our proposed metrics, AKI and 𝒦 Gain \mathcal{K}_{\text{Gain}} . Notably, FlowFixer’s advantages over the baseline and the text-based editing [ 19 ] are comparable (64.9% and 64.4%), suggesting that a text prompt for editing only makes a negligible difference in terms of subject fidelity. Moreover, FlowFixer is favored over OminiControl variants [ 39 ] by even larger margins (92.7% and 77.2%).

[93] p: In addition to the human evaluation, we also evaluate metric agreement with a Vision-Language Model (VLM), Claude 3.7, serving as an automated judge. For each case, the VLM receives the reference image and two subject-region crops (Baseline vs. one alternative). To mitigate order bias, we present two images in both A/B and B/A orders and average the decisions.

[94] p: As shown in Table 2 , VLM judges FlowFixer to be the best restoration method in terms of subject fidelity. In addition to that, VLM judgments exhibit strong alignment with AKI and 𝒦 Gain \mathcal{K}_{\text{Gain}} , cross-validating their effectiveness in capturing perceptual improvements in subject fidelity.

[95] figure: Figure 8 : Impact of training distortion levels on refinement performance. Using a range of distortion levels during training enhances the model’s ability to handle diverse degradation at inference time, resulting in more robust restoration.

[96] figure: Figure 9 : Efficacy of cropped refinement in comparison with full image refinement. While full image refinement moderately enhances subject fidelity, cropping further improves legibility.

[97] h3: 5.3 Distortion levels for training

[98] p: To assess the impact of degradation diversity during training, we compare FlowFixer models trained with different subsets of distortion levels: (i) only slight noise ( 1.0 × 1.0\times ), (ii) moderate and slight noise ( 1.0 × 1.0\times , 0.5 × 0.5\times ), and (iii) the full range ( 1.0 × 1.0\times , 0.5 × 0.5\times , 0.25 × 0.25\times ). As illustrated in Figure 8 , including various levels of distortion during training significantly boosts robustness, especially under large-scale artifacts, highlighting the importance of diverse degradation simulation for effective refinement.

[99] h3: 5.4 Crop-based refinement

[100] p: Figure 9 compares a single global refinement pass against our crop-based refinement strategy. In both cases, the global scene composition remains unchanged, highlighting FlowFixer’s inherent stability with respect to layout drift. Notably, even under the same evaluation resolution, crop-based refinement yields more accurate recovery of fine-grained subject details, thanks to its focused and localized processing. This allows better fidelity in details without compromising global coherence.

[101] h2: 6 Conclusion

[102] p: We introduced FlowFixer, a model-agnostic detail refiner for subject-driven generation that recovers fine structural details while preserving global layout. Trained on self-supervised pseudo pairs simulating high-frequency degradation, FlowFixer scales to in-the-wild references without paired subject–scene data. Our text-free, direct image-to-image formulation avoid prompt ambiguity and consistently improve fidelity. Paired with keypoint-matching-based metrics for ground-truth-free evaluation, FlowFixer demonstrates superior performance across diverse SDG methods. Future directions include (i) multi-reference refinement that leverages multiple reference images, and (ii) user-interactive correction using auxiliary control signals, such as scribble masks.

[103] h2: References

[104] h2: Instructions for reporting errors

[105] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[106] p: Tip: You can select the relevant text first, to include it in your report.

[107] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[108] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
