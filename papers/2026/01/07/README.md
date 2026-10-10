# Daily Research — 2026-01-07

**规范：** V3
**窗口：** 2026-01-06T09:00:00+08:00 ～ 2026-01-07T09:00:00+08:00
**补充窗口：** 2026-01-06 ～ 2026-01-06
**窗口说明：** 用户明确授权保留原窗口和已有候选日期，只补遗漏；新增材料按前一完整北京时间自然日补查，原材料仅去重且不搬归属。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T14:58:00+08:00

用户授权说明：本轮只补查遗漏，补充窗口为北京时间2026-01-06完整自然日；原窗口及已存在51个家族的日期、评分、有效审阅、Books结果和争议均保留，不搬候选、不从旧Weekly建池。下述原窗口历史验收不代替本轮非作者终态复核。

## 1. 结论

本轮14个每日源均执行有限补查，其中11项已检查，Google/Meta必要日级入口及arXiv9项必要公开日期受阻；实际完整读16个具名题摘。独立贡献校准保留9项潜在增量的日级公开证据请求，6项贡献前关闭及1项旧事件线索；9项未证明属于补充Jan06，均隔离而不并入原51候选，不评分、不写Books。本轮0新增确定候选、0新增完整证据审阅、0新增Books；不是“本日没有遗漏”。root非作者复核通过， ordinary待办已处理到安全终态，具体范围与恢复点见[补查证据](../_sources/daily-20260107/supplement-20261007.md)。

原窗口历史结论（保留）：

本日独立重建完成，冻结51个确定家族：19项实际整合及非作者写后复核通过、4项具体已有覆盖、24项仅报告/低分关闭、4项中心保证隔离。来源有限停止、逐项证据与Books处置、代表性负侧和日级复核已处理，普通待办为0。历史目录与公开事件恢复仍有下述限制，完成不表示这些保留项已获证据支持或互联网上无遗漏。宽metadata不等候选、全文或证据完成；未继承旧日报/Weekly候选或评分，不扫描Weekly组。

## 2. 来源覆盖

下表为本轮实际有界入口、日期切片、查询/返回及停止；必要日级受阻与可完成的有限目录分别记录，不将空检索当零事件。原窗口来源/查询证据继续保存于[原停止记录](../_sources/daily-20260107/source-stop-updates.md)与[原查询记录](../_sources/daily-20260107/queries-and-screening.md)；原候选日期与有效证据不变。

以下为本轮来源记录；原窗口日期切片和有效来源证据由上述原始记录保留。

原日期切片见[切片0](../_sources/daily-20260107/official-date-slices-0.jsonl)/[切片1](../_sources/daily-20260107/official-date-slices-1.jsonl)，旧接口失败不继续作为已恢复入口的本轮状态。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [RSS](https://openai.com/news/rss.xml)1251日期字段；Grove Jan2→Health Jan7→Tolan Jan7，只定位Jan06切片；官方Jan6定点补检应用文章核心无新机制 | 已检查 | 有限feed不证明全机构事件；Health原归属保留 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)174 publishedOn/slug，Dec19 Bloom→Jan8 critical-infrastructure，Jan06切片未定位条目 | 已检查 | 只核有限目录，不声称无隐藏研究 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/publications/)page1首30/total265/9页，Jan9→Dec3；[January Blog](https://research.google/blog/2026/01/)9日期最早Jan12；[pubs](https://research.google/pubs/)年度字段首15 | 受阻 | Blog及DeepMind有限日期段已查，Google年度publication无法确认必要日级公开；需当窗日级目录或具名原事件 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)只有Muse标题，正文25秒超时；publications/page3不可读；Jan6官方域窄检索无结果 | 受阻 | 必要可读日级目录未恢复；空搜索不等零事件，不索全站镜像 |
| SRC-QWEN | [原research-list API](https://qwen.ai/api/page_config?code=research.research-list)完整60个无序date字段，最大Dec23，Jan06切片未定位条目 | 已检查 | 该有限目录不是全机构/所有revision；不再索无具名遗漏的历史快照 |
| SRC-DEEPSEEK | [官方News](https://www.deepseek.com/en/news/)有限10个research日期，Jan12 Engram→Dec31 mHC | 已检查 | 未扩View All全站，其他失败入口不当零 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)26标题、最新Nov7；[Kimi-K2 releases](https://github.com/MoonshotAI/Kimi-K2/releases)没有release | 已检查 | 有限两入口不证明全机构无研究，不审无具名变化的PR |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)经原POST publicList page1/pageSize100/renderType0，total9/list9全部日期字段，最早Feb03 | 已检查 | 只覆盖当前完整有限目录，不授当时无删除档案保证 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)15条Jan13→Dec10/9；[release](https://docs.z.ai/release-notes/new-released)Jan14→Dec22，在跨窗邻接处停 | 已检查 | More未扩全站，有限目录不证明全部渠道 |
| SRC-BYTEDANCE-SEED | [原论文/Blog API](https://seed.bytedance.com/api/get_article_list_v2)type1/2×2026ASC/2025DESC、page0/count20；实际20/0/9/15、total82/94/23/49，next20/has_more；2026最早Jan20/Feb12，2025blog最晚Dec24 | 已检查 | type1-2025两次缺list不当零论文；本窗2026 ASC日期桥接有限，不扩2025库存 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)当前page1/下一页2，Jan8→Dec23邻接 | 已检查 | 仅该有限技术Blog日期段，不扫每周源 |
| SRC-XIAOMI-MIMO | [官网](https://mimo.xiaomi.com/)Paper8/Blog15，原JS688092字符/743278字节、16EN routes；已读frontmatter与v2-flash显式iframe正文Dec16 | 已检查 | 本轮实际有日期材料窗外；无日generic Model Description非贡献，不索全部隐藏路径 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)12/[CN](https://www.minimax.cn/blog)13日期，Jan27/28→Dec23；AgentTech本日有限入口未定位新Jan06条目 | 已检查 | Agent本日原历史日列表未恢复，仅保实际有限停止，不授全机构零事件 |
| SRC-ARXIV | 本轮CL 100相关标题（00557→02670）、DC25、CV25、RO25与LG首100仅发现；按主线题名定点16完整v1题摘，9潜在贡献/6关闭/1旧事件 | 受阻 | 月标题/Submitted/Updated不证明Jan06公开；9具名日级日期隔离，不扩整类题摘队列或授全部revision召回 |

## 3. 候选与判断

本轮9项潜在增量：01280、01624、01299、01584、01500、01712、01046，以及独立补核后的06100、06103。分别涉及memory条件、SFT prefix、rank×bits控制、授权steering、CPU DiT训练、缓存亲和、KV表征，以及linearized Kalman学习边界和后训练重现污染的评价反证；只有具体贡献理由已校准，公开日仍未落实，不先评分或并入下表。6项负侧及1旧事件线索见[逐项筛选与root校准](../_sources/daily-20260107/supplement-20261007.md)，不是按领域、实验规模或已有主题自动排除。

以下是原窗口冻结候选与历史判断（保留）：

以下51家族是有限发现与贡献筛选后的逐项归并，不把宽列表升成队列；已获root独立日级验收。arXiv首公开区间以官方排程/holiday、Submitted缓冲确在上一有效截止之后、首次ID月份与原registered存在的保守上界合取：起点Jan6T01Z，上界由registered原秒向上取整到下一分钟。registered不是public时刻，Submitted/Updated也不是；原字段保存在date-probe-specific/date-fields-E-title，原事件页更早镜像线索与公开revision召回有限，不能据此授无遗漏。Health以官方RSS原发布时间归属。评分对象仅原增量，不借成熟恢复/μP/RL原则抬分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Making MoE based LLM inference resilient with Tarragon](https://arxiv.org/abs/2601.01310v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:31:00+08:00 | stateful AW/KV 与 stateless EW 重放分责，ERT免全communicator恢复；2+2+2=6 | 深入完成 | 整合 `INFER-DYNAMO`：[Ch52 Failure](../../../../books/part-05-inference-system/52-dynamo.md)，root实际写后通过 |
| [Towards a Principled Muon under $μ\mathsf{P}$: Ensuring Spectral Conditions throughout Training](https://arxiv.org/abs/2601.01306v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:31:00+08:00 | 时间轴weight/update谱条件，unique-top/gap约束和rescale净更新区别；3+1+2=6 | 深入完成 | 整合 `TRAIN-PRETRAINING`：[Ch28 optimizer invariant](../../../../books/part-04-training-system/28-pretraining.md)，root实际写后通过 |
| [OrchestrRL: Dynamic Compute and Network Orchestration for Disaggregated RL](https://arxiv.org/abs/2601.01209v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:28:00+08:00 | rollout波前parallel/migration及phase fabric-slack提交分责；2+2+2=6 | 深入完成 | 整合 `TRAIN-DISTRIBUTED-TRAINING`：[Ch36 RL phase](../../../../books/part-04-training-system/36-distributed-training.md)，root实际写后通过 |
| [ChatGPT Health安全contract](https://openai.com/index/introducing-chatgpt-health/) | 2026-01-07T08:00:00+08:00 | 单向敏感memory/context及连接器新scope显式permission；2+2+2=6 | 深入完成 | 整合 `AGENT-MEMORY`：[Ch77 Memory安全](../../../../books/part-07-agent/77-memory.md)，root实际写后通过 |
| [Aggressive Compression Enables LLM Weight Theft](https://arxiv.org/abs/2601.01296v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:30:00+08:00 | 明文失陷后压缩外传与runtime量化恢复约束/取证分责不同；2+2+2=6 | 深入完成 | 整合 `PLATFORM-SECURITY`：[Ch72 Weight Streaming之后](../../../../books/part-06-ai-infrastructure/72-security.md)，root实际写后通过 |
| [FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness](https://arxiv.org/abs/2601.01332v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:31:00+08:00 | checkpoint×TTC与refresh horizon成本联合选择；2+2+2=6 | 深入完成 | 整合 `WORLDVIEW-SCALING-LAW`：[Ch7 N/D/k之后](../../../../books/part-01-worldview/07-scaling-law.md)，root实际写后通过 |
| [Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning](https://arxiv.org/abs/2601.01362v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:32:00+08:00 | 高资源SFT跨语confidence↑与accuracy近不变的设计反证；3+1+2=6 | 深入完成 | 整合 `TRAIN-SFT`：[Ch29 likelihood/entropy之后](../../../../books/part-04-training-system/29-sft.md)，root实际写后通过 |
| [Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage](https://arxiv.org/abs/2601.01685v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:40:00+08:00 | 局部真实片段仍可合谋误导联合belief，同feed报告非独立见证；2+2+2=6 | 深入完成 | 整合 `PLATFORM-SECURITY`：[Ch72 CoT monitor后](../../../../books/part-06-ai-infrastructure/72-security.md)，root实际写后通过 |
| [Confidence Estimation for LLMs in Multi-turn Interactions](https://arxiv.org/abs/2601.02179v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:52:00+08:00 | 逐轮answer/target与evidence身份、正确概率及证据充分性不可合并；3+1+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM`：[Ch66 evidence-shape后](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root实际写后通过 |
| [Routing by Analogy: kNN-Augmented Expert Assignment for Mixture-of-Experts](https://arxiv.org/abs/2601.02144v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:51:00+08:00 | reference优化assignment检索混合替代冻结router，纠正现书logit归属；2+1+2=5 | 深入完成 | 整合 `MODEL-MOE`：[Ch21检索router](../../../../books/part-02-model/21-moe.md)，root实际纠错写后通过 |
| [Guiding Token-Sparse Diffusion Models](https://arxiv.org/abs/2601.01608v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:38:00+08:00 | 同θ/c不同γ的capacity gap提供guidance，不是去条件CFG；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24 guidance成本](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root实际写后通过 |
| [LANCET: Neural Intervention via Structural Entropy for Mitigating Faithfulness Hallucinations in LLMs](https://arxiv.org/abs/2601.01401v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:33:00+08:00 | structural entropy路径干预，但图节点/重叠优先规则影响中心拓扑保证；2+1+2=5 | 争议 | 暂缓：精确图/优先规则重开见§5 |
| [Bayesian Subspace Gradient Estimation for Zeroth-Order Optimization of Large Language Models](https://arxiv.org/abs/2601.01452v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:34:00+08:00 | 跨扰动posterior复用，但cached同观测非独立新增测量；2+1+2=5 | 标准完成 | 仅报告：局部optimizer recipe，不改当前ZO成本/方差解释 |
| [The Two-Stage Decision-Sampling Hypothesis: Understanding the Emergence of Self-Reflection in RL-Trained LLMs](https://arxiv.org/abs/2601.01580v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:38:00+08:00 | decision/sampling梯度归属反证，lexical proxy非内部模块；3+1+2=6 | 深入完成 | 仅报告：受限分析case，不授普遍RL因果 |
| [Can LLMs Track Their Output Length? A Dynamic Feedback Mechanism for Precise Length Regulation](https://arxiv.org/abs/2601.01768v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:42:00+08:00 | 外部count callback替代自估，质量/中断成本须分账；2+1+2=5 | 标准完成 | 仅报告：句界注入recipe，未改变现有feedback/质量控制边界 |
| [UnPII: Unlearning Personally Identifiable Information with Quantifiable Exposure Risk](https://arxiv.org/abs/2601.01786v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:43:00+08:00 | risk-weighted unlearning替代统一权重，PRI非真实exposure；2+1+2=5 | 深入完成 | 仅报告：受限风险重权recipe，不授真实删除或worstcase保障 |
| [COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs](https://arxiv.org/abs/2601.01836v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:44:00+08:00 | org许可/拒绝评价不对称，预过滤部分结果口径冲突；3+1+2=6 | 深入完成 | 仅报告：受限政策评价人口，不授全生产合规 |
| [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:45:00+08:00 | 统一policy操作LTM/STM及分阶段credit，但内容奖励非真值；1+2+2=5 | 标准完成 | 已有覆盖 `AGENT-MEMORY`：[Ch77 typed memory与learned transition](../../../../books/part-07-agent/77-memory.md) |
| [Output Embedding Centering for Stable LLM Pretraining](https://arxiv.org/abs/2601.02031v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:49:00+08:00 | μ-centering与μ-loss分责，但原谱/最大logit普遍界有反例；2+1+2=5 | 争议 | 暂缓：修正h与bound条件/推导后定点重开 |
| [Streaming Hallucination Detection in Long Chain-of-Thought Reasoning](https://arxiv.org/abs/2601.02170v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:52:00+08:00 | 可恢复prefix检测对象替代单step，非内部faithfulness证书；2+1+2=5 | 标准完成 | 仅报告：model-filtered prefix训练case，不改长期faithfulness边界 |
| [DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models](https://arxiv.org/abs/2601.01156v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:27:00+08:00 | target-token loss与防传播mask有增量，但中心反事实loss/准入公式冲突；2+1+2=5 | 争议 | 暂缓：精确公式及实际配置重开见§5 |
| [Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments](https://arxiv.org/abs/2601.01075v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:25:00+08:00 | 群结构latent递归分开known self-action inverse与external velocity；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-WORLD-MODELS`：[Ch25 persistent state](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，root实际写后通过 |
| [Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2601.01618v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:39:00+08:00 | 可编辑ego-view sketch作为action chunk条件，身份/重新生成与controller分责；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-EMBODIED-VLA`：[Ch26 Visual trajectory](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，root实际写后通过 |
| [Beyond Gemini-3-Pro: Revisiting LLM Routing and Aggregation at Scale](https://arxiv.org/abs/2601.01330v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:31:00+08:00 | query-response routing与support-set选aggregator/switch，预生成成本仍在；2+1+2=5 | 标准完成 | 仅报告：局部router recipe，未改变长期质量/成本合同 |
| [Yuan3.0 Flash: An Open Multimodal Large Language Model for Enterprise Applications](https://arxiv.org/abs/2601.01718v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:41:00+08:00 | RAPO first-answer/verify奖励及entropy/negative clipping局部objective；1+1+2=4 | 已关闭 | 仅报告：局部训练recipe，不授内部reasoning因果或全成本优势 |
| [Safety at One Shot: Patching Fine-Tuned LLMs with A Single Instance](https://arxiv.org/abs/2601.01887v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:45:00+08:00 | 少量样本safety patch反证，但gradient rank非全局curvature/安全保证；3+1+2=6 | 深入完成 | 仅报告：受限修补case，不授worstcase恢复 |
| [Tackling the Inherent Difficulty of Noise Filtering in RAG](https://arxiv.org/abs/2601.01896v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:45:00+08:00 | 有限attention/噪声条件与query-first干预，不是所有RAG不可能界；3+1+2=6 | 深入完成 | 仅报告：受限noise-sensitivity case，不改现有retrieval/验收边界 |
| [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:56:00+08:00 | 外部reasoning string干预敏感性不识别内部因果；2+1+2=5 | 标准完成 | 仅报告：受限审计protocol，不授generative faithfulness |
| [DatBench: Discriminative, Faithful, and Efficient VLM Evaluations](https://arxiv.org/abs/2601.02316v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:56:00+08:00 | 生成转换/盲解/标签过滤改变评价人口与estimand；3+1+2=6 | 深入完成 | 仅报告：本suite筛选protocol，不授视觉必要性或新架构泛化保证 |
| [Forget Less by Learning Together through Concept Consolidation](https://arxiv.org/abs/2601.01963v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:47:00+08:00 | set-invariant proxy聚合替代固定顺序concept学习；2+1+2=5 | 标准完成 | 仅报告：局部personalization recipe，不授无遗忘 |
| [Geometric and Dynamic Scaling in Deep Transformers](https://arxiv.org/abs/2601.01014v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:24:00+08:00 | sigmoid coordinate damping组合不等Householder/流形投影；1+1+2=4 | 已关闭 | 仅报告：局部几何recipe未改变当前长期解释 |
| [NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation](https://arxiv.org/abs/2601.02204v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:53:00+08:00 | next-scale历史修正收益取决于accumulated/residual-code输入兼容；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24 AR历史扰动之后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root实际写后通过 |
| [Not All Needles Are Found: How Fact Distribution and Don't Make It Up Prompts Shape Literal Extraction, Logical Inference, and Hallucination Risks in Long-Context LLMs](https://arxiv.org/abs/2601.02023v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:48:00+08:00 | evidence位置/分散与拒答contract改变单取、组合及幻觉评价；2+1+2=5 | 标准完成 | 已有覆盖 `MODEL-LONG-CONTEXT`：[Ch22 有效上下文与证据竞争](../../../../books/part-02-model/22-long-context.md) |
| [ELLA: Efficient Lifelong Learning for Adapters in Large Language Models](https://arxiv.org/abs/2601.02232v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:54:00+08:00 | aggregated past update的坐标shrink替代严格正交，但不是basis-invariant语义去干扰；2+1+2=5 | 标准完成 | 仅报告：有限持续适配recipe，不授无遗忘或零额外state |
| [CD4LM: Consistency Distillation and aDaptive Decoding for Diffusion Language Models](https://arxiv.org/abs/2601.02236v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:54:00+08:00 | paired-view蒸馏与adaptive commit，强制进展不等正确性；2+2+2=6 | 标准完成 | 仅报告：有限training/sampler case，不授全trajectory或approx-KV保证 |
| [GDRO: Group-level Reward Post-training Suitable for Diffusion Models](https://arxiv.org/abs/2601.02036v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:49:00+08:00 | 离线group soft-ranking及top1 likelihood分责，预算/采样人口改变结论；2+1+2=5 | 标准完成 | 仅报告：局部offline objective，不授reward为质量真值 |
| [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:49:00+08:00 | private tests与pass-conditioned style population限制FP测量；2+1+2=5 | 标准完成 | 仅报告：有限测试协议，不授关键词检测为语义purity |
| [VINO: A Unified Visual Generator with Interleaved OmniModal Context](https://arxiv.org/abs/2601.02358v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:57:00+08:00 | frozen VLM/MLP与VAE-MMDiT conditioning局部组合；1+1+2=4 | 已关闭 | 仅报告：局部conditioning recipe未改变长期接口选择 |
| [K-EXAONE Technical Report](https://arxiv.org/abs/2601.01739v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:41:00+08:00 | signed group advantage/长度几何概率与SimPER局部objective；1+1+2=4 | 已关闭 | 仅报告：公开区间仅arXiv v1；更早模型发布未核，不当作新版本事件 |
| [MotionAdapter: Video Motion Transfer via Content-Aware Attention Customization](https://arxiv.org/abs/2601.01955v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:47:00+08:00 | reference形状保留使attention场需target correspondence再warp；2+1+2=5 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24 shared motion](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root实际POST通过 |
| [Correctness isnt Efficiency: Runtime Memory Divergence in LLM-Generated Code](https://arxiv.org/abs/2601.01215v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:29:00+08:00 | normalized shape/DTW不能验已排除capacity失败；3+1+2=6 | 深入完成 | 整合 `PLATFORM-TRACE`：[Ch69 exposure之后](../../../../books/part-06-ai-infrastructure/69-trace.md)，root实际POST通过 |
| [A New Benchmark for the Appropriate Evaluation of RTL Code Optimization](https://arxiv.org/abs/2601.01765v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:42:00+08:00 | 后端优化可能抹掉source改写收益；3+1+2=6 | 深入完成 | 整合 `INFER-TENSORRT-LLM`：[Ch49 lowering之后](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，root实际POST通过 |
| [Luminark: Training-free, Probabilistically-Certified Watermarking for General Vision Generative Models](https://arxiv.org/abs/2601.01085v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:25:00+08:00 | fixed-input/random-key证书不等fixed-key/adaptive输出安全；3+1+2=6 | 深入完成 | 仅报告：受限OR watermark case，不改变现有密钥/检测验收边界 |
| [Warp-Cortex: An Asynchronous, Memory-Efficient Architecture for Million-Agent Cognitive Scaling on Consumer Hardware](https://arxiv.org/abs/2601.01298v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:31:00+08:00 | shared参数/privateKV但TDA覆盖与因果publish未定义充分；2+2+2=6 | 争议 | 暂缓：精确append mask/TDA/publish同步重开，不写Books |
| [RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian](https://arxiv.org/abs/2601.01129v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:26:00+08:00 | comment行动代理与self-selected部署人口限制生产力归因；3+1+2=6 | 深入完成 | 仅报告：受限线上评价case，不授修bug/生产力因果 |
| [LinMU: Multimodal Understanding Made Linear](https://arxiv.org/abs/2601.01322v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:31:00+08:00 | 冻结视觉encoder后decoder替换与初始化不等语义等价；2+2+2=6 | 标准完成 | 仅报告：局部decoder replacement，不改变长期表示/执行接口 |
| [Hidden State Poisoning Attacks against Mamba-based Language Models](https://arxiv.org/abs/2601.01972v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:47:00+08:00 | 有限SSM contraction干预与hybrid恢复反证；3+1+2=6 | 深入完成 | 仅报告：受限state攻击case，不授所有SSM不可逆 |
| [From Failure to Mastery: Generating Hard Samples for Tool-use Agents](https://arxiv.org/abs/2601.01498v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:35:00+08:00 | failure筛选与legal trace重写query改变构造人口；2+2+2=6 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM`：[Ch66 generator/filter/oracle](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CORE: Code-based Inverse Self-Training Framework with Graph Expansion for Virtual Agents](https://arxiv.org/abs/2601.02201v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:53:00+08:00 | executable label/策略图不能认证negative falseaccept或路径时序；2+2+2=6 | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM`：[Ch66 label/path与构造人口](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:55:00+08:00 | progress检查与stop提交分责，reverse动作不是world rollback；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-EMBODIED-VLA`：[Ch26 subgoal stack之后](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，root实际POST通过 |
| [Deferred Commitment Decoding for Diffusion Language Models](https://arxiv.org/abs/2601.02076v1) | 2026-01-06T09:00:00+08:00 ～ 2026-01-06T11:50:00+08:00 | eligible窗口/top1推进与temporary KV刷新分责；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24 confidence之后](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，root实际POST通过 |

## 4. 证据与知识整合

本轮16项完整题摘与两项必要准入核心补读不等16项正文证据审阅；9项潜在增量先隔离公开日，证实属于Jan06后才按精确版本核必要机制/评价与Books差额。T3C证书、steering行动安全、RelayGR通用SLO、DiT-HC全成本、Kalman适用条件及污染研究外推均未被摘要批准。当前没有新增Books判断或写入，下文原有效证据和整合结果不变。

逐项原材料限定如下，独立身份与实际范围见§6。

首批原题摘在[exact-v1-first-screening](../_sources/daily-20260107/exact-v1-first-screening.jsonl)，[日期原字段](../_sources/daily-20260107/date-fields-first.jsonl)只作身份与区间合取材料，不把registered伪装为public时刻。Health核心停点见[公开安全约束](../_sources/daily-20260107/openai-health-admission.md)；WildIng只读决定准入的方法，见[定点记录](../_sources/daily-20260107/wilding-admission.md)，不默认全附件。

### [Making MoE based LLM inference resilient with Tarragon](https://arxiv.org/abs/2601.01310v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01310v1)。

§5.1–5.2/6.1–6.2分开无状态expert确定性重放与stateful attention已提交KV恢复；seq/commit让恢复不落后于提交frontier。§7.1–7.4仅有限Mixtral/H200、单worker fail-stop与SIGINT注入；shadow HBM、store、链路空档付成本，不授Byzantine、store全故障或client stream exactly-once。实际融入Ch52 device-preserving之后、WideEP之前两段（340/342）与末注；root必要原源、owner差异及实际正文/邻接/末注写后通过，未复现。

### [Towards a Principled Muon under $μ\mathsf{P}$: Ensuring Spectral Conditions throughout Training](https://arxiv.org/abs/2601.01306v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01306v1)。

§4.2–4.3/5.1：unique-top、双侧正交补、非负步长ηS≤S−σ₂才保持最大谱范数；并非所有奇异值不变。超宽gap缩小后的rescale改变净更新，不授无条件μP transfer或feature-learning证明。实际融入Ch28固定全谱段之后两段（598/600）及末注；root必要原源、owner差异、实际写后通过，不采用额外§4.4统计recipe。

### [OrchestrRL: Dynamic Compute and Network Orchestration for Disaggregated RL](https://arxiv.org/abs/2601.01209v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01209v1)。

§4.1–4.2/5.1–5.3/6.1–6.3分开波前parallel/migration、load-index排序/KV headroom可行性与phase fabric-slack提交/旧EPS回退。§6实体H800 compute与§7 RLSim fabric不能合成物理OCS已测保证；不采用headline速度/成本数。实际融入Ch36 RL弹性之后两段（1198/1200）及末注；root必要原源、owner差异、实际写后通过。

### [ChatGPT Health安全contract](https://openai.com/index/introducing-chatgpt-health/)

官方核心Memory/connector L77–87允许general→sensitive单向复用，反向conversation/files/memory不继承，connector新域需显式permission。它是公开access/memory约束，不是加密或医疗效果证据；撤未来access≠删除已派生状态是本书工程核验要求，不是作者实现断言。实际融入Ch77 purpose-limited之后一段（1164）及末注；root必要原源、owner差异和实际写后通过。Current July23 availability不作为本窗新增。

### [Aggressive Compression Enables LLM Weight Theft](https://arxiv.org/abs/2601.01296v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01296v1)。

§3.1–3.2/4.2–4.3/5.2–5.3及C/E.1只支持已攻陷明文服务器后的泄漏预算变化：接收端可付继续训练成本，不必维持原低比特推理格式。固定检测概率估算且未计攻击压缩计算，不授真实入侵成功率；QK稳定乘积/基不等单权重稳定，原单层恢复不证明全模型拼接；水印只有限取证且未测对抗移除。实际Ch72 159/161两段及3006注，root必要原源、owner/邻接与实际POST通过，未复现。日期依据为官方缓冲公告/首ID约束、原Submitted与registered区间合取，原字段见date-probe-specific，不把registered当public瞬间。

### [FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness](https://arxiv.org/abs/2601.01332v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01332v1)。

§2–4/Limitations与AppendixA成本口径支持checkpoint、部署到refresh的horizon与TTC策略联合选择。有限质量投影/validation最优筛选可能有偏，pass@k、oracle、真实DVTS/majority选择人口不同，全部生成/verification应计入。主文与AppendixA的Ninfer口径、常数6及成本λ→accuracy跳步不采用，不写92%通用收益。实际Ch7 185一段及278注，root必要原源、owner及实际POST通过；原日期字段合取区间同上，未复现。

### [Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning](https://arxiv.org/abs/2601.01362v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01362v1)。

§3–4.2/Table1与局限：三种2B～8B、MMLU-ProX/GlobalMMLU29/42语言，以候选答案perplexity归一概率而非口头confidence；高资源SFT能跨语提高confidence但未对应accuracy增益。3+1+2=6的Design Delta3针对这个具体反证，不因语言数量计分。LS是有限目标分支，高强度可伤accuracy，不授任意语言/开放生成校准；不采原CE=-KL符号错误或latent因果。硬件/precision Not Disclosed。实际Ch29 94/96两段与1119注，root必要原源、owner及实际POST通过；日期原字段合取区间同上，未复现。

### [Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage](https://arxiv.org/abs/2601.01685v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01685v1)。

§3.3/5.1–5.2/B.3–B.4：局部truthful fragments并不证明联合解释有因果支持，同feed多个报告仍依赖同源。有限CoPHEME/judge模拟不证自然传播率或CoT因果，false/unverified分开。来源ancestry与独立证据检查是工程推断而非已验证防御。实际Ch72 670及3008首注；root必要原源、owner/前后与实际POST通过。日期用具体Submitted缓冲、首次ID公告约束及registered 03:39:36Z合取保守区间，不把registered当public。

### [Confidence Estimation for LLMs in Multi-turn Interactions](https://arxiv.org/abs/2601.02179v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.02179v1)。

§3–4/5.2–5.4：Ptrue与Psufficient的对象不同；固定目标一致线索的实验不能授合法矛盾/改变答案时confidence也必须递增。InfoECE轮次代理不是实际信息量，离线正确且收敛人口不提供在线gold；placebo/同证据summary对照及逐轮成本保留。实际Ch66 1005及4287首注，root必要原源、owner/前后与实际POST通过。registered 03:51:42Z仅合取区间上界线索。

### [Routing by Analogy: kNN-Augmented Expert Assignment for Mixture-of-Experts](https://arxiv.org/abs/2601.02144v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.02144v1)。

§4.1–4.2/Implementation/6.6/Limitations实际value是Top-K softmax assignment，不是优化logits；在线线性混合支持集可扩大，原文没有再Top-K。S1有限优化不证globaloptimal，RBF相似度不是校准正确概率；有标签reference/每层索引/查询与支持扩张dispatch付成本。原2+1+2=5保持，现书logit归属冲突触发深入，不按纠错增加SystemReach。实际Ch21 499/509、图501–507与899首注；root必要原源、具体纠错与POST通过。registered 03:50:50Z仅合取区间上界线索。

### [Guiding Token-Sparse Diffusion Models](https://arxiv.org/abs/2601.01608v1)

必要正文采用 [exact-v1](https://arxiv.org/html/2601.01608v1)。

§3.2/Eq6–8、4.1–4.2/4.4、A.2：同θ/c的强弱γ两支不同于unconditional CFG，random subset/routing回填与mask状态损失分开。双forward、训练compatibility、ω×γ校准、质量多样性及端到端成本不能由attention省算或NFE代替；有限ImageNet/T2I结果不授variance/吞吐普效。实际Ch24 158及1518首注；root必要原源、owner/邻接与POST通过。registered 03:37:44Z仅合取区间上界线索。

### [LANCET: Neural Intervention via Structural Entropy for Mitigating Faithfulness Hallucinations in LLMs](https://arxiv.org/abs/2601.01401v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01401v1) III-B/C、IV-E及有限对照。G只列Nsrc却需下游distance，source α=1/critical α=0重叠优先未明；不能采用完整切断/健康路径不变保证，有限消融不因此全失败。5分标准所需核心已核，中心保证隔离且不写Books；root实际必要原段核通过。恢复仅需图范围/优先规则与决定算法。

### [Bayesian Subspace Gradient Estimation for Zeroth-Order Optimization of Large Language Models](https://arxiv.org/abs/2601.01452v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01452v1) §3.2–3.5/4.1/4.3–4.5。cached同observations重复不是新独立测量，固定subspace/noise理论不能升级成adaptive过程的精确posterior；两类GPU、best-of-grid/有限tasks不授免费walltime收益。新增posterior局部recipe不改变Ch28既有forward预算与相关误差解释，标准仅报告；root实际3.2–3.4/4.3核通过，不混用后续v4标题/机制。

### [The Two-Stage Decision-Sampling Hypothesis: Understanding the Emergence of Self-Reflection in RL-Trained LLMs](https://arxiv.org/abs/2601.01580v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01580v1) §3.1–3.3/4.1–4.2/E3–E5。相同advantage scalar不等梯度等幅，retry词是proxy而非独立模块，length/KL需限定计法；Qwen7B算术反侧与SFT/GRPO预算未matched，不授普遍泛化归因。深入仅报告受限分析case，未改变现有objective/credit边界；root实际3.3.1/4.1/4.2/E4核通过，未冒充全部附件复核。

### [Can LLMs Track Their Output Length? A Dynamic Feedback Mechanism for Precise Length Regulation](https://arxiv.org/abs/2601.01768v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01768v1) Method/Models/Evaluation/general-domain反侧/Limitations。句界外部token/word/sentence count callback提供可执行反馈，质量judge有限且ELI5有退步，中断batch非免费counter。原误4分已按该原机制纠正2+1+2=5，不以不写Books倒推评分。标准仅报告受限recipe：没有改变现有feedback与质量联合验收边界，不因只有三model否定潜在长期价值；root实际必要core与处置通过。

### [UnPII: Unlearning Personally Identifiable Information with Quantifiable Exposure Risk](https://arxiv.org/abs/2601.01786v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01786v1) §3/4.1–4.2/5.1–5.2/6/7。PRI是可配置policy权重，公式乘积/prose inner product不作真实风险证书；Llama2-7B、合成PII/regex或GPT4mini只支持受限重权unlearning，hardware/precision Not Disclosed。安全必要深入仅报告：新增局部risk-weight recipe不改长期删除/authorization/attack验收边界，非完备删除或worstcase防御。root实际必要source核通过。

### [COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs](https://arxiv.org/abs/2601.01836v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01836v1) §3.1–3.2/4/5.1–5.2/6、F1/F2。allow/deny与PAS明确测量对象，synthetic八org人口/F2 CityGov专家不等全部gold；Table4 deny-edge约54–60与正文>96冲突不授预过滤普效。反证深入仅报告该有限org-policy protocol，现有长期scope/许可/拒绝合同未改变；root实际metric/反侧核通过，争议数值不作正面证据。

### [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01885v1) §3.2–3.5/4.1/4.3/limits。stage reset STM保LTM、terminal advantage广播与额外proxy奖励，AllReturns更多tokens/tools；有限Hotpot→五环境不是零成本通用memory真值。Ch77 106–164具体已有typed proposal/commit、learned transition与outcome/content proxy分账承载拟采用命题，标准已有覆盖/No Change；root必要原源及owner实际核通过。

### [Output Embedding Centering for Stable LLM Pretraining](https://arxiv.org/abs/2601.02031v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.02031v1) §2.1–2.4/3/4/7。五embedding反例、h=(0,1)使B_ratio<1但maxabslogit 1→1.6；Eq17普遍界及Eq26拆max不成立，μ-loss不控制零均值对消行。5分标准中心保证隔离，保有限预训练实验不判全失败；root实际原段及反例复算通过。恢复只需修正h/bound条件、推导及依赖实现，不遍历数学附件。

### [Streaming Hallucination Detection in Long Chain-of-Thought Reasoning](https://arxiv.org/abs/2601.02170v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.02170v1) §2.2/4.1–4.2/7。step/prefix teacher标签、过滤与可恢复alarm并非单向累计，白盒hidden signal/终态拟合不授内部真值。原4纠正2+1+2=5，标准仅报告新增检测对象case，不改长期faithfulness或可靠在线干预判断；root实际core及处置通过。

### [DHI: Leveraging Diverse Hallucination Induction for Enhanced Contrastive Factuality Control in Large Language Models](https://arxiv.org/abs/2601.01156v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01156v1) Eq2/3/4及FactScore配置，原式保留在[DHI公式记录](../_sources/daily-20260107/DHI-formula-review.md)。事实位合并loss为−αlogP的非负CE，不支持prose的反向事实训练；raw-logit threshold非共同平移不变且max<0可空，mainβ≤1与FactScoreβ2冲突。5中心保证争议隔离，不否认有限实验；root实际重开原HTML核通过。精确loss/准入/配置材料恢复再开，不写Books。

### [Flow Equivariant World Models: Memory for Partially Observed Dynamic Environments](https://arxiv.org/abs/2601.01075v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01075v1) §3.1–3.2、SelfMotion Eq7/2D Eq8/3D Eq9、有限实验/limits。known action inverse搬运与external velocity channels预测分开，write→flow→readout依fully-observed/equivariant条件；3D encoder as-if近似不授精确几何、确定性有限地图不授真实state或control safety。H100B1与串行state、额外训练/离散速度边界保留。实际Ch25 376一段/1228首注承接persistent→预算，root必要原源、具体owner及实际正文/邻接/末注POST通过。registered 03:24:38Z仅合取区间上界。

### [Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2601.01618v1)

必要正文为 [exact-v1](https://arxiv.org/html/2601.01618v1) §3.2.2–3.2.3/4.1–4.3。ego框/点/箭头render入actionprefix，可编辑不等安全；view/time/object/coordinate/edit identity与fresh observation后重新生成是本书工程推导。Table3仅subtask completion，不授整任务near-perfect；stage数据/额外训练/互动render成本保留。实际Ch26 404一段/1350首注，root必要原源、owner及实际正文/邻接/末注POST通过。registered 03:38:00Z仅合取区间上界。

### [Beyond Gemini-3-Pro: Revisiting LLM Routing and Aggregation at Scale](https://arxiv.org/abs/2601.01330v1)

[exact-v1](https://arxiv.org/html/2601.01330v1) 核心及Inference extra：先生成K候选response，再由query/support选择与阈值switch；切换不退还已有生成成本。SWE单query评分不是真实仓库执行验收，原有限质量/成本与本地router recipe不改变长期owner合同，因此标准仅报告。feb01_v3实际必要原源非作者核、root确认处置通过。原Submitted/ID/首公告与registered 03:30:50Z合取保守区间，不把registered当public。

### [Yuan3.0 Flash: An Open Multimodal Large Language Model for Enterprise Applications](https://arxiv.org/abs/2601.01718v1)

[exact-v1](https://arxiv.org/html/2601.01718v1) §3.1–3.2/6.4：gold-assisted first-answer/verify tags奖励与ADS/entropy/negative clipping是原新增局部objective；不把MoE/RL成熟原则算原创，也不因企业领域关闭。1+1+2=4，局部recipe不改现有训练信用/成本解释，已关闭且仅报告；不采用headline普效或内部reasoning因果。feb01_v3实际必要源、root确认通过。registered 03:40:25Z仅合取区间上界。

### [Safety at One Shot: Patching Fine-Tuned LLMs with A Single Instance](https://arxiv.org/abs/2601.01887v1)

[exact-v1](https://arxiv.org/html/2601.01887v1) §3.1–3.3/4.1–4.2及理论/AppC/A2：gradient SVD不是Hessian，PSD/PL是额外局部假设、复杂度还绑定步长；binary fixed-m与连续L2不能混成稀疏选择证明。selected十epoch不等single update、API至少10examples不是one-shot；只保有限修补反证，不授全worstcase恢复。3+1+2=6，安全必要深入，仅报告受限patch case而不改长期权限/防线保障；feb01_v3实际必要source核、root确认通过。registered 03:44:33Z仅合取区间上界；v2 submitted不自动作本窗已公开重要修订。

### [Tackling the Inherent Difficulty of Noise Filtering in RAG](https://arxiv.org/abs/2601.01896v1)

[exact-v1](https://arxiv.org/html/2601.01896v1) §3–6/limits：pair/triple lower-bound有特定hypotheses，不是所有retrieval无法过滤；g(x)与query-first训练是gold+3noise/r64的局部干预。max/min连续但切换点不必可微，tanh段不是全局clamp，不采用普遍容量不可能界。3+1+2=6反证深入，仅报告噪声敏感case；原retrieval质量与stop验收边界没有因该受限recipe改变。feb01_v3实际必要source、root确认通过。registered 03:44:46Z仅合取区间上界。

### [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314v1)

[exact-v1](https://arxiv.org/html/2601.02314v1) 必要方法/评价/限制：替换外部reasoning字符串→重采样→semantic judge的φ测的是外部干预敏感性，不识别内部因果。§5.1的500-query评价与§5.5的30-trace audit/qualitative不同，后者未明示人工，已纠正原笔记。2+1+2=5标准仅报告protocol，不采用内部generative faithfulness保证，不改现长期evidence权限。feb01_v3实际必要source、root确认通过。registered 03:55:02Z仅合取区间上界。

### [DatBench: Discriminative, Faithful, and Efficient VLM Evaluations](https://arxiv.org/abs/2601.02316v1)

[exact-v1](https://arxiv.org/html/2601.02316v1) §3各problem/solution、结果/limits与AppE/F；AppD长表未作实际复核。MCQ→生成/Qwen semantic judge/circular与blind/format过滤改变estimand和人口；privileged GPT gold仅核全smallmodel失败项，不能证明全套noise-free。point-biserial依同suite global score，negative r不是缺陷证书。3+1+2=6，评价反证深入仅报告本suite清洗/选择protocol；借Ch66既有测量合同限定判断，不冒称exact Existing，也不授unseen architecture或真正视觉必要性已证。feb01_v3实际必要source、root确认通过；registered 03:55:05Z仅合取区间上界。

### [Forget Less by Learning Together through Concept Consolidation](https://arxiv.org/abs/2601.01963v1)

[exact-v1](https://arxiv.org/html/2601.01963v1) §5.1–5.2/6.2/6.4/7：独立concept后set-invariant proxy attention与prompt-conditioned weights带额外state/MLP/contrastive成本；有限IA/TA亦有concept退步，不授无交叉干扰/永无遗忘或O(2G)优于O(G)。2+1+2=5标准仅报告局部personalization recipe，不改变现有长期表示/遗忘验收边界。feb01_v3实际必要source、root确认通过；registered 03:46:23Z仅合取区间上界。

### [Geometric and Dynamic Scaling in Deep Transformers](https://arxiv.org/abs/2601.01014v1)

[exact-v1](https://arxiv.org/html/2601.01014v1) 决定性几何方法：sigmoid signed-coordinate damping不是Householder，LN/epsilon与算法未完全对应，不授流形投影或全depth稳定保证。1+1+2=4仅保局部优化组合、不进一步采用；不是因无实验、几何名称或书稿主题已覆盖而删贡献。feb01_v3实际决定source、root确认关闭通过；registered 03:23:09Z仅合取区间上界，v2 Submitted不能当本窗public。

### [NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation](https://arxiv.org/abs/2601.02204v1)

[exact-v1](https://arxiv.org/html/2601.02204v1) §3.2.1/8.2及受影响消融：统一decoder的next-scale self-correction与旧accumulated VAR feature组合退步，direct residual/code-index输入有限改善，complexity是作者解释假说而非唯一原因。冻结codec/scale/input/perturb/target分别验收，额外训练和可选refiner成本保留；refiner可改结构，理论FLOPs不等同质量walltime。2+2+2=6、具体输入兼容反证缺口深入，实际Ch24 57一段/1520首注；root原source、owner及实际正文/前后/末注POST通过，未复现。registered 03:52:19Z仅合取区间上界。

### [Not All Needles Are Found: How Fact Distribution and Don't Make It Up Prompts Shape Literal Extraction, Logical Inference, and Hallucination Risks in Long-Context LLMs](https://arxiv.org/abs/2601.02023v1)

[exact-v1](https://arxiv.org/html/2601.02023v1) §3.1–3.3/4.1–4.3/6：固定38 facts/30 queries及四生产API alias只构成有限测试；位置、证据分散、单取与组合分别验收，AH prompt改变回答/拒答contract，heatmap不是内部attention因果。2+1+2=5标准完成，Ch22 118–145已具体承载位置/干扰、单needle与组合、拒答及成本边界，不称该书已有exact 38-fact recipe。root实际必要原源与正文对读通过，无新增Books。registered 03:47:50Z仅合取区间上界，当前DataCite题名不覆盖exact-v1题名。

### [ELLA: Efficient Lifelong Learning for Adapters in Large Language Models](https://arxiv.org/abs/2601.02232v1)

[exact-v1](https://arxiv.org/html/2601.02232v1) §3.1–3.2/4.1–4.2/4.4–4.5/4.8/7：Hadamard坐标shrink不保证basis-invariant语义去干扰；Eq5 loss符号冲突不采用，任务标签训练、额外Wpast/LoRA state和异构硬件回归不能省去。2+1+2=5标准仅报告有限持续适配recipe，不改变当前更新约束与回归验收判断，不授forward-transfer/forgetting普遍保障。root实际上述必要源处置通过；registered 03:53:01Z仅合取区间上界，v2 Submitted落窗不证明本窗公开重要revision。

### [CD4LM: Consistency Distillation and aDaptive Decoding for Diffusion Language Models](https://arxiv.org/abs/2601.02236v1)

[exact-v1](https://arxiv.org/html/2601.02236v1) §3.2–3.3/C3/C4及4.1–4.2/4.4/5.2/6.1：paired-view KL/CE只是surrogate，不能授full trajectory guarantee；k_min强制低confidence commit保证进展不等保证correctness。teacher/static canvas与8 MI250条件保留，full-recompute benchmark不证明approx-KV实际收益，pass1/T0与pass5/T1不能拼同协议。2+2+2=6标准仅报告有限蒸馏/sampler设计case，未改变长期采样正确性与模型接口边界；root实际上述必要source处置通过。registered 03:53:07Z仅合取区间上界。

### [GDRO: Group-level Reward Post-training Suitable for Diffusion Models](https://arxiv.org/abs/2601.02036v1)

[exact-v1](https://arxiv.org/html/2601.02036v1) §3.2–3.3/4.1–4.5：离线group soft-ranking加top1 likelihood regularizer不等在线reward采样，16/prompt预生成未包含于reported GPU-hours，k/B不同不能省去成本。相同reward仍可有不同质量，score offset/proxy不是quality真值；temperature公式歧义不采用。2+1+2=5标准仅报告该offline objective与局部反证，不把一般验收原则当新增Books；jan02_v3实际必要source非作者核、root确认通过。registered 03:48:09Z仅合取区间上界。

### [Perish or Flourish? A Holistic Evaluation of Large Language Models for Code Generation in Functional Programming](https://arxiv.org/abs/2601.02060v1)

[exact-v1](https://arxiv.org/html/2601.02060v1) §2.1 validation/style、2.3/3.2–3.3/6：LeetCode/GPT4o private tests不是完备oracle，关键词规则不证明functional purity；pass-conditioned style人口和模型温度分别记录。2+1+2=5标准仅报告受限测量protocol，未建立改变当前代码验收选择的新语义证书，不授FP泛化优势。jan02_v3实际必要source非作者核、root确认通过；registered 03:48:44Z仅合取区间上界。

### [VINO: A Unified Visual Generator with Interleaved OmniModal Context](https://arxiv.org/abs/2601.02358v1)

[exact-v1](https://arxiv.org/html/2601.02358v1) §2.1–2.3/limits：frozen VLM penultimate MLP映射VAE/MMDiT条件及3D RoPE为本次局部conditioning组合，未改变当前长期生成接口或约束判断。1+1+2=4仅报告关闭；没有读全training/ablation，也不采用headline性能，不因视觉领域或模型规模排除。jan02_v3实际决定性source非作者核、root确认通过。registered 03:56:07Z仅合取区间上界。

### [K-EXAONE Technical Report](https://arxiv.org/abs/2601.01739v1)

[exact-v1](https://arxiv.org/html/2601.01739v1) §2.1/3.2/Rehearsal/3.4–3.5/5：signed group advantage、长度几何概率和SimPER是本次局部objective，不借成熟MoE/RL原则抬分。1+1+2=4，仅报告、不进一步采用；更早模型项目首次公开线索未核，不能以版本名称授新研究事件，也不为不改变本次决定的部分扩索材。jan02_v3实际必要source非作者核、root确认低分关闭通过。registered 03:40:55Z仅支持arXiv v1合取区间上界，不是模型首发时刻。

### [MotionAdapter: Video Motion Transfer via Content-Aware Attention Customization](https://arxiv.org/abs/2601.01955v1)

[exact-v1](https://arxiv.org/html/2601.01955v1) §3.2–3.4/4.1/4.3/4.4/8.2：TopK reference cross-frame attention仍带source形状，target DINO/Hungarian correspondence与warp才改为目标控制条件；不是target语义真值。MF full .550低于no-extraction .772，20人偏好为另一protocol，不合并为全面优胜；10.5min/49帧/4090不免费。原2+1+2=5，具体shape-interface gap深入，实际Ch24 shared-motion后一段/源注已由root实际POST通过；artifact identity/失败回退是工程要求，不授物理真值。

### [Correctness isnt Efficiency: Runtime Memory Divergence in LLM-Generated Code](https://arxiv.org/abs/2601.01215v1)

[exact-v1](https://arxiv.org/html/2601.01215v1) §3.2/3.3/3.5、4.1–4.3、5.3–5.5与language/budget/aggregate必要补段：baseline/cummax/unitpeak丢释放与absolute bytes，DTW丢clock；只成功运行形状不能验已排除的OOM/timeout/instrument错误。tracemalloc filename不包native/device所有内存，N5/r10平均不能验tail。原3+1+2=6反证gap深入，实际Ch69 exposure后一段/raw容量与失败人口及源注root POST通过。当前DataCite title仅定位，采用exact-v1身份，不把后续修订混入。

### [A New Benchmark for the Appropriate Evaluation of RTL Code Optimization](https://arxiv.org/abs/2601.01765v1)

[exact-v1](https://arxiv.org/html/2601.01765v1) §2.1–2.3/3.3.1–3/4.1：DC/Yosys、优化模式、clock/library会改变source收益，strong backend可抹掉rewrite差异；43/54成功转换过滤人口保留。Formality功能与VCS有限时序、综合PPA分账，不授all-HW proof/实芯。3+1+2=6具体反证gap深入，feb01_v3实际source与Ch49 lowering owner核通过、root授权，实际Ch49:80窄段/首注及68–89邻接root POST通过。

### [Luminark: Training-free, Probabilistically-Certified Watermarking for General Vision Generative Models](https://arxiv.org/abs/2601.01085v1)

[exact-v1](https://arxiv.org/html/2601.01085v1) 必要core：Prop1固定x跨随机key不授固定key/adaptive-image FPR，OR flip/retry要算多重尝试；FID不证语义保真，threshold rate/count冲突不采用。3+1+2=6安全必要深入，保有限图像watermark case，仅报告不重写既有密钥/检测人口合同。feb01_v3实际必要source核通过，未扩所有攻击附件。

### [Warp-Cortex: An Asynchronous, Memory-Efficient Architecture for Million-Agent Cognitive Scaling on Consumer Hardware](https://arxiv.org/abs/2601.01298v1)

[exact-v1](https://arxiv.org/html/2601.01298v1) 必要core：shared θ与private KV可分账，但TDA覆盖、virtual RoPE因果publish、append mask与event/fence缺决定性实现，cosine相近不证推理真值。2+2+2=6中心保证争议，feb01_v3实际必要原段核后隔离；不判有限实验全假、不写Books。具体恢复材料见§5。

### [RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian](https://arxiv.org/abs/2601.01129v1)

[exact-v1](https://arxiv.org/html/2601.01129v1) core与necessary-extra：actionability的2068 code changes/2894 human comments、47 judge小sample分账，不是全部human gold。43k PR自选with/without及OLS/ITS不是随机试验，resolved comment或近行变化不证修bug，RQ1 August→July文字时序冲突不统一为全年因果。3+1+2=6反证深入，仅报告受限部署case，未改变长期评价证据权限；feb01_v3实际必要原文核通过。

### [LinMU: Multimodal Understanding Made Linear](https://arxiv.org/abs/2601.01322v1)

[exact-v1](https://arxiv.org/html/2601.01322v1) 必要core：冻结vision encoder后以MaskMamba2/Swin替代decoder，QKV初始化不等函数等价；8A100训练与H100 decoder-only不是整链预算。2+2+2=6标准完成，仅报告局部replacement recipe，未建立改变当前长期表示/执行接口的额外条件；feb01_v3实际必要原文核通过，不授headline整体性能。

### [Hidden State Poisoning Attacks against Mamba-based Language Models](https://arxiv.org/abs/2601.01972v1)

[exact-v1](https://arxiv.org/html/2601.01972v1) necessary-extra：uniform contraction只限原carry设定，hybrid/skip可恢复；白盒hidden cosine不同于hard-label-only接口。3+1+2=6安全反证深入，仅报告有限state攻击case，不授所有SSM不可逆。§3.2十V100与末限制singleV100冲突，不拼硬件数；feb01_v3实际必要原段核通过，v2 Submitted不是本窗公开证明。

### [From Failure to Mastery: Generating Hard Samples for Tool-use Agents](https://arxiv.org/abs/2601.01498v1)

[exact-v1](https://arxiv.org/html/2601.01498v1) core6+extra必要11：failure duel1204/2095→legal prerequisite→advanced query→Kmax3/allM call-pass只构造成功执行人口，400GPT4o difficulty judge不是internal gold；27k/BFCLtransfer局部，不授跨工具普效。2+2+2=6标准具体Existing，Ch66 1262–1298/1783–1803已有generator/filter/scorer、合法状态/reference≠query meaning和自然/reference人口；不称exact算法已写书。jan02_v3实际必要source与body对读通过，无Books改动。

### [CORE: Code-based Inverse Self-Training Framework with Graph Expansion for Virtual Agents](https://arxiv.org/abs/2601.02201v1)

[exact-v1](https://arxiv.org/html/2601.02201v1) method/analysis/D3/E2与backbone/B4：executable labels、strategy graph/Eq8–10 counts/pathlabel+stateF1是测量身份；E2专家五try的positive OSR不证negative falseaccept或完整路径时序，NGPT额外trajectory非总预算。2+2+2=6标准具体Existing，Ch66同上述generator/filter/oracle人口与空解应失败/integrity论证已承载可用边界；jan02_v3实际source/body核通过，无Books改动。

### [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295v1)

[exact-v1](https://arxiv.org/html/2601.02295v1) IV-A/B/Alg1、V-C/D/E、Appendix C/VI：progress近完成触发VLM与stop终止分责；反放delta是新动作，不是环境undo，fresh observation后再proposal且要求可逆性/controller许可。LIBERO模拟，无真实机器人；N²比较/VLM/retry成本保留。主MBR与Appendix C不同，不选择精确implementation。2+2+2=6具体gap深入，root实际source/Ch26 stack owner核后授权，actual Ch26:474窄段/首注及465–485邻接root POST通过。

### [Deferred Commitment Decoding for Diffusion Language Models](https://arxiv.org/abs/2601.02076v1)

[exact-v1](https://arxiv.org/html/2601.02076v1) §5.1–5.3、模型协议/6.3–6.4/hardware/limits：leftmostMASK窗口受长度+mask数限制，confidence加top1强制推进可提交低置信；semi-causal训练大块不能跨改。active不缓存，prefix/dual只是temporary并周期重建，非永久exact；窗口/阈值/成本/quality非单调。A100与A800等不同资源分账。2+2+2=6具体gap深入，root实际source/Ch24 owner核后授权，actual Ch24:258窄段/首注及248–270邻接root POST通过。

## 5. 缺口与下一步

本轮普通待办：无。来源有限停点、16项完整题摘、代表性负侧决定性核心与9项潜在贡献的日期停点经非作者复核。必要恢复仅为01280v1、01624v1、01299v1、01584v1、01500v1、01712v1、01046v1、06100v1、06103v1的日级首次公开/带ID官方公告，或可核作者具名公开记录；当前为什么不能采用及原链接分别见[筛选/日期停点](../_sources/daily-20260107/supplement-20261007.md)。可以接受相同正文的官方可核日期；不索秒级时刻、全机构历史或所有先行镜像。9项不支撑Coverage/Evidence或无遗漏断言，材料到达只恢复对应项。未发现具名机制变化且本日公开的重要修订；版本号或Submitted/Updated不代替该判断。

以下普通待办与终态限制是原窗口历史处置（保留）：

普通待办：无。有限51项逐项证据/Books决定及19处实际写后复核已通过；root完成六部分报告与来源停止、日期边界、负侧复核范围及终态隔离的日级验收，不扩大185宽列表或新库存。

本窗终态保留项均不用于正面证据、不进入Books、不支持无遗漏断言。本轮Google/Meta必要日级入口按§2隔离，需当窗可核日级目录或具名原事件记录才重开；Qwen/Hunyuan/MiMo已恢复的有限目录不再索无具名遗漏的全历史快照；其余原停止记录仅保留原范围，不以空响应、宽metadata或假期规则授无遗漏。公开revision/mirror的具体事件需原公告，不能由Submitted/current Updated或未支持API字段探针推断落窗。下列中心受影响保证均隔离，不把中心争议扩大为整篇实验无效：01401需完整图节点/下游distance与source∩critical优先规则；02031需修正h/bound条件与推导及依赖实现；01156需loss符号、shift-invariant准入与实际β配置；01298需TDA覆盖/append mask、virtual RoPE因果publish与同步实现。可接受同exact版本作者更正或可核实现决定性片段，只重开相关命题，不重读全部附件。

## 6. 复核

复核者：root（本轮非作者独立复核）

结论：通过（有限来源与外部日期保留项已隔离，不授无遗漏）

独立复核实际范围：9潜在增量全部完整v1题摘及日期限制；其余6负侧/1旧事件完整题摘和具体关闭理由，其中SuperSFL02092与V-VLAPS00969定点读必要方法，纠正value用于MCTS Q而非prior。SuperSFL保留其深度/损失梯度加权与timeout局部分支的实际描述，不因视觉或小模型关闭；当前局部组合未建立新的基础模型共享训练状态/恢复契约或具体设计反证。06100/06103原仅线索经完整题摘校准后补入9个具名日期保留，不将缺少日级证明伪装成贡献不足。14到期源的窗口/有限停点和恢复结果已核，未扩每周来源或整类逐项队列；原51家族、19实际整合及有效复核未重审/搬移。当前修改的机器校验另行通过，不代替语义验收。

### 原窗口历史复核（保留）

复核者：root

结论：通过

最新小批：root实际核Motion/Memory的必要原源、具体owner及实际正文/邻接/末注POST通过；RTL/DCD/Cycle已实际核Ch49:68–89、Ch24:248–270、Ch26:465–485及各首注，POST通过、锁释放。feb01_v3实际独立核01765/01085/01298/01129/01322/01972必要core与受限处置，RTL具体owner缺口已核、root授权窄写；Rovo纠正2068 code changes/2894 human comments、47只小sample，月份文字冲突不统一为全年因果。jan02_v3实际独立核HardGen core全部6+extra必要11、CORE method/analysis/D3/E2与backbone/B4，并对读Ch66 1262–1298/1783–1803，两项具体Existing通过；EverMemOS决定性§3.2–3.5贡献前关闭通过。只上述具名范围，不冒称全部附件。

root已实际完整读首批6、A–E完整题摘与两个title-backstop具名题摘，按具体增量校准，不是metadata全核；01005/01844/WildIng及具名决定性贡献前关闭原段独立通过。十九项实际整合均核必要原文、owner具体差异、实际正文/图/末注及相邻衔接；01401/02031/01156中心受影响保证隔离已核。feb01_v3实际独立核01330/01718/01887/01896/02314/01014/02316/01963的必要source，root确认原评分及处置通过；02314 audit未明示人工已修正，其余界限保留。root另实际核02023必要§3.1–3.3/4.1–4.3/6与Ch22 118–145具体已有覆盖、02232必要§3.1–3.2/4.1–4.2/4.4–4.5/4.8/7、02236 §3.2–3.3/C3/C4与4.1–4.2/4.4/5.2/6.1仅报告处置。jan02_v3实际核02036/02060标准仅报告、02358/01739低分关闭与02045贡献前关闭，root确认。最终六部分顺读与原入口/停止记录定点检查通过；51项采用范围与19处实际写入一致，没有可执行审阅或写后待办。负侧抽核不称全metadata/全站/所有附件验证；历史目录、公开revision/mirror限制及四项中心争议是本窗终态保留项，不用于正面证据、Books或无遗漏断言。完成态V3及限定diff检查另核，机器校验不能替代上述语义验收。
