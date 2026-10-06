# 03/18 仅有界题摘身份记录

检查时间2026-10-02T02:26:56+08:00。本文件仅原始题摘/历史，不是Evidence完成、不继承旧库存。12 arXiv潜在线索与4具名负侧；16068v1原HTML恢复见末段，API返回v3不替代v1。

[2603.15854v1] FlashSampling: Fast and Memory-Efficient Exact Sampling (https://arxiv.org/abs/2603.15854v1)
citeturn25356view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.15854v1","lineno":null}); Total lines: 168
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Machine Learning
L7: 
L8: [Submitted on 16 Mar 2026 (this version), latest version 25 Sep 2026 (cite5†v3 )]
L9: # Title:FlashSampling: Fast and Memory-Efficient Exact Sampling
L10: 
L11: Authors:cite6†Tomas Ruiz , cite7†Zhen Qin , cite8†Yifan Zhang , cite9†Xuyang Shen , cite10†Yiran Zhong , cite11†Mengdi Wang L12: 
L13: View a PDF of the paper titled FlashSampling: Fast and Memory-Efficient Exact Sampling, by Tomas Ruiz and 5 other authors
L14: 
L15: cite12†View PDF cite13†HTML (experimental) L16: > Abstract:Sampling from a categorical distribution is mathematically simple, but in large-vocabulary decoding, it often triggers extra memory traffic and extra kernels after the LM head. We present FlashSampling, an exact sampling primitive that fuses sampling into the LM-head matmul and never materializes the logits tensor in HBM.
L17: The method is simple: compute logits tile-by-tile on chip, add Gumbel noise, keep only one maximizer per row and per vocabulary tile, and finish with a small reduction over tiles. The fused tiled kernel is exact because $\argmax$ decomposes over a partition; grouped variants for online and tensor-parallel settings are exact by hierarchical factorization of the categorical distribution.
L18: Across H100, H200, B200, and B300 GPUs, FlashSampling speeds up kernel-level decode workloads, and in end-to-end vLLM experiments, it reduces time per output token by up to $19%$ on the models we test. These results show that exact sampling, with no approximation, can be integrated into the matmul itself, turning a bandwidth-bound postprocessing step into a lightweight epilogue. Project Page: cite14†this https URL†github.com .
L19: Comments:  | Project Page: cite14†this https URL†github.com L20: Subjects:  | Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
L21: Cite as:  | cite15†arXiv:2603.15854 [cs.LG]
L22:    | (or cite16†arXiv:2603.15854v1 [cs.LG] for this version)
L23:    | cite17†https://doi.org/10.48550/arXiv.2603.15854†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Yifan Zhang [cite18†view email ]
L27: [v1] Mon, 16 Mar 2026 19:37:08 UTC (242 KB)
L28: cite19†[v2] Tue, 12 May 2026 21:02:06 UTC (252 KB)
L29: cite5†[v3] Fri, 25 Sep 2026 23:50:47 UTC (252 KB)
L30: 



[2603.15953v1] A Family of LLMs Liberated from Static Vocabularies (https://arxiv.org/abs/2603.15953v1)
citeturn25356view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.15953v1","lineno":null}); Total lines: 162
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 16 Mar 2026]
L9: # Title:A Family of LLMs Liberated from Static Vocabularies
L10: Authors:cite5†Aleph Alpha : cite6†Adnen Abdessaied , cite7†Artur Baranowski , cite8†Lukas Balles , cite9†Michael Barlow , cite10†Fabien C. Y. Benureau , cite11†Felix Berkenkamp , cite12†Lukas Bluebaum , cite13†Bastian Boll , cite14†Thomas F.
L11: Burns , cite15†Björn Deiseroth , cite16†Constantin Eichenberg , cite17†David Friede , cite18†Pablo Iyu Guerrero , cite19†Ahmed Hammam , cite20†Bastian Harren , cite21†Johann Higl , cite22†Yasser Jadidi , cite23†Carina Kauf , cite24†Johannes Messner , cite25†Jan Hendrik Metzen , cite26†Max Meuer , cite27†Vedant Nanda , cite28†Pit Neitemeier , cite29†Koen Oostermeijer , cite30†Letitia Parcalabescu , cite31†Markus Pernpointner , cite32†Felix Reinfurt , cite33†Dylan Rodriquez , cite34†Grégory Schott , cite35†Philipp Siedler , cite36†Martin Simonovsky , cite37†Till Speicher , cite38†Volker Stampa , cite39†Stephan Wäldchen , cite40†Samuel Weinbach , cite41†Gregor Ziegltrum L12: View a PDF of the paper titled A Family of LLMs Liberated from Static Vocabularies, by Aleph Alpha: Adnen Abdessaied and 35 other authors
L13: 
L14: cite42†View PDF cite43†HTML (experimental) L15: > Abstract:Tokenization is a central component of natural language processing in current large language models (LLMs), enabling models to convert raw text into processable units. Although learned tokenizers are widely adopted, they exhibit notable limitations, including their large, fixed vocabulary sizes and poor adaptability to new domains or languages. We present a family of models with up to 70 billion parameters based on the hierarchical autoregressive transformer (HAT) architecture.
L16: In HAT, an encoder transformer aggregates bytes into word embeddings and then feeds them to the backbone, a classical autoregressive transformer. The outputs of the backbone are then cross-attended by the decoder and converted back into bytes.
L17: We show that we can reuse available pre-trained models by converting the Llama 3.1 8B and 70B models into the HAT architecture: Llama-3.1-8B-TFree-HAT and Llama-3.1-70B-TFree-HAT are byte-level models whose encoder and decoder are trained from scratch, but where we adapt the pre-trained Llama backbone, i.e., the transformer blocks with the embedding matrix and head removed, to handle word embeddings instead of the original tokens.
L18: We also provide a 7B HAT model, Llama-TFree-HAT-Pretrained, trained entirely from scratch on nearly 4 trillion words. The HAT architecture improves text compression by reducing the number of required sequence positions and enhances robustness to intra-word variations, e.g., spelling differences.
L19: Through pre-training, as well as subsequent supervised fine-tuning and direct preference optimization in English and German, we show strong proficiency in both languages, improving on the original Llama 3.1 in most benchmarks. We release our models (including 200 pre-training checkpoints) on Hugging Face.
L20: Subjects:  | Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
L21: Cite as:  | cite44†arXiv:2603.15953 [cs.CL]
L22:    | (or cite45†arXiv:2603.15953v1 [cs.CL] for this version)
L23:    | cite46†https://doi.org/10.48550/arXiv.2603.15953†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Fabien C. Y. Benureau [cite47†view email ]
L27: [v1] Mon, 16 Mar 2026 22:07:18 UTC (1,634 KB)
L28: 
L29: Full-text links:
L30: 



[2603.16054v1] inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for LLM Inference (https://arxiv.org/abs/2603.16054v1)
citeturn25356view2 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16054v1","lineno":null}); Total lines: 160
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Distributed, Parallel, and Cluster Computing
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for LLM Inference
L10: 
L11: Authors:cite5†Huamin Chen , cite6†Xunzhuo Liu , cite7†Yuhan Liu , cite8†Junchen Jiang , cite9†Bowei He , cite6†Xue Liu L12: 
L13: View a PDF of the paper titled inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for LLM Inference, by Huamin Chen and 5 other authors
L14: 
L15: cite10†View PDF cite11†HTML (experimental) L16: > Abstract:Sizing a GPU fleet for LLM inference is harder than it looks. The obvious questions -- how many GPUs, which type, where to split a two-pool fleet -- have no closed-form answers. They depend on the full token-length distribution, the routing policy, and queueing dynamics that turn ugly under heavy-tailed workloads. Existing tools optimize per-engine configuration for a fixed GPU count; none of them address the upstream question of how many GPUs to buy and how to arrange them.
L17: > inference-fleet-sim fills that gap. It combines analytical M/G/c queueing with discrete-event simulation (DES) to find the minimum-cost fleet configuration that empirically meets a P99 TTFT SLO. It includes a physics-informed GPU performance model covering A10G, A100, and H100 across monolithic, two-pool-routed, and disaggregated topologies, all without requiring access to real hardware.
L18: We run the tool on seven fleet-planning scenarios drawn from two public workload traces (LMSYS, Azure) and one synthetic agent-heavy trace. Each one surfaces a result that simple analysis gets wrong -- the right split threshold, the cheapest GPU type, whether an apparently idle fleet is actually broken -- and shows why joint simulation of queueing, routing, and hardware is necessary to find it.
L19: Comments:  | Work in progress
L20: Subjects:  | Distributed, Parallel, and Cluster Computing (cs.DC)
L21: Cite as:  | cite12†arXiv:2603.16054 [cs.DC]
L22:    | (or cite13†arXiv:2603.16054v1 [cs.DC] for this version)
L23:    | cite14†https://doi.org/10.48550/arXiv.2603.16054†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Huamin Chen [cite15†view email ]
L27: [v1] Tue, 17 Mar 2026 01:44:04 UTC (20 KB)
L28: 
L29: Full-text links:
L30: 



[2603.16152v1] HIPO: Instruction Hierarchy via Constrained Reinforcement Learning (https://arxiv.org/abs/2603.16152v1)
citeturn25356view3 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16152v1","lineno":null}); Total lines: 166
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Machine Learning
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:HIPO: Instruction Hierarchy via Constrained Reinforcement Learning
L10: 
L11: Authors:cite5†Keru Chen , cite6†Jun Luo , cite7†Sen Lin , cite8†Yingbin Liang , cite9†Alvaro Velasquez , cite10†Nathaniel Bastian , cite11†Shaofeng Zou L12: 
L13: View a PDF of the paper titled HIPO: Instruction Hierarchy via Constrained Reinforcement Learning, by Keru Chen and 6 other authors
L14: 
L15: cite12†View PDF cite13†HTML (experimental) L16: > Abstract:Hierarchical Instruction Following (HIF) refers to the problem of prompting large language models with a priority-ordered stack of instructions. Standard methods like RLHF and DPO typically fail in this problem since they mainly optimize for a single objective, failing to explicitly enforce system prompt compliance. Meanwhile, supervised fine-tuning relies on mimicking filtered, compliant data, which fails to establish the priority asymmetry at the algorithmic level.
L17: In this paper, we introduce \textsc{HIPO}, a novel alignment framework that formulates HIF as a Constrained Markov Decision Process. \textsc{HIPO} elevates system prompts from mere input context to strict algorithmic boundaries. Using a primal-dual safe reinforcement learning approach, the algorithm dynamically enforces system prompt compliance as an explicit constraint, maximizing user utility strictly within this feasible region.
L18: Extensive evaluations across diverse model architectures (e.g., Qwen, Phi, Llama) demonstrate that \textsc{HIPO} significantly improves both system compliance and user utility. Furthermore, mechanistic analysis reveals that this constrained optimization autonomously drives the model to shift its attention toward long-range system tokens, providing a principled foundation for reliable LLM deployment in complex workflows.
L19: Comments:  | 9 pages + appendix. Under review
L20: Subjects:  | Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
L21: Cite as:  | cite14†arXiv:2603.16152 [cs.LG]
L22:    | (or cite15†arXiv:2603.16152v1 [cs.LG] for this version)
L23:    | cite16†https://doi.org/10.48550/arXiv.2603.16152†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 


[2603.16435v1] VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization (https://arxiv.org/abs/2603.16435v1)
citeturn25357view0 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16435v1","lineno":null}); Total lines: 158
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization
L10: 
L11: Authors:cite5†Yixuan Wang , cite6†Qingyu Shi , cite7†Jiayu Zhou , cite8†Dianbo Liu , cite9†Ziwei He , cite10†Zhouhan Lin L12: 
L13: View a PDF of the paper titled VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization, by Yixuan Wang and 5 other authors
L14: 
L15: cite11†View PDF cite12†HTML (experimental) L16: > Abstract:The growing context length of Large Language Models (LLMs) enlarges the Key-Value (KV) cache, limiting deployment in resource-limited environments. Prior training-free approaches for KV cache compression typically rely on low-rank approximation or scalar quantization, which fail to simultaneously achieve high compression ratios and high reconstruction fidelity.
L17: We propose VQKV, a novel, training-free method introducing vector quantization (VQ) to obtain highly compressed KV representations while preserving high model fidelity, allowing for the representation of thousands of floating-point values with just a few integer indices. As a result, VQKV achieves an 82.8\% compression ratio on LLaMA3.1-8B while retaining 98.6\% of the baseline performance on LongBench and enabling 4.3x longer generation length on the same memory footprint.
L18: Subjects:  | Computation and Language (cs.CL)
L19: Cite as:  | cite13†arXiv:2603.16435 [cs.CL]
L20:    | (or cite14†arXiv:2603.16435v1 [cs.CL] for this version)
L21:    | cite15†https://doi.org/10.48550/arXiv.2603.16435†doi.org arXiv-issued DOI via DataCite
L22: ## Submission history
L23: 
L24: From: Yixuan Wang [cite16†view email ]
L25: [v1] Tue, 17 Mar 2026 12:16:06 UTC (1,917 KB)
L26: 
L27: Full-text links:
L28: 
L29: ## Access Paper:
L30: 



[2603.16590v1] BATQuant: Outlier-resilient MXFP4 Quantization via Learnable Block-wise Optimization (https://arxiv.org/abs/2603.16590v1)
citeturn25357view1 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16590v1","lineno":null}); Total lines: 162
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:BATQuant: Outlier-resilient MXFP4 Quantization via Learnable Block-wise Optimization
L10: 
L11: Authors:cite5†Ji-Fu Li , cite6†Manyi Zhang , cite7†Xiaobo Xia , cite8†Han Bao , cite9†Haoli Bai , cite10†Zhenhua Dong , cite11†Xianzhi Yu L12: 
L13: View a PDF of the paper titled BATQuant: Outlier-resilient MXFP4 Quantization via Learnable Block-wise Optimization, by Ji-Fu Li and 6 other authors
L14: 
L15: cite12†View PDF cite13†HTML (experimental) L16: > Abstract:Microscaling floating-point (MXFP) formats have emerged as a promising standard for deploying Multi-modal Large Language Models (MLLMs) and Large Language Models (LLMs) on modern accelerator architectures. However, existing Post-Training Quantization (PTQ) methods, particularly rotation-based techniques designed for integer formats, suffer from severe performance collapse when applied to MXFP4.
L17: Recent studies attribute this failure to a fundamental format mismatch: global orthogonal rotations inadvertently transfer outlier energy across quantization blocks, inducing new outliers that disrupt local block-wise scaling, while often creating bimodal activation distributions that underutilize the limited quantization range.
L18: To address these issues, we propose BATQuant (Block-wise Affine Transformation), which restricts transformations to align with MXFP granularity to prevent cross-block outlier propagation, while relaxing orthogonality constraints to optimize distribution shaping. To ensure parameter efficiency, we introduce Global and Private Kronecker (GPK) decomposition to effectively reduces storage and runtime overhead and incorporate Block-wise Learnable Clipping to suppress residual outliers.
L19: Extensive experiments on both MLLMs and LLMs demonstrate that BATQuant establishes new state-of-the-art results under aggressive W4A4KV16 configurations, recovering up to 96.43% of full-precision performance on multimodal benchmarks and clearly outperforming existing methods across diverse tasks.
L20: Comments:  | 30 pages, 13 figures, 7 tables
L21: Subjects:  | Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
L22: Cite as:  | cite14†arXiv:2603.16590 [cs.CL]
L23:    | (or cite15†arXiv:2603.16590v1 [cs.CL] for this version)
L24:    | cite16†https://doi.org/10.48550/arXiv.2603.16590†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Xiaobo Xia [cite17†view email ]
L28: [v1] Tue, 17 Mar 2026 14:37:08 UTC (4,515 KB)
L29: 
L30: Full-text links:



[2603.15803v1] Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs (https://arxiv.org/abs/2603.15803v1)
citeturn25357view2 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.15803v1","lineno":null}); Total lines: 164
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Machine Learning
L7: 
L8: [Submitted on 16 Mar 2026]
L9: # Title:Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs
L10: 
L11: Authors:cite5†Linrui Ma , cite6†Yufei Cui , cite7†Kai Han , cite8†Yunhe Wang L12: 
L13: View a PDF of the paper titled Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs, by Linrui Ma and 3 other authors
L14: 
L15: cite9†View PDF cite10†HTML (experimental) L16: > Abstract:Discrete diffusion models offer global context awareness and flexible parallel generation. However, uniform random noise schedulers in standard DLLM training overlook the highly non-uniform information density inherent in real-world sequences. This wastes optimization resources on low-density structural glues while leaving high-density logical pivot points severely under-optimized. To address this, we propose an Information Density Driven Smart Noise Scheduler.
L17: By extracting information-dense hubs and applying Complementary Priority Masking, our method decouples a single training instance into mutually reinforcing reasoning and syntax samples, forcing the model to master both logical deduction and foundational sequence structure. Experiments demonstrate that our approach improves average accuracy by ~4\% across four Code and Math reasoning benchmarks, significantly outperforming uniform baselines.
L18: Mechanistic analyses further reveal that probabilistic priority masking effectively mitigates contextual collapse during block diffusion training. Overall, this density-aware strategy efficiently unlocks the reasoning potential of diffusion language models at minimal annotation cost, emerging as a promising new masked data training paradigm for Diffusion LLMs. Our processed dataset can be found at cite11†this https URL†huggingface.co .
L19: Comments:  | Ongoing work
L20: Subjects:  | Machine Learning (cs.LG)
L21: Cite as:  | cite12†arXiv:2603.15803 [cs.LG]
L22:    | (or cite13†arXiv:2603.15803v1 [cs.LG] for this version)
L23:    | cite14†https://doi.org/10.48550/arXiv.2603.15803†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Linrui Ma [cite15†view email ]
L27: [v1] Mon, 16 Mar 2026 18:33:43 UTC (524 KB)
L28: 
L29: Full-text links:
L30: 



[2603.16817v1] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights (https://arxiv.org/abs/2603.16817v1)
citeturn25357view3 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16817v1","lineno":null}); Total lines: 163
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Artificial Intelligence
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights
L10: 
L11: Authors:cite5†Yi Chen , cite6†Daiwei Chen , cite7†Sukrut Madhav Chikodikar , cite8†Caitlyn Heqi Yin , cite9†Ramya Korlakai Vinayak L12: 
L13: View a PDF of the paper titled Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights, by Yi Chen and 4 other authors
L14: 
L15: cite10†View PDF cite11†HTML (experimental) L16: > Abstract:Large language models (LLMs) frequently hallucinate, limiting their reliability in knowledge-intensive applications. Retrieval-augmented generation (RAG) and conformal factuality have emerged as potential ways to address this limitation. While RAG aims to ground responses in retrieved evidence, it provides no statistical guarantee that the final output is correct.
L17: Conformal factuality filtering offers distribution-free statistical reliability by scoring and filtering atomic claims using a threshold calibrated on held-out data, however, the informativeness of the final output is not guaranteed. We systematically analyze the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency. We propose novel informativeness-aware metrics that better reflect task utility under conformal filtering.
L18: Across three benchmarks and multiple model families, we find that (i) conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, (ii) conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions, and (iii) lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over $100\times$ fewer FLOPs.
L19: Overall, our results expose factuality-informativeness trade-offs and fragility of conformal filtering framework under distribution shifts and distractors, highlighting the need for new approaches for reliability with robustness and usefulness as key metrics, and provide actionable guidance for building RAG pipelines that are both reliable and computationally efficient.
L20: Comments:  | 56 pages
L21: Subjects:  | Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)
L22: Cite as:  | cite12†arXiv:2603.16817 [cs.AI]
L23:    | (or cite13†arXiv:2603.16817v1 [cs.AI] for this version)
L24:    | cite14†https://doi.org/10.48550/arXiv.2603.16817†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Yi Chen [cite15†view email ]
L28: [v1] Tue, 17 Mar 2026 17:20:08 UTC (16,968 KB)
L29: 
L30: Full-text links:


[2603.15831v1] Persona-Conditioned Risk Behavior in Large Language Models: A Simulated Gambling Study with GPT-4.1 (https://arxiv.org/abs/2603.15831v1)
citeturn25362view0 [wordlim: 200] Crawled: 3 weeks ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.15831v1","lineno":null}); Total lines: 162
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Artificial Intelligence
L7: 
L8: [Submitted on 16 Mar 2026]
L9: # Title:Persona-Conditioned Risk Behavior in Large Language Models: A Simulated Gambling Study with GPT-4.1
L10: 
L11: Authors:cite5†Sankalp Dubedy L12: 
L13: View a PDF of the paper titled Persona-Conditioned Risk Behavior in Large Language Models: A Simulated Gambling Study with GPT-4.1, by Sankalp Dubedy
L14: 
L15: cite6†View PDF cite7†HTML (experimental) L16: > Abstract:Large language models (LLMs) are increasingly deployed as autonomous agents in uncertain, sequential decision-making contexts. Yet it remains poorly understood whether the behaviors they exhibit in such environments reflect principled cognitive patterns or simply surface-level prompt mimicry.
L17: This paper presents a controlled experiment in which GPT-4.1 was assigned one of three socioeconomic personas (Rich, Middle-income, and Poor) and placed in a structured slot-machine environment with three distinct machine configurations: Fair (50%), Biased Low (35%), and Streak (dynamic probability increasing after consecutive losses).
L18: Across 50 independent iterations per condition and 6,950 recorded decisions, we find that the model reproduces key behavioral signatures predicted by Kahneman and Tversky's Prospect Theory without being instructed to do so. The Poor persona played a mean of 37.4 rounds per session (SD=15.5) compared to 1.1 rounds for the Rich persona (SD=0.31), a difference that is highly significant (Kruskal-Wallis H=393.5, p<2.2e-16). Risk scores by persona show large effect sizes (Cohen's d=4.15 for Poor vs Rich).
L19: Emotional labels appear to function as post-hoc annotations rather than decision drivers (chi-square=3205.4, Cramer's V=0.39), and belief-updating across rounds is negligible (Spearman rho=0.032 for Poor persona, p=0.016). These findings carry implications for LLM agent design, interpretability research, and the broader question of whether classical cognitive economic biases are implicitly encoded in large-scale pretrained language models.
L20: Comments:  | 21 pages, 13 figures, 9 tables. Independent research. Submitted to arXiv for open dissemination
L21: Subjects:  | Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
L22: Cite as:  | cite8†arXiv:2603.15831 [cs.AI]
L23:    | (or cite9†arXiv:2603.15831v1 [cs.AI] for this version)
L24:    | cite10†https://doi.org/10.48550/arXiv.2603.15831†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Sankalp Dubedy [cite11†view email ]
L28: [v1] Mon, 16 Mar 2026 19:03:19 UTC (688 KB)
L29: 
L30: Full-text links:



[2603.15909v1] Prompt Engineering for Scale Development in Generative Psychometrics (https://arxiv.org/abs/2603.15909v1)
citeturn25362view1 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.15909v1","lineno":null}); Total lines: 163
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Artificial Intelligence
L7: 
L8: [Submitted on 16 Mar 2026]
L9: # Title:Prompt Engineering for Scale Development in Generative Psychometrics
L10: 
L11: Authors:cite5†Lara Lee Russell-Lasalandra , cite6†Hudson Golino L12: 
L13: View a PDF of the paper titled Prompt Engineering for Scale Development in Generative Psychometrics, by Lara Lee Russell-Lasalandra and Hudson Golino
L14: 
L15: cite7†View PDF cite8†HTML (experimental) L16: > Abstract:This Monte Carlo simulation examines how prompt engineering strategies shape the quality of large language model (LLM)--generated personality assessment items within the AI-GENIE framework for generative psychometrics. Item pools targeting the Big Five traits were generated using multiple prompting designs (zero-shot, few-shot, persona-based, and adaptive), model temperatures, and LLMs, then evaluated and reduced using network psychometric methods.
L17: Across all conditions, AI-GENIE reliably improved structural validity following reduction, with the magnitude of its incremental contribution inversely related to the quality of the incoming item pool. Prompt design exerted a substantial influence on both pre- and post-reduction item quality.
L18: Adaptive prompting consistently outperformed non-adaptive strategies by sharply reducing semantic redundancy, elevating pre-reduction structural validity, and preserving substantially larger item pool, particularly when paired with newer, higher-capacity models. These gains were robust across temperature settings for most models, indicating that adaptive prompting mitigates common trade-offs between creativity and psychometric coherence.
L19: An exception was observed for the GPT-4o model at high temperatures, suggesting model-specific sensitivity to adaptive constraints at elevated stochasticity. Overall, the findings demonstrate that adaptive prompting is the strongest approach in this context, and that its benefits scale with model capability, motivating continued investigation of model--prompt interactions in generative psychometric pipelines.
L20: Comments:  | 22 pages, 7 figures
L21: Subjects:  | Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC)
L22: Cite as:  | cite9†arXiv:2603.15909 [cs.AI]
L23:    | (or cite10†arXiv:2603.15909v1 [cs.AI] for this version)
L24:    | cite11†https://doi.org/10.48550/arXiv.2603.15909†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Hudson Golino [cite12†view email ]
L28: [v1] Mon, 16 Mar 2026 20:55:17 UTC (3,260 KB)
L29: 
L30: Full-text links:



[2603.15797v1] OMNIFLOW: A Physics-Grounded Multimodal Agent for Generalized Scientific Reasoning (https://arxiv.org/abs/2603.15797v1)
citeturn25362view2 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.15797v1","lineno":null}); Total lines: 166
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Machine Learning
L7: 
L8: [Submitted on 16 Mar 2026 (this version), latest version 18 Mar 2026 (cite5†v2 )]
L9: # Title:OMNIFLOW: A Physics-Grounded Multimodal Agent for Generalized Scientific Reasoning
L10: 
L11: Authors:cite6†Hao Wu , cite7†Yongheng Zhang , cite8†Yuan Gao , cite9†Fan Xu , cite10†Fan Zhang , cite11†Ruobing Xie , cite12†Ruijian Gou , cite13†Yuxuan Liang , cite14†Xiaomeng Huang , cite15†Xian Wu L12: 
L13: View a PDF of the paper titled OMNIFLOW: A Physics-Grounded Multimodal Agent for Generalized Scientific Reasoning, by Hao Wu and 9 other authors
L14: 
L15: cite16†View PDF cite17†HTML (experimental) L16: > Abstract:Large Language Models (LLMs) have demonstrated exceptional logical reasoning capabilities but frequently struggle with the continuous spatiotemporal dynamics governed by Partial Differential Equations (PDEs), often resulting in non-physical hallucinations. Existing approaches typically resort to costly, domain-specific fine-tuning, which severely limits cross-domain generalization and interpretability.
L17: To bridge this gap, we propose OMNIFLOW, a neuro-symbolic architecture designed to ground frozen multimodal LLMs in fundamental physical laws without requiring domain-specific parameter updates. OMNIFLOW introduces a novel \textit{Semantic-Symbolic Alignment} mechanism that projects high-dimensional flow tensors into topological linguistic descriptors, enabling the model to perceive physical structures rather than raw pixel values.
L18: Furthermore, we construct a Physics-Guided Chain-of-Thought (PG-CoT) workflow that orchestrates reasoning through dynamic constraint injection (e.g., mass conservation) and iterative reflexive verification. We evaluate OMNIFLOW on a comprehensive benchmark spanning microscopic turbulence, theoretical Navier-Stokes equations, and macroscopic global weather forecasting.
L19: Empirical results demonstrate that OMNIFLOW significantly outperforms traditional deep learning baselines in zero-shot generalization and few-shot adaptation tasks. Crucially, it offers transparent, physically consistent reasoning reports, marking a paradigm shift from black-box fitting to interpretable scientific reasoning.
L20: Subjects:  | Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
L21: Cite as:  | cite18†arXiv:2603.15797 [cs.LG]
L22:    | (or cite19†arXiv:2603.15797v1 [cs.LG] for this version)
L23:    | cite20†https://doi.org/10.48550/arXiv.2603.15797†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Hao Wu [cite21†view email ]
L27: [v1] Mon, 16 Mar 2026 18:29:01 UTC (4,051 KB)
L28: cite5†[v2] Wed, 18 Mar 2026 09:11:28 UTC (4,051 KB)
L29: 
L30: Full-text links:



[2603.16131v1] SciZoom: A Large-scale Benchmark for Hierarchical Scientific Summarization across the LLM Era (https://arxiv.org/abs/2603.16131v1)
citeturn25362view3 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16131v1","lineno":null}); Total lines: 162
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computation and Language
L7: 
L8: [Submitted on 17 Mar 2026 (this version), latest version 23 Jun 2026 (cite5†v2 )]
L9: # Title:SciZoom: A Large-scale Benchmark for Hierarchical Scientific Summarization across the LLM Era
L10: 
L11: Authors:cite6†Han Jang , cite7†Junhyeok Lee , cite8†Kyu Sung Choi L12: 
L13: View a PDF of the paper titled SciZoom: A Large-scale Benchmark for Hierarchical Scientific Summarization across the LLM Era, by Han Jang and 2 other authors
L14: 
L15: cite9†View PDF cite10†HTML (experimental) L16: > Abstract:The explosive growth of AI research has created unprecedented information overload, increasing the demand for scientific summarization at multiple levels of granularity beyond traditional abstracts. While LLMs are increasingly adopted for summarization, existing benchmarks remain limited in scale, target only a single granularity, and predate the LLM era.
L17: Moreover, since the release of ChatGPT in November 2022, researchers have rapidly adopted LLMs for drafting manuscripts themselves, fundamentally transforming scientific writing, yet no resource exists to analyze how this writing has evolved. To bridge these gaps, we introduce SciZoom, a benchmark comprising 44,946 papers from four top-tier ML venues (NeurIPS, ICLR, ICML, EMNLP) spanning 2020 to 2025, explicitly stratified into Pre-LLM and Post-LLM eras.
L18: SciZoom provides three hierarchical summarization targets (Abstract, Contributions, and TL;DR) achieving compression ratios up to 600:1, enabling both multi-granularity summarization research and temporal mining of scientific writing patterns. Our linguistic analysis reveals striking shifts in phrase patterns (up to 10x for formulaic expressions) and rhetorical style (23% decline in hedging), suggesting that LLM-assisted writing produces more confident yet homogenized prose.
L19: SciZoom serves as both a challenging benchmark and a unique resource for mining the evolution of scientific discourse in the generative AI era. Our code and dataset are publicly available on GitHub (cite11†this https URL†github.com ) and Hugging Face (cite12†this https URL†huggingface.co ), respectively.
L20: Comments:  | 12 pages, 7 figures, Submitted to KDD 2026
L21: Subjects:  | Computation and Language (cs.CL)
L22: Cite as:  | cite13†arXiv:2603.16131 [cs.CL]
L23:    | (or cite14†arXiv:2603.16131v1 [cs.CL] for this version)
L24:    | cite15†https://doi.org/10.48550/arXiv.2603.16131†doi.org arXiv-issued DOI via DataCite
L25: ## Submission history
L26: 
L27: From: Han Jang [cite16†view email ]
L28: [v1] Tue, 17 Mar 2026 05:34:46 UTC (1,934 KB)
L29: cite5†[v2] Tue, 23 Jun 2026 13:43:37 UTC (969 KB)
L30: 

[2603.16666v1] Fast-WAM: Do World Action Models Need Test-time Future Imagination? (https://arxiv.org/abs/2603.16666v1)
citeturn25382view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16666v1","lineno":null}); Total lines: 162
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computer Vision and Pattern Recognition
L7: 
L8: [Submitted on 17 Mar 2026 (this version), latest version 23 Mar 2026 (cite5†v2 )]
L9: # Title:Fast-WAM: Do World Action Models Need Test-time Future Imagination?
L10: 
L11: Authors:cite6†Tianyuan Yuan , cite7†Zibin Dong , cite8†Yicheng Liu , cite9†Hang Zhao L12: 
L13: View a PDF of the paper titled Fast-WAM: Do World Action Models Need Test-time Future Imagination?, by Tianyuan Yuan and 3 other authors
L14: 
L15: cite10†View PDF cite11†HTML (experimental) L16: > Abstract:World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance.
L17: In this paper, we ask whether WAMs need explicit future imagination at test time, or whether their benefit comes primarily from video modeling during training. We disentangle the role of video modeling during training from explicit future generation during inference by proposing \textbf{Fast-WAM}, a WAM architecture that retains video co-training during training but skips future prediction at test time. We further instantiate several Fast-WAM variants to enable a controlled comparison of these two factors.
L18: Across these variants, we find that Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. Empirically, Fast-WAM achieves competitive results with state-of-the-art methods both on simulation benchmarks (LIBERO and RoboTwin) and real-world tasks, without embodied pretraining. It runs in real time with 190ms latency, over 4$\times$ faster than existing imagine-then-execute WAMs.
L19: These results suggest that the main value of video prediction in WAMs may lie in improving world representations during training rather than generating future observations at test time. Project page: cite12†this https URL†yuantianyuan01.github.io L20: Subjects:  | Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)
L21: Cite as:  | cite13†arXiv:2603.16666 [cs.CV]
L22:    | (or cite14†arXiv:2603.16666v1 [cs.CV] for this version)
L23:    | cite15†https://doi.org/10.48550/arXiv.2603.16666†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Tianyuan Yuan [cite16†view email ]
L27: [v1] Tue, 17 Mar 2026 15:33:43 UTC (2,613 KB)
L28: cite5†[v2] Mon, 23 Mar 2026 05:41:14 UTC (2,550 KB)
L29: 
L30: Full-text links:



[2603.16860v1] DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models (https://arxiv.org/abs/2603.16860v1)
citeturn25382view1 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16860v1","lineno":null}); Total lines: 160
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Robotics
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models
L10: 
L11: Authors:cite5†Emily Yue-Ting Jia , cite6†Weiduo Yuan , cite7†Tianheng Shi , cite8†Vitor Guizilini , cite9†Jiageng Mao , cite10†Yue Wang L12: 
L13: View a PDF of the paper titled DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models, by Emily Yue-Ting Jia and 5 other authors
L14: 
L15: cite11†View PDF cite12†HTML (experimental) L16: > Abstract:Robotic manipulation requires sophisticated commonsense reasoning, a capability naturally possessed by large-scale Vision-Language Models (VLMs). While VLMs show promise as zero-shot planners, their lack of grounded physical understanding often leads to compounding errors and low success rates when deployed in complex real-world environments, particularly for challenging tasks like deformable object manipulation.
L17: Although Reinforcement Learning (RL) can adapt these planners to specific task dynamics, directly fine-tuning VLMs via real-world interaction is prohibitively expensive, unsafe, and sample-inefficient. To overcome this bottleneck, we introduce DreamPlan, a novel framework for the reinforcement fine-tuning of VLM planners via video world models. Instead of relying on costly physical rollouts, DreamPlan first leverages the zero-shot VLM to collect exploratory interaction data.
L18: We demonstrate that this sub-optimal data is sufficient to train an action-conditioned video generation model, which implicitly captures complex real-world physics. Subsequently, the VLM planner is fine-tuned entirely within the "imagination" of this video world model using Odds Ratio Policy Optimization (ORPO). By utilizing these virtual rollouts, physical and task-specific knowledge is efficiently injected into the VLM.
L19: Our results indicate that DreamPlan bridges the gap between semantic reasoning and physical grounding, significantly improving manipulation success rates without the need for large-scale real-world data collection. Our project page is cite13†this https URL†psi-lab.ai .
L20: Subjects:  | Robotics (cs.RO)
L21: Cite as:  | cite14†arXiv:2603.16860 [cs.RO]
L22:    | (or cite15†arXiv:2603.16860v1 [cs.RO] for this version)
L23:    | cite16†https://doi.org/10.48550/arXiv.2603.16860†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Emily Jia [cite17†view email ]
L27: [v1] Tue, 17 Mar 2026 17:59:00 UTC (5,517 KB)
L28: 
L29: Full-text links:
L30: 



[2603.16871v1] WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation (https://arxiv.org/abs/2603.16871v1)
citeturn25382view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/abs/2603.16871v1","lineno":null}); Total lines: 160
L0: cite0†Search cite1†Submit cite2†Donate†info.arxiv.org cite3†Log in L1: 
L2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]
L3: 
L4: Press Enter to search · cite4†Advanced search L5: 
L6: # Computer Science > Computer Vision and Pattern Recognition
L7: 
L8: [Submitted on 17 Mar 2026]
L9: # Title:WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation
L10: 
L11: Authors:cite5†Jisu Nam , cite6†Yicong Hong , cite7†Chun-Hao Paul Huang , cite8†Feng Liu , cite9†JoungBin Lee , cite10†Jiyoung Kim , cite11†Siyoon Jin , cite12†Yunsung Lee , cite13†Jaeyoon Jung , cite14†Suhwan Choi , cite15†Seungryong Kim , cite16†Yang Zhou L12: View a PDF of the paper titled WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation, by Jisu Nam and 11 other authors
L13: 
L14: cite17†View PDF cite18†HTML (experimental) L15: > Abstract:Recent advances in video diffusion transformers have enabled interactive gaming world models that allow users to explore generated environments over extended horizons. However, existing approaches struggle with precise action control and long-horizon 3D consistency.
L16: Most prior works treat user actions as abstract conditioning signals, overlooking the fundamental geometric coupling between actions and the 3D world, whereby actions induce relative camera motions that accumulate into a global camera pose within a 3D world. In this paper, we establish camera pose as a unifying geometric representation to jointly ground immediate action control and long-term 3D consistency.
L17: First, we define a physics-based continuous action space and represent user inputs in the Lie algebra to derive precise 6-DoF camera poses, which are injected into the generative model via a camera embedder to ensure accurate action alignment. Second, we use global camera poses as spatial indices to retrieve relevant past observations, enabling geometrically consistent revisiting of locations during long-horizon navigation.
L18: To support this research, we introduce a large-scale dataset comprising 3,000 minutes of authentic human gameplay annotated with camera trajectories and textual descriptions. Extensive experiments show that our approach substantially outperforms state-of-the-art interactive gaming world models in action controllability, long-horizon visual quality, and 3D spatial consistency.
L19: Comments:  | Project page is available at cite19†this https URL†cvlab-kaist.github.io L20: Subjects:  | Computer Vision and Pattern Recognition (cs.CV)
L21: Cite as:  | cite20†arXiv:2603.16871 [cs.CV]
L22:    | (or cite21†arXiv:2603.16871v1 [cs.CV] for this version)
L23:    | cite22†https://doi.org/10.48550/arXiv.2603.16871†doi.org arXiv-issued DOI via DataCite
L24: ## Submission history
L25: 
L26: From: Jisu Nam [cite23†view email ]
L27: [v1] Tue, 17 Mar 2026 17:59:56 UTC (6,926 KB)
L28: 
L29: Full-text links:
L30: 



Internal Error ()
citeturn25382view3 [wordlim: 200] Source: open({"ref_id":"https://arxiv.org/abs/2603.16068v1","lineno":null}); Total lines: 1
L0: Failed to fetch https://arxiv.org/abs/2603.16068v1: Cache miss
 

16068v1官方原HTML单次恢复：
```json
{
  "url": "https://arxiv.org/abs/2603.16068v1",
  "title": [
    "Resource Consumption Threats in Large Language Models"
  ],
  "abstract": "Abstract: Given limited and costly computational infrastructure, resource efficiency is a key requirement for large language models (LLMs). Efficient LLMs increase service capacity for providers and reduce latency and API costs for users. Recent resource consumption threats induce excessive generation, degrading model efficiency and harming both service availability and economic sustainability. This survey presents a systematic review of threats to resource consumption in LLMs. We further establish a unified view of this emerging area by clarifying its scope and examining the problem along the full pipeline from threat induction to mechanism understanding and mitigation. Our goal is to clarify the problem landscape for this emerging area, thereby providing a clearer foundation for characterization and mitigation.",
  "history": [
    "[v1]</strong>",
    "[v2]</a></strong>",
    "[v3]</a></strong>"
  ],
  "withdraw": []
}
```
