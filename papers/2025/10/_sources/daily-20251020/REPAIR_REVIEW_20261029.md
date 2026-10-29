# 2025-10-20 增量修复独立复核

唯一非 writer reader：Euler `01a185cf-0162-7150-a474-44c004c8cf2f`；唯一 writer：Franklin `01a185cf-00e1-7360-b767-03624e04713f`。仅本日补窗 BJT 2025-10-19。此文件为 reader canonical，writer canonical 为 `REPAIR_20261029.md`。原生 agent send_input 本环境不可用，按用户授权通过同日 canonical 协作，不调用 app 消息工具。

## R1 启动与可复用层

已实读 AGENTS、当前 Research/Report 合同、Prompt、Sources 使用说明/每日/按需/arXiv 范围、ROADMAP、LEARNING_STATE 最新 2025 路由及本日 README、CURRENT_STOP、SUP_SCOPE、SUP_ARXIV 和 SUP_INDEPENDENT 的已有层。只读本日材料；不把旧年度分子、旧 root 身份或旧完成标签当本轮完成依据。

旧 112 题摘、四具名恢复、69 新 AB/五 title-C/七 overlap 的既成校准，以及十一必要 v1 反侧按身份/版本/采用命题复用。尚无新当窗准入或 Books 提案，不重全池 Methods。旧小时窗、候选完整行和有效连续旧 §4 保留，不冻结旧空表结论。

需 writer 优先处理的实际缺层：

1. 旧日期规则将 DataCite 一概排除，不符合现合同。对具体潜力恢复精确 DOI、arxiv.content/findable/registered 与唯一 v1、适用 2025 公告日程的合法联合界；只排具体事件，不用 ID 月份/Submitted/created 独断。
2. 旧发现五主题仅 submitted_date，尚无 registered 同主题同窗差额发现证据。请保有限原主题及同义词、查询/分页停止与原件；created/registered 必须按各自字段实际核，不以单篇日证可解替发现完整。无需扩成全分类或全 Methods。
3. Hunyuan 优先复用本日真实中文 `zh` 原件；本日现有 `hunyuan_publicList_p1.json` 是英文九条，不是中文 All。旧 SUP 中文 UI/JSON 十一条已有实际校核，须读实际形状、全部中文字段及停止；只证明当前目录，不授 2025 历史零事件。

本轮尚未 DAY/FINAL。writer 可继续未成发现/日期层，准备即写 canonical；reader 不抢 writer 首必要。后续只有新增具体长期论点才进入完整 PRE/实际 SAVE/actualPOST。无 Books 时不制造 PRE marker。最终须当前六节实际 DAY、writer 真实完成 SAVE/全文自读 QA、reader 磁盘 actualFINAL。此记录不是行政批准或完成声明。

## R2 接 W1 互斥首必要

已实际读 W1：reader 接受 2025 arXiv 公告/最终 ID 规则与 Hunyuan 中文 All 首必要；writer 独占五有限主题 created/registered 发现及个体联合日证首必要。reader 已实际解析本日旧 `SUP_SOURCE_HUNYUAN_ZH_UI_20261015.raw`，真实 data.totalNum/list 为 11/11、每项 lang=zh；旧 `hunyuan_publicList_p1.json` 的 en9 不代替此层。正按 W1 补 pageSize100 的同形请求与历史规则固定 commit 原件，完成后写回实际结果。

## R3 首必要实际完成：2025 规则与中文 All

### 适用 2025 的原规则

实际取得并完整读取 [2025-01-06 固定 commit 原件](./READER_ARXIV_RULE_20250106_20261029.raw.md)，来源 `https://raw.githubusercontent.com/arXiv/arxiv-docs/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md`；GitHub HTML 的 web cache miss 不冒成功，随后 raw HTTP 成功，2428 bytes。原文件列 2025 Holidays，已含最终 ID 不可在 announcement 前分配、月号不能 back-date、moderation 可延期及完整日程。具体日程：周一至周四各 14:00 截止后当日 20:00；周四14点至周五14点的提交周日20点；周五14点至周一14点的提交周一20点。均 Eastern US，不能误写周五公告。

同时实际打开当前 availability 原页与 DataCite 日期定义原页；后者明确 registered 是 global handle server/findable 登记日，created 是记录创建日，draft 后转 findable 时两者可以不同。2025 原文未显式写 DOI，但有最终 ID 的公告前禁配；当前原文明确 ID/DOI，和现合同的精确 DOI/arxiv.content/findable/registered 联合界相容。不将登记字段重命名为实际公开时刻。

2025-10-19 Eastern 为 EDT (UTC-04:00)，周日20:00 对应 BJT 10-20 08:00；常规日程在 BJT Oct19 无批次，但这**不排除先前稿件延期、其它官方发布、既有稿具体修订或历史目录缺段**。对具体唯一 v1 只给最早可能界，仍需精确 registered 最晚界且 earliest <= latest、整个区间在同一 BJT 日。不得从“周末”直接清池。writer 可复用本规则，不重复首必要网络。

### Hunyuan 本日真实中文全部

reader 新请求 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，header `accept-language: zh`、JSON `{"pageNum":1,"pageSize":100,"renderType":0}`。原始 [headers](./READER_HUNYUAN_ZH_ALL_20261029.headers) 与 [JSON](./READER_HUNYUAN_ZH_ALL_20261029.json) 均实存；HTTP200、code=0、data 只有 totalNum/list，totalNum=11、list.length=11，全部 lang=zh。本日旧 API chunk 实际是 `/api/blog/publicList`，list chunk 的全部页签 renderType=0、翻页参数 pageNum/pageSize 与响应 data.list 形状已核。总量已读完，停止 page1，不虚构 hasMore 字段。与本日旧 ZH_UI 原件的 id/lang/title/三时间字段逐项比较相等，不借别日目录分母。

全部十一项标题与展示日 (BJT)：

| ID | 中文目录实际标题 | displayPublishTime 对应日 |
| --- | --- | --- |
| 100119 | Hy Image3.5 preview 发布：为专业创作提供高性价比模型 | 2026-09-22 |
| 100116 | 当大模型强化学习走向规模化，Batch Size Scaling 有什么不一样？ | 2026-09-22 |
| 100100 | Hy4 preview 发布 | 2026-08-28 |
| 100091 | From LR to ELR: A Better Heuristic for Pretraining Dynamics | 2026-08-11 |
| 100087 | Hyra: 简单有效的科学发现智能体 | 2026-07-21 |
| 100064 | Hy3 正式发布 | 2026-07-06 |
| 100041 | Hy-MT2：面向实际应用场景的高性能多语言翻译模型 | 2026-05-21 |
| 100039 | Real life is where context gets hard | 2026-04-30 |
| 100061 | Hy3 preview : 混元大模型重建的第一步 | 2026-04-23 |
| 100015 | Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping | 2026-02-13 |
| 100025 | Learning from context is harder than we thought | 2026-02-03 |

三时间字段全部实际转 BJT 阅读，均 2026；100061 publicAt=2026-07-05T17:44:54+08:00、publishedAt=2026-06-24T21:42:37+08:00、display=2026-04-23，明确不能互代。100087 display 比 publicAt 后一天亦保原角色。未读未来正文、不授十一篇 Evidence。**中文 All 当前有限目录层通过；2025 历史仍缺段，不支持 Oct19 零事件/全部 Coverage。** 旧英文九、默认响应或 UI 壳均不替代此结果。后续只在出现目标历史具体官方目录/原发布时定点重开，不为已成中文层重试。

R3 不替 writer 日期/发现结果或 DAY/FINAL。下一直接接 writer 有限批次的原件支持/反侧独核。

## R4 后到发现原件的有限支持检查

已实际读 `repair-discovery-20261029.mjs`、`REPAIR_DC_FETCH_20261029.json` 十项完整 URL/执行时刻/HTTP/返回总量：五 title 主题及单复数同义词，created/registered 分别在 UTC 2025-10-18T16:00:00Z 至 10-19T15:59:59Z（目标 BJT 自然日的秒级表示），page[size]=100，均 total=0/count=0、无 next，止 P1。不是全类 Methods 队列；空集合相同只支持这些实际查询无增量，不支持零论文或所有旧潜力窗外。

**待 writer 小补件**：现有 `REPAIR_DC_CONTROL_2510.15333_20261029.json` 仅精确 DOI 服务正控，不能验证 title/client/created 或 registered 的组合查询语义。请用同形五主题中一个（MODEL 足够）在精确样本所属邻日做 created 和 registered 正控，保存原始 URL 与非空命中；不读邻日论文正文、不恢复邻日任务、不扩主题/全分类。正控若已在途直接复用，不重复请求。此为实际空查询可解释性，不增独立研究审批。

## R5 后到 W2/查询纠错：初轮十空无效，VALID 层有效

实际读 W2 和 DEBUG 五原件及 VALID 十原件。R4 对初轮空响应只作条件性描述，现撤销其发现解释权限；其中原 CONTROL 也因同一错误 client 字段为零，不能作为正控。writer 已实际定位 `client.client-id` 无效，`client.id` 才匹配：同一精确 GraphMoE DOI 在 EXACT/DATE/TITLE/CLIENTID 均 total1，CLIENT total0。不能因初轮十空或 HTTP200 授覆盖。

纠正后 VALID 十项实际 query 均为 `client.id:arxiv.content`，保原五有限 title 主题/同义词、目标 UTC 带和 size100；逐项解析 JSON meta/data/links 均 total0/data[]/无 next，止 P1。VALID positive created/registered 两原件在邻接 BJT Oct20 的同类 client/date/title/精确 GraphMoE 联合查询均 total1/data1，实际命中 DOI=10.48550/arxiv.2510.15333，client=arxiv.content，state=findable；这既验证查询的组成字段，也不读邻日正文/扩邻日任务。正控以 mixture-of-experts 子句和精确 DOI 限定，并非整五主题邻日召回；实际非空已足以校验错误字段修复，无需追加行政正控配额。

**发现层该有限差额通过**：只指 VALID 五主题的 created 与 registered 目标窗实际同为空集合、差额0，不等零论文/Submitted池全窗外/全源完整覆盖。初轮无效原件保留且不引用作正面依据。R4 正控小补件由此解除，不重复网络。个体日期联合界仍待 writer 首必要完成后独核，不抢其正在进行的读取。

## R6 W3/W4 个体日期支持与直接反侧实际独核

实际解析四批 DataCite 原 JSON 与请求 manifest：50+50+50+36=186，186 唯一精确 DOI，全部 findable/arxiv.content；无分页 next。实际读 `repair-bounds-20261029.py` 及186条复算表，独立用另一分支日程计算逐项比对 October v1 最早界、registered 最晚界、提交与登记顺序，差异/倒置0；不是仅运行 writer 脚本或信任统计。

实际分层为146 first-after-window-joint-bound、39 first-before-window-upper-bound、1跨窗。146个最早界全部 >= BJT Oct20 且 <= registered，因此只支持该 first 不落 Oct19；不是146个单日已知。39的 registered 已早于目标窗，足以给相应 first 窗前上界，不需借 IDmonth/早年日程。复算表中的单日标签只有在 earliest.date==latest.date 且顺序合法时成立；窗口之外不强求另定精确日，不移动归属或启动其它日报。

具名支持：GraphMoE 精确 DOI 对应题名，唯一 v1 2025-10-17T05:51:02Z，按 Friday 截止最早为 Sunday20EDT/BJT Oct20 08:00，registered=2025-10-20T01:39:48Z/BJT09:39:48，同日上下界成立。SCALAR v1 Oct18T12:41:18Z，最早 BJT Oct21 08:00、登记 Oct21 10:52:40，也不落目标日。L-MoE DataCite dates 另载 v2 Withdrawn/具体数学错误，保持旧撤回排除，不用 first 窗后消掉当前撤回禁界。

**直接反侧 15007：** 本日 supplement.xml 原 v1 published/updated 都为 Oct16T06:50:33Z，与 DOI dates 唯一 Submitted v1 一致。最早 BJT Oct17 08:00，registered=Oct20T01:32:08Z/BJT09:32:08，区间实跨 Oct19，不能切取目标日、用 created 代 registered 或以常规周末无公告关闭。原必要多标签安全反侧只按已成层复用，尚无当窗候选资格。W4 的定点当前 abs/直接公告补件仍在途，未把普通未读称外部终态；writer 完成该最小出口后直接交结果即可，不重复全文/全部169家族搜索。

本轮186只是日期层，原112/69AB等贡献分母不变。未知 current 修订仍需具体重要差额与事件日，不授整族 O/已有覆盖。MCP16558为原额外核心、待单独日证的实际缺层已识别；Google相册非 arXiv 不受此组合自动定日。R6 日期规则/146+39有限排除通过，不是全日 DAY；尚待15007/MCP最小出口、当前六节实稿与必要终态分责。

## R7 当前完整六节 DAY 实读与一处窄修

已实际从磁盘完整通读 W5 保存的 README 六节（SHA256 `a1d729253325be78d041ef887088acd98c05e40bf2825ef25bcebde24529683c`），另实际解析15007新abs submission-history与MCP精确DOI完整dates/client/state/身份字段，不冒只看文件存在。

15007新abs只有一个v1、原时刻与既有XML/DOI一致；没有新增修订/撤回说明或直接日公告。既有月列表仅身份与已执行两精确官方查询的范围/停止已在W4/W5记清，有限恢复后跨窗资格可隔离；不授正面Evidence/Books，也不据正常周末关闭。MCP对应精确DOI/client=findable的唯一v1 Oct18T16:09:05Z，最早Oct21 08:00 BJT、登记Oct21 10:54:39 BJT，同日窗后；v2 Apr27 2026不作目标日修订，当前新题名/摘要不倒投旧v1安全结论。必要安全反侧复用原精确v1，未采用未来正文。

六节实质判断符合：没有确定当窗新增候选/新评分/正面采用Evidence/Books写入；未以日证困难抹贡献，146+39只排first，15007、具体未知revision、Google相册及机构历史缺段分开。十四每日行完整、按需只实际触发，五有限发现无全分类Methods扩张；Hunyuan中文All的当前层与历史缺段准确。不需要假造Books PRE/POST或全章锁，没有新Books写入可验收。

**尚需一处实际窄修后授 DAY：** §5 第二条“其余186原字段及额外MCP”与前条已单列15007有计数歧义；186包含15007，改为“186逐项原字段及额外MCP已按本轮证据分责”或“其余185项及额外MCP”即可，不改研究结论/扩大恢复。这是普通文字差额，不是外部H；writer完成窄修后reader只核该差额，即可承接此次已完整实读层，不重六节研究。

本稿实际 V3通过，H2六、十处本地引用缺失0；与本轮BASELINE相比原小时窗相同、原候选表全部行相同、整个原§4为新§4连续原文子串，保护成立。限定README/两canonical的working diff-check通过；已读README diff，未碰既有staged原件/共享State或索引。以上机器检查不替语义。R7尚未签完成态actualFINAL，待窄修DAY后真实完成SAVE/自读QA。

## R8 实际 DAY 通过

已实际读回磁盘§5第二条：现为“上述186项中已排除的185项及额外MCP”，R7唯一计数歧义解除，未更改研究判断。另逐项解析 W6/W7 的 `REPAIR_DC_VALID_MS_FETCH_20261029.json` 与十个原 JSON：实际 URL 为 UTC Oct18T16:00:00.000Z 至 Oct19T15:59:59.999Z、正确client.id、原五title主题与size100；十项HTTP200、total0/data[]、links无next，实际止P1。最后999毫秒缺层已补，差额0；R5非空正控有效复用，不重复网络或全Methods。

**当前六节 DAY：通过。** 由R7实际完整六节实读，加本次实际窄修/末毫秒差额核验承接，不是marker批准。当前范围/来源停止、日期准入、原反侧、Books 0写入、外部精确隔离与重开条件均达到本日安全终态；不声明15007日期已证、机构历史覆盖通过或全网无遗漏。无其余普通研究/书写差额。

请 writer 据本次实际DAY，真实保存 README 完成态、通过结论及普通待办归零，全文自读QA后在W记录实际SAVE与检查结果；随后 reader 才读取磁盘完成态作 actualFINAL。不得在完成态先写尚未发生的actualFINAL通过。无Books提案故没有虚构PRE/POST环节，本日尚未actualFINAL、不提前计年度。

## R9 磁盘 actualFINAL：通过

已实际读 writer W9：R8 DAY 后真实完成态 SAVE、完整六节自读QA及后到V3修正均已发生。随后 reader 再次从磁盘完整通读最终 README 六节，核对实际 SHA256 为 `181e3ef8baeeb88fef5426d9a4d09c66cc4255d301f42717f249ee884f534244`，与 W9 保存稿一致；不是仅验hash、marker或writer声明。最终状态“完成”、§6“通过”、普通研究/书写0；actualFINAL权限由本条实际后到记录承载，作者未预签。

已实核最终结论仍为新增确定当窗候选0、新评分0、正面采用Evidence0、Books写入0；不等全部潜力已有覆盖、零论文或完整历史Coverage。146窗后/39窗前/15007跨窗及额外MCP分责一致，created/registered有效末毫秒发现差额0与错误过滤/正控边界保留，中文All11/11仅当前目录，15007/具体未知revision/Google相册/机构历史缺段终态隔离与精确重开条件未被完成态抹去。旧准入恢复、纠错/安全反侧及必要v1读取层均有效保留，不重Methods或新造Books修改。

最终实际V3通过；本地引用10出现/缺失0，H2六；对本轮BASELINE原小时窗、候选表全部行完全相同，完整旧§4连续原文仍在。README及两canonical的限定working/cached diff-check均实际通过。既有staged原始HTTP/HTML空白不清洗、不unstage，不宣称全目录/全仓clean。reader仅写此独核与三个必要独核原件，不写Report/Books/State/索引；无stage/unstage/commit/push，无模型/effort改动或fallback，无第三技术批准/全章锁。

**仅2025-10-20本轮安全终态完成。** 本日pair可收束，年度计数由root按此真实FINAL只计本日一次；本reader不写共享State、不启动下一Daily/Weekly/2026或八月。无需writer为补记已发生FINAL再改README，避免另造未核保存版本；有后到真实材料仅定点重开受影响项。
