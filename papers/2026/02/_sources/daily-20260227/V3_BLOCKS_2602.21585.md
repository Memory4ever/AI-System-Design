[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Duel-Evolve: Reward-Free Test-Time Scaling via LLM Self-Preferences

[3] h6: Abstract

[4] p: Many applications seek to optimize LLM outputs at test time by iteratively proposing, scoring, and refining candidates over a discrete output space. Existing methods use a calibrated scalar evaluator for the target objective to guide search, but for many tasks such scores are unavailable, too sparse, or unreliable. Pairwise comparisons, by contrast, are often easier to elicit, still provide useful signal on improvement directions, and can be obtained from the LLM itself without external supervision. Building on this observation, we introduce Duel-Evolve , an evolutionary optimization algorithm that replaces external scalar rewards with pairwise preferences elicited from the same LLM used to generate candidates. Duel-Evolve aggregates these noisy candidate comparisons via a Bayesian Bradley–Terry model, yielding uncertainty-aware estimates of candidate quality. These quality estimates guide allocation of the comparison budget toward plausible optima using Double Thompson Sampling, as well as selection of high-quality parents to generate improved candidates. We evaluate Duel-Evolve on MathBench, where it achieves 20 percentage points higher accuracy over existing methods and baselines, and on LiveCodeBench, where it improves over comparable iterative methods by over 12 percentage points. Notably, the method requires no reward model, no ground-truth labels during search, and no hand-crafted scoring function. Results show that pairwise self-preferences provide strong optimization signal for test-time improvement over large, discrete output spaces.

[5] h2: 1 Introduction

[6] p: Problems involving natural or symbolic language naturally lend themselves to optimization over a multidimensional discrete space: we seek a candidate y ∈ 𝒴 y\in\mathcal{Y} that attains a high value under an objective f : 𝒴 → ℝ f:\mathcal{Y}\to\mathbb{R} . For example, in MaxSAT, y y is a Boolean assignment and f ⁡ ( y ) f(y) counts satisfied clauses ( Biere et al., 2021 ; Bacchus et al., 2019 ) ; in proof search, y y is a candidate proof and f ⁡ ( y ) ∈ { 0 , 1 } f(y)\in\{0,1\} indicates whether the target proposition is established ( Polu and Sutskever, 2020 ; Bansal et al., 2019 ; Yang et al., 2023b ) . Test-time refinement of an LLM response ( Madaan et al., 2023 ; Snell et al., 2024 ) also fits this paradigm, where y y is a token sequence and f ⁡ ( y ) f(y) measures solution quality for some downstream task.

[7] p: While the problem is easy to formulate, optimization over 𝒴 \mathcal{Y} is challenging. The discrete space is combinatorially large, small edits can impact quality discontinuously, and gradients, the signal that drives modern machine learning optimization, are undefined. Recent work addresses these difficulties by using LLMs as semantic-aware optimizers: they maintain a population of candidates, evaluate each by assigning a scalar reward s s from a surrogate function approximating f f , and prompt the LLM with ( y , s ) (y,s) pairs to propose improved variants ( Romera-Paredes et al., 2024 ; Novikov et al., 2025 ) . When the surrogate is informative, the score plays the role of a noisy gradient signal: it induces a consistent ordering over candidates and provides a dense direction for local improvement.

[8] p: However, in many domains, an informative real-valued surrogate is unavailable or unreliable. Binary verifiers and stochastic batch scores are too sparse or noisy to provide effective guidance for search. A natural way to remove the requirement of specifying an external surrogate is to prompt the LLM itself to qualify or score its responses. However, such ratings may still require an externally specified rubric, and are often poorly calibrated and mutually inconsistent ( Zheng et al., 2023 ) .

[9] p: In this paper, we propose to use a different signal that remains internal to the model yet is typically more stable: pairwise preference. Concretely, we use the same LLM as both generator and judge. We query it to choose a winner between two candidates ( y i , y j ) (y_{i},y_{j}) and pool these duels to recover a global estimate of quality—an implicit surrogate for f f defined without any external feedback.

[10] p: Using preferences as the sole optimization signal introduces two algorithmic challenges. First, comparisons are local and noisy, so the algorithm must aggregate them into a coherent global ranking while accounting for statistical uncertainty. Second, comparisons are expensive: under a limited evaluation budget, the algorithm must decide which pairs to compare so that effort is concentrated on candidates that are still plausible optima, rather than on those known to be suboptimal.

[11] p: To address both challenges, we propose Duel-Evolve , an evolutionary optimizer for discrete structured spaces that is guided solely by pairwise preferences. Duel-Evolve maintains a growing pool of candidates and alternates between (i) selecting informative pairs to compare, (ii) fitting a Bayesian Bradley–Terry model ( Bradley and Terry, 1952 ) to aggregate all observed outcomes, and (iii) conditioning the generator LLM on a small set of high scoring parents along with their estimated posterior utilities to propose new candidates.

[12] p: Duel-Evolve efficiently explores the space of possible solutions through a Bayesian model of global scores, while exploiting the LLM’s understanding of language to produce high quality proposals. We use a Laplace approximation to obtain per-candidate posterior means and confidence intervals, and we adapt Double Thompson Sampling (DTS) ( Wu and Liu, 2016 ) to allocate the comparison budget toward competitive candidates.

[13] p: We demonstrate Duel-Evolve on mathematical reasoning and code generation tasks. On MathBench ( Liu et al., 2024 ) , our method reaches 94% accuracy, exceeding the strongest baseline by 20 percentage points; for LiveCodeBench ( Jain et al., 2024 ) , it achieves 37% accuracy, improving over similar evolutionary methods by over 12 percentage points. Notably, these gains are obtained without training a reward model or designing a task-specific scalar surrogate, as the LLM generates both the proposals and comparative judgments.

[14] h2: 2 Method

[15] p: We develop Duel-Evolve , an LLM-based optimization algorithm for discrete structured spaces guided only by pairwise preferences. We first describe our problem setting (§ 2.1 ). We then cast it as a dueling-bandits problem and motivate an idealized Bayesian solution (§ 2.2 ). Finally, we derive practical approximations that yield Duel-Evolve (§ 2.3 ).

[16] h3: 2.1 Problem Setting

[17] p: Given a query x x , let 𝒴 \mathcal{Y} be a discrete space of candidate solutions (e.g., programs, proofs, reasoning traces, or prompt variants), and let f : 𝒴 → ℝ f:\mathcal{Y}\to\mathbb{R} denote an unknown latent utility function that implicitly depends on x x . Our goal is to find a maximizer

[18] table: y ∗ = arg ⁡ max y ∈ 𝒴 ⁡ f ⁡ ( y ) . y^{*}\;=\;\arg\max_{y\in\mathcal{Y}}f(y). (1)

[19] p: We consider a setting in which f f is well-defined but never observed during optimization. Instead, optimization proceeds solely through an LLM, which we use in two roles. First, as a noisy judge 𝒥 \mathcal{J} that, given two candidates y i , y j ∈ 𝒴 y_{i},y_{j}\in\mathcal{Y} for the same query x x , returns which candidate it prefers.

[20] p: Second, the LLM also acts as a generator p ϕ p_{\phi} that, given x x and a small set of parent solutions A ⊂ 𝒴 A\subset\mathcal{Y} , proposes new candidates in 𝒴 \mathcal{Y} .

[21] p: The core algorithmic problem is then how to reliably move toward y ∗ y^{*} using only pairwise preferences and LLM-based generation, without access to an external reward model or verifier, under a limited budget of LLM calls.

[22] h3: 2.2 A First Approach: Double Thompson Sampling with Dueling Bandits

[23] figure: Figure 1: Duel-Evolve approximates Double Thompson Sampling (DTS) over a combinatorial space. At round t t , DTS maintains a posterior p ( 𝜽 ∣ D 1 : t ) p(\boldsymbol{\theta}\mid D_{1:t}) over latent utilities 𝜽 = ( θ y ) y ∈ 𝒴 \boldsymbol{\theta}=(\theta_{y})_{y\in\mathcal{Y}} given comparison history D 1 : t = { ( y i , y j , c i ​ j ) } D_{1:t}=\{(y_{i},y_{j},c_{ij})\} , and selects the next duel by sampling y a , y b ∼ p t ∗ ( y ) = P ( y = arg max y ′ θ y ′ ∣ D 1 : t ) y_{a},y_{b}\sim p_{t}^{*}(y)=P\!\big(y=\arg\max_{y^{\prime}}\theta_{y^{\prime}}\mid D_{1:t}\big) . Duel-Evolve approximates posterior inference by fitting a Bradley–Terry model on the evaluated pool E t E_{t} with a Laplace approximation, yielding per-candidate summaries ( μ i , t , σ i , t ) (\mu_{i,t},\sigma_{i,t}) (§ 2.3.1 ); it then approximates maximizer-focused sampling by Thompson-sampling duels and parents A t A_{t} from a pruned survivor set S t ⊆ E t S_{t}\subseteq E_{t} , and proposing children via a conditioned LLM generator y ∼ p ϕ ​ ( y ∣ x , { ( y i , μ i , t ) } y i ∈ A t ) y\sim p_{\phi}\!\big(y\mid x,\{(y_{i},\mu_{i,t})\}_{y_{i}\in A_{t}}\big) (§ 2.3.2 –§ 2.3.3 ).

[24] p: With access only to pairwise comparisons, we adopt the dueling bandits framework ( Yue et al., 2012 ) as a convenient formulation of Problem ( 1 ). In this framework, we are given a set of arms 𝒴 \mathcal{Y} , and optimization proceeds iteratively: at each round, the algorithm selects a pair of arms ( y i , y j ) (y_{i},y_{j}) to compare, observes noisy binary feedback indicating which is preferred, and uses this outcome to refine its estimates of arm quality, with the goal of identifying the best arm y ∗ y^{*} under a limited budget of comparisons.

[25] p: The difficulty is that pairwise comparisons are both local — each involves only two candidates — and noisy . Identifying the best arm therefore requires (i) aggregating many such noisy local signals into a global ranking of the arms while (ii) deciding which pairs to compare next under a limited budget.

[26] p: We address both by assigning a latent utility to each arm and modeling comparisons as noisy functions of utility differences. This yields estimates of the quality of the arms, quantifies remaining uncertainty, and guides the choice of the next pair to compare. Below, we formalize this idea with a Bradley–Terry likelihood and describe Double Thompson Sampling (DTS) ( Wu and Liu, 2016 ) , an idealized algorithm for this setting. We then discuss the obstacles that prevent the direct application of DTS, motivating the approximations that lead to our algorithm in § 2.3.3 .

[27] h5: Bradley–Terry Model.

[28] p: Let 𝜽 = ( θ y ) y ∈ 𝒴 ∈ ℝ | 𝒴 | \boldsymbol{\theta}=(\theta_{y})_{y\in\mathcal{Y}}\in\mathbb{R}^{|\mathcal{Y}|} be a vector of latent utilities, one per candidate, so that a higher θ y \theta_{y} indicates a better solution y y . We place a prior Π ⁡ ( 𝜽 ) \Pi(\boldsymbol{\theta}) over this vector to encode structural assumptions about 𝒴 \mathcal{Y} — for instance, that semantically similar solutions should have similar utilities.

[29] p: Given a pair ( y i , y j ) (y_{i},y_{j}) , we model the judge’s feedback with a Bradley–Terry model ( Bradley and Terry, 1952 ) . It models the probability that y i y_{i} is preferred over y j y_{j} as

[30] table: P ⁡ ( c i ​ j = + 1 ) = σ ⁡ ( θ i − θ j ) , P(c_{ij}=+1)=\sigma\,\!\big(\theta_{i}-\theta_{j}\big), (2)

[31] p: where σ \sigma denotes the logistic sigmoid and c i ​ j ∈ { − 1 , + 1 } c_{ij}\in\{-1,+1\} .

[32] p: Given all comparisons observed up to round t t , denoted 𝒟 t = { ( y i , y j , c i ​ j ) } \mathcal{D}_{t}=\{(y_{i},y_{j},c_{ij})\} , we combine the prior Π ⁡ ( 𝜽 ) \Pi(\boldsymbol{\theta}) with the Bradley–Terry likelihood to obtain the posterior p ⁡ ( 𝜽 ∣ 𝒟 t ) p(\boldsymbol{\theta}\mid\mathcal{D}_{t}) . This posterior aggregates many pairwise comparisons into a global distribution over the utility of each arm.

[33] h5: Algorithm: Double Thompson Sampling.

[34] p: Given the posterior, the algorithm must decide which pair to compare next. Intuitively, comparisons are most informative when they involve candidates that are plausibly optimal. Spending comparisons on arms that the posterior already deems suboptimal with high confidence yields little new information.

[35] p: This intuition is formalized by the posterior probability that a given candidate is optimal, its maximizer probability ,

[36] table: p t ∗ ( y ) ≡ P ( y = y ∗ ∣ 𝒟 t ) = ∫ [ y = arg max y ′ θ y ′ ] p ( 𝜽 ∣ 𝒟 t ) d 𝜽 . p_{t}^{*}(y)\;\equiv\;P\!\big(y=y^{*}\mid\mathcal{D}_{t}\big)=\int\mathbbm{1}\!\Big[y=\textstyle\arg\max_{y^{\prime}}\theta_{y^{\prime}}\Big]\;p(\boldsymbol{\theta}\mid\mathcal{D}_{t})\,d\boldsymbol{\theta}. (3)

[37] p: Double Thompson Sampling ( Wu and Liu, 2016 ) uses p t ∗ p_{t}^{*} to select which pair to compare: at each round, independently draw y a , y b ∼ p t ∗ ​ ( ⋅ ) y_{a},y_{b}\sim p_{t}^{*}(\cdot) , query the judge, and update Bradley–Terry posterior. After T T rounds, it returns y ^ = arg ⁡ max y ⁡ μ y , T \hat{y}=\arg\max_{y}\mu_{y,T} , where μ y , T \mu_{y,T} is the posterior mean utility. The procedure is summarized in the top half of Figure 1 .

[38] h3: 2.3 From Double Thompson Sampling to Duel-Evolve

[39] p: Duel-Evolve follows a similar structure to Double Thompson Sampling. It maintains a pool of candidates, selects pairs to compare, observes which candidate the judge prefers, and updates a posterior over latent utilities. This posterior then guides the next comparison. Duel-Evolve extends this loop by also proposing new, improved candidates via LLM-based generation at each iteration.

[40] p: However, because 𝒴 \mathcal{Y} is a combinatorially large space of natural-language solutions, two operations that are tractable in the classical finite-arm setting must now be approximated: (i) maintaining and sampling from the posterior p ⁡ ( 𝜽 ∣ 𝒟 t ) p(\boldsymbol{\theta}\mid\mathcal{D}_{t}) and (ii) sampling candidates proportional to their posterior probability of being optimal, p t ∗ ​ ( y ) p_{t}^{*}(y) . We address each in turn (§ 2.3.1 –§ 2.3.2 ), then show how the two approximations combine to form the Duel-Evolve loop (§ 2.3.3 ).

[41] h4: 2.3.1 Operation (i): Approximating p ⁡ ( 𝜽 ∣ 𝒟 t ) p(\boldsymbol{\theta}\mid\mathcal{D}_{t})

[42] p: To approximate the first operation p ⁡ ( 𝜽 ∣ 𝒟 t ) p(\boldsymbol{\theta}\mid\mathcal{D}_{t}) , rather than defining the posterior over all of 𝒴 \mathcal{Y} , we restrict inference to the finite set of candidates that the algorithm has generated and compared so far (how candidates enter this set is described in § 2.3.3 ). We assign a latent utility θ i \theta_{i} to each such candidate y i y_{i} and place an independent Gaussian prior θ ∼ 𝒩 ⁡ ( 0 , σ 0 2 ​ I ) \theta\sim\mathcal{N}(0,\,\sigma_{0}^{2}I) .

[43] p: The posterior is unimodal under this prior, so we compute the MAP estimate

[44] table: 𝜽 ^ t = arg ⁡ max θ ​ [ ∑ ( y i , y j , c ) ∈ 𝒟 t log ⁡ σ ⁡ ( c ⁡ ( θ i − θ j ) ) − ‖ θ ‖ 2 2 ​ σ 0 2 ] , \hat{\boldsymbol{\theta}}_{t}=\arg\max_{\theta}\left[\sum_{(y_{i},\,y_{j},\,c)\,\in\,\mathcal{D}_{t}}\log\sigma\!\bigl(c(\theta_{i}-\theta_{j})\bigr)\;-\;\frac{\|\theta\|^{2}}{2\sigma_{0}^{2}}\right], (4)

[45] p: where c ∈ { − 1 , + 1 } c\in\{-1,+1\} . The regularizer resolves the additive non-identifiability inherent to pairwise models. We use a Laplace approximation around θ ^ t \hat{\theta}_{t} with a diagonal Hessian. This yields per-candidate Gaussian summaries ( μ i , t , σ i , t 2 ) (\mu_{i,t},\,\sigma_{i,t}^{2}) which we can use to judge the quality of each candidate and our uncertainty about it. In practice, we solve this problem using an L-BFGS solver ( Liu and Nocedal, 1989 ) .

[46] h4: 2.3.2 Operation (ii): Approximating p t ∗ p_{t}^{*}

[47] p: Computing p t ∗ ​ ( y ) = P ⁡ ( y = y ∗ ∣ 𝒟 t ) p_{t}^{*}(y)=P(y=y^{*}\mid\mathcal{D}_{t}) exactly would require drawing 𝜽 ∼ p ⁡ ( 𝜽 ∣ 𝒟 t ) \boldsymbol{\theta}\sim p(\boldsymbol{\theta}\mid\mathcal{D}_{t}) and solving arg ⁡ max y ′ ∈ 𝒴 ⁡ θ y ′ \arg\max_{y^{\prime}\in\mathcal{Y}}\theta_{y^{\prime}} , which is intractable over the full solution space. We replace this with an LLM-conditioned proposal: given a set of existing solutions annotated with their estimated qualities, the LLM can infer the relationship between solution structure and score and extrapolate toward improvements. In-context learning thus plays the role that a structured prior over 𝒴 \mathcal{Y} would have played in an exact Bayesian treatment, providing the structural generalization needed to propose plausibly optimal candidates without enumeration.

[48] p: Concretely, we condition the generator on a parent set A t A_{t} together with their posterior means,

[49] table: y new ∼ p ϕ ( y | x , { ( y i , μ i , t ) } y i ∈ A t ) , y_{\mathrm{new}}\;\sim\;p_{\phi}\!\left(y\;\middle|\;x,\;\bigl\{(y_{i},\,\mu_{i,t})\bigr\}_{y_{i}\in A_{t}}\right), (5)

[50] p: where A t A_{t} is selected from the set of candidates that have already been generated and compared. The exact construction of A t A_{t} is detailed in the next section as part of the full algorithm.

[51] h4: 2.3.3 Putting it together: the Duel-Evolve loop

[52] p: Duel-Evolve combines the two approximations above in an evolutionary loop. The algorithm maintains an evaluated pool E t E_{t} of all candidates generated so far, initialized by sampling N 0 N_{0} candidates from p ϕ ( ⋅ ∣ x ) p_{\phi}(\cdot\mid x) conditioned only on the query, with an empty comparison history 𝒟 = ∅ \mathcal{D}=\emptyset . Each generation t t then proceeds in three phases in a loop:

[53] p: Update. Fit the posterior over E t E_{t} using full comparison history 𝒟 t \mathcal{D}_{t} , obtaining ( μ i , t , σ i , t 2 ) (\mu_{i,t},\,\sigma_{i,t}^{2}) via Equation 4 and the Laplace approximation.

[54] p: Evaluate. Select a batch of pairs from E t E_{t} via Thompson sampling—drawing θ ~ i ∼ 𝒩 ⁡ ( μ i , t , σ i , t 2 ) \tilde{\theta}_{i}\sim\mathcal{N}(\mu_{i,t},\,\sigma_{i,t}^{2}) and pairing the top-ranked candidates—then query the judge J J on all pairs and append the outcomes to 𝒟 t \mathcal{D}_{t} .

[55] p: Evolve. Select parents A t A_{t} from E t E_{t} via Thompson sampling, sample a batch of B B new candidates from p ϕ ( ⋅ ∣ x , A t ) p_{\phi}(\cdot\mid x,A_{t}) via Equation 5 , and add them to E t E_{t} .

[56] p: Within each phase, all judge queries (Step 2) and all generation calls (Step 3) are issued in parallel, so the wall-clock cost per generation is dominated by a single round of LLM inference rather than by the number of comparisons or children produced. The cycle repeats until the budget is exhausted and in the end we return as output y ^ = arg ⁡ max y i ∈ E T ⁡ μ i , T \hat{y}=\arg\max_{y_{i}\in E_{T}}\mu_{i,T} .

[57] p: While in theory Thompson Sampling effectively balances the exploration/exploitation tradeoff, in practice we invoke two additional mechanisms to compensate for the fact that our approximations are not exact. First, we maintain a survivor set S t ⊆ E t S_{t}\subseteq E_{t} and prune any candidate whose upper confidence bound falls below the best lower confidence bound, where the width of these bounds is a hyperparameter. Steps 2 and 3 then operate over S t S_{t} rather than E t E_{t} , avoiding wasted comparisons on confidently suboptimal candidates while retaining them in E t E_{t} so their data still informs the posterior. Second, we construct A t A_{t} by mixing Thompson-sampled top scorers with recently generated candidates that still have high uncertainty, ensuring new arrivals are always evaluated in the next iteration. Figure 1 gives the complete procedure.

[58] h2: 3 Related Work

[59] h5: Optimization in discrete spaces.

[60] p: Although our work is applied in the context of LLM-generated outputs, it belongs to the broader tradition of heuristic optimization over discrete and combinatorial spaces, where exact methods are intractable and gradient information is unavailable. Classic metaheuristics such as genetic algorithms ( Goldberg, 1989 ) and simulated annealing ( Kirkpatrick et al., 1983 ) iteratively refine candidate solutions through stochastic perturbation and selection, guided by a scalar objective. Recently, LLMs have been embedded into such search loops—proposing improved candidates conditioned on scored histories ( Yang et al., 2023a ) , maintaining evolutionary populations of programs scored by explicit evaluators ( Romera-Paredes et al., 2024 ; Novikov et al., 2025 ) , or optimizing prompts for downstream tasks, like GEPA ( Agrawal et al., 2025 ) , among others ( Fernando et al., 2023 ; Guo et al., 2023 ) . However, all of these approaches rely on an informative scalar evaluator, which is often unavailable or prohibitively expensive to design for open-ended generation tasks. Duel-Evolve removes this requirement by replacing scalar scores with pairwise preferences aggregated through a Bayesian Bradley–Terry model into a global posterior over candidate quality. Concurrent work, Feedback Descent ( Lee et al., 2025 ) , also eschews scalar evaluation but performs single-trajectory hill-climbing against a single incumbent, maintaining no global model of candidate quality and offering no mechanism for allocating comparisons efficiently. Duel-Evolve addresses both limitations by fitting a posterior over observed duels to obtain uncertainty-aware quality estimates and using Thompson sampling to focus comparisons on strong candidates. Prompt Duel Optimizer (PDO) ( Wu et al., 2025 ) , another concurrent method that forgoes scalar evaluation, applies Double Thompson Sampling with LLM-judged pairwise preferences similarly to Duel-Evolve . However, PDO targets dataset-level prompt selection rather than per-instance response optimization, and uses independent Beta posteriors with a Copeland-style objective rather than our global Bayesian Bradley–Terry posterior over candidate utilities.

[61] h5: Dueling bandits.

[62] p: Duel-Evolve builds on the dueling-bandits framework, first introduced by Yue and Joachims (2009) for interactive information retrieval and online ranker optimization, and later formalized as the K K -armed dueling-bandits problem by Yue et al. (2012) . Since then, dueling bandits have become a general framework for preference-based online learning and comparison-based selection ( Ailon et al., 2014 ; Bengs et al., 2021 ) . Standard formulations assume a fixed, finite arm set and a winner notion such as a Condorcet winner, and design sampling rules to minimize regret or identify the best arm. Prominent algorithms include frequentist confidence-bound methods ( Yue et al., 2012 ; Zoghi et al., 2014 ; Zoghi et al., 2015 ; Komiyama et al., 2015 ) and Bayesian posterior-sampling rules such as DTS ( Wu and Liu, 2016 ) , and are often paired with parametric preference models like Bradley–Terry or Plackett–Luce ( Saha, 2021 ) . While Duel-Evolve adopts a similar parametric formulation and is inspired by standard algorithms such as DTS, it diverges from these works by operating over a combinatorially large arm set that grows during optimization, requiring approximate inference and pruning heuristics in place of the exact computations of the finite-arm literature.

[63] p: Test-time search, refinement, and compute scaling for LLM outputs. Duel-Evolve is also part of the growing family of methods that improve LLM outputs by scaling test-time computation ( Snell et al., 2024 ) . These methods can be organized along two axes: whether they require an external reward signal, and whether performance continues to improve as more compute is invested. Methods relying on external evaluators—Best-of- N N with trained verifiers ( Cobbe et al., 2021 ) , process reward models with step-level tree search ( Lightman et al., 2023 ) , and repeated sampling at scale ( Brown et al., 2024 ) —are often bottlenecked by scorer quality and availability. Methods that avoid external reward—reasoning models ( Jaech et al., 2024 ; Guo et al., 2025 ) , iterative self-refinement ( Madaan et al., 2023 ; Shinn et al., 2023 ) , and search over intermediate steps ( Yao et al., 2023 ) —typically operate on a single candidate with no mechanism to pool information across solutions and have an upper bound on scaling. Duel-Evolve sits in the quadrant that requires no external reward yet continues improving with additional compute, as more generations yield both better utility estimates and exploration of stronger regions of the solution space. It also complements single-generation methods: for example, reasoning models and refinement techniques can serve as subroutines (e.g., as a stronger judge or generator) within the algorithm.

[64] h2: 4 Experiments

[65] p: We evaluate Duel-Evolve on two benchmarks: mathematical reasoning (MathBench) and code generation (LiveCodeBench). Our experiments compare against chain-of-thought prompting, multiple sampling with aggregation, and iterative-refinement baselines. We also examine how performance scales with the number of evolutionary generations.

[66] h3: 4.1 Tasks and Metrics

[67] h5: MathBench.

[68] p: MathBench ( Liu et al., 2024 ) is a dataset that contains multiple-choice mathematics questions spanning primary school to college-level curricula. A math problem serves as the query x x , and the candidate space 𝒴 \mathcal{Y} is the model’s reasoning trace paired with a multiple-choice answer. Duel-Evolve evolves these trace-answer pairs. We use the English-language splits at the Middle , High , and College difficulty levels, restricting to the single-choice format in which each question is presented as a four-option problem with one correct answer. We exclude all “knowledge” subsets, which primarily test recall of definitions or formulae, and retain only word-problem-style questions that require multi-step numerical and algebraic reasoning. From the selected subsets, we construct a balanced test set of 150 problems by stratified sampling, with 50 problems per difficulty level. A separate validation split is held out for constructing few-shot demonstrations (see § 4.2 ). We report accuracy, or the fraction of problems with the correct multiple-choice answer, both over all problems and stratified by difficulty level. All MathBench experiments use Gemma-3-4b-it ( Gemma Team et al., 2024 ) , a model well-suited to these problem difficulties.

[69] h5: LiveCodeBench.

[70] p: LiveCodeBench v6 ( Jain et al., 2024 ) is an execution-based dataset of Python competitive programming problems sourced from AtCoder () , LeetCode () , and CodeForces () . A programming problem serves as the query x x , and the candidate space 𝒴 \mathcal{Y} consists of code solutions. Every problem includes a small set of public tests (1–4 per problem; median 3) and a substantially larger hidden test set (up to 100; median 25). We use the public tests only as a coarse feedback signal for all iterative methods during evolution and report accuracy as the percentage of problems for which 100% of the hidden test cases pass, following standard practice for LiveCodeBench. To enable rapid iteration, we construct an evaluation set of 99 problems, selecting 33 problems from each difficulty level: Easy , Medium , and Hard . Because the competitive programming problems in LiveCodeBench require stronger reasoning skills than those in MathBench, we use the larger Gemma-3-27b-it ( Gemma Team et al., 2024 ) (4-bit quantized; Red Hat AI (2025) ) for all LiveCodeBench experiments.

[71] p: The two tasks studied exemplify the sparse-reward settings that motivate our approach. On MathBench, the only signal is final correctness, with no intermediate feedback to guide search. On LiveCodeBench, each problem exposes 1–4 public tests, which provide a coarse intermediate reward. However, a solution that passes all public tests may still fail on the hidden suite, so optimizing against public tests alone is insufficient. In both tasks, the absence of a rich scalar objective reduces the effectiveness of score-based search methods, motivating the use of pairwise preferences as an alternative signal for guiding evolutionary search.

[72] h3: 4.2 Baselines

[73] p: We compare Duel-Evolve against baselines that operate under increasingly privileged information regimes. Problem-only methods receive only the problem statement: zero-shot chain-of-thought ( Wei et al., 2022 ) , self-consistency ( Wang et al., 2022 ) , Feedback Descent ( Lee et al., 2025 ) , Best-of- N N —which selects from N N i.i.d. samples via the same pairwise preference mechanism used by Duel-Evolve but without the evolutionary loop—and Duel-Evolve itself. Demonstration-aided methods additionally condition on solved examples: few-shot chain-of-thought prepends k k exemplars with reasoning traces from a held-out validation split ( k = 8 k{=}8 for MathBench and k = 3 k{=}3 for LiveCodeBench). Label-aided methods further have access to per-instance correctness: we evaluate GEPA ( Agrawal et al., 2025 ) , which uses ground-truth supervision to maintain a Pareto frontier and drive reflective mutation of a system prompt used to generate problem solutions. All methods use the same underlying language model; further baseline details are provided in Appendix D .

[74] h3: 4.3 Main Results

[75] figure: Method Accuracy (%) Zero-shot CoT 57.3 Few-shot CoT ( k = 8 k{=}8 ) 64.0 Self-consistency 62.7 Best-of- N N 65.3 GEPA 51.3 Feedback descent 72.0 Duel-Evolve 94.0 Figure 2: MathBench accuracy over 150 generations. Left: Duel-Evolve performance stratified by difficulty level ( Middle , High , College ). Middle: Method comparison over generations: non-iterative baselines (Zero-shot CoT, Few-shot CoT, Self-consistency, and Best-of- N N ) remain flat, while iterative methods (Feedback Descent, GEPA, and Duel-Evolve ) improve over time. Right: Final accuracy across methods. Duel-Evolve achieves the best performance.

[76] p: We report accuracy across all methods for both MathBench and LiveCodeBench. For iterative methods, we report the accuracy of the identified best solution at each generation step.

[77] p: The table in Figure 2 reports final accuracy for each method on MathBench after 150 generations. Duel-Evolve achieves 94% accuracy, exceeding the strongest baseline by 22 percentage points. Sampling methods perform modestly, with self-consistency, Best-of- N N , and few-shot prompting all achieving similar accuracies. GEPA did not perform as well—we believe this is because the optimized prompts overfit to the validation set, on which the best prompt achieved 67% accuracy. Iterative refinement via Feedback Descent improves over static methods and GEPA, but Duel-Evolve achieves the highest accuracy given the iteration budget. Its accuracy as a function of generation step ( Figure 2 , left and middle) shows rapid early improvement, rising from 57% to 90% within the first 10 generations, followed by slower improvement to 94% by generation 64. The difficulty-stratified curves (left) show that middle problems are solved fastest, reaching 96% by generation 6 and 98% at convergence. High and college problems follow a similar trajectory but converge more slowly, both reaching 92%.

[78] figure: Method Accuracy (%) Zero-shot CoT 13.1 Few-shot CoT ( k = 3 k{=}3 ) 16.2 Self-consistency 20.2 Best-of- N N 31.3 GEPA 25.3 Feedback Descent 24.2 Duel-Evolve 37.4 Figure 3: LiveCodeBench accuracy over 200 generations. Left: Duel-Evolve performance stratified by difficulty level ( Easy , Medium , Hard ). Middle: Method comparison over generations: static baselines (Zero-shot CoT, Few-shot CoT, Self-consistency, and Best-of- N N ) are flat, while iterative methods (Feedback Descent, GEPA and Duel-Evolve ) improve over time. Right: Final accuracy across methods. Duel-Evolve achieves the best performance.

[79] p: Figure 3 reports results on LiveCodeBench after 200 generations. As on MathBench, Duel-Evolve outperforms the baselines, attaining 37.4% accuracy and exceeding Feedback Descent and GEPA by over 12 percentage points. Notably, Duel-Evolve surpasses other iterative baselines by the fifth generation ( Figure 3 , middle). Best-of- N N performs competitively, suggesting that our preference-based selection procedure provides a meaningful signal even without iterative search; Duel-Evolve builds on this to achieve further gains. In the difficulty-stratified accuracy plot, we see large early improvement followed by steady accuracy gains in both the Easy and Medium problems. Unlike in our MathBench experiments, GEPA outperforms the sampling-based baselines, except for Best-of- N N , and even exceeds the final accuracy of Feedback Descent. However, due to the substantially higher wall-clock cost of the reference GEPA implementation on LiveCodeBench problems, we limited GEPA to 125 iterations and extrapolate its accuracy at iteration 125 for (middle) in Figure 3 . We made a best-faith effort to optimize its throughput in our setup, but the method remained significantly more expensive than other baselines.

[80] h2: 5 Discussion

[81] p: Duel-Evolve demonstrates that pairwise preferences elicited from an LLM can serve as effective optimization signals when informative scalar rewards are unavailable. Choosing a winner between two candidates is typically an easier task for an LLM than producing an optimal solution directly. Duel-Evolve exploits this by aggregating many noisy local duels into global quality estimates via the Bayesian Bradley–Terry model, and using the model posteriors to generate proposals from stronger regions of the solution space. Notably, Duel-Evolve does not use an external reward model, ground-truth labels, or task-specific scoring functions. On MathBench, where the only feedback is final binary correctness, Duel-Evolve reaches 94.0% accuracy, exceeding the strongest baseline by over 20 percentage points. On LiveCodeBench, where public test coverage is insufficient to guarantee hidden-test success, it attains 37.4% accuracy, improving over other iterative methods by over 12 percentage points.

[82] p: It is important to note that, relative to k k -shot baselines, all iterative methods incur additional inference cost from repeated generation and judging. Nevertheless, on MathBench, approximately 90% of the total improvement occurs within the first 10 generations, demonstrating rapid convergence is possible depending on the task. Further, on both benchmarks, Duel-Evolve performance separates from the other iterative methods early in the search, with the rate of improvement exceeding that of Feedback Descent and GEPA within the first few generations.

[83] p: Because the optimization signal of Duel-Evolve derives entirely from the model’s own preferences, a limitation of the method is that it will amplify rather than correct systematic judge biases, such as a preference for confidence over correctness. This may be especially apparent in more open-ended domains such as summarization, dialogue, or creative generation, where quality criteria are subjective. Mitigating such biases in the context of Duel-Evolve through ensembling models or calibrating against labeled subsets remains important future work.

[84] h2: References

[85] h2: Appendix A Method Details

[86] h3: A.1 Implementation Details

[87] p: All experiments use the same model for both generation and evaluation. For Duel-Evolve on MathBench, each evolutionary generation produces a batch of 12 candidate solutions, each conditioned on 6 scored parents selected via a Thompson-sampling / recency mixture.

[88] p: For Duel-Evolve on LiveCodeBench, each evolutionary generation produces a batch of 40 candidate solutions, each conditioned on 5 scored parents selected via a Thompson-sampling / recency mixture. Additionally, we employ abstract syntax tree-based (AST-based) de-duplication of candidates for LiveCodeBench, where AST-based signatures for each candidate are stored. If a candidate with a repeating signature would be added to the candidate pool, it is instead discarded and not replaced.

[89] p: Evaluation uses order-consistent pairwise judging: each pair is judged twice with swapped presentation order, and only concordant judgments are retained as decisive comparisons. The Bradley–Terry posterior (MAP + Laplace) is updated after each evaluation round, and the population is maintained at a maximum of 200 solutions with confidence-based pruning. Responses are generated in structured JSON format with explicit reasoning and answer fields.

[90] p: We retain only order-consistent decisive outcomes,

[91] table: d i ​ j = [ ( z i ​ j ( 1 ) = A ∧ z i ​ j ( 2 ) = B ) ∨ ( z i ​ j ( 1 ) = B ∧ z i ​ j ( 2 ) = A ) ] . d_{ij}=\mathbbm{1}\!\left[(z^{(1)}_{ij}=A\wedge z^{(2)}_{ij}=B)\;\vee\;(z^{(1)}_{ij}=B\wedge z^{(2)}_{ij}=A)\right].

[92] p: If d i ​ j = 1 d_{ij}=1 , we record a directed preference y i ≻ y j y_{i}\succ y_{j} or y j ≻ y i y_{j}\succ y_{i} accordingly. If d i ​ j = 0 d_{ij}=0 , the comparison is treated as non-informative and excluded from model updates. Operationally, this is equivalent to dropping ties before fitting the Bradley–Terry model.

[93] p: For solution generation for MathBench, we use a temperature of 0.7. For LiveCodeBench, we increase the temperature to 1.2 as we noticed duplicate solutions. After adding AST-based de-duplication, for some problems half of the generation batch would get de-duplicated. To remedy this, we increased the temperature to promote more diverse generations. This likely explains why Best-of- N N performs relatively better on LiveCodeBench than on MathBench, as the higher temperature naturally leads to more exploration.

[94] p: For LiveCodeBench, we additionally add “evolving memory" to the generation prompt. Evolving memory acts as a model scratchpad and is preserved through each iteration in an evolutionary path. At each iteration, the model is allowed to both update the solution and also edit the evolving memory to use as additional short “notes”. For example, the evolving memory may be used to store key insights for future attempts like edge cases found, algorithmic patterns that work, complexity considerations, etc. We instruct the model to keep the evolving memory to less than 500 characters.

[95] p: Feedback Descent ( Lee et al., 2025 ) . We implemented Feedback Descent based on the paper, as the method does not have a public codebase. To prevent overly long context lengths in the iterative solution generation step, we use a window size of 15 previous solutions.

[96] p: GEPA ( Agrawal et al., 2025 ) . We set the base and reflective LLMs to be the same model. For LiveCodeBench, we use GEPA inference-time search, which sets the training and validation splits to be the test set; for MathBench, we use separate training and validation splits, as feedback for an example is identical to its solution. For both datasets, we run GEPA using the AnyMaths Adapter from the GEPA GitHub repository; 0 0 0 https://github.com/gepa-ai/gepa for LiveCodeBench, we modify the adapter to incorporate test case-based evaluation and feedback.

[97] h2: Appendix B Prompt Templates

[98] p: For all methods except GEPA ( Section B.2.6 ), we use the system prompt "You are a helpful assistant."

[99] h3: B.1 MathBench

[100] h4: B.1.1 Initial Generation Prompt Template (No Parents)

[101] h4: B.1.2 Generation Prompt Template (Evolution / With Parents)

[102] h4: B.1.3 Template for Each Parent Solution Block ( {parent_solutions} )

[103] h4: B.1.4 Evaluation Prompt Template (LLM Judge)

[104] h4: B.1.5 Few-Shot Generation Template (k-shot)

[105] h4: B.1.6 GEPA

[106] p: We use a slightly modified prompt for GEPA, as their method optimizes the system prompt.

[107] p: System prompt.

[108] p: User prompt.

[109] h3: B.2 LiveCodeBench

[110] h4: B.2.1 Initial Generation Prompt Template (No Parents)

[111] h4: B.2.2 Generation Prompt Template (Evolution / With Parents)

[112] h4: B.2.3 Template for Each Parent Solution Block ( {parent_solutions} )

[113] h4: B.2.4 Evaluation Prompt Template (LLM Judge)

[114] h4: B.2.5 Few-Shot Generation Template (k-shot)

[115] h4: B.2.6 GEPA

[116] p: We use a slightly modified prompt for GEPA, as their method optimizes the system prompt.

[117] p: System prompt.

[118] p: User prompt.

[119] h2: Appendix C GEPA Optimized Prompts

[120] p: Below we show the final optimized prompts found by GEPA for MathBench and LiveCodeBench.

[121] h3: C.1 MathBench

[122] h3: C.2 LiveCodeBench

[123] h2: Appendix D Baselines

[124] p: The base model is prompted with a single chain-of-thought instruction and no demonstrations.

[125] p: We prepend k k solved examples drawn from a held-out validation split, each annotated with a step-by-step reasoning trace. The exemplar set is sampled once with a fixed seed and reused across all test problems. For MathBench, we use k = 8 k=8 . For LiveCodeBench, we found that using k = 8 k=8 deteriorated performance, so we use k = 3 k=3 .

[126] p: For each problem we draw N N independent responses at non-zero temperature and return the majority-vote answer.

[127] p: Using the same N N samples, we run pairwise LLM-judge battles across all candidates, fit the same Bradley–Terry model (MAP + Laplace), and return the response with the highest posterior mean utility. This uses the same preference-based evaluation mechanism as Duel-Evolve but without the evolutionary loop, isolating the contribution of evolution from that of the selection procedure alone.

[128] p: Iterative propose-and-judge refinement: the first round generates an initial solution; each subsequent round proposes a new candidate conditioned on the recent attempt history and compares it against the current incumbent via an LLM judge. The judged winner becomes the new incumbent; ties and invalid judgments retain the incumbent. Presentation order is randomized at each comparison to mitigate position bias, and only the most recent W W attempts are shown to the proposer to bound prompt length.

[129] p: An initial seed system prompt is optimized by: (1) obtaining evaluation traces from a minibatch sampled from the training split, which are provided along with labels to the reflective LLM to suggest an improved prompt; (2) maintaining a Pareto frontier of dominant prompts for each validation example; a previously generated prompt is sampled according to its appearance frequency in the frontier and iteratively provided as input to (1).

[130] h2: Appendix E LLM Use Disclosure

[131] p: The authors used large language models throughout this project, including for writing and debugging experiment code, monitoring experiments, and for paper writing tasks such as improving phrasing, clarity, and rewriting passages. All LLM-generated content was reviewed and validated by the authors, who take full responsibility for the contents of this paper.

[132] h2: Instructions for reporting errors

[133] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[134] p: Tip: You can select the relevant text first, to include it in your report.

[135] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[136] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
