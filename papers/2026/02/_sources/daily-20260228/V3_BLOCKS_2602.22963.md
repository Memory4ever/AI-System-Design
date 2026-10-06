[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning

[3] h6: Abstract

[4] p: Multimodal large language models (MLLMs) have substantially advanced video misinformation detection through unified multimodal reasoning, but they often rely on fixed-depth inference and place excessive trust in internally generated assumptions, particularly in scenarios where critical evidence is sparse, fragmented, or requires external verification. To address these limitations, we propose FactGuard , an agentic framework for video misinformation detection that formulates verification as an iterative reasoning process built upon MLLMs. FactGuard explicitly assesses task ambiguity and selectively invokes external tools to acquire critical evidence, enabling progressive refinement of reasoning trajectories. To further strengthen this capability, we introduce a two-stage training strategy that combines domain-specific agentic supervised fine-tuning with decision-aware reinforcement learning to optimize tool usage and calibrate risk-sensitive decision making. Extensive experiments on FakeSV, FakeTT, and FakeVV demonstrate FactGuard’s state-of-the-art performance and validate its excellent robustness and generalization capacity.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: The rapid growth of large-scale online content-sharing platforms, such as TikTok, has accelerated the spread of information ( Bu et al., 2023 ) . This accessibility creates a fundamental asymmetry between rapid misinformation propagation and delayed manual verification, allowing misleading content to influence public discourse beyond the limits of human intervention. Consequently, post-hoc fact-checking becomes increasingly inadequate, highlighting the need for accurate and timely automated misinformation detection ( Sheng et al., 2025 ; Shang et al., 2021 ) .

[8] p: Among various content modalities, videos have emerged as a dominant and particularly challenging medium for misinformation dissemination due to their rich temporal dynamics and inherent multimodal complexity. In recent years, increasing attention has therefore been devoted to video misinformation detection, yielding encouraging progress. However, most existing approaches ( Qi et al., 2023a ; Bu et al., 2024 ; Qi et al., 2023b ) rely on task-specific discriminative models and lack the general understanding and reasoning capabilities, which are required for handling various verification needs in open-world scenarios.

[9] figure: Figure 1 : Comparison of video misinformation detection methods and our proposed FactGuard in terms of (a) explainability analysis and (b) comprehensive performance analysis.

[10] p: The rapid advancement of large-scale multimodal models has significantly improved multimodal content understanding and enabled reasoning-based approaches for misinformation verification. However, most existing methods remain constrained by a single-pass inference paradigm, lacking explicit mechanisms for uncertainty awareness and targeted evidence acquisition. In ambiguous or weakly verifiable scenarios, models therefore tend to rely on internally generated assumptions rather than grounding their reasoning in modality-specific or external evidence. As illustrated in Figure 3 (a), this behavior results in cross-modal hallucinations , where the model fabricates or misattributes visual or textural evidence that is not present in the input, and consequently leads to erroneous verification outcomes , namely confident but incorrect judgments about the factuality of the underlying claim. Consequently, reliable misinformation verification requires a system that can (1) identify when available information is insufficient, (2) selectively acquire targeted external evidence, and (3) iteratively refine its judgments based on new observations.

[11] p: Motivated by this insight, we propose FactGuard , an end-to-end agentic framework for video misinformation detection built on multimodal large language models (MLLMs). FactGuard formulates verification as an uncertainty-aware, iterative decision-making process, selectively invoking external tools when necessary to support reliable verification. Specifically, FactGuard introduces an agentic reasoning pipeline that integrates multimodal deliberation with explicit tool invocation and evidence-driven refinement. When the available information is insufficient for confident verification, the model adaptively selects external tools based on its reasoning state, including FactProbe for external knowledge verification and ClipScout for targeted visual evidence inspection, to supplement textual and visual inputs. The acquired evidence is incorporated into subsequent reasoning stages, enabling more informed and reliable verification outcomes. To further strengthen this capability, we construct a multimodal agentic Chain-of-Thought dataset for misinformation detection and perform supervised fine-tuning to establish structured reasoning and tool-invocation behaviors. We additionally incorporate a decision-aware reinforcement learning strategy that reinforces evidence-grounded reasoning while explicitly modeling tool usage, asymmetric error costs, and decision preferences under uncertainty. Together, these design choices enable FactGuard to move beyond existing approaches, establishing a general, and interpretable verification framework, as shown in Figure 1 .

[12] p: Our main contributions are as follows:

[13] p: We propose FactGuard , an agentic multimodal framework that formulates video misinformation detection as an iterative verification process with self-reflective reasoning and selective evidence acquisition.

[14] p: We construct a multimodal agentic Chain-of-Thought dataset for misinformation detection and perform targeted CoT-based supervised fine-tuning to inject domain-specific reasoning behaviors into MLLMs.

[15] p: We develop a decision-aware reinforcement learning strategy that explicitly models tool usage, asymmetric error costs, and decision-making preferences, leading to more calibrated and reliable verification outcomes.

[16] p: Extensive experiments on FakeSV, FakeTT, and FakeVV datasets demonstrate that FactGuard achieves state-of-the-art performance and consistently outperforms existing methods by a significant margin.

[17] h2: 2 Related Work

[18] h3: 2.1 Misinformation Detection

[19] figure: Figure 2 : Pipeline of FactGuard . The upper part illustrates the inference-time agentic verification process, where FactGuard assesses uncertainty based on the ambiguity of the input and selectively invokes external tools to acquire additional evidence before refining its reasoning and producing a final decision. The lower part depicts the training pipeline, which combines supervised fine-tuning with decision-aware reinforcement learning to reinforce structured reasoning, calibrated tool usage, and risk-sensitive verification behavior.

[20] p: Early studies on multimodal misinformation detection mainly focused on the image–text setting, where static visual content can be directly aligned with textual claims. These approaches ( Wang et al., 2018 ; Qian et al., 2021 ; Wang et al., 2023 ) model cross-modal interactions via attention, feature fusion, or contrastive learning to capture semantic consistency between images and text, achieving promising performance on social media benchmarks.

[21] p: In recent years, research on misinformation detection has moved beyond static images to the video domain, driven by the growing prevalence of video-based misinformation on social media platforms. Existing approaches ( Qi et al., 2021 ; Wang et al., 2025b ) typically focus on exploiting the rich multimodal signals embedded in videos by jointly modeling visual, acoustic, and textual information. Some studies ( Mittal et al., 2020 ; Xu et al., 2025 ) enhance detection performance by integrating linguistic patterns with emotional or prosodic cues from audio, while others ( Wang et al., 2025a ; McCrae et al., 2022 ) explicitly model cross-modal inconsistencies among video frames, audio streams, and subtitles. In addition, prior work ( Qureshi et al., 2021 ) has explored cross-channel watermarking for manipulation detection, as well as multimodal fusion frameworks that combine topic representations with keyframe-level visual features. More recent efforts ( Qi et al., 2023b ; Gong et al., 2025 ; Qi et al., 2023a ) further incorporate social context or neighborhood structures to capture relational dependencies among multimodal samples.

[22] h3: 2.2 Multimodal LLMs Reasoning

[23] p: Recent advances in multimodal large models (MLMs) have significantly improved the ability to jointly understand and reason over visual, textual, and auditory inputs. Models such as GPT-4V ( Yang et al., 2023 ) , LLaVA ( Guo et al., 2024 ; Li et al., 2023 ; Zhang et al., 2025b ; Lin et al., 2024 ) , and Qwen-VL ( Bai et al., 2023 ; Wang et al., 2024a ; Yang et al., 2025 ) demonstrate strong generalization across diverse multimodal tasks, enabling more expressive reasoning beyond traditional feature-level fusion.

[24] p: Building on these models, recent work has increasingly explored multimodal reasoning, including visual grounding ( Alayrac et al., 2022 ) , reasoning process prompting ( Wei et al., 2022 ) , and explanation generation ( Cheng et al., 2023 ) . By explicitly modeling intermediate reasoning steps, these methods improve both interpretability and performance on complex perceptual tasks. Reinforcement learning–based post-training has further enhanced model capabilities, as demonstrated by OpenAI-o1 ( Jaech et al., 2024b ) and DeepSeek-R1 ( Guo et al., 2025 ) .

[25] p: In misinformation detection, early efforts such as Fact-R1 ( Zhang et al., 2025a ) demonstrate the promise of combining large pretrained models with domain-specific fine-tuning and reinforcement learning.

[26] h3: 2.3 Tool-Augmented Agentic System

[27] p: Recent works ( Zheng et al., 2025 ; Cui et al., 2025 ) have increasingly explored augmenting multimodal models with external tools to support more complex reasoning and adaptive information access. Early studies ( Li et al., 2025 ; Sun et al., 2025 ) introduce tools as auxiliary sources of visual evidence, enabling models to ground intermediate reasoning steps in external perception signals. Subsequent efforts ( Liu et al., 2024 ; Zhao et al., 2025 ) investigate how tool usage can be learned rather than manually specified, through supervision or reinforcement signals that align tool invocation with task objectives. However, tool-augmented and agentic reasoning paradigms remain largely unexplored in video misinformation detection, which is still dominated by single-pass verification without iterative evidence acquisition or adaptive decision-making. In contrast, our work introduces an agentic, tool-augmented verification framework that enables iterative and evidence-driven reasoning.

[28] h2: 3 Methodology

[29] h3: 3.1 Overview

[30] p: As illustrated in Figure 2 , FactGuard formulates video misinformation verification as an agentic, iterative decision-making process that explicitly integrates multimodal reasoning, evidence-guided action, and outcome-aware optimization. In the following sections, we first introduce the agentic formulation of FactGuard and its two-stage inference process (Section 3.2 ), and then describe the evidence-guided action module that governs tool invocation and information acquisition, including FactProbe for external knowledge retrieval and ClipScout for targeted video-clip inspection (Section 3.3 ). We subsequently detail the training pipeline, including agentic Chain-of-Thought supervised fine-tuning (Section 3.4 ), and decision-aware reinforcement learning with structured rewards (Section 3.5 ).

[31] h3: 3.2 Problem Formulation

[32] p: Each input sample is represented as a triplet n = ( n vid , n aud , n txt ) n=(n^{\mathrm{vid}},n^{\mathrm{aud}},n^{\mathrm{txt}}) , where n vid n^{\mathrm{vid}} denotes the news video content, n aud n^{\mathrm{aud}} is the speech-to-text transcript extracted from the audio stream, and n txt n^{\mathrm{txt}} refers to textual metadata such as titles and keywords.

[33] p: Upon receiving the full multimodal input n n , the agent applies an agent policy 𝒜 θ \mathcal{A}_{\theta} to perform an initial chain-of-thought reasoning pass for assessing the difficulty and ambiguity of the case. The first-stage inference process is abstracted as:

[34] table: ( r t , a t ) = 𝒜 θ ( 1 ) ​ ( n , s t ) , (r_{t},\;a_{t})=\mathcal{A}_{\theta}^{(1)}\!\big(n,\,s_{t}\big), (1)

[35] p: where r t r_{t} denotes the reasoning trajectory generated at step t t , and a t a_{t} is the agent’s action decision indicating whether to invoke an external tool. The decision is conditioned on the initial observation n n together with the agent state s t s_{t} , which captures its current belief and uncertainty.

[36] p: If a tool is executed and returns an observation o t o_{t} , the agent incorporates this evidence and proceeds to a second-stage, evidence-augmented reasoning process. This refinement stage jointly considers both the original multimodal input and the tool feedback, and is formalized as:

[37] table: ( r t + 1 , y ^ ) = 𝒜 θ ( 2 ) ​ ( n , o t , s t + 1 ) , (r_{t+1},\;\hat{y})=\mathcal{A}_{\theta}^{(2)}\!\big(n,\,o_{t},\,s_{t+1}\big), (2)

[38] p: where r t + 1 r_{t+1} denotes the refined reasoning trajectory and y ^ \hat{y} is the final verdict. The second-stage reasoning conditions on both the original input n n and the tool-provided evidence o t o_{t} , enabling the agent to update its decision based on external verification signals. This agentic formulation promotes cautious, evidence-driven verification behaviour, which is essential for robust misinformation detection under ambiguous and information-scarce real-world conditions.

[39] h3: 3.3 Evidence-Guided Action Module

[40] p: When the first-stage reasoning identifies missing context or unresolved uncertainty, FactGuard issues an evidence-guided action to acquire supplementary information. Rather than relying on tools by default, tool invocation is treated as a deliberate verification decision that is triggered only when internal reasoning is deemed insufficient. In practice, FactGuard supports multiple evidence acquisition tools, including FactProbe and ClipScout .

[41] p: Formally, given an action decision at step t t , the agent invokes a tool operator 𝒯 \mathcal{T} , which executes the corresponding query and returns an observation:

[42] table: o t = 𝒯 ⁡ ( κ t , ψ t ) , o_{t}=\mathcal{T}(\kappa_{t},\psi_{t}), (3)

[43] p: where κ t \kappa_{t} specifies the selected tool identity and ψ t \psi_{t} denotes the associated query parameters.

[44] h4: External Knowledge Retrieval (FactProbe).

[45] p: Certain misinformation claims cannot be resolved solely from visual or audio cues, particularly those involving real-world events, historical facts, or temporal assertions. To address this limitation, FactGuard employs FactProbe , a retrieval-augmented knowledge access module that formulates structured factual queries based on the model’s current reasoning state and retrieves evidence from web-based sources. Retrieved results are filtered using reliability heuristics and summarized into a concise textual report, which is incorporated as auxiliary evidence in the refinement stage to supplement incomplete or uncertain textual information and support more reliable verification.

[46] h4: Video-Clip Temporal Inspection (ClipScout).

[47] p: Misinformation videos often exhibit long durations with substantial visual redundancy, while only a small number of localized temporal segments contain decisive evidence. ClipScout is designed to enable targeted inspection of such evidence-bearing intervals by selectively sampling representative frames from queried time spans and aggregating them into a compact visual summary. This focused visual evidence supports evidence-oriented reasoning by guiding the model’s attention toward salient events. Through repeated agentic interaction and training, the model learns to efficiently localize and ground critical visual cues without exhaustively processing the entire video.

[48] h3: 3.4 Agentic Supervised Fine-Tuning

[49] p: To address the limited reasoning horizon and underdeveloped tool-usage behaviors of existing multimodal models in misinformation detection, we construct a misinformation-oriented agentic Chain-of-Thought (CoT) dataset that provides structured demonstrations of multi-round reasoning, tool selection intent, and evidence-grounded reflection.

[50] p: Each annotated trajectory records how the agent analyzes multimodal content, determines when external evidence is required, and incorporates retrieved evidence to refine subsequent reasoning and the final judgment. This reframes misinformation detection from a one-shot classification task into an agentic, self-regulated decision-making process.

[51] p: We then perform chain-of-thought supervised fine-tuning to align the model with these agentic reasoning behaviors. Given an input n n and its annotated agent trajectory τ = ( r t , a t , o t , r t + 1 , y ^ ) \tau=(r_{t},a_{t},o_{t},r_{t+1},\hat{y}) , the model is trained to maximize the likelihood of the full reasoning and action sequence:

[52] table: ℒ SFT = − 𝔼 ( n , τ ) ∼ 𝒟 ​ [ log ⁡ p θ ​ ( τ ∣ n ) ] . \mathcal{L}_{\mathrm{SFT}}=-\mathbb{E}_{(n,\tau)\sim\mathcal{D}}\big[\log p_{\theta}(\tau\mid n)\big]. (4)

[53] p: This supervision encourages the model to internalize longer reasoning chains, explicit uncertainty awareness, and evidence-seeking preferences in ambiguous cases. As a result, FactGuard avoids premature or over-confident conclusions and develops verification-oriented reasoning behaviors that are critical for real-world misinformation detection.

[54] h3: 3.5 Decision-Aware Reinforcement Learning

[55] p: To further calibrate the verification policy under uncertainty, we introduce a decision-aware reinforcement learning stage.

[56] h4: Group Relative Policy Optimization (GRPO).

[57] p: We adopt GRPO as a critic-free reinforcement learning paradigm that operates at the level of full agent trajectories. For each input instance, the policy generates a group of candidate trajectories, each reflecting different reasoning depth, tool-invocation behaviour, and final prediction outcomes. GRPO performs groupwise comparison over these trajectories and updates the policy according to their relative verification quality. The policy network π θ \pi_{\theta} is optimized by an importance-weighted objective with KL regularization against a frozen reference model:

[58] table: ℒ G ​ R ​ P ​ O ​ ( θ ) = 𝔼 q ∼ P ⁡ ( Q ) , { o i } i = 1 G ∼ π θ old ​ ( O | q ) [ ∑ i = 1 G π θ ​ ( o i | q ) π θ old ​ ( o i | q ) ⋅ A i − β 𝔻 K ​ L ( π θ | | π r ​ e ​ f ) ] , \begin{split}\mathcal{L}_{GRPO}(\theta)=\mathbb{E}_{q\sim P(Q),\{o_{i}\}^{G}_{i=1}\sim\pi_{\theta_{\text{old}}}{(O|q)}}\\ \left[\sum_{i=1}^{G}\frac{\pi_{\theta}(o_{i}|q)}{\pi_{\theta_{\text{old}}}(o_{i}|q)}\cdot A_{i}-\beta\mathbb{D}_{KL}(\pi_{\theta}||\pi_{ref})\right],\end{split} (5)

[59] table: 𝔻 K ​ L ( π θ | | π r ​ e ​ f ) = π r ​ e ​ f ​ ( o | q ) π θ ​ ( o | q ) − log π r ​ e ​ f ​ ( o | q ) π θ ​ ( o | q ) − 1 , \mathbb{D}_{KL}(\pi_{\theta}||\pi_{ref})={\frac{\pi_{ref}(o|q)}{{\pi_{\theta}}(o|q)}}-\log{\frac{\pi_{ref}(o|q)}{{\pi_{\theta}}(o|q)}}-1, (6)

[60] p: where β \beta controls the trade-off between exploration and stability, π θ old \pi_{\theta_{\text{old}}} denotes the rollout policy used for trajectory sampling, and π ref \pi_{\mathrm{ref}} is a frozen reference model that stabilizes policy updates. The KL term serves as a pointwise surrogate of the KL divergence for efficient policy regularization. Each trajectory τ i \tau_{i} is assigned a task-specific reward based on verification reliability, including the correctness of the decision and the quality of its reasoning and tool usage. To enable stable comparison within each trajectory group, we compute a normalized advantage:

[61] table: A i = R ⁡ ( τ i ) − mean ⁡ ( { R ⁡ ( τ j ) } ) std ⁡ ( { R ⁡ ( τ j ) } ) , A_{i}=\frac{R(\tau_{i})\;-\;\mathrm{mean}(\{R(\tau_{j})\})}{\mathrm{std}(\{R(\tau_{j})\})}, (7)

[62] p: which reduces reward-scale variance and emphasizes trajectories exhibiting stronger evidence-grounded agent behaviours relative to their peers.

[63] figure: Figure 3 : Key advantages of FactGuard. (a) MLLM-based methods with enhanced reasoning may induce cross-modal hallucination in ambiguous cases by over-relying on internally generated assumptions, treating them as grounded evidence without acquiring or validating critical supporting information. (b) FactGuard formulates misinformation verification as an uncertainty-aware, tool-assisted decision-making process that adaptively refines its conclusions, enabling reliable verification in open and dynamic environments.

[64] h4: Reward Design.

[65] p: To ensure that reinforcement learning optimizes verification-oriented decision behavior rather than merely maximizing label accuracy, we design a gated reward function that jointly models decision correctness, tool usage, and risk sensitivity for multimodal misinformation detection. We first define the overall trajectory reward and then describe each component in turn. Specifically, for each agent trajectory τ \tau , the total reward is formulated as:

[66] table: R ⁡ ( τ ) = R acc ​ ( τ ) + R format ​ ( τ ) + λ ​ R risk ​ ( τ ) + R tool ​ ( τ ) . R(\tau)=R_{\mathrm{acc}}(\tau)+R_{\mathrm{format}}(\tau)+\lambda\,R_{\mathrm{risk}}(\tau)+R_{\mathrm{tool}}(\tau). (8)

[67] p: R acc ​ ( τ ) R_{\mathrm{acc}}(\tau) provides outcome-level supervision based on the final prediction y ^ \hat{y} , encouraging correct verification decisions. To reflect the asymmetric risk profile inherent in misinformation detection, we introduce an explicit risk-shaping term:

[68] table: R risk ​ ( τ ) = − α ​ 𝕀 FP ​ ( τ ) − γ ​ 𝕀 FN ​ ( τ ) , R_{\mathrm{risk}}(\tau)=-\alpha\,\mathbb{I}_{\mathrm{FP}}(\tau)-\gamma\,\mathbb{I}_{\mathrm{FN}}(\tau), (9)

[69] p: where 𝕀 FP ​ ( τ ) \mathbb{I}_{\mathrm{FP}}(\tau) and 𝕀 FN ​ ( τ ) \mathbb{I}_{\mathrm{FN}}(\tau) indicate false-positive and false-negative outcomes, respectively. The coefficients α \alpha and γ \gamma explicitly control the trade-off between precision and recall, allowing the detector’s risk preference to be adjusted for different misinformation scenarios.

[70] p: Beyond decision outcomes, reinforcement learning is constrained to valid and interpretable agent behaviors. Accordingly, R format ​ ( τ ) R_{\mathrm{format}}(\tau) enforces well-formed outputs by requiring structured reasoning and final decisions to be enclosed within <think> and <answer> tags, thereby restricting policy optimization to well-defined agent trajectories.

[71] p: In addition to supervising decision correctness and output validity, we introduce an action-level reward to explicitly regulate tool usage. Tool invocation is treated as a deliberate verification action and is rewarded only when it leads to a correct verification outcome, while unnecessary or ineffective tool use is penalized:

[72] table: R tool ​ ( τ ) = { r tool + , tool used and ​ R acc ​ ( τ ) > 0 , − r tool − , tool used and ​ R acc ​ ( τ ) ≤ 0 , 0 , otherwise . R_{\mathrm{tool}}(\tau)=\begin{cases}\;\;\;r_{\mathrm{tool}}^{+},&\text{tool used and }R_{\mathrm{acc}}(\tau)>0,\\ -\,r_{\mathrm{tool}}^{-},&\text{tool used and }R_{\mathrm{acc}}(\tau)\leq 0,\\ 0,&\text{otherwise}.\end{cases} (10)

[73] p: This design discourages indiscriminate tool usage while rewarding evidence-seeking behavior only when it contributes to correct verification. Consequently, GRPO optimizes verification-oriented agent behavior under uncertainty beyond raw label accuracy, including calibrated tool invocation, evidence-grounded reasoning, and adaptive risk control. Unlike prior reinforcement learning methods that focus solely on output correctness, our approach treats misinformation detection as a decision-aware agentic problem, in which uncertainty handling and tool usage are first-class optimization objectives.

[74] figure: Table 1: Performance comparison on FakeSV, FakeTT and FakeVV datasets. We highlight the improvements achieved by FactGuard. Model FakeSV FakeTT FakeVV Acc Prec Rec F1 Acc Prec Rec F1 Acc Prec Rec F1 BERT ( Koroteev, 2021 ) 65.4 66.0 66.5 66.2 68.7 67.5 67.5 67.5 60.4 57.9 56.8 57.3 TikTec ( Shang et al., 2021 ) 64.8 63.2 61.9 62.5 61.1 64.8 64.2 64.5 59.3 59.1 59.5 59.3 FANVM ( Choi & Ko, 2021 ) 65.4 66.1 64.3 65.2 68.9 64.7 68.8 67.1 61.9 60.7 60.8 60.8 SV-FEND ( Qi et al., 2023a ) 67.1 67.4 66.3 66.8 67.6 72.2 69.0 70.6 70.9 71.4 71.3 71.3 FakingRec ( Bu et al., 2024 ) 69.5 69.7 70.4 70.0 71.0 71.9 72.0 72.0 72.1 72.4 71.6 72.0 Gemini2-thinking ( Gemini Team, 2023 ) 63.1 61.8 61.9 61.9 56.6 55.2 55.3 55.3 51.5 46.0 46.0 48.6 GPT-4o ( Achiam et al., 2023 ) 66.6 65.2 64.7 64.9 57.9 57.8 62.9 60.2 56.0 60.4 35.0 44.3 GPT-o1-mini ( Jaech et al., 2024a ) 60.3 57.7 56.5 57.1 52.5 51.6 51.7 51.7 47.5 46.9 37.6 41.8 DeepSeek-R1 ( Guo et al., 2025 ) 61.8 60.4 60.3 60.3 49.8 52.6 52.5 52.6 53.5 58.1 25.2 35.1 Qwen2.5-VL-7B ( Bai et al., 2025 ) 55.6 55.5 55.7 55.6 54.9 54.0 54.1 54.0 52.9 51.1 51.1 51.1 Qwen2.5-VL-72B ( Bai et al., 2025 ) 57.6 55.4 55.2 55.3 59.2 58.1 58.3 58.2 54.0 60.0 24.0 34.3 QVQ-72B-preview ( Qwen Team, 2024 ) 60.8 59.0 58.8 58.9 58.1 54.0 52.8 53.4 53.5 52.6 52.6 52.6 InternVL2.5-8B ( Chen et al., 2024 ) 49.8 52.6 52.5 52.6 43.9 44.0 44.0 44.0 53.5 58.5 24.0 34.0 InternVL2.5-78B-MPO ( Wang et al., 2024b ) 57.5 53.0 52.0 52.5 59.2 57.1 56.7 56.9 54.0 60.0 24.0 34.3 Fact-R1 ( Zhang et al., 2025a ) 75.6 77.7 72.0 74.7 74.4 77.8 68.3 72.7 81.2 84.5 76.4 80.3 FactGuard (Ours) 79.3 82.2 80.6 81.4 75.3 73.8 76.7 75.2 83.0 85.8 82.1 83.9

[75] h2: 4 Experiment

[76] h3: 4.1 Experimental Settings

[77] h4: Baselines.

[78] p: To comprehensively evaluate the performance of FactGuard, we compare it against three categories of baselines. Discriminative Models include the single-modality method, BERT ( Koroteev, 2021 ) and multimodal methods such as TikTec ( Shang et al., 2021 ) , FANVM ( Choi & Ko, 2021 ) , SVFEND ( Qi et al., 2023a ) , and FakingRec ( Bu et al., 2024 ) . Zero-shot MLLMs comprise closed-source models, including Gemini2-thinking ( Gemini Team, 2023 ) , GPT-4o ( Achiam et al., 2023 ) , and GPT-o1-mini ( Jaech et al., 2024a ) , as well as open-source models, including Qwen2.5-VL ( Bai et al., 2025 ) , InternVL2.5 ( Chen et al., 2024 ) , QVQ-72B ( Qwen Team, 2024 ) , InternVL2.5-MPO ( Wang et al., 2024b ) , and DeepSeek-R1 ( Guo et al., 2025 ) , which are evaluated in a zero-shot setting. For models without native video support, textual descriptions of news videos are used as substitutes. Finally, Task-Aligned Reasoning Models include Fact-R1 ( Zhang et al., 2025a ) and our method.

[79] h4: Benchmarks.

[80] p: We employ three widely adopted benchmark datasets: FakeSV ( Qi et al., 2023a ) , FakeTT ( Bu et al., 2024 ) , and FakeVV ( Zhang et al., 2025a ) . Following the protocol in ( Qi et al., 2023a ) , we use a temporal split for testing, selecting the most recent 15% of samples from each dataset. In accordance with the Fact-R1 standard, all baseline models are trained on the training sets of FakeVV, FakeTT, and FakeSV. We report four standard evaluation metrics, including accuracy (ACC), precision, recall, and F1 score, to provide a comprehensive assessment of classification performance.

[81] h4: Training Details.

[82] p: Our model is trained on Qwen2.5-VL-7B using a two-stage pipeline consisting of supervised fine-tuning (SFT) followed by decision-aware reinforcement learning with GRPO. All experiments are conducted on 8 NVIDIA H100 GPUs. During GRPO training, each input prompt is unfolded into 8 candidate trajectories. The video-clip inspection tool can be invoked at most once per prompt, while external knowledge retrieval is unconstrained. We set the learning rate to 1 × 10 − 6 1\times 10^{-6} and train the policy for one epoch. The maximum prompt length is set to 16,384 tokens, and the maximum response length is 768 tokens. The KL regularization coefficient is set to 0.04. Unless otherwise specified, we use a per-device batch size of 1 with no gradient accumulation. Additional implementation details are provided in Appendix A.1 .

[83] h3: 4.2 Main Results

[84] h4: Comparison to State-of-the-Art Approaches.

[85] p: As shown in Table 1 , we evaluate FactGuard on the FakeSV, FakeTT, and FakeVV datasets and compare it with discriminative models, zero-shot MLLMs, and task-aligned reasoning models specifically trained or reinforced for misinformation detection. All results are reported using accuracy, precision, recall, and F1-score. Overall, FactGuard consistently outperforms existing methods across all datasets in terms of both accuracy and F1 score.

[86] p: For discriminative approaches, FakingRec yields the strongest performance, benefiting from its effective modeling of fine-grained multimodal correlations and its exploitation of user–content interaction patterns, which are particularly suited for recommendation-style verification. For zero-shot MLLMs, GPT-4o attains the highest accuracy, likely due to its large-scale multimodal pretraining and strong general reasoning priors. Within the same model family, larger models generally exhibit better performance, although their effectiveness varies across datasets, reflecting differences in task difficulty and evidence availability.

[87] p: Compared to discriminative methods, task-aligned reasoning approaches, including Fact-R1 and our method, not only provide improved interpretability through explicit reasoning processes but also achieve substantially higher verification accuracy. While Fact-R1 significantly improves performance via reinforcement learning, FactGuard consistently delivers superior results. As illustrated in Figure 3 (b), this advantage stems from FactGuard’s ability to avoid cross-modal hallucination in ambiguous cases by explicitly recognizing uncertainty and adaptively acquiring supporting evidence through tool-assisted, iterative decision making.

[88] figure: Figure 4 : Qualitative analysis of model reasoning. Representative reasoning traces under correct predictions show that FactGuard produces more coherent and evidence-grounded reasoning than Qwen2.5-VL and Fact-R1, highlighting improved interpretability.

[89] h4: Explainability Analysis.

[90] p: Compared to discriminative models, multimodal large language model–based approaches not only produce final predictions but also generate explicit reasoning traces, substantially improving interpretability. Accordingly, we adopt GPT-4o as an automatic evaluator to assess the quality of model-generated reasoning and to provide fine-grained reasoning accuracy scores. The evaluation considers multiple complementary dimensions, including faithfulness to the provided multimodal evidence, logical consistency of the reasoning chain, and the ability to capture salient misinformation patterns.

[91] p: To ensure a fair and meaningful evaluation, we restrict the analysis to instances where the predicted labels are correct, thereby preventing incorrect predictions from confounding the assessment of reasoning quality. As illustrated in Figure 4 , we compare Qwen2.5-VL and Fact-R1 without tool assistance against their tool-augmented counterparts, Qwen2.5-VL with tools and FactGuard. The results indicate that both reinforcement learning and external tool integration contribute to improved reasoning capability over the base model. Reinforcement learning enhances the model’s ability to generate structured and consistent reasoning, while tool integration further strengthens evidence grounding. Notably, their combination yields a complementary effect: FactGuard consistently exhibits the strongest reasoning performance, producing coherent, evidence-grounded, and logically sound inference chains across diverse cases.

[92] figure: Table 2: Cost-sensitive precision and recall achieved by FactGuard on FakeSV and FakeVV under different asymmetric error cost ratios. Cost Ratio FakeSV FakeVV ( α : γ \alpha:\gamma ) Precision Recall Precision Recall 1:2 80.8 82.1 83.2 83.7 1:1 82.2 80.6 85.8 82.1 2:1 83.2 75.0 86.6 79.3

[93] h4: Cost-Sensitive Risk Analysis.

[94] p: We report the precision and recall on the FakeSV and FakeTT datasets to analyze the effect of cost-sensitive risk modeling. As shown in the Table 2 , the cost ratio α : γ \alpha:\gamma plays a critical role in shaping the trade-off between precision and recall. When α \alpha is increased, the model places a higher penalty on false positives, leading to improved Fake precision at the cost of a modest reduction in recall. Conversely, emphasizing γ \gamma encourages the model to reduce false negatives, resulting in higher recall but lower precision. This behavior highlights the flexibility of the proposed cost-sensitive risk function in regulating decision preferences under asymmetric error costs. Unless otherwise specified, we adopt a balanced cost ratio of α : γ = 1 : 1 \alpha:\gamma=1:1 in all other experiments.

[95] p: Unlike conventional misinformation detectors that optimize a fixed objective, FactGuard enables explicit control over the precision–recall balance, allowing the verification policy to be adapted to different deployment requirements. In practice, this is particularly important for misinformation detection, where the relative costs of false alarms and missed misinformation can vary substantially across application scenarios. For example, high-precision settings are desirable in content moderation to avoid unjustified censorship, whereas high-recall configurations are preferable in early-warning or monitoring systems to minimize the spread of harmful content. These results demonstrate that FactGuard offers a principled and practical approach to risk-aware verification, effectively bridging model optimization with real-world decision-making constraints.

[96] figure: Table 3: Ablation study of FactGuard on FakeSV and FakeTT datasets. We report Accuracy (%) and F1-score (%) to evaluate the contribution of each component. Model FakeSV FakeTT Acc F1 Acc F1 FactGuard (Ours) 79.3 81.4 75.3 75.2 w/o SFT 73.1 74.7 71.6 68.2 w/o RL 62.0 63.2 67.9 65.7 w/o R t ​ o ​ o ​ l R_{tool} 77.7 78.5 74.7 72.9 w/o R r ​ i ​ s ​ k R_{risk} 78.5 78.9 74.9 73.8 Base (Qwen2.5-VL-7B+tool) 57.6 60.6 56.8 55.4

[97] h3: 4.3 Ablation Studies

[98] h4: Variants of component ablations.

[99] p: Table 3 presents the ablation results of FactGuard on the FakeSV and FakeTT datasets. The full model consistently achieves the best performance, indicating that all components contribute positively to misinformation detection. Removing either supervised fine-tuning (SFT) or reinforcement learning (RL) leads to substantial performance degradation, with the absence of RL causing the most severe drop, highlighting its critical role in optimizing multi-step verification and decision-making. In contrast, ablating the tool-related reward ( R tool R_{\mathrm{tool}} ) or the risk-aware reward ( R risk R_{\mathrm{risk}} ) results in moderate but consistent performance declines, suggesting that these rewards provide complementary benefits by improving evidence grounding and uncertainty calibration.

[100] p: We find that reinforcement learning without prior SFT yields inferior performance, consistent with Video-Star ( Yuan et al., 2025 ) . Direct RL causes the policy to collapse toward tool-free reasoning, as it must simultaneously explore complex reasoning trajectories and tool-use decisions under distributional mismatch. This motivates our two-stage training scheme, where SFT establishes structured evidence-seeking behaviors before RL refinement.

[101] h4: Variants of different GRPO hyperparameters.

[102] p: As shown in Table 4 , increasing the number of rollouts generally improves performance by yielding more reliable advantage estimates, with diminishing returns beyond 8 rollouts, while further increasing the number of rollouts incurs additional computational overhead with limited efficiency gains. We also observe that the KL coefficient β \beta exhibits a clear trade-off: overly small values lead to insufficient regularization, while larger values overly constrain policy updates. Based on this balance, we adopt 8 rollouts and β \beta = 0.04.

[103] figure: Table 4: Performance of GRPO variants on FakeSV and FakeTT. Variant FakeSV FakeTT Acc F1 Acc F1 (a) w/. Rollouts = 6 77.3 78.9 72.6 69.4 (b) w/. Rollouts = 8 (Ours) 79.3 81.4 75.3 75.2 (c) w/. Rollouts = 12 79.5 81.5 75.2 74.3 (d) w/. β \beta = 0.02 78.2 79.5 74.6 73.4 (e) w/. β \beta = 0.04 (Ours) 79.3 81.4 75.3 75.2 (f) w/. β \beta = 0.06 78.8 80.9 74.8 73.7

[104] h2: 5 Conclusion

[105] p: In this work, we presented FactGuard , an agentic framework for video misinformation detection that formulates verification as an uncertainty-aware, iterative decision-making process. By integrating multimodal reasoning with selective, tool-assisted evidence acquisition, FactGuard addressed key limitations of existing approaches, including over-reliance on internally generated assumptions and the failure to obtain critical supporting evidence in ambiguous cases. We further introduced a two-stage training strategy that combines agentic Chain-of-Thought supervised fine-tuning with decision-aware reinforcement learning, enabling high-quality reasoning, calibrated tool usage, and explicit control over asymmetric verification risks. Extensive experiments on three public benchmarks demonstrate that FactGuard consistently outperforms strong discriminative baselines and MLLM-based reasoning models, including reinforcement learning–enhanced methods, in both prediction accuracy and reasoning quality.

[106] h2: Impact Statement

[107] p: This work aims to advance research in multimodal reasoning, agentic decision-making, and video misinformation detection. The proposed framework is developed solely for research purposes and is intended to support the study of reliable and interpretable verification systems. All datasets used in this work are publicly available and are employed in accordance with their respective licenses and intended usage scopes. Any additional data constructed for training or evaluation are synthetically generated or obtained through automated processes, and are used exclusively for research purposes. While the techniques studied in this work could potentially be applied in real-world verification or content moderation scenarios, we emphasize that our contributions are intended as research tools rather than deployment-ready systems. We do not foresee significant negative societal impact when the proposed methods are used responsibly and within their intended research scope.

[108] h2: References

[109] h2: Appendix

[110] p: In this appendix, we provide more experimental details, related work, tool library, and discussions for a comprehensive evaluation and understanding of our method. Detailed contents are as follows:

[111] h2: Appendix A Experiment

[112] h3: A.1 More Experimental Details

[113] h4: Datasets.

[114] p: A variety of datasets have been developed to facilitate research on video-based misinformation detection. Early datasets typically focused on narrow domains, such as medical misinformation ( Hou et al., 2019 ) or COVID-19-related content ( Knuutila et al., 2021 ) , and often covered multiple languages. While valuable for domain-specific analysis, these datasets are generally limited in scale, topical diversity, and long-term public availability.

[115] p: More recent benchmarks have shifted toward large-scale, short-video misinformation detection. In particular, FakeSV ( Qi et al., 2023a ) consists of short news-style videos collected from social media platforms, paired with textual metadata and crowd-sourced annotations. FakeTT ( Bu et al., 2024 ) focuses on TikTok videos and incorporates multimodal signals including visual content, audio transcripts, and user interaction features. FakeVV ( Zhang et al., 2025a ) focuses on more complex and ambiguous misinformation scenarios and offers richer multimodal signals and annotations, enabling more comprehensive evaluation of reasoning-oriented verification models.

[116] p: Together, these datasets provide complementary coverage in terms of content sources, multimodal structure, and verification difficulty, enabling comprehensive evaluation of video misinformation detection systems under diverse real-world conditions. Accordingly, all experimental evaluations in this work are conducted on FakeSV, FakeTT, and FakeVV.

[117] h4: Training Details.

[118] p: To support agentic reasoning and tool-aware decision making, we first construct a multimodal agentic Chain-of-Thought (CoT) dataset tailored for video misinformation detection. Starting from the training sets of FakeSV, FakeTT, and FakeVV, we employ a stronger teacher model, Qwen2.5-VL-72B, to generate agentic reasoning trajectories under carefully designed prompts. These prompts explicitly encourage uncertainty assessment, tool-selection intent, evidence grounding, and final verification decisions conditioned on multimodal inputs.

[119] p: Given the multimodal input and the ground-truth label, the teacher model produces full agent trajectories, including intermediate reasoning steps, tool invocation decisions, and evidence-aware conclusions. To ensure data quality, we apply a two-stage filtering process. First, rule-based validation removes malformed trajectories, such as missing reasoning structure, invalid tool actions, or incorrect final decisions. Second, a subset of samples is manually inspected to further eliminate low-quality or hallucinated reasoning traces. Only high-quality, coherent, and evidence-grounded trajectories are retained for supervised fine-tuning.

[120] p: We perform agentic supervised fine-tuning (SFT) on Qwen2.5-VL-7B-Instruct using the curated agentic CoT dataset. The objective of this stage is to inject structured reasoning patterns, explicit uncertainty awareness, and tool-invocation behaviors into the base model prior to reinforcement learning.

[121] p: Training is conducted with mixed-precision (BF16) and DeepSpeed optimization. We use a per-device batch size of 1 with gradient accumulation and train the model for one epoch. Gradient checkpointing and FlashAttention are enabled to reduce memory consumption. This SFT stage provides essential inductive bias for evidence-seeking and multi-step reasoning, which we find to be critical for stabilizing and guiding subsequent reinforcement learning.

[122] p: Following supervised fine-tuning, we further optimize FactGuard using decision-aware reinforcement learning with Group Relative Policy Optimization (GRPO). All reinforcement learning experiments are conducted on 8 NVIDIA H100 GPUs.

[123] p: During GRPO training, each input prompt is unfolded into 8 candidate trajectories, capturing diverse reasoning paths, tool-invocation behaviors, and final verification outcomes. The video-clip inspection tool is restricted to at most one invocation per prompt, encouraging selective and deliberate visual evidence acquisition, while external knowledge retrieval remains unconstrained. Unless otherwise specified, the model is configured with a balanced cost setting ( α : γ = 1 : 1 \alpha:\gamma=1:1 ), encouraging neutral treatment of false positives and false negatives during trajectory generation.

[124] p: We set the learning rate to 1 × 10 − 6 1\times 10^{-6} and train the policy for one epoch. The maximum prompt length is set to 16,384 tokens and the maximum response length is 768 tokens. The KL regularization coefficient is fixed to 0.04 to stabilize policy updates against a frozen reference model. We use a per-device batch size of 1 without gradient accumulation.

[125] p: This reinforcement learning stage refines verification decisions under task-aligned rewards, explicitly calibrating tool usage and asymmetric error costs, and further strengthens evidence-grounded reasoning beyond supervised imitation.

[126] h3: A.2 More Results

[127] p: As illustrated in Figure 5 , when confronted with uncertain or insufficient evidence, FactGuard adaptively invokes multiple tools to refine its verification process. Specifically, FactGuard first calls FactProbe to retrieve external knowledge and verify the factual validity of the claimed event. It then employs ClipScout to perform focused visual analysis, attending to the reactions of surrounding spectators in the video. By integrating the retrieved factual evidence with the localized visual cues, FactGuard is able to conduct a more informed and reliable reasoning process, ultimately leading to a more accurate and well-supported conclusion.

[128] figure: Figure 5 : Additional Case Study of FactGuard.

[129] h2: Appendix B Tool Library Details

[130] p: FactGuard is equipped with a lightweight yet effective tool library to support evidence acquisition during agentic verification. The tool library is designed to complement the model’s internal multimodal reasoning by providing access to external factual knowledge and localized visual evidence. In this work, we implement two core tools: an external knowledge retrieval tool ( FactProbe ) and a video clip inspection tool ( ClipScout ). These tools are selectively invoked by the agent when internal reasoning alone is insufficient for confident verification.

[131] h3: B.1 External Knowledge Retrieval (FactProbe)

[132] p: FactProbe implements a retrieval-augmented generation (RAG) pipeline for external factual verification. Given a structured factual query produced by the agent during the first-stage reasoning, the tool issues a web search request via a commercial search API (Serper) to retrieve a small set of relevant results. To reduce noise, only organic search results are retained, and user-generated or social media sources are excluded.

[133] p: For each query, the tool collects the top-ranked results and extracts their titles, snippets, and source links. The retrieved content is then aggregated into a compact textual report that summarizes the external evidence relevant to the queried claim. Rather than performing full document reading, FactProbe adopts a lightweight retrieval-and-snippet strategy to balance evidence coverage and efficiency. The resulting report is passed to the second-stage reasoning process as auxiliary textual input, enabling the model to incorporate externally grounded information during verification.

[134] h3: B.2 Video Clip Temporal Inspection (ClipScout)

[135] p: ClipScout provides targeted temporal inspection of video content by extracting representative frames from a specified time interval. When the agent invokes ClipScout, it outputs a precise temporal query (e.g., a start–end timestamp) corresponding to the most evidence-bearing segment of the video.

[136] p: The tool decodes the video stream and uniformly samples a small number of frames (four by default) within the queried interval. These frames are then arranged into a 2 × 2 2\times 2 visual grid to form a compact visual summary. To control computational and token overhead, the grid is resized such that its maximum spatial dimension does not exceed a fixed resolution threshold.

[137] p: The resulting composite image is appended to the multimodal input during the refinement stage, allowing the model to reason over localized visual evidence without processing the entire video. ClipScout is constrained to at most one invocation per instance, ensuring that temporal inspection remains selective and aligned with deliberate evidence acquisition rather than exhaustive visual scanning.

[138] h2: Appendix C Prompt Templates

[139] p: We present the prompt templates used in our framework, including the two-stage prompting strategy for FactGuard and the auditing prompt employed by GPT-4o. FactGuard operates in a structured two-turn manner: the first turn determines whether external evidence is required and selects appropriate tools, while the second turn produces the final verification result conditioned on the gathered evidence. In addition, GPT-4o is used as an external auditor to assess the evidence grounding of the generated reasoning.

[140] h4: FactGuard’s Two-Turn Prompting.

[141] p: As shown in Figure 6 , FactGuard adopts a two-turn prompting strategy to enable explicit evidence-seeking and grounded verification. In the first turn, the model analyzes the input claim and decides whether external tools should be invoked to acquire additional evidence. In the second turn, FactGuard integrates the retrieved evidence with its internal reasoning to produce a final prediction and explanation. This design explicitly separates evidence acquisition from answer generation, reducing reliance on unsupported internal assumptions.

[142] figure: Figure 6 : FactGuard Two-Turn Prompting.

[143] h4: GPT-4o’s Reasoning Audit Prompt.

[144] p: To assess the faithfulness, logical consistency, and evidence grounding of model-generated reasoning, we adopt GPT-4o as an external auditor with a dedicated evaluation prompt. Given the model’s prediction, reasoning trace, and associated evidence, GPT-4o evaluates whether the conclusion is logically coherent, internally consistent, and supported by explicit evidence rather than speculative or internally generated assumptions, as illustrated in Figure 7 . This auditing procedure provides an additional layer of quality control to evaluate theity and interpretinterpretability of reasoningning.

[145] figure: Figure 7 : GPT-4o reasoning audit prompt. The prompt evaluates whether a model’s reasoning and prediction are supported by explicit and relevant evidence, serving as an external assessment of reasoning faithfulness.

[146] h2: Instructions for reporting errors

[147] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[148] p: Tip: You can select the relevant text first, to include it in your report.

[149] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[150] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
