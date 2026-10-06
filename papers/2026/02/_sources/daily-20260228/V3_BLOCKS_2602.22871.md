[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching

[3] h6: Abstract

[4] p: Reasoning with large language models often benefits from generating multiple chains-of-thought, but existing aggregation strategies are typically trajectory-level (e.g., selecting the best trace or voting on the final answer), discarding useful intermediate work from partial or “nearly correct” attempts. We propose Stitching Noisy Diffusion Thoughts, a self-consistency framework that turns cheap diffusion-sampled reasoning into a reusable pool of step-level candidates. Given a problem, we (i) sample many diverse, low-cost reasoning trajectories using a masked diffusion language model, (ii) score every intermediate step with an off-the-shelf process reward model (PRM), and (iii) stitch these highest-quality steps across trajectories into a composite rationale. This rationale then conditions an autoregressive (AR) model (solver) to recompute only the final answer. This modular pipeline separates exploration (diffusion) from evaluation and solution synthesis, avoiding monolithic unified hybrids while preserving broad search. Across math reasoning benchmarks, we find that step-level recombination is most beneficial on harder problems, and ablations highlight the importance of the final AR solver in converting stitched but imperfect rationales into accurate answers. Using low-confidence diffusion sampling with parallel, independent rollouts, our training-free framework improves average accuracy by up to 23.8% across six math and coding tasks. At the same time, it achieves up to a 1.8× latency reduction relative to both traditional diffusion models (e.g., Dream, LLaDA) and unified architectures (e.g., TiDAR). Code is available at https://github.com/roymiles/diffusion-stitching .

[5] h6: Keywords:

[6] figure: Figure 1 : Accuracy vs. wall-clock latency on Math500 comparing autoregressive baselines ( \mathbin{\hbox to5.62pt{\vbox to4.94pt{\pgfpicture\makeatletter\hbox{\hskip 0.25pt\lower-0.25pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {{\lx@inpgf@ignorespaces}} {}{{}}{} {}{} {}{} {\lx@inpgf@ignorespaces}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.6914,0.8164,0.8789}\lxSVG@fill\lxSVG@drawpath@unclipped{M 0 0 L 7.09 0 L 3.54 6.14 Z}{stroke:none} \lx@inpgf@ignorespaces \lxSVG@closescope {}{{}}{} {}{} {}{} {\lx@inpgf@ignorespaces}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.5,0.5,0.5}\lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.5pt} \lx@inpgf@ignorespaces{}\lxSVG@stroke\lxSVG@drawpath@unclipped{M 0 0 L 7.09 0 L 3.54 6.14 Z}{fill:none} \lx@inpgf@ignorespaces \lxSVG@closescope \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}} ) using early stopping, diffusion baselines ( ∘ \color[rgb]{0.5,0.5,0.5}\circ ), and our stitching pipeline ( ■ \color[rgb]{0.1211,0.4648,0.707}\blacksquare , ∙ \color[rgb]{0.1211,0.4648,0.707}\bullet ) using 4 reasoning traces. All models are 7B in size, except for LLaDA 2.0. All diffusion models are run without KV caching, so enabling caching ( Wu et al., 2025 ) would likely provide additional practical speedups.

[7] h2: 1 Introduction

[8] p: Large language models have become strong general-purpose reasoners, but reliable reasoning at test time is still expensive. On hard problems, accuracy often scales with the amount of computation devoted to search and naive scaling quickly becomes impractical. A core difficulty is that reasoning traces are noisy: a single incorrect intermediate step can derail an otherwise promising derivation, so allocating all compute to one long trajectory is risky. This motivates approaches that trade a single high-fidelity rationale for a broader exploration under a fixed latency budget.

[9] p: A common strategy is to sample multiple reasoning paths and aggregate them, e.g., via self-consistency or verifier-based selection ( Zhang et al., 2025a ) . However, most aggregation methods operate at the trajectory level: they choose one full chain (or vote over final answers), effectively discarding partial work from runs that contain useful intermediate results but fail later. In parallel, diffusion language models offer an appealing mechanism for broad exploration because they can refine partially masked sequences with parallel denoising, producing many diverse, low-cost reasoning trajectories. Recent unified hybrid models ( Liu et al., 2025 ) that combine diffusion-style refinement with autoregressive (AR) decoding can be effective, but they couple the exploration, scoring, and final generation stages together in a way that limits flexibility and makes targeted improvements harder. In practice, they also see a big drop in reasoning accuracy compared to the strong AR models.

[10] p: In this work, we propose Stitching Noisy Diffusion Thoughts, a self-consistency framework that turns diffusion sampling into a reusable pool of intermediate reasoning steps rather than a set of complete candidate solutions. Our key observation is that cheap diffusion-sampled chains can contain many locally correct sub-results. If we can identify these high-utility steps across trajectories and recombine them, we can recover much of the benefit of a broad search without paying for a single long derivation from scratch. Concretely, we advocate a specialist pipeline: a diffusion model for inexpensive exploration, a step-level evaluator to score intermediate reasoning, and a lightweight autoregressive model to produce the final answer conditioned on the stitched rationale.

[11] p: Our method has three components. (i) Explore: given an input problem, we sample N N diverse chains-of-thought using a masked diffusion language model with a confidence-based sampling procedure that encourages diversity while preserving high-confidence content. (ii) Evaluate: we score every intermediate step in every trajectory using an off-the-shelf process reward model (PRM), yielding a global pool of candidate steps with quality estimates. This step-level view is crucial: it allows us to retain useful intermediate results even when an overall trajectory later derails. (iii) Stitch + Recompute: rather than selecting a single “best” trajectory (e.g., by maximizing the geometric mean of step scores), we collect the highest-quality steps across paths and concatenate them into a composite rationale. A small autoregressive model then conditions on the original problem and this stitched rationale and recomputes the final answer.

[12] p: Empirically, this separation of roles makes the system both modular and effective. The diffusion component supplies breadth; the PRM provides a fine-grained notion of step quality; and the AR solver converts a partially redundant set of high-quality steps into a more accurate final response. This design also cleanly exposes ablations: we can quantify the value of (a) diffusion exploration alone, (b) trajectory-level selection, and (c) step-level stitching plus AR recomputation. In summary, our contributions are given as follows:

[13] p: We introduce a step-level self-consistency framework for reasoning that replaces trajectory-level selection with PRM-scored step selection and stitching over diffusion-sampled chains-of-thought.

[14] p: We analyze key stitching choices: generation count, diffusion diversity (e.g., temperature), PRM thresholding/anchoring, and a lightweight AR solver. In doing so we show how each component improves robustness and test-time scaling.

[15] p: We demonstrate strong reasoning under tight latency budgets, improving the accuracy–latency Pareto frontier over state-of-the-art AR and diffusion baselines (see Figure 1 and 4 ), with up to 9.85 × \times fewer sequential forward passes / 1.8 × \times lower end-to-end latency at matched accuracy, and up to +30.6% absolute accuracy points over vanilla diffusion decoding.

[16] h2: 2 Related Work

[17] h4: Diffusion Language Models.

[18] p: Masked diffusion language models (dLLMs) ( Nie et al., 2025 ) formulate generation as iterative denoising of a partially masked sequence. This view connects discrete diffusion and masked modeling by leveraging bidirectional Transformers for parallel refinement ( Devlin et al., 2019 ; Austin et al., 2025 ; Hoogeboom et al., 2021 ; Ghazvininejad et al., 2019 ) . In the text domain, diffusion has been investigated for controllable and conditional generation ( Li et al., 2022 ; Gong et al., 2023 ; Lou et al., 2024 ) . More recent scaling studies demonstrate that diffusion pretraining can be competitive with autoregressive (AR) approaches: LLaDA ( Nie et al., 2025 ) trains an 8B masked dLLM from scratch, and Dream 7B ( Ye et al., 2025 ) improves general capabilities, including mathematics, code, and planning. On the inference side, Fast-dLLM ( Wu et al., 2025 ) accelerates diffusion decoding by enabling block-wise approximate KV caching and confidence-aware parallel decoding. For reasoning, diffusion sampling can produce diverse chain-of-thought (CoT) trajectories, which can be aggregated using self-consistency-style methods ( Ye et al., 2024 ; Wang et al., 2023 ; Shao et al., 2025 ) . While LLaDA 2.0 ( Bie et al., 2025 ) demonstrated that discrete diffusion can be stably trained up to tens of billions of parameters, other recent works focus on hybrid architectures. Block Diffusion ( Arriola et al., 2025 ) alternates diffusion-style refinement with autoregressive decoding, while TiDAR ( Liu et al., 2025 ) unifies both autoregressive and diffusion generation within a single network. In contrast, we advocate for a decoupled pipeline: diffusion provides inexpensive, broad exploration, and a lightweight AR model performs step selection and final answer generation.

[19] h4: Speculative Decoding.

[20] p: Speculative decoding (and closely related speculative sampling) accelerates autoregressive (AR) generation via a draft-and-verify procedure: a lightweight draft model proposes multi-token continuations, and the large target AR model verifies them in parallel using rejection-style correction to ensure the accepted output matches the target distribution ( Leviathan et al., 2023 ; Chen et al., 2023 ) . Recent hybrid frameworks, including SpecDiff ( Christopher et al., 2025 ) , SpecDiff-2 ( Sandler et al., 2025 ) , DiffuSpec ( Li et al., 2025 ) , and DEER ( Cheng et al., 2025 ) , mitigate the token-level sequential drafting bottleneck by replacing the AR drafter with a discrete diffusion model. Alternatively, the autospeculation paradigm represented by Spiffy ( Agrawal et al., 2026 ) and SSD ( Gao et al., 2025 ) enables diffusion models to act as their own drafters. These approaches take advantage of the multi-step nature of the diffusion process by predicting unmasked token states multiple timesteps ahead. Then, the resulting state trajectories are verified in parallel, enforcing consistency with the model’s own generative distribution. Overall, these speculative decoding and autospeculation methods are designed to accelerate next-token generation by maximizing token acceptance between a drafter and a verifier, and thus focusing on token-level alignment and verification. In contrast, our method targets test-time reasoning quality and efficiency by using diffusion sampling for broad trajectory-level exploration, scoring intermediate reasoning steps with a PRM, and stitching high-quality steps into a compact evidence trace that conditions an AR solver to recompute the final answer, rather than verifying and accepting/rejecting drafted tokens.

[21] h4: Test-Time Reasoning.

[22] p: Large language models can improve their performance on complex tasks by leveraging additional compute at inference time. For example, chain-of-thought prompting ( Wei et al., 2022 ) elicits intermediate reasoning steps that substantially improve performance on multi-step problems, and self-consistency decoding ( Wang et al., 2023 ) generates multiple diverse chain-of-thought (CoT) solutions and selects the most frequent answer via majority vote, greatly improving reasoning accuracy. Related prompting approaches, such as least-to-most prompting ( Zhou et al., 2022 ) , explicitly decompose problems into simpler subproblems to improve generalization. More structured search strategies like Tree-of-Thought ( Yao et al., 2023a ) further expand the reasoning space by exploring a branching set of possible solution paths rather than a single linear chain. Complementary to sampling-based exploration, verifier-based methods generate many candidates and use a learned verifier to select the best solution, achieving strong gains on math reasoning ( Cobbe et al., 2021 ) . More interactive paradigms such as ReAct ( Yao et al., 2023b ) interleave reasoning with action/feedback at test time, enabling iterative correction but typically increasing inference cost. While effective, such test-time reasoning techniques incur substantial overhead ( Feng et al., 2025 ) . In this work, we instead pursue an efficient test-time exploration approach: by using a diffusion model to generate candidate reasoning trajectories in parallel, we obtain broad exploration with no latency overhead. In fact, through step-wise stitching across multiple trajectories we can use a much lower confidence score for sampling, thus significantly reducing attainable latency.

[23] h2: 3 Method

[24] figure: Figure 2 : Diffusion Stitching pipeline . We first use a diffusion model to efficiently explore diverse reasoning paths, then score each intermediate step with a PRM, and finally stitch the highest-quality steps into a single rationale that conditions an AR solver to recompute the final answer.

[25] p: Improved reasoning often scales with heavy test-time compute, making it impractical for low-latency applications. This issue stems from treating each reasoning trace as an all-or-nothing object, which both wastes useful partial progress and makes aggregation high-variance. In this section, we propose a framework that addresses this problem by reframing reasoning as a modular pipeline using both efficient search and robust step evaluation (see Figure 2 ). Our approach first decouples exploration from synthesis: we first generate a diverse pool of low-cost thoughts via a diffusion model ( Section 3.2 ), evaluate their utility at the step level using a process reward model ( Section 3.3 ), and finally employ a stitching mechanism ( Section 3.4 ) to recombine high-confidence steps into a coherent rationale that guides an AR solver to recompute the final answer ( Section 3.5 ).

[26] h3: 3.1 Preliminaries: Masked Diffusion Language Models.

[27] p: LLaDA ( Nie et al., 2025 ) produces an L L -token sequence via iterative refinement, progressively replacing mask tokens in an initially fully-masked template with predicted tokens, rather than generating tokens one-by-one left-to-right as in autoregressive models. Let 𝒱 \mathcal{V} be the vocabulary, M M denote the mask token, and initialize the input sequence x ( 0 ) = [ prompt , M , … , M ] ∈ ( 𝒱 ∪ { M } ) L x^{(0)}=[\text{prompt},M,\dots,M]\in(\mathcal{V}\cup\{M\})^{L} . For diffusion steps k = 1 , … , K k=1,\dots,K , the bidirectional mask predictor outputs logits ℓ i ( k ) ∈ ℝ | 𝒱 | \ell^{(k)}_{i}\in\mathbb{R}^{|\mathcal{V}|} for each masked position i i , which we convert to a sampling distribution with temperature τ > 0 \tau>0 :

[28] table: p i ( k ) = softmax ⁡ ( ℓ i ( k ) / τ ) , x ^ i ( k ) ∼ p i ( k ) . \displaystyle p^{(k)}_{i}=\mathrm{softmax}\!\left(\ell^{(k)}_{i}/\tau\right),\qquad\hat{x}^{(k)}_{i}\sim p^{(k)}_{i}. (1)

[29] p: We define a per-position confidence score as c i ( k ) = max j ⁡ p i , j ( k ) c^{(k)}_{i}=\max_{j}p^{(k)}_{i,j} . LLaDA then performs low-confidence remasking : after proposing x ^ i ( k ) \hat{x}^{(k)}_{i} for masked positions, it keeps high-confidence predictions fixed while remasking uncertain ones, e.g. remask all positions with c i ( k ) < γ c^{(k)}_{i}<\gamma (or equivalently, remask the lowest-confidence tokens to match a target mask budget), where γ ∈ [ 0 , 1 ] \gamma\in[0,1] is a tunable confidence threshold. Repeating this refine–(re)mask process until no masks remain yields the final completion. This iterative process is unlike autoregressive decoding, which commits to a left-to-right prefix.

[30] h3: 3.2 Reasoning Path Exploration.

[31] p: Masked diffusion language models are well suited to broad exploration: starting from a partially-masked sequence, they iteratively denoise tokens in parallel, rather than generating tokens in a strict chronological order. Given an input problem x x , we run N N independent diffusion generations to obtain diverse reasoning traces. Each trace n ∈ { 1 , … , N } n\in\{1,\dots,N\} is then deterministically segmented into human-readable steps:

[32] table: τ ( n ) = ( s 1 ( n ) , … , s T n ( n ) ) , s t ( n ) ∈ 𝒱 ∗ . \displaystyle\tau^{(n)}\;=\;\bigl(s^{(n)}_{1},\dots,s^{(n)}_{T_{n}}\bigr),\qquad s^{(n)}_{t}\in\mathcal{V}^{*}. (2)

[33] p: We segment each generated rationale into a sequence of steps using task-appropriate boundaries. For example, for the math problems, we split into sentence-level steps.

[34] h3: 3.3 Evaluating the quality of each reasoning step.

[35] p: Given the segmented reasoning traces { τ ( n ) } n = 1 N \{\tau^{(n)}\}_{n=1}^{N} , we assign a quality score to every step using an off-the-shelf process reward model (PRM) ( Zhang et al., 2025b ; Zeng et al., 2025 ) . For each trace n n and step index t t , the PRM outputs a scalar confidence:

[36] table: r t ( n ) = PRM ϕ ( x , s 1 : t ( n ) ) ∈ [ 0 , 1 ] , \displaystyle r^{(n)}_{t}\;=\;\mathrm{PRM}_{\phi}\!\bigl(x,\;s^{(n)}_{1:t}\bigr)\in[0,1], (3)

[37] p: where the score is conditioned on the problem x x and the partial solution history s ( n ) 1 : t s^{(n)}_{1:t} . This step-level view allows us to retain useful intermediate derivations even when a reasoning path later derails.

[38] h4: Single-pass scoring via marker tokens.

[39] p: In practice, we score all steps in a trace using one forward pass by inserting a special marker token ⟨ m ⟩ \langle m\rangle (e.g., <extra_0> ) after each step boundary and reading the model’s predicted probability of the marker:

[40] table: r t ( n ) = p ϕ ( ⟨ m ⟩ | x , s 1 : t ( n ) ) . \displaystyle r^{(n)}_{t}\;=\;p_{\phi}\!\left(\langle m\rangle\,\middle|\,x,\;s^{(n)}_{1:t}\right). (4)

[41] p: Collecting scores over all traces yields a global pool of scored steps,

[42] table: 𝒫 = { ( n , t , s t ( n ) , r t ( n ) ) : n ∈ [ N ] , t ∈ [ T n ] } , \displaystyle\mathcal{P}\;=\;\bigl\{(n,t,s^{(n)}_{t},r^{(n)}_{t})\;:\;n\in[N],\;t\in[T_{n}]\bigr\}, (5)

[43] p: which forms the candidate set for the stitching process in Section 3.4 .

[44] h3: 3.4 Stitching the reasoning steps together.

[45] p: From the global pool of scored steps in Equation 5 , we build a stitched evidence list E E by selecting reliable steps across all reasoning traces. We score each trace by the geometric mean of its step-level PRM scores. Let n ⋆ n^{\star} denote the trace with the highest geometric-mean score. We always keep the final step of this best trace as an answer anchor. Given a confidence threshold δ ∈ [ 0 , 1 ] \delta\in[0,1] , we retain all steps in 𝒫 \mathcal{P} with a PRM score at least δ \delta , and we also include every step from the best full trace (to serve as an anchor). We construct the stitched rationale as a sequence of ( step , confidence ) (\text{step},\text{confidence}) pairs, i.e., by prefixing each retained step with its score ( [c=0.93] ... ), which allows the downstream solver to condition jointly on the content and its confidence score (see Figure 5 ). To maintain coherence, we then concatenate selected steps in chronological order based on their original positions. This preserves local dependencies while still allowing complementary sub-derivations from different reasoning traces to co-exist in a single rationale. Finally, we utilize the resulting confidence-annotated evidence list E E to recompute the final answer ( Section 3.5 ).

[46] h3: 3.5 Recomputing the final answer.

[47] p: The stitched evidence list E E is not guaranteed to form a complete and perfectly consistent chain-of-thought: it may contain redundancy, small gaps, or occasional contradictions from mixing reasoning paths. Instead of directly returning the endpoint of any diffusion trace, we use a lightweight autoregressive (AR) solver to recompute the final answer.

[48] h4: Evidence-conditioned decoding.

[49] p: We construct a solver prompt by concatenating the problem x x with the confidence-annotated evidence list E E . We explicitly instruct the solver to treat these steps as evidence, prioritizing high-confidence entries while ignoring conflicts. We then obtain the final answer y ^ \hat{y} by maximizing the likelihood:

[50] table: y ^ = arg ⁡ max y ​ p ψ ​ ( y ∣ x , E ) , \hat{y}\;=\;\arg\max_{y}p_{\psi}(y\mid x,E),

[51] p: implemented via greedy or low-temperature decoding with a strict stopping rule (e.g., stop after producing a complete \boxed{...} answer) with ψ \psi denoting the parameters of the AR solver. In effect, this AR stage acts as a reconciliation step: it selects a consistent subset of evidence, fills in missing links, and produces a coherent final solution. In practice, we implement this via greedy or low-temperature decoding with a strict stopping rule.

[52] h3: 3.6 Extending to coding tasks.

[53] p: The same pipeline extends to code generation by redefining steps and using code-aware evaluators. We use different step definitions for MBPP and HumanEval: MBPP solutions are short and benefit from local code-line reuse, whereas HumanEval often requires more global planning, for which natural-language rationales are more robust. For MBPP, we treat each line in the code as a step. The diffusion model then proposes candidate code, a code PRM assigns a confidence score to each line, and we stitch high-confidence lines together. An autoregressive solver then generates the final program conditioned on this stitched evidence, correcting inconsistencies and filling in missing details. As shown in Figure 3 , this conditioning yields concise solutions with 3.21× fewer forward passes than the baseline. For HumanEval, we instead stitch a natural-language rationale and condition the solver on this reasoning before generating code, which avoids spending compute on re-generating the rationale and allows the solver to just generate the code implementation.

[54] figure: Figure 3 : Parallisable inference cost (gen length 512) . We report the number of parallelisable diffusion steps and the number of AR solver decoding steps for math and coding tasks.

[55] h2: 4 Experiments

[56] figure: Table 1: Evaluation Results: We evaluate the performance of Diffusion Stitching over several coding and math tasks. Baseline LLaDA and Dream numbers are taken from the TiDAR paper. The confidence-sampling variants were reproduced using γ = 0.9 \gamma=0.9 and 512 denoising steps, respectively. Our model and those reproduced were evaluated in a zero-shot setting. Coding Math Avg Model Arch Size HumanEval HumanEval+ MBPP MBPP+ GSM8K Minerva Math Qwen3 4B 57.32 50.61 67.00 80.69 77.48 47.10 63.37 Qwen3 8B 64.63 56.71 69.40 83.07 81.80 52.94 68.09 LLaDA 8B 32.32 27.44 40.80 51.85 70.96 27.30 41.78 ↰ \Lsh w/ conf sampling 8B 40.24 37.80 41.89 55.82 78.77 36.54 48.51 Dream 7B 54.88 49.39 56.80 74.60 77.18 39.60 58.74 ↰ \Lsh w/ conf sampling 7B 59.76 57.32 59.14 71.96 81.96 42.78 62.15 Block Diff 4B † 56.10 51.22 54.60 69.84 82.87 47.02 60.27 TiDAR (Trust AR) 8B ‡ 55.49 52.44 65.40 79.63 79.83 50.58 63.90 TiDAR (Trust Diff) 8B ‡ 57.93 55.49 65.40 80.95 80.44 51.64 65.31 Ours 8B 70.37 64.02 74.61 81.75 91.51 53.20 72.38

[57] figure: (a) MBPP (b) GSM8K (c) MATH500 Figure 4 : Pareto fronts of forward passes vs. accuracy on MBPP, GSM8K, and MATH500, showing that diffusion stitching bridges the gap between diffusion and AR models while enabling efficient test-time scaling for low-latency reasoning. All models are of the same 7-8B size, except for DeepSeek Coder which is 14B. We report our result for generation length 128, 256, and 512.

[58] h4: Implementation details.

[59] p: We distribute the batch of N N independent diffusion generations over G G GPUs, assigning [ N / G N/G ] traces per device and accumulating step-level PRM scores locally. Following this local evaluation, we perform a single all_gather operation to synchronize the scores and content, thereby forming the global pool of candidate steps. Since the trajectories are generated independently, our method scales linearly with the available compute, requiring synchronization only for the final aggregation.

[60] h4: Evaluation Benchmarks.

[61] p: We evaluate diffusion stitching on a mix of mathematical reasoning and program synthesis tasks under a strictly zero-shot setting. For math, we report accuracy on GSM8K-CoT ( Cobbe et al., 2021 ) , Math500 (a 500-problem subset of MATH ( Lightman et al., 2024 ) ), and Countdown 1 1 1 huggingface.co/datasets/Jiayi-Pan/Countdown-Tasks-3to4 (target-number arithmetic) (see Supplementary). For code, we report pass@1 on HumanEval ( Chen et al., 2021 ) , HumanEval+ ( Liu et al., 2023 ) , MBPP ( Austin et al., 2021 ) , and MBPP+ ( Liu et al., 2023 ) . Unless stated otherwise, we use a fixed generation budget ( N = 4 N{=}4 ) with generation lengths in the range 256–512, and we follow each benchmark’s standard answer normalization and scoring protocol (strict/exact match for math; unit-test execution for code). Finally, we evaluate all models in the zero-shot setting.

[62] h4: Models used.

[63] p: Unless stated otherwise, we use LLaDA as the masked diffusion backbone for generating candidate reasoning trajectories. We score intermediate steps with an off-the-shelf process reward model, and produce the final answer using an autoregressive solver conditioned on the stitched rationale.

[64] p: Process reward models (PRMs).

[65] p: Qwen-Math-PRM-7B ( Zhang et al., 2025b ) : step-level scoring for mathematical reasoning traces.

[66] p: AceCoderRM ( Zeng et al., 2025 ) : reward model used to score each step in a block of code.

[67] p: Autoregressive (AR) solvers.

[68] p: Qwen2.5-Math-Instruct ( Yang et al., 2024 ) : instruction tuned model for mathematical reasoning tasks.

[69] p: Qwen2.5-Coder-7B ( Hui et al., 2024 ) : code generation, code reasoning, and code fixing.

[70] h3: 4.1 Main Results

[71] h4: Accuracy on reasoning benchmarks.

[72] p: Table 1 summarizes overall task performance. Stitching yields large gains over vanilla diffusion decoding by converting diverse but noisy reasoning paths into a higher-quality evidence set: In the 8B setting, we outperform the LLaDA baseline decoded with a high confidence threshold ( γ = 0.9 \gamma=0.9 ), despite using a much lower threshold ( γ = 0.7 \gamma=0.7 ), by an average of 23.9% average points (72.38 vs. 48.51), with especially strong jumps on HumanEval ( +30.1 ), HumanEval+ ( +26.2 ), and MBPP ( +32.7 ). We also outperform recent hybrid diffusion–AR systems, exceeding TiDAR (Trust Diff) by +7.1 . Notably, our training-free pipeline is competitive with strong AR baselines: compared to Qwen3-8B, we are +4.3 points higher on average, driven by sizable gains on GSM8K ( +9.7 ) and consistent improvements on HumanEval ( +5.7 ) and HumanEval+ ( +7.3 ) (with MBPP+ roughly matched). These results highlight that step-level reuse can deliver state-of-the-art accuracy among diffusion-based approaches while remaining latency-friendly: exploration is cheap and parallel in diffusion, and the AR solver is invoked only once to produce the final answer.

[73] h4: Accuracy vs. inference steps.

[74] p: To study efficiency, Figure 4 reports Pareto frontiers as accuracy versus inference steps, where we measure inference steps as the number of model forward evaluations required to answer a problem (this includes the forward passes of the diffusion model, PRM, and AR Solver). Across MBPP, GSM8K, and Math500 , diffusion stitching achieves a consistently better trade-off than both diffusion-only baselines (which are efficient but less accurate) and AR baselines (which are accurate but require many sequential decoding steps), demonstrating an effective test-time scaling regime for low-latency reasoning. Moreover, we achieve much higher reasoning performance with far fewer steps than prior unified architectures (TiDAR), suggesting that a natural decoupling of diffusion-based exploration and AR-based verification is an important design choice for efficient reasoning.

[75] h3: 4.2 Ablation Study

[76] figure: Figure 5 : Qualitative examples of step stitching . Each column shows a stitched evidence trace built from multiple diffusion trajectories (colors denote retained high-scoring steps). A lightweight AR solver then conditions on this trace to output only the final answer. Column 1 illustrates resolving disagreements; column 3 shows using confidence as to guide the final prediction.

[77] h4: Effect of Aggregation Strategy and the AR Solver.

[78] p: We ablate both how we aggregate diffusion traces and when an AR solver is needed in Table 2 . Concretely, we compare three setups. Without a solver , we either (i) decode a single trajectory ( Baseline ) or (ii) apply self-consistency by majority voting over final answers from multiple generations ( Majority Vote ; Wang et al. 2023 ). With a solver but without stitching , we condition the AR model on either (iii) the concatenation of all sampled CoTs ( All CoT ) or (iv) the single highest-quality CoT ( Best CoT ), selected by the geometric mean of PRM step scores. With a solver and stitching , we provide the solver with (v) our confidence-filtered stitched rationale ( Stitching ), (vi) an improved variant that keeps all above-threshold steps and also the best CoT as an anchor ( Stitching + Best CoT ).

[79] p: Overall, we observe a clear progression: diverse exploration provides a stronger set of candidate trajectories, adding an AR solver improves coherence via re-computation, and confidence-based stitching best leverages the full set of sampled traces. These results are consistent across both GSM8K and Math500 , where we see that the full pipeline obtains an average of 14.7 % 14.7\% improvement over the strong LLaDA baseline decoded with a high confidence ( γ = 0.9 \gamma=0.9 ).

[80] figure: Table 2: Ablation of stitching strategies . We compare selecting the best rollout, majority voting over final answers, using all steps, and our confidence-filtered step stitching, showing that selective stitching yields the best accuracy. Using γ = 0.7 \gamma=0.7 and τ = 1.4 \tau=1.4 and τ = 0.8 \tau=0.8 for GSM8K and Math500 respectively. Setting GSM8K MATH500 Baseline LLaDA 78.8 37.6 without Solver or PRM Majority vote ( Wang et al., 2023 ) 85.1 42.0 with Solver and PRM All CoT 86.6 46.0 Best CoT 90.1 49.2 with Solver, PRM, and Stitching Above confidence 90.4 52.0 Best CoT and above confidence 91.5 54.2

[81] h4: Low-latency inference via parallel generations.

[82] p: Our framework naturally supports low-latency test-time scaling because reasoning traces are independent and can be executed in parallel across devices. Figure 1 plots accuracy versus end-to-end latency on Math500 and shows that diffusion stitching achieves a better trade-off than both strong AR baselines, which achieve high accuracy but incur high sequential decoding latency, and vanilla diffusion baselines, which are fast but less accurate. By combining cheap parallel exploration with PRM-based step selection and a lightweight recomputation stage, stitching closes the gap to AR reasoning while remaining in the low-latency regime.

[83] h4: Controlling the diversity of reasoning paths.

[84] p: The benefits of stitching depend not only on how many reasoning traces are sampled but also on how diverse those traces are (see Figure 6 ). If the trajectories are highly similar, additional samples add little new information. We control diversity using the temperature parameter for sampling, and evaluate the resulting trade-offs on GSM8K and Math500 . We find that a moderate-to-high diversity is important for strong performance: too low temperatures leads to poor exploration and diversity, while too high degrades the quality of each trace.

[85] figure: (a) GSM8K (b) Math500 Figure 6 : Ablation on sampling temperature . Accuracy (%) improves with higher temperature by promoting diverse reasoning paths. Although strong performance is achieved across a range of values, the optimal temperature is dataset-specific.

[86] figure: Table 3: Ablation on the number of generations . Accuracy (%) increases with more reasoning traces, and strong performance is already achieved with a modest number of samples. When these generations run in parallel, increasing the number of traces does not increase latency. The default number of traces used in the main experiments is highlighted in blue . GSM8K MATH500 Avg 1 82.4 46.0 64.2 2 88.1 49.2 68.7 4 91.5 54.2 72.9 6 91.4 54.3 72.9 8 91.3 55.0 73.2

[87] h4: Scaling with the number of generations.

[88] p: We next study how performance scales with the number of diffusion generations N N on GSM8K and Math500 (see Table 3 ). Increasing N N improves performance initially, as additional trajectories provide more opportunities to recover correct intermediate steps and reduce the impact of any single noisy path. This trend is most pronounced on Math500 , where each trace often shares re-usable sub-derivations but diverge in later steps; stitching allows us to preserve those shared correct components while avoiding late-stage derailment.

[89] h4: Diffusion sampling confidence.

[90] p: A key advantage of our framework is that it remains accurate even when the diffusion sampler is run with a low sampling confidence , producing highly noisy and low quality trajectories. Our pipeline is explicitly designed to tolerate this noise: the PRM scores each step and filter out those of low quality. The stitched rationale can also contain gaps, yet the downstream AR solver can still recover the final solution.

[91] p: Table 4 shows that accuracy is stable across a wide range of sampling confidences, while the required inference steps change substantially. On GSM8K, reducing the sampling confidence from 0.8 0.8 to 0.6 0.6 decreases the average step budget from 111.3 111.3 to 86.8 86.8 (a 22.0 % 22.0\% reduction) with little loss in accuracy (from 91.7 91.7 to 90.5 90.5 ). On Math500 , the same reduction lowers steps from 158.5 158.5 to 119.8 119.8 (a 24.4 % 24.4\% reduction), again with comparable accuracy ( 54.4 54.4 vs. 52.0 52.0 ). These results indicate that we can operate the diffusion model with a relatively low confidence to substantially reduce latency.

[92] figure: Table 4: Ablation on the confidence threshold . We report the average steps for the longest diffusion trajectory of each question + the number of solver steps required to regenerate the final answer. We use τ = 1.4 \tau=1.4 and τ = 0.8 \tau=0.8 for GSM8K and Math500 respectively with the confidence value used in main experiments highlighted in blue . GSM8K MATH500 Confidence Acc #steps Acc #steps 0.4 87.6 76.6 46.8 103.4 0.5 89.1 79.8 49.2 108.7 0.6 90.5 86.8 52.0 119.8 0.7 91.5 96.9 54.2 135.5 0.8 91.7 111.3 54.4 158.5

[93] h4: Other diffusion backbones.

[94] p: Our stitching framework is model-agnostic: it only assumes (i) a generator that can produce candidate reasoning trajectories (here, masked diffusion LMs) and (ii) a PRM that can score intermediate steps. To test generality, we apply our framework to several other diffusion backbones.

[95] p: Table 5 shows consistent gains across diffusion models. For LLaDA-1.5 , stitching raises Math500 accuracy from 38.0 38.0 to 53.8 53.8 while reducing inference steps from 163 163 to 134 134 , since it allows a lower confidence threshold γ \gamma to be used. For Dream , stitching similarly increases accuracy on both GSM8K ( 82.6 → 85.4 82.6\rightarrow 85.4 ) and Math500 ( 48.2 → 53.2 48.2\rightarrow 53.2 ), with essentially unchanged step counts (the diffusion model is already run at a fixed-length budget in this setting). Finally, on LLaDA-2.0 , stitching provides a substantial boost on Math500 ( 44.6 → 61.4 44.6\rightarrow 61.4 ) while keeping compute comparable ( 256 → 267 256\rightarrow 267 steps), and preserves strong performance on GSM8K. This small increase in steps comes from the PRM and AR solvers.

[96] figure: Table 5: dLLM/AR model ablation . AR models achieve strong accuracy but require many decoding steps, while our method boosts dLLM performance while also reducing the inference costs by enabling the use of a lower confidence for sampling. Accuracy (%) and the number of parallelizable steps performed. GSM8K MATH500 Model Acc #steps Acc #steps Qwen-Math-Instruct 94.3 440 79.6 1504 Phi-4 92.4 295 76.8 791 LLaDA-1.5 84.0 101 38.0 163 ↰ \Lsh w/ stitching 90.8 87 53.8 134 Dream 82.6 512 48.2 512 ↰ \Lsh w/ stitching 85.4 521 53.2 523 LLaDA 2.0 88.0 256 44.6 256 ↰ \Lsh w/ stitching 89.6 266 61.4 267

[97] h2: 5 Limitations

[98] p: If the candidate pool is not sufficiently diverse some of the traces share the same mistakes. The solver cannot recover missing intermediate evidence and can only reuse what is already present.

[99] h2: 6 Conclusion

[100] p: We introduced a training-free reasoning framework that combines inexpensive diffusion-based exploration with step-level verification and selective aggregation. By scoring intermediate steps and stitching those with high confidence across independent rollouts, we turn noisy trajectories into a reusable pool of reliable evidence, which conditions a final autoregressive solver to produce the answer. Across both maths and coding benchmarks, stitching substantially strengthens accuracy–latency trade-offs: it improves accuracy by up to +30.6% over vanilla diffusion decoding and remains competitive with strong autoregressive baselines (e.g., +4.3% on average), while reducing sequential solver compute to a single AR solve and yielding up to 3.2× fewer forward passes in latency-critical settings. Overall, these results show that aggregating steps rather than only final answers is an effective approach for scalable reasoning.

[101] h2: Impact Statement

[102] p: This paper presents work whose goal is to advance the field of machine learning. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.

[103] h2: References

[104] h2: Appendix A Supplementary Material

[105] p: This supplementary provides implementation and evaluation details that are omitted from the main paper due to space. We first present pseudo-code for the complete stitching procedure in algorithmic form (Appendix B ), including the exact step-pool construction, confidence filtering, and evidence formatting provided to the AR solver. We then report all hyperparameters and decoding settings needed to reproduce the reported results (Appendix C ). The next section (Appendix D and E ) provide some qualitative stitching examples and failure cases. After this, we include additional comparisons against an RL fine-tuning baseline (Appendices F ) and a recent speculative decoding baseline (Appendices G ). Finally, we then list the prompts used for (i) diffusion generation, (ii) PRM step scoring, and (iii) solver recomputation (Appendix H ).

[106] h2: Appendix B Full Stitching Algorithm

[107] p: Algorithm provides the pseudocode of our pipeline.

[108] figure: PyTorch-style pseudocode for diffusion stitching ⬇ 1: # p_theta : diffusion generator (exploration) 2: # PRM_phi : process reward model (step scoring) 3: # p_psi : AR solver (final recomputation) 4: # N : num generations (traces) 5: # delta : PRM stitch threshold (step selection) 6: # geom_mean(r) = (prod_t r[t])^(1/max(len(r),1)) 7: 8: for batch in loader : 9: x , _ = batch # one problem x (batch size 1) 10: S , R = [], [] # steps and PRM scores per trace 11: 12: for n in range ( N ): # generations can be dispatched to different GPUs 13: y_n = diffusion_generate ( p_theta , x ) 14: s_n = extract_steps ( y_n ) # s_n = [s^{(n)}_1, ..., s^{(n)}_{T_n}] 15: r_n = PRM_phi ( x , s_n ) # r_n = [r^{(n)}_1, ..., r^{(n)}_{T_n}] in [0,1] 16: S . append ( s_n ); R . append ( r_n ) 17: 18: n_star = argmax_n geom_mean ( R [ n ]) # best trace by geometric mean PRM score 19: 20: E = [] # stitched evidence list 21: for n in range ( N ): 22: for t in range ( len ( S [ n ])): 23: keep = ( R [ n ][ t ] >= delta ) or ( n == n_star ) # keep all best-trace steps as anchor 24: if keep : 25: E . append (( t , R [ n ][ t ], S [ n ][ t ])) # (step index, score, step text) 26: 27: E = sort ( E , key =( t , - score )) # chronological; break ties by higher score 28: prompt = build_prompt ( x , E ) # format as: [c=score] step 29: y_hat = ar_generate ( p_psi , prompt ) # stop after complete \boxed{...}

[109] h2: Appendix C Hyperparameters

[110] p: We report the exact models and score metrics used for each evaluation benchmark in table 6 .

[111] figure: Table 6: Metrics used for each evaluation task . All tasks were evaluated zero-shot, using 4 generations, and with a generation length of 512. Strict match is implemented using the math-verify library 3 3 3 github.com/huggingface/Math-Verify and exact match uses string matching equality. Task Category Task Name PRM Solver Score Metric Coding HumanEval Qwen2.5-Math-PRM-7B QWEN2.5-CODER-7B Pass@1 HumanEval+ Qwen2.5-Math-PRM-7B QWEN2.5-CODER-7B Pass@1 MBPP ACECODERRM QWEN2.5-CODER-7B Pass@1 MBPP+ ACECODERRM QWEN2.5-CODER-7B Pass@1 Math GSM8K-CoT Qwen2.5-Math-PRM-7B Qwen2.5-Math-Instruct strict-match MATH500 Qwen2.5-Math-PRM-7B Qwen2.5-Math-Instruct strict-match Minerva Math Qwen2.5-Math-PRM-7B Qwen2.5-Math-Instruct strict-match Puzzle Countdown Qwen2.5-Math-PRM-7B Qwen2.5-Math-Instruct exact-match

[112] h2: Appendix D More stitching examples

[113] p: Figure 7 shows representative cases where stitching succeeds. On the left, different diffusion trajectories contain complementary correct steps but disagree on the final answer; the solver resolves the split decisions into a correct final answer. On the far right, a less common case, the diffusion generations produce only low-confidence predictions, yet the solver over-rules them by recomputing from the stitched intermediate evidence.

[114] figure: Figure 7 : Qualitative examples . Left: resolving split decisions and right: over-ruling uniformly low-confidence predictions.

[115] h2: Appendix E Failure cases

[116] p: To understand the limits of stitching, we include representative cases where it provides the incorrect final answer (Figure 8 ). These failures arise when the sampled diffusion trajectories lack a correct sub-derivation e.g., many traces share the same early error due to insufficient diversity, which results in the the stitched pool containing no reliable evidence to recompute a correct solution. Stitching can also fail when the PRM misranks steps, either assigning low scores to a crucial but correct intermediate step (so it is filtered out) or being over-confident in a fluent but incorrect late step, which then dominates the stitched evidence and steers the solver toward the wrong answer.

[117] figure: Figure 8 : Representative failure cases for stitching . Each column shows the stitched evidence list and the final autoregressive solver prediction. Failures occur when the sampled trajectories contain no correct sub-derivation (left, third), when a key correct step is scored too low by the PRM and is omitted (second), or when the PRM is over-confident in an incorrect late step (or anchor trace), causing the evidence set to be dominated by a wrong conclusion (right).

[118] h2: Appendix F Comparisons with RL

[119] p: We also compare against d1 ( Zhao et al., 2025 ) , an RL fine-tuning approach that optimizes a model directly for performance on specific evaluation tasks. Unlike our training-free inference-time pipeline, d1 is a fine-tuning approach for specialist models using task specific reward losses. We compare in Table 7 , where we can see that our generalist stitching framework is much more effective across various generation lengths, and evaluations.

[120] figure: Table 7: Model performance on GSM8K, MATH500, and Countdown Benchmarks: All models are evaluated zero-shot with generation lengths of 256–512. Diffusion stitching is training-free, whereas d1 requires task-specific RL fine-tuning. GSM8K (0-shot) MATH500 (0-shot) Countdown (0-shot) Model / Seq Len 256 512 256 512 256 512 d1-LLaDA 81.1 82.1 38.6 40.2 32.0 42.2 Ours 89.4 91.5 49.4 54.2 37.5 45.7

[121] h2: Appendix G Comparisons with Speculative Decoding

[122] p: We compare against a recent speculative decoding baseline (RSD ( Liao et al., 2025 ) ), which follows a draft-and-verify paradigm: a lightweight drafter proposes multi-tokens and a larger verifier selectively accepts them based on a scalar quality signal, falling back to the verifier to regenerate rejected segments. In contrast, diffusion stitching is not a token-acceptance scheme. We first use a diffusion model to explore multiple complete reasoning traces in parallel, then select and recombine high-quality intermediate steps into a stitched evidence list, and finally invoke an autoregressive solver once to recompute the final answer conditioned on this evidence.

[123] p: The results are shown in table 8 , where RSD attains only a small increase in accuracy on GSM8K, but requires substantially more forward passes. RSD uses 325 drafter steps and 75 verifier steps, whereas our pipeline uses 86 total steps (21.5% of RSD).

[124] figure: Table 8: Comparison to speculative decoding on GMS8K. RSD steps are reported as drafter steps / verifier steps . For ours, the steps are reported as diffusion steps / solver steps . GSM8K Model Acc #steps RSD ( Liao et al., 2025 ) 94.6 325/75 Ours 91.5 80/6

[125] h2: Appendix H Prompts

[126] p: We use three prompt templates for the math reasoning benchmarks:

[127] p: We use the following prompt templates for the coding benchmarks:

[128] h2: Instructions for reporting errors

[129] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[130] p: Tip: You can select the relevant text first, to include it in your report.

[131] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[132] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
