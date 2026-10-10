# Daily Research — 2026-01-27

**规范：** V3
**窗口：** 2026-01-26T09:00:00+08:00 ～ 2026-01-27T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T12:08:15+08:00

## 1. 结论

本日有三类需要分账的增量：理想Attention对称性不能直接移植有限浮点实现；checkpoint异构状态语义与byte movement分离仍须captureepoch/背压/restore；Agent与多模态评价应区分信息接口、几何合法与真实执行。其余局部机制与反侧按各自配置保留，不合并为普遍性能或安全结论。

发现采用有限主题查询、官方目录片段和必要精确事件恢复，不把103条模型查询或全年目录当候选/全文队列。本日冻结候选37唯一家族（36篇arXiv精确v1＋Kimi CLI0.88）；原作者36项必要审阅和独立重开LogitMatch共37/37，独立必要证据37/37，日级语义验收通过。已有具体贡献关闭4项及LongCat早正文去重，另4项必要日期隔离，不冒正面候选。Books已实际整合4项/4文件（MODEL-POSITION-ENCODING、MULTIMODAL-GENERATIVE-PARADIGMS、INFER-SGLANG、TRAIN-SFT），具体已有覆盖4项（TRAIN-CHECKPOINT、AGENT-MEMORY、PLATFORM-EVALUATION-SYSTEM、AGENT-PLANNING）；其余29项仅报告，逐项具体采用对象/长期差额已核；不把报告-only当book写入。

Ch13实际22/31/33–35行修正了无条件的排列等变解释，root必要原源与写后衔接POST通过。没有运行论文代码、复现实验或验证GPU/生产行为。外部目录/日期保留不支持无遗漏、Coverage通过或正面安全保证；四处整合均获非作者实际必要源→正文/邻接POST；没有普通可执行待办。

## 2. 来源覆盖

执行2026-10-04，仅本日窗口和ROADMAP模型/训练/推理/平台/Agent/多模态主题；原始查询、分页、停止、具体关闭见[有限发现记录](_sources/discovery.md)。结果“已检查”只指表中实际范围，不是完整官网历史覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | openai.com/research及news；site:openai.com "January 26, 2026"、模型/训练/推理主题定点搜索 | 已检查 | Jan26 Maggie Hulce业务访谈不贡献机制；ChatGPT voice release说明为功能/质量事实无新机制。当前目录+补检不构成完整历史目录。 |
| SRC-ANTHROPIC | anthropic.com/research与Jan26/模型Agent主题定点搜索 | 已检查 | Jan15 EconomicIndex窗外；未得到本窗机制线索。当前入口未证明完整历史。 |
| SRC-GOOGLE-AI | deepmind.google/research、research.google/pubs及research.google/blog；Jan26定点主题补检 | 已检查 | 年度/分类目录只线索，未逐年/逐页扫；本窗没有可确认事件线索，历史缺段隔离。 |
| SRC-META-AI | ai.meta.com/research无法提取正文；site:ai.meta.com Jan26主题定点补检 | 受阻 | 空提取/空搜索不能证明0命中，历史目录缺段隔离。 |
| SRC-QWEN | qwenlm.github.io重定向qwen.ai，旧页2025文章；qwen.ai/blog无法提取；Jan26定点补检 | 受阻 | 无可确认原事件线索，动态历史目录未恢复，不证明无遗漏。 |
| SRC-DEEPSEEK | deepseek.com当前页面；api-docs.deepseek.com/updates官方完整可读changelog | 已检查 | 所列更新从2026-04-24跨至2025-12-01，本窗没有列出更新。范围仅该changelog，不覆盖未列研究。 |
| SRC-MOONSHOT | platform.kimi.com/blog可读25条最新至2025-11-07；MoonshotAI/kimi-cli exact release 0.88/PR681 | 已检查 | Kimi0.88正式published_at落窗；只核改变HTTP header ownership的patch，不遍整repo。K2.5 repo Jan30 created不是模型首次证明，模型历史入口仍缺。 |
| SRC-TENCENT-HUNYUAN | hunyuan.tencent.com/research动态页无正文；子线程browser一次超时，root独立IAB一次36.8秒超时并kernelreset | 受阻 | 无法核“全部”历史范围，终态隔离该必要目录缺段；不能说空目录或0研究，不继续无界重试。 |
| SRC-ZAI | zhipuai.cn/zh/research官方可读research目录 | 已检查 | Feb2 GLMOCR→Jan19 GLM4.7Flash→Jan13，停止到Jan19并核夹窗；仅此可见research目录无Jan26列项，不代表所有artifact。 |
| SRC-BYTEDANCE-SEED | seed.bytedance.com/en/research选择目录Jan27 Post-LayerNorm→Dec2；public_papers第一页20/242；Jan26定点补检 | 已检查 | 242条只route非13页队列。Keel作者Jan27页与arXiv19895v1提交Jan27T18:58:46Z不能唯一证明本窗作者首公开，精确日期保留。 |
| SRC-BAIDU-ERNIE | ernie.baidu.com/blog/zh官方首页 | 已检查 | Jan29 PaddleOCRVL→Jan15 ERNIE榜单夹窗，停Jan15；只此博客列项，不覆盖无独立时间artifact。 |
| SRC-XIAOMI-MIMO | mimo.xiaomi.com papers/blog | 已检查 | papers Jan8 MiMoV2Flash→Feb3 HySparse夹窗；blog少量未有精确本窗时间条目，不证明全部GitHub事件。 |
| SRC-MINIMAX | minimax.io/blog14条、minimaxi.com/blog重定向minimax.cn、agent.minimax.io/docs/techblog15导航项 | 已检查 | Jan27 M2her→Dec23 M2.1；M2her核心机制已读但展示日/JSONLD00Z不足精确首公开时刻，跨本窗边界日期保留。 |
| SRC-ARXIV | 上述有限3主题slice+相关官方标题补检；必要项exact-v1/identity metadata | 已检查 | 列表分页已到尾；特殊late、未匹配术语或早artifact不能从标准公告推定保证。不把143左右去重线索误称候选数。 |
| 表外：[MCP规范](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) | Kimi header变化触发，仅精确2025-06-18 Session Management/传输条件 | 已检查 | 非来源发现扫描；未证明任意SDK/所有server行为 |
| 补检：[DataCite](https://api.datacite.org/dois) | 选中arXiv ID的created/registered/dates恢复；identity-*.json及identity-extra.json | 已检查 | 只身份/日期上界，不能证明首公开时刻或研究结论 |

SRC-ARXIV有效分页：模型0/20/40/60/80/100共6页到103尾，系统1页6条到尾、多模态0/20共2页38条到尾；跨分类线索先去重，不报这些线索为当窗研究数量。主题提交slice为2026-01-22T19:00:00Z～2026-01-23T19:00:00Z；模型CL/LG/AI+language model/transformer/MoE，系统DC/AR/PL/OS/PF+LLM/GPU/training/inference，多模态CV/RO/IR/MA+foundation/multimodal/worldmodel/VLA/diffusion/RAG/agentmemory。cs.CL月目录只浏览16979～16276附近相关标题。失败/截断Atom不用于覆盖。Daily未扫描Weekly来源。

## 3. 候选与判断

以下arXiv公开时间均为**推定区间**2026-01-26T09:00:00+08:00～2026-01-26T10:43:00+08:00，完全落窗，非逐篇精确公开时刻。[官方availability](https://info.arxiv.org/help/availability.html)本批标准Sunday20:00 Eastern对应下界Jan26T01Z，exact-v1提交在Friday14:00 Eastern cutoff前；各DataCite created为上界（最大Jan26T02:42:29Z），共同端点向下一分钟保守扩至10:43。每项原始history、created精度/时区保存在identity-ID.json；新增6项在[identity-extra.json](_sources/identity-extra.json)。created不能当精确public时刻；早正文LongCat与跨截止上界两项已另隔离。当前精确abs/事件页没有影响采用命题的撤回/删除提示，不为证明无标记遍历全史。

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

## 5. 缺口与下一步

普通可执行待办0。原ARMD/CORD仅报告与LogitMatch贡献关闭已经纠正；37家族均具必要证据与明确Books处置，四处整合由root实际必要源→正文/邻接非作者POST通过，四项已有覆盖由实际段位核对；不为其他recipe/理论context扩书。

本窗终态保留项（外部日期/目录缺段及不采用子命题）：不用于正面证据、Books或无遗漏断言；日期项不进入确定候选，GRIP争议数字不属于已采用命题。以下各项仅按精确定点重开条件恢复：

- [2601.17111v1](https://arxiv.org/abs/2601.17111v1)和[2601.17086v1](https://arxiv.org/abs/2601.17086v1)：标准下界Jan26T01Z、DataCite created上界分别Jan27T03:42:15Z/03:41:42Z，跨09BJT截止。缺同事件作者首次公开/官方公告timestamp；不自动宣称Jan28归属。接受精确公告批次、作者artifact首次body时间或完全落窗前后界，只重开这两个ID的日期。
- [MiniMax M2her](https://www.minimax.io/blog/minimax-m2-her)：核心selfplay/taxonomy/synthesis/RLHF实际读，但展示Jan27与JSONLDPublished/Modified均00Z不足确定真实首公开边界，缺同事件作者timestamp/可靠artifact；[原字段](_sources/minimax-date.json)。不得把页面date无精度时间格式升级真实时刻。
- Seed Keel：作者页面Jan27与[2601.19895v1](https://arxiv.org/abs/2601.19895v1)提交Jan27T18:58:46Z不能确认作者正文是否曾在本窗前公开，需作者首正文timestamp/官方announce；[原history](_sources/seed-keel-date.json)。不因晚arXiv提交证明作者首次同样晚，不补整站历史。
- 必要历史目录缺段：OpenAI/Anthropic/Google/Meta/Qwen/Moonshot/Hunyuan/Seed等当前入口/有限补检不证明目标历史完整；恢复需该源本窗语言/多模态/训练推理Agent原事件列表或时间明确原文，定点重开各ID本窗，不逐全年目录。Hunyuan“全部”browser两次有限失败后终态隔离；不说空目录。其他已夹窗可读博客/changelog只支持其列表范围，不能升级全机构无遗漏。
- GRIP2601.16905v1正文恢复百分比与Table4冲突：保留路由几何与有限expertforcing定义，但恢复比率/真erase/safety保证不采用。只有同事件正式勘误或明确指标与分母对齐可重开冲突命题，不为了消除争议读后来v3替代v1。

窗外恢复线索不属本窗且不阻塞：LongCat2601.16725采用body已在Jan23官方commit PDF第1/9/10页出现，首公开归属早于本窗；保留[history](_sources/longcat-history.json)和[实际旧body必要读取](_sources/longcat-early-pdf.json)，不假称早事件已完成别日报。特殊late-announcement/新修订线索只有出现具体原事件才恢复真实归属日，不扩月/Weekly。

## 6. 复核

复核者：root与/root/jan27_gate（均非报告作者；jan27_gate后续撰写的Ch24/51/29新段由root非作者POST，不自验）。

结论：通过

本日37=12深入完成+25标准完成，Books=4整合+4已有覆盖+29仅报告；普通可执行尾部0，终态保留项不支持正面Coverage/Evidence/Books或无遗漏声明。root首批八项有效必要源核与Ch13写后POST复用，jan27_gate实际重读当前合同/本日停点，按最终主张核其余27篇exact-v1 HTML blocks的必要机制、对照/评价条件与直接反侧，以及Kimi0.88正式release字段、PR681实际9行patch和2025-06-18官方transport规范；另定点重开LogitMatch，双方实际v1必要机制/评价/反侧完成，合计37家族必要证据覆盖，但不是全文/所有附件重审。

日期层实际核29份采用identity与identity-extra中6项原字段；加16946单项原字段后所有36篇submitted都在Jan23T19Z前，最大created为Jan26T02:42:29Z，官方Sunday20EST与共同保守10:43BJT端点一致。17111/17086仍跨截止而非自动窗外，LongCat实际旧PDF第1/9/10页足以支持早body关闭。来源层实际核模型6页103条、系统1页6条、多模态2页38条到尾和14日级来源/按需触发行完整，不把宽库存变逐篇队列；机构有限历史目录夹窗/停止范围与Hunyuan两次有限browser失败复用root实际独立检查；只能支持发现范围与停止限制，缺段仍隔离，不授完整历史召回。

Books层实际顺读Ch13当前修正与32–42前后交接、Ch35 285–310 provider/captureepoch/hostpool/restore正文；Ch35已有覆盖成立。另外定点读Ch24 masked-generation、Ch51 117–140 structured-generation、Ch66 626–642可见输入与墙钟协议、Ch77 194–207 task适用性，ARMD query/KV联合排标签与LogitMatch input-span状态具体差额已落实，root实际原源→正文/邻接POST通过；RPEval/OnlineSI/Timely已改具体Existing。P-Tokens/Memory-V2V逐段比Ch29/Ch24后仅报告通用编辑分隔符recipe与生成历史实施配置；CORD同prefix跨模态student分布已在Ch29 262–264补接口，root实际必要原源及248–272邻接/末注POST通过。排除抽检按理由分层：AgentDrive的单域benchmark题摘、LogitMatch的解码机制与tokenization必要段、另三项成熟recipe/单域应用关闭复用root首批校准；不声称所有宽列表排除全验。LogitMatch明确机制被原关闭理由漏掉，已重开这一项并单核日期，没有重开全池。

格式校验：python3 scripts/validate_research.py --report papers/2026/01/27/README.md 通过（1 V3）；限定git diff --check通过；本地引用存在、六部分/37候选行及12深入+25标准、4整合+4覆盖+29仅报告一致性通过。机器检查不替代语义验收。已有与无关worktree/staged变更均保护，本任务未stage/commit/push。

