# Sep02 第二批有界补检完整题摘 / 版本标记差额

作者：Darwin / Codex本会话。执行补充窗口：2025-09-01 ～ 2025-09-01（北京时间）；2026-10-07T21:40+08:00整理。仅本日题名补检新增8身份，6P/1U/1撤回后恢复版本争议；尚未独立校准，不是当窗候选、Evidence、评分或DAY。首批23与代表2C拟保留于[first-batch](first-batch-supplement-20261007.md)，不覆盖作者拟判断。累计31新完整题摘身份为22P/5U/2C拟/1当前撤回/1版本争议。00072的额外v2/v4题摘只作同家族标记核查，不增身份。

来源为本轮五类官方YYYY-MM月表各首25题名有界浏览（共125出现/125身份）；与Advanced178重合5，发现库存合并298。新机制标题定点选8读精确v1完整题摘，不把298设为摘要/全文队列。原件与执行收据全在同日supplement目录；题摘位置为原页citation_abstract与blockquote.abstract，metadata日期只作版本/提交说明，**不得作为首次公开日期**。未知公开日不关闭贡献，也不评分。当前版本标记为必要轻量核查，不遍历所有历史版本。

## 1. 2509.00388v1 — GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction

官方：[精确版本](https://arxiv.org/abs/2509.00388v1)；实际原件：[resume2-2509.00388v1.html](supplement-20261007/resume2-2509.00388v1.html)；[执行收据](supplement-20261007/resume2-2509.00388v1.html.receipt.json)。

作者（本精确版）：Li, Xuelin; Jin, Xiangqi; Zhang, Linfeng。citation_date=2025/08/30、citation_online_date=2025/08/30，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Efficient Key-Value (KV) cache management is essential for processing long text sequences in large language models (LLMs), where memory constraints often limit performance. Conventional KV eviction strategies, such as top-k selection based on attention scores, depend on static heuristics that fail to capture the evolving implicit dependencies among tokens during inference. To overcome this, we propose GraphKV, a graph-based framework that redefines token selection for KV cache compression. In GraphKV, tokens are modeled as nodes with importance scores, and edges represent their similarity relationships. Through a decay-signal-propagation mechanism, token importance is dynamically updated by propagating information across the graph, enabling adaptive retention of the most contextually significant tokens. GraphKV can be seamlessly utilized in existing KV cache eviction methods such as SnapKV and PyramidKV in a plug-and-play manner. Codes will be released on Github.

作者拟处置：**P**。静态attention/top-k难表示演进依赖 → GraphKV把token设为带importance的图节点、相似边上做decay-signal propagation → 若成立需比较动态保留与静态选择的质量/图更新成本，而非仅减KV容量。

条件唯一owner：`INFER-KV-CACHE`；尚未进行Books实际论点比较。反侧/停止：尚未核runtime图构建/传播成本、长程漂移与可比质量；代码will be released不算实现核验。

## 2. 2509.00461v1 — TECP: Token-Entropy Conformal Prediction for LLMs

官方：[精确版本](https://arxiv.org/abs/2509.00461v1)；实际原件：[resume2-2509.00461v1.html](supplement-20261007/resume2-2509.00461v1.html)；[执行收据](supplement-20261007/resume2-2509.00461v1.html.receipt.json)。

作者（本精确版）：Xu, Beining。citation_date=2025/08/30、citation_online_date=2025/08/30，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Uncertainty quantification (UQ) for open-ended language generation remains a critical yet underexplored challenge, especially under black-box constraints where internal model signals are inaccessible. In this paper, we introduce Token-Entropy Conformal Prediction (TECP), a novel framework that leverages token-level entropy as a logit-free, reference-free uncertainty measure and integrates it into a split conformal prediction (CP) pipeline to construct prediction sets with formal coverage guarantees. Unlike existing approaches that rely on semantic consistency heuristics or white-box features, TECP directly estimates epistemic uncertainty from the token entropy structure of sampled generations and calibrates uncertainty thresholds via CP quantiles to ensure provable error control. Empirical evaluations across six large language models and two benchmarks (CoQA and TriviaQA) demonstrate that TECP consistently achieves reliable coverage and compact prediction sets, outperforming prior self-consistency-based UQ methods. Our method provides a principled and efficient solution for trustworthy generation in black-box LLM settings.

作者拟处置：**P**。黑盒不可得logit → sampled-generation token entropy加split conformal calibration → 可检验prediction-set覆盖与成本，不外推通用语义正确性。

条件唯一owner：`PLATFORM-EVALUATION-SYSTEM`；尚未进行Books实际论点比较。反侧/停止：exchangeability、校准集分布变化、token entropy是否代表epistemic uncertainty及生成集合定义须证据；六模型/两任务不作普遍保证。

## 3. 2509.00391v1 — The Resurgence of GCG Adversarial Attacks on Large Language Models

官方：[精确版本](https://arxiv.org/abs/2509.00391v1)；实际原件：[resume2-2509.00391v1.html](supplement-20261007/resume2-2509.00391v1.html)；[执行收据](supplement-20261007/resume2-2509.00391v1.html.receipt.json)。

作者（本精确版）：Tan, Yuting; Li, Xuying; Li, Zhuo; Shu, Huizhen; Hu, Peikang。citation_date=2025/08/30、citation_online_date=2025/08/30，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Gradient-based adversarial prompting, such as the Greedy Coordinate Gradient (GCG) algorithm, has emerged as a powerful method for jailbreaking large language models (LLMs). In this paper, we present a systematic appraisal of GCG and its annealing-augmented variant, T-GCG, across open-source LLMs of varying scales. Using Qwen2.5-0.5B, LLaMA-3.2-1B, and GPT-OSS-20B, we evaluate attack effectiveness on both safety-oriented prompts (AdvBench) and reasoning-intensive coding prompts. Our study reveals three key findings: (1) attack success rates (ASR) decrease with model size, reflecting the increasing complexity and non-convexity of larger models' loss landscapes; (2) prefix-based heuristics substantially overestimate attack effectiveness compared to GPT-4o semantic judgments, which provide a stricter and more realistic evaluation; and (3) coding-related prompts are significantly more vulnerable than adversarial safety prompts, suggesting that reasoning itself can be exploited as an attack vector. In addition, preliminary results with T-GCG show that simulated annealing can diversify adversarial search and achieve competitive ASR under prefix evaluation, though its benefits under semantic judgment remain limited. Together, these findings highlight the scalability limits of GCG, expose overlooked vulnerabilities in reasoning tasks, and motivate further development of annealing-inspired strategies for more robust adversarial evaluation.

作者拟处置：**P**。prefix判成功可能高估攻击 → GCG/T-GCG跨三个不同模型的prefix与GPT-4o语义判断差异/编码负面证据 → 安全评价须分开攻击收益与judge误差。

条件唯一owner：`PLATFORM-SECURITY`；尚未进行Books实际论点比较。反侧/停止：三个不同家族/训练条件不控制size因果；非凸loss解释与reasoning本身可攻击是作者解释非已证实；GPT-4o judge也非ground truth。

## 4. 2509.00072v1 — Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination

官方：[精确版本](https://arxiv.org/abs/2509.00072v1)；实际原件：[resume2-2509.00072v1.html](supplement-20261007/resume2-2509.00072v1.html)；[执行收据](supplement-20261007/resume2-2509.00072v1.html.receipt.json)。

作者（本精确版）：Zhang, Terry Jingchen; Dev, Gopal; Wang, Ning; Ni, Nicole; Jiang, Wenyuan; Huang, Yinya; Schölkopf, Bernhard; Sachan, Mrinmaya; Jin, Zhijing。citation_date=2025/08/26、citation_online_date=2025/08/26，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Capability evaluation of large language models (LLMs) is increasingly shadowed by rising concerns of data contamination that cast doubts on whether static benchmarks measure genuine reasoning or mere memorization. We present an empirical study using an infinitely scalable framework to synthesize research-level QA directly from arXiv papers, harnessing the natural temporal structure of research publications where performance decay after knowledge cutoffs may indicate potential contamination. We evaluated 4 frontier model represented by 2 models of different knowledge cutoff dates per family on 1,643 multi-step reasoning questions synthesized from 20,277 arXiv papers stratified over 26 months, covering at least 6 months before and after all cutoff dates. Our results consistently showed a lack of significant performance decay near knowledge cutoff dates for models of various sizes, developers, and release dates. We further performed a comparative analysis with previous longitudinal studies that reported significant post-cutoff performance decay using directly retrieved questions based on public data. we hypothesize that the multi-step reasoning required by our synthesis pipeline offered additional complexity that goes deeper than shallow memorization, which effectively serves a mitigation strategy against benchmark contamination. We fully open source our code and dataset to aid reproducibility and advocate for a paradigm shift that prioritize reasoning-driven synthesis to construct benchmarks over simply collecting newly released questions periodically.

作者拟处置：**版本争议隔离**。v1借无cutoff退化推合成reasoning可缓解污染；v2作者因incomplete work撤回旧稿；v3/v4恢复且v4改为同源题目构造会改变时间信号的评价盲区 → 不采用旧稿mitigation因果，不把新稿反侧静默套回2025事件。

条件唯一owner：`PLATFORM-EVALUATION-SYSTEM`；尚未进行Books实际论点比较。反侧/停止：v2不入选/不评分/不Books，旧稿采用链隔离；current v4不是当前整家族撤回，但恢复/新命题属2026窗外。v1首次公开日未核，保留潜在评价反证供非作者版本裁决，不整体关掉家族。

## 5. 2509.00031v1 — ZeroQAT: Your Quantization-aware Training but Efficient

官方：[精确版本](https://arxiv.org/abs/2509.00031v1)；实际原件：[resume2-2509.00031v1.html](supplement-20261007/resume2-2509.00031v1.html)；[执行收据](supplement-20261007/resume2-2509.00031v1.html.receipt.json)。

作者（本精确版）：Tan, Qitao; Song, Xiaoying; Lu, Jin; Li, Guoming; Liu, Jun; Hong, Lingzi; Ding, Caiwen; Li, Jundong; Zhai, Xiaoming; Huang, Shaoyi; Niu, Wei; Yuan, Geng。citation_date=2025/08/21、citation_online_date=2025/08/21，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Quantization is an effective technique to reduce the deployment cost of large language models (LLMs), and post-training quantization (PTQ) has been widely studied due to its efficiency. However, existing low-bit PTQ methods suffer from accuracy degradation because their layer-wise optimization introduces cumulative error propagation and misalignment between local reconstruction objectives and downstream performance. While quantization-aware training (QAT) provides a principled solution, its reliance on backpropagation incurs prohibitive data, time, and memory costs, limiting its practicality. To address these challenges, we propose ZeroQAT, a zeroth-order optimization-based QAT framework. ZeroQAT leverages forward-only gradient estimation to eliminate the need for backpropagation, significantly reducing computational and memory overhead while retaining the benefits of end-to-end optimization. Moreover, ZeroQAT jointly learns quantized weights, weight clipping thresholds, and equivalent transformations to mitigate quantization error and handle activation outliers. Experiments demonstrate that ZeroQAT achieves the efficiency of PTQ while retaining the accuracy of QAT, offering a practical solution for high-quality low-bit quantization of LLMs.

作者拟处置：**P**。layer-wise PTQ局部重构误差与下游目标错配，而QAT反传占资源 → ZeroQAT以forward-only zeroth-order估计联合低比特weights/clipping/等价变换 → 可改变端到端量化训练资源取舍。

条件唯一owner：`INFER-TENSORRT-LLM`；尚未进行Books实际论点比较。反侧/停止：需核forward查询总量/估计方差与目标预算、outlier处理；摘要PTQ效率+QAT精度不直接采用。当前v2已改题，不能用当前title代替v1证据。

## 6. 2509.00579v1 — KVComp: A High-Performance, LLM-Aware, Lossy Compression Framework for KV Cache

官方：[精确版本](https://arxiv.org/abs/2509.00579v1)；实际原件：[resume2-2509.00579v1.html](supplement-20261007/resume2-2509.00579v1.html)；[执行收据](supplement-20261007/resume2-2509.00579v1.html.receipt.json)。

作者（本精确版）：Jiang, Bo; Yang, Taolue; Liu, Youyuan; Zhang, Chengming; He, Xubin; Jin, Sian。citation_date=2025/08/30、citation_online_date=2025/08/30，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Transformer-based large language models (LLMs) demonstrate impressive potential in various practical applications. However, long context inference poses a significant challenge due to the enormous memory requirements of the key-value (KV) cache, which can scale to multiple gigabytes as sequence length and batch size increase. In this paper, we present KVComp, a generic and efficient KV cache management framework optimized for long-text generation that synergistically works with both latency-critical and throughput-critical inference systems. KVComp employs novel lossy compression techniques specifically designed for KV cache data characteristics, featuring careful co-design of compression algorithms and system architecture. Our approach maintains compatibility with the growing nature of KV cache while preserving high computational efficiency. Experimental results show that KVComp achieves on average 47\% and up to 83\% higher memory reduction rate compared to existing methods with little/no model accuracy degradation. Furthermore, KVComp achieves extremely high execution throughput, effectively reducing decompression overhead and, in some cases, even accelerating the matrix-vector multiplication operation and outperform cuBLAS-based attention kernels with less data movement.

作者拟处置：**U**。KVComp明确声称适应持续append的KV有损压缩与系统共设计、decompression甚至影响matvec成本，可能不是普通量化数字；决定准入的压缩表示/执行路径尚含糊，校准后定点方法补读，不因摘要缺实验而关闭。

条件唯一owner：`INFER-KV-CACHE`；尚未进行Books实际论点比较。反侧/停止：不自造fused kernel或无损保证；47/83%和cuBLAS对比均未读等条件。U指新增机制事实未清，不是实验可信度尚待核的拒收。

## 7. 2509.00642v1 — HADIS: Hybrid Adaptive Diffusion Model Serving for Efficient Text-to-Image Generation

官方：[精确版本](https://arxiv.org/abs/2509.00642v1)；实际原件：[resume2-2509.00642v1.html](supplement-20261007/resume2-2509.00642v1.html)；[执行收据](supplement-20261007/resume2-2509.00642v1.html.receipt.json)。

作者（本精确版）：Yang, Qizheng; Chen, Tung-I; Zhao, Siyu; Sitaraman, Ramesh K.; Guan, Hui。citation_date=2025/08/31、citation_online_date=2025/08/31，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Text-to-image diffusion models have achieved remarkable visual quality but incur high computational costs, making real-time, scalable deployment challenging. Existing query-aware serving systems mitigate the cost by cascading lightweight and heavyweight models, but most rely on a fixed cascade configuration and route all prompts through an initial lightweight stage, wasting resources on complex queries. We present HADIS, a hybrid adaptive diffusion model serving system that jointly optimizes cascade model selection, query routing, and resource allocation. HADIS employs a rule-based prompt router to send clearly hard queries directly to heavyweight models, bypassing the overhead of the lightweight stage. To reduce the complexity of resource management, HADIS uses an offline profiling phase to produce a Pareto-optimal cascade configuration table. At runtime, HADIS selects the best cascade configuration and GPU allocation given latency and workload constraints. Empirical evaluations on real-world traces demonstrate that HADIS improves response quality by up to 35% while reducing latency violation rates by 2.7-45$\times$ compared to state-of-the-art model serving systems.

作者拟处置：**P**。固定cascade所有query先走轻模型会浪费hard-query计算 → rule-based直接hard路由+offline Pareto配置表、runtime GPU allocation → 联合route与资源选择可能改变质量/SLO边界。

条件唯一owner：`INFER-SCHEDULING`；尚未进行Books实际论点比较。反侧/停止：需核prompt规则错路由/质量proxy/profile漂移与全路径成本；35%及2.7–45x是作者摘要数字，不采用。后出v3改题不回写v1。

## 8. 2509.03018v1 — Mycroft: Tracing Dependencies in Collective Communication Towards Reliable LLM Training

官方：[精确版本](https://arxiv.org/abs/2509.03018v1)；实际原件：[resume2-2509.03018v1.html](supplement-20261007/resume2-2509.03018v1.html)；[执行收据](supplement-20261007/resume2-2509.03018v1.html.receipt.json)。

作者（本精确版）：Deng, Yangtao; Zhang, Lei; Wang, Qinlong; Zhi, Xiaoyun; Zhang, Xinlei; Jiang, Zhuo; Xu, Haohan; Wang, Lei; Song, Zuquan; Liu, Gaohong; Bai, Yang; Wang, Shuguang; Xiao, Wencong; Ye, Jianxi; Yu, Minlan; Xu, Hong。citation_date=2025/09/03、citation_online_date=2025/09/03，仅版本metadata；首次公开日未核，不填当窗日期。

完整摘要（原文，不是core审阅）：

Reliability is essential for ensuring efficiency in LLM training. However, many real-world reliability issues remain difficult to resolve, resulting in wasted resources and degraded model performance. Unfortunately, today's collective communication libraries operate as black boxes, hiding critical information needed for effective root cause analysis. We propose Mycroft, a lightweight distributed tracing and root cause analysis system designed to address previously hidden reliability issues in collective communication. Mycroft's key idea is to trace collective communication states and leverage internal control and data dependencies to resolve reliability problems in LLM training. Mycroft has been deployed at ByteDance for over six months to debug collective communication related issues at runtime. It detected anomalies within 15 seconds in 90% of cases and identified the root cause within 20 seconds in 60% of cases. We also conducted extensive fault injection experiments to demonstrate Mycroft's capability and efficiency.

作者拟处置：**P**。collective黑盒隐藏故障依赖 → Mycroft追踪collective状态及内部control/data依赖做root-cause → 可改变训练可靠性诊断从症状相关到依赖定位的选择。

条件唯一owner：`TRAIN-DISTRIBUTED-TRAINING`；尚未进行Books实际论点比较。反侧/停止：15s/20s比例与六个月部署是作者声明，需核故障集、overhead/trace缺失与误归因；v1 submitted Sep3不等公开日也不直接指认Sep01；保留贡献线索，落窗必要证据独立隔离。

## 00072必要版本标记与恢复反侧

v2原页L119官方withdrawn标记、L136 Comments：作者因incomplete work撤回；[v2原件](supplement-20261007/resume2-2509.00072v2.html)及[收据](supplement-20261007/resume2-2509.00072v2.html.receipt.json)。v4官方history L169–176保留v2撤回，v3（2026-04-26）/v4（2026-05-13）恢复；当前v4 Comments=ACL 2026，并非当前整家族withdrawn。[v4原件](supplement-20261007/resume2-2509.00072v4.html)及[收据](supplement-20261007/resume2-2509.00072v4.html.receipt.json)。日期为提交历史，不授公开日。当前v4完整摘要：

Post-cutoff performance decay of LLMs has been widely interpreted as a temporal signal for benchmark contamination, where public information released before the training cutoff may have been included into training corpora and inflated model performance by memorization. We critically examine this view and demonstrate that this temporal signal is highly sensitive to how benchmark questions are constructed, even if the underlying source material remains invariant. Specifically, we show that LLM-transformed questions can produce remarkably different temporal patterns compared to fill-in-the-blank (cloze) questions directly retrieved from the very same documents. We validate this effect on prior benchmarks that report clear post-cutoff decay (LiveCodeBench), and show that a simple LLM-driven transformation of the same problems can effectively remove the temporal pattern. We further provide a mechanistic understanding of this phenomenon using influence function analysis. Overall, our results suggest that post-cutoff performance decay is a sensitive contamination signal, motivating more robust contamination probes for reliable LLM evaluation.

重要反侧：同一source材料换cloze与LLM transformed question会改变cutoff时间信号；“没有post-cutoff退化”不自动等于reasoning消除了污染。只读当前题摘/必要withdrawal说明，未读v4 influence-function方法或评价core，不声称反侧已证明，不把2026恢复归入Sep01。请求非作者校准旧稿排除/历史家族隔离、新稿窗外反侧及准入保留边界。

## 交接

本包与首批全部拟保留/5U/2代表排除及官方文本重合、当前撤回、版本恢复争议一并交root协调非作者。先校准，后围绕具体命题读必要core/日期/家族；有长期差额才提交唯一owner及Books具体提案，由root共享写入。未受影响初筛可继续，不扩大到其他日，不自署FIRST或DAY。

后续差额：首批Boole FIRST已落盘19P/3C/1撤回，作者R1–R6写回另存[具名差额](author-calibration-writeback-20261007.md)。本包8尚未校准、6P/1U/1版本争议拟判断不变；累计31当前25P/1U/3C/1当前撤回/1版本争议，不覆盖21:40快照或上文原拟判断。LongCat同旧家族release单列，不计第32新身份。

2026-10-07T22:18:32+08:00实际结果更新：[Boole §7](review-supplement-20261007.md)已实际读本包8份完整精确v1题摘及00072必要v2/v4，独裁7P/1版本争议；KVComp U→窄P的实际方法位置、00072分版本隔离已落实到[作者R7–R8](author-calibration-writeback-20261007.md)。累计31=26P/3C/1当前撤回/1版本争议、0U；上文原6P/1U及25P/1U保留为到达前历史，不冒作当前值。公开日未核不评分，不把31变成当窗候选或全文队列。LongCat实际No Change已由Boole §8核通过，无需root重复同核心，最终DAY另交。
