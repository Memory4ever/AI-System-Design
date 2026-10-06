[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: SimpleOCR: Rendering Visualized Questions to Teach MLLMs to Read

[3] h6: Abstract

[4] p: Despite the rapid advancements in Multimodal Large Language Models (MLLMs), a critical question regarding their visual grounding mechanism remains unanswered: do these models genuinely “read” text embedded in images, or do they merely rely on parametric shortcuts in the text prompt? In this work, we diagnose this issue by introducing the Visualized-Question (VQ) setting, where text queries are rendered directly onto images to structurally mandate visual engagement. Our diagnostic experiments on Qwen2.5-VL reveal a startling capability-utilization gap: despite possessing strong OCR capabilities, models suffer a performance degradation of up to 12.7% in the VQ setting, exposing a deep-seated “modality laziness.” To bridge this gap, we propose SimpleOCR, a plug-and-play training strategy that imposes a structural constraint on the learning process. By transforming training samples into the VQ format with randomized styles, SimpleOCR effectively invalidates text-based shortcuts, compelling the model to activate and optimize its visual text extraction pathways. Empirically, SimpleOCR yields robust gains without architectural modifications. On four representative OOD benchmarks, it surpasses the base model by 5.4% and GRPO based on original images by 2.7%, while exhibiting extreme data efficiency, achieving superior performance with 30x fewer samples (8.5K) than recent RL-based methods. Furthermore, its plug-and-play nature allows seamless integration with advanced RL strategies like NoisyRollout to yield complementary improvements. Code is available at https://github.com/aiming-lab/SimpleOCR .

[5] h2: 1 Introduction

[6] p: Multimodal Large Language Models (MLLMs) have achieved remarkable progress in visual reasoning by integrating vision encoders with large language models Liu et al. (2023) ; Bai et al. (2023) ; Bai et al. (2025) ; Hurst et al. (2024) ; Comanici et al. (2025) . Central to this capability is optical character recognition (OCR), i.e., the ability to extract and interpret text embedded in images, which underpins performance on chart understanding Masry et al. (2022) ; Wang et al. (2024c) , document analysis Mathew et al. (2021) ; Han et al. (2025) ; Mathew et al. (2022) , and geometry-centric reasoning Lu et al. (2021) ; Lu et al. (2023) . While current MLLMs achieve strong performance on standalone OCR benchmarks, a fundamental question remains underexplored: do these models actually leverage their OCR capabilities when solving downstream tasks?

[7] p: To investigate this, we introduce a controlled diagnostic intervention called the visualized-question (VQ) format. In standard evaluation, models receive questions via text, which may allow reasoning based on linguistic priors or parametric shortcuts rather than visual evidence. In the VQ setting, we render the question text directly onto the image and provide only a generic instruction (e.g., “ Please answer the question in the image ”), forcing the model to ground its reasoning in visual text. If a model fully utilizes its OCR capabilities, performance under both settings should be comparable. However, our experiments reveal a striking capability–utilization gap .

[8] figure: (a) (b) Figure 1: (a) Visualized-Question (VQ) Format. We render the question text into the image as the only question source, removing text-channel shortcuts and requiring visual reading. (b) Capability–Utilization Gap. On Qwen2.5-VL-7B, performance drops markedly under VQ versus standard inputs, indicating that OCR capability is not reliably utilized during reasoning.

[9] p: As shown in Figure 1 , Qwen2.5-VL-7B suffers substantial degradation under the VQ setting, with an average absolute drop of 6.9% across four multimodal reasoning benchmarks and a maximum drop of 12.7% on WeMath Qiao et al. (2024) . This phenomenon aligns with recent observations of “modality laziness” Lin et al. (2023) ; Fu et al. (2025) ; Yao et al. (2025) , where models systematically underweight visual evidence when informative text prompts are available.

[10] p: Motivated by this diagnosis, we propose SimpleOCR , a training strategy that addresses this gap through structural constraint . Rather than auxiliary losses or architectural modifications Yu et al. (2025a) ; Cao et al. (2025) ; Sarch et al. (2025) , SimpleOCR operates purely through input transformation: all training samples are converted to VQ format with randomized visual styles, eliminating text-based shortcuts entirely. Notably, SimpleOCR introduces zero additional computational overhead or inference latency. By embedding questions directly into the visual space, it forces the model to decode image-based prompts prior to reasoning, thereby drastically improving OCR-based understanding. As a plug-and-play strategy, SimpleOCR can be seamlessly incorporated into any VLM training framework, enhancing model robustness and reasoning by enriching the visual distribution of training data.

[11] p: Empirically, SimpleOCR induces robust performance gains across both in-domain (ID) and out-of-distribution (OOD) scenarios. When trained on Geo3K and MMK12, SimpleOCR achieves a 6.6% improvement over the base model on ID test sets, and achieves 8.5% compared to GRPO based on original images. The generalization capability of our approach is substantiated by results on challenging OOD benchmarks. On MathVerse, MathVision, MathVista, WeMath, and HallusionBench, SimpleOCR surpasses the base model by 5.4% and GRPO based on original images by 2.7%. Notably, SimpleOCR exhibits extreme data efficiency: with only 8.5K training samples, it outperforms RL-based methods Zhang et al. (2025a) ; Yang et al. (2025b) that require over 260K samples, demonstrating a 30x reduction in data dependency. Furthermore, SimpleOCR is a plug-and-play strategy that requires no modifications to the model architecture or training paradigms. It integrates seamlessly with existing VLM training frameworks. For instance, when combined with RL methods like NoisyRollout Liu et al. (2025b) , it yields complementary gains, confirming that SimpleOCR enhances a unique and orthogonal dimension of multi-modal reasoning.

[12] p: Our primary contribution is SimpleOCR, a plug-and-play training strategy designed to bridge the OCR capability–utilization gap. By imposing structural constraints, SimpleOCR forces models to actively engage with visual text, effectively addressing the performance degradation (up to 12.7%) seen when text shortcuts are removed. Empirical results across multiple multimodal reasoning benchmarks demonstrate that our approach significantly enhances out-of-distribution generalization. Furthermore, we verify the effectiveness of our structural components and demonstrate the broad compatibility of SimpleOCR with existing multimodal architectures.

[13] h2: 2 Related Work

[14] h4: Reinforcement Learning for MLLMs.

[15] p: Reinforcement Learning from Verifiable Rewards (RLVR) advances multimodal reasoning by utilizing programmatic signals rather than subjective preferences, extending the RLHF paradigm Ouyang et al. (2022) ; Yu et al. (2024) ; Wang et al. (2025a) ; Tu et al. (2025) ; Xia et al. (2025a) ; Xia et al. (2025b) ; Liu et al. (2025a) ; Su et al. (2025) ; Xia et al. (2026) ; Yang et al. (2025a) . The GRPO algorithm Shao et al. (2024) has powered frontier models like DeepSeek-R1 Guo et al. (2025) , with recent adaptations refining the framework through diverse mechanisms. Specifically, R1-Onevision Yang et al. (2025b) and Vision-R1 Huang et al. (2025) optimize cross-modal formalization and training dynamics, respectively, while R1-VL Zhang et al. (2025a) and VLAA-Thinker Chen et al. (2025) introduce step-wise rewards and mixed perception-cognition signals. To enhance stability, MM-Eureka Meng et al. (2025) and ThinkLite-VL Wang et al. (2025b) employ data-centric strategies such as rejection sampling and MCTS-based selection. Then NoisyRollout Liu et al. (2025b) targets policy diversity by mixing distorted trajectories. However, these methods primarily focus on logical derivation or robustness, lacking explicit constraints to enforce visual text reading against shortcut learning.

[16] h4: Visual Grounding in Text-Rich Contexts.

[17] p: The paradigm for text-rich understanding has shifted from modular OCR pipelines to unified end-to-end architectures Bai et al. (2025) ; Zeng et al. (2025) ; Li et al. (2024a) ; Zhang et al. (2025b) . To circumvent resolution constraints, Monkey Li et al. (2024b) and TextMonkey Liu et al. (2024) introduced patch-division strategies, while VisInContext Wang et al. (2024a) leveraged visual tokens to efficiently scale context length. Subsequently, architectures like GOT Wei et al. (2024) and Donut Blecher et al. (2023) unified perception and reasoning. Current state-of-the-art models, including Qwen2.5-VL Bai et al. (2025) , MiniCPM-V 4.5 Yu et al. (2025b) , and HunyuanOCR Team et al. (2025a) , leverage large-scale OCR corpora Geng et al. (2025) and native-resolution ViTs Dosovitskiy (2020) to handle complex layouts. Despite these advances in capability acquisition , a critical dichotomy remains: models possess strong OCR capabilities but suffer from systematic “modality laziness” Fu et al. (2025) ; Yao et al. (2025) , failing to utilize visual evidence during reasoning. Unlike prior works, our work targets capability utilization , ensuring the model actively grounds its reasoning in visual text evidence.

[18] figure: Figure 2: The SimpleOCR framework. During training, all inputs are transformed into visual question contexts C v ​ q C_{vq} , where question text is rendered onto images. This structurally eliminates text-based shortcuts and forces visual OCR engagement. At inference, models trained this way demonstrate robust performance on standard inputs C o ​ r ​ i ​ g C_{orig} . The method integrates seamlessly as an augmentation branch in existing RL frameworks.

[19] h2: 3 Preliminaries

[20] p: In this section, we will provide a brief overview of MLLMs and GRPO algorithm. We build upon Group Relative Policy Optimization (GRPO) Shao et al. (2024) , a reinforcement learning framework designed to improve the reasoning ability of large language models.

[21] p: Given a multimodal question q q , consisting of an image x img x_{\text{img}} and a text prompt q text q_{\text{text}} , the policy model π θ \pi_{\theta} generates a reasoning response o o . For each question q q , GRPO samples a group of G G candidate responses { o 1 , o 2 , … , o G } \{o_{1},o_{2},\ldots,o_{G}\} from the old policy π θ o ​ l ​ d \pi_{\theta_{old}} . Each response o i o_{i} is assigned a reward r i r_{i} (e.g., from a reward model or rule-based verifier). The group-relative advantage A ^ i \hat{A}_{i} for each response is then computed by:

[22] table: A ^ i = r i − 1 G ​ ∑ j = 1 G r j std ​ ( r 1 , … , r G ) , \hat{A}_{i}=\frac{r_{i}-\frac{1}{G}\sum_{j=1}^{G}r_{j}}{\text{std}(r_{1},\ldots,r_{G})}, (1)

[23] p: which centers and normalizes the rewards within the group, effectively removing question-level biases.

[24] p: The policy model π θ \pi_{\theta} is updated by maximizing the GRPO objective, which incorporates a PPO-style clipped surrogate loss and a KL divergence penalty against a frozen reference model π ref \pi_{\text{ref}} :

[25] table: ℒ GRPO ​ ( θ ) \displaystyle\mathcal{L}_{\text{GRPO}}(\theta) = 𝔼 q ∼ 𝒟 , { o i } ∼ π θ old [ 1 G ∑ i = 1 G ( \displaystyle=\mathbb{E}_{q\sim\mathcal{D},\{o_{i}\}\sim\pi_{\theta_{\text{old}}}}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\bigg( (2) min ⁡ ( r i ​ ( θ ) ​ A ^ i , clip ​ ( r i ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ^ i ) \displaystyle\min\left(r_{i}(\theta)\hat{A}_{i},\text{clip}\left(r_{i}(\theta),1-\epsilon,1+\epsilon\right)\hat{A}_{i}\right) − β D K ​ L ( π θ ∥ π ref ) ) ] , \displaystyle-\beta D_{KL}(\pi_{\theta}\|\pi_{\text{ref}})\bigg)\Bigg],

[26] p: where r i ​ ( θ ) = π θ ​ ( o i | q ) π θ old ​ ( o i | q ) r_{i}(\theta)=\frac{\pi_{\theta}(o_{i}|q)}{\pi_{\theta_{\text{old}}}(o_{i}|q)} denotes the probability ratio. The hyperparameters ϵ \epsilon and β \beta represent the clipping range and the KL divergence penalty weight, respectively. By bypassing the value function and utilizing group-relative advantages, GRPO significantly optimizes memory usage and training efficiency while maintaining robust performance.

[27] h2: 4 SimpleOCR: Addressing the Gap Through Visual Question Training

[28] h3: 4.1 Visual Question Setting

[29] p: Given a training sample S = ( 𝐱 img , q text ) S=(\mathbf{x}_{\text{img}},q_{\text{text}}) , we define two informationally equivalent yet structurally distinct input contexts.

[30] h4: Standard Context C orig C_{\text{orig}} .

[31] p: This context preserves the conventional multimodal schema, C orig = ( 𝐱 img , q text ) C_{\text{orig}}=(\mathbf{x}_{\text{img}},q_{\text{text}}) , where the question is provided via the text channel.

[32] h4: Visual Question Context C vq C_{\text{vq}} .

[33] p: To structurally enforce visual grounding, we introduce a transformation 𝒯 render \mathcal{T}_{\text{render}} that embeds the semantic content of q text q_{\text{text}} directly into the visual modality:

[34] table: C vq = ( 𝒯 render ( 𝐱 img , q text ) , p prompt ) C_{\text{vq}}=\left(\mathcal{T}_{\text{render}}(\mathbf{x}_{\text{img}},q_{\text{text}}),\quad p_{\text{prompt}}\right) (3)

[35] p: where p prompt p_{\text{prompt}} is a generic instruction (e.g., “ Answer the question in the image ”). By removing q text q_{\text{text}} from the text channel, C vq C_{\text{vq}} eliminates the possibility of text-based shortcuts, making visual text reading structurally necessary.

[36] p: As detailed in Algorithm 1 , 𝒯 render \mathcal{T}_{\text{render}} appends the question text to a canvas region below the original image, ensuring all original visual features are preserved. To prevent the model from overfitting to specific layouts, we employ a randomized rendering strategy: parameters such as font family (with CJK support), color, and size (dynamically scaled between 18–42pt) are sampled stochastically during training. This diversity ensures that the learned OCR capabilities are robust to varying visual presentations.

[37] figure: Algorithm 1 Visual Question Rendering ( 𝒯 render \mathcal{T}_{\text{render}} ) 1: # x: original image, q: question text 2: def render(x, q): 3: # Sample random style (language-aware) 4: font, color ← \leftarrow random_style() 5: size ← \leftarrow random.randint(18, 42) 6: 7: # Wrap text and create canvas 8: lines ← \leftarrow wrap(q, width=x.width, size=size) 9: h ← \leftarrow len(lines) × \times line_height(size) 10: canvas ← \leftarrow Image.new((x.width, x.height + h), white) 11: 12: # Paste original image and draw text 13: canvas.paste(x, (0, 0)) 14: draw(canvas, lines, font, size, color, y=x.height) 15: return canvas

[38] figure: Algorithm 2 SimpleOCR Training Strategy 0: Dataset 𝒟 \mathcal{D} , Policy π θ \pi_{\theta} , Reference π θ 0 \pi_{\theta_{0}} , Renderer T render T_{\text{render}} 0: Optimized Policy π θ \pi_{\theta} 1: for each batch ( x img , q text , a ) ∈ 𝒟 (x_{\text{img}},q_{\text{text}},a)\in\mathcal{D} do 2: ⊳ \triangleright 1. Construct Visual Question Context 3: x render ← T render ​ ( x img , q text ) x_{\text{render}}\leftarrow T_{\text{render}}(x_{\text{img}},q_{\text{text}}) 4: C vq ← ( x render , p prompt ) C_{\text{vq}}\leftarrow(x_{\text{render}},p_{\text{prompt}}) 5: ⊳ \triangleright 2. Group Sampling (Visual Exploration) 6: Sample G G outputs from visual context: { s 1 , … , s G } ∼ π θ ( ⋅ | C vq ) \{s_{1},\ldots,s_{G}\}\sim\pi_{\theta}(\cdot|C_{\text{vq}}) 7: ⊳ \triangleright 3. Advantage Computation 8: for k = 1 k=1 to G G do 9: Compute reward r k r_{k} comparing s k s_{k} to ground-truth a a 10: end for 11: A ^ k = r k − mean ​ ( 𝐫 ) orig ​ ( 𝐫 ) + ϵ \hat{A}_{k}=\frac{r_{k}-\text{mean}(\mathbf{r})}{\text{orig}(\mathbf{r})+\epsilon} // Group-relative advantage 12: ⊳ \triangleright 4. Policy Update 13: Compute GRPO loss on C vq C_{\text{vq}} : ℒ = − 1 G ∑ k = 1 G [ A ^ k log π θ ( s k | C vq ) − β 𝔻 KL ] \mathcal{L}=-\frac{1}{G}\sum_{k=1}^{G}\left[\hat{A}_{k}\log\pi_{\theta}(s_{k}|C_{\text{vq}})-\beta\mathbb{D}_{\text{KL}}\right] 14: Update θ \theta using gradient descent 15: end for

[39] h3: 4.2 Training Strategy

[40] p: SimpleOCR trains models exclusively on visual question format. All training samples undergo the 𝒯 render \mathcal{T}_{\text{render}} transformation which is no mixing of standard and visual question formats during training. This design eliminates text channel shortcuts entirely, forcing every training update to engage the visual text reading pathway.

[41] p: Our approach is implemented purely as data preprocessing via 𝒯 render \mathcal{T}_{\text{render}} , requiring no architectural changes and no modification to standard training objectives. For RL training, as illustrated in Alg. 2 , we follow the standard GRPO algorithm while conditioning generation on C vq C_{\text{vq}} : we first construct x render x_{\text{render}} and C vq C_{\text{vq}} , sample a group of G G responses, compute rewards and group-relative advantages, and update the policy using the GRPO objective with the KL regularizer unchanged.

[42] p: Critically, while training uses exclusively C vq C_{\text{vq}} , evaluation employs standard format C orig C_{\text{orig}} . This forces models to develop format-agnostic reasoning capabilities rather than format-specific patterns, learning to extract and process question content regardless of presentation modality.

[43] h3: 4.3 Plug-and-Play Integration

[44] p: Beyond standalone training, SimpleOCR integrates seamlessly into existing training frameworks. We demonstrate this with NoisyRollout Liu et al. (2025b) .

[45] p: NoisyRollout employs a hybrid rollout strategy: for each sample, it generates n 1 n_{1} rollouts from clean images ( 𝐱 img , q text ) (\mathbf{x}_{\text{img}},q_{\text{text}}) and n 2 n_{2} rollouts from perturbed images ( T α ​ ( 𝐱 img ) , q text ) (T_{\alpha}(\mathbf{x}_{\text{img}}),q_{\text{text}}) , where T α T_{\alpha} applies image distortion with strength α \alpha . All rollouts contribute to computing group-relative advantages, improving policy exploration and visual robustness.

[46] p: We integrate SimpleOCR by substituting the perturbation branch with visual question samples. Specifically, we generate n 1 n_{1} rollouts from the standard context C orig C_{\text{orig}} and n 2 n_{2} rollouts from the visual question context C vq C_{\text{vq}} . All rollouts contribute to group-relative advantage computation as in standard NoisyRollout. Policy updates remain conditioned on C orig C_{\text{orig}} following NoisyRollout’s original design. This integration requires no algorithmic modifications, as we simply substitute one augmentation strategy for another. The combination proves effective because the two methods target orthogonal objectives: NoisyRollout enhances visual robustness through image perturbations, while SimpleOCR specifically addresses OCR utilization through visual text reading.

[47] h2: 5 Experiments

[48] h3: 5.1 Experiment Settings

[49] h4: Dataset.

[50] p: We train on Geometry3K Lu et al. (2021) (2.1K instances) and MMK12 Meng et al. (2025) (6.4K instances), totaling 8.5K instances.

[51] h4: Evaluation.

[52] p: We evaluate on two dimensions: (1) in-domain performance on Geometry3K and MMK12 test sets, and (2) out-of-distribution generalization on MathVerse Zhang et al. (2024) , MathVision Wang et al. (2024b) , MathVista Lu et al. (2023) , and HallusionBench Guan et al. (2024) . We additionally evaluate on OCR-intensive benchmarks: InfographicVQA Mathew et al. (2022) (InfoVQA) and ChartQA Masry et al. (2022) . All evaluations utilize greedy decoding, followed by a hybrid judging pipeline combining symbolic verification (Math-Verify 1 1 1 https://github.com/huggingface/Math-Verify ) and LLM-based assessment (GPT-4o Hurst et al. (2024) ). We detail the full protocol in Appendix E .

[53] h3: 5.2 Main Results

[54] figure: In-Domain Out-of-Distribution Method Data Size Geo3K MMK12 Avg. MathVerse MathVision MathVista HallusionBench Avg. Open-source Baselines (SFT / General) InternVL-2.5-8B-Instruct* Chen et al. (2024) - - - - 39.5 19.7 64.4 67.3 47.7 LLaVA-OneVision-7B* Li et al. (2024a) - - - - 26.2 - 63.2 48.4 - Kimi-VL-16B* Team et al. (2025b) - - - - 44.9 21.4 68.7 66.2 50.3 Mulberry-7B* Yao et al. (2024) - - - - - - 63.1 - - Math-LLaVA Shi et al. (2024) 360K - - - 22.9 15.7 46.6 - - RL-Optimized Models (R1-series) R1-VL-7B Zhang et al. (2025a) 260K + 10K 34.3 39.1 36.7 37.5 19.1 61.6 62.8 45.3 R1-OneVision-7B Yang et al. (2025b) 155K + 10K 37.4 47.2 42.3 43.6 20.9 63.1 65.6 48.3 ThinkLite-7B-VL Wang et al. (2025b) 1.1K 38.8 56.8 47.8 46.7 24.2 66.9 66.1 51.0 VLAA-Thinker-7B Chen et al. (2025) 25K 37.6 56.7 47.2 46.9 24.4 67.6 68.1 51.8 MM-Eureka-8B* Meng et al. (2025) 15K - - - 40.4 22.2 67.1 65.3 48.8 Our Methods Qwen2.5-VL-7B-Instruct Bai et al. (2025) - 37.6 53.6 45.6 43.9 23.4 64.2 68.2 49.9 + GRPO 8.5K 44.3 61.9 53.1 46.4 22.5 66.9 68.9 51.2 + SimpleOCR 8.5K 43.4 62.3 52.9 47.7 24.9 68.7 69.1 52.6 Table 1: Performance on mathematical reasoning and visual perception benchmarks. Models marked with “*” are cited from original papers. Bold and underlined numbers indicate the best and second-best performance, respectively. Data sizes for SFT and RL are respectively marked in blue and red .

[55] h4: Robust Transfer via Zero-Shot Generalization.

[56] p: SimpleOCR trains exclusively on VQ inputs but evaluates on standard inputs, creating a severe distributional shift that rigorously tests visual capability. Rather than suffering the expected degradation from format mismatch, SimpleOCR achieves robust zero-shot transfer. As shown in Table 1 , it matches the baseline’s in-domain performance (52.9% vs. 53.1%) while strictly outperforming it on out-of-distribution generalization (52.6% vs. 51.2%). This transfer is most potent on visually demanding tasks like MathVision, where we observe a 10.7% gain. These results prove that the model has not merely memorized the VQ format, but has internalized a fundamental visual text extraction capability that persists even when text shortcuts are restored.

[57] h4: Gains Correlate with Visual-Text Dependency.

[58] p: The performance improvements are structurally non-uniform. MathVision exhibits the most significant boost (24.9% vs. 22.5%), followed by MathVista (68.7% vs. 66.9%) and MathVerse (47.7% vs. 46.4%). Crucially, these benchmarks share a dependency on visual information density: they require extracting critical data or text embedded directly within figures. In contrast, performance slightly regresses on Geometry3K (43.4% vs. 44.3%), a benchmark governed more by abstract geometric logic than by visual text reading. This divergence confirms that SimpleOCR specifically sharpens the visual-text extraction pathway rather than offering a generic reasoning boost. We consider this a strategic trade-off: a marginal dip in pure geometry is exchanged for robust generalization on tasks where visual grounding is paramount.

[59] figure: Figure 3: Performance on OCR-intensive benchmarks. SimpleOCR demonstrates superior performance, achieving 81.6% on ChartQA and 69.1% on HallusionBench.

[60] h4: Superiority on OCR-Intensive Benchmarks.

[61] p: Figure 3 (see Appendix Table 7 ) confirms that SimpleOCR excels on tasks requiring explicit visual text recognition. On ChartQA, while standard GRPO slightly degrades performance (79.8% → \rightarrow 79.5%), SimpleOCR reverses this trend, reaching 81.6%. Consistent improvements are observed on InfographicVQA and HallusionBench, reaching 80.5% and 69.1%, respectively. This establishes a clear hierarchy of efficacy: gains are pronounced on OCR-centric tasks (e.g., ChartQA) and visually grounded math (e.g., MathVision), but negligible on pure geometry (e.g., Geometry3K). This distribution confirms that SimpleOCR functions as a targeted enhancer of visual-text utilization rather than a generic regularizer.

[62] h3: 5.3 Analysis

[63] figure: Table 2: Analysis of Integration & Scalability: SimpleOCR integrates seamlessly with HybridRollout across model scales. The combination yields consistent gains, particularly on the 3B model, validating that SimpleOCR (focused on text reading) and HybridRollout (focused on visual robustness) are orthogonal and complementary. In-Domain Out-of-Distribution Method Configuration Geo3K MMK12 Avg. MathVerse MathVision MathVista Hallusion Avg. Qwen2.5-VL-3B-Instruct 26.0 45.9 36.0 32.5 18.2 50.8 59.1 40.2 + GRPO (baseline) ( n = 6 n=6 ) 35.1 51.2 43.2 36.6 18.5 53.0 58.6 41.7 + SimpleOCR ( n = 6 n=6 ) 36.1 53.6 44.9 40.4 20.1 53.3 61.7 43.9 + HybridRollout ( n 1 = 3 n_{1}=3 , n 2 = 3 n_{2}=3 ) 34.8 53.6 44.2 41.4 20.6 57.3 58.7 44.5 Qwen2.5-VL-7B-Instruct 37.6 53.6 45.6 43.9 23.4 64.2 68.2 49.9 + GRPO (baseline) ( n = 6 n=6 ) 44.3 61.9 53.1 46.4 22.5 66.9 68.9 51.2 + SimpleOCR ( n = 6 n=6 ) 43.4 62.3 52.9 47.7 24.9 68.7 69.1 52.6 + HybridRollout ( n 1 = 3 n_{1}=3 , n 2 = 3 n_{2}=3 ) 41.1 65.0 53.1 47.6 24.9 68.7 68.0 52.3

[64] h4: Plug-and-Play Compatibility.

[65] p: Table 2 demonstrates the compatibility of SimpleOCR with advanced training strategies like NoisyRollout Liu et al. (2025b) . On Qwen2.5-VL-7B, SimpleOCR outperforms the GRPO baseline by 2.7%. This trend is consistent at the 3B scale: SimpleOCR delivers a 5.3% boost in average OOD accuracy, which is further amplified by the inclusion of NoisyRollout. The consistent gains confirm that the methods target distinct reasoning dimensions: SimpleOCR provides semantic grounding, while NoisyRollout improves perceptual robustness. This orthogonality validates SimpleOCR as a flexible plug-and-play augmentation compatible with existing training paradigms.

[66] h4: Consistency Across Model Scales.

[67] p: We further investigate scaling behavior in Table 2 . On Qwen2.5-VL-7B, SimpleOCR delivers a robust 2.7% over the GRPO baseline (52.6% vs. 51.2%), validating its efficacy beyond small-scale models. While the gain margin naturally narrows compared to the 3B model (an expected consequence of performance saturation in larger models), the consistent positive trajectory confirms that “modality laziness” is a fundamental architectural tendency irrespective of capacity. SimpleOCR effectively mitigates this tendency regardless of scale, serving as a scalable corrective mechanism.

[68] h3: 5.4 Ablation Study

[69] h4: Optimization Conflict in Mixed Strategies.

[70] p: To better understand the interaction between standard inputs and VQ training, we evaluated a mixed strategy (Partial Exposure). Figure 4 reveals a distinct U-shaped performance trajectory. On average across four representative OOD benchmarks (detailed in Appendix Table 6 ), the mixed setting (50% VQ) unexpectedly dips below the baseline (49.3% vs. 50.3%), creating a generalization valley. This degradation is particularly pronounced on reasoning-heavy tasks like WeMath ( − 4.4 % -4.4\% ) and MathVista ( − 2.8 % -2.8\% ).

[71] figure: Figure 4: The “U-Shaped” Optimization Conflict. We report the average performance across four representative OOD benchmarks. The mixed strategy (50% VQ) results in a net performance loss, illustrating that contradictory modality signals hinder generalization.

[72] p: We attribute this to a fundamental optimization conflict. When exposed to mixed formats, the model receives contradictory learning signals: standard inputs encourage reliance on the text encoder (the path of least resistance), while VQ inputs demand active visual engagement. Rather than converging on a robust joint strategy, the model oscillates between these modalities, failing to master either. The SimpleOCR (100% VQ) setting resolves this by enforcing a structural constraint. By completely blocking text-based shortcuts, the model is compelled to optimize the visual extraction pathway. Paradoxically, this “forced commitment” yields representations that are modality-agnostic, enabling superior zero-shot transfer (51.3% average accuracy).

[73] figure: Table 3: Ablation on rendering style. Randomization prevents overfitting to specific visual patterns. (Note: “Random style” corresponds to the full SimpleOCR method used in main results.) In-Domain Out-of-Distribution Rendering Strategy Geo3K MMK12 M-Verse M-Vision M-Vista WeMath Fixed style 41.4 61.3 46.9 23.4 65.9 61.6 Random style 43.4 62.3 47.7 24.9 68.7 64.0

[74] h4: Robustness via Randomization.

[75] p: Table 3 validates the efficacy of our randomized rendering strategy. Compared to a static rendering style (e.g., fixed font and color), applying stochastic styles (varying font, size, and color) yields consistent gains, most notably a 2.8 % 2.8\% improvement on MathVista and 2.4 % 2.4\% on WeMath. We attribute the limitations of the fixed setting to feature overfitting . When text always appears with a deterministic visual style, the model tends to memorize low-level texture cues (e.g., specific font patterns) rather than performing generalizable OCR. Randomization disrupts these shortcuts. By diversifying the stylistic presentation, we compel the model to actively decode text regardless of its visual variations. This strategy effectively prevents the model from relying on nuisance variables (such as font type or color), ensuring that the learned grounding capability is genuinely robust.

[76] figure: Figure 5: Left: On MathVista, the GRPO baseline is misled by hallucinated semantic priors, while SimpleOCR correctly identifies material properties. Right: On ChartQA, the baseline relies on superficial keyword spotting, whereas SimpleOCR performs holistic visual analysis. Blue : correct grounding; red : heuristic errors.

[77] h4: Sensitivity to Group Sampling Size.

[78] figure: Table 4: Impact of Group Sampling Size n n . We analyze the effect of the number of generations per prompt during GRPO training. In-Domain Out-of-Distribution Configuration Geo3K MMK12 Avg. M-Verse M-Vision M-Vista WeMath Hallusion Avg. n = 3 n=3 40.4 62.5 51.5 46.2 24.0 67.5 60.5 70.4 53.7 n = 6 n=6 43.4 62.3 52.9 47.7 24.9 68.7 64.0 69.1 54.9 n = 9 n=9 41.4 63.0 52.2 47.4 24.6 66.4 61.6 67.9 53.6

[79] p: We investigate the impact of the group size n n (the number of rollouts generated per prompt) on SimpleOCR training dynamics in Table 4 , employing the 7B model as the backbone. Standard RL scaling laws typically suggest that larger group sizes improve gradient estimation. However, our results reveal an inverted U-shaped trend. Increasing the group size from n = 3 n=3 to n = 6 n=6 yields a robust 2.2% gain in average OOD performance, confirming that sufficient exploration is critical for learning complex visual grounding. Crucially, further scaling to n = 9 n=9 does not yield additional benefits; instead, performance suffers a slight 2.4% regression. We hypothesize that in the context of VQ training, excessively large groups may introduce “reward hacking” on noisy visual samples or optimization instability. Consequently, we adopt n = 6 n=6 as the optimal trade-off between computational efficiency and reasoning performance.

[80] h3: 5.5 Qualitative Analysis

[81] p: Figure 5 illustrates the behavioral shift. In visual reasoning (MathVista), the baseline GRPO model succumbs to semantic priming, associating the text “blue” with a prominent sphere despite conflicting visual evidence (metallic luster), whereas SimpleOCR discriminates texture correctly. Similarly, on ChartQA, the baseline relies on superficial keyword spotting, matching “52” without comprehending the structural condition “largest value”, while SimpleOCR successfully parses the chart topology. These cases validate that the capability-utilization gap is not a deficit of perception but of execution preference. Standard models default to spurious text shortcuts, but SimpleOCR structurally blocks this path, compelling the model to engage in grounded visual reasoning.

[82] h2: 6 Conclusion

[83] p: In this paper, we identified and quantified the “modality laziness” in MLLMs, where models bypass visual evidence in favor of text-based shortcuts. Our diagnostic VQ setting revealed a significant capability-utilization gap, which we addressed through SimpleOCR. By structurally enforcing visual engagement via randomized text rendering, SimpleOCR effectively transforms the model’s reliance from parametric priors to grounded visual perception. Empirically, SimpleOCR delivers consistent improvements across both in-domain and out-of-distribution benchmarks. Notably, it achieves these gains with extreme data efficiency (using 30 × \times less data than comparable RL methods) and seamless plug-and-play compatibility with existing frameworks.

[84] h2: Acknowledgments

[85] p: This work was partially supported by the Amazon Research Award, the Cisco Faculty Research Award.

[86] h2: Limitations

[87] p: While SimpleOCR effectively bridges the capability-utilization gap, we identify two primary limitations. First, our method operates as an elicitation strategy rather than a fundamental capability builder. It relies on the base MLLM having latent OCR capabilities (i.e., a strong vision encoder) to recognize the rendered text. Second, our approach is bounded by visual resolution constraints when handling extremely long queries. Unlike text encoders that scale efficiently to long contexts, rendering extensive text prompts (e.g., multi-paragraph instructions) onto a single image is limited by the vision encoder’s input resolution.

[88] p: Potential Risks. Enhanced visual text extraction could theoretically be leveraged to bypass visual security measures (e.g., CAPTCHA solvers) or to automate the extraction of sensitive personal information from natural images (e.g., reading documents or screens in the background of photos). However, our method functions as an activation strategy for existing base models rather than introducing new, specialized attack capabilities. The risks are inherently bound by the safety alignment and capabilities of the underlying foundation models.

[89] h2: References

[90] h2: Appendix A Dataset Details

[91] h3: A.1 Training Data

[92] p: Our training set consists of two high-quality mathematical reasoning datasets, totaling 8.5K instances. Detailed statistics are provided in Table 5 .

[93] figure: Table 5: Training Data Statistics. We combine geometry-focused and general K-12 math datasets to construct a diverse training corpus. Dataset Source Domain Size Geometry3K ( Lu et al., 2021 ) Plane Geometry 2,100 MMK12 ( Meng et al., 2025 ) K-12 Mathematics 6,400 Total - Mixed 8,500

[94] p: Geometry3K ( Lu et al., 2021 ) . A high-quality geometry problem-solving dataset containing formal geometric diagrams and corresponding problem descriptions. We utilize the training split (2.1K samples) to enhance the model’s spatial reasoning and geometric calculation capabilities.

[95] p: MMK12 ( Meng et al., 2025 ) . A comprehensive multimodal dataset derived from K-12 mathematics curriculum. It covers a wide range of topics including algebra, arithmetic, and function analysis. The subset used (6.4K samples) provides diverse visual-text reasoning scenarios essential for general mathematical grounding.

[96] h3: A.2 Evaluation Benchmarks

[97] p: To rigorously assess generalization capabilities, we evaluate on five mathematical reasoning benchmarks and two OCR-intensive tasks.

[98] h4: Mathematical Reasoning.

[99] p: MathVista ( Lu et al., 2023 ) . A comprehensive benchmark integrating diverse mathematical reasoning tasks. It serves as a primary gauge for general multimodal mathematical capability.

[100] p: MathVision ( Wang et al., 2024b ) . A large-scale benchmark designed to evaluate MLLMs across diverse mathematical domains and complex visual contexts.

[101] p: MathVerse ( Zhang et al., 2024 ) . A dataset specifically curated to diagnose whether MLLMs truly interpret visual diagrams or rely on text shortcuts. This aligns perfectly with our study’s motivation to detect “modality laziness”.

[102] p: WeMath ( Qiao et al., 2024 ) . A benchmark focusing on human-like reasoning processes in complex mathematical problems, testing the depth of the model’s logical derivation.

[103] p: HallusionBench ( Guan et al., 2024 ) . An advanced diagnostic suite for detecting visual hallucinations and illusions. We use it to verify faithful visual grounding and resistance to perceptual interference.

[104] h4: OCR-Intensive Tasks.

[105] p: To verify the transfer of visual text reading skills, we include two specific benchmarks:

[106] p: ChartQA ( Masry et al., 2022 ) . A dataset requiring reasoning over charts with data labels, titles, and legends, serving as a direct test of the model’s ability to extract and integrate fine-grained visual text.

[107] p: InfographicVQA ( Mathew et al., 2022 ) . A benchmark challenging models to understand complex document layouts and infographics with high-density text.

[108] h2: Appendix B System Prompts

[109] p: We utilize the standard system prompt from the verl framework to elicit structured reasoning (Chain-of-Thought) and formatted answers.

[110] h3: B.1 Evaluated Models

[111] p: We include a comprehensive set of state-of-the-art multimodal models in our evaluation, categorized into general-purpose open-source baselines and recent RL-optimized models.

[112] h4: Open-Source Baselines.

[113] p: Qwen2.5-VL-3/7B-Instruct ( Bai et al., 2025 ) . The latest iteration of the Qwen-VL series, featuring state-of-the-art OCR and visual understanding capabilities trained on massive-scale datasets. We utilize these as our primary base models to demonstrate the effectiveness of SimpleOCR.

[114] p: InternVL-2.5-8B-Instruct ( Chen et al., 2024 ) . A powerful MLLM that expands performance boundaries through model and test-time scaling, known for its strong general-purpose visual perception.

[115] p: LLaVA-OneVision-7B ( Li et al., 2024a ) . A model designed for easy visual task transfer, utilizing a unified architecture to handle diverse vision-language scenarios efficiently.

[116] p: Kimi-VL-16B ( Team et al., 2025b ) . A large-scale open-weights model utilizing a Mixture-of-Experts (MoE) architecture, demonstrating competitive performance on chart and document understanding benchmarks.

[117] p: Mulberry-7B ( Yao et al., 2024 ) . An MLLM empowered with OpenAI-o1-like reasoning capabilities via collective Monte Carlo Tree Search (MCTS), focusing on enhanced logical deduction.

[118] h4: RL-Optimized & R1-Series Models.

[119] p: Math-LLaVA. ( Shi et al., 2024 ) A specialized model bootstrapped for mathematical reasoning, serving as a strong baseline for SFT-based mathematical capability.

[120] p: R1-VL-7B. ( Zhang et al., 2025a ) A pioneering model trained via step-wise Group Relative Policy Optimization (GRPO), explicitly rewarding intermediate reasoning steps to improve logical consistency.

[121] p: R1-OneVision-7B. ( Yang et al., 2025b ) An extension of the R1 series that advances generalized multimodal reasoning through cross-modal formalization techniques.

[122] p: ThinkLite-7B-VL. ( Wang et al., 2025b ) A data-efficient model achieving state-of-the-art performance with fewer samples, utilizing MCTS-guided sample selection for self-improvement.

[123] p: VLAA-Thinker-7B. ( Chen et al., 2025 ) A model investigating the trade-offs between SFT and RL in R1-like reasoning, providing insights into training recipes for reasoning-heavy MLLMs.

[124] p: MM-Eureka-8B. ( Meng et al., 2025 ) A model exploring the frontiers of multimodal reasoning using rule-based reinforcement learning, emphasizing verified feedback signals.

[125] h2: Appendix C Detailed Ablation Results

[126] p: In Section 5.4, we discussed the optimization conflict observed in mixed training strategies. Table 6 provides the detailed performance breakdown across four representative out-of-distribution benchmarks.

[127] p: As shown, the mixed strategy (50% VQ) fails to improve over the baseline in most reasoning-intensive tasks (e.g., WeMath, MathVista), confirming that the conflicting modality signals hinder model convergence. In contrast, the pure SimpleOCR strategy (100% VQ) achieves the best average performance across the board.

[128] figure: Table 6: Impact of VQ Training Ratio (Detailed Breakdown). We report the performance on four reasoning-heavy OOD benchmarks. The mixed strategy (50% VQ) consistently underperforms or stagnates compared to the baseline (Avg. 49.3 vs 50.3), supporting the hypothesis of optimization conflict. Only the full VQ strategy (SimpleOCR) achieves robust generalization gains (Avg. 51.3). VQ Ratio MathVerse MathVision MathVista WeMath Avg. Standard (0% VQ) 46.4 22.5 66.9 65.3 50.3 Mixed (25% VQ) 47.8 22.9 67.2 62.8 50.2 Mixed (50% VQ) 46.2 23.7 65.0 62.4 49.3 Mixed (75% VQ) 48.0 23.9 65.7 62.2 50.0 SimpleOCR (100% VQ) 47.7 24.9 68.7 64.0 51.3

[129] h2: Appendix D OCR-Intensive Benchmarks

[130] p: We provide the exact numerical breakdown for OCR-intensive tasks in Table 7 . A key observation is that standard GRPO can lead to negative transfer on fine-grained visual tasks like ChartQA (dropping from 79.8% to 79.5%), likely due to the model overfitting to textual reasoning shortcuts. In contrast, SimpleOCR consistently yields improvements across all metrics (81.6% on ChartQA), confirming its effectiveness in preserving and enhancing visual grounding capabilities without compromising general reasoning.

[131] figure: Table 7: Performance on OCR-Intensive Benchmarks. Exact numbers corresponding to Figure 3 . Method ChartQA HallusionBench InfoVQA Base Model 79.8 68.2 79.7 GRPO (Original images) 79.5 68.9 80.1 GRPO + SimpleOCR 81.6 69.1 80.5

[132] h2: Appendix E Evaluation Protocol Details

[133] h4: Inference and Extraction.

[134] p: For all experiments, we perform inference using greedy decoding ( temperature=0 ) to ensure reproducibility. To isolate the final answer from the Chain-of-Thought (CoT) rationale, we employ a rule-based extraction parser. Specifically, we extract the content within the last occurrence of the \boxed{…} delimiter in the model output. If no such delimiter is found, the raw output is passed to the subsequent evaluation stages.

[135] h4: Hierarchical Judging Pipeline.

[136] p: We implement a two-stage cascaded evaluation strategy to balance strict symbolic correctness with semantic flexibility:

[137] p: Stage 1: Symbolic Verification (Math-Verify). We first employ the math-verify library for symbolic equivalence checks. This tool parses mathematical expressions into canonical forms (e.g., standardizing fractions, square roots, and units) to determine correctness. If math-verify returns a positive match, the sample is marked as correct immediately.

[138] p: Stage 2: LLM-based Fallback Judge. For samples where symbolic verification fails or is inconclusive (e.g., complex textual reasoning or format mismatches), we employ gpt-4o-2024-08-06 as a fallback evaluator. We construct a meta-evaluation prompt containing the question, the ground truth, and the student’s answer. The LLM is strictly instructed to:

[139] p: Ignore superficial formatting differences (e.g., Markdown styling).

[140] p: Check for mathematical equivalence rather than string matching.

[141] p: Allow a relative numerical tolerance of ± 1 % \pm 1\% (unless specified otherwise).

[142] p: For multiple-choice questions, verify that the selected option letter matches the ground truth.

[143] p: The LLM outputs a binary score (0 or 1) based on these criteria.

[144] h4: Benchmark-Specific Protocols.

[145] p: HallusionBench: We strictly adhere to the official evaluation protocol, utilizing its dataset-specific LLM judge to handle the unique “uncertain” label requirements.

[146] p: Geometry3K: Due to the strict formatting of this dataset, we rely primarily on symbolic verification, enforcing exact matches for geometric values and units.

[147] h2: Appendix F Supplementary Implementation Details

[148] p: We provide the detailed hyperparameter configurations used in our experiments in Table 8 .

[149] figure: Table 8: Summary of hyperparameter configurations. Parameter Configuration Model Base Qwen2.5-VL-Instruct Vision Encoder Frozen Global Batch Size 128 Rollout Batch Size 512 Rollout Temperature 1.0 Learning Rate 1 × 10 − 6 1\times 10^{-6} Optimizer AdamW Total Training Steps 200 CPU Memory 512GB GPU RTX 6000 Pro Blackwell

[150] h2: Instructions for reporting errors

[151] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[152] p: Tip: You can select the relevant text first, to include it in your report.

[153] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[154] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
