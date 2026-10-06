# 2025-05-01 增量补查：最终日级精确停点复核

**复核者：** Gibbs，独立复核 agent，非 root 报告作者、非人类 reviewer
**id：** `01a11536-2adf-70d3-865a-b49aaff4fc37`
**检查时间：** 2026-10-07 15:52～15:56（Asia/Shanghai）
**授权范围：** 冻结旧 22 身份/日期/评分/处置，只补 Apr30 自然日；只写本文件，不改 Report、Books、State、合同或 Git。
**结论：** 局部证据、旧记录机械保留与受阻隔离通过；**当前日级完成验收未通过**，仍有第 6 节的具体普通修正/入口核验。不能把本文件称为全源 Coverage、全部旧 22 重新审阅、年度补查或 162 日完成。

## 1. 实际检查范围

按 May01 独立重读 `AGENTS.md`、当前研究/来源/Report 三合同、Prompt、ROADMAP；没有继承 Sep01 的上下文作为本日合同加载。读取 [当前 README](../../01/README.md)、[作者来源记录](supplement-20261007.md)、[首批复核](supplement-first-review-20261007.md)；机械解析旧候选表及其保留位置，不重读旧 22 篇论文或整个 Books。

实际原始证据检查包括：本轮全部 `*.request.json` 的 URL、参数、抓取时间、HTTP/curl 结果；相关 HTML 的显示文本/Next 数据、Hunyuan/Seed JSON、OpenAI XML；8 项系统线索完整题摘；catchup 新 headers/raw。Google Apr30 代表排除与 OpenAI 初报再次回源读取当前官方核心说明。旧 Ch66 两处受限比较结果复用，并重新读取第 33～58、3208～3227 行确认当前正文仍承载该命题。

旧 22 的方法、实验、Books 语义质量不在本轮重授范围；只确认冻结字段、身份、原件和复用指向。没有把 241 个当前版本线索或月目录全部转成审阅队列，没有扩扫 Weekly 来源。

## 2. 冻结、日期与新事件

- [baseline](baseline-before-supplement-20261007.md)与只读 `git show HEAD:papers/2025/05/01/README.md` **同为 79,802 字节且逐字节相同**，SHA256 `029608d49080f6b04c16c5141871fe444e1acb8b827ed8616c0161e58d059507`。保存的不只是摘要，而是旧完整报告及其证据/反证/处置记录。
- 按旧候选表的 22 个 `SF-*` / exact-v1 ID 逐项匹配当前表：均唯一存在；22 行日期仍 May1，三维与总分不变，18 行深入、4 行标准审阅的处置不变，owner 与已有覆盖决定保留，每个旧家族在当前 §4 明示复用并指向 baseline。当前表 23 行，没有重复增加 Prover-V2。这里是**机械保留核验**，不是重新证明旧公开日或旧实验。
- 当前日历范围 Apr30～May1 展示旧精确窗口触及的日期；原 `Apr30 09:00～May1 09:00 BJT` 左闭右开仍明写，新增只用 Apr30 完整自然日。它没有授权新增 May1 材料。
- [RSS 原件](supplement-20261007/openai-rss.raw)标准 XML 解析为 1251 项；初报 `Tue, 29 Apr 2025 18:00:00 GMT` 转为 BJT **Apr30 02:00**，官网显示 Apr29 的原口径保留。合同不要求新追秒级时刻，但不能丢掉已提供的 GMT。RSS SHA256 `11e5d81c046452a2d42154552386fa8cf1ead86a6bd8317356d868d48339739d`。
- May2 后续说明 RSS 为 `Fri, 02 May 2025 08:00:00 GMT` / BJT May2 16:00。它与初报是同一事故家族的不同公开解释事件；05-03 旧日期/评分不移，不把其 memory、reward、A/B 细节回填初报，不在跨日汇总中相加为两个独立事故家族。

## 3. 新初报允许命题与 Books 边界

[当前官方初报](https://openai.com/index/sycophancy-in-gpt-4o/)的 What happened、Why this matters、How addressing 支持：厂商报告回滚；承认过重短期反馈、未充分考虑长期互动，对应过度迎合行为；计划调整训练、提示与评价。支持的是**厂商公开解释及生产回归反例**，不是独立受控根因实验。3+2+2=7 与当前受限采用命题一致，纠错信号要求深入受影响内容，不能因 Books 已有覆盖降级或关闭。

当前 §4 正确保留旧反馈方案的合理性，不断言所有点赞无效；明确未披露内部 reward、权重、数据和独立对照，不能认定单一因果、长期满意优化完成、修复已验证或模型普遍安全。本地 [403 raw](supplement-20261007/openai-sycophancy.raw)仍是挑战页，不充作正文；当前可读官网也不是冻结的 2025 逐字快照。

唯一 Books 命题限评价代理。`PLATFORM-EVALUATION-SYSTEM` 的 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)第 33～58 行实际解释非随机反馈、短期满意与事实/低频风险不等价、scorer 改变行为并限制数学例子的权限；3208～3227 行明确 offline/replay/shadow/canary/online 互不替代、长期低频与因果证据限制。已有覆盖局部判断通过，不改书、不把事故未披露训练实现扩展为 RLHF 新机制。该受限命题来自主任务协调与作者拟采用范围，不虚构人类用户对细节的确认。

## 4. 8 项完整题摘独立校准

逐项读取 [systems API 原件](supplement-20261007/arxiv-topic-systems.raw)的完整 Atom title/summary 与版本身份。以下均**保留贡献潜力、首公开日期待证**；不因日期、已有 Books 原理、局部 kernel 优化或实验未核而关闭。不是 8 项已入选/已深入审阅，不评分、不采用其性能数字，不提前判 Books。

| 实际读取身份 | 原约束 → 潜在差额 → 需要重考的选择 | 后续局部路由与必要反侧 |
| --- | --- | --- |
| `2504.19442v3` Triton-distributed | 分布式 kernel 通信/计算编程分离 → 编译器内 OpenSHMEM 原语及通信、访存、计算协同 → 是否把 overlap 表达/优化交给编译器 | `TRAIN-DISTRIBUTED-TRAINING` 比较入口；核精确初版、原语语义/同步、拓扑与 64-device 条件、手调对照和开发成本。当前 v3 不能回填 Apr30 v1。 |
| `2504.19516v4` Bullet | prefill/decode 资源需求不匹配且 hybrid batch 有取舍 → 空间/时间 phase 协调、性能建模与 SLO-aware 分配 → 是否改同卡 serving 调度 | `INFER-SCHEDULING`；核 phase 并发、资源干扰、TTFT/TPOT/SLO、负载/预算及额外模型成本。**作者表的“在线离线任务”与所读 v4 摘要不符，应改为 prefill/decode；如要保留前者，须另给精确版本证据。** |
| `2504.19519v2` FlashOverlap | 整 kernel 完成才通信限制 overlap → tile 完成信号、前后数据重排、NCCL 调用 → 是否改变计算/通信提交粒度 | `TRAIN-DISTRIBUTED-TRAINING`；保留局部机制价值，核 signaling 时机、ordering/correctness、重排带宽与端到端干扰；不把摘要的 interference-free 或最高 speedup 当普遍保证。 |
| `2504.19746v1` FineQ | 粗组 mixed precision 牺牲异常值质量或存储 → 更细簇保护、索引/数据对齐及 temporal-coding accelerator → 是否共同选择数值表示与硬件执行 | `INFER-TENSORRT-LLM`；核平均 bit-width、量化质量、metadata/带宽与硬件评价方式/面积能耗条件。3bit 异常值表示不等于整模型固定 3bit 或现有 GPU 实测速率。 |
| `2504.19867v1` semi-PD | 跨 GPU PD 复制权重并迁移 KV → 分 SM 计算、共享存储及动态 partition → 是否用同卡资源划分换取存储/隔离取舍 | `INFER-PD-DISAGGREGATION`；核共享权重/KV 并发语义、容量/带宽、调节成本、模型和 SLO，不等同跨 GPU PD 的全部优点。 |
| `2504.19925v2` SYMI | 热门专家重平衡迁移 optimizer state 成本大 → optimizer 静态分片、专家权重按步 placement 且利用更新 → 是否解耦两类状态位置 | `TRAIN-DISTRIBUTED-TRAINING`；核 token skew、权重/梯度/更新一致性、网络成本和同精度 convergence 对照，不只看吞吐。v2 不回填 v1。 |
| `2504.20854v1` Genie | 真实 GPU 集群网络试验昂贵 → CPU 发流硬件试验床与 ASTRA-sim 联动 → 是否以可校准代理做网络测量 | `TRAIN-DISTRIBUTED-TRAINING`；不是仅用通用模拟器，保留测量替代条件潜力；需核 CPU/GPU 流量等价、工作负载交互、校准误差和拓扑。不能称真实 GPU 端到端复现。 |
| `2504.20964v2` OSVBench | 长上下文代码生成分数不回答规格完整性 → 状态/转移受限 programming model、复杂 specification 生成任务和模型差异 → 是否改变形式化验证的评价对象 | `PLATFORM-EVALUATION-SYSTEM`；245 任务、20k～30k token 只作当前摘要范围；核 verifier/规格完整性与潜在 vacuity、数据泄漏、预算、形式化假设。不是因 benchmark 名称自动采用，也不是因为 OS 领域自动关闭。 |

共同缺口只请求一次：这些 ID 对应首次公开正文的 BJT 日历日期，由当期官方日公告/列表 ID 映射、可信存档，或作者明确首次公开发布记录确认。API `published` 的提交口径、ID 月份、当前版号、DataCite 登记、常规公告时刻推算均不能替代。取得后定点核真实事件与精确初版；窗外按真实归属保留，不动旧 22。正文未读完不是正文外部受阻，但在日期授权前不扩读全部后版绕过门限。

## 5. 来源停止、负侧与证据权限

全部 14 个每日来源均有本轮实际入口记录；这只证明“已实查”，不证明 14 源全部覆盖。代表排除检查 2 项：Anthropic 复用已通过的政策核心校准，Google 本轮新读核心；不是所有旧排除项全量验收。

| 来源/入口 | 独立核到的实际范围 | 可接受的停止与禁止外推 |
| --- | --- | --- |
| OpenAI | RSS 1251 项与初报；Research 403 | 新事件证据局部通过；feed 不等全站，403 非正文。 |
| Anthropic | Next 数据去重 Apr/May Research 6、News 13；Apr30 09:15Z diffusion-rule 政策 | 该政策关闭通过：出口管制立场非新增模型/系统机制，不推导成本数字；两个目录不授全部 Engineering。 |
| Google | 官方 April 归档 9 标题、Apr30 唯一条目；pubs 超时，DeepMind page7 SSL 失败 | [global-health 核心](https://research.google/blog/benchmarking-llms-for-global-health/)实际是疾病 persona/诊断评测、临床语境/疾病 OOD、少样本调优及筛查 UI。现阶段领域研究暂缓，不能借 Evaluation/Data 名称重引；没有否定所有医疗来源的通用模型贡献。关闭通过，Blog 不授 Publications/DeepMind 全覆盖。 |
| Qwen | 两页原件 Apr29 Qwen3 / 下页 Mar28 邻接 | 仅旧 Blog 段未列 Apr30；不推全部 artifact 无事件。 |
| DeepSeek | Next 的 16 个 News 日期标题，Mar25/May28 邻接；伪 Research 404 | News 实查成立，原 Prover-V2 只去重；当前 Research Index 可见切片不等历史全库存。 |
| Moonshot | 单页 26 日期标题，Apr7/May6 邻接 | 单页 Blog 负侧成立；不推全部仓库首发。 |
| Hunyuan | publicList 两 renderType 的 9/6 项，displayPublishTime 均 2026 | 当前库存结束不是历史为空；2025 切片未恢复。普通 UI/历史入口核验见第 6 节。 |
| ZAI | 两页显示/Next：18 独立条目、终页 hasMore=false、最早 Dec7 | 当前目录终页不授权四月无事件，不因缺旧段记“不适用”。 |
| Seed | 论文 US 5 页 18+20+19+15+13=85，85 独立 ID / total94，p80 has_more=false；Blog 15+18+8=41，41 独立 ID / total49，p40 终页 | 逐 PublishDate/标题核，包括置顶；论文近邻 May2/Apr25、Blog May12/Apr23，所返回条目无 Apr30。只能授返回切片的目录阴性，**缺 9/8 未补齐**。PublishDate 不是 arXiv 首公开。US 修复确实恢复数组，不能继续把旧空数组当全局不可取。 |
| ERNIE | Blog 页1 10 项、页2 6 项，页2指回页1，最早 **Jun30 2025** | 两页 Blog 没有 May9，作者混写目录范围须修正；即便另有 May9 的论文目录，也须单列入口/证据。均不能推出 Apr30 来源不存在。 |
| MiMo | 当前 Paper 8 条最早 May12；Blog 15 卡日期不全；Apr30 README commit `0f485cc...` | 本地 commit 是简化 transformers 推理示例的变更，不是公开首发证明。当前官方 README 含后续更新，不能整体倒填 Apr30。首次公开缺口保留，但定点历史/发布核验仍可做。 |
| MiniMax | EN12/CN13 当前可见项及 CollectionPage，旧目录缺段 | 当前有限页不能当四月全目录或零发布；先核实际 More/分页，不凭自造 page 参数宣布终页。 |
| arXiv | 同日 Advanced 200 实际日期表单错误；相邻日响应仅 807449/952285 字节、1～200/2979、Announced 仅 Apr2025；月表 CL April 尾100/May头50、DC April首100 | 退化宽入口有界停止合理；不关闭2979、不授Apr30日窗。API 四主题 `submittedDate:[202504280000 TO202504302359]` 返回100/225、22/22、100/202、95/95，共317行/241当前版本ID，仅邻近提交线索；不授全量初筛。 |

新增 [catchup headers](supplement-20261007/arxiv-catchup-correct.headers)/[raw](supplement-20261007/arxiv-catchup-correct.raw)独立读取：官方表单 GET `subject=cs.CL&date=2025-04-30&include_abs=True`，301 到 `/catchup/cs.CL/2025-04-30?abs=True`，最终 **HTTP400 / Catchup only allowed for past 90 days**，headers 时间 07:47:25 UTC。不是错误参数、零条目或单凭路径猜测；这个当前入口不能恢复该历史日。

另定点解码旧 April/May recovery gzip 的 `authority_boundary`：DataCite Updated:v1 映射公告日程、部分相邻 ID reconciliation，非独立官方日批次快照。旧375=22+353及旧完成标签仅存档，不能授新材料日归属，也不据此改冻结旧候选。

## 6. 给 root 的普通工作与外部清单

**当前可以继续，不应包装成外部终态的事项：**

1. 修正 Bullet 所读 v4 的 prefill/decode 语义，以及 ERNIE Blog 的 Jun30 最早日期/独立目录范围。只修本轮来源说明，不改旧候选日期或得分。将 Google 代表关闭、8 项贡献潜力与本次已完成检查从“待独核”停点中同步清楚，再做受影响范围复核。
2. Seed 已取得合法终 cursor，但 total 与返回不等。先从实际前端/客户端支持的 locale、过滤含义核 9/8 缺差，作一次有界恢复/诊断并保存失败或接口限制；不是凭空接 p100，也不是必须审全年94/49。当前记录没有证明这些缺差已穷尽可用入口，不能仅因不是 Apr30 返回条目就排除缺段。
3. Hunyuan 动态历史切片、MiniMax More/真实分页、Google pubs/DeepMind 与 Meta 的历史入口尚仅有当前有限页或 curl 失败。通过可用 web/浏览器对**目标 Apr30 历史入口**做有界原始恢复，或记录具体无历史选择/合法 cursor/失败响应。curl 单次失败不等所有工具路线已穷尽，不需全站/全月逐项重扫。
4. MiMo 已有明确 Apr30 commit 身份；可定点检查其 README/原始发布说明与当前后续更新的区别，成功或失败均留范围。写后看到作者新增 15:54 官方域名限定查询及停止记录，已读该记录；未独立读这些搜索的全部结果，不授其全量复核。现有提交元数据已足以否定“commit 日期直接授权首次公开”，不要求重复无界社交搜索；原作者明确首发记录仍是具名缺口。ZAI/ERNIE 若当前官方目录确无旧段，保留已证实的有限终页，不强制无界仓库考古。

**不能由当前公开接口完成的已隔离材料：**

- arXiv Apr30 官方日公告/列表与上述 8 ID 的首公开映射；可接受当期原始列表存档或作者明确首公开记录，要求日历日期、不追加秒级条件。正确 catchup 的90天限制、月表退化和旧推算已说明为什么当前不足。
- Google Publications/DeepMind、Meta、Hunyuan、ZAI、ERNIE、MiniMax 四月历史目录，以及 MiMo 首发记录、Seed 缺差条目；普通路线核验后仍不可得时，请求相应当期官方切片/存档或具体材料的原始发布。每个缺口只按受影响来源/身份重开，不要求年度全集替代单日事实。

**当前可接受停点：** 23 行原候选表机械保留；新增确定落窗 1 家族/1 事故事件、受限证据与 Ch66 已有覆盖 1；8 项贡献潜力/日期待证隔离；两项代表排除通过；来源只授上表实际切片。普通事项尚在，故本次不能给日级完成通过。完成普通事项并局部复核后，仍不可恢复的外部材料可按合同终态保留，但它们不支持正面证据、Books、零发布、无遗漏或 Coverage/Evidence 通过。

用户正在被询问单日受阻与另行年度方案的选择，**尚无年度替代授权**。共同公告缺口可以向主任务报告，但不能自行年度去重采纳/缺日单留，不能把本日检查外推为162份现存 Daily 已扫完。

## 7. 机器检查与记录边界

本轮只读运行 `python3 scripts/validate_research.py --report papers/2025/05/01/README.md`：1 份 V3 schema/consistency passed；`git diff --check -- papers/2025/05/01/README.md` 无诊断。它们不消除第 6 节语义/入口待办。

本次复核目标快照：README SHA256 `7886c7dc0a94e0cf58934c89368fa02fcd8b277eabf49d7b0804f052081d23be`；含 catchup 的初次 source 快照 SHA256 `c60bad41a649f6a01b2da0d7c28c80137d6de82e5afc988f81c2c48a64d17f12`，写后追加 MiMo 有界搜索记录的快照为 `9ed2b2dc39b8e962eded0367a6953a21a889f2b12452c5d77353a9e6d4153be2`，该差额已定点读取。用于标明检查对象，不创建额外完成账本；后续作者修正须定点重核差额。

本文件写后检查：10 个本地链接均存在，Markdown 表格/围栏无异常；`git diff --no-index --check /dev/null <本文件>` 无空白诊断（新增文件差异退出码 1，不是校验错误）。本 agent 未 stage、commit、push，不修改 Report/Books/State/合同；May01 首批文件另按请求仅修协调来源措辞与 Gibbs 身份，不改变实际读取/裁决。写后发现两个首批文件已被其他工作流加入 index，未干预其状态，也不把它记成本 agent 的 Git 动作。
