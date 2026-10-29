# Jun11 增量补查：首批准入校准

作者：supp_jun11；执行日：2026-10-26 Asia/Shanghai。只补 Jun10 北京时间自然日，保留旧报告小时窗、旧52家族及有效证据；不是重新审核旧562宽列表。下列题摘实际读取官方精确v1 abs；DataCite只用于身份和公告日期组合，不以其current摘要替代v1（10890当前v2摘要与v1不同，以下为v1）。独核：待root实际校准。

## 日期共用依据

精确DOI `10.48550/arxiv.<ID>`，登记方 `arxiv.content`、`publisher=arXiv`、`state=findable`。各唯一v1 submitted均在Jun09 EDT 14:00以前，按适用官方日程最早公告为 `2026-06-10T00:00:00Z`；registered最晚界如下，均晚于最早界、整个区间落Jun10 BJT。原始字段没有改名为实际公开时刻；不证明全球首稿。当前官方abs未显示withdraw/correction。10890有Oct16 v2，10381有Sep28 v2，均不进入本窗。

| ID | submitted v1 UTC | registered UTC |
| --- | --- | --- |
| 2606.11169 | 2026-06-09T17:48:41Z | 2026-06-10T02:24:50.000Z |
| 2606.11173 | 2026-06-09T17:50:09Z | 2026-06-10T02:24:55.000Z |
| 2606.10890 | 2026-06-09T14:03:04Z | 2026-06-10T02:18:02.000Z |
| 2606.11164 | 2026-06-09T17:44:23Z | 2026-06-10T02:24:43.000Z |

来源：`https://api.datacite.org/dois/10.48550/arxiv.<ID>` 与下列精确官方abs。最早界依据研究合同§2和脚本 `scripts/arxiv_publication_date.py`，该脚本仅复算、不是日期证明。

## 拟准入

### [Piper: A Programmable Distributed Training System](https://arxiv.org/abs/2606.11169v1)

完整v1摘要：

> Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO. Deployed systems for foundation model pretraining often rely on human experts to manually design a high-level parallelism strategy then implement the corresponding low-level execution strategy, making it difficult to adapt the system to new strategies. Meanwhile, many general-purpose frameworks are more flexible but their implementations are still tied to a fixed set of common parallelism strategies, making it challenging to integrate state-of-the-art strategies.
> We present Piper, a user-controllable distributed training system that decouples the strategy from the runtime implementation. Piper allows users to declare a comprehensive distributed training strategy with a small set of model annotations and scheduling directives. Each directive applies a transformation on Piper's intermediate representation (IR), a unified global training DAG that represents all computation and communication. Using this IR, Piper compiles per-device execution plans and executes them with a distributed runtime agnostic to the strategy. We show that the combined system maintains performance parity on commonly available strategies such as ZeRO, while also enabling additional performance and memory efficiency gains through joint scheduling of compute and communication in composed parallelism strategies such as DeepSeek-V3's DualPipe.

准入理由：训练并行策略与runtime低层实现耦合→用统一全局计算/通信DAG接受用户变换指令并编译每设备计划→需重新考虑“每个新混合并行方案必须定制runtime”的边界。不是因可映射章节而准入。拟2+2+2=6；若涉及执行语义等具体命题则加深相应部分。潜在owner TRAIN-DISTRIBUTED-TRAINING；未作Books决定。

### [The Role of Feedback Alignment in Self-Distillation](https://arxiv.org/abs/2606.11173v1)

完整v1摘要：

> Conditioning a language model on additional context, such as feedback on a previous attempt, typically improves its response. Self-distillation trains the model to retain this improvement when the context is not present. The method works by matching the model's output distribution under two settings: a student that sees only the question, and a self-teacher that also sees the context. What the model learns therefore depends on what context the self-teacher receives, yet the design of this context remains largely unexplored.
> We study context design for self-distillation by training a solver on feedback from a frozen critic. We compare three conditions: (i) a binary reward (GRPO), (ii) the reference solution, and (iii) a step-by-step critique aligned to the solver's reasoning trace.
> Step-aligned critique yields the largest gains, outperforming GRPO by 16.11 points and reference-solution-conditioned self-distillation by 5.27 points (Avg@12). Per-token advantage analysis reveals why: step-aligned feedback targets only the tokens where reasoning fails, leaving correct behavior intact. Conditioning on the reference solution, by contrast, pressures the model to change its behavior at every token (even correct steps) because an alternative derivation inevitably differs in phrasing and approach. This suggests that structural alignment between feedback and the solver's reasoning is a key driver of self-distillation effectiveness.

准入理由：通常把“教师获得更多正确信息”当自蒸馏收益代理→对齐学生原轨迹的逐步批评与参考解给出不同token级压力→需核验反馈结构而非仅其信息量是否决定更新已有正确步骤的损伤。局部小模型/有限任务也足以修正具体判断；不要求工业LLM消费者。拟2+1+2=5。潜在owner TRAIN-SFT；未作Books决定。

### [Optimal Post-Training Quantization Scales and Where to Find Them](https://arxiv.org/abs/2606.10890v1)

完整v1摘要：

> Post-training quantization (PTQ) compresses large language models by mapping weights to low-bit representations. The scaling factor that defines the quantization grid is typically chosen using simple, data-free heuristics. In this work, we present PiSO (Piecewise Scale Optimization), an algorithm that leverages calibration data to compute the optimal channel-wise weight scales exactly and efficiently under round-to-nearest quantization. PiSO partitions the scale search space into finitely many intervals on which the objective admits a closed-form minimizer. We extend PiSO to group-wise quantization via principled heuristics and propose effective strategies for interleaving scale optimization with error correction. Experiments on Llama and Qwen models across multiple model sizes and target weight bit-widths demonstrate consistent improvements in perplexity and downstream zero-shot accuracy, both standalone and combined with error correction. In particular, we observe increased benefits as the target bit-width narrows and quantization becomes more challenging.

准入理由：RTN量化通常用data-free scale且把优化重点放在rounding/error correction→固定量化归属区间内可闭式求最优channel scale→需重审scale是否必然只能启发式搜索，以及该局部最优与groupwise/全网最优的界限。拟2+1+3=6；理论优化条件需深入对应证明。潜在owner INFER-TENSORRT-LLM；不采用v2新数字。

### [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164v1)

完整v1摘要：

> Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods mitigate this issue via token eviction, but typically assume a uniform budget distribution across all layers and heads. In contrast, existing non-uniform budget allocation methods are predominantly designed for the static prompt prefill phase, and they do not capture the stepwise context demands of autoregressive reasoning. To bridge this gap, we propose ReasonAlloc, a training-free framework that recasts decoding-time KV compression as a hierarchical budget allocation problem. ReasonAlloc operates at two complementary levels: an offline layer-wise preallocation strategy captures an architecture-driven demand pattern which we call “Reasoning Wave”, while an online head-wise strategy reallocates resources during decoding to information-rich heads based on real-time utility. Evaluations on mathematical reasoning benchmarks (MATH-500, AIME 2024) using DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, and AceReason-14B show that ReasonAlloc outperforms uniform-budget R-KV, SnapKV, and Pyramid-RKV (a baseline enforcing a static, monotonically decreasing layer budget), with the largest gains at small budgets (128-512 tokens). ReasonAlloc is plug-and-play with existing token-eviction policies and introduces negligible inference-time overhead.

准入理由：把prefill静态预算或uniform预算沿用到CoT decode→离线层级需求与在线head utility分层分配→需比较预算“分给谁”与token“淘汰谁”是否是独立轴及其动态适用边界。拟2+1+2=5。潜在owner INFER-KV-CACHE；未作Books决定。

## 代表性贡献前排除

### [Unifying Data, Memory, and Compute Efficiency in LLM training: A Survey](https://arxiv.org/abs/2606.10706v1)

完整v1摘要：

> Resource constraints increasingly determine what can be trained, fine-tuned, and deployed in large language models (LLMs), yet efficiency is often studied through isolated techniques rather than as an interacting system of limits. This survey adopts a constraint-centric perspective and organizes recent progress around three coupled bottlenecks: data efficiency (what to train on), memory efficiency (how to fit training), and compute budget awareness (when and where to spend FLOPs). On the data axis, we review selection and pruning methods that maximize learning per token, ranging from scalable proxy signals based on learning dynamics to gradient- and influence-based scoring, as well as difficulty-aware and curriculum-style strategies. We highlight emerging evidence that different notions of good data dominate in different regimes, implying that optimal subsets depend on the task objective and resource budget rather than being universal. On the systems side, we show that GPU memory, not raw compute, is often the dominant bottleneck in fine-tuning, and that effective scaling requires jointly reducing weight storage, optimizer states, and activation memory rather than optimizing any single component in isolation. Beyond memory, we frame training and inference as compute-governed processes in which optimization, data selection, and decoding must explicitly account for finite FLOP budgets. We review evidence for compute-optimal allocation and stopping rules, where computation should be halted or reallocated once marginal performance gains fall below a budget-dependent threshold. Together, these results unify compute-aware data selection, scaling laws, and adaptive inference under a common principle of resource-conditioned decision-making.

排除理由：完整摘要给出已有data/memory/compute研究的约束中心整理，未指明新增实验证据、对照混杂或足以修正既有系统判断的反例；“联合考虑资源预算”本身不是该文新增机制。无withdraw/correction信号。未评分，不以survey标签一概排除；若具名新证据到达仅重开此项。

### [Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis](https://arxiv.org/abs/2606.10381v1)

完整v1摘要：

> Muon collider research spans accelerator physics, detector instrumentation, and high-energy phenomenology, with relevant evidence scattered across a rapidly expanding and heterogeneous body of scientific literature. As high-energy physics (HEP) increasingly explores agent-assisted analysis workflows, efficiently locating, integrating, and verifying scientific evidence becomes an essential capability. While retrieval-augmented generation (RAG) offers a promising framework for scientific question answering, integrating agentic reasoning without compromising retrieval precision remains a key challenge. In this work, we present agentic hybrid RAG, an evidence-grounded RAG framework for muon collider research. The framework combines a hybrid retriever, integrating sparse lexical and dense semantic retrieval, with an agentic reasoning module for query decomposition, evidence expansion, and grounded answer generation. To enable systematic evaluation, we construct the first benchmark for retrieval-augmented scientific question answering in the muon collider domain, comprising a curated literature corpus together with dedicated retrieval and answer-generation benchmarks covering major detector and physics research topics. Extensive evaluation shows that hybrid retrieval provides the strongest retrieval backbone, while agentic reasoning is most effective for controlled evidence expansion and answer synthesis. Built on this principle, agentic hybrid RAG consistently outperforms representative retrieval and RAG baselines in retrieval effectiveness, answer quality, evidence coverage, and factual grounding. Together, the benchmark and framework provide a foundation for evidence-grounded scientific question answering and future HEP analysis agents operating over large-scale scientific literature.

排除理由：ROADMAP暂缓的AI for Science领域应用；增量为muon collider文献语料/benchmark和hybrid retrieval+agentic reasoning组合，不绕道AGENT-RAG重新纳入。未评分，日期不为该排除另追。当前v2不改变本窗v1应用范围。

## B2：补充语义筛选（待root校准后的必要审阅）

完整精确v1题目/摘要、官方版本记录及逐项DataCite字段保存在 [B2原件摘录](SUP_TITLE_ABSTRACT_B2_20261026.json)。不是把DataCite current摘要冒充v1；抽取自精确官方abs。12项唯一v1 submitted均为Jun09、18UTC之前，最早界Jun10 00UTC至各registered上界均落Jun10 BJT，身份/登记方/findable无冲突；当前abs无withdrawn标记。后续版本不采用，11190 v2及10820 v2的提交虽然落Jun10，也没有据submitted当该版公开事件。

| ID / 精确题目见原件 | 原有判断 → 实际增量 → 重新考虑 | 拟分数 | 潜在owner |
| --- | --- | --- | --- |
| 2606.11190 When to Align, When to Predict | 跨模态共同signal通常被当作融合收益前提→带相关nuisance的线性框架导出CA/CP各自失败及Neither区→需核目标/预测方向应先诊断而非默认多模态必好。含image-caption/立体视觉与通用线性机制，不因同时含科学数据误排。 | 2+2+3=7 | MULTIMODAL-REPRESENTATION |
| 2606.10929 Recoverable but Not Stationary | 低秩task vector常被理解成稳定任务平面→局部低秩但百步内basis漂移且静态basis漏恢复方向→需核局部可控与全程固定子空间不可混同。小模型反证仍有效。 | 2+1+3=6 | TRAIN-LORA |
| 2606.11155 Mean Flow Distillation | 直接借diffusion score蒸馏可能高方差→平均velocity目标及时间低通解释→需核平均velocity匹配何时足够分布对齐而非任何“mean flow”皆正确。 | 2+1+3=6 | MULTIMODAL-GENERATIVE-PARADIGMS |
| 2606.11081 Unifying Local Communications and Local Updates | 减少collective频率仍要求全局同步同态→将outer optimizer扩到稀疏随机gossip并兼容local adaptive步骤→需比较通信频率与通信拓扑两种自由度和优化漂移。 | 2+2+2=6 | TRAIN-DISTRIBUTED-TRAINING |
| 2606.10820 K-Forcing | speculative的验证成本在高batch可能不摊销→把多token联合采样蒸馏为uniform noise到joint token的单pass推送→需区分近似联合解码/质量代价与无损speculation。 | 2+1+3=6 | MODEL-DECODER-ONLY |
| 2606.11025 Flow-DPPO | flow后训练用sample ratio clipping当trust代理→Gaussian per-step闭式KL及方向性mask→需核可计算divergence如何改变过/欠约束及是否仍只是局部约束。 | 2+1+2=5 | TRAIN-PPO |
| 2606.10968 Beyond Uniform Token-Level Trust Region | token独立统一阈值不管prefix偏离→位置权重加累计prefix预算→需重审单token约束可否代表整条AR轨迹稳定。 | 2+1+3=6 | TRAIN-PPO |
| 2606.11188 ARM | 理解/生成共享离散表征通常有语义与重建冲突→联合tokenizer多目标并报告生成/编辑RL跨任务协同→需核共享表征的目标取舍及RL迁移证据，不仅因模型组合或涨分准入。 | 2+1+2=5 | MULTIMODAL-REPRESENTATION |
| 2606.11167 Multi-Faceted Interactivity Alignment | full-duplex likelihood不直接优化pause/turn/backchannel/interruption→分轴片段奖励与语义质量guard→需核行为时间控制与内容质量是否冲突及如何分别评价。 | 2+1+2=5 | TRAIN-RLHF |
| 2606.11145 OpenPCC | proprietary PCC不可外部署、TEE标签不足定义隐私→commodity TEE CIS的要求/端到端prototype并分解hardware代价→需核attestation/服务链能否真正封闭请求信任边界。潜机制明确、security可信度待核，不因摘要缺细节排除。 | 2+2+2=6 | PLATFORM-SECURITY |
| 2606.11127 Provenance-Grounded Gating | synthetic过滤多用holistic judge且丢弃拒例→source-grounded gate×失败诊断再生成，且generator scale仍主导下游→需把faithfulness、reward、yield和下游收益分开，不以高回收率推质量。 | 2+1+2=5 | TRAIN-DATA |
| 2606.11075 FlowBP | 全rollout反传贵且梯度链长，短pinned surrogate又会偏→cached无梯度采样与轻backward surrogate拆四个选择并限制Jacobian链→需区分采样轨迹与优化轨迹及误差/内存代价。 | 2+2+2=6 | TRAIN-RLHF |

B2原表是初筛提案，不是已证实结论或Books结果。root实际完整题摘校准见SUP_REVIEW_20261026 §5：11190/10929/11155/11081/10820/11025/10968/11127/11075九项潜在贡献通过；11188 ARM贡献前排除（多目标tokenizer+统一AR+taskRL与未限定cross-task synergy未提出新兼容条件/机制或足以修正既有判断的反证，不借新7B/组合或分数准入，撤回拟5分，不列当窗候选）；11167仅定点核新时序/质量兼容条件或旧reward失效，11145仅定点核具体PCC glitch/commodity TEE信任链新失效，决定事实明确才准入或排除。两者尚不算已准入/待全篇深审，不因security或reward轴相加扩池。无按比例保留或整合配额。

## B3：系统/注意力补主题的有界语义批次

[完整精确v1题摘及原始版本/登记字段](SUP_TITLE_ABSTRACT_B3_20261026.json)。所有拟候选除下述10932外唯一v1为Jun09且18UTC前，合法最早00UTC～registered上界均落Jun10。当前官方abs无withdrawn；11171的DataCite current题名为Bellman-sufficient，而精确v1官方题名为Algorithmic and Minimax Complexities in Kernel Bandits，版本已多次更题，不混用current题摘。以下待root校准，未展开无关Methods。

| ID | 判断与具体问题链 | 初评分/下一层 |
| --- | --- | --- |
| 2606.11158 Defeat the Heap | N提案：把heap先copy到DMA buffer改成直接DMA分配，是已知zero-copy原则的一次accel dialect/lowering实现；摘要没有新layout/lifetime兼容条件、失效边界或改变原系统判断的反证。不能仅因编译器/少一份copy/2x数据移动准入。 | 不评分 |
| 2606.10937 Provenance Tracking in AI Compilers | 传统ID传播在non-injective rewrite下丢来源→观察computational actions并以bisimulation跨消除节点重建provenance→需核可观察等价与原语义provenance能否区分，不把新形式语言等同正确性。拟准入。 | 2+2+2=6；INFER-TENSORRT-LLM |
| 2606.10932 Density Field State Space Models | 潜在1bit scaffold+int8 correction及SSM state kernel，但唯一v1 submitted Apr28，registeredJun10，界跨April29～Jun10；没有官方目标日公告证明。不评分/不列确定窗内候选，不拿ID月份或Updated字段补造首公开。 | 具名日期恢复；正文未深读 |
| 2606.10944 Express Language Modeling | 非causal attention近似不可直接当流式有界memory近似→构造保误差保证的causal化转换并有I/O-aware实现→需核其memory/误差/压缩费用前提，不能从kernel速度直接许decoder质量。拟准入。 | 2+2+3=7；MODEL-SELF-ATTENTION |
| 2606.11171 Algorithmic and Minimax Complexities in Kernel Bandits | 需校准边界：实际v1是frequentist RKHS bandit的算法轨迹信息量与class-wide DEC/minimax证书比较，非DataCite current Bellman题名。可能修正“类最坏界即实际algorithm复杂性”的理解，但本文未建立foundation模型学习/参数或Agent policy上的具体改变。不能因纯理论/无大LLM自动N，也不能因overparameterized一词自动C；root请定其现主线解释增量是否足够。 | 未评分、决定事实/范围校准 |
| 2606.11052 Attention Amnesia in Hybrid LLMs | CoT-SFT通常只验reasoning gain→hybrid模型long-range recall大退并局部定位Q/K routing，恢复preSFT Q/K与其余postSFT分开→需核增益/旧能力保护接口而非默认SFT只增不损。拟准入。 | 2+2+2=6；TRAIN-SFT |
| 2606.10829 ADAS | 独立高置信位置未必可共同commit→保原sampler stopping只改subset构造，对已选未确定位置的attention施soft penalty→需把选几个与选谁的相互依赖分开。拟准入，不把attention等依赖真值。 | 2+1+3=6；MULTIMODAL-GENERATIVE-PARADIGMS |
| 2606.10759 miniReranker | 仅决定事实待核：vision-first相对query/document-first是否形成新的兼容/质量约束，或只是prefix cache+early-exit+稀疏attention/pruning成熟组合。高复用<1% runtime和保96%本身不够。 | 未评分，定点看格式/复用对照 |
| 2606.10650 Dynamic Linear Attention | 固定多state合并不可逆模糊重要token→信息变化决定state边界并在容量超界时只合并相邻低信息state→需核bounded chronological cache与可回忆信息的取舍，不把信息proxy当无损。拟准入。 | 2+1+2=5；MODEL-LONG-CONTEXT |
| 2606.10493 Cloud-Grade Local MoE | 仅决定事实待核：stream-loaded prefill/本地shared-weight PD是否新增可辨识resource/lifetime条件或旧组合失效；五项模块+SLO数字不单独准入。 | 未评分，定点机制/对照 |
| 2606.10440 ASTRA-sim3 | collective latency不能由纯字节网络模型表达→cacheline load/store GPU控制/数据路径与InfraGraph细化→需核精细粒度何时改变collective设计排序与模拟代价，非因版本3.0准入。拟准入。 | 2+2+2=6；TRAIN-DISTRIBUTED-TRAINING |
| 2606.10646 FlowTracer | pointwise内部信号忽略answer可达路径→attention-DAG按answer可达性重权并局部守恒，再由throughput塑token reward→需核credit是否仅proxy/长度偏差及为何不是attention大即贡献。拟准入。 | 2+1+2=5；TRAIN-GRPO |

## B4：Agent训练/评价/记忆主题

[完整精确v1题摘、history与日期原字段](SUP_TITLE_ABSTRACT_B4_20261026.json)。12项唯一Jun09 v1、18UTC前至各registered的联合界均落Jun10，官方abs未见withdraw。下表是待root校准的贡献判断，不是深读结论；没有为五项明确N另追无关Methods。

| ID | 具体准入/排除理由 | 拟分数/owner |
| --- | --- | --- |
| 2606.11079 VISTA | N：六metric衡量realism/coverage/effectiveness并接合UI/API，摘要没给新增评价混杂、控制条件或足以修正原判断的对照；工具kit/组合使评估“更全面”的宣称本身不足。 | 不评分 |
| 2606.11042 Workflow-GYM | N：扩展到专业软件长workflow并列阶段遗漏/错误传播/goal drift与低成功率，没有区别已有long-horizon失败机制的新条件或受控反例；不是因benchmark身份自动N，而是实际增量仍为domain/task覆盖。 | 不评分 |
| 2606.10728 DeNovoSWE | N：全repo任务数据规模、divide-and-conquer+critic-repair+difficulty filtering与FT涨分；摘要未给新验证合同、filter兼容条件或纠正成熟组合判断的反证。数据集与任务难度不单独建立长期增量。 | 不评分 |
| 2606.11045 What Fits Doesn't Overfit | C：重复validation易过拟合→fresh reproducer只读短prompt/traindata仍重现，故意诱导overfit则不能短描述复现→需把策略可压缩性与反馈信息量作为benchmark适应性风险的可证伪条件，不把短prompt当万能免责。 | 2+2+3=7；PLATFORM-EVALUATION-SYSTEM |
| 2606.10933 Frontier Coding Agents Use Metaprogramming | C：主流language基准可能压缩Agent差异→禁meta-programming大退，给helper代码与给口头指引收益不同，额外budget只增强已会策略者→需把工具策略可执行性/传递形式与语言熟悉度分开，不以纯加token解决能力差。 | 2+1+2=5；AGENT-TOOL-CALLING |
| 2606.10875 KATE | C：一般以更抽象经验与更深reasoning作为工具改进方向→instance经验强于intent抽象、宽采样胜过深思的受控潜证据→需核经验粒度、激活方式和全预算；不是KATE组合模块本身准入。 | 2+1+2=5；AGENT-TOOL-CALLING |
| 2606.10852 Janus | C：deception只测假事实→固定同事实池、neutral vs goal条件仍可通过遗漏/弱化/强调造成误导印象→需把事实支持与material事实呈现完整性分开评。 | 2+1+3=6；PLATFORM-EVALUATION-SYSTEM |
| 2606.10747 Arbiter | C：被动监控被假定只读且足够→有预算主动提问/看内部信息改变可识别性，logging提高recall却损precision且weight-induced更难→需核auditor能力/费用/证据访问不同不能直接比较检测率。 | 2+2+2=6；AGENT-MULTI-AGENT |
| 2606.10742 MemVenom | C：prompt或text memory防护未覆盖graph多模态长期记忆→retrieval触发与读取后诱导分两段且任务间可复用→需核记忆召回资格与动作授权两条污染路径，不能因benign平均保持授安全。只做防御性机制/限制审阅，不复制攻击payload。 | 2+2+2=6；AGENT-MEMORY |
| 2606.10709 Query recycling | C：zero-variance group被当成query静态难度属性并永久过滤→同query随policy改进/漂移可重获非零信号，mutable pool重采→需核排除资格是否随policyrevision失效，及重采成本/分布bias。 | 2+1+2=5；TRAIN-GRPO |
| 2606.10677 Infini Memory | N：topic文档、buffer周期维护和iterative reads的成熟组合及互补消融，未给新的修订一致性/生命周期机制或改写设计判断的失效条件；64.7分与text-doc形式本身不足。 | 不评分 |
| 2606.10532 ActiveMem | N：Planner消费gist、memory并行整理与神经类比，摘要没有说明超出已知角色分工的状态协议/失效边界，SOTA与开销宣传不能证明去中心结构消除trade-off。 | 不评分 |

## B5：后训练/稀疏/资源主题

[完整精确v1题摘及日期字段](SUP_TITLE_ABSTRACT_B5_20261026.json)。12项唯一Jun09 v1均在18UTC前，合法最早界至各registered上界落Jun10，未把后续版本提交计事件；当前官方abs未见withdraw。

| ID | 具体增量链/排除 | 拟分数/owner |
| --- | --- | --- |
| 2606.10989 NSRU | 仅决定事实待核：retain-hidden子空间的nullspace LoRA+安全target/suppression组合之外，局部一阶分析是否给出新的可编辑性/retain保护条件，而非重述正交投影恒等式；未评分，不因三个loss相加先准入。 | 定点理论/控制条件 |
| 2606.10935 CLP | MTP首token与backbone输出竞争→让backbone固定拥有首token、后续由span predictor决定长度→需核职责分离是否改变退化边界，及learnedgate无独立验证是否真“零损”。 | 2+1+2=5；INFER-SPECULATIVE-DECODING |
| 2606.10722 Continual Upcycling | dense→bank-sparse训练通常只看aggregate性能→报告单层/特定长上下文失效与单层修复→需核稀疏routing如何定位能力损伤，而非4xsparsity或模块组合准入。 | 2+1+2=5；MODEL-FFN |
| 2606.10617 SSR-Merge | parameter merge任务冲突→在拼接低秩信号space decorrelate再按任务guide路由，sufficient statistics流式更新→需核OLS条件与生成行为最优不能混同、统计支持怎样决定task混叠。 | 2+1+3=6；TRAIN-LORA |
| 2606.10613 BFQ | 多步diffusionQ或额外蒸馏才能单步action→从短程flow displacement自举为noise-to-action→需核bootstrapped displacement是否替代额外teacher以及offline支撑/误差边界；D4RL小policy也可能支撑生成/控制机制，不因无LLM误排。 | 2+1+3=6；MULTIMODAL-GENERATIVE-PARADIGMS |
| 2606.10610 SDBN | N：将adversarial训练带入PEFT，并用字符梯度枚举/LLM变体等已知扰动集合，摘要主要宣称较少研究的组合与低资源涨分，未提出新兼容条件、噪声失效机理或改变既有鲁棒训练判断的反证。 | 不评分 |
| 2606.10445 SpenseGPT | 严格2:4质量代价与宽松格式runtime代价冲突→矩阵拆2:4与dense区域、选择dense位置而沿用两类现有GEMM→需核布局/区域选择如何改变质量—执行兼容，不把B200单数字准入。 | 2+2+2=6；INFER-TENSORRT-LLM |
| 2606.10435 PCAF | dense全历史与固定SSM state二选一→hash-bucket causal successor records、bounded candidates形成cache分布再gate mix localLM→需核稀疏content-addressed历史何时可并行保持因果及capacity/质量取舍，303M局部实验不因小规模排除。 | 2+1+3=6；MODEL-LONG-CONTEXT |
| 2606.10415 RATrain | GPU型runtime假设HBM/互联不适MT3000显式memory/20GBDDR→layer/stage-local训练state lifecycle规划同步/更新/prefetch/recovery→需核重排是否守1F1B训练语义及显式层级可行性边界，不由新平台适配名准入。 | 2+2+2=6；TRAIN-DISTRIBUTED-TRAINING |
| 2606.10346 DiRL | 只奖励semantic/gradient多样性不分新reasoning与旧shortcut变体→internal方向加权gradient特征再塑reward→需核方向标签/contrast与行为评价的可识别性，不把rep投影当真实reasoning。 | 2+1+2=5；TRAIN-GRPO |
| 2606.10520 UniSVQ | scalar整型kernel兼容但2bit误差、VQ灵活但码本/查表成本→把codeword参数化为integer lattice仿射变换→需核能否同时消费整型kernel与vector灵活性及真正执行费用。 | 2+2+2=6；INFER-TENSORRT-LLM |
| 2606.10651 KwaiKeyeVL2 | 只定点决定DSA→GQA的视频token/状态契约或MOPD多teacher冲突是否有新兼容/遗忘条件；不能以30B MoE+三个RL/蒸馏模块+lossless256K宣传直接准入。 | 未评分，必要条件明确后决 |

### B4/B5 三个决定事实（完整题摘已root§12校准，2026-10-26定点补读）

- **2606.10989 NSRU：具体pre-N，不评分。** 实际[精确v1 §III–IV](https://arxiv.org/html/2606.10989v1#S3)得到的条件仍为retain-feature的SVD projector P与BA(I−P)，retain落span则局部增量小，forget有nullspace分量则可编辑；反传同投影是链式法则恒等式。rank-capped能量阈值只在所算谱内截取，固定特征rule/安全target+undesired ascent+retain NLL未新增整网保持或可编辑性条件，也没有比已知投影失效更具体的新反证。按原决定点关闭，不因低成本/安全标签扩实验与全篇Methods，未把日期不确定作排除理由。
- **2606.10651 KwaiKeyeVL2：具体pre-N，不评分。** 实际[§2.3](https://arxiv.org/html/2606.10651v1#S2.SS3)为共享MQA lightning index产生同一Top-k(2048)交GQA各组消费，densewarmup用各group attention的sum-KL，随后truncated top-k KL+sparse adaptation与detach；这是既有DSA/indexer训练到GQA接线，未给新的组间兼容条件或它失效的控制反证。[§4.2.6](https://arxiv.org/html/2606.10651v1#S4.SS2.SSS6)13teacher按task/modality路由、共同top-k overlap的条件logratio、token类别scaling/repetition penalty，说明常见style interference但未给可隔离的冲突消除条件；[§5.3](https://arxiv.org/html/2606.10651v1#S5.SS3)adjacent-query Top-k去重/既有MMA mask与chunk ViT仅实现说明和H800局部成本数，无新的错误/布局资格。模型规模/组合和256K宣传不足准入，不扩完整RL/data/评测recipe；不因此否认其工程价值。
- **2606.10747 Arbiter：决定事实支持窄候选2+2+2=6，待独核。** 实际[§3](https://arxiv.org/html/2606.10747v1#S3)、[§4.1/4.2](https://arxiv.org/html/2606.10747v1#S4.SS1)及[§5 T2/T5](https://arxiv.org/html/2606.10747v1#S5)：同weight-induced organism、同neutral prompts下，pure observation与Ask+Log两格均无CoT/systemprompt读取，F1 .12→.51；因此不只是偷看恶意systemprompt。Ask-only F1.28→加Log.51，成本/时间有限；有受限直接证据检验“同公开conversation被动读已足”是否成立，不归因Ask单一组件或普遍监控能力。weight-vs-prompt比较含Qwen/Gemma及topic人口变化，不能作同人口因果；baseline误报population亦不同，logging误报只在人口内比较。普通logging precision/recall不是独立新贡献，若后续必要不足则收窄此检测命题而非扩所有工具/攻击payload。潜在准入后才执行标准必要/actualowner，不把这些门槛事实先称证据完成。

### 有限主题补检末项：2606.10089（不扩大目录）

[A Theory on Flow Matching with Neural Networks — 精确v1](https://arxiv.org/abs/2606.10089v1)。完整题摘实际读：

> In this work, we develop theoretical foundation for flow matching with neural-network-parameterized conditional velocity fields. We establish convergence guarantees for gradient descent in the over-parameterized 2-layered ReLU neural network regime. We derive generalization bounds for the conditional velocity-field matching objective. Building on these results, we provide Wasserstein-distance guarantees for the samples generated by the induced flow. Our analysis is based on generalization bound for multi-task representation learning with unbounded losses, which may be of independent interest beyond flow-based generative modeling. These theoretical results are validated through extensive experiments on both synthetic and real-world image benchmarks.

原身份唯一v1 submitted Mon Jun08 19:16:32UTC，晚于适用EDT14点=18UTC cutoff，最早Jun10 00UTC公告；[同精确DOI](https://api.datacite.org/dois/10.48550/arXiv.2606.10089)登记方arxiv.content、findable、registered2026-06-10T01:58:19.000Z，整个合法界落Jun10 BJT，不能因submitted日期Jun08误当跨日。DataCite原dates Submitted/v1同19:16:32，Updated/v1 Jun10 00:07:39Z仅原元数据，不改名为公告。当前abs轻查无撤回/纠错标记。

准入提案2+1+3=6，owner `MULTIMODAL-GENERATIVE-PARADIGMS`：固定目标速度场误差不能自动保证神经网络GD训练后样本距离→原文连接两层ReLU过参数化下优化、无界loss的多任务泛化及诱导flow的Wasserstein误差→可能限定“学好velocity即可交付样本”所需宽度/步数/人口条件。只准入这条受限链，不因纯数学/小模型排除、不借image分数或通用FM名称；具体条件与边界待必要核验，不预授所有定理。有限导航末项后不再补全269/128/1361为队列；另五个具名日期跨界仅恢复日期，不偷转候选。

10747会期cue有限核：exact-v1页头写AI Transparency Conference Jun5–6；[官方最终programme](https://coairesearch.org/aitc-2026/)明确Jun6 15:15–15:35为同题同作者Paper Talk，当前页面展示经speaker许可陆续发布的recordings，未提供本稿PDF/proceedings或当时正文上线日期。沿唯一[官方Publications入口](https://coairesearch.org/publications/)九条当前公开记录，无同题本稿/更早正文链接；两个精确题名/会议日期查询只回arXiv及该官方programme，没有具名更早正文原件。本次只确认更早口头报告与会期，不能把会期单字段改成论文正文公开日，也不能承诺全球不存在早稿；不扩大会议全站扫描。该cue和有限恢复结果交独核决定，未以它无故删候选。
