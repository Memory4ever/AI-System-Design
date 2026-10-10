# 2026-01-09 Daily 增量 source 补查 — 2026-10-07

窗口：2026-01-08 ～ 2026-01-08（BJT 完整自然日）。原窗口、17项候选及评分、exact-v1 证据结论、原验收记录全部保留。只补遗漏，不把提交日期当公开，不把发现列表人口当逐篇审读队列；不写共享 Books / LEARNING_STATE / 索引，不 stage / commit / push。

当前状态：作者必要证据与停点已整理，非作者最终复核未完成。root已通过官方API独立完整读17份 exact-v1 题摘：13项明确潜在增量、ALERT与VideoMemory各要求一处决定核心；补后认可ALERT准入6分/仅报告及VideoMemory具体关闭，AgentDrift贡献关闭，04301只核必要公开日。作者随后定点读14份拟准入论文的方法/关键评价/限制，不称14全文或代码审阅。root实际独核机构短文的窄反证及Ch72/78已有覆盖，准入6分；新增15与原17去重合计32，本文件不自授独立验收。

## 1. 独立启动与有限发现范围

已完整重读 AGENTS.md、RESEARCH_CONTRACT.md、REPORT_CONTRACTS.md、CODEX_RESEARCH_PROMPT.md、ROADMAP.md；RESEARCH_SOURCES 只读取使用说明、14 Daily 来源与 arXiv 主题/恢复规则，未运行 Weekly。学习状态只读本月路由。本日 README、STOP、DATE_BASIS、机构停点及原始有限目录独立读取，未加载其他日期 Daily/Weekly 判断。

本日原始 `ARXIV_THEME_PAGES.json` 的四个主题、八页、12分类是一次有限发现人口：model-learning 283 / execution-systems 123 / multimodal-action 70 / agent-memory 132，跨组 union 364 unique families。该人口按 UTC submitted 缓冲 2026-01-06T19:00～2026-01-08T01:00 收集，**不是364本窗候选，也不是364份摘要审读队列**。本次实际读取这些标题，按可辨认的机制或反证手选17份完整v1题摘；未把整个主题类别排成待审池，未检查全月库存或未知早ID版本史。

完整原始题摘唯一接口：[17份 exact-v1 Atom](https://export.arxiv.org/api/query?id_list=2601.03500v1,2601.03509v1,2601.03555v1,2601.03570v1,2601.03600v1,2601.03649v1,2601.03655v1,2601.03791v1,2601.03905v1,2601.03955v1,2601.03992v1,2601.04056v1,2601.04061v1,2601.04098v1,2601.04170v1,2601.04171v1,2601.04301v1&max_results=30)。只读17题摘，不称17全文通过。API current family 字段可能含后续版本，因此评估文字限定精确v1。

## 2. 14 Daily 来源的本次实际范围与停止点

以下是本次独立访问及本日原始有限目录的可复用元数据范围，不继承原报告的本窗事件判断。当前首页、空 payload、排序不明、语言筛选或未披露历史记录均不作“零发布”证明。

| 来源 | 本次实际读到的有限范围 | 窗口判断及停止点 |
| --- | --- | --- |
| SRC-OPENAI | Research→Research Index 当前8个 dated cards（Oct06～Sep06）；Jan08官方域定点检索，实际读Netomi全文，Healthcare为原报告已处置身份 | Netomi Jan08发布日期成立，但现有schema/PII/fallback与并行原则组合没有给新的依赖控制、条件或反证，贡献前关闭。当前index非Jan08历史目录；不从无搜中断言0发布，不要求整个历史恢复 |
| SRC-ANTHROPIC | 当前Research可见10条；复用本日原始174条有限SSR目录元数据作日期路由；实际读Jan08 critical-infrastructure全文及PNNL同日合作原文 | 原Jan08T00Z＝BJT08:00现在落补充自然日，不继承“旧窗口前”关闭。root核单次水厂模拟替代known technique的窄反证，6分/具体已有覆盖；无新攻击技术、生产成功率或速度保证 |
| SRC-GOOGLE-AI | Google Research `/blog/2026/01/` 完整9条 Jan28～Jan12且无pager；DeepMind `/blog/page/4/` 完整列表Feb2026～Nov2025，Jan三条具名日期分别Genie Jan29、D4RT Jan22、Veo Jan13 | 这些有限目录没有Jan08项。未运行忽略year的772页publication库存；尚无Jan08完整dated research catalog，不能授机构0事件/无遗漏 |
| SRC-META-AI | Research当前空text；Blog当前页1与页2实际全部可见主cards，页2含Mar27/Mar11/Feb09及Dec18/Feb2025等混排，Next仍在 | 停页2，未用首旧卡片关闭历史排序，不扩到整个archive。需要具体Jan08具名条目/该日dated切片才重开；空text不等0事件 |
| SRC-QWEN | 官方API `https://qwen.ai/api/page_config?code=research.research-list` 的完整60条date/title/id独立解析；原始同URL缓存 `daily-20260104/supplement-20261007/qwen.raw`（只读元数据，未读别日判断）；最早2022-11-14、最晚2025-12-23 | 本有限返回人口无Jan08，停止完整60条；无具名隐藏Jan08线索时不请求全机构历史，不授全网无遗漏 |
| SRC-DEEPSEEK | 官方updates可见完整chronology当前Sep10→Apr24 V4→Dec01 V3.2等跨窗邻项 | 此updates切片无Jan08项，停止于公开有限更新表；不等同研究论文/未知早ID修订全覆盖 |
| SRC-MOONSHOT | 官方Platform Blog完整26条Nov07/Nov06_2025～May2024，没有pager | 仅该目录无本日项；不承诺整个机构模型/仓库发布0事件 |
| SRC-TENCENT-HUNYUAN | Research/browser失败作为初始恢复记录；独立解析root给的同URL `daily-20260104/supplement-20261007/hunyuan.raw` 完整en9/total9；displayPublishTime BJT Feb03～Sep22，9个具名title/id均实际读；zh11保持原不同切片不合并date | 本有限9条没有Jan08，停止total9；不把语言/updatedAt等同首次公开，也不因目录無当窗项要求全部历史无删除证明 |
| SRC-ZAI | 当前Research实际15可见cards，Jan19/Jan13→Dec10/Dec09跨窗，View more在；本日原SSR另16条元数据。release当前 dated chain Jan19/Jan14→Dec22 | 当前可见切片无Jan08项。明确15可见不伪装成全历史或16条全部当前重取，不假设后台createdAt为公开日期 |
| SRC-BYTEDANCE-SEED | 当前Research动态页；本日本源2026/US及CN有限5页元数据仍作目录路由；本次重新请求paper page80/US：total82、returned2、has_more=false、Jan21/Jan19，与原尾页一致 | 当前语言/状态筛选及total与returned人口差额仍在。page80 false只允许有限分页停止，不证明Jan08无事件。Blog原有限14/19最早Feb11，不展开整个publication历史 |
| SRC-BAIDU-ERNIE | 官方当前Blog10cards May09～Nov21，相邻Jan15→Jan08 ranking→Dec23，Next 2/2 | Jan08 ranking原身份已关闭，新增无机制不重开、不改原分。只能对可见列表负责，非全网无遗漏 |
| SRC-XIAOMI-MIMO | 本次实际官方 `4752.2908c99e.js` route17EN含index，即16非index=15内容+1template；6 frontmatter Dec18/19、May30/Jun08/10、Sep27；9null的async chunk→iframe逐项定位Dec16、Mar18、Apr2026/22/27、Sep21；template完整文本泛例core读完 | 15内容均窗外，template无可辨本日机制，不评分；原MiMo v1/v2日期/评分/证据不动。没有具名Jan08隐藏身份，不索全历史。恢复仅新具名Jan08事件/重要修订 |
| SRC-MINIMAX | 当前Blog完整12可见卡片Aug13→Jan27→Dec23/Oct27，未见本日dated项 | 有限目录停止；没有索整个AgentTech历史，不授全机构无遗漏 |
| SRC-ARXIV | 上述四主题8页/364 unique标题；17手选完整v1题摘；17个具名DOI原日期字段，结合官方ID/公告政策作日级必要过滤 | 16项arXiv事件的公告政策下界/具名ID实际公开上界同落Jan08；不是registered直接等first-public。04301仅恢复到Jan08～Jan09界限，缺实际公开日，不列正式候选/不评分。早ID未知重要修订仍精确隔离，不扩月库存 |

## 3. 新17题摘 FIRST 准入信号与核心后的处置

| exact-v1 | 完整题摘中的具体贡献方向 | 暂定处置 / 不授予的保证 |
| --- | --- | --- |
| [2601.03500 SDCD](https://arxiv.org/abs/2601.03500v1) | 结构破坏的图像对照保留局部纹理，惩罚在结构改变后仍高置信的输出，区分纹理支持与几何支持 | 潜在mechanism；不由hallucination分数保证所有视觉事实正确 |
| [2601.03509 Evolving Programmatic Skill Networks](https://arxiv.org/abs/2601.03509v1) | 可执行skill网络、局部故障修复与成熟度门控降低更新概率，局部refactor需短窗回滚验证 | root准入校准通过；更新概率有0.1下界，不是冻结成熟skill；不保证稳定终身学习 |
| [2601.03555 SCRIBE](https://arxiv.org/abs/2601.03555v1) | skill prototype路由子目标与rubric约束中层过程监督，试图避开噪声逐token process judge | 需校准是否新增监督接口而非任务rubric换名；不采中层掌握的因果保证 |
| [2601.03570 CPT概念学习](https://arxiv.org/abs/2601.03570v1) | concept/circuit代理显示阶段学习、较大增益伴随遗忘，语义关联影响干扰/迁移方向 | 潜在成立条件/反侧；代理读数不自证概念因果 |
| [2601.03600 ALERT](https://arxiv.org/abs/2601.03600v1) | gated FFN相乘前的gate/context差异，两VIB classifier及benign/harmful prototype距离softmax token权重 | 决定核心已补：具体pre-product operator和progressive ablation支持局部替代传感分支；等root核，不采用零样本/安全保证 |
| [2601.03649 SyncThink](https://arxiv.org/abs/2601.03649v1) | answer主要关注think结束transition，推理饱和与文本结束分离，监测transition信号作training-free早停 | 潜在termination设计；不把token节省当通用质量不降 |
| [2601.03655 VideoMemory](https://arxiv.org/abs/2601.03655v1) | 实体descriptor memory在逐镜头检索、更新中保身份而允许故事状态变化 | §3.3决定核心后拟关闭：LLM匹配tuple相似状态/生成新状态再append，没有新的commit/identity/transition约束或评价反证；不是因模块组合本身排除 |
| [2601.03791 PII cue-controlled](https://arxiv.org/abs/2601.03791v1) | 按cue分层人口比较重建率，低cue条件人口下降揭示泄漏分数可能混入模式补全；不是逐样本删除cue的因果介入 | 潜在隐私评估反证；不是“模型不会记忆PII” |
| [2601.03905 World model as tool](https://arxiv.org/abs/2601.03905v1) | 低调用、错误使用预测，强制调用仍不自动改善任务，区分tool available/调用/解释/行动能力 | 潜在负向工具接口证据；不推断所有world model无用 |
| [2601.03955 ResTok](https://arxiv.org/abs/2601.03955v1) | 图像/latent层级残差量化、跨层融合减少语义重叠，按层并行AR而非逐token | 潜在表示→生成调度接口；不采用摘要headline fidelity/steps作保证 |
| [2601.03992 Edge GPU-NDP MoE scheduling](https://arxiv.org/abs/2601.03992v1) | 低batch NDP tensor parallel、联合GPU/NDP专家放置与不依赖profile的预取 | 潜在资源分配机制；当前DOI v1 Updated为July，日期不能由该字段抹掉Jan注册或混入后版本 |
| [2601.04056 CoM-DAD](https://arxiv.org/abs/2601.04056v1) | 先训练连续semantic prior，再用其projection条件化离散absorbing decoder；paired representation swapping与模态adapter | root准入校准通过；不是逐步joint latent coupling，“Optimal Transport”没有对应cost/solver/最优证明，性能与理论权限限定 |
| [2601.04061 CLAP](https://arxiv.org/abs/2601.04061v1) | 人视频动作latent与机器人proprioception对比对齐后量化为动作codebook，区分运动外观与可执行动作 | 潜在表示校准条件；对齐不保证任意物理动作安全/可执行 |
| [2601.04098 Positional bias](https://arxiv.org/abs/2601.04098v1) | layer conductance/sliding-window观察到架构与深度条件，lexical scrambling下局部profile仍在 | 潜在短context反侧；归因代理不直接证明attention因果 |
| [2601.04170 AgentDrift](https://arxiv.org/abs/2601.04170v1) | 独立补§2.1/2.2/2.4/4.4后确认rolling50、三窗阈值、加权ASI及baseline/reset/exemplar具体配方；模拟人格ground truth与成熟治理组合尚未建立可辨认新机制或独立有效性条件 | 非作者决定核心核通过后贡献关闭，不说没有operator；安全负向标题不自动准入，不评分或扩读全部附件 |
| [2601.04171 SWE-Agentic Rubrics](https://arxiv.org/abs/2601.04171v1) | repository context→专家checklist→不执行tests的patch judge，对照context/清晰度影响并暴露test未覆盖语义问题 | 需核是不是上下文评估接口条件而非只新增任务rubric；不由judge分数签发patch正确 |
| [2601.04301 Contamination](https://arxiv.org/abs/2601.04301v1) | 控制预训练污染，fresh data/finetuning/temperature/长度改变污染表现 | 公开日隔离：submitted Jan07、实际DOI registered Jan09及v1 Updated Jan09不能单独证明Jan09公告；可核区间Jan08～Jan09跨窗。只需Jan08/Jan09具名实际公告或作者原文公开日，不评分/不搬别日 |

## 4. 日期边界原值与有限性

日级必要依据沿本日 `DATE_BASIS.md` 已保存的 [arXiv identifier政策](https://info.arxiv.org/help/arxiv_identifier.html) / [公告政策](https://info.arxiv.org/help/submit/index.html)：精确v1提交后才能公开、ID/DOI在实际公告时分配；submitted不是公开。Actual DataCite registration只提供该具名公开ID已经存在的上界，不能单独当作者/家族first-public。按公告下界与实际上界合取同一BJT日；不能把schedule推作实际公告时刻，不恢复秒级first-public。具体作者早公开线索出现时只核该身份。

本次实际读取17个 `https://api.datacite.org/dois/10.48550/arXiv.2601.<id>` 原字段；v1 Submitted均Jan07且早于19Z，以下实际DOI registered只是上界原值（UTC），不是直接first-public：

| id | DOI registered UTC | v1 Updated UTC（仅原字段） |
| --- | --- | --- |
| 03500 | 2026-01-08T02:39:47Z | 2026-01-08T01:11:08Z |
| 03509 | 2026-01-08T02:40:00Z | 2026-01-08T01:11:30Z |
| 03555 | 2026-01-08T02:41:14Z | 2026-01-08T01:16:28Z |
| 03570 | 2026-01-08T02:41:35Z | 2026-01-08T01:18:20Z |
| 03600 | 2026-01-08T02:42:17Z | 2026-01-08T01:20:19Z |
| 03649 | 2026-01-08T02:43:25Z | 2026-01-08T01:23:31Z |
| 03655 | 2026-01-08T02:43:33Z | 2026-01-08T01:24:02Z |
| 03791 | 2026-01-08T02:46:48Z | 2026-01-08T01:35:40Z |
| 03905 | 2026-01-08T02:49:33Z | 2026-01-08T01:42:10Z |
| 03955 | 2026-01-08T02:50:44Z | 2026-01-08T01:45:08Z |
| 03992 | 2026-01-08T02:51:38Z | 2026-07-01T00:12:34Z（异常较晚原值，不能当本窗公告） |
| 04056 | 2026-01-08T02:53:08Z | 2026-01-08T01:52:04Z |
| 04061 | 2026-01-08T02:53:16Z | 2026-01-08T01:52:17Z |
| 04098 | 2026-01-08T02:54:08Z | 2026-01-08T01:54:20Z |
| 04170 | 2026-01-08T02:55:51Z | 2026-01-08T01:57:57Z |
| 04171 | 2026-01-08T02:55:52Z | 2026-01-08T01:57:59Z |
| 04301 | 2026-01-09T02:41:56Z | 2026-01-09T01:02:37Z |

## 5. 机构核心与已有owner的有限比较

[Anthropic Jan08短文](https://www.anthropic.com/research/critical-infrastructure-defense)全文、[PNNL Jan08合作原文](https://www.pnnl.gov/news-media/generative-ai-speeds-cybersecurity-defenses)必要核心实际读：夏2025 Sonnet4及预定义网络工具、单次模拟水厂；工具失败后选择另一个已知替代技术，不是创造未知攻击。合作原文说明自然语言重建动作链与故障修复，不披露可审计的失败频数、工具/权限全部状态或matched speed control。3小时/一周估计不采作对照性能。

`AGENT-TOOL-CALLING` Ch78已有“失败反馈是Retry State”、repair/substitute/decompose和proposal≠授权机制链，一般exception→replan不是本次Books差额。root实际独核Anthropic L19–24与PNNL L263–287、`PLATFORM-SECURITY` Ch72 29–31资产可达路径不等界面/已列工具、canonical Ch78 707–728 structured failure→registry/resolver替代且真实effect时授权；具体已有覆盖定案，2+2+2=6必要安全命题深入完成，只报告受限实例，不堆Books案例。文章Jan08日期据publishedOn＋两primary，不把Summer2025模拟日期当首次文章日期。不得改写真实水厂侵入率、自动攻击普遍成功或安全保证，作者无Books写入。

[OpenAI Netomi Jan08原文](https://openai.com/index/netomi/)全文实际读：低置信fallback、schema/PII/policy/observability及concurrency原则没有披露新并行dependency/cancellation/effect机制或matched control。因此不因品牌/enterprise/吞吐数字准入，贡献前关闭；没有说这些成熟原则无用。

### [SDCD exact-v1](https://arxiv.org/html/2601.03500v1)

实际§3 Eq2、§4.1/4.3及限制：原图与patch-shuffle图的logits作`(1+α)original−αshuffle`，plausibility过滤β=.1、α=2。结构破坏对照能形成纹理支持/结构支持的不同分支，但patch重排也改变邻域内容，不是完美语义保持介入。三个7B模型、A100、POPE/MME及500幅CHAIR caption，max512/T1/topP.9；实现还给两视图image attention+.6，不能把总体收益全归shuffle，resampler切片不总胜VCD。只报告局部contrastive alternative，不授通用视觉事实正确。候选2+2+2=6、标准核心已读；`MULTIMODAL-REPRESENTATION` Ch23为视觉支持权限提案，Books待root决定。

### [Evolving Programmatic Skill Networks exact-v1](https://arxiv.org/html/2601.03509v1)

实际§2.4 Eq6、§2.5、§4.4与限制：失败trace只修被执行skill，top-down定位/bottom-up patch；成熟度更新概率`0.9·sigmoid(5·(.6−V))+.1`，不冻结成熟程序。refactor检查parent/child与top5 semantic邻居、5个rewrite case；用最近3个受影响任务暂测，成功率降超20%执行inverse operations回滚。Fig5有门控对照，当前online batch1/3 runs，部分旧baseline模型不匹配；无形式语义保持、稳定收敛或长期最优保证。2+2+2=6标准完成；Ch80现有candidate lesson/revision/held-out/promotion/rollback分责（344附近）已经承载一般治理，概率门控/极短回滚人口只是有限实现案例，提案仅报告，未称exact recipe已有覆盖。

### [SCRIBE exact-v1](https://arxiv.org/html/2601.03555v1)

实际§3–6：subgoal/skill/span router→prototype 0–3 judge→0.3 process＋0.7 outcome的GRPO；prototype每1000 step重聚类。Qwen3-4B/Llama3.2-3B、GPT5-mini judge、10k MATH/ToolACE与BFCLv4；PRM/不同reward weighting有局部对照。中层掌握先出现不证明独特的因果涌现链，cluster/router/judge可失配，刷新与judge成本要另外付。2+2+2=6标准完成，非作者必要核完成；最终仅报告受限prototype人口，不把judge当真值，不声称精确配方已写入Books。

### [CPT概念学习 exact-v1](https://arxiv.org/html/2601.03570v1)

实际§3.2–4及限制：FICO→BIO继续训练、GPT2-Large/.7B及Llama3.2-1B，以同一(c,r)目标logit变动测学习/遗忘；500个concept的circuit相关读数不是因果机制。Qwen3-Embedding相关性top/mid/bottom各100，5×4知识顺序在固定阶段预算与BIO对照下有干扰/迁移不对称，未验证future circuit-aware scheduler。2+2+2=6标准完成；`TRAIN-PRETRAINING` Ch28提案仅报告阶段概念干扰条件，不将embedding relatedness当训练分配oracle或概念唯一因果。

### [ALERT exact-v1](https://arxiv.org/html/2601.03600v1)

实际§3.1–3.3、§4 Tables2–3及限制：FFN gated multiplication可能掩盖类别差异，取相乘前gate/context两分支，分别VIB classifier；按benign/harmful prototype距离各作softmax token权重再聚合。Table3逐步消融支持该局部operator，不只是classifier数量。Layer4选择已使用AutoDAN探索样本，所以classifier只用benign/harmful训练不等整个框架从未看attack；Llama3-8B/Mistral7B/Vicuna7B及三个attack人口，Table2 Vicuna/XSTest部分68–86不支持“全都>90”。2+2+2=6，安全边界受影响核心深入已读；Ch72提案仅报告实验传感替代，不授unseenattack/生产安全保证，待root核operator。

### [SyncThink exact-v1](https://arxiv.org/html/2601.03649v1)

实际§3.4 Eq3–5、§4 Table1、§5.4–5.6及限制：显式`</think>` rank≤`floor(t·exp(−λH))`注入结束，λ=.8经heldout MATH500调节；三个R1 distill 7–14B、greedy单run，部分任务accuracy下降。中心方向冲突：式子增λ会降threshold，理论上更难触发stop；§5.5却称增λ单调缩短。没有核code，不选择一方补造解释；保2+2+2=6与描述性transition接口，不授参数方向/可复现控制律。`INFER-REQUEST-LIFECYCLE` Ch42提案暂缓中心采用，精确重开只需原实现或修正式与对应配置，不请求全部实验复现。

### [PII cue-controlled exact-v1](https://arxiv.org/html/2601.03791v1)

实际§3–5及限制：PII normalize后的target/prefix最长公共子串定义cue，CRM在`cue<τ`条件人口上测重建，不是do-intervention的因果cue效果。未见训练的高cue文本也可重建说明reconstruction≠membership，不证明无记忆/真实隐私风险低。mC4已知训练、560M/1.3B/13B、32语言blackbox PT；MIA数据25语言与结果32的口径不混合。3+2+2=7、隐私评价反证深入核心完成。root在Ch72原membership邻接实际写294–296附近两段normalized cue分层/Unknown/真实泄漏后果；jan02_new_evidence实际源/owner及两段/前后/源注POST通过，整合1项。不重复一般低loss≠membership、不授逐样本去cue因果或低真实风险；作者无Books写入。

### [World model as tool exact-v1](https://arxiv.org/html/2601.03905v1)

实际§3/§4.1–2/§5.2及限制：normal/no-tool/forced工具接口；Agent任务用cloned ground-truth environment simulator、VQA用Wan2.1生成视频，不能合称已验证统一learned world model。9个GPT/Llama/Qwen，未测Gemini/Claude因成本；强制调用不自动提高foresight，call频率相关不证明“多调用因果有害”。未来Decider/Reflector/Memory/RL建议非已实现保证。3+2+2=7、工具评价负侧深入完成。jan02_new_evidence实际必要core/Ch78 218–242 utility admission、调用观测与使用结果、no-tool反事实核通过，具体已有覆盖，只报告本次新实验，不授所有world model无用。

### [ResTok exact-v1](https://arxiv.org/html/2601.03955v1)

实际§3–4、§5.1/5.4 Tables2–5与Recon-vs-Gen：多尺度image/latent residual、masked cross-hierarchy attention，NTP之后HAR按层group并行。Table5 AR128step gFID4.56→HAR9step5.53，不是质量免费；tokenizer训练更久重建可改善而generation后退。DINO alignment、nested dropout与两阶段训练付费，ImageNet256且ablation30/50epoch与主200/300分开。2+2+2=6标准完成；Ch24提案仅报告codec→factorization/质量取舍，残差重建不自签生成质量。

### [GPU-NDP MoE scheduling exact-v1](https://arxiv.org/html/2601.03992v1)

实际III–IV关键方法/评价：前两FFN列TP/最后行TP减低batch NDP不均衡；GPU/NDP placement用activation/最后传输时间平衡。prefill频率初始化decode prefetch，dataset-free仍依赖当前prompt，GPU驻留上限/无命中fallback必需。AttAcc+modified Ramulator2仿真、假定RTX5080/NDP-DIMM，batch1、input/output512、四MoE/2–6DIMMs；2DIMM TP单独有退步，prefetch不是越多越好，非物理runtime结果。2+2+2=6标准完成；`MODEL-MOE` Ch21为专家TP/placement提案，仅报告特定仿真，不写错Ch57为推理调度。

### [CoM-DAD exact-v1](https://arxiv.org/html/2601.04056v1)

实际§3–4/限制：StageI 400k continuous semantic prior（frozen MoCov3/MPNet）；StageII 300k `Proj(r)` prefix条件MASK denoiser，paired表示swap与2adapter，text:image:paired=2:2:1/100k paired、8A800。不是每step jointly evolving coupled latent。“Optimal Transport”未给cost/solver/最优证明，仅采用混合采样/交换的描述。Table1不同长度40/64/128/256、预算与BLEU/AR identity口径限制，图引用也不一致，不采5×end-to-end或理论最优。2+2+2=6标准机制核心完成；Ch24提案仅报告连续prior→离散条件接口，性能/OT权限隔离，未运行实现。

### [CLAP exact-v1](https://arxiv.org/html/2601.04061v1)

实际III-D/E、IV、V-A/C/D：robot ActVAE frozen VQ码本→visual action/nuisance分支，人视频contrastive正例为self-anchor；NTP pseudo/gold codes，RF action expert读stop-gradient VLM KV，KL reference是regularizer非trust-region保证。20seen/20OOD pickplace、其他10次小样本任务，Astribot chassis/torso锁定；人视频/contrastive消融支持局部OOD条件，不证明完美物理解缠或任意可执行。IV Qwen3VL4B与V-C Qwen2VL4B/36layers记载冲突，精确backbone/层位复现权限隔离；3090 RF/NTP latency不直接给机器人SLO。2+2+2=6标准核心完成；Ch26提案仅报告机器人码本锚定video latent的受限action分支。

### [Positional bias exact-v1](https://arxiv.org/html/2601.04098v1)

实际§3–4.2/限制：8文本+1scramble、4模型124M–8B；P10 stride1舍边界、normalized layer conductance。P50两故事用Llama1B而非8B，不作纯window ablation；“全是learned positional embedding”与Llama/Phi身份不符，不采用架构唯一因果。next-token最后层读出下的早层低归因不证明信息不存在/电路不必要或长context压缩正确。2+1+2=5标准完成，Ch13提案仅报告短context lexical scrambling/层位proxy条件；不授attention因果。

### [SWE-Agentic Rubrics exact-v1](https://arxiv.org/html/2601.04171v1)

实际§3、4.2、5、8：Sonnet4.5 expert 30turn repo调查→加权FileChange/SpecAlignment/Integrity/Runtime rubrics，GPT5-low binary judge用于BestK；500 SWE-Verified×16固定patch，Qwen32B30turn/QwenCoder50turn、T1。repo/no-repo同expert对照给上下文条件；100case utility audit是GPT5-medium非独立人工，低rubric/testpass中54%“highutility”不证明真实bug、46%有过度要求/失配。expert可shell，不能称wholepipeline execution-free；更强judge与granularity confounded，RL为future。2+2+2=6，具体test/judge权限反侧核心深入；jan02_new_evidence实际必要core/Ch66 2739–2763 formation/execution/ranking/hidden executable holdout核通过，精确repo-grounded binary recipe受限仅报告，不称exact recipe已有覆盖。

### 决定核心关闭 / 日期隔离

[VideoMemory exact-v1](https://arxiv.org/html/2601.03655v1)只补§3.3：tuple(entity, attributes, reference image)、character/prop/background三bank，LLM matcher取相似state，否则history refs条件生成新图再appendtuple。未给新的commit/identity验证/transition约束或足以改变判断的反证；按此具体事实拟贡献关闭，保留初始潜在信号及改判依据，待root实际核心核。AgentDrift按root完整题摘上述理由贡献关闭，无分数。[04301](https://arxiv.org/abs/2601.04301v1)有潜在评价反证但只恢复Jan08～09公开界限：未确认本窗前不评分、不进入Books；只请求具名实际公告或作者原始正文公开日一次。

## 6. 当前停止与独立复核权限

14入口的本次有限目录/失败和停止位置如上；17完整v1题摘已交root FIRST校准，随后只对已校准13项及ALERT补必要核心，VideoMemory只补决定准入的§3.3。原17候选/原评分/原Books及四中心隔离不动。新的机构/论文方向当前未授实验复现、Books采用或日级验收。

作者普通工作已收束：报告六部分单连续32候选表（原17逐字保留＋新增15）、逐项必要核心/采用权限与有限源停点、V3校验及限定diff-check通过；原§4前缀逐字保留。最终必要证据以[独立审计](independent-audit-20261007.md)为准：全部新增14论文加1机构、日期界限、具体owner/最终处置已核，PII实际POST通过；新增1整合/2已有覆盖/11仅报告/1中心争议隔离。上文“提案/待root”为作者阶段记录，不再是普通证据待办；当前仅待最终窄改后的六部分日级验收，不扩源/扩池/附件。
