[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: ContextRL: Enhancing MLLM’s Knowledge Discovery Efficiency with Context-Augmented RL Thanks: † \dagger Work done during an internship at Kuaishou Technology. Thanks: ‡ {\ddagger} Corresponding Authors: Jinpeng Wang and Chun Yuan Thanks: ⋆ \star Project Leader.

[3] h6: Abstract.

[4] p: Reinforcement Learning with Verifiers (RLVR) has become a standard paradigm for post-training Multimodal Large Language Models (MLLMs): During the sampling process, the policy model generates experience. The verifier then distinguishes this experience into correct knowledge and erroneous patterns, and subsequently guides the policy model to internalize the valid knowledge while avoiding the incorrect patterns, thereby improving overall model performance. Although effective, we argue that current RLVR frameworks suffer from two intrinsic information bottlenecks that hinder effective knowledge discovery: (1) Identifiability: Verifiers with limited context (e.g., only final answers) struggle to distinguish correct reasoning from hallucinations, leading to reward hacking; (2) Reachability: For hard queries, the policy model rarely samples correct responses, resulting in sparse gradient signals. In this work, we propose ContextRL, a novel framework that leverages context augmentation to overcome these bottlenecks. Specifically, to enhance Identifiability, we provide the reward model with full reference solutions as context, enabling fine-grained process verification to filter out false positives (samples with the right answer but low-quality reasoning process). To improve Reachability, we introduce a multi-turn sampling strategy where the reward model generates mistake reports for failed attempts, guiding the policy to "recover" correct responses from previously all-negative groups. Experimental results on 11 perception and reasoning benchmarks show that ContextRL significantly improves knowledge discovery efficiency. Notably, ContextRL enables the Qwen3-VL-8B model to achieve performance comparable to the 32B model, outperforming standard RLVR baselines by a large margin while effectively mitigating reward hacking. Our in-depth analysis reveals the significant potential of contextual information for improving reward model accuracy and document the widespread occurrence of reward hacking, offering valuable insights for future RLVR research.

[5] h6: Keywords:

[6] h2: 1. INTRODUCTION

[7] p: Knowledge discovery ( Frawley et al., 1992 ) is defined as a systematic process to identify valid, novel, and interpretable patterns from large-scale data and transforming them into actionable knowledge structures ( Cios et al., 1998 ) . In the big data era, how to perform knowledge discovery under with large-scale heterogeneous multimodal data becomes a core challenge in the construction of intelligent information systems. In recent years, Multimodal Large Language Models ( Bai et al., 2025 ; Hong et al., 2025 ; Team et al., 2025a ) (MLLMs) have demonstrated remarkable capabilities in multimodal understanding and reasoning tasks ( Team, 2025 ; OpenAI, 2025 ) , offering critical support for knowledge acquisition ( Deng et al., 2025 ) and representation ( Pan et al., 2024 ; Luo et al., 2024 ) .

[8] p: The training of MLLMs can be conceptualized as a parameter-centric process of knowledge discovery: models acquire knowledge from training datasets driven loss functions, with the learned representations encoded within parameters. Building upon Large Language Model (LLM) ( Han et al., 2021 ; Alayrac et al., 2022 ) , MLLM training is typically divided into two stages: pre-training and post-training ( Bai et al., 2025 ; Team et al., 2025b ) . During pre-training, models leverage large-scale image–text corpora to achieve multimodal alignment ( Bai et al., 2023 ; Fu et al., 2025 ) . In post-training, common approaches include knowledge distillation via supervised fine-tuning (SFT) ( Wang et al., 2025d ; Li et al., 2024a ) and policy optimization through reinforcement learning (RL) ( Murphy, 2024 ; Zheng et al., 2025b ) . For both pre-training and SFT, the model directly acquires knowledge from static datasets. In contrast, RL requires the MLLM to function as a policy model that interactively explores an environment composed of a reward system and a dataset, receiving feedback to iteratively refine its behavior, enabling MLLMs to acquire knowledge adaptively across diverse scenarios ( Li et al., 2026 ; Lu et al., 2025a ) .

[9] p: Inspired by large reasoning LLMs ( Liu et al., 2024 ; Zhang et al., 2025 ) , RL training for MLLMs commonly adopts the RLVR (Reinforcement Learning with verifier Reward) paradigm ( Huang et al., 2025 ) . In this framework, the MLLM samples from the training set to generate responses for each query, which are then evaluated by a Verifier that provides correctness-based feedback. The model subsequently adjusts the generation probabilities of different responses according to this feedback signal. RLVR-based methods, such as GRPO ( Shao et al., 2024 ) and DAPO ( Yu et al., 2025 ) , have demonstrated considerable success. Current optimization on RL algorithms primarily focuses on reward shaping ( Wu et al., 2025 ) , regularization ( Cui et al., 2025b ) , and training-inference consistency ( Zheng et al., 2025a ) , these approaches fail to increase the amount of knowledge that the policy model acquires from the environment during RL, and thus do not overcome the information bottleneck of RLVR systems.

[10] p: To elucidate this, we conduct an in-depth analysis: We first identify two information sources for the policy model in RLVR framework: (1) responses generated by sampling, which constitute exploratory experience, and (2) reward signals provided by the verifier, which discriminate experience into knowledge and mistakes. We then delineate the information bottlenecks of each source: For experience sampling, if the policy model cannot produce correct responses, no actionable optimization signal is conveyed, thereby stalling learning; for knowledge discrimination, if the verifier does not provide accurate judgment, the model becomes susceptible to reward hacking ( Wang et al., 2024a ) . Both bottlenecks substantially constrain the knowledge discovery efficiency of MLLMs during RLVR training.

[11] p: Recognizing these limitations, we propose leveraging context augmentation to overcome both information bottlenecks. We introduce the ContextRL framework, which consists of: (1) Context-Augmented Reward Model that enhances the reliability of reward signals by providing the reward model with richer reference context, thereby mitigating reward hacking caused by false-positive samples; (2) Context-Augmented Policy Model that employs a multi-turn sampling strategy, wherein mistake reports derived from negative responses are fed back to the policy model to expand its knowledge boundaries and facilitate the acquisition of correct responses; and (3) tailored optimization procedures for both single-turn and multi-turn samples to ensure training stability and convergence.

[12] p: To validate the efficacy of ContextRL in enhancing knowledge discovery for MLLMs, we constructed a training dataset comprising 29K samples to train the Qwen3VL-8B-Instruct ( Bai et al., 2025 ) model. We conduct comprehensive evaluations on 5 perception benchmarks and 6 reasoning benchmarks, comparing ContextRL against SFT and other RLVR methods. Experimental results demonstrate that ContextRL successfully injects more reliable knowledge into Qwen3VL-8B , significantly outperforming baslines. Notably, the ContextRL-trained 8B model achieves performance comparable to that of the 32B variant. To further elucidate the underlying mechanisms of ContextRL, we performed in-depth analytical experiments. Results indicate that context augmentation substantially improves the discriminative capability of the reward model. Moreover, we observed that false-positive samples are prevalent during training and pose a significant threat to effective knowledge acquisition by MLLMs. Finally, we quantitatively characterize the information gain introduced by ContextRL, providing empirical evidence for its effectiveness in alleviating information bottlenecks within the RLVR framework.

[13] p: We summarize our contributions as follows:

[14] p: An in-depth analysis : We figure out the information bottlenecks inherent in the RLVR framework, highlighting the critical importance of reward reliability and the generation of correct responses for effective knowledge acquisition in MLLMs.

[15] p: A novel and powerful framework : We propose ContextRL, leveraging context augmentation to enhance both the policy model and the reward model. Evaluations across 11 diverse benchmarks demonstrate that ContextRL substantially improves the efficiency of knowledge discovery during RLVR training, expands the MLLM’s knowledge boundaries, and exhibits strong generalizability.

[16] p: Insightful findings : Through analytical experiments, we reveal the detrimental impact of false-positive samples on MLLM learning, uncover the substantial potential of context in improving reward model accuracy, and document the pervasive occurrence of reward hacking phenomena, providing valuable insights and practical guidance for future RLVR research.

[17] h2: 2. METHODOLOGY

[18] h3: 2.1. RLVR for MLLMs

[19] p: RLVR provides an efficient mechanism for MLLMs to extract, consolidate, and store knowledge from interactions with the environment.

[20] h4: 2.1.1. RLVR’s Components

[21] p: A typical RLVR system for MLLMs consists of the following elements:

[22] p: Dataset: Let 𝒟 \mathcal{D} denote a set of queries and corresponding ground truth, 𝒟 = { ( x , t ) } , \mathcal{D}=\{(x,t)\}, x x is a multimodal query (e.g., text-image input), and t t is x x ’s ground-truth annotation (e.g., answer or solution).

[23] p: Policy Model: The policy model π θ \pi_{\theta} is an MLLM parameterized by θ \theta . Given a query x x , π θ \pi_{\theta} can generate a response: y ∼ π θ ( ⋅ ∣ x ) . y\sim\pi_{\theta}(\cdot\mid x).

[24] p: Verifier: A verifier V V evaluates the quality (e.g., correctness) of a response by taking the query x x , the generated response y y , and the ground truth t t as inputs. It outputs a scalar reward signal: R ⁡ ( x , y ) = V ⁡ ( x , y , t ) . R(x,y)=V(x,y,t). The verifier V V can be instantiated as rule-based programs, powerful MLLMs or human annotations.

[25] h4: 2.1.2. RLVR Workflow: GRPO as an Example

[26] p: We take the famous Group Relative Policy Optimization (GRPO) algorithm to illustrate RLVR’s optimization dynamics. Given a query-ground-truth pair ( x , t ) ∼ 𝒟 (x,t)\sim\mathcal{D} , RLVR proceeds as follows.

[27] p: (1) Experience Sampling. The policy model samples a group of G G responses for x x : { y 1 , … , y G } ∼ π θ ( ⋅ ∣ x ) . \{y_{1},\ldots,y_{G}\}\sim\pi_{\theta}(\cdot\mid x). In this step, the policy explores x x ’s response space to produce diverse experiences.

[28] p: (2) Knowledge Discrimination. The verifier assigns a reward score to each sampled response to discriminate between good and bad experiences: { R 1 , … , R G } , R k = R ⁡ ( x , y k ) = V ⁡ ( x , y k , t ) . \{R_{1},\ldots,R_{G}\},R_{k}=R(x,y_{k})=V(x,y_{k},t).

[29] h5: (3) Advantage Construction.

[30] p: To obtain relative advantages within the sampled group, rewards are normalized: A ⁡ ( x , y k ) = R ⁡ ( x , y k ) − μ x σ x , A(x,y_{k})=\frac{R(x,y_{k})-\mu_{x}}{\sigma_{x}}, where μ x \mu_{x} and σ x \sigma_{x} denote the mean and standard deviation of { R 1 , … , R G } \{R_{1},\ldots,R_{G}\}

[31] h5: (4) Knowledge Internalization.

[32] p: Finally, the policy model updates parameters to increase the generation probability of responses with a positive advantage and decrease the negatives’ generation probability. A standard policy-gradient estimator is formulated as:

[33] table: (1) ∇ θ J ( θ ) ≈ 𝔼 x ∼ 𝒟 , y ∼ π θ ( ⋅ ∣ x ) [ A ( x , y ) ∇ θ log π θ ( y ∣ x ) ] . \nabla_{\theta}J(\theta)\approx\mathbb{E}_{x\sim\mathcal{D},\,y\sim\pi_{\theta}(\cdot\mid x)}\left[A(x,y)\,\nabla_{\theta}\log\pi_{\theta}(y\mid x)\right].

[34] p: Through repeated updates, the policy model internalizes verifier-endorsed patterns as implicit knowledge encoded in θ \theta .

[35] h4: 2.1.3. Brief Summary

[36] p: Overall, RLVR enables the policy model to explore candidate behaviors on multimodal queries, leverages a verifier to distinguish high-quality experiences from low-quality ones, and consolidates the discovered knowledge by shifting generation probabilities via advantage-weighted optimization.

[37] h3: 2.2. Information Bottlenecks in RLVR

[38] p: Despite the success of RLVR in enhancing the internal knowledge and capabilities of MLLMs, we argue that the standard RLVR paradigm suffers from intrinsic information bottlenecks . As formalized in Section 2.1 , the knowledge that the policy model π θ \pi_{\theta} can internalize is determined by: (i) whether π θ \pi_{\theta} can reach informative (ideally correct) solutions during experience generation, and (ii) whether the verifier can reliably identify correctness during experience discrimination. Accordingly, RLVR can bottleneck at either stage.

[39] h4: 2.2.1. Bottleneck I: Reachability of Positive Solutions

[40] p: RLVR relies on policy sampling to produce high-quality experiences. However, when the probability of sampling a correct response is small, the learning signal becomes extremely sparse. Let C ∈ { 0 , 1 } C\in\{0,1\} denote the true correctness of a sampled response y y for query x x , where C = 1 C=1 indicates a positive solution (e.g., correct answer with valid reasoning). Define the per-sample success probability under the current policy as p x ≜ Pr y ∼ π θ ( ⋅ ∣ x ) [ C = 1 ] . p_{x}\triangleq\Pr_{y\sim\pi_{\theta}(\cdot\mid x)}[C=1]. In group-based RLVR, the probability of obtaining at least one positive solution in the group is q x ​ ( G ) ≜ 1 − ( 1 − p x ) G . q_{x}(G)\triangleq 1-(1-p_{x})^{G}. For hard queries, p x p_{x} may be extremely small, yielding q x ​ ( K ) ≈ 0 q_{x}(K)\approx 0 even for moderately large G G . Consequently, sampled groups are often all-negative , i.e., C ⁡ ( y k ) = 0 C(y_{k})=0 for all k k . This regime causes a fundamental bandwidth collapse of the learning signal. Intuitively, the policy receives predominantly “what not to do” feedback, but rarely observes “what to do” exemplars.

[41] h4: 2.2.2. Bottleneck II: Identifiability of Correctness

[42] p: Even if the policy successfully samples candidate solutions, RLVR further depends on the verifier to correctly discriminate good/bad experiences. We highlight that this discrimination can be inherently ambiguous when the verifier operates under restricted context : Let T T denote the context available to the verifier when assessing a response y y for query x x . In typical RLVR practice, the ground-truth signal is often minimal (e.g., only a final answer t t ). In such settings, negative samples that do not match t t can be easy to reject, but false positives may arise: a response may match the final answer while being incorrect in the reasoning process. Formally, identifiability requires that correctness be determined by the verifier’s context, i.e., C C is a deterministic function of T T . When this is not the case, there exists irreducible uncertainty captured by the conditional entropy

[43] table: (2) H ⁡ ( C ∣ T ) > 0 . H(C\mid T)>0.

[44] p: When Eq. ( 2 ) holds, even an optimal verifier cannot perfectly infer the true correctness label under the limited context, and the scalar reward becomes potentially biased and noisy. This bias directly contaminates the advantage signals and reduces training efficiency.

[45] figure: Figure 1. Overview of ContextRL. (a) Context-augmented reward model . (b) Context-augmented policy. (c) Training workflow. method figure

[46] h2: 3. ContextRL: Augmenting RLVR with Context

[47] p: To address the information bottlenecks of RLVR, we propose ContextRL to augment both the policy model and the reward model with additional context. (1) For the reward model, we provide a full solution rather than a minimal final answer, enabling fine-grained process evaluation to reduce false positives. (2) For the policy model, we provide mistake reports and conduct a second-stage generation to increase the reachability of correct solutions

[48] h3: 3.1. Context-Augmented Reward Model

[49] h5: Reward Context: Full Solution vs. Final Answer.

[50] p: Compared to regular ground truth with only the final answer a a , we introduce the full solution s s for each query x x to enrich the reward context, which includes both the reasoning process and the final answer for x x :

[51] table: T 0 = ( x , y , a ) ​ (regular RLVR) , T 1 = ( x , y , s ) ​ (ContextRL) . T_{0}=(x,y,a)\ \text{(regular RLVR)},\qquad T_{1}=(x,y,s)\ \text{(ContextRL)}.

[52] p: Here, a = g ⁡ ( s ) a=g(s) is the final answer in s s . The augmented context T 1 T_{1} provides more comprehensive information compared to T 0 T_{0} , which allows the verifier to perform a finer-grained assessment of the response y y by comparing y y against s s in detail. This results in a reduction of the uncertainty H ⁡ ( C ∣ T 1 ) H(C\mid T_{1}) , improving the identifiability of correctness compared to T 0 T_{0} : H ⁡ ( C ∣ T 1 ) ≤ H ⁡ ( C ∣ T 0 ) , H(C\mid T_{1})\leq H(C\mid T_{0}), with strict inequality when the correctness of the response depends on intermediate steps present in s s but absent from a a .

[53] h5: Context-Augmented Reward Model.

[54] p: Given the augmented reward context ( x , y , s ) (x,y,s) , the reward model now produces two outputs: (i) a scalar reward R ⁡ ( x , y ) R(x,y) for evaluating the correctness of y y , and (ii) a mistake report M ⁡ ( x , y − ) M(x,y^{-}) for each negative sample y − y^{-} , which identifies errors in y − y^{-} . These outputs are computed as:

[55] table: R ⁡ ( x , y ) = r ψ ​ ( x , y , s ) , M ⁡ ( x , y − ) = h ψ ​ ( x , y − , s ) . R(x,y)=r_{\psi}(x,y;s),\quad M(x,y^{-})=h_{\psi}(x,y^{-};s).

[56] p: The mistake report M ⁡ ( x , y − ) M(x,y^{-}) , generated with respect to the full solution s s , explicitly pinpoints the issues in y − y^{-} .

[57] h3: 3.2. Context-Augmented Policy Model

[58] h5: Stage-1: Standard Group Sampling.

[59] p: In stage-1, the policy model samples G G responses { y g } g = 1 G ∼ π θ ( ⋅ ∣ x ) \{y_{g}\}_{g=1}^{G}\sim\pi_{\theta}(\cdot\mid x) for each query x x . These responses are then evaluated by the context-augmented verifier to obtain rewards and mistake reports for negative responses. If at least one positive response is found, the sampling process terminates.

[60] h5: Stage-2: Context-Augmented Sampling.

[61] p: If stage-1 receives an all-negative sample group, we proceed to conduct stage-2 sampling: We append the query x x , each negative response y g − y_{g}^{-} , and its mistake report M g M_{g} into π θ \pi_{\theta} ’s context and initiate a second-round generation:

[62] table: { y g ( 2 ) } g = 1 G ∼ π θ ( ⋅ ∣ x , y g − , M g ) . \{y_{g}^{(2)}\}_{g=1}^{G}\sim\pi_{\theta}(\cdot\mid x,y_{g}^{-},M_{g}).

[63] p: This context-augmented generation process guides π θ \pi_{\theta} to avoid previous issues and increase the chances of sampling positive solutions.

[64] h5: Sample Filtering.

[65] p: After stage-2, we filter the samples to retain only those that meet two criteria: (i) correctness , as verified by the reward model, and (ii) independence , meaning the stage-2 sample does not mention the previous negative response or mistake report. Let 𝒫 ⁡ ( x ) \mathcal{P}(x) represent the set of retained positive samples:

[66] table: 𝒫 ⁡ ( x ) = { y i ( 2 ) : R ψ ​ ( x , y i ( 2 ) , s ) = 1 ​ and ​ y i ( 2 ) ​ is independent } . \mathcal{P}(x)=\left\{y_{i}^{(2)}:R_{\psi}(x,y_{i}^{(2)};s)=1\text{ and }y_{i}^{(2)}\text{ is independent}\right\}.

[67] h3: 3.3. ContextRL’s Optimization Process

[68] p: ContextRL uses two types of training groups for optimization.

[69] h5: Online Training Group.

[70] p: For queries that receive at least one positive response in stage-1, stage-1 samples produce an online training group for π θ \pi_{\theta} (online means no other conditions):

[71] table: G on ​ ( x ) = { ( x , y k ( 1 ) ) } k = 1 K , ∃ k : R ⁡ ( x , y k ( 1 ) ) = 1 . G_{\mathrm{on}}(x)=\{(x,y_{k}^{(1)})\}_{k=1}^{K},\qquad\exists k:R(x,y_{k}^{(1)})=1.

[72] p: This group undergoes training using the standard GRPO objective, with group-relative advantages computed over all samples.

[73] h5: Mixed Training Group.

[74] p: In cases where the stage-1 group contains no positive samples and stage-2 sampling provides high-quality positives, we form a mixed group consisting of both online negatives and offline positives (with y − y^{-} and M M as condition). Specifically, for each stage-2 positive y ∈ 𝒫 ⁡ ( x ) y\in\mathcal{P}(x) , we apply context rollback to remove y − y^{-} and M M and convert it into a single-turn sample ( x , y ( 2 ) ) (x,y^{(2)}) . The mixed training group is defined as:

[75] table: G m = { ( x , y k ) } k = 1 K ⏟ online negatives ∪ { ( x , y ) : y ∈ 𝒫 ⁡ ( x ) } ⏟ offline positives . G_{m}=\underbrace{\{(x,y_{k})\}_{k=1}^{K}}_{\text{online negatives}}\cup\underbrace{\{(x,y):y\in\mathcal{P}(x)\}}_{\text{offline positives}}.

[76] p: The group undergoes optimization using the GRPO objective with scaled advantages for the mixed group and selective KL regularization to handle the offline-stitched positives.

[77] h5: Advantage Scaling.

[78] p: To mitigate the impact of the mixed training group on policy entropy, we scale the advantages for mixed groups:

[79] table: A ~ ​ ( x , y ) = λ ​ A ​ ( x , y ) , λ ∈ ( 0 , 1 ) , \widetilde{A}(x,y)=\lambda A(x,y),\qquad\lambda\in(0,1),

[80] p: λ \lambda is a hyperparameter to controls the influence of mixed groups.

[81] h3: 3.4. ContextRL Algorithm

[82] p: Pseudocode 1 describes the full ContextRL pipeline.

[83] figure: Algorithm 1 ContextRL Pipeline 0: Policy π θ \pi_{\theta} ; reward model ( r ψ ) (r_{\psi}) ; dataset 𝒟 \mathcal{D} providing ( x , s ) (x,s) 1: for each query x ∼ 𝒟 x\sim\mathcal{D} do 2: Stage 1 (standard group sampling): { y k ( 1 ) } k = 1 K ∼ π θ ( ⋅ ∣ x ) \{y_{k}^{(1)}\}_{k=1}^{K}\sim\pi_{\theta}(\cdot\mid x) 3: Produce rewards and mistake report: 4: R k ( 1 ) = r ψ ​ ( x , y k , s ) , M − = h ψ ​ ( x , y − , s ) R_{k}^{(1)}=r_{\psi}(x,y_{k};s),\quad M^{-}=h_{\psi}(x,y^{-};s) 5: if ∃ k \exists k s.t. R k ( 1 ) = 1 R_{k}^{(1)}=1 then 6: Online group update: compute advantages on { R 1 ( k ) } \{R_{1}^{(k)}\} and update π θ \pi_{\theta} with GRPO objective 7: else 8: Stage 2 (context-augmented sampling): sample { y k ( 2 ) } k = 1 K ∼ π θ ( ⋅ ∣ x , y − , M ) \{y_{k}^{(2)}\}_{k=1}^{K}\sim\pi_{\theta}(\cdot\mid x,y^{-},M) 9: Filter standalone positives: 𝒫 ( x ) = { y i ( 2 ) : R ( x , y i ( 2 ) ; s ) = 1 and y i ( 2 ) is independent } . \mathcal{P}(x)=\Big\{y_{i}^{(2)}:{R}(x,y_{i}^{(2)};s)=1\ \ \text{and}\ \ y_{i}^{(2)}\ \text{is independent}\Big\}. 10: Context rollback: form stitched pairs { ( x , y ) : y ∈ 𝒫 ⁡ ( x ) } \{(x,y):y\in\mathcal{P}(x)\} and mixed training group G x G_{x} 11: Mixed group update: compute group-relative advantages on G x G_{x} , scale by λ \lambda , update π θ \pi_{\theta} 12: end if 13: end for

[84] h2: 4. EXPERIMENTS

[85] h3: 4.1. Experimental Setup

[86] h4: 4.1.1. Dataset Construction

[87] p: To construct a training dataset with Reference Solution, we select FineVision ( Wiedmann et al., 2025 ) as the data source. The Policy Model used for optimization is Qwen3-VL 8B Instruct, while the Reward Model is Qwen3-VL 32B Instruct. To validate the generality of ContextRL over tasks, we choose VQA and multimodal math problems to conduct experiments. We select several VQA dataset (e.g., ArXivQA ( Li et al., 2024b ) , ThinkLite ( Wang et al., 2025c ) , AI2D ( Kembhavi et al., 2016 ) ) and several Math dataset (e.g., MMK12 ( Meng et al., 2025 ) , GEOQA ( Chen et al., 2021 ) ) from FineVision. The candidate dataset consists of approximately 250,000 data instances each with query and final answer. We then filter all instances based on accuracy ( Cui et al., 2025a ) : For each instance, four responses are generated by the Policy Model, and the Reward Model evaluates their correctness according to the ground truth. Instances with all correct responses are filtered out. The remaining instances are then re-sampled using the stronger Reward Model to generate positive samples. From these positive samples, the Reward Model selects the optimal solution as the reference solution for enhancing reward modeling context. To balance the difficulty, the data is categorized based on the number of correct responses generated by the Policy Model, ensuring an equal number of samples in each category. Ultimately, the training dataset consists of 16K VQA instances and approximately 14K multimodal math instances, each containing a multimodal query, a reference solution, and its final answer.

[88] h4: 4.1.2. Benchmarks

[89] p: To comprehensively evaluate the effect of ContextRL in enhancing the perception and reasoning capabilities of MLLMs, we select the corresponding two types of benchmarks. For perception evaluation, we choose five benchmarks: SimpleVQA ( Cheng et al., 2025 ) , MMStar ( Chen et al., 2024a ) , HallusionBench ( Guan et al., 2024 ) , HRBench8K ( Wang et al., 2025b ) , and MME-RealWorld-lite ( Zhang et al., 2024b ) . MMStar primarily evaluates the general capabilities of MLLMs across multiple dimensions, HallusionBench and SimpleVQA focus on assessing hallucinations in generated outputs, while HRBench8K and MME-RealWorld-Lite examine the performance of MLLMs in high-resolution scenarios. For reasoning evaluation, we select six benchmarks: MathVerse ( Zhang et al., 2024a ) , MathVista ( Lu et al., 2024 ) , LogicVista ( Xiao et al., 2024 ) , We-Math ( Qiao et al., 2024 ) , CharXiv-RQ ( Wang et al., 2024b ) , and DynaMath ( Zou et al., 2024 ) . MathVerse, MathVista, and We-Math target visual mathematical reasoning, emphasizing fine-grained understanding and multi-step reasoning, LogicVista focuses on visually grounded logical reasoning, systematically assessing models’ abilities in inductive, deductive, spatial, and symbolic reasoning tasks. CharXiv-RQ evaluates scientific chart reasoning, and DynaMath tests MLLMs’ consistency under dynamic visual and textual scenarios.

[90] h4: 4.1.3. Baselines

[91] p: To validate the effectiveness of ContextRL in enhancing policy model’s knowledge compared with SFT paradigm and other RLVR methods, we adopt the following baselines:

[92] p: (1) SFT: We directly fine-tune the policy model using the reference solutions as training targets. This process is equivalent to distilling knowledge from the reward model, which acts as a teacher, combined with rejection sampling on the policy model.

[93] p: (2) GRPO ( Shao et al., 2024 ) : As introduced earlier (Section 5.2 ), GRPO is the most commonly applied RLVR approach, which improves the accuracy of the policy model by computing intra-group relative advantages and applying policy gradient optimization.

[94] p: (3) DAPO ( Yu et al., 2025 ) : DAPO is a well-known variant of GRPO that enhances training stability and learning efficiency through multiple techniques including clip-shifting, dynamic sampling, token-level policy gradient Loss, and overflowing reward shaping.

[95] p: (4) Qwen3-VL 32B Instruct: Qwen3-VL 32B Instruct is the largest dense model in the Qwen3-VL open-source family and significantly outperforms Qwen3-VL 8B Instruct across a wide range of tasks.

[96] h4: 4.1.4. Implementation Details

[97] p: For all our training experiments, we adopt the QwenVL-3-8B-Instruct model as the policy model and QwenVL-3-32B-Instruct as the reward model, with their maximum pixel budgets set to 3M and maximum response lengths capped at 16k tokens. During SFT, the model is trained on 29K samples for 5 epochs, with a learning rate of 1e-5 and a global batch size of 128.

[98] p: For ContextRL and GRPO, the KL divergence loss coefficient β \beta is set to 0.01. The global batch size is configured to 128, the sampling group size to 8, and the learning rate to 1e-6. All reinforcement learning experiments are conducted for a single training epoch. In both SFT and RL phases, we employ the AdamW optimizer ( Loshchilov and Hutter, 2017 ) with a cosine_with_min_lr learning rate scheduler and a warm-up ratio of 0.03. All SFT and RL training is performed on 8 NVIDIA H800 GPUs using the ms-swift framework ( Zhao et al., 2025b ) .

[99] p: All the evaluation is carried out via VLMEvalKit framework, with GPT-4o ( Hurst et al., 2024 ) judging model generated solutions’ correctness. For SFT, we select the checkpoint exhibiting the highest average performance across the 5 training epochs; for RL methods, we directly report results from the single-epoch checkpoint.

[100] figure: Table 1. Performance comparison of different models on perception and reasoning Benchmarks. We report the evaluation metrics on each split of the benchmark to provide a fine-grained presentation of the models’ performance. Optimal and sub-optimal performance for each metric is denoted in bold and underlined fonts, respectively. Perception Benchmarks Benchmark SimpleVQA MMStar HallusionBench HRBench8K MME-Real-lite Avg. split overall overall aAcc fAcc qAcc single cross overall percept reason Qwen3-VL 8B 44.93 64.06 71.08 53.46 53.19 79.00 61.00 70.00 54.66 41.73 59.31 SFT 46.14 70.87 74.97 56.36 56.48 67.75 70.00 71.88 55.95 50.27 62.07 GRPO 46.86 71.87 75.50 58.09 55.60 80.50 70.25 75.38 57.83 50.67 64.25 DAPO 47.62 72.00 75.29 60.98 54.73 82.25 68.75 75.50 58.51 51.73 64.74 ContextRL 48.35 73.00 75.71 60.40 56.48 80.75 70.50 75.63 58.17 53.20 65.22 Qwen3-VL 32B 53.07 74.53 75.08 55.49 55.38 79.25 70.50 74.88 57.14 45.73 64.10 Reasoning Benchmarks Benchmark MathVerse MathVista LogicVista We-Math CharXiv-RQ DynaMath Avg. split mini mini overall strict loose chart general overall worst overall Qwen3-VL 8B 60.50 76.80 56.82 55.33 72.67 50.36 45.68 46.00 39.52 67.49 57.12 SFT 64.82 76.80 59.06 55.43 73.52 48.38 47.95 47.80 38.32 67.37 57.94 GRPO 64.64 78.80 57.04 61.62 75.90 47.32 43.66 44.90 40.11 67.80 58.17 DAPO 65.17 77.70 60.85 63.81 78.67 51.29 51.13 48.90 41.17 68.08 60.68 ContextRL 69.34 78.90 60.40 64.48 81.24 51.75 51.23 50.40 47.52 68.42 62.37 Qwen3-VL 32B 69.40 82.40 62.20 63.52 78.00 55.06 58.24 55.20 49.70 76.53 65.03

[101] h3: 4.2. Main Results

[102] p: In Table 1 , we present the performance of ContextRL and other baselines on five perception benchmarks and six reasoning benchmarks. From these results, we draw the following conclusions:

[103] p: (1) ContextRL yields significantly larger performance gains. Across all perception benchmarks, ContextRL achieves the best or second-best results. On most reasoning benchmarks, it attains the second-best performance, only behind Qwen3-VL 32B Instruct, while on We-Math, ContextRL outperforms Qwen3-VL 32B Instruct. Moreover, ContextRL consistently surpasses SFT and the other two RLVR methods. We attribute this advantage to ContextRL’s ability to break the information bottleneck inherent in RLVR systems.

[104] p: (2) ContextRL demonstrates generality across tasks. ContextRL delivers consistent performance improvements on both perception and reasoning tasks. On perception benchmarks, it improves the average performance of Qwen3-VL 8B by 5.91%, while on reasoning benchmarks, it achieves a 5.25% gain. In contrast, SFT, GRPO, and DAPO tend to yield larger improvements on simpler perception tasks, whereas ContextRL exhibits comparable gains across both task categories, validating its generality. We attribute this to ContextRL’s use of multi-round sampling to enhance the reachability of positive samples for hard instances, thereby providing richer reward signals in challenging reasoning tasks.

[105] p: (3) ContextRL is robust to the quality of reference solutions. We observe that directly applying SFT with reference solutions can result in unchanged or even degraded performance on certain benchmarks (e.g., HRBench8K, MathVistaMini, and DynaMath). This suggests potential dataset bias across benchmarks, as well as suboptimal quality in some reference solutions generated by the reward or policy models. In contrast, by incorporating reference solutions as contextual information for reward modeling, ContextRL achieves stable performance improvements, indicating strong robustness to the quality of reference solutions.

[106] p: (4) Divergence between perception and reasoning tasks. Improving Qwen3-VL 8B’s performance on perception tasks is easier compared to more complex reasoning tasks. The Qwen3-VL 8B model trained with ContextRL surpasses the Qwen3-VL 32B on perception tasks, but still lags behind on reasoning tasks. The difficulty of reasoning tasks results in a larger performance gap between the initial 8B and 32B models, and RL training brings less performance improvement on reasoning benchmarks. We attribute this to the small scale of mathematical instances in our training data. We are working to conduct experiments with more reasoning training data to achieve more significant improvements.

[107] h3: 4.3. Analysis Experiments

[108] h4: 4.3.1. Context-augmented reward modeling significantly improves error detection.

[109] p: We first evaluate the reliability of our context-augmented reward model in identifying ‘false positives’: responses that arrive at the correct final answer through flawed reasoning. To establish an evaluation dataset for analysis, we collect responses rejected by our ContextRL reward model. We cross-verify these negatives with Qwen3-VL-235B-Insturct and retain only those consistently classified as negative by both models, labeling them as High-Confidence False Positives . To validate this automated classification, we manually inspected a random subset of 1,000 such samples. Human verification confirmed that 95.8% of these samples indeed contained reasoning errors or hallucinations. And we take 30k false-positive responses for the following experiment.

[110] p: To validate the effective of context augmentation for detecting false positives, we investigate the impact of different reference information in the context on reward modeling. We select Qwen3-VL 32B and Qwen3-VL 235B as reward models and test them under three context settings: (1) no reference provided (w/o ref), (2) final answer as reference (w. answer), and (3) full solution as reference w. solution. The models are required to judge the correctness of the high-confidence false-positive samples. We report the ratio of samples that are identified as wrong by the reward models in Table 2 .

[111] p: The results show that the proportion of false-positive samples identified as errors increases with the amount of reference information. The higher identification rate supports our hypothesis that additional reference information results in a reduction of uncertainty ( H ⁡ ( C ∣ T ) H(C\mid T) ). We further observe that, as the reference information increases, the performance gap between the 32B and 235B reward models gradually narrows. This indicates that, given sufficient in-context reference information, smaller models can achieve reward accuracy comparable to that of larger models. This holds significance for developing of efficient MLLM RL system.

[112] figure: Table 2. Reward Accuracy Analysis: The proportion of identified high-confidence false-positive samples under different reward models across context settings. Reward Model w/o ref w. answer w. solution Qwen3-VL 32B 46.25 50.03 81.98 Qwen3-VL 235B 51.25 54.60 82.12

[113] figure: Table 3. Model performance after SFT with different proportions of false-positive samples in the training data. Benchmark MME-Real MMStar HRBench8K MathVista We-Math split lite overall overall mini strict Qwen3-VL 8B 49.61 64.06 70.00 76.80 59.14 all positive 53.93 72.87 73.25 78.60 63.05 w 10% false 53.88 73.93 73.00 78.30 62.76 w 20% false 54.72 73.00 73.50 78.30 61.33 w 30% false 53.41 72.47 73.49 77.00 61.29

[114] h4: 4.3.2. The influence of false-positive samples

[115] p: To demonstrate the impact of reducing false-positive samples on model training, we conduct SFT experiments: We mix the false-positive samples with positive samples generated during training to construct 50k training datasets containing different proportions of false positives (ranging from 0% to 30%). We train the policy model using different versions of the datasets and examine the models’ performance.

[116] p: Table 3 shows that training data consisting entirely of positive samples yields the largest performance gains. As the false-positive samples increases, model performance degrades on most benchmarks, with pronounced declines on reasoning benchmarks, MathVista and We-Math. This indicates that eliminating false-positive samples is of significant importance for improving the model’s knowledge discovery efficiency and ability. However, there are also cases (e.g., HRBench8K) where the impact of false-positive samples is limited or even slightly beneficial. This phenomenon is related to task difficulty and evaluation protocols, as false-positive issues may also exist in the evaluation process (e.g., multiple-choice questions where correctness is determined by the final option).

[117] p: The SFT experiments further indicate that positive samples generated by the policy model itself lead to better learning outcomes than directly using reference answers as training targets. We attribute this advantage of policy-generated positive samples to three main factors. First, they undergo stricter correctness evaluation than the reference solutions provided as in-context guidance. Second, they are more diverse: a single query can yield multiple positive samples, whereas only one reference solution is available. Third, they exhibit closer proximity to the policy model, making the self-generated samples easier for the model to learn from.

[118] h4: 4.3.3. Quantizing the information gain of ContextRL

[119] p: In the Appendix A.1 , we quantize the information gain introduced by ContextRL from: (1) the context-augmented reward model corrects the rewards of false-positive samples; (2) context-augmented policy sampling provides non-zero advantages and gradients for all-negative groups. Accordingly, the information gain of ContextRL is formulated as ℐ ContextRL = ρ f ​ p + ρ r . \mathcal{I}_{\mathrm{ContextRL}}=\rho_{fp}+\rho_{r}. Here, ρ f ​ p \rho_{fp} denotes the fraction of false positives eliminated by the context-augmented reward system, and ρ r \rho_{r} denotes the fraction of queries with positive samples recovered from stage-2 sampling among all queries in the training process.

[120] p: Using the strategy for identifying false positives (Sec 4.3.1 ), we statistic the proportion of false positive samples in a single training epoch of ContextRL. An epoch of ContextRL generates approximately 230K responses (29K queries * 8 responses per query), of which 51.12% are judged as negative by the context-augmented reward model, totaling 118K. Among these samples, we identify 20.6K false-positive samples, which account for 8.9% of the total samples. During the training process, 8.56% of the queries obtain positive samples from the stage-2 sampling. Considering that eliminating false positive samples would increase the proportion of all-negative groups in stage-1, the information gain of ContextRL compared to regular RLVR is approximately 17%.

[121] p: Our statistic results indicate a significant reward hacking issue in the traditional RLVR training process, where the policy model’s reasoning contains mistakes, yet it produces answers that are consistent with the ground truth. Furthermore, compared to DAPO, which directly discards the all-negative group, ContextRL recovers these discarded samples by providing positive samples for difficult queries, resulting in a greater information gain.

[122] figure: Table 4. Ablation Study:In the table, CAR denotes context-augmented reward. CAS denotes context-augmented sampling. w/o report indicates that the mistake report is not provided, and w/o scale indicates that advantage scaling is not applied. Method SimpleVQA MMStar HallusionBench HRBench8K DynaMath MathVista LogicVista We-Math Avg. ContextRL 48.35 73.00 64.20 75.63 68.42 78.90 60.40 64.48 66.67 w/o CAR 47.02 72.13 63.13 73.00 69.64 78.60 55.93 58.19 64.71 w/o CAS 46.68 71.27 62.90 74.38 69.58 77.90 55.48 62.86 65.13 w/o report 46.70 73.07 63.29 74.63 70.16 78.50 60.36 64.10 66.35 w/o scale 47.15 72.80 63.64 78.25 68.22 78.80 59.13 61.90 66.24

[123] figure: Figure 2. False Positive Example (Hallucination).

[124] h3: 4.4. Ablation Study

[125] p: In Table 4 , we present a performance comparison between ContextRL and its four variants: (1) without context-augmented reward model : we replace the full solution in the reward model’s context with the final answer; (2) without context-augmented policy sampling : we remove the multi-stage sampling procedure of ContextRL and perform only stage-1 sampling; (3) without mistake report : during stage-2 sampling, we do not provide the policy model with explicit mistake reports, and instead directly ask it to correct the erroneous stage-1 responses; (4) without advantage scaling for mixed training groups : for mixed groups containing stage-2 positive samples, we calculate loss using the unscaled GRPO advantage.

[126] p: Our ablation study shows that the reference solution in the reward model’s context brings the largest performance gain to ContextRL, further highlighting the importance of eliminating false positive samples and avoiding reward hacking in RL training. Removing multi-turn sampling and directly discarding hard queries also leads to performance degradation, which is particularly pronounced on reasoning benchmarks, indicating that providing positive samples for difficult data helps the policy model overcome its knowledge limitations. Moreover, providing no mistake report reduces the policy model’s accuracy on hard samples, thereby decreasing the information gain. Finally, advantage scaling for mixed training groups contributes to improved training stability by reducing the influence of offline positive samples.

[127] h3: 4.5. Reward Hacking Case Study

[128] p: As shown in Figure 2 , the model is tasked with counting horses in a landscape. While the final count ( 4 4 ) matches the ground truth, the intermediate reasoning reveals a severe hallucination. The model fails to identify a clearly visible horse on the far left but compensates for this count by fabricating a non-existent “fourth horse” in the lower right corner, describing it as “partially blocked by the fence.” This suggests the model may be gaming the counting objective by generating plausible-sounding descriptions for features that do not exist, rather than performing genuine visual grounding.

[129] h2: 5. RELATED WORKS

[130] h3: 5.1. MLLMs and Knowledge Discovery

[131] p: Multi-Modal Large Language Models (MLLMs) have undergone rapid evolution in both architecture and training paradigms, progressing from early dual-encoder alignment models to modern MLLMs with strong generative reasoning abilities. Early work typically learned joint visual–text representations via contrastive objectives, enabling robust cross-modal retrieval and transferable visual semantics (e.g., CLIP-style pretraining) ( Radford et al., 2021 ; Zhai et al., 2023 ) . More recent MLLMs integrate a vision encoder with an auto-regressive language model, often through learnable adapters or projectors, and exhibit emergent capabilities in multimodal understanding, grounded generation, and multi-step reasoning ( Team et al., 2025a ; Team, 2025 ; Bai et al., 2025 ) .

[132] p: This line of progress is closely related to knowledge discovery ( Cios et al., 1998 ) . First, MLLM representations can be viewed as implicitly discovering structured regularities from large-scale multimodal corpora and storing them in parameters. Such implicit knowledge is later extracted through text generation (or probing), making MLLMs both repositories and interfaces of multimodal knowledge ( Gu et al., 2025 ; Xue et al., 2025 ) . Second, MLLMs have also been explicitly connected to knowledge graphs (KGs) and knowledge discovery tasks ( Pan et al., 2024 ; Luo et al., 2024 ; Farquhar et al., 2023 ) . Multimodal encoders provide unified embeddings for entities and relations grounded in both textual and visual evidence, which benefits KG completion and link prediction under sparse or ambiguous descriptions ( Chen et al., 2024b ) .

[133] p: From a training perspective, contemporary MLLMs pipelines typically follow a two-stage recipe ( Fu et al., 2025 ; Bai et al., 2025 ) . In the pretraining stage ( Liu et al., 2023 ; Bai et al., 2023 ) , models ingest broad and noisy web-scale data to acquire general world knowledge and aligned cross-modal representations. In the post-training stage ( Team et al., 2025b ; Team et al., 2025a ) , models improve knowledge utilization and controllability by increasing supervision quality and signal richness, including curated instruction tuning, preference optimization, and alignment objectives. This paper follows this trend and focuses on improving the efficiency of knowledge discovery during post-training , especially when reinforcement learning is used to internalize verifier-endorsed knowledge.

[134] h3: 5.2. Reinforcement Learning for MLLMs

[135] p: Inspired by the success of reinforcement learning (RL) in aligning and enhancing reasoning in large language models ( Liu et al., 2024 ; OpenAI, 2025 ) , RL has become an important tool for improving MLLMs’ perception ( Zhang et al., 2026 ) and reasoning synergy ( Team, 2025 ; Team et al., 2025a ) and decision-making under interaction ( Li et al., 2026 ; Lu et al., 2025a ) . Compared to supervised fine-tuning ( Liu et al., 2023 ; Li et al., 2024a ) , RL optimizes behavior by exploring the response space and exploiting evaluative feedback, which is widely believed to offer stronger generalization ( Huang et al., 2025 ; Zheng et al., 2025b ) when the supervision is weak, sparse, or underspecified.

[136] p: A common practice for MLLM post-training is reinforcement learning with verifiers (RLVR), where the model samples candidate responses and a verifier (rule-based, model-based, or human) assigns rewards. Recent variants further improve stability and sample efficiency via group-based sampling and relative advantage estimation ( Wu et al., 2025 ) (e.g., GRPO-style updates) or via stronger regularization ( Yu et al., 2025 ) and preference-based objectives ( Lu et al., 2025b ; Li et al., 2025 ) . Nevertheless, prior studies have pointed out that RLVR can be limited by the quality and informativeness of the verification signal ( Yue et al., 2025 ) . When the verifier only checks a final answer, optimization may overfit to superficial cues and can fail to encourage correct intermediate reasoning, leading to reward hacking or spurious “correct” solutions.

[137] p: In this work, we emphasize that RLVR may suffer from intrinsic information bottlenecks that hinder knowledge discovery. (i) Reachability bottleneck: for hard queries, correct solutions may be rarely sampled, making learning signals extremely sparse . Existing solutions include increasing the number of samples, curriculum design ( Huang et al., 2025 ) , self-training/rejection sampling ( Wang et al., 2025e ) , or using auxiliary search/tool feedback ( Lai et al., 2025 ; Zhao et al., 2025a ) , but these approaches can be compute-intensive or task-specific. (ii) Identifiability bottleneck: correctness judgment may be fundamentally ambiguous under restricted verification context, resulting in false positives and reward hacking ( Wang et al., 2025a ) . Related directions attempt to provide denser supervision by incorporating process-level signals ( Cui et al., 2025a ) , critique models ( Duo et al., 2026 ) , reflection ( Li et al., 2025 ) , or step-wise rewards ( Guan et al., 2025 ) .

[138] h2: 6. CONCLUSION

[139] p: In this paper, we propose ContextRL , a novel framework to enhance the knowledge discovery efficiency of MLLMs during RL. ContextRL leverages context augmentation to overcome the information bottleneck in conventional RLVR methods. Specifically, (1) ContextRL provides richer reference information to the reward model, improving reward accuracy and mitigating reward hacking; (2) ContextRL supplies explicit mistake reports, increasing the probability that the policy model generates positive samples for hard queries, thereby pushing the upper bound of MLLM knowledge capacity. Experimental results on 11 benchmarks demonstrate that ContextRL consistently outperforms other RLVR methods. Notably, it enables Qwen3-VL 8B to achieve performance comparable to Qwen3-VL 32B, substantially improving the knowledge capability of MLLMs. Further analytical experiments confirm the detrimental impact of reward hacking caused by false-positive samples and validate the effectiveness of incorporating contextual reference information to enhance reward model accuracy. We carefully quantify the information gain introduced by ContextRL and conduct ablation studies to verify the effectiveness of each component. Overall, ContextRL highlights the critical role of context information for broadening MLLM’s knowledge boundaries.

[140] h2: References

[141] h2: Appendix A APPENDIX

[142] h3: A.1. Quantifying the Information Gain of ContextRL

[143] p: In this section, we provide a quantitative analysis of the information gains introduced by ContextRL. We show that ContextRL increases the effective optimization signal through two mechanisms: (i) augmenting reward model’s fidelity to reduce false positives, and (ii) converting ineffective all-negative samples into informative training signals via context-augmented sampling. We formalize both effects under a unified notion of information gain .

[144] h4: A.1.1. Information Gain from Reduced False Positives in Reward Modeling

[145] p: Let C ∈ { 0 , 1 } C\in\{0,1\} denote the true correctness of a sampled response and C ^ \widehat{C} the binary decision induced by the reward model. Under standard RLVR with minimal reference context, the reward system typically exhibits a non-negligible false positive rate:

[146] table: (3) α 0 = Pr ⁡ [ C ^ = 1 ∣ C = 0 ] . \alpha_{0}=\Pr[\widehat{C}=1\mid C=0].

[147] p: Such false positives introduce spurious positive advantages, corrupting the policy-gradient signal.

[148] p: With context-augmented reward modeling, the false positive rate is reduced to α 1 < α 0 \alpha_{1}<\alpha_{0} due to improved identifiability. Let ρ fp = α 0 − α 1 \rho_{\mathrm{fp}}=\alpha_{0}-\alpha_{1} denote the fraction of false positives eliminated context-augmented reward system. We define the reward-model information gain as

[149] table: (4) ℐ RM = ρ fp , \mathcal{I}_{\mathrm{RM}}=\rho_{\mathrm{fp}},

[150] p: which measures the proportion of previously misleading positive signals that are corrected and converted into reliable supervision. This term directly reflects the increase in usable label information provided to the policy optimizer.

[151] h4: A.1.2. Information Gain from Context-Augmented Sampling on All-Negative Queries

[152] p: In GRPO-style RLVR, queries whose sampled group is all-negative yield zero group-relative advantages and therefore contribute no effective gradient signal. ContextRL introduces a context-augmented stage-2 sampling procedure that recovers correct solutions for a subset of these queries. Let ρ r \rho_{r} denote the fraction of queries with stage-2 recovered positives among all queries in the overall training process.

[153] p: For each group with G G stage-1 negatives, stage-2 positives transform these zero-advantage samples into effective policy-gradient contributors. The information gain from context-augmented sampling is

[154] table: (5) ℐ TS = ρ r . \mathcal{I}_{\mathrm{TS}}=\rho_{r}.

[155] h4: A.1.3. Unified Information Gain Expression

[156] p: Combining the two effects, we define the total information gain introduced by ContextRL as

[157] table: (6) ℐ ContextRL = ρ fp ⏟ reward modeling gain + ρ r ⏟ two-stage sampling gain \boxed{\mathcal{I}_{\mathrm{ContextRL}}=\underbrace{\rho_{\mathrm{fp}}}_{\text{reward modeling gain}}+\underbrace{\rho_{r}}_{\text{two-stage sampling gain}}}

[158] p: In particular, ContextRL (i) suppresses misleading gradients caused by false positives, and (ii) activates previously dormant queries by converting all-negative samples into effective learning opportunities.

[159] h3: A.2. Instructions for Different Tasks

[160] p: In Figure A-1 and A-2 , we present two types of instructions used to guide our reward model in assessing the correctness of generated samples and in providing error reports. Figure A-1 illustrates the instructions used in regular RLVR, where the final answer is taken as the reference information. Figure A-2 shows the context-augmented instructions employed in ContextRL, in which the full solution is used as the reference information.

[161] figure: Regular Reward Instruction You are an expert in visual question answering. Given a Question, a Reference Answer, and a Generated Solution (with ` reasoning ` and a ` final answer ` in \boxed{} ), evaluate: (1) Self-Consistency; (2) Correctness vs. the image and Reference Answer; if Correctness=0, write a Mistake Report. 1. **Self-Consistency**: If the reasoning aligns with the final answer, score 1; otherwise score 1. 2. **Correctness** (only if Self-Consistency=1): If no hallucinations/conflicts with the image, reasoning is logically correct, and the final answer matches the Reference Answer in meaning, score 1; else 0. 3. **Mistake Report** (only if Self-Consistency=1 and Correctness=0): Summarize wrong content concisely; do not provide correct facts or reveal the correct final answer. Inputs: #### **Question**: <Input Question> #### **Reference Answer**: <Ref Answer> #### **Generated Solution**: <Gen Solution> ### Output Format (JSON): ⬇ { " Analysis ": brief analysis of self - consistency and correctness , " Self - Consistency ": score1 , " Correctness ": score2 , " Mistake Report ": " mistakes ( if applicable )" } Your Evaluation Result: Figure A-1. Regular reward instruction template. regular reward instruction

[162] figure: Context-Augmented Reward Instruction You are an expert in visual question answering. Given a Question, a Reference Solution, and a Generated Solution (with ` reasoning ` and a ` final answer ` in \boxed{} ), evaluate Self-Consistency and then Correctness. If Correctness=0, provide a Mistake Report. 1. **Self-Consistency:** If pleasantries or revision cues (e.g., "You are absolutely right", "Thank you for your review", "I apologize for my mistake", "re-analyze", "reconstruct", "re-examine") appear, set Self-Consistency=0 and Correctness=0; else Self-Consistency=1 iff reasoning matches final answer (otherwise set both to 0). 2. **Correctness** (only if Self-Consistency=1): Using the image as truth and the Reference Solution as auxiliary, set Correctness=1 iff no hallucinations/conflicts, reasoning is logical, and the final answer matches the Reference Solution’s final answer in meaning; else 0. 3. **Mistake Report** (only if Self-Consistency=1 and Correctness=0): List wrong reasoning content only; **no** evidence, correct facts, or final-answer leakage. Inputs: #### **Question**: <Input Question> #### **Reference Solution**: <Ref Solution> #### **Generated Solution**: <Gen Solution> ### Output Format (JSON): ⬇ { " Analysis ": brief analysis of self - consistency and correctness , " Self - Consistency ": score1 , " Correctness ": score2 , " Mistake Report ": " mistakes ( if applicable )" } Your Evaluation Result: Figure A-2. Context-augmented reward instruction template. context-augmented reward instruction

[163] h3: A.3. Another Case

[164] p: To further investigate the limitations of outcome-based supervision, we visualize representative “false positive” cases. These are instances where the model arrives at the correct final answer (e.g., the correct count or multiple-choice option) but relies on flawed reasoning or hallucinations. In standard reinforcement learning settings that rely solely on outcome verifiers, these responses would receive a positive reward, encouraging the model to reinforce erroneous logic—a phenomenon known as reward hacking.

[165] h5: Logical Inconsistency.

[166] p: Figure A-3 demonstrates a reasoning error in a physics problem regarding magnetic forces. The model correctly selects Option B; however, its derivation contains a fundamental factual error. It incorrectly analyzes the pole orientation in the first pair of magnets as “attraction” (North facing South) when the visual evidence clearly shows “repulsion” (South facing South). The correct final answer is reached only serendipitously.

[167] p: These cases highlight the necessity of the proposed review mechanism. As illustrated in the red text within the figures, our approach successfully detects these reasoning flaws, assigning a negative quality score despite the correct final outcome, thereby preventing the policy from learning these spurious correlations.

[168] figure: Figure A-3. False Positive Example (Reasoning Error).

[169] h2: Instructions for reporting errors

[170] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[171] p: Tip: You can select the relevant text first, to include it in your report.

[172] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[173] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
