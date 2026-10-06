[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SkyReels-V4 : Multi-modal Video-Audio Generation, Inpainting and Editing model

[3] h6: Abstract

[4] p: SkyReels-V4 is a unified multi-modal video foundation model for joint video–audio generation, inpainting, and editing. The model adopts a dual-stream Multimodal Diffusion Transformer (MMDiT) architecture, where one branch synthesizes video and the other generates temporally aligned audio, while sharing a powerful text encoder based on the Multimodal Large Language Models (MMLM). SkyReels-V4 accepts rich multi-modal instructions, including text, images, video clips, masks, and audio references. By combining the MMLM’s multi-modal instruction-following capability with in-context learning in the video-branch MMDiT, the model can inject fine-grained visual guidance under complex conditioning, while the audio-branch MMDiT simultaneously leverages audio references to guide sound generation. On the video side, we adopt a channel-concatenation formulation that unifies a wide range of inpainting-style tasks—such as image-to-video, video extension, and video editing—under a single interface, and naturally extends to vision-referenced inpainting and editing via multi-modal prompts. SkyReels-V4 supports up to 1080p resolution, 32 FPS, and 15-second duration, enabling high-fidelity, multi-shot, cinema-level video generation with synchronized audio. To make such high-resolution, long-duration generation computationally feasible, we introduce an efficiency strategy: Joint generation of low-resolution full sequences and high-resolution keyframes, followed by dedicated super-resolution and frame interpolation models. To our knowledge, SkyReels-V4 is the first video foundation model that simultaneously supports multi-modal input, joint video–audio generation, and a unified treatment of generation, inpainting, and editing, while maintaining strong efficiency and quality at cinematic resolutions and durations.

[5] h2: 1 Introduction

[6] p: From the earliest days of cinema, filmmakers have understood that compelling storytelling demands the seamless orchestration of sight and sound. When the Lumière Brothers first projected L’Arrivée d’un train en gare de La Ciotat in 1895, audiences recoiled at the silent image of an approaching locomotive; yet it was not until The Jazz Singer synchronized Al Jolson’s voice with his moving lips in 1927 that cinema truly came alive. This historical evolution from silent film to “talkies” reflects a fundamental truth about human perception: vision provides spatial structure and compositional context, while audition conveys temporal rhythm, emotional texture, and narrative continuity. Neither modality alone suffices—their synergy creates the immersive experiences that define modern media.

[7] p: Over the past year, the field of video generation has witnessed a decisive paradigm shift from unimodal synthesis toward joint audio-video generation . Proprietary commercial systems such as Veo-3.1 [ 8 ] , Sora-2 [ 33 ] , Kling-2.6 [ 23 ] , Gen-4.5 [ 38 ] , Seedance-1.5 [ 40 ] , Wan-2.6 [ 50 ] have transformed video generation capabilities into practical, utility-driven tools that natively produce synchronized audio alongside visual content. These systems mark a significant departure from earlier text-to-video (T2V) or video-to-audio (V2A) pipelines, which handled one modality at a time and often suffered from audio-visual asynchrony, lip-speech mismatches, and degraded unimodal quality.

[8] p: In parallel, substantial progress has been made in multimodal-referenced video generation , where models accept diverse conditioning inputs beyond text. For instance, Vidu [ 47 ] pioneered Reference-to-Video generation, enabling coherent synthesis from multiple referenced images. Runway Aleph [ 39 ] introduced state-of-the-art in-context video editing, performing a wide range of operations—adding, removing, and transforming objects, generating arbitrary scene angles, and modifying style and lighting—directly on input videos. In the audio-to-video domain, systems such as Omnihuman-1/1.5 [ 30 , 22 ] , SkyReels-A3 [ 42 , 10 ] , KlingAvatar [ 9 , 45 ] , and Multitalk [ 26 ] have demonstrated compelling talking-head synthesis and audio-driven animation. Recently, Kling-Omni [ 44 ] emerged as the first model to support both image and video references for video generation, yet it remains limited to visual synthesis without audio output. Alongside these developments, concurrent works including Kling-3.0 [ 24 ] , Seedance-2.0 [ 5 ] , and Vidu-Q3 [ 48 ] have taken meaningful steps toward bridging this gap, each integrating multimodal inputs with joint video–audio generation within a unified model. Nevertheless, these systems still fall short of a fully comprehensive solution.

[9] p: Despite these advances, no existing system simultaneously unifies multimodal inputs (text, images, videos, masks, and audio references), joint video–audio generation, comprehensive inpainting, and editing capabilities within a single framework . Current state-of-the-art models remain fundamentally fragmented: audio-driven systems such as Omnihuman-1/1.5 and Multitalk adopt shallow fusion mechanisms (e.g., cross-attention or lightweight adapters) that fail to fully align audio-visual representations, while multimodal-referenced models such as Kling-Omni focus exclusively on visual conditioning without native audio synthesis. Although recent efforts—Kling-3.0, Seedance-2.0, and Vidu-Q3—have taken meaningful steps toward joint video–audio generation under multimodal inputs, none of these systems natively integrates comprehensive inpainting and fine-grained editing within a unified architecture. The field therefore still lacks a unified foundation model capable of seamlessly handling generation, inpainting, and editing conditioned on arbitrary combinations of text, images, videos, masks and audio references.

[10] p: To address these limitations, we present SkyReels-V4 , a multi-modal video foundation model that jointly generates video and audio while unifying generation, inpainting, and editing within a single architecture. SkyReels-V4 is built on a dual-stream MMDiT (Multi-Modal Diffusion Transformer) design: one branch is dedicated to video synthesis, and the other to audio generation. The two branches share a common text encoder instantiated by a strong MMLM that provides multi-modal understanding and instruction-following across text, images, videos and audios. This shared MMLM backbone allows SkyReels-V4 to condition on diverse inputs—including text, images, videos, and audio references—in a unified, semantically coherent manner.

[11] p: To support a broad set of video manipulation tasks, we design the video branch around a channel concatenation formulation that treats diverse operations as special cases of inpainting. Specifically, tasks such as image-to-video generation, video extension, and video editing are expressed via masked inputs and additional conditioning channels that are concatenated with the latent representation. This unified inpainting perspective allows SkyReels-V4 to handle heterogeneous workflows within a single model, while the underlying MMLM enables visually referenced inpainting: for example, altering a character’s clothing based on a reference image, extending a shot while preserving composition from a provided frame, or editing specific regions indicated by a mask.

[12] p: SkyReels-V4 is designed not only for flexibility but also for cinematic quality. The model supports video generation at up to 1080p resolution, 32 FPS, and 15-second duration, and it can handle multi-shot sequences suitable for film-like storytelling. Achieving such resolutions and lengths with diffusion-based architectures is computationally demanding; naive scaling leads to prohibitive memory and time costs. To overcome this, we introduce an efficiency strategy. Instead of direct 1080p generation, we present a joint low-resolution / high-resolution keyframe generation, where the model first produces a low-resolution full sequence and high-resolution keyframes, followed by specialized super-resolution and frame interpolation modules that reconstruct a temporally consistent, high-resolution video. This design enables SkyReels-V4 to achieve surprisingly high generation speed even for long, high-resolution videos with synchronized audio, making it practical for real-world creative and production environments.

[13] p: To the best of our knowledge, SkyReels-V4 is the first system worldwide that simultaneously supports (i) rich multi-modal inputs (text, images, video, masks, and audio), (ii) joint video–audio generation, and (iii) a unified framework for generation, inpainting, and editing, while scaling effectively to high-resolution, long-duration outputs. This combination of capabilities positions SkyReels-V4 as a versatile foundation model for next-generation video creation and editing.

[14] p: Extensive experiments demonstrate the superior performance of SkyReels-V4 compared to current state-of-the-art methods. Our model achieves state-of-the-art results on the Artificial Analysis Arena [ ArtificialAnalysis ] . Comprehensive human evaluation through SkyReels-VABench reveals that SkyReels-V4 significantly outperforms proprietary commercial systems, with particular strengths in instruction following, motion quality, and complex multi-shot narratives. Additionally, the model demonstrates robust performance across diverse multimodal conditioning tasks including reference-to-video, motion-to-video, and video editing, validating its effectiveness as a unified foundation model for professional video-audio content creation.

[15] p: In summary, our contributions are:

[16] p: We introduce SkyReels-V4, a dual-stream MMDiT-based foundation model that jointly generates video and audio under multi-modal instruction and reference inputs.

[17] p: We propose a unified channel-concatenation inpainting framework for video, enabling image-to-video, video extension, video editing, and vision-referenced inpainting within a single architecture.

[18] p: We design an efficiency scheme — Joint low-res / high-res keyframe generation with super-resolution and interpolation—that makes 1080p, 32 FPS, 15-second, multi-shot video generation with synchronized audio computationally feasible.

[19] p: We demonstrate that SkyReels-V4 is, to our knowledge, the first model to unify multi-modal input, joint video–audio generation, and generation/inpainting/editing tasks at cinematic quality and speed, setting a new baseline for multi-modal video foundation models.

[20] h2: 2 Related Work

[21] h3: 2.1 Video Generative Models

[22] p: Diffusion models have transformed video generation, evolving from early 2D+1D architectures like Video Diffusion Models [ 21 ] and AnimateDiff [ 14 ] to DiT-based frameworks [ 34 ] . Sora [ 4 ] demonstrated the effectiveness of large-scale training with spatiotemporal attention. While closed-source systems (Veo-3.1 [ 8 ] , Kling-O1 [ 44 ] , Sora-2 [ 33 ] , Hailuo-2.3 [ 17 ] , Gen-4.5 [ 38 ] ) lead commercially, open-source models—CogVideoX [ 57 ] , HunyuanVideo [ 25 , 46 ] , WAN-2.1/2.2 [ 49 ] , SkyReels series [ 35 , 41 , 6 , 11 , 28 ] , LTX [ 16 , 15 ] , MAGI-1 [ 1 ] —are rapidly narrowing the gap through data scaling and quality improvements.

[23] h3: 2.2 Video-Audio Generative Models

[24] p: Joint text-to-audio+video (T2AV) generation aims to synthesize synchronized audiovisual content from text. Commercial systems (Veo-3.1 [ 8 ] , Sora-2 [ 33 ] , Kling-3.0 [ 24 ] ) show strong capabilities but lack transparency. Open-source approaches evolved from coupled U-Nets [ 37 ] to DiT-based methods: adapter-based (AV-DiT [ 54 ] ), expert-orchestration (MMDisCo [ 18 ] , Universe-1 [ 51 ] ), and dual-stream architectures (Ovi [ 32 ] , BridgeDiT [ 13 ] , JavisDiT [ 31 ] ) using cross-attention or flow matching—though these incur high computational costs. LTX-2 [ 15 ] proposes asymmetric streams for efficiency. Unified single-tower models like Apollo [ 53 ] process audio-video tokens jointly via Omni-Full Attention, enabling multitask training (T2AV/TI2AV/TI2V) with tighter coupling. Despite progress, synchronized speech-video synthesis and complete soundscapes remain underexplored, with precise spatio-temporal alignment an open challenge.

[25] figure: Figure 1: Overview of the proposed method.

[26] h2: 3 Model Design

[27] p: We present SkyReels-V4, a unified multi-modal video foundation model for joint video-audio generation, inpainting, and editing. The model adopts a dual-stream MMDiT architecture with rich multi-modal instruction following, enabling seamless integration of text, image, video, mask, and audio conditioning signals while maintaining computational efficiency across cinematic resolutions and durations. The overview of the model architecture is shown in Figure 1 .

[28] h3: 3.1 Dual-Stream MMDiT Architecture for Joint Video-Audio Generation

[29] p: Our architecture employs a symmetric twin backbone design with parallel video and audio branches, both constructed on an identical Multimodal Diffusion Transformer (MMDiT) framework. The video branch is initialized from a pretrained text-to-video model, while the audio branch is trained from scratch with matching architectural specifications.

[30] p: Hybrid Dual-Stream and Single-Stream MMDiT Blocks. Following the MMDiT design, each transformer block processes video (or audio) and text modalities through a hybrid architecture that balances modality alignment with parameter efficiency. The initial M M layers employ a Dual-Stream design where video/audio and text tokens maintain separate parameters for adaptive layer normalization, QKV projections, and MLPs, but interact during joint self-attention:

[31] table: 𝐐 v , 𝐊 v , 𝐕 v \displaystyle\mathbf{Q}_{v},\mathbf{K}_{v},\mathbf{V}_{v} = QKV v ​ ( LayerNorm v ​ ( 𝐱 v ) ) , \displaystyle=\text{QKV}_{v}(\text{LayerNorm}_{v}(\mathbf{x}_{v})), (1) 𝐐 t , 𝐊 t , 𝐕 t \displaystyle\mathbf{Q}_{t},\mathbf{K}_{t},\mathbf{V}_{t} = QKV t ​ ( LayerNorm t ​ ( 𝐱 t ) ) , \displaystyle=\text{QKV}_{t}(\text{LayerNorm}_{t}(\mathbf{x}_{t})), (2) 𝐱 v ′ , 𝐱 t ′ \displaystyle\mathbf{x}^{\prime}_{v},\mathbf{x}^{\prime}_{t} = Attention ​ ( [ 𝐐 v ; 𝐐 t ] , [ 𝐊 v ; 𝐊 t ] , [ 𝐕 v ; 𝐕 t ] ) , \displaystyle=\text{Attention}([\mathbf{Q}_{v};\mathbf{Q}_{t}],[\mathbf{K}_{v};\mathbf{K}_{t}],[\mathbf{V}_{v};\mathbf{V}_{t}]), (3)

[32] p: where 𝐱 v \mathbf{x}_{v} and 𝐱 t \mathbf{x}_{t} denote video/audio and text token embeddings, respectively, and [ ⋅ ; ⋅ ] [\cdot;\cdot] represents concatenation. This design facilitates strong cross-modal alignment during early layers. The subsequent N N layers transition to a Single-Stream architecture that processes concatenated video (or audio) and text tokens with shared parameters, maximizing computational efficiency. This hybrid strategy achieves faster convergence than either pure approach.

[33] p: Reinforced Text Conditioning via Cross-Attention. To address potential semantic dilution of text features in the single-stream stages, we augment the video block with an additional text cross-attention layer immediately following self-attention:

[34] table: 𝐱 v ′′ = 𝐱 v ′ + Attention ​ ( 𝐐 = 𝐱 v ′ , 𝐊 = 𝐱 t , 𝐕 = 𝐱 t ) , \mathbf{x}^{\prime\prime}_{v}=\mathbf{x}^{\prime}_{v}+\text{Attention}(\mathbf{Q}=\mathbf{x}^{\prime}_{v},\mathbf{K}=\mathbf{x}_{t},\mathbf{V}=\mathbf{x}_{t}), (4)

[35] p: where the video stream queries the text embeddings, reinforcing textual guidance throughout the generation process. This cross-attention mechanism is crucial for maintaining fine-grained semantic control in later model stages.

[36] p: Bidirectional Audio-Video Cross-Attention. To enable temporal synchronization between modalities, each transformer block incorporates paired cross-attention layers: the audio stream attends to video features, and the video stream reciprocally attends to audio features. This bidirectional mechanism exchanges synchronization cues throughout the entire network depth:

[37] table: 𝐚 i ′ \displaystyle\mathbf{a}^{\prime}_{i} = 𝐚 i + CrossAttn ​ ( 𝐐 = 𝐚 i , 𝐊 = 𝐯 i , 𝐕 = 𝐯 i ) , \displaystyle=\mathbf{a}_{i}+\text{CrossAttn}(\mathbf{Q}=\mathbf{a}_{i},\mathbf{K}=\mathbf{v}_{i},\mathbf{V}=\mathbf{v}_{i}), (5) 𝐯 i ′′ \displaystyle\mathbf{v}^{\prime\prime}_{i} = 𝐯 i ′ + CrossAttn ​ ( 𝐐 = 𝐯 i ′ , 𝐊 = 𝐚 i ′ , 𝐕 = 𝐚 i ′ ) , \displaystyle=\mathbf{v}^{\prime}_{i}+\text{CrossAttn}(\mathbf{Q}=\mathbf{v}^{\prime}_{i},\mathbf{K}=\mathbf{a}^{\prime}_{i},\mathbf{V}=\mathbf{a}^{\prime}_{i}),

[38] p: where 𝐚 i \mathbf{a}_{i} and 𝐯 i \mathbf{v}_{i} are audio and video features at layer i i . The architectural symmetry ensures both modalities share the same latent dimension, eliminating the need for intermediate projection layers and preserving the attention structure from unimodal pretraining.

[39] p: Temporal Alignment via RoPE Scaling. Despite architectural symmetry, the temporal resolutions differ: video latents span 21 frames while audio latents contain 218 tokens (44.1 kHz × \times 5s). To align these temporal scales, we apply Rotary Positional Embeddings (RoPE) to both modalities and scale the audio RoPE frequencies by 21 / 218 ≈ 0.09633 21/218\approx 0.09633 to match the video’s coarser temporal resolution. This ensures that audio and video tokens attend to each other with temporally consistent correspondence.

[40] p: Shared Multi-Modal Text Encoder. We simplify prompt conditioning by employing a single frozen MMLM text encoder applied to a combined prompt that concatenates visual and acoustic descriptions. The resulting multi-modal embeddings are independently consumed by both audio and video branches via self-attention and cross-attention. This unified semantic context improves cross-modal alignment while simplifying training and inference, and crucially enables the model to process rich multi-modal instructions including text, images, video clips, and audio references.

[41] p: Training Objective. We adopt a flow matching framework for training. Given a video latent 𝐳 v 0 \mathbf{z}_{v}^{0} and audio latent 𝐳 a 0 \mathbf{z}_{a}^{0} , we sample timestep t ∼ 𝒰 ⁡ ( 0 , 1 ) t\sim\mathcal{U}(0,1) and construct noisy latents 𝐳 v t = t ​ 𝐳 v 0 + ( 1 − t ) ​ ϵ v \mathbf{z}_{v}^{t}=t\mathbf{z}_{v}^{0}+(1-t)\boldsymbol{\epsilon}_{v} and 𝐳 a t = t ​ 𝐳 a 0 + ( 1 − t ) ​ ϵ a \mathbf{z}_{a}^{t}=t\mathbf{z}_{a}^{0}+(1-t)\boldsymbol{\epsilon}_{a} , where ϵ v , ϵ a ∼ 𝒩 ⁡ ( 0 , 𝐈 ) \boldsymbol{\epsilon}_{v},\boldsymbol{\epsilon}_{a}\sim\mathcal{N}(0,\mathbf{I}) . The model predicts the velocity field 𝐯 θ \mathbf{v}_{\theta} that pushes noise toward data:

[42] table: ℒ flow = 𝔼 t , 𝐳 v 0 , 𝐳 a 0 , ϵ v , ϵ a ​ [ ‖ 𝐯 θ v ​ ( t , 𝐳 v t , 𝐳 a t , 𝐜 ) − ( 𝐳 v 0 − ϵ v ) ‖ 2 + ‖ 𝐯 θ a ​ ( t , 𝐳 a t , 𝐳 v t , 𝐜 ) − ( 𝐳 a 0 − ϵ a ) ‖ 2 ] , \mathcal{L}_{\text{flow}}=\mathbb{E}_{t,\mathbf{z}_{v}^{0},\mathbf{z}_{a}^{0},\boldsymbol{\epsilon}_{v},\boldsymbol{\epsilon}_{a}}\left[\left\|\mathbf{v}_{\theta}^{v}(t,\mathbf{z}_{v}^{t},\mathbf{z}_{a}^{t},\mathbf{c})-(\mathbf{z}_{v}^{0}-\boldsymbol{\epsilon}_{v})\right\|^{2}+\left\|\mathbf{v}_{\theta}^{a}(t,\mathbf{z}_{a}^{t},\mathbf{z}_{v}^{t},\mathbf{c})-(\mathbf{z}_{a}^{0}-\boldsymbol{\epsilon}_{a})\right\|^{2}\right], (6)

[43] p: where 𝐜 \mathbf{c} denotes the conditioning information (multi-modal embeddings and optional spatial-temporal masks). The joint training objective encourages both branches to learn synchronized generation while respecting their respective modality-specific characteristics.

[44] h3: 3.2 Unified Video Inpainting via Channel Concatenation

[45] p: To enable diverse video generation and editing tasks within a single framework, we employ a flexible input conditioning mechanism applied to the video branch. The input to the video MMDiT is formed by concatenating three tensors along the channel dimension:

[46] table: 𝐙 input = Concat ​ ( 𝐕 , 𝐈 , 𝐌 ) , \mathbf{Z}_{\text{input}}=\text{Concat}(\mathbf{V},\mathbf{I},\mathbf{M}), (7)

[47] p: where 𝐕 ∈ ℝ T × H × W × C \mathbf{V}\in\mathbb{R}^{T\times H\times W\times C} is the noisy video latent, 𝐈 ∈ ℝ T × H × W × C \mathbf{I}\in\mathbb{R}^{T\times H\times W\times C} contains VAE-encoded conditional frames (with non-conditional frames filled with black image latents), and 𝐌 ∈ ℝ T × H × W × 1 \mathbf{M}\in\mathbb{R}^{T\times H\times W\times 1} is a binary mask specifying which spatiotemporal regions are conditions (value 1) versus regions to be generated (value 0).

[48] p: This formulation unifies multiple generation tasks through different mask configurations:

[49] p: Text-to-Video (T2V): 𝐌 = 𝟎 \mathbf{M}=\mathbf{0} (all frames generated)

[50] p: Image-to-Video (I2V): M t = 0 = 1 , M t > 0 = 0 M_{t=0}=1,M_{t>0}=0 (first frame conditioned)

[51] p: Video Extension: M t < k = 1 , M t ≥ k = 0 M_{t<k}=1,M_{t\geq k}=0 (first k k frames conditioned)

[52] p: Start-End Frame Interpolation: M t = 0 = M t = T − 1 = 1 M_{t=0}=M_{t=T-1}=1 , others 0

[53] p: Video Editing: M t , h , w = 1 M_{t,h,w}=1 for preserved regions, 0 for edited regions (arbitrary spatiotemporal masks)

[54] p: This unified formulation naturally accommodates both fixed foreground/background masks and dynamic per-frame editing masks, enabling precise control over spatial and temporal modifications.

[55] p: Crucially, the inpainting mechanism is applied exclusively to the video stream. During inpainting and editing tasks, the audio branch generates audio from scratch conditioned on the (partially conditioned or edited) video content, ensuring acoustic consistency with the generated or modified visual content. This design allows the audio to adapt seamlessly to video modifications while maintaining temporal synchronization through the bidirectional cross-attention mechanism.

[56] h3: 3.3 Multi-Modal In-Context Learning for Vision-Referenced Generation and Editing

[57] p: Beyond text and inpainting masks, our framework supports rich multi-modal conditioning through reference images and video clips, enabling complex vision-referenced generation tasks such as multi-identity video generation and identity-preserving video editing under multi-modal prompts.

[58] p: Multi-Modal Instruction Following via MLLM. Reference visual inputs (images or video frames) are jointly processed with the text prompt through the MMLM text encoder to extract semantically enriched multi-modal embeddings. The MLLM’s instruction-following capability enables the model to understand complex compositional requests that combine visual references with textual descriptions (e.g., “generate a video of person A from the reference @image_1 speaking <dialogue>hello, how are you?</dialogue> in the style of person B’s @video_1”). These multi-modal embeddings are consumed by both the video and audio branches.

[59] p: In-Context Visual Conditioning via Self-Attention. To provide explicit visual reference signals beyond semantic guidance, we inject reference visuals directly into the video self-attention mechanism. Each reference image or video frame is encoded via the VAE, padded to a uniform spatial resolution, and concatenated along the temporal dimension. These condition latents 𝐙 cond \mathbf{Z}_{\text{cond}} are prepended to the noisy video latents 𝐙 video \mathbf{Z}_{\text{video}} before self-attention:

[60] table: 𝐙 attn = [ 𝐙 cond ; 𝐙 video ] , \mathbf{Z}_{\text{attn}}=[\mathbf{Z}_{\text{cond}};\mathbf{Z}_{\text{video}}], (8)

[61] p: where the concatenated sequence undergoes joint self-attention. This in-context learning enables the model to directly reference fine-grained visual patterns (e.g., identity characteristics, texture details, pose variations) from the conditions when generating or editing video content.

[62] p: Temporal Positional Disambiguation via Offset 3D RoPE. To distinguish condition latents from noisy video latents and organize multiple reference visuals, we employ 3D Rotary Positional Embeddings with temporal index offsets. Condition latents receive negative temporal indices, sequentially encoding each reference visual before the generated video frames:

[63] table: RoPE temporal ​ ( 𝐙 cond , i ) = RoPE ​ ( t = − N cond + i ) , RoPE temporal ​ ( 𝐙 video , j ) = RoPE ​ ( t = j ) , \text{RoPE}_{\text{temporal}}(\mathbf{Z}_{\text{cond},i})=\text{RoPE}(t=-N_{\text{cond}}+i),\quad\text{RoPE}_{\text{temporal}}(\mathbf{Z}_{\text{video},j})=\text{RoPE}(t=j), (9)

[64] p: where N cond N_{\text{cond}} is the total number of condition tokens and i , j i,j index the condition and video tokens respectively. Spatial indices are preserved across all tokens, ensuring that attention relationships respect both spatial and temporal structure. This offset-based positional encoding provides an effective inductive bias for distinguishing conditioning context from generation targets without introducing task-specific architectural modifications, and naturally extends to multiple reference visuals of varying types (images, short clips, etc.).

[65] p: Audio Reference Conditioning. Similarly, audio references (e.g., speech samples, musical themes, ambient soundscapes) are encoded and processed as in-context conditions for the audio branch. By combining multi-modal semantic guidance from the MLLM with in-context visual patterns from the video branch and audio patterns from audio references, the model achieves fine-grained control over both visual and acoustic generation.

[66] h3: 3.4 Data Pipeline

[67] p: Our data pipeline consists of three main components: data collection, data processing, and captioning. This pipeline handles three modalities—images, videos, and audio—to support multimodal model training.

[68] h4: 3.4.1 Data Collection

[69] p: Our training data comprises both real-world and synthetic data across three modalities: images, videos, and audio.

[70] p: Real-world Data. We collect real-world data from two primary sources: publicly available datasets and licensed in-house data. Public datasets include images (LAION [ 27 ] , Flickr [ 20 ] , etc.), videos (WebVid-10M [ 3 ] , Koala-36M [ 55 ] , OpenHumanVid [ 29 ] , etc.), and audio (Emilia [ 19 ] , AudioSet [ 12 ] , VGGSound [ 7 ] , SoundNet [ 2 ] , etc.). Our in-house licensed data encompasses authorized movies, TV series, short videos, and web series.

[71] p: Synthetic Data. We generate synthetic data to address sparse scenarios and generation tasks inadequately covered by real-world data. We focus on three key areas: multilingual text generation, multilingual speech synthesis and multimodal inpainting/editing tasks.

[72] p: For text generation, we construct synthetic data covering multiple languages, including Chinese, English, Japanese, Korean, German, French, etc. Our synthetic image-text data includes simple text rendering and context-aware text generation that preserves font characteristics. For video-text data, we generate basic text effect videos and context-aware text with attributes matching reference styles (font, size, color) and motion characteristics (trajectories, special effects).

[73] p: To enhance speech generation and multilingual coverage, we employ multiple TTS models spanning various languages. We curate diverse text corpora to ensure the model learns pronunciations beyond common characters, including rare and uncommon scripts.

[74] p: For multimodal inpainting and editing tasks, paired training data is inherently unavailable in real-world datasets. We therefore construct these data through a sophisticated pipeline involving visual segmentation models, image/video editing models, and controllable generation techniques.

[75] h4: 3.4.2 Data Processing

[76] p: Our data processing pipeline is tailored to three data types: images, pure audio, and videos (with or without audio).

[77] p: Image Data Processing. The image processing pipeline consists of three stages: deduplication, filtering, and balancing. Deduplication employs strict image-level matching. Filtering includes basic quality metrics (resolution, IQA scores, aspect ratio, etc.) and content quality criteria (watermarks, stamps, logos, overly small text, etc.). For data balancing, we adopt stage-specific strategies: during pretraining, we compute image embedding similarities, perform clustering, and balance cluster proportions; during supervised fine-tuning (SFT), we define entity and scene categories, matching them against captions for fine-grained balancing.

[78] p: Audio Data Processing. The audio processing pipeline includes: category classification, quality filtering, duration control, content recognition, and audio captioning. First, we classify audio into four categories—sound effects, music, speech, and singing—using Qwen3-Omni [ 56 ] . Next, we perform quality filtering based on SNR, MOS score, clipping ratio, and audio bandwidth. We use voice activity detection (VAD) to select audio with silence ratios below 0.2. For duration control, we segment long audio clips into 15-second chunks and concatenate short clips by category to reach 15 seconds. For speech and singing categories, we employ Whisper to transcribe spoken and sung content. Finally, we uniformly caption all audio using Qwen3-Omni.

[79] p: Video Data Processing. Video processing consists of four stages: preprocessing (segmentation and deduplication), filtering, balancing, and audio-video synchronization for videos with audio tracks.

[80] p: Preprocessing. Traditional methods using PyDetect and TransNet-V2 [ 43 ] produce scene-cut clips that often lack narrative coherence. Instead, we adopt intelligent segmentation that combines TransNet’s shot boundary predictions via VLM to extract semantically complete segments, including both long takes and multi-shot clips. In later training stages, we further apply video highlight detection to identify segments with richer content. We deduplicate segmented clips using VideoCLIP embeddings [ 52 ] .

[81] p: Filtering. We filter videos based on three quality dimensions: basic quality (duration, resolution, aesthetic score, blur, contrast, exposure), content quality (watermarks, logos, text overlays, synthetic artifacts, content type/source issues), and motion quality (camera stability, motion magnitude/speed, frame drops).

[82] p: Balancing. To improve training efficiency, we balance data along two dimensions: conceptual diversity and motion diversity. We define a taxonomy of concept labels covering different subjects and scene types, matching them against video content for concept balancing. We further balance motion types by defining key motion patterns for each subject or scene category.

[83] p: Audio-Video Synchronization. Following the audio pipeline, we obtain preliminary audio captions. For videos containing speech or singing, we determine whether the video is person-free (background audio), single-person, or multi-person based on the first frame, and apply audio-visual synchronization filtering accordingly. We adopt the widely-used SyncNet [ 36 ] model, which uses a ConvNet architecture to learn joint embeddings between sound and mouth images, to filter speech videos lacking sufficient audio-video synchronization. We adapt the model to handle millions of video samples and produce scalar confidence and offset values. We retain only clips satisfying | offset | ≤ 3 ∧ confidence > 1.5 |\text{offset}|\leq 3\land\text{confidence}>1.5 with a minimum mean volume of -60 decibels. Finally, we integrate audio and video captions into unified descriptions.

[84] h4: 3.4.3 Captioning

[85] p: We generate three types of captions: short captions, long captions, and structured captions. Short captions provide concise descriptions of video content and audio information. Long captions offer comprehensive descriptions of environment, subjects, lighting, atmosphere, and other nuanced details. Structured captions follow a standardized descriptive order with special tokens to denote in-video text(<text></text>), sound effects(<sfx></sfx>), speech content(<dialogue></dialogue>), singing content(<singing></singing>), and background music(<bgm></bgm>). In final training stages, we exclusively use structured captions. To align user prompts with this format, we employ a prompt enhancer that reformats free-form input into the structured representation.

[86] h2: 4 Training Strategy

[87] p: We adopt a progressive multi-stage training paradigm that systematically develops the model’s capabilities across multiple modalities and tasks. Our training pipeline consists of three major phases: Video Pretrain, Audio Pretrain, and Video-Audio Joint Training, followed by supervised fine-tuning. This structured approach enables the model to learn spatial concepts, temporal dynamics, audio generation, and multi-modal alignment in a stable and efficient manner. Table 1 summarizes our complete multi-stage training schedule, including tasks, resolutions, data volumes, and training epochs for each stage.

[88] h3: 4.1 Video Pretrain

[89] p: The video pretraining phase follows a progressive strategy that gradually increases spatial resolution, temporal length, and task complexity. We begin with text-to-image (T2I) training to establish strong semantic understanding and visual concept learning, which we find significantly accelerates subsequent video training convergence.

[90] p: Stage 1: Text-to-Image Foundation. We first train the T2I task at 256px resolution using 3 billion images for 3 epochs. This stage enables the model to learn the correspondence between text and visual content, establishing a solid foundation for spatial composition and concept formation.

[91] p: Stage 2: Initial Video Learning. We introduce text-to-video (T2V) generation while maintaining T2I training. At 256px resolution and 16 fps, we train on 1 billion images and 400 million videos for 3 epochs, with video durations ranging from 2 to 10 seconds. Training at lower resolution allows the model to more rapidly converge on motion dynamics and temporal coherence.

[92] p: Stage 3: Inpainting Capabilities. We expand the task set to include image inpainting, image-to-video (I2V), video-to-video (V2V), and video editing tasks, each comprising 5% of the training mix. This stage trains for 2 epochs with video durations extended to 2–15 seconds, enabling the model to learn spatial and temporal inpainting capabilities.

[93] p: Stage 4: Mixed Resolution Scaling. We employ mixed-resolution training at 256px and 480px, maintaining 16 fps and 2–15 second durations. Training on 100 million images and 100 million videos, we keep the inpainting task ratio unchanged, allowing the model to gradually adapt to higher resolution generation.

[94] p: Stage 5: High Resolution Training. We further scale to mixed resolutions of 480px, 720px, and 1080px at 16 fps, with video durations of 3–15 seconds. This stage uses 50 million images and 50 million videos, substantially improving the model’s high-resolution generation quality.

[95] p: Stage 6: Multi-modal Condition Pretrain. We introduce image reference and video reference conditioning for both generation and inpainting tasks, comprising 20% of the training data each, with the remaining 60% dedicated to T2V. This stage trains on 20 million images and 50 million videos, equipping the model with flexible multi-modal conditioning capabilities.

[96] h3: 4.2 Audio Pretrain

[97] p: The audio backbone is pretrained from scratch on hundreds of thousands of hours of primarily speech data, with durations up to 15 seconds. During pretraining, we use variable-length audio to maximize coverage of diverse acoustics, providing the audio backbone with broad exposure to natural variability in duration and content. The long-form raw audio enables the model to generate consistent audio that respects speaker traits such as pitch and emotion.

[98] h3: 4.3 Video-Audio Joint Training

[99] p: Following the completion of video and audio pretraining, we enter the joint training phase, simultaneously training three tasks: text-to-video (T2V), text-to-audio-video (T2AV), and text-to-audio (T2A). In this phase, we allocate half of the video pretrain data to T2AV joint training while incorporating T2A data to enable synchronized audio-visual generation.

[100] h3: 4.4 Video-Audio Supervised Fine-tuning

[101] p: In the final SFT stage, we focus exclusively on joint generation data, training on 5 million videos with multi-modal condition support (image, video, and audio), which comprises 20% of the data. We conclude with a final fine-tuning step on 1 million manually curated high-quality videos, further refining generation quality, motion coherence, and audio-visual alignment.

[102] figure: Table 1: Complete training schedule across all stages. The progressive strategy gradually increases resolution, temporal length, and task complexity. Task Stage Resolution Data Volume Epochs Video Pretrain T2I Stage 1 256px 3B images 3 T2I + T2V Stage 2 256px, 16fps, 2-10s 1B images / 400M videos 3 T2I + T2V + Inpaint Stage 3 256px, 16fps, 2-15s 1B images / 400M videos 2 (Image Inpaint, I2V, V2V, Edit) (Inpaint: 5% each) Mixed Tasks Stage 4 256/480px, 16fps, 2-15s 100M images / 100M videos 2 (T2I, T2V, Inpaint) (Inpaint ratio unchanged) Mixed Tasks Stage 5 480/720/1080px, 50M images / 50M videos 2 (T2I, T2V, Inpaint) 16fps, 3-15s Multi-modal Condition Stage 6 480/720/1080px, 20M images / 50M videos 2 (Image/Video Ref: 20% each) 16fps, 3-15s (T2V: 60%) Audio Pretrain Audio Backbone Pretrain Variable length, up to 15s Hundreds of thousands of hours 3 Video-Audio Joint Training T2V + T2AV + T2A Joint Pretrain 720/1080px, 16fps, 5-15s 50% video data + T2A data 2 Video-Audio Supervised Fine-tuning T2AV + Multi-modal SFT Stage 1 720/1080px, 16fps, 5-15s 5M videos (Multi-modal: 20%) 3 T2AV + Multi-modal SFT Stage 2 720/1080px, 16fps, 5-15s 1M curated videos 3

[103] h3: 4.5 Video Super-Resolution and Frame Interpolation (Refiner)

[104] figure: Figure 2: The pipeline of the video super-resolution and frame interpolation method. F denotes the output latent of our base model. KF demotes the key frames latent of our base model.

[105] p: To further enhance visual quality and temporal smoothness of generated videos, we introduce a dedicated Refiner module that jointly performs video super-resolution (VSR) and frame interpolation, as shown in Fig. 2 . This cascaded architecture operates on the outputs of the base multi-modal video generation model, leveraging both low-resolution results and high-resolution key-frame results to synthesize high-fidelity, fine-grained visual details while simultaneously increasing temporal resolution.

[106] p: Architecture and Design. We initialize the Refiner weights from the pre-trained video generation model to ensure effective knowledge transfer and training stability. The Refiner accepts three categories of inputs: (1) multi-modal visual conditions (image, video, and audio references at high resolution), (2) multi-modal text instructions consistent with the base model, and (3) the base model outputs, which include low-resolution predictions for all frames and high-resolution predictions for keyframes. To support the efficient inference strategy described earlier, we incorporate a joint prediction task during post-training, where the base model learns to simultaneously predict all frames at low resolution and keyframes at high resolution. With these inputs, we first linearly interpolate the low-resolution latents to the target high resolution. Then, for keyframe positions, we replace the interpolated results with the directly predicted high-resolution keyframe latents from the base model. Finally, these combined latents are concatenated with high-resolution noisy latents along the channel dimension as input to the DiT model.

[107] p: To support multi-task generation, inpainting, and editing capabilities in the Refiner, we design a unified framework. For inpainting tasks, we incorporate the high-resolution version of the source video, using it to replace the interpolated regions where inpainting is not required. A spatial mask guides the model to distinguish between regions requiring refinement and those that should remain unchanged. This design enables the Refiner to handle both unconditional super-resolution and conditional inpainting across multiple modalities.

[108] p: Computational Efficiency. To address the computational overhead imposed by long temporal contexts and high-resolution inputs, we adopt Video Sparse Attention (VSA) [ 58 ] , a trainable sparse attention mechanism designed for video diffusion transformers. VSA employs a hierarchical two-stage approach: a coarse stage that aggregates spatial-temporal cubes to identify critical token regions through lightweight pooled attention, and a fine stage that applies dense attention only within the selected top-K cubes. This design eliminates the need to compute full quadratic attention while maintaining hardware efficiency through block-sparse layouts compatible with modern GPU kernels. By exploiting spatio-temporal redundancy in a learnable manner, VSA enables us to reduce attention computational cost by approximately 3 × 3\times while preserving generation quality, making it practical to process high-resolution video sequences during both training and inference.

[109] p: Training Data and Configuration. For dataset construction, we curate 1 million high-quality video clips spanning diverse scenarios and resolutions from 1K to 4K. We incorporate high-resolution images alongside video data to enhance the model’s capability for generating fine visual details. The task composition mirrors the base model’s multi-task structure, maintaining consistent ratios for generation, inpainting, and editing tasks. All weights of the Refiner are fully trainable throughout the training process, following the flow matching paradigm.

[110] h2: 5 Model Performance

[111] p: We evaluate model performance on a public arena leaderboard to assess overall user preference in an open-ended setting. Beyond this, we conduct comprehensive human assessments spanning five key dimensions: Instruction Following, Audio-Visual Synchronization, Visual Quality, Motion Quality, and Audio Quality, providing a fine-grained analysis of model capabilities. Furthermore, our multimodal inpainting and editing framework unlocks a wide range of practical applications, including but not limited to subject insertion, object removal, background replacement, and reference-guided video synthesis. We showcase representative examples of these applications in Appendix A .

[112] h3: 5.1 Artificial Analysis Arena

[113] p: Artificial Analysis [ ArtificialAnalysis ] is a widely recognized benchmarking platform for evaluating generative models across image and video generation domains. The platform operates an open arena where models are scored by the public, with Elo scores calculated from pairwise comparisons to reflect user preferences. We evaluate our model on the Artificial Analysis Video Arena, specifically on the text-to-video with audio generation track, which is designed to assess the quality of joint video–audio synthesis. Our model is benchmarked against notable external baselines including Veo 3.1, Kling 3.0, grok-imagine-video, Sora-2, Vidu-Q3, Wan 2.6, etc.

[114] p: Results: Our model ranks third on the leaderboard (as of 2026-02-24) among all participating systems (Figure 3 ), demonstrating strong and competitive audiovisual generation quality as evaluated by public user preferences.

[115] figure: Figure 3: Artificial Analysis Text-to-Video with Audio Arena Leaderboard. Our model ranks third among all competing baselines including Veo 3.1, grok-imagine-vide, Sora-2, Vidu-Q3, Wan 2.6 and etc.

[116] h3: 5.2 Human Assessments

[117] p: To comprehensively assess the joint video-audio generation capabilities, we introduce SkyReels-VABench , a novel human evaluation benchmark designed to evaluate state-of-the-art text-to-video+audio models in the market.

[118] h4: 5.2.1 Benchmark Design

[119] p: SkyReels-VABench extends our previous SkyReels-Bench [ 6 ] by incorporating comprehensive audio dimensions and multi-shot video scenarios. The benchmark comprises 2000+ carefully curated prompts spanning diverse content categories including advertising, social media content, narrative storytelling, educational content, and entertainment. The prompts are designed to test models across varying complexity levels, from single-shot scenarios to complex multi-shot sequences with sophisticated audio requirements.

[120] p: Language Coverage: The benchmark includes prompts in multiple languages, with particular emphasis on Chinese and English to assess cross-lingual generation capabilities.

[121] p: Content Diversity: Prompts cover a wide range of subjects (humans, animals, objects, abstract concepts), environments (indoor, outdoor, natural, urban), and temporal dynamics (static, slow-motion, fast-action sequences).

[122] p: Audio Complexity: The benchmark tests various audio modalities including speech (monologue, dialogue, narration), singing (various genres and vocal styles), sound effects (environmental, mechanical, natural), and background music (various genres and emotional tones).

[123] h4: 5.2.2 Evaluation Metrics

[124] p: Our evaluation framework encompasses five primary dimensions:

[125] figure: Table 2: Comprehensive Evaluation Dimensions for Audio-Visual Generation Dimension Sub-dimension Evaluation Criteria Instruction Following Video Instruction Following Subject description Accurate representation of subjects, attributes, and appearances Subject interaction Correct execution of actions, interactions, and motion dynamics Camera movement Proper execution of camera operations (pan, tilt, zoom, dolly) Style and aesthetics Adherence to visual styles, color palettes, and artistic directions Multi-shot consistency Correct shot transitions, cross-shot coherence, and reference accuracy Audio Instruction Following Semantic adherence Fidelity to audio content and characteristics Temporal accuracy Correct timing and duration of audio events Speaker attributes Speaker-visual matching, vocal characteristics, emotional tone, content accuracy Audio-Visual Synchronization Lip-sync accuracy Precise speech-mouth synchronization and correct speaker identification Sound effect alignment Temporal correspondence between visual events and sound effects Atmospheric matching Coherence between BGM, scene atmosphere, and emotional tone Spatial audio Sound spatialization matching visual source locations Visual Quality Visual clarity Sharpness, definition, and resolution Color accuracy Natural color balance and saturation without distortion Compositional quality Aesthetic composition, framing, and visual balance Structural integrity Absence of visual artifacts and corruptions Motion Quality Physical plausibility Adherence to physical laws (gravity, inertia, momentum) Motion fluidity Smooth transitions without abrupt discontinuities Motion stability Absence of jittering, deformation, and flickering Temporal consistency Consistency of dynamic elements across frames Motion vividness Action, camera, atmospheric, and emotional expressiveness Audio Quality Absence of artifacts No clipping, truncation, distortion, or glitches Spatial soundstage Appropriate stereo imaging and spatial rendering Timbre realism Natural and realistic tonal qualities Signal clarity Clean audio with appropriate signal-to-noise ratio Dynamic range Appropriate audio level variation without compression artifacts

[126] figure: Figure 4: Absolute scoring results (5-point Likert scale) comparing SkyReels V4 against baselines. Higher scores indicate better performance.

[127] figure: GSB overall quality comparison: SkyReels V4 vs. all baselines. Each bar shows the proportion of “Good”, “Same”, and “Bad” ratings. ((a)) SkyReels V4 vs. Kling 2.6 ((b)) SkyReels V4 vs. Seedance 1.5 Pro ((c)) SkyReels V4 vs. Veo 3.1 ((d)) SkyReels V4 vs. Wan 2.6 Figure 5: GSB comparison results. Top: Overall quality comparison between SkyReels V4 and all baselines. Bottom: Per-dimension GSB comparison across five evaluation dimensions: Prompt Following, Audio-Visual Synchronization, Visual Quality, Motion Quality, and Audio Quality.

[128] h4: 5.2.3 Evaluation Methodology

[129] p: We employ a dual-metric evaluation protocol conducted by a panel of 50 professional evaluators with backgrounds in video production, audio engineering, and content creation:

[130] p: Absolute Scoring: Evaluators rate each dimension using a 5-point Likert scale (1 = Extremely Dissatisfied, 2 = Dissatisfied, 3 = Neutral, 4 = Satisfied, 5 = Extremely Satisfied), enabling standardized performance comparison across models.

[131] p: Good-Same-Bad (GSB) Comparison: Pairwise comparisons between model outputs enable more granular quality differentiation. For each prompt, evaluators compare outputs from different models and assign one of three labels: "Good" (clearly better), "Same" (comparable quality), or "Bad" (clearly worse).

[132] h4: 5.2.4 Baselines

[133] p: We compare our model against state-of-the-art video-audio generation systems, including

[134] p: Veo 3.1 (Google)

[135] p: Kling 2.6 (Kuaishou)

[136] p: Seedance 1.5 Pro (ByteDance)

[137] p: Wan 2.6 (Alibaba)

[138] h4: 5.2.5 Results

[139] h5: Absolute Scoring.

[140] p: We first evaluate all models using the absolute scoring protocol, where human evaluators rate each dimension on a 5-point Likert scale. As shown in Figure 4 , SkyReels V4 achieves the highest overall average score among all competing models. The per-dimension breakdown reveals a nuanced picture of SkyReels V4’s strengths: it demonstrates particularly strong performance in Prompt Following and Motion Quality. For Visual Quality, SkyReels V4 performs comparably to the strongest competing models. While SkyReels V4 shows relatively modest advantages in Audio-Visual Synchronization and Audio Quality, it nonetheless maintains state-of-the-art performance in these dimensions as well, underscoring its overall competitiveness across the full evaluation spectrum.

[141] h5: Good-Same-Bad (GSB) Comparison.

[142] p: To further validate our model’s superiority, we conduct pairwise GSB comparisons between SkyReels V4 and each baseline. As illustrated in Figure 5 , SkyReels V4 consistently achieves a higher proportion of “Good” ratings against all competing models in terms of overall quality. The per-dimension GSB results for each pairwise comparison are presented, demonstrating that SkyReels V4 outperforms Kling 2.6, Seedance 1.5 Pro, Veo 3.1, and Wan 2.6 across the majority of evaluation dimensions.

[143] h2: 6 Conclusion

[144] p: In this work, we present SkyReels-V4 , a unified multi-modal video foundation model that jointly generates video and audio while supporting generation, inpainting, and editing within a single architecture. Built upon a dual-stream MMDiT design with a shared MMLM-based text encoder, SkyReels-V4 accepts rich multi-modal conditioning inputs—including text, images, video clips, masks, and audio references—and produces high-fidelity, synchronized video–audio outputs at cinematic quality (up to 1080p, 32 FPS, 15 seconds). To support diverse video creation tasks, we employ channel-concatenation to unify generation, inpainting, and editing by reformulating them as inpainting problems under specific mask configurations, while leveraging temporal-concatenation to flexibly incorporate multi-modal references such as images, video clips, and audio. Additionally, our joint low-resolution/high-resolution keyframe generation strategy enables efficient generation at scale.

[145] p: Extensive evaluations validate SkyReels-V4’s effectiveness. On the Artificial Analysis Arena, our model ranks among the top systems in the text-to-video-with-audio track. On our proposed SkyReels-VABench, SkyReels-V4 achieves the highest overall average score, with particularly strong performance in Prompt Following and Motion Quality, while maintaining state-of-the-art performance across all evaluation dimensions. Pairwise comparisons further confirm that SkyReels-V4 consistently outperforms competing baseline systems.

[146] p: To the best of our knowledge, SkyReels-V4 is the first model to simultaneously unify multi-modal inputs, joint video–audio generation, and generation/inpainting/editing capabilities at cinematic quality and scale. We hope this work serves as a foundation for future research in multi-modal video generation systems.

[147] h2: 7 Contributors

[148] p: We gratefully acknowledge all contributors for their dedicated efforts. The following lists recognize participants by their primary contribution roles:

[149] p: Project Sponsor: Yahui Zhou

[150] p: Project Leader: Guibin Chen (guibin.chen@kunlun-inc.com)

[151] p: Contributors:

[152] p: Infrastructure: Hao Zhang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Zhuangzhuang Liu, Wenyan Liu

[153] p: Data & Video Understanding: Mingyuan Fan, Yiming Wang, Mingshan Chang, Jiahua Wang, Yuqiang Xie, Peng Zhao, Xuanyue Zhong, Fuxiang Zhang, Peiyu Wang

[154] p: Video Model Training: Dixuan Lin, Jiangping Yang, Sheng Chen, Chaofeng Ao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Weikai Xu

[155] p: Audio Model Training: Zhengcong Fei, Zheng Chen, Tuanhui Li, Baoxuan Gu, Kaifei Wang, Xuchen Song

[156] p: Multi-modal Training: Youqiang Zhang, Debang Li, Nuo Pang, Yikun Dou, Xiaopeng Sun, Jingtao Xu, Binjie Mao, Liang Zeng, Haoxiang Guo

[157] p: Model Evaluation: Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng

[158] h2: References

[159] h2: Appendix A Application Examples

[160] figure: Table 3: Summary of video generation, inpainting, and editing tasks Main Task Subtask Description Generation Image + Audio Ref Generate videos from multiple reference images and audio inputs Image + Motion Ref Generate videos from image and video/motion reference (poses, trajectories) Inpainting Region Inpainting Inpaint subjects, attributes, or backgrounds in video regions Reference-Guided Inpaint using reference image guidance for style consistency Editing Element Removal Remove watermarks, subtitles, and logos intelligently Subject Manipulation Add, delete, or modify subjects in videos Attribute Editing Edit local attributes (color, texture, shape, etc.) Background Editing Modify backgrounds while preserving foreground Style Transfer Transform videos into different artistic styles Camera Control Modify shot angle, shot type, and camera position Scene Attributes Edit weather, lighting, tone, and time of day Subject + Motion Ref Combine subject and motion from different references Subject + Expression Ref Transfer facial expressions from reference video Background + Video Ref Combine background and video references First-Frame + Effect Ref Apply effects from reference to first-frame

[161] p: This appendix demonstrates typical application cases of our model in video-audio generation, inpainting, and editing. Our model supports flexible multimodal reference inputs, capable of processing various modalities including images, audio, and motion information. The following sections are organized into three main categories: Generation, Inpainting, and Editing.

[162] h3: A.1 Reference-based Generation

[163] h4: A.1.1 Multiple Image and Audio Reference Generation

[164] p: Our model can simultaneously accept multiple reference images and audio inputs to generate videos that are stylistically consistent with the references and audio-matched. The result is shown in Fig. 6 .

[165] figure: Instruction: In an elegantly decorated indoor environment with warm, intimate lighting, two people sit facing each other across a dark wooden table. The camera first focuses on @Actor-0, looking weary, says softly, <dialogue>I’m a little tired, I’m going back to my room to rest.</dialogue>@Audio-0. @Actor-1 sits across from @Actor-0, hands clasped on the table, and says with determination, <dialogue>I will pay a visit to your parents tomorrow.</dialogue>@Audio-1. Then @Actor-0 in another room, by the window, holds her phone to her ear and speaks, <dialogue>Mom, Li Zeting said he’s coming to our house tomorrow.</dialogue>@Audio-0. The scene shifts to another location—a warm-toned home interior, with a red fabric sofa visible in the background. @Actor-2, sitting tensely with phone to her ear, worries, <dialogue>But with our family’s situation, do you think he might look down on us?</dialogue>@Audio-2. <bgm>Soft, sorrowful music plays during the first two shots, transitioning to slow, melancholic tense music for the last two shots.</bgm> Ref. Image @Actor-0 @Actor-1 @Actor-2 Ref. Audio @Audio-0 @Audio-1 @Audio-2 Output Video Figure 6: Example of multiple images and audios reference.

[166] h4: A.1.2 Image Reference and Motion Reference Generation

[167] p: The model supports using image references to determine content and style, while simultaneously using motion references (e.g., pose sequences, trajectories) to control the dynamic characteristics of the generated video.

[168] p: Instruction: Animate the person in @image_1 using the movements from @video_1.

[169] table: Ref. Image Input Video Output Video

[170] p: Instruction: The medical professional in @image_1 and the curly-haired woman from @image_2 execute the dance movements demonstrated in @video_1, all set within the same stage environment as @video_1.

[171] table: Ref. Image Input Video Output Video

[172] figure: Figure 7: Examples of motion transfer in video reference.

[173] h3: A.2 Video Inpainting

[174] h4: A.2.1 Subject/Attribute/Background Inpainting

[175] p: The model can precisely inpaint specific regions in videos, including subject replacement, attribute modification, and background replacement.

[176] p: Instruction: Replace the subject in the mask area in @video_1 with a majestic elk standing in the same field.

[177] table: Input Video Masked Video Output Video

[178] p: Instruction: Change the color of the tie in the masked area of @video_1 to blue.

[179] table: Input Video Masked Video Output Video

[180] p: Instruction: Replace the background in the masked area of @video_1 with a stunning cinematic view of the Amalfi Coast in Italy during a warm golden hour sunset.

[181] table: Input Video Masked Video Output Video

[182] figure: Figure 8: Examples of subject/attribute/background inpainting.

[183] h4: A.2.2 Image Reference Inpainting

[184] p: The model supports using reference images to guide the inpainting process, ensuring that the inpainted content is consistent with the reference style.

[185] p: Instruction: Add the man from @image_1 to the left mask area of @video_1.

[186] table: Ref. Image Input Video Masked Video Output Video

[187] p: Instruction: Replace the right mask area in @video_1 with the cat from @image_1 and the left mask area in @video_1 with the woman from @image_2, ensuring a harmonious and natural scene.

[188] table: Ref. Image Input Video Masked Video Output Video

[189] figure: Figure 9: Examples of image reference inpainting.

[190] h3: A.3 Video Editing

[191] h4: A.3.1 Local Editing

[192] p: The model enables fine-grained local video editing: subject, attribute, and element edits.

[193] h5: Watermark/Subtitle/Logo Removal

[194] p: The model can intelligently identify and remove watermarks, subtitles, logos, and other elements from videos while maintaining content coherence and naturalness.

[195] p: Instruction: Remove watermarks in @video_1. Input Video Output Video

[196] p: Instruction: Remove the text overlay at the bottom of @video_1. Input Video Output Video

[197] p: Instruction: Remove the logo in the upper right corner in @video_1. Input Video Output Video

[198] figure: Figure 10: Examples of watermark/subtitle/logo removal.

[199] h5: Subject Manipulation

[200] p: The model supports adding, deleting, and modifying subjects in videos while maintaining temporal consistency.

[201] p: Instruction: Place a wooden bench with black metal armrests and legs on the grass next to the large rock on the right side of the path in @video_1.

[202] table: Input Video Output Video

[203] p: Instruction: Remove a bee from the center of @video_1.

[204] table: Input Video Output Video

[205] figure: Figure 11: Examples of subject manipulation.

[206] h5: Local Attribute Editing

[207] p: The model can perform fine-grained editing of attributes for specific objects or regions in videos, such as color, texture, shape, etc.

[208] p: Instruction: Change the chair’s color to black and replace its edges with wooden material in @video_1.

[209] table: Input Video Output Video

[210] p: Instruction: Change the man’s sleeveless shirt in @video_1 to a blue Polo shirt style.

[211] table: Input Video Output Video

[212] h5: Background Editing

[213] p: The model supports modifying background elements while preserving the foreground subjects.

[214] p: Instruction: Replace the background of @video_1 with a post-rain European cobblestone street scene at dusk.

[215] table: Input Video Output Video

[216] figure: Figure 12: Examples of local attribute editing.

[217] h4: A.3.2 Global Editing

[218] p: The model supports global modifications that affect the entire video, including style, camera properties, and scene attributes.

[219] h5: Style Transfer

[220] p: The model can transform videos into different artistic or visual styles while maintaining semantic consistency of the video content.

[221] p: Instruction: Transform @video_1 into Paper-Cutting style.

[222] table: Input Video Output Video

[223] p: Instruction: Transform @video_1 into LEGO style.

[224] table: Input Video Output Video

[225] figure: Figure 13: Examples of style transfer.

[226] h5: Camera Control

[227] p: The model supports modifying camera properties including shot angle, shot type, and camera position.

[228] p: Instruction: Re-render @video_1 with a Pan Right camera movement.

[229] table: Input Video Output Video

[230] figure: Figure 14: Examples of camera control.

[231] h5: Global Scene Attributes

[232] p: The model supports transforming global scene attributes such as weather, lighting, color tone, and time of day.

[233] p: Instruction: Make @video_1 nighttime.

[234] table: Input Video Output Video

[235] p: Instruction: Make @video_1 snowy.

[236] table: Input Video Output Video

[237] figure: Figure 15: Examples of global scene attributes.

[238] h4: A.3.3 Reference-Based Editing

[239] p: The model supports video editing based on image references, including subject reference, background reference, and first-frame reference, combined with reference videos to generate the final output. Reference videos can provide motion, expression, or visual effects guidance.

[240] h5: Subject Reference with Motion Reference

[241] p: The model can generate videos by combining a subject from a reference image with motion patterns from a reference video, matching action rhythm and trajectory.

[242] p: Instruction: Woman from @image_1 mimics gestures from @video_1 in its golden field background.

[243] table: Ref. Image Input Video Output Video

[244] figure: Figure 16: Example of subject reference with motion reference.

[245] h5: Subject Reference with Expression Reference

[246] p: The model can transfer natural facial expressions from a reference video to a subject from a reference image.

[247] p: Instruction: Transfer the facial expressions from @video_1 to the man in @image_1.

[248] table: Ref. Image Input Video Output Video

[249] figure: Figure 17: Example of subject reference with expression reference

[250] h5: Background Reference with Video Reference

[251] p: The model can combine a background from a reference image with content or motion from any reference video.

[252] p: Instruction: Replace the background of @video_1 with @image_1.

[253] table: Ref. Image Input Video Output Video

[254] figure: Figure 18: Example of background reference with video reference.

[255] h5: First-Frame Reference with Effect Reference

[256] p: The model can apply visual effects from a reference video to generate a video starting from a reference image, enabling effect transfer from the reference video.

[257] p: Instruction: Transfer the diamond morphing effect from @video_1 onto the subject in @image_1.

[258] table: Ref. Image Ref. Video Output Video

[259] figure: Figure 19: Example of first-frame reference with effect reference.

[260] h2: Instructions for reporting errors

[261] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[262] p: Tip: You can select the relevant text first, to include it in your report.

[263] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[264] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
