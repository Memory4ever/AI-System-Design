# 2026-04-01 V3 定点重审 checkpoint

检查时间：2026-09-25～26（Asia/Shanghai）。本文件是过程材料，不是已完成的日报或独立复核。原 V2.1 正文、516 条 owner-replay identity 与 exact-v1 缓存均保留；下表不继承旧 `deep_complete`、评分或 Books `No Change`。

## 机构来源停点补审（2026-09-26）

- Qwen 官网 Research 前端合并 `GET https://qwen.ai/api/page_config?code=research.research-list`（旧静态 60 条，均早于 2026）和 `GET https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US`（动态 40 条）。后者 `extra.date` 在目标窗口邻域由 2026-03-30T04:00+08 跳到 2026-04-02T04:00+08；两组官网列表无本窗条目。此结论仅限官网所列研究，不能排除作者单独投 arXiv 的稿件。
- Seed 官方论文目录 `GET https://seed.bytedance.com/api/get_article_list_v2`，请求头 `x-tt-locale: US`、`article_type=1,count=20,order_desc=true,page_token` 分页；总数 242。页 40 邻域 04-07→03-31 20:00 北京时间→03-25。本窗列出 TDDFT 分子计算 `2603.29257v1`，属于暂缓的 AI for Science，不进入本项目候选分母。官网 Research Blog 的 Foundation、Visual、Audio、AI Infra、Frontier 分类均有跨窗日期停点，见当日日报来源表。
- Moonshot 官方 Kimi Platform Blog 最新可见 2025-11-07；`MoonshotAI/kimi-cli` 1.28.0 release 于 03-30T15:15Z，1.29.0 于 04-01T14:06Z，均非本窗；UTC 03-31～04-01 邻域 17 条 commit 仅作为局部 CLI 改动发现线索，不用 committer date 判首次发布。
- 百度 ERNIE Blog 04-15→02-06、MiMo 官网 Paper 06-29→03-13、MiniMax 英文研究博客 05-26→03-18/中文博客 04-27→03-18，均有跨窗停点。MiniMax CLI 最近邻 release 04-01T09:03Z，晚于本窗 01:00Z 截点。MiMo Blog 无可靠单篇日期，不能从未注明日期推断无新稿；作者稿另由 arXiv 路由。
- OpenAI Research index 首屏停于 2026-08-18，`Load more` 历史分页未得到可核验停点；官方 News RSS 可读但不是 Research 的替代。Meta Research 入口公开 HTML 为空，Meta Blog 可见 04-08→03-26，不能据 Blog 断言 Research 零命中。两项目前为**精确来源覆盖缺口**，不是用户材料 blocker，也不得静默标为已检查。

## exact-v1 PDF 版本污染抽检（2026-09-26）

鉴于相邻日期曾发现 arXiv HTML `/v1` 首页与 PDF v1 不一致，定点打开本日拟整合的八份官方 PDF v1，而非无差别重读 516 项。下列结论仅确认这些关键命题的 PDF v1 存在且与日报所据机制一致，不能替代日级候选漏收复核：

| Source Family / PDF v1 | 核对命题 | 结果 |
| --- | --- | --- |
| [CRAFT 2603.28768v1](https://arxiv.org/pdf/2603.28768v1) | 按层 expert replica 边际收益、显存与 KV 并发竞争 | PDF §1、§5.3 明示，未见此命题的 HTML 后版污染。PDF 页脚日期不作为首次公告时间。 |
| [OptiMer 2603.28858v1](https://arxiv.org/pdf/2603.28858v1) | 各域 CPT 向量后验组合，15–35× 只指作者搜索成本对照 | PDF 摘要、§5–6 对齐。 |
| [LLM Memory Pipeline 2603.29002v1](https://arxiv.org/pdf/2603.29002v1) | Prepare/Compute Relevancy/Retrieval/Apply 四阶段与异构放置 | PDF 摘要及 §1 对齐，GPU–FPGA 测试仍是受限设备案例。 |
| [FlexMem 2603.29252v1](https://arxiv.org/pdf/2603.29252v1) | clip 的 Context Memory 与 Local Memory 派生、bank 写入与条件读回 | PDF 图 2、§3.3 对齐，不等于精确原始 KV 复用。 |
| [Single-Vector Retrieval 2603.29519v1](https://arxiv.org/pdf/2603.29519v1) | domain shift、relevance metric 错位与单/多向量条件比较 | PDF §3 明示；仍不能泛化为所有向量检索失效。 |
| [Video-Oasis 2603.29616v1](https://arxiv.org/pdf/2603.29616v1) | 视觉/时序输入必要性与 benchmark shortcut | PDF v1 可读；日报沿用 v1 口径，不引用后版 55% 作为 v1 数字。 |
| [DUME 2603.29765v1](https://arxiv.org/pdf/2603.29765v1) | 非 MLP 合并、域特征统计、闭式 router 初始化 | PDF §3 对齐；深层 feature 分布偏差仍保留。 |
| [ShapE-GRPO 2603.29871v1](https://arxiv.org/pdf/2603.29871v1) | 单回答内候选集合的 Shapley marginal credit | PDF §3–4 对齐，仅限作者特定集合 reward。 |

## 独立反向抽检触发的分母调整（2026-09-26）

- [SLVMEval `2603.29186v1`](https://arxiv.org/pdf/2603.29186v1) 从旧 516 条标题关闭侧恢复。exact-v1 摘要及 §3–4 构造 10 类视频质量/文图一致性受控退化配对，五名标注者筛出人可辨差异；§6 对自动评价器按退化类型与视频时长作 meta-evaluation，人工配对正确率 84.7%–96.8%，受测自动系统九类弱于人工。Appendix K 明说合成退化分布和强度不能代表未来真实生成错误。它对 `PLATFORM-EVALUATION-SYSTEM` Ch66 的增量是：长视频生成 evaluator 准入不能只依短视频指标或视频理解输入消融，还须测试长度/退化条件下的最低辨别力。`2+2+2=6`；确认现有章节缺口后按研究合同深审 override，由主任务在 Ch66 Video-Oasis 段后写入。[arXiv OAI](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2603.29186&metadataPrefix=arXiv) 的 `created=2026-03-31`、`updated=2026-04-01`、当前 datestamp `2026-04-01`，DataCite initial `created=2026-04-01T02:04:56Z`；连同官方公告规则支持本日 08:00～09:00 北京时间批次归属，但后二者都不是单篇精确公开时刻。HTML/PDF v1 页脚的 03-31 是稿件日期，不代替首公告。
- [ASI-Evolve `2603.29640v1`](https://arxiv.org/html/2603.29640v1) 从工作候选降为**前分母关闭**。其 Researcher 提议、Engineer 实验、Analyzer 反馈、Cognition/database 保留经验的循环可作为 AI-for-AI 受限实现，但 `AGENT-WORKFLOW` Ch81 已具体持有 proposal→实验执行→evaluator→反馈/记忆→下一轮设计以及 holdout/provenance 边界；作者 judge fitness、任务域与不同框架停止条件不一致，未给独立可迁移新机制或反证。不能仅因模型/数据/算法实验都与 AI 相关就准入。原全文审阅保留于本 checkpoint，移出日报候选与评分并非删除证据。
- 本轮一进一出，**工作分母净仍 20**，但旧 `19/15`、`+6−4−1` 仅是早期工作账本，不作为最终冻结候选公式。最终分母须由独立复核检查两侧反例与来源停点后确认。

### `2603.29693v1` — 有贡献线索，但版本/出处隔离

[arXiv abs](https://arxiv.org/abs/2603.29693) 记 v1 提交 2026-03-31T12:48:42Z、v2 2026-04-16、v3 2026-07-08；[官方 PDF v1](https://arxiv.org/pdf/2603.29693v1) 与 HTML v1 的参考文献 [12] 均写 `Accessed: 9 Septembre 2026`，晚于上述所有版本日期；v2/v3 PDF 仍保留这一字段。未见作者勘误或版本来源解释。它可能是手误，不能据此称整篇论文伪造，但不能把该版本的出处与时间无条件当已核准。

题摘和 §2–4 确实提出超出泛化“置信度校准”的两条 measurement 区分：先用 type-1 task sensitivity `d′` 控制主任务难度，再比较 confidence discrimination/meta-`d′`；风险条件下的自发 decision criterion shift 与模型事后给出的 confidence rating 是不同被测行为。实验限 GPT-5、DeepSeek-V3.2-Exp、Mistral-Medium-2508 和三个二选一任务，五级 confidence 与 risk prompt；不能外推开放式长回答、事实引用或生产拒答。Ch66 已有 calibration、risk–coverage 和 confidence sensor，但未显式固定 type-1 能力归一化及风险决策 criterion。由于上述日期出处异常，本轮状态 `Disputed`、**不进冻结候选、不评分、不写 Books、不作正面长期证据**；等待作者可核勘误或版本解释后只重开该家族。

## 窗口与日期依据

- 本窗：`[2026-03-31T09:00:00+08:00, 2026-04-01T09:00:00+08:00)`。
- [arXiv 官方说明](https://info.arxiv.org/help/availability.html)称 ID 在首次公告时分配，取首次公告的月份；常规周二 20:00 ET 公告，2026-03-31 20:00 EDT 对应北京时间 2026-04-01 08:00。`abs` 中的 `[v1] Submitted` 是提交时间，不是公开时间。
- [arXiv OAI `2603.28766`](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2603.28766&metadataPrefix=arXiv) 的未修订 datestamp 为 `2026-03-31`；相邻 [OAI `2603.28769`](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2603.28769&metadataPrefix=arXiv) 与 [OAI `2603.28795`](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2603.28795&metadataPrefix=arXiv) 的未修订 datestamp 为 `2026-04-01`；高位 [OAI `2603.30016`](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2603.30016&metadataPrefix=arXiv) 同为 `2026-04-01`。
- [DataCite `2603.28767`](https://api.datacite.org/dois/10.48550/arxiv.2603.28767) 的 initial `created=2026-03-31T03:52:00Z`，[`2603.28768`](https://api.datacite.org/dois/10.48550/arxiv.2603.28768) 则为 `2026-04-01T01:55:08Z`，`28769` 紧接 `01:55:10Z`。这是相邻 ID 的跨批次边界线索，不等同 DOI 登记就是公开时间；已修订 paper 的当前 OAI datestamp 也不能反推 v1 公告日。
- 本次补回的四篇也落在同一有界批次：DataCite initial created 分别为 [`2603.28858` 01:57:17Z](https://api.datacite.org/dois/10.48550/arxiv.2603.28858)、[`2603.29252` 02:06:29Z](https://api.datacite.org/dois/10.48550/arxiv.2603.29252)、[`2603.29519` 02:12:49Z](https://api.datacite.org/dois/10.48550/arxiv.2603.29519)、[`2603.29616` 02:15:07Z](https://api.datacite.org/dois/10.48550/arxiv.2603.29616)，均在 2026-04-01 UTC。未修订的 29252/29519 的 arXiv OAI datestamp 同为 `2026-04-01`；28858/29616 已修订，当前 OAI datestamp 跟随后版，不用于 v1 归属。四条仍只可写“**由官方公告规则+相邻 ID/OAI+批次 DOI 有界推定 04-01 08:00～09:00 北京时间**”，不能伪造单篇精确公开分秒。
- 旧 `daily-20260401/inventory.json` 的 513 条按 v1 **提交**时间取窗，含 `2604.*` ID，不能作本窗公开事件分母。旧 `arxiv-owner-replay-20260903/20260401/arxiv-owner-receipt.json` 的 516 条按 DOI created 批次取窗，具备较强日期交叉证据，仍需独立检查窗口边界及候选漏收。

## 旧 34 项候选的题摘重审（未冻结新分母）

状态含义：`保留待证据` 只表示题摘提出值得核验的具体项目增量；`定点判定` 是准入理由仍需读关键段；`前分母关闭` 不评分、不全文审阅。日期归属另由上节交叉证据处理。所有题摘来自原始 arXiv identity 缓存，对机制与实验尚未作 V3 完成声明。

| arXiv ID | 初筛状态 | 项目相关的具体理由或关闭理由 |
| --- | --- | --- |
| 2603.28768 | 保留待证据 | MoE expert replica 的层级边际收益与显存预算共同决定 placement；需核对与 Ch21 已有 replica/quantize 路线的差异。 |
| 2603.28769 | 定点判定 | Spark 分布式评估、统计检验和内容寻址缓存的组合；需确认是否超出已有 Evaluation evidence contract，而不因使用 Spark 准入。 |
| 2603.28780 | 前分母关闭 | Byzantine 容错的通用异构分布训练，题摘未证明与大模型训练拓扑/状态合同相关的新边界。 |
| 2603.28781 | 保留待证据 | GPU 脱附时 metrics 消失/监控 payload 完整性而非数值异常成为故障信号，可能修正 Ch67 的 sensor-missing 判定。 |
| 2603.28793 | 前分母关闭 | 跨厂商 ISA 原语综述，题摘没有带出模型/训练/推理的具体新设计选择。 |
| 2603.28795 | 保留待证据 | 按输出 step 验证与局部修补，区别于 whole-response 与 KV cache；需验明任务验证器、污染传播和回退界限。 |
| 2603.28815 | 定点判定 | Agent skill paired utility/security test 若确有可复算 release gate 新合同才准入；评分标签本身不足。 |
| 2603.28823 | 保留待证据 | 固定 wall-clock 与 consumer GPU 的选型最优点不等于固定 FLOPs 最优点，需核验对照范围与公式外推。 |
| 2603.28887 | 定点判定 | Occupancy world model 脱离连续驾驶日志生成长序列；需辨别是通用 action-conditioned state 机制，还是专属道路资产模拟。 |
| 2603.28963 | 定点判定 | LiDAR occupancy 原始感知驱动交通代理；需辨别是否改变 world-model state/agent control 责任，还是汽车仿真局部指标。 |
| 2603.28988 | 保留待证据 | 将训练与 release claim 加密绑定第三方 weights/adapter/data/build artifact，涉及平台 artifact provenance 与执行 gate。 |
| 2603.29002 | 保留待证据 | 将稀疏注意力、RAG、压缩 memory 归入可测四阶段处理流水线，若 profiling 成立可能改变异构执行计划。 |
| 2603.29010 | 保留待证据 | Kernel Agent 的 DSL 抽象与硬件上界同时约束搜索预算，需检验正确性/benchmark gaming guard 及所测 kernel 合同。 |
| 2603.29020 | 保留待证据 | Web Agent 任务实例化、失败处理与标注口径可改变与既有成功率的比较有效性；不能只沿用作者对其他产品的差值。 |
| 2603.29090 | 定点判定 | Object slot、分层时序和因果图组合需证明超出已知模块拼装；单一 PushT 数据与 kernel microbenchmark 不足通用 World Model 结论。 |
| 2603.29122 | 前分母关闭 | LLM-oriented logging 的反馈式生成主要是通用软件调试；题摘未给出本项目监控/发布控制合同的独立新增边界。 |
| 2603.29193 | 前分母关闭 | 长对话压缩的 importance/coherence/budget 模块属已知方法组合；题摘未定位新记忆所有权或失效条件。 |
| 2603.29194 | 前分母关闭 | Working/episodic/semantic 三层记忆与门控是已知分层；单一对话任务指标不能改变现有记忆设计结论。 |
| 2603.29231 | 保留待证据 | 长任务跨重复运行的 reliability decay 与 meltdown onset 改变 pass@1 评价合同；需核实统计和任务分布。 |
| 2603.29235 | 保留待证据 | 训练 OS→GPU→network 连续跨层诊断及观测开销权衡可能改变平台 Trace/Monitoring 的根因定位路径。 |
| 2603.29357 | 保留待证据 | 用 benchmark score spectrum 的有效维度判别多指标冗余，可能改变 evaluation coverage inference；需检查 population dependence。 |
| 2603.29399 | 保留待证据 | 审计 ELT Agent benchmark 的评价错误可能纠正能力结论；需确认原 task、数据和修正后的独立复测。 |
| 2603.29403 | 定点判定 | LLM-as-judge security SoK 的 taxonomy 有用，但若只是既有攻击分类综述、不解决新证据分歧则不入选。 |
| 2603.29493 | 定点判定 | Agent memory 操作训练与推理统一框架：需检查 memory state/version/evaluation contract 是否真有新机制，不能因框架集成入选。 |
| 2603.29494 | 保留待证据 | Video attention 的 vector-wise sparse pattern 若经质量/吞吐对照成立，可能改变稀疏粒度与缓存/计算选择。 |
| 2603.29559 | 前分母关闭 | 教育自动评分的 confidence calibration 属局部领域评测；题摘未证明可迁移至通用 LLM judge/release gate。 |
| 2603.29640 | 定点判定 | AI-for-AI research loop 涉及训练架构与算法搜索，但需解开 evaluator leakage、独立 holdout 及已有 Agent workflow 内容；不纳入 AI for Science 部分。 |
| 2603.29665 | 保留待证据 | Agent policy 仅凭最终状态会漏掉未执行检查但偶然正确的 near miss，可能改变 workflow audit event 与 release gate。 |
| 2603.29678 | 保留待证据 | Agent trace 的 lossless IR 与多视图索引可能改变长轨迹可观测/检索的证据边界。 |
| 2603.29765 | 定点判定 | 不训练直接组合专用 dense experts，需核实跨域保真与加入新专家时模型接口、路由和回归，而非只看局部得分。 |
| 2603.29844 | 保留待证据 | VLA 用 latent intent 隔开 VLM 高层决策与低层动作，可触及动作状态和控制频率责任；需核实 sim-to-real 与实验范围。 |
| 2603.29848 | 前分母关闭 | AgentFixer 将既有规则/LLM judge 和根因分析整合成诊断工具，题摘没有单独的新控制/证据合同。 |
| 2603.29919 | 保留待证据 | Skill 路由与正文分层压缩，并校验 faithfulness，可能改变 Agent Context 的加载预算/质量取舍。 |
| 2603.30016 | 前分母关闭 | 间接提示注入的系统级立场论文主要陈述既有防线和未来议程，题摘无新可验证机制或反证。 |

当前 34 项中：保留待证据 17、定点判定 9、前分母关闭 8。此数只对应旧表 34 条，不是新的冻结分母；尚需对原 516 条关闭集做误排抽检，并处理 13 个机构来源。上述 `前分母关闭` 仅初步审查，独立复核未通过前不从旧日报删除原证据。

### 题摘准入第二轮：旧分母不再默认继承（2026-09-26）

第二轮使用可追溯的 exact-v1 摘要定点校正旧缓存；下表只决定是否值得进入本项目候选分母，**不等于全文审阅或 Books 决策**。尤其 `2603.28963` 的旧缓存标题/摘要属于后续版本，v1 应以[原始摘要](https://arxiv.org/abs/2603.28963v1)为准；`2603.29418` 也有同类标题变化。

| ID | 第二轮准入 | 具体原因与后续责任 |
| --- | --- | --- |
| `2603.28769` | 前分母关闭 | Spark、统计检验与内容缓存是已有评估构件的实现组合；题摘未提出会改变 Evaluation 的样本、判定或发布合同的新约束。 |
| `2603.28815` | 前分母关闭 | Skill utility/security 的配对检查与既有能力—风险双轨评价同向；单篇框架若未改变授权或发布 gate，不因安全主题自动入选。 |
| `2603.28887` | 保留待证据 | [OccSim v1](https://arxiv.org/html/2603.28887v1)明确把 action-conditioned 静态占据状态与动态交通代理拆开，针对长时空间持久性而非仅视频画质；需审其道路几何假设和非驾驶外推界限。 |
| `2603.28963` | 前分母关闭 | [AutoWorld v1](https://arxiv.org/abs/2603.28963v1)着重以无标签 LiDAR 改善道路交通仿真和 WOSAC realism，感知上下文虽有价值，但题摘未建立超出驾驶领域的 AI System 状态/控制 owner 新判断。不能使用旧缓存的 v2 式“lossy trajectory”叙述替代 v1。 |
| `2603.28988` | 前分母关闭 | [Attestation gate v1](https://arxiv.org/abs/2603.28988v1)提出 claims-to-controls 映射与 **evaluation blueprint**，自己说明尚待完整研究论文；无已执行的机制或对现有 artifact provenance/release gate 的反证。可保留为背景，不作为已证实候选。 |
| `2603.29090` | 前分母关闭 | 分层对象状态、因果图与 PushT 单域验证尚不足以改变 Ch25 的 world-state owner 或可控性边界，属具体架构组合。 |
| `2603.29403` | 前分母关闭 | LLM judge security taxonomy/综述是已知攻击面整理，不构成新防护或评价判定机制。 |
| `2603.29493` | 前分母关闭 | Agent memory 统一训练/推理框架的题摘没有呈现超出既有 memory identity、读取、修订与持久化主线的必要新增合同。 |
| `2603.29640` | 保留待证据 | [ASI-Evolve v1](https://arxiv.org/abs/2603.29640v1)将 AI 模型/数据/算法的实验结果持续写入 cognition base 并反馈下一轮设计，属于 AI-for-AI workflow；作者的大幅 benchmark 改善需查泄漏、控制组与独立 holdout，不能直接进 Books。 |
| `2603.29765` | 保留待证据 | [DUME v1](https://arxiv.org/abs/2603.29765v1)用闭式 ridge regression 将独立 dense experts 无额外训练地接成动态 MoE；若新增专家与跨域能力真的保持，改变模型组合/训练成本边界，须核其接口兼容及干扰实验。 |
| `2603.29292` | 前分母关闭 | ConSelf 的 semantic entropy 和行为共识针对无 test oracle 的代码生成自训练；题摘只给代码任务内的 curriculum/preference proxy，没有证据足以改写通用后训练证据合同。若后续独立审阅找到跨任务反例可重开。 |
| `2603.29418` | 前分母关闭 | [v1](https://arxiv.org/abs/2603.29418v1)为多模态视觉提示注入的一种隐蔽扰动/叠字攻击；不可信图像可携带指令的授权边界在 Books 已有，题摘未显示新的系统 owner 或防线失效类别。 |

第二轮暂得旧 34 中 **19 保留、15 前分母关闭**；再加从旧 516 关闭集中明确恢复的 OptiMer、FlexMem、single-vector retrieval、Video-Oasis 四项，形成 **23 项待证据与独立准入复核**的工作分母，非最终冻结候选数。旧 34 的 ELT-Bench-Verified 暂保留：它纠正同一 Agent benchmark 的 rigid evaluator/ground truth 错误，可能直接改变能力结论；这是具体 evaluation contract 问题，不因 ELT 领域名而自动排除。四项恢复不能直接挪用旧 `No Change`，实际 Book 增量由 owner 章节对照决定。

## 已完成的 exact-v1 来源小批次：机制、实验证据与边界

以下只表示三篇单项 primary-source 审阅完成；未代表当日 Coverage、分母或 Books Gate 完成。arXiv HTML 顶部的 `v1 Submitted` 也不作为当窗首次公开日。

### 2603.28768v1 — CRAFT

- **来源和版本**：[exact-v1 HTML](https://arxiv.org/html/2603.28768v1)，访问日 2026-09-25。v1 标题为 *CRAFT: Cost-Aware Expert Replica Allocation with Fine-Grained Layerwise Estimations*；后续版本标题或措辞不能倒灌到 v1。
- **为什么旧方案合理**：Expert Parallelism 通过专家放置分散热点；极端偏斜时放置仍无法拆开同一热专家，因此 EPLB 统一给层分配副本。这简化容量规划、每 GPU 内存一致，但副本挤占 KV。
- **机制与状态责任**：CRAFT 离线收集每层专家负载，回放不同副本数的平衡收益，以固定副本/显存预算做 multiple-choice knapsack 的动态规划，再用交错分配与贪心放置保持每 GPU expert capacity 接近。Router 不变；它改变的是 **deployment epoch 的 replica 数和专家放置**，并间接改变可用于 KV cache 的容量。文中明确指出：同一 DP rank 中最小 KV 容量设备约束并发，因而不能只优化专家平衡度。
- **实验合同**：作者在 AWS p4de.24xlarge（8×NVIDIA A100 80 GB/节点、NVLink、EFA、CUDA 12.8、NCCL 2.26.2）使用 BF16 DeepSeek-R1-671B 与 Kimi-K2-1000B、top-8 routing、输入截断 4096、固定输出 256。主要比较为 SGLang v0.4.8 的 EPLB 放置无副本、均匀副本和 CRAFT；部署同时用 DP、head-parallel TP-attention、EP、mixed chunked prefill 最大 4096。Goodput 定义为不进入长队列前可持续吞吐，报告吞吐—TTFT 曲线及 ITL；请求并发和生产 SLO 未作跨系统通用披露。
- **证明与未证明**：作者在 8 节点这些设置下报告相对 EPLB，CRA8 的 DeepSeek-R1 goodput 平均 1.15×（最高 1.2×）、Kimi-K2 平均 1.12×（最高 1.17×），副本少约 7.25/7.5 倍。结果支持这些 workload 的“按层边际收益换 KV 空间”取舍，不证明所有 MoE、动态负载漂移或生产 SLO 下普适收益。离线画像可能过时；重规划/迁移会有额外成本。均匀副本在负载稳定、显存宽裕、追求简单控制路径时仍合理。
- **Books 对照/暂定 disposition**：`MODEL-MOE` Ch21 已写 router、placement/replication 责任分离以及 replica/quantize 的内存预算，但尚缺 **按层边际收益—每设备 expert capacity—KV 并发** 的连续约束链。主任务已将该机制增量合入 `books/part-02-model/21-moe.md` 现有论证（2026-09-25 工作树，未提交）；待本日公告归属与最终候选独立复核后，日报才可记录最终 `Integrate`，绝不能因此标整日报 Complete。

### 2603.28781v1 — When GPUs Fail Quietly

- **来源和版本**：[exact-v1 HTML](https://arxiv.org/html/2603.28781v1)，访问日 2026-09-25。
- **问题与机制**：常规 GPU 温度/功率/利用率监控把缺值当单纯数据质量问题，但 GPU 脱附可能没有稳定数值前兆。作者将 GPU、监控管道和 OS 三个特征平面放在同一节点时间线上，识别 scrape 样本数塌缩、设备指标消失、scrape gap；这不等同“数值预测了硬件故障”，而是将 **观测通道完整性** 纳入被监控状态。
- **实验合同与证据边界**：作者的 GWDG 事故目录有 69 条 GPU 类记录，仅 15 条有完整对齐 telemetry；脱附子集 7 条跨 3 个节点，仅 5 条可处理，另 2 条缺 tidy archive。operator 事件日可能是发现日，不是故障瞬间；`t0` 以 scrape payload collapse 对齐。10 分钟原生采样、60 分钟特征窗/10 分钟 stride、1% 固定告警预算和 48-window lookback 下，对弱事件代理做 GPU-only 与 joint-plane 比较；joint Isolation Forest 的平均提前量 7 窗，相对 GPU-only 2 窗，但中位数仅 1.5 窗，且 17 段告警有碎片化 triage 成本。弱事件由 signature 高于 0.99 分位且至少 3 连续窗构造，**并不代表脱附故障**；五个脱附 case 的证据主要是事故锚定的 forensic 对齐，非稳健的前瞻性预测试验。作者也列出 slice 节点/GPU 覆盖、完整缺失统计和 detector 超参数等尚未导出字段。
- **演进/失效边界**：稳定数值传感器仍适用于温漂；观测塌缩可提示“硬件掉线或 exporter/网络损坏”，必须通过节点日志/健康检查交叉区分，不能仅凭缺值诊断具体根因。
- **Books 对照/暂定 disposition**：`PLATFORM-MONITORING` Ch67 已明示 missing signal 与零值不同；本文可作为该既有命题的有限案例，但样本和标签不足以改变书稿结论。倾向 `No Change — Existing Coverage`，由主任务最终判定。

### 2603.28795v1 — StepCache

- **来源和版本**：[exact-v1 HTML](https://arxiv.org/html/2603.28795v1)，访问日 2026-09-25。
- **为什么旧方案合理及新机制**：whole-response cache 高效但约束微调后会复用错误答案，KV cache 则属于模型内部序列状态，不是跨请求答案逻辑复用。StepCache 在 OpenAI-compatible API 前缓存输出 step，取相似先例后逐 step 做任务校验；语义状态改变或大量不一致时整答再生成，否则仅重生失败的连续块，再做 stitched final check。数学任务若有界修补仍失败会用解析方程的确定性求解兜底，因此所谓 correctness 不能归因于“缓存机制本身保证通用正确”。状态 owner 是外部 response cache/验证器，非 KV 或模型权重。
- **实验合同与证明边界**：薄 Python 层、FAISS 与 MiniLM embeddings，后端 Qwen2.5-3B；CPU-only 的线性方程/JSON 两类微基准，各 10 个 base prompt、每扰动 3 变体，每 seed 222 请求、3 seeds。作者报告平均延迟 2.13→0.67 秒，p95 3.38→3.30 秒，总 token 36.1k→27.3k，quality/final-check 72.5%→100%，但这些是任务专用 rule check + deterministic math fallback 下的作者结果。GPU/并发、长输出、真实用户 trace、SLO 与 cache poisoning 尚未测试；`keys_change` 100% 走 patch，`value_change` 100% skip reuse。尾延迟几乎不降，说明 slow path 仍主导。
- **Books 对照/暂定 disposition**：`AGENT-WORKFLOW` Ch81 已讨论带前置条件的部分产物复用和最终验收；此 paper 使边界更清楚，但实验仅限极小、易验证任务。倾向 `No Change — Existing Coverage` 或仅在该章证据区作受限例证；不应将 CPU microbenchmark 写成通用推理 serving 提速结论。

## 旧 516 条关闭集的反向抽检：发现误排风险

已按 arXiv ID 顺序读完旧 owner receipt 中 516 条 **title**，并先对与 ROADMAP 主线最相关的已排除条目复读其原始摘要；这不是宣称 516 条 exact-v1 摘要和公开时间全部复核完成。旧 receipt 的 title/abstract 可能随版本变化，不能代替事件时 v1。例如 `2603.29616` 旧缓存写 **55%**，但 [v1 页面](https://arxiv.org/abs/2603.29616v1) 摘要写 **54%**；`2603.29418` 旧缓存标题也不是 [v1 标题](https://arxiv.org/abs/2603.29418v1)。以下事件仍需与公告批次核对，不凭 v1 Submitted 或 DOI created 单独定 owner。

| 原关闭 family | V3 准入重审 | 与项目的具体潜在增量和待核问题 |
| --- | --- | --- |
| [2603.28858v1](https://arxiv.org/abs/2603.28858v1) OptiMer | 拟补入候选 | CPT 的数据混合比例由预训练前固定搜索转为每数据集独立训练、参数分布向量后验组合搜索；改变选择时点和重训/存储成本，需查方法与 Gemma 3 27B 实验是否把向量合成与重新混合真正公平比较。 |
| [2603.29252v1](https://arxiv.org/abs/2603.29252v1) FlexMem | 拟补入候选 | 长视频 visual KV 不全部留在 prompt，而按双通道压缩写入/任务相关读取；可能改变多模态状态所有权与显存边界。`infinite lengths` 是作者表述，实验证据最多为两模型、五长视频+一流视频任务、单 RTX 3090 的有限条件。 |
| [2603.29519v1](https://arxiv.org/abs/2603.29519v1) Single-Vector Embeddings | 拟补入候选 | 与 RAG 检索设计直接相关：单向量退化未必由维度导致，domain shift、相似度与任务 relevance 错位和文档量增大均是边界；需验证 LIMIT/MSMARCO 评价及 multi-vector 比较，不能把 toy 推导外推为所有 embedding。 |
| [2603.29616v1](https://arxiv.org/abs/2603.29616v1) Video-Oasis | 拟补入候选 | 不再单看视频问答总分，而分离视觉/时序输入与语言先验 shortcut；v1 作者称 54% 样本可不靠视觉或时序解题，需核 benchmark 集合、过滤和 chance baseline，可能收窄多模态评价合同。 |
| [2603.29292v1](https://arxiv.org/abs/2603.29292v1) ConSelf | 定点判定 | 以生成程序的行为分歧构造语义不确定度和 curriculum，再以行为共识给 DPO pair 加权，可能改变无 oracle 自训练的 reward/proxy 责任；需核查是否只是代码任务局部方法，以及无 test oracle 时何以测定语义行为一致。 |
| [2603.29418v1](https://arxiv.org/abs/2603.29418v1) Visual Prompt Injection | 定点判定 | v1 标题是 *Adversarial Prompt Injection Attack on Multimodal Large Language Models*。不可见视觉扰动+文字覆盖能否改变平台对不可信图像的安全边界，需检查攻击权限、黑盒闭源目标、任务、可感知阈值和现有防线；不能因又有一个注入技巧就准入。 |

旧 `516→34` 的分母不能沿用。当前小批次至少有四项明确的可能漏收，尚未完成证据/Books 审阅及独立准入复核；其余高相关关闭集还需定点抽检。原有排除行不删除，最终若恢复需保存 `old closure → V3 retained` 的改判理由。

## 第二小批次：旧关闭集 exact-v1 复核与章节对照

以下四条确为旧 `516→34` 关闭集中的误排风险，但本段只完成正文机制与受限实验证据；首次公告批次、其余候选和独立复核仍待闭合。四条均不因题目匹配而自动进入最终分母。

- **OptiMer `2603.28858v1`**：[原始全文](https://arxiv.org/html/2603.28858v1)，访问日 2026-09-25。固定数据混合比的 CPT 每次试错要重新训练；作者先从同一 PT base 分别在每个分布上做 CPT，形成参数增量 `τ_i=θ_CPT_i−θ_PT`，将 IT 向量与若干分布向量加权合成，再在 development set 上以 TPE 搜索合成权重。由此把“训练前决定数据比”变成“训练后先试合成权重”，但并非无需训练：各分布模型仍须先完整训练，模型合并也会出现干扰和额外权重存储。Gemma-3-27B-PT 的日语/中文/数学/代码各 1B token CPT，8×H200 141GB、BF16、ZeRO-3、4096 token，100 次 TPE trial，搜索时各 proxy task 前 100 样本、top-3 再用前 300；作者报告 15–35× 是**搜索成本**对比，不是端到端 CPT 成本。更重要的是同一 dev set 驱动权重搜索，最终结论仍需独立 holdout 和不同 domain shift 检查。`TRAIN-DATA` Ch27 已解释 mixture/数据身份，`TRAIN-PRETRAINING` Ch28 已解释在线计划与预算，但尚未论证“预先混合训练 ↔ 先训练分布向量、后验选择”这个条件分支；Books 若吸收应由 Ch28 解释控制权与额外训练/合并成本，Ch27 只短 handoff。
- **FlexMem `2603.29252v1`**：[原始全文](https://arxiv.org/html/2603.29252v1)，访问日 2026-09-25。把长视频全部帧一次塞入模型在 token/KV 容量上有上限；作者逐 clip 编码视觉 KV，双通道筛选用于传播近期历史的 context memory `C` 与写入可检索 memory bank 的长期片段 `M`，问答时按 query 再读必要片段。这里 memory bank 是推理外层的压缩视觉状态，并非改变基础 KV cache 的精确复用身份；所谓“无限长度”仅指分段迭代的理论接口，不能推出无损回忆或无限资源。两种 LLaVA 系模型、五类长视频与一类 streaming benchmark，512/1024 均匀采样帧、最终 decode token 13k/7k、K=3 visual cache layers、k=5 索引特征；单 RTX 3090 24GB 的受限比较支持容量收益，但没有生产并发、尾延迟和长期 stale-memory 证据。`MULTIMODAL-REPRESENTATION` Ch23 已有长视频 token/事件表示和 shortcut；若吸收应补“视觉 KV 到可修订压缩 memory 的读写身份”，而不是在 `INFER-KV-CACHE` Ch45 重写一套泛化 KV 结论。短视频完全可装入窗口时，直接编码仍是简单有效的基线。
- **Single-vector retrieval `2603.29519v1`**：[原始全文](https://arxiv.org/html/2603.29519v1)，访问日 2026-09-25。单向量 ANN 使召回成本低，但把查询和文档的多关系压成一个相似度。作者反驳“维度不够就是主因”：top-k 表示存在低维充分构造，而 LIMIT 类数据上控制 tokenizer 后单向量仍差；重要压力是 domain shift、余弦 proxy 与任务 relevance 错位以及大库中的噪声近邻淹没。原始实验比较 Qwen3-Embedding-0.6B 的 1024 维单向量与 GTE-ModernColBERT-v1 的 128 维多向量，并在 LIMIT 变体/MSMARCO 看微调与遗忘；作者报告 LIMIT 微调后单向量在 MSMARCO 下降超过 40%，只能作为其训练/测试配置的迁移风险。数学 toy 模型说明机制，不证明所有语料/索引的退化率。`AGENT-RAG` Ch76 已有单/多向量质量-执行成本取舍，但缺“relevance proxy/迁移/规模导致同一相似度失效”的成因链；应在既有段内 refine，而非添加论文独立小节。单向量在稳定、低成本、高吞吐检索仍有正当性。
- **Video-Oasis `2603.29616v1`**：[原始全文](https://arxiv.org/html/2603.29616v1)，访问日 2026-09-25。视频问答高分可能来自问题语言、音频、单帧或无序帧；作者对 14 个 benchmark 的 24,416 条 QA 依次做 blind/audio/narrative/center-frame/frame shuffle/bag-of-frames 消融，并用三模型严格一致阈值标记 shortcut，剩余 11,332 QA / 5,199 videos。v1 的摘要写 **54%** 原题不需要完整视觉/时序证据；不能引用旧缓存后来修订版 55%。不同消融并非正交，`k≥1` 宽松阈值曾给 92.7% 而 `k=3` 给出较保守过滤，说明数字受定义强烈影响；模型原 benchmark 比较最多 128 帧、1fps。该证据支持“测模态能力须有必要性干预”，不证明其剩余集就是视频真值或模型内部因果理解。`MULTIMODAL-REPRESENTATION` Ch23 已写 temporal shortcut/成对干预；`PLATFORM-EVALUATION-SYSTEM` Ch66 更适合承载多基准诊断协议、阈值与发布分数边界。应先核 Ch66 是否已有同命题，再决定 No Change 或紧凑 refine。

### 第三小批次：训练预算、异构执行和 kernel 搜索（2026-09-26）

- **Time is Not Compute `2603.28823v1`**：[原始全文](https://arxiv.org/html/2603.28823v1)。固定 FLOPs 下的最优模型规模没有计入固定硬件的 tokens/s 随模型变化；作者把自变量改为实际训练时长，报告 5 分钟～24 小时的质量—规模 U 型变化。然而其 8×RTX4090 是 **8 个独立单卡实验**，不是一个 8 卡训练任务；50M～1.03B 参数、48M FineWeb-Edu unique tokens、512 序列长度、70+ runs。48M 数据在小模型上被重复到数百轮，故长预算的左侧变差是数据重复/过拟合，不能推出“所有大模型时间最优幂律都是 0.60”。作者自己列出单 GPU 类型、有限 seeds、无多卡、数据量小等限制；不同硬件或大数据集会改变该指数，且论文所比 Chinchilla 的 FLOPs 预算不是同一约束。`TRAIN-PRETRAINING` Ch28 已有 `Scaling 不是只增加参数` 与 Unique Data/Repetition 分账，主任务已独立对照，判 `No Change — Existing Coverage`；本论文作为 4090 小规模受限例证，不改书稿通用结论。
- **Memory Processing Pipeline `2603.29002v1`**：[原始全文](https://arxiv.org/html/2603.29002v1)。作者将 long-context sparse attention、RAG、compressed memory 的输入处理拆成 prepare → relevance score → retrieval → apply；这里的 memory 是供生成使用的**处理后信息**，不等于只指设备 RAM/KV。各阶段计算密度和访问模式不同，因此其 GPU–FPGA 设计把稀疏、非规则、memory-bound 的检索相关核迁到 FPGA，密集模型算子留 GPU，但产生 PCIe 搬运与自定义 kernel 维护成本。作者在 AMD MI210 + Alveo U55C 同机与同型号 GPU baseline 上测试 sparse attention/RAG/MemAgent/Memory-as-Context：memory-processing 占其所测端到端延迟 22–97%，不同负载端到端提速 1.04–2.2×、能量下降 1.11–4.7×；RAG 示例用 Llama 2 7B 或 Llama 3.1 8B，不是统一模型/输入合同。A100+U55C 没有同机实测，附录用分部量测估计；“未来硬件都应 FPGA offload”仍是作者推断。长上下文/检索步骤跨越 Attention runtime 与外部 RAG，初步 owner 指向 `INFER-TENSORRT-LLM` Ch49 的执行计划而非将所有 memory 混为 KV；Books 决定待主任务与 Ch49、Ch76 现文对照。
- **GPU Kernel Agent DSL/SOL `2603.29010v1`**：[原始全文](https://arxiv.org/html/2603.29010v1)。旧 kernel agent 直接搜索 CUDA/CUTLASS，候选空间和正确性 harness 的漏洞消耗迭代预算。作者给 Agent 一个较窄的 µCUTLASS DSL，并用硬件 `speed-of-light` (SOL) 估算做问题级搜索预算、近似性能上界和过快候选的可疑信号；低于 bound 10% 的结果被标记供进一步检查，**不是**数学上已证明作弊。H100 SM90a 锁时钟，基于 Qwen2.5-7B/Mistral-7B/Phi-3.5-mini/Mamba/RWKV profiling 选 KernelBench 250 中 59 项，三档 GPT 模型，Nsight Compute 只计 GPU kernel 时间，不计 launch、Python、host 同步或服务端 SLO。作者报告同迭代预算 GPT-5-mini baseline 为 0.40× PyTorch、DSL 达 1.27×、再加 SOL 达 1.56×；integrity filtering 缺失可把报告 speedup 虚高最多 1.9×，属于特定 harness 的风险。稳定增量是把“搜索自由度、测量上界与正确性检查”放在同一优化闭环；现有 `INFER-TENSORRT-LLM` Ch49/`PLATFORM-EVALUATION-SYSTEM` Ch66 的机制归属与是否已有此链仍待主任务对照，不能把 benchmark 的 kernel-only gain 外推为全服务收益。

### 机构来源的已核停止点（尚非 13/13 完成）

- [Google Research 2026 年 3 月归档](https://research.google/blog/2026/03/) 本窗邻域有两条 3 月 31 日博文：量子密码货币披露与本项目无关；[人类标注数量与 benchmark 可复现性](https://research.google/blog/building-better-ai-benchmarks-how-many-raters-are-enough/) 在主题上相关，但它链接的 [AAAI 正式论文](https://ojs.aaai.org/index.php/AAAI/article/view/39659) 已于 **2026-03-14** 发表。3 月 31 日博客是同一 Source Family 的后续解释，不能作为 4 月 1 日新研究重复入选；博客仅有日期、无时分，也不推断它必落本窗。[DeepMind Publications](https://deepmind.google/research/publications/) 当前有序列表由 2026-04-22 直接跨至 2026-03-22，未见本窗新增；该站称“selection”，所以不冒称覆盖全部 Google 作者论文，相关原始论文仍由 arXiv 路由补检。
- [Z.ai 研究页](https://www.zhipuai.cn/zh/research) 的 [GLM-5V-Turbo](https://www.zhipuai.cn/zh/research/156) 明示 `2026/04/01 16:00`，晚于本窗截止，留给 4 月 2 日，不算本窗发现。
- [ERNIE 官方博客](https://ernie.baidu.com/blog/zh/) 首屏日期从 4 月 15 日越至 2 月 6 日；[小米 MiMo](https://mimo.xiaomi.com/) Paper 段从 6 月 29 日越至 3 月 13 日；[MiniMax 英文博客](https://www.minimax.io/blog) 日期从 5 月 26 日越至 3 月 18 日：各自可对**该可见日期序列**记录无本窗新增，但其他官方 endpoint（仓库/中文页）尚未全检。
- [Seed Publications](https://seed.bytedance.com/en/public_papers) 的网页只显示 Page 1/13，不把其首屏无命中当作完成。2026-09-26 读取其前端使用的同站[官方列表接口](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&page_token=40&count=20&order_desc=true)：`article_type=1`、`page_token=40`、`count=20`、倒序，返回 14 篇 Publication、`next_page_token=60`、`total=242`，该页网站 `PublishDate` 从 2026-04-07 跨到 2026-03-25，故官网自己的发表序列无本窗新增。列表中的一条 2026-02-27 `PublishDate` 却链接 `2604.*` arXiv ID，说明站点日期不能替代论文首次公告；同名 arXiv family 仍按 arXiv 规则核。
- 主任务从混元官网前端 `index-CUQAWQeM.js` 定位其实际使用的[官方 publicList 接口](https://api.hunyuan.tencent.com/api/blog/publicList)：POST `{"pageNum":1,"pageSize":100,"renderType":0}`，返回 `totalNum=9`、`list=9`；`renderType=0` 为“全部”，1 为“研究”6 条、2 为“发布”3 条。`displayPublishTime` 为 Unix 秒，列表从 2026-04-30、04-23 直接跨至 02-13，故“全部”可见目录没有本窗条目。此结论只覆盖该官网目录，不能断言团队未列出任何作者论文。
- [Anthropic Research](https://www.anthropic.com/research) 的 HTML 内嵌有原站 `publishedOn` ISO 字段，不必依靠可见首屏 `See more`。窗口邻域检到唯一 `2026-03-31T22:17:00.000Z` → **2026-04-01T06:17:00+08:00**，slug `how-australia-uses-claude`，对应[澳大利亚 Claude 用量分析](https://www.anthropic.com/research/how-australia-uses-claude)。正文主要是地区采用率与用途分布，未改变模型、训练、推理、平台或 Agent 机制；本窗确有一条该入口研究记录，但因项目范围前分母关闭。同日政府 MOU 亦非机制研究。`publishedOn` 与 sitemap `lastmod` 不混用。
- [OpenAI 2026-03-31 融资声明](https://openai.com/index/accelerating-the-next-phase-ai/)是公司融资/算力战略，不给可检验的模型系统机制；仅为范围外发现线索，其日内时刻不影响排除。OpenAI Research index 仍须解决分页才能对到期来源下零命中结论。
- OpenAI、Anthropic、Meta、Qwen、腾讯混元等网页含分页或 JS 客户端目录；文本抽取看不到本窗条目**不等于**无更新。Seed 正式论文目录分页尚未走到 3 月，DeepSeek/Moonshot 其他 endpoint 也需补查；在此之前机构覆盖保持进行中。

| Daily Source ID | 本次实际可见的停止点 | 状态及不可越过的断言 |
| --- | --- | --- |
| `SRC-OPENAI` | [Research index](https://openai.com/research/index/) 仅首屏 7 卡至 2026-08-18，`Load more` 未能在本子任务浏览器展开；[Research overview](https://openai.com/research/) 可见相邻 03-05 与 04-23 模型卡；定点搜索找到 [03-31 融资公告](https://openai.com/index/accelerating-the-next-phase-ai/)，不属于研究候选。 | 未完成归档页翻页；不能写零命中。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) 原站 HTML 内嵌 `publishedOn` 历史序列，窗口 UTC 03-31 01:00～04-01 01:00 内检到一条 `03-31T22:17Z` / [how-australia-uses-claude](https://www.anthropic.com/research/how-australia-uses-claude)；此页不受当前首屏 `See more` 限制。 | 该入口本窗唯一可见命中属经济/采用率，范围外前分母关闭；不以 sitemap `lastmod` 计事件。 |
| `SRC-GOOGLE-AI` | [Google Research 03 月归档](https://research.google/blog/2026/03/) 与一项 [AAAI first-public 03-14](https://ojs.aaai.org/index.php/AAAI/article/view/39659) 的博客复述已审；[DeepMind Publications](https://deepmind.google/research/publications/) 有序列表 04-22 → 03-22 越窗。 | 两个发现入口已核窗口；DeepMind 自称精选目录，不能覆盖未列出的所有作者稿，但 arXiv 主线路由会做主题补检。 |
| `SRC-META-AI` | [Research](https://ai.meta.com/research/) 文本提取空；[AI at Meta Blog](https://ai.meta.com/blog/) 日期序列 04-08 → 03-26，研究 publication index 仍未逐窗核。 | Blog 可见序列无本窗条目，Research 空响应不能算无命中。 |
| `SRC-QWEN` | 注册的 [旧 Qwen 页](https://qwenlm.github.io/) 已重定向提示新 [Research](https://qwen.ai/research)；旧页可读条目只到 2025-09，新站文本提取空。 | 旧页不能代表 2026 窗口；新站需可读日期目录或定点官方条目。 |
| `SRC-DEEPSEEK` | [Research/news](https://www.deepseek.com/news/) 可见公告 04-24 → 2025-12-01、研究索引 06-24 → 02-25。 | 该两条有序可见列表无本窗新条目；无须把空档编造为研究事件。 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog) 当前首项仍为 2025-11-07；补充 GitHub 端尚未定点查。 | Blog 有序可见列表无本窗；整个 Source ID 仍未完全闭合。 |
| `SRC-TENCENT-HUNYUAN` | [Research](https://hunyuan.tencent.com/research) HTML 文本为空；主任务读取官网 JS 找到[官方 publicList 接口](https://api.hunyuan.tencent.com/api/blog/publicList)，POST `{"pageNum":1,"pageSize":100,"renderType":0}` 得 `9/9`，`displayPublishTime` 序列 04-23 → 02-13 越窗。 | 官网“全部”目录无本窗条目；不能扩展成所有作者论文无命中，论文主题线索仍由 arXiv 补检。 |
| `SRC-ZAI` | [Research](https://www.zhipuai.cn/zh/research) 有序 04-01 GLM-5V-Turbo → 03-15 GLM-5-Turbo；[04-01 原文](https://www.zhipuai.cn/zh/research/156) 精确到 16:00 北京时间，已越过本窗 09:00 截点。 | 本窗目录区间可核无新 research 条目；相关发布归 04-02。 |
| `SRC-BYTEDANCE-SEED` | [Publication index](https://seed.bytedance.com/en/public_papers) 首屏 `1–20/242`；其[官方分页接口 offset40](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&page_token=40&count=20&order_desc=true)在 `x-tt-locale: US` 下返回 `total=242,next_page_token=60`。页 40 序列 04-07 → **03-31T12:00Z** → 03-25：中间 [TDDFT 大型有机分子计算](https://arxiv.org/abs/2603.29257v1)在本窗官网 PublishDate 命中 1 条。 | 该条为材料计算/AI for Science 暂缓，前分母关闭；官网 PublishDate 不是 arXiv first-public。Research/Blog 补充入口待核，不能称 Publication 零原始命中。 |
| `SRC-BAIDU-ERNIE` | [Blog](https://ernie.baidu.com/blog/zh/) 日期 04-15 → 02-06 越窗；论文/仓库补充端未定点。 | Blog 可见序列无本窗；整个 Source ID 仍需确认论文端。 |
| `SRC-XIAOMI-MIMO` | [MiMo Paper/Blog](https://mimo.xiaomi.com/) Paper 日期 06-29 → 03-13 越窗；Blog 不完全有时间。 | Paper 段无本窗；Blog/仓库需定点。 |
| `SRC-MINIMAX` | [English Blog](https://www.minimax.io/blog) 日期 05-26 → 03-18 越窗；中文/Agent Blog 未定点。 | 英文博客无本窗；其他端待核。 |

上述表格不是“13 源已完成”收据，明确列出尚可执行部分。后续只按受影响入口补页/官方日期，不无差别重扫年度内容。

### 第四小批次：Agent 评价、训练跨层诊断与 benchmark 测量（2026-09-26）

- **Emergence WebVoyager `2603.29020v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29020v1) §3–5。旧 WebVoyager 的 643 个任务/15 站点便于可重复比较，却把 `start_url` 当成指定执行站点，硬编码日期随时间失效；不同团队对 CAPTCHA、站点故障、重试与人工/自动判定口径不同，原始总成功率不是单一能力测量。作者人工审查原任务后发布 535 个任务，加入指定站点、相对日期实例化、外部阻碍处理、可复核标注与报告协议；两名标注者的 agreement 为 95.9%。单独测 Operator 得 68.6%，原 OpenAI 报告的 87% 使用不同任务、执行地点及判定合同，**不可把差值写成同一模型退化**。新协议提高比较可解释性，但 live web 仍受地点、登录、反爬、页面版本和人工判定影响；离线封闭站点仍适合确定性回归。`PLATFORM-EVALUATION-SYSTEM` Ch66 已明确冻结 Agent tools/sandbox/environment/scorer、替代路径与动态环境，倾向 `No Change — Existing Coverage`，待独立者对其具体段落复核；该受限案例不单列新通用指标。
- **Beyond pass@1 `2603.29231v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29231v1) §3–7。作者把单次成功扩成按任务人类预估时长分层的重复成功 `pass^k`、部分完成 GDS、跨运行方差 VAF 和工具序列熵的 meltdown onset。396 任务＝三类（软件工程/Web 研究/文档处理）×四时长桶×33，10 个模型经 OpenRouter、温度 0.7、每任务模型三次、两种 scaffold、50-step 截止，共报告 23,392 episodes。结果说明在**其任务/供应商路由**中能力排序与长任务稳定性可倒置；但 `human duration` 与 Agent 实际步数不等，OpenRouter 不同模型走不同 provider，前期 quota/404 还会系统性选择偏差。论文把高 VAF 解释成能力签名以及“memory scaffold universally hurt”，仅能限定到所测模型、任务和特定简单记忆架构；不能推断生产应偏好高方差或所有外部记忆有害。Ch66 已明确 `Pass@k` 与 `Pass^k`、重复运行/环境/部分进度及分层 reliability profile，倾向 `No Change — Existing Coverage`，但本论文可作为错误相关性与时长代理失配的受限例证；是否补充这两个压力交主任务比较。
- **SysOM-AI `2603.29235v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29235v1) §2–5、§7。只看 GPU utilization 或 NCCL 慢 rank 时，NIC softirq、VFS 锁或数据读取的 CPU/OS 根因可能被误归于 GPU/网络。系统用每通信组相对 rank 的 CPU waterline 做层级差分，eBPF uprobes 观察 CUDA/NCCL，逐函数缓存 FP 可用性、必要时 DWARF unwind，Build-ID 对应的符号解析后移到中心；控制权仍是诊断提案，不自动修训练 job。作者报告阿里 80,000+ GPU 一年部署，半年 2,649 诊断事件中 94 件是确认的跨层 root-cause 事件；默认 99Hz tick/10% sampling 的 overhead **仅在** 2×A100 80GB、Llama-3.2-1B-Instruct、PyTorch 2.1/NCCL 2.18、seq 1500/batch 8、20 测量步上为 0.33%，不能把这个数或 10 分钟 median 扩为全 fleet SLO。FP-only→hybrid→完整符号的 frame accuracy 实验分别约 5/70/95%，是所测生产二进制。限制为 Linux eBPF、CUDA/NCCL/CPython 兼容性、少数慢 rank 假设；off-CPU blocking 和 RDMA 根因需额外 sensor。Ch67 已有 collective 低基数聚合→定点 trace 与旁路 sensor，但尚未见这条 **跨 rank 症状→CPU/GPU/OS 差分→栈可靠性→符号 provenance** 的连续诊断链；拟由主任务判断 `PLATFORM-MONITORING` Ch67 是否真正需要条件性整合。
- **BenchScope `2603.29357v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29357v1) §2–5、§10。多个 benchmark/category 名称不等于独立测量轴。作者对 item×model outcome 矩阵中心化后取谱 participation ratio `ED=(Σσ²)²/Σσ⁴`，配对相关与 leave-one-out 检查冗余；在其 Open LLM Leaderboard v2 的 4,576 模型×6 aggregate 上 ED≈1.66、BBH/MMLU-Pro Spearman ρ≈0.96；22 套 benchmark atlas 中，BFCL 的 20 类在 109 模型汇成约 7 组。该指标只是**给定模型群体和结果矩阵的筛查**：binary Pearson ED 会高估潜在维度约 1.5–8×；少模型/少任务受形状上界，限制模型群体时 BigCodeBench ED 从 29 降到 7；高相关不证明两个任务语义相同，低 ED 不能独自授权删测项。收益是把 suite 冗余与权重脆弱性可计算化，代价是持有版本化 item-level matrix、代表性模型群体、统计稳定性和补充构念判断。Ch66 已有多轴证据/相关性非因果原则，但未见明确的**人口条件下 suite 独立测量容量**审计。拟请主任务判断是否条件性整合到 `PLATFORM-EVALUATION-SYSTEM`，绝不写 ED 为能力维度真值。
- **ELT-Bench-Verified `2603.29399v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29399v1) §3–5、§7.4。作者针对 100 个 ELT 任务/203 数据模型中失败的 81 任务、136 数据模型、660 不匹配列，用 Claude Opus 4.5 辅助排查再由数据工程师归因，发现 218/660 列是 benchmark-attributable（含 156 评价误拒、32 模糊规格、30 ground-truth 错），不能把 82.7% `failed tasks contain ≥1 benchmark error` 误写成 82.7% Agent 成功。修正脚本和排除 30 个不可靠 GT 列后，**同一** SWE-Agent+Claude Sonnet 4.5 的 transformation pass 从 46/203（22.66%）到 66/203（32.51%）；ReAct+同模型也到 66/203，但通过的具体模型不同。50 列多人复核的高层归因 Fleiss κ=0.851，不是全 660 逐人一致；初始失败只来自一种 Agent，修正后仍 67.5% 数据模型失败。Ch66 已明确 scorer/reference artifact 先核、SQL set/multiset 与 ambiguous alternative valid paths，此文是局部实证纠偏，倾向 `No Change — Existing Coverage`；如主任务发现缺少“先分 agent error/benchmark error 再改分”的明确交接，可在既有评估段作小幅 refine，而非并排追加论文。

### 第五小批次：正确终态背后的策略缺口与轨迹视图（2026-09-26）

- **Near-Miss `2603.29665v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29665v1) §3–4、§6。只按最终数据库状态评价业务 Agent，可能把“未读前置状态但恰好没有违规”的 mutating action 记成成功；旧的 outcome checker 对终态仍必要，却无法证明执行时知晓 eligibility。作者把自然语言 policy 离线映射成工具前置 guard，并在离线轨迹审计时检查指定 read-only 状态是否**先于** mutating tool call 出现，同时允许等价的其他只读调用；因此评测状态分为 `最终状态正确/错误` 与 `关键前置证据确曾读取/未读`，不能只看最终动作。六种模型各在改造后的 τ²-verified Airlines 50 任务×4 次运行，作者报告涉及 mutating call 的轨迹有约 8–17% near miss；其分母不是所有任务，更不是生产事故率。实验额外加入两个原 benchmark 缺少的数据访问工具；guard 代码由 LLM 生成、部分人工验证且单一领域/政策集，遗漏的前置条件会漏报；论文仅**离线评价**，不证明在线守卫能阻断风险。`AGENT-TOOL-CALLING` Ch78 已要求 action 前读集/前提与提交端复核，且指出终态相同也可能掩盖中途越权；`PLATFORM-EVALUATION-SYSTEM` Ch66 已要求 trace 与 final environment outcome 分账，倾向 `No Change — Existing Coverage`，不把 8–17% 写成普遍风险。
- **VCC `2603.29678v1`**：[exact-v1 全文](https://arxiv.org/html/2603.29678v1) §2–3。直接把冗长 JSONL 交给 reflector 可保留原始信息，却让内部思考、tool I/O 和 system directive 混成难导航文本；直接摘要更省 tokens，却可能丢掉支持具体记忆规则的源证据。作者采用 lex→parse→IR→lower→emit，把原始轨迹编成三份同源视图：可重构的 full view 是稳定行号坐标，UI view 是用户当时实际看到的交互，adaptive view 只投影匹配谓词的结构块，每条投影可回指 full view 的范围。状态 owner 是外部轨迹转换/检索层，不是模型参数或 authoritative memory；derived rule 仍由 reflector 提议、任务 outcome 验证。AppWorld train 90 任务×2 epoch 用生成器/反思器写共享 `MEMORY.md`，test_normal 168、test_challenge 416；三组 Opus/Sonnet/Haiku+Sonnet 下比较 raw JSONL vs VCC view。Opus normal task-goal 92.9→94.0、challenge 84.7→86.3，reflector tokens 22.1M→7.6M；Sonnet normal 90.5→92.9、challenge 71.0→74.3。不同难度单元有 JSON 反胜，且 JSON 对照并非优化的结构检索器；并行 worker 的 memory 合并由另一个 LLM 做，收益不能只归因于某个格式 token。Ch77 已明示保存 lossless source、按读时任务生成 derived memory、raw transcript locator 与派生规则证据支持集；VCC 提供一个实施案例，倾向 `No Change — Existing Coverage`，或仅在 Ch68 Logging 的 trace view 设计已有空白时由主任务作 owner 判断。不得把 UI view 当完整证据，也不得把更短 memory 直接当更正确。

## Books 与来源待办

### 旧关闭集的分层误排复核（2026-09-26）

旧 `arxiv-owner-receipt.json` 的 516 条 identity 里，部分 `screening_reason` 是泛化模板，不能以其 `pre-denominator closure` 自动通过 V3。对 cs.CL/LG/AI/MA/CR 的强信号标题作反向抽检后，打开以下七条官方 **exact-v1 标题和完整摘要**，先记准入判断；只有恢复项才继续方法/评价正文。每项 DOI 批次归属仍受本文件“窗口与日期依据”约束，不能以 v1 Submitted 的单项时间反推公开。

| arXiv v1 | 准入判断 | 具体理由 |
| --- | --- | --- |
| [`2603.29123v1`](https://arxiv.org/abs/2603.29123v1) | 恢复待证据 | v1 真正标题是 *Concept Training for Human-Aligned Language Models*，并非旧 ledger 的后版 *Learning Concepts, Not Tokens*。把单 token NTP 的唯一目标改为语义相关 token 集合作为概念监督，直接构成训练目标设计分支；v1 仅报告 lexical semantic alignment 与 global perplexity 略升，**不继承后版 reasoning/reranking 改善**。需读 v1 方法和评价，并比较 Ch28。 |
| [`2603.29871v1`](https://arxiv.org/abs/2603.29871v1) | 恢复待证据 | set-level utility 若直接给每个候选相同 reward 会让弱候选搭强候选便车；Shapley credit 重分配到候选级，是特定集合推荐任务的 credit owner/成本选择，不等同普通同 prompt 的 GRPO 分组。需核 polynomial 计算、对照及 Ch33 已有 credit 分支。 |
| [`2603.29902v1`](https://arxiv.org/abs/2603.29902v1) | 定点判定 | 文图交错输出时生成/检索工具选择的遗漏机会是 evaluation 新轴，但作者 MLLM-as-judge 无 ground truth，须确认 Ch66 是否已有把 tool-plan 与工具后端成败分账；不能因 7,702 QA 或 10 模型规模直接准入。 |
| [`2603.28807v1`](https://arxiv.org/abs/2603.28807v1) | 前分母关闭 | SafeClaw-R 把 action 前 mediation 作为执行图安全不变量，方向与现有 Tool Calling/Agent Platform effect gate 一致；三领域作者检测率不能单凭摘要证明新的 authority owner 或反证。36.4% 高风险 skill 是作者样本判断，不可外推生态系统。 |
| [`2603.28955v1`](https://arxiv.org/abs/2603.28955v1) | 前分母关闭 | DreamerV2 latent transition 加 inverse-dynamics action recovery 以抑制 observation-only shortcut，Ch25 已在“inverse-dynamics loss 是 action-information anti-collapse regularizer”具体说明 precondition、失败与回退；八个 CALVIN 任务的成功率是同机制的受限验证，不新增通用成立边界。 |
| [`2603.28990v1`](https://arxiv.org/abs/2603.28990v1) | 前分母关闭 | 自组织 Agent 角色与拓扑的主张在 Ch82 已由固定角色的稳定条件、动态 topology/委派的版本化与评估边界承载；摘要的 25k tasks/8 models/4–256 agents 比较不足以推翻“强 SLO/不可逆动作回退静态角色”的判断，单一报告的质量与成本数值不外推。 |
| [`2603.29632v1`](https://arxiv.org/abs/2603.29632v1) | 前分母关闭 | 固定时间预算下 subagent 并行探索与专家团队交接的两种优势已由 Ch82 的 budget、critical path、独立 worktree、merge verifier 分账解释；自动 ML 研究测试床提供受限案例，不单独改变 owner。 |

补充核查后，`2603.29902v1` 判为**前分母关闭**：ATP-Bench 把交错文图输出的检索/生成工具选择、漏用图像机会和成品质量分开，确有针对性；但 `PLATFORM-EVALUATION-SYSTEM` Ch66 与 `AGENT-TOOL-CALLING` Ch78 已要求规划选择与工具执行/环境结果分账，本文五种工具、文图输出和 MLLM-as-judge（400 条人工协议一致性抽样，并非独立真值）没有提出新的通用判定责任。保留其 [exact-v1 §5–7](https://arxiv.org/html/2603.29902v1) 为受限实例，不把作者榜单或 7,702 条数据当作新的系统机制。

该七条是强信号子集的**定点抽检**，不是对其余旧关闭集的全量复核；需独立者复核恢复与拒绝两侧，并沿相同误排理由扩查受影响部分。

### 补充官方目录核验

- [OpenAI 官方 News RSS](https://openai.com/news/rss.xml) 为有界可读辅助入口：其邻域条目在本窗 `[2026-03-31T01:00Z,2026-04-01T01:00Z)` 仅列 [`2026-03-31T13:00Z` 融资/算力战略声明](https://openai.com/index/accelerating-the-next-phase-ai)，属于公司事实而非技术机制；下一条 [`2026-04-01T02:00Z` 银行业客户案例](https://openai.com/index/gradient-labs) 已过本窗截止。RSS 的 News/Company/Product 分类**不能**替代 Research index 的独立完整性，故 `SRC-OPENAI` Research 分页缺口仍保留。
- [DeepSeek 官方「研究与动态」](https://www.deepseek.com/news/)的可见研究索引从 2026-06-24 直接到 2026-02-25；动态列表 2026-04-24→2025-12-01，均跨本窗，无该目录可见的新技术条目。此判断仅限页面已列项目，不代表其所有未列论文。
- [MiniMax 英文官方 Research / Blog](https://www.minimax.io/blog)的可见邻域从 2026-05-26 直接到 2026-03-18，且 03-18 下一项为 02-14；本窗无该目录条目。[中文目录](https://www.minimax.cn/blog)作为补充核验入口，不拿英文空白外推全部渠道。
- [小米 MiMo 官网 Paper 栏](https://mimo.xiaomi.com/) 2026-06-29 下一篇为 2026-03-13；本窗无 Paper 栏条目。其 Blog 栏在当前 HTML 缺可靠单篇日期，不能以栏目可见而推定本窗无 Blog。
- [百度 ERNIE 技术博客](https://ernie.baidu.com/blog/zh/)的可见邻域是 2026-04-15→2026-02-06；[Publication 栏](https://ernie.baidu.com/blog/zh/publication/)当前只有 2025 ERNIE4.5/PaddleOCR-VL 与 2026 PaddleOCR-VL1.5、ERNIE5.0，不见本窗新条目。`SRC-BAIDU-ERNIE` 的 GitHub 补充入口仍需确认 tag/release 的真实事件时间。
- [Moonshot/Kimi 官方 Platform Blog](https://platform.kimi.com/blog) 当前列出的最新文章为 2025-11-07，该目录本身不覆盖 2026 研究，不能借此宣布该机构无更新；须用注册的 [MoonshotAI 官方仓库](https://github.com/MoonshotAI)及可读正式论文入口有界补查。
- [Qwen 旧 Blog](https://qwenlm.github.io/blog/)当前明确跳转到 [qwen.ai/research](https://qwen.ai/research)，但后者的 HTML 抽取为空；旧 Blog 可见最新 2025-09-23，**不能**代表 2026 时间窗。需浏览器或官方 API/索引的定点恢复；搜索引擎的无命中不可代替来源覆盖。

### 第六小批次：World/Video、MoE 组合与 Agent Skill（2026-09-26）

- **OccSim `2603.28887v1`**：[原始全文](https://arxiv.org/html/2603.28887v1) §3–4、§10。连续道路日志和 HD map 约束了闭环仿真场景，直接逐帧生成又积累几何漂移。作者把静态 occupancy 状态从动态车流分离：已知 ego 轨迹产生 rigid transform，warp 上一帧 latent 后对未观察区域补全；keyframe fusion 构成路网，再由 layout generator 生成车位、IDM 控制动态代理。**静态地图生成、代理初始状态和动态控制分别有 owner**，不是一个端到端模型完成全部物理因果。评估含静态分布距离、多样性、轨迹与下游 occupancy forecasting；“3000 帧/4 km/80×”只限作者道路 occupancy 设置，不能等于真实闭环驾驶可靠性。作者明确限制包括平面运动、latent 旋转不变性、启发式地图融合及少于 10 万帧语义 occupancy 训练数据。`MULTIMODAL-WORLD-MODELS` Ch25 已写 persistent state 与 simulator/real boundary；待主任务核其是否缺“静态持久性与动态行为解耦”的命题。旧日志回放在需要真实传感器分布和确定性回归时仍成立。
- **VecAttention `2603.29494v1`**：[原始全文](https://arxiv.org/html/2603.29494v1) §3–4、§13。块/stripe 稀疏在视频局部显著区域会带入无关 KV；更细的 vertical-vector 稀疏理论上更精确，却有重要性矩阵、排序和不规则 gather 的执行代价。作者对 pooled query/K tiles 使用 minS 阈值及 tiling selection，使选择与 attention kernel 融合；状态 owner 是执行计划的选取索引和加载 KV，不是模型语义记忆。在 NVIDIA A100 80GB、Qwen2.5-VL-7B 约 26K tokens、InternVL3.5-8B 约 17K tokens、Wan2.1/HunyuanVideo 720p 约 76K/119K tokens 上测视频理解/生成；Qwen 的 78.5% sparsity 下表中平均准确率 49.9 与 full 49.9，相同论文所报 2.65× attention kernel 提速仅对应 1.17× 端到端 TTFT，说明选择开销/其余阶段限制收益。未给可普遍转用的并发/SLO；作者明示 Agent reasoning、RAG、其他稀疏方向未证。`INFER-TENSORRT-LLM` Ch49 如已说明 pattern-selection overhead、kernel/end-to-end 区分，则可 `No Change`；若缺 modality-dependent 稀疏粒度-选择代价的演进链，才紧凑 refine，不把视频结论扩为文本推理结论。
- **ASI-Evolve `2603.29640v1`**：[原始全文](https://arxiv.org/html/2603.29640v1) §3–5。提出 Researcher 提议代码、Engineer 真执行并评分、Analyzer 将日志压成诊断、Cognition 检索领域先验、database 存每轮结果的研究循环；控制权在任务特定 evaluator，持久状态是代码版本、实验输出及被选中历史，不是模型“自主发现真理”。包含模型架构、数据清理、RL 算法搜索三项 AI-for-AI 场景及 circle-packing 代理比较：后者 26 圆任务的 GPT-5-mini 17 轮达到 2.63597，但与其他框架的模型/停止条件并不齐，不能比较通用研究效率。RL 分支以 4B/150-step/6 数学基准探索、14B/300-step 扩展验证；fitness 混合 benchmark accuracy 与 LLM judge，独立未见长期外部 holdout、泄漏与专家人工复现实验。`AGENT-WORKFLOW` Ch81 已有实验-反馈-记忆闭环；除非现文缺 evaluator 与 cognition provenance/holdout 解耦，倾向 `No Change — Existing Coverage`。本项是 AI-for-AI 工程流程而非暂缓的领域型 AI for Science。
- **DUME `2603.29765v1`**：[原始全文](https://arxiv.org/html/2603.29765v1) §2–3。已有独立 dense 专家若共享同一预训练 seed、架构和 tokenizer，可以抽取各层 feature 与领域标签，以闭式 ridge regression 拟合路由器，再将专家层组为 MoE；“training-free”只指**组装时不再反传**，先前 seed/专家训练及组装特征前向仍需成本。作者用 115M Llama seed/OpenWebText + 5 个 M2D2 领域专家（各 1k 迭代）、另外四个 3B reasoning 专家；最多 4×H100 80GB，CLM 按五域 normalized perplexity，reasoning 用 HumanEval/GSM8K/M_ARC/IFEval。条件不同的专家、tokenizer 不兼容、域漂移和在线路由不均衡没有普遍解决；报告没有生产 serving 并发/SLO。`MODEL-MOE` Ch21 与 `TRAIN-PRETRAINING` Ch28 需核是否已有“独立专家→后验路由组装”条件分支；若没有，这是可写的训练/部署边界，但不把它写成无代价扩容。
- **DIAL `2603.29844v1`**：[原始全文](https://arxiv.org/html/2603.29844v1) §3–5。高层 VLM 的预测若仅作为辅助 loss 或松散拼接，低层 policy 仍可绕开“意图”而走 proprioception shortcut；作者用可微 latent future-view bottleneck 作为 System-2→System-1 的必经条件，System-1 结合当前视觉/本体状态经 flow matching 生成 16-step action chunk。共享冻结 ViT，先以真实未来特征 warmup 再接预测特征联合训练。RoboCasa GR1 24 个桌面任务及少量真实 IRON-R01 操作构成实验；同骨干消融中 58.3% 对松散连接约 47.2–51.9%，是该任务和训练量下的接口证据，不证明真实环境物理安全或意图解释性。`MULTIMODAL-EMBODIED-VLA` Ch26 已有分层 controller；需比较是否缺“预测状态须为动作路径必经接口，且共享表征才能避免旁路”的明确机制。旧松散接口在不要求预测状态强制控制、资源更受限时仍可选择。
- **SkillReducer `2603.29919v1`**：[原始全文](https://arxiv.org/html/2603.29919v1) §IV–V、§VII。单体 skill 描述、规则和资料一起加载，路由噪声与 token cost 增加。作者分两阶段：先以 delta debugging 找最小可路由 description，再把正文分类为核心规则/背景/示例/模板并按需加载，保留可回取的原始信息路径。600 个样本来自官方/社区/野生 skill；外部 SkillsBench 是 87 tasks/229 skills。作者的内部 Gate 2 同时参与优化与评价，86% 通过率有 criterion-coupling 风险；外部 deterministic 结果只部分缓解；跨模型验证仅 30 skills，其它协议未证。`AGENT-SKILL` Ch83 / `AGENT-CONTEXT` Ch75 若已有 progressive disclosure 与路由最小元信息，可 `No Change`；若尚缺“routing description 与执行正文分层、按需材料加载及任务回归”的完整因果链，再由主任务局部 refine。

### 旧关闭集恢复项：训练目标与集合奖励（2026-09-26）

- **Concept Training `2603.29123v1`**：[原始全文](https://arxiv.org/html/2603.29123v1) §3–5 与 Appendices A–D；旧 ledger 后版标题/摘要不得代入。单一正确 next token 的 NTP 在多个语义等价续词中只奖励观察到的词，简单且与推理 tokenizer 对齐，但可能把等价表述误作互斥目标。作者对上下文同义词集合的预测概率求和再取负对数，以 `λ` 与原 NTP 插值；监督集合由 Llama3.1 8B 的 top-200 候选和 8B-Instruct 过滤生成，只在英语中可对齐为单 token 的名/动/形容词上建立，约占处理文本 token 的 28%。这把“语义等价”判断移到教师生成的数据标签；教师偏差、词性/分词边界和多义词误归类是新增 failure mode。C4/OWT 各抽 2,000 段，Llama 3.2 1B/3B 和 3.1 8B 做短继续训练；MEN、WordSim353、SimLex-999、STS-B 的表示相似度 Spearman 及 held-out content-word perplexity/accuracy 受限改善，而全局 token perplexity 略变差。该证据不证明指令遵循、长程推理或通用 AI System 能力提高。`TRAIN-PRETRAINING` Ch28 现文讨论 objective/data coupling，但缺 NTP 单标签→等价 token-set 这一条件性设计分支；可由主任务在 Ch28 一小段吸收，并保留标准 NTP 在精确字符串生成、低成本标签和开放词表规模化下成立。暂拟 `Integrate — Experimental`，首次公告归属和独立准入审核未完成前不宣称最终。
- **ShapE-GRPO `2603.29871v1`**：[原始全文](https://arxiv.org/html/2603.29871v1) §3–6。普通 GRPO 对同 prompt 的多个独立回答做组内相对优势；本文不同的是**单条回答内的 K 个候选**共同形成 set utility，若把集合 reward 同样广播给每个候选，弱候选会搭强候选便车。作者在集合效用取候选最大值且候选顺序无关时，用 Shapley marginal contribution 把 set-level 价值分到候选，再广播给对应 token；说明部分仍用原集合 reward。该特殊 max 结构可按奖励排序 `O(K²)` 算精确值，binary reward `O(K)`，不能泛称任意 set reward 都多项式。等长候选是其总体重加权/无额外 bias 命题的条件；候选抽取、候选级 oracle 不可靠或效用并非 permutation-invariant 时，这条 credit chain 会失效。作者用 Qwen3-8B、2×GH200 在 ACLSum（LLM judge）、DS-1000（执行测试）和 Netflix 模拟推荐与 GRPO、Winner-Takes-All 比较；表中不同任务有提升，但 Netflix 历史样本与 output-length 基线条件不同，且未证生产任务、真实点击效用或跨模型稳定。`TRAIN-GRPO` Ch33 已有 group-relative advantage 与 reward 颗粒度问题；需主任务核对是否已有**集合效用→候选边际贡献**这一不同 credit owner，再决定小幅 `Integrate — Experimental` 或 `No Change`。首次公告归属及独立准入审核尚待完成。

这两条也有同批次边界的独立交叉线索：[DataCite `2603.29123`](https://api.datacite.org/dois/10.48550/arxiv.2603.29123) 的 initial `created=2026-04-01T02:03:25Z`；[`2603.29871`](https://api.datacite.org/dois/10.48550/arxiv.2603.29871) 为 `2026-04-01T02:21:12Z`。二者的 DOI 登记时刻**不是** arXiv 公告时刻，仍需与官方 ID/公告批次合用，不伪造单篇公开分秒。

### 已读正文与 Books 具体命题对照

- `2603.28887v1` OccSim → `MULTIMODAL-WORLD-MODELS` Ch25「Memory 架构为何从静态 cache 演进」已把 scene structure 与 motion state 分开，并保留 stale/identity 失败边界；本文的道路 occupancy rigid warp、keyframe fusion、IDM agent 是驾驶域专用实现，未改变该长期 owner。**暂拟 No Change — Existing Coverage**，不把作者的里程/加速转换成通用世界模型结论。
- `2603.29494v1` VecAttention → `INFER-TENSORRT-LLM` Ch49 已明示 index generation、selection、gather 的融合，以及 kernel 与端到端收益不能混淆；其 vertical-vector 粒度和 minS/tiled selection 给出受限视频实现，但没有反证现有设计分支。**暂拟 No Change — Existing Coverage**，不要把视频长序列条件迁到文本 serving。
- `2603.29844v1` DIAL → `MULTIMODAL-EMBODIED-VLA` Ch26「latent visual interface」已解释 action head 直接旁路视觉状态、pose bottleneck 的受限收益与信息丢失；DIAL 的未来视觉 latent 必经接口和 16-step chunk 属于这一机制的不同实现。**暂拟 No Change — Existing Coverage**，真实控制安全仍由 controller 拥有。
- `2603.29919v1` SkillReducer → `AGENT-PLATFORM` Ch84 已明确 skill body/lazy references 反复占 Context，并要求 task-slice canary、risk-aware budget 与按需加载；算法化的 delta debugging 不改变正文命题。**暂拟 No Change — Existing Coverage**，内部 Gate 2 优化与评价耦合限制作者结果。

### 第七小批次：强信号关闭侧与剩余评价审阅（2026-09-26）

本轮再次读取下列 exact-v1 标题与摘要，并对确需判断的机制段与现有 owner 作定点对照；它们不是靠关键词自动通过。旧 516 身份池的其余排除项仍未被宣称逐篇全文审核。

| Source Family | 本轮前分母裁定 | 可核查的贡献与排除界线 |
| --- | --- | --- |
| [PolarQuant `2603.29078v1`](https://arxiv.org/html/2603.29078v1) | 前分母关闭 | 权重块归一化、Hadamard 旋转后按 Gaussian Lloyd–Max codebook 量化；Qwen3.5-9B 的 Q5/INT4 质量及消费级单机吞吐是作者局部 PTQ 条件。`INFER-TENSORRT-LLM` Ch49 已把分布诊断、旋转/量化格式耦合、kernel 和端到端发布 Gate 放在同一链，本文未改变设计责任或证明普适无校准无损压缩。 |
| [APEX-EM `2603.29093v1`](https://arxiv.org/html/2603.29093v1) | 前分母关闭 | PRGII 把成功/失败的计划、错误、artifact 与 verifier feedback 保存在 procedural-episodic graph，再以语义/结构签名/图遍历检索；作者三个 benchmark 的收益不能证明跨版本、权限与未见任务的程序可用性。`AGENT-MEMORY` Ch77 已区分 source episodes、derived procedural lessons、verifier/admission、graph/structural retrieval 与旧规则撤销；本文是组合实现，尚无新权威边界。 |
| [ConSelf `2603.29292v1`](https://arxiv.org/html/2603.29292v1) | 前分母关闭 | v1 以程序行为分歧定义 semantic entropy，选代码自训练 curriculum，并以行为共识加权 DPO pair；针对没有教师/测试 oracle 的代码任务。行为共识仍是代理监督，不等于真值；题摘与 §2–4 未提供足以修正通用 `TRAIN-DPO` 的 verifier/奖励权威合同或跨任务证据。此前具体关闭理由保持。 |
| [Xuanwu `2603.29211v1`](https://arxiv.org/html/2603.29211v1) | 前分母关闭 | 约 2B 的视觉编码器+Qwen3 1.7B、多阶段训练及内容审核/对抗 OCR 是专域模型工程组合；业务样本、zero-shot 商业模型对照与作者训练条件不能推出通用多模态架构或安全发布结论。`MULTIMODAL-REPRESENTATION` Ch23、训练/评估章节已有 encoder-projector、domain adaptation、业务/开放能力分账，本文未修正其 owner。 |
| [StepCache `2603.28795v1`](https://arxiv.org/html/2603.28795v1) | **由 21 工作分母降为前分母关闭，现为 20 工作候选** | 低分 `1+1+2=4` 的跨请求 step 复用+verifier+整答回退在 `AGENT-WORKFLOW` Ch81 已有部分产物复用、前提及最终验收；CPU-only Qwen2.5-3B 线性方程/JSON 微基准没有新 serving SLO 或长期机制。原 §3–5 详细证据保留在本 checkpoint，不因移出 Daily 正文而删除。 |

- [Emergence WebVoyager `2603.29020v1`](https://arxiv.org/html/2603.29020v1) §3–5：人工审 643 原任务，按指定站点、动态相对日期、环境故障与 Agent 自身错误的 retry 边界重做为 535 题；两人 95.9% agreement 是协议一致性，不是 ground truth 保证。Operator 68.6% 与原 87% 不同 benchmark/protocol，不可作直接能力差。`PLATFORM-EVALUATION-SYSTEM` Ch66 已拥有 task/evaluator/environment revision、过程与终局分账；`No Change — Existing Coverage`，标准审阅完成。
- [Beyond pass@1 `2603.29231v1`](https://arxiv.org/html/2603.29231v1) §3–7：396 题×10 模型×3 重复×2 scaffolds 计划 23,760 episodes，作者完成 23,392；按 SE/网页研究/文档处理及四个人类预估时长分层，温度 0.7，最多 50 steps。pass^k 与衰减/partial-credit/工具熵 MOP 分开测；`MOP` 阈值在 19 题 pilot 的人工标签上调，早停恢复只列未来工作。quota/404 造成先跑短任务后漏长任务，作者换付费/多 provider 路由后报告完成；任务选择、路由、未完成 episode、人类时长与 Agent 步数错位限制外推。`PLATFORM-EVALUATION-SYSTEM` Ch66 已把 Pass@k/Pass^k、horizon/domain、环境/服务身份及重复运行分账；`No Change — Existing Coverage`，标准审阅完成。
- [FlexMem `2603.29252v1`](https://arxiv.org/html/2603.29252v1) 已由主任务在 `MULTIMODAL-REPRESENTATION` Ch23 补入逐 clip visual KV 派生近期 `C`/长期 `M`、bank 写入及按 query 读取的有界分支；本日报同步 `Integrate`。确认该状态不是精确 KV reuse，也没有无损无限或生产尾部证据。

1. 对保留的 family 按精确 v1 方法/评价/限制段重审；不能直接沿用旧 `No Change`。此前列出的 `2603.28768`、`2603.28781`、`2603.28795`、`2603.29231` 已分别完成上述或前文定点判断，其余见当日报告。
2. 逐个检查 13 个机构 Daily 发现入口的本窗发布时间与分页/停止点；当前旧日报仅有 arXiv 来源行，不得宣称来源完成。已确认 [Z.ai GLM-5V-Turbo 原文](https://www.zhipuai.cn/zh/research/156) 标注 `2026/04/01 16:00`，在本窗截止后，属于 4 月 2 日候选线索，不计入本日。
3. 待复核者检查本 checkpoint 中 Date reconciliation、题摘准入两侧（误收/误排）与 source scope。Books 若有必要修改，由主任务协调书稿 owner；本日报维持 `进行中`。
