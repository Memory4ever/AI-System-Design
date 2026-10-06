[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SemanticVocoder: Bridging Audio Generation and Audio Understanding via Semantic Latents

[3] h6: Abstract

[4] p: Recent audio generation models typically rely on Variational Autoencoders (VAEs) and perform generation within the VAE latent space. Although VAEs excel at compression and reconstruction, their latents inherently encode low-level acoustic details rather than semantically discriminative information, leading to entangled event semantics and complicating the training of generative models. To address these issues, we discard VAE acoustic latents and introduce semantic encoder latents, thereby proposing SemanticVocoder, a generative vocoder that directly synthesizes waveforms from semantic latents. Equipped with SemanticVocoder, our text-to-audio generation model achieves a Fréchet Distance of 12.823 and a Fréchet Audio Distance of 1.709 on the AudioCaps test set, as the introduced semantic latents exhibit superior discriminability compared to acoustic VAE latents. Beyond improved generation performance, it also serves as a promising attempt towards unifying audio understanding and generation within a shared semantic space. Generated samples are available at https://zeyuxie29.github.io/SemanticVocoder/ .

[5] figure: Figure 1: The SemanticVocoder pioneers the generation of waveforms directly from semantic latents, thereby bridging understanding-oriented representations and generation tasks. (Left): Three sub-tasks from the HEAR benchmark are employed to evaluate the latent representations, in which linear classifiers are trained on fixed latents. The semantic latents exhibit a more discriminative semantic structure than the acoustic VAE latents used in previous work. (Right): For the downstream text-to-audio task, a text-to-latent model predicts latents conditioned on input text. The predicted latents are then fed into SemanticVocoder for audio synthesis, yielding superior performance.

[6] h2: 1 Introduction

[7] p: Text-to-audio (TTA) generation has attracted considerable attention and advanced rapidly in recent years. Previous audio generation systems [ 1 , 2 , 3 , 4 , 5 , 6 ] typically follow the classic Latent Diffusion Model (LDM) architecture, which relies on a first-stage Variational Autoencoder (VAE). The VAE compresses audio into compact latents via an encoder and reconstructs the original audio through a latent-to-waveform decoder, while a second-stage text-to-latent generative model performs prediction in this latent space. Because the VAE is fundamentally based on pure acoustic compression, its latent representation is referred to as acoustic latents .

[8] p: However, acoustic latents pose challenges for second-stage generative models. The reconstruction objective compels the VAE encoder to retain fine-grained acoustic details within the latent space. This preservation ensures high-fidelity reconstruction but yields acoustically dense latents, leading to weak semantic discriminability. Moreover, the VAE bottleneck typically employs low-dimensional representations, imposing an upper bound on representation capacity and further limiting semantic information capture (see Table 2 ). Consequently, second-stage models face a challenging cross-modal task: they must map semantic textual captions directly to complex, low-level acoustic variations—an objective substantially more difficult than mapping to high-level semantic structures. These properties are suboptimal for generative modeling

[9] p: We thus attempt to introduce a novel representation to mitigate the adverse effects of VAE acoustic latents for audio generation. An intuitive ideal representation is that extracted by a semantic encoder, which we refer to as semantic latents . To excel in downstream understanding tasks, semantic encoders are optimized to learn latent spaces characterized by strong semantic disentanglement and clear discriminative structure. These high-dimensional, abstract, and semantically rich latents effectively capture the high-level “content” of the audio (e.g., “a dog barking”) rather than fine-grained acoustic details, making them inherently more conducive to generative modeling.

[10] p: However, directly incorporating semantic latents into the classic LDM framework is non-trivial, as such latents prioritize semantic information at the expense of acoustic details, resulting in severe audio distortion when reconstructed through traditional VAE training frameworks. We thus propose the SemanticVocoder , a flow-matching approach that directly synthesizes waveforms from semantic latents in a generative manner. It exhibits the following properties: (1) It leverages high-dimensional semantic latents without dimensionality reduction, thereby preserving well-structured semantic representations. This mitigates issues arising from acoustic redundancy and the low-dimensional bottleneck inherent in VAE latents. (2) It shifts the training paradigm from VAE-based reconstruction to flow-matching driven generation, thus alleviating the objective mismatch between VAE reconstruction and second-stage generation in the original framework. (3) With semantic latents as the anchor, the text-to-latent model and SemanticVocoder can be trained simultaneously, rendering the two models mutually independent and endowing them with plug-and-play capabilities. By contrast, conventional VAEs and second-stage models must be trained sequentially, as the VAE latents vary during VAE training. Our contributions are summarized as follows:

[11] p: We propose SemanticVocoder, which leverages the semantic latents to directly generate waveforms , enabling the audio generation framework to operate in semantic latent space, while eliminating any reliance on VAE modules and alleviating their negative impacts.

[12] p: By incorporating SemanticVocoder, our text-to-audio system achieves excellent performance on AudioCaps, with a Fréchet Distance of 12.823 and a Fréchet Audio Distance of 1.709.

[13] p: SemanticVocoder bridges semantic latents and generation tasks, thereby enabling semantic latents to support unified modeling for both audio generation and audio understanding.

[14] h2: 2 Related works

[15] p: Neural vocoder and audio VAE Neural vocoders, such as HiFi-GAN [ 7 ] and BigVGAN [ 8 ] , typically take intermediate acoustic representations such as mel-spectrograms or audio codec tokens as input, and reconstruct waveforms. On the other hand, VAEs [ 5 , 9 ] follow an encoding–decoding paradigm: they first compress original audio into compact latent representations via an encoder, reconstruct waveforms from these latents through a decoder. Both traditional neural vocoders and VAEs rely exclusively on acoustic representations, which are reconstruction-oriented; in contrast, the proposed SemanticVocoder utilizes semantic latents and is oriented toward generation.

[16] p: Text to audio generation TTA models accept text descriptions and generate corresponding audio. Previous studies, such as AudioLDM2 [ 2 ] , TangoFlux [ 3 ] , and Make-An-Audio [ 4 ] , adopt a two-stage paradigm combining a VAE with a latent diffusion model. The diffusion model generates text-conditioned latents within the VAE latent space, which are subsequently decoded into waveforms by the VAE decoder. This framework has become the mainstream approach for text-to-audio generation in recent years, and our work represents one of the pioneering attempts to build an audio generation framework that dispenses with VAEs entirely.

[17] p: Semantic audio encoder Semantic audio encoders learn high-level semantic representations from large-scale audio datasets, prioritizing semantic content over low-level acoustic details. These latent representations demonstrate strong performance on various audio understanding tasks, such as classification, event detection, and audio-text retrieval, by capturing intrinsic semantic structure. Typical semantic audio encoders include: (1) Contrastive Language-Audio Pre-training (CLAP) models [ 10 , 11 ] , which adopt contrastive learning to align paired audio and text representations while distancing mismatched pairs; (2) supervised pre-trained encoders [ 12 ] , which are trained on large annotated datasets with full supervision to optimize classification objectives and learn task-oriented semantics; (3) Masked Autoencoder (MAE) based encoders [ 13 ] , which adopt a self-supervised masked reconstruction paradigm. By randomly masking and recovering parts of audio spectrograms or latent features, they capture structured semantic patterns without manual annotations. We adopt the MAE semantic encoder in our work, as its reconstruction objective is more closely aligned with our waveform generation task compared to the other two.

[18] h2: 3 Methodology: generative semantic vocoder

[19] p: SemanticVocoder innovatively generates waveforms directly from semantic latents. As illustrated in the upper-lef part of Figure 2 , it consists of: (1) a flow-matching based training strategy; (2) a semantic encoder that extracts semantic latents from input audio; and (3) a generative backbone for waveform prediction.

[20] figure: Figure 2: An overview of SemanticVocoder training, downstream TTA training, and downstream task inference. ( → \rightarrow Blue arrow) SemanticVocoder training: the input audio is fed into a semantic encoder to extract semantic latents, which serve as conditions to train the flow-matching network for waveform prediction. ( → \rightarrow Red arrow) Generative audio DiT training: the input text is processed by a text encoder to obtain textual features, which are used to train the DiT model for generating semantic latents. ( → \rightarrow Black arrow) Downstream task inference: equipped with SemanticVocoder, both audio generation and understanding tasks can be performed within the same semantic latent space.

[21] h3: 3.1 Flow estimator

[22] p: Conventional VAEs are not straightforward for reconstruction from semantic latents, as these latents primarily preserve high-level semantic information while discarding fine-grained acoustic details, thus leading to reconstruction distortions. To address this issue, we propose a generative approach to synthesize waveforms from semantic latents via a flow estimator. Vanilla flow matching learns a velocity field v t ​ ( x t ) v_{t}(x_{t}) that transforms a noise distribution p 0 ​ ( x ) = 𝒩 ⁡ ( 0 , σ 2 ​ I ) p_{0}(x)=\mathcal{N}(0,\sigma^{2}I) to the target distribution p 1 ​ ( x ) p_{1}(x) over a continuous time interval t ∈ [ 0 , 1 ] t\in[0,1] . The trajectory of a sample x t x_{t} follows:

[23] table: d ​ x t d ​ t = v t ​ ( x t ) , x 0 ∼ p 0 ​ ( x ) , x 1 ∼ p 1 ​ ( x ) \frac{dx_{t}}{dt}=v_{t}(x_{t}),\quad x_{0}\sim p_{0}(x),\quad x_{1}\sim p_{1}(x) (1)

[24] p: where x t = ( 1 − t ) ​ x 0 + t ​ x 1 x_{t}=(1-t)x_{0}+tx_{1} denotes the linear interpolation between the initial noise x 0 x_{0} and target data x 1 x_{1} . The training objective is to minimize the Mean Squared Error loss between the predicted velocity field v ^ t ​ ( x t , θ ) \hat{v}_{t}(x_{t};\theta) and the ground-truth velocity v t ∗ = x 1 − x 0 v_{t}^{*}=x_{1}-x_{0} :

[25] table: ℒ FM-velocity = 𝔼 t ∼ 𝒰 ⁡ ( 0 , 1 ) , x 0 ∼ p 0 , x 1 ∼ p 1 ​ [ ‖ v ^ t ​ ( x t , θ ) − v t ∗ ‖ 2 2 ] \mathcal{L}_{\text{FM-velocity}}=\mathbb{E}_{t\sim\mathcal{U}(0,1),x_{0}\sim p_{0},x_{1}\sim p_{1}}\left[\left\|\hat{v}_{t}(x_{t};\theta)-v_{t}^{*}\right\|_{2}^{2}\right] (2)

[26] p: We adopt the improved strategies introduced in Flow2GAN [ 14 ] for better waveform generation. An energy-aware loss scaling method is used to prioritize perceptually critical segments. Furthermore, the model x ^ 1 ​ ( x t , θ ) \hat{x}_{1}(x_{t};\theta) directly predicts the target clean data x 1 x_{1} , since vanilla flow matching with velocity estimation tends to suffer from instability and noise amplification in low-energy audio regions:

[27] table: ℒ FM-data = 𝔼 t ∼ 𝒰 ⁡ ( 0 , 1 ) , x 0 ∼ p 0 , x 1 ∼ p 1 ​ [ ‖ x ^ 1 ​ ( x t , θ ) − x 1 ‖ 2 2 ] \mathcal{L}_{\text{FM-data}}=\mathbb{E}_{t\sim\mathcal{U}(0,1),x_{0}\sim p_{0},x_{1}\sim p_{1}}\left[\left\|\hat{x}_{1}(x_{t};\theta)-x_{1}\right\|_{2}^{2}\right] (3)

[28] h3: 3.2 Semantic encoder

[29] p: We employ a pretrained MAE encoder [ 13 ] to extract semantic latents, as its masked predictive reconstruction paradigm is conceptually analogous to the waveform generation paradigm of SemanticVocoder. During training, the MAE first converts the audio signal into a spectral representation, splits it into patches, and randomly masks a large fraction of these patches. Only the unmasked patches are fed into the encoder to capture global structural patterns and long-range contextual dependencies. A lightweight decoder then reconstructs the masked patches. This training mechanism enables the encoder to learn generalizable and intrinsic semantic patterns that go beyond low-level acoustic details. In practice, the decoder is discarded, and the encoder is used to encode the input audio without masking, yielding implicit features rich in high-level semantic information that serve as semantic latents L semantic L_{\text{semantic}} :

[30] table: L semantic = ℰ MAE ​ ( Patchify ​ ( Mel ​ ( x ) ) ) L_{\text{semantic}}=\mathcal{E}_{\text{MAE}}(\text{Patchify}(\text{Mel}(x))) (4)

[31] h3: 3.3 Generative backbone

[32] p: The generative backbone follows the design of traditional acoustic vocoders [ 15 , 14 , 16 ] and outputs waveforms conditioned on audio latents. It consists of a latent conditioner and a waveform generator.

[33] h4: 3.3.1 Latent conditioner

[34] p: To better integrate the information from semantic latents, we employ a latent conditioner to further encode and map the semantic latents L semantic ∈ ℝ B × D × T L_{\text{semantic}}\in\mathbb{R}^{B\times D\times T} into a suitable feature space, resulting in L semantic ′ ∈ ℝ B × D ′ × T L^{\prime}_{\text{semantic}}\in\mathbb{R}^{B\times D^{\prime}\times T} . Specifically, the latent conditioner begins with a 1D convolutional layer to project features to the target channel size, followed by BiasNorm normalization and a stack of ConvNeXt [ 17 ] blocks. Each ConvNeXt block consists of a grouped convolution for spatial mixing, two pointwise convolutions for channel mixing with PReLU activation in between, and a residual connection for gradient flow.

[35] table: L semantic ′ = ℰ conditioner ​ ( L semantic ) L^{\prime}_{\text{semantic}}=\mathcal{E}_{\text{conditioner}}(L_{\text{semantic}}) (5)

[36] h4: 3.3.2 Waveform generator

[37] p: Waveform reconstruction from complex spectrograms can be effectively achieved via the Inverse Short-Time Fourier Transform (iSTFT) [ 15 , 16 ] . Therefore, we take the Short-Time Fourier Transform (STFT) coefficients x coef x_{\text{coef}} as the network prediction target, which is further converted into the target waveform x 1 x_{1} through iSTFT. Specifically, a flow matching model ℱ ​ ℳ SemanticVocoder \mathcal{FM}_{\text{SemanticVocoder}} is employed to predict x coef x_{\text{coef}} based on the time interval t ∈ 𝒰 ⁡ [ 0 , 1 ] t\in\mathcal{U}[0,1] , the noisy data x t x_{t} , and the conditional semantic latent features L semantic ′ L^{\prime}_{\text{semantic}} :

[38] table: x coef = ℱ ​ ℳ SemanticVocoder ​ ( x t , t , L semantic ′ ) x_{\text{coef}}=\mathcal{FM}_{\text{SemanticVocoder}}\left(x_{t},t,L^{\prime}_{\text{semantic}}\right) (6)

[39] p: To enable ℱ ​ ℳ \mathcal{FM} to adapt to audio of varying complexity, we employ R R parallel ConvNeXt [ 17 ] branches to predict STFT coefficients at different spectral resolutions. The final waveform is obtained by averaging their outputs:

[40] table: x 1 = 1 R ​ ∑ r = 1 R iSTFT R ​ ( x coef- ​ R ​ th ) x_{1}=\frac{1}{R}\sum_{r=1}^{R}\text{iSTFT}_{R}(x_{\text{coef-}R\text{th}}) (7)

[41] p: Each stacked ConvNeXt block shares a similar structure to that in Section 3.3.1 , but is adapted for flow-matching timestep and conditional information, thus modulating the intermediate variable x hidden x_{\text{hidden}} . In detail, the timestep information t t is embedded as t emb t_{\text{emb}} using sinusoidal positional encoding and processed through a MLP (Multilayer Perceptron, denotes as 𝒫 \mathcal{P} ). The embedded timestep features are multiplied, while the conditional features L semantic ′ L^{\prime}_{\text{semantic}} are subsequently added.

[42] table: t emb = 𝒫 time ​ ( SinPE ​ ( t ) ) t_{\text{emb}}=\mathcal{P}_{\text{time}}\left(\text{SinPE}(t)\right) (8)

[43] table: x hidden = x hidden ⊙ ( 1 + t emb ) + 𝒫 latents ​ ( L semantic ′ ) x_{\text{hidden}}=x_{\text{hidden}}\odot(1+t_{\text{emb}})+\mathcal{P}_{\text{latents}}\left(L^{\prime}_{\text{semantic}}\right) (9)

[44] h2: 4 Downstream tasks

[45] p: SemanticVocoder establishes a direct mapping from semantic latents to waveforms, facilitating the integration of these latents into downstream text-to-audio generation. Furthermore, through comparison in downstream understanding tasks, we demonstrate that semantic latents exhibit stronger discriminability and clearer semantic structure, which benefits audio generative modeling.

[46] h3: 4.1 Text to audio generation

[47] p: We employ a Diffusion Transformer (DiT) [ 18 ] for TTA to verify the benefits of introducing semantic latents, as shown in Figure 2 . It uses the vanilla flow-matching strategy described in Section 3.1 . Its prediction target is changed from traditional VAE latents to semantic latents L semantic L_{\text{semantic}} , which are then converted into waveforms by SemanticVocoder. Specifically, a text encoder is utilized to extract textual embeddings c emb c_{\text{emb}} from caption c c . The DiT backbone employs a stack of DiT blocks, which take text embeddings c emb c_{\text{emb}} , timestep embeddings t emb t_{\text{emb}} (Equation 8 ), and noisy latents L noisy L_{\text{noisy}} as inputs.

[48] table: L semantic = ℱ ​ ℳ audioDiT ​ ( L noisy , t , c ) L_{\text{semantic}}=\mathcal{FM}_{\text{audioDiT}}\left(L_{\text{noisy}},t,c\right) (10)

[49] p: Each block utilizes AdaLN (adaptive layer normalization) to incorporate the timestep information and adopts cross-attention to fuse c emb c_{\text{emb}} , thereby modulating the intermediate predicted latent L hidden L_{\text{hidden}} :

[50] table: L hidden = AdaLN ​ ( t emb , L hidden ) L_{\text{hidden}}=\text{AdaLN}\left(t_{\text{emb}},L_{\text{hidden}}\right) (11)

[51] table: L hidden = CrossAttn ​ ( c emb , L hidden ) + L hidden L_{\text{hidden}}=\text{CrossAttn}\left(c_{\text{emb}},L_{\text{hidden}}\right)+L_{\text{hidden}} (12)

[52] figure: Figure 3: Visualization of different latents on HEAR-ESC50, where the 10 most frequent categories are presented. Each audio feature is aggregated by mean pooling along the temporal axis and projected into 2D space via t-SNE. Compared to VAE acoustic latents used in baseline models, semantic latents exhibit a more discriminative structure and superior semantic disentanglement.

[53] h3: 4.2 Audio understanding

[54] p: To demonstrate why semantic latents benefit audio generation, we compare their performance with the original VAE acoustic latents on downstream understanding tasks. We adopt the HEAR benchmark [ 19 ] for evaluation, which trains separate MLPs on fixed latents for various understanding tasks, including multi-class classification, multi-label classification, and event detection.

[55] h2: 5 Implementation

[56] h3: 5.1 Datasets

[57] p: AudioSet [ 20 ] A large-scale human-labeled audio event dataset containing about 2 million 10-second clips from YouTube videos, with annotations across 527 hierarchical audio event categories. AudioCaps [ 21 ] A pioneering audio captioning dataset built upon AudioSet, which consists of about 50K audio clips (10 seconds each) paired with human-written natural language captions. WavCaps [ 22 ] As large-scale weakly-labeled audio captioning dataset. It comprises approximately 400K audio-caption pairs collected from 4 sources. Raw web-harvested descriptions are refined via a three-stage pipeline to filter noise and generate human-like captions.

[58] h3: 5.2 Models setup

[59] p: SemanticVocoder We employ the MAE-based d ​ a ​ s ​ h ​ e ​ n ​ g ​ _ ​ b ​ a ​ s ​ e dasheng\_base [ 13 ] as the semantic encoder due to its strong downstream performance. The latent conditioner employs a 4-layer ConvNeXt with a hidden dimension of 512. We employ three parallel 8-layer ConvNeXt branchs as the flow-matching backbone at different resolutions, corresponding to STFT hop lengths ( 320,160 , 80 ) (320,160,80) and ConvNeXt hidden dimensions ( 768,512,384 ) (768,512,384) , respectively. They target the STFT coefficients of 24 kHz audio, and the final output waveform is obtained by averaging their outputs. SemanticVocoder is trained on AudioSet for 270 epochs with the ScaledAdam optimizer [ 23 ] , with each audio clipped into 1.6-second segments. We use a batch size of 1440. The learning rate starts at 3.5 × 10 − 3 3.5\times 10^{-3} , linearly warmed up to 3.5 × 10 − 2 3.5\times 10^{-2} over the first 500 steps, and decays using the Eden2 scheduler after 7500 steps. During inference, an Euler ODE solver is used with a step size of 200.

[60] p: Text to audio generation The F ​ l ​ a ​ n ​ _ ​ T ​ 5 ​ _ ​ l ​ a ​ r ​ g ​ e Flan\_T5\_large [ 24 ] is employed as the text encoder to extract text embeddings. We utilize 24-layer canonical DiT blocks with a hidden dimension of 1024 and the AdaLN-SOLA fusion mechanism [ 25 , 1 ] . The DiT is pretrained on the combined WavCaps and AudioCaps datasets for 40 epochs, followed by fine-tuning on AudioCaps for 300 epochs, using a batch size of 32, the AdamW optimizer, and a learning rate of 5 × 10 − 5 5\times 10^{-5} . During inference, the Euler ODE solver with 100 steps is used, and the classifier-free guidance scale is set to 3.5 3.5 .

[61] p: Audio understanding We follow the standard protocol of the HEAR benchmark [ 19 ] . Three highly relevant audio understanding tasks are selected: HEAR-DCASE2016 (multi-label detection), HEAR-ESC50 (multi-class classification), and HEAR-FSD50k (multi-label classification). SemanticVocoder uses semantic latents, while other systems employ acoustic latents sampled from VAE encoders.

[62] h3: 5.3 Metrics

[63] p: For text-to-audio generation, we adopt common objective metrics 1 1 1 AudioLDM Eval: https://github.com/haoheliu/audioldm_eval , including FAD, FD, KL divergence, Inception Score (IS), and CLAP similarity 2 2 2 LAION-CLAP: https://github.com/LAION-AI/CLAP LAI MS-CLAP: https://github.com/microsoft/CLAP . Although SemanticVocoder is designed for generative tasks, its reconstruction performance remains comparable to reconstruction models. We therefore also report reconstruction metrics 3 3 3 DAC: https://github.com/descriptinc/descript-audio-codec , including ViSQOL and Mel/STFT/Waveform loss.

[64] h2: 6 Results

[65] p: This section presents the experimental results on text-to-audio generation, semantic representation capability, and reconstruction ability. Additional details and ablation studies are provided in Appendix . High-performing systems, including EzAudio [ 1 ] , AudioLDM2 [ 2 ] , TangoFlux [ 3 ] , MakeAnAudio [ 4 ] , StableAudio [ 5 ] , and MMAudio [ 6 ] , serve as comparative baselines.

[66] figure: System FAD VGG {}_{\text{VGG}} ↓ \downarrow FD PANNs {}_{\text{PANNs}} ↓ \downarrow KL ↓ \downarrow IS ↑ \uparrow CLAP LAION {}_{\text{LAION}} ↑ \uparrow CLAP MS {}_{\text{MS}} ↑ \uparrow EzAudio [ 1 ] 2.262 15.738 1.322 11.018 0.458 0.423 AudioLDM2 [ 2 ] 2.957 24.387 1.545 9.105 0.395 0.556 TangoFlux [ 3 ] 2.338 19.319 1.183 12.365 0.482 0.468 MakeAnAudio [ 4 ] 2.455 18.169 1.506 8.820 0.406 0.574 StableAudio [ 5 ] 3.409 44.806 2.152 9.446 0.216 0.345 MMAudio [ 6 ] 6.184 18.631 1.337 12.144 0.416 0.446 SemanticVocoder 1.709 12.823 1.154 11.286 0.454 0.557 Table 1: Text-to-audio generation performance on AudioCaps. The best FAD and FD scores reflect that the audio distribution generated by SemanticVocoder is closest to that of the reference audio.

[67] h3: 6.1 Text to audio generation performance

[68] p: The quantitative evaluation results for text-to-audio generation are presented in Table 1 . All evaluations are conducted on the AudioCaps test set using the first corresponding caption, ensuring fair comparison. Our SemanticVocoder achieves the lowest FAD VGG {}_{\text{VGG}} and FD PANNs {}_{\text{PANNs}} scores, outperforming all baseline models while maintaining competitive performance on other metrics. As FAD and FD measure the distribution distance between generated and reference audio, it indicates that SemanticVocoder produces audio closer to the real distribution than VAE-based systems.

[69] p: To summarize the underlying reasons, compared with directly predicting low-level acoustic latents from text, high-dimensional semantic latents serve as more suitable targets for generative modeling. The VAE acoustic latents contain excessive details, rendering second-stage text-to-latent modeling difficult to optimize. In other words, in conventional VAE-based LDM frameworks, text-to-latent prediction is challenging, whereas latent-to-waveform generation remains relatively straightforward. In contrast, SemanticVocoder balances optimization difficulty across these two stages . These results demonstrate the effectiveness of substituting traditional acoustic latents with semantic latents.

[70] figure: System Dimension DCASE2016 ↑ \uparrow ESC50 ↑ \uparrow FSD50k ↑ \uparrow StableAudio [ 5 ] /TangoFlux [ 3 ] 64 60.523 42.450 21.134 EzAudio [ 1 ] 128 21.616 22.850 10.768 AudioLDM2 [ 2 ] 8*16 20.821 36.150 16.221 MakeAnAudio [ 4 ] 4*10 68.771 35.250 15.694 MMAudio [ 6 ] 40 56.770 35.600 15.831 SemanticVocoder 768 93.690 83.400 51.583 Table 2: Evaluation scores of acoustic and semantic latents on the HEAR audio understanding benchmark. TangoFlux adopts the same VAE as StableAudio.

[71] h3: 6.2 Audio understanding capability

[72] p: The semantic discriminability performance on the HEAR benchmark is shown in Table 2 . Benefiting from the powerful pre-trained semantic encoder [ 13 ] , the semantic latents significantly outperform the acoustic latents on all three understanding tasks. As also observed from Figure 3 , semantic latents exhibit a clearer distribution across different sound events. This reveals the drawback of original VAE latents, which prioritize compression and reconstruction, yielding low-level acoustic encodings that lack structured semantic discriminability. Furthermore, these results illustrate that SemanticVocoder opens up an opportunity to unify audio generation and understanding within a single latent space.

[73] figure: System Sample Rate ViSQOL ↑ \uparrow Mel ↓ \downarrow STFT ↓ \downarrow Waveform ↓ \downarrow StableAudio [ 5 ] /TangoFlux [ 3 ] 44.1K 4.381 0.766 2.001 0.047 EzAudio [ 1 ] 24K 4.550 1.115 2.267 0.038 AudioLDM2 [ 2 ] 16K 3.514 1.488 3.332 0.084 MakeAnAudio [ 4 ] 16K 3.214 1.498 3.831 0.089 MMAudio [ 6 ] 44.1K 4.481 0.620 2.003 0.099 SemanticVocoder 24K 3.239 1.304 3.283 0.096 Table 3: Reconstruction evaluation on AudioCaps test set. Despite SemanticVocoder being optimized for generation based on semantic information, it exhibits comparable reconstruction performance. TangoFLux adopts the same VAE from StableAudio.

[74] h3: 6.3 Audio reconstruction performance

[75] p: Although SemanticVocoder is primarily designed for generative tasks, we additionally evaluate its reconstruction performance on the AudioCaps test set, as reported in Table 3 . SemanticVocoder is comparable to dedicated reconstruction-focused baselines. This demonstrates that semantic latents can benefit not only generation but also robust audio reconstruction.

[76] h2: 7 Discussion

[77] p: Advantages SemanticVocoder breaks away from the dependence of audio generation on VAEs, thereby alleviating several inherent limitations. It rebalances the optimization difficulty across the two-stage pipeline: text-to-latent and latent-to-waveform generation. In traditional frameworks, modeling the text-to-acoustic latent mapping is notoriously challenging, whereas converting acoustic latents to waveforms remains relatively straightforward. In contrast, SemanticVocoder fundamentally rebalances this trade-off by enabling the generative model to focus on the simpler task of aligning text with high-level semantic latents, while shifting the burden of reconstructing fine-grained acoustic details to the vocoder. Meanwhile, SemanticVocoder aligns the optimization objectives of both stages toward generation. Finally, by employing semantic latents as an intermediate anchor, the two stages become mutually independent, and can thus be trained separately and are inherently plug-and-play.

[78] p: Limitations SemanticVocoder still has several limitations. Its performance depends on the capability of the pretrained semantic encoder to abstract semantic structures. It is constrained by audio length: the model currently cannot generate long-form audio. The objective metrics such as FAD and FD cannot reflect all aspects of audio generation quality, necessitating subjective evaluation to further assess generation quality from a human perception perspective.

[79] h2: 8 Conclusion

[80] p: In this paper, we propose SemanticVocoder, a novel generative vocoder that directly synthesizes audio waveforms from semantic latents, departing from conventional VAE-based acoustic latents. By discarding the conventional VAE module that focuses on low-level acoustic compression and reconstruction, our framework effectively mitigates issues of semantic entanglement and weak discriminability inherent in traditional latent spaces. We adopt a generative paradigm to mitigate the waveform distortion caused by feed-forward reconstruction networks when recovering signals from semantic latents. Downstream experiments on text-to-audio generation demonstrate that SemanticVocoder outperforms baseline systems, as evidenced by the lowest FAD and FD scores, which indicate closest alignment between generated audio and the real distribution. Meanwhile, evaluations on semantic understanding benchmarks reveal that the introduced semantic latents exhibit a highly discriminative structure and clear semantic separation, demonstrating the superiority of semantic latents over acoustic latents. Although primarily optimized for generation, SemanticVocoder maintains competitive reconstruction capability. This underscores the flexibility and generality of semantic representations enabled by SemanticVocoder. Furthermore, it balances optimization difficulty across two-stage models and exhibits inherent plug-and-play properties. Overall, SemanticVocoder not only offers an effective alternative to VAE-centric audio generation pipelines but also presents a promising avenue toward unifying audio generation and understanding within a shared semantic space.

[81] h2: References

[82] h2: Appendix A Ablation studies

[83] p: We conduct ablation studies comparing semantic latents with conventional acoustic latents within the same training framework. We employ two acoustic latent representations: VAE latents and Mel latents. For VAE latents, we adopt the pre-trained VAE from EzAudio [ 1 ] and perform text-to-latent generation within this latent space. For Mel latents, the model predicts the Mel spectrograms, which are subsequently converted to waveforms via the BigVGAN [ 8 ] acoustic vocoder. All text-to-latent models are trained exclusively on AudioCaps. As shown in Table 4 , these results are consistent with those in Section 6.1 , demonstrating that semantic latents achieve superior performance relative to acoustic latents. This superiority arises because acoustic latents encode low-level signal properties, whereas semantic latents capture high-level structural information more conducive to generative modeling.

[84] figure: Latent Type FAD VGG {}_{\text{VGG}} ↓ \downarrow FD PANNs {}_{\text{PANNs}} ↓ \downarrow KL ↓ \downarrow IS ↑ \uparrow CLAP LAION {}_{\text{LAION}} ↑ \uparrow CLAP MS {}_{\text{MS}} ↑ \uparrow VAE acoustic latents 2.449 16.358 1.531 10.250 0.419 0.391 Mel acoustic latents 5.087 22.295 1.790 8.475 0.410 0.421 Semantic latents 1.956 14.110 1.292 11.038 0.438 0.541 Table 4: Ablation studies on replacing semantic latents with VAE latents or mel-spectrograms.

[85] h2: Appendix B Generative versus reconstructive approaches

[86] p: We further investigate alternative strategies to verify the necessity of a generative framework for latent-to-waveform generation. For fair comparison, we employ the same text-to-latent model used in Table 1 , since the introduction of semantic latents as an anchor renders our two-stage pipeline mutually independent and plug-and-play. We adopt the training framework of the StableAudio [ 5 ] VAE to reconstruct waveforms from semantic latents. As shown in Table 5 , employing a a reconstruction-based approach for latent-to-waveform conversion results in performance degradation, as traditional reconstruction methods suffer from audio distortion when dealing with semantic latents.

[87] figure: Strategy Architecture FAD VGG {}_{\text{VGG}} ↓ \downarrow FD PANNs {}_{\text{PANNs}} ↓ \downarrow KL ↓ \downarrow IS ↑ \uparrow CLAP LAION {}_{\text{LAION}} ↑ \uparrow Reconstruction VAE 4.781 18.962 1.212 8.240 0.403 Generation Flow-Matching 1.709 12.823 1.154 11.286 0.454 Table 5: Text-to-audio generation results on AudioCaps. The same text-to-semantic latent model is used, while different training strategies are adopted for the latent-to-waveform module.

[88] h2: Appendix C Sampling steps and Class-Free guidance

[89] p: We investigate the effects of different numbers of inference steps and Class-Free Guidance (CFG) scale on the generation results, as shown in Figure 4 . It can be observed that CFG has a relatively large impact on model performance, while the performance varies only slightly across different sampling steps for both the text-to-latent and latent-to-waveform modules.

[90] figure: Figure 4: The influence of inference steps and Class-Free guidance on TTA performance.

[91] h2: Appendix D Cross domain generation capability

[92] p: For cross-domain evaluation, we utilize the Clotho [ 26 ] test set. The first corresponding caption is used as the input prompt. Each audio clip is truncated to 10 seconds. It can be observed from Table 6 that SemanticVocoder also achieves competitive performance and obtains the best FAD and FD scores.

[93] figure: System FAD VGG {}_{\text{VGG}} ↓ \downarrow FD PANNs {}_{\text{PANNs}} ↓ \downarrow KL ↓ \downarrow IS ↑ \uparrow CLAP LAION {}_{\text{LAION}} ↑ \uparrow CLAP MS {}_{\text{MS}} ↑ \uparrow EzAudio [ 1 ] 1.887 20.499 2.581 10.476 0.264 0.473 AudioLDM2 [ 2 ] 2.677 21.257 2.188 8.754 0.289 0.422 TangoFlux [ 3 ] 2.503 21.899 2.462 10.833 0.318 0.495 MakeAnAudio [ 4 ] 3.368 23.032 2.631 8.173 0.236 0.384 StableAudio [ 5 ] 2.994 40.731 2.515 9.168 0.285 0.481 MMAudio [ 6 ] 2.257 20.143 2.501 9.223 0.356 0.515 SemanticVocoder 1.833 18.690 2.542 9.651 0.265 0.465 Table 6: Cross-domain evaluation results. Experiments are conducted on the Clotho test set, where the first caption is used as input and each audio clip is truncated to 10 seconds.

[94] h2: Instructions for reporting errors

[95] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[96] p: Tip: You can select the relevant text first, to include it in your report.

[97] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[98] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
