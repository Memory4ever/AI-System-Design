# 2026-01-30 首批准入校准（作者初判，未冻结）

最终修正：以下保留初判与原题摘，不是最终池。root实际12完整题摘校准：Drift/LogSieve成熟诊断/日志过滤未给新增选择边界，贡献EX；MeCo按186–221 task/motion-reuse定义重开5并完成必要评价；PILOT新增局部机制Durability2不借长期planning原则。早Submitted的19910/19917/19921日期精确隔离，不能由Created+通常schedule定day。最终唯一判断与63冻结池见本日README，原反证保留。

窗口：2026-01-29T09:00:00+08:00 ～ 2026-01-30T09:00:00+08:00。

90为一个窄窗主题query标题线索，不是候选分母；全部12份以下原始v1完整题摘已读，不先深审。元数据firstpublic上界与官方schedule仅组成包络，不写Created为精确公开时刻。90条metadata完整存V3_TOPIC_TITLE_RAW.jsonl；其余来源/主题还在有限处理。v1官方页当前Comments包含后续接受信息，不当窗内事件。

## 2601.20332 — Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching

原始页：https://arxiv.org/abs/2601.20332v1

拟准入：全序列反复去噪带来冗余→观察prefix-local活跃token、已解码token暂态稳定并用active/buffer/farfield滑窗复用→重考虑无需重训的DLM计算/质量取舍。2+2+3=7。99x不是已采用结论。

原始完整题摘（以下原文不作为结论）：

Abstract:Diffusion language models (DLMs) generate text through iterative denoising, but inference requires full-sequence attention at every iteration, resulting in substantial redundant computation on masked tokens. Block-wise diffusion can reduce this cost, yet it typically relies on retraining and constrained update orders, limiting its direct applicability to pretrained DLMs. Our token-level analysis reveals pronounced structural locality in DLM inference. Decoding is driven by a small set of prefix-localized active tokens; the influence of distant undecoded context diminishes rapidly, and decoded tokens exhibit stage-wise temporal stability, enabling reuse of intermediate representations except for a brief post-decode transient. Motivated by these observations, we propose \textbf{\placeholder}\footnote{The source code is available at this https URL.}, a window-based token pruning and caching method for inference. We maintain a local computation window that slides rightward as denoising progresses, and partition undecoded tokens into: (i) \textit{active tokens} that are computed online, (ii) \textit{buffer tokens} whose KV states are cached and periodically refreshed, and (iii) \textit{far-field tokens} that are pruned outside the window. Computation is restricted to active and buffer tokens within the window, while far-field tokens are omitted at each stage. Experiments on LLaDA and Dream show that, under matched compute budgets, our method achieves up to $99\times$ inference speedup while largely preserving generation performance.

本日日期原值：{"created":"2026-01-29T02:50:30Z","v1_dates":[{"date":"2026-01-28T07:49:20Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:29:43Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.19910 — Understanding Bottlenecks for Efficiently Serving LLM Inference With KV Offloading

原始页：https://arxiv.org/abs/2601.19910v1

拟准入：CPU KV容量不能等同服务可行性→提出cached/prefill临界比与具体传输瓶颈→重考虑offload负载与互联选择。2+2+3=7。Submitted为2025/12不直接当旧公开；ID本月和DataCite v1生成及schedule共同支持本窗包络。

原始完整题摘（以下原文不作为结论）：

Abstract:KV cache offloading enables long-context LLM inference by storing caches in CPU DRAM, but PCIe bandwidth limitations create severe bottlenecks. In this paper, we develops an analytical framework that derives $\kappa_{\text{crit}}$, the critical cached-to-prefill token ratio where execution becomes memory-bound and show typical workloads exceed this threshold by orders of magnitude. Empirical characterization reveals 99\% of latency spent on transfers and serving offloaded requests results in GPU's consuming only 28\% of their rated TDP, motivating our proposed optimizations for hardware interconnects, model architectures, and scheduling algorithms.
Comments:
Submitted to MLSys 2026

本日日期原值：{"created":"2026-01-29T02:40:30Z","v1_dates":[{"date":"2025-12-16T19:29:13Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:00:23Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20309 — SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips

原始页：https://arxiv.org/abs/2601.20309v1

拟准入：高并发KV预算不足造成HOL且PCIe不足以满足SLO→主动轮转RotaSched+全双工NVLink-C2C状态搬运→重考虑superchip上TTFT/TBT与状态驻留的联合策略。2+3+2=7。

原始完整题摘（以下原文不作为结论）：

Abstract:Large Language Model (LLM) serving faces a fundamental tension between stringent latency Service Level Objectives (SLOs) and limited GPU memory capacity. When high request rates exhaust the KV cache budget, existing LLM inference systems often suffer severe head-of-line (HOL) blocking. While prior work explored PCIe-based offloading, these approaches cannot sustain responsiveness under high request rates, often failing to meet tight Time-To-First-Token (TTFT) and Time-Between-Tokens (TBT) SLOs. We present SuperInfer, a high-performance LLM inference system designed for emerging Superchips (e.g., NVIDIA GH200) with tightly coupled GPU-CPU architecture via NVLink-C2C. SuperInfer introduces RotaSched, the first proactive, SLO-aware rotary scheduler that rotates requests to maintain responsiveness on Superchips, and DuplexKV, an optimized rotation engine that enables full-duplex transfer over NVLink-C2C. Evaluations on GH200 using various models and datasets show that SuperInfer improves TTFT SLO attainment rates by up to 74.7% while maintaining comparable TBT and throughput compared to state-of-the-art systems, demonstrating that SLO-aware scheduling and memory co-design unlocks the full potential of Superchips for responsive LLM serving.
Comments:
Accepted by MLSys '26

本日日期原值：{"created":"2026-01-29T02:49:57Z","v1_dates":[{"date":"2026-01-28T07:01:46Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:27:32Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20267 — SATA: Sparsity-Aware Scheduling for Selective Token Attention

原始页：https://arxiv.org/abs/2601.20267v1

拟准入：稀疏attention算术减少仍受分散访问制约→重排operand流并提前fetch/retire Q/K中间向量→重考虑稀疏算法与执行调度耦合。2+2+2=6；待证据确认实际foundation/model trace适用边界。

原始完整题摘（以下原文不作为结论）：

Abstract:Transformers have become the foundation of numerous state-of-the-art AI models across diverse domains, thanks to their powerful attention mechanism for modeling long-range dependencies. However, the quadratic scaling complexity of attention poses significant challenges for efficient hardware implementation. While techniques such as quantization and pruning help mitigate this issue, selective token attention offers a promising alternative by narrowing the attention scope to only the most relevant tokens, reducing computation and filtering out noise.
In this work, we propose SATA, a locality-centric dynamic scheduling scheme that proactively manages sparsely distributed access patterns from selective Query-Key operations. By reordering operand flow and exploiting data locality, our approach enables early fetch and retirement of intermediate Query/Key vectors, improving system utilization. We implement and evaluate our token management strategy in a control and compute system, using runtime traces from selective-attention-based models. Experimental results show that our method improves system throughput by up to 1.76x and boosts energy efficiency by 2.94x, while incurring minimal scheduling overhead.
Comments:
This paper has been accepted to DATE 2026

本日日期原值：{"created":"2026-01-29T02:48:57Z","v1_dates":[{"date":"2026-01-28T05:20:07Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:23:27Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.19917 — PILOT: Planning via Internalized Latent Optimization Trajectories for Large Language Models

原始页：https://arxiv.org/abs/2601.19917v1

拟准入：小模型跨步推理依赖外部teacher planning增加在线成本→query-conditioned hypernetwork latent guidance而冻结backbone→重考虑teacher指导如何前移至内生推理。2+2+3=7。

原始完整题摘（以下原文不作为结论）：

Abstract:Strategic planning is critical for multi-step reasoning, yet compact Large Language Models (LLMs) often lack the capacity to formulate global strategies, leading to error propagation in long-horizon tasks. Our analysis reveals that LLMs possess latent reasoning capabilities that can be unlocked when conditioned on explicit plans from a teacher model; however, runtime reliance on external guidance is often impractical due to latency and availability constraints. To bridge this gap, we propose PILOT (Planning via Internalized Latent Optimization Trajectories), a non-invasive framework designed to internalize the strategic oversight of large models into intrinsic Latent Guidance. Instead of altering backbone weights, PILOT employs a lightweight Hyper-Network to synthesize a query-conditioned Latent Guidance vector. This vector acts as an internal steering mechanism, guiding the model's representations toward optimal reasoning paths. Extensive experiments on mathematical and coding benchmarks demonstrate that PILOT effectively stabilizes reasoning trajectories, consistently outperforming strong baselines (e.g., +8.9% on MATH500) with negligible inference latency.

本日日期原值：{"created":"2026-01-29T02:40:40Z","v1_dates":[{"date":"2026-01-07T12:38:56Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:00:32Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20577 — MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization

原始页：https://arxiv.org/abs/2601.20577v1

准入事实未明：cache/reuse及新相似度方法尚未在题摘给出判别边界；只定点看similarity定义与环境状态变化如何处理，然后判断，不因新benchmark或机器人场景收。

原始完整题摘（以下原文不作为结论）：

Abstract:Multi-robot systems have been widely deployed in real-world applications, providing significant improvements in efficiency and reductions in labor costs. However, most existing multi-robot collaboration methods rely on extensive task-specific training, which limits their adaptability to new or diverse scenarios. Recent research leverages the language understanding and reasoning capabilities of large language models (LLMs) to enable more flexible collaboration without specialized training. Yet, current LLM-empowered approaches remain inefficient: when confronted with identical or similar tasks, they must replan from scratch because they omit task-level similarities. To address this limitation, we propose MeCo, a similarity-aware multi-robot collaboration framework that applies the principle of ``cache and reuse'' (a.k.a., memoization) to reduce redundant computation. Unlike simple task repetition, identifying and reusing solutions for similar but not identical tasks is far more challenging, particularly in multi-robot settings. To this end, MeCo introduces a new similarity testing method that retrieves previously solved tasks with high relevance, enabling effective plan reuse without re-invoking LLMs. Furthermore, we present MeCoBench, the first benchmark designed to evaluate performance on similar-task collaboration scenarios. Experimental results show that MeCo substantially reduces planning costs and improves success rates compared with state-of-the-art approaches.

本日日期原值：{"created":"2026-01-29T02:56:08Z","v1_dates":[{"date":"2026-01-28T13:15:58Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:45:27Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20433 — MARE: Multimodal Alignment and Reinforcement for Explainable Deepfake Detection via Vision-Language Models

原始页：https://arxiv.org/abs/2601.20433v1

贡献关闭：完整题摘是deepfake场景中alignment+RLHF奖励+forgery模块组合、局部准确率/可靠性；未说明通用VLM机制、原方案失效条件或足以修正设计的反证。官方v1页无相关撤回/纠错信号。

原始完整题摘（以下原文不作为结论）：

Abstract:Deepfake detection is a widely researched topic that is crucial for combating the spread of malicious content, with existing methods mainly modeling the problem as classification or spatial localization. The rapid advancements in generative models impose new demands on Deepfake detection. In this paper, we propose multimodal alignment and reinforcement for explainable Deepfake detection via vision-language models, termed MARE, which aims to enhance the accuracy and reliability of Vision-Language Models (VLMs) in Deepfake detection and reasoning. Specifically, MARE designs comprehensive reward functions, incorporating reinforcement learning from human feedback (RLHF), to incentivize the generation of text-spatially aligned reasoning content that adheres to human preferences. Besides, MARE introduces a forgery disentanglement module to capture intrinsic forgery traces from high-level facial semantics, thereby improving its authenticity detection capability. We conduct thorough evaluations on the reasoning content generated by MARE. Both quantitative and qualitative experimental results demonstrate that MARE achieves state-of-the-art performance in terms of accuracy and reliability.

本日日期原值：{"created":"2026-01-29T02:52:50Z","v1_dates":[{"date":"2026-01-28T09:44:31Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:35:43Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20048 — Insight Agents: An LLM-Based Multi-Agent System for Data Insights

原始页：https://arxiv.org/abs/2601.20048v1

贡献关闭：e-commerce域的成熟plan/execute+manager routing+两worker/API拆解配方与90%/P90数字，没有新执行保证、失效机制或模块收益成立边界。且SIGIR2025发表先公开线索只在必要时恢复；贡献明确不收，日期未核实后停。

原始完整题摘（以下原文不作为结论）：

Abstract:Today, E-commerce sellers face several key challenges, including difficulties in discovering and effectively utilizing available programs and tools, and struggling to understand and utilize rich data from various tools. We therefore aim to develop Insight Agents (IA), a conversational multi-agent Data Insight system, to provide E-commerce sellers with personalized data and business insights through automated information retrieval. Our hypothesis is that IA will serve as a force multiplier for sellers, thereby driving incremental seller adoption by reducing the effort required and increase speed at which sellers make good business decisions. In this paper, we introduce this novel LLM-backed end-to-end agentic system built on a plan-and-execute paradigm and designed for comprehensive coverage, high accuracy, and low latency. It features a hierarchical multi-agent structure, consisting of manager agent and two worker agents: data presentation and insight generation, for efficient information retrieval and problem-solving. We design a simple yet effective ML solution for manager agent that combines Out-of-Domain (OOD) detection using a lightweight encoder-decoder model and agent routing through a BERT-based classifier, optimizing both accuracy and latency. Within the two worker agents, a strategic planning is designed for API-based data model that breaks down queries into granular components to generate more accurate responses, and domain knowledge is dynamically injected to to enhance the insight generator. IA has been launched for Amazon sellers in US, which has achieved high accuracy of 90% based on human evaluation, with latency of P90 below 15s.
Comments:
Accepted to SIGIR 2025. DOI: https://doi.org/10.1145/3726302.3731959

本日日期原值：{"created":"2026-01-29T02:43:43Z","v1_dates":[{"date":"2026-01-27T20:51:01Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:06:31Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20148 — LogSieve: Task-Aware CI Log Reduction for Sustainable LLM-Based Analysis

原始页：https://arxiv.org/abs/2601.20148v1

初拟贡献关闭供校准：CI日志semantics-aware过滤减少token并保留局部语义，是成熟过滤/分类配方的领域评价；摘要未新增可复用token质量阈值或失败机制，且energy为按token比例推断，不把该比例当实际端到端收益。请特别检查是否应按可比质量/资源边界准入。

原始完整题摘（以下原文不作为结论）：

Abstract:Logs are essential for understanding Continuous Integration (CI) behavior, particularly for diagnosing build failures and performance regressions. Yet their growing volume and verbosity make both manual inspection and automated analysis increasingly costly, time-consuming, and environmentally costly. While prior work has explored log compression, anomaly detection, and LLM-based log analysis, most efforts target structured system logs rather than the unstructured, noisy, and verbose logs typical of CI workflows.
We present LogSieve, a lightweight, RCA-aware and semantics-preserving log reduction technique that filters low-information lines while retaining content relevant to downstream reasoning. Evaluated on CI logs from 20 open-source Android projects using GitHub Actions, LogSieve achieves an average 42% reduction in lines and 40% reduction in tokens with minimal semantic loss. This pre-inference reduction lowers computational cost and can proportionally reduce energy use (and associated emissions) by decreasing the volume of data processed during LLM inference.
Compared with structure-first baselines (LogZip and random-line removal), LogSieve preserves much higher semantic and categorical fidelity (Cosine = 0.93, GPTScore = 0.93, 80% exact-match accuracy). Embedding-based classifiers automate relevance detection with near-human accuracy (97%), enabling scalable and sustainable integration of semantics-aware filtering into CI workflows. LogSieve thus bridges log management and LLM reasoning, offering a practical path toward greener and more interpretable CI automation.
Comments:
Preprint. Accepted for presentation at Mining Software Repositories (MSR'26), co-located ICSE 2026. The final version will appear in the ACM Digital Library as part of the MSR'26 conference proceedings

本日日期原值：{"created":"2026-01-29T02:46:09Z","v1_dates":[{"date":"2026-01-28T00:49:50Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:12:17Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.20094 — T-Mimi: A Transformer-based Mimi Decoder for Real-Time On-Phone TTS

原始页：https://arxiv.org/abs/2601.20094v1

拟准入：Mimi的deconv在XNNPACK/mobile CPU并非低延迟→纯Transformer decoder替代与靠近waveform层量化敏感性→重考虑音频codec架构与端侧精度分配。2+2+2=6。

原始完整题摘（以下原文不作为结论）：

Abstract:Neural audio codecs provide promising acoustic features for speech synthesis, with representative streaming codecs like Mimi providing high-quality acoustic features for real-time Text-to-Speech (TTS) applications. However, Mimi's decoder, which employs a hybrid transformer and convolution architecture, introduces significant latency bottlenecks on edge devices due to the the compute intensive nature of deconvolution layers which are not friendly for mobile-CPUs, such as the most representative framework XNNPACK. This paper introduces T-Mimi, a novel modification of the Mimi codec decoder that replaces its convolutional components with a purely transformer-based decoder, inspired by the TS3-Codec architecture. This change dramatically reduces on-device TTS latency from 42.1ms to just 4.4ms. Furthermore, we conduct quantization aware training and derive a crucial finding: the final two transformer layers and the concluding linear layers of the decoder, which are close to the waveform, are highly sensitive to quantization and must be preserved at full precision to maintain audio quality.
Comments:
Accepted by ICASSP 2026

本日日期原值：{"created":"2026-01-29T02:44:47Z","v1_dates":[{"date":"2026-01-27T22:27:40Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:09:09Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.19921 — Demystifying Multi-Agent Debate: The Role of Confidence and Diversity

原始页：https://arxiv.org/abs/2601.19921v1

拟准入：同质agent均匀update的MAD可能不优于majority→候选多样性初始化与显式校准confidence更新分别改变初始正确率/漂移→重考虑增加通信前是否具备有效信号。2+2+3=7。

原始完整题摘（以下原文不作为结论）：

Abstract:Multi-agent debate (MAD) is widely used to improve large language model (LLM) performance through test-time scaling, yet recent work shows that vanilla MAD often underperforms simple majority vote despite higher computational cost. Studies show that, under homogeneous agents and uniform belief updates, debate preserves expected correctness and therefore cannot reliably improve outcomes. Drawing on findings from human deliberation and collective decision-making, we identify two key mechanisms missing from vanilla MAD: (i) diversity of initial viewpoints and (ii) explicit, calibrated confidence communication. We propose two lightweight interventions. First, a diversity-aware initialisation that selects a more diverse pool of candidate answers, increasing the likelihood that a correct hypothesis is present at the start of debate. Second, a confidence-modulated debate protocol in which agents express calibrated confidence and condition their updates on others' confidence. We show theoretically that diversity-aware initialisation improves the prior probability of MAD success without changing the underlying update dynamics, while confidence-modulated updates enable debate to systematically drift to the correct hypothesis. Empirically, across six reasoning-oriented QA benchmarks, our methods consistently outperform vanilla MAD and majority vote. Our results connect human deliberation with LLM-based debate and demonstrate that simple, principled modifications can substantially enhance debate effectiveness.

本日日期原值：{"created":"2026-01-29T02:40:46Z","v1_dates":[{"date":"2026-01-09T02:38:30Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:00:38Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}

## 2601.19934 — Quantifying non deterministic drift in large language models

原始页：https://arxiv.org/abs/2601.19934v1

拟准入：固定temperature常被误当repeatability保证→跨两个实际model/deployment反复运行量化temp0行为漂移→重考虑重复性评价及解码接口保证。2+2+2=6；不以两种部署推model-size因果。

原始完整题摘（以下原文不作为结论）：

Abstract:Large language models (LLMs) are widely used for tasks ranging from summarisation to decision support. In practice, identical prompts do not always produce identical outputs, even when temperature and other decoding parameters are fixed. In this work, we conduct repeated-run experiments to empirically quantify baseline behavioural drift, defined as output variability observed when the same prompt is issued multiple times under operator-free conditions. We evaluate two publicly accessible models, gpt-4o-mini and llama3.1-8b, across five prompt categories using exact repeats, perturbed inputs, and reuse modes at temperatures of 0.0 and 0.7. Drift is measured using unique output fractions, lexical similarity, and word count statistics, enabling direct comparison across models, prompting modes, and deployment types. The results show that nondeterminism persists even at temperature 0.0, with distinct variability patterns by model size, deployment, and prompt type. We situate these findings within existing work on concept drift, behavioural drift, and infrastructure-induced nondeterminism, discuss the limitations of lexical metrics, and highlight emerging semantic approaches. By establishing a systematic empirical baseline in the absence of stabilisation techniques, this study provides a reference point for evaluating future drift mitigation and control methods.
Comments:
10 pages, 3 figures, 1 table. Empirical measurement study reporting new repeated-run experiments quantifying baseline nondeterministic drift in large language models. This manuscript presents original empirical results (not a review or position paper) and establishes a baseline reference for future drift-mitigation work

本日日期原值：{"created":"2026-01-29T02:41:03Z","v1_dates":[{"date":"2026-01-12T10:34:48Z","dateType":"Submitted","dateInformation":"v1"},{"date":"2026-01-29T01:00:55Z","dateType":"Updated","dateInformation":"v1"},{"date":"2026-01","dateType":"Available","dateInformation":"v1"}]}
