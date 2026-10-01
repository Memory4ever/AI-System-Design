# 2026-04-28 Daily V3 恢复检查点

本日作者：apr02。固定北京时间窗口为 `[2026-04-27T09:00:00+08:00, 2026-04-28T09:00:00+08:00)`。恢复时已重新读取仓库 `AGENTS.md`、统一 Prompt、三份当前研究合同、`ROADMAP.md` 及四月 V3 checkpoint。只处理本日期独立材料；旧 README 的 V2.1 `Complete/Passed` 字段已被页首明确降为历史记录，不代表 V3 验收。04/22、04/25 已各自完成有界独立日级验收；它们的完成不替代 04/28 的准入、来源、Books 与日级 Gate。

## 旧库存不能直接构成当窗候选分母

### 快速合同漏斗（2026-09-29 恢复口径，非冻结分母）

| 层级 | 当前可核数量与状态 | 不可偷换为 |
| --- | --- | --- |
| 原始身份与来源 | 相邻批次账本给 `2604.22754`～`2604.24764` 共 945 个待核公告身份，旧排除集 834 个标题已全览；官方十二分类月页实际读到 1,229 行、845 个去重 ID，仅为交叉查漏的分类标题宽库存。旧提交日 API 的 1,183 条属于另一时间字段，不能合并入本日。 | 945 或 845 个候选、全日已完成题摘审阅。 |
| 完整题摘准入工作 | 旧保留线索 111 个已按完整题摘重筛，作者工作态为 41 个具名/拟前关、70 个开放；旧排除侧的 44 条定点复读完整摘要、15 条恢复为待消歧线索，分类页另有 3 条新线索。原 111 与排除侧 44 不重叠，故已明确记录 **155 个完整题摘读取**；这不是要求对其余标题全取摘要。`70+15+3=88` 是身份去重后的**工作上限**，非正面候选。后 51 条的非作者准入口径及所有开放线索的具体增量仍须收束。 | 111、70、88 个正式候选或 88 篇待全文审阅。 |
| 正式候选及证据 | 当前正式 §3 只有 8 个已判定子集，均已完成必要 exact-v1 审阅、评分、source→实际 owner 比较及有界日期/非作者单篇核；其余开放线索未获准入与日期双门槛，不预填正式分母。 | 8 是最终分母，或已有单篇审查等于日级 Gate。 |
| Books 实际状态 | 上述 8 项为 3 项真实写入并获非作者写后 PASS、5 项具体 Existing Coverage；其他 `Books gap` 仅属待准入/日期/写前裁决的作者提案。 | 章名相关即整合、proposal 即实际写入。 |

本轮**没有扩张 raw 或全文队列**。对既有开放线索按“旧判断→原文具体增量→会改变的选择”快速裁决：`.23626` 的旧“无历史图消融”理由确有误，读过必要段和 Ch81/82 后提出新的具名前关理由，仍待非作者准入核；`.23455` 的用户可见症状→后端 fault 同事件评价对象可能真实不同，暂留待核，而不是因已有 Ch66 主题词就关闭。二者不改变 8 个正式候选、111/70/41 工作状态或 88 上限。对明确范围外标题直接关闭；含糊者读完整摘要，只在贡献判断依赖正文事实时读必要局部，不继续把每条旧开放线索都变成独立全文/Books 小项目。首公开不确定但贡献已排除的条目停在具名关闭，不为拒绝它追完整版本史。

下一批普通可执行项按**共享错误理由**合并处理，而非逐篇创建全文任务：先对 41 个作者拟前关中的代表负例和 70 个开放项中的仅主题映射/局部配方作双向独立准入校准；15 个排除侧重开线索已经有 10 个继续/5 个拟关闭的必要差异记录，非新的 15 篇自动候选；3 个分类新增线索在必要贡献判断后均仍有晚于截点的日期字段，只对真正过准入者定点解锁。随后仅对准入且可归窗的身份做必要证据、评分和 Books。当前**普通待办未归零**：旧开放 70 中已有 8 项正式子集，余 62；排除侧重开 15 项（含 5 个尚待独立校准的作者拟关闭），分类新增 3 项，合计 **80 个未终态工作身份**。其中不少可按已有共通理由快速关闭，80 不是必须全文审阅数量或精确最终候选数。外部历史目录和个别 date 例外另按来源表隔离；不与普通待办混写。

当前 scoped `validate_research.py --report papers/2026/04/28/README.md` 通过格式/可判定一致性，`git diff --check` 通过本 checkpoint；这两项均不判定上述 80 个普通身份、来源日期或独立日级语义 Gate，正式报告继续标“进行中”。

- 旧 [README](../../28/README.md) 的 `945 raw / 111 retained` 以 DataCite initial DOI `created` 当 owner-day proxy；DOI 入库日不是首次公开，原 `Complete` 不能继承。
- 另一份已存 [arXiv API 枚举](./arxiv-api-enumeration.json) 实际以 `submittedDate:[20260427010000 TO 20260428010000]` 查询，`start=0` 取 1000、`start=1000` 取 183，合计 1183 条；这是**提交时间窗口**，不是公开公告窗口。其 ID 月份为 `2604` 1140、`2605` 32、`2606` 8、`2607` 1、`2608` 2。arXiv [官方公告说明](https://info.arxiv.org/help/availability.html)明确 ID 在首次公告时分配、按首次公告月份编号，且提交可因审核而延后。后四个月 ID 的 43 项是这批提交窗口不能等于本日公开窗口的直接反例；不能把其中 1140 个 2604 ID 自动转为本日候选。
- [旧 screening ledger](./screening-ledger-final.json)把上述 1183 条全标 `full_semantic_screened`、保留 61、关闭 1122；其输入以**当前 API 返回的标题/摘要**为主，部分身份已到 v2 或之后。现阶段只作为线索和可能复用的逐项理由，不沿用 `gate_status=independent_prewrite_pass`、日期、分数或冻结分母，也不因此逐项重读 1183 篇全文。
- 官方 arXiv 常规周一 20:00 美东公告在夏令时为周二 08:00 北京时间，落在本窗；但公告时刻规则不能单独给任何一个身份定日。须定点取得本批官方列表/OAI与连续 ID 边界、相邻批次和 v1 状态，例外单列；`submitted`、DataCite `created` 或当前 OAI datestamp 不单独定 owner。

### 已有官方 OAI 快照的有界交叉检查

历史抓取的 arXiv 官方 `ListIdentifiers` 快照在 `../arxiv-owner-replay-20260903/oai-list-identifiers/2026-04-27-cs.xml`、`2026-04-28-cs.xml`、`2026-04-29-cs.xml`，请求原字段为 `metadataPrefix=arXivRaw`、`set=cs`、相应 `from=until` 日；28日快照 responseDate 为 `2026-09-03T03:32:24Z`。在 ID 数字≥`2604.22750` 的 CS set 中，28日快照有847个身份，最小`2604.22754`、最大`2604.24756`；27日快照无该段，29日快照又有422个、最小`2604.22761`、最大`2604.25914`。这些是**按 OAI datestamp 变化**的集合，有旧 ID 修订/交叉上市，绝非847个本日新稿，也不能将区间两端自动填满。

将28日这847个 CS set 变化 ID 与旧 submittedDate API 的1183身份按 ID 去重求差，**521个**28日 OAI 身份不在旧提交日查询中（起始例：`2604.22754`～`2604.22760`）；原因可包括更早提交/公告延后或后续元数据变化，不能逐个未经核实地叫“当日新论文”。但它已直接否定“提交日查询覆盖当日公告批次”的旧完整性断言。反方向的 submittedDate 库存也含43个 `2605`～`2608` ID，故两者不能简单合并为新分母。下一步以主题入口和官方当批身份筛选，旧全量集合只做缺漏线索。

官方个案交叉：[2604.22754v1](https://arxiv.org/abs/2604.22754)页面虽显示提交于02/19，arXiv ID是04月且28日 OAI 有记录，说明“提交早于ID月份”属正常而非自动窗外；这是一篇食品包装OCR benchmark，题摘在当前项目范围外，贡献可前分母关闭，无须为排除它证明精确公开小时。[2604.23927](https://arxiv.org/abs/2604.23927) v1 提交04/27T01:01:32Z、后有05/14 v2，旧API标题/摘要是现版本风险样本；其眼镜声区定位属领域任务，不因混入旧缓存变成系统候选。[2604.24756v1](https://arxiv.org/abs/2604.24756) 提交04/27T17:56:14Z、28日OAI列入，但属拍卖算法范围外。三例只说明字段关系和范围裁决，**未证明全批精确first-public时刻或完整候选分母**。

### 相邻批次的有限归属推断（不是 DOI 日期等同公告）

已存三日官方源回放的原始身份边界为：04/27 账本 `2604.21932`～`2604.22753`（339 身份），04/28 账本 `2604.22754`～`2604.24764`（945 身份），04/29 账本 `2604.24765`～`2604.25917`（446 身份）。相邻 ID 在两处无断裂；04/28 的 DataCite 入库集中在 04/28T03:07～03:55Z，v1 元数据 `Updated` 分布为 04/28T00:00～02:06Z；04/27 与 04/29 的入库簇分别在各自 01:24～01:45Z、01:49～02:25Z。arXiv [官方公告时钟](https://info.arxiv.org/help/availability.html)将周一 20:00 ET 批次放在北京时间 04/28 08:00；官方 04/28 OAI 变化集起于 `2604.22754`，与相邻 ID 边界相互支持。**这只是将 `22754`～`24764` 视为待核本日公告批次的有界推断**：DataCite `created`、v1 `Updated` 和 OAI datestamp 均不单独证明首次公开；并非证明这 945 条逐篇都在 08:00 公开，更不等于 945 条贡献候选。04/28 v1 `Updated` 还有 443 条位于本窗 09:00 截点之后或边界上，必须按公告批次/版本例外定点查，不能按单个字段机械划走或纳入。后续对真正通过贡献准入的身份逐项核版本与反例；区间外的提交日检索身份不回填。

## 下一独立工作单元

### 公告段边界的官方 v1 个案抽样（2026-09-28 定点复核）

相邻五个官方摘要页再次确认不能把提交时间当公告：前界 [`2604.22753`](https://arxiv.org/abs/2604.22753) 的 v1 提交为 04/24T17:59:42Z；段首 [`2604.22754v1`](https://arxiv.org/abs/2604.22754) 是 02/19T20:19:49Z；中段 [`2604.23798v1`](https://arxiv.org/abs/2604.23798) 是 04/26T16:41:30Z；段末 [`2604.24764v1`](https://arxiv.org/abs/2604.24764) 是 04/27T17:59:56Z，且其摘要页现已到 v4，后发正文不得回填；后界 [`2604.24765v1`](https://arxiv.org/abs/2604.24765) 又是 04/04T03:15:27Z。提交日期跨月、同公告段内不单调，正是采用**官方公告槽＋连续 ID 邻界＋OAI 批次交叉**作有界 owner 推断、逐项保留例外的理由。这五个 submitted 字段本身均**不证明**逐篇公开时刻；抽样也不宣称对 945 身份逐一公告复验。

1. 恢复 04/27 20:00 ET 官方公告批次的 ID 与类别边界，记录范围、可能的 deferred/替换例外；再从旧缓存中只恢复身份和必要题摘，不用旧 111 或 61 当分母。
2. 按 `docs/RESEARCH_SOURCES.md` 每日十四来源逐项核本窗可见目录及精确限制；跨窗且未变的实际停点可复用，不能复用旧日报仅有 arXiv 一行的覆盖声明。
3. 对确定落窗且在项目范围内的材料按完整题摘判断**具体长期贡献**；只对真正入选者核 exact-v1 必要方法/对照/反证、三维评分、实际 Books 命题。已有 `_sources/exact-v1/` HTML 只在版本身份吻合时复用。
4. 与共享 Books 的 owner 锁及非作者写前/写后、日级语义 Gate 分开记录。未知公开日的材料精确隔离，不挪入本日也不冒充零命中；可执行的来源/筛选/Books 工作保持普通待办。

此处只是日期污染发现与可恢复入口，**不是本日 Coverage、Evidence 或 Books 通过**。

## 每日机构来源首批有界检查（2026-09-28 07:25 北京时间前）

- `SRC-QWEN`：官方动态 Research/Article 接口 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 返回可见 40 项，日期从 2025-11 至 2026-09；其中 04/22 10:00+08 后相邻可见项为 FlashQLA 的 **04/28 10:00+08**，晚于本窗 09:00 截点，不能回填为本日报候选。官方静态 `GET https://qwen.ai/api/page_config?code=research.research-list` 返回 60 项，最大 `date=2025-12-23T05:08:30Z`。这是两段官网 Research 可见列表的停点，不声称作者所有 arXiv 稿零命中。
- `SRC-TENCENT-HUNYUAN`：官方“全部”列表对应 `POST https://api.hunyuan.tencent.com/api/blog/publicList`、`{"pageNum":1,"pageSize":100,"renderType":0}` 返回 `totalNum=9/list=9`；相邻 04/30《Real life is where context gets hard》与 04/23《Hy3 preview》之间无本窗 Research 条目。`displayPublishTime` 是 Unix 秒；这里只确认完整可见目录，不能代替作者论文/仓库事件检查。
- `SRC-BYTEDANCE-SEED`：官方 Publications API `GET https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20`，请求头 `x-tt-locale: US`，返回 `total=242`、本页 20、`next_page_token=40`；按 `ArticleMeta.PublishDate` 毫秒倒序，本页从 05/12T16Z 经 04/29T16Z 跳到 04/25T16Z，横跨本窗 04/27T01Z～04/28T01Z 而无可见论文目录条目。Blog type=2 和仓库重要发布仍需单独定点确认；不能把 242 全部当日报筛选队列。
- `SRC-BAIDU-ERNIE`：官方 [中文博客](https://ernie.baidu.com/blog/zh/) 可见首页相邻日期为 04/30、04/15，无 04/27～28 条目；这只覆盖 Blog 首页，PaddlePaddle/ERNIE 重要 release 尚待检查。
- `SRC-MINIMAX`：中文官方 [Research/Blog 列表](https://www.minimax.cn/blog) 命中 [《MiniMax Agent Team: 为长程任务，持续进化而生》](https://www.minimax.cn/blog/minimax-agent-team-long-running-1779893521)，页面及 JSON-LD `datePublished=2026-04-27T12:00:00.000Z`（本窗北京时间 20:00）。但同题英文官方 [文章](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953) 明示 05/27，JSON-LD `2026-05-27T00:00:00.000Z`，中文 URL 中 Unix 尾数亦对应 05/27；故**不能断言家族在 04/27 首公开**。已读中文原文核心 §3–4：Leader/Worker/Verifier、producing→verifying→done、IM 异步与交接成本，主要是 Agent Team 产品组织和成熟协作原则，未公开足以改变当前系统责任/权限/评价合同的可检验新机制或受控反证，按本项目贡献门槛作此家族的前分母关闭；不因日期疑点扩大版本史，也不把产品发布数字写进 Books。MiniMax CLI 官方 release 列表在本窗 `[04/27T01Z,04/28T01Z)` 检出零 release；这仅是该仓库 release 层，不代表整家机构。Agent Tech Blog 历史目录仍需核或精确隔离。

上述是有界来源子入口结果，**每日十四来源尚未闭合，arXiv 当窗新稿集合也尚未确认**。有确切跨窗事件（例如 Qwen 04/28 10:00+08）归后日恢复线索，不改本窗候选。

## 每日机构来源第二批有界检查

- `SRC-OPENAI`：官方 `https://openai.com/news/rss.xml` 当次枚举历史 04/27～28 UTC 事件，04/27T00Z 的 Symphony 和 Choco 早于本窗 04/27T01Z；落窗四条为 04/27T06Z [微软合作下一阶段](https://openai.com/index/next-phase-of-microsoft-partnership/)、04/27T14Z [FedRAMP Moderate](https://openai.com/index/openai-available-at-fedramp-moderate/)、04/28T00Z [OpenAI on AWS](https://openai.com/index/openai-on-aws/)与[community safety](https://openai.com/index/our-commitment-to-community-safety/)。已读后两者核心正文：AWS 是 GPT-5.5/ Codex/Managed Agents 的有限预览及 provider/数据处理版本事实，未披露新的模型/系统机制或可核实设计对照；安全文章概述现有监测→人工复核→升级路径，无新增实现参数、受控证据或明确改变当前知识树授权边界的事件。前两者标题/原文按合作与合规发布范围关闭，不将政策/商业可用性强行评成长期模型机制。四项均留此逐家族理由、不评分。RSS 是 News，不代表 Research/Publication 历史列表覆盖，后者仍精确缺口；不能写整个 OpenAI 原始零命中。
- `SRC-ANTHROPIC`：官方 `https://www.anthropic.com/research` HTML 的原始 `publishedOn` ISO 时间，04/22T14:12:30.673Z、14:27:03.434Z 后直接到 04/29T20:26Z、04/30T16:35Z，完整跨本窗 `[04/27T01Z,04/28T01Z)`，可见 Research 列表无当窗条目；不代表所有作者投稿。
- `SRC-GOOGLE-AI`：官方 [DeepMind 04/27 韩国合作](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)只标自然日，正文是 AI for Science 机构合作与既有模型应用清单，无当前项目主线新机制，按范围/贡献前分母关闭，无需为拒绝它推定 09:00 后。Google Research Blog 当前首页不回溯到四月；04/25 实际核过 April Blog 04/22→04/29 相邻段，可核实后复用。Publications 历史原始入口仍不可由 Blog 替代，单列外部检索限制，不冒作零论文。
- `SRC-ZAI`：官方 [智谱 Research](https://www.zhipuai.cn/zh/research) 可见排序从 04/29《Scaling Pain》直接到 04/07《GLM-5.1》，无 04/27～28 条目；日期为页面自然日，只说明目录停点。官方 release notes 与仓库重要 release/论文须另查，不从目录零推全文零。
- `SRC-BYTEDANCE-SEED` 补项：Blog API `article_type=2,page_token=0,count=20` 返回 15 项、`total=95,next=20`；相邻 PublishDate 为 04/22T16Z→04/08T16Z，无本窗 Blog 列项。与上节 Publications 页 20～39 合起来只证明这两个官网可见目录，不证明外链 arXiv 公告日，也未逐篇审 242/95 项。
- `SRC-MOONSHOT`：`https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100` 中 1.39.0=04/24T06:22:19Z、下一 1.40.0=**04/28T13:51:04Z**，后者晚于本窗截止，归真实后日；所见 release 层本窗无新增。Kimi Platform Blog 历史目录仍需精确隔离/补检，不把 GitHub 一项替代机构整体。

这些结果继续是**局部来源停点**而非十四源 Gate。日期只用于相应官方事件；拒绝范围外/既有商业合作的材料不追完整发表史。

## 每日机构来源第三批有界检查

- `SRC-DEEPSEEK`：官方 [Research & News](https://deepseek.com/en/news/) 可见 News 从 04/24 V4 Preview 直接到 09/10 V4.1；Research Index 从 02/25 DualPath 直接到 06/24 V4 正式论文，无本窗目录列项。官方 [V4 技术说明 PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf) 页首写 `Publication date: April 27, 2026`、`Updated date: April 24, 2026`，次页又写模型 `Release date April 24, 2026`；自然日 publication 无时区/时刻，且未证明是 April24 Preview 之外的独立新版本。其 CSA/HCA、mHC、Muon 是厂商版本描述，不提供可分离受控机制结果；先作**版本材料及日期待核线索**，不在本日报计入评分/Books，不回填 06/24 后发论文。此处官网列表已查；透明度卡片的首次可见时刻不以 PDF 内印刷日自动定窗。
- `SRC-META-AI`：官方 [Meta Blog](https://ai.meta.com/blog/) 当前可见分页含 04/08 Muse Spark→06/29 Brain2Qwerty，未见 04/27–28，且 [Research 首页](https://ai.meta.com/research/)在当前抓取正文为空；[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)为近 1975 条分页结果、首屏更新至 09 月，不能把首屏无本窗当作完整历史无命中。限定为 Blog 可见段已检查、Publications 必要历史日期页**受阻隔离**；已有当窗作者 arXiv 若命中另按 family 去重，不以该限制阻断其证据审阅。
- `SRC-GOOGLE-AI` 补项：官方 [DeepMind Publications](https://deepmind.google/research/publications/) 当前总 264 条，实际只读首屏 25 条，日期从 09/01 倒序至 2025/10；其中相邻段为 04/25 `ProEval`、04/23 `Dynamic Reflections`、04/22 `Image Generators are Generalist Vision Learners`，故其**首屏可见条目**跨本窗无 04/27～28 日期。作者来源与首次公开仍须按具体条目核，不把站点日标签当公开小时。[Google Research Publications](https://research.google/pubs/) 当前 11,555 条、2026 年过滤计数 360，首页 15 条按年份显示而非 04/27–28 的可复核日排序；未找到能有界停在本窗的日期页。Google Research 历史 2026 条目保留精确检索限制，不用 DeepMind 子目录替代它。
- `SRC-MOONSHOT` 补项：[Kimi Platform Blog](https://platform.kimi.com/blog) 直读当前可见 26 个题名/日期，首页自 2025/11/07 至 2024/05/29，未包含 2026 历史段；这可能是旧目录，不能把 2025 的顶项当 2026 无 Blog 发布。当前可闭合的仍是前述 CLI release 定点；Blog 2026 日期索引待恢复，按外部目录缺口隔离，不再重复翻同一静态页。
- `SRC-XIAOMI-MIMO`：官方 [MiMo 首页 Paper 列表](https://mimo.xiaomi.com/)从 06/29 MOPD 直接到 03/13 ARL-Tangram，跨本窗无 Paper 列项。该页 Blog 卡片未标日期，不能据排列断言无 04/27–28 Blog；`XiaomiMiMo` 官方仓库重要 release 历史仍须定点核或单列限制。
- `SRC-MINIMAX` 补项：[Agent Tech Blog 文档索引](https://agent.minimax.io/docs/llms.txt) 当前只列一篇 [Agent Team](https://agent.minimax.io/docs/techblog/agent-team.md)，与中文/英文官方同题文章为一个 Source Family，不另计。索引本身没有可信历史首发时刻；前节中文/英文日期冲突和贡献关闭仍成立，不因 docs 复制多算一条。

`SRC-ZAI` 发布说明补核：官方 [New Released](https://docs.z.ai/release-notes/new-released) 的模型日期从 06/16 GLM-5.2 直接跳到 04/07 GLM-5.1，确实跨过本窗；这与上述 Research 04/29→04/07 目录停点和选定 GLM-5 仓库 release=0 相互独立。`SRC-TENCENT-HUNYUAN` 的完整可见 Research 9/9、`SRC-BYTEDANCE-SEED` 的 Publications/Blog 跨窗页段也已和选定重要 release 层共同形成本次注册入口的有界停点。因此正式表把这三行改为“已检查”，但不声称逐一枚举机构所有旧仓库、作者稿或站外发表；若有具名重要 release/原稿线索，仅重开该身份。

目前仍有 Google Research Publications、OpenAI Research/Publication、Meta Publications 及各机构重要仓库发布等不同程度的历史目录缺口；其范围、已尝试入口与重开条件需在正式来源表逐项写准，不能被以上局部“无列项”覆盖。

## 题摘与证据审阅 checkpoint（续）

### 官方仓库重要发布层的有界补检（2026-09-28）

GitHub 官方 REST `GET /orgs/<org>/repos?sort=created&direction=desc` 只用于**新仓库身份发现**，`created_at` 不等于论文或 release 首发；只看普通 `pushed_at` 更不能计新研究。实际读 `Tencent-Hunyuan` 每页 20 的第 1–2 页（由 05/06 跳到 04/29、04/22）、`ByteDance-Seed` 首 20（05/06→04/23）、`zai-org` 首 20（04/28T12:32Z 和 10:33Z 两项均晚于本窗→03/30）、`PaddlePaddle` 首 20（05/14→02/11）、`XiaomiMiMo` 全部 18、`MiniMax-AI` 全部 35、`MoonshotAI` 全部 43。所见**新建仓库**均无 `[04/27T01Z,04/28T01Z)` 命中；这不表示已有仓库无新 tag/release、论文或普通代码改动。API 的具体例子：[腾讯组织](https://api.github.com/orgs/Tencent-Hunyuan/repos?per_page=20&sort=created&direction=desc&page=2)、[Seed 组织](https://api.github.com/orgs/ByteDance-Seed/repos?per_page=20&sort=created&direction=desc)、[智谱组织](https://api.github.com/orgs/zai-org/repos?per_page=20&sort=created&direction=desc)。

重要 release 只做**选定项目**定点：官方 GitHub release API 中 `Tencent-Hunyuan/Hy3-preview`、`zai-org/GLM-5`、`ByteDance-Seed/Seed2.0`、`XiaomiMiMo/MiMo-Skills` 可见 release 数均为 0；`PaddlePaddle/ERNIE` 唯一 release 在 2025-06-30；`MiniMax-AI/cli` 全 26 个 release，临近本窗仅 04/26T01:40:29Z `v1.0.12`，本窗无 release。Moonshot `kimi-cli` 的 1.39.0→1.40.0 边界已另核。零 release 是这些项目的发布层结果，**不是组织全仓库或全部论文零命中**。余下未穷尽的历史 tag/发布目录按来源表精确限定/隔离，不展开普通 commits 或全年仓库清单。

官方十二分类的月页标题补检另见 [独立记录](./V3_ARXIV_OFFICIAL_CATEGORY_TITLE_CHECK.md)：实际 1,229 分类行/845 去重 ID 是宽标题库存，不是候选；`.23519` 具名前关闭，`.24222/.24391/.24608` 三条需独立准入与日期核的线索，均未评分或进入 Books。

OpenAI Research/Publication 的有界补检：官方 [Research sitemap](https://openai.com/sitemap.xml/research/) 本次返回 52 个 `<loc>`，[Publication sitemap](https://openai.com/sitemap.xml/publication/) 返回 200 个 `<loc>`；两者有交集，且 sitemap `lastmod` 不等于首发。对单篇正文 `https://openai.com/index/what-parameter-golf-taught-us/` 的直接读取返回 Cloudflare `HTTP 403` challenge；Research index 也未在本次终端直取中给出可用日期目录。官方域名定点日期搜索仅复现已在 News RSS 处理的 04/27–28 合作、安全及应用文章，搜索召回不是历史目录全覆盖。因此 `SRC-OPENAI` 的 News 四项可保留已判结果，而 Research/Publication 历史条目仍标**未完成/外部访问限制**：恢复单篇官方 `datePublished` 或可分页的官方目录后，仅对本窗附近条目定点审阅，不把 52+200 URL 全文化、不称零研究命中。

- 旧 V2.1 `retained` 的 111 个身份已分四个有限区段重新做完整题摘贡献判断，见 [首批](./V3_ARXIV_ADMISSION_BATCH1.md)、[第二批](./V3_ARXIV_ADMISSION_BATCH2.md)、[第三批前十](./V3_ARXIV_ADMISSION_BATCH3A.md)、[中十](./V3_ARXIV_ADMISSION_BATCH3B.md)、[后十](./V3_ARXIV_ADMISSION_BATCH3C.md)、[末批前十](./V3_ARXIV_ADMISSION_BATCH4A.md)、[末批后十一](./V3_ARXIV_ADMISSION_BATCH4B.md)。这 **不是** 111 个候选，也不取代官方公告 945 身份的反向查漏。首批 16 继续/1 最小消歧/13 关闭，`.22901` 定点重开后关闭已获非作者核；第二批 11/9/10 经非作者双向校准，`.23467/.23626` 纠正为待核，`.23646` 不再误称无威胁模型。后 51 条尚待非作者有限准入校准，所有开放项仍要按真实长期贡献剪枝。
- 已完成两项官方 v1 与实际 Books 的 source→owner 预审，见 [前两项](./V3_FIRST_TWO_SOURCE_REVIEW.md)：`.22782` 训练期随机跨层 KV retention，`.22783` PEFT adapter 激活形状，各有 Ch45/Ch30 的具体增量；两处随后已获协调锁实写和[非作者写后通过](./V3_ROOT_22782_22783_WRITE_AFTER.md)，可计单篇 Integrate，但不能计整日 Gate。另 [TCRM `.22981` PDF v1](./V3_TCRM_EXACT_V1_REVIEW.md) 已对 Ch32 实际机制段，暂作 Existing Coverage；其“独立 prefix-value state”有可能误读为新网络，已向 root 提最小措辞纠错，尚未取得共享写锁或日级终态。三项都未凭 submitted/DOI 单字段确定首次公告。
- 排除侧已进行一次有界[反向查漏](./V3_ARXIV_REVERSE_ADMISSION_AUDIT.md)：旧 834 排除身份标题全览，44 条潜在系统材料完整摘要定点复读，15 条恢复为**待贡献消歧工作线索**，非 15 个候选。十五条现在均已定点核必要 exact-v1 与实际 owner，见[前五](./V3_REVERSE_EXACT_V1_TRIAGE_A.md)、[中五](./V3_REVERSE_EXACT_V1_TRIAGE_B.md)、[后五](./V3_REVERSE_EXACT_V1_TRIAGE_C.md)：作者提出 10 条继续、5 条具名前关闭，仍待非作者校准，不能直接从工作上限扣除。原 ledger 的 family-specific 排除理由对未受影响项保留；旧“局部优化/无 owner 迁移”模板不能直接维持于 filtered-feedback credit、streaming revision、audio modality reliance 等命中项。
- 旧 `retained` 前七条开放身份已有两组 bounded exact-v1→实际 owner 作者侧贡献消歧，见[前四](./V3_EARLY_FOUR_EXACT_V1_TRIAGE.md)和[续三](./V3_EARLY_THREE_EXACT_V1_TRIAGE.md)：`.23046` 因 Ch72 已承载二阶状态/离线曲率 artifact 责任且实验仅二维 ONS，新增一条具名前分母关闭提案；`.22891` 的 judge 判别力/同质自偏好分账仍待非作者比较，`.22985` 的工具调用 AST/置信度为受限 Only 倾向，余项仍待必要证据。这一条提案**尚未改变**前述 70/41 计数，也不代表七篇已评分或日期核准。后续最小工作单元：非作者定点校准后 51 项的开放线索与代表性关闭、十五条反向找回的 10/5 贡献分歧；仅对最终保留者核公告日期、主要反证、三维评分与 Books 决策；来源历史目录不足精准隔离，最后交非作者日级 Gate。当前机器格式校验通过不表示任何上述语义 Gate 已过。
- 第二批开放项又以完整题摘和当前 owner 具体命题做[三条贡献反向剪枝](./V3_SECOND_BATCH_CONTRIBUTION_REPRUNE.md)：`.23272` 的 tactile/torque/future-signal 与 Ch23/25/26，`.23366` 的静态 FEVER typed evidence/三档行动与 Ch66/76，`.23553` 的 RTX5090 full-block cluster fusion 与 Ch49 已有 fusion/graph/DSMEM 成本均无新的长期权责，作者提出具名前分母关闭并保存重开条件；**三条均待非作者校准、未改当前 70/41 计数**。这不是对本批其他开放项按比例关闭，也不把摘要级排除伪装成已读全篇。
- 安全项 `.24118v1` [定点 exact-v1 审阅](./V3_AGENTVISOR_EXACT_V1_BOUNDED_REVIEW.md)发现 §4.1 Eq(6)–(7)、§4.4 与 Appendix A Algorithm 1 对首轮拒绝后的修订 `T′` 均写成直接执行，未显示重新 STI audit；故保留安全候选工作提案，并隔离“所有最终 effect 都经 Visor 授权”的强结论。只是论文协议层潜在反证、非经验证实现漏洞；待非作者复核和公告归属，不计正式分母或 Books。

截至本轮的**工作漏斗，不是候选分母**：旧 111 个 `retained` 经完整题摘先判 72 开放/39 具名前关闭；`.24441` 的 pinned-v1/Ch66 和 `.24647` 的 pinned-v1/Ch45 定点比较使作者侧改为 **70 开放/41 关闭**，两项仍待非作者校准。后段 19 个 exact-v1 消歧中，另有 7 条拟前关闭、12 条继续（含 AgentVisor 窄争议提案），尚未替换前述 70/41 口径；其中 `.24647` 已包含在 70/41 的两条提前改判中，尚未反映的拟前关为 6 条；若这 6 条独立获认可，旧 111 将是 64 开放/47 关闭。旧排除 834 标题全览、44 完整摘要定点复读得到 15 条反向线索，必要 exact-v1/owner 作者侧已全 15 条完成、拟 10 继续/5 前关闭；官方十二分类标题页另得 3 条新线索。它们均不自动成为正式候选。因此当前普通准入工作上限仍为 70+15+3=88 条；若后段尚未反映的 6 条与反向 5 条均获独立关闭认可，上限可降至 64+10+3=77 条；另 `.23046/.23272/.23366/.23553` 四条作者侧前关提案若均通过，可再降至 60+10+3=73 条，仍非评分分母。已冻结评分分母仍为零；此处原“新增真实 Books 写入零”仅为当时快照，后续两项实写见下方记录。`2604.23099v1` 已定点核出 GP 定理目标与实测总体分数不是同一个等式，保留继续但不采用摘要的无条件保证。14 来源表当前 8 已检查、1 未完成、5 受阻；混元、智谱与 Seed 官网目录和选定重要发布层有界闭合，但不代表其全部作者稿或旧仓库零遗漏。OpenAI、Google Research、Meta、Kimi Blog 与小米 Blog 的必要历史日期材料已按各行精确隔离并列重开条件；唯一来源普通待办是 arXiv 公告归属/贡献分母。格式 validator 和 diffcheck 已通过，仅证明结构，不证明此日研究完结。

补充贡献队列定位（2026-09-29）：原 batch 表中 29 条 `继续核贡献` 是**旧题摘标签**，并非还有 29 项事实疑点或自动候选。作者侧已将其中十个不重复身份按[第一组五项](./V3_FIVE_CONTRIBUTION_AMBIGUITIES.md)、[第二组五项](./V3_SECOND_FIVE_CONTRIBUTION_AMBIGUITIES.md)定点指向具体设计/评价增量；[余三项](./V3_LAST_THREE_CONTRIBUTION_AMBIGUITIES.md)处理 `.23210/.23711/.24320`；另十三身份已在[末段 A](./V3_LATE_BATCH_FINITE_TRIAGE_A.md)至[E](./V3_LATE_BATCH_FINITE_TRIAGE_E.md)具名消歧，`.23272/.23366/.23553` 三条有既存具名前关提案。29 项现在是 **13 新准入提案 + 末段十三项既有裁决 + 3 既有前关提案**的作者工作分流，仍缺相应非作者校准和正式入选后的日期/必要证据，不能把全部 29 转为分母，也不能重复扣除同一晚段关闭项。下一小单元优先让独立审阅者按共同的“真实机制增量 vs 既有组合”理由定点校准已提出的关闭和代表性准入，再冻结唯一候选身份集合；不展开官方 945 身份全篇阅读。

前两项窄写入（2026-09-29）：`2604.22782v1/.22783v1` 的官方 v1 submitted 均为 04/03，仅作来源 provenance；[独立日期记录](./V3_FIRST_TWO_DATE_BOUNDARY.md)用官方 04/28 OAI 当日出现、04/27 同类快照未出现、连续 ID 邻界、早于截止的 v1 Updated 与周一 20 ET 常规公告槽共同推断落在本窗 08～09，未把 DOI/OAI/submitted 任一字段单独当首发。root 独立通过两项 exact-v1 source→Ch45/Ch30 写前；协调锁后两处机制正文与 Review notes 已实写、锁释放，并[实际逐段写后通过](./V3_ROOT_22782_22783_WRITE_AFTER.md)。这两项 6 分因确切长期知识缺口按合同深入审阅，已可列单篇 Integrate；**但 70/41 作者题摘工作口径、88 工作上限与未冻结的全日评分分母并未因此变成最终计数，日级 Gate 仍开。**

### 十三项新准入提案与官方月页三线索的日期字段分流（非逐篇公告证明）

这 16 条仍是作者侧贡献线索，尚未经非作者准入或完整证据 Gate。只对 `arxiv-owner-replay-20260903/20260428/arxiv-owner-receipt.json` 中已保存的**原字段**定点对账；该历史 receipt 的 `owner_receipt_route` 基于 DOI/OAI 代理，不能继承为 V3 first-public 判定。全部 ID 均位于本日 `22754–24764` 连续公告段推断范围，DataCite initial created 均在 04/28T03Z 以后（北京时间 11 点以后），不可能当 09:00 前公开时刻。以 `v1 Updated` 是否早于本窗截止 04/28T01:00Z 分流，仅用于优先查例外：

| v1 元数据边界 | 精确身份与原字段 | 后续日期工作 |
| --- | --- | --- |
| 截点前七项 | `.23210` 00:25:21Z、`.23238` 00:28:08Z、`.23467` 00:42:45Z、`.23577` 00:49:52Z、`.23584` 00:50:05Z、`.23626` 00:52:46Z、`.23711` 00:57:37Z | 可沿官方公告槽＋连续 ID＋相邻 OAI 批次作有界归属推断；逐项仍须核 v1/撤回与具体例外，不能把 Updated 写为公告时刻。`.23238` 的 receipt 只有 DOI 代理路由，需补官方身份出现记录或同批邻界，不独立用 DOI 判日。 |
| 截点后九项 | `.23853` 01:06:13Z、`.23932` 01:10:56Z、`.24005` 01:15:20Z、`.24222` 01:27:11Z、`.24320` 01:33:09Z、`.24391` 01:39:22Z、`.24542` 01:50:30Z、`.24579` 01:52:31Z、`.24608` 01:56:26Z | 这些不是自动窗外，也不能机械沿整批 08～09 记入。须定点核是否先公告后 v1 更新、OAI 所示是否仅元数据变化及官方分类/邻界；若无更早公开依据，对真正通过贡献准入者保留精确 Date Hold。`.24222` 的旧 receipt 题名/摘要与 official exact-v1 不同，必须以 v1 为准。 |

上述七加九为十三旧准入提案与三条官方标题新增线索的**日期证据工作分流**，不是又新增 16 个候选、不是对 `443` 个晚字段做逐篇版本史，也不改变 `70/41` 或 `88` 工作上限。初筛可先继续；仅真正通过贡献筛选的项目才为本日报确认 first-public。

### 继续准入的独立校准队列（不改工作上限）

- [三项题摘到现有 owner 的重筛](./V3_THREE_ABSTRACT_OWNER_RESCREEN.md)记 `.23455` 用户可见症状与后端诊断证据、`.24300` 稀疏输入可答性与 gold 支持集为待贡献消歧；`.23466` 因 Ch49 已有跨硬件/端到端验收合同拟具名前关闭。此三项都不是已评分候选；`.24300` 的晚 Updated 另需日期例外或 Date Hold。
- [三项系统与评价必要对读](./V3_THREE_SYSTEM_EVAL_OWNER_TRIAGE.md)记 `.23178` judge 主导偏差诊断、`.23577` 失败定向小模型再训练/路由联动为待非作者判定的具体缺口；`.23581` 已有 Ch69 依赖图诊断正文，倾向窄 Existing；`.23987` 已有 Ch66 校准 artifact 正文，也倾向窄 Existing，但其 v1 Updated 在截点后，未解决日期前不正式采用。
- [八项真实 Books 正文及日期分流](./V3_EIGHT_ACTUAL_BODY_DATE_TRIAGE.md)确认旧开放项 `.22981/.23036/.23073/.23080/.23205/.23853/.23932/.23987` 均有对应机制正文而非仅章末 Review note；作者拟必要 exact-v1→正文比较后作窄 Existing，不因命中 source marker 自动通过。后三项 v1 Updated 为 01:06/01:10/01:13Z，须有更早官方公开依据或精确 Date Hold。已请 root 作为非作者做一组有限 source→body 校准；当前正式 04/28 候选仍只有两项已经完成的 Integrate，`70/41` 与 `88` 不变。
- `.23467` 的官方公告槽、04/27→28 OAI 身份、连续 ID 邻界与早于截点的 v1 Updated 已由 root [独立日期复核通过](./V3_ROOT_23467_DATE_BOUNDARY_INDEPENDENT.md)：只可称 arXiv v1 本窗 08～09 的有据推断，且须保留同族更早公开 artifact 重开条件；贡献准入、必要证据与 Books 均未因此通过，当前不列正式候选。
- [两条监测／VLA 贡献对读](./V3_TWO_MONITOR_VLA_ADMISSION.md)使 `.23488/.23121` 继续保留，但严格缩到训练来源×monitor 验收来源交叉失效、低数据视觉 grounding 保存×动作去噪双前向 guidance 两个可核命题；前者旧 receipt 使用后稿题名且本地 CS OAI 三日缺该身份，日期需定点补证，后者有 04/28 OAI 与早字段。两项均待非作者 source→owner/日期复核，不评分、不改正式候选或 88 上限。
- root 对上述八项中的前五项已作 [exact-v1→实际机制正文独立核验](./V3_ROOT_FIVE_EXISTING_BODY_INDEPENDENT.md)：`.22981/.23036/.23080/.23205` 的窄 Existing Coverage 写前比较通过，仍须本窗日期 Gate；`.23073` 机制正文同样吻合，且后经[独立日期判定](./V3_ROOT_23073_DATE_BOUNDARY_INDEPENDENT.md)把 arXiv v1 路径有据推断归入本窗 08～09，OAI 当前记录仅可能反映后修订，若发现同族更早全文须重开。后三项 `.23853/.23932/.23987` 晚字段既未纳入本次 source→body 复核，也不凭已有书稿回推日期。正式两项 Integrate、`70/41` 和 `88` 均未改。
- [三条真实增量的必要准入对读](./V3_THREE_TRUE_INCREMENT_ADMISSION.md)区分 `.23051` 的隐式时间 scope 继承评价、`.23459` 的多 Agent 拓扑×恶意/良性双分母、`.23333` 的前缀可解性 probe 与 policy margin reward。这三项不因现有章节主题相似而关闭，也不因方法新名自动写书；均待非作者 source→owner、日期与证据 Gate，当前计数仍不变。
- [两条 MoE 的必要贡献／owner 对读](./V3_TWO_MOE_CONTRIBUTION_OWNER_TRIAGE.md)保留 `.23108` 异宽 expert 组×同宽度混置布局、`.23150` prefill 激活→decode request clustering/条件 expert placement 的窄差异；root 已作[有限非作者 source→owner 复核](./V3_ROOT_TWO_MOE_OWNER_INDEPENDENT.md)，确认 `.23108` 的静态参数布局不等动态负载均衡，且将 `.23150` 主 owner 从训练 Ch36 纠正为推理调度 Ch56、Ch21 仅 handoff。两项仍待日期、最终评分与 Books 实际差异裁决，不预记正式候选或整合。`.24708` HDET 则在[末批必要消歧](./V3_LATE_BATCH_FINITE_TRIAGE_D.md)补明不同参数上的共同梯度 AllReduce 不等 Local SGD，但 v1 Updated 02:03Z 超本窗截止，真实贡献若通过仍先 Date Hold，须有更早可读依据。
- [三条训练／视觉选择开放线索](./V3_THREE_TRAINING_VISUAL_OWNER_TRIAGE.md)定点对读 `.23950/.24003/.24005` 的 exact-v1 必要方法与 Ch23/33 现有正文：二阶段视觉剪枝已大体覆盖，但 visual-self 与 text→vision attention 的位置偏差职责待非作者判是否值得新增；短窗本身压缩、失败组高置信步骤免负 credit 与 teacher 成功前缀导航是可能的窄增量，同时保留截断/verifier、PRM proxy、pass@10 成功轨迹与执行成本。均只是作者贡献提案，未评分、冻结或写 Books。
- [两条评价线索](./V3_TWO_EVAL_ADMISSION_TRIAGE.md)定点核 `.22891/.22985` 的 exact-v1 必要方法和 Ch66/78：分别是判别力与等质 self-preference/Null-PIR 分母分离、工具调用 AST 等价与语义 token 风险 sensor。保留双基准 judge 非真值/缓解组门槛不一致、AST 改善不遍及全部任务与八模型非多轮等边界；仍待非作者贡献与日期核，不评分、不预写 Books。
- `.23467` 已在 [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的 graph 条件段后写入 miss→本次 JIT 执行/异步 capture→event 完成后 rolling cache replay 两段；[root 非作者实际写后审计](./V3_ROOT_23467_CH49_WRITE_AFTER.md)通过，Table II 350/500-token 逐 token P99 反例、首次成本与受限 H100 配置均保留。正式 [04/28 日报](../../28/README.md)现可如实列 **3 项实际 Integrate 子集**；旧 `70/41` 题摘工作口径、`88` 工作上限仍不是冻结候选分母，日级来源/日期/负侧 Gate 继续。
- `.23073` 官方 exact-v1 §IV–VI 的冻结 VLA、任务 demo 适配的 RL token 与小型在线 actor–critic 已由 root [source→Ch26 实际正文独立核](./V3_ROOT_FIVE_EXISTING_BODY_INDEPENDENT.md)和[日期有界独立核](./V3_ROOT_23073_DATE_BOUNDARY_INDEPENDENT.md)分别通过；作者本轮另核必要方法/四真机边界，root认可 `2+2+2=6` 深入、窄 Existing Coverage。正式日报可作为**第四项已判定子集**，不是第四项新增 Books，也不冻结全日分母；若出现同族更早公开正文，重开 first-public owner。
- `.22981/.23036/.23080/.23205` 的 root source→实际正文 Existing 复核已存在，作者另作[四项日期组合提案](./V3_FOUR_EARLY_EXISTING_DATE_PROPOSAL.md)：official v1 投稿均在周五 18:00Z 后或周六、v1 Updated 均为 04/28T00Z，连续 ID 与 `.23073` 已核公告簇相邻，正常周一 20 EDT→本窗 08 BJT。此处仅请求非作者定点日期核，**未**把四项移入正式候选；机构更早正文、延迟审核及撤回仍为单篇重开条件。
- `SRC-GOOGLE-AI` 的 Google Research Blog 分入口已直接核[官方 2026 年 4 月月页](https://research.google/blog/2026/04/)：九条可见项 04/29 直接跳到 04/22，本窗 04/27 09:00～04/28 09:00 无 Blog 列项；与 04/25 历史日报旧停点一致。**这只关闭 Blog 分入口**，不能替代 Google Research Publications 约 11555 条、2026 过滤后 360 条中尚无按日有界历史停点的来源缺口，故正式来源行继续 `受阻` 而不是机构零命中。
- root 已在[四项独立日期核](./V3_ROOT_FOUR_EARLY_EXISTING_DATE_INDEPENDENT.md)中重开 `.22981/.23036/.23080/.23205` 官方 v1、公告规则与连续处理簇，准予 arXiv 路径按本窗 08～09 作有据范围推断；与既有[五项正文独立对读](./V3_ROOT_FIVE_EXISTING_BODY_INDEPENDENT.md)合并后，正式日报已同步为 **3 Integrate + 5 Existing 的已判定子集**。投稿/Updated 均不是逐篇首发秒点，机构更早全文或延期反证仍需单项重开；旧 `70/41` 题摘工作口径及 `88` 上限仍非冻结分母，整日 Gate 未过。
- 两项 MoE 的[作者日期分流](./V3_TWO_MOE_DATE_PROPOSAL.md)另查 `.23108` 当前 OAI `04/29` 与官方 v2 `04/28T02:47Z` 修订相容，不能把 v1 自动迁至次日；`.23150` 当前 OAI `04/28` 且仅 v1。两者均仍只是官方公告槽、连续 ID 与早处理簇支持的本窗**待独立确认**提案，不据此评分或进入正式分母；前者尤其不得用当前 OAI datestamp 否定已存在的 v1。
- 工作上限身份去重另以四份旧保留题摘表的**主表行**核为 111 个唯一 ID、反向查漏主表为 15 个唯一 ID，二者交集为空；官方分类新增 `.24222/.24391/.24608` 均不在上述两表主行。因此 `70+15+3=88` 的三来源在身份上无重复，但 70 仍是作者开放线索、15/3 仍是待准入，不得把 88 称作冻结候选或已完成 88 篇全文审阅。
- 分母独立校准请求已按受影响集合聚合而非重审全池：早批拟前关 `.23046/.23272/.23366/.23553`，末段 19 条中的七个拟前关 `.23941/.24013/.24198/.24074/.24086/.24583/.24647`（其中 `.24647` 已先计入当前 `70/41`，其余六尚未扣），反向 15 条中的五个拟前关 `.22820/.23734/.23855/.24026/.24618`。root 非作者尚未逐项裁决前，作者不把这些提案改为最终贡献分母。两条开放项另作[23747 训练基线必要审阅](./V3_23747_NECESSARY_CONTRIBUTION.md)和[23051 时间作用域必要审阅](./V3_23051_NECESSARY_CONTRIBUTION.md)：前者是 CPU offload 梯度 owner 与有效 token 聚合两种错误改变 SFT→RL 对照，后者是已知时间事实下对话 scope 传播的 gold/self/no-context 三条件；两者均仅为待独立 source→owner 与日期核的作者线索，不是新增正式候选或 Books。
- 第91–100项又有[四项必要准入对读](./V3_BATCH4A_NECESSARY_ADMISSION.md)：`.24432` chunk-aligned text/summary 可见性、`.24579` 合成吸收链 first-passage 分母、`.24320` 同任务多环境 rollout、`.24542` 全层 hidden 差分安全 sensor；`.24447` 的[单篇对读](./V3_24447_NECESSARY_ADMISSION.md)则把同次 denoising 的旧观测 KV 早步→新观测 KV 晚步从普通异步 pipeline 分离。五条只保留作者侧有限贡献线索；它们的 v1 Updated 均在本窗 01:00Z 截点后，如通过贡献门槛须逐项核更早公开依据，当前不计正式分母/Books。反例包括 KSA RULER8K 非全胜、DTMC仅合成链验证、DPEPO reward 消融非单调、LCF实测FPR与自适应规避、V-AEFusion stale步数及310P反向；没有把主题相似自动关掉或把局部新意自动升格。
- 旧保留末段 `.24708/.24715/.24763/.24764` 的[完整题摘与必要 exact-v1 贡献消歧](./V3_BATCH4B_FOUR_NECESSARY_ADMISSION.md)已保存：HDET 的同梯度/异参数周期合并、HyLo 的混合架构迁移、Tuna-2 的 encoder-free 训练阶段对照、World-R1 的几何 reward 与动态场景目标冲突分别是待非作者反向校准的窄线索，不自动计候选。四项 v1 `Updated` 皆为 04/28T02:03～02:06Z，晚于本窗 01:00Z 截点；当前 OAI 日期也不单独解锁。若准入须分别找更早公开依据，否则 `Date Hold`、不评分、不写 Books。
- 七份旧保留题摘表的**工作状态**另作[70 条开放线索的日期字段分层](./V3_OPEN70_DATE_STRATIFICATION.md)：111 身份中作者侧 41 个具名/拟前关、70 个开放；70/70 可联接原 receipt，39 个 v1 `Updated` 早于 01:00Z、31 个不早于。该分层不包括反向 15/分类新增 3，不是候选分母；晚字段只对通过贡献门槛者再核更早公开依据，早字段也不自动通过首次公开 Gate。
- `.23150` 已完成[有界 exact-v1 Source Review 与 Ch56 具体差异](./V3_23150_BOUNDED_SOURCE_REVIEW.md)：历史 decode 请求簇条件 `U_{d,e}` placement 不是现有 prefill-signature locality routing 的同义重复；作者未在评价中使用冗余 expert，all-to-all 字节缩减也不等 padding 后层时延或请求 SLO。其日期仍仅作者组合提案，须非作者有界归属确认后才能入正式分母／评分、申请 Ch56 锁；本页没有将其改记 Integrate。
- `.23108` 的[有界 exact-v1 Source Review](./V3_23108_BOUNDED_SOURCE_REVIEW.md)亦分开异宽 expert 的静态 all-size-set 设备组合与需组内路由支持的动态工作量均衡；Table 3 是 token-route 比例而非逐 GPU 利用率，Tables 4–5 的词频/perplexity 是难度 proxy，Table 1 同时改变 total/activated 参数。Ch21 的窄联合结构/placement 差异待日期和 root 写前裁决，未评分或写 Books。
- `.23051` 的[有界 exact-v1 Source Review](./V3_23051_BOUNDED_SOURCE_REVIEW.md)把事实有效期/Memory store audit 与**对话中隐式时间 scope 的继承、覆盖、跨实体转移**分成两种评价对象；Gold 历史、自生成历史、仅当前问题三个同题条件在 Ch66 现有 Longitudinal State 尚未明确分账，可能是窄 Books gap。Wikidata 模板、现今值 snapshot、不同链长题组与观察性 drift 均限制外推；Ch66 当前另有共享锁，不写正文，日期/非作者写前尚待核，不计分母。
- `.22879` 的[有界安全 Source Review](./V3_22879_BOUNDED_SAFETY_REVIEW.md)保留“各域图不汇总、源 sidecar 回答谓词、sink 前独立授权”的条件分支，但隔离 §4.8.4 从计算型零知识直接推出 Shannon `I(G;View)≤1 bit` 的缺桥；作者 §6 亦承认自适应多次查询泄露风险。PhantomEcosystem 的 160/40 合成机会集与普通 boolean 成本不等跨机构生产或加密模式成本。日期/非作者安全争议与 owner 裁决前不评分、不写 Ch72。
- `.22888` 的[中心数值有界复核](./V3_22888_NUMERIC_BOUNDARY.md)把官方 Tables 1/2/3/4/5 的打印 P/R 与 F1 逐项核算；SI-CH `.9334/.6442` 对应约 `.7623`，不是正文核心 `.8834`，SI、MASB、MASW、SI-BL 也有非舍入误差。该冲突只隔离正面 detector 优势及 Books 采用，不声称原始预测或全部实验已被证伪；保留非作者安全纠错/具体 owner/日期待审，不计正式分母。
- `.23584` 的[有界视觉隐私复核](./V3_23584_BOUNDED_PRIVACY_REVIEW.md)确认检索后、reader 前 identity 替换与视觉证据保真有具体长期合同价值，但 exact-v1 把 MINE 下界写成互信息上界，且 Theorem 4 把依原身份拒绝后的替换码误当独立；最小两码反例在零 attribute 泄漏下仍保留 1 bit 替换码依赖。作者仅拟 6 分并触发中心安全保证的深入争议隔离；Ch72 primary/Ch76 handoff、公告日期与反例均待非作者核，不能据实验重认率写通用隐私或直接改 Books/正式分母。
- `.23459` 的[必要 source→Ch72 对读](./V3_23459_BOUNDED_SOURCE_REVIEW.md)支持受限 architecture×opportunity-set 安全评价增量：规划拒绝、执行拒绝、部分有害动作、目标完成和正常任务成功须分账，BrowserART 与 RedCode-Gen 的拓扑排序反向；但三环境 action space/工具分区、独立 benign 集、RedCode 仅代码 judge、模型/guard 覆盖受限，不能给普适拓扑安全率。维持作者 `2+2+2=6` 安全深入提案，待非作者准入/日期/Ch72 实际 owner 裁决，不计正式分母或 Books。
- `.23577` 的[RouteNLP 有界 source→Ch56 对读](./V3_23577_BOUNDED_SOURCE_REVIEW.md)找出唯一待判增量：升级失败日志选择蒸馏数据、改变便宜 tier 后连带重训 router／重校阈值；同数据量 random-vs-targeted 只在 benchmark 支持选例分支。8 周 pilot 是 shadow、无 A/B 且未在生产失败日志运行该 co-optimization，不能把 58% 成本/P99 归因于训练闭环。保留作者 `2+2+2=6` Books-gap 深入提案，待非作者与日期核，不计正式分母或共享写入。
- `.23581` 的[有界 exact-v1→Ch69/66 对读](./V3_23581_BOUNDED_EXISTING_REVIEW.md)确认 150 人工 case/195 失败 step 的同 judge/rubric Flat 对照确有局部 DAG 诊断收益，但最低分 parent 只是 root/propagated 启发式，非 DAG/循环轨迹退步，前后修复时间分母不可当同测量。实际 Ch69 的派生诊断图与 Ch66 的 typed step/judge/effect 分账已经承载长期 owner；作者建议保留为窄 Existing Coverage 而非新增正文，待非作者和日期核，不改正式分母。
- `.23178` 的[有界 exact-v1→Ch66 对读](./V3_23178_BOUNDED_EXISTING_REVIEW.md)区分受控 STYLE/position/length 实验、MT-Bench 与 LLMBar 的策略反向及多重校正；Ch66 已承载 bias 分账、顺序/格式身份和外部校准，作者建议受限 `5` 分标准 Existing，而非把 CoT/position swap 选择表写成通则。日期与非作者 source→body 待核，不改正式分母。
- 十二分类标题页的 845 去重身份只命中旧 111 retained 中 104 项；以旧 receipt 原始 categories 反查，余七项恰为只在未注册 `cs.CR/cs.SE/cs.NI` 的 `.22935/.23374/.23455/.23711/.23932/.24118/.24579`，见[分类补检记录](./V3_ARXIV_OFFICIAL_CATEGORY_TITLE_CHECK.md)。它们由旧身份/题摘队列另行处理；分类差额已解释，但此反查不证明 845 外不存在新高信号或全日候选分母已冻结。
- 三项[末段贡献重判](./V3_THREE_REPRUNE_23941_24074_24013.md)已按 exact-v1 必要方法/关键评价和 Ch23/81/72、Ch66、Ch36 实际正文分离：`.23941` 仿真 L20 的 GUI grounding 配方拟具名前关，`.24074` 固定 judge 的 prompt 配置敏感度拟受限 5 分 Existing，`.24013` RS/AG 分解内 dependent-output-first 排程撤回原拟前关、保留窄贡献线索，但 Algorithm 1 仍逐轮 wait、实验仅 layer 前向。三项均待非作者准入及各自日期核；暂不改变 `70/41` 工作口径、正式候选分母或 Books。
- 下一组三项[有界 owner/反证对读](./V3_THREE_BOUNDARY_23987_24086_24088.md)：`.23987` Ch66 已有实际 `SF` 机制段，作者拟窄 Existing，须核真实写后/日期；`.24086` cloud waypoint anchor 的历史→当前 `SE(2)` 变换和 LiDAR local control 有窄 Ch26 gap、真机每模型 20 次，但 CMDP 不给普适硬安全；`.24088` TP 中间张量分布重整/FP8+codec 融合与 Ch36 有损传输已有原则比较后仍有条件性实现分支，INT8/格式消融不能略去。三项均未取得非作者准入/日期/Books 写前许可，不进入正式冻结集合。
- `.23318` 的[有界 credit 复核](./V3_23318_BOUNDED_CREDIT_REVIEW.md)把隐藏态 span 分布距离乘原 outcome advantage 与因果 step credit 分开；同题正误混合、条件化定理、best-observed checkpoint、默认跨 rollout 重加权及 Sinkhorn 训练成本均保留。实际 Ch33 已有 outcome 广播和字段/entropy/过程 verifier，却未具体承载该同模型 span-distribution 传感器分支；仅属作者侧潜在长期增量，仍待非作者 source→owner、日期与必要 Books 决策，不改工作池计数或正式分母。
- `.23374` 的[有界 taint 复核](./V3_23374_BOUNDED_TAINT_REVIEW.md)把显式内容、隐式 sink 决策和跨会话 lineage 分开；Ch72 已有 source→sink 与确定性授权，可能新增的仅是离线 sink-time 反事实归因和 memory 读出不即判传播的诊断职责。TaintBench propagation 标签≠unsafe effect，模板级标签/五次聚合、FN/FP 与额外审计成本均保留；仍待非作者贡献/日期/Books 裁决，不沿旧 `No Change` 自动结案。
- `.23626` 的[有界贡献重判](./V3_23626_BOUNDED_CONTRIBUTION_RECHECK.md)承认旧“无历史图贡献消融”关闭错误，保留 role×backbone 联合动作、current/history graph 和 w/o History 对照；进一步实读 Ch81/82 后，作者侧建议以“已有 workflow 修订/peer capability 历史 ledger/role 决策分责，异构图和固定三角色动作只给受限实现”为**新具名理由前分母关闭**。推理 token×价格 Cost 与 Table 4 的训练 `GPU Compute GiB` 不可混为同一成本；此建议待非作者准入核，不修改正式工作池或冻结分母。
- `.23455` 的[有界评价贡献复核](./V3_23455_BOUNDED_EVAL_CONTRIBUTION.md)实读 v1 冻结浏览器/后台 snapshot、三层标签及六模型三条件：**87 corpus≠25 场景实际测试**，446/450 次，B2/B3 同 15 turns 却不同工具集/提交率，browser-only 聚合优于 full 不能写成后台证据有害定律。Ch66 现有 outcome/trace/探索-决策分账尚未明确用户可见症状到后台 fault 的同事件跨层诊断分母；作者侧建议保留窄评价合同潜在增量，仍待非作者准入、日期与必要 Books Decision，不改工作池或正式分母。
- `.23711` Spore 在[此前三项准入提案](./V3_LAST_THREE_CONTRIBUTION_AMBIGUITIES.md)中被作者暂留；现对该提案作**快速贡献反查并提出反向改判**：官方 [exact-v1 §3–4](https://arxiv.org/html/2604.23711v1)针对推理时置入 Agent memory 的 PII，黑盒先让模型给出扰动值再在最多 20 个候选内试探，灰盒另可用 top-k logprobs；§3.4 不给形式恢复保证，560 个 TrustLLM 隐私查询构造的是合成上下文而非生产记忆。相对旧“只测训练数据记忆”，它确是不同攻击素材；但现有 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 已把训练 memorization、运行时 memory privacy unit、black/gray-box access、query family/budget、parametric prior 与 memory-induced delta、输出 release 权分开（现文约 376–382、1080–1088 行）。本稿的扰动值候选枚举是这些已设审计对象上的受限攻击实例，未改谁持有 context exposure 或 release 决策，也未给可迁移的新保证；作者侧建议以此**新具名理由前分母关闭**，非作者反向准入核前不扣 `70/41`、不删除原题摘，也不把一篇的 pass@k 外推为“单查询恢复率”。本次止于决定贡献所需源段与现有命题，不继续全文附件。

## 2026-09-30 作者普通工作收口（等待独立日级 Gate）

以上为过程停点，不能覆盖当前终判。[正式 V3 日报](../../28/README.md) 已自包含71唯一候选/71证据段：45整合、15已有覆盖、7仅报告、4中心争议终态暂缓。71=13已认可子集+65逐条身份−7具名前关；24542/24579恢复Only、22985改Only、23747 exact纠错gap改I、23711恢复为5安全深入Existing、24618恢复两个机会集I，均按具体source→actual owner而非主题名单。所有新Books窄段获非作者写前授权与实际写后通过，位置修复亦已实际复读；普通作者工作0。日期按[有界首公开组合](./V3_BOUNDED_PUBLICATION_RESOLUTION.md)取公告/连续ID/OAI/v1组合，不由晚Updated自动隔离，也不由早字段单证首发。5机构历史入口仍具名外部source Hold。机器一致性及diff检查通过，不是语义自签；[非作者有限记录](./V3_APR24_FINITE_INDEPENDENT.md)与日级最终记录分开，当前仅等待日级检查及其必要定点修订。未修改共享索引/LEARNING_STATE，不stage/commit/push。

日级终核已由 apr24_close 实际通过，见 [V3_APR24_INDEPENDENT_FINAL_REVIEW](./V3_APR24_INDEPENDENT_FINAL_REVIEW.md)。正式日报已同步完成/通过，终态来源及争议不用于正面证据、Books 或无遗漏断言；完成状态的校验与 scoped diff 检查通过。本日到此停止，普通可执行工作0，不新增队列、不扩大窗口。
