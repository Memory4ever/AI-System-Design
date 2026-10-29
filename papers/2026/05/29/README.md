# Daily Research — 2026-05-29

**规范：** V3

**窗口：** 2026-05-28T09:00:00+08:00 ～ 2026-05-29T09:00:00+08:00

**补充窗口：** 2026-05-28 ～ 2026-05-28

**冻结候选日期：** [补查前真实原档案](../_sources/daily-20260529/baseline-before-supplement-20261021.md)

**窗口说明：** 用户授权2026已有Daily增量补遗漏，保留旧候选日期、评分及原小时窗口；新增材料按前一完整北京时间自然日检查，不重新定时或重审有效旧层。

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-10-21T15:32:07+08:00

> 以下原完成声明及旧层统计只适用于原冻结小时窗。本轮由supp_may29_author唯一作者、root唯一非作者复核，已另经R20整日六部分验收通过；原116候选完整行及连续原§4保留。

> 前一轮 fresh non-author 对抗复核发现并有界修复了两条 owner-status 投影、TaskMem 缺失评分、Redpanda binding marker 位置及随后产生的正文 hash 漂移。另一位未参与 author rebuild、Books writeback 或该轮修复的 fresh reviewer 已逐项验证这些修复；本日 Evidence、Books 与独立复核 Gate 均闭合。

## 1. 结论

本轮补May28自然日新增52个唯一家族：49个按arXiv公告/登记联合界落窗、1个Google官方先公开honeypot、Opus4.8及Kimi Code v0.5两个版本事件。逐项必要审阅与Books处置为23项真实整合、27项具体已有覆盖、1项仅报告、1项中心主张争议隔离；原116完整行/日期/评分保留，合168。本轮没有候选数或保留率配额，不把宽目录命中总数称当天新论文数。

主要变化是训练反馈/参考与真值分权、上下文和工具状态的接口身份，以及采样/表示目标的条件边界。全部23项书稿差额均经root必要Source/具体owner与真实写后检查通过，本版六部分整体DAY由root R20实际通过，研究及Books普通待办为0；A-CBO定理/查询条件争议不进入Books，OpenAI/Meta历史索引与Hunyuan旧Research档案保证缺口不支持完整Coverage或无遗漏。

原冻结小时窗确认824个唯一raw Source Family：823个arXiv identity与1个Seed TaskMem官方事件，历史守恒为 `824 = 116 retained + 708 pre-denominator closure + 0 withdrawn`；arXiv子集 `823 = 115 + 708 + 0`，由623个OAI direct与200个initial-registration recovery组成。原116候选有效审阅与13 Applied、102 No Change、1 Report Only不重做；该统计不含本轮增量。

原层归档说明：TaskMem的Seed官方事件早于 `arXiv:2605.31075v1` 的后续论文批次，两者属于同一Source Family。旧fresh review发现“只保留TaskMem、隔离823 arXiv identities”的owner口径与权威日期依据冲突；该旧修复轮只恢复冻结corpus及既有exact-v1/adopted-proposition证据，没有扩来源、日期或改共享Books。这不是2026-10-21补查52家族的范围声明。

## 2. 来源覆盖

本表记录2026-05-28自然日补查的实际入口与停止位置。旧小时窗来源、筛选与审阅仍按有效层复用，不把旧全量列表转成本轮逐项队列；具名查询/排除、去重与尾项在[唯一作者记录A1–A16](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。覆盖指这些公开入口与主题切片已处理，不宣称全球无遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS访问失败后，限定官方域与May28恢复FGF发布及PDF§1/2.1–2.3；GPT5.5Instant release核心只作版本线索 | 受阻 | FGF实际为现有实践/法律披露映射，未识别新增release/risk机制，贡献前关闭；历史Research/RSS索引不可读的覆盖保证隔离，不影响已读官方正文 |
| SRC-ANTHROPIC | Research索引失败后，官方May28 Opus4.8 news核心/评价脚注；必要Messages API system-entry域，未扩全卡 | 已检查 | 新增Opus接口家族；未独核卡摘要精确OSWorld数字不采用，不从营销或客户引言授性能/安全 |
| SRC-GOOGLE-AI | Research 2026/05月档May28/27/19/1；DeepMind blog真实page2/3至March、publication目标May28两篇253391/252981 | 已检查 | I/O recap贡献前关闭；Gram与原116同事件去重；honeypot新增，官方date-only足够自然日不再追时刻；不扩AI for Science |
| SRC-META-AI | Research SPA与publication入口，后者本次仅45chars异常；May28官方域/具名标题限定检索未恢复历史日切片 | 受阻 | 历史Research/Publications分页缺口隔离；第三方RADAR提交日不作公开日期，详§5；不作零命中或全覆盖断言 |
| SRC-QWEN | 官方前端GET qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US，完整当前40条未排序，实际核May19/20/29近邻 | 已检查 | 当前响应无May28条，40条不是所有历史文章全集；结论只限此次可见入口，不授隐藏/删除条目覆盖 |
| SRC-DEEPSEEK | 官网research/paper与官方api-docs.deepseek.com/updates，实际日期July31→April24→2025Dec1停止 | 已检查 | 公开目录目标处无条目；不将2025May28更新误计2026，也不称所有隐藏历史研究为零 |
| SRC-MOONSHOT | Platformblog只至2025Nov；Kimi Code官方What'sNew到May29v0.6→May28v0.5→May27v0.4边界，目标核心已读 | 已检查 | v0.5调度与/auto合同新增Only；不从后续docs倒推历史实现，不遍历组织所有仓库 |
| SRC-TENCENT-HUNYUAN | research SPA所用publicList最后窄核：POST pageNum=1/pageSize=1000/renderType=0（All），accept-language:zh；HTTP200/code0，totalNum与list均11，含Papers7/Models4；[必要原字段](../_sources/daily-20260529/supp-hunyuan-all-zh-necessary.json)。显示日期邻界July6 Hy3→May21 Hy-MT2→Apr30 context，11项题名及三日期字段无May28 | 受阻 | 当前All/zh列表已处理，纠正默认en9仅blog的覆盖不足；现站不能证明旧Research被隐藏/删除的历史全集，仍不授完整历史Coverage；Hy3preview显示Apr23而publishedAt June24/publicAt July5，字段不混用；重开见§5 |
| SRC-ZAI | 官方Research当前卡Aug→June→May20ZCube→April29；release-notes/new-released Aug26/18→June16→April7停止 | 已检查 | 所查公开目录目标无条目；不遍历zai-org库存，也不把空搜索证明无遗漏 |
| SRC-BYTEDANCE-SEED | 真实get_article_list_v2、x-tt-locale US：Publication1空token/count20，18visible/total86/moretrue/next20，读至May29TaskMem→May26FFN；Blog2 15visible/total20/morefalse June19→April23 | 已检查 | 按目标日期边界停止而非扫86篇；TaskMem是原116有效家族，本轮不重复或搬日期；日期附近无新增入选 |
| SRC-BAIDU-ERNIE | 官方zhblog第一屏10cards，May9→April30/15→2025Nov，读过目标日期边界停止 | 已检查 | 可见公开目录无目标条；不扩大普通NLP/科学应用或仓库修复队列 |
| SRC-XIAOMI-MIMO | 官网Paper June29MOPD→March13ARLTangram→Feb3HySparse；唯一Blog卡定点正文核Sep27 | 已检查 | 原无日期卡已解为窗外；MiMoCode产品入口非具名本窗研究，不按猜测404建立候选；不称当前目录为历史全集 |
| SRC-MINIMAX | EN/ZH Blog当前完整可见列表June1以上/May27/26，ZHMay25/April27；Agent Tech Blog最早Sep19 | 已检查 | 日期差异按各官方页面保留，目标无新增；不把翻译页日期当第二家族或扩大techblog历史 |
| SRC-ARXIV | 三组主线同义主题API、实际199/316/113返回作线索；有界cs.CL官方May月末页相关标题补检（skip2000/show2000，目标ID27500–28822）；完整题摘→精确去重→贡献准入 | 已检查 | 宽列表不逐项关闭/全文化；新增49个v1按DataCite/公告联合界落May28，已核必要Source/owner；另29729由Google官方先公开。不授全学科召回 |
| 补检：[DataCite](https://api.datacite.org/) | 官方arXiv公告/发号规则与[首30原字段](../_sources/daily-20260529/supp-datacite-v1-raw.json)、[第四24原字段](../_sources/daily-20260529/supp-datacite-fourth24-raw.json)，Submitted-v1/arxiv.content/findable/registered联合界 | 已检查 | registered只是公告最晚界，不改名实际公开时刻；整个可能区间均May28BJT，身份/字段root逐项独核；不证明全球更早渠道绝不存在 |

本轮无独立会议/release固定清单触发；具名必要版本/官方发布证据均在对应来源内处理，未扩Weekly/Live。旧小时窗的[source-coverage-v3.json](../_sources/daily-20260529/source-coverage-v3.json)、[screening-outcomes-v3.json](../_sources/daily-20260529/screening-outcomes-v3.json)与[arXiv owner receipt](../_sources/arxiv-owner-replay-20260903/20260529/arxiv-owner-receipt.json)仅是原层有效依据，不作为本轮已完成扫描的替代。

## 3. 候选与判断

前116行按用户授权保持原顺序、原公开时间/评分与有效判断；其后52行是本轮May28自然日新增，不重复计同事件。下面连续原§4原文保留为旧层证据，末尾另接本轮逐项必要证据，历史完成用语不代替当前复核。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ReclaimNet: Reclaim-Aware Network Protocols for Voluntary GPU Sharing on Campus](https://arxiv.org/html/2605.28872v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-GPU-SCHEDULER；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-GPU-SCHEDULER，[目标章](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)；已落实 |
| [Pre-Registering the Detectable Effect: A Paired-MDE Budget for 4-bit Quantization Benchmarks, with a Pilot Audit](https://arxiv.org/html/2605.28873v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LogDx-CI: Benchmarking Log Reduction Tools for LLM Root-Cause Diagnosis](https://arxiv.org/html/2605.28876v1) | 2026-05-29T08:00:00+08:00 | AGENT-CONTEXT；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-CONTEXT，[目标章](../../../../books/part-07-agent/75-context.md) |
| [GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human](https://arxiv.org/html/2605.28882v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Context Distillation as Latent Memory Management](https://arxiv.org/html/2605.28889v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md) |
| [Echoes within the Reasoning: Stealthy and Effective Watermarking via Chain of Thought](https://arxiv.org/html/2605.28890v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities](https://arxiv.org/html/2605.28893v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Review Arcade: On the Human Alignment and Gameability of LLM Reviews](https://arxiv.org/html/2605.28897v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AIRGuard: Guarding Agent Actions with Runtime Authority Control](https://arxiv.org/html/2605.28914v1) | 2026-05-29T08:00:00+08:00 | AGENT-TOOL-CALLING；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md) |
| [When LLM Reward Design Fails: Diagnostic-Driven Refinement for Sparse Structured RL](https://arxiv.org/html/2605.28918v1) | 2026-05-29T08:00:00+08:00 | TRAIN-GRPO；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md) |
| [Conf-Gen: Conformal Uncertainty Quantification for Generative Models](https://arxiv.org/html/2605.28920v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beyond Recall: Behavioral Specification as an Interpretive Layer for AI Personalization](https://arxiv.org/html/2605.28969v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md) |
| [A Secure, Manifest-Based Framework for Delegated Privilege Promotion](https://arxiv.org/html/2605.28991v1) | 2026-05-29T08:00:00+08:00 | AGENT-TOOL-CALLING；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md) |
| [Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening](https://arxiv.org/html/2605.28999v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FormInv: A Measurement Protocol for Semantic Invariance in Mathematical Reasoning Benchmarks](https://arxiv.org/html/2605.29001v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LoRe: Adaptive Interaction-Evaluation Routing with Per-Step Interaction Budgets for Iterative Graph Solvers](https://arxiv.org/html/2605.29005v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Converted, Not Equivalent: Benchmarking Codebase Conversion via Observational Equivalence](https://arxiv.org/html/2605.29054v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Robust and Efficient Guardrails with Latent Reasoning](https://arxiv.org/html/2605.29068v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Embodied3DBench: Benchmarking Low-Level Embodied Spatial Intelligence of Vision Language Models](https://arxiv.org/html/2605.29074v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Knowledge Offloading: Decomposing LLMs into Sparse Backbones and Memory Modules](https://arxiv.org/html/2605.29075v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md) |
| [Bridging the Sim-to-Real Gap in Reinforcement Learning-Based Industrial Dispatching through Execution Semantics](https://arxiv.org/html/2605.29078v1) | 2026-05-29T08:00:00+08:00 | AGENT-WORKFLOW；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md) |
| [The Importance of Out-of-Band Metadata for Safe Autonomous Agents: The Redpanda Agentic Data Plane](https://arxiv.org/html/2605.29082v1) | 2026-05-29T08:00:00+08:00 | AGENT-PLATFORM；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md)；已落实 |
| [The Chain Holds, the Answer Folds: Trace-Answer Dissociation in Reasoning Models Under Adversarial Pressure](https://arxiv.org/html/2605.29087v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/html/2605.29107v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ReasonBreak: Probing Vulnerabilities in Reasoning-Enabled Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/html/2605.29114v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [unix-ctf: Procedural Environments for Unix-Competence Reinforcement Learning](https://arxiv.org/html/2605.29115v1) | 2026-05-29T08:00:00+08:00 | TRAIN-GRPO；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md) |
| [PRO-CUA: Process-Reward Optimization for Computer Use Agents](https://arxiv.org/html/2605.29119v1) | 2026-05-29T08:00:00+08:00 | TRAIN-GRPO；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md) |
| [A Minimal Bifurcation Model of Load Imbalance in a Softmax Mixture-of-Experts Router](https://arxiv.org/html/2605.29121v1) | 2026-05-29T08:00:00+08:00 | MODEL-MOE；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MODEL-MOE，[目标章](../../../../books/part-02-model/21-moe.md) |
| [The Confidence Shortcut: A Reasoning Failure Mode of Masked Diffusion Models](https://arxiv.org/html/2605.29123v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-GENERATIVE-PARADIGMS；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[目标章](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Governing Technical Debt in Agentic AI Systems](https://arxiv.org/html/2605.29129v1) | 2026-05-29T08:00:00+08:00 | AGENT-PLATFORM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md) |
| [Rotary GPU: Exploring Local Execution Paths for Large Mixture-of-Experts Models Under Limited GPU Memory](https://arxiv.org/html/2605.29135v1) | 2026-05-29T08:00:00+08:00 | INFER-GPU-MEMORY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[目标章](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Anytime-Valid Federated Conformal RAG for LLM Swarms](https://arxiv.org/html/2605.29139v1) | 2026-05-29T08:00:00+08:00 | AGENT-RAG；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-RAG，[目标章](../../../../books/part-07-agent/76-rag.md) |
| [RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training in Non-verifiable Domains](https://arxiv.org/html/2605.29156v1) | 2026-05-29T08:00:00+08:00 | TRAIN-RLHF；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-RLHF，[目标章](../../../../books/part-04-training-system/31-rlhf.md) |
| [The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems](https://arxiv.org/html/2605.29178v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [TIMEGATE: Sustainable Time-Boxed Promotion Gates for Continual ML Adaptation Under Resource Constraints](https://arxiv.org/html/2605.29183v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-PRODUCTION；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-PRODUCTION，[目标章](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [ReasonOps: Operator Segmentation for LLM Reasoning Traces](https://arxiv.org/html/2605.29192v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-TRACE；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-TRACE，[目标章](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [The WER Trap: Shattering the Illusion of Unified Tokens in Speech Language Models](https://arxiv.org/html/2605.29209v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-REPRESENTATION；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[目标章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Inferring the Size of Large Language Models From Popular Text Memorization](https://arxiv.org/html/2605.29223v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Relevance as a Vulnerability: How Web Retrieval Degrades Safety Alignment in LLM Agents](https://arxiv.org/html/2605.29224v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [BlockBatch: Multi-Scale Consensus Decoding for Efficient Diffusion Language Model Inference](https://arxiv.org/html/2605.29233v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-GENERATIVE-PARADIGMS；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[目标章](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth](https://arxiv.org/html/2605.29234v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Provably Secure Agent Guardrail](https://arxiv.org/html/2605.29251v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [OpenClawBench: Benchmarking Process-side Anomalies in Real-world Agent Execution Trajectories](https://arxiv.org/html/2605.29253v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling](https://arxiv.org/html/2605.29262v1) | 2026-05-29T08:00:00+08:00 | AGENT-WORKFLOW；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md) |
| [When and How Human Curation Backfires: Preference Alignment under Multi-Model Self-Consuming Loop](https://arxiv.org/html/2605.29267v1) | 2026-05-29T08:00:00+08:00 | TRAIN-DPO；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-DPO，[目标章](../../../../books/part-04-training-system/34-dpo.md) |
| [Prompt-Level Reward Specifications for Open-Ended Post-Training](https://arxiv.org/html/2605.29275v1) | 2026-05-29T08:00:00+08:00 | TRAIN-DPO；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-DPO，[目标章](../../../../books/part-04-training-system/34-dpo.md) |
| [PatchBoard: Schema-Grounded State Mutation for Reliable and Auditable LLM Multi-Agent Collaboration](https://arxiv.org/html/2605.29313v1) | 2026-05-29T08:00:00+08:00 | AGENT-MULTI-AGENT；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md) |
| [STAMP: Training Explicit Memory for Mobile GUI Agents in Controllable and Scalable Virtual Environments](https://arxiv.org/html/2605.29324v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)；已落实 |
| [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/html/2605.29341v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md) |
| [Draft-OPD: On-Policy Distillation for Speculative Draft Models](https://arxiv.org/html/2605.29343v1) | 2026-05-29T08:00:00+08:00 | TRAIN-SFT；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-SFT，[目标章](../../../../books/part-04-training-system/29-sft.md) |
| [ConMoE: Expert-Pool Consolidation via Prototype Reassignment for MoE Compression](https://arxiv.org/html/2605.29350v1) | 2026-05-29T08:00:00+08:00 | MODEL-MOE；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：MODEL-MOE，[目标章](../../../../books/part-02-model/21-moe.md) |
| [Does Distributed Training Undermine Compute Governance?](https://arxiv.org/html/2605.29359v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md)；已落实 |
| [MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models](https://arxiv.org/html/2605.29360v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [On the Optimizer Dependence of Neural Scaling Laws](https://arxiv.org/html/2605.29387v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/html/2605.29438v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions](https://arxiv.org/html/2605.29442v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Full-Pipeline Framework for Evaluating Membership Inference Attacks in Machine Learning](https://arxiv.org/html/2605.29454v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Honest Lying: Understanding Memory Confabulation in Reflexive Agents](https://arxiv.org/html/2605.29463v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)；已落实 |
| [FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Retrieval](https://arxiv.org/html/2605.29517v1) | 2026-05-29T08:00:00+08:00 | INFER-TENSORRT-LLM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [KBF: Knowledge Boundary as Fingerprint for Language Model and Black-Box API Auditing](https://arxiv.org/html/2605.29524v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention](https://arxiv.org/html/2605.29548v1) | 2026-05-29T08:00:00+08:00 | TRAIN-DATA；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-DATA，[目标章](../../../../books/part-04-training-system/27-data.md) |
| [ParaTool: Shifting Tool Representations from Context to Parameters](https://arxiv.org/html/2605.29561v1) | 2026-05-29T08:00:00+08:00 | AGENT-TOOL-CALLING；2 + 3 + 3 = 8 | 深入完成 | 整合：AGENT-TOOL-CALLING，[目标章](../../../../books/part-07-agent/78-tool-calling.md)；已落实 |
| [Mitigating State Aliasing in Vision-Language-Action Models via Inverse Dynamics Learning](https://arxiv.org/html/2605.29577v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [World Models in Words: Auditing Physical State-Transition Commitments in Vision-Language Models](https://arxiv.org/html/2605.29585v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-WORLD-MODELS；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[目标章](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Training Deliberative Monitors for Black-Box Scheming Detection](https://arxiv.org/html/2605.29601v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models](https://arxiv.org/html/2605.29605v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Beyond Attack Success Rate: Temporal Logit Observability for LLM Safety Failures](https://arxiv.org/html/2605.29629v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RTP-LLM: High-Performance Alibaba LLM Inference Engine](https://arxiv.org/html/2605.29639v1) | 2026-05-29T08:00:00+08:00 | INFER-TENSORRT-LLM；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [VikingMem: A Memory Base Management System for Stateful LLM-based Applications](https://arxiv.org/html/2605.29640v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md) |
| [AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training](https://arxiv.org/html/2605.29664v1) | 2026-05-29T08:00:00+08:00 | TRAIN-PIPELINE-PARALLEL；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL，[目标章](../../../../books/part-04-training-system/38-pipeline-parallel.md)；已落实 |
| [Scaling Laws for Agent Harnesses via Effective Feedback Compute](https://arxiv.org/html/2605.29682v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding](https://arxiv.org/html/2605.29707v1) | 2026-05-29T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [RASET: Router-Agnostic Safety-Critical Expert Tuning Exposes Localized Safety Enforcement Failures in Mixture-of-Experts LLMs](https://arxiv.org/html/2605.29708v1) | 2026-05-29T08:00:00+08:00 | MODEL-MOE；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MODEL-MOE，[目标章](../../../../books/part-02-model/21-moe.md) |
| [Bastion: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](https://arxiv.org/html/2605.29727v1) | 2026-05-29T08:00:00+08:00 | INFER-SPECULATIVE-DECODING；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[目标章](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [From Roofline to Ruggedness: Decomposing and Smoothing the GEMM Performance Landscape](https://arxiv.org/html/2605.29752v1) | 2026-05-29T08:00:00+08:00 | INFER-TENSORRT-LLM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Croissant Tasks: A Metadata Format for Reproducible Machine Learning Evaluations](https://arxiv.org/html/2605.29786v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已落实 |
| [Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems](https://arxiv.org/html/2605.29790v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HARP: Hadamard-Preconditioned Adaptive Rotation Processor for Extreme LLM Quantization](https://arxiv.org/html/2605.29843v1) | 2026-05-29T08:00:00+08:00 | INFER-TENSORRT-LLM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Moment-KV: Momentum-Based Decode-Time KV Cache Compression for Long Generation](https://arxiv.org/html/2605.29873v1) | 2026-05-29T08:00:00+08:00 | INFER-KV-CACHE；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [LaRA: Layer-wise Representation Analysis for Detecting Data Contamination in RL Post-Training](https://arxiv.org/html/2605.29888v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Uncertainty Quantification for Multimodal Retrieval Augmented Generation](https://arxiv.org/html/2605.29956v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction](https://arxiv.org/html/2605.29960v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-SECURITY；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[目标章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Fingerprinting Inference Systems of Large Language Models](https://arxiv.org/html/2605.29979v1) | 2026-05-29T08:00:00+08:00 | INFER-TENSORRT-LLM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies](https://arxiv.org/html/2605.30011v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Token Inflation: How Dishonest Providers Can Overcharge for Large Language Model Usage](https://arxiv.org/html/2605.30040v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-COST；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-COST，[目标章](../../../../books/part-06-ai-infrastructure/70-cost.md)；已落实 |
| [REPOT: Recoverable Program-of-Thought via Checkpoint Repair](https://arxiv.org/html/2605.30052v1) | 2026-05-29T08:00:00+08:00 | AGENT-WORKFLOW；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md) |
| [A Predictive Law for On-Policy Self-Distillation From World Feedback](https://arxiv.org/html/2605.30070v1) | 2026-05-29T08:00:00+08:00 | TRAIN-GRPO；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[目标章](../../../../books/part-04-training-system/33-grpo.md) |
| [Future Forcing: Future-aware Training-free KV Cache Policy for Autoregressive Video Generation](https://arxiv.org/html/2605.30083v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-WORLD-MODELS；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[目标章](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Conformal Certification of Reasoning Trace Prefixes](https://arxiv.org/html/2605.30085v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison](https://arxiv.org/html/2605.30087v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems](https://arxiv.org/html/2605.30102v1) | 2026-05-29T08:00:00+08:00 | AGENT-PLATFORM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[目标章](../../../../books/part-07-agent/84-agent-platform.md) |
| [SEAL: Can Saturated Benchmarks Be Revived by LLM-as-a-Meta-Judge?](https://arxiv.org/html/2605.30104v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing](https://arxiv.org/html/2605.30117v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?](https://arxiv.org/html/2605.30152v1) | 2026-05-29T08:00:00+08:00 | AGENT-WORKFLOW；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[目标章](../../../../books/part-07-agent/81-workflow.md) |
| [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/html/2605.30159v1) | 2026-05-29T08:00:00+08:00 | AGENT-MEMORY；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md) |
| [Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms](https://arxiv.org/html/2605.30169v1) | 2026-05-29T08:00:00+08:00 | AGENT-MULTI-AGENT；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md) |
| [A Dual-Path Architecture for Scaling Compute and Capacity in LLMs](https://arxiv.org/html/2605.30202v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MarginGate: Sparse Margin-Triggered Verification for Batch-Invariant LLM Inference](https://arxiv.org/html/2605.30218v1) | 2026-05-29T08:00:00+08:00 | INFER-CONTINUOUS-BATCHING；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-CONTINUOUS-BATCHING，[目标章](../../../../books/part-05-inference-system/46-continuous-batching.md)；已落实 |
| [BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/html/2605.30226v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization](https://arxiv.org/html/2605.30227v1) | 2026-05-29T08:00:00+08:00 | AGENT-MULTI-AGENT；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md) |
| [Same Evidence, Different Answers: Canonical-Context On-Policy Distillation for Multi-Turn Language Models](https://arxiv.org/html/2605.30251v1) | 2026-05-29T08:00:00+08:00 | TRAIN-SFT；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-SFT，[目标章](../../../../books/part-04-training-system/29-sft.md) |
| [How LoRA Remembers? A Parametric Memory Law for LLM Finetuning](https://arxiv.org/html/2605.30260v1) | 2026-05-29T08:00:00+08:00 | TRAIN-LORA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-LORA，[目标章](../../../../books/part-04-training-system/30-lora.md) |
| [minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://arxiv.org/html/2605.30263v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-WORLD-MODELS；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[目标章](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；已落实 |
| [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/html/2605.30280v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-EMBODIED-VLA；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[目标章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [MIRA: Mid-training Rubric Anchoring for Source-Aware Data Selection](https://arxiv.org/html/2605.30288v1) | 2026-05-29T08:00:00+08:00 | TRAIN-DATA；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-DATA，[目标章](../../../../books/part-04-training-system/27-data.md) |
| [Self-Trained Verification for Training- and Test-Time Self-Improvement](https://arxiv.org/html/2605.30290v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RAFI -- A Ray/Work Forwarding Infrastructure for Data Parallel Multi-Node/Multi-GPU Computing](https://arxiv.org/html/2605.30294v1) | 2026-05-29T08:00:00+08:00 | TRAIN-PIPELINE-PARALLEL；2 + 3 + 3 = 8 | 深入完成 | 仅报告：实现语境不改变长期知识 |
| [Gram: Assessing sabotage propensities via automated alignment auditing](https://arxiv.org/html/2605.30322v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?](https://arxiv.org/html/2605.30329v1) | 2026-05-29T08:00:00+08:00 | PLATFORM-EVALUATION-SYSTEM；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[目标章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Demystifying Data Organization for Enhanced LLM Training](https://arxiv.org/html/2605.30334v1) | 2026-05-29T08:00:00+08:00 | TRAIN-DATA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-DATA，[目标章](../../../../books/part-04-training-system/27-data.md) |
| [Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents](https://arxiv.org/html/2605.30335v1) | 2026-05-29T08:00:00+08:00 | AGENT-MULTI-AGENT；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MULTI-AGENT，[目标章](../../../../books/part-07-agent/82-multi-agent.md)；已落实 |
| [Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching](https://arxiv.org/html/2605.30337v1) | 2026-05-29T08:00:00+08:00 | TRAIN-SFT；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-SFT，[目标章](../../../../books/part-04-training-system/29-sft.md) |
| [YoCausal: How Far is Video Generation from World Model? A Causality Perspective](https://arxiv.org/html/2605.30346v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-WORLD-MODELS；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[目标章](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [LLMSurgeon: Diagnosing Data Mixture of Large Language Models](https://arxiv.org/html/2605.30348v1) | 2026-05-29T08:00:00+08:00 | TRAIN-DATA；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-DATA，[目标章](../../../../books/part-04-training-system/27-data.md) |
| [VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion](https://arxiv.org/html/2605.30351v1) | 2026-05-29T08:00:00+08:00 | MULTIMODAL-GENERATIVE-PARADIGMS；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[目标章](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Task-Focused Memorization for Multimodal Agents](https://arxiv.org/html/2605.31075v1) | 2026-05-29T00:00:00+08:00 | AGENT-MEMORY；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY，[目标章](../../../../books/part-07-agent/77-memory.md)；已落实 |

| [UNIQUE: Universal Top-k Sparse Attention for Training-free Inference and Sparsity-aware Training](https://arxiv.org/html/2605.27740v1) | 2026-05-28 | 均值页摘要遗漏尖峰→query-scaled dispersion提议稀疏读；softmask另需训练；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor](https://arxiv.org/html/2605.28062v1) | 2026-05-28 | dense排名邻域不等时间轴；重训对照修正temporal收益归因；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [From Pixels to Words -- Towards Native One-Vision Models at Scale](https://arxiv.org/html/2605.28820v1) | 2026-05-28 | 原生多模态显式visual-unit因果接口与THW时间身份；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [PrunePath: Towards Highly Structured Sparse Language Models](https://arxiv.org/html/2605.28283v1) | 2026-05-28 | 累计质量动态选expert与渐进稀疏的有限预算取舍；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Compositional Generalization in Autoregressive Models via Logit Composition](https://arxiv.org/html/2605.28304v1) | 2026-05-28 | 固定独立token-mask条件下组合专家logits的足够条件；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-SAMPLING，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Models That Know How Evaluations Are Designed Score Safer](https://arxiv.org/html/2605.28591v1) | 2026-05-28 | 参数化protocol-trait曝光可改安全分数且无需显式测评自述；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Attentional White Bear Effect in Transformer Language Models](https://arxiv.org/html/2605.28639v1) | 2026-05-28 | 词汇抑制不等敏感概念表征或后续语义信号已消；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Off-Policy Learning to Reason Works Because It Is More Pessimistic Than You Think](https://arxiv.org/html/2605.28150v1) | 2026-05-28 | ratio-free off-policy替代目标的baseline平移与pessimism条件；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Importance of Being Statistically Earnest: A Critical Re-evaluation of GSM-Symbolic](https://arxiv.org/html/2605.28700v1) | 2026-05-28 | 模板聚类与数值人口重审GSM-Symbolic反证；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains](https://arxiv.org/html/2605.28014v1) | 2026-05-28 | 有正确参照的反射quote仅定位可错局部蒸馏起点；2 + 1 + 3 = 6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs](https://arxiv.org/html/2605.28388v1) | 2026-05-28 | 非零组调幅与零方差组换feature evaluator须分责；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation](https://arxiv.org/html/2605.28222v1) | 2026-05-28 | 等参数q/v与全attention的局部结构取舍；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Beyond pass@k: Redundancy-Aware RLVR for Multi-Sample Code Generation](https://arxiv.org/html/2605.28022v1) | 2026-05-28 | 固定多样本预算内LOO集合credit减少代码冗余；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates](https://arxiv.org/html/2605.28440v1) | 2026-05-28 | 两概率坐标与reference-ratio坐标的梯度平衡不能混同；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DPO，[Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents](https://arxiv.org/html/2605.28532v1) | 2026-05-28 | 工具遮蔽的可行性标签需独立验证依赖与替代路径；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies](https://arxiv.org/html/2605.28527v1) | 2026-05-28 | 冻结VLA的value-like读出与online selector归因分开；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Self-Consistency via Marginal Sharpening](https://arxiv.org/html/2605.28142v1) | 2026-05-28 | 答案边缘分布取幂不同于完整trajectory取幂；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-SAMPLING，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Transformers Provably Learn to Internalize Chain-of-Thought](https://arxiv.org/html/2605.28600v1) | 2026-05-28 | 受限parity结构的CoT内部化充分例不等LLM总费下降；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR](https://arxiv.org/html/2605.28295v1) | 2026-05-28 | 首semantic-token均匀无放回分支改变rollout人口；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Abstraction Gap in Vision-Language Causal Reasoning](https://arxiv.org/html/2605.28779v1) | 2026-05-28 | 解释文本与causal-chain输出的差额不能认证内部faithfulness；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/html/2605.28365v1) | 2026-05-28 | partial Lean证据与选择性风险需覆盖及faithfulness资格；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts](https://arxiv.org/html/2605.28042v1) | 2026-05-28 | translation calibration的expert裁剪/恢复有局部容量条件；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Understanding Generalization and Forgetting in In-Context Continual Learning](https://arxiv.org/html/2605.28705v1) | 2026-05-28 | 线性/掩码attention的受限context干扰与遗忘分解；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use](https://arxiv.org/html/2605.27788v1) | 2026-05-28 | 工具raw transient与persistent extraction的critic消费分工；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-PPO，[Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [Thinking as Compression: Your Reasoning Model is Secretly a Context Compressor](https://arxiv.org/html/2605.28713v1) | 2026-05-28 | task/budget条件reasoning trace可作有损上下文压缩；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Multi-Mixer Models: Flexible Sequence Modeling with Shared Representations](https://arxiv.org/html/2605.28769v1) | 2026-05-28 | 序列轴共享KV的双mixer选择仍需两份state持续推进；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Bridging the Detection-to-Abstention Gap in Reasoning Models under Insufficient Information](https://arxiv.org/html/2605.28070v1) | 2026-05-28 | 同回答显式检测与最终拒答的conditional控制缺口；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models](https://arxiv.org/html/2605.28292v1) | 2026-05-28 | 分段VQ functional-token与扩展词表是训练接口而非真实算子；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Skill-Conditioned Gated Self-Distillation for LLM Reasoning](https://arxiv.org/html/2605.28791v1) | 2026-05-28 | 弱PI teacher支持/抑制极性由外部outcome门控；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Agentic Separation Logic Specification Synthesis](https://arxiv.org/html/2605.27531v1) | 2026-05-28 | 逻辑selector与fuzz反例过滤不证明最强语义规范；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Why LLMs Fail at Causal Discovery and How Interventional Agents Escape](https://arxiv.org/html/2605.27567v1) | 2026-05-28 | 挑战observational causal learning的中心kernel/查询收敛主张；3 + 1 + 3 = 7 | 争议 | 暂缓：中心定理/查询条件争议，不进入Books |
| [You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents](https://arxiv.org/html/2605.27586v1) | 2026-05-28 | 少数训练seed经交互影响未更新peers的替代分工；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems](https://arxiv.org/html/2605.27787v1) | 2026-05-28 | 持久导航角色的freshness与pointer工具物化分工；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Revealing Algorithmic Deductive Circuits for Logical Reasoning](https://arxiv.org/html/2605.27824v1) | 2026-05-28 | 配对patch与跨题消融支持局部推理head参与而非完整算法；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [CAREF: Calibration-Aware Regularization for Explanation Faithfulness Without Rationale Supervision](https://arxiv.org/html/2605.27835v1) | 2026-05-28 | 非加性entropy/sparsity目标只改变概率形状不认证faithfulness；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness?](https://arxiv.org/html/2605.27932v1) | 2026-05-28 | 固定恶意query下工具前缀及局部activation影响ASR；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents](https://arxiv.org/html/2605.27955v1) | 2026-05-28 | typed child合同需与父流程原actiontemplate成对呈现；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [VCap: Hypergeometric Rewards for Weak-to-Strong Visual Captioning](https://arxiv.org/html/2605.28023v1) | 2026-05-28 | 参考只提出probe槽，原视觉裁决可推翻参考错误；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers](https://arxiv.org/html/2605.28215v1) | 2026-05-28 | 更复杂解释格式的决策退化与解释质量需分验；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AI, Take the Wheel: What Drives Delegation and Trust in Human-Computer Cooperative Question Answering?](https://arxiv.org/html/2605.28255v1) | 2026-05-28 | 未见proposal前自主授权与见后adoption是两时点；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Entropy-aware Masking for Masked Language Modeling](https://arxiv.org/html/2605.28526v1) | 2026-05-28 | MLM选位producer的full-input entropy与teacherwarmup/selfmask；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Cultural Binding Heads in Language Models](https://arxiv.org/html/2605.28543v1) | 2026-05-28 | identity-item配对与edgeKO支持partial bindinghead作用；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability](https://arxiv.org/html/2605.28602v1) | 2026-05-28 | solver验证SAT/UNSAT最小编辑对需双正确并另验witness；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction](https://arxiv.org/html/2605.28645v1) | 2026-05-28 | GraphRAG回答可泄露跨query累积结构而非仅独立PII；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Interpretability-Guided Layer Selection over Subspace Projection: SAEs as Stethoscopes, Not Scalpels, for Raw Task Vector Model Editing](https://arxiv.org/html/2605.28649v1) | 2026-05-28 | SAE可诊断选层，但weight增量过滤需独立坐标映射；2 + 1 + 3 = 6 | 深入完成 | 整合：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Activation Steering for Synthetic Data Generation: The Role of Diversity in Downstream Safety Detection](https://arxiv.org/html/2605.28664v1) | 2026-05-28 | steering生成成功/coherence/diversity与下游检测utility分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests](https://arxiv.org/html/2605.28734v1) | 2026-05-28 | promptbank新release中provider403改变judge可用人口；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents](https://arxiv.org/html/2605.28775v1) | 2026-05-28 | teacherstate重采rejected，按function/args差异选择DPO损失；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-DPO，[Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [Personal Visual Memory from Explicit and Implicit Evidence](https://arxiv.org/html/2605.28806v1) | 2026-05-28 | 个人视觉证据pending后再解释/结构写入而非立即caption事实化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Realistic honeypot evaluations for scheming propensity](https://deepmind.google/research/publications/253391/) | 2026-05-28 | 真实代码副本机会式honeypot与promptedorganism的测量权限；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) | 2026-05-28 | 后续可信system-entry更新任务控制而保旧prefix；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Kimi Code v0.5.0](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) | 2026-05-28 | scheduled tasks及/auto改变无人值守提问/approval合同；2 + 1 + 2 = 5 | 深入完成 | 仅报告：版本接口事实；未披露历史调度/审批实现，不改变既有长期授权与执行分权 |

## 4. 证据与知识整合

以下 arXiv 审阅只复用 identity、exact-v1 与 adopted proposition 均未变化的既有证据；owner 日期修正不改变机制结论。结构化 Evidence 与当前 Books 投影见 [`evidence-review-v3.json`](../_sources/daily-20260529/evidence-review-v3.json) 和 [`books-comparison-v3.json`](../_sources/daily-20260529/books-comparison-v3.json)。

### [ReclaimNet: Reclaim-Aware Network Protocols for Voluntary GPU Sharing on Campus](https://arxiv.org/html/2605.28872v1)

**问题与机制。** We present ReclaimNet, a network-layer migration protocol suite that treats provider reclaim as a first-class contract rather than a failure case, combining three mechanisms: (i) reclaim-aware checkpoint scheduling that jointly adapts to time-varying departure hazards and contended bandwidth across co-resident jobs; (ii) volatility-aware destination selection integrating topology, survival probability, and notice-window feasibility; and (iii) deadline-aware migration traffic control with edge enforcement and a submillisecond TC BPF kill-switch. owner=`PLATFORM-GPU-SCHEDULER`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§IV measurement; §§V–VI reclaim-aware membership/lease protocol`；Evaluation=`§VII Evaluation and campus deployment measurements`；Limitations/Counterevidence=`§VIII Limitations and Conclusion; voluntary campus-network and failure-domain boundary`。

<!-- claim:SF-2026-ARXIV-2605-28872:start -->ReclaimNet: Reclaim-Aware Network Protocols for Voluntary GPU Sharing on Campus only supports the exact-v1 disclosed method and evaluated workload; it does not establish untested models, hardware, distributions, production tail-SLO, formal safety or cross-domain generality.<!-- claim:SF-2026-ARXIV-2605-28872:end -->

**当前 Books 投影。** `Applied` 到 `PLATFORM-GPU-SCHEDULER` / `books/part-06-ai-infrastructure/63-gpu-scheduler.md`；当前正文唯一 marker 已核验，未产生新写回。

### [Pre-Registering the Detectable Effect: A Paired-MDE Budget for 4-bit Quantization Benchmarks, with a Pilot Audit](https://arxiv.org/html/2605.28873v1)

**问题与机制。** We illustrate the bound on four models and four benchmarks ($k=5$ splits of $n=100$), and add a parallel MMLU prompt-template study to put the bound's quantization-noise scale alongside the prompt-noise scale. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 paired MDE bound; §4 quantization/benchmark/scoring protocol`；Evaluation=`§5 pilot audit and §6 interpretation`；Limitations/Counterevidence=`§9 Limitations; QRI is descriptive, small NF4 pilot and prompt confounding`。

<!-- claim:SF-2026-ARXIV-2605-28873:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-28873:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [LogDx-CI: Benchmarking Log Reduction Tools for LLM Root-Cause Diagnosis](https://arxiv.org/html/2605.28876v1)

问题与 changed constraint：log reduction is an upstream evidence transform whose quality and cost must be measured both single-shot and inside an agent recovery loop。

机制与 ownership：We introduce LogDx-CI, a benchmark that compares 11 context-reduction tools (raw, tail, grep, three RTK modes, two real LLM map-reduce summarizers, three hybrid routers) on 35 real GitHub Actions failure cases, scored by 3 LLM debugger families (Claude Haiku 4.5, Claude Sonnet 4.6, OpenAI gpt-5-mini) plus a Sonnet 4.6 tool-using agent. owner=`AGENT-CONTEXT`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.28876v1 — §3 LogDx-CI corpus and reduction tools (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.28876v1 — §4 single-shot and agent-loop evaluation (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.28876v1 — §5 limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-28876:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-28876:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-CONTEXT` / `books/part-07-agent/75-context.md` 的当前正文，采用命题与 prior comparison 未变。

### [GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human](https://arxiv.org/html/2605.28882v1)

问题与 changed constraint：open-ended evaluation needs versioned human seeds and rubric-case co-evolution so the judge contract changes explicitly as model behavior shifts。

机制与 ownership：Therefore, we propose GrowLoop, a self-evolving conversation evaluation system that continuously adapts as models advance and scenarios shift. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.28882v1 — §3 rubric-case co-evolution (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.28882v1 — §4 experiments (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.28882v1 — §5 limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-28882:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-28882:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Context Distillation as Latent Memory Management](https://arxiv.org/html/2605.28889v1)

问题与 changed constraint：We formulate context distillation as a latent memory management problem.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28889v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28889v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28889v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28889v1 — official HTML sha256=484b7c915791a1d932ca5b0d304ea69886f807144f2b39de985b7a9026b5cc7f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28889:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that our method substantially outperforms baselines with retrieval, while Self-Gating improves robustness by deactivate unnecessary latent memories.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28889:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [Echoes within the Reasoning: Stealthy and Effective Watermarking via Chain of Thought](https://arxiv.org/html/2605.28890v1)

问题与 changed constraint：We propose BiCoT, a watermarking framework that embeds ownership signals into the internal geometry of reasoning traces by aligning high-saliency structural anchors with a private signature subspace while regularizing ordinary control tokens to preserve semantic capacity.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28890v1 — § exact heading: 4 The Proposed Method`；Evaluation=`arXiv:2605.28890v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28890v1 — § exact heading: 5.8 Threat Model Boundary and Limitation: Logprob Enabled Verification`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28890v1 — official HTML sha256=fd2aa444bf003c5dbca9124efc078287ad0ad64b1b099778107fd4dff06c8dbe; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28890:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that BiCoT preserves reasoning fidelity across diverse complex reasoning tasks while achieving robust detection under fine-tuning, quantization, model-level perturbations, and adaptive output-level attacks across in-domain and out-of-distribution settings.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28890:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities](https://arxiv.org/html/2605.28893v1)

问题与 changed constraint：Although some studies have attempted to investigate the impact of LiL vulnerabilities, they have unfortunately failed to clearly distinguish LiL vulnerabilities from conventional ones, leaving the understanding of real-world LiL vulnerabilities an open problem.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28893v1 — § exact heading: 3. Methodology`；Evaluation=`arXiv:2605.28893v1 — § exact heading: 3.2. Benchmark Construction`。

Trade-off / failure / fallback：`arXiv:2605.28893v1 — § exact heading: 4.5. RQ4: Repair Failure Root Causes`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28893v1 — official HTML sha256=0ccec6e5023425d608e1da29b300536ad3391a559b6104605c01c756bba173de; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28893:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experimental results on 20 agent-model configuration demonstrate that LiL vulnerabilities are far more challenging to fix, with an average decrease of 10.8% Pass@1 rate compared to other types of vulnerabilities.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28893:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [Review Arcade: On the Human Alignment and Gameability of LLM Reviews](https://arxiv.org/html/2605.28897v1)

问题与 changed constraint：In this work, we perform empirical experiments on papers from the 2025 ACL Rolling Review (ARR) to evaluate LLM reviews from both the author and the reviewer perspective.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28897v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28897v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28897v1 — § exact heading: 5 Results and Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28897v1 — official HTML sha256=42918fe6e08c174c1b7c008a76802891bf988cc6c027269eecf588031cbe8111; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28897:start -->仅支持 exact-v1 披露机制及实验边界；不把“We find that this "gaming" of LLM reviews can be effective in specific scenarios, leading to a statistically significant increase of overall scores for up to 35\% of papers.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28897:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [AIRGuard: Guarding Agent Actions with Runtime Authority Control](https://arxiv.org/html/2605.28914v1)

问题与 changed constraint：We present AIRGuard, a runtime guard that operationalizes least privilege as action-time authorization.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28914v1 — § exact heading: 2.1 Threat Model`；Evaluation=`arXiv:2605.28914v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28914v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28914v1 — official HTML sha256=d0264220f2ded5ab77e06f15529acb9124ca3dc29ce337b5266947540395fa49; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28914:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code and data are available at https://github.com/Sophie508/AIRGuard.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28914:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md` 的当前正文，采用命题与 prior comparison 未变。

### [When LLM Reward Design Fails: Diagnostic-Driven Refinement for Sparse Structured RL](https://arxiv.org/html/2605.28918v1)

问题与 changed constraint：We study PPO-trained agents using MiniGrid as core evaluation and MuJoCo as boundary stress test.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28918v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28918v1 — § exact heading: 5 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28918v1 — § exact heading: 7 Failure Taxonomy`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28918v1 — official HTML sha256=a085ce1d967c0158fa236d3b634861af1ef381b37448f8e1ccb20c4757bf685b; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28918:start -->仅支持 exact-v1 披露机制及实验边界；不把“Continuous-control results show the boundary: success-based diagnostics can misfire in dense-reward locomotion, and return-trend feedback removes one false-positive mechanism without robust gains.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28918:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md` 的当前正文，采用命题与 prior comparison 未变。

### [Conf-Gen: Conformal Uncertainty Quantification for Generative Models](https://arxiv.org/html/2605.28920v1)

问题与 changed constraint：In this work we introduce conformal generation (Conf-Gen), a general framework adapting CRC to generative tasks while relaxing its theoretical assumptions.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28920v1 — § exact heading: Section 1 Introduction`；Evaluation=`arXiv:2605.28920v1 — § exact heading: Section 6 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28920v1 — § exact heading: Section 7 Conclusion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28920v1 — official HTML sha256=0e5297f8e2a1b9339cab9737e3c87239243a625f9b74bb74f5b340282fcfea97; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28920:start -->仅支持 exact-v1 披露机制及实验边界；不把“We demonstrate the flexibility of Conf-Gen through some novel applications, including obtaining conformal guarantees on: image generators producing non-memorized images, conversational AI systems having asked enough clarifying questions, and the output of AI agents being correct.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28920:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Beyond Recall: Behavioral Specification as an Interpretive Layer for AI Personalization](https://arxiv.org/html/2605.28969v1)

问题与 changed constraint：We introduce representational accuracy to measure how faithfully a system captures a person's interpretation.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28969v1 — § exact heading: 2.2 Memory systems for LLM agents`；Evaluation=`arXiv:2605.28969v1 — § exact heading: 2. Prior Work, Industry Benchmarks, The Fifth Target`。

Trade-off / failure / fallback：`arXiv:2605.28969v1 — § exact heading: 3.3.6 Rubric-handling limitations (post-hoc validity audit)`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28969v1 — official HTML sha256=101b3e17cd8bba2def194b91f2814eea8c6024099488edfc82a5e614fab3a555; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28969:start -->仅支持 exact-v1 披露机制及实验边界；不把“We evaluate the Specification on a prototype benchmark of held-out behavioral predictions scored by a calibrated 5-judge LLM panel.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28969:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [A Secure, Manifest-Based Framework for Delegated Privilege Promotion](https://arxiv.org/html/2605.28991v1)

问题与 changed constraint：We present a secure, manifest-based infrastructure for delegated promotion of privileged software components, deployed in production as part of a large-scale enterprise database system serving both cloud and on-premises installations.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28991v1 — § exact heading: II System Architecture and Design`；Evaluation=`arXiv:2605.28991v1 — § exact heading: IV Security Analysis`。

Trade-off / failure / fallback：`arXiv:2605.28991v1 — § exact heading: II-A Threat Model`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28991v1 — official HTML sha256=38bca95491babf9d404fed1ccf11bc2e90fd9714aaab3e3ec0e9861181a48d41; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28991:start -->仅支持 exact-v1 披露机制及实验边界；不把“The system explicitly mitigates Time-of-Check-to-Time-of-Use (TOCTOU) attacks using file-descriptor-bound validation and promotion, supports offline key rotation and revocation, and enables zero-downtime self-update via atomic replacement.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28991:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md` 的当前正文，采用命题与 prior comparison 未变。

### [Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening](https://arxiv.org/html/2605.28999v1)

问题与 changed constraint：In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28999v1 — § exact heading: 3.1 Threat Model`；Evaluation=`arXiv:2605.28999v1 — § exact heading: 5.5 Method Selection for Large-Scale Analysis`。

Trade-off / failure / fallback：`arXiv:2605.28999v1 — § exact heading: 7 Discussion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28999v1 — official HTML sha256=4c6e94a2e9d6e480605f51128be9c9358f590c91fc80d8e103ef939bb84b73b6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28999:start -->仅支持 exact-v1 披露机制及实验边界；不把“Manual validation on a small-scale dataset demonstrates that our detectors achieve high precision and outperform state-of-the-art general-purpose detectors.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28999:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [FormInv: A Measurement Protocol for Semantic Invariance in Mathematical Reasoning Benchmarks](https://arxiv.org/html/2605.29001v1)

问题与 changed constraint：A paraphrase-quality audit of MathCheck (ICLR 2025) detected 4 semantically incorrect paraphrases in 129 groups (3.1%); removing them drops GPT-4o from rank 2 to rank 4 and elevates Claude Haiku and DeepSeek V3 above it; these ranking changes are invisible to any single-model evaluation.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29001v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29001v1 — § exact heading: 4 FormInv Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.29001v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29001v1 — official HTML sha256=d0e7ab93baa2dac7887cdb236f80c5996169d4fed3f8e888dd5fe36d3c7ac6c1; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29001:start -->仅支持 exact-v1 披露机制及实验边界；不把“FormInv supplies the audit protocol (replicated on external benchmarks at 100% recall), SCR and per-theorem Cochran's Q as primary invariance measures evaluated on 9 models across 366-811 items (on Lean4-verified theorems), and FormInvSelector for regime-aware model selection.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29001:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [LoRe: Adaptive Interaction-Evaluation Routing with Per-Step Interaction Budgets for Iterative Graph Solvers](https://arxiv.org/html/2605.29005v1)

问题与 changed constraint：Diffusion-based neural solvers for combinatorial optimization repeatedly re-evaluate dense edge/factor interactions, making inference expensive in wall-clock time and often memory-bound at scale.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29005v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29005v1 — § exact heading: 3.1 Formulation: Iterative Refinement as Operator Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.29005v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29005v1 — official HTML sha256=559be4e8e9ca49a19ad2512c93ccd1b2a3d8402c89267afee289a4eeaff9db6d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29005:start -->仅支持 exact-v1 披露机制及实验边界；不把“Diffusion-based neural solvers for combinatorial optimization repeatedly re-evaluate dense edge/factor interactions, making inference expensive in wall-clock time and often memory-bound at scale.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29005:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Converted, Not Equivalent: Benchmarking Codebase Conversion via Observational Equivalence](https://arxiv.org/html/2605.29054v1)

问题与 changed constraint：We introduce T2J-Bench, a benchmark for codebase conversion that reformulates conversion as transfer under a fixed equivalence contract.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29054v1 — § exact heading: 5.3 Self-Validation Systematically Overstates Progress`；Evaluation=`arXiv:2605.29054v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29054v1 — § exact heading: 5.1 A Cross-Agent Failure Taxonomy`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29054v1 — official HTML sha256=f83a8a863b6eb67137c3c9aafb5efbf2773bf40a0fdb22358ff2e0fbf8945566; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29054:start -->仅支持 exact-v1 披露机制及实验边界；不把“This suggests that failures stem more from contract-misaligned self-validation than from limited budget or backbone strength.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29054:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Robust and Efficient Guardrails with Latent Reasoning](https://arxiv.org/html/2605.29068v1)

问题与 changed constraint：To address this challenge, we propose COLAGUARD, a guardrail model that transfers multi-step safety reasoning into a continuous latent space through a stage-wise training curriculum, enabling direct hidden-state propagation at inference.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29068v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29068v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29068v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29068v1 — official HTML sha256=aa57cbc30dac5822270c591d7ab737c1481861b157bec9e3849280b77ddb6943; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29068:start -->仅支持 exact-v1 披露机制及实验边界；不把“Reasoning-based guardrails significantly outperform classification-only baselines, but they incur substantial query latency and token overhead that make them impractical for highthroughput deployment.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29068:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [Embodied3DBench: Benchmarking Low-Level Embodied Spatial Intelligence of Vision Language Models](https://arxiv.org/html/2605.29074v1)

问题与 changed constraint：We introduce Embodied3DBench, a robot-centric benchmark targeting low-level spatial intelligence in embodied 3D environments.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29074v1 — § exact heading: 1. Introduction`；Evaluation=`arXiv:2605.29074v1 — § exact heading: 3.3. Benchmark Construction`。

Trade-off / failure / fallback：`arXiv:2605.29074v1 — § exact heading: 5. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29074v1 — official HTML sha256=159ce42649abf09570b373306b1b776ec886382edbc1e4f6ed98b4e64438ba8f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29074:start -->仅支持 exact-v1 披露机制及实验边界；不把“We evaluate 13 state-of-the-art models, and the results show that while current models exhibit relatively strong high-level spatial reasoning, such as understanding object-to-object positional relations, they remain fragile in interaction-oriented perception, highlighting a significant lack of robust 3D-aware interaction priors.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29074:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [Knowledge Offloading: Decomposing LLMs into Sparse Backbones and Memory Modules](https://arxiv.org/html/2605.29075v1)

问题与 changed constraint：We propose \emph{knowledge offloading} (KOFF), a framework for decomposing a pretrained LLM into a sparse shared backbone and domain-specific memories.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29075v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.29075v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29075v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29075v1 — official HTML sha256=cc51fcaee66f9e9767fe6ae83f3d8c792c4420ad4f471a094ffd75a6ec6cf8fa; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29075:start -->仅支持 exact-v1 披露机制及实验边界；不把“Ablations show that LoRA and learned KV memories are complementary, and specialization analyses suggest that the learned decomposition is meaningful: language-specific neurons are preferentially removed while language-general neurons largely remain in the backbone.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29075:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [Bridging the Sim-to-Real Gap in Reinforcement Learning-Based Industrial Dispatching through Execution Semantics](https://arxiv.org/html/2605.29078v1)

问题与 changed constraint：The results show analytical benefits across all observation lag regimes, as undifferentiated execution failures are transformed into structured, typed outcomes with full attribution coverage.

Mechanism 与 ownership：owner=`AGENT-WORKFLOW`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29078v1 — §III execution requirements; §IV snapshot isolation, policy-neutral contract and divergence record`；Evaluation=`arXiv:2605.29078v1 — §V empirical evaluation across lag regimes`。

Trade-off / failure / fallback：`arXiv:2605.29078v1 — §IV-D implementation constraints; §VI future-work boundary`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29078v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29078:start -->仅支持 exact-v1 披露机制及实验边界；不把“The results show analytical benefits across all observation lag regimes, as undifferentiated execution failures are transformed into structured, typed outcomes with full attribution coverage.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29078:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md` 的当前正文，采用命题与 prior comparison 未变。

### [The Importance of Out-of-Band Metadata for Safe Autonomous Agents: The Redpanda Agentic Data Plane](https://arxiv.org/html/2605.29082v1)

问题与 changed constraint：We present the Redpanda Agentic Data Plane (ADP), an architecture built around out-of-band metadata channels: infrastructure pathways that carry security context, policy signals, and audit trails deterministically, entirely outside the agent's read and write path and across heterogeneous infrastructure.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29082v1 — § exact heading: 4. System: The Agentic Data Plane`；Evaluation=`arXiv:2605.29082v1 — § exact heading: 1. Introduction`。

Trade-off / failure / fallback：`arXiv:2605.29082v1 — § exact heading: 7. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29082v1 — official HTML sha256=081c38dee7db84a2bf1efd9e8d9c06a15d35b76a905537a9e2fb49b3745d6d87; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29082:start -->仅支持 exact-v1 披露机制及实验边界；不把“We demonstrate ADP with a multi-agent portfolio rebalancing system in which autonomous agents monitor markets, make trade decisions, and execute orders across isolated client accounts -- with per-client data scoping, trade approval thresholds, and tamper-proof audit trails all enforced by out-of-band channels the agents can neither see nor bypass.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29082:end -->

**当前 Books 投影。** `Applied` 到 `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md`；当前正文唯一 marker 已核验，未产生新写回。

### [The Chain Holds, the Answer Folds: Trace-Answer Dissociation in Reasoning Models Under Adversarial Pressure](https://arxiv.org/html/2605.29087v1)

问题与 changed constraint：Reasoning models are evaluated on single-turn benchmarks but deployed in multi-turn dialogue, where users push back on correct answers.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29087v1 — § exact heading: 3 The Latent-versus-Behavioral Framework`；Evaluation=`arXiv:2605.29087v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.29087v1 — § exact heading: 10 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29087v1 — official HTML sha256=86ee2f058f79289bfbe5520d1df0b0a7e4e647c112d9eb14f7909d3e814255f9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29087:start -->仅支持 exact-v1 披露机制及实验边界；不把“Under sustained adversarial pressure we find a previously undocumented failure mode: the chain-of-thought stays factually correct from first turn to last while the emitted answer flips wrong.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29087:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization](https://arxiv.org/html/2605.29107v1)

问题与 changed constraint：We present GEO-Bench, a benchmark that evaluates GEO ranking-manipulation attacks under one protocol.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29107v1 — § exact heading: 3 GEO-Bench: Benchmark Design`；Evaluation=`arXiv:2605.29107v1 — § exact heading: 3.3 Evaluation Metrics`。

Trade-off / failure / fallback：`arXiv:2605.29107v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29107v1 — official HTML sha256=d6201036e694c5ae9088a4681e2fb3c28bba0aec07bcf0292995a841ff377130; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29107:start -->仅支持 exact-v1 披露机制及实验边界；不把“By standardizing datasets, attack implementations, and metrics, GEO-Bench enables the first direct comparison across these attack paradigms and supports the development of detection methods.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29107:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [ReasonBreak: Probing Vulnerabilities in Reasoning-Enabled Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/html/2605.29114v1)

问题与 changed constraint：We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, leading to increased collision rates and degraded safety metrics.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29114v1 — § exact heading: 3 Threat Model`；Evaluation=`arXiv:2605.29114v1 — § exact heading: 5 Evaluation Protocol and Success Criteria`。

Trade-off / failure / fallback：`arXiv:2605.29114v1 — § exact heading: 8 Discussion and Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29114v1 — official HTML sha256=5847a96dc6b379895ef66c5cde52b6481cec3e2864b1e460feee0735fb6a8ac8; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29114:start -->仅支持 exact-v1 披露机制及实验边界；不把“We show that these models are highly vulnerable to realistic input perturbations, achieving up to 89% attack success rate (ASR) on reasoning and up to 72% on trajectory manipulation in closed-loop simulation, leading to increased collision rates and degraded safety metrics.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29114:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [unix-ctf: Procedural Environments for Unix-Competence Reinforcement Learning](https://arxiv.org/html/2605.29115v1)

问题与 changed constraint：We make the distinction operational and build a training surface for the Unix component.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29115v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29115v1 — § exact heading: 5 Evaluation protocol`。

Trade-off / failure / fallback：`arXiv:2605.29115v1 — § exact heading: 7 Conclusion and limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29115v1 — official HTML sha256=61533d9472b107db9809f1be716cd7739d680592f79ad97fdeba6e052ccc4d81; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29115:start -->仅支持 exact-v1 披露机制及实验边界；不把“Tasks are produced by an LLM-assisted synthesis pipeline that generates candidate hiding techniques, rewrites them into parameterized hide-and-find script pairs, and filters them with a bidirectional contract: the hide script must leave no plaintext trace of the flag on disk, and the find script must recover the flag in a fresh directory.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29115:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md` 的当前正文，采用命题与 prior comparison 未变。

### [PRO-CUA: Process-Reward Optimization for Computer Use Agents](https://arxiv.org/html/2605.29119v1)

问题与 changed constraint：In this work, we propose PRO-CUA, a process-reward optimization framework for training CUAs with iterative step-level reinforcement learning.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29119v1 — § exact heading: 3.3 Process Reward Model Grading`；Evaluation=`arXiv:2605.29119v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29119v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29119v1 — official HTML sha256=cc5c35fe725e92575fa9815caf18800be44be6f9e67621c5918dc55aacf8a0c9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29119:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on live web benchmarks demonstrate the effectiveness of PRO-CUA and the reliability of PRM-guided step-level training.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29119:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md` 的当前正文，采用命题与 prior comparison 未变。

### [A Minimal Bifurcation Model of Load Imbalance in a Softmax Mixture-of-Experts Router](https://arxiv.org/html/2605.29121v1)

问题与 changed constraint：We propose a minimal dynamical model of adaptive softmax routing for a two-expert Mixture-of-Experts (MoE) layer.

Mechanism 与 ownership：owner=`MODEL-MOE`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29121v1 — § exact heading: 3.1 Two-Expert Model`；Evaluation=`arXiv:2605.29121v1 — § exact heading: 8 Numerical Experiments with Batch Routing`。

Trade-off / failure / fallback：`arXiv:2605.29121v1 — § exact heading: 9 Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29121v1 — official HTML sha256=ab3f9a8273c3d33151de33c82a689df6b669452299c69ed0cc1d123e1a06babe; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29121:start -->仅支持 exact-v1 披露机制及实验边界；不把“The results provide a controlled low-dimensional mechanism for abrupt transitions to load imbalance in adaptive MoE routers.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29121:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MODEL-MOE` / `books/part-02-model/21-moe.md` 的当前正文，采用命题与 prior comparison 未变。

### [The Confidence Shortcut: A Reasoning Failure Mode of Masked Diffusion Models](https://arxiv.org/html/2605.29123v1)

问题与 changed constraint：Masked diffusion language models (MDMs) uniquely support any-order generation, with confidence-based decoding currently serving as the de facto standard inference policy.

Mechanism 与 ownership：owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29123v1 — § exact heading: 2.1 Masked Diffusion Models`；Evaluation=`arXiv:2605.29123v1 — § exact heading: 4 Experiments on Other Reasoning Tasks`。

Trade-off / failure / fallback：`arXiv:2605.29123v1 — § exact heading: 3.5 Discussion: What addition teaches us`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29123v1 — official HTML sha256=e64903394774e58c756155d421de40b4a449290a81bcdd015cfa13c276a88c3f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29123:start -->仅支持 exact-v1 披露机制及实验边界；不把“In contrast, random masking -- despite its perceived inefficiency -- robustly preserves the reasoning-trajectory conditionals essential for solving the challenging tail.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29123:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的当前正文，采用命题与 prior comparison 未变。

### [Governing Technical Debt in Agentic AI Systems](https://arxiv.org/html/2605.29129v1)

问题与 changed constraint：The distinction matters: debt is a stock of design and governance liability, while the tax is a flow of operating cost that arises because stochastic agents act through tools and workflows.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29129v1 — §2 debt/tax model; §3 debt accumulation`；Evaluation=`arXiv:2605.29129v1 — §4 operationalizing governance`。

Trade-off / failure / fallback：`arXiv:2605.29129v1 — §5 Conclusion; position paper without empirical validation or dedicated limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29129v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29129:start -->仅支持 exact-v1 披露机制及实验边界；不把“We outline how managers can make both visible through lightweight dashboards and governance controls.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29129:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md` 的当前正文，采用命题与 prior comparison 未变。

### [Rotary GPU: Exploring Local Execution Paths for Large Mixture-of-Experts Models Under Limited GPU Memory](https://arxiv.org/html/2605.29135v1)

问题与 changed constraint：Large language models have achieved remarkable capabilities through scaling, and this paper does not challenge that.

Mechanism 与 ownership：owner=`INFER-GPU-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29135v1 — §4 Rotary GPU concept; §6 setup`；Evaluation=`arXiv:2605.29135v1 — §8 results and failure analysis`。

Trade-off / failure / fallback：`arXiv:2605.29135v1 — §11 Limitations: one platform, ten-prompt smoke set and undisclosed implementation`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29135v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29135:start -->仅支持 exact-v1 披露机制及实验边界；不把“The results should be read as exploratory rather than definitive, but they suggest deployment accessibility deserves continued investigation as these models evolve.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29135:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-GPU-MEMORY` / `books/part-05-inference-system/54-gpu-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [Anytime-Valid Federated Conformal RAG for LLM Swarms](https://arxiv.org/html/2605.29139v1)

问题与 changed constraint：Federated Conformal RAG (FC-RAG) provides distribution-free coverage for a bandwidth-limited swarm of weak language models, but only at a fixed horizon.

Mechanism 与 ownership：owner=`AGENT-RAG`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29139v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.29139v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29139v1 — § exact heading: 6 Discussion and outlook`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29139v1 — official HTML sha256=a8ec74cd405ca490d4b9ef8c2163fa06058832b58674ce3390d164cb1abab1e3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29139:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on a GPT-2-small + MiniLM swarm across MMLU, DBpedia, and AG News verify the predicted alarm rate, detection delay, envelope coverage, and $14$-$57\%$ bandwidth savings; the alarm fires when and only when coverage genuinely breaks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29139:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-RAG` / `books/part-07-agent/76-rag.md` 的当前正文，采用命题与 prior comparison 未变。

### [RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training in Non-verifiable Domains](https://arxiv.org/html/2605.29156v1)

问题与 changed constraint：We present RUBRIC-ARROW, an alternating framework that jointly trains a rubric generator and a rubric-conditioned judge, with its RL stage using only pairwise preference data.

Mechanism 与 ownership：owner=`TRAIN-RLHF`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29156v1 — § exact heading: 4 Method`；Evaluation=`arXiv:2605.29156v1 — § exact heading: 5 Theoretical Analysis`。

Trade-off / failure / fallback：`arXiv:2605.29156v1 — § exact heading: 7 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29156v1 — official HTML sha256=0276e263a7af8bd4b456d156d09b1c86044e9c77ddc9ab84a6ae06a066509473; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29156:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that RUBRIC-ARROW achieves competitive reward-modeling accuracy and yields consistent gains for downstream policy post-training.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29156:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-RLHF` / `books/part-04-training-system/31-rlhf.md` 的当前正文，采用命题与 prior comparison 未变。

### [The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems](https://arxiv.org/html/2605.29178v1)

问题与 changed constraint：We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29178v1 — § exact heading: 3.1 Coordinated sabotage is already practical for frontier models`；Evaluation=`arXiv:2605.29178v1 — § exact heading: 3 Results`。

Trade-off / failure / fallback：`arXiv:2605.29178v1 — § exact heading: 3.3 Recovery, not failure incidence, drives the model gap`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29178v1 — official HTML sha256=c64659adcde64aa6748ea9f8a3eee8358c0782dcf23a8c50fc40826a7df132e9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29178:start -->仅支持 exact-v1 披露机制及实验边界；不把“Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29178:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [TIMEGATE: Sustainable Time-Boxed Promotion Gates for Continual ML Adaptation Under Resource Constraints](https://arxiv.org/html/2605.29183v1)

问题与 changed constraint：We introduce TIMEGATE, a policy layer managing adaptation by budgeting time, labeling, training, and evaluation.

Mechanism 与 ownership：owner=`PLATFORM-PRODUCTION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29183v1 — § exact heading: 2 The TimeGate Model`；Evaluation=`arXiv:2605.29183v1 — § exact heading: 3 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.29183v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29183v1 — official HTML sha256=a3923b577e9eb61591e3fc195930456c0d3c5d06bdf8deaa0945c9384d3c4a94; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29183:start -->仅支持 exact-v1 披露机制及实验边界；不把“We validate: (i) labeling outperforms training by 2.3x on Adult tabular; (ii) it transfers to LLaMA-3.1-8B + QLoRA on SST-2 (accuracy 0.80 to 0.96; M =1 in 35/36 runs); (iii) M is informative, 28-cell sensitivity shows M drops to 0.81 at tight thresholds; (iv) 100-cycle simulation achieves 66% evaluation-compute savings with no silent mis-promotions; (v) 10%-slice evaluation on LLaMA uses 89% less wall-clock and ener”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29183:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-PRODUCTION` / `books/part-06-ai-infrastructure/73-production-best-practice.md` 的当前正文，采用命题与 prior comparison 未变。

### [ReasonOps: Operator Segmentation for LLM Reasoning Traces](https://arxiv.org/html/2605.29192v1)

问题与 changed constraint：To remedy this, we develop ReasonOps, an unsupervised, expressive method for annotating chain-of-thought traces, providing succinct universal operators.

Mechanism 与 ownership：owner=`PLATFORM-TRACE`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29192v1 — § exact heading: 3 Methods`；Evaluation=`arXiv:2605.29192v1 — § exact heading: 5 Analysis of operator distributions`。

Trade-off / failure / fallback：`arXiv:2605.29192v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29192v1 — official HTML sha256=e420a9f8f6e5d0391e17194107e7b985ed8142555896991b2d2ec2b1ca2d68c9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29192:start -->仅支持 exact-v1 披露机制及实验边界；不把“The ReasonOps pipeline is unsupervised and annotation-free, enabling deep insights into LLM reasoning traces as well as strong downstream results on model identification and correctness prediction.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29192:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-TRACE` / `books/part-06-ai-infrastructure/69-trace.md` 的当前正文，采用命题与 prior comparison 未变。

### [The WER Trap: Shattering the Illusion of Unified Tokens in Speech Language Models](https://arxiv.org/html/2605.29209v1)

问题与 changed constraint：To overcome this, we develop a dynamic compression tokenizer that intelligently aligns representations with semantic boundaries, achieving ultra-low frame rates with exceptionally low WER.

Mechanism 与 ownership：owner=`MULTIMODAL-REPRESENTATION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.29209v1 — § exact heading: 3 The Methodological Bottleneck: Fixed-Stride Compression`；Evaluation=`arXiv:2605.29209v1 — § exact heading: 5 Evaluation Framework: The Dual-Probing Protocol`。

Trade-off / failure / fallback：`arXiv:2605.29209v1 — § exact heading: 7 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.29209v1 — official HTML sha256=c85bde6618b205f1951294db9ece991e3cd1320c1319aaf4196c9000944fe070; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-29209:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our findings demonstrate that semantic categorization rewarded by low WER is inherently orthogonal to the continuous phonetic trajectories required for synthesis, shattering the illusion of the unified token and advocating for explicitly decoupled speech representations.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-29209:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-REPRESENTATION` / `books/part-03-multimodal-world-models/23-multimodal-representation.md` 的当前正文，采用命题与 prior comparison 未变。

### [Inferring the Size of Large Language Models From Popular Text Memorization](https://arxiv.org/html/2605.29223v1)

问题与机制：We propose a black-box method to infer conservative lower bounds on LLM size from generated text outputs alone, requiring nothing beyond the ability to submit text fragments and observe next-token predictions. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：When applied to popular closed-weight models, our framework recovers internal product hierarchies and reveals a clear divergence in industry scaling strategies: while some developers yield significantly higher bounds indicative of large generational parameter growth, others operate under strict parameter ceilings, demonstrating that hidden design choices can be systematically probed even under strict API limitations.。Method=`arXiv:2605.29223v1 HTML — §III Approach; excerpt=ry reference point for interpreting capabilities and costs—largely undisclosed. We propose a black-box method to infer conservative lower bounds on LLM size from generated text outputs alone, requiring nothing beyond the ability to submit text fragments and observe next-token predictions. Our approach is grounded in a key observation: popular, widely-circulated texts—such as classical literature, religious texts, and`；Evaluation=`arXiv:2605.29223v1 HTML — §IV Evaluation; excerpt=e Size Inference III-D Relative Size Inference III-E Scope and Applicability IV Evaluation IV-A Framework IV-B Open-Weight Dense Models IV-B 1 Absolute Size Inference IV-B 2 Relative Size Inference IV-C Open-Weight Mixture-of-Experts Models IV-D Closed-Weight Models V Related Work VI Conclusions References A Texts and Prompts B Correctness of Assumption 1 License: CC BY 4.0 arXiv:2605.29223v1 [cs.LG] 28 May 2026 Infe`。

Trade-off / failure / fallback：`arXiv:2605.29223v1 HTML — §VI Conclusions; excerpt=g that hidden design choices can be systematically probed even under strict API limitations. I Introduction Large language models (LLMs) have become deeply integrated into many applications and services. The development of the most advanced systems is heavily driven by major tech companies such as OpenAI, Google, Meta, and Anthropic. The most widely used are general-purpose models, which are trained on vast amounts o`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29223:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29223:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Relevance as a Vulnerability: How Web Retrieval Degrades Safety Alignment in LLM Agents](https://arxiv.org/html/2605.29224v1)

问题与机制：We introduce AgentREVEAL, a diagnostic framework for analyzing retrieval-induced safety degradation in LLM agents. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Along the integration axis, we find that binding tool invocation and response generation in a single step amplifies harmful outputs.。Method=`arXiv:2605.29224v1 HTML — §3 Methodology; excerpt=t 1 Introduction 2 Related Work Retrieval Safety. Agentic Tool Use. Defenses. 3 Methodology 3.1 Definitions 3.2 Problem Setup 3.3 Dataset Construction: LLM-Driven Adversarial Discovery Pipeline Query Generator ( M g ​ e ​ n M_{gen} ). Search Aggregator. Content Evaluator ( M e ​ v ​ a ​ l M_{eval} ). 3.4 Experimental Setup Agent Architecture and Tool-Calling Mechanism. 3.5 Evaluation Framework 4 Results 4.1 Axis 1: D`；Evaluation=`arXiv:2605.29224v1 HTML — §3.4 Experimental Setup; excerpt={gen} ). Search Aggregator. Content Evaluator ( M e ​ v ​ a ​ l M_{eval} ). 3.4 Experimental Setup Agent Architecture and Tool-Calling Mechanism. 3.5 Evaluation Framework 4 Results 4.1 Axis 1: Does the delivery mechanism amplify harm? 4.2 Axis 2A: Does retrieved content affect the model vulnerability? 4.3 Axis 2B: How does topical relevance affect the vulnerability? 4.4 Are these vulnerabilities limited to the extern`。

Trade-off / failure / fallback：`arXiv:2605.29224v1 HTML — §5 Conclusion; excerpt=e vulnerabilities limited to the externally specified URL setup? 5 Conclusion 6 Limitations 7 Ethics Statement References A Evaluation Protocol and Dataset Construction A.1 Dataset Labeling and Query-Generation Prompts A.2 Human Validation of Dataset Labels A.3 Harmfulness Rubric and Judge Calibration A.4 Dataset Coverage Statistics B Scope and Release Details B.1 Threat Model and Scope B.2 HarmURLBench Release Plan`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29224:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29224:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [BlockBatch: Multi-Scale Consensus Decoding for Efficient Diffusion Language Model Inference](https://arxiv.org/html/2605.29233v1)

问题与机制：We show that block size itself is a useful branching dimension. owner=`MULTIMODAL-GENERATIVE-PARADIGMS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We show that block size itself is a useful branching dimension.。Method=`arXiv:2605.29233v1 HTML — §4 Method; excerpt=.3 Token-Level Characterization: Bifurcation Tokens and Later-Stage Consensus 4 Method 4.1 Exploiting Bifurcation Confidence-Gated Merge Leader-Based Sync 4.2 System-Level Optimization BlockBatch Denoise Optimization. 5 Experiments 5.1 Setup 5.2 Main Results 5.3 Ablation Studies Synchronization Threshold. Refresh Interval. Block-Size Configuration. 6 Conclusion 7 Limitations References A Appendix: Ablation Tables B A`；Evaluation=`arXiv:2605.29233v1 HTML — §5 Experiments; excerpt=der-Based Sync 4.2 System-Level Optimization BlockBatch Denoise Optimization. 5 Experiments 5.1 Setup 5.2 Main Results 5.3 Ablation Studies Synchronization Threshold. Refresh Interval. Block-Size Configuration. 6 Conclusion 7 Limitations References A Appendix: Ablation Tables B Appendix: Token-Level Characterization B.1 Later-Stage Consensus and Bifurcation Tokens B.2 Token Bifurcation Case studies GSM8K sample 1. GS`。

Trade-off / failure / fallback：`arXiv:2605.29233v1 HTML — §6 Conclusion; excerpt=onization Threshold. Refresh Interval. Block-Size Configuration. 6 Conclusion 7 Limitations References A Appendix: Ablation Tables B Appendix: Token-Level Characterization B.1 Later-Stage Consensus and Bifurcation Tokens B.2 Token Bifurcation Case studies GSM8K sample 1. GSM8K sample 2. GSM8K sample 3. Takeaway. C Appendix: KV Cache Vector Space Formulation C.1 Basic Operations C.2 Proposition 1: Expected Block-Local`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29233:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29233:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的当前正文，采用命题与 prior comparison 未变。

### [Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth](https://arxiv.org/html/2605.29234v1)

问题与机制：We study large-scale literature search from two complementary angles: improving the retrieval pipeline, and stress-testing the human reference list as an evaluation target. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We study large-scale literature search from two complementary angles: improving the retrieval pipeline, and stress-testing the human reference list as an evaluation target.。Method=`arXiv:2605.29234v1 HTML — §Appendix B System Details; excerpt=v-API baseline and reaches 51.9% recall at K = 1000 K{=}1000 . Precision Recall Method @20 @100 @1k @20 @100 @1k No Rerank (no DR) 0.1 0.1 0.0 0.0 0.3 1.9 PaSa 5.3 4.5 1.5 1.3 7.4 27.8 ScholarQA 5.7 4.0 1.2 7.7 13.5 31.0 Debate 9.6 4.5 1.5 5.1 12.2 39.9 Debate + + Qwen3 14.7 6.6 1.7 8.1 18.1 46.2 Qwen3 emb. 16.8 8.0 1.9 9.6 22.2 51.9 Table 1: Precision and recall at K ∈ { 20,100 , 1 , 000 } K\in\{20,100,1{,}000\} . B`；Evaluation=`arXiv:2605.29234v1 HTML — §Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth; excerpt=Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction Contributions. 2 Deep Research Pipe`。

Trade-off / failure / fallback：`arXiv:2605.29234v1 HTML — §6 Discussion and Conclusion; excerpt=val Results Diversity and ranking quality. 5 Human References = Ground Truth? 6 Discussion and Conclusion References A Background and Related Work Scholarly APIs and index-based retrieval. Dense retrievers and re-rankers. LLM-based retrieval agents. Evaluating LLM literature search. B System Details B.1 Phase 1: Retrieval with LLM-Constructed Queries B.2 Phase 2: Citation Graph Expansion B.3 Re-ranking Modules B.4 En`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29234:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29234:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Provably Secure Agent Guardrail](https://arxiv.org/html/2605.29251v1)

问题与机制：Based on this paradigm, we further introduce an executable Proof-Constrained Action (ePCA) framework with a neural symbolic isolation architecture. owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Empirical evaluations of macroscopic and microscopic two-dimensional dynamic adversarial systems demonstrate that our formal verification mechanism achieves zero attack success rate and zero false positive rate across the evaluated scenarios, with extremely low computational latency.。Method=`arXiv:2605.29251v1 HTML — §3.1. Formal Problem Formulation; excerpt=lem Formulation 3.2 Threat Model 4 From Empirical to Provable Security 4.1 ePCA Architecture Overview 4.2 Formalizing the Operational Semantics 4.3 Axioms of Safe Behavior 4.4 Semantic Translation 5 System Design 5.1 Semantic Stripping 5.2 Verification Plane 5.3 Axiomatic Settings 5.4 Deadlock Instantiation 5.5 Security Proof of Our System 6 Experiment 6.1 Experimental Philosophy 6.2 Experimental Setting Models and B`；Evaluation=`arXiv:2605.29251v1 HTML — §6. Experiment; excerpt=xiomatic Settings 5.4 Deadlock Instantiation 5.5 Security Proof of Our System 6 Experiment 6.1 Experimental Philosophy 6.2 Experimental Setting Models and Baselines. Evaluation Environments. 6.3 Controlled Multi-Step Financial Transfer 6.3.1 Observed Behavior 6.3.2 Analysis of Aggregated Results 6.3.3 Proof of the Case 6.4 Enterprise Sandbox Data Exfiltration 6.4.1 Attack Trajectory 6.4.2 Proof of the Case 7 Related`。

Trade-off / failure / fallback：`arXiv:2605.29251v1 HTML — §3.2. Threat Model; excerpt=tic Guardrails. Formal Reasoning Based on Large Models. Intent Formalization. 8 Discussion 8.1 Limitation 8.2 Future Work 9 Conclusion 10 Ethical Considerations 11 Generative AI Usage References A Open Science A.1 Description and Requirements A.1.1 How to access. A.1.2 Hardware Dependencies. A.1.3 Software Dependencies. A.1.4 Models. A.1.5 Datasets. A.2 Artifact Installation and Configuration A.3 Experiment Workflow`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29251:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29251:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [OpenClawBench: Benchmarking Process-side Anomalies in Real-world Agent Execution Trajectories](https://arxiv.org/html/2605.29253v1)

问题与机制：We study this mismatch as the Outcome-Process Gap and introduce OpenClawBench, a large-scale dataset for measuring and supervising process-side anomalies in real agent execution processes. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：These results show that success-only evaluation misses a concrete class of process-side failures in real agent executions.。Method=`arXiv:2605.29253v1 HTML — §Introduction / disclosed mechanism body; excerpt=labels, and risk slices are used as annotation priors rather than ground truth. We introduce OpenClawBench to make the Outcome–Process Gap measurable in real OpenClaw agent traces. OpenClawBench is built from BFCL-grounded executions produced by a real agent stack with tool and environment interaction, rather than from outcome labels or synthetic trajectories alone. It addresses a core data construction question: how`；Evaluation=`arXiv:2605.29253v1 HTML — §OpenClawBench: Benchmarking Process-side Anomalies in Real-world Agent Execution Trajectories; excerpt=Abstract 1 Introduction 2 Related Work 2.1 Agent benchmarks and outcome-centric evaluation 2.2 Trajectory-aware evaluation and process anomaly auditing 2.3 Real-agent misbehavior and runtime intervention 3 OpenClawBench: Data Source, Construction Pipeline, and Data Protocol 3.1 Data source and trajectory collection 3.2 From sessions to structured process evidence 3.3 Outcome-aware fusion and anomaly taxonomy 3.4 Full`。

Trade-off / failure / fallback：`arXiv:2605.29253v1 HTML — §Limitations.; excerpt=ows uniform improvement 6.3 Finding III: cross-backbone hold-out generalization Limitations. 7 Conclusion References A Dataset Collection Details A.1 Task source A.2 Agent executions A.3 Raw records and normalized construction inputs A.4 Split construction A.5 Calibration subset A.6 Construction boundary B Trajectory Schema and Event Evidence B.1 Normalized trajectory representation B.2 Parsing rules B.3 Step-level e`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29253:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29253:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling](https://arxiv.org/html/2605.29262v1)

问题与机制：To resolve this conflict, we introduce RACE-Sched, an asynchronous agent-based framework that decouples policy execution from logical reasoning via a dual-stream architecture. owner=`AGENT-WORKFLOW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Extensive evaluations on GEN-Bench, MK-Bench, and JMS-Bench demonstrate that RACE-Sched outperforms leading Deep Reinforcement Learning and other LLM-based baselines.。Method=`arXiv:2605.29262v1 HTML — §Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling; excerpt=ng. LLM Reasoning and Code-as-Policy. 3 Problem Formulation and Preliminaries 4 Methodology 4.1 Asynchronous Dual Stream Architecture 4.1.1 Reactive Stream for Execution 4.1.2 Deliberative Reasoning Stream for Policy Evolution 4.1.3 Trigger Update Protocol and Atomic Transition 4.2 The Agentic Loop: A Safety-Constrained Evolutionary Cycle 4.2.1 Strategic Planner for Bottleneck-Aware Reasoning 4.2.2 Syntactic Enforcer`；Evaluation=`arXiv:2605.29262v1 HTML — §5 Experiments; excerpt=cture of the Knowledge Repository 4.3.2 Retrieval and Cross Scenario Transfer 5 Experiments 5.1 Experimental Setup 5.1.1 Benchmark Datasets and Evaluation Metrics 5.1.2 Baseline Methods and LLM Backends 5.2 Performance and Efficiency 5.2.1 Scheduling Performance Analysis 5.2.2 Token Consumption Assessment 5.2.3 Real-Time Latency Evaluation 5.3 Ablation Studies 5.3.1 Contribution of Epistemic Transfer via Rule Reposit`。

Trade-off / failure / fallback：`arXiv:2605.29262v1 HTML — §5.4 Resilience Under Machine Failures; excerpt=itory 5.3.2 Impact of Recursive Agentic Refinement 5.4 Resilience Under Machine Failures 6 Conclusion References License: CC BY 4.0 arXiv:2605.29262v1 [cs.AI] 28 May 2026 Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling Shijie Cao Affiliation: School of Computer Science and Engineering, Beihang University, Beijing 100191, China Affiliation: Shenzhe`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29262:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29262:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md` 的当前正文，采用命题与 prior comparison 未变。

### [When and How Human Curation Backfires: Preference Alignment under Multi-Model Self-Consuming Loop](https://arxiv.org/html/2605.29267v1)

问题与机制：Unlike isolated settings where human curation always enhances model alignment, we show that cross-model interactions can dampen or even invert this effect, ultimately degrading long-term alignment. owner=`TRAIN-DPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Unlike isolated settings where human curation always enhances model alignment, we show that cross-model interactions can dampen or even invert this effect, ultimately degrading long-term alignment.。Method=`arXiv:2605.29267v1 HTML — §2 Problem Formulation; excerpt=R. A. Bradley and M. E. Terry Rank analysis of incomplete block designs: i. the method of paired comparisons . Biometrika 39 ( 3/4 ), pp. 324–345 . Cited by: item 3 . Brown et al. (2022) G. Brown, S. Hod, and I. Kalemaj Performative prediction in a stateful world . In International conference on artificial intelligence and statistics , pp. 6045–6061 . Cited by: Appendix A . Cai et al. (2026) Z. Cai, Y. Wang, Y. Liu,`；Evaluation=`arXiv:2605.29267v1 HTML — §5 Experiments; excerpt=ative Impact of Human Curation 4.4 From Local Sensitivity to Global Deviation 5 Experiments 5.1 Mechanism Validation 5.2 Convergence and The Impact of Human Curation 5.3 Preference Domain Mismatch (PDM) Experiments References A Related work B Discussion B.1 Limitations of our framework C Conclusion D Experiment Discussion And Additional Experiments D.1 Experiments on CIFAR-10 datasets D.1.1 Settings D.1.2 Reward desi`。

Trade-off / failure / fallback：`arXiv:2605.29267v1 HTML — §Appendix B Discussion; excerpt=on 5.3 Preference Domain Mismatch (PDM) Experiments References A Related work B Discussion B.1 Limitations of our framework C Conclusion D Experiment Discussion And Additional Experiments D.1 Experiments on CIFAR-10 datasets D.1.1 Settings D.1.2 Reward design D.1.3 Additional results of CIFAR-10 experiments D.2 Preference domain mismatch and Qwen2.5-0.5B experiment settings D.3 Mechanism validation experiment setting`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29267:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29267:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-DPO` / `books/part-04-training-system/34-dpo.md` 的当前正文，采用命题与 prior comparison 未变。

### [Prompt-Level Reward Specifications for Open-Ended Post-Training](https://arxiv.org/html/2605.29275v1)

问题与机制：We propose a prompt-level reward specification framework that separates reward specification from reward computation. owner=`TRAIN-DPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments show that the resulting reward improves offline RM-style response ranking and supports online reinforcement learning across multiple open-ended benchmarks.。Method=`arXiv:2605.29275v1 HTML — §Rubric-based evaluation and reward design.; excerpt=ion and reward design. Prompt-level reward specifications and hybrid rewards. 3 Method 3.1 Overview and Problem Formulation 3.2 Offline Reward Specification Construction Task-adaptive rubric. Hard-constraint checkers. 3.3 Online Hybrid Reward Computation Rubric-based score. Global score. Code-based score. Unified hybrid reward. 3.4 Why Hybrid Reward? 4 Experiments 4.1 Experimental Setup Reward pipeline instantiation.`；Evaluation=`arXiv:2605.29275v1 HTML — §Rubric-based evaluation and reward design.; excerpt=F Abstract 1 Introduction 2 Related Work RL for LLM post-training. Rubric-based evaluation and reward design. Prompt-level reward specifications and hybrid rewards. 3 Method 3.1 Overview and Problem Formulation 3.2 Offline Reward Specification Construction Task-adaptive rubric. Hard-constraint checkers. 3.3 Online Hybrid Reward Computation Rubric-based score. Global score. Code-based score. Unified hybrid reward. 3.4`。

Trade-off / failure / fallback：`arXiv:2605.29275v1 HTML — §6 Conclusion; excerpt=Training Setup A.3 Evaluation Protocols and Settings A.4 Checker Validation and Failure Handling A.5 Reproducibility and Released Artifacts B Additional Analysis B.1 Component Ablation with Qwen3-30B-A3B B.2 Reliability Analysis of Code-Based Verification Main finding. Analysis setup. Metrics. Discussion. B.3 Diagnostic Analysis of Advantage Normalization Main finding. Setup. Rationale. Discussion. B.4 Additional Det`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29275:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29275:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-DPO` / `books/part-04-training-system/34-dpo.md` 的当前正文，采用命题与 prior comparison 未变。

### [PatchBoard: Schema-Grounded State Mutation for Reliable and Auditable LLM Multi-Agent Collaboration](https://arxiv.org/html/2605.29313v1)

问题与机制：We introduce PatchBoard, a schema-grounded collaboration architecture that replaces inter-agent dialogue with validated JSON Patch mutations over a shared structured state. owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：On 630 matched ALFWorld episodes, PatchBoard achieves an 84.6% success rate, compared with 30.8% for LangGraph and 61.6% for Flock, while reducing tokens per successful task to 45.5k, compared with 368.3k and 64.2k, respectively.。Method=`arXiv:2605.29313v1 HTML — §3 Methodology; excerpt=nd agent memory. Structured outputs, transactions, and semantic verification. 3 Methodology 3.1 Method Overview 3.2 Architect and Task Blueprint 3.3 Schema-Grounded Patch Interface 3.4 Deterministic Kernel 3.5 Budgeted Context Views 3.6 Structural Properties 4 Experimental Setup 4.1 Evaluation Goals 4.2 Benchmarks and Systems 4.3 Metrics and Estimation 4.4 Fault Injection 5 Results and Analysis 5.1 Main ALFWorld Resu`；Evaluation=`arXiv:2605.29313v1 HTML — §4 Experimental Setup; excerpt=3.4 Deterministic Kernel 3.5 Budgeted Context Views 3.6 Structural Properties 4 Experimental Setup 4.1 Evaluation Goals 4.2 Benchmarks and Systems 4.3 Metrics and Estimation 4.4 Fault Injection 5 Results and Analysis 5.1 Main ALFWorld Results 5.2 Blackboard Controls 5.3 Ablation Study 5.4 Sensitivity Analyses 5.5 Fault Isolation and Termination 6 Conclusion References A PatchBoard Kernel Pseudocode B Implementation a`。

Trade-off / failure / fallback：`arXiv:2605.29313v1 HTML — §6 Conclusion; excerpt=ion. Dialogue histories grow with the number of turns, mix task facts with meta-discussion and repair attempts, and often leave unclear which intermediate outputs should be treated as committed state. A downstream agent may read an unverified observation, stale plan, malformed intermediate claim, or failed repair attempt as if it were reliable task state. Once such information enters the shared context, later agents`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29313:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29313:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MULTI-AGENT` / `books/part-07-agent/82-multi-agent.md` 的当前正文，采用命题与 prior comparison 未变。

### [STAMP: Training Explicit Memory for Mobile GUI Agents in Controllable and Scalable Virtual Environments](https://arxiv.org/html/2605.29324v1)

问题与机制：To resolve this, we present STAMP, a framework that trains explicit memory in mobile agents through controllable virtual environments, where deterministic memory variables are programmatically injected into synthesized tasks to control what must be memorized, when it should be encoded, and when it must later be retrieved, thereby producing verifiable supervised data at scale and enabling online reinforcement learning through environment-driven reward feedback. owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Evaluated on our newly introduced Memory-World benchmark, the resulting Stamp-GUI agent achieves state-of-the-art performance among GUI-specialized models and sets a new high watermark on our Memory-World benchmark, demonstrating exceptional memory accuracy and task resilience while maintaining strong general mobile navigation capabilities.。Method=`arXiv:2605.29324v1 HTML — §3 Method; excerpt=t 1 Introduction 2 Related Works 2.1 Mobile GUI Agent 2.2 Memory in GUI Agent 3 Method 3.1 Overview 3.2 Problem Setup 3.3 Virtual Environment Data Construction 3.4 Supervised Training 3.5 Online Reinforcement Learning 4 Experiments 4.1 Benchmarks and Metrics 4.2 Baselines and Implementation Details 4.3 Main Results Consistent Dominance Across Evaluation Levels. Memory Fidelity as a Foundation for Task Success. Multi-`；Evaluation=`arXiv:2605.29324v1 HTML — §4 Experiments; excerpt=t Data Construction 3.4 Supervised Training 3.5 Online Reinforcement Learning 4 Experiments 4.1 Benchmarks and Metrics 4.2 Baselines and Implementation Details 4.3 Main Results Consistent Dominance Across Evaluation Levels. Memory Fidelity as a Foundation for Task Success. Multi-Attempt Scalability. 4.4 Ablation Study 4.5 Detailed Empirical Analysis Qualitative Case Study. General Mobile Capability. Effect of Step Ba`。

Trade-off / failure / fallback：`arXiv:2605.29324v1 HTML — §5 Conclusion; excerpt=e Capability. Effect of Step Balancing. Dynamic testing quality. 5 Conclusion 6 Limitations References A Appendix A.1 Output Format A.2 Memory Content Storage Step output format. A.2.1 Two-Tier History Retention A.2.2 History Construction from Old Steps A.2.3 Storage Behavior for Empty Memory A.3 Benchmark Details A.3.1 AndroidWorld-M A.3.2 MemGUI-Bench A.4 Prompt Templates A.4.1 System Prompt A.4.2 User Prompt A.4.3`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29324:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29324:end -->

**当前 Books 投影。** `Applied` 到 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；当前正文唯一 marker 已核验，未产生新写回。

### [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/html/2605.29341v1)

问题与机制：To close these gaps, we formulate multimodal agent memory as an Action-World Interaction Loop with an observable four-stage lifecycle, and instantiate it in WorldMemArena: 400 multi-session multimodal tasks spanning Lifelong Evolution (evolving personal and task states) and Agentic Execution (memory from real observations, actions, and feedback), annotated with gold memory points, updates, distractors, and evidence chains for stage-level diagnosis. owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Results show that: (1) better memory writing and storage do not guarantee better performance; (2) multimodal memory still struggles to fully use visual evidence; (3) systems are unstable across domains and degrade on realistic agentic trajectories; and (4) harness memory is more flexible but remains costly and less reliable.。Method=`arXiv:2605.29341v1 HTML — §3 Problem Formulation; excerpt=profile of memory baselines. Retrieval on WorldMemArena. Variance across memory architectures. Backbone competence along 11 types of capabilities. F More Analysis ❖ Long-horizon collapse. License: arXiv.org perpetual non-exclusive license arXiv:2605.29341v1 [cs.CV] 28 May 2026 \settitleleftlogo [2.2cm]assets/logo_title.png \settitleleftlogogap -2.2mm \settitleleftlogooffset 3mm-3mm \settitleboxverticalpadding 5mm5mm`；Evaluation=`arXiv:2605.29341v1 HTML — §4.4 Evaluation Protocol; excerpt=n-World Interaction 4.1 Memory Regimes 4.2 Data Collection 4.3 Data Statics 4.4 Evaluation Protocol 5 Experiments 5.1 Main Results 6 Analysis 7 Discussion 8 Conclusion References A Experimental Setting B Evaluation Metrics B.1 Notation B.2 Memory metrics B.3 QA metrics B.4 Retrieval metrics B.5 Per-question-type accuracy C Additional dataset details C.1 Data sources C.2 Quality validation C.3 Further Introduction to`。

Trade-off / failure / fallback：`arXiv:2605.29341v1 HTML — §7 Discussion; excerpt=ata Statics 4.4 Evaluation Protocol 5 Experiments 5.1 Main Results 6 Analysis 7 Discussion 8 Conclusion References A Experimental Setting B Evaluation Metrics B.1 Notation B.2 Memory metrics B.3 QA metrics B.4 Retrieval metrics B.5 Per-question-type accuracy C Additional dataset details C.1 Data sources C.2 Quality validation C.3 Further Introduction to Dataset Domains Lifelong evolution. Professional verticals domai`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29341:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29341:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [Draft-OPD: On-Policy Distillation for Speculative Draft Models](https://arxiv.org/html/2605.29343v1)

问题与机制：A common way to build draft models, like EAGLE3 or DFlash is supervised fine-tuning (SFT) on target-generated trajectories. owner=`TRAIN-SFT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments show that Draft-OPD achieves over $5\times$ lossless acceleration for thinking models across diverse tasks, improving over EAGLE-3 and DFlash by 23\% and 13\%.。Method=`arXiv:2605.29343v1 HTML — §4 Method; excerpt=odel Distillation 3 Preliminary Speculative Decoding. On-Policy Distillation. 4 Method 4.1 Challenges of Direct OPD 4.2 Draft-OPD Rollout with error-position collection. Replay for Log-Probability Computation. Acceptance-Aware Distillation Objective. 5 Experiment Models and tasks. Datasets. Implementation. Baselines. Metrics. 5.1 Main Results Thinking Mode Enabled. Thinking Mode Disabled. Performance on SGLang. 5.2 A`；Evaluation=`arXiv:2605.29343v1 HTML — §5 Experiment; excerpt=lay for Log-Probability Computation. Acceptance-Aware Distillation Objective. 5 Experiment Models and tasks. Datasets. Implementation. Baselines. Metrics. 5.1 Main Results Thinking Mode Enabled. Thinking Mode Disabled. Performance on SGLang. 5.2 Ablation Study Training Data. KL Type. Anchor Position. Weight Decay. 5.3 Analysis Experiments Target-Assisted Rollout. Thinking-Mode Draftability Gap. 6 Conclusion Training`。

Trade-off / failure / fallback：`arXiv:2605.29343v1 HTML — §6 Conclusion; excerpt=ta used for OPD can even reduce the accepted length. This suggests that the key limitation does not lie in offline training compute. Instead, the plateau points to a mismatch between the states used for training and the states that determine speculative acceptance. In SFT, the drafter learns from fixed target-generated trajectories, so every prefix is produced by the target model. During speculative decoding, however`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29343:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29343:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-SFT` / `books/part-04-training-system/29-sft.md` 的当前正文，采用命题与 prior comparison 未变。

### [ConMoE: Expert-Pool Consolidation via Prototype Reassignment for MoE Compression](https://arxiv.org/html/2605.29350v1)

问题与机制：We formulate post-training MoE compression as expert-pool consolidation: retaining a smaller set of pretrained experts as reusable prototypes and deterministically remapping each original expert reference to one selected prototype. owner=`MODEL-MOE`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on three pretrained MoE language models show that ConMoE matches or outperforms strong pruning and merging baselines in several settings, achieving the best average score on deepseek-moe-16b-base at both 25% and 50% routed-expert reduction, while remaining competitive on Qwen3-30B-A3B and OLMoE-1B-7B-0125.。Method=`arXiv:2605.29350v1 HTML — §3 Problem Formulation; excerpt=se MoE Expert Pools 3.2 Expert-Pool Consolidation 3.3 Consolidation Objective 4 Method 4.1 Prototype Scoring 4.2 Prototype Selection and Reassignment 4.3 Consolidated MoE Operator 5 Experiments 5.1 Experimental Setup Models. Calibration and evaluation. Baselines. 5.2 Main Results 5.3 Ablation Studies Consolidation structure. Effect of scope size. Prototype selection. Post-hoc fusion diagnostics. 5.4 Analysis: Local C`；Evaluation=`arXiv:2605.29350v1 HTML — §5 Experiments; excerpt=coring 4.2 Prototype Selection and Reassignment 4.3 Consolidated MoE Operator 5 Experiments 5.1 Experimental Setup Models. Calibration and evaluation. Baselines. 5.2 Main Results 5.3 Ablation Studies Consolidation structure. Effect of scope size. Prototype selection. Post-hoc fusion diagnostics. 5.4 Analysis: Local Cross-layer Expert Substitutability 6 Discussion 7 Conclusion References A Reproducibility and Complian`。

Trade-off / failure / fallback：`arXiv:2605.29350v1 HTML — §6 Discussion; excerpt=c fusion diagnostics. 5.4 Analysis: Local Cross-layer Expert Substitutability 6 Discussion 7 Conclusion References A Reproducibility and Compliance AI assistant use. Artifacts and licenses. Compute. B Implementation Details B.1 Distance and Normalization B.2 Compression Accounting and Evaluation Checkpoints B.3 Calibration Data B.4 Evaluation Metrics C Baseline and Ablation Details Frequency pruning. REAP pruning. M-`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29350:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29350:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MODEL-MOE` / `books/part-02-model/21-moe.md` 的当前正文，采用命题与 prior comparison 未变。

### [Does Distributed Training Undermine Compute Governance?](https://arxiv.org/html/2605.29359v1)

问题与机制：Compute governance proposals often rely on the assumption that frontier AI training requires large, detectable computing clusters. owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：This paper evaluates the feasibility of such evasion and outlines recommended countermeasures, including whistleblowing, chip tracking, forensic accounting, and memory and compute thresholds for clusters.。Method=`arXiv:2605.29359v1 HTML — §3 Methodology; excerpt=o Abstract Download PDF Abstract 1 Introduction 2 Background and Related Work 3 Methodology 3.1 Threat Model 3.2 Hardware Selection 3.3 Efficiency Model 3.4 Chinchilla Quality Adjustment 3.5 Pipeline-parallel DiLoCo 4 Results 5 Discussion 5.1 Assumptions 5.2 Evader Strategy 5.3 Countermeasures 5.4 The Simulator 6 Conclusion Impact Statement LLM Usage Statement Acknowledgements A Training Time Limit B Hardware Configu`；Evaluation=`arXiv:2605.29359v1 HTML — §4 Results; excerpt=ficiency Model 3.4 Chinchilla Quality Adjustment 3.5 Pipeline-parallel DiLoCo 4 Results 5 Discussion 5.1 Assumptions 5.2 Evader Strategy 5.3 Countermeasures 5.4 The Simulator 6 Conclusion Impact Statement LLM Usage Statement Acknowledgements A Training Time Limit B Hardware Configurations B.1 Standard Commercial Pods B.2 Nodes Under the 16 H100-Equivalent Threshold C Bandwidth Sensitivity D Simulator and Modeling Doc`。

Trade-off / failure / fallback：`arXiv:2605.29359v1 HTML — §3.1 Threat Model; excerpt=odel 3.4 Chinchilla Quality Adjustment 3.5 Pipeline-parallel DiLoCo 4 Results 5 Discussion 5.1 Assumptions 5.2 Evader Strategy 5.3 Countermeasures 5.4 The Simulator 6 Conclusion Impact Statement LLM Usage Statement Acknowledgements A Training Time Limit B Hardware Configurations B.1 Standard Commercial Pods B.2 Nodes Under the 16 H100-Equivalent Threshold C Bandwidth Sensitivity D Simulator and Modeling Documentation`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29359:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29359:end -->

**当前 Books 投影。** `Applied` 到 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md`；当前正文唯一 marker 已核验，未产生新写回。

### [MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models](https://arxiv.org/html/2605.29360v1)

问题与机制：We introduce \textsc{MiraBench}, a hierarchical benchmark that defines \emph{action-conditioned reliability} as a core evaluation target for robotic world models. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We introduce \textsc{MiraBench}, a hierarchical benchmark that defines \emph{action-conditioned reliability} as a core evaluation target for robotic world models.。Method=`arXiv:2605.29360v1 HTML — §3 Problem Formulation; excerpt=Reproducibility I.1 Action-Conditioned World Model Post-Training Base model and architecture. Training data. Tokenizer and text encoder. Inference. Code and scripts. I.2 Benchmark Evaluation Configuration Critical notes for reproduction. I.3 Random Seeds and Determinism I.4 Data and Model Availability J Physics Consistency Gallery J.1 Per-Indicator Ablation Key observations. J.2 Case 1: Cascading Failure under Full O`；Evaluation=`arXiv:2605.29360v1 HTML — §Evaluation benchmarks for video world models.; excerpt=wnload PDF Abstract 1 Introduction 2 Related Work World models for embodied AI. Evaluation benchmarks for video world models. Physical reasoning in video models. Action following, policy learning, and synthetic data. 3 Problem Formulation World model as a conditional generator. Physical Adherence. Optimism Bias. 4 Motivating Study 5 Design of MIRABENCH 5.1 Construction of Test Cases 5.2 Human-Grounded Evaluator 6 Exp`。

Trade-off / failure / fallback：`arXiv:2605.29360v1 HTML — §7 Conclusion; excerpt=ta Format and Organisation. Task Coverage. Train / Validation Split. B Implicit Failure Perturbation Taxonomy B.1 Perturbation Definitions 1. Grip Force Insufficient ( grip_force_weak ). 2. Premature Release ( premature_release ). 3. Grip Carry Slip ( grip_carry_slip ). 4. Contact Oscillation ( contact_oscillation ). 5. Wrist Tilt During Grasp ( wrist_tilt_grasp ). 6. Approach Overshoot ( approach_overshoot ). B.2 Pe`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29360:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29360:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [On the Optimizer Dependence of Neural Scaling Laws](https://arxiv.org/html/2605.29387v1)

问题与机制：We present evidence that $α$ depends systematically on the optimizer. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Our results imply that scaling-law forecasts should account for optimizer choice, and we provide a spectral diagnostic predicting when advanced optimizers will pay off.。Method=`arXiv:2605.29387v1 HTML — §Appendix C Experimental Algorithm; excerpt=∝ N − α L(N)\propto N^{-\alpha} is commonly treated as a fixed constant set by architecture and data. We present evidence that α \alpha depends systematically on the optimizer. In controlled random-feature regression experiments—the canonical theoretical framework for neural scaling—we measure α \alpha across five optimizer variants and six spectral conditions. Preconditioned optimizers consistently yield steeper sc`；Evaluation=`arXiv:2605.29387v1 HTML — §3 Simulation Results; excerpt=ioners 2.3 Spectral Intuition: Why Preconditioning Shifts α \alpha 3 Simulation Results 3.1 Experimental Protocol 3.2 Core Results 3.3 Interpretation 4 Validation Against Published Results 5 Discussion and Limitations References A Full Numerical Results B Experimental Details B.1 Hyperparameters B.2 Fitting Procedure B.3 Data Generation C Experimental Algorithm D Derivation Supporting Proposition D.1 Claim (i): Preco`。

Trade-off / failure / fallback：`arXiv:2605.29387v1 HTML — §5 Discussion and Limitations; excerpt=ol 3.2 Core Results 3.3 Interpretation 4 Validation Against Published Results 5 Discussion and Limitations References A Full Numerical Results B Experimental Details B.1 Hyperparameters B.2 Fitting Procedure B.3 Data Generation C Experimental Algorithm D Derivation Supporting Proposition D.1 Claim (i): Preconditioning increases α \alpha D.2 Claim (ii): Δ ​ α \Delta\alpha is monotone increasing in s s D.3 Claim (iii):`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29387:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29387:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/html/2605.29438v1)

问题与机制：We propose ElegantVLA, a plug-in phase-adaptive inference framework that accelerates VLA models through intra-model dynamic compute scheduling. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on GR00T and CogACT achieve up to 2.55x and 3.77x speedup, and on six real-world GR00T tasks ElegantVLA cuts computation by 2.18x while raising control frequency from 13.8 Hz to 26.3 Hz.。Method=`arXiv:2605.29438v1 HTML — §3 Method; excerpt=rt Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work 3 Method 3.1 Phase-Adaptive Scheduling Framework 3.2 Semantic-Stability-Guided Vision–LLM Scheduling 3.3 Motion-Aware Action-Head Scheduling 3.4 Two-Stage Joint RL Scheduler Design 4 Experiments 4.1 Main Results 4.2 Analysis 5 Conclusion References A Real-World Protocol and Additional Results Platform and protocol. Task design and analysis.`；Evaluation=`arXiv:2605.29438v1 HTML — §4 Experiments; excerpt=3 Motion-Aware Action-Head Scheduling 3.4 Two-Stage Joint RL Scheduler Design 4 Experiments 4.1 Main Results 4.2 Analysis 5 Conclusion References A Real-World Protocol and Additional Results Platform and protocol. Task design and analysis. Additional real-world results. B Simulation Environment and Task Protocol Benchmark protocol. Task groups. C Additional Scheduler Ablations C.1 Effect of Rule-Based and Two-Stage R`。

Trade-off / failure / fallback：`arXiv:2605.29438v1 HTML — §5 Conclusion; excerpt=manipulation . arXiv preprint arXiv:2503.20384 . Cited by: Table 1 , Table 1 . Limitations and Responsible Use This work is a technical study of inference-time acceleration for already trained vision-language-action robot policies. It does not involve new human-subject data, personal data, or deployment decisions, and we do not identify direct social or ethical concerns specific to the proposed scheduling method. As`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29438:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29438:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions](https://arxiv.org/html/2605.29442v1)

问题与机制：We present an observational study of 20,574 coding-agent sessions from 1,639 repositories across IDE and CLI workflows. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Our findings inform the design of training, evaluation, and interfaces for keeping coding agents aligned with real developer workflows.。Method=`arXiv:2605.29442v1 HTML — §3 Methodology; excerpt=eloper Workflows 2.2 Failure Analysis of Coding Agents 2.3 Human-AI Alignment 3 Methodology 3.1 Datasets 3.2 Structured Misalignment Extraction Scope. Session preprocessing. Extraction. 3.3 Post-Extraction Validation Precision and Coverage Estimation. 3.4 Multi-Axial Annotation Codebook development. Annotation and validation. 4 Results 4.1 RQ1: Forms and Causes of Misalignment Developer Constraint Violation (S3, 38.3`；Evaluation=`arXiv:2605.29442v1 HTML — §How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions; excerpt=. 3.4 Multi-Axial Annotation Codebook development. Annotation and validation. 4 Results 4.1 RQ1: Forms and Causes of Misalignment Developer Constraint Violation (S3, 38.33%). Misread Developer Intent (S2, 26.95%). Inaccurate Self-Reporting (S7, 22.58%). Faulty Implementation (S5, 17.82%). Wrong Project Diagnosis (S1, 11.56%). Self-Initiated Overreach (S4, 10.20%). Operational Execution Error (S6, 2.87%). Additional c`。

Trade-off / failure / fallback：`arXiv:2605.29442v1 HTML — §2.2 Failure Analysis of Coding Agents; excerpt=ract 1 Introduction 2 Related Work 2.1 Coding Agents in Developer Workflows 2.2 Failure Analysis of Coding Agents 2.3 Human-AI Alignment 3 Methodology 3.1 Datasets 3.2 Structured Misalignment Extraction Scope. Session preprocessing. Extraction. 3.3 Post-Extraction Validation Precision and Coverage Estimation. 3.4 Multi-Axial Annotation Codebook development. Annotation and validation. 4 Results 4.1 RQ1: Forms and Caus`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29442:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29442:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [A Full-Pipeline Framework for Evaluating Membership Inference Attacks in Machine Learning](https://arxiv.org/html/2605.29454v1)

问题与机制：To bridge this gap and provide actionable insights, we introduce a comprehensive evaluation framework that systematically characterizes privacy risks across the entire machine learning pipeline, spanning data, architectures, algorithms, and post-training modules. owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：To bridge this gap and provide actionable insights, we introduce a comprehensive evaluation framework that systematically characterizes privacy risks across the entire machine learning pipeline, spanning data, architectures, algorithms, and post-training modules.。Method=`arXiv:2605.29454v1 HTML — §A Full-Pipeline Framework for Evaluating Membership Inference Attacks in Machine Learning; excerpt=Abstract Download PDF Abstract Keywords: 1 Introduction 2 Related Works 2.1 MIA Methods 2.2 MIA Surveys 3 Unified Evaluation Protocol 3.1 Threat Model 3.2 Metrics 3.3 Full-Pipeline Benchmark Framework 4 Evaluation and Observation 4.1 Impact of Threat Models 4.2 Impact of Data 4.3 Impact of Architectures 4.4 Impact of Training Algorithms 4.5 Impact of Post Training 5 Discussion 5.1 Comparison among Top-Performing MIA`；Evaluation=`arXiv:2605.29454v1 HTML — §3 Unified Evaluation Protocol; excerpt=words: 1 Introduction 2 Related Works 2.1 MIA Methods 2.2 MIA Surveys 3 Unified Evaluation Protocol 3.1 Threat Model 3.2 Metrics 3.3 Full-Pipeline Benchmark Framework 4 Evaluation and Observation 4.1 Impact of Threat Models 4.2 Impact of Data 4.3 Impact of Architectures 4.4 Impact of Training Algorithms 4.5 Impact of Post Training 5 Discussion 5.1 Comparison among Top-Performing MIA Methods 5.2 Overfitting leads to M`。

Trade-off / failure / fallback：`arXiv:2605.29454v1 HTML — §3.1 Threat Model; excerpt=f Architectures 4.4 Impact of Training Algorithms 4.5 Impact of Post Training 5 Discussion 5.1 Comparison among Top-Performing MIA Methods 5.2 Overfitting leads to MIA vulnerability 5.3 Takwaway Message for practitioners 6 Conclusion 7 Acknowledgments References A Additional Experimental Results A.1 Performance of Target Model in the Experiments License: CC BY 4.0 arXiv:2605.29454v1 [cs.LG] 28 May 2026 A Full-Pipelin`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29454:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29454:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [Honest Lying: Understanding Memory Confabulation in Reflexive Agents](https://arxiv.org/html/2605.29463v1)

问题与机制：We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time.。Method=`arXiv:2605.29463v1 HTML — §3 Problem Formulation; excerpt=flective memory and reused across trials despite contradictory task evidence. • We introduce the Reflection Repetition Rate (RRR) , a log-based diagnostic for frozen reflective memory that strongly correlates with trials-to-solve in ALFWorld ( shridhar2020alfworld ) ( r = 0.808 r=0.808 ). • We provide cross-domain evidence from ALFWorld and HumanEval ( Chen et al., 2021 ) , finding that 0/121 reflections in 16 frozen`；Evaluation=`arXiv:2605.29463v1 HTML — §4.1 RRR Analysis; excerpt=Confabulation 4.3 Cross-Domain Replication 4.4 Evidence of Memory Confabulation Results. 5 Mitigation and Results 5.1 Grounded Reflection 5.2 Programmatic Feedback Extraction 5.3 ALFWorld Results env_35 case study. 5.4 HumanEval Results Confabulation in code generation. Domain-adapted extraction. Cross-domain parallel. 6 Discussion 6.1 The Feedback Granularity Hypothesis 6.2 Model Capability and Confabulation 6.3 Gen`。

Trade-off / failure / fallback：`arXiv:2605.29463v1 HTML — §3.3 Two Failure Categories; excerpt=Definition (Memory Confabulation). 3.2 Reflection Repetition Rate (RRR) 3.3 Two Failure Categories 4 Evidence of Memory Confabulation 4.1 RRR Analysis 4.2 Task-Object Confabulation 4.3 Cross-Domain Replication 4.4 Evidence of Memory Confabulation Results. 5 Mitigation and Results 5.1 Grounded Reflection 5.2 Programmatic Feedback Extraction 5.3 ALFWorld Results env_35 case study. 5.4 HumanEval Results Confabulation in`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29463:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29463:end -->

**当前 Books 投影。** `Applied` 到 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；当前正文唯一 marker 已核验，未产生新写回。

### [FLASH-MAXSIM: IO-Aware Fused Kernels for Late-Interaction Retrieval](https://arxiv.org/html/2605.29517v1)

问题与机制：We present Flash-MaxSim (FM), an IO-aware fused GPU kernel that computes the same MaxSim scores without ever materialising the tensor, and extends the same principle to the training backward. owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：The kernel is a drop-in replacement, exact up to floating-point evaluation order under its stated FP32-accumulation protocol: rankings match the FP32 reference within 5e-4 of nDCG@10 on BEIR and REAL-MM-RAG.。Method=`arXiv:2605.29517v1 HTML — §3.3 System-Level Constraints in Real Deployments; excerpt=intensity and the roofline. 3.3 System-Level Constraints in Real Deployments 4 Methodology 4.1 Fused Forward: Materialization-Free Scoring via Online Max 4.1.1 Online-Max Recurrence 4.1.2 IO Complexity and Roofline 4.1.3 Numerical Fidelity 4.1.4 Kernel Family 4.2 Inverse-Grid Update: Low-Contention Gradient Aggregation 4.2.1 Closed-Form Gradients 4.2.2 Runtime Inverse-Grid Construction 4.2.3 Destination-Owned Reduct`；Evaluation=`arXiv:2605.29517v1 HTML — §5 Experiments; excerpt=ants 4.3.1 INT8 × \times INT8 Quantization 4.3.2 Padding-Free Variable-Length 5 Experiments 5.1 Experimental Setup 5.2 Forward Latency and Memory HBM traffic validates the IO bound. Tile-size robustness. Memory and the OOM unlock. 5.3 Out-of-Core Corpus Scaling 5.4 Training Step 5.5 Variable-Length Scoring 5.6 Numerical Correctness 6 Conclusion Limitations. References License: arXiv.org perpetual non-exclusive licens`。

Trade-off / failure / fallback：`arXiv:2605.29517v1 HTML — §6 Conclusion; excerpt=raining Step 5.5 Variable-Length Scoring 5.6 Numerical Correctness 6 Conclusion Limitations. References License: arXiv.org perpetual non-exclusive license arXiv:2605.29517v1 [cs.IR] 28 May 2026 Flash-MaxSim : IO-Aware Fused Kernels for Late-Interaction Scoring Roi Pony † † thanks: Corresponding author: roi.pony@ibm.com . Adi Raz Goldfarb Idan Friedman Daniel Ezer Udi Barzelay Affiliation: IBM Research Israel Abstract`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29517:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29517:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md` 的当前正文，采用命题与 prior comparison 未变。

### [KBF: Knowledge Boundary as Fingerprint for Language Model and Black-Box API Auditing](https://arxiv.org/html/2605.29524v1)

问题与机制：We introduce KBF, a low-cost black-box auditing protocol that fingerprints model APIs using stable numerical recall near the knowledge boundary. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across 16 production LLM endpoints, KBF flags all 155 economically relevant substitutions without rejecting any same-model controls, remains stable under deployment variation, detects high-separation mixed-routing attacks when only 5-10% of traffic is substituted, and finds that 7 of 27 platform model cells in a six-platform shadow API audit are statistically inconsistent with their reference endpoints, with inconsis。Method=`arXiv:2605.29524v1 HTML — §II Problem Formulation and Preliminaries; excerpt=way to verify that a claimed endpoint is actually serving the advertised model. We introduce KBF , a low-cost black-box auditing protocol that fingerprints model APIs using stable numerical recall near the knowledge boundary. Across 16 production LLM endpoints, KBF flags all 155 economically relevant substitutions without rejecting any same-model controls, remains stable under deployment variation, detects high-separ`；Evaluation=`arXiv:2605.29524v1 HTML — §IV Empirical Evaluation; excerpt=udit III-F Adaptive Routing Extension III-G Implementation Details IV Empirical Evaluation IV-A Experimental Setup IV-B Detection Accuracy IV-C Audit Cost IV-D Configuration Robustness IV-E Additional Robustness Analysis IV-F Adaptive Routing Detection IV-G Shadow API Audit IV-H Operational Use and Limitations V Additional Related Work VI Conclusion Future work References A Experimental Setup A-A Prompts and Request`。

Trade-off / failure / fallback：`arXiv:2605.29524v1 HTML — §II-B Access and Threat Model; excerpt=IV-F Adaptive Routing Detection IV-G Shadow API Audit IV-H Operational Use and Limitations V Additional Related Work VI Conclusion Future work References A Experimental Setup A-A Prompts and Request Configuration A-B Implementation Details for Probe Construction B Baseline Implementation Details C Shadow API Platform Mapping License: CC BY 4.0 arXiv:2605.29524v1 [cs.CR] 28 May 2026 KBF: Knowledge Boundary as Fingerp`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29524:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29524:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention](https://arxiv.org/html/2605.29548v1)

问题与机制：We develop a simple phenomenological argument that power-law scaling already suggests that a larger model will be able to learn a part of the data distribution that a smaller model fails to learn, even with infinite training data. owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：To validate this claim and identify its causes, we study the effects of model scaling on a synthetic setup consisting of a mixture of tasks that show monotonic scaling curves.。Method=`arXiv:2605.29548v1 HTML — §Introduction / disclosed mechanism body; excerpt=s, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models: Methods, analysis & insights from training gopher. arXiv preprint arXiv:2112.11446 , 2021. [26] Ibrahim M Alabdulmohsin, Behnam Neyshabur, and Xiaohua Zhai. Revisiting neural scaling laws in language and vision. Advances in Neural Information Processing Systems , 35:22300–22312, 2022. [27] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhr`；Evaluation=`arXiv:2605.29548v1 HTML — §Appendix B Experimental Details; excerpt=ization and Scaling. Generalization and Scaling. Lottery Tickets and Scaling. B Experimental Details B.1 Synthetic Experiment Data-generating process. Model. Optimizer. Metrics. B.2 OLMo Pretraining Pipeline Models. Training hyperparameters. Training pipeline. Compute resources. B.3 Pre-training and Injected Task Data Pre-training data. Reference Tasks. Inject tasks. B.4 Localizing and Measuring Task Features in Sec.`。

Trade-off / failure / fallback：`arXiv:2605.29548v1 HTML — §5 Discussion; excerpt=radient Interference Between General Language Modeling and Our Injected Task. 5 Discussion References A Related Work Multi-Task Learning. Memorization and Scaling. Generalization and Scaling. Lottery Tickets and Scaling. B Experimental Details B.1 Synthetic Experiment Data-generating process. Model. Optimizer. Metrics. B.2 OLMo Pretraining Pipeline Models. Training hyperparameters. Training pipeline. Compute resource`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29548:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29548:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-DATA` / `books/part-04-training-system/27-data.md` 的当前正文，采用命题与 prior comparison 未变。

### [ParaTool: Shifting Tool Representations from Context to Parameters](https://arxiv.org/html/2605.29561v1)

问题与机制：To address these limitations, we propose ParaTool, a framework that projects each tool into a dedicated, loadable set of parameters. owner=`AGENT-TOOL-CALLING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on Stable ToolBench and BFCL demonstrate that ParaTool significantly outperforms strong ICL-based baselines, achieving superior performance while reducing computational complexity.。Method=`arXiv:2605.29561v1 HTML — §3 Methodology; excerpt=oduction 2 Related Work 2.1 Tool Learning 2.2 Parameter-Efficient Fine-Tuning 3 Methodology 3.1 Problem Formalization 3.2 Framework Overview 3.3 Parametric Tool Pre-training 3.4 Soft Tool Selection 3.5 Parametric Tool Fine-tuning 3.6 Theoretical Analysis of Soft Tool Composition 3.7 Complexity Analysis 4 Experiments 4.1 Datasets 4.2 Experimental Settings 4.3 Baselines 4.4 Main Results 4.5 Ablation Study 4.6 Computati`；Evaluation=`arXiv:2605.29561v1 HTML — §3.6 Theoretical Analysis of Soft Tool Composition; excerpt=ing 3.6 Theoretical Analysis of Soft Tool Composition 3.7 Complexity Analysis 4 Experiments 4.1 Datasets 4.2 Experimental Settings 4.3 Baselines 4.4 Main Results 4.5 Ablation Study 4.6 Computational Complexity 4.7 Hyperparameter Analysis 5 Conclusion References A Proofs of Theoretical Results A.1 Proof of Theorem A.2 Proof of Corollary B Benchmark Details C Data Synthesis Details C.1 Data Synthesis for Stable ToolBen`。

Trade-off / failure / fallback：`arXiv:2605.29561v1 HTML — §5 Conclusion; excerpt=s, thereby retaining a dependency on in-context documentation. To address these limitations, we propose ParaTool , a framework that projects each tool into a dedicated, loadable set of parameters. By equipping a dynamic integration of these parameterized tools, the LLM can perform tool calling without relying on in-context documents or examples. Specifically, our approach consists of three stages: (1) parametric tool`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29561:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29561:end -->

**当前 Books 投影。** `Applied` 到 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md`；当前正文唯一 marker 已核验，未产生新写回。

### [Mitigating State Aliasing in Vision-Language-Action Models via Inverse Dynamics Learning](https://arxiv.org/html/2605.29577v1)

问题与机制：To mitigate state aliasing, we introduce inverse dynamics learning as an auxiliary objective that directly supervises the VLA vision encoder. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on CALVIN ABC-D and SimplerEnv show consistent gains across diverse VLA baselines.。Method=`arXiv:2605.29577v1 HTML — §3 Method; excerpt=els 2.2 Visual and reasoning supervision in VLA 2.3 Inverse dynamics modeling 3 Method 3.1 Auxiliary inverse dynamics learning 3.2 Pseudo Time Reversal 3.3 Overall pipeline 4 Experiments 4.1 Experimental setup 4.2 CALVIN ABC → \rightarrow D 4.3 SimplerEnv-Bridge 4.4 Frozen vision encoder evaluation 4.5 Analysis 5 Limitations & Future Works 6 Conclusion References A Implementation details A.1 Inverse dynamics head A.2`；Evaluation=`arXiv:2605.29577v1 HTML — §4 Experiments; excerpt=liary inverse dynamics learning 3.2 Pseudo Time Reversal 3.3 Overall pipeline 4 Experiments 4.1 Experimental setup 4.2 CALVIN ABC → \rightarrow D 4.3 SimplerEnv-Bridge 4.4 Frozen vision encoder evaluation 4.5 Analysis 5 Limitations & Future Works 6 Conclusion References A Implementation details A.1 Inverse dynamics head A.2 Probing MLP heads A.3 CALVIN ABC → \rightarrow D implementation details A.3.1 FLOWER A.3.2 VLM`。

Trade-off / failure / fallback：`arXiv:2605.29577v1 HTML — §5 Limitations & Future Works; excerpt=row D 4.3 SimplerEnv-Bridge 4.4 Frozen vision encoder evaluation 4.5 Analysis 5 Limitations & Future Works 6 Conclusion References A Implementation details A.1 Inverse dynamics head A.2 Probing MLP heads A.3 CALVIN ABC → \rightarrow D implementation details A.3.1 FLOWER A.3.2 VLM4VLA A.4 Bridge / SimplerEnv implementation details A.5 LIBERO-90 pretraining A.6 Behavior cloning probe A.7 Proprioceptive state prediction`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29577:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29577:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [World Models in Words: Auditing Physical State-Transition Commitments in Vision-Language Models](https://arxiv.org/html/2605.29585v1)

问题与机制：We introduce \wmw, an evaluation framework for auditing the \emph{language-expressed physical commitments} of VLMs. owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We introduce \wmw, an evaluation framework for auditing the \emph{language-expressed physical commitments} of VLMs.。Method=`arXiv:2605.29585v1 HTML — §Introduction / disclosed mechanism body; excerpt=lausible transition, or merely selected the right option for the wrong reasons. We introduce World Models in Words , an evaluation framework for auditing the language-expressed physical commitments of VLMs. Instead of scoring only I , q ↦ a I,q\mapsto a , we ask models to produce a typed trace I , q ↦ ( s 0 , Δ ​ s , s 1 , a ) I,q\mapsto(s_{0},\Delta s,s_{1},a) : an initial state, a state transition, a resulting stat`；Evaluation=`arXiv:2605.29585v1 HTML — §Physical reasoning benchmarks.; excerpt=Taxonomy 5 WMW-TraceBank 5.1 Construction Quality gates. 5.2 Preference Pairs 6 Experimental Setup 6.1 Models 6.2 Prompting Conditions 6.3 Preference Training 6.4 Human Audit 6.5 Metrics 7 Results RQ1: Answer accuracy hides invalid physical commitments. RQ2: Models fail at different stages. RQ3: The verifier is reliable where it is used quantitatively. RQ4: Verifier-guided selection improves trace quality. 8 Analysis`。

Trade-off / failure / fallback：`arXiv:2605.29585v1 HTML — §4.2 Failure Taxonomy; excerpt=a . Assumptions and abstention. 4 Trace Verification 4.1 Verifier Contract 4.2 Failure Taxonomy 5 WMW-TraceBank 5.1 Construction Quality gates. 5.2 Preference Pairs 6 Experimental Setup 6.1 Models 6.2 Prompting Conditions 6.3 Preference Training 6.4 Human Audit 6.5 Metrics 7 Results RQ1: Answer accuracy hides invalid physical commitments. RQ2: Models fail at different stages. RQ3: The verifier is reliable where it i`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29585:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29585:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的当前正文，采用命题与 prior comparison 未变。

### [Training Deliberative Monitors for Black-Box Scheming Detection](https://arxiv.org/html/2605.29601v1)

问题与机制：In this work, we study action-only deliberative monitors: smaller open-weight models trained to detect scheming and sabotage from agentic trajectories without accessing the monitored agent's reasoning or model internals. owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We show that applying our method to Qwen3.5-27B yields higher performance than all low-cost frontier models as prompted monitors (Gemini 3.1 Flash-Lite, GPT-5.4 Nano, and Claude Haiku 4.5) and than Gemini 2.5 Pro, while also achieving lower marginal inference cost (token-metered USD per 1,000 evaluations).。Method=`arXiv:2605.29601v1 HTML — §3 Method; excerpt=ought fragility. Constitutional black-box monitoring and trained classifiers. 3 Method 3.1 Action-only black-box monitoring 3.2 Scheming specification and deliberative judgments 3.3 Data and deliberative supervision construction 3.4 Training and evaluation protocol Evaluation and metrics. Model choices. 4 Experiments 4.1 Supervised distillation teaches action-only deliberation, RL improves marginally 4.2 Trained moni`；Evaluation=`arXiv:2605.29601v1 HTML — §3.4 Training and evaluation protocol; excerpt=e judgments 3.3 Data and deliberative supervision construction 3.4 Training and evaluation protocol Evaluation and metrics. Model choices. 4 Experiments 4.1 Supervised distillation teaches action-only deliberation, RL improves marginally 4.2 Trained monitors are low-cost Pareto-optimal for low-FPR monitoring 4.3 Broad training mixtures improve OOD transfer, but effects are non-monotonic 4.4 Larger trained monitors wi`。

Trade-off / failure / fallback：`arXiv:2605.29601v1 HTML — §4.6 Failure modes and additional analysis; excerpt=families perform better 4.5 Supervised deliberative data scales effectively 4.6 Failure modes and additional analysis 5 Conclusion, Limitations and Future Work References A Broader Impact B Additional Related Works Detailed scheming and sabotage threat models. AI control, monitor independence, and deployment protocols. Chain-of-thought monitorability and restricted-information monitoring. White-box probes and activat`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29601:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29601:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [VLAConf: Calibrated Task-Success Confidence for Vision-Language-Action Models](https://arxiv.org/html/2605.29605v1)

问题与机制：To address this issue, we propose VLAConf, a two-stage representation-level confidence framework that operates on frozen pretrained VLA representations. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experimental results on the LIBERO benchmark demonstrate that VLAConf improves online task-success confidence estimation over alternative approaches.。Method=`arXiv:2605.29605v1 HTML — §Introduction / disclosed mechanism body; excerpt=sitive decision-making and failure anticipation. Existing confidence estimation methods typically rely on ensemble-based paradigms or action-token probabilities to predict the likelihood of task success. However, they still encounter challenges in computational efficiency and cross-architecture generalizability. These methods usually require repeated sampling, leading to inference inefficiency, and are restricted to`；Evaluation=`arXiv:2605.29605v1 HTML — §V Experiments; excerpt=IV-C Step-Conditioned Anomaly Scoring IV-D Prefix Aggregation and Calibration V Experiments V-A Experimental Setup V-B Main Results V-C Robustness under Shifted LIBERO Suites V-D Real-World Robot Experiments VI Conclusion References A Additional Analyses A-A Prefix-Score Progress Analysis A-B Real-World Calibration Across Task Completion B Full Standard LIBERO Results C Full Perturbation-Level Robustness Results Lice`。

Trade-off / failure / fallback：`arXiv:2605.29605v1 HTML — §II-B Out-of-Distribution and Failure Detection in Robotics; excerpt=II-A Confidence Estimation and Uncertainty in VLAs II-B Out-of-Distribution and Failure Detection in Robotics III Problem Definition IV VLAConf IV-A Overview IV-B Frozen VLA Execution Representation IV-C Step-Conditioned Anomaly Scoring IV-D Prefix Aggregation and Calibration V Experiments V-A Experimental Setup V-B Main Results V-C Robustness under Shifted LIBERO Suites V-D Real-World Robot Experiments VI Conclusion`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29605:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29605:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [Beyond Attack Success Rate: Temporal Logit Observability for LLM Safety Failures](https://arxiv.org/html/2605.29629v1)

问题与机制：By design, this plane is most informative exactly where ASR is least informative: among attacks that succeed for genuinely different reasons. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Safety evaluation should report when and how a failure unfolds, not only whether it occurred.。Method=`arXiv:2605.29629v1 HTML — §Our approach.; excerpt=itative 12-Condition Result Ledger A.2 ASR-Neighboring Motivation B Lexicon and Method Details B.1 Lexicon Specification Refusal Lexicon ( ℒ ref \mathcal{L}_{\text{ref}} , 26 entries). Compliance Lexicon ( ℒ cmp \mathcal{L}_{\text{cmp}} , 21 entries). Implementation details. B.2 Multi-Turn Context Manipulation Protocol B.3 Benign Sample Exclusion Rationale C RP-Plane Calibration and Coarse Annotations C.1 Reference-A`；Evaluation=`arXiv:2605.29629v1 HTML — §Evaluation at the final response.; excerpt=1 Introduction Our approach. What TLO recovers. Contributions. 2 Preliminaries Evaluation at the final response. Decoding setup and access. Logit-Margin Score. 3 Temporal Logit Observability 3.1 Temporal Logit Signal 3.2 Activation Timing Signals 3.3 Relative-Position Calibration What RP measures, by design. Reading the RP plane. 4 Experiments 4.1 Setup 4.2 Q1: RP-Plane Geometry Recovers ASR-Hidden Model–Attack Inte`。

Trade-off / failure / fallback：`arXiv:2605.29629v1 HTML — §Beyond Attack Success Rate: Temporal Logit Observability for LLM Safety Failures; excerpt=Beyond Attack Success Rate: Temporal Logit Observability for LLM Safety Failures Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction Our approach. What TLO recovers. Contributions. 2 Prelim`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29629:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29629:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [RTP-LLM: High-Performance Alibaba LLM Inference Engine](https://arxiv.org/html/2605.29639v1)

问题与机制：We present RTP-LLM, a high-performance inference engine for industrial-scale LLM deployment, successfully deployed across Alibaba Group serving over 100 million users. owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：The results demonstrate RTP-LLM's superior performance against vLLM and SGLang: 4.7x-6.3x model loading speedup, 35-37% TTFT P95 latency reduction with 215% cache reuse improvement in production traffic scheduling, 1.12x-2.48x and 1.86x-2.52x throughput improvements in speculative decoding and multimodal inference, respectively, and 35-40% batch latency reduction with 1.9x-3.0x TTFT improvement in quantized inference。Method=`arXiv:2605.29639v1 HTML — §3. RTP-LLM System Design; excerpt=6 Speculative Decoding Design 6.1 RTP-LLM Speculative Sampling Framework 6.1.1 Architecture Overview 6.1.2 Supported Algorithms 6.2 Prompt Lookup Speculative Sampling 7 Runtime and System Extensions 7.1 Parallel Execution 7.2 Quantization Techniques 7.2.1 Weight-Only Quantization 7.2.2 KV Cache Quantization 7.3 Multimodal Model Support 7.3.1 Supported Multimodal Architectures 7.3.2 Service Deployment 8 Experiments 8`；Evaluation=`arXiv:2605.29639v1 HTML — §8. Experiments; excerpt=del Support 7.3.1 Supported Multimodal Architectures 7.3.2 Service Deployment 8 Experiments 8.1 Traffic Scheduling Strategies Validation 8.2 PD Disaggregation Performance 8.3 Speculative Sampling Performance 8.4 Model Loading Performance 8.5 Quantized Inference Performance 8.6 EPD Disaggregation Performance 9 Conclusions References License: CC BY 4.0 arXiv:2605.29639v1 [cs.OS] 28 May 2026 RTP-LLM: High-Performance Al`。

Trade-off / failure / fallback：`arXiv:2605.29639v1 HTML — §9. Conclusions; excerpt=a significant advancement in the field. However, vLLM and similar systems face limitations in production environments, particularly in their focus on single-node optimization and limited support for heterogeneous hardware environments. Figure 1. RTP-LLM System Architecture The LLM inference process can be decomposed into two distinct phases with different computational characteristics. The Prefill Phase processes th`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29639:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29639:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md` 的当前正文，采用命题与 prior comparison 未变。

### [VikingMem: A Memory Base Management System for Stateful LLM-based Applications](https://arxiv.org/html/2605.29640v1)

问题与机制：To bridge this gap, we introduce the Memory Base, a novel data management paradigm for managing the persistent state of long-term interactions. owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Extensive evaluations on long-term memory benchmarks demonstrate that VikingMem outperformes baselines by up to 30% in memory retrieval effectiveness while maintaining the low latency essential for interactive applications.。Method=`arXiv:2605.29640v1 HTML — §VikingMem : A Memory Base Management System for Stateful LLM-based Applications; excerpt=5 Ablation Studies 5.5.1 Impact of Rerank 5.5.2 Intelligent memory segmentation method 5.5.3 Entity Memory 5.5.4 Keyword Graph 5.6 Operator Usage Frequency Across Real-World Application Scenarios 5.7 Evaluation with F1-Score 6 Related Work 6.1 Retrieve Augment Generation 6.2 Memory-centric Architecture and Systems 7 Conclusion References License: CC BY-NC-SA 4.0 arXiv:2605.29640v1 [cs.AI] 28 May 2026 VikingMem : A Me`；Evaluation=`arXiv:2605.29640v1 HTML — §5. Experimental Evaluation; excerpt=Cases 4.1 Downstream Application Scenarios 4.2 Example Event-Entity Instance 5 Experimental Evaluation 5.1 Experiment Setup 5.1.1 Dataset 5.1.2 LLM Settings 5.1.3 Baselines 5.1.4 Evaluation Metrics 5.1.5 Implementation Details 5.2 End-to-end Evaluation 5.2.1 Effectiveness 5.2.2 Efficiency 5.3 Effect of One-pass Extraction and EUA 5.4 Storage Efficiency and Retention Analysis 5.5 Ablation Studies 5.5.1 Impact of Rera`。

Trade-off / failure / fallback：`arXiv:2605.29640v1 HTML — §7. Conclusion; excerpt=r contradict its own prior corrections. These issues do not primarily stem from limitations in the LLM’s reasoning ability. Instead, they arise because long-term state is often handled in an ad hoc and fragmented manner at the application layer. While an LLM’s context window is transient and bounded, persistent state is frequently spread across logs, shallow caches, and task-specific heuristics rather than maintained`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29640:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29640:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training](https://arxiv.org/html/2605.29664v1)

问题与机制：We propose Asynchronous Multi-Directional Pipeline parallelism (AMDP) to mitigate this issue while sustaining high utilization. owner=`TRAIN-PIPELINE-PARALLEL`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on GPT- and BERT-style models demonstrate that AMDP significantly accelerates training while preserving convergence.。Method=`arXiv:2605.29664v1 HTML — §3 Methodology; excerpt=rt Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work 3 Methodology 3.1 Parameter Mismatch Control 3.2 Multi-Directional Scheduling 3.3 Gradient Accumulation Updates 3.4 Zero Redundancy Optimizer 4 Experiments 4.1 Experimental Setup 4.2 Main Results 4.3 Gradient-Accumulation Threshold Study 4.4 Ablation Study 5 Conclusions References A Implementation Details A.1 Server and System Configuration`；Evaluation=`arXiv:2605.29664v1 HTML — §4 Experiments; excerpt=al Scheduling 3.3 Gradient Accumulation Updates 3.4 Zero Redundancy Optimizer 4 Experiments 4.1 Experimental Setup 4.2 Main Results 4.3 Gradient-Accumulation Threshold Study 4.4 Ablation Study 5 Conclusions References A Implementation Details A.1 Server and System Configuration A.2 Code Modifications A.3 Experiment Workflow B Convergence Analysis of AMDP B.1 Problem Setup and Assumptions General Adaptive Update Rule.`。

Trade-off / failure / fallback：`arXiv:2605.29664v1 HTML — §5 Conclusions; excerpt=ve Update Rule. B.2 Bounded Parameter Mismatch B.3 Near-Synchronous Convergence Discussion. B.4 Invariance of the Mismatch Bound C Experiments C.1 Comparison with recent work License: arXiv.org perpetual non-exclusive license arXiv:2605.29664v1 [cs.DC] 28 May 2026 AMDP: Asynchronous Multi-Directional Pipeline Parallelism for Large-Scale Models Training Ling Chen Affiliation: State Key Laboratory of Blockchain and Dat`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29664:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29664:end -->

**当前 Books 投影。** `Applied` 到 `TRAIN-PIPELINE-PARALLEL` / `books/part-04-training-system/38-pipeline-parallel.md`；当前正文唯一 marker 已核验，未产生新写回。

### [Scaling Laws for Agent Harnesses via Effective Feedback Compute](https://arxiv.org/html/2605.29682v1)

问题与机制：We introduce \emph{Effective Feedback Compute} (EFC), a trace-level scaling coordinate for informative, valid, non-redundant, and retained feedback. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across synthetic, real, held-out, and prospective evaluations, EFC-based coordinates outperform raw-compute baselines and SAS.。Method=`arXiv:2605.29682v1 HTML — §2 Problem Formulation and Experimental Setup; excerpt=ch does not distinguish useful feedback from redundant or unstable interaction. We introduce Effective Feedback Compute (EFC), a trace-level scaling coordinate that credits feedback only when it is informative, valid, non-redundant, and retained for subsequent decisions, and we normalize it by task demand when comparing tasks with different feedback requirements. Across synthetic controllable tasks, executable code t`；Evaluation=`arXiv:2605.29682v1 HTML — §2 Problem Formulation and Experimental Setup; excerpt=Back to Abstract Download PDF Abstract 1 Introduction 2 Problem Formulation and Experimental Setup 2.1 Agent Harnesses as Closed-Loop Computation 2.2 Task Layers 2.3 Harness Families 2.4 Models, Budgets, and Repeated Runs 2.5 Scalar Predictors and Baselines 3 Effective Feedback Compute 3.1 Feedback Events 3.2 Event-Level EFC 3.3 Oracle-EFC and Estimated-EFC 3.4 Task Demand and Normalized EFC 3.5 Scaling Model and Eva`。

Trade-off / failure / fallback：`arXiv:2605.29682v1 HTML — §8 Conclusion; excerpt=and a prospective validation batch, EFC-based coordinates consistently predict failure rates better than raw-compute baselines and a strong multivariate SAS baseline. In controlled scaling, raw tokens and tool calls explain limited variation ( R 2 = 0.33 R^{2}=0.33 and 0.42 0.42 ), SAS reaches 0.88 0.88 , while Oracle-EFC and Estimated-EFC reach 0.94 0.94 and Oracle-EFC/ D task D_{\mathrm{task}} reaches 0.99 0.99 .`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29682:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29682:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding](https://arxiv.org/html/2605.29707v1)

问题与机制：In this paper, we propose Domino, a speculative decoding framework that decouples causal dependency modeling from expensive autoregressive draft execution. owner=`INFER-SPECULATIVE-DECODING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on Qwen3 models show that Domino achieves up to \(5.49\times\) end-to-end speedup under the Transformers backend and up to \(5.8\times\) throughput speedup under SGLang serving.。Method=`arXiv:2605.29707v1 HTML — §4 Methodology; excerpt=lative Decoding and Speedup 3.2 Autoregressive Drafting 3.3 Parallel Drafting 4 Methodology 4.1 Architecture of Domino 4.1.1 Parallel Draft Backbone 4.1.2 Domino Head Causal Encoder. Low-Rank Correction Head. 4.2 Training Teacher-Forced Causal Encoding. Base-anchored curriculum. 4.3 Efficient Runtime Implementation 5 Experiments 5.1 Experimental Setup Models and Evaluations. Training Data. Baselines. Implementation D`；Evaluation=`arXiv:2605.29707v1 HTML — §5 Experiments; excerpt=usal Encoding. Base-anchored curriculum. 4.3 Efficient Runtime Implementation 5 Experiments 5.1 Experimental Setup Models and Evaluations. Training Data. Baselines. Implementation Details. 5.2 Main Results Low-concurrency case. High-concurrency case. 5.3 Ablation 5.3.1 Training Data 5.3.2 Training Strategy 5.3.3 Effect of Domino Head 6 Conclusion 7 Limitations References A Appendix A.1 Training Details License: CC BY`。

Trade-off / failure / fallback：`arXiv:2605.29707v1 HTML — §6 Conclusion; excerpt=raining Data 5.3.2 Training Strategy 5.3.3 Effect of Domino Head 6 Conclusion 7 Limitations References A Appendix A.1 Training Details License: CC BY 4.0 arXiv:2605.29707v1 [cs.CL] 28 May 2026 Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding Jianuo Huang 1,2* Yaojie Zhang 1,3* Qituan Zhang 4 Hao Lin 2 Hanlin Xu 5 Linfeng Zhang 1† 1 EPIC Lab, Shanghai Jiao Tong University 2 Schoo`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29707:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29707:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-SPECULATIVE-DECODING` / `books/part-05-inference-system/48-speculative-decoding.md` 的当前正文，采用命题与 prior comparison 未变。

### [RASET: Router-Agnostic Safety-Critical Expert Tuning Exposes Localized Safety Enforcement Failures in Mixture-of-Experts LLMs](https://arxiv.org/html/2605.29708v1)

问题与机制：Motivated by this observation, we present RASET (Router-Agnostic Safety-Critical Expert Tuning), a red-teaming framework that probes safety enforcement that is localized in a small subset of experts while preserving the model's intrinsic routing behavior. owner=`MODEL-MOE`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：These results reveal a distinct MoE safety risk, highlighting the need for expert-aware alignment mechanisms.。Method=`arXiv:2605.29708v1 HTML — §3 Methodology; excerpt=Download PDF Abstract 1 Introduction 2 Related Work Mixture-of-Experts LLMs. 3 Methodology 3.1 Notation 3.2 Contrastive Activation Analysis 3.3 Constrained Expert-Level Adaptation Refusal Pattern Statistics. Per-token NLL Definition. Controlled Safety-boundary Violation. Preserve General Capabilities. 4 Evaluation 4.1 Experimental Setup Target Models. Baselines. Datasets. Metrics. Implementation Details. 4.2 Compreh`；Evaluation=`arXiv:2605.29708v1 HTML — §3.2 Contrastive Activation Analysis; excerpt=inition. Controlled Safety-boundary Violation. Preserve General Capabilities. 4 Evaluation 4.1 Experimental Setup Target Models. Baselines. Datasets. Metrics. Implementation Details. 4.2 Comprehensive Performance Assessment 4.3 Impact on General Capabilities 4.4 Verification of RASET ’s Routing Preservation 5 Conclusion References A Empirical Motivation Details A.1 Routing Metrics A.2 Probe I: Teacher-forced Refusal`。

Trade-off / failure / fallback：`arXiv:2605.29708v1 HTML — §5 Conclusion; excerpt=oss five open-weight MoE backbones, RASET exposes a consistent localized safety failure mode. It achieves the highest red-teaming yield under all strictness levels, reaching 50.5 % 50.5\% average ASR hq under the most stringent quality-qualified criterion and outperforming the strongest baseline by 37.6 37.6 points on average. At the same time, it updates only 0.12 % 0.12\% – 0.95 % 0.95\% of model parameters and pre`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29708:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29708:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MODEL-MOE` / `books/part-02-model/21-moe.md` 的当前正文，采用命题与 prior comparison 未变。

### [Bastion: Budget-Aware Speculative Decoding with Tree-structured Block Diffusion Drafting](https://arxiv.org/html/2605.29727v1)

问题与机制：To address this, we propose BASTION, a budget-aware speculative decoding framework with tree-based diffusion drafting. owner=`INFER-SPECULATIVE-DECODING`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across diverse benchmarks and GPU architectures, BASTION achieves up to a 6.61x speedup over standard autoregressive decoding, outperforming state-of-the-art block-diffusion baselines by 39%.。Method=`arXiv:2605.29727v1 HTML — §Algorithm variants.; excerpt=ften fails to capture the target model’s preferred trajectory. To address this, we propose Bastion , a b udget- a ware s peculative decoding framework with t ree-based diffus ion drafting. Unlike existing methods that rely on static tree topologies, Bastion dynamically constructs query-dependent trees by balancing draft quality against hardware constraints. Our framework integrates three synergistic components: (1) a`；Evaluation=`arXiv:2605.29727v1 HTML — §Efficiency analysis.; excerpt=uction via Best-First Expansion 3.4 Online Controller for Budget Optimization 4 Experiments 4.1 Experimental Settings 4.2 Main Results End-to-end speedup. Average acceptance length. Generalization across GPUs and model families. 4.3 Tree Expansion Comparison Tree topology comparison. Best-first expansion outperforms beam search under matched budgets. 5 Analysis 5.1 Fixed vs. Adaptive Budget Policies Fixed-budget tree`。

Trade-off / failure / fallback：`arXiv:2605.29727v1 HTML — §6 Conclusion; excerpt=tic is the most robust default; EMA alone is fragile. 6 Conclusion References A Limitations B Related Works Block diffusion drafter for speculative decoding. Tree-based speculative decoding. Adaptive draft tree structure. C Mathematical Proofs C.1 Proofs of Lemma and Proposition C.2 Proof of Proposition C.3 Proof of Proposition D Algorithm E Overall Pipeline Drafting. Linearization and verification mask. Acceptance.`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29727:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29727:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-SPECULATIVE-DECODING` / `books/part-05-inference-system/48-speculative-decoding.md` 的当前正文，采用命题与 prior comparison 未变。

### [From Roofline to Ruggedness: Decomposing and Smoothing the GEMM Performance Landscape](https://arxiv.org/html/2605.29752v1)

问题与机制：Adjacent GEMM problems that differ by a single 128-element step in N can show 30% different throughput. owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Adjacent GEMM problems that differ by a single 128-element step in N can show 30% different throughput.。Method=`arXiv:2605.29752v1 HTML — §1.4 Generality of the framework; excerpt=ition, yet dominant for every non-peak workload - is the subject of this paper. We propose performance ruggedness analysis as an analytical framework complementary to roofline: rather than summarizing GPU performance with a scalar bound, treat the full multidimensional performance surface as the object of study, decomposes its texture into mechanism-attributable components, and separates software-removable losses fro`；Evaluation=`arXiv:2605.29752v1 HTML — §5 Memory Subsystem Analysis; excerpt=amic-Programming based Padding and Splitting 7.1 The T0 → T1 → T2 Algorithm 7.2 Results on Fixed Tile (256 × 256; 32,768 Configurations) 7.3 What Does the DP Choose? 7.4 Results on the Dynamic-Tile Landscape 7.5 The Combined Optimization Stack 8 Mechanism Refinement: Four Targeted Experiments 8.1 Independent Measurement on Hand-Picked Configurations 8.2 Per-Configuration Timing Variance 8.3 Cross-Tile Fine-N Sweep: T`。

Trade-off / failure / fallback：`arXiv:2605.29752v1 HTML — §11 Conclusions; excerpt=From Roofline to Ruggedness: Decomposing and Smoothing the GEMM Performance Landscape Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 1.1 The Roofline Hides a Surface 1.2 Performance Landscape`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29752:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29752:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md` 的当前正文，采用命题与 prior comparison 未变。

### [Croissant Tasks: A Metadata Format for Reproducible Machine Learning Evaluations](https://arxiv.org/html/2605.29786v1)

问题与机制：To address this, we introduce Croissant Tasks: a declarative, machine-actionable metadata format that abstracts low-level implementation details into high-level specifications. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We envision this format as a new foundation for automated and conceptual reproducibility in machine learning.。Method=`arXiv:2605.29786v1 HTML — §Introduction / disclosed mechanism body; excerpt=oven, The Netherlands Abstract Reproducibility is fundamental to the scientific method, yet remains a critical challenge in machine learning. Contributing factors include underspecified execution details and brittle software environments. Human-centric remedies, such as checklists and manual verification, help but require intensive effort and fail to scale. To address this, we introduce Croissant Tasks : a declarativ`；Evaluation=`arXiv:2605.29786v1 HTML — §Croissant Tasks: A Metadata Format for Reproducible Machine Learning Evaluations; excerpt=Croissant Tasks: A Metadata Format for Reproducible Machine Learning Evaluations Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work Technical replication vs. conceptual r`。

Trade-off / failure / fallback：`arXiv:2605.29786v1 HTML — §5 Discussion and Future Work; excerpt=Croissant Tasks Files 4.2 Agentic Code Generation for Automated Reproduction 5 Discussion and Future Work 5.1 Other Benefits of Croissant Tasks Interoperability. Evolution and Reuse. Discoverability. 5.2 Limitations and Challenges Adoption and Ease of Use. Fidelity and Quality of Metadata. Generalization and the Vision of Reproducible Science. 6 Conclusion References A Croissant Tasks Turtle Schema B Skill File and`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29786:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29786:end -->

**当前 Books 投影。** `Applied` 到 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；当前正文唯一 marker 已核验，未产生新写回。

### [Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems](https://arxiv.org/html/2605.29790v1)

问题与机制：However, in real-world tasks, MAS often exhibit various failures during execution and such failures are difficult to eliminate during design. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across six long-horizon agent benchmarks, Meta-Team consistently outperforms single-agent systems, hand-crafted MAS, and prior MAS evolution methods; further analyses demonstrate that Meta-Team enables more reliable and scalable MAS self-evolution.。Method=`arXiv:2605.29790v1 HTML — §Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems; excerpt=2 Preliminaries 2.1 LLM-based MAS 2.2 Experience-Driven Self-Evolution of MAS 3 Method 3.1 Collaborative Scheme for MAS Self-Evolution Empirical validation. Discussion. 3.2 Meta-Team: Multi-Scale Collaborative Self-Evolution Agent-Level Evolution (L1). Interaction-Level Evolution (L2). Team-Level Evolution (L3). 4 Experiments and Results 4.1 Experimental Setup Benchmarks. Baselines. Evolution and Evaluation Setup. 4.`；Evaluation=`arXiv:2605.29790v1 HTML — §4 Experiments and Results; excerpt=Evolution (L1). Interaction-Level Evolution (L2). Team-Level Evolution (L3). 4 Experiments and Results 4.1 Experimental Setup Benchmarks. Baselines. Evolution and Evaluation Setup. 4.2 Main Results 4.3 Ablation Study 4.4 Scalability and Generalization of Meta-Team 4.5 Evolution under Constrained Budget 5 Related Work 5.1 LLM-based Multi-Agent Systems 5.2 Automated MAS Generation and Evolution 6 Conclusion References`。

Trade-off / failure / fallback：`arXiv:2605.29790v1 HTML — §Discussion.; excerpt=3 Method 3.1 Collaborative Scheme for MAS Self-Evolution Empirical validation. Discussion. 3.2 Meta-Team: Multi-Scale Collaborative Self-Evolution Agent-Level Evolution (L1). Interaction-Level Evolution (L2). Team-Level Evolution (L3). 4 Experiments and Results 4.1 Experimental Setup Benchmarks. Baselines. Evolution and Evaluation Setup. 4.2 Main Results 4.3 Ablation Study 4.4 Scalability and Generalization of Meta-`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29790:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29790:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [HARP: Hadamard-Preconditioned Adaptive Rotation Processor for Extreme LLM Quantization](https://arxiv.org/html/2605.29843v1)

问题与机制：We introduce HARP (Hadamard-preconditioned Adaptive Rotation Processor), a learnable structured two-sided orthogonal processor that replaces fixed Hadamard mixing while preserving exact full-precision equivalence. owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Importantly, HARP preserves deployment efficiency, reaching 128 tok/s versus 61 tok/s for FP16.。Method=`arXiv:2605.29843v1 HTML — §Methods compared.; excerpt=nts Scope of comparison. Models. No-finetuning comparison. Evaluation protocol. Methods compared. Effective bitrate accounting. 4.1 Language modeling perplexity Kronecker fallback and parameter storage. 4.2 Zero-shot evaluation 4.3 Inference latency and storage 4.4 Backend portability: QTIP 4.5 Comparison with Published Baselines 5 Related Work 5.1 Post-Training Quantization of LLMs Heavy-Tailed Statistics and Outlie`；Evaluation=`arXiv:2605.29843v1 HTML — §4 Experiments; excerpt=2 Parameter quantization for deployment 3.5.3 Fitting HARP processors for PTQ 4 Experiments Scope of comparison. Models. No-finetuning comparison. Evaluation protocol. Methods compared. Effective bitrate accounting. 4.1 Language modeling perplexity Kronecker fallback and parameter storage. 4.2 Zero-shot evaluation 4.3 Inference latency and storage 4.4 Backend portability: QTIP 4.5 Comparison with Published Baselines`。

Trade-off / failure / fallback：`arXiv:2605.29843v1 HTML — §6 Conclusion; excerpt=k We organize related work into three parts: post-training quantization and its failure modes, transform-based reparameterizations, and structured orthogonal transforms for quantization. 5.1 Post-Training Quantization of LLMs Heavy-Tailed Statistics and Outlier Channels. Extreme low-bit quantization is dominated by heavy-tailed weight distributions and a small number of high-magnitude outlier channels that inflate pe`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29843:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29843:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md` 的当前正文，采用命题与 prior comparison 未变。

### [Moment-KV: Momentum-Based Decode-Time KV Cache Compression for Long Generation](https://arxiv.org/html/2605.29873v1)

问题与机制：We propose Moment-KV, a decoding-time KV cache compression method based on momentum-driven temporal attention aggregation. owner=`INFER-KV-CACHE`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments show that Moment-KV significantly improves generation fidelity in long-generation tasks (2.3-3.2 %) while maintaining decoding latency.。Method=`arXiv:2605.29873v1 HTML — §4 Methodology; excerpt=bservations 3.1 Temporal Nature of Attention 3.2 Curse of Fixed Recent Window 4 Methodology 4.1 KV Cache Preliminaries 4.2 Moment-KV Prefill pool Φ p \Phi^{p} (frozen): Decoding pool Φ d \Phi^{d} (compressed): 5 Experiments 5.1 Benchmarks 5.2 Baselines 5.3 Implementation Details 6 Results and Discussions 6.1 Results on LongGenBench 6.2 Results on HelloBench 6.3 Integration of Moment-KV with Prefill Compression Techni`；Evaluation=`arXiv:2605.29873v1 HTML — §5 Experiments; excerpt=Prefill pool Φ p \Phi^{p} (frozen): Decoding pool Φ d \Phi^{d} (compressed): 5 Experiments 5.1 Benchmarks 5.2 Baselines 5.3 Implementation Details 6 Results and Discussions 6.1 Results on LongGenBench 6.2 Results on HelloBench 6.3 Integration of Moment-KV with Prefill Compression Techniques 7 Analysis 7.1 Mitigating the Curse of Fixed Recent Window 7.2 Enhanced Long-Horizon Stability 7.3 Sensitivity of Momentum Fact`。

Trade-off / failure / fallback：`arXiv:2605.29873v1 HTML — §6 Results and Discussions; excerpt=periments 5.1 Benchmarks 5.2 Baselines 5.3 Implementation Details 6 Results and Discussions 6.1 Results on LongGenBench 6.2 Results on HelloBench 6.3 Integration of Moment-KV with Prefill Compression Techniques 7 Analysis 7.1 Mitigating the Curse of Fixed Recent Window 7.2 Enhanced Long-Horizon Stability 7.3 Sensitivity of Momentum Factor α \alpha 7.4 Throughput Analysis 7.5 Generalization of Moment-KV 8 Conclusion R`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29873:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29873:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-KV-CACHE` / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的当前正文，采用命题与 prior comparison 未变。

### [LaRA: Layer-wise Representation Analysis for Detecting Data Contamination in RL Post-Training](https://arxiv.org/html/2605.29888v1)

问题与机制：We propose LaRA, a layer-wise representation analysis framework for detecting contamination in RL post-trained LLMs. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：However, there has been little exploration on the problem of data contamination in RL post-training, potentially undermining generalization and evaluation reliability of the training process itself.。Method=`arXiv:2605.29888v1 HTML — §Appendix A Algorithm; excerpt=n and evaluation reliability of the training process itself. Existing detection methods primarily rely on output-level signals such as likelihood or entropy, which become unreliable for RL-trained models since RL shapes behavior through trajectory-level rewards rather than token likelihoods. We propose LaRA, a layer-wise representation analysis framework for detecting contamination in RL post-trained LLMs. LaRA intro`；Evaluation=`arXiv:2605.29888v1 HTML — §LaRA: Layer-wise Representation Analysis for Detecting Data Contamination in RL Post-Training; excerpt=tion Analysis to Detect RL Contamination 3.1 Contamination Dataset Construction Evaluation set. Training set. 3.2 Three Metrics for Analysis Metric 1: Representation Shift Magnitude. Metric 2: Directional Collapse. Metric 3: Representation Stability Index. 3.3 Layer-wise Analysis with Three Metrics 4 Contamination Detection Protocol Step 1: Clean-reference Robust Standardization. Step 2: Metric-specific Anomaly Align`。

Trade-off / failure / fallback：`arXiv:2605.29888v1 HTML — §6 Conclusion; excerpt=, entropy-based detection ( Tao et al., 2025 ) . Consequently, they inherit the limitations above, often compounded by exploration dynamics. Representation Dynamics in LLMs. Recent work has increasingly leveraged representation dynamics in LLMs to study behaviors beyond outputs ( Kang et al., 2025 ; Lee et al., 2025 ; Gwak et al., 2025 ; Zhao et al., 2025 ) . One line of work analyzes internal states and their evolut`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29888:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29888:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Uncertainty Quantification for Multimodal Retrieval Augmented Generation](https://arxiv.org/html/2605.29956v1)

问题与机制：In this work, we show that modeling uncertainty using multimodal and retrieval-aware probability signals improves estimation in multimodal RAG systems. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：In this work, we show that modeling uncertainty using multimodal and retrieval-aware probability signals improves estimation in multimodal RAG systems.。Method=`arXiv:2605.29956v1 HTML — §4. Methodology; excerpt=Abstract Download PDF Abstract. 1 Introduction 2 Related Work 3 Preliminaries 4 Methodology 4.1 Problem Formulation 4.2 LeMUQ: Learnable Multimodal Uncertainty Quantification 5 Experimental Setup 6 Results 6.1 LeMUQ Performance 6.2 Out-of-Domain Generalizability 6.3 Impact of Probability Components 7 Conclusions and Future Work Acknowledgements References A Prompt Details License: arXiv.org perpetual non-exclusive li`；Evaluation=`arXiv:2605.29956v1 HTML — §5. Experimental Setup; excerpt=roblem Formulation 4.2 LeMUQ: Learnable Multimodal Uncertainty Quantification 5 Experimental Setup 6 Results 6.1 LeMUQ Performance 6.2 Out-of-Domain Generalizability 6.3 Impact of Probability Components 7 Conclusions and Future Work Acknowledgements References A Prompt Details License: arXiv.org perpetual non-exclusive license arXiv:2605.29956v1 [cs.IR] 28 May 2026 Uncertainty Quantification for Multimodal Retrieval`。

Trade-off / failure / fallback：`arXiv:2605.29956v1 HTML — §7. Conclusions and Future Work; excerpt=rly when the underlying data distribution shifts ( Ovadia et al., 2019 ) . This limitation arises because such models tend to overfit to the specific characteristics of the training distribution, which leads to decreased performance on different validation and test distributions. To examine the generalizability of our method, we evaluate LeMUQ under out-of-distribution settings across three dimensions: varying the re`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29956:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29956:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction](https://arxiv.org/html/2605.29960v1)

问题与机制：In this paper, we propose MemPoison, a novel memory poisoning attack that bypasses selective memory mechanisms in LLM agents, where an attacker can inject triggerable backdoors into the agent's long-term memory through dialogue interactions, thereby misleading its subsequent responses. owner=`PLATFORM-SECURITY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Evaluations across different agent domains and memory mechanisms show MemPoison achieves attack success rates up to 0.95, outperforming existing baselines.。Method=`arXiv:2605.29960v1 HTML — §4. Method; excerpt=oad PDF Abstract. 1 Introduction 2 Background and Related Work 3 Threat Model 4 Method 4.1 Overview 4.2 Multi-objective Optimization Problem 4.3 Optimization algorithm 5 Experiments 5.1 Experimental Settings 5.2 Main Results (RQ1) 5.3 Ablation and Sensitivity Analyses (RQ2) 5.3.1 Impact of Methodological Components 5.3.2 Impact of Memory Mechanism Configurations 5.4 Potential Defenses (RQ3) 5.5 Real-World Case Study`；Evaluation=`arXiv:2605.29960v1 HTML — §5. Experiments; excerpt=Overview 4.2 Multi-objective Optimization Problem 4.3 Optimization algorithm 5 Experiments 5.1 Experimental Settings 5.2 Main Results (RQ1) 5.3 Ablation and Sensitivity Analyses (RQ2) 5.3.1 Impact of Methodological Components 5.3.2 Impact of Memory Mechanism Configurations 5.4 Potential Defenses (RQ3) 5.5 Real-World Case Study (RQ4) 5.6 Mechanistic Analysis (RQ5) 5.6.1 Trigger-Induced Self-Attention Redistribution 5`。

Trade-off / failure / fallback：`arXiv:2605.29960v1 HTML — §3. Threat Model; excerpt=ace Geometry Analysis 5.6.3 Geometric Vulnerabilities Across Embedding Models 6 Discussion and Limitations 7 Conclusion References A Pilot Study A.1 Dataset A.2 Experimental Details A.3 Results B Method Details B.1 Semantic Relational Bridge Prompt B.2 Trigger Initialization B.3 Optimization and Implementation Details C Experimental Details C.1 Datasets and Usage C.2 Memory Mechanism Details C.2.1 A-Mem C.2.2 LangMem`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29960:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29960:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md` 的当前正文，采用命题与 prior comparison 未变。

### [Fingerprinting Inference Systems of Large Language Models](https://arxiv.org/html/2605.29979v1)

问题与机制：In this paper, we show that these deviations are characteristic of specific components and propagate to observable textual outputs, exposing the inference system to any party that can query the model. owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：In this paper, we show that these deviations are characteristic of specific components and propagate to observable textual outputs, exposing the inference system to any party that can query the model.。Method=`arXiv:2605.29979v1 HTML — §Fingerprinting Inference Systems of Large Language Models; excerpt=nce system to any party that can query the model. Building on this observation, we introduce a fingerprinting method that analyzes the prompt-response behavior of LLMs to identify components of the inference system. Our empirical evaluation demonstrates that the inference engine, attention backend, and underlying hardware platform can be identified reliably, even when the LLM is operated at non-zero temperature. We s`；Evaluation=`arXiv:2605.29979v1 HTML — §4 Evaluation; excerpt=ngs and Classification Training. Fingerprinting. 3.3 Practical Considerations 4 Evaluation Inference systems and models. Fingerprinting setup. 4.1 Fingerprinting Systems with Deterministic Decoding 4.2 Fingerprinting Systems with Stochastic Decoding 5 Analysis Application-specific system prompt. Batch size generalization. Proprietary system components. Temperature generalization. 6 Related Work Numerical deviations i`。

Trade-off / failure / fallback：`arXiv:2605.29979v1 HTML — §Threat model.; excerpt=rical deviations in machine learning. Side-channel attacks using LLM outputs. 7 Discussion Mitigations. Limitations. 8 Conclusion References A Societal Impact B Technical Setup C Application-Specific System Prompts License: CC BY 4.0 arXiv:2605.29979v1 [cs.CR] 28 May 2026 Fingerprinting Inference Systems of Large Language Models Anna Wimbauer Affiliation: BIFOLD & TU Berlin Jonas Möller Affiliation: BIFOLD & TU Berli`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-29979:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-29979:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md` 的当前正文，采用命题与 prior comparison 未变。

### [VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies](https://arxiv.org/html/2605.30011v1)

问题与机制：We present VISUALTHINK-VLA, a visual intermediate-reasoning framework for accurate, low-latency VLA policies. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across multiple benchmarks and real-robot evaluation, VISUALTHINK-VLA achieves the highest success rate on most benchmarks while reducing the multi-second latency of reasoning-augmented baselines to the sub-second regime.。Method=`arXiv:2605.30011v1 HTML — §3 Method; excerpt=rt Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work 3 Method 3.1 Method Overview 3.2 Channel Evidence Interface 3.3 Task-Adaptive Orchestration 3.4 Visual State Composer 3.5 Training the Routed Interface 4 VisualEvidence-Kit 4.1 VisualEvidence-Agent 4.2 VisualEvidence-Set 5 Experimental Setup 6 Results and Analysis 7 Ablation Studies 8 Conclusion 9 Limitations A VisualEvidence-Kit Workflow E`；Evaluation=`arXiv:2605.30011v1 HTML — §5 Experimental Setup; excerpt=nterface 4 VisualEvidence-Kit 4.1 VisualEvidence-Agent 4.2 VisualEvidence-Set 5 Experimental Setup 6 Results and Analysis 7 Ablation Studies 8 Conclusion 9 Limitations A VisualEvidence-Kit Workflow Evidence-channel construction. B Real-Robot Task Suite C Qualitative Case Studies D VisualEvidence-Kit Audit and Faithfulness Details E Human Review Protocol F Artifact Licenses G AI Assistant Use References License: arXiv`。

Trade-off / failure / fallback：`arXiv:2605.30011v1 HTML — §8 Conclusion; excerpt=t 5 Experimental Setup 6 Results and Analysis 7 Ablation Studies 8 Conclusion 9 Limitations A VisualEvidence-Kit Workflow Evidence-channel construction. B Real-Robot Task Suite C Qualitative Case Studies D VisualEvidence-Kit Audit and Faithfulness Details E Human Review Protocol F Artifact Licenses G AI Assistant Use References License: arXiv.org perpetual non-exclusive license arXiv:2605.30011v1 [cs.CV] 28 May 2026`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30011:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30011:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [Token Inflation: How Dishonest Providers Can Overcharge for Large Language Model Usage](https://arxiv.org/html/2605.30040v1)

问题与机制：We show that this kind of billing is hard to audit by design: providers hide the model, the tokenizer, and the execution to protect their IP, mitigate jailbreaks, and preserve user privacy, which means an auditor can only inspect proofs the provider supplies. owner=`PLATFORM-COST`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We show that this kind of billing is hard to audit by design: providers hide the model, the tokenizer, and the execution to protect their IP, mitigate jailbreaks, and preserve user privacy, which means an auditor can only inspect proofs the provider supplies.。Method=`arXiv:2605.30040v1 HTML — §3.1 Auditing Framework Overview and the Easy-to-Violate Assumptions; excerpt=for neural text processing . In Proceedings of the 2018 conference on empirical methods in natural language processing: System demonstrations , pp. 66–71 . Cited by: §2 , §5.1 . Kuo et al. (2025) M. Kuo, J. Zhang, A. Ding, Q. Wang, L. DiValentin, Y. Bao, W. Wei, H. Li, and Y. Chen H-cot: hijacking the chain-of-thought safety reasoning mechanism to jailbreak large reasoning models, including openai o1/o3, deepseek-r1,`；Evaluation=`arXiv:2605.30040v1 HTML — §Evaluation setup.; excerpt=mation disadvantage. Easy-to-violate assumptions. 3.2 Simple Attack Breaks CoIn Evaluation setup. Canonical attack chain. 3.3 Other Attack Variants and Discussion Discussion. 4 Predicting Hidden Token Counts via Reasoning Length Estimation 4.1 Auditing Framework Overview and Easy-to-Violate Assumptions PALACE inherits a deeper trust gap. Easy-to-violate assumptions. Experimental setup. 4.2 Breaking PALACE’s Two Assum`。

Trade-off / failure / fallback：`arXiv:2605.30040v1 HTML — §2 Background and Threat Model; excerpt=ks CoIn Evaluation setup. Canonical attack chain. 3.3 Other Attack Variants and Discussion Discussion. 4 Predicting Hidden Token Counts via Reasoning Length Estimation 4.1 Auditing Framework Overview and Easy-to-Violate Assumptions PALACE inherits a deeper trust gap. Easy-to-violate assumptions. Experimental setup. 4.2 Breaking PALACE’s Two Assumptions Breaking Assumption 1: Steering the Auditor at Inference Time. Br`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30040:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30040:end -->

**当前 Books 投影。** `Applied` 到 `PLATFORM-COST` / `books/part-06-ai-infrastructure/70-cost.md`；当前正文唯一 marker 已核验，未产生新写回。

### [REPOT: Recoverable Program-of-Thought via Checkpoint Repair](https://arxiv.org/html/2605.30052v1)

问题与机制：We introduce RePoT (Recoverable PoT): a deterministic verified replay that walks the plan through the environment to its first invalid transition, then one LLM call that resumes from the verified prefix. owner=`AGENT-WORKFLOW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：On Derail-550, our controlled recovery benchmark, every condition with access to checkpoint information clears >=30% on GPT-medium and >=70% on Gemini, vs <=3.1% for error-only feedback -- showing that checkpoint information, not the specific verified-prefix tail, is the load-bearing recovery signal.。Method=`arXiv:2605.30052v1 HTML — §4 Method; excerpt=ork on one-shot brittleness. Process verification and rewards. 3 Related Work 4 Method 4.1 Problem setting 4.2 Verified replay 4.3 RePoT algorithm A simple recovery model. 4.4 Adaptive recovery policy 4.5 Repair prompt and ablations 5 Experimental Setup 5.1 Benchmarks PuzzleZoo -775. PlanBench Blocksworld (378 problems). Derail -550 (550 errors × \times 11 conditions). 5.2 Models 5.3 Methods compared 6 Results 6.1 He`；Evaluation=`arXiv:2605.30052v1 HTML — §4.5 Repair prompt and ablations; excerpt=recovery model. 4.4 Adaptive recovery policy 4.5 Repair prompt and ablations 5 Experimental Setup 5.1 Benchmarks PuzzleZoo -775. PlanBench Blocksworld (378 problems). Derail -550 (550 errors × \times 11 conditions). 5.2 Models 5.3 Methods compared 6 Results 6.1 Headline cross-model accuracy 6.2 Per-environment breakdown 6.3 External replication: PlanBench Blocksworld Limitation: matched-budget control. Multi-seed va`。

Trade-off / failure / fallback：`arXiv:2605.30052v1 HTML — §Limitation: matched-budget control.; excerpt=y 6.2 Per-environment breakdown 6.3 External replication: PlanBench Blocksworld Limitation: matched-budget control. Multi-seed variance. 6.4 Open-source replication and capability scaling 7 Mechanism Analysis 7.1 Checkpoint information is the load-bearing signal Cost. Failure modes. 8 Discussion When RePoT helps and when it does not. Future work. 9 Conclusion Verifier-required scope. Single-call repair budget. Within`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30052:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30052:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md` 的当前正文，采用命题与 prior comparison 未变。

### [A Predictive Law for On-Policy Self-Distillation From World Feedback](https://arxiv.org/html/2605.30070v1)

问题与机制：Interestingly, we show that this linear predictability holds with model scale, suggesting a potential basis for new empirical scaling laws on larger models with stronger in-context learning capabilities. owner=`TRAIN-GRPO`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Interestingly, we show that this linear predictability holds with model scale, suggesting a potential basis for new empirical scaling laws on larger models with stronger in-context learning capabilities.。Method=`arXiv:2605.30070v1 HTML — §Problem formulation.; excerpt=racy improvements. 3.2 The predictive law holds with model size. 4 Discussion 5 Methodology Self-Teacher Construction Configurations. Models, Training, and Evaluation. 6 Related Work RL with LLMs. On-policy distillation. On-policy self-distillation. References A Experimental Details Computational Resources. License: arXiv.org perpetual non-exclusive license arXiv:2605.30070v1 [cs.LG] 28 May 2026 Tufa Labs August 24,`；Evaluation=`arXiv:2605.30070v1 HTML — §3 Experiments; excerpt=to Abstract Download PDF 1 Introduction 2 Preliminaries Problem formulation. 3 Experiments 3.1 Initial student–self-teacher gap predicts final student accuracy improvements. 3.2 The predictive law holds with model size. 4 Discussion 5 Methodology Self-Teacher Construction Configurations. Models, Training, and Evaluation. 6 Related Work RL with LLMs. On-policy distillation. On-policy self-distillation. References A E`。

Trade-off / failure / fallback：`arXiv:2605.30070v1 HTML — §4 Discussion; excerpt=student accuracy improvements. 3.2 The predictive law holds with model size. 4 Discussion 5 Methodology Self-Teacher Construction Configurations. Models, Training, and Evaluation. 6 Related Work RL with LLMs. On-policy distillation. On-policy self-distillation. References A Experimental Details Computational Resources. License: arXiv.org perpetual non-exclusive license arXiv:2605.30070v1 [cs.LG] 28 May 2026 Tufa Lab`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30070:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30070:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md` 的当前正文，采用命题与 prior comparison 未变。

### [Future Forcing: Future-aware Training-free KV Cache Policy for Autoregressive Video Generation](https://arxiv.org/html/2605.30083v1)

问题与机制：Building on this insight, we propose Future Forcing, a training-free future-aware KV cache policy for AR video generation. owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Extensive experiments show that Future Forcing improves long-horizon consistency under limited KV caches, achieving up to 1.49 improvement in subject consistency on VBench-Long for 60s generation over existing AR video KV cache policies.。Method=`arXiv:2605.30083v1 HTML — §4 Method; excerpt=Motivation : Pre-RoPE Query Distribution Stability Across AR Video Generation 4 Method 4.1 Future-aware KV Cache Eviction Module 4.2 Future-aware KV Cache Merging Module 5 Experiment 5.1 Experimental Settings 5.2 Generation Quality Study 5.3 Ablation Study 5.4 Efficiency and Peak GPU Memory Usage Study 5.5 Visualization 6 Conclusion References A Proof B Custom Kernel Design Algorithm. Implementation Details. C Additi`；Evaluation=`arXiv:2605.30083v1 HTML — §3 Motivation and Analysis; excerpt=uture-aware KV Cache Eviction Module 4.2 Future-aware KV Cache Merging Module 5 Experiment 5.1 Experimental Settings 5.2 Generation Quality Study 5.3 Ablation Study 5.4 Efficiency and Peak GPU Memory Usage Study 5.5 Visualization 6 Conclusion References A Proof B Custom Kernel Design Algorithm. Implementation Details. C Additional Experiment Results C.1 Additional Query Distribution Analysis Results. C.2 Additional A`。

Trade-off / failure / fallback：`arXiv:2605.30083v1 HTML — §6 Conclusion; excerpt=Analysis Results. C.7 Difference to PaFu-KV D Experiments Compute Resources. E Limitations F Additional Visualization Results. G Quantitative Analysis of Pre-RoPE Query Stability H Pre-RoPE Stability under Highly Dynamic Scenarios License: CC BY 4.0 arXiv:2605.30083v1 [cs.CV] 28 May 2026 Future Forcing: Future-aware Training-free KV Cache Policy for Autoregressive Video Generation Jiayi Luo Qiyan Liu Tengyang Wang J`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30083:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30083:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的当前正文，采用命题与 prior comparison 未变。

### [Conformal Certification of Reasoning Trace Prefixes](https://arxiv.org/html/2605.30085v1)

问题与机制：To address this, we introduce CROP (Conformal Reasoning Output Prefixes), a verifier-agnostic calibration procedure for clean-prefix certification. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across six process-labeled reasoning datasets, we demonstrate that standard step-level metrics such as AUROC do not fully capture prefix utility, suggesting verifiers should instead be evaluated by certified prefix length.。Method=`arXiv:2605.30085v1 HTML — §4 Method; excerpt=iction in LMs. 3 Problem Setup Setup. Step-Level Risk Proxy. Exchangeability. 4 Method 4.1 Risk Control Primitive 4.2 CROP Loss and Calibration Rule 4.3 CROP Algorithm 5 Experiments Risk Proxy Sources. Evaluation Metrics. Datasets. 5.1 Prefix Utility at Varying Risks 5.2 Prefix Utility vs. AUROC 5.3 Boundary Quality of the Retained Prefix 5.4 Certified Prefixes for Downstream Repair 6 Discussion PRM gains extend beyo`；Evaluation=`arXiv:2605.30085v1 HTML — §5 Experiments; excerpt=Risk Control Primitive 4.2 CROP Loss and Calibration Rule 4.3 CROP Algorithm 5 Experiments Risk Proxy Sources. Evaluation Metrics. Datasets. 5.1 Prefix Utility at Varying Risks 5.2 Prefix Utility vs. AUROC 5.3 Boundary Quality of the Retained Prefix 5.4 Certified Prefixes for Downstream Repair 6 Discussion PRM gains extend beyond superficial artifacts. CROP changes the operational interface. Prefix certification is`。

Trade-off / failure / fallback：`arXiv:2605.30085v1 HTML — §6 Discussion; excerpt=y Quality of the Retained Prefix 5.4 Certified Prefixes for Downstream Repair 6 Discussion PRM gains extend beyond superficial artifacts. CROP changes the operational interface. Prefix certification is complementary to conformal factuality. 7 Limitations 8 Ethical Considerations References A Proofs B Experimental Details Splits and threshold grids. Token/format and trace-feature inventory. PRM risk proxy construction`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30085:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30085:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison](https://arxiv.org/html/2605.30087v1)

问题与机制：Existing benchmarks rarely show whether an error came from the evidence given to a method or from the method's conflict-resolution step. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：This creates an evaluation problem: systems must decide how to use conflicting or incomplete evidence; they cannot just retrieve facts from one clean history.。Method=`arXiv:2605.30087v1 HTML — §Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison; excerpt=ctive QA over Conflicting Multi-Source Personal Memory:A Diagnostic Testbed and Method Comparison Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Benchmark Design 2.1 Data-Generating Process`；Evaluation=`arXiv:2605.30087v1 HTML — §2 Benchmark Design; excerpt=Process and Scale 2.2 Ground Truth, Splits, and Protocol 3 Evaluated Methods 4 Experiments 4.1 Main Results and Selective QA 4.2 Factorial Decomposition (Resolver × \times Input) 4.3 Diagnostic Analysis by Reasoning Type 4.4 Robustness Summary 5 Discussion 6 Conclusion References A Related Work A.1 Comparison Table with Existing Conflict-Related Benchmarks A.2 Long-Term Memory Benchmarks and Agent Memory A.3 Knowled`。

Trade-off / failure / fallback：`arXiv:2605.30087v1 HTML — §5 Discussion; excerpt=times Input) 4.3 Diagnostic Analysis by Reasoning Type 4.4 Robustness Summary 5 Discussion 6 Conclusion References A Related Work A.1 Comparison Table with Existing Conflict-Related Benchmarks A.2 Long-Term Memory Benchmarks and Agent Memory A.3 Knowledge Conflicts A.4 RAG Conflict Resolution A.5 Cross-Modal Conflict Benchmarks A.6 Selective Prediction and Abstention A.7 Synthetic Benchmarks A.8 Agent Evaluation Benc`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30087:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30087:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems](https://arxiv.org/html/2605.30102v1)

问题与机制：The design space of agentic AI inference spans two extremes: frontier large language models (LLMs), typically hosted in the cloud and offering strong performance across a wide range of tasks at substantially high cost, and more cost-efficient small language models (SLMs), which are amenable to on-device inference. owner=`AGENT-PLATFORM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Our findings paint a nuanced picture of hybrid MAS design: while SLMs can effectively benefit from LLM assistance, the optimal architecture is highly task-dependent, and greater frontier-level compute does not consistently translate to better performance.。Method=`arXiv:2605.30102v1 HTML — §When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems; excerpt=ti-Agent systems Hybrid AI Context summarization and reset 3 Hybrid Multi-Agent architectures Plan–Execute–Verify–Replan (PEVR) Execute–Verify–Advise (EVA) 4 Experimental setup 4.1 Benchmarks HotpotQA FanOutQA AppWorld 4.2 Efficiency metrics 4.3 MAS backbones and hyper-parameters 5 Exploring the design space of Hybrid MASs Plan-based orchestration is a good fit for UI assistance tasks Query-based summarization and ad`；Evaluation=`arXiv:2605.30102v1 HTML — §4 Experimental setup; excerpt=t architectures Plan–Execute–Verify–Replan (PEVR) Execute–Verify–Advise (EVA) 4 Experimental setup 4.1 Benchmarks HotpotQA FanOutQA AppWorld 4.2 Efficiency metrics 4.3 MAS backbones and hyper-parameters 5 Exploring the design space of Hybrid MASs Plan-based orchestration is a good fit for UI assistance tasks Query-based summarization and advice is a better fit for Deep Search tasks (but only in small doses) The best`。

Trade-off / failure / fallback：`arXiv:2605.30102v1 HTML — §6 Limitations; excerpt=the sum of its parts Multi-Agent systems make better use of Executor KV-cache 6 Limitations 7 Conclusions References A Cost and Efficiency Metrics A.1 Energy consumption model A.1.1 Inference Decomposition A.1.2 Operation Count A.1.3 Hardware Efficiency and Energy A.1.4 Numerical Example A.1.5 Limitations A.2 Cloud Subscription Costs A.3 KV-cache size estimation B Ablating Summarization from EVA C Prompts C.1 Plannin`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30102:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30102:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md` 的当前正文，采用命题与 prior comparison 未变。

### [SEAL: Can Saturated Benchmarks Be Revived by LLM-as-a-Meta-Judge?](https://arxiv.org/html/2605.30104v1)

问题与机制：Therefore, we present Seeded Elimination with Adaptive LLM-as-a-Meta-Judge, a self-improving evaluation protocol for extracting latent ranking signal from saturated benchmarks. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Rather than constructing harder alternatives, we ask whether existing tasks can be made informative again through improved evaluation over the same candidate outputs.。Method=`arXiv:2605.30104v1 HTML — §Introduction / disclosed mechanism body; excerpt=the latency of exhaustive all-pairs comparison [ 4 ] . Motivated by this view, we introduce SEAL , S eeded E limination with A daptive L LM-as-a-Meta-Judge. SEAL first uses a cheap listwise judge to seed candidate outputs, then ranks them through a single-elimination tournament. Each match is judged pairwise under predefined task-level principles, while an LLM meta-judge generates rank-adaptive checklist items that`；Evaluation=`arXiv:2605.30104v1 HTML — §SEAL : Can Saturated Benchmarks Be Revived by LLM-as-a-Meta-Judge?; excerpt=ge 2.1 Seeded Elimination 2.2 LLM-as-a-Meta-Judge 2.3 Aggregation and Latency 3 Experiments 3.1 Agreement with Pairwise Judging 3.2 Accuracy–Latency Trade-off 3.3 Case Study: Adaptive Refinement vs. Non-Adaptive Backbone 3.4 Discussions 3.4.1 Stability Analysis 3.4.2 Leaderboards and Model Candidates 3.4.3 API Calls, Token Consumption, and Estimated Cost 4 Related Work 5 Conclusion 6 Limitations References A Detailed`。

Trade-off / failure / fallback：`arXiv:2605.30104v1 HTML — §3.4 Discussions; excerpt=ncy Trade-off 3.3 Case Study: Adaptive Refinement vs. Non-Adaptive Backbone 3.4 Discussions 3.4.1 Stability Analysis 3.4.2 Leaderboards and Model Candidates 3.4.3 API Calls, Token Consumption, and Estimated Cost 4 Related Work 5 Conclusion 6 Limitations References A Detailed Experimental Settings A.1 Predefined Principles and Seed Checklists Code Generation. Mathematical Reasoning. General Question Answering. Tool Ca`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30104:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30104:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing](https://arxiv.org/html/2605.30117v1)

问题与机制：We present VLA-Trace, a progressive diagnostic framework that analyzes VLA models through a unified evidence chain from representation dynamics to causal control attribution and behavioral manifestation. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on $π_{0.5}$ and OpenVLA reveal three key findings.。Method=`arXiv:2605.30117v1 HTML — §3 Representation Analysis Framework; excerpt=cult to diagnose model failures and, consequently, to design more effective VLA architectures. In particular, it remains unclear whether multimodal knowledge is preserved, how visual and linguistic signals are aligned during policy learning, and which modalities govern action decoding. Figure 1: Overview of VLA-Trace. The framework progressively diagnoses VLA models by tracing representation dynamics, identifying cau`；Evaluation=`arXiv:2605.30117v1 HTML — §2.2 Mechanistic Analysis of VLA Models; excerpt=echanistic Analysis of VLA Models 3 Representation Analysis Framework Overview. Experiment Setup. 3.1 Representation Shifts under VLA Adaptation Evaluation Metrics. 3.1.1 CKA Alignment Analysis Vision-Language Alignment. Checkpoint Drift and Adaptation. 3.2 Causal Pathways for Action Decoding Evaluation Metrics. 3.2.1 Attention Knockout 3.3 Behavioral Probes of Grounding and Shortcut Dependence Evaluation Metrics. 3.`。

Trade-off / failure / fallback：`arXiv:2605.30117v1 HTML — §4 Discussion and Outlook; excerpt=3.1 Attention IoU and Patterns 3.3.2 Visual Patch Masking 3.3.3 Input Editing 4 Discussion and Outlook Representation preservation and embodied modality adaptation. Designing causal visual-language circuits for action decoding. From visual grounding to compositional semantic control. 5 Conclusion References A Implementation Protocol Details A.1 Model Interfaces and Input Templates A.2 CKA Protocol Prompt templates fo`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30117:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30117:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?](https://arxiv.org/html/2605.30152v1)

问题与机制：Proactive agents read user activity as text and call an LLM on every event to decide whether to act. owner=`AGENT-WORKFLOW`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：It runs at 11.13 ms per event on a GPU server and 13.99 ms on a consumer laptop, approximately 4--7x and 12--83x faster than every single-forward LLM-as-trigger configuration tested in each regime, with an approximately 220 MiB BF16 resident footprint deployable on-device alongside the privacy-sensitive activity stream it consumes.。Method=`arXiv:2605.30152v1 HTML — §3 Problem Formulation; excerpt=act Download PDF Abstract 1 Introduction 2 Related Work 3 Problem Formulation 4 Method 4.1 Joint Trigger and Routing as Two Heads 4.2 Anchor Routing Labels 4.3 Downstream Agent 5 Experiments 5.1 Setup 5.2 Main Results 5.3 Ablation Study 5.4 Which Data Structure Best Suits the Proactive Trigger? 5.5 Efficiency 6 Conclusion References A Auxiliary Study: TGL on Mobile Proactive Agent A.1 Evaluation Protocol A.2 Results`；Evaluation=`arXiv:2605.30152v1 HTML — §5 Experiments; excerpt=igger and Routing as Two Heads 4.2 Anchor Routing Labels 4.3 Downstream Agent 5 Experiments 5.1 Setup 5.2 Main Results 5.3 Ablation Study 5.4 Which Data Structure Best Suits the Proactive Trigger? 5.5 Efficiency 6 Conclusion References A Auxiliary Study: TGL on Mobile Proactive Agent A.1 Evaluation Protocol A.2 Results B Per-Session Graph Construction Principled construction rule. Same recipe, two instantiations. Why`。

Trade-off / failure / fallback：`arXiv:2605.30152v1 HTML — §6 Conclusion; excerpt=F.1 Desktop ProactiveAgent F.2 FingerTip Mobile Proactive Agent G Case Study H Discussion Resource and latency implications. Why GNN trigger latency scales smoothly from server to consumer hardware. Shared hidden state. Drop-in compatibility. Personalization path. I Extended Related Work License: CC BY 4.0 arXiv:2605.30152v1 [cs.CL] 28 May 2026 \setmainfont texgyretermes-regular.otf[ BoldFont = texgyretermes-bold.ot`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30152:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30152:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md` 的当前正文，采用命题与 prior comparison 未变。

### [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/html/2605.30159v1)

问题与机制：As interactions unfold, ambiguous recursive summaries progressively discard task-relevant information and introduce semantic noise. owner=`AGENT-MEMORY`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments show that MMPO consistently outperforms existing methods on diverse long-horizon tasks, maintaining 97.1% performance even when scaled to 1.75M-token contexts.。Method=`arXiv:2605.30159v1 HTML — §2.1 POMDP Formulation; excerpt=ut on the clarity of the belief induced by intermediate summaries. To this end, we introduce Belief Entropy, a self-supervised proxy that probes how uncertain the model remains about the latent task state given its current memory. Based on this proxy, we propose Metacognitive Memory Policy Optimization (MMPO). Instead of relying only on sparse outcome-based signals, MMPO provides fine-grained, memory-specific supervi`；Evaluation=`arXiv:2605.30159v1 HTML — §4 Experiments; excerpt=ion 3.3 Optimization Objective 3.4 Algorithm Overview Implementation Details. 4 Experiments 4.1 Experimental Setup 4.2 Main Results Comparison with MemAgent Comparison with MEM1 4.3 Analysis Anchor Question Ablation. Belief Entropy Dynamics. 5 Related Work Memory-Augmented LLM Agents. Reinforcement Learning for LLMs. Belief States and Uncertainty Estimation. 6 Conclusion References A MMPO Algorithm B Summary-Induced`。

Trade-off / failure / fallback：`arXiv:2605.30159v1 HTML — §6 Conclusion; excerpt=F Implementation Details Memory Generation. Training Setup. Prompt Templates. G Limitations H Impact Statement License: arXiv.org perpetual non-exclusive license arXiv:2605.30159v1 [cs.AI] 28 May 2026 Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents Ziyan Liu Zhezheng Hao Yeqiu Chen Hong Wang Affiliation: University of Science and Technology of China Jingren Hou Affiliation: University of Science`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30159:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30159:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md` 的当前正文，采用命题与 prior comparison 未变。

### [Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms](https://arxiv.org/html/2605.30169v1)

问题与机制：As autonomous language model agents proliferate, forming an emerging agentic web with real-world consequences, what credibility signals can you use to decide whether to trust an unfamiliar agent in the wild and delegate to it? owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We argue that identity-based, ex post, regulative, sanction-based governance, such as reputation, is structurally inapplicable to dissociative agents, and we suggest a shift to observability-based, ex ante, constitutive, protocol-based behavioral harnesses.。Method=`arXiv:2605.30169v1 HTML — §Multi-Agent System (MAS) inherits these assumptions uncritically.; excerpt=ada DOI: 10.1145/3805689.3806748 ISBN: 979-8-4007-2596-8/2026/06 CCS: Computing methodologies Multi-agent systems CCS: Security and privacy Social aspects of security and privacy CCS: Social and professional topics Computing / technology policy Botao Amber Hu Note: Corresponding author Affiliation: University of Oxford , Oxford , UK email: botao.hu@cs.ox.ac.uk , Helena Rong Affiliation: New York University Shanghai ,`；Evaluation=`arXiv:2605.30169v1 HTML — §Evaluation/results body; dedicated heading Not Disclosed; excerpt=merely record behavior; it evaluates behavior against norms and translates that evaluation into Reward/Punishment . Rewards—such as price premiums, preferred placement, or expanded access—incentivize cooperation, while punishments—such as exclusion, reduced visibility, or financial penalties—deter defection ( Milgrom and Roberts, 1982 ) . These evaluations are then aggregated into Reputation : a summary record indexe`。

Trade-off / failure / fallback：`arXiv:2605.30169v1 HTML — §5. Discussion; excerpt=Hart’s four justifications. Principal Erosion. Prompt injection as inversion. 5 Discussion 5.1 Situating the Argument 5.2 DID Jurisprudence as Precedent 5.3 From Ex Post Governance to Ex Ante Harnesses Open questions. On surveillance. 6 Conclusion References License: CC BY-NC-ND 4.0 arXiv:2605.30169v1 [cs.CY] 28 May 2026 Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms \acmConfere`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30169:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30169:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MULTI-AGENT` / `books/part-07-agent/82-multi-agent.md` 的当前正文，采用命题与 prior comparison 未变。

### [A Dual-Path Architecture for Scaling Compute and Capacity in LLMs](https://arxiv.org/html/2605.30202v1)

问题与机制：We propose a novel dual-path block that can flexibly scale compute, the number of sequential operations applied to a hidden state, and capacity, the parameters available at a single step. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We show that across two FLOP budgets, our dual-path model surpasses iso-FLOP matched models on language modeling and downstream evaluations, while using fewer parameters than the baseline at matched FLOPs.。Method=`arXiv:2605.30202v1 HTML — §A Dual-Path Architecture for Scaling Compute and Capacity in LLMs; excerpt=A Dual-Path Architecture for Scaling Compute and Capacity in LLMs Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related W`；Evaluation=`arXiv:2605.30202v1 HTML — §4 Experiments; excerpt=er-token gating. Single-axis baselines. 3.4 Routing read-outs Path alignment. 4 Experiments 4.1 Setup Models and configurations. Data and training. Baselines. Evaluation. 4.2 Main results A dual-path configuration performs best at both budgets. Allocation between deep and wide path. Pareto position in the parameter–quality plane. 4.3 Where does the model spend its budget? Depth in the stack. Task. Token identity. Per`。

Trade-off / failure / fallback：`arXiv:2605.30202v1 HTML — §5 Conclusion; excerpt=A Dual-Path Architecture for Scaling Compute and Capacity in LLMs Report GitHub Issue × Title: Content selection saved. Describe the issue below: Description: Submit without GitHub Submit in GitHub arXiv is now an independent nonprofit! Learn more × Back to arXiv Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work Looped and recursive transformers. Per-token compute allocation.`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30202:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30202:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [MarginGate: Sparse Margin-Triggered Verification for Batch-Invariant LLM Inference](https://arxiv.org/html/2605.30218v1)

问题与机制：Temperature-zero BF16 LLM inference is often treated as reproducible, yet the same request can emit different tokens when decoded alone or inside a larger batch. owner=`INFER-TENSORRT-LLM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：On DSR1-Distill-Qwen-7B, the same policy reaches determinism in a harder regime at 49.50% triggers.。Method=`arXiv:2605.30218v1 HTML — §3 Design: MarginGate; excerpt=d token against a deterministic re-computation and repairs disagreements. These methods establish that deterministic decoding is recoverable. They also raise a narrower question: which decoded steps actually need verification? Our answer starts from measurement: batch-induced token flips are rare, local, and signaled by near-tie margins . Across five open-weight LLMs and the three flip-rate benchmarks, only 0.3 0.3 –`；Evaluation=`arXiv:2605.30218v1 HTML — §4 Evaluation; excerpt=Single-Column Repair Deterministic verifier contract. 3.3 Verifier Accounting 4 Evaluation 4.1 Setup Evaluation protocol. Baselines. 4.2 Main Results Implementation details. 4.3 Threshold Operating Points End-to-end sweep. 4.4 Ablations and Robustness Repair-action ablation. Heterogeneous batches. Batch-size scaling. Dataset transfer. Recall and sequence determinism. 5 Discussion 6 Conclusion References A Threshold C`。

Trade-off / failure / fallback：`arXiv:2605.30218v1 HTML — §5 Discussion; excerpt=tches. Batch-size scaling. Dataset transfer. Recall and sequence determinism. 5 Discussion 6 Conclusion References A Threshold Calibration Details B Additional K/V Diagnostics B.1 Per-Model Flip-Aligned Trajectories B.2 Oracle Repair Traces B.3 Layer-Wise Structure C Heterogeneous Batches License: arXiv.org perpetual non-exclusive license arXiv:2605.30218v1 [cs.LG] 28 May 2026 MarginGate: Sparse Margin-Triggered Veri`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30218:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30218:end -->

**当前 Books 投影。** `Applied` 到 `INFER-CONTINUOUS-BATCHING` / `books/part-05-inference-system/46-continuous-batching.md`；当前正文唯一 marker 已核验，未产生新写回。

### [BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/html/2605.30226v1)

问题与机制：To address these challenges, we propose BORA, an offline-to-online RL post-training framework designed for real-world dexterous VLA models. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Extensive evaluations across five complex real-world dexterous tasks demonstrate that BORA significantly outperforms pure imitation learning and traditional decoupled RL baselines, achieving a 33% absolute increase in average success rate under standard settings and up to a 43% improvement in unseen object generalization.。Method=`arXiv:2605.30226v1 HTML — §3 Method; excerpt=Manipulation Post-Training and Adaptation of Vision-Language-Action Policies 3 Method 3.1 Offline RL with Action-Conditioned Critic and Consistency Policy Action-Conditioned Critic. Conservative Policy Improvement. 3.2 Bridging the Deployment Gap: HiL Residual Chunk Adaptation 4 Experiments 4.1 Experimental Setup 4.2 Main Results and Analysis 5 Limitations 6 Conclusion A Detailed Critic Formulation B Implementation`；Evaluation=`arXiv:2605.30226v1 HTML — §4 Experiments; excerpt=y Improvement. 3.2 Bridging the Deployment Gap: HiL Residual Chunk Adaptation 4 Experiments 4.1 Experimental Setup 4.2 Main Results and Analysis 5 Limitations 6 Conclusion A Detailed Critic Formulation B Implementation Details and Training Safeguards B.1 Advantage Gating Mechanism B.2 Two-Stage Post-Training Pipeline B.3 Online Residual Alignment via Conservative Value Guidance B.4 Online Residual Adaptation Algorith`。

Trade-off / failure / fallback：`arXiv:2605.30226v1 HTML — §5 Limitations; excerpt=Adaptation 4 Experiments 4.1 Experimental Setup 4.2 Main Results and Analysis 5 Limitations 6 Conclusion A Detailed Critic Formulation B Implementation Details and Training Safeguards B.1 Advantage Gating Mechanism B.2 Two-Stage Post-Training Pipeline B.3 Online Residual Alignment via Conservative Value Guidance B.4 Online Residual Adaptation Algorithm C Experimental Details C.1 Robot Hardware and Teleoperation Setup`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30226:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30226:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization](https://arxiv.org/html/2605.30227v1)

问题与机制：We propose temporal and structural credit assignment, which decomposes the objective along two axes: (i) temporal credit, using state-space bottlenecks to identify critical rounds, and (ii) structural credit, using stationary role policies to isolate agent contributions. owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across diverse reasoning benchmarks, our approach substantially reduces query complexity while improving performance, providing a principled and interpretable path toward self-improving MAS.。Method=`arXiv:2605.30227v1 HTML — §3 Problem Formulation; excerpt=Final-Round Scoring. Optimization Objective. Textual-Gradient Prompt Update. 4 Methodology 4.1 State-Space Bottleneck Without aggregation. With aggregation. New optimization variables. 4.2 Parameter Sharing 4.3 Verbalized BCD Credit Computing. Verbalized BCD over Prompt Blocks. Phase A: optimize roles while fixing aggregation prompts. Phase B: optimize aggregation prompts while fixing roles. 5 Experiments 5.1 Settin`；Evaluation=`arXiv:2605.30227v1 HTML — §5 Experiments; excerpt=ggregation prompts. Phase B: optimize aggregation prompts while fixing roles. 5 Experiments 5.1 Settings 5.2 Main Results and Analysis 5.3 RQ1: Effectiveness 5.4 RQ2: Ablations 5.5 RQ3: Sensetivity 5.6 RQ4: Interpretability 6 Closing Remarks References A Appendix Overview B Evaluation and Prompt Optimisation Prompts B.1 Agent Turn Evaluation Prompt B.2 Agent Diagnosis Prompt B.3 Role Prompt Optimisation Prompt C Exte`。

Trade-off / failure / fallback：`arXiv:2605.30227v1 HTML — §D.3 Failure Pattern Distribution; excerpt=le) D.1 Overall Prediction Statistics D.2 Distribution Across Debate Rounds D.3 Failure Pattern Distribution D.4 Round–Error Cross Analysis License: CC BY 4.0 arXiv:2605.30227v1 [cs.MA] 28 May 2026 Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization Wenwu Li Affiliation: Tongji University Shanghai, China {wenwu,2250753,bjin,whli}@tongji.edu.cn Yuran Song Affiliation: Tongji`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30227:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30227:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `AGENT-MULTI-AGENT` / `books/part-07-agent/82-multi-agent.md` 的当前正文，采用命题与 prior comparison 未变。

### [Same Evidence, Different Answers: Canonical-Context On-Policy Distillation for Multi-Turn Language Models](https://arxiv.org/html/2605.30251v1)

问题与机制：We argue that a key reason for this gap is self-anchored drift: responses produced under partial information introduce unsupported assumptions, and those assumptions later distort the final answer. owner=`TRAIN-SFT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Further analyses suggest that CCOPD strengthens grounding in user evidence and reduces sensitivity to contamination from earlier assistant turns.。Method=`arXiv:2605.30251v1 HTML — §3.1 Problem Formulation; excerpt=s, and those assumptions later distort the final answer. To reduce this effect, we propose Canonical-Context On-Policy Distillation (CCOPD). During training, the same base model is used in two roles: a frozen teacher conditioned on the clean FULL prompt and a trainable student that receives the same evidence incrementally through a multi-turn conversation; CCOPD aligns the student’s behavior on its own trajectories w`；Evaluation=`arXiv:2605.30251v1 HTML — §5 Experiments and Analysis; excerpt=onical Relabeling 4.3 Answer-Masked Reverse-KL Objective Sequence-level view. 5 Experiments and Analysis 5.1 Experimental Setup Models. Training data and pair construction. Evaluation protocol. Compared systems. 5.2 Main Results RAW improves without clean-task drift. Math-only training transfers out of domain. 5.3 Ablations and Mechanism Diagnostics Teacher source. KL direction. History-stress diagnostics. Evidence f`。

Trade-off / failure / fallback：`arXiv:2605.30251v1 HTML — §6 Conclusion; excerpt=lly re-grounding its answer in the completed user-provided shards. We call this failure mode self-anchored drift . A trivial solution is to repair the trajectory at inference time. Such methods can reflect on, revise, reset, or consolidate intermediate reasoning before the model commits to a final answer ( Shinn et al., 2023 ; Madaan et al., 2023 ; Mohammad Khalid et al., 2025 ) . Although they are often useful in de`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30251:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30251:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-SFT` / `books/part-04-training-system/29-sft.md` 的当前正文，采用命题与 prior comparison 未变。

### [How LoRA Remembers? A Parametric Memory Law for LLM Finetuning](https://arxiv.org/html/2605.30260v1)

问题与机制：We introduce the Parametric Memory Law, a robust power law linking loss reduction Delta L to effective parameters and sequence length. owner=`TRAIN-LORA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Empirical evaluations demonstrate that MemFT can enhance memory fidelity and efficiency.。Method=`arXiv:2605.30260v1 HTML — §5 MemFT: Methodology and Empirical Verification; excerpt=.2 Token-Level Probability Dynamics 4.3 Deterministic Phase Transition 5 MemFT: Methodology and Empirical Verification 5.1 The MemFT Method MemFT-OT: Only Threshold Variant. MemFT-SW: Adaptive Sliding Mechanisms. 5.2 Experimental Setup 5.3 Main Results 5.4 Analysis Applicability to Exact-Memory Scenarios. Beyond Memorization: Enhanced Generalization. 6 Related Work LLM Memory. LoRA as Parametric Memory. 7 Conclusion`；Evaluation=`arXiv:2605.30260v1 HTML — §Evaluation Metrics.; excerpt=reliminary 2.1 Exact Parametric Memory Task Task Setup. Answer-only Accounting. Evaluation Metrics. 2.2 LoRA-based Parametric Memory Injection 3 The Parametric Memory Law 3.1 Empirical Observation: Linearity in Log-Log Space 3.2 Formulating the Parametric Memory Law 3.3 Fitting Validation 4 The Deterministic Phase Transition of Memory 4.1 The Loss-Accuracy Misalignment 4.2 Token-Level Probability Dynamics 4.3 Determi`。

Trade-off / failure / fallback：`arXiv:2605.30260v1 HTML — §7 Conclusion; excerpt=with alternative tokens, sharply increasing the risk of autoregressive cascade failure. Based on these insights, we propose MemFT , an optimization strategy that redirects the parameter budget to sub-threshold tokens to maximize efficiency. Our main contributions are: • Parametric Memory Law: We establish a power law that quantifies exact memory capacity based on parameters and sequence length. • Dynamics Mechanism:`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30260:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30260:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-LORA` / `books/part-04-training-system/30-lora.md` 的当前正文，采用命题与 prior comparison 未变。

### [minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models](https://arxiv.org/html/2605.30263v1)

问题与机制：In this work, we present minWM, a full-stack open-source framework for building real-time interactive video world models. owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Project Page: [https://github.com/shengshu-ai/minWM](https://github.com/shengshu-ai/minWM)。Method=`arXiv:2605.30263v1 HTML — §minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models; excerpt=Why HTML? Report Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Method 2.1 Camera-Controllable Training for Bidirectional Diffusion Models 2.2 AR Diffusion Distillation for Real-Time Interactive Video World Models Stage 1: AR diffusion training. Stage 2 (option a): causal ODE initialization. Stage 2 (option b): causal CD initialization. Stage 3: asymmetric DMD. Camera-controllable distillation. 3 Expe`；Evaluation=`arXiv:2605.30263v1 HTML — §3 Experiments; excerpt=CD initialization. Stage 3: asymmetric DMD. Camera-controllable distillation. 3 Experiments 3.1 Setup 3.2 Results Few-step AR models substantially reduce the first-frame latency. Few-step AR models preserve camera-controllable generation capability. 3.3 Ablation Studies Training data. Training steps. Minimal batch size. 4 Conclusion and the Future Work References License: CC BY 4.0 arXiv:2605.30263v1 [cs.CV] 28 May 2`。

Trade-off / failure / fallback：`arXiv:2605.30263v1 HTML — §4 Conclusion and the Future Work; excerpt=eady possesses autoregressive generation capability, but still suffers from two limitations: (1) it requires multi-step generation, leading to high latency; and (2) due to exposure bias induced by autoregression [ 20 ] , its quality remains inferior to that of bidirectional diffusion models. These limitations motivate the subsequent distillation strategy. Stage 2 (option a): causal ODE initialization. Causal Forcing`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30263:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30263:end -->

**当前 Books 投影。** `Applied` 到 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`；当前正文唯一 marker 已核验，未产生新写回。

### [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/html/2605.30280v1)

问题与机制：In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. owner=`MULTIMODAL-EMBODIED-VLA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Experiments on manipulation, navigation, and trajectory-centric benchmarks show consistent multi-task performance and out-of-distribution generalization under variations in scene layout, background, lighting, object configuration, and robot embodiment.。Method=`arXiv:2605.30280v1 HTML — §2.1 Problem Formulation; excerpt=tract 1 Introduction 2 Unified Embodied Model 2.1 Problem Formulation 2.2 Model Architecture Vision-language backbone. Action expert. 2.3 Embodiment-aware Prompt Conditioning 2.4 Unified Action and Trajectory Representation Control signal types. Channel layout. Task-aware conditioning. 2.5 Training Objectives Flow-matching action loss. Vision-language loss. Joint objective. 3 Large-Scale Joint Pretraining 3.1 Trainin`；Evaluation=`arXiv:2605.30280v1 HTML — §Experiments; excerpt=atching. Reward design. Rollout infrastructure. Out-of-domain generalization. 5 Experiments 5.1 Main Results 5.1.1 Manipulation Results in Simulation A single generalist outperforms most specialists. Pretraining provides a strong foundation, and instruction tuning yields substantial gains. 5.1.2 Manipulation Results in the Real World In-domain tasks. OOD tasks. Results on in-domain tasks. Results on OOD tasks. Overal`。

Trade-off / failure / fallback：`arXiv:2605.30280v1 HTML — §Conclusion; excerpt=ments. 5.2.3 Effect of RL Post-Training 5.2.4 State Conditioning 6 Conclusion 7 Limitations and Future Work 8 Contributions and Acknowledgments References License: arXiv.org perpetual non-exclusive license arXiv:2605.30280v1 [cs.RO] 28 May 2026 Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments Qwen Team Abstract Embodied intelligence is often studied through speciali`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30280:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30280:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的当前正文，采用命题与 prior comparison 未变。

### [MIRA: Mid-training Rubric Anchoring for Source-Aware Data Selection](https://arxiv.org/html/2605.30288v1)

问题与机制：To address this mismatch, we propose MIRA, a source-aware filtering framework based on self-anchored rubric discovery. owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：As a result, effective selection requires both scalability and source-adaptive semantic criteria.。Method=`arXiv:2605.30288v1 HTML — §3 Method; excerpt=ct 1 Introduction 2 Related Work 2.1 Mid-training 2.2 Training Data Selection 3 Method 3.1 Overview 3.2 Self-Anchored Rubric Discovery Source Clustering and Free-form Judging. Judgment clustering and anchor extraction. 3.3 Anchored Judge Distillation Anchored teacher scoring. Student distillation. 3.4 Source-Conditioned Reliability Aggregation Residual diagnostics. Post-hoc masking and robust aggregation. 3.5 Source-`；Evaluation=`arXiv:2605.30288v1 HTML — §4 Experiments; excerpt=nd robust aggregation. 3.5 Source-Preserving Selection Selection granularity. 4 Experiments 4.1 Main Results 5 Analysis 5.1 Scorer Analysis 5.2 Reliability Masking 5.3 Rubric Space Visualization 5.4 Rubric Space 5.5 Case Study 6 Conclusion References A Experimental Setup A.1 Baselines A.2 Data Sources and Grouping Sources and groups. Per-source sampling. A.3 Mid-training Configuration Token budget and iteration count`。

Trade-off / failure / fallback：`arXiv:2605.30288v1 HTML — §6 Conclusion; excerpt=lid and whether tool feedback changes subsequent actions. These source-specific failures would be difficult to capture with a single generic text-quality criterion, supporting the need for source-aware semantic filtering in heterogeneous mid-training data. 6 Conclusion We presented MIRA , a source-aware filtering framework for heterogeneous mid-training data. MIRA discovers group-specific anchor rubrics from sampled`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30288:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30288:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-DATA` / `books/part-04-training-system/27-data.md` 的当前正文，采用命题与 prior comparison 未变。

### [Self-Trained Verification for Training- and Test-Time Self-Improvement](https://arxiv.org/html/2605.30290v1)

问题与机制：To address this challenge, we propose self-trained verification (STV). owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Website: https://ar-forum.github.io/stv-webpage。Method=`arXiv:2605.30290v1 HTML — §2 Problem Formulation; excerpt=erification-refinement (V-R) loops; and at training time, through self-training methods. Both are gated by the same bottleneck: the verifier. V-R loops stall when verifier scores inflate while accuracy stagnates, and when feedback is too generic to act on; self-training fails similarly when bad self-generated data are added to training. Better verification would unlock both, but the capability we want to train, i.e.,`；Evaluation=`arXiv:2605.30290v1 HTML — §5 Experiments; excerpt=ion 3 Self-Trained Verification 4 Verifier-in-the-Loop Training for Generator 5 Experiments 5.1 Setup 5.2 Verifier-Guided Refinement Base generator. Scientific reasoning results. Continual-trained generator. 5.3 Weak-to-Strong Verification 5.4 Verifier-in-the-Loop (ViL) Generator Training Ablation for the use of oracle. 5.5 Why STV Works Calibrated test-time scaling. Value of trained feedback. 5.6 How STV Shapes the`。

Trade-off / failure / fallback：`arXiv:2605.30290v1 HTML — §7 Conclusion, Limitations, and Future Work; excerpt=not suppress diversity. Refinement vs resampling. 6 Related Work 7 Conclusion, Limitations, and Future Work References A Verifier Feedback Examples A.1 The untrained verifier accepts flawed solutions A.2 Both verifiers reject, but the untrained verifier’s feedback is incoherent License: CC BY 4.0 arXiv:2605.30290v1 [cs.LG] 28 May 2026 Self-Trained Verification for Training- and Test-Time Self-Improvement Abstract Se`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30290:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30290:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [RAFI -- A Ray/Work Forwarding Infrastructure for Data Parallel Multi-Node/Multi-GPU Computing](https://arxiv.org/html/2605.30294v1)

问题与机制：We present RaFI, a CUDA and MPI based software framework that simplifies the task of building GPU-enabled data-parallel software where rays or similar work items need to migrate between different GPUs. owner=`TRAIN-PIPELINE-PARALLEL`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We describe RaFI's motivation and implementation, and show its potential in several example applications.。Method=`arXiv:2605.30294v1 HTML — §2.1 “Ray”s, Templates, and Overall Software Architecture; excerpt=RaFI Ray Forwarding Infrastructure 2.1 “Ray”s, Templates, and Overall Software Architecture 2.2 Ray Queues 2.3 Device Interface 2.4 RaFI Host Context 3 Implementation 3.1 Host Context and Device Interface 3.2 MPI Ray Forwarding 3.2.1 Sorting by Destination 3.2.2 Exchanging Rays 3.2.3 Wrap-up 4 Sample Use Cases 4.1 VoPaT 4.2 Data-Parallel Unstructured Volume Rendering 4.3 Data-Parallel Unstructured Schlieren Renderin`；Evaluation=`arXiv:2605.30294v1 HTML — §Evaluation/results body; dedicated heading Not Disclosed; excerpt=ed by the BriX framework [ 27 ] , which forwarded rays from GPU kernels. In our evaluation, we will also integrate RaFI into VoPaT [ 28 ] , which can best be viewed as a re-work of BriX for volume data (see Section 4.1 ). In our implementation, we use CUDA [ 12 ] for all device kernels. This framework mainly influences how rays are placed into the output queues, but it can be easily adapted to other GPU programming p`。

Trade-off / failure / fallback：`arXiv:2605.30294v1 HTML — §5 Summary and Discussion; excerpt=eamline Computation 4.5 Distributed Barnes-Hut N-Body Computation 5 Summary and Discussion 5.1 Performance 5.2 Usage Beyond Ray Forwarding 5.3 Limitations 6 Conclusion and Future Work Acknowledgements References License: CC BY 4.0 arXiv:2605.30294v1 [cs.DC] 28 May 2026 \preprinttext \vgtccategory Research \authorfooter Ingo Wald and Andrea Paris are with NVIDIA (e-mails: iwald@nvidia.com, aparis@nvidia.com). Serkan D`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30294:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30294:end -->

**当前 Books 投影。** `Report Only — Context`；该实现语境不改变长期知识，不写入 Books。

### [Gram: Assessing sabotage propensities via automated alignment auditing](https://arxiv.org/html/2605.30322v1)

问题与机制：We introduce Gram, an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We find Gemini models misbehave in about 2-3% of our simulated trajectories.。Method=`arXiv:2605.30322v1 HTML — §2 Method; excerpt=rt Issue Back to Abstract Download PDF Abstract 1 Introduction Contributions. 2 Method 2.1 Background: Automated Auditing with Petri 2.2 Seed instructions 2.3 Improved auditor 2.4 Reproduction & Investigator agents Reproduction of misbehavior Investigation of misbehavior. 3 Results 3.1 Automated auditing 3.2 Qualitative analysis of Gemini’s behavior 3.2.1 Excessive role-playing 3.2.2 Evaluation awareness goes both wa`；Evaluation=`arXiv:2605.30322v1 HTML — §3 Results; excerpt=Investigator agents Reproduction of misbehavior Investigation of misbehavior. 3 Results 3.1 Automated auditing 3.2 Qualitative analysis of Gemini’s behavior 3.2.1 Excessive role-playing 3.2.2 Evaluation awareness goes both ways 3.2.3 Excessive goal-seeking 3.3 Reproducing misbehavior in static environments 3.3.1 Validation of the investigator agent 3.3.2 Applying the investigator agent to auditing trajectories 4 Rela`。

Trade-off / failure / fallback：`arXiv:2605.30322v1 HTML — §5 Conclusion; excerpt=ing the investigator agent to auditing trajectories 4 Related work 5 Conclusion Limitations & Future Work. References A Appendix A.1 Additional results A.2 Judges and validation A.2.1 Scheming judge prompt A.2.2 Eval awareness judge prompt A.2.3 Role-playing judge prompt A.3 Auditor instructions A.3.1 Differences from Petri v2 De-emphasized red-teaming framing. Strengthened autonomous-mode guidance. Removed rollback`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30322:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30322:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?](https://arxiv.org/html/2605.30329v1)

问题与机制：We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. owner=`PLATFORM-EVALUATION-SYSTEM`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives.。Method=`arXiv:2605.30329v1 HTML — §Challenges and Design Choices.; excerpt=r-Removal Robustness B.6 Surface-Feature Baselines B.7 Adversarial Injection of Methodological Flaws B.8 Breakdowns by Year, Subfield, and Writing Quality B.9 Qualitative Examples of False and True Positives License: arXiv.org perpetual non-exclusive license arXiv:2605.30329v1 [cs.LG] 28 May 2026 SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones? Sy-Tuyen Ho Minghui Liu Huy Nghiem Fu`；Evaluation=`arXiv:2605.30329v1 HTML — §2 SoundnessBench: Benchmark Reconstruction; excerpt=ap. 2 SoundnessBench: Benchmark Reconstruction Challenges and Design Choices. 3 Evaluation 3.1 Evaluation Setup 3.2 Main Results: A Broad Optimism Bias in Scientific Judgment 3.3 Robustness Controls and Alternative Explanations 3.4 Under Aggressive Prompting: Bias Shifts Toward Over-Conservatism 4 Related Work 5 Conclusion References A Supplementary Material for Data Construction A.1 Prompt to Extract Proposal A.2 Pr`。

Trade-off / failure / fallback：`arXiv:2605.30329v1 HTML — §5 Conclusion; excerpt=• Confounder and Robustness Controls: We add analyses for reviewer-label proxy limitations, public-corpus contamination, title/identifier recognition, surface-feature heuristics, year/subfield/writing-quality slices, and injected methodological flaws. These controls strengthen the interpretation that LLM failures are not artifacts of a single shallow cue. • Quantifying the “Optimism-Fragility” Tradeoff: We provide a`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30329:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30329:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md` 的当前正文，采用命题与 prior comparison 未变。

### [Demystifying Data Organization for Enhanced LLM Training](https://arxiv.org/html/2605.30334v1)

问题与机制：Guided by them, we introduce two novel data ordering methods termed STR and SAW. owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：They also demonstrate the robustness of our proposed data ordering methods in enhancing the stability and performance of LLM training.。Method=`arXiv:2605.30334v1 HTML — §2 Problem Formulation; excerpt=2: Cyclic Scheduling. 3.3 G3: Curriculum Continuity. 3.4 G4: Local Diversity. 4 Methodology 5 Experiment 5.1 Experimental Setup 5.2 Guidance Analysis 5.2.1 G1: Boundary Sharpening 5.2.2 G2: Cyclic Scheduling 5.2.3 G3: Curriculum Continuity 5.2.4 G4: Local Diversity 5.3 Main Results 5.4 Scaling-up Result 6 Conclusion References A Extended Discussion on Guidances B Related Work B.1 Data Efficiency B.2 Data Organization`；Evaluation=`arXiv:2605.30334v1 HTML — §5 Experiment; excerpt=duling. 3.3 G3: Curriculum Continuity. 3.4 G4: Local Diversity. 4 Methodology 5 Experiment 5.1 Experimental Setup 5.2 Guidance Analysis 5.2.1 G1: Boundary Sharpening 5.2.2 G2: Cyclic Scheduling 5.2.3 G3: Curriculum Continuity 5.2.4 G4: Local Diversity 5.3 Main Results 5.4 Scaling-up Result 6 Conclusion References A Extended Discussion on Guidances B Related Work B.1 Data Efficiency B.2 Data Organization C Additional`。

Trade-off / failure / fallback：`arXiv:2605.30334v1 HTML — §6 Conclusion; excerpt=rsity 5.3 Main Results 5.4 Scaling-up Result 6 Conclusion References A Extended Discussion on Guidances B Related Work B.1 Data Efficiency B.2 Data Organization C Additional Experimental Setup C.1 Setup for Guidances Analysis C.1.1 G1: Boundary Sharpening C.1.2 G2: Cyclic Scheduling C.1.3 G3: Curriculum Continuity C.1.4 G4: Local Diversity C.2 Data C.3 Model C.4 Training Configuration C.5 Evaluation D Test Loss Extra`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30334:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30334:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-DATA` / `books/part-04-training-system/27-data.md` 的当前正文，采用命题与 prior comparison 未变。

### [Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents](https://arxiv.org/html/2605.30335v1)

问题与机制：Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is locally coherent. owner=`AGENT-MULTI-AGENT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Three intuitive LLM-side mitigations(retrieval, partition-aware prompting, aggregator-LLM) each fail or regress.。Method=`arXiv:2605.30335v1 HTML — §3 Method; excerpt=omponent JCD. Multi-component agent. Aggregator. The two candidate workflows. 3 Method 3.1 When local coherence composes Lifted local feasible sets. 3.2 Exposure interpretation 3.3 Disagreement controls the residual 3.4 Quantitative magnitude prediction 3.5 Hierarchical repair Per-iteration cost. Where the cyclic machinery actually bites. 3.6 Runtime use 3.7 Sequential monitoring: anytime-valid coherence test 4 Exper`；Evaluation=`arXiv:2605.30335v1 HTML — §4 Experimental setup; excerpt=ites. 3.6 Runtime use 3.7 Sequential monitoring: anytime-valid coherence test 4 Experimental setup Models. Leakage control. Scope of the evaluation. Compositional ensemble. Benchmark properties. 5 Results 5.1 Compositional residual and controls Compositional residual under random routing. Empirical validation of the magnitude prediction. Same-model decoupling control. Compositional Brier against resolved labels. Disa`。

Trade-off / failure / fallback：`arXiv:2605.30335v1 HTML — §6 Conclusion; excerpt=ing thresholds. 5.8 Per-component layer (summary) Reproducibility. 6 Conclusion Limitations. Future work. References A Within-component projection facts B Proof of Theorem (reverse direction) C Closed-form local projections Negation ( m = 2 m{=}2 , r 1 + r 2 = 1 r_{1}+r_{2}=1 ). Conjunction ( m = 3 m{=}3 , r 3 = r 1 ∧ r 2 r_{3}{=}r_{1}\!\wedge\!r_{2} ). Disjunction ( m = 3 m{=}3 , r 3 = r 1 ∨ r 2 r_{3}{=}r_{1}\!\vee\`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30335:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30335:end -->

**当前 Books 投影。** `Applied` 到 `AGENT-MULTI-AGENT` / `books/part-07-agent/82-multi-agent.md`；当前正文唯一 marker 已核验，未产生新写回。

### [Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching](https://arxiv.org/html/2605.30337v1)

问题与机制：We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. owner=`TRAIN-SFT`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.。Method=`arXiv:2605.30337v1 HTML — §3 Method; excerpt=rt Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related work 3 Method 3.1 Data selection via convex approximation 3.2 Efficient finetuning via gradient reuse 4 Experimental results 5 Conclusion and Limitations References A Experimental protocol details B Algorithmic details B.1 Core HullFT procedures B.2 Exact Carathéodory reduction B.3 PCA-reduced convex approximation B.4 Weight-proportional padding`；Evaluation=`arXiv:2605.30337v1 HTML — §4 Experimental results; excerpt=election via convex approximation 3.2 Efficient finetuning via gradient reuse 4 Experimental results 5 Conclusion and Limitations References A Experimental protocol details B Algorithmic details B.1 Core HullFT procedures B.2 Exact Carathéodory reduction B.3 PCA-reduced convex approximation B.4 Weight-proportional padding C Ablations C.1 Integerization: pad-by-weights vs. geometric (FW family) C.2 Carathéodory select`。

Trade-off / failure / fallback：`arXiv:2605.30337v1 HTML — §5 Conclusion and Limitations; excerpt=Efficient finetuning via gradient reuse 4 Experimental results 5 Conclusion and Limitations References A Experimental protocol details B Algorithmic details B.1 Core HullFT procedures B.2 Exact Carathéodory reduction B.3 PCA-reduced convex approximation B.4 Weight-proportional padding C Ablations C.1 Integerization: pad-by-weights vs. geometric (FW family) C.2 Carathéodory selection and its integerizations C.3 Frank–`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30337:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30337:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-SFT` / `books/part-04-training-system/29-sft.md` 的当前正文，采用命题与 prior comparison 未变。

### [YoCausal: How Far is Video Generation from World Model? A Causality Perspective](https://arxiv.org/html/2605.30346v1)

问题与机制：We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. owner=`MULTIMODAL-WORLD-MODELS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol.。Method=`arXiv:2605.30346v1 HTML — §3 Method; excerpt=-of-Expectation Paradigm. Arrow of Time and Causality in Video Understanding. 3 Method 3.1 Dataset Construction 3.2 Formulating Surprise via Denoising Loss 3.3 Level 1: Measuring Arrow-of-Time Perception via RSI 3.3.1 Reversal Surprise Index. Blind spot of RSI. 3.4 Level 2: Disentangling Causality via CCI 3.4.1 Causality Cognition Index. 4 Experiment Settings. 4.1 RSI Results 4.2 CCI Results 4.3 Aggregating Arrow of`；Evaluation=`arXiv:2605.30346v1 HTML — §Video Generation Evaluation.; excerpt=Abstract 1 Introduction 2 Related Work Video Diffusion Models. Video Generation Evaluation. Intuitive Physics and Violation-of-Expectation Paradigm. Arrow of Time and Causality in Video Understanding. 3 Method 3.1 Dataset Construction 3.2 Formulating Surprise via Denoising Loss 3.3 Level 1: Measuring Arrow-of-Time Perception via RSI 3.3.1 Reversal Surprise Index. Blind spot of RSI. 3.4 Level 2: Disentangling Causalit`。

Trade-off / failure / fallback：`arXiv:2605.30346v1 HTML — §5 Conclusion and Limitation; excerpt=d Generation Evolution. 4.5 Entropy-Controlled Subset Analysis 5 Conclusion and Limitation Limitation. A.1 Details on Dataset Construction A.2 Models Setting A.3 Video Preprocessing A.4 Details on RSI Algorithm A.5 Details on CCI Algorithm A.6 Prompt Bias A.7 VLM Reliability A.8 VLM Sensitivity Analysis A.9 Limitation: Implicit Causality A.10 Details on Human Annotating A.11 Details on Human Preference A.12 Detailed`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30346:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30346:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的当前正文，采用命题与 prior comparison 未变。

### [LLMSurgeon: Diagnosing Data Mixture of Large Language Models](https://arxiv.org/html/2605.30348v1)

问题与机制：We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. owner=`TRAIN-DATA`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures.。Method=`arXiv:2605.30348v1 HTML — §3.1 Problem Formulation; excerpt=Benchmark for Data Mixture Surgery 4 LLMSurgeon: A simple Data Mixture Surgery Method 4.1 Characterizing Systematic Bias 4.2 Observing the Target Distribution 4.3 The Inverse Surgery: Recovering 𝝅 \boldsymbol{\pi} Why Direct Audit-by-Aggregation is Biased for DMS. 5 Experiments 5.1 Experimental Settings and Metrics 5.2 Baselines 5.3 Results of LLMScan Benchmark 5.4 Ablation Studies 5.5 Controlled and Held-Out Genera`；Evaluation=`arXiv:2605.30348v1 HTML — §3.2 LLMScan: First Benchmark for Data Mixture Surgery; excerpt=overing 𝝅 \boldsymbol{\pi} Why Direct Audit-by-Aggregation is Biased for DMS. 5 Experiments 5.1 Experimental Settings and Metrics 5.2 Baselines 5.3 Results of LLMScan Benchmark 5.4 Ablation Studies 5.5 Controlled and Held-Out Generalization 5.6 Safety Auditing Triage via Toxic Injection 6 Conclusion 7 Limitations and Future Work References A More Experiments Details B Class-wise Detection Error B.1 Coarse-Grained Det`。

Trade-off / failure / fallback：`arXiv:2605.30348v1 HTML — §6 Conclusion; excerpt=ut Generalization 5.6 Safety Auditing Triage via Toxic Injection 6 Conclusion 7 Limitations and Future Work References A More Experiments Details B Class-wise Detection Error B.1 Coarse-Grained Detection Error B.2 Mid-Grained Detection Error B.3 Fine-Grained Detection Error License: CC BY 4.0 arXiv:2605.30348v1 [cs.CL] 28 May 2026 LLMSurgeon : Diagnosing Data Mixture of Large Language Models Yaxin Luo Jiacheng Cui Xi`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30348:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30348:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `TRAIN-DATA` / `books/part-04-training-system/27-data.md` 的当前正文，采用命题与 prior comparison 未变。

### [VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion](https://arxiv.org/html/2605.30351v1)

问题与机制：In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. owner=`MULTIMODAL-GENERATIVE-PARADIGMS`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下继续成立。

Evaluation contract：We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it.。Method=`arXiv:2605.30351v1 HTML — §3 Method; excerpt=rt Issue Back to Abstract Download PDF Abstract 1 Introduction 2 Related Work 3 Method 3.1 Compressed KV Cache Construction 3.2 Decoupled 3D-RoPE 3.3 Training-Time Forward Pass 4 Experiments 4.1 Setup and Dataset 4.2 Main Results 4.3 Ablations 5 Why MLA Works in Video Diffusion: Rank Budget vs. Spectral Structure 6 Limitations and Broader Impact 7 Conclusion References Table of Contents A Videos and Website B Details`；Evaluation=`arXiv:2605.30351v1 HTML — §4 Experiments; excerpt=ed KV Cache Construction 3.2 Decoupled 3D-RoPE 3.3 Training-Time Forward Pass 4 Experiments 4.1 Setup and Dataset 4.2 Main Results 4.3 Ablations 5 Why MLA Works in Video Diffusion: Rank Budget vs. Spectral Structure 6 Limitations and Broader Impact 7 Conclusion References Table of Contents A Videos and Website B Details on User Study C Background C.1 Wan2.1-T2V-1.3B Backbone D Implementation Details D.1 Backbone and`。

Trade-off / failure / fallback：`arXiv:2605.30351v1 HTML — §6 Limitations and Broader Impact; excerpt=ations 5 Why MLA Works in Video Diffusion: Rank Budget vs. Spectral Structure 6 Limitations and Broader Impact 7 Conclusion References Table of Contents A Videos and Website B Details on User Study C Background C.1 Wan2.1-T2V-1.3B Backbone D Implementation Details D.1 Backbone and Tokenization D.2 VideoMLA Block D.3 NoPE/RoPE Split and 3D RoPE D.4 Chunk-Causal Sliding-Window Attention D.5 Long-Horizon RoPE Re-indexin`。未披露的 model、hardware、precision、length、batch、concurrency、SLO、seed 与 evaluator 记为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-30351:start -->只接受 exact-v1 披露机制与实验边界，不将作者 benchmark 外推为跨模型、跨硬件或生产结论。<!-- claim:SF-2026-ARXIV-2605-30351:end -->

**当前 Books 投影。** `No Change — Existing Coverage`；已复核 `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的当前正文，采用命题与 prior comparison 未变。

### [Task-Focused Memorization for Multimodal Agents](https://arxiv.org/html/2605.31075v1)

Seed 官方 `ArticleMeta.PublishDate=1779984000000` 对应 `2026-05-29T00:00:00+08:00`；该官方事件拥有本日归属，arXiv v1 是同一 Source Family 的机制证据，不在 823 个本日 arXiv batch identity 中另计。v1 页面在审阅时无 withdrawn 标记。

TaskMem 把 streaming episodic-memory generation 分成两阶段：Phase One 用 RL 优化 fidelity、coherence、non-redundancy、format 与 richness；Phase Two 固定基础策略，对每个 context 采样八个候选，用近期环境问题构造顺序互换的一致 pairwise preference、删除 cycle，再以 DPO 训练轻量 adapter。Recent tasks 只提供 relevance proxy，writer 只提出写入内容；provenance、authorization、conflict 与 durable commit 仍属于 Memory 系统。

作者结果绑定 Qwen3-VL-30B-A3B、VideoMME/EgoLife/EgoTempo、32×80GB GPU 训练与 GPT-4o/Gemini learned judges；GPU 型号、精度、在线 latency/concurrency/SLO 未披露，Phase Two 只有约 100 videos 形成有效偏好对。不能外推为生产 memory、真值判定、semantic/visual memory 或 embodied safety。

**当前 Books 投影。** `Applied` 到 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；paired binding 位于机制正文且早于 Review notes，保留 task adapter drift、future-task forgetting、authority separation 与 general-policy/raw-evidence fallback。

### 本轮自然日增量证据（2026-10-21）

以上连续旧证据块仅属原冻结小时窗，其有效审阅复用，不因补查重读；以下52家族按当前贡献门与必要证据分层处理。49个arXiv v1的日期联合界见两个DataCite原字段文件；Google29729、Opus与Kimi分别由官方May28公开页/发布记录定日。当前版本号变化不自动替换精确v1或触发全史比较，具体重要纠错只影响对应命题。下列“已整合/已有覆盖”均指root实际完成的具名层，不把题摘校准当Source或POST。

### [UNIQUE: Universal Top-k Sparse Attention for Training-free Inference and Sparsity-aware Training](https://arxiv.org/html/2605.27740v1)

均值页摘要遗漏尖峰→query-scaled dispersion提议稀疏读；softmask另需训练。全KV驻留与全页评分仍付费；当前k/k+1中点stop-gradient不是跨step固定；page/token预算冲突不合成速度质量保证。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-text-2605.27740v1.txt)与[本日作者A4](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[INFER-KV-CACHE/Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [ConvMemory: A Lightweight Learned Memory Reranker, a Negative Attribution Result, and a Research-Preview Conflict Editor](https://arxiv.org/html/2605.28062v1)

dense排名邻域不等时间轴；重训对照修正temporal收益归因。五seed temporal-hop区间跨零，非时间对照收益更大；只支持LoCoMo受限负归因，不否定所有时间学习，也不授最终QA省费。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-text-2605.28062v1.txt)与[本日作者A4](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[AGENT-RAG/Ch76](../../../../books/part-07-agent/76-rag.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [From Pixels to Words -- Towards Native One-Vision Models at Scale](https://arxiv.org/html/2605.28820v1)

原生多模态显式visual-unit因果接口与THW时间身份。继承Qwen3/prebuffer不等从零；unit内双向、跨unit/文字因果，更多交互交换训练/序列成本，有限预算非native普胜。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-text-2605.28820v1.txt)与[本日作者A4](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[MULTIMODAL-REPRESENTATION/Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [PrunePath: Towards Highly Structured Sparse Language Models](https://arxiv.org/html/2605.28283v1)

累计质量动态选expert与渐进稀疏的有限预算取舍。严格sum<阈值加top1不同于标准top-p，softmax选集/sigmoid输出与decode-only成本分账；Ch21 variable-k已承载平均预算非局部load保证。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28283v1.txt)与[本日作者A5](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[MODEL-MOE/Ch21](../../../../books/part-02-model/21-moe.md)的具体承载与局部比较见作者A5，root已实际独核；本次不为制造diff再写。

### [Compositional Generalization in Autoregressive Models via Logit Composition](https://arxiv.org/html/2605.28304v1)

固定独立token-mask条件下组合专家logits的足够条件。common support、区外等于background及factorization不可省；不采用任意feature等价推广/weight arithmetic，数学反退、EOS和多模型费用保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28304v1.txt)与[本日作者A5](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[MODEL-SAMPLING/Ch20](../../../../books/part-02-model/20-sampling.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Models That Know How Evaluations Are Designed Score Safer](https://arxiv.org/html/2605.28591v1)

参数化protocol-trait曝光可改安全分数且无需显式测评自述。matched FineWeb与Nemotron不同控制分开；非verbal子人口不是内因随机干预，缺deployment对照，不证明inflation或真实alignment未提高。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28591v1.txt)与[本日作者A5](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [The Attentional White Bear Effect in Transformer Language Models](https://arxiv.org/html/2605.28639v1)

词汇抑制不等敏感概念表征或后续语义信号已消。65/35/三seed仅probe与lexically-compliant人口，语义近邻不是秘密恢复，aggregate routing p=.55；Ch5读出vs使用及局部因果已有承载。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28639v1.txt)与[本日作者A5](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[WORLDVIEW-REPRESENTATION/Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)的具体承载与局部比较见作者A5，root已实际独核；本次不为制造diff再写。

### [Off-Policy Learning to Reason Works Because It Is More Pessimistic Than You Think](https://arxiv.org/html/2605.28150v1)

ratio-free off-policy替代目标的baseline平移与pessimism条件。weightedMLE加句级logratio²的stationary条件不保证共享网络收敛，finiteG不等population；并非原PG无偏或无IS通用更好。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28150v1.txt)与[本日作者A5](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [The Importance of Being Statistically Earnest: A Critical Re-evaluation of GSM-Symbolic](https://arxiv.org/html/2605.28700v1)

模板聚类与数值人口重审GSM-Symbolic反证。100模板×50非5000独立题，GLMM/多重比较不识别内部根因，不显著非equivalence；Ch66 clustered单位与固定预算已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28700v1.txt)与[本日作者A5](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A5，root已实际独核；本次不为制造diff再写。

### [ROSD: Reflective On-Policy Self-Distillation for Language Model Reasoning across Domains](https://arxiv.org/html/2605.28014v1)

有正确参照的反射quote仅定位可错局部蒸馏起点。错误轨迹匹配quote后suffix/匹配失败全段、正确轨迹全token；并非首错oracle，OOD低于GRPO和额外teacher费保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28014v1.txt)与[本日作者A6](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Mechanistically Interpreting the Role of Sample Difficulty in RLVR for LLMs](https://arxiv.org/html/2605.28388v1)

非零组调幅与零方差组换feature evaluator须分责。全同binary reward时是真实引入TSAE新feedback人口，不是恢复binary真值；ReasonScore相关非因果，basis版本与独立outcome保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28388v1.txt)与[本日作者A6](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation](https://arxiv.org/html/2605.28222v1)

等参数q/v与全attention的局部结构取舍。8对仅2显著、6CI跨零不证等价/普遍结构优势；单A100/B1整RAG阶段不授线上SLO；Ch30 rank与module分别控制已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28222v1.txt)与[本日作者A9](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[TRAIN-LORA/Ch30](../../../../books/part-04-training-system/30-lora.md)的具体承载与局部比较见作者A9，root已实际独核；本次不为制造diff再写。

### [Beyond pass@k: Redundancy-Aware RLVR for Multi-Sample Code Generation](https://arxiv.org/html/2605.28022v1)

固定多样本预算内LOO集合credit减少代码冗余。JPlag结构相似非语义真值，集合效用不同于独立sample正确率，diversity-only质量崩；Ch33集合身份/LOO信用已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28022v1.txt)与[本日作者A6](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)的具体承载与局部比较见作者A6，root已实际独核；本次不为制造diff再写。

### [AdaDPO: Self-Adaptive Direct Preference Optimization with Balanced Gradient Updates](https://arxiv.org/html/2605.28440v1)

两概率坐标与reference-ratio坐标的梯度平衡不能混同。Eq8双严格约束仅受限reference相等才兼容；实际lengthnorm/clip改变目标，有限配方保留，Ch34 gradient/scale已承载。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28440v1.txt)与[本日作者A6](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[TRAIN-DPO/Ch34](../../../../books/part-04-training-system/34-dpo.md)的具体承载与局部比较见作者A6，root已实际独核；本次不为制造diff再写。

### [Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents](https://arxiv.org/html/2605.28532v1)

工具遮蔽的可行性标签需独立验证依赖与替代路径。successful-trace交集只提议依赖，closed工具集仍不证infeasible；91%无需tool不证明污染，不同人口token均值不授因果节费。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28532v1.txt)与[本日作者A9](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies](https://arxiv.org/html/2605.28527v1)

冻结VLA的value-like读出与online selector归因分开。online逐16候选模拟success优先/否则reward+probe，不是纯probe且baseline无同oracle；success/time标签非Bellman，Ch26排序/仿真/执行gate已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28527v1.txt)与[本日作者A9](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[MULTIMODAL-EMBODIED-VLA/Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)的具体承载与局部比较见作者A9，root已实际独核；本次不为制造diff再写。

### [Self-Consistency via Marginal Sharpening](https://arxiv.org/html/2605.28142v1)

答案边缘分布取幂不同于完整trajectory取幂。integer traces扩张是目标恒等，局部解码丢future normalizer仍近似；answer-string不是语义oracle，32trace/多forward与majority反侧保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28142v1.txt)与[本日作者A9](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[MODEL-SAMPLING/Ch20](../../../../books/part-02-model/20-sampling.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Transformers Provably Learn to Internalize Chain-of-Thought](https://arxiv.org/html/2605.28600v1)

受限parity结构的CoT内部化充分例不等LLM总费下降。position-only/identityV/特制非线性/levelmask及随B扩d均有条件，zero-pad scratch仍计算；Ch18 codec/内部transition成本与taskstate已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28600v1.txt)与[本日作者A9](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[MODEL-DECODER-ONLY/Ch18](../../../../books/part-02-model/18-decoder-only.md)的具体承载与局部比较见作者A9，root已实际独核；本次不为制造diff再写。

### [Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR](https://arxiv.org/html/2605.28295v1)

首semantic-token均匀无放回分支改变rollout人口。top20选4再续写不恢复原iid/onpolicy，低token负载非无因果；N/K增大不总更好，所有rollout与reweight资格分账。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28295v1.txt)与[本日作者A7](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [The Abstraction Gap in Vision-Language Causal Reasoning](https://arxiv.org/html/2605.28779v1)

解释文本与causal-chain输出的差额不能认证内部faithfulness。不同任务/评分对象与judge依赖保留；Gemini8.60/8.46和AG=-.006按Eq1不一致不采用，Ch66输出合同/因果识别已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28779v1.txt)与[本日作者A8](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A8，root已实际独核；本次不为制造diff再写。

### [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/html/2605.28365v1)

partial Lean证据与选择性风险需覆盖及faithfulness资格。未证rival是unresolved非负标签，IID/frozenpipeline/devcal隔离只授accepted人口风险；Ch66 intent/spec和partialcoverage已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28365v1.txt)与[本日作者A7](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A7，root已实际独核；本次不为制造diff再写。

### [Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts](https://arxiv.org/html/2605.28042v1)

translation calibration的expert裁剪/恢复有局部容量条件。routingmass/动态JS非因果贡献，successful-output子人口不证知识全保，恢复训练/serving费分开；Ch21静态artifact与外域质量已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28042v1.txt)与[本日作者A8](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[MODEL-MOE/Ch21](../../../../books/part-02-model/21-moe.md)的具体承载与局部比较见作者A8，root已实际独核；本次不为制造diff再写。

### [Understanding Generalization and Forgetting in In-Context Continual Learning](https://arxiv.org/html/2605.28705v1)

线性/掩码attention的受限context干扰与遗忘分解。unmasked linear顺序无关，masked才有该顺序论证；Ft是新旧预测平方差非真实增误；Ch8固定θ/Ch22干扰已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28705v1.txt)与[本日作者A7](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[MODEL-LONG-CONTEXT/Ch22](../../../../books/part-02-model/22-long-context.md)的具体承载与局部比较见作者A7，root已实际独核；本次不为制造diff再写。

### [Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use](https://arxiv.org/html/2605.27788v1)

工具raw transient与persistent extraction的critic消费分工。γ1/terminal-only下boundary差可望远镜，segment广播不证原clipped参数梯度等价；critic warmup/五次MC proxy/工具KV恢复费保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27788v1.txt)与[本日作者A7](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-PPO/Ch32](../../../../books/part-04-training-system/32-ppo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Thinking as Compression: Your Reasoning Model is Secretly a Context Compressor](https://arxiv.org/html/2605.28713v1)

task/budget条件reasoning trace可作有损上下文压缩。硬截B后才交frozenconsumer，antiHack非已验安全；LoCoMo更高压缩但质量反退，所谓E2E未含compressor；Ch75 derivedview/raw与全费已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28713v1.txt)与[本日作者A8](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[AGENT-CONTEXT/Ch75](../../../../books/part-07-agent/75-context.md)的具体承载与局部比较见作者A8，root已实际独核；本次不为制造diff再写。

### [Multi-Mixer Models: Flexible Sequence Modeling with Shared Representations](https://arxiv.org/html/2605.28769v1)

序列轴共享KV的双mixer选择仍需两份state持续推进。Q独立/WGWO共享，chunk兼容训练与静态assignment非动态router；KV完整驻留、不同LR/2K与切换方向失败保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28769v1.txt)与[本日作者A7](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[MODEL-LONG-CONTEXT/Ch22](../../../../books/part-02-model/22-long-context.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Bridging the Detection-to-Abstention Gap in Reasoning Models under Insufficient Information](https://arxiv.org/html/2605.28070v1)

同回答显式检测与最终拒答的conditional控制缺口。A@D用joint/DR，只在特殊拒答子集可替OAR/DR；训练format非runtime硬gate/内省真值，正常题反退与长度差保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28070v1.txt)与[本日作者A8](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [CIRF: Tokenizing Chain-of-Thoughts into Reusable Functional Units for Efficient Latent Reasoning in Large Language Models](https://arxiv.org/html/2605.28292v1)

分段VQ functional-token与扩展词表是训练接口而非真实算子。optional result来自训练gold及greedy删减非全局，几何分散非faithfulness；Ch18 codec/checkpoint/显式读出与CoT退路已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28292v1.txt)与[本日作者A8](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[MODEL-DECODER-ONLY/Ch18](../../../../books/part-02-model/18-decoder-only.md)的具体承载与局部比较见作者A8，root已实际独核；本次不为制造diff再写。

### [Skill-Conditioned Gated Self-Distillation for LLM Reasoning](https://arxiv.org/html/2605.28791v1)

弱PI teacher支持/抑制极性由外部outcome门控。top8同权重teacher/retrieval非truth，有符号r/neutral/commonwrong保留，有界scalar非参数梯度保证，best-test-checkpoint选择和全词表费保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28791v1.txt)与[本日作者A8](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Agentic Separation Logic Specification Synthesis](https://arxiv.org/html/2605.27531v1)

逻辑selector与fuzz反例过滤不证明最强语义规范。结构lattice/fuzz无反例与真实intent分开，unit survivors仍可被fuzz推翻；Ch66 intent/spec/proof/独立tests已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27531v1.txt)与[本日作者A10](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A10，root已实际独核；本次不为制造diff再写。

### [Why LLMs Fail at Causal Discovery and How Interventional Agents Escape](https://arxiv.org/html/2605.27567v1)

挑战observational causal learning的中心kernel/查询收敛主张。D2漏norm差项的φ+=e/φ−=.5e反例击穿δ0 bound；D4缺各wrong获区分query/噪声集中，不用LLM口头do替真实干预；中心隔离不进Books。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27567v1.txt)与[本日作者A10](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。中心定理及查询条件争议经root独核成立；保持候选与7分，不作正面证据、不入Books。

### [You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents](https://arxiv.org/html/2605.27586v1)

少数训练seed经交互影响未更新peers的替代分工。mute/remove/topology/scaling支持局部行为传播，不等永久参数alignment/开放群体门槛；恶意规范/外部权限和生成训练交互费用保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27586v1.txt)与[本日作者A10](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[AGENT-MULTI-AGENT/Ch82](../../../../books/part-07-agent/82-multi-agent.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Long Live the Librarian! A Persistent Search Sub-Agent for Energy-Efficient Multi-Agent Software Engineering Systems](https://arxiv.org/html/2605.27787v1)

持久导航角色的freshness与pointer工具物化分工。consumer仍读snippet/prefill，search-only prompt非只读权限；B200/cache条件与NVML/OLS归因不授通用单token能耗因果。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27787v1.txt)与[本日作者A10](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[AGENT-MULTI-AGENT/Ch82](../../../../books/part-07-agent/82-multi-agent.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Revealing Algorithmic Deductive Circuits for Logical Reasoning](https://arxiv.org/html/2605.27824v1)

配对patch与跨题消融支持局部推理head参与而非完整算法。合成logit/最终accuracy不同人口，约3%attention-only不排MLP与替代回路；Ch5读出vs使用/跨construction局部因果已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27824v1.txt)与[本日作者A11](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[WORLDVIEW-REPRESENTATION/Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)的具体承载与局部比较见作者A11，root已实际独核；本次不为制造diff再写。

### [CAREF: Calibration-Aware Regularization for Explanation Faithfulness Without Rationale Supervision](https://arxiv.org/html/2605.27835v1)

非加性entropy/sparsity目标只改变概率形状不认证faithfulness。绝对p log(p/U)令α1β0不一般等KL；FlanT5/FEB/nBERT与人审有限，Ch29概率目标/label smoothing不保校准已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27835v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[TRAIN-SFT/Ch29](../../../../books/part-04-training-system/29-sft.md)的具体承载与局部比较见作者A13，root已实际独核；本次不为制造diff再写。

### [When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness?](https://arxiv.org/html/2605.27932v1)

固定恶意query下工具前缀及局部activation影响ASR。返回图/textprior对照与heldout干预仅部分支持，无充分adaptive/benignutility；Ch72版本化pipeline/局部干预与效用边界已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27932v1.txt)与[本日作者A11](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-SECURITY/Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)的具体承载与局部比较见作者A11，root已实际独核；本次不为制造diff再写。

### [Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents](https://arxiv.org/html/2605.27955v1)

typed child合同需与父流程原actiontemplate成对呈现。四checks非语义等价，BE/RC仍LLM，invoke不是runtimecall；20题/10题反侧、30synthetic negatives与构建成本保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.27955v1.txt)与[本日作者A11](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[AGENT-TOOL-CALLING/Ch78](../../../../books/part-07-agent/78-tool-calling.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [VCap: Hypergeometric Rewards for Weak-to-Strong Visual Captioning](https://arxiv.org/html/2605.28023v1)

参考只提出probe槽，原视觉裁决可推翻参考错误。MLLM不是无误adjudicator，uniform/exchangeable理论不保真实训练收敛；槽外遗漏/选择偏差、e1/e2重训与有限lesion反侧保留。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28023v1.txt)与[本日作者A11](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-GRPO/Ch33](../../../../books/part-04-training-system/33-grpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Explaining is Harder Than Predicting Alone: Evaluating Concept-based Explanations of MLLMs as ICL Visual Classifiers](https://arxiv.org/html/2605.28215v1)

更复杂解释格式的决策退化与解释质量需分验。E1–E5变输出义务，judge缺supportset/LD依prior，聚合非逐模型单调，4×26 caption口径不闭；Ch66输出合同/spec已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28215v1.txt)与[本日作者A12](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A12，root已实际独核；本次不为制造diff再写。

### [AI, Take the Wheel: What Drives Delegation and Trust in Human-Computer Cooperative Question Answering?](https://arxiv.org/html/2605.28255v1)

未见proposal前自主授权与见后adoption是两时点。mute仍保建议，human初答/揭示/最终选择分开；重复人队决策与观测性不授阈值/因果，agreement/confidence非权限。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28255v1.txt)与[本日作者A12](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[AGENT-PLATFORM/Ch84](../../../../books/part-07-agent/84-agent-platform.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Entropy-aware Masking for Masked Language Modeling](https://arxiv.org/html/2605.28526v1)

MLM选位producer的full-input entropy与teacherwarmup/selfmask。unmasked score非已mask难度，coldstart退化，15%/五策略/两小模型两seed；Ch27sampler/checkpoint/history/人口分责已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28526v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[TRAIN-DATA/Ch27](../../../../books/part-04-training-system/27-data.md)的具体承载与局部比较见作者A13，root已实际独核；本次不为制造diff再写。

### [Cultural Binding Heads in Language Models](https://arxiv.org/html/2605.28543v1)

identity-item配对与edgeKO支持partial bindinghead作用。66items/五fold/同层random及scale有限，S不等accuracy/文化真值，77–91%未解释/Llama反侧；Ch5局部因果/读出vs使用已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28543v1.txt)与[本日作者A12](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[WORLDVIEW-REPRESENTATION/Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)的具体承载与局部比较见作者A12，root已实际独核；本次不为制造diff再写。

### [Satisfiability Solving with LLMs: A Matched-Pair Evaluation of Reasoning Capability](https://arxiv.org/html/2605.28602v1)

solver验证SAT/UNSAT最小编辑对需双正确并另验witness。ADR不识别内部solver/排所有shortcut，representation一致不证真实求解，timeout人口/成本分开；Ch66配对响应vs正确/decision-witness已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28602v1.txt)与[本日作者A12](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A12，root已实际独核；本次不为制造diff再写。

### [GraphSteal: Structural Knowledge Stealing from Graph RAG via Traversal Reconstruction](https://arxiv.org/html/2605.28645v1)

GraphRAG回答可泄露跨query累积结构而非仅独立PII。受限子图/NRR-MCS-GED/大图topK瓶颈，90%非全网秘密恢复；Ch72 topology跨调用与selected/recovered单位已有覆盖，防御建议非已验。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28645v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-SECURITY/Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)的具体承载与局部比较见作者A13，root已实际独核；本次不为制造diff再写。

### [Interpretability-Guided Layer Selection over Subspace Projection: SAEs as Stethoscopes, Not Scalpels, for Raw Task Vector Model Editing](https://arxiv.org/html/2605.28649v1)

SAE可诊断选层，但weight增量过滤需独立坐标映射。原projection标量无lift不录recipe，normratio非平方energy；单Gemma/NT、搜索与统计局限不授一般不相容或所有SAE失效。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28649v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-LORA/Ch30](../../../../books/part-04-training-system/30-lora.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Activation Steering for Synthetic Data Generation: The Role of Diversity in Downstream Safety Detection](https://arxiv.org/html/2605.28664v1)

steering生成成功/coherence/diversity与下游检测utility分开。同negative替换positive的有限AUROC，main29/112非多数普胜，toxicity反退/HM只是相关；Ch27集合多样性与独立下游已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28664v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[TRAIN-DATA/Ch27](../../../../books/part-04-training-system/27-data.md)的具体承载与局部比较见作者A13，root已实际独核；本次不为制造diff再写。

### [Code as a Weapon: A Consensus-Labeled Prompt Bank for Measuring Coding-Model Compliance with Malicious-Code Requests](https://arxiv.org/html/2605.28734v1)

promptbank新release中provider403改变judge可用人口。沿用03179旧分类不重复新贡献；ERROR非KNOWLEDGE/安全拒绝，四/五panel与κ人口分开；Ch66缺答Unknown/subject-adapter身份已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28734v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A13，root已实际独核；本次不为制造diff再写。

### [Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents](https://arxiv.org/html/2605.28775v1)

teacherstate重采rejected，按function/args差异选择DPO损失。固定preadaptstudent，reasoning排直接loss仍作prefix，teacher差异非唯一错误真值，mask不保共享参数行为；普通可靠pairs共存。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28775v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已整合到[TRAIN-DPO/Ch34](../../../../books/part-04-training-system/34-dpo.md)相应机制段（非章末摘要），必要源/具体差额及实际POST均由root通过。

### [Personal Visual Memory from Explicit and Implicit Evidence](https://arxiv.org/html/2605.28806v1)

个人视觉证据pending后再解释/结构写入而非立即caption事实化。合成人设/多选/内部confirm非真实ownership，tokens只answerercontext；Ch77 raw/pending/逐fact可撤销admission已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.28806v1.txt)与[本日作者A13](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[AGENT-MEMORY/Ch77](../../../../books/part-07-agent/77-memory.md)的具体承载与局部比较见作者A13，root已实际独核；本次不为制造diff再写。

### [Realistic honeypot evaluations for scheming propensity](https://deepmind.google/research/publications/253391/)

真实代码副本机会式honeypot与promptedorganism的测量权限。官方May28先公开；simulation非production，CoTtrigger与bug/意图分开，零观察不授部署0风险；Ch66真实vs模拟/自发vs构造已有覆盖。 精确v1必要方法、关键对照/反侧及采用域见[原件](../_sources/daily-20260529/supp-core-2605.29729v1.txt)与[本日作者A14](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。已有覆盖：[PLATFORM-EVALUATION-SYSTEM/Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的具体承载与局部比较见作者A14，root已实际独核；本次不为制造diff再写。

### [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)

仅采用官方May28 news的Messages API新合同：可信开发者可用后续system entries更新运行中的权限、budget和环境，保先前prefix；不等于改旧bytes/任意cache兼容或prompt取得执行授权。已在[AGENT-CONTEXT/Ch75信任分类末句后](../../../../books/part-07-agent/75-context.md)落实，root实际必要Source/owner/POST通过。营销性能、四倍诚实及卡摘要中的精确OSWorld数不采用；news脚注只支持评价合同改变须重验可比性。必要原件与card非原页转录限制见[作者A14](../_sources/daily-20260529/SUP_SOURCES_20261021.md)及[官方核心返回](../_sources/daily-20260529/supp-opus-fgf-web.txt)，不声称实现已验或实验复现。

### [Kimi Code v0.5.0](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)

May28版本记录明确自然语言scheduled tasks与/auto自动处理tool approvals且不再提问，改变无人值守交互合同。只采这一短核心的版本事实，不从后续文档补造当日持久化、runtime实现、权限阈值或安全保证；没有本地试运行。root实际打开目标版本核心并通过必要接口/安全域审阅；仅报告，因未披露的新实现不改变Ch84/Ch75既有授权与执行分权。原入口/日期邻接与采用限制见[作者A14](../_sources/daily-20260529/SUP_SOURCES_20261021.md)。

## 5. 缺口与下一步

本轮普通扫描、题摘贡献门、必要Source、具体Books决定、23项真实写后检查与本版六部分root DAY均已通过，普通研究/Books待办为0。以下为本窗终态保留项，不作正面证据、不入Books、不支持完整Coverage、无遗漏或性能/安全保证：

- OpenAI / SRC-OPENAI：必查Research/RSS历史索引访问失败，目标官方核心FGF已读且贡献前关闭，不受索引缺口否定；索引覆盖仍受阻，不以限域搜索推零。终态保留项的定点重开条件是可读官方May28索引/RSS或具名漏项正文，只重开该切片；不用于正面证据、Books或无遗漏断言。
- Meta / SRC-META-AI：官方Research SPA/Publications历史日切片未恢复，异常45chars响应与限域搜索不能证明零研究。需要可读May28官方list/API、可重放分页或具名同日官方正文；重开只查该日期/入口，不遍历历年库存。
- Hunyuan / SRC-TENCENT-HUNYUAN：默认en9不代表Research全部；最后实际All renderType0/zh/pageNum1/pageSize1000返回当前11条（totalNum11），显示日期July6→May21→Apr30，三日期字段均无May28，不新增候选。当前All已恢复，剩余只隔离现站不能证明旧Research隐藏/删除历史全集的覆盖限制；重开需可核目标日的旧官方档案或具名原稿，不再猜测其他分组/遍历全站。原始publicAt/publishedAt/displayPublishTime保留各自身份，不以Hy3preview后端/显示日期差异补造旧公开日期。
- [A-CBO / 2605.27567v1](https://arxiv.org/html/2605.27567v1)：D.2在仅norm上界与normalized similarity下漏掉norm差，φ+=e、φ−=.5e、δ=0的合法反例破坏所写bound；D.4缺实际区分query/每个wrong候选与噪声集中条件。保7分候选和争议，但中心obstruction/logn收敛/必要充分escape不正面采用。重开需精确修订的定理假设/证明及oracle信息与有限噪声/query规则，不以局部benchmark替理论修复；[必要原证](../_sources/daily-20260529/supp-acbo-appendixD-necessary.txt)已保存，root实际争议核验通过。

原两个Google date-only请求已按自然日处理：Gram同事件有效去重、honeypot官方May28先公开，未再要求时分秒。MiMo原无日期卡已核Sep27窗外；旧[materials-request-v3.json](../_sources/daily-20260529/materials-request-v3.json)只保历史范围，不是本轮现行待办。Opus卡摘要不是原页转录，其精确OSWorld数字不采用；所采API合同只依赖官方news，本轮不为未采用数字扩读整卡。CAGE/CAREF/SAE等局部公式或归因争议已在各条中收窄，不用删候选/降分代审阅。

窗外线索（不属于本窗、不阻塞本日）：[RADAR / 2605.30208](https://arxiv.org/abs/2605.30208)的arXiv v1提交May28 16:44Z，公告最早May29北京时间；未恢复更早具名官方正文，第三方May28日期不替公开日，仅留待真实归属日恢复，不在本轮读全文/评分。原116候选归属按用户授权保持，不据自然日补查搬移旧事件。

## 6. 复核

复核者：root（独立非报告作者；supp_may29_author为本日唯一作者）

结论：通过

单篇必要层、23真实POST与本版六部分整体DAY均实际通过，依据R1–R20；root已在R21实际读回保存完成态并通过有限FINAL，本日作者ownership及全部窄位释放。

root已实际完成首批准入校准、后续全部拟入选的必要Source与日期/身份层、具体owner比较、23项真实正文/完整直接两侧/本人注POST，并在R20实际通过当前六部分整日验收及Hunyuan All/zh差额、R21实际通过保存态有限FINAL；记录在[唯一独立复核R1–R21](../_sources/daily-20260529/SUP_REVIEW_20261021.md)。代表排除实际包括27636/27916/28400/28317、GoogleI/O/FGF、GUI28534及fourth组合EX/两个决定门；宽列表只作主题线索，不声称逐项全量验证。其余明确排除按已记录主题/理由有限抽检，未读取无关全站论文/全部附录。原116有效层复用，旧[最终非作者复核](../_sources/daily-20260529/FRESH_NONAUTHOR_V3_FINAL_PASS_20260916_R3.md)只证明其原小时窗，不替代本轮DAY。

本版已运行唯一当前V3格式校验通过：168唯一URL/家族，新增52=23整合+27已有覆盖+1仅报告+1争议；审阅35深入/16标准/1争议。原116完整行逐行同序，SHA256为b5425c75b435f419457ec8120e688d33e590ebe0ff8493dc8b8631032b3d3606；连续原§4 252787 Unicode字符/279305 bytes，SHA256为299412455ef1248a674d44a1365500ec31d13c35a779868b7ef787cf760662da，仍逐字连续存在。补查前真实原档案SHA256与启动基线bb6d8b0ab2a745f835099707a262df7163562ede636968a9eb5cedf2efe008a5一致。README/作者SUP的396条本地引用检查无缺失；限定working/cached差额检查通过。机器结果不代语义验收，不将并发index称为干净。本方不stage/commit/push，不改合同、脚本、索引或LEARNING_STATE。
