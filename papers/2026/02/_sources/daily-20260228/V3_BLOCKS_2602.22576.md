[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training

[3] h6: Abstract

[4] p: Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge, yet traditional single-round retrieval struggles with complex multi-step reasoning. Agentic RAG addresses this by enabling LLMs to dynamically decide when and what to retrieve, but current RL-based training methods suffer from sparse outcome rewards that discard intermediate signals and low sample efficiency where failed samples contribute nothing. We propose Search-P1 , a framework that introduces path-centric reward shaping for agentic RAG training, comprising two key components: (1) Path-Centric Reward , which evaluates the structural quality of reasoning trajectories through order-agnostic step coverage and soft scoring that extracts learning signals even from failed samples, and (2) Dual-Track Path Scoring with offline-generated reference planners that assesses paths from both self-consistency and reference-alignment perspectives. Experiments on multiple QA benchmarks demonstrate that Search-P1 achieves significant improvements over Search-R1 and other strong baselines, with an average accuracy gain of 7.7 points.

[5] figure: Figure 1: Performance comparison of Search-P1 against baselines on QA benchmarks. Our method achieves the highest average accuracy across all datasets on both (a) Qwen2.5-7B and (b) Qwen2.5-3B models.

[6] h2: 1 Introduction

[7] p: Large Language Models (LLMs) have demonstrated strong reasoning capabilities Zhong et al. (2023) ; Xia et al. (2025) ; Hu et al. (2025) , but their static knowledge often leads to hallucinations on knowledge-intensive queries. Retrieval-Augmented Generation (RAG) Lewis et al. (2020) addresses this by incorporating external knowledge, yet single-round retrieval is insufficient for complex multi-step reasoning—a common need in industrial applications such as advertising guidance, where answering a question often requires synthesizing information across multiple knowledge domains.

[8] p: Agentic RAG extends traditional RAG by enabling LLMs to dynamically invoke search and iteratively refine answers. Recent methods like Search-R1 apply RL with outcome-based rewards, but this approach has three limitations: (1) sparse rewards that ignore intermediate reasoning quality, (2) low sample efficiency where partially correct trajectories receive zero reward, and (3) slow convergence due to weak training signals when most samples share similar binary rewards.

[9] p: We propose Search-P1 , a framework introducing path-centric reward shaping for agentic RAG training that addresses all three limitations. Instead of evaluating only final answers, our reward design comprises: (1) dual-track path scoring that provides dense intermediate signals by evaluating reasoning trajectories from both self-consistency and reference-alignment perspectives, directly alleviating reward sparsity; and (2) soft outcome scoring that assigns partial credit to incorrect trajectories, converting zero-reward samples into useful training signals to improve sample efficiency. Together, the denser reward landscape accelerates convergence by providing more informative gradients throughout training. Experiments on public QA benchmarks and an internal advertising dataset (AD-QA) show Search-P1 outperforms existing methods with an average accuracy gain of 7.7 points, while also transferring effectively to enterprise knowledge base systems. Our contributions:

[10] p: We propose dual-track path scoring that evaluates trajectories from self-consistency and reference-alignment perspectives with order-agnostic matching.

[11] p: We design a path-centric reward shaping framework that extracts learning signals even from failed trajectories via path-level reward.

[12] p: Extensive experiments on public benchmarks and an industrial dataset demonstrate consistent improvements across models and settings.

[13] h2: 2 Related Work

[14] h5: Prompt-Based Agentic RAG.

[15] p: Initial efforts leverage prompts to guide LLMs through multi-step retrieval Singh et al. (2025) ; Li et al. (2025a) . These approaches interleave reasoning with retrieval actions Yao et al. (2023) ; Trivedi et al. (2023) or enhance reasoning through sophisticated retrieval strategies Li et al. (2025b) ; Wang et al. (2025) ; Guan et al. (2025) . However, prompt-based methods depend heavily on the base model’s instruction-following ability.

[16] h5: RL-Based Agentic RAG.

[17] p: Recent work applies reinforcement learning to train adaptive search agents Zhang et al. (2025a) ; Jin et al. (2025) . Follow-up methods incorporate auxiliary signals to stabilize training Song et al. (2025a) ; Chen et al. (2025) ; Huang et al. (2025) or improve search efficiency Sha et al. (2025) ; Song et al. (2025b) ; Wu et al. (2025b) . Some work explores process rewards for RAG Sun et al. (2025) ; Wu et al. (2025a) ; Zhang et al. (2025b) , but still relies primarily on binary outcome feedback. Our work proposes path-centric reward shaping offering denser training signals.

[18] h2: 3 Methodology

[19] figure: Figure 2: Overview of Search-P1 framework. Our approach introduces path-centric reward shaping for agentic RAG training, comprising: (1) Dual-Track Path Scoring that evaluates trajectories from both self-consistency and reference-alignment perspectives, and (2) Soft Outcome Scoring that extracts training signals even from incorrect answers.

[20] p: We first formalize the problem setting (§ 3.1 ), then describe the path-centric reward framework including dual-track scoring and soft outcome scoring (§ 3.2 ). Figure 2 provides an overview.

[21] h3: 3.1 Problem Formulation

[22] p: We consider an agentic RAG system where a language model π θ \pi_{\theta} generates a reasoning trajectory 𝒯 \mathcal{T} in response to a question q q . In standard agentic RAG frameworks, the trajectory consists of interleaved reasoning and action steps:

[23] table: 𝒯 = ( r 1 , a 1 , o 1 , … , r n , a n , o n , r final , a ^ ) \mathcal{T}=(r_{1},a_{1},o_{1},\ldots,r_{n},a_{n},o_{n},r_{\text{final}},\hat{a}) (1)

[24] p: where r i r_{i} denotes reasoning, a i a_{i} denotes a search action, o i o_{i} is the observation (search results), and a ^ \hat{a} is the final answer.

[25] p: We make the implicit planning in r 1 r_{1} explicit by restructuring the trajectory as:

[26] table: 𝒯 = ( p , r 1 , a 1 , o 1 , … , r n , a n , o n , r final , a ^ ) \mathcal{T}=(p,r_{1},a_{1},o_{1},\ldots,r_{n},a_{n},o_{n},r_{\text{final}},\hat{a}) (2)

[27] p: where p p is an explicit planner that outlines the reasoning strategy. This serves two purposes: (1) providing a self-declared plan against which execution can be evaluated, and (2) making the intended reasoning structure observable for path-centric evaluation.

[28] p: Standard GRPO assigns binary rewards based on answer correctness:

[29] table: R outcome = 𝟙 ​ [ match ​ ( a ^ , a ∗ ) ] R_{\text{outcome}}=\mathbb{1}[\text{match}(\hat{a},a^{*})] (3)

[30] p: where a ∗ a^{*} is the ground-truth answer. This formulation ignores the quality of the reasoning path and suffers from the limitations discussed in § 1 .

[31] h3: 3.2 Path-Centric Reward

[32] p: We propose a path-centric reward that evaluates trajectory quality rather than solely relying on final answer correctness, addressing the three limitations of outcome-based methods. The complete reward function is:

[33] table: R total = λ p ⋅ R path + λ a ⋅ R outcome + λ f ⋅ R format R_{\text{total}}=\lambda_{p}\cdot R_{\text{path}}+\lambda_{a}\cdot R_{\text{outcome}}+\lambda_{f}\cdot R_{\text{format}} (4)

[34] p: where R path R_{\text{path}} is the path-centric reward computed via dual-track evaluation, R outcome R_{\text{outcome}} is the soft outcome score that extracts signals even from incorrect answers, R format R_{\text{format}} encourages well-structured outputs, and λ p \lambda_{p} , λ a \lambda_{a} , λ f \lambda_{f} are balancing coefficients.

[35] h4: 3.2.1 Reference Planner Generation

[36] p: We generate reference planners offline through rejection sampling and LLM voting. For each training sample ( q , a ∗ ) (q,a^{*}) , we generate K K candidate trajectories using a high-capability LLM, filter for correct answers, and apply LLM voting to distill an optimized reference planner P ref P_{\text{ref}} :

[37] table: P ref = Vote ​ ( { T i } i = 1 K | correct ​ ( T i ) ) P_{\text{ref}}=\text{Vote}(\{T_{i}\}_{i=1}^{K}|\text{correct}(T_{i})) (5)

[38] p: The voting identifies the minimal set of essential steps across successful trajectories, yielding a reference reasoning path ℛ ref = { s 1 , s 2 , … , s m } \mathcal{R}_{\text{ref}}=\{s_{1},s_{2},\ldots,s_{m}\} .

[39] h4: 3.2.2 Dual-Track Path Scoring

[40] p: We evaluate trajectory quality from two complementary perspectives. Track A (Self-Consistency) assesses whether the model effectively executes its own stated plan:

[41] table: S self = r planner × n exec self n plan × n exec self n actions S_{\text{self}}=r_{\text{planner}}\times\frac{n_{\text{exec}}^{\text{self}}}{n_{\text{plan}}}\times\frac{n_{\text{exec}}^{\text{self}}}{n_{\text{actions}}} (6)

[42] p: where r planner r_{\text{planner}} rates the plan quality, n exec self n_{\text{exec}}^{\text{self}} counts executed steps, n plan n_{\text{plan}} is the total planned steps, and n actions n_{\text{actions}} is the total actions in the trajectory. Track B (Reference-Alignment) measures coverage of essential steps from the reference planner using order-agnostic matching:

[43] table: S ref = n covered | ℛ ref | × n covered n actions S_{\text{ref}}=\frac{n_{\text{covered}}}{|\mathcal{R}_{\text{ref}}|}\times\frac{n_{\text{covered}}}{n_{\text{actions}}} (7)

[44] p: where n covered n_{\text{covered}} counts accomplished reference steps regardless of execution order. Both tracks incorporate an efficiency ratio n effective n actions \frac{n_{\text{effective}}}{n_{\text{actions}}} to prevent reward hacking through excessive redundant steps and encourage concise reasoning trajectories. The concrete criteria for determining effective steps and covered steps—including the LLM-based semantic matching procedure—are detailed in Appendix D.3 . The final path-centric reward R path = max ⁡ ( S self , S ref ) R_{\text{path}}=\max(S_{\text{self}},S_{\text{ref}}) takes the maximum rather than a weighted combination, so that when the reference plan is suboptimal or the model discovers a better strategy, the self-consistency track can dominate without being diluted by a low reference score (and vice versa).

[45] h4: 3.2.3 Soft Outcome Scoring

[46] p: To improve sample efficiency, we extract learning signals from trajectories with incorrect final answers through soft scoring:

[47] table: R outcome = { 1.0 if correct α ⋅ r acc + ( 1 − α ) ⋅ r reason otherwise R_{\text{outcome}}=\begin{cases}1.0&\text{if correct}\\ \alpha\cdot r_{\text{acc}}+(1-\alpha)\cdot r_{\text{reason}}&\text{otherwise}\end{cases} (8)

[48] p: where α = 0.8 \alpha=0.8 , r acc r_{\text{acc}} indicates partial answer correctness and r reason r_{\text{reason}} evaluates reasoning quality independent of the final answer. This converts previously zero-reward failed samples into useful training signals based on their path quality.

[49] h2: 4 Experiments

[50] figure: Method General QA Multi-Hop QA Avg. Internal NQ † TriviaQA PopQA HotpotQA † 2Wiki Musique Bamboogle AD-QA Qwen2.5-7B Direct 13.4 40.8 14.0 18.3 25.0 3.1 12.0 18.1 10.3 CoT 4.8 18.5 5.4 9.2 11.1 2.2 23.2 10.6 8.7 RAG 34.9 58.5 39.2 29.9 23.5 5.8 20.8 30.4 60.4 IRCoT 22.4 47.8 30.1 13.3 14.9 7.2 22.4 23.9 52.3 Search-o1 15.1 44.3 13.1 18.7 17.6 5.8 29.6 20.6 48.5 Search-R1 42.9 62.3 42.7 38.6 34.6 16.2 40.0 39.6 65.6 HiPRAG 46.5 65.8 45.8 42.0 46.1 14.0 40.0 42.9 75.6 Search-P1 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 Qwen2.5-3B Direct 10.6 28.8 10.8 14.9 24.4 2.0 2.4 13.4 7.8 CoT 2.3 3.2 0.5 2.1 2.1 0.2 0.0 1.5 5.2 RAG 34.8 54.4 38.7 25.5 22.6 4.7 8.0 27.0 54.7 IRCoT 11.1 31.2 20.0 16.4 17.1 6.7 24.0 18.1 45.8 Search-o1 23.8 47.2 26.2 22.1 21.8 5.4 32.0 25.5 42.1 Search-R1 39.7 56.5 39.1 33.1 31.0 12.4 23.2 33.6 58.3 HiPRAG 43.0 59.8 42.0 36.0 40.5 10.8 24.0 36.6 70.2 Search-P1 53.0 74.5 47.9 36.2 36.6 13.3 28.8 41.5 79.5 Table 1: Main results (ACC %) on seven public QA benchmarks and one internal dataset. Best results are in bold , second best are underlined . † denotes in-domain datasets used for training; others are out-of-domain. AD-QA is a proprietary advertising QA dataset. HiPRAG results are from our reproduction using the same retrieval setup.

[51] figure: Method Avg. ACC Search-P1 (Full) 47.3 w/o Reference-Alignment 42.0 w/o Self-Consistency 44.2 Search-R1 (Baseline) 39.6 Table 2: Ablation study on path-centric reward components (Qwen2.5-7B). Per-dataset results are in Appendix F.4 .

[52] h3: 4.1 Experimental Setup

[53] h5: Datasets.

[54] p: Following prior work, we evaluate on seven public QA benchmarks spanning two categories: (1) General QA : NQ Kwiatkowski et al. (2019) , TriviaQA Joshi et al. (2017) , and PopQA Mallen et al. (2023) ; (2) Multi-Hop QA : HotpotQA Yang et al. (2018) , 2WikiMultiHopQA Ho et al. (2020) , Musique Trivedi et al. (2022) , and Bamboogle Press et al. (2023) . Additionally, we evaluate on AD-QA , a fully anonymized proprietary advertising QA dataset containing 1,000 multi-hop test instances from an internal business to assess real-world applicability (details in Appendix A ). Following Search-R1, we merge the training sets of NQ and HotpotQA to form a unified training dataset. Evaluation is conducted on all datasets to assess both in-domain (NQ, HotpotQA) and out-of-domain (TriviaQA, PopQA, 2WikiMultiHopQA, Musique, Bamboogle, AD-QA) generalization.

[55] h5: Models.

[56] p: We conduct experiments with Qwen2.5-7B-Instruct and Qwen2.5-3B-Instruct Qwen et al. (2025) , denoted as 7B and 3B for brevity. For retrieval, we use the 2018 Wikipedia dump as the knowledge source and E5 as the retriever, with top-3 passages returned per search step.

[57] h5: Evaluation Metric.

[58] p: We use Accuracy (ACC) as the primary evaluation metric, which checks whether the ground-truth answer is contained in the model’s generated response.

[59] h5: Baselines.

[60] p: We compare against the following methods: (1) Direct Inference : Generation without retrieval, including direct prompting and Chain-of-Thought (CoT); (2) Standard RAG : Single-round retrieval before generation; (3) Prompt-Based Agentic RAG : IRCoT and Search-o1 that use prompting for multi-step retrieval; (4) RL-Based Agentic RAG : Search-R1 and HiPRAG that use reinforcement learning for training. All RL-based methods share identical training and retrieval configurations (detailed in Appendix B ); the only difference is the reward function.

[61] h3: 4.2 Main Results

[62] p: As shown in Table 1 , Search-P1 achieves the highest average accuracy across both model sizes, outperforming all baselines by a clear margin (+7.7 Avg. ACC over Search-R1 on 7B). The gains are especially pronounced on the internal AD-QA benchmark (+20.6 over Search-R1 on 7B), a real-world advertising QA dataset with complex multi-hop queries, confirming the practical value of path-centric rewards in industrial settings. Notably, the improvements are consistent across model scales, with the 3B model achieving +7.9 Avg. ACC over Search-R1, demonstrating that path-centric rewards are effective even for smaller models.

[63] h3: 4.3 Ablation Study

[64] p: We conduct ablation studies to validate the contribution of each reward component in Search-P1 : format reward, path-centric reward, and outcome reward.

[65] h4: 4.3.1 Format Reward

[66] figure: Figure 3: Training dynamics comparison of different format reward strategies. Soft Format (our buffered design) achieves faster ACC improvement and higher stable rewards compared to Strict Format (zero reward for invalid format) and Without Format baseline.

[67] figure: Figure 4: Effect of soft outcome scoring across datasets. Gray bars show accuracy without soft scoring (binary outcome), blue bars show accuracy with soft scoring. Per-dataset results are in Appendix F.6 .

[68] p: As shown in Figure 3 , we compare three strategies: (1) Soft Format (our buffered design), (2) Strict Format (zero reward for violations), and (3) Without Format. Our soft format achieves significantly faster convergence by providing continuous gradient feedback, while the strict approach yields near-zero rewards in early training steps due to frequent formatting errors.

[69] h4: 4.3.2 Path-Centric Reward

[70] p: As shown in Table 2 , removing reference-alignment causes a 5.3% accuracy drop, confirming that reference planners provide valuable path-centric guidance. Removing self-consistency results in a 3.1% decrease. The full dual-track model achieves the best performance, validating that both external guidance and internal consistency are complementary signals.

[71] h4: 4.3.3 Outcome Reward

[72] p: As shown in Figure 4 , soft outcome scoring provides modest gains for single-hop tasks (+1.2%), larger improvements for multi-hop QA (+3.5%), and the highest gain for AD-QA (+8.8%), confirming that complex scenarios benefit most from partial credit signals.

[73] h2: 5 Analysis

[74] h3: 5.1 Hyperparameter Sensitivity

[75] p: We investigate the impact of two critical hyperparameters in our reward formulation: the path reward weight λ p \lambda_{p} and the accuracy weight λ a \lambda_{a} .

[76] p: As shown in Figure 5 , both λ p \lambda_{p} and λ a \lambda_{a} exhibit clear sweet spots. Too little path weight provides insufficient supervision, while too much induces reward overfitting where path metrics improve but accuracy drops. Similarly, over-weighting accuracy neglects reasoning quality and leads to reward hacking. The optimal configuration ( λ p = 0.3 \lambda_{p}{=}0.3 , λ a = 0.6 \lambda_{a}{=}0.6 ) balances accuracy as the primary objective with reasoning quality as a regularizer.

[77] figure: Figure 5: Hyperparameter sensitivity analysis. All rewards are averaged over steps 195–205. (a) Effect of path reward weight λ p \lambda_{p} . (b) Effect of accuracy weight λ a \lambda_{a} . Per-dataset results are in Appendix F.7 .

[78] h3: 5.2 Efficiency Analysis

[79] h5: Training Efficiency

[80] p: Figure 6 (a) compares training dynamics. Search-P1 converges significantly faster, reaching Search-R1’s final accuracy ( ∼ \sim 40%) within 60 steps versus over 150. Meanwhile, Search-P1 ’s interaction turns steadily decrease, indicating path-centric rewards guide toward higher accuracy and more concise reasoning, while Search-R1’s turns remain flat or increase.

[81] h5: Inference Efficiency

[82] p: Figure 6 (b) compares turn distributions across dataset types. Two key findings emerge: (1) Both methods require more turns for complex adversarial queries. (2) Search-P1 maintains consistent turn counts between successful and unsuccessful cases, while Search-R1 exhibits larger gaps for multi-hop (+60%) and adversarial (+47%) tasks.

[83] figure: Figure 6: Efficiency analysis. (a) Training efficiency: accuracy and interaction turns comparison between Search-P1 and Search-R1 during training. (b) Inference efficiency: turns by outcome across dataset types.

[84] h3: 5.3 Model and RL Algorithm Analysis

[85] figure: Model RL Single Multi AD Qwen2.5-3B GRPO 58.5 28.7 79.5 Qwen2.5-3B PPO 57.2 27.5 77.8 Llama-3.2-3B GRPO 56.8 27.1 76.3 Llama-3.2-3B PPO 55.6 26.2 74.6 Table 3: ACC (%) across base models and RL algorithms. All models use Instruct versions. Per-dataset results are in Appendix F.5 .

[86] p: Table 3 examines the impact of base models and RL algorithms. Qwen2.5-3B-Instruct Qwen et al. (2025) slightly outperforms Llama-3.2-3B-Instruct Grattafiori et al. (2024) across all task types, likely due to stronger instruction-following and reasoning capabilities in the base model. GRPO Shao et al. (2024) achieves marginally higher accuracy than PPO Schulman et al. (2017) ; however, PPO exhibits more stable training dynamics with lower variance across runs. Importantly, path-centric rewards yield consistent gains across all model–algorithm combinations, suggesting that our approach is orthogonal to the choice of base model and RL algorithm.

[87] h3: 5.4 LLM Evaluator Analysis

[88] p: Our dual-track scoring and soft outcome scoring rely on an external LLM evaluator during training (at inference time, no evaluator calls are needed). To examine sensitivity, we replaced the default evaluator (HY 2.0-Instruct) with Qwen3-32B and Qwen3-8B, and sampled 200 trajectories to measure human agreement. As shown in Table 4 , Qwen3-32B achieves comparable accuracy ( − - 0.8) and human agreement, while Qwen3-8B degrades by 3.2 points with lower outcome scoring agreement (78.5%). Nevertheless, step coverage—the core component of our path-centric reward—remains robust even with the 8B evaluator (88.0% agreement), confirming that Search-P1 is not tightly coupled to a specific evaluator.

[89] figure: Evaluator ACC Human Agree. (%) Plan Step Outc. HY 2.0-Inst. 47.3 91.2 94.5 88.7 Qwen3-32B 46.5 89.0 92.5 85.0 Qwen3-8B 44.1 83.5 88.0 78.5 Table 4: Effect of LLM evaluator choice on Search-P1 Avg. ACC and human agreement. Per-dataset results are in Appendix F.8 .

[90] h3: 5.5 Case Study

[91] p: To qualitatively illustrate Search-P1 ’s advantages, we present case studies comparing reasoning trajectories with baseline methods. Appendix E provides a representative example from multi-hop QA, demonstrating how path-centric rewards lead to more structured decomposition, precise query formulation, and effective information synthesis.

[92] h2: 6 Conclusion

[93] p: We presented Search-P1 , a framework that introduces path-centric reward shaping for agentic RAG training. By evaluating the structural quality of entire reasoning paths rather than isolated elements, our approach provides fine-grained supervision while respecting the inherent diversity of multi-step reasoning. Extensive experiments on public QA benchmarks and an internal advertsing dataset demonstrate significant improvements in accuracy and efficiency, validating path-centric rewards in both academic and industrial settings.

[94] h2: Ethics Statement

[95] p: Our work focuses on improving the training of AI systems for information retrieval and reasoning. We use publicly available datasets for training and evaluation. The internal AD-QA dataset is fully anonymized with all personally identifiable information removed prior to use. The improved efficiency of agentic RAG systems could reduce computational resources required for deployment, contributing to more sustainable AI.

[96] h2: References

[97] h2: Appendix A AD-QA Dataset

[98] p: AD-QA is a fully anonymized multi-hop QA benchmark from a real-world advertising domain, containing 1,000 test instances requiring multi-step reasoning across domains such as campaign configuration, bidding strategies, audience targeting, and conversion tracking. All instances are derived from authentic user queries with all personally identifiable information removed.

[99] p: Each question requires synthesizing information from at least two distinct knowledge domains, making it a challenging benchmark for multi-hop reasoning in enterprise settings. Ground-truth answers are curated by domain experts and verified through cross-validation.

[100] h2: Appendix B Implementation Details

[101] h3: B.1 Training Configuration

[102] p: For GRPO training, we set the policy learning rate to 1 × 10 − 6 1\times 10^{-6} with a warm-up ratio of 0.1. Training is conducted on 8 × \times H20 GPUs using a total batch size of 512, with a mini-batch size of 256. The micro-batch size per GPU is set to 8 for 7B models and 16 for 3B models.

[103] p: The maximum prompt length and response length are both set to 4,096 tokens, with a maximum model context length of 8,192 tokens. We enable gradient checkpointing for memory efficiency and use Fully Sharded Data Parallel (FSDP) with reference model parameter offloading.

[104] p: For efficient rollout generation, we use SGLang with tensor parallel size of 1 and GPU memory utilization of 0.8 (7B) or 0.75 (3B). Rollout sampling uses temperature τ = 0.6 \tau=0.6 , top- k = 20 k=20 , and top- p = 0.95 p=0.95 . We sample 16 candidate responses per prompt for 7B models and 32 for 3B models with an over-sample rate of 0.1. The KL divergence coefficient β \beta is set to 0.001 with low-variance KL loss, and the clip ratio ranges from 0.2 to 0.28.

[105] h3: B.2 Reward Computation

[106] p: The path-centric reward combines three components with the following default weights: format reward weight λ f = 0.1 \lambda_{f}=0.1 , path reward weight λ p = 0.3 \lambda_{p}=0.3 , and outcome accuracy weight λ a = 0.6 \lambda_{a}=0.6 . The reference planner uses a proprietary instruction-tuned model (anonymized as HY 2.0-Instruct) to generate guidance trajectories, which are cached offline before training to avoid runtime overhead.

[107] p: For self-consistency scoring, we sample 3 independent reasoning paths per query and compute pairwise agreement using Jaccard similarity on extracted evidence spans. The soft outcome scoring applies a decay factor of 0.5 for partial matches when the final answer is incorrect but the reasoning path demonstrates high path quality.

[108] h3: B.3 Computational Cost

[109] p: Reference planners are generated offline for all 90K training samples using HY 2.0-Instruct, with each sample requiring on average 1.91 LLM calls. This is a one-time cost cached before RL training and amortized over all subsequent runs.

[110] h3: B.4 Inference Settings

[111] p: During inference, we set the maximum action budget B = 4 B=4 , allowing up to 4 search-reason iterations per query. The retriever returns top-3 passages per search step. We use sampling with temperature 0.6 and top- p p 0.95 for validation. Model checkpoints are saved every 10 steps, and we select the checkpoint with the highest validation accuracy for final evaluation.

[112] h2: Appendix C Algorithms

[113] p: This section provides algorithmic descriptions of the key components in Search-P1 : (1) offline reference planner generation, (2) agentic RAG inference, and (3) path-centric reward computation.

[114] p: Algorithm 1 describes reference planner generation using a high-capability LLM (HY 2.0-Instruct) to produce structured plans and reference reasoning paths, cached offline for training.

[115] p: Algorithm 2 illustrates agentic RAG inference: the model iteratively generates reasoning, issues search queries via <tool_call> , and receives retrieved passages as <tool_response> until the action budget is exhausted or an answer is produced.

[116] p: Algorithm 3 details the reward computation combining format, dual-track path-centric, and soft outcome signals.

[117] figure: Algorithm 1 Reference Planner Generation 0: Training dataset 𝒟 = { ( q i , a i ) } i = 1 N \mathcal{D}=\{(q_{i},a_{i})\}_{i=1}^{N} , reference LLM ℳ ref \mathcal{M}_{\text{ref}} 0: Reference trajectories 𝒯 ref = { ( p i , r i ) } i = 1 N \mathcal{T}_{\text{ref}}=\{(p_{i},r_{i})\}_{i=1}^{N} 1: for each ( q , a ) ∈ 𝒟 (q,a)\in\mathcal{D} do 2: prompt p ← \text{prompt}_{p}\leftarrow PlannerPrompt ( q ) (q) {Generate planning prompt} 3: p ← ℳ ref ​ ( prompt p ) p\leftarrow\mathcal{M}_{\text{ref}}(\text{prompt}_{p}) {Generate reference plan} 4: prompt r ← \text{prompt}_{r}\leftarrow ReasoningPrompt ( q , p ) (q,p) {Generate reasoning prompt} 5: r ← ℳ ref ​ ( prompt r ) r\leftarrow\mathcal{M}_{\text{ref}}(\text{prompt}_{r}) {Generate reference reasoning path} 6: 𝒯 ref ← 𝒯 ref ∪ { ( p , r ) } \mathcal{T}_{\text{ref}}\leftarrow\mathcal{T}_{\text{ref}}\cup\{(p,r)\} 7: end for 8: return 𝒯 ref \mathcal{T}_{\text{ref}}

[118] figure: Algorithm 2 Agentic RAG Inference 0: Question q q , policy model π \pi , retriever ℛ \mathcal{R} , action budget B B , top- K K 0: Generated trajectory y y with final answer 1: y ← <reasoning> y\leftarrow\texttt{<reasoning>} ; t ← 1 t\leftarrow 1 2: while t ≤ B t\leq B do 3: Δ ← Generate ​ ( π , y ) \Delta\leftarrow\textsc{Generate}(\pi,y) until </tool_call> or </answer> 4: y ← y | Δ y\leftarrow y\,\|\,\Delta 5: if Contains ​ ( y , </answer> ) \textsc{Contains}(y,\texttt{</answer>}) then 6: break {Final answer generated} 7: end if 8: if Contains ​ ( Δ , <tool_call> ) \textsc{Contains}(\Delta,\texttt{<tool\_call>}) then 9: query ← Extract ​ ( Δ , <tool_call> ) \text{query}\leftarrow\textsc{Extract}(\Delta,\texttt{<tool\_call>}) 10: docs ← ℛ ⁡ ( query , K ) \text{docs}\leftarrow\mathcal{R}(\text{query},K) {Retrieve top- K K passages} 11: y ← y | <tool_response> ​ ‖ docs ‖ ​ </tool_response> y\leftarrow y\,\|\,\texttt{<tool\_response>}\,\|\,\text{docs}\,\|\,\texttt{</tool\_response>} 12: t ← t + 1 t\leftarrow t+1 13: end if 14: end while 15: if not Contains ​ ( y , </answer> ) \textsc{Contains}(y,\texttt{</answer>}) then 16: y ← y ​ ‖ <answer> ‖ ​ Generate ​ ( π , y ) y\leftarrow y\,\|\,\texttt{<answer>}\,\|\,\textsc{Generate}(\pi,y) until </answer> 17: end if 18: return y y

[119] figure: Algorithm 3 Search-P1 Reward Computation 0: Trajectory y y , ground truth a ∗ a^{*} , reference plan p ref p_{\text{ref}} , reference path r ref r_{\text{ref}} 0: Total reward R ⁡ ( y ) R(y) 1: // Format Reward 2: if ValidFormat ​ ( y ) \textsc{ValidFormat}(y) and HasAnswer ​ ( y ) \textsc{HasAnswer}(y) and HasToolCall ​ ( y ) \textsc{HasToolCall}(y) then 3: r f ← 0.1 r_{f}\leftarrow 0.1 4: else if HasAnswer ​ ( y ) \textsc{HasAnswer}(y) and HasToolResponse ​ ( y ) \textsc{HasToolResponse}(y) then 5: r f ← 0.05 r_{f}\leftarrow 0.05 6: else 7: return 0 0 {Invalid trajectory} 8: end if 9: 10: // Path-Centric Reward via Dual-Track Evaluation 11: eval ← LLMEvaluate ​ ( y , p ref , r ref ) \text{eval}\leftarrow\textsc{LLMEvaluate}(y,p_{\text{ref}},r_{\text{ref}}) {Call evaluator LLM} 12: r planner ← eval . planner_score r_{\text{planner}}\leftarrow\text{eval}.\text{planner\_score} {Plan quality: 0.2/0.6/1.0/1.2} 13: 14: // Track A: Self-Consistency 15: s self ← r planner × eval . eff_steps_self eval . model_plan_steps s_{\text{self}}\leftarrow r_{\text{planner}}\times\frac{\text{eval}.\text{eff\_steps\_self}}{\text{eval}.\text{model\_plan\_steps}} 16: 17: // Track B: Reference-Alignment 18: s ref ← eval . eff_steps_ref | steps ​ ( r ref ) | s_{\text{ref}}\leftarrow\frac{\text{eval}.\text{eff\_steps\_ref}}{|\text{steps}(r_{\text{ref}})|} 19: 20: r p ← max ⁡ ( s self , s ref ) r_{p}\leftarrow\max(s_{\text{self}},s_{\text{ref}}) {Best of dual tracks} 21: 22: // Outcome Reward with Soft Scoring 23: if ExactMatch ​ ( GetAnswer ​ ( y ) , a ∗ ) \textsc{ExactMatch}(\textsc{GetAnswer}(y),a^{*}) then 24: r o ← 1.0 r_{o}\leftarrow 1.0 25: else 26: r o ← 0.8 × eval . acc_score + 0.2 × eval . reason_score r_{o}\leftarrow 0.8\times\text{eval}.\text{acc\_score}+0.2\times\text{eval}.\text{reason\_score} 27: end if 28: 29: R ⁡ ( y ) ← λ f ⋅ r f + λ p ⋅ r p + λ o ⋅ r o R(y)\leftarrow\lambda_{f}\cdot r_{f}+\lambda_{p}\cdot r_{p}+\lambda_{o}\cdot r_{o} 30: return R ⁡ ( y ) R(y)

[120] h2: Appendix D Prompt Templates

[121] p: This section presents the prompt templates used in Search-P1 for inference, reference planner generation, and reward evaluation.

[122] h3: D.1 Agentic RAG Inference Prompt

[123] p: Figure 7 shows the prompt template used during both training rollouts and inference. The prompt instructs the model to decompose questions into sub-tasks, execute searches iteratively, and produce structured outputs with <reasoning> , <tool_call> , and <answer> tags.

[124] figure: Agentic RAG Inference Prompt You are a meticulous Deep Research Agent . Your goal is to provide a comprehensive and accurate answer by conducting multiple rounds of search. ## CRITICAL INSTRUCTIONS 1. Detailed Planning (<reasoning>): • In the first turn, you MUST break the question down into multiple dependent sub-questions . • Focus on one sub-question at a time. 2. Step-by-Step Execution (<tool_call>): • Execute only ONE search query per turn. • After receiving results, verify: “Is this sufficient? Do I need more details?” 3. No Guessing: • If results are incomplete, issue another search. Do NOT hallucinate. 4. Final Answer (<answer>): • Only output <answer> when ALL necessary information is gathered. ## CURRENT TASK Question: {question} Figure 7: Prompt template for agentic RAG inference. The model is instructed to plan, search iteratively, and provide structured outputs.

[125] h3: D.2 Reference Planner Generation Prompt

[126] p: Figure 8 shows the prompt used to generate reference plans and reasoning paths from HY 2.0-Instruct. Given a question and its correct answer, the reference LLM produces an optimized search strategy that serves as guidance during path reward computation.

[127] figure: Reference Planner Generation Prompt You are an expert planner and reasoning optimizer. Current Question: {question} Correct Answer: {golden_answers} Your task is to generate: 1. Optimized Reasoning Path: A sequence of search queries that would lead directly to the correct answer in the most efficient way. Format as a numbered list. 2. Optimized Planner: A concise, step-by-step instruction on how a reasoning agent should solve this question correctly and efficiently. Important: • Focus on the minimal set of queries needed. • Avoid redundant or inefficient steps. Output format: <correct_reasoning_path> 1. query 1 2. query 2 </correct_reasoning_path> <optimized_planner> To solve this, first search for... then... </optimized_planner> Figure 8: Prompt template for reference planner generation. HY 2.0-Instruct generates optimal search strategies for each training sample.

[128] h3: D.3 Dual-Track Evaluation Prompt

[129] p: Figure 9 presents the prompt used for dual-track path evaluation. An evaluator LLM assesses the model’s trajectory along two dimensions: self-consistency (execution of its own plan) and reference-alignment (coverage of expert reference steps), along with outcome quality scoring.

[130] figure: Dual-Track Evaluation Prompt You are an expert RL researcher evaluating an AI agent’s trajectory. Your task is to conduct a Dual-Track Evaluation : 1. Self-Consistency Track : How well did the agent execute its OWN plan? 2. Reference-Alignment Track : How well did the agent follow the Expert plan? 3. Outcome Evaluation : Assess accuracy and reasoning quality. Evaluation Inputs: • Question : {question} • Correct Answer : {golden_answers} • Reference Planner : {ref_planner} • Reference Path : {ref_reasoning_path} • Model Trajectory : {trajectory} Scoring Criteria: • Planner Score : 0.2 (Bad) / 0.6 (Average) / 1.0 (Good) / 1.2 (Excellent) • Outcome Accuracy : 0.0 (Wrong) / 0.5 (Partial) / 1.0 (Correct) • Reasoning Quality : 0.0 / 0.5 / 0.8 / 1.0 Output: JSON with planner_score , model_plan_steps , effective_steps_self , effective_steps_ref , outcome_accuracy_score , outcome_reasoning_score . Figure 9: Prompt template for dual-track evaluation. The evaluator LLM assesses both self-consistency and reference-alignment of model trajectories.

[131] h2: Appendix E Case Study

[132] p: To qualitatively illustrate Search-P1 ’s advantages, we present a representative case from MuSiQue demonstrating how path-centric reward shaping leads to more accurate multi-hop reasoning.

[133] h3: E.1 Multi-Hop Reasoning Comparison

[134] p: Figure 10 compares Search-R1 and Search-P1 on a multi-hop question. Without explicit planning, Search-R1 misinterprets “rock & roll” as a genre descriptor, retrieving information about the wrong entity. In contrast, Search-P1 ’s planning correctly identifies “Bang Bang Rock & Roll” as a complete album title, leading to the correct answer.

[135] figure: Query: Who is the lead singer of the band performing Bang Bang Rock & Roll? Answer: Eddie Argos Search-R1 (Incorrect) <think> I need to find who performs “Bang Bang Rock & Roll.” </think> <search> song Bang Bang rock and roll genre </search> <result> In 2017, Dan Auerbach collaborated with Robert Finley on “Bang Bang,” featuring a classic rock and roll sound… </result> <search> lead singer of The Black Keys </search> <result> Dan Auerbach serves as the lead vocalist… </result> Final: ✗ Dan Auerbach Search-P1 (Correct) <reasoning> I need to: 1. Find the band performing “Bang Bang Rock & Roll”. 2. Find the lead singer. </reasoning> <tool_call> “Bang Bang Rock & Roll” album </tool_call> <tool_response> “Bang Bang Rock & Roll” is the debut album by British rock band Art Brut … </tool_response> <tool_call> lead singer of Art Brut </tool_call> <tool_response> …frontman Eddie Argos ’ enthusiastic vocal delivery… </tool_response> Final: ✓ Eddie Argos Figure 10: Comparison of reasoning trajectories. Search-R1’s imprecise query retrieves valid but irrelevant results; Search-P1 ’s planning-driven query retrieves the correct information. Highlighted text shows search queries.

[136] h2: Appendix F Additional Results

[137] h3: F.1 Impact of Retrieved Documents per Search

[138] figure: Model # Docs General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA 7B 1 45.8 67.2 38.5 35.2 32.0 15.5 36.0 38.6 72.8 2 52.0 74.2 44.0 39.5 36.8 18.8 41.0 43.8 80.5 3 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 5 55.8 77.8 46.8 42.5 39.2 22.4 45.2 47.1 85.5 10 53.5 74.5 44.5 40.5 37.2 20.1 42.8 44.7 82.5 3B 1 42.8 63.5 38.2 28.8 28.5 9.2 21.2 33.2 64.5 2 48.5 69.8 43.6 32.8 33.2 11.5 25.2 37.8 73.2 3 53.0 74.5 47.9 36.2 36.6 13.3 28.8 41.5 79.5 5 52.2 73.8 47.2 36.5 36.0 12.8 30.4 41.3 78.8 10 49.8 71.2 45.0 33.8 34.2 11.8 27.6 39.1 75.5 Table 5: Performance (ACC %) with different numbers of retrieved documents per search. Retrieving 3 documents achieves the best average performance. While 5 documents shows advantages on specific datasets (MuSiQue, Bamboogle for 7B; HotpotQA, Bamboogle for 3B), the overall best configuration is 3 documents.

[139] p: Table 5 shows how the number of retrieved documents per search iteration affects model performance. Retrieving too few documents may miss relevant information, while retrieving too many can introduce noise and increase context length.

[140] h3: F.2 Effect of Format Reward on Output Compliance

[141] figure: Model Method General QA Multi-Hop QA Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA 7B w/o Format Reward 82.8 84.2 81.5 79.1 76.8 75.2 83.6 88.2 w/ Format Reward 95.1 95.6 94.2 91.5 88.8 87.6 96.4 97.5 3B w/o Format Reward 72.8 75.5 72.2 67.1 61.8 62.4 65.2 78.8 w/ Format Reward 87.2 88.1 85.4 80.2 74.8 75.1 78.0 91.5 Table 6: Format compliance rate (%) with and without format reward. Adding format reward significantly improves the model’s ability to produce properly structured responses with parseable answers.

[142] p: Table 6 analyzes the relationship between the format reward component and the model’s ability to produce properly formatted outputs.

[143] h3: F.3 Search Iterations Analysis

[144] figure: Model Dataset Successful Cases Failed Cases 1 iter 2 iter 3+ iter 1 iter 2 iter 3+ iter 7B NQ 68.5% 22.3% 9.2% 45.2% 28.6% 26.2% TriviaQA 72.1% 19.8% 8.1% 48.3% 26.4% 25.3% PopQA 65.8% 24.5% 9.7% 42.1% 29.8% 28.1% HotpotQA 28.5% 48.2% 23.3% 35.4% 30.1% 34.5% 2Wiki 25.1% 50.6% 24.3% 33.8% 29.5% 36.7% MuSiQue 18.5% 52.3% 29.2% 31.2% 28.6% 40.2% Bamboogle 22.4% 45.6% 32.0% 28.3% 25.4% 46.3% AD-QA 35.2% 42.5% 22.3% 22.8% 28.5% 48.7% Average 42.0% 38.2% 19.8% 35.9% 28.4% 35.7% 3B NQ 62.3% 26.1% 11.6% 40.5% 30.2% 29.3% TriviaQA 66.8% 23.4% 9.8% 44.1% 28.5% 27.4% PopQA 60.2% 28.3% 11.5% 38.6% 31.2% 30.2% HotpotQA 22.4% 45.8% 31.8% 30.2% 28.5% 41.3% 2Wiki 20.3% 47.2% 32.5% 28.5% 27.8% 43.7% MuSiQue 14.2% 48.6% 37.2% 26.4% 26.2% 47.4% Bamboogle 16.8% 42.1% 41.1% 24.5% 23.8% 51.7% AD-QA 28.5% 40.2% 31.3% 18.2% 25.6% 56.2% Average 36.4% 37.7% 25.9% 31.4% 27.7% 40.9% Table 7: Distribution of search iterations for successful and failed cases. General QA datasets (NQ, TriviaQA, PopQA) show high success rates with single-iteration searches, while Multi-Hop QA datasets require more iterations. Failed cases consistently show higher proportions of 3+ iterations, suggesting that excessive searching indicates difficulty in finding relevant information.

[145] p: Table 7 presents the distribution of search iterations for successful and failed cases across different datasets.

[146] h5: Key Observations.

[147] p: (1) General QA datasets achieve most successes with single-iteration searches. (2) Multi-hop datasets show successful cases concentrated at 2 iterations. (3) Failed cases consistently show higher 3+ iteration rates, suggesting excessive searching indicates difficulty. (4) The 3B model requires slightly more iterations than 7B.

[148] h3: F.4 Detailed Ablation on Path-Centric Reward Components

[149] figure: Method General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA Qwen2.5-7B Search-P1 (Full) 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 w/o Reference-Alignment 50.8 73.0 43.2 37.5 34.0 16.8 39.5 42.1 78.8 w/o Self-Consistency 53.0 75.5 44.8 39.8 37.2 19.2 40.2 44.2 82.5 Search-R1 (Baseline) 42.9 62.3 42.7 38.6 34.6 16.2 40.0 39.6 65.6 Qwen2.5-3B Search-P1 (Full) 53.0 74.5 47.9 36.2 36.6 13.3 28.8 41.5 79.5 w/o Reference-Alignment 47.8 68.5 43.4 31.2 30.5 10.1 24.0 36.5 70.5 w/o Self-Consistency 49.8 71.8 45.2 33.8 34.0 11.8 26.0 38.9 75.2 Search-R1 (Baseline) 39.7 56.5 39.1 33.1 31.0 12.4 23.2 33.6 58.3 Table 8: Detailed ablation study on path reward components (ACC %). Removing reference-alignment causes larger drops on multi-hop datasets where external guidance is more critical, while removing self-consistency affects general QA more where the model’s own planning suffices.

[150] p: Table 8 provides the complete per-dataset breakdown for the path-centric reward component ablation study (extending Table 2 in the main paper).

[151] h3: F.5 Detailed Model and RL Algorithm Analysis

[152] figure: Model RL General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA Qwen2.5-3B-Inst. GRPO 53.0 74.5 47.9 36.2 36.6 13.3 28.8 41.5 79.5 Qwen2.5-3B-Inst. PPO 51.6 73.1 46.8 34.8 35.4 12.6 27.6 40.3 78.1 Llama-3.2-3B-Inst. GRPO 50.2 71.8 45.4 33.9 34.1 11.8 26.0 39.0 75.8 Llama-3.2-3B-Inst. PPO 48.9 70.2 44.2 32.8 33.0 10.9 24.8 37.8 74.2 Table 9: Detailed accuracy (%) across different base models and RL algorithms on all datasets. Qwen2.5 consistently outperforms Llama-3.2, and GRPO achieves slightly higher accuracy than PPO across all datasets.

[153] p: Table 9 extends Table 3 with per-dataset accuracy for different base models and RL algorithms.

[154] h3: F.6 Detailed Soft Outcome Scoring Analysis

[155] figure: Model Method General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA 7B w/o Soft Scoring 55.4 77.5 46.0 39.2 36.5 18.5 40.8 44.8 77.4 w/ Soft Scoring 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 Δ \Delta +1.2 +1.1 +1.5 +3.7 +3.3 +3.3 +3.2 +2.5 +8.8 3B w/o Soft Scoring 51.8 73.2 46.5 32.6 33.1 10.4 24.5 38.9 68.5 w/ Soft Scoring 53.0 74.5 47.9 36.2 36.6 13.3 28.8 41.5 79.5 Δ \Delta +1.2 +1.3 +1.4 +3.6 +3.5 +2.9 +4.3 +2.6 +11.0 Table 10: Effect of soft outcome scoring (ACC %). Multi-hop QA datasets benefit more from soft scoring (+3.0–3.7%) compared to general QA datasets (+1.1–1.5%), while the internal AD-QA dataset shows the largest improvement (+8.8–11.0%), confirming that complex enterprise queries benefit most from partial credit signals.

[156] p: Table 10 provides the per-dataset breakdown of the soft outcome scoring ablation (corresponding to Figure 4 in the main paper).

[157] h3: F.7 Detailed Hyperparameter Sensitivity Analysis

[158] figure: λ p \lambda_{p} General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA 0.2 55.5 77.8 46.8 41.8 38.5 20.8 44.5 46.5 83.5 0.3 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 0.4 55.8 78.0 47.2 42.2 39.2 21.5 43.8 46.8 85.0 Table 11: Effect of path reward weight λ p \lambda_{p} on performance (ACC %, Qwen2.5-7B). The optimal value is λ p = 0.3 \lambda_{p}=0.3 , which achieves the best average performance. While λ p = 0.2 \lambda_{p}=0.2 shows slight advantage on Bamboogle, λ p = 0.3 \lambda_{p}=0.3 provides the best overall balance.

[159] figure: λ a \lambda_{a} General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA 0.6 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 0.8 56.0 78.2 47.0 42.5 39.2 22.2 44.8 47.1 85.5 1.0 54.8 76.8 45.8 41.2 38.0 20.8 43.2 45.8 83.2 Table 12: Effect of outcome accuracy weight λ a \lambda_{a} on performance (ACC %, Qwen2.5-7B). The optimal value is λ a = 0.6 \lambda_{a}=0.6 , which achieves the best average performance. While λ a = 0.8 \lambda_{a}=0.8 shows slight advantages on MuSiQue and Bamboogle, λ a = 0.6 \lambda_{a}=0.6 provides better overall results.

[160] p: Tables 11 and 12 provide the per-dataset breakdown for hyperparameter sensitivity analysis (corresponding to Figure 5 in the main paper).

[161] h3: F.8 Detailed LLM Evaluator Analysis

[162] figure: LLM Evaluator General QA Multi-Hop QA Avg. Internal NQ TriviaQA PopQA HotpotQA 2Wiki MuSiQue Bamboogle AD-QA HY 2.0-Instruct 56.6 78.6 47.5 42.9 39.8 21.8 44.0 47.3 86.2 Qwen3-32B 55.5 77.5 46.2 41.8 38.8 20.8 42.5 46.2 84.2 Qwen3-8B 52.8 74.2 43.5 39.2 35.8 17.8 39.8 43.3 79.5 Table 13: Detailed accuracy (%) across LLM evaluators (Qwen2.5-7B + GRPO). Qwen3-32B shows modest degradation ( − - 1.1 Avg.), while Qwen3-8B exhibits larger drops on multi-hop tasks where step coverage evaluation is more challenging.

[163] p: Table 13 provides the per-dataset breakdown for the LLM evaluator analysis. The Qwen3-8B evaluator shows larger drops on multi-hop datasets (e.g., − - 4.0 on MuSiQue, − - 4.0 on 2Wiki) where accurately counting covered reasoning steps is more challenging.

[164] h2: Instructions for reporting errors

[165] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[166] p: Tip: You can select the relevant text first, to include it in your report.

[167] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[168] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
