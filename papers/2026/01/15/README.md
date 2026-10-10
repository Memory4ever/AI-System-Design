# Daily Research — 2026-01-15

**规范：** V3
**窗口：** 2026-01-14T09:00:00+08:00 ～ 2026-01-15T09:00:00+08:00
**补充窗口：** 2026-01-14 ～ 2026-01-14
**窗口说明：** 用户于2026-10-07授权对现有Daily只补来源遗漏；保留原窗口、52家族原日期/评分及有效审阅，新增材料按前一完整北京时间自然日检查，不搬移旧归属。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T00:50:13+08:00

## 1. 结论

本轮2026-10-07启动的增量补查已达本日安全终态，检查时间到10-08而补窗不移动；原52家族与原验收只复用有效成果，不代表本轮验收。正式新增51家族：24项必要命题深入与实际Books POST通过、17项标准必要证据/具体已有覆盖通过、6项仅报告（08082标准，08251/08653/08557/08430/08276低分关闭判断）、4项中心争议隔离（08333/08271/08280/08726）。07963/08815/08778本窗首次公开或重要增量未建立，不评分/Books、不定旧日。78份完整题摘和216库存不是候选/全文队列；普通扫描/筛选/候选审阅/Books待办0，review_jan15_delta非作者已实际核六部分，独立DAY通过。[增量停点](../_sources/daily-20260115/supplement-20261007.md)。

冻结52个唯一论文家族：39项实际整合并经非作者root正文/邻接/末注写后通过、3项已有具体覆盖、8项仅报告、2项中心主张争议隔离；没有结构候选。既定arXiv分页已补至下界，尾部七项全部获得必要审阅与处置，GEPA因日期区间跨窗隔离。HA-DW此前未保存数字分数，本次首次明确2+1+3=6并经独立确认。root已完整顺读正式六部分并核来源停止点、条件日期、逐项证据/Books与具名负侧范围，非作者独立日级Gate通过；普通待办0。

最重要的变化不是宣称更多模型/系统更好，而是把具体接口分开：单连续reasoning state不等K条轨迹；全局时长预算不等逐kernel无慢；树内工具credit、memory最新update-step与workflow prerequisite均是受条件限制的proxy。偏好目标还依赖部署k、采样coverage和reference/history身份；评价中的language-ID、拒绝率、hidden一致与合法终态都不替代真正需要验证的对象。

39项实际改动保留原方案、局部反侧及成本。没有运行代码、复现实验或证明生产收益；论文作者结果与本报告工程推断分开。下面52项的证据/Books结果均已独立逐项确认，不因补尾校准重审未变化部分。原始查询总数、读取完整题摘数与当窗家族不是一个分母；首次宽114与AB2取得65均仅发现库存，AB2未审53不成为默认任务队列。

## 2. 来源覆盖

只处理14个Daily入口及实际论文/日期恢复，不扫Weekly。以下“已检查”只代表所列有限切片；外部保留项不支撑无遗漏或零研究结论。[来源恢复细节](../_sources/daily-20260115/SOURCE_RECOVERY.md)、[原官方说明](../_sources/daily-20260115/OFFICIAL_CORE_RAW.md)、[原API](../_sources/daily-20260115/THEME_API.jsonl)和[补尾标题](../_sources/daily-20260115/THEME_TAIL_TITLES.jsonl)保留依据。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮Research当前目录首屏/RSS受限；Jan14日期主题检索；原Cerebras与RFP同event必要core复用，检索到Academy教育活动标题范围外停止 | 已检查 | 当前目录不是历史全集；有限检索无新可核mechanism，采购/集成计划不授上线性能，历史删漏只由dated原条目重开 |
| SRC-ANTHROPIC | 本轮Research当前首10条，native403；Jan14 PBT blog与2510.09907v1同身份有效核心复用 | 已检查 | 本轮未见新事件差额；Sonnet4.5/evaluationagent/三专家为局部验证配方，非新PBT机制。当前首10不授历史完整 |
| SRC-GOOGLE-AI | 本轮DeepMind当前6条May–Sep；Research pubs总11597首15条至2027；官方域Jan14日期主题查询，原FunctionGemma card身份复用 | 受阻 | 当前首屏/查询无命中不证明Jan14 archive齐全；UpdatedJan14不是Dec18机制新公开。原dated新事件/目标日列表到达定点重开 |
| SRC-META-AI | 本轮Research空shell，官方域January14日期主题查询；原native shell有效失败身份复用 | 受阻 | 未恢复Jan14历史条目，空响应不作零；需dated原目标正文或可读archive，只重开对应身份 |
| SRC-QWEN | 本轮旧blog实际redirect qwen.ai，新blog动态shell；site:qwen.ai 2026-01-14有限检索，原浏览器/已观察资产失败复用不再遍历chunk | 受阻 | 新入口未恢复本窗历史article列表；需具体Jan14原dated条目/usable archive，不据current空shell授零 |
| SRC-DEEPSEEK | 本轮当前官网非archive及site:deepseek.com 2026-01-14；Engram公开PR/issue同event原有效日期复用 | 已检查 | Engram原Jan13T03:47:53Z早于补充窗，不搬材料；其余历史目录不可由current首页/无检索命中证明无遗漏 |
| SRC-MOONSHOT | 本轮Platform Blog有限dated列表至Nov7/6'25并停止；site:platform.kimi.com 2026-01-14有限查询；GitHub仅原身份去重非历史扫描 | 受阻 | 未恢复Jan14可用列表；需具体本窗dated报告/release或archive，不以当前旧blog/仓库代替 |
| SRC-TENCENT-HUNYUAN | 本轮首查Research direct timeout、后台浏览器create实际30秒timeout/内核reset；官方域Jan14定点查询，原GitHub fallback有效入口复用 | 受阻 | Research列表不可读且current仓库不是Janarchive；原dated本窗研究条目/实际Research列表可替代，不称零、不无限重试 |
| SRC-ZAI | 本轮Research有限dated目录Jan19→Jan13→Dec10跨窗；官方release-notes明确Jan14 GLM-Image事件，实际guide/API核心；原Jan13 research/早repo身份复用 | 已检查 | Jan14API availability不是先前研究first-public；仅text→image URL/size/quality与既有AR+DiT/Glyph暴露，具体贡献前关闭。原research日期保留不动；当前API不授性能/安全或512/1024尺寸冲突保证 |
| SRC-BYTEDANCE-SEED | 本轮当前Research/Public Papers与既有真实get_article_list_v2恢复接口；2026/type1/count20/offset60→80跨Feb26→Jan26→Jan21/19且end；type2 EN0、ZH0/20终页有效范围复用 | 已检查 | 当前语言过滤/total与visible不一致，最早blogFeb12；仅这有限返回无新Jan14event，catalog删除/语言漏段不授历史齐全 |
| SRC-BAIDU-ERNIE | 本轮官方blog有限datedJan29→Jan15→Jan8→Nov21越过Jan14停止；原Jan15榜单core与GitHub身份复用 | 已检查 | Jan15榜单产品排名无新mechanism，补充窗外不搬；current catalog不证明历史全集，具体dated原事件可定点恢复 |
| SRC-XIAOMI-MIMO | 本轮官方8 dated paper tiles：Jun29/Mar13/Feb3/Jan8及更早；15 undated blogs与Flash原blog shell，有限可见目录读完 | 受阻 | Jan8 paper在补充窗前；undated/无body的历史blog不作零，需dated本窗机制正文或可读目标archive |
| SRC-MINIMAX | 本轮CN dated catalog Jan28→Dec23→Oct27→Jan15'25越窗；EN当前首屏不齐；AgentTech原入口→llms.txt→techblog.md仅May13一条并end，原有效接口停止复用 | 已检查 | 所读有限目录无新Jan14event；语言/删漏历史保留，不授全机构无遗漏，需具体dated原研究/release重开 |
| SRC-ARXIV | 原52和有效原筛选只去重；本轮四主题日粒度API submittedDate Jan12–14仅发现：model281读0/100末Jan12T17:55:51Z；agent341读0/100/200末Jan12T08:07:35Z；multimodal114/page0末Jan12T08:15:36Z；system22/page0末Jan12T01:17:01Z，均越Jan12T19下界停止 | 已检查 | 正常cohort跨主题216唯一身份仅库存，78完整题摘与formal候选分开，不逐项全库存AB/fulltext。额外越界页仅保存；12位无效API过滤不授零。CL/DC月首200及CL/CV/AI有界月页访问失败，原公告/目标list可恢复具名日期，不授全学科召回 |

表外：arXiv论文exact-v1 HTML/原作者repo、DataCite exact DOI与arXiv官方availability，均由具体材料或日期歧义触发；只用于其权限内的必要证据/身份恢复。来源清单八个按需软件项目未发生本窗机制触发，不扫描。其他辅助索引只发现，不能支持性能、安全或first-public断言。

## 3. 候选与判断

公开范围均含起点、不含终点；共同下界是批次公告Jan14T01Z，右界为该DOI registered的秒精度存在上界再加一秒，依据/条件见§4。不是把Submitted、Available月份或registered直接当首次公开时刻。以下当前52家族不包括日期跨窗的GEPA，不因深审耗时缩池。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge](https://arxiv.org/html/2601.08808v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T11:00:11+08:00 | 单token离散轨迹→K抽样embedding聚合到一个连续state→重新区分投影状态与K独立轨迹；2+2+2=6 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../Books/part-02-model/20-sampling.md) |
| [Reducing Compute Waste in LLMs through Kernel-Level DVFS](https://arxiv.org/html/2601.08539v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:53:38+08:00 | 逐kernel不慢→总kernel时长约束容许局部慢→时钟优化改用全局预算；2+2+2=6 | 深入完成 | 整合：PLATFORM-COST [Ch70](../../../../Books/part-06-ai-infrastructure/70-cost.md) |
| [MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm](https://arxiv.org/html/2601.08800v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:59:59+08:00 | 固定collective→分层A2A/RS/AG与并行计划联合搜索→布局选择受硬件拓扑制约；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../Books/part-05-inference-system/49-tensorrt-llm.md) |
| [Modeling LLM Agent Reviewer Dynamics in Elo-Ranked Review System](https://arxiv.org/html/2601.08829v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T11:00:41+08:00 | reviewer排名→Elo适应同时产生metric退步→评价准确与激励gaming分账；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling](https://arxiv.org/html/2601.08777v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:59:27+08:00 | 单输出偏好目标→k-dependent product policy人口win-rate界→训练目标绑定部署采样数；2+2+3=7 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md) |
| [Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs](https://arxiv.org/html/2601.08763v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:59:07+08:00 | token entropy代理策略→本组策略frequency乘全部signed advantage→稀有负adv也变权；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../Books/part-04-training-system/33-grpo.md) |
| [PrivGemo: Privacy-Preserving Dual-Tower Graph Retrieval for Empowering LLM Reasoning with Memory Augmentation](https://arxiv.org/html/2601.08739v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:58:30+08:00 | 名称匿名化→remote最小拓扑/local原KG验证→曝光与grounding分权；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../Books/part-06-ai-infrastructure/72-security.md) |
| [RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis](https://arxiv.org/html/2601.08699v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:57:30+08:00 | clean教师轨迹→受控fake retrieval后恢复→噪声暴露、筛选与observation mask分工；2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../Books/part-04-training-system/27-data.md) |
| [Analyzing Bias in False Refusal Behavior of Large Language Models for Hate Speech Detoxification](https://arxiv.org/html/2601.08668v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:56:44+08:00 | 毒性input被当请求风险→benign detox拒绝人口变化→拒绝率与输出效用/安全分账；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../Books/part-06-ai-infrastructure/72-security.md) |
| [From Rubrics to Reliable Scores: Evidence-Grounded Text Evaluation with LLM Judges](https://arxiv.org/html/2601.08654v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:56:24+08:00 | rubric prompt→immutable compile→lexical gate→后calibration→区分criterion身份与末分有效性；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs](https://arxiv.org/html/2601.08634v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:55:56+08:00 | 固定model价值测量→moral endorsement和role改变人口→区分条件输出与内部道德；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [How Order-Sensitive Are LLMs? OrderProbe for Deterministic Structural Reconstruction](https://arxiv.org/html/2601.08626v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:55:45+08:00 | semantic recall稳定→四字符23permutations重建错→解释稳定与canonical reconstruction独立；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Ministral 3](https://arxiv.org/html/2601.08584v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:54:47+08:00 | one-shot压缩→前个short checkpoint初始化的cascade→short与final-long分支区分；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../Books/part-04-training-system/28-pretraining.md) |
| [Your Group-Relative Advantage Is Biased](https://arxiv.org/html/2601.08521v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:53:11+08:00 | group-relative无偏假定→选样条件baseline偏移命题→检查conditioning/gradient对象；2+1+3=6 | 争议 | 暂缓：中心命题隔离见§4 |
| [BenchOverflow: Measuring Overflow in Large Language Models via Plain-Text Prompts](https://arxiv.org/html/2601.08490v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:52:25+08:00 | 长度账本→5k cap右删失与utility反侧→resource amplification不等可用性；2+1+2=5 | 深入完成 | 整合：PLATFORM-COST [Ch70](../../../../Books/part-06-ai-infrastructure/70-cost.md) |
| [Surgical Refusal Ablation: Disentangling Safety from Intelligence via Concept-Guided Spectral Cleaning](https://arxiv.org/html/2601.08489v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:52:23+08:00 | exact protected nullspace假定→ridge residual有限registry→geometry不授behavior保留；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../Books/part-01-worldview/05-what-neural-networks-learn.md) |
| [JudgeRLVR: Judge First, Generate Second for Efficient Reasoning](https://arxiv.org/html/2601.08468v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:51:50+08:00 | generate RLVR直接初始化→同policy judge-gold后generate→objective阶段交接；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md) |
| [Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management](https://arxiv.org/html/2601.08435v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:51:01+08:00 | final task reward→last-update-step memory credit→局部QA与检索operation反馈分离；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../Books/part-07-agent/77-memory.md) |
| [Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering](https://arxiv.org/html/2601.08427v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:50:49+08:00 | 外部verifier单一来源→last-hidden robust centroid proxy→reward来源与truth分账；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../Books/part-04-training-system/33-grpo.md) |
| [Coverage Improvement and Fast Convergence of On-policy Preference Learning](https://arxiv.org/html/2601.08421v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:50:40+08:00 | onpolicy覆盖口号→conditional linear-BT coverage/errorfloor→刷新须匹配batch和joint design；2+2+3=7 | 深入完成 | 整合：TRAIN-DPO [Ch34](../../../../Books/part-04-training-system/34-dpo.md) |
| [Controlled LLM Training on Spectral Sphere](https://arxiv.org/html/2601.08393v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:49:57+08:00 | update谱约束→unique-top tangent求根+radial校正→有限步不等exact双侧不变量；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../Books/part-04-training-system/28-pretraining.md) |
| [Deconstructing Pre-training: Knowledge Attribution Analysis in MoE and Dense Models](https://arxiv.org/html/2601.08383v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:49:42+08:00 | final knowledge attribution→GatedLPI同模型时序/干预→区分local sensor与架构causal；2+1+2=5 | 标准完成 | 仅报告：局部观察/诊断不改变长期owner，见§4 |
| [CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark](https://arxiv.org/html/2601.08331v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:48:28+08:00 | language-ID成功→language control和semantic relevance双轴→选择layer/strength须heldout；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting](https://arxiv.org/html/2601.08316v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:48:06+08:00 | double-descent解释→signal/noise activation分离→分离现象非必要充分；1+1+2=4 | 已关闭 | 仅报告：局部观察/诊断不改变长期owner，见§4 |
| [Demystifying the Slash Pattern in Attention: The Role of RoPE](https://arxiv.org/html/2601.08297v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:47:39+08:00 | content-only slash解释→activation Q/K近rankone+RoPE频谱条件→位置偏好受条件限定；2+1+3=6 | 深入完成 | 整合：MODEL-POSITION-ENCODING [Ch13](../../../../Books/part-02-model/13-position-encoding.md) |
| [Discovery and Reinforcement of Tool-Integrated Reasoning Chains via Rollout Trees](https://arxiv.org/html/2601.08274v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:47:07+08:00 | iid完整rollout→tool-hint条件树local+global span credit→工具机会proxy分账；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../Books/part-04-training-system/33-grpo.md) |
| [MPCI-Bench: A Benchmark for Multimodal Pairwise Contextual Integrity Evaluation of Language Model Agents](https://arxiv.org/html/2601.08235v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:46:08+08:00 | privacy只数拒绝→samevisual positive/negative CI pair→utility与leakage同账；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../Books/part-06-ai-infrastructure/72-security.md) |
| [Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints](https://arxiv.org/html/2601.08215v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:45:40+08:00 | total/active params→expert/core geometry非唯一→匹配memory和compute仍需结构自由度；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-MOE [Ch21](../../../../Books/part-02-model/21-moe.md) |
| [Generation-Augmented Generation: A Plug-and-Play Framework for Private Knowledge Injection in Large Language Models](https://arxiv.org/html/2601.08209v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:45:31+08:00 | text序列注入→frozen expert晚层state/projector替换base anchor→input-adapter带宽与总成本分离；2+2+2=6 | 深入完成 | 整合：MODEL-EMBEDDING [Ch12](../../../../Books/part-02-model/12-embedding.md) |
| [Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs](https://arxiv.org/html/2601.08198v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:45:16+08:00 | 当前pairgap坍缩→gold/current与current/frozeninitial两项→固定gold/历史cache分工；2+2+2=6 | 深入完成 | 整合：TRAIN-DPO [Ch34](../../../../Books/part-04-training-system/34-dpo.md) |
| [Evaluating Implicit Regulatory Compliance in LLM Tool Invocation via Logic-Guided Synthesis](https://arxiv.org/html/2601.08196v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:45:13+08:00 | final goal成功→LTL规则+masked搜索trace→oracle-relative compliance压力；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Relational Knowledge Distillation Using Fine-tuned Function Vectors](https://arxiv.org/html/2601.08169v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:44:36+08:00 | 统计取回functionvector→learnedaffine组合→训练身份不等relation代数定律；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../Books/part-01-worldview/05-what-neural-networks-learn.md) |
| [WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents](https://arxiv.org/html/2601.08158v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:44:21+08:00 | 历史经验文本→成功/恢复/失败procedure+prerequisite→软guidance不同harddispatch；2+2+2=6 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../Books/part-07-agent/81-workflow.md) |
| [Attention Projection Mixing with Exogenous Anchors](https://arxiv.org/html/2601.08131v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:43:43+08:00 | identity residual→外部anchor投影混合→另一attention通路不等导数I；2+2+2=6 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../Books/part-02-model/17-transformer-layer.md) |
| [Debiasing Large Language Models via Adaptive Causal Prompting with Sketch-of-Thought](https://arxiv.org/html/2601.08108v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:43:12+08:00 | prompting偏差→frontdoor识别命题→因果调整的分布条件不可省略；2+1+3=6 | 争议 | 暂缓：中心命题隔离见§4 |
| [STO-RL: Offline RL under Sparse Rewards via LLM-Guided Subgoal Temporal Order](https://arxiv.org/html/2601.08107v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:43:10+08:00 | sparse reward→LLM subgoal temporal potential→局部noise与terminal条件限制；2+1+2=5 | 标准完成 | 仅报告：局部观察/诊断不改变长期owner，见§4 |
| [AdaJudge: Adaptive Multi-Perspective Judging for Reward Modeling](https://arxiv.org/html/2601.08097v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:56+08:00 | scalar reward→全K refinement+多视图readout→aggregation不等earlyexit/token真值；2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md) |
| [Q-realign: Piggybacking Realignment on Quantization for Safe and Efficient LLM Deployment](https://arxiv.org/html/2601.08089v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:45+08:00 | reconstruction-only PTQ→class-conditional frozenSLR loss→safetyproxy与utility同时验；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../Books/part-05-inference-system/49-tensorrt-llm.md) |
| [MemoBrain: Executive Memory as an Agentic Brain for Reasoning](https://arxiv.org/html/2601.08079v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:31+08:00 | 普通consolidation→resolved Fold/未resolved Flush→状态区分与原轨迹回读；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../Books/part-07-agent/77-memory.md) |
| [Semantic Gravity Wells: Why Negative Constraints Backfire](https://arxiv.org/html/2601.08070v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:19+08:00 | negative instruction稳健假定→目标token干预局部失败→行为反证与component因果分开；2+1+2=5 | 标准完成 | 仅报告：局部观察/诊断不改变长期owner，见§4 |
| [Universal computation is intrinsic to language model decoding](https://arxiv.org/html/2601.08061v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:07+08:00 | fixed-interface可达性→unbounded external string consume/append协议→机器身份改变；2+2+2=6 | 深入完成 | 整合：MODEL-DECODER-ONLY [Ch18](../../../../Books/part-02-model/18-decoder-only.md) |
| [Triggering Chain-of-Thought via Latent Feature Interventions in Large Language Models](https://arxiv.org/html/2601.08058v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:03+08:00 | 强genuineconcept资格→首步SAE操作mode-control→行为有效不等唯一module；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../Books/part-01-worldview/05-what-neural-networks-learn.md) |
| [DYCP: Dynamic Context Pruning for Long-Form Dialogue with LLMs](https://arxiv.org/html/2601.07994v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:40:33+08:00 | 预写段或topK→query-time contiguous span→按时间assembly兼顾context预算；2+1+2=5 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../Books/part-07-agent/75-context.md) |
| [Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs](https://arxiv.org/html/2601.07972v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:40:03+08:00 | selfsurvey价值→recognition/role/文字选择分离→text choice不等执行行动；2+1+2=5 | 标准完成 | 仅报告：局部观察/诊断不改变长期owner，见§4 |
| [Calibration Is Not Enough: Evaluating Confidence Estimation Under Language Variations](https://arxiv.org/html/2601.08064v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:42:11+08:00 | ECE/AUROC充分假定→P-RB/A-STB语义变化blindspot→局部诊断与敏感度隔离；2+1+2=5 | 标准完成 | 仅报告：局部观察/诊断不改变长期owner，见§4 |
| [MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness](https://arxiv.org/html/2601.08118v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:43:25+08:00 | task success代理→用户human-likeness与lexical/judge可分离→另验模拟人口；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TP-Blend: Textual-Prompt Attention Pairing for Precise Object-Style Blending in Diffusion Models](https://arxiv.org/html/2601.08011v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:40:56+08:00 | 整体风格注入→full-head对象位置迁移与self-attention HF分支→content/style分别校准；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LLM Review: Enhancing Creative Writing via Blind Peer Review Feedback](https://arxiv.org/html/2601.08003v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:40:45+08:00 | 公开全部修订稿→分享critique但不分享revised drafts→保留独立创作轨迹；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../Books/part-07-agent/82-multi-agent.md) |
| [Reasoning over Precedents Alongside Statutes: Case-Augmented Deliberative Alignment for LLM Safety](https://arxiv.org/html/2601.08000v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:40:41+08:00 | 显式安全规则越多越好→code/case局部安全与误拒反向→绑定训练/推理人口；2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md) |
| [Cost and accuracy of long-term graph memory in distributed LLM-based multi-agent systems](https://arxiv.org/html/2601.07978v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:40:11+08:00 | graph更多关系默认更强→网络/建图成本增加但accuracy差异不显著→成本与证据强度分账；2+2+2=6 | 标准完成 | 仅报告：一次受限成本/准确观察；等效/Pareto子命题不采用 |
| [Towards Specialized Generalists: A Multi-Task MoE-LoRA Framework for Domain-Specific LLM Adaptation](https://arxiv.org/html/2601.07935v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:39:08+08:00 | uniform/top/bottom分配→局部top优于bottom观察→保留层间资源配置的受限验证；2+1+2=5 | 标准完成 | 仅报告：非等容量层因果、无稀疏执行保证 |
| [Embedded AI Companion System on Edge Devices](https://arxiv.org/html/2601.08128v1) | 2026-01-14T09:00:00+08:00 ～ 2026-01-14T10:43:39+08:00 | 同步memory维护阻塞响应→active检索/存raw与inactive extract/merge分期→校准session空闲期维护边界；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../Books/part-07-agent/77-memory.md) |
| [When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges](https://arxiv.org/html/2601.08343v1) | 2026-01-14 | 新增补充：固定候选/顺序的dense参照下，answer质量与selection/attribution分账；3+2+2=7 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，正文selection/attribution段及末注，root实际POST通过 |
| [Training-Free Distribution Adaptation for Diffusion Models via Maximum Mean Discrepancy Guidance](https://arxiv.org/html/2601.08379v1) | 2026-01-14 | 单样本surrogate guidance→有限reference人口的attraction/repulsion与prompt×latent kernel接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root实际POST通过 |
| [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://arxiv.org/html/2601.08325v1) | 2026-01-14 | 固定已观察pointcloud→virtual view/zoom分配render-resolution预算，不等新sensor observation；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，root实际POST通过 |
| [Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs](https://arxiv.org/html/2601.08773v1) | 2026-01-14 | 抽取成功才embedding会缩corpus并混杂建库费用→manifest独立于derived graph；3+1+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，root实际POST通过 |
| [HIPPO: Accelerating Video Large Language Models Inference via Holistic-aware Parallel Speculative Decoding](https://arxiv.org/html/2601.08273v1) | 2026-01-14 | 视觉token保留×draft/verify overlap的受限预算取舍；2+1+2=5 | 标准完成 | 已有覆盖：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)，target commit、cancel/费用与视觉budget已有具体承载 |
| [Lessons from the Field: An Adaptable Lifecycle Approach to Applied Dialogue Summarization](https://arxiv.org/html/2601.08682v1) | 2026-01-14 | 固定core prompt仅改special tokens后的模型迁移质量取舍反侧；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-PROMPT [Ch74](../../../../books/part-07-agent/74-prompt.md)，model/template/context/decoding依赖与prompt版本回归已具体承载 |
| [MemRec: Collaborative Memory-Augmented Agentic Recommender System](https://arxiv.org/html/2601.08816v1) | 2026-01-14 | curated即时邻域批量写入独立memory LM，验证rank收益与调用/token/延迟不一致的条件；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，entity/邻域provenance、异步维护/stale与全读写费用已具体承载 |
| [Learning from Demonstrations via Capability-Aware Goal Sampling](https://arxiv.org/html/2601.08731v1) | 2026-01-14 | demo访问前沿决定真实采集支持域，BC延伸供model replay再训练imagined策略；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，104–106两段，root实际POST通过 |
| [RAVEN: Erasing Invisible Watermarks via Novel View Synthesis](https://arxiv.org/html/2601.08832v1) | 2026-01-14 | 输出生成重构压力下的检测持久性须与内容proxy保持分账；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，正文191，root实际POST通过 |
| [Semantic Laundering in AI Agent Architectures: Why Tool Boundaries Do Not Confer Epistemic Warrant](https://arxiv.org/html/2601.08333v1) | 2026-01-14 | transport与warrant的形式类型分工，必然self-licensing定理前提不足的中心争议；2+1+2=5 | 争议 | 暂缓：必要定理/反例深入审阅但不进Books，三前提未排除独立OBSERVER/有效推理，需补足必要条件或更正证明 |
| [SafeRedir: Prompt Embedding Redirection for Robust Unlearning in Image Generation Models](https://arxiv.org/html/2601.08623v1) | 2026-01-14 | 风险sensor消费latent/text/timestep并以conditioning hook介入sampling，检测与干预资格分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，正文380，root实际POST通过 |
| [ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/html/2601.08620v1) | 2026-01-14 | 正式稿新增oracle/retrieval与bbox grounding评价反侧，answer不替代定位证据；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，1065–1100 pipeline/阶段receipt已有承载；Nov5旧dataset不重计 |
| [VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking](https://arxiv.org/html/2601.08611v1) | 2026-01-14 | gold-conditioned改写与多属性早停揭示标签选择/缺失及季度refresh边界；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，141–147标签链与3177–3185 provenance/refresh已有承载 |
| [TabPFN Through The Looking Glass: An interpretability study of TabPFN and its internal representations](https://arxiv.org/html/2601.08181v1) | 2026-01-14 | context-dependent probe与native output形成不同证据对象，可读出信息不授因果必要/early exit；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，2206–2229/3049–3063 probe与识别边界已有承载 |
| [Mechanisms are Transferable: Data-Efficient Low-Resource Adaptation via Circuit-Targeted Supervised Fine-Tuning](https://arxiv.org/html/2601.08146v1) | 2026-01-14 | proxy任务形成后更新decision或NearZero scope，塑性分支受初始competence约束；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，正文415/自身1357，root实际POST通过 |
| [Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/html/2601.08545v1) | 2026-01-14 | failed patch的edit方向改变下一轮reference检索proposal；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，正文732，review_jan15_delta实际POST通过 |
| [When Models Know When They Do Not Know: Calibration, Cascading, and Cleaning](https://arxiv.org/html/2601.07965v1) | 2026-01-14 | 离线small-confidence分箱的large增益决定线上small生成后升级；2+1+2=5 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，分箱升级段，review_jan15_delta实际POST通过 |
| [Cross-Cultural Expert-Level Art Critique Evaluation with Vision-Language Models](https://arxiv.org/html/2601.07984v1) | 2026-01-14 | aggregate校准与heldout/culture/fusion反侧揭示量表一致不授真实评价；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，328–347/368–389尺度、anchor/共偏与agreement边界 |
| [Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis](https://arxiv.org/html/2601.07974v1) | 2026-01-14 | prompt/model/domain分轴迁移及方向丢失/严格校正反侧限制detector解释；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，551–587/636–665人口与关联/holdout边界 |
| [TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL](https://arxiv.org/html/2601.08743v1) | 2026-01-14 | 显式relation决定offline联合编码边界而非线上补位置恢复因果；2+1+2=5 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，正文212，review_jan15_delta实际POST通过 |
| [Parallel Context-of-Experts Decoding for Retrieval Augmented Generation](https://arxiv.org/html/2601.08670v1) | 2026-01-14 | 独立KV保留N+1stream而在decode读出面汇合共享history；2+1+2=5 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，正文214，review_jan15_delta实际POST通过 |
| [Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention](https://arxiv.org/html/2601.08151v1) | 2026-01-14 | early-late attention差作晚层visual软mask proposal，不授fusion/因果完成；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，正文107，review_jan15_delta实际POST通过 |
| [Hierarchical Precision and Recursion for Accelerating Symmetric Linear Solves on MXUs](https://arxiv.org/html/2601.08082v1) | 2026-01-14 | 递归TRSM/SYRK混合precision与scaling的局部计算/数值取舍；2+1+2=5 | 标准完成 | 仅报告：局部solver计算核未验证同optimizer/foundation workload，不改变现有长期owner判断 |
| [Coordinated Cooling and Compute Management for AI Datacenters](https://arxiv.org/html/2601.08113v1) | 2026-01-14 | cooling慢actuator与TP/DVFS快执行协同但权限/费用独立；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，正文101，独立actual POST通过 |
| [Hierarchical Online-Scheduling for Energy-Efficient Split Inference with Progressive Transmission](https://arxiv.org/html/2601.08135v1) | 2026-01-14 | task reference到packet实际consume/deadline及渐进feature stop分工；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，正文496，独立actual POST通过 |
| [KidVis: Do Multimodal Large Language Models Possess the Visual Perceptual Capabilities of a 6-Year-Old?](https://arxiv.org/html/2601.08292v1) | 2026-01-14 | 构念/输出失配限制由task失败反推encoder或size机制；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，86–90 recover/access/express已有承载 |
| [UM-Text: A Unified Multimodal Model for Image Understanding](https://arxiv.org/html/2601.08321v1) | 2026-01-14 | 同ROI latent velocity与decoded RGB edge两consumer目标分账；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，正文81，独立actual POST通过 |
| [SnapGen++: Unleashing Diffusion Transformers for Efficient High-Fidelity Image Generation on Edge Devices](https://arxiv.org/html/2601.08303v1) | 2026-01-14 | 同xt fewstep teacher velocity/feature与realteacher/critic分布目标分责；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，正文700，独立actual POST通过 |
| [VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory](https://arxiv.org/html/2601.08665v1) | 2026-01-14 | think_on才reason/summary写memory，off仍当前visual+旧memory出action；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，正文520，独立actual POST通过 |
| [FSAG: Enhancing Human-to-Dexterous-Hand Finger-Specific Affordance Grounding via Diffusion Models](https://arxiv.org/html/2601.08246v1) | 2026-01-14 | SD multi-step feature提出finger contact，kinematic retarget/controller另验可达稳定；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，29–40 contact/retarget/control责任已有承载 |
| [Semantic Misalignment in Vision-Language Models under Perceptual Degradation](https://arxiv.org/html/2601.08355v1) | 2026-01-14 | corruption下输出/解析分歧限制pixel/语义/unsafe构念混合；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，104–119/208–225 taxonomy/scorer与分母分账已有承载 |
| [Representations of Text and Images Align From Layer One](https://arxiv.org/html/2601.08017v1) | 2026-01-14 | 逆优化prototype支持有限recoverability而非自然分布或native使用；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，87–94 recover/access/express与consumer分账 |
| [Sparsity Is Necessary: Polynomial-Time Stability for Agentic LLMs in Large Action Spaces](https://arxiv.org/html/2601.08271v1) | 2026-01-14 | sparse稳定性条件暴露population到empirical及dual feasibility缺口；2+1+2=5 | 争议 | 暂缓：中心必要证明未闭合，不采用Books；§4具体反侧/重开条件 |
| [Greedy Is Enough: Sparse Action Discovery in Agentic LLMs](https://arxiv.org/html/2601.08280v1) | 2026-01-14 | 条件greedy与exploration lowerbound分责，跨世界计数不能据单世界预算归并；2+1+2=5 | 争议 | 暂缓：中心下界争议，不采用Books；§4具体反侧/重开条件 |
| [Hyperbolic Heterogeneous Graph Transformer](https://arxiv.org/html/2601.08251v1) | 2026-01-14 | relation-specific曲率与线性attention局部表示/计算分支；1+1+2=4 | 已关闭 | 仅报告：成熟Hypformer算子借用不新增foundation系统长期知识链 |
| [CASHEW: Stabilizing Multimodal Reasoning via Iterative Trajectory Aggregation](https://arxiv.org/html/2601.08010v1) | 2026-01-14 | object-sensor核候选→subset synthesis产新trace→再次核验，区别原trace选择；2+1+2=5 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md)，正文394及末注，独立actual POST通过 |
| [Model-Agnostic Solutions for Deep Reinforcement Learning in Non-Ergodic Contexts](https://arxiv.org/html/2601.08726v1) | 2026-01-14 | horizon不改expected-wealth estimand的具体反例边界；2+1+2=5 | 争议 | 暂缓：Alg2固定f/iid回报仍端点最优，不采Books；§4定点反侧与重开条件 |
| [PersonaDual: Balancing Personalization and Objectivity via Adaptive Reasoning](https://arxiv.org/html/2601.08679v1) | 2026-01-14 | forced均衡mode探索与within/inter credit分工；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，正文110及自身末注actual POST通过 |
| [Prism: Towards Lowering User Cognitive Load in LLMs via Complex Intent Understanding](https://arxiv.org/html/2601.08653v1) | 2026-01-14 | CID prerequisite分层澄清与局部NLI/MC监督接口；1+1+2=4 | 已关闭 | 仅报告：成熟拓扑/训练的局部适配，不新增长期知识链 |
| [ExpSeek: Self-Triggered Experience Seeking for Web Agents](https://arxiv.org/html/2601.08605v1) | 2026-01-14 | step entropy分process/answer触发经验guide与reopen；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，231–247 bank事实/controller时机与费用退路 |
| [VideoHEDGE: Entropy-Based Hallucination Detection for Video-VLMs via Semantic Clustering and Spatiotemporal Perturbations](https://arxiv.org/html/2601.08557v1) | 2026-01-14 | 视频frame/pixel扰动预算适配已有entropy sensor；1+1+2=4 | 已关闭 | 仅报告：成熟HEDGE/SE/RadFlag/VASE适配，未新增长期metric机制 |
| [M3-BENCH: Process-Aware Evaluation of LLM Agents Social Behaviors in Mixed-Motive Games](https://arxiv.org/html/2601.08462v1) | 2026-01-14 | 行动/visible rationale/通信三view评价分责；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，208–225/269–282可观察证据与EvalIdentity |
| [Decoding Order Matters in Autoregressive Speech Synthesis](https://arxiv.org/html/2601.08450v1) | 2026-01-14 | duration segment选择与段内逐frame reveal两级接口；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，406及末注actual POST通过 |
| [YaPO: Learnable Sparse Activation Steering Vectors for Domain Adaptation](https://arxiv.org/html/2601.08441v1) | 2026-01-14 | 固定SAE latent干预与原activation残差保留分工；2+1+2=5 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md)，291及末注actual POST通过 |
| [RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation](https://arxiv.org/html/2601.08430v1) | 2026-01-14 | 高分reference对→新增微差rubric，局部缓解score饱和；1+1+2=4 | 已关闭 | 仅报告：prompt-level判据追加不改变长期foundation系统链 |
| [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/html/2601.08406v1) | 2026-01-14 | 外部click/type与人工semanticID评价真实effect，修正仅内部choice测量；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，95–119/208–225 target/system/scorer与真实effect分权 |
| [AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation](https://arxiv.org/html/2601.08323v1) | 2026-01-14 | CRUD序列与Read观察步学习proposal，terminal EM信用非事实commit；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，91–124/153–173 typedtransition、terminal proxy与local credit |
| [ToolACE-MCP: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/html/2601.08276v1) | 2026-01-14 | dependency-rich合成history产生routing监督接口；1+1+2=4 | 已关闭 | 仅报告：局部合成训练适配，成熟graph/DFS/LoRA不新增长期协议链 |
| [T3: Benchmarking Sycophancy and Skepticism in Causal Judgment](https://arxiv.org/html/2601.08258v1) | 2026-01-14 | valid/trap/不足信息与matched压力拆开accuracy及拒答；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，49–60/208–225条件风险、coverage与pairedpressure |
| [Owen-Shapley Policy Optimization (OSPO): A Principled RL Algorithm for Generative Search LLMs](https://arxiv.org/html/2601.08403v1) | 2026-01-14 | 有限连续输入subset的oracle marginal重分span/token proxy，区别候选集合credit；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，313及自身末注actual POST通过 |
| [ORBIT: On-policy Exploration-Exploitation for Controllable Multi-Budget Reasoning](https://arxiv.org/html/2601.08310v1) | 2026-01-14 | budget-specific teacher在mode条件student prefix上给监督，隔离teacher与采样人口；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，294及自身末注actual POST通过 |

新增补充日期采用正常announcement下界与正式ID/DOI已存在的上界共同限定到BJT Jan14自然日；不是把 Submitted、Updated 或 DataCite 注册单独当first-public。原52行及其原日期/评分不动；新增51家族均已逐篇必要审阅/Books处置，外部日期保留不进入确定候选，本轮六部分非作者日级验收已通过。[增量停点](../_sources/daily-20260115/supplement-20261007.md)。

## 4. 证据与知识整合

日期共同依据：精确DOI原返回保存于[NATIVE1](../_sources/daily-20260115/NATIVE1.jsonl)、[NATIVE2](../_sources/daily-20260115/NATIVE2.jsonl)、[DATE_AB1](../_sources/daily-20260115/DATE_AB1.jsonl)、[DATE_AB2](../_sources/daily-20260115/DATE_AB2.jsonl)、[08064恢复](../_sources/daily-20260115/DATE-08064-retry.jsonl)、[GAG字段](../_sources/daily-20260115/EARLY_REPO_GAG_DATE.jsonl)与[尾部5项原字段](../_sources/daily-20260115/DATE_TAIL5.jsonl)。保留dates中Submitted/Updated/Available、created、registered原值；Available只有月份时不补日时。[arXiv availability](https://info.arxiv.org/help/availability.html)规定ID随announcement、公告不能advance/backdate；当前52项实际Submitted-v1逐项在[Jan12T19Z,Jan13T19Z)正常cohort（最早07935 Jan12T19:04:58Z、最晚08829 Jan13T18:59:17Z），registered均Jan14T02:39:07～03:00:40Z，结合已存在DOI上界，条件区间为[Jan14T01Z,registered+1sec)，全部落窗。registered本身只是ID已存在的上界，不是first-public日志。

这是以本次arXiv公开论文事件为对象的条件归属，不证明互联网不存在早稿。Multiplex早repo/README已定点核：[first commits](../_sources/daily-20260115/MULTIPLEX_FIRST_COMMITS.json)/[first tree](../_sources/daily-20260115/MULTIPLEX_FIRST_TREE.json)是artifact时间线索；commit时刻非public push，概览非已取得的早公开完整论文。不把早artifact直接当论文first-public；若确实取得早公开PDF/完整正文才重开该归属。GAG早repo线索同样不将创建/提交时间等同公开正文。网页当前轻量版本/纠错说明已查看；later version不是当前v1机制证据，未默认遍历revision或附录。

以下小节均采用exact-v1，围绕拟采用命题读Method、关键对照与直接反侧，必要附录止于该命题；详笔记见[原证据笔记](../_sources/daily-20260115/EVIDENCE.md)。HTML抓取完整不是声称每一附录已读。原作者测量未复现；未列硬件/精度/完整训练或搜索预算、输入输出长度、concurrency、SLO、evaluator时为Not Disclosed或理论不适用，不据跨协议合并宣传数字。工程退路/验证要求是本报告推断，不冒称原实现。

### [Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge](https://arxiv.org/html/2601.08808v1)

必要位置：§3.1–3.3、§4–5/Tables1–4。tuple log-prob并非many-to-one投影density/entropy证明。Qwen1.5B/7B相同GRPO的数学任务比较仅支持局部接口；部分任务不胜soft-thinking。无匹配wall-clock/SLO，保留离散sampling。 具体缺口已写入MODEL-SAMPLING [Ch20](../../../../Books/part-02-model/20-sampling.md)的对应论证（当前正文L301，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Reducing Compute Waste in LLMs through Kernel-Level DVFS](https://arxiv.org/html/2601.08539v1)

必要位置：§4–9/Tables1–2。RTX3080Ti、GPT3xl/llm.c、seq1024/batch40的隔离profile；重测收益低于选中值，100cross-pairs不是100独立运行。§9切频延迟使逐kernel全部successively应用不可行；不是生产zero-loss。保留粗粒度clock并重测热/通信成本。 具体缺口已写入PLATFORM-COST [Ch70](../../../../Books/part-06-ai-infrastructure/70-cost.md)的对应论证（当前正文L330，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [MixServe: An Automatic Distributed Serving System for MoE Models with Hybrid Parallelism Based on Fused Communication Algorithm](https://arxiv.org/html/2601.08800v1)

必要位置：§III-A–D、IV-A–C。额外workspace与依赖完成进入计划。DeepSeekR1/Qwen3、H20与910B两类部署的最优DP/EP关系相反；后端/搜索集合不同，不能将headline视跨硬件因果。局部sync/async支持overlap；precision/实际输入输出切分/concurrency/SLO Not Disclosed。 具体缺口已写入INFER-TENSORRT-LLM [Ch49](../../../../Books/part-05-inference-system/49-tensorrt-llm.md)的对应论证（当前正文L213，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Modeling LLM Agent Reviewer Dynamics in Elo-Ranked Review System](https://arxiv.org/html/2601.08829v1)

必要位置：§3.5/4.1–4.3/Table1。Gemini2.5Flash、150篇/30轮，ACaccuracy上升但full-visibility recall/F1下降。visible通道与memory同时改变，非独立effort/因果测量。Ch66 feedback隔离与独立holdout已承载实际采用原则，不声称已有精确reviewer算法。 Books：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)已有覆盖，无新写。

### [Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling](https://arxiv.org/html/2601.08777v1)

必要位置：Property1、Props2–6、Theorems2–3。有限response与反对称/copy/subadditivity条件，k/(k+1)是偏好人口对单输出对手，非事实正确。NLHF可多样性坍缩；历史法先取一个iterate再取kcopies。Prop5fixedpoint不证LLM训练收敛；不授固定checkpoint的所有k保证。 具体缺口已写入TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md)的对应论证（当前正文L407，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs](https://arxiv.org/html/2601.08763v1)

必要位置：§3.2–3.4/Eq4–5、4.4/limitations。LLMjudge局部聚类，非全局novelty。8rollouts与大judge成本保留；20题coverage对照INSTRUCT非GRPO，不能隔离weight因果。HLE局部tie与未知seeds/hardware不支持普胜；旧GRPO退路。 具体缺口已写入TRAIN-GRPO [Ch33](../../../../Books/part-04-training-system/33-grpo.md)的对应论证（当前正文L197，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [PrivGemo: Privacy-Preserving Dual-Tower Graph Retrieval for Empowering LLM Reasoning with Memory Augmentation](https://arxiv.org/html/2601.08739v1)

必要位置：§4.1–4.3、Table4/AppC–D。HMAC别名不加密结构；node-count/utility不授重识别概率、DP或零泄漏。local32B非免费，多数published-baseline非同预算；Table4/prose call数冲突不采用。保留本地核验和旧privacy/fallback。 具体缺口已写入PLATFORM-SECURITY [Ch72](../../../../Books/part-06-ai-infrastructure/72-security.md)的对应论证（当前正文L317，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis](https://arxiv.org/html/2601.08699v1)

必要位置：§3.3–3.4/Eq8–9、4.3/Table2–3。教师不知fakeKB，fake后一步给clean。F1>.9不是路径证书；joint ablation同时移除curation/elicitation。fake shortcut18.5%/fallacy1.3%及额外teacher筛选成本保留，不授真实KB泛化。 具体缺口已写入TRAIN-DATA [Ch27](../../../../Books/part-04-training-system/27-data.md)的对应论证（当前正文L327，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Analyzing Bias in False Refusal Behavior of Large Language Models for Hate Speech Detoxification](https://arxiv.org/html/2601.08668v1)

必要位置：Table2、200分层标注、limitations。六语言非平行人口；Phi4judge的200人验50%来自flagged，非总体error率。Table2toxicity属于仍拒绝的原input非输出；cross-translation未证最终安全/保真，额外calls未完整披露。不采绕过做法，旧riskgate保留。 具体缺口已写入PLATFORM-SECURITY [Ch72](../../../../Books/part-06-ai-infrastructure/72-security.md)的对应论证（当前正文L1215，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [From Rubrics to Reliable Scores: Evidence-Grounded Text Evaluation with LLM Judges](https://arxiv.org/html/2601.08654v1)

必要位置：§3.1–3.3、4.6/limits。substring存在不授entailment，calibration在cap后不能授final-cap不变量。200dev/数据集校准、joint ablation与Compiler错误锁定、字符串误拒、分布漂移保留；既有评价退路。 具体缺口已写入PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)的对应论证（当前正文L3482，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs](https://arxiv.org/html/2601.08634v1)

必要位置：§2、4.5–4.6/limits。12模型、62forced-choice、七values条件；英文/观察人群与rationalejudge非内在因果。Ch66 PrincipalHierarchy、Bias及EvalSpec已具体承载role/scenario人口，仅采用这层。 Books：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)已有覆盖，无新写。

### [How Order-Sensitive Are LLMs? OrderProbe for Deterministic Structural Reconstruction](https://arxiv.org/html/2601.08626v1)

必要位置：§2.5–3、字符守恒/metrics、QwenVL CoT反侧。保留CJK四字符有限人口与模型时间；重复字符distinct分母只是工程要求非已核全数。CoT不普遍改善，不授唯一结构circuit。早期因未证架构因果而关闭的理由已纠正。 具体缺口已写入PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)的对应论证（当前正文L114，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Ministral 3](https://arxiv.org/html/2601.08584v1)

必要位置：§3.1/Algo1、5.1teacher对照。24→14→8→3，固定MS3 teacher不是child-teacher；final-long不成为下一child初始化。完整data/FLOP未匹配，stronger teacher反侧禁止总体compute优于one-shot或最大teacher必佳。 具体缺口已写入TRAIN-PRETRAINING [Ch28](../../../../Books/part-04-training-system/28-pretraining.md)的对应论证（当前正文L1082，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Your Group-Relative Advantage Is Biased](https://arxiv.org/html/2601.08521v1)

此前仅保存了准入理由和“原分数保留”的叙述，未找到数字评分；本次首次明确2+1+3=6，并由root独立确认，不称恢复原值。Design Delta 2对应条件人口/估计对象差额，System Reach 1仅局部训练objective，Durability 3对应长期数学边界。争议不降低评分，实际审阅已深入。

必要位置：Theorem1/2、AppD.1/Eq40–41。Eq40条件baseline可成立，但定理把随机r_i条件期望与随机r_i−p比较，exchangeability给E[r_i−R/G|S]=0；邻接方向文字也相反。局部HA-DW recipe实验/退步与8vs16采样成本不能挽救全定理；中心命题隔离，不进Books。 中心主张争议终态保留，不作为正面证据或Books；纠正其明确公式/条件才重开。

### [BenchOverflow: Measuring Overflow in Large Language Models via Plain-Text Prompts](https://arxiv.org/html/2601.08490v1)

必要位置：§4.1/Table3、§6。九策略×100prompts×4，openT1/closeddefault不matched。min(L,C)右删失是本报告测量推断非作者未截断tail证明。Gemini93.2→54.8与GPT5反向表明mitigation不无损；未测真实latency/crosstenantDoS/energy。 具体缺口已写入PLATFORM-COST [Ch70](../../../../Books/part-06-ai-infrastructure/70-cost.md)的对应论证（当前正文L119，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Surgical Refusal Ablation: Disentangling Safety from Intelligence via Concept-Guided Spectral Cleaning](https://arxiv.org/html/2601.08489v1)

必要位置：§3.3、5.1、§7。λ>0时Aᵀr̃=λŵ，不一定0；finiteatomspan即exactorthogonality也不保护nonlinear下游。teacher-forced PPL/首tokenKL非capability/safety，λ/config/编辑预算未完整披露。保留行为回归，不写绕过recipe。 具体缺口已写入WORLDVIEW-REPRESENTATION [Ch5](../../../../Books/part-01-worldview/05-what-neural-networks-learn.md)的对应论证（当前正文L424，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [JudgeRLVR: Judge First, Generate Second for Efficient Reasoning](https://arxiv.org/html/2601.08468v1)

必要位置：§3.2–3.3/4.1–4.5/Tables1–2。offline verdict匹配gold不是上线独立judge或局部critique真值。相等250steps非相等rollout/tokens/预处理；MATH50097.2<98、Mixed/JudgeOnly反侧及长输出局部保留。stylePPL/marker不证内部纠错。 具体缺口已写入TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md)的对应论证（当前正文L64，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management](https://arxiv.org/html/2601.08435v1)

必要位置：§2.2/3.1–3.2/Algo1、B.2Eq7–11、E.2/Table3。nonempty且complete mapping才守恒，守恒不授相同PG/causal credit。EARAalone .622<.627；20%QA、epochs/步数和单层memoryjoint改变，预算不匹配。选中evidence不是事实证书，manager/answerer成本保留。 具体缺口已写入AGENT-MEMORY [Ch77](../../../../Books/part-07-agent/77-memory.md)的对应论证（当前正文L163，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering](https://arxiv.org/html/2601.08427v1)

必要位置：§3–4/Eq2–4、Table4、§6/F2/limits。hidden一致可能系统同错/末token格式，groupminmax不是校准概率/梯度安全。小模型/任务有退步；2QPS为作者限流，不授普遍2x。IRCE/hidden存储成本非零，可靠outcome优先。 具体缺口已写入TRAIN-GRPO [Ch33](../../../../Books/part-04-training-system/33-grpo.md)的对应论证（当前正文L70，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Coverage Improvement and Fast Convergence of On-policy Preference Learning](https://arxiv.org/html/2601.08421v1)

必要位置：Assumptions2–4/Prop3.1/Th3.2/Algo2、Table1。bounded identifiable feature、exact BT oracle/realizability/local growth等才给条件上界，不授任意currentpolicy改善coverage。固定reference与Goptimaljoint design非任意replay；TLDR/GeneralChat退步与fresh label预算保留。lowerbound印刷/定义争议不采用，不global否定有效上界。 具体缺口已写入TRAIN-DPO [Ch34](../../../../Books/part-04-training-system/34-dpo.md)的对应论证（当前正文L263，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Controlled LLM Training on Spectral Sphere](https://arxiv.org/html/2601.08393v1)

必要位置：§3/Eq8–14、实现、Table4/B200反侧。一阶切向条件不证每一中间时刻严格有限步sphere；每步前retraction与更新后placement不同。tol/迭代成本明确；optimizedSSO比Muon慢11.45%、MuonSphere低cost退路，不授普遍稳定或无WD。 具体缺口已写入TRAIN-PRETRAINING [Ch28](../../../../Books/part-04-training-system/28-pretraining.md)的对应论证（当前正文L608，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Deconstructing Pre-training: Knowledge Attribution Analysis in MoE and Dense Models](https://arxiv.org/html/2601.08383v1)

必要位置：§method/model/Table4 mask、5layerstrength。OLMo7B32/2.5TDolma与MoE16/5TDCLM存在data/depth/compute混杂；same-modelmask支持所测relational人口，不支持MoE稳定架构因果。只报告此局部诊断，无长期owner新规则采用。 Books仅报告；保留准入增量和局部证据，不借用成熟通用原则升成新正文。

### [CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark](https://arxiv.org/html/2601.08331v1)

必要位置：§2/LFS-OR-HM、§5/limits。两8B、32language/70parallel题局部；FastText和Qwenjudge非truth。强early干预伤语义；same-benchmarkbest参数不独立heldout，late效应非唯一circuit。 具体缺口已写入PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)的对应论证（当前正文L112，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting](https://arxiv.org/html/2601.08316v1)

必要位置：§6–7、MLP3/5反侧。CIFAR30%noise、FC3/5/7长epoch局部；MLP5无DD仍分离、MLP3亦largeactivation，类均值与改变的correct子集无因果身份。关闭进一步采用，只报告现象，不借LLMmassiveactivation抬分。 Books仅报告；保留准入增量和局部证据，不借用成熟通用原则升成新正文。

### [Demystifying the Slash Pattern in Attention: The Role of RoPE](https://arxiv.org/html/2601.08297v1)

必要位置：§4.1/4.2/4.4 Eq9–10、§5.1assumptions。不是weight低rank；direction/norm/tokenpair近不变条件才简化Fourier。strength threshold改变的OOD不写sameκ或一般语义独立，训练理论受限；不采futurecompression/longcontext收益。 具体缺口已写入MODEL-POSITION-ENCODING [Ch13](../../../../Books/part-02-model/13-position-encoding.md)的对应论证（当前正文L161，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Discovery and Reinforcement of Tool-Integrated Reasoning Chains via Rollout Trees](https://arxiv.org/html/2601.08274v1)

必要位置：§2.1–2.2/Eq1–7、§5.2–5.4、A3/A4。hint改变采样条件且末20%excluded；leafmean/local不授tool因果真值或iidGRPO，15估计8train代价不match。GPQA局部退步，零KL/max16384等局部设置；不采用Eq7完整梯度实现，旧outcome退路。 具体缺口已写入TRAIN-GRPO [Ch33](../../../../Books/part-04-training-system/33-grpo.md)的对应论证（当前正文L213，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [MPCI-Bench: A Benchmark for Multimodal Pairwise Contextual Integrity Evaluation of Language Model Agents](https://arxiv.org/html/2601.08235v1)

必要位置：§3–5/Trace、Tables3–5/limits。recipient/purpose/transmission改变情境；normativeprobe不是真attachmentgate。synthetic generatorjudge共源、50human与文化限制，Eq1分母/率冲突精确数不采，CIprompt非production保证。 具体缺口已写入PLATFORM-SECURITY [Ch72](../../../../Books/part-06-ai-infrastructure/72-security.md)的对应论证（当前正文L52，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints](https://arxiv.org/html/2601.08215v1)

必要位置：§1–3/Eq1–5/Tables1–3。FineWebEdu/Qwenstyle30M–3B有限token预算拟合非hardwareSLO/普遍最优。Ch21 229–251已具体承载expert数、corewidth/depth与dispatch/fanout；不采exact exponent，无新写。 Books：MODEL-MOE [Ch21](../../../../Books/part-02-model/21-moe.md)已有覆盖，无新写。

### [Generation-Augmented Generation: A Plug-and-Play Framework for Private Knowledge Injection in Large Language Models](https://arxiv.org/html/2601.08209v1)

必要位置：§4.1–4.3/Eq5–14、Tables3–4/§9。late L₂−4，不是早层；onebasetoken不免expert AR。oracle-routing消融只局部知识接口；generalpeer argmax非OODabstention，新prototype可改旧route。单域/数值单位丢失与8A100/BF16总成本限制，不采用science领域优势。 具体缺口已写入MODEL-EMBEDDING [Ch12](../../../../Books/part-02-model/12-embedding.md)的对应论证（当前正文L128，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Triplets Better Than Pairs: Towards Stable and Effective Self-Play Fine-Tuning for LLMs](https://arxiv.org/html/2601.08198v1)

必要位置：Eq4–6、Table1、β=0对照。Proto缓存lineage+每轮重生成成本、固定gold drift与局部退步保留。闭式在指定函数类/优化条件，不授LLM全局最优/永不vanish；不是实时reference。 具体缺口已写入TRAIN-DPO [Ch34](../../../../Books/part-04-training-system/34-dpo.md)的对应论证（当前正文L435，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Evaluating Implicit Regulatory Compliance in LLM Tool Invocation via Logic-Guided Synthesis](https://arxiv.org/html/2601.08196v1)

必要位置：§3.2–3.4/4.2、limits。schema签名不授NL等价/法律真值；terminal state不是whole trace。两模板/240synthetic任务/作者review不证一般未来LTL可解，arguments/dataflow未覆盖，domain数字冲突不采。 具体缺口已写入PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)的对应论证（当前正文L163，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Relational Knowledge Distillation Using Fine-tuned Function Vectors](https://arxiv.org/html/2601.08169v1)

必要位置：§3Eq1–3、4.3/limits。冻结base但FV/combiner训练；118basis每sourcepair forwards/2430analogies非Bayesianposterior。四term及FFV OOD不等pretrainingunknown，near无显著优点；小testpairs/版本成本与prompt/PEFT退路。 具体缺口已写入WORLDVIEW-REPRESENTATION [Ch5](../../../../Books/part-01-worldview/05-what-neural-networks-learn.md)的对应论证（当前正文L308，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents](https://arxiv.org/html/2601.08158v1)

必要位置：§3.2–3.3/5.3–5.4/limits/LOTO。lastsuccesscall定位，LLM prerequisite非真实环境真值。ToolSandbox/tau2模拟，LOTO退步、缺日志/反复action/spuriousprereq；Cohere/FAISS/LLMcalls成本非免费，goalqueue与authority保留。 具体缺口已写入AGENT-WORKFLOW [Ch81](../../../../Books/part-07-agent/81-workflow.md)的对应论证（当前正文L118，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Attention Projection Mixing with Exogenous Anchors](https://arxiv.org/html/2601.08131v1)

必要位置：Eq7–10、4.1/Table1/offloading。anchor normalize→mix→QKNorm/RoPE/gate有次序；四projection额外capacity。约450M/10Btokens/H100/BF16/seq2048局部，longctx未测，offloading是假说非causal保证；普通residual退路。 具体缺口已写入MODEL-TRANSFORMER-LAYER [Ch17](../../../../Books/part-02-model/17-transformer-layer.md)的对应论证（当前正文L66，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Debiasing Large Language Models via Adaptive Causal Prompting with Sketch-of-Thought](https://arxiv.org/html/2601.08108v1)

必要位置：mainEq1–2、AppB推导、D/E。删P(q|e)但保留∑q，使主式一般不再归一，固定query不修复调整分布；directQ→A/截断条件未证。cluster-weightedSC和demo的局部实验/成本不挽救中心识别；作者更正前不进Books。 中心主张争议终态保留，不作为正面证据或Books；纠正其明确公式/条件才重开。

### [STO-RL: Offline RL under Sparse Rewards via LLM-Guided Subgoal Temporal Order](https://arxiv.org/html/2601.08107v1)

必要位置：§3/Eq1–theorems、实验/noise/limits。φ_t=−t/(Tk_t)；Th1严格order/非terminal原reward0，Th2需γ>(T−1)/T，γ.99边界不严格；terminalφ非0不授最优policy不变。grid/IQL/1kupdates有限，小maze输GCBC/最终趋同，100trials非100trainseed。仅报告局部shaping，无新的普遍PBRS保证。 Books仅报告；保留准入增量和局部证据，不借用成熟通用原则升成新正文。

### [AdaJudge: Adaptive Multi-Perspective Judging for Reward Modeling](https://arxiv.org/html/2601.08097v1)

必要位置：§3.1–3.4/Eq1–6、4.1–4.4/Table1–3/limits。router消费末response、meanresponse、attention+prompt三视图，不是单prompt。≤8B局部，component切片退步/同预算latency未匹配，不授整体省或下游policy收益；旧pooling/BT保留。 具体缺口已写入TRAIN-RLHF [Ch31](../../../../Books/part-04-training-system/31-rlhf.md)的对应论证（当前正文L101，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Q-realign: Piggybacking Realignment on Quantization for Safe and Efficient LLM Deployment](https://arxiv.org/html/2601.08089v1)

必要位置：§3.1–3.2/Eq3–5、AppD/E/limits。alignedSLR几何不等行为因果；W4A4与100%单类低harmful但incoherent，sameformat重构control才可比。限LoRA/3runs/A6000，calibration及behavior回归成本不免；不授kernel吞吐/普遍恢复。 具体缺口已写入INFER-TENSORRT-LLM [Ch49](../../../../Books/part-05-inference-system/49-tensorrt-llm.md)的对应论证（当前正文L885，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [MemoBrain: Executive Memory as an Agentic Brain for Reasoning](https://arxiv.org/html/2601.08079v1)

必要位置：§3.2–3.3/Eq4–10、4.3–4.4/limits。同已解决子问题才Fold，Flush留结构history不等删除；copilot图非因果/摘要非truth。小预算退步、未训大copilot/工具call增加、管理latency和早停反侧；保留简单window/原轨迹。 具体缺口已写入AGENT-MEMORY [Ch77](../../../../Books/part-07-agent/77-memory.md)的对应论证（当前正文L396，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Semantic Gravity Wells: Why Negative Constraints Backfire](https://arxiv.org/html/2601.08070v1)

必要位置：§method/pressure、full-residual patch、limits。Qwen2.5-7B/2500oneword局部，pressure相关和full-residual patch不是FFN独占/唯一circuit。40k/2500与例∆P数字冲突不采；alternative future未测。仅报告局部negative-constraint failure，不采用中心模块因果。 Books仅报告；保留准入增量和局部证据，不借用成熟通用原则升成新正文。

### [Universal computation is intrinsic to language model decoding](https://arxiv.org/html/2601.08061v1)

必要位置：§5–6/Theorem1/Cor3、MethodsE。精确1857rulecodebook+外部可增长串并非任意naturalprompt；randomnet冻结不免encoderdecoder训练。30init实验不授任意随机网络/效率，规则校验/外部增长成本保留，固定接口上界不被反驳。 具体缺口已写入MODEL-DECODER-ONLY [Ch18](../../../../Books/part-02-model/18-decoder-only.md)的对应论证（当前正文L350，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Triggering Chain-of-Thought via Latent Feature Interventions in Large Language Models](https://arxiv.org/html/2601.08058v1)

必要位置：§3.4/Eq10–13、Table1/limits。训练侧feature选择后heldout，decoded difference加residual不是全重构。输出增长、SAE/选择成本、random10runs vsselectedseed与GPQA/CoT退步；不授内部concept真值，不写绕过recipe。 具体缺口已写入WORLDVIEW-REPRESENTATION [Ch5](../../../../Books/part-01-worldview/05-what-neural-networks-learn.md)的对应论证（当前正文L445，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [DYCP: Dynamic Context Pruning for Long-Form Dialogue with LLMs](https://arxiv.org/html/2601.07994v1)

必要位置：§4/Algo1、6.1/GPT4.1、Discussion。append-beforetest不授所有span≥threshold，zeroσ/exhaustion需实现check。embedding/index非免费，GPT4.1 fullhistory可相当、漏检存在；三小dialogbench不能授超长能力/强causal，完整history退路。 具体缺口已写入AGENT-CONTEXT [Ch75](../../../../Books/part-07-agent/75-context.md)的对应论证（当前正文L96，source-family标记定位），并保留前后交接；root实际源→owner及正文/邻接写后通过。

### [Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs](https://arxiv.org/html/2601.07972v1)

必要位置：§3–5/数据、人标及limits。3000Reddit synthetic/20actions与47UShumans，50专家题、10维aggregate r非文化不变量或内部动机因果。语言人口/contamination/conditional subset有限；只报告具体测量协议，现泛边界不足强称exact Existing，不新增正文凑覆盖。 Books仅报告；保留准入增量和局部证据，不借用成熟通用原则升成新正文。

### [Calibration Is Not Enough: Evaluating Confidence Estimation Under Language Variations](https://arxiv.org/html/2601.08064v1)

必要位置：§3–5/Eq5/eligibility与limits。Eq5绝对difference不区分between>within；不同meaning可同为正确/同confidence，不自行修公式。GPT4ojudge/英文四QA/greedy/maxmincluster选择限制人口；仅报告局部blindspot，中心A-SST sensitivity不采用。 Books仅报告；保留准入增量和局部证据，不借用成熟通用原则升成新正文。

### [MirrorBench: An Extensible Framework to Evaluate User-Proxy Agents for Human-Likeness](https://arxiv.org/html/2601.08118v1)

exact-v1 §4/Eq1–8与§6/Limitations：词汇多样性、judge realism与固定assistant的task outcome不是同一对象；judge替换会改变水平/排序。HH/PP自比较同近.5的Eq8分母不稳定，校正分数不采用为人类不可区分或稳定校准证书。795对话/四英语数据/单seed、100条单proxy人工核与judge成本限制局部范围。具体缺口是Ch66已有persona/合作性覆盖尚未分开三种验证对象及judge自身控制，root必要源→owner通过，新增UserSimulator两段 [Ch66:1126](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md:1126)，root实际正文/前后邻接及末注POST通过。日期原字段见[DATE_TAIL5](../_sources/daily-20260115/DATE_TAIL5.jsonl)，原段见[CORE_TAIL-08118](../_sources/daily-20260115/CORE_TAIL-08118.jsonl)和[必要补段](../_sources/daily-20260115/NECESSARY_TAIL-08118.md)。

### [TP-Blend: Textual-Prompt Attention Pairing for Precise Object-Style Blending in Diffusion Models](https://arxiv.org/html/2601.08011v1)

exact-v1 §3.3/Eq5–15、§3.4/Eq16–19与§4.1/4.3：head-average分别选source/destination positions，迁移的是完整head输出features而非只换attention weights；局部统计/残差及style-KV是另一控制接口。两集合不必互斥，替换KV后先前调制仍可经Query/hidden route影响。原运输边际总质量与Sinkhorn更新不相容、σ频率解释不一致，相关exact solver/几何保证不采用。SDXL有限组合、CLIP/LPIPS代理、threshold/strength与NoneOT反侧不授语义保真；多stream/矩阵成本及完整latency/memory预算Not Disclosed。Ch24已有reference注入cap缺位置迁移/风格接口分工，root必要源→owner通过，新增 [Ch24:147](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:147)两段；root实际正文/前后邻接及末注POST通过。日期见[DATE_TAIL5](../_sources/daily-20260115/DATE_TAIL5.jsonl)，原段见[CORE_TAIL-08011](../_sources/daily-20260115/CORE_TAIL-08011.jsonl)和[必要补段](../_sources/daily-20260115/NECESSARY_TAIL-08011.md)。

### [LLM Review: Enhancing Creative Writing via Blind Peer Review Feedback](https://arxiv.org/html/2601.08003v1)

exact-v1 §3.5及§5.1–5.3/Limitations：peer可见同题初稿与反馈、独立修订不共享别人的revised drafts，不是完全盲评；这是feedback与artifact visibility的具体分层，不是通用多Agent数量原则。100短SciFi题/3personas/3rounds及9学生人工仅局部，GPT4o写作/judge同源；多人数/轮数可退步，单Agent总调用不匹配，noveltyproxy不等语义质量或正确。Ch82已有consensus/aggregation未承载修订可见性边界，root必要源→owner通过，新增 [Ch82:158](../../../../Books/part-07-agent/82-multi-agent.md:158)两段，root实际正文/前后邻接及末注POST通过。日期见[DATE_TAIL5](../_sources/daily-20260115/DATE_TAIL5.jsonl)，原段见[CORE_TAIL-08003](../_sources/daily-20260115/CORE_TAIL-08003.jsonl)。

### [Reasoning over Precedents Alongside Statutes: Case-Augmented Deliberative Alignment for LLM Safety](https://arxiv.org/html/2601.08000v1)

exact-v1 §2.3、§3.1–3.4及§4.1/关键反侧：完整显式code在局部推理对照损伤安全/helpfulness，case reasoning+短code是待验证替代；unsafe-only500请求训练的拒绝outcome和非空reasoning/格式reward分开，后者不认证推理质量，KL也不认证benign效用。两个8B/三runs/固定A100预算、最终回答judge与harmful/benign分母、MMLU及benign局部退步限制采用；不授未知攻击/内部reasoning因果，不提供绕过recipe。Ch31 safety/helpfulness原bullet缺监督呈现与reward对象的具体差额，root必要源→owner通过，新增 [Ch31:154](../../../../Books/part-04-training-system/31-rlhf.md:154)两段，root实际正文/前后邻接及末注POST通过。日期见[DATE_TAIL5](../_sources/daily-20260115/DATE_TAIL5.jsonl)，原段见[CORE_TAIL-08000](../_sources/daily-20260115/CORE_TAIL-08000.jsonl)。

### [Cost and accuracy of long-term graph memory in distributed LLM-based multi-agent systems](https://arxiv.org/html/2601.07978v1)

root实际核§2–4/Tables1–6后通过标准审阅/仅报告：单一LoCoMo对话19sessions/199QA、固定coordinator/reader和200ms/8Mbit/s/50msjitter的成本与准确率观测支持局部反证，不改变一般graph/flat选择法则。p>.05不表示等效或非劣；作者strict dominance/Pareto中心子命题隔离，配对题目/会话cluster未控制，不能由不拒绝零假设授相同准确率。Table1 token/USD不一致与声称gpt4omini8B不采用，未匹配schema/extractor或完整生命周期重复预算。成熟统计原则不冒称新Books机制，无新书稿。日期原字段见DATE_TAIL5，正常cohort区间落窗。原段见[CORE_TAIL-07978](../_sources/daily-20260115/CORE_TAIL-07978.jsonl)。

### [Towards Specialized Generalists: A Multi-Task MoE-LoRA Framework for Domain-Specific LLM Adaptation](https://arxiv.org/html/2601.07935v1)

exact-v1 §2/3.1–3.6与4.2.3/Table3：原文明确综合既有top-heavy/rank异构/soft-routing，但新局部bottom-heavy退步验证仍保留，不因medical场景排除。其top/bottom/uniform配置未证明等容量、rank与其他组件全匹配，不能因局部结果授高层语义因果。Eq1/3 all-N soft mixture与Table4 sparse-active参数叙述不一致，不采用省算执行保证；anchor初始化也不授梯度隔离。2+1+2=5仅报告由root实际必要源独立通过，无新Books。 日期原字段见[DATE_DECIDING3](../_sources/daily-20260115/DATE_DECIDING3.jsonl)，原段见[CORE_TAIL-07935](../_sources/daily-20260115/CORE_TAIL-07935.jsonl)。

### [Embedded AI Companion System on Edge Devices](https://arxiv.org/html/2601.08128v1)

exact-v1 §3–4.3、§5Tables1–4、§6–7/C.1：同JetsonOrinNanoSuper8GB/Qwen2.5-7Bint4模型的active仅retrieve+appendraw，静默阈值触发inactive分块extract/merge/update，是维护时序而非事实authority改变。未证明维护在用户返回前结束/可抢占/一致读写；raw30k基线在A100，inferred QA反侧、合成5用户/100k及judge、缺multihop、不同commit/动态prefix缓存保留。Ch77 consolidation/forgetting未承载session静默分工，root必要源→owner通过，新增 [Ch77:400](../../../../Books/part-07-agent/77-memory.md:400)两段；stale/抢占/读写仅工程验收推导，root实际正文/前后邻接及末注POST通过。日期原字段见[DATE_DECIDING3](../_sources/daily-20260115/DATE_DECIDING3.jsonl)，原段见[CORE_TAIL-08128](../_sources/daily-20260115/CORE_TAIL-08128.jsonl)与[必要补段](../_sources/daily-20260115/NECESSARY_TAIL-08128.md)。

### [When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges](https://arxiv.org/html/2601.08343v1)

新增补充 exact-v1 §3–6/Table1–2、§7与Limitations：N4固定候选文本与顺序，execution侧dense，仅改变judge状态。RoPE重定位/stitch及anchor修正仍可能改变selected candidate identity，即使某设置最终答案质量近似不变。Dense只是配对行为参照不是gold，JCR不等正确率/公平；attention诊断与mask干预不证明唯一因果。Llama3.2-3B主实验与3–14B消融、execution温度.2/judge0，复用比例排除prefix/output，不授全链速度；hardware/precision/batch/concurrency/SLO Not Disclosed。直接匿名代码入口当前为空，不影响论文可支持的局部反证，不声称实现核验/复现。

actual INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 原dependency identity/conditioning seam/role-flip对照未明确保存联合judge的selection/attribution验收对象，已在role-flip后窄补该差额：固定candidate/permutation与matched dense分账，修复后无法验明合同则完整prefill。root独立必要原证/actual owner PRE通过，实际正文979、完整967–991邻接及末注POST通过，窄锁释放；不推翻exact prefix reuse，不授heterogeneous或生产SLO。[必要证据与具体owner](../_sources/daily-20260115/increment-pre-first3-20261007.md)。

### [Training-Free Distribution Adaptation for Diffusion Models via Maximum Mean Discrepancy Guidance](https://arxiv.org/html/2601.08379v1)

新增 exact-v1 §4 Eq5–8/Alg1、§5 product kernel Eq10–11、§6 Tables1–4/§7：empirical MMD在reverse sampling叠加生成batch内repulsion与finite-reference attraction，prompt×latent kernel不是classifier surrogate。iid reference及有界平滑条件的cross-term集中界不证明有限solver或decoder最终law，稀疏reference/kernel失配反侧保留。局部图像FD/KD/coverage及五seed不是语义真值；4090/50step增加kernel/reference费用，precision/batch/concurrency/SLO Not Disclosed，training-free非免费。[必要原证/actual owner](../_sources/daily-20260115/increment-pre-four-20261007.md)。实际 [Ch24:248](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 补有限人口guidance接口，root实际240–259连续邻接及末注POST通过，不替代CFG或签发分布一致性证书。

### [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://arxiv.org/html/2601.08325v1)

新增 exact-v1 §3.1–3.3、§4 Tables1–4、真实Table5及Appendix3：粗投影heatmap→3D ROI→virtual view/FoV重渲染→action定位；同一已观察RGBD pointcloud无法提供未观测背面信息。RLBench同组件view/zoom由87.6/.26s至91.8/.53s支持局部取舍；过多view增费、过zoom损context，GemBenchL4仅1.2/真实四任务不授开放物理安全。SigLIP/tokenembedding冻结不是整个VLM冻结，训练预算分别记录；precision/controlfrequency/fullSLO/realtrialcount Not Disclosed。[必要原证/actual owner](../_sources/daily-20260115/increment-pre-four-20261007.md)。实际 [Ch26:71](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 区分表示预算与真实取证，root实际65–84连续邻接及末注POST通过。

### [Reliable Graph-RAG for Codebases: AST-Derived Graphs vs LLM-Extracted Knowledge Graphs](https://arxiv.org/html/2601.08773v1)

新增 exact-v1 §5–6/Alg1、§7–11/14：Java三repo/45题的局部对照中，截断、class-map/schema失败前置embedding可缩vector corpus并混杂较低建库费用；377skip不是单一LLM因果，节点/边数不自证完整，AST不包含reflection/dynamic生成/dispatch全部语义。ThingsBoard向量与DKB同14/15，human coarse labels缺inter-rater/重复次数，hardware/precision/concurrency/SLO Not Disclosed。原项目exactSHA42paths包含code/log/JSON/PNG而无MD/PDF/tex完整本稿信号，早artifact不改本次arXiv事件限定日期。[必要原证/actual owner](../_sources/daily-20260115/increment-pre-four-20261007.md)。实际 [Ch76:63](../../../../books/part-07-agent/76-rag.md) 保存独立source manifest并分账抽取/embedding/graph权限与费用，root实际57–78连续邻接及末注POST通过。

### [HIPPO: Accelerating Video Large Language Models Inference via Holistic-aware Parallel Speculative Decoding](https://arxiv.org/html/2601.08273v1)

新增 exact-v1 §3.2/4/5.1–5.2/§6–8及AppendixB/C/D：target attention、adjacent-frame cosine与crop variance按frame归一后保10%视觉token，上轮全accept才optimistic overlap；不授heuristic语义保真，cancel隐藏critical-path不等算力/争用免费。4H200140GB/batch1/greedy256outputs、7B draft与32/72B target四GPU，LLaVA64/128frames，precision/concurrency/SLO Not Disclosed。10VideoMME的164.84→58.82s含相同targetprefill33.71s；质量未实测，非高batch吞吐/生产SLO或代码复现。成熟PEARL并行原则不计新增分。[必要原证/actual owner](../_sources/daily-20260115/increment-pre-four-20261007.md)。[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 的204、743–745、955–963已承载target authority、prefix/version cancel/费用及视觉budget；root实际Existing通过，无书稿写入。

### [Lessons from the Field: An Adaptable Lifecycle Approach to Applied Dialogue Summarization](https://arxiv.org/html/2601.08682v1)

新增exact-v1 §3/§4/Table1–2/§5/Table3–4及Limitations：内部100 transcripts固定core prompt，仅special tokens改配Llama3.3-70B→gpt-oss120B，accuracy/readability/completeness取舍发生改变。AutoEval Claude3.7的三次重复不是全部生成seed；42人工/合成pair与4×50人审只验证内部构念。50component labels、ASR局部WER/下游偏好观察不证明一般prompt不可迁移或单一ASR因果；hardware/precision/batch/concurrency/SLO Not Disclosed，未复现。日期原字段与直接原件见[必要证据](../_sources/daily-20260115/increment-pre-next3-20261007.md)。实际AGENT-PROMPT [Ch74](../../../../books/part-07-agent/74-prompt.md) 16–29的model/tokenizer/template/context/decoding依赖与102–126的prompt版本/cohort/regression/canary/rollback已承载该条件，root必要原证及完整对应邻接Existing通过，无书稿写入。

### [MemRec: Collaborative Memory-Augmented Agentic Recommender System](https://arxiv.org/html/2601.08816v1)

新增exact-v1 §2.1/Eq5–6、§3.1–3.5、A.3/A.5/C/D.3：curated immediate-neighbor memories批量更新，独立memory LM异步供reader；O(1)仅调用数，不授tokens/write/freshness/隐私。四推荐split与1000user子研究中，关闭write使H@1 .527→.505却H@5 .803→.814，不授所有K更强。D.3的R3200/ReRank2000/W4500=9700 tokens确计写入；Standard16.5s/Ceiling10.4s/LocalQwen34s来自不同配置，黑箱cloud routing/network混杂，非匹配本征速度。Local仅memory LM A5000 24GB/vLLM FP16/temp0，reader仍云4o-mini；主实验hardware/precision/batch/concurrency/SLO Not Disclosed，queue/stale/commit未验证。价格仅Dec2025估计，未复现。见[必要原证](../_sources/daily-20260115/increment-pre-next3-20261007.md)。actual [Ch77](../../../../books/part-07-agent/77-memory.md) 363–427的entity/邻域作用域、provenance、consolidation/crossrecord merge、异步管理/stale退路及全生命周期成本已承载本次采用命题，root必要原证/具体Existing通过，无写入。

### [Learning from Demonstrations via Capability-Aware Goal Sampling](https://arxiv.org/html/2601.08731v1)

新增exact-v1 §3.1–3.3/Alg1–2/Theorem1、§4及F.4/G：L2/imageMSE访问计数提出demo附近goal，Go尝试到达或timeout后BCExplore真实采集，replay训练Dreamer/RSSM，再imagined训练goal policy。访问阈值/最终成功不证明BC occupancy κ、model μ及imagined轨迹ν三条件；只允许demo初态reset。11模拟任务10/20demos、8训练seeds/100held-out初态，有限质量扰动5seed；失败demo仍带成功标签并只以成功示教训练goal predictor，不采“无imitate”。72–155h/1M–5Msteps、8A100披露与逐step×demo长度匹配费不授matched墙钟改善，precision/batch/concurrency/SLO Not Disclosed，未复现。见[必要原证](../_sources/daily-20260115/increment-pre-next3-20261007.md)。actual [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 104–106补真实采集支持域分工与proxy/费用/普通replay回退，root完整邻接/自身末注POST通过，窄锁释放，不签发TV或部署shield。

### [RAVEN: Erasing Invisible Watermarks via Novel View Synthesis](https://arxiv.org/html/2601.08832v1)

新增exact-v1 §3–5/Table2–5/§9：仅带水印输出+公开img2img、无key/detector查询/weights，生成重构可损检测而CLIP/FID等内容proxy近似；proxy不是严格语义/来源或ownership。SD2.1 512²/三backbone、1000pairs TPR@1%FPR与bit accuracy协议分开，COCO meanTPR .026 vsUnMarker .078仅局部；method14/abstract15/table16数量冲突不报统一规模。strength增大损FID、attention/颜色消融不授唯一几何因果。单A10040GB/固定seed/~6s每图，precision/batch/concurrency/SLO Not Disclosed，zero-shot非免费，代码未来未核实现/复现。见[必要原证/owner](../_sources/daily-20260115/increment-pre-bench4-20261007.md)。actual [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 191补regeneration transformation class下持久性/内容分责，artifact/detector记录与signed provenance回退明确工程推断；root实际185–201完整邻接/自身末注POST通过，锁释放，不授所有水印必失效。

### [Semantic Laundering in AI Agent Architectures: Why Tool Boundaries Do Not Confer Epistemic Warrant](https://arxiv.org/html/2601.08333v1)

新增exact-v1 §3.1–3.5/§4.1：Theorem1三前提为同命题类型P、tool output当observation、LLM proposition可影响status；proof sketch额外选LLM expert及同epistemic process，未排除独立OBSERVER或有效外部推理。作者声称这些前提使循环许可必然且更强judge不能消除，但前提只允许影响，不强制缺外部依据或形成循环；本文§3.5另明示OBSERVER/COMPUTATION/GENERATOR分工。这是中心证明争议，不把一般‘transport不自动增warrant’推成所有tool/judge无效，不因是position paper/无实验自动排除。理论workload/硬件/seed/SLO不适用；未核框架实现，没有实证发生率。必要原文及双方判断见[core](../_sources/daily-20260115/increment-j15theory-core-20261007.txt)/[tail](../_sources/daily-20260115/increment-j15theory-tail-20261007.txt)，root确认保留中心争议信号。不得用于正面定理/安全证据或Books；补足‘确无独立依据/有效推理且循环可达’等必要条件或更正证明后，只重开§3.4及依赖结论，不索取所有框架史。

### [SafeRedir: Prompt Embedding Redirection for Robust Unlearning in Image Generation Models](https://arxiv.org/html/2601.08623v1)

新增exact-v1 §IV-B/C/TablesIII–IV、D-C/Alg2、E-A及§V：text/latent/timestep风险头提出token embedding redirection，内部conditioning hook/cooldown消费，不是对任意黑箱API的无内钩方法或参数知识删除。辅助120k数据来自300标准/300adversarial prompts×2seed×50steps的随机80/20，不授prompt-family heldout或校准；FSR由NudeNet/EraX_NSFW/MultiClf等局部detector判未检出，不是真实安全。alpha提高风险抑制却损FID，mask与未mask存在取舍；I2P .70/MMA1.73不覆盖全部强基线，active NSFW9.38/style50.16残留保留。8A100 server/50MB/<1.5%局部overhead不是完整生产SLO，precision/batch/concurrency Not Disclosed；SD1.4→1.5同encoder迁移不授所有encoder零样本，v2需调整/重采训练。必要源及actual owner见[PRE](../_sources/daily-20260115/increment-pre-bench4-20261007.md)。actual [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 380新增sampling suppression与风险/hook资格分工，冻结base仍需辅助训练；root实际376–386完整邻接/自身note4333 POST通过，锁释放。未核实现或复现。

### [ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation in Complex Real-World Scenarios](https://arxiv.org/html/2601.08620v1)

只采用本次正式稿§4.2/4.3新增evaluation，不重计Nov5,2025已发布dataset/annotation/retrieval；可变blog顶部告示不用于确定稿日期，本次普通announcement/正式ID界限复用且保留早稿重开条件。固定image hard panel为六model至少一个失败的选择条件，不授自然难度或记忆证书；hybrid generation是top5 visual+5text不去重，retrieval hybrid才去重/用unranked F1，收益与context预算混杂。best-over-annotator bbox F1 .089/.065 vs人.602不代表内部attention因果；五judge重复为一致性非真值，两domain五E2E runs不外推全域。12k人标时/3000 H100h及precision/batch/concurrency/SLO Not Disclosed，未复现。root实际必要原证及actual [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1065–1100完整邻接确认pipeline/阶段receipt、oracle非生产、answer≠evidence已有覆盖，无Books diff。[必要证据](../_sources/daily-20260115/increment-pre-bench4-20261007.md)。

### [VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking](https://arxiv.org/html/2601.08611v1)

exact-v1§3.1–3.6/§4.1–4.4/AppG：四judge ensemble/gold-conditioned rectification及季度平衡改变选择分布，agreement不授全库真值；Integrity min仅含contextualization/veracity/contextcoverage而非authenticity，早停空白是未测非独立低分。63 retained human claims需≥2native/C1且同fact-check article/过滤分歧，96.8%仅该样本；Gemini native-video vs其余fiveframes不matched，search时间/domain过滤非无泄漏，post-KCD变化不识别唯一记忆原因。$14.9k/$600季度为估计，2700 GPUh/8H100标注非训练，precision/batch/concurrency/SLO Not Disclosed；2028季度承诺不是已执行。root实际必要原证及actual [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 标签/provenance/refresh正文确认具体Existing，min规则保报告case不升新长期机制，无Books diff。[必要证据](../_sources/daily-20260115/increment-pre-bench4-20261007.md)。

### [TabPFN Through The Looking Glass: An interpretability study of TabPFN and its internal representations](https://arxiv.org/html/2601.08181v1)

exact-v1§3.1–3.5/§4：独立context系数probe低train accuracy，合并关系加switch后较可读（probe不消费switch），作者承认可能context特有signature。中层a·b/answer可预测不证明内部算法或后层可删；复杂MLP probe退不授线性唯一性，公式重复x未采用recipe。Toy additive/multiplicative、无activation patching，sample/seed/probe协议及hardware/precision/batch/concurrency/SLO Not Disclosed。root实际必要source及actual [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 2206–2229的probe≠causal/干预权与3049–3063识别/无法识别时降级已有覆盖通过，无Books diff；正常公告/正式ID日期条件与原项轻量无早正文信号复用，不授互联网上没有早稿。[必要证据](../_sources/daily-20260115/increment-pre-language3-20261007.md)。

### [Mechanisms are Transferable: Data-Efficient Low-Resource Adaptation via Circuit-Targeted Supervised Fine-Tuning](https://arxiv.org/html/2601.08146v1)

exact-v1§3–6、C、D.1–3：label-balanced mean/task projection选head，grad mask还更新LayerNorm，其余参数冻不是完整forward剪枝。有限Qwen2.5-0.5B、NusaX/XNLI、一token标签、4seeds，poolA competence/mean/discovery共用，poolB第二阶段heldout，不授筛选免偏。难task倾向Circuit、易task可NearZero，弱English50-sample XNLI深scope退；Table4选择更佳test分支不能当预先部署rule。Mean是reference非faithful counterfactual，D1与ratio/depth反侧保留；5epochs/128tokens/lr5e-5/batch16，hardware/precision/concurrency/SLO及总discovery+training wall-clock Not Disclosed，.23–.66%trainable参数不授同幅计算/显存节省。具体scope缺口触发受影响命题深入；root实际必要原证/actual [Ch29](../../../../books/part-04-training-system/29-sft.md) PRE后窄写415，root独读397–430完整邻接/自身1357 POST通过，锁释放。未核实现/复现。[必要证据](../_sources/daily-20260115/increment-pre-language3-20261007.md)。

### [Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/html/2601.08545v1)

exact-v1 method Eq1–14/主Tables2–4/迭代与Appendix：同problem历史错误—通过pair的edit向量与failed generated patch改变下一轮reference search；Eq10符号不统一不采用solver recipe，failed vector不是bug真值。ACPR选407tests/306users/65problems及CodeNet同题274349条限制人口，三次repair filter与reference/LLM说明共同增益非单因果。iter3额外calls未matched总budget；B-F1只计通过code，189输出/1390pairs的人审point93.02%不等sample67.72%/11.12%未定的全部说明正确。temperature.2/top5、4o-mini T0 judge、A800仅open模型；precision/batch/concurrency/SLO/完整调用费/seed Not Disclosed。actual [Ch76](../../../../books/part-07-agent/76-rag.md) 正文732区分proposal与独立full-project验收；review_jan15_delta实际724–746邻接/自身末注POST通过，锁释放。未运行代码/复现。[必要证据](../_sources/daily-20260115/increment-pre-language3-20261007.md)。

### [When Models Know When They Do Not Know: Calibration, Cascading, and Cleaning](https://arxiv.org/html/2601.07965v1)

exact-v1 §2.1–3.5/AppD/Alg1：validation按small-confidence分箱统计large−small平均calibrated advantage，K低增益bins保small；线上先small完整生成，仅按bin决定large，非在线先跑两模型。两模型marginal校准不证明small-bin条件下large已校准；有限OOD/accuracy—small-use ratio不授完整SLO，small沉没prefill/decode/升级重prefill与offline双模型均有费。ImageNet1000人工核不同MMLU/ARC/MBPP的4o pseudo-label，cleaning不授原库饱和真值。hardware/precision/batch/concurrency/SLO/完整费用 Not Disclosed。actual [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) Calibration Routing State新增分箱升级段，review_jan15_delta实际1033–1057邻接/自身末注POST通过（后续段位顺延），锁释放。[必要证据](../_sources/daily-20260115/increment-pre-evaluation3-20261007.md)。

### [Cross-Cultural Expert-Level Art Critique Evaluation with Vision-Language Models](https://arxiv.org/html/2601.07984v1)

exact-v1 §3/RG-RF/heldout152与train298、AppB2/B3/B8/B9/Limitations：isotonic只aggregate，训练MAE改善47.6%非heldout5.2%，不同culture小n与迁移反侧保留；ICC−.50不是普遍ensemble无效，ρ≥.97仅weight ranking稳定非humanρ。Pure TierII对human可强于fusion，B14六×98/686口径冲突不合并。15VLM/294anchors/4406评价，hardware/precision/batch/concurrency/SLO/全费用 Not Disclosed，未复现。review_jan15_delta实际源与 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 328–347/368–389的尺度/共偏、anchor、agreement非下游真值已有覆盖通过，无Books diff。[必要证据](../_sources/daily-20260115/increment-pre-evaluation3-20261007.md)。

### [Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis](https://arxiv.org/html/2601.07974v1)

exact-v1 §3–6.3/Limitations：7LLM/6prompt/4英语域516k，跨prompt、family、domain各轴分开非联合OOD；绝对相关失去方向，总体.109/.116和局部>.7不合成根因。§6.3确做BH/Bonferroni及Spearman，cross-domain严格校正零显著；不能误写未做校正或唯一语言feature因果。XLMR/DeBERTa168detector、3epochs/batch16/len512/H100约400GPUh，precision/concurrency/SLO/seed Not Disclosed。review_jan15_delta实际原证与 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 551–587/636–665的人口/scorer、相关非因果/holdout已有覆盖通过，不作自动作者身份或普遍detector无效保证。[必要证据](../_sources/daily-20260115/increment-pre-evaluation3-20261007.md)。

### [TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL](https://arxiv.org/html/2601.08743v1)

exact-v1 §4.1–4.2/§5 Tables1–5/§6/8：PK/FK先选offline joint-encoding boundary、位置对齐后组合packet；FK非天然DAG或完整query因果，position不修复hidden。A800/Omni7B/Qwen7B/Spider-BIRD，mask tuning/lr1e-6/3epochs；BIRD Table1 61.5→59.9与training-free Table5 51→42.9反侧保，全test累计TTFT不是P99，precision/concurrency/SLO/seed及完整offline/lifecycle费 Not Disclosed。actual [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 212补relation closure、扩大边界/full-prefill与全部费用；review_jan15_delta实际204–224邻接/自身末注POST通过，锁释放，不授实现/复现。[必要证据](../_sources/daily-20260115/increment-pre-cachefusion3-20261007.md)。

### [Parallel Context-of-Experts Decoding for Retrieval Augmented Generation](https://arxiv.org/html/2601.08670v1)

exact-v1 Eq1–3/§4–5/Tables1–3/Lim与AppA–C：context-minus-empty-prior加retrieval信号，在expert×vocab读出面选择token，append给全部N+1独立stream，非恢复cross-document attention。Raw logit可比与prior并非truth confidence，missing/lowrank evidence有反侧；7–13B/greedy/top90单seed42，QA任务与64×2048 one-secret/512output synthetic latency不拼无损SLO。FP16 1222×74token的11.04GB只是cache非总HBM，hardware/batch/concurrency/fullSLO Not Disclosed；N+1forward/history与offline更新均收费。actual [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 214补第三读出接口/完整context回退，review_jan15_delta实际204–224邻接/自身末注POST通过，锁释放，未核实现/复现。[必要证据](../_sources/daily-20260115/increment-pre-cachefusion3-20261007.md)。

### [Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention](https://arxiv.org/html/2601.08151v1)

exact-v1 §3–5.6/Eq1–4/Tables1–3：LLaVA1.5/1.6 7B六VQA，early-late map差提出晚层visual-position软mask。Visual hidden zeroing不删除全部已传播信息，late敏感不授fusion完成/唯一因果；扩candidate层、深层/过mask退，Qwen2更强与58.17/58.25汇总冲突保留。Soft suppression非physical pruning，hooks/map取得仍付费，作者RTX A800口径不自行修SKU；precision/batch/concurrency/SLO/seed/fullfee Not Disclosed。actual [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 107新增sensor-map/consumer-hook分责，review_jan15_delta实际101–116邻接/自身末注POST通过，锁释放，未核代码/复现。[必要证据](../_sources/daily-20260115/increment-pre-cachefusion3-20261007.md)。

### [Hierarchical Precision and Recursion for Accelerating Symmetric Linear Solves on MXUs](https://arxiv.org/html/2601.08082v1)

exact-v1 §III/IV/H200/MI300X：递归TRSM/SYRK/POTRF、off-diagonal低精度GEMM与diagonal高精度/scaling是明确局部计算分支；good-conditioned随机SPD+nI不授一般diagonal dominance或稳定保证，factor error不是solve residual/optimizer convergence。浅递归开销及跨hardware/caption尺寸冲突保留，不拼同数值质量训练加速；Julia1.12/vendor basecase，batch/concurrency/seed/SLO及同optimizer workload Not Disclosed。review_jan15_delta必要原证及actual Ch28:610–620/720–738判断通过；局部solver未验证foundation训练，不为成熟mixed precision原则新增Books owner，标准完成仅报告。[必要证据](../_sources/daily-20260115/increment-pre-system3-20261007.md)。

### [Coordinated Cooling and Compute Management for AI Datacenters](https://arxiv.org/html/2601.08113v1)

exact-v1 §III-C/D、IV-A–D、V/A：30min forecast/5minTP与cooling/job-class DVFS，controller周期表30s/正文1min冲突不采recipe。8V10016GB/Llama2-7B有限1h与Azure 1day模拟分开；compute/cooling24.2/31.2%分账，平均2.31→2.28s非P99，coldzone12°C/supplymin18°C口径不明。precision/batch/concurrency/SLO/完整forecast-transition费 Not Disclosed。Ch56:101补cooling慢权/compute快执行，review_jan15_delta实际91–108/自身1981 POST通过，锁释放，未核实现/复现。 [必要证据](../_sources/daily-20260115/increment-pre-system3-20261007.md)。

### [Hierarchical Online-Scheduling for Energy-Efficient Split Inference with Progressive Transmission](https://arxiv.org/html/2601.08135v1)

exact-v1 §III/Alg2/Eq23–28/IV：任务profile给split/bandwidth/referencepower，packet队列跟踪实际consume，importance排序与interim inference/entropy/deadline提出stop，entropy非percase正确。ResNet50/ImageNet/Rayleigh FDMA同任务1000模拟round，300msframe/1msslot/device2GHz/edge20GHz非实测GPU。Server重复inference/MLP训练费/serverenergy未计，precision/真实batch/concurrency/SLO及全链费 Not Disclosed。Eq25 q0除零/正Hessian concave冲突不采recipe，M² residual不授零violation。Ch56:496补reference/packet与stop分责，review_jan15_delta实际485–506/自身1983 POST通过，锁释放，不泛化LLM协议。 [必要证据](../_sources/daily-20260115/increment-pre-system3-20261007.md)。

### [KidVis: Do Multimodal Large Language Models Possess the Visual Perceptual Capabilities of a 6-Year-Old?](https://arxiv.org/html/2601.08292v1)

exact-v1 methods/metrics及§III–IV：20MLLM zero-shot，10×50任务/6重叠construct/3名6–7岁儿童；2K image file非相同actualvisualtoken，95.32/67.33非全儿童总体界。family/size encoder与训练混杂不识scaling因果，ViT/attention/memory原因是hypothesis非干预。Prompts附录HTML缺失、模型version/temperature/resize/实际visualtoken与hardware/precision/batch/concurrency/SLO/全費 Not Disclosed，采用局部输出构念反侧不授风险率。review_jan15_delta必要原证与actual Ch23:86–90 recover/access/express具体Existing通过，无Books diff。 [必要证据](../_sources/daily-20260115/increment-pre-multimodal3-20261007.md)。

### [UM-Text: A Unified Multimodal Model for Image Understanding](https://arxiv.org/html/2601.08321v1)

exact-v1 §3.2–3.5/Eq1–3/§4 Tables1–4：mask-local RCL约束velocity，RCI约束decoder RGB Canny edge，不授semantic/shape真值。Qwen2.5VL3B/T5/OCR与FLUXFill，16A100/512²；顺序消融非factorial，同Designer baselines不授独有收益，LPIPS .0479劣于DreamText .0328，§3.5/4.1更新范围冲突不作recipe。precision/batch/concurrency/SLO/seed/fullfee Not Disclosed。review_jan15_delta必要原证与actual Ch24:73–87/自身2219 POST通过，锁释放，未核代码/复现。 [必要证据](../_sources/daily-20260115/increment-pre-multimodal3-20261007.md)。

### [SnapGen++: Unleashing Diffusion Transformers for Efficient High-Fidelity Image Generation on Edge Devices](https://arxiv.org/html/2601.08303v1)

exact-v1 §3.1–3.3/Eq4–10/§4 Tables1–2/Fig8/AppA/C/H：K-DMD双目标不同权限，ASSA/elastic保crossKV及部分独立LN；无matched DMD-only不授稳定性单因果。LoRAr64/alpha128不免额外teacher/critic，student每5次更新；256A100前训与4nodes step-stage，iPhone16ProMax4step小模型1.8s/4.3bit full6.7s局部。28→4步有指标退，VAE~120ms/encoder完整费不明，手机forward/GPUmaxbatchFPS不合并SLO。review_jan15_delta actual Ch24:694–710/自身2221 POST通过，锁释放，未核代码/复现。 [必要证据](../_sources/daily-20260115/increment-pre-multimodal3-20261007.md)。

### [VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory](https://arxiv.org/html/2601.08665v1)

exact-v1 §3.3/Alg1、label/5.4/6.3/6.5 Tables6–8：summary非sensor observation，gate与memory write分时钟。128A100/4.5M训练，annotation teacher72B非reason真值；2.1%仅think_on steps非总费用节省。NoMem collision1.90低于full5.51反侧保，remote4090/Go2D457/300ms+100network约2.5FPS非P99/deadline。precision/batch/concurrency/SLO/seed/fullannotationtrainfee Not Disclosed，hidden变量/stride公式冲突不采recipe。review_jan15_delta actual Ch26:509–532/自身2005 POST通过，锁释放，不授物理安全/实现复现。 [必要证据](../_sources/daily-20260115/increment-pre-robot3-20261007.md)。

### [FSAG: Enhancing Human-to-Dexterous-Hand Finger-Specific Affordance Grounding via Diffusion Models](https://arxiv.org/html/2601.08246v1)

exact-v1 III-A–C/IV-A–D/TablesI–III/V：130demo/13objects+7unseen，两手20trials/object，lift>0.1m/hold>3s，H100/batch2/4k/3seeds。SD/DINO局部同label非全pipeline归因，baseline3keypoint/固定执行vs5finger/newplanner混杂；globalvector/dense身份冲突不采recipe，TableIII不证明统计等价。RGB+stereo depth/segmentation非depth-only，固定closure可slip，触觉仅future；precision/latency/concurrency/SLO/fullfee Not Disclosed。review_jan15_delta实际必要原证/Ch26:29–40具体Existing通过，无Books diff。 [必要证据](../_sources/daily-20260115/increment-pre-robot3-20261007.md)。

### [Semantic Misalignment in Vision-Language Models under Perceptual Degradation](https://arxiv.org/html/2601.08355v1)

exact-v1官方PDF§3–6/Tables1–6及§6.3/7/8：19Cityscapesclasses/9corruption条件；§5.4 VLM读rawimages，seg仅分析，不能授上游causal传递。§4.3 ambiguity计失败、Qwenparse.02–.22/SMR~1，parse/拒答与真实unsafe分开；CLIP/SigLIP TopK异于freeform，Figure3十aggregate条件非percase因果。hardware/precision/batch/concurrency/SLO/seed/精确N/reference来源/visualtoken值/全費 Not Disclosed，未复现。review_jan15_delta实际视读PDF3–7完整必要页与保存limitations、actual Ch66:104–119/208–225 Existing通过，无Books diff，不授真实驾驶风险率。 [必要证据](../_sources/daily-20260115/increment-pre-robot3-20261007.md)。

### [Representations of Text and Images Align From Layer One](https://arxiv.org/html/2601.08017v1)

exact-v1 §2.1–2.3/§3/5/AppE/F/G：600步DAS逆优化、100词center/patch聚合的prototype在Gemma3 4B与有限InternVL3概念转移，支持有限可恢复存在性，不证明自然text/image分布相同、原模型native调用或失败即信息消失。GPT5 hint/无hint、图中文字与十responses条件须分开，优化/外部judge全费不免；硬件/精度/SLO/优化seed Not Disclosed。review_jan15_delta独读必要源与actual Ch23:87–94/邻接，recover/access/express与方向存在/当前/适配后consumer确已有承载，具体Existing通过，无Books diff。 [必要证据](../_sources/daily-20260115/increment-pre-last4-20261007.md)。

### [Sparsity Is Necessary: Polynomial-Time Stability for Agentic LLMs in Large Action Spaces](https://arxiv.org/html/2601.08271v1)

exact-v1 A2/A3/Lemma4.5与Eq23–25/PDW必要原证：population RSC及θ*梯度条件未控制empirical增量；Hessian only-on-exact-support不能直接授邻域，dual上界仍可超过λ而不证明strict feasibility。作者sparse/klogM设计命题与这些中心缺口并存，不降分删反侧。review_jan15_delta独立核中心争议信号通过，保留准入评分，不作正面稳定/率定理或Books；只在empirical控制、邻域/dual条件及受影响证明得到补足/更正时定点重开。理论硬件/SLO不适用，未运行实现。 [core](../_sources/daily-20260115/increment-j15theory-core-20261007.txt)/[必要尾段](../_sources/daily-20260115/increment-j15theory-requiredlast-20261007.txt)。

### [Greedy Is Enough: Sparse Action Discovery in Agentic LLMs](https://arxiv.org/html/2601.08280v1)

exact-v1 §3–5/App必要Alg1及Thm4.8 L502–506：conditional greedy须稀疏support、coverage/incoherence条件，OMP扫描全部M/refit不等未知support已免费找到或logM实现。不同P_i下E_i N_i均值不能由单世界ΣN_i=T推出≤T/M；所用onehot族本身1-sparse也不建立‘去稀疏才线性’。review_jan15_delta独核此中心下界信号通过；有限条件算法与失败下界分开保留，当前不作正面复杂度/Books。更正跨世界change-of-measure/计数及dense-vs-sparse假设后仅重开对应证明，非要求完整附件。理论硬件/SLO不适用，未实现/复现。 [必要原证](../_sources/daily-20260115/increment-j15theory-requiredlast-20261007.txt)。

### [Hyperbolic Heterogeneous Graph Transformer](https://arxiv.org/html/2601.08251v1)

exact-v1 relation-specific curvature/QKV+Hypformer HT/HR/linear attention，在三真实graph与合成BA规模的局部node classification有证据；Eq18 log-tangent聚合与‘all-hyperbolic’标签需分开，借用算子不计新增Design/Reach。两类实验配置/容量不同，CE与SVM度量描述不一致不采recipe，更多heads/layers/dim有退步。review_jan15_delta必要方法/评价与4分局部关闭判断通过；仅报告，尚未改变foundation系统长期选择，不因小图或局部实验拒准入，无Books。 [core](../_sources/daily-20260115/increment-j15theory-core-20261007.txt)/[评价](../_sources/daily-20260115/increment-j15theory-evaluation-20261007.txt)。

### [CASHEW: Stabilizing Multimodal Reasoning via Iterative Trajectory Aggregation](https://arxiv.org/html/2601.08010v1)

exact-v1 §4/Eq1–6、§6/Tables1–3、AppC/D1–4：N8/K4/T3候选先以GroundingDINO标注object keys，再对subset合成新trajectory并重核。检出对象不授关系/逻辑/总体truth，共享detector误差可传播；同NKT有无DINO只支持局部增量，SFT-only两任务退步与更多轮次边际/退收益保留。8H100推理/16H100训练而precision/latency/SLO/全部calls费用Not Disclosed，teacher30B/30kSFT/200kRL与多轮生成/检测均计账；Eq13–14不照录为标准ratio-GSPO recipe。actual [Ch20](../../../../books/part-02-model/20-sampling.md)394补“新trace生成→重核”接口，review_jan15_delta实际366–409完整邻接/自身EOF注POST通过，root锁释放，未运行实现/复现。[必要证据](../_sources/daily-20260115/increment-pre-last4-20261007.md)。

### [Model-Agnostic Solutions for Deep Reinforcement Learning in Non-Ergodic Contexts](https://arxiv.org/html/2601.08726v1)

exact-v1 §2–5/Alg1–2/AppA1–3：重复horizon和wealth输入的有限toy曲线有研究价值，但Alg2一次抽f后M轮iid乘法收益、reward=WM−W0及expected policy gradient并未改目标。E[WM|f]=W0[1+f(E[R]−1)]^M，M>0仍单调端点；例如p=.4、win3/loss.2给ER1.32，expected最优f1而Kelly为.2。反例只绑定所述固定f/iid前提，不否定所有growth RL；近Kelly曲线不修复estimand。40DQN/20AC重复不授普适理论，runtime/fullfees Not Disclosed或toy不适用。review_jan15_delta已独核中心信号，5分准入保留、中心争议终态隔离，不作正面证明/Books；仅更正目标/状态/回报依赖或Alg2推导时重开。[必要原件与边界](../_sources/daily-20260115/increment-pre-last4-20261007.md)。

### [PersonaDual: Balancing Personalization and Objectivity via Adaptive Reasoning](https://arxiv.org/html/2601.08679v1)

exact-v1 §3.1–3.3/Eq1–8、Tables1–2/AppB2–3：每mode强制n回答保证探索人口，mode内response与跨mode平均收益分账。Eq8合计r−另一mode均值不授prefix/selector无偏joint-loss；aligned/unaligned合成persona非真实人群，attention非因果。8B/8A800/2nrollout、teacher及训练预算不可省，NoPersona局部仍强。actual Ch33:110补该信用分工，review_jan15_delta实际99–118邻接/self note POST通过，root锁释放。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [Prism: Towards Lowering User Cognitive Load in LLMs via Complex Intent Understanding](https://arxiv.org/html/2601.08653v1)

exact-v1 §4.2–4.4/§5.1–5.3及完整AB：LLM与counterexample人审prerequisite→层内并问/层间history，NLI/MC是局部澄清改进。20人固定Prism→others顺序、100预选任务与order练习混杂不授普遍cognitive因果；不因用户研究领域贡献前排除。1+1+2=4关闭判断，reviewer已独核，仅报告不增书，不授标准全附件。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [ExpSeek: Self-Triggered Experience Seeking for Web Agents](https://arxiv.org/html/2601.08605v1)

exact-v1 §3–6/主Tables1–4/AppA1：fullvocab entropy的两类trigger、teacher235B标签、topicguide/answer reopen/cooldown，processAUC.6223/answer.7187非单步truth。170例/1000bootstrap与5runs局部；GAIA8B66.94→127.57s、xbench51.06→143.81s，去库仍改善不归memoryalone。reviewer实际Ch77:231–247已有bank/controller分权、误干预/漏触发、Context费/passive/always-off，具体Existing通过，无diff。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [VideoHEDGE: Entropy-Based Hallucination Detection for Video-VLMs via Semantic Clustering and Spatiotemporal Perturbations](https://arxiv.org/html/2601.08557v1)

exact-v1 §3/§4.4：复用HEDGE/SE/RadFlag/VASE并适配视频frame/pixel预算，490clips/1460pairs局部贡献保留。Clean/noisy预算随distortion一起增，AUC非视觉grounding因果，judge只读参考/文本；1885unsupported>1035supported与作者相反措辞不采。1+1+2=4关闭判断，reviewer已独核，仅报告不增书。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [M3-BENCH: Process-Aware Evaluation of LLM Agents Social Behaviors in Mixed-Motive Games](https://arxiv.org/html/2601.08462v1)

exact-v1 §3.3–3.4/§4.1 Tables3–4：BTA行动/paidrules、RPA可见理由、CCA通信三view，50episodes与50human subset只支持两任务局部反侧。RPA非内部motivation真值，score一致非agent本体trait，通信改context并计fee。reviewer实际Ch66:208–225与269–282已有并行可观察证据/visible rationale非intent及完整identity，标准与具体Existing通过，无diff。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [Decoding Order Matters in Autoregressive Speech Synthesis](https://arxiv.org/html/2601.08450v1)

exact-v1 §2.4.2–3/§3/§4/§5.2：duration定segment、meanconfidence选段，段内随机逐frame，不等TopK并行或80bins jointposterior。LJSpeech单speaker/50audios/10MOSraters，top1*同时改值采样；K增MCD/F0改善却UTMOS退，durationMOS只相当基线。Duration/encoder/vocoder/fullforward/排序训练费与ND完整runtime保留。reviewer实际Ch24:399–417/406/self note POST通过，root锁释放。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [YaPO: Learnable Sparse Activation Steering Vectors for Domain Adaptation](https://arxiv.org/html/2601.08441v1)

exact-v1 §3.2 Eq3–4/Alg1、§4–5 Tables1–5/Lim/AppA/B：仅优化SAE码向量，原h−DecEnc(h)残差加回；ReLU非独立概念/稀疏证书，Eq4缺负号不采solver。Reference-free仍需unsteered模型比照，latent维度可超dense；65k/131k参数、8MI210/20epochs不含SAE/patch/数据/judge总费。PortugueseOG BiPO更强、CAA general平均更高，MMLU非全utility。revieweractual Ch20:282–305/291/selfnote POST通过，root锁释放。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation](https://arxiv.org/html/2601.08430v1)

exact-v1 §3.1 L124–145：先response/principle生成与异模型聚合，再选高分两答案追加细判据，有局部criterion-generation增量；成熟rubric/RS/GRPO不计本稿DesignReach，110k数量不自增长期贡献。Table3累计组件/两medical评价不授偏差消除、criterion truth或通用difficulty校准。4分关闭判断仅报告，reviewer已实际必要fact通过，不因medical名称排除、不授标准全附件。 原件/必要独核见[余项提案](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)及[独立恢复层](../_sources/daily-20260115/increment-independent-delta-20261007.md)。

### [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/html/2601.08406v1)

exact-v1 §II-A/B、§IV-A/B/TableII：外部click/type及人工semanticID是scorer接口而非真实安全权威，仅覆盖这些action。1226任务的1-ASR按三风险源取mean非全部请求加权；同GPT4o跨四框架不能归单一内部机制，QwenVLMax/六model口径冲突不采统一recipe。hardware/precision/seeds/runtime/SLO/全部费用Not Disclosed。review_jan15_delta必要原证及actual [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)95–119/208–225通过，target/system/scorer与choice/effect/可见理由的具体分权已有承载，无diff。[必要命题](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。

### [AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation](https://arxiv.org/html/2601.08323v1)

exact-v1 §3.1–3.3/Eq1–7、§4/Tables1–3：CRUD action序列、Read的下一内部step观察与每step scratchpad，terminal EM advantage广播不授局部操作真值或DB原子性。三QA/三runs与200→400/800docs局部；Delete去除2wiki+.3，更大K不总优，Table1/3不统一为完整recipe，组件去除不是生产failover；hardware/precision/SLO/全部费用Not Disclosed。reviewer实际 [Ch77](../../../../books/part-07-agent/77-memory.md)91–124/153–173的typedtransition/事实commit与terminal proxy/local credit具体已有覆盖通过，无diff。[必要命题](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。

### [ToolACE-MCP: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/html/2601.08276v1)

exact-v1 §3.3–3.4/§4.5/Limitations：依赖graph与mutation形成全部LLM模拟的多turn response及history routing监督，是局部训练接口增量。成熟graph/DFS/LoRA不计新增Reach，router不获真实执行权；去history局部53→48/60→52与91.6不授协作完成或webscale保证。1+1+2=4关闭判断仅报告，非作者已独核，不因MCP名称排除，不增加长期协议链。[必要命题](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。

### [T3: Benchmarking Sycophancy and Skepticism in Causal Judgment](https://arxiv.org/html/2601.08258v1)

exact-v1 §3.1–3.6、Tables5–7、AppC/Limitations：三label与neutral/social/epistemic压力是局部诊断接口，GoodFlip定义仅从wrong换label未必更正；454/504分母及55pp构念不合不作统一全局结果。10组内gradannotator规则不授因果真值，T0/paired问题不等完整独立runs，RCA与普适模型排名不采用；runtime/API/全部费用Not Disclosed。review_jan15_delta独立必要源及actual [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)49–60/208–225的risk/coverage/conditionalaccuracy、matchedpressure与valid/拒答分母已有具体承载通过，无diff。[必要命题](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。

### [Owen-Shapley Policy Optimization (OSPO): A Principled RL Algorithm for Generative Search LLMs](https://arxiv.org/html/2601.08403v1)

exact-v1 §3.1/Eq4–8/Alg1、Tables1–2、coalition/retriever反侧与AppA1/A2：有限连续子串→oracle marginal→span/token weight是可核局部归因proposal，非真实因果或完整Shapley效率证书。均adv恒等式不证均gradient/PBRS；T2、gradient[1,−1]、A1、weight[1,0]给原均gradient0而重分1，zero/signed归一不可免。有限Qwen/ESCI-HM、宽度/采样与迁移不授普遍稳健，hardware/precision/seeds/SLO与全链query/teacher费用Not Disclosed。actual [Ch33](../../../../books/part-04-training-system/33-grpo.md)313将该接口接在候选集合max后，保旧credit、完整账本/回退；reviewer实际303–328及自身3034note POST通过，锁释放，未核实现/复现。[必要命题](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。

### [ORBIT: On-policy Exploration-Exploitation for Controllable Multi-Budget Reasoning](https://arxiv.org/html/2601.08310v1)

exact-v1 §3.1–3.2/Eq5–12、Tables1–2、jointRL与OPD/offline反侧：预算压缩保存各mode teacher，uniform mode的student prefix由对应teacher评分；merge仅初始化。三backbones/两训练corpora/五评测分开；avg@32为mean pass1非pass32，GPQA/MMLU mode不总单调，OPD/offline同mergeinit稳定/收敛相近，不采Pareto/globalceiling或online hardbudget保证；Eq5次概率与Eq8条件分布/pnontrunc0限制不混。hardware/precision/seeds/SLO/全teacher/RL/merge/rollout费用Not Disclosed，图tokens/samples对齐不等全费匹配。actual [Ch29](../../../../books/part-04-training-system/29-sft.md)294补mode/teacher/prefix责任，保固定teacher/offline验收与推理consumer；reviewer实际280–308及自身1365note POST通过，锁释放，未核实现/复现。[必要命题](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。

## 5. 缺口与下一步

新增补充普通扫描、筛选、候选必要审阅及Books修改待办：无。正式51=24actual POST+17具体Existing+6OnlyReport+4争议，各确定候选逐篇处置；14源有限范围/停止已归并§2。最终六部分非作者DAY已通过，无可执行待办，外部历史/日期与中心争议已按下述终态隔离，不扩216库存、不重做有效项。

新增中心争议保留08333：三前提未排除独立OBSERVER或有效外部推理，故不支持所有同类型tool架构必然self-licensing。保留原文、具体反例与准入评分，不作正面证据/安全保证或Books；只在§3.4必要前提/证明得到补足或更正时定点重开，不索取全部Agent框架历史。必要中心信号已由root独核通过，本轮非作者日级验收已通过，不使争议证明变成正面证据。

新增日期终态保留：08815窗前whitepaper、08778窗前supplementary PDF A.3/Table9已有采用命题，commit非public时间，本窗first/重要增量未建立。07963 3DGS-Drag原文链接repo明列ICLR2025同题citation，官方OpenReview同题/作者/完整摘要发现但旧PDF/forum/API2 challenge，不能由会议年/搜索摘要/新arXiv注册确定first或重要revision。三项不评分/确定候选/Books、不定旧归属；必要原证/actual Existing仅供恢复。重开仅需dated本窗重要机制/evaluation差额或可核旧完整稿时序，不索取全历史。[07963定点原件](../_sources/daily-20260115/increment-pre-remaining14-20261007.md)。19935/16224正式ID上界Jan29/Jan26跨窗，原公告/作者dated完整稿可替代，不据Submitted补日期。非作者已确认精确隔离；不作正面证据、Books或来源无遗漏保证。

以下保留原52家族批次的有效终态；其“无可执行待办”及原通过仅指原批次，不代替新增补充验收。

可执行待办：无。52家族已逐项处置、39处改书及3项具体Existing经非作者确认，最终六部分非作者独立日级Gate通过；无未读正文、待写Books或尚待日期判定的确定候选。

终态保留项：以下外部材料与争议子命题不用于正面证据、Books或无遗漏断言；定点重开条件逐项如下。

GLM-Image缺可确定落窗的first-public下界；现有粗日blog/repo/公开issue只给上界，无法证明整个区间在本窗。可接受作者原dated完整公开稿、announcement原日志或原全文公开证据；只重开该日期身份，当前不评分/不入Books。Qwen/Hunyuan/Meta/Moonshot/MiMo历史目录及其他机构语言/catalog漏段缺可用本窗列表；恢复原dated目标条目/可读archive即可，不请求整年抓取、不用于无遗漏。官方arXiv月列表404的缺口可由同批次原公告补回，只恢复受影响主题/身份。

中心争议HA-DW08521与ACPS08108缺明确conditioning/gradient对象或完整frontdoor调整分布更正；当前实验不充当识别证明，保留原准入/评分与已读反侧，未纳入Books。相关lower-bound、率分母、成本call数字等实际子命题冲突已在对应小节隔离；不global否定独立可支持接口，也不以未来全文复查为普通待办。

窗外/日期恢复另段：08893 SGFM上界Jan15T02:33:21Z越过本日报终点，保留Jan16定点恢复线索，不扩本窗。08884 GEPA OpenACC的Submitted虽为Jan12T23:54:08Z，Updated-v1Jan15T01:01:00Z/registeredJan15T02:33:09Z仍跨本窗右界；正常提交不能保证未延迟公开，当前不当确定本窗候选/评分/Books。[原字段](../_sources/daily-20260115/DATE_DECIDING3.jsonl)只支持这项日期保留，必要core反馈/编译与speedup分账线索留真实归属日恢复，不无限查月页。CRAFT的2603 ID及PTCBENCH2602 ID不能因SubmittedJan12放入Jan15，first-announcement月份不同；没有已知Jan原完整正文公开线索时到此停止，不给本窗分数/Books。均不阻塞本窗终态。

## 6. 复核

新增补充复核者：root与review_jan15_delta（均非报告作者）。结论：通过，review_jan15_delta已实际六部分DAY PASS，普通扫描/筛选/候选必要审阅/Books待办0。root完整AB校准首8/第二20/第三42/边界8与代表排除，原52有效成果及增量8POST/6Existing/08333信号复用；review_jan15_delta实际增量16POST/11Existing/6Only/3争议信号通过，连同root共51=24POST/17Existing/6Only/4争议。各POST实际正文完整邻接/selfnote，全部共享窄锁释放，DAY依据实际来源停止/日期准入/必要证据/owner与实际写入，而非PRE/机器校验；08422/08477/GLM具体关闭与07963/08778日期隔离已具名独核，下面原日级通过仅指原批次。

本轮独立验收依据：[review_jan15_delta审阅记录](../_sources/daily-20260115/increment-independent-delta-20261007.md)“本轮独立DAY：通过”。实际完整六部分核来源与停止、候选/日期/评分、逐篇采用及反侧、具体Books/实际POST、外部终态与恢复条件；复用root有效首15，不无差别重读源或原52。新增36由fresh reviewer按必要命题核，其中16POST/11Existing/6Only/3争议；明确排除与未读库存的分层范围见独立记录，不授全216或全学科召回。没有普通待办，不启动其他日期。

本轮最新机器检查：103正式家族（原52逐字+新增51），V3 exit0；249个本地引用按真实文件目标存在，5条原批次`.md:行号`旧链接原样保留，本次新增均用真实relative.md并把行位写标签/近文。原窗口、前52候选行及原§4连续正文机械保留通过，新增候选表为一个连续Markdown表。README/sources及本轮实际11个Books owner的限定unstaged/cached diff-check exit0；不代替独立DAY、不授复现/生产性能。未stage、commit、push，LS/索引由root持有未写。

复核者：root（非作者）
结论：通过

root完整顺读本报告六部分，实际核有限来源/补尾停止范围、52条件日期、39处正文/邻接/末注POST、3项具体已有覆盖、8项仅报告、2项争议终态及下述具名负侧范围，日级Gate通过；不授历史目录无遗漏、实验复现或生产能力。

实际已独立校准全部52家族题摘、必要原证据→具体owner与39处正文/邻接/末注写后；3项Existing的现正文也实际读到。纠正了OrderProbe“未证架构因果就关闭”的误判，恢复canonical reconstruction与semantic稳定不同评价对象；GAG不因science测试领域关闭，贡献限定输入adapter。HA-DW/ACPS中心实际公式冲突终态隔离，不以降分缩池。准确性/安全负侧均读必要位置而非全附件。

具名负侧分层已核：机构发布层OpenAI Cerebras/RFP和Anthropic PBT（3项具体关闭）；任务组合层08741 rows/RRF、08742 attribution层级、08472 sui-1、08689 QuantEval（4项共同理由受影响复查）；领域范围层08692 nationality任务与08750 ecology（2项，不因名称直接关闭）。这是至少9项具名实际层次，不把宽API或未读AB2余53说成全量排除已验。尾部负侧根实际完整题摘分层样本7项：07944条件posterior域边界、07954医疗任务SFT/DPO组合、08884 GEPA反馈（由原泛组合理由改为潜在机制但精确日期分流）、08035 HCI教育概念lens，以及07964传统ontology/game（LLM仅未来）、07953量子resolution/Wu、07939 citation sentiment+LLM summary。最后三项完整题摘已补读；scope/任务组合具体关闭而非仅按领域名。作者15份完整AB筛选不等根全15/fulltext重审；07942portfolio、07930chemical、07951weather仅明确范围标题查漏未展开，AB2其余53库存没有逐项关闭或全文验收。来源有限停止点在§2及原查询，未恢复的目录不作无遗漏断言。

机器检查：当前52项六部分稿运行 `python3 scripts/validate_research.py --report papers/2026/01/15/README.md` exit0；115个本地引用实际存在；本日README/sources及本日涉及21章范围的unstaged/cached `git diff --check` 均exit0。这只确认格式、引用和可判定一致性，不替代语义验收。保护全部已有/其他日期dirty与staged改动，未stage、commit、push，不改其他日期/LS/索引。root日Gate已经通过、普通待办为0，本日结束；外部保留项的未来材料只定点重开，不启动其他日期。
