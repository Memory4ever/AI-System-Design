# 12/12 独立准入、证据与日级验收

复核者：Popper（用户指定的独立非作者agent，不是作者Plato或Books写入者root，不使用共同chat ID）。
结论：未通过

2026-10-02T19:51:08+08:00。只验ready的[2025-12-11T09:00:00+08:00,2025-12-12T09:00:00+08:00)。逐日重读合同/每日源/ROADMAP/state，实际读本日四份原始材料及晚恢复Google记录。确定两家族的限定准入/必要证据通过，日级仍普通A/B/C三组；历史缺失不一律算ordinary。

## 晚恢复Google：实际source与owner

两篇[Interactions API](https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api/)与[Deep Research / DeepSearchQA](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/)完整核心、原始HTML JSONLD本次重新取得HTTP200。NewsArticle.datePublished均2025-12-11T17:00:00+00:00，换算12/12 01:00BJT落本窗；modified分别17:12:20.625361/17:09:48.161070，article:published_time仅12/11标签，不用后两者替代published。

API 2+2+2=6及标准完成通过，采用只限history/typed interleaving/background loop职责。实际Ch84 52–96已分KV/Context/AgentRun/Memory、服务端回读、typed Item/Turn、terminal evidence；Ch83 100–108五轴与245–257远端对象映射，Ch82开篇保留执行/委派分工。不是“都写Agent”主题去重；该有限设计差额已有具体覆盖，No Change合理。博客没有授durable workflow、exactly-once、幂等、取消回滚、retention或继承授权，cache只是可能，不采用性能保证。旧generateContent仍适合stateless/生产，beta可breaking，当前后续文档不反推2025实现；未运行API。

DeepSearchQA 2+2+2=6，知识缺口触发深入必要证据，通过但Books未落实。实际[16页技术稿](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)首页12/11、§2三人独立gold/冲突仲裁与时锚、§3集合与zero-shot语义judge、§4 metric divergence/失败及§5.1实际对读。逐题P/R/F1再平均不等strict fully-correct；final answer-set equality、missing/extraneous/无交集分责是本次受限测量增量。只有结果集合不能辨可靠过程与幸运，静态源仍会删改。只采用协议与边界，不采rank、参数/预算因果、成本优势或后来结果；博客66.1与稿81.9不是同一成功率。当前PDF与发布事件对应但未认证历史字节冻结，工程论证不依赖表中数值。

### 普通A交root：实际增量、写入位置与POST

唯一owner [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) PLATFORM-EVALUATION-SYSTEM。实际读890–928 Context/FACTS/RAG、1078–1095 expected-fact inventory及Ch65/67开篇，并定点搜索答案集合/strict set/extra-items。RAG 910–912拥有“必要信息→可替代chunk”覆盖，inventory拥有expected facts缺项；都不等final entity-set全部正确且无额外项。4633的其他高熵枚举review note不替代本次实际owner段落，不能借目录/关键词认完整覆盖。

请root在RAG前两自然段后、exposure/copy baseline前（当前914之前）自然补GOOGLE_LATE_RECOVERY的最小差额：最终输出去重/同义匹配/截止时刻是scorer合同，分missing、extra、无交集与strict equality；F1是部分质量诊断，不证明任务完整交付或开放搜索穷尽。保留原retrieval信息覆盖与exposure诊断，不覆盖它们；保留gold穷尽/语义judge/网页变化复核成本、无trajectory边界、单答案低成本exact-match共存，gold不可穷尽时收窄/Unknown。工程分账是本书推断，不虚构stop算法。

原始必要支持§2 Quality Verification、§3.1–3.2、§4 Metric Divergence、§5.1。绑定原官方博客与该技术稿，别绑定排行榜或数值优势。root实际写入后交精确位置，Popper只做非写入者POST（本会话无该Books写权限）；作者同步报告实际Books决定。API已有覆盖不用重复写书。不等其他日期修复才落实这一个准备好的家族。

## 133题摘与有界负侧校准

原表133项精确v1的原站可读题摘均本次重新取得HTTP200；10363/10365输出缺片单独重取，10522源摘要尾缺失不补造。题摘层有效，不等全文Evidence、first-public或133确定候选。本次实际原始列表CL326–375（09440→10865）、DC76–100（10236→12476）、CV1076–1175（09383→10416）；没有独立重扫LG/AI/AR和其他页，不扩全池。

在这三段按模型/训练/评价/安全机制边界取得17项额外题摘，15项潜在需补（含已误关10102）。下列全部为精确v1；原始地址统一 https://arxiv.org/abs/2512.<短ID>v1，未授日期/评分/Books：

| 短ID | 实际潜在信号与限制 |
| --- | --- |
| 09636 | MentraSuite v1心理评价与跨维推理/答案准确性分账、SFT/RL；当前目录名MiraMind不替代v1，不因心理领域直接排除 |
| 09730 | Interpreto分类/生成解释目标、activation granularity与logits/softmax耦合接口；必要§2/4/5/6核过，不自动信API统一即解释忠实 |
| 09854 | social bias PRM在best-of-N与顺序引导之间、跨语言公平/性能取舍，非成熟PRM标签关闭 |
| 09910 | continual LoRA梯度约束与gate-free线性专家混合，跨任务遗忘/正向迁移条件未证 |
| 10195 | AutoMedic QA到multi-agent对话与CARE准确/效率/共情/鲁棒性评价，局部医疗负载不等临床标题边界 |
| 10430 | Tpro2混合reasoning/tokenizer与适配EAGLE，版本/调用性能未独立证实，不以型号名入选 |
| 10734 | 数据层de-bias成功但模型层bench偏见未一致下降，训练材料与模型评价不等价的negative |
| 10443 | clustered FL分层multi-teacher蒸馏与edge/cloud通信/个性化，非LLM不自动范围外 |
| 09665 | OxEnsemble低数据fairness在各成员约束后聚合与held-out复用，理论/公平保证未核 |
| 10102 | 层级tracking父子关系identity-switch指标、语义part与多pass/GT首帧初始化的评价/成本边界，不能“只有数据集”关闭 |
| 10209 | 中间feature coding的edge/cloud split与codec任务质量/带宽取舍，不从feature载荷宣称隐私保证 |
| 10230 | VCM/FCM与既有inner codec复用的任务相关性能差，标准综述身份不自动排除设计反证 |
| 10252 | LKVA、Gated Delta Rule中间memory与局部多尺度融合的容量/效率选择，echo负载不自动排除通用memory机制 |
| 10316 | text-guided prototype与frozen foundation结构蒸馏补弱监督定位，pathology不是独立关闭理由 |
| 10408 | 视频级分类到hate temporal localization及弱监督MIL/跨模态时序融合，安全定位不是只看片段总分 |

[10102正文](https://arxiv.org/html/2512.10102v1)实际必要§1/4/5.3/Table3：父object变更计入H-IDSW；高image segmentation不等跨帧关联，VOS首帧给GT会抬高结果且多次推理。撤销作者“新任务/库存、无独立机制/反证”的摘要缺省关闭；恢复潜在，不采用privacy guarantee或普遍性能。 [09730必要正文](https://arxiv.org/html/2512.09730v1)分类与生成目标粒度、logits默认及concept fidelity/stability边界保留，不机械以工具集合关闭；没有源码/性能复现。

[10440正文](https://arxiv.org/html/2512.10440v1)实际§III/IV给“向Claude/GPT4加内层attention”等主张，却没有可核模型版本、内部访问路径、匹配实验或可复算实现；表格gain没有对应独立控制依据。这里关闭的是未建立可验证项目设计增量，不以KG成熟组合/缺新算法为理由，也不采其收益。[10080精确PDF](https://arxiv.org/pdf/2512.10080v1)实际必要§5/7/8是随机生成与溯因外观的哲学解释/既有研究举例，没有本次独立设计机制或新验证；限定贡献前关闭，不采“LLM没有理解”的通用事实结论。

两个DC晚段locator11200/11306也实际读题摘，只用于核主题停止后仍有相关线索，不宣称ID代表证明窗外、不把作者明示的晚段locator变成12候选队列；后续归属由相应日独立处理。明确范围外临床诊断/传统ID/评论仅title，不称完整题摘负样本。

### Replication安全反证与普通B

本次实际读取[Anthropic replication](https://alignment.anthropic.com/2025/auditing-mo-replication/)Introduction/Replication procedure、reward/redteam/audit非assistant与讨论必要核心，未读全部附录。Llama3.3-70B SFT外推较差→用DPO、adversarial DPO隐藏目标、旧非assistant攻击审计失灵等是潜在安全/设计反证；局部replication不等无增量，SAE多义信号也不等可靠审计。页面12/12日标签不证明09:00之后，更不能只由该标签跳到13并放弃本日贡献校准。当前没有精确first-public，保留潜在及日期不确定，条件路由而不是证明窗外；不评分/Books。

**普通B**：作者在SOURCE_SCREEN及README §1/2/5补上述15项精确潜在身份/边界、10102关闭纠正与Replication安全信号/日期关系；同一有界段共同遗漏理由受影响集合做有限补核，不全读所有正文。SOURCE_SCREEN表首项仍字面“+|”，由作者一并纠正。本次独立原始校准可以定点复用，日期未知不要求所有题摘再次全读或无期限求firstpublic。修的是未做筛选/错误关闭的普通差额，而非把所有外部日期变普通。

## GPT5.2必要证据与实际RSS：普通C

实际[发布原文](https://openai.com/index/introducing-gpt-5-2/)核心、[27页精确card](https://cdn.openai.com/pdf/3a4153c8-c748-4b71-8e31-aecbde944f8d/oai_5_2_system-card.pdf)必要§3.3页5与§3.7页8–9/Table6、Ch66 14–112及Context段对读。厂商缺图严格格式/宽松格式与生产traffic不是同分布；已知prompt-injection训练split不证明未知攻击泛化，coding从零实现/虚报分类边界保留。局部反证确能改变评价切片，不因非整体性能提升关闭；仍未授本窗、评分或Books。MRCRv2修正GT/version切片保留，compact endpoint未披露机制不编造算法；science/math按暂缓范围关闭。

官方[RSS](https://openai.com/news/rss.xml)本次Mozilla UA实际HTTP200，XML解析精确link匹配，不靠搜索摘要：
- Introducing GPT-5.2：link /index/introducing-gpt-5-2，pubDate原值 Thu, 11 Dec 2025 00:00:00 GMT。
- Update to GPT-5 System Card: GPT-5.2：link /index/gpt-5-system-card-update-gpt-5-2，pubDate同值。
- science/math对应条目为 Thu, 11 Dec 2025 10:00:00 GMT，不能代替前两项时间。

前两原字段换算为12/11 08:00BJT，按此字段在本窗前。不能继续写必要RSS替代全失败；也不能直接将00:00字段回填27页原稿first-public。原值是否精确可访问时刻、当前RSS与旧artifact是否同事件的精度/版本关系未核；日标签本身不能补造小时。当前[card入口](https://openai.com/index/gpt-5-system-card-update-gpt-5-2/)转到后续Safety Hub，新增CoT monitorability不是27页旧稿内容；当前hub仅日期标签未得另一精确timestamp。原release/card HTML Mozilla依然403，不以此推RSS不通。

**普通C**：作者同步实际恢复的RSS字段/换算与条目→原稿关系，撤回笼统访问失败；若必要有限入口不能确证时刻精度或旧稿关系，将该具名历史边界隔离安全终态并留精确重开点，允许关闭本窗处理，不要求无限恢复时间。不得机械授12或改作11确定候选；仅给11恢复线索，不盲审别日未知新事件。GPT5.2没有Books写入，条件草案仍不采用。

## 完成边界与机器

本次普通A root实际Books/POST，B潜在/负侧及有限共同理由修正，C RSS恢复/精度与报告同步。最终§5应明确“终态保留项”、不支持正面证据/Books/无遗漏断言与定点重开条件，不能作者“普通0”或机器通过代替内容核。所有真正穷尽日期/历史入口仍可安全终态，不是Coverage/Evidence通过或零事件。未全量重放14源查询、全读133+15正文/代码/附录、认证所有first-public、运行模型/API；两个Google候选仅所列采用命题通过。Books只提出准入条件，未验新写入。

本次补丁仅12 README metadata/§6及本记录，不改§1–5/Books/index/state或13–16。09仍C一组，10内容A/B/C/D已闭但§5终态措辞同步一组，11仍四组；不用等待09差额推进ready12。机器结果更新于下。

2026-10-02T19:54:57+08:00机器实际结果：本日V3格式/本地链接校验通过，09–12授权文件限定diff空白通过，12验收补丁前后README §1–5逐字一致。机器只证接口/一致性；语义结论仍未通过及A/B/C三组。本次未改Books、index/state，未stage/commit/push。

## 给root的DeepSearchQA最小自然段写入方案

唯一owner：`PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`。本次实际重读当前RAG开头两段`required information → 可替代的 supporting chunk 集合`及其gold审计/回退。精确插入位置是第二段“这张映射本身也要审计……”之后、“检索答案的提升还要先扣除已经暴露给模型的输入信息”之前。与现文差异：现文检查必要信息/替代支持是否取得；新增检查最终规范化答案集合是否漏项、夹带额外项，不把检索sufficiency、F1或上下文copy诊断当全部答案完整。后文presence/absence inventory也不等最终实体集合严格判定。Ch65调度与Ch67运行监测不是owner。

必要原文：[官方发布](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/)DeepSearchQA核心及[16页原技术稿](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)§1–3、§4度量分歧/失败、§5.1限制，均已实际读。gold由独立研究者交叉研究/冲突处理，绑定时间；逐题precision/recall/F1再macro平均，严格全对与漏项/额外项/无正确项分开；自动matching与仅看final answer的限制保留。当前PDF不认证2025原始字节冻结，采用只限与发布博客匹配的定性协议，不搬后来排名、阈值/数值，也不推同模型同预算因果增益。

建议两自然段，由root自然融入并绑定独立家族（建议`SF-2025-GOOGLE-DEEPSEARCHQA`，先核无重复）：

> 取得全部必要信息，仍不等于最终答案完整。要求列举多项事实或实体时，应在固定范围与时间截点下保存规范化的gold集合，将“没有正确项、漏项、夹带额外项、完全一致”分开；逐题precision、recall与F1保留部分正确性，但不能替代严格完整判定。[DeepSearchQA的公开协议](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/)采用这一分账思路。实体去重、同义词和匹配器版本也须进入scorer合同，避免把检索召回率或较高F1当作最终集合完整。
>
> 这类gold需要交叉研究、冲突裁决、时间绑定和人工抽检，自动judge及网页变化仍可能制造错标；只检查最终集合也不能区分过程可靠与幸运答对。单答案任务继续保留简单exact-match基线；开放世界无法可信穷举时，应缩小问题范围和截点、将完整性标为Unknown，再保留证据充分性与claim-level核验，而不是从benchmark协议推得搜索已穷尽或在线停止保证。额外研究和judge成本也须与任务收益一起验收。

Books只有root写，写后Popper核实际source→两段→前后/Ch65/67再给真实POST。交Plato逐项：B把15项恢复潜在及Anthropic replication必要负侧校准同步，并完成同有界段共同理由扩查，修SOURCE_SCREEN表首行`+|`；C同步实际可读RSS两条00:00GMT及旧card关系/精度终态，不继续说所有RSS失败、不硬授11/12；A实际写入/POST到达后同步§1/3/4/5与来源家族。最终§5显式终态、否定采用、定点重开。API候选现有责任覆盖的No Change已经按实际owner核过，不要求因邻近DeepSearch新增而再写一遍。09/10差额不阻断本日继续执行。

## DeepSearchQA真实非写入者POST

复核者：Popper（独立于作者Plato与Books写入者root）。
结论：通过

检查时间：2026-10-02T20:24:04+08:00。本结论只授`SF-2025-GOOGLE-DEEPSEARCHQA`两自然段POST，不授12日完成。实际重新读取官方发布DeepSearchQA核心与当前16页技术稿§1–3、§4度量分歧/失败、§5.1局限；实际对读Ch66新两段、前后required-information/gold审计/exposure诊断、相邻Context/FACTS及Ch65/67开篇。新段区分部分P/R/F1与strict answer-set equality，gold需交叉研究/时间绑定/冲突处理，匹配器、网页漂移与仅final-answer评价的局限明确。Unknown、单答案基线及claim-level回退是工程推论，不冒称原稿已提供在线穷尽保证；未采用排名、成本或架构因果收益，不认证历史PDF字节冻结。未运行Agent。

只改用户授权的本新增来源末注POST状态，不改Books正文或其他末注。Plato同步§1/3/4/5真实POST即可，无需root再写两段。最新FEEDBACK_BC已到：原15项恢复及Replication/RSS具名安全终态保留，新增26项精确v1潜在由Popper继续实际原始校准；日级暂未通过，不把所有历史日期隔离当普通待办。机器检查稍后据实追加。

## 新增26项原始校准及实际POST同步闭环

复核者：Popper（独立非作者、非Books写入者）。
结论：未通过

检查时间：2026-10-02T20:36:38+08:00。FEEDBACK_BC新增26项09444/09563/09666/10110/10148/10453/10780/10987/09423/09446/09580/09583/09617/09626/09633/09847/10095/10244/10262/10284/10293/10314/10321/10340/10352/10384均实际取得原站HTTP200精确v1完整可读题摘，逐项潜在成立，不授first-public/评分/Books。10780只保留roman/native script的意图识别不等最终分类反证，不采临床部署误差预测；09626单步RNN输入已包含短时间窗kinematic特征，不采“时序无用”；10244既有SSL接VLM的flat softmax导致阈值下未标注数据零使用，不能成熟组件关闭。其余按作者具体表示/监督/调度/评价条件潜在保留，没有仅因病理/场景排除。

实际重读最新12 README §1–5，root DeepSearchQA两段/来源家族/20:24:04真实POST已同步，原133有效层及15恢复不重扫。Replication必要附录A/B/C在13日原文实际核验，身份/命题未变可复用；RSS精度/27页关系安全隔离合理。SOURCE_SCREEN首行`+|`已修。实质A/B/C闭；仅剩Plato在§5既有终态否定句明写“不支持正面证据、Books或无遗漏断言”供完成态校验，不改判断、不重扫、不写Books。现§5“不正面采用/不支撑”意图明确但与11相同无法满足完成态解析，metadata暂进行中，待这句到达立即日Gate。Books新增末注之外的全文过滤哈希补丁前后相同，12 POST补丁前后§1–5逐字一致；不认证其他会话后续全文不变。

## 最终日级独立验收

复核者：Popper（主线程委派，独立于作者Plato与Books写入者root）。
结论：通过

检查时间：2026-10-02T20:46:57+08:00。用户明确授权后，仅将§5既有终态否定句收束为“不支持正面证据、Books或无遗漏断言”，未改变潜在判断、日期归属或Books决定。此前实际内容核验与26项原始校准继续有效，普通差额0；metadata完成，§6记录真实独立身份、范围、样本与未检查边界。完成态V3及本地引用校验实际通过，限定diff空白检查通过；§1–5除上述唯一授权措辞外与补丁前快照逐字一致。未重扫、不改Books正文/index/state，未stage/commit/push。真正穷尽的首公开隔离保留，不授Coverage/Evidence通过、零事件或无遗漏保证。

2026-10-02T21:00:21+08:00用户追加窄授权后，仅同步§5交接段的旧“待非作者新增题摘校准与日级复核”及同段“日Gate”措辞为实际已通过/见§6。未重开未变证据、未改变潜在判断/日期/Books；全文件与补丁前快照除该交接段的两处状态短语外逐字一致。完成态V3/本地引用及限定diff空白检查实际通过，普通差额0和日级通过保持。
