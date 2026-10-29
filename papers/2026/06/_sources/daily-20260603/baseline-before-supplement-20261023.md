# Daily Research — 2026-06-03

**规范：** V3
**窗口：** 2026-06-02T09:00:00+08:00 ～ 2026-06-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T07:03:22+08:00

## 1. 结论

本轮14每日来源已有限检查，确认Kimi Code 0.7/0.8与OpenAI roles/Sites两发布家族落窗；分别完成受影响正确性深入审阅与发布边界标准审阅，两项仅报告处置已通过非作者准入、必要证据与实际owner复核，本次安全终态日级复核通过。前者明确goal持久状态、compaction独立TODO、approval observer与undo/replay分账，后者明确生成/部署/共享与刷新/重新发布分账；没有把功能公告或受控代码测试当成长任务成功、生产SLO或授权安全保证。

旧87 arXiv家族全部转入[唯一packet具名DateHold](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#87旧工作家族具名datehold清单)；DataCite登记时间与最早正常schedule不能证明首次公开上界。另Seed MetaPoint完整题摘有具体贡献，但目录日历时间与v1窗外submission不足以证落窗，独立DateHold，共88具名日期保留，不是88候选或88Evidence/Books通过。原719宽发现仅旧线索，不展开全池；旧87题摘/证据笔记保留，旧16I/70E/1Only的arXiv采用链未经本轮验收，不计本轮产出，不一刀删除其他有效来源与已有书稿。旧总88含Kimi的71E/16I/1Only统计已失效。

本轮新增Books为0，来源的Google Research/Qwen/MiMo/arXiv目标历史目录及MetaPoint必要日期均明确隔离，不支持“本日零论文”或全源无遗漏。两具体发布家族与四negative有限非作者复核均通过；普通可执行待办为0；完成表示已处理到安全终态，不是全部日期/目录证据或全部论文主张通过。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)直接UA恢复1240item，过滤本窗得5事件；前邻06/01 17Z、后邻06/03 10Z。五核心原文已读，见下节逐项分流 | 已检查 | RSS当前保留不证已删除事件；当前Learn文档不反推6月首次功能 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)可见10条；原HTML hydration 173 publication的publishedOn中，06/03 10:55Z/18Z→05/27 17:51:10.599Z跨窗，无目标metadata，停止 | 已检查 | 当前目录不证历史删除项；不读窗外正文 |
| SRC-GOOGLE-AI | [DeepMind第2页](https://deepmind.google/blog/page/2/)06月→05月边界；实际所链[Gemma4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)JSON-LD datePublished=2026-06-03T16:00:00+00:00，窗外；Singapore原页05/20。Research pubs仅年度2026/369与当前首15，无daily时间；Blog当前185行，日期限定June2 2026官方域搜索未取目标 | 受阻 | Google Research历史目标日目录受阻，非零命中；重开需原始目标日列表/带时区事件，不扩年度 |
| SRC-META-AI | Research空，错误publications直路content unavailable；从[SA-3DAO原页](https://ai.meta.com/datasets/sa-3dao-sam-3d-artist-objects/)导航得到[official publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)，有限重试成功：06/05→05/27；SA原页核心100公开/900heldout沿用2025 SAM3D benchmark，无新protocol，关闭 | 已检查 | 旧年份乱序/目录保留不能证明无遗漏；SA日历06/02时区未核但贡献已明确排除，不额外追时刻 |
| SRC-QWEN | [旧目录](https://qwenlm.github.io/)到2025/09并redirect；qwen.ai Blog/Research动态壳。公开前端969.js恢复只读page_config：news.news-list17条最大2025/04/28，research.research-list60条最大2025/12/23，日期切片无2026/06/02；两次target官方域搜索只有无关用户分享，无官方结果 | 受阻 | 这些配置是旧保留目录，不能证明2026本窗零材料；目标日原始目录缺口终态隔离，不扩全站 |
| SRC-DEEPSEEK | [News/research](https://www.deepseek.com/news/)研究06/24→02/25、News09/10→04/24跨窗，停止边界，不读其他日正文 | 已检查 | 查看全部动态/保留局限 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)Overview26最晚2025/11/07；kimi-code releases API page1/per_page100实际81条，0.7/0.8落窗见下；kimi-cli API page1/per_page20最邻1.47=06/05 10:35:01Z→1.46=05/29 05:56:52Z | 已检查 | 版本家族只审两窗内事件；0.9=06/03 14:01:42Z窗外，非本日重复已审项 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)web0行，直接公开publicList只读POST pageNum1/pageSize100/renderType0，total9/list9，逐项publicAt与displayDate均保留；两字段无本窗记录，展示07/08与04/30/04/23分列，停止9条元数据，不读窗外正文 | 已检查 | displayDate不等于publicAt，Hy3preview7月publicAt/4月displayDate不可混用；不以空壳为零 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)web一次timeout、直接HTML实际日期08/26/08/14→06/16 GLM5.2→05/20 ZCube，停止目标相邻范围 | 已检查 | 查看更多动态/目录保留局限 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)page1/13、20/242，06/04→06/03 MetaPoint→05/29；MetaPoint完整官方题摘与exact-v1日期见下。Blog动态壳，公开前端main恢复只读get_article_list_v2 article_type2；按实际100/101/102/103/104五主线分组首20元数据，均到目标前且has_more=false，Foundation06/23→02/14、Visual07/08→04/23、Audio07/20→04/09、模型系统2025、Frontier07/07→2025 | 已检查 | PublishDate多为日历占位，不能直接补成公开时刻；不扫描AIforScience或后续页正文 |
| SRC-BAIDU-ERNIE | [Blog zh](https://ernie.baidu.com/blog/zh/)page1/2最晚05/09→04/30→2025，目标前停止，不读page2/窗外正文 | 已检查 | 当前保留目录局限 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper8日期06/29→03/13、Blog15无日期；实际公开4752.2908c99e.js routes frontmatter EN/ZH Code06/10、UltraSpeed06/08、pipeline05/30，无目标；日期限定官方域06/02搜索无结果 | 受阻 | undated custom routes不证零，历史目标发布元数据缺口终态隔离；不逐篇打开其他日期 |
| SRC-MINIMAX | [English Blog](https://www.minimax.io/blog)06/09→06/01→05/27，[Chinese Blog](https://www.minimaxi.com/blog)实际HTML日期06/09→06/01→05/25；[Agent TechBlog](https://agent.minimax.io/docs/techblog)→官方/docs/llms.txt48索引，只1 AgentTeam techblog，已在05/27原官方Blog，停止 | 已检查 | undated文档索引不作本窗发布；不扩其他docs/body |
| SRC-ARXIV | 旧cs.CL Atom0字节；exact02643/02800官网只有submission，正确2026-06月25切片2718total无dayheaders；官方域精确target公告搜索无可用first-public receipt。旧official44 actual41正常schedule/3no不能补上界；87旧家族统一待日期恢复 | 受阻 | DataCite Created/Updated均非public Available；正常最早schedule非实际公告上界；不能授权87当日采用或宣称零漏项。只要同家族精确公告/作者带时区公开正文到达即可重开 |

执行时间为2026-10-01，查询始终限定本窗及停止边界。具体代码位置、元数据语义与分流见[本日packet](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#本轮有限原始来源恢复2026-10-01)。每周组未扫描；未触发其他清单按需来源。宽目录、搜索空或动态壳不作为无遗漏证明。

## 3. 候选与判断

以下为两项确定落窗、已通过非作者有限准入/证据与仅报告判断的家族；88个日期保留不混入此表。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.7.0 / 0.8.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.7.0) | 2026-06-02T10:23:53+08:00 ～ 2026-06-02T22:56:14+08:00 | 独立goal/TODO与typed undo/replay、审批observer具体改变长会话状态恢复边界；2+2+2=6 | 深入完成 | 仅报告：版本实现新增，不宣称现有Ch81泛主题全部覆盖；长期context/worldeffect/resume分账由实际正文承载 |
| [Codex roles / ChatGPT Sites](https://openai.com/index/codex-for-every-role-tool-workflow) | 2026-06-02T17:00:00+08:00 ～ 2026-06-02T18:00:01+08:00 | artifact局部context与受管理hosted输出、独立automation刷新→review→redeploy改变交付边界；1+2+2=5 | 标准完成 | 仅报告：公开publication/refresh接口事实，无新运行实现/因果评价，成熟review/permission原则不加高分 |

时间范围仅包住同家族两个已核事件；原始精确时刻在§4，范围完全落窗。不为换版本重复评分。

## 4. 证据与知识整合

### [Kimi Code 0.7.0 / 0.8.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.7.0)

官方release API `published_at` 分别2026-06-02T02:23:53Z与2026-06-02T14:56:13Z，两核心release及PR319/336/277/270/315必要实现/说明实际读，详见[精确packet](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#kimi-code-070--080发布正确性差额待非作者有限核)。PR319把独立tool store的TODO确定性附在compaction summary before history write，不能证明其他摘要忠实或任务完成。PR336 PermissionRequest/Result仅真实approval RPC成对异步通知，return ignored，不是authorization gate。PR277撤销real-user-prompt suffix并同步修剪replay、保injection/不穿compaction_summary；达到边界超额undo可先删suffix再throw，非全无修改；测试只支持受控context/replay一致，不是worldeffect undo。PR270 persisted active/paused/blocked、complete transient announce-clear，restart active→paused需resume；模型markComplete没有独立执行completionCriterion验证，完成消息/statistics非成功证明。

发布正确性差额按研究合同深入受影响部分；未读/未采用无关release项，也没有运行厂商测试或宣称复现。当前实际[AGENT-WORKFLOW Ch81](../../../../books/part-07-agent/81-workflow.md)“Context与Environment必须在同一恢复点对齐”约579–615及“Resume语义”约1142–1148已承载context/environment/effectledger与durable state分账；[AGENT-CONTEXT Ch75](../../../../books/part-07-agent/75-context.md)约282–300已有control-state最低fidelity与原文authority。它们支持长期边界，但不使特定新接口变成旧正文已有实现。因此最终处置仅报告，非作者必要证据与实际owner定点核通过，不另写版本手册段或新的Books。

### [Codex roles / ChatGPT Sites](https://openai.com/index/codex-for-every-role-tool-workflow)

官方RSS `pubDate`分别2026-06-02T09:00:00Z与[Academy](https://openai.com/academy/chatgpt-sites)10:00:00Z。原文核心：role plugins捆apps/skills/instructions/workflows；annotations把artifact局部选中span带入context；Sites生成/预览→review→deploy/shareURL，admin与connected app权限继续独立。Academy说当时不能直接连接live data，另automation gather更新后reviewrefresh/redeploy；没有承诺生成、保存、部署、共享、刷新自动成为一个成功事务。具体可改变选择：静态发布产物需要显式freshness/republication路径，不能把一次创建当作持续最新资料。

采用限发布接口/边界，无运行实现、matched comparison、heldout或端到端质量成本证据；评分只给这一局部机制，不给成熟approval原则或机构声望。当前[PLATFORM-PRODUCTION Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)与Ch81负责review/release与状态交付，公告未形成必须新增的长期机制，仅报告处置已通过有限非作者准入/证据核。10/01额外读当前Learn Sites save/deploy说明用于避免现在功能倒填6月，**当前文档不是历史发布证据**，不将其viewer connector、APIkey等新细节用于本窗判断。

### 机构事件的贡献前关闭与风险边界

[Codex productivity](https://openai.com/index/codex-for-knowledge-work)RSS06/02 02Z：知识工作者用户群增长速度超过开发者用户群3倍，非任务效率提升；采用数据没有新的评价协议或机制；[Youth leadership](https://openai.com/index/advancing-youth-safety-and-opportunity-through-global-leadership)07Z：9原则是政策提案，旧ageprediction/parentalcontrols回顾，不当作新部署；[Travelers](https://openai.com/index/travelers)12Z：Realtime应用85–90%completion缺cohort/denom/CI/E2E与新架构，不因应用成功数字准入。[Meta SA-3DAO](https://ai.meta.com/datasets/sa-3dao-sam-3d-artist-objects/)沿用2025 benchmark的100公开/900heldout，无新evaluation盲区/protocol。四项读核心后pre-denominator关闭，具体证据边界保留，不把日期未核明的SA再追时刻。四项有限negative校准已由apr29_close通过。

原旧raw所列2606.24369当前原站v2 withdrawn、v3重新提交，并非全家族永远撤回；v1=06/23且v3=09/22，都窗外，只纠正材料身份，不评分/不采用任何版本、不扩另一日。87 DateHold不是证据失败；其已有方法/反证留在[旧必要笔记](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#旧readme必要证据留存非本轮87-evidencebooks验收)，没有在本轮声称逐篇全文已读。

## 5. 缺口与下一步

普通可执行待办：0。两发布家族、四negative与校正后六部分非作者日级安全终态复核通过；剩余仅下列精确外部保留，不用于正面采用或无遗漏断言。

本窗终态保留：

- 87旧arXiv身份：首次公开上界未证，具名表与旧必要笔记在[唯一packet](../_sources/daily-20260603/V3_RECOVERY_BLOCKERS.md#87旧工作家族具名datehold清单)。正常最早schedule、Created、Updated或无dailyheader的月表不准入；需对应家族的官方目标公告/带时区作者公开正文receipt，届时只重开身份/日期及受影响采用链。旧16I本轮不验收、不计新整合，不删其他有效论点。
- [MetaPoint2606.05031v1](https://arxiv.org/abs/2606.05031v1)：SeedPublishDate1780416000000为日历占位（BJT06/03零点），而v1提交06/03 15:58:56UTC已窗外；完整题摘具体coordinate-posencoding贡献成立，但不能证窗内公开正文。需Seed原始公开上界receipt或可核快照，不读全文/不写Books来代替日期核。与87旧家族不重叠，共88个日期保留，非88证据审阅完成。
- Google Research历史日入口、Qwen2026动态目录、MiMo无日期custom routes与arXiv官方每日/主题公告缺口：有限原始入口和恢复/补检均已停止，不能记零或全源无遗漏。重开只接受目标日期官方目录/带时区原始研究事件，不扩全年或逐篇窗外正文。

窗外Gemma4 12B官方06/03 16Z与Kimi0.9 14:01:42Z只作停止边界，不属于本窗，也不冒充已处理的重复候选。不顺带处理06/04或9月。

## 6. 复核

复核者：apr29_close（非作者；报告作者sep22_resume_v3不自验）。

结论：通过

本次为安全终态日Gate，不是88项Evidence/Books全通过。apr29_close实际核官方RSS1240与五时刻、Kimi API及0.7/0.8核心release/PR319/336/277/270必要patch、roles/Sites与Academy刷新说明、四negative核心，及Ch81联合恢复/Resume、Ch75 typed fidelity/原文authority和Ch73同revision发布合同。两项6分深入/5分标准的Only通过；87唯一DateHold与MetaPoint独立=88，四历史覆盖缺口隔离通过。纠正productivity用户群增长非任务效率，并标明packet旧trace-to-body/exact-v1 blocker为旧过程非本轮验收；修改后只复读本次差异与最终状态，不重审87全文。无新Books；旧16I不在本轮Books验收范围。当前V3及限定diffcheck由作者与非作者实际复跑通过，机械结果不能替代日Gate。保护原staged/dirty，未stage、commit、push或破坏性Git操作.
