# 2026-10-28 国际机构来源：暂停停点

窗口：BJT 2026-10-27 自然日。检查时间：2026-10-28 09:20 BJT（随后用户要求暂停，立即停止新检索与审阅）。作者：live1028_org。仅本文件 ownership；未写 Books、Report、State 或 index，未 stage/commit/push。

本次已独立重读 AGENTS.md、研究合同、Report 合同、统一入口、来源使用说明/每日组、ROADMAP 与 LEARNING_STATE 顶部相关暂停说明。不恢复 10-27 或历史任务。候选及代表排除已送唯一独核 live1028_review；尚未收到准入校准，不能标独核通过。

## 来源与实际停止位置

| 来源 | 已查入口、范围与观察 | 当前限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research index](https://openai.com/research/index/)实际可读，不是 focus 首页。首屏最新三个 Oct26（academic communities、Terra card、Terra product），后 Oct23 security、Oct21、Oct19、Oct7、Oct6；在日期已早于窗口的首屏停止，未点 Load more。此最新列表未见 Oct27。 | 不声称整个 OpenAI 全网零发布。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)的 Most recent（199 articles），Oct27两项：drug development、agents judgment calls；之后 Oct23 alignment assessment、Oct20、Oct16。两项均定点打开；agents核心与PDF必要方法/评价/限制已读，drug页已恢复但正文尚未读出。 | 首批准入与证据独核未完成；drug标题与目录说明明确AI for Science，可按暂缓范围排除，无需扩为Agent泛机制。 |
| SRC-GOOGLE-AI | [DeepMind News](https://deepmind.google/blog/)首屏从 Oct2026 到 Aug2026；实际打开 Genie4=Oct27、forest types=Oct22、antimicrobial=Oct15、on-device scam=Oct14，后项未入当窗。Genie4核心与限制全文已读。[Google Research Blog](https://research.google/blog/)当窗 Sleep Oct27已打开；另官方带trk入口返回不同缓存首屏（最新Oct23），不能用其否定已直接恢复的Oct27页。 | [Google Pubs](https://research.google/pubs/)可读但仅年份筛选（2026=433）而非Oct27日级清单；页面未含Sleep。日期查询 `?q=2026-10-27`不可访问。有界官方域日期搜索仅恢复Sleep/Blog，不构成完整当窗Pubs覆盖。Pubs日级目录精确隔离，不授零命中/无遗漏。 |
| SRC-META-AI | 原[Research](https://ai.meta.com/research/)0正文；旧 `/research/publications/`提示不可用。导航实际[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)恢复424行：首条Oct20 Learning to Program Retrievals、Oct19 Muse Glimmer、Oct14多个条目，之后混2019/2020等旧年并有Next，非可靠完整日级排序。[Blog](https://ai.meta.com/blog/)首屏最新Jul27/Jul21/Jul9等旧日。sort_by/page变体不可访问。 | 原目录未覆盖到Oct27，替代页混旧记录、缓存/排序不完备；不能写零发布。已作有界 `site:ai.meta.com/research "October 27, 2026"`、`site:ai.meta.com/blog "October 27, 2026"`、`site:ai.meta.com "October 27, 2026" model research`、`site:ai.meta.com/blog/ "Oct 27" "2026"`、`site:ai.meta.com "2026-10-27" research`、`site:research.facebook.com "October 27, 2026"`，返回旧索引而非具名本窗材料。停止重试，隔离完整Oct27目录缺口。 |

恢复外部目录的条件：可复查的官方Oct27日级记录/快照或具名当窗原始发布。只重开对应来源和材料；上述缺口不支持正面Coverage、Books或“无遗漏”。这是来源缺口，不把普通候选审阅待办改成外部受阻。

## 首批拟入选（均待独核，不是最终候选表）

### A1 — How AI agents shape experts’ judgment calls

- [官方事件页](https://www.anthropic.com/research/agents-judgment-calls)Published Oct27,2026；[官方PDF](https://www-cdn.anthropic.com/519c17a5d23a794e8b6d50a854048d0b61e0d73a.pdf)，29页。未发现页面撤回/纠错标记；未遍历历史。
- 准入命题：正确/错误型审核不能覆盖多种可辩护判断 → 随机分配Agent偏好产生专家分析选择偏移 → human-in-loop签字不自动成为独立判断证据。拟评分2+2+3=7；暂路由AGENT-WORKFLOW/PLATFORM-EVALUATION-SYSTEM，唯一owner须后续实际正文比较，尚无Books结论。
- 已读：Blog Study design/Results/limitations/meaning核心，PDF §3.1–3.6、§4.1–4.3、§5及§6开头。PDF方法与Table2实际核验，不只是摘要。
- 条件：61完成者中50使用Agent；11自行不用Agent，AI-vs-noAI非随机。固定Claude Code v2.1.220、Opus4.8 high effort；同一约一小时虚构农业合作社任务，分析师有因果推断背景但非农业领域专家。隐藏系统prompt随机配置五项lean（32配置分块平衡），鼓励诚实论证/证据冲突时改变判断，非指令欺骗。
- 主结果须区分：四分析选择的lean一致率86%是描述性；Table2 H1 pooled arm contrast=.72、95%CI[.60,.83]、195 trials，participant CR2聚类/Satterthwaite；将contrast解读为flip rate需no-backlash假设。H2 adjusted policy shift=.17、CI[-.06,.40]、单侧p=.069不显著，不用Blog54%/36%证明最终政策效应显著。H4 38例为post-treatment自选子集，条件解释；82%预测vs61%多数基线是in-sample探索，不作独立泛化结果。
- 自主noAI组完成快慢/错误比较存在自选、经验差，不能证明Agent因果收益。注册在17人已启动、4人drop后；作者声明未分析已收集数据，除计划披露的两例外。初始个人判断未普遍测量，不能从平均效应推每人受影响；强lean、单模型/单任务、领域外专家限制外推。双边论证、先询问人的观点等为后续设计建议，非已验证缓解方法。
- 剩余：独核准入；如准入则补足拟采用命题必要附件（特别注册两例外、A.3 lean prompt/A.4模型和排除/编码必要项，由具体采用命题决定），比较真实owner与相邻段，提出有限Books结论；不可宣称深入完成或已整合。

### G1 — Genie 4: A new generation of world simulation

- [官方Blog](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)October27,2026。发布研究预览给trusted testers；消费者/API扩大开放为后续计划，不写已普遍可用。
- 准入命题：单纯渲染与长程任务控制分离 → 文中披露Gemini3.8Flash持续观察生成帧、拆解目标、检查步完成并适应用户干预，以实时caption/text控制Genie生成 → 值得比较语言规划与感官生成耦合时的控制边界。拟2+2+2=6；路由MULTIMODAL-WORLD-MODELS，尚未比较Books。
- 全核心已读：four capabilities、Simulating complex events、Future Work、current limitations。Genie新增原生声音/实时对话；Gemini4Argon演示把步骤交错为caption控制Genie。该描述可支持有限架构/反馈接口，不支持内部模型结构、训练实现、bench或真实物理有效性已证。
- 文中自述短会话较连贯，但长时、多次复杂编辑、导航可出现视觉细节/object permanence漂移；物理交互、实时audio、空间精度与长期一致性仍待研究。示范视频与厂商描述非定量独立对照；没有公开控制消融/端到端运行配置，性能字段Not Disclosed，未实际运行/复现。不能照录reliable causality或泛化机器人收益。
- 剩余：独核是否具有足够具体增量（不是一般“规划+生成”术语组合），然后标准证据判断及真实owner比较。尚未评分定案/Books决定。

## 代表性排除与窗外线索

### G-N1 — Sleep Blog：旧家族再介绍，不迁首次公开

[Oct27 Blog](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)核心说明已读：扩容低秩MoE记忆块、GKD/LTI知识巩固、临时记忆reset、random expert dreaming和数据选择。其链接[原稿2606.03979](https://arxiv.org/abs/2606.03979)实际题名Language Models Need Sleep；v1提交Jun2，当前v2 Jul10，Comments明确2025年9月OpenReview已有版本。完整AB已读，consolidation/upward-distillation、GKD+RL imitation、Dreaming均已在原稿，Blog无具名实质修订事件。Oct27机构介绍不能当新论文首公开或仅因主题相关再次评分。没有重读旧Methods，未声称历史审阅已完成；有更早归属需恢复时只定点核该家族，不在本日扩历史任务。

### A-N1 — Drug development

[官方页](https://www.anthropic.com/research/early-progress-drug-development)，Research MostRecent Oct27，目录描述六家新药机构合作。标题/说明明确AI for Science当前暂缓；已打开原页但正文未进一步读取。未因出现Claude/Agent把药物领域应用重新引入主线。无已见纠错/安全/重要修订信号；不评分、不进入Books。

## 暂停后的准确续跑位置

用户要求立即暂停后只保存本文件，没有追加研究。已送首批校准，等待独核记录实际结论；本文件不得被解释为校准通过。恢复需用户明确授权；先重读当前日适用合同与本文件，接A1/G1未完成层和具名目录缺口，不重新做已有效的发现/日期/必要核心阅读，不唤醒10-27或历史游标。唯一写入是本文件。

## 明确恢复后的补缺层（2026-10-28 14:48 BJT）

root已转达用户明确恢复本日；上方暂停块为历史停点，不再限制本日执行。重新完整加载AGENTS、研究/Report合同、统一Prompt、来源使用/每日组、ROADMAP、ORG与唯一REVIEW；开始Books比较前加载PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE及State顶部本日路由。没有恢复10-27或历史、没有写Books或共享文件。

### 来源恢复结果

已有OpenAI index、Anthropic MostRecent和DeepMind日期段有效，不重跑已读层。GooglePubs/Meta再做一轮有界补检：`site:research.google/pubs after:2026-10-26 before:2026-10-28 "2026" language model`、`site:ai.meta.com/research after:2026-10-26 before:2026-10-28 model`、`site:ai.meta.com/results/ "October 27, 2026"`。搜索仍返年份/缓存而非完整日级目录；GooglePubs返回PLD/SKILL.state/PROMPTS等只有2026年份的宽线索，不建立当窗候选队列，不将搜索时间过滤当公开日期证据。Meta官方Research带trk版本可恢复WHAT'S NEW（Oct12 MuseWonder、Sep2 Spark1.3、Aug5 Code/Spark1.2、Jul9 Spark1.1）；这是部分发布入口恢复，不证明Oct27Pubs目录完整。停止扩查，继续精确隔离上方两项日级目录缺口，不支持零发布/无遗漏。必要具名材料未受此目录缺口阻断。

### A1 — 必要证据补足与Books提案

唯一reader消息已独立通过A1准入2+2+3=7；其PDF深入证据/本提案仍待单独核。恢复了官方Blog当前同一PDF链接（直接URL一度失败、从Blog Read the paper成功），精确题名为 **Who’s Aligned to Whom? How AI Agents Shape Experts’ Research Judgment Calls**，无显式v号，采用官方Oct27链接版本，不称arXiv版本。原§3–5/Table2有效层复用。

新增必要实际阅读：PDF A.1/A.2筛选及人口，A.3完整共同lean前言与d5逃逸条件，A.4缺失排除、统计与disengagement敏感性，A.5五项判断依据。A.3要求忠实数据、证据明确相反则改变立场；d5 estimate反向时改提一年extension。这是prompt设计，不是已证明每次都无误导。A.4不明确/冲突trial仅排该decision；H1 195而非200，因此不能把所有五项等同处理。删除idle>50%的3sessions后H1=.74、CI[.63,.85]、184trials；这支持主分析对该特定敏感性不脆弱，不等处理所有选择偏差。A.5 outcome/identification/estimand/weighting有各自可辩护前提，确实不以唯一正确答案定义lean选择。

注册原件[OSF t3q59](https://osf.io/t3q59)定点不可达。本文不采用“严格前瞻预注册”或无选择偏差保证，只使用原文披露的随机lean试验与主效应的有限反例；保留§3.6已在17人启动后注册、所称两例外未核的限制，不因此把其他已可核方法改成全项受阻。无恢复全部注册文件/全部遥测的需要。未独立运行代码、未复现实验。

真实owner比较：完整读Ch81 `## Human-in-the-Loop`（原894–921）及直接前后：上方为工具effect/物理取消证据，下方是显式ask/takeover/handback与AI-set遗漏风险。它已经说明approval身份/版本/有效期、多人职责分离和集合包含真值不保证人选对；但尚未解释**没有唯一正确答案时，合法人类签字也不证明判断独立于Agent的预设偏好**。Ch80开篇feedback independence、Ch82开篇角色共偏不能替这份human-agent证据；Ch66开篇评估合同不接管Workflow中的人工决策权。唯一owner为`AGENT-WORKFLOW` Ch81，不新建结构或重复写Ch66。

拟最小正文（插在“Action 在等待期间若发生变化，旧 approval 失效。高风险任务还可使用双人批准或职责分离。”之后、“真实用户交互还要求区分...”之前；待reader逐字PRE，尚未保存Books）：

> 授权身份正确，还不证明人的判断独立于 Agent。若同一证据允许多种合理的目标、估计对象或分析假设，检查答案有没有错不能识别究竟是谁决定了这些前提。[一项受限随机偏好试验](https://www.anthropic.com/research/agents-judgment-calls)在要求 Agent 诚实论证的同时随机指定其立场，仍观察到专业分析师的分析选择随之偏移；最终签字及事后自称“我的判断”因此不能单独认证独立审查。这不证明任意 Agent 都会产生同等影响：试验人为强化偏好，仅用一个模型和任务，最终政策推荐的主估计亦未显著。需要保留人的判断权时，应另记录关键判断点、采用的假设及其来源，并给人形成意见和核对替代方案的时间；这些是由反例提出的设计要求，不是已验证的缓解方案。额外审查增加人时与交互成本；无法建立独立判断时，保留明确的判断委派与责任归属或另行复核，不把形式 approval 当作认知独立性的证书。

拟唯一marker：`SF-ANTHROPIC-20261027-JUDGMENT-CALLS`。拟Review note要点：官方Oct27PDF §3–5/Table2/A.1–5、2+2+3=7；195trial participant-cluster H1 arm contrast=.72 CI[.60,.83]，flip interpretation需no-backlash；H2 adjustedCI跨零；38例post-treatment/82% in-sample/noAI自选均不作额外因果主张。晚注册两例外未独核、固定Opus4.8/单领域外任务、强lean/编码限制保留；无代码/复现/已验证防御声明。根节点是否写入及实际POST须唯一reader/root后续落实，本文件不预签。

### G1 — 标准证据与具体已有覆盖提案

唯一reader已确认有限接口候选2+2+2=6，末限制段独核待其记录。官方披露的实现分工支持“Flash观察生成帧、拆步、检查并重规划，将控制条件交给Genie”的架构事实；不披露训练/同步接口、独立控制消融、horizon与质量/费用测量，因此不给可靠因果、持久state、物理正确、机器人迁移或净实时性结论。所有performance配置Not Disclosed，不适用数值混比；没有外部benchmark缺失就否认公开接口事实。

已实际比较唯一owner `MULTIMODAL-WORLD-MODELS` Ch25：

- `#### Reason-then-Render：Transition Token 是 Proposal，不是物理定律`原540–548：reasoner以当前observation/action intent提出中间transition，renderer生成future；完整identity和generation质量不替intervention/闭环证据已明确。它承载本次语言推理与感官生成的分责，不把Genie的caption臆称transition-token实现。
- `## Control flow 与数据流`原1135–1156：观测→belief→rollouts→policy/controller→新观测的分工，以及imagined branches不是事实提交；其后分块renderer段明确派生视觉历史不拥有显式物理真值。Genie观察自己的生成帧可形成内部调整，但不能凭其闭环名称把帧当外部观察。
- `### Open-loop imagination vs closed-loop correction`原1365–1371与开篇原14/18–36：horizon/误差、感官生成和action-conditioned可校准后果的区别已具体存在。Ch24开篇只拥有生成路径、Ch26开篇拥有真实controller/安全执行；二者不被产品扩模态改写。

据此提 **已有覆盖/No Change**：采用的长期命题是推理/renderer分责、预测/真实观察区分及短horizon局限，已有上述原文承载；本次native audio/实时对话和trusted preview是版本能力/发布事实，未披露足以修改这些长期机制的实现/对照，不为产品名增段。此为已准入候选的证据与Books处置，不改判排除、不降分、不声称Genie实现等同既有transition-token模型。待reader核NC具体位置，尚无最终处置通过。

### 唯一独核已返结论（仅同步实际结果）

`/root/live1028_review`实际独核A1 PDF页5–14方法/Table2/结果/讨论限制、页17–19 A.3/A.4/A.5，确认缺失/敏感性、诚实约束与d5逃逸条件；OSF例外未核作为不授严格前瞻保证的限定，不阻有限反例。它又实际顺读Ch81完整HITL及直接两侧，**上方最小正文及note命题PRE通过**。由root协调窄位并实际写入后，仍须唯一reader实际POST；本作者没有写Books，也不将PRE计为实际整合完成。

同一reader实际读Ch25 Reason-Render/Controlflow/Openloop与两侧，**G1具体已有覆盖/NC通过**；保原2+2+2=6/标准证据范围，不声称同Genie实现，不为native audio产品事实添段。G1此层已可由报告作者同步，不能把A1尚未写入/POST隐藏为整批完成。

### A1实际保存，待唯一写后复核

root随后fresh授权本作者唯一Ch81窄位。写前再次读当前HITL完整直接两侧与Review notes尾部，确认无本family现存重复；按批准最小正文实际apply_patch插入并追加唯一note，没有改前后原段。保存时正文/marker在Ch81 **906**，本人note在 **1752**；已实际顺读完整新增、直接两侧和本人note，限定`git diff --check`通过。已送唯一reader实际POST，未预签POST或整合生效；没有写State/Report/index、无stage/commit/push。

唯一reader随后实际完整读906正文/全部直接两侧、1752本人note/marker并核working diff4增0删及diffcheck，**A1实际POST通过、整合生效并可释放本窄位**；G1 NC仍有效。仅同步真实结果，不预DAY。国际机构普通研究/Books待办0，GooglePubs/Meta日级目录与OSF限定仍按上文隔离；完成本ownership不等本日全源/全日报完成。root另授ARXIV_MULTI.md有界主题发现，另存第二ownership，不混入ORG或重开本机构有效层。
