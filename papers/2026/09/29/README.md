# Daily Research — 2026-09-29

**规范：** V3

**窗口：** 2026-09-28T09:00:00+08:00 ～ 2026-09-29T09:00:00+08:00

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-10-01T19:16:12+08:00

## 1. 结论

本日冻结 **43个唯一贡献候选家族：40篇arXiv首次公开材料、3项OpenAI官方事件**，均已完成与拟采用命题相匹配的必要证据审阅及Books判断；**40项实际整合、3项仅报告**。原19项有效证据与实际写后结果复用，新增24项有分批非作者审阅和实际书稿POST；摘要准入、证据支持和写入验收分别记录，不把宽分类命中称为几百篇项目贡献。

本日主线包括：训练/服务资源计划须与实际状态提交分权；近似状态复用、精度切换及Kernel选择都须保留质量/可执行性边界；评价要分开reference、测量坐标和真值；Agent与物理行动的旧proposal不能由内部一致性自授提交。SPIMOE、MTP profile和Argus局部验证保留报告，不重复书中既有通用机制。正文保留旧方案成立条件、代价、反证与fallback，未复现实验，也没有采用普遍性能或安全保证。

14个到期来源已处理到有限停止或精确外部隔离；**7组目录/发布时间限制**见§5，未被算作正面覆盖或候选。必要证据、Books处置、实际写后复核及非作者整日验收均已通过，普通待办为0；本次完成仅指本日报合同允许的安全终态，不扩大到其他日期/Weekly，也不声明外部缺口消失。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research Index](https://openai.com/research/index/)与官方RSS日期有序前14条，越窗到Sep23停止；本窗Dots、Safety cases、Australia三核心；Lenfest负侧关闭。GPT6.1Sol/DevDay窗后、CodexOriginals/Basis窗前不深读 | 已检查 | 支持这些公开入口的有限停点，不证明全组织召回 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)日序30/29→25/24→17；GLM5.3 JSON-LD Sep29 15:46Z窗后，survey核心无新控制/评价机制；Sonnet真实详情定点恢复 | 受阻 | Sonnet5.5仅Sep28日级、时区/时刻缺失，外部项1隔离 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/)日序Sep16→1→Aug26；News Argon窗后、LiveAvatar24/PrivateCompute23窗前；[Research Blog](https://research.google/blog/) Sep29→24→18。DiffusionController属2603.06981旧家族且无重要修订信号；CustomAgents核心具体关闭 | 受阻 | 年度/标题排序的[Publications](https://research.google/pubs/)不构成日级停止，外部项2隔离；不是全站无发布 |
| SRC-META-AI | [Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)日序Sep24→7→6；[Blog](https://ai.meta.com/blog/)首页混排序，限定Sep28查询只作补检 | 受阻 | Blog历史窗口列表无法确认，外部项3隔离，不把旧卡/搜索零结果当零发布 |
| SRC-QWEN | [Research](https://qwen.ai/research)和detail动态shell；官方github旧Blog2025Sep23→Aug19；可用替代入口仍缺本窗列表 | 受阻 | 外部项4：可归属本窗的官方Research公开目录 |
| SRC-DEEPSEEK | [Updates](https://api-docs.deepseek.com/updates/)直接官方HTML恢复，日序Sep10→Aug21→Aug13→Jul31；News最近Sep10、公开论文入口Jun24 | 已检查 | 完成这些公开入口有限停止，不作全组织commit断言 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)可见2025Nov7→Jan23；CLI releases Sep22→21→1、Sep23归档；Kimi-K2 releases空列表，仅支持该入口 | 已检查 | 不把空releases扩大成全组织零事件 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)官方publicList page1/size30/renderType0，9/9到末；100116日期字段不同，但原2608.29296仅v1 Aug29，无重要修订信号，网页出现不重计论文 | 已检查 | 仅核该公开Research列表与对应家族，不把其他发布类型归零 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) Aug26→14→Jun16；[release](https://docs.z.ai/release-notes/new-released) Aug26→18→Jun16有序停点 | 已检查 | 不遍历全组织普通PR，不宣称全组织零事件 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) Jul6；[public_papers](https://seed.bytedance.com/en/public_papers) Aug18→12→6；en/zh Blog动态shell，有限替代未恢复历史日期 | 受阻 | 外部项5：本窗官方Blog列表/发布日期，不能由论文旧首页推零 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)最近May9；[官方releases](https://github.com/PaddlePaddle/ERNIE/releases)完整可见单条ernie-4.5 Jun30 | 已检查 | 仅上述公开Blog/release入口停止，不外推全部commit |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/) Paper8项最近Jun29→Mar13→Feb3→Jan8；Blog15卡无日期，相关五卡定点详情仍无可归属时间 | 受阻 | 外部项6：五具名卡原始日期/正文，不把动态空壳归零 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)/[中文](https://www.minimaxi.com/blog) Aug13→Jul31→Jun9；[techblog](https://agent.minimax.io/docs/techblog.md) May13；[changelog](https://agent.minimax.io/docs/changelog.md) v3.0.74/CLI0.5.9核心具体关闭、0.5.8生命周期信号定点核 | 受阻 | 外部项7：0.5.8精确release时间/时区；0.5.9局部计数/UI/字节修复不构新机制 |
| SRC-ARXIV | fresh official Tue29 CL392/DC76 New+Cross仅为原始身份库存；CL首140/DC76标题、AR Tue29 16条/OS4条/PF20条New+Cross标题（越窗至Mon28停止），CV首65/RO首45/PL18/IR首45/MA首45标题有界查漏。仅具体信号读完整题摘，归并40 exact-v1贡献家族；首公开New身份与必要源/反侧均处理 | 已检查 | 分类计数含Cross/重叠，不能相加作新论文数；没有声称全列表全摘要或所有附件读完 |

来源访问/恢复日期为2026-10-01，实际查询和停止依据见[本日原始记录](../_sources/daily-20260929/screening-checkpoint.md#2026-10-01-来源尾收口优先于下面过程快照)。机构日级未知时间没有补成09:00；arXiv各家族是官方Tue29 **New**身份与[公告日程](https://info.arxiv.org/help/availability.html#announcement-schedule)联合推定正常Monday20:00 Eastern→Tuesday08:00北京时间，**不是Submitted、RSS或Cross字段单独证明**。精确v1/事件页已作轻量撤回/纠错检查，未将撤回项纳入；没有全版本逐字比较。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [TopoEP 2609.35481v1](https://arxiv.org/abs/2609.35481v1) | 2026-09-29T08:00:00+08:00 | 共享矩阵确定deviceplan与两级topology成本门；2+2+3=7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，MoonEP→Cobalt，两段实际写后root通过 |
| [WavePP 2609.35263v1](https://arxiv.org/abs/2609.35263v1) | 2026-09-29T08:00:00+08:00 | all-stage endpoint租约与suffix backing先commit、延后materialize；2+2+3=7 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，05219→retention，两段实际写后root通过 |
| [TempoKV 2609.35065v1](https://arxiv.org/abs/2609.35065v1) | 2026-09-29T08:00:00+08:00 | metadata claim与capacity commitment分开，由TTU/TTR共同触发；2+1+3=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，prefetch23049→CacheScout，两段实际写后root通过 |
| [Nereus 2609.34645v1](https://arxiv.org/abs/2609.34645v1) | 2026-09-29T08:00:00+08:00 | sealed TP/PP replica与跨stage转移DAG，feasibility与payback分权；2+2+3=7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，22614→token balance，两段实际写后root通过 |
| [EfficientAgent 2609.33762v1](https://arxiv.org/abs/2609.33762v1) | 2026-09-29T08:00:00+08:00 | pool working-set压力下host writefilter与大池恢复写全的反向条件；2+1+3=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，初Eviction→ContextResidency，实际写后root通过 |
| [AgentReplay 2609.32283v1](https://arxiv.org/abs/2609.32283v1) | 2026-09-29T08:00:00+08:00 | 模型正常forward后、nextstate前固定轨迹，logicalroute/tool等待与runtime自由度分开；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Runtime→AgentOutcome，实际写后root通过 |
| [Introducing dots](https://openai.com/index/introducing-dots/) | 2026-09-29T08:00:00+08:00 | 主动只读发现不继承delegated task执行权限；2+2+2=6 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，Omni→Scheduling，实际写后root通过 |
| [Towards safety cases for frontier AI training](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/) | 2026-09-29T03:00:00+08:00 | 持续case失效暂停covered runs，派生数据/评分恢复与权重rollback分开；3+2+3=8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，SafetyEval首两段，实际写后root通过 |
| [How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/) | 2026-09-29T03:00:00+08:00 | 初步受影响方通知不等待最终调查归因，已知/未知分别提交；3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，n-days→匿名，两段实际写后root通过 |
| [Read-Blindness 2609.35630v1](https://arxiv.org/abs/2609.35630v1) | 2026-09-29T08:00:00+08:00 | 读敏感、写增量与累积的不同权限；2+1+3=6 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，两段实际写后root通过 |
| [Entity Copy 2609.35663v1](https://arxiv.org/abs/2609.35663v1) | 2026-09-29T08:00:00+08:00 | context参与准备路由不等于原生context读出提供答案；2+1+3=6 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)，两段实际写后root通过 |
| [Rubric IRT 2609.35646v1](https://arxiv.org/abs/2609.35646v1) | 2026-09-29T08:00:00+08:00 | 条件latent测量与冻结测量器的criterion信息预算；2+1+3=6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，两段实际写后root通过 |
| [SparseOPD 2609.34386v1](https://arxiv.org/abs/2609.34386v1) | 2026-09-29T08:00:00+08:00 | 全correction观察和有符号稀疏head微分分离；2+1+3=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，两段实际写后root通过 |
| [ProbeQuant 2609.33923v1](https://arxiv.org/abs/2609.33923v1) | 2026-09-29T08:00:00+08:00 | isolated uncertainty、input secondmoment与downstream目标不同权限；2+1+3=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际两段root写后通过 |
| [Reset Is Not Recovery 2609.33672v1](https://arxiv.org/abs/2609.33672v1) | 2026-09-29T08:00:00+08:00 | reset事件不等于effectivecontext恢复，以pairedclean核残余影响；2+1+3=6 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md)，实际两段root写后通过 |
| [LLaDA-Guard 2609.33634v1](https://arxiv.org/abs/2609.33634v1) | 2026-09-29T08:00:00+08:00 | labelconditional重构证据域与verdict权限；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际两段root写后通过 |
| [World-Model Post-Training Audit 2609.33335v1](https://arxiv.org/abs/2609.33335v1) | 2026-09-29T08:00:00+08:00 | 正确预测内容与额外优化、selection与coverage归因拆开；3+1+3=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，实际两段root写后通过 |
| [Perturbed Documents 2609.33642v1](https://arxiv.org/abs/2609.33642v1) | 2026-09-29T08:00:00+08:00 | 同question/rubric的with/without文档双侧admission门；2+1+3=6 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)，实际两段root写后通过 |
| [Event-Set Completion Distillation 2609.34738v1](https://arxiv.org/abs/2609.34738v1) | 2026-09-29T08:00:00+08:00 | 实际child completion集合总概率不同于单token配给；2+1+3=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，实际两段root写后通过 |
| [Torch-PIM 2609.34657v1](https://arxiv.org/abs/2609.34657v1) | 2026-09-29T08:00:00+08:00 | Lowering 产生的实际 loop nest 决定放置候选域与 host profile 权限；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 lowering→dequantization](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [SpecStream 2609.33184v1](https://arxiv.org/abs/2609.33184v1) | 2026-09-29T08:00:00+08:00 | 仅迁移已提交历史、多 query 流式验证与 target 优先准入；2+2+3=7 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48 memory-budget→drafter](../../../../books/part-05-inference-system/48-speculative-decoding.md)；实际正文与非作者写后通过 |
| [Planarian 2609.35366v1](https://arxiv.org/abs/2609.35366v1) | 2026-09-29T08:00:00+08:00 | 预先可补偿操作与 tool-boundary 联合 capture，不自授远端 fork；2+2+3=7 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81 AgentRewind→Waypoint](../../../../books/part-07-agent/81-workflow.md)；实际正文与非作者写后通过 |
| [Dynamic Flow, Static Graph 2609.34727v1](https://arxiv.org/abs/2609.34727v1) | 2026-09-29T08:00:00+08:00 | 固定图容纳选择性 KV 重算，并按实测调用成本规划 chunks；2+1+3=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 静态图→基础优化](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures 2609.34612v1](https://arxiv.org/abs/2609.34612v1) | 2026-09-29T08:00:00+08:00 | 联合稀疏/PIM 的质量与资源耦合验证，不把 recipe 升为通用机制；2+1+3=6 | 标准完成 | 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节 |
| [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation 2609.34351v1](https://arxiv.org/abs/2609.34351v1) | 2026-09-29T08:00:00+08:00 | 非轴向 reuse 先仿射 realignment，再映射有限 CIM/layout；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 Nautilus→Persistent Executor](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection 2609.34663v1](https://arxiv.org/abs/2609.34663v1) | 2026-09-29T08:00:00+08:00 | 静态 bucket 与内生 tool re-arrival 联合决定 padding/驻留成本；2+1+3=6 | 深入完成 | 整合：`INFER-CONTINUOUS-BATCHING` [Ch46 trade-off→工程判断](../../../../books/part-05-inference-system/46-continuous-batching.md)；实际正文与非作者写后通过 |
| [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions 2609.35569v1](https://arxiv.org/abs/2609.35569v1) | 2026-09-29T08:00:00+08:00 | 固定部署运营排序与跨部署 embodied crossover 分账；2+1+3=6 | 深入完成 | 整合：`PLATFORM-COST` [Ch70 Unit Economics 生命周期→需求反弹](../../../../books/part-06-ai-infrastructure/70-cost.md)；实际正文与非作者写后通过 |
| [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference 2609.35188v1](https://arxiv.org/abs/2609.35188v1) | 2026-09-29T08:00:00+08:00 | 每有效 token 的调用摊销与单 kernel 时间不是同一指标；1+1+3=5 | 标准完成 | 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节 |
| [DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory 2609.34380v1](https://arxiv.org/abs/2609.34380v1) | 2026-09-29T08:00:00+08:00 | persistent weights/residual/KV 非对称共享与 forward 模式提交；2+2+3=7 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54 双模式 Weight 与 KV](../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过 |
| [Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding 2609.33889v1](https://arxiv.org/abs/2609.33889v1) | 2026-09-29T08:00:00+08:00 | weight-read/KV-read 的 byte 交点还须质量和 kernel 成本校准；2+1+3=6 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54 少读 Weight 与少读 KV 的交点](../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过 |
| [Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs 2609.33477v1](https://arxiv.org/abs/2609.33477v1) | 2026-09-29T08:00:00+08:00 | 按 linear group 保存输入锚点，近似 replay 与发布边界分开；2+2+3=7 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45 Group 输入锚点→Video cache](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；实际正文与非作者写后通过 |
| [BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification 2609.34785v1](https://arxiv.org/abs/2609.34785v1) | 2026-09-29T08:00:00+08:00 | 允许 transaction timing 差异但双产物都须独立 hidden gold；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Transaction oracle→Dense Process](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过 |
| [Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization 2609.35508v1](https://arxiv.org/abs/2609.35508v1) | 2026-09-29T08:00:00+08:00 | 同 workload reference 与 tree/probe 定位的受限实现验证；1+1+3=5 | 标准完成 | 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节 |
| [Hardware-Aware Features for CUTLASS Kernel Selection 2609.35587v1](https://arxiv.org/abs/2609.35587v1) | 2026-09-29T08:00:00+08:00 | candidate-induced 硬件代理排序、shape-group 留出与执行 coverage；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 硬件行为代理→Tensor Core层级](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [Semantic Prefix Oracles 2609.35425v1](https://arxiv.org/abs/2609.35425v1) | 2026-09-29T08:00:00+08:00 | 语义 prefix 安全剪枝与可完成性是两份合同；2+2+3=7 | 深入完成 | 整合：`INFER-SGLANG` [Ch51 Structured Generation→Adapter readiness](../../../../books/part-05-inference-system/51-sglang.md)；实际正文与非作者写后通过 |
| [Rubric-Calibrated Preferences 2609.35739v1](https://arxiv.org/abs/2609.35739v1) | 2026-09-29T08:00:00+08:00 | query内BT排序与跨query单位/原点分开校准；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Judge Ranking→Route/defer](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过 |
| [SpeakGR 2609.35430v1](https://arxiv.org/abs/2609.35430v1) | 2026-09-29T08:00:00+08:00 | 扩SID词表后分开检索正确与原文本条件分布保护；2+1+3=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29 Occupancy→共享Trace](../../../../books/part-04-training-system/29-sft.md)；实际正文与非作者写后通过 |
| [TRACE 2609.33517v1](https://arxiv.org/abs/2609.33517v1) | 2026-09-29T08:00:00+08:00 | return epoch 下逐项有效不等整组关键义务覆盖；2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77 Memory Read Recency→累计披露](../../../../books/part-07-agent/77-memory.md)；实际正文与非作者写后通过 |
| [Revision, Not Restart: Revisable Visual Plans for Closed-Loop World–Action Models 2609.35439v1](https://arxiv.org/abs/2609.35439v1) | 2026-09-29T08:00:00+08:00 | 保存visual solver路径，用真实feedback修订未执行计划再解动作；2+2+3=7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 World-action→Future-to-Action](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过 |
| [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining 2609.35652v1](https://arxiv.org/abs/2609.35652v1) | 2026-09-29T08:00:00+08:00 | common endpoint loss下clean-head/velocity-head改变noise burden；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 固定点decoder→endpoint initialization](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过 |
| [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching 2609.35469v1](https://arxiv.org/abs/2609.35469v1) | 2026-09-29T08:00:00+08:00 | flow阶段绑定code可见性形成ordered increments而非物理因果；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 离散codec→粗planner/refiner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过 |
| [Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG 2609.35304v1](https://arxiv.org/abs/2609.35304v1) | 2026-09-29T08:00:00+08:00 | supporting-edge subset admission与明确baseline的模态交互诊断；2+1+3=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76 多模态admission→Escalation](../../../../books/part-07-agent/76-rag.md)；实际正文与非作者写后通过 |
| [MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems 2609.34496v1](https://arxiv.org/abs/2609.34496v1) | 2026-09-29T08:00:00+08:00 | initial→final proposal→aggregate分三层质量账；2+1+3=6 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82 Evaluation成本表→条件分支](../../../../books/part-07-agent/82-multi-agent.md)；实际正文与非作者写后通过 |

候选分母为43个唯一家族，已冻结。每篇arXiv绑定精确v1及官方New批次，重要修订不因版本号重计；机构事件依据原始RSS/核心发布时间。评分为Design Delta/System Reach/Durability，不计可靠性、访问、读成本或Books决定。5–6分的整合项因实际长期owner缺口定点深入；三项仅报告已标准审阅。每项证据及具体采用/不采用理由如下，不用最多三条跨材料分析替代逐项审阅。

## 4. 证据与知识整合

43项均完成独立准入校准与必要证据处置，40项已实际整合、3项仅报告。原19项未变化的有效审阅与写后结果复用；新增24项按具体命题分批核验，不将复用记录称为重新全文审阅。以下逐项保留支持、反证、具体owner与最终处置。

### [TopoEP 2609.35481v1](https://arxiv.org/abs/2609.35481v1)

[N1必要证据](../_sources/daily-20260929/screening-checkpoint.md#n1--topoep-260935481v1)核§2.4/3–6。相同routing矩阵的确定性device planner省host往返/plan广播，不省输入collective；跨domain正收益副本与域内细化不改logical top-k，authoritative optimizer/梯度仍归home。截层H800对照的uniform路由退步、slot/搬运与two-stream成本不作普遍最佳；当前短loss不证明能力全保。[Ch36实际两段](../../../../books/part-04-training-system/36-distributed-training.md)弥补MoonEP尚未解释的跨域规划分权，root实际703/705及前后写后PASS，原Cobalt历史coactivation分支保留。

### [WavePP 2609.35263v1](https://arxiv.org/abs/2609.35263v1)

[N2必要证据](../_sources/daily-20260929/screening-checkpoint.md#n2--wavepp-260935263v1)核§3.2/4–6。共同可恢复endpoint与lease不是时间expiry；suffix backing预留、victim替换、endpoint降低后容量重算先于schedule，但evict/copy/allocation延后各stage执行前完成，不是持久分布式事务。有限PP配置、含cached input吞吐和低并发/p95反退保留。[Ch45实际两段](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)接05219稀疏checkpoint后，root1008/1010及前后写后PASS；仅补跨stage资源承诺，不把调度公平性/SLO接管为cache保证。

### [TempoKV 2609.35065v1](https://arxiv.org/abs/2609.35065v1)

[N3必要证据](../_sources/daily-20260929/screening-checkpoint.md#n3--tempokv-260935065v1)核§3–5：claim不触发I/O或授容量；runtime TTU按state已ready估计、避免把自身缺状态造成的延迟用于延期，provider TTR不含等待容量或GPU transfer。Eligibility与capacity grant不同，commit后仍须保引用到I/O/GPU消费结束。有限CXL/单GPU对照减少的是protected byte-time而非物理occupancy，旧策略部分更快。[Ch45两段](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)接prefetch23049后，root已实际写后通过；原需求取回与早stage路径保留，不外推普遍SLO。

### [Nereus 2609.34645v1](https://arxiv.org/abs/2609.34645v1)

[N4必要证据](../_sources/daily-20260929/screening-checkpoint.md#n4--nereus-260934645v1)核§4.3/5–7及Table5：TP/PP依赖封在model-stage replica内、DP在外复制，跨stage DAG按release-before-acquire且读取source后才释放。急迫切换可跳payback而不能跳feasibility；最后copy与inflight policy语义仍由恢复/训练框架承载。有限同构ZeRO0布局和真实数据构造trace、短训练结果不授任意parallel/fault/bitwise保证。[Ch36两段](../../../../books/part-04-training-system/36-distributed-training.md)接22614后，root实际1426/1428与前后写后通过，保原checkpoint与固定pool分支。

### [EfficientAgent 2609.33762v1](https://arxiv.org/abs/2609.33762v1)

[N5必要证据](../_sources/daily-20260929/screening-checkpoint.md#n5--efficientagent-260933762v1)核§3–5/AppA–B：LRU的条件oracle命题不授在线working-set估计同保证；host full且evict压力下写resident prefix小extension、拒大refill，压力解除恢复writeall。固定filter在大池退步，H800测得offload也更慢。固定token回放包括tool等待而不授自由生成质量。[Ch45两段](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)实际314/316及初Eviction→ContextResidency已获root写后通过，补整个pool压力条件而不删除语义历史。

### [AgentReplay 2609.32283v1](https://arxiv.org/abs/2609.32283v1)

[N6必要证据](../_sources/daily-20260929/screening-checkpoint.md#n6--agentreplay-260932283v1)核§3–6：正常forward/LMhead/sampling后、nextstate前提交recordedtoken，logicalexpert hook不固定placement/batching，toolduration只模拟依赖等待不重effect。有限轨迹显示length-only可分别高估prefill/低估decode，不认证小模型能力、lossyKV质量或speculative路径。[Ch66两段](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际704/706及Runtime→AgentOutcome已获root写后通过，保内容不敏感的length-only基线。

### [Introducing dots](https://openai.com/index/introducing-dots/)

[N7必要证据](../_sources/daily-20260929/screening-checkpoint.md#n7--introducing-dots)核只读proactive/active动作review/身份与pilot核心。已受理后台任务可持续，但无人交互的新发现仅在数据scope中读取/建议，不能默认发消息、修改app或控制browser。公开功能合同不证明review无漏判或pilot普遍上线。[Ch84实际575/577](../../../../books/part-07-agent/84-agent-platform.md)与Omni→Scheduling交接root写后通过，保旧明确委派任务的执行寿命。

### [Towards safety cases for frontier AI training](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/)

[N8必要证据](../_sources/daily-20260929/screening-checkpoint.md#n8--towards-safety-cases-for-frontier-ai-training)核§1–3：前提失效暂停全部covered runs、monitor不能由被训练对象自禁，generated data/grading的downstream影响不因回退权重自动撤销。此为正在实施的建议/north star，不作部署认证或风险零保证。[Ch72实际645/647](../../../../books/part-06-ai-infrastructure/72-security.md)与SafetyEval前后root写后通过，继续保独立release、run与prompt权限。

### [How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/)

[N9必要证据](../_sources/daily-20260929/screening-checkpoint.md#n9--how-we-will-do-better-for-australia)核官方事件/response/change核心：benign统计目的仍转向非公开系统访问，但未发现个人病历访问；承认等待完整调查再初步通知有失误。当前监控可检测是厂商counterfactual、不是独立测试。[Ch72实际105/107](../../../../books/part-06-ai-infrastructure/72-security.md)与n-days→匿名交接root写后通过，采用初步known/unknown通知与最终归因分账，未扩泄漏事实。

### [Read-Blindness 2609.35630v1](https://arxiv.org/abs/2609.35630v1)

[必要证据与边界](../_sources/daily-20260929/screening-checkpoint.md) §3–6 Gram两侧、signed写入反侧、有限干预与local AdamW；proxy非精确null，跨checkpoint时间顺序不授因果或全程增长保证。 [实际owner](../../../../books/part-02-model/17-transformer-layer.md)新增读敏感、写增量与累积的不同权限的具体差额；root亲读必要原文、实际Ch17:197/199及前后交接，非作者写后PASS，旧路径/反侧保留，未复现。

### [Entity Copy 2609.35663v1](https://arxiv.org/abs/2609.35663v1)

[必要证据与边界](../_sources/daily-20260929/screening-checkpoint.md) §2–5三pass/边干预与恢复对照；单Qwen/有限模板下的necessary/sufficient不授一般早层删除或context无信息。 [实际owner](../../../../books/part-02-model/14-self-attention.md)新增context参与准备路由不等于原生context读出提供答案的具体差额；root亲读必要原文、实际Ch14:231/233及前后交接，非作者写后PASS，旧路径/反侧保留，未复现。

### [Rubric IRT 2609.35646v1](https://arxiv.org/abs/2609.35646v1)

[必要证据与边界](../_sources/daily-20260929/screening-checkpoint.md) §3–5正单调/条件独立与局部Fisher界；MAP不继承likelihood保证，半预算退步、RPN校准/judge成本保留。 [实际owner](../../../../books/part-04-training-system/31-rlhf.md)新增条件latent测量与冻结测量器的criterion信息预算的具体差额；root亲读必要原文、实际Ch31:208/210及前后交接，非作者写后PASS，旧路径/反侧保留，未复现。

### [SparseOPD 2609.34386v1](https://arxiv.org/abs/2609.34386v1)

[必要证据与边界](../_sources/daily-20260929/screening-checkpoint.md) §2–4/B4保聚合mass/zero-sum而非exact densegradient；full forward/backbone仍需，extra backward allocation不等总显存收益，完整step反而更慢。 [实际owner](../../../../books/part-04-training-system/29-sft.md)新增全correction观察和有符号稀疏head微分分离的具体差额；root亲读必要原文、实际Ch29:389/391及前后交接，非作者写后PASS，旧路径/反侧保留，未复现。

### [ProbeQuant 2609.33923v1](https://arxiv.org/abs/2609.33923v1)

[必要证据](../_sources/daily-20260929/screening-checkpoint.md) §3–4.6线性trace与非线性传播分开，真实activation局部目标更准确不保证混合位宽模型更好；budget低估/完整文件与成本独立验收。 [实际owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)补isolated uncertainty、input secondmoment与downstream目标不同权限的具体差额，root已亲读必要原文、实际Ch49:851/853及前后写后PASS；旧路径保留，未复现。

### [Reset Is Not Recovery 2609.33672v1](https://arxiv.org/abs/2609.33672v1)

[必要证据](../_sources/daily-20260929/screening-checkpoint.md) §3–8/10 aggregate标准非逐item恢复率；pressure和自己旧answer混杂，gold/delete仅诊断上界。 [实际owner](../../../../books/part-07-agent/75-context.md)补reset事件不等于effectivecontext恢复，以pairedclean核残余影响的具体差额，root已亲读必要原文、实际Ch75:549/551及前后写后PASS；旧路径保留，未复现。

### [LLaDA-Guard 2609.33634v1](https://arxiv.org/abs/2609.33634v1)

[必要证据](../_sources/daily-20260929/screening-checkpoint.md) §3–4/B1/G learned下界不继承true NP证书；sameweights scoring不证训练因果，多mask成本/误拒/泄漏保留。 [实际owner](../../../../books/part-06-ai-infrastructure/72-security.md)补labelconditional重构证据域与verdict权限的具体差额，root已亲读必要原文、实际Ch72:546/548及前后写后PASS；旧路径保留，未复现。

### [World-Model Post-Training Audit 2609.33335v1](https://arxiv.org/abs/2609.33335v1)

[必要证据](../_sources/daily-20260929/screening-checkpoint.md) §2–4/A1–2仅ALFWorld/VWA；GT/MIS固定recipe非全cost，COIN不授普遍randomreward有效。 [实际owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)补正确预测内容与额外优化、selection与coverage归因拆开的具体差额，root已亲读必要原文、实际Ch25:731/733及前后写后PASS；旧路径保留，未复现。

### [Perturbed Documents 2609.33642v1](https://arxiv.org/abs/2609.33642v1)

[必要证据](../_sources/daily-20260929/screening-checkpoint.md) §2–4文档改写与teacher/judge仅依赖proxy，不证无记忆/无污染；teacher选择/RL有退步，构造非免费。 [实际owner](../../../../books/part-04-training-system/27-data.md)补同question/rubric的with/without文档双侧admission门的具体差额，root已亲读必要原文、实际Ch27:1008/1010及前后写后PASS；旧路径保留，未复现。

### [Event-Set Completion Distillation 2609.34738v1](https://arxiv.org/abs/2609.34738v1)

[必要证据](../_sources/daily-20260929/screening-checkpoint.md) §3–5 native mass与emptyset loss0；COUF局部，99%是16轨迹visitedmass，非全任务。 [实际owner](../../../../books/part-04-training-system/29-sft.md)补实际child completion集合总概率不同于单token配给的具体差额，root已亲读必要原文、实际Ch29:261/263及前后写后PASS；旧路径保留，未复现。

### [Torch-PIM 2609.34657v1](https://arxiv.org/abs/2609.34657v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34657v1) §4.1–4.4/5–6 的必要证据与直接反侧：Loop/nest 与 allocation/alias 绑定后再比较实际 host 时间与保守 PIM 上界；实 CPU+模拟 PIM、同集合阈值拟合和非单调/变慢反侧均保留，不授实芯服务加速。逐 nest 与更细 basic-block 的成本分开。

与现有正文相比，新增的是“Lowering 产生的实际 loop nest 决定放置候选域与 host profile 权限”而非同主题材料列表；已落实到 `INFER-TENSORRT-LLM` [Ch49 lowering→dequantization](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_N20_23_PRE.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [SpecStream 2609.33184v1](https://arxiv.org/abs/2609.33184v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.33184v1) §4.1–4.3/5 的必要证据与直接反侧：CPU 复制成功才推进 history 边界并回收 GPU；每 query/head 各自 m/l/a，在共同 reference 下合并。同 GPU draft 逐 token ACK/时限准入不隔离 L2/带宽；质量接近不授 bitwise，acceptance 增仍可能吞吐降，长历史逊全GPU路径。

与现有正文相比，新增的是“仅迁移已提交历史、多 query 流式验证与 target 优先准入”而非同主题材料列表；已落实到 `INFER-SPECULATIVE-DECODING` [Ch48 memory-budget→drafter](../../../../books/part-05-inference-system/48-speculative-decoding.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_N20_23_PRE.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Planarian 2609.35366v1](https://arxiv.org/abs/2609.35366v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35366v1) §4.3–4.5/6.1–6.3 的必要证据与直接反侧：支持域内先拒不可补偿请求、SQL pre-image/日志绑定，再等 inflight、冻结并 capture；这不是恢复成功证书。仅逆序 undo 的远端不允许 children 并发共用变更，真正分支需 service-side 支持；tenant 隔离、锁/日志成本和人工 reconciliation 保留。

与现有正文相比，新增的是“预先可补偿操作与 tool-boundary 联合 capture，不自授远端 fork”而非同主题材料列表；已落实到 `AGENT-WORKFLOW` [Ch81 AgentRewind→Waypoint](../../../../books/part-07-agent/81-workflow.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_N20_23_PRE.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Dynamic Flow, Static Graph 2609.34727v1](https://arxiv.org/abs/2609.34727v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34727v1) §4/7 的必要证据与直接反侧：非前缀近似复用与 exact prefix 分开，新 token 总需重算；离线 per-graph latency 驱动有限 DP，不是按调用次数或复用率直接授收益。Qualcomm/小模型的 QA 退步、全部复用更差、profiling/搬运成本与 full-prefill fallback 保留。

与现有正文相比，新增的是“固定图容纳选择性 KV 重算，并按实测调用成本规划 chunks”而非同主题材料列表；已落实到 `INFER-TENSORRT-LLM` [Ch49 静态图→基础优化](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_N20_23_PRE.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures 2609.34612v1](https://arxiv.org/abs/2609.34612v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34612v1) §3.2–3.4/4.1–4.4 的必要证据与直接反侧：phase/depth、expert pruning 与 SRAM/HBM 分工改变路径；prediction 是 hint，selection 少读不等释放 KV。模拟/综合非实芯，长序列无 sparse 反慢、uniform pruning 退步。Ch21/49/54 已解释质量/真实驻留/完整执行预算；新的局部 recipe 和联合模拟只保留报告，不声称全文已有。

最终仅报告，不把“已有相关原则”冒充整篇新实验已在书中。具体对照为 [Ch21](../../../../books/part-02-model/21-moe.md) 的phase/capacity、[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的联合编译与 [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) 的selection/驻留分账。 本次局部测量保留，不为制造diff重复机制。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_A.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation 2609.34351v1](https://arxiv.org/abs/2609.34351v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34351v1) §3/4 的必要证据与直接反侧：access-matrix nullspace 暴露 reuse；affine realignment/pre-tiling 将其变成阵列可映射结构，不把降低 macro traffic 当完整执行加速。CNN 模拟、微弱/退步收益、浮点非 bitwise、离线与成熟编译 fallback 保留。

与现有正文相比，新增的是“非轴向 reuse 先仿射 realignment，再映射有限 CIM/layout”而非同主题材料列表；已落实到 `INFER-TENSORRT-LLM` [Ch49 Nautilus→Persistent Executor](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_A.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection 2609.34663v1](https://arxiv.org/abs/2609.34663v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34663v1) §II/III-A–C及评价反侧的必要证据：同一 batch/slot 配置改变逐步成本也改变重返时点，dummy/cache 共池与真实请求互相作用。先共同优化 bucket 与 active membership，而非独立最大 batch；有限静态 backend 的代理成本不等实际 occupancy/SLO，原动态策略共存。

与现有正文相比，新增的是“静态 bucket 与内生 tool re-arrival 联合决定 padding/驻留成本”而非同主题材料列表；已落实到 `INFER-CONTINUOUS-BATCHING` [Ch46 trade-off→工程判断](../../../../books/part-05-inference-system/46-continuous-batching.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_A.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions 2609.35569v1](https://arxiv.org/abs/2609.35569v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35569v1) §2 Eq2–6及实验边界 的必要证据与直接反侧：固定地域/时间/正强度时运营能量与排放排序相同；跨部署寿命/embodied 差额才可能改排序，pairwise crossover 不授全候选最优。sunk fleet 与新采购分账，固定系数/寿命假设、数据不确定及实际路由权限保留。

与现有正文相比，新增的是“固定部署运营排序与跨部署 embodied crossover 分账”而非同主题材料列表；已落实到 `PLATFORM-COST` [Ch70 Unit Economics 生命周期→需求反弹](../../../../books/part-06-ai-infrastructure/70-cost.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_A.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference 2609.35188v1](https://arxiv.org/abs/2609.35188v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35188v1) §3.1–3.5/4.3–4.4 的必要证据与直接反侧：Gemma4-E4B W4A16/assistant、depth2、单A10G单请求、9 prompts×20 repeats×2；AR先于MTP，profile与clean测量分开。GEMM单次不快但有效token摊销下降，是Ch48/49已有机制的局部验证，不构成新长期结论或生产SLO，故仅报告。

最终仅报告，不把“已有相关原则”冒充整篇新实验已在书中。具体对照为 [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 的每target forward有效token及验证成本、[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的launch/graph分账。 本次局部测量保留，不为制造diff重复机制。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_A.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory 2609.34380v1](https://arxiv.org/abs/2609.34380v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34380v1) IV-A–D/Alg1/V 的必要证据与直接反侧：residual 全部恢复后才提交 full，一个 forward 共用模式但请求历史可混精度；KV mapping 保留避免 inflight/free race。effective pass@1 含SLO而非纯质量，低压力/静态FP8反侧、host传输/graph成本保留。

与现有正文相比，新增的是“persistent weights/residual/KV 非对称共享与 forward 模式提交”而非同主题材料列表；已落实到 `INFER-GPU-MEMORY` [Ch54 双模式 Weight 与 KV](../../../../books/part-05-inference-system/54-gpu-memory.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_B.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding 2609.33889v1](https://arxiv.org/abs/2609.33889v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.33889v1) §3–7 的必要证据与直接反侧：full weights/KV 仍驻留，省读取不授容量；batch union/dtype 改 byte crossing，校准 kernel/selection 改 latency crossing。同高效 dense 对照、远距检索反侧、PPL不等任务等价与短输出摊销保留，不给固定context阈值。

与现有正文相比，新增的是“weight-read/KV-read 的 byte 交点还须质量和 kernel 成本校准”而非同主题材料列表；已落实到 `INFER-GPU-MEMORY` [Ch54 少读 Weight 与少读 KV 的交点](../../../../books/part-05-inference-system/54-gpu-memory.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_B.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs 2609.33477v1](https://arxiv.org/abs/2609.33477v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.33477v1) §4–7/9 的必要证据与直接反侧：group input sidecar 而非旧 exact state，完整attention KV 复用；页/transfer完成后发布，消费者wait各stream，缺失回full-prefill/live state直接复用。质量比不等token/state等价，OLMo/RULER及exact-hit性能退步、graphs/headroom成本保留。

与现有正文相比，新增的是“按 linear group 保存输入锚点，近似 replay 与发布边界分开”而非同主题材料列表；已落实到 `INFER-KV-CACHE` [Ch45 Group 输入锚点→Video cache](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_B.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification 2609.34785v1](https://arxiv.org/abs/2609.34785v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34785v1) §3–4/B.4–5 的必要证据与直接反侧：输入/reset/输出mapping固定，顺序默认保留、仅spec授权重排，timing另验；agent自写RTL与BehaviorIR一致不授真值。有限stimulus pass、coverage和bounded/unknown分开，支持面窄、不采用曲线算法因果或真实芯片交付。

与现有正文相比，新增的是“允许 transaction timing 差异但双产物都须独立 hidden gold”而非同主题材料列表；已落实到 `PLATFORM-EVALUATION-SYSTEM` [Ch66 Transaction oracle→Dense Process](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_B.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization 2609.35508v1](https://arxiv.org/abs/2609.35508v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35508v1) §2–4 的必要证据与直接反侧：五victim×四perturber×三repeats的60干扰样本不授生产false-alarm；missing tree导致pf_cow abstain不等健康，微probe成本不等全服务无开销。Ch69已有reference/deviation只作候选和call-chain/干预分权；新工程矩阵仅报告，不说全文已覆盖。

最终仅报告，不把“已有相关原则”冒充整篇新实验已在书中。具体对照为 [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) 的同观测对象reference、deviation仅作候选与call-chain/干预验证。 本次局部测量保留，不为制造diff重复机制。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_B.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Hardware-Aware Features for CUTLASS Kernel Selection 2609.35587v1](https://arxiv.org/abs/2609.35587v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35587v1) §3–5/5.5 的必要证据与直接反侧：静态合法性筛选的有限catalog只提出选择，实际编译/执行须验收；布局同base shape留出，shortlist best不同近全量oracle。regret和execution coverage同报，FP8/fusion负侧、迁移目标测量成本保留，不把失败请求解释为全catalog空。

与现有正文相比，新增的是“candidate-induced 硬件代理排序、shape-group 留出与执行 coverage”而非同主题材料列表；已落实到 `INFER-TENSORRT-LLM` [Ch49 硬件行为代理→Tensor Core层级](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_TAIL_B.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Semantic Prefix Oracles 2609.35425v1](https://arxiv.org/abs/2609.35425v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35425v1) §2.2–4/6 的必要证据与直接反侧：稳定矛盾才安全剪枝，Live不提供completion witness；dead-end freedom/token lift另需productivity/type覆盖/拼写/词表。有限differential不等实现证明，STLC/tool反侧与syntax/compiler fallback保留，不授行为真值。

与现有正文相比，新增的是“语义 prefix 安全剪枝与可完成性是两份合同”而非同主题材料列表；已落实到 `INFER-SGLANG` [Ch51 Structured Generation→Adapter readiness](../../../../books/part-05-inference-system/51-sglang.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_TAIL.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Rubric-Calibrated Preferences 2609.35739v1](https://arxiv.org/abs/2609.35739v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35739v1) §3.1–3.4/4.1–4.5/6 的必要证据与直接反侧：共享2PL rubric下正affine尺度保持query内顺序，criterion概率提供gain不是真值。单doc不含冗余/互补，同源judge偏差不消失，近差额/独立标签fallback保留；不重复Ch31的RL信息预算。

与现有正文相比，新增的是“query内BT排序与跨query单位/原点分开校准”而非同主题材料列表；已落实到 `PLATFORM-EVALUATION-SYSTEM` [Ch66 Judge Ranking→Route/defer](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_TAIL.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [SpeakGR 2609.35430v1](https://arxiv.org/abs/2609.35430v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35430v1) §3–5/Appendix B 的必要证据与直接反侧：学生text-only rollout，原base同prefix给teacher→student KL，text subset重归一；teacher不生成suffix，adaptive只改下一步权重。有限检索/文本、recall退步及matched-weight限制，不授全能力或完整RAG。

与现有正文相比，新增的是“扩SID词表后分开检索正确与原文本条件分布保护”而非同主题材料列表；已落实到 `TRAIN-SFT` [Ch29 Occupancy→共享Trace](../../../../books/part-04-training-system/29-sft.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_TAIL.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [TRACE 2609.33517v1](https://arxiv.org/abs/2609.33517v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.33517v1) §3/4.2–4.6/6/C.4–5 的必要证据与直接反侧：departure checkpoint/absence delta绑定epoch，预算内缺critical obligations就reset/block，private experience需source再准入。authenticated view不认证事实；显式替换未稳定领先、长缺席/漏失效反侧和成本保留。

与现有正文相比，新增的是“return epoch 下逐项有效不等整组关键义务覆盖”而非同主题材料列表；已落实到 `AGENT-MEMORY` [Ch77 Memory Read Recency→累计披露](../../../../books/part-07-agent/77-memory.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_TAIL.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Revision, Not Restart: Revisable Visual Plans for Closed-Loop World–Action Models 2609.35439v1](https://arxiv.org/abs/2609.35439v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35439v1) §3–5 的必要证据与直接反侧：facts/旧proposal、root坐标和checkpoint分离，Bridge冻结velocity+residual修未执行prefix，所有模式按当前事实重解action。经验discrepancy不是安全，均值降伴p95升、消融归因有限及任务退步保留；独立controller拥有提交。

与现有正文相比，新增的是“保存visual solver路径，用真实feedback修订未执行计划再解动作”而非同主题材料列表；已落实到 `MULTIMODAL-EMBODIED-VLA` [Ch26 World-action→Future-to-Action](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_ROOT_PREP.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining 2609.35652v1](https://arxiv.org/abs/2609.35652v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35652v1) §3/4/6.1–6.3 的必要证据与直接反侧：输出parameterization不等objective/sampling空间；同网络/数据/noise/loss且no raw-input skip的低秩条件比较。synthetic allocation给定不等学会协调，有限机器人消融有退步，不授普遍head优势或物理安全。

与现有正文相比，新增的是“common endpoint loss下clean-head/velocity-head改变noise burden”而非同主题材料列表；已落实到 `MULTIMODAL-EMBODIED-VLA` [Ch26 固定点decoder→endpoint initialization](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_ROOT_PREP.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching 2609.35469v1](https://arxiv.org/abs/2609.35469v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35469v1) §3–5/Appendix C 的必要证据与直接反侧：noise起点全部codes可读，随后移前留后，早影响存在action state；decoder/tokenizer冻结而AR CE仍更新backbone。matched annealing和native swap支持阶段效应，不授唯一语义/物理因果，更多codes与具体任务退步保留。

与现有正文相比，新增的是“flow阶段绑定code可见性形成ordered increments而非物理因果”而非同主题材料列表；已落实到 `MULTIMODAL-EMBODIED-VLA` [Ch26 离散codec→粗planner/refiner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_ROOT_PREP.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG 2609.35304v1](https://arxiv.org/abs/2609.35304v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.35304v1) §3–6.2/7–8 的必要证据与直接反侧：只将允许subset支持的edge/chunks交reader，在固定图/排序下测贡献与合作。V∅是组内most-frequent gold predictor不是空context；负交互不独辨冗余/干扰，有限两模态DocVQA/CI切片不授固定淘汰或部署router。

与现有正文相比，新增的是“supporting-edge subset admission与明确baseline的模态交互诊断”而非同主题材料列表；已落实到 `AGENT-RAG` [Ch76 多模态admission→Escalation](../../../../books/part-07-agent/76-rag.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_ROOT_PREP.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

### [MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems 2609.34496v1](https://arxiv.org/abs/2609.34496v1)

采用 [精确v1 HTML](https://arxiv.org/html/2609.34496v1) Multi-Layer Metrics/Experiments/Ablation 的必要证据与直接反侧：与strongest initial、各proposer初终及strongest final分别比较，AL可负，dynamic episode和state decision分母不同。共同backbone/代理分数/不等tokens不授一般因果，CLEARS w/oCCE预算混杂仅报告；保equal-budget单agent与独立verifier。

与现有正文相比，新增的是“initial→final proposal→aggregate分三层质量账”而非同主题材料列表；已落实到 `AGENT-MULTI-AGENT` [Ch82 Evaluation成本表→条件分支](../../../../books/part-07-agent/82-multi-agent.md)，原论证与回退条件保留，实际写入经非作者POST通过。完整范围、评价条件及反证见 [必要审阅记录](../_sources/daily-20260929/V3_THEME_ROOT_PREP.md)。性能/质量结果是作者披露而非本项目复现；未披露的部署条件为 Not Disclosed，不据此授跨配置结论。

## 5. 缺口与下一步

本窗普通扫描、候选证据与必要Books待办为0，最终独立整日报告验收已通过。以下 **7组外部终态保留项** 均不支持正面Coverage/Evidence、Books、零遗漏或安全/性能保证，未列入43候选，不能算零命中。同一身份只请求一次：

1. [Anthropic Sonnet5.5](https://www.anthropic.com/claude-sonnet-5-5)：只有Sep28日级原值，缺first-public时刻/时区，可能跨本窗起点；需官方带时区发布时间或可绑定事件的发布批次约定。无日期正文不能替代；到达仅重开此事件落窗及模型/安全合同判断。
2. [Google Research Publications](https://research.google/pubs/)：年度/标题排序无法恢复该24小时切片；需官方本窗增量列表/可定位分页快照及日期字段。到达只筛新增具名条目，不重读历年论文；Blog已核不代替这个目录。
3. [Meta Blog](https://ai.meta.com/blog/)：首页混排序、限定搜索零结果不能证明历史窗口无发布；需官方日期有序窗口列表、分页快照或本窗发布条目。到达只恢复本窗技术发布筛选。
4. [Qwen Research](https://qwen.ai/research)：动态目录/detail和旧官方Blog替代不能恢复本窗公开条目；需官方本窗列表/原文链接及公开时间。到达只处理该范围的独立事件，不能从shell推零。
5. [Seed Blog](https://seed.bytedance.com/en/blog)：en/zh入口动态shell，论文目录已核但不证明Blog；需官方本窗Blog条目和发布时间/可读快照。到达只重开这组Blog，不重扫已核public_papers。
6. [MiMo Blog](https://mimo.xiaomi.com/)：ToolCallRepetition、V2.6、MiMoCode、V2.5UltraSpeed、FullPipelineInference五个具名卡缺原始公开日期；定点/rl/与/mimocode/仍无可归属时间正文。需这些卡的官方带日期原文或页面/接口快照与时区约定；不得用CDN Last-Modified或抓取时间。先唯一身份/落窗，只有符合本窗且有增量的再审阅，五卡不等五贡献候选。
7. [MiniMax CLI0.5.8](https://agent.minimax.io/docs/changelog.md)：Sep28日级且无时区/时刻，stop终止后台而switch/clear保留是真实生命周期信号，不能按普通bugfix关闭；需绑定0.5.8的官方release timestamp/发布批次及时区。到达仅重开落窗及任务寿命命题；不先评分/写书，不重跑CLI全历史。

RiKFAD [2609.30342v2](https://arxiv.org/html/2609.30342v2) 当前必要方法/理论仍支持已采用的v1命题，未见要求改变设计的实质信号，版本事件关闭、不重复评分；不是宣称全篇逐字相同。[Google CustomAgents](https://antigravity.google/blog/custom-agents-in-google-plugins)为既有roles/plugins包装，无新增执行或验证保证：Flutter可改代码、Firebase可写rules，只有Play示例read-only/plan；已纠正“全体只读”的过宽概括。CLI0.5.9后台计数/字节/UI局部修复贡献前关闭，不为处置无影响的日期穷查材料。窗外旧Mon28发现只保留真实归属和有效证据，没有为了扩大本日分母重列或制造Books差额。

## 6. 复核

复核者：sep29_four_pre（非报告作者）。

结论：通过

验收时间：2026-10-01T19:10:21+08:00，详见[独立日级验收](../_sources/daily-20260929/V3_FINAL_REVIEW.md)。43项日期、贡献、评分与必要证据均有最终处置；40项实际Books写入的非写入作者POST链闭合，3项仅报告保留具体理由。原19项未变化的有效审阅与写后结果复用，新增24项分批核验；14来源有限停止与7外部隔离核齐。

负侧复核直接抽检7个论文/官方事件的完整题摘或核心材料，并复用RiKFAD当前必要方法及既有owner的独立核验；范围与排除理由见验收记录。不声称读完全部原始分类摘要、无关附件或历史版本，不声称全站无遗漏。V3格式、130本地链接及23 Stable owner检查通过，未暂存diff-check通过；已有暂存区空白告警保留。格式检查不代替上述语义验收；未stage、commit或push。
