# Daily Research — 2026-05-24

**规范：** V3
**窗口：** 2026-05-23T09:00:00+08:00 ～ 2026-05-24T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-21T09:42:48+08:00
**补充窗口：** 2026-05-23 ～ 2026-05-23
**窗口说明：** 用户要求保留原小时窗与有效旧证据，只补前一北京时间完整自然日。旧0候选、原窗口及连续原§4保留；新增事件按补充窗口归属，不搬移窗外论文。当前六节已归并，独立R10 DAY通过；完成表示有限补查安全闭合，不授被隔离历史slice或全源无遗漏。

## 1. 结论

补查保留旧0候选，新增本窗待处理家族5个：4个新PR家族与原Glasswing家族的一个重要snapshot事件；跨Daily不新计Glasswing家族分数。五项必要证据均已完成安全/正确性受影响域深入审阅，Books为2处实际整合＋3项具体已有覆盖，两窄位均经独立reader一次真实POST生效释放。没有本项目实现运行、漏洞复现或生产能力验收。

最重要的差额是：封存报告digest与披露后preimage可以绑定原内容，却不能证明漏洞真值或历史公开时间；MoE热图必须绑定实际indices、distinct-token rank population和phase，不能从图存在推导全局负载正确。这两项分别进入Ch72和Ch67。FSDP offload状态、YOLO temp审批和项目MCP配置则由现有具体责任边界承载，不为版本接线另造长期recipe。

arXiv[官方日程](https://info.arxiv.org/help/availability.html)及[适用历史规则原文](../_sources/daily-20260524/SUP_ARXIV_RULE_20261021.md)确认Fri/Sat Eastern无常规公告，前批BJT05-22 08:00、后批05-25 08:00；无具体例外线索，不展开旧289 submitted/40 exact packet。它们仅保[原迁移路由](../_sources/daily-20260524/legacy-v21-migration-v3.json)，不继承候选、评分或证据。

两Anthropic文章官方公开日期05-22为窗外，旧精确时刻请求不再适用；本日snapshot日期由官方published/live archive声明与带PT时区artifact/payload联合限定，不单靠URL或generated字段。Meta、Google Pubs日级元数据、MiMo无日期cards与Moonshot Blog历史缺段仍隔离；完成本次补查不表示全互联网或所有历史入口无遗漏。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 本日有效RSS相邻05-22 00Z→05-25，覆盖自然日两侧；复用身份/日期层。 | 已检查 | 无新增具名线索；非全站保证 |
| `SRC-ANTHROPIC` | Research及FRT/Engineering/Alignment/Interpretability/Economics/Societal六主题日期列表均读至May23前更早项；snapshot About/Overview/Archive原件及联合日期深入。 | 已检查 | 不用sitemap lastmod/首页未命中证明全站无遗漏；May22文章不请求时分秒 |
| `SRC-GOOGLE-AI` | 本日DeepMind dated边界05-19→28复用；新Google May月archive4条05-01/19/27/28；Pubs仍year/venue。 | 受阻 | Pubs无日级日期slice隔离，不授全库无事件 |
| `SRC-META-AI` | 实际Research timeout、Publications“content unavailable”，有限两官方入口后停。 | 受阻 | 缺可读历史dated目录，不当零命中 |
| `SRC-QWEN` | 本日官方article index有效相邻05-20 10:00→05-29 17:00，完整自然日两侧。 | 已检查 | 无新增具名线索 |
| `SRC-DEEPSEEK` | 本日官方News/Research有效相邻04-24→06-24，完整自然日两侧。 | 已检查 | 无新增具名线索 |
| `SRC-MOONSHOT` | 新Blog26 dated卡最新2025-11，2026历史段不可得；org全天PR q3条全部core，8/2349入选、2350原版关闭。 | 受阻 | Blog历史缺段隔离；代码查询确定结果不受影响 |
| `SRC-TENCENT-HUNYUAN` | 新POST publicList page1/pageSize10：total9/list9，各publicAt/publishedAt/displayDate读完无May23；org全天PR0/false。 | 已检查 | 字段分责，不把display回填作first-public；不沿窗外全文 |
| `SRC-ZAI` | 本日Research05-20→06-16复用；新release notes04-07→06-16；org全天PR首次限流后相同q重试0/false。 | 已检查 | 首次错误不计零；仅成功有限入口 |
| `SRC-BYTEDANCE-SEED` | 本日Research/Public Papers05-16→29复用；org全天PR2条、必要exact实现，786/787入选。 | 已检查 | merge May24/26不倒作本日已ship |
| `SRC-BAIDU-ERNIE` | 本日技术Blog最近05-09复用；repo全天PR0/false。 | 已检查 | 无新增具名线索 |
| `SRC-XIAOMI-MIMO` | 新Paper8项03-13→06-29；Blog15无日卡；org全天PR0/false。 | 受阻 | undated Blog slice隔离，不作无遗漏证据 |
| `SRC-MINIMAX` | 本日双语言/Agent Blog03-18→05-26/27复用；org全天PR1条#161全文core，普通fixture更换关闭。 | 已检查 | 不把测试标签当排除依据 |
| `SRC-ARXIV` | 当前和历史适用官方日程；本自然日无常规公告，无具名例外线索。 | 已检查 | 旧提交库存不作本轮队列；不宣称全球无其它渠道 |

本轮查询/原件/分页/停止点及复用边界见[唯一作者A1–A7](../_sources/daily-20260524/SUP_SOURCES_20261021.md)。7scope GitHub精确UTC全天范围为05-22T16:00:00Z～05-23T15:59:59Z，`is:pr <org/repo> created:<range>`、per_page100/page1，均不足100且incomplete=false即停；只6个命中读core，没有机构全commit队列。旧[source-coverage](../_sources/daily-20260524/source-coverage-v3.json)/[window evidence](../_sources/daily-20260524/official-owner-window-evidence-v3.json)保持旧小时窗历史语义，新结论以上述补充为准。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Anthropic CVD snapshot 2026-05-22-1027](https://red.anthropic.com/2026/cvd/snapshots/2026-05-22-1027/about/) | 2026-05-23 | Glasswing家族重要修订事件：新artifact补充封存→揭示接口，非文章改版或新家族首发；不重复评分 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [VeOmni#787: rework MoE load-balance monitor](https://github.com/ByteDance-Seed/VeOmni/pull/787) | 2026-05-23 | actual indices/DP+SP distinct人口与phase分责，修正“热图存在即全局负载”；2+2+2=6 | 深入完成 | 整合：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [VeOmni#786: Qwen-Image & FSDP state API](https://github.com/ByteDance-Seed/VeOmni/pull/786) | 2026-05-23 | 强置私有state再reshard/offload不证明真正完成；2+2+2=6 | 深入完成 | 已有覆盖：TRAIN-ZERO，[Ch39](../../../../books/part-04-training-system/39-zero.md) |
| [Kimi-Code#8: temp access without approval](https://github.com/MoonshotAI/kimi-code/pull/8) | 2026-05-23 | YOLO temp-root例外改变审批面，不等完整capability；2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Kimi-CLI#2349: project-level MCP config](https://github.com/MoonshotAI/kimi-cli/pull/2349) | 2026-05-23 | 自动project层/同名覆盖改变catalog来源与trust分责；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md) |

没有把提交库存、未核资格或后来head倒作本日候选。下节开头连续634字符/892字节为旧小时窗空候选证据原块，保持但不支撑本轮0候选/精确时刻请求；后续补充是当前判断。

## 4. 证据与知识整合

确认候选分母为 0，因此没有可执行的 exact-version Evidence Review、评分或 Books comparison。空 Evidence 集合见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260524/exact-v1-evidence-v3.json)，空 Books 对读与队列分别见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260524/books-current-content-comparison-v3.json)和 [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260524/BOOKS_WRITEBACK_QUEUE_V3.json)。

Anthropic 边界 family 若取得在窗时刻，不得直接套用空集合：应重开 title + full abstract 贡献准入；若 retained，再读 exact-version 正文，审查 ExploitBench 任务分层、程序化验证、随机化布局、相同 harness、试验重复与 disclosure/fallback 边界，随后重新评分和对读唯一 Stable Knowledge Node。当前不预判 Books 结果。

### [Anthropic CVD snapshot 2026-05-22-1027](https://red.anthropic.com/2026/cvd/snapshots/2026-05-22-1027/about/)

采用Revision1 dated About/Overview/Archive与payload元数据。官方archive的published/live-on-date说明，联合原PT日期和payload17:27Z限定本artifact为BJT05-23；不把生成字段单独叫公开时刻。仍归SF-2026-ANTHROPIC-MYTHOS-GLASSWING-UPDATE，不证明protocol此前从未公开，不重复旧评分。旧文章只有dashboard/阶段统计，没有canonical preimage接口。

必要原文支持先hash、通知后显示状态、窗口后可揭示preimage；批准时未知null必须按原序列化保留。PoC hash不证明复现，发布方append-only自述不独立证明时间或排除不同ledger，所有披露项也不都外部确认。未复算manifest整包hash、不读1611漏洞队列、不运行PoC。Ch72旧CVD两段缺封存/揭示接口，已在其后/BYOK前写一段及本人注；reader R3实际POST通过。Ch69 hash/promotion一般边界只作定点去重，不另写。

### [VeOmni#787: rework MoE load-balance monitor](https://github.com/ByteDance-Seed/VeOmni/pull/787)

采用本窗head `3e7d35a37fa9f51b1022840aba3c0d6e4feefeb5`（May23 15:32:50Z）；PR创建14:51Z，merge May24是后续。实读monitor/callback/DeepSeek实际topk插点与必要tests：旧hook未接、rank-local图不能代表全局；所测mesh内distinct DP+SP求和而排除复制EP，模型家族下游真实indices不得另算。pause接口不等verl engine已接，后者原文仍future work。

重复attach的层表去重不证明hook计数不重复；空rank在allreduce前return、回调全rankformat也不授全部distributed correctness/低开销。作者Qwen3-30B-A3B/8×H100/EP8/6steps只是smoke，不是项目复现或收敛保证。Ch67 counter两段后/四层table前新增population/phase/费用与回退一段，reader R6实际POST通过。

### [VeOmni#786: Qwen-Image & FSDP state API](https://github.com/ByteDance-Seed/VeOmni/pull/786)

采用本窗head `3f1881b0ee41a6d0f6a7fa7758cdac7e127461e1`（May23 12:45:59Z），三files必要diff；原创建12:09Z，May26merge不倒作本日ship。FSDP私有state强置IDLE后reshard/cpu、optimizer只搬top-level Tensor且nonblocking无显式同步，未给异常恢复/输出等价或性能验证；Qwen-Image注称fresh sample但仍mode()，统一predict_noise/grid属版本接线，不宣称额外质量收益。

长期只采用搬运位置≠状态owner/完成边界：Ch39 Offload/CPU-authoritative stream已有Backward-Done、Buffer-Free、等offload/CPU消费排空与模型版本边界；Ch35 phase段交叉确认等待/恢复分责。现文不含API，但不需把防御helper写成新通用恢复recipe，具体已有覆盖，reader R8通过。

### [Kimi-Code#8: temp access without approval](https://github.com/MoonshotAI/kimi-code/pull/8)

当前head是May25 merge-main，故定点恢复本窗原commit `56f25f083f446bbb8a54ce2604b5de35323d71fd`（May23 05:14Z）完整policy/gettmpdir与tests，original path-access全文与现行相同。YOLO指定五file tools、outsideWorkspace且词法temp-root内返回undefined，只表示此policy不ask；SSH realpath的是root非每个target，symlink/TOCTOU、shared temp及其它policy未被证明安全。closed/unmerged、comments空，不称ship，也无官方撤回依据。

采用审批/实际capability分责，Ch72 commandguard/workspace完整段已逐项要求启动模式、覆盖配置、审批缺席和文件/网络/进程隔离，后path段又要求实际consumer检查；不假称已含temp名单。本提案是该边界的版本例子，具体已有覆盖，reader R8通过。

### [Kimi-CLI#2349: project-level MCP config](https://github.com/MoonshotAI/kimi-cli/pull/2349)

采用本窗head `fe2ba8e679ca11d90f44b0fe626fd538f980ec08`（May23 07:13Z）helper/config/CLI/ACP/Web/tests必要域。override的explicit files/raw是同一层集合、merge同名覆盖；ACP client有server时与CLI fallback不同，Web错误后可空MCP继续。PR仍open，既不授全部UI完全一致，也不推任意代码执行或已部署。

采用config来源/连接/动作执行与真实server admission分责，Ch83 Kimi0.68完整论证及Server Admission四段已绑定identity/tool allowlist/版本和effect-time授权；priority recipe是本提案策略而非协议标准。现文不含merge算法，本次也不采为普遍recipe；具体已有覆盖，reader R8通过。所有精确原件、反侧与对读位置见作者A3/A5。

## 5. 缺口与下一步

普通可执行工作0；独立R10 DAY已通过，扫描、Source与Books普通工作均闭合。以下真实外部缺段为已隔离的终态保留项：不支持正面证据、候选、Books或无遗漏断言，取得官方材料后只定点重开相应identity：Meta可读该日archive；Google Publications日级公开日期；MiMo undated Blog日级原页；Moonshot Blog在2025-11之后的2026历史目录。具体失败/停止见作者A7。

旧[材料请求](../_sources/daily-20260524/materials-request-v3.json)保留历史，Anthropic两May22文章的精确时刻请求已撤销，不再阻本日；snapshot资格独立按联合证据成立。旧289/40只路由，不是普通待办。

窗外线索：Kimi-CLI#2350 May27 `48d2b296…`把decoded stdout用于json.loads，具体改变acceptance/data identity，应仅在真实归属日恢复；May23 `e5ff5957…`仅locale诊断/广播容错而raw parser未改，原事件具体关闭不评分，A6拟稿已取消。两版代码与反证保留，不能拿新版倒灌本日，也不是因缺受控实验、工作量或分数关闭。MiniMax#161普通test fixture在原始筛选记录关闭。它们不在本日候选分母。

## 6. 复核

复核者：supp_may23_reader（本日独立reader，非报告/Books作者）

结论：通过

独核已实际完成五候选必要Source与具体Books判断；R3/R6两次真实写后完整新增/完整两侧/本人注POST生效，R8三具体NC通过。代表排除MiniMax161完整core、2350本日/May27具名原commit与反侧均实际核；本轮仅这6个代码命中与一个snapshot，不把宽库存/1611漏洞数当逐项队列。R9来源边界与四历史/metadata缺段独核通过；R10实际完整六节DAY通过，独跑V3、原窗/连续旧§4 634字符892bytes恰一次、六节/16本地refs与限定cached/unstaged检查均通过；机器结果不代语义。记录及保存态有限FINAL见[本日SUP_REVIEW](../_sources/daily-20260524/SUP_REVIEW_20261021.md)；[旧fresh final](../_sources/daily-20260524/V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260915.md)仅支撑原小时窗旧层，不代本次验收。
