# 2026-03-08 增量来源补查

作者：supplement_20260308；执行：2026-10-09 04:25～04:33 +08:00。仅本日 README 与本目录；共享 Books、Learning State、索引不写。原始冻结稿见 [baseline](./baseline-before-supplement-20261009.md)。完整重读本日 AGENTS、当前 Research/Report 合同、Sources 使用说明/每日/主线 topic/恢复说明、Prompt、ROADMAP；Learning State 只读 2026 路由。原窗口、0 候选及原 §4 连续正文保留。新增窗口为 2026-03-07 完整北京时间自然日；不创建 Sunday Weekly。

## 实际来源与停止

原始获取时间、URL、状态、bytes 见 [official](./SUP_FETCH_official.json)、[recovery](./SUP_FETCH_recovery.json)、[dates](./SUP_FETCH_dates.json)。下载正文不等于已审正文：本次目录只读日期/相关标题；没有把目录全部题摘变为队列。

| 来源 | 本日实际范围 / 停止 | 结果与权限 |
| --- | --- | --- |
| SRC-OPENAI | [新 RSS raw](./SUP_OPENAI.raw) 1257 items，按 Mar07 日期过滤；相邻 Mar06 Codex Security/Descript/Balyasny → Mar09 Promptfoo，无 Mar07 item。 | 有限目录已检查；不是机构全部历史保证。旧 Descript core 不重读、不迁移 Mar06。 |
| SRC-ANTHROPIC | [Research raw](./SUP_ANTHROPIC.raw) embedded publishedOn/slug 历史 Mar13 diff-tool → Mar06 Mozilla/exploit → Mar05 labor；[Alignment](./SUP_ALIGNMENT.raw) 只读 March 5 标题段，逐个官方页日期核。 | Research 可见段已检查；Alignment 4 日期明确窗外，1 月份级潜在事件日期隔离，见下。 |
| SRC-GOOGLE-AI | [DeepMind pubs](./SUP_DEEPMIND.raw) 页1相邻 Mar10 → Feb15；[Blog page3](./SUP_DEEPMIND_P3.raw) March 相关标题段，对应旧有效 Source 的 Mar10 AlphaGo/Mar03 FlashLite 日期不重审正文。GoogleResearch [March页1 web](./SUP_WEB_RECOVERY.json) 12 项，日期 Mar31→Mar06，相邻 Mar11→Mar06；页2新 curl timeout/web不可达，复用 [旧本日有效 Source](./V3_SOURCE_STOPPOINT.md) 已核 2/2 Mar06 SpeciesNet/Mar04 Bayesian，不继承旧候选。pubs web实际 1–15/11600、2026 年396，只有年/标题排序。 | 有限 Blog/pub 入口已处理；pubs 必要日级切片仍隔离，不能把396年项扩池。 |
| SRC-META-AI | 新 curl SSL 错误；[web](./SUP_WEB_RECOVERY.json) 官方 Research 0 行；本窗官方域模型/架构/训练补检没有恢复历史目录。 | 必要历史 Research 外部隔离；search 空不证明零覆盖。不重复旧无浏览器 surface 尝试。 |
| SRC-QWEN | [真实 API raw](./SUP_QWEN.raw) 返回40/40，title/extra.date/embedded datePublished 对读，display Feb16 Qwen3.5 → Mar19 MaxPreview，无 Mar07；Blog内嵌 Feb14 与display不一致保留，不据display归论文首公开。 | 返回切片已检查，没有额外分页接口/机构全历史保证；旧 PR2021/2059 有效判断复用，不重读正文或再次评分。 |
| SRC-DEEPSEEK | [Research/News raw](./SUP_DEEPSEEK.raw)：Research10项 Jun24→Feb25 DualPath；News5项 Sept10/Apr24/Dec01 等，停 View All。 | 可见段已检查；隐藏 News/APIupdates 历史未恢复，外部隔离。 |
| SRC-MOONSHOT | [Kimi Blog raw](./SUP_KIMI.raw) 19项，Apr20→Feb09，最老2025Jan20，无可见未完分页。 | 有限可见目录已检查；不授删除历史/机构全历史。 |
| SRC-TENCENT-HUNYUAN | [publicList raw](./SUP_HUNYUAN_ALL.raw) POST renderType0/page1/size20，totalNum11/list11；display Feb13→Apr23，无Mar；初始Research JSshell不当零响应。 | 当前“全部”目录已检查；updatedAt/display不互替首次公开日期，不全文审11项。 |
| SRC-ZAI | [Research raw](./SUP_ZAI.raw) 首可见15项，Mar15 Turbo→Feb21 GLM5，停查看更多。 | 有限可见段已检查；不授隐藏完整历史。 |
| SRC-BYTEDANCE-SEED | [token0 raw](./SUP_SEED_P0.raw) 20项 Jan20→Feb25；[token20 raw](./SUP_SEED_P20.raw) 本次14项 Feb27→Mar26，next40/has_more=true/total82；按 display/BJT日期邻接 Mar01→Mar12，跨窗后停止。 | 真实有限历史切片已检查；不遍历剩余82，display可能回填不是论文首公开证据。与旧返回38差异不凭空解释为新增/删除事件。 |
| SRC-BAIDU-ERNIE | [页1raw](./SUP_ERNIE.raw) May09→Apr15→Feb06→Jan29→2025；错误 ?page=2 返回相同页不作翻页成功，随后[真实 /page/2/](./SUP_ERNIE_REAL_P2.raw) 更老2025段。 | 有限有序段已检查；本窗无可见目录项，不授全机构。 |
| SRC-XIAOMI-MIMO | [Paper/Blog raw](./SUP_MIMO.raw) 8 Paper，Mar13 ARL-Tangram→Feb03 HySparse；15 Blog相关标题/More无日级日期。本窗主题补检未恢复。 | Paper 可见段已检查；Blog 日期历史切片外部隔离，不以版本号推公开日。 |
| SRC-MINIMAX | [Blog raw](./SUP_MINIMAX.raw) current→Mar18 M2.7→Feb14 Forge/Feb12 M2.5→2025Oct27；补检命中用户space金融目录不属于机构研究。 | 有限有序段已检查；不认证 Agent子站全部历史。 |
| SRC-ARXIV | [官方 availability raw](./SUP_ARXIV_AVAILABILITY.raw) 明确Sunday–Thursday公告、Fri/Sat无常规new/replacement/withdrawal/crosslist/jref；Mar07 BJT为Fri06Mar11EST→Sat07Mar11EST，无对应常规批次可浏览。8条topic日期同义补检见下，结果仅ZeroFolio线索。 | 常规批次0，不用Submitted/updated/registered/月号；补检不证明全网off-cycle无事件。没有窗口批次，不把March全类列表变题摘队列。 |

## 查询与有限标题补检

[ARXIV1](./SUP_WEB_ARXIV_1.json)：4条 `site:arxiv.org "7 Mar 2026"` 分别加 `(language model OR Transformer OR MoE OR optimization OR theorem)`、`(GPU OR serving OR inference OR training OR kernel)`、`(multimodal OR world model OR VLA OR diffusion)`、`(agent OR memory OR retrieval OR planning)`；每条只读返回结果页，无后续分页。只命中1条ZeroFolio。

[ARXIV2](./SUP_WEB_ARXIV_2.json)：同四主线加日期同义 `(March 7, 2026 OR 7 March 2026 OR 2026-03-07)`，系统加入compiler/parallel，Agent加入collaboration。四条返回空；只是有限索引限制，不授无遗漏。未重试已知失败advanced日查询、catchup或all-class API。

[OFFICIAL](./SUP_WEB_OFFICIAL.json)：四条官方域分组（OpenAI/Anthropic/Google，Meta/Qwen/DeepSeek/Kimi，Seed/Hunyuan/ZAI，MiMo/MiniMax/ERNIE），每条限定 `(March 7 OR 2026-03-07 OR 3月7日)`、2026与model/agent/training/architecture。命中主要为窗外卡片、Alignment目录与用户space财经目录。相关标题补检由以上真实官方有序目录与Alignment March段承载，不扩全年/全机构正文。

## 首批准入与代表排除

实际进入完整题摘语义检查的2家族：Abstractive Red-Teaming 与 ZeroFolio。另4条Alignment只核完整官方标题/页首日期，明确Mar23/11/10/5窗外后不读其正文。下载core不计全文审阅完成。

- **潜在贡献 / 日期隔离：** [Abstractive Red-Teaming of Language Model Character](https://alignment.anthropic.com/2026/abstractive-red-teaming/)；[官方 core raw](./SUP_ALIGN_ABSTRACTIVE.raw) 和 [完整 arXiv题摘/版本](./SUP_WEB_DATE_ABSTRACTIVE.json)，精确身份2602.12318v1。固定eval对稀有自然失效召回低、单query优化可能失真 → 按自然query类别搜索（CRL类别generator策略梯度，QCI从高分query经验池归纳category并探索）→ 需要重新考虑character审计在自然性与失效频率上的取舍，潜在owner PLATFORM-EVALUATION-SYSTEM。不是仅mapping或成熟workflow类比。Blog仅`March 2026`，无日级datePublished；关联arXiv仅Submitted/v1 Feb12，不能当公开日。一轮有界官方abs+官方/作者域dated公告搜索未恢复精确公开日期；不再全文补偿日期。root独立准入校准通过；日期隔离不评分、不列确定候选、不Books、不授Coverage/Evidence。请求本Blog官方日级首公开/重要修订日期及对应内容身份，或可核验的有日期作者原稿/官方公告；只重开该事件。已读core可复用。未把月份当Mar07，更未将提交日映射到本窗。
- **EX / 范围与贡献前关闭：** [Algorithm Selection with Zero Domain Knowledge via Text Embeddings](https://arxiv.org/abs/2604.19753)（ZeroFolio）。[搜索返回完整题摘](./SUP_WEB_ARXIV_1.json)及[当前官方v3完整题摘/版本页](./SUP_WEB_ABS_ZEROFOLIO.json)实际是原始实例serialize→既有pretrained embedding→weighted KNN做SAT/MaxSAT等algorithm selection；embedding借用既有能力，消融line shuffle/距离加权没有给foundation表示学习/训练/推理系统或LLM Agent的新机制/有效性边界。不是因为是小模型、负面/理论或没有owner而关闭。当前v3题摘的10→9/11等评价叙述与搜索旧题摘不同，具体数值不采用；这不改变上述机制与项目范围判断，且v3 Oct05 revision不是Mar07事件，不沿此扩读窗外全文。官方当前页未显示撤回/安全说明；Submitted Mar20与IDApr均不当公开日，已明确贡献排除，日期无需另追。只保留发现身份，不评分。
- **标题明确范围外：** MiniMax用户Space“ A股数据分析系统”是金融行情/持仓目录，不是MiniMax官方研究发布；领域应用不能经cost/evaluation泛owner回收，未读其正文。
- **日期窗外，不贡献排除：** Alignment [Coding audit realism](./SUP_ALIGN_REALISM.raw) Mar23、[A3](./SUP_ALIGN_A3.raw) Mar11、[AuditBench](./SUP_ALIGN_AUDITBENCH.raw) Mar10、[3 Challenges and 2 Hopes](./SUP_ALIGN_CHALLENGES.raw) Mar05，原始官方日期足以排窗，不追时分秒、不声称已审全文、不路由新任务。Qwen3.5/AgentWorld、DeepSeekV4/V4.1、Gemini3.7等搜索线索不凭宽search命中迁移为Mar07。

## 来源外部隔离与复用

四组必要外部源材料：GoogleResearch日级pubs、Meta历史Research、DeepSeek隐藏News/APIupdates、MiMo有日级日期Blog。当前可用官方目录/raw/web入口有限尝试后仍缺。恢复材料为覆盖Mar07的官方有日期历史list/API或明确公开日的原始事件说明；官方明确日期即可，不要求时分秒。隔离项不支撑无遗漏、性能安全或Books正面结论，不算Coverage通过。Google March页2的新网络失败不推翻旧有效2/2 Source结果；只复用不变身份/可核的目录事实，未复用别日候选。

旧原报告 §4/Source/PRE/POST有效结果均复用；Qwen同release/PR的旧重复与关闭不重读、不重评分，BrowseComp/Descript官方Mar06事实足以判补充Mar07窗外，不要求旧零点确时，不改原 §4。无确定新增候选、无新增评分/证据审阅/Books写入；Abstractive日期保留不是无贡献结论。

## 交接

本日源扫描/筛选已结束，确定新增0，完整题摘2=潜在日期保留1+EX1。root首批准入校准与完整非作者六部分DAY已通过；README状态完成，不继承旧通过为本轮证据。独立复核需检查14实际源范围、上述具名日期/potential/EX、四源+一材料隔离、原窗口/候选/§4冻结、Books无新增与机器验证，不验全互联网。root验收后本日结束，不领下一日。

最终本地验证：完成态V3校验1份通过；原窗口、原§3与原§4连续正文逐字一致；README+supplement本地引用63个全部存在；本日限定unstaged/cached git diff --check通过。首次完成态检查因§5缺少显式“终态保留项”标签失败，定点核校验器规则并补正标签后重跑通过，不改任何研究/隔离判断。作者检查不替代语义/非作者DAY，未stage/commit/push。

本轮复核者：root（非作者）；结论：通过。root实际对读本日补查与README、14抓取/恢复记录及停止范围、OpenAI1257日期字段、Qwen40/Hunyuan11当前返回、Kimi/ERNIE/MiMo/MiniMax邻接与availability；完整读Abstractive官方core及官方完整AB、ZeroFolio当前v3完整AB，校准月份/Submitted不授公开日、category搜索潜力隔离与领域embedding+KNN具体EX。四日期明确Alignment不授全文已读。拟入选0，无新Books写入；四源与一材料继续安全隔离。未全审隐藏历史/全类库存，普通工作0，不称无遗漏。
