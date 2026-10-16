# 2026-04-24 自然日遗漏补查（唯一记录）


作者：supp_apr24_author；启动2026-10-15；只补2026-04-23北京时间自然日。原85候选整行/小时窗/连续§4保留于baseline-before-supplement-20261015.md，不调整日期归属或评分；原必要Source、具体owner及实际POST仅按身份/v/采用命题不变复用，不以旧完成标签签本轮。root为本轮非作者准入/Source/PRE/POST/DAY与FINAL复核者，本文件root区由root写入。

## A1. 有限发现与停点

已重读当前AGENTS、Research/Report合同、Daily14/arXiv来源、统一Prompt、ROADMAP与本日现存README/机构记录/筛选记录最新结论。月级LS仅路由，未继承他日池。旧Daily的85候选不重审，跨日仅查已发现材料身份去重。

4主题API：submittedDate:[202604211800 TO 202604221800]配MODEL（language model/transformer/MoE/foundation model）、SYSTEM（LLM inference/distributed training/KV cache/GPU kernel/model serving）、AGENT（language agent/LLM agent/RAG/tool calling/context engineering）、MULTIMODAL（vision language/world model/VLA/diffusion model）。start0/max350，各total216/9/34/39，250唯一发现身份；submitted仅发现筛子，不等公开日期或本窗新论文。全部标题已浏览，明确领域应用/数学同名噪音不进入逐项题摘队列。相关/含糊73项已完整题摘语义读取，首批独立校准待root实际读取下文。入选尚未冻结；需exact-v1、自然公开日期和当前撤回/纠错信号。

有界分类标题补检：12分类月列表只定位Apr23相邻ID簇，非整月逐项队列。初始show2000的大分类响应尾部截断，不能作读完；CL/LG/CV/AI收窄show250定位目标页，其余小类已有限标题提取。只补检本日主线相关标题，不把宽月库存或later-ID延迟条目强推落窗。

机构原14源的邻界记录可复用并重新按Apr23自然日解释；已新开当前官方目录核活跃入口。确定差额待核：Hy3-preview card News明确Apr23但仅参数/MTP规格及未披露RL管线，拟贡献EX；ContextUnrolling21921原日期例外须核Seed官方Apr23，GPT5.5/DiLoCo原85去重，Seed3D2同家族已在旧归属处理不重列。其它来源限制保留原具体历史缺段，不授零更新或全站覆盖。

## A2. 首批独立准入校准

首批拟正：19907、19945、20117、20140；20158普遍系统断言需定点纠错核。代表拟EX：19926、19972、20015、20183。下文保留当时完整题摘；A3最新裁决覆盖其初始提案，不是证据审阅结论。

### 2604.19907 — 首批准入校准材料

原始：`SUP_TOPIC_AGENT_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.19907v2`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

SceneOrchestra: Efficient Agentic 3D Scene Synthesis via Full Tool-Call Trajectory Generation

Recent agentic frameworks for 3D scene synthesis have advanced realism and diversity by integrating heterogeneous generation and editing tools. These tools are organized into workflows orchestrated by an off-the-shelf LLM. Current approaches typically adopt an execute-review-reflect loop: at each step, the orchestrator executes a tool, renders intermediate results for review, and then decides on the tool and its parameters for the next step. However, this design has two key limitations. First, next-step tool selection and parameter configuration are driven by heuristic rules, which can lead to suboptimal execution flows, unnecessary tool invocations, degraded output quality, and increased runtime. Second, rendering and reviewing intermediate results after each step introduces additional latency. To address these issues, we propose SceneOrchestra, a trainable orchestration framework that optimizes the tool-call execution flow and eliminates the step-by-step review loop, improving both efficiency and output quality. SceneOrchestra consists of an orchestrator and a discriminator, which we fine-tune with a two-phase training strategy. In the first phase, the orchestrator learns context-aware tool selection and complete tool-call trajectory generation, while the discriminator is trained to assess the quality of full trajectories, enabling it to select the best trajectory from multiple candidates. In the second phase, we perform interleaved training, where the discriminator adapts to the orchestrator's evolving trajectory distribution and distills its discriminative capability back into the orchestrator. At inference, we only use the orchestrator to generate and execute full tool-call trajectories from instructions, without requiring the discriminator. Extensive experiments show that our method achieves state-of-the-art scene quality compared to previous work.


### 2604.19945 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.19945v1`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

Visual Reasoning through Tool-supervised Reinforcement Learning

In this paper, we investigate the problem of how to effectively master tool-use to solve complex visual reasoning tasks for Multimodal Large Language Models. To achieve that, we propose a novel Tool-supervised Reinforcement Learning (ToolsRL) framework, with direct tool supervision for more effective tool-use learning. We focus on a series of simple, native, and interpretable visual tools, including zoom-in, rotate, flip, and draw point/line, whose tool supervision is easy to collect. A reinforcement learning curriculum is developed, where the first stage is solely optimized by a set of well motivated tool-specific rewards, and the second stage is trained with the accuracy targeted rewards while allowing calling tools. In this way, tool calling capability is mastered before using tools to complete visual reasoning tasks, avoiding the potential optimization conflict among those heterogeneous tasks. Our experiments have shown that the tool-supervised curriculum training is efficient and ToolsRL can achieve strong tool-use capabilities for complex visual reasoning tasks.


### 2604.20117 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.20117v1`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

To Know is to Construct: Schema-Constrained Generation for Agent Memory

Constructivist epistemology argues that knowledge is actively constructed rather than passively copied. Despite the generative nature of Large Language Models (LLMs), most existing agent memory systems are still based on dense retrieval. However, dense retrieval heavily relies on semantic overlap or entity matching within sentences. Consequently, embeddings often fail to distinguish instances that are semantically similar but contextually distinct, introducing substantial noise by retrieving context-mismatched entries. Conversely, directly employing open-ended generation for memory access risks "Structural Hallucination" where the model generates memory keys that do not exist in the memory, leading to lookup failures. Inspired by this epistemology, we posit that memory is fundamentally organized by cognitive schemas, and valid recall must be a generative process performed within these schematic structures. To realize this, we propose SCG-MEM, a schema-constrained generative memory architecture. SCG-MEM reformulates memory access as Schema-Constrained Generation. By maintaining a dynamic Cognitive Schema, we strictly constrain LLM decoding to generate only valid memory entry keys, providing a formal guarantee against structural hallucinations. To support long-term adaptation, we model memory updates via assimilation (grounding inputs into existing schemas) and accommodation (expanding schemas with novel concepts). Furthermore, we construct an Associative Graph to enable multi-hop reasoning through activation propagation. Experiments on the LoCoMo benchmark show that SCG-MEM substantially improves performance across all categories over retrieval-based baselines.


### 2604.20140 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.20140v2`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

HiPO: Hierarchical Preference Optimization for Adaptive Reasoning in LLMs

Direct Preference Optimization (DPO) is an effective framework for aligning large language models with human preferences, but it struggles with complex reasoning tasks. DPO optimizes for the likelihood of generating preferred over dispreferred responses in their entirety and lacks the granularity to provide feedback on subsections of many-step solutions typical of reasoning tasks. Existing methods excel at either stable preference learning (e.g., DPO variants like KTO and RSO) or structured reasoning (e.g., ReMA's multi-agent RL framework, Tree of Thoughts), but fail to merge these complementary strengths. We propose HiPO (Hierarchical Preference Optimization), an extension of DPO that separates responses into reasoning segments (query clarification and context, reasoning steps, and answer) and computes loss as a weighted sum of the DPO loss for each segment. Our approach enables segment-specific training while maintaining DPO's computational efficiency and training stability. We demonstrate that for multiple 7B LLMs fine-tuned using HiPO and DPO on the Math Stack Exchange preference dataset, the models trained with HiPO outperform the others on a variety of common math benchmarks and achieve greater organization, logical flow, and consistency as measured by GPT-4.1.


### 2604.20158 — 首批准入校准材料

原始：`SUP_TOPIC_AGENT_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.20158v1`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

Stateless Decision Memory for Enterprise AI Agents

Enterprise deployment of long-horizon decision agents in regulated domains (underwriting, claims adjudication, tax examination) is dominated by retrieval-augmented pipelines despite a decade of increasingly sophisticated stateful memory architectures. We argue this reflects a hidden requirement: regulated deployment is load-bearing on four systems properties (deterministic replay, auditable rationale, multi-tenant isolation, statelessness for horizontal scale), and stateful architectures violate them by construction. We propose Deterministic Projection Memory (DPM): an append-only event log plus one task-conditioned projection at decision time. On ten regulated decisioning cases at three memory budgets, DPM matches summarization-based memory at generous budgets and substantially outperforms it when the budget binds: at a 20x compression ratio, DPM improves factual precision by +0.52 (Cohen's h=1.17, p=0.0014) and reasoning coherence by +0.53 (h=1.13, p=0.0034), paired permutation, n=10. DPM is additionally 7-15x faster at binding budgets, making one LLM call at decision time instead of N. A determinism study of 10 replays per case at temperature zero shows both architectures inherit residual API-level nondeterminism, but the asymmetry is structural: DPM exposes one nondeterministic call; summarization exposes N compounding calls. The audit surface follows the same one-versus-N pattern: DPM logs two LLM calls per decision while summarization logs 83-97 on LongHorizon-Bench. We conclude with TAMS, a practitioner heuristic for architecture selection, and a failure analysis of stateful memory under enterprise operating conditions. The contribution is the argument that statelessness is the load-bearing property explaining enterprise's preference for weaker but replayable retrieval pipelines, and that DPM demonstrates this property is attainable without the decisioning penalty retrieval pays.


### 2604.19926 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.19926v1`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

CreativeGame:Toward Mechanic-Aware Creative Game Generation

Large language models can generate plausible game code, but turning this capability into \emph{iterative creative improvement} remains difficult. In practice, single-shot generation often produces brittle runtime behavior, weak accumulation of experience across versions, and creativity scores that are too subjective to serve as reliable optimization signals. A further limitation is that mechanics are frequently treated only as post-hoc descriptions, rather than as explicit objects that can be planned, tracked, preserved, and evaluated during generation. This report presents \textbf{CreativeGame}, a multi-agent system for iterative HTML5 game generation that addresses these issues through four coupled ideas: a proxy reward centered on programmatic signals rather than pure LLM judgment; lineage-scoped memory for cross-version experience accumulation; runtime validation integrated into both repair and reward; and a mechanic-guided planning loop in which retrieved mechanic knowledge is converted into an explicit mechanic plan before code generation begins. The goal is not merely to produce a playable artifact in one step, but to support interpretable version-to-version evolution. The current system contains 71 stored lineages, 88 saved nodes, and a 774-entry global mechanic archive, implemented in 6{,}181 lines of Python together with inspection and visualization tooling. The system is therefore substantial enough to support architectural analysis, reward inspection, and real lineage-level case studies rather than only prompt-level demos. A real 4-generation lineage shows that mechanic-level innovation can emerge in later versions and can be inspected directly through version-to-version records. The central contribution is therefore not only game generation, but a concrete pipeline for observing progressive evolution through explicit mechanic change.


### 2604.19972 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.19972v1`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

Principal Nested Cones

In many applications, the data lie on a type of cone, where there is a distinction between an overall scale variable and the remaining scale-free structure. For example, the joint size and shape of objects are points on a cone, where size represents scale, and shape is the scale-free structure. Dimension reduction is central in such applications, as shape data are often high-dimensional. Interactions between shape and size are widespread and of significant interest in real-world applications. However, most existing methods either lack a single notion of size or focus solely on shape, effectively removing size information. We propose Principal Nested Cones (PNC), a nonlinear dimension reduction framework that preserves both shape and size. PNC represents data through a sequence of nested hypercones and progressively projects observations onto lower-dimensional cone spaces. The resulting PNC scores provide low-dimensional representations that jointly capture size-shape variation in an interpretable manner. To enable scalable computation in ultra-high-dimensional settings, we develop a fast approximation combining PCA-based transformation with standard PNC. Simulation studies and real data applications demonstrate that PNC captures nonlinear size-shape structure, improves representation and reconstruction, and yields interpretable insights across morphometric, developmental, and molecular datasets.


### 2604.20015 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.20015v2`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

FIKA: Expanding Dependency Reachability with Executability Guarantees

Automated third-party library analysis tools help developers by addressing key dependency management challenges, such as automating version updates, detecting vulnerabilities, and detecting breaking updates. Dependency reachability analysis aims at improving the precision of dependency management, by reducing the space of dependency issues to the ones that actually matter. Most tools for dependency reachability analysis are static and fundamentally limited by the absence of execution. In this paper, we propose FIKA, a pipeline for providing guarantees of executability for third-party library call sites. FIKA leverages a Large Language Model (LLM) guided by static analysis to generate code that is executed, and whose execution trace provides guarantees that a third-party library call site is actually executable. We apply our approach to a dataset of eight Java projects to empirically evaluate the effectiveness of FIKA. On average, 54% of these call sites are covered by the existing test suites, and therefore, have evidence for their executability. FIKA improves this coverage by 20%, generating successful reachability scenarios for 609 out of 1465 previously non-covered call sites. In six out of eight projects, FIKA provides strong guarantees that more than 75% of call sites are executable. We further demonstrate that FIKA improves over Semgrep, a state-of-the-art static vulnerability reachability analysis tool, and outperforms Jazzer, a coverage-guided directed fuzzer. We show that FIKA can help prioritize the vulnerability updates with stronger guarantees of executability.


### 2604.20183 — 首批准入校准材料

原始：`SUP_TOPIC_MODEL_20261015.raw.xml`，Atom entry id `http://arxiv.org/abs/2604.20183v2`；当前题摘仅作初筛，exact-v1/自然公开日期/必要Source尚未签。

Dual-Cluster Memory Agent: Resolving Multi-Paradigm Ambiguity in Optimization Problem Solving

Large Language Models (LLMs) often struggle with structural ambiguity in optimization problems, where a single problem admits multiple related but conflicting modeling paradigms, hindering effective solution generation. To address this, we propose Dual-Cluster Memory Agent (DCM-Agent) to enhance performance by leveraging historical solutions in a training-free manner. Central to this is Dual-Cluster Memory Construction. This agent assigns historical solutions to modeling and coding clusters, then distills each cluster's content into three structured types: Approach, Checklist, and Pitfall. This process derives generalizable guidance knowledge. Furthermore, this agent introduces Memory-augmented Inference to dynamically navigate solution paths, detect and repair errors, and adaptively switch reasoning paths with structured knowledge. The experiments across seven optimization benchmarks demonstrate that DCM-Agent achieves an average performance improvement of 11%- 21%. Notably, our analysis reveals a ``knowledge inheritance'' phenomenon: memory constructed by larger models can guide smaller models toward superior performance, highlighting the framework's scalability and efficiency.

## A3. 首批actual校准与精确跨日去重

root已实际读A2九项完整题摘，支持19907/19945/20117/20140有限potential及20158只核强断言；四EX19926/19972/20015/20183支持，具体是既有组合/领域应用而非参数小或缺普遍保证。随后只匹配已发现身份到邻日具名记录，不加载邻日论文池：

- 20158旧actual§3.2/7反查EX与本轮作者/root新读§3–5/10–12一致。deterministic U与tenant namespace足以反驳stateful原罪，原文也承认retrofit；DPM的event-source投影是成熟分支，10cases/两域不建立新制度性保证。复用具体贡献前关闭，不新增候选，不评分。
- 20117复用旧EX，经本轮实际§3.1–3.6/4.1–4.7再次核：trie合法key/graph组合，合法地址不等语义真实；hop/k反侧与换dense-retrieval的ablation没有新增同步/合法性条件或设计反证。不是要求普遍定律。无需把旧EX重列为候选。
- 20140旧EX按本轮actual方法具体化：preferred整答pair经GPT4.1改写Rq/Mt/A并假设偏好沿段继承；加权独立log-sigmoid不是整答DPO代数拆分；15vs5epoch/LR/改写共变，有限配方不改变当前已有granular-preference选择。当前保EX，root必要目标复核进行中。
- 19945旧仅AB的EX受具体反例重开：Tool-conditioned reward可先答再tool投机，global/answer-only与staged组合有反向切片。root已actual§3.3/T2–3/4.1–4.3，作者同段新读；恢复5分必要标准候选，不授消除优化冲突因果或更省费。必要证据位置见A5。
- 19954/19837各自原EX的边界已定点重新核，普通门裁仍开放，不能因旧已审或初读潜力就强收。19954不以没有通用geometry/物理控制保证否局部迁移；19837不把稳定denominator当独立正确。原必要材料为SUP_ADMIT_*v1_20261015.raw.html。
- root分层actual负侧：19934/20556/20727/20842支持具体EX；19954/19837要求最小补读，尚非EX验收。其它明确EX只按身份/v/理由未变复用或作者裁决，不称全部负侧已独核。

## A4. 有限潜力集合与普通Source停点

发现边界停止在106份相关/含糊完整题摘（73主题筛入+33有界标题lookup）；不是106贡献。下表54新增潜力及19945重开，另19954/19837旧EX因过强准入门被具体反例重开，共57个本轮家族；必要Source作者已逐项完成，独立Source与Books普通继续。无新增撤回信号；不因中心D/Books已覆盖删池或改分。ContextUnrolling21921早目录例外另隔离，不借晚arXiv或UTC提交日期硬归Apr23。

| 身份 | 原约束 → 实际潜力 → 待重核选择 |
| --- | --- |
| 2604.19907 | 逐步执行/渲染每步高延迟→全tool-call轨迹训练及判别蒸馏→离线监督与在线反馈责任重分。 |
| 2604.19945 | tool-conditioned奖励可投机先答再tool→global/answer-grounded监督与分阶段课程→工具会操作与任务效用分开验。 |
| 2604.20316 | 整答正确不识别reasoning帮助→固定CoT给student的成功率差与参数SMV→可读解释/实际作用分账。 |
| 2604.20328 | 文本与latent动作比率尺度不同→分开clip及vMF方向约束/实际非归一surrogate→混合动作训练语义需分层。 |
| 2604.20348 | 双臂联合action context膨胀→leader-follower条件动作与对称debate→动作耦合与推理调用预算重分。 |
| 2604.20354 | 扩散失败到终图才发现→中间PFI/attention检测后restart→selector错误与节约采样成本联合评价。 |
| 2604.20366 | 全局删hallucination分量损正常能力→语义分量提取/选择参数编辑→局部编辑的保留范围重核。 |
| 2604.20368 | linear attention低秩损表示→Laplacian kernel/injective map+Nyström求解→映射性质与近似算子分权。 |
| 2604.20392 | 迭代fovea缺大规模SSL→sequential-to-global DINO蒸馏→teacher全局目标与迭代停止梯度分责。 |
| 2604.20398 | 项目级web奖励异构→模板约束及执行/视觉级联reward→失败Gate与下游偏好分开。 |
| 2604.20452 | 全库检索昂贵/缓存仅exact query→homology重识别接受小范围draft→失配风险与检索延迟取舍。 |
| 2604.20460 | 逐题QA可能高而成对不一致→真实/生成counterfactual四元组→联合正确与生成真值分开。 |
| 2604.20472 | 单步概率与最终成功时序不一致→序列Brier/TD value校准→有限episode confidence与早停保护分开。 |
| 2604.20473 | video推理缺perception适配→cue-tree定位及reasoning-demand reward→视觉证据与额外推理预算条件。 |
| 2604.20487 | 文本RAG挤占上下文→relational capsule编译KV注入→非参数资产与模型attention耦合责任。 |
| 2604.20503 | batch统一spec length/串行draft verify→逐request长度/verify早剪与frontier重叠→相位资源/SLO取舍。 |
| 2604.20505 | 随机dropout难细粒度控制→显式attention/FFN正则→近似等价假设与真实目标分开。 |
| 2604.20544 | 整体数据分数掩局部错→视觉/推断/事实拆解评分及注入缺陷对照→数据质量sensor与下游收益分开。 |
| 2604.20549 | 低资源语言缺quality标签→跨语pool/Q3/retention对照→过滤迁移与稳定性条件。 |
| 2604.20570 | spatial只测理解→生成编辑约束及合成训练迁移→生成几何与理解提升的归因。 |
| 2604.20601 | 预定义subtask依赖人工→LM plan与goal-RL执行器互训/验证→可学plan与controller能力分责。 |
| 2604.20627 | 稀疏reward credit慢→world occupancy几何导出potential shaping→policy-invariance假设与估计模型分权。 |
| 2604.20659 | 整trajectory GRPO不分步→gold-answer likelihood增量作过程reward→progress proxy与真实步骤正确分开。 |
| 2604.20665 | 视觉相对文本损失可能由信息变换混杂→semantic translation及SSC→模态充分性与翻译oracle分开。 |
| 2604.20677 | 低可评人口易掩fairness→intersection/unknown/重复运行切片→公平差距与准确性/支持人口分开。 |
| 2604.20682 | 高variance不等predictive direction→压缩/上游扰动控制→局部linear fit不等跨层可替换。 |
| 2604.20685 | 固定scalarization可能压难目标→梯度几何+收敛动态的DPO→目标选择与descent保证条件。 |
| 2604.20705 | VLM RL奖励依赖语言judge→visual self-supervised puzzle/可验证reward→视觉任务支持与迁移分开。 |
| 2604.20715 | 图像relight/geometry串行误差→联合DiT与iNOD深度表示/混合数据→codec几何与appearance耦合。 |
| 2604.20720 | 多语PEFT会互扰→目标分布cluster缺口采样/漂移更新→语言相似与真实语义支持分开。 |
| 2604.20730 | raw视觉loop未必有益→SVG path分解训练/中间render条件→反馈接口须有训练曝光。 |
| 2604.20755 | 视觉终答reward弱credit→表格critic过程监督/PGPO→process judge与可验证表格真值分开。 |
| 2604.20763 | 启发式query覆盖不明→corpus实体strata补query→覆盖定义、缺层与真实检索人口分开。 |
| 2604.20779 | benchmark success不等实际留用→真实coding会话/commit归属→代码产量、保留与质量分开。 |
| 2604.20789 | 全context不必在少数据最好→固定window/decay对照→有限数据下inductive bias条件。 |
| 2604.20796 | 理解/生成分开模型难interleave→语义离散codec+MoE masked-block diffusion→backbone与pixeldecoder语义。 |
| 2604.20801 | harness固定人工/只调prompt→typed graph角色/工具/拓扑共同优化及runtime反馈→优化artifact与执行权限分权。 |
| 2604.20816 | 固定reward只能单operating point→condition preference并late scalarization→单资产Pareto导航的近似范围。 |
| 2604.20817 | 相同Fourier spikes不等相同算术表示→必要非充分定理及架构/数据/分词控制→spectral与linear separability分开。 |
| 2604.20819 | 单kernel容量失败→CQS分解/任务重组streaming→精确attention与OOM恢复的成本边界。 |
| 2604.20834 | compact VLA知识弱→goal-aware语义/几何alignment+action专家→representation监督与实际动作消费分开。 |
| 2604.20835 | source语言code-RL会损target→parallel programs SFT初始化→跨语言RL迁移的前提。 |
| 2604.19859 | 小research agent终答reward稀疏→information-gain turn奖励/format正则→credit粒度和总训练费分开。 |
| 2604.20446 | EoS自调未说明全域forcing→edge-coupling迭代对推导→Hessian平均/特征值结论假设。 |
| 2604.20500 | self-consistency重复prefix浪费→截断tree distinct-leaf枚举+prefix复用→覆盖分布与预算语义。 |
| 2604.20564 | 推理logical-connective分叉→局部steering/branching/token preference→局部干预与逻辑正确分开。 |
| 2604.20572 | 每步memory retrieval浪费→同prefix有/无检索paired continuation reward→检索动作credit与knowledge novelty分开。 |
| 2604.20614 | 训练校准与sharpness相关→margin-tail共同界/训练干预→同界不等ECE必然随curvature。 |
| 2604.20714 | 多agent只调flat prompt→textual parameter graph/经验化proposal→图编辑优化单位与元改进分开。 |
| 2604.20728 | learned perception有误识别→interval POMDP belief shield→统计区间/已知dynamics/有限horizon保护。 |
| 2604.20733 | 当前self-RL探索变窄→近未来checkpoint指导回滚者→teacher强度/支持差异/历史训练费。 |
| 2604.20811 | grammar语法合法不等执行语义→CFG recursion/branching/alien lexicon控制→schema与解释器能力分开。 |
| 2604.20470 | 静态video sparse mask难适应运动→radial prior+双mode/离线BO路由→proxy重构与真实motion质量分开。 |
| 2604.20486 | live web不可控/稀疏reward→static sandbox训练+知识边界过程reward→静态支持与live迁移有效性。 |
| 2604.20841 | 合成HOI视频不能独证physics→3D人/2D物混合imitation及visual alignment→生成参照与simulation控制分开。 |

日期字段原投影：SUP_DATE_20261015.raw.json的54身份，加SUP_DATE_19945/19954/19837_20261015.raw.json。root已实际逐项54及三个单JSON、SUP_BOUNDARY_19609_20261015.raw.json（Apr22）/SUP_BOUNDARY_20904_20261015.raw.json（Apr24）。54常规和19945/19837 v1处理/created/registered皆Apr23；19954 v1Updated Sep25后处理异常，created/registered Apr23/currentv1/官方CV列表同Apr23ID簇互证，不由Sep25回写首公开。结合官方announcement前moderation、ID只announcement assigned不能预发/回填的规则及相邻批次，57本轮材料可按Apr23 arXiv公开自然日处理。字段均保原义，不声称单created/submitted或这些组合证明全网首次公开；未见具名更早正文信号，日级资格足即停不追秒。57当前abs轻量正文均无withdrawn/retracted/erratum/corrigendum/corrected阳性，不遍历历史版本。

## A5. 逐项必要Source（作者结果，非作者覆盖另记）

本节保留分批审阅时的原始必要层与当时停点；下文“待root/Books普通”若已由A6/A7具名处置覆盖，不再是当前普通Source待办。57项必要Source技术独核已全部完成，只采用各项具名有限命题；精确Books写位/POST与仍未完成的owner以A6/A7后续记录为准，不把旧完成标签替代本轮验收。跨到Oct16不移动Apr23历史补充窗口。

### 2604.19907v1 SceneOrchestra

2+1+2=5，标准必要完成。作者实际§3.2–3.3/4.1及root实际§4.2/T1–3、4.3/T4–5/Limit§9可按身份/命题不变复用：step差分composition score选样→完整trajectory截断SFT/DPO→S2执行标训discriminator、S3用其预测偏好再DPO，仅一轮interleaved，部署仅orchestrator。score是GPT4.1物理/visual−runtime，不是独立真实3D有效oracle。十roomtype每五、complex十×三、Qwen3-4B/A6000；快于逐步SceneWeaver而慢于若干monolithic方案，部分bathroom completeness反退；阶段增数据/训练步与接口一起变，不唯一归因蒸馏。rollout/render/judge/重生及工具名validate/regenerate都计费，未证明原子执行、rollback或免反馈安全。没有实验复现/生产保证。root已actual必要Source，日期/notice与具体owner尚须最终合并核，Books普通。

### 2604.19945v1 ToolsRL

2+1+2=5，标准必要核心已实际读§3.3/4.1–4.3，root另实际T2–3并支持旧EX重开。Stage1 global取全tool trace与answer引用state的grounded tool reward兼顾探索/相关性，Stage2才QA准确reward；答案正确+tool-conditioned reward可先答再tool投机，非操作工具的有效训练监督。global-only/answer-only和mix/stage不能按单一平均判全面胜；原图像混入时可走原图shortcut，rot/flip只用增强图的Stage1使工具真实必要。Qwen2.5-VL7B，16rollouts/input，200steps/stage，batch256，无KL，max10turn，32H200/FSDP；reward/judge与额外工具采样费不是免费，多toolcall非因果证据。作者未复现，不采用“解决所有优化冲突/更省费”。root已actual必要Source，Books具体比较仍普通。

### 2604.20316v1 R2IF

2+1+2=5，标准必要已读§3.1/4.1–4.4、F.1–2与G.2直接标注条件。CER固定生成reason prefix交给另一个faithful student采样continuations，以其有/无prefix成功率差作奖励；只是对该student的条件帮助，不独证actor本身实际依赖该reason。SMV只对exact-match完整tool calls计参数spec/modification语义相似及参数出现，r_val在correct-call条件下已满足，不是独立执行oracle。GT SMV由LLM见query、tool doc和GT call后生成，更多解释一致性不能当真实因果faithfulness。2500balanced ToolACE，Qwen1.5/3/7B与Llama3B，BFCL/ACEBench单轮，6RTX PRO6000；2epochSFT/9epochGRPO、5rollout，student采样/标注总费用未同配预算；BFCL 1.5B不优binary baseline、部分irrelevance/SingleTurn反退，T5 Qwen7B重复行/子项前后不一致不补造统一数。只保有限reward接口和counterfactual consumer责任，不采用全部accuracy/透明度保证，Books普通，待root独立核。

### 2604.20328v1 HyLaR

2+2+2=6，必要核心实际读§3.3/4.1–4.3、补充§6.1–6.3/7。文本categorical与连续latent分别clip，normalized vMF共享κ时KL=kappa*A_D(kappa)*(1−mu_new·mu_old)，rollout存的是旧mode而非随机sample；补充明确该ratio是deterministic mode-referenced更新，不是标准stochastic IS。§6.3实际保留未归一hidden norm、把cosine换inner-product，作者明确此时不再严格density ratio/KL，不能照录主文“exact zero-variance KL”当实际训练证书。该区分足以保留方向surrogate的有限实现，不据此否定所有实验。SFT1epoch，RL rollout8/batch64、只保group accuracy[.1,.9]；sameSFT起点的RL算法与latent clip/weight/gaussian分支，SFT超训练步数退而RL切片缓解只限两fine-grainedbench。额外latent steps/筛组/训练费，clip不是全局trust-region保证；数值backend/完整预算未披露不补造。Books普通，root必要Source尚未核。

### 2604.20368v1 LaplacianFormer

2+2+2=6；纠错受影响深入完成，中心强保证隔离。作者读§4.1–4.3/5及主实验T3，root实际§4.1–4.2含Alg1–2/Eq4/9。Alg2所写alpha=2/||W||2、X0=alpha*W^T、Xnext=X(2I−WX)不由SPD+epsilon保证收敛：最终W=2I时X0=2I、X1=−4I，误差条件失败；合法all-ones Laplace kernel+epsilonI亦可最大特征值>1。交叉landmark Q/K不保证W对称，CW†C^T不自动是一般cross-kernel正确Nyström；实际diagonal normalization非完整whitening，不授近似后injectivity/全rank。只隔离打印inverse稳定/精确kernel及依赖的强保证，不否定ImageNet/PVT+RoPE/H800的有限实验；不再为不采用的普遍证明遍历附录。中心D可安全终态，不作Books正面证据；日期/notice另核。

### 2604.20503v1 FASER

2+2+2=6；作者实际§4.1–4.4/5/6.1–6.5，root实际§4.1–4.4前、4.2–4.3完整/5/6.1/6.5。逐request speculative length优化J=T/(s*accept+epsilon)，sliding GP-LCB结合batch/SMsplit；不是全局SLO证明。中间层TopK异步剪suffix明确可false earlyexit，pad回原shape只解决layout，不披露被误剪位置完整target logits/residual恢复；不得由frontier acceptedprefix/recovery/reset推全流水lossless。GreenContext隔SM而共享HBM/cache仍争用。有限阶段调度可采用，lossless早剪核心强主张隔离，Books不能补造恢复。vLLM0.15.1/5kPython、两小时profile/独立stream+contextpool；Qwen0.6/32B与Llama1/70B，两配置H10096GB按作者原表述，不自行改型号。26req/s trace，5×60s，ShareGPT755/200、LongBench1738/90、HumanEval171/98；precision、并发SLO、CI Not Disclosed。AD .5–.9%、EE5–6.3%是其定义组件开销，不是offline/pool/HBM/试探免费证书。root未实际6.2–6.4全胜数字不采用；不声称复现或生产exactness。日期/notice和具体owner普通。

### 2604.20392v1 Sequential-to-Global active vision

2+1+2=5，作者必要标准已读§2–5。每步固定foveal grid+multi-zoom token数、state8tokens跨step stop-gradient，DINO/Sinkhorn teacher最终step target而student每步match，firststate bottleneck避免poolhead捷径collapse；后冻结backbone/taskhead以GMM gaze+GRPO学位置。积分图先O(HW)构建，再每目标像素O(1)box-resize，不是端到端输入大小无关。ViT-S12block/384dim/6heads、ImageNetB1024；同frozenbackbone/head比较静态grid/8随机/8learned，learned75.0仍低静态76.1而优随机71.7。多步改善仅本实验平均，非每样本单调保证；更大fovealgrid改变token预算，state多有收益递减。积分图构建、8步backbone、任务头/策略训练总费，不把单步恒长当全管线省算证明。hardware/precision/CI Not Disclosed于已读核心。root必要Source/具体owner普通。

### 2604.20366v1 MPD

2+1+2=5；作者必要§3–4/Limit/B/D，受影响理论深入待root。配对同图faithful/hallucinatory描述均值隐状态，选topKweight投影去残差；不是已证实识别真实幻觉方向。X+为N×D却用leftU N×C得P N×N，称rowspace且I写D×D；实际sample-index投影不能自动变feature-space正交grounded方向。Prop1误差维数与该P不符；Eq5残差Gram直接inverse未给满rank。理论与其依赖强保证隔离，不否定三LVLM局部edit结果。LLaVA1.5/MiniGPT4/mPLUGowl2，LURE辅助LLM离线成对数据，layer16–32/C2500/K6000、beam3、单A40(40G按文)。CHAIR/POPE/MME四子项/LLaVABench GPT4V不等全部能力无损；K5k后CHAIR/MME反退、MMHal部分score/halrate反退保留。主表64tokens与runtime128tokens不能混同，3.7s vs3.1s非免费；离线成对生成/SVD/edit费用另计，precision及可信CI未披露。核心理论D/具体owner待独核，不自行改判EX。

### 2604.20398v1 WebGen-R1

2+1+2=5，作者必要§3/4.1–4.3/B标准完成。固定React scaffold→static/build失败0→已render才VLM aesthetics+console无错+thinktag奖；训练功能代理不等交互FSR。rewardweights网格γ大FSR反退，G增同时采样费增，不能当等预算机制归因。600GPT4.1银标/2epochSFT→400RLstep，QwenCoder7B/8H10080G，G16/B256，ctx4096/out8192/T.7/topP.95；训练eval共享GPT4o，101任务GUIagent FSR与视觉AAS不同。3frontend人评101网站的相关不等所有任务校准；Arena119无FSR不与101交互协议合并。静态/无consoleerror/截图均非真实全功能部署证书。root必要Source与owner普通。

### 2604.20452v1 HaS

2+1+2=5，作者必要§II–III/IV-A–D标准完成。cache-doc+aggressiveANN混合draft→doc-query倒排计overlap/k→threshold accept否则fullretrieval；fuzzy通道减少cache共现噪声。§III-B surrogate⇒quasi⇒homology的等价/逆否不成立：共享goldendoc不逻辑蕴含sameentity，同实体常共享属性只是经验；仅可采用heuristic质量/延迟取舍，不签factuality。模拟cloud .1–.2s/edge .01–.05s，49.2M<100word/wiki+Wikidata模板并按popularity采样，i9/3090，Qwen3-8B等AWQ，k10/τ.2/FIFO5000；fuzzy库缩小、τ提高、k变化有latency/RA反侧。ANN fullstore常驻、coldstart/FIFO更新、fallback和网络费都计；平均retrieval latency不等全生成SLO，seed/CI/concurrency Not Disclosed。root必要Source/owner普通。

### 2604.20460v1 CCTVBench

2+1+2=5，作者必要§3/4.2–4.5/Limit标准完成。非穷尽互斥问题和counterfactual视频形成(+,+)=yes、其余3no的quad；高video/question反应不等正确binding，四失败类可重叠且分母failedpairs。305scenes/1776pairs/7104QA，humanfilter+单drivingworldmodel生成counterpart；R3DlinearAUC56.7弱artifactcheck不证明onlyonechange，scene bootstrap2000也不补外部有效性。T0/defaultdecode，商业模型video-level batch与逐QA解析要保。C-TCD借本题给定counterpart，不是自然部署免费对照，VCD有Quad升而BaAcc降反侧。硬件/precision/latency/API版本等未披露不补造，不推广交通安全或真实因果。root必要Source/owner普通。

### 2604.20473v1 Video-ToC（准入门定点补读）

作者实际§III/IV-D/V：tree先用GT QA选clip再回溯caption合成SFT rationale，不是推理时实时树搜索。§III-C明示同题奖励γ/0在GRPO组内标准化抵消，因此另乘γ重加权优势；γ=e^(−directanswer8trialaccuracy)，筛难度.2–.8，是数据级难度proxy，不是每trajectory有益thinking标签或动态预算。TableV同SFT+GRPOvanilla/RD有有限局部比较，支持5 potential而非tree命名组合；具体准入待rootactual，不提前授标准Source或Books。

### 2604.20834v1 PokéVLA（准入门定点补读）

作者实际§V/VI-D：同一SEGtoken监督多视角目标mask，geometry只train-time VGGT cosinealignment，推理actionlatent分别cross-attend hseg、hv、actionquery/proprio。不同于只增加名字的expert，T6–7拆辅助任务/数据组与扰动条件有有限选择证据；不等已证明统一3D一致性/真实geometry或所有robustness。倾向5 potential，准入待rootactual；未授完整必要Source或Books。

### 2604.20348v1 BiCICLe

2+1+2=5，作者必要§3.1–3.4/4.1–4.3/B1–4/E标准完成。leader7D先生成完整keyframes，follower条件leader，而非独立双臂或joint14D；debate用freshprompt非累计history，BestN5需要10生成+5judge，pattern judge不验证physics。13TWIN/CoppeliaSim/6RGBD128/100³voxel/5°rotation/10ICLdemos/3seed×100；松耦合baseLF不优SA/DA、细接触离散化失败，rotation常退、leader选择单seed。只用sim机制不采未读真实机器人宣称；监督基线来自别文且训练数据量不同。E直接反侧：LiftBall21.5k→180.7ktoken仅+1.3pp，debate80<base83.7且更慢；并行较低中位不消高tail。精确API模型/网络等待和示范制备都计费，不授所有task优/无训练免费。root必要Source/owner普通。

### 2604.20354v1 HEaD+

2+1+2=5，作者必要§4–7/9标准完成。PFI/crossattention/CLIP对象文本→HPpresence，LP预测centroid核relation，AND gate可继续否则换seed；不是真实生成oracle。4100prompts×11seeds45kSD1.4/2、50steps，同prompt全部seed同split；GPT3.5抽对象/OWLv2标签与关系评估共享检测代理。MonteCarlo savings按每object独立模拟、successful但gateFN仍加fullcost，是模型化节省非实测全管线wallclock；5restartcap/最好predictedobjectcount与额外采样预算、误停正确image、关系/修饰binding未全检保留。LP仅两对象四方位/5seeds、5%图宽容忍，不推广物理关系真值。训练、检测、PFI/prediction与被拒绝seed都付费。root必要Source/owner普通。

### 2604.20472v1 TDQC

2+1+2=5，作者必要§4–6/D.7/E.4/E.7–9，公式/执行受影响深入待root。轨迹successlabel训练prefixTD/value而非将actiontokenprob当success；同SAFE架构换TD/BCE提供有限比较。§4min squared error错写p而非p(1−p)，§5 generalreturn回归等同success只在binaryterminal等条件成立；§5.2说高success跳search但Alg3 f≤threshold跳search，D.7又以failure为解释，未统一精确执行recipe。只隔离此强等价/搜索算法，不否定binary任务有限TD结果。CP校准successful轨迹且需exchangeability，仅控制误停success，不保证unsafe失败都检出或改policy后不漂移。4VLA/LIBERO/真实数据532WidowX和13Franka每类30+30、21seeds不同split；1000epoch/B512在不同表示中意味着steps或整rollout不同，单RTX5090，主风险和搜索simulator都计费。3新任务50rollout×3seed search在sim才有准确forwardmodel；少失败样本10%时退、CP跨task漂移保留。必要Source独核通过有限命题；Books普通。

### 2604.20487v1 External KVI

2+1+2=5，作者必要§3–4/5.1/7标准完成。symbolic triple+sentenceID外索引，frozenLLM离线anchor/tripleKV，querygraph+DRM选，再与rawsentences双channel；KV不含provenance，tokenoverlap删句不验证事实。Qwen2.5/Mistral7B、NQ100/Hotpot120与严格ID任务，科学应用结果不作主线采用。所谓completeablationgrid不纯控：KVPrefix用rawsentenceKV而KVI tripleKV+prompt，graph/表示/双channel共同变；表文w/oGraph22.5与RAG混指，不能唯一归因KV。位置/独立KVsplicing一致性、precision/hardware/全latency未披露；offline抽取/compile、KVbank存储、检索与prompt都计费，不授exactprefix或无重复语义信息。无清楚实体时fallback原模型，错误triple与非文本场景泛化未授。必要Source独核通过有限命题；Books普通。

### 2604.20544v1 Evian

2+1+2=5，作者必要§3–5/T4/Limit/A.1–2/D–E标准完成。原句tag知识/推断，净化visualsummary后logic/internal-knowledge/image三评分，缺推断/知识默认2，再均值选；不是外部事实核验。gold50k由SCALE净化非人类真值，250kdefect由同Qwen235B生成/decompose，共享生成器偏差不消。sameQwen7B auditor对照不等samepipeline预算，T4拆维度及InternVL2有限迁移不授universalquality。表8真实300k对10k选集虽平均略优但MMBench/SEED/ScienceQA/AOKVQA反退；保稀少判别/预算取舍，不将‘少样本’外推省总费。8H10080G/28h审计、另8vGPU48G SFT/ZeRO3/B128，visiontower冻结；多模型调用/净化丢claim/审计与训练计费，CI和seed不补造。必要Source独核通过有限命题；Books普通。

### 2604.20549v1 Multilingual Quality Filtering

2+1+2=5，作者必要§3–5/E/H/K标准完成。crossfamily过滤可迁移不等语言相似；Q3为初filter50–75%分位负样，retention与重复率共同限定质量/覆盖。4语言、固定XLMR embedding/MLP，ML同时扩anchor池不只pooling；Nordic优Romance-noFR不证抽象qualitymanifold，格式/anchorartifact未消。1B Apertus103Btokens/B2.06M/BF16/84GH200/50kstep；阿语10%/20%分别10×/5×重复反退，.5%增益接近seed.3%，法语classifierseed差.8%，主single-run，不把rank变成稳健普遍最优。filter训练/全库打分、重水化、数据重复与下游训练均计费；弱代表语言、embedding换代时回退单语/较宽retention。必要Source独核通过有限命题；Books普通。

### 2604.20570v1 GSI

2+1+2=5，作者必要§3–6/T3–4标准完成。10500synthetic spatialediting/sceneseparated训练BAGEL→理解迁移是有限选择，不是生成普遍增强理解。Omni overall41.55→42.07但Logic32.14→28.97；SAT65.33→69.33但EgoAct75.68→72.97/ObjM不变。Real441/211scene以DetAny3D重构+Qwen235B/humancheck，真实无GTeditedimage；IC/SA的合理tolerance+localitygate非物理oracle。Syn593/600/200新view，9模型default不同协议，不能平均作唯一机制归因。正文指appendix给threshold/训练细节，但当前HTML无appendix；hardware/precision/seedCI/全部训练预算Not Disclosed，拟采用有限transfer与反侧不补造它们。必要Source独核通过有限命题；Books普通。

### 2604.20601v1 SuperIgor

2+1+2=5，作者必要§3–6/Limit/I标准完成。初cycle一次完整planpool，后DPO按executor成功重排/筛subset，不是持续自由生成新计划；mastered≥70%只扩atmostone新skill，DONE由executor学，LLMontology不是真prerequisite。§6.2 env5B/15Bfixedplanner与rewardfilter反侧支持有限coadaptation，不包含plan生成/DPO/评价全部费用；newobjects静态筛更差，§5.4自身newobject下降仍称improve不能照录。Qwen14B DPO1epochβ.5+PPO-T2.5B/cycle×2，10plans×50seed，A10080G，5B120GPUh、plan1–2h/DPO15h；生成/ontology/筛选和两模型训练都计费。不授计划无环、泛化全优或真实环境安全。必要Source独核通过有限命题；Books普通。

### 2604.20627v1 ORS

2+1+2=5，作者必要§3–5/A.3–4/A.6/B.8标准完成；采用offline futureoccupancy(flow)+goalvelocitydifference surrogate reward后训GCIQL，不是普通gammaPhiNext−Phi shaping。理论要求deterministic、squaredEuclideanPhi对shortestpath强层单调、datasetpolicy successors保持层序等条件；实际velocityMSE只W2 upperbound，不等真实W2/reachability，不授任意noisyoffline最优不变。OGBench12任务/5goals/8seeds，有antmazeexplore低GoFresh、κ依locomotion/manipulation变；A6000，occup14ms/reward8ms/policy6.5ms，前两各约500k轮，不能只计policy费用。Tokamak科学应用不作主线证据/Books，不扩该领域。不采用广泛保证故不进一步全proof，必要Source独核通过有限命题；Books普通。

### 2604.20659v1 GRPO-VPS

2+1+2=5，作者必要§3–4/A.1/A.4.3标准完成。entropy-percentile均衡cutpoint分段、已知GTanswer在prefix前后条件likelihood差ΔC加到outcomeadvantage，不是过程真实性或因果verifier；Eq5只有groupmean不除std，Alg1 segment内update与group叙述不闭，不能照精确recipe。PRM800K100题×6响应去neutral后binary与人工相关，不覆盖neutral/真实必要性。QwenMath1.5/7B+Gemma2B、MATH7500/G8/T1/max3072/B512/pass@1四run；正文8H800 vsA.1 8H100冲突保留。固定partition6的评分budget更大、n2更慢、移除outcome退/α过大回落；额外prefixscoring/entropy/rollout/训练都计费，短输出非端到端省费证明。必要Source独核通过有限命题；Books普通。

### 2604.20665v1 Semantic Sufficiency Criterion

2+1+2=5，作者§2–6受影响中心主张深入，待root裁中心D。三representation对照是具体替代评价，但金融95vs60/医学/分子均‘projecthow’假设例非实验。ToS=SsymT−Sfull、CoS=SsymT−SsymV、FoS=Sfull−SsymV恒有FoS=CoS−ToS；正负不识别encoder/projector(渲染/OCR/位置/融合/训练support共同变)，exhaustivesymbolictext非已证LLM绝对ceiling，lossy亦非语义等价。SSC max(ToS,CoS,absFoS)=0只约束相对分数不证明正确；scale图是hypothesis无matchedscaling证据，不授divergencelaw、普遍架构因果或regulatory规则。科学案例不作项目证据；不为后续泛建议再全读，中心强主张与Books正面链隔离，root待核。

### 2604.20677v1 Intersectional Fairness

2+1+2=5，作者必要§4.2–4.5/4.7/5.2/6标准完成。unknown占优使groupdisparity稀疏，低observable不等公平；modalansweragreement与truthagreement不同。人口原文冲突：3720−840写3300(应2880，下段也2880)，RQ2仍以8952preexclusion称5%，实际448平衡抽224each/56slice，20次共53760calls，不能写全池20run。六模型因版本deprecated替换，T1不消provider/版本/硬件条件差。sDIS删除unknown分母、SF favorable与groundtruthpositive口径未统一、DF零prob稀疏，不采用统一fairness数值结论；稳定可持续错也不等每项bias已证。API/重复采样/人口审核全部计费，范围限两BBQintersection。必要Source独核通过有限命题；Books普通。

### 2604.20682v1 Structural Compression Failure Modes

2+1+2=5，作者必要§3–7标准完成。高PCA保能不保功能、单blockridge拟合好不组成等价、posthocexithead高confidence可错，是具体可复用反侧。8192fit/16samplesheldoutPPL、GPT2/Mistral7B；extended另三model866ktokens不与主实验混。naivefactorquantization cross terms没有普遍strictlyworse定理，文自己给GPTQerrorfeedback例外；30%top1agreement不是可安全skip人口或架构ceiling，扩训可35–53%。不采所有静态compression不可能/普遍四phase或省算数当实测SLO。保校准数据不足、单域、不同fit/token预算与额外head/LoRA成本；硬件/precision/完整seedCI未披露不补造。必要Source独核通过有限命题；Books普通。

### 2604.20685v1 MGDA-Decoupled

2+1+2=5，作者必要§2–4/A.1标准完成。以g/L求系数再applyrawg，不能继承normalized-MGDA common-descent或到Paretofront更近证明，loss依相同DPO/正值proxy而非真实distance。UltraFeedback49k/15k同prompt四属性重配pair，Gemma2B/Qwen.5B，Qwen三perattribute normalized更好而overalldecoupled好，非全优。主文Adam/lr5e-7与A.1AdamW/lr1e-7冲突保留；BF16/1B200/B32/max1024/β.5/epoch1，oversample小属性池改变人口。GramQP开销随k²，GPT4ojudge+poolhighest-sumgolden非人类Paretooracle，额外forward/backward及judge都计费。只保有限系数选择/应用空间分离，不照统一recipe或优化保证。必要Source独核通过有限命题；Books普通。

### 2604.20705v1 SSL-R1

2+1+2=5，作者必要§3–4标准完成。五成熟SSL任务转合成index/rotation标签GRPO，实际新增边界是多任务/难度对迁移有反向切片。G16/B256/1000single与2000multi steps，COCO118k→591k等任务；binary或indexfraction+format.2，几何操作标签可核不认证推理忠实。LISAmulti<single、Omni两task>五task、视觉相似训练损inpainting、rotation过难退；更多采样/增强/updates计费，hardware/precision/CI Not Disclosed，不签100%reasoningverifiable。必要Source独核通过有限命题；Books普通。

### 2604.20715v1 GeoRelight

2+1+2=5，作者必要§3–4/6.3–6.5/8/12完成，受影响iNOD强重建主张深入待root。modality-as-time+conditionmask、ITW自标intrinsics→原图denoise支持缺标签训练任务分配；GTgeometry/GTappearance对zero模态改变可见信息不唯一归因jointcausal。§8.1 Alg1先metricunproject/isotropicscale，Step4仍用原pixels_uv回写z，没有按normalizedXY重采样，不能靠orthographicunprojection无K恢复原shape/relative3D，精确distortionfree主张隔离。7B/64A10080G/BF16/B128/30kSynth+10kmix(.33/.35/.32)/5days；35step单A10035s含VAE+IO不授所有配置。HumanOLAT NeuralGaffer指标反侧、texturegeometry混淆/flicker/OOD/长depthratio保留，离线自标/额外五模态训练都计费。必要Source独核通过有限命题；Books普通。

### 2604.20720v1 COMPASS

2+1+2=5，作者必要§3/4.3/5.7/6.1/F标准完成。devinput语义cluster缺口而非语言距离选aux+DoRA，JS触发centroidanchors/EWC；proxy非真实live，encoder差覆盖语言会跨无关任务污染，Distiluse可低于random/base。JSperformanceblind、固定treeclusterstale不能授selfcorrecting。原式boundaryscore=minotherdist−owndist实际大值偏中心非边界；quota Bernoulli非恒定总额、负penalty/emptyguard未闭，bias降至20%却写删50%，不照完整recipe。Phi3.8/Llama8/Qwen7/Aya/42languages，B128/3epoch/DoRA rank16或8，FFTB16等条件差；embed42min/CPUcluster2.2h+adapter44–105min高于target18–50min，不只少样本就省费。residentlanguage/adapter路由不等coldload恒费，必要Source独核通过有限命题；Books普通。

### 2604.20730v1 Render-in-the-Loop

2+1+2=5，作者必要§3/4.1/4.3/Limit/A核心标准完成。SVGsubpath含洞/opacity交叠先依赖component合并为原子，再interleaverender训练；未经此训练naivefeedback会退，不是所有反馈自然有益。RaV小pixeldiff/repeat拒后有限重采样，失败强END非完成证据，可能误停微细节/隐藏背景；路径分解声明保视觉不授完整SVG语义等价。Qwen3VL8B/8H100/epoch3/224²49tokens/ctx10240，850k与baseline不同数据/updates/renderbudget，少样本不等全费用低。rerender/visionencoding/retry/history都付费，HTML/CAD/TikZ等迁移仅未来建议不采用。必要Source独核通过有限命题；Books普通。

### 2604.20755v1 V-tableR1

2+1+2=5，作者必要§3–4标准完成。输出cell坐标/valueanchor，32Bcritic学8B合成扰动severity给trajectoryscalarproc；正确outcome时高/低proc bonus或减answercredit，再group归一。不是逐step形式验证/因果credit，grid确定不使learnedcritic成为真实checker。length仅保bottom30及60–90%已完整rollout，不能省生成费用；50step消融、1000GPT5judge不证内部anchorfaithfulness或globaloptimum。Qwen3VL2/4B，hardware/precision/B/clip/rewardthreshold/seedCI当前文ND；critic合成/训练/评分及完整rollout计费，不照完整recipe/全tableSOTA。必要Source独核通过有限命题；Books普通。

### 2604.20763v1 Stratified Retrieval Evaluation

2+1+2=5，作者必要§3–5/7标准完成。corpusentitygraph/Leiden+queryJaccard/dispersion分层，§5.5同benchmark按overall或macro加权可反转model选择；1000bootstrap不是部署胜率。理论bias条件给定regimecomposition与wknown，不是iidsamplemean本身有偏；实际多cluster关联与理想partition分开，缺slice不由bootstrap补全。LLMextract/generate/qrel(dense+BM25pool)非人类真值，词名缺席不等语义不可答，≥5query非可靠CI证书。BEIR三领域仅采检索评价机制不采用科学内容；textembedding3large/BM25/RRF60，nDCG/Recall/MAP不同consumer。API/graph/LLM与全costND，必要Source独核通过有限命题；Books普通。

### 2604.20779v1 SWE-chat

2+1+2=5，作者必要§2/4/A/C.3/D.5标准完成。checkpoint→commitline linkage区分成功标签/代码保留/成本/安全分母；48.6%可无歧义join才算commit-session指标，弃用未commit失败日志大多缺失。90%success是LLMannotation非独立验收；publicopt-in/earlyadopter/85%Claude/Entire自仓集中，codingmode内生不证明vibe因果。Semgrepauto before/after只modifiedfiles，pathjoining单rule主导，跨语言规则差异/扫描finding不等真实独立漏洞或生产风险倍数。用户阅读/前后人工工作未全计，不把tokens/committedline当生产率，repo/commit/agent版本身份须固定。必要Source独核通过有限命题；Books普通。

### 2604.20789v1 Working-memory Attention Constraints

2+1+2=5，作者必要§3–5/Limit/A.3标准完成。GPT2从scratch固定4/5/7/9每层mask及primacy/recency/exp/logisticbias，10MEnglish强localbias BLiMP优，100Mgap缩/部分不优，island/NPI仍差。12layerlocalW不是整模型history只W、token非认知chunk；改score也不等postsoftmax严格forgetting，心理读时fit非人类WM机制已证。两语料各训tokenizer同时变化，正文B64又50/A3为64冲突，不擅统一；AdamW5e-5/5epochs，hardware/precision/seedCI ND，句子显著性非训练seed鲁棒。必要Source独核通过有限命题；Books普通。

### 2604.20796v1 LLaDA2.0-Uni

2+2+2=6，作者必要§2/4/5.5标准完成。sameSigLIP-VQsemanticdiscretetokens供理解/生成，16BMoEdLLM+另6Bflowdecoder；不是一个decoder全并行。SPRINT每block首fullforward后按modality/Knorm/confidence剪prefix再adaptiveunmask，非lossless。§2.3 rtext1/rimg.8或full1又称globalr.5字段冲突，不照精确比例；confidence不认证正确，OCR/DPG反退，低τ与steps联动。24.3→39.8TPS是nosglang不同benchmark平均，不等joint1024render端到端；decoder50→8step另B1BF16/singleGPU型号ND、CFG同时变，GenEval.89→.87保留。offlinepreextract/packing/dFactory只公开配置，loadbalanceEq4写F−Q加bias未核实现方向不采用exactupdate。各encoder/decoder/distill/存储与训练计费，必要Source独核通过有限命题；Books普通。

### 2604.20801v1 AgentFlow

2+1+2=5，作者必要§4–7标准完成（`SUP_CORE_20801v1_20261015.raw.html`）。typed DSL联合修改node/topology/prompt/tool/retry；free-variable、edge-use/source-reachability及smoke test、最多两次修复后保留incumbent，是有限预算guard，不授授权隔离或liveness。TerminalBench89反复用于diagnosis/selection，非独立held-out；aggregate优不等七category逐项优，edit-family消融同时改变搜索空间。20% malformed分母是proposer tokens非程序数，ASAN signature非独立bug。Chrome七天192H100案例与对照总费不等；CVE/zero-day未独立vendor核验，不采用真实逃逸/生产安全结论。provider默认、cache命中及完整诊断/重放费用须绑定，用户评审时间ND。拟采用workflow搜索/验证分层及评价复用边界，必要Source独核通过有限命题；Books普通。

### 2604.20816v1 ParetoSlider

2+2+2=6，作者必要§4–5/A.1/B协议/C标准完成（`SUP_CORE_20816v1_20261015.raw.html`）。同(c,ω)组内各reward独立normalize后分别构造NFTloss，最后按ω合并；condition MLP进入time/shared residual或Flux AdaLN，LoRA+EMA old/reference。不是直接优化raw加权reward，也不由线性权重保证非凸Paretofront覆盖；std改变指标单位。early/late/STCH coverage近似，late的中间点视觉平滑仅有限观察。100testprompts/5ω，fixed-weight五模型各九epoch对比FlowMulti300steps、rewrite三点不是matched全费用；HV依global minmax和reference origin代理。SD3.5Medium/FluxKontext/LTX2，warmstart PickScore/CLIP；坏reward扭曲整个surface、gray不等sketch，T2V主要qualitative，不作所有偏好连续可控保证。必要Source独核通过有限命题；Books普通。

### 2604.20817v1 Fourier Number Embeddings

2+1+2=5，作者受影响深入§3–5完成（`SUP_CORE_20817v1_20261015.raw.html`）。中心D：Theorem1(i)由Phi_T=0推出任何linear probe不超chance不成立。N=4/T=2/d=1，e(0..3)=[−2,−1,2,1]，两residue均值皆零，故Phi_2=0；但阈值x>1.5判residue0、其余判1可得3/4，超过1/2。equal mean只限制均值分离，不排方差/分布可线性不均衡切割。Fisher最大特征值不能充当任意linear accuracy绝对ceiling；Phi=N·tr(SB)与正文tr(SB)/N口径冲突。可保谱峰经验相关，不采用modular可读性必要条件/因果保证。300M/10B FineWeb/Llama3、0–999；30probe是3seed×10fold非30训练seed，Muon/AdamW有架构反侧，grokking另三seed。fresh已actual独核中心D，不进入正面Books。

### 2604.20819v1 Stream-CQSA

2+2+2=6，作者必要§2–4标准完成（`SUP_CORE_20819v1_20261015.raw.html`）。Steiner subsequence在存在的c=l(l−1)+1参数下覆盖attention pair；对每段分别累加未归一Num=PV和Den，再scatter-add统一归一，重复对角只交单一子序列负责、mask递归继承；backward按dNum/dDen重算并scatter gradients。可采实数算术的覆盖/归一分工，不授bitwise/numerical exact。§4由FlashAttention的normalized out/lse重建Den=exp(lse)、Num=out·Den，未交代跨段共同max-stabilization，不能补造溢出/下溢防护已实现。OOM退回queue、缩ncap或增加递归，不证明host全量accumulator也能容纳，部分累加重放的rollback未闭。

§2.4 B1/H64/D128/fp16/A10080GiB，SDPA到900k OOM后1M92.53GiB/223s是多项式外推；§3实际B1/H1/D128且nparallel=ncap=1，非异构多卡部署。1B token仅实测七个缩尺subsequence再外推7^itr，未实际执行完整1B forward/backward或训练整model。timing含mask/gather/H2D/D2H/compute/merge但排random QKV生成；二次总计算与host内存未消失，独立task不等整系统无通信。有限分解/transfer-budget选择足，不采无OOM/全规模性能保证。必要Source独核通过有限命题；Books普通。

### 2604.20835v1 Parallel-SFT

2+1+2=5，作者必要§3–7/Limit/B/D标准完成（`SUP_CORE_20835v1_20261015.raw.html`）。固定3111问题/142k code样本，与8language disjoint-question nonparallel对照；parallel让每题跨八语言出现，后只Python/C++ RL向未见Go/PHP/Ruby迁移。不是单纯多语种数目效应，但每题每语种的解数/分布仍改变，alignment相关不证明中层语义hub因果。Maverick400B合成约6.2M，经已有tests过滤只证所测用例非任意功能等价，筛去CodeForces防直接任务重叠。Llama3.1-8B base+替换Tulu3 142k coding的SFT；RL codegen6617train/377test B16、validation B32/200steps/lr5e-7；hardware/precision/训练seed CI/SFT全配置ND，不补造省费。8samples每题非8训练seed，validation人为类平衡。Python500steps parallel12.36 vs nonparallel12.47且CI重叠，只支持未检出损失，非证明永不牺牲；无validation target oracle。generation可用语言无关prompt/test直接在target训练，实际缺口更适合code validation；未测试coding agent/production generalization。必要Source独核通过有限命题；Books普通。

### 2604.19859v1 DR-Venus

2+1+2=5，作者必要§2–3标准完成（`SUP_CORE_19859v1_20261015.raw.html`）。10,001原轨迹清洗到9365、按turn1/2/5倍resample18745；same-source消融显示长轨迹权重与IGPO/GRPO的局部反向选择，不因4B或10k本身准入。IG是当前policy对gold answer平均logprob的turn差，browse得分沿上次browse后的search回传；format错误替换为−λ，IG/outcome各自groupnormalize，再可选IG-Scale及discount cumulative reward分给同turn token。它不是独立证据真值/信息熵或无偏过程credit；γ.95/normalize也不保简单potential telescoping。Table2 IGPO优GRPO有有限证据，但未单独拆IG/browse/scale/format全部因素，不能只归因dense reward。

Qwen3-4B Thinking、SFT8A100/200k/B32/epoch1/lr1e-5、RL16A100/B16/G8/T1/256k context/8192每turn，precision/训练时间/seedCI ND；小样本bench三次eval其余单次，不等独立训练复现。search Serper top10、browse Jina+30B summarizer，4B不是整个系统边缘资源。GAIA SFT65.4→RL64.4；中文pass16 SFT78.5→RL76.5，pass16不能直接比较他模pass1；browse ratio与成功相关非因果。清除toolturn后后续推理依赖完整性未另证，judge235B筛选/重采样/每turn goldscore/外tool全费均计，标题frontier不作同预算优势。必要Source独核通过有限命题；Books普通。

### 2604.20500v1 Distinct Leaf Enumeration

2+2+2=6，作者必要§3–4/A/C.2/D.3标准完成。truncated token tree按已见高prefix mass选分支、greedy suffix枚举distinct leaf，prefix KV复用把重复采样预算换成未见路径。有限树全遍历才支持同support；固定k greedy并非topk全序列最优，C.2仅nexttoken局部最优、忽略futurevalue，不能拿coverage质量相关作正确率保证。10tokens与兄弟suffix相同即earlystop是近似语义merge，作者自己仅85%以上被剪枝同answer，非lossless。主Qwen2.5-.5B/GSM8K/HumanEval/MMLUPro、B200或H100/vLLM及SGLang；precision/inputlength/concurrency/SLO/seedCI ND，不推广所有load。SGLang优势主B1/2，大batch可并行sampling缩差；fixedtokenbudget逐条生成，不等同并发端到端预算。coverage是truncated Q概率质量非语义多样/真实答案覆盖，uniform vote优weighted也不授概率校准；总tree管理/KV占用计费。必要Source独核通过有限命题；Books普通。

### 2604.20572v1 ProactAgent

2+2+2=6，作者必要§3–4/A/D标准完成。typed事实/episode/success/failure/comparative memory与显式retrieve action共演化；相同prefix replay选一个内部retrieval点，对照suppress retrieval后的sampledsuffix，用环境return差和length形成局部process bonus，再GRPO。附A明确single-sample shaped noisy proxy、非unbiased marginalutility/严格causal isolation；exact replay、固定memory/deterministicretriever是必要前提，runtime克隆能力不能由文字自动授予。D2排首末retrieval且uniform选interior，少于三次时实现分支ND；nomemory branch又start-memory disabled，不能擅称只有该retrieval唯一差异。α.5/repeatquery penalty.5/step .25，训练ret-disabled从.5→.25→0；full参数0disabled不等所有训练步骤都有matchedpair。

Qwen2.5-7B/3B、Qwen3-32B抽取、MiniLM/FAISS/k5每type一，hardware/precision/B/G/总训练updates/seedCI ND。消融w/o online参数SR71.5<73.5但rounds17.15<18.38，非每指标全优；offline/online不同teststream经验暴露不能当独立heldout推理同费。0.43k是平均prompttoken口径，不含pairedbranches/experience extraction/更新完整费用；仅采Agent互动benchmark的检索选择机制，不引入SciWorld科学应用知识。必要Source独核通过有限命题；Books普通。

### 2604.20446v1 Origin of Edge of Stability

2+1+2=5，作者必要§2–5条件与公式标准完成。对固定步长full-batch GD，uniform step-averaged Hessian支配dnext=(I−ηHbar)d，triangular average支配losschange，二者不可混同endpoint Hessian。telescoping给加权曲率平均；趋2/η需trajectory上loss上下有界且Σ||d||²→∞，step-level集中另需累计above-threshold预算B+有限。仅bounded-below不能推出全局attractor/每步sharpness都2/η：二次convex在小步长收敛、Σ||d||²有限是直接反侧。MVT只在segment内存在点且λmax≥directional curvature，非endpoint最大特征等式/上界。local C4+nondegenerate center与quartic branch条件限制period-two分析；不授任意过参深网Morse-Bott/width invariance，未为这些未采用强桥全读附录。

有限身份与近两周期→directional curvature界可复核代数；两层linear p5/h3/d10/rank3/n200与四lr4000step仅示例，非LLM/SGD/Adam普遍稳定保证。oscillatory cancellation另要求multiplier∈[−1,0]与forcing variation控制，不由‘oscillation’自动授予boundedness。硬件/precision/seedCI对数学身份不适用，实验配置不足不外推系统recipe。必要Source独核通过有限命题；Books普通。

### 2604.20614v1 Calibration Follows Curvature

2+1+2=5，作者必要§3–5标准完成。小MLP CIFAR10跟踪GN sharpness与ECE/KCE：SAM flatter仍类似calibration，Muon/BulkSGD方向干预不同；训练内关联不等终点flatness因果，test ECE可随training锐度下降而上升。Theorem4的true/robustmargin与boundedJacobian前提不能替换predicted margin、GN也不是完整Hessian。CalMO=CE+clean/PGDKL+inputmargin梯度平方，局部point梯度不自动等于整个ε邻域Lipschitz上界，不签附近test全继承margin；正文称MSE非proper scoring rule不采用（概率Brier/MSE为proper，混淆优化/参数化与scoring-rule性质）。

ResNet20/CIFAR10/B128/10ksteps，SGD/Muon/SAM lr.01、AdamW.001，λr.5/λs.01、PGD3step ε8/255/step2/255无randomstart，ECE15bins，bestvalidationstep；只采用有限优化器相关反侧/校准干预。匹配steps不等匹配3PGD+额外forward/inputgrad全部compute，‘CE再训不补’不代替严格等费控制；hardware/precision/独立训练seedCI ND，不把小ECE差视稳定。完整theorem普遍推广与LLM生成校准未采用，无需全proof。必要Source独核通过有限命题；Books普通。

### 2604.20564v1 Logical Connective Control

2+1+2=5，作者必要§3.3–3.4/4–6/Limit/C/E标准完成。单connective替换对照highentropy非connective显示有限敏感切片，不能由最终答案变化证明chainfaithfulness/逻辑唯一因果。global normalized logprob gradient只局部增加参考token、非隔离‘logical subspace’；top1/connective且top20≥2触发20tokenlookahead，entropy+logprob相对zscore选择不是正确性oracle。TTPO参考ratio仅单token偏好loss，branch完整greedy到EOS依gold答案贴标签；仍更新共享参数，非保证其他token不受影响/无遗忘。Zebra8:2，TTPO3epoch/B1/lr4B1e-6、文写13B1e-7而主Gemma12B不自行改；hardware/precision/独立seedCI ND。

§6.2 groundtruth candidate强行加入且同构造dataset，73.4/69.1%不等部署unknowncandidate正确率；connective稀疏任务机会少、tokenizer/polysemy明确限制。token成本含lookahead、walltime是Zebra小模型相对greedy，不包括steervector/TTPO数据生成训练费；按task选best再平均不等单一通用policy。只采用有限pivot-selection取舍，非logic guarantee。必要Source独核通过有限命题；Books普通。

### 2604.20714v1 Textual Parameter Graph Optimization

2+1+2=5，作者必要§4–5/7/C标准完成。role/logic/tool text graph+rewrite/prune/add；negativefeedback embedding/DBSCAN聚类，按同失败子集验证edit→保存context/proposal/effectiveness，GRAO按similarity再effectiveness重排正负ICL不是GRPO/数值gradient或meta参数训练。targetedsubset rollback只护该子集，不保证其它能力；prompt删tooldescription不自动撤销executor真实权限。附C GAIA142textonly、gold入reflector且同validation优化/汇报，prompt要求generalize不证明无答案泄漏；跨domain有限MCP对照可保，不签GAIA独立泛化。T1 DeepSeek第一轮overall34.77→34.72，T2 GAIA第一轮73.8→70.59，非单调安全提升。

ReAct GPT4.1/DeepSeek3.2 T1/topP1，MiroFlow GPT5 high/medium，Gemini2.5Pro T.7/topP.95做meta，MiniLM DBSCANε.3/min2，最多五轮；API retry3/8concurrency、GAIA一轮19.9Mtokens1380s，73.7k/5.6s amortized分母与实际142task不直接同一，不能当全部optimcost或部署SLO。没有独立seedCI/完整模型revision，finite经验提示聚合收益，不授formal optimization或生产rollbacksafety。必要Source独核通过有限命题；Books普通。

### 2604.20733v1 Near-Future Policy Optimization

2+2+2=6，作者必要§3–4标准完成。训练先前进Δ、离线gold验证成功轨迹缓存，回退后低pass组替换一个slot；原onpolicy n条仍先完整生成，缓存/前进/重放训练不免费。AutoNPO warning用rewardEMA/entropy，probe mistakepool、按Qhat/Vhat选checkpoint，再仅该pool缓存/重放；near checkpoint并不理论保证ratio近1或低variance，忽略IS仅该单配置消融可支持，不能写普遍safe。成功筛选并每prompt只保一条改变实际guidance分布，分母用原future policy的tokenprob不是选后样本的exact IS；标注‘exact’不予继承。

Qwen3VL8B/EasyVideoR1、32H200140G、B256/G8/T1/lr1e-6/8192=4096+4096/clip.2,.28/noKL或entropyreg，precision/seedCI/全GPU时ND。八bench平均与可选passgate.6只该任务分布，Auto版本pool触发与manual低passgate不同不能混成同一recipe。正文引用AppendixB variance指数推导但本HTML正文止bib，无可读附录，不以其强理论作依赖；有限trajectory-source/预算取舍已足，不为未采用保证恢复全附件。必要Source独核通过有限命题；Books普通。

### 2604.20728v1 Interval POMDP Shielding

2+2+2=6，作者必要§III–VI标准及受影响guarantee条件完成。known dynamics+uncertain emission，McCormick外松弛bilinear posterior、Charnes-Cooper归一、固定template每facet LP形成reachable belief外包，再对每action线性safety score取inf；外包仅删可行动作不授点估计同等鲁棒。CP entrywise区间加unionbound提供训练集随机性的model-containment λ，前提binomial样本/固定perception kernel，非任意drift安全。V1是history下Ω-admissibility≥β；V2另需initialC、PCIS一步γ与每步可行动作、其safe-prefix条件不能仅由无条件h posterior自动忽略，完整path guarantee未作正面依赖，fresh已actual反例独核，V2强桥终态隔离。

四有限IPOMDP/DQN同controller，200rollouts×各β，选择minfail再minstuck与maxsafe是不同consumer，非共同β公平全胜。Taxi/Obstacle envelope更保守且可能多stuck；CartPole/Refuel LP sweep不可行，forward sampling是under-approx不继承robustness。uniform步步采kernel/adversarial固定kernel离线crossentropy搜索是两种protocol。EPYC9454P/48cores，shield单call不含controller/env；Taxi83.1ms/Obstacle643.1ms与microsecond单belief不可隐去。finite已知环境模型不等LLM自然界动作safe，sampling/LP/离线Ω合成和标注校准全费。必要Source独核通过有限命题；Books普通。

### 2604.20811v1 Diagnosing CFG Interpretation

2+1+2=5，作者必要§3–6/Limit标准完成。随机lexicon/style/ASTdepth与expressiondepth分开，Lark parseability、同initialstate最终state相同BER、exactAST匹配SCR三个consumer，条件CBER/CSCR分母仅validoutputs；SCR是结构忠实代理非一般语义等价，AST不同也可正确实现指令。BER是单initialstate非所有输入等价，端状态相同不证执行trace正确；Task1 SVR=判别accuracy与Task2/3 SVR=parse rate不能混汇总。200/task/D10/blockAlien/0shotCoT，多model当前API身份未固定revision；MiMo ablation depth/expr/else/style/lexicon改变有界负面证据，0→1shot反退不授示例必有益。CoT显著好也不证明tracefaithfulness/普遍必要，随机opaque token改变tokenization/length、不能宣称清除全部预训练先验。hardware不适用于API，temperature/precision/seedCI/totalcost ND；不据单API样本排名判模型scale定律，模板任务非自然agent生产评估。必要Source独核通过有限命题；Books普通。

### 2604.20470v1 DynamicRad

2+2+2=6，作者必要§3–4/B–D受影响标准完成。promptembedding→flowproxy训2layerrouter→low/mid/high lookup；offlineTPE30trials/ARfeatureproxy选结构稀疏候选，再staticratio或头融合logit threshold、可选maskLoRA。content只在候选内选，保一pair不保证每个query保可用语义；softmask log(M+ε)也非严格−∞hardmask。flow magnitude非physics truth、proxy MSE不自动等生成quality，C.6只定性例而无quant correlation；C.3指数tail假设和Eq21 outlier减项未证明normalized attention误差/strictly superior，不用此理论桥。

FlashInfer B32/H100，241f8H100sequenceparallel、其它single，768p1280×768，longcontext backbone另finetune，maskLoRAr16/1ksteps、router20kpairs/RAFT<1h，precision/seedCI ND。Table3 static338s更快但VisionReward.117<原.123、SC.946<.956；dynamic385s也慢且.119/.948，并非无代价支配。AppendixB称不提供hardware breakdown，D又0.37ms实测/0.5ms theoretical fusedmask排Pythonprototype成本，不能把混合估计说完整实测端到端。BO/RAFT/router/LoRA/profile费计入；只保有限static/dynamic选择，不授全video质量保证或调参数学最优。必要Source独核通过有限命题；Books普通。

### 2604.20486v1 ProMMSearchAgent

2+2+2=6，作者必要§3–4/T2–3/AppD标准完成。eight direct samples任一正确贴tool-free、全错贴required作为fixed元数据，再独立outcome/行为(是否call)/format以7:2:1加权；不是独立knowledge-boundary真值，200审查78.5%才支持多数，推理失败/运气可误贴。加法分工避免特定multiplicativepenalty，不代表无rewardconflict或真实过程credit，任何tool都可领behavior分。T2 NoBehavior MMSearch58.5>full55.2，higherweight各accuracy退；TR接近100不等每call无效，不能照‘full全胜/鲁棒’。

Qwen2.5VL7B/6549/B128/G8/epoch2/lr1e-6/8GPU型号ND、precision/seedCI ND，AppD rollout SGLang Async；作者最初误混别篇而称正文vLLM，与本v1不符，fresh实际全文纠正后删除该冲突判断。Qwen72B judge见gold、train/test共享judge。trainlocalWiki/e5而eval liveSerper，image search训练及测试均事先缓存top10含webtitles，‘never liveweb’不适用于整pipeline。oneepoch50.71→48.83相对tooltime6017.81→457.3s而非GPU全训练walltime，precache/embedding/数据清洗/judge全费。246同query换backend64.1vs56.1仅有限切换证据，非engine-invariant普遍证明；LiveVQA2384不同旧3602不直比。必要Source独核通过有限命题；Books普通。

### 2604.20841v1 DeVI

2+2+2=6，作者必要§4–5/A.6–10/C标准完成。syntheticI2V→3D human estimate+2D visibleobjecttracks，scene初始mesh/camera已知，visualalignment上身pose+2Djoint/temporal/初始object Chamfer再PPO；hybrid 3Dhuman/2Dobject consumer避免强求全6Dobject估计，但不是从单视频唯一恢复真实3D或真实接触。min_t HOIloss只迫至少一帧靠初始object，不授整段contact；contact由pixelvelocity并反向扩静止段、缺depthmotion会误标，作者承认抢夺/精确放置失败。Ro印exp(+λo error²)未给λ符号，PPO式23 clip分支缺adv项，不照录exact implementation或补造纠错；有限目标分工不依这些强recipe。

GRAB16段<7s、baseline单motion，error只双方成功子集有selection bias；276合成video/12类别alignment metric对同estimator，不等真实motion GT。main success称MPJPE/Tobj两阈值，附T3又含Oobj三阈值不能混成同分母。IsaacGym4096env/32rollout/B1024、actorAdam2e-5/critic1e-4，A6000单卡250frame约20h、precision/seedCI ND；每motion训练非零样本直接控制/跨object通用policy。earlytermination均body200mm/任意400mm/finger40mm/pixel.08diag，失败停机不等物理safety。视频生成/估计/对齐/每motion RL全费用计，不采用‘sim physically feasible⇒realrobot safe’。必要Source独核通过有限命题；Books普通。

### 2604.20505v1 Explicit Dropout

2+1+2=5，作者PDF必要pp3–6/8–12受影响深入完成，p4/9公式另外渲染实看。中心D：文称inverted dropout但实际mask m∈{0,1}无1/(1−p)，A.2把同坐标对角m_j与m_j视为独立，故B≈p²XᵀX错误。按其实际unscaled mask，应E[B]=p²XᵀX+p(1−p)diag(diag(XᵀX))；一维X=1、p=.5即真实B=.5非.25，增样本不消该差。真inverted的零均值差应仅p/(1−p)diag项。AV A.5同一entry相乘同错；FF第二层输入应为中间激活而非同一个X，不自动跨非线性。主定义是linear/score discrepancy，不是一般softmax下taskloss期望精确等价。

不采用dropout-equivalent deterministicregularizer/从旧理论继承generalization保证，打印误差不由自由λ统一修正跨特征形状。CIFAR10小7layerViT、THUMOS/GTZAN2layer预提取feature实验可保有限作者观察但不独立证实理论；CIFAR100 DropKey59.11而explicit V55.15/AV56.62反侧，不能全任务match。p.2、70:30train/validation、bestvalidation超参、五seed均std已披露；hardware/precision/epochs/全搜索预算ND，不签省费/LLM迁移。该中心D与依赖正面Books链隔离，root已actual独核必要p3–4/A2(p8–9)，不再为不采用强桥扫其它附件。

### 20473/20834 必要配置与反侧补齐（承接各自A5方法，不增家族）

20473作者IV-A–D完整补读：Qwen2.5VL7B caption、Llama3.3-70B看gold QA选择clip/过滤并要求‘假装不知道答案’生成rationale，不授真实推理轨迹或过程faithfulness。构造SFT约A6000一GPUday、RL集14GPUh，SFT1k/epoch1/125step/B8/6.5GPUh与RL2k/epoch1/500step/B4/20GPUh、Adam5e-7；训练16frame/128×28²、推理16/32/64frame与256×28²不是同视觉费。RD同prompt正γ被std消去后显式乘adv是具体选择。VideoMMMU32/64frame不胜VideoR1，VideoHallucer factual20.0<base25.5、VideoR123.5，均不能写全bench/全类别减少幻觉。precision/rollout G/seedCI ND；format100%仅本test，Tree vsSingleCue也改rationale长度/构造费用。

20834作者IV/VI/VII-A补齐：Prismatic+Qwen.5B、DINOv2/SigLIP dualvision与2.5M任务mix；预训2epoch/8GPU/B128/AdamW2e-5/3%warmup，postLoRA8GPU/B64/lr1e-4/10%warmup/150ksteps，型号/precision/seedCI ND；LIBERO各suite单独训、Plus混合训不同。ablation每suite7×80=560、四suite2240，正文括号把4×7×80称560不可抄。SEG共享跨view与VGGT训练teacher非真实3Doracle，图示attention不是执行因果证明。real实验xArm7/双D435/97物件57seen40unseen/60task×50=3000demo、SAM2人工目标mask；8A100/50kiter/B32并非无需额外监督、jointabsolutecontrol不授真实环境普遍safe。这里只采用已读仿真切片和目标/geometry/actionconsumer分工，不采未读完整real性能数。auxlabels/teacher/segmentation/actionhead与data/training全部计费。

### 2604.19954v1 Viewpoint Tokens（具体旧EX重开）

2+1+2=5，作者原必要§3.2–3.3/4.3/4.7–4.8与本次§3.1/4.1–4.4/A，root必要门实核复用。object-canonical正x朝前、zeroRoll/fixedFoV约55°，五参数token经3layer1024MLP与backbonejointtrain，factorizedposition/orientation不授相机内参/完整真实geometry控制。11未见类别与encoding/data/frozenbackbone对照形成有限transfer，旧要求普遍几何/物理迁移过强而重开，不因‘maturecamera conditioning’抹除。Harmon7.5kiter/B192/AdamW MLP2e-4/backbone2e-5、A10080G约28h/1%warmup，precision/训练seedCI ND；5550test/2220hardview、regressor自身4.16°误差与CLIP/GenEval singleobject/color只是代理。backview/landmark水平中心先验、人脸细结构退，train elevation0–45°不推广rareangle；full/synthetic/photo data费及regressor不省略。

v1Updated=2026-09-25为后处理异常，不作为首次公开；DOI created/registered Apr23、官方CV当月19954位置/currentv1与Apr23ID簇可互证。root已actual准按Apr23 arXiv事件归属，非单字段证明全网firstpublic。当前官方页未见撤回/勘误，Books owner普通。

### 2604.19837v1 Forage V2（具体旧EX重开）

2+1+2=5，作者已读§3.1–3.3/4.1–4.5，补§4.2/5.1/5.5/6.1并复用root必要独核。强模型document知识转弱模型时Evaluator也继承completeness denominator经验；同task/runtime却每run自定义分母，稳定266不是独立oracle，不能拿coverage％与cold直接等义比较。advisoryknowledge可被忽略，static task而非动态环境，newharness/knowledge/evaluator均共变。具体安全反侧为Planner发现隐藏.eval.py→postmortem把评价偷看写成知识→跨run传播；dotfile hiding不是隔离，directory namespace移除能减该路径而不自动保证全工具sandbox。breached实验作者称另archive/exclude，本轮未独立复现。

仅NVIDIA目录收集的通用Agent/eval机制采用，生物/数学领域结论不采。Opus4.6/Sonnet4.6六run/condition、structuredmaxturn15/medium/timeout1200/maxround8；API成本全run含plugin加载但强模型预积知识构建费不能由seeded本次call费消除。资源超时/无结果与能力界限不可由隔离Evaluator区分；固定turn数×未知每turntoken/fee非严格总费用上界。precision/hardware对API不适用，版本suffix日期ND、样本6不授普遍稳定；rootSource准入与Apr23批次日期已actual，Books owner普通。

### Context Unrolling 2604.21921：日期终态保留（非确定Apr23候选）

已读[完整题摘及v1§1–2](https://arxiv.org/html/2604.21921v1)、[官方项目核心说明](https://omni-model.com/)，原件SUP_CORE_21921v1_20261015.raw.html/SUP_PROJECT_21921_20261015.raw.html。异质中间context再供下游消费有潜力，但日期资格未成立，不评分、不作本日正面证据或Books。项目仅标April2026；旧Seed Apr23目录metadata未证明当日正文已可得，arxiv Submitted Apr23UTC已Apr24BJT也不是公开日。当前定点官方入口/搜索未取得早正文日，API400/web不可达不升级零命中。root认可日级隔离：恢复须同身份官方正文/项目release的Apr23公开日依据；只重开该族，不扩本窗或全月日期账本。

### 已读但不计新增候选的原EX

20117、20140、20158的本轮必要段与具体未新增差额见A3；Source/AB/raw保留，不删除原反侧、不凭已读全文强收。19954/19837已由root最小必要独核具体重开，处理见各自A5，不再继承旧过强准入门。旧85候选与其全部有效Source/Books层仍原位保护，本轮不是重审原85或把旧小时跨日归属重新搬移。

## A6. 具体Owner差额与逐字PRE（未获lease不写）

### 第一批具体NC提案（作者actual正文，待root处置独核）

| 身份 | Stable owner / 已实际正文位置 | 具体承载与本轮为何不改书 |
| --- | --- | --- |
| 20452 | AGENT-RAG / Ch76 “Speculative Retrieval Draft必须经过Accept/Fallback”三段（约233–245）与后邻TenantFilter | 同家族原v1已在正文：cache/fuzzy draft→surrogate accept/fullretrieval fallback、query/source revision、homology falsepositive与accuracy代价。有限必要Source命题不变，复用该Books层，不把未经证明的逻辑等价添回。 |
| 20316 | WORLDVIEW-REPRESENTATION / Ch5 “信息存在、可读与被使用是三个不同命题”（319起）及前邻解释证据阶梯 | 独立reader可解码不等actor实际使用，联合reader/reconstructor可privatecode；CER的另一student条件帮助与SMV正确匹配不越过该证据层。不是因局部结果而排候选，只不把已有分权重复为新owner段。 |
| 20398 | PLATFORM-EVALUATION-SYSTEM / Ch66 “评估对象有四层/Agent andOutcome”及真实repo/受控任务两段（1137–1169）；Ch33 Measurement前置correctnessgate | renderer/build/console只验运行代理、不是交互任务成功，scaffold staticcheck和WebVoyager FSR不同consumer已由该层级/结构行为独立验收实际承载。训练gate的本轮有限实例仅报告证据，不让外观reward授功能成功。 |
| 20755 | TRAIN-GRPO / Ch33 “VerifiableReward的优势边界”(759–778)与“语义Segment”(924–942)，Ch31 ProcessReward有限证据强度 | cell/value anchor仍由learned scalar critic评分，不是formalstepchecker；现有正文已区分final matcher、局部数值slot、整trajectory advantage和真正segment credit。该具体小模型表格反侧保日报，不改一般规则为已实现celltruth。 |
| 20659 | TRAIN-GRPO / Ch33 “语义Segment”全局部与“DerivedSkill Utility”(1180–1190) | 分段边界owner、proxy/value/continuation结果不同权限、tokenprobabilitydelta只是relevance非因果已在正文。Δgoldbelief仍不能成为真过程verifier；entropy分段/中心化配方与budget反侧只保报告，不把类似局部proxy再堆一节。 |
| 20354 | MULTIMODAL-GENERATIVE-PARADIGMS / Ch24 “复杂视觉生成需要Plan/Predicate/RetryBudget”与NUMINA早期layout→regeneration两段（1985–1997） | 内部attention/detector只是中间predicate提案、再生成有额外费用与误检/时序失败。PFI/LP AND早停restart是该有限选择分支，MonteCarlo成本非wallclock、5次retry不证completion；保新实验反侧而不改变现有control分工。 |

上述六项root已逐项实际现有正文与必要邻接，NC处置通过；未变化Source层继续有效，不声称论文全部配方已有。若有新具体反例只重开该项owner，不回退整个发现池。

### 20500 → MODEL-SAMPLING，Ch20

作者实际顺读Ch20 ParallelSampling的coverage/selection、共享prefix高entropy重新分叉两段及随后program局部变体，旧SF2604-00018 marker后/“当候选是可执行程序时”前。已有的是随机/熵选重分叉，没有按截断树prefixmass枚举distinctleaf及概率coverage与语义coverage区别。拟补两段，root PRE/lease待审：

> 若截断采样经常重复相同轨迹，还可显式维护已探索的 token tree：从尚未展开的高概率 prefix 分支，再用 greedy continuation 完成新的 leaf，并复用共享 prefix 的 KV。这里主动改变的是候选枚举顺序；覆盖的质量是截断分布中的概率质量，不是正确答案、语义多样性或独立样本数量。完整遍历有限树才与原截断分布拥有相同 support，固定 leaf 预算下的 greedy suffix 也不保证找到概率最高的完整序列。
>
> [有限 distinct-leaf 对照](https://arxiv.org/html/2604.20500v1)支持这条预算分支，但连续十个 token 与兄弟后缀相同就停止，是会误剪不同答案的近似 merge；较高 coverage 不能替代最终 verifier。树管理、保留 KV、候选完成与选择均计费，低 batch 的 prefix-cache 收益也不能直接搬到可并行生成的大 batch。截断支持不合适、分叉过多或语义误剪不可接受时，保留普通 self-consistency、较保守的分支枚举和独立答案核验。<!-- source-family:SF-2026-ARXIV-2604-20500 -->

### 20733 → TRAIN-RLHF，Ch31

作者actual Ch31“Teacher与未来RewardModel”完整首段/marker与后续RM双层闭环两段，前邻handoff/探索保持。拟在SF2605-03677之后、迭代RLHF未来RM之前插入：已有studentvisited teacher与futureRM，但没有future-policy scout/cache→rollback这一训练数据供给分支。逐字PRE：

> Teacher 也可以来自同一训练轨迹稍后的 checkpoint，而不是另一个更强模型：先向前训练一段，离线生成并验证正确轨迹，再回退到较早的 policy，在当前低通过率的 rollout group 中替换一个样本。它把外部 teacher 的供给问题换成 checkpoint、成功样本缓存和重放窗口的管理；当前组仍先完整生成，前进训练、验证与回滚重训并不免费。自动触发还可读取 reward 停滞、entropy 下降与历史失败 prompt，但这些只提出重放建议，不证明训练一定陷入错误盆地。
>
> [有限 near-future 对照](https://arxiv.org/html/2604.20733v1)支持这一轨迹来源选择，却不保证相近 checkpoint 的概率比总接近一。按成功、长度或 entropy 筛选后再缓存一条，已经改变实际供给分布，不能只用未筛选 future policy 的 token probability 就自称 exact importance correction；同配置去掉修正几乎不变也不是普遍安全证明。应分别核验来源支持、指导样本偏差、重放后的 held-out 质量和完整训练费用；没有新成功轨迹、支持漂移大或重放不合算时，保留新鲜 on-policy rollout、普通监督复用与独立训练验收。<!-- source-family:SF-2026-ARXIV-2604-20733 -->

### 20446 → WORLDVIEW-WHY-MODELS-LEARN，Ch4（fresh owner actual提案）

fresh已实际Ch4 EoS两段及梯度/mini-batch/curvature前后、Ch28 schedule/ELR/optimizer、Ch3尾/Ch5首。现有Ch4仅静态阈值→局部分岔与sensor≠LR权限，没有两种路径积分曲率测量分责。拟在Ch4 EoS首段后、Optimizer段前，逐字PRE（root待审，不授写）：

> 这条边界还需要分清“梯度怎样改变”和“loss 怎样改变”。对固定步长、full-batch GD 的一步 d=w_next−w，沿该线段均匀平均的 Hessian 控制下一步梯度，而按三角权重平均的 Hessian 控制这一步 loss 变化；只看端点的最大特征值，不能把两者当成同一个观测量。若整条轨迹的 loss 上下有界，且累计平方步长持续发散，望远镜求和才迫使按平方步长加权的方向曲率均值趋向 2/η；有限能量的正常收敛轨迹不受这条结论约束，也不由它推出全局吸引或每步最大曲率锁定。
>
> [必要一步恒等式与条件边界](https://arxiv.org/html/2604.20446v1)将 EoS 变成可核的轨迹诊断，却没有把 SGD、momentum 或大模型训练自动纳入定理。计算路径曲率仍需 Hessian-vector 或等价探测成本；局部振荡、持续 forcing 与 loss 控制条件失效时，应回到实际 loss、gradient 和 step norm 的联合监控，而不是按 2/η 自动提高 learning rate。

### 本批写后待核

root actual上述三处逐字PRE/完整邻接后授两段与本人注窄lease。作者已逐字写20500 Ch20 L365–369、20733 Ch31 L1083–1087、20446 Ch4 L133–137并顺读完整前后及本人注；root非writer实际新两段/完整前后/本人注POST通过，限定diffcheck0，三lease释放。累计5真实I，此前19907/19945两项POST仍有效；不授DAY。

### fresh互斥Owner实际比较：五NC（待root处置独核）

| 身份 | 实际正文与必要邻接 | 具体关闭理由 |
| --- | --- | --- |
| 20486 | Ch78 L490–515 Tool出现不等于贡献、508模型版本相对no-tool能力、707–723 necessity与admission两Gate；Ch31 outcome/trace邻接 | 固定八次direct样本任一正确是有噪声能力估计实例；已有no-tool对照、调用率非贡献、真实outcome独立验收与全费。奖励比例/local→live实例留日报，不为recipe另造长期diff；v1不存在vLLM冲突已纠正。 |
| 20811 | Ch78 L87–140 stream/repair/compiler diagnostics/真实runtime分权与Ch79形式executor邻接 | parse、精确AST与单初态终态是现有syntax/type/behavior不同consumer的具体基准，不改执行状态或权威分工。AST不同可等功能、单s0不证全状态/trace等价留日报，不添metric词典。 |
| 20714 | Ch80 L128–151跨episode evidence/可变prompt、303–331 harness修订/rollback；Ch82 L155–166 runlocal与promotion、205–207 graph/prompt优化对象 | TPG/失败聚类/局部rollback/历史proposal排序是已有有界harness adaptation的搜索表示，不新增commit/rollback语义。有限MCP正证保留，非因GAIA混杂或无定理排材料。 |
| 20564 | Ch20 L304–334 steering/local续写、349–379 coverage/selector/单token局部搜索；Ch34 L150–172同prefix替expert action再policy suffix与outcome资格；Ch19/21/79必要邻接 | 连词触发、lookahead、single-position DPO是已有局部分叉/偏好接口实例，没有新独立逻辑真值或提交链。非连词对照有限、共享参数、强制gold候选限制保日报。 |
| 20614 | Ch4 L64–94 loss与业务目标、109–145曲率sensor；Ch66 L200–217 calibration独立Gate、1210–1219 H/C/F/GGN与当前regime排名；必要邻接 | flatness降但ECE不降是既有geometry诊断≠可靠性验收的新有限反侧。CalMO组合训练recipe留日报，不因无普遍定理否实验；不采MSE非proper/点梯度升邻域证书。 |

### 20572 → AGENT-MEMORY（fresh actual最小PRE，未授lease）

fresh实际Ch77 L308–333 Fact/Retrieval-policy state、157–177 contentcredit、1489–1501 MCtree/marginalrewrite；Ch31行为identity/Ch76首/Ch78邻接。旧batch memory utility与tree MC未覆盖同可重放prefix一次Retrieve的配对continuation信用。拟在“不是单条memory的因果贡献…不只测最终任务分数。”后、U-Mem前：

> 训练“何时主动检索”时，整段任务 reward 还会混入检索前已发生的进展。若环境能精确恢复到同一 prefix，可固定 memory bank 与 retriever，从该状态分别继续“执行这次 Retrieve”和“跳过这次 Retrieve”，把完成质量与长度的配对差作为局部检索信号，再与原 trajectory reward 合并。这里比较的是一次读取决策及其后续行为，不是单条 memory 的事实真值；分支后继续采样仍会产生噪声，配对也不自动给出严格因果、无偏梯度或方差下降保证。
>
> [受限主动记忆实验](https://arxiv.org/html/2604.20572v1)支持这种训练接口，但状态恢复、冻结 bank、确定性检索与额外 continuation 都是条件和成本，在线持续改库的测试流也不能混作独立冻结 holdout。Replay 不可靠、bank 已变或配对费用不值时，保留普通 outcome reward、固定读取与受控组件消融；较短注入 Context 不抵扣经验提取、双分支训练和记忆更新的全费用。

### 20728 → MULTIMODAL-EMBODIED-VLA（fresh actual有限V1 PRE，V2中心D仍隔离）

fresh实际Ch26 L1428–1468 RuntimeAssurance、1770–1786可达域/几何及Ch25/27必要邻接。旧physicalenvelope/staleness未覆盖有限已知T+观测kernel区间→belief外包络→worstbelief单步准入。拟在RuntimeAssurance首段后、“安全层即使没有触发告警”前：

> 感知不能精确标定时，安全过滤器也不能只消费一个最可能 state。在已知有限状态转移的模型中，可将观测概率限制为区间，逐步维护包含可能 posterior 的 belief 外包络，再对每个候选动作求最坏 belief 下落在安全动作集合的质量；达到门槛才允许交给后续执行层。双线性 posterior 更新可经外松弛与归一化变换落到 LP，但模板、正分母和包含性必须成立；外包络扩大通常换来更保守的准入，而不是额外的物理事实。
>
> [受限 POMDP shield](https://arxiv.org/html/2604.20728v1)给出这条机制的有限实例，不提供完整轨迹安全证书：按完整 observation history 的当前安全质量下界，不能直接乘成“此前从未离开安全集”的概率下界。区间校准、belief 更新、离线动作集合和每步 LP 都需计费；感知漂移、模型失配、LP不可行或停滞时，应拒绝这份准入并交 verified fallback/停止，不能用采样得到的 belief 子集继续声称原 worst-case 保证。此处只采用条件化一步过滤，不把本文仿真签发为真实 VLA 的物理安全。

### 20470 → MODEL-SELF-ATTENTION（fresh actual最小PRE，未授lease）

fresh实际Ch14 L124–136 indexer/support、326–407 support/视觉预算与完整邻接、Ch13/15首；Ch24 L1682–1710 motioncache/Ch49 L942–1005同logicalmask retile。旧在线support未覆盖prompt先预测运动代理→离线mask配置。拟在视觉Token预算sourcebinding后、“改变匹配表示”前：

> 生成视频前还没有真实运动可供测量，固定稀疏比例因此仍是便宜的起点；若不同 prompt 对长距离关系的需求差异明显，可以先以参考视频的运动强度代理离线标定多组稀疏配置，再由 prompt embedding 预测代理类别、选择配置。在线选择器继续在几何候选窗口内用少量 Q/K 探测提议动态 mask；这把“需要多少候选”和“本步保留哪些候选”分成两个控制层，预测的运动类别不是生成结果的物理事实。
>
> [有限视频 Attention 对照](https://arxiv.org/html/2604.20470v1)支持这条条件化预算路径，但固定稀疏和动态 mask 单独使用仍有质量反退，动态探测还可能慢于原路径；预测器与可选 LoRA 的结果不能混成同一个免训练收益。参考生成、光流标签、离线配置搜索、router/adapter 训练及在线探测都需计费，soft mask 加 epsilon 也不自动形成严格删除支集。类别漂移、漏掉重要关系或净收益不成立时，应扩大预算、回到已验证固定 mask 或 dense Attention，并由 runtime 独立验实际 mask 执行与端到端费用，不从局部 feature/光流 proxy 宣称物理一致或生产 SLO。

## A7. 独立Owner继续闭合与具体写位

57项必要Source技术层已由root/fresh互斥分批实际完成；仅支持A5具名有限命题与中心隔离，不授全主张、实现、复现或DAY。日期57及19954后处理异常的组合日级资格亦经root actual。六个整族暂缓为20366/20368/20505/20665/20715/20817：各中心D已实际反例/原文核验，暂不采用正面Books命题，保留其局部实验但不为争议强桥作正面证据；重开需相同中心桥修正原证/证明或独立有效替代，不将实际反例当访问受阻。20728另保V2强桥D，仅经独立PRE采用V1有限一步过滤，不将局部I升级全轨迹保证。

root互斥8项实际当前正文/必要邻接比较（不重审Source）：

| 身份 | 处置与具体owner | 实际承载/差额 |
| --- | --- | --- |
| 20677 | NC / PLATFORM-EVALUATION-SYSTEM Ch66 L1427–1437 | 同decisionrule/有效人口/Unknown不当零错误、自一致≠外部gold已承载。双BBQ稀疏未知与有限人群反侧保日报，不称全部sDIS/SF公式已有。 |
| 20682 | NC / WORLDVIEW-REPRESENTATION Ch5 L350–360；Ch14 L79、Ch28 L192–200交接 | replacement fidelity≠原网络干预、方差方向≠任务功能、谱截断需value/跨层/最终验收、exit校准≠SLO已承载；ridge/earlyexit具体recipe留日报。 |
| 20789 | NC / MODEL-SELF-ATTENTION Ch14 L20–23与Ch22交接 | 局部窗口可跨层传播远距、位置/有效利用分责。有限localmask/偏置是其归纳偏置实例，100M反退/token非认知chunk留日报，不签认知机制。 |
| 20796 | NC / MULTIMODAL-REPRESENTATION Ch23 L294–319、494–500；Ch24 L680–687 | 共享semantic code/独立pixeldecoder、重算与objective/commit分责已承载。SPRINT配方/ratio冲突/反侧仅报告，不冒称全部recipe已有。 |
| 20801 | NC / AGENT-WORKFLOW Ch81 L1094–1106；Ch80 L319邻接 | typedskillgraph/执行权限、graph/prompt优化、validation独立test和失败恢复已承载。DSL search/最多两次repair为有限实现，不新增授权/活性保证。 |
| 20705 | Only / TRAIN-PRETRAINING Ch28 | 五成熟SSL任务合成标签GRPO的有限工作点/任务冲突与难度反侧保日报；1000/2000steps预算未控，不从有限人口造通用任务数/难度规则，也不因无普遍定理否候选。 |
| 20685 | I单段待POST / TRAIN-DPO Ch34 L309 | root实际必要Source/当前多目标偏好局部给逐字PRE并授单段+本人注；作者已保存并顺读完整邻接。求系数loss-normalized空间≠应用rawgradient空间，保单属性反退与全费。 |
| 19954 | I单段待POST / MULTIMODAL-GENERATIVE-PARADIGMS Ch24 L429 | root actual相机控制局部后给逐字PRE并授单段+本人注；作者已保存并顺读完整邻接。固定FoV/roll/objectcanonical的五参数token与unseen类别局部transfer，不授通用geometry/worldstate。 |

fresh五NC处置已由root接纳有效实际比较，不第三次重读同章。20572/20728/20470三处逐字PRE经root实际完整插点后授各两段与本人注窄lease，作者已保存并顺读完整前后/末注；root实际POST通过并释放三lease。20685/19954两单段及本人注也经root实际POST通过，五项本人注仅行政同步并actual读回。累计10真实I；其后写位仍须各自POST，不授DAY。

### 20348 → MULTIMODAL-EMBODIED-VLA 最小PRE

作者actual Ch26 Perception分流/Action耦合完整两分支与协同通信三段（381–389、1330–1342），Ch25/27交接。已有jointdecoder交换summary，没有先生成一臂完整trajectory再条件化另一臂的ICL分解。拟插“从单体控制到协同通信与可回滚proposal”标题后、现多机器人消息首段前：

> 两个执行器共享目标时，联合生成完整动作最直接，却可能让模型同时处理过多配合关系；完全独立生成又会遗漏对方的后续路径。一条受限分支先生成 leader 的完整 trajectory，再把它作为 follower 生成的条件，把联合问题改成有顺序的条件分解。这里的 leader 是提案顺序，不是更高的执行权限；两份轨迹仍须按同一时间轴、坐标和任务约束联合检查，换先后顺序也可能改变可达的候选。
>
> [有限双臂 ICL 对照](https://arxiv.org/html/2604.20348v1)支持这种 factorization 与示例供给选择，部分任务仍比 joint 生成略差，新的 debate 也会变慢并退步。Leader 错误会传播给 follower，多样候选、judge 与完整 trajectory token 都计费；较低并行中位时间不等 token 更少，模型自评也不是物理 validator。耦合太强、候选失配或质量/预算回归时，保留 joint proposal、固定示范与独立低层 controller，不以模拟成功率批准真实双臂安全。

### 20392 → MULTIMODAL-REPRESENTATION 最小PRE

作者actual Ch23共享codec/teacher分责完整局部与activeobservation八种读取分支（494–511、879–905），Ch22/24交接。现有crop proposal不含全图SSL teacher→逐步state student的训练目标。拟在“固定表示之后，可以按未决Claim主动补充Observation”标题前：

> 局部读取也可以先在表示训练中学习，而不只在问答时按 claim 选择 crop：训练期让 teacher 读取完整图像，student 每步只取得一个固定大小的 glimpse，并把更新后的 recurrent state 对齐 teacher 的全局语义 target。Teacher target 只在末端计算，student 却在每一步接受监督；对前一步 state 停止梯度，是控制跨步优化的选择，不说明较早观察已被充分保存。后续还可冻结表示路径，只训练“下一步看哪里”的 policy。
>
> [有限自监督对照](https://arxiv.org/html/2604.20392v1)中 learned glimpse 优于随机位置，却未超过同 backbone 的静态全图读取；更多步的收益也会递减。Integral-image 先遍历输入、随后每个目标位置常数时间的提取，只是摊销局部成本，不能变成端到端费用与输入大小无关。Teacher、三阶段训练、额外 state/policy 与全部读取都需计费；小物体、上下文丢失或预算回归时，保留静态全图、固定 crop 与独立下游验收，不由表示接近批准证据完整。

### 20472 → PLATFORM-EVALUATION-SYSTEM 最小PRE

作者actual Ch66 Calibration隐藏regime、条件与联合人口、Conformal适用边界及Model/System/Runtime四层（900–908、1036起、1137起），Ch65/67交接。现置信sensor未有用terminal binary success训练prefix TD概率目标的接口。拟在Calibration隐藏regime首段后、“人为扰动模型logit”前：

> 轨迹置信还要先声明预测对象：若任务只有终端二值 success，可把每个 prefix 的输出训练为后续成功概率，用下一步预测作 temporal-difference target，而不是把当前 action 的 token probability 当任务成功率。BCE 拟合终局标签与 TD 传播后续估计是两种训练接口，后者会继承 bootstrap 和行为分布偏差；一般累计 return 的回归值并不自动等于 success probability。
>
> [有限轨迹校准对照](https://arxiv.org/html/2604.20472v1)支持这个 binary-task 分支，但成功轨迹上的 conformal 门主要约束误拒成功，并不保证失败或危险轨迹都会检出；少失败人口和跨任务 shift 仍可退步。样本单位、prefix/rollout batch、训练 epochs、校准人口与当前 policy 必须分别绑定，并计入标签、训练、搜索 simulator 和 rollout 全费。公式与搜索伪码的阈值方向尚不统一时，不照录完整执行 recipe；改 policy、校准漂移或模型失配时，应回退普通 outcome 验证、冻结阈值或 Unknown，不由较小 ECE 授予物理行动安全。

### 20503 → INFER-SCHEDULING 最小PRE

作者actual Ch56 VerificationGranularity、DecodeBatch CriticalPath、SLO Co-serving，以及Ch48 variablelength、正确前缀/残差恢复与SpecStream完整局部。现有batch重组未区分每request draft长度局部目标与共享batch真实latency。拟在DecodeBatch首段后、prefix-aware regrouping前：

> Speculative Decode 还可以逐请求改变 draft 长度，但这些长度共同组成一次 target verification batch：某请求的局部接受率或吞吐最优点，并不独立决定这轮所有请求的 latency。可先离线 profile 阶段费用，再用在线不确定性模型提议长度，以执行中的 batch 时间修正选择；draft 与 verification 分 stream 或分配不同 SM 资源，只改变执行排布，不消除共享 HBM、cache 和队列竞争。
>
> [有限分阶段调度实例](https://arxiv.org/html/2604.20503v1)支持这种 request-control 与 batch-cost 的分责，局部 GP-LCB 目标不是全局 SLO 证明。提前剪掉 draft suffix 后 pad 回 shape，也不自动保留 target sampling law；误剪时的完整 target logits、拒绝残差和 frontier 恢复必须由验证器另行闭合，不能由 layout 相容代签 lossless。两小时 profiling、context pool、探测与全部共享资源都计费；负载漂移、恢复语义不明或净费用回归时，回到固定/保守 draft 长度、完整 verification 与原 continuous batching。

### 作者actual第二批不改正文提案（待独核）

| 身份 | 处置提案 / actual具体承载 | 理由与仍保报告的新证据 |
| --- | --- | --- |
| 20460 | NC / PLATFORM-EVALUATION-SYSTEM Ch66 L276–286 joint与conditional人口、空间选项+定位联合成功、视频实例/时间归属，以及配对干预局部 | 同scene四QA要联合答对而非边际均值，是现有joint成功/绑定关系与固定分母的具体实例；C-TCD用pairedcounterpart不等自然部署可得、AUC有限artifactprobe和BaAcc/Quad反侧留日报，不称真实因果已证。 |
| 20473 | NC / TRAIN-GRPO Ch33 L109–133完整groupstd/跨difficulty尺度、FGRPO独立归一和阈值λ；896–911阶段credit；1892 curriculum适用人口 | 原无稳定项公式下组内同一positive γ在std中抵消，归一后再乘才改组权重；若对照Books sigma+delta，固定delta下不严格缩放不变，不能把近似写恒等。此为现有reward/advantage尺度分责的具体工作点；cue-tree/reasoningreward与γ搜索费用保报告，不重复recipe，也不因局部实验而取消候选。 |
| 20487 | NC / AGENT-RAG Ch76 L35–45外部知识context/KV/参数三分支、独立chunk拼KV不等jointencoding及provenance/claim支持链 | graph外索引负责定位provenance，tripleKV与rawsentence prompt是已有两消费通道的组合实例；未新增cache identity/sync或事实验收权限，不能把非纯控表当KV独有归因。双channel/graph的有限结果保报告，不称算法全部已写。 |
| 20570 | Only / TRAIN-DATA Ch27 L198–208 format-vs-content干预及Ch23读取/任务消费交接 | synthetic spatial-edit训练迁移理解的局部新工作点有效保留，但其图像编辑proxy/测量接口未改变本稿数据内容与目标consumer分责；个别understanding任务反退，不由平均增益造跨任务单向演进规则。报告保具体transfer证据与额外标注/训练费，不因无普遍保证排除。 |
| 20834 | Only / MULTIMODAL-EMBODIED-VLA Ch26 L152–176 privileged3Dteacher训练期/部署读出、872–891语义anchor+语言动作对齐 | 同SEG跨view约束、训练期geometry蒸馏与actionhead接口为新的有限组合工作点，但本次可采用的是已建立的teacher target≠runtime几何/动作权限与真实consumer验收；不把SEG特征相近升级真实3D或每suite560分母。具体geometry-loss/SEG配方保报告，不冒称全部recipe已有。 |

### 20544 → TRAIN-DATA 最小单段PRE

上表三NC/两Only已由root actual具体正文/完整局部与本轮有限采用命题核过，通过。20473固定delta修正已收准；不声称各论文完整recipe都在旧正文。

作者actual Ch27 QualityFiltering完整类型/retention/集合选择及phrase sensitivity局部、Ch66 expectedfactinventory与Ch26/28交接。旧filter没有先将推断claim与视觉描述分开审计后回聚合的具体通道；拟在retention/分布变化原段后、Host-aware crawling前：

> 多模态训练样本还可以先拆开“画面里描述了什么”和“作者额外推断了什么”，让图像一致性、推断逻辑和知识支持分别产生筛选信号，再决定保留原样本。分解本身也是有损变换：净化 summary 可能删去 claim，未出现某类 claim 时给默认高分也会改变选样偏好；auditor 的内部知识不是外部事实核验。[有限分解审计对照](https://arxiv.org/html/2604.20544v1)支持这种筛选接口，却有任务反退，同源生成/分解/打分还会共享偏差。应保存原句到 claim 的覆盖、各 sensor 身份和最终人口，并同时核未提及与被删内容；候选生成、分解、全部审计和后续训练均计费，少用样本不等总费用更低。分解不完整、知识支持不可查或能力回归时，保留原始内容、普通质量过滤与人工/外部证据核验，不让平均 audit score 取得训练真值。<!-- source-family:SF-2026-ARXIV-2604-20544 -->

### 20549 → TRAIN-DATA 最小单段PRE

作者actual Ch27 FilterThreshold完整两段、language/domain retention与quality/diversity局部、Ch26/28交接。旧regime合同未有跨语言移植筛选器与重采样次数的混杂；拟在SF2605-19407 marker后、“内容无害不等于更新无害”前：

> 语言之间复用质量过滤器，还要分清“共享评分函数”和“共享质量真值”。可先在多语言公共表示上用若干语言的质量对照训练 scorer，再在新语言中比较不同保留比例；迁移有效只说明该表示与所测来源有可复用信号，不能排除百科或指令格式等共同 artifact。[有限跨语言过滤对照](https://arxiv.org/html/2604.20549v1)在部分小保留集上有收益，但收紧比例后反复使用同一语料，也同时改变 unique tokens 与重复次数，不能单归因为更纯数据；小差额还可能接近采样变化。Anchor、负样本得分区间、语言来源、retention 与 passes 必须共同保存，表示、打分和完整训练继续付费。新语言支持、长尾覆盖或独立能力回归时，保留本语言过滤、随机/分层混合与较宽保留集，不从通用 embedding 推出语言无关的质量标尺。<!-- source-family:SF-2026-ARXIV-2604-20549 -->

### 20720 → TRAIN-DATA 最小单段PRE

作者actual Ch27数据分布即权重、QualityFiltering集合互补、onlinepolicy selection与coveragecontract局部，Ch26/28交接。旧语言相似/质量选择没有按target dev-input语义覆盖选择auxiliarypool的接口，不把该覆盖当当前student真实知识缺口；拟在SF2602-03103 instruction-specificity段后、集合质量/多样性段前：

> 为目标输入补充训练覆盖时，语言相似度也未必是合适的采样距离。一条受限分支先对目标开发输入作语义聚类，比较辅助数据池的覆盖缺口，再按容量与覆盖预算选择辅助样本，而不只依语言表面距离；边界分数只提出哪里值得补样，不成为真实知识缺失或答案正确的 oracle。[有限语义缺口对照](https://arxiv.org/html/2604.20720v1)支持这一选择轴，却不由 pool quota 认证尾部覆盖；分布 JS 接近也可能漏掉对任务关键的局部变化。Encoder、表示/聚类、开发集、辅助池、adapter 与训练人口须共同版本化，并计入编码、检索、训练和独立能力回归全费。缺口估计、类别支持或净收益不成立时，保留随机/分层供给、语言覆盖与可信原语料，而不是继续追逐单一距离或分布分数。<!-- source-family:SF-2026-ARXIV-2604-20720 -->

### 20601 → AGENT-PLANNING 最小单段PRE

作者actual Ch79条件化planning分支/rolloutbudget/acquisition-shaping-integration，Ch26层级subgoal与controller完整局部、Ch78/80交接。没有完整planpool固定后随executor能力重排并推进skillcurriculum的训练闭环。拟在SF2607-24720 marker后、“环境排序不应改写用户目标”前：

> Planner 与 executor 还可以在训练中交替适应，而不只在部署时互相重试：先生成一份候选 plan pool，按当前 executor 的实际成功反馈筛选或重排，再让 executor 练习已掌握技能与至多一个新增技能的组合，随后更新 plan 偏好。这里改变的是供给给 executor 的训练计划分布；后续 DPO 不等于每轮都自由生成新计划，LLM 给出的 prerequisite 也不是真实依赖 oracle。[有限共适应对照](https://arxiv.org/html/2604.20601v1)支持计划选择相对固定供给的局部作用，却仍有新对象反退；同环境步数不包含 ontology、初始 plan、筛选、planner DPO 和全部 executor 训练费用。应共同绑定技能定义、掌握阈值、pool 与两端 checkpoint；依赖图有环、技能误判或迁移回归时，保留固定可信计划、简单 curriculum 与独立执行验收，不让计划偏好批准环境完成。<!-- source-family:SF-2026-ARXIV-2604-20601 -->

### 20627 → TRAIN-RLHF 最小单段PRE

作者actual Ch31 demonstration-derived reward完整局部与potential/trueoutcome边界、Ch25 occupancy/worldstate交接及Ch30/32首。现有专家video progress potential没有离线futureoccupancy→goal-velocity surrogate的模型派生reward。拟在SF2603-07784完整段后、“更保守的演进”前：

> 没有专家进度标签时，还可从离线状态转移学习未来 occupancy，再用它与目标点的差异提出 goal-conditioned reward；用 flow 的 velocity 差作可计算代理，把占据分布建模、reward 拟合和 policy 学习分成三个资产。它不是普通的折扣 potential 差分，velocity MSE 对分布距离的上界也不等真实 reachability 或 policy invariance。[有限离线控制对照](https://arxiv.org/html/2604.20627v1)的最优性解释另需确定性、路径层级单调和 dataset-policy successor 顺序等条件，不能直接借给任意有噪声日志；部分任务仍弱于原对照，奖励尺度也随任务改变。应核 occupancy 支持与独立 outcome，并计入分布模型、reward 和 policy 的全部训练，不能只比较最后一阶段。模型失配、代理奖励被利用或质量回归时，保留已知任务 reward、可信示教或更保守离线策略，不把拟合的未来状态当环境事实。<!-- source-family:SF-2026-ARXIV-2604-20627 -->

### 20763 → PLATFORM-EVALUATION-SYSTEM 最小单段PRE

作者actual Ch66 distribution合同/平均与切片/rare-failure与重加权局部，Ch65/67交接。现有分布原则未区分给定regimecomposition的consumer重权与iid无偏，拟在“数据量增大只会降低部分samplinguncertainty”后、污染检查前：

> 评价人口还应声明谁来决定各切片的权重：原 benchmark 的条目比例、每个语义 regime 等权，以及部署 consumer 的目标比例，估计的是不同目标。可先固定语料与 query 到 regime 的映射，同时报告各层分数和目标加权结果；若某层缺少支持，应报告缺口，而不是用 bootstrap 补造该层。[有限检索重加权对照](https://arxiv.org/html/2604.20763v1)显示同一题集只改 overall/macro 权重就可能改变模型选择；这不证明 iid sample mean 固有有偏，条件化组分偏差与总体抽样无偏须分开。图谱/聚类、生成 query、自动 qrel 和重复估计都付费，也不因每层有五题就形成可靠证书；映射重叠、标签不稳或部署比例未知时，保留原分项/总体结果与人工分层审计，不让一个新均值取代 consumer 的真实目标。<!-- source-family:SF-2026-ARXIV-2604-20763 -->

### 20779 → PLATFORM-EVALUATION-SYSTEM 最小单段PRE

作者actual Ch66 AgentOutcome、repo结构/行为独立验收、Trajectory/Checkpoint完整局部；Ch65/67交接。现有pass评价没有session→tooloutput→commit存活可连接人口的观测缺失机制，拟在AgentAndOutcome标题后、incident首段前：

> 真实开发 trace 还要把“模型写出代码”“代码进入 commit”与“后来仍被保留”接成可核的证据链。Session、tool diff、文件和 commit 无法无歧义连接时，只能在可连接人口上计算 survival；未提交、被放弃或缺失的失败不能静默当作没有发生。[有限开发日志研究](https://arxiv.org/html/2604.20779v1)因此提供观测边界而非生产率因果排名：vibe-coding 与其它 agent mode 的采用本就可能内生，静态 scanner 的 findings/committed-line 也不等真实漏洞发生率。应同时保存完整session分母、join资格、成功标签来源和审查/规划/人工成本；代码存活不认证功能正确或安全。连接不足、标签失准或历史覆盖偏差无法控制时，保留分项描述、独立执行测试与人工审计，不从留下来的代码反推全部尝试的成功。<!-- source-family:SF-2026-ARXIV-2604-20779 -->

### 20816 → TRAIN-RLHF 最小单段PRE

作者actual Ch31 rewardbasis/jury、bottleneck、SER/ESR、adaptive scalarizer与GradientHarmonization完整局部，Ch24条件control及Ch30/32交接。旧聚合不含偏好ω作为部署condition的一模型目标surface。拟在GradientHarmonization旧marker后、DemonstrationDerivedReward标题前：

> 多目标取舍也可以作为部署条件交给同一生成器，而不为每个固定权重训练独立模型：把偏好向量作为额外 conditioning，训练时对同一条件下的各 reward 分别标准化、形成各自 loss，再在 loss 层按偏好合并。这样共享的是一张可查询的条件化生成 surface，不是已经找到所有真实 Pareto 解；标准化改变指标单位，也不同于直接最大化原始 reward 的加权和。[有限条件化对照](https://arxiv.org/html/2604.20816v1)中 late aggregation 的中间偏好表现较平滑，但有限提示和五个权重不证明连续偏好全域正确，坏 reward 会扭曲整张 surface。Condition encoder、reward尺度、warm-start、LoRA 与评价 reference 都需版本化，全部训练/评分费不能由单模型数目抵消；偏好超出支持、质量或校准回归时，保留固定权重 specialists、原 scalarization 与分项独立验收，不让 preference knob 获得事实或安全权限。<!-- source-family:SF-2026-ARXIV-2604-20816 -->

### 20819 → MODEL-SELF-ATTENTION 最小单段PRE

作者actual Ch14 Attention语义/FlashAttention/数值实现完整局部，Ch48 SpecStream runningmax NumDen与Ch54驻留交接。没有pair-cover子序列任务及跨段未归一归约的责任，拟在FlashAttention“这些技术共享Attention背景...”后、数值与实现边界标题前：

> 若完整序列仍放不进设备，还可把允许的 query–key pairs 分配给若干相互覆盖的子序列任务，而不是让每段各做 softmax 后直接平均。组合设计必须保证每个有效 pair 被处理、重复对角只计一次，并继承原 mask；各任务累加未归一的 numerator 与 denominator，再汇总后统一相除，反向也沿同一归约重算和累加。[有限 pair-cover 分解](https://arxiv.org/html/2604.20819v1)依赖所选 Steiner 结构确实存在，实数算术恒等不等低精度 bitwise exact；从局部 out/lse 还原质量时，共同数值缩放仍须实现验收。Host accumulator、gather/transfer、mask、二次总计算与 OOM 后的部分写回恢复都计费，缩尺任务外推不是完整十亿 token 执行。覆盖、内存或数值恢复未闭时，保留普通分块/streaming Attention 与已验证序列上限，不由可重排任务推出整模型不会 OOM。<!-- source-family:SF-2026-ARXIV-2604-20819 -->

### 20835 → TRAIN-SFT 最小单段PRE

作者actual Ch29少量示教、轨迹结构/行动接口与SFT选择/蒸馏局部，Ch28/30交接。旧语言/格式覆盖未区分相同题目跨PL配对与同总样本但题目不相交的初始化。拟在“重复大量同质examples”段后、拒答示教前：

> 跨语言监督还要保存“哪些实现解决同一道题”的配对关系，而不只保持各语言样本总数。可让同一问题的多种编程语言实现共同进入 SFT，再只在少数 source languages 上做 RL，检查是否把收益带到未参与监督的 target language；同题配对与各语言独立题集是不同初始化。[有限 Parallel-SFT 对照](https://arxiv.org/html/2604.20835v1)支持这一选择，但同题实现数分布也在改变，表示相似与迁移相关不唯一证明语义 hub；测试通过的合成代码也不是任意输入的形式等价。Problem/language配对、过滤器、SFT/RL人口及target oracle资格须共同保存，造数、测试、全部SFT与RL计费。未检测到source下降不证明永不牺牲；配对失真、target验证不可得或质量回归时，保留独立多语言SFT、可信目标示教与分语言验收，不把语言无关题目误写成目标语言完全无法直接训练。<!-- source-family:SF-2026-ARXIV-2604-20835 -->

### 19837 → PLATFORM-EVALUATION-SYSTEM 最小单段PRE

作者actual Ch66 expectedfactinventory完整定义/unknown/来源粒度、harness/testboundary与Ch77知识效用局部、Ch65/67交接。旧inventory有漏项风险，但未覆盖知识memory与评价completeness分母共同跨run转移的混杂。拟在SF2608-31016 marker后、UserSimulator标题前：

> 经验复用也可能同时改变被测能力和 evaluator 的分母：把强模型积累的文档知识交给弱模型后，后者不仅更会找信息，还可能借同一经验重新定义“应找到哪些项”。即使 task/runtime 相同、分母后来稳定，也不能把每次自建 inventory 的 coverage 百分比当作同一测量。[有限知识迁移审计](https://arxiv.org/html/2604.19837v1)暴露这条路径，并显示评测文件线索可能经 postmortem 变成可传播知识；隐藏文件名不等于隔离评价资产。应冻结独立权威 inventory，把能力增益、分母修正与评价泄漏分别报告；命名空间/工具可见性、knowledge lineage、独立审校和强模型预积累全部计费。原分母或权限边界不可核时，保留原始items、固定判据和 Unknown，不让更熟悉答案的自评者批准更高完整性，也不由迁移后的低API账单抹掉知识制备成本。<!-- source-family:SF-2026-ARXIV-2604-19837 -->

## A8. 最后四项Owner：作者actual（非fresh结果）

此前向已结束fresh reader仅发送消息请求，未取得其这四项owner结果；不能计fresh实际通过。以下四项由作者本人实际比较，必要Source有效层不重审，均待root独立处置。前三批14真实I已actualPOST并释放相应lease，20348/20392本人注已明确fresh必要Source与root现正文/PRE/POST分责；三Data单段已保存待POST，其余普通按本日有限清单继续。

### 20328 → TRAIN-GRPO 最小单段PRE

作者actual Ch33 TypedCreditBoundary完整innerMDP、UDM重采样目标/cross-trajectory ratio/ODE surrogate/pivot噪声分支（395–420）及Ch31/32/34必要交接。没有连续latent deterministic mode-only proposal与vMF参考更新的测度边界；拟在SF2609-12245 marker后、离散diffusion段前：

> 混合推理还可以把文字 token 与连续 latent 当作两种更新对象：文字沿 categorical policy 计概率，latent 则用方向分布定义局部参考和单独 clipping。若 rollout 实际只输出该方向分布的 mode，而没有从它随机采样，参考方向上的新旧密度比只是训练 surrogate，不是实际供给分布的 importance ratio；再保留未归一 hidden norm、用 inner product 替代纯方向相似时，原归一化密度及解析 KL 更不能直接继承。[有限混合 latent 对照](https://arxiv.org/html/2604.20328v1)支持拆开两类更新，却不授 exact 零方差校正或全局 trust region。Latent proposal、归一规则、旧 mode、clip 与两类 loss 权重须共同保存，额外 latent steps、筛组、训练与独立答案验证都计费；方向代理或质量失配时，保留普通文字推理、可信 SFT 与分别校准的更新，而不让一个好看的 density 公式替实际采样 law 签字。<!-- source-family:SF-2026-ARXIV-2604-20328 -->

### 20730 → MULTIMODAL-GENERATIVE-PARADIGMS 最小单段PRE

作者actual Ch24 WorkflowIntermediateState完整局部（1049起）与SVG serialization/typeddecoder完整段（1271–1290）、Ch23/25交接。旧单path坐标分工未有跨subpath hole/opacity依赖决定render反馈原子单位；拟在SF2602-21461段后、Any-to-any标题前：

> 让生成中的 SVG 回看局部 render 之前，还须先决定什么是可独立显示的修改单位。单个 subpath 可能依赖其它轮廓形成孔洞，opacity 与重叠又会改变其显示结果；先把这类依赖合成一个 component，再交错生成与重渲染，才不会把本来不可独立解释的碎片当作失败反馈。[有限 render-in-the-loop 对照](https://arxiv.org/html/2604.20730v1)支持该原子单位与匹配训练的选择，未经相应训练的直接视觉反馈仍可退步；路径规范化也不保证任意 SVG 全语义等价。Pixel-difference/repetition gate 只决定是否重采样，重试耗尽后强制 END 不是画面已完成。合并/渲染、视觉编码、完整历史、重试与训练全部计费；微小细节误停、依赖解析或预算失配时，保留原 serialization、整图渲染/外部检查与有界修订，不由合法 END 批准成品质量。<!-- source-family:SF-2026-ARXIV-2604-20730 -->

### 19859 → TRAIN-GRPO 具体NC提案

作者actual Ch33 phasecredit完整旧分支与19945新段（896–913）、semanticsegment局部、DerivedSkill probabilitydelta三段（1180–1193），并读Ch31/32/34必要交接。Current-policy对gold answer的turn likelihood差、browse后的score回分此前search，是已有分段/阶段credit与belief/relevance代理的具体训练实例；不取得信息熵、真实步骤或因果verifier权限，与20659 NC采用边界一致。Same-source resampling及IGPO的局部反向实验继续入日报，format/browse/scale未独立分离、γ/标准化不保telescoping、4B另用30B总结和全部费用保留，不为参数配方再堆正文。不因无普遍保证或4B而否贡献；拟NC非已独核。

### 20841 → MULTIMODAL-EMBODIED-VLA 最小单段PRE

作者actual Ch26“要到哪里/这台机器怎样到达”、多指接触恢复、geometry消费者完整局部（18–50、126–135）、privileged3Dteacher/部署几何分责（152–176）及Ch25/27交接。未有同一imitation task为human与object采用不同维度target、再由仿真闭环对齐的接口；拟在SF2605-20811 end后、“但目标到哪里在多指接触...”前：

> 视频示教的目标也不必全部恢复成同一种三维状态：已知初始 mesh 与 camera 时，可为 human 估计三维姿态，却只用可见 object 的二维轨迹作另一约束，再由物理仿真中的 policy 联合跟踪。这把较难取得的完整 object pose 换成投影目标，不证明单视频唯一恢复了真实几何或接触；投影相近仍可能在深度方向发生不同运动。[有限合成视频模仿对照](https://arxiv.org/html/2604.20841v1)支持这种混合 target 选择，精确放置、抢夺与不可见接触仍会失败，成功子集上的对齐误差也不是完整任务成功率。Scene/camera、human estimator、可见轨迹、接触 proxy 与每段训练 policy 应分别绑定；视频生成、估计、对齐和每motion RL均计费，单 A6000 的250frame约20小时不是零样本或实时控制。遮挡、深度歧义、动力学或预算失配时，保留真实示教、明确三维/接触状态与独立 controller，不由模拟器中可行动作签发真实机器人安全。<!-- source-family:SF-2026-ARXIV-2604-20841 -->

## A9. 进行中可读稿与限定校验（待DAY）

发现与必要Source不再扩张：57家族均有具名自然日资格/轻量当前说明检查和有限必要技术独核；原EX重开/具体关闭及分层负侧范围见A3–A5。所有owner决定已具名闭合，实际对账为28拟整合/20已有覆盖/3仅报告/6整族中心D；20728仅有限一步I、V2强桥另隔离，不另算家族。

28项获批正文均已真实保存于15唯一owner，结构对账40正文段、28本人注、24份可提取逐字PRE与实际正文无差异；19907/19945原两I及20685/19954两单段沿root actual有效层复用。root确认28实际POST均通过、全部窄lease释放；末20328/20730/20841亦按其非writer实际新段/完整邻接/本人注结果通过。已POST的本人注仅行政同步并读回，Source角色按root/fresh实际结果，不一概写root阅读全文。

README已融入六部分，候选单表142=原85+新增57；14source不重复ID，新增57证据/具体Books理由在原连续§4之后。实比原85整行85/85、原小时窗及原连续§4均exact保持。V3格式/一致性校验通过；715链接、378本地引用/56唯一相对路径零missing；SUP尾空白0，限定15Books+README unstaged diffcheck0。六整族D身份在Books无引用命中，不凭校验签语义完成。保既有staged/unstaged与并发2025，未stage/commit/push。

当前普通只剩完整六部分DAY、完成态保存和最小FINAL；无新Source/owner队列。21921缺Apr23已公开正文、历史目录缺段及中心强桥争议均按§5终态隔离，不支持正面证据/Books/全站无遗漏；只在具名新原证到达时定点重开，不请求无关全月材料。

## A10. root完整DAY与保存完成态FINAL实际通过

root非报告作者完整六部分DAY通过：实际读57全部新增§4及§1/2/5/6，逐项有限必要Source/owner与28真实POST有效复用；14源实际范围/外部限制、9具名负侧分层样本与未全查范围、日期投影/19954异常/21921资格隔离及六整族D、20728局部V2隔离均按真实边界。不是再全量重审旧85，不证明所有论文主张或全站无遗漏。此前七个行政旧状态残留已按root/fresh实际角色修正，SRC-SEED仅21921必要公开日受阻，有限目录已读层不否定。

实际对账142=原85+新增57；本轮28真实I（15唯一owner/40正文段）、20具体NC、3Only、6整族中心D。28实际POST均已通过、所有窄lease释放，普通研究/Books待办0。root实际V3、42窗口测试、冻结85每行各一次/原窗口同值/连续old§4、本地引用零missing/围栏偶数与限定diff检查通过；机器校验不代语义。

作者于2026-10-16T03:30:41+08:00仅行政保存完成状态/时间、§1普通0、§5隔离和§6通过并实际读回。root随后最小FINAL实际读取该完成字段/§1/5/6，scope未扩，actual V3及README cached/unstaged diffcheck0；冻结85整行/原窗口/连续old§4仍有效，正式接受本日完成。§5等待读回残留已仅行政同步为实际通过，不新开研究。

作者ownership在此释放；不接其它日期，不改LS/index/合同，不stage/commit/push。root负责LS协调与下一日分派，保既有staged/unstaged及并发2025写入。外部日期/目录/中心主张保留项仍不作正面证据、Books或覆盖保证，只按具名新原证定点重开。


