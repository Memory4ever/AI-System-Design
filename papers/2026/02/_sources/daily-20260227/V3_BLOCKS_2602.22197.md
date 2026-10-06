[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes

[3] h6: Abstract

[4] p: Advances in Generative AI (GenAI) have led to the development of various protection strategies to prevent the unauthorized use of images. These methods rely on adding imperceptible protective perturbations to images to thwart misuse such as style mimicry or deepfake manipulations. Although previous attacks on these protections required specialized, purpose-built methods, we demonstrate that this is no longer necessary. We show that off-the-shelf image-to-image GenAI models can be repurposed as generic “denoisers” using a simple text prompt, effectively removing a wide range of protective perturbations. Across 8 case studies spanning 6 diverse protection schemes, our general-purpose attack not only circumvents these defenses but also outperforms existing specialized attacks while preserving the image’s utility for the adversary. Our findings reveal a critical and widespread vulnerability in the current landscape of image protection, indicating that many schemes provide a false sense of security. We stress the urgent need to develop robust defenses and establish that any future protection mechanism must be benchmarked against attacks from off-the-shelf GenAI models. Code is available in this repository: https://github.com/mlsecviswanath/img2imgdenoiser .

[5] h6: Index Terms:

[6] h2: I Introduction

[7] p: The rise of Generative AI (GenAI) has heightened concerns about the unauthorized use of images, a risk that manifests itself in various forms. For instance, GenAI models are developed by indiscriminately collecting web images without obtaining permission, crediting, or compensating original creators [ 7 ] . This technology also enables deepfakes that target individuals by altering their personal images [ 61 ] , threatens artists’ income by creating synthetic art in their style without consent, also known as a style mimicry attack [ 97 ] , and poses a danger to online communities through the production of harmful images [ 126 ] .

[8] p: This has sparked significant interest in creating protection strategies to defend against unauthorized use of images. Due to the variety of potential threats, defense measures also vary. These include strategies such as: (1) defensive watermarking [ 68 , 34 ] , (2) mitigating art style mimicry [ 62 , 97 ] , (3) preventing deepfake manipulations of personal images [ 85 , 61 ] , (4) enabling image traceability when used to customize GenAI models [ 59 , 118 ] , and (5) safeguarding facial privacy [ 57 , 147 ] . A unifying feature of all these protection strategies is the application of protective perturbations or a protective cloak (which are typically imperceptible) to help prevent unauthorized use. As an example, a technique known as UnGANable [ 61 ] applies a protective cloak to an image to thwart GAN-based deepfake manipulation of that image.

[9] p: Note that the defender has only one chance to protect the images. If an adversary removes this protection, there will be no way to secure the images against future misuse. Recent studies have begun to demonstrate that some of these protection methods provide a false sense of security [ 3 , 31 , 40 , 53 ] . However, these attacks are generally tailored to specific types of protection strategies and require uniquely crafted AI-based methods to dismantle the protection. In this study, we demonstrate that developments in GenAI have progressed to a point where crafting specialized attacks is no longer required—off-the-shelf image-to-image ( img2img ) models can be easily repurposed as versatile “denoisers” to eliminate protective perturbations covering a wide variety of protection schemes. Our key contributions are as follows:

[10] p: Given a protected image, we show that image translation using an off-the-shelf img2img model guided by a simple text prompt (e.g., “Denoise this image”) is sufficient to remove a variety of protective perturbations available today. We use open-source Diffusion models such as FLUX [ 11 ] and SD3 [ 24 ] , and a closed-source, commercial model, GPT-4o [ 33 , 45 ] . Our approach requires no protection-specific adaptations and can be easily used by a low-skilled attacker to circumvent several protection schemes. Advances in generative processes and extensive pretraining on web-scale image datasets enable this simple attack.

[11] p: We demonstrate the effectiveness of this simple attack using 8 case studies, covering 6 diverse protection schemes, demonstrating the versatility of the attack. In 4 of these case studies, we also compare our attack against specialized protection-specific attacks [ 3 , 31 , 40 , 53 ] . Our scheme outperforms these specialized attacks.

[12] p: Our simple approach can remove sophisticated protective perturbations. This includes perturbations to protect specialized semantic properties (e.g., facial identity) [ 61 ] , perturbations applied through the latent space [ 34 ] , and perturbations designed to survive downstream fine-tuning tasks [ 59 ] .

[13] p: We conduct a comprehensive user study to assess how well our denoising approach preserves utility for the attacker. Through a study of the Mist [ 62 ] protection scheme, designed to prevent style mimicry attacks, we show that our denoisers produce images that are of high-quality, while preserving the expected style/content in the image. Our user study also shows that we significantly outperform recent specialized attacks against Mist, such as LightShed [ 31 ] .

[14] p: We show that it is challenging to create a protective scheme that is resistant to our simple attack. Our efforts to integrate our denoiser into two diverse protection pipelines, i.e., to create an attack-aware protection scheme, resulted in failure. The generated “adversarial” perturbations can still be easily removed by our denoiser. As future work, we recommend investigating robust approaches to generate protective perturbations in the low-frequency bands of an image. Our analysis of the VINE [ 68 ] watermarking scheme shows that this is a promising approach. However, VINE’s implementation of this approach still shows serious vulnerabilities against even simpler attack strategies—we find that the VINE watermark can be easily destroyed by extremely mild 0.7% center cropping of an image.

[15] p: Our findings highlight that future specialized protection removal attacks should invariably use off-the-shelf img2img models as a benchmark for comparison. Our approach can even outperform specialized attacks that use a supervised learning strategy, i.e., using knowledge of protected and unprotected variants of images, to remove protective perturbations [ 31 , 3 ] .

[16] p: Our results further reveal that more advanced and bigger capacity off-the-shelf img2img models are more capable at removing protections. img2img models will only continue to advance in the near future, potentially making this threat worse. We stress the need to urgently invest efforts into building robust protection schemes that can survive our attack. We have disclosed our findings to the creators of the affected protection schemes (see Section -A in Appendix).

[17] h2: II Goals, Threat Model, and Rationale

[18] h3: II-A Goals

[19] p: We define a perturbation as any modification, typically noise, applied to an image that may be human-perceptible or not. It is usually obtained by optimizing a tailored loss function and can be added directly in pixel space or via latent space changes. Such perturbations, or protective cloaks , are widely used as proactive defenses against unauthorized image use, including misuse of AI-generated images and copyright-protected images in training or any GenAI-based image pipeline. We show that recent GenAI advances threaten these perturbation-based defenses (i.e., protective measures).

[20] p: Recent breakthroughs in GenAI have led to the development of robust image translation models or img2img models. These models can take an existing image (source) along with a descriptive text prompt to create a new image aligned with the prompt’s directive. We demonstrate that these models can be repurposed to serve as efficient denoisers , i.e., to remove any noise from the source image. We argue that this noise-removal technique is sufficient to circumvent protective mechanisms employed in current perturbation-based defense strategies. Our key research questions are as follows:

[21] p: RQ1: Can off-the-shelf img2img models, used as generic denoisers, remove perturbations without any protection-specific adaptations? We aim to minimize protection-specific customizations, i.e., our denoising strategies are generic and not tailored to particular protections (e.g., watermarking, deepfake manipulation protection, artwork protection). Attacker goal: Can this process remove protective perturbations added by a defender, such as watermarks or perturbations preventing unauthorized use of images for fine-tuning GenAI models?

[22] p: RQ2: How does our attack performance vary with increasingly capable img2img models (used as denoisers)? img2img models continue to evolve rapidly. We experiment with a variety of open-source models in addition to an advanced commercial model. Open-source models include SD1.5 [ 87 ] , SDXL [ 82 ] , SD3 [ 24 ] and FLUX [ 11 ] . GPT-4o [ 33 , 45 ] is our commercial model.

[23] p: RQ3: Does our denoising approach preserve the utility for the attacker? After removing the protective perturbations, does our scheme preserve image utility for the downstream use case, e.g., to use unauthorized images to train a GenAI scheme?

[24] p: RQ4: How does our simple approach compare with recent work that uses specialized perturbation-removal schemes adapted towards the protection setting? Recall that our method is agnostic to the protection scheme and, therefore, generally applicable across many settings. Specialized schemes include methods such as UnMarker [ 53 ] designed specifically to remove watermarks from images, or INSIGHT [ 3 ] designed to remove protections to prevent style mimicry attacks threatening artists [ 97 , 62 ] .

[25] p: RQ5: Can our attacks, powered by simple denoisers, be neutralized by a countermeasure that leverages our denoising model in the perturbation-generation process? Can defenders create protective perturbations that cannot be removed by our denoising schemes?

[26] p: We address these research questions through 8 case studies, summarized in Table I . Four case studies examine different data protection strategies, including defenses against deepfake alterations, watermarking methods, and mitigating unauthorized use of images for training GenAI models. The remaining four compare our attack with recently proposed specialized (i.e., protection-specific) perturbation removal schemes.

[27] figure: TABLE I: Overview of our 8 case studies. Case study # Our attack against protection schemes Protection type Protection scheme (venue) 1 Preventing deepfake face manipulation UnGANable (USENIX Sec’23) [ 61 ] 2 In-processing watermarking PRC (ICLR’25) [ 34 ] 3 Post-processing watermarking VINE (ICLR’25) [ 68 ] 4 Traceability when misused for model personalization SIREN (IEEE S&P’25) [ 59 ] Our attack Vs. protection-specific attacks Protection type Specialized attack (venue) 5 Preventing finetuning -based style mimicry INSIGHT (USENIX Sec’24) [ 3 ] 6 7 Preventing Textual Inversion-based style mimicry Noisy Upscaling (ICLR’25) [ 40 ] LightShed (USENIX Sec’25) [ 31 ] 8 Semantic watermarking UnMarker (IEEE S&P’25) [ 53 ]

[28] h3: II-B Threat Model

[29] p: Since we cover a wide range of case studies, we outline a generalized threat model that is applicable to all cases. We will describe further details of the threat model pertinent to a case study in Sections IV and V . In this study, we adopt the perspective of an attacker, assuming access to powerful and widely available open and closed-source img2img tools.

[30] p: Defenders add perturbations in latent or pixel space to prevent unauthorized image use. As attackers, we aim to remove these perturbations to enable such use, for instance by stripping watermarks or protections on personal images that prevent deepfake manipulations. We assume no knowledge of the internals or design of the protection scheme, i.e., the attack is not tailored to it. Despite this challenging setting, we show that advances in GenAI can still weaken these defenses.

[31] p: Countermeasures. We also perform experiments to understand adaptive strategies by the defender based on the knowledge of our attack. This is studied in Section VI .

[32] h3: II-C Research Design and Rationale

[33] p: Why conduct 8 different case studies and why is such a study important now? Table I summarizes the 8 case studies. Examining this many cases departs from prior work on vulnerabilities of data protection schemes, which typically considers only 1–4 case studies [ 31 , 40 , 3 ] . Our main reasons are:

[34] p: (1) Our goal is to show that many perturbation-based protection schemes are vulnerable to advances in img2img technology. Our method is agnostic to the protection setting: across all 8 case studies, we use the same perturbation removal technique without any internal knowledge of the schemes. This shows that sophisticated, targeted mechanisms are unnecessary to uncover vulnerabilities in existing protection schemes.

[35] p: (2) Perturbation-based data protection is rapidly evolving. Our survey found over 30 papers in top venues since 2024 on perturbation-based protection for images (full list in Table VIII in the Appendix), spanning watermarking and copyright protection [ 68 , 34 , 132 ] , art style protection [ 110 , 97 , 62 ] , facial privacy [ 57 , 144 , 147 ] , deepfake manipulation [ 85 , 61 , 114 ] , and data traceability [ 59 , 118 ] . Similar efforts appear in other modalities, e.g., video [ 67 , 100 , 102 ] , audio [ 74 , 145 , 135 ] , and text [ 141 , 143 , 92 ] . It is infeasible to conduct a study that covers all these works. Instead, we carefully choose 8 case studies within the image modality.

[36] p: In the absence of our study, this research area will likely evolve into many disparate attempts to provide data protection without realizing that many protection pathways are easily threatened by off-the-shelf img2img schemes.

[37] p: How were the 8 case studies chosen? We selected 8 case studies based on three criteria: (1) High Performance: We chose protection schemes and specialized attacks that significantly outperform prior methods. Notably, 6 of the 8 works were published in 2025 in top venues, representing the state-of-the-art. (2) Diversity: We cover a range of threats, including style mimicry, misuse of data for model personalization, watermark removal, and deepfake manipulation. (3) Reproducibility: We prioritized methods with publicly released checkpoints, source code, and data.

[38] p: What is the novelty? We highlight two contributions. First, empirical simplicity : we show that off-the-shelf img2img models can effortlessly remove complex, diverse protective cloaks. Second, recombinant novelty : Beyond our empirical insights, we identify a systemic risk: foundation models act as a convergent threat vector, rendering diverse security problems susceptible to the same class of attacks.

[39] p: How do we navigate the complexity of evaluating 8 case studies? Given the diverse methodologies across our 8 case studies, a unified benchmark is infeasible. Instead, we tailor metrics and datasets to each specific threat model, with the exception of Noisy Upscaling [ 40 ] and LightShed [ 31 ] , which we evaluate jointly due to their shared settings. To maintain focus, we present primary findings in the main text, relegating implementation details and auxiliary results to the Appendix.

[40] h2: III Attack Methodology

[41] p: Given a protected image, we use an off-the-shelf img2img model, guided by a text prompt, as a “denoiser” to remove the (protective) perturbations in the image. There is no protection-specific adaptation or further fine-tuning of the img2img model.

[42] p: Denoising models. We use five models: four open-source Diffusion models and one closed-source commercial model.

[43] p: FLUX (FLUX.1 [dev]) [ 11 ] , a Diffusion-based model, enables photorealistic image generation and high-fidelity editing with 12B parameters.

[44] p: SD3 (Stable Diffusion 3 Medium) [ 24 ] with 2B parameters is one of the latest models from Stability AI.

[45] p: SDXL (Stable Diffusion XL Refiner) [ 82 ] with 6.6B parameters employs a two-stage ensemble model that offers superior composition and text-instruction following capabilities, just behind SD3 and FLUX in quality evaluations [ 24 , 5 ] .

[46] p: SD1.5 (Stable Diffusion 1.5) [ 87 ] with approximately 890M parameters is a widely used model.

[47] p: GPT-4o (GPT Image 1) [ 33 , 45 ] is an Autoregressive model from OpenAI that generates extremely high-quality images [ 48 , 130 ] . Currently, architectural and training details are unknown. OpenAI has been consistently releasing high-performing GenAI models [ 80 ] and we expect GPT-4o to perform significantly better than open-source models. Due to GPT-4o’s pricing and our budget restrictions, we use GPT-4o on a subset of images for certain case studies. The subset is carefully chosen to be the most difficult for open-source models to denoise.

[48] p: Denoising methodology. Given a perturbed image, we use a simple text prompt (e.g., “Denoise the image”) to guide generation of the denoised image. All models support prompt-guided generation, so any user with API access and a chosen prompt can denoise images this way. Prompts can be positive (e.g., “Denoise the image”) to condition denoising on, or negative (e.g., “Add noise to the image”) to condition against. Positive and negative prompts are tokenized and used to condition attention blocks during denoising. We evaluate 8 positive–negative prompt pairs (Table IX in the Appendix). The FLUX model does not support negative prompts and is tested only with positive prompts. All prompts are simple, intuitive denoising instructions; we use no special rules or prompt optimizations.

[49] p: In all experiments, we input images to each denoising model at a resolution of 512 × 512 512\times 512 (the original training resolution for many models). 1 1 1 In Case Studies 1, 6, and 7, the initial datasets contain 256 × 256 256\times 256 images, which we upscale to 512 × 512 512\times 512 using the Stable Diffusion Upscaler [ 87 ] . Other hyperparameter settings for each case study are detailed in Sections IV and V .

[50] p: Why off-the-shelf img2img models? Our intuition is based on the following key characteristics of current models:

[51] p: (1) Latent space representation to compress irrelevant information: All four Diffusion models we use operate in a latent space, i.e., the source image is encoded into a lower-dimensional latent space, manipulated, and then decoded back to the pixel space. This compression captures the most perceptually relevant features, thus potentially removing any noise (perturbations) in an image.

[52] p: (2) Advances in generative process aids with denoising: We use both Diffusion and Autoregressive (GPT-4o) models. Diffusion models learn by adding noise to the latent representation in the Forward Diffusion process, followed by reconstructing the source image by iteratively removing the noise at each step in the Reverse Diffusion process. This Diffusion process has significantly advanced over time. We select models that utilize various Diffusion processes. SD1.5 and SDXL utilize SDEdit [ 75 ] for realistic image synthesis through iterative denoising with a Stochastic Differential Equation. SD3 and FLUX are Rectified Flow models that transform noise to data linearly, improving efficiency with fewer denoising steps and improving image quality. This noise-removal process of Diffusion models makes them suitable for removing perturbations.

[53] p: During inference, we use two key hyperparameters: (a) Strength: A parameter ranging from 0 to 1 that determines the amount of noise added, where 0 adds no noise and 1 dissolves the image into random noise. Higher values can more effectively destroy perturbations, but risk altering source characteristics (e.g., facial identity). (b) Number of inference steps: This parameter sets the number of denoising steps, with more steps enhancing image quality but slowing inference.

[54] p: Autoregressive models such as GPT-4o, despite unknown architecture, use a generative process aiding effective denoising. These models have strong contextual awareness [ 48 ] , i.e., the generation of a new pixel is conditioned on the source image and all the pixels it has already generated. This can enhance the correction of corrupted (perturbed) pixels. Similarly, the U-Net backbone [ 88 ] in Diffusion models uses a wide receptive field that captures contextual information surrounding a larger area, helping to differentiate between essential details and noise that should be removed.

[55] p: (3) Improved knowledge of distribution of clean images: Current models are trained on web-scale datasets (e.g., LAION-5B [ 95 ] ) of high quality, noise-free images, helping to better learn the mapping from noisy inputs to clean outputs.

[56] p: (4) Guidance-based generation capability: We steer generation with a text prompt that emphasizes noise removal. The strong text-conditioning abilities of these models further improve denoising. Models like GPT-4o are natively multimodal, providing a deep understanding of language–vision relationships. In Section VII , we show that prompt-guided denoising often outperforms prompt-free denoising.

[57] h2: IV Our Attack Against Existing Defenses

[58] p: We evaluate our attack on data protection schemes through four case studies, addressing RQ1 – RQ3 . For each study, results use the best of eight prompt combinations by denoising performance (prompts in Table IX , Appendix).

[59] p: Baselines: We compare our attack with the perturbation removal baselines used in each case study. In addition, we use a common baseline based on DiffPure [ 79 ] , a denoising strategy originally proposed to purify adversarial samples in classification settings. DiffPure uses a Diffusion model based on DDPM [ 39 ] , which operates in the pixel space, unlike our approach, which operates in the latent space (LDM [ 87 ] ). DiffPure does not require a prompt and instead relies on the Diffusion process to remove perturbations.

[60] h3: IV-A Case Study 1: Mitigating Deepfake Manipulations (USENIX Security’23)

[61] p: Defense background. UnGANable [ 61 ] protects face images ( target images) from unauthorized GAN-based deepfake manipulations. In such attacks, the adversary inverts the target image into a latent code ( GAN inversion ), modifies it, and reconstructs an image with desired facial features. UnGANable adds imperceptible perturbations to the target image to disrupt inversion, yielding inaccurate latent codes and blocking manipulation. Our goal is to remove these protective perturbations to enable successful GAN inversion, verified by matching the reconstructed image’s facial identity with the target image.

[62] p: Experimental setup. Detailed setup is in Appendix -B .

[63] p: Defense setup: We reproduce the evaluation in UnGANable work focusing on protecting face images generated using StyleGANv2 [ 52 ] . We start with 500 256 × 256 256\times 256 face images, from which we eliminate images that are not successfully protected by UnGANable. We use the black-box setting of UnGANable, i.e., the defender has no knowledge of the attacker’s GAN model. UnGANable bounds the perturbations using the L ∞ L_{\infty} measure using the budget parameter ϵ \epsilon . We experiment with ϵ \epsilon values of 0.05, 0.06 and 0.07 which achieved the best results in the UnGANable work.

[64] p: Baselines for comparison: We compare our attack with Gaussian Smoothing (used by UnGANable) and DiffPure [ 79 ] .

[65] p: Attack evaluation metrics : (1) Matching Rate: We measure the percentage of reconstructed images that match the identity of the corresponding target images, indicating a successful attack. Values range from 0 to 1, with 1 indicating a perfect attack. (2) Utility measures: We compare the denoised images with the corresponding original target images using the same utility measures used by UnGANable. This includes Structural Similarity Index Measure (SSIM) [ 120 ] , Peak Signal-to-Noise Ratio (PSNR), and Mean Squared Error (MSE). Higher PSNR and SSIM and lower MSE indicate better attack performance.

[66] figure: TABLE II: Denoising results for UnGANable. The best results for each metric are bolded . The highlighted row indicates the best model of our pipeline in terms of performance and utility. ϵ = \epsilon= 0.06 Attacker Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ No attack 0.00% 32.417 0.924 0.0006 Smoothing 63.25% 32.355 0.947 0.0006 DiffPure 48.29% 25.781 0.830 0.0028 SD1.5 63.25% 29.077 0.904 0.0013 SDXL 63.68% 30.726 0.925 0.0010 SD3 77.78% 31.488 0.937 0.0007 FLUX 76.07% 31.552 0.941 0.0007

[67] figure: Fig. 1 : Images in bottom row are generated with StyleGANv2 using their respective top row image as an input. SD3 better restores the original face features compared to the baselines.

[68] p: Results. We report the performance for Prompt C6 (Table IX ) that yielded the best denoising results. Table II shows the results for ϵ = 0.06 \epsilon=0.06 . Results for other chosen ϵ \epsilon values are in Table X (Appendix) providing similar takeaways.

[69] p: RQ1: Our attack easily circumvents UnGANable. Without an attack, all images have a Matching Rate of 0.0% (i.e., perfect defense). Using the SD3 model, at ϵ = 0.06 \epsilon=0.06 , we achieve a high Matching Rate of 77.8%, significantly outperforming the baseline attacks (Gaussian Smoothing and DiffPure). The fact that Gaussian Smoothing can achieve a Matching Rate of 63% further highlights the limitations of UnGANable. Note that any non-zero Matching Rate is undesired because it places those individuals at risk for serious deepfake manipulation threats.

[70] p: RQ2: Models with more effective diffusion/generative processes (Section III ) are indeed more capable. FLUX and SD3 outperforms SDXL and SD1.5. GPT-4o (not shown in Table II ) when applied to the remaining images where SD3 failed, boosted the SD3 Matching Rate from 77.8% to 78.6%.

[71] p: RQ3: Our attack preserves data utility. We show sample images in Figure 1 , and additional samples in Figure 8 (Appendix). Our attack achieves comparable data utility measures (SSIM, PSNR and MSE) when compared to Gaussian Smoothing. We outperform DiffPure based on PSNR and SSIM, and achieve comparable and low MSE scores.

[72] p: GPT-4o substantially enhanced the image quality to the point where the denoised image is of higher quality than the target image, rendering our chosen utility metrics ineffective. We measure this using the SER-FIQ [ 109 ] metric, a state-of-the-art referenceless face image quality metric. GPT-4o improved the SER-FIQ scores of the target images from 0.54 to 0.64. We further discuss this metric in Appendix -B . A GPT-4o image sample is shown in Figure 9 (Appendix).

[73] p: We highlight two key findings. Finding 1. Off-the-shelf img2img models can even remove sophisticated perturbations aimed at protecting specialized semantic properties, i.e., facial identity features. Finding 2. img2img models that perform translation within a latent space are more successful at stripping away protections than Diffusion-based approaches that operate directly in pixel space (DiffPure). This observation further corroborates our intuition discussed in Section III .

[74] h3: IV-B Case Study 2: In-Processing Watermark (ICLR’25)

[75] p: Defense background. PRC Watermark [ 34 ] is the state-of-the-art method for in-processing watermarking in the latent space, where the watermark is applied during image generation from a prompt. PRC Watermark uses a cryptographically pseudo-random pattern that is embedded across the latent space, allowing operation at a semantic level and helping to preserve image quality. It outperforms Stable Signature [ 30 ] and Tree-Ring Watermarking (TRW) [ 123 ] , and is shown to be robust to pixel-level watermark removal attacks [ 146 ] .

[76] p: Our goal is to remove the watermark so that watermark verification fails.

[77] p: Experimental setup. Detailed setup is in Appendix -C .

[78] p: Defense setup: We reproduce PRC Watermark’s evaluation pipeline using randomly sampled prompts from the Stable Diffusion Prompt (SDP) dataset [ 103 ] to produce 500 512 × 512 512\times 512 images with and without watermarking.

[79] p: Baselines for comparison: Similar to the original work, we use Gaussian Smoothing and Regen-VAE [ 146 ] . Regen-VAE is an attack specially designed to remove watermarks. It uses a VAE model to create a latent code that is subsequently noised and then reconstructed to disrupt the watermark. There are Regen-VAE variants, B and C , based on state-of-the-art image compression performance (see details in Appendix -C ). We also include DiffPure.

[80] p: Attack evaluation metrics: (1) TPR@FPR: Similar to the original work, we calculate TPR@FPR (FPR=0.00001), ranging between 0 and 1, to measure watermarking performance. Lower values indicate better attack performance. (2) Utility measures: Similar to the original work, we use PSNR and SSIM (interpreted in the same way as Case Study 1) to measure impact on image quality. In this case, these metrics are computed between watermarked and denoised images. Additionally, we use Kernel Inception Distance (KID) [ 10 ] , computed between unwatermarked and denoised images. 2 2 2 PRC Watermark and other case studies used the FID metric [ 38 ] , but this metric is known to show significant biases for smaller sample sizes like ours. A lower KID value indicates better attack performance.

[81] figure: TABLE III: Denoising results for PRC Watermark. FLUX demonstrates the best balance between performance and utility. Attacker TPR@FPR ↓ PSNR ↑ SSIM ↑ KID ↓ No attack 1.000 - - 0.0183 Smoothing (Avg.) 1.000 30.656 0.868 0.0294 DiffPure 0.280 21.694 0.305 0.0302 Regen-VAE B 0.312 28.859 0.770 0.0618 SD1.5 0.878 23.314 0.611 0.0248 SDXL 0.000 24.018 0.652 0.0142 SD3 0.262 25.613 0.700 0.0196 FLUX 0.258 28.042 0.775 0.0196

[82] figure: Fig. 2 : Qualitative image samples for PRC Watermark. Regen-VAE causes the image to appear blurrier in detail and DiffPure causes the image to appear more sharp and distorted. FLUX is able to preserve better quality during denoising.

[83] p: Results. Prompt C8 (Table IX ) is most effective. The key results are in Table III , with additional results in Table XI (Appendix).

[84] p: RQ1: Our attack is highly effective at removing the PRC Watermark. TPR@FPR is at 1.0 when there is no attack against images, indicating perfect watermarking performance. FLUX provides the best balance in terms of reducing TPR@FPR, while maintaining image quality. FLUX significantly reduces the TPR@FPR value to 0.258 outperforming all the baselines.

[85] p: RQ2: Models with more advanced generative processes and larger capacity are in fact more effective, i.e., FLUX, SD3, and SDXL outperform SD1.5. GPT-4o is applied to a subset of 100 images in which FLUX failed to remove the watermark (sampling strategy in Appendix -C ). GPT-4o results are in Table XII (Appendix). After applying GPT-4o, TPR@FPR was reduced to 0.060 when combined with the results of FLUX, further highlighting the capabilities of more advanced models.

[86] p: RQ3: Our attack has a minimal impact on image quality. Figure 2 shows sample images, and additional samples are in Figure 10 (Appendix). Using FLUX, we achieve the highest SSIM of 0.775, among attacks that degrade TPR@FPR. Among the effective baselines (where TPR@FPR is reduced), we have comparable PSNR values to Regen-VAE and outperform DiffPure. Gaussian Smoothing, despite its better utility, was completely ineffective in lowering TPR@FPR. We also achieve a low KID score of 0.0196, outperforming all baselines. Similar to Case Study 1, GPT-4o significantly enhanced image quality after denoising. Therefore, we use a referenceless widely-used metric called BRISQUE [ 77 ] (lower values are better). 3 3 3 The SER-FIQ [ 109 ] metric used in Case Study 1 is designed for face images and therefore not suitable here. We justify this metric in Appendix -C . GPT-4o achieves a lower BRISQUE score of 2.859 for denoised images, compared to 5.164 for FLUX.

[87] p: Finding 2 holds in this case as well. In addition: Finding 3. Perturbations added through latent-space manipulations can also be removed using img2img models available today. Finding 4. Off-the-shelf img2img models outperform specialized watermark removal attacks (Regen-VAE).

[88] h3: IV-C Case Study 3: Post-Processing Watermark (ICLR’25)

[89] p: Defense background. VINE [ 68 ] is a post-processing watermarking scheme, where the watermark is applied to an existing image. VINE is the state-of-the-art method in terms of robustness against image-editing techniques. VINE achieves robustness by adding invisible watermarks to the low-frequency bands of an image. The intuition is that image editing or image regeneration (like our methodology) tends to remove patterns in the high-frequency bands, and therefore embedding the watermarks in low-frequency bands can provide resilience. Our goal is to remove the watermark such that the watermark verification fails.

[90] p: Experimental setup. Detailed setup is in Appendix -D .

[91] p: Defense setup: We reproduce VINE’s evaluation pipeline and apply their watermark to 1000 512 × 512 512\times 512 images sourced from W-Bench [ 68 ] .

[92] p: Baselines for comparison: VINE evaluates robustness against two image regeneration attacks: Stochastic Regeneration [ 75 , 146 ] and Deterministic Inversion [ 101 , 78 ] . We include these methods as baselines. Both methods use different Diffusion-based strategies to add noise to an image and then denoise it, but unlike our approach, no prompt is involved. They were not originally designed for watermark removal and were instead proposed for more general use cases (e.g., image editing). Both image regeneration methods use the SD2.1 model [ 87 ] . We also compare with Gaussian Smoothing, DiffPure, and Regen-VAE (see Case Study 2).

[93] p: Evaluation metrics: We use the same metrics used by VINE. (1) TPR@FPR: We calculate TPR@FPR (FPR=0.001) to measure watermarking performance. (2) Utility measures: We use PSNR, SSIM, and KID. These metrics can be interpreted similarly to Case Study 2. From VINE, we also use Learned Perceptual Image Patch Similarity (LPIPS) [ 140 ] . LPIPS values lie between 0 and 1 and lower values indicate better attack performance. All these metrics are calculated between unwatermarked and watermarked/denoised images, since we are considering a post-processing watermarking scheme.

[94] figure: TABLE IV: Denoising results for VINE. FLUX exhibits the best balance between performance and utility. Attacker TPR@FPR ↓ PSNR ↑ SSIM ↑ LPIPS ↓ KID ↓ No Denoising 1.000 37.479 0.993 0.007 0.0000 DiffPure 0.991 22.087 0.336 0.575 0.0033 Regen-VAE B 0.976 29.424 0.832 0.275 0.0194 Sto. Regen. 0.981 22.325 0.636 0.270 0.0106 Det. Inver. 0.997 25.408 0.750 0.225 0.0072 FLUX 0.878 26.646 0.775 0.154 0.0006

[95] figure: Fig. 3 : The bottom edge of three W-Bench samples with and without VINE. VINE’s watermarking creates visible perturbations on the edges of an image.

[96] p: Results. Prompt C6 (Table IX ) is most effective. Our key results are in Table IV and full results in Table XIII (Appendix).

[97] p: RQ1: Our attack is moderately effective at degrading TPR@FPR. Our FLUX model degrades TPR@FPR to 0.878 from 1.000, while not significantly impacting image quality. We outperform all the baseline schemes. Our performance can be attributed to the better generative process used by FLUX compared to our baselines and older Stable Diffusion schemes.

[98] p: Is VINE truly robust? We further examined the effect of VINE restricting its perturbations to low-frequency bands, motivated by the observation that TPR@FPR did not drop substantially. Our analysis shows that VINE’s low-frequency design leads to perturbations that concentrate near the image boundaries and are easy to remove. As illustrated in Figure 3 , these artifacts are mainly visible along the image edges. To evaluate this, we apply a simple center-cropping–based perturbation removal technique. Whereas prior center-cropping studies typically remove 10% of the image [ 1 ] , we instead crop only 0.7%, i.e., we retain 99.3% of the original content. After cropping, we resize the image back to 512 × 512 512\times 512 . With just 0.7% cropping, TPR@FPR drops to 0.066, essentially erasing the watermark. Although this center-cropping method is a protection-specific adaptation (and therefore departs from our original, method-agnostic evaluation protocol), it exposes a key design weakness: VINE’s dependence on edge pixels that can be removed with minimal image modification.

[99] p: RQ2: More advanced and bigger capacity models are more effective. FLUX, SD3 and SDXL outperform SD1.5 based on TPR@FPR (see Table XIII in Appendix). We did not test GPT-4o as the simple center cropping attack was sufficient to fully neutralize the protection.

[100] p: RQ3: Our attack has minimal impact on image quality. FLUX achieves the lowest KID and LPIPS scores of 0.0006 and 0.154, respectively, outperforming all baseline schemes. For PSNR and SSIM, FLUX demonstrates values slightly below the Regen-VAE baseline, but outperforms all other baselines. Figure 11 (Appendix) shows sample images.

[101] p: Finding 2 holds in this case as well. Additionally: Finding 5. Using low-frequency bands to insert the watermark is a promising idea. However, the state-of-the-art scheme (VINE) uses an implementation that produces easily removable localized perturbations in watermarked images. Future work can address this issue.

[102] h3: IV-D Case Study 4: Verifying Unauthorized Data Usage in Personalized Models (IEEE S&P’25)

[103] p: Defense background. SIREN [ 59 ] mitigates unauthorized use of images to fine-tune or personalize text-to-image Diffusion models. An unauthorized party can use an artist’s images to personalize a Diffusion model and generate new images that mimic the artist’s style, also known as style mimicry attacks [ 97 ] . SIREN’s idea is to enable data traceability by adding an imperceptible perturbation or coating to an image that can be reliably learned during personalization. SIREN argues that existing watermarking schemes [ 97 , 110 , 64 , 118 , 70 ] are not reliable enough to transfer to output images after personalization. Watermarking schemes are independent of downstream personalization tasks and focus primarily on stealthiness. In contrast, SIREN’s novel coating is designed to be relevant to the personalization task and therefore transfers to the generated images. SIREN implements a human perceptual-aware constraint using a hypersphere classification network to improve imperceptibility and traceability. Our goal is to remove the coating so that data traceability fails. Our attack denoises the images before being used for personalization.

[104] p: Experimental setup. Detailed setup is in Appendix -E .

[105] p: Defense setup: We reproduce the experimental setup in the original work. We use the Pokemon [ 49 ] dataset (used by SIREN) consisting of 819 512 × 512 512\times 512 images and associated captions generated using BLIP [ 60 ] . We use SD1.5 as the text-to-image model to personalize with “an image of a Pokemon” as the personalization prompt. The model is fine-tuned on the Pokemon dataset, then used to generate 1000 images. For the SIREN encoder (coating mechanism) and decoder (verification scheme), we use the provided pretrained checkpoints.

[106] p: Baselines for comparison: We compare our attack with Regen-VAE [ 146 ] , which SIREN identifies as the most effective purification attack. In addition, we compare with DiffPure.

[107] p: Evaluation metrics: We use the following metrics used in the original work. (1) TPR@Significance: We calculate TPR@Significance to measure traceability performance. Significance serves as a threshold for the Kolmogorov-Smirnov test [ 73 ] to determine whether a generated image is traced to SIREN-coated training data. SIREN uses a Significance of α = 10 − 9 \alpha=10^{-9} where a high TPR indicates reliable data tracing. (2) Utility measures: Similar to SIREN, we use PSNR, SSIM, and LPIPS (interpreted in the same way as Case Study 3) measured between clean (without coating) and protected/denoised images. We also use KID to measure the generation quality between clean and generated images.

[108] figure: TABLE V: Denoising results for SIREN. FLUX exhibits the best balance between performance and utility. Attacker TPR@Sign. ↓ PSNR ↑ SSIM ↑ KID ↓ LPIPS ↓ No attack 1.000 39.142 0.880 0.070 0.016 DiffPure 0.101 29.835 0.596 0.084 0.215 Regen-VAE C 0.591 31.886 0.890 0.071 0.085 SD1.5 0.147 22.348 0.803 0.100 0.122 SDXL 0.000 22.049 0.765 0.100 0.136 SD3 0.001 22.935 0.612 0.112 0.121 FLUX 0.016 28.882 0.787 0.071 0.050

[109] p: Results. Prompt C6 (Table IX in Appendix) yielded the best denoising performance. Results are in Table V (with additional results in Table XIV in the Appendix).

[110] p: RQ1: Our attack is highly effective at removing the SIREN coating. Without an attack, SIREN protection is perfect at a TPR of 1.000 allowing every image to be traced to the protection. Among our different models, FLUX performs the best in terms of TPR and utility metrics. With FLUX, TPR is reduced to 0.016. We outperform all baselines, including Regen-VAE which only achieves a TPR of 0.591.

[111] p: RQ2: More advanced models with larger capacity are more effective. FLUX, SD3, and SDXL all outperform SD1.5, which still produced a low TPR of 0.147. We did not test GPT-4o as the open-source models effectively neutralize the protection.

[112] p: RQ3: Our attack has a minimal impact on image quality. FLUX achieves the lowest LPIPS of 0.050 outperforming all baseline schemes. Our FLUX and SD1.5 models achieve a high SSIM of 0.79 and 0.80, respectively, and is only outperformed by Regen-VAE with an SSIM of 0.89. However, recall that Regen-VAE is much less effective at lowering TPR (i.e., attack performance). Our FLUX model achieves comparable KID and PSNR values to Regen-VAE and DiffPure. Figure 12 (Appendix) shows sample images.

[113] p: In addition to Finding 2, we highlight the following: Finding 6. Protective coatings designed to survive downstream fine-tuning tasks can be effectively removed by off-the-shelf img2img models. Future work can focus on more robust data traceability schemes for personalization tasks.

[114] h2: V Comparing Our Attack Against Protection-Specific Attacks

[115] p: We present 4 case studies that compare our attack against protection-specific attacks, covering RQ4 . In each case study, we aim to match or exceed the performance of existing attacks.

[116] h3: V-A Case Study 5: INSIGHT (USENIX Security’24)

[117] p: Background. INSIGHT [ 3 ] is an attack that removes invisible protections, enabling unauthorized use of images. It targets style mimicry attacks , where an adversary fine-tunes a GenAI model on an artist’s images to generate new works that mimic the artist’s style. Following the original work, we attack Mist [ 62 ] , a data protection scheme that adds imperceptible perturbations to images to mitigate such attacks. We compare our attack with INSIGHT, focusing on removing Mist’s protective perturbations.

[118] p: INSIGHT uses a sophisticated method to remove perturbations. Given a protected image, the key insight is to build a denoising framework that aligns the protected image towards a carefully chosen reference image. The reference image is created by taking a photo of the protected image, which serves as a reference for how humans perceive a protected image (since perturbations are mostly imperceptible). This denoising framework includes a carefully tuned optimization scheme using VAE and UNet models.

[119] p: Experimental setup. Detailed setup is in Appendix -F .

[120] p: Attack setup: We use a dataset provided by the INSIGHT work. This includes 19 512 × 512 512\times 512 Mist-protected WikiArt [ 106 ] images of Van Gogh, as well as the photo-captured variants of each image (i.e., reference images). 4 4 4 We contacted INSIGHT authors requesting a larger dataset which they were not able to provide. The adversary aims to generate new images in the Van Gogh style by fine-tuning an SD1.5 model with DreamBooth [ 90 ] on the denoised images. Based on the performance in Section IV , we choose FLUX as the denoising model. Configuration details are in Appendix -F . As a baseline to understand our attack performance, we study a non-adversarial setting, i.e., analysis of images generated from Mist-protected images under no denoising attack.

[121] p: Evaluation metrics: (1) CLIP Accuracy: As in INSIGHT, we use a pretrained CLIP model [ 86 ] to assess whether generated images match the desired artistic style, reporting Top-1 and Top-3 classification accuracy. A stronger attack yields higher CLIP accuracy, i.e., more images classified as the target style. (2) Utility measures: We use the referenceless BRISQUE metric from Case Study 2 to assess generated-image quality, which is the attacker’s primary concern. Reference-based metrics (SSIM, PSNR) are unsuitable for measuring the quality of generated images, since they naturally differ from the (reference) training images. Instead, following INSIGHT, we compute PSNR and SSIM between unprotected and denoised/protected images, interpreted as in Case Study 1, and additionally report BRISQUE for denoised images.

[122] figure: TABLE VI: Utility and performance results for INSIGHT and FLUX against Mist protection. We measure CLIP accuracy to Van Gogh’s style as performance. FLUX exhibits the best performance and BRISQUE utility. CLIP Accuracy Generated Utility Denoising Utility Attacker Top-1 Top-3 BRISQUE PSNR SSIM BRISQUE Mist 0.0% 1.3% 60.883 25.941 0.813 33.174 + INSIGHT 0.7% 48.2% 29.229 17.945 0.393 28.231 + FLUX 4.1% 74.6% 22.684 19.570 0.431 21.206

[123] figure: Fig. 4 : Qualitative samples for INSIGHT. FLUX provides the best style fit for Van Gogh, greatly improving performance compared to INSIGHT.

[124] p: Results. Results are shown in Table VI .

[125] p: RQ4: Our attack outperforms INSIGHT based on both Top-1 and Top-3 accuracy. Our attack achieves a high Top-3 accuracy of 74.6%, compared to only 48.2% for INSIGHT, rendering the Mist protection scheme ineffective. Our attack also outperforms INSIGHT based on SSIM, PSNR, and BRISQUE scores. We achieve the lowest BRISQUE (lower is better) of 22.68, compared to a score of 60.88 when there is no attack and 29.23 for INSIGHT. This quality is also visually reflected in the sample images of Figure 4 (more samples in Figure 13 (Appendix)).

[126] p: Finding 7. Studies aimed at creating advanced protection-removal attacks should invariably use off-the-shelf img2img models as a benchmark for comparison. Our results underscore the advantages of employing a simpler method that leverages a robust, off-the-shelf model as opposed to a more complex attack approach.

[127] p: Finding 8. Off-the-shelf img2img models can even outperform protection-removal attacks using a supervised learning approach, e.g., INSIGHT uses reference (clean) images to guide the denoising process. Our attack does not require such reference images or supervision.

[128] h3: V-B Case Studies 6 and 7: Noisy Upscaling (ICLR’25) and LightShed (USENIX Security’25)

[129] p: Background. Noisy Upscaling [ 40 ] and LightShed [ 31 ] are designed to remove protections to mitigate style mimicry. In fact, both schemes were originally evaluated against the Mist [ 62 ] protection scheme (also used in Case Study 4). Therefore, we study these schemes together in this section.

[130] p: Noisy Upscaling removes perturbations by first adding Gaussian noise to an image and then applying the Stable Diffusion Upscaler [ 87 ] to it. Directly using the SD Upscaler does not remove any noise; however, the addition of Gaussian noise in the first step helps with purification. This is because the SD Upscaler is originally trained on images augmented with Gaussian Noise. LightShed is a more sophisticated scheme. Unlike Noisy Upscaling and our approach, LightShed uses a supervised learning scheme. As protection tools are usually made publicly available, LightShed assumes that the attacker can create a paired dataset of clean and protected versions of images. Such a dataset is used to train an Autoencoder with sophisticated loss terms to extract the perturbations in an image. The extracted perturbation is subsequently subtracted from the protected image to obtain the purified image.

[131] p: Experimental setup. Detailed setup is in Appendix -G .

[132] p: Attack setup: We use the attack setup studied in the Mist work that personalizes text-to-image models for style mimicry. Given a limited set of art images (e.g., 5 images), the adversary aims to generate new variations that mimic their content or style. This is implemented using Textual Inversion [ 32 ] , where a given limited set of images is used to find a new pseudo word , S ∗ S^{*} in the embedding space of a frozen text-to-image LDM [ 87 ] model. This pseudo word is then used to condition the LDM model by leveraging its text-to-image functionality to generate new style mimicking variations, e.g., using a prompt “a photo of S ∗ S^{*} ”.

[133] p: We use the LAION-Aesthetic dataset [ 95 , 25 ] (used by LightShed) and filter 100 cat images (sampling strategy in Appendix -G ). We create 20 5-image groups that are each used to optimize a pseudo-word S ∗ S^{*} . These pseudo-words are then used to conditionally generate 50 images each, obtaining a total of 1000 images. When images are protected using Mist, the defender aims for the pseudo word estimated by the attacker to differ from “cat,” thereby producing images that fail to accurately represent the concept of a cat and appear more visibly distorted. In contrast, the attacker aims to generate images without any visible distortions/perturbations that accurately represent the concept of a cat.

[134] p: For our attack, we choose FLUX and GPT-4o as our denoising models. We use the trained checkpoint provided by LightShed authors (for the Mist protection). More details are provided in Appendix -G .

[135] figure: Fig. 5 : Images in top row are source images. Images in bottom row are generated images from Textual Inversion. Note the high-quality sample produced when using GPT-4o.

[136] p: User study to answer RQ4. We conduct a user study to evaluate the performance of our attack compared to LightShed and Noisy Upscaling. Note that Noisy Upscaling also relied on a user study to assess the performance of their attack. We evaluate across two dimensions: image concept-appropriateness and image quality . A successful attack should score highly across both dimensions. We conduct two IRB approved user studies to answer this question.

[137] p: Study setup: In both user studies, each participant was randomly shown 23 cat image pairs. Out of the 23, three were control image pairs (with gold standard objective answers) and rest were randomly sampled from a set of pre-generated image pairs (using the Textual Inversion pipeline). For each image pair, the users were asked to detect the better image based on image quality (noise levels, presence of artifact) and concept-appropriateness (details of the image, fit with description of cat, prompt response appropriateness and overall realism) along with attention check questions. Ultimately, every image pair is evaluated by 3 participants and we use majority voting to decide the preferred image. We also randomized the order of image pairs, added attention check questions and piloted the study to ensure data quality. More details are in Appendix -H .

[138] p: In the first study , the 20 image pairs for each participant were randomly chosen from a set of 100 image pairs. One image in the pair is always a clean image, i.e., an image generated without Mist protection (and with no attack). The other generated image varies between those produced under Mist protection, or Mist protection further denoised by Noisy Upscaling, LightShed, FLUX, GPT-4o (one chosen randomly). In the second study , the 20 image pairs were randomly chosen from a set of 40 image pairs, where each pair contains one image generated when attacked using GPT-4o, and the other generated when attacked using Noisy Upscaling or LightShed (chosen randomly). We recruited 15 participants from Prolific academic for the first study and 6 for the second study.

[139] p: Study results: Detailed results are in Table XV and Table XVI (Appendix). For the first study, we compute (for each quality and concept-appropriateness question) the proportion of image-pairs where the clean image is perceived to have better utility. For the second study, we compute the proportion of image-pairs where GPT-4o images are perceived to perform better. We then leverage one-sample proportion tests (one-sided) to check if these proportions are statistically significant [ 6 ] . We make four important observations:

[140] p: (1) Our participants labeled a statistically significantly greater proportion (more than 80%) of GPT-4o images as more concept-appropriate than even clean images. In contrast, participants marked a statistically significant majority of clean images having better concept-appropriateness than LightShed images (for all concept-appropriateness metrics) and Noisy Upscaling images (for details and overall realism) images (p value ranged from 1.2 × 10 − 5 1.2\times 10^{-5} to 0.003 0.003 ). We did not observe any statistically significant differences in proportions for cases where Mist and Mist+FLUX was marked as higher/lower quality than clean image.

[141] p: (2) Participants labeled a statistically significant majority of GPT-4o images (in 87% to 100% image pairs) having better concept-appropriateness than both LightShed and Noisy Upscaling images (p value ranged from 1.2 × 10 − 18 1.2\times 10^{-18} to 1.47 × 10 − 5 1.47\times 10^{-5} ).

[142] p: (3) In terms of image quality (noise and artifact) statistically significant greater proportion of GPT-4o images are perceived to have better quality than Noisy Upscaling and LightShed (p value ranged from 2.4 × 10 − 13 2.4\times 10^{-13} to 7.8 × 10 − 8 7.8\times 10^{-8} ). In fact, for 100% of cases users perceived GPT-4o images to have less noise compared to Noisy Upscaling and LightShed. Thus, our results show that GPT-4o preserves image utility to a greater extent than competing methods—in terms of both quality and concept-appropriateness.

[143] p: (4) LightShed fails to effectively remove the Mist protection. Our participants labeled a statistically significant greater proportion of clean images (over 85%) as more concept-appropriate (for all concept-appropriateness metrics) and of better quality (for all quality metrics) than LightShed images ( p < 0.0001 p<0.0001 ). This further highlights the limitations of a supervised approach.

[144] p: Findings 7 and 8 (Section V-A ) are applicable here.

[145] h3: V-C Case Study 8: UnMarker (IEEE S&P’25)

[146] p: Background. UnMarker [ 53 ] is a universal watermark removal attack. It observes that robust watermarks must lie in spectral amplitudes rather than spatial structure (pixel values), i.e., across different image frequency bands. UnMarker targets semantic watermarks like Tree-Ring Watermark (TRW) [ 123 ] , which are embedded in low-frequency amplitudes and are hard to remove [ 146 , 91 ] . Note that such semantic watermarks can significantly alter content while remaining imperceptible. UnMarker’s core idea is to disrupt the spectral amplitudes where robust watermarks reside, attacking both high- and low-frequency components. For low frequencies, UnMarker employs a trainable filter; additionally, it applies cropping (up to 10%) to further weaken semantic watermarks. Recall that in Case Study 3, the VINE watermarking scheme was nearly defeated by simple cropping. We compare our attack with UnMarker, focusing on removing the TRW watermark.

[147] p: Experimental setup. Detailed setup is in Appendix -I .

[148] p: Attack setup: Following UnMarker’s evaluation, we use a dataset of 100 SDP [ 103 ] prompts to generate watermarked and unwatermarked images. We focus on two key variants of UnMarker—a L variant that only performs low-frequency disruption, and a HL variant that performs both high- and low-frequency disruption. In Appendix -I , we present results for two additional variants that incorporate cropping ( C ), denoted as corresponding CL and CHL variants. For our attack, we choose FLUX and GPT-4o as our denoising models.

[149] p: Evaluation metrics: (1) Inverse Distance and TPR@FPR: Following UnMarker, we use Inverse Distance and TPR@FPR for attack performance. Inverse Distance is the inverse of the average Mean Absolute Error (MAE) of extracted watermark sequences. Lower values indicate better attack performance. TPR@FPR (FPR=0.01) is also used to measure the detection performance of watermarks. Lower values are better for attacks. (2) Utility metrics: Attacker aims to have high-quality unwatermarked images. We use the BRISQUE referenceless metric from Case Study 2 to measure the quality of the denoised images (lower is better). To further assess how much the denoised images deviate from their watermarked counterparts, we use CLIP FID [ 55 ] , calculated between watermarked and denoised images. Lower value would indicate that the denoised image distribution is closer to the watermarked versions.

[150] figure: TABLE VII: Denoising results for TRW comparing our attack (FLUX and GPT-4o) with UnMarker on no cropping. GPT-4o exhibits best balance between performance & utility. Performance Denoising Utility Protection Inv. Dist. ↓ TPR@FPR = 0.01 ↓ CLIP FID ↓ BRISQUE ↓ UnMarker (HL) 0.0162 0.9011 6.774 62.969 UnMarker (L) 0.0166 0.9560 5.771 7.728 FLUX 0.0153 0.7912 11.549 13.958 GPT-4o 0.0149 0.6813 12.559 8.002

[151] figure: Fig. 6 : Qualitative examples comparing UnMarker with FLUX and GPT-4o on TRW. Note that GPT-4o provided a high quality sample that appears different from the watermarked sample but is still of the same concept.

[152] p: Results. Results are shown in Table VII and additional results are in Table XVII (Appendix).

[153] p: RQ4: GPT-4o and FLUX outperform both variants of UnMarker (HL and L) in Inverse Distance and TPR@FPR metrics. GPT-4o reduces the TPR@FPR from 1.0 to 0.68, which is achieved while maintaining high image quality. GPT-4o achieves a low BRISQUE score, comparable to UnMarker (L). Figure 6 shows image samples. More images are in Figure 16 (Appendix). Figure 6 also indicates that the GPT-4o image looks slightly different from the watermarked image, but maintains the content/theme, i.e., a white tiger wearing a crown with a certain color background. This further explains our CLIP FID results. Although UnMarker shows the least deviation from the watermarked version (at the cost of reduced attack performance), GPT-4o removes watermarks more effectively while regenerating similar images (with some changes).

[154] p: We also experiment with UnMarker variants using 10% cropping (CHL and CL). The results in Table XVII (Appendix) show that UnMarker benefits significantly from cropping, outperforming our attack with a TPR@FPR of 0.18 compared to our GPT-4o’s 0.56. Cropping also improves our attack. UnMarker does not adequately explain why cropping aids in semantic watermark removal. In fact, cropping is not part of their main method and is added only, as an additional step in their experimental sections. We believe, like with VINE (Case Study 3), perturbations are concentrated at image edges.

[155] p: Finding 9. Off-the-shelf img2img models, without any protection-specific optimizations, outperform sophisticated watermark removal attacks. However, if simple cropping is used as an additional step, protection-specific schemes like UnMarker will outperform off-the-shelf img2img approaches. This can be attributed to the spatial biases exhibited by certain watermarking schemes (such as TRW).

[156] h2: VI Countermeasures

[157] p: We study an attack-aware defender who aims to produce perturbations that are resilient to our removal attacks and answers RQ5 . The key idea is to use our denoiser in the protection-generation pipeline. We conduct this study for UnGANable (Case Study 1) and SIREN (Case Study 4). 5 5 5 For VINE (Case Study 3), we already show that denoisers are not needed to remove protection, just simple cropping will suffice. PRC Watermark (Case Study 2) does not provide training code to conduct such an experiment.

[158] p: Attack-aware UnGANable. UnGANable’s protective cloak is computed over a set number of iterations. We design a countermeasure by integrating our SDXL denoiser into this pipeline. 6 6 6 Other denoising models were not compatible with the older libraries used by UnGANable. After each iteration to optimize the cloak, we denoise the adversarial image using SDXL, thereby having the next iteration account for this adversarial modification. We use 17 images where we succeeded in our denoising attack. The defender now aims to create new perturbations for these images that are resilient to our denoising attack. Appendix -J provides more details of UnGANable’s optimization objectives and our experimental configuration.

[159] figure: Fig. 7 : Loss curve for UnGANable with and without the countermeasure. Without the countermeasure (left), loss values display an increasing trend with high magnitude. With the countermeasure (right), loss values plateau after only four training iterations, exhibiting values of low magnitude.

[160] p: We find that this countermeasure is not highly effective in producing attack-resistant perturbations. The Matching Rate dropped to 83% from 100%, i.e., only 17% of the images survived our denoising attack. Results are in Table XVIII (Appendix). To understand this outcome, we analyze the UnGANable optimization loss curves in Figure 7 . Note that UnGANable aims to maximize ℒ t ​ o ​ t ​ a ​ l \mathcal{L}_{total} (see Equation 2 in Appendix). Without the countermeasure, the total loss steadily improves with each iteration. When the countermeasure is applied, the loss value barely exceeds 0.11 and does not improve subsequently. This change in learning behavior suggests that integrating our denoiser destabilizes UnGANable’s optimization scheme.

[161] p: Attack-aware SIREN. We follow a similar strategy for SIREN, by integrating our denoiser into SIREN’s perturbation generation pipeline. Due to space limitations, we discuss this in Appendix -K . We show that our denoising attack can still effectively reduce TPR@FPR from 0.99 to 0.00 for samples using attack-aware perturbations. Our analysis of the loss curves again highlights a trend similar to that observed in the UnGANable countermeasure study.

[162] p: Finding 10. It is challenging to create protective perturbations that are resilient to off-the-shelf img2img models. Future work can study more robust protection schemes. Finding 5 further provides a promising direction.

[163] h2: VII Impact of Hyperparameters and Denoising Adaptations

[164] p: We describe ablation studies to test the impact of our attack hyperparameters, and also evaluate two adaptations to our attack: no-prompt denoising and supervised denoising .

[165] p: Impact of hyperparameters. We discuss the impact of two key hyperparameters of our attack: (1) Text prompt: We use the UnGANable case study to demonstrate the impact of text prompt variations when using our SD3 denoiser. Results are in Table XXVI (Appendix). At ϵ = 0.06 \epsilon=0.06 , the Matching Rate (higher is better) varies from 63% to 78% (average of 69%), suggesting that certain prompts can indeed offer a boost in attack performance. The standard deviation of the Matching Rate is only 4.52%. Prompts C6 and C8 were our best prompts across all the case studies. (2) Strength parameter: This parameter controls the amount of noise added during the Forward Diffusion process and is only applicable to our Diffusion models. We use PRC Watermark (Case Study 2) and SIREN (Case Study 4) to evaluate the impact of the strength parameter. Tables XX and Table XXI in Appendix show the results for PRC and SIREN, respectively. As expected, we see that increasing strength does improve attack performance (e.g., reduce TPR@FPR), but at the cost of reduced image utility (e.g., image quality metrics).

[166] p: Denoising without prompts. Our open-source denoisers (Diffusion models) can be used without a text prompt, by setting the prompt field to an empty string and the guidance scale [ 47 ] parameter to 1. The results are shown in Tables XXII , XXIII , XXIV , and XXVII (all in Appendix) for the 4 case studies in Section IV . We find that prompt-based denoising outperforms the no-prompt approach across all four case studies based on the key evaluation metrics in each case study. One such significant improvement is the TPR@FPR for FLUX on PRC Watermark improving from 0.420 for no-prompt to a lower 0.258 with the prompt-based approach. More results are in Appendix -L .

[167] p: Supervised denoising. Protection tools are usually made publicly available. This allows an attacker to create a paired dataset of protected and unprotected images. We use such a dataset to fine-tune our img2img pipeline for UnGANable (Case Study 1). We use the SDXL denoiser for this experiment. More details are in Appendix -M . With supervised denoising, we obtain a Matching Rate of 69.66% which outperforms unsupervised SDXL’s 63.68%. However, the supervised approach does not outperform our best unsupervised denoiser—SD3 which achieves a Matching Rate of 77.78%. This suggests that models with larger capacities and more effective generative processes can still outperform supervised approaches that use less capable img2img models. Detailed results are in Table XXV (Appendix).

[168] h2: VIII Conclusion

[169] p: This work demonstrates that the arms race between image protection and misuse has reached a critical turning point. Our research reveals that the prevailing assumption that removing protective perturbations requires specialized, purpose-built attacks—is now obsolete. The very GenAI technologies that necessitated these protections have evolved into powerful and universally effective tools for dismantling them. Our key finding is that off-the-shelf img2img models can be easily repurposed as “denoisers” to strip a wide array of protective cloaks from images using simple text prompts. Our attack not only preserves the utility of the image for an adversary but also outperforms existing specialized protection-specific attacks. As GenAI models continue to grow in capability, this threat will only become more severe. Therefore, we stress the urgent need for the research community to develop a new generation of robust protection schemes. We posit that resilience against this simple denoising attack must serve as a fundamental benchmark for any future defense mechanism.

[170] h2: Acknowledgments

[171] p: This material is based upon work supported by the National Science Foundation under grant award numbers 2231002, 1943351, and 2442171. This work is also partially supported by a Google Academic Research Award (GARA).

[172] h2: LLM Usage Considerations

[173] p: Originality. LLMs were used for editorial purposes in this manuscript, and all outputs were inspected by the authors to ensure accuracy and originality.

[174] p: Transparency. We ensure full reproducibility for experiments involving all local models and deterministic algorithms. However, experiments utilizing the GPT-4o API as a denoiser may exhibit minor variations over time due to the continuous updates. Experiments were conducted using publicly available datasets and code repositories, and full methodological details are provided in the paper. We released all the relevant code, datasets, and model checkpoints together with comprehensive instructions and scripts to reproduce all analyses and figures.

[175] p: Responsibility. We performed an extensive evaluation across 8 different case studies. To prioritize efficiency and reduce environmental impact, we intentionally selected representative experimental pipelines for each of the papers instead of exhaustively replicating every reported result. For our GPT-4o experiments, API usage was intentionally minimized and targeted to the most challenging samples to establish model capabilities while containing compute and monetary costs. Experimental settings, selection rationale, and implementation details are fully described in the manuscript. All experiments were conducted on NVIDIA hardware: A100 GPUs (80 GB VRAM), Quadro RTX 8000 GPUs, Titan RTX GPUs, and A40 GPUs (48 GB VRAM).

[176] h2: References

[177] h3: -A Ethical Considerations

[178] p: All experiments were conducted in controlled laboratory settings using publicly available code and datasets; no deployed real-world models were attacked in the process. We also followed responsible disclosure prior to submission and communicated our findings to the authors of the protection schemes we found vulnerable: UnGANable, PRC Watermark, VINE, SIREN, Mist, and TRW. We have made code and data publicly available after verifying that their release poses no safety concerns. This supports transparency and reproducibility, and will facilitate future research focused on building stronger protections against unauthorized image use. The total cost of image editing using OpenAI’s GPT-4o amounted to approximately $73.

[179] p: We place a high value on ethical human subjects research —as a result our survey study protocol went through multiple iterations and scrutiny. Researchers and personnel from the Institutional Review Board (IRB)—referred to as the Institute Ethics Committee (IEC) in the university—were actively involved in the process. In the final protocol, participants were provided with a clear explanation of the study’s objectives, the expected time commitment, and the compensation. We also mentioned that this study involved labeling of cat images, in case they have ailurophobia. They were explicitly informed that we would not store any personally identifiable information. They could abort the study at any time. Finally, we removed identifying information like prolific ids from the final stored data and keep the data in a password protected computer situated within our university. In summary, we followed the best ethical research practices to obtain informed consent from participants, preserve participant anonymity and ensure security of the survey data.

[180] figure: TABLE VIII : Published papers using perturbation-based techniques for proactive defense or protection. The publication venues are highlighted in parentheses after each group of citations. Domain Category Published Papers Image Watermarking / Copyright Protection [ 28 ] (AAAI) [ 128 , 72 , 27 ] (ACM MM) [ 142 , 132 ] (CVPR) [ 19 ] (ECCV) [ 107 ] (ICASSP) [ 30 ] (ICCV) [ 34 , 68 ] (ICLR) [ 29 ] (ICML) [ 139 , 35 , 127 , 43 , 123 ] (NeurIPS) [ 71 ] (IEEE TETCI) [ 84 ] (IEEE TIFS) [ 138 , 76 ] (IEEE TMM) [ 69 ] (USENIX Security) Art Style Protection [ 110 ] (ICCV) [ 129 ] (ICLR) [ 62 , 93 ] (ICML) [ 97 ] (USENIX Security) Facial Privacy [ 104 , 112 , 96 , 119 , 42 ] (CVPR) [ 144 ] (ICASSP) [ 122 , 131 ] (ICCV) [ 2 ] (IEEE ICME) [ 111 ] (NeurIPS) [ 57 , 56 , 17 ] (PETS) [ 115 ] (IEEE TIFS) [ 99 ] (USENIX Security) Deepfake Manipulation [ 44 ] (AAAI) [ 116 , 14 ] (CVPR) [ 26 ] (ICASSP) [ 114 ] (IJCAI-ECAI) [ 22 , 85 ] (IEEE TIFS) [ 61 ] (USENIX Security) [ 133 ] (WACV) Data Traceability [ 54 ] (CVPR) [ 118 ] (ICLR) [ 59 ] (IEEE S&P) Video - [ 67 ] (ICASSP) [ 89 ] (ICCV Workshop) [ 36 ] (IEEE Access) [ 4 ] (IEEE ICMLA) [ 105 ] (IEEE LSP) [ 58 ] (IEEE TDSC) [ 13 ] (IEEE TIFS) [ 66 ] (IEEE TIP) [ 100 ] (IEEE TPAMI) [ 102 ] (USENIX Security) Audio - [ 136 , 135 ] (ACM CCS) [ 65 ] (ACSAC) [ 124 , 125 ] (ICASSP) [ 145 ] (LAMPS) [ 23 ] (IEEE LSP) [ 74 ] (IEEE S&P) [ 15 ] (IEEE TDSC) [ 46 ] (USENIX Security) [ 117 ] (WiSec) Text - [ 137 ] (ACL) [ 18 ] (COLT) [ 143 ] (EACL) [ 92 , 37 ] (EMNLP) [ 141 ] (IEEE S&P) [ 113 ] (IEEE TASLP)

[181] figure: TABLE IX: Labels for prompts and negative prompts combinations numbered C1-C8. These prompts are used as part of our denoising pipeline to attack perturbed images. Note that FLUX does not use negative prompts. Label prompts negative prompts C1 Denoise the image Add noise to the image C2 Smoothen the image Add noise to the image C3 Denoise the image while preserving content of the image Add noise to the image C4 Remove adversarial perturbations Add noise to the image C5 Denoise the image Add adversarial perturbation to the image C6 Smoothen the image Add adversarial perturbation to the image C7 Denoise the image while preserving content of the image Add adversarial perturbation to the image C8 Remove adversarial perturbations Add adversarial perturbation to the image

[182] h3: -B Case Study 1: Mitigating Deepfake Manipulations (USENIX Security’23)

[183] figure: TABLE X: Full denoising results for UnGANable on the best prompt (C6) highlighting its performance on perturbation budgets ϵ = { 0.05 , 0.06 , 0.07 } \epsilon=\{0.05,0.06,0.07\} . ϵ = \epsilon= 0.05 ϵ = \epsilon= 0.06 ϵ = \epsilon= 0.07 Attacker Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ No Denoising 0.00% 33.880 0.944 0.0004 0.00% 32.417 0.924 0.0006 0.00% 31.218 0.903 0.0008 Smoothing 57.44% 32.881 0.954 0.0006 63.25% 32.355 0.947 0.0006 56.52% 31.856 0.940 0.0007 DiffPure 45.13% 25.810 0.831 0.0028 48.29% 25.781 0.830 0.0028 46.01% 25.731 0.828 0.0028 SD1.5 64.62% 29.400 0.913 0.0014 63.25% 29.077 0.904 0.0013 54.71% 28.684 0.894 0.0014 SDXL 72.31% 31.097 0.932 0.0008 63.68% 30.726 0.925 0.0010 64.49% 30.388 0.918 0.0010 SD3 75.38% 31.908 0.943 0.0007 77.78% 31.488 0.937 0.0007 71.01% 31.029 0.929 0.0008 FLUX 76.41% 31.940 0.947 0.0007 76.07% 31.552 0.941 0.0007 72.46% 31.148 0.934 0.0008

[184] figure: Fig. 8 : More image samples for UnGANable.

[185] p: Experimental setup.

[186] p: Defense setup: The GAN inversion process is performed using StyleGANv2 [ 52 ] . StyleGANv2 is the second iteration of StyleGAN [ 51 ] , a state-of-the-art model that synthetically generates images using style vectors representing high-level attributes and stochastic variation provided through noise. We choose StyleGANv2 because it is shown to have the best results of UnGANable’s tested inversion models. StyleGANv2 is trained on the Flickr Faces High Quality (FFHQ) dataset [ 51 ] , a high-quality dataset of various human faces.

[187] p: When selecting a cloak, we target the black-box setting, where the defender is unaware of the attacker’s GAN model or inversion technique. From the two cloaks that satisfy this setting, we choose Cloak v1 over Cloak v4. The difference between these methods is that Cloak v1 handles optimization-based inversion, where the inversion process uses random noise as a starting point, instead of hybrid inversion, where an encoded variant of the input image is used instead. The former is the weaker inversion strategy and thus more compelling for showing the attack improvement of our pipeline.

[188] p: Attack setup: We test strength values from 0.025 in increasing increments of 0.025 until we find the optimal strength value. Since 0.05 strength yielded worse utility and performance than 0.025 strength, we choose 0.025. We find that even the most subtle denoising can significantly increase performance. Because UnGANable uses 256 × 256 256\times 256 images, an additional Stable Diffusion Upscaler [ 87 ] step is integrated into the pipeline to keep consistent with other case studies where our pipeline is used for 512 × 512 512\times 512 images. We use Stable Diffusion x4 Upscaler [ 87 ] to perform an upscale to 1024 × 1024 1024\times 1024 with the same positive prompt as the denoising model. We downscale this image to 512 × 512 512\times 512 as the input to our pipeline and subsequently downscale the output to 256 × 256 256\times 256 .

[189] p: Baselines for comparison: We include Gaussian Smoothing and DDPM-based DiffPure [ 79 ] as baselines. Gaussian Smoothing is a pixel averaging method that is tested in UnGANable as an easy-to-apply countermeasure. The process involves using a filter width of k k , representing the nearest k k pixels to average for each pixel. We test filter width values in the set {1,3,5,7,9,11} following UnGANable’s evaluation and report the best results at filter width 3.

[190] p: DiffPure is an adversarial purifier that integrates Diffusion models and strategies such as Denoising Diffusion Probabilistic Models (DDPM) [ 39 ] , a pixel space strategy capable of generating high quality images from noise. DDPM-based DiffPure has been trained on CelebA-HQ [ 50 ] , a high-quality dataset of celebrity faces. We run DiffPure for {200, 300, 400, 500} timesteps of which we report the best DiffPure results at 200 timesteps.

[191] p: Attack evaluation metrics: The Matching Rate is determined by the number of successfully reconstructed images divided by the number of total images. From UnGANable’s implementation, an image is considered successfully reconstructed if the contained faces of the ground truth and reconstructed images have a FaceNet [ 94 ] similarity distance of 0.58 or less, indicating preserved identity. Based on UnGANable’s utility thresholds, an image is considered high-quality if MSE < < 0.001 and SSIM > > 0.9. FLUX, SD3, and SDXL denoising all successfully meet these thresholds. We measure the utility across all 500 images per setting.

[192] figure: Fig. 9 : A GPT-4o image sample for UnGANable. While GPT-4o does not see much improvement in performance, certain face features are recovered during generation better than SD3.

[193] p: Results. RQ3: With GPT-4o on UnGANable, we require the addition of referenceless metrics to better capture the utility of GPT-4o denoised images. We consider the widely-used referenceless BRISQUE [ 77 ] but given Case Study 1’s focus on face images, a referenceless metric centered on that focus is more appropriate. SER-FIQ [ 109 ] is a suitable alternative that outperforms BRISQUE as a referenceless metric for face images. SER-FIQ uses stochastic embedding robustness to measure the quality of face images. SER-FIQ values are bounded between 0 and 1 with higher values indicating better face image quality.

[194] h3: -C Case Study 2: In-processing Watermark (ICLR’25)

[195] figure: TABLE XI: Full denoising results for PRC Watermark on the best prompt (C8). This table includes Regen-VAE C. Attacker TPR@FPR ↓ PSNR ↑ SSIM ↑ KID ↓ No attack 1.000 - - 0.0183 Smoothing (Avg.) 1.000 30.656 0.868 0.0294 DiffPure 0.280 21.694 0.305 0.0302 Regen-VAE B 0.312 28.859 0.770 0.0618 Regen-VAE C 0.360 29.741 0.786 0.0543 SD1.5 0.878 23.314 0.611 0.0248 SDXL 0.000 24.018 0.652 0.0142 SD3 0.262 25.613 0.700 0.0196 FLUX 0.258 28.042 0.775 0.0196

[196] figure: Fig. 10 : More image samples for PRC Watermark.

[197] p: Experimental setup.

[198] p: Defense setup: PRC Watermark provides two watermark verification schemes to evaluate performance: Detect , which detects the presence of the watermark, and Decode , which fully decodes the retrieved watermark. We choose Detect as it is more robust to watermark removal attacks. In terms of hyperparameters, the default settings from the provided public implementation are used. This includes a setting for t t which represents the sparsity of the parity checks that PRC Watermark solves by sampling a pseudorandom pattern. From the implementation, we set t t to 3, the number of inversion steps to 50 and the False Positive Rate (FPR) value to 0.00001. PRC Watermark is implemented such that the resulting FPR will never exceed the provided rate during generation. Given our number of images and the default FPR value, this ensures that every generated image is watermarked.

[199] p: Attack setup: Similar to Case Study 1, we test strength values from 0.025 in increasing increments of 0.025 until we find the optimal strength value. With this strategy, we choose a strength of 0.15 for our denoising pipeline for PRC Watermark. This strength setting is sufficient to remove PRC Watermark while maintaining high utility.

[200] p: Baselines for comparison: We include Gaussian Smoothing, DiffPure [ 79 ] , and Regen-VAE [ 146 ] as baselines. We perform Gaussian Smoothing with filter widths {1, 3, 5, 7, 9, 11}. Unlike Case Study 1, we find that Gaussian Smoothing does not show any improvement for any setting and as such we average the results together.

[201] p: For DiffPure, we once again use the provided DDPM implementation. However, as PRC Watermark does not exclusively use face images, we substitute the CelebA checkpoint for a 512 × 512 512\times 512 ImageNet [ 20 ] Diffusion checkpoint with the class conditioning steps removed. Removing the class conditioning is necessary as we do not have class labels for any of our Section IV case studies. We run this implementation with timesteps {100, 200, 300} from experimentation and report the best results at 100 timesteps.

[202] p: Regen-VAE is a regeneration attack against watermarking that is instantiated with a variational autoencoder (VAE). It utilizes pretrained image compression schemes from the Compress AI library [ 9 ] as VAEs. We report two main variants of Regen-VAE, Regen-VAE B and Regen-VAE C , based on the following image compression models: the hyperprior variant of Bmshj2018 [ 8 ] and the anchor variant of Cheng2020 [ 16 ] , respectively. These models are chosen because they are the two best state-of-the-art image compression models. Cheng2020 is the better of the two compression schemes as it leverages Gaussian mixture models and attention to improve performance. For both Regen-VAE models, compression factors from 1 through 6 are tested and the best denoising results, corresponding to quality 1 for both variants, are reported.

[203] figure: TABLE XII: Denoising results with GPT-4o improvement for PRC Watermark. The 100 remaining images were chosen as the most challenging to denoise. Full Set 100 Remaining Images Attacker TPR@ FPR ↓ KID ↓ TPR@ FPR ↓ BRISQUE ↓ FLUX 0.258 0.0196 1.000 5.164 + GPT-4o 0.060 0.0174 0.010 2.859

[204] p: Results. RQ3: Similarly to Case Study 1, we require referenceless metrics to capture the utility of GPT-4o denoised images. We choose the 100 most easily watermarked images remaining after the attack, after ranking them based on distance to a calculated detection threshold value. A greater distance indicates greater confidence that the PRC Watermark is present. This is done due to budget restrictions and to show whether or not GPT-4o can break the most confident protections. Because PRC Watermark’s image samples are much more abstract and generalized compared to UnGANable, we use BRISQUE [ 77 ] instead of SER-FIQ. BRISQUE is a referenceless image quality evaluator that scores with a bounded value from 0 to 100 where a lower number indicates a higher quality image. BRISQUE has been used as an evaluation metric in other significant related work [ 110 ] . We report the BRISQUE score for a set of images as the average score of that set.

[205] h3: -D Case Study 3: Post-processing Watermark (ICLR’25)

[206] figure: TABLE XIII: Full denoising results for VINE on the best prompt (C6). The performance of SD1.5, SDXL, SD3, Regen-VAE C, and Gaussian Smoothing are included. Attacker TPR@ FPR ↓ PSNR ↑ SSIM ↑ LPIPS ↓ KID ↓ No Denoising 1.000 37.479 0.993 0.007 0.0000 Smoothing (Avg.) 1.000 32.524 0.917 0.182 0.0015 DiffPure 0.991 22.087 0.336 0.575 0.0033 Regen-VAE B 0.976 29.424 0.832 0.275 0.0194 Regen-VAE C 0.982 29.949 0.840 0.240 0.0182 Sto. Regen. 0.981 22.325 0.636 0.270 0.0106 Det. Inver. 0.997 25.408 0.750 0.225 0.0072 SD1.5 0.986 22.786 0.649 0.208 0.0005 SDXL 0.720 22.998 0.675 0.227 0.0037 SD3 0.817 23.867 0.690 0.185 0.0005 FLUX 0.878 26.646 0.775 0.154 0.0006

[207] figure: Fig. 11 : Image samples for VINE. FLUX is able to improve performance without sacrificing significant utility.

[208] p: Experimental setup.

[209] p: Defense setup: To apply the watermark, VINE has two variants: the base model, VINE-B, and a fine-tuned, more robust model, VINE-R. We use the more robust variant as used in the original work. We also use their provided pretrained checkpoints for the VINE-R encoder and decoder. The encoded message used in the watermark is set to the default “Hello World!”.

[210] p: Attack setup: From experimentation, our denoising pipeline is tested starting with strength 0.05 in increments of 0.05. We report the results of strength 0.25, which enables our pipeline to completely outperform all baselines while still providing competitive utility.

[211] p: Baselines for comparison: Stochastic Regeneration adds noise to an image and then denoises it using a Diffusion model given a number of timesteps. It functions similarly to DiffPure with SD2.1 as the Diffusion method. Deterministic Inversion inverts a clean image into a noisy image which is then used to reconstruct the clean image given a number of sampling steps. SD2.1 is also used as the base model for Deterministic Inversion.

[212] p: Following VINE’s evaluation, we perform the Stochastic Regeneration baseline from timesteps 60 to 240 in increments of 20 of which we report the best setting. We similarly report the best setting for Deterministic Inversion, which is tested from sampling steps 15 to 45 in increments of 10. We determine the best settings to be 240 timesteps for Stochastic Regeneration and 15 sampling steps for Deterministic Inversion. We implement Regen-VAE, DiffPure, and Gaussian Smoothing similarly to Case Study 2, with the only exception that the filter width of 11 is not tested for Gaussian Smoothing as VINE also did not test it.

[213] figure: TABLE XIV: Full denoising results for SIREN on the best prompt (C6). The performance of Regen-VAE B is included. Attacker TPR@Sign. ↓ PSNR ↑ SSIM ↑ KID ↓ LPIPS ↓ No Denoising 1.000 39.142 0.880 0.070 0.016 DiffPure 0.101 29.835 0.596 0.084 0.215 Regen-VAE B 0.652 30.552 0.702 0.062 0.110 Regen-VAE C 0.591 31.886 0.890 0.071 0.085 SD1.5 0.147 22.348 0.803 0.100 0.122 SDXL 0.000 22.049 0.765 0.100 0.136 SD3 0.001 22.935 0.612 0.112 0.121 FLUX 0.016 28.882 0.787 0.071 0.050

[214] figure: Fig. 12 : Image samples for SIREN.

[215] h3: -E Case Study 4: Verifying Unauthorized Data Usage in Personalized Models (IEEE S&P’25)

[216] p: Experimental setup.

[217] p: Defense setup: For the SIREN encoder (coating mechanism) and decoder (verification scheme), we use pre-trained checkpoints (fine-tuned for the Pokemon dataset) provided by the authors, configured with the recommended hyperparameters. We use SIREN’s provided Pokemon encoder checkpoint to encode the traceability cloak and the Pokemon decoder to detect the coating within generated images. We use SIREN’s provided script to generate fine-tuned LoRA [ 41 ] checkpoints with pretrained SD1.5 as a starting point. This is done for 80 epochs and with the learning rate set to 0.0001. We use the default parameters when using the fine-tuned checkpoint to generate 1000 images for each denoising setting.

[218] p: Attack setup: Our denoising pipeline is tested from strengths 0.05 to 0.45 in increments of 0.1. We report the results for strength 0.35 from experimentation. This strength provided performance values close to 0 TPR@Significance while maintaining high utility.

[219] p: Attack evaluation metrics: Following SIREN, we use a sample size of 30 for the generated images and perform the Kolmogorov-Smirnov test 10,000 times to obtain TPR@Significance.

[220] h3: -F Case Study 5: INSIGHT (USENIX Security’24)

[221] figure: Fig. 13 : More samples for INSIGHT.

[222] p: Experimental setup.

[223] p: Attack setup. Following their codebase configuration, we run INSIGHT for 500 iterations and follow their selection of loss weights. The total loss consists of four components: the visual bound, the UNet alignment loss, the VAE alignment loss, and the reconstruction loss. From their implementation, the weights for these losses are set to 0.1, 0.01, 1, and 1, respectively.

[224] p: We use the best FLUX setting from PRC Watermark, a latent space protection scheme much like Mist, consisting of prompt C8 and a strength of 0.15. We use these denoised images to fine-tune an SD1.5 model with DreamBooth [ 90 ] training and subsequently generate 1000 images. We keep the settings of DreamBooth consistent for all attacks using a learning rate of 5 ​ e − 6 5e^{-6} and maximum train steps of 400 (from Hugging Face).

[225] p: Evaluation metrics: We perform CLIP accuracy using the top 40 most common WikiArt [ 106 ] styles as classes, with Van Gogh’s art style being the desired class “post impressionism”. We use the standard ViT-B/32 model as our pretrained CLIP model to perform this classification.

[226] h3: -G Case Studies 6 and 7: Noisy Upscaling (ICLR’25) and LightShed (USENIX Security’25)

[227] p: Experimental setup.

[228] p: Attack setup. We use Mist’s latest implementation, Mist v3, as our protection scheme. We use the default parameters for Mist generation including a strength of 16, 100 optimization steps, the “fused” mode for watermarking, and a fused weight of 1. We also set the image size to be consistently 256 × 256 256\times 256 throughout this case study following Mist’s text-to-image generation experiment.

[229] p: Mist’s evaluation utilizes the LSUN-cat [ 134 ] dataset but it is no longer publicly available. As a result, we adopt the higher quality LAION-Aesthetic dataset [ 95 , 25 ] and filter 100 cat images. Specifically, we filter unique images that contain “cat” in their associated captions and have good CLIP scores (using a score threshold of 0.24) corresponding to “a photo of a cat.”

[230] p: For finding the pseudo-word, we use Textual Inversion [ 32 ] ’s provided pretrained checkpoints as a starting point to fine-tune on. We then use the resulting fine-tuned checkpoint as the model to generate images adhering to the pseudo-word. For generation, we use the default parameters from Textual Inversion including a guidance scale of 10 and 50 DDIM steps.

[231] p: For LightShed, we assume that every input image is poisoned and change the output image size from 512 × 512 512\times 512 to 256 × 256 256\times 256 . We use their Autoencoder checkpoint trained on NightShade [ 98 ] , Glaze [ 97 ] , Mist, and MetaCloak [ 64 ] . We use the default hyperparameters for LightShed.

[232] p: For Noisy Upscaling, we use LightShed’s implementation of Noisy Upscaling including its default hyperparameters of a 0.05 standard deviation for the Noise step and a noise level of 160 for the Upscale step. We additionally add a non-adversarial setting only consisting of Mist protection as a baseline for further insights.

[233] p: Using FLUX with prompt C8 and strength 0.15 from PRC Watermark as a starting point, we adjust the strength and inference steps hyperparameters until we obtain FLUX with a strength of 0.35 and inference steps set to 100. Our reasoning for adjusting the timesteps was to determine whether we can improve the quality of generated images after the denoise. We choose the number of inference steps from {28, 50, 100, 300, 500} with 28 being the default number of timesteps for FLUX.

[234] p: Since we use 256 × 256 256\times 256 for this case study, we apply an upscaling step prior to our denoising (both GPT-4o and FLUX) to scale the input image to 512 × 512 512\times 512 . We follow the same Stable Diffusion Upscaler [ 87 ] and scaling strategy as in Case Study 1 (Appendix -B ).

[235] h3: -H Details of User Study for Case Study 6 and 7.

[236] figure: TABLE XV: Proportion of image pairs in Study 1 where the clean image has better utility than the corresponding counterpart generated image given a Mist-protected or denoised input. ** {}^{\textbf{**}} indicates that the corresponding proportion is statistically significant with p < 0.001 p<0.001 and *** {}^{\textbf{***}} indicates p < 0.0001 p<0.0001 . Proportion of image pairs where clean image has better utility Quality metrics ↑ Concept-appropriateness metrics ↑ Noise Artifacts Detail Concept fit Prompt fit Overall realism Clean image vs. Mist + GPT-4o 0.08 *** {}^{\textbf{***}} 0.29 0.10 *** {}^{\textbf{***}} 0.00 *** {}^{\textbf{***}} 0.10 *** {}^{\textbf{***}} 0.18 ** {}^{\textbf{**}} Clean image vs. Mist + FLUX 0.95 *** {}^{\textbf{***}} 0.33 0.20 0.42 0.36 0.30 Clean image vs. Mist + LightShed 0.94 *** {}^{\textbf{***}} 0.88 *** {}^{\textbf{***}} 0.85 *** {}^{\textbf{***}} 0.90 *** {}^{\textbf{***}} 0.90 *** {}^{\textbf{***}} 0.90 *** {}^{\textbf{***}} Clean image vs. Mist + Noisy Upscaling 1.00 *** {}^{\textbf{***}} 0.92 *** {}^{\textbf{***}} 0.93 *** {}^{\textbf{***}} 0.60 0.58 0.85 *** {}^{\textbf{***}} Clean image vs. Mist 1.00 *** {}^{\textbf{***}} 0.40 0.59 0.38 0.31 0.44

[237] figure: TABLE XVI: Proportion of image pairs in Study 2 where the generated image when attacked with GPT-4o has better utility than the corresponding image attacked with Noisy Upscaling or LightShed. *** {}^{\textbf{***}} indicates that the corresponding proportion is statistically significant with p < 0.0001 p<0.0001 . Proportion of image pairs where GPT-4o image has better utility Quality metrics ↑ Concept-appropriateness metrics ↑ Noise Artifacts Detail Concept fit Prompt fit Overall realism GPT-4o vs. LightShed 1.00 *** {}^{\textbf{***}} 0.94 *** {}^{\textbf{***}} 0.87 *** {}^{\textbf{***}} 1.00 *** {}^{\textbf{***}} 0.94 *** {}^{\textbf{***}} 0.94 *** {}^{\textbf{***}} GPT-4o vs. Noisy Upscaling 1.00 *** {}^{\textbf{***}} 0.89 *** {}^{\textbf{***}} 1.00 *** {}^{\textbf{***}} 1.00 *** {}^{\textbf{***}} 1.00 *** {}^{\textbf{***}} 0.95 *** {}^{\textbf{***}}

[238] figure: Fig. 14 : An example of a training phase pair. The right image is an example of a control image as it is not concept-appropriate, showing a car instead of a cat.

[239] figure: Fig. 15 : An example image pair and 2 of the 6 questions presented to participants. The right image is the image generated with GPT-4o, which the participant is unaware of.

[240] p: Study design. Our studies focused on detecting the better image based on image quality ( noise levels, presence of artifact ) and concept-appropriateness ( details of the image, fit with description of “cat”, prompt response appropriateness and overall realism ). Our study protocols were approved by the institution IRB of the author(s) who performed the studies.

[241] p: Each study has two sections: (i) a training phase , where participants were shown three examples (image pairs labeled as “left” image and “right” image) to explain the image labeling guidelines (Figure 14 shows an image pair from the training phase), (ii) a labeling phase , where participants were asked to provide their judgment on image quality and concept-appropriateness for multiple image pairs.

[242] p: For each image pair, the participant answered the following six questions in line with LightShed [ 31 ] :

[243] p: Noise: Which image has more noise?

[244] p: Artifacts: Which image has more artifacts (things look distorted, cut off, unrealistic etc.)?

[245] p: Detail: Which image has more details?

[246] p: Concept fit: Which image fits the description of a “cat” better?

[247] p: Prompt fit: Overall, ignoring the image quality, which image is more appropriate as a response to the prompt ”photo of a cat” given to AI?

[248] p: Overall realism: Based on noise, artifacts, detail, prompt response appropriateness, and your impression, which image looks more like a realistic photo of a cat?

[249] p: Each of these questions have the following options for the participants:

[250] p: Left Image

[251] p: Right Image

[252] p: Both images [have similar noise levels / are similar in terms of artifacts / have similar level of details / fit the description of a cat equally / are similarly appropriate / are of similar quality]

[253] p: Figure 15 shows an example image pair that is presented to the participants for utility evaluation in our survey.

[254] p: Recruitment. We recruited 21 participants, 15 for the first study and 6 for the second study. We ensured that participant pool was mutually exclusive across studies through Prolific recruitment filter. We recruited participants whose first language was English and had an approval rating of at least 50 % 50\% on Prolific [ 83 ] . The average time to complete the studies was 20.9 minutes and the participants were each paid 5 USD.

[255] p: Generating data for user studies. We randomly sample a subset of 110 generated images from the set of 1000 images generated with clean input. For 100 images of this subset, we sample their counterpart generated images given a Mist-protected or denoised input. We sample 20 images from Mist protection, 20 images from LightShed, 20 images from Noisy Upscaling, 20 images from FLUX, and 20 images from GPT-4o in this manner. The remaining 10 images are paired with 10 control images.

[256] p: We sample 2 counterpart images from GPT-4o and apply significant Gaussian Noise to serve as control images for Noise. We sample another 2 counterpart images from GPT-4o and apply significant Gaussian Blurring to serve as control images for Detail. The remaining 6 images are completely unrelated and chosen from various sources such as INSIGHT [ 3 ] generation, dog images with NightShade [ 98 ] poisoning, and Textual Inversion [ 32 ] personalization from MSCOCO [ 63 ] cat images. These serve as control images for Concept fit, Prompt fit, and Overall realism, with the Overall realism control images also having Gaussian Blur and Gaussian Noise applied.

[257] p: For the GPT-4o vs. LightShed and GPT-4o vs. Noisy Upscaling experiments, we sample an additional 80 images, 40 from GPT-4o, 20 from LightShed, and 20 from Noisy Upscaling. They are sampled so that each pair contains two images from denoised inputs that are counterparts of the same clean image.

[258] p: Ensuring data quality. We included multiple attention checks and control image pairs to verify that users answered correctly.

[259] p: Checkboxes were put at the beginning of labeling phase of the study for participants to acknowledge they have understood the instructions in the training phase and are now ready to being the labeling phase.

[260] p: Random attention check questions places throughout the studies – Which number is even?, Please select ”Yes” as the answer to this question., and Which century are we living in? .

[261] p: Finally, the randomly introduced control image pairs acted as additional quality control. The answer to these pairs was obvious and objective: either the left image or the right image was higher quality, but never both.

[262] p: The responses of the participants passed all attention checks and were correct for the control images.

[263] p: Data analysis. For each image pair, we used majority voting to get the final rating of the image against each evaluation criteria for every image pair. We then calculate the proportion of image pairs where majority voted the clean image as having better quality (for first study) or image generated when attacked with GPT-4o with better quality (for second study). We excluded control image pairs from the analysis. We used one-proportion z-test [ 6 ] to check the significance level of this accuracy.

[264] p: Results. The full results for the first and second studies are presented in Tables XV and XVI , respectively.

[265] figure: TABLE XVII: Full denoising results for UnMarker, FLUX, and GPT-4o on TRW. This table shows both the 0% and 10% crop settings. Performance Denoising Utility Protection Inv. Dist. ↓ TPR@MAE = 68.48 ↓ CLIP FID ↓ BRISQUE ↓ UnMarker (HL) 0.0162 0.9011 6.774 62.969 UnMarker (L) 0.0166 0.9560 5.771 7.728 FLUX 0.0153 0.7912 11.549 13.958 GPT-4o 0.0149 0.6813 12.559 8.002 UnMarker (CHL) 0.0140 0.1758 8.785 67.552 UnMarker (CL) 0.0142 0.2857 8.106 16.070 Crop + FLUX 0.0148 0.6044 12.429 23.441 Crop + GPT-4o 0.0146 0.5604 13.209 7.904

[266] figure: Fig. 16 : More examples for UnMarker.

[267] h3: -I Case Study 8: UnMarker (IEEE S&P’25)

[268] p: Background. Tree-Ring Watermarking (TRW) [ 123 ] is a sophisticated watermarking method that embeds a watermarking key into the Fourier Transform of an initial noise vector prior to image generation, making it robust and imperceptible. Alongside TRW, UnMarker also studies the semantic watermarking method StegaStamp [ 108 ] , a watermarking method that robustly encodes hyperlink bitstrings into images imperceptibly. We choose TRW as the semantic scheme to attack due to StegaStamp’s checkpoints being unavailable.

[269] p: Experimental setup.

[270] p: Attack setup. We follow the implementation of TRW based on UnMarker’s codebase which shares the same hyperparameters as TRW’s own implementation, including the choice of TRW-Rings, a watermarking radius of 10, a circle for the shape of the mask, and no additional image distortion. TRW-Rings is the best performing watermark variant of TRW. We follow the provided “TreeRing.yaml” file to set UnMarker’s hyperparameters.

[271] p: As per UnMarker’s evaluation, we use a dataset of 100 SDP [ 103 ] prompts to generate watermarked and unwatermarked images. Of this set, we work with a subset of 91 generated images that can be GPT-4o denoised. Unfortunately, 9 of the 100 watermarked images, despite all being safe, were falsely blocked by GPT-4o’s moderation system as unsafe input.

[272] p: Using FLUX on C8 with strength 0.15 from Case Study 2, we adjust the strength until we obtain a strength of 0.45. This strength allows us to significantly improve performance compared to UnMarker in the no crop setting.

[273] p: Evaluation metrics. UnMarker uses a different threshold than other papers to calculate TPR@FPR (lower is better). Specifically, UnMarker leverages Mean Absolute Error (MAE) to determine whether or not a watermark is considered detected. From experimentation, we select an MAE of 68.48 which is the closest value to the hundredth higher than the lowest MAE of one unwatermarked image (68.47), falsely flagging it as watermarked (i.e. FPR=0.01).

[274] h3: -J Countermeasure Study 1: Denoising-Aware UnGANable

[275] p: Countermeasure setup. UnGANable’s Cloak v1 is defined by Equation 1 where F F is the feature extractor and ℒ t ​ o ​ t ​ a ​ l = ℒ m ​ s ​ e − ℒ c ​ o ​ s \mathcal{L}_{total}=\mathcal{L}_{mse}-\mathcal{L}_{cos} with ℒ m ​ s ​ e \mathcal{L}_{mse} being an MSE similarity loss representing visual similarity and ℒ c ​ o ​ s \mathcal{L}_{cos} being a cosine similarity loss representing perceptual or feature similarity.

[276] table: max x̂ ​ ℒ t ​ o ​ t ​ a ​ l ​ ( F ⁡ ( x̂ ) , F ⁡ ( x ) ) ​ s.t. ​ | x̂ − x | ∞ < ϵ \text{max}_{\textbf{\^{x}}}\mathcal{L}_{total}(F(\textbf{\^{x}}),F(\textbf{x}))\text{ s.t. }|\textbf{\^{x}}-\textbf{x}|_{\infty}<\epsilon (1)

[277] p: The goal is to find a cloaked image x̂ such that it is visually similar to x but their feature spaces, F ⁡ ( x̂ ) F(\textbf{\^{x}}) and F ⁡ ( x ) F(\textbf{x}) respectively, deviate as much as possible. We introduce a denoising function D D as an adversary in the process leading to Equation 2 .

[278] table: max x̂ ​ ℒ t ​ o ​ t ​ a ​ l ​ ( F ⁡ ( D ⁡ ( x̂ ) ) , F ⁡ ( x ) ) ​ s.t. ​ | D ⁡ ( x̂ ) − x | ∞ < ϵ \text{max}_{\textbf{\^{x}}}\mathcal{L}_{total}(F(D(\textbf{\^{x}})),F(\textbf{x}))\text{ s.t. }|D(\textbf{\^{x}})-\textbf{x}|_{\infty}<\epsilon (2)

[279] p: Note that we apply the denoising step after the cloaking step and as such given an initial x̂ 0 , D ⁡ ( CLOSE D( x̂ ) 0 = {}_{0})= x̂ 0 .

[280] p: Defense setup. We follow the defense setup of Case Study 1, where we choose the black-box cloak of UnGANable, Cloak v1, as the protection scheme. We selected SDXL on the best performing prompt C6 as the countermeasure. We start with 20 images, of which we select 17 images in which we succeeded in our attack (i.e., without the countermeasure). We perform this experiment with a perturbation budget of 0.05. When integrating SDXL as a countermeasure, we also integrate the Stable Diffusion Upscaler [ 87 ] to ensure that the input is 512 × 512 512\times 512 . We follow the same strategy as our denoising pipeline for Case Study 1 (Appendix -B ).

[281] p: Attack evaluation metrics. We use the same performance and utility metrics as Case Study 1. (1) Matching Rate: Percentage of reconstructed images that match the identity of the corresponding target images, indicating a successful attack. (2) Utility measures: We use PSNR, SSIM, and MSE to measure image utility (same interpretation as Case Study 1).

[282] figure: TABLE XVIII: The performance and utility of Cloak v1 vs. Cloak v1 with an SDXL countermeasure. The countermeasure fails to add significant protection to images that were unsuccessfully cloaked and harms utility. Attacker Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ UnGANable Cloak v1 100.0% 33.819 0.943 0.0004 + SDXL C6 Denoising 82.4% 29.155 0.928 0.0013

[283] h3: -K Countermeasure Study 2: Denoising-aware SIREN

[284] p: This appendix section outlines our setup and findings for our countermeasure strategy for SIREN.

[285] p: Countermeasure setup. We follow the defense setup of Case Study 4, where we use the Pokemon [ 49 ] dataset to personalize a SD1.5 model to generate 1000 images. The one difference is that we fine-tune our own encoders and decoders instead of using their provided checkpoints for the dataset. We start with their generalized checkpoints as a starting point and fine-tune with the LoRA [ 41 ] checkpoint obtained by running personalization on clean images from Case Study 4. From experimentation, 20 epochs is sufficient to create an encoder and decoder that can properly apply the SIREN coating.

[286] p: SIREN’s total loss, ℒ t ​ o ​ t ​ a ​ l \mathcal{L}_{total} , consists of several loss components defined by the training objective in Equation 3 .

[287] table: min ​ ℒ t ​ o ​ t ​ a ​ l = λ 1 ​ ℒ l ​ e ​ a ​ r ​ n + λ 2 ​ ℒ p ​ e ​ r ​ c ​ e ​ p ​ t + λ 3 ​ ( ℒ h ​ c + + ℒ h ​ c − ) \text{min}_{\textbf{}}\mathcal{L}_{total}=\lambda_{1}\mathcal{L}_{learn}+\lambda_{2}\mathcal{L}_{percept}+\lambda_{3}(\mathcal{L}_{hc}^{+}+\mathcal{L}_{hc}^{-}) (3)

[288] p: ℒ l ​ e ​ a ​ r ​ n \mathcal{L}_{learn} represents the learnability loss which ensures that personalized methods are able to learn the coating as being feature relevant. ℒ p ​ e ​ r ​ c ​ e ​ p ​ t ​ u ​ a ​ l \mathcal{L}_{perceptual} represents the perceptual loss which ensures that the coating is imperceptible. ℒ h ​ c + \mathcal{L}_{hc}^{+} and ℒ h ​ c − \mathcal{L}_{hc}^{-} represent hypersphere classification losses of positive and negative samples, respectively, which ensure that the coating on generated images are detectable. λ 1 , λ 2 , \lambda_{1},\lambda_{2}, and λ 3 \lambda_{3} represent hyperparameters to alter the importance of each loss component.

[289] p: For each epoch where SIREN creates adversarial images through added noise, we integrate our pipeline to denoise those images to serve as an adversary. We specifically choose FLUX and follow the setting from PRC Watermark (Case Study 2). We also fine-tune an encoder and decoder without the countermeasure for the same 20 epochs for fair comparison. The same attack configuration, including evaluation metrics, of Case Study 4 are reused for this experiment. We use our fine-tuned “no countermeasure” decoder as the detection scheme for calculating performance.

[290] figure: TABLE XIX: The performance and utility of SIREN vs. SIREN with a FLUX countermeasure. Adding the countermeasure reduces the protection to 0. Attacker TPR@ Sign. ↓ KID ↓ PSNR ↑ SSIM ↑ LPIPS ↓ SIREN Coating 0.991 0.078 36.040 0.816 0.030 + FLUX 0.000 0.069 36.866 0.827 0.029

[291] figure: Fig. 17 : Loss curve for SIREN with and without the countermeasure. With the countermeasure, loss values increase and fluctuate (right). Without the countermeasure, the loss properly minimizes resulting in effective SIREN coating (left).

[292] p: Results. The results are in Table XIX .

[293] p: RQ5: Similarly to our countermeasure design for UnGANable, applying the countermeasure does not aid the protection. We find that the TPR@Significance decreases from 0.991, which is close to 1 for ideal cloaking, to an abysmal 0.000. This suggests that the countermeasure is hindering the process of learning an effective SIREN coating. This is further supported by examining the loss curves (Figure 17 ). The total loss increases over time and hovers between 0.25 and 0.40 after epoch 8. Without the countermeasure, the total loss properly minimizes as the number of iterations increase.

[294] p: Examining the loss components, we find that ℒ p ​ e ​ r ​ c ​ e ​ p ​ t \mathcal{L}_{percept} , ℒ h ​ c + \mathcal{L}_{hc}^{+} , and ℒ h ​ c − \mathcal{L}_{hc}^{-} exhibit different behavior for the countermeasure. ℒ h ​ c + \mathcal{L}_{hc}^{+} , and ℒ h ​ c − \mathcal{L}_{hc}^{-} closely follow the total loss curve which indicates that the detectability is not well optimized. This is a significant flaw of the countermeasure as it removes the data tracing feature of SIREN. ℒ p ​ e ​ r ​ c ​ e ​ p ​ t ​ u ​ a ​ l \mathcal{L}_{perceptual} also more properly minimizes for the countermeasure, indicating that applying the countermeasure causes the fine-tuning process to instead optimize the imperceptibility of the coating. Considering that the default coating provides high quality, this is not a benefit to the countermeasure. Ultimately, a countermeasure cannot be designed for SIREN as it disrupts the coating process entirely.

[295] figure: TABLE XX: Strength ablation for PRC Watermark. Modifying the strength shows a tradeoff between performance and utility. FLUX TPR@FPR ↓ PSNR ↑ SSIM ↑ KID ↓ Strength 0.05 0.982 32.399 0.894 0.0198 Strength 0.15 0.258 28.042 0.775 0.0196 Strength 0.25 0.002 25.944 0.703 0.0214

[296] figure: TABLE XXI: Strength ablation for SIREN. Modifying the strength shows a tradeoff between performance and utility. FLUX TPR@Sign. ↓ KID ↓ PSNR ↑ SSIM ↑ LPIPS ↓ Strength 0.25 0.089 0.066 31.748 0.828 0.034 Strength 0.35 0.016 0.071 28.882 0.787 0.050 Strength 0.45 0.000 0.079 26.188 0.731 0.075

[297] h3: -L No-prompt Denoising

[298] figure: TABLE XXII: No-prompt denoising results for PRC Watermark. The no-prompt result has a higher TPR@FPR than the with prompt result. Attacker TPR@FPR ↓ PSNR ↑ SSIM ↑ KID ↓ SD1.5 0.862 23.334 0.612 0.0244 SDXL 0.004 24.172 0.657 0.0144 SD3 0.286 25.656 0.701 0.0187 FLUX 0.420 28.478 0.791 0.0199

[299] figure: TABLE XXIII: No-prompt denoising results for VINE-R. The no-prompt result has a higher TPR@FPR than the with prompt result. Attacker TPR@FPR ↓ PSNR ↑ SSIM ↑ LPIPS ↓ KID ↓ SD1.5 0.987 22.863 0.650 0.203 0.0002 SDXL 0.774 23.269 0.682 0.204 0.0008 SD3 0.854 23.911 0.691 0.179 0.0003 FLUX 0.956 27.415 0.797 0.132 0.0001

[300] figure: TABLE XXIV: No-prompt denoising results for SIREN. The no-prompt result has a higher TPR@Significance than the with prompt result. Attacker TPR@Sign. ↓ KID ↓ PSNR ↑ SSIM ↑ LPIPS ↓ SD1.5 0.120 0.091 22.401 0.812 0.121 SDXL 0.000 0.101 22.541 0.745 0.119 SD3 0.015 0.096 23.179 0.636 0.111 FLUX 0.472 0.079 29.243 0.827 0.054

[301] figure: TABLE XXV: Supervised results for UnGANable. Supervised SDXL does not outperform SD3. ϵ = \epsilon= 0.06 Attacker Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ SD3 77.78% 31.488 0.937 0.0007 FLUX 76.07% 31.552 0.941 0.0007 SDXL 63.68% 30.726 0.925 0.0010 Supervised SDXL 69.66% 25.302 0.873 0.0034

[302] figure: TABLE XXVI: Prompt ablation for UnGANable. C2 and C6 are the best performing prompts. ϵ = \epsilon= 0.05 ϵ = \epsilon= 0.06 ϵ = \epsilon= 0.07 SD3 Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Prompt C1 68.21% 31.672 0.939 0.0007 67.09% 31.204 0.931 0.0008 61.96% 30.679 0.921 0.0009 Prompt C2 77.44% 31.923 0.943 0.0007 72.65% 31.495 0.937 0.0007 68.48% 31.044 0.929 0.0008 Prompt C3 73.33% 31.632 0.939 0.0007 65.81% 31.108 0.930 0.0010 63.04% 30.579 0.920 0.0013 Prompt C4 77.44% 31.820 0.942 0.0007 67.09% 31.351 0.935 0.0008 67.39% 30.870 0.926 0.0008 Prompt C5 70.26% 31.671 0.939 0.0007 63.68% 31.193 0.931 0.0008 61.96% 30.640 0.921 0.0009 Prompt C6 75.38% 31.908 0.943 0.0007 77.78% 31.488 0.937 0.0007 71.01% 31.029 0.929 0.0008 Prompt C7 71.28% 31.634 0.939 0.0007 66.24% 31.108 0.930 0.0009 62.68% 30.652 0.921 0.0009 Prompt C8 73.33% 31.803 0.942 0.0007 68.38% 31.342 0.934 0.0008 65.22% 30.864 0.926 0.0008 Average 73.33% 31.758 0.941 0.0007 68.59% 31.286 0.933 0.0008 65.22% 30.795 0.924 0.0009 Standard Deviation 3.33% 0.121 0.002 0.0000 4.52% 0.156 0.003 0.0001 3.41% 0.182 0.004 0.0002

[303] figure: TABLE XXVII: No-prompt denoising results for UnGANable. The no-prompt result for SD3 has a lower Matching Rate than the with prompt result. ϵ = \epsilon= 0.05 ϵ = \epsilon= 0.06 ϵ = \epsilon= 0.07 Attacker Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ Matching Rate ↑ PSNR ↑ SSIM ↑ MSE ↓ SD1.5 68.21% 31.314 0.936 0.0008 66.24% 30.870 0.928 0.0009 64.13% 30.402 0.919 0.0009 SDXL 75.38% 32.513 0.948 0.0006 74.79% 32.064 0.941 0.0006 72.46% 31.580 0.935 0.0007 SD3 73.85% 31.909 0.943 0.0007 70.94% 31.432 0.935 0.0007 68.12% 30.940 0.927 0.0008 FLUX 76.92% 32.150 0.947 0.0006 76.07% 31.708 0.940 0.0007 72.10% 31.238 0.932 0.0008

[304] p: Results. Our no-prompt results can be found in Tables XXII , XXIII , XXIV , and XXVII . For UnGANable, the Matching Rate at the best no-prompt setting is 76.92% which is worse than the best with prompt results of 77.78%. The best models for UNGANable, SD3 and FLUX, obtain similar or worse performance overall to their “with prompt” variants. SDXL no-prompt improves to a competitive 75.38% Matching Rate and provides the best utility of 32.513 PSNR, 0.948 SSIM, and 0.0006 MSE, but it still fails to outperform “with prompt” SD3 and FLUX.

[305] p: Performance metrics for PRC Watermark are worse overall for no-prompt. This is especially true for FLUX in which a worse TPR@FPR of 0.420 is obtained. VINE’s performance for no-prompt is similarly worse overall for all models in our pipeline. This includes FLUX and SDXL in which we obtain 0.956 and 0.774, respectively. For SIREN, we obtain a significantly higher TPR of 0.472 for FLUX (“with prompt” result is 0.016) and similar performance for the other three models.

[306] p: The decrease in performance ultimately outweighs the increase in utility and also shows that setting a prompt can help improve results. As a result, the “with prompt” setting is preferred to answer RQ1 through RQ3 for these case studies.

[307] h3: -M Supervised Denoising

[308] p: The results for supervised denoising are shown in Table XXV . The backbone of this process is Instruction-tuned Stable Diffusion [ 81 ] , where a Stable Diffusion model is fine-tuned on a paired dataset of original and protected images with an edit instruction linking the pairs. Instruction-tuning was introduced through FLAN [ 121 ] and popularized by InstructPix2Pix [ 12 ] . The goal is to learn the cloaking patterns of UnGANable and denoise them for further improvement.

[309] p: We create a paired dataset of 5000 generated images (following Case Study 1’s generation) and set the edit instruction to be the positive prompt of C6. We use this dataset to finetune a “diffusers/sdxl-instructpix2pix-768” model [ 21 ] to remove the cloak and subsequently use the model for denoising. We follow the default configuration of Instruction-tuned Stable Diffusion, with a learning rate of 5 ​ e − 5 5e^{-5} and training steps of 15,000 for the fine-tune process. We follow the same attack configuration and evaluation metrics as Case Study 1.

[310] h2: Instructions for reporting errors

[311] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[312] p: Tip: You can select the relevant text first, to include it in your report.

[313] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[314] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
