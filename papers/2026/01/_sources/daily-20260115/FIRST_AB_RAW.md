[2601.08808v1] Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge (https://arxiv.org/abs/2601.08808v1)
citeturn26908view0 [wordlim: 200] Crawled: 2 weeks ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.08808v1","lineno":null}); Total lines: 163
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 13 Jan 2026]
L9: # Title:Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge
L10: 
L11: Authors:cite5†Yao Tang , cite6†Li Dong , cite7†Yaru Hao , cite8†Qingxiu Dong , cite9†Furu Wei , cite10†Jiatao Gu L12: 
L13: View a PDF of the paper titled Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge, by Yao Tang and 5 other authors
L14: 
L15: cite11†View PDF cite12†HTML (experimental) L16: > Abstract:Large language models often solve complex reasoning tasks more effectively with Chain-of-Thought (CoT), but at the cost of long, low-bandwidth token sequences. Humans, by contrast, often reason softly by maintaining a distribution over plausible next steps. Motivated by this, we propose Multiplex Thinking, a stochastic soft reasoning mechanism that, at each thinking step, samples K candidate tokens and aggregates their embeddings into a single continuous multiplex token.
L17: This preserves the vocabulary embedding prior and the sampling dynamics of standard discrete generation, while inducing a tractable probability distribution over multiplex rollouts. Consequently, multiplex trajectories can be directly optimized with on-policy reinforcement learning (RL).
L18: Importantly, Multiplex Thinking is self-adaptive: when the model is confident, the multiplex token is nearly discrete and behaves like standard CoT; when it is uncertain, it compactly represents multiple plausible next steps without increasing sequence length. Across challenging math reasoning benchmarks, Multiplex Thinking consistently outperforms strong discrete CoT and RL baselines from Pass@1 through Pass@1024, while producing shorter sequences.
L19: The code and checkpoints are available at cite13†this https URL†github.com .
L20: Comments:  | 21 pages. Code available at cite13†this https URL†github.com L21: Subjects:  | Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
L22: Cite as:  | cite14†arXiv:2601.08808 [cs.CL]
L23:    | (or cite15†arXiv:2601.08808v1 [cs.CL] for this version)
L24:    | cite16†https://doi.org/10.48550/arXiv.2601.08808†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Jiatao Gu [cite17†view email ]
L28: [v1] Tue, 13 Jan 2026 18:48:00 UTC (952 KB)
L29: 
L30: Full-text links:
L31: 
L32: ## Access Paper:
L33: 
L34: View a PDF of the paper titled Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge, by Yao Tang and 5 other authors
L35: 



[2601.08539v1] Reducing Compute Waste in LLMs through Kernel-Level DVFS (https://arxiv.org/abs/2601.08539v1)
citeturn26908view1 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.08539v1","lineno":null}); Total lines: 161
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Performance
L7: 
L8: [Submitted on 13 Jan 2026]
L9: # Title:Reducing Compute Waste in LLMs through Kernel-Level DVFS
L10: 
L11: Authors:cite5†Jeffrey Spaan , cite6†Kuan-Hsun Chen , cite7†Ana-Lucia Varbanescu L12: 
L13: View a PDF of the paper titled Reducing Compute Waste in LLMs through Kernel-Level DVFS, by Jeffrey Spaan and 2 other authors
L14: 
L15: cite8†View PDF cite9†HTML (experimental) L16: > Abstract:The rapid growth of AI has fueled the expansion of accelerator- or GPU-based data centers. However, the rising operational energy consumption has emerged as a critical bottleneck and a major sustainability concern. Dynamic Voltage and Frequency Scaling (DVFS) is a well-known technique used to reduce energy consumption, and thus improve energy-efficiency, since it requires little effort and works with existing hardware.
L17: Reducing the energy consumption of training and inference of Large Language Models (LLMs) through DVFS or power capping is feasible: related work has shown energy savings can be significant, but at the cost of significant slowdowns. In this work, we focus on reducing waste in LLM operations: i.e., reducing energy consumption without losing performance.
L18: We propose a fine-grained, kernel-level, DVFS approach that explores new frequency configurations, and prove these save more energy than previous, pass- or iteration-level solutions. For example, for a GPT-3 training run, a pass-level approach could reduce energy consumption by 2% (without losing performance), while our kernel-level approach saves as much as 14.6% (with a 0.6% slowdown).
L19: We further investigate the effect of data and tensor parallelism, and show our discovered clock frequencies translate well for both. We conclude that kernel-level DVFS is a suitable technique to reduce waste in LLM operations, providing significant energy savings with negligible slow-down.
L20: Subjects:  | Performance (cs.PF); Machine Learning (cs.LG)
L21: Cite as:  | cite10†arXiv:2601.08539 [cs.PF]
L22:    | (or cite11†arXiv:2601.08539v1 [cs.PF] for this version)
L23:    | cite12†https://doi.org/10.48550/arXiv.2601.08539†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Kuan-Hsun Chen [cite13†view email ]
L27: [v1] Tue, 13 Jan 2026 13:26:57 UTC (1,529 KB)
L28: 
L29: Full-text links:
L30: 
L31: ## Access Paper:
L32: 
L33: View a PDF of the paper titled Reducing Compute Waste in LLMs through Kernel-Level DVFS, by Jeffrey Spaan and 2 other authors
L34: 
L35:   * cite8†View PDF L36:   * cite9†HTML (experimental) L37:   * cite14†TeX Source L38: 



[2601.08800v1] MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm (https://arxiv.org/abs/2601.08800v1)
citeturn26908view2 [wordlim: 200] Crawled: last month; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.08800v1","lineno":null}); Total lines: 161
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Distributed, Parallel, and Cluster Computing
L7: 
L8: [Submitted on 13 Jan 2026]
L9: # Title:MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm
L10: 
L11: Authors:cite5†Bowen Zhou , cite6†Jinrui Jia , cite7†Wenhao He , cite8†Yong Zhang , cite9†Fang Dong L12: 
L13: View a PDF of the paper titled MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm, by Bowen Zhou and 3 other authors
L14: 
L15: cite10†View PDF cite11†HTML (experimental) L16: > Abstract:The Mixture of Experts (MoE) models are emerging as the latest paradigm for Large Language Models (LLMs). However, due to memory constraints, MoE models with billions or even trillions of parameters can only be deployed in multi-GPU or even multi-node & multi-GPU based serving systems. Thus, communication has became a major bottleneck in distributed serving systems, especially inter-node communication.
L17: Contemporary distributed MoE models are primarily implemented using all-reduce (AR) based tensor parallelism (TP) and all-to-all (A2A) based expert parallelism (EP). However, TP generally exhibits low inter-node efficiency and is thus confined to high-speed intra-node bandwidth. In contrast, EP tends to suffer from load imbalance, especially when the parallel degree is high.
L18: > In this work, we introduce MixServe, a novel automatic distributed serving system for efficient deployment of MoE models by a novel TP-EP hybrid parallelism based on fused AR-A2A communication algorithm. MixServe begins by evaluating the communication overhead associated with various parallel strategies, taking into account the model hyperparameters and the configurations of network and hardware resources, and then automatically selects the most efficient parallel strategy.
L19: Then, we propose the TP-EP hybrid parallelism based on fused AR-A2A communication algorithm that overlaps intra-node AR communication and inter-node A2A communication. Extensive experiments on DeepSeek-R1 and Qwen3 models demonstrate that MixServe achieves superior inference performance, with 1.08~3.80x acceleration in time to first token (TTFT), 1.03~1.66x acceleration in inter-token latency (ITL), and 5.2%~50.3% throughput improvement compared to existing approaches.
L20: Comments:  | Submitted to ICDCS 2026
L21: Subjects:  | Distributed, Parallel, and Cluster Computing (cs.DC)
L22: Cite as:  | cite12†arXiv:2601.08800 [cs.DC]
L23:    | (or cite13†arXiv:2601.08800v1 [cs.DC] for this version)
L24:    | cite14†https://doi.org/10.48550/arXiv.2601.08800†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Bowen Zhou [cite15†view email ]
L28: [v1] Tue, 13 Jan 2026 18:38:18 UTC (549 KB)
L29: 
L30: Full-text links:
L31: 
L32: ## Access Paper:
L33: 
L34: View a PDF of the paper titled MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm, by Bowen Zhou and 3 other authors
L35: 



[2601.08692v1] Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models (https://arxiv.org/abs/2601.08692v1)
citeturn26908view3 [wordlim: 200] Crawled: last month; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2601.08692v1","lineno":null}); Total lines: 161
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 13 Jan 2026 (this version), latest version 19 Jan 2026 (cite5†v2 )]
L9: # Title:Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models
L10: 
L11: Authors:cite6†Keito Inoshita L12: 
L13: View a PDF of the paper titled Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models, by Keito Inoshita
L14: 
L15: cite7†View PDF cite8†HTML (experimental) L16: > Abstract:Predicting nationality from personal names has practical value in marketing, demographic research, and genealogical studies. Conventional neural models learn statistical correspondences between names and nationalities from task-specific training data, posing challenges in generalizing to low-frequency nationalities and distinguishing similar nationalities within the same region.
L17: Large language models (LLMs) have the potential to address these challenges by leveraging world knowledge acquired during pre-training. In this study, we comprehensively compare neural models and LLMs on nationality prediction, evaluating six neural models and six LLM prompting strategies across three granularity levels (nationality, region, and continent), with frequency-based stratified analysis and error analysis.
L18: Results show that LLMs outperform neural models at all granularity levels, with the gap narrowing as granularity becomes coarser. Simple machine learning methods exhibit the highest frequency robustness, while pre-trained models and LLMs show degradation for low-frequency nationalities.
L19: Error analysis reveals that LLMs tend to make ``near-miss'' errors, predicting the correct region even when nationality is incorrect, whereas neural models exhibit more cross-regional errors and bias toward high-frequency classes. These findings indicate that LLM superiority stems from world knowledge, model selection should consider required granularity, and evaluation should account for error quality beyond accuracy.
L20: Subjects:  | Computation and Language (cs.CL)
L21: Cite as:  | cite9†arXiv:2601.08692 [cs.CL]
L22:    | (or cite10†arXiv:2601.08692v1 [cs.CL] for this version)
L23:    | cite11†https://doi.org/10.48550/arXiv.2601.08692†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Keito Inoshita [cite12†view email ]
L27: [v1] Tue, 13 Jan 2026 16:17:04 UTC (406 KB)
L28: cite5†[v2] Mon, 19 Jan 2026 08:02:06 UTC (407 KB)
L29: 
L30: Full-text links:
L31: 
L32: ## Access Paper:
L33: 
L34: View a PDF of the paper titled Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models, by Keito Inoshita
L35: 



Internal Error ()
citeturn26908view4 [wordlim: 200] Source: open({"ref_id":"https://arxiv.org/abs/2601.08750v1","lineno":null}); Total lines: 1
