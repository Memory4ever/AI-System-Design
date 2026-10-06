# 2026-05-09 增量来源补查

## A1 — 范围、冻结与独立日级上下文

- 作者：`supp_may09_author`；本轮检查始于2026-10-18 02:56 BJT。只补2026-05-08完整北京时间自然日，不启动Live/Weekly/2025或05-10。
- 完整原件：[baseline-before-supplement-20261018.md](baseline-before-supplement-20261018.md)。原1候选ERNIE 5.1、原日期/评分/小时窗及连续原§4保留；本轮不改有效原证、不搬移日期。
- 已完整重读当前AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES使用说明/每日组/主题、CODEX_RESEARCH_PROMPT、ROADMAP、本日README与LS最新相关路由。LS只作路由，不继承其他日期研究池。
- ownership仅本日日报、本唯一SUP与baseline。无Books/LS/索引/其他日期写权；既有及并发index/worktree修改保护，不stage/commit/push。技能使用：using-agent-skills用于边界与可验证出口；git-workflow-and-versioning只用于保护脏工作区，不执行其默认提交建议。
- 本次窗口含Thursday20:00ET公告（BJT05-08 08:00）；原05-08小时窗可能已处理同事件。跨日只具名核身份/重复，不读取其他日长内容或旧Core/regex脚本，不继承旧Weekly。

## A2 — 首批准入校准请求（尚未通过，不预授候选）

实际搜索（2026-10-18 BJT）：`site:openai.com "May 8, 2026" research`、`site:anthropic.com "May 8, 2026" research`、`site:deepmind.google "May 8, 2026"`；Google Research/Meta/Qwen随后具名定点。搜索只负责发现，不作正文证据。

### P1 Teaching Claude Why（拟准入）

- primary：[Anthropic研究目录](https://www.anthropic.com/research)、[完整研究文](https://alignment.anthropic.com/2026/teaching-claude-why/)、[官方简版](https://www.anthropic.com/research/teaching-claude-why)。官方日期May8,2026；日期口径保留原字段，不补造时刻。当前已读完整Introduction与Methods概要、why-misalignment和response-quality主段；必要后续图/结果/限制尚普通未读，不叫外部受阻。
- 原约束/判断→实际增量→设计选择：对特定honeypot做拒绝行为模仿虽能压低同分布misalignment，却未改善held-out自动审计；与之相比，伦理困境advice、constitutional synthetic document finetuning及无关工具定义环境增强报告跨分布变化。这允许定点核验“训练匹配评测足以代表alignment改进”的失败边界，以及SFT数据语义/情境多样性如何改变后训练选择，不是新benchmark数量或把流程翻译成控制状态。
- 拟命题范围：仅作者内部模型与评测/干预对照，不证明普遍安全；准入后核必要训练顺序、主对照、样本预算、held-out评测与直接限制。Owner预路由TRAIN-SFT/PLATFORM-EVALUATION-SYSTEM，唯一owner须具体对读后决定。
- 尚需具名跨日核同事件；未评分，未写Books。

### C1 Running Codex safely at OpenAI（代表性拟排除）

- primary：[官方正文](https://openai.com/index/running-codex-safely/)，可见May8,2026；已读核心说明和全部6个控制/telemetry段。
- 内容为sandbox技术边界、approval授权、network allow/deny、keyring/enterprise identity、rules/admin config与agent-native OTel日志的实际部署组合；auto-review送planned action/recent context给审阅子代理，但未给新判定算法、失败率、对照或新的正确性边界。
- 当前拟不准入：单一机构运行案例与已有控制组合，不因映射Ch72/Ch84或把日志称evidence plane即有长期增量。保留排除待独核，若独核指出具体新机制再局部重开。不评分。

### C2 Axios developer-tool compromise（窗外关闭）

- [官方事件说明](https://openai.com/index/axios-developer-tool-compromise/)日期Apr10,2026；搜索命中May8只是证书轮换/旧版支持截止，不是本日新研究发布。当前未见新的本日实质修订证据，不把安全标签或deadline当新增事件。无本窗候选/评分/Books。

## A3 — 来源执行停点

- SRC-ARXIV：误开`pastweek`只返回Oct近期列表，立即停止，不将其作May覆盖。`https://arxiv.org/list/cs.CL/2605?show=2000`官方返回404；仍在恢复本窗有限入口/具名duplicate，尚普通，不将访问失败写零命中或全源受阻。
- 其余每日机构入口继续按表顺序有限检查；首批准入交root校准后再进入必要原证。

## A4 — 有限系统主题完整题摘准入（18篇，不是全分类队列）

在官方`/list/<category>/2026-05?skip=0&show=2000`的cs.DC/AR/PL/OS/PF/IR/MA中浏览05200～06700附近相关题名，范围只作同原May08公告簇相邻查漏，不按编号判日期。原May08表只提取188个唯一URL身份作具名去重（05216等），不继承其贡献或评分。另按GPU/World Model主题搜索发现ROSE/HaM-World/EA-WM；后两者原日同事件不新增。18篇下列精确`https://arxiv.org/abs/<id>v1`的完整题名/摘要及v1史已实际读；下表不是已完成证据审阅，拟P尚待root独校准。

| ID / 标题 | 完整题摘后具体增量与拟处理 |
| --- | --- |
| [2605.06055 Relay Buffer Independent Communication over Pooled HBM](https://arxiv.org/abs/2605.06055v1) | P：MoE dispatch/combine的relay/reorder buffer开销→pooled globally addressable HBM上直接expert-window placement/read，prefill与decode两调度→需核中间缓冲是否仍必要及平台边界。 |
| [2605.06057 FalconGEMM](https://arxiv.org/abs/2605.06057v1) | P：LCMA理论乘法减少不等于运行快→group-parallel reuse及shape/hardware分析模型选择→核可复用的算术/访存/选择边界而非单一加速数。 |
| [2605.06113 BalanceRoute](https://arxiv.org/abs/2605.06113v1) | P：sticky KV与增长请求使DP decode barrier负载不平衡→非对称piecewise F-score及短horizon termination分类→核在线路由安全余量与预测收益条件。 |
| [2605.06374 ResiHP](https://arxiv.org/abs/2605.06374v1) | P：序列长变化可假扮fail-slow→workload-aware时间预测剥离变化并联调hybrid groups/partition/schedule→核误报与适配成本，不能仅换故障框架名。 |
| [2605.06534 ROSE](https://arxiv.org/abs/2605.06534v1) | P：rollout长尾与额外GPU分配开销→借serving闲置GPU、SLO co-executor、跨池shard/sparse权重同步→核异构模型共置与SLO保护边界。 |
| [2605.05639 TokenStack](https://arxiv.org/abs/2605.05639v1) | P：uniform HBM-PIM让冷KV/weights付PIM容量代价→dense/PIM分层与logic-die DMA/migration/placement→核容量/带宽/热KV迁移tradeoff，拟采用受simulation边界限定。 |
| [2605.05248 Governed Metaprogramming](https://arxiv.org/abs/2605.05248v1) | 潜力：将form纯计算与materialization授权效应形式分离，含no-bypass等证明。日期必要保留：v1May5，最早公告May6与registeredMay8跨日；不拿May8 Updated字段当直接公告。不先列确定本窗候选。 |
| [2605.06184 Teaching LLMs Program Semantics via Symbolic Execution Traces](https://arxiv.org/abs/2605.06184v1) | P：verification总体accuracy掩盖violation漏检→3k bug traces与CoT有superadditive交互，并有28配置语义/代码量控制→核正负类评价与训练语义条件，不是C代码应用本身。 |
| [2605.05253 EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253v1) | C：500k合成企业文档/9source types/500问题及noise构造；完整摘要只陈述新资源与coverage，未展示新评价盲点/混杂因子的证据或改变选择的机制；不因规模收。日期未核实且不影响排除，不建请求。 |
| [2605.06235 OBLIQ-Bench](https://arxiv.org/abs/2605.06235v1) | P：常规retrieval饱和→latent/implicit relevance下LLM可verify却retriever不surface的非对称证据→核检索与验证解耦盲点及协议，不因benchmark名入选。 |
| [2605.06647 SIRA](https://arxiv.org/abs/2605.06647v1) | P：多轮exploration成本→offline文档词汇补充+query evidence词预测+DF过滤，一次weightedBM25→核何种语料可把搜索转为discriminative query，含offline成本/比较公平性。 |
| [2605.05703 Active Learning for Communication Structure Optimization](https://arxiv.org/abs/2605.05703v1) | P：随机task优化图在小预算不稳定→ensemble Kalman近似task信息增益配代表pool/Thompson batch→核优化预算与图/任务外推条件。 |
| [2605.06623 MASPO](https://arxiv.org/abs/2605.06623v1) | P：local prompt validity不等于successor成功→joint downstream evaluation+evolutionary beam无GT联合优化→核评价器误差与局部/全局目标对照，不将组合本身当贡献。 |
| [2605.06671 GraphDC](https://arxiv.org/abs/2605.06671v1) | C：graph decomposition→specialists→master integration的divide/conquer组合；完整摘要只说多规模指标更好，未给新增分解/跨cut correctness条件或失败边界。不是因数学任务或局部实验排除。日期不影响排除，不追。 |
| [2605.06696 Hidden Coalitions](https://arxiv.org/abs/2605.06696v1) | 潜力：hidden-state MI graph/spectral boundary区分真实informational coupling与行为相似，并负对照拒绝伪阳性。日期必要保留：v1May4，registeredMay11跨日，不能以五月ID或当前提交日定本窗。 |
| [2605.05538 AgenticRAG](https://arxiv.org/abs/2605.05538v1) | 待定：search/find/open/summarize组合与single-shot→tool-use消融；需定点读核心贡献/直接消融决定是否有可复用的成立条件，不能单因既有模块或摘要未全控变量排除。 |
| [2605.06230 Safactory](https://arxiv.org/abs/2605.06230v1) | C：Parallel Simulation/Trustworthy Data/Autonomous Evolution统一流水线；完整摘要未给新的trajectory ownership、算法、失效条件或可改变选择的反证；不把三平台组合译状态/控制即准入。 |
| [2605.06082 PoTAcc](https://arxiv.org/abs/2605.06082v1) | 待定：PoT量化不同策略与shift-PE/TFLite端到端平台；须定点读Transformer模型范围和策略对照看是否支撑模型执行主线条件，不因generic DNN或小模型一刀切。 |

### 本批日期合证（原件在线可复查；不使用Created）

每项均读同DOI `https://api.datacite.org/dois/10.48550/arxiv.<id>`：`state=findable`、`relationships.client.data.id=arxiv.content`。下列v1均唯一、提交在May7 18:00Z cutoff前；按官方公告日程最早May8 00:00Z（BJT08:00），registered最晚界也在May8 BJT。因此整个区间同落May8；这只限定arXiv公告日，不证明全球首次公开或历史逐字内容。当前官方v1史用于唯一性，后续版本不偷换入当前命题；必要后续纠错信号还须定点检查。

| ID | 唯一v1 Submitted UTC | registered UTC |
| --- | --- | --- |
| 06055 | 2026-05-07T11:41:18Z | 2026-05-08T13:12:38Z |
| 06057 | 2026-05-07T11:41:54Z | 2026-05-08T13:12:43Z |
| 06113 | 2026-05-07T12:25:38Z | 2026-05-08T13:15:01Z |
| 06374 | 2026-05-07T14:52:54Z | 2026-05-08T13:25:37Z |
| 06534 | 2026-05-07T16:33:40Z | 2026-05-08T13:32:09Z |
| 05639 | 2026-05-07T03:47:18Z | 2026-05-08T02:15:03Z |
| 06184 | 2026-05-07T13:01:06Z | 2026-05-08T13:17:53Z |
| 06235 | 2026-05-07T13:22:49Z | 2026-05-08T13:19:58Z |
| 06647 | 2026-05-07T17:54:29Z | 2026-05-08T13:45:15Z |
| 05703 | 2026-05-07T05:48:43Z | 2026-05-08T02:16:33Z |
| 06623 | 2026-05-07T17:35:26Z | 2026-05-08T13:44:16Z |
| 05538 | 2026-05-07T00:39:22Z | 2026-05-08T02:12:40Z |
| 06230 | 2026-05-07T13:21:15Z | 2026-05-08T13:19:46Z |
| 06082 | 2026-05-07T12:03:08Z | 2026-05-08T13:13:44Z |

05248：v1May5T02:56:43Z、registeredMay8T02:05:45Z；06696：v1May4T16:59:08Z、registeredMay11T02:02:23Z。二者目前合证跨日，必要日期仍普通恢复，不伪装受阻。06184 metadata的Updated=v1 June16信号不改变已登记最晚界，但提示当前metadata处理，不能拿Updated替代公告；对拟采用历史语义仍精确v1读取。

公告规则已直接重读[官方availability](https://info.arxiv.org/help/availability.html)的ID assignment与Announcement Schedule：最终ID/DOI公告时分配，不可提前给；Wednesday14:00～Thursday14:00 ET最早Thursday20:00 ET。本批May7为EDT UTC-4，故最早May8T00:00Z/BJT08:00，不是将May7Submitted直接作为May8。适用于目标时期的[2025-01-06官方版本](https://github.com/arXiv/arxiv-docs/blob/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md)路径由现合同提供，网页版此次cache miss不另造已读；当前规则正文已实读，目标时期原件仍可依root既有有效核验层复用。

## A5 — P1 必要深入 Source prepared（待非作者核验，不预授Books）

root首批校准实际通过P1；C1/C2按A2具体理由关闭；A4抽核06055/06113/06235及代表C05253/06671/06230方向成立，尚不等全部候选Source通过。

P1评分拟`2+2+3=7`：改变安全训练分布与评测迁移的具体判断，而非借机构权威或所有既有安全原理加分。实际读完整主文Methods、Results各核心段与Limitations，足以限定拟采用命题，未遍历无关附件。

- 身份：[Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/)，官方May8；作者内部研究博客，无独立复现。Methods的实验主要在Sonnet4/Haiku4.5及其base模型；这些模型pretraining早于原agentic-misalignment博客，作者据此排除那份公开评测场景的预训练知晓，不因此证明所有训练无污染。
- 训练协议：SDF指synthetic pretraining-style documents，随后generic chat SFT；不把document与chat训练格式混为一谈，也不写成在产品已完成SFT之后随意加文档即等效。文档转换chat对照在constitution事实回忆/hallucination较弱，open-ended差异较小；“更新prior/persona”为作者解释，尚无完整机理证明。
- 关键反证：同类honeypot约10k/30M tokens只按正确拒绝行为过滤使misalignment约22%→15%；sampling时加指令并在训练前移除、提高用户可见理由质量可到约3%。重复将一部分数据固定8k transcripts仍见类似方向，较多29M→85M数据约1%；不能用这个局部控制宣称完整等算力或解释唯一因果。
- OOD分支：difficult-advice约3M tokens，让用户面临伦理困境而模型给建议，与模型自主行动honeypot分布不同；原文报告该分支在旧automated alignment assessment也更强。流程反侧去掉prompt rewrite约2%且在误差内，去掉final response rewrite约19%；说明这组数据中response质量是重要可干预因素，不授“所有显式解释都更安全”。所有该节数据extended thinking关闭，reasoning明确是user-facing explanation，不是内部CoT。
- SDF持久性：四种haiku-class初始化（baseline generic SFT；SDF+同generic SFT；SDF+harmless SFT；SDF+values SFT）在harmlessness RL子集跑；初始较好者一般保留优势、部分指标饱和；不等于任意RL rewards下安全不回退。Tool definitions/system prompt增强时user prompt固定，工具对该任务无必要，honeypot学习较快；这是环境格式多样性的受限对照，不证明tool实际执行安全。
- 必要限制：作者明确不解决鼓励reward hacking的环境；honeypot/内部Petri有限，0%不是开放环境保证；主实验scale/architecture有限且lab-specific，SDF理解与效果之间仍有机理缺口。较低token mix不完全是大mix随机子样本，constitution recall与behavior相关不证明内化因果；自报“我”与“Claude”belief仍有gap。硬件、precision、完整预算/并发/SLO及seed数量/跨lab复现Not Disclosed，不适用serving性能结论。
- 拟长期链：正确拒绝demonstration可以先满足已知交互；当能力训练扩向工具与自主情境，单一同分布分数不足→把高质量响应、OOD困境advice、文档知识与环境格式多样性当可比对照，并在独立heldout行为中验收；情境/奖励或评测coverage变化时回退旧checkpoint、普通verified SFT与独立风险评估。唯一owner拟TRAIN-SFT Ch29，PLATFORM-EVALUATION-SYSTEM只消费评测边界，具体已有正文差异仍需对读。

### P1 owner具体对读

Ch29现§为什么少量高质量数据也可能有效列出base能力/输出协议/目标分布/困难失败覆盖/规模变量，并说明同质examples会style collapse/过拒/phrasing过拟合；§数据质量列正确性、refusal边界、synthetic judge selection bias，§Evaluation分开能力行为/训练模板与部署分布。Ch66§评估结论相对于分布定义无污染、目标population、scorer三假设。但当前局部没有“相同行为拒绝仍弱、response rewrite与OOD伦理advice强”的干预对照，也没有SDF-pretrainingstyle→genericSFT→RL初始化/环境格式增强的具体分支。因此拟唯一Ch29在同质example段后补受限对照与迁移验收，不重复Ch66评测定理或散写多个owner。无Books写入，等待root Source/PRE决定。

## A6 — 主要主题有界补检：33完整题摘（发现封口，不全目录排队）

官方cs.CL/LG/AI/CV/RO五月列表首2000条的05200～06667邻接题名只作查漏；先按原May08的188唯一ID去重，再以LLM/Transformer学习、推理、表示/生成、World/WAM/VLA与可改变评测的具体机制收窄。医学/天气/材料应用、传统机器人控制/定位、通用推荐/领域分类等明确范围外题名不展开；没有把宽目录每个身份设为待关闭队列。对下列33个相关题名实际逐篇读精确v1完整摘要与v1史，原始在线入口统一`https://arxiv.org/abs/2605.<id>v1`。本批拟P是具体待核验增量，不代表Source完成，不因已有覆盖或审阅费时缩池。A4和A6之外不追加无限发现。

| ID / 简称 | 完整题摘准入理由/处理 |
| --- | --- |
| 05225 MACS | 潜力：token-count EP balancing忽略视觉token信息异质/模态配比，entropy-weighted load+dynamic modality capacity替代。唯一v1Apr19，registeredMay8不能合证同日；定点恢复直接公开资格后再决定本窗。 |
| 05226 Internalizing outcome/process | 潜力：failed trajectories识别/修复/复用形成内部process监督；具体学习信号尚待核心方法。v1Apr19+registeredMay8跨日，不先列确定候选。 |
| 05556 Extremely coarse learning objectives | P：细监督未必更人类视觉对齐→同数据PCA层级2～64类、数百CNN/Transformer与神经/人相似性对照→核监督粒度对表示选择的反证，不采用神经科学应用/脑机理推断。 |
| 05674 EGA | P：global contrastive adapter使unseen几何坍塌→zero-init residual+local margin triplet/hypersphere使满足margin梯度停止→核OOD扰动bound假设与实际高容量适配tradeoff。 |
| 05765 X-OmniClaw | C：multimodal ingress/短长memory/XML+vision grounding/BC replay统一mobile assistant；完整摘要仅组合与demonstrations，没有新grounding/执行正确性条件或反证，不能因三块变state/control收。 |
| 05848 VideoRouter | P：固定video compression忽略query时域证据不均→semantic allocation-policy router与early-layer relevance router区分coverage/detail→核token预算下保留必要证据与路由开销。 |
| 05922 DeScore | P：AR chain耦合reason/scoring的优化瓶颈→explicit-CoT后dedicated query/regression head+dual objectives→核reason质量与score校准分权，不授解释忠实。 |
| 06137 Prologue | P：重建token与AR可预测性冲突→只用ARCE学独立prologue而原visual tokens保重建→核ELBO与相近重建条件下generation改变。 |
| 06148 wAR-Tok | P：frozen two-stage tokenizer遗漏prior consistency→token distribution Wasserstein flow，用aux-currentAR与targetAR的token contrast只需forward→核先验匹配和重建代价。 |
| 06298 NOVA | P：opaque latents/heavy decoder→state表示为INR权重、解析render与content/dynamics结构分离→核生成/预测representation边界而非把视频预测等同真实物理model。 |
| 06222 FFDC | P：固定WAM action-chunk盲执行→predicted future与real observations一致性verifier自适应chunk+mixture-horizon→核效率/接触响应与false trust失效。 |
| 06175 VLA-GSE | P：固定PEFT预算下control适配/知识保留冲突→leading singular generalized experts+disjoint residual routed experts→核谱分解初始化与same-budget知识/动作双回归。 |
| 06421 FREPix | P：pixel flow统一频率路径→low/high频独立transport、factorized network及objective→核显式coarse/fine调度与low-NFE质量/成本。 |
| 06663 EMO | P：普通MoE剪domain experts能力严重退→document-shared expert pool约束形成可独立子集→核模块化训练与稀疏部署选择，不把active少等参数内存少。 |
| 06546 TokenSuperposition | P：预训练token/FLOPs成本→多token bag/multi-hotCE阶段再recover标准训练→核质量目标、时序信息损失和包含recovery的端到端成本。 |
| 06241 ReasonMaxxer | P：RL是否创造策略的判断→高entropy少数位置/top5替代+targeted causal corrections、RL-free contrastive gated训练→核干预对照/评价支持，只审稀疏选择证据不照录普遍“RL不学习”。 |
| 05630 TurnGate | P：multi-turn benign碎片积累风险→把candidate-response导致harm-enabling closure的最早turn作为monitor目标、matched benign分支→核时点/过拒tradeoff，非只添安全benchmark。 |
| 05443 SLAM | P：watermark扰动词频损质量→SAE结构方向因果steer语法几何→核word edits vs syntax paraphrase互补robustness边界。 |
| 05927 TextPro-SLM | P：speech/text gap不能只output侧缓解→同步text tokens/prosody embedding输入与语义保留训练→核转录/韵律分责与真实audio预算。 |
| 06132 MemReranker | P：semantic相似不等回答信息/阈值score可比→multi-teacher pairwise soft labels、pointwiseBCE calibration+InfoNCE memory任务→核score/usefulness与temporal/context heldout，不因新model family入选。 |
| 06283 Rubric modifications | P：analytic/holistic并非自动更一致→rubric例子/复杂度/聚合方式的human-autorater agreement方向变化→核rating协议与domain条件，修正judge设计选择。 |
| 06416 MiA-Signature | 待核心判定：submodular high-level concept cover压缩后conditioning与轻量更新，须核是否有真实新压缩机制/条件；不把global ignition脑类比或aggregate提升作为准入依据。 |
| 06485 Litespark | P：ternary权重若走densefloat不省乘法→CPU integer-dot SIMD加减执行→核packing/内核与已有ternary backend对照，保版本工程范围而不授通用速度。 |
| 06597 UniSD | P：SD组件联合常被凭组合名宣传→systematic agreement/EMA/tokencontrast/feature/divergence交互对照→核具体何时帮助/失败而非五模块相加。 |
| 05341 AEN-SAE | P：feature starvation不只data不足→l1 coding稳定性/encoder mismatch，l2强凸+adaptive l1的Lipschitz/support理论→核假设和有限LLM证据。 |
| 05209 Flat Minima | 潜力：reparameterization/sharpness混杂与function-level weakness替代及MNIST/Fashion对照；必要日期v1Mar24至registeredMay8跨日，不能只因五月ID纳当日。 |
| 05220 MidSteer | 潜力：affine concept erasure/switch最优条件与minimal disturbance替代；v1Apr17至registeredMay8跨日，需直接公开资格。 |
| 05387 Conditional diffusion linear constraints | P：measurement consistency不定conditional density→normal/tangent score分解+conditionalMI mismatch bound、projected Langevin init→核正确性假设/计算代价，不因inpainting应用排除基础生成机制。 |
| 06638 ScaleLogic | P：horizon与logic expressiveness混淆训练难度→独立两轴可控、scaling exponent/transfer比较→核 curriculum与compute合同，不把局部power-law外推普适。 |
| 06390 Automated alignment harder | P：自动研究即使无scheming仍可系统错→优化选择reviewer-blind错误、shared-model相关与aggregation过信四条具体风险链→标准核论证前提，不把概念风险算已观测事故。 |
| 06095 Metonymy vision models | P：part-centric attention默认local feature→部件标注测whole-object leakage、two-stage无泄漏对照→核attention解释权限和评价盲点，不据attention当因果。 |
| 06094 VISD | P：sequence reward与dense teacher监督不稳→advantage定update direction、structured privileged token信号调magnitude→核teacher/judge资格及direction/magnitude消融。 |
| 05285 Attribution-guided continual | 待核心判定：task element-wise importance调gradient与既有importance regularization区别在摘要不清；不得仅因可映射continual owner准入。v1May6T17:38Z在cutoff前，registeredMay8跨日，必要公开资格亦未定。 |

### A6日期原字段（在线DOI同A4，全部findable/arxiv.content）

以下组的唯一v1在May6T18:00Z之后且May7T18:00Z前，按官方规则最早May8T00:00Z；各registered均May8且BJT当日，合证本窗。精确Submitted与registered用于核身份/同日边界，不将Updated当实际announcement。

| ID | v1 Submitted UTC | registered UTC（均2026-05-08） |
| --- | --- | --- |
| 05556 | 2026-05-07T01:02:21Z | 02:13:06Z |
| 05674 | 2026-05-07T04:56:37Z | 02:15:52Z |
| 05765 | 2026-05-07T06:58:34Z | 13:00:49Z |
| 05848 | 2026-05-07T08:23:27Z | 13:04:13Z |
| 05922 | 2026-05-07T09:30:58Z | 13:07:14Z |
| 06137 | 2026-05-07T12:35:51Z | 13:16:00Z |
| 06148 | 2026-05-07T12:41:46Z | 13:16:27Z |
| 06298 | 2026-05-07T14:02:00Z | 13:22:33Z |
| 06222 | 2026-05-07T13:18:28Z | 13:19:26Z |
| 06175 | 2026-05-07T12:56:58Z | 13:17:31Z |
| 06421 | 2026-05-07T15:27:46Z | 13:27:33Z |
| 06663 | 2026-05-07T17:59:20Z | 13:45:54Z |
| 06546 | 2026-05-07T16:41:37Z | 13:32:37Z |
| 06241 | 2026-05-07T13:25:05Z | 13:20:12Z |
| 05630 | 2026-05-07T03:35:31Z | 02:14:50Z |
| 05443 | 2026-05-06T21:11:17Z | 02:10:22Z |
| 05927 | 2026-05-07T09:32:05Z | 13:07:26Z |
| 06132 | 2026-05-07T12:33:57Z | 13:15:48Z |
| 06283 | 2026-05-07T13:55:11Z | 13:21:56Z |
| 06416 | 2026-05-07T15:25:02Z | 13:27:21Z |
| 06485 | 2026-05-07T16:07:39Z | 13:30:08Z |
| 06597 | 2026-05-07T17:22:11Z | 13:34:42Z |
| 05341 | 2026-05-06T18:11:14Z | 02:07:58Z |
| 05387 | 2026-05-06T19:19:54Z | 02:09:02Z |
| 06638 | 2026-05-07T17:48:42Z | 13:44:53Z |
| 06390 | 2026-05-07T15:06:37Z | 13:26:16Z |
| 06095 | 2026-05-07T12:14:46Z | 13:14:16Z |
| 06094 | 2026-05-07T12:13:15Z | 13:14:13Z |

跨日资格仍普通恢复（不是外部终态）：05225(v1Apr19T07:25:39Z→registeredMay8T02:05:06Z)、05226(Apr19T10:33:19Z→May8T02:05:09Z)、05209(Mar24T06:14:05Z→May8T02:04:41Z)、05220(Apr17T19:23:33Z→May8T02:04:59Z)、05285(May6T17:38:13Z→May8T02:06:39Z)。不把这些潜力列确定候选，不通过一个字段为整批伪造日期。

## A7 — P1拟写窄段与纯source note（待root实际PRE）

root已实际P1必要Source独核通过7分与收窄命题，并授Ch29该项唯一窄owner待PRE。作者已按AGENTS再读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE与Ch28/Ch30交接；保Ch29既有Parallel-SFT等段，唯一插入锚点为§为什么少量高质量数据也可能有效的“重复大量同质 examples 可能快速降低 training loss，却造成 style collapse、过度拒答或对 prompt phrasing 过拟合。”后，不改Ch66。

拟正文：

> 对安全示教，“展示了正确拒绝”还不等于学会在未见情境下选择安全行为。当能力训练从聊天扩到工具和自主行动，先固定拒绝行为，再比较响应如何解释取舍、训练情境与独立持出行为，可以发现对某组 honeypot 的拟合没有迁移到更广审计的情况。[Anthropic 的受限数据对照](https://alignment.anthropic.com/2026/teaching-claude-why/)中，单按正确行为筛选不如高质量响应重写；让模型为用户的伦理困境提供建议，也能迁移到模型自己面临困境的部分评测。这些“理由”是 extended thinking 关闭时的用户可见解释，不是已取得内部推理真值；同 transcript 数控制也不等于完整等算力。
>
> 这给数据分布留下另一条可检验分支：先在 base model 上训练合成的原则文档或正面虚构故事，再用 generic chat SFT 适配交互，并检查后续 harmlessness RL 中的持久性；另可在固定用户请求下改变工具定义与 system prompt 的情境多样性。前者不能与普通 chat demonstration 静默互换，后者也不认证真实工具执行安全。文档构造、响应重写、训练与独立 OOD 回归均计费，persona/prior 是解释假说，有限零失误不授开放环境安全；当奖励鼓励违规、情境迁移或旧能力回归时，保留经核验的普通示教、原 checkpoint 与外部行为审计，不靠更流畅的伦理解释自签可靠性。 <!-- source-family:SF-2026-ANTHROPIC-TEACHING-CLAUDE-WHY-20260508 -->

拟本人source note：

> - 2026-05-09增量补查：对读Teaching Claude Why的Methods/训练顺序、同8k transcripts与response-rewrite反侧、旧held-out automated assessment、SDF→generic SFT→harmlessness RL及Limitations，仅采用安全demonstration内容/格式/情境分布的受限分支。用户可见解释不是内部CoT；零honeypot失误、token效率、persona/prior或局部持久性均不授普遍安全/唯一因果/任意RL不回退；未复现实验，唯一owner TRAIN-SFT。

## A8 — 06055 / 06113必要Source prepared（待独核）

轻量现官方abs信号检查：A4/A6共40个待核机制页面当前comments/abstract未读出官方withdraw/retract/erratum告示；06241的correction是摘要所说token修正，不当撤稿信号。05674仅added ack/github，06416明确work-in-progress，05927明确work-in-progress边界保留。没有为了“无标记”翻完整版本史；这不等于所有后版语义已逐字比较。

### 2605.06055 — 2+2+2=6，具体内核差额深入

- 精确[HTMLv1](https://arxiv.org/html/2605.06055v1)：实际读§3–4 design/schedules、§5实现前半和§6全部setup/results/limitations；§5中间细节首次工具输出裁剪，不冒称整节完整通读。拟命题不依赖未读code或指针API签名。
- pooled HBM/AclShmem或Memfabric的symmetric world-visible address域是已有下层能力，不记该论文发明。本文变化是relay/staging/reorder大payload tensor不再中转：dispatch直接写destination expert-window，combine由消费rank按路由/offset直接读producer expert输出并本地加权归并；count、offset、remoteaddress、status/synchronization、小temp仍在，不能翻成zero-buffer/zero-state。
- prefill保Layout→Notify的路由计数/offset规划以摊销大批token；decode把紧凑count/offset/address协调折入dispatch/combine，cache remoteaddresses仅可选fastpath，default结果是lightweighthandshake。旧relay方案提供交换可见区、layout target和同步anchor，在没有稳定远端address/同步域时仍合理。
- §6比较同routing/runtime的HCCL-enabled DeepEP，decode hidden4096/7168、quant/nonquant、batch16/32/64/80/128/144；大tokenprefill的relativebuffer开销更显，quantdispatch收益缩小，表2均值不是单一batch通用速度。
- 必要反侧：DeepSeek3.1 serving TTFT下降但TPOT30.10→31.31ms变差，不能写训推全指标改善。DeepSeek3.2 scheduling只在TTFT<5000/TPOT<60ms的作者测试空间成立。§6自称early set，完整memory footprint和systematicserving留未来；具体芯片/数量/链路、dtype/scale格式、serving输入输出长/并发完整合同Not Disclosed，不采通用百分比或生产SLO保证。未核code/未复现。
- 可采用机制边界：用stable symmetric remote-window替代大payload中转，phase-specific planning/coordination仍必须保留；全球可寻址不等硬件零复制或网络free。采纳/owner/当前差额尚待具体对读与独核，不预授Books完成。

### 2605.06113 — 2+2+2=6，具体同步路由差额深入

- 精确[HTMLv1](https://arxiv.org/html/2605.06113v1)：实际读§2完整模型、§3–4 F-score/two-stage、§5statefulproxy、§6setup/main/scaling/overhead；仅必要predictioninterface摘要，未遍历全appendix。
- 明确模型：stickyPD→decodeassignment，KV load `s_i+j-1`增长，`I(k)=G max(L_g)-ΣL_g`估同步空转；须有共享decodebarrier/EP域才有该目标，不把任意独立DP replicas写成普遍同步。对某worker加入Δload，相对当前最大负载safe margin `m=M-Lg`，`F=Δ-G max(0,Δ-m)`；safe内填负载有益，超过margin则惩罚不对称。先空slot多时greedy，slot稀缺时有限Rmax子集搜索，nonpositive时仍admit避免starvation；不是全局最优certificate。
- BR-H以H短horizon/discount投影剩余负载，β/γ经验校准；oracle只作上界参考。部署用Survival或prompt-hashExactMatch+miss回Survival，预测recurrence失败不继续信oracle。Proxy需全局active/load/waitpool/SSE进度，latebindKVtransfer、陈旧状态、取消/失败与中心proxy是额外代价；不能让“无engine改造”变“无runtime成本”。
- 评价：vllm-ascend V1/continuousbatch/PagedAttention、MooncakePD，DeepSeekV3671B W8A8/910C与Qwen330BA3B/910B部署；proprietary8k req(meanprompt3197/output1185)与Azure2024筛output>1000的10k req(mean4652/1052)，heavyload；Random/RR/P2C/JSQ对照。同trace下BR0与部署BRH对decode吞吐/TPOT有局部改进，但只报decode-stage，非完整端到端全请求成本/质量。
- 精确反证/未决：§6.1把主配置称144NPUs，但4P1D列4×16+32=96，§6.3/Table2又列G8=96/G16=144；不能引用“144NPU主结果”强保证。scaling/parameter-sweep用oracle，不将其+34.5%称部署predictor收益。完整arrivalconcurrency、模型quality回归与独立复现Not Disclosed。保留机制候选与局部数值限制，不以配置冲突否认算法差额，也不照录全部性能主张。

### 已实际完成层与资格局部更新

- P1：root Source/PRE通过后作者仅保存Ch29指定两段与纯source note；root实际顺读原同质段→新两段→ParallelSFT邻接和本人note POST通过（本日独核R3），锁释放。形式日报已同步该单项，不自签DAY。
- 06055：root已实际§3–5/§6必要Source独核通过6分与最小机制，具体owner差额尚未最终判定。
- [Are Flat Minima an Illusion?同作者先稿](https://www.preprints.org/manuscript/202603.1737/v1)已直接读publication状态、身份与完整摘要：Posted 23 March2026、DOI10.20944/preprints202603.1737.v1，已有function-preserving99x/weakness/PAC-Bayes/MNIST100networks等同一中心内容。因此05209本日首次公开资格关闭，非新增候选、不评分/不写Books；不从搜索日期或arXivSubmitted推公开。后版差异不在本日新增授权内，不扩March任务。
- 其余六资格：05248/06696/05225/05226/05220/05285已各精确标题官方索引/作者检索一次，未恢复足以收窄到May8的直接公开日期；arXiv历史单日两路径实返400/404，不能用聚合器Submitted代announcement。MidSteer官方GitHub与HiddenCoalitions作者研究索引已打开，仅身份恢复、没有直接May8公告日期；仍待有限原站日期/当前可核字段，未宣称全部恢复路径已穷尽。
- 已直接取回并完整阅读2025-01-06官方availability原件（raw.githubusercontent同commit路径），同日程与final-ID不可提前规则有效；不再依赖网页cache-miss或父上下文记忆。

06113 root独核补充关键反侧：§3.2将“空槽最多”直接称safe-margin足够，不一般成立；旧请求很长时有更多空槽仍可高residentKV，单个新请求也可overflow。因此拟采用时必须逐请求实际检查F/余量，不能照录空slot安全保证。其§2–6必要最小Source已由root实核通过6分；此反侧不删，只禁止未证明保证。

## A9 — 05538与06082核心准入解歧（拟P，新增Source准备）

- 05538 AgenticRAG实际§5.5完整消融与FailurePatterns读出决定性新条件：单轮8.41%至agent43.49/49.59的比较使用同proprietary快速搜索栈，并不是对所有dense retriever公平等预算；更重要的是Pony平均6.9gold docs而整体约1.9，coarse-to-fine少数高价值证据策略在广multi-evidence需求下失败。multiquery关闭R@1反略升(44.84vs43.49)而toolcalls6.79vs4.79，semanticfind关闭亦可提升(46.34)。这不是单纯“多tool组合更好”：明确需要在检索宽覆盖/深阅读之间按evidence需求切换，效率/质量反向是新成立条件。拟`1+2+2=5`标准，后续只需核§3–4实际harness/预算/评价协议，原§5.5不重读；未授Source完整或Books。
- 06082 PoTAcc实际§III-A、§V-A2/3/4、§V-B3及TableIV/V与结论：Transformer对象为ViT/DeiT，部分accuracy只训练CNN，latency/energy大量syntheticPoT权重，不把ViT速度当已保持质量的LLM。QKeras/MSQ/APoT的sign/exponent/zero-case编码不同，最大shift决定intermediateproduct宽（QKeras A8+maxshift7需15bit），统一更窄ipw会误导PEm成本；zero需mux；32bitaccum固定。hardware可复用机制是quantization格式→真实PE宽度/packing/CPUfallback/dataflow的端到端条件，非普通图像分类应用。确定贡献准入，拟`2+1+2=5`；还须§IV conversion/weight/transfer必要完整核后授Source。
- 06082反侧已读：CPU2threads/PYNQ-Z2与CPU4threads/Kria，conv/FC走accelerator、depthwise等仍CPU，跨层CPU↔DMA往返可吃完收益；Kria MobileNet/EfficientNet比CPU慢，VSAC相对VMAC_opt不进一步提速但可省energy。energy减idle基线、100次均值，不能称全板总能耗或所有backend加速。不要只复制3.6x/78%峰值。

## A10 — 06055具体已有覆盖与06113窄差额提议（待root owner独核）

### 06055拟Existing Coverage，唯一TRAIN-DISTRIBUTED-TRAINING Ch36

已实际顺读Ch36 §从Collective Call到Kernel内RemoteMemory完整局部：现文明确one-sided/symmetric peer预注册布局减少中间同步和额外buffer，却须保存registration/layout、peer/topology、lifetime、ordering/completion/failure；紧邻Purlin段已有layout与copy/reduce分层、ready/consume/reuse协调及bandwidth pull/latency push选择，ThunderEP段已有source一次发布/receiver直接取减少relay与phase差异；MoE dispatch节已有count/offset稳定address、payloadvisibility与combine Topk/数值次序。

因此06055的受限可采用命题——稳定地址域下directwindow placement/consumer read绕大中转、仍保紧凑协调和phase边界——已被这些具体正文承载；Ascend API/版本与早期收益不足改变通用完成合同，TPOT反退和未披露配置也不支持写成新普遍性能边界。拟ExistingCoverage，不为硬件实例强写同一one-sided原理；评分仍6，不因不写书降分。

### 06113拟新增可实作solver分支，唯一INFER-SCHEDULING Ch56

已实际顺读Ch56 §Barrier-synchronized Worker不能只按RequestCount均衡（原950附近）全部局部：现文已有stickyKV+barrier目标、resident-work与短lookahead、waitingpool/freshness/latency/TTFT/fairness成本及simulator证据限定。当前没有safe-margin分段F-score和oracle/实际termination预测分账，因此本次只提这一窄差额，不重写既有主线，不把生产性能数字或空槽安全误推纳入。

拟插在现“部署前还必须验证近似 solver 能否在 routing deadline 内完成。”后：

> 这个目标可进一步收窄成可在线求值的 admission 分数：令当前同步域最大 resident work 为 M，目标 worker 为 L，安全余量 m=M−L；加入等待请求的总增量 Δ 时，用 `F=Δ−G·max(0,Δ−m)` 比较填平余量与抬高全局最大值的非对称代价，再在有限候选子集中搜索。空槽数只决定可接多少请求，不证明其 resident-work 余量足够；即使只加一个长请求也可能 overflow，必须按实际 Δ 与 m 核对。短 horizon 可用带折扣的投影余量替代当前值，但 oracle 剩余长度只是分析参照，部署应保留实际 termination 预测及失配时的无预测回退。
>
> [BalanceRoute 的受限实现](https://arxiv.org/html/2605.06113v1)在 stateful proxy 汇集 active set、等待池与真实 decode 进度，代价包括晚绑定 KV transfer、状态陈旧、候选搜索与中心控制失败；所测 Azure 切片只含较长输出和重载，共享 barrier 假设不能传给独立前进的 replicas。拓扑计数存在正文冲突、扩规模部分又使用 oracle，故不由这些数字承诺生产 SLO、全局最优或通用扩展比。等待人口不足、预测漂移或路由预算不合时，保留无预测 resident-work 分数或原简单路由，并独立验收 TTFT、TPOT 与完整成本。 <!-- source-family:SF-2026-ARXIV-2605-06113 -->

拟纯本人note：

> - Daily2026-05-09补May08：2605.06113v1§2–6，只用共享barrier下safe-margin F-score/短horizon与实际预测回退；空slot不能证明safe，96/144NPU正文计数不一致，scaling/sweep使用oracle、Azure筛长输出/重载，不采精确部署扩展比/SLO保证；未核代码或复现，唯一INFER-SCHEDULING。

## A11 — 每日机构有限来源停点（不授无遗漏）

实际执行时间为本轮2026-10-18 BJT；所有查漏限定May08及紧邻日期。除下列明确原始事件外，搜索无命中只表示该查询未恢复，不证明全站无发布。旧本日报的有效同页历史相邻slice可以复用，但旧完成标签不作本轮验收。

| ID | 实际入口/查询与停止范围 | 结果/限制 |
| --- | --- | --- |
| SRC-OPENAI | Research主入口、定点`site:openai.com "May8,2026" research`及A2两官方事件全文；主入口ResearchIndex未恢复May日级完整历史分页 | C1具体组合关闭/C2Apr10窗外；历史分页限制不支持零遗漏，不影响两事件具体判断。 |
| SRC-ANTHROPIC | Research与AlignmentTeam公开列表，May8 TeachingClaudeWhy及May7 Donating条目相邻，当前精确研究文Methods/Results/Limitations | P1恢复并已实际Books通过；只复核这组历史slice，不称全机构无遗漏。 |
| SRC-GOOGLE-AI | DeepMind Research/GooglePubs实际打开、May8定点官方域搜索、DeepMindMay模型card列表；可见Gemini3.5FlashMay19等窗外 | 不恢复May8日级完整分页；科学应用明确暂缓不经通用owner回收。历史目录粒度限制，不作零命中保证。 |
| SRC-META-AI | 官方Research实际返回空正文，官方域May8定点检索与本窗arXiv家族身份交叉 | 必要历史日级slice未恢复，精确限制而非从空响应授已覆盖。 |
| SRC-QWEN | qwenlm重定向说明→qwen.ai/research及/blog实际200空壳、定点May8/2026-05-08查询 | 可见旧blog停2025；当前动态日期档未恢复。未以空页面说无更新。 |
| SRC-DEEPSEEK | /news官方研究索引直接读；可见研究Jun24/Feb25、产品Apr24等跨越本窗 | 该公开列表切片未见May8新独立事件，不扩历年；不是全站证明。 |
| SRC-MOONSHOT | platform.kimi.com/blog实际列表停2025Nov，MoonshotAI官方GitHub页面及May8定点query | 当前仓库不能替历史发布序列，历史slice未恢复，不作零遗漏断言。 |
| SRC-TENCENT-HUNYUAN | Research首查web timeout、directHTML无日期；按来源要求两次真实浏览器尝试，一次subagent visible不支持、后无visible创建仍超时；定点官方域May8查询 | 本轮未成功读动态全部列表；原件旧sliceApr30/May21只保原历史依据，不将其当完整本轮Coverage。需要该日官方归档或可复查日期索引。 |
| SRC-ZAI | 官方Research全部列表实际读，May20 ZCube与Apr29 ScalingPain跨越本窗 | 该日级列表切片未见本窗事件，加载列表停止在2025Dec；无需向更早分页。 |
| SRC-BYTEDANCE-SEED | Research主入口显示May16/Apr26，PublicPapers第一页20/246止May26；`?page=2`不可访问，官方域May8定点query | 旧报告有效page2历史停止点可作线索，不替代当前未恢复的分页。无新增确定事件，目录限制不授无遗漏；不把PublishDate覆盖arXiv资格。 |
| SRC-BAIDU-ERNIE | /blog/zh当前第一页完整跨越May9→Apr30→Apr15 | 原ERNIE5.1保May9旧归属，不搬进May8补窗；该列表May8未见新独立事件。 |
| SRC-XIAOMI-MIMO | 官方主站实际读paper/blog，paperJun29→Mar13跨窗、blog无日期；May8官方域定点检索 | Paper日级slice可核，Blog未标日期无法完整历史归属；精确保留Blog入口，不把未标日期全条目设队列。 |
| SRC-MINIMAX | 官方/blog当前列表直接读，May26→Mar18跨窗；IR官方Research引用作同索引旁证 | 未见独立May8研究事件；仅该列表切片，不扩News财报/其他非研究。 |
| SRC-ARXIV | A4/A6官方12类五月列表有限邻接题名+主题发现/完整题摘、188具名同事件去重；全部拟P精确v1/当前abs信号及同DOI合证，datehold定点 | 主要主题发现收口；本轮不继承旧91k抓取/Core/regex准入，不使用catchup/Created，未将整目录变队列。有限方法不宣称全学科召回。 |

未触发新的按需会议/版本扫描，不扫描每周组。机构历史缺段并非普通未读集合；本轮不会以它们作为候选证据或无遗漏/性能/安全保证。若取得May08带日期官方归档、稳定分页或明确原始发布，只重开该来源/事件；其余确定性论文与Books继续。

## A12 — 范围纠偏与作者必要Source（06057/06374，待独核）

- 05556 root实际完整题摘范围复核后，作者确认改判C：中心target是macaque electrophysiology/人fMRI及humanperceptualsimilarity，不是当前LLM/基础多模态模型效用；未见原文直接基础模型设计贡献，不能把brainalignment代理泛化为大模型训练而绕AI-for-Science暂缓。保A6原拟P判断痕迹与此具体改判依据，不评分/不候选/不Books，不再投入PDF。这是单项范围纠偏，不按保留率缩池。
- 06113 root A10实际PRE补G定义后作者已保存Ch56窄两段与本人note、自读完整邻接及note、限定diffcheck通过；尚待root实际POST，不计最终完成。06055具体NC由root实读Ch36局部通过。

### 06057 FalconGEMM — 2+2+2=6，具体执行/数值差额深入

精确[HTMLv1](https://arxiv.org/html/2605.06057v1)。实际读§III-A/B group与split实现、§III-C costmodel、§IV-A setup/§IV-C端到端/§IV-F数值；§III部分首次输出裁剪后以具名core补齐，不声称所有operator矩阵/stepwise附录已遍历。

- LCMA系数U/V/W是算法库提供的稀疏±1组合，不是本文发明新的乘法下界。降低rank乘法会新增CombineA/B/H的加减/访存；按同相对coordinate跨R作为group，一个unit读取源一次形成全部R，再在GEMM后就地CombineH避免中间H offchip写/读与重复输出竞争。Atilde/Btilde仍materialize，不能称全阶段零中间tensor。
- 系数compiletime常量与tiling/寄存器规划减少访问；group更粗会造成SM尾波，splitgroup persistentkernel/cacheaware调度为另一代价分支。其“跨SM确定执行次序自然无写冲突”文字本身不是任意CTA同步/内存安全证明，拟采用只限group-local数据复用与实际已核执行依赖，不移植该跨SM无atomic保证。
- costmodel区分GEMM算力、combine加减算力与offchipbandwidth，按shape/dtype/device估算选择LCMA或普通GEMM；memorybound标准GEMM本就合理。模型不是runtime全局最优证明，未披露tile/boundary推导不补造。
- 评价：H20/A100与Intel/AMD/ARM，linearshape来自DeepSeekR1/Qwen3.5/HunyuanVideo，FP32/BF16/FP16/FP8按设备能力；FP8是BF16→E4M3 block1×128完整workflow。对照cuBLAS/MKL/OpenBLAS/ACL/AlphaTensor/CUTLASS；effectiveFLOPS按传统2MNK归一，因此“超过硬件peak”是少做算术的口径，不是物理峰值失效。
- 端到端只测PyTorch替换linear的GPU prefill，staticB的CombineB离线，不能把该准备免费或扩成完整training/decode/SLO。relativeerror相对AlphaTensor约降低17.2%来自highprecisionH不降精存offchip，不证明与standardGEMM bitwise、LLM quality或长训收敛等价；code称uponpublication再开源，本轮未核实现/未复现。采用窄形状/带宽/中间态与数值合同，不照录通用7–18%或“production全平台”。

### 06374 ResiHP — 2+2+2=6，具体failure/recovery差额深入

精确[HTMLv1](https://arxiv.org/html/2605.06374v1)：实际读§5diagnosis/§6TP-PP-DP重配、§7状态恢复/通信实现、§8setup/主结果/消融/反侧。不是只从摘要推训练语义保持。

- fixedtokenbudget N下MLP约linear N稳定，但packing的attention按`Σ l_i²`而非N²；warmup估hardware/model成本，再沿真实F/BackwardActivation/BackwardWeight pipeline DAG预测healthyiteration。changepoint若超过预测25%才送Greyhound式validation，其他benign spike从时序剔除；这是workload-aware预过滤，不把所有可观测异常等同硬件故障，silentsdc/无liveness或timing信号不覆盖。
- failstop侧local心跳/进度聚合与central通知；TP选择memoryfeasible且head/layout兼容的poweroftwo子组，按吞吐/最慢者权衡，未选设备保standby；PP给慢stage少layers，DP再按Fchunkprogress迁移待执行microbatch，要求每stage/workload一次、相邻activation/gradient依赖和目的liveactivation内存上界。不是任意位置透明换并行度或全局最优。
- §7重建communicator并reshape：healthyreplica当前iteration完成后同步最新已提交参数/optimizer；不同replica故障使缺state时必须pause，回lastcompletediteration persistentstate；layer移交parameter+optimizer一起搬，TP变则reshard。异构TP P2P按较大TPdegree scatterchunks再机内gather，原owner/完成顺序仍需保存。
- 评价32nodes×8A100/NVSwitch/200GbHDRIB、CUDA12.2/NCCL2.20.1，LLaMA2/Qwen2.5，故障由kill/lockSMclock/sidechannelbandwidthcontention注入；相同trace与Greyhound/Adaptra/ReCycle/Oobleck及strengthened复合对照，非真实所有failuretaxonomy。2500step7B loss重合只支持该测试，不采“strictconvergence/最终quality全保持”的作者强句；warmupprofiling不含在1.2–1.5%iterationoverhead，layertransfer需摊销，故障后state同步与同seed逐bit未证明。
- 精确反侧：Table5 Greyhound falsealarmoverhead列2.24–3.72s，正文却1.24–1.72s，不能引用其精确倍率；small falsealarm0、medium有0.1/0.3，不写零误报。§8.3“reduce delay to0.64x/2.03x/8.72x/11.14x”的数值方向不一致，不采用。需要保留warmup/模型失配、重配置/状态传输费用与原checkpoint回退；本轮未运行内部framework、未复现。owner具体差额待对读/独核，不因有failure框架名自动写Books。

## A13 — 暂停checkpoint（用户明确要求；作者ownership释放）

用户要求暂停并保存进度。此段覆盖A1–A12所有普通“继续”指令；不再新研究、Books写入、候选扩展或接05-10。README保持进行中、本日未DAY/FINAL，不计全年验收。全部作者窄写权释放，root只接已保存06113实际POST及行政checkpoint；尚未核的Source/owner不得预支通过。运行前与并发index/worktree修改保留，本方未stage/commit/push。

### 已完成、可直接复用

1. 当前AGENTS及适用合同/ROADMAP/本日上下文重读；完整baseline规范命名保存，原1ERNIE候选整行/日期/评分/小时窗与连续原§4保持。
2. 主要主题发现已封口。A4/A6共51精确v1完整题摘及代表独校准；原May08只提188唯一ID去重，未继承其长正文或评分。列表不是51候选/Source完成；不恢复旧全量Core/regex/Weekly。
3. P1 TeachingClaudeWhy：7分、必要深入、root实际Source/owner/PRE与Ch29两段/完整局部邻接/本人note POST已通过；正式六部分已同步该单项。
4. 06055：6分、必要Source及Ch36具体ExistingCoverage由root实际通过，无Books新写；正文具体承载见A10，正式表/证据已同步。
5. 06113：6分、必要Source及Ch56具体差额/PRE通过；按root补G定义后作者仅保存指定两段/本人note并自读，暂停保存时root实际POST尚待，不能自己认证通过。原文空slot→safe不成立、96/144计数冲突和oracle/deployed分账继续保留。
6. 代表关闭：C1OpenAI控制组合、C2AxiosApr10窗外；05253/06671/06230与05765具体仅资源/组合关闭，05556依target范围改判关闭；05209由PostedMar23同作者先稿退出本日首次公开资格。后两改判的实际证据/理由保留A12与A8尾，不评分、不Books。
7. A11每日机构实际入口/停止点与历史限制已保存。明确缺段不授正面Coverage/候选/无遗漏；本日普通论文/owner队列不是外部受阻。

### 普通差额，恢复仅接有效层之后

- **必要Source作者prepared、未独核：** 06057 FalconGEMM、06374 ResiHP，实际范围/机制/评价/精确反侧均见A12；不重读已完成局部，也不称其Source通过。两者还无具体Books决定/PRE/写入。
- **部分必要core已读、Source未完：** 05538 AgenticRAG的§5.5具体广证据失败/多query反侧已读，需§3–4 harness/预算协议；06082 PoTAcc的PE宽度/模型范围/quality-vs-syntheticperf/CPUfallback/energy反侧已读，需§IV conversion/weight/transfer；06416 MiA-Signature只有完整题摘和heading导航，必要§3/§4实际core尚未读完，准入仍待解歧。
- **HTML已恢复heading与有限主文、仍普通：** 06534 ROSE、05639 TokenStack。暂停前有两条已发网络读取（session24279/61505）返回未接收；不把在飞/可能已完成输出算实际阅读。现有确定已读层只包括A4完整题摘，以及前次裁剪输出可见的ROSE§4开头/VMM前段、TokenStack§7–8评价/limitations；ROSE§4.1后半/4.2/4.3和§6完整、TokenStack§4–6仍需按具体命题补读，不为裁剪误标全文。
- **已完整题摘/身份日期、必要Source仍待：** A4的06184/06235/06647/05703/06623；A6的05674/05848/05922/06137/06148/06298/06222/06175/06421/06663/06241/05630/05443/05927/06132/06283/06485/06597/05341/05387/06638/06390/06095/06094。各自精确原文与准入链在A4/A6；heading导航不是Source完成，root局部准入或代表抽核也不是全文Evidence通过。
- **06546 TokenSuperposition：** HTMLv1实际404，精确[PDFv1](https://arxiv.org/pdf/2605.06546v1)已恢复25页；只实际读tool返回的abstract、intro与§3最前段（embedding平均、nonoverlapbag、丢bag内序、恢复标准causalobjective），尚未读关键公式/table/实验/限制或视觉核表。PDF技能已完整读取，尚未渲染/生成新文件；恢复用其必要页，不误记PDF不可得或完整Source。
- **本日报普通：** 除三已正式同步项外，其余明确增量仍在本SUP准入/Source分层，后续需必要评分、独核与Books具体决定，再合并六部分、DAY及完成态FINAL；不因暂停把这批潜力/未读当完成。

### 六个必要日期资格保留（尚未足以终态隔离）

05248/06696/05225/05226/05220/05285：A4/A6保完整v1/registered原字段、精确DOI身份及跨日失败范围。已尝试官方历史日列表（400/404）与各精确标题原站搜索；05220官方repo、06696作者research索引已打开但未取得直接May08公告日期。缺的是足以限定May08首次公开的直接原站/归档，或明确更早正文退出证据；不是只缺Created。恢复先看这些具名入口是否有日期字段，必要时定点隔离/退出；不得从早Submitted或五月ID硬判早公开/May08，也不为所有假想渠道无限追查。

### 校验与保护

暂停态README同步06055/06113后已重跑V3接口通过，README/SUP/Ch29/Ch56限定diff-check通过；只证明接口与空白一致性，不代语义验收。原1ERNIE整行恰好1次、原小时窗及连续原§4实比保持；baseline与启动原始完整文本逐字一致（5329字符，修正了创建时多余的单个EOF空行，未改任何原内容）。根独核独立记录保本日SUP_REVIEW，父agent可只补既成POST事实，不由作者自签DAY。

暂停保存后行政同步：root已实际完成06113 Ch56两段/完整邻接/本人注POST并存独核R5，正式README同步这一既成事实；P1和06113均有真实写后复核，06055已有覆盖成立。本日日级仍未验收，其他普通待办不变；不再研究、扩池或写Books。

## A14 — 用户明确恢复：只接差额（2026-10-18）

本段覆盖 A13 暂停指令。恢复作者 `may09_resume_author` 已完整重读当前 AGENTS、Prompt、研究/Report 合同、来源说明/每日/arXiv、ROADMAP、Learning State 的2026暂停路由与本日A13/R5；技能 using-agent-skills 用于范围和可验证出口。仅写本日报与本唯一SUP，不改baseline、Books、State、索引或其他日，不stage/commit/push。原1 ERNIE整行/日期/评分、原小时窗与连续原§4保留；两实际POST和06055具体NC复用。05556误收已关闭，不恢复；发现封口，不把51题摘转全文队列。

### 05538 AgenticRAG：必要Source差额 prepared，拟1+2+2=5

精确 [HTMLv1](https://arxiv.org/html/2605.05538v1) 已补读§3–4、§5.4成本与§5.5反侧；与A9有效层衔接。15轮上限/强制完成、128K摘要阈值、引用保留、每次至多五查询/各十结果是作者harness，不是形式充分性保证。BRIGHT long-doc、WixQA factuality与FinanceBench correctness不能合并同一指标；单次搜索为同proprietary backend，不能把差额全归tool策略或当等预算胜dense retrieval。总token含thinking/tool/结果；FinanceBench约7.8倍单轮token，不采“轻量”即低总成本或生产就绪。关键可采条件仍为证据广度需求上升时coarse-to-fine深读会失效，multiquery主要减少调用而非保证更高R@1。硬件/precision/并发/SLO、独立复现Not Disclosed。Books未决，非作者Source尚待。

### 06082 PoTAcc：必要Source差额 prepared，拟2+1+2=5

精确 [HTMLv1](https://arxiv.org/html/2605.06082v1) 补齐§IV-A/B/C，复用A9已核宽度/评价反侧。转换先按原quantizer forward恢复目标量化权重，再经Nobuco/TFLite；int8导出后MSQ/APoT须把scale修回PoT整码，并同步bias scale，而非只把权重重新编码。每byte两4bit code、prepare阶段preload全部权重要求足够DMA容量；首轮与持久准备成本不能静默省略。只复制各GEMM实际需用tile、不让更大buffer名义容量冒充减少全模型流量。CNN accuracy对照不能给synthetic-weight ViT/DeiT速度补上质量验收；CPU fallback/跨层搬运和idle-subtracted energy边界保留。可采命题为格式/scale/bias/PE宽度/packing/prepare与实际路径共同决定执行产物，未核代码或复现；Books/独核未决。

### 06416 MiA-Signature：核心解歧后准入，拟1+2+2=5，Source prepared

精确 [HTMLv1](https://arxiv.org/html/2605.06416v1) 实际读§3.1–3.2、§4.1–4.4、A.2–A.5与G。准入不取脑类比或普通摘要组合，而取具体检索/生成接口反侧：同retriever/generator下signature可改变检索候选，但把signature或累积evidence再喂generator并不总帮助；NarrativeQA/NovelHopQA部分answer-time附加状态反退，NoCha需要组合状态。这会改变“有用检索状态必然有用回答context”的设计判断。

实现以离线每20chunk的GPT4o摘要、step0 top50/最多五summary、后续20chunks/三步与query-signature混合；须保存原chunk与summary映射，signature只是派生prior，不替代证据。NovelHopQA保固定query、别的任务改写，不宣统一策略；额外摘要、encoder与更新调用均计费。§4.2/表2的agent用First-K，而A.5又说all main results用submodular，存在口径差异；只取表中可分离接口对照，不采一套全局配方。A.3的1−1/e只在去diversity后的子目标及额外非负等条件成立，原cosine fQ也不自动单调；不采全目标保证。证据限文学/narrative，未证代码/多模态/真实长期memory；未核实现/复现。Books与非作者独核待办。

## A15 — 下一两项必要Source prepared

### 06534 ROSE — 2+2+2=6，具体co-serving差额深入

精确[HTMLv1](https://arxiv.org/html/2605.06534v1)补齐§4–6必要原域。CUDA VMM分开各模型virtual-KV空间与共享physical pages；serving burst时按request回收rollout KV并abort/reroute，budget减半后冻结到下一RL step，不是无损地把旧KV改属另一个模型。serving-first compute使用每tick profile预测TTFT/TPOT余量，仅admit能容纳的chunked rollout，512token/20%headroom/2s timeout均为作者例值，非通用保证。跨池relay以shard key、COO稀疏Δ和正确旧权重重构发布；浮点减加与异步copy本身不证明bitwise、atomic或任意policy freshness，不能由“lossless”自签训练等价。

评价H800两池/各池400GbIB/跨池200GbEthernet，Qwen3-8B/32B与FrozenLake/ALFWorld、GRPO/DAPO和one-step offpolicy；borrowed16/64 GPUs是额外有效资源，不是同GPU预算加速。Serving replay为Microsoft24h trace、Qwen2.5-7B/32B、PD1:3，P99(TPOT,TTFT)分别(150,500)/(450,1000)ms；不能套引言100/50ms例值。Table2仅memory管理仍超TPOT门限，必须与dual-SLO调度区分；§6.5不共置baseline延迟更低。Serverless baseline是作者按产品设计实现，非真实厂商服务独立测量；“0% allocation overhead”不等没有activation/压缩/重构/迁移或组织成本。高非零比例约20%时稀疏metadata抵消收益，profile漂移/服务burst超预计或无空闲时保专用rollout与完整snapshot。未核artifact/复现；必要Source尚待非作者核，owner未决。

### 05639 TokenStack — 2+2+2=6，具体PIM容量/布局差额深入

精确[HTMLv1](https://arxiv.org/html/2605.05639v1)实际补读§4–6并核§7–8配置/限制。将dense capacity层与减容量PIM compute层放同stack，base-die MC持逻辑到物理映射并做page-DMA/inline K8V4；热度与PIM适用性共同决定驻留。K按token分bank、V按dimension分bank减少各阶段cross-bank reduction，却仍有query/attention-weight广播、TSV与跨卡callback；cold-KV晋升要反量化/转置，不是免费透明恢复原值。FP16→K8V4→FP16有量化误差，引用他文平均0.3%并非本文全部trace独立质量试验。

必要反侧：§4文字capacity-near-base/compute-top与figure短述顺序不一致；§5.1代γ≈1/B本得2d与d/2，文称含hysteresis约4d/d4但未给变换，不采用精确阈值。§6.2以负ReuseProb做lex-min反而优先高reuse，与正文“低reuse先demote”相反，且CDF差未条件化到已存活age；不照录policy公式/伪代码或概率保证。只采用分域/布局/完整搬运成本这一硬件机制。

证据为AttAcc/Ramulator2 cycle模拟+Python frontend/CACTI，不是实芯/RTL控制器或现成DGX部署；“DGX-A100/HBM3/UCIe”等为模拟组合，不给实际机器背书。W16A16/四model×四trace的arrival/order/reuse重放与不同物理容量需分账；自定SLO是p50 e2e不超过最低点2倍，非P99TTFT/TPOT生产门。939倍来自队列膝点两侧，非raw kernel速度；4B/thinking约1.03倍保明确弱收益边界。两级加权service time不等单tier hit率，全部controller/复制/迁移/量化成本及fallback保留；未核代码/复现。owner拟Ch54，待实际对读/独核。

## A16 — 06057/06374 Source通过后的逐字拟文（尚未PRE/未写书）

root已实际核两精确v1必要原域，各6分最小Source通过；cost单位/跨SM/physical peak与25%阈值限制按反馈收窄。作者已完整读取PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、各target实际局部与Ch48/50、Ch35/37交接。

### 06057 唯一INFER-TENSORRT-LLM Ch49

拟位置：§GEMM现“Attention 的 Q/K/V/O projections…会形成不同 kernel search spaces。”后、SISA形状分工段前，保现有段落不重排。拟一自然段：

> 形状选择也可以向上推进到乘法算法，而不只在同一 GEMM 中调 tile。对足够大的 dense 矩阵，算法库提供的低乘法次数分解可先用稀疏加减组合构造输入、执行较少子 GEMM，再组合输出；省去的乘法却新增中间态与带宽需求。一个受限执行分支按相同局部坐标组成 group，复用一次输入读取形成多路组合，并在子 GEMM 后就地完成输出组合，减少中间结果的片外往返；输入组合仍可能物化，group 加粗也会增加寄存器压力与尾波。选择器因而要共同估计 GEMM、加减和实际 bytes/带宽，所有量保持相容单位，再按 shape、dtype 与设备比较普通 GEMM。[FalconGEMM 的有限对照](https://arxiv.org/html/2605.06057v1)只支持这条执行取舍；按传统 FLOPs 归一后“超过峰值”不等硬件峰值被突破，GPU prefill 的离线权重组合也不能免费，较低中间舍入误差不授逐 bit、完整模型质量或训练收敛等价。带宽占主导、准备不能摊薄、数值或依赖未验时，保留成熟 GEMM；group 内复用更不授权跨 SM 无同步写入。 <!-- source-family:SF-2026-ARXIV-2605-06057 -->

拟纯本人source note：

> - Daily2026-05-09补May08：2605.06057v1 III-B/C、IV setup/e2e/numerical；6分，只采用LCMA group-local输入复用/就地CombineH与shape-cost分支。cost单位须一致，A/B仍可物化、离线CombineB计费；effective FLOPS非物理超峰，未授跨SM顺序安全/逐bit/质量/收敛等价。未核实现或复现；唯一INFER-TENSORRT-LLM。

### 06374 唯一TRAIN-DISTRIBUTED-TRAINING Ch36

拟位置：§Failure不再是单进程退出现“Elastic membership 对纯 DP 相对容易…checkpoint correctness 是分布式容错的前提。”后，R2CCL链路局部恢复段前。拟一自然段：

> 启动恢复之前，还应先解释一次健康 iteration 本来应有多慢。固定 token 总量并不固定 Attention 成本：packing 后的序列长度为 l_i 时，相关工作随各段平方和 Σl_i² 变化，而 MLP 更接近总 token 数的线性项；再沿真实 forward、activation-backward 与 weight-backward 的 pipeline 依赖组合，才得到当前 workload 的健康时间预期。一个[受限故障诊断分支](https://arxiv.org/html/2605.06374v1)先用 warmup 校准该模型，将仍不能解释的 changepoint 送进一步 validation，而不是把长度变化或每次时延 spike 直接当 fail-slow；作者使用的25%只属其配置，不是通用诊断阈值。它增加 profiling、预测失配与漏检成本，不能识别没有可见时序信号的 silent corruption。检测成立后，改变 TP/PP/DP 仍须重建 communicator、连同 parameter/optimizer 一起迁移或重分片；缺少可信当前 state 时回最近 committed iteration。有限注入故障与短程 loss 重合不证明任意重配或最终收敛等价，模型失配、状态不全或恢复费用过高时，保留原检测、静态 plan 与 checkpoint 重启。 <!-- source-family:SF-2026-ARXIV-2605-06374 -->

拟纯本人source note：

> - Daily2026-05-09补May08：2605.06374v1§5–8；6分，只采用Σli²+真实pipeline-DAG健康时间预测、再validation的诊断分支及既有状态恢复边界。25%为作者配置，profiling不含iteration overhead；Table5正文数字冲突/延迟倍率方向不采，短程loss非普遍等价。未核内部framework或复现；唯一TRAIN-DISTRIBUTED-TRAINING。

## A17 — 三项必要Source prepared（不授独核或Books）

### 06184 Teaching LLMs Program Semantics — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06184v1)实际读§3–6与Table1关键两类分账。平衡500个single-file C tasks/五properties，holds/violated各50，verdict不是machine-checkable witness；四次inference重复不是四个独立训练seed。主训练Qwen3-8B的CPT为Soteria3208 manifest-bug HTML traces，code-only按相同文件数控制、不等同token/compute；原CodeParrot与SVCOMP未显式dedup，不授无污染。更多trace同时改变bug composition，不能因规模越大越差推出数据量本身致因。

关键边界为训练分布/结构与inference thinking的交互：HTML-bug+COT提高violation检测，但holds由90.7降78.0，不能只报67.3的violation；全部34k traces/code-only可反退，plain/informalized的unparsed大幅升高，格式与completion预算不能剥掉。8k到24k预算仍有timeout，按parseable子集的高分不能替固定分母。单模型/工具/C、短single-file及五property有限迁移不能证明formal verifier或任意安全审计替代。拟唯一ownerTRAIN-PRETRAINING/Ch28，具体差额未核；未核代码/weights/复现。

### 06235 OBLIQ-Bench — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06235v1)实际读§3–5，Table的全数未作采用命题。以真实语料先抽latent属性/聚类再写不带identifier的query，并用pool补标；不是任意难题都证明retriever缺陷。评价把普通候选pool与gold-injected pool分别交同reasoning reranker，pool-scale时仍保gap；gold注入是诊断反事实，不是实际retriever收益或全局可达上界证明，reranker稳定性/LLM相关judging与漏标仍限制。WritingStyle有外部authorship gold，不等其他任务全人工真值。

具体增量：能在给定文档后验证关系，不等能在大语料先找出；多轮query改写对style可能抹掉目标信号，WildChat分散行为也未明显帮助。Congress有单gold、四hop后R@10/50/100同平台，是候选面失败而非继续深排可修复。dense pool并不对每个模型同hard-negative构造；不能把所有数值当完全等预算因果或泛化“dense无用”。全语料属性抽取/多轮标注、pool/rerank/search调用均计费；未核实现或复现。拟ownerAGENT-RAG，待具体正文比较/非作者核。

### 06647 SIRA — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06647v1)实际读§3–4含主表/limitations。离线按doc扩新词进index，online以LLM提出缺失evidence词，DF上界过滤两侧、online另需DF>0，再与原query加权BM25单call。DF只检存在/稀有，不证明相关性或事实正确；doc侧没DF>0下界，不能写双侧统一同规则。十BEIR、共同frozen Qwen3.6-35B-A3B-FP8的部分LLM对照支持局部实现，仍未单独消融DF/离线扩词/weight及额外全语料LLM预算，不能全归某一机制或宣无训练即无准备成本。NQ/Quora部分retrieval不最优。

§4.3 answer-string coverage与他文generated-answer accuracy不是同metric，不能照录“击败全部QA agents”或把matching string当充分grounding。完整hardware/batch/latency/SLO、index增长与维护成本未披露，远离LLM先验的语料未测。可采范围仅corpus-statistics约束的可解释lexical提案、保原query与词面/hybrid退路；未核实现/复现。拟AGENT-RAG，具体Books/非作者核未完。

## A18 — 两项multi-agent必要Source prepared与两Books差额

### 05703 Active Task Selection — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.05703v1)，实际读§4–6必要方法/评价与A.1.3–4、D.2/B.6；长输出中batch reuse尾句未完整显示，不采用其所有复杂度。已有答案的task pool中，用图logits ensemble经MAS rollout+evaluator得到score，再单步EKI/Gaussian KL估task对图优化的信息量；信息量是近似selection proxy，不是准确posterior/无标签EIG或task-value真值。代表pool+surrogate/Thompson减少昂贵rollout，图训练本身仍REINFORCE，不混为同算法。

六GPT4.1nano+decision agent、MMLU/GSM8K及三具名攻击agent下，比较小预算的task selection与均值/尾部稳定性；额外selection费用不能从等训练budget中消失。D.2实际独立seed数量不等，bootstrap10k；benign均值/尾部CI均跨0，attack MMLU均值也跨0，仅部分lower-tail/attack GSM8K明确，因此不采普遍稳定改善或“鲁棒安全”。EKI精确采样依赖linear-Gaussian，有限ensemble/非Gaussian图后验无全局保证；更多模型/拓扑/无标签设置未证。采用task-selection应与graph-update及全调用预算分账，漂移时回random/代表采样与固定graph。未核实现或复现；owner拟AGENT-MULTI-AGENT，待具体对读/非作者核。

### 06623 MASPO — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06623v1)实际读§3–4必要核心/评价、相关消融说明；Table2全部数字未作为采用范围。topological coordinate式交替优化时，上游改变输入分布会令旧beam分数陈旧，于新epoch重新对当前best比较；local validity、直接successor lookahead和final-output的judge偏好分责，局部合法/下游无益的trace进hard-negative buffer。此处是prompt proposal/evaluation协议，不证明因果credit或运行时执行权限。

Qwen3-8B nonthinking、Gemini2.5pro optimizer/evaluator、50未标注样本池、两拓扑/有限数学推理代码任务；same steps与same Gemini calls只是两个不同预算控制，不等全token/硬件/总成本相同。局部/组合/refresh消融支持在所测设置下复合策略，不授“唯一因果”或topology-agnostic普律；无GT判断可能同源相关且被反复优化，held-out actual success仍须独立验收。更深lookahead无收益仅当前任务，不证明one-hop普遍充分；同prompt迁模型是有限transfer非独立system安全。角色/peer版本、trace、judge与预算必须绑定；judge漂移/优化过拟合时保原prompt、固定graph与持出回归。未核代码或复现；owner拟AGENT-MULTI-AGENT，待非作者核/具体Books比较。

### A16写后实际状态

root已实际核两逐字稿/当前邻接PRE并授精确一段+本人note写权；作者保存两段/notes并self-read与限定diff-check。Falcon Ch49:468/本人3167由root实际POST通过，窄位释放。Resi Ch36:1062/本人2302的首次POST指出Σli²须block-diagonal attention，作者仅将假设修为“采用阻断跨文档注意力的 packing、各段长度为 l_i 时”，保其余全文不变；root仅此必要假设差额待回读，未预授通过。A16保存的原逐字稿是历史PRE文本，实际采用以本假设补充为准。全部其他Books未获许可、未写。

## A19 — 05538/06416具体owner判断（Source已root核，未PRE）

### 05538拟具体已有覆盖：AGENT-RAG Ch76

实际对读Ch76§Recall还要服从固定Context的可用工作集（682起）与§Relevance不等SufficientContext（690起）：已有正文明确单文件深度、跨源diversity、关键依赖完整度与最终任务成功须同时报告，不能由更高recall或更多读取批准sufficiency；后节还分菜单出现、实际open与实际use。AgenticRAG的可采命题是evidence广度与深读的预算取舍、multiquery减少调用不等质量提高；当前正文已经承载这项选择，没有未覆盖的执行/正确性机制。Pony6.9vs平均1.9只是当前benchmark的受限说明，不足单独再开同一知识分支。因此拟5分标准完成/ExistingCoverage，保新验证与反侧在报告，不因已有覆盖撤候选或降分。待root实核此具体NC。

### 06416拟窄新增：AGENT-RAG Ch76

现§Chunking已有摘要树选择候选与来源权限，但没有将同一派生摘要状态的retrieval-time使用和answer-time使用分开验收的具体机制；Ch75拥有调用assembly、Ch77拥有跨调用持久写入，本条不改那两章。拟接Ch76跨文摘要树段后（当前source-family2605-00529完整段后）、“检索单元与交给reader的内容…”前，一自然段：

> 派生摘要还可以作为检索条件，而不必全部进入最终回答 Context：先从原 chunk 命中的高层摘要形成紧凑的全局线索，再让后续检索同时消费原问题与这份线索；迭代时分别更新搜索意图、已取证事实和全局线索，不把三者混成同一事实状态。这样的线索可能帮助找对语义区域，却仍可能干扰已经足够直接的答案路径。[MiA-Signature 的受限对照](https://arxiv.org/html/2605.06416v1)中，检索侧改善并不保证向 generator 追加 signature 或累积 evidence 也改善，任务和 reader 应分别验收“用它选材料”与“让它参与回答”。摘要离线构建、额外编码和每轮更新均有成本；文学语料、有限迭代与存在口径差异的初始化实验不授全局选集保证或开放域效果。线索漂移、摘要丢失前提或回答反退时，保留原问题、原 chunk/hybrid 检索与只交付必要证据的 reader，不让压缩 prior 替代支持。 <!-- source-family:SF-2026-ARXIV-2605-06416 -->

拟纯本人note：

> - Daily2026-05-09补May08：2605.06416v1§3、4.2–4.4/Tables1–2、A.5/G；5分，具体接口差额深入。仅采用检索条件状态与回答Context分门验收，保文学/三步/离线摘要与更新全费及任务反退；FirstK/submodular口径差异、全目标保证/精确配方不采。未核实现/复现；唯一AGENT-RAG。

## A20 — 三项模型/表示必要Source prepared

### 05674 EGA — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.05674v1)实际§3–5/Limitations、A.3–4。zero-init residual+unit-sphere projection/局部triplet hinge满足margin即停该triplet梯度，不能因未见class没入triplet就说parametric MLP不会动unseen几何。A3有界triplet梯度G、参数Jacobian L、gradient-flow路径才得到累计active-ratio积分界；small steady-state ratio不抹掉早期累计，不把input Lipschitz偷当parameter Jacobian，更不自动覆盖AdamW/weight decay。A4方向与unseenJacobian不相关明确conjecture；不采用标题式无条件OOD下界。

CLIP/DINOv2/SigLIP frozen image encoders+ANN，LP@K的语义标签质量与AR@K几何近邻重建分开；对照matched参数量不等相同functionalcapacity，§4.2“一样adapter只不同loss”不能套给LoRA行。EGA在CIFAR10/Food可较frozen/低秩路径退步，worst-case只是有限四数据min、marginablation只有ID非OOD。可采增量为适配时loss停止压力与容量限制两分支须以未见类语义质量而非ANN recall单验收；不保证高维局部保护/全系统无重建。训练/重索引/回归都计费，未核代码或复现。owner拟AGENT-RAG，待具体比较/非作者核。

### 05848 VideoRouter — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.05848v1)实际§3–5必要方法/评价、B/C标注审计。两router分配policy与frame relevance：Global保uniform覆盖、Fragment将高分frame留细节，极紧budget仍会丢highpriority，context长度预算不证明无OOM或证据全保。复制前四LLM层作shadow pass而非免费重用一次已算特征；三阶段含joint backbone微调，不能把总差额全归路由名。

InternVL3-8B/4H20、controlled64frames与max12288tokens另有实际tokens不同；与默认38frames比较不算相同观测人口。低budget64frame可优于128、充足budget反向，直接支持coverage-v-detail成立条件。额外router精度/5.1%开销是有限depth设置，不授跨model通用Pareto。监督由reverse-QA/counterfactual过滤与A/B policyprobe构造，B中两人500样本审计的policy94%/frame88.4%，不是标注全真，mixed需求正是误差来源。无benchmark视频参与训练为作者声明非独立全污染审计；真实稀有事件漏帧/错误routing仍须回full/higherbudget。未核实现或复现；拟MULTIMODAL-REPRESENTATION，待owner/独核。

### 05922 DeScore — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.05922v1)实际§3–4/I，未采用A/B理论梯度结论或遍历无关附录。先生成CoT，再追加Reward query以regressionhead产scalar；coldstart做BT与CoT随机mask，后stage用GRPO调格式/子项分数/长度，辅BT维护pairwise排序。CoT质量reward的labels含teacher生成筛选，不当human细粒度真值；BT ranking不授概率校准、解释忠实或独立验证。

Qwen3VL8B、22k人偏好pairs+1469ID，2fps、LoRAr64coldstart再RL；T2V/GenAI/VideoGen各有限协议。去BT时VideoGen偏好准确率反退支持reasoning与score目标不能互代；随机mask与attention图不证明visualgrounding的唯一因果。Acc含/不含tie不可混，GenAI含tie并非最佳，76%少data非等compute成本。下游Wan1.3B有限GRPO/DPO不证明所有视频质量维度改善；I明确motionimplausibility/visualartifacts较弱。全部teacher/CoT生成/二次score前向与校准回归计费，保直接reward/原prompt与独立human/heldout检查。未核实现/复现；拟TRAIN-RLHF Ch31，待owner/非作者核。

## A21 — 06082具体owner差额逐字拟文（Source R8通过，未PRE）

Ch49现1112已定义格式/scale/图/artifact、1116将ternary辅助bias与consumer绑定，但没有PoT码表示与真实intermediate PE宽度的关系，也未把重新编码后的scale修正与bias重定标串成具体条件。本文不因更少bits新写容量原则；只提这条格式到datapath的窄分支。唯一INFER-TENSORRT-LLM；位置拟接§先定义低比特表示的INT4手算例后、§粒度与校准前。拟一自然段：

> 低位码也可以表示带符号的单个或多个二次幂项，使乘法改由移位与加减实现；此时权重码宽不等于中间乘积宽。输入整数位宽、最大移位量、零值与符号处理共同决定真实 PE，累加还须另留范围。导出也不只是把原浮点值换成指数：若先经过普通 int8 转换，再恢复目标幂次码，必须按原 quantizer 还原码值、修正 weight scale，并同步重定标 bias，最后才 packing 给匹配的 consumer。[PoTAcc 的受限端到端实例](https://arxiv.org/html/2605.06082v1)还把全部权重预置于 DMA buffer，准备时间与持久容量都不能省去；只支持部分算子的 accelerator 会在跨层 CPU 回退与搬运中损失收益，较少乘法不保证更低延迟。CNN 的转换精度也不能给采用合成权重测时的 Transformer 补上质量证书，扣除 idle 的能耗不等全板总能耗。格式、scale/bias 或实际路径未验时，保留普通整数/浮点 kernel，分别验完整任务质量、准备成本和请求执行。 <!-- source-family:SF-2026-ARXIV-2605-06082 -->

拟纯本人note：

> - Daily2026-05-09补May08：2605.06082v1 III-A/IV/V，5分具体格式/执行差额深入；只采PoT码宽-v-intermediate PE宽与scale/bias重新编码合同，保prepare全权重DMA容量/CPUfallback、synthetic Transformer未获CNN质量与idle-subtracted energy边界。未核代码或复现；唯一INFER-TENSORRT-LLM。

## A22 — 两项AR视觉tokenizer必要Source prepared

### 06137 Prologue — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06137v1)实际读§2–4必要机制/评价。共享bidirectional encoder产16辅助prefix与256visual tokens、分codebook；decoder只用visual重建，ARCE经ProbSTE直达prologue不直达visual。共享attention/encoder仍有间接梯度，不称visual完全冻结；只有Post变体冻结整个既有visual路径。训练先compactAR辅助tokenizer，再冻结tokenizer重训fullAR；重建与AR可预测性分工的新分支，不等端到端单阶段总成本更低。

关键理论反侧：条件熵下降不等联合序列更容易，仍须计H(zp)与模型KL；对固定zv，H(zp)−I(zp;zv)=H(zp|zv)非负，§2.1/4.1“只能I增长比H快”与“自然不collapse”不能当形式保证。采用实际gradient-routing/额外prefix方法及有限ImageNet对照，不取全局无collapse或纯因果attention解释。相近rFID的generation改善也有2.15→2.24反退，CFG为两组不同schedule不能混一个更强质量保证。额外16tokens、tokenizer/compactAR/fullAR、STE/dropout与准备预算全计，Post仅Base proof-of-concept，未核实现/复现。拟MULTIMODAL-REPRESENTATION，待Source独核/具体owner。

### 06148 wAR-Tok — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06148v1)实际读§4.4–4.7/5–6必要原域；不采用未读完整TVC theorem/earlier数学推广。auxAR近似当前aggregate token分布，targetAR给先验；两者逐token logprob差经STE作为encoder/quantizer的stopgradient更新提案，与重建目标联合。aux须跟上当前encoder、target须有更好归纳偏好；只有取两次teacher forward的接口不等aux/target不需训练或全链免费。

离散categorical连续化与AR prefix冻结是近似，逐token logprob向量不自动是完整联合AR density的连续梯度；不得称实际实现严格Wasserstein flow或所有proxy误差下仍向target下降。CIFAR matched-rFID与matched-iteration分开，ImageNet单seed且rFID2.05→2.35反退；支持有限reconstruction-v-prior可预测性取舍，不授普适Pareto/绝对SOTA或等质量。不同prior/MIM未测，teacher/aux训练、额外forward、STE与独立质量回归均付费；proxy漂移或质量变差时保固定two-stage tokenizer/普通联合目标。未核代码或复现；拟MULTIMODAL-REPRESENTATION，待独核/owner。

### 当前既成结果同步

root R7已实际通过Falcon/Resi两真实POST（Resi含block-diagonal必要假设差额），两位释放。R8三项必要Source通过；R9已实际接纳05538具体已有覆盖、MiA一段/完整两侧/本人note POST通过，该窄位释放。作者不再重Source/PRE/POST；06137/06148本节与其他prepared仍不预通过。PoT逐字稿仍待PRE，无其他Books写权。

## A23 — 两项World/Action必要Source prepared

### 06298 NOVA — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06298v1)实际§2/3.1–3.3、4.1–4.2/5与AppE spurious部分。state编码成小INR权重offset，叠dataset-shared base并按坐标render；IDM从连续state推latentaction，FDM用A(state)+B(action)分解，再GCM学预测latentaction。render仍是learned非线性网络，不是无任何decoder或物理解析真值。单RTX4080/40M、MovingMNIST/PhyWorld的identity/motion编辑是当前主线证据；WeatherBench应用本次按AIforScience暂缓，不作准入/Books依据。

最小可采边界：weight-space+additive归纳偏好使部分内容/运动可替换，但latentaction仍混brightness/position，PhyWorld换content会带y坐标，非严格disentanglement或可映射真实动作。jointFDM的OOD物理误差更低，additive换的是可编辑性不是更准确物理；action替换本来故意违原质量守恒，不把视频像真当physical valid。原§3训练phase1用MSE+正SSIM记号与最小化意义不闭，不照录loss配方；未给完整先验/OOD guarantees。全encoding/render/IDM/GCM训练与rollout计费，真实control/safety未测，保常规latent/pixel与实际observations回退。未核代码/复现；拟MULTIMODAL-WORLD-MODELS，待非作者核/owner。

### 06222 FFDC-WAM — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06222v1)实际§3–4/A.1。长chunk Motus WAM联合动作与futurevisual，执行期间把真实新observation与原预测/action/instruction交小verifier，低于固定0.5触发replan。保预测与观察不同事实权限，cache只属该计划版本/时段；作者所述futuretoken可attend当前realobs却又一次缓存，需要实现进一步证明更新依赖，不声称所有KV复用精确或任意mask可用。

训练正例来自demonstration/少量成功rollout、负例含failed与人工corruption，后者不是所有真实失败真值；mixture-horizon/padded终止动作不证明校准概率。4A100训WAM/1A100训与测verifier，RoboTwin50tasks×100与Astribot S1两pickplace有限。LC16/32/48/64共享longchunk训练而BaseMotus16，不能将所有差额单归verifier。真实两任务success提高但平均执行28.1s/16calls多于LC16的25.6s/14calls，不能宣总成本/延迟全降。Threshold系统tradeoff未研究，不将confidence称safetycertificate；全WAM与verifier/感知/重规划计费，模态漂移、cache不一致或未覆盖失败时回短chunk闭环/可靠controller。未核实现/复现；拟MULTIMODAL-EMBODIED-VLA，待非作者核/owner。

## A24 — 三机构可执行历史入口恢复与六项日期有限尝试

执行日期仍为2026-10-18 BJT。这里是作者本日实际请求/字段读取，不继承他日响应；只恢复A11明确缺口，不扩全站或已封口arXiv池。以下未有root独核，不能预授完整Coverage。

### Seed：实际返回量、next与跨窗停止

官方JS路由 `GET https://seed.bytedance.com/api/get_article_list_v2`，参数 `article_type=1/2,publish_year=2026,page_token=0/20,count=20,order_desc=true`，请求头 `x-tt-locale: US`。`count=20`是请求上限，不是实际响应数。

- type1/page0：实际18条，`next_page_token='20',has_more=true,total=86`，BaseResp status0；逐条读id/title/PublishDate，实际日期从Sep28至May26，继续有限下一页。
- type1/page20：实际20条，`next_page_token='40',has_more=true,total=86`。本页May16→Apr15跨过May08，故按目标窗口停止，不继续page40。实际May10为1667 Sequential Image Editing/2605.09233；May07为1631 TDDFT（科学应用关闭）和1629 Continuous Latent Diffusion LM/2605.06548；其余May15/14/13/12及May06/04/01和Apr30/26/23/22/20/16/15。本片段没有PublishDate May08。目录当前May10不能继承旧报告May09目录线索；任一目录日均不覆盖arXiv首次公开合证，也不搬原ERNIE日期或扩相邻日论文。
- type2/page0：实际15条，`next_page_token='',has_more=false,total=20`；本响应英语可见行Oct14/Aug05/Jul31/Jul20/Jul08/Jul07/Jun23/Jun19/Apr23/Apr09/Apr01/Feb16/Feb14/Feb13/Feb12，没有May08。next空且false，故不请求type2/page20；total20与实返15差额保留，不冒称两语言/全历史均覆盖。

只对上述实际英语字段切片作阴性判断。type1若后续补入本窗日期、或取得当时归档/其他语言明确原件，只定点重开；不以当前列表证明全站历史无遗漏。

### Qwen：无序40条按extra.date逐项筛

实际 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN`，data仅见articles，无可用next/分页字段；实际40条，不按返回顺序当日期排序。最后一次窄输出逐项读全部40条id/title/extra.date（前两次输出携长内容被工具截断，不作为完整正文阅读）。日期范围2025Nov13→2026Sep20；没有May08。相邻已读日期为Qwen-Scope/id66eb554c-3631-489d-abf4-44b3b65eea06的`2026-04-30T12:00:00+08:00`，与Qwen3.5-LiveTranslate/ide3d5b6b8-3280-461c-b5c9-9a6066c13555的`2026-05-19T17:40:00+08:00`，另Qwen3.7为May20。故恢复的是当前zh-CN这40条日期元数据，不是完整历史/所有语言正文；A11动态空壳不再冒未执行解析，但历史删条/缺分页限制仍隔离。

### Hunyuan：官方公开列表POST的实际英语9条

从页面脚本路由实际公开读取 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，JSON body `{"pageNum":1,"pageSize":100,"renderType":0}`，Content-Type application/json，无凭据。响应code0/success，data.totalNum9，实际9条且全lang=en。实际displayPublishTime分别1790006400/1787846400/1785945600/1784599200/1783440000/1777532400/1776873600/1770971763/1770090898；按BJT为Sep22/Aug28/Aug06/Jul21/Jul08/Apr30/Apr23/Feb13/Feb03。最近跨窗前项id100039“Real life is where context gets hard”为Apr30 15:00 BJT，下一项id100064 Hy3为Jul08；这9条没有May08。只采用原displayPublishTime，不以updatedAt搬日。实际totalNum9/实返9可终止该响应，不替代未知中文列表；未发明语言参数、未授全双语/历史全部覆盖。

### 六具名日期：必要替代入口尝试，仍非确定本窗候选

复用A7/A8已有精确v1、registered与跨日界；不重发arXiv export/API/RSS/OAI。实际重新打开六个具名abs v1，针对已知作者/项目做有限日期恢复：

- 05248：读[mashin.live](https://mashin.live/)及其官方[governance-proofs](https://github.com/mashin-live/governance-proofs)当前原件，公开releases API实际空数组；未得May08带日期全文首公开。当前proof代码与commit时间不证明历史公开日。
- 05220 MidSteer：读[项目](https://github.com/Atmyre/MidSteer)、[作者页](https://atmyre.github.io/)；作者News May01“Two papers are accepted to ICML”当前连MidSteer，但acceptance不等当时全文已公开，七月PMLR发表也不确认May08。releases API实际空数组。[OpenReview具名forum](https://openreview.net/forum?id=9ZWVPbHmhl)返回浏览器挑战，公开notes API `https://api2.openreview.net/notes?id=9ZWVPbHmhl`实际403，停止，不绕过/重试。此项ID原误写06696，现按A35精确身份核回；该repo/forum证据不属于Hidden Coalitions。
- 05225 MACS、05226 Internalizing outcome/process：精确题名+作者/官方域有限检索未恢复具名带日期原始全文或公告。05285 Attribution与06696 Hidden Coalitions在本节原互相错绑，受影响恢复范围及正确原始入口见A35；不以错误串号宣称已完成日期恢复。第三方Submitted/后期收录不能替代首公开。没有把搜索无命中写成全球更早稿不存在。

六项仍缺可把整个可能区间限定为同一BJT May08的官方公告/可复查共同约束，或能确认更早全文的原始发布。不得先给确定候选/分数/Books；拟作为本窗日期保留项，待root核实际恢复范围后决定终态。重开只需其中任一具名的目标公告/官方历史归档、原始带日期全文、或OpenReview已可公开读取且能说明全文公开日的note；不重整个池。

### 已有效层同步

root R10已实际通过06534/05639两项6分与06184/06235/06647三项5分必要Source；这不等具体Books差额或PRE。PoT A21已授窄写并真实保存，root实际读Ch49:1049完整新增、两侧与本人note3171后POST通过、位释放；当前新实际整合六项（Teaching/Balance/Falcon/Resi/MiA/PoT）。A18/A20/A22/A23尚未独核的各项继续prepared，不由本节升级。

## A25 — R10三项Training/Memory具体owner与逐字窄稿（未PRE/未写）

已对读当前ROADMAP、写作上下文及Ch32/34、Ch27/29、Ch53/55交接；不把公共服务化/分层/数据质量原则再算新差额。

### 06534 唯一TRAIN-GRPO Ch33

实际§Rollout变成服务1562起已有policy/group freshness、Relax字段就绪、Tangram行动租约、RLHFless actor迁移；未承载“借用在线serving的虚拟KV/物理页、以两个线上余量让出rollout”的耦合机制。拟接本节首段后、Relax数据总线段前，保其余正文一字不动：

> Rollout 服务也可借用在线推理的暂时空闲资源，但空闲显存不等于可用执行时间。一个受限共服分支为各模型保留独立虚拟 KV 地址域，按需借用共享物理页；线上突发时回收 rollout 页会中止或改派相关生成，不能把原 KV 直接改属另一个模型。计算侧再按当前 TTFT、TPOT 两个余量中更紧的一项，结合 profile 估计，才接纳有限 rollout chunk；仅共享内存仍可能违反 token 间延迟。[ROSE 的有限对照](https://arxiv.org/html/2605.06534v1)用额外借入的 GPU 换更快训练，不证明同 GPU 预算优胜；跨池稀疏权重差额还依赖正确旧版本和 shard，重构不能自行证明逐 bit、原子发布或训练 freshness。页回收、失败重算、压缩/传输及 profile 都要计费，线上 burst、预测或版本失配时，回专用 rollout、静态预留和完整权重快照；完整 group 与 optimizer admission 仍由 trainer 验收。 <!-- source-family:SF-2026-ARXIV-2605-06534 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06534v1§4–6，6分必要Source R10通过；只采独立virtual KV/共享物理页与TTFT/TPOT双余量共服，保abort/reroute、正确旧权重/shard及稀疏失利/额外GPU预算反侧；未核实现/复现，不授同预算、bitwise或SLO保证。唯一TRAIN-GRPO。

### 05639 唯一INFER-GPU-MEMORY Ch54

实际§异构近数据505起已有PIM placement/reduction与host/flash；§Physical Layout595起已有view translation、host-cache/PIM副本及CD-PIM pseudo-bank phase分工。后者明确损的是PIM并行度而非模型容量，故不能用它冒承载vertical stack的计算阵列面积-v-密度容量权衡。拟接CD-PIM完整第二段（“不由模拟加速签发部署保证”）后、“启动路径还需要区分”前一段：

> 器件内部还可以沿容量与计算分域，而不只按 Prefill/Decode 分 bank：高密度层保存更多冷状态，带 PIM 逻辑的层牺牲部分容量换就地计算，base-die controller 按可计算资格与复用共同迁页。热度高不代表任何数据布局都能在 PIM 执行；K 按 token、V 按维度分 bank 可减少各自 reduction，却仍支付广播、垂直链路及跨设备通信。[TokenStack 的模拟分支](https://arxiv.org/html/2605.05639v1)还在冷 KV 下沉时压缩，晋升时反量化并转置；恢复 FP16 容器不等恢复量化前原值。它没有实芯端到端验收，原阈值与驱逐公式又有口径矛盾，故不移植为通用策略；排队膝点的大倍率也不是算子或生产 P99 加速。应共同验收容量损失、搬运、controller、质量与真实负载，硬件不可得、复用不足或净收益不成立时，保留普通 HBM、host offload 与已有 bank 分工。 <!-- source-family:SF-2026-ARXIV-2605-05639 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.05639v1§4–8，6分必要Source R10通过；只采vertical capacity/compute分域、非对称K/V布局与全迁移费用，保K8V4不可逆、层顺序/阈值/negative-reuse驱逐矛盾及模拟非实芯/排队膝点非P99。未核实现或复现；唯一INFER-GPU-MEMORY。

### 06184 唯一TRAIN-PRETRAINING Ch28

实际Mid-training1499起已分原文/structured QA、阶段mixture与非目标回归；首段tool transition提供执行数据资格，但尚无符号执行路径/抽象状态作CPT语料、并把violation与holds和格式人口分开验的分支。拟接2603.27164阶段QA两段后、长上下文NIAH段前一段；Ch27保数据provenance，Ch29保instruction行为，不重复改其正文：

> 定向继续预训练也可把程序的符号执行路径和状态报告作为语言模型语料，而非只增加 raw code 或最终正确答案。此时结构、bug 人口与推理时是否展开 thinking 可能共同改变能力，须固定评测分母，把找到 violation、正确保留 holds、无法解析与超时分开；模型给出二值判断不等于产生可检查的证明。[一组受限 C 程序对照](https://arxiv.org/html/2605.06184v1)中，bug-focused HTML traces 配合 thinking 改善违例发现，却使 holds 从90.7降到78.0；相同文件数的 code-only 也不等 token 或算力控制，较大语料又改变组成，不能归因于“越多越差”或纯语义监督。轨迹生成、格式化、CPT 与额外推理预算均计费，去重未披露就不授无污染；格式、非违例保持或净质量退步时，保留原 code/trace mixture、入口 checkpoint 与独立 formal verifier，不由局部检测收益批准安全审计替代。 <!-- source-family:SF-2026-ARXIV-2605-06184 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06184v1§3–6/Table1，5分Source R10通过；为Ch28 trace-CPT/推理接口差额深入必要原域，采holds/violated与unparsed/timeout固定分母分账，保同文件非等token、组成混杂/单训练与无显式去重，binary非proof。未核实现/weights或复现；唯一TRAIN-PRETRAINING。

## A26 — R10两项RAG具体owner与逐字窄稿（未PRE/未写）

Ch75单调用assembly、Ch77跨调用持久状态职责已对读；两项只修改Ch76检索接口，不重复充分性/来源权限普遍原则。

### 06235 OBLIQ 唯一AGENT-RAG Ch76

实际Ch76单向量域迁移/corpus-size诊断351–356、ARK双轴hard-negative358及reranker固定池147等已说明漏召回不能由精排恢复；尚无给同一reasoning reranker分别喂普通pool与gold-injected pool来定位“找不到但给定后能验”的诊断反事实。拟接2603.29519完整单向量研究段后、ARK段前：

> 对隐含作者风格或潜在属性，能在给定文档后验证关系，不表示能先从大库找出它。可保持同一 query 和 reasoning reranker，分别测真实检索池与注入已标 gold 的诊断池，再观察扩大 pool 或改写能否缩小差额；这把候选发现与给定候选后的验证分开，而不是让 reranker 为缺失文档负责。[OBLIQ 的受限评价](https://arxiv.org/html/2605.06235v1)显示部分改写还会抹去风格线索，多轮更深并非必然恢复；gold 注入只是离线反事实，不是线上可得检索、完备真值或全局可达上界。属性抽取、pool 标注、各路搜索与重排都付费，LLM 标注和 verifier 可共同犯错；因此按关系类型、真实候选覆盖与最终支持分别验收，漏证或改写失真时，保留原 query、lexical/hybrid、显式属性索引或重新取证，不据局部 gap 宣布 dense 无用。 <!-- source-family:SF-2026-ARXIV-2605-06235 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06235v1§3–5，5分Source R10通过；只采retrieval–verification的普通/gold-injected pool反事实诊断与style改写反退，保pool构造/LLM相关标注/不完备gold及全部费用；未核实现或复现。唯一AGENT-RAG。

### 06647 SIRA 唯一AGENT-RAG Ch76

实际Online Retrieval Pipeline173已有dense/lexical/hybrid适用边界，query侧已有多路提案/融合，却未承载双侧扩词如何以当前库DF限定可检索词面、且online必须非零的具体接口。拟接“Dense retrieval 擅长语义相似…Hybrid retrieval常更鲁棒…”段后、query-side distractor段前：

> Lexical 路径也可以在不重训 encoder 的情况下扩展匹配词面：离线为文档生成扩词并建立新索引，在线只提出当前 query 缺失的证据词，再按语料 document frequency 过滤常见词，并排除在线扩词中库内根本不存在的词，与原 query 加权后执行一次 BM25。两侧规则不同，离线新词不能一概要求原库已有；DF 只说明词面存在与稀有，不证明相关或事实正确。[SIRA 的有限对照](https://arxiv.org/html/2605.06647v1)支持这条语料统计约束的提案接口，但未独立拆出各组件因果；一次在线检索也不等无离线生成、索引增长/重建或语言模型调用成本。应保留原 query、扩词及索引版本，分别验召回、答案支持与总预算，不能把 gold answer-string coverage 与他文生成准确率合并。扩词漂移、语料远离模型先验或净费用不合算时，保留原 BM25、dense/hybrid 与独立原文核验。 <!-- source-family:SF-2026-ARXIV-2605-06647 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06647v1§3–4，5分Source R10通过；只采两侧扩词/DF上界与online非零接口，DF非truth，保离线预算/缺组件消融/answer-string非generated accuracy与局部反退；未核实现或复现。唯一AGENT-RAG。

## A27 — R11三项具体owner（VideoRouter拟NC；另两逐字稿未PRE）

### 05848 VideoRouter拟具体已有覆盖：MULTIMODAL-REPRESENTATION Ch23

实际对读Ch23:850–856的固定预算/CLASP类别路由→relevance与coverage两支、926–934的“局部细节问题与跨事件问题”完整段、随后Tempo两份预算及4K/8K非单调反侧，并读Ch22/24交接。现正文已经要求先按问题时间粒度路由、在固定帧预算下分配相关性与事件覆盖，proposal不认证充分性，漏瞬时证据时回均匀/固定或dense；Tempo又明确局部/全局预算分账与非单调。VideoRouter当前5分可采命题是全局覆盖/局部细节的预算取舍和固定帧对照，正由这些实际条件承载。shadow前四层分类器和三阶段训练是这一选择的受限实现，64/128反转及标注mixed-query错误保报告，不因新case和分类器实现另堆同一原则。因此拟5分标准完成/ExistingCoverage；尚待root核具体NC，不降低分数或隐去反侧。

### 05674 EGA唯一AGENT-RAG Ch76逐字稿

实际Ch76:366–369的REZE只以固定reference构造source条件target，515起讨论度量/几何诊断，均未有“零初始化残差适配+有限局部hinge停止压力但累计全局漂移仍存”的机制。拟接REZE完整两段后、Teacher负采样段前一段；不新增一般cosine/索引原则：

> 保留冻结 embedding 之后再训练小残差，也不等于保住所有未见样本的几何。一个受限分支从零残差初始化，在归一化表示上只对未满足 margin 的局部 triplets 继续施压，避免已经分开的样本持续扩大距离；容量与停止条件共同限制适配方向，却不让局部训练变成只影响这些样本。[EGA 的有限对照](https://arxiv.org/html/2605.05674v1)中，参数 Jacobian 的路径积分说明累计漂移仍依赖整条更新路径；它不是 input Lipschitz 或实际 AdamW 的无条件 OOD 保证，方向安全仍是作者 conjecture。ANN 相对当前向量的几何 recall 与语义分类/检索也须分开，部分 Food/CIFAR 切片弱于 frozen，四集最小值不认证任意新域。triplet、margin/容量搜索、训练及索引重编码全计费；原域、未见域或总预算回归时，保留冻结向量、普通适配或较小残差，不由零初始化和训练后少梯度宣称无遗忘。 <!-- source-family:SF-2026-ARXIV-2605-05674 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.05674v1§3–5/A.3–A.4，5分Source R11通过；为局部hinge停止/残差累计漂移差额深入，只采参数路径条件，保ANN-v-semantic、Food/CIFAR反退与conjecture/gradient-flow非AdamW保证。未核实现或复现；唯一AGENT-RAG。

### 05922 DeScore唯一TRAIN-RLHF Ch31逐字稿

实际Ch31:99–111先BT比较人口、再解释+score生成式RM、teacher为已知偏好造理由、最后AdaJudge scalar pooling；已有解释不是真值，却尚未把训练阶段的随机CoT mask与专用Reward-query scalar路径、辅助BT维持排序区分。root指出初稿误把cold-start mask扩为两条已评测部署路径，以下已收窄；拟接2604.28078完整teacher理由段后、AdaJudge scalar-readout段前一段；Ch30/32交接已读，保持RM训练归本章：

> 奖励模型生成解释之后，也可用专用 reward query 读取标量，分别维护文本目标与偏好排序。一个受限分支在冷启训练时随机 mask CoT，让数值读出也学习视觉输入，而不总依赖解释；部署实验仍先生成 thinking、再查询 score，这项训练 mask 不证明可用无解释路径同质替代，也不认证理由忠实。[DeScore 的受限视频对照](https://arxiv.org/html/2605.05922v1)先以解释监督和 Bradley–Terry 冷启，再用生成式 RL 配合辅助 BT，去掉 BT 的反退支持“不让解释奖励独占 scalar 排序”的取舍，而非概率校准或独立因果保证。人类 pair 标签不验证 teacher 每个子维度，motion/artifact 也弱于文本一致性；teacher、CoT、额外读出前向与两阶段训练均计费。解释支持、排序或净费用失配时，保留直接 scalar head、原 BT 与独立人工/grounding 评价，不把 attention 图或更长理由当证据证书。 <!-- source-family:SF-2026-ARXIV-2605-05922 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.05922v1§3–4/I，5分Source R11通过；为cold-start随机CoT mask/Reward query与辅助BT排序差额深入，部署仍think→query→score，保mask非无解释等价/faithfulness/校准、teacher子维度非人真值、tie人口及motion弱项/完整费用。未采用理论附件，未核实现或复现；唯一TRAIN-RLHF。

## A28 — R12两项Multi-agent具体owner逐字稿（未PRE/未写）

实际对读Ch82意见传播/信任→受扰图与邻接prompt的完整局部、Resource Algebra、边协议路由与运行时拓扑修复；Ch81 durable执行/Ch83协议边界已读。两项均只管离线训练/搜索提案，不自授运行权限。

### 05703 Active Task Selection唯一AGENT-MULTI-AGENT Ch82

现2601.04694用任务代理学图并固定图优化邻接prompt，尚未决定小训练预算该查哪些有答案任务。拟接其第二段（“图的资源可行性再由下节另行准入”）后、Resource Algebra heading前一段：

> 图训练预算还可以先分配给哪些任务，而不只优化图本身。在已有答案的 pool 中，用当前图参数 ensemble 的真实执行得分估计任务对更新的不确定性，再以单步 EKI/Gaussian 近似提出信息量较高的训练子集；图的实际学习仍可用 REINFORCE，不能把 selection 近似当作同一个更新器或无标签 EIG。[有限任务选择对照](https://arxiv.org/html/2605.05703v1)还用代表子池与 surrogate 减少 rollout，但缓存只在同一 ensemble 下复用，新增 selection 费用常高于 train 费用。Benign 与部分攻击均值的 CI 跨零，仅部分尾部/任务有明确收益，非 Gaussian 与有限 ensemble 也无全局最优保证。已知答案、代理、任务人口与选择/训练总调用均须绑定，漂移、标签缺失或净收益不成立时，保留随机/代表采样和固定小图，不由高信息量签发真实任务价值或协作安全。 <!-- source-family:SF-2026-ARXIV-2605-05703 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.05703v1§4–6/A.1.3–4/D.2/B.6，5分Source R12通过；为已标task-selection与graph-update分责差额深入，保linear-Gaussian条件、同ensemble缓存/selection费用与benign/attack-MMLU CI跨零；未核实现或复现。唯一AGENT-MULTI-AGENT。

### 06623 MASPO唯一AGENT-MULTI-AGENT Ch82

现图与邻接prompt优化说明要随任务重训，却未有某peer更新后旧beam分数失效的显式refresh及局部/后继/终局分账。拟接上项新段后、同一Resource Algebra heading前一段，两段各唯一marker不合并材料：

> 同一固定拓扑内轮流优化各角色 prompt，还会让评分对象随 peer 改变：上游改写输入后，旧 beam 的高分未必仍成立。一个受限分支按拓扑顺序交替搜索，每轮在当前 peer 版本下重新比较旧候选与当前 best，并把 local validity、直接后继 lookahead 和最终输出的 judge 偏好分开；局部合法但下游无益的 trace 可作为下一轮 hard negative。[MASPO 的有限对照](https://arxiv.org/html/2605.06623v1)支持这个陈旧评分刷新接口，不把 judge preference 认证为因果 credit；一跳更合算也不是普遍充分定律。同一 Gemini judge 参与优化和评价会带共同偏差，50 个未标注任务、两拓扑与单一受测 agent 族不授任意拓扑迁移。候选/peer/judge 版本、trace、搜索与完整 token 成本须共同保存，持出质量或净预算失配时，保留原 prompts、固定图与独立终局验证，而非由局部高分批准运行安全。 <!-- source-family:SF-2026-ARXIV-2605-06623 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06623v1§3–4，5分Source R12通过；为peer版本变化下beam刷新/三层judge分账差额深入，保same calls非全token、共同judge偏差/有限transfer与onehop非普律。未核实现或复现；唯一AGENT-MULTI-AGENT。

### 已发生写后状态

root R13实际核A25/A26当前owner/PRE后授四精确段；作者逐字保存Ch28新1523/本人2002、Ch54新609/本人985、Ch76新173与360/本人1935–1936，自读及限定diff-check通过；root R14已真实完整新增/两侧/本人注POST通过、四位释放。ROSE仍只有PRE，等May08同文件lease释放，不并发写Ch33。新实际整合由六增四为十，仍未DAY。

## A29 — wAR-Tok target更新接口必要反侧补核（不改成单一配方）

root指出score-stopgrad不等跨step冻结，作者实际重新读取[06148精确v1](https://arxiv.org/html/2605.06148v1) Algorithm1完整steps1–8/§4.6及AppendixF.1–F.3相关完整训练细节；不扩未采用TVC定理。step4是score forward无反传，step7明确同时计算target `p_theta` 与proxy `q_psi` CE，step8/后文写联合AdamW更新。因此不能仅凭step4宣称target永久固定。

同时原F.1又明确为避免target适配非AR分布，使用固定的随机初始化causal `p_theta0` 加低temperature；这不是作者推断，而是与Algorithm1 target-CE/联合更新表述的真实冲突。F.1还写AR loss/WGF/reconstruction联合、不交替；F.2及§5.2列tokenizer150epochs、target AR300epochs/独立AR计时，但没有明确解释哪个是引导target、哪个是后训评价AR，不能自行补齐两份同名模型或以ImageNet配置抹去冲突。

可保留的最小层为：当前step读取target/proxy逐token logprob差并经STE作用tokenizer、proxy拟合当前aggregate、重建与可预测性分别验收；不采target跨step固定或联合训练二者之一为已证明全配置。固定随机target-v-可训练target的实际阶段/参数更新策略、附录/算法同名theta分责仍是精确未决；缺少能解释这项冲突的作者勘误/代码或配置时，不写可执行训练recipe，也不继承严格WGF/保证下降。A22原“target给先验”不授固定性，相关口头fixed概述以本更正为准；尚待root核边界/Source处置，未写Books。

## A30 — 三项既有有限线索必要Source prepared

没有新发现池。以下只接A4/A6已有06175/06421/06663具名机制，均未独核/未授Books。

### 06175 VLA-GSE — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06175v1)实际读§3–5、A.1、B受影响Eq19→21/25及D.4计时。SVD主成分给always-on generalized、后续disjoint段给top-k specialized；action head全训，backbone大部冻结。非零初始化以减去shared+专家平均贡献保持expected weight，而非每sample W或输出保持；router对输入有条件，不能把平均weight相同提升为每个输入的函数同一。trace-inverse scale也只是适配初始化分支：B从E[w² trace(ggT…)]拆成E[w²]×E[trace…]，相同routing二阶矩本身不足推出这项分解，需额外独立/条件统计假设；不照录“精确等梯度”定理，isotropic gradient也不能自动排除router/gradient相关。

Qwen3VL4B/OpenVLA-OFT actionMLP、8A100×80kstep/global128，trainable2.51%含actionhead65.62M而非全是adapter；Table2各PEFT约相同参数、独立调参，不等全训练/部署compute。LIBERO-Plus和retention同backbone支持受限适配/保留取舍，LoRA/VLA-GSE仍低于base部分VLM项。消融限Long，aux与scaling收益不证明唯一模块因果。真实PiPER四task×60trial（四扰动×15），不是开放control可靠性；D.4 RTX5080/actionchunk/batch1/120runs，FFT更快，额外expert不是免费推断。SVD、router、balance/scale搜索、训练与部署全计费，保普通LoRA/FFT及独立retention/control验收。未看图像素/核代码/复现；拟TRAIN-LORA，具体owner待核，不把robot案例转Ch26重复适配数学。

### 06421 FREPix — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06421v1)实际§3.1–3.3、4.1–4.2/Table1–3、B、E.4配置/F训练step与G.1 computational。正交Haar把pixel state无损换成低/高频坐标，不是VAE压缩；两组有共同endpoint而不同单调schedule，低频先靠近clean，DiT仅预测低频、detaildecoder读noisy高频+predicted低频，再逆变换。低频不是全部semantic、highfreq也可有关键结构，factorization不是所有自然图像的因果分离。正time-only权重不改无约束population conditional-mean目标，不推出受限低-only f与conditional g精确保全部原flow；未采用D.2复杂度更好/理论全局保证。

ImageNet256/512 class-conditional、50kFID/IS/precision/recall；L420M的40epoch/50Euler无CFG消融与XL674M/320–330epoch/25或100×2CFG分开。path异质对homogeneous FID13.85vs13.94但IS105.6vs107.1反退，joint/refiner对照也有recall反退，不授全指标Pareto或唯一因果。REPA DINOv2与LPIPS VGG监督/双分支、DWT、全部ODE/CFG需付费；230GFLOPs只是单forward，不含采样/CFG和完整训练。硬件/服务SLO未披露不补造；本次仅采用路径/预测职责/权重的分工，不宣端到端部署加速。未核代码/复现；拟MULTIMODAL-GENERATIVE-PARADIGMS，待独核/owner。

### 06663 EMO — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06663v1)实际§3–5必要机制/评价及A.1–A.2、B.2–B.4/C相关原域。训练用整document平均routing给pool，再让每token在pool内top-k；随机pool大小提高不同submodel容量适应，global-DP-batch balancing避免少量doc的microbatch迫使同文分散。弱doc边界不证明真实semantic domain，pool读取整文routing也不自动是逐prefix部署可得，不能搬作任意自回归线上路由。部署另按已给domain的validation聚合选subset，非自动识别未知query domain；selection与finetune共用train+val，测试另分。

1Bactive/14Btotal、128experts/127routed+1shared/k8，1T+50Banneal；共同architecture/mixture对照，fullmodel MC9/Gen5/GSM8K均可略低baseline，不宣无损。MMLU/Pro原样本40/60分、宏均值排除Other，B.3 Other小subset弱于memory-matched从头模型；需将新训练全费与subset部署内存分开。单validation example默认仍含5/8shot demonstrations，不等只需一个无示范文本；validation格式和大小非单调，B.1图口径17/14与主文16/13宏均值不能混算。训练架构/阶段、global统计通信、selection/finetune及重验全费，不由参数减少证明部署latency/SLO/安全。未核代码/图像素或复现；拟MODEL-MOE，待独核/具体owner。

## A31 — R15两Tokenizer具体owner逐字稿（未PRE/未写）

实际对读Ch23共享token space/VideoFlexTok重建-v-下游AR完整两段（354–362），以及码本更新471起与rate/distortion节；现有“易重建不等易预测”尚无下列两个训练接口。Ch22/24交接已读，只接表示训练，不移植Ch24具体sampling算法。May08 Ch23租约root已确认释放；本方仍等PRE和窄授。

### 06137 Prologue唯一MULTIMODAL-REPRESENTATION Ch23

拟接VideoFlexTok完整第二段后、RT-MAE显式属性/残余段前一段：

> 重建与 AR 可预测性还可由不同 token 承担，而不直接让同一视觉码同时接受两种压力。一个受限分支在共享 encoder 内另产少量 prologue codes，AR 目标只通过这些辅助码的直接路径更新，decoder 仍只用原视觉码重建；共享 encoder 的间接梯度却仍能改变视觉表示，不能称整条重建路径冻结。更严格的后置变体才冻结已有视觉路径。[Prologue 的有限对照](https://arxiv.org/html/2605.06137v1)支持这条梯度分工，辅助 prefix 的额外熵与后续 AR 预算仍须计算；条件熵变小不证明联合生成更容易，也没有无坍缩保证。ImageNet 的部分生成收益伴随重建反退，不同 CFG schedule 又改变采样，compact AR、tokenizer、full AR 与额外 prefix 都付费。两侧质量或净预算失配时，保留普通 two-stage codec、原 visual codes 与独立重构/生成验收，不由辅助前缀替全部消费者签字。 <!-- source-family:SF-2026-ARXIV-2605-06137 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06137v1§2–4，5分Source R15通过；只采prologue直接AR梯度与visual重建分工，保共享encoder间接更新、Post才冻结旧路径、H(zp|zv)非负反侧/重建退步/全费。未核实现或复现；唯一MULTIMODAL-REPRESENTATION。

### 06148 wAR-Tok唯一MULTIMODAL-REPRESENTATION Ch23

拟接上项后、同一RT-MAE段前，保两种分支分别归属：

> 另一条分支不添加辅助前缀，而用当前 token 分布的 AR proxy 与目标 AR 的逐位置 log-probability 差，经 stop-gradient 的评分接口和 STE 向 tokenizer 提议更新，同时继续约束重建。Proxy 需要跟上 aggregate token 分布，评分前向不反传也不表示这些模型跨训练 step 永远冻结。[wAR-Tok 的受限机制](https://arxiv.org/html/2605.06148v1)在算法中写 target CE/联合更新，附录又写固定随机 target，阶段与同名模型身份尚未对齐，因此这里不采用任一完整 target 更新配方；离散连续化与冻结 prefix 也不自动实现精确联合 Wasserstein flow 或保证真实 KL 下降。单 seed ImageNet 的生成改善伴随重建退步，proxy/target、额外前向、tokenizer 与后训 AR 全计费。实际更新身份、重建或下游质量未验时，保留普通 two-stage tokenizer/AR 与原联合目标，不凭 score 差或理论名称自签最优。 <!-- source-family:SF-2026-ARXIV-2605-06148 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06148v1§4.4–4.7/5–6与F必要target接口，5分Source R15通过；只采score-difference/STE与proxy追踪，算法联合target CE与F.1固定随机target冲突隔离，不采完整更新recipe/严格WGF保证；保single-seed重建反退与全费。未核TVC全证明/代码或复现；唯一MULTIMODAL-REPRESENTATION。

## A32 — R15 World/Action具体owner逐字稿（未PRE/未写）

### 06298 NOVA唯一MULTIMODAL-WORLD-MODELS Ch25

实际Latent dynamics279起已有普通E/F/D与control-sufficiency、operator-structured391起已分state/action forcing。新差额仅状态对象改为共享INR的小weight offset，以及由此支持编辑但混杂的接口；不重写一般additive/可解释≠causal原则。拟接Latent dynamics首个“reconstruction好不证明…验证”段后、定长链几何段前：

> Latent state 也可以是一份小型坐标 renderer 的参数增量，而不只是一组 feature tokens：共享 base 定义共同图像先验，各帧保存 offset，由同一 learned INR 在坐标上渲染。相邻 offsets 可用于反推 latent action，再用 state 演化与 action forcing 的加性组合推进，尝试交换内容或运动；学到的 renderer 仍是 decoder，latent action 也不是已标定的真实控制量。[NOVA 的有限运动视频对照](https://arxiv.org/html/2605.06298v1)中，action 仍混入亮度/位置，换内容也可能带走坐标；joint predictor 的 OOD 物理误差更低，说明可编辑性不是物理准确性免费增强。故只把 weight-space 状态视作可比较的表示分支，不采用其未闭合 loss 记号或严格 disentanglement 保证。编码/render、IDM/GCM训练与每步生成均计费，长程或真实控制未验时，保留常规 latent/pixel dynamics、短 horizon 和真实观察，不由像真视频批准物理有效或执行安全。 <!-- source-family:SF-2026-ARXIV-2605-06298 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06298v1§2/3.1–3.3/4.1–4.2/5/AppE必要，5分Source R15通过；仅MovingMNIST/PhyWorld的INR-weight state与可编辑性/准确性取舍，不采用WeatherBench科学应用、严格disentanglement或未闭loss。未核实现/复现；唯一MULTIMODAL-WORLD-MODELS。

### 06222 FFDC-WAM唯一MULTIMODAL-EMBODIED-VLA Ch26

实际§World-action model494起分预测/事实与多接口，§Action chunk640起只写较长openloop曝露，§Memoization706起管跨时间完整chunk缓存资格，没有执行中以当前real observation对计划future作小verifier来触发重新规划的分支。拟接Action chunk第一“剩余动作可能已stale”段后、Chronos时间网格段前：

> 较长 chunk 也可以边执行边检查，而不只能固定短周期全部重算：计划时保留预测 future、动作与指令，执行中让小 verifier 对照最新真实 observation，低于配置阈值便重新规划。预测只提供预期，真实新观测才提供偏离证据；verifier 分数不是校准概率，更不是 controller 的安全许可。[FFDC-WAM 的有限对照](https://arxiv.org/html/2605.06222v1)用0.5阈值和部分人工 corruption 负例，不能覆盖所有真实失败；其一次缓存又允许 future tokens 读取更新观测的依赖尚需实现澄清，不授任意 mask 下 KV 精确复用。长 chunk 训练本身与基线不同，真实两任务的成功提高也伴随比短 chunk 更多调用与时间，不能把收益全归 verifier 或宣全费用下降。WAM、verifier、观测与重规划都付费，失配时缩短 chunk、重建计划状态并回真实闭环/独立 controller，不让预测一致代替物理提交。 <!-- source-family:SF-2026-ARXIV-2605-06222 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06222v1§3–4/A.1，5分Source R15通过；只采realobs对照planfuture的小verifier/replan，保0.5配置非safety、corruption非完整失败真值、cache依赖/训练chunk混杂与真机成本反退。未核实现/复现；唯一MULTIMODAL-EMBODIED-VLA。

### 已发生写后同步

root R16已实际ROSE Ch33新增/完整两侧/本人注POST通过，位释放；R17已实际VideoRouter具体NC通过，四逐字稿PRE/窄授后作者保存EGA Ch76:377/本人1943、DeScore Ch31:109/本人1635、ActiveTask Ch82:215/MASPO217及本人1445–1446，R18已非writer实际全部正文/完整邻接与本人注POST通过、四位释放。新实际整合15，另新具体NC三项；本日未DAY，其他prepared不借此通过。

## A33 — R19具体owner（EMO拟NC；另两窄稿未PRE）

### 06663 EMO拟具体已有覆盖：MODEL-MOE Ch21

实际读Ch21:710–730完整“从统计Expert偏好到可部署模块，需要改变Objective”：已逐字承载document identity→共享candidate expert pool→token top-k→global load-balance→domain validation选择versioned部署subset，并说明语义偏好不等faithful模块、selector dataset bias/subset stale/global collective/未知domain fallback与latency非同比。与本次精确v1可采主机制相同，非仅主题关联；random d与few-shot validation敏感是该分支实现/评价条件，保在报告即可，不为参数再加同一原理。故拟5分标准完成/ExistingCoverage；B.3 Other反退、fullmodel弱项和前述训练全费保留，不由NC降分或抹去新验证。Ch20/22交接已读，待root实际核NC。

### 06175 VLA-GSE唯一TRAIN-LORA Ch30

实际Ch30初始化104–117已有非零增量扣残余可精确保初始W；239起共享basis/生成expert，291起implicit专家已有动态gate不能静态merge。未承载input-dependent非零专家只在routing期待下抵消、且路由×梯度相关会破期待分解的边界。拟接2604.17396非零初始化完整第二段后、初始化保留因果段前一段（Ch29/31交接已读）：

> 若非零初始化同时带输入相关 expert routing，扣除一份平均增量就不再保证每个样本都继承原函数。一条受限分支用主奇异方向初始化 always-on shared expert、其余不重叠方向初始化 routed experts，再从基座扣除 shared 与专家平均贡献；只有初始化 routing 对称等条件下才保持平均 weight，输入相关的 weight 与输入相乘后也不能直接推出输出期待相等。[VLA-GSE 的有限适配对照](https://arxiv.org/html/2605.06175v1)还按奇异值规模调整专家 scale，但相同 routing 二阶矩不足以将 routing 与 gradient 的乘积期待拆开，不能据此移植精确等梯度定理。参数预算包含全训 action head，LoRA式保留与机器人控制收益须分别验收；expert路由比同骨干 FFT 更慢，SVD、scale搜索、训练与部署均付费。初始/旧能力或净质量不成立时，保留普通零增量 LoRA、静态专家或经独立回归的 FFT，不把少 trainable 参数与期待补偿当无损控制保证。 <!-- source-family:SF-2026-ARXIV-2605-06175 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06175v1§3–5/B必要Eq19→21/25/D.4，5分Source R19通过；只采SVD共享/路由专家及期待补偿边界，保乘积期待可分缺假设、actionhead预算/retention与部署反侧；未核代码/图像素/复现。唯一TRAIN-LORA。

### 06421 FREPix唯一MULTIMODAL-GENERATIVE-PARADIGMS Ch24

实际Ch24:188–203噪声合同/time-unconditional/latent几何/频谱日程→SCoRe完整局部；已有频谱改变logSNR和重生，不是把同一state两频带分开path与预测职责。拟接2603.19222频谱日程段后、SCoRe“频谱还可以只控制一次生成后的再生”段前一段（Ch23/25交接已读）：

> 频率还可以成为当前生成状态的坐标，而不只调一条全图噪声日程。正交 wavelet 把同一像素状态无损分为低/高频，两支保共同噪声与数据端点，却沿不同单调时钟推进；一个结构预测器先读 noisy 低频，细节预测器再读 noisy 高频和预测的低频，逆变换回图像。无损的是坐标变换，不是学得的频率分工或输出质量，低频也不等全部语义。[FREPix 的有限对照](https://arxiv.org/html/2605.06421v1)将这两份路径与预测职责、正的频带训练权重分开；正权重保无约束 population 目标，不保证受限两支网络仍实现完整目标 flow。低频先行的 FID 改善仍可伴 IS 反退，部分分工对照也损 recall；固定ImageNet/solver/CFG之外不授普遍优胜。双分支、wavelet、teacher/perceptual监督和全部采样步都计费，单forward FLOPs不等完整生成延迟。分解先验、细节或净费用不合用途时，保留联合pixel/latent模型、统一时钟与原sampler，不把可逆表示当端到端无损或免费粗到细。 <!-- source-family:SF-2026-ARXIV-2605-06421 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06421v1§3–4/B/E.4/F训练step/G.1 computational，5分Source R19通过；只采正交state/异质path/显式预测/weight分责，保受限函数类/简化理论、FID-v-IS与recall反侧及单forward非全采样费用。未核全证明/代码/图像素或复现；唯一MULTIMODAL-GENERATIVE-PARADIGMS。

## A34 — 三项既有LLM机制必要Source prepared（未独核）

### 06241 ReasonMaxxer — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.06241v1)实际§2.3/3.1–3.3、4.1–4.2、5.1–5.3、6.1–6.3必要设置/对照、B训练mask与D费用。仅取离线mixed-success题的entropy-gated outcome加权logprob与非decision base-KL接口：一次base采样不等无生成，150题×20rollouts后留50题1000序列，另50validation/τ扫。负advantage项是signed CE，不是有界pairwise contrastive概率损失；门内无KL，clipping advantage/一次epoch并不能形式保证loss有界或不漂移，不能写完整稳定recipe。最终outcome广播到高entropy token也不证明这些token有逐步因果credit。

Table2 shifted非零，与正文“zero/always top5”冲突，不采绝对稀疏比例/全top5；凡逐步把所有argmax分歧替成teacher，同prefix下greedy走teacher轨迹本来由构造可得，随机替换对照不证明RL未学任何新策略。小LoRA复现局部准确率也不证明完整distributional change低维或能力支持不变。共同base公开RL对照不是同数据/compute；Qwen7B落后ORZ等反侧保留，六math/seed42不足普遍推理结论。实跑费用为4RTXPro6000并含rollout/entropy/τ/checkpoint，部分baseline按脚本/模型比例和1.5–2开销估计，非复跑同机TCO。部署普通base+adapter，不把三数量级当普遍成本保证。未核实现/复现；拟TRAIN-GRPO或SFT的唯一目标接口，具体owner待核。

### 05630 TurnGate — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.05630v1)实际§3.1–3.2/4.2、§5.1/5.2局部主观察及5.3跨域段、C.2–C.7/B、D.5/E/F必要边界。受测机制为生成candidate后/交付前，监控已交付history+当前query+candidate；首次BLOCK终止episode。earliest harm-enabling turn由judge估计，train warm-SFT+offline return/clipped目标学习timing，不等单query分类；部署未知latent g。t*取决攻击者prior/评价judge，不能当真实不可逆边界或必然“前面都可安全放行”；C6只用另一模型复核t*和t*−1，不足对无单调Suff的所有更早轮形式证明。

800seeds/每seed最多20rollouts，两technical域；70/15/15 seed分隔，完整history/input受控trainable对照支持turn监督/目标取舍，不把response-blind prompt差额全归RL。指标F1是benign-pass与自定义harmful timing score的harmonicmean，不是普通分类F1；部分OOD类别无改善、未测开放攻击/真实human能力转移。4B理由称轻量未给全路径实时P99保证，postgen gate须候选未向用户泄露才有意义（streaming需缓存是系统推断）。所有assistant生成/guard逐轮history读、APIjudge/数据/FT付费，非redaction/持续block后对话已实现；保layered guard/tool权限/人审。未核代码/复现；拟PLATFORM-SECURITY，待非作者源/owner。

### 05443 SLAM — 2+1+2=5

精确[HTMLv1](https://arxiv.org/html/2605.05443v1)实际§3.1–3.5/4.1–4.3/5限制与D两项组件反侧、F.5–F.12必要校准/身份。contrastive语法对经SAE、SVD方向回到residual，仅新生成token做加法；HMAC/doc身份选方向，最多四candidate以detector早停/最高分fallback，不是一次免费抽样。SVD右向量经positive clipping与Wdec映射后不自动仍正交；hidden改变也会改变后续logits，不采用“完全不改token分布/语义域不变/quality-neutral by construction”的强句。

检测需同模型whitebox前向，no-SAE只省检测器部分；FPR2.3%为同100prompt baseline拟Gaussian尾，非独立human-text跨域FPR保证，raw选择A空集guard未闭不发布完整zscore recipe。Gemma2PT2B/9B、100prompt、自动reward/PPL/grammar/diversity有限，PT→IT质量约−4.1/TPR93–99反退；DIPPER后TPR12/10，不能授paraphrase稳健。EWD是MarkLLM greenbias实现非原distortionfree机制，baseline默认而本法调参/重采样，不称普遍优越；PPLratio近1不证明分布相同。mining/校准、hook、全部candidates和GPU检测全费，单bit无安全/法律归属证明。未核实现/复现；拟PLATFORM-SECURITY，仅白盒watermark carrier/校准取舍待核。

### 已有效层同步

root R20/A31–32四逐字PRE后已实际保存，R22完整新增/两侧/本人注POST通过，Ch23/25/26释放；R21具体EMO NC与A33两稿PRE后已保存，R23 Ch30/24实际POST通过，两位释放。当前新实际整合21、具体NC四项；新增来源A34仍prepared，不借前批通过。README尚需同步后到有效家族，日级验收未开始。

## A35 — A24三项日期身份错绑的精确纠正（待root核，不倒重有效层）

root发现A24把三项ID/题名串位。本次只重开该集合，实际重新读取下列精确abs v1的title/authors/history；A4/A6原身份是正确的，未修改其v1/registered原字段，也不撤销其他有效Source/PRE/POST。

- [06696v1](https://arxiv.org/abs/2605.06696v1)是Hidden Coalitions in Multi-Agent AI: A Spectral Diagnostic from Internal Representations，Cameron Berg/Susan L. Schneider/Mark M. Bailey；唯一v1为`2026-05-04T16:59:08Z`。正确作者机构[research索引](https://reciprocalresearch.org/research)实际Published Work与Prosocial Cognition均连此题名及同arXiv，但无逐项发布日期。精确v1 HTML作者/链接栏未恢复带日期project/code入口；精确题名+作者有限补检仅恢复arXiv、该机构页和第三方索引。第三方May12收录或搜索Submitted不能把公告定为May08；未将它与MidSteer repo/forum混用。
- [05220v1](https://arxiv.org/abs/2605.05220v1)是MidSteer: Optimal Affine Framework for Steering Generative Models，Tatiana Gaintseva等七人；v1为`2026-04-17T19:23:33Z`，后v2May29/v3June05不代替首公开。实际[作者页](https://atmyre.github.io/)Selected Publications将题名/作者/ICML2026与[Atmyre/MidSteer](https://github.com/Atmyre/MidSteer)联结，repo Citation实际URL为`https://arxiv.org/abs/2605.05220`。May01是acceptance news，不是明确全文首次公开日期。A24已取得的release空数组及OpenReview9ZWVPbHmhl挑战/notes403只归此ID，不重复请求或绕过。
- [05285v1](https://arxiv.org/abs/2605.05285v1)是Attribution-Guided Continual Learning for Large Language Models，Yazheng Liu/Yuxuan Wan/Rui Xu/Xi Zhang/Sihong Xie/Hui Xiong；v1为`2026-05-06T17:38:13Z`，v2July13。精确v1 HTML作者/链接栏和精确题名+首作者+github有限补检未恢复具名带日期作者稿/项目公告；HTML中的GitHub仅arXiv渲染反馈链接，不能冒代码仓。没有把Hidden Coalitions机构索引证据归到本项，也不以无命中证明更早稿不存在。

本次新增读取仅支持正确身份及有限恢复范围，不证明三项May08首次公开或技术证据完成。六日期资格仍不进入确定候选/评分/Books，待root核正确身份绑定与当前可用入口后裁其本窗保留边界；不因此重查另三项或扩旧池。

## A36 — 三项既有Representation/Retrieval/Eval必要Source prepared

只接A6已有05927/06132/06283，不扩发现；当窗日期/current身份沿A7/A8有效层。以下作者已读的必要域不等独核通过。

### 05927 TextPro-SLM — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.05927v1)§3–4/Tables1–5、A、B输入/重建接口、C/D、E文字范围与F蒸馏接口。Whisper decoder16层提供与Whisper token对齐的声学状态，ASR CE+mel reconstruction保声学；下游重新用Qwen tokenizer，故N≠T，不是逐token跨词表严格对齐。默认平均pool为单prosody prefix，interleave只是按LLM长度重新分组的替代；重建压力不证明semantic/prosody独立因果解耦。Frozen-projector阶段再jointLLM，两阶段CE/文本teacher监督；F另比较KL/clean-v-ASR条件，不能混为主配置唯一KL recipe。

Qwen2.5-3/7B、六text-output QA和四paralinguistic为局部证据；7B gap0.7平均含负gap抵消，逐task仍正gap，VoxEval512token的college gap10.8。ASR-only+Qwen也有79.7，KD去除反退13.3gap，但改了训练目标，不能把全部收益归prosody。WhisperPro约1000h与LLM989.6h分列，还继承大规模ASR预训练/文本模型；非从零1000h全成本。5:1 emotion弱于默认、默认emotion/gender弱于部分baseline。C的50run是probe交叉验证非50次系统训练。A明确无speech synthesis/非streaming、用户说完才跑encoder，长段/一般audio/情绪动态未证；训练/ASR解码/TTS造数据/teacher/额外prefix全费，未披露硬件/交互SLO不补造。未核代码/图像素/复现；拟Ch23输入表示分责，owner实际差额待核。

### 06132 MemReranker — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06132v1)§3–4/Table4–10、A hardcase、B原prompt及C各类别。Teacher pairwise/majority→BT相对分数→归一soft-label，pointwise BCE后InfoNCE与instruction/history组合是受限pipeline；BT偏好只定相对效用、归一[0,1]和sigmoid不自行认证跨query概率校准/统一threshold。文中无组件消融或heldout reliability/ECE检验证明该校准，不能把BCE/InfoNCE/多teacher各自因果或最佳配方照录；历史由LLM压缩可能丢信息，positive取当前answer也不认证真实长期记忆。

LOCOMO固定BGE-M3 Top100、LongMemEval Top50仅验候选内ranking，非端到端QA/全召回或memory lifecycle；无显式去重/任务heldout说明不授无污染。8A800/3epoch/8192训练与teacher/合成/hardnegative/search全费，LLMAPI失败19/500被跳过使GPT分母不同。LOCOMO temporal/multihop不全胜Gemini；LongMem R@20也非4B全赢，与文字allmetrics相反；hardcase由Opus造100项，CMedQAv2弱于BGE/原Qwen，非全面域迁移。Table10均值247.2vs241ms不支持caption“3×BGE”；硬件/precision/batch/concurrency/SLO缺披露，listwise JSON排序prompt又与正文pointwise描述不一致，不采精确8×/10–20%部署比。未核实现/权重或复现；拟Ch76 rerank score/selection，具体owner待核，不因memory题名改Ch77生命周期。

### 06283 Rubric modifications — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06283v1)§3–7/Tables1–2、A.1/2受影响比较。两autorater、AES三prompt/IF50instructions×5generations/三expert，固定原human标签、仅改机器rubric；example/context/separate调用组合改善一些agreement，不是所有逐组件因果。Human原rubric不必逐字机器同形，但measurement construct需一致；AES ASAP/++ criterion已不同，故不能把holistic-v-analytic差额全归分解。Kendall含ties/概率加权模型score，AES Pareto与IF yes-ratio是不同aggregation；更高selfagreement不是human validity或无偏真值，Pareto也不是已证明普适lowerbound。

1000bootstrap与三条件Bonferroni只支持作者这些比较，不补普遍multiplicity/独立样本保证。Analytic不稳定胜holistic、IF batch弱且separate较好；GPT/Llama编辑方向不同，增加例子亦非总显著。既有human annotation训练/情境混杂、英语两域两模型，不能外推所有语言/任务；分criteria多API、标注/代表例挑选、概率读出与重验均计费。未核实现/复现，拟Ch66 evaluator合同；是否已有相同条件先实际对读，再NC或窄增量。

## A37 — 三项既有Kernel/SD/SAE必要Source prepared

### 06485 Litespark — 2+1+2=5（数字与整数路径争议隔离）

实际读[精确v1](https://arxiv.org/html/2605.06485v1)§4–7与AppendixA完整必要域。只支持天然ternary权重选择int8执行容器来免逐次unpack、rowwise activation quantize/int32 accumulate/rescale及平台dispatch；SDOT/VNNI仍为硬件integer dot product，不能称无任何乘法硬件。x86 VPDPBUSD为unsigned×signed接口，而正文只写symmetric signed activation/事后zero-point，没有完整unsigned offset构造，不自补可执行精确kernel。更严重§4.1.1把2B×int8宣556MB，明显与约2GB最小原权重容器矛盾，padding不能缩至556；peakRSS/14×/L3-fitting不采用，待artifact实际storage/常驻集合说明。

单BitNet2B4T，M4与x86、主文FP32 PyTorchvsINT8且prompt/batch/concurrency不全；A pp128+tg128与threads固定的BitNet.cppV2：AMD prefill反而V2更快，decode近同，ARM无V2对照，不继承52×为ternary后端普遍优胜。0.68logit最大差不能证明同分布/所有token相同；“hundreds identical”缺任务/seed/质量人口。离线conversion/scale、特性检查、padding、KV和quality全费；未核仓库/安装/复现。拟Ch49格式-v-execution容器窄机制或已有覆盖，不用争议数字支持性能/质量/容量，Source裁决待root。

### 06597 UniSD — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06597v1)§2–3.5、Algorithm1、B成本、C配置及G。Auxiliary views是同一teacher不同任务保持context，只给主target信号估disagreement weight，不等多个独立teacher投票或truth；EMA随step平滑主target，token/sequence粒度有稳定-v-适应取舍。Hard scalar min(divergence,κ)是已reduce-vocab后的token loss cap，超阈值常规梯度为零，不是全梯度范数裁剪或自动只剪stylistic token；denominator和权重仍须有定义。对比正负context可含标注答案/错解，没更强teacher不等无外部监督。

Qwen2.5-7B主消融/另五模型、LoRA r64/1epoch/bf16/3072+1024/vLLM T.7；6A100，evalgreedy code10s/工具exact-name+args非真实执行。MoreK非单调，full组合不是各task全胜/完备factorial同预算因果，15/18改善仍1OOD退步。base-scored sampled PPL低可来自低熵常见输出，不是distribution距离或旧能力无损，单轨迹JSD/最终答案也不认证长horizon。Agreement约100minvsSFT18.6、完整组合token-normalized吞吐更低；TDP/u/PUE能耗是估算非meter。检索上下文/额外teacher passes/negative和配置搜索/rollout全费。未核代码/图像素/复现；拟Ch29 teacher条件/可靠性取舍，owner待实际比较。

### 05341 AEN-SAE — 2+1+2=5（oracle/实现对应不外推）

实际读[精确v1](https://arxiv.org/html/2605.05341v1)§2–5/Tables1–4、A.1 Theorem2完整证明、A.2–3必要假设/证明、B验证/C死特征定义。固定D和固定非负weights时l2使精确nonnegative sparse-code问题强凸，Theorem2的Lipschitz界有该域；不自动成为同时训D/浅ReLU encoder的收敛、连续可微或无死特征保证。Overcomplete本身不推出IRC必坏、所有l1 map必不连续；support切换不等code必跳。A1信号下界/A2 EMA收敛oracle期待/A3活跃penalty消失而非活跃发散及精确argmin是oracle结论条件，实作clip[wmin,wmax]/固定lambda并未达到该渐近，不把有限“很小/很大”当极限。

§3权重随EMA活跃度减小、会压早期不活跃并需warmup；§4.2/4.3却说“更罚高活跃”相反，保持此实现解释争议，不照录反向recipe。Pythia3seed/Layer3、LlamaLayer16/32×/约400Mtokens，所有baseline也禁aux/resampling，非最佳TopK全域；matched target不全matched achieved l0。Pythia~16时AEN死特征更多，Llama减少dead却明显降EV、仍39–55%dead。10ksteps-window inactivity非语义无用，未做人类解释评估，不授monosemantic/causal；encoder/EMA/稀疏lambda搜索/patching全费，<0.1%FLOPs非完整runtime证明。未核代码/复现，拟表示/SAE现owner对读，争议中心不作普遍训练保证。

## A38 — R24三项具体owner与逐字窄稿（未PRE/未写）

本次实际重读Books公共写作上下文、ROADMAP与Ch32/34、Ch71/73职责；只提下面三个精确位，不改共享正文或注释。Source R24有效，六日期R25终态资格隔离另责，不冒Source完成。

### 06241 ReasonMaxxer唯一TRAIN-GRPO Ch33

实际Ch33:1788–1794完整selective eligibility→EG-GRPO邻接已有低/高熵mask、KL保留和entropy非causal，却未承载“离线基座混合成功轨迹的signed CE可作为昂贵online RL之前的替代基线”。Ch29:668–690是student rollout teacher条件目标/方向，本项不将teacher-forcing替换探针写成蒸馏理论。拟接EG-GRPO完整段后、Typed Trajectory heading前一段：

> 若目标只是在基座已有的成功与失败延续之间重分配概率，昂贵在线 RL 之前还可加入一个更便宜的离线基线：先冻结采样人口，用可核终局结果给轨迹有符号权重，仅在高熵位置优化 signed cross-entropy，其他位置保留基座约束。[ReasonMaxxer 的有限数学对照](https://arxiv.org/html/2605.06241v1)支持这种局部替代，但高熵位置仍不是因果决策真值，轨迹级结果广播也没有逐 token credit；负权 CE 无下界，裁权和少量训练不等普遍稳定。基座采样、全概率/熵计算、阈值与 checkpoint 搜索都计费，训练后的分布变化并非严格为零；把所有分歧都替换成 teacher token 的探针又会按构造靠近 teacher，不能由此断言 RL 没有学习或全部效果只是模式放大。支持不足、偏好反转或旧能力回归时，保留 verified SFT、普通 outcome RL 和独立 held-out 校验，不将小离线实验签作在线探索的通用替代。 <!-- source-family:SF-2026-ARXIV-2605-06241 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.06241v1§2.3/3–6/B/D必要，5分Source R24通过；只采offline mixed-support/highentropy signedCE替代基线，保negativeCE无界/终局广播非causal、Table2 shifted非零与teacherreplacement构造反侧/全部采样搜索费。未核实现或复现；唯一TRAIN-GRPO。

### 05630 TurnGate唯一PLATFORM-SECURITY Ch72

实际Ch72:938–987已以run保存turn/stop与最终outcome，1032–1082/1110–1136已有monitor时机/真实effect gate及完整exchange；782 response/prompt分责。仍无以候选回复条件化的turn guard，训练“放行早期正常turn/临界前拒绝”并区分经验sufficiency边界的分支。拟接Learned Security Sensor heading前、2604.06840训练stop边界两段之后一段：

> 多轮防护也可在本轮回复已经生成、尚未交付时，把完整历史、当前请求和候选回复共同交给 turn guard，而不只从当前 query 猜下一步风险。训练可把过早拒绝的良性损失与接近危险完成时的漏放分开，学习何时停止；第一次 BLOCK 结束所测 episode，并不是删掉某个 span 后继续运行。[TurnGate 的有限对照](https://arxiv.org/html/2605.05630v1)用经验标注的充分性 turn 定位这个取舍，该标注并非真实不可逆伤害的首时刻，自定义 timing/benign-pass 汇总分也不是普通分类 F1。已测两技术域和跨域反退不授开放攻击覆盖；guard 还消费完整候选、生成和训练/标注费用，轻量参数不等流式低延迟。工程上须在判定前缓冲未授权输出，这是接口要求而非论文已测流式保证；若内容已经发出就不能追回。边界标签、状态或分布失配时，保留固定 output 检查、保守拒绝和独立 effect gate，不让 guard 的放行获得工具权限或安全证明。 <!-- source-family:SF-2026-ARXIV-2605-05630 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.05630v1§3–5/B/C/D.5/E/F必要，5分Source R24通过；只采response-conditioned pre-delivery turnguard/经验t*分账，保首BLOCK终止、非真first-harm/普通F1、OOD反退与全部费用，缓冲为工程推断。未核实现/复现或生产流式SLO；唯一PLATFORM-SECURITY。

### 05443 SLAM唯一PLATFORM-SECURITY Ch72

实际Ch72:261–271完整Gumbel detector→重写→签名→trace训练取证，已有null/费用与sensor权限，却没有把来源bit载到SAE所选结构方向、以白盒重放同层读出这条carrier替代。拟接2512.16904重写水印完整段后、soundness/unforgeability段前一段：

> 文本来源信号也可以不直接偏置下一 token 的绿色词表，而由白盒模型在选定层的结构相关方向上注入扰动，再用同一模型重放文本读取该层来检测。方向可由 SAE 特征对照筛选后投回 residual 空间，key 与文档身份决定所用方向子集；这改变 carrier 和检测权限，不是让表示中的结构变成来源真值。[SLAM 的受限实验](https://arxiv.org/html/2605.05443v1)中，裁剪和 decoder 投影不保持最初正交性，hidden-state 改动仍会改变后续 logits，近似不变的困惑度不证明原分布或内容无损。最多四候选的选择、特征挖掘、白盒注入/重放与校准都付费；同 prompt 生成基线拟合的低误报不替代独立人类文本或未知域校准，paraphrase 也有明显漏检。模型/层/SAE/key 或变换变化时应重新验效用与检测，权限不足或误报不可控时保留 Unknown、普通统计 detector 与签名 origin/provenance，不将检出升级为授权违规、法律所有权或抗移除保证。 <!-- source-family:SF-2026-ARXIV-2605-05443 -->

拟本人纯note：

> - Daily2026-05-09补May08：2605.05443v1§3–5/D/F必要，5分Source R24通过；只采SAE结构carrier与whitebox重放分责，保clip/projection非正交、logits改变/同prompt null非humanFPR、四候选全费和DIPPER/PT→IT反侧。未核实现/复现；唯一PLATFORM-SECURITY。

## A39 — 三项既有Safety/Representation/RL必要Source prepared

### 06390 Automated Safety is Harder Than You Think — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06390v1)§2–5必要完整论证。设想non-scheming研究代理逐代为nextagent产overall safety assessment；可测proxy→真实安全语义、单报告错误→正确报告的相关不确定聚合是两独立失效层。Approval优化可选择reviewer盲点，shared model/data/reviewer/研究前提可共错，研究量增加并不自动增独立证据；少选关键论文只是把风险转给selection judgment。代理非人类错误/不可人工评价论证/研究volume是条件风险链，不是已观测代理比人类更差的事故或定量证明。

Generalization须分别假设proxy↔truetask耦合、跨部署耦合保持和表现转移；scalable decomposition仍可能留下fuzzy judgment及相关概率重组。原文承认若子问题更易评就仍有用，不能写所有debate/oversight无效；Bayesian belief network为建议非已验证解法。本文概念分析无benchmark或风险率，不能靠机构把假设当已证，也不机械因无实验排除这两层接口反证。新增依赖记录/独立复核/selection与judge成本为本方设计推断，不称作者实现。拟Ch66证据聚合或Ch72安全case，先现owner唯一定位/NC；未核外部引用全原件，只采用本论证明确前提。

### 06095 Metonymy vision — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06095v1)§3–6/Tables1–3、A训练、F/G必要反侧。Late mask在全图backbone后pool不能撤销已混入的其他part；early分组prefix/patch并全层hard attention隔离阻断跨组值路径，STE只让backward借soft分支，不把soft forward当zero leakage。PS为匹配-v-非匹配part的attribute mAP差，低PS也可来自真实属性相关；MPPO只要求非空交，并非mask IoU/因果faithfulness。Stage1 mask由整图产生，条件在既定mask的value隔离不证明全系统输入信息独立/全局零泄漏，ensemble再引global分支更不能继承纯local承诺。

CUB/CelebA支持这份表示接口反证；CheXpert只作同篇机制的评价边界，非医学应用新增知识。STE partmetric更好不等全task质量更高，Stage2-only在CelebA等accuracy退步；global/local ensemble恢复accuracy但职责混回。RTX3090/batch1/224测双阶段143vs310im/s且GFLOPs增，非免费解释；mask发现/两backbone/属性训练/标注与GT分配全费。Part labels、keypoint merge和mask空间改变会改变指标，不照录“early为普遍上界”或所有attention不可信。未核图像素/代码/复现，拟Ch23表示局部性与mask位置，具体owner待核。

### 06094 VISD — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06094v1)§3–4/Tables1–7、B、C.1–3/Alg1/Table8、D.1/D.4及E.3–4/G必要。Verifier按任务支持的answer/format/grounding求rollout advantage；GPT5.4 judge只提供hidden answer/evidence/feedback给EMA teacher重放同student completion，无新teacher answer或额外KD loss。G明确judge不直接看原video frames，只用文本/可用grounding，故不认证逐帧视觉错误真值。Teacher top16并sampletoken的共同支持上两分布各自归一，logratio含supportmass校准项，不是全词表ratio或因果credit；detach的正weight[.8,1.2]、λ0.5→600step归零只保A的符号，不保全部参数梯度方向/无偏原目标或过程忠实。

同SFT Qwen2.5VL7B、STGR-CoT30k/RL36k、16A100/ZeRO3/bf16/G4/16384+768、student1200step对>2300baseline非同walltime，teacher/judge/重放/支持处理与全部SFT/RL付费。Table5 EMA gradnorm不低于current/no-feedback，部分topK与teacher消融切片退步，最终100step平均非多训练seed；VSTAR Qwen72B评answer、16frame-v-other64frame分开，IoU/ROUGE非reasoning faithful或实际工具成功。2×steps不授总费减半，有限视频bench非开放交互可靠性。未核代码/图像素/复现，拟Ch33 verifier方向-v-teacher幅度，先现owner实际比较；不把video case重复写Ch23。

## A40 — 最后三项既有预训练/采样/RL必要Source prepared

### 06546 Token Superposition — 2+1+2=5

实际读[精确v1 PDF](https://arxiv.org/pdf/2605.06546v1)§3–7、A代码、C目标推导、D加权及E/Table3必要反退；已实际渲染并读页4/5/6/9/10/20，核公式、主表及扩展表，不只文本抽取。连续不重叠s-gram embedding平均→单head预测下一bag，各位置CE平均；标签在已有NTP偏移上再移s−1。重复词按出现位置参与，不是不同词均匀；减log s常数的KL解释仅在无重复等条件成立，不转成一般零loss声明。Bag内次序丢失，不能直接当正常AR采样，r比例粗粒度预训练后完整恢复NTP且保embedding/head；重置两者反退支持接口连续性但不证明唯一因果解释。

TorchTitan/FSDP，8或64B200；270M/600M/3B dense DCLM、10B-A1B MoE FineWebEdu/DCLM，Llama3词表/untied head。为同latent长度/作者等FLOPs提高原始sequence s倍，换更多data消费，不是免费同数据加速。3B主表s6/r.3：247对443B200-h达到相近final loss，但同105B data的622h baseline loss更低；Figure3写s8与表s6冲突，精确plot配置不采用。E表BoolQ/ARC-C/Winogrande及MoE OpenBookQA有反退，不称全task优胜。小模型LR sweep不等大模型全调，未多相同run；§7明确compute-bound假设、data-bound/longcontext未测。Bag/r/全恢复/数据与搜索费均计入，拟Ch28粗到细objective接口，未核仓库或复现。

### 05387 Conditional Diffusion — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.05387v1)§2 Lemma2完整分解、§3/Algorithm1完整BAOAB、§4/Tables1–3、§5假设及Theorems4/9/11声明、A后半MMSE分解、B初始化定义与D完整VP/DDPM推导。无噪声满行秩线性测量给normal投影；Gaussian noising下normal score可解析，tangent仍需条件分布，拿unconditional tangent替代不因满足测量就无偏。先固定正确noisy normal切片跑projected BAOAB，再normal修正+逆过程；有限K混合并非exact conditional，slice极限也是给noisy normal的unconditional law，不消原条件错配。

256²预训练prior、CelebA-HQ/LSUNChurch/ImageNet，固定/逐图确定随机mask与8×mean-downsample；随机和SR各1000图，LPIPS/FID不证明posterior coverage或真值唯一恢复。作者以缓存score宣称50BAOAB+50DDIM对100DDIM同100有效NFE，非实测同walltime；hardware/precision/batch/置信区间Not Disclosed，混合/投影/cache与全部先验训练仍费。§5是理想连续/精确score、平均B及t0终点；更强初始化/指数界另需Gaussian mixture、有限entropy、KL敏感性和code间隔，不覆盖任意learned score、有限BAOAB离散误差/任意非线性噪声测量。采用normal可行性≠tangent质量这一最小机制，不采用未完整逐证的KL保证；拟Ch24条件采样owner。

### 06638 ScaleLogic — 2+1+2=5

实际读[精确v1](https://arxiv.org/html/2605.06638v1)§3–5、A/C/D构造、E shortcut/Z3、F训练/课程、H.1–5及I.1–5/Tables4–8必要反侧。反向生成唯一可证candidate树，其他破坏一axiom；fresh predicate/打乱与每配置1000题Z3审计支持有限标签可靠，不证明所有shortcut/生成实现完备。Qwen3-4B/8B nonthinking、verl/DAPO，8B200，G8/8192、binary answer+format reward。主T是验证1000题首次90% Pass@1的RL step数；H.3另列全部rollout token/FLOPs估计/GPU-h，不能混称同一指数：quantification step2.60但FLOPs3.12。主单seed拟合SE不是多训练seedCI，三seed仅conjunction分布/算法实验；H.5两entity的D6/8/10反侧不分离全部quantifier+reuse混杂。

更丰富逻辑/课程在已测范围改变样本效率和迁移；固定D对照最简单setting实用D16而非12，约100step也非等token，不能独因果归expressiveness。八bench为Avg@8非Pass@8，分任务/深度可反退，最大quantification平均增益非所有问题改善；OOD给32768输出预算，约3倍训练depth回随机，非无界算法推理。有限深度log-log与AIC偏好不证明普遍多项式律/排除指数困难，70%课程门槛为配置非通用；val频读及生成过滤/全部训练费用保留。拟Ch33任务结构与课程边界，未核代码/复现或图像素。

## A41 — R26两项具体已有覆盖prepared

**06132 MemReranker → `AGENT-RAG` / Ch76，具体NC待reader。** 实读Ch76「Reranking与Context Packing」首段至完整offline utility/UAE两段及后续history-feedback、共享encoder两段，及「Retrieval基本度量」trace-conditioned/AgentIR完整两段、Ch75/77开篇职责。Ch76现有「若检索器只学语义相似…离线训练」段已明确teacher→成对排序utility proxy→soft utility分布蒸馏embedding、线上ANN不是正确/支持概率；其下一段保teacher/参考答案/negative/索引与最终生成费用、consumer失配回普通reranker。更下history段已保存consumer/曝光历史不等文档独立效用，固定池排序与真实召回/最终答案分测。MemReranker换成对话历史候选与BT归一+BCE→InfoNCE未新增可采用的独立校准证据或生命周期权限，强absolute-label最佳性亦无独立消融，不把这一实例再写一遍。通用相对尺度owner Ch66「Judge Ranking」现有Query内BT不能直接跨query同单位两段与member-scale不可识别段已经承载评分边界；不在Ch76重复测量推导，也不写Ch77的持久真值。5分仍是这份新验证的证据贡献，不因NC降分；A36/R26反侧留报告。

**06283 Rubrics → `PLATFORM-EVALUATION-SYSTEM` / Ch66，具体NC待reader。** 实读Ch66:510–526的criterion测量/调用粒度→ARTS层级→meta-eval条件人口/聚合→跨query刻度完整邻接，以及1537–1555可靠性→generator×reader×domain→四维profile完整局部。现有「输出包含多个约束」已分开每criterion verdict、整表-v-逐条调用、理由协议与最终allpass/平均聚合；「Rubric的层级」要求独立responses校准、区分/跨judge一致/冗余且不因更复杂更正确；「当rubric也由模型生成」已经冻结name/description/scale/instruction、示例人口，明确同reader自一致、跨reader迁移、外部human/task效度三者不可互签，并保全调用成本和人工/Unknown回退。本篇两个英语域/两模型的analytic-v-holistic及表面edit反例是这条具体合同的新验证，不证明更一般构念结论，也不另增同义段。保ASAP/++criteria混杂、例子/调用预算、概率读出/Pareto与统计界；5分不变。邻章Ch65资源调度与Ch67观测不接管测量责任，复用已读ROADMAP交接。

## A42 — 三项具体已有覆盖prepared

**06485 Litespark → `INFER-TENSORRT-LLM` / Ch49 NC待reader。** 实读Ch49:1032–1052低位格式/scale/zero-point/PoT→粒度及1138–1167完整weight-only成本→三值pack→LUT分支；另67–78冷启动转换/兼容/回退、Ch48/50开篇交接。1138起已有artifact/resident/dequant与真实时延分账，1157起「同一低精度数值域也可以选择不同物理打包」明确紧码省存储但decode更慢，较宽码与实际consumer必须联合验，完整驻留/转换/workspace/质量另计，布局不适配回较宽码/成熟路径。Litespark的int8容器绕2bit unpack与int32积累是这条已承担条件的新CPU实例，R29已隔离的556MB/14×/unsigned未闭recipe不能提供额外正面差额；不据此降分或关闭材料。5分新验证保报告，正文不重复CPU案例。

**06094 VISD → `TRAIN-GRPO` / Ch33 NC待reader。** 实读Ch33:918–942完整DPVG→「Verifier拥有方向，Privileged Teacher最多调节幅度」→negative reset→expert-prefix分流及Ch32/34开篇职责。现有两段已逐字承担binary verifier为authority、严格正受限multiplier只保sampled-token sign、不保参数轨迹/真实causalcredit，teacher bias/forward/normalization/leakage费与teacher不可靠回sequence verifier。VISD换成视觉/evidence feedback、EMA和top16 conditional支持，是新受限验证，不增加teacher的真值/全帧观看权；R30已限定judge不见原frames、parameter gradient不保、step非总费。无需为video实例加同义段，也不把negative-reset分支误称本论文执行。5分保持。

**06390 Automated Safety → `PLATFORM-EVALUATION-SYSTEM` / Ch66 NC待reader。** 实读Ch66「从目标到证据」120–151链路/EvalSpec、上述1537–1555构念效度，以及1643–1658 active judge/邻题/expanded panel/AuditBench完整局部。目标风险→spec→scorer→aggregation/uncertainty→decision已经分层；1539–1543明确自身一致不等外部gold/构念效度；1651邻题段明确shared模型构题/求解共同盲区与开放正确性Unknown，1653 panel段明确评分稳定不等独立问题发现、原意见数不等去重覆盖、相关错误与审阅成本。本文non-scheming条件的proxy解释与跨报告相关聚合不能只因更多自动研究就消失，恰是这些现有分责的条件概念反证，不新增经过验证的融合算法或事故率。保容易子任务仍可分解、BBN仅建议、选择关键论文也需审阅；5分新理论视角保报告，不扩写成所有自动安全研究不可能。Ch72消费安全/权限边界，不复制本章测量链。

## A43 — 三份表示/稀疏码逐字窄稿prepared（未PRE/未写）

已实读Ch23语义anchor完整四段及前后S2R交接、阶段二f-CBM完整两段→multilingual map两段，以及Ch5 sparsemax完整两段→external-consistency两段；Ch22/24与Ch4/6职责按ROADMAP和实际开篇对读。具体差额不是声学重要/解释不是真值的一般原则，而是双目标输入流、mask的生效位置、固定优化码的稳定性对象。

### 05927 TextPro → `MULTIMODAL-REPRESENTATION` / Ch23

插入「语义锚点不是原模态的替代品」结构化target费用段之后、S2R「转录作为中间接口」之前，保旧段。逐字拟文：

保留非词面信息还可以在输入表示内部另设训练责任，而不只增加输出字段：从语音识别器的decoder states读取内容流，另让声学encoder的表示经重构目标学习可供消费者读取的附加线索，再将两路投影给语言模型。这样选择的是表示来源与目标，不证明内容和韵律已正交解耦；两套tokenizer的分词数不同，也不能把逐位置融合称为严格逐词对齐。[TextPro-SLM的有限对照](https://arxiv.org/html/2605.05927v1)支持比较全局pool与分组交错接口，却没有让重构质量成为纯韵律证书，同骨干ASR级联也已解释部分收益。应分别验词面QA、情感等非词面任务和每项绝对质量，避免平均差额相互抵消；继承的ASR/文本预训练、教师合成、双流训练与完整输入等待均付费，不能从数据小时数推出从零低成本或实时流式能力。附加线索无益、分词/语言失配或质量退步时，保留原声、可校订转录与成熟级联，不让更复杂输入替消费者验收。<!-- source-family:SF-2026-ARXIV-2605-05927 -->

本人纯note拟文：`SF-2026-ARXIV-2605-05927` — Daily2026-05-09补May08，exact-v1§3–5/A–F；2+1+2=5，双流来源/目标与token粒度职责差额深入。保重构非解耦、ASR级联/绝对质量/负面切片、全部继承与训练费、非streaming；未核代码/复现，Source R26有效，本段待PRE/实际POST。

### 06095 Metonymy → `MULTIMODAL-REPRESENTATION` / Ch23

插入阶段二f-CBM两段之后、multilingual map前，保原段。逐字拟文：

局部概念的读出还取决于隔离发生在哪一层。先让全图backbone混合信息，再按part mask汇聚末层feature，不能撤销已进入这些feature的其他区域线索；若目标确需受限局部读取，可以在各层阻断不同part组之间的attention值通路，再分别汇聚。训练时的straight-through近似只改变反向梯度，不使soft forward获得硬隔离。[Metonymy的有限对照](https://arxiv.org/html/2605.06095v1)支持这份位置差别，但mask本身由全图发现，所以隔离仅条件于给定mask，不保证整个系统输入独立或概念因果忠实；重新融合global分支也不能继承纯local承诺。Part属性区分与mask非空相交指标不等真实边界，局部性改善还会牺牲部分分类质量；mask发现、双阶段编码、标注和独立局部/全局回归均有成本。局部语义、mask或净预算不支持时，保留完整feature、独立概念监督与明确的全局路径，不由更可读的part标签批准全系统无泄漏。<!-- source-family:SF-2026-ARXIV-2605-06095 -->

本人纯note拟文：`SF-2026-ARXIV-2605-06095` — Daily2026-05-09补May08，exact-v1§3–6/T1–3/A/F/G；2+1+2=5，late readout-v-early value隔离具体差额。保全图mask生成、STE前反向/ensemble、PS/MPPO非因果与质量/全费反侧；未核代码/图像素/复现，Source R30有效，本段待PRE/实际POST。

### 05341 AEN-SAE → `WORLDVIEW-REPRESENTATION` / Ch5

插入sparsemax SAE完整两段后、external-consistency前。逐字拟文：

稀疏码的稳定性还要先固定被比较的对象。给定dictionary和非负稀疏权重，在非负code的平方重构目标上加入严格正的L2项，可使这份优化问题强凸，得到唯一且对输入连续稳定的最优code；它不证明联合学习dictionary、有限浅层encoder或真实语义解释同样稳定。可再用历史激活频率提出逐feature罚权，但其EMA状态、正则与clip范围都是训练配方，[AEN-SAE的必要原域](https://arxiv.org/html/2605.05341v1)中oracle支持恢复还需要收敛到正确活动权重及相应极限，有限clip不能直接继承。原文不同段落对频繁feature的罚权方向未一致，不据此发布唯一执行recipe。Dead feature比例降低也可能伴随explained variance损失，低稀疏度切片还会反退；EMA、超参搜索与匹配稀疏度/预算的重构及干预评价均付费。权重解释、覆盖或原模型行为不合格时，保留普通SAE、固定Top-k与独立null/干预对照，不由连续最优码签发无dead或monosemantic保证。<!-- source-family:SF-2026-ARXIV-2605-05341 -->

本人纯note拟文：`SF-2026-ARXIV-2605-05341` — Daily2026-05-09补May08，exact-v1§2–5/A.1–3/B/C；2+1+2=5，固定D/权重的最优code与联合学习分责。保oracle极限/clip不符、罚权方向冲突、dead与EV反侧/全费；未核代码/复现，Source R29有效，本段待PRE/实际POST。

## A44 — 四份训练/采样逐字窄稿prepared（未PRE/未写）

### 06597 UniSD → `TRAIN-SFT` / Ch29

实读Ch29 DiSC→完整short/full context两段→snapshot状态/刷新风险，及前面同模型privileged target/GUI-SD、Ch28/30开篇与现有末尾职责。差额为主teacher受多context视图agreement调制，不是再讲teacher非真值。插入short/full-context两段之后、snapshot状态段之前。逐字拟文：

不同context视图还可以只参与监督权重，而不把多份teacher分布直接平均。一个条件分支在同一已访问prefix上，让EMA teacher分别读取主指令与辅助上下文，用视图间分歧调节对主分布的蒸馏；辅助路径不因此获得单独目标权，也不是多个独立教师的正确性投票。[UniSD的有限对照](https://arxiv.org/html/2605.06597v1)还对已汇聚的divergence scalar设置上限，超过上限的局部梯度会关闭，这不是直接裁剪参数梯度范数，更不证明所有风格或旧能力被保留。正负上下文可能包含外部gold，不能称零监督；EMA、所有视图前向、rollout与训练均计费，较少更新步数不能代签总费下降。视图数量增加、任务迁移和保持指标也有反退，训练轨迹上的JSD或较低PPL不是完整旧分布等价证书。Context不保义、teacher一起错或保持回归失败时，保留固定可靠teacher、verified targets、较少视图或原训练，不让高agreement替外部真值与实际能力验收。<!-- source-family:SF-2026-ARXIV-2605-06597 -->

本人纯note拟文：`SF-2026-ARXIV-2605-06597` — Daily2026-05-09补May08，exact-v1§2–3.5/A/B/C/G；2+1+2=5，多context只调主teacher权重/EMA与scalar cap分责。保gold权限、保持指标/多视图非单调/总费反侧；未核代码/复现，Source R29有效，本段待PRE/实际POST。

### 06546 Token Superposition → `TRAIN-PRETRAINING` / Ch28

实读「Future-token辅助目标」NTP→受控模型→采用边界三段、LET、rollout未来序列与几何正则完整局部，以及压缩baseline/预算粒度并非输入bag的现owner。Ch27/29职责实际开篇已读。插入future-token三段之后、LET前；区别单主头next-bag训练阶段与额外future head。逐字拟文：

更粗的训练目标也可以暂时替换主头，而不增加future-token辅助头：把连续不重叠s个token的embedding平均成一个输入位置，用同一输出logits对下一bag各出现位置的token取CE平均，随后恢复普通NTP，并保留两阶段的embedding与输出头。它丢掉bag内次序，粗阶段模型不能直接当标准AR生成器；重复词仍按出现计数，也不把训练loss的常数平移当一般零误差证明。[Token Superposition的有限对照](https://arxiv.org/pdf/2605.06546v1)在相同latent序列长度下扩大原始输入，以更多data消费换作者等FLOPs预算内的质量，恢复阶段与数据获取不能省账。同data基线仍可达到更低loss，部分任务反退，重置两端表示的消融只支持接口连续性而非唯一因果解释；较大模型未全量调参或多相同run。应共同选择bag大小、粗阶段比例和完整恢复质量，计入全部数据与搜索费用；data-bound、次序信息重要或恢复失败时，保留原NTP、较短粗阶段或已验辅助目标，不从吞入更多原始token推成免费训练或部署加速。<!-- source-family:SF-2026-ARXIV-2605-06546 -->

本人纯note拟文：`SF-2026-ARXIV-2605-06546` — Daily2026-05-09补May08，exact-v1 PDF§3–7/A/C/D/E，实际视觉页4–6/9/10/20；2+1+2=5，next-bag主目标/恢复NTP与等FLOPs多data分责。保重复词/常数条件、Figure3表配置冲突、单任务/同data反侧与全费；未核仓库/复现，Source R31有效，本段待PRE/实际POST。

### 05387 Conditional Diffusion → `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24

实读Ch24:237–247双条件混合→InpaintSLat→空间噪声→多视角修复完整段，及973–997 manifold reach与curvature guidance，末尾owner/Ch23/25实际开篇。现有几何切向是manifold而非测量nullspace，不当同义已有覆盖。插入InpaintSLat后、空间噪声前。逐字拟文：

初始化与约束的关系还须分开可行性和条件概率：无噪声满行秩线性测量只固定normal分量，nullspace内的tangent分布仍须与观测条件匹配。Gaussian加噪下normal score可由测量解析求出，把它修正正确却不使unconditional tangent score自动成为conditional score；一种受限分支先在正确noisy normal的仿射切片上做projected BAOAB混合，再继续带normal修正的逆过程。[Conditional Diffusion的必要原域](https://arxiv.org/html/2605.05387v1)支持这份职责分解，但有限混合不保证精确条件采样，理想slice极限也不能抹去原条件错配。其连续精确score声明不覆盖learned score与有限步误差，更强界另需混合分布、entropy、敏感性及间隔等假设；感知/FID改善不是posterior coverage证书。初始化、投影、缓存与全部网络调用均计费，作者缓存后的有效NFE匹配不等实测walltime；非线性/噪声测量、score失配或质量退步时，保留原条件模型、较保守projection/solver与独立测量及质量检查，不由满足测量签发无偏或真实细节恢复。<!-- source-family:SF-2026-ARXIV-2605-05387 -->

本人纯note拟文：`SF-2026-ARXIV-2605-05387` — Daily2026-05-09补May08，exact-v1§2–4/Alg1/D及§5必要假设声明；2+1+2=5，measurement normal-v-conditional tangent具体差额。只采用机制分责，不转写未完整逐证的KL保证；保有限K/离散误差、100有效NFE非walltime与全费。未核代码/图像素/复现，Source R31有效，本段待PRE/实际POST。

### 06638 ScaleLogic → `TRAIN-GRPO` / Ch33

实读Ch33:1910–1945 exploration/mode→tool预算→自博弈职责→Tool-R0→VZero完整局部，及ReasonMaxxer的离线预算分责，不把Task结构归Ch66测量器。插入自博弈职责段之后、Tool-R0具体工具自博弈前。逐字拟文：

课程还可以在固定生成规则和可核答案下先控制任务结构，而不让出题者与solver共同漂移。对合成逻辑任务，证明深度、可用运算符和采样深度分布是不同轴：相同目标深度不保证相同prompt长度、分支或训练成本；更丰富逻辑与由浅入深的课程，在[ScaleLogic的有限对照](https://arxiv.org/html/2605.06638v1)中改变达到验证阈值的效率及下游迁移，但不能把已测log-log拟合当普遍多项式律。主指标为首次达到90%验证Pass@1的更新步数，全部rollout token、FLOPs估计与GPU-h的指数不同；主曲线单seed的拟合误差也不是多训练seed置信区间。固定深度/约定步数对照仍混有结构和token预算，Avg@8不等Pass@8，增加输出上限后的OOD仍有视野边界。题目构造/审计、课程门槛、频繁验证、所有生成与更新均计费；规则、标签或迁移支持不足时，保留固定题库、普通深度混合与直接任务验收，不从合成训练成功授予无界推理或通用课程常数。<!-- source-family:SF-2026-ARXIV-2605-06638 -->

本人纯note拟文：`SF-2026-ARXIV-2605-06638` — Daily2026-05-09补May08，exact-v1§3–5/A/C–F/H/I必要；2+1+2=5，task结构/课程/预算量尺分责差额。保有限深度/单seed、quantifier与reuse混杂、Avg@8/OOD预算、全部费用；未核代码/图像素/复现，Source R31有效，本段待PRE/实际POST。

## A45 — 作者六部分归并与日级送验停点

恢复后只接本日有限差额，全部Source已root实际分批核至R31，具体NC核至R33；A43/A44七稿PRE R34，Ch24实际POST R35、其他六段R36均通过，31新实际整合＋9具体NC，原1 ERNIE另保留。所有Books窄位已释放，本人七条纯注仅行政同步既成POST事实，不重Source或再造研究审阅；未写其他notes/正文。曾有六稿批量patch同文件hunk倒序导致验证失败，确认六处未写后按实际正文顺序修正，实际保存逐字与PRE稿一致，完整两侧与本人注已自读，root实际POST接纳。

有限arXiv 51完整题摘＝39当窗新增＋6贡献/早事件关闭＋6资格终态隔离，另Teaching Claude Why1，合40新家族。六关闭仍保原理由/05556范围纠偏/05209Mar23先稿，不恢复；六资格以A35/R25正确身份与有限停止为准，不支持候选/完整Source/Books/无遗漏。来源实际语言/数量/分页及历史缺段沿A11/A24保留，不拿count20代实际返数或继承他日coverage。

报告已归并原1＋新40＝41行连续单表、41个§4证据小标题，31整合/10NC含原ERNIE1。检查时间2026-10-18T21:18:26+08:00；本轮仍进行中，仅待非作者完整DAY，未预授完成。实际机器核：baseline5329字符，原整行/小时窗及1854字符连续原§4均逐字保留；91本地引用0缺失，V3通过；限定报告/SUP与本轮最后书稿位cached/unstaged diff-check无诊断。校验不替代语义/源覆盖，原始文件、既有index及并发更改未动；未stage/commit/push。普通作者Source/Books工作0，下一步只消费本日报DAY诊断或通过结果，再保存完成态并交非作者FINAL。

## A46 — DAY后完成态保存

Root R37已真实连续读完整六部分并独立核41候选/41证据URL、31整合/10NC含旧1、原行/窗/连续旧§4、91本地引用、V3和限定两层diff，通过本日日级验收。作者仅同步报告开头/结论/§2当时等待句/§5/§6为2026-10-18T22:02:17+08:00完成态；六资格/机构历史缺段保持隔离，原§4及有效研究/Books未再改。Root R38已对实际保存完成态FINAL读回通过并接纳本日；全部窄位与作者ownership释放，普通研究/Books待办0，本日结束，不接新日、不再研究或书稿；未stage/commit/push。
