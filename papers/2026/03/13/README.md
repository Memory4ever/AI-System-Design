# Daily Research — 2026-03-13

**规范：** V3
**窗口：** 2026-03-12T09:00:00+08:00 ～ 2026-03-13T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T01:27:28+08:00

## 1. 结论

本轮没有确认完全落窗的候选，不等于当日没有研究进展或互联网零命中。14每日来源已执行有限检查并保存真实停止位置；arXiv四主题及有界系统同义补检得到169去重标题线索，实际读28家族完整v1题摘，另恢复MiMo官网ARL-Tangram对应1份题摘。2项arXiv明确准入前关闭，26项潜在贡献或决定准入事实含糊项因小时级日期未定隔离，不把全部称贡献通过；Google两洪水科学应用按当前阶段范围关闭。

IndexCache跨层选址复用、Expert Threshold因果动态路由，以及CLASP结构新trigger检测、HomeSafe动态安全评价盲区，均通过独立题摘层潜在准入校准，但没有足够公开时间证据归入本窗。DataCite26实际成功返回；其registered上界均晚于本日09:00终点，官方日程给最早08:00而非确定发布，Updated v1尚未核实公开语义。没有打分、必要正文Evidence完成或Books整合/已有覆盖认证。

旧报告完整保留于[旧报告原貌](../_sources/daily-20260313/V3_LEGACY_REPORT.md)，旧614库存、31候选、EffectiveDate、评分及完成标签不继承。root非作者日级验收已通过，普通待办0；外部限制见§5，不授正面覆盖或证据保证。

## 2. 来源覆盖

下表自包含本日实际范围；更细原值及恢复停止见[14源停点](../_sources/daily-20260313/V3_SOURCE_STOPPOINT.md)。已检查只指有限可见切片，不代表机构历史完整。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方news/rss.xml实际1241item，UTC03/12T01→03/13T01筛0；返回RSS停止 | 已检查 | RSS不证明未列出的全部历史事件 |
| SRC-ANTHROPIC | 官方Research嵌入publishedOn全March段，Mar6T10:30Z→Mar13T10:15Z跨窗；后者BJT18:15窗外 | 已检查 | 只限可见Research目录，不授删除历史保证 |
| SRC-GOOGLE-AI | Research March archive实际2/2，page1 12、page2两cards；Mar12两洪水core已读/范围关闭。DeepMindpage3六March日期核Mar26/26/25/17/10/3均窗外；Publications页面yearfilter及officialdate主题搜 | 受阻 | 必要Pub日级历史主题切片未恢复；不能用2026库存372或search代替 |
| SRC-META-AI | Research实际0line；Blogpage1/2可见cards跨Mar10CHMv2→Mar26TRIBEv2，officialdate主题搜未恢复本窗Research段 | 受阻 | 必要Research历史切片，Blog/search不证明无遗漏 |
| SRC-QWEN | 公开cy API40/40display与embeddedpublished pair，本窗无返回项，Feb16→Mar19邻接；[原值](../_sources/daily-20260313/V3_QWEN_FINITE_METADATA.md) | 已检查 | 当前40slice无paginationkey，字段冲突保留，非全机构历史保证 |
| SRC-DEEPSEEK | 实际ResearchIndex10完整至May2025，Feb25→Jun24；News可见5至Dec1/ViewAll停 | 受阻 | News隐藏历史段不能由Research目录认证 |
| SRC-MOONSHOT | 实际新Research www.kimi.com/en/blog/19完整至Mooncake，Feb9→Apr20，无可见未完成分页 | 已检查 | 可见Research切片，不用旧platform blog断言新Research缺失 |
| SRC-TENCENT-HUNYUAN | 本日对读11rawdates并实际publicList全部分支page1,size20,renderType0，total11/11，Feb13→Apr23 | 已检查 | publishedAt/display不同，不互换first-public；有限公开目录非全机构历史保证 |
| SRC-ZAI | 实际Research全部time-sort首可见15至Dec9，Feb21→Mar15，到查看更多停 | 已检查 | 仅跨窗可见段，不把Mar15day-only补时刻 |
| SRC-BYTEDANCE-SEED | Research首页当前Blog5/Pub10精选；本日完整对读公开type1/year2026 token0/20历史metadata跨Feb25→Mar26,next40，窗口邻近仅量子波函数科学标题；实际type0历史query返回total0与首页Blog有差 | 受阻 | 论文有限slice不是all82；Blog历史slice未恢复，空响应不授zero |
| SRC-BAIDU-ERNIE | 实际zhBlogpage1/2可见10至Nov2025，Feb6→Apr15跨窗，页底更旧next2/2停 | 已检查 | 不扩全部GitHub活动，不保证删除历史 |
| SRC-XIAOMI-MIMO | 实际Paper8/8、Blog15 nondated+More；官方runtime有限route/metadata探针未获datedhistory；Tangram13019v1完整题摘/Submitted晚本日结束 | 受阻 | 官网TangramMar13day-only仍相交；Blog历史段未恢复，两事件不合并为exact |
| SRC-MINIMAX | 实际EN12/ZH13主Blog跨Feb14/12Forge→Mar18；AgentTech heading及llms.txt48line当前guides目录停止 | 受阻 | AgentTech本窗历史切片，主Blog不替代 |
| SRC-ARXIV | [四topic+系统supp](../_sources/daily-20260313/V3_ARXIV_TOPIC_DISCOVERY.md) start0/max100，78/9/34/62/3、169独立标题；28完整v1题摘及26DataCite实际定点；officialavailability/OAI/currentpastweek核日期 | 受阻 | 26公开区间跨右端，不能确认落窗；更早Submitted moderation/修订本窗历史主题切片未恢复 |

本日未扩每周来源、未从旧Weekly反推。Google核心、arXiv API/DataCite/OAI仅服务本窗发现与日期恢复，不扫描全月版本或把宽库存变候选队列。

## 3. 候选与判断

没有通过日期确认的确定当窗候选，故本表为空。潜在或准入事实含糊但日期只相交的26项均在§5具名保留，不先评分或移入候选表。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

没有可归入本窗的候选，未作必要正文Evidence或Books Existing认证/修改。题摘读完不是证据审阅完成。

[题摘与筛选停止](../_sources/daily-20260313/V3_SCREENING_STOP.md)区分潜在贡献、决定准入事实含糊和具体负侧。IndexCache/ET仅潜在机制；CLASP不因XGBoost加模块准入，保留结构新trigger受限反证；HomeSafe不把双brain成熟组合计新贡献，保留动态对静态评价盲区。这四项root实际完整题摘校准有效，未读/未认证中心实验。

明确负侧为VMAO既有DAG/LLMcomplete/replan组合无新verification条件、Perplexity RFI风险与defense taxonomy/standards agenda无新具体安全contract；Google洪水预报与Groundsource完整core属于暂缓科学应用及既有prompt流程。root实际核这些4负侧，不宣称全169或旧614审阅。Seed量子波函数标题范围排除未由root重新读。

## 5. 缺口与下一步

普通待办0。以下为本窗终态保留项，不支持正面证据、Books或无遗漏断言，也不授性能/安全保证；材料到达时按各项条件定点重开。

**26项具名日期保留：** [首8日期原值](../_sources/daily-20260313/V3_FIRST_DATE_PACKET.md)、[补18原值](../_sources/daily-20260313/V3_DATE_PACKET_18.md)与[各项增量/准入状态](../_sources/daily-20260313/V3_SCREENING_STOP.md)保留完整身份、Submitted、Updated v1、registered、findable、arxiv.content。实际公开上界是registered而非exact，最早常规公告08:00与之复合仍跨09:00；OAI12201仅UTCday、pastweek实际是当前Sep，没有可用小时级primary。需要对应ID正文于03/13BJT09前公开的官方announcement/日志或有明确公开语义的timestamp原值，形成完全落窗range；不要求全库重建，不套Updated为upper。

- [IndexCache12201v1](https://arxiv.org/abs/2603.12201v1)、[Expert Threshold11535v1](https://arxiv.org/abs/2603.11535v1)、[Slow-Fast12038v1](https://arxiv.org/abs/2603.12038v1)、[AdaFuse11873v1](https://arxiv.org/abs/2603.11873v1)、[DapQ11564v1](https://arxiv.org/abs/2603.11564v1)、[EBFT12248v1](https://arxiv.org/abs/2603.12248v1)、[Attention Sinks11487v1](https://arxiv.org/abs/2603.11487v1)、[Cornserve12118v1](https://arxiv.org/abs/2603.12118v1)。
- [RewardHackingAgents11337v1](https://arxiv.org/abs/2603.11337v1)、[User Sim2Real11245v1](https://arxiv.org/abs/2603.11245v1)、[Self-Locking12109v1](https://arxiv.org/abs/2603.12109v1)、[RL Generalization12011v1](https://arxiv.org/abs/2603.12011v1)、[ARROW11395v1](https://arxiv.org/abs/2603.11395v1)、[VLA Continual11653v1](https://arxiv.org/abs/2603.11653v1)、[EndoCoT12252v1](https://arxiv.org/abs/2603.12252v1)、[Jailbreak Scaling11331v1](https://arxiv.org/abs/2603.11331v1)。
- [Instructional Leakage11862v1](https://arxiv.org/abs/2603.11862v1)、[CLASP12206v1](https://arxiv.org/abs/2603.12206v1)、[Refusal Triggers11388v1](https://arxiv.org/abs/2603.11388v1)、[Paralinguistic11947v1](https://arxiv.org/abs/2603.11947v1)、[PRISM11853v1](https://arxiv.org/abs/2603.11853v1)、[Taming OpenClaw11619v1](https://arxiv.org/abs/2603.11619v1)、[SSGM11768v1](https://arxiv.org/abs/2603.11768v1)、[HomeSafe11975v1](https://arxiv.org/abs/2603.11975v1)、[XSkill12056v1](https://arxiv.org/abs/2603.12056v1)、[Think While Watching11896v1](https://arxiv.org/abs/2603.11896v1)。

取得完全落窗证据后才继续准入事实含糊项的定点机制/必要对照，以及已清楚potential的证据审阅、评分与唯一owner比较；当前不称26全部贡献通过。首8当前官方事件header/Comments已[补核](../_sources/daily-20260313/V3_FIRST8_EVENT_HEADERS.md)：AdaFuse11873官方admin标注与2405.17741有substantial text overlap，原创/重复增量仍未核；若恢复拟采用，先定点核重叠如何影响pre-gating/fused-kernel命题，不推撤回或全部机制重复。若核窗外只作真实归属日恢复线索，不挪窗或从深审成本删项。

**MiMo官网ARL-Tangram事件：** [13019v1](https://arxiv.org/abs/2603.13019v1) Submitted03/13T14:25:20Z已晚于结束，arxiv事件可排本窗；官网Paper“March13”另有先挂时间未知，需官网正文实际公开时区/range。当前目录day-only不能强拼论文公告或正式releaseexact；不读全文/评分/Books。

**6组必要官方历史切片：** Google Publications、Meta Research、DeepSeek News隐藏ViewAll、Seed Blog、MiMo Blog、MiniMax Agent Tech Blog。缺本窗主题datedlist或原文；已实际入口、有限fallback及停止如§2与停点。当前publiclist/搜索/空响应不支持完整覆盖，替代为可公开核验的对应窗口目录/原文；仅重开该源本窗，不能由其他机构arxiv证据认证它们。arxiv早Submitted moderation/重要修订相关历史公告主题slice另保留，不把169标题或28题摘称完整公开批次。

窗外恢复线索不阻塞本窗：Tangram论文事件最早在以后公告；Anthropic diff-tool精确Mar13T10:15Z属于03/14 Daily窗口。未作这些窗外核心深审，不授已处理重复标签。

## 6. 复核

复核者：root（非作者）
结论：通过

root实际完整读本报告六部分、14源停止记录、五有限主题查询参数与停止位置、28题摘筛选状态、26DataCite原值/OAI及首8当前官方header/Comments记录。首8最初只查API身份的遗漏已补正；AdaFuse官方admin text-overlap信号与§5的日期及受影响增量/重复关系定点重开条件已独立核，不推撤回、原创或全稿重复。日期隔离、0确定候选、六组历史切片限制符合安全终态，普通待办0；没有Books写入或待POST。

复用root已实际读IndexCache/ET及CLASP/HomeSafe四份完整v1题摘的潜在准入校准，以及Google两完整core、VMAO/Perplexity两完整题摘的四项负侧校准。28份中其余22份题摘未由root重读，中心方法/实验未复核，26项necessaryEvidence与Books均未认证；隔离项不算正面Coverage或Evidence通过，也不宣称全169、全机构历史或互联网无遗漏。

作者与root实际运行V3 validator通过（exit0），本日报git diff --check通过（exit0）；结果只能证明机械一致性，不能替代上述语义验收。没有stage、commit或push。
