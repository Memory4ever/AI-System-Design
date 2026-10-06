# 2025-11-25 首批准入校准请求

作者：Aristotle。窗口：BJT [2025-11-24 09:00, 2025-11-25 09:00)。检查启动：2026-10-04 14:41 BJT。仅本日原源，不读旧 Weekly 或别日候选。此文件不是独立复核结论。

## 请求 root 校准的集合

1. **确定落窗 / 拟入选：[Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)**。已读官方完整核心说明（raw-event-0.json），原页下载在 native-opus.html；`article:published_time`、JSON-LD `datePublished` 和正文 `time` 一致为 `2025-11-24T19:00:00.000Z`，即 BJT 11/25 03:00。拟准入命题：固定输出 token 预算不能表达同一模型在任务质量与计算投入之间的全部取舍 → 发布引入 effort 控制并报告同一 SWE-bench Verified 工作负载上的质量/token 曲线，同时记录 harness 基础设施修复如何改变被比较模型的分数 → 需要区分 effort、模型能力和 evaluator 环境，而非把单一排行榜当可比能力证明。拟评分 2+2+2=6；系统卡 ARC-AGI 数据划分纠错触发受影响证据深入审阅，不因 6 分只读摘要。不采用“世界最强”或生产安全保证。Books owner 初路由 PLATFORM-EVALUATION-SYSTEM，尚未读 owner，不宣称知识缺口。

2. **贡献拟通过、日期未定：[Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch, 2511.17826v1](https://arxiv.org/abs/2511.17826v1)**。完整题摘见 raw-event-0.json / raw-search-0.json。拟准入链：TP 规模改变浮点归约顺序，而单纯 batch-invariant kernel 不能消除 training/rollout 的跨 TP 数值差额 → TBIK 用统一二叉归约树对齐 GPU 内外次序 → 应核验跨并行策略的同一 log-probability 是否可做到 bitwise 一致及其代价。该机制增量不能因 Books 已谈确定性而排除，也不借成熟浮点原则加分。日期原字段 `[v1] Fri, 21 Nov 2025 22:40:00 UTC` 仅是 submitted。DataCite 实查 v1 Updated=`2025-11-25T01:12:35Z`，created/registered=`2025-11-25T03:57:35.000Z`；均在截止之后，不能从这个上界推出首公开也在窗外。arXiv 当前官方公告规则（raw-date-and-trigger.json）为美国东部 20:00，冬令时正好 BJT 09:00 截止；不能按规则反推这篇无延期/无早公开。当前不计确定候选，下一步仅核官方公告身份或作者早公开，不读全文队列。owner 初路由 TRAIN-DISTRIBUTED-TRAINING / INFER-TENSORRT-LLM，待确定唯一具体命题 owner。

3. **贡献拟通过、日期未定：[Multimodal Large Language Models with Adaptive Preference Optimization for Sequential Recommendation, 2511.18740v1](https://arxiv.org/abs/2511.18740v1)**。完整题摘已回原 v1（raw-screening-calibration.json）。不是因为“用了 DPO”准入：摘要明确提出 fixed reference 的跨模态对齐偏差，以及按样本 hardness 和 policy responsiveness 调权、扰动输出分布的替代目标。需定点读 objective，判断实际增量是推荐任务特设还是可复用的 preference optimization 条件；不因是推荐一律范围外，也不以摘要无消融关闭。原 submitted=`2025-11-24T04:10:46Z`；未确认 public。本项暂不评分、不计确定候选。

4. **贡献拟通过、事件日期需校准：[Introducing advanced tool use on the Claude Developer Platform](https://www.anthropic.com/engineering/advanced-tool-use)**。完整核心说明见 raw-date-and-trigger.json。动态 defer_loading 与工具引用展开、代码调用中间结果不进模型上下文、调用样例补 schema 三项是具体执行接口变化，不是把常规检索/脚本原则换名。原页面 native-tools.html 中 `datePublished` 与 `article:published_time` 均为 `2025-11-24T00:00:00.000Z`（BJT 08:00，窗前）；正文仅日精度 Nov 24。Opus 官方 19:00Z 发布同时宣告相关平台能力。不能静默将文章归本日，也不能把 midnight 元数据当经验证的实际首次公开时刻。请 root 校准按“明确 API 发布事件”是否可单列，或保留先公开区间跨起点的日期缺口。当前不计确定候选，不预授 Books。

## 代表性负侧 / 定点重开

- **[A Multi-Agent LLM Framework for Multi-Domain Low-Resource In-Context NER via Knowledge Retrieval, Disambiguation and Reflective Analysis, 2511.19083v1](https://arxiv.org/abs/2511.19083v1)**：完整题摘见 raw-screening-calibration.json。当前关闭依据是静态实体示例+Wikipedia 检索+消歧+反思的 NER 组合，摘要的跨十数据集性能未提出新的执行/状态/控制机制或能修正通用 Agent 判断的失败条件；不是因为局部实验或无开源。若 root 认为“减少动态示例依赖”足以形成可复用 ICL 边界，只重开这个命题所需方法段。submitted 日期未作 public，不为不影响关闭的日期继续追查。当前官方页无撤回/纠错标记。
- **[Beyond Protein Language Models: An Agentic LLM Framework for Mechanistic Enzyme Design, 2511.19423v1](https://arxiv.org/abs/2511.19423v1)**：完整题摘已读，Genie-CAT 将文献、PDB、静电与 redox prediction 组合用于蛋白设计。ROADMAP 明确暂缓 AI for Science，不能通过 RAG/Tool owner 重引入；关闭并停止全文/日期恢复。当前官方页无撤回/纠错标记。
- **[Introducing shopping research in ChatGPT](https://openai.com/index/chatgpt-shopping-research/)**：已读原文 How it works、Limitations 核心（raw-screening-calibration.json）。公开的是 GPT-5 mini 购物 RL、澄清偏好和网络调查的产品流程，没有披露奖励/训练/检索机制的新可验证增量；不能以“Agent 应问问题/核来源”成熟原则制造长期缺口。关闭，不评分、不要求日期恢复。仅产品误差提醒，不是研究结论撤回。
- **[Measuring political bias in Claude](https://www.anthropic.com/news/political-even-handedness)**：发现明确 11/24 changelog 将 Sonnet opposing-viewpoint 28% 改为35%（raw-search-0.json）。**不关闭，不漏审纠错**；本次只核更正所影响的评价数字和日期边界，不重读 11/13 初公开全文。当前是普通必要日期/纠错待办，不称 Evidence 完成。

## 实际来源与停止范围

- 14 每日来源均已启动官方入口核查，但尚未完成覆盖；native0/1 与 search0/1/2/3 记录真实 open 和 search 命中。搜索第一页均为有限线索，不证明零命中或无遗漏。
- arXiv 第一个 CLI date 查询返回畸形规范化 query 和 26,505 个跨时段总数，**执行失效，不作覆盖，不筛其 100 个宽返回**。第二个修正 date query max_results=5 得273，仍是过宽发现探针，五条不建全文队列。之后应改为 title/abstract 窄主题并保存分页停点。
- 官方月表 cs.LG show=2000 只是标题线索，返回3,648项；**不逐篇题摘/全文排队**。本日的有效公告切片仍待恢复，不把整月当当日。
- Hunyuan 官方 Research 静态返回0行；浏览器首次 createBrowserTab 30秒超时。按用户线索 POST publicList page1/pageSize20/renderType0 实际返回 totalNum=9，九条均2026，且是blog，不足覆盖历史Research论文。下一步只恢复 Research 展示对应入口，不遍历2026博客正文。
- Seed 已实查 GET get_article_list_v2，article_type=2/publish_year=2025/count20/page_token0/order_desc=true，header x-tt-locale:US。返回博客目录而不是论文（文件名 seed-papers-page0.json 是首次误命名，保留原raw，不重命名冒充论文）；has_more=true，next_page_token有原值，尚需读元字段并处理 pinned边界。下一步article_type=1本日附近目录。

## 窄主题追加首批校准（2026-10-04T15:01:29+08:00）

实际执行四组查询见 fetch_scoped_arxiv.py 与 arxiv-{model,systems,agents,multimodal}-query.json / page0.xml。均为 submittedDate:[202511201900 TO 202511211900] 加明确主题表达，start=0/max_results=100，返回30/7/38/34，四组各自返回完毕，109条跨组去重为88个论文身份。这只是本日可能公告的发现切片，不是public日期证明或全体题摘/全文队列；API返回latest摘要，仅下列五项回到精确v1读完整题摘，原始页见raw-scoped-calibration.json，Rynn补全页见raw-rynn-v1.json。

- **[Masked-and-Reordered Self-Supervision for Reinforcement Learning from Verifiable Rewards, 2511.17473v1](https://arxiv.org/abs/2511.17473v1)**：完整题摘明确 final-answer 验证不能有效利用 theorem proving 的中间推理，token SFT又可能记忆训练链；MR-RLVR以 masked-then-fill/step-reordering构造过程级自监督奖励，先过程训练再outcome RLVR。拟准入是替代奖励信号与两阶段训练的局部增量，不因小模型或摘要缺消融关闭。作者两小模型固定sampling/decoding预算结果不是已核训练总预算因果证据；后续只核奖励实现、两阶段预算和对照。submitted=`2025-11-21T18:23:04Z`，public未确认，不评分、不计确定候选。
- **[MicroMoE: Fine-Grained Load Balancing for Mixture-of-Experts with Token Scheduling, 2511.16947v1](https://arxiv.org/abs/2511.16947v1)**：完整v1题摘提出按micro-batch跨GPU token调度的MicroEP，目标是在不改变模型质量或引入已有方案额外开销的前提下细粒度平衡；拟核验这类执行重分配是否提供新的负载/通信取舍。47.6%最高端到端训练吞吐是作者未绑定完整配置的摘要结果，不照录普遍收益。原v1题名严格保留，不采用2026v2“Linear Programming”改题作为2025机制。submitted=`2025-11-21T04:50:13Z`，public未确认；当前只需准入/日期，不强造Books缺口。
- **[UI-CUBE: Enterprise-Grade Computer Use Agent Benchmarking Beyond Task Accuracy to Operational Reliability, 2511.17131v1](https://arxiv.org/abs/2511.17131v1)**：完整题摘给出136 simple/50 copy-paste/40enterprise任务、界面变化/多分辨率/application-state验收及human对照。拟准入是局部负证据：简单UI完成率不能代表复杂workflow条件下的完成率，不是因为新增benchmark即可收。作者将性能断崖归因于memory/planning/state的“根本架构限制”，这个因果解释尚无干预证据，不直接采用；需核workflow/human任务条件、agent配置和失效分析。submitted=`2025-11-21T10:47:22Z`，public未确认。
- **[MURMUR: Using cross-user chatter to break collaborative language agents in groups, 2511.17671v1](https://arxiv.org/abs/2511.17671v1)**：完整题摘报告普通群聊消息污染persistent sharedstate，后续诱发代理替良性用户执行攻击者动作，跨任务持续；构造并发多用户任务框架并提task-basedclustering第一步防御。拟准入是跨用户状态污染的具体新攻击路径，不借通用prompt injection原则加分。安全信号必须深入核受影响用户/权限/状态传播及真实系统条件；不提前声称防御生产可用。submitted=`2025-11-21T04:56:37Z`，public未确认；没有按低分或局部证据关闭。
- **[RynnVLA-002: A Unified Vision-Language-Action and World Model, 2511.17502v1](https://arxiv.org/abs/2511.17502v1)**：完整v1题摘给出 action+visual→futureimages 与 observations→actions 联合训练、双向增强，以及simulation/realrobot对照。拟核验action预测与未来视觉预测是否在可比训练条件下互助，不能只凭“统一模型”准入，也不能因worldmodel潜在物理领域一律按AIforScience排除。97.4% LIBERO/no pretraining与realrobot“+50%”均待精确基线和相对/绝对口径，不外推学会物理。submitted v1=`2025-11-21T18:59:32Z`，v2=`2025-11-24T04:49:33Z`；这两字段不是public，v2存在不自动证明本日重要修订。

这五个官方v1当前题摘页未见撤回/纠错声明；后续具体必要原页若出现安全/更正信号只重开受影响命题。首公开仍普通有限恢复待办，不将跨截止上界转换为“已证窗外”。

接口停点更新：Seed article_type=1已实查，18返回/total94/has_more=true/next_page_token="20"，type2亦18返回/total45/has_more=true/next20。论文前两条December pinned之后首个non-pinned Oct22BJT，博客前五条较新pinned之后首个non-pinned Oct23BJT；本页无目标日，不称年度/仓库无遗漏。Hunyuan另两次浏览器尝试分别为subagent visibility不支持（不是网页失败）与45秒超时；不再循环空路径。此前“下一步type1”与“下一步四组窄检索”已执行，上文原过程保留不充当最新待办。

## 普通待办 / 外部保留

校准包补充负侧：[How Conservation X Labs Is Using Segment Anything Model 3 for Endangered Wildlife Monitoring](https://ai.meta.com/blog/segment-anything-conservation-x-wildlife-monitoring/)，实际读取原页L48～88核心（raw-boundary-core.json）。本文是既有SAM2/3在动物监测及SA-FARI科学数据集上的应用与资源说明，未披露新增模型/系统机制或主线设计反证；AIforScience按ROADMAP暂缓，不因出现foundationmodel重引入。贡献关闭、未评分；Nov24原日字段/时区未核，关闭后不为不影响处置的日期新增请求。当前页核心未见纠错/撤回信号。该项加入代表性范围外样本，不重开SAM3窗外首发。

普通待办：首批准入独立校准；其余官方目录有限补查；arXiv窄主题及本日公告补检；Opus精确system card必要机制/对照/纠错；实际Books context/owner对照；最终六部分和非作者复核。上述未完成工作不能标外部受阻。

日期外部保留目前只是 provisional：TBIK和HaNoRec尚未穷尽有限原源恢复，不宣称终态；advanced-tools原文章与API事件日期边界需裁决。完整raw未失效；不反复空路径，不用它们作正面当窗证据。

## Root 独立准入校准回传（2026-10-04，本日继续）

复核者：root，非报告作者。以下按直接回传记录，不是作者自授证据/Books或日级完成。

实际原源范围：Opus L161～236（effort/token、harness、τ2合法替代路径误计失败），advanced-tool原文全文核心及接口，八项exactv1完整题摘：TBIK、HaNoRec、MR-RLVR、MicroMoE、UI-CUBE、MURMUR、RynnVLA、KDR-NER。

校准结论：Opus具体effort质量/token曲线与harness修复可审，2+2+2=6可继续必要systemcard和纠错；七篇潜在机制方向继续有限date/必要review，不从跨截止元数据上界直接关闭。UI-CUBE只采用复杂workflow相对simple局部负证据，不采用“根本架构限制”因果归因。KDR-NER现有组合/领域指标无新增通用条件的关闭可继续。HaNoRec必须定点目标式核是否有实际新优化/更强主张，不能借DPO名称或目标说明直接收。

advanced-tool必须分开00Z文章与19Z明确平台release：可用Opus19Z原release宣布new effort/contextcompaction/advancedtool的正式可用事实建立本窗API发布事件，与原文章接口证据组成同一家族；不写文章首次公开为19Z，不重复未变事件，没有同窗新增事实则保留日期缺口。政治bias纠错继续核必要对照与日期，不重读初公开所有正文。

本校准不授Books通过、不授日级完成。Books算法名字未见不代表长期缺口；只读拟采用命题所需机制、对照、限制和反证，不扩所有附件或benchmark。作者当前只处理Nov25，25～30总任务仍在进行。
