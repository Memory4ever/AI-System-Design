# 2025-11-04 首批独立准入复核

复核者：Codex（独立复核 lane，非作者）；作者：Carver。author != reviewer。

检查时间：2026-10-04T16:24:18+08:00，工具实际 clock 为 2026-10-04 08:24:18 UTC。

结论：**首批五家族准入/代表性关闭校准通过**。IndQA 准入与官方 RSS 落窗字段通过；AWS 合作贡献关闭通过；三篇 exact-v1 的潜在方向通过，日期仍保留。不授 Evidence/Books/日级完成，不冻结全日候选。

## 1. 实际范围

按 04 fresh 重读 AGENTS、当前三合同、每日/按需/arXiv 来源说明、CODEX_RESEARCH_PROMPT、ROADMAP 与相关 checkpoint（仅路由）。窗口为 BJT `[2025-11-03T09:00:00+08:00,2025-11-04T09:00:00+08:00)`。

以 [FIRST_CALIBRATION_READY](./FIRST_CALIBRATION_READY.md) 为请求，亲读 [两篇官方核心原记录](./RAW_FIRST_CORE.json)、[三篇精确 v1 完整题摘与版本历史](./RAW_THREE_FULL_AB_DATE.json)，并定点打开对应五个 primary 原页核身份与当前说明。不是只读作者摘要。官方网页 native 获取 403 的两次不当缺失证明；web 原页可读，保留此传输差异。

结构化解析 [保存的官方 RSS](./openai-rss.xml) 1245 items，并本次 live GET 同一官方 RSS 得到 HTTP200、1245 items，核 title/link/guid/pubDate 对应对象；只判这两个指定事件，没有把 RSS 库存变题摘队列。收到的 RSS 时刻不是午夜占位值，也不是 submitted 或一般 schedule。其权限是官方事件发布字段，不额外宣称完整历史删除/版本追踪已证明。

## 2. IndQA：准入与日期通过

原源：[Introducing IndQA](https://openai.com/index/introducing-indqa/)。保存记录与 live 核心位置：How it works 48–51 行、How we built 54–58 行、Improvements/Caveats 64–70 行。

RSS 同一事件 `pubDate=Mon, 03 Nov 2025 22:30:00 GMT`，BJT `2025-11-04T06:30:00+08:00`，落窗；原页 November 3 的日精度与 UTC 事件日期相容，不把日精度独自补成时刻。当前页面未见本项纠错/撤回/重要修订说明；未遍历完整版本史，不认证原页不可变。

准入链成立：翻译题/饱和多语榜单难以代表本地语境 → 原生专家题目、逐题 rubric，且题目不配对并按指定模型失败筛选 → 必须重新限定跨语言及跨模型比较的解释。`2+1+2=5` 可沿用；贡献是具体评价协议边界，不是题目数量、地区名称或机构声望。ROADMAP 路由到 `PLATFORM-EVALUATION-SYSTEM`（Ch66）合理，但本轮未核具体 Books Existing 或差额。

必要限定：

- 不同语言的题目不同，平均分不是配对语言能力比较；本地题目可以继续有价值，不等于所有既有多语 benchmark 无效。
- 筛题涉及 GPT-4o/o3/GPT-4.5 与部分 GPT-5，可能影响 GPT-5 相对表现并使 OpenAI 与其他模型族比较不对称。不能直接外推通用模型排名、普遍文化能力，亦不能假定其偏差一定朝某个方向或某个幅度。
- 每题 criteria 有权重，model grader 汇总满足 criteria 的分值。原页没有给本项 grader 的精确模型/提示/version 与一致性检验；不认证人审等价、judge 无偏或统一成本收益。
- 本项核心没有链接可核的 IndQA 发布 artifact；MMMLU 是旧对照，不能顶替本次题库/实现。若只采用原页明确的构造与比较限制，不要求复现所有题目或找不到可选实现就永久阻塞。

Carver 可继续必要标准审阅和具体 owner 对读。若采用定量排名、grader 有效性或与现有 Books 冲突的更强命题，需相应证据/受影响内容深入审阅，不能靠本次准入通过升级。作者收益声明与 reviewer 限定分开。

## 3. AWS：代表性贡献关闭通过

原源：[AWS and OpenAI announce multi-year strategic partnership](https://openai.com/index/aws-and-openai-partnership/)。实际 Key takeaways 与部署核心 24–39 行已读。RSS `Mon, 03 Nov 2025 06:00:00 GMT`，BJT 11/03 14:00，事件落窗，但日期不使其自动成为研究候选。

正文确实说明 EC2 UltraServers、GB200/GB300 同网、训练/推理负载和容量承诺；当前没有新执行/通信协议、可归因的质量-资源取舍或新的失效/可靠性条件。low-latency 与规模措辞不能认证机制增量。按已读具体贡献关闭，不评分、不进 Books；不否认商业/部署意义，也不为未披露技术猜测展开 AWS 全库。

## 4. 三篇 exact-v1：潜在贡献通过，日期不通过

亲读完整题摘及 exact-v1 页面身份/历史；不是用当前 v2/v3 摘要替代旧稿。没有已显示的撤回/纠错说明，未遍历所有版本。

| 精确家族 | 可继续核验的潜在贡献 | 必须保留的边界 |
| --- | --- | --- |
| [Interact-RAG 2510.27566v1](https://arxiv.org/abs/2510.27566v1) | 黑盒 query-only 限制动作面 → Corpus Interaction Engine 的细粒度动作与轨迹 SFT/RL → 检索控制界面与训练策略的分工值得核验。不是只换 RAG 任务。 | 六 benchmark 宣称不足以归因动作接口；后续核 action primitives、query-only 与训练/预算对照。v2/v3 为 2026，不由后来 OpenReview 稿补历史证据。 |
| [TetraJet-v2 2510.27527v1](https://arxiv.org/abs/2510.27527v1) | FP4 权重震荡/outlier 失真 → double-block quantization、OsciReset、OutControl → 低精度训练稳定性与精度取舍值得核验。 | 标题的“-v2”是方法名，当前审的是 arXiv v1；不是一项已证明的本窗重要修订。370M/200B token 不使机制无价值；平均 gap reduction 51.3% 不是 51.3% 加速/成本下降，也不认证所有算子/状态都 FP4。 |
| [EBT-Policy 2510.27545v1](https://arxiv.org/abs/2510.27545v1) | learned scalar energy 与动作迭代优化、uncertainty-aware compute → 值得核行为克隆下 recovery 与分布偏移条件，不按普通机器人应用关闭。 | scalar energy 不自动是校准的不确定性或安全分数；部分任务 two vs 100 steps 不认证 50x 端到端加速。BC 下未显式 retry training 的恢复不等任意失败恢复、真机安全或内部推理归因。 |

原字段仅保留提交事件：Interact-RAG `2025-10-31T15:48:43Z`；TetraJet `14:57:16Z`；EBT `15:21:05Z`。三者不能凭 submitted、October ID、DataCite registered 或一般公告 schedule 授 04 首公开。三项不评分、不计确定候选；此次通过仅为贡献潜力校准，不是标准/深入审阅完成。

另实际读 [作者仓库早公开声明原记录](./RAW_DATE_RECOVERY_END.json)：TetraJet 当前 README 称 `(2025/10) We released the first version ... on arXiv`，同时列 2026/05 updated version。这个 primary 回顾性声明必须保留，不能让 11/03 DOI 注册覆盖它；其月精度与是否把 submission 称 release 仍不足以定位真实首公开事件。当前保持日期冲突/未定比直接授 04 或把 submission 当 October public 更准确。没有必要为这项恢复整月、全部 commits 或先读全文。

## 5. 给 Carver / root 的后续范围

本次没有要求改判上述五家族的筛选理由。Carver 可复用首批校准，继续 IndQA 受限证据与具体 owner 对读，以及尚未完成的来源/报告工作；本轮不代作者推进这些工作。

三篇日期层继续独立处理：已有可用入口有限恢复结束后，可作为具名终态保留隔离，不用于正面证据、Books、无遗漏或性能/安全保证；只在精确 v1 与实际首公开上下界可核且完全落窗时定点重开。不是永久全篇深审待办，也不能因日期缺口关闭贡献。作者现有精确重开条目可保留，本次未全量验收其恢复过程。

当前漏斗是：首批检查 5 家族；1 个有官方落窗字段且准入通过；1 个贡献关闭；3 个有潜力但日期未定。不是 4 个确定候选，也不是全日冻结分母。

未检查范围：14 来源最终 Coverage、所有负侧/纠错信号、Google Suncatcher/Cloud 的新增边界、三论文完整方法/实验/代码、IndQA grader/artifact、最终 Books Existing/POST 与六部分日级语义。本次不重复 07 SECOND8 校准，不借 13 或其他日期候选补 04。

本次当前 04 进行中报告 validator 实际通过，仅接口检查，非日级验收。只新增此 notes，不改报告、Books/state/index，不 stage/commit/push。
