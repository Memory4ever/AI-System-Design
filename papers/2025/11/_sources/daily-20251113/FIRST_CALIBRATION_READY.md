# 11/13 首批准入校准 ready

作者：nov13–18 lane；请求 root/非作者仅校准下列拟准入与代表性关闭，未作独立通过声明。窗口 BJT [2025-11-12 09, 2025-11-13 09)。

## 原入口与边界

- arXiv 主线首查发生日期范围解析异常：`raw-arxiv-api-core.xml` 返回 total=28897，未继续分页或展开其100条全文；`raw-arxiv-api-core-narrow.xml` 是第一次收窄原返回。
- 修复使用14位时间字段，官方规范化为12位：`submittedDate:[20251110190000 TO 20251111185959] AND (cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AI) AND (ti:"language model" OR ti:LLM OR ti:transformer OR ti:agent)`；start=0,max_results=100，total=92，92标题实际浏览。修复原返回 `raw-arxiv-api-core-repair.xml`。按主线语义选择以下8份完整题摘，不把92标题变全量题摘/全文队列。其余潜在相关标题仍是普通有界初筛待办，不是关闭。
- 月度 `cs.CL` 标题页已取，只作指定提交/公开边界附近查漏，不据此遍历全月；具体补检仍待做。`raw-arxiv-cl-month.html`。
- 公开时间不由 submittedDate 授予；Orion DataCite v1 Submitted=2025-11-10T19:49:55Z，Updated=2025-11-12T01:05:29Z，created=2025-11-12T02:49:07Z，registered=2025-11-12T02:49:08Z，Available=2025-11。此前提出的“正常公告下界 + DOI注册上界”不是已核实公开区间：常规 schedule 不能补造本篇首公开时刻，DOI注册与公开正文的对应仍需核实。OAI datestamp=2025-11-12 也只有日期精度。保留原字段，请 root 独立核这组证据是否足以给出完全落窗的真实上下界；未解决者不进正式§3，不据此否定贡献或扩成全日全文队列。

## 首批完整题摘与拟准入

原文全标题与完整摘要在修复XML各精确ID的 `<title>/<summary>`，本批8项均已实际读完；官方abs/core与信号核查见 `raw-web-06/07/09.json`。API给最新版本的条目不代替精确v1。

| ID / 精确原源 | 原有判断 → 本文实际增量 → 需要重考的选择 | 拟评分 / 最低投入 | 当前边界 |
| --- | --- | --- | --- |
| [2511.07555v1 LLM Optimization Unlocks Real-Time Pairwise Reranking](https://arxiv.org/abs/2511.07555v1) | pairwise rerank耗时限制在线使用 → 多种局部优化的组合及Recall@k损失证据 → 是否可用小模型/单向排序/输出约束满足给定质量延迟目标；不因优化成熟就关闭其新局部测量 | 1+2+2=5；标准 | 166x跨组合不能归因单机制；硬件、candidate数与端到端成本待核 |
| [2511.07568v1 Procedural Knowledge Improves Agentic LLM Workflows](https://arxiv.org/abs/2511.07568v1) | 自由agent依靠隐式规划 → 同任务手写/LLM生成HTN及模型规模对照 → 何种显式过程知识能代替更大模型；局部能力差额而非发明HTN | 1+2+2=5；标准 | 任务分布/HTN人工预算/先验信息公平性待核 |
| [2511.07572v1 SCALAR: Benchmarking SAE Interaction Sparsity in Toy LLMs](https://arxiv.org/abs/2511.07572v1) | 单层feature稀疏不等于跨层circuit稀疏 → SCALAR度量和共享权重Staircase SAE消融 → 是否用单层解释指标选择跨层解释器 | 2+1+2=5；标准 | 216K toy/GPT2-small局部实验，不按小模型排除；泛化待核 |
| [2511.07581v1 Think Before You Retrieve: Learning Test-Time Adaptive Search with Small Language Models](https://arxiv.org/abs/2511.07581v1) | static rewrite不能随证据迭代 → Orion小模型轨迹SFT/RL与beam搜索 → retrieval策略学习与模型规模预算如何选择 | 2+2+2=6；标准 | 只采用局部检索策略/质量成本对照，不把200–400x模型规模当吞吐收益 |
| [2511.07585v1 LLM Output Drift: Cross-Provider Validation & Mitigation for Financial Workflows](https://arxiv.org/abs/2511.07585v1) | temperature=0/seed常被当输出复现保证 → 480 runs中跨任务/服务的重复输出测量 → 是否需绑定运行路径和task invariant验证；负面结果可准入 | 2+2+2=6；标准 | 不采用“大模型导致不确定性”因果结论；不同模型/运行后端混杂待核，法律映射不进入项目 |
| [2511.07637v1 Private-RAG: Answering Multiple Queries with LLMs while Keeping Your Data Private](https://arxiv.org/abs/2511.07637v1) | single-query DP无法直接支持持续RAG服务 → individual privacy filter按document检索频次累计及私有threshold → 多query下隐私/效用的控制边界 | 2+2+3=7；深入 | 文档邻接、组成定理、threshold自身费用待核；不把epsilon≈10称普遍安全 |
| [2511.07685v1 ResearchRubrics: A Benchmark of Prompts and Rubrics For Evaluating Deep Research Agents](https://arxiv.org/abs/2511.07685v1) | 长答案多解难按单一reference打分 → expert fine-grained rubric与隐含context/推理失败分解 → 是否用事实检索成功替代完整research质量验收 | 2+2+2=6；标准 | rubric/evaluator一致性和各agent运行budget待核；不是因新增benchmark而准入 |

## 代表性负侧写

1. [2511.07641v1 LLMs vs. Traditional Sentiment Tools in Psychology: An Evaluation on Belgian-Dutch Narratives](https://arxiv.org/abs/2511.07641v1)：完整摘要读完。25000 responses/102 participants、3 Dutch微调LLM在自评valence上的应用对照，Pattern优于LLM。拟关闭原因是**当前题摘只给特定心理学测量任务指标，没有揭示foundation model评估/训练机制新条件或可直接改变本项目的评价接口**，不是因为负面、小模型或未读实验；若root认为任务定义/label mismatch本身已构成主线新边界，应定点重开方法/评价，不把关闭当独立通过。官方页未见撤回/纠错标签；日期未作为关闭必要事实，不另无限恢复。
2. [OpenAI Neuro客户案例](https://openai.com/index/neurogum/)：retail adoption与business结果，未提供模型训练/推理/agent新机制或评价条件，范围/贡献关闭；仅检索发现说明，不算完整研究审阅。
3. [Anthropic Agent Skills webinar](https://www.anthropic.com/webinars/agent-skills-transform-claude-from-assistant-to-specialized-agent)：活动描述和既有Skills演示，不因有“架构”术语纳入；没有新变更/评估命题。先关闭活动说明，不能证明录制内容无研究增量。原字段11/12 10:00 PT不作本窗论文候选。

## 继续工作与交接

root 已实际读取 repair.xml 中8份完整题摘及首批校准文件，确认7项的具体增量可继续必要审阅；sentiment application当前关闭可继续，未否定负证据价值。Output Drift必须检查相同backend/重复条件，不能把模型与服务路径共同变化归因规模。Private-RAG机制准入可，7分中的Durability=3暂未证明，按稳定DP机制实际差额核后再定，不能计借用的成熟DP原则。日期只授予逐项核验路径：2025历史官方公告、精确v1、官方当日list身份、公告后的DOI registered共同构成完全落窗range才可采用；一般schedule或单DataCite不够。该批是独立准入校准，不是日期、证据、Books或日级完成。Project Fetch及追加5篇尚未获这次校准。

首批校准已获root，必要作者审阅见EVIDENCE_NOTES.md；未校准追加拟准入不展开深审。GPT-5.1日期/具体准入待核；OpenAI RSS原字段为Nov12 00:00 GMT，与实际发布时刻不能直接等同。Hunyuan browser有限三次尝试（timeout；subagent不支持IAB visibility；无visibility重试timeout）后按用户给出的publicList实际请求成功，但9项2026 blog目录不是历史Research论文覆盖，必须保留缺口，不再重复空浏览器路径。Seed type1/type2各p0及p20实际取得，pinned与has_more保留；p20未置顶段已跨到6月及更早，按窗口边界停止，不继续p40。

## 补交：真实落窗材料与身份纠错

- 拟准入 [Project Fetch: Can Claude train a robot dog?](https://www.anthropic.com/research/project-fetch-robot-dog)。官方 Research 原始 hydration 的该 slug 对应 `publishedOn=2025-11-12T18:19:00.000Z`，即 BJT11/13 02:19，实际字段落窗，不靠 schedule；`raw-anthropic.html` 和 `raw-web-16.json` 可复核。核心说明已读；拟评分1+2+2=5，标准。原有“编程辅助收益可作为自主硬件能力代理”的判断 → 一次两队各4人的随机分组实验显示连接/传感接口收益但未完成自主取球，且有阶段控制器不均、对照获提示等混杂 → 应分开测量接口接入 uplift 与自主闭环成功。采用只限本实验，不声称普遍两倍加速、生产安全或未来自主能力。请校准这条局部评价边界是否值得准入，不能仅因涉及机器人就关闭，也不因节点缺少 Project Fetch 名称就提出Books整合。
- 代表性身份纠错：[JAX Privacy 1.0](https://github.com/google-deepmind/jax_privacy/releases/tag/v1.0.0) 官方 artifact `published_at=2025-07-10T15:34:35Z`；`raw-jax-privacy-releases.json`。11/12博客不能当1.0首发，release已有DP-SGD/DP-FTRL/accounting等内容。当前拟关闭“11月新release”命题，博客若有独立机制差额才定点重开，不扫描7月报告或JAX runtime全站。此项属于表外artifact身份支持，不冒充SRC-JAX执行语义发布已检查。
- 后续窄主题6份精确v1题摘实际读完，原文在 `raw-exact-ab-2511-07776v1.json` 及逐篇HTML；STeP、Autospeculation、HipKittens、Dynamic Sparsity、跨模态组合仍待贡献裁决/补交校准；3D4D摘要是4D可视化/交互框架说明，未明确action-conditioned transition或新的生成机制，拟定点核核心模块而不凭World Model名称准入。未把6项授候选或Books差额。

本文件保留初始请求与root实际校准，不是候选冻结或Evidence/Books通过。实际Books写入0；当前V3六部分README已形成进行中稿，单项Project Fetch独立审阅ready及新增方向分别见PROJECT_FETCH_READY.md/NARROW_CALIBRATION_READY.md。余宽标题不变全量题摘，日期未闭合材料隔离，不授日级完成。
