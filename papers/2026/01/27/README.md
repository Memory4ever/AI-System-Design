# Daily Research — 2026-01-27

**规范：** V3
**窗口：** 2026-01-26T09:00:00+08:00 ～ 2026-01-27T09:00:00+08:00
**补充窗口：** 2026-01-26 ～ 2026-01-26
**窗口说明：** 用户授权本轮仅补已有 Daily 的来源遗漏；原窗口、37 家族候选、日期、评分及有效审阅保持，不搬移旧材料。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T08:09:59+08:00

## 1. 结论

2026-10-08 增量补查只处理 1 月 26 日北京时间完整自然日遗漏，原报告完成结论属于上一轮有效研究，不代替本轮验收。已保存[原报告基线](_sources/supplement-original-20261008.md)，14 每日入口及四类有限 arXiv 主题已实际补查；37个具名完整题摘分为23新增候选、11贡献前关闭及3日期保留，另1医疗维修标题明确范围外不计完整AB。新23项必要 exact-v1 审阅与root逐项独核完成（5深入/18标准），Books=4整合+1具体已有覆盖+18仅报告；连同原37，当前60家族、17深入/43标准、8整合/5已有/47仅报告。四处增量正文为Ch12查找无冲突与学习质量分账、Ch33 best-turn效用与同history动作组、Ch66 data-withheld负控制/过滤人口、Ch77社区derived prototype/维护周期，root实际source/PRE/正文完整邻接/末注POST通过。root已实际完成六部分DAY独立验收并授予通过，本轮完成。截断接口、空搜索、动态目录失败及日期/子命题争议不授零事件或全源正面覆盖；原37行和原§4连续正文保留，下文原结论只属于上一轮。

本日有三类需要分账的增量：理想Attention对称性不能直接移植有限浮点实现；checkpoint异构状态语义与byte movement分离仍须captureepoch/背压/restore；Agent与多模态评价应区分信息接口、几何合法与真实执行。其余局部机制与反侧按各自配置保留，不合并为普遍性能或安全结论。

发现采用有限主题查询、官方目录片段和必要精确事件恢复，不把103条模型查询或全年目录当候选/全文队列。本日冻结候选37唯一家族（36篇arXiv精确v1＋Kimi CLI0.88）；原作者36项必要审阅和独立重开LogitMatch共37/37，独立必要证据37/37，日级语义验收通过。已有具体贡献关闭4项及LongCat早正文去重，另4项必要日期隔离，不冒正面候选。Books已实际整合4项/4文件（MODEL-POSITION-ENCODING、MULTIMODAL-GENERATIVE-PARADIGMS、INFER-SGLANG、TRAIN-SFT），具体已有覆盖4项（TRAIN-CHECKPOINT、AGENT-MEMORY、PLATFORM-EVALUATION-SYSTEM、AGENT-PLANNING）；其余29项仅报告，逐项具体采用对象/长期差额已核；不把报告-only当book写入。

Ch13实际22/31/33–35行修正了无条件的排列等变解释，root必要原源与写后衔接POST通过。没有运行论文代码、复现实验或验证GPU/生产行为。外部目录/日期保留不支持无遗漏、Coverage通过或正面安全保证；四处整合均获非作者实际必要源→正文/邻接POST；没有普通可执行待办。

## 2. 来源覆盖

原执行2026-10-04的有效范围见[原有限发现](_sources/discovery.md)，本轮2026-10-08只补Jan26自然日和ROADMAP模型/训练/推理/平台/Agent/多模态主题。下表更新本輪实际入口、有限恢复与停止位置，完整原件路由见[有限补查](_sources/supplement-discovery-20261008.md)；原夹窗有效证据只作身份/claim一致复用，本轮失败或空搜索不升级Coverage。结果“已检查”只指表中实际范围，不是完整官网历史覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research当前可读切片；Jan26模型/训练/推理主题有限site补检，native-0/search-0/2；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 当前目录未到Jan26历史段；社区命中只发现，空搜索不证明零。原有效业务/voice关闭仅身份一致复用。 |
| SRC-ANTHROPIC | Research当前可读切片及单源Jan26定点补检，native-0/narrow-recovery；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 未恢复Jan26官方历史列段；Jan15已知窗外线索不增加本窗候选。 |
| SRC-GOOGLE-AI | DeepMind Research、Google Blog当前切片；pubs一次恢复；Jan26单源主题补检；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 当前年度分类只定位，空搜索不授零；不遍2026/全年pubs，Jan26列段保留。 |
| SRC-META-AI | Research首查返回0行，Jan26单源主题定点补检，native-0/narrow-recovery；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 空提取/空搜索非0研究；缺目标日主线相关官方列表。 |
| SRC-QWEN | 旧Qwen入口重定向/动态当前页；Jan26模型主题单源补检，native-1/narrow-recovery；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 动态历史正文范围未恢复；旧2025页/搜索不证明Jan26无遗漏。 |
| SRC-DEEPSEEK | 当前官方首页及updates可读changelog，native-1；Jan26主题补检；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 已检查 | 可见updates从Apr24跨Dec1未列Jan26，只支持此changelog；不覆盖未列研究。 |
| SRC-MOONSHOT | Platform Blog当前25条切片；原Kimi0.88确切release/PR仅身份和采用命题一致复用；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 本轮当前Blog不证明Jan26完整历史；原0.88不重列或重评，不扩repo事件。 |
| SRC-TENCENT-HUNYUAN | Research首查空；本轮动态浏览一次30秒timeout/reset；原两次有限失败身份/claim一致复用；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 不能核全部Jan26列表，有限恢复终止；空提取不是空目录，恢复需当日官方事件段。 |
| SRC-ZAI | Research首查失败，定点重开一次仍timeout，native-1/native-recovery；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 原可读Jan19–Feb2列段作为有效历史证据保留，但本轮失败不授新正面Coverage或零。 |
| SRC-BYTEDANCE-SEED | Research/public_papers切片；官方2026 ascending API paper page0/count30实际20条，首次Jan28即停；blog page0从Feb12起；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | paper Jan26两项与官方index/精确v1日期冲突；blog排序无目标历史段。不按hasmore扫全库存，日期项不入候选。 |
| SRC-BAIDU-ERNIE | 中文Blog首查timeout，再单次恢复仍timeout，native-2/native-recovery；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | 原Jan15–Jan29有效夹窗证据保留；本轮失败不证明Jan26零或完整目录。 |
| SRC-XIAOMI-MIMO | MiMo papers/blog可见切片，native-2；仅Jan26模型/attention/后训练主题；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 已检查 | 可见papers Jan8→Feb3夹窗范围复用，blog有限无确认新事件；不授全部GitHub artifact召回。 |
| SRC-MINIMAX | 中英文Blog当前列表/Agent techblog导航及Jan26单源补检；定点M2her事件页；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 已检查 | 可见Jan27 M2her→Dec23 M2.1；M2her显示Jan27不纳Jan26新增，原旧窗口日期hold保留。不是全机构无遗漏。 |
| SRC-ARXIV | 四个Submitted发现slice：model102/systems8/multi37/agent110到请求尾；相关CL/CV/AI月标题片段有界补检；本轮原件见[有限补查](_sources/supplement-discovery-20261008.md) | 受阻 | model/agent原输出截断后compact标题投影完整；三官方月目录cachemiss终止。宽库存非逐项队列，最终仅具名37完整题摘+1明确题名范围外。 |
| 表外：[MCP规范](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) | Kimi header变化触发，仅精确2025-06-18 Session Management/传输条件 | 已检查 | 非来源发现扫描；未证明任意SDK/所有server行为 |
| 补检：[DataCite](https://api.datacite.org/dois) | 选中arXiv ID的created/registered/dates恢复；identity-*.json及identity-extra.json | 已检查 | 只身份/日期上界，不能证明首公开时刻或研究结论 |

上一轮SRC-ARXIV有效分页仍保留：模型0/20/40/60/80/100共6页到103尾，系统1页6条到尾、多模态0/20共2页38条到尾；它们仅作旧有效发现依据，不将本轮不同102/8/37/110投影数量混合为当窗唯一研究数。两轮Submitted发现slice均2026-01-22T19:00:00Z～2026-01-23T19:00:00Z，本轮主题、停止与三处官方相关标题片段cachemiss见[增量有限发现](_sources/supplement-discovery-20261008.md)。失败/截断Atom不用于覆盖。Daily未扫描Weekly来源。

## 3. 候选与判断

原37项arXiv公开时间保留下述上一轮**推定区间**2026-01-26T09:00:00+08:00～2026-01-26T10:43:00+08:00，完全落原窗，非逐篇精确公开时刻。[官方availability](https://info.arxiv.org/help/availability.html)本批标准Sunday20:00 Eastern对应下界Jan26T01Z，exact-v1提交在Friday14:00 Eastern cutoff前；各DataCite created为上界（最大Jan26T02:42:29Z），共同端点向下一分钟保守扩至10:43。每项原始history、created精度/时区保存在identity-ID.json；上一轮新增6项在[identity-extra.json](_sources/identity-extra.json)。created不能当精确public时刻；早正文LongCat与跨截止上界两项已另隔离。当前精确abs/事件页没有影响采用命题的撤回/删除提示，不为证明无标记遍历全史。

表中后23项为本轮具名增量审阅集合，只按补充自然日检查，不改原37行；准入、必要证据与Books逐项处置已获root实际独核，最后六部分DAY已获root实际独立验收通过。全部采用exact-v1，不将API latest后改内容投射Jan26。新增公开日依[官方final-ID公告规则与必要上下界合取](_sources/supplement-date-policy-20261008.md)，原字段见[20项身份](_sources/supplement-date-bounds-20261008.jsonl)、[四项补字段](_sources/supplement-additional-date-bounds-20261008.jsonl)、[RRC字段](_sources/supplement-rrc-date-bounds-20261008.jsonl)与[EvoConfig字段](_sources/supplement-evoconfig-date-bounds-20261008.jsonl)；registered、Submitted或单独一般排期均不证明public。

新增23项准入、必要证据与Books逐项处置已获root独核。排除抽检重开EvoConfig的独立诊断/只读工具接口，Jan26日期已核、标准6仅报告；2601.17112的局部质量/结构反侧亦撤销粗关闭，但公开界限跨Jan26–27，已获root日期终态保留通过，不列确定候选。不会因外部日期保留/子命题不采用而删除已成立的受限贡献。最终分母为原37+新增23=60，root最后整体DAY实际验收通过。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs](https://arxiv.org/html/2601.16979v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 沿实际更新方向测criticalsharpness而非昂贵最大Hessian→需区分方向诊断与全曲率/配比最优；2 + 1 + 2 = 5 | 标准完成 | 仅报告：诊断量在作者checkpoint/data-mix局部成立，未证明改变预训练optimizer或普遍配比选择；不把诊断0.7当实测最优0.6。 |
| [Auto-Regressive Masked Diffusion Models](https://arxiv.org/html/2601.16971v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | maskedblock训练可能漏标签→query与KV共同strict排当前block、双流并行条件项→生成分解/并行近似须重新定义；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#block-diffusion局部自回归与块内并行)690–692，query构造/KV来源/mask联合排除本block标签，保留双流FLOPs、近似分布与逐token回退；root实际必要源→正文/邻接POST通过。 |
| [Strategies for Span Labeling with Large Language Models](https://arxiv.org/html/2601.16946v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | schema合法不绑定输入span→SELECT/COPY维护输入前缀与tokenization边界→约束状态不认证occurrence或语义标签；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-SGLANG [Ch51](../../../../books/part-05-inference-system/51-sglang.md#输出-span-还可以绑定输入序列)134–138，复制状态/输入身份与grammar合法性分责；root必要原源→正文/邻接POST通过。 |
| [DataStates-LLM : Scalable Checkpointing for Transformer Models Using Composable State Providers](https://arxiv.org/html/2601.16956v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | opaque状态序列化阻碍异构并行→state-provider隔离layout/serialization与byte movement→捕获epoch及hostpool背压成为接口条件；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-CHECKPOINT [Ch35](../../../../books/part-04-training-system/35-checkpoint.md#从统一-object-graph-到-composable-state-providers)已明确provider placement/byteview/offset、captureepoch、hostpool、restore及全局commit；无需重复实例。 |
| [Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias](https://arxiv.org/html/2601.16934v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 长文只测位置忽略语言混杂→同segmentset排列揭示language×position及校准反侧→公平不能由均匀attention直接推出；2 + 1 + 2 = 5 | 标准完成 | 仅报告：本次增量是language×position的两encoder诊断切片与basket校准反侧，而不是新的检索/排序机制；Ch66 EvalSpec已有population/slice/scorer分责，几何cosine变化不授检索公平修复，不另增校准配方。 |
| [GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints](https://arxiv.org/html/2601.16905v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | forgetaccuracy可由router绕开知识expert下降→retain几何约束/PTC与expertforcing反侧→遗忘必须拆开routing与内容；2 + 2 + 2 = 6 | 深入完成 | 仅报告：Ch21现有router选择与knowledge expert版本/撤销分责不能由forget输出直接签内容删除；本项固定X投影/PTC是受限更新recipe，实际采用的是该评价shortcut反侧而非无条件全分布保留定理。恢复指标冲突仍隔离，不把recipe扩为erase/safety知识链。 |
| [Provably Learning Attention with Queries](https://arxiv.org/html/2601.16873v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 参数恢复常混同文本API盗模→任意实向量精确scalaroracle可解单头合并参数→访问模型/可识别对象必须明确；2 + 1 + 3 = 6 | 标准完成 | 仅报告：新增可识别对象是单头合并参数、访问合同是任意实向量精确scalar oracle；本次保留这个理论context，不把它移植为tokenAPI/现实服务盗模机制，因而不改变部署威胁或访问控制判断。 |
| [Reasoning Promotes Robustness in Theory of Mind Tasks](https://arxiv.org/html/2601.16853v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | ToM平均分可掩盖prompt脆弱性→新扰动thinking版本更稳仍有共同失效→稳健性不同于新能力；2 + 1 + 2 = 5 | 标准完成 | 仅报告：改变的是ToM提示扰动下的服务行为观察，不是推理算法或训练目标；所采用反侧落在Ch66既有harness/prompt与能力声明分账，thinking开关/模型版本混杂不能产生新的RLVR因果知识。 |
| [Trapped in the past? Disentangling fluid and crystallized intelligence of large language models using chess](https://arxiv.org/html/2601.16823v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 推理预算收益可能依熟悉度→chessprior-density分层与legal-normalized评价→更多tokens并非同难度同收益；2 + 1 + 2 = 5 | 标准完成 | 仅报告：prior-density/合法着归一化只是棋局任务的分层诊断；数据库频率不是train membership，因此本次不改变memorization与generalization机制，保留预算×熟悉度的上下文观察而非新的能力定理。 |
| [Persuasion Tokens for Editing Factual Knowledge in LLMs](https://arxiv.org/html/2601.16781v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 长IKEdemonstrations占context→通用编辑分隔token加fact-locality训练→短提示必须与训练摊销/邻居退化合算；2 + 2 + 2 = 6 | 标准完成 | 仅报告：事实仍随每次请求prefix提供，只训练通用BEGIN/END_EDIT embedding而非每事实持久权重；Ch29已有部署soft-prompt/训练artifact分责，本文是缩短编辑演示的prompt适配recipe，邻居KL/摊销配置不新增事实真值或持久知识接口。 |
| [Select or Project? Evaluating Lower-dimensional Vectors for LLM Training Data Explanations](https://arxiv.org/html/2601.16651v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 保fullgradient几何未必最适解释检索→greedycomponent subset优于RP的retrievalproxy→影响解释需另验目标；2 + 1 + 2 = 5 | 标准完成 | 仅报告：greedy梯度分量选择是解释检索proxy的recipe，不是训练数据因果贡献估计；selection/test隔离未明使本次只采用proxy目标与几何保真不同的上下文反侧，不改变长期influence机制。 |
| [LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents](https://arxiv.org/html/2601.16649v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | endtask失败无法定位planning/state/history→可构造oracle干预→必须按充分state条件解释historypruning；2 + 1 + 2 = 5 | 标准完成 | 仅报告：state/planning/history oracle是三个确定性游戏的诊断fixture；充分state才可删历史，未新增可部署memory/planning更新接口。保留旧Ch79 observation/belief与规划分账，horizon/prompt改变的排行不作能力机制。 |
| [How Does Personalized Memory Shape LLM Behavior? Benchmarking Rational Preference Utilization in Personalized Assistants](https://arxiv.org/html/2601.16621v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | memoryrecall不等合理采用→Ignore/Support/Dominate及misuse反侧→偏好相关性与truth分账；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md#memory-read-是受约束检索)实际当前task适用性、频繁模式不是此刻意图及proposal不授tool权限；RPEval synthetic标签/likelihood排序是这一读取边界的诊断实例，不新增memory事实更新机制。 |
| [CORD: Bridging the Audio–Text Reasoning Gap via Weighted On-policy Cross-modal Distillation](https://arxiv.org/html/2601.16547v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | audio/text不同生成轨迹不能直接逐token对齐→同学生onpolicy prefix跨模态KL+position权重→蒸馏目标与音频utility并验；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md#distillation-不是teacher-越强越好)262–264，共同audio student prefix上的audio/text条件分布、监督/结果权限及双路/rollout成本，不能硬对齐独立轨迹或猜stop-gradient；root实际必要源→正文/邻接POST通过。 |
| [TangramPuzzle: Evaluating Multimodal Large Language Models with Compositional Spatial Reasoning](https://arxiv.org/html/2601.16520v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 视觉轮廓IoU可高但拼图非法→exactalgebraic约束分账→几何合法不能由图像相似验收；2 + 1 + 2 = 5 | 标准完成 | 仅报告：采用的是固定七pieces的exact面积/相交/覆盖约束与图像IoU不能互代的评价fixture，不新增空间生成或物理状态机制；Ch66 EvalSpec既有target/scorer权限分责，保留具体合法性反侧，不把2D verifier扩为3D物理链。 |
| [Finite-Time Analysis of Gradient Descent for Shallow Transformers](https://arxiv.org/html/2601.16514v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | length增加是否必然恶化训练界→受限shallowNTK给无显式T的经验MSE界→假设与内存代价须拆开；2 + 1 + 3 = 6 | 标准完成 | 仅报告：增量是固定query、transport/RKHS目标和投影GD假设内的经验MSE界；无显式T不取消输入存储/计算。只保留浅模型可训练性的理论context，不借无投影实验把条件界迁移成深LLM训练机制。 |
| [Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic](https://arxiv.org/html/2601.16486v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | tokens预算漏tooltime→wallclock含generation/toollatency改变model选择→实时任务不能只按生成速度选；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md#依赖并行与-critical-path)实际model/tool calls、orchestration latency、critical path与queue/resource constraints分账；人工tool latency与TimelyRL是这个选模合同的任务实例，不新增生产SLO保证。 |
| [Persona Jailbreaking in Large Language Models](https://arxiv.org/html/2601.16466v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | systempersona不变未必阻止history操纵→blackbox persona directional displacement→history安全需独立验；2 + 1 + 2 = 5 | 深入完成 | 仅报告：PHISH是操纵对话history的攻击fixture，STIR测量方向性trait displacement而非jailbreak成功率；本次不吸收问卷为临床人格或新防护机制，保留history可改变输出的受限安全反侧。 |
| [On the Expressive Power of Floating-Point Transformers](https://arxiv.org/html/2601.16450v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 理想attention排列等变被无条件移植实现→固定浮点归约破坏一般对称并有剩余对称/碰撞→位置语义需限定算术模型；3 + 1 + 3 = 7 | 深入完成 | 整合：MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md#为什么纯-self-attention-看不见顺序)22/31/33–35及Review notes：精确算术限定、finitefloat反侧和显式位置fallback；root实际正文及前后交接非作者POST通过，日级Gate通过。 |
| [Exploring the Effects of Alignment on Numerical Bias in Large Language Models](https://arxiv.org/html/2601.16444v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | judge分数更分散未必更准→base/instruct及calibration可降Pearson→分布偏置与评价有效性分账；2 + 1 + 2 = 5 | 标准完成 | 仅报告：四base/instruct对与gold校准提供judge分布形状和有效性分离的观察；kurtosis不是正确率，训练差异也不是alignment因果。新增的是评价context而非新的无偏judge更新算法，Pearson退化反侧保留。 |
| [White-Box Sensitivity Auditing with Steering Vectors](https://arxiv.org/html/2601.16398v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | I/O对照可能漏内部概念敏感性→steering与word替换不同干预并可随namecue接近→审计对象必须声明；2 + 1 + 2 = 5 | 标准完成 | 仅报告：steering与word替换改变不同干预对象；本次只采用审计对象须声明的对照背景，不把线性direction变成真实保护属性的因果操作或合规测量接口，强namecue让两者接近的反侧保留。 |
| [Cross-Lingual Activation Steering for Multilingual Language Models](https://arxiv.org/html/2601.16390v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | activation更近English未必质量更好→language-specific rescale可变远且gain/退化共存→geometry不是下游目标；2 + 1 + 2 = 5 | 标准完成 | 仅报告：language-specific rescale/negative blend是activation-steering recipe；本次采用的是geometry接近English与下游质量可分离的观察，不建立geometry因果目标。Ch66已明确language-forcing/relevance双轴，具体language调参不另增长期control接口。 |
| [NOIR : Privacy-Preserving Generation of Code with Open-Source LLMs](https://arxiv.org/html/2601.16354v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | split推理不自动私密/廉价→hiddenvocab与token扰动仍有crossprompt/adaptive攻击及client显存成本→威胁与隐私粒度必须限明；2 + 2 + 2 = 6 | 深入完成 | 仅报告：隐藏词表/扰动是特定split code服务的威胁模型context；token邻接证明不能提升sequence隐私，正文排adaptive与末段待测adaptive/crossprompt攻击张力保留。不能据此选定新隐私保障机制；本次仅保留分责/攻击范围，不新增sequence DP或安全部署结论。 |
| [VisGym : Diverse, Customizable, Scalable Environments for Multimodal Agents](https://arxiv.org/html/2601.16973v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | Agent历史/visualrender可能混淆能力评价→history窗口与ASCII/taskfeedback改变局部成功→匹配信息接口再解释能力；2 + 1 + 2 = 5 | 标准完成 | 仅报告：history窗口、ASCII与feedback改变可见接口，是Ch66现有harness/environment identity的benchmark实例；本次没有新增agent状态更新或跨模态算法，只保留匹配输入后再解释成绩的任务context。 |
| [ReViP: Reducing False Completion in Vision-Language-Action Models with Vision–Proprioception Rebalance](https://arxiv.org/html/2601.16667v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | VLA内部completion可与视觉失败冲突→externalobserver/taskprior调制动作→termination证据与selfstate分账；2 + 2 + 2 = 6 | 标准完成 | 仅报告：外部视觉observer给termination/task-stage信号的recipe仍以观测校验内部completion；本次只采用false-completion反侧，不把72B observer当新world/action真值接口，能力/成本混杂也未隔离vision-proprio因果。 |
| [OnlineSI: Taming Large Language Model for Online 3D Understanding and Grounding](https://arxiv.org/html/2601.16538v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | partialvisibility使完整GT precision/recall不可比→strict/lenient visibleGT FuzzyF1→online3D评价须声明可见性；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#视频评估先确认模态与时间信息是否必要)实际gold支持绑定可见输入、重建支持集和分别报告分母；ScanNet strict/lenient GT是该合同的具体指标实例，不把buffer当世界真值。 |
| [Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs](https://arxiv.org/html/2601.16527v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | hallucinationforget可被有限relearn反转→TargetedSAM局部扰动训练→erase与再学稳定性必须拆开；2 + 2 + 2 = 6 | 深入完成 | 仅报告：TargetedSAM是把成熟局部sharpness扰动作用于hallucination mapping的训练recipe；再学测试限定了该recipe的持久性，不新增完备erase语义。实际采用再学/保持目标分账与CHAIR/POPE反侧，双梯度成本保留。 |
| [Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory](https://arxiv.org/html/2601.16296v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 多轮video生成历史增加token成本→FOV检索/动态token合并/DRoPE身份→compressedcontext与全pipeline资源分账；2 + 2 + 2 = 6 | 标准完成 | 仅报告：Ch24 79–99已有自产history状态、有损分层压缩、局部位置重索引与原帧回退，59已有来源坐标映射分责；本项FOV排名、10/20层merge与DRoPE有界role位置是该生成条件接口的实现配置，未新增action-conditioned worldstate；保留检索/缓存增长和质量反侧，不把token预算当总成本。 |
| [W4A16 Mixed-Precision Matrix Multiplication on Decoupled Architecture: Kernel Design and Memory Bottleneck Analysis for Ascend NPUs](https://arxiv.org/html/2601.16536v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | GPU反量化经验不直接适Ascend→vector/cube解耦GMroundtrip促SplitK→核瓶颈取决硬件路径/shape；2 + 1 + 2 = 5 | 标准完成 | 仅报告：Ch49 29/86–88已有中间量HBM往返与dequant前置瓶颈/硬件融合分责；Vector→GM→Cube SplitK→GM reduce是Ascend910对这个执行合同的shape配置实例，不另建kernel知识链，4x存储不等4x执行。 |
| [Space Filling Curves is All You Need: Communication-Avoiding Matrix Multiplication Made Simple](https://arxiv.org/html/2601.16294v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | CPU GEMM固定tiling有cacheglassjaw→SFC workownership加K副本reduce→communication界依缓存/复制预算；2 + 1 + 2 = 5 | 标准完成 | 仅报告：SFC ownership/复制K分块是共享CPU cache与2.5D GEMM的communication-avoiding recipe；FastMem假设与c/Kblock选择是其模型context，不改变分布式collective或GPU执行机制，不能把CPU缓存界当跨设备最优。 |
| [Mixture-of-Models: Unifying Heterogeneous Agents via N-Way Self-Evaluating Deliberation](https://arxiv.org/html/2601.16863v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 多agentvote可能放大危险而非减→fixedheterogeneous团队Sneaking反侧→共识与安全分账；2 + 1 + 2 = 5 | 深入完成 | 仅报告：AGENT-MULTI-AGENT Ch82 156–160已有plurality/modal bias与共识非真值；本项异构fixed-team vote的Sneaking退步是该边界的具体安全切片。broker knapsack只提出未验证设计，不作为新runtime机制整合。 |
| [Revisiting the Role of Natural Language Code Comments in Code Translation](https://arxiv.org/html/2601.16661v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | comment看似额外帮助→同代码成功/失败集合不嵌套及具体内存错误→translation须保pairedsemantic验收；2 + 1 + 2 = 5 | 标准完成 | 仅报告：同code有/无comments的成功集合不嵌套，是程序翻译paired fixture反侧，不新增compiler/模型更新机制；COMMENTRA是在既有test oracle后的条件重试recipe，不能由文本意图标签给代码语义认证。 |
| [AuroraEdge-V-2B: A Faster And Stronger Edge Visual Large Language Model](https://arxiv.org/html/2601.16615v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 只数LM视觉token漏压缩旁路→未压缩视觉参与crossfusion→tokenbudget须按整路径计；2 + 2 + 2 = 6 | 标准完成 | 仅报告：64 LM token之外仍有256视觉token参与crossfusion，是该VLM结构的执行账实例；新增的是压缩后仍支付旁路成本的配置事实，不是新token-budget或edge调度合同，36→40ms反侧保留。 |
| [SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment](https://arxiv.org/html/2601.16506v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | 风险router可节省解码却自带误判→gateway/SATE/DDGT局部安全反侧→路由安全与全expert资源取舍；2 + 2 + 2 = 6 | 深入完成 | 仅报告：gateway高/低/不确定风险选择refuse/SATE/DDGT是受限安全router recipe；本次采用误路由/完整expert资源反侧而非新安全授权接口。两步共享topk不提供后续全程保证，fullrouteprefill反退与fallback界保留。 |
| [Graph-Anchored Knowledge Indexing for Retrieval-Augmented Generation](https://arxiv.org/html/2601.16462v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | graph压缩便于迭代检索可能丢答案信息→graphonly退化需rawfallback→索引增长不等answer收益；2 + 1 + 2 = 5 | 标准完成 | 仅报告：graph-index迭代检索是已有RAG证据选择/原文回退的实现recipe；graphonly丢答案信息是此压缩配置的反侧，不新增事实owner或支持真值。抽图/调用成本未全披露，exact-v1不借v2扩机制。 |
| [Towards a Theoretical Understanding to the Generalization of RLHF](https://arxiv.org/html/2601.16403v1) | 2026-01-26T09:00:00+08:00 ～ 2026-01-26T10:43:00+08:00 | empiricalRLHF优化好不自动population好→featurecoverage/conditioning控制stationary与bestiterate界→部署解释必须暴露coverage假设；2 + 1 + 3 = 6 | 标准完成 | 仅报告：coverage/conditioning给knownreward、linearfeatures与Boltzmannreference的population/优化界；新增的是这些假设下的理论context，不是learnedRM训练或lastiterate部署算法，stationary/bestiterate不得互代。 |
| [Kimi CLI0.88](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.88) | 2026-01-26T21:10:05+08:00 | 应用session误注入protocolheader→PR681去runtime.session.id默认注入→传输会话身份不能混同应用会话；2 + 1 + 2 = 5 | 深入完成 | 仅报告：受限实现兼容case，Ch83已承载version/sessionhandle/backend身份分离；非规范新机制或所有server保证 |
| [SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer](https://arxiv.org/html/2601.16515v1) | 2026-01-26 | 稀疏率不等加速→并行linear分支与gate补质量→检验端到端质量/费用；2 + 2 + 2 = 6 | 标准完成 | 仅报告：hybrid attention的受限视频验证，未建立通用替代条件。 |
| [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/html/2601.16746v1) | 2026-01-26 | 固定PPL裁剪破坏代码→goal-conditioned完整行选择→需保留hint缺失回退；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md#从-generic-compression-到-goal-conditioned-structured-pruning)374–389目标/完整行、hint身份与bypass/raw回退，root实际核通过。 |
| [A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics](https://arxiv.org/html/2601.16531v1) | 2026-01-26 | hash碰撞可干扰→静态无冲突hot-tier受限对照→查找正确性不等学习收益；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-EMBEDDING [Ch12](../../../../books/part-02-model/12-embedding.md#从-token-row-到-hashed-n-gram-capacity)294–296及自身末注，root实际POST通过。 |
| [TL-GRPO: Turn-Level RL for Reasoning-Guided Iterative Optimization](https://arxiv.org/html/2601.16480v1) | 2026-01-26 | best-turn效用非累计return→同history内动作组比较→需显式目标/人口与探索代价；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md#hierarchy-of-groups-必须成为-trajectory-identity)1553–1555 best-turn utility与同history动作credit，两段已写，root实际必要source/PRE及窄修后POST通过。 |
| [Jacobian Scopes: token-level causal attributions in LLMs](https://arxiv.org/html/2601.16407v1) | 2026-01-26 | attention权重不识别输入影响→局部J投影与Fisher分账→区分logit/范数/分布诊断；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部微扰诊断不建立可发布的全局因果解释。 |
| [Endless Terminals: Scaling RL Environments for Terminal Agents](https://arxiv.org/html/2601.16443v1) | 2026-01-26 | 合成任务可能无效→执行验证与solution-filter→需保留测试/教师能力cap；2 + 2 + 2 = 6 | 标准完成 | 仅报告：可执行任务生成的受限验证实例，未改变通用环境 authority。 |
| [DSGym: A Holistic Framework for Evaluating and Training Data Science Agents](https://arxiv.org/html/2601.16344v1) | 2026-01-26 | 持有文件不证明依赖数据→data-withholding反控与过滤→评价需区分残余shortcut/curated人口；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)153–155 data-withheld负控制及过滤人口，两段已写，root实际必要source/PRE及人工先行顺序纠正后POST通过。 |
| [Clarify or Answer: Reinforcement Learning for Agentic VQA with Context Under-specification](https://arxiv.org/html/2601.16400v1) | 2026-01-26 | 缺上下文不应强答→Answer/Clarify controller与问题策略分离→奖励变化不等真值；2 + 2 + 2 = 6 | 标准完成 | 仅报告：单次询问的受限视觉实验，未定义可验证通用澄清阈值。 |
| [Calibrated Similarity for Reliable Geometric Analysis of Embedding Spaces](https://arxiv.org/html/2601.16907v1) | 2026-01-26 | embedding重编码改索引→posthoc isotonic校分→需保留ties与条件概率方向；2 + 1 + 2 = 5 | 标准完成 | 仅报告：已有cosine的受限校准替代，中心完全不变性不采用。 |
| [Process-Tensor Tomography of SGD: Measuring Non-Markovian Memory via Back-Flow of Distinguishability](https://arxiv.org/html/2601.16563v1) | 2026-01-26 | 仅probe输出可能非闭合→两步可区分性witness与buffer干预→观测非Markov不等完整训练state非Markov；2 + 1 + 3 = 6 | 标准完成 | 仅报告：新测量反侧不改变已含optimizer/data状态的恢复接口。 |
| [EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents](https://arxiv.org/html/2601.16690v1) | 2026-01-26 | 固定QA可能不对齐交互→自身轨迹+环境真值模板→比较题目人口及modality反侧；2 + 2 + 2 = 6 | 标准完成 | 仅报告：环境QA生成的有限实例，不能由不同轨迹分数授相同难度。 |
| [From Atom to Community: Structured and Evolving Agent Memory for User Behavior Modeling](https://arxiv.org/html/2601.16872v1) | 2026-01-26 | 单summary覆盖偏好→atomic行为链接/社区prototype传播→需区分derived偏好与推理时维护；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md#memory-粒度必须分层不能用一个-summary-同时承担证据与画像)409–411社区derived prototype与维护周期，root实际POST通过。 |
| [AnyView: Synthesizing Any Novel View in Dynamic Scenes](https://arxiv.org/html/2601.16982v1) | 2026-01-26 | 显式depthwarp依赖view overlap→RGB/Plücker条件implicit生成→极端view仍需受限验证；2 + 1 + 2 = 5 | 标准完成 | 仅报告：动态view新验证条件不证明任意pose或物理世界状态。 |
| [SyncLight: Controllable and Consistent Multi-View Relighting](https://arxiv.org/html/2601.16981v1) | 2026-01-26 | 单view relight可能跨view不一致→pair-trained bridge与jointattention→有限N扩展需条件化；2 + 1 + 2 = 5 | 标准完成 | 仅报告：pair到有限多view的受限照明控制，无任意N/生产内存保证。 |
| [Fast, faithful and photorealistic diffusion-based image super-resolution with enhanced Flow Map models](https://arxiv.org/html/2601.16660v1) | 2026-01-26 | few-step SR质量目标不同→avgflow训练CFG/LoRA→保真-感知-计算取舍分账；2 + 1 + 2 = 5 | 标准完成 | 仅报告：SR条件下CFG/FlowMap新实现分支，不构成通用生成替代结论。 |
| [Cognitively-Inspired Tokens Overcome Egocentric Bias in Multimodal Models](https://arxiv.org/html/2601.16378v1) | 2026-01-26 | 视觉朝向可遗漏→pose/rotation显式token→同信息text与坐标条件仍需比较；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受限朝向表示替代，不授allocentric circuit或全域优越。 |
| [Where is the multimodal goal post? On the Ability of Foundation Models to Recognize Contextually Important Moments](https://arxiv.org/html/2601.16333v1) | 2026-01-26 | 多模态总分掩盖任务需求→ALV子集与dominant modality反侧→不把融合总改善当先验；2 + 1 + 2 = 5 | 标准完成 | 仅报告：任务异质性的有限验证，未给可部署通用modal selector。 |
| [Will It Survive? Deciphering the Fate of AI-Generated Code in Open Source](https://arxiv.org/html/2601.16809v1) | 2026-01-26 | 短期merge不能答disposable叙事→纵向modification survival→仅观察反侧不授quality因果；2 + 2 + 2 = 6 | 深入完成 | 仅报告：维护期观察反侧，非代码质量/工具因果或release规则；root独核通过。 |
| [ResAgent: Entropy-based Prior Point Discovery and Visual Reasoning for Referring Expression Segmentation](https://arxiv.org/html/2601.16394v1) | 2026-01-26 | 文本坐标不认证point正确→标记图像视觉yes/no验证→point数量并非单调收益；2 + 1 + 2 = 5 | 标准完成 | 仅报告：RES图像标记验证的受限界面反侧，LoRA/SAM适配不归因纯interface，root必要源准入通过。 |
| [Learning Domain Knowledge in Multimodal Large Language Models through Reinforcement Fine-Tuning](https://arxiv.org/html/2601.16419v1) | 2026-01-26 | 文字prior不一定执行→原/变换image分布一致性reward→弱监督有效条件需任务symmetry；2 + 1 + 2 = 5 | 标准完成 | 仅报告：任务symmetry下distribution-consistency的受限选择，不采用科学领域路线/普遍prior必须objective，root必要源范围核通过。 |
| [Retrieve-Refine-Calibrate: A Framework for Complex Claim Fact-Checking](https://arxiv.org/pdf/2601.16555v1) | 2026-01-26 | 拆分可能放大无关证据→entity-first检索与claim-refinement/低conf重评→保留多跳受限替代路径；2 + 1 + 2 = 5 | 标准完成 | 仅报告：完整框架局部有效，不授decomposition唯一噪声因果或通用fact-check规则。 |
| [SemanticALLI: Caching Reasoning, Not Just Responses, in Agentic Systems](https://arxiv.org/html/2601.16286v1) | 2026-01-26 | boundary cache漏内部复用→AIR与VS独立IR key/lexical保护→需分阶段命中分母与quality未验；2 + 1 + 2 = 5 | 标准完成 | 仅报告：内部IR复用的受限验证，未验analytic accuracy、全生命周期或普遍质量保持。 |
| [EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration](https://arxiv.org/html/2601.16489v1) | 2026-01-26 | 配置执行trace撑大主context→独立诊断stdout/exitcode、只读单行工具→证据收集与维修执行分责；2 + 2 + 2 = 6 | 标准完成 | 仅报告：受限诊断分工验证，self-evolve规则未披露/pytest执行非tests通过，不授生产环境正确性。 |

## 4. 证据与知识整合

[实际必要证据笔记](_sources/evidence.md)保留方法位置、配置、直接反侧及不采用项；本节逐项列采用命题与处置。全部采用精确v1，不拿API后来v2/v3摘要替代本事件。标准项已读核心方法/评价/关键限制；安全变化与明确纠错项按受影响命题深入，不遍全部附件。

### [A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs](https://arxiv.org/html/2601.16979v1)

沿实际更新方向测criticalsharpness而非昂贵最大Hessian→需区分方向诊断与全曲率/配比最优。诊断量在作者checkpoint/data-mix局部成立，未证明改变预训练optimizer或普遍配比选择；不把诊断0.7当实测最优0.6。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16979.json)。

### [Auto-Regressive Masked Diffusion Models](https://arxiv.org/html/2601.16971v1)

maskedblock训练可能漏标签→query与KV共同strict排当前block、双流并行条件项→生成分解/并行近似须重新定义。具体差额已写入MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#block-diffusion局部自回归与块内并行)690–692：query与KV信息流共同排本块标签，而不只严格mask；双流FLOPs、近似条件分解及普通AR回退就近保留，root非作者POST通过。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16971.json)。

### [DataStates-LLM : Scalable Checkpointing for Transformer Models Using Composable State Providers](https://arxiv.org/html/2601.16956v1)

opaque状态序列化阻碍异构并行→state-provider隔离layout/serialization与byte movement→捕获epoch及hostpool背压成为接口条件。TRAIN-CHECKPOINT [Ch35](../../../../books/part-04-training-system/35-checkpoint.md#从统一-object-graph-到-composable-state-providers)已明确provider placement/byteview/offset、captureepoch、hostpool、restore及全局commit；无需重复实例。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16956.json)。

### [Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias](https://arxiv.org/html/2601.16934v1)

长文只测位置忽略语言混杂→同segmentset排列揭示language×position及校准反侧→公平不能由均匀attention直接推出。本次增量是language×position的两encoder诊断切片与basket校准反侧，而不是新的检索/排序机制；Ch66 EvalSpec已有population/slice/scorer分责，几何cosine变化不授检索公平修复，不另增校准配方。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16934.json)。

### [GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints](https://arxiv.org/html/2601.16905v1)

forgetaccuracy可由router绕开知识expert下降→retain几何约束/PTC与expertforcing反侧→遗忘必须拆开routing与内容。Ch21现有router选择与knowledge expert版本/撤销分责不能由forget输出直接签内容删除；本项固定X投影/PTC是受限更新recipe，实际采用的是该评价shortcut反侧而非无条件全分布保留定理。恢复指标冲突仍隔离，不把recipe扩为erase/safety知识链。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16905.json)。

### [Provably Learning Attention with Queries](https://arxiv.org/html/2601.16873v1)

参数恢复常混同文本API盗模→任意实向量精确scalaroracle可解单头合并参数→访问模型/可识别对象必须明确。新增可识别对象是单头合并参数、访问合同是任意实向量精确scalar oracle；本次保留这个理论context，不把它移植为tokenAPI/现实服务盗模机制，因而不改变部署威胁或访问控制判断。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16873.json)。

### [Reasoning Promotes Robustness in Theory of Mind Tasks](https://arxiv.org/html/2601.16853v1)

ToM平均分可掩盖prompt脆弱性→新扰动thinking版本更稳仍有共同失效→稳健性不同于新能力。改变的是ToM提示扰动下的服务行为观察，不是推理算法或训练目标；所采用反侧落在Ch66既有harness/prompt与能力声明分账，thinking开关/模型版本混杂不能产生新的RLVR因果知识。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16853.json)。

### [Trapped in the past? Disentangling fluid and crystallized intelligence of large language models using chess](https://arxiv.org/html/2601.16823v1)

推理预算收益可能依熟悉度→chessprior-density分层与legal-normalized评价→更多tokens并非同难度同收益。prior-density/合法着归一化只是棋局任务的分层诊断；数据库频率不是train membership，因此本次不改变memorization与generalization机制，保留预算×熟悉度的上下文观察而非新的能力定理。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16823.json)。

### [Persuasion Tokens for Editing Factual Knowledge in LLMs](https://arxiv.org/html/2601.16781v1)

长IKEdemonstrations占context→通用编辑分隔token加fact-locality训练→短提示必须与训练摊销/邻居退化合算。事实仍随每次请求prefix提供，只训练通用BEGIN/END_EDIT embedding而非每事实持久权重；Ch29已有部署soft-prompt/训练artifact分责，本文是缩短编辑演示的prompt适配recipe，邻居KL/摊销配置不新增事实真值或持久知识接口。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16781.json)。

### [Select or Project? Evaluating Lower-dimensional Vectors for LLM Training Data Explanations](https://arxiv.org/html/2601.16651v1)

保fullgradient几何未必最适解释检索→greedycomponent subset优于RP的retrievalproxy→影响解释需另验目标。greedy梯度分量选择是解释检索proxy的recipe，不是训练数据因果贡献估计；selection/test隔离未明使本次只采用proxy目标与几何保真不同的上下文反侧，不改变长期influence机制。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16651.json)。

### [LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents](https://arxiv.org/html/2601.16649v1)

endtask失败无法定位planning/state/history→可构造oracle干预→必须按充分state条件解释historypruning。state/planning/history oracle是三个确定性游戏的诊断fixture；充分state才可删历史，未新增可部署memory/planning更新接口。保留旧Ch79 observation/belief与规划分账，horizon/prompt改变的排行不作能力机制。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16649.json)。

### [How Does Personalized Memory Shape LLM Behavior? Benchmarking Rational Preference Utilization in Personalized Assistants](https://arxiv.org/html/2601.16621v1)

memoryrecall不等合理采用→Ignore/Support/Dominate及misuse反侧→偏好相关性与truth分账。AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md#memory-read-是受约束检索)实际当前task适用性、频繁模式不是此刻意图及proposal不授tool权限；RPEval synthetic标签/likelihood排序是这一读取边界的诊断实例，不新增memory事实更新机制。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16621.json)。

### [CORD: Bridging the Audio–Text Reasoning Gap via Weighted On-policy Cross-modal Distillation](https://arxiv.org/html/2601.16547v1)

audio/text不同生成轨迹不能直接逐token对齐→同学生onpolicy prefix跨模态KL+position权重→蒸馏目标与音频utility并验。TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md#distillation-不是teacher-越强越好)262–264已补同audio rollout prefix比较audio/text条件输出的接口；不是两条独立轨迹逐token对齐，text分支提供监督而非事实真值，KL权重/sequencejudge与最终utility分账。双路forward/rollout、stop-gradient未披露及配对SFT/原checkpoint回退就近；root非作者实际必要源与POST通过。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16547.json)。

### [TangramPuzzle: Evaluating Multimodal Large Language Models with Compositional Spatial Reasoning](https://arxiv.org/html/2601.16520v1)

视觉轮廓IoU可高但拼图非法→exactalgebraic约束分账→几何合法不能由图像相似验收。采用的是固定七pieces的exact面积/相交/覆盖约束与图像IoU不能互代的评价fixture，不新增空间生成或物理状态机制；Ch66 EvalSpec既有target/scorer权限分责，保留具体合法性反侧，不把2D verifier扩为3D物理链。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16520.json)。

### [Finite-Time Analysis of Gradient Descent for Shallow Transformers](https://arxiv.org/html/2601.16514v1)

length增加是否必然恶化训练界→受限shallowNTK给无显式T的经验MSE界→假设与内存代价须拆开。增量是固定query、transport/RKHS目标和投影GD假设内的经验MSE界；无显式T不取消输入存储/计算。只保留浅模型可训练性的理论context，不借无投影实验把条件界迁移成深LLM训练机制。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16514.json)。

### [Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic](https://arxiv.org/html/2601.16486v1)

tokens预算漏tooltime→wallclock含generation/toollatency改变model选择→实时任务不能只按生成速度选。AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md#依赖并行与-critical-path)已分model/tool calls、orchestration latency、critical path与queue/resource约束；这是wallclock选模合同的任务实例，TimelyRL与人工时延不授生产SLO。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16486.json)。

### [Persona Jailbreaking in Large Language Models](https://arxiv.org/html/2601.16466v1)

systempersona不变未必阻止history操纵→blackbox persona directional displacement→history安全需独立验。PHISH是操纵对话history的攻击fixture，STIR测量方向性trait displacement而非jailbreak成功率；本次不吸收问卷为临床人格或新防护机制，保留history可改变输出的受限安全反侧。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16466.json)。

### [On the Expressive Power of Floating-Point Transformers](https://arxiv.org/html/2601.16450v1)

理想attention排列等变被无条件移植实现→固定浮点归约破坏一般对称并有剩余对称/碰撞→位置语义需限定算术模型。MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md#为什么纯-self-attention-看不见顺序)22/31/33–35及Review notes：精确算术限定、finitefloat反侧和显式位置fallback；root实际正文及前后交接非作者POST通过，日级Gate待验。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16450.json)。实际书稿不新增章/附录，保留原位置方案和舍入不能替代编码的fallback。

### [Exploring the Effects of Alignment on Numerical Bias in Large Language Models](https://arxiv.org/html/2601.16444v1)

judge分数更分散未必更准→base/instruct及calibration可降Pearson→分布偏置与评价有效性分账。四base/instruct对与gold校准提供judge分布形状和有效性分离的观察；kurtosis不是正确率，训练差异也不是alignment因果。新增的是评价context而非新的无偏judge更新算法，Pearson退化反侧保留。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16444.json)。

### [White-Box Sensitivity Auditing with Steering Vectors](https://arxiv.org/html/2601.16398v1)

I/O对照可能漏内部概念敏感性→steering与word替换不同干预并可随namecue接近→审计对象必须声明。steering与word替换改变不同干预对象；本次只采用审计对象须声明的对照背景，不把线性direction变成真实保护属性的因果操作或合规测量接口，强namecue让两者接近的反侧保留。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16398.json)。

### [Cross-Lingual Activation Steering for Multilingual Language Models](https://arxiv.org/html/2601.16390v1)

activation更近English未必质量更好→language-specific rescale可变远且gain/退化共存→geometry不是下游目标。language-specific rescale/negative blend是activation-steering recipe；本次采用的是geometry接近English与下游质量可分离的观察，不建立geometry因果目标。Ch66已明确language-forcing/relevance双轴，具体language调参不另增长期control接口。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16390.json)。

### [NOIR : Privacy-Preserving Generation of Code with Open-Source LLMs](https://arxiv.org/html/2601.16354v1)

split推理不自动私密/廉价→hiddenvocab与token扰动仍有crossprompt/adaptive攻击及client显存成本→威胁与隐私粒度必须限明。隐藏词表/扰动是特定split code服务的威胁模型context；token邻接证明不能提升sequence隐私，正文排adaptive与末段待测adaptive/crossprompt攻击张力保留。不能据此选定新隐私保障机制；本次仅保留分责/攻击范围，不新增sequence DP或安全部署结论。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16354.json)。

### [VisGym : Diverse, Customizable, Scalable Environments for Multimodal Agents](https://arxiv.org/html/2601.16973v1)

Agent历史/visualrender可能混淆能力评价→history窗口与ASCII/taskfeedback改变局部成功→匹配信息接口再解释能力。history窗口、ASCII与feedback改变可见接口，是Ch66现有harness/environment identity的benchmark实例；本次没有新增agent状态更新或跨模态算法，只保留匹配输入后再解释成绩的任务context。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16973.json)。

### [ReViP: Reducing False Completion in Vision-Language-Action Models with Vision–Proprioception Rebalance](https://arxiv.org/html/2601.16667v1)

VLA内部completion可与视觉失败冲突→externalobserver/taskprior调制动作→termination证据与selfstate分账。外部视觉observer给termination/task-stage信号的recipe仍以观测校验内部completion；本次只采用false-completion反侧，不把72B observer当新world/action真值接口，能力/成本混杂也未隔离vision-proprio因果。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16667.json)。

### [OnlineSI: Taming Large Language Model for Online 3D Understanding and Grounding](https://arxiv.org/html/2601.16538v1)

partialvisibility使完整GT precision/recall不可比→strict/lenient visibleGT FuzzyF1→online3D评价须声明可见性。PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#视频评估先确认模态与时间信息是否必要)已承载gold支持绑定可见输入/重建支持slice及分别报告分母；strict/lenient GT是此合同的指标实例，buffer不改worldstate真值。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16538.json)。

### [Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs](https://arxiv.org/html/2601.16527v1)

hallucinationforget可被有限relearn反转→TargetedSAM局部扰动训练→erase与再学稳定性必须拆开。TargetedSAM是把成熟局部sharpness扰动作用于hallucination mapping的训练recipe；再学测试限定了该recipe的持久性，不新增完备erase语义。实际采用再学/保持目标分账与CHAIR/POPE反侧，双梯度成本保留。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16527.json)。

### [Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory](https://arxiv.org/html/2601.16296v1)

多轮video生成历史增加token成本→FOV检索/动态token合并/DRoPE身份→compressedcontext与全pipeline资源分账。Ch24 79–99已有自产history状态、有损分层压缩、局部位置重索引与原帧回退，59已有来源坐标映射分责；本项FOV排名、10/20层merge与DRoPE有界role位置是该生成条件接口的实现配置，未新增action-conditioned worldstate；保留检索/缓存增长和质量反侧，不把token预算当总成本。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16296.json)。

### [W4A16 Mixed-Precision Matrix Multiplication on Decoupled Architecture: Kernel Design and Memory Bottleneck Analysis for Ascend NPUs](https://arxiv.org/html/2601.16536v1)

GPU反量化经验不直接适Ascend→vector/cube解耦GMroundtrip促SplitK→核瓶颈取决硬件路径/shape。Ch49 29/86–88已有中间量HBM往返与dequant前置瓶颈/硬件融合分责；Vector→GM→Cube SplitK→GM reduce是Ascend910对这个执行合同的shape配置实例，不另建kernel知识链，4x存储不等4x执行。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16536.json)。

### [Space Filling Curves is All You Need: Communication-Avoiding Matrix Multiplication Made Simple](https://arxiv.org/html/2601.16294v1)

CPU GEMM固定tiling有cacheglassjaw→SFC workownership加K副本reduce→communication界依缓存/复制预算。SFC ownership/复制K分块是共享CPU cache与2.5D GEMM的communication-avoiding recipe；FastMem假设与c/Kblock选择是其模型context，不改变分布式collective或GPU执行机制，不能把CPU缓存界当跨设备最优。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16294.json)。

### [Mixture-of-Models: Unifying Heterogeneous Agents via N-Way Self-Evaluating Deliberation](https://arxiv.org/html/2601.16863v1)

多agentvote可能放大危险而非减→fixedheterogeneous团队Sneaking反侧→共识与安全分账。AGENT-MULTI-AGENT Ch82 156–160已有plurality/modal bias与共识非真值；本项异构fixed-team vote的Sneaking退步是该边界的具体安全切片。broker knapsack只提出未验证设计，不作为新runtime机制整合。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16863.json)。

### [Revisiting the Role of Natural Language Code Comments in Code Translation](https://arxiv.org/html/2601.16661v1)

comment看似额外帮助→同代码成功/失败集合不嵌套及具体内存错误→translation须保pairedsemantic验收。同code有/无comments的成功集合不嵌套，是程序翻译paired fixture反侧，不新增compiler/模型更新机制；COMMENTRA是在既有test oracle后的条件重试recipe，不能由文本意图标签给代码语义认证。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16661.json)。

### [AuroraEdge-V-2B: A Faster And Stronger Edge Visual Large Language Model](https://arxiv.org/html/2601.16615v1)

只数LM视觉token漏压缩旁路→未压缩视觉参与crossfusion→tokenbudget须按整路径计。64 LM token之外仍有256视觉token参与crossfusion，是该VLM结构的执行账实例；新增的是压缩后仍支付旁路成本的配置事实，不是新token-budget或edge调度合同，36→40ms反侧保留。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16615.json)。

### [SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment](https://arxiv.org/html/2601.16506v1)

风险router可节省解码却自带误判→gateway/SATE/DDGT局部安全反侧→路由安全与全expert资源取舍。gateway高/低/不确定风险选择refuse/SATE/DDGT是受限安全router recipe；本次采用误路由/完整expert资源反侧而非新安全授权接口。两步共享topk不提供后续全程保证，fullrouteprefill反退与fallback界保留。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16506.json)。

### [Graph-Anchored Knowledge Indexing for Retrieval-Augmented Generation](https://arxiv.org/html/2601.16462v1)

graph压缩便于迭代检索可能丢答案信息→graphonly退化需rawfallback→索引增长不等answer收益。graph-index迭代检索是已有RAG证据选择/原文回退的实现recipe；graphonly丢答案信息是此压缩配置的反侧，不新增事实owner或支持真值。抽图/调用成本未全披露，exact-v1不借v2扩机制。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16462.json)。

### [Towards a Theoretical Understanding to the Generalization of RLHF](https://arxiv.org/html/2601.16403v1)

empiricalRLHF优化好不自动population好→featurecoverage/conditioning控制stationary与bestiterate界→部署解释必须暴露coverage假设。coverage/conditioning给knownreward、linearfeatures与Boltzmannreference的population/优化界；新增的是这些假设下的理论context，不是learnedRM训练或lastiterate部署算法，stationary/bestiterate不得互代。 精确v1必要原文与实际段位、主要代价/对照限制、直接反侧见[证据笔记](_sources/evidence.md)及[v1提取](_sources/v1-16403.json)。

### [Kimi CLI0.88](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.88)

published_at=2026-01-26T13:10:05Z，created_at=13:01:13Z不替代release发布时间。[PR681](https://github.com/MoonshotAI/kimi-cli/pull/681)在35fa76b6…toolset.py移除非OAuth远端且header缺位时注入runtime.session.id的9行；不删除用户配置header，也不证明FastMCP不支持server会话。[官方2025-06-18规范](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)只允许server初始化可选分配Mcp-Session-Id，返回后client须回传、404后重新初始化。稳定原则是应用session≠协议session；[AGENT-MCP Ch83](../../../../books/part-07-agent/83-mcp.md#lifecycle-与-version-contract)现有lifecycle/version/sessionhandle和backend执行责任段已承载身份分离，缺一个0.88例子不是长期gap。仅报告静态受限case，未运行e2e、未声称普遍必须生成session。原字段/patch见[kimi-release.json](_sources/kimi-release.json)、[kimi-patch.json](_sources/kimi-patch.json)。

### [Strategies for Span Labeling with Large Language Models](https://arxiv.org/html/2601.16946v1)

连续输入substring约束与schema合法性不同。INFER-SGLANG [Ch51](../../../../books/part-05-inference-system/51-sglang.md#输出-span-还可以绑定输入序列)134–138已补输入序列/候选位置/复制状态和多tokenization、quote边界；不解决重复occurrence及类别语义，不因合法span授质量保证，保留tagging/显式位置/parser回退。原关闭遗漏具体机制，分数2+1+2=5不变，owner gap定点深入；root必要原源及写后POST通过。必要证据位置与反侧见[定点重开笔记](_sources/review-16946.md)，单项首公开字段见[identity](_sources/identity-16946.json)，不是后来v2替代。

以下为本轮增量必要证据，原本节以上连续正文保持。

### [SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer](https://arxiv.org/html/2601.16515v1)

v1 §3–5/Table1/消融（blocks27–96、114–128）共享QKV，稀疏分支与ReLU linear分支经零初始化投影和input gate合成，LoRA调Q/K/V/O。Wan2.1-1.3B、480p/77frames、2000 Mixkit视频/1600steps/batch8条件下，Table1 Spatial90%给1.72×而TopK90%仅1.04×；sparsity本身不是执行成本。单卡batch1硬件/precision为Not Disclosed，20.6GPUh是finetuning成本，不是线上费用。Gate-detach消融可比，不能把效果只归动态gate；§5.2 prose与Table1数值、A.3排序措辞冲突不采用。保留受限质量/执行取舍，不授无损或最优balance；未建立当前Attention owner新增通用成立条件，仅报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16515v1-20261008.json)。

### [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/html/2601.16746v1)

v1 §3–5/limitations（blocks22–75、81–84）：Agent生成optional context_focus_question；无hint绕过保留完整源码。0.6B skimmer聚合行分数/阈值，CRF NLL+rerank MSE，61,184合成teacher标签不是执行验证。Mini-SWE-Agent/Sonnet4.5的500 SWEVerified任务success70.6%→70.2%、tokens.911M→.701M；Long Code Completion EM40.5→31.0并非SWE-QA，Table3随机裁剪比较仅50子集不能混500全量。硬件/precision/并发为Not Disclosed，API任务不适用本地GPU吞吐。Ch75当前374–389已实际承载goal/完整line、derived hint/version、缺hint bypass/raw回退及success退步边界，root原源与实际owner核通过，具体已有覆盖，无diff。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16746v1-20261008.json)。

### [A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics](https://arxiv.org/html/2601.16531v1)

v1 §3–5/Table3/limits（blocks25–134、160–165）：MPHF为100K固定hot成员独占槽，fingerprint核membership，非成员走400K cold hash；原baseline500K hash。GPT-2 125M backbone、总313,567,232参数、FineWeb-Edu100M-token数据集、约82M训练token/5000steps、A10040GB、batch4/accum4/AdamW、2seeds。loss4.4809±.0082与4.4799±.0123相近，1910→1693tokens/s付11–12%代价；等参数仍同时重分冷热容量，不能单碰撞因果。hot/cold gate和训练轨迹仅关联，不证有益regularizer/因果固化。实际Ch12原论证只有碰撞干扰/联合容量预算，新增两段区分成员无冲突、fingerprint非成员误判与质量/运行分账，保留后续4月data-aware分支；root必要源/PRE/实际正文、完整邻接和末注POST通过，数据集/训练token配置按复核纠正，未复现实验。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16531v1-20261008.json)。

### [TL-GRPO: Turn-Level RL for Reasoning-Guided Iterative Optimization](https://arxiv.org/html/2601.16480v1)

v1 §3–7（blocks24–82、99–122）：单state、各轮同口径确定性quality reward下，目标为预算内最大turn reward；先采一条backbone history，再每history采G动作并按该turn mean/std赋advantage，不是拿不同history同轮号当同分布。ACS仅验证此受限机制：Qwen3-30B-A3B、G8/batch32/最多5次simulation、10k queries/8train+4OOD任务；不引入AI-for-Science路线。名义GT action数量不等token/tool/walltime，simulations可能分钟/小时；硬件/precision为Not Disclosed。即时reward可能漏掉通向未来更优状态的探索，原文也承认，不能把greedy单turn更新当best-turn全目标的等价最优保证。Ch33已有turn-index/history与即时/终局信用分责，但尚无该效用/采样组合具体分支；root实际source/PRE与Ch33两段1553–1555、完整邻接及末注POST通过；受限分支约束不限制一般best-of-turn效用定义。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16480v1-20261008.json)。

### [Jacobian Scopes: token-level causal attributions in LLMs](https://arxiv.org/html/2601.16407v1)

v1 §2–4/案例（blocks7–72）取post-LN hidden对输入embedding的J，leading direction/projected norm可读某target logit或hidden norm温度；Fisher trace JᵀWᵀ(diag(p)−ppᵀ)WJ刻画局部KL二阶，不等前者。target投影一次backward而完整hidden J需d_model次；CPU单句Fisher153s/temperature1.4s/forward.9s的未完整配置不能升级系统性能。Llama3.2翻译/偏见/时序case只支持局部线性化，norm温度不改变方向、不证明校准，gradient不是global causal circuit/patching或生产调试收益。仅报告诊断替代，不把术语因果标签升级长期机制。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16407v1-20261008.json)。

### [Endless Terminals: Scaling RL Environments for Terminal Agents](https://arxiv.org/html/2601.16443v1)

v1 §3–5（blocks19–70）生成task/privileged tests、执行环境并最多3次修复、要求completion tests在初始不通过，o3 pass16>0再保留3255任务（约半数丢弃）。阳性只认证当前tests与teacher可解，非任务完备/真实repo分布；frontier-filter可能删除更难任务。persistentPTY保留文件/进程状态，训练16turn/16kcontext/每turn2048，eval64turn与5分钟environment timeout；Llama3.2-3B/Qwen2.5-7B四A100两天与Qwen3-8B八B200八小时不同配置，SFT15k teacher traces另计。loop39%与turnexhaust26%部分重叠不加成失效率。局部生成过滤机制有效性可保留，但不是production正确性或统一训练预算；只报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16443v1-20261008.json)。

### [DSGym: A Holistic Framework for Evaluating and Training Data Science Agents](https://arxiv.org/html/2601.16344v1)

v1 §3/关键audit与limits（blocks18–25、57–79、119–142、174–182）移除全部dataset文件再测同任务，QRData平均40.5%为相对score drop而非残余accuracy；先人工修复或剔除无效任务，再排除五frontier模型中无文件仍≥3正确的任务。统一CodeAct/temp0条件下，curation前后up to21%相对退步揭示shortcut影响，但改变题目人口，不证明模型能力下降或完备消除泄漏。数学答案/容差与prediction私有competition metrics不同，不直接拼分数。仅采用data-free负控制与过滤有限性，不采用DSBio科学发现路线。现Ch66访问/标签权限已有，新增153–155两段data-withheld负控制/过滤人口，root实际SOURCE/PRE/完整邻接与末注POST通过，人工检查先于shortcut筛选。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16344v1-20261008.json)。

### [Clarify or Answer: Reinforcement Learning for Agentic VQA with Context Under-specification](https://arxiv.org/html/2601.16400v1)

v1 §3–5/limits（blocks21–57、69–118、120–132）：controller用CE选Answer/Clarify，独立question policy用group-mean GRPO-CR；format、GPT4o参考keywords/Jaccard和答案变化构reward，改答不是变正确。ContextClarify550题275ambiguous/275unambiguous仅一缺失factor、2B/3B/7B VL实验；user由GPT4o看图模拟，不能认证真实用户知道缺失context。mixed e2e .316→.474只是该协议，Clear/OOD另人口；human评估仅30%子集。单ask不测多轮budget，cost-sensitive threshold在future而非实现。没有新authority或总latency保障，局部controller机制与overask取舍仅报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16400v1-20261008.json)。

### [Calibrated Similarity for Reliable Geometric Analysis of Embedding Spaces](https://arxiv.org/html/2601.16907v1)

v1理论/评价/limits（blocks115–170、237–244）非降piecewise-constant isotonic可不重编码embedding而校score；但会新增ties，raw argmax仍属映射argmax集合不等唯一rank不变，threshold图可增加边，不采用all order-based constructions严格不变。HCS用human>.9条件score quantile控制的是P(score≥threshold|true-positive)式召回，不能倒作PPV P(true|score≥threshold)。human STS分布/模型变化需重新校准，discontinuous映射也非通用gradient路径。评价数字缺独立heldout明确性不采用near-perfect guarantee；不把校分替代RAG事实核验，有限posthoc替代与反侧仅报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16907v1-20261008.json)。

### [Process-Tensor Tomography of SGD: Measuring Non-Markovian Memory via Back-Flow of Distinguishability](https://arxiv.org/html/2601.16563v1)

v1方法/controlled protocol/Table2–3（blocks16–101）固定probe softmax observable下，D2−D1>0否定可收缩的observable memoryless channel；完整(θ,optimizer buffers)仍可Markov，不能称固有训练动力学非Markov。CIFAR100/Imagenette小vision模型2000probes、5seeds/128重复、batchnorm冻结/AMP关闭；100groups35positive，reset后仍22positive，50groups14signflip，不采用全collapse。mom0/placebo是重要null，二步有限witness不证明更好curriculum/下游LLMcheckpoint选择；Ch35已明确optimizer/data state与完整恢复合同，无新具体owner差额，仅报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16563v1-20261008.json)。

### [EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents](https://arxiv.org/html/2601.16690v1)

v1 §3–5/limits（blocks20–60、69–112）每agent自身trajectory与environment state生成QA，保存step/episode/runseed、answerability/hop与horizonprefix规则；groundtruth可由game signal计算不等跨agent题目相同。不同动作改变QA人口，作者称差异仅trajectory而非difficulty未受充分控制。15Jericho/seed42、Crafter5seeds；Table3 GPT5.1 A-Mem文本49.7→49.9近似、视觉43.8→42.1反退，不能概括memory普遍改善；human仅11text/3visual，不授template抗污染或通用memory容量。Ch66已有population/generator/subject身份边界，不为benchmark实例造diff；仅报告并近结论保留题目人口混杂。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16690v1-20261008.json)。

### [From Atom to Community: Structured and Evolving Agent Memory for User Behavior Modeling](https://arxiv.org/html/2601.16872v1)

v1 §3–4/Table5/limits（blocks36–76、98–110、135–146）atom含content/embedding/interactionrecords/communitylink；跨user cosine/topk形成community与prototype，2hop BFS及affected-neighbor queue传播。training forward预测与backward reflection，consolidation合并content/行为、formation新atom；inference不执行backward/evolution。content改动后community L保留不是已经验证一致性，不能自造原子维护能力；共享embedding不证明隐私。GPT3.5-turbo16k0613/temp.2、MiniLM、τ.5、100users与9随机negative是受限协议；Table5去CCML在100K NDCG10 .5069略高于full.5064，非各组件全赢。现Ch77 atomic/raw/profile与consolidation已有，显式跨user社区derived prototype补入409–411两段，root实际source/PRE/完整邻接/末注POST通过；不因recommendation拒潜在机制。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16872v1-20261008.json)。

### [AnyView: Synthesizing Any Novel View in Dynamic Scenes](https://arxiv.org/html/2601.16982v1)

v1方法/评价（blocks19–66）RGB与Plücker ray/moment编码、view token jointattention/RoPE，已知camera规范训练12种2D/3D/4D数据，Cosmos2B、40ksteps/64H200/global512/384→576。对比baseline多为zero-shot且训练域预算不同，不能唯一归implicit geometry；AnyViewBench15sets/最多64views的PSNR/SSIM/LPIPS评已知GT距离，非unknown-view真实性或physical dynamics。极低view overlap是旧warp条件失效线索，作者仍需一定spatial overlap，不授any viewpoint/unbounded support。新受限视图验证留Report，不改变现World Model action/state authority。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16982v1-20261008.json)。

### [SyncLight: Controllable and Consistent Multi-View Relighting](https://arxiv.org/html/2601.16981v1)

v1 §3–4/消融（blocks29–54、63–94）SDXL latent source→target bridge四timesteps/σ.005，pair token联合attention；training N2到inference观察N7/平均4.38，不证明arbitraryN。单reference4-channel lightmap复制其他views并未显式空间对齐，依赖learnedattention，不用camera pose不等无对应关系。6A40/batch6/100ksteps/1280×720；w/oMV22.47对full30.23有限配套训练消融支持crossview分支，但Table1环境不同不并榜。0.01GB/view主张不作为内存保证，rare lights/遮挡/低overlap未验收，不由图像一致性授真实3D状态；仅报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16981v1-20261008.json)。

### [Fast, faithful and photorealistic diffusion-based image super-resolution with enhanced Flow Map models](https://arxiv.org/html/2601.16660v1)

v1 §3–5/Table2/5（blocks66–91、109–158）训练CFG从instantaneous扩avgflow，conditional/null/quality-positive-negative目标；LSD/ESD/SSD训练额外calls2/1/0，inferenceconditional只一call，不代表训练免费。RPGAN LoRA两step detach中间状态，H100单卡128→512×4的1/2/4步.14/.22/.4s仅该workload；>2B训练模型与<100Mbaseline非等训练预算。NFE、CFG、LoRA改变保真/感知质量目标而非更多步一律更正确，细节hallucination/tiling边界保留。Ch24现CFG/flow/reconstruction目标分责足以承载通用关系，新增局部SR条件只报告。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16660v1-20261008.json)。

### [Cognitively-Inspired Tokens Overcome Egocentric Bias in Multimodal Models](https://arxiv.org/html/2601.16378v1)

v1 §3–5（blocks10–69）frozen-vision LLaVA1.5-13B LoRA，token embedding/head可训；keypoints yaw8bins与OrientAnything azimuth10bins，18k/20k token训练与200/650推理任务curriculum。Natural COCO/3DSR同信息text控制常优tokens（COCO text.84 vs.79/.78，3DSR text.63 vs.54/.57），不能只与缺pose基线比较宣称token必要。40Isle/45COCO/45SR筛orientation正确人口，外部pose成本/precision为Not Disclosed；latent unit相关不认证neural mechanism。方法方向措辞冲突不采具体yaw规则；只保留observer-coordinate条件与输入表示对照，不改通用worldstate。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16378v1-20261008.json)。

### [Where is the multimodal goal post? On the Ability of Foundation Models to Recognize Contextually Important Moments](https://arxiv.org/html/2601.16333v1)

v1方法/评价（blocks34–69）MOMENTS由football highlights推binary importance，三ALV模态的7subsets，多backbone与2prompts/最佳order人口不同。最佳VL V MCC.502与Omni LV.502不证明总体显著multimodal gain；4个include对3个exclude coalition contribution非Shapley/因果，uncalibrated logitconfidence非quality。50goal+100context评估，bestuni/mm per-item是oracle选择非可部署。highlights未入选不等nonimportant真值，训练/backbone预算不匹配；有限dominant-modality反侧保留，不授staticfusion普遍无效或selector已成立。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16333v1-20261008.json)。

### [Will It Survive? Deciphering the Fate of AI-Generated Code in Open Source](https://arxiv.org/html/2601.16809v1)

v1 §3–6/limits（blocks19–91、191–202）201repos/5171 mergedPR/15,990files/210,184lines，merge为birth，任何修改为death，Dec31右删失且≥5个月观察。AI line53.9%modified vs human69.3%可反“必然disposable”叙事，不等质量更高或未改代码正确；mixed-file归属、人群/任务复杂度与repo活跃度混杂。Cox所有covariates PH检验p<.005违背，HR.842只能受限平均描述，KM/logrank与非random cohort近结论；Devin71.7 vsCursor38.7非工具因果。Ch66 137–154已说明merge/retainedratio代理不是真值；没有新可操作release policy，only纵向上下文。root实际必要源及具体owner核通过。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16809v1-20261008.json)。

### [ResAgent: Entropy-based Prior Point Discovery and Visual Reasoning for Referring Expression Segmentation](https://arxiv.org/html/2601.16394v1)

v1 §3–4/Table3–4（blocks31–65、78–100）coarse bbox geometry logistic entropy是选择proxy不是校准uncertainty；候选点标色与imageVQA yes/no variants聚合，再Top5/2positive1negative送SAM，LoRA VBR与COCO-adapt SAM额外训练。Table3 textcoord→VBR avg78.20→80.63支持限定接口对照；K4→5反而80.63→79.87、时间4.86→5.03，更多points不必更好。硬件/precision未完整披露，不作生产时延或置信保证。定点core足以判断视觉验证新边界，不把模块成熟当拒绝依据；root实际必要源准入通过；LoRA/SAM风格适配与marker界面组合有局部验证，不归因纯interface，只报告受限RES分支。 必要原件：[exact-v1 核心](_sources/supplement-core-2601.16394v1-20261008.json)。

### [Learning Domain Knowledge in Multimodal Large Language Models through Reinforcement Fine-Tuning](https://arxiv.org/html/2601.16419v1)

v1 §3.2/4/Table6–8（blocks19–50、66–81）除output constraint，policy在原/变换image分布KL约束与Aᴰ=(1−JS)A的有符号缩放；一致性较高时负advantage反而更负，不能说一律更大；JS[0,1]需base2约定，仅按作者口径。输入旋转等symmetry只有标签不变的classification适用，不外推grounding坐标任务。UCM Table6 domainadaptation comparison几乎无改善，Table7 outputconstraint小而distribution consistency更好，支持有限通用VLM弱监督条件而非单domain reward替换。prompt与objective信息/训练条件不等，不能采“prior必须注入objective”或科学任务成绩；Table8与JS/KL prose选择不授普遍JS-DC优越。root实际必要源范围核通过，标准仅报告，不以领域标签忽略潜在学习机制。必要原件：[exact-v1 核心](_sources/supplement-core-2601.16419v1-20261008.json)。

### [Retrieve-Refine-Calibrate: A Framework for Complex Claim Fact-Checking](https://arxiv.org/pdf/2601.16555v1)

exact-v1 HTML两次404后改官方PDF页2–6的§2–3/Tables1–4，未追无关附件。LUKE实体→BM25→claim-conditioned paraphrase→同LLM低selfconfidence重评；§2.1的refutes还包括insufficient/unverifiable，不等全部已证false。自报γ不是校准正确率，高置信错误不会触发重试。同backbone/retrieval的完整框架在3/4hop切片有收益，Table1二跳FOLK更好，支持有限替代路线而不唯一归因decomposition噪声；Table2/3消融仅限定pipeline，不能授通用消除此噪声。更多entity/doc可能退步；Table4 HOVER四列相同却average3.45/2.87矛盾，FEVEROUS平均方向相反，隔离该质量评估命题，不授refinement全面改善。原拟关闭错误地要求独立所有组合因素，已撤销，保留5分标准仅报告的受限设计选择；未建立当前Books应更换通用fact-check规则。硬件/precision及完整重复预算Not Disclosed，未运行代码。root实际必要PDF与完整AB独核通过，未采子命题争议不用于Books或正面质量保证。[必要原件定位](_sources/supplement-rrc-core-20261008.md)、[v1题摘](_sources/supplement-rrc-semantic-v1-abstract-20261008.jsonl)及[落日字段](_sources/supplement-rrc-date-bounds-20261008.jsonl)保留。

### [SemanticALLI: Caching Reasoning, Not Just Responses, in Agentic Systems](https://arxiv.org/html/2601.16286v1)

v1 §3–5（[blocks34–104](_sources/supplement-core-2601.16286v1-20261008.json)）AIR(q,schema)→canonical intent I与VS(serialized I)→visual directives C分别缓存，lexical schema约束拒DDA/GA4 cosine≈.96但不同metric语义的匹配。500prompts下AIR194 semantic hits与VS4841invocations/4023 exact hits不同分母，不可把83.10%倒推准入/整体收益。τ.90→.85同500prompts、20agents的mean57.3→31.5s是具体阈值取舍；§5明确未评analytic accuracy，Fig1 tokens节省是counterfactual投影，不是实测等质量收益；VS讨论τ.95不同于evaluation.90不混用。text-embedding-3-large3072/HNSW/BM25/RRF为方法，模型、硬件、precision/并发为Not Disclosed；closed proprietary仅作者trace，不授公开实现已核或生产通用性。采用阶段key与entity-sensitive复用的有限设计验证，5分标准仅报告；不要求新retrieval算法或完备quality证明才准入，原拟关闭撤销。

### [EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration](https://arxiv.org/html/2601.16489v1)

v1 §3.2–3.3/4–6/limits（[blocks37–49/52–88/98–99](_sources/supplement-core-2601.16489v1-20261008.json)）主agent在有限context执行atomic commands，把stdout/exitcode交独立expert，压缩诊断反馈返回；expert可动态创建单行工具但只收集diagnostic evidence、禁止维修，repair commands仍是建议。这个具体分责/只读接口增量不该因摘要只写self-evolve/领域成绩关闭；原粗关闭已撤销。规则如何incremental update没有可重现操作语义，不补造；Table4随机100EnvBench83→75去掉整个expert module，非self-evolve独立效应。Repo2Run420与EnvBench324/小模型30子集、2小时/100round、GPT4o-2024-05-13/GPT3.5/GPT4omini与纠错4201 EnConda GPT4.1/DeepSeekV3不同协议；Table5成功build子集30.5→20.9分钟不推广全任务，hardware/precision/并发Not Disclosed。EBSR只要求Docker build且pytest能执行，不要求tests通过；缺文件、硬件/依赖安装/测试timeout仍失败。root实际必要源有限命题通过，标准6仅报告，不把诊断建议当可信权限或环境正确性，不强造Books差额。公开日合取[字段](_sources/supplement-evoconfig-date-bounds-20261008.jsonl)与官方final-ID规则为Jan26；[精确v1题摘](_sources/supplement-evo-tensor-v1-abstract-20261008.jsonl)保留。

## 5. 缺口与下一步

本轮作者扫描、准入处理、必要证据与Books写入普通待办0；新增23项已逐项获得root必要原源与具体处置独核，四处正文/完整邻接及自身末注POST通过。root六部分DAY独立验收已通过，完成态已同步，普通可执行工作0。具名来源/日期/子命题终态限制依下段保留，不采用上一轮完成声明或机器校验代替本轮语义验收。

本轮source终态保留：§2逐行所列OpenAI/Anthropic/Google/Meta/Qwen/Moonshot/Hunyuan/ZAI/Seed/ERNIE的目标历史目录，以及arXiv三个相关月标题片段未恢复；已有限首查/定点恢复/停止，不能用于正面Coverage或零事件。接受各源Jan26主线官方事件片段/明确日期正文、或相应arXiv官方标题片段后只重开该入口，不扩全年/90天。Seed与三晚final-ID潜在项依下段单一日期请求，不重复索取。

不采用子命题同样终态隔离：RRC2601.16555v1 Table4的refinement质量平均/方向冲突、SALAD2601.16515v1 prose与Table1的数字及A.3排序措辞、Calibration2601.16907v1的all-order严格不变、Domain-RL2601.16419v1的JS/KL普遍优越均不用于Books或性能/质量保证；各项必要原件已读，不以未采用子命题否定受限贡献。只接受同事件正式勘误或定义/分母/假设明确对齐后定点重开相应命题，不为了消除争议遍历新版差分。

新增日期终态保留：Lost in Simulation [2601.17087v1](https://arxiv.org/abs/2601.17087v1) 的真人/模拟用户评价反侧、Boltzmann-GPT [2601.17094v1](https://arxiv.org/abs/2601.17094v1) 的 DBM latent→adapter→冻结语言模型机制，以及 Low-Rank Tensor Approximation [2601.17112v1](https://arxiv.org/html/2601.17112v1) 的cproduct tensorization/单FFN与双FFN质量反转不能因局部/领域实例或资源预算未披露关闭。17112原粗关闭亦撤销，root定点实际v1§6.5–6.6/Table5–7识别局部结构取舍；但三项final-ID公告下界Jan26与DataCite created上界Jan27跨补充自然日，v1 Updated不单独证明首公开日期。保留[前两项v1題摘](_sources/supplement-reopened-v1-abstract-20261008.jsonl)、[前两項日期](_sources/supplement-reopened-date-bounds-20261008.jsonl)、[17112精确题摘](_sources/supplement-evo-tensor-v1-abstract-20261008.jsonl)及[17112字段](_sources/supplement-tensor-date-bounds-20261008.jsonl)，不列确定候选、不记零、不移动到另日报；接受当期官方公告批次或Jan26已公开作者正文后只重开这些身份，日期当前终态已经root通过并停止无关全文。

Seed paper API 将 [Visual Generation Unlocks Human-Like Reasoning through Multimodal World Models, 2601.19834](https://arxiv.org/abs/2601.19834v1) 与 Keel 2601.19895 标作 Jan26，官方可见 Keel index 却是 Jan27，且两篇精确 v1 Submitted 均 Jan27；API PublishDate、后来的更新时间及 Submitted 任一字段均不足消除此首正文边界冲突。保留 [API 原件](_sources/supplement-seed-paper-20261008.json)和[exact-v1 日期核](_sources/supplement-seed-date-20261008.txt)，本轮不采用；重开需同事件 Jan26 作者正文/明确官方公告。MiniMax M2her 当前官方展示 Jan27，故不纳 Jan26 补充候选；原窗口的历史日期保留理由仍按下文原记录保留，不重算旧归属。

普通可执行待办0。原ARMD/CORD仅报告与LogitMatch贡献关闭已经纠正；37家族均具必要证据与明确Books处置，四处整合由root实际必要源→正文/邻接非作者POST通过，四项已有覆盖由实际段位核对；不为其他recipe/理论context扩书。

本窗终态保留项（外部日期/目录缺段及不采用子命题）：不用于正面证据、Books或无遗漏断言；日期项不进入确定候选，GRIP争议数字不属于已采用命题。以下各项仅按精确定点重开条件恢复：

- [2601.17111v1](https://arxiv.org/abs/2601.17111v1)和[2601.17086v1](https://arxiv.org/abs/2601.17086v1)：标准下界Jan26T01Z、DataCite created上界分别Jan27T03:42:15Z/03:41:42Z，跨09BJT截止。缺同事件作者首次公开/官方公告timestamp；不自动宣称Jan28归属。接受精确公告批次、作者artifact首次body时间或完全落窗前后界，只重开这两个ID的日期。
- [MiniMax M2her](https://www.minimax.io/blog/minimax-m2-her)：核心selfplay/taxonomy/synthesis/RLHF实际读，但展示Jan27与JSONLDPublished/Modified均00Z不足确定真实首公开边界，缺同事件作者timestamp/可靠artifact；[原字段](_sources/minimax-date.json)。不得把页面date无精度时间格式升级真实时刻。
- Seed Keel：作者页面Jan27与[2601.19895v1](https://arxiv.org/abs/2601.19895v1)提交Jan27T18:58:46Z不能确认作者正文是否曾在本窗前公开，需作者首正文timestamp/官方announce；[原history](_sources/seed-keel-date.json)。不因晚arXiv提交证明作者首次同样晚，不补整站历史。
- 必要历史目录缺段：OpenAI/Anthropic/Google/Meta/Qwen/Moonshot/Hunyuan/Seed等当前入口/有限补检不证明目标历史完整；恢复需该源本窗语言/多模态/训练推理Agent原事件列表或时间明确原文，定点重开各ID本窗，不逐全年目录。Hunyuan“全部”browser两次有限失败后终态隔离；不说空目录。其他已夹窗可读博客/changelog只支持其列表范围，不能升级全机构无遗漏。
- GRIP2601.16905v1正文恢复百分比与Table4冲突：保留路由几何与有限expertforcing定义，但恢复比率/真erase/safety保证不采用。只有同事件正式勘误或明确指标与分母对齐可重开冲突命题，不为了消除争议读后来v3替代v1。

窗外恢复线索不属本窗且不阻塞：LongCat2601.16725采用body已在Jan23官方commit PDF第1/9/10页出现，首公开归属早于本窗；保留[history](_sources/longcat-history.json)和[实际旧body必要读取](_sources/longcat-early-pdf.json)，不假称早事件已完成别日报。特殊late-announcement/新修订线索只有出现具体原事件才恢复真实归属日，不扩月/Weekly。

## 6. 复核

本轮增量复核者：root（非本轮报告作者）。本轮结论：通过；root实际完成全部23项必要primary source、4整合owner PRE/POST、1具体Existing、分层排除/3跨日日期保留，以及本轮全部六部分DAY（含旧有效§6尾部恢复读取）。本轮完成，普通可执行工作0。37完整题摘先按8潜在/代表关闭、第二19题摘校准，后定点恢复RRC/Semantic及ResAgent/Domain-RL；不是宽库存逐篇排除。新23=5深入+18标准，root逐项实际读取精确v1必要方法、关键对照/评价和直接限制；已有覆盖1项SWE-Pruner具体Ch75；4整合为Ch12/33/66/77各两段与自身末注，source/PRE/实际正文完整邻接POST通过。纠正Engram100M数据集/82M训练token、TL-GRPO方案约束非一般best-turn限制、DSGym人工检查先于shortcut过滤；其余18仅报告限定population/代理/费用，不把局部验证视作普遍production机制。RRC refutes含未证/不可验证、γ非校准且不重试高置信错误，Table4质量平均冲突隔离；Semantic阶段分母/阈值/质量未验已近结论。17087/17094/17112完整v1题摘与跨日字段亦实际独核，撤销粗关闭后日期隔离，不进入确定分母。EvoConfig定点只读诊断界限及Jan26日期已核；其余11关闭按来源/理由分层校准，不声称全部宽列表审阅；下文仅保留上一轮有效复核。

本轮最终机器与保护检查：60候选（原37+新增23）、17深入/43标准，Books8整合/5具体已有/47仅报告；原37行逐字及原§4连续正文对照通过，158个本地引用缺0、候选表连续，完成态V3与本日/四owner限定unstaged/cached diff-check通过。没有stage、commit、push或改其他日/索引/State；共享Books其他并发差额不归本轮，不声称实验复现或全源无遗漏。

复核者：root与/root/jan27_gate（均非报告作者；jan27_gate后续撰写的Ch24/51/29新段由root非作者POST，不自验）。

结论：通过

本日37=12深入完成+25标准完成，Books=4整合+4已有覆盖+29仅报告；普通可执行尾部0，终态保留项不支持正面Coverage/Evidence/Books或无遗漏声明。root首批八项有效必要源核与Ch13写后POST复用，jan27_gate实际重读当前合同/本日停点，按最终主张核其余27篇exact-v1 HTML blocks的必要机制、对照/评价条件与直接反侧，以及Kimi0.88正式release字段、PR681实际9行patch和2025-06-18官方transport规范；另定点重开LogitMatch，双方实际v1必要机制/评价/反侧完成，合计37家族必要证据覆盖，但不是全文/所有附件重审。

日期层实际核29份采用identity与identity-extra中6项原字段；加16946单项原字段后所有36篇submitted都在Jan23T19Z前，最大created为Jan26T02:42:29Z，官方Sunday20EST与共同保守10:43BJT端点一致。17111/17086仍跨截止而非自动窗外，LongCat实际旧PDF第1/9/10页足以支持早body关闭。来源层实际核模型6页103条、系统1页6条、多模态2页38条到尾和14日级来源/按需触发行完整，不把宽库存变逐篇队列；机构有限历史目录夹窗/停止范围与Hunyuan两次有限browser失败复用root实际独立检查；只能支持发现范围与停止限制，缺段仍隔离，不授完整历史召回。

Books层实际顺读Ch13当前修正与32–42前后交接、Ch35 285–310 provider/captureepoch/hostpool/restore正文；Ch35已有覆盖成立。另外定点读Ch24 masked-generation、Ch51 117–140 structured-generation、Ch66 626–642可见输入与墙钟协议、Ch77 194–207 task适用性，ARMD query/KV联合排标签与LogitMatch input-span状态具体差额已落实，root实际原源→正文/邻接POST通过；RPEval/OnlineSI/Timely已改具体Existing。P-Tokens/Memory-V2V逐段比Ch29/Ch24后仅报告通用编辑分隔符recipe与生成历史实施配置；CORD同prefix跨模态student分布已在Ch29 262–264补接口，root实际必要原源及248–272邻接/末注POST通过。排除抽检按理由分层：AgentDrive的单域benchmark题摘、LogitMatch的解码机制与tokenization必要段、另三项成熟recipe/单域应用关闭复用root首批校准；不声称所有宽列表排除全验。LogitMatch明确机制被原关闭理由漏掉，已重开这一项并单核日期，没有重开全池。

格式校验：python3 scripts/validate_research.py --report papers/2026/01/27/README.md 通过（1 V3）；限定git diff --check通过；本地引用存在、六部分/37候选行及12深入+25标准、4整合+4覆盖+29仅报告一致性通过。机器检查不替代语义验收。已有与无关worktree/staged变更均保护，本任务未stage/commit/push。
