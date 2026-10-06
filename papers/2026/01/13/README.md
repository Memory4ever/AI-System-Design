# Daily Research — 2026-01-13

**规范：** V3
**窗口：** 2026-01-12T09:00:00+08:00 ～ 2026-01-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T14:35:00+08:00

## 1. 结论

本日的共同问题不是更多 agent、更多 trace 或更高 reward 是否总有益，而是比较人口、证据来源与更新/执行权限能否保持一致。55份完整论文题摘中六项贡献前关闭、49个形成本窗论文候选；四主题 140 行去重 122 题名仅作有界查漏，不是 122 篇落窗新论文或强制全文队列。49 项必要方法、关键评价与直接反侧已由作者完成（含受限配方关闭与已据具体owner差额加深的材料），候选分母已冻结为50唯一家族（49论文+1 Kimi CLI 0.76 release，两个PR不另计家族）。24项已实际融入17个Stable Node owner章节并通过非写入作者POST；15项具体已有覆盖、11项仅报告已完成必要源终裁。普通扫描/筛选/审阅/Books待办0；root完整六部分非作者日级Gate通过，当前日级任务完成。

明确的负侧包括：speech/text 同题仍可有不同 reward 人口；self-rolled 专家轨迹去掉 plan 后不是原采样条件；memory trust 可以只反映系统处理成功而错误接纳 poison；加密 entity 保留关联也保留可观察关系；citation graph 连通不认证事实真值。以上不授生产性能、安全保证或全网无遗漏。未运行代码、未复现实验；数字仅在已实际核的原评价条件下使用。

## 2. 来源覆盖

实际执行时间为 2026-10-03 恢复；旧停点及以下原返回可复查。本轮只 Daily 组与确实触发的原事件/版本材料，不扫 Weekly。来源内没有确定新增项不等于机构没有发布。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 首入口及 news RSS 一次 feed，1244 metadata；本窗邻接 Jan9 SB Energy/Datadog、Jan13 Zenken、Jan14 Cerebras，读到跨窗停止；[原字段](../_sources/daily-20260113/NATIVE_ADJACENT.md) | 已检查 | 当前 feed 不恢复已删除历史；无全站无发布声明 |
| SRC-ANTHROPIC | Research 原嵌入 publishedOn 切片；Jan9 constitutional classifiers 与 Jan14 property-based-testing 跨窗；[记录](../_sources/daily-20260113/NATIVE_ADJACENT.md) | 已检查 | 当前目录不能证明被删除事件完整性 |
| SRC-GOOGLE-AI | DeepMind Blog 首页及 page4有限恢复、Google Research 2026/01月页至Jan12 NeuralGCM；该项为暂缓 AI for Science 的降水应用，关闭，不借 systems词汇准入；pubs year2026入口失败；[月页原返回](../_sources/daily-20260113/SOURCE_FOURTH.json) | 受阻 | DeepMind完整本窗历史切片及pubs未恢复；Jan13日粒度邻项不能凭日期移入本窗 |
| SRC-META-AI | Research 0正文；Blog page2当前有限条目，未恢复本窗dated slice；[原返回](../_sources/daily-20260113/SOURCE_THIRD.json)、[补检](../_sources/daily-20260113/SOURCE_FINITE_WEB.json) | 受阻 | 无可用本窗历史原事件目录；不当零发布 |
| SRC-QWEN | 旧Blog首尾与真实 research-list API 60条，最新2025-12-23；[有限恢复](../_sources/daily-20260113/NATIVE_RECOVERY_ADJACENT.md) | 受阻 | 目录缺2026历史切片，不能证明Jan12无事件 |
| SRC-DEEPSEEK | 主页与updates单页恢复，日期从2026近期跳2025-12-01，跨窗邻接即停；[原字段](../_sources/daily-20260113/NATIVE_ADJACENT.md) | 已检查 | 单页旧/删除事件不恢复；不继续全部旧正文 |
| SRC-MOONSHOT | Platform Blog日期切片与kimi-cli releases per_page100 page1跨窗；0.76 published_at=2026-01-12T13:11:16Z；定点PR603/602实际body；[材料](../_sources/daily-20260113/FIRST_META_AND_KIMI.jsonl) | 已检查 | 两兼容修订同release已深入核受影响行为/仅报告；不扫其他repo |
| SRC-TENCENT-HUNYUAN | Research超时，真正publicList API page1 size20 renderType0实际9条，最早Feb3；[恢复](../_sources/daily-20260113/NATIVE_RECOVERY_ADJACENT.md) | 受阻 | 本窗历史条目未恢复，当前9条不是历史完整证明 |
| SRC-ZAI | Research首查原title/createAt邻接：GLM-Image Jan13T16Z、GLM4.7Flash Jan19T16Z均窗后，别名不重计；[字段](../_sources/daily-20260113/NATIVE_ADJACENT.md) | 已检查 | createAt非论文首公开；当前列表历史完整性有限 |
| SRC-BYTEDANCE-SEED | 真正get_article_list_v2按2026升序；论文type1 count20实19/total82/has_more=true/next20，首Jan19后窗停止；Blogtype2实14/total19/has_more=false/next空；[恢复](../_sources/daily-20260113/NATIVE_RECOVERY_ADJACENT.md) | 受阻 | 返回数/total差额隔离，空next不认证完整历史；不扫描后续全年 |
| SRC-BAIDU-ERNIE | Blog中文首入口实际可读近期三项Apr15–May9，有限切片；[原返回](../_sources/daily-20260113/SOURCE_THIRD.json) | 受阻 | 没有本窗历史目录，不能用近期首页当零发布 |
| SRC-XIAOMI-MIMO | 首页可提取338行但本窗公开时间/历史列表未定；[原返回](../_sources/daily-20260113/SOURCE_THIRD.json) | 受阻 | 需准确本窗原事件/版本日期；无日期页面不采用 |
| SRC-MINIMAX | 英文Blog一次当前列表跨Jan27/Dec23邻接；中文入口与Agent Tech Blog有限原入口；[记录](../_sources/daily-20260113/SOURCE_FINITE_WEB.json) | 已检查 | Agent index无完整dated历史，当前目录不恢复已删除事件 |
| SRC-ARXIV | Submitted缓冲四主线主题、max100分页边界与140/122题名见[API返回](../_sources/daily-20260113/ARXIV_API_STOP.json)、[题名](../_sources/daily-20260113/ARXIV_TITLES.json)；55份exact-v1完整题摘AB1–5、六贡献前关闭；逐IDnormal Submitted+registered推定公告区间 | 已检查 | API首批摘要传输截断未当全读；未遍历完整分类/全年版本；首公开区间为推定非分秒日志 |
| 表外：[DataCite/arXiv日期恢复](https://info.arxiv.org/help/availability.html) | 仅恢复已有ID日期与原版本身份；[官方规则](../_sources/daily-20260113/OFFICIAL_ANNOUNCEMENT_RULE.md)、DATES2/3、DATES_AB5_RESUME、DATES_TWO_MISSING、FIRST_META；无新发现扫描 | 已检查 | registered只提供ID已公开上界；Updated/created与PDF LastModified不单独授首公开 |
| 表外：[Kimi CLI版本/PR](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.76) | 已触发release，仅核PR602 MIME错误→VideoURLPart能力误判与PR603按runtime模态能力渲染描述 | 已检查 | 必要行为已独立终裁；不声明artifact测试已运行 |

## 3. 候选与判断

下面只处理同一论文ID一次，全部采用 v1，后续修订只用于轻量事件信号/身份，不重评全年版本。公开区间按[official排程+ID仅announcement分配规则](../_sources/daily-20260113/OFFICIAL_ANNOUNCEMENT_RULE.md)与逐ID真实 registered 推定：正常v1 Submitted位于Thursday14:00–Friday14:00 EST批次；本窗09:00为常规排程下界，registered换算北京时间为ID已公开上界；表内为纳入原字段所标整秒精度，将各ID原registered上界加1秒，再写为半开区间。原registered字段未改，+1秒不是补造正文首公开时刻，也不使用Updated/created。不是first-public分秒日志，不把Updated/created当公开上界；有具名提前公开或延期相反证据时只重开该ID。所有列出的区间均完全落窗。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse](https://arxiv.org/html/2601.05505v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:54+08:00 | 共享冻结KV生成latent memory，entropy仅触发consolidation；last state并非无条件充分统计。 2+2+2=6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)；实际正文/非作者 POST 已通过 |
| [Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks](https://arxiv.org/html/2601.06007v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:34:54+08:00 | prefix稳定度、cache hit、TTFT与计费分责，cache命中不保证延迟改善。 2+2+2=6 | 深入完成 | 已有覆盖：`INFER-KV-CACHE` [Ch45 251–284，命中分母/TTFT/decode/费用分责](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；root已实际核必要源与现有具体承载，通过。 |
| [Peek2: A Regex-free implementation of pretokenizers for Byte-level BPE](https://arxiv.org/html/2601.05833v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:30:49+08:00 | regex改扫描器须保留精确pretoken边界，性能与兼容语义分别验收。 2+1+2=5 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)；实际正文/非作者 POST 已通过 |
| [Double: Breaking the Acceleration Limit via Double Retrieval Speculative Parallelism](https://arxiv.org/html/2601.05524v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:23:23+08:00 | target-corrected/retrieved suffix改下一draft支持集，验证与commit权限仍在target。 2+2+2=6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48，proposal／逐位置verified guidance／commit段](../../../../books/part-05-inference-system/48-speculative-decoding.md)；root已实际核正文与前后邻接，POST通过。 |
| [Lost in Execution: On the Multilingual Robustness of Tool Calling in Large Language Models](https://arxiv.org/html/2601.05366v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:19:38+08:00 | 多语言工具错误分intent与参数值语言surface，两者不能用同一翻译修复。 2+2+2=6 | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78，界面值语言与query语义分责段](../../../../books/part-07-agent/78-tool-calling.md)；root已实际核正文与前后邻接，POST通过。 |
| [Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers from Statistical Distributions](https://arxiv.org/html/2601.05414v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:20:45+08:00 | token随机不保证所请求数值分布或跨调用独立性。 3+1+2=6 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78，专用sampler承载数值分布与独立性，不能由token随机或批内多样性认证](../../../../books/part-07-agent/78-tool-calling.md)；root已实际核必要源及现有具体论点，通过。 |
| [Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models](https://arxiv.org/html/2601.05445v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:28+08:00 | 多turn真实history、局部分支重试与抽象策略搜索可复用攻击；本地overwrite不改目标历史。 2+2+2=6 | 深入完成 | 仅报告：受限偏好数据/攻击搜索配方，本轮不足以改变长期owner判断；原机制/反侧及root终裁通过。 |
| [RingSQL: Generating Synthetic Data with Schema-Independent Templates for Text-to-SQL Reasoning Models](https://arxiv.org/html/2601.05451v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:37+08:00 | SQR结构模板先生成SQL、再重述问题；编译正确性不自动传递给语言问题。 2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-DATA` [Ch27，可执行spec→SQL→NL的共享ontology与语义边界，不授NL重写形式正确](../../../../books/part-04-training-system/27-data.md)；root已实际核必要源及现有具体论点，通过。 |
| [ART: Adaptive Reasoning Trees for Explainable Claim Verification](https://arxiv.org/html/2601.05455v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:42+08:00 | support/attack树将相对persuasiveness经DFQuAD传播，但分数不是真值概率。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [MaxCode: A Max-Reward Reinforcement Learning Framework for Automated Code Optimization](https://arxiv.org/html/2601.05475v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:10+08:00 | max-return搜索须把当前best写入value state，frozen generator不是policy RL更新。 2+2+2=6 | 深入完成 | 整合：`AGENT-PLANNING` [Ch79，best state与max-return critic两段](../../../../books/part-07-agent/79-planning.md)；root已实际核正文与前后邻接，POST通过。 |
| [MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards](https://arxiv.org/html/2601.05488v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:28+08:00 | memory改写引用旧entry并重建时间戳；共享QA reward按retrieval count分配非因果credit。 2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77，retrieval count非causal credit段](../../../../books/part-07-agent/77-memory.md)；root已实际核正文与前后邻接，POST通过。 |
| [Over-Searching in Search-Augmented Large Language Models](https://arxiv.org/html/2601.05503v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:51+08:00 | 可答与应abstain两人口中更多search可能相反，intent含糊不是检索不足。 3+1+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76 493，双人口与澄清](../../../../books/part-07-agent/76-rag.md)；root已实际核正文/邻接，POST通过。 |
| [Closing the Modality Reasoning Gap for Speech Large Language Models](https://arxiv.org/html/2601.05543v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:23:52+08:00 | 同policy异输入模态按子组中心化，以当前正确text作有条件moving reference。 2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文/非作者 POST 已通过 |
| [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](https://arxiv.org/html/2601.05560v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:24:18+08:00 | 共同base task vector的reasoning低梯度与task高梯度选择方向不同，overlap双方排除。 2+1+2=5 | 深入完成 | 整合：`TRAIN-CHECKPOINT` [Ch35 426，calibration mask merge](../../../../books/part-04-training-system/35-checkpoint.md)；root已实际核正文/前后邻接及末注，POST通过 |
| [PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning](https://arxiv.org/html/2601.05593v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:25:10+08:00 | parallel轨迹结论压缩后另训合成能力；扩大候选不等majority已可靠。 2+2+2=6 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82，conclusion compaction与synthesis两段](../../../../books/part-07-agent/82-multi-agent.md)；root已实际核正文与前后邻接，POST通过。 |
| [SceneAlign: Aligning Multimodal Reasoning to Scene Graphs in Complex Visual Scenes](https://arxiv.org/html/2601.05600v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:25:20+08:00 | scenegraph局部扰动筛选偏好negative，结构难度与监督truth分开。 2+1+2=5 | 标准完成 | 仅报告：受限偏好数据/攻击搜索配方，本轮不足以改变长期owner判断；原机制/反侧及root终裁通过。 |
| [Dual-Phase LLM Reasoning: Self-Evolved Mathematical Frameworks](https://arxiv.org/html/2601.05616v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:25:42+08:00 | 数学框架提示、rejection与分阶段SFT局部配方，未新增一般credit或可验证更新机制。 1+1+2=4 | 已关闭 | 仅报告：受限两阶段/rejection配方，本轮不足以改变长期owner判断；root必要源终裁通过 |
| [Transformer Is Inherently a Causal Learner](https://arxiv.org/html/2601.05647v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:26:26+08:00 | conditional score理论的因果识别依赖A1–A4，实践MSE/LRP proxy不能由attention直接授因果。 3+1+2=6 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5 417，conditional lagged identifiability](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；root已实际核正文/前后邻接及末注，POST通过 |
| [Tracing Stereotypes in Pre-trained Transformers: From Biased Neurons to Fairer Models](https://arxiv.org/html/2601.05663v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:26:48+08:00 | IG定位后zero activation的BERT偏见干预只支持局部可移除关联，utility必须单列。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [Do Sparse Autoencoders Identify Reasoning Features in Language Models?](https://arxiv.org/html/2601.05679v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:27:11+08:00 | SAE reasoning label要过表面风格注入与语义FP/FN反证，contrastive激活本身不够。 3+1+2=6 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch05，specificity/invariance两段](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；root已实际核正文与前后邻接，POST通过。 |
| [Do LLMs Need Inherent Reasoning Before Reinforcement Learning? A Study in Korean Self-Correction](https://arxiv.org/html/2601.05459v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:49+08:00 | 韩语self-correction code-switch warmstart的alignment现象不等英语neuron因果。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [The Facade of Truth: Uncovering and Mitigating LLM Susceptibility to Deceptive Evidence](https://arxiv.org/html/2601.05478v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:15+08:00 | 可信表面与证据真伪可错配，intent-warning只改变对材料的使用不证明truth。 2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72 590–609及616–618，非命令framing与证据使用](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源与现有具体承载，通过。 |
| [Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection](https://arxiv.org/html/2601.05501v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:46+08:00 | importance-guided FO+ZO混合层更新是受限优化器配方，非全模型稳定保证。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [Memory Poisoning Attack and Defense on Memory Based LLM-Agents](https://arxiv.org/html/2601.05504v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:22:53+08:00 | memory trust与真实poison标签可以完全失配，零accepted与全通过必须分人口。 2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77 125，trust/accepted与utility](../../../../books/part-07-agent/77-memory.md)；root已实际核正文/邻接，POST通过。 |
| [Continual Pretraining on Encrypted Synthetic Data for Privacy-Preserving LLMs](https://arxiv.org/html/2601.05635v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:26:09+08:00 | 确定性entity加密保留关联也保留equality/frequency/关系泄漏，非语义安全。 2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72，确定性entity加密的关联泄漏段](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核正文与前后邻接，POST通过。 |
| [Multilingual Amnesia: On the Transferability of Unlearning in Multilingual LLMs](https://arxiv.org/html/2601.05641v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:26:18+08:00 | forget语言与probe语言应组成非对称矩阵，单语言likelihood下降不授跨语言删除。 2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72，forget/retain语言迁移与regain矩阵，likelihood抑制不等知识物理删除](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源及现有具体论点，通过。 |
| [PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility](https://arxiv.org/html/2601.05739v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:28:38+08:00 | PII visibility/refusal/content truth需分账，虚构PII与真实memorized leak不是同事件。 2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72 452，visibility/cPDR/真实秘密](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核正文/前后邻接及末注，POST通过 |
| [AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Monitor](https://arxiv.org/html/2601.05752v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:28:56+08:00 | misbehavior monitor应以配对benign/positive测FAR/FN，训练已知类可能损伤未见类。 2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 1618，pairedMR/FAR类别cross-test](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root已实际核正文/邻接，POST通过。 |
| [VIGIL: Defending LLM Agents Against Tool Stream Injection via Verify-Before-Commit](https://arxiv.org/html/2601.05755v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:29:00+08:00 | tool docstring/runtime/error皆输入攻击面，LLM branch verification与cache不授effect权限。 2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72 590–609，外部input无authority/guard是sensor](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源与现有具体承载，通过。 |
| [Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer](https://arxiv.org/html/2601.05770v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:29:21+08:00 | 可抽程序需要专门hard-routing/小算术MLP架构，不是任意LLM weights可还原算法。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [Fusion Matters: Length-Aware Analysis of Positional-Encoding Fusion in Transformers](https://arxiv.org/html/2601.05807v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:30:13+08:00 | position fusion也是编码器设计变量，gate收益受长度与任务人口条件限制。 2+1+2=5 | 深入完成 | 整合：`MODEL-POSITION-ENCODING` [Ch13，position内容与fusion operator段](../../../../books/part-02-model/13-position-encoding.md)；root已实际核正文与前后邻接，POST通过。 |
| [Chaining the Evidence: Robust Reinforcement Learning for Deep Search Agents with Citation-Aware Rubric Rewards](https://arxiv.org/html/2601.06021v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:35:14+08:00 | citation-supported rubric连到答案后仍须correct outcome gate，connectivity非真值。 2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-GRPO` [Ch33 525及1493–1507，outcome gate与rubric provenance](../../../../books/part-04-training-system/33-grpo.md)；root已实际核必要源与现有具体承载，通过。 |
| [RECOR: Reasoning-focused Multi-turn Conversational Retrieval Benchmark](https://arxiv.org/html/2601.05461v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:51+08:00 | 多轮history可帮隐式桥接也可污染query，retrieval recall不授生成truth。 2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76，history对query桥接与污染、retrieval与generation分测](../../../../books/part-07-agent/76-rag.md)；root已实际核必要源及现有具体论点，通过。 |
| [PRISMA: Reinforcement Learning Guided Two-Stage Policy Optimization in Multi-Agent Architecture for Open-Domain Multi-Hop Question Answering](https://arxiv.org/html/2601.05465v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:57+08:00 | 冻结校准专家后用真实trace训Inspector，恢复收益与regression分账。 2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文/非作者 POST 已通过 |
| [Efficient Temporal-aware Matryoshka Adaptation for Temporal Information Retrieval](https://arxiv.org/html/2601.05549v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:24:01+08:00 | Matryoshka短向量内部再保时间prefix和语义tail，避免截断预算吞时间表示。 2+1+2=5 | 深入完成 | 整合：`AGENT-RAG` [Ch76，temporal prefix／semantic tail两段](../../../../books/part-07-agent/76-rag.md)；root已实际核正文与前后邻接，POST通过。 |
| [Conformity Dynamics in LLM Multi-Agent Systems: The Roles of Topology and Self-Social Weighting](https://arxiv.org/html/2601.05606v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:25:28+08:00 | 更密拓扑/更高social权重可更快形成wrong-but-sure共识，confidence非truth。 3+1+2=6 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82，wrong-mode相关错误与consensus/correctness分测；非具体拓扑配方](../../../../books/part-07-agent/82-multi-agent.md)；root已实际核必要源及现有具体论点，通过。 |
| [GIFT: Games as Informal Training for Generalizable LLMs](https://arxiv.org/html/2601.05633v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:26:06+08:00 | 顺序subtask episode改变训练联合人口，但实现是平均reward不是严格AND门。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning](https://arxiv.org/html/2601.05705v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:27:50+08:00 | 形式verifier权限绑定logic/axioms/自然语言formalization，改logic改变可证明集合。 2+2+2=6 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78，logic/axioms/formalization绑定证明权限，不授NL忠实或伦理真值](../../../../books/part-07-agent/78-tool-calling.md)；root已实际核必要源及现有具体论点，通过。 |
| [Multimodal In-context Learning for ASR of Low-resource Languages](https://arxiv.org/html/2601.05707v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:27:52+08:00 | MICL低PPL、直接ASR生成与外部10-best重排序是三人口，acoustic支持集决定收益边界。 2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66 110，同prefixNLL与实际生成质量分责](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root已实际核必要源与现有具体承载，通过。 |
| [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/html/2601.05787v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:29:45+08:00 | plan-conditioned self-roll后去plan混cache，轨迹来源不抹去conditioning变化。 2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文/非作者 POST 已通过 |
| [EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/html/2601.05808v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:30:15+08:00 | programmatic环境state/checker能支持多路径，但AST不证明自动terminal validator语义完整。 2+2+2=6 | 深入完成 | 已有覆盖：`TRAIN-DATA` [Ch27，环境state/checker与共享rubric盲点；生成验证器不等独立oracle](../../../../books/part-04-training-system/27-data.md)；root已实际核必要源及现有具体论点，通过。 |
| [iReasoner: Trajectory-Aware Intrinsic Reasoning Supervision for Self-Evolving Large Multimodal Models](https://arxiv.org/html/2601.05877v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:31:51+08:00 | 同答案轨迹step agreement是内部proxy，不是visual truth或faithful reasoning。 2+1+2=5 | 标准完成 | 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4 |
| [HAPS: Hierarchical LLM Routing with Joint Architecture and Parameter Search](https://arxiv.org/html/2601.05903v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:32:28+08:00 | router选择base后按同prompt生成LoRA，architecture选择与可变参数artifact共同验收。 2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA` [Ch30 207，按输入权重/身份与bucket成本](../../../../books/part-04-training-system/30-lora.md)；root已实际核正文/邻接，POST通过。 |
| [Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency](https://arxiv.org/html/2601.05905v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:32:31+08:00 | point-wise一致可遮邻域情境脆弱，NCB是正确频率×邻居几何平均而非posterior。 3+1+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 580，邻域经验score](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root已实际核正文/邻接，POST通过。 |
| [Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset](https://arxiv.org/html/2601.05918v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:32:49+08:00 | 删除显式PII后公开项目/经历等组合线索仍能链接身份，富文本发布需composition审计。 3+1+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72，去显式PII后外部公开知识组合链接，候选池/高置信误匹配分账](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源及现有具体论点，通过。 |
| [Can We Predict Before Executing Machine Learning Agents?](https://arxiv.org/html/2601.05930v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:33:05+08:00 | verified profiling→forecast筛选→实际执行，仅执行分支拥有groundtruth，预测不能认证safe prune。 2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-PLANNING` [Ch79 69–75与179，预测/快筛不等真实执行与safe-prune](../../../../books/part-07-agent/79-planning.md)；root已实际核必要源与现有具体承载，通过。 |
| [AdaFuse: Adaptive Ensemble Decoding with Test-Time Scaling for LLMs](https://arxiv.org/html/2601.06022v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:35:16+08:00 | word-boundary共享候选+首token margin控提交span，跨tokenizer NLL均值只是fusion score。 2+2+2=6 | 深入完成 | 整合：`MODEL-SAMPLING` [Ch20 293，word-boundary与meanNLL heuristic](../../../../books/part-02-model/20-sampling.md)；root已实际核正文/邻接，POST通过。 |
| [Towards Generalized Multi-Image Editing for Unified Multimodal Models](https://arxiv.org/html/2601.05572v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:24:37+08:00 | relative spatial RoPE之外显式separator/image index可减来源混淆，变图数泛化仅有限对照。 2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23 720，separator/image index](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root已实际核正文/邻接，POST通过。 |
| [Jailbreaking Large Language Models through Iterative Tool-Disguised Attacks via Reinforcement Learning](https://arxiv.org/html/2601.05466v1) | 2026-01-12T09:00:00+08:00 ～ 2026-01-12T10:21:58+08:00 | tool-call结构可携带受禁止内容，mock成功不是真执行证据；低拒绝非高危害。 3+1+2=6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72 605–609与757–765，toolproposal非真实effect/四分责](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源与现有具体承载，通过。 |
| [Kimi CLI 0.76](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.76) | 2026-01-12T21:11:16+08:00 | ReadFile MIME错误修订与按Runtime模态能力渲染描述；两个PR归并同release，不授权限/文件真实性。1+1+1=3 | 深入完成 | 仅报告：版本相关兼容事实，本轮不改变长期owner；root必要受影响行为终裁通过 |

## 4. 证据与知识整合

各项以精确v1 HTML及原摘取核心定位；结果表未采用的数值不照录。HTML抽取可能损失不等式，精确公式只采用已对原页核实的部分。评分未因Books处置而修改；标准项因实际owner差额或安全反侧深入时只加深证据，不升分。完整题摘保存在本日AB1–5；轻量查看已有官方身份/历史中的撤回修订信号，未见所采用v1的withdrawn标记，不遍历完整版本史。非作者范围见§6。

### [FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse](https://arxiv.org/html/2601.05505v1)

精确版本 v1；必要证据：[jan13-corefirst.txt](../_sources/daily-20260113/jan13-corefirst.txt)，§3–5，内部state/monitor、消融与复杂任务反侧；少数模型/环境，不采普遍5倍或可持久事实真值。判断：共享冻结KV生成latent memory，entropy仅触发consolidation；last state并非无条件充分统计。 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)；实际正文/非作者 POST 已通过。

### [Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks](https://arxiv.org/html/2601.06007v1)

精确版本 v1；必要证据：[jan13-coresecond.txt](../_sources/daily-20260113/jan13-coresecond.txt)，三provider/三策略/DeepResearchBench与API费用统计；dynamic工具结果策略需保持语义，供应商结果不能横向当硬件速度定律。费用/TTFT关键反侧见[jan13-corefourth.txt](../_sources/daily-20260113/jan13-corefourth.txt) L136–178；不采用所有动态工具结果永不缓存的普适建议。判断：prefix稳定度、cache hit、TTFT与计费分责，cache命中不保证延迟改善。 已有覆盖：`INFER-KV-CACHE` [Ch45 251–284，命中分母/TTFT/decode/费用分责](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；root已实际核必要源与现有具体承载，通过。

### [Peek2: A Regex-free implementation of pretokenizers for Byte-level BPE](https://arxiv.org/html/2601.05833v1)

精确版本 v1；必要证据：[jan13-corethird.txt](../_sources/daily-20260113/jan13-corethird.txt)，方法、字符/边界规则与性能条件；不声称完整BPE替代、任意regex兼容或本地已运行。判断：regex改扫描器须保留精确pretoken边界，性能与兼容语义分别验收。 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)；实际正文/非作者 POST 已通过。

### [Double: Breaking the Acceleration Limit via Double Retrieval Speculative Parallelism](https://arxiv.org/html/2601.05524v1)

精确版本 v1；必要证据：[jan13-corefourth.txt](../_sources/daily-20260113/jan13-corefourth.txt)，§2.2/4.2–4.3与[D.2必要补读](../_sources/daily-20260113/core-05524-lossless.txt)；只采用同路径逐位置验证的guidance与commit边界。causal-mask描述与EM accuracy不单独证明greedy链/token-law；原全局lossless子命题隔离，不进入Books。判断：target-corrected/retrieved suffix改下一draft支持集，验证与commit权限仍在target。 整合：`INFER-SPECULATIVE-DECODING` [Ch48，proposal／逐位置verified guidance／commit段](../../../../books/part-05-inference-system/48-speculative-decoding.md)；root已实际核正文与前后邻接，POST通过。

### [Lost in Execution: On the Multilingual Robustness of Tool Calling in Large Language Models](https://arxiv.org/html/2601.05366v1)

精确版本 v1；必要证据：[core-05366.txt](../_sources/daily-20260113/core-05366.txt)，§3–5；BFCLv4英式schema/values、FT/PAR/PT/PRE/POST，低资源理解与post语义漂移，非生产多轮。判断：多语言工具错误分intent与参数值语言surface，两者不能用同一翻译修复。 整合：`AGENT-TOOL-CALLING` [Ch78，界面值语言与query语义分责段](../../../../books/part-07-agent/78-tool-calling.md)；root已实际核正文与前后邻接，POST通过。

### [Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers from Statistical Distributions](https://arxiv.org/html/2601.05414v1)

精确版本 v1；必要证据：[core-05414.txt](../_sources/daily-20260113/core-05414.txt)，§2–4；batch/stateless两人口、15分布/有限N、W1重尾条件、检验不拒绝非精确认证；不采无内部sampler因果。判断：token随机不保证所请求数值分布或跨调用独立性。 已有覆盖：`AGENT-TOOL-CALLING` [Ch78，专用sampler承载数值分布与独立性，不能由token随机或批内多样性认证](../../../../books/part-07-agent/78-tool-calling.md)；root已实际核必要源及现有具体论点，通过。

### [Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models](https://arxiv.org/html/2601.05445v1)

精确版本 v1；必要证据：[core-05445.txt](../_sources/daily-20260113/core-05445.txt)，§3–5.4；10turn/两数据集/LLM harmfulness judge及三有限defense，不证明任意安全机制或现实危害。判断：多turn真实history、局部分支重试与抽象策略搜索可复用攻击；本地overwrite不改目标历史。 仅报告：受限偏好数据/攻击搜索配方，本轮不足以改变长期owner判断；原机制/反侧及root终裁通过。

### [RingSQL: Generating Synthetic Data with Schema-Independent Templates for Text-to-SQL Reasoning Models](https://arxiv.org/html/2601.05451v1)

精确版本 v1；必要证据：[core-05451.txt](../_sources/daily-20260113/core-05451.txt)，§3–4；32人工模板/DDL外键、4k训练1kdev、3B/7B；重述与schema assumptions限制。判断：SQR结构模板先生成SQL、再重述问题；编译正确性不自动传递给语言问题。 已有覆盖：`TRAIN-DATA` [Ch27，可执行spec→SQL→NL的共享ontology与语义边界，不授NL重写形式正确](../../../../books/part-04-training-system/27-data.md)；root已实际核必要源及现有具体论点，通过。

### [ART: Adaptive Reasoning Trees for Explainable Claim Verification](https://arxiv.org/html/2601.05455v1)

精确版本 v1；必要证据：[core-05455.txt](../_sources/daily-20260113/core-05455.txt)，§3–4；500平衡claims/强judge及CoT对照，局部score组合不建立新的长期verification机制，trace也非内部faithfulness。判断：support/attack树将相对persuasiveness经DFQuAD传播，但分数不是真值概率。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [MaxCode: A Max-Reward Reinforcement Learning Framework for Automated Code Optimization](https://arxiv.org/html/2601.05475v1)

精确版本 v1；必要证据：[core-05475.txt](../_sources/daily-20260113/core-05475.txt)，§2–3；single-path训练value转beam有分布改变与反收益，64候选不等wallclock；代码tests不授通用correctness。判断：max-return搜索须把当前best写入value state，frozen generator不是policy RL更新。 整合：`AGENT-PLANNING` [Ch79，best state与max-return critic两段](../../../../books/part-07-agent/79-planning.md)；root已实际核正文与前后邻接，POST通过。

### [MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards](https://arxiv.org/html/2601.05488v1)

精确版本 v1；必要证据：[core-05488.txt](../_sources/daily-20260113/core-05488.txt)，§3–4.4；Qwen4B/固定answerer/三dialog sets；α过大与稀疏reward退步、Memory-R1数字取自论文。判断：memory改写引用旧entry并重建时间戳；共享QA reward按retrieval count分配非因果credit。 整合：`AGENT-MEMORY` [Ch77，retrieval count非causal credit段](../../../../books/part-07-agent/77-memory.md)；root已实际核正文与前后邻接，POST通过。

### [Over-Searching in Search-Augmented Large Language Models](https://arxiv.org/html/2601.05503v1)

精确版本 v1；必要证据：[core-05503.txt](../_sources/daily-20260113/core-05503.txt)，§3–5.4；594+594、三unanswerability类型/10search/固定TPC系数，judge非gold、fewshot过拒绝；成本非实际API价格。判断：可答与应abstain两人口中更多search可能相反，intent含糊不是检索不足。 整合：`AGENT-RAG` [Ch76 493，双人口与澄清](../../../../books/part-07-agent/76-rag.md)；root已实际核正文/邻接，POST通过。

### [Closing the Modality Reasoning Gap for Speech Large Language Models](https://arxiv.org/html/2601.05543v1)

精确版本 v1；必要证据：[core-05543.txt](../_sources/daily-20260113/core-05543.txt)，§3.2–3.3/Eq2–7/§4；7B/TTS、冻结encoder/projector；无正确text退base，MRR分母旧text、similarity非reasoning因果。判断：同policy异输入模态按子组中心化，以当前正确text作有条件moving reference。 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文/非作者 POST 已通过。

### [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](https://arxiv.org/html/2601.05560v1)

精确版本 v1；必要证据：[core-05560.txt](../_sources/daily-20260113/core-05560.txt)，§2–4；Qwen/Llama有限calibration与mask消融；gradient敏感性不证明知识地址，低ASR可能output collapse。判断：共同base task vector的reasoning低梯度与task高梯度选择方向不同，overlap双方排除。 整合：`TRAIN-CHECKPOINT` [Ch35 426，calibration mask merge](../../../../books/part-04-training-system/35-checkpoint.md)；root已实际核正文/前后邻接及末注，POST通过。

### [PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning](https://arxiv.org/html/2601.05593v1)

精确版本 v1；必要证据：[core-05593.txt](../_sources/daily-20260113/core-05593.txt)，§2–3.3；conclusion-only必须fit context、过滤voting可解训练、缓存输入/首轮池；TTC总token非wallclock或独立新样本数。判断：parallel轨迹结论压缩后另训合成能力；扩大候选不等majority已可靠。 整合：`AGENT-MULTI-AGENT` [Ch82，conclusion compaction与synthesis两段](../../../../books/part-07-agent/82-multi-agent.md)；root已实际核正文与前后邻接，POST通过。

### [SceneAlign: Aligning Multimodal Reasoning to Scene Graphs in Complex Visual Scenes](https://arxiv.org/html/2601.05600v1)

精确版本 v1；必要证据：[core-05600.txt](../_sources/daily-20260113/core-05600.txt)，§3–4；GPT4o图/中区Jaccard+diversity/DPO、五MLLM；图非visual gold、CoT质量非faithfulness，过窄/过宽及更多negative退步。判断：scenegraph局部扰动筛选偏好negative，结构难度与监督truth分开。 仅报告：受限偏好数据/攻击搜索配方，本轮不足以改变长期owner判断；原机制/反侧及root终裁通过。

### [Dual-Phase LLM Reasoning: Self-Evolved Mathematical Frameworks](https://arxiv.org/html/2601.05616v1)

精确版本 v1；必要证据：[core-05616.txt](../_sources/daily-20260113/core-05616.txt)，决定性§3–4；采用局部训练配方事实，不授通用新范式；4分关闭原评分保持，root已实际核两阶段与失败题2→10→100 rejection，不因工作量/Books已有降级。判断：数学框架提示、rejection与分阶段SFT局部配方，未新增一般credit或可验证更新机制。 仅报告：受限两阶段/rejection配方，本轮不足以改变长期owner判断；root必要源终裁通过。

### [Transformer Is Inherently a Causal Learner](https://arxiv.org/html/2601.05647v1)

精确版本 v1；必要证据：[core-05647.txt](../_sources/daily-20260113/core-05647.txt)，§3–4.1；exogeneity/无同期effect/窗口/faithfulness、latent或instant失效；sim三seed、Top-k/F1与timeout排除。判断：conditional score理论的因果识别依赖A1–A4，实践MSE/LRP proxy不能由attention直接授因果。 整合：`WORLDVIEW-REPRESENTATION` [Ch5 417，conditional lagged identifiability](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；root已实际核正文/前后邻接及末注，POST通过。

### [Tracing Stereotypes in Pre-trained Transformers: From Biased Neurons to Fairer Models](https://arxiv.org/html/2601.05663v1)

精确版本 v1；必要证据：[core-05663.txt](../_sources/daily-20260113/core-05663.txt)，§3–6；BERT110/340M、masked triples/十种问法、PPL/control与五下游任务；部分accuracy下降，论文2–3%概述不能授无效用损害。判断：IG定位后zero activation的BERT偏见干预只支持局部可移除关联，utility必须单列。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [Do Sparse Autoencoders Identify Reasoning Features in Language Models?](https://arxiv.org/html/2601.05679v1)

精确版本 v1；必要证据：[core-05679.txt](../_sources/daily-20260113/core-05679.txt)，§3–6；196所测context-dependent feature无genuine、有限模型SAE/严格单feature标准；不排除distributed reasoning，少量steering非全因果排除。判断：SAE reasoning label要过表面风格注入与语义FP/FN反证，contrastive激活本身不够。 整合：`WORLDVIEW-REPRESENTATION` [Ch05，specificity/invariance两段](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；root已实际核正文与前后邻接，POST通过。

### [Do LLMs Need Inherent Reasoning Before Reinforcement Learning? A Study in Korean Self-Correction](https://arxiv.org/html/2601.05459v1)

精确版本 v1；必要证据：[core-05459.txt](../_sources/daily-20260113/core-05459.txt)，§2–4；selected初始失败/4模型、CAS/DAS长度normalization、早层ablation与random control；teacher/格式/样本规模混杂，不采通用必要英语推理。判断：韩语self-correction code-switch warmstart的alignment现象不等英语neuron因果。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [The Facade of Truth: Uncovering and Mitigating LLM Susceptibility to Deceptive Evidence](https://arxiv.org/html/2601.05478v1)

精确版本 v1；必要证据：[core-05478.txt](../_sources/daily-20260113/core-05478.txt)，§2–4；4800八域、Likert表达/排名非内部belief、同源生成与analyst；800advice prompts非真实行动。判断：可信表面与证据真伪可错配，intent-warning只改变对材料的使用不证明truth。 已有覆盖：`PLATFORM-SECURITY` [Ch72 590–609及616–618，非命令framing与证据使用](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源与现有具体承载，通过。

### [Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection](https://arxiv.org/html/2601.05501v1)

精确版本 v1；必要证据：[core-05501.txt](../_sources/daily-20260113/core-05501.txt)，§3–5；DP选FO/seed恢复ZO、350M–13B/H100、epochs及wallclock不同，Math500 FO反侧；ρ/α/r过高退步。判断：importance-guided FO+ZO混合层更新是受限优化器配方，非全模型稳定保证。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [Memory Poisoning Attack and Defense on Memory Based LLM-Agents](https://arxiv.org/html/2601.05504v1)

精确版本 v1；必要证据：[core-05504.txt](../_sources/daily-20260113/core-05504.txt)，§3–8；EHR只是威胁场景不采领域方案；mini全拒绝不能称有用防御，Gemini接受population含poison仍trust=1，threshold不认证内容。判断：memory trust与真实poison标签可以完全失配，零accepted与全通过必须分人口。 整合：`AGENT-MEMORY` [Ch77 125，trust/accepted与utility](../../../../books/part-07-agent/77-memory.md)；root已实际核正文/邻接，POST通过。

### [Continual Pretraining on Encrypted Synthetic Data for Privacy-Preserving LLMs](https://arxiv.org/html/2601.05635v1)

精确版本 v1；必要证据：[core-05635.txt](../_sources/daily-20260113/core-05635.txt)，§3–4与core-05635-limitations；AES-ECB/Base64/NER/7–8B有限语料；明文问答效用不是privacy证明，ethics保证不采用。判断：确定性entity加密保留关联也保留equality/frequency/关系泄漏，非语义安全。 整合：`PLATFORM-SECURITY` [Ch72，确定性entity加密的关联泄漏段](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核正文与前后邻接，POST通过。

### [Multilingual Amnesia: On the Transferability of Unlearning in Multilingual LLMs](https://arxiv.org/html/2601.05641v1)

精确版本 v1；必要证据：[core-05641.txt](../_sources/daily-20260113/core-05641.txt)，§3–6；十语translated TOFU1%=2authors/Aya8B/三目标，retain/PPL与刻板QA中Unknown非物理erasure，syntactic distance非因果。判断：forget语言与probe语言应组成非对称矩阵，单语言likelihood下降不授跨语言删除。 已有覆盖：`PLATFORM-SECURITY` [Ch72，forget/retain语言迁移与regain矩阵，likelihood抑制不等知识物理删除](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源及现有具体论点，通过。

### [PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility](https://arxiv.org/html/2601.05739v1)

精确版本 v1；必要证据：[core-05739.txt](../_sources/daily-20260113/core-05739.txt)，§3–5.6；200subjects/4000、18VLM、20tokens/3seeds；search visibility非train coverage，cPDR仅non-refusal分母、格式有效不证明真实。判断：PII visibility/refusal/content truth需分账，虚构PII与真实memorized leak不是同事件。 整合：`PLATFORM-SECURITY` [Ch72 452，visibility/cPDR/真实秘密](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核正文/前后邻接及末注，POST通过。

### [AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Monitor](https://arxiv.org/html/2601.05752v1)

精确版本 v1；必要证据：[core-05752.txt](../_sources/daily-20260113/core-05752.txt)，§3–6；3010pairs/三类/153kSFT，引用证据可能增加false alarm；Qwen4B已见提升不授unseen gaming或生产监控可靠性。判断：misbehavior monitor应以配对benign/positive测FAR/FN，训练已知类可能损伤未见类。 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 1618，pairedMR/FAR类别cross-test](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root已实际核正文/邻接，POST通过。

### [VIGIL: Defending LLM Agents Against Tool Stream Injection via Verify-Before-Commit](https://arxiv.org/html/2601.05755v1)

精确版本 v1；必要证据：[core-05755.txt](../_sources/daily-20260113/core-05755.txt)，§3–5；AgentDojo/ToolBench/Qwen两模型，LLM query anchor不是formal truth；ASR非零/BU代价，validated cache需当前语义复核。判断：tool docstring/runtime/error皆输入攻击面，LLM branch verification与cache不授effect权限。 已有覆盖：`PLATFORM-SECURITY` [Ch72 590–609，外部input无authority/guard是sensor](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源与现有具体承载，通过。

### [Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer](https://arxiv.org/html/2601.05770v1)

精确版本 v1；必要证据：[core-05770.txt](../_sources/daily-20260113/core-05770.txt)，§3–6；PLE/温度退火/PySR/backtrace、toy MIPS三seed；MSE fidelity非global formal equivalence，soft→hard可退步。判断：可抽程序需要专门hard-routing/小算术MLP架构，不是任意LLM weights可还原算法。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [Fusion Matters: Length-Aware Analysis of Positional-Encoding Fusion in Transformers](https://arxiv.org/html/2601.05807v1)

精确版本 v1；必要证据：[core-05807.txt](../_sources/daily-20260113/core-05807.txt)，§3–9；fixed encoder/add/concat/scalar gate/pos-only conv、AGNews/IMDB/Arxiv paired seeds；非decoder/generative证明，跨corpus长度混杂。判断：position fusion也是编码器设计变量，gate收益受长度与任务人口条件限制。 整合：`MODEL-POSITION-ENCODING` [Ch13，position内容与fusion operator段](../../../../books/part-02-model/13-position-encoding.md)；root已实际核正文与前后邻接，POST通过。

### [Chaining the Evidence: Robust Reinforcement Learning for Deep Search Agents with Citation-Aware Rubric Rewards](https://arxiv.org/html/2601.06021v1)

精确版本 v1；必要证据：[core-06021.txt](../_sources/daily-20260113/core-06021.txt)，§2–3.4/§4；visited web snippets、LLM judge、bipartite BFS；α大退步/all-rollout shaping可推高错误adv，64kRL/128k test边界。判断：citation-supported rubric连到答案后仍须correct outcome gate，connectivity非真值。 已有覆盖：`TRAIN-GRPO` [Ch33 525及1493–1507，outcome gate与rubric provenance](../../../../books/part-04-training-system/33-grpo.md)；root已实际核必要源与现有具体承载，通过。

### [RECOR: Reasoning-focused Multi-turn Conversational Retrieval Benchmark](https://arxiv.org/html/2601.05461v1)

精确版本 v1；必要证据：[core-05461.txt](../_sources/daily-20260113/core-05461.txt)，§3–4；事实分解/来源核与多轮rewrite、GPT4o/200human；只收受限history/implicitbridge评价边界，不收benchmark规模。判断：多轮history可帮隐式桥接也可污染query，retrieval recall不授生成truth。 已有覆盖：`AGENT-RAG` [Ch76，history对query桥接与污染、retrieval与generation分测](../../../../books/part-07-agent/76-rag.md)；root已实际核必要源及现有具体论点，通过。

### [PRISMA: Reinforcement Learning Guided Two-Stage Policy Optimization in Multi-Agent Architecture for Open-Domain Multi-Hop Question Answering](https://arxiv.org/html/2601.05465v1)

精确版本 v1；必要证据：[core-05465.txt](../_sources/daily-20260113/core-05465.txt)，§3.3–4.4；OARPO非新optimizer、oracle/success-trace mining偏置；4H100五次平均，inspection成本不授do-no-harm/生产。判断：冻结校准专家后用真实trace训Inspector，恢复收益与regression分账。 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文/非作者 POST 已通过。

### [Efficient Temporal-aware Matryoshka Adaptation for Temporal Information Retrieval](https://arxiv.org/html/2601.05549v1)

精确版本 v1；必要证据：[core-05549.txt](../_sources/daily-20260113/core-05549.txt)，§3–5；LoRA/contrastive/六TEM/TNP-TimeQA+NQ；高α伤semantic、低维可无收益，metadata时间过滤不能替代这一representation问题。判断：Matryoshka短向量内部再保时间prefix和语义tail，避免截断预算吞时间表示。 整合：`AGENT-RAG` [Ch76，temporal prefix／semantic tail两段](../../../../books/part-07-agent/76-rag.md)；root已实际核正文与前后邻接，POST通过。

### [Conformity Dynamics in LLM Multi-Agent Systems: The Roles of Topology and Self-Social Weighting](https://arxiv.org/html/2601.05606v1)

精确版本 v1；必要证据：[core-05606.txt](../_sources/daily-20260113/core-05606.txt)，§3–4；七固定agents/星形1轮与分布式≤10、Snopes448/三模型十run；selfreport p不校准，tokens每轮非总免费。判断：更密拓扑/更高social权重可更快形成wrong-but-sure共识，confidence非truth。 已有覆盖：`AGENT-MULTI-AGENT` [Ch82，wrong-mode相关错误与consensus/correctness分测；非具体拓扑配方](../../../../books/part-07-agent/82-multi-agent.md)；root已实际核必要源及现有具体论点，通过。

### [GIFT: Games as Informal Training for Generalizable LLMs](https://arxiv.org/html/2601.05633v1)

精确版本 v1；必要证据：[core-05633.txt](../_sources/daily-20260113/core-05633.txt)，§3–4/AppendixB.2（core-05633-nested）；1.5B/7B/math+games，平均允许partial credit，不能采用正文AND或普遍gradient dominance。判断：顺序subtask episode改变训练联合人口，但实现是平均reward不是严格AND门。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning](https://arxiv.org/html/2601.05705v1)

精确版本 v1；必要证据：[core-05705.txt](../_sources/daily-20260113/core-05705.txt)，§2–4.1；LogiKey FOL/KD/DDL/Isabelle、syntax+consistency再entailment；证明不授NL忠实/伦理真值，补bridge需外部authority。判断：形式verifier权限绑定logic/axioms/自然语言formalization，改logic改变可证明集合。 已有覆盖：`AGENT-TOOL-CALLING` [Ch78，logic/axioms/formalization绑定证明权限，不授NL忠实或伦理真值](../../../../books/part-07-agent/78-tool-calling.md)；root已实际核必要源及现有具体论点，通过。

### [Multimodal In-context Learning for ASR of Low-resource Languages](https://arxiv.org/html/2601.05707v1)

精确版本 v1；必要证据：[原必要方法与反侧](../_sources/daily-20260113/core-05707-decisive.txt)，§2–5.2；MMS hypotheses/LoRA/三语WER、joint decoding额外成本；attention是诊断/语言数据量混杂，跨model PPL不直比。判断：MICL低PPL、直接ASR生成与外部10-best重排序是三人口，acoustic支持集决定收益边界。 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66 110，同prefixNLL与实际生成质量分责](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root已实际核必要源与现有具体承载，通过。

### [From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation](https://arxiv.org/html/2601.05787v1)

精确版本 v1；必要证据：[core-05787.txt](../_sources/daily-20260113/core-05787.txt)，§4–5.1；全失败替换/任务动态成功cache、128/241与54中19刷新子集；old-policy ratio不严格校正cache行为。判断：plan-conditioned self-roll后去plan混cache，轨迹来源不抹去conditioning变化。 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文/非作者 POST 已通过。

### [EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/html/2601.05808v1)

精确版本 v1；必要证据：[core-05808.txt](../_sources/daily-20260113/core-05808.txt)，§3–5；100round .85 LLM checking筛191env，LLM生成checkpoint函数给partial reward；共享盲点/小模型Tau退步/Conv缺func无改善。判断：programmatic环境state/checker能支持多路径，但AST不证明自动terminal validator语义完整。 已有覆盖：`TRAIN-DATA` [Ch27，环境state/checker与共享rubric盲点；生成验证器不等独立oracle](../../../../books/part-04-training-system/27-data.md)；root已实际核必要源及现有具体论点，通过。

### [iReasoner: Trajectory-Aware Intrinsic Reasoning Supervision for Self-Evolving Large Multimodal Models](https://arxiv.org/html/2601.05877v1)

精确版本 v1；必要证据：[core-05877.txt](../_sources/daily-20260113/core-05877.txt)，§3–4；dominant group/按步embedding prototype含自身、密度/时间衰减/混合warmup；answer-only部分benchmark更好，更多step可噪声。判断：同答案轨迹step agreement是内部proxy，不是visual truth或faithful reasoning。 仅报告：受限实现/配方或现有原则案例，本轮不足以改变长期owner判断；具体机制与反侧见§4。

### [HAPS: Hierarchical LLM Routing with Joint Architecture and Parameter Search](https://arxiv.org/html/2601.05903v1)

精确版本 v1；必要证据：[core-05903.txt](../_sources/daily-20260113/core-05903.txt)，§3–4.7；两agent/Llama1Brouter+MLP、r8/outputproj、Hotpot/MMLU；pricing模拟非生产成本，局部最优loss论证非global superiority。判断：router选择base后按同prompt生成LoRA，architecture选择与可变参数artifact共同验收。 整合：`TRAIN-LORA` [Ch30 207，按输入权重/身份与bucket成本](../../../../books/part-04-training-system/30-lora.md)；root已实际核正文/邻接，POST通过。

### [Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency](https://arxiv.org/html/2601.05905v1)

精确版本 v1；必要证据：[core-05905.txt](../_sources/daily-20260113/core-05905.txt)，§2–5；2000facts/LLM邻居与误导context/四32B，高一致子集30+10采样；stratified association非causal，CoT可放大干扰。判断：point-wise一致可遮邻域情境脆弱，NCB是正确频率×邻居几何平均而非posterior。 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 580，邻域经验score](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root已实际核正文/邻接，POST通过。

### [Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset](https://arxiv.org/html/2601.05918v1)

精确版本 v1；必要证据：[core-05918.txt](../_sources/daily-20260113/core-05918.txt)，§2–4；125采访筛24有公开项目、7高confidence人工6确认；一未发表排除，自信可false positive，非对全125普遍25%重识别。判断：删除显式PII后公开项目/经历等组合线索仍能链接身份，富文本发布需composition审计。 已有覆盖：`PLATFORM-SECURITY` [Ch72，去显式PII后外部公开知识组合链接，候选池/高置信误匹配分账](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源及现有具体论点，通过。

### [Can We Predict Before Executing Machine Learning Agents?](https://arxiv.org/html/2601.05930v1)

精确版本 v1；必要证据：[core-05930.txt](../_sources/daily-20260113/core-05930.txt)，§3.4/§4–6与C.4；pairwise低于全局ranking要求、m10/c.7/top1，未执行无testgroundtruth；五ML任务headline不采领域方案/因果world model。判断：verified profiling→forecast筛选→实际执行，仅执行分支拥有groundtruth，预测不能认证safe prune。 已有覆盖：`AGENT-PLANNING` [Ch79 69–75与179，预测/快筛不等真实执行与safe-prune](../../../../books/part-07-agent/79-planning.md)；root已实际核必要源与现有具体承载，通过。

### [AdaFuse: Adaptive Ensemble Decoding with Test-Time Scaling for LLMs](https://arxiv.org/html/2601.06022v1)

精确版本 v1；必要证据：[core-06022.txt](../_sources/daily-20260113/core-06022.txt)，§3–4；M3/τ.7、main关闭diversity、固定pair与oracle top2分开、GSM8K固定pair低于单model；4A100 batch1/10newtoken非SLO。判断：word-boundary共享候选+首token margin控提交span，跨tokenizer NLL均值只是fusion score。 整合：`MODEL-SAMPLING` [Ch20 293，word-boundary与meanNLL heuristic](../../../../books/part-02-model/20-sampling.md)；root已实际核正文/邻接，POST通过。

### [Towards Generalized Multi-Image Editing for Unified Multimodal Models](https://arxiv.org/html/2601.05572v1)

精确版本 v1；必要证据：[core-05572.txt](../_sources/daily-20260113/core-05572.txt)，§3–6；QwenEdit backbone、274cases/两MLLM/同seed，2→5images qualitative；normalized j/N变总数也变coordinate，不能授任意数目稳定identity。判断：relative spatial RoPE之外显式separator/image index可减来源混淆，变图数泛化仅有限对照。 整合：`MULTIMODAL-REPRESENTATION` [Ch23 720，separator/image index](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root已实际核正文/邻接，POST通过。

### [Jailbreaking Large Language Models through Iterative Tool-Disguised Attacks via Reinforcement Learning](https://arxiv.org/html/2601.05466v1)

精确版本 v1；必要证据：[core-05466.txt](../_sources/daily-20260113/core-05466.txt)，§III–V；JBB100/HarmfulQA50/三模型、JADES/StrongREJECT；detector仅non-refusal样本，tSNE关联非因果，防御须审核语义与effects。判断：tool-call结构可携带受禁止内容，mock成功不是真执行证据；低拒绝非高危害。 已有覆盖：`PLATFORM-SECURITY` [Ch72 605–609与757–765，toolproposal非真实effect/四分责](../../../../books/part-06-ai-infrastructure/72-security.md)；root已实际核必要源与现有具体承载，通过。

### [Kimi CLI 0.76](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.76)

[PR602](https://github.com/MoonshotAI/kimi-cli/pull/602) 的实际错误是 .ts/.tsx/.mts/.cts被mimetypes当MPEG Transport Stream，ReadFile返回VideoURLPart导致video_in能力拒绝；修订登记text/typescript。PR603按Runtime的image/video能力动态渲染描述，改变的是工具暴露的兼容说明，不认证文件真类型、用户意图或执行权限。精确release [published_at原字段](../_sources/daily-20260113/KIMI076_RELEASE_EXACT.json)=2026-01-12T13:11:16Z，BJT21:11:16；不采用created_at作为发布事件。两项具体行为已读，1+1+1=3，受影响兼容行为深入完成，root已实际核两PR和发布原字段，通过仅报告具体版本事实，不改变长期owner。不采用slash help与version bump为机制增量，未运行unit tests。

## 5. 缺口与下一步

本窗普通可执行待办为0。到期来源有限停止、50候选必要证据与Books处置、24实际写后及非作者完整日级Gate均已闭合；下述外部保留项及未采用子命题不是正面Coverage/Evidence通过。

外部终态保留项与定点重开条件：Qwen/Hunyuan/Seed返回差额、Google pubs/DeepMind历史、Meta、ERNIE、MiMo以及MiniMax Agent历史切片未被原入口完整恢复；需准确本窗官方dated事件/目录或精确版原正文，得到后只重开对应源/材料。现有目录、搜索或无日期正文不支持正面证据、候选、Books或零发布/无遗漏断言。arXiv区间只在normal batch+ID规则+真实registered推定下采用；具名repo先行公开/延期信号出现时定点核该ID，不把一般可能延期扩成全年检索。Native目录中Jan13日粒度或更晚事件不得移入本窗。

中心边界：FlashMem最后状态充分性、reasoning similarity causalproof、BEPA严格cache correction、GIFT严格AND、CaRR connectivity真值、PII确定性加密安全、未执行枝safe prune均未获得正面证明；本报告不以它们支撑长期保证。Double原文全局lossless/exact子主张隔离，状态机制窄采用只允许同一更正路径已逐位置验证的guidance延伸；causal mask和EM accuracy不补token-law证明。仅该子命题未采用，不误记整个材料家族中心争议。

## 6. 复核

复核者：root（本轮非作者日级验收）、jan01_v3、jan02_v3（具名局部范围）。

结论：通过

root已实际顺读完整六部分、50候选与§4必要边界、49个v1日期字段及normal公告条件、14来源有限停止、六具名贡献前关闭题摘及两项重开决定性机制；复用未变化的源→owner与24项实际POST。最后修正registered整秒上界为+1秒半开区间、表/正文旧处置尾句、Ch66指代与本地引用统计，均已核实，不扩大研究范围。

有效分批复用：本日AB首13项准入、AB5的23题摘及AB4十二题摘由具名非作者实际读取校准，不授日期或全文验收。FlashMem/Peek2必要原源→owner由jan01_v3通过、前root实际写Books、jan02_v3实际正文/邻接POST通过；其余原必要源、具体owner已有论点/差额均由root分批窄核。TARS/PRISMA/BEPA、TMRL/SAE/PaCoRe/MaxCode/Double、LostInExecution/MemBuilder/ECB/Fusion、HAPS/AdaFuse/Multiimage以及memorypoison/OverSearch/NCB/AutoMonitor及lagged-causal/ReasonAny/PII-visibility共24项真实正文、前后邻接与源注POST通过。15项Existing实际承载和11项OnlyReport必要源/关闭理由已逐项独立终裁，并非只按章名或标签准入。

负侧复核范围：AB5的23份完整题摘由jan01_v3实际读取；贡献前关闭六项05548/05746/05874/05890/05899/05960全部纳入具名准入校准，具体不足理由见[原记录](../_sources/daily-20260113/AB5_DECISIONS.md)。05707/05930两项原误关已按决定性机制重开，不因ASR小模型/ML题名或Book主题删池。Google Jan12 NeuralGCM降水应用仅按明确范围题名关闭，机构邻接条目核日期/范围，不声称重审所有旧正文；122宽题名只有有限查漏，不列作候选或逐项负侧全文库存。其余未变化的准入校准复用，不重新审无关旧附件；必要原源/Books已逐项独立终裁，并经上述完整日级验收；未声称全站、全分类或无关附件全量复核。

完成态V3结构校验通过；149本地引用存在、19个本报告Stable IDs均在当前ROADMAP，17个整合owner章节及本日Report/_sources的限定cached/unstaged diff-check通过。源列表历史限制与未采用子命题仍隔离，校验不能代替语义。保护运行前已有staged/unstaged，未stage、commit或push。
