# 2601.08884v1 — decisive reopening core

Primary exact HTML: https://arxiv.org/html/2601.08884v1 . 定点恢复线索来自Jan15作者，不继承其准入/评分/日期结论；本日实际读以下必要段。只重开先前generic-GEPA应用关闭的08884，不扩发现范围。未运行code/实验。

## II-A/B/C: canonical-feedback and generated-DM handoff

II-A GEPA for OpenACC Pragma Generation 
 Our approach leverages the GEPA framework within the DSPy library to evolve simple initial prompts (see Appendix, List.  11 and List.  12 ) to generate optimized prompts that enable the lower-parameter and smaller “nano” models to generate syntactically and semantically correct OpenACC pragma for a given C/C++ program. 
 In each iteration, the “student” model prompted with a simple initial prompt and an example program with a single <DM_PRAGMA> or <LP_PRAGMA> tag to indicate the what kind of pragma it needs to generate. The quality of the predicted pragma is determined by semantically comparing it with the “gold” pragma written by us for that particular tagged location in the program. The pragma are also normalized to a canonical map representation to compare them semantically and identify clause-level and parameter-level mismatch between the predicted pragma and the “gold” pragma. The core of our optimization strategy lies in the structured granular feedback report detailing clause- and parameter-specific mismatches. This feedback, along with the semantic similarity score, is passed on to the GEPA optimizer for the reflection model. The reflection model uses this feedback to mutate the prompt towards better performance in the next iteration, i.e., getting the model to predict pragma that are semantically more similar to the corresponding “gold” pragma for a particular tagged location in the program. 
 II-B Semantic Similarity Scoring 
 At the heart of GEPA there is the automatic comparison between predicted pragma and “gold” pragma (ground truth). Clearly, evaluating the accuracy of generated OpenACC pragmas via direct textual comparison is insufficient. Standard string-matching metrics such as BLEU [ 12 ] or Exact Match are order-sensitive and do not account for the commutativity of clauses (e.g., copy(A) copyin(B, C) ≡ copyin(B, C) copy(A) \texttt{copy(A) copyin(B, C)}\equiv\texttt{copyin(B, C) copy(A)} ) and the order-independence of variable lists within a clause. To address this, we define a normalization function N : Σ ∗ → ℳ N:\Sigma^{*}\to\mathcal{M} that maps a raw pragma string to a structured canonical representation ℳ \mathcal{M} . 
 The pragma normalization process involves three stages. First, the primary directive (e.g., parallel loop , kernels , data , etc.) is extracted from the raw pragma string. Any mismatch between the predicted and ground truth directive directly results in a penalty. Second, the remaining pragma string is split into its constituent clauses using a robust splitting algorithm that respects nested parentheses to handle complex expressions (e.g., array slicing A[0:N] ). Third, for each clause c c , the argument list P c = p 1 , p 2 , … , p n P_{c}={p_{1},p_{2},...,p_{n}} is sorted lexicographically and the whitespace amongst the clause arguments is normalized. For the reduction clause, special handling is applied by parsing the operator and variable list into a set of tuples { ( o ​ p , v ​ a ​ r 1 ) , ( o ​ p , v ​ a ​ r 2 ) , … } \{(op,var_{1}),(op,var_{2}),...\} , ensuring that reduction(+:a, b) and reduction(+:b,a) map to the same canonical representation. For example, as shown in Fig.  1 , the different pragma input strings map to the same canonical representation. 
 ℳ = { \displaystyle\mathcal{M}=\{ 
 “parallel loop” , \displaystyle\text{``parallel loop''}, 
 private → ( “i” ) , \displaystyle\text{private}\to(\text{``i''}), 
 reduction → ( “+ : sum” , “+ : temp” ) } \displaystyle\text{reduction}\to(\text{``+ : sum''},\ \text{``+ : temp''})\} 
 Input (Gold): 
 #pragma acc parallel loop reduction(+:sum, temp) private(i) 
 Input (Predicted): 
 #pragma acc parallel loop private(i) reduction(+:temp, sum) 
 Fig. 1: Comparison of Gold and Predicted OpenACC Pragma. 
 To measure the semantic similarity between predicted and ground truth pragma, the normalized predicted pragma map P P is compared against the gold standard pragma map G G . Clause-level F1 and parameter-level F1 scores are calculated by treating the clause names (the keys of the maps) as sets K G K_{G} and K P K_{P} . Let I = K G ∩ K P I=K_{G}\cap K_{P} , represent the intersection of the clause sets. 
 Precision clause = | I | | K P | , Recall clause = | I | | K G | \mathrm{Precision}_{\textit{clause}}=\frac{\lvert I\rvert}{\lvert K_{P}\rvert},\qquad\mathrm{Recall}_{\textit{clause}}=\frac{\lvert I\rvert}{\lvert K_{G}\rvert} 
 F1 clause = 2 ⋅ Precision clause ⋅ Recall clause Precision clause + Recall clause \mathrm{F1}_{\textit{clause}}=2\cdot\frac{\mathrm{Precision}_{\textit{clause}}\cdot\mathrm{Recall}_{\textit{clause}}}{\mathrm{Precision}_{\textit{clause}}+\mathrm{Recall}_{\textit{clause}}} 
 For the subset of clauses within the intersection I I , we evaluate parameter accuracy. Let v G , c v_{G,c} and v P , c v_{P,c} be the multi-sets of normalized parameters for clause c c in the gold and predicted pragma maps, respectively. The total matches (Hits) are calculated across all shared clauses as: 
 Hits = ∑ c ∈ I | v G , c ∩ v P , c | \mathrm{Hits}=\sum_{c\in I}\left\lvert v_{G,c}\cap v_{P,c}\right\rvert 
 Precision param = Hits ∑ c ∈ I | v P , c | , Recall param = Hits ∑ c ∈ I | v G , c | \mathrm{Precision}_{\textit{param}}=\frac{\mathrm{Hits}}{\sum_{c\in I}\left\lvert v_{P,c}\right\rvert},\qquad\mathrm{Recall}_{\textit{param}}=\frac{\mathrm{Hits}}{\sum_{c\in I}\left\lvert v_{G,c}\right\rvert} 
 The final score, S total \mathrm{S}_{\textit{total}} , is a weighted sum that prioritizes structural correctness while heavily penalizing incorrect data movement or privatization variables. 
 S total = 0.6 ⋅ F1 clause + 0.4 ⋅ F1 param \mathrm{S}_{\textit{total}}=0.6\cdot\mathrm{F1}_{\textit{clause}}+0.4\cdot\mathrm{F1}_{\textit{param}} 
 Scoring Examples: 
The following cases illustrate the metric’s behavior across different error types: 
 Perfect Semantic Match (Fig.  2 ) : Predicted and gold pragma differ only in clause order. 
 F1 clause = 1.0 , F1 param = 1.0 ⇒ S total = 1.0 \mathrm{F1}_{\textit{clause}}=1.0,\mathrm{F1}_{\textit{param}}=1.0\Rightarrow\mathrm{S}_{\textit{total}}=1.0 
 Correct Structure, Incorrect Variable (Fig.  3 ): The clause sets match ( F1 clause = 1.0 \mathrm{F1}_{\textit{clause}}=1.0 ), but the parameter j j is missing. Precision param = 1.0 \mathrm{Precision}_{\textit{param}}=1.0 , Recall param = 0.5 ⇒ F1 param ≈ 0.66 \mathrm{Recall}_{\textit{param}}=0.5\Rightarrow\mathrm{F1}_{\textit{param}}\approx 0.66 . Total score: 
 S total = 0.6 ⋅ ( 1.0 ) + 0.4 ⋅ ( 0.66 ) = 0.86 \mathrm{S}_{\textit{total}}=0.6\cdot(1.0)+0.4\cdot(0.66)=0.86 
 Structural Mismatch, Incorrect Primary Directive (Fig.  4 ) : A mismatch in the primary directive triggers significant penalty due to structural divergence from gold standard, resulting in F1 clause ≈ 0.5 \mathrm{F1}_{\textit{clause}}\approx 0.5 . 
 Gold: 
 #pragma acc data copyin(A[0:N]) copyout(B[0:N]) 
 Predicted: 
 #pragma acc data copyout(B[0:N]) copyin(A[0:N]) 
 Fig. 2: Example of Perfect Semantic Matching. 
 Gold: 
 #pragma acc parallel loop private(i, j) 
 Predicted: 
 #pragma acc parallel loop private(i) 
 Fig. 3: Example of Correct Structure, but Incorrect Variables. 
 Gold: 
 #pragma acc kernels copy(A) 
 Predicted: 
 #pragma acc parallel loop copy(A) 
 Fig. 4: Example of Incorrect Primary Directive. 
 II-C Inference 
 Inference is conducted in two stages: 
 • 
 Stage 1: Data Management (DM) Pragma Synthesis: The model is prompted with a data management prompt to generate data management pragma for the <DM_PRAGMA> sites in the serial PolyBench program. The synthesized DM pragmas from Stage 1 are re-inserted into the source, forming the input context for the second stage. 
 • 
 Stage 2: Loop Parallelization (LP) Pragma Synthesis: The model is prompted with a loop parallelization prompt to generate compute pragma at the <LP_PRAGMA> sites. 
 By performing loop-parallelization inference in the presence of the model-generated data management pragma rather than “gold” ground truth pragma, the evaluation accurately reflects real-world downstream usage. This approach ensures that the generated compute pragmas are contextually aware of the memory orchestration established in the preceding stage. 
 TABLE I: Feedback Analysis from GEPA Script 
 Error Category 
 Prompt Hint 
 Corrective Action 
 Missing collapse clause 
 The model failed to recognize that the nested loops are tightly coupled and can be collapsed. Ensure the prompt emphasizes checking for ’tightly nested loops’ (loops with no intervening code) and apply ’collapse(N)’ to maximize parallelism. 
 Add collapse({inner}) clause. 
 Unnecessary collapse clause 
 The prompt must explicitly forbid ’collapse’ if there are intervening statements or complex index dependencies between loops. 
 Remove collapse({inner}) clause. 
 Missing reduction clause 
 The prompt should define a ’reduction’ as a scalar accumulated across the loop (e.g. sum+=, max=) that is not re-initialized inside. Do not reduce arrays. 
 Add reduction({op}:{vars_txt}) clause. 
 Unnecessary, extra reduction clause 
 The prompt must clarify that reduction is ONLY for scalars that are truly accumulated across the loop, and not reinitialized per outer iterations, and not for arrays or private vars. Use the correct operator for the accumulated scalar. Do not reduce arrays. 
 Remove reduction({op}:{vars_txt}) clause. 
 Missing private clause 
 The prompt should explicitly state that scalars assigned within the loop body must be marked ’private’ unless they are reductions to prevent data races. 
 Add private({inner}) clause. 
 Extra or incorrect private clause 
 The prompt must state that loop iterators are implicitly private and read-only shared variables do not need privatization. 
 Remove private({inner}) clause. 
 Missing present clause 
 The prompt must instruct the model to use ’present’ for arrays that are already resident on the GPU (e.g., passed from a calling function or managed by an enclosing data region). 
 Add present({inner}) clause. 
 Unnecessary present clause 
 The prompt should not use ’present’ if the data is not guaranteed to be on the device. Use data movement clauses (copy/copyin) if transfer is needed. 
 Remove present({inner}) clause. 
 Missing copyin clause 
 The prompt must enforce ’copyin’ for arrays that are Read-Only inside the region and require initialization from the host. 
 Add copyin({inner}) clause. 
 Unnecessary copyin clause 
 Do not use ’copyin’ if the variable is written to (use copy/copyout) or not used at all. 
 Remove copyin({inner}) clause. 
 Missing copyout clause 
 The prompt must enforce ’copyout’ for arrays that are Write-Only on the device and whose results are needed back on the host. 
 Add copyout({inner}) clause. 
 Unnecessary copyout clause 
 Do not use ’copyout’ if the variable needs initial values from the host (use copy) or is not used. 
 Remove copyout({inner}) clause. 
 Missing copy clause 
 The prompt must enforce ’copy’ for arrays that are Read-Write (accessed and modified) inside the region. 
 Add copy({inner}) clause. 
 Unnecessary copy clause 
 Use more specific clauses if possible: ’copyin’ for Read-Only, ’copyout’ for Write-Only. Use ’copy’ only for true Read-Write dependencies. 
 Remove copy({inner}) clause. 
 Missing create clause 
 The prompt must use ’create’ for temporary arrays used only on the device (scratchpad) that do not require host values. 
 Add create({inner}) clause. 
 Unnecessary create clause 
 Do not use ’create’ if the variable needs initialization from the host (use copyin/copy). 
 Remove create({inner}) clause. 
 collapse clause parameter mismatch 
 The prompt should instruct the model to list all relevant variables for the clause and verify against the variable declarations. 
 Use ’collapse(N)’ as seen in GOLD). 
 reduction clause parameter mismatch 
 The prompt should instruct the model to list all relevant variables for the clause and verify against the variable declarations. Use reduction clause for the scalar that is truly accumulated across the parallelized dimension and not reinitialized per outer iteration. Do not reduce arrays. Do not duplicate variables in private() if they appear in reduction(). 
 Use reduction({gop}:{gvars}) (as seen in GOLD), instead of reduction({pop}:{pvars}) (currently in PRED) 
 private clause parameter mismatch 
 The prompt should instruct the model to list all relevant variables for the clause and verify against the variable declarations. Use reduction clause for the scalar that is truly accumulated across the parallelized dimension and not reinitialized per outer iteration. Do not reduce arrays. Do not duplicate variables in private() if they appear in reduction(). List only scalars written inside the loop and not covered by reduction(); loop indices are implicit private. 
 Use private({g_inner}) (as seen in GOLD), instead of private({p_inner}) (currently in PRED) 
 

## III / IV-A: evaluation population

III Evaluation 
 We evaluated the compilation success rate and speedup over CPU baselines on the PolyBench suite of benchmarks  [ 3 ] with OpenACC pragma generated by the models using the initial simple prompt as the baseline and the GEPA-optimized prompt (see Appendix  B Figures  11 and   12 ).
We selected the PolyBench/C 4.2.1  [ 3 ] suite as our primary evaluation vehicle because it provides a standardized, diverse set of kernels representing fundamental computational patterns in scientific computing, such as stencil operations, linear algebra, and data mining. Although PolyBench consists of relatively small kernels, it serves as a rigorous baseline to isolate the ability of an LLM to correctly identify data dependencies and manage memory movement without the confounding complexity of large-scale inter-procedural analysis. By demonstrating success on these ”building blocks” of HPC, we establish a performance ceiling for prompt-optimized directive generation before extending the methodology to more complex scientific mini-apps.
 Hardware Setup: All GPU execution tests and performance measurements were conducted on a workstation equipped with an NVIDIA GeForce RTX 4070 GPU (12GB GDDR6X VRAM, Ada Lovelace architecture). The host system featured an AMD Ryzen 9 7900X 12-Core Processor with 32GB of system memory. We utilized the NVIDIA HPC SDK (nvc 24.5) for compilation, targeting the cc89 compute capability with the -acc -fast optimization flags. 
 IV Results 
 IV-A Prompt Optimization Delivers a Robustness Jump 
 GEPA-optimized prompts enhance the models’ ability to generate syntactically and semantically correct OpenACC pragma, significantly improving the fraction of benchmarks that compiled successfully, relative to the fraction of benchmarks with pragma generated using the initial prompt with the same models. Across 120 model–benchmark evaluations (30 benchmarks from the PolyBench suite and four model variants: GPT-4.1, GPT-4.1 Nano, GPT-5, and GPT-5 Nano, best-of-5 runs per setting), aggregate compilability rose from 78.3 % 78.3\% ( 94 / 120 94/120 ) using the initial prompt to 95.8 % 95.8\% ( 115 / 120 115/120 ) with the GEPA-optimized prompt (Table  II ). The use of the GEPA-optimized prompt converted 21 previously failing cases into successful GPU compilations and achieved zero regressions i.e. no benchmark that compiled under the initial prompt failed under the optimized prompt. 
 As shown in Table  III the performance gains are consistent across all model sizes and are particularly pronounced for smaller, lower-capacity models. For “nano”–scaled models, the optimized prompt significantly bridged the compilation reliability gap. The compilation success rate for GPT-4.1 Nano improved from 66.7 % 66.7\% ( 20 / 30 20/30 ) to 93.3 % 93.3\% ( 28 / 30 28/30 ), and for GPT-5 Nano from 86.7 % 86.7\% ( 26 / 30 26/30 ) to 100 % 100\% ( 30 / 30 30/30 ). A similar trend was observed for larger models, where failures were reduced to a smaller subset of highly complex benchmarks. The compilation success rates for GPT-4.1 improved from 83.3 % 83.3\% ( 25 / 30 25/30 ) to 96.7 % 96.7\% ( 29 / 30 29/30 ), and for GPT-5 from 76.7 % 76.7\% ( 23 / 30 23/30 ) to 93.3 % 93.3\% ( 28 / 30 28/30 ). Overall, using the optimized prompt reduces syntactic/semantic errors in OpenACC pragmas even when generated using the smaller model. This stabilization of offloading patterns is critical for automated HPC pipelines, where compilability serves as a primary metric for practical utility. 
 TABLE II: Overall impact of optimized prompt on robustness in terms of Compilability and Speedup. 
 Prompt 
 Compilable 
 Compilability Rate 
 Speedup > 1 >1 count 
 Initial 
 94 
 78.3% 
 67 
 Optimized (ours) 
 115 
 95.8% 
 81 
 Despite the improvements made by using optimized prompts, a small subset of benchmarks remains intractable. As shown in Table  V these failures are mainly concentrated in specific kernels. The gemver benchmarks failed to compile under both initial and optimized prompts for GPT-4.1 and GPT-4.1 Nano models. Furthermore, fdtd-apml was unsuccessful for GPT-4.1 Nano in both prompt configurations. For GPT-5 (Fig.  10 ), the remaining failures are floyd-warshall and jacobi-2d-imper , which produce no valid GPU result under either prompt (Table  V ). 
 TABLE III: Per-model compilability and speedup summary. 
 Model 
 Prompt 
 Compilability 
 (out of 30) 
 # Benchmarks 
 [-0.2em] with Speedup > 1 >1 
 GPT-4.1 
 Initial 
 83.3% (25) 
 16 
 GPT-4.1 
 Optimized 
 96.7% (29) 
 22 
 GPT-4.1 Nano 
 Initial 
 66.7% (20) 
 14 
 GPT-4.1 Nano 
 Optimized 
 93.3% (28) 
 21 
 GPT-5 Nano 
 Initial 
 86.7% (26) 
 21 
 GPT-5 Nano 
 Optimized 
 100.0% (30) 
 23 
 GPT-5 
 Initial 
 76.7% (23) 
 16 
 GPT-5 
 Optimized 
 93.3% (28) 
 15 
 

## Table IV / IV-C: common-compiled counterexample

TABLE IV: Speedup on the Common Compiled Subset of Benchmarks. 
 Model 
 Mean Speedup 
 (Initial Prompt ) 
 Mean Speedup 
 (Optimized Prompt) 
 GPT-4.1 
 2.401 
 3.669 
 GPT-4.1 Nano 
 4.308 
 4.606 
 GPT-5 Nano 
 4.143 
 3.828 
 GPT-5 
 2.820 
 2.542 
 IV-C Prompt Optimization Preserves Speedups While Improving Compilation Reliability 
 For GPT-5 (Fig.  10 ), peak speedups remain high under both prompts, e.g., symm : 78.82 × 78.82\times (initial) versus 73.42 × 73.42\times (optimized), and 3mm : 64.8 × 64.8\times (initial) versus 58.83 × 58.83\times (optimized). Similar behavior holds for other models on dense linear-algebra kernels (e.g. symm ). Prompt optimization can be slightly conservative on some already-compiling kernels. For example, GPT-4.1 Nano’s symm drops from 79.55 × 79.55\times (initial) to 62.81 × 62.81\times (optimized) despite both compiling, illustrating that the optimized prompt sometimes trades aggressiveness for safer offload patterns. This modest conservatism on a subset of kernels is outweighed by the substantial increase in compile-and-run coverage and the net increase in accelerated cases across the suite. 
 On the subset of benchmarks that compile under both prompts, the performance impact of the optimized prompt is model-dependent. The optimized prompt improves the mean speedup for GPT-4.1-class models while being close to neutral, and occasionally conservative, for GPT-5-class models. For GPT-4.1, the mean speedup increased from 2.40 × 2.40\times to 3.67 × 3.67\times on the common compiled set, and for GPT-4.1 Nano from 4.31 × 4.31\times to 4.61 × 4.61\times . In contrast, GPT-5 Nano shows a modest reduction ( 4.14 × → 3.83 × 4.14\times\rightarrow 3.83\times ) on the common compiled set, consistent with safer offload choices. The optimized prompt again primarily improves robustness while yielding comparable or modestly reduced speedups on already-compiling kernels (Table  IV . 
 We observe that GEPA reflective prompt optimization is a practical and effective mechanism for writing prompts that substantially improve the correctness of OpenACC pragma, especially for smaller, “nano”–scale models while preserving strong speedups on dense kernels and increasing the end-to-end throughput of automated GPU offloading. In a practical HPC developer setting, dramatically higher reliability with largely preserved peak speedups on compute-dense kernels is typically preferable to fragile high-variance behavior. 
 

## VI: limits

VI Limitations 
 While our results demonstrate that prompt optimization significantly improves compilability and often matches expert-level speedups, this study has several limitations. First, the evaluation is limited to the PolyBench suite, which lacks the inter-procedural data dependencies and multi-file structures common in large-scale scientific applications. Second, we observed that GEPA-optimized prompts can occasionally be overly conservative, sacrificing peak performance (as seen in the symm kernel) to ensure memory safety and compilation success. This ”safety-first” bias is a byproduct of our current multi-objective Pareto optimization.
