# Daily Research — 2026-02-22

**规范：** V3
**窗口：** 2026-02-21T09:00:00+08:00 ～ 2026-02-22T09:00:00+08:00
**窗口说明：** 用户2026-10-08授权既有Daily增量遗漏补查；保留原候选/日期/评分、旧窗口、有效Source/Books及原§4连续正文。
**补充窗口：** 2026-02-21 ～ 2026-02-21
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T20:11:00+08:00

## 1. 结论

本轮自然日补查确定新增0，原1/合计1候选及其标准审阅、Ch83已有覆盖不变，Books新写0。2份完整题摘的有限初筛：2602.18899v1有表示机制潜力但缺必要公开日期，作为本窗终态保留项；Reliability作者Feb21介绍与既有v1同事件复用，不移原归属、不重新授Evidence。root已独立校准这两项及代表关闭，并实际通过最终六部分增量DAY；普通待办0。详细原查询、实际停止与题摘路由在[补查依据](../_sources/daily-20260222/supplement-20261008.md)。原正文以下完成/复核陈述均为2026-10-05已有效研究，不替代本轮增量验收。

本窗确认1个唯一贡献候选，已完成标准证据审阅；Books为1项具体已有覆盖，实际改书0。新的MCP schema适配修复说明：消除validator的元模式报错，并不等于保留参数语义。不能只按协议名称或“JSON Schema兼容”推断互操作。

14每日来源及两个实际触发表外release已经作本窗有界检查；窗外GLM-5目录收录、Anthropic安全路线图状态日期和OpenAI科学发布未移入本窗。没有把宽库存转换为逐题摘/全文队列，也没有继承旧V2.1的0候选/完成标签。原始发现、排除和停止位置见[本日来源/筛选依据](../_sources/daily-20260222/V3_SCREENING.md)；发布核心关闭不称全文审阅。

普通待办0；root非作者独立日级复核已通过。历史目录与arXiv非标准公开限制已隔离，不计正面Coverage/Evidence，不支持全网无遗漏或任意MCP server可靠性保证。未修改Books、共享索引、其他日期；未stage、commit、push。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS原item/pubDate扫描本窗，邻界02/20 14:30GMT～02/23 05:30GMT；[原响应](../_sources/daily-20260222/V3_NATIVE_openai_rss.txt)<br>**本轮补查：** 本次原RSS全部item日期定位，Feb20 14:30GMT之后为Feb23 05:30GMT，止当前完整item列表 | 已检查 | 已检查；本窗无RSS事件；当前RSS不保证历史删除项不存在；补查：当前RSS留存范围，历史删除不能排除 |
| SRC-ANTHROPIC | Research原HTML全部publishedOn，02/18 15:10Z～02/23 11:52Z跨窗，无本窗条目；[原响应](../_sources/daily-20260222/V3_NATIVE_anthropic_research.txt)。安全信号另核RSP官网timeline，Roadmap发布为02/24<br>**本轮补查：** 本次Research全部嵌入publishedOn跨Feb18 15:10Z至Feb23 11:52/53Z；官方日期主题查询原Roadmap既有关闭复用，止结果页 | 已检查 | 插图_createdAt、能力状态日期不当发布时刻；补查：当前留存范围，不将插图日期/状态日期当公开 |
| SRC-GOOGLE-AI | DeepMind原RSS邻界02/19 16:06:14Z～02/26 16:01:50Z；[RSS](../_sources/daily-20260222/V3_NATIVE_deepmind_rss.txt)。Google Research官方February目录7条，最新Feb17、整页止；[目录](../_sources/daily-20260222/V3_NATIVE_google_blog_feb.txt)。Publications限定主题/日期补检，未全扫773页<br>**本轮补查：** February Blog7卡最新Feb17整页止；本次DeepMind RSS邻界Feb19 16:06Z～Feb26 16:01Z；Publications当前第一页+有限日期主题查询止 | 受阻 | Blog/RSS已检查；Publications受阻；论文目录只有年份/当前第一页，未恢复本窗日级发布，不授该段历史覆盖；补查：Blog/RSS已检查；Publications缺本窗日级公开，不全扫年份目录 |
| SRC-META-AI | Research原网页0行；限定ai.meta.com模型/训练/Agent与Feb21～22补检返回窗外条目后止；[原读取](../_sources/daily-20260222/V3_RAW_web2.json)、[查询](../_sources/daily-20260222/V3_RAW_web8.json)<br>**本轮补查：** Research0行+限定官方域日期/模型/训练/Agent补检，止本次结果页 | 受阻 | 历史研究目录不可提取；搜索不证明零事件；补查：历史目录不能恢复，0行不作零事件 |
| SRC-QWEN | 注册入口跳qwen.ai；[native Blog壳](../_sources/daily-20260222/V3_NATIVE_qwen.txt)、网页0行、一次浏览器读取超时；限定官网本窗日期查询止<br>**本轮补查：** Blog native壳、p_home-index JS有限恢复、一次官方浏览器读取超时；官网本窗补检止 | 受阻 | 未恢复动态历史Blog；不扫全部旧release、不宣称零事件；补查：动态历史Blog未恢复，不以壳/无搜索命中授覆盖 |
| SRC-DEEPSEEK | 官方主页→API Docs；/news/实际跳当前First API Call，不能作历史目录；限定官网/API Docs日期补检止；[原读取](../_sources/daily-20260222/V3_RAW_web2.json)、[补检](../_sources/daily-20260222/V3_RAW_web13.json)<br>**本轮补查：** 本次主页和API /news，native当前/news/news260910，限定官网/API日期查询止 | 受阻 | 未恢复本窗历史研究目录；当前API示例不证明历史变更；补查：当前单页不是Feb21历史研究目录 |
| SRC-MOONSHOT | Platform Blog实际26条、最新2025/11/07；真实/blog/posts/changelog最新2025/11/06；限定官方/kimi-cli GitHub日期补检止；[列表](../_sources/daily-20260222/V3_RAW_web2.json)、[补检](../_sources/daily-20260222/V3_RAW_web13.json)<br>**本轮补查：** Blog26条及真实/posts/changelog，最新2025/11/07与11/06；已越窗止，限定官网日期补检 | 已检查 | 已检查公开Blog；历史代码检索受限；Blog不能覆盖所有官方代码变更，未恢复本窗相关release，不赋全项目零变更；补查：Blog已检查，不覆盖所有代码release；原代码历史局限保留 |
| SRC-TENCENT-HUNYUAN | 原站JS确认allTab=renderType0；本日实际POST publicList，pageNum1/pageSize100，EN9/9、ZH11/11全部返回，窗前最近Feb13、窗后Apr22，止第1页；[ZH原响应](../_sources/daily-20260222/V3_NATIVE_hunyuan_zh.txt)<br>**本轮补查：** 本次publicList POST page1/size100/renderType0，EN9/9完整当前目录，Feb13/Feb3→Apr22；两语言头及追加lang=zh均返同EN，止page1 | 已检查 | 已检查当前公开“全部”目录；无本窗条目；当前保留范围，不保证历史删除/未保留内容；补查：EN当前全部已查；ZH历史段未恢复，不声称ZH11/全历史覆盖 |
| SRC-ZAI | Research时间列表从03/15跨02/21 GLM-5 report再到02/11；潜力题摘/current abs/本窗README commit核查；[目录](../_sources/daily-20260222/V3_RAW_web3.json)、[abs](../_sources/daily-20260222/V3_NATIVE_glm_abs.txt)<br>**本轮补查：** 本次Research时间段Mar15→Feb21 GLM-5→Feb11，跨起点止；同家族旧有效处置复用 | 已检查 | 已检查；晚收录不重复准入；没有本窗重要修订差额，不用目录日期重移v1归属；补查：同名目录不当新修订或搬移原论文日期 |
| SRC-BYTEDANCE-SEED | 原get_article_list_v2：type1 ASC/year2026/offset0/count20实际20条Jan20～Feb25，第19条已窗后即止、next20；type2 DESC/offset0实际12条跨March31～Feb14即止；[论文](../_sources/daily-20260222/V3_NATIVE_seed_papers_asc.txt)、[Blog](../_sources/daily-20260222/V3_NATIVE_seed_blogs0.txt)<br>**本轮补查：** type1 ASC2026/offset0/count20实际20/82，19th Feb25跨窗止；type2 ASC实际9卡、next20/has_more=true，4th April1跨窗止 | 已检查 | 已检查；本窗无目录事件；首次type1空但has_more=true未作零命中；目录不是全网召回保证；补查：两返回序列本窗无目录事件；Blog9卡但has_more只作跨窗停止，不称全目录读完/历史全覆盖 |
| SRC-BAIDU-ERNIE | 官方Blog第一页日期从Apr15跨Feb06再到2025；已跨起点不翻第2页旧文；[页面](../_sources/daily-20260222/V3_RAW_web3.json)<br>**本轮补查：** 官方Blog首页May9→Apr15→Feb6→Jan29→2025，跨起点止，不翻旧page2 | 已检查 | 已检查；本窗无卡片；当前公开Blog范围，不保证过去删除项；补查：当前公开Blog留存范围 |
| SRC-XIAOMI-MIMO | Paper/Blog当前Research从Mar13跨到HySparse Feb03，整段止；[原页面](../_sources/daily-20260222/V3_NATIVE_mimo.txt)<br>**本轮补查：** Paper当前段June29→Mar13→Feb3→Jan8已跨起点止；Blog15标题无逐项日期，有限官方日期补检 | 受阻 | 已检查；本窗无目录条目；只当前公开Research范围；补查：Paper有限段已检查；Blog历史日级日期未恢复，不授整段零事件 |
| SRC-MINIMAX | 英文SSR Blog12卡，邻界March18～Forge February14；中文入口跳minimax.cn；[英文原卡](../_sources/daily-20260222/V3_NATIVE_minimax_blog.txt)、[中文读取](../_sources/daily-20260222/V3_RAW_web5.json)<br>**本轮补查：** 本次EN原SSR10日期卡Mar18→Forge Feb14→Feb12→Jan27；ZH13卡Mar18→Forge Feb12→Jan28，整页止 | 已检查 | 已检查；本窗无目录条目；不代表过去未保留内容不存在；补查：EN/ZH Forge显示不同日期但均窗前；只当前留存范围 |
| SRC-ARXIV | 官方availability实际读取：Eastern Friday/Saturday无scheduled announcement；本窗是Eastern Fri20 20:00～Sat21 20:00，标准批次0。模型/训练、GPU/推理、Agent/RAG、多模态/World Model/VLA四组本窗官方域补检无恢复项；[主题查询](../_sources/daily-20260222/V3_RAW_web14.json)、[原规则](../_sources/daily-20260222/V3_NATIVE_availability.txt)<br>**本轮补查：** BJT Feb21对应Eastern Fri20 11:00～Sat21 11:00，官方无scheduled batch；4主题announced查询修正为Feb21～22后真实no results；cs.CL2602首25标题补检native404，止此 | 受阻 | 标准批次已检查；历史列表受阻；cs.LG2602月列表web失败/native404，非标准提前公开不能穷尽；未把分类列表当逐题队列；补查：初same-date表单错误不算0；修正查询仅有界发现，非标准先公开/标题列表仍缺段，不用Submitted或DOI登记推公开 |
| 表外：[HKUDS/nanobot](https://github.com/HKUDS/nanobot/releases/tag/v0.1.4.post1) | 搜索触发release，原API Published21T13:09:50Z；核心说明及5个实际安全/执行信号定点核，止相应PR，不扩全项目；[原release](../_sources/daily-20260222/V3_NATIVE_nanobot_release.txt) | 已检查 | 已检查；贡献关闭；不赋memory/shell/Agent生产可靠性保证 |
| 表外：[oh-my-pi](https://github.com/can1357/oh-my-pi/releases/tag/v12.16.0) | 搜索触发release，原API Published21T14:00:02Z；#126核心/唯一diff、精确tag两条convertSchema消费路径；[release](../_sources/daily-20260222/V3_NATIVE_omp_release.txt)、[tag实现](../_sources/daily-20260222/V3_NATIVE_omp_tag_bridge.txt) | 已检查 | 已检查；1候选；静态原源审阅，未运行validator/项目或复现生产 |

到期来源已处理至上述有限停止或明确隔离；没有触发会议/每周来源的新发现扫描。历史目录受阻的行不称Coverage通过，其他确定原始入口照常处理。

### 本轮补充窗口的实际来源停止

本次原件/请求在[补查依据](../_sources/daily-20260222/supplement-20261008.md)及其链接manifest与native原件；下表不以旧窗口覆盖替代自然日补查，不宣称全网召回。


本轮没有新增会议/每周触发或其他日期扫描；仅实际触发作者Reliability介绍页与phonological vectors原项目恢复，均见首批准入包；原两个release同事件有效证据复用，不重复深审。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [oh-my-pi v12.16.0 — MCP schema bridge #126](https://github.com/can1357/oh-my-pi/releases/tag/v12.16.0) | 2026-02-21T22:00:02+08:00 | draft-07 validator原本拒绝某些server元模式/nullable，递归适配恢复局部可调用性，却要求重新确认参数语义；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MCP，[Ch83 协议比较/adapter契约](../../../../books/part-07-agent/83-mcp.md#协议比较必须拆开五类契约)，实际改书0 |

没有把nanobot已有能力接入、结构化输出修补、公开help、regex误报、进程回收及in-process单飞当作新长期机制；排除项不评分。GLM-5和安全路线图不是本窗候选，不进入唯一家族分母。

本轮未新增确定候选，以上原候选行逐字冻结。2602.18899v1明确有表示机制准入潜力，但必要公开日期无法确认，不评分、不先填确定候选；Reliability作者页是已审v1同事件，MARTI-v2原News Feb10与First Proof本次RSS Feb20为窗前代表关闭。具体完整题摘、日期限制与root准入校准见[首批准入包](../_sources/daily-20260222/supplement-admission-20261008.md)。没有以Books覆盖或深审工作量缩池。

## 4. 证据与知识整合

### [oh-my-pi v12.16.0 — MCP schema bridge #126](https://github.com/can1357/oh-my-pi/releases/tag/v12.16.0)

采用精确release v12.16.0，不是搜索后来拼接的完整changelog。原release只有#126与memory文档两项；先前索引中的abort提示不在本次release，已纠正，不构造第二个贡献。#126原说明：rmcp/schemars发出draft2020-12元模式声明和OpenAPI式nullable，draft07 AJV会拒绝未知元模式/keyword；作者在MCP→TypeBox边界递归去除字段，而非换validator方言。

[精确tag代码](https://github.com/can1357/oh-my-pi/blob/v12.16.0/packages/coding-agent/src/mcp/tool-bridge.ts) sanitizeSchema（[原响应](../_sources/daily-20260222/V3_NATIVE_omp_tag_bridge.txt)L53～89）在convertSchema执行；MCPTool/DeferredMCPTool分别L196/L300消费同一结果。原代码和[唯一diff](../_sources/daily-20260222/V3_NATIVE_omp_126_files.txt)支持“添加一条消除所述校验报错的适配路径”，不支持任意server方言语义等价。

关键反侧：递归处理所有object，并未把nullable:true重写为包含null的类型；properties字典中若业务参数本来叫nullable或$schema，也会被解构删除。去除声明并不会翻译draft2020-12其他keyword。这是静态实现推断，不是项目运行/生产攻击复现；不声称真实server中的发生比例。

本项无论文benchmark，吞吐、GPU、batch、concurrency、SLO/evaluator不适用，因采用对象是公开实现的兼容分支。PR声明tested locally但未给跨方言完整对照；实际运行环境与回归覆盖为Not Disclosed，本次未执行artifact，没有性能/安全收益数字可外推。

Books判断：Ch83“协议比较必须拆开五类契约”实际分离schema/effect/授权与runtime owner，要求adapter映射不完整时适配或拒绝；相邻typed definition生成两类adapter论证要求保留独立adapter、contract tests/schema diff以防最低公分母/特性漂移。这承载本次采用的稳定判断；#126只是新的局部兼容实例，不强造长期机制diff。root非作者实际核release、PRbody、完整diff及Ch83 L96～120，确认收窄与已有覆盖/No Change。

其余排除/日期关系见[本日筛选判断](../_sources/daily-20260222/V3_SCREENING.md)，不把已读发布核心计为贡献候选或正面Evidence。

### 本轮增量证据与知识整合

原§4从oh-my-pi标题至上段连续正文完全保留；没有重新授原审阅/Books权限。Reliability作者页及[精确v1原abs](../_sources/daily-20260222/supplement-native-reliability_v1-20261008.txt)均为14模型/12指标，相同摘要；本次current abs的v3为15模型，仅用于轻量当前说明检查，不混入v1或解释为Feb21重要修订。02-20原v1的C_out争议及采用边界按同事件复用，作者介绍页没有新方法/纠错差额，Books无新命题。

2602.18899v1完整题摘的96语言线性方向与连续尺度关系值得核验，不能因旧speech命名排除；潜在owner为WORLDVIEW-REPRESENTATION/MULTIMODAL-REPRESENTATION，但本窗缺首公开证据，未进行正文/实验/Books采用。本轮必要日期原源一次有界恢复（v1 abs、项目README、原repo响应）不含Feb21发布关系，不把Submitted/created_at当论文公开，不为日期展开全文或版本史。其处置为精确终态隔离，不称Source完成或表示干预结论成立。本轮Books新写0，原AGENT-MCP/Ch83具体已有覆盖有效保持。

## 5. 缺口与下一步

本轮普通待办：0。作者扫描/初筛/六部分补层和root非作者准入、最终增量DAY均已完成；以下来源/日期保留不是未执行普通队列。原下列“普通待办0”为旧有效审阅说明，保留原文本，本轮通过依据在§6新增复核段。

本轮新增终态保留：[2602.18899v1 phonological vectors](https://arxiv.org/abs/2602.18899v1)缺本次事件的首公开日；有表示机制潜力，日期决定是否属于Feb21，故当前不能评分/作为确认新增或Books。原v1/项目一次恢复仍只有Submitted和无日期README，均不能证明公开。接受Feb21作者正文发布页、官方首公告或能确定真实归属日的原证；只重开本身份日期与其依赖准入，若落窗再作评分/必要Source，不扩大本窗。

本轮来源保留：Qwen/Meta历史目录、DeepSeek历史目录、Google Publications日段、Hunyuan未恢复ZH段、MiMo Blog日段、arXiv非标准先公开/首25标题列表及当前目录过去删除，具体身份/当前停止在§2表与补查依据。需要本窗原发布清单、具名事件/精确原稿公开关系，回来只重开该段；搜索首页、壳、空响应不能作正面覆盖。以上不支持候选/Books/无遗漏，也不是普通未执行全文队列；其他确定入口继续处理至有限停止。

普通待办：0。来源/候选标准审阅/Books处置及非作者独立日级复核均已完成；以下仅终态保留项，不是待执行工作。

本窗终态保留项（不用于正面证据、Books或“无遗漏”）：

- Qwen/Meta动态历史研究目录、DeepSeek历史发布目录与Moonshot未恢复的相关代码release：有限官方入口和日期主题补检没有恢复本窗完整目录。需要本窗官方列表、精确release或作者原稿及公开时刻；回来只重开该来源/事件，不从API当前页、空响应或旧标签推零。
- Google Publications本窗日级事件：当前第一页只有年份/题摘，目录773页；需要官方日级发布关系或具体paper的首公开证据。已核Blog/RSS不填该缺段，不遍历全年以制造当日分母。
- arXiv非标准提前公开/cs.LG历史列表：标准Friday/Saturday无公告，但月列表失败。具体潜力身份及完全落窗的官方公告/作者先公开证据回来才重开；Submitted、DataCite-created、后收录日期不补造本窗时刻。
- 当前机构目录/RSS过去删除或未保留内容：当前暴露的有限范围就是本次停止位置；发现本窗相关遗漏原始事件时只定点补查，不重跑整月或扩Weekly。

窗外定位：GLM-5 2602.15763身份Registered02/18 02:49:09Z给出窗前上界，不能赋首公开精确时刻；Research目录02/21为后收录，无本窗重要修订信号。Anthropic RSP官网timeline的Roadmap发布为02/24，不从正文February22能力状态日期造候选。OpenAI Our First Proof是02/20 22:30BJT，窗前且AI for Science暂缓。均不阻塞本窗，不请求第二次材料或续跑窗外全文。

## 6. 复核

本轮复核者：root（非报告作者）。结论：通过。首批准入实际2完整题摘与MARTI/FirstProof代表关闭已通过，范围/日期隔离/同v1复用裁决在首批准入包。最终增量DAY：root实际顺读全部六部分及补查依据，核native请求参数/status、RSS日期、Anthropic publishedOn、Hunyuan9返回、Seed20/9与真实跨窗日期和has_more、4修正query真实no results、两精确完整题摘/同事件及代表关闭；确认原1/新增0/Books0、日期保留1与有限受阻源隔离。未重新授旧1/旧Source，也未检验其他无关release、全年目录或全网排除，不称全量验证；机器校验不能替代独立DAY。报告作者据该非作者实际验收消息改为完成，普通待办0，本日结束不自行接其他日。

本轮进行态及root验收后完成态V3校验通过；原1候选行、原窗口、原§4连续正文保留核验通过，34本地引用存在性及限定cached/unstaged diff-check通过。首次仅检查时间夹带历史说明与第二张重复来源表导致结构报错，已移除字段说明并将补查范围合入原14行（不改校验器/候选/§4）；不由修正或机器校验授语义完成。

以下root结论为原2026-10-05有效复核记录，完整保留，不能用作本轮新来源/筛选/六部分验收。

复核者：root（非报告作者）。

结论：通过

分批与最终复核：root实际核全部1项拟入选的release/PR/完整diff、精确tag证据及Ch83具体已有覆盖；GLM/roadmap/Proof日期与范围关闭通过。安全/执行负侧实际覆盖nanobot #824公开帮助、#820guard误报、#866memory schema修复；新增#851/#823的PR原body和完整唯一patch经root回核：5秒wait超时pass不授终止保证，同loop set/finally不授跨进程原子性，贡献关闭成立。最终顺读六部分、14每日与2触发源实际停止位置、公告时区、首公开关系及隔离边界，通过DAY。未检查其他无关release PR、全部机构历年论文或全网排除项，不称全量验证；历史缺段不是正面Coverage/Evidence。

机器校验已执行，首次只发现结果字段夹带说明、公开时刻字段夹带原值说明及候选标题与§4不一致，已只调整字段/标题、不改判断或校验器；V3通过。自写2份Markdown/30本地链接、围栏/空白及本日限定cached/unstaged diff-check通过。完成态再次校验，不以工具替代上述语义验收。
