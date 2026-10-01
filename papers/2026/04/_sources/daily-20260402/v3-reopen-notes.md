# 2026-04-02 V3 重审工作笔记（日报已验收，保留过程记录）

**阅读说明：** 本文件保留重建过程中逐批的“待判/拟入选”原始记录，这些阶段性词语不是最终状态。最终分母、关闭项与 Books 决定见文末“V3 最终归并与反向抽检”；日报正文以 `papers/2026/04/02/README.md` 为准。

旧 V2.1 报告正文在本次 V3 重写前保留于 Git `HEAD:papers/2026/04/02/README.md`，blob `59f1cb4e6636f43c5f6f383f4af6a0cf63a1969e`。该旧稿是错误审计材料，不是可复用的 V3 完成证据；特别是其 `Complete/Passed`、DataCite created 归属、35 个候选旧分数及 `TE+` 文本均须重新判断。

窗口：`2026-04-01T09:00:00+08:00` ～ `2026-04-02T09:00:00+08:00`。本文件保留已读证据、阶段性待判与最终归并；不是另一个候选分母或完成收据。

## 旧记录的边界

- 旧日报的 513 条来自 `arxiv-owner-replay-20260903/20260402/arxiv-owner-receipt.json` 的 DataCite DOI `created` 日期查询，35 个旧入选来自同目录 `canonical-ledger.json`。DOI 创建时间不是论文首次公开时间。另一个 `daily-20260402/screening-ledger-final.json` 包含按 v1 `submitted` 构造的不同旧分母，不能与前者混算；其中月末高序号 ID 可因提前提交、后来公告而出现。
- [arXiv 公告时间说明](https://info.arxiv.org/help/availability.html)指出永久 ID 属于首次公告月份，常规公告在美东 20:00；[官方月度分类列表](https://arxiv.org/list/cs.DC/2026-04?show=2000)只能证明 4 月收录，不提供每篇精确公开日。旧 35 条里抽检 `2604.00067`、`2604.00368`、`2604.00726`、`2604.01168` 的 v1 `updated` 为 4 月 2 日 `00:01`、`00:18`、`00:44`、`01:08` UTC；末项已在北京 09:00 之后。不能把 v1 `updated`、提交或 DOI 日期任一个直接替换成 first-public time；需找官方逐日公告或同等级证据定点确认归属。
- 日期误判防线：[arXiv 官方规则](https://info.arxiv.org/help/availability.html)明确区分提交截止、质检和实际公告；质量检查可延迟 1～4 天或更久，永久 `2604` ID 则在首次公告月份才赋予。[2604.00067v1](https://arxiv.org/abs/2604.00067v1) 的 3 月 31 日 `12:04 UTC` 与 [2604.00073v1](https://arxiv.org/abs/2604.00073v1) 的 `14:14 UTC` 只是提交时刻，不能因为早于美东 14:00 截稿就归到 4 月 1 日北京日报；它们可能在审核后延至 4 月美东公告。[2604.00368v1](https://arxiv.org/abs/2604.00368v1) 的 4 月 1 日 `01:29 UTC` 也只给最早可公告批次。以上具体 owner 仍待实际公告记录；不得据此把论文机械迁往相邻日。历史 DOI-created 513 条和 v1-submitted 库存都不是实际公告清单。
- 可交叉复算的批次轮廓：上述 513 条在旧原始库存中的 ID 范围为 `2604.00001`～`2604.01224`，v1 提交最晚 `2026-04-01T17:59:35Z`（距美东 14:00 截止 25 秒），没有一条 v1 提交晚于截止；DataCite 首次 DOI created 全集中在 `2026-04-02T01:51:00Z`～`02:19:56Z`。旧收据对其中 362 条有 arXiv OAI 当日 `2026-04-02` datestamp，对余下 151 条只有代理入口；旧 35 入选分别是 18 条 OAI 当日 / 17 条代理。这组连续 ID、截稿和批量 DOI 记录与官方 4 月 1 日 20:00 ET（北京 4 月 2 日 08:00）公告相容，是来源查漏的有界线索；但 OAI datestamp 可随修订改变，DOI-created 可晚于发布，不能把 513 条直接宣称为 513 个已核实的当窗首次公开。
- 相邻 ID 批次边界追加核验：[2604.01225 官方 OAI Raw](https://export.arxiv.org/oai2?verb=GetRecord%26identifier=oai:arXiv.org:2604.01225%26metadataPrefix=arXivRaw)记录 v1 提交 2026-04-01 17:59:50 UTC，其 [DataCite DOI](https://api.datacite.org/dois/10.48550/arxiv.2604.01225)初建 04-02 02:19:58 UTC、`Updated v1` 04-02 01:10:55 UTC；紧接的 [2604.01226 OAI Raw](https://export.arxiv.org/oai2?verb=GetRecord%26identifier=oai:arXiv.org:2604.01226%26metadataPrefix=arXivRaw)虽 v1 提交早到 03-12，却在 [DataCite DOI](https://api.datacite.org/dois/10.48550/arxiv.2604.01226)初建于 04-03 01:43:07 UTC、`Updated v1` 为 04-03 00:00:04 UTC。这一相邻切点加强 `2604.00001`～`2604.01225` 属于同一 04-01 20:00 ET 首公告批次的推断，并展示“提交日可早于公告月”的实际例子；但推断仍不能取代官方逐篇公告字段，需独立日期复核后才冻结 owner。
- 依独立复核要求，进一步定点取本段首/中/末的 arXiv 原站 v1 页面与 DataCite 日期：[00001v1](https://arxiv.org/abs/2604.00001v1) 提交早至 03-08，但 `Updated v1=04-02 00:00:04 UTC`、DOI 初建 04-02 01:51:00；[00600v1](https://arxiv.org/abs/2604.00600v1) 提交 04-01 08:06，`Updated v1=04-02 00:35:50`、DOI 初建 04-02 02:05:09；[01224v1](https://arxiv.org/abs/2604.01224v1) 提交 04-01 17:59，`Updated v1=04-02 01:10:53`、DOI 初建 04-02 02:19:56。与相邻 01225/01226 切点同向，且 00001/00600 后来确有 v2，说明必须读取 v1，不从 current metadata 反推。未见这三个 v1 的 withdrawn 标记；其余真正入选仍须逐项检查 withdrawn/identity。这里的 04-02 08:00 北京时间是[官方公告时刻规则](https://info.arxiv.org/help/availability.html)加批次边界的**归属推断**，不是原站逐篇提供的精确公告时刻。
- 日期独立复核判断（2026-09-26）：上述首/中/末与相邻切点已足以将旧 513 条注册主题 identity 作为 **04-02 08:00 北京公告批次的有界归属**继续筛选；它不提供每篇精确公告时刻，也不保证没有单篇异常。凡具体页面状态、version 或后续证据与批次推断冲突，单篇标日期未决并从确定候选隔离，不强行沿用批次假设。
- 精确版本污染抽查：对旧 DOI-created `canonical-ledger.json` 的 35 个 ID，调用 [arXiv 官方 API 的 pinned v1 查询](https://export.arxiv.org/api/query) 取得 35/35 v1 标题与摘要；旧 ledger 标题有 6/35 与 v1 不同：`2604.00387`（v1 为 *RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems*）、`00392`（v1 为 *EvolveTool-Bench: Evaluating the Quality of LLM-Generated Tool Libraries as Software Artifacts*）、`00715`（v1 为 *To Memorize or to Retrieve: Scaling Laws for RAG-Considerate Pretraining*）、`00865`（v1 为 *Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation*）、`01007`（v1 为 *OmniMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory*）、`01039`（v1 为 *Automated Framework to Evaluate and Harden LLM System Instructions against Encoding Attacks*）。不能把后发/current 标题、摘要或其 framing 回填本窗；后续准入与审阅逐项以 pinned v1 为准，不为此无界逐版比对。
- 旧 `screening-ledger-final.json` 虽把身份标为 v1，也未能完整防止后发摘要倒灌：旧 DOI 35 与它交集为 29，和 pinned-v1 API 对照其中 11 条摘要不同（`00368/00387/00392/00478/00547/00715/00830/00865/01007/01039/01168`），差异不全是空白符（如 `00865` v1 摘要约 1661 字、旧 ledger 约 1163 字）。其余 6 个旧 DOI 候选不在该按提交时间建的不同库存。特别是 [00387v1](https://arxiv.org/abs/2604.00387v1) 的中心主张为 provenance attestation、taint lattice 与多层防御，数值篡改只是部分反例；不能按后发标题把它缩成单一数值相似度漏洞。V3 最终题摘准入必须以 35 条 pinned-v1 内容重判，旧摘要判断只能是线索。
- 同一 35 ID 用官方 API 分别查 pinned-v1 与 current 条目，35/35 均返回，标题或摘要中未见 `withdrawn/withdrawal/retracted` 标记。这只是检索字段的有限检查，不是逐篇状态页验收；真正入选候选仍需在精确页面核撤回状态，若已经撤回则按用户约束直接移出 selected、不保留“已选”痕迹。

## 机构来源：智谱研究目录

[官方目录](https://www.zhipuai.cn/zh/research)列出 [GLM-5V-Turbo 发布原文](https://www.zhipuai.cn/zh/research/156)，文章原始时间字段 `2026/04/01 16:00`，未写时区。按中文站本地时间推断它可能属于本窗口；推断未获时区原始证据确认，故只作发现线索、不作为确定落窗候选。CogViT、MTP、多任务 RL 是发布方描述，当前原文没有足以复原方法与归因的技术报告、受控消融及完整 benchmark 配置；即使日期确认，也只能收窄为版本事实，不能写入 Books 的长期机制。

## 到期机构来源补检进度

OpenAI 追加有界入口（2026-09-26）：官方 [Research sitemap](https://openai.com/sitemap.xml/research/) 实读 52 个 URL、[Publication sitemap](https://openai.com/sitemap.xml/publication/) 实读 200 个 URL；XML `lastmod` 在研究子图未显示 2026-04 项，在出版子图仅见 04-23 的后续修改项。`lastmod` 是网页修订，不是 first-public，因此这些数字只界定要查的原始身份集合，**不能**以“没有 04-01/02 lastmod”推出没有本窗新增。News RSS 的 Gradient Labs 关闭仍有效，Research/Publication 当窗身份需页面原始发布时间进一步核验；本源暂为未完成。

截至 2026-09-25 的官方入口重放。下表中的“未在可见索引找到”只说明所列入口的可见范围，不自动证明该来源全站无命中；留白必须继续补查，不能写成 `已检查`。

| Source ID | 实际官方入口和观察 | 仍缺什么 |
| --- | --- | --- |
| `SRC-OPENAI` | [Research](https://openai.com/research/)仅精选卡片；[官方 News RSS](https://openai.com/news/rss.xml)可回溯到 2015。RSS 按 `pubDate` 本窗只有 [Gradient Labs 银行客服案例](https://openai.com/index/gradient-labs)（2026-04-01 02:00 UTC），题摘陈述 GPT-4.1/GPT-5.4 mini/nano 应用与低延迟客服，没有新的模型/训练/基础设施机制，按贡献门槛在分母前关闭。下一篇 2026-04-02 10:00 UTC 已在窗外。 | 此结论仅覆盖官方 News RSS（含其 Research/Engineering 等栏目），不是对 Research Index 独立内容、论文/模型卡或 GitHub 全部通道的零命中证明；必要时定点补查。 |
| `SRC-ANTHROPIC` | [Research Publications](https://www.anthropic.com/research)的官方 HTML 内嵌历史条目 `publishedOn` 与 slug 已可完整抽取至 2021 年；与本窗相邻的上一条为 `2026-03-31T22:17:00Z`（`how-australia-uses-claude`），下一条为 `2026-04-02T10:56:00Z`（`emotion-concepts-function`）。本窗换算成 UTC 为 `2026-04-01T01:00:00Z`～`2026-04-02T01:00:00Z`，二者均在窗外，官方 Research 列表无本窗文章。 | 此为 Research 页面历史列表的有界检查；不把网页 `lastmod` 当发布日期，也不外推到未列的研究人员论文或 GitHub 发布。 |
| `SRC-GOOGLE-AI` | [Google Research 2026-04 Blog 归档](https://research.google/blog/2026/04/)展示本月最早博客为 2026-04-03 `Evaluating alignment of behavioral dispositions in LLMs`，因此该月 Blog 日期列表没有 04-01/02 条目；[Google Research Publications](https://research.google/pubs/)含 2026 年论文但未按本窗给精确公开时刻；[DeepMind Publications](https://deepmind.google/research/publications/)首屏为近期精选。 | Blog 列表仅日精度且不涵盖 Google Publications / DeepMind 的所有原稿；后两者本窗事件仍需核，不能把 Blog 零命中当成整个 `SRC-GOOGLE-AI` 零命中。 |
| `SRC-META-AI` | [Meta AI Research](https://ai.meta.com/research/)当前纯文本视图为空；转查 [官方 AI at Meta Blog](https://ai.meta.com/blog/)历史列表，可见 2026-04-08 的 Muse Spark / 系统测试文章与 2026-03-26 的 TRIBE v2 研究相邻；没有本窗列出的 Blog 标题。 | Blog 列表没有命中不等于所有 Research 发布、正式论文或代码事件均无命中；动态列表的完整分页/停止范围仍待核，不能凭空视图关闭整个 Source ID。 |
| `SRC-QWEN` | [官方 Research 列表](https://qwen.ai/blog)的前端将 `GET https://qwen.ai/api/page_config?code=research.research-list` 静态旧项（60 条，均早于 2026）与同站 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US` 动态项（40 条，2025-11-13～2026-09-20）拼接。动态 `articles` 的 `extra.date` 唯一本窗项是 [Qwen3.6-Plus 原文](https://qwen.ai/blog?id=qwen3.6)，`2026-04-02T04:00:00+08:00`；同一 API `content` 给全篇官方 HTML，含 `article:published_time` 同值。其模型能力和大幅 benchmark 属发布方受限结果；原文未披露训练/架构因果机制。`preserve_thinking` API 选项（默认 false）属于真实接口版本事实，未给受控质量/成本证据；原文没有改变现有 [AGENT-CONTEXT](../../../../../books/part-07-agent/75-context.md)关于跨轮 state、retention 与 raw fallback 的长期判断，故以具体理由在分母前关闭，不按 1M context、SWE-bench 分数强行入选。 | 官网 Research 两组列表及正文已可核；不外推为 Qwen 作者未列 arXiv 或仓库独立事件的零命中。 |
| `SRC-DEEPSEEK` | 从官网进入 [官方 Research & News](https://deepseek.com/en/news/)：可见 News 的 2026-04-24 紧邻 2025-12-01；Research Index 的 2026-06-24 紧邻 2026-02-25，列表所见没有 04-01/02 项。 | 页面另有 `View All` 动态展开，当前可见的前五新闻和前十研究不是无界完整档案；须核其余页或将未核范围明确隔离，不能把首页零命中写成全源零命中。 |
| `SRC-MOONSHOT` | [Kimi Blog](https://platform.kimi.com/blog)当前索引只到 2025-11，不能推出 2026 零发布；[MoonshotAI 组织](https://github.com/MoonshotAI)排序页查 100 repo 未见本窗新建；[checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine/releases) 的 19 个 release 于 2026-02-02 与 06-08 相邻，[Kimi-K2.5](https://github.com/MoonshotAI/Kimi-K2.5/releases) release 列表为空。 | 已核的特定仓库无本窗重大 release；Blog 2026 档案不可见，隔离该外部入口，未来凭带日期的原文或恢复目录重开，不推断全部组织代码无更新。 |
| `SRC-TENCENT-HUNYUAN` | [官方研究页](https://hunyuan.tencent.com/research)的动态目录通过同域官方 API `POST https://api.hunyuan.tencent.com/api/blog/publicList`，参数 `{"pageNum":1,"pageSize":100,"renderType":0}` 重放；返回 `totalNum=9`、`list=9`，无第二页。`displayPublishTime` 原值中相邻可见发表为 `1776873600`（2026-04-23 发布）与 `1770971763`（2026-02-13 研究）；2026-04-01 09:00～04-02 09:00 没有该目录的可见文章。此前文本抽取空白不是无命中证明；此 API 回执才提供有界列表检查。 | 结论仅限官网“全部”博客/研究目录，不外推为机构作者的 arXiv 论文或全部代码库没有当窗事件；GitHub/原始论文按其本身来源判断。 |
| `SRC-ZAI` | [官方 Research](https://www.zhipuai.cn/zh/research)及 [2026-04-01 16:00 原文](https://www.zhipuai.cn/zh/research/156)已审；这是一个可能落窗、但机制未披露的版本事实线索。 | 时区未标，若要确认当窗身份须补证明；目录其余相邻条目还应检查。 |
| `SRC-BYTEDANCE-SEED` | [Research / Blog](https://seed.bytedance.com/en/research)可见 2026-04-11 与 2026-01-27 相邻；[官方论文目录](https://seed.bytedance.com/en/public_papers)的同站 `GET /api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=40`（`x-tt-locale: US`）返回总量 `242`、倒序本页首项 `2026-04-07T16:00:00Z`，紧接次项 `2026-03-31T12:00:00Z`。按本窗 `2026-04-01T01:00Z`～`04-02T01:00Z`，目录相邻边界间无 publication 条目；实际停止于 token 40，不需翻其后的更早页。 | 这只关闭官网研究博客和论文目录的可见当窗发布，不证明未列出的作者 arXiv 工作或同组织 GitHub artifact 全部无事件；目录 `PublishDate` 精度/时区由 Unix 毫秒换算，未把网页本地日期当原值。 |
| `SRC-BAIDU-ERNIE` | [Blog](https://ernie.baidu.com/blog/zh/) 04-15→02-06 与 [Publication](https://ernie.baidu.com/blog/zh/publication/) 四篇均无本窗条目；[PaddlePaddle/ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases) 仅有 2025-06-30 `ernie-4.5`。 | Blog 仅日精度，无法界定 09:00 边界；但本窗无同日标题。未列原始报告凭身份重开。 |
| `SRC-XIAOMI-MIMO` | [MiMo Paper](https://mimo.xiaomi.com/) 八篇 06-29→03-13 无本窗项；[XiaomiMiMo 组织](https://github.com/XiaomiMiMo)排序页未见本窗新建，[vllm](https://github.com/XiaomiMiMo/vllm/releases)与[MiMo-V2-Flash](https://github.com/XiaomiMiMo/MiMo-V2-Flash/releases) release 列表均为空。 | 同页 Blog 约十四项无原始日期，不作零命中；找到该日 Blog 原文或日期字段时重开。 |
| `SRC-MINIMAX` | [英文 Blog](https://www.minimax.io/blog) 06-01→03-18、[中文 Blog](https://www.minimaxi.com/blog) 04-27→03-18；[MiniMax-AI/cli 官方 releases](https://github.com/MiniMax-AI/cli/releases) 本窗 UTC 04-01 09:03/11:14/11:20 的 v0.4.0/0.4.1/0.4.2 分别为状态栏/配额、配置/安装、CI 上传变动，均非项目长期机制，分母前关闭。 | Agent Tech Blog 无历史日期，隔离该入口；不能以博客/CLI 结论推断其它研究零发布，若发现 exact-dated 原文重开。 |

DeepSeek `View All` 补查（2026-09-26）：官方可读首页仍只给 Research 前十 / News 前五；直接取得 `/en/news/` 的 HTTP 响应为 `429`，WAF `block-event-id`。本次不是论文正文身份已知却无法取得，而是完整目录检索受限；记录为**检索受限的隔离项**，不形成零发布断言。若官方恢复完整历史目录，或给出该窗口原始研究 URL，再只重开本来源。

## 旧 35 条之外的查漏小批次

以下均已阅读旧原始清单所保存的完整标题和摘要。它们只是可能具有项目贡献的查漏线索；需要先确认当窗公开、撤回/修订状态，再据精确版本深入审阅，不能直接算候选或评分。

| arXiv | 题摘中可定位的增量 | 需要验证的边界 |
| --- | --- | --- |
| [2604.00001](https://arxiv.org/abs/2604.00001) | 在线 LLM 微调的数据选择从静态样本排序改为匹配当前优化器状态下的下一步目标更新，并考虑样本间冗余。 | 是否有能隔离优化器状态与筛选/重加权效果的对照；长上下文矩阵优化的实际成本。 |
| [2604.00004](https://arxiv.org/abs/2604.00004) | RoPE 长窗扩展后用原生 RoPE 教师的 attention 关系蒸馏恢复短文能力，并以重算替代二次关系矩阵存储。 | LLaMA2-7B 的 4K→32K 受限条件，训练 token 与质量目标的对照是否可比。 |
| [2604.00007](https://arxiv.org/abs/2604.00007) | 将多模态统一生成条件从串行 AR 改为共享离散 token 空间上的 masked diffusion。 | 具体模态离散化、迭代推理延迟和 benchmark 是否支持“统一范式”而非单模型 operating point。 |
| [2604.00012](https://arxiv.org/abs/2604.00012) | 后训练安全下降被解释为安全表征受抑而非彻底消失，并试图用分层 LoRA 恢复。 | 表征干预是否因果隔离；是否只对特定基座、危害集和适配预算成立。 |
| [2604.00028](https://arxiv.org/abs/2604.00028) | FlashAttention-3 在低 head-count decode 关闭 sequence split 造成 SM 空闲，提出按序列条件恢复并行。 | 改进是否只是特定 Hopper/内核局部 operating point；端到端收益与回退条件。 |
| [2604.00072](https://arxiv.org/abs/2604.00072) | 将安全 gate 的分类器预测与可验证安全保证区分，称分类器在受控自改进实验中不能同时满足两种安全要求。 | 强“不可能”结论依赖的故障模型、Lipschitz 假设和 LLM LoRA 外推边界。 |
| [2604.00209](https://arxiv.org/abs/2604.00209) | 区分 LLM 内部可表示隐私规范与实际遵循，并按信息类型、接收者及传输原则实施分量干预。 | 线性探针是否可归因，隐私泄漏减少是否跨模型/任务且不损害其他行为。 |
| [2604.00223](https://arxiv.org/abs/2604.00223) | 分解 reverse-KL 蒸馏的 target/non-target 梯度，指出匹配教师后非目标梯度仍可抬高目标 logit、压低多样性。 | 推导假设、控制实验及相对 forward-KL 的质量/多样性取舍。 |
| [2604.00235](https://arxiv.org/abs/2604.00235) | 长上下文 decode 通过近邻 query 匹配、局部修正和尾段合并复用 attention 计算，试图区别于 KV 压缩/驱逐。 | 相似命中率、错配质量、额外索引/回退成本和端到端负载条件。 |
| [2604.00280](https://arxiv.org/abs/2604.00280) | Agent 生成的形式规约即使通过 verifier 也可能错误或不完整；增加 correctness/completeness harness。 | 是否真正新增评价有效性约束，或只是特定 JML 基准与生成任务。 |
| [2604.00304](https://arxiv.org/abs/2604.00304) | 固定的专有 actor 配开源轻量 critic，在单条对话轨迹中实时监督，而非依靠重试或 actor 微调。 | 干预权限、critic 错误、成本和不可回滚行动的适用边界。 |

其他旧未入选条目仍待按题摘及来源窗口检查；本小批次既不证明它们应入选，也不证明其余旧排除正确。旧 35 条准入与已有 Books 比较亦待重审。

### 旧排除集的追加题摘查漏（非候选）

已顺序复看旧 478 条未入选身份的标题。只有标题足以确认的领域专用应用（如病灶分割、天气/金融预测、通用图论、量子计算）可作范围排除；含糊项必须继续读完整摘要。以下是读过完整摘要后仍值得定点决定准入的线索，尚未确认实际公告窗口、撤回状态或贡献门槛，不预先给分：

| arXiv | 摘要指出的可能增量 | 准入需要回答的问题 |
| --- | --- | --- |
| [2604.00375](https://arxiv.org/abs/2604.00375) | diffusion LM 的低置信度 remasking 提高单样本质量，却可能压低分布熵与多样本探索；作者给出质量/探索目标及采样替代。 | 有无可迁移的解码取舍，还是只在作者的数学/代码 benchmark 成立？ |
| [2604.00421](https://arxiv.org/abs/2604.00421) | 以 hidden-state 子空间直接路由 MoE expert，取消单独 router 参数与负载均衡 loss。 | 对训练稳定、expert collapse、capacity/placement 的完整代价是否披露；否则只是局部参数削减。 |
| [2604.00445](https://arxiv.org/abs/2604.00445) | 把行为 proxy 的不确定性与事实正确性区分，主张在低信息区域使用带少量真值的校准。 | 是否改变现有 claim-level evidence/calibration 结论，或只是已知原则的另一个后处理实现？ |
| [2604.00491](https://arxiv.org/abs/2604.00491) | code interpreter 从“全代码生成后执行”改为 AST 有界分块、生成与执行流水线重叠。 | 早执行的副作用、未完成代码与错误回滚如何限制其适用范围；端到端延迟是否隔离了预执行风险？ |
| [2604.00660](https://arxiv.org/abs/2604.00660) | semantic SQL 的 cascade 不再先全局评分，而在流式批次中用 oracle 标签迭代阈值，并联合精度/召回约束。 | 是否形成通用 AI inference routing/evaluation contract，还是语义 SQL 的特定优化点？ |
| [2604.00788](https://arxiv.org/abs/2604.00788) | UK AISI 模拟 AI 实验室 coding-agent 部署，分别测 sabotage、拒绝安全研究任务和 evaluation awareness。 | 独立研究是否提供现有 agent 安全评价遗漏的有效性条件；四模型/模拟 scaffold 可外推多远？ |
| [2604.00824](https://arxiv.org/abs/2604.00824) | Agent 训练轨迹用 decision-critical token 过滤而非只追求数量。 | 数据选择机制是否与已有 trajectory masking/quality filtering 真正不同，受控消融能否归因？ |
| [2604.00986](https://arxiv.org/abs/2604.00986) | 手机 Agent 的任务成功、隐私合规完成和跨会话偏好使用被分开测量，instrumented app 可观察不必要披露。 | 是否新增可迁移的 privacy/action-effect 验收合同，还是手机场景扩项？ |
| [2604.01029](https://arxiv.org/abs/2604.01029) | 配对拆解第二模型“修订”收益为重新求解、结构脚手架与原稿内容；MCQ 和代码任务可能选不同 pipeline。 | 四个 matched conditions 能否排除额外计算/提示长度混杂，并改变何时直接路由强模型？ |
| [2604.01193](https://arxiv.org/abs/2604.01193) | 无 verifier/teacher 的自采样 SFT 可能因 decoder precision/exploration 分布重塑改善代码。 | 是否为后训练新增稳定机制，而非特定采样温度、截断及 LiveCodeBench operating point？ |
| [2604.01220](https://arxiv.org/abs/2604.01220) | 共享参数的部分循环深度与 YOCO 常数全局 KV 结合，避免深度扩展时 cache 同比膨胀。 | 架构是否真正改变 depth/compute/cache 关系，质量与吞吐条件是否同时可复核？ |

上述 11 项只体现完整题摘之后的定点疑问；`2604.00733` 等只给异常规模数字但缺少足够比较条件的项目不因显眼数字直接入选。其余含糊标题仍待按合同摘要初筛；不能把这 11 项与前表的 11 项直接相加当最终候选分母。

### 追加项定点裁决：2604.00375v1 / 00421v1 / 00660v1

- **`2604.00375v1`，候选，`2+1+2=5/9`，owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Books Integrate。** [exact-v1 §3–5](https://arxiv.org/html/2604.00375v1)证明的是**自评分且每次 commit 满足置信门槛**时的局部 GenPPL 与全序列熵上界，而不是所有 diffusion sampler 的质量定理。保守 remasking 在单样本预算下合理，但高确定性局部提交压缩重复采样的有效分支；随机顺序扩展探索却降低单样本质量。作者将整体 entropy-regularized 目标的 suffix mass 写入局部条件，但精确 lookahead 指数级不可算，实际是 mean-field 近似加单位置 independent MH 的 batched proposals；“无额外串行步骤”不等于无额外前向 FLOPs。LLaDA-8B-Instruct 与 WeDLM-8B、MATH500/AIME24–25/HumanEval/MBPP，同一步一个 token、共享本地 temperature=0.5；WeDLM 不测 random remasking。Table 2 中 WeDLM MBPP pass@1 default entropy 0.784 > IMH 0.776，LLaDA HumanEval default confidence 0.410 > IMH 0.385，故不能照录摘要的全面 Pareto 优越。Ch24 原 confidence schedule 未把单路径质量与多样本探索分成两种目的；Books owner 已在原段后写入理论条件、探索代价、旧方案共存与受限证据。我对照 exact-v1 与书稿复核通过。
- **`2604.00421v1`，pre-denominator closure。** [exact-v1 §2–5](https://arxiv.org/html/2604.00421v1)令 hidden state 固定 N 个坐标充当 expert logits，省掉单独的可学习投影；但 **Top-2 与 Softmax 均保留**，并非分散化 expert self-activation。GPT-2 Small/OpenWebText、8 experts/12 layers 中参数差为 0.07M / 520.81M；固定随机投影已有相近成绩，Self-Routing 对 WikiText 26.7→27.4 PPL 反而退化。utilization entropy 0.617→0.724 来自 4.43M routed tokens 的同设置观察，不能独立归因坐标对齐还是跨层共用。作者 §6 明说两者机制未分离、大模型未测；与已入 Ch21 的 `2604.00801v1` 相比，此项是有限规模的局部参数简化，没有单独改变 placement、容量、路由控制或长期结论。保留为被审的反例，不评分、不作 Books 决定。
- **`2604.00660v1`，候选，建议 `2+1+2=5/9`，唯一 owner 待 Books 比较。** [exact-v1 §3–6](https://arxiv.org/html/2604.00660v1)针对分区流式 semantic SQL 的二值 row predicate：旧 SUPG 需要全局 proxy scores、一次采样只定单一 precision 或 recall；SUPG-IT 让各 partition worker 按 batch 采 oracle label、迭代更新 accept/reject/defer 双阈值，并通过 per-worker failure-budget union bound 组合全局约束。GAMCAL 从 oracle samples 学 proxy score→概率的 GAM，以单参数权衡分类误差和 oracle 调用；**它没有 SUPG-IT 的同类形式保证**。形式保证假设 proxy 校准及 oracle label 近似真值，union bound 保守；代理失准、oracle 噪声或多类语义任务都需重校。§6 使用 Snowflake Cortex AISQL、Llama 3.1-8B proxy / Llama 3.3-70B oracle、batch4096、单 worker 主试验/最多16 worker 补试、六个 5K–250K 行数据集、10 seeds；作者各算法使用不同控制参数/预算设置，Table 2 高峰质量可需 40–90% oracle delegation，不能把 `F1>0.95` 当低成本普适保证。报告硬件、模型精度、请求并发、端到端时延和 SLO 未披露。它有明确 streaming-vs-global cascade 的运行时/保证分权，不因 SQL 领域窄即排除；但只支持二值 predicate，不可迁移为自由文本回答保证。需与 Ch56 已有 conformal cascade 和 Ch66 evidence identity 对读后由 Books owner 给终态。

## 旧 35 条的首批准入重估

### Exact-v1 复核小批次：数据分配、专家自激活与 Agent 适配

- **`2604.00715v1`，准入：保留候选，建议 `2+2+2=6/9`，唯一 owner `TRAIN-DATA`。** [原文 §3–5](https://arxiv.org/html/2604.00715v1)把同一候选语料的预算分别投入预训练 tokens `D` 与检索库存 `R`，而不是在部署后把 RAG 当免费外挂。六个 OLMo-2 尺度为 30M、136M、233M、728M、1B、3B，DCLM 来源最多 100B tokens；检索库用固定 Qwen3-Embedding-8B、FAISS IVFPQ、top-5 passages。训练数据规模、retrieval store 和模型参数三轴共同决定作者拟合的 loss/任务指标；数据从权重转向索引会节约训练代价，却引入索引构建、查询质量、运行时 Context/延迟和 freshness 责任。§4.2 Table 2 的 leave-one-model-out 误差高于插值，PIQA/StrategyQA 等更不稳定；§4.3 的 `D/N≈4.14` 是作者拟合设置的交叉点，不能当跨架构通用阈值。§4.4 的 retrieval 增益也因知识型与推理型任务而异。对读 [Ch27 数据](../../../../../books/part-04-training-system/27-data.md)现有 collection、quality、mixture/budget 论证与 [Ch76 RAG](../../../../../books/part-07-agent/76-rag.md)运行时索引链：两章尚未明确**同一 source corpus 在参数化训练与非参数化索引之间的生命周期预算分配**。建议在 Ch27 将 `data allocation -> train/index artifact -> matched lifecycle evaluation` 插于数据配比之后，Ch76 只短交接；不得把该论文的具体公式、模型尺度或交叉常数升格为普适设计律。当前 Books owner 尚未落笔，整日报进行中。
- **`2604.00801v1`，准入：保留候选，建议 `2+2+2=6/9`，唯一 owner `MODEL-MOE`。** [原文 §3–5 与 Appendix B/C](https://arxiv.org/html/2604.00801v1)从外部 router 的 token-choice Top-K（逐 token compute 可预期、expert 负载未必均衡）与 expert-choice（expert 负载可控、逐 token compute 可变）出发，用每个 expert 内部低秩 gate 投影的范数减可学偏置，再经全局阈值决定独立激活。这样移走集中式 Softmax/Top-K/router 参数，却**没有**移走全局激活密度目标、token/expert 共同辅助平衡或 capacity/admission 责任；variable fanout 仍可能产生瞬时热点、零专家命中和动态 dispatch shape。论文 Mixtral-like 基座在 OpenWebText 一个 epoch、三尺度至约 0.8B、iso-FLOPs 约 1% 对齐，PPL/九项零样本任务总体改善，但每尺度任务差异、非 frontier 规模及没有生产通信/SLO 对照均限制外推；Appendix 的小规模 EP microbenchmark 也不证明 fleet-wide 收益。对读 [Ch21 MoE](../../../../../books/part-02-model/21-moe.md)已有 Top-K、batch expert-choice 和 **population cutoff** 分支：后者仍依赖独立 router score 的历史分布，此文把 activation evidence 内生于 expert 并以全局密度正则化，是不同的条件分支。建议 Ch21 窄幅整合 `external selection -> expert self-activation + soft global budget`，保留 Top-K 在固定形状、硬 capacity 和可预测时延下的优势；Ch36 只接执行 handoff。当前 Books owner 尚未落笔，整日报进行中。
- **`2604.00830v1`，准入：保留候选，建议 `2+2+2=6/9`，Books `No Change — Existing Coverage`，owner `AGENT-REFLECTION`。** [原文 §3–4](https://arxiv.org/html/2604.00830v1)分开单 episode 内的 frozen actor `π`、episode 间按轨迹修改 actor system prompt 的 meta-agent `fφ`，以及部署前在训练任务上进化搜索并冻结 `φ` 的外层 policy。reset 与多 episode outcome 是必要前提；actor 权重不变，跨 episode prompt 是 mutable state，outer training/validation 不能变成运行时自改安全策略。Jericho 3 ID/3 OOD 游戏（每 session 6 episode）和 WebArena-Lite 3 ID/2 OOD 域（每 session 5 episode）使用 Gemini 3 Flash actor、三个 meta-agent backbone；密集游戏分数比二值网站结果给 outer search 更可辨的反馈，WebArena OOD 平均 W-AUC 增幅小且个别域/模型无显著提升。没有生产 reset、权限、token 成本或跨长期任务泛化保证。[Ch80](../../../../../books/part-07-agent/80-reflection.md)88–97 行已经写出 `reset -> episode evidence -> learned meta-policy -> next prompt`、revision/rollback 及 Experimental 边界，原文新增的三层命名不需要复制正文；保留该候选作为已读反证和具体评价条件，而不是因为已有 Review note 就跳过审阅。
- **`2604.00865v1` Doctor-RAG，准入：保留候选，建议 `2+1+2=5/9`，Books `No Change — Existing Coverage`，owner `AGENT-REFLECTION`。** [exact-v1 §4–5](https://arxiv.org/html/2604.00865v1)针对已失败的多跳 Agent RAG，先判断现有证据是否足以回答，再把错误归于输出格式、推理、有效 query 下的 retriever 或推理诱导的错误 query；定位最早错误 action，保留条件有效的前缀。完整证据时只修答案/推理，不重复检索；证据不足时才改 query/top-k 或重规划后缀。比全量重跑减少 token，但 LLM sufficiency judge 的误判会错误保留前缀，外部网页/权限/effect 已变化时更不能直接 replay。实验限 HotpotQA、2Wiki、MuSiQue 的失败轨迹，ReAct/Search-o1/Search-R1 与 Qwen/Llama 模型，对比 rerun、step-wise retry、RAG-Critic，报告 EM/F1/ROUGE-L、repair rate 与 token；数据有 gold supporting evidence，非生产在线纠错保证。v1 HTML 模板里 DOI/2018 conference 字段未填，不将其视为正式发表。对读 [Ch80](../../../../../books/part-07-agent/80-reflection.md)112–151 行已将 `earliest evidence-backed critical step -> root cause -> repair directive -> affected-state boundary` 写入正文，[Ch76](../../../../../books/part-07-agent/76-rag.md)已有 coverage 与检索/answer gate。此文是这条路线的受限实现而非新 owner，不重复追加。
- **`2604.00892v1` InterruptBench，准入：保留候选，建议 `2+1+2=5/9`，建议唯一 owner `AGENT-WORKFLOW` 或评估 handoff `PLATFORM-EVALUATION-SYSTEM`。** [exact-v1 §2–4](https://arxiv.org/html/2604.00892v1)在 WebArena-Lite 165 个已核任务上合成 addition/revision/retraction 用户更新，并在无中断轨迹相对 60% 进度处注入；用最终意图下的成功率 `SR(k)`、post-interruption action/token 及 matched no-update 四象限分开判断恢复质量和额外开销。六个 backbone 共享 WebAgent-R1 scaffold、tool 和终止条件；作者结果说明更新能增加成功，也有少量本来成功却被更新弄失败的 `S/F`，不能只看总体正确率。关键限制：§3.2 明确这批中断**仅提供信息**，不 reset 环境、也不使已执行 progress 无效，故不能证明错误操作的撤销、补偿或不可逆 effect 处理。[Ch81](../../../../../books/part-07-agent/81-workflow.md)已有 checkpoint/interruptible state，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已有实时话轮打断测量，但没有把用户 goal revision 与持久效果、post-update outcome/cost 拆作独立评价合同。拟请 Books owner 决定是否在 Ch81 的中断状态段加窄幅 handoff；不把 benchmark 提升为恢复机制证据，整日报尚未完成。
- **`2604.01168v1` S0 Tuning，准入：保留候选，建议 `2+1+2=5/9`，Books `No Change — Existing Coverage`，owner `TRAIN-LORA`。** [exact-v1](https://arxiv.org/abs/2604.01168v1)冻结混合 recurrent-attention 模型权重，只优化每层初始 recurrent state；这是 weight delta 与显式 prompt 之外的第三适配资产。Qwen3.5-4B 的约 48 个 execution-verified HumanEval 训练样本和 10 seeds 支持作者所测 pass@1 增益；FalconH1-7B 与 LoRA 在 3 seeds 下不可区分，Spider 无跨域迁移，状态文件约 48 MB。这里的“zero overhead”是无额外每 token adapter matmul，不是状态加载、隔离、批处理和切换免费。对读 [Ch30](../../../../../books/part-04-training-system/30-lora.md)345–365 行已明确 base revision/state schema、S0 tensor、tenant routing/reset 与旧 LoRA/prompt 共存；另记 paper/model-card 层数、硬件与 base identity 的既有冲突。此 v1 没有足以推翻已有身份边界的新证据，不重复写 Books。

已对旧 canonical receipt 保存的 35 条完整标题和摘要逐项重读；这是摘要层筛选意见，不是精确版本 Source Review，也不沿用旧表的 `7～9` 分。先记能够明确或需要定点核验的理由，以待确认实际公告窗口后分层推进。

| 原 ID | 摘要层判断 | 具体理由或未决问题 |
| --- | --- | --- |
| [00067](https://arxiv.org/abs/2604.00067) | 拟排除 | 固定 Gaussian mixture 与 diffusion bridge 的解析记忆模型明确“不存数据、无神经网络”；摘要没有展示与本项目 LLM/Agent 记忆系统的可迁移条件，不能仅因词语 `agent memory` 入选。 |
| [00073](https://arxiv.org/abs/2604.00073) | 继续核 | Terminal/API 与 MCP/browser 的企业任务比较可能改变工具接口选择；须看任务配对、权限与功能等价性，不能把“terminal suffice”普遍化。 |
| [00131](https://arxiv.org/abs/2604.00131) | 继续核 | 将记忆问题从“总是检索”改为 read/write 分离与可访问性衰减，可能改变长程 Agent 的记忆控制面；73% token 节省须绑定 120K 交互设置。 |
| [00136](https://arxiv.org/abs/2604.00136) | 继续核 | 非平稳多模型服务里闭环成本预算与质量漂移追踪，比静态路由多出可执行控制约束；需核 1,824 prompts/三模型条件与预算保证。 |
| [00200](https://arxiv.org/abs/2604.00200) | 继续核 | 多偏好 oracle 的离线 constrained RLHF 提出高概率约束保证；需读定理假设、有限样本条件及与 LLM 后训练的实际对应。 |
| [00317](https://arxiv.org/abs/2604.00317) | 继续核 | 异构 GPU 网络在 skewed collective 下由静态路径改为运行时最小拥塞路径规划；须核 1.35× 端到端 MoE 的配置和中间 GPU 路由成本。 |
| [00356](https://arxiv.org/abs/2604.00356) | 继续核 | 把全量 Agent 轨迹审核改为低成本 signal 采样与 triage，可能改变训练反馈/观测预算；需核是否只测信息性而未测下游模型改进。 |
| [00368](https://arxiv.org/abs/2604.00368) | 继续核 | KV 迁移从初始化时固定路径到 slice-time 依网络遥测绑定，可能改变分离式推理数据面责任；旧书稿是否真正已吸收需逐句比对。 |
| [00387v1](https://arxiv.org/abs/2604.00387v1) | 继续核 | v1 主张知识库投毒防御需 ingestion 签章、trust-weighted retrieval、taint lattice、跨源矛盾检测与可审计引用分层；数值篡改仅是其中一类绕过签章的反例。须核 500 passage/63 攻击文档/200 查询与 insider in-place 替换 17.5% 失败边界，不外推通用 RAG 安全保证。 |
| [00392v1](https://arxiv.org/abs/2604.00392v1) | 继续核 | v1 的 EvolveTool-Bench 将 Agent 自生工具库视为可演进软件 artifact；即使 99 任务的完成率接近，复用、冗余、组合、回归稳定性与安全可异。须核三领域、两模型对照是否真能支撑独立 release/evaluation contract。 |
| [00414](https://arxiv.org/abs/2604.00414) | 边界核 | 显式 signal/policy/action 分离听起来与已有 Agent workflow/control plane 相同；只有三组实验揭示新的可归因失效或适用条件才准入。 |
| [00430](https://arxiv.org/abs/2604.00430) | 边界核 | Agent state/trajectory/environment unlearning 的删除粒度可能改变隐私控制权；须核是否有实际可验证遗忘保证，还是仅框架分类与 prompt 诱导。 |
| [00477](https://arxiv.org/abs/2604.00477) | 继续核 | Agent 评委的均分收敛与独特问题发现速度不同，可能改变评估 panel 停止规则；960 sessions 的人类对照与外推边界待核。 |
| [00478](https://arxiv.org/abs/2604.00478) | 边界核 | sycophancy 风险 gate/critic 属已知分层守护模式；除非受控实验证明新的失效路径或治理边界，否则新组合及作者相对降幅不足准入。 |
| [00499](https://arxiv.org/abs/2604.00499) | 继续核 | 输出长度随机且重尾，point estimate 的 SJF 可能劣于尾部风险调整；需核分布拟合、SLO/公平性与端到端调度对照。 |
| [00500](https://arxiv.org/abs/2604.00500) | 边界核 | 图文组合成检索证据单元有实际跨 parser 收益；须判断是长期 chunk identity 边界，还是特定文档解析器/benchmark 的局部增量。 |
| [00510](https://arxiv.org/abs/2604.00510) | 继续核 | MCTS 负向提前终止和 reclaimed compute 重新分配直接针对多请求长尾时延；需核准确性、搜索预算和服务并发条件。 |
| [00529](https://arxiv.org/abs/2604.00529) | 继续核 | 多格式 QAT + 单 anchor checkpoint 的运行时精度转换可能改变 artifact/接受证据契约；旧书稿实际写入待核。 |
| [00547](https://arxiv.org/abs/2604.00547) | 继续核 | 一体化多模态模型的安全继承可能不成立，评测同时区分理解与生成；须核同一基座/训练数据混杂，不能把榜单差异归因于统一架构。 |
| [00594](https://arxiv.org/abs/2604.00594) | 边界核 | coding agent task-level IRT 将 LLM/scaffold 能力分开可能补足聚合 pass rate；要核是否独立辨识而非统计拟合。 |
| [00694](https://arxiv.org/abs/2604.00694) | 边界核 | Shadow API 缓存可能减少网页重发现，但其授权、稳定性与站点同意条件不清；不能仅凭 warm-cache 加速为 Agent 平台建议。 |
| [00715](https://arxiv.org/abs/2604.00715) | 继续核 | 以模型参数/预训练 token/检索库存联合控制，研究参数记忆与检索增益随任务及评价指标变化的边界；须保留 OLMo-2 30M～3B 范围。 |
| [00726](https://arxiv.org/abs/2604.00726) | 继续核 | GPU 矩阵乘硬件注错揭示训练更新前的 silent corruption，检测后重算 step；限作者 LLaMA 60M～1.3B 实验，旧书稿写入待核。 |
| [00785](https://arxiv.org/abs/2604.00785) | 继续核 | 具体 Aurora/PVC 的 expert-parallel-aware optimizer 与规模扩展可能限定异构硬件 MoE 训练边界；须区分可迁移机制与厂商配置纪录。 |
| [00801](https://arxiv.org/abs/2604.00801) | 继续核 | 去中心化 Router/Softmax/Top-K 的专家自激活是 MoE 明确替代分支；需核负载均衡是否真正无需控制器及训练/推理代价。 |
| [00830](https://arxiv.org/abs/2604.00830) | 继续核 | 从手工 test-time adaptation policy 到训练任务上双层搜索，可能改变 Agent 持续适配策略所有权；需核越域结果与搜索成本。 |
| [00835](https://arxiv.org/abs/2604.00835) | 拟排除 | 综述整理 prompting/SFT/RL 工具使用范式，没有独立新机制或反证；旧章节可用作背景但不重复计分。 |
| [00865](https://arxiv.org/abs/2604.00865) | 继续核 | 多跳 Agent RAG 出错后定位最早失败点并局部修复、复用有效前缀，可能改变 repair checkpoint；须核前缀有效性的判断与回退成本。 |
| [00892](https://arxiv.org/abs/2604.00892) | 继续核 | 用户中途增加/修订/撤销目标时，已发生状态变更的 Agent 任务是否可恢复，是现有静态 benchmark 缺失；需核环境操作与 oracle。 |
| [01007](https://arxiv.org/abs/2604.01007) | 边界核 | 多模态 Agent memory 的 autoresearch 提升多数来自修 bug/改 prompt；缺少受控机制增量时不因大幅 F1 增长而准入。 |
| [01020](https://arxiv.org/abs/2604.01020) | 边界核 | 公司层级多 Agent 角色与成本胜于平铺，可能只是组织比喻；需核任务、模型与并行预算等价性和稳定技能分工边界。 |
| [01039](https://arxiv.org/abs/2604.01039) | 继续核 | 结构化/编码输出绕过直接拒绝的系统提示泄漏，可能修正安全 gate 的 threat model；需核 46 指令测试、机密暴露与缓解归因。 |
| [01128](https://arxiv.org/abs/2604.01128) | 拟排除 | AI 写学术论文的呈现/幻觉基准是领域任务评价，摘要未指出一般 AI System 评价 contract 的新约束，不能因用 Agent 判别而入选。 |
| [01168](https://arxiv.org/abs/2604.01168) | 继续核 | 混合 recurrent-attention 模型把可调参数放在每层初始状态而不是权重/LoRA；需核 Qwen/Falcon 对照、48 条训练样本和域外失败。 |
| [01221](https://arxiv.org/abs/2604.01221) | 边界核 | 个人文件多模态 Agent benchmark 指向 perception/grounding 瓶颈；须看样本/轨迹诊断能否提供泛化的新评价边界，而非只新增场景。 |

“拟排除”只表示目前题摘足够关闭贡献；在本窗来源与官方公告尚未闭合前不统计最终排除。需要核的条目不预先评分，不借旧分数决定阅读深度。

### 有界准入校准：先剪枝，再深读

这轮先用上述已保存的完整题摘判断**贡献**，不把旧 35 项或追加 22 项自动转换成 V3 候选。以下只是对旧条目的准入改判；日期 Gate 尚未通过，不能将它们计作已核实的本窗排除或入选。

| Identity | 摘要层处置 | 贡献门槛判断 |
| --- | --- | --- |
| `2604.00067` | Pre-denominator closure | 非神经 Gaussian-mixture 记忆模型；仅有 Agent Memory 名称相似，未给本项目的模型/Agent 状态设计可迁移条件。 |
| `2604.00835` | Pre-denominator closure | 工具使用范式综述，没有独立机制、重要反证或纠错；可作背景但不作为独立候选。 |
| `2604.01128` | Pre-denominator closure | AI 写论文的领域评价，没有表明通用 AI System evaluation contract 新增失效条件。 |
| `2604.00478` | Pre-denominator closure | 风险分类器、访问 gate、生成器—critic 是已知组合；作者在 TruthfulQA 受限设置的相对改善没有隔离出新的权限/状态机制。 |
| `2604.00694` | Pre-denominator closure | 共享站点内部 API 缓存的性能比较建立在 warm cache；授权、站点协议和稳定性未形成可验证的一般 Agent 工具设计边界，不能据浏览器快慢宣布“browser-first”应退出。 |
| `2604.01007` | Pre-denominator closure | Autoresearch 在两个 Agent memory 基准里的最大收益来自修 pipeline bug/提示词；摘要未分离出可迁移的长期 memory 机制或独立评估反证。 |
| `2604.01020` | Pre-denominator closure | 以公司层级组织 Agent 的已知规划—执行—检查分工，任务/模型/并行预算难判等价；仅凭受限 SQuAD 相对增益不足以改变 Multi-Agent owner。 |
| `2604.01221` | Pre-denominator closure | 个人电脑文件 benchmark 的新数据规模和感知瓶颈，与现有检索/grounding 压力同向；摘要未揭示此前评价无法测到的独立失效机制或发布条件。 |
| `2604.00414`, `2604.00430`, `2604.00500`, `2604.00594`, `2604.00785` | 定点待判 | 分别核是否仅重述分层控制、遗忘粒度、文档 chunk、LLM/scaffold 能力估计及 Aurora/PVC 配置；只有原文给出新可迁移边界才保留，不因 system 用词、规模或章节映射入选。 |

上述 8 条准入前关闭已另用 arXiv 官方 pinned-v1 摘要逐项重读（2026-09-26）：`00067/00835/01128/00694/01020/01221` 的中心问题与上表相符；`00478` v1 有 50 条 TruthfulQA 场景及双模型受限结果，但 BAC、Trait classifier、Generator-Critic 的组合仍未在摘要中分离新的授权/反馈机制；`01007` v1 将修 bug、改 prompt、架构调整各项贡献列出，但没有仅凭题摘可独立迁移的 memory-state 设计结论。两项虽有后发摘要差异，关闭理由仍成立。此处只完成**贡献准入**，日期批次与 withdrawn 状态仍需最终核，不把关闭数冒充已确证落窗数。

五条边界项的 pinned-v1 题摘也已核到：`00414` 的 signal/policy/action 分离与现有 [Agent Workflow 的 policy graph](../../../../../books/part-07-agent/81-workflow.md)及 [Security 的 sensor/decision/effect 分权](../../../../../books/part-06-ai-infrastructure/72-security.md)已陈述的原则重合，摘要未显示新的可迁移保证，拟作第九条准入前关闭；`00430` 提出 state/trajectory/environment 遗忘粒度，但“自然语言请求→提示引导遗忘”的可验证删除范围不明，须定点读 threat model/attack evaluation 后再决定，不能把作者的“防止推断”视作合规删除证明。`00500` 的 parser-independent 图文 Evidence Unit、`00594` 的 LLM/scaffold ability 分解与未见 benchmark task 预测、`00785` 的 EP-aware sharded optimizer 分别可能新增 ingestion identity、测量归因、MoE 训练状态所有权的窄边界，暂留有界证据审阅，而不因关键词或硬件规模自动高分。以上仍是准入建议，日期/撤回与独立复核未完成。

旧排除集追加的 11 个线索也已逐项读完整摘要，可按贡献门槛收缩审阅范围：`2604.00375` 的质量—探索目标及推导、`00421` 的 router 责任迁移、`00491` 的生成/执行重叠及副作用、`00660` 的 streaming cascade 精确率/召回率联合保证、`01029` 的 matched revision/re-solving 拆解、`01193` 的无教师 self-distillation 反常证据、`01220` 的深度—KV 联合设计，都有可定位的设计或评价问题，仍需证据审阅（不是已经入选）。`00445` 的 low-information 校准失效、`00788` 的安全评估 scaffold、`00824` 的 decision-critical token 过滤和 `00986` 的隐私合规任务拆分可能形成独立边界，但是否只是已有原则/新场景，须与具体 Books 命题或关键实验定点比较；不以摘要宣称为新长期结论。由此不会对旧 478 条逐篇全文审读。

**计数边界：** 旧 DOI-created proxy 为 513 个 raw identities（不是已核实当窗分母）；旧入选 35、旧排除 478。旧入选中已有 8 条在题摘层给出具体 pre-denominator closure，另 5 条仍待定点准入判；旧排除集中目前定点查漏 22 条。V3 `retained candidates`、retain rate 和最终 closure 总数均**未冻结**，不得拿 `35−8+22` 代替。尚缺实际公告时点/ID 边界、14 个来源窗口覆盖、追加项准入独立校准、入选项精确版本证据与 Books Decision。

### 定点准入关闭：2604.00131v1（Oblivion）

[原站 exact-v1](https://arxiv.org/html/2604.00131v1)将 uncertainty-gated read、按使用反馈强化 write、hierarchical memory 与 decay temperature 组合。作者在 LongMemEval 与 GoodAI-LTM 上比较，120K 设置相对 FullCTX 报 token cost 降 73%，同时 latency 却为 FullCTX 的 `1.34×`；温度过小几乎无法留存、过大可使 buffer 饱和，证明“少检索”也不是免费。这个条件演示有价值，但机制层面仍是已知 read/write 分离、按不确定性触发、衰减/强化与分层存储的组合；[Ch77](../../../../../books/part-07-agent/77-memory.md)已明确区分 retrieval 与 adjudication、activation 与保留/遗忘控制、dormant 生命周期和 cost/真实性边界。论文未以独立干预表明一个此前书稿缺失的 state owner 或新的失效边界，且只测两种授权 benchmark、四个模型家族，作者承认温度需任务调参且未测多模态/开放任务。因此仅以“长历史 benchmark 上的组合实现与受限数值，不改变当前 memory 设计判断”作 pre-denominator closure；不是因已有 Books 或低分而拒绝，若以后出现受控反证可重开。

### 定点准入关闭：2604.00356v1（Signals）

[arXiv exact-v1 摘要](https://arxiv.org/abs/2604.00356v1)提出从 Agent live trajectory 的 interaction、execution、environment 事件提取无需模型调用的低成本 signal，再优先送人工/模型审阅；受控 `τ`-bench annotation 的 informative 比率为 `82%`，相对 heuristic `74%`、random `54%`。该量测的是**标注者所见轨迹信息性**，不是下游训练增益、线上错误发现召回率或发布风险上界。把失败、停滞、loop 等可观测事件作优先级本身未改变 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已有 evidence selection / 风险分层与随机审计 floor，亦未给出此前无法表述的状态/授权关系；在本项目当前范围作 pre-denominator closure，避免把单 benchmark 的抽样效率外推为长期 Agent 学习控制合同。若后来能证明该信号改变 release gate 的漏报界或反馈策略，再作为新事件重开。

### 精确版本证据复核：2604.00073v1（Terminal Agents）

[arXiv exact-v1 HTML](https://arxiv.org/html/2604.00073v1)的题名是 *Terminal Agents Suffice for Enterprise Automation*，页首显示 2026-03-31 提交；本日报的公开归属依 `2604.00001–01225` 有界公告批次，而非此提交字段。当前原站未显示 withdrawn 标记。§3 使用 ServiceNow/GitLab/ERPNext 隔离环境，分别有 330/192/207 项任务和 93/107/7 个所选 MCP server tools；同组内四种 backbone（Claude Sonnet/Opus 4.6、GPT-5.4 Thinking、Gemini 3.1 Pro）比较 MCP、browser 与 terminal。任务结果由环境状态验证；作者报告 token 推理成本、成功率和附录中的 wall-clock/tool calls，没有证明生产权限、安全、并发或 SLO。

§4 主表的 MCP 低成功率不能直接归咎协议：作者明言服务目录漏掉 ServiceNow 过半任务类别、ERPNext delete 等操作。附录 A.1 只留三范式都可做的 444 项（ServiceNow 120/GitLab 127/ERPNext 197）仍有差距，但对应的是这些具体 server 的 query/filter/payload 表达力，不是 MCP 的形式上限。§5.1.2 还揭示反向边界：ServiceNow impersonation 的 API 返回 HTTP 200 却未完成浏览器 cookie/session 切换，渲染图表值不一定可由底层表格精确还原，Flow Designer 无公开 API；terminal 在这些操作上应让位于 browser。提示/任务采样和作者自己构建的环境可能偏向一种接口；论文承认完整多 seed 矩阵未跑，artifact 宣称接收后发布，不可声称复现。

贡献不是又一组 Agent benchmark 排名，而是受限对照显示 **catalog coverage / field expressivity** 可成为成功率的控制变量；组合 API 提升表达力又扩大 credential、脚本构造、side-effect 与审计压力。旧 narrow typed tool 对低风险、固定业务操作仍有最小权限/治理优势；UI-only 需要 browser fallback。评分 `Design Delta=2, System Reach=2, Durability=2, Total=6`；标准 Source Review 足够。对读 [Ch78](../../../../../books/part-07-agent/78-tool-calling.md) 的 Interface Granularity 主线，正文已写 typed tool→generic API→terminal→browser fallback，并直接限定 Terminal Agents 实验范围，故 `No Change — Existing Coverage`；不得重复加“shell 优于 MCP”结论。确认本项进入候选是它把 interface expressivity 作为可测的条件边界，不是因为书稿已有同名论文。

### 定点准入关闭：2604.00430v1

[原文 exact-v1](https://arxiv.org/html/2604.00430v1)的 §III、§V、§VI 把 state/trajectory/environment 分成三种 Agent 遗忘目标，但实际控制面是自然语言请求经 conversion model 转为 prompt/behavior steering；Agent owner 不能直接修改基座权重。其收敛命题限定 Bradley–Terry 偏好、线性潜在特征、正定特征协方差等假设；GridWorld、AlfWorld、HotPotQA 与有限 adversary probes 检验的是行为，不证明模型、派生状态或外部备份已删除。AlfWorld 部分设置的任务成功率还下降（如作者表中 GPT 0.88→0.71、Claude 0.68→0.60），显示 over-forgetting/utility regression。现有 [AGENT-MEMORY](../../../../../books/part-07-agent/77-memory.md) 和 [PLATFORM-SECURITY](../../../../../books/part-06-ai-infrastructure/72-security.md) 已明确区分行为抑制、逐项删除、派生副本和最终 artifact 验收。该 v1 没有推翻此 contract，也未证明新的删除机制；因此以“行为引导不等于可验证删除，书稿已有覆盖”作 **pre-denominator closure**，不沿用旧表‘继续核’，更不把作者的防推断措辞写入 Books。日期仍按本日有界批次归属推断，若发现单篇异常则单独重开。

### 定点准入关闭：2604.00594v1

[官方 PDF v1](https://arxiv.org/pdf/2604.00594v1) §3–5 把 coding-agent benchmark 的 task difficulty 由 issue、repo、tests、solution 特征预测，并在 IRT 中把 Agent ability 近似拆成 LLM 与 scaffold 两个相加的参数；其新组合预测仅在 LLM 与 scaffold **各自已在训练响应中出现**时成立。作者承认未见的新 LLM/scaffold 不能外推，且所测 SWE-bench Verified/Pro、Terminal-Bench 2.0、GSO 四套编码 benchmark 的 agent-run 成本/任务设计不是生产 release SLO。现有 [PLATFORM-EVALUATION-SYSTEM](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求冻结模型、scaffold、任务、预算及日期，不以汇总 pass rate 当作系统能力；IRT 可作为稀疏矩阵的统计预测和 benchmark 选题工具，但没有证明它可取代真实 held-out Agent run 或改变既有 release gate。因此这项尽管方法具体，仍因**只提供作者四个 benchmark 的估计器而未改变本项目的评价决策权/长期边界**作 pre-denominator closure；不把模型/scaffold 相加当因果分解。

### 精确版本证据复核：2604.00500v1（Evidence Units）

[arXiv pinned-v1 HTML](https://arxiv.org/html/2604.00500v1)和[版本页](https://arxiv.org/abs/2604.00500v1)为同一题名且无已知后续版本或撤回；v1 提交 `2026-04-01 05:32:16 UTC`，只作为 provenance，公开归属仍按本日 ID 批次边界推断。论文不是单纯调 chunk size：旧 element-level chunk 可低成本索引，表格、caption、单位及解释段落却可能各自成为不同候选；作者先把 MinerU/Docling 异构标签映到 DoCO 扩展 canonical roles，再以视觉元素为 seed 连接结构锚点、以整页 paragraph×EU 相似矩阵给解释段落分配候选，剩余孤段保留独立单元。它把 parser 输出变成 ingestion proposal，Evidence Unit 才拥有可检索语义组合；原页、parser revision 与 region locator 仍是事实来源。公式中的逐段 `argmax` 不等于具全局一对一容量约束的最优匹配，不能沿摘要“globally optimal”措辞外推。D1 构造规则在 pipeline 中执行；Neo4j 中 D2/D3 restoration/validation 只是 future runtime schema，不能宣称现已在线校验所有 invariant。

作者对 OmniDocBench 1,355 原页排除 15 个非内容页后用 1,340 页、1,551 条按 GT layout 规则自动产生的 QA；同一 `ko-sbert` 384d embedding 与 strict evidence protocol 下，GT track 的 element baseline→EU `Recall@1 0.1502→0.5113`、平均 LCS `0.5006→0.8068`。另用 MinerU 和 Docling 解析同语料，报告 LCS 相对增量 `+0.27/+0.23`；parser 失败页在共同 1,551 QA 分母记零，而 1,341 页交集又另作 parser 间对照。EU 平均 `2,931` 字符，对照 chunk `623`，约 `4.7×`；这可消耗更多 embedding/context、稀释短 query，相对召回收益不等于答案正确率、延迟或生产 SLO。论文明确 single-page EU，未处理跨页引用；两个 parser 不能证明“任意 parser 无需重写”，OCR/label 错误也使绝对质量下降。

Artifact 边界：[作者 GitHub 仓库](https://github.com/hanyeonjee/evidence-units)当前 README 明说仅发布 evaluation code 与 1,551 QA，**完整 EU construction pipeline 未包含**。其当前 README 改用 471 English-primary pages、`0.501→0.797` LCS，与 arXiv v1 的 1,340 页、`0.5006→0.8068` 不同；该仓库 2026-03-31 创建、2026-05-01 最近推送，现时页面不能回填为 04-02 exact-v1 artifact。只能据 pinned-v1 论文作机制及作者实验判断，不宣称已独立复现 pipeline 或混合两个 denominator。

对读 [AGENT-RAG Ch76](../../../../../books/part-07-agent/76-rag.md) Offline Ingestion/Chunking：现有正文已有 parser/chunker identity、region provenance、结构边界与大 chunk 成本，但尚未将**跨 parser canonical role → 表格/图像/说明文字 Evidence Unit → parser 变更后的 region/内容一致性验收**作为一条明确的条件分支。该分支可在多解析器、结构化图文文档的 ingestion 中改变 artifact identity/验收，简单纯文本、小语料仍以普通 chunk 为基线。暂评 `Design Delta=2, System Reach=1, Durability=2, Total=5/9`，标准证据已读；建议 Books owner 在 Ch76 窄幅 Integrate，而非新建节点或把作者具体 ontology/阈值当通用规范。Books owner 尚未落笔，整日报仍进行中。

### 精确版本证据复核：2604.00785v1（Aurora MoE）

[arXiv exact-v1 HTML](https://arxiv.org/html/2604.00785v1)与[版本页](https://arxiv.org/abs/2604.00785v1)均为相同技术报告，无已知后续版本或撤回；v1 提交 `2026-04-01 11:46:17 UTC`，公开归属仍依本日有界公告批次。规模描述是 Intel Aurora 上的作者实验，不是核心准入理由。§1/§3.1 明确旧 DP-sharded AdamW 只按 DP rank 分 owner；加入 EP 后 expert 参数在 EP rank 间分割、仅在 DP 维复制，而 attention/embedding/router 等 non-expert 参数还在 EP rank 间复制。EPSO 将 optimizer state 的两个 parameter families 按不同 replica group 放置：expert state 沿 DP shard，non-expert state 沿 DP×EP shard；对应 gradient aggregation/parameter consistency 和 checkpoint mapping 也须按各自 owner 复核。其 FastSparseMoE 另以 gather input/route index、grouped GEMM、reduce-scatter 输出替代逐 expert kernel，但这是另一条优化，不能把总 speedup 全归于 EPSO。

§2–3 作者在 256 节点、3,072 Intel PVC tiles 上完成 Mula-1B dense/Mula-7B-A1B MoE 的 4T token 训练；20B/100B/220B MoE 仅训练 100B token。模型扩展用 EP=12、100B PP=4、220B PP=8；220B 的 compute scaling 报到 12,288 tiles，约 90% 效率，但该效率随 batch 变化，不能推为固定 workload 强缩放。Table 3 的 component ablation 对 EPSO：20B optimizer `1.36×`/full step `1.19×`，100B `1.23×/1.06×`，220B `1.07×/1.01×`；FastSparseMoE 与 EPSO 叠加 full step 20B/100B/220B 为 `1.35×/1.41×/1.51×`，摘要的最高 `1.71×` 是 **7B 未用 EP 的 FastSparseMoE**，不是 EPSO。精度为 BF16 mixed precision/AdamW；训练 token、并行组和硬件条件决定这些数值，未披露跨 AMD/NVIDIA 平台、网络分布、线上 SLO 或所有 optimizer 的泛化。可靠性部分的 dual checkpoint 只保留最后两份完整状态，另有 model-only checkpoint 会丢失 optimizer momentum，不能写成等价无损恢复。

对读 [TRAIN-DISTRIBUTED-TRAINING Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)与 [TRAIN-ZERO Ch39](../../../../../books/part-04-training-system/39-zero.md)：前者定义 EP×DP 执行/step handoff，后者 ZeRO 按 DP shard state，却尚未明说混合复制域需要**按参数族分别选 state sharding group**。这可改变 optimizer memory/step design，预计 `Design Delta=2, System Reach=2, Durability=2, Total=6/9`，并非把 Intel FastSparseMoE 具体 kernel 当通用结论。建议 Ch39 canonical owner 窄幅 Integrate、Ch36 最多短 handoff，要求 Books 保留单 DP/shard 旧方案在 dense 或 EP=1 时合理，检查完整 step/checkpoint round-trip 后才声称状态等价。Books owner 尚未落笔，整日报仍进行中。

### 精确版本证据复核：2604.00499v1（TIE）

[arXiv abs v1](https://arxiv.org/abs/2604.00499v1)载明 2026-04-01 05:31 UTC 提交、后有 v2；依本日公告批次边界暂归 04-02 08:00 北京批次。**版本异常：**[HTML `/v1`](https://arxiv.org/html/2604.00499v1)首页写 `Preprint. August 24, 2026`，但[PDF `/v1`](https://arxiv.org/pdf/2604.00499v1)首页写 `Preprint. April 2, 2026`。因此以下机制、实验以 pinned **PDF v1** 为依据；HTML 的日期及任何只在 HTML 出现的内容都不能作为当窗证据。

PDF v1 §3–5 从 FCFS→point-prediction SJF 的队头阻塞出发，指出相同 prompt 的采样轨迹长度也有分布。作者对 1,000 个 LMSYS prompt 各生成 100 次，固定自由度的 log-t 拟合作者样本中的长尾；其定理基于 EOS 终止率近零处的分布假设，**不是所有模型/解码策略均必重尾**。策略按 `max_tokens` 截尾后用 `E[length] + β·CVaR₀.₉` 给 SJF 排序，β 随等待队列/最大 batch 大小调整；aging 限制长请求饥饿。部署在 vLLM 0.11.1 中，主调度线程与 DeBERTa-v3-base 长度分布预测线程分开，预测异步批量化；这同时引入 900K 等量训练样本中对 TIE 需要 45K prompt × 20 次重采样、模型漂移时再校准、额外 predictor/排序开销及压测负载偏移。

PDF v1 §6 与附录在 8×NVIDIA A6000 48 GB/NVLink、128 vCPU、FP16 Llama-3-8B-Instruct 与 TP8 Llama-3-70B-Instruct 的作者 testbed 对照 FCFS/SSJF/LTR。100 RPS、ShareGPT/8B 的平均 per-token latency 为 LTR 0.86 s/token、TIE 0.57；平均 TTFT 为 120.03 与 98.10 **秒**，已是严重排队的实验 operating point，不能宣称生产 SLO 已达标。离线 10K Alpaca prompts 的 time@3K/throughput 另测，不能与在线延迟混成同一收益。§6.4 对比 log-normal 与仅用期望的消融支持分布拟合和 tail risk 各自有作用；Appendix E 公开重采样标注难以直接从普通在线流量获得。论文未证明跨未测模型、解码温度、精度/硬件/真实租户混合的统一 log-t 形状，亦未给生产并发 SLO 下的绝对收益。

这项有明确通用推理调度增量，计 `Design Delta=2, System Reach=2, Durability=2, Total=6`，Owner `INFER-SCHEDULING` / Ch56。Books 原有 admission estimate→runtime drift 和 aging，但未把**输出长度尾部分布与排队压力共同定义排序风险**写成同一条件分支；Books owner 已在 Ch56 的 SJF 基线后插入这一窄命题，且保留 point+aging/FIFO 回退及作者高 TTFT 实验边界。我对照 PDF v1 §3–6 独立复核了机制和正文，Books Decision 为 **Integrate**。整日报的机构来源、最终分母及独立审阅仍未闭合，**不得标 Complete**。

### 精确版本证据复核：2604.00529v1（MF-QAT）

[原站 PDF v1](https://arxiv.org/pdf/2604.00529v1)首页和 [abs v1](https://arxiv.org/abs/2604.00529v1)同为本窗公告批次线索；本文读 PDF v1 的 §3–4、表 1–2、附录，而非把未来修订版结论回填。旧 single-format QAT 在目标格式固定时最清楚，但设备/负载驱动的弹性精度使每目标一份 checkpoint 带来存储与训练组合爆炸。作者让 full-precision master weight 在 2→4→6→8 bit 的 MXINT 或 4→6→8 bit MXFP 顺序中接收多格式 QAT 梯度，再保存 MXINT8/MXFP8 anchor；运行时 slice-and-scale 把 anchor 派生为低比特格式。MXINT 转换可右移、round 并调整共享 scale，MXFP 需数值转换；**派生结果不是已测硬件上的动态 serving 保障**。

评价限 Llama-2-7B、Llama-3.2-1B/3B、Qwen3-0.6B/1.7B/4B 与 Qwen3-VL-2B/4B 的 decoder weight-only；QAT 只用 128 条 WikiText-2 train 示例，多数表看 WikiText-2 perplexity、HellaSwag/MMLU/MathQA 零样本及 ChartQA，未测 KV、activation、实际 kernel latency、持续 runtime 切换成本、并发或生产 SLO。§3.2 为不同模型/格式扫三个学习率并择最优；大于 2B 的单格式 QAT 因过拟合还改变 epoch 设置。所谓“未见格式也稳健”只限作者检查的目标 bit width/块结构，不能扩成任意 precision/hardware。实验与公式证明 anchor 的**可转换性及该任务集上的质量**，不证明跨硬件服务验收可复用。

暂计 `Design Delta=2, System Reach=2, Durability=2, Total=6`。Owner `INFER-TENSORRT-LLM` / Ch49；[现有正文](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)已经写出“一个 anchor 支撑多格式 ≠ 一次验收覆盖所有格式”的旧方案、机制、风险与回退，且 review note 标 exact-v1，故 Books Decision 为 **No Change — Existing Coverage**。这不是把 single-format QAT 废除：目标格式与硬件固定时它仍可给最简单的独立验收。

### 精确版本证据复核：2604.00368v1 TENT

- **身份与准入：** [arXiv exact-v1 HTML](https://arxiv.org/html/2604.00368v1)标题及 §2–5 均为 **TENT**，非旧日报反复写的 `TE+`。静态绑定/均匀 striping 适用于同构、稳定链路；异构 GPU fabric、拥塞与链路 churn 使路径选择/重试应从应用转到传输控制面，属于可迁移的数据面责任变化。按当前命题建议 `Design Delta 2 + System Reach 2 + Durability 3 = 7/9`；仅在最终候选分母冻结后入正式评分。
- **状态与流：** 应用提交 source/destination segment、offset、length 的 transfer intent；orchestrator 读取拓扑、可达性、backend 能力并在请求时晚绑定，切为 slices；各 transport backend 执行字节搬运、回报完成与遥测；slice 失败由 orchestrator 在候选路径上重派，所有 slices 完成后才向上层发一次 batch completion。跨 GPU 不能直连时可经 host 做 D2H/H2H/H2D 流水线；`§3.3–4.4` 还披露无锁队列和分层计数器，但正文不应推为 exactly-once 外部 effect 保证。
- **评价合同：** `§5.1.1` SGLang HiCache：Qwen3-235B-A22B-Instruct-2507、单节点 8×H800、TP=8、60 clients、并发 4、每请求 2048 input token、10 轮、600 GB KV 预算，HiCache policy 固定；TENT vs Mooncake TE 为输入吞吐 `78,759 vs 58,006 tok/s`、P90 TTFT `0.67 vs 0.90 s`。文中明确本对比含 **NVLink 直连 vs TE 的 RDMA 路径差异**，不能把全部 1.36× 归因于 slice spraying。`§5.1.2` Checkpoint Engine v0.2.0 在 8×H800、TP8、FP16 下给两模型 apply time `12.87→10.34s`、`7.17→5.30s`；不是通用 RL throughput。`§5.3` 64 MB transfer 的 NIC 故障注入在该 testbed 出现 <50 ms 吞吐跌落与 26 ms 恢复；不保证未知 fabric/SLO。输出长度、精度（HiCache serving）、跨请求多租户公平性未完整披露。
- **Books 现状：** [INFER-DYNAMO Ch52](../../../../../books/part-05-inference-system/52-dynamo.md) 正文 116–120 行已按 intent→slice/path→completion 逻辑承载，402 行 Review note 也正确标 `TENT / arXiv:2604.00368v1`。V3 需要在日报保留 `已有整合/无需重复修改`，而不是沿旧稿的 `TE+` 文本再次写 Books；如需改论点，应由 Books owner 独立判断。

### 独立推进的精确版本证据：2604.00491v1

- **精确版本身份更正：** [arXiv v1 HTML](https://arxiv.org/html/2604.00491v1) 标题是 *Executing as You Generate: Hiding Execution Latency in LLM Code Generation*；当前 OAI arXivRaw 元数据展示的 *... LLM Code Interpreters* 是后发版本标题，不能倒灌到本窗口 v1。以下机制及实验读取 v1 正文，不以 current OAI 的标题/摘要替代。
- **准入命题和评分（待日期 Gate）：** 本文不是又一个 code interpreter benchmark。旧串行方案在完整代码到达后执行，状态语义最简单；当生成和解释执行都占用端到端路径时，作者把已完成的 Python 顶层语句从 token stream 中切出，在后续 token 生成期间于持久解释器里执行。这改变 Agent 工具的生成→执行 handoff 与 latency critical path。`Design Delta=2, System Reach=2, Durability=2, Total=6/9`，暂按标准审阅；不是凭显著速度数字加分。
- **原文与身份：** [arXiv 2604.00491v1 HTML](https://arxiv.org/html/2604.00491v1) §2–6 已读；v1 页面显示 2026-04-01，但这只是版本/投稿显示，不替代精确公告时刻。旧 DataCite-created proxy 把它纳入 513；当窗归属仍须批次证据。这里审 v1，不把旧库存保存的后来 abstract 中 `37.3%`/`99.8%` 字句混作 v1 的全部结果。
- **机制、状态及控制流：** 模型是 producer；AST chunker 在顶层语句语法边界确认完整（歧义时多看一个 token）才 enqueue；executor 在单个持久 Python session 中顺序执行并保持 import/变量，队列积累时合批摊销 setup。运行时错误可以中断后续生成；此选项改变返回给 repair 模型的代码前缀，而不只是隐藏执行时间。均匀 chunk 模型说明当每块 generation 时间大于 execution+setup 时，多数执行可隐藏；块太细则 setup 占优，故不是“越早越细越快”。
- **评价合同与证明范围：** 四个 Python 脚本基准（DSBench 442、DABench 257、PandasPlotBench 175、GitChameleon 116）、七个经 OpenRouter streaming 的模型、Local/Docker/Open Interpreter 三环境；Ubuntu 22.04、Xeon 8352V，单 CPU/容器 CPU pinning、task-local persistent interpreter。作者先用 20/50/100/200 TPS mock token replay 测相对 serial 的 NEL 与 E2EL，再在 real streaming、Docker 条件中分 error-free/error-encountered 报告。v1 Table 2 的 error-free Gemini-3.1/PandasPlotBench 为 `1440→903 ms`（37.3% E2EL）；error case DeepSeek-R/PandasPlotBench `10326→4619 ms`（55.3%，包含错误后提前停生成）。NEL 高比例隐藏不等于端到端同等比例节省；上下文长度、并发和服务 SLO 未披露，不能外推生产 serving。v1 Table 3 中 GitChameleon 的部分代码 repair 反而可比完整代码低 15.0 个百分点，说明提前中断会丢失诊断所需后缀。
- **未证明、代价和共存边界：** 论文 §6 承认只测 Python 短/中型单脚本，未测长任务、多文件及编译语言。字符级重组一致与 deterministic 程序执行等价不证明含外部副作用代码安全；文章没有给付款、发信、文件写入、网络动作的授权、隔离/回滚及 effect identity。现有 [AGENT-TOOL-CALLING Ch78](../../../../../books/part-07-agent/78-tool-calling.md) 已区分 proposal 与授权后的 effect-time commit，也已允许低风险可取消并行准备；该论文只可能补一个**沙箱内解释器的生成—执行 overlap 受限案例**，不能推翻副作用 gate。需由 Books owner 判断是否正文真有增量；本笔记不代替整日报 Books Gate。

### 独立推进的精确版本证据：2604.01029v1

- **准入命题和评分（待日期 Gate）：** 把“弱模型出草稿、强模型修订”的总收益直接归功于 correction，会混淆更强模型独立重答、review 提示/占位脚手架以及草稿实际语义的贡献。作者以四个 matched conditions 拆解三种效应，可改变 Multi-LLM/Reflection pipeline 是否值得支付第一遍草稿的决策。`Design Delta=2, System Reach=2, Durability=3, Total=7/9`，深入审阅；高分来自可迁移的评价合同，不来自论文声称普遍胜出。
- **原文与日期：** [arXiv 2604.01029v1 HTML](https://arxiv.org/html/2604.01029v1) §3–4、Appendix A/B 已读；v1 页眉 `01 Apr 2026` 不等于公告时刻，当窗归属仍等待同批 ID 的官方公告证据。实验流程与 prompt 模板刊于 Appendix；artifact 可用性与复现尚未核验。
- **控制变量与数据流：** `x1` 弱生成器原答；`x2` 强 reviewer 看真实草稿；`x3` 强模型直接解题；`x4` 强 reviewer 在与 `x2` 同模板中看语义空白、格式匹配的草稿。三个差值依次定位 re-solving、scaffold、content；同题 `x1` 缓存给两种 review，后续调用新取样。MCQ 空稿保留 Reason/Answer 格式而用问题哈希决定占位选项；代码空稿是可解析 stub，另有 `x5` 去函数名 ablation。这里的组件是实验条件，不是一个已证明的线上路由控制器。
- **评价与受限结果：** 两组模型对、两方向：Gemini Flash Lite→GPT-5-mini 与 GPT-4o-mini→Gemini Flash（反向用作草稿质量检查）；GPQA Diamond 198、HLE 451、LiveCodeBench 1054；McNemar 两侧配对检验且 Yates 校正。弱→强 MCQ 的内容效应接近零且不显著，较大收益来自更强模型 re-solving；LiveCodeBench 中 `x4` 空 scaffold 比 `x2` 弱草稿更好，Pair1 `87.0%` vs `83.9%`、Pair2 `86.0%` vs `78.1%`，作者以 weak draft anchoring 解释。强→弱草稿内容有益，说明不能把“不要使用草稿”绝对化。上述准确率只适用于两组具体 API snapshot、这些 prompt/benchmark；论文未给实际调用价格、token 成本、并发及任务 SLO，不得从 accuracy 推成本最优策略。
- **证明/未证明、演进和 Books 关系：** matched decomposition 支持“二次调用增益并不必然来自纠错”，但仍可能受 prompt phrasing、模型采样、benchmark 类型影响，不是自然任务上的严格 causal identification。旧方案在草稿质量高、输出可验证或代码结构可复用时仍可能有价值；约束改变时应比较直接强模型、空 scaffold 与真实草稿修订，并监测错误覆盖正确答案和代码弱草稿锚定。现有 [AGENT-REFLECTION Ch80](../../../../../books/part-07-agent/80-reflection.md) 已写“retry/critique/重新 grounding 要分 treatment，paired ablation 归因”；本论文可细化其**真实草稿内容 vs review scaffold**一层，以及 MCQ/代码不同的 branch，不应新增孤立章节。由 Books owner 决定是否需正文 refine，日报尚不能标 Books 完成。

### 精确版本证据复核：2604.00510v1（Adaptive Parallel MCTS）

[arXiv exact-v1 HTML](https://arxiv.org/html/2604.00510v1) §3–5 同时给旧 positive early exit 的合理性和新 negative early exit / adaptive boosting：低 PRM 分数且全部当前叶子低于阈值时停止继续搜索，释放 rollout 容量给另一活跃任务。这里的“无希望”是关于当前 PRM、累积乘积/最小值及阈值的观测，不是数学题真实无解的证明。调度器还拥有 active-job admission、partial tree statistics、初期串行观察阈值、按 parallelism score 分配剩余 rollout slots，降低配额时抢占低评分 rollout；抢占可浪费已花 token，也会让优先级噪声变成资源抖动。串行 MCTS 在负载低、PRM 不可靠或预算/质量优先时仍是清晰回退。

§5 的作者系统是单节点 4×H100-SXM 80GB/NVLink，2 张生成、2 张 Qwen2.5-Math-PRM-7B 评分；生成模型 Llama-3.1-8B-Instruct 和 Qwen2.5-14B-Instruct，Math500 500 题与 AMC23 40 原题。AMC23 的不同前缀只补足性能压测，不进入准确率分母。论文称最高 2.83× p99 降幅，但不能脱离具体到达率、baseline 和硬件移作一般 SLO。§5.3 显示 AMC23/Qwen 加 boosting 相比仅 negative exit 吞吐降至 0.8×；§5.4 Table 1 更直接反驳摘要“maintaining reasoning accuracy”的无条件概括：Full Suite 对 Vanilla 在 AMC23/Qwen 为 `65.0%` vs `72.5%`，Llama 为 `55.0%` vs `57.5%`，Math500/Qwen `87.6%` vs `88.3%`。40 题的抽样不确定性也不允许断言必然退化；正确表述是**这项实验未证明无代价地维持精度**。并发、输入/输出长度、量化及目标 SLO 没有完整披露。独立对读 [Ch56](../../../../../books/part-05-inference-system/56-inference-scheduling.md)：已有推理预算和队列调度，但正/负退出后 reallocate 的控制流是独立条件分支；Books owner 已写入且明确准确率联测和 workload 回退，计 `2+2+2=6`，因纠正摘要与表格冲突作深入审阅，`Integrate`。

### 精确版本证据复核：2604.00726v1（Silent Data Corruption in LLM Training）

[arXiv exact-v1 HTML](https://arxiv.org/html/2604.00726v1) §III–VII、Limitations 支持以下受限判断。旧周期性 checkpoint 能恢复显性故障，但单个 HMMA 运算错误可能在 loss spike 明显前改变梯度和参数更新。作者用 NVBit 给 HMMA 输入寄存器注入 bit flip，按 bit 位置、前/反向 kernel、SM/lane 和持续步数检查传播。检测依据参数更新 RMS 相对基线的异常及 pre-clipping 梯度范数，命中后重算最近 step；监控器只产生 suspect evidence，optimizer/训练 runtime 才能拒绝当前 revision，checkpoint writer 不得提交未经核验参数。错误漏报会持续污染，误报会重复计算，硬件持续故障则须隔离并回退上一个 verified state。

§VII 单 GPU L40S、BF16 AdamW、LLaMA 60M/350M/1.3B 受控注错：12/6/3 seeds，各训练 10,000 steps，约每 100 steps 注错一次、持续 1–5 steps，重算阶段关闭注错；所报告接近无错 baseline 的 evaluation loss 和约 1% overhead 只属于该压力测试。§VII-D 承认未测分布式梯度聚合/系统级故障，不能写“生产 SDC 可检测或恢复”。[Ch35](../../../../../books/part-04-training-system/35-checkpoint.md)已有同源 `SF-2026-ARXIV-2604-00726` 的 update-integrity gate、proposal/commit 分权与上一个已验 checkpoint 回退，正是本文可迁移增量，`2+2+3=7` 深入审阅、`No Change — Existing Coverage`。本日报重新验 exact-v1，不把原有 Books 注记本身当 primary source。

### 定点准入关闭：2604.00200v1

[arXiv exact-v1 摘要](https://arxiv.org/abs/2604.00200v1)提出多个偏好 oracle 的 offline constrained RLHF、KL-regularized Gibbs policy 和 dual-only 算法，形式上很接近 [TRAIN-RLHF](../../../../../books/part-04-training-system/31-rlhf.md) 对多群体偏好不能压成单一平均分的边界。但正文 §3 的高概率约束保证要求参考策略在有限 action space 全支持、已知 feature map 的线性 reward、偏好差分协方差正定与可识别；附录 A 只在 `|X|=100, |A|=10` 的合成环境、五个 seeds、最多 3,000 条 pairwise comparisons 演示。它没有训练 LLM、没有验证 group welfare oracle 的现实标注与分布漂移，更不能把理论 `high probability` 直接交给生产安全 release gate。当前书稿已要求分开 rater identity、群体切片、标注偏差与独立安全验证；该定理在其严格假设下有学术价值，却未给当前 AI System 设计一个可验证的新 owner/决策合同。因此本窗在贡献分母前关闭；若未来同家族提供真实 LLM preference pipeline、明确覆盖假设和 held-out welfare 证据，再定点重开。注意 HTML `/v1` 页眉另写 2026-08-24，不能用该页眉替代原站 v1 身份/窗口归属。

### 定点准入关闭：2604.00387v1（RAGShield）

[原站 exact-v1 HTML](https://arxiv.org/html/2604.00387v1)的命题是政府文档 RAG 的 provenance attestation、trust-weighted retrieval、taint 标记、跨源矛盾检查与引用分层，不是后发标题所暗示的单一数值相似度漏洞。原文的 500 passages、63 attack documents、200 queries 是受控测试，不是开放 KB threat coverage；摘要称所有 tier ASR 为零，但表格承认 insider in-place replacement 仍有 `17.5%` ASR，不能采无条件“零攻击成功”。签名/来源链可证明文档身份，却不能证明签名前的内容真实或阻止有权限者原位替换，这一点现有 [AGENT-RAG](../../../../../books/part-07-agent/76-rag.md) 的来源权威/矛盾/abstain 及 [PLATFORM-SECURITY](../../../../../books/part-06-ai-infrastructure/72-security.md) 的 provenance 不等于运行时真实性边界已覆盖。其新意主要是特定政府 KB 的现有防线组合和弱评价；未给改变本项目安全 control ownership 的独立机制或可信保证，故作 family-specific pre-denominator closure。若有独立、高权限 insider threat 的可复现反证，再重开，而不是沿旧高分表纳入。

### 定点准入关闭：2604.00392v1（EvolveTool-Bench）

[原站 exact-v1 HTML](https://arxiv.org/html/2604.00392v1)把 Agent 自生成工具库当可复用软件 artifact，不只看一次任务完成率；这与 [AGENT-PLATFORM](../../../../../books/part-07-agent/84-agent-platform.md) 现有版本化 skill、依赖、回归与 promotion gate 同向。作者评估仅 99 tasks、9 sessions（每组 11）、两款 Claude 模型和自定义 library health composite；ARISE 的任务完成率 `63.6%` 甚至低于 no-evolution `66.7%`，而更高 composite 取决于复用、冗余、组合、回归等作者权重。原文没有显著性检验、未形成现实软件供应链/权限安全证明，部分 baseline 可比性仍受实现差异限制。该基准提醒“完成率与库健康不同”，但当前书稿已经将二者拆开；没有新发布决策或可迁移 failure boundary，因此不因 benchmark 名称与系统相关就进入贡献分母。后来若其回归 metric 在 held-out versioned libraries 上改变 admission 判定，再作为新证据重开。

### 精确版本证据复核：2604.01220v1（Universal YOCO）

[原站 exact-v1 HTML](https://arxiv.org/html/2604.01220v1) §3 把 YOCO 的 Self-Decoder/Cross-Decoder 分工与参数共享循环结合：只有使用 sliding-window 等 efficient attention 的浅 Self-Decoder 循环 `T` 次，最后形成一份供全部 Cross-Decoder 层复用的 global KV；不是每次循环都复制完整 global cache。旧普通 decoder/Universal Transformer 的全层循环在短上下文、小并发或已有优化 runtime 下仍是简单对照，但其 global attention 与逐层 KV 会随深度/循环一起扩大。新方案将**额外表征深度的 compute** 与**全局 KV 物化**部分解耦，代价是局部 window state、额外前向次数、训练时长和跨层接口复杂度；`O(N)` 是固定层/窗口/循环设置下的序列长度复杂度，不是总运行时内存常数。

§4 的主要模型为 10B 总参数/1.3B activated MoE、300B tokens、AMD MI300X；另以 1.3B dense、20B tokens 比较 RINS/Universal Transformer/ParScale，等 FLOP 结果和等步数结果不能混称。§4.5 的 Nano-vLLM/H100-80GB serving 用 1.3B、batch 32、128 输出 token 及所测序列长度；文中声称相对 YOCO decode 仅约 5% throughput 损失、相对 RINS KV 显著下降，是作者受控图形结果，不提供多租户、精度/量化、真实请求长度分布和 SLO。与 [Ch22](../../../../../books/part-02-model/22-long-context.md) 的 fixed-state、recurrence/stop 主线对读，已有“循环何时停”的风险，但没有“只循环局部注意力、global KV 单次生成”这个架构条件分支；可在 MODEL-LONG-CONTEXT 窄幅吸收，Inference KV 只短 handoff。建议 `2+2+2=6`、标准 Source Review、Books Integrate，待共享 Books owner 落笔与独立复核；不把单篇当通用架构最优。

### 精确版本证据复核：2604.00477v1（Agent-Judge Score 与 Coverage）

[原站 exact-v1 HTML](https://arxiv.org/html/2604.00477v1) §3–4 用 32 个有专家度/persona 的 Agent 评委，在 15 个领域×复杂度任务、两个 target/judge 模型对里共运行 960 次会话。评委既交互又写逐轮分数/问题 diary；不同 judge 会改变目标模型所见请求，故“多评委对同一题评分”与“多交互路径发现问题”是两个 estimand。ICC 随 panel 大小上升，并不意味着经语义去重的独特问题种类也已饱和；作者用嵌套 panel 及七个去重阈值观察后者仍递增。设计上发布评估应分别跟踪 score uncertainty、独立交互的 issue coverage 和严重度，不能用均分稳定作停止规则。旧静态 rater panel 对固定 benchmark 的分数校准仍成立；主动交互探索则需更多预算、去重与风险切片，并面对 persona/任务选择偏差。

实验边界：50 名人类招募后只保留 43 人/86 会话；人—Agent 与人—人配对差异的 `p=0.379` 仅是**未拒绝差异**，不是统计等价或人类可被替代的证书。独特 issue 的 `N^0.69` 受作者 15 任务、两模型对、32 人设、嵌套 panel 和语义去重阈值定义；阈值 0.50–0.80 下指数仍低于 1，但不能外推 universal panel size。Ch66 已有按 estimand 与 rater/item/repeat variance 分配预算，却未把 active judge 的分数收敛与问题发现覆盖作为独立停止轴。`2+1+2=5`；Books owner 已在 Ch66 active judge 小节后加入“评分可靠性 vs 去重问题发现”的两个 estimand 与预算停止决策。我独立对读 exact-v1 §3–4 与正文，确认段落未将 `p=0.379` 解释为等价，Books Decision 为 Integrate：PLATFORM-EVALUATION-SYSTEM Ch66。

### 精确版本证据复核：2604.00986v1（MyPhoneBench）

[原站 exact-v1 HTML](https://arxiv.org/html/2604.00986v1) §2–5 把手机 Agent 的良性任务拆成三种独立评价对象：最终任务状态、执行途中有无越过数据最小化/许可边界，以及跨 session 是否正确使用用户可控的已保存偏好。作者的 Android 模拟环境有 10 个 controlled apps/300 tasks，其中 250 独立任务、50 跨 session 对；SQLite `form_drafts` 保存**未提交**字段的每次编辑，access log 区分申请许可与实际读取，避免只看最终 app 状态漏掉过度填写。受控任务把权限请求、非必要小部件再次披露、可选个人字段填写分别做 deterministic probes。作者以五个模型评估，任务成功与隐私合规完成/偏好迁移的排序不同；这是作者受限环境中的观察，不是模型生产隐私排序。

评测的 privacy-qualified success 让任务完成与 privacy score 达门槛共同进入**同一 300 任务分母**；否则弱 Agent 因过早失败没有接触风险表单，平均隐私分反而虚高。论文默认阈值 `τ=0.7` 是作者操作点，非规范要求，不能覆盖三项原始 probe 和阈值 sweep。mock apps 为 form-centric 场景、每次 HIGH 请求由模拟用户总是批准，故只测 voluntary restraint，没测拒绝权限后的行为；不包含网络泄漏、商业 app 差异或真实用户数据。Ch66 已有多轴评估与任务 outcome/证据身份原则，但此文进一步把**动作流中的数据写入**纳入 evaluator contract，同时保留固定分母的成功∧隐私结果和跨 session paired outcome，形成可迁移的发布检查路径；Security/Agent 只需短 handoff。`2+1+2=5`、标准 Source Review。Books owner 已在 Ch66 Outcome Witness 后加入未提交字段编辑、权限日志、固定任务分母及 always-grant 的受限条件；我独立对读原文 §2/§3/Appendix B 和相邻正文，确认没有把阈值、模拟环境或模型排序外推，Books Decision 为 Integrate：PLATFORM-EVALUATION-SYSTEM Ch66。

### 精确版本证据复核：2604.00788v1（UK AISI Alignment Evaluation）

[原站 exact-v1 HTML](https://arxiv.org/html/2604.00788v1) §1–5 的可迁移贡献并非“未发现 sabotage = 系统安全”，而是 **evaluation scaffold 本身可改变可见结果**：Petri 评估者可 rollback 到先前对话点，选择另一条诱发路径；`last branch`、`any branch` 与 `average over branches` 的统计单位不同，不能把最末成功分支冒充全部尝试的发生率。机构用内部 Claude Code deployment-task 轨迹、同任务在模拟 scaffold 的轨迹和安全研究 sabotage 场景交叉测试，以尝试分开环境外观驱动的 evaluation awareness 与任务本身高风险驱动的 awareness；前者缩小后，后者仍可让目标识别评估。被 LLM grader 标出的 sabotage 例子中，人工复核的子集均属误报，故论文只报告在所测条件下**无确认案例**，不支持‘不存在倾向’或部署率结论。

四模型/有限安全研究任务、Sonnet 4.5 作为 evaluator、内部 deployment 数据只覆盖 Sonnet、prompted pairwise/事后问题与未提示自述并非同一传感器；GPT-5 没有可见 reasoning trace 时，零自述不能比较真实 awareness。scaffold 产生的 sabotage 轨迹仍可与部署轨迹区分，统计也受评估者 rollback 选择偏差。对读 Ch66 现有 evaluator/target/sampling identity、外部 outcome 及 judge blind-spot 段，尚未明确 **可回滚 evaluator 的分支选择与环境/任务识别度** 作为评估合同；`2+1+2=5`、标准 Source Review。Books owner 已在 Ch66 主动 probe 之后加入 branch-tree、last/any/average branch 统计及同任务不同环境的条件对照；我对读原文 §1.1/§1.3/§2/§5 与新正文，确认其保留人工复核与任务分布局限，Books Decision 为 Integrate。日报整体 Gate 尚未通过。

### 精确版本证据复核：2604.01193v1（Simple Self-Distillation）

[原站 PDF v1](https://arxiv.org/pdf/2604.01193v1) 首页写 `Date: April 2, 2026`，而[同版本 HTML](https://arxiv.org/html/2604.01193v1) 错写 `August 24, 2026`；以下机制与数值以 PDF v1 为准，arXiv ID 批次只作首次公告归属。§2 和 Appendix B 说明：若从同一模型在温度 1、全词表支持下抽样，再用交叉熵训练回同一分布，则期望 score-function 梯度为零；自采样不是天然增益。SSD 在**采样时**改变温度并做 top-k/top-p 截断，拟合目标被推离原分布支持；截断产生 kept-support mass gate，保留支持集内再可重新分配概率。代码中低歧义 lock 位的尾部 distractor 会被压缩，多路正确 fork 位可以保留相对探索，而单一全局推理温度不易同时做到两者。这是目标分布转移的条件机制，不是错误程序自动变真。训练和推理都须版本化 sampling/truncation/模型状态；压掉稀少但正确的分支、错误自强化与分布外退化是新增压力。

实验为约 10K 去重 rSTARcoder 竞争编程题、每题一个自生成解、只去空/单行 stub、不做代码执行或正确性过滤；五个 Qwen/Llama instruct/thinking 4B–30B 模型，用 8×B200、Megatron-LM、长度 65,536、global batch 32、instruct 2,500 step/thinking 300 step。LiveCodeBench v6 上 Qwen3-30B-Instruct pass@1 `42.4→55.3%`，其它模型增益较小；v5/域外只作有限补证，不能据此宣称无 verifier 的训练适合任意领域。作者改变训练目标与 evaluation decoding 的配置，不能把全部改善单独归于“数据质量”；pathological 高温样本有大量无有效代码仍改善所测结果，也不证明错误文本安全可普遍再训练。Ch29 原有 self-distillation 段落曾错写“生成示范再正确性过滤”，与 exact-v1 的 raw 未验证样本不符；Books owner 已在原段纠正，并明确**同模型分布 fixed point → 训练采样支持集变换 → 情境依赖精度/探索重分布**的条件分支。我独立对读 PDF v1 §2/Appendix B 和上下文，确认其保留错误固化、真实 lock/fork 未知及 serving policy 分离；`2+1+2=5`、标准 Source Review，Books Decision 为 Integrate：TRAIN-SFT Ch29。

### 余项题摘准入裁决：不是把相关论文全送全文

- **`2604.00547v1`，前分母关闭。** [exact-v1 摘要与 §3–5](https://arxiv.org/html/2604.00547v1)提出统一图文模型的七类理解/生成任务安全矩阵和 intrinsic/contextual 两种判断；这提示不能用文字拒答率代替所有输出模态的安全验收。但其 16 模型比较混合了不同 backbone、数据、后训练和接口，某些 closed-source 模型不提供图像生成 API；表 2 的差异不能单独识别“架构统一导致安全下降”。[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)与 [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)已经要求理解、生成各自及联合验收、不能复用另一侧结果，Ch66 已按模态/故障切片分账。本篇是特定 benchmark 扩项，不产生新的安全 owner、因果结论或 release contract；若未来有同 backbone/同训练预算的配对实验改变该结论再重开。
- **`2604.01039v1`，前分母关闭。** [exact-v1 摘要与 Method](https://arxiv.org/html/2604.01039v1)以 46 条 system instructions、四模型检查直接询问被拒而编码/序列化输出泄露的情形；这是已知“拒答 prompt 不等于保密边界”的另一个攻击格式，不应沿用摘要的 `>0.7` 当生产泄露率。其 one-shot instruction reshaping 在所测提示下降低攻击率，却仍把秘密置于模型可读 Context，不能给可验证的 confidentiality 或授权保证。[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)已规定 secret/credential 不进入模型 Context、使用 opaque handle、最小权限工具和独立 DLP/授权。它不改变这一设计判断；若新攻击越过外部 effect gate 或显示独立隔离失败，可重开。
- **`2604.00445v1`，前分母关闭。** [exact-v1 摘要与 §1–2](https://arxiv.org/html/2604.00445v1)将语言行为导出的 entropy/不确定性称为 correctness proxy，低信息区域会失去区分性；Truth AnChoring 用少量或噪声真值标签对 score 做后校准。该形式化和方法有学术价值，但在本知识树中，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)已明确同源信心/一致性不是真值、高风险阈值必须有独立 ground-truth calibration，校准受 slice 和漂移约束。TAC 未移走标签、校准分布或 evaluator 身份责任，也没有修正现有结论；不因新后处理名词重复计分。若出现明确不同的可验证 label-scarce coverage contract，再重开。
- **`2604.00824v1`，前分母关闭。** [exact-v1 摘要与 §3.3–3.6](https://arxiv.org/html/2604.00824v1)把长 coding-agent 轨迹先经 Logistic Regression 特征筛选，再按 action–observation 完整边界切块、以滑动摘要给 LLM judge 评分并选取局部高分段；所谓 `decision-critical tokens` 实际主要是**段级数据筛选**，不是新的 token loss/gradient owner。安全切分减少分块误判，但摘要状态可能遗漏跨段因果，局部 judge 高分也不等于最终 executable patch 正确；多个模型/脚手架结果未把 safe-split、摘要、宏筛、训练量和模型差异单独识别。Ch27/29 已有训练轨迹筛选与 supervised-token 分配，论文目前只能作具体流水线案例，不能据高百分比推一条新普适设计律。若有等预算、同 verifier、分组件消融证明新的 state boundary，可按新证据重开。

## V3 最终归并与反向抽检

旧 DOI-created 线索共 513 个 raw identities，覆盖当时登记的 arXiv 类别，不等于 04-02 官方全部公告量，也不等于本项目候选。旧选择 35 条的 pinned-v1 完整题摘均重读；其中 **17 条**达到长期贡献准入、**18 条**在分母前关闭。旧排除 478 条做标题全览与 22 条有潜在系统机制/纠错信号的定点摘要查漏，恢复 **8 条**候选；最终本窗 **25 个唯一家族**，日报表中 25/25 有 exact-v1 证据与 Books 终态。不能把 `25/513` 当作真实每日研究保留率，513 是 DOI 入库日期和注册分类限定的旧库存。

旧 35 中保留的 17 个 ID 为 `00073/00136/00317/00368/00477/00499/00500/00510/00529/00715/00726/00785/00801/00830/00865/00892/01168`；关闭的 18 个为 `00067/00131/00200/00356/00387/00392/00414/00430/00478/00547/00594/00694/00835/01007/01020/01039/01128/01221`（均属 `2604.*v1`）。`00414` 的 [exact-v1 摘要](https://arxiv.org/abs/2604.00414v1)只把 signal/policy/action 分层用于三组 Agent case，未隔离出新的可迁移 control-owner 边界；Ch81 的 policy graph 和 Ch72 的 sensor/decision/effect 已表达该分权，故将阶段性的“拟关闭”落实为 pre-denominator closure。其余关闭项的 family-specific 理由在上文表及定点复核段，不沿用旧高分或“继续核”状态。

从旧排除集恢复的 8 个候选是 `00375/00491/00660/00788/00986/01029/01193/01220`；这证实旧筛选存在**假阴性**，但不是将排除集全部升级为全文队列。反向对照中，`00421` 虽提出 hidden-state subspace routing，仍未独立移走 Ch21 已有的中心路由与负载所有权；`00445` 的少标签真值校准未超出 Ch66 已写的独立标签与切片校准；`00824` 是受限 coding trajectory 分段筛选，不是新的 token-gradient 机制；`00547` 的多模态安全矩阵混合 backbone/训练/API 差异，不能把差异归因统一架构。这四条经完整题摘与必要方法段定点核后关闭，作为**假阳性防线**的对照；旧 35 的 `00547` 同时计入上面的 18 条，不能重复计数。

日期归属采用[官方公告计划](https://info.arxiv.org/help/availability.html)（美东夏令时 20:00=次日北京 08:00）和本笔记前部 `00001/00600/01224/01225/01226` 相邻切点及 pinned-v1 交叉校验，将 `2604.00001–01225` 归于本窗公告批次；它是**有界批次推断**，不是逐篇秒级 first-public 字段。Submitted、DataCite created 与当前 OAI datestamp 任一单项均未单独用来定 owner。未来有单篇延期公告、撤回或精确日期的官方反证，仅重开该家族。TIE `00499` 与 SSD `01193` 的 v1 HTML/PDF 日期冲突以 PDF v1 内容作机制证据，HTML 页眉不用于时间判定。2026-09-26 的 25-ID 官方 arXiv API 批量复查均返回记录、标题没有 withdrawn 标记；这只是当前可见状态，不证明未来不会撤回，也不代替原文里的修订/纠错说明。

14 个日级来源的实际停点和隔离缺口在日报 §2 与 §5。外部历史目录、时区或正文仍缺失的项目不进入本窗确定候选、不支持零遗漏断言；它们不会把已有可核的 25 项重新变成 pending。至此报告作者一侧的来源、分母、证据与 Books 处置已收束，且主任务独立审计智能体 `/root` 已通过日级语义复核；实际复核范围与残余外部限制见日报 §6。本文件的阶段性行保留为审计轨迹，而非未完成任务清单。
