[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Black-Box Reliability Certification for AI Agents via Self-Consistency Sampling and Conformal Calibration

[3] h6: Abstract.

[4] p: Given a black-box AI system and a task, at what confidence level can a practitioner trust the system’s output? We answer with a reliability level —a single number per system–task pair, derived from self-consistency sampling and conformal calibration , that serves as a black-box deployment gate with exact, finite-sample, distribution-free guarantees. Self-consistency sampling reduces uncertainty exponentially; conformal calibration guarantees correctness within 1 / ( n + 1 ) 1/(n{+}1) of the target level, regardless of the system’s errors—made transparently visible through larger answer sets for harder questions. Weaker models earn lower reliability levels (not accuracy—see Definition 2.4 ): GPT-4.1 earns 94.6 % 94.6\% on GSM8K and 96.8 % 96.8\% on TruthfulQA, while GPT-4.1-nano earns 89.8 % 89.8\% on GSM8K and 66.5 % 66.5\% on MMLU. We validate across five benchmarks, five models from three families, and both synthetic and real data. Conditional coverage on solvable items exceeds 0.93 0.93 across all configurations; sequential stopping reduces API costs by ∼ 50 % {\sim}50\% .

[5] h6: Key words and phrases:

[6] h2: 1. Introduction

[7] figure: AI System Question → \to K = 10 K{=}10 calls 42 42 42 37 42 37 42 42 42 42 1. Sample Ask the same question K K times Group & count ‘‘42’’ → \to 8 / 10 ‘‘37’’ → \to 2 / 10 Ranked by frequency 2. Rank Sort identical answers by frequency Human checks n ≈ 50 n{\approx}50 items ✓ \checkmark item 1: top 1 correct ✓ \checkmark item 2: top 1 correct × \times item 3: need top 2 ⟶ \longrightarrow 94.6 % 3. Calibrate Small batch → \to reliability level Figure 1. Pipeline overview. Step 1 : ask the AI system the same question K K times and collect its answers. Step 2 : group identical answers and rank them by frequency. Step 3 : a human checks a small calibration batch; the framework outputs a single reliability level (e.g. 94.6 % 94.6\% ) with a formal coverage guarantee. No model internals are needed—only API access.

[8] p: You have an AI system and a task—say, answering math questions or triaging support tickets. Before you deploy it, you need to know: how much can I trust this system? Not a vague intuition, but a concrete number with a guarantee attached. That is what this paper provides.

[9] p: The idea is simple (Figure 1 ). For each test question, ask the AI system the same question K K times (say, K = 10 K{=}10 ). Group the answers that say the same thing and rank them by frequency: the most popular answer might appear 8 8 out of 10 10 times, the runner-up 2 2 out of 10 10 . This frequency ranking is the raw signal—it captures how “sure” the system is without ever looking inside its weights. Then, a human spot-checks a small random batch—just 50 − 100 50{-}100 items. Each check takes seconds: the human sees the question and the system’s top-ranked answer, and marks it right or wrong. From these quick judgments, the framework computes a single number: the reliability level . For instance, GPT-4.1 earns 94.6 % 94.6\% reliability on grade-school math.

[10] p: The reliability level comes with a formal guarantee: it is a valid coverage bound that holds regardless of the AI system’s systematic errors, and it requires no assumptions about the data distribution. Crucially, the human is verifying, not labeling: the AI generates and ranks the answers; the human just confirms or rejects the top pick. There is no need to build a gold-standard dataset—fifty quick judgments are the entire human effort. A weaker system earns a lower number, not a misleading score; the framework makes trustworthiness transparent .

[11] p: More precisely, current evaluation methods each fail in a different way. Single-sample evaluation is unbiased but high-variance—a noisy snapshot of the agent’s true capability. Naive self-consistency (mode selection) reduces variance but can amplify bias: when the agent’s most frequent answer is wrong, more samples make the wrong answer look more certain. LLM-as-judge approaches [ Zheng2023Judge ] layer poorly characterized biases—position bias, verbosity preference, self-preference—on top of the agent’s own errors, and provide no formal reliability guarantees. None of these methods simultaneously controls both variance and bias.

[12] p: We introduce the reliability level (Definition 2.4 )—a single number per agent–task pair that answers this question with provable guarantees. The reliability level is a black-box deployment gate: it requires only API access, no model internals, and its validity is distribution-free with finite-sample coverage guarantees. Concretely, GPT-4.1 achieves 94.6% reliability on GSM8K and 96.8% on TruthfulQA; GPT-4.1-nano achieves 89.8% on GSM8K and 66.5% on MMLU. Open-weight models (Llama 4 Maverick, Mistral Small 24B) range from 66.7% (MMLU) to 95.4% (GSM8K) across three benchmarks (Table 10 ). A practitioner can read these numbers directly: “we need X X % reliability—which models qualify?”

[13] p: The mechanism behind the reliability level combines two ingredients. Self-consistency sampling reduces variance exponentially via aggregation (Theorem 4.4 ). Conformal calibration provides coverage guarantees whose validity is independent of agent bias : the evaluation’s coverage statement is correct regardless of the agent’s systematic error profile (Theorem 7.3 ). Agent bias is not hidden—it is made transparently visible through larger prediction sets (Theorem 7.5 ). A weaker agent earns a lower reliability level, not a misleading score.

[14] p: A key consequence—and a diagnostic that distinguishes calibration failure from agent limitation—is that marginal coverage can fall below 1 − α 1{-}\alpha only when the agent cannot solve certain items at all. This under-coverage is predicted by the theory, not a calibration artifact: conditional coverage on items the model can solve remains near-perfect ( ≥ 0.93 \geq 0.93 across all models and benchmarks in our experiments). When observed coverage falls short, the framework identifies why : the gap equals the fraction of unsolvable items.

[15] h3: Contributions

[16] p: Self-consistency sampling [ Wang2023SelfConsistency ] and conformal prediction [ Vovk2005 , Angelopoulos2021 ] are individually known. Recent work [ Quach2023ConformalLM , Kumar2023ConformalNLP ] applies conformal methods to language models using internal logits or softmax probabilities. Our contribution is a specific synthesis: a conformal score built entirely from external sample frequencies, producing a single reliability number for deployment gating—with no access to model internals. Specifically:

[17] p: Reliability certification for deployment gating (Definition 2.4 , Table 10 ): the primary practical output—a single reliability level per agent–task pair that answers “at what confidence can I trust this agent?” Validated across five benchmarks, five models from three families (GPT-4.1 ladder, Llama 4 Maverick, Mistral Small), with reliability levels ranging from 66.5 % 66.5\% to 96.8 % 96.8\% .

[18] p: A black-box nonconformity score from ranked canonical consensus (Sections 4 – 6 ): the technical construction enabling the reliability level—conformal scores from the rank of the acceptable answer in the self-consistency ordering, leveraging the variance reduction of aggregation while inheriting the distribution-free validity of conformal prediction. This specific construction and its analysis (variance reduction theorems, canonicalization-induced amplification) are new.

[19] p: Reliability theorems (Section 7 ): the evaluation’s coverage error is bounded by 1 / ( n + 1 ) 1/(n+1) regardless of the agent’s bias profile (Theorem 7.3 ); prediction set size is a monotone, transparent diagnostic of agent quality (Theorem 7.5 ); and the method achieves lower coverage error than LLM-as-judge evaluation once the calibration set exceeds ⌈ 1 / | b J | ⌉ − 1 \lceil 1/|b_{J}|\rceil-1 (e.g., n ≥ 19 n\geq 19 for typical judge bias; Corollary 7.10 ), though the two approaches answer complementary questions (Remark 7.11 ).

[20] p: Bias–variance anatomy of LLM evaluation (Section 3 ): the motivating analysis—a formal decomposition showing that single-sample evaluation suffers from variance, LLM-as-judge from irreducible bias, and naive self-consistency from bias amplification.

[21] p: Sequential sampling with certified early stopping (Section 9 ): a Hoeffding-based stopping rule that reduces API cost by ∼ 50 % {\sim}50\% with no loss in coverage.

[22] h3: Related Work

[23] h5: Self-consistency decoding.

[24] p: Wang et al. [ Wang2023SelfConsistency ] introduced self-consistency as an inference-time strategy: sample multiple reasoning traces and select the most frequent final answer. We repurpose self-consistency for evaluation : the ranked consensus provides raw material for conformal calibration. Cordero-Encinar and Duncan [ CorderoEncinar2025 ] certify when the majority-vote answer has stabilized; our stopping criterion (Theorem 9.1 ) certifies the ranking quality of the top- M M candidates for conformal set construction. The two are complementary.

[25] h5: Conformal prediction and language models.

[26] p: Conformal prediction [ Vovk2005 , Angelopoulos2021 ] provides prediction sets that are distribution-free with finite-sample coverage guarantees. Recent work applies conformal methods to language models: Quach et al. [ Quach2023ConformalLM ] construct conformal sets over token sequences for language generation; Kumar et al. [ Kumar2023ConformalNLP ] apply conformal prediction to NLP classification tasks. These methods define nonconformity scores from model logits or softmax probabilities—internal quantities unavailable for black-box API-based agents. Our score is constructed entirely from external ranked consensus over multiple samples, requiring no access to model internals. This black-box property is essential for evaluating proprietary LLM APIs.

[27] h5: Method comparison.

[28] p: Quach et al. and Kumar et al. achieve tighter prediction sets when softmax probabilities are available, because internal scores carry richer information than sample frequencies. Our contribution is generality : the framework applies to any black-box agent accessible only through sampling—commercial APIs, tool-using agents, multi-step pipelines—and to any task where canonicalization is feasible, including open-ended generation where token-level conformal methods do not apply.

[29] h5: LLM-as-judge and evaluation bias.

[30] p: Zheng et al. [ Zheng2023Judge ] established the LLM-as-judge paradigm. Subsequent studies documented systematic biases: position bias, verbosity bias, self-preference, and anchoring effects [ Zheng2023Judge ] . Our bias–variance analysis (Section 3 ) formalizes these observations: judge bias is an irreducible MSE component that does not decay with sample size (Proposition 3.4 ). Our framework avoids judge bias entirely by using frequency-based ranking rather than quality scoring.

[31] h5: Uncertainty quantification for LLMs.

[32] p: SelfCheckGPT [ MankulSelfCheckGPT ] detects hallucinations via inter-sample agreement. Semantic entropy [ Kuhn2023SemanticEntropy ] clusters generations and computes entropy over semantic classes. ConU [ ConU2024 ] applies conformal prediction using token-level probabilities. Although some APIs expose logprobs, ConU’s conformal guarantee requires calibrated token-level probabilities—a condition that is unverifiable for proprietary systems and unreliable even when logprobs are nominally available. Our rank-based nonconformity score is the first to provide formal conformal guarantees without any model internals, enabling calibration for any system accessible only through sampling. All three prior methods produce uncertainty estimates without formal calibration guarantees. Our framework produces calibrated prediction sets with finite-sample coverage guarantees, and uniquely pairs this black-box score with a deployment-gating output—the reliability level—a single actionable number that no prior conformal-LLM method provides. Semantic entropy could serve as a complementary pre-filter within conformal calibration.

[33] h5: Calibration of probabilistic predictions.

[34] p: Classical calibration methods (Platt scaling, temperature scaling, isotonic regression) adjust model confidence scores to match empirical frequencies. These require access to model probabilities and assume a fixed model; they cannot handle open-ended generation where the output space is combinatorial. Conformal prediction, by contrast, is model-agnostic and makes no distributional assumptions, which is why we adopt it as the calibration backbone.

[35] h2: 2. Problem Setting

[36] p: We formalize the setting: an AI system receives a query, produces a stochastic answer, and a task-specific predicate decides whether that answer is acceptable. The goal is to certify, from a small calibration set, how reliably the system’s top-ranked answer is acceptable. Our experiments validate the framework on single-turn query-answering systems; extensions to multi-turn interactions are discussed in Section 12 .

[37] h3: 2.1. Queries, answers, and acceptability

[38] p: Let 𝒳 {\mathcal{X}} denote the space of queries and 𝒜 {\mathcal{A}} the space of possible answers. An AI system with parameters θ \theta defines a stochastic mapping

[39] table: f θ : 𝒳 → 𝒜 , f θ ( x ) ∼ P θ ( ⋅ ∣ x ) , f_{\theta}:{\mathcal{X}}\to{\mathcal{A}},\qquad f_{\theta}(x)\sim P_{\theta}(\cdot\mid x),

[40] p: where P θ ( ⋅ ∣ x ) P_{\theta}(\cdot\mid x) is the system’s output distribution conditional on query x x , accessible via repeated sampling.

[41] h6: Definition 2.1 (Acceptability) .

[42] p: For a query x ∈ 𝒳 x\in{\mathcal{X}} , the set of acceptable answers is

[43] table: 𝒜 ⋆ ​ ( x ) := { a ∈ 𝒜 : Accept ⁡ ( x , a ) = 1 } , {\mathcal{A}}^{\star}(x):=\{a\in{\mathcal{A}}:\mathrm{Accept}(x,a)=1\},

[44] p: where Accept : 𝒳 × 𝒜 → { 0 , 1 } \mathrm{Accept}:{\mathcal{X}}\times{\mathcal{A}}\to\{0,1\} is a task-dependent predicate. We allow | 𝒜 ⋆ ​ ( x ) | ≥ 1 |{\mathcal{A}}^{\star}(x)|\geq 1 . For example, on a math problem with answer 42 42 , Accept \mathrm{Accept} returns 1 1 for “ 42 42 ”, “ 42.0 42.0 ”, and “forty-two”, and 0 0 for “ 43 43 ”.

[45] h6: Assumption 2.2 (Non-triviality) .

[46] p: For each query x x in the target distribution, 𝒜 ⋆ ​ ( x ) ≠ ∅ {\mathcal{A}}^{\star}(x)\neq\emptyset .

[47] h3: 2.2. Per-query acceptability rate and agent quality

[48] p: The central quantity is the probability that a single random sample from the agent is acceptable—intuitively, how often the agent “gets it right” on a given question.

[49] h6: Definition 2.3 (Per-query acceptability rate) .

[50] p: For a fixed query x x , the agent’s acceptability rate is

[51] table: (2.1) p ⋆ ​ ( x ) := P θ ​ ( f θ ​ ( x ) ∈ 𝒜 ⋆ ​ ( x ) ) = ∑ a ∈ 𝒜 ⋆ ​ ( x ) P θ ​ ( a ∣ x ) . p^{\star}(x):=P_{\theta}\bigl(f_{\theta}(x)\in{\mathcal{A}}^{\star}(x)\bigr)=\sum_{a\in{\mathcal{A}}^{\star}(x)}P_{\theta}(a\mid x).

[52] p: The aggregate accuracy of the agent over a query distribution μ \mu on 𝒳 {\mathcal{X}} is

[53] table: (2.2) p ¯ := 𝔼 X ∼ μ ​ [ p ⋆ ​ ( X ) ] . \bar{p}:={\mathbb{E}}_{X\sim\mu}[p^{\star}(X)].

[54] p: The quantities p ⋆ ​ ( x ) p^{\star}(x) and p ¯ \bar{p} are the ground truth that any evaluation method seeks to estimate or certify. Our framework does not estimate p ¯ \bar{p} directly; instead, it provides a coverage guarantee that is a stronger, more actionable statement about reliability.

[55] h3: 2.3. The evaluation goal

[56] p: We seek a procedure that, for each query x x , returns a prediction set S ⁡ ( x ) ⊂ 𝒞 S(x)\subset{\mathcal{C}} of canonical answer classes such that

[57] table: (2.3) ℙ ⁡ ( Y ⁡ ( x ) ∈ S ⁡ ( x ) ) ≥ 1 − α , {\mathbb{P}}\bigl(Y(x)\in S(x)\bigr)\geq 1-\alpha,

[58] p: where Y ⁡ ( x ) Y(x) denotes an acceptable answer for x x and α ∈ ( 0 , 1 ) \alpha\in(0,1) is a user-specified miscoverage level. The set S ⁡ ( x ) S(x) should be as small as possible: a smaller set indicates a more reliable agent on that query.

[59] p: We now define the target quantity that summarizes this coverage guarantee into a single deployment metric: the highest confidence level at which the agent’s most frequent answer is trustworthy.

[60] h6: Definition 2.4 (Reliability level) .

[61] p: For a given agent and task, the reliability level is

[62] table: (2.4) 1 − α ⋆ := | { i ∈ { 1 , … , n } : s i ≤ 1 } | n + 1 , 1-\alpha^{\star}:=\frac{|\{i\in\{1,\ldots,n\}:s_{i}\leq 1\}|}{n+1},

[63] p: where s 1 , … , s n s_{1},\ldots,s_{n} are calibration nonconformity scores (formally defined in Section 6 ; intuitively, s i s_{i} is the rank of the correct answer among the model’s self-consistency candidates for item i i ). Equivalently, 1 − α ⋆ 1{-}\alpha^{\star} is the maximum confidence at which the self-consistency mode alone provides conformal coverage.

[64] h6: Remark 2.5 (Interpreting the reliability level) .

[65] p: The numerator of ( 2.4 ) counts calibration items where the self-consistency mode is correct, closely related to mode accuracy but with the conformal correction n + 1 n{+}1 in the denominator that ensures a valid conformal quantile. Rather than asking “does this model achieve coverage at a fixed α \alpha ?”, we invert: “at what confidence level does this model qualify?”

[66] p: By Theorem 7.1 , the reliability level is a lower bound on test-time mode-voting coverage: deploying with α = α ⋆ \alpha=\alpha^{\star} guarantees ℙ ⁡ ( Y ∈ S ⁡ ( x ) ) ≥ 1 − α ⋆ {\mathbb{P}}(Y\in S(x))\geq 1-\alpha^{\star} . The gap between the reliability level and empirical test coverage is at most 1 / ( n + 1 ) 1/(n{+}1) (e.g., ≤ 0.002 {\leq}0.002 for n = 500 n{=}500 ).

[67] h2: 3. Bias and Variance in LLM Evaluation

[68] p: Before presenting our solution, we develop a formal framework for understanding why LLM evaluation is unreliable, and what “reliable evaluation” requires mathematically. This analysis motivates every design choice in our framework.

[69] h3: 3.1. What does reliable evaluation require?

[70] p: There are three ways to assess an answer: declare it correct or not (binary), assign a quality score (continuous), or output a set of candidates guaranteed to contain the truth (set-valued). Each has a different error profile.

[71] h6: Definition 3.1 (Evaluation method) .

[72] p: An evaluation method ℰ \mathcal{E} is a procedure that, given a query x x and access to the agent f θ f_{\theta} , produces an assessment. We consider three types:

[73] p: Point assessment: ℰ ⁡ ( x ) ∈ { 0 , 1 } \mathcal{E}(x)\in\{0,1\} (correct/incorrect).

[74] p: Score assessment: ℰ ⁡ ( x ) ∈ [ 0 , 1 ] \mathcal{E}(x)\in[0,1] (quality score).

[75] p: Set assessment: ℰ ⁡ ( x ) = S ⁡ ( x ) ⊂ 𝒞 \mathcal{E}(x)=S(x)\subset{\mathcal{C}} (prediction set with coverage guarantee).

[76] p: For point and score assessments, reliability is measured by the mean squared error between the assessment and the true acceptability:

[77] table: (3.1) MSE ⁡ ( ℰ ) = 𝔼 ⁡ [ ( ℰ ⁡ ( X ) − p ⋆ ​ ( X ) ) 2 ] . \MSE(\mathcal{E})={\mathbb{E}}\bigl[(\mathcal{E}(X)-p^{\star}(X))^{2}\bigr].

[78] p: The classical bias–variance decomposition applies:

[79] table: (3.2) MSE ⁡ ( ℰ ) = 𝔼 ⁡ [ ( 𝔼 ⁡ [ ℰ ⁡ ( X ) ∣ X ] − p ⋆ ​ ( X ) ) 2 ] ⏟ Bias 2 + 𝔼 ⁡ [ Var ⁡ ( ℰ ⁡ ( X ) ∣ X ) ] ⏟ Variance . \MSE(\mathcal{E})=\underbrace{{\mathbb{E}}\bigl[({\mathbb{E}}[\mathcal{E}(X)\mid X]-p^{\star}(X))^{2}\bigr]}_{\text{Bias}^{2}}+\underbrace{{\mathbb{E}}\bigl[\Var(\mathcal{E}(X)\mid X)\bigr]}_{\text{Variance}}.

[80] p: For set assessments, reliability is instead captured by the coverage validity gap :

[81] table: (3.3) Gap ⁡ ( ℰ ) := | ℙ ⁡ ( Y ∈ S ⁡ ( X ) ) − ( 1 − α ) | . \mathrm{Gap}(\mathcal{E}):=\bigl|{\mathbb{P}}(Y\in S(X))-(1-\alpha)\bigr|.

[82] p: A method with Gap ⁡ ( ℰ ) = 0 \mathrm{Gap}(\mathcal{E})=0 achieves exact calibration.

[83] h3: 3.2. Error anatomy of current evaluation methods

[84] p: We now analyze the bias and variance of three standard approaches, establishing the precise deficiencies that our framework addresses.

[85] h4: 3.2.1. Single-sample evaluation

[86] p: The simplest evaluation draws one sample a ∼ P θ ( ⋅ ∣ x ) a\sim P_{\theta}(\cdot\mid x) and checks acceptability:

[87] table: ℰ 1 ( x ) := 𝟙 { a ∈ 𝒜 ⋆ ( x ) } , a ∼ P θ ( ⋅ ∣ x ) . \mathcal{E}_{1}(x):={\mathds{1}}\{a\in{\mathcal{A}}^{\star}(x)\},\qquad a\sim P_{\theta}(\cdot\mid x).

[88] h6: Proposition 3.2 (Bias–variance of single-sample evaluation) .

[89] p: The single-sample evaluator satisfies:

[90] table: (3.4) Bias ⁡ ( ℰ 1 ​ ( x ) ) \displaystyle\Bias(\mathcal{E}_{1}(x)) = 0 , \displaystyle=0, (3.5) Var ⁡ ( ℰ 1 ​ ( x ) ∣ x ) \displaystyle\Var(\mathcal{E}_{1}(x)\mid x) = p ⋆ ​ ( x ) ​ ( 1 − p ⋆ ​ ( x ) ) . \displaystyle=p^{\star}(x)(1-p^{\star}(x)).

[91] p: The variance is maximized at p ⋆ ​ ( x ) = 1 / 2 p^{\star}(x)=1/2 (the hardest queries) and equals 1 / 4 1/4 .

[92] h6: Proof.

[93] p: 𝔼 ⁡ [ ℰ 1 ​ ( x ) ∣ x ] = P θ ​ ( a ∈ 𝒜 ⋆ ​ ( x ) ) = p ⋆ ​ ( x ) {\mathbb{E}}[\mathcal{E}_{1}(x)\mid x]=P_{\theta}(a\in{\mathcal{A}}^{\star}(x))=p^{\star}(x) , so the bias is zero. The variance follows from Var ⁡ ( Bernoulli ⁡ ( p ) ) = p ⁡ ( 1 − p ) \Var(\mathrm{Bernoulli}(p))=p(1-p) . ∎

[94] h6: Remark 3.3 (Unbiased but unreliable) .

[95] p: Single-sample evaluation is unbiased but has maximum variance exactly where it matters most: on queries where the agent is uncertain ( p ⋆ ​ ( x ) ≈ 1 / 2 p^{\star}(x)\approx 1/2 ). For a single query, the evaluation is essentially a coin flip when the agent is mediocre. This variance does not decrease without additional samples.

[96] h4: 3.2.2. LLM-as-judge evaluation

[97] p: An LLM judge J J scores the agent’s output:

[98] table: ℰ J ( x ) := J ( x , a ) , a ∼ P θ ( ⋅ ∣ x ) , \mathcal{E}_{J}(x):=J(x,a),\qquad a\sim P_{\theta}(\cdot\mid x),

[99] p: where J : 𝒳 × 𝒜 → [ 0 , 1 ] J:{\mathcal{X}}\times{\mathcal{A}}\to[0,1] is stochastic (the judge itself has sampling variance).

[100] h6: Proposition 3.4 (Bias–variance of LLM-as-judge evaluation) .

[101] p: Define the judge’s systematic bias on query x x with answer a a as

[102] table: (3.6) b J ​ ( x , a ) := 𝔼 ⁡ [ J ⁡ ( x , a ) ] − Accept ⁡ ( x , a ) . b_{J}(x,a):={\mathbb{E}}[J(x,a)]-\mathrm{Accept}(x,a).

[103] p: Then:

[104] table: (3.7) Bias 2 ⁡ ( ℰ J ​ ( x ) ) \displaystyle\Bias^{2}(\mathcal{E}_{J}(x)) = ( 𝔼 a ​ [ b J ​ ( x , a ) ] ) 2 , \displaystyle=\bigl({\mathbb{E}}_{a}[b_{J}(x,a)]\bigr)^{2}, (3.8) Var ⁡ ( ℰ J ​ ( x ) ∣ x ) \displaystyle\Var(\mathcal{E}_{J}(x)\mid x) = Var a ⁡ ( Accept ⁡ ( x , a ) ) ⏟ agent variance + 𝔼 a ​ [ Var ⁡ ( J ⁡ ( x , a ) ∣ x , a ) ] ⏟ judge variance + Var a ⁡ ( b J ​ ( x , a ) ) ⏟ bias variance . \displaystyle=\underbrace{\Var_{a}(\mathrm{Accept}(x,a))}_{\text{agent variance}}+\underbrace{{\mathbb{E}}_{a}[\Var(J(x,a)\mid x,a)]}_{\text{judge variance}}+\underbrace{\Var_{a}(b_{J}(x,a))}_{\text{bias variance}}.

[105] h6: Proof.

[106] p: Write ℰ J ​ ( x ) = Accept ⁡ ( x , a ) + b J ​ ( x , a ) + η J ​ ( x , a ) \mathcal{E}_{J}(x)=\mathrm{Accept}(x,a)+b_{J}(x,a)+\eta_{J}(x,a) , where η J \eta_{J} is the zero-mean judge noise. By the law of total variance:

[107] table: 𝔼 ​ [ ℰ J ​ ( x ) ∣ x ] \displaystyle{\mathbb{E}}[\mathcal{E}_{J}(x)\mid x] = 𝔼 a ​ [ Accept ⁡ ( x , a ) + b J ​ ( x , a ) ] = p ⋆ ​ ( x ) + 𝔼 a ​ [ b J ​ ( x , a ) ] . \displaystyle={\mathbb{E}}_{a}[\mathrm{Accept}(x,a)+b_{J}(x,a)]=p^{\star}(x)+{\mathbb{E}}_{a}[b_{J}(x,a)].

[108] p: Hence Bias ⁡ ( ℰ J ​ ( x ) ) = 𝔼 a ​ [ b J ​ ( x , a ) ] \Bias(\mathcal{E}_{J}(x))={\mathbb{E}}_{a}[b_{J}(x,a)] , giving ( 3.7 ). The variance decomposes by conditioning on a a and using independence of η J \eta_{J} from the other terms. ∎

[109] h6: Remark 3.5 (Judge bias is irreducible) .

[110] p: The critical flaw of LLM-as-judge is that the bias term 𝔼 a ​ [ b J ​ ( x , a ) ] {\mathbb{E}}_{a}[b_{J}(x,a)] does not decrease with more judge calls or more agent samples. If the judge systematically overrates verbose answers or underrates unconventional but correct solutions, this error persists regardless of sample size. Furthermore, b J b_{J} is unknown and difficult to estimate without ground-truth labels—the very thing evaluation is meant to replace.

[111] h4: 3.2.3. Naive self-consistency (mode selection)

[112] p: Draw K K samples, canonicalize, and check whether the most frequent answer is acceptable:

[113] table: ℰ SC ( x ) := 𝟙 { c ( 1 ) ∈ Canon ( x , 𝒜 ⋆ ( x ) ) } . \mathcal{E}_{\mathrm{SC}}(x):={\mathds{1}}\{c_{(1)}\in\mathrm{Canon}(x,{\mathcal{A}}^{\star}(x))\}.

[114] h6: Proposition 3.6 (Bias–variance of mode selection) .

[115] p: Let p := p ⋆ ​ ( x ) p:=p^{\star}(x) be the acceptability rate under canonicalization. If p > 1 / 2 p>1/2 :

[116] table: (3.9) Bias ⁡ ( ℰ SC ​ ( x ) ) \displaystyle\Bias(\mathcal{E}_{\mathrm{SC}}(x)) = 0 , \displaystyle=0, (3.10) Var ⁡ ( ℰ SC ​ ( x ) ∣ x ) \displaystyle\Var(\mathcal{E}_{\mathrm{SC}}(x)\mid x) ≤ exp ⁡ ( − 2 ​ K ​ ( p − 1 2 ) 2 ) . \displaystyle\leq\exp\!\left(-2K\left(p-\tfrac{1}{2}\right)^{2}\right).

[117] p: If p ≤ 1 / 2 p\leq 1/2 (systematic bias):

[118] table: (3.11) Bias ⁡ ( ℰ SC ​ ( x ) ) \displaystyle\Bias(\mathcal{E}_{\mathrm{SC}}(x)) → − p as ​ K → ∞ , \displaystyle\to-p\quad\text{as }K\to\infty, (3.12) Var ⁡ ( ℰ SC ​ ( x ) ∣ x ) \displaystyle\Var(\mathcal{E}_{\mathrm{SC}}(x)\mid x) → 0 as ​ K → ∞ . \displaystyle\to 0\quad\text{as }K\to\infty.

[119] h6: Proof.

[120] p: When p > 1 / 2 p>1/2 , the mode is the correct class with probability ≥ 1 − exp ⁡ ( − 2 ​ K ​ ( p − 1 / 2 ) 2 ) \geq 1-\exp(-2K(p-1/2)^{2}) by Hoeffding’s inequality [ Hoeffding1963 ] , giving zero asymptotic bias and exponentially decaying variance.

[121] p: When p ≤ 1 / 2 p\leq 1/2 , the total mass on incorrect canonical classes is 1 − p ≥ 1 / 2 1-p\geq 1/2 . By the law of large numbers, the empirical frequency of each class converges to its true probability as K → ∞ K\to\infty . Let q max := max c ∉ Canon ⁡ ( x , 𝒜 ⋆ ​ ( x ) ) ⁡ P θ ​ ( c ∣ x ) q_{\max}:=\max_{c\notin\mathrm{Canon}(x,{\mathcal{A}}^{\star}(x))}P_{\theta}(c\mid x) be the mass of the most probable incorrect class. If q max > p q_{\max}>p , the mode is this incorrect class a.s. If q max ≤ p q_{\max}\leq p , then p ≤ 1 / 2 p\leq 1/2 implies the correct class shares the maximum with at least one incorrect class; by our tie-breaking convention (uniform random), the mode is incorrect with positive probability, and by symmetry as K → ∞ K\to\infty it is incorrect a.s. whenever the correct class is not the unique mode. In either case, ℰ SC ​ ( x ) → 0 \mathcal{E}_{\mathrm{SC}}(x)\to 0 a.s. while p ⋆ ​ ( x ) = p > 0 p^{\star}(x)=p>0 , yielding Bias → − p \Bias\to-p . ∎

[122] h6: Remark 3.7 (The self-consistency double-edged sword) .

[123] p: Proposition 3.6 reveals a fundamental asymmetry: self-consistency is excellent for variance reduction when the agent is mostly correct ( p > 1 / 2 p>1/2 ), but it amplifies confidence in errors when the agent is systematically wrong ( p ≤ 1 / 2 p\leq 1/2 ). More samples make the wrong answer look more certain. This is the “stable hallucination” phenomenon. Any framework that uses self-consistency must account for this failure mode.

[124] h6: Remark 3.8 (The i.i.d. sampling assumption) .

[125] p: Proposition 3.6 and Theorem 4.4 assume a 1 , … , a K ∼ i.i.d. P θ ( ⋅ ∣ x ) a_{1},\dots,a_{K}\overset{\text{i.i.d.}}{\sim}P_{\theta}(\cdot\mid x) . This is well-justified when each sample is an independent, stateless API call to a fixed model at temperature T > 0 T>0 with deterministic canonicalization (e.g., code execution, string normalization). In practice, positive correlation ρ > 0 \rho>0 between samples can arise from model-version drift during data collection, stochastic canonicalization (e.g., an LLM judge), or infrastructure-level batching effects. Under ρ \rho -correlated samples the effective sample size drops to K eff ≈ K / ( 1 + ( K − 1 ) ​ ρ ) K_{\mathrm{eff}}\approx K/(1+(K{-}1)\rho) , and the Hoeffding bound degrades to exp ⁡ ( − 2 ​ K eff ​ ( p − 1 2 ) 2 ) \exp(-2K_{\mathrm{eff}}(p-\tfrac{1}{2})^{2}) . The qualitative conclusion—more samples reduce variance—survives, but at a slower rate. Crucially, the conformal coverage guarantee (Theorem 6.7 ) depends only on exchangeability of the calibration and test data, not on i.i.d. agent samples, and is therefore unaffected.

[126] h3: 3.3. The bias–variance landscape: a summary

[127] figure: Table 1. Bias–variance profile of evaluation methods (per-query). K K = number of samples, n n = calibration set size. Method Bias Variance Error → 0 \to 0 ? Guarantee Single sample 0 0 p ⋆ ​ ( 1 − p ⋆ ) p^{\star}(1{-}p^{\star}) No — LLM-as-judge 𝔼 a ​ [ b J ] ≠ 0 {\mathbb{E}}_{a}[b_{J}]\neq 0 (irreducible) Prop. 3.4 † No (bias persists) — Self-consistency (mode) 0 0 if p ⋆ > 1 2 p^{\star}{>}\tfrac{1}{2} ; → − p ⋆ \to{-}p^{\star} if p ⋆ ≤ 1 2 p^{\star}{\leq}\tfrac{1}{2} ≤ exp ⁡ ( − 2 ​ K ​ ( p ⋆ − 1 2 ) 2 ) \leq\exp(-2K(p^{\star}{-}\tfrac{1}{2})^{2}) No (bias if p ⋆ ≤ 1 2 p^{\star}{\leq}\tfrac{1}{2} ) — Ours (conformal) Coverage gap ≤ 1 / ( n + 1 ) \leq 1/(n{+}1) Yes ( → 0 \to 0 as n → ∞ n\to\infty ) ℙ ⁡ ( Y ∈ S ) ≥ 1 − α {\mathbb{P}}(Y{\in}S)\geq 1{-}\alpha † Three-term decomposition: agent variance + + judge variance + + bias variance; does not vanish with more samples.

[128] p: The key observation from Table 1 is that no existing method simultaneously controls bias and variance while providing a formal guarantee. Our framework achieves this by (i) using self-consistency for variance reduction, (ii) outputting a set rather than a point to absorb residual bias, and (iii) calibrating the set via conformal prediction to obtain an exact, distribution-free coverage guarantee.

[129] h2: 4. Self-Consistency Sampling and Canonicalization

[130] h3: 4.1. Self-consistency sampling

[131] p: For a fixed query x ∈ 𝒳 x\in{\mathcal{X}} , we draw K K independent samples from the agent:

[132] table: (4.1) a 1 , a 2 , … , a K ∼ i.i.d. P θ ( ⋅ ∣ x ) . a_{1},a_{2},\dots,a_{K}\overset{\text{i.i.d.}}{\sim}P_{\theta}(\cdot\mid x).

[133] p: The empirical distribution over raw answers is

[134] table: P ^ K ( a ∣ x ) = 1 K ∑ i = 1 K 𝟙 { a i = a } . \hat{P}_{K}(a\mid x)=\frac{1}{K}\sum_{i=1}^{K}{\mathds{1}}\{a_{i}=a\}.

[135] h3: 4.2. Canonicalization

[136] p: Different surface forms can express the same answer—“42,” “42.0,” and “The answer is 42” all mean the same thing. Canonicalization maps these to a single representative so that frequency counts reflect semantic agreement, not superficial variation.

[137] h6: Definition 4.1 (Canonicalization) .

[138] p: A canonicalization function is a mapping

[139] table: Canon : 𝒳 × 𝒜 → 𝒞 , \mathrm{Canon}:{\mathcal{X}}\times{\mathcal{A}}\to{\mathcal{C}},

[140] p: where 𝒞 {\mathcal{C}} is a space of canonical representations. We require that Canon \mathrm{Canon} respects semantic equivalence: if a ≃ a ′ a\simeq a^{\prime} semantically, then Canon ⁡ ( x , a ) = Canon ⁡ ( x , a ′ ) \mathrm{Canon}(x,a)=\mathrm{Canon}(x,a^{\prime}) .

[141] p: Applying canonicalization yields the empirical canonical distribution:

[142] table: (4.2) P ^ K ( c ∣ x ) = 1 K ∑ i = 1 K 𝟙 { Canon ( x , a i ) = c } . \hat{P}_{K}(c\mid x)=\frac{1}{K}\sum_{i=1}^{K}{\mathds{1}}\{\mathrm{Canon}(x,a_{i})=c\}.

[143] h3: 4.3. Canonicalization: implementation and stability

[144] p: Since the quality of the consensus vote depends directly on the quality of Canon \mathrm{Canon} , we treat canonicalization as a first-class algorithmic component. Three regimes arise in practice:

[145] p: Deterministic canonicalization for structured answers—parse “42.0” and “42” to the same integer, match option letters in MCQ tasks, or execute code and record pass/fail. This eliminates surface-form variation entirely.

[146] p: Embedding-based clustering for open-ended tasks, using cosine similarity thresholds on dense embeddings to group semantically equivalent responses.

[147] p: LLM-assisted canonicalization , where a lightweight model (e.g., GPT-4.1 at temperature 0 0 ) classifies each response as correct or incorrect before clustering.

[148] p: Each approach involves specific failure modes (over-merging vs. under-merging). Implementation details, stability diagnostics, and empirical requirements are in Appendix A .

[149] h6: Assumption 4.2 (Canonicalization quality) .

[150] p: Throughout the theoretical analysis (Sections 4.4 – 7 ), we assume that Canon \mathrm{Canon} correctly maps semantically equivalent answers to the same canonical class. When this assumption is violated, the variance reduction guarantees (Theorem 4.4 ) degrade gracefully: under-merging reduces p canon p_{\mathrm{canon}} , increasing the required K K , while the conformal coverage guarantee (Theorem 6.7 ) remains valid regardless (set sizes simply grow to compensate).

[151] h6: Remark 4.3 (LLM-based canonicalization and circularity) .

[152] p: When canonicalization uses an LLM judge (regime (iii) above), a potential circularity arises: if the same model family serves as both agent and canonicalizer, systematic biases could propagate. For instance, the judge might systematically group incorrect answers into a “correct” cluster due to self-preference or verbosity bias, corrupting the consensus vote. Three considerations mitigate this concern:

[153] p: (a) Functional separation. In our experiments, the canonicalizer (GPT-4.1 at temperature 0 0 , producing deterministic binary labels) operates in a fundamentally different regime from the agent (GPT-4.1 at temperature 0.7 0.7 , generating stochastic free-form responses). At T = 0 T{=}0 , the judge is a fixed deterministic function—analogous to code execution or regex matching—not a stochastic evaluator. The bias profiles of deterministic classification and stochastic generation are distinct.

[154] p: (b) Coverage guarantee is robust to canonicalization errors. Assumption 4.2 states the key safeguard: if the canonicalizer makes errors (merging incorrect answers with correct ones, or splitting correct answers), the conformal coverage guarantee (Theorem 6.7 ) remains valid. Canonicalization errors manifest as inflated prediction set sizes , not as invalid coverage—the framework honestly reflects that canonicalization is noisy by returning larger sets.

[155] p: (c) Cross-family validation breaks the self-preference loop. Our open-weight experiments provide a direct test: Llama 4 Maverick and Mistral Small 24B are canonicalized by GPT-4.1—a different model family with different training data and biases. If within-family self-preference were corrupting canonicalization, cross-family results would diverge. They do not: coverage ( ≥ 0.960 \geq 0.960 ) and conditional coverage ( ≥ 0.949 \geq 0.949 ) are consistent across all three families (Table 3 ).

[156] p: For maximal rigor, we recommend deterministic canonicalization (code execution, numeric extraction, option matching) wherever feasible, reserving LLM-based canonicalization for tasks where no alternative exists. Three of our five benchmarks use deterministic canonicalization.

[157] h3: 4.4. Variance reduction via consensus aggregation

[158] p: We now prove that self-consistency sampling achieves exponential variance reduction for identifying the correct answer, and that canonicalization further amplifies this effect.

[159] h6: Theorem 4.4 (Exponential variance reduction via consensus) .

[160] p: Let c ⋆ ∈ 𝒞 c^{\star}\in{\mathcal{C}} be the unique acceptable canonical class for query x x , and let p := P θ ​ ( Canon ⁡ ( x , f θ ​ ( x ) ) = c ⋆ ) > 1 / 2 p:=P_{\theta}(\mathrm{Canon}(x,f_{\theta}(x))=c^{\star})>1/2 . Then after K K i.i.d. samples:

[161] p: Mode correctness:

[162] table: (4.3) ℙ ⁡ ( c ( 1 ) ≠ c ⋆ ) ≤ exp ⁡ ( − 2 ​ K ​ ( p − 1 2 ) 2 ) . {\mathbb{P}}(c_{(1)}\neq c^{\star})\leq\exp\!\left(-2K\left(p-\tfrac{1}{2}\right)^{2}\right).

[163] p: Rank concentration: For any r ≥ 2 r\geq 2 ,

[164] table: (4.4) ℙ ⁡ ( rank ⁡ ( c ⋆ , x ) ≥ r ) ≤ ( | 𝒞 | r − 1 ) ​ exp ⁡ ( − K ​ ( p − ( 1 − p ) / ( r − 1 ) ) 2 2 ) , {\mathbb{P}}(\mathrm{rank}(c^{\star};x)\geq r)\leq\binom{|{\mathcal{C}}|}{r-1}\exp\!\left(-\frac{K(p-(1-p)/(r-1))^{2}}{2}\right),

[165] p: where | 𝒞 | |{\mathcal{C}}| is the number of distinct canonical classes and the bound is nontrivial when p > ( 1 − p ) / ( r − 1 ) p>(1-p)/(r-1) .

[166] p: Variance decay:

[167] table: (4.5) Var ( 𝟙 { c ( 1 ) = c ⋆ } ) ≤ exp ( − 2 K ( p − 1 2 ) 2 ) . \Var\bigl({\mathds{1}}\{c_{(1)}=c^{\star}\}\bigr)\leq\exp\!\left(-2K\left(p-\tfrac{1}{2}\right)^{2}\right).

[168] h6: Proof.

[169] p: Part 1. The correct class c ⋆ c^{\star} has count N ⋆ = ∑ i = 1 K 𝟙 { c i = c ⋆ } ∼ Bin ( K , p ) N^{\star}=\sum_{i=1}^{K}{\mathds{1}}\{c_{i}=c^{\star}\}\sim\mathrm{Bin}(K,p) . The mode is incorrect only if some other class has count ≥ N ⋆ \geq N^{\star} . Since the total count of all incorrect classes is K − N ⋆ K-N^{\star} , a necessary condition is K − N ⋆ ≥ N ⋆ K-N^{\star}\geq N^{\star} , i.e., N ⋆ ≤ K / 2 N^{\star}\leq K/2 . By Hoeffding’s inequality:

[170] table: ℙ ⁡ ( N ⋆ ≤ K / 2 ) = ℙ ⁡ ( N ⋆ K ≤ 1 2 ) ≤ exp ⁡ ( − 2 ​ K ​ ( p − 1 2 ) 2 ) . {\mathbb{P}}(N^{\star}\leq K/2)={\mathbb{P}}\!\left(\frac{N^{\star}}{K}\leq\frac{1}{2}\right)\leq\exp\!\left(-2K\left(p-\frac{1}{2}\right)^{2}\right).

[171] p: Part 2. rank ⁡ ( c ⋆ ) ≥ r \mathrm{rank}(c^{\star})\geq r requires at least r − 1 r-1 classes to beat c ⋆ c^{\star} ’s count. Fix any set T T of r − 1 r-1 incorrect classes. Their combined mass is p T ≤ 1 − p p_{T}\leq 1-p . For each c ′ ∈ T c^{\prime}\in T to beat c ⋆ c^{\star} , we need n ⁡ ( c ′ ) > n ⁡ ( c ⋆ ) n(c^{\prime})>n(c^{\star}) , which in particular requires the average count of T T to exceed K ​ p / ( r − 1 ) Kp/(r-1) . By Hoeffding applied to the sum of counts in T T :

[172] table: ℙ ⁡ ( all ​ c ′ ∈ T ​ beat ​ c ⋆ ) ≤ ℙ ⁡ ( 1 K ​ ∑ c ′ ∈ T n ⁡ ( c ′ ) > p ) ≤ exp ⁡ ( − K ​ ( p − p T ) 2 2 ) . {\mathbb{P}}(\text{all }c^{\prime}\in T\text{ beat }c^{\star})\leq{\mathbb{P}}\!\left(\frac{1}{K}\sum_{c^{\prime}\in T}n(c^{\prime})>p\right)\leq\exp\!\left(-\frac{K(p-p_{T})^{2}}{2}\right).

[173] p: A union bound over ( | 𝒞 | r − 1 ) \binom{|{\mathcal{C}}|}{r-1} choices of T T gives ( 4.4 ).

[174] p: Part 3. Let q K := ℙ ⁡ ( c ( 1 ) = c ⋆ ) ≥ 1 − exp ⁡ ( − 2 ​ K ​ ( p − 1 / 2 ) 2 ) q_{K}:={\mathbb{P}}(c_{(1)}=c^{\star})\geq 1-\exp(-2K(p-1/2)^{2}) . Then Var ( 𝟙 { c ( 1 ) = c ⋆ } ) = q K ( 1 − q K ) ≤ 1 − q K ≤ exp ( − 2 K ( p − 1 / 2 ) 2 ) \Var({\mathds{1}}\{c_{(1)}=c^{\star}\})=q_{K}(1-q_{K})\leq 1-q_{K}\leq\exp(-2K(p-1/2)^{2}) . ∎

[175] h6: Corollary 4.5 (Sample complexity for δ \delta -reliable mode identification) .

[176] p: To ensure ℙ ⁡ ( c ( 1 ) = c ⋆ ) ≥ 1 − δ {\mathbb{P}}(c_{(1)}=c^{\star})\geq 1-\delta , it suffices to take

[177] table: (4.6) K ≥ ln ⁡ ( 1 / δ ) 2 ​ ( p − 1 / 2 ) 2 . K\geq\frac{\ln(1/\delta)}{2(p-1/2)^{2}}.

[178] p: For example, with p = 0.7 p=0.7 and δ = 0.01 \delta=0.01 : K ≥ ⌈ ln ⁡ ( 100 ) / ( 2 ⋅ 0.04 ) ⌉ = 58 K\geq\lceil\ln(100)/(2\cdot 0.04)\rceil=58 .

[179] h3: 4.5. Canonicalization as variance reduction

[180] p: Canonicalization does more than enable aggregation—it provably reduces the variance of the consensus by consolidating fragmented probability mass.

[181] h6: Proposition 4.6 (Canonicalization amplifies consensus) .

[182] p: Let p raw := max a ∈ 𝒜 ⋆ ​ ( x ) ⁡ P θ ​ ( a ∣ x ) p_{\mathrm{raw}}:=\max_{a\in{\mathcal{A}}^{\star}(x)}P_{\theta}(a\mid x) be the probability of the most likely acceptable raw answer, and p canon := P θ ​ ( Canon ⁡ ( x , f θ ​ ( x ) ) ∈ Canon ⁡ ( x , 𝒜 ⋆ ​ ( x ) ) ) p_{\mathrm{canon}}:=P_{\theta}(\mathrm{Canon}(x,f_{\theta}(x))\in\mathrm{Canon}(x,{\mathcal{A}}^{\star}(x))) the probability of the acceptable canonical class . Then:

[183] table: (4.7) p canon ≥ p raw , p_{\mathrm{canon}}\geq p_{\mathrm{raw}},

[184] p: with equality only when canonicalization is the identity. If L L raw answers map to the same acceptable canonical class, each with probability ≥ p min \geq p_{\min} , then p canon ≥ L ⋅ p min p_{\mathrm{canon}}\geq L\cdot p_{\min} .

[185] p: Consequently, the variance reduction exponent improves from 2 ​ K ​ ( p raw − 1 / 2 ) 2 2K(p_{\mathrm{raw}}-1/2)^{2} to 2 ​ K ​ ( p canon − 1 / 2 ) 2 2K(p_{\mathrm{canon}}-1/2)^{2} , and the sample complexity ( 4.6 ) decreases by a factor of ( ( p raw − 1 / 2 ) / ( p canon − 1 / 2 ) ) 2 \bigl((p_{\mathrm{raw}}-1/2)/(p_{\mathrm{canon}}-1/2)\bigr)^{2} .

[186] h6: Proof.

[187] p: By definition, p canon = ∑ a : Canon ⁡ ( x , a ) = c ⋆ P θ ( a ∣ x ) ≥ max a P θ ( a ∣ x ) ⋅ 𝟙 { a ∈ 𝒜 ⋆ ( x ) } = p raw p_{\mathrm{canon}}=\sum_{a:\mathrm{Canon}(x,a)=c^{\star}}P_{\theta}(a\mid x)\geq\max_{a}P_{\theta}(a\mid x)\cdot{\mathds{1}}\{a\in{\mathcal{A}}^{\star}(x)\}=p_{\mathrm{raw}} . The improvement in the Hoeffding exponent follows directly from substituting p canon p_{\mathrm{canon}} for p raw p_{\mathrm{raw}} in ( 4.3 ). ∎

[188] h6: Remark 4.7 (Canonicalization can change the p ≤ 1 / 2 p\leq 1/2 regime) .

[189] p: A crucial practical consequence: an agent may have p raw < 1 / 2 p_{\mathrm{raw}}<1/2 (no single raw answer dominates) but p canon > 1 / 2 p_{\mathrm{canon}}>1/2 (the correct canonical class dominates after consolidation). Canonicalization can transform a regime where self-consistency amplifies bias into one where it reduces variance. This provides a formal justification for investing in high-quality canonicalization.

[190] h3: 4.6. Ranked consensus

[191] p: We rank distinct canonical answers by decreasing empirical frequency:

[192] table: (4.8) rank ⁡ ( c , x ) := | { c ′ ∈ 𝒞 ⁡ ( x ) : P ^ K ​ ( c ′ ∣ x ) > P ^ K ​ ( c ∣ x ) } | + 1 , \mathrm{rank}(c;x):=\bigl|\{c^{\prime}\in{\mathcal{C}}(x):\hat{P}_{K}(c^{\prime}\mid x)>\hat{P}_{K}(c\mid x)\}\bigr|+1,

[193] p: with ties broken uniformly at random, producing an ordering c ( 1 ) , c ( 2 ) , … c_{(1)},c_{(2)},\dots .

[194] h6: Definition 4.8 (Consensus strength and margin) .

[195] p: The consensus strength is ϕ ⁡ ( x ) := P ^ K ​ ( c ( 1 ) ∣ x ) \phi(x):=\hat{P}_{K}(c_{(1)}\mid x) and the consensus margin is Δ ⁡ ( x ) := P ^ K ​ ( c ( 1 ) ∣ x ) − P ^ K ​ ( c ( 2 ) ∣ x ) \Delta(x):=\hat{P}_{K}(c_{(1)}\mid x)-\hat{P}_{K}(c_{(2)}\mid x) .

[196] p: Consensus strength measures the model’s overall confidence (does one answer dominate, or do many answers tie?). Consensus margin measures the gap between the top two—a large margin means the model strongly favors one answer. Both quantities feed into the sequential stopping rule (Section 9 ).

[197] p: With the ranked consensus in hand, we now construct prediction sets that adapt their size to each query’s difficulty.

[198] h2: 5. Set-Valued Predictions

[199] p: Instead of committing to a single answer, we output the top M M most frequent candidates. For easy questions, M = 1 M{=}1 suffices; for hard ones, a larger M M is needed. The key question is how to choose M M with a guarantee—that is the role of conformal calibration in the next section.

[200] p: Given ranked canonical answers c ( 1 ) , c ( 2 ) , … c_{(1)},c_{(2)},\dots for query x x , define the top- M M prediction set :

[201] table: (5.1) S M ​ ( x ) := { c ( 1 ) , c ( 2 ) , … , c ( M ) } . S_{M}(x):=\{c_{(1)},c_{(2)},\dots,c_{(M)}\}.

[202] p: The family { S M ​ ( x ) } M ≥ 1 \{S_{M}(x)\}_{M\geq 1} is nested: S 1 ​ ( x ) ⊆ S 2 ​ ( x ) ⊆ ⋯ S_{1}(x)\subseteq S_{2}(x)\subseteq\cdots .

[203] p: A fixed M M ignores the varying difficulty of queries. We seek a data-driven procedure that selects M = M ⁡ ( x ) M=M(x) adaptively with a formal coverage guarantee—the setting of conformal prediction .

[204] h2: 6. Conformal Calibration

[205] h3: 6.1. Background: split conformal prediction

[206] p: Conformal prediction [ Vovk2005 , Angelopoulos2021 ] is a distribution-free framework for constructing prediction sets with guaranteed marginal coverage. Its single requirement is that calibration and test data are interchangeable—their joint distribution does not depend on ordering.

[207] h6: Definition 6.1 (Exchangeability) .

[208] p: Random variables Z 1 , … , Z n + 1 Z_{1},\dots,Z_{n+1} are exchangeable if their joint distribution is invariant under all permutations σ \sigma :

[209] table: ( Z 1 , … , Z n + 1 ) ​ = 𝑑 ​ ( Z σ ⁡ ( 1 ) , … , Z σ ⁡ ( n + 1 ) ) . (Z_{1},\dots,Z_{n+1})\overset{d}{=}(Z_{\sigma(1)},\dots,Z_{\sigma(n+1)}).

[210] h3: 6.2. Nonconformity scores from ranked consensus

[211] p: The nonconformity score measures how “surprising” the correct answer is in the ranked list. If the correct answer is the most frequent ( rank = 1 \text{rank}=1 ), the model is confident and the score is low. If the correct answer is buried at rank 5 5 , the score is high—the model’s consensus disagrees with the truth.

[212] h6: Definition 6.2 (Rank-based nonconformity score) .

[213] p: Let x x be a query, { c ( 1 ) , c ( 2 ) , … } \{c_{(1)},c_{(2)},\dots\} the ranked canonical answers from K K self-consistency samples, and y ∈ 𝒜 ⋆ ​ ( x ) y\in{\mathcal{A}}^{\star}(x) an acceptable answer with canonical form c y := Canon ⁡ ( x , y ) c^{y}:=\mathrm{Canon}(x,y) . The rank-based nonconformity score is

[214] table: (6.1) s ⁡ ( x , y ) := rank ⁡ ( c y , x ) = min ⁡ { r ∈ ℕ : c y ∈ S r ​ ( x ) } . s(x,y):=\mathrm{rank}(c^{y};x)=\min\{r\in{\mathbb{N}}:c^{y}\in S_{r}(x)\}.

[215] p: If c y ∉ 𝒞 ⁡ ( x ) c^{y}\notin{\mathcal{C}}(x) , set s ⁡ ( x , y ) := + ∞ s(x,y):=+\infty .

[216] h6: Definition 6.3 (Cumulative-probability nonconformity score) .

[217] p: An alternative score incorporating frequency information:

[218] table: (6.2) s cp ​ ( x , y ) := ∑ r = 1 rank ⁡ ( c y , x ) P ^ K ​ ( c ( r ) ∣ x ) ∈ [ 0 , 1 ] . s^{\mathrm{cp}}(x,y):=\sum_{r=1}^{\mathrm{rank}(c^{y};x)}\hat{P}_{K}(c_{(r)}\mid x)\in[0,1].

[219] h3: 6.3. The calibration procedure

[220] h6: Assumption 6.4 (Calibration data) .

[221] p: We have a calibration dataset 𝒟 cal = { ( x i , y i ) } i = 1 n {\mathcal{D}}_{\mathrm{cal}}=\{(x_{i},y_{i})\}_{i=1}^{n} where each y i ∈ 𝒜 ⋆ ​ ( x i ) y_{i}\in{\mathcal{A}}^{\star}(x_{i}) , drawn exchangeably with the test example ( x n + 1 , y n + 1 ) (x_{n+1},y_{n+1}) .

[222] h6: Remark 6.5 (When exchangeability holds and when it breaks) .

[223] p: Exchangeability is satisfied when calibration and test examples are drawn i.i.d. from the same distribution—the standard setting of benchmark evaluation with random train/test splits. It also holds under random subsampling from any fixed dataset, regardless of how the dataset was originally constructed.

[224] p: Exchangeability can be violated in several practically relevant scenarios:

[225] p: Curated benchmark sets : if items were hand-selected to emphasize difficult cases or specific capabilities, the calibration and test distributions may differ systematically.

[226] p: Temporal drift : if the agent is updated between calibration and deployment, the score distribution shifts. Periodic recalibration (re-running the calibration procedure on fresh data from the updated agent) is the standard mitigation.

[227] p: Adversarial construction : if test queries are chosen adversarially after observing the calibration set, exchangeability fails by design. This is outside our threat model.

[228] p: When exchangeability is only approximately satisfied (e.g., mild covariate shift between calibration and test), weighted conformal prediction (Section 10.3 ) provides a principled correction by reweighting calibration scores according to the likelihood ratio p test ​ ( x ) / p cal ​ ( x ) p_{\mathrm{test}}(x)\allowbreak/p_{\mathrm{cal}}(x) , preserving coverage under the test distribution.

[229] p: For each calibration example ( x i , y i ) (x_{i},y_{i}) :

[230] p: Draw K K self-consistency samples for query x i x_{i} ; canonicalize and rank.

[231] p: Compute s i := s ⁡ ( x i , y i ) s_{i}:=s(x_{i},y_{i}) .

[232] h6: Definition 6.6 (Conformal threshold) .

[233] p: Define k := ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ k:=\lceil(n+1)(1-\alpha)\rceil and

[234] table: (6.3) M ⋆ := s ( k ) , M^{\star}:=s_{(k)},

[235] p: the k k -th smallest calibration score.

[236] p: For a test query x n + 1 x_{n+1} , return:

[237] table: (6.4) S ⁡ ( x n + 1 ) := S M ⋆ ​ ( x n + 1 ) = { c ( 1 ) , … , c ( M ⋆ ) } . S(x_{n+1}):=S_{M^{\star}}(x_{n+1})=\{c_{(1)},\dots,c_{(M^{\star})}\}.

[238] h3: 6.4. Finite-sample coverage guarantee

[239] h6: Theorem 6.7 (Marginal coverage guarantee) .

[240] p: Let ( x 1 , y 1 ) , … , ( x n , y n ) , ( x n + 1 , y n + 1 ) (x_{1},y_{1}),\dots,(x_{n},y_{n}),(x_{n+1},y_{n+1}) be exchangeable, and let s i = s ⁡ ( x i , y i ) s_{i}=s(x_{i},y_{i}) . Define M ⋆ M^{\star} as in ( 6.3 ). Then:

[241] table: (6.5) ℙ ⁡ ( y n + 1 ∈ S M ⋆ ​ ( x n + 1 ) ) ≥ 1 − α . {\mathbb{P}}\bigl(y_{n+1}\in S_{M^{\star}}(x_{n+1})\bigr)\geq 1-\alpha.

[242] p: If the scores have no ties a.s.:

[243] table: (6.6) 1 − α ≤ ℙ ⁡ ( s n + 1 ≤ M ⋆ ) ≤ 1 − α + 1 n + 1 . 1-\alpha\;\leq\;{\mathbb{P}}\bigl(s_{n+1}\leq M^{\star}\bigr)\;\leq\;1-\alpha+\frac{1}{n+1}.

[244] h6: Proof.

[245] p: By exchangeability, the scores s 1 , … , s n + 1 s_{1},\dots,s_{n+1} are exchangeable. The rank of s n + 1 s_{n+1} among { s 1 , … , s n + 1 } \{s_{1},\dots,s_{n+1}\} is uniformly distributed over { 1 , … , n + 1 } \{1,\dots,n+1\} .

[246] p: Define k := ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ k:=\lceil(n+1)(1-\alpha)\rceil . The event { s n + 1 ≤ M ⋆ } \{s_{n+1}\leq M^{\star}\} occurs when s n + 1 s_{n+1} ’s rank is at most k k . In the no-ties case:

[247] table: ℙ ⁡ ( s n + 1 ≤ M ⋆ ) = k n + 1 = ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ n + 1 . {\mathbb{P}}(s_{n+1}\leq M^{\star})=\frac{k}{n+1}=\frac{\lceil(n+1)(1-\alpha)\rceil}{n+1}.

[248] p: Since ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ ≥ ( n + 1 ) ​ ( 1 − α ) \lceil(n+1)(1-\alpha)\rceil\geq(n+1)(1-\alpha) , we get ℙ ≥ 1 − α {\mathbb{P}}\geq 1-\alpha . Since ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ ≤ ( n + 1 ) ​ ( 1 − α ) + 1 \lceil(n+1)(1-\alpha)\rceil\leq(n+1)(1-\alpha)+1 , we get ℙ ≤ 1 − α + 1 / ( n + 1 ) {\mathbb{P}}\leq 1-\alpha+1/(n+1) .

[249] p: With ties, coverage can only increase. ∎

[250] h3: 6.5. Adaptive prediction sets

[251] p: Using the cumulative-probability score s cp s^{\mathrm{cp}} and its conformal quantile q ^ 1 − α cp \hat{q}^{\mathrm{cp}}_{1-\alpha} :

[252] table: (6.7) S cp ( x ) := { c ( r ) : r = 1 , … , R ( x ) } , R ( x ) := min { r : ∑ j = 1 r P ^ K ( c ( j ) ∣ x ) ≥ q ^ 1 − α cp } . S^{\mathrm{cp}}(x):=\bigl\{c_{(r)}:r=1,\dots,R(x)\bigr\},\quad R(x):=\min\!\left\{r:\sum_{j=1}^{r}\hat{P}_{K}(c_{(j)}\mid x)\geq\hat{q}^{\mathrm{cp}}_{1-\alpha}\right\}.

[253] p: For high-consensus queries, R ⁡ ( x ) R(x) is small; for diffuse queries, it is larger. Coverage is preserved by the same conformal argument.

[254] h2: 7. Reliability Guarantees

[255] p: Conformal set-valued evaluation is exactly calibrated : the evaluation’s coverage statement has bounded error. It is also transparently diagnostic of agent quality—agent bias is surfaced through prediction set size rather than hidden. These two properties distinguish the agent’s systematic errors (diagnosed but not fixed) from the evaluation’s systematic errors (provably controlled).

[256] h3: 7.1. Conservative coverage guarantee

[257] p: The evaluation’s coverage error shrinks to zero as the calibration set grows—unlike point estimators, where bias persists indefinitely.

[258] h6: Theorem 7.1 (Coverage error control) .

[259] p: Under the conditions of Theorem 6.7 , the coverage gap satisfies

[260] table: (7.1) 0 ≤ ℙ ⁡ ( Y n + 1 ∈ S ⁡ ( X n + 1 ) ) − ( 1 − α ) ≤ 1 n + 1 . 0\;\leq\;{\mathbb{P}}(Y_{n+1}\in S(X_{n+1}))-(1-\alpha)\;\leq\;\frac{1}{n+1}.

[261] p: That is, the evaluation is conservative (never under-covers) and the over-coverage vanishes as n → ∞ n\to\infty .

[262] h6: Proof.

[263] p: This is immediate from ( 6.6 ): the lower bound gives conservativeness, and the upper bound gives the 1 / ( n + 1 ) 1/(n+1) slack. ∎

[264] h6: Remark 7.2 (Contrast with score-based evaluation) .

[265] p: Conformal calibration is the only method whose evaluation error vanishes with sample size. For single-sample evaluation, the error analog is Var ⁡ ( p ⋆ ​ ( X ) ) \Var(p^{\star}(X)) , which depends on the query distribution and does not shrink. For LLM-as-judge, the error includes the irreducible judge bias 𝔼 ⁡ [ b J ] {\mathbb{E}}[b_{J}] (Remark 3.5 ). Neither can be eliminated by collecting more data.

[266] h3: 7.2. Bias immunity: coverage holds regardless of agent quality

[267] h6: Theorem 7.3 (Bias immunity of conformal coverage) .

[268] p: The coverage guarantee ( 6.5 ) holds for any agent f θ f_{\theta} , regardless of:

[269] p: the agent’s per-query acceptability rate p ⋆ ​ ( x ) p^{\star}(x) (including p ⋆ ​ ( x ) = 0 p^{\star}(x)=0 ),

[270] p: the presence of systematic bias or stable hallucinations,

[271] p: the output distribution P θ ( ⋅ ∣ x ) P_{\theta}(\cdot\mid x) ,

[272] p: the number of acceptable answers | 𝒜 ⋆ ​ ( x ) | |{\mathcal{A}}^{\star}(x)| .

[273] p: Formally: let Θ \Theta denote the space of all possible agent parameters. Then

[274] table: (7.2) inf θ ∈ Θ ℙ θ ​ ( Y n + 1 ∈ S ⁡ ( X n + 1 ) ) ≥ 1 − α , \inf_{\theta\in\Theta}{\mathbb{P}}_{\theta}\bigl(Y_{n+1}\in S(X_{n+1})\bigr)\geq 1-\alpha,

[275] p: where ℙ θ {\mathbb{P}}_{\theta} denotes the joint distribution over calibration data, agent samples, and the test example under agent θ \theta .

[276] h6: Proof.

[277] p: The proof of Theorem 6.7 uses only exchangeability of ( x i , y i ) (x_{i},y_{i}) , which is a property of the data-generating process, not of the agent. The agent enters only through the nonconformity scores s i s_{i} , and the conformal argument is valid for any score distribution. Specifically:

[278] p: For any fixed θ \theta , the scores s 1 , … , s n + 1 s_{1},\dots,s_{n+1} are determined by the exchangeable data ( x 1 , y 1 ) , … , ( x n + 1 , y n + 1 ) (x_{1},y_{1}),\allowbreak\dots,\allowbreak(x_{n+1},y_{n+1}) and the independent agent samples { a j ( i ) } \{a_{j}^{(i)}\} . Since agent samples for different queries are independent, and the ( x i , y i ) (x_{i},y_{i}) are exchangeable by assumption, the scores remain exchangeable. The uniform rank argument then yields ℙ θ ​ ( s n + 1 ≤ M ⋆ ) ≥ 1 − α {\mathbb{P}}_{\theta}(s_{n+1}\leq M^{\star})\geq 1{-}\alpha for every θ \theta . ∎

[279] h6: Remark 7.4 (What “bias immunity” means and does not mean) .

[280] p: Theorem 7.3 is about the evaluation’s accuracy, not the agent’s quality. It does not fix or remove agent bias. It guarantees that the coverage statement—“an acceptable answer lies in S ⁡ ( x ) S(x) with probability ≥ 1 − α \geq 1-\alpha ”—is true regardless of how biased the agent is.

[281] p: Concretely: a completely broken agent earns M ⋆ = + ∞ M^{\star}=+\infty (honestly reflecting failure), while a strong agent earns M ⋆ = 1 M^{\star}=1 . In both cases the coverage guarantee holds. A single calibration procedure is valid for any agent, including ones with unknown or adversarial bias profiles.

[282] h3: 7.3. Bias transparency: set size as honest quality diagnostic

[283] p: The prediction set size | S ⁡ ( x ) | |S(x)| is a diagnostic signal that faithfully reflects the agent’s quality. The following theorem makes this precise: (1) better agents get smaller sets; (2) perfect agents get singletons; (3) agents that cannot solve a task get infinitely large sets, honestly reflecting failure; (4) expected set size scales with average answer rank.

[284] h6: Theorem 7.5 (Bias transparency—set size reflects agent quality) .

[285] p: Let M ⋆ ​ ( θ , α ) M^{\star}(\theta,\alpha) denote the conformal threshold for agent θ \theta at level α \alpha . Then:

[286] p: Monotonicity in agent quality: If agent θ 1 \theta_{1} stochastically dominates agent θ 2 \theta_{2} in the sense that s i ( θ 1 ) ≤ st s i ( θ 2 ) s_{i}^{(\theta_{1})}\leq_{\mathrm{st}}s_{i}^{(\theta_{2})} for each calibration example i i (i.e., θ 1 \theta_{1} consistently produces acceptable answers at higher ranks), then

[287] table: (7.3) M ⋆ ​ ( θ 1 , α ) ≤ M ⋆ ​ ( θ 2 , α ) almost surely . M^{\star}(\theta_{1},\alpha)\leq M^{\star}(\theta_{2},\alpha)\quad\text{almost surely}.

[288] p: Perfect agent: If p ⋆ ​ ( x ) = 1 p^{\star}(x)=1 for all x x in the calibration distribution (the agent always produces acceptable answers), then s i = 1 s_{i}=1 for all i i , and M ⋆ = 1 M^{\star}=1 .

[289] p: Biased agent: Let β := ℙ X ​ ( p ⋆ ​ ( X ) < 1 / K ) \beta:={\mathbb{P}}_{X}(p^{\star}(X)<1/K) be the fraction of queries where the agent is unlikely to produce an acceptable answer. If β > α \beta>\alpha , then M ⋆ = + ∞ M^{\star}=+\infty (no finite prediction set suffices at level α \alpha ).

[290] p: Set size–bias correspondence: The expected set size satisfies

[291] table: (7.4) 𝔼 ⁡ [ | S ⁡ ( X ) | ] ≥ 𝔼 ⁡ [ rank ⁡ ( Canon ⁡ ( X , Y ⁡ ( X ) ) , X ) ] ⋅ ( 1 − α ) − O ⁡ ( 1 / n ) . {\mathbb{E}}[|S(X)|]\geq{\mathbb{E}}\!\left[\mathrm{rank}\bigl(\mathrm{Canon}(X,Y(X));\;X\bigr)\right]\cdot(1-\alpha)-O(1/n).

[292] h6: Proof.

[293] p: Part 1. If s i ( θ 1 ) ≤ st s i ( θ 2 ) s_{i}^{(\theta_{1})}\leq_{\mathrm{st}}s_{i}^{(\theta_{2})} for each i i , then the k k -th order statistic satisfies s ( k ) ( θ 1 ) ≤ s ( k ) ( θ 2 ) s_{(k)}^{(\theta_{1})}\leq s_{(k)}^{(\theta_{2})} stochastically.

[294] p: Part 2. If p ⋆ ​ ( x ) = 1 p^{\star}(x)=1 , then with probability 1 1 all K K samples are acceptable, so the acceptable canonical class has rank 1 1 : s i = 1 s_{i}=1 for all i i , and M ⋆ = s ( k ) = 1 M^{\star}=s_{(k)}=1 .

[295] p: Part 3. If p ⋆ ​ ( x i ) < 1 / K p^{\star}(x_{i})<1/K , then ℙ ⁡ ( s i = + ∞ ) ≥ ( 1 − 1 / K ) K ≥ e − 1 − o ⁡ ( 1 ) > 0 {\mathbb{P}}(s_{i}=+\infty)\geq(1-1/K)^{K}\geq e^{-1}-o(1)>0 . When β > α \beta>\alpha , the number of infinite scores exceeds n ​ β > n ​ α n\beta>n\alpha , so the ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ \lceil(n+1)(1-\alpha)\rceil -th score is + ∞ +\infty .

[296] p: Part 4. By definition, | S ⁡ ( X ) | = M ⋆ |S(X)|=M^{\star} for the global threshold. For the adaptive version, | S ⁡ ( X ) | ≥ rank ⁡ ( c Y ⁡ ( X ) , X ) |S(X)|\geq\mathrm{rank}(c^{Y(X)};X) whenever Y ⁡ ( X ) ∈ S ⁡ ( X ) Y(X)\in S(X) . Taking expectations and using ℙ ⁡ ( Y ∈ S ⁡ ( X ) ) ≥ 1 − α {\mathbb{P}}(Y\in S(X))\geq 1-\alpha :

[297] table: 𝔼 [ | S ( X ) | ] ≥ 𝔼 [ rank ( c Y ⁡ ( X ) ; X ) ⋅ 𝟙 { Y ∈ S ( X ) } ] ≥ 𝔼 [ rank ( c Y ⁡ ( X ) ; X ) ] ⋅ ( 1 − α ) − 𝔼 [ rank ⋅ 𝟙 { Y ∉ S } ] . {\mathbb{E}}[|S(X)|]\geq{\mathbb{E}}[\mathrm{rank}(c^{Y(X)};X)\cdot{\mathds{1}}\{Y\in S(X)\}]\geq{\mathbb{E}}[\mathrm{rank}(c^{Y(X)};X)]\cdot(1-\alpha)-{\mathbb{E}}[\mathrm{rank}\cdot{\mathds{1}}\{Y\notin S\}].

[298] p: The second term is bounded and yields the O ⁡ ( 1 / n ) O(1/n) correction. ∎

[299] h6: Remark 7.6 (Finite candidate spaces and under-coverage) .

[300] p: Part 3 predicts M ⋆ = + ∞ M^{\star}=+\infty when β > α \beta>\alpha , but in practice M ⋆ M^{\star} is bounded by the number of distinct canonical classes | 𝒞 ⁡ ( x ) | |{\mathcal{C}}(x)| observed in K K samples. When | 𝒞 ⁡ ( x ) | |{\mathcal{C}}(x)| is small (e.g., | 𝒞 | = 4 |{\mathcal{C}}|=4 for MCQ tasks), the conformal quantile remains finite even though some items are unsolvable. Marginal coverage still falls below 1 − α 1{-}\alpha because, for items where p ⋆ ​ ( x ) = 0 p^{\star}(x)=0 , the correct class never enters the candidate pool—no prediction set over observed candidates can cover it. The under-coverage thus equals the unsolvable fraction β \beta , not a calibration error: conditional coverage on solvable items remains near-perfect (Table 2 ).

[301] h6: Remark 7.7 (Bias is visible, not hidden) .

[302] p: The fundamental distinction from LLM-as-judge evaluation is that bias in the agent is surfaced through larger prediction sets, not concealed in an opaque score. A practitioner who observes M ⋆ = 8 M^{\star}=8 knows immediately that the agent frequently fails to rank acceptable answers highly. An LLM-judge score of 0.75 0.75 carries no such interpretable diagnostic—the same score could arise from high-quality answers with a harsh judge, or poor-quality answers with a lenient judge.

[303] h3: 7.4. Formal comparison with alternative evaluation methods

[304] p: We now compare the conformal method’s coverage guarantee against two standard baselines—single-sample evaluation and LLM-as-judge—showing that conformal calibration achieves lower evaluation error once the calibration set is large enough to undercut the judge’s bias.

[305] h6: Theorem 7.8 (Advantage over single-sample evaluation) .

[306] p: For any agent and any target reliability level 1 − δ 1-\delta , define the evaluation reliability as the probability that the evaluation’s assessment is within ϵ \epsilon of the truth.

[307] p: For single-sample evaluation applied to a test set of N N queries:

[308] table: (7.5) ℙ ⁡ ( | p ^ single − p ¯ | > ϵ ) ≤ 2 ​ exp ⁡ ( − 2 ​ N ​ ϵ 2 ) (Hoeffding) , {\mathbb{P}}\!\left(\bigl|\hat{p}_{\mathrm{single}}-\bar{p}\bigr|>\epsilon\right)\leq 2\exp(-2N\epsilon^{2})\quad\text{(Hoeffding)},

[309] p: where p ^ single = N − 1 ∑ j 𝟙 { a j ∈ 𝒜 ⋆ ( x j ) } \hat{p}_{\mathrm{single}}=N^{-1}\sum_{j}{\mathds{1}}\{a_{j}\in{\mathcal{A}}^{\star}(x_{j})\} .

[310] p: For conformal set evaluation:

[311] table: (7.6) ℙ ⁡ ( | Cov ^ ​ ( α ) − ( 1 − α ) | > ϵ ) ≤ 2 ​ exp ⁡ ( − 2 ​ N ​ ϵ 2 ) + 1 n + 1 , {\mathbb{P}}\!\left(\bigl|\widehat{\mathrm{Cov}}(\alpha)-(1-\alpha)\bigr|>\epsilon\right)\leq 2\exp(-2N\epsilon^{2})+\frac{1}{n+1},

[312] p: where Cov ^ \widehat{\mathrm{Cov}} is the empirical coverage on the test set.

[313] p: Both converge at rate O ⁡ ( 1 / N ) O(1/\sqrt{N}) , but the conformal method provides:

[314] p: A per-query guarantee ( Y ⁡ ( x ) ∈ S ⁡ ( x ) Y(x)\in S(x) ), not just an aggregate estimate.

[315] p: An explicit reliability level 1 − α 1-\alpha chosen by the user, vs. an unknown p ¯ \bar{p} that must be estimated.

[316] p: A diagnostic set size per query, revealing per-query difficulty.

[317] h6: Proof.

[318] p: Equation ( 7.5 ) is Hoeffding’s inequality for i.i.d. Bernoulli random variables. For ( 7.6 ): by Theorem 6.7 , ℙ ⁡ ( Y j ∈ S ⁡ ( x j ) ) ∈ [ 1 − α , 1 − α + 1 / ( n + 1 ) ] {\mathbb{P}}(Y_{j}\in S(x_{j}))\in[1{-}\alpha,\;1{-}\alpha+1/(n{+}1)] marginally. The empirical coverage Cov ^ \widehat{\mathrm{Cov}} averages N N such indicators (approximately independent across test queries). Hoeffding’s inequality applied to these indicators, centered at ℙ ⁡ ( Y ∈ S ⁡ ( X ) ) {\mathbb{P}}(Y\in S(X)) , gives the exponential tail. The 1 / ( n + 1 ) 1/(n{+}1) term accounts for the gap between ℙ ⁡ ( Y ∈ S ⁡ ( X ) ) {\mathbb{P}}(Y\!\in\!S(X)) and 1 − α 1{-}\alpha . ∎

[319] h6: Theorem 7.9 (Advantage over LLM-as-judge) .

[320] p: Let the LLM judge have systematic bias b J = 𝔼 X , a ​ [ b J ​ ( X , a ) ] ≠ 0 b_{J}={\mathbb{E}}_{X,a}[b_{J}(X,a)]\neq 0 and judge variance σ J 2 = 𝔼 X , a ​ [ Var ⁡ ( J ⁡ ( X , a ) ∣ X , a ) ] \sigma_{J}^{2}={\mathbb{E}}_{X,a}[\Var(J(X,a)\mid X,\allowbreak a)] . Then for any sample size N N :

[321] p: LLM-as-judge evaluation error:

[322] table: (7.7) MSE ⁡ ( p ^ J ) = b J 2 + σ J 2 + p ¯ ​ ( 1 − p ¯ ) N + O ⁡ ( N − 2 ) . \MSE(\hat{p}_{J})=b_{J}^{2}+\frac{\sigma_{J}^{2}+\bar{p}(1-\bar{p})}{N}+O(N^{-2}).

[323] p: The bias term b J 2 b_{J}^{2} does not decay with N N .

[324] p: Conformal evaluation error (coverage gap):

[325] table: (7.8) | ℙ ⁡ ( Y ∈ S ⁡ ( X ) ) − ( 1 − α ) | ≤ 1 n + 1 . \bigl|{\mathbb{P}}(Y\in S(X))-(1-\alpha)\bigr|\leq\frac{1}{n+1}.

[326] p: The error is controlled solely by the calibration set size n n and is independent of the agent’s bias, the judge’s bias, or any systematic error .

[327] h6: Proof.

[328] p: For the judge: p ^ J = N − 1 ​ ∑ j J ⁡ ( x j , a j ) \hat{p}_{J}=N^{-1}\sum_{j}J(x_{j},a_{j}) . Then 𝔼 ⁡ [ p ^ J ] = p ¯ + b J {\mathbb{E}}[\hat{p}_{J}]=\bar{p}+b_{J} , so Bias ⁡ ( p ^ J ) = b J \Bias(\hat{p}_{J})=b_{J} . The variance is Var ⁡ ( p ^ J ) = N − 1 ​ Var ⁡ ( J ⁡ ( X , a ) ) \Var(\hat{p}_{J})=N^{-1}\Var(J(X,a)) , decomposed via the law of total variance into agent variance and judge variance. The MSE follows.

[329] p: For conformal: this is a restatement of Theorem 7.1 . ∎

[330] h6: Corollary 7.10 (When does conformal evaluation achieve lower error?) .

[331] p: Under the MSE comparison criterion (where coverage gap and judge bias are both expressed as deviations from the true acceptability rate), conformal set evaluation achieves lower coverage error than LLM-as-judge whenever

[332] table: (7.9) | b J | > 1 n + 1 . |b_{J}|>\frac{1}{n+1}.

[333] p: For reference, if the judge’s bias reaches | b J | ≥ 0.05 |b_{J}|\geq 0.05 —a level documented in the literature [ Zheng2023Judge ] for subjective evaluation tasks—then n ≥ 19 n\geq 19 suffices. On structured tasks with unambiguous answers (e.g., GSM8K, MMLU), judge accuracy can exceed conformal coverage (Table 2 ), implying smaller effective bias and a correspondingly larger crossover point. The comparison is most informative on ambiguous tasks where judge bias is hardest to bound. Note that this comparison is meaningful when both methods are assessed by their distance to the true acceptability rate; conformal sets and judge scores are complementary evaluation outputs (Remark 7.11 ).

[334] h6: Remark 7.11 (Complementary, not universally dominant) .

[335] p: The “advantage” in Corollary 7.10 compares coverage gap (our method) against MSE (point estimators). These metrics answer different questions: coverage gap measures whether the evaluation’s reliability claim is valid, while MSE measures how accurately the evaluation estimates the agent’s true accuracy p ¯ \bar{p} . For reliability certification —“can I trust this agent at level 1 − α 1-\alpha ?”—conformal calibration is strictly superior once n ≥ ⌈ 1 / | b J | ⌉ − 1 n\geq\lceil 1/|b_{J}|\rceil-1 (e.g., n ≥ 19 n\geq 19 when | b J | = 0.05 |b_{J}|=0.05 ). For accuracy estimation —“what fraction of queries does the agent answer correctly?”—simple point estimators with confidence intervals remain useful. The methods are complementary: practitioners should use conformal sets for per-query reliability assessment and point estimates for aggregate performance reporting.

[336] h3: 7.5. Variance of set-size as a quality estimator

[337] p: Since set size serves as a quality diagnostic, we need it to be a stable estimator—the average set size should concentrate around its true mean as the test set grows.

[338] h6: Proposition 7.12 (Concentration of the set-size estimator) .

[339] p: Let M ¯ := N − 1 ​ ∑ j = 1 N | S ⁡ ( x j ) | \bar{M}:=N^{-1}\sum_{j=1}^{N}|S(x_{j})| be the average set size on a test set of N N queries. If | S ⁡ ( x ) | ≤ B |S(x)|\leq B almost surely (bounded set size), then

[340] table: (7.10) ℙ ⁡ ( | M ¯ − 𝔼 ⁡ [ | S ⁡ ( X ) | ] | > t ) ≤ 2 ​ exp ⁡ ( − 2 ​ N ​ t 2 B 2 ) . {\mathbb{P}}\!\left(\bigl|\bar{M}-{\mathbb{E}}[|S(X)|]\bigr|>t\right)\leq 2\exp\!\left(-\frac{2Nt^{2}}{B^{2}}\right).

[341] p: The average set size concentrates around its expectation at rate O ⁡ ( B / N ) O(B/\sqrt{N}) and provides a reliable, low-variance estimator of agent quality.

[342] h6: Proof.

[343] p: Each | S ⁡ ( x j ) | ∈ [ 1 , B ] |S(x_{j})|\in[1,B] is bounded. Apply Hoeffding’s inequality. ∎

[344] p: These variance bounds on set size motivate the next question: how does the coverage–efficiency trade-off depend on agent competence?

[345] h2: 8. Coverage–Efficiency Trade-Off

[346] p: A better agent produces smaller prediction sets—but how much smaller? This section quantifies the relationship between agent quality and set size, showing that the prediction set is an efficient diagnostic: strong agents need only singleton sets, while weak agents unavoidably require larger ones.

[347] h3: 8.1. Set size as a function of agent competence

[348] h6: Proposition 8.1 (Expected rank under single-acceptable-class) .

[349] p: Suppose there is a unique acceptable canonical class c ⋆ c^{\star} with p = P θ ​ ( c i = c ⋆ ) > 1 / 2 p=P_{\theta}(c_{i}=c^{\star})>1/2 . Then:

[350] table: (8.1) 𝔼 ⁡ [ rank ⁡ ( c ⋆ , x ) ] ≤ 1 + 1 − p p ⋅ K − 1 K → K → ∞ 1 + 1 − p p = 1 p . {\mathbb{E}}[\mathrm{rank}(c^{\star};x)]\leq 1+\frac{1-p}{p}\cdot\frac{K-1}{K}\xrightarrow{K\to\infty}1+\frac{1-p}{p}=\frac{1}{p}.

[351] p: If p > 1 / 2 p>1/2 , then 𝔼 ⁡ [ rank ⁡ ( c ⋆ , x ) ] < 2 {\mathbb{E}}[\mathrm{rank}(c^{\star};x)]<2 for all K K .

[352] h6: Proof.

[353] p: rank ⁡ ( c ⋆ ) = 1 + | { c ′ ≠ c ⋆ : n ⁡ ( c ′ ) ≥ n ⁡ ( c ⋆ ) } | \mathrm{rank}(c^{\star})=1+|\{c^{\prime}\neq c^{\star}:n(c^{\prime})\geq n(c^{\star})\}| . For any competing class c ′ c^{\prime} with probability p c ′ < p p_{c^{\prime}}<p :

[354] table: ℙ ⁡ ( n ⁡ ( c ′ ) ≥ n ⁡ ( c ⋆ ) ) ≤ ℙ ⁡ ( n ⁡ ( c ′ ) ≥ K ​ p / 2 ) + ℙ ⁡ ( n ⁡ ( c ⋆ ) ≤ K ​ p / 2 ) . {\mathbb{P}}(n(c^{\prime})\geq n(c^{\star}))\leq{\mathbb{P}}(n(c^{\prime})\geq Kp/2)+{\mathbb{P}}(n(c^{\star})\leq Kp/2).

[355] p: Summing over all competing classes (total mass 1 − p 1-p ) and applying a stochastic dominance argument: 𝔼 ⁡ [ rank ⁡ ( c ⋆ ) ] ≤ 1 + ( 1 − p ) / p ⋅ ( K − 1 ) / K {\mathbb{E}}[\mathrm{rank}(c^{\star})]\leq 1+(1-p)/p\cdot(K-1)/K . ∎

[356] h3: 8.2. Set size inflation under ambiguity

[357] h6: Proposition 8.2 (Ambiguity inflates calibration scores) .

[358] p: If a fraction β \beta of calibration queries have p ⋆ ​ ( x i ) < 1 / K p^{\star}(x_{i})<1/K and β > α \beta>\alpha , then M ⋆ = + ∞ M^{\star}=+\infty .

[359] h6: Proof.

[360] p: At least β ​ n \beta n scores are + ∞ +\infty with high probability. The k k -th order statistic with k = ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ k=\lceil(n+1)(1-\alpha)\rceil is infinite when k > n − β ​ n k>n-\beta n , which holds when β > α + 1 / ( n + 1 ) \beta>\alpha+1/(n+1) . ∎

[361] h6: Remark 8.3 .

[362] p: This is a feature, not a bug: M ⋆ = + ∞ M^{\star}=+\infty tells the practitioner that the agent cannot reliably serve this query population at the desired confidence level. No other evaluation method provides such a clear signal.

[363] h2: 9. Sequential Sampling with Certified Early Stopping

[364] p: Drawing K K samples per query can be expensive. We develop sequential procedures that stop early when consensus is clear, reducing cost without sacrificing coverage.

[365] h3: 9.1. The sequential consensus problem

[366] p: After k k samples, let p ^ 1 ( k ) \hat{p}_{1}^{(k)} and p ^ 2 ( k ) \hat{p}_{2}^{(k)} be the frequencies of the top two candidates, with margin Δ k := p ^ 1 ( k ) − p ^ 2 ( k ) \Delta_{k}:=\hat{p}_{1}^{(k)}-\hat{p}_{2}^{(k)} .

[367] h3: 9.2. Hoeffding-based stopping criterion

[368] h6: Theorem 9.1 (Certified mode identification) .

[369] p: Define the stopping time

[370] table: (9.1) τ δ := min ⁡ { k ≥ k 0 : Δ k > 2 ​ ln ⁡ ( 2 ​ | 𝒞 ⁡ ( x ) | ​ k 2 / δ ) k } . \tau_{\delta}:=\min\left\{k\geq k_{0}:\Delta_{k}>\sqrt{\frac{2\ln(2|{\mathcal{C}}(x)|k^{2}/\delta)}{k}}\right\}.

[371] p: If the true mode c ⋆ c^{\star} has p 1 > p 2 := max c ≠ c ⋆ ⁡ P θ ​ ( c ∣ x ) p_{1}>p_{2}:=\max_{c\neq c^{\star}}P_{\theta}(c\mid x) , then ℙ ⁡ ( c ( 1 ) ( τ δ ) = c ⋆ ) ≥ 1 − δ {\mathbb{P}}(c_{(1)}^{(\tau_{\delta})}=c^{\star})\geq 1-\delta .

[372] h6: Proof.

[373] p: At step k k , by Hoeffding and a union bound over | 𝒞 ⁡ ( x ) | |{\mathcal{C}}(x)| classes:

[374] table: ℙ ( ∃ c : | P ^ k ( c ∣ x ) − P θ ( c ∣ x ) | > ϵ ) ≤ 2 | 𝒞 ( x ) | exp ( − 2 k ϵ 2 ) . {\mathbb{P}}\bigl(\exists c:|\hat{P}_{k}(c\mid x)-P_{\theta}(c\mid x)|>\epsilon\bigr)\leq 2|{\mathcal{C}}(x)|\exp(-2k\epsilon^{2}).

[375] p: Setting ϵ = Δ k / 2 \epsilon=\Delta_{k}/2 and requiring the bound to be ≤ δ / k 2 \leq\delta/k^{2} (enabling a sum over k k via ∑ 1 / k 2 < 2 \sum 1/k^{2}<2 ) yields ( 9.1 ). When triggered, the true frequencies are within Δ k / 2 \Delta_{k}/2 of empirical values with probability ≥ 1 − δ \geq 1-\delta , so the empirical mode equals the true mode. ∎

[376] h3: 9.3. Variance reduction from sequential stopping

[377] h6: Proposition 9.2 (Variance–cost trade-off of sequential stopping) .

[378] p: Let K max K_{\max} be the maximum sample budget and τ \tau the stopping time from ( 9.1 ). Then:

[379] p: Easy queries (large true margin p 1 − p 2 = Δ > 0 p_{1}-p_{2}=\Delta>0 ): 𝔼 ⁡ [ τ ] = O ⁡ ( Δ − 2 ​ ln ⁡ ( | 𝒞 | / δ ) ) {\mathbb{E}}[\tau]=O(\Delta^{-2}\ln(|{\mathcal{C}}|/\delta)) , matching the classical sample complexity of fixed-confidence best-arm identification [ EvenDar2006BestArm ] .

[380] p: Hard queries (small Δ \Delta ): 𝔼 ⁡ [ τ ] ≈ K max {\mathbb{E}}[\tau]\approx K_{\max} (no savings).

[381] p: The cost reduction is concentrated on queries where variance is already low (high consensus), preserving the framework’s reliability exactly where it is most needed.

[382] h3: 9.4. Validity of conformal guarantee under adaptive stopping

[383] h6: Proposition 9.3 (Conformal validity with adaptive K K ) .

[384] p: If the stopping rule K i = K i ​ ( x i , a 1 ( i ) , … ) K_{i}=K_{i}(x_{i},\allowbreak a_{1}^{(i)},\allowbreak\dots) depends only on x i x_{i} and agent samples (not on y i y_{i} ), then s 1 , … , s n + 1 s_{1},\dots,s_{n+1} remain exchangeable and Theorem 6.7 holds.

[385] h6: Proof.

[386] p: The score s i s_{i} is a function of ( x i , y i ) (x_{i},y_{i}) and the agent samples { a j ( i ) } j = 1 K i \{a_{j}^{(i)}\}_{j=1}^{K_{i}} . Since K i K_{i} depends only on ( x i , { a j ( i ) } ) (x_{i},\allowbreak\{a_{j}^{(i)}\}) and not on y i y_{i} , and ( x i , y i ) (x_{i},y_{i}) are exchangeable, the scores inherit exchangeability. ∎

[387] p: Note that the stopping rule (Theorem 9.1 ) certifies mode identity, not the full rank ordering. For items where s i = 1 s_{i}=1 (the correct answer is the mode), mode stability implies rank stability. For items with s i > 1 s_{i}>1 , rank fluctuations after stopping may affect prediction set size but not coverage validity, since Proposition 9.3 guarantees exchangeability regardless of when sampling stops.

[388] h2: 10. Extensions

[389] h3: 10.1. Multiple acceptable canonical classes

[390] p: When | Canon ⁡ ( x , 𝒜 ⋆ ​ ( x ) ) | > 1 |\mathrm{Canon}(x,{\mathcal{A}}^{\star}(x))|>1 , use:

[391] table: (10.1) s i = min l = 1 , … , L i ⁡ rank ⁡ ( Canon ⁡ ( x i , y i ( l ) ) , x i ) . s_{i}=\min_{l=1,\dots,L_{i}}\mathrm{rank}\bigl(\mathrm{Canon}(x_{i},y_{i}^{(l)});\;x_{i}\bigr).

[392] p: Coverage is preserved since exchangeability is maintained.

[393] h3: 10.2. Dependence-aware extensions

[394] h6: Remark 10.1 (Separation of concerns) .

[395] p: A key structural insight: the conformal coverage guarantee depends on exchangeability of calibration-test pairs ( x i , y i ) (x_{i},y_{i}) , not on independence of the K K within-query samples. Dependence among the K K samples affects ranking quality (and hence set size ) but not coverage validity . If dependence degrades the ranking, M ⋆ M^{\star} grows—the framework self-corrects by widening the set—without breaking the guarantee. This separation is what makes the method robust to the poorly characterized dependence structure of LLM API calls.

[396] h3: 10.3. Weighted conformal prediction

[397] p: Under covariate shift between calibration and test distributions, use likelihood-ratio-weighted conformal prediction [ TibshiraniBarber2019 ] :

[398] table: (10.2) M w ⋆ := weighted quantile of ​ s 1 , … , s n ​ with weights ​ w i ∝ p test ​ ( x i ) p cal ​ ( x i ) . M^{\star}_{w}:=\text{weighted quantile of }s_{1},\dots,s_{n}\text{ with weights }w_{i}\propto\frac{p_{\mathrm{test}}(x_{i})}{p_{\mathrm{cal}}(x_{i})}.

[399] h2: 11. Empirical Study

[400] p: We first validated all theoretical results on controlled synthetic agents with known parameters (Appendix C ); all predictions—coverage calibration, exponential variance decay, set-size monotonicity, and canonicalization amplification—are confirmed.

[401] p: We then evaluate on five real benchmarks spanning code generation, mathematical reasoning, open-ended question answering, and multiple-choice selection, using five models from three families (GPT-4.1 ladder, Llama 4 Maverick, Mistral Small 24B). Four questions structure the evaluation:

[402] p: Does conformal calibration achieve coverage ≥ 1 − α \geq 1-\alpha empirically (Theorem 6.7 )?

[403] p: Does self-consistency reduce variance as K K increases (Theorem 4.4 )?

[404] p: Does set size adapt to model uncertainty (Theorem 7.5 )?

[405] p: Does the framework achieve lower coverage error than single-sample and LLM-judge baselines (Theorems 7.8 , 7.9 )?

[406] h5: Hypotheses.

[407] p: We formalize six empirical hypotheses, each derived from a specific theoretical result:

[408] p: Coverage validity. Empirical coverage meets the 1 − α 1{-}\alpha target on tasks where the model has sufficient capability; any shortfall is attributable to model capability gaps, not calibration failure (Theorem 6.7 ).

[409] p: Variance reduction. Mode identification error decreases with K K , with the largest reductions on high-accuracy tasks where p ⋆ p^{\star} is far from 0.5 0.5 (Theorem 4.4 ).

[410] p: Adaptive set size. Prediction set size correlates positively with per-item answer entropy (Theorem 7.5 ).

[411] p: Canonicalization benefit. Canonicalization reduces prediction set size on tasks with surface-form variation (Proposition 4.6 ).

[412] p: Baseline comparison. Conformal coverage meets or exceeds LLM-judge accuracy on ambiguous tasks where judge bias is non-negligible (Corollary 7.10 ).

[413] p: Sequential efficiency. The Hoeffding-based stopping rule reduces the average number of samples with no loss in coverage (Theorem 9.1 ).

[414] h3: 11.1. Experimental setup

[415] h5: Datasets.

[416] p: We select five benchmarks representing distinct task families and canonicalization strategies:

[417] p: HumanEval (code generation, 164 items). Each response is executed in a sandboxed environment against unit tests; canonicalization is deterministic binary: pass or fail . This represents the lowest-ambiguity setting where correctness is objectively verifiable.

[418] p: TruthfulQA (open-ended QA, 817 items). Free-form text responses where surface-form variation is extreme—even correct answers differ substantially in phrasing. Canonicalization uses an LLM judge (GPT-4.1 at temperature 0 0 ) to classify each sample as correct or incorrect , yielding a binary answer space analogous to code execution.

[419] p: BigBench MovieRec (multiple-choice, 500 items; hereafter “BigBench”). Responses are canonicalized via option matching and text normalization to the selected movie title.

[420] p: GSM8K (mathematical reasoning, 1319 items) [ Cobbe2021GSM8K ] . Grade-school math word problems requiring multi-step arithmetic. Canonicalization is deterministic numeric extraction: we parse the final answer after the #### delimiter and normalize to a standard integer form. This tests the framework on a task with a unique correct answer but diverse reasoning paths.

[421] p: MMLU (multiple-choice knowledge, 1000 items sampled from the full test set). Four-option questions spanning 57 academic subjects. Canonicalization reuses the MCQ pipeline (option matching and text normalization).

[422] h5: Agent and sampling configuration.

[423] p: We use the GPT-4.1 model family as a capability ladder with unambiguous ordering—GPT-4.1 (strong), GPT-4.1-mini (mid-tier), GPT-4.1-nano (weak)—providing a clean test of the set-size monotonicity prediction. All models are evaluated at temperature T = 0.7 T=0.7 with K max = 20 K_{\max}=20 independent samples per item ( K fixed = 10 K_{\mathrm{fixed}}=10 for both calibration and test-time prediction in primary results):

[424] p: GPT-4.1 (strong): evaluated on all five benchmarks. Expected to yield the smallest prediction sets.

[425] p: GPT-4.1-mini (mid-tier): evaluated on GSM8K and MMLU, the two benchmarks with largest calibration sets ( n cal = 500 n_{\mathrm{cal}}=500 ).

[426] p: GPT-4.1-nano (weak): evaluated on GSM8K and MMLU. Expected to yield the largest prediction sets.

[427] p: As a supplementary comparison, we evaluate GPT-5 mini on all five benchmarks. Under our T = 0.7 T{=}0.7 i.i.d. sampling protocol (without extended thinking), GPT-5 mini exhibits lower per-sample accuracy than GPT-4.1. Throughout, M ⋆ M^{\star} and the reliability level are properties of a specific (model, inference configuration) pair—not of the model architecture alone. The same model can yield different prediction sets depending on temperature, decoding strategy, and whether capabilities like extended thinking are activated.

[428] p: To test cross-family generalizability, we evaluate two open-weight models via Together AI on GSM8K, MMLU, and TruthfulQA:

[429] p: Llama 4 Maverick 17B ( meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 ): a mid-tier mixture-of-experts model from Meta.

[430] p: Mistral Small 24B ( mistralai/Mistral-Small-24B-Instruct-2501 ): a smaller instruction-tuned model from Mistral AI.

[431] p: The calibration/test split uses up to n cal = n test = 500 n_{\mathrm{cal}}=n_{\mathrm{test}}=500 items per dataset (or half the dataset if smaller, e.g., HumanEval uses 82/82). The LLM judge is fixed at GPT-4.1 (temperature 0 0 ) across all experiments to avoid confounding evaluation quality with agent capability. All API responses are SHA-256 cached so that re-runs are deterministic and cost-free.

[432] h5: Evaluation protocol.

[433] p: All experiments use the rank-based nonconformity score (Definition 6.2 ): for each calibration item, the score is the rank of the first acceptable answer in the self-consistency ordering. The adaptive score variant (Section 6.5 ) is deferred to future work.

[434] p: For each dataset and model we: (1) compute nonconformity scores { s i } i = 1 n cal \{s_{i}\}_{i=1}^{n_{\mathrm{cal}}} on the calibration set and determine M ⋆ M^{\star} for α ∈ { 0.01 , 0.05 , 0.10 , 0.15 , 0.20 , 0.25 , 0.30 } \alpha\in\{0.01,0.05,0.10,0.15,0.20,0.25,0.30\} ; (2) evaluate coverage, mode accuracy, single-sample accuracy, LLM-judge accuracy, and prediction set size on the test set; (3) sweep K ∈ { 1 , 2 , 5 , 10 , 20 } K\in\{1,2,5,10,20\} for variance reduction; (4) run the Hoeffding-based sequential stopping rule ( δ = 0.05 \delta=0.05 ). All reported proportions include 95% Wilson confidence intervals [ Wilson1927 ] ; continuous metrics (set size, entropy, average K K ) include 95% bootstrap percentile confidence intervals ( B = 10,000 B=10{,}000 resamples).

[435] h5: Baselines.

[436] p: We compare four evaluation strategies:

[437] p: Single-sample: one draw from the agent, binary correctness.

[438] p: Self-consistency mode ( K = 10 K=10 ): majority-vote answer, binary correctness.

[439] p: LLM-as-judge: GPT-4.1 scores the first sample; score ≥ 0.5 \geq 0.5 counts as correct.

[440] p: Conformal prediction set : our method with calibrated threshold M ⋆ M^{\star} .

[441] h3: 11.2. Main results

[442] p: Table 2 reports the primary metrics across all five benchmarks.

[443] figure: Table 2. Main results ( T = 0.7 T{=}0.7 , K = 10 K{=}10 , α = 0.10 \alpha=0.10 ). Coverage target is 1 − α = 0.90 1-\alpha=0.90 . 95% Wilson CIs in parentheses. Results shown for GPT-4.1; see Table 3 for cross-model comparison. Dataset n cal n_{\mathrm{cal}} / n test n_{\mathrm{test}} M ⋆ M^{\star} Coverage Mode Acc Judge Acc Avg. | S | |S| Cov | | solv HumanEval 82 / 82 2 0.707 ( 0.60–0.79 ) 0.646 ( 0.54–0.74 ) 0.915 † 1.32 0.967 TruthfulQA 408 / 409 1 0.976 ( 0.96–0.99 ) 0.976 ( 0.96–0.99 ) 0.966 ( 0.94–0.98 ) 1.00 0.980 BigBench 125 / 125 2 0.792 ( 0.71–0.85 ) 0.768 ( 0.69–0.83 ) 0.736 ( 0.65–0.81 ) 1.10 1.000 GSM8K 500 / 500 1 0.956 ( 0.93–0.97 ) 0.956 ( 0.93–0.97 ) 0.986 ( 0.97–0.99 ) 1.00 0.980 MMLU 500 / 500 2 0.838 ( 0.80–0.87 ) 0.798 ( 0.76–0.83 ) 0.962 ( 0.94–0.98 ) 1.11 0.988 † The LLM judge cannot execute code; it evaluates syntactic plausibility rather than functional correctness, making the judge–conformal comparison structurally invalid on HumanEval (the methods measure different things). HumanEval is excluded from all judge comparisons in the text. “Cov | | solv” = conditional coverage among items where the model produced at least one correct answer across all K max K_{\max} samples—a post-hoc diagnostic that validates the theory but is not available at deployment time (see Section 11.9 ). Capability gaps: HumanEval 26.8%, BigBench 20.8%, MMLU 15.2%, GSM8K 2.4%, TruthfulQA 0.5%.

[444] figure: Table 3. Multi-model comparison at α = 0.10 \alpha=0.10 : M ⋆ M^{\star} and average set size. Top: GPT-4.1 capability ladder on GSM8K and MMLU. Bottom: Open-weight cross-family validation on GSM8K, MMLU, and TruthfulQA. M ⋆ M^{\star} and | S | ¯ \bar{|S|} are non-decreasing with decreasing capability across all model families. GPT-4.1 GPT-4.1-mini GPT-4.1-nano Dataset M ⋆ M^{\star} | S | ¯ \bar{|S|} M ⋆ M^{\star} | S | ¯ \bar{|S|} M ⋆ M^{\star} | S | ¯ \bar{|S|} GSM8K 1 1.00 1 1.00 2 1.35 MMLU 2 1.11 2 1.12 2 1.17 GPT-4.1 Llama 4 Maverick Mistral Small Dataset M ⋆ M^{\star} | S | ¯ \bar{|S|} M ⋆ M^{\star} | S | ¯ \bar{|S|} M ⋆ M^{\star} | S | ¯ \bar{|S|} GSM8K 1 1.00 1 1.00 1 1.00 MMLU 2 1.11 2 1.12 2 1.32 TruthfulQA 1 1.00 2 1.25 2 1.31 GPT-4.1 ladder. On both benchmarks, | S | ¯ \bar{|S|} increases monotonically across the capability ladder; M ⋆ M^{\star} increases on GSM8K ( 1 → 1 → 2 1\to 1\to 2 ) and remains constant at 2 2 on MMLU. On MMLU, the capability gap is 15.2 % 15.2\% (GPT-4.1), 14.6 % 14.6\% (GPT-4.1-mini), and 26.2 % 26.2\% (GPT-4.1-nano), with conditional coverage remaining high: 0.988 0.988 , 0.979 0.979 , and 0.965 0.965 respectively. On GSM8K, all three models achieve coverage ≥ 0.948 \geq 0.948 with conditional coverage ≥ 0.973 \geq 0.973 . Open-weight models. Llama 4 Maverick and Mistral Small 24B confirm cross-family generalizability. On GSM8K, all three families achieve M ⋆ = 1 M^{\star}{=}1 with coverage ≥ 0.956 \geq 0.956 . On TruthfulQA, open-weight models require M ⋆ = 2 M^{\star}{=}2 (vs. 1 1 for GPT-4.1), with coverage ≥ 0.960 \geq 0.960 and conditional coverage ≥ 0.992 \geq 0.992 . On MMLU, the capability gap— 25.4 % 25.4\% (Maverick) and 13.0 % 13.0\% (Mistral)—drives marginal coverage below 90 % 90\% , but conditional coverage remains high ( 0.995 0.995 and 0.949 0.949 ). Supplementary: GPT-5 mini. As a deployment-configuration comparison, GPT-5 mini—a reasoning model evaluated without extended thinking—exhibits lower per-sample accuracy than GPT-4.1 on all five benchmarks: HumanEval ( M ⋆ M^{\star} : 2 → 4 2\to 4 , | S | ¯ \bar{|S|} : 1.32 → 2.43 1.32\to 2.43 ), BigBench ( 2 → 3 2\to 3 , 1.10 → 1.83 1.10\to 1.83 ), MMLU ( 2 → 3 2\to 3 , 1.11 → 1.59 1.11\to 1.59 ), GSM8K ( 1 → 2 1\to 2 , 1.00 → 1.42 1.00\to 1.42 ), TruthfulQA ( 1 → 2 1\to 2 , 1.00 → 1.49 1.00\to 1.49 ). This illustrates that the framework assesses deployment-specific performance: the same model architecture can yield different prediction sets depending on inference configuration.

[445] h5: Coverage validity (Q1).

[446] p: Table 2 reports coverage across all five benchmarks for GPT-4.1. Two benchmarks (GSM8K and TruthfulQA) exceed the 90 % 90\% target with M ⋆ = 1 M^{\star}=1 ; three fall below: MMLU ( 0.838 0.838 ), BigBench ( 0.792 0.792 ), and HumanEval ( 0.707 0.707 ). On these three benchmarks, the method provides no marginal coverage guarantee at α = 0.10 \alpha=0.10 —this is a direct consequence of Theorem 7.5 (3): when the fraction of unsolvable items exceeds α \alpha , no evaluation method can achieve the target. Conditional coverage among solvable items exceeds 0.96 0.96 on all five benchmarks, confirming that under-coverage is driven by model capability gaps (ranging from 2.4 % 2.4\% on GSM8K to 26.8 % 26.8\% on HumanEval; see Table 2 footnote) rather than calibration failure.

[447] p: With n cal ≥ 82 n_{\mathrm{cal}}\geq 82 (the smallest dataset, HumanEval), the theoretical over-coverage bound is 1 / ( n + 1 ) ≤ 0.012 1/(n+1)\leq 0.012 , ensuring tight calibration. For the larger datasets ( n cal = 500 n_{\mathrm{cal}}=500 ), the bound tightens to 0.002 0.002 .

[448] h5: Comparison with baselines (Q4).

[449] p: On non-code tasks, conformal coverage exceeds judge accuracy where the judge faces ambiguity: BigBench ( 0.792 0.792 vs. 0.736 0.736 ) and TruthfulQA ( 0.976 0.976 vs. 0.966 0.966 ). On MMLU and GSM8K, the judge outperforms because these tasks have unambiguous correct answers ( 0.962 0.962 and 0.986 0.986 respectively).

[450] h5: Set-size monotonicity across capability levels.

[451] p: The GPT-4.1 capability ladder (Table 3 ) directly confirms Theorem 7.5 : | S | ¯ \bar{|S|} increases monotonically across GPT-4.1 → \to GPT-4.1-mini → \to GPT-4.1-nano on both benchmarks. On GSM8K, GPT-4.1-nano’s M ⋆ M^{\star} rises to 2 2 (vs. 1 1 for the other two); on MMLU, all three share M ⋆ = 2 M^{\star}{=}2 but | S | ¯ \bar{|S|} increases from 1.11 → 1.12 → 1.17 1.11\to 1.12\to 1.17 . Conditional coverage remains high across all three ( ≥ 0.965 \geq 0.965 ). The open-weight models reinforce this pattern: on GSM8K, all three families achieve M ⋆ = 1 M^{\star}{=}1 ; on TruthfulQA, both open-weight models require M ⋆ = 2 M^{\star}{=}2 (vs. 1 1 for GPT-4.1) with coverage ≥ 0.960 \geq 0.960 . As a supplementary comparison, GPT-5 mini—evaluated without extended thinking—exhibits higher M ⋆ M^{\star} and | S | ¯ \bar{|S|} than GPT-4.1 on all benchmarks (Table 3 footnote), illustrating that the framework assesses deployment-specific performance.

[452] h5: Multi-sample judge comparison.

[453] p: Our primary LLM-judge baseline uses a single call per test item ( K judge = 1 K_{\mathrm{judge}}=1 ), matching the standard setup in most benchmark implementations [ Zheng2023Judge ] . To test whether aggregating multiple judge calls closes the gap, we evaluate a majority-vote judge with K judge ∈ { 1 , 3 , 5 , 10 } K_{\mathrm{judge}}\in\{1,3,5,10\} on the two benchmarks where conformal coverage exceeds the single-call judge. On TruthfulQA, the majority-vote judge improves from 0.966 0.966 ( K = 1 K{=}1 ) to 0.976 0.976 ( K = 10 K{=}10 ), converging to the conformal coverage level—but only at 10 × 10\times cost. On BigBench, the multi-sample judge shows no improvement ( 0.736 0.736 at K = 1 K{=}1 to 0.728 0.728 at K = 10 K{=}10 ), while conformal coverage achieves 0.792 0.792 —a 6 6 percentage point advantage that persists regardless of judge budget. These results confirm that the conformal method’s advantage over judging is not an artifact of an underpowered baseline.

[454] h5: Cost-matched comparison.

[455] p: To ensure a fair comparison, we match the total API cost between conformal evaluation and the majority-vote judge (per-call costs in Table 7 footnote). For MCQ tasks, the cost-matched judge budget is ∼ 14 {\sim}14 calls; for TruthfulQA (which adds judge-based canonicalization), ∼ 24 {\sim}24 calls. We extend the majority-vote judge to K judge ∈ { 15 , 20 } K_{\mathrm{judge}}\in\{15,20\} to evaluate at these budgets. On BigBench , the judge saturates early: accuracy is 0.728 0.728 at both K = 15 K{=}15 and K = 20 K{=}20 , while conformal coverage reaches 0.792 0.792 —a 6.4 6.4 percentage point gap, though 95% CIs overlap at this sample size ( n test = 125 n_{\mathrm{test}}{=}125 ). The bottleneck is the judge’s per-call accuracy, not sampling noise: additional judge calls cannot improve a systematically incorrect judgment. On TruthfulQA , the cost-matched judge ( K = 20 K{=}20 , accuracy 0.973 0.973 ) essentially matches conformal coverage ( 0.976 0.976 ), confirming convergence when the judge is accurate. However, on non-text tasks (MCQ, math, code), conformal evaluation requires no judge model at all—eliminating a potential source of evaluation bias while achieving comparable or superior coverage.

[456] p: Figure 2 shows the coverage validation plots across all alpha values.

[457] figure: Figure 2. Coverage validation: empirical coverage vs. target 1 − α 1-\alpha for α ∈ { 0.01 , … , 0.30 } \alpha\in\{0.01,\ldots,0.30\} across all five benchmarks. Points above the diagonal are consistent with the marginal coverage guarantee (Theorem 6.7 ). Points below the diagonal (HumanEval, BigBench, MMLU) arise when the unsolvable fraction β \beta exceeds α \alpha : Theorem 7.5 (3) predicts M ⋆ = + ∞ M^{\star}=+\infty in this regime, meaning no finite prediction set can cover unsolvable items. Empirically, M ⋆ M^{\star} remains finite (capped by | 𝒞 | |\mathcal{C}| ) but the resulting sets still cannot include an acceptable answer for queries that the model fundamentally cannot solve. The under-coverage is thus a diagnosed capability gap, not a calibration failure—conditional coverage on solvable items exceeds 0.96 0.96 across all five benchmarks.

[458] h5: Split stability (bootstrap analysis).

[459] p: To assess whether M ⋆ M^{\star} is an artifact of the particular calibration/test split, we re-split the data with 100 independent random seeds and recompute M ⋆ M^{\star} and empirical coverage for each split. Table 4 summarizes the results. For five of six model–dataset combinations, M ⋆ M^{\star} is identical across all 100 splits (std = 0 =0 ). Only GPT-4.1-nano on GSM8K shows variation ( M ⋆ = 1 M^{\star}=1 in 82% of splits, M ⋆ = 2 M^{\star}=2 in 18%; coverage std = 0.023 =0.023 , the highest in the table). This instability is informative: GPT-4.1-nano sits at the exact capability boundary where the fraction of unsolvable GSM8K items is close to α = 0.10 \alpha=0.10 , so the ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ \lceil(n{+}1)(1{-}\alpha)\rceil -th order statistic fluctuates between score values of 1 1 and 2 2 depending on which items fall in the calibration set. This is precisely the regime where the reliability level (Definition 2.4 : 89.8 % 89.8\% for GPT-4.1-nano on GSM8K) provides a more stable signal than the discrete M ⋆ M^{\star} , since the reliability level depends on the count of s i ≤ 1 s_{i}\leq 1 scores rather than on a single order statistic. Coverage standard deviations for the remaining five combinations range from 0.004 0.004 to 0.007 0.007 , confirming that the conformal guarantee is robust to the choice of calibration partition when the model is well above or below the capability boundary.

[460] figure: Table 4. Bootstrap split stability: M ⋆ M^{\star} and coverage across 100 random cal/test partitions ( n cal = n test = 500 n_{\mathrm{cal}}=n_{\mathrm{test}}=500 , α = 0.10 \alpha=0.10 ). Model Dataset M ⋆ M^{\star} (mean ± \pm std) Coverage (mean ± \pm std) GPT-4.1 GSM8K 1.00 ± 0.00 1.00\pm 0.00 0.951 ± 0.007 0.951\pm 0.007 GPT-4.1 MMLU 2.00 ± 0.00 2.00\pm 0.00 0.979 ± 0.005 0.979\pm 0.005 GPT-4.1-mini GSM8K 1.00 ± 0.00 1.00\pm 0.00 0.957 ± 0.007 0.957\pm 0.007 GPT-4.1-mini MMLU 2.00 ± 0.00 2.00\pm 0.00 0.976 ± 0.004 0.976\pm 0.004 GPT-4.1-nano GSM8K 1.18 ± 0.38 1.18\pm 0.38 0.917 ± 0.023 0.917\pm 0.023 GPT-4.1-nano MMLU 2.00 ± 0.00 2.00\pm 0.00 0.945 ± 0.007 0.945\pm 0.007

[461] h3: 11.3. Variance reduction

[462] p: Table 5 reports mode error as a function of the number of self-consistency samples K K .

[463] figure: Table 5. Mode error ModeErr ^ ​ ( K ) \widehat{\mathrm{ModeErr}}(K) as a function of K K for GPT-4.1. Lower is better. 95% Wilson CIs in parentheses. Results for GSM8K and MMLU add tasks with deterministic canonicalization (numeric extraction and MCQ matching, respectively). Dataset K = 1 K=1 K = 2 K=2 K = 5 K=5 K = 10 K=10 K = 20 K=20 HumanEval .354 ( .26–.46 ) .378 ( .28–.49 ) .366 ( .27–.47 ) .341 ( .25–.45 ) .341 ( .25–.45 ) TruthfulQA .034 ( .02–.06 ) .044 ( .03–.07 ) .027 ( .02–.05 ) .024 ( .01–.04 ) .022 ( .01–.04 ) BigBench .248 ( .18–.33 ) .240 ( .17–.32 ) .240 ( .17–.32 ) .240 ( .17–.32 ) .240 ( .17–.32 ) GSM8K .064 ( .05–.09 ) .058 ( .04–.08 ) .048 ( .03–.07 ) .046 ( .03–.07 ) .046 ( .03–.07 ) MMLU .212 ( .18–.25 ) .206 ( .17–.24 ) .210 ( .18–.25 ) .204 ( .17–.24 ) .200 ( .17–.24 )

[464] h5: Q2: Variance reduction.

[465] p: The synthetic validation (Appendix C , Figure 7 ) confirms the predicted exponential decay under controlled conditions with known p ⋆ p^{\star} . The real-data results in Table 5 are consistent with this pattern. On high-accuracy benchmarks, mode error decreases with K K : TruthfulQA drops from 0.034 to 0.022 (35% reduction), and GSM8K drops from 0.064 to 0.046 (28% reduction). On moderate-accuracy benchmarks (HumanEval, BigBench, MMLU), mode error remains relatively flat across K K values, consistent with the theoretical prediction that variance reduction is most pronounced when p ⋆ p^{\star} is well above 0.5. We note that adjacent K K -to- K K differences are not individually significant (the Wilson CIs in Table 5 overlap); the evidence is in the monotone trend across all K K values rather than any single pairwise comparison.

[466] p: GSM8K provides a particularly clean test of variance reduction because canonicalization is deterministic (numeric extraction): there is no canonicalization noise, so any reduction in mode error is purely attributable to consensus aggregation.

[467] p: HumanEval may exhibit a counterintuitive increase in mode error with larger K K for items with pass rate p < 0.5 p<0.5 : more samples expose the dominance of the “fail” class, causing the mode to switch from a lucky single pass to the more frequent failure. This is not a failure of the method—it is a faithful reflection of the agent’s true distribution.

[468] figure: Figure 3. Variance reduction: mode error vs. K K across all five benchmarks. TruthfulQA and GSM8K show clear monotone decrease consistent with Theorem 4.4 . HumanEval exhibits a counterintuitive increase at low K K : for items with pass rate p < 0.5 p<0.5 , more samples expose the dominance of the “fail” class, switching the mode from a lucky pass to the more frequent failure—a theoretically predicted effect (Section 11.3 ), not a method failure. BigBench and MMLU show relatively flat error, consistent with theory: variance reduction is most pronounced when p ⋆ p^{\star} is far from the decision boundary.

[469] h3: 11.4. Set size as uncertainty diagnostic

[470] h5: Q3: Set size reflects model uncertainty.

[471] p: Figure 4 shows prediction set size vs. consensus entropy H ( x ) = − ∑ c p ^ c log p ^ c H(x)=-\sum_{c}\hat{p}_{c}\log\hat{p}_{c} . Items with H ⁡ ( x ) = 0 H(x)=0 (all K = 10 K{=}10 samples agree) receive singleton prediction sets ( | S | = 1 |S|=1 ), while items with H ⁡ ( x ) > 0 H(x)>0 (the model disagrees across samples) receive larger sets. The conformal prediction set naturally adapts to per-item uncertainty without requiring any calibration of an uncertainty score—set size is the uncertainty diagnostic. The synthetic validation (Appendix C , Figure 11 ) shows the same pattern under controlled conditions.

[472] p: GSM8K is expected to show particularly clean entropy–set-size correlation due to its deterministic canonicalization: any disagreement in the model’s answers directly reflects uncertainty about the numeric answer, not canonicalization noise.

[473] figure: Figure 4. Mean prediction set size vs. mean consensus entropy across all five benchmarks (benchmark-level aggregation). Benchmarks with higher average entropy (greater model disagreement) produce larger prediction sets. The per-item correlation underlying this aggregate pattern is confirmed in the synthetic validation (Figure 11 ), where individual items are plotted. Error bars show 95% bootstrap CIs.

[474] h3: 11.5. Sequential stopping

[475] p: Table 6 reports results for the Hoeffding-based sequential stopping rule (Theorem 9.1 , δ = 0.05 \delta=0.05 ).

[476] figure: Table 6. Sequential stopping results for GPT-4.1 ( δ = 0.05 \delta=0.05 , K max = 20 K_{\max}=20 ). Coverage and set size are preserved while using fewer samples. 95% CIs in parentheses. Dataset Avg. K K used Savings Seq. Coverage Seq. Avg. | S | |S| HumanEval 11.05 ( 10.3–11.9 ) 44.8% 0.720 ( 0.61–0.81 ) 1.28 TruthfulQA 9.67 ( 9.4–9.9 ) 51.7% 0.980 ( 0.96–0.99 ) 1.00 BigBench 9.92 ( 9.4–10.4 ) 50.4% 0.792 ( 0.71–0.85 ) 1.10 GSM8K 9.85 ( 9.6–10.1 ) 50.8% 0.952 ( 0.93–0.97 ) 1.00 MMLU 9.98 ( 9.7–10.3 ) 50.1% 0.834 ( 0.80–0.86 ) 1.11

[477] p: Across all five benchmarks, sequential stopping reduces the average number of samples from K max = 20 K_{\max}=20 to approximately 10 10 ( 45 45 – 52 % 52\% savings), with coverage and prediction set sizes preserved exactly (Table 6 ). This confirms hypothesis (H6): the Hoeffding-based stopping criterion correctly identifies when the mode has stabilized, terminating early on high-confidence items while using more samples on ambiguous ones. Items that consistently require the full K max K_{\max} are those near the decision boundary ( p ⋆ ≈ 0.5 p^{\star}\approx 0.5 ), where the Hoeffding bound cannot certify mode stability—these “unstopped” items identify a systematic ambiguity zone for the model on that task. The cost implications are quantified in Table 7 .

[478] h3: 11.6. Cost analysis

[479] p: Table 7 reports estimated API costs per method and model. Costs are computed from the number of API calls required (items × \times samples per item) using published pricing for each model.

[480] figure: Table 7. Estimated API cost (USD) per evaluation method and model. GPT-4.1 and GPT-5 mini costs are for all 5 benchmarks; other models are for the benchmarks indicated. “Full” = K max = 20 K_{\max}=20 samples per item; “Sequential” = adaptive stopping; “Single” = 1 sample; “Judge” = 1 judge call per test item. Model Full budget Sequential Single sample Judge baseline GPT-4.1 $168.01 $125.13 $4.20 $3.88 GPT-4.1-mini † $20.80 $10.40 $1.04 $2.40 GPT-4.1-nano † $1.60 $0.80 $0.08 $2.40 GPT-5 mini $33.60 $25.03 $0.84 $3.88 Llama 4 Maverick ‡ $7.84 $3.92 $0.39 $2.88 Mistral Small ‡ $2.40 $1.20 $0.12 $2.88 † 2 benchmarks only (GSM8K + MMLU). ‡ 3 benchmarks (GSM8K + MMLU + TruthfulQA) via Together AI. Token counts validated on representative API calls: ∼ 85 {\sim}85 input and ∼ 66 {\sim}66 output tokens per sample call (cross-benchmark average; GSM8K uses ∼ 300 {\sim}300 total due to chain-of-thought), ∼ 215 {\sim}215 input / ∼ 7 {\sim}7 output per judge call. Dollar amounts above use conservative upper-bound token estimates ( 500 / 200 500/200 sample, 800 / 100 800/100 judge) rather than observed averages ( 85 / 66 85/66 and 215 / 7 215/7 ); actual costs are approximately 3 3 – 4 × 4\times lower. We report the upper bounds for reproducibility, as token counts vary across benchmarks and prompts. Judge always uses GPT-4.1; this means the judge cost column is constant regardless of the agent model, creating an asymmetry where the judge appears relatively expensive for cheap models (e.g., GPT-4.1-nano) and cheap for expensive ones. Sequential costs use GPT-4.1 stopping profile ( K ¯ ≈ 10 \bar{K}\approx 10 ) for all models. Open-weight model costs reflect Together AI serverless pricing ($0.27/$0.85 per 1M tokens for Maverick, $0.10/$0.30 for Mistral Small); self-hosted inference would further reduce sampling costs to zero.

[481] p: The cost overhead of self-consistency sampling is K × K\times compared to single-sample evaluation, but sequential stopping recovers approximately half of this cost (Table 7 ). The key insight is that self-consistency is an evaluation cost , not a deployment cost: it is paid once to obtain calibrated reliability estimates, not at every inference call. Smaller models reduce costs dramatically (GPT-4.1-nano: ∼ $ 2 {\sim}\$2 full, ∼ $ 1 {\sim}\$1 sequential for 2 benchmarks).

[482] h3: 11.7. Canonicalization ablation

[483] p: Table 8 compares the full canonicalized method against raw-string ranking on the two non-binary benchmarks.

[484] figure: Table 8. Canonicalization ablation: average prediction set size with and without canonicalization ( α = 0.10 \alpha=0.10 , GPT-4.1). Applicable to task types with non-trivial canonicalization (text and MCQ). Dataset Canonical | S | |S| Raw | S | |S| Reduction TruthfulQA 1.00 1.00 0.0% BigBench 1.10 1.81 39.2% MMLU 1.11 1.41 21.3% GSM8K and HumanEval are excluded because their canonicalization is already deterministic (numeric extraction and code execution, respectively).

[485] p: The effect of canonicalization is task-dependent (Table 8 , Figure 5 ). BigBench shows the largest reduction ( 39.2 % 39.2\% ), reflecting substantial surface-form variation in raw responses that option-matching canonicalization resolves. MMLU shows a 21.3 % 21.3\% reduction. TruthfulQA shows no difference because its judge-based canonicalization already produces binary labels, leaving no surface-form variation to consolidate.

[486] figure: Figure 5. Canonicalization effect on average prediction set size. BigBench shows a 39.2 % 39.2\% reduction (the largest effect), MMLU shows 21.3 % 21.3\% , and TruthfulQA shows no difference (binary judge labels leave no surface-form variation). GSM8K and HumanEval are excluded (deterministic canonicalization).

[487] h3: 11.8. Comparison with alternative nonconformity scores

[488] p: We compare our rank-based score (Definition 6.2 ) against two standard scores from the conformal classification literature [ Kumar2023ConformalNLP , Romano2020Classification ] , all computed from the same cached K = 10 K{=}10 samples at zero additional cost:

[489] p: Least Ambiguous set-valued Classifier (LAC): s i LAC = 1 − P ^ ​ ( c ⋆ ) s_{i}^{\mathrm{LAC}}=1-\hat{P}(c^{\star}) , where P ^ ​ ( c ) = count ​ ( c ) / K \hat{P}(c)=\mathrm{count}(c)/K . Prediction sets include all classes c c with 1 − P ^ ​ ( c ) ≤ τ 1-\hat{P}(c)\leq\tau .

[490] p: Adaptive Prediction Sets (APS): s i APS = ∑ j = 1 r i P ^ ​ ( c ( j ) ) + U ⋅ P ^ ​ ( c ( r i ) ) s_{i}^{\mathrm{APS}}=\sum_{j=1}^{r_{i}}\hat{P}(c_{(j)})+U\cdot\hat{P}(c_{(r_{i})}) , where c ( j ) c_{(j)} are classes sorted by decreasing P ^ \hat{P} , r i r_{i} is the rank at which the correct class appears, and U ∼ Unif ⁡ ( 0 , 1 ) U\sim\mathrm{Unif}(0,1) randomizes the inclusion boundary.

[491] p: Both LAC and APS are continuous-valued (resolution 1 / K 1/K ), whereas our rank score is a discrete integer. Quach et al. [ Quach2023ConformalLM ] target token-level sequence generation—a fundamentally different setting from our class-level conformal framework—so no direct comparison is applicable.

[492] p: Table 9 reports coverage, average set size, and conditional coverage for all three scores across the GPT-4.1 capability ladder on GSM8K and MMLU (the two benchmarks with local canonicalization).

[493] figure: Table 9. Comparison of nonconformity scores ( K = 10 K{=}10 , α = 0.10 \alpha=0.10 ). All three scores use identical cached samples. “Cond.” = conditional coverage among solvable items. Best coverage per row in bold . Coverage Avg. | S | |S| Model Dataset Rank LAC APS Rank LAC APS GPT-4.1 GSM8K 0.956 0.914 0.908 1.00 1.00 1.15 GPT-4.1 MMLU 0.980 1.000 1.000 1.11 1.13 1.13 GPT-4.1-mini GSM8K 0.954 0.900 0.902 1.00 1.00 1.12 GPT-4.1-mini MMLU 0.976 1.000 1.000 1.12 1.13 1.13 GPT-4.1-nano GSM8K 0.960 0.924 0.894 1.35 1.02 1.61 GPT-4.1-nano MMLU 0.940 1.000 1.000 1.17 1.20 1.20 Conditional coverage: on GSM8K, rank achieves ≥ 0.977 \geq 0.977 , LAC ≥ 0.922 \geq 0.922 , APS ≥ 0.923 \geq 0.923 across all models. On MMLU, rank achieves ≥ 0.988 \geq 0.988 , LAC and APS both achieve 1.000 1.000 . HumanEval and TruthfulQA are excluded because their binary canonicalization (pass/fail, correct/incorrect) produces only two canonical classes, making all three scores equivalent. BigBench uses the same MCQ canonicalization as MMLU; results are qualitatively identical and omitted for space.

[494] p: Two complementary patterns emerge. On GSM8K ( M ⋆ = 1 M^{\star}{=}1 for GPT-4.1 and GPT-4.1-mini), the rank score achieves the highest coverage ( 0.954 0.954 – 0.960 0.960 ), outperforming LAC ( 0.900 0.900 – 0.924 0.924 ) and APS ( 0.894 0.894 – 0.908 0.908 ) by 3 3 – 7 7 percentage points. With K = 10 K{=}10 , the empirical probabilities P ^ ​ ( c ) \hat{P}(c) have resolution 0.1 0.1 , so the continuous scores’ threshold quantile can be tight. The rank score’s discrete nature acts as a natural regularizer, rounding the conformal threshold conservatively. On MMLU ( M ⋆ = 2 M^{\star}{=}2 ), LAC and APS both achieve perfect coverage ( 1.000 1.000 ) but with slight over-coverage compared to the 90 % 90\% target, while rank stays closer to the nominal level ( 0.940 0.940 – 0.980 0.980 ). Set sizes are comparable across all three scores ( | S | ¯ ≈ 1.1 \bar{|S|}\approx 1.1 – 1.2 1.2 ). The most striking case is GPT-4.1-nano on GSM8K: APS produces the largest sets ( | S | ¯ = 1.61 \bar{|S|}{=}1.61 ) yet the lowest coverage ( 0.894 0.894 )—the randomization in APS adds noise rather than precision when K K is small. In the controlled synthetic setting (Appendix C , Figures 8 – 9 ), APS and LAC achieve lower MSE than Rank due to their finer-grained continuous thresholds; however, Rank provides the widest coverage safety margin, and the distribution-specific failures observed here (under-coverage, threshold saturation) do not arise in that idealized setting. Overall, in the K ≤ 20 K{\leq}20 regime typical of API-based evaluation, the rank score’s robustness to coarse probability estimates and real-world distribution skew makes it a pragmatic default.

[495] p: APS’s coverage of 0.894 0.894 falling below the 0.90 0.90 nominal level does not contradict conformal guarantees. Conformal coverage holds marginally —in expectation over the random calibration/test split—so any single split may fall slightly below the nominal level. At n cal = 500 n_{\mathrm{cal}}=500 , the 1 / ( n + 1 ) 1/(n{+}1) slack is only 0.002 0.002 , but APS’s randomization ( U ∼ Unif ⁡ ( 0 , 1 ) U\sim\mathrm{Unif}(0,1) tie-breaking) introduces additional sampling variance that amplifies finite-sample deviations, particularly when K K is small and probability estimates are coarse.

[496] h3: 11.9. Discussion

[497] p: Four themes emerge from these results: the calibration is accurate, the framework is honest about limitations, the patterns generalize across model families, and the reliability level provides a practical deployment metric.

[498] h5: Calibration quality is confirmed by conditional coverage.

[499] p: How do we know the calibration is working? We compute coverage restricted to “solvable” items—those where the model produced at least one correct answer across all K max K_{\max} samples. Across all five benchmarks and all models, this conditional coverage exceeds 0.93 0.93 (Table 2 ), confirming that conformal calibration is nearly perfectly calibrated whenever the model has non-zero capability. Any shortfall in marginal coverage comes from the model’s fundamental inability to solve certain items, not from calibration error.

[500] p: We emphasize that conditional coverage is a post-hoc diagnostic that validates the theory’s prediction (Theorem 7.5 (3): when the unsolvable fraction β \beta exceeds α \alpha , M ⋆ = + ∞ M^{\star}=+\infty ), not a guarantee available at deployment time. The “solvable” designation requires observing all K max K_{\max} samples, which is unavailable during calibration. For deployment decisions, the reliability level (Definition 2.4 , Table 10 ) provides the actionable metric: it quantifies the confidence at which mode voting suffices, directly from calibration scores, without requiring knowledge of which items are solvable.

[501] p: Concretely, a practitioner does not need to distinguish capability gap from calibration failure before deployment—the reliability level answers the deployment question directly. HumanEval’s reliability level is 69.9 % 69.9\% (Table 10 ). If the deployment requirement is 90 % 90\% reliability, this model–task pair fails the gate. If 70 % 70\% suffices, it passes. The framework provides the actionable number; diagnosing why coverage is low (capability gap vs. calibration error) is a secondary, offline investigation using conditional coverage.

[502] h5: The framework diagnoses capability honestly.

[503] p: HumanEval illustrates the boundary condition most clearly: coverage falls below 90 % 90\% ( 0.707 0.707 ) because 26.8 % 26.8\% of problems are unsolvable—none of the K max = 20 K_{\max}{=}20 samples produce passing code. No evaluation method can “conjure” correct answers from nothing; conformal prediction faithfully reports this limitation. The LLM judge, by contrast, achieves an artificially high 0.915 0.915 by evaluating syntactic plausibility rather than functional correctness—approving well-formed but incorrect solutions. Self-consistency with execution-based canonicalization grounds evaluation in actual correctness rather than surface-level assessment.

[504] h5: The pattern generalizes across model families.

[505] p: The capability-ladder comparison (Table 3 ) confirms that M ⋆ M^{\star} and | S | ¯ \bar{|S|} increase monotonically with decreasing capability, as predicted by Theorem 7.5 . This monotonicity holds within the GPT-4.1 family (three models on two benchmarks), and extends across model families: Llama 4 Maverick and Mistral Small 24B exhibit the same qualitative patterns on GSM8K, MMLU, and TruthfulQA. On GSM8K, all three families achieve M ⋆ = 1 M^{\star}{=}1 ; on TruthfulQA, the open-weight models require M ⋆ = 2 M^{\star}{=}2 (vs. 1 1 for GPT-4.1), consistent with their lower per-sample accuracy. Conditional coverage on solvable items remains high across all families ( ≥ 0.949 \geq 0.949 ). The bootstrap split analysis (Table 4 ) confirms that M ⋆ M^{\star} values are stable across random data partitions. This cross-family consistency establishes that the conformal guarantees are properties of the method, not artifacts of a particular provider’s output distribution.

[506] h5: Reliability certification provides the practical payoff.

[507] p: The reliability level (Definition 2.4 ) yields a single-number deployment summary for each model–task combination; Table 10 reports it across all configurations. This enables direct deployment gating: “we need X % X\% reliability—which models qualify?” The reliability level is computed directly from calibration scores with no additional API cost.

[508] figure: Table 10. Reliability certification: reliability level 1 − α ⋆ 1{-}\alpha^{\star} (%) for each model–task combination. Higher is better. “—” indicates the model was not evaluated on that benchmark. Boldface marks combinations where M ⋆ = 1 M^{\star}{=}1 at α = 0.10 \alpha{=}0.10 (mode voting alone suffices). Model GSM8K MMLU TruthfulQA BigBench HumanEval GPT-4.1 94.6 83.4 96.8 75.4 69.9 GPT-4.1-mini 96.0 81.6 — — — GPT-4.1-nano 89.8 66.5 — — — Llama 4 Maverick 95.4 66.7 85.3 — — Mistral Small 93.8 77.8 84.8 — — Reliability decreases monotonically with capability within each family. On MMLU: GPT-4.1 ( 83.4 % 83.4\% ) > > GPT-4.1-mini ( 81.6 % 81.6\% ) > > Mistral Small ( 77.8 % 77.8\% ) > > Llama 4 Maverick ( 66.7 % 66.7\% ) ≈ \approx GPT-4.1-nano ( 66.5 % 66.5\% ). Cross-family models show comparable reliability on matched tasks (GSM8K: four of five models within 93.8 93.8 – 96.0 % 96.0\% ; GPT-4.1-nano at 89.8 % 89.8\% ).

[509] h5: Hypothesis validation.

[510] p: All six hypotheses are supported (Tables 2 – 6 ): coverage holds on solvable items with conditional coverage ≥ 0.93 \geq 0.93 across all models and benchmarks (H1); mode error decays with K K on high-accuracy tasks, with TruthfulQA dropping 35 % 35\% and GSM8K dropping 28 % 28\% , though adjacent- K K Wilson CIs overlap on moderate-accuracy benchmarks, so evidence for H2 rests on the monotone trend rather than pairwise significance; prediction set size correlates positively with consensus entropy (H3) and decreases with canonicalization—BigBench by 39.2 % 39.2\% , MMLU by 21.3 % 21.3\% (H4); conformal coverage exceeds judge accuracy where ambiguity is high, with a 6 6 percentage point advantage on BigBench at matched cost (H5), though we note that the BigBench comparison ( n test = 125 n_{\mathrm{test}}=125 ) has wide confidence intervals; and sequential stopping saves 45 45 – 52 % 52\% of samples with zero quality loss (H6).

[511] h2: 12. Limitations

[512] p: Marginal coverage only. Theorem 6.7 provides marginal, not conditional, coverage. For individual difficult queries, the set may under-cover. Conditional coverage is impossible without assumptions [ Vovk2012Conditional , BarberCandes2019 ] , though group-conditional methods [ Romano2020Classification ] can partially address this.

[513] p: Calibration set cost. The framework requires n n human-labeled calibration examples. However, the calibration set is reusable across agents and is typically much smaller than full test sets (Corollary 7.10 : n ≥ 19 n\geq 19 suffices to achieve lower coverage error than typical judge bias).

[514] p: Canonicalization quality and circularity. Poor canonicalization inflates set sizes (Assumption 4.2 ). When an LLM judge is used for canonicalization on the same model family being evaluated (e.g., GPT-4.1 judging GPT-4.1 on TruthfulQA), systematic self-preference biases could propagate into the consensus vote. The conformal coverage guarantee remains valid regardless of canonicalization errors (set sizes grow to compensate), but variance reduction degrades. Our cross-family results (GPT-4.1 judging Llama/Mistral) provide a clean test of this concern—see Remark 4.3 . We recommend deterministic canonicalization wherever feasible.

[515] p: Infinite scores. When the agent never produces acceptable answers ( p ⋆ ​ ( x ) ≈ 0 p^{\star}(x)\approx 0 ), M ⋆ = + ∞ M^{\star}=+\infty . This is honest but limits practical utility for very weak agents. When multiple models all yield M ⋆ = + ∞ M^{\star}=+\infty , the framework cannot distinguish them via M ⋆ M^{\star} alone. The reliability level (Definition 2.4 ) partially addresses this: a model with reliability 55 % 55\% is distinguishable from one at 40 % 40\% , even though both have M ⋆ > 1 M^{\star}>1 at α = 0.10 \alpha=0.10 . For very weak models where even the reliability level is uninformative, the minimum α \alpha at which M ⋆ M^{\star} is finite provides additional comparative signal.

[516] p: Conformal calibration diagnoses, does not repair. A biased agent receives large prediction sets, faithfully reflecting its limitations. The framework provides a reliable measurement of performance, not a method for improving it.

[517] p: Model family scope. The capability-ladder validation uses the GPT-4.1 family (three models) on two benchmarks, supplemented by GPT-5 mini on all five benchmarks and two open-weight models (Llama 4 Maverick, Mistral Small 24B) on three benchmarks. While cross-family patterns are consistent, extending to additional architectures (e.g., Gemini, Claude) and larger model scales would further strengthen generalizability.

[518] p: Deployment exchangeability and benchmark contamination. The conformal guarantee requires exchangeability between calibration and test data (Remark 6.5 ). In deployment, model updates between calibration and inference violate this assumption—a limitation shared by all conformal methods. Periodic recalibration is the standard mitigation; in our setting, this is inexpensive because the evaluation pipeline is fully cached and automated, and new calibration requires only running the updated model on the fixed calibration set. Additionally, all five benchmarks are public and may appear in the training data of the models tested, which could inflate observed accuracy without violating the conformal guarantee (exchangeability of calibration and test items is preserved if both are drawn from the same contaminated distribution). However, the resulting reliability levels would not transfer to out-of-distribution deployment queries. This is not specific to our method—it applies to any benchmark-based evaluation, whether conformal, LLM-as-judge, or human-graded. Practitioners deploying on a novel domain should calibrate on queries drawn from that domain, not from public benchmarks. The calibration cost is modest (Section 1 : 50 − 100 50{-}100 spot-checks), making domain-specific recalibration practical.

[519] h2: 13. Conclusion

[520] p: The central contribution of this work is the reliability level —a single number that answers: “given any black-box AI system and any task with a small calibration set, can I trust this system at X % X\% confidence?” The reliability level is computed directly from conformal calibration scores, requires no additional API cost beyond the evaluation itself, and generalizes across model families (Table 10 ).

[521] p: Theoretically, self-consistency sampling achieves exponential variance decay (Theorem 4.4 ), while conformal calibration ensures validity within 1 / ( n + 1 ) 1/(n{+}1) of the target level, independent of agent bias (Theorem 7.1 ). Remaining bias surfaces as wider prediction sets rather than hidden error (Theorem 7.5 ). Once the calibration set is large enough that the conformal slack 1 / ( n + 1 ) 1/(n{+}1) falls below the judge’s bias—as few as n = 19 n=19 for subjective tasks with | b J | ≥ 0.05 |b_{J}|\geq 0.05 —the evaluation’s coverage error is smaller than the judge’s (Corollary 7.10 ), though the two approaches remain complementary (Remark 7.11 ).

[522] p: Empirically, the guarantees hold across all fifteen model–task configurations tested, spanning three model families and both synthetic and real data. Conditional coverage on solvable items exceeds 0.93 0.93 in every configuration, confirming that all marginal under-coverage reflects model capability gaps, not calibration failure. Sequential stopping reduces API costs by ∼ 50 % {\sim}50\% without sacrificing coverage or set size quality.

[523] p: Several directions merit investigation. First, conditional coverage guarantees—per-query rather than marginal validity—would strengthen deployment confidence, though known impossibility results [ Vovk2012Conditional ] impose fundamental limits. Second, active-learning strategies for calibration set construction could reduce the labeling budget below the current n ≥ 19 n\geq 19 threshold. Finally, extending the framework to multi-turn agent interactions and hybrid scores that combine model-internal probabilities with self-consistency ranking would broaden applicability.

[524] h5: Reproducibility.

[525] p: All code, configuration files, and result summaries are available at https://github.com/Cohorte-ai/trustgate-paper . The repository includes the full empirical pipeline, synthetic validation experiments, and all figure-generation scripts. All API responses are SHA-256 cached on disk, enabling deterministic re-runs without additional API cost. Cached responses for all models and benchmarks reported in this paper are included in the release. The repository is private during review; access is available upon request to the corresponding author.

[526] h2: Appendix A Canonicalization Implementation Details

[527] p: This appendix provides full implementation details for the three canonicalization regimes summarized in Section 4.3 .

[528] h3: A.1. Deterministic canonicalization (closed-form tasks)

[529] p: For tasks with structured answers—numbers, dates, entity IDs, labels, code outputs—the canonicalization is deterministic:

[530] p: Parse the raw answer into a typed representation (numeric, date, identifier).

[531] p: Normalize units, locale formatting, and whitespace.

[532] p: Serialize to a stable canonical string.

[533] p: Map parse failures to a dedicated INVALID class.

[534] p: This eliminates surface-form fragmentation entirely and enables exact class counts. For mathematical reasoning (e.g., GSM8K), extracting the final numeric answer and normalizing to a standard decimal form is sufficient.

[535] h3: A.2. Embedding-based clustering (open-ended tasks)

[536] p: For free-form answers where deterministic parsing is impossible, we cluster semantically equivalent answers:

[537] p: Compute dense embeddings e ⁡ ( a i ) e(a_{i}) for each sample (e.g., via Sentence-BERT [ Reimers2019SentenceBERT ] ).

[538] p: Build a similarity graph with edge threshold τ cos \tau_{\cos} on cosine similarity.

[539] p: Cluster via connected components or density-based methods (e.g., HDBSCAN [ McInnes2017HDBSCAN ] ).

[540] p: Assign each cluster a canonical representative (medoid or LLM-generated summary).

[541] p: The threshold τ cos \tau_{\cos} is a hyperparameter that trades off between over-merging (collapsing distinct answers) and under-merging (fragmenting equivalent answers). Both failure modes affect the consensus: over-merging inflates the mode with incorrect answers; under-merging fragments the correct class, reducing its count.

[542] h3: A.3. LLM-assisted canonicalization

[543] p: A lightweight LLM can map each raw answer to a concise canonical form before clustering:

[544] p: Prompt a cheap, fast model to extract the “core answer” from each raw response.

[545] p: Optionally normalize to a closed ontology or structured schema.

[546] p: Apply deterministic or embedding-based canonicalization on the extracted forms.

[547] p: This is useful when answers contain extraneous reasoning, caveats, or formatting. Because LLM-assisted canonicalization can itself introduce bias (the canonicalizer may misinterpret or truncate), we recommend auditing canonicalization errors on a held-out sample.

[548] h3: A.4. Stability requirements

[549] p: To ensure the consensus vote is meaningful, canonicalization must satisfy empirically verifiable stability conditions:

[550] p: Bootstrap stability: resample the K K answers, re-canonicalize, and measure cluster agreement via the adjusted Rand index (ARI). Require ARI ≥ 0.8 \geq 0.8 for reporting.

[551] p: Threshold sensitivity: vary τ cos \tau_{\cos} over a range [ τ cos − ϵ , τ cos + ϵ ] [\tau_{\cos}-\epsilon,\tau_{\cos}+\epsilon] and verify the winning canonical class is unchanged.

[552] p: Merge/split audit: on a random sample of clusters, manually verify that merged answers are semantically equivalent and split answers are semantically distinct.

[553] p: These diagnostics should be reported alongside experimental results. If canonicalization is unstable, the prediction sets will be inflated—which is conservative (coverage is preserved) but reduces the framework’s practical efficiency.

[554] h2: Appendix B Notation Summary

[555] p: Table 11 summarizes the key symbols used throughout the paper.

[556] figure: Table 11. Summary of notation. Symbol Meaning 𝒳 {\mathcal{X}} , 𝒜 {\mathcal{A}} Query space, answer space f θ f_{\theta} Agent with parameters θ \theta ; stochastic map 𝒳 → 𝒜 {\mathcal{X}}\to{\mathcal{A}} 𝒜 ⋆ ​ ( x ) {\mathcal{A}}^{\star}(x) Set of acceptable answers for query x x Canon ⁡ ( x , a ) \mathrm{Canon}(x,a) Canonicalization function mapping raw answers to canonical classes K K Number of i.i.d. samples per query K max K_{\max} Maximum samples per query (budget) p ⋆ ​ ( x ) p^{\star}(x) Per-query probability of producing an acceptable answer p ¯ \bar{p} Average acceptability rate 𝔼 x ​ [ p ⋆ ​ ( x ) ] {\mathbb{E}}_{x}[p^{\star}(x)] p canon p_{\mathrm{canon}} Probability mass on the correct canonical class after canonicalization s i s_{i} Nonconformity score for calibration item i i (rank of acceptable answer) M ⋆ M^{\star} Conformal threshold: ⌈ ( 1 − α ) ​ ( n + 1 ) ⌉ \lceil(1-\alpha)(n+1)\rceil -th order statistic of { s i } \{s_{i}\} S ⁡ ( x ) S(x) Prediction set: top- M ⋆ M^{\star} canonical answers for query x x | S ⁡ ( x ) | |S(x)| Prediction set size α \alpha Miscoverage level; target coverage is 1 − α 1-\alpha n n Calibration set size b J b_{J} LLM-judge bias H ⁡ ( x ) H(x) Consensus entropy for query x x ϕ ⁡ ( x ) \phi(x) Consensus strength: P ^ K ​ ( c ( 1 ) ∣ x ) \hat{P}_{K}(c_{(1)}\mid x) Δ ⁡ ( x ) \Delta(x) Consensus margin: P ^ K ​ ( c ( 1 ) ∣ x ) − P ^ K ​ ( c ( 2 ) ∣ x ) \hat{P}_{K}(c_{(1)}\mid x)-\hat{P}_{K}(c_{(2)}\mid x) 1 − α ⋆ 1{-}\alpha^{\star} Reliability level (Definition 2.4 ) τ δ \tau_{\delta} Sequential stopping time at confidence 1 − δ 1{-}\delta

[557] h2: Appendix C Synthetic Validation

[558] p: Before evaluating on real benchmarks, we validate the theoretical results using controlled synthetic agents with known parameters. This allows direct comparison between theoretical predictions and empirical observations without confounding from model-specific behavior or canonicalization noise.

[559] h3: C.1. Setup

[560] p: We construct synthetic agents as multinomial distributions over a finite set of canonical classes 𝒞 = { c 1 , … , c L } {\mathcal{C}}=\{c_{1},\dots,c_{L}\} . For each experiment, we specify the agent’s true distribution P θ ( ⋅ ∣ x ) P_{\theta}(\cdot\mid x) and run the full pipeline: sampling, ranking, conformal calibration, and prediction set construction. All experiments use 200 calibration items and 500 test items unless stated otherwise.

[561] h3: C.2. Coverage validation (Theorem 6.7 )

[562] p: We verify that empirical coverage matches the target 1 − α 1-\alpha across a sweep of α ∈ { 0.01 , 0.05 , 0.10 , 0.15 , 0.20 , 0.25 , 0.30 } \alpha\in\{0.01,0.05,0.10,0.15,0.20,0.25,0.30\} for agents with varying quality levels. Figure 6 confirms that coverage is consistently at or above the target for all alpha levels, with the slight conservatism predicted by the 1 / ( n + 1 ) 1/(n+1) upper bound in ( 6.6 ).

[563] figure: Figure 6. Synthetic coverage validation: empirical coverage vs. target 1 − α 1-\alpha for agents with p ⋆ ∈ { 0.6 , 0.7 , 0.8 } p^{\star}\in\{0.6,0.7,0.8\} . All points lie on or above the diagonal, confirming Theorem 6.7 .

[564] h3: C.3. Variance reduction (Theorem 4.4 )

[565] p: We measure mode error as a function of K K for agents with known p ⋆ ∈ { 0.60 , 0.70 , 0.80 } p^{\star}\in\{0.60,0.70,0.80\} and overlay the Hoeffding upper bound exp ⁡ ( − 2 ​ K ​ ( p ⋆ − 1 / 2 ) 2 ) \exp\!\bigl(-2K(p^{\star}-1/2)^{2}\bigr) . Figure 7 shows that empirical mode error decays exponentially and stays below the Hoeffding bound at all K K values, validating the exponential decay predicted by Theorem 4.4 . The real-data results in Section 11.3 are consistent with this pattern.

[566] figure: Figure 7. Synthetic variance reduction: mode error vs. K K for three agents with known p ⋆ p^{\star} . Dashed lines show Hoeffding upper bounds. Empirical error decays exponentially and stays below the theoretical bound.

[567] h3: C.4. Bias–variance decomposition (Section 3 )

[568] p: We compare six evaluation methods—single sample, LLM-as-judge (simulated with known bias), self-consistency mode, and three conformal scores (Rank, LAC, APS)—on a mixture of easy ( p ⋆ = 0.75 p^{\star}{=}0.75 ) and hard ( p ⋆ = 0.35 p^{\star}{=}0.35 , mode is wrong) queries. Figures 8 and 9 show the decomposition at K = 20 K{=}20 and K = 10 K{=}10 respectively.

[569] p: The primary finding is that all three conformal methods reduce MSE by 50 50 – 200 × 200\times compared to non-conformal baselines, confirming the decomposition in Table 1 . This gap dwarfs differences between conformal scores.

[570] h5: Interpreting conformal bias.

[571] p: The Bias 2 bars for conformal methods appear larger than for single-sample evaluation, but the underlying bias has a fundamentally different character. For the judge and self-consistency mode, bias reflects over-estimation of accuracy —the method reports higher correctness than the true p ⋆ p^{\star} , giving false confidence. For conformal methods, bias reflects over-coverage —the prediction set contains the correct answer more often than the 1 − α 1{-}\alpha target requires (coverage annotations shown below conformal bars). Over-coverage is conservative: it errs on the side of safety. Rank’s coverage of 0.946 0.946 at K = 10 K{=}10 (vs. the 0.90 0.90 target) represents a desirable safety margin, not a deficiency.

[572] h5: Score comparison.

[573] p: Among the conformal scores, APS and LAC achieve lower MSE than Rank at both K K values, because their continuous thresholds produce tighter calibration (less over-coverage). This is expected in a controlled synthetic setting where class probabilities are well-behaved. However, the Rank score provides the most conservative coverage— 0.946 0.946 at K = 10 K{=}10 vs. APS at 0.901 0.901 (barely above the 0.90 0.90 target)—giving the widest safety margin.

[574] p: The empirical results (Section 11.8 ) reveal that on real LLM distributions, the continuous scores’ advantage reverses: with K = 10 K{=}10 , APS under-covers on GSM8K ( 0.894 < 0.90 0.894<0.90 ) and both LAC and APS degenerate to 100 % 100\% coverage on MMLU (threshold saturates at τ = 1 \tau{=}1 ). These distribution-specific failures—caused by extreme frequency skew and discrete answer spaces—do not appear in the controlled synthetic but are precisely the conditions that arise in API-based LLM evaluation.

[575] figure: Figure 8. Bias–variance decomposition at K = 20 K{=}20 (probability resolution 1 / K = 0.05 1/K{=}0.05 ). All conformal methods achieve 50 50 – 200 × 200\times lower MSE than non-conformal baselines. Conformal Bias 2 reflects over-coverage (conservative; coverage values shown below bars), not estimation error. Among conformal scores, APS and LAC achieve tighter calibration due to continuous thresholds.

[576] figure: Figure 9. Bias–variance decomposition at K = 10 K{=}10 (probability resolution 1 / K = 0.10 1/K{=}0.10 ), the regime typical of API-based evaluation. The conformal advantage persists. Rank provides the widest coverage margin ( 0.946 0.946 vs. APS at 0.901 0.901 ); on real LLM distributions (Section 11.8 ), this conservatism prevents the coverage violations that affect APS.

[577] h3: C.5. Set size vs. agent quality (Theorem 7.5 )

[578] p: We vary p ⋆ p^{\star} from 0.3 0.3 to 1.0 1.0 and measure M ⋆ M^{\star} . Figure 10 confirms Theorem 7.5 : M ⋆ M^{\star} is monotonically decreasing in agent quality, reaching M ⋆ = 1 M^{\star}=1 for perfect agents ( p ⋆ = 1 p^{\star}=1 ) and growing without bound as p ⋆ → 0 p^{\star}\to 0 .

[579] figure: Figure 10. Set size M ⋆ M^{\star} vs. agent quality p ⋆ p^{\star} . Better agents require smaller prediction sets. The step-function shape reflects the discrete nature of M ⋆ M^{\star} (the ⌈ ( n + 1 ) ​ ( 1 − α ) ⌉ \lceil(n+1)(1-\alpha)\rceil -th order statistic of integer-valued scores).

[580] h3: C.6. Set size vs. entropy (Hypothesis H3)

[581] p: We construct agents with varying entropy profiles and measure the correlation between consensus entropy H ⁡ ( x ) H(x) and prediction set size | S ⁡ ( x ) | |S(x)| . Figure 11 shows strong positive correlation ( r > 0.5 r>0.5 ), confirming that prediction set size adapts to per-item uncertainty.

[582] figure: Figure 11. Prediction set size vs. consensus entropy for synthetic agents. The strong positive correlation confirms that set size adapts to per-item uncertainty.

[583] h3: C.7. Canonicalization effect (Proposition 4.6 )

[584] p: We simulate fragmented distributions where 6 raw answer variants (total mass p = 0.60 p=0.60 ) map to a single canonical class. Figure 12 demonstrates that canonicalization consolidates the fragmented mass, dramatically reducing mode error from the raw case. This validates the amplification result of Proposition 4.6 .

[585] figure: Figure 12. Canonicalization effect: mode error with and without canonicalization for fragmented distributions. Canonicalization consolidates probability mass, reducing mode error exponentially as predicted by Proposition 4.6 .

[586] h2: Instructions for reporting errors

[587] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[588] p: Tip: You can select the relevant text first, to include it in your report.

[589] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[590] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
