[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: CADC: Content Adaptive Diffusion-Based Generative Image Compression

[3] h6: Abstract

[4] p: Diffusion-based generative image compression has demonstrated remarkable potential for achieving realistic reconstruction at ultra-low bitrates. The key to unlocking this potential lies in making the entire compression process content-adaptive, ensuring that the encoder’s representation and the decoder’s generative prior are dynamically aligned with the semantic and structural characteristics of the input image. However, existing methods suffer from three critical limitations that prevent effective content adaptation. First, isotropic quantization applies a uniform quantization step, failing to adapt to the spatially varying complexity of image content and creating a misalignment with the diffusion model’s noise-dependent prior. Second, the information concentration bottleneck—arising from the dimensional mismatch between the high-dimensional noisy latent and the diffusion decoder’s fixed input—prevents the model from adaptively preserving essential semantic information in the primary channels. Third, existing textual conditioning strategies either need significant textual bitrate overhead or rely on generic, content-agnostic textual prompts, thereby failing to provide adaptive semantic guidance efficiently. To overcome these limitations, we propose a content-adaptive diffusion-based image codec (CADC) with three technical innovations: 1) an Uncertainty-Guided Adaptive Quantization (UGAQ) method that learns spatial uncertainty maps to adaptively align quantization distortion with content characteristics; 2) an Auxiliary Decoder-Guided Information Concentration (ADGIC) method that uses a lightweight auxiliary decoder to enforce content-aware information preservation in the primary latent channels; and 3) a Bitrate-Free Adaptive Textual Conditioning (BFATC) method that derives content-aware textual descriptions from the auxiliary reconstructed image, enabling semantic guidance without bitrate cost. Comprehensive experimental results show that our codec achieves state-of-the-art perceptual quality at ultra-low bitrates.

[5] figure: Figure 1 : A qualitative comparison between our codec, StableCodec [ 65 ] , and DLF [ 59 ] when compressing a 2K-resolution image of the test set of CLIC 2020 Professional [ 57 ] under ultra-low bitrate conditions. Our codec produces images with high visual quality, especially in regions with complex texture. In contrast, DLF and StableCodec exhibit noticeable artifacts, such as blurring and color shifting.

[6] h2: 1 Introduction

[7] p: Digital images account for a substantial portion of internet traffic, driving continuous demand for efficient compression technologies that reduce storage and transmission costs while maintaining visual quality. Traditional image codecs [ 58 , 54 , 56 , 9 ] have been widely adopted for decades. To pursue higher compression performance, learned image compression [ 6 , 13 , 16 , 66 , 42 , 41 , 1 , 22 , 3 , 19 , 7 , 44 , 45 , 24 , 23 , 17 , 27 , 48 , 32 ] has emerged in recent years. However, at ultra-low bitrates, even state-of-the-art learned image codecs tend to produce reconstructions plagued by blurring and loss of fine details, as they primarily optimize for pixel-level signal fidelity rather than perceptual quality [ 8 ] .

[8] p: Generative image compression addresses this limitation by leveraging strong generative models to produce visually realistic reconstructions. Existing generative image codecs can be broadly categorized into three classes: Generative Adversarial Network (GAN)-based codecs [ 43 , 2 , 37 , 5 , 11 ] , which employ adversarial training [ 20 ] to enhance visual quality; vector quantization (VQ)-based codecs [ 60 , 26 , 47 ] , which learn discrete representations for efficient compression; and diffusion-based codecs [ 10 , 18 , 65 , 60 , 51 , 50 , 39 , 38 , 28 , 30 ] , which utilize diffusion denoising to reconstruct images. While GAN-based and vector quantization codecs have shown promising results, their generative capabilities remain inherently constrained. In contrast, diffusion-based codecs—benefiting from the exceptional generative capacity of diffusion models—have recently achieved remarkable performance, particularly under ultra-low bitrate conditions.

[9] p: Despite these advances, we identify three fundamental limitations in current diffusion-based image codecs that prevent them from achieving effective content adaptation, which is crucial for optimally leveraging generative priors across diverse image structures and semantics. First, the prevalent use of isotropic quantization applies a uniform quantization step across the compact latent representation, ignoring the spatial heterogeneity of image content. This content-agnostic quantization creates a mismatch with the diffusion model’s noise-dependent prior: textured regions receive insufficient generative intervention while smooth regions are over-regularized, limiting the overall rate-perception performance. Second, these codecs suffer from an information concentration bottleneck caused by the architectural mismatch between the high-dimensional noisy latent and the fixed 4-channel input of the pre-trained diffusion decoder [ 52 ] . Without explicit supervision, the model may fail to concentrate essential semantic information into the primary channels, leading to a non-adaptive latent representation that does not prioritize critical content. Third, existing methods struggle with ineffective textual conditioning : they either incur substantial bitrate overhead by transmitting textual side information or rely on generic prompts that lack content relevance, failing to provide content-adaptive textual guidance without bitrate costs.

[10] p: To tackle the aforementioned limitations and establish a content-adaptive diffusion-based image codec, we introduce three technical innovations that address the identified limitations. First, we propose an Uncertainty-Guided Adaptive Quantization (UGAQ) method that fundamentally redesigns the quantization process. Our key innovation lies in learning a spatially-varying uncertainty map from the residual between the main latent representation and the upsampled hyperprior latent. This uncertainty map modulates the quantization noise level across different spatial locations, ensuring that textured regions receive stronger generative intervention while smooth regions maintain structural fidelity. This method effectively aligns the quantization-induced distortion with the diffusion model’s noise-dependent denoising strategy, enabling content-aware noise shaping. Second, we develop an Auxiliary Decoder-Guided Information Concentration (ADGIC) method that explicitly solves the information concentration bottleneck. We introduce a lightweight auxiliary decoder that operates exclusively on the first four channels of the noisy latent, producing an auxiliary reconstruction and computing its distortion against the original image. This design forces the compression model to concentrate semantically critical information into the primary channels used by the diffusion decoder, ensuring that the essential visual content is properly preserved and accessible to the generative prior, thereby enforcing a content-driven information allocation. Third, we design a Bitrate-Free Adaptive Textual Conditioning (BFATC) method that enables effective textual conditioning without textual bitrate overhead. We generate content-adaptive captions using a pre-trained BLIP model [ 36 ] from the auxiliary reconstruction image, providing semantically meaningful guidance to the diffusion process while requiring zero additional textual bitrate, effectively bridging the gap between conditioning quality and bitrate efficiency and achieving dynamic, content-specific conditioning.

[11] p: In summary, our contributions are as follows:

[12] p: We identify three key limitations in current diffusion-based image codecs that hinder content adaptation: i) the mismatch from content-agnostic isotropic quantization, ii) the non-adaptive latent representation due to the information concentration bottleneck, and iii) the inability to provide content-aware textual guidance efficiently.

[13] p: We propose three novel methods that collectively establish a content-adaptive diffusion-based image codec: Uncertainty-Guided Adaptive Quantization for content-aware noise shaping, Auxiliary Decoder-Guided Information Concentration for content-driven information allocation, and Bitrate-Free Adaptive Textual Conditioning for content-specific semantic guidance.

[14] p: We validate our codec across various datasets and evaluation criteria, showing improved quantitative and qualitative results, particularly at ultra-low bitrates.

[15] h2: 2 Related Work

[16] h3: 2.1 Learned Image Compression

[17] p: Learned image compression has gained significant research interest in recent years. Mosts methods typically build upon three core components: non-linear transforms, quantization, and entropy models. Early work by Ballé et al . [ 6 ] established a foundational framework using convolutional networks with generalized divisive normalization (GDN) for non-linear analysis and synthesis transforms. To enable gradient-based training, they approximated quantization with additive uniform noise during optimization, combined with a factorized entropy model. Subsequent efforts have focused on enhancing each of these components. For transform design, attention mechanisms [ 13 , 16 ] and transformer architectures [ 66 , 42 , 41 ] have been incorporated to better capture both global structures and local textures. For quantization, several alternatives have been proposed to improve quantizer differentiability and efficiency while maintaining inference-time discretization, including soft-to-hard quantization [ 1 ] , soft-then-hard quantization [ 22 ] , universal quantization [ 3 ] , and non-uniform quantization [ 19 ] . Entropy modeling has also seen considerable advances. Early hyperprior models [ 7 ] introduced side information to capture spatial dependencies, while autoregressive model [ 44 ] further improved accuracy through spatial conditioning. More recent methods combine these ideas, such as channel-wise autoregressive models [ 45 ] , checkerboard context models [ 24 ] , and hybrid designs [ 23 , 17 , 27 ] . Transformer-based entropy models [ 48 , 32 ] have also been explored to leverage long-range dependencies for more accurate probability estimation.

[18] h3: 2.2 Diffusion-Based Image Compression

[19] p: The success of diffusion models in image generation has motivated their recent adoption in extreme image compression, enabling highly realistic reconstruction under ultra-low bitrates. These methods typically leverage generative priors from pre-trained diffusion models by conditioning the decoding process on the noisy latent representation extracted from the input image. For example, PerCo [ 10 ] fine-tunes a diffusion model using vector-quantized spatial features and global text descriptions generated by BLIP-2 [ 35 ] . ResULIC [ 28 ] further analyzes semantic residuals between the original and reconstructed images, transmitting text-guided residuals to steer the diffusion process. DiffEIC [ 38 ] and its extension RDEIC [ 39 ] demonstrate that conditioning solely on VAE-compressed latents can yield competitive performance without textual input. Alternatively, Relic et al . [ 50 ] and later work [ 51 ] model quantization errors in the latent space as noise and recover the image via a diffusion denoising process. Despite gains in perceptual realism, such methods often incur high decoding latency due to multi-step sampling strategies like DDIM [ 55 ] . To mitigate this, recent methods [ 65 , 60 , 21 ] have incorporated one-step diffusion models [ 53 ] , substantially improving inference efficiency while preserving high perceptual quality. Notwithstanding these advances, several key challenges persist that hinder content adaptation, motivating our work toward further improving compression performance.

[20] figure: Figure 2 : On the encoder side, an analysis transform g a g_{a} encodes the input image 𝐱 \mathbf{x} into a compact latent representation 𝐲 \mathbf{y} . An uncertainty map 𝐦 \mathbf{m} is estimated by f u f_{u} to guide the quantization of 𝐲 \mathbf{y} . The quantized latent 𝐲 ^ \mathbf{\hat{y}} is encoded into a bitstream via an arithmetic encoder (AE) and transmitted. On the decoder side, a synthesis transform g s g_{s} upsamples 𝐲 ^ \mathbf{\hat{y}} to produce a noisy latent 𝒍 T \bm{l}_{T} at the spatial resolution required by the pre-trained Stable Diffusion VAE decoder 𝒟 S ​ D \mathcal{D}_{SD} [ 52 ] . In learned codecs, 𝒍 T \bm{l}_{T} typically has a high channel count (e.g., 320), while 𝒟 S ​ D \mathcal{D}_{SD} is fixed to accept only 4-channel input. To resolve this, the entire 𝒍 T \bm{l}_{T} is commonly input to the Unet ϵ S ​ D \epsilon_{SD} (a new input channel number is set to the first convolutional layer of the Unet) to utilize all available context for estimating more accurate 4-channel noise (the output channel number of the Unet is still 4) [ 65 ] . The denoising process is applied exclusively to the first four noisy channels 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} , yielding the standard 4-channel clean latent 𝒍 0 \bm{l}_{0} for 𝒟 S ​ D \mathcal{D}_{SD} . To concentrate essential semantic information into 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} , a lightweight auxiliary decoder g a ​ u ​ x g_{aux} takes 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} as inputs to reconstruct an auxiliary image 𝐱 ^ a ​ u ​ x \mathbf{\hat{x}}_{aux} . To produce a content-adaptive textual description c a ​ u ​ x c_{aux} , 𝐱 ^ a ​ u ​ x \mathbf{\hat{x}}_{aux} is captioned by f c f_{c} (a frozen BLIP [ 36 ] ). c a ​ u ​ x c_{aux} is then combined with a fixed description c f ​ i ​ x c_{fix} to condition a one-step diffusion denoising process [ 53 ] .

[21] h2: 3 Limitations of Diffusion-Based Compression

[22] h3: 3.1 Isotropic Quantization

[23] p: A critical yet underexplored challenge in diffusion-based generative compression lies in the mismatch between the content-agnostic quantization strategy and the operational principle of diffusion models. For example, most methods [ 38 , 21 , 60 , 65 ] directly quantized the latent representation with a fixed step size, treating the quantization errors as uniform noise to be removed by diffusion process. While Relic et al . [ 51 ] introduced universal quantization to better align the quantization errors with Gaussian diffusion noise schedule through a derived signal-to-noise ratio (SNR)-matching scheme, it still relies on a global isotropic quantization parameter that is applied uniformly across the entire compact latent representation. This common practice of isotropic quantization implicitly assumes that the distortion introduced by quantization—which the diffusion model is tasked with denoising—affects all image regions equally. However, this assumption contradicts both the nature of image content and the behavior of diffusion models. Natural images exhibit significant spatial heterogeneity, comprising textured regions rich in high-frequency details and smooth regions with minimal information. Diffusion models, in turn, possess noise-level-dependent priors: at high noise levels, they excel at hallucinating realistic textures from a strong generative prior, while at lower noise levels, they act more as conservative denoisers, preserving transmitted structural information. Global isotropic quantization forces a single, compromise noise level upon the entire compact latent representation, failing to adapt to the varying content complexity. Consequently, textured regions suffer from insufficient generative intervention, leading to blurred details, while smooth regions are subjected to unnecessary and potentially disruptive artificiality. This isotropic quantization strategy fails to harness the full potential of the diffusion model’s adaptive denoising capabilities due to its inability to perform content-aware noise shaping, creating a suboptimal alignment between the encoded signal and the decoder’s generative prior.

[24] h3: 3.2 Information Concentration Bottleneck

[25] p: Diffusion-based image codecs face a fundamental information concentration bottleneck that limits its efficiency and prevents content-aware representation learning. This bottleneck arises from the architectural mismatch between the high-dimensional noisy latents produced by learned codecs and the fixed-dimensional input expected by the pre-trained Stable Diffusion VAE decoder [ 52 ] . As shown in Fig. 2 , learned codecs commonly generate a noisy latent 𝒍 T \bm{l}_{T} with channel dimensions significantly exceeding the standard 4-channel latent space of the VAE decoder. However, only the first four channels 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} are denoised and fed into the subsequent VAE decoder 𝒟 S ​ D \mathcal{D}_{SD} . This creates a critical constraint: the most semantically meaningful information must be concentrated within 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} for effective reconstruction. Without explicit guidance, the learning process may fail to adaptively concentrate essential semantic information into the critical first four channels based on image content. The diffusion model’s generative prior cannot be fully leveraged if the noisy latent lacks the necessary information density in its primary channels, resulting in a non-adaptive latent representation that fails to preserve content-specific details.

[26] h3: 3.3 Ineffective Textual Conditioning

[27] p: Despite the remarkable capability of diffusion models to leverage textual guidance for high-quality image generation, existing diffusion-based compression methods struggle to effectively integrate content-adaptive text conditioning in a rate-efficient manner. Several methods [ 10 , 18 , 28 ] leverage multimodal large models to automatically generate textual descriptions, which are then losslessly compressed and transmitted as side information. While this provides content-aware guidance for the diffusion denoising process, the associated textual bitrate constitutes some overheads in ultra-low bitrate scenarios. For example, for the mobile satellite image communication application, the transmission packet size is limited (e.g., 450 bytes). Even low-bitrate texts consume a portion of the precious bit budget, leaving fewer bits for image transmission. Therefore, Zhang et al . [ 65 ] proposed to avoid transmitting textual descriptions and instead condition the diffusion model on a fixed, generic prompt such as “ A high-resolution, 8K, ultra-realistic image with sharp focus, vibrant colors, and natural lighting ”. Although this eliminates textual bitrate cost, the prompt is inherently agnostic to image content, failing to provide semantically meaningful guidance and limiting the model’s ability to reconstruct content-specific details. The fundamental limitation of these methods is their inability to provide content-adaptive textual conditioning without incurring additional textual bitrate costs, thereby hindering the potential for semantically-aware reconstruction.

[28] h2: 4 Method

[29] h3: 4.1 Uncertainty-Guided Adaptive Quantization

[30] p: To address the limitations of content-agnostic global isotropic quantization in diffusion-based compression, we propose an Uncertainty-Guided Adaptive Quantization method that aligns the quantization process with the diffusion model’s noise-dependent generative prior, thereby achieving content-adaptive quantization.

[31] p: Specifically, as illustrated in Fig. 2 , our method begins by upsampling the hyperprior latent 𝐳 ^ \mathbf{\hat{z}} to match the spatial resolution of the main latent representation 𝐲 \mathbf{y} :

[32] table: 𝐳 ¯ = UP ​ ( 𝐳 ^ ) , \mathbf{\bar{z}}=\text{UP}(\mathbf{\hat{z}}), (1)

[33] p: where UP ​ ( ⋅ ) \text{UP}(\cdot) denotes bilinear upsampling. We then compute the residual between 𝐲 \mathbf{y} and 𝐳 ¯ \mathbf{\bar{z}} :

[34] table: 𝐫 = 𝐲 − 𝐳 ¯ . \mathbf{r}=\mathbf{y}-\mathbf{\bar{z}}. (2)

[35] p: This residual reflects the uncertainty between 𝐲 \mathbf{y} and 𝐳 ¯ \mathbf{\bar{z}} —the larger the residual in a region, the less information 𝐳 ¯ \mathbf{\bar{z}} conveys about 𝐲 \mathbf{y} , indicating more complex image textures and serving as a basis for content-aware adaptation. The residual is then processed through a lightweight uncertainty estimation network f u f_{u} to predict an uncertainty map:

[36] table: 𝐦 = f u ​ ( 𝐫 ) , \mathbf{m}=f_{u}(\mathbf{r}), (3)

[37] p: where each element of 𝐦 \mathbf{m} is restricted to be m i , j ≥ 1 m_{i,j}\geq 1 .

[38] p: We then modulate the latent representation 𝐲 \mathbf{y} using the uncertainty map 𝐦 \mathbf{m} to achieve content-adaptive scaling:

[39] table: 𝐲 ¯ = 𝐲 / 𝐦 , \mathbf{\bar{y}}=\mathbf{y}/\mathbf{m}, (4)

[40] p: where ` ​ ` / " ``/" denotes element-wise division. The modulated latent 𝐲 ¯ \mathbf{\bar{y}} is then quantized:

[41] table: 𝐲 ^ = Q ⁡ ( 𝐲 ¯ ) = ⌊ 𝐲 ¯ Δ ⌉ ⋅ Δ , \mathbf{\hat{y}}=Q(\mathbf{\bar{y}})=\left\lfloor\frac{\mathbf{\bar{y}}}{\Delta}\right\rceil\cdot\Delta, (5)

[42] p: where Q ⁡ ( ⋅ ) Q(\cdot) represents the quantization function, ⌊ ⋅ ⌉ \lfloor\cdot\rceil denotes rounding to the nearest integer, and Δ \Delta is the quantization bin width. The quantization process can be approximated as the addition of independent uniform noise:

[43] table: 𝐲 ^ − 𝐲 ¯ ≈ ϵ , ϵ i , j ∼ 𝒰 ( − Δ / 2 , Δ / 2 ) , \mathbf{\hat{y}}-\mathbf{\bar{y}}\approx\bm{\epsilon},\quad\epsilon_{i,j}\sim\mathcal{U}(-\Delta/2,\Delta/2), (6)

[44] p: where ϵ \bm{\epsilon} represents the quantization error approximated as i.i.d. uniform noise, and 𝒰 ( − Δ / 2 , Δ / 2 ) \mathcal{U}(-\Delta/2,\Delta/2) denotes a uniform distribution over the interval [ − Δ / 2 , Δ / 2 ] [-\Delta/2,\Delta/2] . The quantized latent representation is therefore:

[45] table: 𝐲 ^ ≈ 𝐲 ¯ + ϵ = 𝐲 / 𝐦 + ϵ . \mathbf{\hat{y}}\approx\mathbf{\bar{y}}+\bm{\epsilon}=\mathbf{y}/\mathbf{m}+\bm{\epsilon}. (7)

[46] p: At the decoder, 𝐲 ^ \mathbf{\hat{y}} is directly feed into the diffusion model without applying the inverse scaling. This formulation reveals that although the quantization noise ϵ \bm{\epsilon} has a constant variance σ ϵ 2 = Δ 2 / 12 \sigma_{\epsilon}^{2}=\Delta^{2}/12 [ 51 ] , the pre-quantization modulation by 𝐦 \mathbf{m} creates a locally varying signal-to-noise ratio (SNR) at the decoder input, enabling content-aware noise shaping. The effective local SNR for a latent element y i , j y_{i,j} can be characterized as:

[47] table: SNR i , j ∝ 𝔼 ⁡ [ y ¯ i , j 2 ] σ ϵ 2 = 𝔼 ⁡ [ y i , j 2 ] m i , j 2 ⋅ σ ϵ 2 , \text{SNR}_{i,j}\propto\frac{\mathbb{E}[\bar{y}_{i,j}^{2}]}{\sigma_{\epsilon}^{2}}=\frac{\mathbb{E}[y_{i,j}^{2}]}{m_{i,j}^{2}\cdot\sigma_{\epsilon}^{2}}, (8)

[48] p: where 𝔼 ⁡ [ y ¯ i , j 2 ] \mathbb{E}[\bar{y}_{i,j}^{2}] is the power of the modulated latent. This quantitative relationship leads to our central content-adaptive mechanism:

[49] p: High uncertainty regions ( m i , j m_{i,j} is large): The signal power is reduced by a factor of m i , j 2 m_{i,j}^{2} , resulting in low local SNR. The diffusion model therefore relies more heavily on its generative prior to synthesize details, adaptively enhancing texture generation where needed.

[50] p: Low uncertainty regions ( m i , j m_{i,j} is small): The signal power remains largely unchanged, maintaining high local SNR. The diffusion model thus prioritizes faithful preservation of the transmitted structural information, adaptively conserving fidelity in smooth areas.

[51] p: Our UGAQ method thereby reduces the misalignment between the quantization distortion and the diffusion model’s noise-dependent denoising strategy through content-aware noise shaping, adaptively leveraging its generative capabilities based on local image content.

[52] h3: 4.2 Auxiliary Decoder-Guided Information Concentration

[53] p: To address the information concentration bottleneck and enable content-aware latent representation learning, we propose an Auxiliary Decoder-Guided Information Concentration method. Our key insight is that without explicit supervision, it may be difficult for the first four channels of the noisy latent contain essential semantic information for high-quality reconstruction, resulting in a non-adaptive latent distribution. Therefore, we introduce a lightweight auxiliary decoder g a ​ u ​ x g_{aux} that operates exclusively on these primary channels, providing direct supervision to optimize their information-carrying capacity and enforce content-driven information allocation.

[54] p: Formally, given the full noisy latent 𝒍 T \bm{l}_{T} with C C channels where C ≫ 4 C\gg 4 , as shown in Fig. 2 , we feed its first four channels 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} into an auxiliary decoder g a ​ u ​ x g_{aux} to produce an auxiliary reconstructed image 𝐱 ^ a ​ u ​ x \mathbf{\hat{x}}_{aux} :

[55] table: 𝐱 ^ a ​ u ​ x = g a ​ u ​ x ( 𝒍 T ( 1 : 4 ) ) . \mathbf{\hat{x}}_{aux}=g_{aux}(\bm{l}_{T}^{(1:4)}). (9)

[56] p: We then compute an auxiliary reconstruction loss between this output and the original image 𝐱 \mathbf{x} :

[57] table: ℒ a ​ u ​ x = ‖ 𝐱 − 𝐱 ^ a ​ u ​ x ‖ 2 2 . \mathcal{L}_{aux}=\|\mathbf{x}-\mathbf{\hat{x}}_{aux}\|_{2}^{2}. (10)

[58] p: This auxiliary reconstruction loss will be incorporated into the overall loss function [ 65 ] to optimize the model.

[59] figure: Figure 3 : Quantitative comparisons of different generative image codecs on Kodak, DIV2K Val, and CLIC 2020 Test.

[60] h3: 4.3 Bitrate-Free Adaptive Textual Conditioning

[61] p: To overcome the limitation of being unable to obtain content-adaptive textual conditioning without additional textual bitrate costs, we propose a Bitrate-Free Adaptive Textual Conditioning method. Our key insight is to leverage the auxiliary reconstruction 𝐱 ^ a ​ u ​ x \mathbf{\hat{x}}_{aux} —generated by the lightweight auxiliary decoder g a ​ u ​ x g_{aux} introduced in Section 4.2 —as a proxy to infer a content-aware textual description. Since 𝐱 ^ a ​ u ​ x \mathbf{\hat{x}}_{aux} is derived entirely from the noisy latent 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} , our method provides semantically meaningful textual guidance with zero textual bitrate cost.

[62] p: As shown in Fig. 2 , the auxiliary reconstructed image 𝐱 ^ a ​ u ​ x \mathbf{\hat{x}}_{aux} is fed into an image captioning model f c f_{c} (a frozen BLIP [ 36 ] ) to produce a content-adaptive textual description c a ​ u ​ x c_{aux} :

[63] table: c a ​ u ​ x = f c ​ ( 𝐱 ^ a ​ u ​ x ) . c_{aux}=f_{c}(\mathbf{\hat{x}}_{aux}). (11)

[64] p: To enhance robustness and stability, we then combine c a ​ u ​ x c_{aux} with a fixed, generic textual description c f ​ i ​ x c_{fix} (“ A high-resolution, 8K, ultra-realistic image with sharp focus, vibrant colors, and natural lighting ”) [ 65 , 63 ] using the simple string concatenation:

[65] table: c = c a ​ u ​ x + c f ​ i ​ x . c=c_{aux}+c_{fix}. (12)

[66] p: This combined textual description c c is used as the conditions for the diffusion denoising process.

[67] h3: 4.4 Implementation

[68] p: Our codec follows the prevalent auto-encoder architecture commonly adopted in learned image compression. To balance generative capability against decoding complexity, we employ a distilled version [ 53 ] of Stable Diffusion 2.1 [ 52 ] to achieve one-step diffusion . A lightweight blip-image-captioning-base model is used for auxiliary reconstructed image captioning. For entropy modeling, we integrate both a hyperprior c h c_{h} and a spatial prior c s c_{s} , where the latter is generated by a 4-step autoregressive entropy model with quadtree partitioning [ 34 ] .

[69] p: We train our codec on the training sets of DF2K [ 40 ] and CLIC 2020 Professional [ 57 ] with the rate-distortion objective:

[70] table: ℒ = λ ​ ℛ + 𝒟 , \mathcal{L}=\lambda\mathcal{R}+\mathcal{D}, (13)

[71] p: where λ \lambda is the Lagrange multiplier, ℛ \mathcal{R} is the bitrate. In addition to our proposed auxiliary reconstruction loss, the distortion term 𝒟 \mathcal{D} incorporates several components from [ 65 ] , including MSE, LPIPS (with VGG features), a CLIP distance [ 49 ] , and a GAN loss. More implementation details can be found in the supplementary materials.

[72] figure: Figure 4 : Qualitative comparison of different generative image codecs on the Kodak dataset under ultra-low bitrate conditions.

[73] h2: 5 Experiments

[74] h3: 5.1 Experimental Settings

[75] p: Test Datasets. We use Kodak [ 29 ] , the validation set of DIV2K (DIV2K Val) [ 4 ] , and the test set of CLIC 2020 Professional (CLIC 2020 Test) [ 57 ] for evaluation. The Kodak dataset contains 24 images with a resolution of 768 × 512 768\times 512 . The DIV2K Val and the CLIC 2020 Test contain 100 and 428 high-quality 2K-resolution images, respectively. All images are evaluated with the original resolution.

[76] p: Evaluation Metrics. We measure bitrate cost in bits per pixel (bpp). Following prior work [ 59 , 51 , 65 ] , we evaluate perceptual quality using DISTS [ 15 ] , LPIPS [ 64 ] , FID [ 25 ] , and KID [ 63 ] . Note that FID and KID are omitted on the Kodak dataset due to its limited size. Results of PSNR and MS-SSIM are also provided in the supplementary material.

[77] p: Comparison Methods. We compare our codec against several state-of-the-art generative image codecs. These include: HiFiC [ 43 ] , a representative GAN-based codec [ 20 ] ; DLF [ 59 ] and GLC [ 26 ] , which are leading vector quantization-based codecs; and a range of diffusion-based codecs, namely DiffEIC [ 38 ] , ResULIC [ 28 ] , MKIC [ 18 ] , OSCAR [ 21 ] , and StableCodec [ 65 ] .

[78] h3: 5.2 Quantitative and Qualitative Comparisons

[79] p: As illustrated in Fig. 3 , we evaluate the quantitative compression performance of different generative image codecs under ultra-low bitrate conditions. Our codec consistently outperforms other diffusion-based codecs—including DiffEIC, ResULIC, MKIC, OSCAR, and StableCodec—across all evaluated datasets in terms of LPIPS, DISTS, FID, and KID, validating the effectiveness of our design. We further provide a qualitative comparison on the Kodak dataset in Fig. 4 under comparable bitrates. Visual results show that competing codecs such as StableCodec, DLF, MKIC, and OSCAR produce overly smooth regions or lose fine-grained textures. In contrast, our reconstructions preserve more high-frequency details and exhibit more natural visual characteristics. More results can be found in the supplementary material.

[80] figure: Table 1 : Ablation studies of our proposed methods on Kodak. Negative BD-rate (%) values indicate better compression performance. The distortion is measured by LPIPS and DISTS. Models UGAQ ADGIC BFATC LPIPS DISTS M 0 M_{0} ✗ ✗ ✗ 0.00 0.00 M 1 M_{1} ✓ ✗ ✗ –3.7 –2.7 M 2 M_{2} ✓ ✓ ✗ –5.3 –3.5 M 3 M_{3} ✓ ✓ ✓ –6.8 –5.5

[81] h3: 5.3 Ablation Study

[82] p: In this section, we conduct ablation studies to validate the effectiveness of our proposed methods.

[83] p: Uncertainty-Guided Adaptive Quantization. We first evaluate the contribution of our UGAQ method by integrating it into the baseline Model M 0 M_{0} to construct Model M 1 M_{1} . As shown in Tab. 1 , UGAQ yields BD-rate reductions of 3.7% and 2.7% on LPIPS and DISTS, respectively. This improvement is attributed to the ability of UGAQ to provide content-aware quantization, in contrast to isotropic quantization which applies uniform quantization strength regardless of local content complexity. As visualized in Fig. 5 , the residual 𝐲 − 𝐳 ¯ \mathbf{y}-\mathbf{\bar{z}} serves as an indicator of content uncertainty, with larger values corresponding to highly textured regions. Our method translates this signal into a spatially-varying uncertainty map 𝐦 \mathbf{m} , where regions with more complex texture are assigned larger values—opposing existing spatial scaling-based quantization method [ 33 ] . This map guides the quantization process in a content-adaptive manner, producing quantization residuals 𝐲 − 𝐲 ^ \mathbf{y}-\mathbf{\hat{y}} that exhibit clear semantic alignment and strongly correlate with content complexity. This demonstrates the ability of UGAQ to actively shape quantization errors, thereby aligning the quantization distortion with the diffusion model’s noise-dependent denoising behavior through content-aware noise allocation.

[84] figure: Figure 5 : Analysis of Uncertainty-Guided Adaptive Quantization (UGAQ) and the isotropic quantization on the DIV2K dataset.

[85] p: Auxiliary Decoder-Guided Information Concentration. We proceed to validate our ADGIC method by progressively integrating it into Model M 1 M_{1} . The results in Tab. 1 show that ADGIC yields a further BD-rate reduction of 1.6% (from − 3.7 % -3.7\% to − 5.3 % -5.3\% ) on LPIPS and 0.8% (from − 2.7 % -2.7\% to − 3.5 % -3.5\% ) on DISTS. To better understand its working mechanism, we analyze the energy distribution across the first four channels of the noisy latent 𝒍 T ( 1 : 4 ) \bm{l}_{T}^{(1:4)} with and without ADGIC under varying bitrate conditions on the Kodak dataset. Following [ 12 ] , we employ variance as a measure of channel energy. As shown in Fig. 6 , ADGIC enhances energy concentration in the primary channels, demonstrating its role in enforcing content-aware information allocation by prioritizing essential semantics adaptively.

[86] p: Bitrate-Free Adaptive Textual Conditioning. We further validate our BFATC method by integrating it into Model M 2 M_{2} . As reported in Tab. 1 , BFATC brings an additional 1.5% BD-rate improvement (from –5.3% to –6.8%) on LPIPS and 2.0% (from –3.5% to –5.5%) on DISTS. This performance gain demonstrates that providing content-adaptive textual guidance is crucial for enhancing compression efficiency. Our BFATC method remains robust across bitrates. As visualized in Fig. 7 , even under severe reconstruction noise at low bitrates, the auxiliary reconstructed image retains sufficient semantic content to produce textual descriptions that remain semantically consistent.

[87] figure: Figure 6 : Energy comparison of the first four channels of the noisy latents of the codecs with and without Auxiliary Decoder-Guided Information Concentration (ADGIC) on the Kodak dataset.

[88] figure: Figure 7 : Illustration of the textual descriptions extracted from auxiliary reconstructed images under different bitrate conditions.

[89] h2: 6 Conclusion

[90] p: In this work, we address three key limitations hindering content adaptation in diffusion-based image compression: the misalignment from isotropic quantization, the information concentration bottleneck in latent representation, and the inefficiency of textual conditioning. To this end, we propose a content-adaptive diffusion-based image codec (CADC) built upon three technical innovations: an Uncertainty-Guided Adaptive Quantization method that aligns effective quantization distortion with content characteristics through content-aware noise shaping; an Auxiliary Decoder-Guided Information Concentration method that ensures essential semantic information is adaptively preserved in the primary latent channels via content-driven allocation; and a Bitrate-Free Adaptive Textual Conditioning method that derives content-specific semantic guidance without textual bitrate overhead. Extensive experiments validate that our codec achieves the state-of-the-art perceptual quality, particularly at ultra-low bitrates.

[91] h2: References

[92] p: Supplementary Material

[93] h2: 7 Implementation Details

[94] figure: Figure 8 : Network structures of the main modules, including the main analysis transform g a g_{a} , main synthesis transform g s g_{s} , hyper analysis transform h a h_{a} , hyper synthesis transform h s h_{s} , auxiliary decoder g a ​ u ​ x g_{aux} , uncertainty estimation network f u f_{u} , and the context model. For efficient network construction, we primarily rely on modified versions of InceptionNeXt [ 62 ] , GatedCNN [ 61 ] , and their combination (StarBlock).

[95] figure: Figure 9 : Illustration of our entropy modeling process.

[96] figure: Figure 10 : All rate-distortion curves of different generative image codecs on Kodak, the validation set of DIV2K, and the test set of CLIC 2020 Professional in terms of LPIPS, DISTS, FID, KID, MS-SSIM, and PSNR metrics.

[97] figure: Figure 11 : Visual examples and comparisons on 2K-resolution images from the test set of CLIC 2020 Professional.

[98] figure: Figure 12 : Visual examples and comparisons on 2K-resolution images from the test set of CLIC 2020 Professional.

[99] figure: Figure 13 : Visual examples and comparisons on 2K-resolution images from the validation set of DIV2K.

[100] figure: Figure 14 : Visual examples and comparisons on 2K-resolution images from the validation set of DIV2K.

[101] h3: 7.1 Network Structure

[102] p: The detailed architectures of the main modules are illustrated in Fig. 8 , including the main analysis transform g a g_{a} , main synthesis transform g s g_{s} , hyper analysis transform h a h_{a} , hyper synthesis transform h s h_{s} , auxiliary decoder g a ​ u ​ x g_{aux} , uncertainty estimation network f u f_{u} , and the context model. For efficient network construction, we primarily rely on modified versions of InceptionNeXt [ 62 ] , GatedCNN [ 61 ] , and their combination (StarBlock).

[103] p: We also illustrate the overall entropy modeling process in Fig. 9 . Our entropy model integrates a hyperprior module with an autoregressive context model. The hyperprior representation 𝐜 𝐡 \mathbf{c_{h}} is derived as:

[104] table: 𝐳 = h a ​ ( 𝐲 ) , 𝐳 ^ = ⌊ 𝐳 ⌉ , 𝐜 𝐡 = h s ​ ( 𝐳 ^ ) , \mathbf{z}=h_{a}(\mathbf{y}),\quad\mathbf{\hat{z}}=\lfloor\mathbf{z}\rceil,\quad\mathbf{c_{h}}=h_{s}(\mathbf{\hat{z}}), (14)

[105] p: where ⌊ ⋅ ⌉ \lfloor\cdot\rceil denotes rounding to the nearest integer. Here, 𝐲 \mathbf{y} has 320 channels with a spatial downsampling factor of 64, while 𝐳 \mathbf{z} and 𝐳 ^ \mathbf{\hat{z}} also have 320 channels but with a higher spatial compression ratio of 256 × \times . To balance coding performance and computational efficiency, we employ a 4-step autoregressive process based on quadtree partitioning [ 34 ] . As shown in Fig. 9 , this process estimates the Gaussian parameters 𝝁 \bm{\mu} and 𝝈 \bm{\sigma} for the quantized latent 𝐲 ^ \mathbf{\hat{y}} . Subsequently, arithmetic coding is applied to encode or decode 𝐲 ^ \mathbf{\hat{y}} into/from the bitstream.

[106] p: For BLIP, we use the lightweight blip-image-captioning-base model (247.41M parameters, with inputs resized to 384 × 384 384\times 384 by default).

[107] h3: 7.2 Training Process

[108] p: We train our codec based on the standard rate-distortion loss:

[109] table: ℒ = λ ​ ℛ + 𝒟 , \mathcal{L}=\lambda\mathcal{R}+\mathcal{D}, (15)

[110] p: where ℛ \mathcal{R} denotes the bitrate, 𝒟 \mathcal{D} is the distortion measure, and λ \lambda is a Lagrange multiplier that balances the two terms. We employ a two-stage training strategy [ 65 ] . In the first stage, a base model is trained using a relatively small λ base \lambda_{\text{base}} . In the second stage, this pre-trained model is fine-tuned with a larger λ target \lambda_{\text{target}} to achieve ultra-low target bitrates. The distortion term 𝒟 \mathcal{D} incorporates multiple components: MSE, LPIPS (computed with VGG features), a CLIP-based loss ℒ CLIP \mathcal{L}_{\text{CLIP}} [ 65 ] —defined as the ℓ 2 \ell_{2} -distance between CLIP embeddings of 𝐱 \mathbf{x} and 𝐱 ^ \mathbf{\hat{x}} , an adversarial loss ℒ adv \mathcal{L}_{\text{adv}} , and our proposed auxiliary reconstruction loss ℒ aux \mathcal{L}_{\text{aux}} . We use DINOv2 [ 46 ] with registers [ 14 ] as the discriminator backbone [ 31 ] . Note that ℒ adv \mathcal{L}_{\text{adv}} and ℒ aux \mathcal{L}_{\text{aux}} are only activated in the second training stage. The complete objective is formulated as follows:

[111] table: Stage I : arg ⁡ min 𝜃 L 1 = λ base ℛ + 𝒟 1 , \displaystyle\text{ Stage I : }\underset{\theta}{\arg\min}L_{1}=\lambda_{\text{base }}\mathcal{R}+\mathcal{D}_{1}, (16) Stage II : arg ⁡ min 𝜃 L 2 = λ target ℛ + 𝒟 2 , \displaystyle\text{ Stage II : }\underset{\theta}{\arg\min}L_{2}=\lambda_{\text{target }}\mathcal{R}+\mathcal{D}_{2}, 𝒟 1 = d 1 ​ MSE ⁡ ( x , x ^ ) + d 2 ​ LPIPS ⁡ ( x , x ^ ) + d 3 ​ ℒ C ​ L ​ I ​ P ​ ( x , x ^ ) 𝒟 2 = d 1 ​ MSE ⁡ ( x , x ^ ) + d 2 ​ LPIPS ⁡ ( x , x ^ ) + d 3 ​ ℒ C ​ L ​ I ​ P ​ ( x , x ^ ) + d 4 ​ ℒ a ​ u ​ x ​ ( x , x ^ a ​ u ​ x ) + d 5 ​ ℒ a ​ d ​ v , \displaystyle\begin{aligned} &\mathcal{D}_{1}=d_{1}\operatorname{MSE}(x,\hat{x})+d_{2}\operatorname{LPIPS}(x,\hat{x})+d_{3}\mathcal{L}_{CLIP}(x,\hat{x})\\ &\begin{aligned} &\mathcal{D}_{2}=d_{1}\operatorname{MSE}(x,\hat{x})+d_{2}\operatorname{LPIPS}(x,\hat{x})+d_{3}\mathcal{L}_{CLIP}(x,\hat{x})\\ &\quad+d_{4}\mathcal{L}_{aux}(x,\hat{x}_{aux})+d_{5}\mathcal{L}_{adv},\end{aligned}\end{aligned}

[112] p: where θ \theta denotes all trainable parameters in the codec, and d 1 d_{1} – d 5 d_{5} are weighting coefficients that balance the distortion terms.

[113] h2: 8 More Experimental Results

[114] h3: 8.1 More Quantitative Results

[115] p: A comprehensive evaluation of rate-distortion performance is conducted on Kodak, the validation set of DIV2K [ 4 ] , and the test set of CLIC 2020 Professional [ 57 ] , comparing various codecs (HiFiC [ 43 ] , DiffEIC [ 38 ] , GLC [ 26 ] , DLF [ 59 ] , ResULIC [ 28 ] , MKIC [ 18 ] , OSCAR [ 21 ] , StableCodec [ 65 ] ) across six metrics: LPIPS, DISTS, FID, KID, MS-SSIM, and PSNR. Figure 10 shows that our codec consistently delivers state-of-the-art perceptual quality, particularly under ultra-low bitrate conditions.

[116] h3: 8.2 More Qualitative Results

[117] p: Following the quantitative analysis, we also provide a more detailed subjective comparison of the three top-performing codecs: our codec, StableCodec [ 65 ] , and DLF [ 59 ] , under ultra-low bitrate conditions. Visual comparisons are presented in Figs. 11 , 12 , 13 and 14 . The results show that our codec consistently achieves the best visual quality, corroborating the quantitative findings and confirming its superior perceptual performance at ultra-low bitrates.

[118] h3: 8.3 Runtime Comparison

[119] p: Table 2 compares the runtime efficiency of our codec against StableCodec and DLF on the Kodak dataset using a single RTX 3090 GPU. The encoding time of our codec is significantly reduced, as it eliminates the need for the pre-trained VAE encoder used in Stable Diffusion and the auxiliary encoder along with the latent residual prediction (LRP) module [ 65 ] in StableCodec’s entropy model. For decoding, although our codec incorporates an auxiliary decoder and a BLIP image captioning model, the overall decoding time sees only a marginal increase. This is achieved by simplifying the architecture of the main and hyper synthesis transforms, coupled with the removal of the LRP module [ 65 ] in the entropy model, which collectively reduce computational overhead. Nonetheless, due to the inherent complexity of the diffusion model, our decoding time remains higher than that of DLF.

[120] p: It is important to note that in ultra-low bitrate application scenarios, such as mobile-satellite communications, the uplink bandwidth (from the mobile device to the satellite) is often more constrained and valuable than the downlink. This places a premium on low encoding complexity at the client side, while the more computationally intensive decoding can be offloaded to powerful cloud servers. Therefore, our codec—with its fast encoding and competitively performing decoding—retains strong practical value for real-world deployment.

[121] figure: Table 2 : Runtime comparison of in seconds averaged on the Kodak dataset. Method Encoding Time (s) Decoding Time (s) Ours 0.034 0.355 StableCodec 0.156 0.322 DLF 0.181 0.195

[122] h3: 8.4 User Study

[123] p: To comprehensively evaluate the perceptual quality of reconstructed images at ultra-low bitrates, we conduct a user study on the Kodak dataset, comparing our codec with two top-performing codecs: StableCodec [ 65 ] and DLF [ 59 ] . The study follows a top-1 preference protocol, in which participants are asked to select the reconstruction they perceive as most visually consistent with the ground-truth image. Each participant evaluates 24 randomly ordered test cases. For each case, the ground-truth image is displayed together with the three reconstructed images in a single row of four images, with the order of the methods randomized across trials. Participants are instructed to select the reconstruction that is the most “consistent” with the original image. A total of 25 participants took part in the study, collectively contributing 600 evaluation cases. The results, summarized in Tab. 3 , indicate that reconstructions from our codec were preferred in 58.5% of cases. This strong preference underscores its superior perceptual quality as judged by human observers.

[124] figure: Table 3 : Top-1 user preference on the Kodak dataset. Method Ours StableCodec DLF Bitrate (bpp) 0.0076 0.0072 0.0079 Top-1 Percentage (%) 58.5 29.0 12.5

[125] h2: Instructions for reporting errors

[126] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[127] p: Tip: You can select the relevant text first, to include it in your report.

[128] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[129] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
