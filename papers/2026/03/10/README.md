# Daily Research — 2026-03-10

**规范：** V3
**窗口：** 2026-03-09T09:00:00+08:00 ～ 2026-03-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T01:16:02+08:00

**窗口说明：** 用户授权本轮只补来源遗漏，原窗口、候选/评分/日期及原§4连续正文冻结；此前完成声明只对应原处理，不代表本轮增量验收。
**补充窗口：** 2026-03-09 ～ 2026-03-09
**补充检查时间：** 2026-10-09（北京时间）

冻结依据：[运行前原样基线](../_sources/daily-20260310/supplement-baseline-20261009.md)。本轮新增的来源、日期、证据和非作者验收只审差额，不搬移旧候选，不扩 Weekly、当前日、其他年份或共享索引。

## 1. 结论

以下原处理结论冻结复用，仅对应原窗口；新增处置见本节后半。

本次没有能够同时满足具体贡献与确定落窗的候选。14 家每日来源已作有限历史/主题检查；arXiv 四组主题查询分别返回171、116、34、150条元数据，存在跨查询重复，不能相加为本日论文数，更不是逐项题摘或全文队列。主题发现中有界选取16个家族读完整题摘：14项潜在机制或评价增量因公告日期区间跨09:00右端而隔离，1项SoK在贡献前关闭，1项Caller Identity Confusion因当前撤回及方法/伦理问题不采用。另有4个官方发布核心作具体关闭或窗外重呈现去重；两篇窗外论文题摘仅用于确认重呈现身份，不纳入16项发现集或本窗分母。

确定落窗候选为0，候选证据审阅完成0/0，Books新增/已有覆盖均为0。本日未把日期隔离项记作 Evidence 完成、仅报告候选或 Books 已有覆盖，也没有为了恢复旧日报33项而补造评分。旧原文、原始记录及此前书稿未删除，旧报告另存[原样快照](../_sources/daily-20260310/V3_LEGACY_REPORT_SNAPSHOT.md)，其旧分母、9分、EffectiveDate豁免及完成标签不继承。

机构目录只有当前可恢复切片，arXiv实际批次、部分机构历史入口的外部限制见§5。这不是“当天无相关论文”或全互联网无遗漏结论。普通可执行待办0；root已完成本六部分与有限停点的最终非作者日Gate，报告到达安全终态。

### 本轮补充（2026-10-09，已完成增量验收）

新增窗口为03-09完整自然日，原候选分母0及旧日期判断冻结。四组主题查询87/87、63/63、17/17、83/83为重叠发现元数据，不能相加；实际72完整题摘经root完整独读与决定性core校准后分为48确定日级归属候选、10具体贡献EX、10必要日期边界项、4先前公开身份项，已核窗外0。宽标题不自动成为逐项队列，无数量/保留率配额。

48项作者已完成按评分必要的机制/评价/直接反侧（不等复现或独立Gate），实际逐项Books PRE也齐。经独立复核确认处置为4整合、38具体已有覆盖、1仅报告、5中心争议暂缓；BoN→Ch20、NOBLE→Ch17、DC-DiT→Ch24、R4T→Ch76共四处各两段由root实际窄写，均已由非写入者supplement_20260310回对原证与完整局部邻接/末注POST通过。其余具体采用范围/位置见§3–4，已有覆盖不是覆盖每个recipe，有限新设计/反侧仍留报告。

BoN的win-rate/pairwise error不等任务正确率；永久非线性支路不能merge成LoRA；联合检索张量并不single-forward或保证事实support；非均匀2D去噪网格不认证硬预算。PPG/SPOT/Polarization/Bandit/GenHOI的强理论或归因争议隔离，局部观察不补齐中心主张。root前26项与review_mar10_remaining后22项必要Source/实际PRE独核已齐；四项实际写入POST通过。root已完成六部分最终非作者日级验收，普通可执行待办0；本轮补充到达安全终态。有限来源/14个必要日期项及原处理保留项仍不支持全源无遗漏或全部Evidence通过。

## 2. 来源覆盖

原处理2026-10-02的14行及有限原值保留于[原样基线](../_sources/daily-20260310/supplement-baseline-20261009.md#2-来源覆盖)，本轮复用身份/原证未变的实际切片并把新增差额并到以下唯一来源表；不改原窗口、候选日期或§4。

### 补充窗口来源差额

执行2026-10-09，本轮只Daily与实际触发的日期恢复，不扫描Weekly。旧源切片身份/原证未变且覆盖03-09邻接的予以复用，Seed locale与arxiv较早批次为定点新增，不重跑他日。实际范围与限制如下；[补查停点](../_sources/daily-20260310/supplement-source-coverage-20261009.md)、[四query原式](../_sources/daily-20260310/supplement-fetch-20261009.py)及[实际标题原值](../_sources/daily-20260310/supplement-arxiv-titles-20261009.json)可复查。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方入口](https://openai.com/research/)；复用本日官方RSS1240项的3/8–3/11七条切片及Promptfoo原core；覆盖03-09完整日，不以09:00筛新材料 | 已检查 | Promptfoo仅收购/计划，贡献EX；精选/RSS不证明全部历史 |
| SRC-ANTHROPIC | [官方入口](https://www.anthropic.com/research)；复用本日Research10项/See more同页、Alignment March五项；AuditBench/Abstractive旧事件定点身份 | 受阻 | 主Research历史分页未恢复；March可见切片不等机构全历史 |
| SRC-GOOGLE-AI | [官方入口](https://deepmind.google/research/)；复用本日DeepMind真实page3 24卡/Google March archive12卡3/11→3/6、下一页更早；Pubs仅year | 受阻 | 官方论文日级切片缺口保留；回顾EX，非全研究无命中 |
| SRC-META-AI | [官方入口](https://ai.meta.com/research/)；复用本日Blog page1十卡/page2十二卡；Research/publication入口400 timeout | 受阻 | 需要03-09模型/训练/推理原始历史论文清单；Blog不是全FAIR |
| SRC-QWEN | [官方入口](https://qwenlm.github.io/)；复用本日新public API40项标题/date/path，2/16→3/19跨窗；旧页停2025 | 已检查 | 可见40项无03-09条目；无total，不证完整机构历史 |
| SRC-DEEPSEEK | [官方入口](https://www.deepseek.com/en/news/)；复用本日官方/en/news Research10/News5元数据，2/25→6/24及12/1→4/24 | 已检查 | 可见切片无03-09；不外推View all/删除历史 |
| SRC-MOONSHOT | [官方入口](https://www.kimi.com/en/blog/)；复用本日现官方Kimi Blog19条，2/9→4/20跨窗 | 已检查 | 19可见范围无03-09；不扩repo/release队列 |
| SRC-TENCENT-HUNYUAN | [官方入口](https://hunyuan.tencent.com/research)；复用本日本publicList page1/pageSize20/renderType0，11/11 current total；2/13→4/23 | 已检查 | 当前可见无03-09；入口恢复有效，不证删除历史 |
| SRC-ZAI | [官方入口](https://www.zhipuai.cn/zh/research)；复用本日官方Research15可见卡，2/21→3/15邻接；停View more | 已检查 | 本页无03-09；不把可见15卡称全部历史 |
| SRC-BYTEDANCE-SEED | [官方入口](https://seed.bytedance.com/en/research)；同页API article_type1/year2026/token20/count100/order_descfalse；US18项与默认14项实际比较，next40/moretrue/total82；Feb25/27→Mar2→Mar12，已过目标未来段即停 | 已检查 | 无03-09目录项；US四额外身份1992/1644/1664/1661不遗漏，显示date≠paper first-public；不遍历剩全年 |
| SRC-BAIDU-ERNIE | [官方入口](https://ernie.baidu.com/blog/zh/)；复用本日Blog/zh page1十项；2/6→4/15跨窗，下一页更早 | 已检查 | 可见无03-09；不证其他历史/修订 |
| SRC-XIAOMI-MIMO | [官方入口](https://mimo.xiaomi.com/)；复用本日首页Paper八项2/3→3/13；Blog15标题无日期，/blog为旧单篇 | 受阻 | Paper无03-09；请求带原始日的03-09 Blog切片，不以无日期标题作零 |
| SRC-MINIMAX | [官方入口](https://www.minimax.io/blog)；复用本日英文Blog12卡2/14→3/18；中文redirect shell/Agent Tech heading与llms48行恢复链接不可读 | 受阻 | 英文可见无03-09；Agent历史正文/日期缺口不因llms目录消失 |
| SRC-ARXIV | 本轮四主题submitted缓冲UTC03-05 19:00→03-06 19:00；start0/max200/ascending各87/87、63/63、17/17、83/83页内取完；72完整题摘冻结，宽标题仅发现。48日级区间归属/10 EX/10边界日期/4早稿身份；当前72官方header已轻核 | 已检查 | 约定主题已查；10+4必要日期保留，不授全分类召回；官方03-09列表cache miss不是日级零 |
| SRC-OPENREVIEW | 只触发MoELens GS4WXncwSF、COLD afV4qzquBN、CODEC同题早稿身份/公开history，API403；不扫会议全站 | 受阻 | 精确公开版本日与同事件关系见§5；不以索引相对时间/会期代日 |
| 表外：[Microsoft Research](https://www.microsoft.com/en-us/research/publication/scaling-agentic-capabilities-not-context-efficient-reinforcement-finetuning-for-large-toolspaces/) | ATLAS原页只March2026与同题作者身份，停止L0–17日期恢复 | 受阻 | 需原dated全文/会议公开稿日，不读全文绕日期 |
| 表外：[Real-3DQA作者](https://xianzhengma.github.io/) | News/对应title作者与项目header/BibTeX；Jan22accepted未明示全文同公开 | 受阻 | 需exact-paper原始公开history日；接受/参会非首公开 |


Seed两locale原值：[US18](../_sources/daily-20260310/supplement-seed-us-projection-20261009.json)、[默认14](../_sources/daily-20260310/supplement-seed-default-projection-20261009.json)；有more不意味着遍历目标之后全年。当前72身份官方header/comments/history已实际逐页轻核（[原值](../_sources/daily-20260310/supplement-current-events-20261009.json)）：没有当前撤回/方法伦理/安全纠错标记；PolyBlocks补漏Acknowledgments与Omni后窗优化checkpoint不凭标签触发v1全版史队列。版本重要性按实际变化而非v2名判断。

表外：[Microsoft Research ATLAS](https://www.microsoft.com/en-us/research/publication/scaling-agentic-capabilities-not-context-efficient-reinforcement-finetuning-for-large-toolspaces/)月级元数据及[Real-3DQA作者](https://xianzhengma.github.io/)/[项目](https://real-3dqa.github.io/)必要日级恢复已查但仍受阻。SRC-OPENREVIEW只触发GS4WXncwSF、afV4qzquBN与CODEC早稿精确身份，API403；GraphRAG出版方/DOI亦只核同事件。其余按需源未触发，不做会议或repo全站扫描。

## 3. 候选与判断

原处理冻结：无确定落窗候选（唯一家族分母0）。潜在贡献但日期未证的14项只在§5，不评分、不记标准/深入完成，也不借“暂缓候选”偷换为已确认当窗归属。官方明确关闭或当前撤回项只留筛选原始理由，不为它们建立候选行。

### 补充窗口候选（48唯一家族）

公开日为2026-03-09，依据官方availability finalID/DOI随公告分配、exact-v1 Submitted所在Thu14–Fri14批次最早Sunday20公告给该BJT日下界，与arxiv.content findable DOI实际registered在该日内的可发现上界共同夹证。**不是Submitted/Updated/registered直接作first-public**，也不沿用旧09:00截点；先前稿疑点4项另隔离，不混入48。原始题摘/history/DataCite见四份supplement-abstracts原件与[72分解](../_sources/daily-20260310/supplement-screening72-20261009.md)。作者必要审阅及逐项独立Source/PRE已齐，争议采用界限经独核确认；日级验收依据见§6，不以此表单独授整日验收。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling — 2603.06199v1](https://arxiv.org/abs/2603.06199v1) | 2026-03-09 | pool-key近似block discovery与max-threshold免排序/index jumping；下界非一般保序且有质量掉点；2+2+2=6 | 标准完成 | 已有覆盖 / `INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [Revisiting the (Sub)Optimality of Best-of-N for Inference-Time Alignment — 2603.05739v1](https://arxiv.org/abs/2603.05739v1) | 2026-03-09 | win-rate目标下BoN的pairwise排序误差/尾部coverage及regularized选择；最坏界不授每实例单调；3+1+3=7 | 深入完成 | 整合 / `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [NOBLE: Accelerating Transformers with Nonlinear Low-Rank Branches — 2603.06492v1](https://arxiv.org/abs/2603.06492v1) | 2026-03-09 | pretraining起永久非线性低秩projection支路；不可merge、推理成本与augmentation反侧保留；2+1+2=5 | 深入完成 | 整合 / `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understanding and Editing — 2603.06503v1](https://arxiv.org/abs/2603.06503v1) | 2026-03-09 | 同模型/工具50subset下planner+专用context少token却更慢；联合变化不归因planner单模块；2+1+2=5 | 标准完成 | 已有覆盖 / `AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion — 2603.06397v1](https://arxiv.org/abs/2603.06397v1) | 2026-03-09 | nondecomposable set objective的RL→joint tensor diffusion蒸馏→固定库NN部署替代；实际256-step SDE非单forward，库grounding非事实可信；2+2+2=6 | 深入完成 | 整合 / `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in LLMs — 2603.05618v1](https://arxiv.org/abs/2603.05618v1) | 2026-03-09 | 推理轨迹与最终输出的PII外泄分测及预算/检测器交互；只限prompt内显式重现，混改提示不授reasoning因果；2+2+2=6 | 深入完成 | 已有覆盖 / `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Sparse Crosscoders for diffing MoEs and Dense models — 2603.05805v1](https://arxiv.org/abs/2603.05805v1) | 2026-03-09 | 等active预算模型间crosscoder重建偏置/分区反侧；独有字典feature不等概念唯一；2+1+2=5 | 标准完成 | 已有覆盖 / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Fragility Of Moral Judgment In Large Language Models — 2603.05651v1](https://arxiv.org/abs/2603.05651v1) | 2026-03-09 | 固定冲突下协议扰动与复采噪声的局部比较；评价身份含输出映射/提示协议，不授内在道德能力；2+1+2=5 | 标准完成 | 已有覆盖 / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Structured Multidimensional Representation Learning for Large Language Models — 2603.05727v1](https://arxiv.org/abs/2603.05727v1) | 2026-03-09 | feature谱切片的宽度/容量预算分支；总图深度与Norm同时变化，不授完整Transformer等价或整体4倍服务收益；2+1+2=5 | 标准完成 | 仅报告 / `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models — 2603.05773v1](https://arxiv.org/abs/2603.05773v1) | 2026-03-09 | 有害识别与拒答方向干预的受限行为分离；不授pure正交内因或白盒到API安全迁移；2+2+2=6 | 深入完成 | 已有覆盖 / `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [RouteGoT: Node-Adaptive Routing for Cost-Efficient Graph of Thoughts Reasoning — 2603.05818v1](https://arxiv.org/abs/2603.05818v1) | 2026-03-09 | ordinal最低成功成本与全图budget/fallback分责；all-fail训练隔离，少输出token不等低端到端延迟；2+2+2=6 | 标准完成 | 已有覆盖 / `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [Test-Time Adaptation via Many-Shot Prompting: Benefits, Limits, and Pitfalls — 2603.05829v1](https://arxiv.org/abs/2603.05829v1) | 2026-03-09 | 固定总N的示例选择/顺序条件；隔离GPQA共享test生成过滤，不授模型容量因果；2+1+2=5 | 标准完成 | 已有覆盖 / `AGENT-PROMPT` [Ch74](../../../../books/part-07-agent/74-prompt.md) |
| [ROSE: Reordered SparseGPT for More Accurate One-Shot Large Language Models Pruning — 2603.05878v1](https://arxiv.org/abs/2603.05878v1) | 2026-03-09 | 估大剪枝误差驱动两级离线排序、让更多剩余权重补偿；估计/量化顺序定理不能迁作全剪枝保证；2+1+2=5 | 标准完成 | 已有覆盖 / `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation — 2603.05881v1](https://arxiv.org/abs/2603.05881v1) | 2026-03-09 | confidence先于answer及分段GRPO奖励；当前policy经验正确率与独立真值不同；2+2+2=6 | 标准完成 | 已有覆盖 / `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA — 2603.05931v1](https://arxiv.org/abs/2603.05931v1) | 2026-03-09 | 状态容量内驻片及物理routing约束的GDN数据流分支；综合周期、P&R与功耗估算分责；2+2+2=6 | 标准完成 | 已有覆盖 / `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Omni-Masked Gradient Descent: Memory-Efficient Optimization via Mask Traversal with Improved Convergence — 2603.05960v1](https://arxiv.org/abs/2603.05960v1) | 2026-03-09 | 无放回活跃mask/层选择改变更新coverage；balanced cycle不等每步无偏，AdamW LM不继承SGD理论率；2+1+2=5 | 标准完成 | 已有覆盖 / `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [EvoESAP: Non-Uniform Expert Pruning for Sparse MoE — 2603.06003v1](https://arxiv.org/abs/2603.06003v1) | 2026-03-09 | 层内expert排序与跨层整数预算正交；teacher-forced词表overlap是离线proxy而非在线acceptance；2+1+2=5 | 标准完成 | 已有覆盖 / `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [Diffusion Language Models Are Natively Length-Aware — 2603.06123v1](https://arxiv.org/abs/2603.06123v1) | 2026-03-09 | 首full pass EOS proxy提长度再裁剪canvas；τ非校准证书，质量掉点及batch长度异构保留；2+1+2=5 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Partial Policy Gradients for RL in LLMs — 2603.06138v1](https://arxiv.org/abs/2603.06138v1) | 2026-03-09 | 截断未来reward的局部credit范围；prefix max改终值/最坏Hoeffding界不证明实际方差排序；2+1+2=5 | 争议 | 暂缓 / `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [SPOT: Span-level Pause-of-Thought for Efficient and Interpretable Latent Reasoning in Large Language Models — 2603.06222v1](https://arxiv.org/abs/2603.06222v1) | 2026-03-09 | 冻结head/embedding、外插pause与span训练分支；理想OT退到mean-embedding目标，token结构强归因隔离；2+2+2=6 | 争议 | 暂缓 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty — 2603.06317v1](https://arxiv.org/abs/2603.06317v1) | 2026-03-09 | entropy→校准target→confidence LoRA的目标人口分责；低ECE不等AUROC/每实例/OOD正确；2+1+2=5 | 标准完成 | 已有覆盖 / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Gradient Flow Polarizes Softmax Outputs towards Low-Entropy Solutions — 2603.06248v1](https://arxiv.org/abs/2603.06248v1) | 2026-03-09 | 所列softmax-value梯度流的有限诊断；loss链法/符号与pair量词冲突，强极化定理不采用；2+1+2=5 | 争议 | 暂缓 / `MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Stem: Rethinking Causal Information Flow in Sparse Attention — 2603.06274v1](https://arxiv.org/abs/2603.06274v1) | 2026-03-09 | position依赖与output-aware近似的局部稀疏预算；向量抵消不授top individual norm普遍最优；2+2+2=6 | 标准完成 | 已有覆盖 / `INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [MoEless: Efficient MoE LLM Serving via Serverless Computing — 2603.06350v1](https://arxiv.org/abs/2603.06350v1) | 2026-03-09 | 前层预测replica/placement分支且原router保持权威；层CDF不等SLO，memory×latency不等账单；2+2+2=6 | 标准完成 | 已有覆盖 / `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Dynamic Chunking Diffusion Transformer — 2603.06351v1](https://arxiv.org/abs/2603.06351v1) | 2026-03-09 | 同一步内非均匀二维计算网格再恢复fullgrid；软预算/路由与teacher代价需全计；2+2+2=6 | 深入完成 | 整合 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling — 2603.06403v1](https://arxiv.org/abs/2603.06403v1) | 2026-03-09 | 有限adapter+scheduler观察；CLS causal读取与latency/cost量纲中心冲突，不采用强保证；2+2+2=6 | 争议 | 暂缓 / `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Speak in Context: Multilingual ASR with Speech Context Alignment via Contrastive Learning — 2603.06505v1](https://arxiv.org/abs/2603.06505v1) | 2026-03-09 | 冻结speech/LLM间context contrastive connector；gold→CTC迁移及费用不授语音证据真值；2+1+2=5 | 标准完成 | 已有覆盖 / `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation — 2603.05754v1](https://arxiv.org/abs/2603.05754v1) | 2026-03-09 | pseudo-thermal感知与QP约束过滤的局部接口；感知合成/controller链不授真实全局安全；2+2+2=6 | 深入完成 | 已有覆盖 / `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [EmboAlign: Aligning Video Generation with Compositional Constraints for Zero-Shot Manipulation — 2603.05757v1](https://arxiv.org/abs/2603.05757v1) | 2026-03-09 | VLM组合约束同时用于video选择与trajectory refinement；soft target/retarget不等hard physical safety；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Training-free Latent Inter-Frame Pruning with Attention Recovery — 2603.05811v1](https://arxiv.org/abs/2603.05811v1) | 2026-03-09 | clean zero-noise KV和近期RoPE身份的跨帧复用；mutable denoising与anchor恢复分责，非exact无限时长；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Hierarchical Latent Action Model — 2603.05815v1](https://arxiv.org/abs/2603.05815v1) | 2026-03-09 | observation-only latent层级pretrain再真动作低层finetune；冻结high不等部署无需动作监督；2+1+2=5 | 标准完成 | 已有覆盖 / `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models — 2603.05868v1](https://arxiv.org/abs/2603.05868v1) | 2026-03-09 | 校准view重绘adapter→冻结policy；LVSM域适配/real LoRA仍付费，任意camera免训练不成立；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration — 2603.06001v1](https://arxiv.org/abs/2603.06001v1) | 2026-03-09 | normal与矛盾语言指令分测及白盒sink干预；LGS敏感非矛盾识别/安全abstain；2+2+2=6 | 深入完成 | 已有覆盖 / `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection — 2603.06048v1](https://arxiv.org/abs/2603.06048v1) | 2026-03-09 | 多head reference位置/门控分支；0/1乘logit不阻断softmax，中心hard isolation争议；2+1+2=5 | 争议 | 暂缓 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Cross-Resolution Distribution Matching for Diffusion Distillation — 2603.06136v1](https://arxiv.org/abs/2603.06136v1) | 2026-03-09 | 跨resolution logSNR/state切换与fake-score分支；scalar SNR非全分布等价、threshold冲突隔离；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching — 2603.06331v1](https://arxiv.org/abs/2603.06331v1) | 2026-03-09 | heterogeneous proxy分组reuse/外推与drift触发FULL；proxy非实际世界误差，scale条件与无hard cap保留；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Physical Simulator In-the-Loop Video Generation — 2603.06408v1](https://arxiv.org/abs/2603.06408v1) | 2026-03-09 | simflow与template背景flow/TTCO分工；sim合法与人类偏好非世界物理真值；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [What if? Emulative Simulation with World Models for Situated Reasoning — 2603.06445v1](https://arxiv.org/abs/2603.06445v1) | 2026-03-09 | 想象状态保真/观察相位/下游推理分测；合成轨迹与GPT QA不授真实可执行世界状态；2+1+2=5 | 标准完成 | 已有覆盖 / `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation — 2603.06480v1](https://arxiv.org/abs/2603.06480v1) | 2026-03-09 | salience×novelty/history的有限token选择；OS非STOP可靠，4-action生成延迟非完整控制Hz；2+1+2=5 | 标准完成 | 已有覆盖 / `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion — 2603.06577v1](https://arxiv.org/abs/2603.06577v1) | 2026-03-09 | typed多模态masked路径与tail/EOS/位置软约束；各codec仍不同，forward减量非无损端到端提速；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [CodeScout: Contextual Problem Statement Enhancement for Software Agents — 2603.05744v1](https://arxiv.org/abs/2603.05744v1) | 2026-03-09 | 独立AST/scope issue preparation与trajectory内增强的局部反侧；派生提案不等原事实/可复现故障；2+2+2=6 | 标准完成 | 已有覆盖 / `AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [InfoGatherer: Principled Information Seeking via Evidence Retrieval and Strategic Questioning — 2603.05909v1](https://arxiv.org/abs/2603.05909v1) | 2026-03-09 | 有限hypotheses BBA/ignorance与主动问询信息收益；BBA非事实概率，representation+fallback共变；2+2+2=6 | 标准完成 | 已有覆盖 / `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [The World Won't Stay Still: Programmable Evolution for Agent Benchmarks — 2603.05910v1](https://arxiv.org/abs/2603.05910v1) | 2026-03-09 | 生成环境graph变更下task/test/replay身份重验；coverage非pass，memory反退不授一般因果；2+2+2=6 | 标准完成 | 已有覆盖 / `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality — 2603.05912v1](https://arxiv.org/abs/2603.05912v1) | 2026-03-09 | challenger纠错触发benchmark版本/同版重评分与hiddenmicrogold校准；posthoc一致非accuracy；3+2+2=7 | 深入完成 | 已有覆盖 / `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Agentic LLM Planning via Step-Wise PDDL Simulation: An Empirical Characterisation — 2603.06064v1](https://arxiv.org/abs/2603.06064v1) | 2026-03-09 | 真实STRIPS sim回执与完整计划checker分测；局部成功提升小/token增多，不泛称Agent无效；2+2+2=6 | 标准完成 | 已有覆盖 / `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input — 2603.06444v1](https://arxiv.org/abs/2603.06444v1) | 2026-03-09 | 边界marker、有限ahead和历史窗口重置；TTFA/RTF/等待分责，不授全acoustic state O(k+f)；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Pinterest Canvas: Large-Scale Image Generation at Pinterest — 2603.06453v1](https://arxiv.org/abs/2603.06453v1) | 2026-03-09 | 原product只读区跨生成/codec/SR两次回贴与质量filter；分割/边界误差不授严格全部identity；2+2+2=6 | 标准完成 | 已有覆盖 / `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models — 2603.05828v1](https://arxiv.org/abs/2603.05828v1) | 2026-03-09 | 给定span/context的multiquery与rerank局部消融；equivalence hit不等entailment或真实内部原因；2+1+2=5 | 标准完成 | 已有覆盖 / `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |

## 4. 证据与知识整合

本窗无可正面采用的候选证据，因此没有 Research→Books 新增、已有覆盖或结构改动。ROADMAP owner仅作未来重开路由：Covenant→TRAIN-DISTRIBUTED-TRAINING，EAGLE-Pangu→INFER-SPECULATIVE-DECODING，Ares→AGENT-PLANNING，SlowBA→PLATFORM-SECURITY；映射owner本身不是贡献或整合证明。日期修复后还须核对应实际命题所需方法/对照/边界与Books原论证，不能直接采用现在的题摘/准入校准。

弱侧已定点读到足以决定potential而非完成Evidence：Native Retrieval抽已生成query hidden states并训练两层head，不取消query生成；Table1 MRR .329→.293不支持“97%全面保留”，encoder计时不是全请求21.8×。RoboRouter历史multimodal retrieval与Evaluator消融不只是无证组合，但withdraw引用纠错依赖见§5。PIRA同PIRF有/无视觉noise对precision的受控差异，意图预测不构成行动授权。OfficeQA oracle parsed/PDF与同agent file/vector、table-header修复对照涉及解析/检索收益归因，不因是新benchmark误关。这些材料仅保存消歧证据与反例，不采用任何性能/安全保证。

[有界筛选记录](../_sources/daily-20260310/V3_FINITE_DISCOVERY_STOP.md)保留具名关闭及实际版本/位置：

- Promptfoo：原始RSS3/9 10:00GMT，官方核心22–39只收购与未来Frontier integration计划，未披露可采用的新安全机制或受控评价。
- AuditBench：本次Blog重呈现，不是说旧论文无长期价值；v1 §1/§4.2已含tool→agent gap、三种机制与release。Blog的Qwen32B与v1的14B不同，未见32B受控新边界；SAE case Blog KTO与v1 SFT不一致原样保留，未解释成新受控结果、不采用该差异结论。
- Abstractive red-teaming：month-only Blog核心12–43的category search、CRL/QCI、7×12评价已在2/12唯一v1题摘；没有独立新机制说明，不为本次重呈现另开日期请求。
- AlphaGo3/10回顾：核心123–169复述AlphaGo/Zero和已发模型、科学应用及AGI愿景，没有本次新受控机制。
- SoK 2603.07379v1：完整题摘加定点§IX安全归纳，风险数字引用旧研究，POMDP/taxonomy/研究议程未建立本次可改变具体机制选择的新证据；不泛化所有SoK无价值。
- Caller 2603.07473：最新v2官方撤回，理由为实验方法缺陷与数据伦理问题，仅保留排除依据。定点检索Books和旧本日报告的ID/title无采用链，不声称安全保证；不用撤回版本评分/入书。

### 补充窗口的逐项证据与Books处置

以下不改上方原§4连续正文。全部精确v1关键机制、评价配置、直接反侧、Not Disclosed项与自身推断见[逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；逐项实际已读正文和采用差额见[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。未核实现/未复现，不把作者benchmark推广到完整服务SLO。作者PRE不替代独立复核；48项具体采用/已有覆盖/仅报告/争议边界现均已独核，见§6。

### [FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling — 2603.06199v1](https://arxiv.org/abs/2603.06199v1)

采用边界：pool-key近似block discovery与max-threshold免排序/index jumping；下界非一般保序且有质量掉点。Ch43 95–150、182–209、458–470：approximate discovery、row-max/pooled block 下界与选择费用。不是一般保序或无损。root 必要 Source/PRE 已通过；§3.5/T4 作者最后补读已完成。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Revisiting the (Sub)Optimality of Best-of-N for Inference-Time Alignment — 2603.05739v1](https://arxiv.org/abs/2603.05739v1)

采用边界：win-rate目标下BoN的pairwise排序误差/尾部coverage及regularized选择；最坏界不授每实例单调。root 写 Ch20 Parallel Sampling 后两段与末注：win-rate 目标、pairwise error/coverage 与 M/N 分责；作者实际独立 POST 通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [NOBLE: Accelerating Transformers with Nonlinear Low-Rank Branches — 2603.06492v1](https://arxiv.org/abs/2603.06492v1)

采用边界：pretraining起永久非线性低秩projection支路；不可merge、推理成本与augmentation反侧保留。root 写 Ch17 184–186 与末注：不可 merge 的永久低秩非线性支路/训练与部署代价；作者独立 POST 通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understanding and Editing — 2603.06503v1](https://arxiv.org/abs/2603.06503v1)

采用边界：同模型/工具50subset下planner+专用context少token却更慢；联合变化不归因planner单模块。Ch75 38–72、244–282：capacity、程序化回读/子调用与 compressor+target 总时延；Ch81 292–310 调度费用。少 token 不等少 latency 已承载。50subset 的两组件联合对照仅报告，不称 planner 单因果。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion — 2603.06397v1](https://arxiv.org/abs/2603.06397v1)

采用边界：nondecomposable set objective的RL→joint tensor diffusion蒸馏→固定库NN部署替代；实际256-step SDE非单forward，库grounding非事实可信。root 写 Ch76 setwise段后567/569两段与1342末注：固定 retriever/库/reward→RL fan-out→joint target tensor→diffusion→NN对象部署接口。supplement_20260310实际顺读549–577完整邻接与1337–1347末注、回对§2.3–2.5/3.1/3.4/AppA全部必要原证，非写入者POST通过。迭代采样/预付/漂移再验和事实support边界保留，不授完整RAG加速。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in LLMs — 2603.05618v1](https://arxiv.org/abs/2603.05618v1)

采用边界：推理轨迹与最终输出的PII外泄分测及预算/检测器交互；只限prompt内显式重现，混改提示不授reasoning因果。Ch72 238–280、394–429：detector 是分布/policy sensor，final/tool/获授权 process trace 分测及 U/V 预算。root 已核必要 Source/PRE；计数与曲线争议不采用。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Sparse Crosscoders for diffing MoEs and Dense models — 2603.05805v1](https://arxiv.org/abs/2603.05805v1)

采用边界：等active预算模型间crosscoder重建偏置/分区反侧；独有字典feature不等概念唯一。Ch66 256–284：跨模型重建偏置、字典分区/假阳性与独立 steering，exclusive 不等概念唯一。root 已核 Source/PRE。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [The Fragility Of Moral Judgment In Large Language Models — 2603.05651v1](https://arxiv.org/abs/2603.05651v1)

采用边界：固定冲突下协议扰动与复采噪声的局部比较；评价身份含输出映射/提示协议，不授内在道德能力。Ch66 285–313、338–356：adapter/serialization/retry/environment/scorer 与固定答案 judge prompt 漂移/人工 anchor，协议不等模型内在道德。root 已核 Source/PRE。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Structured Multidimensional Representation Learning for Large Language Models — 2603.05727v1](https://arxiv.org/abs/2603.05727v1)

采用边界：feature谱切片的宽度/容量预算分支；总图深度与Norm同时变化，不授完整Transformer等价或整体4倍服务收益。Ch17 74–112 Norm 跨 hidden dimensions/位置与变换责任；14 108–135 完整 attention 读取。DCT feature slices、窄分支/深度共同变化是此结构分支的有限预算对照；没有证明全 Norm 层谱可分或普遍 Transformer 等价，不将具体模块写为新稳定默认。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models — 2603.05773v1](https://arxiv.org/abs/2603.05773v1)

采用边界：有害识别与拒答方向干预的受限行为分离；不授pure正交内因或白盒到API安全迁移。Ch17 395–406 readout、minimal pair、patching、weight revision/utility 外验；Ch72 588–603 refusal 管理访问不等消除能力。受限方向干预不签独立/唯一 harm-refusal 内因。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [RouteGoT: Node-Adaptive Routing for Cost-Efficient Graph of Thoughts Reasoning — 2603.05818v1](https://arxiv.org/abs/2603.05818v1)

采用边界：ordinal最低成功成本与全图budget/fallback分责；all-fail训练隔离，少输出token不等低端到端延迟。Ch79 191–230 搜索预算/训练 teacher 与 runtime controller、297–310 不确定性与实际费用、368–388 完整 verifier。ordinal 成功路径路由 recipe 和 QA full 更慢仅报告，不将 all-fail 删除后的 proxy 当部署质量保证。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Test-Time Adaptation via Many-Shot Prompting: Benefits, Limits, and Pitfalls — 2603.05829v1](https://arxiv.org/abs/2603.05829v1)

采用边界：固定总N的示例选择/顺序条件；隔离GPQA共享test生成过滤，不授模型容量因果。Ch74 67–94 示例质量/覆盖/顺序，Ch75 38–72、244–282 容量与前置成本；固定 N 选择/顺序边界。root Source/PRE 通过；GPQA test 生成/过滤不采用。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [ROSE: Reordered SparseGPT for More Accurate One-Shot Large Language Models Pruning — 2603.05878v1](https://arxiv.org/abs/2603.05878v1)

采用边界：估大剪枝误差驱动两级离线排序、让更多剩余权重补偿；估计/量化顺序定理不能迁作全剪枝保证。Ch49 505–517 稀疏 artifact、局部重构/真实 kernel admission，2183–2199 更新顺序与误差度量分责。两级大误差优先剪枝是局部新 recipe，仅报告；不迁移量化 fixed-order 等价证明。root Source/PRE 通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation — 2603.05881v1](https://arxiv.org/abs/2603.05881v1)

采用边界：confidence先于answer及分段GRPO奖励；当前policy经验正确率与独立真值不同。Ch33 369–387 prefix confidence/scorer 与 outcome/update 目标分责，802–855 segment credit 边界，870–904 reward 测量身份。Brier segment 配方局部评价保留，不由自采 target 授独立正确率/因果 credit。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA — 2603.05931v1](https://arxiv.org/abs/2603.05931v1)

采用边界：状态容量内驻片及物理routing约束的GDN数据流分支；综合周期、P&R与功耗估算分责。Ch22 460–560 GDN 状态数学；Ch54 16–35、120–142、488–550 片上减少物化/HBM往返、真实生命周期与 hardware verification。root Source/PRE 通过，特定 FPGA layout/P&R 与估算数字仅报告。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Omni-Masked Gradient Descent: Memory-Efficient Optimization via Mask Traversal with Improved Convergence — 2603.05960v1](https://arxiv.org/abs/2603.05960v1)

采用边界：无放回活跃mask/层选择改变更新coverage；balanced cycle不等每步无偏，AdamW LM不继承SGD理论率。Ch28 298–336、512–545 活跃更新/optimizer state，800–915 layer LR 非活跃集合；Ch30 149–175 轮换原参数层/历史 optimizer 驻留。只采更新顺序/coverage 的条件分支；root Source/PRE 通过，不授逐步无偏/AdamW LM 理论率。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [EvoESAP: Non-Uniform Expert Pruning for Sparse MoE — 2603.06003v1](https://arxiv.org/abs/2603.06003v1)

采用边界：层内expert排序与跨层整数预算正交；teacher-forced词表overlap是离线proxy而非在线acceptance。Ch21 600–640 layer budget、离线 contribution/teacher 特定校准；Ch49 780–817 执行状态费用。层内排序与跨层预算分责已承载。固定 teacher-forced overlap/搜索仅报告，非 online acceptance，反退和不同 GPU 费用保留。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Diffusion Language Models Are Natively Length-Aware — 2603.06123v1](https://arxiv.org/abs/2603.06123v1)

采用边界：首full pass EOS proxy提长度再裁剪canvas；τ非校准证书，质量掉点及batch长度异构保留。Ch24 1778–1807 长度 admission、画布坐标、EOS/VOID 与 commit/质量分责；首 full pass 代理/τ recipe 仅报告。root Source/PRE 通过，FLOPs 非 wall-clock。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Partial Policy Gradients for RL in LLMs — 2603.06138v1](https://arxiv.org/abs/2603.06138v1)

采用边界：截断未来reward的局部credit范围；prefix max改终值/最坏Hoeffding界不证明实际方差排序。Ch33 369–387/802–855 前缀估计与分段监督不能自授终局等价。prefix max 改终值、未校正离线 ρ/actual variance 强 claim 争议隔离；窄 shaping recipe 仅报告。需原作者明确目标/采样校正才能重开，不跑代码绕公式冲突。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [SPOT: Span-level Pause-of-Thought for Efficient and Interpretable Latent Reasoning in Large Language Models — 2603.06222v1](https://arxiv.org/abs/2603.06222v1)

采用边界：冻结head/embedding、外插pause与span训练分支；理想OT退到mean-embedding目标，token结构强归因隔离。Ch24 1278–1300 冻结表示与迁移上限、Ch23 653–669 对齐不等几何真值。理想 fixed ε/marginal 下 OT 退为 mean φ(h) 的推导由我们给出，不授额外 token 结构；pause+mapping 窄分支仅报告。root 必要公式独核通过，需作者解释 pooling/归一/ε/数值差额。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty — 2603.06317v1](https://arxiv.org/abs/2603.06317v1)

采用边界：entropy→校准target→confidence LoRA的目标人口分责；低ECE不等AUROC/每实例/OOD正确。Ch66 723–738 evolving uncertainty sensor 与独立 correctness、Ch33 369–387 prefix BCE/relative margin 目标不同；VN entropy→Platt→confidence LoRA recipe 仅报告，低 ECE 不认证 Brier/AUROC/OOD 每实例。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Gradient Flow Polarizes Softmax Outputs towards Low-Entropy Solutions — 2603.06248v1](https://arxiv.org/abs/2603.06248v1)

采用边界：所列softmax-value梯度流的有限诊断；loss链法/符号与pair量词冲突，强极化定理不采用。Eq6/7 与 Appendix15/16 符号冲突、pair 求和口径不一致；Ch14 108–135 attention 路由/Value 方向不等语义贡献可复用，但不能补其中心证明。需作者更正公式与适用条件。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Stem: Rethinking Causal Information Flow in Sparse Attention — 2603.06274v1](https://arxiv.org/abs/2603.06274v1)

采用边界：position依赖与output-aware近似的局部稀疏预算；向量抵消不授top individual norm普遍最优。Ch14 123–135 mass、Value 尺度/方向/抵消与执行选择费用，Ch43 95–150/182–209 approximate selector/error budget。TPD/OAM proxy 与 anti-diagonal/minimum/sink recipe 仅报告，不授全模型最优或语义因果。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [MoEless: Efficient MoE LLM Serving via Serverless Computing — 2603.06350v1](https://arxiv.org/abs/2603.06350v1)

采用边界：前层预测replica/placement分支且原router保持权威；层CDF不等SLO，memory×latency不等账单。Ch21 780–857 router 语义与 replicas/placement epoch，Ch49 696–780 前层预测 expert cohort→暖复制与 async 费用、正常 router 仍权威。采用的早预测分责有具体 coverage；CDF×latency 不签 SLO/账单。 root实际必要Source/PRE已通过。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Dynamic Chunking Diffusion Transformer — 2603.06351v1](https://arxiv.org/abs/2603.06351v1)

采用边界：同一步内非均匀二维计算网格再恢复fullgrid；软预算/路由与teacher代价需全计。root 已写 Ch24 1274–1276 全局 patch 段之后两段与1859末注；supplement_20260310非写入者实际顺读1258–1285完整邻接、1853–1864末注，回对§3.1–3.5/4.1–4.4必要原证，POST通过。非均匀2D grid→Gaussian/nearest plugback→fullgrid decoder/residual，软预算/全部费用/teacher条件与旧路径边界近文，不授DAY。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling — 2603.06403v1](https://arxiv.org/abs/2603.06403v1)

采用边界：有限adapter+scheduler观察；CLS causal读取与latency/cost量纲中心冲突，不采用强保证。cost/latency 单位、causal CLS 读取未来和 reward 区间口径冲突；Ch20 230–282 校准排序/预算不等 correctness 可复用，不补齐中心目标。需实际 mask/cost objective 原件。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Speak in Context: Multilingual ASR with Speech Context Alignment via Contrastive Learning — 2603.06505v1](https://arxiv.org/abs/2603.06505v1)

采用边界：冻结speech/LLM间context contrastive connector；gold→CTC迁移及费用不授语音证据真值。Ch23 518–546 input/训练/部署信息责任、653–669 对齐与原模态 evidence 分责、727–743 encoder/时间/provenance。speech-context contrastive connector 与 gold→CTC retrieval 迁移仅本配方，不授语音内容/对齐真值。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation — 2603.05754v1](https://arxiv.org/abs/2603.05754v1)

采用边界：pseudo-thermal感知与QP约束过滤的局部接口；感知合成/controller链不授真实全局安全。Ch26 725–815 全感知/transfer/controller 链费用，882–965 safety envelope，1170–1226 sensor/projection/真实控制 guard。pseudo thermal/QP 局部机制保留，不授全局安全或 recover。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [EmboAlign: Aligning Video Generation with Compositional Constraints for Zero-Shot Manipulation — 2603.05757v1](https://arxiv.org/abs/2603.05757v1)

采用边界：VLM组合约束同时用于video选择与trajectory refinement；soft target/retarget不等hard physical safety。Ch26 882–965 imagined proposal/constraint/controller 分权、1170–1226 约束投影与独立动作验收。两次 VLM+retarget/SLSQP recipe 和 6×10 有限联合对照仅报告，非 soft target=hard physical safety。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Training-free Latent Inter-Frame Pruning with Attention Recovery — 2603.05811v1](https://arxiv.org/abs/2603.05811v1)

采用边界：clean zero-noise KV和近期RoPE身份的跨帧复用；mutable denoising与anchor恢复分责，非exact无限时长。Ch24 1302–1345 mutable denoising state 与 clean 条件、1350–1440 per-phase anchor/cache budget 与 refresh。clean zero-noise KV/近期 RoPE identity 采用范围具体覆盖，不授 exact/无限时长。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Hierarchical Latent Action Model — 2603.05815v1](https://arxiv.org/abs/2603.05815v1)

采用边界：observation-only latent层级pretrain再真动作低层finetune；冻结high不等部署无需动作监督。Ch26 135–153 high-level latent target→embodiment decoder/controller、1170–1226 latent 监督非可执行动作。freeze high/finetune low 条件分支及更深未更优仅报告，不授 observation-only 部署。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models — 2603.05868v1](https://arxiv.org/abs/2603.05868v1)

采用边界：校准view重绘adapter→冻结policy；LVSM域适配/real LoRA仍付费，任意camera免训练不成立。Ch26 725–815 camera/coordinate/calibration、adapter费用与全 loop 验收。视图重绘 adapter→frozen policy 具体 recipe 留报告，sim 还要 LVSM FT、real policy 先 LoRA，不称任意 camera 免训练/安全。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration — 2603.06001v1](https://arxiv.org/abs/2603.06001v1)

采用边界：normal与矛盾语言指令分测及白盒sink干预；LGS敏感非矛盾识别/安全abstain。Ch26 1170–1226 sensor敏感与controller guard、1350–1378 task/sensor attack 与 clean recovery；Ch66 285–313 评价对象身份。normal/contradictory instruction 分测已承载，LGS 敏感不是识别矛盾或安全 abstain。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection — 2603.06048v1](https://arxiv.org/abs/2603.06048v1)

采用边界：多head reference位置/门控分支；0/1乘logit不阻断softmax，中心hard isolation争议。Ch14 132 binary multiply mask 不等−∞可见性、Ch24 79–81 区域编辑/decoder验收；中心 hard isolation 与 Eq8/9 冲突隔离，RoPE 非一般单调。需作者真实 mask/公式原件，窄 gating recipe 仅报告。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Cross-Resolution Distribution Matching for Diffusion Distillation — 2603.06136v1](https://arxiv.org/abs/2603.06136v1)

采用边界：跨resolution logSNR/state切换与fake-score分支；scalar SNR非全分布等价、threshold冲突隔离。Ch24 939–1028 跨 resolution draft/semantic lock、1125–1345 noise/parameterization/solver/codec身份。logSNR state 切换分责已承载；fake score recipe、threshold 冲突与 teacher 费用仅报告，不授 full distribution match。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching — 2603.06331v1](https://arxiv.org/abs/2603.06331v1)

采用边界：heterogeneous proxy分组reuse/外推与drift触发FULL；proxy非实际世界误差，scale条件与无hard cap保留。Ch24 1350–1440 FULL anchor/每chunk phase/累计displacement/proxy触发refresh、identity与全部费用。分组近似 proxy 非观测误差/物理曲率，scale条件与缺hard cap仅报告。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Physical Simulator In-the-Loop Video Generation — 2603.06408v1](https://arxiv.org/abs/2603.06408v1)

采用边界：simflow与template背景flow/TTCO分工；sim合法与人类偏好非世界物理真值。Ch25 1185–1223 Reason/Execute/Render 不同状态、1266–1272 veracity/influence/克制三证据；Ch26 882–965真实控制。simulator 合法/偏好非世界真值，hybridflow/TTCO recipe 留报告。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [What if? Emulative Simulation with World Models for Situated Reasoning — 2603.06445v1](https://arxiv.org/abs/2603.06445v1)

采用边界：想象状态保真/观察相位/下游推理分测；合成轨迹与GPT QA不授真实可执行世界状态。Ch25 1185–1223 visual proxy非世界真值、1266–1272 状态真实性与下游决策效果分测。合成路径/GPT QA/real observation 相位只有限评价人口，不能将可视化认作真实可执行状态。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation — 2603.06480v1](https://arxiv.org/abs/2603.06480v1)

采用边界：salience×novelty/history的有限token选择；OS非STOP可靠，4-action生成延迟非完整控制Hz。Ch23 518–546 selector/proxy/原token/预算分责；Ch26 725–815全loop费用和action identity。salience×novelty/history MMR recipe 与 joint 反侧仅报告；OS≠STOP success、生成4-action latency非控制Hz。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion — 2603.06577v1](https://arxiv.org/abs/2603.06577v1)

采用边界：typed多模态masked路径与tail/EOS/位置软约束；各codec仍不同，forward减量非无损端到端提速。Ch24 1020–1125 typed unified路径不删codec、1778–1792 PAD/EOS/length与commit分责。tail mask/logit熵软位置/initial length是局部recipe，不授同codec或硬顺序/无损加速。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [CodeScout: Contextual Problem Statement Enhancement for Software Agents — 2603.05744v1](https://arxiv.org/abs/2603.05744v1)

采用边界：独立AST/scope issue preparation与trajectory内增强的局部反侧；派生提案不等原事实/可复现故障。Ch75 70–109 dependency事实/AST-symbol派生view/assembly 与独立生成提示，244–282 prep+target费用；Ch81 1091–1098 exact code verifier。issueaugmentation只派生提案，scope/filter/newrunner identity不能当实际reproduction；局部独立prep优于trajectory内增强不普遍化。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [InfoGatherer: Principled Information Seeking via Evidence Retrieval and Strategic Questioning — 2603.05909v1](https://arxiv.org/abs/2603.05909v1)

采用边界：有限hypotheses BBA/ignorance与主动问询信息收益；BBA非事实概率，representation+fallback共变。Ch79 297–310 calibrated prior/expected info gain→ask/explore/cost/fallback。BBA ignorance/discord recipe未成事实概率，representation+fallback联合改变不授DS唯一收益；root已完成实际必要Source/PRE独核。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [The World Won't Stay Still: Programmable Evolution for Agent Benchmarks — 2603.05910v1](https://arxiv.org/abs/2603.05910v1)

采用边界：生成环境graph变更下task/test/replay身份重验；coverage非pass，memory反退不授一般因果。Ch81 177–209 template/runtime graph/trace，931–967 synthetic环境先验结构/语义/可行性与test版本；1091–1098 verifier identity。coverage≠pass、环境/任务共变与memory反退仅报告；root已完成实际必要Source/PRE独核。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality — 2603.05912v1](https://arxiv.org/abs/2603.05912v1)

采用边界：challenger纠错触发benchmark版本/同版重评分与hiddenmicrogold校准；posthoc一致非accuracy。Ch66 1534–1538 trace反例→owner裁定→固定version及修前后重跑，865–892 typed verifier/聚合可重算；采用纠错权限/同版本重评分已有覆盖。hiddenmicrogold/5%再校准具体recipe仅报告，posthoc一致非accuracy；root已完成实际必要Source/PRE独核。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Agentic LLM Planning via Step-Wise PDDL Simulation: An Empirical Characterisation — 2603.06064v1](https://arxiv.org/abs/2603.06064v1)

采用边界：真实STRIPS sim回执与完整计划checker分测；局部成功提升小/token增多，不泛称Agent无效。Ch79 191–230 symbolic executor合法不等终局计划、368–388 milestone与完整checker；Ch81 931–955 deterministic state测试与model success分测。真实sim observation不等goal-distance，有限65→68/5.7×token负面留报告，不授所有Agent失效。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input — 2603.06444v1](https://arxiv.org/abs/2603.06444v1)

采用边界：边界marker、有限ahead和历史窗口重置；TTFA/RTF/等待分责，不授全acoustic state O(k+f)。Ch24 712–727 有限lookahead chunk renderer/码层vs时间帧、首包费用、RTF≠SLO与播放不可rollback；marker/reset具体训练配方仅报告，ahead等待另计，不授全部状态O(k+f)。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [Pinterest Canvas: Large-Scale Image Generation at Pinterest — 2603.06453v1](https://arxiv.org/abs/2603.06453v1)

采用边界：原product只读区跨生成/codec/SR两次回贴与质量filter；分割/边界误差不授严格全部identity。Ch24 79–81 local改写不能保未mask区、171 nonlinearcodec mask leakage、1163–1176独立decoder/输出验收。原图/生成region/最终像素分别验收，双回贴/VAEharmonization与qualityfilter工业recipe仅报告，segmentation非全identity保证。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

### [HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models — 2603.05828v1](https://arxiv.org/abs/2603.05828v1)

采用边界：给定span/context的multiquery与rerank局部消融；equivalence hit不等entailment或真实内部原因。Ch76 496–500 crossencoder ranking、581–613 relevance/sufficiency/claim-support三层及人工anchor；span/context/MQ/rerank有限诊断保留。equivalence cosine hit非entailment/真实内因；root已完成实际必要Source/PRE独核。 [逐项原证与反侧](../_sources/daily-20260310/supplement-evidence-notes-20261009.md)；[实际Books PRE](../_sources/daily-20260310/supplement-books-pre-20261009.md)。

## 5. 缺口与下一步

### 原处理缺口（冻结，仅原窗口）

普通可执行待办0，root最终日Gate已通过。以下为本窗外部终态保留项，不支持正面证据、Books或无遗漏断言；以后只按具体条件重开受影响材料。现有日期不确定性不是“14项论文已审完”，来源缺口也不等于Coverage无遗漏通过。

日期依据：实际读取[官方availability](https://info.arxiv.org/help/availability.html)的no-advance ID/DOI与Eastern公告schedule、[官方DOI说明](https://info.arxiv.org/help/doi.html)，以及DataCite[created/registered定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)和[DOI states](https://support.datacite.org/docs/doi-states)。本日DST后Monday20:00EDT对应Tuesday08:00BJT。以下v1 Submitted均在3/6 Friday14:00Eastern之后至3/9 Monday14:00之前，最早可公告下界为3/10 08:00；arxiv.content拥有、findable DOI的registered原值给公告不晚于该秒的上界，转BJT加1秒表示半开区间。created/Updated不作为public时间。所有上界均晚于09:00，故只有跨窗范围而非确定本窗公告；不证明更早作者页面不存在。

首8原值见[DataCite原始字段](../_sources/daily-20260310/V3_DATACITE_FIRST_BATCH_RAW.json)，后6见[同样live字段](../_sources/daily-20260310/V3_DATACITE_TAIL_DATE_FIELDS.json)。旧 reconciliation的scheduled_match使用created+schedule猜公告，其自身说明月目录只证明收录，不证明具体首批；本次未采用。一次有界实际官方批次恢复（/list/cs/2026-03-10及cs.DC日期页、月目录目标页）cache miss，已有原始月页定点未给上述身份实际日批次。当前停止，不继续公告代码考古或凭推定slot强纳。

以下每个身份只提出一次日期请求：需要可核的官方实际首次公告批次/时间，或原始作者首次公开正文及时间，足以证明整个时间范围落在本窗；收到后只重开该身份的日期与对应采用命题，不重扫列表，不默认题摘即可入书。

| 材料与精确版本 | 原文具体potential，未证为当窗 | registered原值（UTC）→复合上界BJT（不含） |
| --- | --- | --- |
| [Covenant 2603.08163v1](https://arxiv.org/abs/2603.08163v1) | 动态非白名单peer实际训练的参与/结果接纳边界；不以72B或chain名准入 | 2026-03-10T04:24:49Z → 2026-03-10T12:24:50+08:00 |
| [EAGLE-Pangu 2603.08088v1](https://arxiv.org/abs/2603.08088v1) | branch/commit、safe indexing、fused/eager backend接口 | 2026-03-10T04:23:02Z → 2026-03-10T12:23:03+08:00 |
| [Ares 2603.07915v1](https://arxiv.org/abs/2603.07915v1) | 逐step最低成功effort标签/history router；标签选择与反事实仍需Evidence | 2026-03-10T04:18:55Z → 2026-03-10T12:18:56+08:00 |
| [SlowBA 2603.08316v1](https://arxiv.org/abs/2603.08316v1) | 维持动作正确率却制造资源退化的安全反证；日期恢复后必要定点深入 | 2026-03-10T04:28:23Z → 2026-03-10T12:28:24+08:00 |
| [Native Retrieval 2603.08429v1](https://arxiv.org/abs/2603.08429v1) | encoder成本与embedding质量取舍，保留非端到端计时/MRR反例 | 2026-03-10T04:31:04Z → 2026-03-10T12:31:05+08:00 |
| [RoboRouter 2603.07892v1](https://arxiv.org/abs/2603.07892v1) | 历史multimodal retrieval、Evaluator对routing的受控差异；另有引用纠错依赖 | 2026-03-10T04:18:23Z → 2026-03-10T12:18:24+08:00 |
| [PIRA 2603.08013v1](https://arxiv.org/abs/2603.08013v1) | 同PIRF clean/noise precision退化，主动意图评价盲区 | 2026-03-10T04:21:17Z → 2026-03-10T12:21:18+08:00 |
| [OfficeQA 2603.08655v1](https://arxiv.org/abs/2603.08655v1) | oracle parsed/table-header修复与file/vector对照的收益归因边界 | 2026-03-10T04:36:43Z → 2026-03-10T12:36:44+08:00 |
| [NEST 2603.06798v1](https://arxiv.org/abs/2603.06798v1) | network/memory feasibility联接DP搜索，而非仅吞吐数字 | 2026-03-10T03:52:34Z → 2026-03-10T11:52:35+08:00 |
| [Swimba 2603.06938v1](https://arxiv.org/abs/2603.06938v1) | expert参数空间混合维持单state recurrence，与多trajectory不同 | 2026-03-10T03:55:55Z → 2026-03-10T11:55:56+08:00 |
| [CAMEL 2603.08022v1](https://arxiv.org/abs/2603.08022v1) | capacity×mixture非线性与固定拟合预算跨scale分配 | 2026-03-10T04:21:29Z → 2026-03-10T12:21:30+08:00 |
| [LiveWorld 2603.07145v1](https://arxiv.org/abs/2603.07145v1) | out-of-sight实体持续推进，而非静态观察memory | 2026-03-10T04:00:44Z → 2026-03-10T12:00:45+08:00 |
| [KohakuRAG 2603.07612v1](https://arxiv.org/abs/2603.07612v1) | prompt ordering/retry/blank-voting消融的数值引用取舍待核，不仅排行 | 2026-03-10T04:11:48Z → 2026-03-10T12:11:49+08:00 |
| [Governance 2603.07191v1](https://arxiv.org/abs/2603.07191v1) | 两种cascade的IR/FPR和资源选择潜在受限对照；不采用四层名或robust保证 | 2026-03-10T04:01:49Z → 2026-03-10T12:01:50+08:00 |

RoboRouter不能只补日期便直接采用：[v2](https://arxiv.org/abs/2603.07892v2) Submitted 3/10T02:21:36Z撤回，comment指出错误引用须移除；[v4](https://arxiv.org/abs/2603.07892v4)6/24已恢复且header无当前撤回标记。v2不入选、不评分、不进入Books；不把后来有效v4误作全部家族撤回。本次v1的重开须日期证据与引用纠错受影响范围核，后窗v3/v4不是本窗revision触发。

有限来源外部请求（不重复无限恢复）：Meta的publication历史入口400 timeout，需要本窗模型/训练/推理论文清单及原始日期；Anthropic主Research历史分页未提供，Google Pubs仅年份，需要3/9–3/10主线论文原始发布切片，不能拿当前精选反证无命中；MiMo Blog首页15无日期标题/More未可读、/blog单篇旧稿，需要本窗Blog历史分页或带官方原始时间的文章；MiniMax Agent techblog链接不可读且当前llms目录非历史，需要本窗Tech Blog正文/日期或当时官方可核归档。替代材料均须是官方目录、作者原始发布/确切版本与日期，不接受搜索零命中作为覆盖证据。到达时只重开对应来源本窗切片与具体材料。

窗外材料只保留路由：AuditBench v3 Submitted3/9T18:35:46Z晚于Monday18:00Z deadline，最早公告3/11 08BJT，不以v3变更反填本窗；Abstractive唯一v1为2/12，不归本日；OpenAI instruction hierarchy/Responses电脑环境、A3与Meta MTIA属于后窗，未声明已完成其研究。Caller7/21撤回信号属于当次检查的必要不采用依据，不当作本窗新增研究贡献。以上均不扩张本窗或替代其目标日工作。

### 补充窗口：普通工作与外部保留分开

48项作者必要Source/PRE与全部独立复核齐，四项实际整合POST通过；root六部分最终非作者日级验收通过，候选/证据/Books/复核普通可执行待办0。无新增同query分页或已读源可执行扫描，不扩发现池。下列保留项只按具体外部材料重开，不支持正面证据、Books或无遗漏断言。

以下14项已做本日必要有界原入口恢复，安全隔离不评分、不作确定本窗候选/正面Evidence/Books/全源覆盖。每个材料只请求一次：需要该精确稿官方实际公开批次/出版方公开日，或作者首次公开全文dated公告及身份关系；仅有Submitted/registered/acceptance/搜索索引不够。可接受替代是同一版本原始发布或当时官方归档，取得后只重开对应日期和准入/采用命题，不读全文猜日期、不遍历他日。具体停点见[日期恢复](../_sources/daily-20260310/supplement-date-recovery-20261009.md)。

| 精确v1身份 | 当前日期限制（registered只是上界，UTC） | 必要材料/定点重开 |
| --- | --- | --- |
| [MSA 2603.23516v1](https://arxiv.org/abs/2603.23516v1) | 03-26T01:55:45Z | 作者原press公开正文日；Mar19转载不能代原证 |
| [Orion 2603.06728v1](https://arxiv.org/abs/2603.06728v1) | 03-10T03:50:57Z | Mar5作者代码/Reddit不等exactpaper，需原稿dated公告 |
| [PolyBlocks 2603.06731v1](https://arxiv.org/abs/2603.06731v1) | 03-10T03:51:01Z | 需官方批次或作者dated全文公告 |
| [Model2Kernel 2603.24595v1](https://arxiv.org/abs/2603.24595v1) | 03-27T01:49:11Z | 安全潜力不绕必要日，需原稿公开公告/批次 |
| [HeteroDDM 2603.06741v1](https://arxiv.org/abs/2603.06741v1) | 03-10T03:51:15Z | Bagel Mar11 archive非日级原稿证明 |
| [StableDRL 2603.06743v1](https://arxiv.org/abs/2603.06743v1) | 03-10T03:51:17Z | HF Submitted/社区时间非首公开 |
| [Gauge 2603.06774v1](https://arxiv.org/abs/2603.06774v1) | 03-10T03:52:00Z | 作者CV Submitted JMLR非公开日 |
| [InfoVLA 2603.13335v1](https://arxiv.org/abs/2603.13335v1) | 03-17T03:49:24Z | 需原作者dated公告或真实原批次 |
| [ATLAS 2603.06713v1](https://arxiv.org/abs/2603.06713v1) | 03-10T03:50:36Z | MSR只有March；需exact会议公开稿日/作者共发说明 |
| [Real-3DQA 2603.23523v1](https://arxiv.org/abs/2603.23523v1) | 03-26T01:55:54Z | Jan22accepted非明确全文同时公开；需exact OpenReview原稿公开日 |
| [GraphRAG 2603.05698v1](https://arxiv.org/abs/2603.05698v1) | 先前身份 | DOI10.1109/SMC58881.2025.11343466：Crossref Jan28created/Feb11deposit与SMC2025非确定首公开日；需publisher公开日/作者原稿关系 |
| [MoELens 2603.05806v1](https://arxiv.org/abs/2603.05806v1) | 先前身份 | SLLM2025 GS4WXncwSF，需原稿公开版本及与v1同事件关系 |
| [COLD-Steer 2603.06495v1](https://arxiv.org/abs/2603.06495v1) | 先前身份 | afV4qzquBN API403，需原OpenReview公开history+精确原稿 |
| [CODEC 2603.06557v1](https://arxiv.org/abs/2603.06557v1) | 先前身份 | OpenReview稿/作者ICLR2026只有年，API403；需同题同作者exact公开history，不靠会期/索引相对时间 |

中心争议（保留候选身份但不正面采用争议主张）：PPG06138需原作者明确prefix-max目标是否保原终值/离线ρ校正及actual variance证明；SPOT06222需作者说明pool在φ前后、normalization/fixedε或数值solver条件，才重开token-structure归因（mean等价是我们对公式的推导，非代码复现）；Polarization06248需Eq6/7与Appendix15/16符号/pair量词更正；Bandit06403需CLS causal-mask调整、Eq26–28/token与FLOPs量纲/预算口径原件；GenHOI06048需真实−∞mask或可核执行材料说明Eq8/9的0/1乘logit冲突。有限机制/观察只报告，不能通用已有覆盖补齐强定理/安全隔离。必要局部原证已读并独核，不是尚未读取造成的hold。

本轮来源外部请求：Meta/Anthropic/Google需要03-09主线研究的官方日级历史目录及原始发布；MiMo需要03-09 Blog原始日期/正文切片；MiniMax Agent Tech需要03-09原Tech Blog正文/日期或官方归档。已尽有限入口，不拿当前精选/搜索零命中授无遗漏。收到只重开对应来源03-09切片。原轮14旧日期保留不搬移；本轮新增日级48不因旧09:00隔离理由重新hold。窗外当前修订只留身份/信号，不扩本次窗口。

## 6. 复核

### 原处理复核（冻结，不替代补查验收）

复核者：root（非报告作者）
结论：通过

root实际完整检查本六部分与新增有限发现文件、14源结果/停点/查询参数、0确定候选和14日期隔离的计数/请求，确认不采用withdraw版本、无Books写入待POST。复用已经完成且未变化的独立校准：root逐项读取首8官方完整题摘/历史，通过潜在贡献但明确未证明日期；Promptfoo core、AuditBench Blog及v1 §1/§4.2、Abstractive Blog核心及唯一v1题摘、AlphaGo回顾由root实际定点核；SoK完整题摘代表性负侧通过。RoboRouter v2引用撤回与v4当前header、Caller最新撤回comment由root实际核。新增6个potential的完整题摘仅作者已读，root未逐项重读；其余metadata没有root逐项题摘复核，本次不称全库存初筛或全文验收。

最终Gate通过；发现的来源结果非枚举、被引有限停点缺失、AuditBench ID及DeepMind页卡数均已实际修正并由root核验。机器校验已通过：`python3 scripts/validate_research.py --report papers/2026/03/10/README.md`；限定本日报告/日_sources的`git diff --check`无错误，root亦实际复验。结果不替代非作者语义验收；未stage、commit或push。

### 本轮增量复核（最终日级验收）

复核者：root（非报告作者；后22必要Source/PRE由其协调fresh-context review_mar10_remaining实际独核）
结论：通过（含明确隔离的外部终态保留项，不是全部Coverage/Evidence通过）

root实际完整独读冻结72份exact-v1题摘、全部拟入选准入和决定性8EX core/2 taxonomy议程EX；Dream不因小robot/negative关闭，R4T由初稿拟EX改为候选，Dense/TML/LIT/Harvest/PONTE/MAS/ESAA有具体core理由改EX，BRTR受限少token≠少latency反侧保留。宽query不变逐项队列。前26必要Source/owner按实际分批校准复用；review_mar10_remaining实际独核后22必要方法/评价/直接反侧和指定owner局部，确认21具体已有覆盖、GenHOI中心hold，root已收到全部逐项范围。48项必要证据与具体Books采用/保留边界独核齐，不称全部作者宣传已证。

实际Books改动由root本人窄写，supplement_20260310非写入者独立顺读四处新增两段、完整局部前后与末注且回对必要原证，BoN Ch20、NOBLE Ch17、DC-DiT Ch24、R4T Ch76 POST通过。root随后实际顺读最终六部分，核对14每日来源及实际触发来源的范围/停止点、72题摘的48/10/10/4分解、全部候选处置、五中心争议及去重材料请求，确认没有未处理的普通工作。当前72官方信号轻核与14必要日期保留不等全部事件史/全源召回。完成态V3、160个本地引用存在性、48新增家族唯一性、原候选0/原窗口/连续§4前缀冻结及本日/四处Books限定cached与unstaged diff检查均通过；格式检查不替代上述实际语义验收。未stage、commit、push；报告作者未写共享Books/LS/index，root只落实本日四处书稿差额并同步必要恢复停点。
