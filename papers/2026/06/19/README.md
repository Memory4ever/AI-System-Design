# Daily Research — 2026-06-19

**规范：** V3
**窗口：** 2026-06-18T09:00:00+08:00 ～ 2026-06-19T09:00:00+08:00
**状态：** 完成
**窗口说明：** 用户授权保留原小时窗、旧候选日期与评分及有效证据，仅补来源遗漏；原完成声明不代替本次验收。
**补充窗口：** 2026-06-18 ～ 2026-06-18
**冻结候选日期：** [补查前原报告](../_sources/daily-20260619/baseline-before-supplement-20261029.md)
**Coverage 限制：** 五个跨日身份、GDM官方日期冲突与Meta/Google具体历史索引限制已隔离，不支持候选、Books或无遗漏断言
**Books：** 纳入本次
**检查时间：** 2026-10-29T14:28:54+08:00

## 1. 结论

来源遗漏补查完成33个新增确定家族的必要审阅：27项窄整合、5项具体已有覆盖、1项中心争议/Books暂缓（19268）。当前97家族=原64+新33，合计49整合、47已有覆盖、1暂缓；原64身份、日期与三维评分逐项保留。确定候选普通必要与待POST均0，十四来源的实际停止与外部保留项已处理，唯一独立日级复核通过；完成仅限这些可核范围与安全终态，不表示所有原件或主张都已得到证明。[唯一补充记录](../_sources/daily-20260619/SUPPLEMENT_20261029.md)保存分批校准、精确版本、直接反侧和实际写入层。

本轮长期差额集中在producer与consumer的具体交接：失败链只提供恢复状态、不把失败答案当成功监督；压缩/层级/动作标签只有保持原人口与消费身份才可比较；代理entropy、probe、equivalence或可读交互证据不拥有正确性与安全许可。局部质量提升与全部训练、索引、双缓存、搜索或人工费用分开，保留反退与原方案。19268的乘积几何解释证明未闭，不进入Books；其有效定义不因此全盘否定。

原590身份及64候选（22整合/42已有覆盖）只描述此前小时窗，不是补窗的逐项配额。旧18967仅修复原June18采用链，旧19386纠正wall-clock decay/action cadence双regime，撤销旧采样相位解释，均不新计/改分/移归属。五个真实早v1跨日身份与一项GDM官方日期冲突未作确定候选；18558因Ai2更早June17正文已退出本日并撤回本轮新增书稿。Project Fetch只标官方Jun18已满足补窗，不再追09:00边界；三试验与人工approve仍限制采用。来源已检查的范围不是全球无遗漏，Meta原入口和Google具体外部限制见§2/5。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)完整1334items；BJT Jun18两项health/rare-disease及date-only Jun18 spend-controls核心均N，原件SUP_OPENAI_RSS；alignment完整目录Jun16→beneficial Jun18→Jul21，后者已完成 | 已检查 | RSS只当前集合，不作历史删改保证；未披新训练机制的产品/领域案例不列候选 |
| SRC-ANTHROPIC | Research当前1–2页各24位置，Oct27→Aug18、Aug12→Apr30；[第二页原接口](https://www.anthropic.com/listing/research/default/2)已跨窗，Fetch Jun18邻Jun26 Economic Index/Jun16 code-expertise，唯一目标项NC | 已检查 | 第二页hasNextPage=true但更早页已离目标；自然日不追原09:00边界 |
| SRC-GOOGLE-AI | [Google June archive](https://research.google/blog/2026/06/)完整12条Jun30→Jun3，邻Jun24→Jun16无Jun18；DeepMind Publications第1页30位置/266总9页，Sept22→2025Nov21跨窗，Jun25→Jun15无Jun18；RSS100items含具名Blog/RSS冲突 | 受阻 | Pubs本体2026年434条只有year/主题filter，无日级公开字段，不将全年变队列；有限日期补检未恢复日目录。GDM具体冲突隔离§5，不授该家族或Pubs全历史日覆盖 |
| SRC-META-AI | ai.meta.com/research与Blog直取失败/web无正文；research.facebook.com/publications重定向login/temporarily blocked；具名Jun18有限官方域补检无可靠日目录 | 受阻 | 当前原入口未恢复可核本日列表，不用旧recert或搜索无命中授零；按官方日目录/原始发布记录重开，隔离不支持完整覆盖 |
| SRC-QWEN | [article retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)完整40条无API分页，UI每次5为客户端More；双语身份/extra.date一致。Jun16 robotnav/world/manip/robotsuite→Jun22/23 agentworld，无Jun18条 | 已检查 | page_config两项500仅限制UI配置；当前集合不保证历史删项不存在 |
| SRC-DEEPSEEK | [news](https://www.deepseek.com/news/)完整Next posts16与实际runtime research固定31项，More仅展开已有数组；新闻Apr24→Sep10、研究Feb25→Jun24，均无Jun18目录项 | 已检查 | 当前目录展示日不重写原19348 arXiv旧归属；不宣全历史无删改 |
| SRC-MOONSHOT | 新主页Research链至[kimi.ai/blog](https://www.kimi.ai/blog/)，完整19卡，Apr20 K2.6→Jul16 K3/PerceptionBench跨目标 | 已检查 | 旧platform止2025不作2026证据；仅当前集合 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)实际所链publicList只读POST，page1/100/renderType0/zh返回code0,total11,list11；displayPublishTime邻May21 Hy-MT2→Jul6 Hy3，sole独立匹配 | 已检查 | 中文All11当前完整，无Jun18显示项，不保证历史删项不存在 |
| SRC-ZAI | 官方Research完整Next payload去重16身份（含featured复用）；Jun16 GLM5.2→Aug14邻界，无Jun18展示 | 已检查 | 不继承旧14计数或将embedded createAt改成首公开日；当前目录非全史保证 |
| SRC-BYTEDANCE-SEED | [Public papers](https://seed.bytedance.com/en/public_papers)首页界面1–20位置/247，实际18records，Oct25→May26；实际API page_token20再20条May26→Apr16。Blog type2/token0为12条Oct14→Feb13、next20再12条Feb12→2025Jul31，均order_desc=true、pinned未打乱日期；Jun23 Seed2.1→Apr23跨目标 | 已检查 | has_more=true但下一页已更早，不追全247/116；research pinned feed6不作完整目录。18524由arXiv有效层完成，不用目录展示日移归属 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)完整首页10卡，May9→Nov21,2025，明示更早2/2；无Jun18条目 | 已检查 | 当前按日降序列表已越过窗口，不扩更早页或沿GitHub组织全扫 |
| SRC-XIAOMI-MIMO | Paper8项；Blog runtime固定15项，More只8→15展开；逐官方页日期：Jun10 MiMoCode/Jun8 UltraSpeed/May30 Inference邻界，其余Apr/Mar及Sep；无Jun18 | 已检查 | UltraSpeed正文Jun23不替显示Jun8发布；当前固定数组不证明历史删改不存在 |
| SRC-MINIMAX | [中文博客](https://www.minimax.cn/blog)完整15卡，Jun9 MaxProof→Jul31 H3邻界，无Jun18条 | 已检查 | 仅当前中文目录；不泛称全部语言/删除历史 |
| SRC-ARXIV | 本日DataCite created四主题288+系统188+plural同义285联合499身份，registered469无新ID；registered系统87补compiler/inference/MoE亦无ID差。末秒至.999Z created/registered两差额JSON均0；官方CL小页100标题17354→19346、后邻19347有界补新命名，非逐项队列 | 已检查 | created仅发现；五真实早v1跨日未定归属不formal，见§5。不以catchup90日错误/partial月页/空响应授0或全学科召回 |

检查执行日2026-10-29，完整原件/查询self、分页与字段边界见[唯一补充记录](../_sources/daily-20260619/SUPPLEMENT_20261029.md#2-有限发现与停止点)及[独核R36–R73](../_sources/daily-20260619/SUP_REVIEW_20261029.md)。宽列表只导航，先题摘语义贡献与独立P/N校准，不按分类或499身份逐项闭队。旧590原小时窗审计保留为旧层，不授新增自然日覆盖。明确贡献N只保原始理由；有更正/反侧的19268/18831已定点重开，未以降分或改名清待办。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees](https://arxiv.org/html/2606.19376v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：Calibration 是在线 Routing State |
| [ClayBuddy: A Framework, Evaluation, &amp; Mitigation of Coding Agent Failures](https://arxiv.org/html/2606.19380v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Pre-execution Guardrail：检测 Off-task 不能等到副作用发生后 |
| [Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence](https://arxiv.org/html/2606.19386v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-MONITORING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MONITORING，[owner](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；纠正后正文锚点：Wall-clock Decay 的校准必须绑定 Action Cadence |
| [Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework](https://arxiv.org/html/2606.19390v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Agent authority BOM、channel coverage 与 executable PoV |
| [OpenRath: Session-Centered Runtime State for Agent Systems](https://arxiv.org/html/2606.19409v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-PLATFORM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[owner](../../../../books/part-07-agent/84-agent-platform.md)；命题锚点：Agent Definition 与 Run Identity（typed Session 主线） |
| [Deontic Policies for Runtime Governance of Agentic AI Systems](https://arxiv.org/html/2606.19464v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Policy-as-Data：可更新规则与模型判断必须分开版本化 |
| [FloatDoor: Platform-Triggered Backdoors in LLMs](https://arxiv.org/html/2606.19535v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：模型内部路由、训练数据与 Weight Repair 都进入攻击面 |
| [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](https://arxiv.org/html/2606.19544v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Scorer 不是绝对真相 |
| [Uncertainty Decomposition for Clarification Seeking in LLM Agents](https://arxiv.org/html/2606.19559v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-PLANNING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；命题锚点：先校准不确定性，再决定行动、询问或探索 |
| [IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows](https://arxiv.org/html/2606.19595v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Resume 的语义必须比“有 Checkpoint”更具体 |
| [StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns](https://arxiv.org/html/2606.19613v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；正文锚点：Long-session Stamina 必须测量状态如何累积失效 |
| [CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference](https://arxiv.org/html/2606.19667v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：Structured knowledge 只有进入 physical access plan 才改变 KV 成本 |
| [When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems](https://arxiv.org/html/2606.19692v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents](https://arxiv.org/html/2606.19704v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Open-world Evaluation 必须重复发生，而不是一次验收 |
| [Closing the Operational Gap in Semantic Caching](https://arxiv.org/html/2606.19719v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：语义 Cache 的发布标准必须绑定工作点，而不是只看排序分数 |
| [SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL](https://arxiv.org/html/2606.19746v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：分布式 Prefix KV 是带复制与新鲜度的 materialized state |
| [Grounded Inference: Principles for Deterministically Encapsulated Generative Models](https://arxiv.org/html/2606.19753v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-PRODUCTION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-PRODUCTION，[owner](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)；命题锚点：Production Contract |
| [SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling](https://arxiv.org/html/2606.19755v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-SPECULATIVE-DECODING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；命题锚点：当 Draft 可能优于 Target，系统进入效用仲裁分支 |
| [Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI](https://arxiv.org/html/2606.19769v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-EMBODIED-VLA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；正文锚点：机器人经验要跨设备、任务与时间复用时 |
| [Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases](https://arxiv.org/html/2606.19803v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：Policy-aware ANN 必须先确定可见集合再优化近似召回 |
| [Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning](https://arxiv.org/html/2606.19808v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：当前 Confidence 不等于继续计算的 Residual Value |
| [ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference](https://arxiv.org/html/2606.19849v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：异质 DAG 需要 Readiness、Residency 与 Deadline 共享一条控制链 |
| [A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models](https://arxiv.org/html/2606.19868v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Calibration Slice 必须包含 Language × Model Scale × Estimator Contract |
| [Multi-Agent Transactive Memory](https://arxiv.org/html/2606.19911v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：共享 Memory 需要分离选择性写入、访问权与事实状态 |
| [Online Dynamic Batching with Formal Guarantees for LLM Training](https://arxiv.org/html/2606.19989v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DISTRIBUTED-TRAINING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[owner](../../../../books/part-04-training-system/36-distributed-training.md)；正文锚点：Variable-length Batch 让并行计划成为 Runtime State |
| [Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services](https://arxiv.org/html/2606.19992v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-MCP 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MCP，[owner](../../../../books/part-07-agent/83-mcp.md)；正文已落实：从静态 Endpoint 到受限 Tool Program |
| [StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation](https://arxiv.org/html/2606.20005v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：通用 Module Replacement 与专用 Structural Fusion |
| [When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents](https://arxiv.org/html/2606.20023v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-TOOL-CALLING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Disclosure Minimization 不能替代 Authorization |
| [When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation](https://arxiv.org/html/2606.20113v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-TOOL-CALLING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；正文锚点：Tool Admission 与 Interaction Latency 必须分开控制 |
| [The Correctness Illusion in LLM-Generated GPU Kernels](https://arxiv.org/html/2606.20128v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：Kernel Verification 需要从孤立输入扩展到 Model–Kernel Interface |
| [N-Version Programming with Coding Agents](https://arxiv.org/html/2606.20158v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Evaluator-Driven Search：可执行反馈如何变成 Workflow |
| [Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference](https://arxiv.org/html/2606.20245v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-CONTEXT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[owner](../../../../books/part-07-agent/75-context.md)；命题锚点：Context Assembly Pipeline |
| [Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic](https://arxiv.org/html/2606.20254v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：Quantization 是新的 Security Revision |
| [ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters](https://arxiv.org/html/2606.20374v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-TRACE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[owner](../../../../books/part-06-ai-infrastructure/69-trace.md)；命题锚点：跨层 Trace 只能提出因果候选，不能自动证明根因 |
| [Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe](https://arxiv.org/html/2606.20381v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 TRAIN-PRETRAINING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；命题锚点：Precision Policy 应沿误差传播路径分区 |
| [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：Quantization Objective 应对齐 Attention Distortion |
| [Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems](https://arxiv.org/html/2606.20487v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Recovery 与 Verification 必须产生不同 Artifact |
| [Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems](https://arxiv.org/html/2606.20493v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点：同根报告可以帮助读懂证据，却不能按独立观察累加 |
| [Efficient and Sound Probabilistic Verification for AI Agents](https://arxiv.org/html/2606.20510v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；正文锚点：概率 Verification 的 Bound 是有前提的验收合同 |
| [Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes](https://arxiv.org/html/2606.20520v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Agent 授权必须沿 Delegation Chain 单调收窄 |
| [LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents](https://arxiv.org/html/2606.20529v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：Persistent Memory 需要显式状态操作，而不只是 Record |
| [The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation](https://arxiv.org/html/2606.20536v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：评测结果属于完整 Runtime Identity |
| [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/html/2606.20537v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 INFER-REQUEST-LIFECYCLE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-REQUEST-LIFECYCLE，[owner](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)；正文锚点：Graph-bound Execution State 需要独立的 Restore Contract |
| [Current World Models Lack a Persistent State Core](https://arxiv.org/html/2606.20545v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：World Model 评测要分离三种结论 |
| [From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning](https://arxiv.org/html/2606.20553v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：训练态共享统计也是隐私通道 |
| [MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/html/2606.20562v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-EMBODIED-VLA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory |
| [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/html/2606.19348v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | 百万 token workload 把 compressed attention、KV tiering、context parallelism 与可恢复 rollout runtime 放进同一约束链，需复核既有长上下文 joint contract；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；现有正文已同时约束模型结构、状态布局与运行时 |
| [Granularity-Regulated Adaptive Computational Efficiency for Optimal Verification in Test-Time Scaling](https://arxiv.org/html/2606.19354v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | 固定 ORM/PRM 在 verifier accuracy、任务难度和预算变化时不再总是最优，系统需要调度 verification granularity；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：`Verification Granularity 也是可调度的计算状态` |
| [Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?](https://arxiv.org/html/2606.19388v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | mobile agent 的 GUI/CLI 选择改变 observation/action contract，但受限于 terminal-reachable state，需复核 interface owner；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；现有 interface-granularity 主线已覆盖 |
| [A Survey of Full-Duplex Spoken Dialogue Systems: Architectural Hierarchy, Interaction Ontology, and Decision State Machine](https://arxiv.org/html/2606.19453v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | full-duplex 需要分离架构层级、交互类型与逐时刻决策状态，不能以单一“支持双工”标签替代系统能力；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；在线状态路由正文已覆盖 |
| [Diffusion Language Models: An Experimental Analysis](https://arxiv.org/html/2606.19475v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | DLM 的质量—效率判断随 denoising steps、block、context 与 unmasking policy 改变，不能形成脱离合同的范式排名；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；现有条件化比较已覆盖 |
| [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/html/2606.19531v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | 若 action expert 可直接读取 image-editing denoiser 的中间 KV，完整未来视频不再是 world-action handoff 的必要边界；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；`World-action model` 已承载 latent predictive interface 与 physical commit boundary |
| [Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment](https://arxiv.org/html/2606.19558v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | KLD/PPL 在明显退化区可粗筛，却在 near-baseline silent zone 失去部署排序能力，量化发布 Gate 需分层；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；compression gate 与 threshold-adjacent churn 已承载 proxy 边界 |
| [Which Pairs to Compare for LLM Post-Training?](https://arxiv.org/html/2606.19607v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | preference label budget 不只影响数据量，pair sampling design 会改变信息覆盖与 DPO policy gap；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-DPO，[owner](../../../../books/part-04-training-system/34-dpo.md)；正文锚点：`Preference Pair 选择是实验设计，不只是数据量选择` |
| [Hard or Just Unreached? Diagnosing the Sampling Blind Spot in Math-Reasoning Difficulty Estimation](https://arxiv.org/html/2606.19636v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | pass@k=0 混合“普通采样未到达”与“模型不可解”，会污染 difficulty、curriculum 和 verifier-data 判断；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；现有 pass@k 非不可能性证明主线已覆盖 |
| [Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization Across Preference Settings](https://arxiv.org/html/2606.19744v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | sequential DPO 的变化依赖 objective compatibility、signal strength 与顺序，aggregate forgetting 无法拥有 release verdict；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DPO，[owner](../../../../books/part-04-training-system/34-dpo.md)；正文锚点：`Sequential DPO 必须保留目标关系与训练顺序` |
| [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](https://arxiv.org/html/2606.19919v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | fast/slow reasoning 的效率 credit 可只绑定 mode-selection action，避免把后续正确长轨迹一并惩罚；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；typed credit / state-action boundary 已覆盖该二元实现案例 |
| [VIMPO: Value-Implicit Policy Optimization for LLMs](https://arxiv.org/html/2606.20008v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | policy/reference log-ratio 可构造 policy-implied value，在 group baseline 与 learned critic 之间形成新的 credit-assignment 分支；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；正文锚点：`Policy-implied Value 是 Group Baseline 与 Learned Critic 之间的条件分支` |
| [What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis](https://arxiv.org/html/2606.20075v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | latent reasoning 同时有 optimization-path gradient attenuation 与 representation drift，trajectory/space supervision 解决不同失败轴；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；正文锚点：`Latent Reasoning 要分开路径优化与表示空间约束` |
| [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/html/2606.20092v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | 长时 VLA 必须在瞬态证据消失前决定写入，预测性 keyframe owner 与 action policy 应分离；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；正文锚点：`瞬态视觉证据需要在消失前完成写入决策` |
| [HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization](https://arxiv.org/html/2606.20097v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | hybrid attention 可按 head 而非 layer 分配 full/linear attention，但证据只来自单一 compact dense model；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；现有 head-level hybrid routing 已覆盖 |
| [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/html/2606.20104v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | inverse dynamics 能阻止 constant latent collapse 并保留 action-controllable information，但依赖动作可由观测转移恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；正文锚点：`Inverse Dynamics 是有前提的 Anti-collapse Regularizer` |
| [Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families](https://arxiv.org/html/2606.20225v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | within-model causal probe 与 cross-model mapped direction 必须分开验收；行为变化但 control specificity 不足时不能升级为 transferable monitor；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；正文锚点：`Learned Security Sensor 与 Reference Monitor 必须分层` |
| [How Transparent is DiffusionGemma?](https://arxiv.org/html/2606.20560v1) | 2026-06-19T08:00:00+08:00 ～ 2026-06-19T09:00:00+08:00 | 可干预 token bottleneck 只支持 variable transparency；不能据此推出 algorithmic transparency 或完整 monitorability；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；正文锚点：`Transparency 不是单一的“可解释程度”` |

| [On the Residual Scaling of Looped Transformers: Stability and Transferability](https://arxiv.org/html/2606.18524v1) | 2026-06-18 | tied-loop相关累积要求独立于depth的缩放/LR条件；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[owner](../../../../books/part-02-model/17-transformer-layer.md)递归计算段后，共享ReLU分支与depth/loop分轴条件 |

| [RegMix-D: Dynamic Data Mixing via Proxy Training Trajectories](https://arxiv.org/html/2606.18663v1) | 2026-06-18 | proxy next-loss的局部预测区分offline递归与online实际观测；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)Data Control Plane后，proxy轨迹与量尺/时钟交接 |
| [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/html/2606.18589v1) | 2026-06-18 | 同phase imagined/observed latent匹配选择已有chunk，暴露恢复支持与延迟条件；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)闭环时间尺度后 |
| [The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs](https://arxiv.org/html/2606.18656v1) | 2026-06-18 | 配对证据在不同群体cue下被否定的条件反证，须保contrast能力分母；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)公平配对评价段后 |

| [Output Vector Editing for Memorization Mitigation in Large Language Models](https://arxiv.org/html/2606.18767v1) | 2026-06-18 | 固定activation的rank-one writer更新改变相关readout投影，非记忆擦除；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-FFN，[owner](../../../../books/part-02-model/16-feed-forward-mlp.md)reader/writer coupling后 |
| [Reinforcement Learning Towards Broadly and Persistently Beneficial Models](https://alignment.openai.com/beneficial-rl/) | 2026-06-18 | trait奖励的域外正向迁移与harmful/helpful steering分责；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)暖启×reward反证后 |
| [Project Fetch: Phase two](https://www.anthropic.com/research/project-fetch-phase-two) | 2026-06-18 | coding/setup提速不授physical closed-loop完成的具体反证；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)action deadline与fast policy/slow reasoner分权 |

| [Sparsity Curse: Understanding RLVR Model Parameter Space from Model Merging](https://arxiv.org/html/2606.18521v1) | 2026-06-18 | sparse taskdelta不授可合并，符号冲突区域用校准敏感度仲裁；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-CHECKPOINT，[owner](../../../../books/part-04-training-system/35-checkpoint.md)Adam历史统计合并段后 |
| [Skill-Guided Continuation Distillation for GUI Agents](https://arxiv.org/html/2606.18890v1) | 2026-06-18 | policy实际偏轨状态的续接监督，失败前史可见而不模仿；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-SFT，[owner](../../../../books/part-04-training-system/29-sft.md)恢复训练与OpenMobile/TILDE段 |
| [Compute Efficiency and Serial Runtime Tradeoffs for Stochastic Momentum Methods](https://arxiv.org/html/2606.19179v1) | 2026-06-18 | gradient-query CE与serial steps的受限谱下界，非已验LM最优batch；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)Batch/tokens/steps与critical batch段 |
| [When Does Trajectory-Level Supervision Permit Efficient Offline Reinforcement Learning?](https://arxiv.org/html/2606.18531v1) | 2026-06-18 | state-action覆盖不保证非线性整轨迹标签的信息可识别性；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)反馈通道与IRL示范之间 |
| [Explaining Attention with Program Synthesis](https://arxiv.org/html/2606.19317v1) | 2026-06-18 | 可执行attention surrogate须分拟合、替换与行为验收；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-MULTI-HEAD-ATTENTION，[owner](../../../../books/part-02-model/15-multi-head-attention.md)统计诊断与固定head身份之间 |
| [Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning](https://arxiv.org/html/2606.18831v1) | 2026-06-18 | 合成数据/中等pass筛选与generic coherence PRM的受控反侧；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)数据制备与难度筛选；TRAIN-GRPO仅作judge反侧支持 |
| [Patnaik-Pearson intrinsic dimension for internal representations of neural networks](https://arxiv.org/html/2606.19268v1) | 2026-06-18 | 谱参与率与operator几何解释的具体命题，但乘积收缩证明桥未闭；2 + 1 + 2 = 5 | 争议 | 暂缓：乘积/attention一般解释不入Books，见具名重开条件 |
| [Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos](https://arxiv.org/html/2606.18955v1) | 2026-06-18 | mask-guided双码运动监督与intent/current-state消费分离；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)共享/私有码后 |
| [MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data](https://arxiv.org/html/2606.18485v1) | 2026-06-18 | text/old encoder/alignment cursor跨句状态与soft prior；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)音频history分路之前 |

| [PAIWorld: A 3D-Consistent World FoundationModel for Robotic Manipulation](https://arxiv.org/html/2606.18375v1) | 2026-06-18 | pose/ray位置条件与冻结3D关系目标分责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)19979后/rectifier前 |
| [Dense Holographic Associative Memories](https://arxiv.org/html/2606.18492v1) | 2026-06-18 | 正交码全局softmax的物理接口与实际装置边界；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)20662完整段后/KV重算前 |
| [Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient Multimodal On-Policy Self-Distillation](https://arxiv.org/html/2606.19120v1) | 2026-06-18 | 分段teacher特权context与invalid整段fallback；2 + 1 + 3 = 6 | 深入完成 | 整合：TRAIN-SFT，[owner](../../../../books/part-04-training-system/29-sft.md)18734后/19327前 |
| [Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation](https://arxiv.org/html/2606.19327v1) | 2026-06-18 | criteria先生成再作为teacher私有context的蒸馏接口；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT，[owner](../../../../books/part-04-training-system/29-sft.md)19120后/31918前 |
| [Learning User Simulators with Turing Rewards](https://arxiv.org/html/2606.19336v1) | 2026-06-18 | 内容相似与真人不可区分性必须分开；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)humanlike参照与SimulatorArena段 |
| [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision–Language–Action Models](https://arxiv.org/html/2606.19297v1) | 2026-06-18 | 文字读出/简单物理选择与layoutpair分母；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)14885后/14773前 |
| [HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification](https://arxiv.org/html/2606.18671v1) | 2026-06-18 | trace派生interactive evidence与live replay/历史证据分责；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-TRACE，[owner](../../../../books/part-06-ai-infrastructure/69-trace.md)21347后/LinearTrace前 |
| [Beyond Safe Data: Pretraining-Stage Alignment with Regular Safety Reflection](https://arxiv.org/html/2606.19168v1) | 2026-06-18 | segment后自评/EOS格式须跨训练阶段继承；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)SGTM后/梯度归一化次序前 |
| [Sumi : Open Uniform Diffusion Language Model from Scratch](https://arxiv.org/html/2606.19005v1) | 2026-06-18 | allocated/active/scored canvas与visible随机尾的采样身份；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)17999后/cyclicpad前 |
| [Dual Dimensionality for Local and Global Attention](https://arxiv.org/html/2606.18587v1) | 2026-06-18 | 近原表示/远逐token bottleneck与共同投影分责；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)10406后/Selector进入Forward前 |
| [STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability](https://arxiv.org/html/2606.19236v1) | 2026-06-18 | sign×sampled-surprisal重权与batch词表entropy gate分责；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)09782后/min-p前 |
| [REVES: REvision and VErification–Augmented Training for Test-Time Scaling](https://arxiv.org/html/2606.18910v1) | 2026-06-18 | GT成功链提供恢复状态、fresh单turnRL重新分配信用；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)17775后/外部伪标签段前 |
| [SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG](https://arxiv.org/html/2606.18381v1) | 2026-06-18 | learned attention二叉层级与跨粒度beam预算；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)MoM后/标题归因段前 |
| [Lost in a Single Vector: Improving Long-Document Retrieval with Chunk Evidence Aggregation](https://arxiv.org/html/2606.18781v1) | 2026-06-18 | 局部编码后query-independent聚合仍保单vector接口；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)29519后/OBLIQ前 |
| [GraphPO: Graph-based Policy Optimization for Reasoning Models](https://arxiv.org/html/2606.18954v1) | 2026-06-18 | 候选等价class共享终局估值与incoming/outgoing信用分权；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)ROSE后/TGPR前 |
| [Enhancing Multilingual Reasoning via Steerable Model Merging](https://arxiv.org/html/2606.19002v1) | 2026-06-18 | runtime复合artifact须保encoder/bridge/consumer而非静态merge；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-CHECKPOINT，[owner](../../../../books/part-04-training-system/35-checkpoint.md)DCR后/taskvector前 |
| [Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams](https://arxiv.org/html/2606.19111v1) | 2026-06-18 | shared-R0配对及flat/matched随机基线、恢复破坏分母；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)23213后/Coordination Tax前 |

## 4. 证据与知识整合

本轮新增arXiv日期以精确身份/唯一v1 history、适用公告日程及同DOI `arxiv.content/findable/registered`组成有限联合界，整段均在BJT Jun18；原始题摘仅作发现，采用锁定v1。原件为本日SUP_DATACITE_TOPIC/SYSTEM/SYNONYMS/REGISTERED JSON及各SUP_BODY，独立日期层已逐身份核验；当前官方事件页的具名撤回/更正信号已定点处理，不用created或Submitted单项替代公开日。

### [PAIWorld: A 3D-Consistent World FoundationModel for Robotic Manipulation](https://arxiv.org/html/2606.18375v1)

精确v1 §3–5/Eq1–12/T1–4必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。GeoRoPE与DA3关系监督是两条接口，不授硬几何或必要充分；四格消融只局部，WorldArena多项反退，Geometric指标箭头与文字方向冲突。14B、2.5M视频、200H200/30K步的作者配置不授实机规划，全部预训练/几何提取与动作回归计费。原MULTIMODAL-WORLD-MODELS实际相邻论点尚未承载“pose/ray位置条件与冻结3D关系目标分责”，现已在19979后/rectifier前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Dense Holographic Associative Memories](https://arxiv.org/html/2606.18492v1)

精确v1 §2–5/Eq2–13必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。理想正交code给Kᵀx→全局softmax→V关联读出，但容量受可用code数/光学串扰限制。实际只测single-cell写入/存储/衰减，未造完整调制/非线性/readout系统；cell功耗排除probe/readamp，不采用LLM吞吐、部署或全系统省费。原INFER-TENSORRT-LLM实际相邻论点尚未承载“正交码全局softmax的物理接口与实际装置边界”，现已在20662完整段后/KV重算前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient Multimodal On-Policy Self-Distillation](https://arxiv.org/html/2606.19120v1)

精确v1 §2–5/A/C/E.2必要证据及独立核验完成，2 + 1 + 3 = 6，具体gap触发深入。同一student prefix下，description teacher只外部image，reasoning/answer另有特权；description有效用forwardKL，invalid整段reverseKL，错误答案仍可格式有效。Vision-SR1-47K、3/7B/8A100/LoRA64有限对照中PALR构造及有效筛选人口、Avg/Pass5与任务反退须分开，不能授全shortcut消除或faithfulness；生成/teacher/训练全计费。原TRAIN-SFT实际相邻论点尚未承载“分段teacher特权context与invalid整段fallback”，现已在18734后/19327前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation](https://arxiv.org/html/2606.19327v1)

精确v1 §2–3/T1–6/A/C.2/D必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。StageI以reference生成rubric，StageII teacher读criteria而student只原题，非部署必用rubric。直接14B生成与generic/random rubric均有强正侧，generator不是已证必要；正文reference补偿与rubric-only context口径未齐，不拼完整recipe。固定teacher/100次reasoner对500×4GRPO不等总费，TV交叉熵界不授任务收益。原TRAIN-SFT实际相邻论点尚未承载“criteria先生成再作为teacher私有context的蒸馏接口”，现已在19120后/31918前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Learning User Simulators with Turing Rewards](https://arxiv.org/html/2606.19336v1)

精确v1 §2–6/Limitations/C.3/D.1–D.7必要证据及独立核验完成，2 + 1 + 2 = 5，标准审阅。history/target disjoint、heldout-user的Qwen3-8B有限训练，Turing reward与相似度不是同一评价目标。human Chat局部显著，Reddit对Sim未显著，不能认证真人替代。cap印式最大2/3非文称1、GT长度罚/混合judge身份与修改版logprob基线均限制归因；全文人评prompt不需无差别重读，未授防hack。当前Ch66的humanlike参照与SimulatorArena实际承载该有限采用，具体NC通过，不为同主题造diff。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision–Language–Action Models](https://arxiv.org/html/2606.19297v1)

精确v1 §3–5/T1–3/A/E/F必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。1720二元items/3440成对换位episodes分目标/错误/OOB；简单动作仍混感知/指令/控制，SR近随机不证明知识擦除。最好跨层probe不等causal usage，换位不是独立样本；正文board yes/no与AppA letter协议不一，tile/prompt/分辨率反退及全部执行/probe/搜索费保留。原PLATFORM-EVALUATION-SYSTEM实际相邻论点尚未承载“文字读出/简单物理选择与layoutpair分母”，现已在14885后/14773前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive Verification](https://arxiv.org/html/2606.18671v1)

精确v1 §4–9/T2/study protocol必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。final-answer选page/snippet会漏废弃分支反证；BrowserView重放当前网页不是immutable历史快照，人工改filter是新交互。14×8固定顺序人评中准确率p=.29未显著，时间仅88correct子人口，错误32.1%仍被信任；抽取precision不授recall，重放权限为项目推断，原trace/网络/人工全计费。原PLATFORM-TRACE实际相邻论点尚未承载“trace派生interactive evidence与live replay/历史证据分责”，现已在21347后/LinearTrace前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Beyond Safe Data: Pretraining-Stage Alignment with Regular Safety Reflection](https://arxiv.org/html/2606.19168v1)

精确v1 §3–7/T1–7/B/C必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。采用片段后guard标签、unsafe后EOS与SFT/finetune格式接口，不采中心安全倍率。prefill/GCG及finetuning攻击的启发式标签与内容judge AND使自标签直接影响ASR；不泛掉AutoDAN独立classifier。rawfinetune失效、600B对100B非matched与能力反退均保，EOS不撤回已发内容，标注/训练/独立内容攻防全计费。原TRAIN-PRETRAINING实际相邻论点尚未承载“segment后自评/EOS格式须跨训练阶段继承”，现已在SGTM后/梯度归一化次序前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Sumi : Open Uniform Diffusion Language Model from Scratch](https://arxiv.org/html/2606.19005v1)

精确v1 §2–5/Limitations/T1–2必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。原生7B约1.55T uniform-noise diffusion提供有限可行性，非等数据/AR优越性；EOS/BOS不是attention隔离，随机tail仍影响内容。30题×4task的canvas探针、GSM k2反退、A→B→A修订不获益和全canvas费用保留。v1确有projectlink；有限shell/bundle恢复未见具体早日期信号，不宣全历史无早稿，也不推翻合法联合日证。原MULTIMODAL-GENERATIVE-PARADIGMS实际相邻论点尚未承载“allocated/active/scored canvas与visible随机尾的采样身份”，现已在17999后/cyclicpad前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Dual Dimensionality for Local and Global Attention](https://arxiv.org/html/2606.18587v1)

精确v1 §2–3/5/T1–4必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。DAR近窗原hidden、远down/up后共享WK/V，所有合法token仍同attention，升维不恢复信息。70–410M/10BPile及OLMo1B适配对照须保uniform reduction、160M与极窄任务反退；实际双KV使cache加倍，on-demand/absorption/Flash/vLLM是future，不采用HBM或净速。原MODEL-LONG-CONTEXT实际相邻论点尚未承载“近原表示/远逐token bottleneck与共同投影分责”，现已在10406后/Selector进入Forward前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability](https://arxiv.org/html/2606.19236v1)

精确v1 §2–6/C/B.5/B.8必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。正负advantage人口内surprisal分位数不是各位置完整entropy；目标entropy只门控正权，不接管verifier。B.8高/低target相对0.3回退但仍胜该表GRPO，W≥2发散；独立logit近似不授共享参数/clipping/Adam精确方向，不采用E/F稳定理论。多数†外部baseline非matched，更多反思词不证明深推理，rollout/排序/搜索全计费。原TRAIN-GRPO实际相邻论点尚未承载“sign×sampled-surprisal重权与batch词表entropy gate分责”，现已在09782后/min-p前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [REVES: REvision and VErification–Augmented Training for Test-Time Scaling](https://arxiv.org/html/2606.18910v1)

精确v1 §3–5/A/B/E/F.1–F.3必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。只保非首答成功的最终成功链，排首答正确/全失败，固定状态上重新采样回答做RL而非模仿错误或广播terminal信用；epoch刷新。C1覆盖/C2逐状态不退及occupancy漂移条件不能由平均收益替代，TailConfidence符号/描述未齐不作停止recipe。one-shot/SC反退、8H200三轮30h2m含8h58m生成、future异步与全部费保留。原TRAIN-GRPO实际相邻论点尚未承载“GT成功链提供恢复状态、fresh单turnRL重新分配信用”，现已在17775后/外部伪标签段前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG](https://arxiv.org/html/2606.18381v1)

精确v1 §3–4/Eq1–12/Alg1/T1–3/Limitations必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。head-layer加权attention对称化、max-link merge固定树，递归父均值非等叶权且可非连续；query不能重组织树。30KCLaRa/1.3B/8A100/3run消融有限，硬merge不授完整可微recipe；按展开底层unit而非node计预算，recall/更重系统质量反侧、离线/输出排除与全部费保留。原AGENT-RAG实际相邻论点尚未承载“learned attention二叉层级与跨粒度beam预算”，现已在MoM后/标题归因段前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Lost in a Single Vector: Improving Long-Document Retrieval with Chunk Evidence Aggregation](https://arxiv.org/html/2606.18781v1)

精确v1 §2–4/T1–4/Limitations/A.2/C.2必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。frozenencoder分token块/local position reset/mean保原query与cosine/onevector索引，并非chunk search。4backbone/bf16A6000、过小chunk/max/topnorm与部分task反退，离线3–4×/overlap80vs43min；EDI有margin筛人口及Table3/6与文字方向争议，隔离普遍机制验证而保有限干预，不授无损或净效率。原AGENT-RAG实际相邻论点尚未承载“局部编码后query-independent聚合仍保单vector接口”，现已在29519后/OBLIQ前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [GraphPO: Graph-based Policy Optimization for Reasoning Models](https://arxiv.org/html/2606.18954v1)

精确v1 §4–5/A3/A5/F.1/G/H必要证据及独立核验完成，2 + 2 + 2 = 6，具体gap触发深入。各prefix保真实生成边，后续终局成功率含失败分母共享；到同class路径长度与从相似状态离开两组分责。cosineκ不授value-stable类/独立不重叠续写假设，跨路径误合不由父子novelty自动纠正；w与κ反侧、16H20/350steps与close-token非全费均保，不采用F普遍无偏/PRM/最短路理论。原TRAIN-GRPO实际相邻论点尚未承载“候选等价class共享终局估值与incoming/outgoing信用分权”，现已在ROSE后/TGPR前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Enhancing Multilingual Reasoning via Steerable Model Merging](https://arxiv.org/html/2606.19002v1)

精确v1 §3–4/T1–4/Limitations/A.2T8必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。mT5末层经映射，目标HB只Embedding而非先跑完整reasoner，crossattention/languageID产生两路1+tanh正权并拼decoder输入。四A100/3epoch/3seed且限mT5+Llama2MetaMath，语言反退与tSNE非因果；T8相同舍入总时不授零开销，w/oGate57.3/56.9口径不齐不拼收益，驻留/编码/桥接/扩展输入全计费。原TRAIN-CHECKPOINT实际相邻论点尚未承载“runtime复合artifact须保encoder/bridge/consumer而非静态merge”，现已在DCR后/taskvector前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。

### [Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams](https://arxiv.org/html/2606.19111v1)

精确v1 §3–6/8/B.5–B.9必要证据及独立核验完成，2 + 1 + 2 = 5，具体gap触发深入。三人同信息按task/seed复用generated-once初答，先比vote再flat与相同动作/频率随机控制；净收益分初错恢复与初对破坏。仅一model×social组合正侧，MATH flat更好；3/5seed重复不增加unique题数，不同probe初答不合并，社会gold非普遍事实，不授领导理论必要充分或唯一因果，所有消息/重开全计费。原AGENT-MULTI-AGENT实际相邻论点尚未承载“shared-R0配对及flat/matched随机基线、恢复破坏分母”，现已在23213后/Coordination Tax前窄整合，完整自读及sole实际POST通过。完整原证据与稿核见[唯一补充记录§8](../_sources/daily-20260619/SUPPLEMENT_20261029.md#8-同义差额第一必要与owner判断)；未核代码执行或复现。


### [Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos](https://arxiv.org/html/2606.18955v1)

精确v1 III–V/TablesI–II，6分因具体gap深入。固定时距frame pair经双query/codebook与mask-guided三路重构形成运动标签，冻结codec监督VLM，目标action expert另消费intent hidden、当前DINO/proprio；mask不是语义纯解耦证明。LIBERO用AR head、RoboTwin用flow协议分别保留；部分任务反退、不可恢复topple及fine-control容量不足，domain PCA剥离后CKA不授语义因果。Ch26共享/私有码只分原生本体分量，原文未承载该无动作视频producer与新观察消费者接口，已窄写两段并sole实际POST通过。预训练无原生动作标签仍需mask与目标机器人示教，codec、mask、两阶段训练、独立视觉与动作expert和真实回归全付费；60Hz名义部署不授完整控制deadline。

### [MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data](https://arxiv.org/html/2606.18485v1)

精确v1 §§2–4/Eq1–3/Tables1–2，5分因状态接口gap深入。末K文本、对应旧encoder状态和alignment cursor跨句继承，soft-logprior保远位置非零，不等通用decoder KV复用。20英文3–4分钟段、单A6000、T.7/eps.1/lambda1/CFG2.5，Whisper/WavLM/TitaNet/UTMOS均代理；缺同模型组件消融、人耳与RTF，能量较好不代表F0或全部声纹领先。Ch24已有latent历史分路，未承载text/encoder/cursor这份交接，已在音乐双history前窄写两段并sole实际POST通过。全部编码/生成、历史驻留、prior调参与完整波形验收计费，不授任意TTS免训或无限一致性。

### [Patnaik-Pearson intrinsic dimension for internal representations of neural networks](https://arxiv.org/html/2606.19268v1)

精确v1 §§3.3/4.1/4.3–4.5，5分因中心证明争议深入。PP为demeaned表示的奇异值参与率，不等语义信息量；operator解释具有准入增量，先前仅descriptor的N已纠正。v1由general position直接取Gaussian Q、由expected Gram推出actual spectrum未闭。当前v4 comments指名Theorem4.1 proof，故仅定点核§4.3：随机正交、ensemble期望与渐近条件不能反灌v1；Eq48将free x,y的τ(x²y²)写成错误混合矩，证明令自身方差为零，上界亦未解释相关entries如何获得所引用iid谱结论。保有效定义/不变性与softmax无一般关系，不泛断全稿错误。sole独核确认该中心争议；乘积收缩及依赖attention解释均不作正证、不进Books。重开只需明确随机/极限条件并修复moment、谱/集中桥的原始更正或独立证明。v1 Jun17 16:44:32Z与arxiv.content/findable registered Jun18 02:11:17Z的合法同日联合已核，不因争议改分或移动归属。

### [When Does Trajectory-Level Supervision Permit Efficient Offline Reinforcement Learning?](https://arxiv.org/html/2606.18531v1)

精确v1 §§2–5与Appendix E.2完整反例证明，7分深入。加法return标签不等整条全对才给一的非线性目标；确定性状态链、均匀二元动作和唯一正确动作串使marginal state-action coverage为2，而trajectory coverage为2^H，TV与Le Cam链说明有限监督模型下的指数区分困难。只采用此分离，不移植完整OPAC速率或推广到LLM。原理论还需iid离线Markov、realizability与Bellman条件；标签产生、全部采样和回归均计费。Ch31现有反馈信息段不承载该具体分离，已在用时反馈后、IRL示范前窄写两段；sole完整PRE及实际POST通过。本地HTML档案不完整，但必要核心及E.2已从官方精确HTML完整读取，不声称全附件审阅或复现。

### [Explaining Attention with Program Synthesis](https://arxiv.org/html/2606.19317v1)

精确v1 §§2–3/5，6分因实际解释接口缺口深入。map摘要→模型生成Python→运行与一次修订→JSD/IoU选择不认证唯一算法；替换仅attention矩阵，V与后续网络仍在。TinyStories同分布PPL与六选择题任务是不同人口，BERT较难、低拟合head和pruning替代解释保留；未测加速或完整生成等价。Ch15统计诊断/activation干预未承载可执行surrogate的fit—replacement—behavior分责，已窄写两段并sole真实POST通过。全部map测量、程序搜索/执行、替换forward和非目标回归均计费；不授可读程序即机制真值。

### [Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning](https://arxiv.org/html/2606.18831v1)

精确v1 §§3–5/Tables2–4/Limitations，5分标准。八数据家族的合成/证据扩展与中等pass筛选构成训练人口，不是三类任务必要充分定理；Qwen3-4B固定50steps添加generic coherence PRM时平均57.58→56.29，但LBv2 44.63→44.83，不能说全任务退或PRM普遍无用。judge采用max(EM,judged)需保评价口径；固定steps不等生成、teacher过滤、rollout和训练总费相同。Ch27 QA-evidence制备与moderate-pass筛选、task×length mixture已承载拟采用recipe；Ch33明确coherence proxy不是grounding及其反退，sole必要与实际owner对读确认已有覆盖，故不为此新增Books。

### [Sparsity Curse: Understanding RLVR Model Parameter Space from Model Merging](https://arxiv.org/html/2606.18521v1)

精确v1 §§3–7/Eq12–16/Tables1–5深入7分。共base的反向conflict与private增量是不同处理域；校准数据上分别计算两源模型的经验对角敏感度，再仲裁符号冲突，不等历史Adam统计或真实知识位置。bf16/1e-5阈值不认证未改字节，二维activation KDE也不是weight loss landscape的因果证据。7B MATH全部低于naive parent平均，Math+Code合并的代码仍低于coder parent；SFT/RL源训练未完全匹配。Eq15只显式写private part，完整拼回不作为已核可执行配方。Ch35原历史统计producer没有这条fresh-conflict分责及sparse-RLVR反证，现窄写两段、自读并sole实际POST通过；未核代码/复现，全源训练、校准、搜索与各parent能力回归均付费。

### [Skill-Guided Continuation Distillation for GUI Agents](https://arxiv.org/html/2606.18890v1)

精确v1 §§4–5、Limitations/AppA/H/I标准6分。plain policy在线重执行前k动作，当前状态交skill-guided producer；只收recoverable且verifier+judge通过的续接，loss仅posthandoff，部署不携skill。前史不监督与多k固定窗口均有支持条件：晚窗整体低于早窗而非严格单调，full-window45.7还含更多数据，不能授纯覆盖因果。142失败任务的continuation success不是全任务成功率；64H100/bf16/三backbones、hardtask续接有限和环境重执行开销均保留。Ch29“恢复训练可看见失败历史，但不模仿失败动作”及TILDE已具体承载learner偏轨、expert恢复、前史context/target分责与成功过滤人口，固定k+skill只是该接口实例；sole实际owner与必要核后NC，不增加书稿。

### [Compute Efficiency and Serial Runtime Tradeoffs for Stochastic Momentum Methods](https://arxiv.org/html/2606.19179v1)

精确v1 §§3–6/Theorems1–2/Corollaries1–2标准6分。consistent noiseless Gaussian、online freshbatch线性回归，compute是gradient queries；HB/ASGD的谱半径下界分开serial步数和总查询数，不把下界饱和视为已证明可达risk或最优batch。formal risk extension和matching upper bounds留future。D50000/N500000、a2、50seed和LR/beta/zeta完整grid只为合成对照，非LM墙钟或生产recipe。Ch28 Batch/tokens/optimizer steps和critical batch段已具体区分这些计量、硬件效率与全搜索费用，sole必要/owner确认NC；不为复制HB数值界新增正文。

### [Output Vector Editing for Memorization Mitigation in Large Language Models](https://arxiv.org/html/2606.18767v1)

精确v1 §§3–6与Limitations深入，6分因Ch16具体writer方向缺口升深入。6831条OLMo7B记忆样本、四editing modes、same-neuron零化对照支持局部定向修改与整neuron删除不同；v1没有后版OVE-MA/full-vocabulary LS。writer改v+c·u_s对其他token产生c·u_jᵀu_s局部投影变化，不是完整模型logit等式。greedy20token BLEU差异仅认证续写变化，约14%未覆盖、逐edit reset、累计EOS10次collapse及非目标尾部均阻止隐私擦除结论。Ch16原coupling与定位段没有这条具体readout联系，已窄写两段、自读并由sole真实POST通过；语料挖掘/定位/完整累计和非目标回归均付费，未核代码或复现。完整日证与审阅记录见[补充记录§7](../_sources/daily-20260619/SUPPLEMENT_20261029.md#7-后续小批当前停点)。

### [Reinforcement Learning Towards Broadly and Persistently Beneficial Models](https://alignment.openai.com/beneficial-rl/)

以官方Jun18完整Blog的同起点/同RL compute、单域与排域对照、harmful/helpful prompt选择性响应和finetune的pre-RL对照为采用范围，2+2+3=7深入。44/53改善不是53项全显著或发布安全；后续[精确arXiv v1 §§3–5](https://arxiv.org/html/2606.24014v1)的generic-helpfulness控制、拒答上升与统计边界仅作本次限定审计，不回填Jun18配方或重计后来论文事件。finetune持久性未隔离trait-specific效应，有益steering仍可响应，未测人口和真实价值不获普遍保证。Ch31原31328暖启×reward是负向跨域反证，一般分布移动也不承载这条正向/pressure接口；已在其后窄写两段、自读并sole真实POST通过。具体训练base ID/总计算Not Disclosed，未核实现/复现或生产SLO。

### [Project Fetch: Phase two](https://www.anthropic.com/research/project-fetch-phase-two)

官方Published Jun18已足够本次自然日，不再沿原小时窗要求时分秒；Updated Jun18仅修Phase1日期。标准审阅6分：三次试验里研究者仍批准命令、提供器材/提示并批准阶段交接，coding/setup uplift不能称无人干预或同预算因果速度。实验的自主精细fetch和物理闭环纠偏仍失败；原文明确任务不涉及challenging低层actuation-policy开发，因此不写成“测试证明低层policy失败”。Ch26开篇action deadline与“通用语言推理不是每次低层动作调用必经接口”两段已具体分开fast policy、slow reasoner、safety envelope和人工接管，覆盖本次采用的接口反证；sole必要/实际owner NC通过，不制造新Books段。旧source recert的09:00缺口仅属原小时窗，此补充自然日已解决。

### [RegMix-D: Dynamic Data Mixing via Proxy Training Trajectories](https://arxiv.org/html/2606.18663v1)

精确v1 §3/Algorithms1–2、§4/Table1、Limitations/A1–A3深入审阅；5分因长期缺口升深入。局部next-loss回归使proxy中间轨迹可被消费，offline递归误差与online实际target-loss量尺映射是不同路径。1M→1B TinyLlama、25B Pile17domains、128/512proxy的平均收益仍伴LogiQA/MultiRC退步；single-seed质量与三次计时不互换，0.37%只是在线query增时，全部proxy/搜索/验证仍计费。Pile-CC单目标与训练时钟线性映射不授多目标最优。Ch27原控制面没有该局部预测/反馈接口，现已窄写、完整自读与sole真实POST通过。未核artifact或复现；完整日证、必要与书稿稿件见[补充记录§6](../_sources/daily-20260619/SUPPLEMENT_20261029.md#6-真新三项第一必要与完整窄稿待整体pre)。

### [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/html/2606.18589v1)

精确v1 §4.1–4.3/E3–6与§5.1–5.2关键对照深入审阅。同phase latent距离只选择固定policy已有candidate chunks；预测不被未来观测reset，不在候选间跳时间，也不创造缺失的恢复策略。恢复示教不足、policyencoder≈RandomSwitch和长horizon latent漂移均限制作用。Kinetix12env及SO101/SmolVLA、Franka/pi0.5有限真机结果不授安全；remote更大N曾因延迟而退步，辅助模型毫秒级不是完整deadline。候选、world-model训练/编码/预测和通信均付费。Ch26原chunk闭环没有该同phase消费接口，现已在时间尺度主线后窄写、完整自读与sole真实POST通过；未核artifact或复现。

### [The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs](https://arxiv.org/html/2606.18656v1)

精确v1 §§3–4及§6深入审阅。2032BBQ-derived English binary pairs里，MAR是contrast答对条件下target答错，不是拒答率；两边原始正确率与反向错误须并报。25模型的行为结果不证明统一机制，3开放模型30failure/30control的head消融也不授闭源或全训练因果。Mistral base contrast正确率21.6%使base/instruct比较未决；7人512input不是全数据人工验证。Ch66原配对公平框架未承载这个证据被群体cue覆盖的具体反证，现已窄写、完整自读与sole真实POST通过。范围止于美国英语二元人口，不据此削弱安全或签发公平真值。

### [On the Residual Scaling of Looped Transformers: Stability and Transferability](https://arxiv.org/html/2606.18524v1)

[精确v1](https://arxiv.org/html/2606.18524v1) §§3–5及§7.2–7.5必要证明已深入审阅（评分6但长期缺口触发深入）和独立必要/Books复核。共享ReLU分支在nondegenerate mass、bounded scale和positive-cone gain前提下呈相关累积；多层分解另需weak cross-layer coupling。SwiGLU只有实验、不继承ReLU证明，LR是条件界、不是普遍最佳值。FineWebEdu10B、L12/24/48与N1/2/4/8的语言建模对照支持局部迁移，也有末轮相关弱负和高LR发散。完整限定命题见[补充记录§5](../_sources/daily-20260619/SUPPLEMENT_20261029.md#5-首批必要证据与实际books决定)。Ch17已有递归预算但未承载相关累积造成的loop/depth分轴；现已在递归主段后整合、完整自读及sole实际POST通过。未核artifact或复现，不授任意深度外推或生产SLO。

本轮去重纠正：18394v1与18967v1均已是June18正式候选，不在此重计、重评分或移归属。18394只确认Ch48已有父路径条件head/边际surrogate及实际验证成本覆盖；18967发现旧实际Books差额后补齐Ch48的policy量化refresh与shrinking-batch区间gate，必要/PRE/实际POST均由sole reader完成，已交June18作者仅行政补注。后者采用v1 Table2的19.6%/12.7%限定数字，不沿用后来摘要24.2%/15.6%；既成修复保留，不伪装成本日新事件。

### [Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees](https://arxiv.org/html/2606.19376v1)

**2606.19376 — Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees**

**问题与旧路径。** `Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** LLM router 可在稀疏、单侧 user feedback下在线学习cost policy，同时把满意度SLA作为约束而非平均reward。 Authoritative owner 是 `INFER-SCHEDULING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 多类LLM benchmarks；SLARouter报告保持SLA并最高降成本2.2×，无需per-benchmark tuning。 Method locator：`https://arxiv.org/html/2606.19376v1 — § exact-v1 anchor: SLARouter`。Evaluation locator：`https://arxiv.org/html/2606.19376v1 — § exact-v1 evaluation anchor: wide range of LLM benchmarks`。Benchmark identity：model=`Candidate LLMs in the exact-v1 SLARouter benchmark matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Per-user satisfaction guarantee used by SLARouter; no universal deployment SLO`；evaluator=`Cost subject to user-satisfaction guarantee over multiple LLM benchmarks with sparse one-sided feedback`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 理论保证依赖反馈与可行性假设；offline benchmark satisfaction不是生产SLA，delayed/strategic feedback会破坏校准。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。


Claim boundary：只使用 `arXiv:2606.19376v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前正文 `Calibration 是在线 Routing State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [ClayBuddy: A Framework, Evaluation, &amp; Mitigation of Coding Agent Failures](https://arxiv.org/html/2606.19380v1)

**2606.19380 — AgentArmor: A Framework, Evaluation, & Mitigation of Coding Agent Failures**

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：coding-agent safety failure 应拆成 underspecification、capability error 与 harness error，并分别用 policy、classifier/immutability 与 context/tool control修复。

**State / data / control owner。** `PLATFORM-SECURITY` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.19380v1 §6 Implementation and Results; Appendices` 支持 `eight coding-agent safety evaluations plus mitigation tests`；模型 `frontier coding agents and AgentArmor`；硬件 `Disclosed only in the exact-v1 setup; no cross-paper normalization`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.19380v1 §3 setup; §4 scenarios; §5 design`；counterevidence locator：`arXiv:2606.19380v1 §7 future directions; Appendix C.17 validity`。

**Trade-off / failure / coexistence / evolution。** 分解支持定向缓解但有限场景不能证明安全 guarantee；自修改 harness 还需外部 immutable authority。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.19380v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Pre-execution Guardrail：检测 Off-task 不能等到副作用发生后`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence](https://arxiv.org/html/2606.19386v1)

**2606.19386 — Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence**

**问题、旧路径与机制。** 固定半衰期累积在采样节奏稳定时仍合理；动作间隔改变后，wall-clock decay相对事件注入量也改变，level trigger可在快节奏持续报警、慢节奏静默。事件映射、实际cadence与校准参数必须联合声明，不将两种regime改写成可观测transition window或真实风险瞬时变化。

**State / data / control owner。** `PLATFORM-MONITORING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.19386v1 §2 Setup; §3 Δt=0 Audit and Erratum; §§4–9 cadence sweeps, scaling and transition triggers`；`arXiv:2606.19386v1 §4 Uniform-Cadence Sweep; §5 Measured Real Cadence; §6 burst structure; Appendix A replay/instrumentation`；counterevidence `arXiv:2606.19386v1 §8 scaling-rule limits; §9 transition-trigger timing problem; §11 Limitations`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 论文先纠正自身Δt=0错误，后续bistability只覆盖所测cadence/monitor class与20轨迹/给定参数。时钟、事件映射或burst分布漂移时重新校准，保sample-time CUSUM对照及外部风险证据/人工升级；edge+hysteresis只抑制重复level告警，不授恢复人类应干预的moment。


仅使用 `https://arxiv.org/html/2606.19386v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**2026-10-29 定点纠正。** 当前 `PLATFORM-MONITORING` owner 为 [books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)，19386 marker内已改为 `Wall-clock Decay 的校准必须绑定 Action Cadence`。旧“同一transition两种采样相位解释/区间双假设”不受v1支持，撤销该解释；保留v1 §§4/6/7/9/11的level/edge/sample-time对照及20轨迹边界。当前v2纠正cadence来自scriptable loop而非Claude Code hook，不以旧描述或cross-instrument相关性作因果证据。sole reader已真实读回并POST通过，不再以旧“首Review notes前”标签代替实际位置检查；日期和分数不变。

### [Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework](https://arxiv.org/html/2606.19390v1)

**2606.19390 — Execution-bound advisory automation for agentic AI: a reproducible AIBOM-driven CSAF-VEX framework**

**问题与机制变化。** Agentic advisory automation需把 AIBOM/SBOM、runtime activation evidence、signed CSAF-VEX与replay bundle连成同一漏洞处置链，不能仅按静态依赖宣告 affected/not affected。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.19390v1 PDF §§3–5 AIBOM-driven CSAF-VEX workflow and execution binding`；Evaluation=`arXiv:2606.19390v1 PDF §§6–7 reproducibility/case-study evaluation`；Counterevidence=`Not Disclosed — arXiv:2606.19390v1 has no dedicated limitations section; exact-v1 counterevidence is localized at PDF limitations on dependency inventory, activation observability and advisory authority`。Workload=`Approximately 10,000 SBOM entries plus synthetic dependency graphs of 50, 500 and 5,000 components; five-fold cross-validation`；Model=`Random forest with 200 estimators and maximum depth 12; XGBoost with 300 trees, learning rate 0.05, maximum depth 6 and subsampling 0.8`；Hardware=`Not Disclosed`；Evaluator=`advisory consistency, activation evidence, signed artifact and replay reproducibility`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 运行证据可减少误报却可能漏掉潜在路径；自动VEX不能替代产品安全 owner签署与补丁验证。


**Claim boundary。** 只使用 `https://arxiv.org/pdf/2606.19390v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Agent authority BOM、channel coverage 与 executable PoV`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [OpenRath: Session-Centered Runtime State for Agent Systems](https://arxiv.org/html/2606.19409v1)

**2606.19409 — OpenRath: Session-Centered Runtime State for Agent Systems**

**问题与旧路径。** Modern agent systems often suffer from fragmented runtime state: transcripts, tool effects, memory events, workspace placement, branch provenance, and replay evidence are recorded separately and become difficult to inspect or reproduce. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Session 应成为执行路径携带的一等 runtime value，统一 transcript、tool effect、sandbox、branch lineage、token usage、pending work 与 memory event；fork/merge/replay 是显式操作。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 报告只验证 controlled runtime properties 与 audited milestones，没有 broad quantitative comparison。 Method=`https://arxiv.org/html/2606.19409v1 — § exact-v1 anchor: Session-Centered Runtime State`；Evaluation=`https://arxiv.org/html/2606.19409v1 — § exact-v1 evaluation anchor: audited milestones`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`audited runtime invariants and controlled replay properties; no broad quality benchmark`。

**Trade-off、failure、共存与演进。** live-provider quality、optional backend availability 与 memory quality明确未证明；central Session 也可能扩大故障域。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19409v1 — § exact-v1 limitation/counterevidence anchor: claims are limited`。


Claim boundary：仅 `arXiv:2606.19409v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `AGENT-PLATFORM` owner 为 [books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)。Review notes 前命题级锚点为 `Agent Definition 与 Run Identity（typed Session 主线）`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Deontic Policies for Runtime Governance of Agentic AI Systems](https://arxiv.org/html/2606.19464v1)

**2606.19464 — Deontic Policies for Runtime Governance of Agentic AI Systems**

**问题与旧路径。** Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** runtime governance 除 permit/prohibit 外还需 obligation lifecycle、dispensation、meta-policy precedence 与 ontology reasoning，并在 LLM 外执行。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 以 AgenticRei examples 展示 tool calls 与 A2A messages 的 policy expression/evaluation。 Method=`https://arxiv.org/html/2606.19464v1 — § exact-v1 anchor: obligations, dispensations`；Evaluation=`https://arxiv.org/html/2606.19464v1 — § exact-v1 evaluation anchor: examples`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`expressibility and runtime policy-evaluation examples`。

**Trade-off、failure、共存与演进。** 示例不构成吞吐、安全或完备性证明；ontology/policy conflict 仍需可信 owner 与版本治理。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19464v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19464v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Policy-as-Data：可更新规则与模型判断必须分开版本化`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [FloatDoor: Platform-Triggered Backdoors in LLMs](https://arxiv.org/html/2606.19535v1)

**2606.19535 — FloatDoor: Platform-Triggered Backdoors in LLMs**

**问题与旧路径。** Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B 跨 NVIDIA GPU、Google TPU、AWS Graviton、Alibaba Yitian-710，并展示目标平台 code vulnerability。 Method=`https://arxiv.org/html/2606.19535v1 — § exact-v1 anchor: platform-triggered backdoor`；Evaluation=`https://arxiv.org/html/2606.19535v1 — § exact-v1 evaluation anchor: broad range of deployment targets`。Benchmark contract：model=`Qwen3-4B and Qwen3-8B with two LoRA adapters`；hardware=`NVIDIA H200, NVIDIA A100, NVIDIA H100, NVIDIA DGX Spark, Google TPU, AWS Graviton and Alibaba Yitian-710`；precision=`Not Disclosed`；batch=`1`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`target-platform activation, aggregate utility and vulnerable-code generation`。

**Trade-off、failure、共存与演进。** 攻击依赖作者平台集合与 LoRA；跨平台不一致不等于任意模型都可植入，可信构建仍需独立证明。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19535v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19535v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `模型内部路由、训练数据与 Weight Repair 都进入攻击面`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](https://arxiv.org/html/2606.19544v1)

**2606.19544 — Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias**

**问题与旧路径。** LLM-as-a-Judge has become the dominant evaluation paradigm for language models, but judge validation in practice relies on exact-match agreement, a metric that does not correct for chance and systematically overstates discriminative ability. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Judge validation 要同时报告 chance-corrected agreement、test-retest consistency 与 position/verbosity bias；高 consistency 不能替代 validity。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 21 judges、9 providers、3 benchmarks、118 runs、约 541k judgments；报告 kappa deflation 与 ranking shifts。 Method=`https://arxiv.org/html/2606.19544v1 — § exact-v1 anchor: Minimum Viable Validation Protocol`；Evaluation=`https://arxiv.org/html/2606.19544v1 — § exact-v1 evaluation anchor: 118 runs`。Benchmark contract：model=`Gemini 3.1 Pro, Claude Opus 4.6, DeepSeek V3.2, Claude Sonnet 4.6, Llama 3.3 70B, Kimi K2.5, GPT-5.4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, GLM-5, GPT-oss 120B, Claude Sonnet 4, Gemini 2.5 Flash, Claude Haiku 4.5, GPT-4.1-mini, Minimax M2.7, Qwen 3 8B, GPT-4o-mini, Mixtral 8x22B and GPT-5.4-mini`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`agreement, Cohen's kappa, test-retest consistency, position bias and verbosity bias`。

**Trade-off、failure、共存与演进。** 三个 benchmark 与单一 pairwise rubric 不证明所有 judge 场景；Cohen kappa 也依赖 prevalence。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19544v1 — § exact-v1 limitation/counterevidence anchor: limitations`。


Claim boundary：仅 `arXiv:2606.19544v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Scorer 不是绝对真相`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Uncertainty Decomposition for Clarification Seeking in LLM Agents](https://arxiv.org/html/2606.19559v1)

**2606.19559 — Uncertainty Decomposition for Clarification Seeking in LLM Agents**

**问题与旧路径。** Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 黑盒 Agent 可把 action confidence 与 request uncertainty 分开；只有后者高时触发 clarification，避免把执行不确定与需求欠规范混成 abstention。 唯一知识 owner 为 `AGENT-PLANNING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 五个 backbones，在 WebShop/ALFWorld clarification variants 与 REAL 上比较 clarification F1/fault detection。 Method=`https://arxiv.org/html/2606.19559v1 — § exact-v1 anchor: action confidence from request uncertainty`；Evaluation=`https://arxiv.org/html/2606.19559v1 — § exact-v1 evaluation anchor: five LLM backbones`。Benchmark contract：model=`GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B and GPT-OSS-120B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`clarification F1 and fault detection across clarification and standard benchmarks`。

**Trade-off、failure、共存与演进。** prompt-based uncertainty 未校准成概率；benchmark 人工制造 50% 欠规范，澄清成本和用户响应质量未被完整建模。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19559v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19559v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `AGENT-PLANNING` owner 为 [books/part-07-agent/79-planning.md](../../../../books/part-07-agent/79-planning.md)。Review notes 前命题级锚点为 `先校准不确定性，再决定行动、询问或探索`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows](https://arxiv.org/html/2606.19595v1)

**2606.19595 — IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows**

**问题与旧路径。** Voice agents deployed in structured workflows (customer service, healthcare scheduling, account management) must handle frequent user interruptions while maintaining progress through multi-step procedures. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** voice-agent interruption recovery 必须保存 workflow node、已提交 side effects 与待确认槽位，恢复时区分 resume、repair、restart。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** IHBench 在 structured workflows 上测 interruption 后 task completion 与 recovery error。 Method=`https://arxiv.org/html/2606.19595v1 — § exact-v1 anchor: Post-Interruption Recovery`；Evaluation=`https://arxiv.org/html/2606.19595v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`GPT-4o Audio, GPT-4o Mini Audio, GPT Audio, GPT Audio Mini, GPT Realtime, GPT Realtime 1.5, GPT Realtime Mini, GPT Realtime 2, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Live, Gemma 4 12B Instruct, Qwen3-Omni-30B-A3B-Instruct, Qwen2.5-Omni-7B, Phi-4-Multimodal-Instruct, Voxtral-Small-24B-2507, Qwen2-Audio-7B-Instruct, MiMo-Audio-7B-Instruct and Kimi-Audio-7B-Instruct across 27 mode/configuration combinations`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`post-interruption task completion and structured recovery error`。

**Trade-off、failure、共存与演进。** 模拟中断与语音管线不覆盖真实网络/ASR drift；恢复成功也不证明重复 effect 被阻止。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19595v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19595v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Resume 的语义必须比“有 Checkpoint”更具体`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns](https://arxiv.org/html/2606.19613v1)

**2606.19613 — StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns**

**问题与旧路径。** We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 6 harnesses×7 open LLMs、20 scenarios×100 turns；所有模型 5–6 turns 内失败，test feedback/retry 最多提升 12×。 Method=`https://arxiv.org/html/2606.19613v1 — § exact-v1 anchor: 100 Interaction Turns`；Evaluation=`https://arxiv.org/html/2606.19613v1 — § exact-v1 evaluation anchor: 20 scenarios`。Benchmark contract：model=`Devstral 2, Devstral Small 2, GLM-5, Kimi K2.5, Nemotron Super, Qwen3-Coder-Next and Qwen3.5-122B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`consecutive passed turns, test feedback/retry effect and harness sensitivity over 20x100-turn scenarios`。

**Trade-off、failure、共存与演进。** 程序生成 REST workload 不能代表全部软件演化；turn-to-failure 对变更难度和 harness 强敏感。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19613v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19613v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前正文 `Long-session Stamina 必须测量状态如何累积失效` 已形成 owner-level 机制链；本项已实际 Integrate。

### [CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference](https://arxiv.org/html/2606.19667v1)

**2606.19667 — CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference**

**问题与旧路径。** Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 三个 vLLM configurations，median TTFT 降约 20–33%，QA quality 未下降；greedy 达 oracle TTFT gain 的 97.5%。 Method=`https://arxiv.org/html/2606.19667v1 — § exact-v1 anchor: prefix tree over recently served evidence sequences`；Evaluation=`https://arxiv.org/html/2606.19667v1 — § exact-v1 evaluation anchor: three vLLM configurations`。Benchmark contract：model=`Qwen2.5-1.5B and Qwen2.5-7B`；hardware=`RTX 4060 Ti 8 GB, RTX 4090 24 GB and RTX 4090D 24 GB`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`median TTFT, prefix reuse and QA answer quality`。

**Trade-off、failure、共存与演进。** 重排可能改变 positional bias 与答案；局部 query locality 不保证生产 cache hit，且不减少 decode cost。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19667v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。


Claim boundary：仅 `arXiv:2606.19667v1` official HTML；不使用 later version；ordinary pending locator count=`0`.

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `Structured knowledge 只有进入 physical access plan 才改变 KV 成本`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems](https://arxiv.org/html/2606.19692v1)

**2606.19692 — When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems**

**问题与旧路径。** Vector hubness, where a few points become nearest neighbors of many queries, creates a poisoning risk in retrieval-augmented generation (RAG): one injected document can influence unrelated requests.

**机制、状态与控制流。** `When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems` 路由到 `AGENT-RAG`：旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。 唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19692v1#S5 — §5 Incremental Systems Architecture`；Evaluation=`https://arxiv.org/html/2606.19692v1#S9 — §9 Systems Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结论限于单向量 cosine 检索、固定 encoder、两个 10 万文档语料和给定攻击；organic hubs 在冻结阈值下大量被标记，targeted single-query、late-interaction、multi-vector 与模型内部投毒未验证。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19692v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19692v1#S13 — §13 Limitations and Discussion`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `RAG 安全必须覆盖完整状态生命周期` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents](https://arxiv.org/html/2606.19704v1)

**2606.19704 — Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents**

**问题与旧路径。** Agent benchmarks are growing fast, but no single benchmark touches more than four or five of the dimensions that deployment exposes.

**机制、状态与控制流。** `Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents` 路由到 `PLATFORM-EVALUATION-SYSTEM`：它不再用单次 aggregate mean 排名决定发布，而要求 evaluation owner 保存 configuration identity，并以 in-sample/OOD rank correlation、judge-independent trajectory verifier 和持久 benchmark transport 判断配置能否外推；旧 leaderboard 可保留为观测列，不能继续拥有 release 决策。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19704v1#S4 — §4 Predictive Validity as the Ranking Criterion`；Evaluation=`https://arxiv.org/html/2606.19704v1#S6 — §6 Implications for Benchmark Design`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 这是基于 AssetOpsBench 与 14 份未同行评审 implementation reports 的 position paper；作者未运行大规模 predictive-validity trial，也未证明十二层正交或排名与真实 incident/override 指标相关。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19704v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19704v1#S8 — §Limitations`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Open-world Evaluation 必须重复发生，而不是一次验收`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Closing the Operational Gap in Semantic Caching](https://arxiv.org/html/2606.19719v1)

**2606.19719 — Closing the Calibration Gap in Semantic Caching**

**问题与旧路径。** Semantic caching cuts LLM inference costs by serving a cached response to semantically similar queries.

**机制、状态与控制流。** `Closing the Calibration Gap in Semantic Caching` 路由到 `AGENT-RAG`：语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。 唯一知识 owner 为 `AGENT-RAG`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19719v1#S3 — §3 Cache-Aware Metrics`；Evaluation=`https://arxiv.org/html/2606.19719v1#S4 — §4 Experimental Setup and §5 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 74,265 个英文 pair、45% 正例、9 个 bi-encoder/reranker 的结果受 ParaBank2 与合成数据占比、标签噪声及部署先验约束；固定 test mix 不证明低重复率生产流量。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19719v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19719v1#A2.SS4 — §Appendix B.4 Quality Considerations and Limitations`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `语义 Cache 的发布标准必须绑定工作点，而不是只看排序分数` 已形成 owner-level 机制链；本项已实际 Integrate。

### [SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL](https://arxiv.org/html/2606.19746v1)

**2606.19746 — SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL**

**问题与旧路径。** The scaling of LLMs toward long-context inference has shifted the primary serving system bottleneck from computation to memory capacity.

**机制、状态与控制流。** `SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL` 路由到 `INFER-KV-CACHE`：dense-attention 时代的 RDMA 全 prefix 搬运被改为 CXL cache-line top-k 按需读取：prefill 把 KV 写入共享池，scheduler 按设备分配请求，decode GPU 只取 sparse attention 选中的条目；KV owner 从单 GPU/整块传输变成 CXL pool 与调度器协同。失败时仍需本地 DRAM/RDMA 路径，代价是 CXL 拓扑、细粒度访问和设备争用。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19746v1#S4 — §4 System Design`；Evaluation=`https://arxiv.org/html/2606.19746v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证 DeepSeek-V3.2 AWQ4、SGLang/HiSparse、8×H20、2TB CXL、16K–128K/1K 输出；RDMA 是本机 loopback 的理想化基线，不能证明跨机、dense attention 或其它 CXL 设备收益。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19746v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19746v1#S6 — §6 Discussion`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `分布式 Prefix KV 是带复制与新鲜度的 materialized state`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Grounded Inference: Principles for Deterministically Encapsulated Generative Models](https://arxiv.org/html/2606.19753v1)

**2606.19753 — Grounded Inference: Principles for Deterministically Encapsulated Generative Models**

**问题与旧路径。** The incorporation of generative models into traditional computational systems presents both enormous opportunity and tremendous peril.

**机制、状态与控制流。** `Grounded Inference: Principles for Deterministically Encapsulated Generative Models` 路由到 `PLATFORM-PRODUCTION`：该文把概率模型封装为受类型化输入、可验证输出、超时/失败状态和确定性 orchestration 约束的组件，主程序保留状态与最终 authority；但它是架构原则而非新的可复算实现，作为现有 grounded-inference 原则的补充而不追加 Books 机制。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19753v1#S2 — §2 Grounded Inference Primitives`；Evaluation=`https://arxiv.org/html/2606.19753v1#S5 — §5 Reference Architecture`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 没有公开 workload、实现 artifact 或对照实验；四个 primitive 与两个 anti-pattern 未被量化验证，不能据此声称确定性、可靠性或生产风险已经闭合。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19753v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19753v1#S7 — §7 Generative Model Risks`。

**V3 Books 复验。** 当前 `PLATFORM-PRODUCTION` owner 为 [books/part-06-ai-infrastructure/73-production-best-practice.md](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)。Review notes 前命题级锚点为 `Production Contract`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling](https://arxiv.org/html/2606.19755v1)

**2606.19755 — SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling**

**问题与旧路径。** Speculative inference accelerates large language model (LLM) decoding but provides no inherent safety guarantees.

**机制、状态与控制流。** `SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling` 路由到 `INFER-SPECULATIVE-DECODING`：SafeSpec 将安全 head 并入 target verification 的同一次前向：draft token 通过语义与风险联合门，风险触发 rollback 和 safety-guided multi-sampling，而非在 speculative path 外串联 guard。target verifier 持有 accept/rollback 控制；外部 guard 仍作为未知攻击与 head 故障 fallback。 唯一知识 owner 为 `INFER-SPECULATIVE-DECODING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19755v1#S3 — §3 Methodology`；Evaluation=`https://arxiv.org/html/2606.19755v1#S4 — §4 Experiments and §5 Ablation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 15% ASR 降幅与 2.06× benign speedup 绑定 Qwen3-32B、论文所列攻击集和 6×A800；latent head 不能证明新型 jailbreak、跨语言或 target/draft 变更后仍校准。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19755v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19755v1#A1 — §Appendix A Experimental Setup and Safety Head`。

**V3 Books 复验。** 当前 `INFER-SPECULATIVE-DECODING` owner 为 [books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)。Review notes 前命题级锚点为 `当 Draft 可能优于 Target，系统进入效用仲裁分支`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI](https://arxiv.org/html/2606.19769v1)

**2606.19769 — Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI**

**问题与旧路径。** The scalability of humanoid robots will depend not only on models and hardware, but also on whether physical experience can accumulate across robots, tasks, organizations, and time.

**机制、状态与控制流。** `Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI` 路由到 `MULTIMODAL-EMBODIED-VLA`：它把 humanoid 数据 owner 从孤立样本仓库提升为 lifecycle contract：每条经验绑定 body/action/task/scene/trace/outcome，并保留时间、坐标系、标定、运动学、单位、版本和 provenance；capability-specific schema 在水平标准之上扩展，旧数据只能经显式兼容层进入训练。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19769v1#S5 — §V Data Standards as Infrastructure`；Evaluation=`https://arxiv.org/html/2606.19769v1#S6 — §VI Implementation Priorities`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 材料源于 ISO/WD 26264-1 制定经验而非完成标准或跨厂商 benchmark；未证明提议字段足以消除硬件差异、隐私/IP 限制和 sim-to-real 偏移。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19769v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19769v1#S4 — §IV Why More Data Is Not Enough`。

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前正文 `机器人经验要跨设备、任务与时间复用时` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases](https://arxiv.org/html/2606.19803v1)

**2606.19803 — Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases**

**问题与旧路径。** Vector databases are increasingly used in security sensitive contexts with Retrieval Augmented Generation and organizational AI pipelines; however, their security capabilities remain limited.

**机制、状态与控制流。** `Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases` 路由到 `PLATFORM-SECURITY`：向量检索不再先 ANN 后应用层过滤，而把 subject/object/policy 与 approximate candidate generation 共同求解；policy engine 拥有可见集合，ANN 只在授权候选内优化 recall/latency。pre/post-filter 可作为规模与索引能力不同的共存路径，但必须分别报告漏检和越权风险。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19803v1#S2 — §2 FGAC Policy Model`；Evaluation=`https://arxiv.org/html/2606.19803v1#S4 — §4 Preliminary Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 论文仅给 formal model 与 preliminary experiments；未覆盖动态 policy、跨租户缓存、删除一致性或所有向量数据库实现，不能宣称 FGAC 与 ANN recall 已同时普适最优。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19803v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19803v1#S5 — §5 Discussion and §6 Future Work`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前正文 `Policy-aware ANN 必须先确定可见集合再优化近似召回` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning](https://arxiv.org/html/2606.19808v1)

**2606.19808 — Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning**

**问题与旧路径。** Test-time reasoning is increasingly used as a serving-time control knob, but extra reasoning is not uniformly valuable: it can repair failed attempts, waste compute on already-correct answers, or introduce harmful answer changes.

**机制、状态与控制流。** `Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning` 路由到 `INFER-SCHEDULING`：SEVRA 把额外推理视为 serving allocation：冻结 solver 先产出 attempt，recoverability gate 决定保留、验证或 bounded retry；scheduler 拥有 token budget 和 harmful-flip 审计。较长 initial budget 在部分任务更优，因此 controller 必须与 no-verify/longer-solve 路径共存。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19808v1#S4 — §4 Selective Verification Method`；Evaluation=`https://arxiv.org/html/2606.19808v1#S5 — §5 Experimental Setup and §6 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 76.3%/26.8% 与 transfer 数字限于 Qwen3-4B、MATH500/GSM8K/CommonsenseQA 和给定 token budgets；不证明 gate 在新模型、开放题或负载漂移下优于先增加初始预算。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19808v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19808v1#A10 — §Appendix J Limitations and Deployment Considerations`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `当前 Confidence 不等于继续计算的 Residual Value`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference](https://arxiv.org/html/2606.19849v1)

**2606.19849 — ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference**

**问题与旧路径。** Streaming VideoLLMs must continuously process incoming video while maintaining low query latency, making both video-ingestion throughput and query-time responsiveness critical for real-time deployment.

**机制、状态与控制流。** `ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference` 路由到 `INFER-SCHEDULING`：ViCoStream 将 video preprocessing、encoder、token drop、prefill/decode 统一到 chunk scheduler，以 CUDA-stream overlap、bounded visual attention 和 query retrieval 控制每 chunk 计算/内存；调度器拥有 stage backpressure，降载时通过 token retention/attention scope 回退，而非让单模块各自最大化。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19849v1#S3 — §3 Stage-Wise Coordinated Streaming`；Evaluation=`https://arxiv.org/html/2606.19849v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 134 FPS 与 <50 ms TTFT 仅对应 Qwen2.5-VL-3B/7B、单 A100 和论文 streaming benchmarks；精度接近 full-history 不证明长时依赖、并发请求或其它 GPU。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19849v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19849v1#S5 — §5 Accuracy-Latency and Resource-Constrained Parallelism`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `异质 DAG 需要 Readiness、Residency 与 Deadline 共享一条控制链`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models](https://arxiv.org/html/2606.19868v1)

**2606.19868 — A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models**

**问题与旧路径。** Although large language models (LLMs) have shown strong capabilities across a wide range of tasks, their outputs often remain unreliable and may contain hallucinations, making uncertainty estimation (UE) essential for building trustworthy LLMs.

**机制、状态与控制流。** `A Systematic Evaluation of Black-Box Uncertainty Estimation Methods for Large Language Models` 路由到 `PLATFORM-EVALUATION-SYSTEM`：统一框架把 black-box UE 的 verbalization、sampling、explanation、multi-agent 与 hybrid 信号放到同一 evaluator contract；但 24 方法无单一 winner，现有评测章已包含按 task/calibration 选择 UE 的原则，因此记为 No Change。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19868v1#S3 — §III Uncertainty-Estimation Taxonomy`；Evaluation=`https://arxiv.org/html/2606.19868v1#S4 — §IV Experimental Setup`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 24 方法×4 模型×4 数据设置不能证明跨 API 版本、开放生成或成本约束下的统一最优；answer-space/hybrid 优势是设置相关观察。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19868v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19868v1#S6 — §VI Conclusion and Future Work`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Calibration Slice 必须包含 Language × Model Scale × Estimator Contract`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Multi-Agent Transactive Memory](https://arxiv.org/html/2606.19911v1)

**2606.19911 — Multi-Agent Transactive Memory**

**问题与旧路径。** The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations.

**机制、状态与控制流。** `Multi-Agent Transactive Memory` 路由到 `AGENT-MEMORY`：多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19911v1#S3 — §3 Multi-Agent Transactive Memory`；Evaluation=`https://arxiv.org/html/2606.19911v1#S4 — §4 Experimental Setup and §5 Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只在论文 multi-agent tasks、拓扑和模型上验证；未证明目录在 agent churn、对抗写入、跨组织权限或长期知识漂移下可靠。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19911v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19911v1#S6 — §6 Discussion`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `共享 Memory 需要分离选择性写入、访问权与事实状态`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Online Dynamic Batching with Formal Guarantees for LLM Training](https://arxiv.org/html/2606.19989v1)

**2606.19989 — Online Dynamic Batching with Formal Guarantees for LLM Training**

**问题与旧路径。** Modern LLM training breaks a core assumption behind offline batch samplers: the true training cost of a sample is only observable after preprocessing, augmentation, templating, tokenization, and multimodal visual-token expansion.

**机制、状态与控制流。** `Online Dynamic Batching with Formal Guarantees for LLM Training` 路由到 `TRAIN-DISTRIBUTED-TRAINING`：训练 batching 从离线固定 batch 改为 online queue policy，在到达、长度与资源状态变化时决定组合，同时以形式化界约束等待/效率；scheduler 拥有 batch formation，超出假设时退回静态 bucket。代价是在线估计误差与公平性。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19989v1#S2 — §2 Online Dynamic Batching System Design`；Evaluation=`https://arxiv.org/html/2606.19989v1#S4 — §4 Experimental Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 形式保证依赖论文到达与成本模型；未证明真实多租户数据 loader、straggler、网络/optimizer 状态或非平稳长度分布满足假设。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19989v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19989v1#S5 — §5 Scope and Limitations`。

**V3 Books 复验。** 当前 `TRAIN-DISTRIBUTED-TRAINING` owner 为 [books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)。Review notes 前正文 `Variable-length Batch 让并行计划成为 Runtime State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services](https://arxiv.org/html/2606.19992v1)

**2606.19992 — Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services**

**问题与旧路径。** In the agentic web era, LLM-based agents increasingly invoke web services as tools, yet most interfaces remain \emph{static endpoints} that poorly express long-horizon workflows with loops, conditionals, joins, and retries.

**机制、状态与控制流。** `Beyond Static Endpoints: Tool Programs as an Interface for Flexible Agentic Web Services` 路由到 `AGENT-MCP`：Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。 唯一知识 owner 为 `AGENT-MCP`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.19992v1#S3 — §3 ToolPro Design`；Evaluation=`https://arxiv.org/html/2606.19992v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验只覆盖作者 web-service/tool tasks；未证明任意第三方 API、副作用事务、认证轮换或不可信程序可安全执行。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.19992v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.19992v1#S5 — §5 Limitations and Discussion`。

**V3 Books 复验。** 当前 `AGENT-MCP` owner 为 [books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md)。Review notes 前正文 `从静态 Endpoint 到受限 Tool Program` 已形成旧路径、约束变化、state/control ownership、trade-off 与 fallback 的完整机制链；本项已实际 Integrate。

### [StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation](https://arxiv.org/html/2606.20005v1)

**2606.20005 — StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation**

**问题与旧路径。** Attention distillation, which trains one attention distribution to match another by minimizing their Kullback-Leibler (KL) divergence, is widely used in knowledge distillation, model compression, continual learning, and sparse-attention LLM training.

**机制、状态与控制流。** `StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation` 路由到 `INFER-TENSORRT-LLM`：StreamKL 将 attention distillation 的 KL 计算分块流式执行，避免物化完整概率张量；kernel/runtime 共同拥有 block state 与数值归约，OOM 或不支持 shape 时回退到标准 KL。速度/显存换来额外 kernel、归约误差和硬件依赖。唯一知识 owner 为 `INFER-TENSORRT-LLM`；训练章节只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20005v1#S3 — §3 StreamKL Forward/Backward Pass`；Evaluation=`https://arxiv.org/html/2606.20005v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证论文 attention shapes、精度、模型与 GPU；未证明所有 vocab/sequence 规模、分布式并行或低精度下保持相同数值和收敛。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20005v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20005v1#S6 — §6 Limitations and Discussion`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `通用 Module Replacement 与专用 Structural Fusion`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents](https://arxiv.org/html/2606.20023v1)

**2606.20023 — When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents**

**问题与旧路径。** As LLM agents increasingly select tools autonomously, their choices among tools with different privileges become safety-relevant.

**机制、状态与控制流。** `When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents` 路由到 `AGENT-TOOL-CALLING`：工具选择不再只优化成功率，而先求满足任务的最小 capability set；planner 提议工具，policy layer 比较 privilege lattice 后降权/拒绝 over-privileged choice，并保留必要时显式 escalation。代价是 capability annotation 不全会误拒绝或低估组合权限。 唯一知识 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20023v1#S2 — §2 Privilege Model and Selection Analysis`；Evaluation=`https://arxiv.org/html/2606.20023v1#S3 — §3 Evaluation Setup and §4 Empirical Analysis`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 测量与 mitigation 绑定论文 agent/tool suites 和 privilege labels；未证明动态 OAuth scope、跨工具权限合成或恶意 metadata。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20023v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20023v1#S5 — §5 Mitigation and Limitations`。

**V3 Books 复验。** 当前 `AGENT-TOOL-CALLING` owner 为 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。Review notes 前命题级锚点为 `Disclosure Minimization 不能替代 Authorization`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation](https://arxiv.org/html/2606.20113v1)

**2606.20113 — When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation**

**问题与旧路径。** Streaming Retrieval-Augmented Generation (Streaming RAG) hides tool latency by issuing retrieval queries in parallel with the user's still-arriving input, before the utterance is complete.

**机制、状态与控制流。** `When Does Streaming Tool Use Help? Characterizing Tool-Intent Stabilization in Streaming Retrieval-Augmented Generation` 路由到 `AGENT-TOOL-CALLING`：streaming tool use 不应在第一个 token 触发；controller 追踪 tool-intent 随解码的稳定度，在置信轨迹达到阈值后才 dispatch，未稳定则继续生成或回落到完整 query。它用 latency 换误调用率，并要求 cancellation/duplicate suppression。 唯一知识 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20113v1#S3 — §3 Problem Formalization and Stabilization Controller`；Evaluation=`https://arxiv.org/html/2606.20113v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 稳定阈值与收益只在论文 retrieval tasks、模型、网络延迟和工具集上测得；未证明有副作用工具、长参数或分布漂移。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20113v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20113v1#S6 — §6 Limitations`。

**V3 Books 复验。** 当前 `AGENT-TOOL-CALLING` owner 为 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。Review notes 前正文 `Tool Admission 与 Interaction Latency 必须分开控制` 已形成 owner-level 机制链；本项已实际 Integrate。

### [The Correctness Illusion in LLM-Generated GPU Kernels](https://arxiv.org/html/2606.20128v1)

**2606.20128 — The Correctness Illusion in LLM-Generated GPU Kernels**

**问题与旧路径。** Benchmarks for LLM-generated GPU kernels (KernelBench, TritonBench, GEAK) score correctness through fixed-shape, small-sample allclose-style checks.

**机制、状态与控制流。** `The Correctness Illusion in LLM-Generated GPU Kernels` 路由到 `INFER-TENSORRT-LLM`：GPU kernel 验收从单设备单输入通过改为 CPU oracle、跨 shape/dtype/GPU differential testing 与 clean controls；release owner 保存失败 witness，并在 verdict 不一致时拒绝上线或回退原 kernel。代价是 oracle/设备矩阵成本和未覆盖输入。唯一知识 owner 为 `INFER-TENSORRT-LLM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20128v1#S3 — §3 Differential Correctness Method`；Evaluation=`https://arxiv.org/html/2606.20128v1#S4 — §4 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 24/26 ops 与 RTX3060/A10/L40S/A100/H100 的测试仍不穷尽未定义行为、驱动版本、并发或大模型端到端性能。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20128v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20128v1#S6 — §6 Limitations`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `Kernel Verification 需要从孤立输入扩展到 Model–Kernel Interface`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [N-Version Programming with Coding Agents](https://arxiv.org/html/2606.20158v1)

**2606.20158 — N-Version Programming with Coding Agents**

**问题与旧路径。** This paper revisits the classical concept on N-version programming in the setting of contemporary AI coding agents.

**机制、状态与控制流。** `N-Version Programming with Coding Agents` 路由到 `AGENT-WORKFLOW`：N-version coding agents 并行产出独立实现，由测试/静态检查和 adjudicator 汇合，而非信任单次生成；workflow owner 管理 diversity、quorum 与 fallback 到人工。额外 token/latency 的收益依赖故障独立性，相关 hallucination 会击穿多数表决。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20158v1#S2 — §II N-Version Coding-Agent Architecture`；Evaluation=`https://arxiv.org/html/2606.20158v1#S3 — §III Experimental Methodology and §IV Results`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果只覆盖论文 coding tasks、agent versions 与 test suites；未证明安全漏洞、缺失 oracle、共享训练数据导致的相关错误。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20158v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20158v1#S5 — §V Threats to Validity`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Evaluator-Driven Search：可执行反馈如何变成 Workflow`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference](https://arxiv.org/html/2606.20245v1)

**2606.20245 — Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference**

**问题与旧路径。** Large language models (LLMs) have achieved strong performance across a wide range of language-based tasks by leveraging both extensive parametric knowledge and in-context learning ability, enabling them to incorporate external information provided in the input prompt.

**机制、状态与控制流。** `Navigating Unreliable Parametric and Contextual Knowledge: Explicit Knowledge Conflict Resolution for LLM Inference` 路由到 `AGENT-CONTEXT`：显式 parametric/context knowledge conflict resolution 属于现有 context provenance 与冲突裁决路径；该研究没有新增跨系统 state owner，故 No Change。 唯一知识 owner 为 `AGENT-CONTEXT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20245v1#S3 — §III Explicit Knowledge-Conflict Methodology`；Evaluation=`https://arxiv.org/html/2606.20245v1#S4 — §IV Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验只验证给定冲突构造、模型和问答集；显式选择不能证明来源真实性、时效性或隐式冲突被发现。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20245v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20245v1#S5 — §V Limitations`。

**V3 Books 复验。** 当前 `AGENT-CONTEXT` owner 为 [books/part-07-agent/75-context.md](../../../../books/part-07-agent/75-context.md)。Review notes 前命题级锚点为 `Context Assembly Pipeline`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic](https://arxiv.org/html/2606.20254v1)

**2606.20254 — Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic**

**问题与旧路径。** Model quantization is widely adopted to reduce memory usage and inference cost when deploying deep neural networks on resource-constrained devices.

**机制、状态与控制流。** `Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic` 路由到 `PLATFORM-SECURITY`：量化不再被当作纯压缩步骤：security owner 将 quantization-conditioned backdoor 视作可分离 task vector，在发布前比较全精度/量化行为并用 task arithmetic 移除，再做 clean/attack 双验收。无法分离时回退到拒绝量化模型。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20254v1#S4 — §4 Threat Model and §5 Task-Arithmetic Removal`；Evaluation=`https://arxiv.org/html/2606.20254v1#S6 — §6 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 移除效果限于论文 backdoor construction、模型、bit-width 与 calibration data；未证明未知触发器、其它量化器或 task-vector subtraction 不损害能力。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20254v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20254v1#S7 — §7 Limitations`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前正文 `Quantization 是新的 Security Revision` 已形成 owner-level 机制链；本项已实际 Integrate。

### [ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters](https://arxiv.org/html/2606.20374v1)

**2606.20374 — ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters**

**问题与旧路径。** Large-scale LLM training requires always-on, fine-grained observability for effective performance diagnosis at scale.

**机制、状态与控制流。** `ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters` 路由到 `PLATFORM-TRACE`：ARGUS 将万卡训练诊断从节点日志提升为跨 rank/collective/network/storage 的统一 trace identity；collector 控制采样与时钟映射，diagnoser 只在证据图上定位瓶颈，超预算时降采样并保留关键 span。代价是 telemetry overhead 与相关性误判。 唯一知识 owner 为 `PLATFORM-TRACE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20374v1#S3 — §3 ARGUS System Overview`；Evaluation=`https://arxiv.org/html/2606.20374v1#S4 — §4 Runtime Monitoring and Diagnosis Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 生产观察来自特定 >10,000-GPU 集群、训练栈和故障集；trace 覆盖与诊断时延不证明因果根因、其它 fabric 或故障自动修复。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20374v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20374v1#S6 — §6 Limitations`。

**V3 Books 复验。** 当前 `PLATFORM-TRACE` owner 为 [books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md)。Review notes 前命题级锚点为 `跨层 Trace 只能提出因果候选，不能自动证明根因`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe](https://arxiv.org/html/2606.20381v1)

**2606.20381 — Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe**

**问题与旧路径。** FP4 training promises substantial reductions in memory and computation cost for LLM pretraining, yet current FP4 hardware paths and recipes, including NVIDIA Blackwell/Rubin-class systems and AMD MI350-series GPUs, remain centered on E2M1 data elements.

**机制、状态与控制流。** `Rethinking Shrinkage Bias in LLM FP4 Pretraining: Geometric Origin, Systemic Impact, and UFP4 Recipe` 路由到 `TRAIN-PRETRAINING`：UFP4 针对 FP4 pretraining 的 shrinkage bias 重新分配量化几何与 scaling，使 optimizer/quantizer 共同拥有低精度状态；异常 loss 时回退 BF16/更高精度。显存/吞吐收益以 recipe、kernel 和收敛敏感性为代价。唯一知识 owner 为 `TRAIN-PRETRAINING`；分布式训练章节只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20381v1#S4 — §4 UFP4 Recipe`；Evaluation=`https://arxiv.org/html/2606.20381v1#S5 — §5 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只在 exact-v1 模型规模、token budget、FP4 hardware/simulation 与下游评测验证；未证明更长预训练、其它 optimizer 或最终能力无回归。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20381v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20381v1#S6 — §6 Limitations and Discussion`。

**V3 Books 复验。** 当前 `TRAIN-PRETRAINING` owner 为 [books/part-04-training-system/28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)。Review notes 前命题级锚点为 `Precision Policy 应沿误差传播路径分区`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474v1)

**2606.20474 — UltraQuant: 4-bit KV Caching for Context-Heavy Agents**

**问题与旧路径。** Context-heavy agents place unusual pressure on the key-value (KV) cache: long prefixes are reused across many short turns, while concurrency determines whether the serving system can keep GPUs utilized.

**机制、状态与控制流。** `UltraQuant: 4-bit KV Caching for Context-Heavy Agents` 路由到 `INFER-KV-CACHE`：UltraQuant 将 agent 长上下文 KV 压到 4-bit，并分别控制 token/channel quantization 与 runtime dequant；cache manager 持有 format metadata，质量回归时按 layer/request 回退高精度。收益以 kernel 复杂度、误差累积和 workload sensitivity 为代价。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20474v1#S4 — §4 Ultra-TurboQuant and §5 UltraQuant`；Evaluation=`https://arxiv.org/html/2606.20474v1#S6 — §6 Accuracy and §7 Systems Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 质量与系统数字限于论文 models、context-heavy agent workloads、长度和 hardware；未证明极长上下文、不同 attention、并发 tail latency 或所有任务无损。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20474v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20474v1#S8 — §8 Limitations`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `Quantization Objective 应对齐 Attention Distortion`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems](https://arxiv.org/html/2606.20487v1)

**2606.20487 — Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems**

**问题与旧路径。** Real-world computer-use tasks often span multiple applications and devices, requiring agents to coordinate heterogeneous environments under dynamic runtime failures.

**机制、状态与控制流。** `Beyond Global Replanning: Hierarchical Recovery for Cross-Device Agent Systems` 路由到 `AGENT-WORKFLOW`：跨设备 agent 从全局 replanning 改为层级 recovery：设备局部 controller 先修复可逆错误，跨设备依赖破坏才升级 workflow planner；handoff state 保存 checkpoint/compensation。代价是故障分类错误，fallback 为全局重规划或人工。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20487v1#S3 — §3 Hierarchical Recovery Methodology`；Evaluation=`https://arxiv.org/html/2606.20487v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证论文 devices、tasks、failure injection 与 latency；未证明真实设备副作用、网络 partition、并发用户或补偿完整。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20487v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20487v1#S5 — §5 Failure Analysis and Limitations`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Recovery 与 Verification 必须产生不同 Artifact`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems](https://arxiv.org/html/2606.20493v1)

**2606.20493 — Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems**

**问题与旧路径。** When large language models serve as evaluators in multi-agent systems, their strategy preferences -- whether induced by explicit prompts or by shared architectural priors -- propagate through the agent network.

**机制、状态与控制流。** `Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems` 路由到 `AGENT-MULTI-AGENT`：它把 evaluator preference 看作多-agent 图上的传播状态，要求 evaluation owner 跟踪 judge influence/依赖，而非把 agent votes 当独立样本；检测到 contagion 时使用隔离 judge 或独立 anchor。代价是图估计与额外评审成本。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20493v1#S3 — §3 Contagion Network Model`；Evaluation=`https://arxiv.org/html/2606.20493v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 结果来自论文 contagion model、拓扑和 LLM judges；未证明真实组织评审、隐藏共享训练或动态 agent 网络中的因果传播。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20493v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20493v1#S5 — §5 Limitations`。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前命题级锚点为 `同根报告可以帮助读懂证据，却不能按独立观察累加`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Efficient and Sound Probabilistic Verification for AI Agents](https://arxiv.org/html/2606.20510v1)

**2606.20510 — Efficient and Sound Probabilistic Verification for AI Agents**

**问题与旧路径。** Securing AI agents that operate in complex digital environments has become a critical need, and runtime monitoring approaches that formulate and enforce policies expressed in a formal language like Datalog offer a promising solution.

**机制、状态与控制流。** `Efficient and Sound Probabilistic Verification for AI Agents` 路由到 `AGENT-WORKFLOW`：概率 verification 将 agent policy 的不确定转移纳入可计算验收，通过 relaxation 在 sound bound 与成本间调节；verifier 拥有 accept/reject，超时或 bound 过松时回退 conservative rule/human review。代价是状态抽象与概率模型误设。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20510v1#S3 — §3 Verification Optimization and §4 Relaxation`；Evaluation=`https://arxiv.org/html/2606.20510v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** soundness 只对论文形式假设、抽象与概率界成立；实验不证明开放工具环境、非平稳 policy 或未建模副作用。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20510v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20510v1#S6 — §6 Limitations`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前正文 `概率 Verification 的 Bound 是有前提的验收合同` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes](https://arxiv.org/html/2606.20520v1)

**2606.20520 — Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes**

**问题与旧路径。** Autonomous agents are increasingly connected to cloud, deployment, and data-control workflows, but production mutation authority should not reside inside non-deterministic reasoning processes.

**机制、状态与控制流。** `Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes` 路由到 `PLATFORM-SECURITY`：Sovereign Execution Broker 将 prompt 声明的权限替换为 certificate-bound authority：principal 提交带 scope/expiry 的证书，broker 在工具执行前验证、记录并可 revoke；agent 不持有最终执行权。证书/身份漂移时 fail closed，并与人工 break-glass 共存。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20520v1#S4 — §4 Broker Execution and §5 Scoped Identity`；Evaluation=`https://arxiv.org/html/2606.20520v1#S8 — §8 Evaluation and §9 Security Analysis`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** evaluation 只覆盖论文 broker、capability 和 attack scenarios；未证明所有第三方工具、密钥轮换、跨域 trust root 或 broker compromise。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20520v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20520v1#S10 — §10 Discussion and Limitations`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Agent 授权必须沿 Delegation Chain 单调收窄`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents](https://arxiv.org/html/2606.20529v1)

**2606.20529 — LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents**

**问题与旧路径。** Policy-adherent tool-calling agents in customer-service domains must maintain task states across turns while calling tools and obeying domain policies.

**机制、状态与控制流。** `LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents` 路由到 `AGENT-MEMORY`：LedgerAgent 将 policy-relevant state 记录为结构化 append-only ledger，planner 每次工具调用前读取约束并提交可审计 transition；ledger/policy engine 拥有状态，LLM 不能静默改写。解析冲突时拒绝或转人工。代价是 schema 覆盖与写放大。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20529v1#S3 — §3 LedgerAgent Method`；Evaluation=`https://arxiv.org/html/2606.20529v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验限于论文 tool tasks、policy set 与 ledger parser；未证明并发事务、隐式状态、恶意工具返回或长期 ledger 压缩。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20529v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20529v1#S5 — §5 Limitations`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `Persistent Memory 需要显式状态操作，而不只是 Record`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation](https://arxiv.org/html/2606.20536v1)

**2606.20536 — The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation**

**问题与旧路径。** The Frechet Inception Distance (FID) is the de facto arbiter of image generation, yet most papers report just a single number from a single trained model using a single sampling seed.

**机制、状态与控制流。** `The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation` 路由到 `PLATFORM-EVALUATION-SYSTEM`：FID 验收从单次 seed 分数改为显式训练 seed×生成 seed 分布与置信区间；evaluation owner 保存随机性来源，release 依据分布而非最好一次。增加重复成本，预算不足时至少报告 seed sensitivity 而非隐藏。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20536v1#S3 — §3 Experimental Setup`；Evaluation=`https://arxiv.org/html/2606.20536v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 数百个 SiT 网络和 ImageNet-256 的方差结论不证明其它生成架构、数据、采样器或人类质量；FID 本身仍不是完整质量/安全指标。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20536v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20536v1#S5 — §5 Limitations and Recommendations`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `评测结果属于完整 Runtime Identity`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/html/2606.20537v1)

**2606.20537 — Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving**

**问题与旧路径。** Mainstream LLM serving systems reuse prefix work mainly through paged or radix key-value (KV) caches.

**机制、状态与控制流。** `Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving` 路由到 `INFER-REQUEST-LIFECYCLE`：Execution-State Capsule 在 graph-boundary 捕获可恢复的静态 buffer/执行状态，使 on-device small-batch serving 可 checkpoint/restore，而非重建整个 runtime；FlashRT 拥有 capsule schema 与兼容性，失配时冷启动。代价是图绑定、静态内存和 backend 特化。 唯一知识 owner 为 `INFER-REQUEST-LIFECYCLE`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20537v1#S2 — §2 FlashRT Runtime Substrate and Execution-State Capsules`；Evaluation=`https://arxiv.org/html/2606.20537v1#S4 — §4 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 只验证 NVIDIA CUDA backend、论文 graph/model/batch 和设备；未证明跨 driver/backend、故障一致性、并发恢复或生产 tail latency。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20537v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20537v1#S5 — §5 Limitations`。

**V3 Books 复验。** 当前 `INFER-REQUEST-LIFECYCLE` owner 为 [books/part-05-inference-system/42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)。Review notes 前正文 `Graph-bound Execution State 需要独立的 Restore Contract` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Current World Models Lack a Persistent State Core](https://arxiv.org/html/2606.20545v1)

**2606.20545 — Current World Models Lack a Persistent State Core**

**问题与旧路径。** World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking.

**机制、状态与控制流。** `Current World Models Lack a Persistent State Core` 路由到 `MULTIMODAL-WORLD-MODELS`：WRBench 把 camera motion 当 observability intervention，依次验证相机执行、在视场内连续性、离开视场后的状态演化和重新观察一致性；world-model evaluator 拥有 persistent-state verdict，普通 fidelity 指标仅并列。失败时回到显式 state memory/受限 camera。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20545v1#S3 — §3 WRBench Suite and Persistent-State Diagnostics`；Evaluation=`https://arxiv.org/html/2606.20545v1#S4 — §4 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** benchmark 只诊断论文 world models、camera paths 与 human calibration；未证明真实物理状态、因果动力学、长期遮挡或安全控制。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20545v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20545v1#S5 — §5 Limitations`。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前命题级锚点为 `World Model 评测要分离三种结论`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning](https://arxiv.org/html/2606.20553v1)

**2606.20553 — From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning**

**问题与旧路径。** Federated learning (FL) enables multiple parties to collaboratively fine-tune language models for domain-specific tasks without sharing raw data.

**机制、状态与控制流。** `From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning` 路由到 `PLATFORM-SECURITY`：联邦微调的效率路径被证明可承载 privacy backdoor；release contract 因此要在 client update 聚合前后检测泄漏触发与 utility，并由 server 持有 quarantine/rollback。安全聚合与效率优化需和隐私 red-team 共存。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20553v1#S3 — §3 Threat Model and §4 Privacy-Backdoor Attack`；Evaluation=`https://arxiv.org/html/2606.20553v1#S5 — §5 Evaluation`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 攻击与防御只在论文 FL topology、语言模型、clients 和 triggers 上验证；未证明 secure aggregation、异构数据或未知 covert channel。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20553v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20553v1#S6 — §6 Limitations`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `训练态共享统计也是隐私通道`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/html/2606.20562v1)

**2606.20562 — MemoryWAM: Efficient World Action Modeling with Persistent Memory**

**问题与旧路径。** Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling.

**机制、状态与控制流。** `MemoryWAM: Efficient World Action Modeling with Persistent Memory` 路由到 `MULTIMODAL-EMBODIED-VLA`：MemoryWAM 将 world-action model 的历史压入 persistent memory，在新 observation/action 时选择性读取和更新，使状态不完全依赖当前窗口；memory controller 拥有写入/遗忘，漂移时清空或回退无记忆 model。代价是错误状态累积和额外带宽。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity 的 handoff。

**Evaluation contract。** Method=`https://arxiv.org/html/2606.20562v1#S3 — §3 MemoryWAM Method`；Evaluation=`https://arxiv.org/html/2606.20562v1#S4 — §4 Experiments`；十字段条件见 Benchmark Contract。

**Trade-off、failure、fallback 与共存。** 实验限于论文 environments、horizons、models 和 memory sizes；未证明真实机器人、不可逆动作、长期漂移或 memory poisoning。 Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。


Claim boundary：仅 `arXiv:2606.20562v1` exact version；不使用 later version；未证明边界为 `https://arxiv.org/html/2606.20562v1#A1 — §Appendix A Additional Results and Limitations`。

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前命题级锚点为 `Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/html/2606.19348v1)

**问题与机制。** 单独扩大 accepted length、换一种 sparse attention 或把 KV 放到更慢介质，都只移动一个瓶颈。exact-v1 将 compressed sparse / heavily compressed attention、context parallelism、异构 KV 与 on-disk state 放进同一百万 token 系统，说明长上下文能力必须联合约束模型连接、训练通信、cache placement 与恢复路径。旧的 dense/full-attention 路径在短上下文、精确回读或异构 runtime 尚不成熟时仍更可靠。

**证据与边界。** Method=[§2 Architecture、§3 General Infrastructures](https://arxiv.org/html/2606.19348v1#S2)；Evaluation=[§4–§6 training/post-training/evaluation](https://arxiv.org/html/2606.19348v1#S4)。论文只能证明作者模型、训练栈和披露 benchmark 的组合，不把百万 token 接口外推为任意位置的有效利用、生产 tail-SLO 或任意硬件收益。

**Books 判断。** `MODEL-LONG-CONTEXT` 已以“位置有效性、Attention、KV 容量、利用率和 SLO 的联合能力”为主线，并已覆盖 sparse/hybrid attention、KV state 与异构 runtime 的共存边界；删除论文名后没有新增 owner-level 结论，故为 `No Change — Existing Coverage`。

### [Granularity-Regulated Adaptive Computational Efficiency for Optimal Verification in Test-Time Scaling](https://arxiv.org/html/2606.19354v1)

**问题与机制。** outcome verifier 便宜但信号稀疏，process verifier 细致但每一步都付费；固定二选一在任务难度、verifier accuracy 与 compute budget 变化时会失效。GRACE 把 verification granularity `g` 作为可调度状态，以理论假设连接计算成本、验证准确率和题目难度，再选择 ORM、PRM 或中间粒度。控制权属于 serving scheduler，verifier 只返回证据，不能自行扩张预算。

**证据与边界。** Method=[§3 Problem Formulation、Assumptions、Main Theorems、GRACE-Adapt](https://arxiv.org/html/2606.19354v1#S3)；Evaluation=[§4 MATH-500、GSM8K、AIME2024](https://arxiv.org/html/2606.19354v1#S4)。作者以 Qwen2.5-7B generator、ORM/PRM 和匹配计算预算比较粒度；结论依赖 accuracy 随 granularity 单调、log-concavity 等假设，且未披露生产并发、硬件与 tail latency。

**Books 判断。** 已整合至 `INFER-SCHEDULING` 的 `Verification Granularity 也是可调度的计算状态`。正文把验证粒度与 rollout 数、推理深度并列为 request-scoped compute state，同时保留静态 ORM/PRM 的稳定 workload 回退与定理、生产 SLO 的证据边界。

### [Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?](https://arxiv.org/html/2606.19388v1)

**问题与机制。** GUI 保留像素与交互布局，CLI 暴露结构化状态与组合动作；两者不是简单的“哪种接口更强”，而是不同 observation/action contract。实验把同一 mobile task suite 映射到三个 CLI harness，并以 oracle protocol 区分真正 terminal-solvable 的子集，说明接口粒度会改变 planning burden、权限面和 failure localization。

**证据与边界。** Method=[§3 Experimental Setup、§4 CLI-Advantage Suite](https://arxiv.org/html/2606.19388v1#S3)；Evaluation=[§5 Results](https://arxiv.org/html/2606.19388v1#S5)；Limit=[§6](https://arxiv.org/html/2606.19388v1#S6)。结果只覆盖 terminal-reachable state；视觉专属或 proprietary UI 不在结论内，且不能由受限任务排名推出 CLI 普遍优于 GUI。

**Books 判断。** `AGENT-TOOL-CALLING` 的 `Agent-friendly Tool 不等于把 CLI 包一层` 与 interface granularity 主线已完整承载该取舍，故为 `No Change — Existing Coverage`。

### [A Survey of Full-Duplex Spoken Dialogue Systems: Architectural Hierarchy, Interaction Ontology, and Decision State Machine](https://arxiv.org/html/2606.19453v1)

**问题与机制。** “支持 full-duplex”会把不同能力混成一个标签。exact-v1 将系统拆为 L0–L3 决策层级、turn × interruption × response interaction ontology，以及 Idle/Listen/Speak/Wait/Dual 状态机；它揭示的是决策 owner 与交互覆盖，而不是从模块化到统一模型的必然进步阶梯。L0 外部调度在安全、可解释和低数据场景仍合理。

**证据与边界。** Method=[§4 Architectural Hierarchy、§5 Interaction Ontology、§6 Decision State Machine](https://arxiv.org/html/2606.19453v1#S4)。这是 survey 与 cross-system audit，没有统一受控 benchmark；名义 ontology cell 不等于训练数据或系统已经覆盖，L3 也仍是概念边界。

**Books 判断。** `MULTIMODAL-REPRESENTATION` 已把 timestamp、stream revision、interrupt boundary 和 safe-point commit 写成在线状态路由，且保留 utterance-level fallback；该 survey 不再改变正文结论，故为 `No Change — Existing Coverage`。

### [Diffusion Language Models: An Experimental Analysis](https://arxiv.org/html/2606.19475v1)

**问题与机制。** 以“AR 对 DLM”做单一范式排名，会混淆训练规模、denoising steps、block size、context 和 unmasking policy。论文在统一协议下比较多种模型，并显示不同任务与执行配置会改变质量—成本排序；因此 DLM 是条件化替代分支，不是线性取代 AR。

**证据与边界。** Method=[§4 Experimental Setup](https://arxiv.org/html/2606.19475v1#S4)；Evaluation=[§5 Large-Scale Analysis](https://arxiv.org/html/2606.19475v1#S5)；Conclusion=[§6](https://arxiv.org/html/2606.19475v1#S6)。跨模型训练配置并非完全 apples-to-apples，作者结果不能生成不绑定 sampler、长度与 workload 的通用性能结论。

**Books 判断。** `MULTIMODAL-GENERATIVE-PARADIGMS` 已按 editable state、commit boundary、block size、correction 与 cache/streaming 合同比较这些分支，故为 `No Change — Existing Coverage`。

### [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/html/2606.19531v1)

**问题与机制。** 先生成完整未来视频再提取动作，保留了可视化中间产物，却把渲染成本和像素质量错误地设为 action handoff 的必要条件。ImageWAM 以 endpoint-frame image editing 训练 world-action context，并让 action expert 直接读取 denoising-layer KV；generative state 可以在 final frame decode 前交给控制分支。denoiser 拥有 latent proposal，action controller 与 safety verifier仍拥有物理提交权。

**证据与边界。** Method=[§3 Architecture、Action Prediction、Efficient Inference](https://arxiv.org/html/2606.19531v1#S3)；Evaluation=[§4 LIBERO、RoboTwin2.0 与 real-world tasks](https://arxiv.org/html/2606.19531v1#S4)。作者环境中的 success rate 不证明广泛 sim-to-real、不可逆动作安全或 denoising KV 是因果充分状态。

**Books 判断。** 独立对读后改为 `No Change — Existing Coverage`。canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，不是 Ch25；其 `World-action model` 正文已完整写出 `explicit future rollout → joint generation → direct latent predictive interface`，并明确 action branch 可消费 layer-wise KV / compact dynamics state 而不 materialize future video，物理 commit 仍归 controller 与 safety envelope。

### [Displacement Is Not Direction: Evaluating Fidelity Metrics for Quantized LLM Deployment](https://arxiv.org/html/2606.19558v1)

**问题与机制。** KLD 或 perplexity 能发现明显量化破坏，却只测 distribution displacement，不保证变化方向与 downstream quality 一致。论文在两个模型 family 的多种 GGUF 量化上发现 near-baseline silent zone：代理指标在该区域不能可靠排序候选。发布 Gate 因而需要两段式控制——明显退化区用 proxy 粗筛，silent zone 内回到任务级评测与置信区间。

**证据与边界。** Method=[§3 Methodology](https://arxiv.org/html/2606.19558v1#S3)；Evaluation=[§4 Silent Zone、§5 Disagreement Volume and Direction](https://arxiv.org/html/2606.19558v1#S4)；Limit=[§6](https://arxiv.org/html/2606.19558v1#S6)。阈值是 cohort-specific 描述，不是跨模型、量化器或任务的通用 routing threshold。

**Books 判断。** 独立对读后改为 `No Change — Existing Coverage`。`PLATFORM-EVALUATION-SYSTEM` 已明确压缩模型的 release gate 不能停留在平均 perplexity，并要求 threshold-adjacent candidate 回到 item-level transition、calibration、OOD、真实 runtime artifact 与 downstream churn；silent-zone 是该既有原则在两个量化 cohort 上的受限证据，不形成新的 owner-level 机制。

### [Which Pairs to Compare for LLM Post-Training?](https://arxiv.org/html/2606.19607v1)

**问题与机制。** 固定 label budget 下，随机取得多少 preference pairs 不是唯一变量；比较哪些 response pair 会改变信息矩阵，进而影响 DPO estimator 与 policy gap。论文把 pair acquisition 写成 sampling design，并给出依赖覆盖与 regularity 的上下界，使 label-generation 成本与 human-label 成本成为可显式优化的两类预算。

**证据与边界。** Method=[§2 Problem Definition、§3 Main Results / Sampling Policy Design](https://arxiv.org/html/2606.19607v1#S2)；Evaluation=[§4 Numerical Experiments](https://arxiv.org/html/2606.19607v1#S4)；Limit=[§5](https://arxiv.org/html/2606.19607v1#S5)。理论依赖 realizability、coverage 与正则条件，离线 randomized design 不证明 adaptive feedback 环境中的收益。

**Books 判断。** 已整合至 `TRAIN-DPO` 的 `Preference Pair 选择是实验设计，不只是数据量选择`。正文绑定 response generation、pair sampling、标注预算与 provenance，并保留随机/分层采样 fallback 及离线理论边界。

### [Hard or Just Unreached? Diagnosing the Sampling Blind Spot in Math-Reasoning Difficulty Estimation](https://arxiv.org/html/2606.19636v1)

**问题与机制。** `pass@k=0` 只表示给定 sampler 和预算没有到达正确轨迹，不等于模型表示中不存在可恢复路径。论文在匹配 forward-pass 成本下，以 residual-stream intervention 恢复部分原本零通过样本，说明难度标签必须保存 sampling identity，并把 coverage failure 与 capability absence 分开。

**证据与边界。** Method=[§3 Setup、§6 Residual-Stream Perturbation](https://arxiv.org/html/2606.19636v1#S3)；Evaluation=[§5–§7](https://arxiv.org/html/2606.19636v1#S5)。四个开放模型、三个数学 benchmark 和单一 layer/position 的结果只证明 intervention 下的可达性；它不是普通 decoding，且多数样本仍未恢复。

**Books 判断。** `PLATFORM-EVALUATION-SYSTEM` 已明确 `pass@k` 是有限 sampling budget 的覆盖率、不是分布不可能性证明，故为 `No Change — Existing Coverage`。

### [Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization Across Preference Settings](https://arxiv.org/html/2606.19744v1)

**问题与机制。** 只比较 sequential DPO 前后的 aggregate score，会把 objective compatibility、signal strength、训练顺序与 pair-level redistribution 混成“遗忘”。论文冻结 evaluation reference，并联合检查 pair margin、quartile、gradient 与 adapter movement，表明 release owner 应保存 objective relation 与顺序，而非让平均分拥有 verdict。

**证据与边界。** Method=[§2 Sequential DPO、§3 Evaluation Protocol](https://arxiv.org/html/2606.19744v1#S2)；Evaluation=[§4 Results](https://arxiv.org/html/2606.19744v1#S4)；Limit=[§5 Limitations](https://arxiv.org/html/2606.19744v1#S5)。证据限一个 8B 模型、LoRA、四类 preference regimes 和固定超参，不是 full-parameter 或跨模型定律。

**Books 判断。** 已整合至 `TRAIN-DPO` 的 `Sequential DPO 必须保留目标关系与训练顺序`。正文要求 campaign identity 保存 objective relation、stage order、reference revision 与 pair provenance，并保留单阶段 DPO 的适用边界。

### [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](https://arxiv.org/html/2606.19919v1)

**问题与机制。** 对整段 response 施加长度惩罚，可能同时惩罚正确但确需长推理的轨迹。ADaPT 在 SFT 中引入 fast/slow mode token，并在 GRPO 中只把 efficiency reward 作用于第一个 mode-selection token，正确性 reward 留到终态；credit owner 因此从“所有生成 token”收缩到选择计算路径的 action state。

**证据与边界。** Method=[§3.2 ADaPT-SFT、§3.3 ADaPT-GRPO](https://arxiv.org/html/2606.19919v1#S3)；Evaluation=[§4 reasoning benchmarks](https://arxiv.org/html/2606.19919v1#S4)；Limit=[§7](https://arxiv.org/html/2606.19919v1#S7)。证据限二元模式、有限 reasoning benchmark 和小中型模型，不证明开放式 workload 或连续预算控制。

**Books 判断。** canonical owner 仍是 `TRAIN-GRPO`，但独立对读后改为 `No Change — Existing Coverage`。该章已经把 typed credit 对齐到实际 state-action boundary，并规定 terminal outcome/verifier 拥有 reward direction、局部 process signal 只调节幅度；fast/slow mode token 是这条原则的二元实现案例，不能因一个受限 benchmark 再扩写同一机制。

### [VIMPO: Value-Implicit Policy Optimization for LLMs](https://arxiv.org/html/2606.20008v1)

**问题与机制。** GRPO 的 group baseline 不产生稳定 token-level credit，PPO 的 learned critic 又增加独立模型与训练误差。VIMPO 在 deterministic token-prefix MDP 中把 policy/reference log-ratio 写成 KL-regularized Bellman recurrence，以 terminal reward anchor 构造 policy-implied value，再用于 PPO-style advantage；它形成 group estimator 与 learned critic 之间的中间分支。

**证据与边界。** Method=[§3 Methodology](https://arxiv.org/html/2606.20008v1#S3)；Evaluation=[§4 MATH-500、AIME、OlympiadBench](https://arxiv.org/html/2606.20008v1#S4)；Limit=[§5](https://arxiv.org/html/2606.20008v1#S5)。fixed reference、beta schedule 与 exact-KL 成本仍是状态和 failure source；数学任务结果不证明通用 agent RL。

**Books 判断。** 已整合至 `TRAIN-GRPO` 的 `Policy-implied Value 是 Group Baseline 与 Learned Critic 之间的条件分支`。正文保留 group estimator、policy-implied value 与 learned critic 的共存条件，以及 reference、系数和 exact-KL 的状态与失败边界。

### [What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis](https://arxiv.org/html/2606.20075v1)

**问题与机制。** outcome-only supervision 进入 latent reasoning 时会同时遇到两类坍塌：长优化路径造成 gradient attenuation，latent manifold 又可能偏离可用语义。论文区分 trajectory supervision 与 space supervision；前者用中间步骤提高路径信息，后者以 generative reconstruction 约束表示，而不是强迫逐点几何对齐。

**证据与边界。** Method=[§3 Optimization Barrier、§4 Process Supervision、§5 Information-Theoretic View](https://arxiv.org/html/2606.20075v1#S3)；实验细节见 [Appendix A](https://arxiv.org/html/2606.20075v1#A1)。结果支持作者 latent-CoT 设置中的 information–performance binding，不是所有隐藏推理的通用定理，也不证明 latent state 可解释或安全。

**Books 判断。** 已整合至 `TRAIN-PRETRAINING` 的 `Latent Reasoning 要分开路径优化与表示空间约束`。正文把 gradient attenuation 与 latent representation drift 分成不同传感器和修复路径，并保留 outcome-only 与显式 reasoning 的适用条件。

### [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/html/2606.20092v1)

**问题与机制。** 周期采样或完整历史 buffer 在长时 manipulation 中要么错过瞬态证据，要么无界增长。EventVLA 维护稀疏 Keyframe Evidence Memory：KEM 从 action-horizon hidden state 预测未来效用，阈值触发写入，并以 FIFO、NMS/cooldown 控制容量；memory write owner 与 action policy 分离，证据必须在离开视场前提交。

**证据与边界。** Method=[§3 EventVLA Framework](https://arxiv.org/html/2606.20092v1#S3)；Evaluation=[§4 RoboTwin-MeM、§5 simulation/real robot](https://arxiv.org/html/2606.20092v1#S4)；Limit=[§6](https://arxiv.org/html/2606.20092v1#S6)。阈值、自动标签和有限 buffer 会漏写或覆盖关键证据；作者任务不构成通用物理安全或 sim-to-real 保证。

**Books 判断。** 已整合至 `MULTIMODAL-EMBODIED-VLA` 的 `瞬态视觉证据需要在消失前完成写入决策`。正文分离 memory controller 与 action policy 的 authority，并保留固定窗口、周期采样和人工 milestone 的回退边界。

### [HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization](https://arxiv.org/html/2606.20097v1)

**问题与机制。** 按 layer 统一替换 full attention，隐含同层所有 heads 对精确历史访问同样敏感。HydraHead 先用 activation/path patching 估计 head 功能，再为 retrieval/reasoning-critical heads 保留 full attention，其余转为 GDN，并通过迁移、层级对齐、logit distillation 和长上下文微调恢复。

**证据与边界。** Method=[§4 Head Importance、Head-wise Hybridization、Transfer](https://arxiv.org/html/2606.20097v1#S4)；Evaluation=[§5 Qwen3-1.7B、RULER 与 reasoning](https://arxiv.org/html/2606.20097v1#S5)；Limit=[Appendix C estimator caveats](https://arxiv.org/html/2606.20097v1#A3)。证据主要来自一个 compact dense model，未证明大模型、MoE、多模态或 serving tail-SLO。

**Books 判断。** `MODEL-LONG-CONTEXT` 已有 hybrid attention 的 exact-access budget 与 layer/head sensitivity 路线，故为 `No Change — Existing Coverage`。

### [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/html/2606.20104v1)

**问题与机制。** 只优化 latent forward prediction 可以用常量表示获得低损失，却丢失控制所需状态。论文联合 encoder、forward predictor 与 inverse dynamics；inverse loss 要求从相邻 observations 恢复 action，从而阻止 constant collapse，并偏向保留 action-controllable information。

**证据与边界。** Method=[§3 Method、Appendix A Training Objective](https://arxiv.org/html/2606.20104v1#S3)；Evaluation=[§4 Learned Latent Structure、§5 Planning](https://arxiv.org/html/2606.20104v1#S4)；Limit=[§6 Discussion](https://arxiv.org/html/2606.20104v1#S6)。机制依赖 action 可由相邻观测恢复；partial observability、行为策略偏置和不可控但任务相关因素可能被错误丢弃，实验只覆盖中等复杂度模拟环境。

**Books 判断。** 已整合至 `MULTIMODAL-WORLD-MODELS` 的 `Inverse Dynamics 是有前提的 Anti-collapse Regularizer`。正文明确 action recoverability 前提、partial observability 与 uncontrollable state 的失败路径，并保留更完整预测目标的 fallback。

### [Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families](https://arxiv.org/html/2606.20225v1)

**问题与机制。** 单模型中可分离且可 steering 的 activation direction，不代表跨模型映射后仍具有因果 specificity。论文对四个小模型做 insecure-code fine-tuning、direction extraction、cross-model ridge mapping 和随机/正交 controls，发现 within-model 因果效果较清楚，而 cross-model controls 常产生相近变化；监测与干预必须分成两级 contract。

**证据与边界。** Method=[§3 Methodology](https://arxiv.org/html/2606.20225v1#S3)；Evaluation=[§4 Results、§5 Implications](https://arxiv.org/html/2606.20225v1#S4)；Limit=[§6](https://arxiv.org/html/2606.20225v1#S6)。证据限小模型、单一 misalignment domain 和 activation steering，不能把跨模型 correlation 升级为 transferable safety sensor。

**Books 判断。** 已整合至 `PLATFORM-SECURITY` 的 `Learned Security Sensor 与 Reference Monitor 必须分层`。正文区分 within-model causal probe 与 cross-model mapped candidate sensor，要求重新验证 specificity，并将 mitigation authority 留给外部 policy/reference monitor。

### [How Transparent is DiffusionGemma?](https://arxiv.org/html/2606.20560v1)

**问题与机制。** 并行/迭代生成可能暴露可编辑 token bottleneck，但“变量可读可改”不等于算法步骤被完整重建。论文区分 opaque serial depth、bottleneck intervention 和 monitorability，并显示 interpretable token canvas 能减少不透明上界；同时 non-chronological correction 与 smearing 仍使内部算法难以恢复。

**证据与边界。** Method=[§2 Opaque Serial Depth、§3 bottleneck ablation](https://arxiv.org/html/2606.20560v1#S2)；Evaluation=[§3–§5 code/math/QA 与 monitorability](https://arxiv.org/html/2606.20560v1#S3)；Limit=[§8.1](https://arxiv.org/html/2606.20560v1#S8.SS1)。serial-depth 是上界，monitorability 与 architecture/training cause 均未完全辨识；结果只约束该模型与 sampler。

**Books 判断。** 已整合至 `MULTIMODAL-GENERATIVE-PARADIGMS` 的 `Transparency 不是单一的“可解释程度”`。正文将 variable transparency、algorithmic transparency 与 safety monitorability 拆成独立合同，并保留 AR/opaque diffusion 的适用边界。

### Books / semantic audit

Fresh-context 终审以首个 `Review notes` 为正文边界。最终 64 个冻结候选中，22 项已在正文形成完整机制链（旧批次 13 项、恢复 9 项），42 项有不依赖 source trace 的命题级覆盖。写后独立复核逐项检查 9 个新增 marker 的唯一性、正文位置、owner/state flow、trade-off、failure、fallback 与 exact-v1 non-proof 边界；其中 4 项从章末导航或首个 Review notes 后移回对应机制主线后通过。Books queue 为 0。

## 5. 缺口与下一步

当前确定候选普通待办、待写与待POST均为0。以下本窗终态保留项不用于正面证据、Books采用或无遗漏断言，不支持覆盖通过；已完成有效层不重读。各项定点重开条件如下，独立日级/最终验收见§6。

日期未定的五个精确身份：[18273](https://arxiv.org/abs/2606.18273)、[18286](https://arxiv.org/abs/2606.18286)、[18307](https://arxiv.org/abs/2606.18307)、[18304](https://arxiv.org/abs/2606.18304)、[18323](https://arxiv.org/abs/2606.18323)。前三唯一v1为Jun5/Jun10/Jun16早时段，后两亦Jun16 cutoff前，至Jun18 arxiv.content/findable登记的合法区间跨日，不能截取Jun18。已核精确official history/登记、有限作者原入口与具名OAI（18273仅metadata created/updated）；catchup只回90日限制、月列表无目标日分组。advanced虽有announced_date_first，其帮助只年/月，knownpositive18524的合法日期范围也空，不把空响应当未公开。现有原入口未恢复可接受日约束，保贡献线索而不formal、不评分、不进Books；只在该身份官方日公告、明确首次正文日期或可复查延期/发号原记录到达时重开归属，不再猜时刻或重复Methods。该局部跨日限制不否定其他33项合法联合日期。

[GDM agent security](https://deepmind.google/blog/securing-the-future-of-ai-agents/)当前display/og/datePublished均Jun18（14Z），modified亦Jun18；完整官方RSS同canonical却为Jun16 15:46:31Z。现有原件无法确定哪一字段对应首次正文公开，不断言Jun16全文已公开，也不以新metadata抹早信号。仅此家族隔离，不formal/评分/Books或支撑Coverage；重开需官方原版本/更正说明或有内容身份的原发布记录，现无可执行的独立版本记录可消除冲突。

来源历史限制：Meta Research/Blog与官方publication替代入口分别无可读正文/访问失败及login block，有限Jun18官方域补检未补日目录；Google Pubs只年/主题过滤、不暴露日级公开列表，Google June Blog与DeepMind Publications有界邻域已核，不把全年434项变方法队列。不可得范围不支持“该机构历史无遗漏”；恢复需官方可访问目标日目录、发布页或明确版本事件列表，只补相关窗口。其余来源只授§2记录的当前集合/页段，未保证目录删改史。

19268中心几何证明争议在§4有moment/谱桥与重开条件，Books暂缓且不作正证，不是改N或已有覆盖。窗外18558：Ai2官方Blog/Research/Molmo目录明确June17正文并称releasing today，按date-only归属退出本日；本轮两段及本人注已可恢复撤用、旧GMM邻接恢复，soleR44实际POST通过。必要/稿证留在canonical，只有真实Jun17恢复授权或独立Jun18新事件才继续，不新建Daily、不移动旧候选。

### Repository Changes

本轮只更新本Report与同日_sources；新增27整合分布18个既有owner，另有原19386 Ch67证据纠错与旧18967 Ch48采用链修复，均不重计。正文经完整PRE、窄SAVE、自读、sole实际POST；18558只撤本人新增，不动旧GMM或并发内容。未改公共合同/ROADMAP/checker，未stage、unstage、commit、push或操作automation，State由root协调。原小时窗的9恢复/8owner历史保有效层，不混作本轮新增统计。

## 6. 复核

复核者：jun19_supp_reader（唯一独立非writer）。

结论：通过

唯一日级DAY为[独核R73](../_sources/daily-20260619/SUP_REVIEW_20261029.md#r73-day--本日独立语义通过)，实际核十四来源查询/停止、全部新增33的贡献/日期/精确版本/轻量信号及必要证据，27份整稿与真实写后POST、5个具体NC及19268争议隔离；旧64有效层复用但Date/评分逐项机械对读无差额。已修复14dup误计、新版反灌、18558早正文误归属、19386书稿及Report依赖失配、19268误N和目录停止范围，未改分清待办。

排除分层独核：18785、19340、18837、18363、18463、18677、18773、18379、19315共9个完整题摘/决定点，另3个OpenAI当窗页核心；覆盖范围边界、成熟组合、数值通信、推荐/隐私与形式证明。19268/18831的反侧已重开并核其必要证据；19340/18837/18463/18677轻量事件信号抽检。未检查范围是宽499导航中无约定逐项队列的无关项、无关附件及已有效旧层未变化部分，不把抽检称全部全文重读。

独立V3校验、本地链接缺失[]、旧64 Date/三维评分差额[]、97唯一、26新增arXiv整合marker逐owner唯一（另beneficial机构真实层）、限定20 Books+本Report/同日source diffcheck均通过；这些只证明可判定一致性，语义结论来自上述实际审阅。完成态的实际终存核验与本次复核共用[唯一独核记录](../_sources/daily-20260619/SUP_REVIEW_20261029.md)，不另建平行收据。以下仅为原小时窗历史复核，有效证据保留，其旧“当前”与完成范围不替代本轮日级结论。

当前来源再认证复核者：\`june_11_20_recert\`（独立于原报告作者）。当前合同来源再认证补齐十三个官方 Daily 源；识别同一项 Anthropic owner-day 外部材料缺口并终态保留，未把日期不明材料用于候选、评分或 Books。

复核者：june_19_books_gate（独立于候选发现、Evidence 审阅与上一轮 Books queue 作者）
复核范围：12 个 Books writeback proposal、其 exact-v1 title/abstract/Method/Evaluation/limitations，以及 9 个 canonical owner 章节在 `## Review notes` 前的当前命题与相邻 handoff。
复核发现与修复：上一轮 queue 仍有 3 个 false-positive Integrate。`2606.19531` 的 latent predictive interface 已在 Ch26 `World-action model` 正文完整存在，且原 owner 指向 Ch25 不准确；`2606.19558` 的 silent-zone 只是既有 compression/threshold-adjacent release contract 的受限量化证据；`2606.19919` 的 mode token 是既有 typed credit / state-action boundary 原则的二元实现案例。三项均改为 Existing；其余 9 项确有当前 owner 尚未承载的长期状态、控制权或评价合同增量。
写前复核结论：Coverage 与 Evidence 继续通过；最终 64 candidates / 526 pre-denominator closures；当时识别出 13 已落实 / 42 Existing / 9 owner-level 待写入。该中间态已由以下写后审计闭合。

复核者：june_19_postwrite（独立于候选发现、Evidence 审阅、写前 Books Gate 与正文写入者）
复核范围：9 个最终 Integrate Source Family、8 个 canonical owner 章节及相邻语义、日报 decision/queue/repository changes/open questions 与写后 artifact。
复核发现与修复：9/9 正文语义成立且 evidence boundary 未越权；其中 `2606.20075`、`2606.20092`、`2606.20104`、`2606.20225` 虽已写入，但原落点位于自检、知识树导航、Reflection 或首个 Review notes 后，已分别移至 Pretraining 机制段、episode memory、latent dynamics 与 CoT monitor/security sensor 主线。9/9 marker 精确唯一且位于首个 Review notes 前。
原复核结论：64 candidates / 526 pre-denominator closures；22 Integrated / 42 Existing / 0 queued；Candidate、Evidence、Books 与 post-write Gate 通过。当前 source recert 追加一项外部日期材料缺口，因此 Coverage 只达到已记录缺口的安全终态，不宣称 gap-free。
结论：通过

Candidate/Evidence/Books 通过；Coverage 以一项已记录的外部日期缺口安全终结。
