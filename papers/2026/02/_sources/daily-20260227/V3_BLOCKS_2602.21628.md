[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning

[3] h6: Abstract

[4] p: Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a prevailing paradigm for enhancing reasoning in Multimodal Large Language Models (MLLMs). However, relying solely on outcome supervision risks reward hacking, where models learn spurious reasoning patterns to satisfy final answer checks. While recent rubric-based approaches offer fine-grained supervision signals, they suffer from high computational costs of instance-level generation and inefficient training dynamics caused by treating all rubrics as equally learnable. In this paper, we propose Stratified Rubric-based Curriculum Learning (RuCL) , a novel framework that reformulates curriculum learning by shifting the focus from data selection to reward design. RuCL generates generalized rubrics for broad applicability and stratifies them based on the model’s competence. By dynamically adjusting rubric weights during training, RuCL guides the model from mastering foundational perception to tackling advanced logical reasoning. Extensive experiments on various visual reasoning benchmarks show that RuCL yields a remarkable +7.83% average improvement over the Qwen2.5-VL-7B model, achieving a state-of-the-art accuracy of 60.06% .

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in complex visual reasoning tasks, spanning from mathematical problem-solving to chart understanding ( Yao et al., 2024 ; Liu et al., 2025b ; Peng et al., 2025 ; Amizadeh et al., 2020 ; Garcez et al., 2019 ) . To further augment these reasoning capabilities, Reinforcement Learning with Verifiable Rewards (RLVR) ( Shao et al., 2024 ; Cui et al., 2025 ; Li et al., 2025 ) has emerged as a prevalent post-training paradigm. By employing straightforward rule-based verification, RLVR avoids the reliance on costly reward models ( Meng et al., 2025 ; Liu et al., 2025a ; Xu et al., 2025b ) .

[8] p: However, this outcome-based reward mechanism suffers from a fundamental limitation: it overemphasizes final answer correctness at the expense of intermediate reasoning quality. As a result, models are prone to learning spurious reasoning patterns or exploiting superficial shortcuts. This frequently leads to the generation of contradictory or hallucinatory intermediate steps that serendipitously arrive at correct answers. Such “reward hacking” phenomenon severely compromises the reliability of the reasoning.

[9] figure: Figure 1 : Comparison of reward paradigms. We move beyond (A) outcome-only signals and (B) unstructured dense feedback. (C) Our RuCL framework organizes rubrics into a stratified curriculum, aligning reward complexity with the model’s progressive learning stages.

[10] p: While recent LLM-as-a-Judge frameworks successfully mitigate reward hacking by constructing rubrics to assess the validity of reasoning trajectories ( Viswanathan et al., 2025 ; Gunjal et al., 2025 ) , they are hampered by two fundamental limitations ( Huang et al., 2025b ; Zhou et al., 2025 ; Pathak et al., 2025 ) . First, generating rubrics at the instance level incurs high computational overhead, especially during online reinforcement learning setting. Second, and more importantly, existing methods treat all rubrics equally challenging throughout the training process, lacking a principled mechanism to account for heterogeneous learnability across evaluation rubrics. Consequently, models are penalized for complex logical failures before mastering basic skills such as visual perception, resulting in noisy gradient signals and hindering efficient convergence.

[11] p: Drawing inspiration from Curriculum Learning (CL) ( Bengio et al., 2009 ; Parashar et al., 2025 ) , which traditionally organizes training data from easy to hard, we propose Stratified Rubric-based Curriculum Learning (RuCL) , a novel framework that applies curriculum learning directly to reward design rather than data selection. Instead of treating all rubrics uniformly throughout training, our key insight is to organize and schedule rubrics according to their learnability, enabling the model to acquire reasoning skills in a structured and progressive manner (Fig. 1 ).

[12] p: RuCL can be explained as a two-phase process: (1) Generalized Rubric Construction and Stratification : We adopt a data-driven approach to generate generalized rubrics that capture essential reasoning primitives shared across tasks, rather than relying on costly instance-specific evaluation. We estimate the model’s initial competence on each rubric and stratify them by empirical proficiency level, ranging from foundational skills to advanced reasoning abilities. (2) Dynamic Curriculum Learning : During training, RuCL dynamically adjusts the weights of these rubrics based on the model’s evolving capabilities. Training initially prioritizes foundational rubrics (e.g., visual element recognition). As the model demonstrates competence, the framework automatically shifts focus towards hard rubrics (e.g., complex logical deduction), effectively guiding the model from basic perception to advanced reasoning. Finally, the combination of final answer reward and rubric-based reward jointly promotes the model’s reasoning capabilities.

[13] p: Our contributions are summarized as follows:

[14] p: We introduce RuCL, a reward-centric curriculum framework that dynamically aligns rubric difficulty with model competence.

[15] p: We instantiate RuCL with a data-driven rubric construction pipeline, an applicability-aware evaluation mechanism, and a performance-triggered curriculum scheduler, yielding a practical and scalable reward design for rubric-based approaches.

[16] p: We conduct extensive experiments across seven benchmarks, showing that RuCL achieves an average performance gain of 7.83% , and provide detailed ablation studies validating its effectiveness.

[17] h2: 2 Related Work

[18] p: Post-training for MLLMs. Early MLLM reasoning methods, such as LLaVA-Reasoner ( Zhang et al., 2025 ) , MPO ( Wang et al., 2024b ) , and Insight-V ( Rafailov et al., 2023 ) , rely on rationale distillation, human preferences, or iterative DPO, but are limited by heavy supervision and low scalability. To address this, Reinforcement Learning with Verifiable Rewards (RLVR) ( Ma et al., 2025 ; Chu et al., 2025 ) verifies final answers against ground truth, enabling scalable reasoning improvement. For example, Vision-R1 ( Huang et al., 2025a ) leverages teacher MLLMs to generate chain-of-thought (CoT) data, DeepScaler ( Luo et al., 2025 ) and Light-R1 ( Wen et al., 2025 ) combine supervised and RL training, and VL-Rethinker ( Wang et al., 2025a ) , SRPO ( Wan et al., 2025 ) , and GThinker ( Zhan et al., 2025 ) use reflection-aware rewards. Despite these advances, sparse outcome-based rewards leave models prone to reward hacking via spurious reasoning.

[19] p: Rubrics as Rewards. To address the opacity and sparsity of outcome-based supervision, recent work uses structured rubrics to evaluate intermediate reasoning processes, decomposing tasks into explicit, verifiable criteria. Rubrics have proven effective in domains such as medical reasoning ( Arora et al., 2025 ) , code generation ( Mahdaoui et al., 2025 ) , and instruction following ( Pathak et al., 2025 ; Galvan-Sosa et al., 2025 ; Fan et al., 2024 ; Winata et al., 2025 ) . LLM-as-a-Judge frameworks ( Team et al., 2025a ; Viswanathan et al., 2025 ) integrate rubrics into reinforcement learning, providing more informative reward signals than standard RLVR ( Huang et al., 2025b ; Gunjal et al., 2025 ) . However, existing approaches typically generate instance-specific rubrics and treat all rubrics as equally learnable, lacking a principled mechanism to account for heterogeneous difficulty across reasoning skills.

[20] p: Curriculum Learning. Curriculum Learning (CL), introduced by ( Bengio et al., 2009 ) , organizes training into phases to mimic human learning and enable progressive skill acquisition ( Parashar et al., 2025 ; Shi et al., 2025 ; Chen et al., 2025 ; Song et al., 2025 ) . Kwai Keye-VL ( Team et al., 2025b ) improves capability and stability by adopting a multi-stage training recipe that structures both pre-training and post-training, while VL-Contigo ( Yuan et al., 2025 ) implements an “easy-to-hard” RL curriculum with online difficulty weighting across three stages. These prior approaches focus on data-level curricula; in contrast, we apply CL at the rubrics level, dynamically adjusting rubric weights during RL to balance training stability and reasoning performance.

[21] figure: Figure 2 : Overview of Stratified Rubric-based Curriculum Learning (RuCL). The framework proceeds in two stages: (Top) Generalized Rubric Construction and Stratification , where evaluation rubrics are generated and categorized into Foundational ( ℛ easy \mathcal{R}_{\text{easy}} ) and Advanced ( ℛ hard \mathcal{R}_{\text{hard}} ) tiers based on empirical difficulty. (Bottom) Dynamic Curriculum Learning , where the rubric-based reward is synthesized via a dynamic weighting mechanism controlled by a scheduler. By adjusting the weight λ \lambda based on real-time performance, RuCL progressively shifts the optimization focus from mastering basic skills to tackling complex reasoning.

[22] h2: 3 Stratified Rubric-based Curriculum Learning (RuCL)

[23] p: In this work, we focus on rubric-based rewards to improve

[24] p: the reasoning capabilities of Multimodal Large Language Models (MLLMs). While rubrics provide fine-grained supervision over reasoning processes, existing methods typically combine them with fixed weights, ignoring differences in difficulty and learnability. This results in noisy gradients and inefficient optimization. We propose Stratified Rubric-based Curriculum Learning (RuCL) , which applies curriculum learning directly to reward design by progressively emphasizing rubrics of increasing difficulty. In this section, we first formalize the learning objective, then detail rubric construction and the curriculum mechanism.

[25] figure: Table 1 : The stratified reward system. The evaluation rubrics are categorized by difficulty and implemented via either a generative LLM Judge or a deterministic Answer Verifier. Detailed rubric definitions and scoring criteria are provided in Appendix D . Rubric Criterion Evaluation Focus Difficulty Stratum Evaluator Visual Presence Penalizes object and attribute hallucinations. Foundational ( ℛ easy \mathcal{R}_{\text{easy}} ) LLM Judge Entity Extraction Isolates the specific Region of Interest (ROI). Intent Alignment Checks compliance with scope and constraints. Conclusion Match Ensures the answer logically follows the reasoning. Step Coherence Detects logical gaps and internal contradictions. Advanced ( ℛ hard \mathcal{R}_{\text{hard}} ) Evidence Grounding Validates inferences using specific visual cues. Answer Correctness Verifies the final answer against the ground truth. — Answer Verifier

[26] h3: 3.1 Problem Formulation

[27] p: We consider a Reinforcement Learning (RL) setting. Given an input query x x (e.g., an image-text pair), a policy π θ ​ ( y ∣ x ) \pi_{\theta}(y\mid x) generates a response y y . The learning signal is provided by a scalar reward function r ( t ) ​ ( y ∣ x ) r^{(t)}(y\mid x) , which may vary over the training step t t to reflect the dynamic curriculum scheduling of supervision signals. This reward integrates multiple sources of supervision, including (i) rule-based verification of final answer correctness, and (ii) rubric-based evaluations that assess intermediate reasoning qualities such as perception, grounding, and logical consistency. These rubric signals are derived from a set of evaluation rubrics ℛ = { R 1 , … , R k } \mathcal{R}=\{R_{1},\dots,R_{k}\} , each targeting a distinct reasoning aspect. Our objective is to learn a policy π θ \pi_{\theta} that maximizes the expected reward:

[28] table: max θ 𝔼 x ∼ 𝒟 , y ∼ π θ ( ⋅ ∣ x ) [ r ( t ) ( y ∣ x ) ] . \max_{\theta}\;\mathbb{E}_{x\sim\mathcal{D},\,y\sim\pi_{\theta}(\cdot\mid x)}\left[r^{(t)}(y\mid x)\right]. (1)

[29] p: We optimize this objective using Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) , a stable policy-gradient method for RLVR (see Appendix A for details). The core challenge is to design r ( t ) r^{(t)} such that it provides adaptive supervision across reasoning skills that differ substantially in difficulty and learnability.

[30] p: Rubric Rewards as Multi-Objective Optimization. Rubric-based supervision can be viewed as optimizing multiple skill-wise objectives under a shared policy. Specifically, each rubric R k ∈ ℛ R_{k}\in\mathcal{R} induces a sub-reward r k ​ ( y ∣ x ) r_{k}(y\mid x) , and the overall rubric reward corresponds to a weighted combination:

[31] table: r rub ( t ) ​ ( y ∣ x ) = ∑ k = 1 K ω k ( t ) ​ r k ​ ( y ∣ x ) , s.t. ​ ∑ ω k ( t ) = 1 . r_{\text{rub}}^{(t)}(y\mid x)=\sum_{k=1}^{K}\omega_{k}^{(t)}\,r_{k}(y\mid x),\quad\text{s.t.}\sum\omega_{k}^{(t)}=1. (2)

[32] p: A key challenge in this formulation is the heterogeneity of the objectives. The rubrics range from basic checks to complex reasoning steps, implying that their corresponding reward signals vary significantly in density and reliability. Indiscriminately mixing these diverse signals with static weights risks letting noisy, high-difficulty objectives dominate or interfere with the learning of foundational skills. Therefore, a time-varying weighting scheme ω ( t ) \omega^{(t)} naturally serves as a curriculum over reward components, allowing optimization to prioritize learnable, low-noise objectives first and progressively incorporate harder reasoning criteria.

[33] p: In the following sections, we detail how r ( t ) r^{(t)} is instantiated via data-driven rubric construction and difficulty stratification (Sec. 3.2 ), and a performance-triggered curriculum scheduling mechanism (Sec. 3.3 ). The overview of RuCL is illustrated in Fig. 2 .

[34] h3: 3.2 Phase I: Generalized Rubric Construction and Stratification

[35] p: To construct a robust and discriminative reward system, we design a quantitative, data-driven pipeline that filters and stratifies rubrics based on their empirical behavior. In contrast to existing rubric-based methods that generate ad hoc, instance-specific rubrics ( Zhou et al., 2025 ; Gunjal et al., 2025 ) , we construct a reusable set of generalized rubrics that remain applicable across diverse reasoning tasks, enabling principled difficulty stratification and curriculum scheduling.

[36] p: Computational Efficiency Analysis. We theoretically differentiate the computational overhead of RuCL from instance-specific methods ( Jia et al., 2025 ; Zhou et al., 2025 ; Gunjal et al., 2025 ) . While both paradigms incur a comparable online evaluation cost proportional to the number of training steps , the critical efficiency gap lies in the rubric generation phase. Let N N denote the total number of unique training queries and C g ​ e ​ n C_{gen} be the unit costs for generating a rubric set. Instance-level approaches must synthesize tailored rubrics for every unique input, scaling linearly with the dataset size ( 𝒪 ⁡ ( N × C g ​ e ​ n ) \mathcal{O}(N\times C_{gen}) ). In contrast, RuCL generates a generalized rubric pool shared across all data, reducing the generation overhead to a constant 𝒪 ⁡ ( 1 × C g ​ e ​ n ) \mathcal{O}(1\times C_{gen}) . By eliminating the repetitive LLM calls for per-instance rubric creation, RuCL significantly reduces the pre-computation burden without compromising the evaluation density.

[37] p: Candidate Generation & Rollout. We prompt a teacher LLM with comprehensive context, including the task category, relevant images, the input query, and the ground truth answer, and instruct it to generate a diverse set of the most relevant rubric candidates ( ℛ candidates \mathcal{R}_{\text{candidates}} ). We then perform rollouts on a randomly sampled subset of training instances ( 𝒟 sample \mathcal{D}_{\text{sample}} ) of size N N using the base model to collect rubric-level evaluation signals.

[38] p: Applicability-Aware Evaluation. Unlike standard scalar scoring, we design a specialized Judge mechanism that explicitly decouples relevance from performance . For each sample x i ∈ 𝒟 sample x_{i}\in\mathcal{D}_{\text{sample}} and rubric candidate R j R_{j} , the Judge outputs a tuple ( a i ​ j , s i ​ j ) (a_{ij},s_{ij}) , where a i ​ j ∈ { 0 , 1 } a_{ij}\in\{0,1\} indicates whether rubric R j R_{j} is applicable to the problem context of x i x_{i} , and s i ​ j ∈ { 0 , 1 } s_{ij}\in\{0,1\} denotes whether the model output satisfies the rubric, evaluated only when a i ​ j = 1 a_{ij}=1 .

[39] p: This explicit decoupling ensures that the computed statistics accurately reflect the rubric’s effective coverage and the model’s actual proficiency. By preventing non-applicable rubrics from skewing the metrics, this mechanism provides a reliable basis for selecting high-coverage rubrics and stratifying them by difficulty. The detailed evaluation prompt is provided in Appendix E .

[40] p: Metric-Based Filtering and Stratification. Using the assessment statistics, we refine the candidate pool to construct a structured curriculum. We first compute the Applicability Rate ( η j \eta_{j} ) to quantify each rubric’s coverage across the dataset: η j = 1 N ​ ∑ i = 1 N a i ​ j \eta_{j}=\frac{1}{N}\sum_{i=1}^{N}a_{ij} . To ensure broad coverage and reduce noise from rarely applicable rubrics, we discard rubrics with insufficient coverage ( η j < τ app \eta_{j}<\tau_{\text{app}} ). We provide detailed statistics in Appendix D.2 illustrating the high variance in rubric coverage (e.g., as low as 9.7%), which empirically justifies the necessity of this filtering mechanism to avoid catastrophic gradient noise. For the remaining rubrics ( ℛ filtered ⊆ ℛ candidates \mathcal{R}_{\text{filtered}}\subseteq\mathcal{R}_{\text{candidates}} ), we compute the Pass Rate ( p j p_{j} ) , defined as the current model’s conditional success rate on applicable instances: p j = ∑ i = 1 N ( a i ​ j ⋅ s i ​ j ) ∑ i = 1 N a i ​ j p_{j}=\frac{\sum_{i=1}^{N}(a_{ij}\cdot s_{ij})}{\sum_{i=1}^{N}a_{ij}} . This metric serves as an empirical proxy for difficulty, allowing us to stratify rubrics based on their role in the learning process. We partition them into two distinct levels (see Table 1 ): a) Foundational Rubrics ( ℛ easy \mathcal{R}_{\text{easy}} ) , characterized by high pass rates, target prerequisite skills to provide stable initial supervision signals; b) Advanced Rubrics ( ℛ hard \mathcal{R}_{\text{hard}} ) , identified by low pass rates, target complex reasoning gaps that remain underdeveloped in the base model. This separation enables a curriculum that reinforces basics first, then progressively pivots to challenging reasoning tasks.

[41] p: Statistical Interpretation of Pass Rate as Difficulty Proxy. We justify using the pass rate as a principled indicator of optimization difficulty through the lens of gradient estimator stability. For a fixed rubric R j R_{j} , we model its signal as a Bernoulli variable r j ∼ Bernoulli ​ ( p j ) r_{j}\sim\text{Bernoulli}(p_{j}) . In policy gradient methods, the reliability of the update is inversely related to the Coefficient of Variation (CV) of the estimator:

[42] table: C ​ V ​ ( r j ) = V ​ a ​ r ​ ( r j ) 𝔼 ⁡ [ r j ] = p j ​ ( 1 − p j ) p j = 1 p j − 1 . CV(r_{j})=\frac{\sqrt{Var(r_{j})}}{\mathbb{E}[r_{j}]}=\frac{\sqrt{p_{j}(1-p_{j})}}{p_{j}}=\sqrt{\frac{1}{p_{j}}-1}. (3)

[43] p: This derivation reveals a critical insight: as the pass rate p j → 0 p_{j}\to 0 , the relative noise diverges ( C ​ V → ∞ CV\to\infty ). This implies that rubrics with low pass rates (Advanced Rubrics) provide gradient signals that are dominated by noise, leading to inefficient credit assignment. Conversely, high-pass-rate rubrics (Foundational Rubrics) offer low-CV, reliable signals. Thus, stratifying rubrics by pass rate is statistically equivalent to stratifying by gradient reliability.

[44] figure: Table 2 : Performance comparison on Mathematical Reasoning and General benchmarks. The “Avg.” column reports the average score across all seven evaluated benchmarks. The best results among open-source reasoning models are highlighted in bold , while the second-best are underlined . Model Mathematical Reasoning General Avg. MathVerse MathVision MathVista WeMATH MMMU LogicVista Counting Proprietary Models GPT-4o 50.20 30.30 63.80 68.80 69.10 45.90 - - Claude-3.5-Sonnet 57.64 46.48 67.70 73.05 68.30 43.97 - - Open-Source General-Purpose Models Qwen2.5-VL-7B 48.98 24.18 70.20 58.52 51.00 39.26 73.50 52.23 Qwen2.5-VL-32B 57.60 38.40 74.70 69.10 57.44 49.26 85.36 61.69 InternVL2.5-8B 39.53 19.70 62.30 53.50 45.73 38.23 74.83 47.69 InternVL2.5-38B 49.40 32.20 71.84 68.61 56.98 47.21 82.77 58.43 Open-Source Multimodal Large Language Models MM-Eureka-7B 51.09 27.70 73.00 65.34 53.78 47.87 75.50 56.33 OpenVLThinker-7B 48.37 25.90 71.38 66.63 54.29 36.24 65.00 52.54 Perception-R1-7B 52.56 28.06 72.80 65.57 53.11 40.94 82.30 56.48 Vision-R1-7B 53.23 27.24 70.63 64.98 43.28 42.94 83.27 55.08 R1-Onevision-7B 45.12 23.91 66.21 61.88 43.70 44.53 78.45 51.97 ThinkLite-VL-7B 51.47 27.24 73.30 65.52 55.44 42.94 86.50 57.49 VL-Rethinker-7B 53.86 29.57 73.27 68.22 54.67 46.08 68.50 56.31 RuCL 54.14 28.88 74.10 71.49 56.67 49.66 85.50 60.06 Δ ⁡ ( Qwen2.5-VL-7B ) \Delta(\text{Qwen2.5-VL-7B}) ↑ \uparrow 5.16 ↑ \uparrow 4.70 ↑ \uparrow 3.90 ↑ \uparrow 12.97 ↑ \uparrow 5.67 ↑ \uparrow 10.40 ↑ \uparrow 12.00 ↑ \uparrow 7.83

[45] h3: 3.3 Phase II: Dynamic Curriculum Learning

[46] p: We employ a hybrid reward mechanism that integrates rule-based correctness with the stratified rubrics derived in Phase I . We introduce a stability-aware curriculum that dynamically adjusts the focus from foundational to advanced reasoning.

[47] p: Hybrid Reward Components. Our reward system adopts a hybrid evaluation strategy that integrates model-based rubric evaluation with strict rule-based verification, balancing fine-grained rubric-level process supervision with unambiguous outcome correctness. We employ a strict rule-based verifier to assess the final answer correctness. For each sampled response y i y_{i} conditioned on input x x , the final outcome reward is defined as:

[48] table: r ans ​ ( y i ∣ x ) = 𝕀 ⁡ ( grade ​ ( y ^ i , y ∗ ) = 1 ) , r_{\text{ans}}(y_{i}\mid x)=\mathbb{I}\!\left(\text{grade}(\hat{y}_{i},y^{*})=1\right), (4)

[49] p: where y ^ i \hat{y}_{i} is the extracted prediction and y ∗ y^{*} is the ground truth.

[50] p: In parallel, we evaluate the reasoning process using the foundational ( ℛ easy \mathcal{R}_{\text{easy}} ) and advanced ( ℛ hard \mathcal{R}_{\text{hard}} ) rubric sets derived in Sec. 3.2 . During training, the Judge model evaluates the generated response against all rubrics in these filtered sets. We aggregate the binary satisfaction signals to compute tier-level reasoning scores:

[51] table: r ¯ easy ​ ( y i ∣ x ) \displaystyle\bar{r}_{\text{easy}}(y_{i}\mid x) = 1 | ℛ easy | ​ ∑ R ∈ ℛ easy r ⁡ ( y i ∣ x , R ) , \displaystyle=\frac{1}{|\mathcal{R}_{\text{easy}}|}\sum_{R\in\mathcal{R}_{\text{easy}}}r(y_{i}\mid x,R), (5) r ¯ hard ​ ( y i ∣ x ) \displaystyle\bar{r}_{\text{hard}}(y_{i}\mid x) = 1 | ℛ hard | ​ ∑ R ∈ ℛ hard r ⁡ ( y i ∣ x , R ) , \displaystyle=\frac{1}{|\mathcal{R}_{\text{hard}}|}\sum_{R\in\mathcal{R}_{\text{hard}}}r(y_{i}\mid x,R),

[52] p: where r ⁡ ( y i ∣ x , R ) ∈ { 0 , 1 } r(y_{i}\mid x,R)\in\{0,1\} denotes whether the response satisfies rubric R R . These aggregated scores r ¯ easy \bar{r}_{\text{easy}} and r ¯ hard \bar{r}_{\text{hard}} serve as the basis of our curriculum scheduling mechanism.

[53] p: Performance-Triggered Curriculum Scheduling. We introduce a Stability-Aware Curriculum that regulates the progression from foundational to advanced reasoning supervision. In contrast to static schedules, RuCL activates advanced rubrics only after the model demonstrates stable proficiency on foundational ones.

[54] p: For a sampled response y i y_{i} at training step t t , we define the curriculum-modulated rubric reward as:

[55] table: r rub ( t ) ​ ( y i ∣ x ) = ( 1 − λ t ) ⋅ r ¯ easy ​ ( y i ∣ x ) + λ t ⋅ r ¯ hard ​ ( y i ∣ x ) , r_{\text{rub}}^{(t)}(y_{i}\mid x)=(1-\lambda_{t})\cdot\bar{r}_{\text{easy}}(y_{i}\mid x)+\lambda_{t}\cdot\bar{r}_{\text{hard}}(y_{i}\mid x), (6)

[56] p: where the curriculum coefficient λ t ∈ [ 0 , λ max ] \lambda_{t}\in[0,\lambda_{\text{max}}] controls the difficulty mix between foundational and advanced reasoning rubrics. Initially, λ t \lambda_{t} is set to zero and remains unchanged until foundational performance stabilizes.

[57] p: The curriculum proceeds in three phases:

[58] h4: (1) Stabilization Phase:

[59] p: We enforce λ t = 0 \lambda_{t}=0 . Let μ easy ( t ) = 𝔼 ( x , y ) ∼ ℬ t ​ [ r ¯ easy ​ ( y ∣ x ) ] \mu_{\text{easy}}^{(t)}=\mathbb{E}_{(x,y)\sim\mathcal{B}_{t}}\!\left[\bar{r}_{\text{easy}}(y\mid x)\right] denote the batch-averaged foundational rewards at step t t , and let W t = { μ easy ( t − w + 1 ) , … , μ easy ( t ) } W_{t}=\{\mu_{\text{easy}}^{(t-w+1)},\dots,\mu_{\text{easy}}^{(t)}\} be a sliding window of length w w . The transition is triggered at step T start T_{\text{start}} only when the model’s performance consistently exceeds a proficiency threshold τ t ​ h \tau_{th} throughout the entire window:

[60] table: T start = min { t ∣ ∀ μ ∈ W t , μ ≥ τ t ​ h } . T_{\text{start}}=\min\{t\mid\forall\mu\in W_{t},\mu\geq\tau_{th}\}. (7)

[61] p: This strict condition ensures that the model does not progress to advanced reasoning stages due to transient lucky guesses.

[62] h4: (2) Curriculum Ramp-up:

[63] p: Once triggered ( t > T start t>T_{\text{start}} ), λ t \lambda_{t} follows a defined growth function (e.g., Linear or Sigmoid) over a duration T ramp T_{\text{ramp}} :

[64] table: λ t = λ base + ( λ max − λ base ) ⋅ ϕ ⁡ ( t − T start T ramp ) , \lambda_{t}=\lambda_{\text{base}}+(\lambda_{\text{max}}-\lambda_{\text{base}})\cdot\phi\left(\frac{t-T_{\text{start}}}{T_{\text{ramp}}}\right), (8)

[65] p: where ϕ ⁡ ( ⋅ ) \phi(\cdot) is the normalized growth function clamped to [ 0 , 1 ] [0,1] and λ base \lambda_{\text{base}} denotes the initial curriculum weight.

[66] h4: (3) Advanced Consolidation:

[67] p: Upon completion of the ramp-up period ( t > T start + T ramp t>T_{\text{start}}+T_{\text{ramp}} ), the curriculum holds the difficulty weight at its peak: λ t = λ max \lambda_{t}=\lambda_{\text{max}} . Finally, we combine the rule-based outcome reward with the curriculum-modulated rubrics reward to obtain the scalar reward used by GRPO:

[68] table: r ( t ) ​ ( y i ∣ x ) = α ⋅ r ans ​ ( y i ∣ x ) + ( 1 − α ) ⋅ r rub ( t ) ​ ( y i ∣ x ) . r^{(t)}(y_{i}\mid x)=\alpha\cdot r_{\text{ans}}(y_{i}\mid x)+(1-\alpha)\cdot r_{\text{rub}}^{(t)}(y_{i}\mid x). (9)

[69] p: Here, r ( t ) ​ ( y i ∣ x ) r^{(t)}(y_{i}\mid x) is the scalar reward used in GRPO advantage estimation. We treat α ∈ [ 0 , 1 ] \alpha\in[0,1] as a fixed hyperparameter that controls the trade-off between outcome correctness and rubric-based process supervision.

[70] p: Analysis. While traditional curriculum learning operates by reshaping the input distribution, RuCL instead modulates the density of evaluative signals over the output space. We posit a hierarchical dependency among rubrics, where satisfying advanced (hard) rubrics presupposes competence in foundational (easy) ones. We further provide a theoretical justification for this design in Appendix B , demonstrating that the proposed schedule reduces the contribution of unreliable and high-noise gradient components induced by sparse advanced rewards, thereby stabilizing early-stage optimization. Prioritizing easy rubrics early in training therefore performs an implicit search-space pruning, restricting optimization to regions of the policy space where advanced rubric signals become attainable. This design reduces gradient interference from currently unachievable objectives, alleviates cold-start instability, and yields more stable and efficient optimization throughout training.

[71] h2: 4 Experiments

[72] h3: 4.1 Experiment Setup

[73] p: Datasets & Models. In our experiments, we utilize the ViRL-39K dataset ( Wang et al., 2025a ) for model training. ViRL-39K is a large-scale, high-quality dataset specifically curated for vision-language reinforcement learning (RL). It comprises approximately 39,000 verifiable question-answering pairs that cover a wide range of complex scenarios, including STEM, spatial reasoning, and multi-disciplinary chart analysis. Specifically, we initialize our training from Qwen2.5-VL-7B-Instruct ( Bai et al., 2025 ) as the base model, leveraging its advanced multi-modal perception and robust instruction-following capabilities to facilitate further reasoning-oriented optimization.

[74] p: Evaluation. We evaluate RuCL on widely used visual reasoning benchmarks covering multimodal mathematical reasoning and general visual reasoning. For multimodal mathematical reasoning, we use MathVista ( Lu et al., 2023 ) , MathVerse ( Zhang et al., 2024 ) , MATH-Vision ( Wang et al., 2024a ) , and WeMATH ( Qiao et al., 2025 ) . For general visual reasoning, we employ LogicVista ( Xiao et al., 2024 ) , Super-CLEVR Counting ( Li et al., 2023 ) , and MMMU ( Yue et al., 2024 ) to assess logical deduction, compositional counting and perception, and multi-disciplinary knowledge, respectively.

[75] p: Baselines. We compare our model with several strong MLLMs, categorized into three groups: (1) Proprietary models , including GPT-4o ( Hurst et al., 2024 ) and Claude-3.5-Sonnet ( Anthropic, 2024 ) ; (2) Open-source general-purpose models , such as Qwen2.5-VL-7B-Instruct, Qwen2.5-VL-32B-Instruct ( Bai et al., 2025 ) , InternVL2.5-8B and InternVL2.5-38B ( Chen et al., 2024 ) ; and (3) Open-source reasoning-focused models , including MM-Eureka-7B ( Meng et al., 2025 ) , OpenVLThinker-7B ( Deng et al., 2025 ) , Perception-R1-7B ( Xiao et al., 2025 ) , Vision-R1-7B ( Huang et al., 2025a ) , R1-Onevision-7B ( Yang et al., 2025 ) , ThinkLite-VL-7B ( Wang et al., 2025b ) , and VL-Rethinker-7B ( Wang et al., 2025a ) .

[76] p: Configuration. For data-driven candidate generation, we utilize Gemini 3 Pro ( Google DeepMind, 2025 ) as the teacher model. Through few-shot prompting, we generate 20 rubric candidates. Subsequently, we conduct a rollout on N = 2,000 N=2,000 samples, retaining 6 core rubrics after filtering with an applicability threshold of 0.99 0.99 . In the reinforcement learning phase, we deploy Qwen3-VL-235B-A22B-Instruct ( Team, 2025 ) as the reward judge. The detailed prompts guiding the judge model’s scoring process are provided in Appendix F . To implement the proposed Stability-Aware Curriculum , we configure the sliding window size K = 20 K=20 and the proficiency threshold τ t ​ h = 0.9 \tau_{th}=0.9 . The reward balancing coefficient is set to α = 0.7 \alpha=0.7 to prioritize factual accuracy. All experiments are conducted on NVIDIA H200 GPUs using the verl framework ( Sheng et al., 2025 ) . Comprehensive hyperparameter details are provided in Appendix C .

[77] figure: Figure 3 : Left: Training dynamics of Foundational (blue) and Advanced (red) rubric rewards. Middle: Ablation study results on rubric aggregation and scheduling strategies. Right: Sensitivity analysis of the reward balancing hyperparameter.

[78] h3: 4.2 Main Results

[79] h4: Mathematical Reasoning Performance.

[80] p: As shown in Table 2 , RuCL demonstrates superior performance, outperforming the baseline Qwen2.5-VL-7B across all mathematical benchmarks. This significant improvement, driven by the integration of our fine-grained rubric-based reward modeling and curriculum learning strategy, validates the efficacy of prioritizing simple rubrics in early training stages before transitioning to harder reasoning constraints. Specifically, on the challenging WeMATH and MathVerse datasets, our model improves by 12.97% (from 58.52% to 71.49%) and 5.16% (from 48.98% to 54.14%), respectively. Furthermore, when compared with other leading open-source reasoning models such as ThinkLite-VL-7B and VL-Rethinker-7B, RuCL achieves the highest average score of 60.06% across all seven tasks, highlighting its robust reasoning capabilities.

[81] p: Generalization to General and Logical Benchmarks. Extending beyond mathematics, our model achieves competitive results across broader reasoning tasks. As shown in the General section of Table 2 , RuCL exhibits remarkable generalization. On the LogicVista benchmark, which requires complex logical deduction, our model achieves a 10.40% improvement over the baseline (from 39.26% to 49.66%), surpassing all other open-source 7B competitors. Similarly, we observe substantial gains on the comprehensive MMMU (+5.67%) and Counting (+12.00%) benchmarks, with the latter highlighting enhanced fine-grained visual perception (85.50%). These results indicate that combining intermediate rubric rewards with final outcome supervision effectively enhances the model’s fundamental reasoning robustness rather than merely overfitting to mathematical domains. Notably, despite its compact scale, our model significantly narrows the performance gap with top-tier proprietary models.

[82] p: Training Dynamics and Curriculum Efficacy. To validate the efficacy of RuCL, we analyze the evolution of reward trajectories throughout the training process, as shown in Figure 3 . Initially, the curriculum prioritizes foundational rubrics, leading to the rapid mastery of prerequisite skills such as visual presence and entity extraction. As the mechanism detects stable proficiency (scores stabilizing > 0.9 >0.9 ) and progressively introduces advanced reasoning constraints, the model exhibits steady improvement in higher-order tasks while maintaining robust performance on foundational metrics. This demonstrates that RuCL fosters complex reasoning while preserving foundational visual perception and instruction-following skills. Furthermore, qualitative case studies in Appendix G provide concrete evidence of RuCL’s capability to mitigate reward hacking. We show that our rubric-based judge effectively penalizes spurious reasoning chains that serendipitously arrive at the correct answer—instances that typically escape detection in outcome-only supervision—thereby enforcing genuine logical consistency.

[83] h3: 4.3 Ablation Study

[84] p: In this section, we conduct ablation studies to validate the contributions of our key design choices. We focus on two key components: the rubric aggregation mechanism and the sensitivity to the reward balancing hyperparameter α \alpha .

[85] p: Impact of Rubric Aggregation and Scheduling. To assess the contribution of rubric aggregation and curriculum scheduling, we compare our method ( Sigmoid Stratification ) with the following baselines, keeping the GRPO backbone and training data fixed: (1) Vanilla GRPO: Trains using solely the rule-based outcome reward r ans r_{\text{ans}} , ignoring all reasoning rubrics. (2) Uniform Averaging: Aggregates all filtered rubrics into a single unweighted average score, discarding difficulty stratification and curriculum scheduling. (3) RuCL (Sigmoid Stratification): Adopts the proposed stratified rubrics ( ℛ easy , ℛ hard \mathcal{R}_{\text{easy}},\mathcal{R}_{\text{hard}} ) with the stability-aware sigmoid schedule for λ t \lambda_{t} . (4) Linear Stratification: Replaces the sigmoid growth function with a simple linear ramp for λ t \lambda_{t} to evaluate the impact of schedule shape.

[86] figure: Table 3 : Ablation results on General benchmarks. Method MMMU LogicVista Counting Avg. Vanilla GRPO 54.89 46.53 76.00 59.14 Uniform Averaging 55.44 50.11 77.00 59.29 Linear Stratification 55.44 47.43 79.50 60.79 RuCL 56.67 49.66 85.50 63.94

[87] p: Figure 3 highlights the aggregate trend: Vanilla GRPO (57.13%) is surpassed by Uniform Averaging (57.56%) due to process supervision, while Linear Stratification (58.41%) yields further gains by distinguishing difficulty. As shown in Table 3 , RuCL significantly outperforms the Linear strategy, particularly on perception-heavy tasks like Counting (85.50% vs. 79.50%) and logic-intensive tasks like LogicVista (49.66% vs. 47.43%). This advantage stems from the Sigmoid schedule’s ability to reach maximum difficulty saturation earlier than the linear ramp. By completing the transition phase faster, Sigmoid affords the model a longer stable period to converge under the full weight of hard constraints, whereas the Linear approach keeps the reward signal in a continuous state of flux.

[88] p: Sensitivity to Reward Balancing Hyperparameter α \alpha . We further investigate the system’s sensitivity to the hyperparameter α ∈ [ 0.5 , 0.9 ] \alpha\in[0.5,0.9] , which governs the trade-off between outcome correctness and rubric-based fine-grained supervision. As visualized in the radar chart (Figure 3 ), the overall performance achieves its optimum at α = 0.7 \alpha=0.7 . At this optimal setting, the model demonstrates robust dominance across diverse tasks, achieving peak scores of 71.49% on WeMath and 85.50% on Counting. Deviating from this balance proves detrimental: lowering α \alpha to 0.5 (where fine-grained rubrics dominate) causes performance drops (e.g., Counting falls to 79.00%), likely because excessive auxiliary constraints distract from the primary objective of solution correctness. Conversely, increasing α \alpha to 0.9 diminishes the benefit of our fine-grained supervision, causing the system to degenerate towards a sparse-reward regime where complex reasoning capability degrades significantly (e.g., WeMath drops to 53.78%). Thus, a configuration of α = 0.7 \alpha=0.7 strikes the most effective balance, integrating precise intermediate guidance without overshadowing the ultimate goal of accurate problem-solving.

[89] figure: Table 4 : Sensitivity analysis of sliding window size w w in curriculum triggering. Window Size w w Mathematical General Avg. w = 10 w=10 55.57 60.8 57.81 w = 20 w=20 57.15 63.94 60.06 w = 30 w=30 56.64 63.74 59.67

[90] p: Sensitivity to Sliding Window Size w w . We study the sensitivity of the stability-aware trigger to the sliding window size w w in Eq. 7 . We vary w ∈ { 10 , 20 , 30 } w\in\{10,20,30\} while keeping all other hyperparameters fixed. As shown in Table 4 , w = 20 w=20 achieves the best overall performance, while w = 30 w=30 performs comparably with only a marginal gap. In contrast, w = 10 w=10 consistently underperforms, indicating that a shorter window is more susceptible to transient fluctuations and may trigger the curriculum transition prematurely. Overall, these observations suggest that our curriculum mechanism is robust to moderate changes in w w , and we adopt w = 20 w=20 as the default setting in all experiments.

[91] h2: 5 Conclusion

[92] p: We propose Stratified Rubric-based Curriculum Learning (RuCL) , a framework that reframes curriculum learning from data selection to reward design. By stratifying evaluation rubrics into foundational and advanced categories, RuCL aligns reward signals with the model’s evolving capabilities. Integrated with GRPO, this approach effectively mitigates reward hacking and training instability. Experiments across seven benchmarks demonstrate that RuCL significantly outperforms the base model and establishes a new state-of-the-art among 7B-scale reasoning models. Future work will explore online rubric construction and scaling to larger architectures.

[93] h2: Impact Statement

[94] p: This paper introduces Stratified Rubric-based Curriculum Learning (RuCL), a framework that enhances the reasoning capabilities of Multimodal Large Language Models (MLLMs) by shifting curriculum focus from data selection to reward design. RuCL guides models to master foundational perception before progressing to advanced deduction, fostering the development of reliable models that prioritize intermediate reasoning integrity. RuCL utilizes widely recognized, publicly available datasets for training and evaluation, strictly adhering to their licenses and usage policies without intentionally introducing private, personally identifiable information (PII) or offensive content, ensuring that our advancements in multimodal intelligence are built upon transparent and reproducible foundations.

[95] h2: References

[96] h2: Appendix A Group Relative Policy Optimization (GRPO)

[97] p: To enhance the reasoning capabilities of our model, we optimize the policy π θ \pi_{\theta} using Group Relative Policy Optimization (GRPO) ( Shao et al., 2024 ) . Unlike standard Proximal Policy Optimization (PPO) ( Schulman et al., 2017 ) , which necessitates a separate value function (critic) for advantage estimation, GRPO reduces computational overhead by leveraging group-based statistics. Specifically, for each input query x x , we sample a group of G G outputs { y i } i = 1 G \{y_{i}\}_{i=1}^{G} from π θ old \pi_{\theta_{\text{old}}} . The advantage A ^ i \hat{A}_{i} for the i i -th output is estimated by normalizing its scalar reward r ⁡ ( y i ∣ x ) r(y_{i}\mid x) (derived from our stratified rubrics as detailed in Sec. 3.2 ) against the group statistics:

[98] table: A ^ i = r ​ ( y i ∣ x ) − mean ​ ( 𝐫 ) std ​ ( 𝐫 ) , \hat{A}_{i}=\frac{r(y_{i}\mid x)-\text{mean}(\mathbf{r})}{\text{std}(\mathbf{r})}, (10)

[99] p: where 𝐫 = { r ⁡ ( y 1 ∣ x ) , … , r ⁡ ( y G ∣ x ) } \mathbf{r}=\{r(y_{1}\mid x),\dots,r(y_{G}\mid x)\} denotes the set of rewards. The objective maximizes the PPO-style clipped loss while penalizing deviations from the reference model π ref \pi_{\text{ref}} via a KL-divergence term. The objective function is formulated as:

[100] table: 𝒥 ( θ ) = 𝔼 [ 1 G ∑ i = 1 G ( ℒ i clip ( θ ) − β 𝔻 KL ( π θ | | π ref ) ) ] , \mathcal{J}(\theta)=\mathbb{E}\left[\frac{1}{G}\sum_{i=1}^{G}\left(\mathcal{L}^{\text{clip}}_{i}(\theta)-\beta\,\mathbb{D}_{\text{KL}}(\pi_{\theta}||\pi_{\text{ref}})\right)\right], (11)

[101] p: where ℒ i clip ​ ( θ ) = min ⁡ ( ρ i ​ A ^ i , clip ​ ( ρ i , 1 − ε , 1 + ε ) ​ A ^ i ) \mathcal{L}^{\text{clip}}_{i}(\theta)=\min(\rho_{i}\hat{A}_{i},\text{clip}(\rho_{i},1-\varepsilon,1+\varepsilon)\hat{A}_{i}) represents the clipped surrogate objective, with the importance ratio ρ i = π θ ​ ( y i ∣ x ) π θ old ​ ( y i ∣ x ) \rho_{i}=\frac{\pi_{\theta}(y_{i}\mid x)}{\pi_{\theta_{\text{old}}}(y_{i}\mid x)} . This approach allows for stable and efficient policy optimization without the memory burden of a critic model.

[102] h2: Appendix B Theoretical Derivation and Analysis of Gradient Variance

[103] p: In this section, we provide a detailed derivation of the gradient variance decomposition to theoretically justify the stability-aware curriculum schedule proposed in Sec. 3.3 . For clarity of exposition, we consider the score-function form of the policy gradient estimator and omit baselines and advantage normalization. The following analysis applies analogously to advantage-based estimators used in practice. For consistency with Eq. 9 , we analyze the curriculum-modulated rubric component r rub ( t ) r^{(t)}_{\text{rub}} ; the outcome term α ​ r ans \alpha\,r_{\text{ans}} is a fixed-weight addend that does not affect the variance decomposition with respect to λ t \lambda_{t} .

[104] h3: B.1 Gradient Estimator Decomposition

[105] p: Consider the standard Policy Gradient objective function J ⁡ ( θ ) = 𝔼 τ ∼ π θ ​ [ r ⁡ ( τ ) ] J(\theta)=\mathbb{E}_{\tau\sim\pi_{\theta}}[r(\tau)] . The gradient estimator at step t t is expressed as:

[106] table: g ^ t = ∇ θ ​ log ​ π θ ​ ( y | x ) ⋅ r rub ( t ) ​ ( y | x ) \hat{g}_{t}=\nabla_{\theta}\log\pi_{\theta}(y|x)\cdot r^{(t)}_{\text{rub}}(y|x) (12)

[107] p: In RuCL, the reward r rub ( t ) r^{(t)}_{\text{rub}} is a dynamic convex combination of foundational ( r ¯ e ​ a ​ s ​ y \bar{r}_{easy} ) and advanced ( r ¯ h ​ a ​ r ​ d \bar{r}_{hard} ) rubric scores:

[108] table: r rub ( t ) ​ ( y | x ) = ( 1 − λ t ) ​ r ¯ e ​ a ​ s ​ y ​ ( y | x ) + λ t ​ r ¯ h ​ a ​ r ​ d ​ ( y | x ) r^{(t)}_{\text{rub}}(y|x)=(1-\lambda_{t})\bar{r}_{easy}(y|x)+\lambda_{t}\bar{r}_{hard}(y|x) (13)

[109] p: Substituting this into the gradient estimator, we obtain a decomposed gradient form:

[110] table: g ^ t = ( 1 − λ t ) ​ ∇ θ ​ log ​ π θ ​ ( y | x ) ​ r ¯ e ​ a ​ s ​ y ⏟ g ^ e ​ a ​ s ​ y + λ t ​ ∇ θ ​ log ​ π θ ​ ( y | x ) ​ r ¯ h ​ a ​ r ​ d ⏟ g ^ h ​ a ​ r ​ d \hat{g}_{t}=(1-\lambda_{t})\underbrace{\nabla_{\theta}\log\pi_{\theta}(y|x)\bar{r}_{easy}}_{\hat{g}_{easy}}+\lambda_{t}\underbrace{\nabla_{\theta}\log\pi_{\theta}(y|x)\bar{r}_{hard}}_{\hat{g}_{hard}} (14)

[111] p: where g ^ e ​ a ​ s ​ y \hat{g}_{easy} and g ^ h ​ a ​ r ​ d \hat{g}_{hard} represent the stochastic gradient components induced by foundational and advanced rubrics, respectively.

[112] h3: B.2 Variance Analysis

[113] p: Since the gradient estimator is a random vector, we quantify its variability using the trace of the covariance matrix:

[114] table: 𝒱 ⁡ ( g ^ t ) ≜ tr ⁡ ( Cov ⁡ ( g ^ t ) ) = 𝔼 ⁡ [ ‖ g ^ t − 𝔼 ⁡ [ g ^ t ] ‖ 2 2 ] . \mathcal{V}(\hat{g}_{t})\triangleq\mathrm{tr}(\mathrm{Cov}(\hat{g}_{t}))=\mathbb{E}\!\left[\|\hat{g}_{t}-\mathbb{E}[\hat{g}_{t}]\|_{2}^{2}\right]. (15)

[115] p: Using the covariance property of linear combinations of random vectors, we obtain:

[116] table: 𝒱 ⁡ ( g ^ t ) = ( 1 − λ t ) 2 ​ 𝒱 ​ ( g ^ e ​ a ​ s ​ y ) + λ t 2 ​ 𝒱 ​ ( g ^ h ​ a ​ r ​ d ) + 2 ​ λ t ​ ( 1 − λ t ) ​ tr ​ ( Cov ⁡ ( g ^ e ​ a ​ s ​ y , g ^ h ​ a ​ r ​ d ) ) . \mathcal{V}(\hat{g}_{t})=(1-\lambda_{t})^{2}\mathcal{V}(\hat{g}_{easy})+\lambda_{t}^{2}\mathcal{V}(\hat{g}_{hard})+2\lambda_{t}(1-\lambda_{t})\,\mathrm{tr}(\mathrm{Cov}(\hat{g}_{easy},\hat{g}_{hard})). (16)

[117] h3: B.3 Justification of Curriculum Schedule

[118] p: Eq. 16 provides three insights that motivate the proposed scheduling strategy:

[119] p: Suppressing Unreliable Gradient Signals: In the early stages of training, the model rarely satisfies advanced reasoning rubrics, making r ¯ h ​ a ​ r ​ d \bar{r}_{hard} highly sparse. This sparsity yields low signal-to-noise ratio and unstable estimates of g ^ h ​ a ​ r ​ d \hat{g}_{hard} , rather than merely large reward variance. Setting λ t = 0 \lambda_{t}=0 eliminates the contribution of 𝒱 ⁡ ( g ^ h ​ a ​ r ​ d ) \mathcal{V}(\hat{g}_{hard}) , thereby preventing noisy high-order signals from dominating early optimization.

[120] p: Reducing Gradient Interference: Before foundational competencies are established, gradient directions induced by perception-oriented and reasoning-oriented rubrics may be weakly correlated or even negatively correlated, which leads to destructive interference under mixed optimization. The curriculum decouples these learning phases, allowing the model to first converge to stable foundational representations.

[121] p: Safe and Progressive Transition: As training progresses, successful satisfaction of advanced rubrics becomes more frequent, which increases the reliability of g ^ h ​ a ​ r ​ d \hat{g}_{hard} and improves alignment between gradient components. Under this condition, increasing λ t \lambda_{t} gradually introduces harder objectives while keeping the covariance term in Eq. 16 controlled.

[122] p: Overall, the curriculum schedule reduces the contribution of unreliable gradient components in early training and progressively incorporates harder objectives as their gradient signals become statistically reliable, which stabilizes optimization during multi-stage reward learning.

[123] h2: Appendix C Configuration Details

[124] p: All experiments are conducted using the verl framework ( Sheng et al., 2024 ) , which facilitates efficient large-scale reinforcement learning. We employ the Group Relative Policy Optimization (GRPO) algorithm. The training utilizes a constant learning rate scheduler to ensure convergence stability in the later stages of curriculum learning.

[125] p: Table 5 summarizes the specific hyperparameter settings. Notably, the curriculum parameters ( K , τ t ​ h K,\tau_{th} ) are chosen based on preliminary experiments to balance the trade-off between stability and learning speed.

[126] figure: Table 5 : Detailed hyperparameters for DR-CL training. Hyperparameter Value Optimization & Rollout Training Batch Size 256 Global Batch Size 128 Rollout Number ( G G ) 8 Sampling Temperature 1.0 Learning Rate 1 ​ e- ​ 6 1\text{e-}6 KL Coefficient ( β \beta ) 0.01 Curriculum & Rewards Reward Weight ( α \alpha ) 0.7 Sliding Window Size ( w w ) 20 Proficiency Threshold ( τ t ​ h \tau_{th} ) 0.9 Max Hard Weight ( λ max \lambda_{\max} ) 1.0

[127] h2: Appendix D Rubric Construction and Filtering

[128] p: To ensure a comprehensive evaluation of the model’s reasoning capabilities, we employ a teacher model, Gemini 3 Pro ( Google DeepMind, 2025 ) , to generate a pool of 20 rubric candidates through few-shot prompting. These rubrics cover dimensions including visual faithfulness, logical coherence, constraint satisfaction, and mathematical accuracy.

[129] h3: D.1 Detailed Definitions of All 20 Rubric Candidates

[130] h3: D.2 Applicability and Accuracy of Rubric Candidates

[131] p: After generating the initial 20 rubric candidates, we evaluate their performance on the sampled data. Table 6 summarizes the applicability (the frequency with which the rubric is deemed relevant to the problem) and the model’s accuracy under each rubric. Based on these metrics and the necessity for automated reward computation, we select the final 6 rubrics (R01–R06) to be used in our Reinforcement Learning (RL) pipeline.

[132] p: The statistics reveal significant disparity in coverage; for instance, candidates like Cand_09 and Cand_03 are applicable to only 9.7% and 18.8% of samples, respectively. Without our applicability-aware filtering, these rubrics would introduce erroneous failure signals in over 80% of training instances, severely destabilizing the reward function.

[133] figure: Table 6 : Statistics for the 20 rubric candidates. The model selects Candidates 01, 02, 07, 11, 13, and 17 to form the core reward metrics R01–R06. Candidate 20 serves as the equivalent of the ground truth accuracy for the final assessment. ID Applicability (%) Accuracy (%) ID Applicability (%) Accuracy (%) Cand_01 (R01) 99.1 98.3 Cand_11 (R04) 100.0 69.4 Cand_02 (R02) 99.4 99.4 Cand_12 78.4 94.8 Cand_03 18.8 98.1 Cand_13 (R05) 99.2 68.6 Cand_04 78.1 99.3 Cand_14 34.0 90.4 Cand_05 71.0 96.7 Cand_15 27.3 98.2 Cand_06 22.9 87.3 Cand_16 33.5 85.8 Cand_07 (R03) 100.0 86.1 Cand_17 (R06) 99.9 91.7 Cand_08 93.2 35.4 Cand_18 97.5 66.4 Cand_09 9.7 90.7 Cand_19 96.7 27.7 Cand_10 83.9 52.2 Cand_20 (GT) 100.0 47.9

[134] h2: Appendix E Rubric Assessment and Filtering

[135] p: We utilized a strict JSON-based prompt to ensure the Judge model evaluates both applicability and correctness. The prompts used in our pipeline are shown below.

[136] h2: Appendix F Reward Signal Generation Prompts

[137] p: This appendix details the prompt engineering used to instantiate the reward model. We employ a strict “Judge” persona to convert the rubric evaluations into binary reward signals. The Judge receives the specific problem context, visual input, and the rubric candidates to generate a rationalized score for each criterion.

[138] h2: Appendix G Case Studies

[139] p: This appendix demonstrates the generation process of rubric-based rewards for two single instances. We present the input problem (text and image), the model’s reasoning chain (rollout), and the raw JSON output generated by the Judge model, which contains the rationale and binary scores for each rubric.

[140] h3: G.1 Case Study 1: Mitigation of Reward Hacking

[141] h4: Analysis and Overview.

[142] p: This case serves as a quintessential example of reward hacking , demonstrating how RuCL detects spurious reasoning that outcome-only supervision would miss.

[143] p: The Trap: The model arrives at the correct final answer ( BC = 20 \text{BC}=20 ) and would receive a perfect reward ( r = 1.0 r=1.0 ) under standard RLVR.

[144] p: The Flaw: As highlighted by the Judge’s rationale in R04 (Step Coherence) , R05 (Evidence Grounding) and R06 (Reasoning Conclusion Match) , the model incorrectly applies a sub-triangle area formula to the whole triangle and makes an unjustified ”magic leap” to the final value.

[145] p: The Mitigation: RuCL identifies these logical gaps. Despite the correct answer, the total reward is penalized significantly, effectively discouraging the model from learning such ”lucky guesses.”

[146] h3: G.2 Case Study 2: Alignment of Foundational and Advanced Reasoning

[147] h4: Analysis and Overview.

[148] p: In contrast to Case 1, this example illustrates a successfully aligned reasoning trajectory where visual perception supports logical deduction.

[149] p: Foundational Skills: The model correctly extracts coordinates and identifies the linear function (satisfying R01–R04 ).

[150] p: Advanced Reasoning: The derivation is mathematically sound, and the final answer is a direct logical consequence of the steps (satisfying R05–R06 ).

[151] p: Conclusion: The high scores across all stratified rubrics confirm that the model has internalized the curriculum, treating perception and reasoning as an integrated process rather than disjoint tasks.

[152] h2: Appendix H Additional Evaluation on Out-of-Distribution Robustness

[153] p: To assess the model’s robustness and generalization capabilities in specialized out-of-domain (OoD) scenarios, we utilize EvadeBench ( Xu et al., 2025a ) . As the first expert-curated Chinese benchmark for evasive content detection in e-commerce, EvadeBench targets the model’s ability to identify content that superficially complies with safety policies but covertly conveys prohibited information. This benchmark challenges the model to reason through ambiguity and context shifts, which serves as a critical indicator of its safety alignment and adaptability beyond standard academic tasks.

[154] figure: Table 7 : Performance evaluation on EvadeBench Method EvadeBench Acc. (%) Qwen2.5-VL-7B-Instruct 43.90 Vanilla GRPO 44.47 RuCL 45.86

[155] p: Table 7 presents the quantitative results on EvadeBench. We observe that the task poses a challenge for all evaluated models, with accuracies remaining below 46%. This reflects the difficulty of generalizing to adversarial examples that differ significantly from the training distribution. In this context, RuCL achieves an accuracy of 45.86%, showing a modest improvement over the Qwen2.5-VL-7B-Instruct baseline (43.90%) and Vanilla GRPO (44.47%). While the overall performance remains limited by the domain gap, the results suggest that RuCL maintains a slight advantage in generalization capability compared to standard reinforcement learning methods.

[156] h2: Appendix I Limitations

[157] p: Despite the success of RuCL, several limitations persist. First, reliance on proprietary teacher LLM for generation and large-scale judges for reward calculation incurs moderate computational overhead. Second, to ensure stability, we employ a static stratification based on initial statistics, which simplifies the curriculum by assuming constant rubric difficulty throughout training. Future research could explore developing adaptive mechanisms to dynamically update rubric difficulties during the online phase. Furthermore, we explore the model’s limitations in specialized out-of-distribution scenarios (e.g., evasive content detection), with detailed results and analysis on EvadeBench provided in Appendix H .

[158] h2: Instructions for reporting errors

[159] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[160] p: Tip: You can select the relevant text first, to include it in your report.

[161] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[162] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
