# 2026-03-15 增量来源独立复核

复核者：review_mar15_16（非报告作者 supp_mar15）。本次仅补 2026-03-14 北京时间完整自然日；原0候选、日期、评分、小时窗口及连续 §4 冻结，不迁移旧归属。只 own 此独核记录，不改日报、Books、Learning State、索引或 Git index。

## 1. 上下文、查询范围与首批校准

本日启动及从3/16切回时均完整重读 AGENTS.md、RESEARCH_CONTRACT.md、REPORT_CONTRACTS.md、CODEX_RESEARCH_PROMPT.md，重读来源使用说明、每日组和arXiv路由；ROADMAP及今日恢复 checkpoint 已核。原报告六部分、V3_SOURCE_STOP、V3_ARXIV_QUERY_STOP 已读；旧三项有效关闭只作判断复用，旧完成label不替新Supplement验收。

实际核对四个 SUP_API_*_20261011.json：均 submitted UTC3/13 00→3/15 00 缓冲、start0/max200/ascending，分别121/76/27/108条与total相等，无分页截断。主题覆盖模型学习、训练/推理系统、多模态及Agent/评价；kernel等宽词引入范围外线索，但作者未把所有返回项送入逐项AB或日期关闭队列。332是跨查询出现次数，不是去重家族、完整题摘或候选分母。Submitted/latest_updated只供发现，不能证本窗first-public。

收到 [首批包](SUP_ADMISSION_20261011.md)后，独立实际读取 [exact-v1原证](SUP_AB_SAMPLE_20261011.txt)中12529、13423、13426、12567完整题摘及header/history，另读 [12694单页](SUP_AB_RXNRECER_20261011.txt)完整题摘及history：

- **12529v1 TERMINATOR**：以首次答案位置构造模型/任务相关的退出长度数据，潜在改变CoT终止与质量/成本判断；不只是章节映射。不采用摘要的收益归因或泛化保证，未确认03-14first-public，保留具名日期门，不评分/Books。
- **13423v1 KWM**：递归Bayesian filtering/Kalman gain代替reverse-mode AD，模型状态innovation与在线训练关系是具体替代设计潜力；未核稳定性/复杂度证明及实验，不能称Evidence完成。未确认03-14first-public，日期隔离。
- **13426v1 OATS**：离线向成功query centroid插值tool embedding，并报告稀疏outcome下MLP匹配或变差，含机制及负面成立边界潜力；不能因小模型、局部数据或Work in Progress排除。不采用zero-cost泛化结论，日期隔离。
- **12567v1**：精确题名为 *Accelerating materials discovery using foundation model based In-context active learning*，不是API最新版改名标题；完整AB是用已有TabPFN替代GP/RF做材料实验主动学习与不确定性评价。AI for Science暂缓范围关闭成立，不能借foundation或TRAIN-DATA回收；不因组合标签泛排，不评分，不追不影响处置的日期。
- **12694v1 RXNRECer**：完整AB是绕过EC标签映射、用protein LM/active learning直接预测酶反应及解释，属于科学应用。范围关闭成立，未建立本项目foundation学习或系统新增约束。首次多页只给header不是AB完成；后续单页已补齐并由本复核者实际读，现应记为完整AB EX。

上述原证显示的轻量header/comments没有撤回或明确纠错信号；12529v2与12567v3存在不自动成为本窗重要修订，不强比较全版本史。该首批全部5项均实际独读，不宣称对其余标题线索或附件全量复核。

## 2. 日期权限与本批结论

独立新读 [官方 availability](https://info.arxiv.org/help/availability.html) L170–186。BJT03-14没有常规公告，只说明常规arXiv事件日程，不证明全部作者原发/异常事件为零。官方abs的Submitted及共享DOI+schedule derived Mar16/17均不当本窗first-public证明。月份目录不能仅凭开头片段证明本窗相关slice；历史slice与3具名potential日期缺口应精确隔离，得到原始公开日才重开对应身份，不迁归其他日、不全March catchup。

首批准入结论：3具体机制potential的日期隔离、2完整AB科学范围EX及查询/队列边界通过。已通知作者将首包末段过时的“1完整AB+1标题EX”改为“2完整AB EX”，并保留12567v1实际题名/最新版家族发现的区分。新增确定候选0；此处不授候选Evidence、Books或完整日报PASS。

## 3. 最终14源与六部分 DAY

作者同步实际增量后，已非作者顺读正式 README 完整六部分及 SUP_SOURCE_STOP_20261011.md、SUP_DATE_LIMIT_20261011.md，核新查询参数和有限停止、旧字段复用权限、具名准入与必要日期隔离、0增量及Books决定。正式报告明确旧完成仅原检查，不授新Supplement完成；§2明示2026-10-02字段复用与本轮恢复分开，无90天catchup、宽列表逐项关闭或Weekly队列。

实际读取本日旧 V3_PUBLIC_DIRECTORY_FIELDS.json（RSS切片/Qwen40/Hunyuan11及辅助DataCite）、V3_SEED_FINITE_FIELDS.json 的18字段和 V3_SEED_BLOG_FINITE_FIELDS.json 的14字段。它们支持本日记录的有限邻接与入口范围，不授当前全机构历史。新 Anthropic 十publication及See more同页原值、Google年份/排序/首15原值与March Blog邻接、Meta当前0行/出版入口错误及MiMo旧单篇日期均已定点核对；其余未变化的既有有限来源判断按合同§7复用，未重新题摘/全文全量认证。

独核发现多页工具原packet只保留 MiMo/MiniMax URL与Total lines，Seed新的US curl没有保留安全字段，不足支持新的当前事实。已要求作者补齐，随后实际读 [MiMo相关Paper8/Blog15完整目录](SUP_MIMO_DIRECTORY_20261011.txt)、[MiniMax三日期卡](SUP_MINIMAX_AGENT_DIRECTORY_20261011.txt)及 [Seed本轮14安全字段/total19/空next](SUP_SEED_BLOG_FIELDS_20261011.json)。原件支持新状态且不外推历史为0；缺5及无日期Blog历史slice仍隔离。无需扩大扫描或改动旧Source有效结果。Google当前2026=406与旧372、Meta当前Internal Error与旧timeout的措辞已通知作者分清，不改变其隔离处置。

分层准入实际检查5/5新增定点完整AB（3日期潜力、2科学范围EX）；不是332元数据行的全量题摘复核。全部拟新增确定candidate为0，没有未读必要候选Evidence或新增Books命题/修改；无Books写入待POST。旧三EX有效范围/重呈现判断复用，不把它们升为新Evidence完成。七来源历史限制及3具名日期门可作外部终态保留，明确不支持正面证据、Books、当天零研究或互联网无遗漏，恢复只到该来源该窗/具名family。

机器检查实际执行：本日报告V3 validator通过；限定日报/本日_sources的cached与unstaged diff-check无输出。原窗口逐字一致，原§4连续前缀与冻结文件比较通过；原0候选表结构不变。机器只验证接口/冻结/空白，不代语义复核。未stage、commit、push，未写共享文件。

**DAY结论：通过。** 本轮原0＋新增确定0、Books新增0、普通扫描/筛选/候选证据/Books/独核待办0。作者可依此把正式报告同步为完成和§6通过；精确隔离项继续保留，不授全Coverage/Evidence或无遗漏。当前通过针对实际所读增量和必要终态，不是旧完成标签。

## 4. Anthropic 单源窄重开后的最终 DAY

root指出Research同URL嵌入公开日期可作安全恢复后，仅重开此来源；上节七来源限制为恢复前事实，其余5份AB、有效邻接及原§4不重复审阅。切回本日再次重读适用合同与每日来源/arXiv路由。实际读本日一次curl保存的 [174唯一publishedOn+slug安全字段](SUP_ANTHROPIC_PUBLIC_FIELDS_20261011.json)及全部9条March日期，逐一核UTC→BJT：03-05晚间归03-06，03-13T10:15仍03-13，03-23T23归03-24，03-31T22归04-01；无03-14。174是去重字段对，不与3/16的177原字段强作同一计数，不扩大为文章题摘队列。

已读README对应§1、Anthropic来源行、§5完整保留项与§6，以及本日sourceStop同步部分。当前嵌入列表窗口切片可恢复，撤回“Anthropic必要历史切片不可得”这个缺口；浏览器10卡限制不再覆盖已恢复HTML事实。但这些字段不证明删除事件或全机构历史无遗漏，也不授正文贡献/证据审阅完成。剩余为Google、Meta、MiMoBlog、MiniMaxAgent、Seed差额5及arXiv共6来源限制，另3具名日期门不变。无新增候选或Books。

本日V3校验重新通过，限定README/day_sources的cached与unstaged diff-check无输出。**最终DAY：通过；原0＋新增0，Books新增0，普通可执行待办0。** 该结论包含本次单源增量，替代上节恢复前限制数量；正式报告可同步完成，精确外部终态保留项不作Coverage/Evidence通过或无遗漏保证。
