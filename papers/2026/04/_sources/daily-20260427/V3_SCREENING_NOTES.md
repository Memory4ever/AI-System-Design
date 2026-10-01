# 2026-04-27 V3 题摘贡献筛选（工作表，未冻结）

**当前恢复点：** 初始 38 家族经 `22436/22050/22708` 三项具名前关闭为 35；旧泛化否定侧经具名定点恢复 `22438/22550/22291/22662/22504/22615/22236/22442/22169/22464/22171` 十一项，现为 **46 项工作候选，仍未冻结**。`22662/22504/22236/22442` 各为 2+1+2=5 标准完成、仅报告；`22615` 是人类 gaze 前动作监督→意图 token→action head 的受限 2+2+2=6 条件分支；`22169` 的稀疏组 repair/搜索—更新宽度分离是受限 2+2+2=6 分支；`22464` 把无额外 router 训练数据时的 expert 演化、输入子空间路由与跨模块 task-origin 路径分权，2+1+2=5 因 Ch30 真缺口深入 override；`22171` 的 predicate-agnostic clique cover/多 seed 物理索引选择为 2+2+2=6，Ch76 实写并经[非书稿作者写后 PASS](V3_APR01_22171_CH76_WRITE_AFTER.md)。日期由官方 Sunday 20 ET/ID 赋号规则、连续相邻 ID、OAI/DOI 原字段和 exact-v1 组合有据推断为本窗 08～09 北京时间，`Submitted`、v1 `Updated`、DOI 初建各非首发单证。正式条目见[证据表](V3_EVIDENCE_REVIEW.md)、[MCI 定点审计](V3_APR01_22171_MCI_REVERSE_ADMISSION.md)及[本轮共享理由抽查](V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)。普通 Books 待办 0；14 源与否定侧仍待日级 Gate。

2026-09-28 非作者按 [38 家族贡献重校准](V3_ADMISSION_RECALIBRATION.md) 定点通过三项具名前分母关闭，工作集合 38→35（仍未冻结）：`2604.22436v1` AgentSearchBench 的目录 top-20/LLM-judge relevance 只在受限目录验证 Ch84 已有声明→task-slice 执行/结果 witness，任务/执行/标签三分母不能合一；`2604.22050v1` LayerBoost 的逐层 identity probe、三档注意力替换和蒸馏 healing 只为 Ch22 已有 dense→hybrid 层位敏感度/质量/执行联验给出 Qwen3-4B/A10 局部配置，10M PIQA 反向且无新决策条件；`2604.22708v1` TraceElephant 的三 scaffold 输入/metadata ablation 只证明 Ch69 已写日志/环境/配置 trace 有助局部归因，未改变诊断 proposal 与效果授权分权，380 trace 与“+76%”相对值不独证因果 root cause。三项 exact-v1 已读事实和负例仍留校准文件，不给排除项评分，也不因 Books 已有章节本身硬拒。

机构补查的非 arXiv 家族：MiniMax-AI/cli [v1.0.12](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.12) 官方 `published_at=2026-04-26T01:40:29Z`，确属本窗。release 与 [PR #94 files](https://github.com/MiniMax-AI/cli/pull/94/files) 显示 HTTPS 下载/重试、URL 与 base64 两种图片响应/本地保存，以及 I2V 参数校验、终端配色、测试/文档等局部 CLI 修复。它们不提供本书模型、Agent 或 Infra 长期设计的新机制、反证或安全授权边界；按贡献前分母关闭，不评分、不写 Books。此判断不等于 MiniMax 组织其它仓库零发布，来源覆盖另见 [实际停止点](V3_SOURCE_DISCOVERY.md)。

QwenLM/qwen-code 本窗 [v0.15.3](https://github.com/QwenLM/qwen-code/releases/tag/v0.15.3)（`2026-04-26T06:49:56Z`）与 [04/27 nightly](https://github.com/QwenLM/qwen-code/releases/tag/v0.15.2-nightly.20260427.3b0b6c052)（`2026-04-27T00:25:13Z`）按同 repo release 家族去重检查，不把每个 PR 都变成日报候选。定点原始 PR：[#3441](https://github.com/QwenLM/qwen-code/pull/3441) 只截断 UI/API 对话历史、保留 recording 的 parentUuid 分叉，没有声称恢复 workspace/tool 副作用；[#3602](https://github.com/QwenLM/qwen-code/pull/3602) 在异常退出前 await 记录 flush，补 #3581 异步记录链的退出路径；[#3581](https://github.com/QwenLM/qwen-code/pull/3581) 本地热路径同步 I/O/缓存修补且注明缓存陈旧窗口；[#3318](https://github.com/QwenLM/qwen-code/pull/3318) 预连接在代理/私有 CA/sandbox/自定义 baseURL 下跳过。本书 Ch81 已明确 conversation+environment 不能单边 rewind，Ch84 已把工具收据/文件/进程与恢复点联合提交，性能与执行身份也需同一路径验收；这些实现没有改变已有长期职责或提供新的失效反证。release 内 UI/语言/SDK修补亦不因新增功能自动准入，故家族贡献前关闭、不评分、不写 Books。release `published_at` 仅证明版本发布在窗内；PR 合并日更早时不重报机制首次公开，其他 Qwen 仓库不由此判零。

当前使用本窗 arXiv 公告批次的原始身份线索，而非旧 V2.1 `Complete` 或旧 48 分母。已逐项浏览 DataCite 初建库存 339 个标题，再以官方历史 `oai-list-identifiers/2026-04-27-cs.xml` 的本 ID 段反向补得 69 个身份及官方 arXiv API 标题。两种入口可能有交叉分类、修订与 DOI 登记漏项；此处不把 408 直接称全量当窗发布数或必须逐篇全文读的队列。范围清楚的领域论文以标题具体关闭；AI System 主线或含糊者读完整题摘。OAI datestamp 不是首次公开时刻，日期仍用官方 announcement 规则、相邻 ID/OAI 和 exact-v1 组合判断。

## 旧 48 线索重判：直接关闭的典型家族

- `2604.22179v1` 只验证 MNIST 10 类 SNN 在 80MHz FPGA 的软件→板卡复现；无大模型训练/推理/平台工作负载桥，前分母关闭，不因“加速器”一词保留。
- `2604.22306v1` ASP 代码生成 10 个图问题/8 模型，属于特定声明式语言 benchmark；没有改变一般 code-agent 验收合同，前分母关闭。
- `2604.22230v1` 通用机器学习竞赛的均衡博弈和奖金结构，非大模型系统的发布/评价控制机制，前分母关闭。
- `2604.22294v1` 自动系统综述 evidence table/reconciliation Agent，属于复用成熟抽取与代码分析的领域 workflow；摘要未给不同于 Ch81/76 现有 typed evidence/provenance 与验证的长期控制边界，前分母关闭。
- `2604.22679v1` 招聘 AI 供应链责任/法律分析不属目前大模型与基础设施主线，前分母关闭。
- `2604.22748v1` L1/L2/L3 × law regime 的跨领域综述 taxonomy，未单独给可验的新状态/评估机制；AI for Science 部分又超当前范围，前分母关闭。
- `2604.22199v1` 机器人未覆盖任务触发 LLM 分析、学习、再写本地方法库，在受测任务上降低 calls；仍是特定机器人应用中的既有技能学习循环，不因可映射 Ch25/84 自动保留。
- `2604.22427v1` 数字孪生隔离下的自动进攻渗透框架，实测 8 场景；重点是特定 offensive-security workflow 与风险减损，不是本项目平台通用授权/隔离验收新责任，前分母关闭。
- [`2604.22446v1`](https://arxiv.org/html/2604.22446v1) OneManCompany 的 Talent Market/E²R 公司比喻组合已有 role、skill、DAG 与 supervisor review。已定点核 exact-v1 §2.2.3–2.2.4：`completed→accepted`、dependency-ready、bounded retry、bottom-up completion 与 Ch81 已有 workflow state、effect/review、retry/blocked/terminal 分权一致；其“每个 task 必达 terminal/无死锁”也不能直接采用：FSM 定义的 terminal 仅 `finished/cancelled`，却允许 `failed/blocked` 和预算触发 `pause`，并未给动态新建子任务全局上界。PRDBench 50 项、self-evolution 未消融和约 $6.91/task 的受限结果未改变现章下一设计判断。**具名前分母关闭**，保留保证缺口作为反例；若作者给出覆盖动态扩图与失败/暂停状态的完整条件和证明，再定点重开。
- `2604.22513v1` 网络配置修复基准以形式验证评价 231 个拓扑问题；具体验证器与外部真值门槛已有 Ch66/81 控制主线，本篇只在网络操作域提供对照，若无新增 owner 命题则前关闭。
- `2604.22659v1` UML 作为代码生成输入的 repo benchmark，揭示域内模块级/整仓策略差异；与现有 coding-agent 仓库状态/测试闭环相比尚缺独立长期机制，前分母关闭。

这些是有具体题摘内容的初步 closure；独立反向抽检若证明漏掉设计反证，定点重开，不能以类别词代替贡献判断。

## 旧 48 中待核长期机制（尚非冻结候选）

- Kernel/执行合同：`22032` 8 元素 kernel contract/三态 calibration；`22312` Blackwell sparse decode 中 previous-step Top-K→threshold 验证→精确选择，正文 Ch49 已有实际段落但须重核本日归属；`22228` UCX/CUDA Graph intra-node 多路径，正文 Ch36 已有受限段落；`22050` attention layer-sensitivity→softmax/linear/remove 及 healing。`22126` GICC 只在 HPC stencil/OFI、IB 中实测，需证明与训练通信的可迁移状态/资源边界，否则关闭。
- 后训练/安全评价：`22074` outcome accuracy 与 CIR/SR 推理因果/充分性分账；`22076` 隐私 unlearning 的 direct/ICL/fine-tune recovery 三层 gate；`22082` sandbagging model organism 中 SFT+RL 与 train/deploy distinguishability，Ch66 已有具体正文；`22167` 非常见 harmful output 的 importance sampling 尾风险；`22191` RLFT 行为 canary 非 verbatim membership；`22117` diffuse pretrain seeding 延迟触发的威胁边界。
- Agent/外部状态：`22136` intent→当前真状态/策略判定→执行与审计链；`22193` 用户/文档/参数三源 assertion 冲突；`22436` Agent 描述相似度 vs execution-grounded 适配检索；`22708` multi-agent failure attribution 的输入完整 trace 分母。`22273v1` 两态 EIR/ECR self-correction 决策阈值；库存后稿标题/摘要不可回填到 v1。
- 多模态/训练与模型：`22152` 离散扩散 world model 作为机器人 policy 评价代理，需区分 proxy 成功与真实执行；`22238` persistent semantic graph→代码 planner→VLA 视图条件；`22409` oracle text state 与 raw visual belief 的分层评估；`22575` MoBA+SSE 混合注意力、Transformer→hybrid 转换及双平台量化；`22591` VLA 物理风险场景生成与受限 guard。
- 其它有条件项：`22565` 不删原文的 task-reward 学习 evidence highlighting，比较 Ch75 压缩与 Ch76 证据路由；`22753v1` 异质成本 pilot run→目标区外推准确度的顺序实验设计，Ch28 已有实际正文，注意旧库存含后发方法名而官方 v1 摘要没有；`22520` 翻译专域 small→large marginal-gain 路由须判断是否超 Ch49/成本现有原则；`22430` 通用 GPU MPS/MIG 配置研究须有大模型资源管理新条件才可入；`22452` 社交 Agent 平台浅交互否定“数量自然产生群智”，须判断 Ch83 已有相同可迁移评估边界。`22577` 已按下文 Method/Table 2 完成定点关闭，不再挂普通待核。

旧 48 中其余与领域/局部方法有关的线索（例如 `21999` 单 block Sudoku ACT memory、`22072` serverless FL 梯度分片、`22085` vendor memory schema、`22128` Dyck attention probe、`22345` personalization head steering、`22411` background temperature 短 note）需与真实 owner 逐项比较后具体前关闭或有限候选；不继承旧高分。`22597` 的定点核与关闭结论见下文，不再留作普通待核。上述待核项不能全变成全文队列。

## 补得 69 个 OAI 身份的双向检查

官方 API 的完整标题列表中，绝大多数是医疗/教育/交通/电信 ISAC、纯数学、PDE/数值模拟、金融、社会研究或 SNN/HPC 非基础模型工作负载，直接按其具体对象在前分母关闭，而非对全部逐篇全文。需完整题摘定点核的例外：

- [`2604.21964v1`](https://arxiv.org/abs/2604.21964v1) 外部独立审查 DeepMind scheming-inability safety case，摘要明确指出风险论证 scope/决策适用性的实质缺口，可能改变 Ch66 safety-case admission；不能因论文来自安全治理就排除。
- [`2604.22149v1`](https://arxiv.org/abs/2604.22149v1) SV-MPC 抽样式 autonomous-system safety filter，关注的是 nominal action 下的 probabilistic restrictiveness；应用是通用车辆避碰，需对 Ch26 VLA physical safety 与形式/实证 gate 后判能否贡献，不能只凭“filter”保留。
- [`2604.22384v1`](https://arxiv.org/abs/2604.22384v1) Reelay 的 LTL/MTL/STL online monitor→synchronous dataflow graph 服务 cyber-physical telemetry；本项目已有 Agent/Infra runtime temporal monitor，若无 LLM/Agent 特定新桥，可具体关闭。
- [`2604.22624v1`](https://arxiv.org/abs/2604.22624v1) 多目标 online monotone co-design 的 optimistic certificate/sample elimination，实测 fleet/mobility，非模型系统 workload；若只可类比 AI pipeline 搜索则前关闭。
- `2604.22589v2` 是同 OAI 日变化中的后修订，不以它当本日新论文；其 Monge–Ampère 数值方法也与项目无关。

69 个的官方 API 题名恢复入口为 `https://export.arxiv.org/api/query?id_list=<69 IDs>&max_results=100`；原 ID 集由本地 04/27 OAI cs 记录限定 `2604.21932`–`2604.22753` 后与 339 identity 求差得到。后续只审相关/含糊项，不扩纯数学全域。

## exact-v1 题摘校准（本轮增量，仍非冻结分母）

旧库存确有后稿污染：`2604.22273v1` 官方题名为 *When Does LLM Self-Correction Help? A Control-Theoretic Markov Diagnostic and Verify-First Intervention*，不是旧库存的后发题名；`2604.22753v1` 摘要没有旧库存后来出现的算法名。下面仅以 `https://export.arxiv.org/api/query?id_list=<ID>v1` 的精确版本题摘准入，不能把 v1 `Submitted` 当首次公开。

- `2604.21964v1`：外部评议 Google DeepMind scheming-inability safety case 指出 risk claim 的 scope 与部署决策适用性问题，形成 safety-case 独立证据准入线；需读评议具体缺陷/作者可得回应并对照 Ch66，非所有治理评论都候选。
- `2604.22032v1`：ML kernel 八字段 contract、reference/violation 双侧校准可作为执行结果争议的可审规范；须比较 Ch66 kernel 物理下界与 Ch49 correctness/precision 既有内容，不能仅因列 schema 就加书。
- `2604.22074v1`：RLVR outcome accuracy 与 CIR/SR（推理对答案的因果重要性、推理自身可独立求解性）分账，是训练评价合同候选；不能把 auxiliary rewards 的受限实验推广为推理普遍真实。
- `2604.22076v1`：direct reveal、in-context recovery、fine-tune restoration 是不同隐私遗忘 adversary；需与 Ch72 现有 unlearning/恢复边界逐项对照，若已有则不强写。
- `2604.22127v1`：混合语言模型 LoRA 的 attention/recurrent placement 对 sequential/parallel 拓扑呈相反结果，改变 adapter owner/placement 决策，候选；仅两小模型与五 benchmark，不能写拓扑因果普律。
- `2604.22167v1`：用不安全 proposal model 做 importance sampling 估计 harmful-output 稀有尾概率，测量对象是同输入下输出分布尾部而非只寻找危险输入；候选安全 evaluation contract，方法偏差与模型替代边界待必要审阅。
- `2604.22180v1`：passage 单 embedding 与 LLM listwise reranker 联合训练、单步 score 为检索与重排成本分账的具体候选；是否改变 Ch76 表示/执行取舍待比对，不因 benchmark 较高就直接入 Books。
- `2604.22191v1`：RLFT 被保护检索内容的影响可能以触发条件下的行为风格而非 verbatim 记忆显现；1% 注入率下仍有明显漏检/误报，属训练合规审计候选，不能把 canary 命中当违规的充分证明。
- `2604.22215v1`：3–9B、Q5_K_M、greedy numeric elicitation 几乎饱和，反证 verbal confidence 可直接作为 item-level calibration input；若 Ch66 已有同等 probe admission，拟 Existing/Only，仍须记所测分母，不能称所有模型无内部不确定性。
- `2604.22266v1`：forced-answer intermediate readout 显示某受测模型在生成中早锁答案，停止可省 token 但有 2% accuracy 代价；候选仅限 stop-controller 的 evidence calibration，不能把 forced readout 直接当线上 oracle。
- `2604.22271v1`：PANL 激活对错误可修复性有独立预测与干预，但只在 Gemma/Qwen、TriviaQA/MNLI 测；可作诊断候选，不能宣称内部 confidence 可直接用于任意线上 Agent 决策。
- `2604.22273v1`：自校正的 ECR/EIR 与初始准确率给出迭代准入阈值，verify-first ablation 为受限因果证据；候选 Agent feedback controller，须检查两态 Markov 与多轮实际过程边界。
- `2604.22335v1`：source-supported token logit boost 以 context/no-context divergence 和 attention/semantic support 调整解码；当前只表明局部 faithfulness 策略，若现有 Ch76/49 已有 source/evidence gate 与 token routing，本篇可能前关闭或仅报告，必要全文不先扩。
- `2604.22407v1`：Adam 二阶矩在梯度投影/重放混合下可改变旧方向有效学习率，提出一阶/二阶职责分离；有真实 optimizer control 边界，候选，受限 8/16-domain stream、7B LoRA 不自动推普遍连续学习。
- `2604.22442v1`：HubRouter learned hub→fingerprint→稀疏 council/causal 修正提供具名设计反证，旧泛化前闭已由 root 撤销，恢复 2+1+2=5 标准候选；Ch22 现有 selector/anchor/混合及回退已承载长期选择，Books 仅报告。pretrained retrofit 失败、未优化 PyTorch 的 90× 非生产收益，具体证据见[同理由子集反查](V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)。
- `2604.22661v1`：同信息需求的 query variant 用廉价 pre-retrieval predictor 选择，nDCG 优选与生成答案效用错位，是 Ch76 query/admission 具体候选；须核同成本 matched 比较和现有 owner 是否已有相同 relevance≠support 分账。
- `2604.22678v1`：每份文档独立条件生成、按生成 token 更新文档后验，可把 RAG 的拼接长度/证据归因/剪枝联到单一状态；候选，但视觉 QA 为主要实验，不能称 Bayesian 后验就是事实真值或一般 RAG 更快。
- `2604.22709v1`：保留词表的离散 latent-CoT 通过 CoT bottleneck/SFT→自蒸馏→受约束 RL，可能改变 reasoning-token 成本/训练表示取舍；须对 Ch33/推理压缩既有分支和真正总训练成本核查，11.6× token 不等端到端效率。
- `2604.22722v1`：以 LLM perplexity-reduction utility distribution 蒸馏双塔检索器，属于‘离线付 LLM 监督、线上用便宜 encoder’的具体候选；若 Ch76 已完整承载 relevance vs answer utility 与后验重排，可能只 Report Only，不凭 180× headline 写书。
- `2604.22750v1`：八个 frontier model 的 SWE-bench Verified token 输入成本/运行方差/成本预测弱相关，支持 Agent 预算与 pre-run cost estimate 不能作硬承诺；候选评估反证，但旧 Ch84 已有 stop-controller/usage receipt，需具体比较再决定是否在分母内。

本批前分母明确关闭：`2604.22653v1` 是一般软件 verifier warning 与 human code-comprehensibility 的弱相关反证，非 AI Agent verifier 的任务真值合同；`2604.22126v1` 若只有 HPC stencil/OFI/IB 下 GPU-initiated 通信收益而无模型训练负载/资源机制桥，应关闭。`2604.22597v1` 已按下文 exact-v1/Ch66 定点核后关闭；前两项仍可对特别强的跨主线机制反例定点重开，不因关键词一次性冻结。

[`2604.22597v1`](https://arxiv.org/html/2604.22597v1) 不是单纯 formatter：§3 先让 judge 独立求解并校验 dataset GT，再对回答的数学等价/单位/格式做多次判分，§4.2 在 Qwen2.5-7B 输出的 640 条人工标注答案上给出较 symbolic baseline 更高的受限 F1。这个受限证据有价值，但 Ch66 已区分 reference coverage、semantic matcher、judge/人工复核和 parser identity，且要求不能把未匹配参考答案直接判错；本篇没有额外独立的发布权或未被现章承载的设计转移。作者也承认多次 judge 调用成本、偏差、框选答案抽取假设和人工集范围。故**具名前分母关闭**，保留数学表示反例与独立参考检查作为现有评价合同的案例，不把 F1 当任意任务的真实性概率；若后续证明当前 reference/matcher 分层在受控切片上失效，再定点重开。

## 旧高分反向收紧（第二批 exact-v1 完整题摘）

以下只解决能否进分母，不以局部学术有效性作否定：

- `2604.21999v1`：单 block UT 的 Sudoku-Extreme 中 scratch memory 下限与 ACT router 初始 bias 陷阱确有机制，不能从 57% exact-match 写成现代 LLM 通用 memory 规律；**反向校准后恢复为候选待标准审阅**，因 Ch17 现有 depth-state 路线尚未处理“循环计算开始时 halting prior 把训练困在浅层、需与显式 scratch slots 联合校准”的窄设计边界。小任务不是排除理由，后续先核 init/seed/固定深度对照，再定 Books。
- `2604.22072v1`：Serverless FL 把 FedAvg gradient 按参数 shard 分摊以绕单 function 内存上限，实测 VGG/43MB–5GB；当前主线是大模型训练平台而非 FL/Lambda 聚合，且 elementwise sharding 是该域实例。前分母关闭；“bit-identical”摘要主张也未给浮点 reduction order 证明。
- `2604.22126v1`：GICC 的 finite NIC state 回收与 GPU fast-path 协调具体且成立于 OFI/IB，但受测主 workload 是 stencil/halo、工业 proxy；没有大模型 collective/训练执行对照或可迁移协议身份变化，故按当前项目范围前分母关闭，不以 229×/25% 写 AI 训练收益。
- `2604.22128v1`：Dyck/模板自然语言上 decodable residual variable 与 causal attention use 分离，是解释性探针案例；Ch66“可解码 Failure Direction 不拥有自动纠错权”与§测量声明的 estimand/intervention gate 已具体区分 probe/readout 与因果使用。本篇受控对照虽显示 top-of-stack attention mask 影响长距离准确率而低维 residual ablation 较弱，仍只校准既有主张在人工语法上的例证，未改变评价或模型的下一选择，故在前分母关闭；不是因为模型小而排。
- `2604.22242v1`：Bandicoot C++ template expression fusion 相对 Armadillo/PyTorch 等一般 GPU 线性代数实现，并未给大模型 kernel/数值或执行路径新的约束；前分母关闭。
- `2604.22345v1`：Preference Heads 的掩蔽/对比 logit steering 是个性化局部机制，结果只证所测 head 与输出风格关系；不提供 Agent memory/权限或模型平台可迁移新设计条件，前分母关闭，不把‘causal’词直接升级为长效 owner。
- `2604.22411v1`：Background Temperature 短 note 给 T=0 环境扰动的等效温度定义和 pilot；Ch66 已要求固定 inference/kernel/env identity、重复测定与最终行为分账，本篇没有受控证据改变该发布判断，前分母关闭，不能用等效标量充真实 sampling 温度。
- `2604.22430v1`：MPS/MIG 多程序共享下弹性/隔离与内存争用取舍是一般 GPU 共址证据，未测模型服务/训练负载或改变现有 GPU isolation/accounting 条件；前分母关闭，30% 等仅所测 profiles。
- `2604.22571v1`：LARA 的 DFT/atomistic HPC Agent 受控执行、dry-run、RAG 修订为 AI for Science 应用组合；现有 Agent effect authorization/外部 oracle 边界可解释，不以 HPC 一词入当前分母，前关闭。
- `2604.22577v1`：QuantClaw 的 Method §2.4/§3 与 Table 2 已核；rule/轻分类器把任务类型映射到离线 task–precision profile，运行时在现有模型变体池选择。GLM-5/PinchBench v1.2 固定 INT4 成本和时间低于动态路由、后者平均分略高，是局部质量—成本折中而非三维支配；与 Ch49 格式/任务切片质量、真实执行成本和高精度回退比较后，**前分母关闭**，不因 21.4% headline 保留。
- `2604.22452v1`：MoltBook 社交 Agent 的稀疏浅交互解释规模未自然产生集体智能；作为 Ch83 假设反证可保留定点摘要比较，但若 Ch83 已有同等交互深度/通信拓扑评估，不因 2M 用户与新的 benchmark 入分母。

第二批值得继续必要证据的不是全部旧分母：`2604.22050v1` 的层敏感替换+healing 有长上下文架构/高并发取舍；`2604.22136v1` 结构化 intent→真实状态/policy→effect 的形式条件需和 Ch72 原授权链比对；`2604.22152v1` world-model proxy 对真实机器人 policy 的评价权力；`2604.22238v1` 持久 graph 与 VLA 短程执行的状态交接；`2604.22312v1` exact sparse Top-K 的 previous-step hint 仍须 threshold verify，已有 Ch49 真实写入；`2604.22409v1` oracle textual state 对 raw visual belief 的分层评估；`2604.22436v1` Agent 描述检索与执行信号之间的偏差；`2604.22520v1` small→large 的条件边际 gain 而非绝对质量路由；`2604.22565v1` 保留原文但强调证据的独立输入变换；`2604.22575v1` MoBA/SSE hybrid 及转换成本；`2604.22591v1` 物理风险场景设计/防护。它们都还未自动成为冻结候选；已有覆盖与原文方法/负例需定点核。

独立校准提醒后又核 Ch75 “Compression 之外还有一种保留全文、只改变注意入口”真实正文：它已经逐项写到 HiLight 的 frozen Solver、Actor span tag、tagged-view identity、额外 selector 成本、不可把 span 当因果 evidence 及短 context/硬预算回退。因此 `2604.22565v1` 的题摘机制确实有当前项目贡献，应保留候选，但 Books 当前为 **已有覆盖（AGENT-CONTEXT，Ch75）**，不是误称“因已有就不准入”、也无需重写同一段。后续核 exact-v1 实验条件，不从报告摘要冒称所有基准。

## 标题反向抽查：非旧 48 的主线与邻域

在 339 条标题中定点读取完整题摘，再以官方 exact-v1 对真正可能改长期判断的家族做必要核：

- [`2604.22509v1`](https://arxiv.org/html/2604.22509v1) LaissezCloud：运行中的 accelerator/training 资源不是 launch-time on-demand/spot 两选一；§2–4 把租户私有阶段效用/重配置成本与运营方私有 power、拓扑压力经价格窄接口接到持续报价、集中匹配与迁移/让出。现有 [PLATFORM-GPU-SCHEDULER Ch63](../../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) 已有 queue、reclaim、checkpoint 代价，却未见跨互不信任的 tenant/operator 持续资源合约；保留工作候选，拟 2+2+2=6、实际 Books gap 深入待非作者采用。只把 8–23% 等当所披露异构 workload/配置结果，不把价格当授权/公平真值，§7 的市场波动和非价格限制必须保留。
- `2604.21950v1` 小模型 Code pipeline 的 execution feedback 主要修 NameError/SyntaxError，逻辑错很少改善；simple generate-execute-refine 与专用 code model 在所测 HumanEval/MBPP/单 laptop 下较复杂 topology 更值得，额外 loop 无早停净负。但现有 Agent code outcome witness/stop controller 已要求执行证据、预算和净收益，本篇只为 1–3B 局部组合提供反例，前分母关闭；不因 code-agent 词汇保留。
- `2604.22028v1` FlyCatcher 从软件测试推断 shadow-state runtime checkers，400 tests/四系统，没有 LLM/训练/推理 workload 适配或 Agent outcome 发行边界；测试→checker 是通用软件方法，前分母关闭，不因使用 LLM synthesis 自动准入。
- `2604.22171v1` MCI 用 maximal-clique cover/densification 做 arbitrary-filtered ANN，是具体索引结构与十数据集结果；当前 Ch76 已按检索目标、过滤条件、recall/延迟/容量联合验收，摘要未给 AI memory/RAG 中不同 state/evidence 权限或修正原设计反例，前分母关闭，不因向量库相关就 retain。
- `2604.22360v1` NAC 对已训练回归网络的 OOD/uncertainty extension，题摘只给该估计器优于 MC-dropout 的局部对照，未改变 LLM/Agent calibration/decision contract，前分母关闭。
- `2604.22583v1` BudgetFormer 每输入 head budget 只在文本分类任务报告 FLOPs/内存，未证明 LLM 长上下文 decode/prefill 的真实 kernel skip、端到端/SLO 或质量边界，属于局部架构方法，前分母关闭；不是“小模型”本身硬拒。
- `2604.22603v1` Chamelio 给共享云网络 datapath 的 bounded eBPF handler/tenant slow path 与 runtime cycle accounting，能保护通用租户网络隔离，但全文目标是自定义 TCP/通用协议，当前 AI System 训练 collective、推理 P/D transport 或 model-serving workload 均未出现独立机制桥；本阶段前分母关闭，不拿其通用网络性能数外推模型 SLO。

本节 raw snapshot 的摘要可受后续版本污染；上述“保留”必须据官方 exact-v1 独立确认（LaissezCloud 已核），明确排除项如独立抽查发现实质 AI 负载桥再定点重开，不机械重读全部 339 篇全文。

## 否定侧新发现：2604.22438 水印注入分组待独立准入

旧 owner receipt 对 [`2604.22438v1` SSG](https://arxiv.org/html/2604.22438v1) 的关闭理由只是“局部模型/优化方法、无可复用 state/data/control ownership”，与官方 exact-v1 §4.1–4.4、§5.1/5.4–5.5 不吻合。该文针对 KGW 在 code/math 等低熵生成中随机 green/red 划分可能把高概率 token 放同侧、使注入概率移动接近零的失效，提出按 logits 相邻配对并以 key 分边；实际实现只在 top-k 排序配对，其余随机。它改变的是生成时的 keyed partition、概率质量和 detector 重放身份，不是一般优化器配方。Ch72 当前 provenance/watermark 段已写低熵携带容量、key/采样配置及检测不可单独当真值，但未明确“随机按词表数平分不等于按当前概率质量平分”的注入侧控制条件；因此旧模板关闭理由不足以支持前分母排除。

反证与成本也必须一起保留：全文每 token 排序昂贵，top-k 实现不同于全词表理论配对；§4.4 的下界随 top-token 概率趋近 1 仍可趋零，不能说任意低熵时有统一严格正的检测保障；§5.1 的代码/数学结果存在质量下降切片，§5.4 无原始 prompt 时增强有正有负，§5.5 paraphrase 使 TPR 普遍下降且跨模型差异明显。它不证明生成来源真实、抗改写或生产时延。原始 receipt 字段为 submitted `2026-04-24T10:55:50Z`、v1 Updated `2026-04-27T00:34:20Z`、DataCite created `2026-04-27T01:37:27Z`、OAI datestamp `2026-04-27`；这些不是单篇首次公开日志，若恢复候选仍要沿本日公告/相邻 ID 联合日期链并检查例外。

**非作者准入与日期链复核后：**[apr20 独立审阅](V3_APR20_SSG_INDEPENDENT.md)确认旧关闭理由不成立，按 2+2+2=6 恢复为具名标准候选，并确认 Ch72 的窄知识缺口；这不自动授权 Books 写入。官方 [abs/v1](https://arxiv.org/abs/2604.22438v1) 的 `2026-04-24T10:55:50Z` 是 submitted 而非首发。官方[公告规则](https://info.arxiv.org/help/availability.html)规定 ID 在公告阶段赋予、Sunday 20:00 ET 常规公告；本日原始 owner receipt 的该 ID `v1 Updated=2026-04-27T00:34:20Z`、`OAI datestamp=2026-04-27`、`DataCite created=2026-04-27T01:37:27Z`，相邻 `22436/22439/22442` 同为本批 00:34Z/01:37Z，04/28 下一批从 `22754` 的 `2026-04-28T00:00:05Z` 开始。字段各自不等于 first-public；合并公告规则、连续 ID、OAI 及精确 v1 后，只把该家族有界推断为 `2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00`，非逐篇日志确证。正式工作分母据此暂为 36，但尚未冻结；Books 仍待 root 写前采用、共享章实写和另一人的写后复核，不把这一次抽检概括为全部 408 身份已通过否定侧 Gate。

## 同类泛化排除理由的第二个具名漏收：2604.22550 ArmSSL

旧 receipt 用“局部模型/优化方法、无可复用 ownership”关闭 [`2604.22550v1` ArmSSL](https://arxiv.org/html/2604.22550v1) 也不成立。作者本轮读官方 exact-v1 摘要、§I/III–V 起点与 Ch72:827–850：Ch72 已有**生成内容** watermark/低熵容量及 key 信任根，但没有 foundation encoder 被盗后经下游 classifier 适配、验证者只能读 black-box confidence vector 的模型归属接口，也没有“水印样本在表示空间形成 OOD 密簇，反成为攻击者检测/移除线索”的具体设计边界。[apr20 非作者必要审阅](V3_APR20_ARMSSL_INDEPENDENT.md)定点核 §III–VI、真实 Ch72 owner 与主对照，确认 2+2+2=6 标准候选值得恢复；不是因视觉 SSL 或论文声称“鲁棒”而准入。主表冻结 encoder 训练下游 head，不等于任意 fine-tune；64 个负模型观测 FPR 0% 不是总体零；§VI `ψ=.1` 的 GTSRB/SVHN 自适应攻击实际可移除信号且约损 20% utility，因此不采“可用即永可验”的宽保证。Books 只留 Ch72 窄 source→owner 待 root 深入采用/写锁，未实写。

官方 [abs/v1](https://arxiv.org/abs/2604.22550v1) 的 `Submitted=2026-04-24T13:40:25Z` 不是首发。原始 owner receipt 给 `v1 Updated=2026-04-27T00:40:48Z`、`OAI datestamp=2026-04-27`、`DataCite created=2026-04-27T01:40:14Z`；相邻 `22549/22551` 分别 00:40:47/00:40:56Z、01:40:12/01:40:15Z，下一 04/28 批从 `22754` 开始。按[官方 ID 公告赋号/Sunday 20 ET 规则](https://info.arxiv.org/help/availability.html)、相邻同批身份、OAI 与精确 v1 的组合，暂有据推断首公告在 `2026-04-27T08:00:00+08:00 ～ 2026-04-27T09:00:00+08:00`；任何单字段都不是逐篇 first-public 日志。该项使临时工作分母 36→37、普通 Books 待办 9→10，仍不冻结或提前日 Gate。

这次只反查受旧泛化理由影响的 watermark/provenance 近邻，不扩 408 身份为新全文队列。`2604.22220v1` 是生成图像水印的频域 diffusion 移除操作，完整题摘只给该视觉攻击/保真局部方法与跨受测 scheme 的作者宣称；Ch72 已明确 embedded signal 会在对抗变换中失效并须与签名/原始证据交叉，当前未给新的长期归属判断，维持具名前分母关闭。`2604.22335v1` 借用水印式 logit bias 增强文本 context 支持，并以有/无 Context 分布差、attention/语义相似度调偏；完整题摘尚只支持 summarization/QA 的局部 faithfulness operating point，Ch76 已把来源支持、条件解码与独立答案 Gate 分权，当前没有证据使 token boost 取得事实授权或改变长期回退条件，维持具名前关闭。二者若日后出现能改变上述具体判断的受控反证才定点重开；不因同词自动恢复。

## 旧高分的定点反向关闭：不能用局部系统名替代贡献

- [`2604.22085v1`](https://arxiv.org/html/2604.22085v1) Memanto 的确直接研究 Agent memory，不能因厂商系统或已有 Ch77 排掉。定点读 §III–V 后，五阶段消融始终使用同一 Moorcheh 向量后端，主要依次改变 top-k/阈值、提示词和 reader 模型；没有独立隔离“13类 typed schema/冲突解析/时间版本”相对 graph 的贡献。跨系统 Table IX 汇集各家已发表结果，不是同候选池、reader、成本与工作负载的匹配比较；Table X 自述 0 次 LLM-per-write 仍列 `<10ms` ingestion，不能称所有写入/索引成本为零。§V-E 还承认仅 LoCoMo/LongMemEval 会话事实问答，非会话 Agent 与并发规模未测。Ch77 已按任务和写后即时可见性选择索引/表示，并要求成本、召回、权限/版本分别验收；本文没有足以把“vector-only 一查询全面取代 graph”升为长期设计判断的隔离证据。**前分母关闭**，保留上述具体未证与受限 recall 调参结果；非因模型小或已有章节而关闭。
- [`2604.22452v1`](https://arxiv.org/abs/2604.22452v1) Superminds Test 在 MoltBook 上用 probing agents 测联合推理、信息合成与基础交互，观察大量 Agent 但讨论浅、单轮回复居多。这提供受限社会平台反例，却没有控制 communication topology、参与/任务分配或平台选择偏差，也未证规模本身对指定分母应产生能力。Ch82 已区分单体通过与多体 composition 及通信拓扑；该文不能从一个平台的 shallow interaction 推出新的可操作系统边界。**前分母关闭**；保留“人数不等协同证据”的否定例，不把原站用户数当实际协作机会分母。
- [`2604.22577v1`](https://arxiv.org/html/2604.22577v1) QuantClaw 的 Method §2.4/§3 将任务分类、离线敏感度 profile 和模型变体池联接；Table 2 的 GLM-5/PinchBench v1.2 中固定 INT4 成本 `0.0105`、时间 `32.19s`，动态路由 `0.0119`、`33.21s`，后者平均分 `89.09` 高于 `88.24`，是质量—成本折中而非三维支配。Ch49 已要求格式/模型/任务切片质量与真实执行路径联验，故作为受限实例**前分母关闭**；不把作者 `21.4%`/`15.7%` 外推跨模型/并发 SLO，也不因 OpenClaw 名称自动准入。

## OAI 补得身份的定点准入边界

- [`2604.22149v1`](https://arxiv.org/abs/2604.22149v1) 的官方题摘对象是单／多车辆避碰：SV-MPC 从控制序列样本近似安全条件后验，采样候选全不安全时覆盖 nominal input；scenario 论证的是受限 restrictiveness。Ch26 已区分 VLA proposal 与低层 safety filter 的物理提交权，且有离散控制周期的一步可达域约束；本文未测 foundation-model policy、VLA action chunk 或不同模型提议的安全／延迟分母，现有题摘不足以改变该主线。**前分母关闭**，不否认其在车辆控制域的概率约束；若有 VLA 控制链的独立接口证据再定点重开。
- [`2604.22384v1`](https://arxiv.org/abs/2604.22384v1) 将 LTL/MTL/STL 等规范编成同步 dataflow graph，并支持离散／稠密时间与 delta-encoded 行为；评价是 cyber-physical stream 与嵌入式／机器人场景。它没有给出 Agent tool trace 的权限／状态身份、LLM 评价 oracle 或模型服务监测的不同设计选择；这些形式语义也不能从泛 runtime-monitor 词汇直接移植为本项目发布保证。**前分母关闭**，保留它作为特定监测器实现而非主线候选。
- [`2604.22624v1`](https://arxiv.org/abs/2604.22624v1) 的 optimistic certificate／淘汰采样为偏序多目标系统 co-design 提供方法，实测多机器人 fleet、交通与合成单调／Lipschitz 任务。当前 Ch66 的配置 Pareto、硬约束与实际硬件／失败分布复核是 AI 系统决策主线；本文未以训练／推理负载或模型平台资源为对象，也未给改变该 Gate 的独立反例。**前分母关闭**，不因“online”“multi-objective”可类比调度而升为 Books 候选。
