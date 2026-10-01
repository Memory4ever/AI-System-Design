# 04/27 排除侧定点重开：2604.22291v1

本文件只核一个被旧共享理由前分母关闭的高风险家族；它不是 408 项全量复审、来源 Gate 或整日语义 Gate。原始身份在 `arxiv-owner-replay-20260903/20260427/arxiv-owner-receipt.json`；其旧 `screening_reason` 称“只形成任务或数据集级 measurement/context，没有新增通用 release/evaluation contract”。这个理由不能在未看 exact-v1 的情况下承担否定结论。下方先保留作者初核，再记 root 独立采用与日期组合；**新增候选仍不是冻结分母或整日 Gate**。

## [2604.22291v1 Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets](https://arxiv.org/html/2604.22291v1)

- **原文身份与日期边界：**官方 [abs/v1](https://arxiv.org/abs/2604.22291v1) 显示 v1 Submitted `2026-04-24T07:12:29Z`，这不是首发公告。04/27 原始 339 身份底稿给该 ID 的 `v1 Updated=2026-04-27T00:24:03Z`、`DataCite initial created=2026-04-27T01:33:47Z`、`OAI datestamp=2026-04-27`；相邻 `22290/22292/22293` 的 Updated 依序 `00:23:54/00:24:12/00:24:13Z`、DOI created 依序 `01:33:46/01:33:49/01:33:51Z`。这些字段均非 first-public；结合[官方 ID 公告赋号及 Sunday 20 ET 规则](https://info.arxiv.org/help/availability.html)、连续批次/次日首 `22754`、exact-v1 身份，仅有据推断 04/27 北京时间 08:00～09:00 公告，不冒称逐篇公告日志确证。
- **威胁模型与方法：** exact-v1 §2 将对象限定为代码数据 owner 发布可供正常开发的代码，却不授权他人据此微调 CodeLLM；对手可控制预处理、静态分析、重写与模型训练，但没有 owner 保留的干净版本。§3/Alg.1 从真实语句抽模板、修复可编译性，在通过 safety filter 后把 execution-inert 的 weak-use 片段置入会被模型学习的代码路径。对代码运行可无副作用，对 autoregressive next-token 监督却非中性；“有合法 license/可编译/功能测试通过”与“可安全送入训练”是不同身份和评价对象。
- **决定性受限对照：**§5 Table 2 用同一模板池作 DeadBranchInsertion：10% 污染时 clean FT Pass@1 `.38`、FunPoison `.20`、dead branch `.38`，支持执行路径位置而非模板露出本身是此设置的差异；Table 3 仅在 984 个 Java HumanEval-X 实例的编译、输出/异常/I/O 等受测条件下称行为保持，另在 Apache Commons Lang 所测 57,764 tests 通过。不能把“100% functional correctness”外推为所有 Java 代码的形式等价。§5 仍限定 DeepSeek-Coder/相关 CodeLLM、Java、所测微调/代码生成、温度与污染率，不能据此称所有预训练或大模型都可被 10% 毒化。
- **作者自述的非证明：**§7 Limitations 承认只测 Java 可执行代码生成，CodeSearchNet Java 在其覆盖下 80.3% 函数有可插位；未证明不可移除，aggressive curriculum、从头大规模预训练及 RL adaptation 尚未验证。§Ethical Considerations 将其称双用途、限定未授权适配威胁，不建议默认污染协作开源语料；故不能把它作为普通数据集“防盗”推荐或法律权属证明。
- **实际 owner 差额：**[TRAIN-DATA Ch27](../../../../../books/part-04-training-system/27-data.md) 当前已把来源/provenance、许可、去重与 benchmark contamination 分账，§Code Memorization 要验证功能而不只文本，但尚未明确反向情形：代码的编译/运行功能保持，仍可通过 next-token 监督污染训练。若保留，最窄长期命题属于训练数据 admission 的“执行功能正确不等于梯度/目标安全”，并与 [PLATFORM-SECURITY Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 生命周期 Data poisoning / 授权分权交接；Ch72 不应因安全标题再写重复算法。它可能只是 Java CodeLLM 域内攻击，是否足以改变 Ch27 长期验收由非作者独立判定。

**非作者采用裁决与当前状态：**root 已独立读 exact-v1 §2–5/Limitations、同模板 DeadBranch Table 2，复核 Ch27/72，确认“编译/功能测试通过≠训练监督效用安全”是 Ch27 未写的窄 admission 边界，旧“仅 measurement/context”前关闭理由不成立。当前以 Score V2 `2+2+2=6`、深入完成准入为第 38 个**未冻结**工作候选；root 已在 Ch27 训练数据准入主线实写防护性分账与 Review note，实际新增段仍待非写入者按原文、相邻段与边界复核。Books 暂记 `Integrate — 实写待作者外写后`，不计已通过 I，不预言整日 Gate 或“10% 对所有语料有效”。

## 同类泛化关闭理由的下一组有界反向抽样（作者定点，待非作者校准）

以下七项均实际读取原始 receipt 的完整题摘；仅 `22662` 进一步读取官方 [exact-v1 §2–5、Limitations](https://arxiv.org/html/2604.22662v1) 并对读现有 Ch66 attribution/evaluation 正文。其余只对读所述现有命题，未声称全文或排除侧全量审阅。此组专查旧 `screening_reason` 把局部方法、评价与领域对象混为“无系统贡献”的共享风险；**不改变当前 38 工作分母**。

| 原关闭身份 | 实际内容与当前有界处置 |
| --- | --- |
| [`2604.22215v1`](https://arxiv.org/abs/2604.22215v1) verbal confidence saturation | 预注册的七个 3–9B instruct model、524 TriviaQA、数值/类别 elicitation 与贪婪解码验证输出 confidence 的 Type-2 discrimination 失效；不等于内部不确定性缺失。Ch66 现有 judge/verbal-confidence 不得直接 route/defer、slice calibration 与 readout/probe≠truth 已承载该 release 边界；此受限测量支持既有命题，暂维持具名前分母关闭，不据 ceiling 数字追加通用规则。 |
| [`2604.22662v1`](https://arxiv.org/html/2604.22662v1) human-centered Shapley audit | 旧模板“仅 measurement/context”不能充分关闭。论文以统一 amortizer 控制实现差异，固定模型输出/界面、随机被试内且有无解释对照，3,735 个 case reviews 中定量 faithfulness/sparsity proxy 与人类 clarity、decision confidence、客观 accuracy/time 分账；§5 报解释提高 confidence 而未见 objective performance 提升。Ch66:2324–2332 已区分 attribution scorer、受众、证据与 release owner，但未明确**解释提升主观把握却不改善实际决策**的 paired human-outcome 反证轴。建议非作者定点判断是否恢复 `2+2+2=6` 候选，可能是 ReportOnly/Existing，绝不因标题自动写书。限制为受控 tabular risk/欺诈审查、37 participants、短期决策；不是 LLM/Agent 解释的普遍因果保证。原始 v1 Updated 04/27T00:46:40Z、OAI 04/27、DataCite created 01:43:05Z 与相邻批次只作公告组合推断，Submitted 04/24T15:38:44Z 与 DOI 均非首次公开时刻。 |
| [`2604.22080v1`](https://arxiv.org/abs/2604.22080v1) scientific falsification | 题摘是论证性文章，警告 Agent 可快速生产可叙述的阳性分析，主张主动寻反证；未给可区分 search/evaluator/claim authority 的新实验合同。Ch27:835 已把科学 protocol、原始读数、negative result 与生成 hypothesis 分层；Ch81:305–314 已分 candidate lineage、evaluator 与 run-derived lesson，故仅题摘层面的理念可具名关，不以“AI-for-Science”题名硬拒。若有独立可执行 adversarial protocol 再定点重开。 |
| [`2604.22282v1`](https://arxiv.org/abs/2604.22282v1) STEM KG-RAG | 题摘给 schema-guided query decomposition、global guidance subgraph/Triple-GNN 的 KGQA 检索实现及多跳结果；没有说明超出现有 Ch76 query/candidate/evidence/answer Gate 的独立长期责任或受控替换边界。暂按 KGQA 实现分支前关闭，不能以“图”或“RAG”字样本身准入；若后续必要 Method 证明 global schema 状态使既有检索停止/证据授权逻辑失效再重开。 |
| [`2604.22313v1`](https://arxiv.org/abs/2604.22313v1) CLARITY NL2SQL | 约束生成多重歧义/不可回答 query 与多轮澄清，题摘报告系统能检测但难定位 schema 歧义；这是值得在 NL2SQL evaluator 的受限负例，但 Ch66:840 已保存 SQL 执行语义身份，Ch81:319–323 已规定歧义未解不编译成确定 workflow。仅题摘不足以推出不同的长期 action/evaluation Gate，暂具名前关闭；若方法给 schema-level ambiguity localization 独立于现有 clarification/abstain 的必要验收差额再重开。 |
| [`2604.22413v1`](https://arxiv.org/abs/2604.22413v1) Graph Transformer distance control | contextual SBM 合成 node classification 中已知 oracle distance target 的控制器优于任务无关零差控制器，说明 local/far-shell label signal 的特定偏置；oracle 拥有离线 target，未验证生产图分布下可获得的动态 distance owner。暂作受限图任务设计案例前关闭，不外推 Transformer/LLM attention 的通用距离法则；若出现无 oracle 的稳定 target/成本验收可重开。 |
| [`2604.22504v1`](https://arxiv.org/html/2604.22504v1) windowed partial AUC | 作者进一步读官方 §2.1/§3.1–3.3：仅在 constrained item vocabulary、单个目标 item 的 binary reward 与规定的 GRPO 组内比较下，随机负样本对应全体 pairwise/AUC；beam 把负样本推到高分尾部，有限 beam 只是 OPAUC 近似，WPAUC 另以 FPR window 显式控制 Top-K 对齐。Ch33:167–178 已讨论零 reward 负样本的信息量和生成成本，但未明“负样本采样律改变隐含排序目标”；有受限训练目标差额，不宜按“推荐应用”直接关。它仍只在推荐候选集、二元 reward、作者四数据集内成立，不是通用 GRPO/AUC 恒等式或线上 Top-K 保证。现提请非作者判 5 分标准 ReportOnly 或具名关闭，**不预先加入 38**，无需无界扩读。 |

本抽样的结果是 `22662` 一项正式提请非作者复核、`22504` 一项已核方法/owner 后待非作者准入裁决、其余五项具名有限前关闭；不是 408 身份全量阴性声明。若其中任一被恢复，必须同步候选表、分母、必要证据和 Books 决定，不能仅改本附录。

## 追加一组跨理由的四项否定侧定点核（2026-09-28）

为防止“局部方法/无 owner”的旧模板继续掩盖具体安全或设计信号，从本日 DataCite 原始 `identities[]` 里按题名主题选择四个尚未恢复的旧关闭项，实际读取各自完整库存题摘及官方 exact-v1 abs，定点对照当前章节。这里只评价准入，不假称四篇全文、全部旧关闭项或独立日级审计已读。

| 身份 | 原文实际信号、owner 差额与有限裁决 |
| --- | --- |
| [`2604.22028v1` FlyCatcher](https://arxiv.org/abs/2604.22028v1) | 由一般软件测试经 LLM synthesis、静态分析和动态校验推出持 shadow state 的 method-call runtime checker，400 tests/四个传统软件系统而非模型训练、推理或 Agent effect 流。旧“局部方法”模板未说明其技术实质；更准确的前分母关闭理由是：Ch66 的模型/Agent evaluation identity 与 executable outcome gate 并未因这套一般软件 checker 推断法而改变，也无受控 AI workload 证据将测试归纳出的断言升级为平台 release oracle。该法对软件运行检测有价值，不能因此默认是本项目候选。 |
| [`2604.22119v1` ESRRSim](https://arxiv.org/abs/2604.22119v1) | 7 类/20 子类风险 taxonomy、自动合成情境、回答/推理轨迹双 rubric 和 11 个 reasoning LLM 风险读数，不能简单称无安全信号。现 Ch66 已把主动 probe 的 task/environment 混杂、evaluation awareness、trace+rubric 与外部 outcome authority 分开；该题摘未给能突破这些既有判断的控制实验，双 rubric 也不能把 CoT 当风险真值。故保留具名前分母关闭，恢复条件是其必要方法/评价给出**同任务、同环境、同 judge 下独立改变 release/evaluator Gate**的反证，不因 taxonomy 数量或检测率跨度入选；本轮未采用 HTML 可能受后发 v2 污染的任何细节作原版结论。 |
| [`2604.22293v1` HGQ-LUT](https://arxiv.org/abs/2604.22293v1) | 原版确有训练时用常规 tensor 运算、部署时编译成 FPGA logic LUT，以及异质 bit/零 bit 与 bit-exact verification 的硬件—训练联合路线；旧“专用硬件局部”模板过粗。但实际目标是 CERN 等小型 DNN/LUT 工作负载，题摘没有 LLM/多模态训练或服务层的同硬件质量—成本/延迟分账，不能将宣称的训练加速移给 Ch49 量化、Ch45 KV/PIM 或生产 GPU serving。按当前项目范围具名前关闭；若以后有基础模型工作负载下独立同预算映射/执行反证再重开。 |
| [`2604.22360v1` Neural Activation Coverage](https://arxiv.org/abs/2604.22360v1) | 题摘仅把 NAC 用于**已训练回归网络**的不确定性评分，并称所测实验优于 MC Dropout；没有校准、选择性预测或 deployment abstention 的跨分母数据，也没有生成模型/Agent 的新控制对象。Ch66 已把 probe score 与真实错误、release threshold 分开，故此受限回归 estimator 不能成为现有 evaluation Gate 的反证；维持前分母关闭，不能由“coverage”一词称主线贡献。 |

四项均为**按原始完整题摘与 exact-v1 abs 的具名否定校准**，不是证明没有隐藏的重要修订，也不是在未读 Method 时对作者全部效果做否定。旧模板理由已在此补为 family-specific 判断，当前 40 个工作候选数不变；仍须 root 对整日负侧、来源和分母作独立 Gate。

## 高信号旧关闭项定点复核：2604.22615v1 GazeVLA（待非作者准入裁决）

旧 receipt 对 [GazeVLA: Learning Human Intention for Robotic Manipulation](https://arxiv.org/abs/2604.22615v1) 的关闭理由只是“局部模型/优化方法，未转移可复用 state/data/control ownership”。这不充分：官方 [HTML/v1](https://arxiv.org/html/2604.22615v1) 首页明确标 `arXiv:2604.22615v1 [cs.RO] 24 Apr 2026`，与官方 abs/v1 的标题、作者、题摘一致；本轮尝试取得 16,827 KB PDF v1，45 秒只收到约 2.4 MB 后超时，**未声称 PDF 已读**。必要机制、消融与限制按可读的官方 HTML/v1 核，未进行版本史比较。

- **日期身份：**abs/v1 的 Submitted `2026-04-24T14:46:03Z` 不是公开时刻。原始 receipt `v1 Updated=2026-04-27T00:44:22Z`、DataCite initial created `2026-04-27T01:41:49Z`、当前 OAI `2026-05-01` 已受 v2 修订影响，均不能单独证明 04/27 首发；本日只能沿官方 ID 赋号/常规 Sunday 20 ET 公告规则、相邻连续批次、exact-v1 身份作 04/27 08:00～09:00 BJT 的有据推断。若逐篇延迟证据出现须重开归属。
- **实际机制：**§3.1 用 13 个 egocentric 人类数据集的 gaze/hand 有效 mask 构建前动作的 2D gaze proxy；§3.2 把 `π(i|o,l)` 的离散 gaze token 自回归预测放在 `π(a|i,s,o,l)` 的连续 action expert/flow matching 之前，后者读取前者产生的 KV；§3.3 人类预训练有 gaze/action，机器人后训练没有 gaze label。这里新增的是**人类数据选什么监督目标、预动作中间状态如何传给机器人动作头**，不是说 gaze 等于真实内在意图或运行时安全授权。
- **关键受限对照：**§4.4 Table 2 在同一 pick-and-place 任务、10 条机器人轨迹加 50 条人类示教下，作者方法与只在推理时取消 intention 自回归步的 `ours w/o CoT` 比较，ID `19/20` 对 `16/20`，OOD-object `8/10` 对 `6/10`，OOD-scene `6/10` 对 `5/10`；同表 robot-only、混合 fine-tune 与混合 pretrain 是其它不同训练分支，不能把它们的所有差额归于 gaze 一项。小 trial 不能证明跨 embodiment 普遍提升、gaze 的因果唯一性或生产安全。§3 另有视频分割/坐标与眼动过滤成本、action expert 及训练计算；§5 明示没有在预训练阶段使用机器人数据，也没有显式共享 latent action space。
- **实际 owner 差额：**[MULTIMODAL-EMBODIED-VLA Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已有 human video breadth→derived transition/trajectory label→embodiment/action alignment，并有 episode Plan/chunk Think，但没有把**前动作、可观测的人类 gaze 标签作为跨本体监督入口，且由意图预测 token 的派生 KV 条件化 action head**这一可替代分支写明。它可能改变“从人类示教提取什么比 action 坐标更可迁移”的设计选择；同时它只是受限 PaliGemma/Gemma-2B 及所测机器人任务的实例，不能由章节映射自动成为 Books。当前建议撤销泛化前关闭，按 `Design Delta=2, System Reach=2, Durability=2` 的候选上界提请非作者**先裁准入**；评分、Books 与当前 40 工作分母尚未改，且需确认日期组合与上述受限条件。若独立认为 Ch26 已实质承载同等选择，应给具体段落与受限反证后具名关闭，而非恢复旧模板理由。

**后续处置（2026-09-28）：**上述段落记录的是提出时的状态；root 已完成独立准入核，Ch26 已实际写入该受限分支，root 再按 exact-v1、实际正文及相邻交接作非作者写后复核并判 PASS。正式工作集合现为 41 项、其中 30 项真实 Integrate；整日来源/排除侧 Gate 仍待独立复核。
