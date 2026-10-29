# 2026-05-31：遗漏来源增量补查

## 启动与真实 baseline

作者 `supp_may31_author` 于2026-10-21独立实际重读AGENTS、Research合同、Report V3、Sources用法/每日14源/arXiv主题及恢复、Prompt、完整ROADMAP和LS本日路由。root为非作者reader。仅补2026-05-30北京时间完整自然日；原0候选，原窗 `2026-05-30T09:00:00+08:00 ～ 2026-05-31T09:00:00+08:00`。原空表不冻结新增准入；旧完成标签只描述旧范围。未修改Books、合同、索引、LS或index。

以下为运行前README真实逐字baseline；保存后才开始修改报告。冻结对象是原窗口和连续原§4，既有候选为空。原零事件/覆盖结论不自动继承到补充窗口。

```markdown
# Daily Research — 2026-05-31

**规范：** V3

**窗口：** 2026-05-30T09:00:00+08:00 ～ 2026-05-31T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-09-16T17:30:00+08:00

> 本页按当前合同重建，并已由未参与作者修复的 fresh non-author reviewer 完成独立终审。

## 1. 结论

本窗确认 0 个 raw identity：0 = 0 retained + 0 pre-denominator closure + 0 withdrawn。官方 arXiv schedule 表明周末没有公告批次；13 个机构来源的窗口切片没有保留材料。Evidence、评分、Books comparison 与 root queue 均为空，作者未修改共享 Books。Meta 历史分页与 MiMo 部分未标日期卡片的限制保持显式，但当前可用原始入口已经穷尽，不把不可恢复的历史列表当作候选或无遗漏证明。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research 索引/RSS 的窗口内 dated entries | 已检查 | 无窗口内可确认事件 |
| SRC-ANTHROPIC | 官方 Research 索引的窗口内 dated entries | 已检查 | 无窗口内可确认事件 |
| SRC-GOOGLE-AI | DeepMind/Google Research 官方 publication 索引 | 已检查 | 无窗口内可确认事件 |
| SRC-META-AI | 官方 Research/Publications 入口的窗口切片 | 受阻 | 稳定的历史日级分页不可重放，不支持全量无遗漏断言 |
| SRC-QWEN | 官方文章索引与正文语义切片 | 已检查 | 窗口附近产品/使用指南不满足长期机制贡献门槛 |
| SRC-DEEPSEEK | 官方 Research/News 窗口切片 | 已检查 | 无窗口内可确认事件 |
| SRC-MOONSHOT | 官方 Kimi Platform Blog 与组织发布切片 | 已检查 | 无窗口内可确认事件 |
| SRC-TENCENT-HUNYUAN | 官方 Research“全部”列表及原始链接 | 已检查 | 无窗口内可确认事件 |
| SRC-ZAI | 官方 Research、release 与仓库发布切片 | 已检查 | 无窗口内可确认事件 |
| SRC-BYTEDANCE-SEED | 官方 Research 页嵌入 ArticleMeta 与完整摘要 | 已检查 | TaskMem 官方时间已归 05-29；本窗未发现其他可确认事件 |
| SRC-BAIDU-ERNIE | 官方技术博客与仓库发布切片 | 已检查 | 无窗口内可确认事件 |
| SRC-XIAOMI-MIMO | 官方论文/博客卡片与仓库发布切片 | 受阻 | 部分卡片缺少日级时间，不支持全量无遗漏断言 |
| SRC-MINIMAX | 官方中英文 Blog、Research 与 Agent Tech Blog | 已检查 | 无窗口内可确认事件 |
| SRC-ARXIV | 官方 announcement cadence 与可重放 membership | 已检查 | 官方 schedule 证明该周末窗口没有公告批次 |

结构化依据见 [`source-coverage-v3.json`](../_sources/daily-20260531/source-coverage-v3.json) 与 [`screening-outcomes-v3.json`](../_sources/daily-20260531/screening-outcomes-v3.json)。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |


无候选。

## 4. 证据与知识整合

没有通过贡献筛选的唯一材料家族，因此没有合法的 Evidence Review、评分或 Books 改动。TaskMem 的官方时间为 `2026-05-29T00:00:00+08:00`，只归 05-29；arXiv 链接及其之后的提交/公告元数据不把同一家族移动到本日。

结构化 Evidence、Books 比较与共享写入队列分别见 [`evidence-review-v3.json`](../_sources/daily-20260531/evidence-review-v3.json)、[`books-comparison-v3.json`](../_sources/daily-20260531/books-comparison-v3.json) 和 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260531/root-books-writeback-queue-v3.json)。

## 5. 缺口与下一步

- 没有候选级材料请求。Meta/MiMo 的历史入口局限已写入来源覆盖；除非出现具体窗口事件或官方历史索引，否则不重扫。
终态保留项：Meta/MiMo 的历史入口局限不用于正面证据、Books 或无遗漏断言。定点重开条件：出现能够唯一归入本窗的具体官方事件，或取得可重放的官方历史索引；触发后只重开对应来源切片。

## 6. 复核

复核者：`fresh-nonauthor:may29-31-final-20260916`（未参与 05-31 author rebuild）

结论：通过

窗口、周末 arXiv cadence、零分母守恒、机构来源边界、TaskMem 跨日去重、空 Evidence/Books/queue 与终态保留项均独立核对；详见 [`FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916.md`](../_sources/daily-20260531/FRESH_NONAUTHOR_V3_FINAL_REVIEW_20260916.md)。
- **作者检查：** 窗口、14 个每日来源、题摘准入、withdrawn 边界、Source Family 去重、V2 三维评分、Evidence、Books comparison 与 root queue 均已核对；共享 Books 未修改。
- **机器检查：** JSON、集合算术、identity uniqueness、marker、validator 与 scoped diff-check 由本轮作者执行；机器通过不替代独立语义复核。
```

## 本轮执行位置

尚未完成补查。常规arXiv公告日程由root本日R2实际核验；美国东部周五/周六无常规公告，不能据此排除机构/作者May30独立正文。只按ROADMAP模型、训练/推理/平台/Agent、多模态与VLA主题检查Daily14；宽raw只作查漏线索，不展开原目录中无本窗资格的June论文。

## MiMo：首批准入、必要原证与唯一 owner PRE

- 身份：[Full-Pipeline Inference Optimization for MiMo-V2.5 Series](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)，官方HTML当前版本，页面与构建bundle frontmatter均明确`2026-05-30`；本日原件`SUP_MIMO_INFERENCE_20261021.html`、`SUP_MIMO_MAIN_20261021.js`，英文/中文同一家族，不重复计数。未见该事件页撤回/勘误信号，不遍历版本史。
- 作者实际读完整导论及§1～7；拟采用证据域是§2.1双池、window-safe长度、双索引、跨层异步有效性，§2.2失败后miss/recompute与§2.3生产命中率适用边界。首批准入与必要Source已由root本日实际原证通过：传统身份兼容且物理存活的prefix可复用→SWA独立驱逐使logical tree存在但window tail已失效→命中必须额外验证对应窗口、双池容量和restore完成，而非只做token比较。3+2+3=8，深入完成。
- 不采用：7倍/93%/95%通用收益、生产SLO、任意SGLang代码正确性、产品已经复现。原文说明MiMo-V2.5-Pro为70层/10Full/60SWA/window128；1/7是该架构大N容量主导项，不是所有phase、序列、batch的端到端速度。生产百分比缺完整流量/硬件/precision/并发/SLO及受控对照，均Not Disclosed；本次不以其认证因果收益。§6表格QPS15→30时平均latency78.39→80.28ms，因负载不同不能作因果退化对照，也不支持字面零回退的普遍声明。
- Books上下文实际读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、ROADMAP，Ch51全文，Ch45生命周期与cache主线、Ch50/52相邻交接。Ch45拥有物理KV生命周期、Ch52拥有远端metadata与transfer ready；Ch51现有`Cache Tree 统一的是 Identity，不是所有状态的物理语义`已承载通用typed-state，但没有SWA窗口尾部有效长度及两独立池的可执行命中边界。唯一owner定为`INFER-SGLANG`，不复制到45/52。

### 逐字 PRE（待root窄写位）

插入在Ch51该小节现有末段后、`## 从 Exact Prefix 到 Dependency-Aware Reusable Blocks`前；原段不改：

```markdown
### Hybrid SWA 的命中还要通过窗口有效性检查

完整 Attention 的 exact-prefix reuse 原本就要求模型、位置、mask 与前缀身份兼容，且对应物理 KV 仍然存活；token 相同从来不能单独保证状态可读。Hybrid SWA 在这一合同上再增加一条独立生命周期：Full Attention 层保留完整历史，SWA 层却可按窗口回收。即使 radix node 仍表示一整段 token，所需尾部窗口的槽位也可能已经释放或覆盖。因此匹配结果应是“仍有有效 SWA 尾部的可复用长度”，不是逻辑最长公共前缀；不满足窗口安全长度时截断命中并重算，不能让 scheduler 消费一个伪命中。

一种实现分工让 Full KV 与 SWA KV 使用独立物理池，树节点保存 Full 段索引及 SWA 映射，上层仍看到同一 sequence identity。Admission 同时检查两池容量；长 Prefill chunk、Decode 与请求结束按各自边界回收窗口外 SWA，跨层搬运也只恢复有效窗口。它把局部窗口的容量优势交给真实 cache manager，却增加双索引、独立驱逐与异步一致性成本：device 的有效窗口不证明 host/远端层已经补齐，完成事件和当前映射都要在复用前验证。[MiMo 的官方工程说明 §2.1](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)支持这份实现取舍，不证明所有 SGLang 版本已具备它，也不把架构容量比例或线上命中率变成通用吞吐保证。低复用、短请求或新状态路径尚未验收时，保留成熟完整缓存与重算路径；窗口安全检查失败则按 miss 处理。<!-- source-family:SF-2026-MIMO-V25-INFERENCE -->
```

本人Review note拟增于既有`## Review notes`后：

```markdown
- `SF-2026-MIMO-V25-INFERENCE` — Daily2026-05-31补May30；[官方工程说明](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)页面及bundle均标2026-05-30，当前HTML§2.1/2.2/2.3。3+2+3=8，采用window-safe长度、双索引/双池与异步restore分责；Full Attention仍需完整identity/物理存活，不授通用7倍、93%命中率或生产SLO。未核代码/实验复现；root非作者必要Source与本逐字PRE已核后再窄写，实际POST另验。
```

## Daily14：本次实际入口、停止范围与分层关闭

执行日2026-10-21；检查窗口只取May30BJT，topic slice为ROADMAP模型能力机制、训练/推理/平台/Agent、多模态与world/VLA。没有按分类/机构全库建全文队列；正文潜力只有MiMo具名事件。原件均在本目录`SUP_*_20261021`。

| 来源 | 实际恢复与停止点 | 筛选与限制 |
| --- | --- | --- |
| SRC-OPENAI / SRC-ANTHROPIC | root承接本日真实来源恢复，待消费其本日R3及原件 | 不以旧零事件继承覆盖；未先记本轮通过 |
| SRC-GOOGLE-AI | `SUP_WEB_B1/B3`：Research→DeepMind Publications第1页可读日期切片跨Sep2026～Nov2025，May28→Jun4边界；Research Blog可见当前目录。Google Pubs默认1～15/11628，2026年份423、按年而非日，窄站域May30检索未给相关事件 | DeepMind该可读有序目录无May30项；Google Pubs没有可复查的May30完整日级切片，保留历史索引能力边界，不以搜索0证明无遗漏，不将其余年度/领域条目送全文队列 |
| SRC-META-AI | `SUP_WEB_B1/B4`：Research正文0行；Publications返回`Sorry, this content isn't available right now`，curl必要原入口35s超时；窄站域日期主题检索无具名线索后停止 | 必要历史日级分页不可得，受阻隔离；不授Coverage/零事件保证 |
| SRC-QWEN | `SUP_QWEN_ARTICLES_20261021.json`：GET官方`/api/v2/article/retrieval?type=qwen_ai&language=en-US`，success=true，40条未排序元数据；按`extra.date`与content内published_time定点检查May邻近 | 无May30日期。Qwen-VLA为May29；Qwen3.7-Plus extra.date Jun1/正文May21，LiveTranslate May19/May11、Qwen3.7 May20/May16均双字段不落窗，不选一字段搬成May30。40条当前列表非历史全集；旧入口redirect/JS home及一次hidden浏览器64s超时后以已知真实API恢复，未逆向整站 |
| SRC-DEEPSEEK | `SUP_WEB_B2/B3`：主页→News Research索引，10个研究日期到2025，动态May附近以Apr24→Sep10及研究Feb25→Jun24界定 | 可读目录无May30；当前目录不认证删除事件，未扩普通代码commit/产品使用指南 |
| SRC-MOONSHOT | `SUP_WEB_B2/B3/B4`：Platform Blog可读2025条目，changelog到2025-11；MoonshotAI组织README Research/Benchmarks/Infra首屏，窄平台May30查询无具名线索 | 官方博客未维护到目标日、组织README是当前主题指针，不证明May30历史全集；该历史目录能力局限保留，不把未定日期项目预评分 |
| SRC-TENCENT-HUNYUAN | `SUP_HUNYUAN_ZH_20261021.json`：首开Research动态空壳，按真实All/zh route POST`api/blog/publicList` body`{pageNum:1,pageSize:1000,renderType:0}`，header`accept-language:zh`，code0/totalNum11/list11；读取必要title/displayPublishTime/content日期，当前列表到Feb2026 | 无May30项；这是Research对应列表，不用默认en博客代替。Hy-MT2 displayMay21，nextHy3Jul6；Hyra science为暂缓领域标题明确关闭，不读整稿。迁站前历史全集仍未获证明，不外推无遗漏 |
| SRC-ZAI | `SUP_WEB_B2/B4`：首查Research全部15项有序跨Aug2026～Dec2025，May20ZCube→Jun16GLM5.2边界；组织主页作为backup | 可读Research无May30，当前组织更新不是新公开日，不建无日证预候选 |
| SRC-BYTEDANCE-SEED | `SUP_SEED_PUB/BLOG...json`：本日Research HTML定位get_article_list_v2，article_type1/2、x-tt-locale US、publish_year2026；正式恢复按服务端next_page_token 0→20→40→60→80，末false，实际可见18/20/18/19/6＝81唯一metadata；BLOG0共15可见、末false | 官方total86/20与可见量81/15不同，当前不可见项不授历史完整性保证。先前按18可见误作分页上限、请求P18/36/54/72的手动恢复不作为最终连续覆盖依据；真实cursor原件另存CURSOR20/40/60/80。两类型可见date均无May30，只读日期/title，不作全量全文队列。TaskMem旧May29不移动 |
| SRC-BAIDU-ERNIE | `SUP_WEB_B2/B4`：官方中文Blog第1页8项跨May9～Dec2025，最新May9；官方ERNIE repo Recent updates到2025-11 | 可读日级目录无May30，不把仓库当前版本或月度更新当窗口事件 |
| SRC-XIAOMI-MIMO | `SUP_MIMO_...html/MAIN...js`：Paper/Blog目录及构建路由，date2026-05-30的中英文同一路由；官方目标HTML正文date同证。只读具名当窗core | 1家族准入8分，必要Source通过待owner窄写；未标日期其他卡片不能证明窗内外，隔离历史目录边界，不将整个JS文档库展开 |
| SRC-MINIMAX | `SUP_MINIMAX/CN_...html`可恢复SSR dated卡片（网页文本render虽空，raw含真实列表），中英文目录May27/May25→Jun1，Agent TechBlog四项Sep19～Oct20；停在目录到May前边界 | 没有May30；EN/CN发布日期不一致项都在窗外，无需为了本窗追版本史；普通上市/订阅或使用指南不因相关模型名进候选 |
| SRC-ARXIV | root本日R2实际官方availability日程/发号/假日段，按BJT自然日核常规公告 | May30无常规公告点，不以周末证明其他机构无稿，不展开本目录旧June宽raw |

### 首批排除/边界校准供独立分层抽查

1. 范围明确：Hunyuan `Hyra: 简单有效的科学发现智能体`，Research All/zh真实题名/内容入口，AI for Science暂缓，不因Agent词汇转挂Ch79；日期本就Jul21，不需全文证明May30贡献不存在。
2. 日期窗外：Qwen-VLA当前官方API `extra.date=2026-05-29T17:00:00+08:00`且正文published_time同日；有潜力也不并入May30，不当已审重复计数。Qwen3.7-Plus双原字段Jun1/May21均排窗；只指出字段差异，不为本窗假造其真实归属。
3. 非贡献排除而是目录边界：Meta官方不可用、Google Pubs无日级切片、Moonshot博客停在2025、Hunyuan迁站前全集未证；均隔离来源保证而非0篇通过。未出现具体必要当窗正文时不预候选、不评分。
4. 不是未来版本反推：MiniMax目录May25/27与Jun1日期断点、ERNIE May9最新、DeepMind May28/Jun4界定，只说明当前可读目录无当窗项；不用窗外新版的headline或后续修订改变本窗判断。

当前拟入选集合仅MiMo1家族，全部其余条目仅标题/日期定位或明确范围外，无额外普通全文队列；必要原件/owner待办继续，不以访问故障删候选。

## 作者收口与检查（DAY前）

已实际消费root本日R3两机构恢复原记录与R4必要Source/owner/PRE，OpenAI RSS当前1303日期元数据目标0、Anthropic六team跨界无May30与TC五月日归属隔离均融入README，未重复请求两源。DeepMind Publications第1页以实际可读日期切片跨目标邻界表述，不报无关目录卡片数量；只读目标附近日期/title，不把原目录条数当本窗新论文数。

root明确窄位后实际apply_patch写Ch51两段及本人note，作者顺读新增与完整typed-state→Exact Prefix邻接。root首次实际POST指出`跨层搬运也只恢复有效窗口`主语含糊，按其请求仅改一句为`SWA 部分的跨层搬运只恢复有效窗口，Full 层仍需完整且兼容的前缀状态`，没有重开已通过Source/owner或改分。本文PRE保留原提案历史，最终采用该澄清版本，待root限定读回正式POST。

当前V3格式校验通过；README/SUP/Ch51限定unstaged及cached diff-check均无输出（不称全仓clean）。运行前原窗逐字保持、原0候选没有搬移，连续原§4 611 UTF-8字节保存；仅其后新增本轮证据。README本地引用实查零missing。未stage、commit、push，未改合同/脚本/索引/LS，未顺带其他日期。尚待root实际POST、分层排除抽检与完整六部分DAY；完成态另行保存，不以机器通过代替独核。

后续实际差额：root本日R5已完成MiMo唯一owner真实POST、完整两侧及本人note读回，主语澄清完整复读通过，窄位释放；本人note仅行政同步该既成结果。root来源抽核发现Seed游标口径，已按真实`next_page_token`0→20→40→60→80逐次恢复至false，raw可见18/20/18/19/6共81唯一metadata，total86不冒可见全集；BLOG可见15/total20/false同理。没有May30可见项、没有新增正文队列；最终README与本表改用真实cursor链并保不可见档案限制。已发DAY READY，普通待办只剩日级独核与保存态FINAL。

## 完成态保存（2026-10-21T15:58:44+08:00）

root本日R6完整六部分DAY实际通过：唯一MiMo准入/必要Source/R5真实POST、真实Seed cursor链、分层排除及历史源边界、12本地引用与格式/限定两层检查均已核；未把抽样当全量、原META/日归属缺口不授Coverage。已按R6只行政保存README完成态及既成复核结果，原0候选/原窗口/连续原§4仍保留；原§4含标题639 UTF-8字节、去标题611是不同计数口径，不是丢失。最终新增1家族＝1深入完成＝1真实Books整合，唯一INFER-SGLANG，普通研究与Books/独核工作0，ownership已释放。只待root一次有限保存态FINAL，不接其他日期、不扩恢复、不stage/commit/push。

root本日R7已实际完成一次有限保存态FINAL：完成header、结论、§5/§6、V3、12引用、639字节原块唯一/旧窗口及两层限定检查均通过。作者仅行政同步该既成事实到README，不新增研究或行政审计轮；本日ownership结束，未接其他日期。
