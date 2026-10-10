# 2025-07-02：独立来源、准入与停点

窗口：[2025-07-01T09:00:00+08:00, 2025-07-02T09:00:00+08:00)。本次检查：2026-10-07T00:34:47+08:00。原始响应中的抓取时间为 UTC。

仅处理本日。未读取其他 Daily/Weekly 的候选、评分或判断；机构原始响应按相同 URL 从同月缓存复制，本日重新过滤。缓存 `.request.json` 中的时间保持原值，不把它改写成新的抓取。`capture.py` 只保存原始响应和文本，没有准入判断。

## 原始入口与实际停止点

- 机构缓存：OpenAI research 与完整 RSS；Anthropic research；DeepMind blog、Google pubs/六月 blog 的运输失败；Meta research 运输失败；Qwen blog 及第 2 页；DeepSeek 官方更新页；Kimi blog；Hunyuan research + `publicList` pageNum=1/pageSize=100；Z.ai research 与 `?page=2`；Seed 2025 papers tokens 0/20/40/60/80、blog tokens 0/20/40；ERNIE blog 及 page 2；MiMo 首页；MiniMax blog 与 `?page=2`。
- 机构过滤以窗口和模型/训练/推理/Agent 主线为界，不逐项阅读跨年目录。可夹住窗口的目录在两侧日期停止；只返回近期内容、伪分页、空文章响应或运输错误的来源不能证明历史零命中。
- OpenAI RSS 的窗内条目为 Genspark：`Tue, 01 Jul 2025 10:00:00 GMT`，即 18:00 BJT。Research curl=403；Genspark 正文经浏览工具成功恢复，URL 为 <https://openai.com/index/genspark/>。核心说明见下节。
- Google 以 `site:deepmind.google "July 1, 2025"`、`site:research.google/blog "July 1, 2025"` 做有限补检；恢复到 <https://deepmind.google/research/publications/102792/> 的完整题摘。页面 July 1 为目录日期，链接正文是 `2506.12346v1`。`google-window.request.json` 保存运输失败；浏览工具另成功读取该官方页面与它直接指向的作者稿。
- Meta、Hunyuan、Z.ai、MiniMax 窗口精确域名/日期检索没有返回可用原件。搜索无结果只表示检索受限，不表示来源零命中。混元按来源说明尝试隐藏浏览器核查 Research：初始化 30 秒超时、会话重置；没有取得目录状态，不声称按钮/历史分页已验收。
- arXiv 首次原始查询用 submitted_date_first，June30→July1（终点不含）和 July1→July2；前者四组：language model/LLM/Transformer、distributed training/model parallel/LLM inference/GPU kernel、diffusion/world/VLA/multimodal、LLM agent/language agent/RAG。June30 系统查询 2 条；其余宽结果仅作查漏，LM 两页实际只抓每页 1–50（另有未读分页），不称全量题摘已筛完。
- 收窄为 title-field 的公告查询：systems、world/VLA/diffusion、Agent/RAG、language model/LLM/Transformer，July1→July3、`announced_date_first`。四个 `*-valid.request.json`/`.raw`/`.txt` 保存完整响应；都返回无结果。但与可取得的 July 论文身份不相容，不能据此证明本窗零命中。一次错误字段 `announced_date` 返回表单错误，明确作废，不计覆盖。
- 月目录短路径 `2507` 返回 404；改 `2025-07` 成功取 cs.CL、cs.LG、cs.CV 各 1–25 标题。仅浏览与主线相关标题、检查撤回信号；月目录没有具体日公告/时刻，不把 75 个条目变成候选队列。`cl-day` 使用 `new?date=2025-07-02` 却返回 2026-10-06，作废为历史证据。
- Announcement API 第一次 URL 方括号导致 curl 参数错误，不是原始接口无材料；没有把它计作已检查或零命中。此前已取得的有效搜索/月份目录/精确 abs 构成本次有限恢复，停止继续追 OAI/DataCite 或正常公告 schedule。

## 首小批：完整题摘、核心说明与具体处置

| 身份及原件 | 本日判断 | 理由与停止边界 |
| --- | --- | --- |
| [HelixPipe 2507.00394v1](https://arxiv.org/abs/2507.00394v1)，`abs-helix-v1.txt` | 贡献方向成立；落窗受阻 | 长序列 quadratic attention 导致 PP 气泡和内存失衡 → 原文新增跨 stage 的不同 microbatch attention partition 与 two-fold FILO schedule → 改变长序列 PP 任务划分/调度选择。不能只因有 owner 入选。已完整读题摘，当前页无撤回/纠错说明。submitted 原值 `Tue, 1 Jul 2025 03:11:18 UTC` 不是 public timestamp；搜索条目还把 original submitted 标成 June30，不以冲突元数据定日期。公告恢复失败后停止全文/评分/Books；26% 不作已核验收益。 |
| [Multi-LLM edge survey 2507.00672v1](https://arxiv.org/abs/2507.00672v1)，`abs-edge-v1.txt` | 排除贡献 | 全题摘为综述 edge、多模型、调度/编排/信任，没有新增执行机制、成立条件或修正既有解释的证据；主题可映射 Agent 不足以准入。当前页无纠错/撤回信号；日期不影响排除，不再追日期。 |
| [PB-LLMs 2507.02966v1](https://arxiv.org/abs/2507.02966v1)，`abs-pba-v1.txt` | 排除贡献 | NER 匿名化与既有 debiasing 方法组合，24,000 简历、BERT/RoBERTa 六算法的局部 resume scoring 保持性能；没有新增通用隐私保证或成立边界。没有将“generally applicable”广告性外推采纳。当前页显示 v2，未见具体纠错/撤回信号；不因版本号扩审。 |
| [HPC accelerator comparison 2507.00418v1](https://arxiv.org/abs/2507.00418v1)，`abs-hpc-v1.txt`；[HTML](https://arxiv.org/html/2507.00418v1)，`hpc-core-v1.txt` | 定点补读后排除贡献 | 不因是 benchmark 或摘要缺配置而关闭。v1 §2–5 实际读到：固定 prompt、32/64/128/256 concurrency、100–500 requests、专用节点、各型号/SoC 的 throughput/W 比较；GH200 ARM compatibility 为已有实现限制。实际增量是型号与部署库存的经验比较，而非新的执行机制或改变既有资源选择的解释/反证。未建立新的质量/能耗成立边界，不能把当前版本的“1卡vs8卡、20×/35×”倒灌 v1。date 未定不继续深审。 |
| [Genspark 官方案例](https://openai.com/index/genspark/) | 排除贡献，时间已核实落窗 | 原始正文核心说明：九个模型、80 余工具动态分派；Realtime 处理会话、shadow model 经 message queue 监视引导。未披露新的协调机制、可靠性条件、失效分析或可比对照；成熟组件组合与 ARR 不改变长期解释。没有把营销案例误收为系统机制论文。 |
| [Refract ICL 官方目录](https://deepmind.google/research/publications/102792/) 与 [2506.12346v1](https://arxiv.org/abs/2506.12346v1)，`abs-refract-v1.txt` | 身份/事件隔离，不作本日新公开证据 | 全题摘确有 challenging demonstrations 重复及 zero-shot error signal 的选择增量。目录 July1 不证明新首次公开，作者稿固定 v1 的 submitted 原值为 June14 04:51:34UTC；目录没有本日重要修订说明。不能把机构收录时间搬作论文归属，也不从提交推精确首公开。只恢复身份后停，不扩全文/评分/Books。 |
| [Pitfalls of Evaluating Language Models with Open Benchmarks 2507.00460](https://arxiv.org/abs/2507.00460)，`abs-withdrawn.txt` | 撤回排除 | 本次读取官方当前页明确 withdrawn，v3 `Wed, 3 Jun 2026 23:11:39 UTC (1 KB) (withdrawn)`；说明核心贡献/方法与已发表工作实质重叠。保留排除依据，不评分、不入 Books、不采用 v1 主张。日期恢复不影响撤回处置。 |

其他查询标题仅作来源恢复线索，不按主题关联批量称“潜在贡献”。例如科学/医学、作物、材料、宇宙学和传统语言学等题名明确范围外的条目无需读正文；宽列表未自动成为需逐项关闭的池。涉及在特定领域组合现成组件者，不绕 Data/Evaluation owner 纳入。

## 终态边界与独立复核

root 已独立完整读取 HelixPipe、Multi-LLM、PB-LLMs、HPC、Refract ICL v1 题摘及当前 withdrawn 官方说明，另读取 Genspark 核心说明 L43–54 与 HPC §2–3 配置，覆盖上述七项原件。确认 attention partition + FILO 的具体 PP 调度替代，FIRST 准入方向成立；收益与日期仍不得采用。其他宽题名未被独立全量读取。

当窗确定候选暂为 0，不等于当窗没有贡献或原始来源零命中。HelixPipe 及不能恢复的历史来源被隔离，不用于正面证据、Books、覆盖无遗漏或性能/安全保证。恢复条件：取得目标公告的原始记录（版本身份、公开日与时区/范围）或正文首次公开的等效作者/官方记录，且完全落窗；先定日期再只重开所需贡献/证据。Refract ICL 先提供 distinct 本窗公开/重要修订事件；不存在新事件则不重开。撤回项不在上述日期恢复队列。

没有可采用候选，没有 Books delta；这不是对既有书稿的“已有覆盖”认定，不制造修改。root 反馈 MiMo Blog 仍缺历史段，Paper 切片不能支撑整源已检查，日报已修为受阻并保留局部恢复范围。其余日期/外部来源隔离与无评分/无写入检查通过；DAY 通过为安全终态验收，不是完整 Coverage/Evidence 通过。
