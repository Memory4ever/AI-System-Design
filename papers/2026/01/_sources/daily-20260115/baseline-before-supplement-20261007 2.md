# Daily Research — 2026-01-15

**规范：** V3
**窗口：** 2026-01-14T09:00:00+08:00 ～ 2026-01-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T17:58:51+08:00

## 1. 结论

冻结52个唯一论文家族：39项实际整合并经非作者root正文/邻接/末注写后通过、3项已有具体覆盖、8项仅报告、2项中心主张争议隔离；没有结构候选。既定arXiv分页已补至下界，尾部七项全部获得必要审阅与处置，GEPA因日期区间跨窗隔离。HA-DW此前未保存数字分数，本次首次明确2+1+3=6并经独立确认。root已完整顺读正式六部分并核来源停止点、条件日期、逐项证据/Books与具名负侧范围，非作者独立日级Gate通过；普通待办0。

最重要的变化不是宣称更多模型/系统更好，而是把具体接口分开：单连续reasoning state不等K条轨迹；全局时长预算不等逐kernel无慢；树内工具credit、memory最新update-step与workflow prerequisite均是受条件限制的proxy。偏好目标还依赖部署k、采样coverage和reference/history身份；评价中的language-ID、拒绝率、hidden一致与合法终态都不替代真正需要验证的对象。

39项实际改动保留原方案、局部反侧及成本。没有运行代码、复现实验或证明生产收益；论文作者结果与本报告工程推断分开。下面52项的证据/Books结果均已独立逐项确认，不因补尾校准重审未变化部分。原始查询总数、读取完整题摘数与当窗家族不是一个分母；首次宽114与AB2取得65均仅发现库存，AB2未审53不成为默认任务队列。

## 2. 来源覆盖

只处理14个Daily入口及实际论文/日期恢复，不扫Weekly。以下“已检查”只代表所列有限切片；外部保留项不支撑无遗漏或零研究结论。[来源恢复细节](../_sources/daily-20260115/SOURCE_RECOVERY.md)、[原官方说明](../_sources/daily-20260115/OFFICIAL_CORE_RAW.md)、[原API](../_sources/daily-20260115/THEME_API.jsonl)和[补尾标题](../_sources/daily-20260115/THEME_TAIL_TITLES.jsonl)保留依据。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方Research/RSS恢复至Jan14–15相邻事件；Cerebras合作与US supply-chain RFP实际核心已读 | 已检查 | 两项为采购/集成计划，无新可核执行机制；粗日期不再影响贡献关闭，不授已上线性能 |
| SRC-ANTHROPIC | Research原目录、Jan14 PBT新blog核心与2510.09907v1必要对应 | 已检查 | 新Sonnet4.5/evaluationagent/三专家为验证配方更新，旧PBT机制与intent反例非本日新增，不作为候选 |
| SRC-GOOGLE-AI | DeepMind/Research当前入口、定点Jan14切片和FunctionGemma card更新线索 | 受阻 | card UpdatedJan14不等Dec18原机制新公开；当前索引/辅助检索不是完整历史archive，需原dated新机制材料重开 |
| SRC-META-AI | 官方Research web/native285061bytes shell与目标日定点检索 | 受阻 | 未恢复可用Jan14历史列表，不据空shell称零；恢复原dated条目/usable archive时只重开对应项 |
| SRC-QWEN | 官方主页动态目录、浏览器/runtime及六个已观察JS资产的有限恢复 | 受阻 | 动态模块未恢复完整历史article接口/列表，不遍历所有chunk；原Jan14文章/可读历史目录可替代 |
| SRC-DEEPSEEK | 官方主页与Engram具体公开PR/issue日期 | 已检查 | Engram已于Jan13T03:47:53Z公开PR，早于窗口；当前主页非历史archive，余目录保留、不授机构无遗漏 |
| SRC-MOONSHOT | Platform Blog有限dated目录、GitHub pinned及首10/42 current repos | 受阻 | blog可见记录早于2026、GitHub Aug–Octcurrent不是Janarchive；需具体Jan14原报告/release |
| SRC-TENCENT-HUNYUAN | 必须首查Research的direct/browser多次尝试；fallback pinned6/首10of83及T1 | 受阻 | Research导航timeout/blank不等无条目；current GitHub不是历史切片，需实际Research列表或dated原稿 |
| SRC-ZAI | 官方Research/GLM-Image blog、早repo有限tree与公开issue | 受阻 | GLM-Image仅粗Jan13/14日期、public upper无必要lower；不能确定落窗，日期终态隔离，不候选/评分/Books |
| SRC-BYTEDANCE-SEED | 观察到的get_article_list_v2：2026/type1/count20/offset60到80跨Feb26→Jan26→Jan21/19并end；type2 EN0/ZH0、20终页 | 已检查 | 当前catalog语言过滤与total/visible不一致，最早blogFeb12；只证这有限返回无本窗event，不证历史齐全 |
| SRC-BAIDU-ERNIE | 官方blog有限相邻Jan目录与Jan15榜单post核心、GitHub入口 | 已检查 | 榜单/产品评价无新增mechanism，贡献前关闭；current repo/catalog未证明历史全集 |
| SRC-XIAOMI-MIMO | 官方八dated paper tiles（Jan8 Flash至2025）、15undated blog tiles及Flash原blog shell | 受阻 | undated/无完整正文的历史blog不可作零命中；需原dated本窗机制材料 |
| SRC-MINIMAX | EN/CN blog catalog跨Jan27/28到Dec23；AgentTech原入口→llms.txt50lines→techblog.md一条May13并end | 已检查 | 有限catalog无Jan14entry，语言/历史删漏保留，不能据current目录授全机构无遗漏 |
| SRC-ARXIV | CL/LG language-model/Transformer/MoE、AI/IR/MA LLM/agent/reasoning/memory、CV/RO multimodal/world/VLA/diffusion、DC/AR/OS/PL/PF LLM/GPU/kernel/inference四主题；submittedJan12–13仅发现，选择Jan12T19～Jan13T19批次；前两主题start100补尾分别跨Jan12T18:53:09、18:15:50，另两73/73及17/17已跨下界 | 已检查 | 分页执行已闭合：model193返回、agent200/223已越界停止，不需全223；相关/含糊尾题15完整AB实际筛选，新增七家族已逐项处置并冻结52。官方月list404为历史覆盖保留，不授全分类召回 |

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

## 5. 缺口与下一步

可执行待办：无。52家族已逐项处置、39处改书及3项具体Existing经非作者确认，最终六部分非作者独立日级Gate通过；无未读正文、待写Books或尚待日期判定的确定候选。

终态保留项：以下外部材料与争议子命题不用于正面证据、Books或无遗漏断言；定点重开条件逐项如下。

GLM-Image缺可确定落窗的first-public下界；现有粗日blog/repo/公开issue只给上界，无法证明整个区间在本窗。可接受作者原dated完整公开稿、announcement原日志或原全文公开证据；只重开该日期身份，当前不评分/不入Books。Qwen/Hunyuan/Meta/Moonshot/MiMo历史目录及其他机构语言/catalog漏段缺可用本窗列表；恢复原dated目标条目/可读archive即可，不请求整年抓取、不用于无遗漏。官方arXiv月列表404的缺口可由同批次原公告补回，只恢复受影响主题/身份。

中心争议HA-DW08521与ACPS08108缺明确conditioning/gradient对象或完整frontdoor调整分布更正；当前实验不充当识别证明，保留原准入/评分与已读反侧，未纳入Books。相关lower-bound、率分母、成本call数字等实际子命题冲突已在对应小节隔离；不global否定独立可支持接口，也不以未来全文复查为普通待办。

窗外/日期恢复另段：08893 SGFM上界Jan15T02:33:21Z越过本日报终点，保留Jan16定点恢复线索，不扩本窗。08884 GEPA OpenACC的Submitted虽为Jan12T23:54:08Z，Updated-v1Jan15T01:01:00Z/registeredJan15T02:33:09Z仍跨本窗右界；正常提交不能保证未延迟公开，当前不当确定本窗候选/评分/Books。[原字段](../_sources/daily-20260115/DATE_DECIDING3.jsonl)只支持这项日期保留，必要core反馈/编译与speedup分账线索留真实归属日恢复，不无限查月页。CRAFT的2603 ID及PTCBENCH2602 ID不能因SubmittedJan12放入Jan15，first-announcement月份不同；没有已知Jan原完整正文公开线索时到此停止，不给本窗分数/Books。均不阻塞本窗终态。

## 6. 复核

复核者：root（非作者）
结论：通过

root完整顺读本报告六部分，实际核有限来源/补尾停止范围、52条件日期、39处正文/邻接/末注POST、3项具体已有覆盖、8项仅报告、2项争议终态及下述具名负侧范围，日级Gate通过；不授历史目录无遗漏、实验复现或生产能力。

实际已独立校准全部52家族题摘、必要原证据→具体owner与39处正文/邻接/末注写后；3项Existing的现正文也实际读到。纠正了OrderProbe“未证架构因果就关闭”的误判，恢复canonical reconstruction与semantic稳定不同评价对象；GAG不因science测试领域关闭，贡献限定输入adapter。HA-DW/ACPS中心实际公式冲突终态隔离，不以降分缩池。准确性/安全负侧均读必要位置而非全附件。

具名负侧分层已核：机构发布层OpenAI Cerebras/RFP和Anthropic PBT（3项具体关闭）；任务组合层08741 rows/RRF、08742 attribution层级、08472 sui-1、08689 QuantEval（4项共同理由受影响复查）；领域范围层08692 nationality任务与08750 ecology（2项，不因名称直接关闭）。这是至少9项具名实际层次，不把宽API或未读AB2余53说成全量排除已验。尾部负侧根实际完整题摘分层样本7项：07944条件posterior域边界、07954医疗任务SFT/DPO组合、08884 GEPA反馈（由原泛组合理由改为潜在机制但精确日期分流）、08035 HCI教育概念lens，以及07964传统ontology/game（LLM仅未来）、07953量子resolution/Wu、07939 citation sentiment+LLM summary。最后三项完整题摘已补读；scope/任务组合具体关闭而非仅按领域名。作者15份完整AB筛选不等根全15/fulltext重审；07942portfolio、07930chemical、07951weather仅明确范围标题查漏未展开，AB2其余53库存没有逐项关闭或全文验收。来源有限停止点在§2及原查询，未恢复的目录不作无遗漏断言。

机器检查：当前52项六部分稿运行 `python3 scripts/validate_research.py --report papers/2026/01/15/README.md` exit0；115个本地引用实际存在；本日README/sources及本日涉及21章范围的unstaged/cached `git diff --check` 均exit0。这只确认格式、引用和可判定一致性，不替代语义验收。保护全部已有/其他日期dirty与staged改动，未stage、commit、push，不改其他日期/LS/索引。root日Gate已经通过、普通待办为0，本日结束；外部保留项的未来材料只定点重开，不启动其他日期。

