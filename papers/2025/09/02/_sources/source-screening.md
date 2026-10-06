# 2025-09-02 原始入口与局部准入笔记

作者：daily_20250902。窗口为 `[2025-09-01T09:00:00+08:00, 2025-09-02T09:00:00+08:00)`，即 `[2025-09-01T01:00:00Z, 2025-09-02T01:00:00Z)`。以下不是旧 Weekly 的重排；从当前可恢复官方入口独立重建。抓取发生于 2026-10-06，抓取时间不替代公开时间。机器只下载、解包和提取字段，不决定贡献。

## 原始抓取范围与日期

原始请求、状态、字节量及时间分别保存在 `fetch-log.json`、`followup-fetch-log.json`、`followup2-fetch-log.json` 和 `directory-js-fetch-log.json`。HTML 保存为 `.html.gz`；`.visible.txt` 是去掉 script/style 的可见文字，`.text` 保留初步 HTML 文本提取，不能因后者有 script 内容而宣称浏览器看到了目录。部分原始 HTTP body 已 gzip 编码，外层存储压缩之外还需再解一层，原始 body 保留。

| 官方来源 | 实际处理 | 当前判断与停止点 |
| --- | --- | --- |
| OpenAI | Research → Research Index → 官方 `/news/rss.xml`，1247 条，`pubDate` 范围 2015-12-11 至 2026-10-05；完整字段见 `openai-rss-records.json` | RSS 中本窗没有发布项。相邻 2025-08-28 与 2025-09-02 04:00 GMT；后者是窗后事件，不能按标题里的 Sep2 纳入本日。Research Index 首页本身未到历史窗，使用同站完整 RSS 恢复。 |
| Anthropic | Research 原始 Flight 内嵌目录 174 条，最早 2021-12-01，最新 2026-10-01；`publishedOn`、slug、title 见 `anthropic-directory-records.json` | 相邻 2025-08-27T00:09Z 与 2025-09-05T00Z；没有本窗目录发布。该记录仅覆盖 Research 目录，不声称全站旧 News 未发生事件。 |
| Google AI | DeepMind Research/Blog 当前入口；Google Pubs 默认首页；`?year=2025` 实测忽略，仍有 773 页；已按官方同源 JS 恢复真正参数 `?category=2025`，46页机械抓取结束，提取676个唯一title/URL（目录filter计数677） | 仅恢复年份目录，未逐项完成题摘/日期筛选，也不将676算本窗命中。该无日粒度目录的后续语义/日期处理仍是普通待办；本轮停止年度扩池。DeepMind Blog当前页仅到2026，历史恢复未完成。 |
| Meta | Research HTTP 200，但是可见正文仅 59 字品牌标题 | 不是论文目录，不能记无更新；需浏览器核查及原始替代目录。 |
| Qwen | 旧官方博客首页，Sep23 与 Aug19 相邻；旧 Publication 为 selected publications；页面声明迁移 qwen.ai | 旧站可读切片无 Sep1/2 事件；新站真实 redirect 被 CONNECT403，当前不能声称迁移后完整覆盖。 |
| DeepSeek | 主页 → `/news/` 的研究索引与动态 | 研究索引最后可见 2025-05-14，未见本窗项；动态只显示最近五条且有“查看全部”，需展开后才可宣称动态范围覆盖。 |
| Moonshot | Kimi Platform Blog完整可见目录到 2024-05-29 | 2025-09-05 与 2025-08-22 相邻，本窗目录未见发布；组织仓库补充路径仍需定点检查。 |
| Hunyuan | Research HTTP 200，可见正文仅“腾讯混元” | 空壳，不证明没有目录；需要浏览器“全部”列表核查。 |
| Z.ai | Research首页与 `?page=2`；第二页末尾“没有更多”，最早 2025-12-07；Release Notes可读至 2025-07-15 | 当前中文研究库没有恢复 Sep2025 历史。Release Notes有 2025-09-30 与 2025-08-11 相邻，无本窗 release；release切片不替代旧技术研究目录。Research JS初取503。 |
| ByteDance Seed | 官方 Public Papers当前前20条，仅2026；主 JS路径已从原HTML恢复 | 需要年份筛选/后续页；JS CDN `lf-flow-web-cdn.doubao.com` CONNECT403，主站200不证明互动能执行。 |
| ERNIE | Blog共两页已读到最早2025-06-30；Publication初次503，定点重试200，有四篇论文（两2025，两2026） | Blog相邻2025-09-12与2025-08-14，无本窗博客事件；论文v1与官方仓库仍需轻量定点核对，不能把year=2025当精确公开日。 |
| MiMo | 首页8项完整Paper目录，相关相邻Sep19与Jun4；Blog条目已恢复 | Paper可见切片无本窗新增；Blog缺少历史精确日期时仍需核查，不能用Paper数量代替Blog检查。 |
| MiniMax | 英文Blog首页到2025-10-27；`?page=2`返回相同条目（参数被忽略） | 需要真实翻页或其他官方历史入口；中文minimaxi.com与官方CDN file.cdn.minimax.io CONNECT403，未把当前首页当全年完整目录。 |
| arXiv | 12个注册分类长月份路径 `/list/<category>/2025-09?show=1000`可读；`show=200`被拒400，改用受支持大小；月份按ID升序、没有公告日分组 | 仅机械恢复2509.00*前缀374个跨类去重标题与API题摘，非本日候选、非本日初筛完成数。官方API published是原始提交时刻，全部前缀提交字段早于Sep1；不能据此决定实际公开窗。 |

arXiv公开日的原始历史政策见 [`availability-before-20250903.md`](../../_sources/official-calendar/availability-before-20250903.md) 和对应 provenance。官方原文明确最终ID在公告过程赋予，不能回填月份；2025 Holidays列 Monday 1 September。按EDT（UTC−4），本窗唯一正常公告槽为 Sep1 20:00 EDT = Sep2 00:00Z = Sep2 08:00 北京时间。`On Deferred Mailings` 只写“defers a mailing”，需独立确认当次是否整个公开批次延期；不能把提交日期、九月ID或一般发信延期冒充当次公开事实。定点 `/list/cs.CL/2025-09-02` 返回 invalid period；`/250902`不是历史日列表；`/new?date=`已知返回当前批次，不用作历史证据。必要替代路径 DataCite API、status.arxiv.org、blog.arxiv.org、info.arxiv.org（help跳转）均实测CONNECT403；官方GitHub历史政策已取得，但实际延期事件尚待恢复。

## 首批题摘语义校准（日期未核，不冻结候选）

直接读取8篇 `https://arxiv.org/abs/<ID>v1` 的完整标题与摘要，原页、题摘与请求日志保留。以下题摘足以界定定点准入问题，未读取机制全文，不评分、未作Books决定，也不把日期未核的材料列为确定本窗候选。

| ID / 精确版本 | 题摘实际贡献与处置依据 |
| --- | --- |
| 2509.00031v1，ZeroQAT | 低bit PTQ的局部重建与端到端性能目标不一致，而传统QAT反传内存高；原文提出前向梯度估计，并联合学习量化权重、clipping阈值与等价变换。因此值得核验反传内存约束下端到端QAT的可行性与代价，连接TRAIN-SFT / INFER-GPU-MEMORY。v1未提供当前v2新增手机与8GB具体数字，禁止套用。 |
| 2509.00036v1，A-FloPS | 现有training-free方法改solver仍受原采样轨迹限制；原文将diffusion score解析变换为flow velocity，再分离线性drift与时间变动较低的residual。因此值得核验极低NFE时高阶求解的收益/误差边界，owner MULTIMODAL-GENERATIVE-PARADIGMS；摘要5NFE数字待相同质量/模型配置对照。 |
| 2509.00105v1，AdaptCache | KV持久层的SSD hit有加载成本；原文把每entry压缩算法、比率与DRAM/SSD放置共同选择，以质量约束换更多DRAM hits。因此值得核验tier placement与有损压缩需联合决策的条件，owner INFER-KV-CACHE / INFER-GPU-MEMORY，不能只引用1.43–2.4×。 |
| 2509.00217v1，Learning to Shard | 现有heuristics分别选择并行度与算子分片；原文把两者放入同一RL搜索并用elite history attention调策略。因此值得核验分开优化遗漏的耦合是否足以改变分布式LLM inference配置选择；H100 MoE与1.6T、吞吐/SLO、搜索预算需读全文才能采用。 |
| 2509.00072v1，Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination | v1实际做的是20,277论文合成1,643多步QA、跨cutoff未见显著衰减；与已报道衰减的直接抽题作比较，并提出推理合成可能缓和contamination的假设。准入只限纵向时序信号缺失的评价反证；题摘不证明“无衰减就是无污染”，也未受控证明问题转换或synthetic reasoning消除了污染。v1原页提示一个较新版本已withdrawn；定点v2官方页证实2025-10-06T14:10:14UTC的v2撤回，未给撤回原因。v3/v4后续恢复且改标题为Test of Time，API当前v4已改为同源问题转换+influence分析，中心证据变化。v1本身未标撤回，不能虚称整个family被撤回；但真实撤回/纠错信号及因果变化未清，不采用v1主张，后续核相关说明。 |
| 2509.00100v1，MODE | 范围内RAG，但cluster/centroid/topcluster路由及100–500chunk局部实验复用了成熟粗索引机制。摘要给cluster粒度、多路召回precision tradeoff，没有指出改变这些已知设计认识的新失效条件或受控反证。按所读题摘排除贡献；日期未核不影响这一处置，不能据此声称本日日期核验完成。 |
| 2509.00244v1，UDR | 范围内Agent，但题摘只是可选模型、自定义minimal/expansive/intensive策略wrapper与UI示例；未给原来做不到的执行机制、可定位的新失效路径或有效性条件。按题摘排除贡献；“framework / configurable”本身不是准入理由。 |
| 2509.00047v1，Brain-inspired replay | 需要校准的反向样本。CIFAR100 continual learning不因模型小而范围外；摘要读到internal replay+SI的忘却改善、初始task accuracy代价及latent overlap增加。它研究表示与稳定/可塑性机制，可能提供受控负面边界，不能仅以没有LLM新架构排除。是否超出已知stability/plasticity复述，要定点读它的受控证据和相对原BIR机制的实际增量；现未关闭。 |

fresh_review实际读取8篇exact-v1题摘后，对ZeroQAT/A-FloPS/AdaptCache/Learning to Shard四项准入与MODE/UDR排除通过局部校准，仍以日期/正文恢复为前提；00072限纵向时序信号反证，00047确认范围内且可定点读负面边界，未把成熟stability/plasticity复述当新机制。该校准不是整日来源、候选证据或Books验收。root于2026-10-06要求在日期/历史枚举阻塞下保存checkpoint，停止全年度/未定日扩池；没有把当前日期不确定的材料纳入Books。普通未处理的目录、全文或Books比较仍保持待办，不写作外部材料阻塞；精确续跑位置见本目录 `RESUME_CHECKPOINT_20261006.md`。
