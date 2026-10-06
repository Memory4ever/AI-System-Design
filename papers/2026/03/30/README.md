# Daily Research — 2026-03-30

**规范：** V3
**窗口：** 2026-03-29T09:00:00+08:00 ～ 2026-03-30T09:00:00+08:00
**窗口说明：** 用户授权只补已有 Daily 遗漏，保留原窗口、候选日期/评分与连续 §4；旧完成声明不替代本轮验收。
**补充窗口：** 2026-03-29 ～ 2026-03-29
**冻结候选日期：** [本日补查前档案](../_sources/daily-20260330/baseline-before-supplement-20261012.md)
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-12T23:29:19+08:00

## 1. 结论

本日按当前合同独立重建，未确认可以完全落在窗口内的候选，因此确定候选、证据采用和 Books 新增均为0；这不是“当天没有有价值研究”。有限发现得到133条跨查询命中、116个唯一题名线索；其中61份精确v1的完整题摘已读，5项明确不满足贡献门槛、5项是4月公开的窗外线索，其余51项仅是日期或准入仍待核的潜在材料。它们没有被计为51个有效贡献或已完成证据审阅。

另有 OpenAI 确认落窗的应用公告，核心说明不提供新的模型或系统判断，贡献前关闭；Qwen3.5-Omni 的动态文本/语音对齐值得核验，但同一官方条目的日期字段冲突，隔离而不强选日期。四组必要历史目录切片也单列限制。作者的有限收集与筛选及两位非作者最终验收已结束，普通待办0；不沿用旧443项分母、评分或完成状态。[旧报告原证据](../_sources/daily-20260330/V3_LEGACY_REPORT.md)保留，不作为当前准入依据。

以上为保留的原研究层。本轮仅补03-29完整自然日，确定新增0，原0＋新增0＝候选0、Books新写0；这不等同于所有潜在材料已有覆盖或No Change。本轮具名新检查是OpenAI原页March29应用公告，完整核心仍不足贡献准入；arXiv在该北京时间自然日无常规公告槽，不把Submitted反填公开。14源的有限日期切片与必要历史限制已回对补窗，root非补充报告作者完整六部分DAY通过，普通待办0。详细执行与未证明范围见[本轮补查及实际DAY](../_sources/daily-20260330/SUP_WORKING_STOP_20261012.md)。

## 2. 来源覆盖

本次只处理14个每日来源；没有扩大到每周来源。下表保留原窗依据，补窗实际新检查与逐源回对见[本轮有限记录](../_sources/daily-20260330/SUP_WORKING_STOP_20261012.md#有限来源与复用边界)；原实际入口、原字段与停止依据见[非作者来源核查](../_sources/daily-20260330/V3_INDEPENDENT_DAILY_SOURCE_CHECK.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS当前1242项的邻接原时间；Disaster Response 为03/29 22:15 GMT，即03/30 06:15+08；原文核心29～56行已读 | 已检查 | 当前可见时段，不保证全历史目录 |
| SRC-ANTHROPIC | Research实际9个March publishedOn字段，Mar31及24/23/13/6/5均窗外 | 已检查 | 目录字段检查，不声称窗外全文审阅 |
| SRC-GOOGLE-AI | Research March首12卡、DeepMind第3页6个March卡跨窗口下界；pubs首1～15/11569仅year/title | 受阻 | H1：仅publications本窗首次公开日期切片 |
| SRC-META-AI | publication实际0～369行非日期排序；Blog第1页10项、第2页12项，SAM3.1 March27更新对本窗明确在前 | 受阻 | H2：publication本窗日期切片；不继承29日SAM日期缺口 |
| SRC-QWEN | retrieval API40项title/id/extra.date；目标Omni条目extra.date与同条目content元字段、可见日期独立对读 | 受阻 | Q1：March30与January7冲突，不能选其一作为首公开 |
| SRC-DEEPSEEK | 原页公开数组实际16 News、31 Research；News Apr24→旧Dec，Research Jun24→Feb25夹窗 | 已检查 | 当前两个数组，不把环境当前日期当第17条发布 |
| SRC-MOONSHOT | Kimi当前19项有日期Research，Apr20→Feb9夹窗 | 已检查 | 仅当前19项，不保证机构全史 |
| SRC-TENCENT-HUNYUAN | 正确生产POST renderType0/pageNum1/pageSize20，totalNum9/list9；display Feb13→Apr22，publishedAt无March行 | 已检查 | 两种原日期不互代首次公开，未扫描旧论文全文 |
| SRC-ZAI | 官方Research15项日期Mar15→Apr1；release16项日期Feb12→Apr7夹窗 | 已检查 | 当前两段目录 |
| SRC-BYTEDANCE-SEED | type1 token20返回18/82、token40返回20/82；原日期Mar25T16Z→Mar31T12Z跨窗；type2 token0返回14/19，Feb15T16Z→Mar31T16Z | 受阻 | H4：未返回身份/日期及返回数量差额，不扩大82项全文队列 |
| SRC-BAIDU-ERNIE | 首10项有日期卡片Apr15→Feb6跨下界停止 | 已检查 | 当前有限目录段 |
| SRC-XIAOMI-MIMO | Paper8项Jun29→Mar13夹窗；Blog15及More没有必要日期 | 受阻 | H3：仅可见Blog/More对应本窗的原日期切片 |
| SRC-MINIMAX | 当前HTML12项有日期卡片May26→Mar18；AgentTech官方原.md仅May13行 | 已检查 | 不展开无关Guide或全历史目录 |
| SRC-ARXIV | 四个项目主题查询Submitted UTC03/26 18:00～03/27 18:00，start0/max50/升序：5/5、43/43、13/13、50/72；agent/eval再一页start50/max25返回22；61完整精确v1题摘 | 受阻 | Submitted不是首公开；51潜在材料的公开上界跨03/30 09:00；分类入口已恢复但本窗公告段未得，不授全学科召回 |

补窗03-29的自包含差额：OpenAI fresh RSS1287项邻接条目为03-28和03-30（显式GMT换算）；原页只标March29，按官方日保留线索并读核心后贡献前关闭。Qwen fresh API4781799B的March extra.date只有03-19与03-30，Omni原字段冲突不变。其他源复用本日原有限March日期字段：Anthropic31/24/23/13/6/5、Google31及26/25/17/10/3、Meta27/26/11/10明确无可见03-29；DeepSeek两个数组、Kimi19、Hunyuan9/9、ZAI两段、ERNIE首10、MiniMax12均夹补窗，按各原停止位置结束，不把当前可见列表授全史保证。MiniMax AgentTech旧May13快照只证明当时可见行，root本轮同官方入口实际见3条Sep/Oct，没有03-29历史段；H5隔离该必要datedslice，不把这3条扩为研究队列。Seed两类有限返回和MiMo8 Paper也回对补窗，无可见落日项，H1～4必要历史slice仍隔离为03-29及原窗的覆盖限制。arXiv官方Sun～Thu Eastern公告制度在03-29北京时间无常规槽；本轮cs.DC月表skip300/show50原GET恢复84203B、Total346/301～346，仅核月header/日期信号，没有逐日公告header，不称46完整题摘，不建月库队列。本轮无新按需触发。

主题与分页原值见[四查询](../_sources/daily-20260330/V3_THEME_DISCOVERY.json)、[agent/eval尾页](../_sources/daily-20260330/V3_THEME_TAIL_TITLES.json)。按DST的官方availability，Sun03/29 20:00 EDT即本日08:00是这批提交最早可能的常规公告槽，不是逐篇确定公开时间；不把周一误写为没有公告。分类补检最初2603路径404，纠正为cs.DC/2026-03后取得89995B、346项/首1～50的月表，实际header及首项位于月初，没有本窗公告段，停止；不拿月初库存代替本窗。实际解析范围和限制见[分类停点](../_sources/daily-20260330/V3_CLASSIFICATION_LIST_STOP.md)。未读完整题摘的宽列表标题不构成逐项负侧审阅。

## 3. 候选与判断

确定落窗且通过贡献准入的候选0，本表为空，不评分。评分没有改成零分或用旧评分补填。

本轮补窗新增0；原候选表保持为空，不以补查搬移原51潜在材料或重新评分。OpenAI补窗线索明确贡献前关闭，只保留必要筛选依据，不入候选表。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

[当前逐项初筛](../_sources/daily-20260330/V3_SCREENING.md)保留61份题摘的实际判断与51个潜在身份。完整原文分为[首38份](../_sources/daily-20260330/V3_PRIMARY_ABSTRACT_DATE.json)、[补13份](../_sources/daily-20260330/V3_EXTRA_PRIMARY_ABSTRACTS.json)、[尾10份](../_sources/daily-20260330/V3_TAIL_PRIMARY_ABSTRACT_DATE.json)；首38份原h1误提取为分类，已用[官方精确原标题](../_sources/daily-20260330/V3_EXACT_IDENTITY_TITLES.json)纠正身份，摘要与历史字段没有改写。RPS-Serve使用26498v1，不以当前TCM-Serve标题代替v1。

具名贡献前关闭包括MAGNET四既有模块组合、Clawed分类与议程、Throughput汇总他人优化证据、MemBoost答案复用与路由模拟、Vision2Web任务扩展和验证模块组合；关闭依据是未指出新的机制、效度条件或反证，不是“组合/综述/模拟一概无价值”。DataFlex曾被过宽地归为模块组合，非作者读到ZeRO-3下全梯度/optimizer state重建、间隔与cache后，已改回潜在训练执行边界；反证和改判均保留，未因日期受阻而降级删除。

## 4. 证据与知识整合

本日没有确证落窗的采用对象，没有执行 Books 机制写入，也不声称已检查所有潜在材料的“已有覆盖”。标题/摘要完成与必要的准入消歧不等于实验、性能或安全结论已核实。

[OpenAI应用公告](https://openai.com/index/helping-disaster-response-teams-asia/)的核心是50名专业人员、13个国家的custom GPT与复用工作流培训及未来pilot计划；使用量增长不是工作流效果、因果收益或生产可靠性。未披露足以改变现有系统解释的增量，故贡献前关闭，不为其应用领域建立Books段落。

[Qwen3.5-Omni](https://qwen.ai/blog?id=qwen3.5-omni)的必要开头说明了ARIA自适应文本/语音单位对齐、turn-taking及Hybrid-Attention MoE，存在待核验的具体机制线索。由于正式事件日期尚冲突，未展开无关榜单、全篇附件或Books正文；不从厂商介绍推导效率和普遍稳定性。

DataFlex的必要方法消歧只确认“分片训练下动态数据选择可能有独立执行问题”；更多optimizer updates也可能解释accuracy变化，未采用作者提升数字。安全类潜在项的hallucination probe、CoT/response稳定代理、图像保护和激活干预同样不作为通用防护保证。

## 5. 缺口与下一步

原研究层普通待办0，原非作者最终验收有效但不代本轮补查验收。本轮root非作者完整六部分DAY已通过，普通待办0。以下均为原窗终态保留项：不计候选或Evidence完成，不用于正面证据、Books 或无遗漏断言，也不支持安全/性能保证。取得必要材料时只定点重开，不顺带扩展日期。

- **D1，51个arXiv潜在身份**：完整身份及各自增量在[逐项表](../_sources/daily-20260330/V3_SCREENING.md#日期准入仍待定的潜在材料)。原Submitted和常规公告只给最早03/30 08:00，arxiv.content/findable的原registered上界均晚于09:00，26846/26829/28651更到03/31；区间与右边界相交不能证明属于本日。需要对应版本官方公告、首次公开正文时间/范围或更早作者原发布，能完全确定归属后才对含糊增量补读、评分和必要审阅。原字段在上述三个题摘日期包及[补13日期](../_sources/daily-20260330/V3_EXTRA_DATE_FIELDS.json)，不能以Updated字段单独替代公开。这个请求按家族去重，51不等于51篇贡献成立。
- **Q1，Qwen3.5-Omni**：同一官方id/path的extra.date为03/30T04:00+08，content JSONLD、meta和可见日期均01/07T04:00+08，content内March30匹配0。[原冲突字段](../_sources/daily-20260330/V3_QWEN_DATE_CONFLICT_RAW.md)完整保留；需要官方原事件/勘误或版本身份解释。正文前缀仍是同标题，不能自行选择“更合理”的日期。猜测旧canonical的404不继续追查。
- **H1～H4，必要历史目录切片**：分别是Google publications、Meta publication、MiMo可见Blog/More的本窗首次公开日期段，以及Seed未返回的具体ID/date或数量差额解释。可接受官方本窗档案/日期化目录/原始发布记录；恢复位置与已查有限段见§2及[来源核查](../_sources/daily-20260330/V3_INDEPENDENT_DAILY_SOURCE_CHECK.md)，并非泛化请求机构全史。
- **分类补检限制**：正确cs.DC/2026-03月表已取得，但仅核月初首段header/首项，未恢复本窗公告相关标题段；可接受本窗官方分类公告切片。主题查询结果有效，原错误路径404不证明全arXiv不可用。

窗外线索：2604.19769、16383、19765、16385、18592的Available为April，registered在April21～23；3月Submitted不能反填3月公开。只保留真实归属恢复依据，不称旧事件已审去重，不阻塞本日。无其他日/月、Live或Weekly任务被启动。

补窗03-29独立限制：H1～4仍需对应日的Google pubs、Meta publication、MiMo Blog/More原日期切片和Seed未返回ID/date及数量差额解释；与原请求按来源去重，不索求机构全史。H5为[MiniMax AgentTech](https://agent.minimax.io/docs/techblog)的03-29官方历史datedslice：旧May13快照与本轮仅3条Sep/Oct均不能确认目标日的公开事件覆盖，缺口隔离为本窗终态，不支持正面Coverage、候选或Books；取得该日原目录/日期化档案才定点重开。没有确定候选被普通未读转为受阻。无常规arXiv公告不证明更早作者公开不存在；月表仅恢复访问，仍不支持全召回/无遗漏。取得上述具体slice才重开补窗受影响来源。补窗Books新写0不授No Change，原§4连续保留、不扩全文或附件。

## 6. 复核

复核者：原研究层mar02_v3、mar03_v3（均非本日作者）；本轮root（非补充报告作者）

结论：通过

原研究层分批校准与终态验收按下文保留。本轮root实际顺读完整六部分、本轮有限来源记录及本日V3非作者源核，直开Disaster核心29～56核具体负侧；确认14源有限回对、无常规arXiv公告的非全召回边界、0新增不等于已有覆盖，以及原51/Q1采用隔离。复用有效原题摘/安全反侧，不冒称root重新全读61篇或附件。MiniMax旧May13快照不能认证补窗覆盖的差额已修正，H1～5历史slice精确隔离，完整DAY通过并持久于[本轮原记录顶部](../_sources/daily-20260330/SUP_WORKING_STOP_20261012.md#root-非补充报告作者-day通过)。无Books实际写入或写后对象、无写锁。完成态V3、本地引用、原窗口/空候选表/617字符连续§4冻结及限定diff检查通过；机器检查不代语义验收。

已分批完成实际准入/负侧校准：mar02读取25份具名完整v1题摘和原日期，核14来源有限切片、OpenAI核心与Qwen原字段；mar03读取首9及后13+10份题摘，其中Throughput重复一次，实际31个唯一身份；必要DataFlex方法与关键对照纠正一次贡献关闭，并独立确认MemBoost/Vision2Web的具体负侧。两位完整题摘范围按身份合并为39/61，余22未被独立完整题摘复读；5项arXiv明确负侧均在复核范围内，安全、评价反证和执行变化的分层样本亦具名记录，未把抽检称全量。

两位非作者实际核正式六部分、查询与停止、61项日期身份和51项隔离，日级安全终态通过。修正分类入口已恢复但本窗公告段仍缺失、旧评分措辞与隔离采用边界后，mar02已定点复读确认；mar03另核extra13+tail10共23项当前官方metadata与轻量事件信号，不展开版本差分。静态校验和限定diff-check实际通过；0 Books新增没有写后对象。当前51项不获得贡献、正面Evidence或无遗漏认证，外部保留条件仍有效。
