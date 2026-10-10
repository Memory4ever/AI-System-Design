# Daily Research — 2025-07-11

**规范：** V3
**窗口：** 2025-07-10T09:00:00+08:00 ～ 2025-07-11T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T00:52:13+08:00

## 1. 结论

本日发现了可改变设计判断的线索，但没有材料获得足以完全落入本窗的原始公开时间证据；这不是“零事件”结论。KVFlow 将已知工作流未来执行顺序用于 KV 淘汰/预取，Synergy Dilemma 给出 Long-CoT SFT 与 RL 不必叠加的反证，H-Net 的动态 chunking 与 byte-level compute trade-off 也值得继续核验。它们均隔离为外部保留项，不计当窗正式候选、不评分、不写入 Books，也不支撑历史来源“无遗漏”。

arXiv 首批宽词查询跨组去重216项，含大量参考文献/词形噪声；按分类与 ti/abs 修正后的四组查询去重156项，两轮并集223个身份已按贡献或明确题名范围处置。初筛曾把新增模块/任务误作新机制，root 校准后同类33项具体关闭；现保留65条机制/反证线索，包含SAGE中心定义争议，而不是65个本窗候选或65项已证实贡献。完整题摘与逐项理由见[筛选停点](../_sources/daily-20250711/SCREENING.md)，宽列表没有扩成逐篇全文队列。KVFlow/Synergy 已读局部核心 v1 HTML；SAGE只因共性校准定点读 v1 方法与消融。本窗正式候选0、当窗事件审阅完成0；潜在贡献不因日期障碍被改写为已排除。

Books 纳入判断，但必要日期/版本证据未闭合，当前均暂缓，没有书稿改动，也没有宣称已有覆盖。作者可执行的有界发现、筛选和隔离记录已收束；root独立DAY复核通过，并修复两处可执行目录提取遗漏后，本日达到含外部保留项的安全终态。完成不表示外部保留项Coverage/Evidence通过或Books已整合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 news RSS共1247项，读取2025年7月条目；7/8→7/11序列越窗，7/11 EU Code条目原字段09:30 GMT在窗外。[原件](../_sources/daily-20250711/openai.raw) | 已检查 | RSS此段无本窗研究命中，不等于所有产品/论文修订完整覆盖。 |
| SRC-ANTHROPIC | Research可见十项之外，真实SSR publications payload含174条publishedOn序列化记录/172不同slug（非论文数量）；独立筛本窗，最近7/15→6/27邻接，无7/10/11目录条目。[本日原件](../_sources/daily-20250711/anthropic.raw)、[邻接原始objects](../_sources/daily-20250711/anthropic-pubs-slice.json)、[恢复依据](../_sources/daily-20250711/RECOVERIES.md) | 已检查 | 仅原目录此日期切片；illustration created/updated不是公开时间，不推及未列修订/全站活动。 |
| SRC-GOOGLE-AI | DeepMind blog页6跨2025年7月→4月，五条July链接核原文：Flash-Lite7/22，Backstory/IMO7/21，T5Gemma/MedGemma7/9；Google Research月页9项全部题名已查，Graph Foundation Models标7/10，pubs首页仅当前2026。[月页](../_sources/daily-20250711/google-month.raw)、[DeepMind页6](../_sources/daily-20250711/deepmind.raw) | 受阻 | GFM7/10及T5Gemma7/9仅原始日期、时区/时刻不足；MedGemma医学主线按AI for Science关闭。pubs历史新增/修订没有完整目录。 |
| SRC-META-AI | Research HTML无可用研究正文；一次历史日期限定官方域补检无可用原件。[响应](../_sources/daily-20250711/meta.raw) | 受阻 | 必要历史目录不可恢复；不能把被拦截响应当零事件。 |
| SRC-QWEN | 官方博客页1/2覆盖7/24、7/22→6/27、6/26；research-list API返回60条，July条目仅7/27、7/24、7/22。[API](../_sources/daily-20250711/qwen-research.raw)、[页2](../_sources/daily-20250711/qwen-page2.raw) | 已检查 | 此目录日期序列越窗且无本窗条目；不推及未列修订。 |
| SRC-DEEPSEEK | 从当前主页不足恢复为[官方updates](https://api-docs.deepseek.com/updates)原始HTML；独立定位h2：8/21后直接接5/28，目录此段没有7月更新。[同日保留原片段](../_sources/daily-20250711/deepseek-updates-slice.raw)、[原件出处/实际停点](../_sources/daily-20250711/RECOVERIES.md) | 已检查 | 仅官方updates此段无命中；不采用窗外benchmark，不声称全站/全部论文修订完整。 |
| SRC-MOONSHOT | 官方blog列表读至2024年，Kimi K2项目标2025-07-11，HTML dateTime为00:00Z（其他多条同样整日序列化）；按真实href取正文失败。[列表](../_sources/daily-20250711/moonshot.raw)、[正文请求](../_sources/daily-20250711/kimi-k2.request.json) | 受阻 | dateTime不能直接当实际发布时刻；缺K2初次公开时刻与正文，不按00:00Z伪造落窗。 |
| SRC-TENCENT-HUNYUAN | Research首查JS壳；浏览器核查30秒超时；一次官方publicList API page1/pageSize100得total9/list9，均2026英语记录。[API](../_sources/daily-20250711/hunyuan-api.raw) | 受阻 | 2025全部研究目录未恢复；有限恢复后停止，非目标窗零事件。 |
| SRC-ZAI | 官方Research首查15项，真实SSR ?page=2延伸到2025-12-07并显示没有更多。[页2](../_sources/daily-20250711/zai-page2.raw) | 受阻 | 该返回不能证明2025-07历史目录读完，缺具体日期段清单。 |
| SRC-BYTEDANCE-SEED | public_papers首查20/242；2025论文API p0空/94，p20仅SwiftSpec6/12，p40空但has_more=true/next60；停止。blog API p0/p20得15/18条，排序从7/15→7/14→6/28越窗，无此段条目。定点CoT官方页7/10与arXiv身份已核。[论文p40](../_sources/daily-20250711/seed-2025-p40.raw)、[blog p20](../_sources/daily-20250711/seed-blog-2025-p20.raw) | 受阻 | 稀疏论文分页不闭合；CoT原论文首次提交2024-11-18，current v2不证明重要修订，本次事件身份未建立，不能冒充当窗首次公开。 |
| SRC-BAIDU-ERNIE | 技术blog两页读取最终回链，第二页6/30→8/14→9月越窗，无7/10/11条目。[最终页](../_sources/daily-20250711/ernie-page2.raw) | 已检查 | 仅官方blog当前保留目录此段；不称全部论文修订无遗漏。 |
| SRC-XIAOMI-MIMO | 官方主页Paper八项读取，6/4→9/19越窗；Blog为当前条目无历史日期。[原件](../_sources/daily-20250711/mimo.raw) | 受阻 | Paper目录此段无命中；Blog目标窗历史目录未恢复。 |
| SRC-MINIMAX | 英文blog当前首12项；中文目录当前条目跳2025-10→1/15，无目标窗历史段；一次历史日期限定补检只返回无关用户知识库并关闭。[中文目录](../_sources/daily-20250711/minimax-cn.raw) | 受阻 | 无完整目标窗技术事件目录；不能将目录跳跃或搜索空命中作无事件。 |
| SRC-ARXIV | submission surrogate范围2025-07-09T18:00Z～07-10T18:00Z；四组窄查询按cs.CL/LG/AI、cs.DC/AR/PL/OS/PF、cs.AI/IR/MA/CL、cs.CV/RO/CL/LG与ti/abs主题边界，114/2/33/55项，start0/max200，各total<200，完整返回页后停止；跨组去重156。宽页216项仅查漏，两轮并集223。[实际查询](../_sources/daily-20250711/narrow.py)、[完整题摘](../_sources/daily-20250711/narrow-discovery.json) | 受阻 | 不是窗口公告查询；可能漏更早提交的延迟公告/重要修订。官方日列表/公告记录有限恢复失败，月列表不提供本窗批次；65项贡献线索不能分配本日。 |
| 补检：[官方域历史检索](https://www.anthropic.com/research) | Anthropic/Meta/DeepSeek/MiniMax四条机构日期限定查询；[实际查询与结果](../_sources/daily-20250711/SUPPLEMENT.md)，一次仅返回无关MiniMax用户生成知识库，按身份关闭后停止。 | 检索受限 | OR与索引覆盖不确定，不用于目录完备或零事件断言。 |

上述受阻项已隔离，不用于 Coverage 通过断言。各请求URL、HTTP状态/错误、检查时间及字节数随同保存；有限恢复原因见[来源日期边界](../_sources/daily-20250711/BOUNDARIES.md)。未扫描Weekly来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

尚无可确证落窗的正式候选，因此不填候选行或伪造0分。潜在贡献、SAGE方法争议和机构目录缺口放在第5节及保留的逐项原始筛选记录；此处的0不是已证实当窗没有重要进展。

## 4. 证据与知识整合

以下是日期未定前已形成的审阅停点，不作为当窗正面证据或审阅完成记录。日期恢复失败后停止其他全文与Books展开。

### [KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows](https://arxiv.org/html/2507.07400v1)

精确v1 HTML §3实现/策略、§4实验已读，原件[core-07400.raw](../_sources/daily-20250711/core-07400.raw)。AgentStepGraph把未来最早使用顺序映到共享prefix tree优先级；AND/OR步骤依赖不同，淘汰不是仅按最近访问；prefetch尝试在GPU/CPU缓存间提前传输。其成立前提是已知工作流图、Agent固定共享prefix与重复执行，不能推成任意临时Agent调用的未来预测。

局部实验范围：顺序10-Agent、batch1、warmup/10次均值，Llama3.1-8B/A10G24GB/PCIeGen1与Qwen2.5-32B/H10080GB/Gen5；长prefix且短输出时收益明显，输出变长时收益下降。PEER模拟仅约1.08×HiCache；64-workflow例中HiCache甚至慢于GPU-only，须同时看基线/缓存容量/传输竞争，不能引用最大倍数作普适加速。未据作者实验认领生产SLO、公平性或独立输出等价验证。

拟议唯一owner为`INFER-KV-CACHE`（[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)）：潜在知识差额是把“未来执行控制流”与“recency/容量/传输代价”分开，而非再写一套KV概念。仅为路由提案；当前未加载并对比该章具体论点，不认领已有覆盖或整合完成。日期门未过，Books暂缓。

### [The Synergy Dilemma of Long-CoT SFT and RL: Investigating Post-Training Techniques for Reasoning VLMs](https://arxiv.org/html/2507.07562v1)

精确v1 HTML方法、数据与评测核心已读，原件[core-07562.raw](../_sources/daily-20250711/core-07562.raw)。采用Qwen2.5-VL-7B并冻结vision encoder/connector；1K Gemini s1、1K R1 s1.1、34K Eureka数据（保留最短正确response）并非等量、等质量的干预。SFT训练轮次/最佳checkpoint选择不同，生成max24K、temp0.6、四次平均，不能将组合不叠加解释为对所有VLM/预算普遍成立的因果定律。

潜在贡献是“Long-CoT SFT后接RL未必同时获得两者收益”，需要按perception/难度层、response length、样本质量与训练预算解释，不能仅比较总榜均值。拟议唯一owner为`TRAIN-RLHF`（[Ch31](../../../../books/part-04-training-system/31-rlhf.md)），SFT入口引用`TRAIN-SFT`而不复制论点。差额提案是给后训练阶段顺序加上混杂控制/非叠加边界；尚未对照现有具体章节论点，日期未定，Books暂缓。

### [SAGE: A Visual Language Model for Anomaly Detection via Fact Enhancement and Entropy-aware Alignment](https://arxiv.org/html/2507.07939v1)

按root准入纠错定点读v1 §3.3 Eq3–7与Table3，原件[sage-v1.raw](../_sources/daily-20250711/sage-v1.raw)。实际提出的不是抽象“熵权重”：GPT-4o对type/location/logic评分，候选MLE score softmax后定义entropy，取相邻rank最小及首尾最大gap，并在BT log-policy margin减去ηΔH。

中心定义未闭合：Eq4对全候选求和得到同一distribution entropy，却称每答案H_i；按书面公式所有H_i相同，不能得到所述pair gap。Eq6/7未展示ref ratio/KL项，正文又称π_ref用于KL稳定；不擅自补公式。Table3领域消融不能消除该复现歧义，也不作通用DPO性能保证。root独立读同一原始核心确认争议；安全终态保留，完全不进入Books。若以后恢复，须先确认逐答案entropy定义及reference/KL实现，再判具体对齐增量。

### 非arXiv线索

[Google GFM原文](https://research.google/blog/graph-foundation-models-for-relational-data/)指出hard-coded schema/type embeddings及absolute feature projections不能迁移到新schema，而feature interaction有潜在泛化价值；但未披露可复现编码recipe/controlled experiment，3–40×average precision不作为本日或Books证据。仅7/10日期，公开时刻缺失。

[T5Gemma官方原文](https://developers.googleblog.com/en/t5gemma/)明确decoder-only权重初始化encoder-decoder后用UL2/PrefixLM adaptation，允许9B encoder/2B decoder的不对称质量/latency取舍。标7/9但时区未披露，不能自行把日期换算至本窗；仅保留边界归属问题，不推进paper/Books。MedGemma相同月日期线索因医学应用范围关闭，没有为排除项另追日期。

## 5. 缺口与下一步

可执行未完工作：无。独立DAY已通过；本作者不再扩扫主题、公告镜像或65篇全文。以下均为已隔离的外部终态保留项，不用于正面证据、候选、Books、性能/安全保证或无遗漏断言；缺少外部材料本身不再无限阻塞本日安全终态。各项身份、必要材料和定点重开条件如下。

- arXiv保留65项：身份、完整题摘、逐项贡献理由与唯一重开请求见[SCREENING](../_sources/daily-20250711/SCREENING.md)。代表包括KVFlow2507.07400v1、Synergy2507.07562v1、H-Net2507.07955、Krul2507.08045（须exact v1）、安全反证2507.07417、feature-leak threat2507.07259。需要官方历史公告批次/精确版本与公开时刻，或作者首次公开正文的可信时间记录。submitted不是public；一般周四20:00EDT调度不能代替单篇公告；OAI datestamp是last modification。KVFlow/Synergy的DataCite Updated语义未证明初公开，registered已在窗尾之后，不能造上界落窗。有限恢复到此停止，材料到达仅重开对应行，先日期再exact-version核心；明确贡献关闭的158项不另追日期。
- SAGE2507.07939v1：除上述公开时间外，必要中心定义争议见第4节；可接受作者明确逐答案entropy算法与reference/KL代码/勘误。它不因领域而被关闭，也不被修改后的猜测公式“挽救”；只重开§3.3与其相关消融。
- [Google GFM](https://research.google/blog/graph-foundation-models-for-relational-data/)与[T5Gemma](https://developers.googleblog.com/en/t5gemma/)：分别缺7/10和7/9原始时区/公开时刻。需要官方发布记录或可信首次公开全文时间上界；T5Gemma可能属于更早相邻窗，交由协调者定点确认归属，作者不读别日报或顺带重跑。日期明确后GFM仍需公开recipe/受控跨schema证据，不能只用内部AP倍数。
- [Kimi K2](https://platform.kimi.com/blog/posts/k2-report)：缺实际首次公开时刻与可用官方正文；列表整日dateTime序列化不是发布clock。可接受带可信时间的官方全文/首发仓库材料；只重开K2，不扩为整月Moonshot扫描。
- [Seed CoT information theory](https://seed.bytedance.com/en/public_papers/understanding-chain-of-thought-in-llms-through-information-theory)、[arXiv2411.11984](https://arxiv.org/abs/2411.11984)：首次提交2024-11-18，本次官方页7/10与current v2没有已识别的具体机制/兼容性/正确性/安全变化信号，版本变化本身不证明重要修订，事件身份未建立。若以后取得官方本窗事件/变更说明，只针对其实际变化读当前必要版本；不默认索取或展开完整v1/v2对比，不重复首论文评分。
- 未恢复的历史目录段：Meta、Hunyuan、ZAI、Seed论文、MiMo blog、MiniMax及Google pubs。各自实际停页/空响应/失败已在来源表列明。需要官方目标窗历史事件清单/当期目录或可核验首次正文记录；空页has_more、当前首页、搜索无结果不是完整性证据。只恢复该来源该时段，不全量重扫历史。Anthropic/DeepSeek的两处提取缺口已定点修复，不再列普通待办。

Books重开条件统一为：身份/当窗事件与exact版本可核验，核心命题证据足够后加载Books上下文、目标和相邻章节，对照现有具体论点差额并由root协调唯一owner写入。现有路由提案不等于实际差额已验收；本次未写共享Books、索引或LEARNING_STATE。

## 6. 复核

复核者：`/root`（独立于作者`/root/jul11_author`）。

结论：通过

root验收含明确隔离外部项的安全终态；不是全部Coverage/Evidence通过，也没有Books实际写入。

FIRST分批校准已由root独立读取原始题摘：KVFlow、Synergy、Krul、CXL与MODA代表关闭项。root指出OAI last-modification误作公开证据，已纠正并停止日期扩追；指出all:Transformer宽词/physics噪声，已改分类+ti/abs有界查询，宽列表仅查漏。后续独立题摘抽检SemRAG/TableReasoner/DisenQ/animal-motion/graph-projector共同误收，作者扩查同类理由关闭33项；SAGE中心定义争议由双方独立读v1 §3.3确认，不采用方法/性能或Books。

独立题摘范围为26个不同身份：FIRST的07400/07562/07201/08045/07223；共性准入校准的21110/08046/07262/07394/07335/07939；DAY的07417/07259/07947/07974/07955/07981/08068/07824与分层关闭样本07247/08878/07445/07274/07317/07799/07901（均为2507前缀；SAGE完整题摘在v1 core首部）。SAGE另独立读取v1 §3.3 Eq3–7，确认中心定义争议。安全威胁/评价负面信号保留，不作普适保证；7项DAY关闭当前理由可成立，成熟机制词不自动成为新贡献。

65保留/争议中12项做过上述独立题摘校准，53项没有逐项独立复核；158关闭中14项为独立题摘样本，144项未逐一独立核验，不能把26样本或格式校验称为65/223全量验证。当前实际拟采用候选为空；所有未定日期线索和SAGE中心争议均隔离，不进入正面采用/Books。root指出的DeepSeek官方updates、Anthropic SSR历史payload两处可执行来源提取遗漏已由作者独立筛本窗并保留原片段；没有读取其他日报判断。root允许修复后结束本日，不自动接别日。

作者机器检查：`python3 scripts/validate_research.py --report papers/2025/07/11/README.md`通过（1份V3）；`git diff --check`通过；日报本地相对链接全部存在。筛选表实际223行，65保留/争议、158关闭。当前metadata撤回/纠错轻核只命中MagiC的self-correction评测用词，不是withdrawal/erratum，范围见[边界记录](../_sources/daily-20250711/BOUNDARIES.md)。本次写入范围仅本日README及同日_sources；没有stage、commit、push或共享Books/索引/学习状态修改。这些检查不构成DAY语义通过。
