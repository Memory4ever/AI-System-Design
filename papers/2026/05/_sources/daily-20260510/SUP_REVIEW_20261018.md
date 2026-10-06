# 2026-05-10 来源补充：独立复核

复核者：`may10_supp_reader`（非报告作者、非 Books writer）

## R1 — 独立上下文与日期/去重校准

已完整重读本仓 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、统一入口、ROADMAP，读取 RESEARCH_SOURCES 使用说明、每日14源与 arXiv 主题/恢复说明，以及 LEARNING_STATE 最新相关恢复段。后已定位确认应读§“2026 年已有 Daily增量来源补查／本次恢复2026-10-18”的128/279路由，下方113/279是旧快照，不覆盖当前。只接本日材料，不采用 Weekly 材料或规则作本日判断。使用 using-agent-skills 的范围/验证纪律；本任务是研究语义复核，不执行代码或产品发布流程。

本轮保原小时窗口 `2026-05-09T09:00:00+08:00 ～ 2026-05-10T09:00:00+08:00` 与原0候选、有效连续§4。新增补查独立处理 `2026-05-09 ～ 2026-05-09` 北京时间完整自然日。原空表不构成禁止新增候选的理由，旧小时窗排除也不能自动沿用到自然日。

实际打开官方 [ERNIE 5.1 发布正文](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)，读完核心 Technical Features（elastic depth/width/sparsity、四子系统异步RL、FP8/R3、MOPD与General-RL分流）。页面标示 May 9；本日原材料保留的 metadata 为 `2026-05-09T00:00:00Z`。该事件落本轮补窗，但定点实读相邻 [05-09 日报](../../09/README.md) 原 ERNIE 整行及对应完整证据段，确认精确同URL、同事件、原7分与深入完成/具体已有覆盖已有效保留。故按同事件有效审阅去重，不在本日新增候选或重复评分，不重审其未变化有效 Books 层。这里只作允许的跨日去重，不引入05-09新增队列。

实际打开 [arXiv 官方 availability](https://info.arxiv.org/help/availability.html) 全部相关段：公开由 scheduled announcement，包含 new/replacement/withdrawal/cross-list；常规公告仅周日至周四20:00 ET。May09北京时间自然日对应May08 12:00～May09 12:00 EDT，其中没有常规batch。该事实只能限定常规batch，不能把 Submitted 当公开，不能证明不可能存在真实延迟/其他官方原稿，也不替代13个机构来源检查或历史公告slice。当前尚未取得全部新增发现/代表C与14源实际停止依据，R1不是DAY或FINAL。

未核代码、未复现实验；不stage、commit、push。所有其他文件与并发修改保持。

## R2 — 具名窗外条目与旧有效层边界

实际打开 [2605.09233 当前官方事件页](https://arxiv.org/abs/2605.09233)，核身份为 *Towards Robust Sequential Decomposition for Complex Image Editing*，读完整题摘及版本/Comments：v1 submission `Sun, 10 May 2026 00:23:05 UTC`、v2 `Mon, 1 Jun 2026 19:32:07 UTC`，当前页未见撤回/纠错标志（非全版本逐字核验）。此submission不能冒充实际公开，但它和旧 Seed 展示日期 `2026-05-10` 都不是本轮May09自然日的正面日期证据，不据此新增本日候选。未因该稿与多模态主题相关就授贡献/评分，亦未把它记为已深入完成；若出现May09更早原稿/发布的具体证据，只重开其资格。

实际读回本日旧 `V3_INDEPENDENT_FINAL_AUDIT.md`，它限定旧小时窗而不是本轮自然日；436 identity/57旧packet/29旧queue只是保留的历史取证，不是本轮候选池或逐项全文队列。旧时分归属表述如需留存，应与新增补窗事实分开，不能把其零候选结论升级为当前全来源零命中。

## R3 — A2实际首批校准与A3机构来源范围

实际读取作者 A1–A3，首批没有确定新增P。ERNIE有效事件去重及09233完整题摘/日期层见R1–R2，不因零P免除独核。实际打开MiMo官网，具名 `How Xiaomi MiMo-V2.6-Pro Boosts Productivity in New Materials R&D` 卡的核心说明为文献、分子设计及PFAS dry-lab：ROADMAP暂缓的科学应用，不因Agent标签重入范围；此明确范围C无需另请求不影响处置的历史日期。其余无日期技术卡未据此排除，也不称全文核过。OpenAI社区支持噪声未作为论文或候选队列；已请作者至少补具名标题/URL，不把类别说明算逐项摘要审阅。

对14源表逐行核入口、停止及权限；下列独立重取核其最易误判字段：Qwen API40行的全部id/title/extra.date，data只有articles无next，不按无序数组相邻位置判断，核真正跨日邻接Apr30 Scope→May19 LiveTranslate；Hunyuan publicList成功code0、total9/实返9、全en，核九displayPublishTime且不拿created/updated替公开；Zai网页工具超时后direct恢复，实见列表04/29 Scaling Pain→05/20 ZCube；Anthropic实际embedded两publishedOn原字段与slug；MiniMax当前列表03/18→05/26；DeepSeek Changelog04/24→07/31；MiMo Paper03/13→06/29；Moonshot Blog最晚2025/11/07。Qwen、Hunyuan等当前响应只支持各自具名切片，不授所有语言或删除历史完整性。

独立实际打开OpenAI/DeepMind/Google Pubs当前页及Meta0行，确认这些不是May09完整日归档；不以当前精选、年份过滤、空页或搜索空证明零事件。Seed API实际重取type1 page0/20与type2 page0，核18/20/15实返、total86/86/20、next20/40/空及has_more真/真/假；type1第二页日字段跨May16至Apr15（1667 May10），支持有限停止，不抹平total差额。未把53条目录条目当53篇本日初筛或全文队列。此处未无差别深读所有窗外附件；本日arXiv有限主题与十二类邻接补检仍属普通未完成，尚不授DAY。

作者后补两具名社区URL，已实际打开核 `Frustration with short free limits` 与 `Cool Feature Request ! Hierarchical Projects`。前者用户额度/回复体验，后者嵌套项目功能请求（原postMay02、May09为回复），非原始研究；日期搜索返回它们不能证明May09研究命中。此两条抽核只覆盖具名噪声，不冒全站初筛。

## R4 — A4发现收口与日期工具权限：通过有限处置

实际读取A4全部内容及 `datacite-registered-window-20261018.json`。作者四个同起止日advanced响应是表单失败，不能记四次0；公告筛选只支持year/month的限制也不许可改用submitted日期。有效月表路径是`/list/<cat>/2026-05?show=2000`，我此前web旧`2605`404/新式超时后，实际direct重取CL与OS：分别total2844与29，页面标题为Authors and titles for May 2026，非May09日列表。作者十二类只核页形状/总量、没有读完月表题名，不授月表全文覆盖或十二类召回。无需把本日无batch问题扩大为整月逐项关闭队列。

独立重取DataCite有效REST `client-id=arxiv.content` + May09完整BJT自然日UTC界 `2026-05-08T16:00:00Z TO 2026-05-09T15:59:59.999Z`，核total0/data空/无next，与已保存JSON一致。独立重取同过滤May08控制，核total1461/sample `10.48550/arxiv.2605.06476`、findable、client=`arxiv.content`、registered=`2026-05-08T13:29:46Z`。这只验证过滤器并限定登记发现切片，不是论文实际公开或不存在延迟的证明，不展开该控制日论文池。初种`client.client-id` query的共同0已被有效控制排除，不沿用阴性权限。

A4已把普通发现完成与历史异常公告slice区分：当前无具名待查May09候选；无常规batch、有限机构入口和具名事件判断可安全收口，而arXiv精确日级/异常延迟历史slice继续隔离，不支持正面Coverage/Evidence/Books或无遗漏。重新取得官方May09公告/状态归档或具名原始发布才定点重开。没有把尚可执行的解析或未读候选改称外部受阻。此层通过只允许合并报告；完整六节DAY与保存完成态FINAL尚待实际执行。

## R5 — 完整六部分DAY：通过

实际从开头至§6连续读完作者保存的进行中README，非仅diff/状态卡。确认：原小时窗保持；新增May09完整自然日与授权说明明确；原0＋新增确定0、Books新写0并非全网无研究或受阻来源阴性保证；14源逐行自包含有限范围、停止与缺口；A2具名去重/范围/日期校准及A4权限已体现在结论/候选/证据/缺口；没有漏入确定新候选、待审普通材料或未落实Books写入。ERNIE在补窗内但同事件有效旧审阅去重，不搬归属或重评分；旧436/57/29不变成本轮待全文队列；09233留窗后定点线索，不冒已核首次公开。

原§4存档边界和当前组合日期判断已分开，旧块保留不提升为本次来源/日期规则。来源外部限制均没有用于正面Evidence/Books/性能安全或无遗漏保证，重开条件具名且只影响对应slice/family。没有新Books写入，故无新增PRE/POST或需要假签的书稿检查；旧ERNIE有效层按R1复用。

独立实跑V3通过（仅结构/可判定一致性）；限定本日README与来源目录的cached/unstaged diff-check均通过。以基线提取并trimEnd的671字符原§4正文在新§4连续命中，原小时窗口逐字相同，候选行0，本地引用7/缺失0。当前§6仍有“A4尚未全部通过”旧行政文字，随本DAY既成事实一次同步，不是新研究待办。作者可将状态/结论/§5/§6同步为已DAY通过与等待保存态FINAL；待其保存后我再一次实际FINAL，当前不预授FINAL或已完成保存态。

## R6 — 首次完成态实际回读：一项格式修复待办

实际读取18:15:46+08保存完成态开头/结论/§5/§6及作者停点，研究、Books和隔离边界没有改变，限定cached/unstaged diff-check仍通过。但重新运行完成态V3失败：§5写“终态来源保留”，未命中校验器对完成报告的“终态保留项”受控字段。内容实际已隔离外部来源、非正面Evidence/Books/无遗漏并有重开条件；请作者仅改前缀为“本窗终态保留项／来源限制”，不放宽校验器或改变研究结论。当前不签FINAL；修后只回读该最小差额与重跑完成态校验，不重审已有效R1–R5。

## R7 — 保存完成态FINAL：实际通过，ownership释放

作者仅改§5前缀后，实际再次读取保存完成态开头/结论/§5/§6：状态完成、原小时窗/May09补窗与授权、0＋0候选/Books0、普通研究/Books0及所有外部隔离/重开条件保持；“本窗终态保留项／来源限制”已落正文。重新实跑完成态V3通过，限定本日cached与unstaged diff-check均exit0。R6唯一格式待办已关闭，R1–R5有效研究/完整DAY未被改动，不重复原件或书段检查。

本日审查结论：通过。最终范围是本轮14源有界停止与权限、全部确定新候选0的真实处置、具名代表C/同事件/日期边界及相应有限原域、完整六节DAY和保存完成态FINAL；不冒全量月题名审阅、全版本审阅、代码核验、实验复现、全部语言/删除历史或无遗漏保证。没有新增Books写入、锁或未落实POST。作者可只把“FINAL待回读”的行政文字同步为本R7既成结果，不新增重复收据或研究复核。reader本日ownership释放，不自行接其他日期，不stage、commit、push。
