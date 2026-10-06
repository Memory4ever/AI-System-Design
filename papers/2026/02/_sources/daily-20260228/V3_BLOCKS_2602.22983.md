[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search

[3] h6: Abstract

[4] p: As Large Language Models (LLMs) are increasingly used, their security risks have drawn increasing attention. Existing research reveals that LLMs are highly susceptible to jailbreak attacks, with effectiveness varying across language contexts. This paper investigates the role of classical Chinese in jailbreak attacks. Owing to its conciseness and obscurity, classical Chinese can partially bypass existing safety constraints, exposing notable vulnerabilities in LLMs. Based on this observation, this paper proposes a framework, CC-BOS, for the automatic generation of classical Chinese adversarial prompts based on multi-dimensional fruit fly optimization, facilitating efficient and automated jailbreak attacks in black-box settings. Prompts are encoded into eight policy dimensions—covering role, behavior, mechanism, metaphor, expression, knowledge, trigger pattern and context; and iteratively refined via smell search, visual search, and cauchy mutation. This design enables efficient exploration of the search space, thereby enhancing the effectiveness of black-box jailbreak attacks. To enhance readability and evaluation accuracy, we further design a classical Chinese to English translation module. Extensive experiments demonstrate that effectiveness of the proposed CC-BOS, consistently outperforming state-of-the-art jailbreak attack methods.

[5] p: Warning: This paper contains model outputs that are offensive in nature.

[6] h2: 1 Introduction

[7] p: Large language models (LLMs) ( Nam et al., 2024 ; Shen et al., 2024b ; Gao et al., 2025 ) have developed rapidly in recent years, demonstrating outstanding performance across tasks such as language understanding and generation ( Dong et al., 2019 ) , machine translation ( Zhang et al., 2023 ) , and code generation ( Nam et al., 2024 ) . However, as these models are increasingly deployed in real-world applications, their potential security risks have become more salient ( Kumar et al., 2023 ; Goh et al., 2025 ) . To mitigate potential abuse, researchers have proposed a range of safety alignment strategies that steer model outputs toward human values ( Hsu et al., 2024 ; Mou et al., 2024 ; Xu et al., 2024b ) , enabling them to reject malicious queries (such as "how to make a bomb"). While such mechanisms reduce the likelihood of harmful exploitation, they also highlight the critical need for safety alignment techniques to ensure the safe and reliable deployment of LLMs.

[8] p: However, prior work has demonstrated that these mechanisms are not unbreakable ( Wallace et al., 2019 ; Paulus et al., 2024 ; Jin et al., 2024 ) . They can circumvent safety constraints through well-designed jailbreak prompts, inducing models to generate harmful or even dangerous content ( Andriushchenko et al., 2024 ; Zheng et al., 2024 ; Li et al., 2024 ; Xu et al., 2024a ; Schwinn et al., 2024 ) . Notably, cross-lingual security researches show significant differences in the vulnerability of LLMs across different language environments ( Wang et al., 2023 ; Deng et al., 2023 ; Yoo et al., 2024 ) . Compared to English, low-resource and non-mainstream languages are more prone to trigger unsafe outputs. This phenomenon is attributed to the uneven distribution of training corpora, which introduces potential security risks ( Shen et al., 2024a ) . This finding suggests that specific languages or contexts may impose even greater challenges for achieving safety alignment in LLMs.

[9] figure: Figure 1: Comparison of jailbreak methods. Unlike prior optimized in modern English (e.g., PAIR/TAP, CL-GSO), our approach exploits a classical Chinese context, formulating an 8D search space with a unified bio-inspired optimization for prompt generation.

[10] p: Against this backdrop, we extend our investigation to the context of classical Chinese. As shown in Figure 1 , prior research has largely concentrated on modern languages, especially English, leaving classical Chinese understudied. Unlike low-resource or non-mainstream languages, which are typically limited by a scarcity of training data ( Shen et al., 2024a ) , classical Chinese, as the formal written language of ancient China, possesses a relatively complete linguistic system and a vast corpus of historical literature. Its available training data primarily comes from ancient texts and possesses distinct stylistic characteristics ( Pulleyblank, 1995 ) that diverge substantially from modern Chinese usage. Moreover, the semantic succinctness, rich metaphors, and inherent ambiguity of classical Chinese ( Xu et al., 2019 ) can undermine the effectiveness of defenses based on keyword or template matching. In addition, the asymmetry in semantic correspondence ( Liu et al., 2022 ; Wei et al., 2024 ; Xu et al., 2019 ) between classical Chinese and modern Chinese heightens the risk of security vulnerabilities when models perform cross-lingual interpretation and generation. Therefore, the security vulnerabilities of Classical Chinese cannot be attributed solely to limited data coverage; rather, they stem from a safety blind spot. While the model fully comprehends the obscure inputs, current safety guardrails optimized for modern languages fail to detect and block harmful intent in this specific context.

[11] p: Based on these observations, this paper proposes a black-box jailbreak framework, CC-BOS , for classical Chinese contexts, as shown in Figure 2 . We formulate jailbreak prompt generation as an eight-dimensional strategy space, covering role identity, behavior guidance, mechanism, metaphor mapping, expression style, knowledge relation, context setting, and trigger pattern. To explore this space, we employ a bio-inspired optimization algorithm based on the fruit fly, which integrates smell search, visual search, and cauchy mutation operator to facilitate automated iterative refinement of the prompt-generation strategy within the classical Chinese context. Furthermore, we design a two-stage translation module to progressively mitigate the metaphorical richness and semantic compression of classical Chinese, thereby ensuring reliable evaluation in cross-lingual scenarios. We conduct systematic experiments on six representative LLMs and demonstrate that our method achieves a nearly 100% attack success rate across all models. The main contributions of this paper are summarized as follows:

[12] p: We propose classical Chinese into the study of adversarial prompt generation and jailbreaks for the first time, thereby establishing a new perspective and extending the scope of LLM security.

[13] p: We propose a black-box jailbreak framework that formalizes prompt generation within an eight-dimensional strategy space and leverages the bio-inspired optimization algorithm to achieve systematic and automated jailbreak prompt generation.

[14] p: We construct a two-stage translation module to progressively mitigate the metaphorical and semantically compressed characteristics of classical Chinese, ensuring consistency and reliability in the model response evaluation process.

[15] p: We conduct systematic experiments on six mainstream black-box LLMs, demonstrating the effectiveness and generality of the proposed framework in practical attack scenarios.

[16] h2: 2 Related work

[17] p: Multilingual Vulnerabilities in LLMs. The difficulty of jailbreaking LLMs exhibits substantial variation across different linguistic environments. Wang et al. (2023) propose XSAFETY, a multilingual security benchmark to systematically evaluate the security of LLMs in ten languages, revealing that they are substantially more prone to generating unsafe content in non-English environments. Shen et al. (2024a) demonstrate that LLMs are more prone to generating harmful content and exhibit lower response relevance in low-resource languages, attributing this vulnerability to the insufficient pre-training data. Deng et al. (2023) construct a multilingual jailbreak benchmark to evaluate the security of LLMs across diverse languages, showing that LLMs are more vulnerable in non-English and low-resource settings, thereby highlighting significant cross-lingual security risks. Yoo et al. (2024) propose Code-Switching Red-Teaming (CSRT), a framework that systematically synthesizes code-switching red-teaming queries and investigates the safety and multilingual understanding of LLMs comprehensively, revealing their vulnerability in low-resource languages.

[18] p: White-box Jailbreak Attacks. Drawing inspiration from adversarial attack techniques originally developed in natural language processing, white-box jailbreaking methods typically leverage gradient information or internal model parameters. Zou et al. (2023) propose the Greedy Coordinate Gradient (GCG) method, which automatically generates adversarial suffixes through greedy and gradient search. Guo et al. (2024) propose COLD-Attack, which adapts the Energy-based Constrained Decoding with Langevin Dynamics (COLD) algorithm to unify and automate the search for adversarial LLM attacks. Jia et al. (2024) propose several enhancements to the GCG framework, including diverse target templates, an automatic multi-coordinate update strategy, and easy-to-difficult initialization. They further develop the I-GCG algorithm, which substantially improved the attack success rate. Hu et al. (2024) propose Adaptive Dense-to-Sparse Constrained Optimization (ADC), a token-level jailbreak method that relaxes discrete token optimization into the continuous space with progressively enforced sparsity, achieving significantly improved efficiency. Geisler et al. (2024) propose a white-box jailbreak method based on Projected Gradient Descent (PGD), which relaxes discrete prompt optimization into continuous space and leverages entropy projection to achieve comparable or superior attack performance to GCG.

[19] p: Black-box Jailbreak Attacks. Black-box jailbreaking methods rely solely on interactive queries with the target LLM, making them more suitable for practical deployment scenarios. Recent studies indicate that black-box jailbreaking methods are evolving towards automated prompt generation and optimization, achieving efficient attacks without reliance on internal information ( Mehrotra et al., 2024 ; Chao et al., 2025 ; Liu et al., 2024c ; Lee et al., 2023 ; Chen et al., 2024 ) . Liu et al. (2024b) propose the Disguise and Reconstruction Attack (DRA), which bypasses safety alignment by disguising harmful instructions and inducing the model to reconstruct them in the reply. Ren et al. (2024) propose the CodeAttack, a framework that evaluates LLMs’ security vulnerabilities by converting natural language instructions into code representations. Huang et al. (2025) propose CL-GSO, a framework that expands the jailbreak policy space by decomposing strategies into basic components and integrates them with genetic optimization, achieving strong success rates in black-box settings. Yang et al. (2025b) propose ICRT, a two-stage jailbreak method based on cognitive heuristics and biases. It effectively bypasses the LLM safety via the "Intent Recognition-Concept Reassembly-Template Matching" strategy.

[20] h2: 3 Methodology

[21] p: This paper proposes a framework, CC-BOS , a framework for automatically generating classical Chinese adversarial prompts for black-box jailbreak attacks. This method systematically sets eight strategic dimensions and leverages the bio-inspired optimization algorithm based on the fruit fly to explore the search space efficiently. Furthermore, we construct a classical Chinese translation model to accurately translate the generated content into English, ensuring that the target model’s responses are understandable.

[22] h3: 3.1 PRELIMINARIES

[23] p: Classical Chinese Context. Classical Chinese is characterized by semantic compression, rigorous syntactic structure, and rich rhetorical devices, which together make it particularly suitable for adversarial prompt generation. Its semantic compression enables complex information to be efficiently expressed within a limited word count, resulting in concise queries. Its inherent polysemy also provides multiple interpretations of the same text that enhance query stealth. The diverse expression styles (e.g., parallel prose) introduce atypical textual forms, complicating the model’s language modeling process. Moreover, rhetorical techniques such as metonymy, allusion, and symbolism can be used for keyword substitution or metaphorical expression. These rhetorical techniques allow modern technical concepts to be naturally embedded in the text, concealing sensitive information and avoiding keyword detection. Finally, the layered grammatical structures and nested cultural logic of classical Chinese provide a foundation for the construction of a multidimensional strategy space. Through the interaction of multidimensional factors such as role identity, the generation of complex and hidden queries can be achieved.

[24] figure: Figure 2: Overall framework of CC-BOS. (Left) A multi-dimensional strategy space generates candidate jailbreak prompts across context, intent, style, and activation timing. (Right) Candidates are iteratively optimized via a bio-inspired search loop, evaluated by a two-stage keyword and semantic-consistency scorer, and guided by fitness signals toward high-performing strategies.

[25] p: Formulation. In this study, we define the multi-dimensional strategy space as a finite Cartesian product

[26] table: 𝒮 = D 1 × D 2 × ⋯ × D m , \mathcal{S}=D_{1}\times D_{2}\times\cdots\times D_{m}, (1)

[27] p: where each D k D_{k} denotes a set of discrete options for the k k -th strategy dimension. A candidate policy combination (i.e., a "fruit fly") can be represented as

[28] table: 𝐬 = ( s 1 , … , s m ) ∈ 𝒮 , s k ∈ D k . \mathbf{s}=(s_{1},\dots,s_{m})\in\mathcal{S},\quad s_{k}\in D_{k}. (2)

[29] p: Given the original query q 0 q_{0} and strategy 𝐬 \mathbf{s} , the prompt generator G G defines a deterministic mapping that produces the candidate adversarial query:

[30] table: q = G ⁡ ( q 0 , 𝐬 ) . q=G(q_{0};\mathbf{s}). (3)

[31] p: The target LLM M M is treated as a black box and returns a response r ∼ M ⁡ ( q ) r\sim M(q) . This response is processed through a two-stage translation module T T to obtain a normalized representation r ~ = T ⁡ ( r ) \tilde{r}=T(r) . The effectiveness of strategy 𝐬 \mathbf{s} is then quantified by a fitness function F ⁡ ( 𝐬 ) F(\mathbf{s}) .

[32] p: Our goal is to identify a high-fitness strategy within the black-box setting:

[33] table: 𝐬 ⋆ ∈ arg ⁡ max 𝐬 ∈ 𝒮 ⁡ F ⁡ ( 𝐬 ) \mathbf{s}^{\star}\in\arg\max_{\mathbf{s}\in\mathcal{S}}F(\mathbf{s}) (4)

[34] p: The optimization is carried out subject to an iteration limit of N N . In addition, an early-stopping threshold τ \tau is employed. The procedure terminates once the best observed fitness value satisfies max ⁡ F ⁡ ( 𝐬 ) ≥ τ \max F(\mathbf{s})\geq\tau , or when the iteration budget N N is exhausted. Upon termination, the algorithm returns the current optimal solution.

[35] p: Translation Module. Since the jailbreak attacks investigated in this paper are primarily based on classical Chinese context, directly evaluating the model’s original responses (which are based on classical Chinese context) can introduce biases in both consistency judgment and keyword detection. To address this, we introduce a translation module in the evaluation phase. This module uniformly translates the model responses into English, ensuring the reliability and robustness of subsequent evaluation.

[36] h3: 3.2 Multi-Dimensional Strategy Space

[37] p: Prior work has demonstrated a wide range of LLM jailbreak strategies, including character identity disguise, scenario nesting, and keyword substitution. However, these strategies are often fragmented and lack a systematic and structured generation framework. As a result, existing efforts in adversarial prompt design and research struggle to comprehensively cover potential attack vectors. More importantly, with the advancement of model security mechanisms, conventional fragmented jailbreak strategies fail to capture the inherent connections and combined effects between strategies, leading to blind spots in security evaluation and defense measures.

[38] p: To this end, we propose a multidimensional strategy space that integrates existing jailbreak techniques with the contextual properties of Classical Chinese. We abstract jailbreak methods into eight core dimensions, formalized as 𝔸 = { D 1 , D 2 , … , D 8 } {\mathbb{A}}=\{D_{1},D_{2},\dots,D_{8}\} , where each D i D_{i} corresponds to a distinct dimension of the proposed strategy space, including Role Identity , Behavioral Guidance , Mechanism , Metaphor Mapping , Expression Style , Knowledge Relation , Contextual Setting , and Trigger Pattern .

[39] p: Building upon these dimensions, we formalize the multidimensional strategy space as a Cartesian product of sets

[40] table: 𝕊 = D 1 × D 2 × ⋯ × D 8 , {\mathbb{S}}=D_{1}\times D_{2}\times\dots\times D_{8}, (5)

[41] p: where each D i D_{i} ( i = 1 , 2 , … , 8 i=1,2,\dots,8 ) represents the set of choices for the i i -th strategy dimension. An element 𝐬 = ( s 1 , s 2 , … , s 8 ) \mathbf{s}=(s_{1},s_{2},\dots,s_{8}) in 𝒮 \mathcal{S} corresponds to a specific combination of strategies, with s i ∈ D i s_{i}\in D_{i} for all i i . The strategy space 𝒮 \mathcal{S} thus encapsulates all possible combinations of strategies, with each combination representing a distinct point in the multidimensional decision space.

[42] h3: 3.3 Bio-Inspired Optimization Algorithm

[43] p: Fruit Fly-Based Bio-Inspired Optimization. We employ the Fruit Fly Optimization Algorithm (FOA), a population-based heuristic inspired by the foraging behavior of fruit flies, as the core of our Fruit Fly-Based Bio-Inspired Optimization framework. Its underlying principle is to iteratively approach optimal point in the search space through smell search and visual search. In our framework, we retain the smell search and visual search operators and introduce cauchy mutation as a complementary mechanism to escape local optima when stagnant. Furthermore, we introduce hash-based deduplication and an early stopping strategy to improve search efficiency and stability.

[44] p: Formally, let the population at iteration t t be P t ⊂ 𝒮 P_{t}\subset\mathcal{S} , and let 𝐬 best t \mathbf{s}^{t}_{\mathrm{best}} denote the best individual identified so far. The iterative update expression is

[45] table: P t ′ = Φ smell ​ ( P t ) , P t ′′ = Φ vision ​ ( P t ′ , 𝐬 best t ) , P t + 1 = { Φ cauchy ​ ( P t ′′ ) , under stagnation , P t ′′ , otherwise . P^{\prime}_{t}=\Phi_{\mathrm{smell}}(P_{t}),\quad P^{\prime\prime}_{t}=\Phi_{\mathrm{vision}}(P^{\prime}_{t},\mathbf{s}^{t}_{\mathrm{best}}),\quad P_{t+1}=\begin{cases}\Phi_{\mathrm{cauchy}}(P^{\prime\prime}_{t}),&\text{under stagnation},\\ P^{\prime\prime}_{t},&\text{otherwise}.\end{cases} (6)

[46] p: where Φ smell , Φ vision , Φ cauchy \Phi_{\mathrm{smell}},\Phi_{\mathrm{vision}},\Phi_{\mathrm{cauchy}} denote the respective operators. The concrete definitions of these operators are provided in the following subsections.

[47] p: Population Initialization. We initialize the population by ensuring both coverage and diversity across the multi-dimensional strategy space. Let each dimension D k D_{k} contain a finite set of options. To guarantee balanced representation, we adopt a coverage-constrained random sampling. Specifically, for each dimension D k D_{k} , we construct a sequence

[48] table: 𝒳 k = { x k , 1 , … , x k , N } , x k , j ∈ D k , \mathcal{X}_{k}=\{x_{k,1},\dots,x_{k,N}\},\quad x_{k,j}\in D_{k}, (7)

[49] p: such that every element in D k D_{k} appears with approximately uniform frequency. This sequence is generated by successively producing random permutations of D k D_{k} and concatenating them until the target length N N is reached.

[50] p: An individual 𝐬 ( j ) \mathbf{s}^{(j)} is then defined as the j j -th element across all dimension sequences

[51] table: 𝐬 ( j ) = ( x 1 , j , x 2 , j , … , x m , j ) , j = 1 , … , N , \mathbf{s}^{(j)}=(x_{1,j},x_{2,j},\dots,x_{m,j}),\quad j=1,\dots,N, (8)

[52] p: yielding the initial population

[53] table: P 0 = { 𝐬 ( 1 ) , … , 𝐬 ( N ) } . P_{0}=\{\mathbf{s}^{(1)},\dots,\mathbf{s}^{(N)}\}. (9)

[54] p: Hash-based deduplication. To eliminate redundant evaluations, we adopt a hash-based deduplication strategy. We first seed a global hash set with P 0 P_{0} and then filter duplicates only when new candidates are proposed during the search. Let h ⁡ ( 𝐬 ) h(\mathbf{s}) be a deterministic key (the tuple of per-dimension indices under a fixed dimension order). We initialize E ← { h ⁡ ( 𝐬 ) ∣ 𝐬 ∈ P 0 } E\!\leftarrow\!\{\,h(\mathbf{s})\mid\mathbf{s}\!\in\!P_{0}\,\} . Whenever an operator Ψ ∈ { Φ smell , Φ vision , Φ cauchy } \Psi\in\{\Phi_{\mathrm{smell}},\Phi_{\mathrm{vision}},\Phi_{\mathrm{cauchy}}\} proposes a candidate 𝐬 ^ \hat{\mathbf{s}} , we accept it if h ⁡ ( 𝐬 ^ ) ∉ E h(\hat{\mathbf{s}})\notin E and then insert h ⁡ ( 𝐬 ^ ) h(\hat{\mathbf{s}}) into E E ; otherwise we resample from the same operator up to R R times and keep the last proposal to maintain population size.

[55] p: Smell Search. Smell search performs adaptive local perturbation around each individual. For the i i -th dimension of strategy 𝐬 ( j ) \mathbf{s}^{(j)} at iteration t t , let i ​ d ​ x ​ ( s i ( j ) ) idx(s^{(j)}_{i}) denote its index in D i D_{i} . We perturb the index by

[56] table: i ​ d ​ x ​ ( s i ( j ) ) ← i ​ d ​ x ​ ( s i ( j ) ) + δ , δ ∼ U ⁡ ( − Δ t , Δ t ) , idx(s^{(j)}_{i})\leftarrow idx(s^{(j)}_{i})+\delta,\quad\delta\sim U(-\Delta_{t},\Delta_{t}), (10)

[57] p: with step bound

[58] table: Δ t = max ⁡ ( 1 , ⌊ α ​ | D i | ⋅ γ t ⌋ ) , \Delta_{t}=\max\left(1,\lfloor\alpha|D_{i}|\cdot\gamma^{t}\rfloor\right), (11)

[59] p: where α ∈ ( 0 , 1 ) \alpha\in(0,1) is the exploration ratio and γ ∈ ( 0 , 1 ) \gamma\in(0,1) controls exponential decay. This mechanism ensures broader exploration in the early stages and progressively refined exploitation as iterations proceed.

[60] p: Vision Search. Vision search directs individuals toward the current global best 𝐬 best t \mathbf{s}^{t}_{\text{best}} . At iteration t t , the attraction probability is defined as

[61] table: β t = β 0 + ( 1 − β 0 ) ⋅ t N , \beta_{t}\;=\;\beta_{0}\;+\;(1-\beta_{0})\cdot\frac{t}{N}, (12)

[62] p: where β 0 ∈ ( 0 , 1 ] \beta_{0}\in(0,1] is the initial attraction strength and N N is the maximum iteration budget. Each dimension s i ( j ) s^{(j)}_{i} is updated by

[63] table: s i ( j ) ← { s best , i t , with probability ​ β t , s i ( j ) , with probability ​ 1 − β t . s^{(j)}_{i}\leftarrow\begin{cases}s^{t}_{\text{best},i},&\text{with probability }\beta_{t},\\[6.0pt] s^{(j)}_{i},&\text{with probability }1-\beta_{t}.\end{cases} (13)

[64] p: This schedule encourages exploration in early iterations while promoting convergence to the global best in later stages.

[65] p: Cauchy Mutation. When stagnation is detected (i.e., no improvement in F ⁡ ( 𝐬 ) F(\mathbf{s}) after K K iterations), we apply a large-scale perturbation via the cauchy distribution. For each dimension i i of strategy 𝐬 ( j ) \mathbf{s}^{(j)} , mutation is applied with probability p mut p_{\mathrm{mut}} , by shifting the index as

[66] table: i ​ d ​ x ​ ( s i ( j ) ) ← ( i ​ d ​ x ​ ( s i ( j ) ) + ⌊ ξ ⌋ ) mod | D i | , ξ ∼ 𝒞 ⁡ ( 0 , λ ) , idx(s^{(j)}_{i})\;\leftarrow\;\big(idx(s^{(j)}_{i})+\lfloor\xi\rfloor\big)\bmod|D_{i}|,\quad\xi\sim\mathcal{C}(0,\lambda), (14)

[67] p: The heavy-tailed nature of cauchy noise induces occasional large jumps, thereby increasing the likelihood of escaping stagnation.

[68] p: Fitness Evaluation. The fitness function F : 𝒮 → ℝ F:\mathcal{S}\to\mathbb{R} quantifies the jailbreak effectiveness of each candidate strategy. Given an individual 𝐬 ∈ 𝒮 \mathbf{s}\in\mathcal{S} , the corresponding adversarial query is q = G ⁡ ( q 0 , 𝐬 ) q=G(q_{0};\mathbf{s}) . Submitting q q to the target model M M yields a response r ∼ M ⁡ ( q ) r\sim M(q) , which is then normalized through a two-stage translation module T T , producing r ~ = T ⁡ ( r ) \tilde{r}=T(r) .

[69] p: The fitness function decomposes into two components, which are the consistency score and the keyword score. We denote by S c ​ ( 𝐬 ) S_{\text{c}}(\mathbf{s}) the alignment between r ~ \tilde{r} and the intended jailbreak instruction q 0 q_{0} . Let ρ ⁡ ( r ~ , q 0 ) ∈ [ 0 , 5 ] \rho(\tilde{r},q_{0})\in[0,5] be the raw compliance score returned by the evaluation model. We scale it linearly:

[70] table: S c ​ ( 𝐬 ) = 20 ⋅ ρ ⁡ ( r ~ , q 0 ) , S c ∈ [ 0,100 ] . S_{\text{c}}(\mathbf{s})=20\cdot\rho(\tilde{r},q_{0}),\quad S_{\text{c}}\in[0,100]. (15)

[71] p: We also incorporate a heuristic indicator S k ​ ( 𝐬 ) S_{k}(\mathbf{s}) based on explicit rejection cues. Let 𝒦 − \mathcal{K}^{-} denote the set of rejection keywords (e.g., refusal markers), and R ⁡ ( r ~ ) R(\tilde{r}) denote the set of tokens in the normalized response r ~ \tilde{r} used for keyword matching. Then the score is defined as:

[72] table: S k ​ ( 𝐬 ) = { 0 , R ⁡ ( r ~ ) ∩ 𝒦 − ≠ ∅ , 20 , R ⁡ ( r ~ ) ∩ 𝒦 − = ∅ . S_{k}(\mathbf{s})=\begin{cases}0,&R(\tilde{r})\cap\mathcal{K}^{-}\neq\emptyset,\\[6.0pt] 20,&R(\tilde{r})\cap\mathcal{K}^{-}=\emptyset.\end{cases} (16)

[73] p: The final fitness score is given by the additive combination:

[74] table: F ⁡ ( 𝐬 ) = S c ​ ( 𝐬 ) + S k ​ ( 𝐬 ) , F ⁡ ( 𝐬 ) ∈ [ 0,120 ] . F(\mathbf{s})=S_{\text{c}}(\mathbf{s})+S_{\text{k}}(\mathbf{s}),\quad F(\mathbf{s})\in[0,120]. (17)

[75] p: The search is terminated once the best fitness score in the population exceeds a threshold τ \tau , or when the maximum number of iterations N N is reached. This termination condition prevents unnecessary iterations, thereby reducing resource consumption and improving search efficiency.

[76] h2: 4 Experiments

[77] h3: 4.1 Experimental settings

[78] p: Datasets. This study adopts the "Harmful Behavior" subset of the AdvBench benchmark ( Zou et al., 2023 ) ) to evaluate the effectiveness of the proposed black-box jailbreaking method. The benchmark originally contains 520 harmful requests involving categories such as abusive language, violent content, misinformation, and illegal activities. Following prior work ( Li et al., 2023 ; Wei et al., 2023a ; Chao et al., 2025 ) , we remove duplicates and select 50 representative requests to form the evaluation set, thereby ensuring fairness and comparability across methods. We also evaluate the proposed CC-BOS method using the Competition for LLM and Agent Safety (CLAS) 2024 Dataset ( Xiang et al., 2024 ) and StrongREJECT datasets ( Souly et al., 2024 ) . The CLAS dataset comprises 100 harmful queries spanning categories such as illegal activity, hate/violence, fraud, and privacy violations, providing challenging jailbreak scenarios. The StrongREJECT dataset assesses a model’s ability to reject high-risk or strongly prohibited requests. For our experiments, we used its streamlined version, StrongREJECT-small, a 60-question subset.

[79] p: Target models. We select Gemini-2.5-flash ( Comanici et al., 2025 ) , Claude-3-7-sonnet-20250219 ( 4 ) , GPT-4o ( Hurst et al., 2024 ) , Deepseek-Reasoner ( Liu et al., 2024a ) , Qwen3-235b-a22b-instruct-2507 ( Yang et al., 2025a ) , and Grok-3 ( xAI, 2025 ) as target models for experiments.

[80] p: Baselines. Our approach is compared with several representative baselines, including PAIR ( Chao et al., 2025 ) , TAP ( Mehrotra et al., 2024 ) , GPTFUZZER ( Yu et al., 2023 ) , AutoDAN-Turbo-R ( Liu and Peiran, 2025 ) , CL-GSO ( Huang et al., 2025 ) , and ICRT ( Yang et al., 2025b ) . All experiments are conducted under the evaluation setting consistent with the original research.

[81] p: Evaluation metrics. To systematically evaluate the attack success rate (ASR) of adversarial prompts, we design an evaluation framework that combines keyword matching with user intent consistency. A template-based detector ( Huang et al., 2025 ) is first applied to identify acceptance and rejection patterns in the output. Subsequently, we employ the judge model proposed by Kuo et al. (2025) , built on GPT-4o, to determine the consistency and compliance between user intent and model responses. Manual review is further conducted to ensure the accuracy of the evaluation. Furthermore, following the judge methodology of Kuo et al. (2025) , we assign quantitative toxicity scores to model responses. We then compute the average toxicity score (Avg.Score) as an aggregate measure to characterize the overall harmfulness of model outputs. We also use the average number of queries (Avg.Q) submitted to the target model to evaluate the efficiency of jailbreak attacks, following the definition in prior work ( Huang et al., 2025 ) .

[82] p: Implementation details. We adopt Deepseek-Chat as both the attack and translation model. Furthermore, we set the initial population size to 5 and the maximum number of iterations to 5. In the evaluation phase using our proposed judge method, a jailbreak is deemed successful if the score reaches or exceeds 80. All experiments were performed on an Ubuntu workstation equipped with two NVIDIA GeForce RTX 4090 GPUs and 125 GB of RAM.

[83] h3: 4.2 Comparisons with other jailbreak attack methods

[84] figure: Table 1: CC-BOS Evaluation on the AdvBench Benchmark and Comparison with Existing Baselines Method Gemini-2.5-flash Claude-3.7 GPT-4o Deepseek-Reasoner Qwen3 Grok-3 ASR Avg.Score ASR Avg.Score ASR Avg.Score ASR Avg.Score ASR Avg.Score ASR Avg.Score PAIR 0% 0.00 2% 0.06 0% 0.00 8% 0.24 0% 0.02 14% 0.52 TAP 0% 0.00 0% 0.00 12% 0.40 6% 0.24 4% 0.12 54% 2.04 GPTFUZZER 28% 1.22 0% 0.04 12% 0.40 24% 1.04 2% 0.06 52% 2.10 AutoDAN-Turbo-R 70% 2.52 74% 2.88 88% 3.18 88% 3.36 88% 3.32 84% 3.10 CL-GSO 80% 2.60 40% 1.86 78% 2.64 50% 1.90 50% 2.00 44% 2.04 ICRT 92% 4.52 40% 1.60 74% 3.06 88% 4.00 84% 4.00 98% 4.30 CC-BOS(Ours) 100% 4.82 100% 3.14 100% 4.74 100% 4.84 100% 4.88 100% 4.76

[85] figure: Table 2: Attack Success Rate (ASR, %) comparison between ICRT and our method on CLAS and StrongREJECT datasets. Dataset Method Gemini-2.5-flash Claude-3.7 GPT-4o DeepSeek-Reasoner Qwen3 Grok-3 CLAS ICRT 96 21 83 89 86 94 Ours 100 99 99 99 99 100 StrongREJECT ICRT 83.33 23.33 71.67 76.67 66.67 93.33 Ours 98.30 98.30 100 98.30 98.30 98.30

[86] figure: Table 3: Average Number of Queries (Avg.Q) for Different Methods Across LLMs on AdvBench Method Gemini-2.5-flash Claude-3.7 GPT-4o Deepseek-Reasoner Qwen3-235b Grok-3 PAIR 60.00 51.12 57.36 40.32 57.00 51.36 TAP 93.14 93.48 65.72 86.44 90.42 53.96 GPTFUZZER 56.96 32.62 77.26 5.98 19.08 1.32 AutoDAN-turbo-R 10.00 14.80 16.84 10.62 13.48 13.58 CL-GSO 3.62 21.42 4.00 3.26 5.06 1.24 CC-BOS(Ours) 1.46 2.38 1.28 1.12 1.54 1.18

[87] p: Comparison results. Table 1 shows the comparative experimental results with other jailbreak attack methods on five representative black-box models. As shown, our proposed method achieves a 100% attack success rate (ASR) across all five black-box models, outperforming all baselines. Furthermore, the average score (quantifying the harmfulness of the model output) also exceeds all baselines. These results indicate our method can not only consistently overcome existing alignment defenses but also reliably induce the model to generate highly harmful outputs. Focusing on the large Chinese model Qwen3, our proposed jailbreak attack method, based on classical Chinese context, achieves a 100% ASR and an Avg.Score of 4.84 in experiments, whereas ICRT attains only 88% ASR and an Avg.Score of 4, which demonstrates that the language distribution shift induced by classical Chinese can materially weaken current Chinese-oriented alignment mechanisms. On the reasoning model Deepseek-Reasoner, our method also achieves 100% ASR and an Avg.Score of 4.84, far surpassing the current best comparison ICRT’s 88% ASR and Avg.Score of 4, further indicating that the classical Chinese context-based jailbreaking method remains highly effective even against the reasoning model. We also evaluate our proposed CC-BOS method on the CLAS and StrongREJECT datasets, comparing it with ICRT, the best-performing baseline on the AdvBench. As shown in Table 2 , CC-BOS achieves an attack success rate (ASR) nearly 100% across five commonly used LLM implementations, substantially outperforming ICRT.

[88] p: Efficiency of Jailbreak Attacks. We evaluate the efficiency of various adversarial attack methods using the average number of queries (Avg.Q). To ensure a fair comparison, only optimization-based jailbreak methods are considered. As shown in Table 3 , our proposed CC-BOS consistently achieves the lowest query count across all evaluated LLMs, outperforming baselines such as AutoDAN-turbo-R and CL-GSO. These results indicate that CC-BOS not only attains high attack success rates but also demonstrates superior query efficiency.

[89] figure: Table 4: Attack Success Rate (ASR) against Llama-Guard-3-8B across multiple models. Defense Claude-3.7 Deepseek-Reasoner Gemini-2.5-flash GPTFUZZER ICRT CC-BOS (Ours) GPTFUZZER ICRT CC-BOS (Ours) GPTFUZZER ICRT CC-BOS (Ours) No Defense 0.00% 40% 100% 24.00% 88% 100% 28.00% 92% 100% Input & Output 0.00% 26% 40.00% 12.00% 2% 28.00% 16.00% 0% 22.00%

[90] p: Attack against Defense. In the defense experiments, we systematically evaluate the performance of CC-BOS against the Llama-Guard-3-8B ( Dubey et al., 2024 ) defense mechanism. As shown in Table 4 , in the absence of defenses, CC-BOS achieves a 100% attack success rate (ASR) on all evaluated models, significantly outperforming GPTFUZZER and ICRT. Under the more challenging dual-defense setting, where both input and output filtering are applied, the overall ASR performance declines; CC-BOS maintains the highest success rate (e.g., reaching 40% on Claude-3.7) while consistently eliciting highly harmful outputs, demonstrating its robustness and ability to overcome defense mechanisms.

[91] h3: 4.3 Transferability of different models

[92] figure: Table 5: Cross-Model Transferability of CC-BOS (ASR, %) Source \ \backslash Target Gemini-2.5-flash GPT-4o DeepSeek-Reasoner Qwen3 Grok-3 Gemini-2.5-flash 100 88 76 80 84 GPT-4o 82 100 88 92 88 DeepSeek-Reasoner 82 78 100 90 84 Qwen3 90 88 76 100 96 Grok-3 84 86 90 90 100

[93] p: We conduct a systematic study of cross-model adversarial transferability, where adversarial examples are generated from each of five widely adopted LLMs (Gemini-2.5-flash, GPT-4o, Deepseek-Reasoner, Qwen3, and Grok3) as source models and subsequently evaluated on the remaining models as targets. As shown in Table 5 , our method demonstrates robust cross-model adversarial transferability, maintaining consistently great attack success rates across diverse models. Adversarial examples generated by GPT-4o achieve consistently high success rates on multiple target models (up to 92%), highlighting the strong cross-model transferability of our method. Moreover, adversarial examples generated by Qwen3 exhibit remarkable transferability, achieving a success rate of 96% on Grok3 and 90% on Gemini-2.5-flash. Similarly, Grok3 demonstrates stable transferability across diverse targets, with success rates ranging from 84% to 90%. Overall, these results demonstrate that our method can generate highly transferable and stable adversarial examples.

[94] h3: 4.4 Ablation Study

[95] figure: Table 6: Ablation study of the proposed method. Ablation Description ASR (%) Base Classical Chinese (CC) 18 + Strategy CC + Strategy 60 + Bio-Inspired Opt. CC + Strategy + BIO (CC-BOS) 100 Eval. w/o Translated Module 90 Eval. + Translated Module 100

[96] p: Ablation of CC-BOS. To evaluate the contribution of each module to the final method, we evaluate the attack success rate (ASR) on Claude-3.7 using the AdvBench test set. We conduct a stepwise ablation of three components: classical Chinese context (CC), multidimensional strategy (strategy), and bio-inspired optimization (BIO). Table 6 shows that introducing the multidimensional strategy (Base → + Strategy) improves the ASR from 18% to 60%, highlighting the critical role of strategy design in steering the model toward inappropriate outputs. Further combining this with bio-inspired optimization (forming CC-BOS) improves the ASR to 100%, demonstrating that the optimization module effectively synergizes with the strategy module to search for the optimal combination, significantly improving the jailbreak success rate. The integration of three components achieves the highest jailbreak attack success rate.

[97] p: Ablation of Evaluation Process. To assess the effect of the translation module on the evaluation process, we conduct a controlled comparison. As shown in Table 6 , when the translation module is removed, the attack success rate (ASR) measured by our evaluation process is 90%. Adding the translation module and refining the evaluation pipeline raises the ASR to 100%. This result indicates that the translation module substantially enhances the reliability of model response assessments, improving both the consistency and accuracy of the evaluation outcomes.

[98] h2: 5 Conclusion

[99] p: We propose CC-BOS , a novel jailbreak approach for LLMs that leverages the unique linguistic characteristics of classical Chinese. We first formalize an eight-dimensional strategy space based on the classical Chinese context and existing jailbreak strategies, covering role, behavior, mechanism, metaphor, expression, knowledge, trigger pattern and context. To efficiently explore this space, we propose a bio-inspired optimization algorithm, inspired by fruit fly foraging behavior, which enables automated and effective generation of adversarial prompts by balancing global exploration and local exploitation. In addition, we design a two-stage translation module to ensure a more objective and robust evaluation of model responses. By integrating these components, we develop a high-performance and stable jailbreaking method. We conduct extensive experiments across multiple LLMs to validate the effectiveness of our proposed method. The results demonstrate that CC-BOS consistently outperforms existing jailbreak methods in success rate.

[100] h2: Ethics statement

[101] p: This paper proposes a jailbreak attack method based on the context of classical Chinese context, multidimensional strategy space and a bio-inspired optimization algorithm. While such a method may generate harmful content and entail potential risks, our work, which is consistent with prior research on jailbreak attacks, is intended to probe the vulnerabilities of large language models (LLMs) rather than to encourage malicious use. By exploring this novel linguistic context, our work guide future work in enhancing the adversarial defense of LLMs. All experiments are conducted on a closed-source victim model. The research on adversarial attacks and defenses is essential for collaboratively shaping the landscape of AI security.

[102] h2: Acknowledgement

[103] p: This work is supported in part by the “Pioneer” and “Leading Goose” R&D Program of Zhejiang No.2025SSYS0005; by the National Research Foundation, Singapore, and DSO National Laboratories under the AI Singapore Programme (AISG Award No: AISG4-GC-2023-008-1B); by the National Research Foundation Singapore and the Cyber Security Agency under the National Cybersecurity R&D Programme (NCRP25-P04-TAICeN); . This research is also part of the IN-CYPHER Programmeand is supported by the National Research Foundation, Prime Minister’s Office, Singapore, underits Campus for Research Excellence and Technological Enterprise (CREATE) Programme. Any opinions, findings and conclusions, or recommendations expressed in these materials are those of the author(s) and do not reflect the views of the National Research Foundation, Singapore, Cyber Security Agency of Singapore, Singapore.

[104] h2: References

[105] h2: Appendix A The Use of Large Language Models (LLMs)

[106] p: In this work, we leverage a large-scale language model (LLM) to assist in manuscript writing and refinement, aiming to enhance readability and precision. All LLM polished content is carefully reviewed to ensure it meets our requirements, with adjustments applied as needed. The LLM is also employed to support literature retrieval. In practice, we rely primarily on conventional search methods, while also leveraging the LLM to discover and locate relevant literature. Recognizing that LLMs may produce inaccurate or spurious information (i.e., “hallucinations”), we rigorously verify all retrieved literature to ensure both accuracy and relevance to our research objectives.

[107] h2: Appendix B Bio-Inspired Optimization Algorithm

[108] p: In this appendix, we detail the main components of the proposed Bio-Inspired Optimization Algorithm (inspired by the fruit fly). The following algorithms describe the initialization strategy, uniqueness-preserving resampling, and the core search operators. The overall process is shown in Algorithm 1 .

[109] figure: Algorithm 1 Formalized FOA for Jailbreak Optimization 1: Input: Initial query q 0 q_{0} , maximum iteration budget N N , population size | P | |P| , stagnation threshold K K , early-stop threshold τ \tau 2: Output: Best strategy 𝐬 ∗ \mathbf{s}^{*} 3: Initialize population P 0 = { 𝐬 ( 1 ) , … , 𝐬 ( | P | ) } P_{0}=\{\mathbf{s}^{(1)},\dots,\mathbf{s}^{(|P|)}\} 4: Initialize hash set E ← { h ⁡ ( 𝐬 ) ∣ 𝐬 ∈ P 0 } E\leftarrow\{h(\mathbf{s})\mid\mathbf{s}\in P_{0}\} 5: Evaluate fitness F ⁡ ( 𝐬 ) F(\mathbf{s}) for all 𝐬 ∈ P 0 \mathbf{s}\in P_{0} ; set 𝐬 best 0 ← arg ⁡ max 𝐬 ∈ P 0 ⁡ F ⁡ ( 𝐬 ) \mathbf{s}^{0}_{\text{best}}\leftarrow\arg\max_{\mathbf{s}\in P_{0}}F(\mathbf{s}) 6: for t = 0 , 1 , … , N − 1 t=0,1,\dots,N-1 do 7: if F ⁡ ( 𝐬 best t ) ≥ τ F(\mathbf{s}^{t}_{\text{best}})\geq\tau then 8: return 𝐬 best t \mathbf{s}^{t}_{\text{best}} 9: end if 10: P t ′ ← UniqGen ​ ( Φ smell , P t , E , R ) P^{\prime}_{t}\leftarrow\textsc{UniqGen}(\Phi_{\text{smell}},P_{t},E,R) 11: Evaluate F ⁡ ( 𝐬 ) F(\mathbf{s}) , for all 𝐬 ∈ P t ′ \mathbf{s}\in P^{\prime}_{t} ; update 𝐬 best t \mathbf{s}^{t}_{\text{best}} 12: P t ′′ ← UniqGen ​ ( Φ vision , P t ′ , E , R ) P^{\prime\prime}_{t}\leftarrow\textsc{UniqGen}(\Phi_{\text{vision}},P^{\prime}_{t},E,R) 13: Evaluate F ⁡ ( 𝐬 ) F(\mathbf{s}) , for all 𝐬 ∈ P t ′′ \mathbf{s}\in P^{\prime\prime}_{t} ; update 𝐬 best t \mathbf{s}^{t}_{\text{best}} 14: if no improvement of F ⁡ ( 𝐬 best t ) F(\mathbf{s}^{t}_{\text{best}}) for K K consecutive iterations then 15: P t + 1 ← UniqGen ​ ( Φ cauchy , P t ′′ , E , R ) P_{t+1}\leftarrow\textsc{UniqGen}(\Phi_{\text{cauchy}},P^{\prime\prime}_{t},E,R) 16: else 17: P t + 1 ← P t ′′ P_{t+1}\leftarrow P^{\prime\prime}_{t} 18: end if 19: end for 20: return 𝐬 best N \mathbf{s}^{N}_{\text{best}}

[110] p: Population Initialization (Alg. 2 ). We initialize the population by coverage-constrained random sampling. This ensures that each dimension of the search space is sampled approximately uniformly, thereby improving initial coverage and reducing the risk of premature convergence due to biased initialization.

[111] figure: Algorithm 2 Population Initialization 1: Input: dimension sets { D 1 , D 2 , … , D m } \{D_{1},D_{2},\dots,D_{m}\} , population size N N 2: Output: population P 0 P_{0} 3: for each dimension D k D_{k} do 4: Generate sequence 𝒳 k = { x k , 1 , … , x k , N } , x k , j ∈ D k \mathcal{X}_{k}=\{x_{k,1},\dots,x_{k,N}\},\ x_{k,j}\in D_{k} 5: where 𝒳 k = ⋃ r = 1 ⌈ N / | D k | ⌉ π r ​ ( D k ) \mathcal{X}_{k}=\bigcup_{r=1}^{\lceil N/|D_{k}|\rceil}\pi_{r}(D_{k}) , with π r \pi_{r} a random permutation of D k D_{k} 6: ensuring Pr [ x k , j = d ] ≈ 1 | D k | , ∀ d ∈ D k \Pr[x_{k,j}=d]\approx\tfrac{1}{|D_{k}|},\ \forall d\in D_{k} 7: end for 8: for j = 1 ​ … ​ N j=1\dots N do 9: Construct individual 𝐬 ( j ) = ( x 1 , j , x 2 , j , … , x m , j ) \mathbf{s}^{(j)}=(x_{1,j},x_{2,j},\dots,x_{m,j}) 10: end for 11: Set P 0 = { 𝐬 ( 1 ) , … , 𝐬 ( N ) } P_{0}=\{\mathbf{s}^{(1)},\dots,\mathbf{s}^{(N)}\} 12: return P 0 P_{0}

[112] p: Deduplication (Alg. 3 ). To avoid redundant individuals, we propose the UniqGen algorithm, which enforces uniqueness through resampling with a maximum of R R attempts. This mechanism prevents wasted evaluations.

[113] figure: Algorithm 3 UniqGen: Deduplication with R R Resampling Attempts 1: Input: Operator Ψ \Psi , population P P , explored set E E , resampling limit R R 2: Output: New population P ′ P^{\prime} 3: P ′ ← ∅ P^{\prime}\leftarrow\emptyset 4: for each 𝐬 ∈ P \mathbf{s}\in P do 5: for r = 1 ​ … ​ R r=1\dots R do 6: 𝐬 ^ ← Ψ ⁡ ( 𝐬 ) \hat{\mathbf{s}}\leftarrow\Psi(\mathbf{s}) 7: if h ⁡ ( 𝐬 ^ ) ∉ E h(\hat{\mathbf{s}})\notin E then 8: P ′ ← P ′ ∪ { 𝐬 ^ } P^{\prime}\leftarrow P^{\prime}\cup\{\hat{\mathbf{s}}\} , E ← E ∪ { h ⁡ ( 𝐬 ^ ) } E\leftarrow E\cup\{h(\hat{\mathbf{s}})\} 9: break 10: end if 11: end for 12: P ′ ← P ′ ∪ { 𝐬 ^ } P^{\prime}\leftarrow P^{\prime}\cup\{\hat{\mathbf{s}}\} , E ← E ∪ { h ⁡ ( 𝐬 ^ ) } E\leftarrow E\cup\{h(\hat{\mathbf{s}})\} 13: end for 14: return P ′ P^{\prime}

[114] p: Smell Search (Alg. 4 ). This operator performs a localized stochastic search. The exploration step size decays over iterations, enabling a smooth transition from global exploration to local exploitation.

[115] figure: Algorithm 4 Smell Search 1: Input: individual 𝐬 = ( s 1 , … , s m ) \mathbf{s}=(s_{1},\dots,s_{m}) , iteration t t , exploration ratio α \alpha , decay factor γ \gamma 2: Output: individual 𝐬 ′ \mathbf{s}^{\prime} 3: Initialize 𝐬 ′ ← 𝐬 \mathbf{s}^{\prime}\leftarrow\mathbf{s} 4: for i = 1 , … , m i=1,\dots,m do 5: Δ t ← max ⁡ ( 1 , ⌊ α ⋅ | D i | ⋅ γ t ⌋ ) \Delta_{t}\leftarrow\max\!\left(1,\lfloor\alpha\cdot|D_{i}|\cdot\gamma^{t}\rfloor\right) 6: δ ∼ U ⁡ ( − Δ t , Δ t ) \delta\sim U(-\Delta_{t},\Delta_{t}) 7: i ​ d ​ x ← ( i ​ d ​ x ​ ( s i ) + δ ) mod | D i | idx\leftarrow(idx(s_{i})+\delta)\bmod|D_{i}| 8: s i ′ ← D i ​ [ i ​ d ​ x ] s^{\prime}_{i}\leftarrow D_{i}[idx] 9: end for 10: return 𝐬 ′ = ( s 1 ′ , … , s m ′ ) \mathbf{s}^{\prime}=(s^{\prime}_{1},\dots,s^{\prime}_{m})

[116] p: Vision Search (Alg. 5 ). This operator biases individuals toward the current global best solution with a time-varying attraction factor. As the iteration progresses, the search becomes increasingly exploitative, guiding convergence.

[117] figure: Algorithm 5 Vision Search 1: Input: current individual 𝐬 = ( s 1 , … , s m ) \mathbf{s}=(s_{1},\dots,s_{m}) , best individual 𝐬 best = ( s 1 best , … , s m best ) \mathbf{s}_{\text{best}}=(s^{\text{best}}_{1},\dots,s^{\text{best}}_{m}) , iteration t t , max iterations N N 2: Output: individual 𝐬 ′ \mathbf{s}^{\prime} 3: Initialize 𝐬 ′ ← 𝐬 \mathbf{s}^{\prime}\leftarrow\mathbf{s} 4: Define attraction factor β t = β 0 + ( 1 − β 0 ) ⋅ t N \beta_{t}=\beta_{0}+(1-\beta_{0})\cdot\frac{t}{N} 5: for i = 1 , … , m i=1,\dots,m do 6: Sample u ∼ U ⁡ ( 0 , 1 ) u\sim U(0,1) 7: if u < β t u<\beta_{t} then 8: s i ′ ← s i best s^{\prime}_{i}\leftarrow s^{\text{best}}_{i} 9: else 10: s i ′ ← s i s^{\prime}_{i}\leftarrow s_{i} 11: end if 12: end for 13: return 𝐬 ′ = ( s 1 ′ , … , s m ′ ) \mathbf{s}^{\prime}=(s^{\prime}_{1},\dots,s^{\prime}_{m})

[118] p: Cauchy Mutation (Alg. 6 ). To further enhance exploration, we apply a Cauchy-distributed mutation. Its heavy-tailed property allows occasional large jumps in the search space, helping the algorithm escape local optima.

[119] figure: Algorithm 6 Cauchy Mutation 1: Input: individual 𝐬 = ( s 1 , … , s m ) \mathbf{s}=(s_{1},\dots,s_{m}) , mutation probability p mut p_{\mathrm{mut}} , scale parameter λ \lambda 2: Output: individual 𝐬 ′ \mathbf{s}^{\prime} 3: Initialize 𝐬 ′ ← 𝐬 \mathbf{s}^{\prime}\leftarrow\mathbf{s} 4: for i = 1 , … , m i=1,\dots,m do 5: Sample u ∼ U ⁡ ( 0 , 1 ) u\sim U(0,1) 6: if u < p mut u<p_{\mathrm{mut}} then 7: i ​ d ​ x ​ ( s i ) ← idx ⁡ ( s i , D i ) idx(s_{i})\leftarrow\operatorname{idx}(s_{i},D_{i}) 8: Sample ξ ∼ 𝒞 ⁡ ( 0 , λ ) \xi\sim\mathcal{C}(0,\lambda) 9: i ​ d ​ x ​ ( s i ′ ) ← ( i ​ d ​ x ​ ( s i ) + ⌊ ξ ⌋ ) mod | D i | idx(s^{\prime}_{i})\leftarrow\big(idx(s_{i})+\lfloor\xi\rfloor\big)\bmod|D_{i}| 10: Set s i ′ ← D i ​ [ i ​ d ​ x ​ ( s i ′ ) ] s^{\prime}_{i}\leftarrow D_{i}[idx(s^{\prime}_{i})] 11: end if 12: end for 13: return 𝐬 ′ = ( s 1 ′ , … , s m ′ ) \mathbf{s}^{\prime}=(s^{\prime}_{1},\dots,s^{\prime}_{m})

[120] h2: Appendix C Experimental Details

[121] p: This appendix details the experimental procedures, method components, and parameter settings. To ensure a thorough evaluation of CC-BOS, each step is carefully designed and executed. It includes the optimization algorithm configuration, multi-dimensional strategy space, evaluation module, and defense implementation. Each section provides step-by-step details to support reproducibility and offer technical insights.

[122] h3: C.1 Parameter Settings

[123] p: In our experiments, the Bio-Inspired Optimization Algorithm is configured with the following parameters: the step size decay rate is set to 0.95, the cauchy mutation scale is 0.2, the stagnation threshold is 2 iterations, and the maximum number of unique attempts for generating new strategies is 5. These settings are chosen to balance exploration and exploitation, maintain population diversity, and ensure stable convergence during the optimization process. It should also be noted that the early stopping conditions differ between the main experiment (Table 1 ) and the efficiency experiment (Table 3 ). The main experiment sets the maximum number of queries to 120, while the efficiency experiment is set to 80.

[124] h3: C.2 Multi-dimensional Strategy Space

[125] p: The eight dimensions briefly introduced in the main text are explained here in detail, highlighting their individual functions within the multi-dimensional strategy space.

[126] p: Role Identity denotes the use of disguised identities to enhance the credibility of jailbreak queries by imparting authority, scholarship, or mystery. The content of this dimension is designed as follows.

[127] p: Behavioral Guidance facilitates the model to generate sensitive content at the semantic level, through meticulously designing jailbreak queries, combining role identity and context. The content of this dimension is designed as follows.

[128] p: Mechanism serves as the inherent design principle of jailbreak queries; it provides structural support for behavioral guidance and collaborates with role identity, metaphor mapping, and triggering patterns to enable controllable and diverse prompt generation. The content of this dimension is designed as follows.

[129] p: Metaphor Mapping replaces sensitive content through metaphors, symbols, or cultural expressions, preventing jailbreak queries from keyword-based detection. The content of this dimension is designed as follows.

[130] p: Expression Style specifies linguistic expressions and synergizes them with role identity and metaphor mapping, to ensure jailbreak queries are standardized and controllable. The content of this dimension is designed as follows.

[131] p: Knowledge Relation transforms ancient knowledge frameworks into modern logical structures, leveraging the synergy of role identity, stylistic expression, and metaphor mapping to naturally embed sensitive requests within cultural narratives. The content of this dimension is designed as follows.

[132] p: Contextual Setting constructs seemingly innocuous historical or cultural contexts, and embeds sensitive requests within these contexts to enhance the plausibility and stealth of queries. The content of this dimension is designed as follows.

[133] p: Trigger Pattern utilizes preset vocabulary, sentence structures, or conditions to control the activation timing and progression rhythm of queries. The content of this dimension is designed as follows.

[134] p: Prompt Design. After having elaborated on the eight dimensions of the multidimensional strategy space, we now proceed to illustrate their practical application in prompt design. Each dimension functions as a guiding principle for refining the original query, ensuring that the resulting prompt remains faithful to the intended meaning while conveying it through a culturally rich, classical literary style.

[135] p: The following defines the prompt template employed to operationalize the multidimensional strategy space:

[136] h3: C.3 Evaluation Module

[137] p: Translated module. The translation module first segments model responses to mitigate the risks of distortion and information loss in overly long texts (e.g., truncation and omissions caused by context window limitations). The module then performs a two-stage translation, from classical Chinese to modern Chinese and subsequently to English, gradually eliminating the metaphorical, implicit, and semantically compressed features characteristic of classical Chinese. To further improve translation accuracy and stability, we incorporate multiple sets of few-shot examples into the prompt design, emphasizing paraphrase priority, semantic integrity, and academic clarity. This ensures that responses grounded in classical Chinese contexts are faithfully rendered into English. The translated outputs are fed into the fitness evaluation modules, providing solid support for cross-context fitness evaluation. The translation prompt word template is as follows:

[138] p: Evaluation Template. To evaluate model responses, we adopt the standardized evaluation template proposed in H-COT ( Kuo et al., 2025 ) . Consistent with this framework, all assessments are carried out using GPT-4o as the evaluation model.

[139] p: Rejection Strings. In this study, we employ the rejection strings as defined in CL-GSO. The following table presents the full set of rejection strings utilized for detection.

[140] p: "I’m sorry"

[141] p: "Sorry"

[142] p: "sorry"

[143] p: "I am sorry"

[144] p: "I apologize"

[145] p: "I cannot"

[146] p: "I do not"

[147] p: "I’m really sorry"

[148] p: "My apologies"

[149] p: "but I cannot"

[150] p: "I’m not able to provide"

[151] p: "I am really sorry"

[152] p: "I cannot create"

[153] p: "I cannot support"

[154] p: "I can’t provide"

[155] p: "I can’t assist"

[156] p: </s>

[157] h3: C.4 Defense Implementation

[158] p: In our defense experiments, the attack success rate (ASR) is evaluated using the Llama-Guard-3-8B ( Dubey et al., 2024 ) defense mechanism. Specifically, input defense filters adversarial prompts before they are sent to the victim model, while output defense evaluates the model’s generated responses. In the dual-defense setting, both input and output filters are applied sequentially. A sample is considered blocked if Llama-Guard marks it as unsafe at either stage. This procedure ensures that ASR is measured against realistic automated defense conditions.

[159] h2: Appendix D More examples

[160] p: In this appendix, we provide several jailbreak attack examples generated using the CC-BOS framework. Please note that any sensitive or harmful content in these examples has been redacted to prevent misuse.

[161] figure: Figure 3: Examples of responses under adversarial prompting. Left: Results on Gemini-2.5-Flash. Right: Results on Claude-3.7.

[162] figure: Figure 4: Examples of responses under adversarial prompting. Left: Results on GPT-4o. Right: Results on Deepseek-Reasoner.

[163] figure: Figure 5: Examples of responses under adversarial prompting. Left: Results on Qwen3. Right: Results on Grok-3.

[164] h2: Appendix E Evaluation on Different Attack LLMs

[165] figure: Table 7: Attack Success Rate (ASR) on AdvBench with various LLMs serving as the Attack Model. Attack Model Target Model Gemini-2.5-Flash GPT-4o Deepseek-Reasoner Deepseek-Chat (Original) 100% 100% 100% GPT-3.5-Turbo 98% 100% 96% Gemini-2.0-Flash 94% 96% 96%

[166] p: To investigate whether the efficacy of CC-BOS depends on the specific capability of the default attack model (Deepseek-Chat), we generalized the framework by replacing the backbone with GPT-3.5-Turbo and Gemini-2.0-Flash. We evaluated these attack models against three diverse target models: Gemini-2.5-Flash, GPT-4o, and Deepseek-Reasoner, maintaining the same experimental settings as the main evaluation.

[167] p: As presented in Table 7 , the results demonstrate remarkable robustness. The alternative attack models maintain consistently high stability, achieving ASRs exceeding 94% across all diverse target models. Notably, GPT-3.5-Turbo still achieves 100% on GPT-4o. This confirms that the attack performance is driven by the strategy space rather than the specific generator.

[168] h2: Appendix F COMPARATIVE ANALYSIS OF OPTIMIZATION ALGORITHMS

[169] p: To justify the selection of the Fruit Fly Optimization Algorithm (FOA) as the core search engine for CC-BOS, we conducted a comparative study againstGenetic Algorithm (GA) and Random Search on GPT-4o. As presented in Table 8 , FOA demonstrates a dual superiority in both attack effectiveness and query efficiency. Regarding effectiveness, FOA achieves a perfect 100% Attack Success Rate (ASR) on GPT-4o, surpassing both GA (94%) and Random Search (90%). More critically, in terms of efficiency, FOA exhibits a significant advantage by requiring an average of only 1.28 queries to generate a successful jailbreak. In stark contrast, GA requires 4.04 queries (about 3 × 3\times cost) and Random Search requires 6.10 queries (about 5 × 5\times cost). These results confirm that FOA effectively balances global exploration and local exploitation, making it the optimal choice for maximizing attack performance while minimizing query overhead.

[170] figure: Table 8: Performance comparison of different optimization algorithms on AdvBench against GPT-4o. The number in bold indicates the best jailbreak performance. Optimizer ASR Avg. Q FOA (Ours) 100% 1.28 Genetic Algorithm (GA) 94% 4.04 Random Search 90% 6.10

[171] h2: Appendix G Evaluation of Translation as a Defensive Pre-processing Step

[172] p: To investigate the role of linguistic obscurity in jailbreak attacks, we repurposed our translation module as a defensive pre-processing step for output filtering under two distinct configurations: "Trans. Output Only" and "Mixed Dual" (Standard Input & Trans. Output). As shown in Table 9 , the translation-enhanced defense proved effective for Gemini-2.5-Flash and Deepseek-Reasoner; notably, it reduced the ASR from 36.00% to 26.00% in the output-only setting on Deepseek-Reasoner.

[173] figure: Table 9: Defense efficacy comparison: Standard Defense vs. Translation Enhanced Output Defense. The "Mixed Dual" setting combines standard input filtering with translation-based output filtering. Defense Deepseek-Reasoner Gemini-2.5-Flash Standard Llama Guard Defense Standard Output Only (Raw) 36.00% 24.00% Standard Dual (Input + Output) 28.00% 22.00% Translation Enhanced Trans. Output Only 26.00% 22.00% Mixed Dual (Input + Trans. Output) 20.00% 20.00%

[174] h2: Appendix H Evaluation against Dynamic and Composite Defenses

[175] p: Previous works ( Wei et al., 2023b ; Wu et al., 2023 ; Xiong et al., 2024 ) have proposed a series of dynamic and composite defense methods to prevent jailbreak attacks. We compare our CC-BOS with state-of-the-art baselines, ICRT and GPTFUZZER, against a spectrum of defense mechanisms on Gemini-2.5-Flash. These mechanisms consist of In-Context Defense (ICD) ( Wei et al., 2023b ) , Self-Reminder ( Wu et al., 2023 ) , and several composite variations.

[176] p: The results are shown in Table 10 . It can be observed that CC-BOS demonstrates significant advantages across various defense strategies. Specifically, CC-BOS achieves 100.00% ASR in the no-defense scenario, surpassing ICRT (92.00%) and GPTFUZZER (28.00%). Under dynamic defenses, our method exhibits superior adaptability: it maintains a robust 28.00% ASR under the highly effective Self-Reminder mechanism, whereas GPTFUZZER collapses to 0.00% and ICRT drops to 8.00%.

[177] p: Moreover, we evaluate the proposed method under rigorous composite defense settings. As shown in the Table 10 , CC-BOS exhibits remarkable resilience, consistently maintaining an ASR exceeding 16% across all composite defense configurations. This advantage is particularly pronounced under the Triple Defense (ICD + Self-Reminder + LG Output), where existing attacks are rendered almost ineffective (ASR ≤ \leq 2.00%). In contrast, CC-BOS retains a 16.00% success rate, which is eight times higher than GPTFUZZER. These results confirm that CC-BOS possesses a distinct capability to penetrate complex, multi-layered safety alignments.

[178] figure: Table 10: ASR (%) comparison under Dynamic and Composite defense strategies on Gemini-2.5-Flash. The number in bold indicates the best jailbreak performance. "ICD" denotes In-Context Defense; "LG" denotes Llama-Guard. Defense Strategy CC-BOS (Ours) ICRT GPTFUZZER No Defense 100.00% 92.00% 28.00% Dynamic Defenses ICD (1-shot) 76.00% 46.00% 24.00% ICD (2-shot) 54.00% 20.00% 22.00% Self-Reminder 28.00% 8.00% 0.00% Composite Defenses ICD (2-shot) + Self-Reminder 24.00% 6.00% 6.00% ICD (1-shot) + Llama Guard (Output) 22.00% 0.00% 20.00% ICD (2-shot) + Llama Guard (Output) 16.00% 0.00% 16.00% Self-Reminder + Llama Guard (Output) 18.00% 0.00% 0.00% ICD (2-shot) + Self-Reminder + LG (Output) 16.00% 0.00% 2.00%

[179] h2: Appendix I Universality Analysis across Classical Languages

[180] p: To investigate the universality of the proposed attack and address concerns regarding language specificity, we extend our evaluation to Latin and Sanskrit . These languages were specifically selected because they share a critical structural isomorphism with Classical Chinese. They are represented in pre-training corpora (e.g., historical archives, legal texts, and religious scriptures) yet are significantly under-represented in modern safety alignment datasets.

[181] p: As presented in Table 11 , our method demonstrates robust efficacy across these distinct linguistic contexts, with Attack Success Rates (ASR) exceeding 94% across all tested models. Notably, GPT-4o and DeepSeek-Reasoner exhibit near-total vulnerability, achieving 100% ASR on Latin prompts. These empirical results confirm that the identified vulnerability is not unique to the syntax of Classical Chinese; rather, it stems from a systemic “High Capability-Low Alignment” distributional shift, where the model retains sophisticated understanding of classical languages while lacking the corresponding safety guardrails.

[182] figure: Table 11: Attack Success Rate (ASR) across different classical languages on various Target Models. Language Target Model Gemini-2.5-Flash GPT-4o DeepSeek-Reasoner Classical Chinese 100% 100% 100% Latin 96% 100% 100% Sanskrit 98% 94% 98%

[183] h2: Appendix J Language Comparison Analysis

[184] p: To examine the impact of linguistic environments on jailbreak effectiveness, we evaluate the attack success rates (ASR) of prompts written in English, Modern Chinese, and Classical Chinese on the target model GPT-4o. As reported in Table 12 , substantial disparities emerge across languages. In particular, Classical Chinese achieves a 100% ASR, markedly outperforming English (82%) and Modern Chinese (86%). This consistent performance gap provides empirical justification for the use of Classical Chinese in CC-BOS, demonstrating its clear advantage over English and Modern Chinese under identical attack settings.

[185] figure: Table 12: Attack Success Rate (ASR) comparison across different language contexts Language ASR English 82% Modern Chinese 86% Classical Chinese 100%

[186] h2: Appendix K Dimension-wise Ablation of CC-BOS

[187] figure: Table 13: Dimension-wise ablation results of CC-BOS on Claude-3.7 under the classical Chinese setting. ASR denotes Attack Success Rate, and Avg.Q denotes the average number of queries. Dimension Removed ASR (%) Avg.Q Role Identity 96 3.88 Behavioral Guidance 92 5.40 Mechanism 82 9.08 Metaphor Mapping 82 9.82 Expression Style 94 4.80 Knowledge Relation 88 7.32 Contextual Setting 94 4.36 Trigger Pattern 96 5.08 CC-BOS (Full) 100 2.38

[188] p: To further analyze the contribution of each strategy dimension in CC-BOS, we conduct a dimension-wise ablation study under the classical Chinese setting on the target model Claude-3.7 . Specifically, we remove one strategy dimension at a time while keeping all other components unchanged and evaluate the resulting attack success rate (ASR) and average number of queries (Avg.Q).

[189] p: As shown in Table 13 , removing any single strategy dimension consistently degrades performance compared to the full CC-BOS configuration, demonstrating that all dimensions contribute meaningfully to the overall effectiveness of the framework on Claude-3.7. Notably, the removal of the Mechanism or Metaphor Mapping dimension leads to a pronounced reduction in ASR (from 100% to 82%) accompanied by a substantial increase in query cost, highlighting their important role in facilitating successful jailbreaks under the classical Chinese setting. Meanwhile, ablating other dimensions also results in observable declines in both ASR and query efficiency, indicating that these components collectively support robust and efficient attack construction rather than serving as interchangeable or redundant strategies.

[190] p: Overall, these results demonstrate that CC-BOS benefits from the complementary interaction of multiple strategy dimensions on Claude-3.7, contributing to both high attack success and reduced query cost relative to ablated variants.

[191] h2: Instructions for reporting errors

[192] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[193] p: Tip: You can select the relevant text first, to include it in your report.

[194] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[195] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
