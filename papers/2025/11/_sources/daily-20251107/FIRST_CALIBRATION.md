# 2025-11-07 首批准入校准请求

作者窗口：BJT [2025-11-06T09:00:00+08:00, 2025-11-07T09:00:00+08:00)。仅本日独占文件；候选集合尚未冻结，未作语义完成声明。首批 ready，需 root 非作者独立校准后才展开受影响集合的正式证据/Books 处置。

## 拟准入，不是已确认的本窗分母

1. [Kimi K2 Thinking](https://platform.kimi.com/blog/posts/k2-think)：官方原字段 `2025年11月06日`，不得补造时刻。已打开 [作者模型卡](https://huggingface.co/moonshotai/Kimi-K2-Thinking) 的完整模型说明；候选命题是后训练 QAT 的原生 INT4 工程取舍及长程交错 reasoning/tool execution 的局部评价条件，而非“MoE/工具调用存在”或榜首。QAT 配置/无损/2x 的具体对照尚未读完。官方 Blog 日界与窗口相交；HF API 元信息和 commits 首次尝试超时，普通日期恢复待办仍在，不用日期含糊强行排除。拟 owner INFER-TENSORRT-LLM / AGENT-TOOL-CALLING；评分待命题收窄与日期恢复。原文完整说明见 nov07-core2.txt。
2. [Shrinking the Variance v1](https://arxiv.org/abs/2511.03710v1)：完整 v1 题摘已读。原有低 rollout 预算下 per-prompt sample mean 噪声较大 -> 原文以双层 leave-one-out 的跨 prompt shrinkage baseline 改善估计 -> 应重新考虑“不用 critic 就只能采用独立组均值”的估计器选择。拟 owner TRAIN-GRPO，拟 2+1+2=5，须核理论 score-function 简化、独立性与实验条件，不照录普适方差优越性。初步核心方法已定位，不算标准完成。submitted `2025-11-05T18:43:15Z` 不是 public；DataCite v1 Updated `2025-11-06T02:01:22Z`、DOI created `2025-11-06T03:02:47Z` 仅日期恢复线索，尚待官方公告/首公开上下界核实。原题摘 nov07-first-v1.txt，方法 nov07-calibration-core.txt。
3. [Learning Without Critics? v1](https://arxiv.org/abs/2511.03527v1)：完整 v1 题摘已读。原有 GRPO 省 critic 的 LLM 经验容易被外推 -> 经典单任务控制消融显示长时序/不相关 episode grouping 下 critic-free 劣化，并提供 gamma/group-size 的局部条件 -> 应重新考虑组内比较何时能承担长程信用分配。局部负证据有准入价值，不要求证明 LLM 上普遍失败。拟 owner TRAIN-GRPO，拟 2+1+2=5；方法/等预算对照尚待审阅。submitted `2025-11-05T15:01:32Z` 不是 public，公告恢复普通待办。原题摘 nov07-first-v1.txt。
4. [SnapStream v1](https://arxiv.org/abs/2511.03092v1)：完整 v1 题摘已读。KV 压缩论文的算法收益与 static graph/continuous batching 部署之间存在接口压力 -> 原文称 dataflow accelerator 上部署稀疏 KV 并保留推理评价 -> 应核具体固定形状、缓存选择和端到端性能的共存边界。拟 owner INFER-KV-CACHE，拟 2+2+2=6。只核这条原文增量，不因“production”字样提高分数；最新 v6 不能替代 v1。submitted `2025-11-05T00:38:31Z` 不是 public，公告恢复普通待办。原题摘 nov07-first-v1.txt。

## 代表性负侧与纠错侧

- [RAGBoost 2511.03475v1](https://arxiv.org/abs/2511.03475v1)：题摘本来显示有具体 context reuse/quality 取舍，不能按“缓存是成熟原则”关闭。但是原页警示 newer version withdrawn；定点打开 [v2](https://arxiv.org/abs/2511.03475v2)，作者明确 `The paper is no longer valid and the contents will be fused to another different paper`。旧 v1 的采用链路不得在此时建立，不评分、不进 Books；v3/v4 不回填本日。此为纠错信号排除项，须非作者检查。原始记录 nov07-date-and-correction.txt。
- [DS-STAR 11/06 官方博客](https://research.google/blog/ds-star-a-state-of-the-art-versatile-data-science-agent/)：核心说明完整已读，file analyzer/router 局部消融具有潜在贡献，不能按“多 Agent 组合”直接排除。定点身份核对发现正文已有 arXiv:2509.21825，v1 09/26、v2 09/29、v3 10/02，博客中 leaderboard 依据为09/18；本窗博客没有指出相对该已公开正文的机制/证据新增。作为窗外首公开家族线索，不作为当窗新论文，不扩扫9/10月。仅在 root 指出博客独有实质 delta 时重开对照，原始记录 nov07-core2.txt、nov07-date-and-correction.txt。
- [Kimi K2 Turbo API 价格调整](https://platform.kimi.com/blog)：11/06 同目录条目。已读[官方论坛完整说明](https://forum.moonshot.ai/t/an-update-on-new-k2-models-and-new-pricing/104)：输入重、速度敏感的 coding 使用是定价理由，没有披露支撑降价的新算法、资源测量或等条件质量/成本对照。关闭商业价格事件的贡献判断，不将公告价格当作硬件效率。论坛原字段 `created_at=2025-11-07T03:27:30.356Z` 在本窗外，正文价格生效日 `November 6, 2025` 不等于首次公开时刻；仅作定点身份与理由支持。原始 JSON kimi-forum-104.json。
- [AI progress and recommendations](https://openai.com/index/ai-progress-and-recommendations/)：搜索已返回核心公开说明；方向/政策愿景未呈现可支持的新机制或评价，不进入候选。日期时区未核实，不为不影响准入的日期继续追查。搜索输出 nov07-search1.txt。
- [CARMA 2511.03102](https://arxiv.org/abs/2511.03102)：宽查询中完整摘要可见，为阿拉伯语心理健康 Reddit 数据/分类应用，未改变模型/系统主线机制；停止，不构造 Data owner 缺口。
- [Multi-Objective Adaptive Rate Limiting in Microservices 2511.03279v1](https://arxiv.org/abs/2511.03279v1)：完整题摘已读（arxiv-topic1.xml）。原文是一般微服务 API 限流，使用 DQN/A3C 在 Kubernetes 控制吞吐/延迟；没有披露大模型计算、模型状态或生命周期特有压力，也没有改变模型学习/优化的基本机制。排除依据为范围，不是“RL/限流成熟”；不将作者吞吐/P99/生产部署数字当作已经验证。日期未恢复，不影响该范围处置。

## 已执行边界与普通待办

14 每日来源入口已实际打开，不等于历史覆盖完成。Hunyuan 浏览器初始化一次超时，官方 publicList 有限 fallback 返回9个2026条目，不能证明2025历史Research无遗漏。Seed 2025 两个 article_type=1/2 均已实际读取 page_token=0、20；page20 的非置顶条目已早于本窗，has_more=true/next_page_token=40 保留，不继续翻到全年末尾。文件名 papers/blog 不代表参数语义，原始标题与返回类型才是依据；置顶穿插保留。arXiv 初个184条宽查询停止，没有把它变为全文队列；后续 inference/decoding/KV cache/reinforcement learning 的4分类窄查询，提交恢复区间11/04 19Z～11/05 19Z，start=0/max=30，返回21条，分页已尽，但非本窗 public 完整性证明。两条补检也已取得：模型/Agent 题名主题4分类 start=0/max=100 共61条；多模态/kernel主题8分类 start=0/max=50 共13条，均分页已尽，目前只是身份浏览，未把全部条目转为题摘/全文待办。完整查询保留于 Atom feed 原字段。跨查询去重后只对语义相关或含糊项读题摘；最新摘要不是历史 v1。cs.LG 宽月标题页仅用于定位，show=200无效已纠正为合法25/2000；2000响应超时且无日级公告，不能计已完成覆盖。

普通待办：其余每日源有限历史恢复；已取得的窄 arXiv 模型/Agent、多模态/kernel 身份中语义相关项的题摘初筛；本批首公开归属；校准后的候选标准/深入审阅与 Books 具体覆盖比较；非作者校准/日级复核。没有把这些待办改称外部终态保留项。

当前精确停点：校准前继续无关来源初筛与日期身份恢复，不先授予本批 Books 结论。Kimi 官方论坛指向 https://x.com/Kimi_Moonshot/status/1986449512538513505 ，实际打开为403；论坛本身公开时间在窗外，不能用它或推导的 Snowflake 时刻替代该公告的可读公开证据。arXiv 常规公告 schedule、Atom submitted/published 与 DataCite 记录时间均不能单独补造本日精确公开时刻；继续有限官方历史公告/公开上下界恢复。其他来源动态历史目录的缺口仍待有限恢复，尚未统一标为外部终态。

Books 限制：不是名称/算法名未见即产生缺口。只在证据独立核验后比较现有 owner 的具体论点与必要相邻交接；只有明确长期命题差额才请求 root 写入。已有覆盖或仅报告同样有效，作者没有共享 Books 写权。

请 root 优先校准4个拟准入命题、RAGBoost撤回处置、DS-STAR事件去重理由，以及经典控制负证据是否误关。校准通过后可继续未受影响的来源初筛；需要Books时由作者只提供具体命题/差额/位置，root协调实际写入及非写入者POST。

## root 独立复核反馈

复核者：独立智能体root，非本报告作者；实际核验反馈经用户转达，不记作人类原文阅读。本次实际核验范围：Shrinking the Variance、Learning Without Critics、SnapStream 三篇 exact-v1 完整题摘；RAGBoost v2 撤回声明；Kimi 当前原模型卡 QAT 核心及评价设置；DS-STAR 官方原博客。

结论：4项具体准入方向可以继续必要证据审阅；这是准入校准，不是日期、日级或 Books 完成。

- Learning Without Critics 保留经典控制的 task/group 与 LLM 训练不同，负证据不得外推为 LLM 上普遍失败。
- RAGBoost 撤回排除通过，不采用 v1、不评分、不进 Books。
- DS-STAR 同已公开家族且本窗博客无新增机制，可按事件去重继续；保留博客本身未披露新差额的依据。博客的 file analyzer/router 和已有消融不是本窗首次公开证明。
- Kimi QAT 的主 owner 应由 training QAT/低精度机制或通用 memory/runtime 的具体命题决定，不因可以部署到 TensorRT 就路由框架章。原先拟 INFER-TENSORRT-LLM 只是作者待核路径，不是已确认 owner，现已重开该路由。长程工具只采用真实控制或质量/成本差额，不将模型榜首外推为 runtime 保证。
- 日期继续逐项恢复原始证据；当前仍不把4项计为全部确认落窗的候选分母。原拟 2+1+2 等评分无需为了处置强改，待实际拟支持命题与证据边界确定后填写正式报告。

可执行停点更新：首批4项可继续必要方法/对照/限制审阅；并行意义上的其他来源初筛与有限日期恢复继续。Books 具体论点比较、root 协调写入及非写入者 POST 尚未完成，不能从本次准入通过推出已整合。
