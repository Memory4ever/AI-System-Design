# Daily Research — 2026-05-31

**规范：** V3

**窗口：** 2026-05-30T09:00:00+08:00 ～ 2026-05-31T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-10-21T15:58:44+08:00

**窗口说明：** 用户授权保留已有候选、日期、评分、原窗口及连续原§4，仅补遗漏；原0候选及旧非作者审阅保留其历史范围，不替代本轮补查验收。

**补充窗口：** 2026-05-30 ～ 2026-05-30

## 1. 结论

原小时窗0候选与有效原证保留；本次补May30完整自然日新增1个唯一家族，合计1。MiMo官方推理工程说明明确了Hybrid SWA独立回收后的prefix伪命中：逻辑树存在不等于所需窗口尾部KV仍有效，必须联合window-safe长度、双索引/双池容量及异步restore状态判断复用。必要原证已深入审阅，8分；唯一owner `INFER-SGLANG` 的具体缺口已写入[Ch51](../../../../books/part-05-inference-system/51-sglang.md#hybrid-swa-的命中还要通过窗口有效性检查)，root实际写后POST与本日R6六部分DAY通过。

14个每日来源的本轮约定主题检查已收口，常规arXiv公告不落May30；不把目录元数据条数当当天论文数，也不把周末公告日程推成机构零发布。OpenAI/Anthropic、Google Pubs、Meta、Moonshot及Hunyuan迁站前等历史索引边界、Transformer Circuits May-update日归属和MiMo未标日期卡片均在§5隔离，不支持无遗漏或生产收益保证。普通研究、Books与日级独核待办0；root本日R7完成态有限FINAL实际通过，不重开有效研究。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | root实际Research/Index首屏后恢复官方RSS：1303条dated metadata，2015～2026；仅筛May30BJT及邻界，May29四项→Jun1四项，目标0 | 已检查 | 当前feed不认证被删或未收录的历史事件；不把1303条展开全文 |
| SRC-ANTHROPIC | root实际Research六个非Science team首屏读到目标相邻日期，均无May30；Alignment Blog五月三卡具名日证复用；TC feed56entry仅定位邻界 | 已检查 | News历史日级分页未恢复；TC May-update只有月份/updated不唯一证明May30，见§5 |
| SRC-GOOGLE-AI | DeepMind Publications第1页可读日期切片跨Sep2026～Nov2025，May28→Jun4，无May30；Google Pubs首屏1～15/11628、2026年份与限定主题日查询 | 受阻 | DeepMind可读切片已检查；Google Pubs按年非按日，未取得必要历史日级切片，不以搜索0证明全集 |
| SRC-META-AI | Research空正文，Publications官方不可用提示；直接请求35s超时及窄日期主题查询后停止 | 受阻 | 官方历史分页不可重放；无具名May30事件不等于无遗漏 |
| SRC-QWEN | 本日官方retrieval API成功，40项未排序，逐查May邻近extra.date与正文published_time；Qwen-VLA两字段均May29，其余双字段均不落May30 | 已检查 | 当前列表非历史全集；不为Qwen3.7-Plus等窗外双日期差异选字段搬窗 |
| SRC-DEEPSEEK | 主页→News研究索引10个dated items，动态Apr24→Sep10、研究Feb25→Jun24边界；无May30 | 已检查 | 仅限当前可读官方目录，不追普通commit或保证删除历史 |
| SRC-MOONSHOT | Platform Blog与changelog实际到2025-11，组织README Research/Benchmarks/Infra作为主题backup，窄日期检索无具名线索 | 受阻 | 博客未维护到目标日，当前组织README不构成May30历史日级全集 |
| SRC-TENCENT-HUNYUAN | 首查Research动态目录；真实POST All/zh publicList，renderType0/page1/size1000，total11/list11，必要标题/displayPublishTime与正文日期无May30 | 已检查 | 不是默认en blog；迁站前历史全集未证，不授无遗漏 |
| SRC-ZAI | 首查Research全部15项到Dec2025，May20ZCube→Jun16GLM5.2边界，组织入口backup | 已检查 | 可读目录无May30；组织当前updated不当首公开日 |
| SRC-BYTEDANCE-SEED | 本日Research→实际API article_type1/2、x-tt-locale US；PUB按真实next_page_token 0→20→40→60→80至has_more=false，当前81可见唯一metadata；BLOG0共15可见至false；仅日期/title切片 | 已检查 | 无May30；total86/20不等于81/15可见量，不授不可见历史项保证；TaskMem旧May29不搬移 |
| SRC-BAIDU-ERNIE | 中文Blog第1页8项跨May9～Dec2025，最新May9；官方repo Recent updates到2025-11 | 已检查 | 当前可读目录无May30，不以月级repo更新制造当窗事件 |
| SRC-XIAOMI-MIMO | Paper/Blog入口→bundle当窗route及官方HTML，英语/中文均date May30，同一家族 | 已检查 | 新增1家族；其他未标日期卡片不提供历史完整性保证 |
| SRC-MINIMAX | EN/CN raw SSR恢复dated cards跨May27/25→Jun1，Agent Tech Blog四项Sep19～Oct20；停在May前日期边界 | 已检查 | 无May30；中英文窗外日期差异不扩版本史或全文队列 |
| SRC-ARXIV | root实际官方2026 availability日程、发号和假日段；目标BJT自然日对应EDT周五中午～周六中午 | 已检查 | 无常规公告点；不排除机构/作者独立正文，旧June宽raw不成为本窗队列 |

本轮实际请求、停止点、身份、准入与分层关闭见[唯一补查记录](../_sources/daily-20260531/SUP_SOURCES_20261021.md#daily14本次实际入口停止范围与分层关闭)，root两机构恢复见[本日独核R3](../_sources/daily-20260531/SUP_REVIEW_20261021.md#r3--委派给-root-的两机构窄来源恢复)。旧[`source-coverage-v3.json`](../_sources/daily-20260531/source-coverage-v3.json)与[`screening-outcomes-v3.json`](../_sources/daily-20260531/screening-outcomes-v3.json)只承载原范围，不覆盖本轮判断。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Full-Pipeline Inference Optimization for MiMo-V2.5 Series](https://mimo.xiaomi.com/blog/mimo-v2-5-inference) | 2026-05-30 | Hybrid SWA独立回收后，以window-safe长度/双索引验证真实prefix hit，并联合两池容量与restore完成；3+2+3=8 | 深入完成 | 整合：`INFER-SGLANG`，[Ch51窗口有效性](../../../../books/part-05-inference-system/51-sglang.md#hybrid-swa-的命中还要通过窗口有效性检查)，实际写后POST通过 |


原0候选不变；本轮新增1家族，中英文同一官方说明不重复计数。

## 4. 证据与知识整合

没有通过贡献筛选的唯一材料家族，因此没有合法的 Evidence Review、评分或 Books 改动。TaskMem 的官方时间为 `2026-05-29T00:00:00+08:00`，只归 05-29；arXiv 链接及其之后的提交/公告元数据不把同一家族移动到本日。

结构化 Evidence、Books 比较与共享写入队列分别见 [`evidence-review-v3.json`](../_sources/daily-20260531/evidence-review-v3.json)、[`books-comparison-v3.json`](../_sources/daily-20260531/books-comparison-v3.json) 和 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260531/root-books-writeback-queue-v3.json)。

以上连续原块只描述原小时窗的历史零候选，不覆盖以下补充窗口新增。

### [Full-Pipeline Inference Optimization for MiMo-V2.5 Series](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)

采用官方当前HTML，页面日期及构建route frontmatter均为May30；未见该页撤回/纠错信号，不补造精确时刻。作者完整读§1～7，必要采用域为§2.1和§2.2/2.3相关限制，独立reader实际重开必要域。核心不是把Full Attention写成“token相同无条件有效”，而是在身份兼容、物理KV存活的原合同上增加SWA独立回收：逻辑prefix node存活时tail窗口可能失效，应截断到window-safe长度并重算；Full/SWA两池、双indices、两容量准入及异步tier有效性共同维护这份合同。窗口外SWA可独立释放，但device存在不说明host/远端副本已经补齐。

原文MiMo-V2.5-Pro为70层/10Full/60SWA/window128，约1/7容量是其大N主导项，不是端到端速度。93%/95%生产命中率缺完整workload、hardware、precision、batch/concurrency、长度分布与SLO/受控对照（Not Disclosed），不用于普遍收益或因果保证；§6平均延迟78.39→80.28ms对应QPS15→30，不是同负载因果退化对照，也不支持零回退的字面泛化。未核SGLang代码或复现实验，不声称所有版本具备实现。

Books具体差额：Ch51已有typed-state原则，但缺SWA尾部有效匹配长度与两独立池的执行合同；已在该原则后、Exact Prefix前融入两段，保留额外metadata/异步一致性费用、旧完整缓存及miss重算fallback，不复制到Ch45/52。完整原证位置、逐字PRE及采用边界见[MiMo证据与PRE](../_sources/daily-20260531/SUP_SOURCES_20261021.md#mimo首批准入必要原证与唯一-owner-pre)；root本日R5实际写后独核通过，窄位已释放。

## 5. 缺口与下一步

普通待办：无。新增1家族的必要Source、唯一owner实际POST及六部分DAY均通过，无候选级必要正文缺失；以下仅为已隔离的本窗终态保留项。

终态保留项均不支持正面证据、Books或无遗漏：

- Meta Research/Publications不可用与Google Pubs无日级历史切片、Moonshot博客停在2025、OpenAI未入feed/删除历史、Anthropic News分页、Hunyuan迁站前全集、Qwen当前40项之外的历史档案、Seed total与可见条目的差额、MiMo其他未标日期卡片：已有实际入口和有界恢复仍不足认证历史全集。重开只需具名当窗官方事件或可重放官方当日索引/快照；定位§2对应来源及唯一SUP，禁止把当前列表、搜索0或普通updated冒作日级保证。
- [Transformer Circuits May-update / Downstream Connections](https://transformer-circuits.pub/2026/may-update/index.html)：官方月份与feed updated Jun1不唯一限定May30首次公开，不评分、不计确定当窗候选或进入Books。必要替代材料为该精确正文官方日级发布记录、当期快照或原作者可核公告；取得后只重开本项日归属与必要贡献审阅，不重扫机构。具体联合约束与复用范围见本日独核R3。

窗外线索不属于本窗：Qwen-VLA的May29双日证、Seed TaskMem既有May29归属及MiniMax May25/27→Jun1邻项只用于界定边界，未把它们写成已审当窗重复或另建本日全文待办。

## 6. 复核

复核者：`root`（未参与本日正式报告写作；承担指定两机构原件恢复与唯一独立reader）

结论：通过

本轮已实际核窗口常规arXiv边界、OpenAI/Anthropic窄来源恢复、MiMo准入8分、必要Source与具体owner逐字PRE，见[本日独核R1～R7](../_sources/daily-20260531/SUP_REVIEW_20261021.md)。其它明确排除及历史目录边界按来源、主题与理由分层抽检，不要求全量无差别重读。root本日R5已实际检查Ch51完整新增、两侧邻接及本人note，澄清SWA主语后完整第二段再读通过并释放窄位。R6实际读当前完整六部分、Seed真实cursor链、分层范围/日期/目录边界关闭、冻结与引用后DAY通过；修正了Seed visible-count误作page-capacity和DeepMind卡片数口径，未把抽检称全量语义证明。MiMo为唯一拟入选，必要Source/具体owner与实际POST全覆盖；范围明确科学应用、Qwen多日字段/窗外、Hunyuan日期、Seed分页和其余目录限制按来源/主题/理由分层核验，未无差别重读所有窗外全文。

原`fresh-nonauthor:may29-31-final-20260916`对原小时窗/零候选的有效审阅继续保留，见[旧原独核](../_sources/daily-20260531/FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916.md)，不替代本轮补充窗口及新增1项。

机器检查：当前V3通过；12个本地引用零missing；原窗口/0候选及连续原§4逐字保持（含标题639 UTF-8字节、去标题611字节）；README/SUP/Ch51限定working/cached diff-check通过。机器只证格式与这些可判定接口，不代替上述独立语义审阅；未stage、commit、push，既有及并发index保持。
