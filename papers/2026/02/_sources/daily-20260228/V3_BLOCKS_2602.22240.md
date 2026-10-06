[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: From Prompts to Performance: Evaluating LLMs for Task-based Parallel Code Generation

[3] h6: Abstract

[4] p: llm show strong abilities in code generation, but their skill in creating efficient parallel programs is less studied. This paper explores how llm generate task-based parallel code from three kinds of input prompts: natural language problem descriptions, sequential reference implementations, and parallel pseudo code. We focus on three programming frameworks: OpenMP Tasking, C ++ standard parallelism, and the asynchronous many-task runtime HPX. Each framework offers different levels of abstraction and control for task execution. We evaluate llm -generated solutions for correctness and scalability. Our results reveal both strengths and weaknesses of llm with regard to problem complexity and framework. Finally, we discuss what these findings mean for future llm -assisted development in high-performance and scientific computing.

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: The rapid evolution of llm has transformed software engineering by enabling automated code generation. Yet their ability to produce correct and performant parallel programs remains largely unexplored. Parallel code generation requires reasoning about data dependencies, workload decomposition, and synchronization. Recent empirical studies show that current models perform substantially worse on parallel than on serial workloads, often producing non-scalable or inefficient implementations [ 1 ] .

[8] p: Asynchronous task-based parallel programming provides a useful framework to examine these limitations, as it imposes more difficult parallelization problems compared to conventional fork-join approaches. We focus on OpenMP Tasking, C ++ standard parallelism, and the asynchronous many-task runtime HPX, which span a wide range of abstraction levels and execution models. We also investigate the impact of prompting input modality on model performance, as prior work shows that zero-shot parallelization remains largely unreliable and prone to concurrency errors [ 2 ] . Specifically, we base our different input prompts on natural language, pseudo-code, and sequential implementations.

[9] p: Furthermore, we evaluate how different classes of llm generate asynchronous task-based code and analyze how prompt complexity and abstraction influence correctness and performance. The remainder of this work is structured as follows. Section 2 surveys recent work on code generation capabilities in the HPC context. Section 3 then describes the evaluation methodology. The results are presented in Section 4 and followed by the conclusion in Section 5 .

[10] h2: 2 Related Work

[11] p: The application of llm to automatic code generation has rapidly evolved from general-purpose programming assistance to domain-specific high-performance computing (HPC) code. Recent advances in foundation models such as ChatGPT [ 3 ] , DeepSeek [ 4 ] , and open-source alternatives including LLaMA-2 [ 5 ] have demonstrated strong capabilities in generating syntactically correct and semantically meaningful code across a wide range of programming languages [ 6 , 7 , 8 , 9 ] . These capabilities have sparked growing interest in using llm to improve developer productivity in HPC applications, where parallel programming remains complex and error-prone.

[12] p: Recent machine learning–based approaches have attempted to bridge the gap between parallelism detection and code synthesis. AutoParLLM [ 10 ] represents an early attempt to combine graph neural network-based parallelism detection with llm -guided code generation, highlighting the potential of hybrid approaches but also underscoring the challenges of correctness and generalization. However, the most significant recent progress in parallel code generation has come from llm -based methods. Early evaluations of OpenAI Codex showed that llm can generate HPC kernels using OpenMP, OpenACC, CUDA, and MPI constructs directly from natural language prompts or partial code, with varying success depending on training data availability [ 11 ] . Subsequent work expanded these evaluations to compare proprietary and open-source models for HPC kernel generation, demonstrating that while both models can generate valid parallel code, their performance and correctness vary significantly across programming models and hardware targets [ 12 ] . Both studies highlighted persistent challenges, including missing synchronization, incorrect data scoping, and performance portability issues. HPC-Coder [ 13 ] investigated llm -based modeling of parallel programs, reporting mixed success in generating correct OpenMP pragmas and MPI calls, underscoring the difficulty of synthesizing semantically correct parallel code. Godoy et al. [ 14 ] extended earlier evaluations by assessing llm -generated parallel kernels across C ++ , Fortran, Python, and Julia, demonstrating that llm can assist in auto-parallelization but still require expert validation to ensure correctness and performance.

[13] p: While existing work focuses on code generation for different programming languages, GPU kernels, and fork-join parallelization, asynchronous task-based code generation remains largely unexplored. Our work fills this existing research gap by evaluating task-based code generation using multiple frameworks across several llm not only regarding compilation and correctness but also parallel scaling. Although crucial, parallel strong and weak scaling was not investigated in previous work.

[14] h2: 3 Methodology

[15] p: We evaluate the ability of llm to generate task-based parallel code using a set of benchmark problems that vary in algorithmic structure, dependency complexity, and sensitivity to compute and memory bandwidth limits. The selected benchmarks span embarrassingly parallel workloads, divide-and-conquer algorithms, regular compute kernels, and iterative methods with global synchronization barriers:

[16] p: Stochastic Approximation of π \pi , representing independent task execution with minimal synchronization.

[17] p: Merge Sort , exhibiting recursive task creation and explicit dependency constraints.

[18] p: Matrix-Matrix Multiplication , a dense linear algebra kernel with high arithmetic intensity and structured data access.

[19] p: Conjugate Gradient Method , an iterative solver involving sparse computations, reductions, and strict iteration ordering.

[20] p: Together, these benchmarks stress different aspects of task-based parallelization, including task granularity, dependency inference, and synchronization placement. For each benchmark, we generate parallel implementations from three prompt modalities of progressively increasing specificity. These modalities assess how input structure influences the model’s ability to infer parallelism:

[21] p: Problem Description , providing only a function signature, a high-level natural language specification, and the target parallel framework.

[22] p: Sequential Code , supplying a complete sequential C ++ implementation to be parallelized.

[23] p: Parallel Pseudo Code , augmenting the description with a structured parallel algorithm outline.

[24] p: This progression reflects common llm usage scenarios, from algorithm design assistance to automated refactoring of existing code. Each problem–prompt combination is evaluated across three llm to enable comparative analysis:

[25] p: ChatGPT-5

[26] p: Qwen-Coder 3 (30B) 1 1 1 https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct

[27] p: Gemini-3

[28] p: Our model selection covers different parameter scales, training objectives, and availability models, including both open-source and proprietary systems.

[29] p: We evaluate llm -generated task-based parallel code using three parallel programming frameworks that represent different abstraction levels and execution models:

[30] p: OpenMP Tasking is a widely used directive-based framework for shared-memory parallelism. Its explicit task creation and synchronization directives make it a natural baseline for evaluating an llm ’s ability to reason about dependencies and task granularity.

[31] p: C ++ Standard Parallelism provides high-level, library-based parallel abstractions such as parallel algorithms and execution policies. It allows us to assess whether llm can exploit declarative parallelism.

[32] p: HPX is a fully asynchronous, task-based runtime leveraging futures and dataflow semantics. We include HPX to evaluate llm performance on fine-grained, dependency-driven parallelism.

[33] p: Together, these frameworks cover a spectrum from directive-based to runtime-driven parallelism, enabling a comparative analysis of how llm adapt to different task-based programming models. For every combination of benchmark problem, prompt modality, llm , and parallelization framework, we generate multiple code snippets. Generated implementations are evaluated along three axes. Correctness is assessed using problem-specific validation and reference outputs. Complexity is quantified using lines of code, comment density, and control-flow patterns in the generated programs. Scalability is evaluated by varying available parallel resources and analyzing speedup behavior.

[34] p: This methodology isolates the impact of problem complexity, prompt modality, and model choice on the quality of llm -generated task-based parallel code.

[35] h3: 3.1 Evaluation Metrics

[36] p: We present pass@k to analyze the correctness of the produced code, scc for complexity evaluation, and PCGQS for benchmarking generated parallel code.

[37] h4: Correctness

[38] p: The pass@k metric is widely used for evaluating llm and their generated code [ 15 ] . It quantifies the probability that at least one out of k k generated samples is correct. The computation of pass@k is given by Equation 1 :

[39] table: pass@k = 1 − ( n − c k ) ( n k ) \text{pass@k}=1-\frac{\binom{n-c}{k}}{\binom{n}{k}} (1)

[40] p: where n n denotes the total number of generated samples and c c the number of correct ones. To assess the quality of the generated code, we introduce a set of levels that characterize the difficulty of correcting code errors. We do not explicitly characterize by the type of error, i.e., compilation, runtime, or general algorithmic error. However, typically compilation errors are easier to correct than runtime or algorithmic errors. By categorizing the effort required to correct the code for successful use, this framework enables a more comprehensive evaluation of programs generated by llm . The set comprises the following levels:

[41] table: C ⁡ ( c ) = { 1 , No Fix – Fully correct, no modifications required , 0.75 , Easy – Minor adjustments are sufficient to achieve correctness , 0.5 , Medium – Moderate debugging, code modifications are required , 0.25 , Hard – Significant intervention is necessary to fix the code , 0 , Infeasible – The code cannot be feasibly corrected . C(c)=\begin{cases}1,&\text{No Fix \textendash Fully correct, no modifications required},\\ 0.75,&\text{Easy \textendash Minor adjustments are sufficient to achieve correctness},\\ 0.5,&\text{Medium \textendash Moderate debugging, code modifications are required},\\ 0.25,&\text{Hard \textendash Significant intervention is necessary to fix the code},\\ 0,&\text{Infeasible \textendash The code cannot be feasibly corrected}.\end{cases} (2)

[42] h4: Complexity

[43] p: Beyond executability and performance of the code, we also assess the intrinsic properties of the generated code examples. We employ the tool scc 2 2 2 https://github.com/boyter/scc to quantify the number of effective lines of code as well as the proportion of comment lines. In addition, scc provides a complexity metric approximating the cyclomatic complexity [ 16 ] , which can be used as an indicator of the expected maintenance effort associated with the code.

[44] h4: Scaling

[45] p: To evaluate the ability of llm to generate efficient parallel code, we define the Parallel Code Generation Quality Score (PCGQS) . The metric combines functional correctness with empirical scaling behavior. For a generated implementation c c , the PCGQS is defined as:

[46] table: PCGQS ⁡ ( c ) = 1 2 ​ C ​ ( c ) + 1 2 ​ S ​ ( c ) , \mathrm{PCGQS}(c)=\frac{1}{2}C(c)+\frac{1}{2}S(c), (3)

[47] p: where C ⁡ ( c ) C(c) denotes functional correctness as defined in Equation 2 and S ⁡ ( c ) S(c) captures parallel scalability.

[48] p: Scaling behavior is evaluated using both strong and weak scaling experiments as defined in Equation 4 and Equation 5 , respectively. T 1 T_{1} is the single-core runtime, T p T_{p} is the runtime using p p processing elements, and 𝒫 \mathcal{P} is the set of evaluated core counts. We combine strong and weak scaling into a single score as in Equation 6

[49] table: S strong ​ ( c ) \displaystyle S_{\text{strong}}(c) = 1 | 𝒫 | ​ ∑ p ∈ 𝒫 T 1 p ⋅ T p \displaystyle=\frac{1}{|\mathcal{P}|}\sum_{p\in\mathcal{P}}\frac{T_{1}}{p\cdot T_{p}} (4) S weak ​ ( c ) \displaystyle S_{\text{weak}}(c) = 1 | 𝒫 | ​ ∑ p ∈ 𝒫 T 1 T p \displaystyle=\frac{1}{|\mathcal{P}|}\sum_{p\in\mathcal{P}}\frac{T_{1}}{T_{p}} (5) S ⁡ ( c ) \displaystyle S(c) = 1 2 ​ S strong ​ ( c ) + 1 2 ​ S weak ​ ( c ) \displaystyle=\frac{1}{2}S_{\text{strong}}(c)+\frac{1}{2}S_{\text{weak}}(c) (6)

[50] h2: 4 Results

[51] p: To ensure experimental reproducibility, all experiments are conducted within a fixed testing environment. The experimental setup consisted of a system equipped with a dual-socket AMD EPYC 7742 CPU. For the scaling experiments, we evaluate the code on up to 128 threads. We bind the thread to CPU cores to eliminate potential unseen effects introduced by multi-threading. Based on a preliminary task-scaling analysis, the number of tasks is fixed at 128 for all experiments. Regarding the key software specifications, we use GCC version 13.3.0 13.3.0 , OpenMP version 4.5, and HPX version 1.11.0 1.11.0 . We begin with an assessment of code correctness, followed by an analysis of complexity. Finally, we examine the scaling behavior.

[52] h3: 4.1 Correctness

[53] p: We begin by analyzing the out-of-the-box performance of the three llm . For each llm , we compute the pass@1 metric across all remaining experimental groups. In this way, Figure 1 provides an initial, yet meaningful, overview of model performance. Even in these first results, substantial differences between the models are apparent. ChatGPT exhibits the strongest out-of-the-box performance in terms of generating correct code. Google’s Gemini ranks second, while the open-source model Qwen-Coder trails at a considerable distance. As shown in Figure 1(a) , OpenMP performs robustly across all models. C ++ standard parallelism achieves near-perfect results for ChatGPT and Gemini but performs very poorly for Qwen-Coder. HPX, by contrast, starts at a low pass@1 rate and degrades rapidly across all models. Figure 1(b) reveals a similar overall pattern with respect to the different prompt formulations. No statistically significant performance differences can be attributed to the prompt type. Prompts containing parallel pseudocode yield only marginal improvements. When examining the individual benchmark problems in Figure 1(c) , several noteworthy observations can be made. Although the parallel approximation of π \pi might intuitively appear simpler than parallel mergesort, both ChatGPT and Gemini generate more reliable code for mergesort. This is likely due to mergesort being a canonical programming exercise commonly encountered in introductory computer science courses, resulting in a large number of readily available implementations. Finally, the cg ( cg ) benchmark proves sufficiently challenging that the pass@1 metric drops markedly in comparison to the generally better-performing matrix–matrix multiplication benchmark.

[54] figure: (a) Grouped by framework. (b) Grouped by prompt type. (c) Grouped by problem. Figure 1 : Pass@1 metric for the respective llm without any correction.

[55] p: In Figure 2 , we analyze the performance improvements obtained when limited human corrections are permitted. The required modifications to obtain correct code are categorized into the five fix levels introduced in Section 3.1 . As a baseline, Figure 2(a) reports the pass@1 metric without any human intervention. This plot is identical to Figure 1(c) . Allowing only easy fixes already leads to a noticeable increase in the proportion of functioning code, as shown in Figure 2(b) . Minor corrections are sufficient to resolve a substantial fraction of failures across all models and benchmark problems. When medium-level fixes are permitted, the pass@1 metric reaches 100% for all models on several benchmarks. Notably, Qwen-Coder surpasses Gemini in this setting by achieving perfect results on both matrix-matrix multiplication and the approximation of π \pi . In contrast, mergesort, which exhibited the highest pass@1 rate without correction, falls behind matrix-matrix multiplication and p ​ i pi approximation at the medium fix level. With hard fixes, a pass@1 rate close to 100% is achieved for nearly all model-benchmark combinations. The only notable exception is the cg benchmark, which continues to show significantly lower pass@1 values for Qwen-Coder. In the following, we describe the concrete code modifications applied and justify their assignment to the respective fix categories.

[56] figure: (a) No fix (b) Easy (c) Medium (d) Hard Figure 2 : Pass@1 metric for the level of fixes, such that the program is correct and runs

[57] p: When it comes to the type of errors, the most common header-related errors include missing headers, outdated headers, or the use of non-existent headers. We categorize them as easy fixes. For HPX and C ++ standard parallelism, lambda expressions frequently exhibit incorrect capture clauses. These are medium fixes. A recurring error class, specific to generated HPX-Code, consists of outdated or incorrect namespaces, such as the use of hpx::parallel::for_loop instead of hpx::experimental::for_loop . Among genuine coding errors, incorrect handling of futures in HPX is particularly prevalent, most often caused by misplaced or missing .get() calls. More severe errors arise from incorrect sharing of arrays across parallel regions, which frequently leads to segmentation faults or silent data corruption. We additionally observe failures when executing the generated code on odd core counts, specifically for 24, 48, and 96 cores. If the code fails in any of the scaling experiments and the required fix is infeasible, we classify the corresponding output as non-executable.

[58] h3: 4.2 Complexity

[59] p: Table 1 presents a comparison of the influence of different llm , programming frameworks, and prompting strategies on the structure and complexity of the generated code. The number of lines of code stays constant for all categories. Notable differences are observed in the extent of code documentation: Gemini-generated code contains a higher density of comments, whereas ChatGPT produces the fewest comments. Furthermore, the level of abstraction in the prompt is directly correlated with the complexity of the resulting code. Prompts that integrate pseudo code provide a clear structure, facilitating code generation. In contrast, prompts that provide a sequential implementation encourage the model to adhere closely to that structure, with parallel constructs added around it. This approach results in increased structural complexity in the generated code.

[60] figure: Category #Lines #Code #Comments Complexity LLM ChatGPT 67.25 51.27 4.66 8.65 Gemini 75.97 51.07 12.80 9.06 Qwen 71.89 50.78 8.63 9.66 Framework OpenMP 70.11 51.14 8.16 9.06 Standard C ++ 70.93 50.26 8.71 10.26 HPX 74.12 51.75 9.25 7.99 Prompt Level Normal 73.46 50.43 10.35 9.01 Sequential 73.86 52.70 8.86 10.23 Pseudo 67.69 49.97 6.87 8.04 Table 1 : Comparison of generated code with regards to length and complexity.

[61] h3: 4.3 Scaling

[62] p: We next analyze the scaling behavior of the generated code using the strong and weak scaling definitions given in Equations 5 and 4 . For that, we fixed all errors, including the ones categorized as hard. Non-executable code is included as zero scaling.

[63] p: The resulting scaling performance is summarized in Figure 3 . Several noteworthy observations emerge from this analysis. As expected, the approximation of π \pi and matrix-matrix multiplication demonstrate consistently superior scaling behavior compared to mergesort and the cg algorithm. This difference arises because both the π \pi approximation and matrix-matrix multiplication exhibit regular memory access patterns. They also require minimal synchronization between parallel tasks. In contrast, mergesort and cg involve irregular control flow, recursive or iterative dependencies, and frequent reductions or synchronization points. These characteristics limit the achievable speedup as the number of cores increases. While the code generated by ChatGPT and Gemini exhibits very similar scaling trends and generally maintains performance across increasing core counts, Qwen-Coder’s implementations scale considerably worse. This poor scaling is particularly evident in the approximation of π \pi , which in theory should achieve near-linear speedup with increasing cores due to its inherently parallel structure. A major factor behind this limitation is that Qwen-Coder frequently implements the HPX variants using a single global random number generator. Consequently, all concurrent tasks, including up to 128 simultaneous threads in our experiments, must access the same generator for random values.

[64] figure: (a) Strong scaling (b) Weak scaling Figure 3 : Scaling of the generated code grouped by benchmark problem.

[65] p: When we categorize the results by the parallelization framework rather than by the benchmark problem, we can identify the best combinations of framework and model. The data in Figure 4 indicates that C ++ standard parallelism consistently achieves the highest weak scaling efficiency across all models. In contrast, OpenMP delivers the worst efficiency. Generated OpenMP code often confuses task-based parallelism with classic loop-based parallelism, for example, by mixing single or parallel regions with parallel for constructs incorrectly.

[66] p: While we see larger discrepancies between the frameworks for weak scaling, the strong scaling performance is very similar across all frameworks. Only code generated by Qwen-Coder achieves slightly lower efficiency. The results suggest that C ++ standard parallelism is the most robust choice for code generated by the evaluated llm , while HPX can be competitive if the model correctly handles framework-specific details. Finally,

[67] p: Last but not least, we use the PCGQS-Score from Equation 3 to evaluate the tested llm . Table 2 shows the combined score over all experiments, frameworks, and prompt levels. ChatGPT demonstrates the strongest overall performance, whereas the open-source model Qwen exhibits substantial difficulties in terms of response correctness, which markedly reduced its combined score.

[68] figure: (a) Strong scaling (b) Weak scaling Figure 4 : Scaling of the generated code grouped by framework.

[69] figure: ChatGPT Gemini Qwen PCGQS-Score 0.7425 0.7008 0.5702 Table 2 : PCGQS-Score for the evaluated llm .

[70] h2: 5 Conclusion and Outlook

[71] p: In this work, we systematically evaluated the ability of llm to generate task-based parallel code across multiple benchmarks with varying algorithmic structure and dependency complexity. Our results show that llm can reliably handle embarrassingly parallel problems and simple task graphs, indicating a solid grasp of basic parallel abstraction. For more complex patterns, such as iterative algorithms with intrinsic synchronization, the models frequently produce suboptimal or incorrect task dependencies. These shortcomings manifest as missing synchronization or latent race conditions, despite syntactically correct code. The proposed evaluation metrics, including the PCGQS, help distinguish models beyond functional correctness by capturing structural parallelism and scalability potential.

[72] p: Regarding future work, we plan to extend the benchmark suite toward larger, more irregular, and multi-stage parallel applications. Further improvements may be achieved through refined prompting, explicit dependency representations, and tool-assisted generation workflows. Together, these directions aim to improve both the reliability and practical usefulness of llm for asynchronous task-based parallel programming. Lastly, recent advances in agentic AI have led to substantial improvements in code generation performance, needing systematic investigation in the context of asynchronous task-based parallelization frameworks.

[73] h3: AI Use Disclosure

[74] p: Generative AI tools, including Grammarly [ 17 ] , DeepL [ 18 ] , Gemini [ 19 ] , and ChatGPT [ 20 ] , were employed to enhance the clarity, grammar, and overall coherence of the manuscript. All technical content, data analyses, and research findings were conceived and developed independently by the authors. AI-assisted outputs were carefully reviewed, verified, and edited by the authors to ensure factual accuracy, interpretive rigor, and scholarly integrity. The final manuscript reflects the authors’ original intellectual contributions and analytical work.

[75] h2: References

[76] h2: Instructions for reporting errors

[77] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[78] p: Tip: You can select the relevant text first, to include it in your report.

[79] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[80] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
